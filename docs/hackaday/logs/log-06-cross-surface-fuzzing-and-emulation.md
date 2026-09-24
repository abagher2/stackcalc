---
title: "Log 06: Emulating the RP2350: Cross-Surface Differential Fuzzing at 40 Hz"
description: "Differential grammar fuzzing across Darwin, watchOS, and bare-metal RP2350 emulator."
---

# Log 06: Emulating the RP2350: Cross-Surface Differential Fuzzing at 40 Hz

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// HACKADAY BUILD LOG 06 · DIFFERENTIAL FUZZING</div>

**Canonical Article:** [Fuzzing the Firmware Path in an RP2350 Emulator](../../blog/posts/2026-09-22-fuzzing-the-firmware-path-in-an-emulator.md)  
**Topic:** Verification, Emulation & Differential Fuzzing  
**Artifact:** 40 Hz Grammar-Guided Differential Fuzz Harness

---

## 1. The Engineering Lesson
Waiting for physical PCBs to arrive before validating firmware is the slowest way to build hardware. But standard unit tests only check the scenarios the engineer remembered to write down.

To ensure mathematical and stack state parity across our Apple Silicon host, watchOS app, and bare-metal RP2350 firmware, we built an automated **cross-surface differential fuzzer**.

```
                           +------------------------+
                           | Grammar-Guided Fuzzer  |
                           |  (40 Keystrokes / Sec) |
                           +-----------+------------+
                                       │
                     ┌─────────────────┴─────────────────┐
                     ▼                                   ▼
        [Darwin Host Reference]             [Emulated RP2350 Core]
        • 64-bit IEEE 754 Engine            • ARM Cortex-M33 Binary
        • Native Swift 6 Runtime            • Custom Memory Layout
                     │                                   │
                     └─────────────────┬─────────────────┘
                                       ▼
                           [Differential State Checker]
                           • Checksum X, Y, Z, T Registers
                           • Flag Registers & Overflow Flags
                           • Bit-for-Bit Discrepancy Halt
```

### The Fuzzing Strategy
1. **Grammar Generation:** The fuzzer generates valid and degenerate mathematical keystroke streams: mixed fractions, nested square roots, transcendental edge cases, division by zero, stack overflow/underflow, and rapid clear/drop sequences.
2. **Lock-Step Execution:** Each keystroke token is dispatched simultaneously to the Darwin reference engine and the RP2350 software emulator.
3. **Automated Shrinking:** When a state discrepancy occurs, the harness minimizes the input sequence down to the minimal reproducible bug trace (e.g. `2 [ENTER] 0 [/] [DROP] [ENTER]`).

---

## 2. Concrete Artifact
Differential assertion check executing inside the test runner:
```python
def check_parity(darwin_state, rp2350_state, step_idx):
    assert darwin_state.x == rp2350_state.x, f"Mismatch at step {step_idx}: X={darwin_state.x} vs {rp2350_state.x}"
    assert darwin_state.stack == rp2350_state.stack, f"Stack diverged at step {step_idx}"
    assert darwin_state.flags == rp2350_state.flags, f"Flags diverged at step {step_idx}"
```

---

## 3. Community Discussion Invitation
**To the Hackaday Community:**  
When developing bare-metal firmware, what emulator or simulation harness do you rely on before spinning hardware? Do you use Renode, QEMU, or bespoke cycle-accurate simulators? How do you fuzz stateful hardware peripherals?
