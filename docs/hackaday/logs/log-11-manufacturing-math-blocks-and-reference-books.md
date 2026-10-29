---
title: "Log 11: 84mm Fraction Towers, Logarithmic Prime Blocks, 3D-Printed Dummy PCBs & Unit-Tested Books"
description: "How our 3D-printed math blocks, pcbnew-derived dummy_pcb test fits, and unit-tested reference manuals turn abstract math into concrete intuition."
---

# Log 11: 84mm Fraction Towers, Logarithmic Prime Blocks, 3D-Printed Dummy PCBs & Unit-Tested Books

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// HACKADAY BUILD LOG 11 · BLOCK MANUFACTURING & DOCS PIPELINE</div>

**Canonical Article:** [From OpenSCAD to the Classroom Desk: 84mm Fraction Towers, Logarithmic Prime Blocks, and Unit-Tested Books](../../blog/posts/2026-10-26-manufacturing-math-blocks-and-reference-books.md)  
**Topic:** Mathematical CAD Invariants, `dummy_pcb.stl` Fit Checks & Unit-Tested Textbooks  
**Artifact:** `Hardware/generate_scad.py`, `Tools/book_engine.py`, & `TextbookVerificationTests_SC32.swift`

---

## 1. The Engineering Lesson
Even in the age of AI, students still need to know how to think mathematically. While our first batch of PCBs finishes assembly at PCBWay, we moved our **3D-printed Gridfinity math manipulatives** (manufactured in-house and on **Slant3D**) and our **unit-tested reference manuals** into production:

### 1. Mathematical CAD Invariants: 84mm Fraction Towers & Logarithmic Prime Blocks
- **Fraction Studio ($84\text{ mm}$ Whole Datum):** Engineered around an $84\text{ mm}$ unit height so $\frac{1}{2}$ ($42\text{ mm}$), $\frac{1}{3}$ ($28\text{ mm}$), $\frac{1}{4}$ ($21\text{ mm}$), $\frac{1}{6}$ ($14\text{ mm}$), $\frac{1}{7}$ ($12\text{ mm}$), and $\frac{1}{12}$ ($7\text{ mm}$) resolve to exact integer millimeters without slicer layer-rounding drift. Students stack $\frac{1}{2} + \frac{1}{3}$ ($70\text{ mm}$) in the left comparator channel, match it with five $\frac{1}{6}$ blocks in the right channel, enter `.1.2 [ENTER] .1.3 [+]` on `StackCalc 6`, and step through prime reduction one divisor at a time on the `SC-6` `[SIMP]` key.
- **Prime Factor Studio & Logarithmic Slide Rule:** Prime blocks ($2, 3, 5, 7$) are scaled logarithmically ($\text{Length} \propto \log(p)$) so snapping a `2` block and a `3` block end-to-end physically equals the length of `6` ($\log(2) + \log(3) = \log(6)$), making `GCD` and `LCM` tangible length-matching puzzles.

### 2. Exporting `dummy_pcb.stl` from KiCad `pcbnew` for Physical Fit Checks
To verify enclosure tolerances before fiberglass boards arrived, `Hardware/generate_scad.py` reads `calculator.kicad_pcb` via `pcbnew` and generates `dummy_pcb.scad` $\rightarrow$ `dummy_pcb.stl`—an exact 3D-printable plastic replica of the populated PCB (including the $1.6\text{ mm}$ board, all 43 switches, rear Pico 2 envelope, and ZIF socket) that we printed in PLA to test rail slide clearances and TPU plunger reach.

### 3. Compiling Textbooks Like Firmware (`book_engine.py`)
Our `Makefile` and `book_engine.py` extract every worked keystroke sequence from the **SC-32 Scientific Manual**, **SC-6 Elementary Manual**, and **590+ workbook problems**, run them as unit tests against `RPNCore`, and auto-render simulator screenshots and OpenSCAD STL diagrams.

![The StackCalc ecosystem of calculators, Gridfinity math blocks, and reference manuals.](../../assets/renders/stackcalc-ecosystem-hero-4x3.png)
*Figure 1: The physical manipulatives and test-verified reference manuals manufactured alongside the calculator.*

---

## 2. Concrete Artifact
The 5-stage dependency chain in our documentation `Makefile`:
```makefile
# 1. OpenSCAD (.scad) -> STL (.stl) -> Orthographic Block Diagrams & blocks_registry.json
# 2. Swift Layout & SwiftUI Tests (.swift) -> layout_data*.json, sequences_registry.json, & Screenshots
# 3. Manuscript Chapters (.md) + Registries + book_engine.py -> Validated Guides & RPNCore Unit Tests
# 4. Validated Guides + Assets + generate_manual_pdfs.py -> Publication PDFs
# 5. Publication PDFs + mkdocs.yml + Chapters -> Strict MkDocs Site (site/index.html)
```

---

## 3. Community Discussion Invitation
**To the Hackaday Community:**  
Have you ever exported a 3D-printable dummy PCB from KiCad to test-fit mechanical enclosures and key plungers before ordering boards? How do you keep hardware user manuals synchronized with firmware changes?
