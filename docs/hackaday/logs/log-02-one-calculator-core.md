---
title: "Log 02: One Core to Rule Them All: Swift Package to Bare-Metal Silicon"
description: "How RPNCore compiles across Apple Watch, iPhone, and bare-metal RP2350."
---

# Log 02: One Core to Rule Them All: Swift Package to Bare-Metal Silicon

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// HACKADAY BUILD LOG 02 · EMBEDDED SWIFT</div>

**Canonical Article:** [One Calculator Core for Watch, Phone, and RP2350](../../blog/posts/2026-09-22-one-calculator-core-watch-phone-rp2350.md)  
**Topic:** Clean-Room Systems Architecture & Embedded Swift  
**Artifact:** Shared `RPNCore` Architectural Model & Target Matrix

---

## 1. The Engineering Lesson
Maintaining separate calculator logic across different platforms is a recipe for divergence: rounding discrepancies, subtle order-of-operation bugs, and stack lift mismatches between app and hardware.

We built a single clean-room engine (`RPNCore`) that compiles across three radically different execution environments:
1. **Darwin Host (iOS, iPadOS, macOS):** Rich SwiftUI interfaces, Metal rendering, high-level haptics.
2. **watchOS Target:** Highly optimized memory constraints, 40 Hz rendering budgets.
3. **Bare-Metal RP2350 Microcontroller (Cortex-M33):** Zero dynamic heap allocation, zero standard library dependencies, running bare-metal Embedded Swift 6.

```
+-------------------------------------------------------------------------+
|                           RPNCore (Swift Package)                       |
|           • Four-Level Stack Architecture (X, Y, Z, T)                  |
|           • Arbitrary-Precision Rational Fraction Engine                |
|           • HP-32SII Saturn CPU State Parity (Clean-Room)              |
+--------------------+--------------------------------+-------------------+
                     │                                │
                     ▼                                ▼
       [Darwin / SwiftUI Runtime]         [Embedded Swift 6 / ARM]
       • iOS & iPadOS (v1.1 Live)         • Bare-metal Cortex-M33
       • watchOS (Standalone)             • WebAssembly Emulator Loop
```

By decoupling state transitions from UI rendering, the core processes a stream of atomic key tokens (`.digit(5)`, `.enter`, `.operation(.add)`) and emits immutable display frame representations.

---

## 2. Concrete Artifact
The stack lift state machine ensures that entering a number immediately after a binary operation automatically pushes the previous result up the stack, exactly matching Corvallis hardware specifications:
```swift
// Stack Lift State Machine
public mutating func pushDigit(_ d: Int) {
    if stackLiftEnabled {
        t = z
        z = y
        y = x
        x = 0
        stackLiftEnabled = false
    }
    x = (x * 10) + Double(d)
}
```

---

## 3. Community Discussion Invitation
**To the Hackaday Community:**  
Have you experimented with **Embedded Swift** on microcontrollers like the RP2040/RP2350 or ESP32? How do you manage heap vs. static memory constraints when porting code from high-level environments down to bare silicon? Share your embedded toolchain experiences!
