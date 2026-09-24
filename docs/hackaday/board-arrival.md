---
title: "Board Arrival Evidence Protocol"
description: "Seven-stage verification protocol and checklist for physical RP2350 board bring-up."
---

# Board Arrival Evidence Protocol & Checklist

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// HARDWARE BRING-UP · GATED EVIDENCE PROTOCOL</div>

> **Hardware Gate Constraint:** A booted screen does not prove keypad reliability or battery endurance. Each physical property must be inspected and recorded as an independent test observation before making public hardware claims.

---

## The Seven Verification Stages

| Stage | Inspection Target | Verification Method | Acceptance Threshold | Failure Condition & Triage |
|---|---|---|---|---|
| **1. Seating Plane** | PCB fit into chassis rails | Slide board into `chassis_award` guide channels. Measure perimeter gap. | Board seats flush on internal shelf; zero lateral rocking; $\le 0.20\text{ mm}$ gap. | Rail binding -> Measure caliper width of PCB routing edge. Sand or adjust CAD. |
| **2. Display Alignment** | 2.5" ST7567 LCD centering | Mount LCD in faceplate cowl. Inspect viewing window margins with backlit test pattern. | Active display area centered within $\pm 0.3\text{ mm}$; zero pixel cutoff by bezel cowl. | Misaligned window -> Adjust faceplate aperture in `unified_faceplate_award.scad`. |
| **3. Connector Clearance** | 0.5 mm ZIF ribbon loop | Insert FFC into bottom-contact ZIF socket. Slide assembly closed. | Ribbon maintains natural $\ge 1.5\text{ mm}$ radius bend; zero pinching against chassis rib. | Creased ribbon -> Immediate stop; deepen chassis relief notch. |
| **4. Matrix / Switch Reach** | Key actuator contact | Depress each of the 37 keys through TPU membrane. Inspect switch plunger contact. | Every key achieves tactile dome click with $\le 1.8\text{ mm}$ travel; zero key binds against aperture. | Switch not engaging -> Check actuator stem height on `tpu_membrane_award.scad`. |
| **5. Cap Closure & Retention** | Snap-retention top cap | Slide `top_cap_award` into place. Measure retention force with pull gauge. | Audible dual-snap engagement; withstands $\ge 15\text{ N}$ pull force without popping open. | Loose cap -> Increase detent engagement lip by $+0.15\text{ mm}$. |
| **6. Powered Boot & Current** | USB-C power-up & quiescent draw | Connect current-limited DC bench supply (3.3V, 100mA limit). Flash UF2 test image. | Boot banner appears; quiescent current $\le 18\text{ mA}$ at 133 MHz; zero thermal runaway. | Short circuit / high current -> Immediate power cut; inspect for soldering bridges. |
| **7. First Calculation** | Operational stack execution | Execute standard golden keystroke sequence: `2 [ENTER] 3 [+]` and verify screen. | Screen displays exact integer `5` in X register; stack lifts cleanly; zero debounce ghosting. | Calculation error or ghost keys -> Check matrix diode orientation and software debounce timer. |
