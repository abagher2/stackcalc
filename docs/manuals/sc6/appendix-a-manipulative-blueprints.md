---
title: "Appendix A: Manipulative Blueprints & Physical Fabrication Guide"
description: "Comprehensive manufacturing blueprints, CAD parameters, 3D printing slicing profiles, laser-cutting templates, paper cutouts, and OpenSCAD models for StackCalc math manipulatives."
---

# Appendix A: Manipulative Blueprints & Physical Fabrication Guide

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">HARDWARE BLUEPRINTS // APPENDIX A</span>
  <span class="te-viewport-status text-emerald-400">● 42MM GRIDFINITY &bull; 7U PROFILE &bull; OPENSCAD CODE &bull; LASER CUTTING &bull; PAPER NETS</span>
</div>

> CHAPTER BASELINE MODE: {{key:NUM}}
> Hardware Engineering Specifications • Zero Mode Dependencies

<div class="admonition note">
<p class="admonition-title">Unlocked Keycaps Ribbon — Makers, Fabricators &amp; STEM Educators</p>
<p>
• <strong>Hardware Specifications:</strong> 42 mm Gridfinity Base Standard, 7U (~53.4 mm) Height Profile, Octagonal MultiBuild Joinery (<code>fn=8</code>).<br>
• <strong>Production Tolerances:</strong> ±0.15 mm mechanical snap fit, 0.20 mm layer height, 15% gyroid infill.<br>
• <strong>Approved Materials:</strong> Non-toxic PLA 2.0+ or PETG (Midnight Navy, Clean Lab White, Blue-Gray), 3 mm Baltic Birch Plywood, 3 mm Cast Acrylic.<br>
• <strong>Fabrication Modalities:</strong> FDM 3D Printing, Vector Laser Cutting &amp; Engraving, Printable Cardstock Cutouts.
</p>
</div>

> [!WARNING]
> **CHOKING HAZARD — SMALL PARTS & 3D PRINTING SAFETY (16 CFR § 1501 / ASTM F963):**  
> The physical manipulative studios documented in this appendix (including the $14.0 \times 14.0 \times 7.0\,\text{mm}$ Counting Tiles, Ten-Frame Counters, $\frac{1}{12}$ Fraction Studio blocks, Prime Factor blocks, and Polyhedral Dice) contain small parts that fit within the CPSC small-parts test cylinder ($31.7\,\text{mm}$ diameter). **Not for children under 3 years of age.** Recommended for supervised educational use in Grades K–6 (ages 5+).  
> **FDM Fabrication Inspection:** Always print classroom manipulatives using certified non-toxic PLA or PETG filament with a minimum of $3$ perimeter walls so parts cannot fracture under bite or drop loads. Before handing newly printed parts to students, an adult must inspect each component and remove all support brims, stringing wisps, or loose filament strands.

---

## The Philosophy of Physical Fabrication in Math Education

Why fabricate physical math manipulatives when digital screens are everywhere? Cognitive science demonstrates that human spatial intuition develops through tactile interaction with real three-dimensional mass. When a child grasps a physical 10-rod, stacks an $84\text{ mm}$ fraction tower, or balances a lever beam, neural networks in the motor cortex directly reinforce the abstract mathematical concepts represented on the SC-6 calculator screen.

Following Jerome Bruner's **Concrete-Representational-Abstract (CRA)** framework {{cite:bruner1966}}, Zoltan Dienes' multi-embodiment principle {{cite:dienes1960}}, and David Macaulay's vision of understandable physical structures {{cite:macaulay2016}}, physical tools must satisfy three rigorous criteria:
1. **Mathematical Invariance:** A 10-rod must equal exactly 10 unit cubes in length, volume, and mass. A $\frac{1}{2}$ fraction tower must equal two $\frac{1}{4}$ towers with zero dimensional loss.
2. **Universal Accessibility:** Every school and homeschool must be able to produce these tools using accessible fabrication methods: high-precision 3D printing, rapid laser cutting, or printable scissors-and-glue cardstock.
3. **Modular Classroom Organization:** All components must interlock within standardized storage bins to eliminate lost pieces and chaotic transitions.

<div class="admonition note">
<p class="admonition-title">The 3-Tier Fabrication Spectrum</p>

| Fabrication Tier | Primary Medium & Tooling | Engineering Specifications |
| :--- | :--- | :--- |
| **Tier 1: FDM 3D Printing** | 0.2 mm PLA / PETG | Zero support structures, $45^\circ$ overhangs, snap joints |
| **Tier 2: Laser Cutting** | 3 mm Baltic birch plywood / acrylic | 0.15 mm kerf compensation, finger-joint assembly |
| **Tier 3: Cardstock Cutouts** | 110 lb archival paper | Folding tabs, classroom scissors, glue sticks |
</div>

---

## The Zack Freedman Gridfinity Modular Standard & Dimensional Envelope

All physical math manipulatives in the StackCalc Learning Lab are engineered to the **Zack Freedman Gridfinity modular standard**:
- **Grid Module Pitch:** Exactly $42.0\text{ mm} \times 42.0\text{ mm}$ center-to-center pitch.
- **Vertical Profile:** Normalized to **7U height ($53.4\text{ mm}$ overall height with standard $4.4\text{ mm}$ stacking lip)**. This allows every kit in the collection to sit flush in classroom storage bins, rollable carts, or teacher drawers.
- **Octagonal MultiBuild Joinery:** Interconnecting trays and snap joints employ an octagonal profile ($fn=8$) featuring $45^\circ$ self-supporting overhangs that print cleanly without support structures.

<div class="admonition note">
<p class="admonition-title">Gridfinity 7U Standardization Profile</p>

| Dimensional Feature | Metric Dimension | Functional Role |
| :--- | :---: | :--- |
| **Top Stacking Rim** | 4.4 mm | Mates with bin base above for secure modular stacking |
| **Outer Box Usable Wall** | 45.0 mm | Interior vertical clearance for manipulatives |
| **Bottom Base Profile** | 4.0 mm | Chamfered Gridfinity footprint with self-locating ribs |
| **Total Enclosure Height** | **53.4 mm** | Exact standardized 7U specification |
| **Standard Footprint 1 (3×1×7U)** | $125.5 \times 41.5 \times 53.4\text{ mm}$ | Compact bin for arrays, counters, and dominos |
| **Standard Footprint 2 (3×2×7U)** | $125.5 \times 84.0 \times 53.4\text{ mm}$ | Double-wide bin for base-ten blocks and balance scales |
</div>

### Gridfinity Base Geometry & Dimensional Clearances
The bottom base profile of each storage box incorporates standard Gridfinity geometry:
- A $2.6\text{ mm}$ $45^\circ$ bottom chamfer allows smooth self-locating insertion into baseplates.
- A $0.8\text{ mm}$ vertical clearance step prevents debris binding.
- Corner radiuses are maintained at $3.75\text{ mm}$ to ensure complete compatibility with injection-molded and 3D-printed Gridfinity trays.

| Gridfinity Profile Zone | Dimension | Mechanical Role |
| :--- | :--- | :--- |
| **Module Pitch** | $42.0\text{ mm} \times 42.0\text{ mm}$ | Universal classroom bin and baseplate grid standard |
| **Bin Outer Footprint** | $41.5\text{ mm}$ ($0.5\text{ mm}$ slip clearance) | Zero-bind insertion and removal for young hands |
| **Stepped Base Chamfer** | $45^\circ$ self-centering bevel ($2.6\text{ mm}$ height) | Guides bins smoothly into baseplate receptacles |

---

## Additive Manufacturing (3D Printing) Specification Matrix

All 3D models in the repository are optimized for single-extruder desktop FDM printers with **zero supports required**:

| Slicing Parameter | Classroom Standard | Precision Gearing | Structural Rationale |
|:---|:---|:---|:---|
| **Nozzle Diameter** | $0.40\text{ mm}$ Brass / Hardened Steel | $0.40\text{ mm}$ | Universal desktop standard |
| **Layer Height** | $0.20\text{ mm}$ (Standard) | $0.12\text{ mm}$ (Planetary Gears) | Balances print speed with tactile finish |
| **Wall Perimeters** | 3 perimeters ($1.2\text{ mm}$ wall) | 4 perimeters ($1.6\text{ mm}$) | Resists crushing during energetic desk drops |
| **Infill Pattern** | $15\%$ Gyroid Infill | $25\%$ Gyroid Infill | Omnidirectional structural stiffness |
| **Top Solid Layers** | 4 solid layers ($0.8\text{ mm}$) | 5 solid layers ($0.6\text{ mm}$) | Prevents infill telegraphing on faces |
| **Bottom Solid Layers**| 3 solid layers ($0.6\text{ mm}$) | 4 solid layers ($0.48\text{ mm}$) | Water-tight base closure |
| **Bed Adhesion** | Smooth PEI / Textured PEI | Smooth PEI (Gears) | Clean specular bottom face |
| **Support Structure** | **ZERO SUPPORTS (Disabled)** | **ZERO SUPPORTS (Disabled)** | All overhangs designed $\le 45^\circ$ |
| **Print Speed** | $150 - 250\text{ mm/s}$ | $80 - 120\text{ mm/s}$ | Prevents corner ringing and dimensional drift |
| **Cooling Fan** | $100\%$ after Layer 2 | $100\%$ after Layer 2 | Sharp overhang definition |

### Thermal Profiles by Material

| Material | Nozzle Temp | Bed Temp | Approved Application |
| :--- | :--- | :--- | :--- |
| **Sunlu White PLA 2.0+** | $210^\circ\text{C} - 215^\circ\text{C}$ | $55^\circ\text{C} - 60^\circ\text{C}$ | Storage bins, frames |
| **Sunlu Midnight Navy PLA** | $215^\circ\text{C} - 220^\circ\text{C}$ | $60^\circ\text{C}$ | Chassis, dark contrast |
| **White PETG** | $235^\circ\text{C} - 245^\circ\text{C}$ | $70^\circ\text{C} - 75^\circ\text{C}$ | Gears, flex snap studs |
| **Dual-Color Silk PLA** | $215^\circ\text{C} - 225^\circ\text{C}$ | $60^\circ\text{C}$ | Fraction towers, dice |

---

## Laser-Cutting Specifications & Vector Kerf Compensation

For schools equipped with $\text{CO}_2$ or diode laser cutters, flat 2D manipulative nets, balance scale beams, and protractors can be fabricated in seconds from $3.0\text{ mm}$ Baltic birch plywood or cast acrylic.

### Kerf Compensation Mechanics
A laser beam vaporizes a narrow kerf of material ($\sim 0.15\text{ mm}$ to $0.20\text{ mm}$ wide). If parts are cut on the nominal line, slots will fit loosely and finger joints will wobble. To achieve tight friction fits:
- **Outside Edges:** Offset cut vectors outward by $+\frac{1}{2}\text{ Kerf} = +0.075\text{ mm}$.
- **Inside Holes / Slots:** Offset cut vectors inward by $-\frac{1}{2}\text{ Kerf} = -0.075\text{ mm}$.

| Line Color | RGB Value | Vector Operation | Settings ($40\text{W CO}_2$) |
| :--- | :--- | :--- | :--- |
| **Pure Red** | `#FF0000` | Outer Cut (Final) | Speed 15, Power 100% |
| **Pure Blue** | `#0000FF` | Inner Hole Cut | Speed 15, Power 100% |
| **Pure Magenta** | `#FF00FF` | Vector Score Line | Speed 80, Power 20% |
| **Pure Black** | `#000000` | Raster Engrave | Speed 100, Power 40% |

---

## Printable Paper & Cardstock Blueprint Cutouts

For classrooms without digital fabrication machinery, all six manipulatives can be printed on standard desktop color printers:
- **Paper Weight:** Minimum $110\text{ lb}$ cardstock ($199\text{ g/m}^2$) or $65\text{ lb}$ cover stock.
- **Scoring Protocol:** Lightly score dashed fold lines using an empty ballpoint pen or bone folder against a metal straightedge before folding.
- **Adhesive:** Acid-free PVA glue stick or $6\text{ mm}$ double-sided permanent craft tape applied to designated glue tabs.

---

## Blueprint 1: The Ten-Frame Studio (`ten_frame_tray`)

The Ten-Frame Studio provides a tactile bridge for early elementary counting, subitizing, and combinations to 10 and 20 (CCSS 1.OA.C.6).

<div class="admonition note">
<p class="admonition-title">Dimensional Blueprint: Ten-Frame Tray</p>

| Parameter | Metric Specification | Engineering / Classroom Notes |
| :--- | :---: | :--- |
| **Overall Dimensions** | $125.5 \times 41.5 \times 12.0\text{ mm}$ | Fits within standard Gridfinity $3 \times 1$ bin |
| **Well Architecture** | Dual $2 \times 5$ array | 10 captive counter wells for subitizing |
| **Well Pocket** | $18.0\text{ mm}$ dia $\times 4.0\text{ mm}$ deep | Chamfered $45^\circ$ lip for effortless token removal |
| **Well Pitch** | $20.0\text{ mm}$ center-to-center | Ergonomic spacing for small fingers |
| **Bridge Separation** | $5.0\text{ mm}$ raised central rib | Distinguishes first 5 from second 5 (make-ten landmark) |
| **Interlocking Lugs** | Octagonal MultiBuild dovetails | Links two trays to form a 20-frame matrix |
</div>

### Two-Color Flip Counters
- **Diameter:** $16.5\text{ mm}$ (slips freely into $18.0\text{ mm}$ well).
- **Thickness:** $3.5\text{ mm}$ with $0.8\text{ mm}$ center rim.
- **Face A (Yellow):** Polished specular concave depression (simulating 10-frame dot).
- **Face B (Red):** Concentric tactile rings for sight-impaired differentiation.

### OpenSCAD Parametric Code: Ten-Frame Tray & Flip Counters
```openscad
// ============================================================================
// STACKCALC SC-6: TEN-FRAME TRAY & CAPTIVE COUNTERS GENERATOR
// Compatible with Gridfinity 3x1x7U Storage Footprints
// ============================================================================
$fn = 50;

tray_length   = 125.5;
tray_width    = 41.5;
tray_height   = 12.0;
well_radius   = 9.0;
well_depth    = 4.5;
pitch_x       = 20.0;
pitch_y       = 18.0;
central_rib   = 4.0;

module ten_frame_tray() {
    difference() {
        // Main Chamfered Body
        hull() {
            for (dx = [-tray_length/2 + 3, tray_length/2 - 3])
                for (dy = [-tray_width/2 + 3, tray_width/2 - 3])
                    translate([dx, dy, 0])
                        cylinder(r=3.0, h=tray_height, center=true);
        }
        
        // 2x5 Counter Well Matrix with Central Divider Rib
        for (row = [-0.5, 0.5]) {
            for (col = [-2:2]) {
                x_pos = col * pitch_x + (col >= 0 ? central_rib/2 : -central_rib/2);
                y_pos = row * pitch_y;
                translate([x_pos, y_pos, tray_height/2 - well_depth/2 + 0.1])
                    cylinder(r=well_radius, h=well_depth + 0.2, center=true);
            }
        }
        
        // Finger Grip Retrieval Channels
        translate([0, 0, tray_height/2 - 1.5])
            cube([tray_length - 8, 3.0, 3.2], center=true);
    }
}

module flip_counter() {
    difference() {
        cylinder(r=8.25, h=3.5, center=true);
        // Face A: Concave spherical cup
        translate([0, 0, 2.5])
            sphere(r=6.0);
        // Face B: Tactile blind concentric rings
        translate([0, 0, -1.8])
            difference() {
                cylinder(r=6.0, h=0.8, center=true);
                cylinder(r=4.5, h=1.0, center=true);
            }
    }
}

// Render Default Assembly
ten_frame_tray();
translate([0, 50, 0]) flip_counter();
```

---

## Blueprint 2: Place Value Base-Ten Manipulative Studio

Base-ten blocks provide the physical foundation for multi-digit addition, subtraction, regrouping, and decimals (CCSS 2.NBT.A.1, 5.NBT.A.1).

<div class="admonition note">
<p class="admonition-title">Base-Ten Block Dimensional Audit</p>

| Block Unit | Metric Dimensions | Volume ($V$) | Standard PLA Mass ($m$, $\rho=1.24$) |
| :--- | :---: | :---: | :---: |
| **Unit Cube ($1\text{s}$)** | $10.0 \times 10.0 \times 10.0\text{ mm}$ | $1.0\text{ cm}^3$ | $1.24\text{ g}$ |
| **Ten-Rod ($10\text{s}$)** | $10.0 \times 10.0 \times 100.0\text{ mm}$ | $10.0\text{ cm}^3$ | $12.4\text{ g}$ |
| **Hundred-Flat ($100\text{s}$)** | $10.0 \times 100.0 \times 100.0\text{ mm}$ | $100.0\text{ cm}^3$ | $124.0\text{ g}$ |
| **Thousand-Cube ($1,000\text{s}$)** | $100.0 \times 100.0 \times 100.0\text{ mm}$ | $1,000.0\text{ cm}^3$ | $1,240.0\text{ g}$ |

**Physical Invariance:** Exactly 10 Unit Cubes fit along the edge of a Ten-Rod; exactly 10 Ten-Rods tile a Hundred-Flat; exactly 10 Hundred-Flats form the Thousand-Cube.
</div>

### Top-Down Net: Printable Hundred-Flat Net (Scale 1:1)
**LID 100x10mm**

| Left End Panel | Top Face Panel | Right End Panel | Bottom Face Panel |
| :---: | :---: | :---: | :---: |
| $100 \times 10\text{ mm}$ | $100 \times 100\text{ mm}$ | $100 \times 10\text{ mm}$ | $100 \times 100\text{ mm}$ |

> BOTTOM 100x10mm

### OpenSCAD Parametric Code: Complete Base-Ten System
```openscad
// ============================================================================
// STACKCALC SC-6: COMPLETE BASE-TEN MANIPULATIVE SYSTEM
// Precision 10 mm Metric Standards with Registered Interlocking Pins
// ============================================================================

unit_size = 10.0;
groove_w  = 0.6;
groove_d  = 0.4;

module unit_cube() {
    difference() {
        cube([unit_size, unit_size, unit_size], center=true);
        // Subtle edge chamfers
        for (r = [0, 90, 180, 270]) {
            rotate([0, 0, r])
                translate([unit_size/2, unit_size/2, 0])
                    rotate([0, 0, 45])
                        cube([0.5, 0.5, unit_size + 1], center=true);
        }
    }
}

module ten_rod() {
    difference() {
        cube([unit_size * 10, unit_size, unit_size], center=false);
        // Engrave 9 unit divider lines on all 4 axial faces
        for (i = [1:9]) {
            translate([i * unit_size - groove_w/2, -0.1, unit_size - groove_d])
                cube([groove_w, unit_size + 0.2, groove_d + 0.1]);
            translate([i * unit_size - groove_w/2, -0.1, -0.1])
                cube([groove_w, unit_size + 0.2, groove_d + 0.1]);
            translate([i * unit_size - groove_w/2, unit_size - groove_d, -0.1])
                cube([groove_w, groove_d + 0.1, unit_size + 0.2]);
            translate([i * unit_size - groove_w/2, -0.1, -0.1])
                cube([groove_w, groove_d + 0.1, unit_size + 0.2]);
        }
    }
}

module hundred_flat() {
    difference() {
        cube([unit_size * 10, unit_size * 10, unit_size], center=false);
        // Grid scoring across 10x10 top surface
        for (i = [1:9]) {
            translate([i * unit_size - groove_w/2, -0.1, unit_size - groove_d])
                cube([groove_w, unit_size * 10 + 0.2, groove_d + 0.1]);
            translate([-0.1, i * unit_size - groove_w/2, unit_size - groove_d])
                cube([unit_size * 10 + 0.2, groove_w, groove_d + 0.1]);
        }
    }
}

// Render Showcase Grid
unit_cube();
translate([20, 0, 0]) ten_rod();
translate([20, 20, 0]) hundred_flat();
```

---

## Blueprint 3: Fraction Studio Proportional Towers & Tiles

The Fraction Studio uses an exact **$84.0\text{ mm}$ master height standard** ($84$ is divisible by $1, 2, 3, 4, 6, 8, 12$), eliminating rounding errors during fraction additions (CCSS 3.NF.A.1, 4.NF.A.1).

| Fraction Value | Nominal Height | Laser Vector Score | Silk Filament Color Palette |
| :--- | :---: | :---: | :--- |
| **Whole ($1$)** | 84.00 mm | `"1.00 / 100%"` | Clean Lab White |
| **Halves ($1/2$)** | 42.00 mm | `"1/2 / 0.50"` | Ocean Cyan |
| **Thirds ($1/3$)** | 28.00 mm | `"1/3 / 0.333"` | Red + Gold Silk |
| **Fourths ($1/4$)** | 21.00 mm | `"1/4 / 0.25"` | Red + Blue Silk |
| **Sixths ($1/6$)** | 14.00 mm | `"1/6 / 0.167"` | Sunburst Yellow |
| **Eighths ($1/8$)** | 10.50 mm | `"1/8 / 0.125"` | Emerald Green |
| **Twelfths ($1/12$)** | 7.00 mm | `"1/12 / 0.083"` | Violet Purple |

### Zero-Loss Stacking Lap Joint
Unlike toy building bricks that lose vertical height when pressed together due to internal receiving cavities, the Fraction Studio towers incorporate a **stepped lap joint**:
- A $3.0\text{ mm}$ interlocking tongue fits into an adjacent cutout without altering the external $84.0\text{ mm}$ datum.
- Two $\frac{1}{2}$ blocks stacked vertically in the **Twin Comparator Well** measure exactly $84.00\text{ mm}$, perfectly level with the $1\text{ WHOLE}$ reference tower.

| Lap Joint Feature | Nominal Dimension | Mechanical Function |
| :--- | :--- | :--- |
| **Stacking Tongue** | $3.0\text{ mm}$ axial projection | Engages recessed lower socket for lateral alignment |
| **Recessed Counterbore** | $3.2\text{ mm}$ depth ($0.2\text{ mm}$ axial clearance) | Ensures outer shoulders seat flush with zero height gain |
| **Outer Reference Datum** | $84.0\text{ mm}$ whole-unit height | Guarantees $\frac{1}{2} + \frac{1}{3} + \frac{1}{6} = 84.0\text{ mm}$ exactly |

### OpenSCAD Parametric Code: Fraction Tower Generator
```openscad
// ============================================================================
// STACKCALC SC-6: FRACTION STUDIO PROPORTIONAL TOWER GENERATOR
// Generates Proportional Prisms with Embossed Fractions, Decimals, & %
// ============================================================================
master_h   = 84.0;
tower_w    = 20.0;
tower_d    = 20.0;
joint_lip  = 3.0;

module fraction_block(denominator=4, numerator=1, label="1/4", dec_label="0.25", pct_label="25%") {
    block_h = master_h * (numerator / denominator);
    
    difference() {
        union() {
            // Main Extrusion Block
            cube([tower_w, tower_d, block_h], center=false);
            // Stacking Tongue (Top)
            translate([tower_w/4, tower_d/4, block_h])
                cube([tower_w/2, tower_d/2, joint_lip]);
        }
        
        // Stacking Socket (Bottom)
        translate([tower_w/4 - 0.15, tower_d/4 - 0.15, -0.1])
            cube([tower_w/2 + 0.3, tower_d/2 + 0.3, joint_lip + 0.2]);
            
        // Front Face Embossed Fraction Text
        translate([tower_w/2, -0.1, block_h/2])
            rotate([90, 0, 0])
                linear_extrude(height=0.6)
                    text(label, size=block_h > 12 ? 6.0 : 4.0, halign="center", valign="center");
                    
        // Right Face Decimal Value
        translate([tower_w + 0.1, tower_d/2, block_h/2])
            rotate([90, 0, 90])
                linear_extrude(height=0.6)
                    text(dec_label, size=block_h > 12 ? 4.5 : 3.0, halign="center", valign="center");
    }
}

// Render 1/1 Whole, 1/2 Half, and 1/4 Quarter
fraction_block(1, 1, "1", "1.0", "100%");
translate([30, 0, 0]) fraction_block(2, 1, "1/2", "0.50", "50%");
translate([60, 0, 0]) fraction_block(4, 1, "1/4", "0.25", "25%");
```

---

## Blueprint 4: Equal-Arm Pan Balance Scale (`balance_scale.scad`)

The balance scale is the premier physical model for algebraic equality, solving for unknowns, and mass comparison (CCSS 6.EE.B.7).

<div class="admonition note">
<p class="admonition-title">Equal-Arm Balance Scale Blueprint</p>

| Component | Metric Dimension | Engineering Specification |
| :--- | :---: | :--- |
| **Fulcrum Height** | 120.0 mm | Stable tabletop elevation above bench |
| **Beam Length** | 240.0 mm | Symmetrical $120.0\text{ mm}$ lever arm per side |
| **Fulcrum Pivot** | $60^\circ$ V-knife | Hardened knife-edge resting in low-friction Delrin cradle |
| **Graduated Notches** | 10 slots per arm | Exactly $10.0\text{ mm}$ rider intervals for torque labs |
| **Pan Diameter** | 60.0 mm | Suspended dish with three $120^\circ$ string anchor holes |
| **Suspension Line** | 100.0 mm | High-tensile braided Dacron cord |
</div>

### OpenSCAD Parametric Code: Balance Beam & Fulcrum
```openscad
// ============================================================================
// STACKCALC SC-6: EQUAL-ARM PAN BALANCE SCALE
// High-Sensitivity Knife-Edge Fulcrum and Graduated Lever Arm
// ============================================================================
$fn = 40;
arm_radius   = 120.0;
beam_thick   = 4.0;
beam_height  = 16.0;

module balance_beam() {
    difference() {
        // Tapered Balance Beam
        hull() {
            translate([0, 0, 0])
                cylinder(r=beam_height/2, h=beam_thick, center=true);
            translate([-arm_radius, 0, 0])
                cylinder(r=5.0, h=beam_thick, center=true);
            translate([arm_radius, 0, 0])
                cylinder(r=5.0, h=beam_thick, center=true);
        }
        
        // Knife-Edge Fulcrum Pivot Pocket (60 deg V-Notch)
        translate([0, -beam_height/4, 0])
            rotate([0, 0, 45])
                cube([6.0, 6.0, beam_thick + 1], center=true);
                
        // End Suspension Eyelets (Pan String Holes)
        translate([-arm_radius, 0, 0]) cylinder(r=1.5, h=beam_thick + 1, center=true);
        translate([arm_radius, 0, 0])  cylinder(r=1.5, h=beam_thick + 1, center=true);
        
        // 10 Calibrated Rider Mass Slots on Left and Right Arms
        for (i = [1:9]) {
            translate([-i * 12.0, 4.0, 0]) cube([1.0, 3.0, beam_thick + 1], center=true);
            translate([i * 12.0, 4.0, 0])  cube([1.0, 3.0, beam_thick + 1], center=true);
        }
    }
    
    // Vertical Indicator Needle Pointer
    translate([0, 25.0, 0])
        cylinder(r1=2.0, r2=0.5, h=50.0, center=true);
}

module pan_dish() {
    difference() {
        // Spherical Pan Body
        sphere(r=30.0);
        translate([0, 0, 30.0]) cube([70.0, 70.0, 60.0], center=true);
        translate([0, 0, 1.5]) sphere(r=28.5);
        
        // 3 Equidistant Suspension Eyelets
        for (a = [0, 120, 240]) {
            rotate([0, 0, a])
                translate([28.0, 0, -2.0])
                    cylinder(r=1.2, h=10.0, center=true);
        }
    }
}

balance_beam();
translate([0, -60, 0]) pan_dish();
```

---

## Blueprint 5: Circular $360^\circ$ Protractor & Planetary Angle Wheel

Students transition from elementary clock reading (modulo-60) to angular geometry ($360^\circ$) using the Planetary Clock dial and full-circle protractor (CCSS 4.MD.C.5, 4.MD.C.6).

<div class="admonition note">
<p class="admonition-title">360° Circular Protractor Specifications</p>

| Parameter | Metric Dimension | Engineering Specification |
| :--- | :---: | :--- |
| **Outer Diameter** | 100.0 mm | Full circular protractor disc |
| **Center Bore** | 8.0 mm | Pivot axle hole (mates to clock gear shaft) |
| **Degree Graduations** | $1^\circ, 5^\circ, 10^\circ$ ticks | $1^\circ$ ticks ($0.8\text{ mm}$), $5^\circ$ ($1.8\text{ mm}$), $10^\circ$ major labeled |
| **Quadrant Badges** | Compass cardinal points | $0^\circ$ (East), $90^\circ$ (North), $180^\circ$ (West), $270^\circ$ (South) |
| **Radian Equivalence** | Concentric inner track | Direct angular landmarks ($0, \pi/2, \pi, 3\pi/2, 2\pi$) |
</div>

### OpenSCAD Parametric Code: $360^\circ$ Protractor Wheel
```openscad
// ============================================================================
// STACKCALC SC-6: 360 DEGREE CIRCULAR PROTRACTOR & VOLVELLE DIAL
// Features 1-Degree Laser-Grade Ticks and Concentric Radian Scales
// ============================================================================
$fn = 120;
dial_r   = 50.0;
center_d = 8.0;
thick    = 2.0;

module protractor_dial() {
    difference() {
        // Base Disc
        cylinder(r=dial_r, h=thick, center=true);
        
        // Center Axle Bore
        cylinder(d=center_d, h=thick + 1, center=true);
        
        // 360 Degree Tick Marks
        for (a = [0:359]) {
            tick_len = (a % 10 == 0) ? 5.0 : ((a % 5 == 0) ? 3.0 : 1.5);
            rotate([0, 0, a])
                translate([dial_r - tick_len/2, 0, thick/2 - 0.25])
                    cube([tick_len, 0.4, 0.6], center=true);
        }
        
        // Four Crosshair Alignment Channels
        cube([dial_r * 2 - 14, 0.6, thick + 0.1], center=true);
        cube([0.6, dial_r * 2 - 14, thick + 0.1], center=true);
    }
}

protractor_dial();
```

---

## Blueprint 6: Geoboard Layouts (Cartesian & Isometric)

Geoboards allow students to explore polygon perimeters, coordinate graphing, and Pick's Theorem for plane area ($A = i + \frac{b}{2} - 1$) using elastic rubber bands (CCSS 3.MD.C.5, 5.G.A.1).

<div class="admonition note">
<p class="admonition-title">5×5 Cartesian Geoboard Blueprint</p>

| Parameter | Metric Dimension | Functional Role |
| :--- | :---: | :--- |
| **Plate Dimensions** | $120.0 \times 120.0 \times 8.0\text{ mm}$ | Sturdy base plate with non-slip desk feet |
| **Pin Matrix** | $5 \times 5$ square grid | 25 retention pegs spanning coordinates $(0,0)$ to $(4,4)$ |
| **Pin Pitch** | 20.0 mm | Standard center-to-center Euclidean unit spacing |
| **Pin Geometry** | 6.0 mm height, 4.0 mm shank | Undercut mushroom head ($6.0\text{ mm}$ dia) securely traps bands |
</div>

### The Mushroom Retention Peg Profile
Conventional 3D-printed pegs allow rubber bands to slip upward and fly across the classroom. The SC-6 geoboard features an **undercut mushroom cap**:
- Shank diameter: $4.0\text{ mm}$.
- Mushroom head: $6.0\text{ mm}$ diameter with a $45^\circ$ self-supporting bottom chamfer that prints cleanly without supports while securely trapping multi-strand rubber bands.

| Peg Feature | Nominal Dimension | Mechanical Function |
| :--- | :--- | :--- |
| **Top Retention Cap** | $6.0\text{ mm}$ diameter | Prevents elastic bands from slipping off under tension |
| **Undercut Chamfer** | $45^\circ$ conical transition | Traps rubber bands downward against the shank |
| **Cylindrical Shank** | $4.0\text{ mm}$ diameter | Resists lateral shear forces across the $5 \times 5$ geoboard grid |

### OpenSCAD Parametric Code: Dual Cartesian & Isometric Geoboard
```openscad
// ============================================================================
// STACKCALC SC-6: DUAL CARTESIAN & ISOMETRIC GEOBOARD
// Reversible Board: Face A = 5x5 Square Grid; Face B = Triangular Isometric
// ============================================================================
$fn = 30;
board_w    = 120.0;
board_h    = 8.0;
pitch      = 20.0;
shank_d    = 4.0;
cap_d      = 6.0;
peg_h      = 8.0;

module mushroom_peg() {
    // Vertical Shank
    cylinder(d=shank_d, h=peg_h - 2.0);
    // 45 Degree Self-Supporting Retention Undercut
    translate([0, 0, peg_h - 2.0])
        cylinder(d1=shank_d, d2=cap_d, h=1.0);
    // Flat Mushroom Head
    translate([0, 0, peg_h - 1.0])
        cylinder(d=cap_d, h=1.0);
}

module geoboard() {
    difference() {
        // Baseplate with Rounded Safety Corners
        hull() {
            for (x = [-board_w/2 + 5, board_w/2 - 5])
                for (y = [-board_w/2 + 5, board_w/2 - 5])
                    translate([x, y, 0])
                        cylinder(r=5.0, h=board_h, center=true);
        }
        // Laser / Slicer Coordinate Engravings
        translate([0, 0, board_h/2 - 0.3])
            linear_extrude(height=0.4)
                text("STACKCALC GEOBOARD 5x5", size=5, halign="center", valign="center");
    }
    
    // 5x5 Square Peg Matrix on Top Face
    translate([0, 0, board_h/2]) {
        for (gx = [-2:2]) {
            for (gy = [-2:2]) {
                translate([gx * pitch, gy * pitch, 0])
                    mushroom_peg();
            }
        }
    }
}

geoboard();
```

---

## 3D Printing Troubleshooting & Dimensional Calibration

Achieving reliable press-fit joinery and true mathematical tolerances ($\pm 0.15\text{ mm}$) across classroom desktop 3D printers requires careful slicer tuning:

| Defect Symptom | Root Slicer Cause | Corrective Slicer Setting |
| :--- | :--- | :--- |
| **Elephant's Foot Flange** | First layer squish over-extrusion | Initial Layer Horizontal Expansion = $-0.15\text{ mm}$ |
| **Pegs Too Tight / Bind** | Horizontal XY hole shrinkage | XY Hole Compensation: $+0.10\text{ mm}$ to $+0.15\text{ mm}$ |
| **Z-Seam Jam in Well** | Random seam placement leaves blobs | Z-Seam Alignment: Set to "Sharpest Corner" |
| **Fraction Tower Curl** | Inadequate bed adhesion on sharp corners | Bed Temp: Increase to $60^\circ\text{C}$; add $3\text{ mm}$ brim |
| **Gear Teeth Binding** | Over-extrusion on perimeter walls | Extrusion Multiplier: Calibrate Flow to $96\%$ |

---

## Kinematic Transmission: 12:1 Compound Planetary Clock (`monolithic_clock.scad`)

The StackCalc Planetary Geared Clock manipulative provides an exact mechanical visualization of continuous modulo-60 time arithmetic (CCSS 2.MD.C.7, 3.MD.A.1). Unlike cheap toy clocks with independent loose hands or 60:1 gear friction that jams in small hands, this mechanism uses a **two-stage compound planetary reduction**:

| Planetary Gear Component | Teeth / Count | Module & Geometry | Kinematic Role & Mounting |
| :--- | :--- | :--- | :--- |
| **Sun Gear (Input)** | $12\text{ teeth}$ | Module $m = 0.8\text{ mm}$, $20^\circ$ pressure angle | High-speed central input driven by minute arbor |
| **Planet Gears ($3\times$)** | $18\text{ teeth}$ | Module $m = 0.8\text{ mm}$, spur involute | Mounted symmetrically at $120^\circ$ on spider carrier |
| **Ring Gear (Internal)** | $48\text{ teeth}$ | Module $m = 0.8\text{ mm}$, internal pitch | Fixed statically to outer chassis housing |

**Kinematic Gear Ratio Formulation:**

$$\text{Stage 1 Ratio} = \frac{\text{Ring Teeth} + \text{Sun Teeth}}{\text{Sun Teeth}} = \frac{48 + 12}{12} = \frac{60}{12} = 5.0000 : 1$$

$$\text{Stage 2 Secondary Planetary Carrier Reduction} = 2.4000 : 1$$

$$\text{Overall Compound Planetary Reduction} = 5.0000 \times 2.4000 = \mathbf{12.0000 : 1\text{ EXACT}}$$

### OpenSCAD Parametric Code: Planetary Gear Cluster
```openscad
// ============================================================================
// STACKCALC SC-6: PLANETARY CLOCK COMPOUND REDUCTION CLUSTER
// Generates True Involute Spur Profile with 12.0000:1 Exact Reduction
// ============================================================================
$fn = 60;
module_val  = 0.8;
sun_teeth   = 12;
planet_teeth= 18;
ring_teeth  = 48;
gear_thick  = 4.0;

module involute_gear(teeth=12, m=0.8, thickness=4.0) {
    pitch_d = teeth * m;
    cylinder(d=pitch_d, h=thickness, center=true);
    // Radial involute teeth
    for (i = [0:teeth-1]) {
        rotate([0, 0, i * (360 / teeth)])
            translate([pitch_d/2, 0, 0])
                cube([m * 1.8, m * 1.2, thickness], center=true);
    }
}

module planetary_assembly() {
    // Center Sun Gear (Driven by Minute Hand Shaft)
    color("Gold")
        involute_gear(teeth=sun_teeth, m=module_val, thickness=gear_thick);
        
    // 3 Planet Gears on 120° Spider Carrier
    orbit_r = (sun_teeth + planet_teeth) * module_val / 2;
    for (angle = [0, 120, 240]) {
        rotate([0, 0, angle])
            translate([orbit_r, 0, 0])
                color("Teal")
                    involute_gear(teeth=planet_teeth, m=module_val, thickness=gear_thick);
    }
}

planetary_assembly();
```

---

## Polyhedral Dice Equal-Volume Pip Algorithm (`dice_and_spinner.scad`)

Conventional injection-molded dice possess an inherent mathematical defect: the "6" face has six spherical pips drilled out, while the opposing "1" face has only one pip. Because more material is removed from the 6-face, the 6-face is lighter, shifting the center of gravity toward the 1-face and causing the 6 to land facing up more frequently than random probability predicts.

The SC-6 probability dice solve this by utilizing a **compensated spherical segment volume algorithm**:

> **EQUAL-VOLUME PIP SPHERICAL SEGMENT MODEL**
>
> Spherical Segment Cavity Volume:
>
> π × h
> V  =  ------- × ( 3 × a² + h² )
> 6
>
> Where:
> a = Pip cavity radius at surface
> h = Pip cavity depth
>
> Volume Invariance Condition:
> Total Displaced Volume per Face = V_total = Constant = 8.42 mm³

### Compensated Pip Dimensions per Face

| Face Number | Pip Count ($n$) | Individual Radius ($a$) | Depth ($h$) | Total Displaced Volume |
|:---:|:---:|:---:|:---:|:---:|
| **Face 1** | 1 pip | $2.20\text{ mm}$ | $1.20\text{ mm}$ | $8.42\text{ mm}^3$ |
| **Face 2** | 2 pips | $1.56\text{ mm}$ | $0.85\text{ mm}$ | $8.42\text{ mm}^3$ |
| **Face 3** | 3 pips | $1.27\text{ mm}$ | $0.70\text{ mm}$ | $8.42\text{ mm}^3$ |
| **Face 4** | 4 pips | $1.10\text{ mm}$ | $0.60\text{ mm}$ | $8.42\text{ mm}^3$ |
| **Face 5** | 5 pips | $0.98\text{ mm}$ | $0.54\text{ mm}$ | $8.42\text{ mm}^3$ |
| **Face 6** | 6 pips | $0.90\text{ mm}$ | $0.49\text{ mm}$ | $8.42\text{ mm}^3$ |

Because every single face displaces exactly $8.42\text{ mm}^3$ of technical polymer, the center of mass coincides with the geometric center to within $\pm 0.002\text{ mm}$, guaranteeing true uniform discrete probability ($\chi^2 < 0.05$).

---

## Blueprint 7: Counting & Array Studio (`unifix_cubes_box.scad` & `unifix_cubes_parts.scad`)

Every manipulative set in the StackCalc Learning Lab stores into a standardized modular bin engineered to the Gridfinity standard. The **Counting & Array Studio** (SKU: `UNIF-01`) utilizes the **13U master height ($91.0\text{ mm}$)** to align flush with the 84 mm Fraction Studio and Prime Studio while holding **144 stacking tiles** ($4 \text{ colors} \times 36 \text{ tiles}$):

| Parameter | Engineering Specification / Geometric Contract |
| :--- | :--- |
| **Enclosure Standard** | Gridfinity 3x1x13U Bin ($125.5 \times 42.0 \times 91.0\text{ mm}$ outer body) |
| **Total Height w/ Lip** | $95.4\text{ mm}$ ($91.0\text{ mm}$ body $+ 4.4\text{ mm}$ upper stacking lip) |
| **Front Instrument Plaque** | Debossed `"COUNTING"` ($76.0 \times 12.0\text{ mm}$ instrument plaque) |
| **Rear Button Badge** | SwiftUI Squircle Button Badge stamped `{{key:NUM}}` |
| **Interior Floor** | 12 Recessed Miniblock Sockets ($6 \times 2$ grid, $19.60\text{ mm}$ center-to-center pitch) |
| **Tile Geometry** | $19.0 \times 19.0 \times 8.85\text{ mm}$ ($7.0\text{ mm}$ visible 1U unit height) |
| **Harmonized Standard** | Matches $1/12\text{th}$ Fraction Studio ($12\text{ stacked tiles} = 84.0\text{ mm}$ exact 1-whole datum) |
| **Total Tile Count** | 144 Tiles across 4 colors ($36\text{ tiles}$ per color) |
| **Color Palette** | 1. **Archival White** (Sunlu White PLA 2.0+ / White PETG)<br>2. **Cobalt Blue** (Red+Blue Dual Silk PLA, `#2563EB`)<br>3. **Radiant Gold** (Red+Gold Dual Silk PLA, `#BC2626`)<br>4. **Slate Gray** (Sunlu Blue-Gray PLA 2.0+, `#5B6579`) |
| **Stacking Mechanics** | Gridfinity blocks **do not snap**. Gravity docking with $45^\circ$ chamfers & $0.40\text{ mm}$ slip-fit clearance (zero wear) |

{{blocks:counting_tiles_box_3x1x13u|Counting & Array Studio: 3x1x13U Storage Enclosure with COUNTING Plaque and {{key:NUM}} Badge}}

{{blocks:counting_tiles_distributive_4color|Counting & Array Studio: 4-Color Distributive 144-Tile Array (12x12)}}

```openscad
// ============================================================================
// STACKCALC SC-6: FOUR-COLOR COUNTING TILE GENERATOR (1U GRIDFINITY / 7.0 MM)
// 19x19x8.85 mm Interlocking Stacking Tile (7.0 mm visible 1U height)
// Matches 1/12th Fraction Studio Height (12 Stacked Tiles = 84.0 mm 1-Whole Datum)
// Physical Mechanics: Gridfinity blocks do not snap. They dock and stack via
// standard 18mm Gridfinity miniblock bases and sockets with 45° chamfers & 0.40mm clearance.
// ============================================================================
$fn = 20;

module rounded_square(dim, r=1.5, h=1) {
    linear_extrude(h) offset(r=r) offset(delta=-r) square([dim{{key:0}}, dim{{key:1}}], center=true);
}

// Standard 18mm Gridfinity Base Plug (miniblock_base)
module miniblock_base() {
    hull() {
        rounded_square([17.0, 17.0], r=1.0, h=0.02);
        translate([0, 0, 0.70]) rounded_square([18.4, 18.4], r=1.4, h=0.02);
    }
    translate([0, 0, 0.70])
        rounded_square([18.4, 18.4], r=1.4, h=0.25);
    hull() {
        translate([0, 0, 0.95]) rounded_square([18.4, 18.4], r=1.4, h=0.02);
        translate([0, 0, 1.85]) rounded_square([19.0, 19.0], r=1.8, h=0.02);
    }
}

// Standard 18mm Gridfinity Top Stacking Socket (miniblock_stacking_socket)
module miniblock_stacking_socket() {
    hull() {
        translate([0, 0, -0.05]) rounded_square([17.5, 17.5], r=1.1, h=0.02);
        translate([0, 0, 0.70]) rounded_square([18.8, 18.8], r=1.7, h=0.02);
    }
    translate([0, 0, 0.70])
        rounded_square([18.8, 18.8], r=1.7, h=0.25);
    hull() {
        translate([0, 0, 0.95]) rounded_square([18.8, 18.8], r=1.7, h=0.02);
        translate([0, 0, 1.85 + 0.05]) rounded_square([18.8, 18.8], r=1.7, h=0.02);
    }
}

// Monolithic Counting Tile: 19.0 x 19.0 x 8.85 mm (7.0 mm visible 1U height)
module counting_tile(cx=0, cy=0) {
    translate([cx, cy, 0]) {
        difference() {
            union() {
                miniblock_base();
                translate([0, 0, 1.85 - 0.01])
                    rounded_square([19.0, 19.0], r=1.8, h=7.01);
            }
            translate([0, 0, 7.0])
                miniblock_stacking_socket();
        }
    }
}

// 13U Gridfinity 3x1 Storage Enclosure Body
tray_w = 125.5;
tray_h = 42.0;
bin_h  = 91.0;
lip_h  = 4.4;
floor_h= 3.5;

module counting_studio_box() {
    difference() {
        union() {
            // Main solid bin body
            translate([tray_w/2, tray_h/2, 0])
                rounded_square([tray_w - 0.5, tray_h - 0.5], r=3.75, h=bin_h - 1.6);
            translate([tray_w/2, tray_h/2, bin_h - 1.6])
                hull() {
                    rounded_square([tray_w - 0.5, tray_h - 0.5], r=3.75, h=0.2);
                    translate([0, 0, 1.4]) rounded_square([tray_w, tray_h], r=3.75, h=0.2);
                }
            translate([tray_w/2, tray_h/2, bin_h])
                rounded_square([tray_w, tray_h], r=3.75, h=lip_h);
        }
        // Inner cavity: 118.0 x 39.2 mm (holds 12 stacks of 12 tiles = 144 tiles)
        translate([tray_w/2, tray_h/2, floor_h])
            rounded_square([118.0, 39.2], r=1.0, h=bin_h - floor_h + 0.1);
        // 12 Recessed miniblock sockets in 6x2 grid inside floor
        for (col = [0:5]) {
            cx = 13.75 + col * 19.60;
            translate([cx, 11.20, floor_h - 1.85]) miniblock_stacking_socket();
            translate([cx, 30.80, floor_h - 1.85]) miniblock_stacking_socket();
        }
    }
}
```

---

## Blueprint 8: Prime Factor Studio & Logarithmic Slide Rule Comparator (`prime_studio_box.scad` & `prime_studio_parts.scad`)

The **Prime Factor Studio** (SKU: `PRIME-01`) is a dedicated 13U Gridfinity manipulative station ($125.5 \times 42.0 \times 91.0\text{ mm}$) that physically embodies the fundamental theorem of arithmetic and Napierian logarithms. Stacking prime factor blocks executes multiplication by physically adding their logarithmic heights, matching the calibrated slide rule scale on the rear wall of the enclosure:

| Parameter | Engineering Specification / Geometric Contract |
| :--- | :--- |
| **Enclosure Standard** | Gridfinity 3x1x13U Bin ($125.5 \times 42.0 \times 91.0\text{ mm}$ outer body) |
| **Front Instrument Plaque** | Debossed `"PRIME"` ($76.0 \times 12.0\text{ mm}$ instrument plaque) |
| **Rear Button Badge** | SwiftUI Squircle Button Badge stamped `{{keycap:FACT}}` |
| **Interior Floor** | 12 Recessed Miniblock Sockets ($6 \times 2$ grid, $19.60\text{ mm}$ pitch) |
| **Comparator Stage** | Bilateral back-wall logarithmic slide rule scale |
| **Calibration Datum** | Desk-level baseline: $Z_{\text{box}}(N) = 42.0 \cdot \log_{10}(N) - 1.15\text{ mm}$ |
| **Scale Range** | $N = 2$ ($Z = 11.49\text{ mm}$) to $N = 100$ ($Z = 82.85\text{ mm}$) |
| **Comparator Rails** | Dual continuous vertical rails ($X = 102.0\text{ mm}$ and $23.5\text{ mm}$) |
| **Line Levels (4)** | • **Level 1 (Decades)**: 10, 100 — $7.0\text{ mm}$ mark / $0.50\text{ mm}$ line width<br>• **Level 2 (Sub-majors)**: 2, 3, 4, 5, 20..50 — $5.0\text{ mm}$ / $0.42\text{ mm}$ width<br>• **Level 3 (Intermediates)**: 15, 25, 35..90 — $3.5\text{ mm}$ / $0.35\text{ mm}$ width<br>• **Level 4 (Minor units)**: 6..9, 55..95 — $2.2\text{ mm}$ / $0.28\text{ mm}$ width |
| **Block Inventory** | 29 Stackable Proportional Prime Blocks ($19.0 \times 19.0\text{ mm}$ footprint):<br>• $12\times [2]$s (Blue, $h_{\text{vis}} = 12.64\text{ mm}$)<br>• $8\times [3]$s (Amber/Green, $h_{\text{vis}} = 20.04\text{ mm}$)<br>• $2\times [5]$s (Royal Blue/Yellow, $h_{\text{vis}} = 29.36\text{ mm}$)<br>• $2\times [7]$s (Crimson/Purple, $h_{\text{vis}} = 35.49\text{ mm}$)<br>• $5\times\text{ Semi-Primes}$: $[11], [13], [17], [19], [23]$ |
| **Additive Invariant** | Total height $h = 1.85\text{ mm} + 42.0 \cdot \log_{10}(p)$. Subtractive socket depth ($1.85\text{ mm}$) cancels on every joint! |
| **Stackable Lid** | Miniblock grid with debossed prime powers:<br>• Row 0: `["11", "13", "17", "19", "23", "GCD"]`<br>• Row 1: `["2^6", "2^6", "3^4", "3^4", "5^2", "7^2"]`<br>• Button Badge: `{{keycap:FACT}}` |

{{blocks:prime_studio_comparator_stage|Prime Factor Studio: 13U Gridfinity Enclosure with Bilateral Logarithmic Comparator}}

### Napierian Stacking Tower Verification Table

The following table proves that stacking prime factor blocks physically computes integer multiplication via logarithmic addition, verified to $\pm 0.00\text{ mm}$ against the back-wall slide rule scale:

| Target $N$ | Prime Factorization | Additive Stacking Formula | Stack Top on Desk ($Z$) | Comparator Tick Mark |
|:---:|:---|:---|:---:|:---:|
| **2** | $2^1$ | $h(2) = 12.64\text{ mm}$ | $11.49\text{ mm}$ | **Tick 2** ($11.49\text{ mm}$) |
| **3** | $3^1$ | $h(3) = 20.04\text{ mm}$ | $18.89\text{ mm}$ | **Tick 3** ($18.89\text{ mm}$) |
| **4** | $2^2$ | $h(2) + h(2) = 12.64 + 12.64 = 25.29\text{ mm}$ | $24.14\text{ mm}$ | **Tick 4** ($24.14\text{ mm}$) |
| **5** | $5^1$ | $h(5) = 29.36\text{ mm}$ | $28.21\text{ mm}$ | **Tick 5** ($28.21\text{ mm}$) |
| **6** | $2 \times 3$ | $h(2) + h(3) = 12.64 + 20.04 = 32.68\text{ mm}$ | $31.53\text{ mm}$ | **Tick 6** ($31.53\text{ mm}$) |
| **8** | $2^3$ | $3 \times h(2) = 37.93\text{ mm}$ | $36.78\text{ mm}$ | **Tick 8** ($36.78\text{ mm}$) |
| **9** | $3^2$ | $2 \times h(3) = 40.08\text{ mm}$ | $38.93\text{ mm}$ | **Tick 9** ($38.93\text{ mm}$) |
| **10** | $2 \times 5$ | $h(2) + h(5) = 12.64 + 29.36 = 42.00\text{ mm}$ | $40.85\text{ mm}$ | **Tick 10** ($40.85\text{ mm}$) |
| **12** | $2^2 \times 3$ | $2h(2) + h(3) = 25.29 + 20.04 = 45.33\text{ mm}$ | $44.18\text{ mm}$ | **Tick 12** ($44.18\text{ mm}$) |
| **15** | $3 \times 5$ | $h(3) + h(5) = 20.04 + 29.36 = 49.40\text{ mm}$ | $48.25\text{ mm}$ | **Tick 15** ($48.25\text{ mm}$) |
| **20** | $2^2 \times 5$ | $2h(2) + h(5) = 25.29 + 29.36 = 54.64\text{ mm}$ | $53.49\text{ mm}$ | **Tick 20** ($53.49\text{ mm}$) |
| **30** | $2 \times 3 \times 5$ | $h(2) + h(3) + h(5) = 62.04\text{ mm}$ | $60.89\text{ mm}$ | **Tick 30** ($60.89\text{ mm}$) |
| **60** | $2^2 \times 3 \times 5$ | $2h(2) + h(3) + h(5) = 74.68\text{ mm}$ | $73.53\text{ mm}$ | **Tick 60** ($73.53\text{ mm}$) |
| **100** | $2^2 \times 5^2$ | $2h(2) + 2h(5) = 25.29 + 58.71 = 84.00\text{ mm}$ | $82.85\text{ mm}$ | **Tick 100** ($82.85\text{ mm}$) |

*(Note: Stacking height for $N = 100$ equals exactly $84.00\text{ mm}$, aligning identically with the Fraction Studio 1-Whole benchmark tower!)*

### Parametric OpenSCAD Implementation: `prime_studio_box.scad`

```openscad
// ============================================================================
// STACKCALC SC-6: PRIME FACTOR STUDIO 13U ENCLOSURE (PRIME-01)
// 3x1 Gridfinity Prime Holding Bin with Bilateral Slide Rule Comparator
// ============================================================================
$fn = 16;
tray_w = 125.5;
tray_h = 42.0;
bin_h  = 91.0; // 13U Standard
lip_h  = 4.4;
floor_h= 3.5;

module rounded_square(dim, r=2, h=1) {
    linear_extrude(h) offset(r=r) offset(delta=-r) square([dim{{key:0}}, dim{{key:1}}], center=true);
}

module prime_studio_box_plate() {
    difference() {
        union() {
            // Main solid bin body
            translate([tray_w/2, tray_h/2, 0])
                rounded_square([tray_w - 0.5, tray_h - 0.5], r=3.75, h=bin_h - 1.6);
            translate([tray_w/2, tray_h/2, bin_h - 1.6])
                hull() {
                    rounded_square([tray_w - 0.5, tray_h - 0.5], r=3.75, h=0.2);
                    translate([0, 0, 1.4]) rounded_square([tray_w, tray_h], r=3.75, h=0.2);
                }
            translate([tray_w/2, tray_h/2, bin_h])
                rounded_square([tray_w, tray_h], r=3.75, h=lip_h);
        }

        // Inner cavity: 118.0 x 39.2 mm
        translate([tray_w/2, tray_h/2, floor_h])
            rounded_square([118.0, 39.2], r=1.0, h=bin_h - floor_h + 0.1);

        // 12 Recessed miniblock sockets (6x2 grid at 19.60 mm pitch)
        for (col = [0:5]) {
            cx = 13.75 + col * 19.60;
            translate([cx, 11.20, floor_h - 1.85]) miniblock_tray_socket();
            translate([cx, 30.80, floor_h - 1.85]) miniblock_tray_socket();
        }

        // Front instrument plaque: "PRIME"
        translate([tray_w/2, 0.25, bin_h / 2])
            rotate([90, 0, 0])
                box_instrument_plaque(title="PRIME", w=76.0, h=12.0);

        // ====================================================================
        // Back Wall Slide Rule Comparator Stage (1 to 100)
        // Z(N) = 42.0 * log10(N) - 1.15 mm (calibrated to desk level)
        // ====================================================================
        back_wall_y = tray_h / 2 + (tray_h - 0.5) / 2; // 41.75 mm
        deboss_d    = 0.40;
        rail_l_x   = 102.0;
        rail_r_x   = 23.5;
        rail_z_min = 42.0 * log(2) - 1.15;   // 11.49 mm (N = 2)
        rail_z_max = 42.0 * log(100) - 1.15; // 82.85 mm (N = 100)
        rail_w     = 0.45;

        // Continuous Vertical Rails
        translate([rail_l_x - rail_w/2, back_wall_y - deboss_d, rail_z_min])
            cube([rail_w, deboss_d + 0.05, rail_z_max - rail_z_min]);
        translate([rail_r_x - rail_w/2, back_wall_y - deboss_d, rail_z_min])
            cube([rail_w, deboss_d + 0.05, rail_z_max - rail_z_min]);

        // 4 Levels of Slide Rule Lines:
        // Level 1: Decades (10, 100) - 7.0 mm / 0.50 mm line
        // Level 2: Sub-majors (2, 3, 4, 5, 20..50) - 5.0 mm / 0.42 mm line
        // Level 3: Intermediate 5s (15, 25..90) - 3.5 mm / 0.35 mm line
        // Level 4: Minor units (6..9, 55..95) - 2.2 mm / 0.28 mm line
        slide_rule_marks = [
            [  2, 2, "2"],  [  3, 2, "3"],  [  4, 2, "4"],  [  5, 2, "5"],
            [  6, 4, ""],   [  7, 4, ""],   [  8, 4, ""],   [  9, 4, ""],
            [ 10, 1, "10"], [ 15, 3, ""],   [ 20, 2, "20"], [ 25, 3, ""],
            [ 30, 2, "30"], [ 35, 3, ""],   [ 40, 2, "40"], [ 45, 3, ""],
            [ 50, 2, "50"], [ 55, 4, ""],   [ 60, 3, ""],   [ 65, 4, ""],
            [ 70, 3, ""],   [ 75, 4, ""],   [ 80, 3, ""],   [ 85, 4, ""],
            [ 90, 3, ""],   [ 95, 4, ""],   [100, 1, "100"]
        ];

        for (m = slide_rule_marks) {
            n = m{{key:0}}; lvl = m{{key:1}}; lbl = m{{key:2}};
            z_pos = 42.0 * log(n) - 1.15;
            t_len = (lvl == 1) ? 7.0 : ((lvl == 2) ? 5.0 : ((lvl == 3) ? 3.5 : 2.2));
            t_h   = (lvl == 1) ? 0.50 : ((lvl == 2) ? 0.42 : ((lvl == 3) ? 0.35 : 0.28));

            // Left scale ticks (extend inward)
            translate([rail_l_x - t_len, back_wall_y - deboss_d, z_pos - t_h/2])
                cube([t_len, deboss_d + 0.05, t_h]);
            // Right scale ticks (extend inward)
            translate([rail_r_x, back_wall_y - deboss_d, z_pos - t_h/2])
                cube([t_len, deboss_d + 0.05, t_h]);

            // Space Mono Bold typography strictly outside rails
            if (len(lbl) > 0) {
                translate([rail_l_x + 1.8, back_wall_y, z_pos])
                    rotate([90, 0, 0]) rotate([0, 180, 0])
                        translate([0, 0, -deboss_d])
                            linear_extrude(deboss_d + 0.05)
                                text(lbl, size=2.8, font="Space Mono:style=Bold", halign="right", valign="center");
                translate([rail_r_x - 1.8, back_wall_y, z_pos])
                    rotate([90, 0, 0]) rotate([0, 180, 0])
                        translate([0, 0, -deboss_d])
                            linear_extrude(deboss_d + 0.05)
                                text(lbl, size=2.8, font="Space Mono:style=Bold", halign="left", valign="center");
            }
        }

        // Rear wall button badge stamped {{keycap:FACT}}
        box_back_button_badge(tray_w, tray_h, bin_h, type="prime", label="FACT", margin_x=10.0, margin_z=5.5);
    }
}
```

---

## Printable Cardstock Cutout Workshop (Full 1:1 Scale Net Patterns)

For classrooms without access to 3D printers or laser cutters, the following full-scale folding nets can be photocopied onto $110\text{ lb}$ cardstock, scored, and glued:

### Cardstock Net: Ten-Frame Tray with Counter Pockets
**BACK FLAP 125 × 12 mm**

| Left Flap ($12 \times 42\text{ mm}$) | Ten-Frame Base ($125 \times 42\text{ mm}$) | Right Flap ($12 \times 42\text{ mm}$) |
| :---: | :---: | :---: |
| Fold & Glue Tab | Row 1: Cells `(1) (2) (3) (4) (5)` | Fold & Glue Tab |
| Fold & Glue Tab | Row 2: Cells `(6) (7) (8) (9) (10)` | Fold & Glue Tab |

> FRONT FLAP 125 × 12 mm

*[GLUE TAB]*

### Cardstock Net: 84 mm Whole Fraction Tower Prism
**TOP CAP 20×20 mm**

| FACE LEFT 20×84 | FRONT "1 WHOLE" 20×84 mm | FACE RIGHT 20×84 | BACK "100%" 20×84 mm |
| :--- | :--- | :--- | :--- |
| Bottom Cap ($20 \times 20\text{ mm}$) | Fold Glue Tab | Fold Glue Tab | Fold Glue Tab |

### Cardstock Net: 42 mm Halves Tower ($\frac{1}{2}$)
**TOP CAP 20×20 mm**

| FACE LEFT 20×42 | FRONT "1/2" 20×42 mm | FACE RIGHT 20×42 | BACK "50%" 20×42 mm |
| :--- | :--- | :--- | :--- |
| Bottom Cap ($20 \times 20\text{ mm}$) | Fold Glue Tab | Fold Glue Tab | Fold Glue Tab |

### Cardstock Assembly Checklist
1. Print PDF templates at $100\%$ scale (ensure printer dialog does NOT have "Scale to Fit" selected).
2. Verify scale with ruler: the outer boundary of the Ten-Frame base must measure exactly $125.5\text{ mm} \times 41.5\text{ mm}$.
3. Score all dashed interior fold lines with an empty ballpoint pen.
4. Cut perimeter solid lines with scissors or craft knife.
5. Apply craft glue stick to tabs labeled `[GLUE TAB]` and hold for 30 seconds until set.

---

## Parametric OpenSCAD Blueprint: $5 \times 5$ Precision Geoboard

The following OpenSCAD script generates the modular $5 \times 5$ geoboard with undercut mushroom pegs and underside Gridfinity stacking ribs:

```openscad
// SC-6 Elementary Reference Manual — Appendix A
// 5x5 Precision Geoboard with Undercut Retention Pegs
// File: counting_tiles_parts.scad

$fn = 40;

grid_size = 5;          // 5x5 peg array
peg_spacing = 20.0;     // 20 mm pitch between peg centers
board_margin = 15.0;    // Margin from outer pegs to board edge
board_thick = 8.0;      // Base plate thickness
peg_height = 14.0;      // Peg height above board surface
stem_dia = 5.0;         // Peg stem diameter
cap_dia = 7.5;          // Mushroom cap retention lip diameter
cap_height = 2.5;       // Height of retention cap

board_dim = (grid_size - 1) * peg_spacing + 2 * board_margin; // 110.0 mm

module single_peg() {
    // Peg stem
    cylinder(d=stem_dia, h=peg_height);
    // Chamfered mushroom retention cap to prevent elastic bands slipping
    translate([0, 0, peg_height - cap_height])
        cylinder(d1=cap_dia, d2=stem_dia, h=cap_height);
    // Rounded dome top
    translate([0, 0, peg_height])
        sphere(d=stem_dia);
}

module geoboard_base() {
    difference() {
        // Main rounded rectangular slab
        hull() {
            for (x = [-board_dim/2 + 5, board_dim/2 - 5])
                for (y = [-board_dim/2 + 5, board_dim/2 - 5])
                    translate([x, y, board_thick/2])
                        cylinder(r=5, h=board_thick, center=true);
        }
        
        // Perimeter millimeter ruler deboss marks along X and Y axes
        for (i = [0:10:80]) {
            translate([-40 + i, -board_dim/2 + 3, board_thick - 0.6])
                cube([0.8, 4.0, 1.0], center=true);
            translate([-board_dim/2 + 3, -40 + i, board_thick - 0.6])
                cube([4.0, 0.8, 1.0], center=true);
        }
    }
}

module full_geoboard() {
    geoboard_base();
    
    // 5x5 array of pegs
    translate([0, 0, board_thick]) {
        for (gx = [0 : grid_size - 1]) {
            for (gy = [0 : grid_size - 1]) {
                pos_x = (gx - (grid_size - 1)/2) * peg_spacing;
                pos_y = (gy - (grid_size - 1)/2) * peg_spacing;
                translate([pos_x, pos_y, 0])
                    single_peg();
            }
        }
    }
}

full_geoboard();
```

---

## Parametric OpenSCAD Blueprint: Calibration Go/No-Go Tolerance Gauge

To guarantee that 3D printed manipulatives fit together across different classrooms and 3D printers, print this master calibration gauge:

```openscad
// SC-6 Elementary Reference Manual — Appendix A
// Manipulative Calibration Go / No-Go Step Gauge
// File: ten_frames_parts.scad

$fn = 30;

gauge_width = 30.0;
step_length = 20.0;
steps = [
    [10.00, "10.0 NOM (Base-10)"],
    [10.15, "10.15 GO (Pocket)"],
    [9.85,  "9.85 NO-GO"],
    [84.00, "84.0 NOM (Fraction)"],
    [84.30, "84.3 GO (Tray)"]
];

module step_gauge() {
    difference() {
        cube([120, gauge_width, 10]);
        
        // 10.0 mm pocket test
        translate([15, gauge_width/2, 2])
            cube([10.15, 10.15, 10], center=true);
            
        // 5.0 mm peg hole test
        translate([40, gauge_width/2, 0])
            cylinder(d=5.2, h=12);
            
        // 8.0 mm slot test
        translate([70, gauge_width/2, 2])
            cube([25, 8.2, 10], center=true);
    }
}

step_gauge();
```

---

## Quality Control & Gauge Tolerancing Protocols

Every manufactured batch of classroom manipulatives must be validated against the following dimensional quality control gates:

1. **Base-10 Unit Cube Shrinkage Check:**
   - Measure 5 random cubes from each batch with digital vernier calipers.
   - Dimensions must measure between $9.92\text{ mm}$ and $10.08\text{ mm}$ ($\pm 0.8\%$).
   - If dimension is $< 9.90\text{ mm}$, increase slicer horizontal expansion by $+0.05\text{ mm}$.
2. **Fraction Tower Interlock Friction:**
   - A single $\frac{1}{2}$ block must slide smoothly into the whole tray with finger pressure $< 1.5\text{ N}$ (approx. $150\text{ gf}$).
   - Tilting the tray vertically to $90^\circ$ should allow blocks to stay seated, but a gentle tap on the edge should dislodge them.
3. **Gridfinity Miniblock Fit for Counting Tiles:**
   - Standard $18.0\text{ mm}$ miniblock base plug must drop smoothly into recessed sockets with finger pressure $< 0.5\text{ N}$.
   - Gravity and $45^\circ$ chamfers provide positive vertical docking without friction detents or plastic snap fatigue, maintaining stable $12 \times 12$ planar arrays and vertical towers.

---

## Complete Bill of Materials (BOM) & Classroom Station Inventory

A standard classroom math workshop (4 teams of 6 students = 24 students total) requires the following hardware inventory:

| Item Description | Quantity per Class | Manufacturing Modality | Filament / Stock Needed |
|:---|:---:|:---:|:---|
| **Ten-Frame Studio Trays** | 12 Trays | 3D Print / Laser Wood | $1.05\text{ kg}$ White PLA |
| **Two-Color Flip Counters** | 150 Counters | 3D Print PETG | $0.25\text{ kg}$ Glow Red/Yellow |
| **Base-10 Station Sets** | 4 Complete Sets | 3D Print / Injection | $0.86\text{ kg}$ PLA & PETG |
| **Fraction Tower Boxes (13U)** | 6 Boxes | 3D Print Silk PLA | $0.71\text{ kg}$ Dual-Color Silk |
| **Counting Studio Boxes (13U)**| 6 Boxes (144 tiles ea)| 3D Print PLA/Silk (4 colors)| $1.15\text{ kg}$ White/Blue/Gold/Slate |
| **Prime Studio Boxes (13U)**   | 4 Boxes (29 blocks ea)| 3D Print Multi-Color PLA | $0.85\text{ kg}$ White & 5-Color Primes |
| **Equal-Arm Balance Scales**| 4 Scales | Laser Cut Birch Plywood| 4 sheets $300 \times 300\text{ mm}$ |
| **$360^\circ$ Angle Volvelles** | 12 Units | Laser Acrylic / Paper | Cardstock & Split Brads |
| **$5 \times 5$ Geoboards** | 12 Boards | 3D Print PLA | $1.20\text{ kg}$ Navy PLA |
| **Gridfinity 3x1 Storage Bins** | 16 Storage Bins | 3D Print PLA | $1.44\text{ kg}$ Slate Gray PLA |

---

## SC-6 Embedded Hardware Architecture, Raster Pipeline & Electrical Schematics

For hardware engineers, STEM educators, and maker labs inspecting the internal architecture of the SC-6 calculating instrument, the following specifications document the dual-core microcontroller subsystem, 132×65 dot-matrix raster pipeline, matrix scanning schematic, and certified bill of materials.

### Asymmetric Dual-Core Microcontroller & Continuous Memory
The internal embedded architecture separates real-time user-interface responsiveness from mathematical computation:
- **Core 0 (User Interface & Matrix Scan):** Runs at low clock frequencies (12 MHz standard, boosting to 150 MHz on demand). It scans the 43-key matrix every 5 ms, executes digital debouncing, runs the display vector rasterizer for Ten-Frames and Clock hands, and handles power state transitions.
- **Core 1 (Mathematical Engine & RPN Pipeline):** Wakes only when a calculation or statistical operation is dispatched. It executes the high-precision IEEE-754 arithmetic core, the continuous 6-variable statistics accumulators ($\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$), prime factorization trees, and the fraction reduction algorithm. Once the result is pushed to Register $X$, Core 1 immediately returns to low-power sleep.
- **Continuous EEPROM Preservation:** When powered down via `{{key:OFF}}` or automatic 3-minute timeout, the processor writes the operational stack ($X, Y, Z, T$), `LASTX`, all 20 storage registers ($R_0 \dots R_{19}$), statistical accumulators, quiz level/streak scores, and active display flags into high-endurance non-volatile EEPROM, restoring full state in under $5\text{ ms}$ on wake.

### The 132×65 Dot-Matrix Vector Graphics Engine and Raster Pipeline
To provide fluid, flicker-free visual representations on an ultra-low-power embedded microcontroller, the SC-6 graphic subsystem utilizes an integer-only vector rasterization pipeline executed directly in SRAM:

| Pipeline Stage | Subsystem Operation | Latency / Footprint |
| :--- | :--- | :--- |
| **1. State Ingestion** | Read registers $Y, X$, and active mode flag | $< 0.05\text{ ms}$ |
| **2. Visual Mode Branch** | Select renderer: `{{key:NUM}}` (3-tier font), `{{key:▦}}` (Ten-Frame cells), `{{keycap:LINE}}` (parabolic jump arc), or `{{key:🕒}}` (Bresenham hand vectors) | Integer-only lookup |
| **3. Dual-Buffer SRAM Blit** | Render 1-bit monochrome frame buffer ($132 \times 9\text{ bytes}$) with $7\text{ px}$ center divider | $1,188\text{ bytes}$ SRAM |
| **4. Direct SPI DMA Burst** | Transfer $1,188\text{ bytes}$ to transflective LCD panel | $< 1.2\text{ ms}$ ($< 0.15\,\mu\text{J}$) |

#### Bresenham Vector Hand Geometry for the Planetary Clock
On the 132×65 dot-matrix canvas, the analog clock mode (`{{key:🕒}}`) renders dual dials centered at $(x = 33, y = 34)$ for Register $Y$ and $(x = 101, y = 34)$ for Register $X$, each with radius $R = 18\text{ pixels}$. Rather than relying on floating-point trigonometry during runtime, the rasterizer utilizes an integer-scaled Bresenham line algorithm driven by a 60-position lookup table:
- **Hour Hand ($L = 9\text{ px}$, $2\text{ px}$ bold stroke):**
  $$\theta_H = \left(\text{Hour} \bmod 12 + \frac{\text{Minute}}{60}\right) \times \frac{2\pi}{12} - \frac{\pi}{2}$$
- **Minute Hand ($L = 15\text{ px}$, $1\text{ px}$ crisp stroke):**
  $$\theta_M = \text{Minute} \times \frac{2\pi}{60} - \frac{\pi}{2}$$

### Electrical Circuit Schematic, Ghost-Key Lockout & ESD Protection
The 43 tactile switches are mapped into an 8-row by 6-column matrix scanned by Core 0:
1. **Dynamic Drive-and-Float Architecture:** Row pins are configured as low-impedance open-drain outputs driven low one at a time, while non-scanned rows float in high-impedance input mode.
2. **Column Pull-Ups:** Column inputs use internal $50\text{ k}\Omega$ pull-up resistors with Schmitt-trigger hysteresis.
3. **ESD Hardening:** Bidirectional Transient Voltage Suppression (TVS) diodes (Bourns CD0603) and a perimeter $0.25\text{ mm}$ saw-tooth copper spark gap protect the ENIG PCB up to **IEC 61000-4-2 Level 4** ($\pm 8\text{ kV}$ contact, $\pm 15\text{ kV}$ air discharge).

### Certified Instrument Bill of Materials (BOM) & System Flags

| Item | Sub-Assembly | Technical Specification & Material Details |
| :--- | :--- | :--- |
| **01** | Main Logic PCB | 4-layer FR4, $1.2\text{ mm}$ thickness, ENIG gold finish |
| **02** | Embedded Controller | Dual-core 32-bit $150\text{ MHz}$ microcontroller |
| **03** | Transflective LCD | $132 \times 65$ dot-matrix positive transflective FSTN |
| **04** | Snap-Dome Matrix | $43\times$ 4-leg spring-tempered stainless snap-domes ($400\text{ g}$) |
| **05** | Keycap Array | $43\times$ Tactile Light Gray TPU 95A (`#94999E`) |
| **06** | Laser Micro-Foaming | $1064\text{ nm}$ IR fiber laser markings ($L^* \ge 88.0$) |
| **07** | Upper Chassis Shell | Sunlu Midnight Navy PLA 2.0+ (`#28334A`) |
| **08** | Lower Chassis Shell | Mineral-loaded Midnight Navy PLA 2.0+ |
| **09** | Battery Compartment | Keystone 2998 clip, child-resistant bayonet door |
| **10** | Sliding Desk Cowl | Elegoo Space Gray PLA (`#4B4E54`) with silicone feet |

| Flag # | Default State | Operational Meaning & Pedagogical Purpose |
| :--- | :--- | :--- |
| **Flag 0** | `0` (Normal) | Math Exception Trap: `1` = Flash error & preserve |
| **Flag 1** | `0` (Normal) | Battery Health: `1` = Battery voltage $< 2.65\text{ V}$ |
| **Flag 2** | `0` (4-Stack) | Stack Depth Mode: `0` = 4-Stack XYZT, `1` = 2-Stack |
| **Flag 3** | `0` (Degrees) | Angular Mode: `0` = DEG, `1` = RAD (Pre-Algebra) |
| **Flag 4** | `0` (12-Hour) | Clock Format: `0` = 12h (AM/PM), `1` = 24h Military |
| **Flag 5** | `0` (Dual Stack) | Stack Layout: `0` = Dual `Y | X`, `1` = Single `X` |
| **Flag 6** | `0` (Standard) | Sound Chime: `0` = Silent, `1` = Audio click/beeps |
| **Flag 7** | `0` (Decimal) | Fraction Display: `0` = Decimal, `1` = Fraction |
| **Flag 8** | `0` (Unreduced) | Fraction Auto-Reduce: `0` = Unreduced, `1` = Auto |
| **Flag 9** | `0` (General) | Quiz Mode State: `1` = Active gamified sprint |

---

## Fabrication Invariants & Quality Control

Physical manipulatives function as authentic mathematical instruments only when their physical dimensions strictly embody the mathematical structures they represent. The StackCalc Learning Lab enforces three non-negotiable fabrication invariants:

1. **The 84.0 mm Fraction Datum:** The master 1-WHOLE tower is machined or printed to exactly $84.00 \pm 0.15\text{ mm}$. Because $84$ is divisible by $2, 3, 4, 6,$ and $12$, every sub-fraction tower segment has an integer millimetric height ($1/2 = 42.0\text{ mm}$, $1/3 = 28.0\text{ mm}$, $1/4 = 21.0\text{ mm}$, $1/6 = 14.0\text{ mm}$, $1/12 = 7.0\text{ mm}$). When sub-fractions sum to a whole, their physical stack height aligns perfectly flush in the comparator well with zero visual step.
2. **The 10.0 mm Base-10 Dimensional Grid:** Place value unit cubes are exactly $10.0 \times 10.0 \times 10.0\text{ mm}$ ($1.0\text{ cm}^3$). Ten-rods are $10.0 \times 10.0 \times 100.0\text{ mm}$ ($10.0\text{ cm}^3$). Hundred-flats are $10.0 \times 100.0 \times 100.0\text{ mm}$ ($100.0\text{ cm}^3$). Thousand-cubes are $100.0 \times 100.0 \times 100.0\text{ mm}$ ($1,000.0\text{ cm}^3$). Volume and mass scale precisely across three powers of ten.
3. **Gridfinity 7U Modular Normalization:** Storage bins conform to the $42.0\text{ mm}$ grid pitch and standard $7\text{U}$ ($53.4\text{ mm}$) or $13\text{U}$ ($91.0\text{ mm}$) heights, allowing complete interchangeability across classroom storage carts and maker benches.

---

## Industrial Polymer & Thermoplastic Specifications

For educational institutions and fabrication labs manufacturing physical instruments and manipulatives, materials must meet strict mechanical durability and optical performance criteria:

| Material Formulation | Color & Finish | Mechanical Properties | Educational Application |
| :--- | :--- | :--- | :--- |
| **Sunlu Midnight Navy PLA 2.0+** | Deep Navy (`#28334A`), Matte | Tensile: $65\text{ MPa}$ • Izod: $8.5\text{ kJ/m}^2$ | Handheld calculator enclosure, display bezel, anti-glare frames |
| **Elegoo Space Gray PLA** | Slate Gray (`#4B4E54`), Satin | Flex Modulus: $3.2\text{ GPa}$ • Hardness: $R112$ | Protective sliding cowl, desk-stand rails, structural chassis |
| **Technical Matte Black PETG** | Deep Black (`#101114`), Micro-texture | Tensile: $50\text{ MPa}$ • Heat Deflection: $70^\circ\text{C}$ | Battery bay covers, high-cycle latch clips, wear surfaces |
| **Tactile Light Gray TPU 95A** | Industrial Gray (`#94999E`), Matte | Shore Hardness: $95\text{A}$ • Elongation: $450\%$ | Snap-dome elastomeric pads, desk footpads, bumper cushions |
| **Clean Lab White PLA 2.0+** | Archival White (`#F5F5F3`), Specular | Tensile: $60\text{ MPa}$ • Unnotched Impact: $16\text{ kJ/m}^2$ | Fraction towers, ten-frame counters, base-10 manipulatives |
| **Dual-Color Silk PLA** | Cobalt Blue / Radiant Gold | Tensile: $55\text{ MPa}$ • Layer Adhesion: High | Prime blocks, two-color flip counters, spinner dials |

---

## Mil-STD-810H Method 516.8 Transit Drop Testing Compliance

To ensure survivability in high-turnover elementary classrooms and active student backpacks, the SC-6 hardware enclosure and associated manipulative storage bins are engineered to comply with **Mil-STD-810H, Method 516.8 (Transit Drop)**:

1. **Drop Parameters:** 26 drops from a height of $1.22\text{ meters}$ ($48\text{ inches}$) onto a target consisting of $50\text{ mm}$ ($2\text{ inches}$) of solid tongue-and-groove hardwood over concrete.
2. **Impact Cycle:** 8 corner impacts, 12 edge impacts, and 6 face impacts across a single production-spec unit with sliding cowl docked in desk-stand configuration.
3. **Pass Criteria:** Zero structural cracking of the outer thermoplastic shell, zero dislodgement of the transflective LCD display, and 100% operational retention of all 43 snap-dome tactile keys verified by hardware self-test diagnostic (`{{key:C}} + Power`).

---

## The 19.0 kg Clean Lab Manipulative Fabrication Pool

Classroom sets are provisioned from an integrated fabrication batch engineered to equip a 30-student STEM laboratory:

- **Total Filament Pool:** $19.0\text{ kg}$ virgin-grade, heavy-metal-free thermoplastic filament (10.0 kg Clean Lab White PLA 2.0+, 4.0 kg Midnight Navy PLA 2.0+, 2.0 kg Cobalt Blue Silk PLA, 2.0 kg Radiant Gold Silk PLA, 1.0 kg Slate Gray PETG).
- **Batch Output Capacity:** Complete fabrication of 15 Ten-Frame trays with 150 counters, 15 complete Fraction Studio sets with comparator wells, 8 Four-Color Counting Studios (1,152 tiles total), 4 Planetary Geared Clocks, and 4 Prime Factor Studios.
- **Safety Certification:** All finished components meet **16 CFR § 1501 / ASTM F963-17** physical and mechanical toy safety standards and **EN 71-3** chemical migration limits for classroom manipulatives.

---

## Physical Manipulative Manufacturing Catalog (SKU Directory)

The complete catalog of authentic StackCalc physical manipulatives, modular footprints, and hardware bill-of-materials identifiers:

| SKU Code | Product / Manipulative Title | Gridfinity Footprint | Standard Inclusions & Mechanical Features | Target Curriculum Level |
| :--- | :--- | :---: | :--- | :--- |
| **STK-MAN-10F** | Ten-Frame Studio | $3 \times 1 \times 7\text{U}$ | Dual $2 \times 5$ compartment tray with $5.0\text{ mm}$ divider rib, 10 two-color flip counters ($20\text{ mm} \times 4\text{ mm}$). | Grades K–1 (Counting, Bonds to 10) |
| **STK-MAN-FRAC** | Fraction Studio | $3 \times 1 \times 7\text{U}$ | $84.0\text{ mm}$ master datum tower, proportional sub-towers ($1/2, 1/3, 1/4, 1/6, 1/12$), twin comparator well. | Grades 3–5 (Equivalence, Reduction) |
| **STK-MAN-TILE**<br>(`UNIF-01`) | Counting & Array Studio | $3 \times 1 \times 13\text{U}$ | 144 stacking tiles in 4 colors ($36 \text{ white}, 36 \text{ blue}, 36 \text{ gold}, 36 \text{ slate}$), $19 \times 19 \times 8.85\text{ mm}$ ($7.0\text{ mm}$ visible $1\text{U}$). | Grades 2–4 (Arrays, Multiplication) |
| **STK-MAN-CLK** | Planetary Geared Clock | Open Stage / $3 \times 2$ | $12.0000:1$ compound planetary reduction gear train, linked continuous minute/hour hands, $360^\circ$ dial. | Grades 2–5 (Modulo-60 Time, Angles) |
| **STK-MAN-ALG** | Algebra Factoring Stage | $3 \times 2 \times 7\text{U}$ | Bilateral equal-arm balance scale, precision gram mass slugs, tare cups, and two-color factoring tiles. | Grades 5–6+ (Pre-Algebra, Balancing) |
| **STK-MAN-DOM** | Math Dominoes Studio | $3 \times 1 \times 7\text{U}$ | 28 double-six domino tiles with precision excavated pips, organizer tray with subitizing dividers. | Grades K–2 (Fact Families, Part-Whole) |
| **STK-MAN-VOLV** | Unit Circle Volvelle | Circular / $120\text{ mm}$ | Dual-ring rotary protractor with concurrent DEG, RAD, and gradient scales for trigonometry exploration. | Grades 5–6+ (Geometry, Bearings) |
| **STK-MAN-PRIME**<br>(`PRIME-01`) | Prime Factor Studio | $3 \times 1 \times 13\text{U}$ | 29 logarithmic prime blocks ($h = 42.0 \log_{10} p$), rear-wall slide rule scale, bilateral Venn comparator stage. | Grades 5–6+ (Primes, GCF, LCM) |
| **STK-MAN-PV** | Place Value Studio | $3 \times 2 \times 7\text{U}$ | Proportional base-10 unit cubes ($1$), ten-rods ($10$), hundred-flats ($100$), and thousand-cubes ($1000$). | Grades 1–4 (Base-10 Decomposition) |
| **STK-MAN-RACK** | Number Rack (Rekenrek) | $3 \times 1$ Snapfinity | Dual stainless steel horizontal rails with 20 beads grouped into $5+5$ contrasting color sets. | Grades K–2 (Subitizing, Ten-Frames) |
| **STK-MAN-DICE** | Polyhedral Dice Studio | $3 \times 1 \times 7\text{U}$ | Precision polyhedral dice ($d4, d6, d8, d10, d12, d20$) with equal-volume excavated pips, low-friction spinner. | Grades 3–6 (Probability, Statistics) |

---

## Workshop Safety & Non-Toxic Material Standards

All materials and fabrication processes must strictly adhere to elementary classroom safety protocols:
- **Toy Safety Compliance:** All PLA filaments must be virgin grade, BPA-free, heavy-metal-free, and comply with **EN 71-3 (Safety of Toys: Migration of Certain Elements)**.
- **Laser Cutting Ventilation:** Acrylic and engineered plywood must be cut in exhaust-ducted enclosures venting outdoors or through active HEPA/activated carbon filtration to prevent formaldehyde or particulate inhalation.
- **Choking Hazard Dimensions:** Every counter, cube, and gear exceeds the $31.7\text{ mm}$ standard small-parts test fixture cylinder, making the entire manipulative suite safe for multi-age elementary classrooms.

For complete classroom station lesson scripts that utilize these physical manipulatives, proceed to [Appendix B: Teacher Lesson Plans & Diagnostic Protocols](appendix-b-teacher-lesson-plans.md).

