---
title: "Log 04: TPU Keypad Membrane: FEA Simulation vs. Printed Actuation"
description: "Modeling off-axis keystroke deformation using a 280-condition FEA parameter sweep."
---

# Log 04: TPU Keypad Membrane: FEA Simulation vs. Printed Actuation

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// HACKADAY BUILD LOG 04 · FEA & TACTILE KEYPAD</div>

**Canonical Article:** [What the First Printed StackCalc Prototype Can Teach Us](../../blog/posts/2026-09-22-current-prototype-evidence-ledger.md)  
**Topic:** Materials Science, FEA Simulation & Keypad Haptics  
**Artifact:** 280-Condition FEA Simulation Sweep & OpenSCAD Parametric Key Model

---

## 1. The Engineering Lesson
Keypad feel makes or breaks a handheld calculator. Early prototypes explored print-in-place cantilevered leaf springs (`prototype-print-in-place-springs.jpg`), but FDM layer delamination under repetitive fatigue proved unreliable.

We pivoted to an integrated **TPU95A elastomer membrane** that sits directly over tactile snap-dome switches.

Before printing dozens of variations, we ran an automated **280-condition Finite Element Analysis (FEA) parameter sweep** modeling keycap travel under non-ideal real-world loading:
- **Off-axis Press Angles:** $0^\circ$ (vertical) to $25^\circ$ (angled thumb press).
- **Contact Offsets:** Center strike vs. edge strike ($1.5\text{ mm}$ off-center).
- **Web Wall Geometry:** Tapered thickness from $0.6\text{ mm}$ to $1.2\text{ mm}$.

![TPU Membrane Deformation FEA Study](../../assets/tpu-membrane-simulation-frame.png)
*Figure 1: FEA simulation mesh illustrating stress concentration along the membrane hinging web under angled actuation.*

### What FEA Taught Us (and What It Didn't)
- **What it solved:** The simulation identified severe binding when key caps had sharp rectangular corners. Filleting the perimeter to $r=1.2\text{ mm}$ eliminated edge pinching against the faceplate aperture.
- **The limitation:** FEA predicts geometry deformation; it does not measure tactile snap ratio, post-press switch bounce, or real-world fingertip fatigue. Physical testing on the printed specimen remains essential.

---

## 2. Concrete Artifact
OpenSCAD parametric web definition used to generate the uniform deformation profile:
```scad
module key_hinge_web(w, h, t_web, drop_angle) {
    rotate([drop_angle, 0, 0])
        difference() {
            cylinder(h=h, d=w, $fn=32);
            translate([0,0,-0.1])
                cylinder(h=h+0.2, d=w - (2 * t_web), $fn=32);
        }
}
```

---

## 3. Community Discussion Invitation
**To the Hackaday Community:**  
For custom mechanical keypads, do you favor printing direct 95A/85A TPU membranes, casting two-part silicone into 3D-printed molds, or using off-the-shelf SMD tactile domes beneath rigid caps? What snap ratio do you aim for in handheld pocket gear?
