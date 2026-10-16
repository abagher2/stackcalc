#!/usr/bin/env python3
"""
Packages open-source 3D printable ZIP archives for:
1. Counting Tiles & Array Studio (counting-tiles-open-source-stls.zip)
2. Prime Factor Studio (prime-factor-studio-open-source-stls.zip)
"""

import sys
import os
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
DOWNLOADS_DIR = DOCS_DIR / "downloads"
WATCH_CALC_ROOT = REPO_ROOT.parent / "watch-calc-32"
SCAD_DIR = WATCH_CALC_ROOT / "Education" / "scad"
STL_DIR = WATCH_CALC_ROOT / "Education" / "build" / "stl"

COUNTING_ZIP = DOWNLOADS_DIR / "counting-tiles-open-source-stls.zip"
PRIME_ZIP = DOWNLOADS_DIR / "prime-factor-studio-open-source-stls.zip"

def build_counting_tiles_zip():
    readme = """================================================================================
STACKCALC LEARNING LAB // COUNTING TILES & ARRAY STUDIO (TILE-01)
================================================================================
Open-Source 3D Printable STL & OpenSCAD Source Pack
Standard: Zack Freedman 42mm Gridfinity Ecosystem (13U Master Height)
Target Grades: K - 6 (One-to-one counting, cardinality, arrays, Four-Color Map Theorem)

CONTENTS:
1. unifix_cubes_parts.stl / unifix_cubes_parts.scad
   - 144 Harmonized Monolithic Counting Tiles (19.0 x 19.0 x 8.85 mm, 7.0mm visible 1U height).
   - Sliced across 4 color plates (36 tiles each):
     Plate 1: Archival White (Sunlu White PLA 2.0+ / White PETG #F5F5F3)
     Plate 2: Cobalt Blue (Red+Blue Dual Silk PLA #2563EB)
     Plate 3: Radiant Gold (Red+Gold Dual Silk PLA #BC2626)
     Plate 4: Slate Gray (Sunlu Blue-Gray PLA 2.0+ #5B6579)
   - Matches 1/12th Fraction Studio block (stack of 3 = 21mm, stack of 12 = 84mm).
   - Gravity docking with 45-degree chamfers and 0.40mm clearance (blocks do not snap or fatigue).

2. unifix_cubes_box.stl / unifix_cubes_box.scad
   - 3x1x13U Gridfinity Enclosure Box (125.5 x 42.0 x 91.0 mm body, 95.4mm with lip).
   - Front debossed instrument plaque: "COUNTING"
   - Rear button badge: "[NUM]"
   - Stackable lid with 12 miniblock docking grid.

PRINT SETTINGS:
- Layer Height: 0.20 mm Standard (0.12 mm for lid legends)
- Infill: 15% - 20% Gyroid
- Supports: NONE (100% Support-Free)
- Material: PLA 2.0+ or PETG

License: CERN Open Hardware License v2 - Strongly Reciprocal
Web: https://stackcalc.io/products/counting-tiles/
Etsy Store: https://www.etsy.com/shop/StackCalc
================================================================================
"""
    with zipfile.ZipFile(COUNTING_ZIP, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("README.txt", readme)
        box_scad = SCAD_DIR / "unifix_cubes_box.scad"
        parts_scad = SCAD_DIR / "unifix_cubes_parts.scad"
        box_stl = STL_DIR / "unifix_cubes_box.stl"
        parts_stl = STL_DIR / "unifix_cubes_parts.stl"

        if box_scad.exists(): zf.write(box_scad, arcname="unifix_cubes_box.scad")
        if parts_scad.exists(): zf.write(parts_scad, arcname="unifix_cubes_parts.scad")
        if box_stl.exists(): zf.write(box_stl, arcname="unifix_cubes_box.stl")
        if parts_stl.exists(): zf.write(parts_stl, arcname="unifix_cubes_parts.stl")

    print(f"Built Counting Tiles ZIP: {COUNTING_ZIP} ({COUNTING_ZIP.stat().st_size} bytes)")

def build_prime_factor_zip():
    readme = """================================================================================
STACKCALC LEARNING LAB // PRIME FACTOR STUDIO & COMPARATOR SCALE (PRIME-01)
================================================================================
Open-Source 3D Printable STL & OpenSCAD Source Pack
Standard: Zack Freedman 42mm Gridfinity Ecosystem (13U Master Height)
Target Grades: 3 - 9 (Prime factorization, prime vs composite, Fundamental Theorem of Arithmetic)

CONTENTS:
1. prime_studio_parts.stl / prime_studio_parts.scad
   - 29 Proportional Stacking Prime Factor Blocks:
     12x [2]  (Teal / Blue,      h_vis = 42.0 * log10(2)  = 12.64 mm)
      8x [3]  (Green / Amber,    h_vis = 42.0 * log10(3)  = 20.04 mm)
      2x [5]  (Royal Blue / Gold, h_vis = 42.0 * log10(5)  = 29.36 mm)
      2x [7]  (Crimson / Purple,  h_vis = 42.0 * log10(7)  = 35.49 mm)
      1x each of [11], [13], [17], [19], [23] (Red / Coral semi-prime markers)
   - Additive Logarithmic Pitch: Each block's visible stacking height is exactly 42.0 * log10(p).
   - Stacking blocks physically sums their logarithms, measuring product N against the box scale!

2. prime_studio_box.stl / prime_studio_box.scad
   - 3x1x13U Gridfinity Enclosure Box (125.5 x 42.0 x 91.0 mm body, 95.4mm with lip).
   - Front debossed instrument plaque: "PRIME"
   - Rear button badge: "[FACT]"
   - Back Wall Bilateral Logarithmic Slide Rule Comparator Scale (1 to 100):
     Towers resting on desk (Z=0) align perfectly (0.000 mm error) with engraved marks
     (2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100).
   - Stackable lid with prime power sockets (2^6, 3^4, 5^2, 7^2, 11, 13, 17, 19, 23, GCD).

3. prime_factorization_assembly.scad
   - OpenSCAD scene verifying 6 simultaneous factorization towers ([2], [4], [6], [10], [20], [50])
     standing against the comparator scale.

PRINT SETTINGS:
- Layer Height: 0.20 mm Standard (0.12 mm for slide rule ticks and numbers)
- Infill: 15% - 20% Gyroid
- Supports: NONE (100% Support-Free)
- Material: PLA 2.0+ or PETG

License: CERN Open Hardware License v2 - Strongly Reciprocal
Web: https://stackcalc.io/products/prime-factor-studio/
Etsy Store: https://www.etsy.com/shop/StackCalc
================================================================================
"""
    with zipfile.ZipFile(PRIME_ZIP, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("README.txt", readme)
        box_scad = SCAD_DIR / "prime_studio_box.scad"
        parts_scad = SCAD_DIR / "prime_studio_parts.scad"
        assembly_scad = SCAD_DIR / "prime_factorization_assembly.scad"
        box_stl = STL_DIR / "prime_studio_box.stl"
        parts_stl = STL_DIR / "prime_studio_parts.stl"

        if box_scad.exists(): zf.write(box_scad, arcname="prime_studio_box.scad")
        if parts_scad.exists(): zf.write(parts_scad, arcname="prime_studio_parts.scad")
        if assembly_scad.exists(): zf.write(assembly_scad, arcname="prime_factorization_assembly.scad")
        if box_stl.exists(): zf.write(box_stl, arcname="prime_studio_box.stl")
        if parts_stl.exists(): zf.write(parts_stl, arcname="prime_studio_parts.stl")

    print(f"Built Prime Factor Studio ZIP: {PRIME_ZIP} ({PRIME_ZIP.stat().st_size} bytes)")

if __name__ == '__main__':
    build_counting_tiles_zip()
    build_prime_factor_zip()
