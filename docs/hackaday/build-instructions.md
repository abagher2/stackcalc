---
title: "StackCalc32 Build Instructions"
description: "Two-phase mechanical 3D-printing and assembly instructions for StackCalc32."
---

# StackCalc32 Build Instructions

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// HACKADAY.IO · BUILD INSTRUCTIONS</div>

> **Current Hardware Stage:** The custom RP2350 PCB is in fabrication. These build directions cover **Phase 1: 3D printing and mechanical assembly** of the four-part tool-free prototype (`chassis_award`, `unified_faceplate_award`, `tpu_membrane_award`, `top_cap_award`). Electrical assembly instructions will be released in Phase 2 once verified boards arrive.

---

## Phase 1: 3D Printing & Mechanical Assembly

### Materials & Tools
- **3D Printer:** $\ge 180 \times 180\text{ mm}$ build bed (Prusa MK3/MK4, Bambu Lab, etc.).
- **Filament:** Rigid PLA or PETG for structural pieces; 95A TPU for the keypad membrane.
- **Fasteners:** None! Zero screws, threaded brass inserts, or glue required.

### Print Settings
1. **`chassis_award.stl`:**
   - Orientation: Flat on bottom face.
   - Layer Height: 0.20 mm | Perimeters: 4 | Infill: 20% Gyroid | Supports: None.
2. **`unified_faceplate_award.stl`:**
   - Orientation: Flat face down on textured bed for smooth top finish.
   - Layer Height: 0.20 mm | Perimeters: 4 | Infill: 20% Grid | Supports: None.
3. **`tpu_membrane_award.stl`:**
   - Orientation: Flat on bed, keycaps facing upward.
   - Layer Height: 0.15 mm | Speed: 25 mm/s | Infill: 100% solid.
4. **`top_cap_award.stl`:**
   - Orientation: Top surface flat on build plate.
   - Layer Height: 0.20 mm | Perimeters: 4 | Infill: 25% | Supports: None.

### Step-by-Step Assembly
1. **Clean Channels:** Remove any bed brim residue or stringing from the internal slide rails along the chassis sides.
2. **Seat the TPU Membrane:** Drop `tpu_membrane_award` into the internal shelf of the chassis. Ensure all 37 key mounds align with the matrix guides without buckling.
3. **Slide the Faceplate:** Engage the tongue-and-groove rails of `unified_faceplate_award` with the chassis. Slide downward until the faceplate seats flush against the bottom stop.
4. **Snap the Top Cap:** Position `top_cap_award` over the top opening and press firmly downward until both retention detents snap audibly into place.
5. **Ergonomic Check:** Verify the assembly feels completely rigid with zero lateral play, and that all keys depress smoothly with tactile rebound.
