---
title: "Pioneering with Embedded Swift (Part 2: Zero-Allocation Byte Parsing)"
date: 2026-08-13
authors:
  - abagher
categories:
  - Firmware
  - Embedded Swift
---

We were feeling pretty confident. We had compiled bare-metal Embedded Swift, linked it against the Raspberry Pi Pico 2 SDK, and verified our core RPN engine inside a simulated environment. The simulated screen drew the stack, the keys responded, and our unit tests passed. But as software engineers driven by the conviction that RPN calculators are mathematically superior—and that it is an absolute injustice that more students and engineers do not use them—we wanted our calculator to run forever without a hitch. So we turned on our automated keystroke fuzzer. At operation 1,214, the calculator died cold with an unhandled hard fault (`isr_hardfault`).

<!-- more -->

## Discovering the Heap Exhaustion Leak

In modern iOS and macOS development, memory is cheap, dynamic allocations are practically invisible, and Automatic Reference Counting (ARC) quietly cleans up after you. On the RP2350, however, we were working with just 264 KiB of total SRAM—out of which we had carved a modest 220 KiB heap pool. In software, memory is abundant; on bare-metal microcontrollers, even the tiniest memory leak is a ticking time bomb.

To track down where our RAM was evaporating without the benefit of expensive lab hardware, we enabled memory allocation tracing in the Pico SDK by passing `PICO_DEBUG_MALLOC=1` and streaming telemetry over the serial port. Watching the console log allocations in real time was sickening. Every single button press produced an upward staircase of small, orphaned chunks:

```
[MALLOC] ptr=0x2001a4f0 size=32  total_allocated=4128  active_blocks=84
[MALLOC] ptr=0x2001a520 size=48  total_allocated=4176  active_blocks=85
[MALLOC] ptr=0x2001a560 size=32  total_allocated=4208  active_blocks=86
...
[PANIC] Out of memory: malloc failed for 64 bytes at Main.swift:88
```

Nobody was calling `free()`. But more importantly, why was a basic calculator engine touching the heap on every keystroke in the first place?

## Root Cause: Dynamic `String` Construction

We traced the allocations straight into `CalculatorEngine.commitInput()`. Coming from high-level Swift, our early implementation took what seemed like the most readable, idiomatic path to parse input into a floating-point number:

```swift
// The leaking implementation:
let str = String(decoding: currentInputBuffer, as: UTF8.self)
if let val = Double(str) {
    push(val)
}
```

On macOS or iOS, creating a short-lived `String` is optimized down to SSO (Small String Optimization) or swept clean by ARC autorelease pools. In Embedded Swift on ARMv6-M, however, strings spanning multi-byte UTF-8 representations trigger heap allocations via the underlying allocator. Without thread-exit collectors or an ARC cycle collector running in background threads, the micro-heap of 220 KiB eventually fragmented into complete exhaustion.

Furthermore, in `LFUManager.swift`, dynamic hashing inside `Dictionary<String, Int>` caused persistent allocations on every function invocation. We addressed this by guarding usage tracking:

```swift
public func recordUsage(of function: String) {
    #if hasFeature(Embedded)
    // Avoid dynamic dictionary hashing and allocation on bare metal
    return
    #endif
    // Host tracking implementation follows...
}
```

```mermaid
graph TD
    subgraph "Leaking Pipeline (Heap Dependent)"
        RawIn1[Raw Key Buffer] --> StrInit[String decoding: as: UTF8]
        StrInit --> HeapAlloc[malloc 32/48 bytes]
        HeapAlloc --> SwiftDbl[Double init str]
        SwiftDbl --> Leak[ARC Retain Leak on Cortex-M33]
    end
    subgraph "Zero-Allocation Pipeline (Pure Byte Inspection)"
        RawIn2[Raw Key Buffer UnsafePointer<UInt8>] --> ByteScan[fastMatchOp byte-by-byte]
        ByteScan --> MatchOp{Length & Byte Match?}
        MatchOp -- Multi-byte UTF-8 --> OpEnum[CalculatorOperation Enum]
        MatchOp -- ASCII Digits --> IntMath[Scalar Horner Math result * 10 + d]
        IntMath --> ZeroAlloc[0 Mallocs / 0 Leaks / 0 Heap Overhead]
        OpEnum --> ZeroAlloc
    end
```

## The Zero-Allocation Solution: `fastMatchOp`

The fix was uncompromising: banish dynamic `String` construction entirely from our hot calculation loop. We prompted an AI coding assistant to help us design an allocation-free scanner that could inspect raw byte buffers directly. The result was `fastMatchOp`, which operates directly on raw memory pointers:

```swift
func fastMatchOp(_ buf: UnsafePointer<UInt8>, _ len: Int) -> CalculatorOperation? {
    if len == 0 { return nil }
    let b0 = buf[0]
    let b1 = len > 1 ? buf[1] : 0
    let b2 = len > 2 ? buf[2] : 0
    let b3 = len > 3 ? buf[3] : 0
    let b4 = len > 4 ? buf[4] : 0
    let b5 = len > 5 ? buf[5] : 0
    let b6 = len > 6 ? buf[6] : 0

    // Multi-byte Unicode mathematical operators
    // "→cm" UTF-8: [226, 134, 146, 99, 109]
    if len == 5 && b0 == 226 && b1 == 134 && b2 == 146 && b3 == 99 && b4 == 109 { return .toCm }
    // "√𝑥" UTF-8: [226, 136, 154, 240, 157, 145, 165]
    if len == 7 && b0 == 226 && b1 == 136 && b2 == 154 && b3 == 240 && b4 == 157 && b5 == 145 && b6 == 165 { return .sqrt }
    // "𝑦ˣ" UTF-8: [240, 157, 145, 166, 203, 163]
    if len == 6 && b0 == 240 && b1 == 157 && b2 == 145 && b3 == 166 && b4 == 203 && b5 == 163 { return .power }
    
    // ASCII Standard Operations
    if len == 1 && b0 == 43 { return .add }         // '+'
    if len == 1 && b0 == 45 { return .subtract }    // '-'
    if len == 1 && b0 == 46 { return .decimal }     // '.'
    if len == 1 && b0 >= 48 && b0 <= 57 {           // '0'..'9'
        return .digit(Int(b0 - 48))
    }
    return nil
}
```

Integer and fraction parsing was similarly rewritten to compute numerical values via pure Horner scalar math (`result = result * 10 + Int(c - 48)`), eliminating intermediate string objects entirely.

| Memory Metric | Leaking `String` Parser | Zero-Allocation `fastMatchOp` |
| :--- | :--- | :--- |
| **Heap Allocations per Keystroke** | 2 to 4 `malloc()` calls | **0 calls** |
| **Active Heap Growth (10,000 ops)** | +128 KiB (fragmentation crash) | **0 bytes (flatline)** |
| **Execution Latency per Match** | $14.2\,\mu\text{s}$ | **$0.48\,\mu\text{s}$ (30x faster)** |
| **Deterministic Timing** | Variable (heap scan jitter) | Constant time ($O(1)$) |

With direct byte inspection in place, our fuzzer ran past 100,000 continuous operations without allocating a single byte on the heap.

## Conclusion: Hard-Learned Heuristics for Embedded Swift Memory

If you are running Embedded Swift on bare silicon, treat the dynamic heap as a dangerous luxury. Coming from software where memory feels infinite, adjusting to 264 KB of SRAM forced us to rethink every abstraction:
- Treat `String` as radioactive in hot loops; parse raw `UnsafePointer<UInt8>` buffers directly.
- Multi-byte Unicode mathematical symbols (`√𝑥`, `𝑦ˣ`) should be matched against their fixed UTF-8 byte sequences.
- Keep the runtime heap flatlined at zero bytes during active calculation. When there are zero allocations, there are zero memory leaks, zero fragmentation traps, and zero garbage collection spikes. Building a bulletproof, low-cost RPN calculator means ensuring every byte of silicon serves the user reliably.
