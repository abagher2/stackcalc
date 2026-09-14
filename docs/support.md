---
title: Support & Customer Care
description: StackCalc Help & Support — Frequently asked questions, user guides, troubleshooting, and contact channels for iOS, watchOS, and physical hardware.
---

# Support & Customer Care

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// SUPPORT PROTOCOL · HELP DESK & DOCUMENTATION</div>

Welcome to the **StackCalc Help & Support Center**. Whether you are exploring Reverse Polish Notation on your Apple Watch, solving differential curves on your iPad, or building a physical open-hardware calculator, we are here to support you.

---

## 📬 Contact Our Team

If you need direct assistance, encountered a bug, or have a question:

- **Email Support:** [support@stackcalc.io](mailto:support@stackcalc.io) *(Average response within 24 hours)*
- **GitHub Issue Tracker:** [github.com/abagher2/watch-calc-32/issues](https://github.com/abagher2/watch-calc-32/issues) *(Best for bug reports and technical questions)*
- **Community Documentation:** Explore our in-depth guides for [Hardware](hardware.md), [Firmware](firmware.md), [iOS App](ios_app.md), and [Interactive Tutorials](tutorials.md).

---

## ❓ Frequently Asked Questions (FAQ)

### 1. How does RPN (Stack Math) work? Why are there no parentheses?
In Reverse Polish Notation (RPN), operators follow their operands:
- To evaluate **$5 + 3$**: Press `5`, `ENTER`, `3`, `+`.
- To evaluate **$(4 \times 5) + (6 \times 7)$**: Press `4`, `ENTER`, `5`, `×`, `6`, `ENTER`, `7`, `×`, `+`.

RPN completely eliminates parentheses, eliminates syntax errors, and keeps all intermediate calculation steps visible in the 4-level stack (X, Y, Z, T).

---

### 2. How do I display and calculate with exact fractions?
StackCalc includes an arbitrary-precision rational fractions engine:
- To toggle between decimal representation and exact fractional notation, press **Yellow Shift** + `.` (`FDISP`).
- A decimal like `2.125` instantly renders as exact `2 1/8`.
- Pressing `.` between integers enters mixed fractions directly (e.g., `3` `.` `1` `/c` `2` for $3 \frac{1}{2}$).

---

### 3. Does the Apple Watch app require an iPhone nearby?
**No.** StackCalc for watchOS is a **100% standalone instrument**.
- The entire calculation engine runs locally on the watch's processor.
- You can perform full 4-level stack calculations, statistical summations, and trigonometric analysis directly on your wrist with zero phone connectivity.
- Features high-contrast typography, digital crown scrubbing, and continuous edge-glow tactile haptic pulses.

---

### 4. How do I switch between the Hardware Digital Twin and Modern App interfaces?
StackCalc offers two distinct user interfaces on iPhone and iPad:
- **Hardware Replica (Default):** An authentic, brutalist digital twin of our physical open-source hardware, featuring the high-contrast icy silver-blue ST7567A dot-matrix screen, trapezoidal snap-dome key caps, and laser-marked legends.
- **Modern App:** An expansive, glassmorphism-free touch interface with dynamic softkeys and high-resolution TUI graph rendering.
- **To Switch:** Press `MODES` &rarr; `Interface` &rarr; toggle between `Hardware Replica` and `App`.

---

### 5. How do I use the Equation Solver and Numerical Integrator?
StackCalc includes an equation solver based on the legendary HP-32SII algorithms:
1. Press **Blue Shift** + `STO` (`EQN Mode`) to view or input equations.
2. Select an equation (such as the preloaded Normal PDF `NPDF`).
3. Press `SOLVE` to solve for any independent variable without isolating it algebraically.
4. Press `∫` (Integrate) to perform numerical integration across specified upper and lower bounds.

---

### 6. How do I clear continuous memory or reset the calculator?
- **Clear Current X:** Press `C` (or backspace `←`).
- **Clear Entire Stack:** Press **Yellow Shift** + `C` (`CLEAR`) &rarr; `Stack`.
- **Full Factory Reset:** Press `FLAGS` &rarr; scroll to `Reset All` / `Clear Continuous Memory`. All memory registers, stack levels, and equations will return to default state.

---

### 7. Physical Hardware & DIY Snap-Together Kits
- **Pre-Soldered Boards:** All electronic circuit boards and LCD modules shipped from our storefront are 100% pre-soldered and tested.
- **Assembly Guide:** Assembly takes less than 5 minutes—no soldering iron required. Detailed step-by-step schematics and video walkthroughs are available in the [Hardware Documentation](hardware.md).
- **3D Printing Files:** All CAD models (`.scad`, `.stl`, `.3mf`) for enclosures, plungers, and faceplates are open-source and free to download from our GitHub repository.

---

## 🛠️ Reporting a Bug or Requesting a Feature

When submitting an issue via [GitHub](https://github.com/abagher2/watch-calc-32/issues) or emailing [support@stackcalc.io](mailto:support@stackcalc.io), please include:
1. **Device & OS Version** (e.g., iPhone 17 Pro Max with iOS 18, Apple Watch Series 11 with watchOS 11, or physical RP2350 hardware).
2. **Interface Mode** (Hardware Replica or App).
3. **Step-by-Step Keystroke Sequence** (e.g., `5`, `ENTER`, `3`, `÷`).
4. **Expected Output vs. Actual Display Output**.

---

<div class="mt-8 pt-6 border-t border-mask/20 flex flex-wrap gap-4 font-mono text-xs text-mask">
    <a href="../privacy/" class="hover:text-accentCyan font-bold">&larr; PRIVACY POLICY</a>
    <span class="text-mask/40">·</span>
    <a href="../terms/" class="hover:text-accentCyan font-bold">TERMS OF SERVICE</a>
    <span class="text-mask/40">·</span>
    <a href="../" class="hover:text-icyblue">HOME</a>
</div>
