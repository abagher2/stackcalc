---
title: "Log 01: The Watch Constraint: Designing an RPN UI for 40mm"
description: "How extreme screen constraints forced the 4-level stack and rotary minimap navigation."
---

# Log 01: The Watch Constraint: Designing an RPN UI for 40mm

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// HACKADAY BUILD LOG 01 · WEARABLE RPN</div>

**Canonical Article:** [Why We Started with the Apple Watch](../../blog/posts/2026-09-22-why-we-started-with-the-apple-watch.md)  
**Topic:** UI Architecture & Physical Constraints  
**Artifact:** Standalone watchOS Calculator Target & Minimap Navigation Engine

---

## 1. The Engineering Lesson
When building a modern scientific calculator, the natural temptation is to fill a high-resolution smartphone display with dozens of tiny buttons and nested flyout sheets. That approach masks sloppy ergonomic decisions.

We chose the opposite path: **we designed for a 40 mm Apple Watch screen first.**

A 40 mm OLED face allows exactly four readable rows of numeric typography and zero room for full alphanumeric button matrices. This extreme constraint forced three foundational architecture choices:
1. **The Four-Level Operational Stack as Primary UI:** In traditional infix calculators, you need an expression buffer, cursor indicators, and parenthesis counters. In RPN, the stack *is* the interface. Stacking $X$ (bottom/active), $Y$, $Z$, and $T$ fits the vertical aspect ratio of a smartwatch display with mathematical perfection.
2. **The Rotary Minimap (Digital Crown Scrubbing):** Instead of cramming 40 buttons onto a touch screen where fingers cause occlusion errors, the watch uses the physical Digital Crown to smoothly scrub across three functional planes (Arithmetic, Transcendental, and Memory).
3. **Discrete Haptic Detents:** Physical calculators provide tactile dome snap. On watchOS, we synthesize this with CoreHaptics: sharp `.click` transients on key contact, followed by inertia detents when rotating through registers.

![StackCalc running on Apple Watch Ultra](../../assets/watch-rpn-stack.png)
*Figure 1: Standalone watchOS interface displaying the four-level stack with zero phone tethering.*

---

## 2. Concrete Artifact
The state machine decoupling the active display register from touch entry is extracted into our standalone Swift engine:
```swift
// Core Watch Minimap State Transition
public enum MinimapPlane: Int, CaseIterable {
    case basic = 0      // +, -, *, /, ENTER
    case scientific = 1 // sin, cos, tan, ln, log, sqrt
    case memory = 2     // STO, RCL, CLSTK, SWAP
}
```

---

## 3. Community Discussion Invitation
**To the Hackaday Community:**  
When designing wearable instruments, do you prefer modal plane switching (scrolling between functional banks) or continuous multi-tap gestures? If you've mapped discrete state machines to the Apple Watch Digital Crown or similar rotary encoders, how do you prevent accidental inertial over-scrolling? Let us know in the comments below!
