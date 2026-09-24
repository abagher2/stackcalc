---
title: "Hackaday Project: StackCalc32"
description: "Project details, hardware boundaries, and component status for Hackaday.io."
---

# StackCalc32: A Tactile RPN Calculator

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// HACKADAY.IO PROJECT · BUILD LOG ARCHIVE</div>

**Project Page:** [https://hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator](https://hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator)  
**Status:** Mechanical Prototype Verified · Custom RP2350 PCB in Fabrication

---

## 1. Project Overview

Reverse Polish Notation (RPN) eliminated parentheses in the golden age of scientific computing, yet modern students are still forced into nested syntax traps. StackCalc32 redesigns the RPN calculator from the ground up: starting with an ultra-constrained Apple Watch UI, extending to a shared clean-room Swift core (`RPNCore`), and culminating in an open-hardware pocket calculator powered by the Raspberry Pi RP2350 microcontroller.

The mechanical enclosure uses a novel tool-free 4-part sliding rail system. The custom 4-layer PCB is currently in fabrication at the board house; visible hardware photos represent unpowered 3D-printed mechanical prototypes used for ergonomic and tolerance validation.

---

## 2. Current Prototype & Evidence Boundaries

We hold our documentation to a strict standard of engineering truthfulness:
- **Board Design Status:** The 4-layer custom KiCad RP2350 PCB design is complete and currently in fabrication at the factory. There is no powered physical board on the desk yet.
- **Physical Photos:** All hardware photos in this project show the 3D-printed tool-free mechanical prototype (`chassis_award`, `unified_faceplate_award`, `tpu_membrane_award`, `top_cap_award`). These parts are unpowered and evaluate rail sliding tolerances, membrane fit, and snap closure.
- **Firmware Verification:** The firmware logic, display driver, and keyboard matrix scanner are tested and verified via a native WebAssembly and RP2350 software emulator subjected to 40 Hz differential grammar fuzzing.
- **Companion Apps:** Full v1.1 versions of StackCalc are available on the Apple App Store for iPhone, iPad, and Apple Watch.

---

## 3. Component Status Matrix

| Component / Subsystem | Physical Medium | Current Status | Validation Evidence |
|---|---|---|---|
| **Microcontroller (RP2350)** | Silicon / KiCad | **In Fabrication** | Schematic & routing complete; DRC passed; gerbers submitted to fab. |
| **Mainboard PCB** | 4-layer FR4 | **In Fabrication** | 0.5mm ZIF routing complete, power delivery routed. Awaiting delivery. |
| **Display Panel** | EastRising 2.5" 132x65 LCD | **Design Envelope Verified** | Mechanical envelope fit into faceplate cowl; driver tested in emulator. |
| **Enclosure Chassis** | 3D-Printed PLA/PETG | **Specimen Verified** | Printed on Prusa MK4; dimensional accuracy ±0.15mm; rail fit tested. |
| **Faceplate** | 3D-Printed PLA/PETG | **Specimen Verified** | Display opening aligned; key aperture clearances verified. |
| **Keypad Membrane** | 3D-Printed 95A TPU | **Specimen & FEA** | 280-run FEA sweep; printed test specimen fits into chassis rails. |
| **Retention Cap** | 3D-Printed PLA | **Specimen Verified** | Snap-retention cycle tested for hand assembly. |
| **Firmware Engine** | Embedded Swift 6 / C | **Emulated & Fuzzed** | 40 Hz cross-surface differential fuzzing; bit-for-bit parity with host. |
| **Watch & Mobile Apps** | Native Swift / SwiftUI | **Production Shipped** | Live on Apple App Store (v1.1); standalone watchOS support. |
| **Tactile Learning Lab** | 3D Prints + Laser Wood | **Prototype 0.2.0** | Upright fraction towers, Stack Stage, Expression Tree validated. |

---

## 4. Explore the Build Logs & Resources

- [Log 01: The Watch Constraint](logs/log-01-the-watch-constraint.md) — Designing an RPN UI for 40mm
- [Log 02: One Calculator Core](logs/log-02-one-calculator-core.md) — Swift Package to Bare-Metal Silicon
- [Log 03: Tool-Free Sliding Assembly](logs/log-03-tool-free-sliding-assembly.md) — Four 3D-Printed Parts, Zero Screws
- [Log 04: TPU Keypad Membrane](logs/log-04-tpu-membrane-fea-study.md) — FEA Simulation vs. Printed Actuation
- [Log 05: Tactile Math & Learning Lab](logs/log-05-learning-lab-and-stack-stage.md) — 3D-Printed Learning Lab & Expression Trees
- [Log 06: Cross-Surface Fuzzing & Emulation](logs/log-06-cross-surface-fuzzing-and-emulation.md) — Emulating the RP2350 at 40 Hz
- [Log 07: Origami to Puzzle Stand](logs/log-07-origami-to-puzzle-stand.md) — From Folding Cardstock to Interlocking 3D Print
- [Log 08: PCB Envelope & Fabrication](logs/log-08-pcb-envelope-and-fabrication.md) — How Routing Drove Enclosure Geometry
- [Build Instructions](build-instructions.md) — Step-by-step mechanical assembly guide
- [Project Files](files.md) — Approved downloadable STLs and teacher PDFs
- [Launch Cadence & Community Asks](launch-cadence.md) — Publishing schedule and engineering questions
- [Board Arrival Protocol](board-arrival.md) — Gated bring-up checklist for PCB delivery
