---
title: "Log 10: Shipping StackCalc v1.1: Unifying Scientific (SC-32) & Visual (SC-6) Modes"
description: "How Version 1.1 on iOS, iPadOS, and standalone watchOS unites a 4-level scientific RPN stack with live dot-matrix visual math models."
---

# Log 10: Shipping StackCalc v1.1: Unifying Scientific (SC-32) & Visual (SC-6) Modes

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// HACKADAY BUILD LOG 10 · SHARED CORE & V1.1 RELEASE</div>

**Canonical Article:** [Shipping StackCalc v1.1 on the App Store: Unifying Scientific Mode (SC-32) and Visual Learning Mode (SC-6)](../../blog/posts/2026-10-23-shipping-stackcalc-v1-1-sc32-and-sc6.md)  
**Topic:** Clean-Room Swift Engine (`RPNCore`), Dot-Matrix Pictorial UI & CoreHaptics  
**Artifact:** StackCalc Calculator v1.1 (`id6801788040` on iOS, iPadOS, and watchOS)

---

## 1. The Engineering Lesson
Because our physical calculator and our Apple apps compile the exact same clean-room Swift engine (`RPNCore`) and bitmap display renderer (`132x65` dot-matrix canvas), every improvement we make while waiting for PCB fabrication ships immediately to real users on iPhone, iPad, and Apple Watch.

In **Version 1.1**, we unified two instruments inside one app:

### 1. Mode A: Scientific Mode (`StackCalc 32`)
- **4-Level RPN Stack (`X, Y, Z, T`):** Zero parentheses, visible intermediate registers, and full scientific/transcendental parity.
- **Step-by-Step Fraction Reduction (`[SIMP]`):** Factors out one prime divisor per press so learners see *how* mixed fractions reduce.
- **Solver, Simpson Integration & Plotting:** Root finding, definite integrals, and live curve plotting on the monochrome dot-matrix display.
- **100% Standalone watchOS App:** Uses the top 75% of the watch screen as a no-look `ENTER` key and the Digital Crown to scrub registers.

### 2. Mode B: Visual Learning Mode (`StackCalc 6` — New in v1.1)
Switching to `StackCalc 6` reconfigures the calculator into a focused 2-level stack where the dot-matrix LCD renders numbers as live pictorial models:
- **Ten-Frames (`10F`) & 20-Bead Number Rack (`RACK`):** Subitizing and make-ten bridging strategies.
- **Dynamic Number Line (`LINE`) & Geared Clock (`🕒`):** Proportional jump arcs and synchronized hour/minute hands.
- **5-Level Adaptive Fluency Quiz Engine (`?`):** Real-time mental math drills (`L1`–`L5`) that adapt to user speed and accuracy.

![StackCalc 6 Visual Learning Mode Hero](../../assets/press/sc6_product_page_header.png)
*Figure 1: StackCalc v1.1 unifies Scientific Mode (`SC-32`) and Visual Learning Mode (`SC-6`) on a shared dot-matrix engine.*

---

## 2. Concrete Artifact
Continuous Tactile Field (`CoreHaptics`) simulation parameters on iOS:
- **Key-Seam Boundary Pulse:** Crisp low-intensity transient triggered when a sliding finger crosses a button aperture boundary.
- **Switch Actuation Snap:** Distinct sharpness and intensity envelopes differentiating numeric keys, shift modifiers (`f`/`g`), and the double-wide `ENTER` bar.

---

## 3. Community Discussion Invitation
**To the Hackaday Community:**  
When building a touchscreen twin for a physical hardware instrument, how do you use haptics (`CoreHaptics` or LRA waveforms) to convey key boundaries before the user commits to a press? What is your favorite pixel resolution for monochrome dot-matrix UI design?
