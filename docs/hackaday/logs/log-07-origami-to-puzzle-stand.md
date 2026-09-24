---
title: "Log 07: From Folding Cardstock to a 3D-Printed Interlocking Desk Stand"
description: "Kinematic paper prototyping to a 6mm flat-packing interlocking puzzle dock."
---

# Log 07: From Folding Cardstock to a 3D-Printed Interlocking Desk Stand

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// HACKADAY BUILD LOG 07 · KINEMATIC PACKAGING</div>

**Canonical Article:** [From an Origami Box to a Puzzle Stand](../../blog/posts/2026-09-22-from-origami-box-to-puzzle-stand.md)  
**Topic:** Ergonomics, Kinematic Packaging & 3D Printing  
**Artifact:** OpenSCAD Puzzle Stand Models (`puzzle_stand.scad`, `puzzle_stand_assembly.scad`)

---

## 1. The Engineering Lesson
Calculators used lying flat on a workbench suffer from severe room-light glare and poor ergonomic viewing angles. Standard desktop docks, however, are bulky, take up too much desk space, and are awkward to transport in a backpack or pencil pouch.

We wanted a stand that could:
1. Support the calculator securely at two distinct ergonomic angles: **Desk Mode** ($22^\circ$ for seated typing) and **Shelf/Display Mode** ($58^\circ$ for upright reference viewing).
2. Pack completely flat into a standard pencil pouch.
3. Lock together securely without loose screws, hinges, or rubber bands.

### The Evolution: Origami Paper to Precision CAD
We began prototyping using heavy 100 lb cardstock and origami scoring techniques. Paper allowed us to iterate on center-of-gravity balance and tip-over angles in minutes.

Once the kinematic pivot lines were verified, we translated the geometry into OpenSCAD, engineering a set of **interlocking puzzle joints**:
- The tabs incorporate a $0.20\text{ mm}$ interference friction fit.
- The base features angled cradles that capture the bottom chamfer of the StackCalc32 chassis.
- When disassembled, the pieces nest together into a flat $6.0\text{ mm}$ thick plate.

![Puzzle Stand Seated with Calculator Prototype](../../assets/prototype-puzzle-stand-seated.jpeg)
*Figure 1: The 3D-printed puzzle stand supporting the mechanical calculator prototype in desk viewing mode.*

---

## 2. Concrete Artifact
OpenSCAD puzzle joint interlocking cutouts:
```scad
module puzzle_tenon(w, t, clearance=0.15) {
    difference() {
        cube([w, t, t*2]);
        translate([w/4, -0.1, t/2])
            cube([w/2 + clearance, t + 0.2, t + clearance]);
    }
}
```

---

## 3. Community Discussion Invitation
**To the Hackaday Community:**  
What is your favorite mechanism for folding or knock-down 3D-printed desk accessories? Living hinges (PP/TPU), dovetail joints, or snap-fit puzzle tabs? How do you prevent friction joints from loosening after months of use?
