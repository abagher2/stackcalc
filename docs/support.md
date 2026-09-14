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

- **GitHub Issue Tracker:** [https://github.com/abagher2/stackcalc/issues](https://github.com/abagher2/stackcalc/issues) *(Best for bug reports, troubleshooting, and feature requests)*
- **Community Documentation:** Explore our in-depth guides for [Hardware](hardware.md), [Firmware](firmware.md), [iOS App](ios_app.md), and [Interactive Tutorials](tutorials.md).
- **Web Support & Help Desk:** Visit [stackcalc.io/support/](https://www.stackcalc.io/support/) for frequent updates.

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
- **To Switch Interface:** Press **Yellow Shift** + `FLAGS` (or tap `FLAGS` in the menu catalog) &rarr; `HW` &rarr; select `APP` or `REPLICA`.
- **Faceplate Themes:** You can also customize faceplate aesthetics in the same menu via `FLAGS` &rarr; `FACE` (`RETRO`, `STEALTH`, `NOVA`, `SPACE`, or `VOYAGER`).

---

### 5. How do I use the Equation Solver and Numerical Integrator?
StackCalc includes an equation solver based on the legendary HP-32SII algorithms:
1. Press **Blue Shift** + `STO` (`EQN Mode`) to view or input equations.
2. Select an equation (such as the preloaded Normal PDF `NPDF`).
3. Press `SOLVE` to solve for any independent variable without isolating it algebraically.
4. Press `∫` (Integrate) to perform numerical integration across specified upper and lower bounds.

---

### 6. How do I clear continuous memory or reset the calculator?
- **Clear Current X Entry / Cancel:** Press `C` (or backspace `←`).
- **The CLEAR Menu:** Press **Yellow Shift** + `C` (`CLEAR`) to open the dedicated memory reset menu:
  - `CLSTK`: Clears all four levels of the operational stack ($X, Y, Z, T$).
  - `CLREGS`: Clears the 26 storage registers ($R_0 \dots R_{25}$).
  - `CLSTAT`: Clears all two-variable statistical accumulation registers ($\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$).
  - `CLEQN`: Clears all stored user equations.
  - `CLVARS`: Clears all variables and financial registers.
  - `CLALL`: Complete factory reset; clears all stack levels, variables, registers, and equations back to initial state.


---

### 7. Physical Hardware & DIY Snap-Together Kits
- **Pre-Soldered Boards:** All electronic circuit boards and LCD modules shipped from our storefront are 100% pre-soldered and tested.
- **Assembly Guide:** Assembly takes less than 5 minutes—no soldering iron required. Detailed step-by-step schematics and video walkthroughs are available in the [Hardware Documentation](hardware.md).
- **Open-Source CAD & 3D Print Models (OpenSCAD & STL):** All mechanical parts are open-source and maintained in the main repository (`Hardware/designs/`):
  - **Chassis Enclosure:** [`Hardware/designs/chassis_tapered.scad`](https://github.com/abagher2/watch-calc-32) &rarr; `chassis_tapered.stl` (1.60857° anti-rocking continuous desk wedge with dual-tier PCB and faceplate sliding rails)
  - **Flexure Top Cap:** [`Hardware/designs/top_cap.scad`](https://github.com/abagher2/watch-calc-32) &rarr; `top_cap.stl` (squeeze-release cap with integrated wired CR2032 coin cell holder)
  - **Locking Retaining Pegs:** [`Hardware/designs/tpu_retaining_peg.scad`](https://github.com/abagher2/watch-calc-32) &rarr; `tpu_retaining_peg.stl` (compliant 95A TPU mushroom pins for screwless interlock)
  - **Unified Faceplate:** [`Hardware/designs/unified_sandwich_faceplate.scad`](https://github.com/abagher2/watch-calc-32) &rarr; `unified_sandwich_faceplate.stl` (dual-tier sliding faceplate with LCD aperture)
  - **Tactile Key Membrane:** [`Hardware/designs/hp32sii_sandwich_tpu_membrane.scad`](https://github.com/abagher2/watch-calc-32) &rarr; `hp32sii_sandwich_tpu_membrane.stl` (95A TPU tactile button suspension)
  - **Keycaps & Plungers:** [`Hardware/designs/hp32sii_production_buttons.scad`](https://github.com/abagher2/watch-calc-32) & [`Hardware/designs/rounded_buttons.scad`](https://github.com/abagher2/watch-calc-32) (trapezoidal HP-32SII or circular retro keycaps with 3-point planar spiral springs)
  - **Protective Pouch:** [`Hardware/designs/tpu_pouch.scad`](https://github.com/abagher2/watch-calc-32) &rarr; `tpu_pouch.stl` (impact-absorbing 95A TPU sleeve with rear reference card pocket)
  - **Desktop Stands:** [`Hardware/designs/puzzle_stand.scad`](https://github.com/abagher2/watch-calc-32) & [`Hardware/designs/origami_stand.scad`](https://github.com/abagher2/watch-calc-32) (modular 4-piece corner bumper / portrait stand and 10° typing elevator)
  - **PrusaSlicer 3MF Project:** `Hardware/watch-calc-32.3mf` (pre-configured multi-material print plate with 0.05 mm button detail layer heights and top-surface ironing)

---

## 🛠️ Reporting a Bug or Requesting a Feature

When submitting an issue via our [GitHub Issue Tracker](https://github.com/abagher2/stackcalc/issues), please include:
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
