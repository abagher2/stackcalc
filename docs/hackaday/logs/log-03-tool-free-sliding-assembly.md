---
title: "Log 03: Tool-Free Sliding Assembly: Four 3D-Printed Parts, Zero Screws"
description: "How internal sliding rails and compliance detents replace threaded brass inserts."
---

# Log 03: Tool-Free Sliding Assembly: Four 3D-Printed Parts, Zero Screws

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// HACKADAY BUILD LOG 03 · MECHANICAL ENCLOSURE</div>

**Canonical Article:** [A Tool-Free Calculator Built Around a Sliding Assembly](../../blog/posts/2026-09-22-tool-free-sliding-assembly.md)  
**Topic:** Mechanical Engineering, CAD & Tolerancing  
**Artifact:** 4-Part Mechanical STL Pack (`chassis_award.stl`, `unified_faceplate_award.stl`, `tpu_membrane_award.stl`, `top_cap_award.stl`)

---

## 1. The Engineering Lesson
Most 3D-printed electronics enclosures fail in one of two ways:
- They use self-tapping screws driven directly into thermoplastic, which strip out after three battery swaps.
- They rely on fragile, non-compliant snap tabs that snap off along print layer lines.

For StackCalc32, we engineered a **tool-free sliding rail assembly** that requires zero metal fasteners, screws, or heat-set brass inserts.

The architecture separates the enclosure into four distinct components:
1. **The Rigid Chassis (`chassis_award.stl`):** Provides structural integrity, houses the battery bay and PCB slide rails, with continuous internal lateral guides.
2. **The Unified Faceplate (`unified_faceplate_award.stl`):** Slides along the chassis rails, retaining the 2.5" LCD screen and locking the key matrix into position.
3. **The Flexible TPU Membrane (`tpu_membrane_award.stl`):** Acts as the tactile keyboard layer and environmental barrier, trapped between the faceplate and internal board shelf.
4. **The Retention Snap-Cap (`top_cap_award.stl`):** Slides over the top perimeter, snapping into dual retention detents to lock all four parts into an unyielding pocket instrument.

![Tool-Free Sliding Rail Assembly Open](../../assets/prototype-open-assembly.jpg)
*Figure 1: The four-part mechanical prototype opened along its continuous sliding rails.*

---

## 2. Print Settings & Tolerances
- **Layer Height:** 0.20 mm (Chassis / Faceplate / Cap); 0.15 mm (TPU Membrane).
- **Filament:** Prusament PLA / PETG for structural parts; Polymaker PolyFlex TPU95A for membrane.
- **Inter-Part Sliding Clearance:** $0.25\text{ mm}$ nominal clearance on guide rails, allowing smooth sliding while eliminating rattle.
- **Detent Retention Force:** Designed for $15\text{ N}$ thumb release force.

---

## 3. Community Discussion Invitation
**To the Hackaday Community:**  
When designing sliding mechanical joints for FDM 3D printers, how do you handle anisotropic layer shrinkage and seam placement along sliding channels? Have you found PETG on PLA to offer lower sliding friction than PLA on PLA? We'd love your maker tips!
