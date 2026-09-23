---
title: "How the PCB Design Shapes a Printed Calculator Before It Arrives"
date: 2026-09-22
authors:
  - abagher
categories:
  - Hardware
  - PCB
  - 3D Printing
---

The printed StackCalc enclosure is not a generic case waiting for an electronics design. Its CAD reads fixed coordinates from the KiCad board so the rails, display opening, key interfaces, and clearances are designed around the same board that is now in fabrication.

<!-- more -->

## One board, several design decisions

The active KiCad project is `Hardware/calculator.kicad_pcb`. The hardware generator extracts the board’s fixed coordinates before producing the chassis, faceplate, TPU membrane, and top-cap exports. That keeps a change to a switch or display interface visible as a mechanical consequence instead of allowing a rendered enclosure and a PCB to drift apart.

The manufacturing BOM records the chosen RP2350/Pico 2 controller, ERC13265FS 132 × 65 LCD, 0.5 mm-pitch FPC display connector, ALPS tactile switches, JST battery connector, and display-support passives. These are selected and sourced manufacturing components, not props added after the enclosure was drawn.

## Why this matters before bring-up

The same board definition guides the firmware simulator’s 132 × 65 display buffer and row-and-column keypad contract. It also constrains physical placement: the faceplate aperture must clear the display interface, the flexible membrane has to meet the intended switch locations, and the enclosure needs a service path that does not pinch the board or wiring.

The current printable assembly lets us inspect that geometry, while the emulator lets us test the logical paths that will use it. Neither substitutes for board bring-up. Once the fabricated board is populated, we will validate electrical connections, display initialization, power use, key travel, and the fit of the actual component stack against the same revision.
