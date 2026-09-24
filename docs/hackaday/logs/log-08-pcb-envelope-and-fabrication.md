---
title: "Log 08: Designing the Envelope: How PCB Routing Drove the Enclosure Geometry"
description: "How 0.5mm ZIF display routing and matrix clearances shaped the 3D-printed chassis."
---

# Log 08: Designing the Envelope: How PCB Routing Drove the Enclosure Geometry

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// HACKADAY BUILD LOG 08 · HARDWARE ENVELOPE</div>

**Canonical Article:** [How the PCB Design Shapes a Printed Calculator Before It Arrives](../../blog/posts/2026-09-22-how-the-pcb-design-shapes-the-printed-calculator.md)  
**Topic:** PCB Design, KiCad, High-Density Routing & Mechanical Envelopes  
**Artifact:** KiCad Schematic & 4-Layer Board Layout Constraints

---

## 1. The Engineering Lesson
In textbook product design, the industrial designer creates an enclosure and hands the internal volume to the electrical engineer. In custom handheld hardware, **the PCB and the enclosure must co-evolve simultaneously**.

Three critical electrical constraints directly dictated the physical geometry of StackCalc32's 3D-printed chassis:

### 1. The 0.5 mm Pitch ZIF Display Connector
We selected an EastRising 2.5" monochrome LCD ($132 \times 65$ dot-matrix) with an integrated ST7567 controller. Its flexible flat cable (FFC) terminates in a 0.5 mm pitch bottom-contact ZIF socket.
- Placing the ZIF socket at the top edge of the board created a severe bend-radius pinch point against the chassis wall.
- Moving the socket $4.2\text{ mm}$ downward provided adequate FFC loop clearance, but required notching the internal structural ribs of the printed faceplate.

### 2. Key Matrix Switch Clearances
The keyboard matrix uses 37 tactile switches arranged in a high-density 5-column by 8-row grid. To prevent the board from bowing under forceful thumb presses, the chassis incorporates three continuous longitudinal support ribs that make contact with bare ground plane zones on the PCB's bottom side.

### 3. Current Fabrication Status
The complete 4-layer board layout passed all electrical Design Rule Checks (DRC) in KiCad with zero clearance errors. The gerber packages and drill files were submitted to our PCB fabricator and are currently in the production pipeline.

**Crucial Note:** Until physical boards arrive, are seated into the printed rails, and successfully execute their first powered boot, all hardware claims in this project remain strictly at the CAD, simulation, and mechanical prototype stage.

![Exploded View of 3D-Printed Calculator Stack](../../assets/prototype-exploded-parts.jpg)
*Figure 1: Exploded view of the four printed mechanical pieces awaiting board arrival.*

---

## 2. Concrete Artifact
Key mechanical envelope specifications:
- **PCB Dimensions:** $142.0\text{ mm} \times 68.0\text{ mm} \times 1.6\text{ mm}$
- **Trace/Space:** $0.15\text{ mm} / 0.15\text{ mm}$ (4-layer stackup: Signal / GND / 3V3 / Signal)
- **ZIF Loop Clearance:** $1.8\text{ mm}$ vertical clearance above board plane.

---

## 3. Community Discussion Invitation
**To the Hackaday Community:**  
When designing tight pocket-sized enclosures around rigid PCBs, what clearance do you budget between component tops and enclosure walls? How do you prevent display FFC cables from creeping out of ZIF sockets under thermal expansion or drop shocks? Let us know in the comments!
