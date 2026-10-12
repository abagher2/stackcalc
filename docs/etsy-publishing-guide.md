---
title: "Etsy Storefront Publishing & Sourcing Guide"
description: "Step-by-step operations manual for publishing StackCalc physical products on Etsy, complete asset index, and Batch 001 in-house vs. Slant3D sourcing analysis."
---

# Etsy Storefront Publishing & Sourcing Guide

This operations guide provides a complete, step-by-step walkthrough for launching and managing the **StackCalc Etsy Storefront**, accompanied by the strategic manufacturing assessment for **Batch 001 In-House Printing vs. Slant3D Additive Sourcing**.

---

## 1. Sourcing Strategy: In-House Printing vs. Slant3D for Batch 001

### Strategic Recommendation: The "In-House Pilot &rarr; Slant3D Farm Scale" Hybrid Model

> **Executive Summary:**  
> **Print Batch 001 (5 units per SKU: 1 studio master copy + 4 ready-to-ship boxed copies) IN-HOUSE.**  
> Do not outsource Batch 001 completely to Slant3D. Maintain full in-house control over the inaugural release, then transition high-volume, single-material components to Slant3D once sales velocity is established.

```
                    BATCH 001 (LAUNCH & PILOT)             BATCH 002+ (SCALE)
┌──────────────────┐  In-House High-Precision Printing      In-House Assembly & QA
│ SC-32 Calculator │ ─────────────────────────────────► ─────────────────────────────►
│ (Dovetail + TPU) │  • 0.15mm TPU membrane (Azure)         • Pre-soldered SMT PCB
│                  │  • Archimedean micro-groove faceplate  • Multi-material faceplates
└──────────────────┘  • 0.20mm sliding rail calibration    • Final serialized testing

┌──────────────────┐  In-House Textured PEI Pilot           Slant3D Additive Farm
│ Math             │ ─────────────────────────────────► ─────────────────────────────►
│ Manipulatives    │  • 10-20 units per SKU                 • High-volume PLA printing
│ (Fraction, Clock)│  • Zero MOQ, zero lead time wait       • Automated fulfillment
└──────────────────┘  • Immediate OpenSCAD CAD tuning       • Monolithic trays & blocks
```

### Detailed Engineering & Economic Comparison

| Strategic Dimension | In-House 3D Printing (Batch 001) | Direct Slant3D Sourcing (Batch 001) | Winner for Batch 001 |
|---|---|---|:---:|
| **Mechanical Tolerances** | **High Precision ($0.20\,\text{mm}$ dovetails):** Calibrated on tuned Bambu/Prusa machines. Tool-free sliding rails glide smoothly without binding or slop. | **Standard Industrial ($0.40–0.60\,\text{mm}$):** Slant3D uses high-flow production nozzles; tight sliding tongue-and-groove joints can bind or require manual post-cleanup. | **In-House** |
| **Multi-Material / CMF** | **Full CMF Capability:** Can print Shore 95A flexible TPU membranes, anisotropic silk PLAs, frosted optical PETG, and Archimedean spiral concentric toolpaths. | **Single-Material PLA/PETG:** Slant3D farm lines do not support multi-material TPU co-molding, special silk gradients, or laser foil inlays. | **In-House** |
| **Inventory & Cash Risk** | **Zero Upfront Inventory:** Print on-demand or keep 5–10 kits boxed on the shelf. Zero capital tied up in unsold units. | **Batch MOQ / Setup Overhead:** Outsourcing small test runs incurs setup fees, shipping freight, and MOQ constraints. | **In-House** |
| **Rapid Iteration Cycle** | **Immediate (10 minutes):** If an early customer reports a fraction block or algebra tile is 0.1mm too snug, you modify the OpenSCAD code and print the corrected part immediately. | **Slow (2–4 weeks):** Re-uploading CAD, queueing at the farm, batch fabrication, and ground freight back to your shop. | **In-House** |
| **First Review Reputation** | **Boutique Surface Finish:** Textured PEI plates, dialed retraction ($0.98$ flow), and hand-checked snap retention generate enthusiastic 5-star Etsy reviews. | **Factory Finish:** Quality is consistent for volume parts, but lacks the hand-inspected artisan feel needed for early Listing Quality Score (LQS). | **In-House** |
| **High-Volume Unit Cost** | Higher labor cost per unit if scaled past 100 units/month. | **Lowest Cost at Scale:** Robotic automated ejection and bulk filament pricing dominate at $>100$ units. | **Slant3D (Scale)** |

### When to Trigger the Slant3D Hand-Off (Batch 002+ Milestone)
Transition parts to Slant3D when:
1. **Steady Velocity:** A manipulative SKU sells $>20$ units per month, or a school district places a PO for $>10$ classroom kits ($>150$ total trays/boxes).
2. **Stable Geometry:** The OpenSCAD CAD code has zero geometry adjustments across 30 days of classroom feedback.
3. **Component Suitability:** Outsource the monolithic, high-part-count components (e.g. Fraction Studio towers, Gridfinity boxes, Ten-Frame carry shelves) while continuing to assemble, QA, and package in-house with the SC-32 electronics.

---

## 2. Pre-Publishing Master Directory & Asset Index

All 8 launch listings have complete, pre-validated copy-paste Markdown packages located in the repository at `watch-calc-32/documentation/etsy/`. Master images are generated in high-resolution $2000 \times 2000$ (1:1 Square) and $2000 \times 1500$ (4:3 Horizontal) in `stackcalc/docs/assets/renders/etsy/`.

### Master Listing Catalog

| SKU | Product Listing Guide | Base Price | Primary 1:1 Image Asset | 4:3 Context Banner Asset |
|---|---|:---:|---|---|
| `SC-32-HW` | SC-32 RPN Calculator | \$89.00 | `sc32-hero-keynote-square.png` | `sc32-hero-keynote-4x3.png` |
| `FRAC-01` | Fraction Studio Towers | \$38.00 | `fraction-studio-hero-square.png` | `fraction-studio-hero-4x3.png` |
| `ALGB-01` | Algebra Factoring Studio | \$34.00 | `algebra-boxes-hero-square.png` | `algebra-boxes-hero-4x3.png` |
| `TIME-01` | Classroom Planetary Clock | \$36.00 | `clock-classroom-hero-square.png` | `clock-classroom-hero-4x3.png` |
| `BASE-10` | Ten-Frames & Counters | \$28.00 | `ten-frames-hero-square.png` | `ten-frames-hero-4x3.png` |
| `PROB-01` | Probability Dice & Spinner | \$29.00 | `dice-spinner-hero-square.png` | `dice-spinner-hero-4x3.png` |
| `TRIG-01` | Unit Circle Trig Volvelle | \$16.00 | `unit-circle-volvelle-hero-square.png` | `unit-circle-volvelle-hero-4x3.png` |
| `DOMI-01` | Math Domino Studio | \$29.00 | `dominoes-studio-hero-square.png` | `dominoes-studio-hero-4x3.png` |
| `DIGI-01` | Complete 3D Print STL Bundle | \$19.00 | `algebra-tiles-craftsmanship-square.png` | `algebra-boxes-hero-4x3.png` |
| `REPLACE-01` | Lifetime Replacement Parts Service | \$2.49+ | `infographic-guarantee-safety-square.png` | `infographic-guarantee-safety-square.png` |

---

## 3. Step-by-Step Publishing Guide (Etsy Shop Manager)

Follow this exact 9-step procedure for every product listing to maximize conversion rate and guarantee compliance with Etsy's 2026 search ranking algorithms.

### Step 1: Photos & Video Upload (10/10 Slots Filled)
1. Open **Etsy Shop Manager** &rarr; **Listings** &rarr; **Add a listing**.
2. Drag and drop all 10 image assets from `watch-calc-32/documentation/etsy/images/` according to the carousel order specified in each listing's Markdown file:
   - **Slot 1 (Primary Thumbnail):** `*-hero-square.png` (Crisp 1:1 square render on clean studio background).
   - **Slot 2 (Context Banner):** `*-hero-4x3.png` (Wide contextual angle showing desk integration).
   - **Slots 3–6 (Features & Craftsmanship):** Close-up macro shots of tactile surfaces, debossed text, and modular dovetails.
   - **Slot 7 (Technical Specs Infographic):** Pre-generated blueprint infographic showing dimensions, grades, and parts.
   - **Slot 8 (Ecosystem):** Docking onto standard 42mm Gridfinity desktop trays.
   - **Slot 9 (Accessories):** Reconfigurable desk stand or protective TPU sleeve.
   - **Slot 10 (Safety & Trust Infographic):** Lifetime piece guarantee, non-toxic material badge, CPSIA notice.
3. **Upload Product Video:** Drag and drop the corresponding MP4 video from `stackcalc/docs/assets/videos/` (5–15 second silent 1080p demonstration).
4. **Fill In Image Alt Text:** Click each image thumbnail in Etsy and paste the exact pre-written descriptive Alt Text provided in Section 3 of the listing markdown file (essential for Google Image Search and accessibility).

### Step 2: Listing Title & Category Placement
1. **Title:** Copy the front-loaded title from Section 1 of the product markdown file.
   - *Example:* `RPN Scientific Calculator - StackCalc SC-32 Open Hardware RP2350 Tactile Keypad Pocket Calculator for STEM & Exam Use`
   - *Why:* The first 40 characters contain the primary keywords (`RPN Scientific Calculator - StackCalc SC-32`) to prevent truncation on mobile screens.
2. **Category Selection:**
   - For SC-32: `Home & Living > Office > Office Supplies > Calculators`
   - For Manipulatives: `Toys & Games > Learning & School > Math Toys` (or `Office Supplies > Desk Organizers`)

### Step 3: Product Attributes & Search Facets
Select all relevant attributes in Etsy Shop Manager to ensure your item appears when shoppers filter search results:
- **Primary Color / Finish:** (e.g. `Black` for Stealth, `White` for Retrofuturism, `Blue` for Voyager).
- **Primary Material:** `Plastic` (or `Bioplastic / PLA`).
- **Subject:** `Mathematics`, `Engineering & Technology`, `Computer Science`.
- **Target Age / Grade:** Select matching grade range (`Kindergarten–3rd` for Ten-Frames, `Grade 3–8` for Fractions, `High School/College` for SC-32 & Algebra).

### Step 4: Product Description & Safety Statements
1. Copy the full formatted description from Section 4 of the listing markdown file.
2. Verify that the **Mandatory Safety Disclaimer** is intact:
   ```markdown
   WARNING: CHOKING HAZARD – Small parts.
   Not for children under 3 years. Recommended for ages 6+ under adult supervision.
   ```
3. Highlight the **"No Lost Piece Left Behind" Lifetime Guarantee**:
   > *"Classrooms lose pieces. If a student loses any fraction block, algebra tile, or counter, we provide exact matching replacement parts starting at $2.49 for the lifetime of the product, matched to the Part ID on your included Archival Reference Card."*

### Step 5: Production Partner Declaration
Etsy requires makers to disclose production assistance under their **Creativity Standards**:
1. Scroll to **Production Partners**.
2. Select your registered production partner profile:
   - **For Batch 001 (In-House):** Check *"I make this item myself"* (StackCalc California Studio).
   - **For Batch 002+ (Slant3D):** Select `Slant 3D` (Boise, Idaho) with the note: *"Custom 3D CAD design, circuit schematic, firmware, and quality control performed in-house; contract farm printing by Slant 3D."*

### Step 6: 13/13 Search Tag Saturation
Copy all 13 exact-match tags from Section 2 of the listing file. Enter each tag individually (all under 20 characters):
- *Example for SC-32:* `rpn calculator`, `pocket calculator`, `stem calculator`, `math engineering`, `hp calculator`, `coder desk toy`, `engineer gift`, `sat test calculator`, `rp2350 hardware`, `retro calculator`, `tactile keyboard`, `college math tool`, `physics calculator`.
- *Rule:* Use all 13 tags. Never leave empty tag slots.

### Step 7: Dropdown Variations & Bundle Pricing (CRO Booster)
Enable **Variations** in the listing editor to provide tier options that increase Average Order Value (AOV):
- **Option 1 (Individual Kit):** Base retail price (e.g., $34.00 – $89.00).
- **Option 2 (Field Bundle / Founder Pack):** Base unit + TPU protective pouch + desktop stand packaging (+$20.00 – $26.00).
- **Option 3 (Classroom 5-Pack Station):** 5 identical kits + bulk teacher lesson guide with a 10–15% district discount.

### Step 8: Standardized Shipping Profile Selection
Select the pre-configured USPS Ground Advantage shipping profile:
- **Profile A (Small Manipulative - 5.1 oz):** \$4.49 (or Free on orders \$35+).
- **Profile B (Learning Box - 10.9 oz):** \$5.49 (or Free on orders \$35+).
- **Profile C (SC-32 Calculator - 12.7 oz):** \$5.99 (or Free on orders \$35+).
- **Profile E (Replacement Envelope - 1.2 oz):** Included in base refill tier.
- **Processing Time:** Set to `1–3 business days` (or 24 hours for refills).

> [!TIP]
> For complete dimensional box engineering, duplex $135 \times 90\,\text{mm}$ reference card workflows (high-speed laser paper vs. monochrome laser engraving), and the 6-step bench packing protocol, see the [Shipping, Packaging & Fulfillment Protocol](shipping-and-packaging.md).

### Step 9: Publish & Initial Ranking Boost
1. Click **Publish** (listing fee: \$0.20 USD).
2. **Initial Social Proof:** Send the listing URL to your pilot educator mailing list. Etsy heavily weights initial click-through rate (CTR) and conversion velocity in its first 72 hours.
3. Link the Etsy listing URL directly into the official documentation and master catalog at `stackcalc.io/products/`.

---

## 4. Git Hash Tracking & 50% Anti-Arbitrage Replacement Workflow

### 4.1 The 50% Anti-Arbitrage Pricing Formula
To prevent customers or third parties from buying individual components to assemble full kits piecemeal, all replacement parts are priced at **50% above the amortized per-piece price** of the full retail kit ($1.5 \times \text{Amortized Cost}$):
- **Small Tile / Counter / Single Domino Tile:** \$2.25 – \$2.49 (Amortized \$1.50–\$1.66)
- **Trio Small Tiles / Domino 6-Pack:** \$3.99 – \$6.75 (Amortized \$2.66–\$4.50)
- **Linear Rod / Medium Tower:** \$3.49 – \$4.95 (Amortized \$2.33–\$3.30)
- **Quadrant Wedge / Clock Hand:** \$5.25 – \$6.00 (Amortized \$3.50–\$4.00)
- **12-Frame Math Tray / Doubling Lid / Quadratic x² Tile:** \$6.49 – \$7.50 (Amortized \$4.33–\$5.00)
- **Whole Block / 3x1x7U Storage Box / Complete Stand:** \$11.25 – \$22.50 (Amortized \$7.50–\$15.00)
- **Planetary Gear Core / SC-32 Bezel:** \$18.00 – \$24.00 (Amortized \$12.00–\$16.00)

*Anti-Arbitrage Result:* Assembling an entire kit piecemeal costs $>2.2\times$ the boxed retail price, eliminating part-out arbitrage while keeping single-piece replacement affordable for honest classrooms.

### 4.2 Automated Git Content-Addressed Manifest Tracking (Zero Version Churn)

A common concern with Git-based versioning is: *"Does every commit to the repository bump the version of all physical parts?"*  
**No.** We eliminate global version churn by leveraging Git's fundamental content-addressing architecture:

1. **Git Content Blob Hashes (`git hash-object`):**
   - The primary ID for every STL model is its Git Blob SHA (e.g., `0bf1e7f` for `algebra_factoring_box.stl`).
   - This SHA is computed strictly from the uncompressed byte content of the 3D geometry file (`SHA-1("blob " + size + "\0" + bytes)`).
   - **Invariance Guarantee:** Whether you make 1 commit or 10,000 commits to documentation, website pages, or Swift calculator code, the Git Blob Hash for that physical part **never changes**. It is 100% frozen in time until someone actually alters that specific CAD model.

2. **Path-Scoped CAD Commits (`git log -1 -- <file>`):**
   - When referencing authoring Git commits, the tooling queries the exact file: `git log -1 --format="%h" -- Education/scad/fraction_studio_box.scad`.
   - Commits elsewhere in the monorepo do not alter this commit stamp. It only advances when that component's CAD code is modified.

3. **Part Identification Syntax:**
   - Standard Part ID format: `<KIT_CODE>-<COMPONENT_SLUG>-<BLOB_SHA>` (e.g., `FRAC-FRAC-eba4c3e`, `SC-CHAS-436ba32`).
   - Customers can quote either the full Part ID, the debossed 7-character Git Blob Hash (`eba4c3e`), or the CAD commit (`a793ddd`).
   - **Automated Manifest Tool (`Tools/generate_part_manifest.py`):**
     ```bash
     # Regenerate the master part manifest and anti-arbitrage pricing:
     python3 Tools/generate_part_manifest.py

     # Reverse lookup any customer Git Blob Hash, commit, or component:
     python3 Tools/generate_part_manifest.py --lookup eba4c3e
     ```
     The lookup instantly prints the component name, exact immutable Git blob SHA, CAD source commit, amortized cost, 50% anti-arbitrage price, and exact Git export command (`git cat-file -p <blob_sha> > component.stl`).

### 4.3 The Etsy Replacement Parts Workflow
1. **Customer Order:** A customer who lost a piece visits our dedicated Etsy listing (`SC-REPLACE-01`).
2. **Personalization Box:** The buyer provides 3 details:
   - Target Set (e.g. *Fraction Studio*, *Algebra Factoring*, *SC-32*)
   - Missing Part & Color (e.g. *1/8 Eighth Block in Azure Blue*, *Linear x Rod in Coral*)
   - Part ID or Git Hash: Matched directly from the **Archival Reference Card** included inside their kit's box lid (or the underside inspection plaque on the box/chassis, e.g. `FRAC-01-eba4c3e` or `a793ddd`).
3. **Automated CAD Slicing:** The fulfillment technician runs `python3 Tools/generate_part_manifest.py --lookup <ID>`, checks out the exact historical OpenSCAD commit, and slices on textured PEI.
4. **24-Hour Dispatch:** The replacement part is dispatched in a rigid stay-flat mailer envelope via standard USPS First Class mail with flat tracking.

---

## 5. Battery-Free Shipping Compliance Policy

> [!IMPORTANT]
> **Strict Postal Compliance: NO BATTERIES SHIPPED IN ANY PACKAGE.**  
> In compliance with USPS Publication 52 (Hazardous Materials), FAA safety regulations, and IATA Class 9 (UN 3090 / UN 3091) air transport restrictions, **StackCalc does not include lithium coin cell batteries in physical calculator shipments**.

### Operational Rationale & Benefits:
1. **Zero Hazmat Labeling & Airmail Friction:** Lithium cells trigger complex DOT/USPS Section 349 shipping rules, hazardous materials declarations, package labeling mandates, and restrictions on international priority airmail.
2. **Eliminated Fire & Ingestion Liability:** Eliminates Reese's Law (16 CFR Part 1263) pre-installed battery testing certification requirements for shipping packages.
3. **Universal Accessibility:** The SC-32 uses a standard, ubiquitous CR2032 3V coin cell available at any grocery store, pharmacy, or hardware store for ~$0.50, and can also run continuously on any standard USB-C desktop cable with zero battery installed.
4. **Transparent Customer Notice:** Every calculator listing and package insert clearly states:  
   *"Requires 1x standard CR2032 coin cell (widely available, not included due to postal carrier safety regulations) or standard USB-C desktop power."*

---

## 6. Comprehensive Item-by-Item Packing Checklists

Before sealing each mailer, warehouse fulfillment must execute the specific checklist for the SKU being dispatched. All boxed kits must include their dedicated **Archival Reference & Schematic Card** to serve as the master inventory, schematic diagram, and lifetime replacement ledger:

> [!TIP]
> **Packing Bench Web Tool:** Open [`docs/downloads/packing_bench_cards.html`](downloads/packing_bench_cards.html) on any desktop or tablet for instant 1-click printable packing bench sheets with full CAD schematics and Part ID verification checkmarks.

### 1. SC-32 Scientific RPN Calculator (Standard Hardware Kit)
- **Packaging:** Profile C Mailer ($9 \times 6 \times 3\text{ in}$ Rigid Corrugated Mailer Box)
- **Target Weight:** ~360 g (12.7 oz) packed
- **Physical Contents:**
  - [ ] 1x Assembled SC-32 Calculator (or unpopulated DIY snap kit: RP2350 SMT mainboard, chassis shell, top cap, TPU membrane, faceplate)
  - [ ] 4-Piece Interlocking Puzzle Stand (seated as internal packaging trusses or flat nested)
  - [ ] **NO BATTERY VERIFICATION:** Confirmed battery compartment is completely empty (no CR2032 cell inside per postal rules).
- **Printed Collateral & Cards:**
  - [ ] 1x Archival Reference & Schematic Card (`SC-32-HW`, with exploded assembly, puzzle stand diagram, Part IDs, and specs)
  - [ ] 1x Double-Sided Credit Card RPN Reference Guide (`reference_card_front.svg` / `reference_card_back.svg`)
  - [ ] 1x Power & Safety Slip: *"Requires 1x CR2032 coin cell or USB-C cable (battery omitted per USPS/ICAO air safety)"*
- **Pre-Sealing QA Gate:**
  - [ ] Sliding faceplate dovetail glide test (smooth engagement, no binding)
  - [ ] All 43 tactile snap-domes actuate cleanly with distinct audible snap
  - [ ] ST7567A transflective LCD bezel centered in cowl aperture
  - [ ] Underside inspection plaque verified: Mirrored `Space Mono Bold` deboss on chassis bottom

---

### 2. SC-32 Engineer's Field Bundle / Founder Pack
- **Packaging:** Profile C Mailer ($9 \times 6 \times 3\text{ in}$ Rigid Corrugated Mailer Box)
- **Target Weight:** ~420 g (14.8 oz) packed
- **Physical Contents:**
  - [ ] 1x Assembled SC-32 Calculator
  - [ ] 4-Piece Interlocking Puzzle Stand
  - [ ] 1x Reversible Shore 95A Flexible TPU Protective Cozy Pouch
  - [ ] 1x Premium 1m Braided USB-C to USB-C Cable
  - [ ] 1x Founder's Serialized Rear Nameplate (inspected for crisp Space Mono laser engraving)
  - [ ] **NO BATTERY VERIFICATION:** Confirmed battery compartment is empty.
- **Printed Collateral & Cards:**
  - [ ] 1x Archival Reference & Schematic Card (`SC-32-HW`)
  - [ ] 1x Double-Sided Credit Card Reference Guide
  - [ ] 1x Founder's Welcome Letter & Quick-Start Slip
  - [ ] 1x Battery Postal Safety & Lifetime Guarantee Postcard

---

### 3. SC-6 Elementary RPN Calculator
- **Packaging:** Profile B Mailer ($8 \times 6 \times 3\text{ in}$ Heavyweight Mailer Box)
- **Target Weight:** ~290 g (10.2 oz) packed
- **Physical Contents:**
  - [ ] 1x SC-6 Elementary Calculator (Sunlu White PLA 2.0+ lab chassis, Slate Gray sliding cowl, tactile snap-dome keypad)
  - [ ] 1x 2-Piece Folding Desk Wedge Stand
  - [ ] **NO BATTERY VERIFICATION:** Confirmed battery cavity is empty.
- **Printed Collateral & Cards:**
  - [ ] 1x SC-6 Elementary Student Quick-Start Card (`sc6_guide_card.png`)
  - [ ] 1x Parental Power Notice: *"Requires 1x CR2032 or USB-C (battery omitted per postal rules)"*
  - [ ] 1x Safety & Choking Hazard card (Ages 6+) + Lifetime Warranty card

---

### 4. Fraction Studio Proportional Towers (Full Classroom Kit)
- **Packaging:** Profile B Mailer ($8 \times 6 \times 3\text{ in}$ Heavyweight Mailer Box)
- **Target Weight:** ~310 g (10.9 oz) packed
- **Physical Contents:**
  - [ ] 15x Debossed 4-Face Proportional Blocks (100% clean math blocks, free of technical alphanumeric codes):
    - [ ] 1x Whole Block (1.0 / 100% / 360°)
    - [ ] 2x Half Blocks (1/2 / 0.50 / 50% / 180°)
    - [ ] 4x Quarter Blocks (1/4 / 0.25 / 25% / 90°)
    - [ ] 8x Eighth Blocks (1/8 / 0.125 / 12.5% / 45°)
  - [ ] 1x 42mm Gridfinity Storage Tray with sliding locking lid
- **Printed Collateral & Cards:**
  - [ ] 1x Archival Reference & Schematic Card (`FRAC-01`, with exploded isometric schematic, Part IDs `FRAC-01-eba4c3e`, piece counts, and replacement instructions)
  - [ ] 1x Fraction Equivalence Pocket Reference Guide (`card_fractions-pocket-guide.svg`)
  - [ ] 1x CPSIA Choking Hazard Card (Ages 6+ notice for eighth blocks)
- **Pre-Sealing QA Gate:**
  - [ ] Blocks stand flush on tabletop without tipping; debossed notation is crisp and legible
  - [ ] Clean Manipulatives Check: Student blocks verified 100% free of distracting technical hashes
  - [ ] Underside inspection plaque verified: Mirrored `Space Mono Bold` deboss on storage box lid underside

---

### 5. Algebra Factoring Studio & Polynomial Tiles
- **Packaging:** Profile B Mailer ($8 \times 6 \times 3\text{ in}$ Heavyweight Mailer Box)
- **Target Weight:** ~340 g (12.0 oz) packed
- **Physical Contents:**
  - [ ] 1x Dual-L Factoring Stage with perimeter slotted factoring rails
  - [ ] 38x Chamfered Polynomial Tiles (100% clean math tiles with $+x^2/-x^2$ badges only, zero technical hashes):
    - [ ] 4x $x^2$ Large Quadratic Tiles (dual-color / debossed)
    - [ ] 10x $x$ Linear Rectangle Tiles
    - [ ] 24x $1$ Unit Constant Square Tiles
  - [ ] 1x 42mm Gridfinity 3x1 Storage Box with debossed lid
- **Printed Collateral & Cards:**
  - [ ] 1x Archival Reference & Schematic Card (`ALGB-01`, with factoring stage schematic, Part IDs `ALGB-01-a793ddd`, piece counts, and QC checkmarks)
  - [ ] 1x Binomial Factoring Quick Reference Guide (`algebra_tiles-pocket-guide.svg`)
  - [ ] 1x Safety Card (Small parts: unit tiles)
- **Pre-Sealing QA Gate:**
  - [ ] Tiles seat smoothly into the L-frame stage rails without catching
  - [ ] Clean Manipulatives Check: Student tiles verified 100% free of technical alphanumeric codes
  - [ ] Underside inspection plaque verified: Mirrored `Space Mono Bold` deboss on storage box base

---

### 6. Sectional Classroom Planetary Clock
- **Packaging:** Profile B Mailer ($8 \times 6 \times 3\text{ in}$ Heavyweight Mailer Box)
- **Target Weight:** ~320 g (11.3 oz) packed
- **Physical Contents:**
  - [ ] 1x Synchronized 12:1 Internal Planetary Gear Core
  - [ ] 1x Hour Hand + 1x Minute Hand (pre-synchronized to 12:00)
  - [ ] 4x Removable 5-Minute Quadrant Wedges (:15, :30, :45, :00)
  - [ ] 1x 42mm Gridfinity 2x1 Desktop Showcase Stand
- **Printed Collateral & Cards:**
  - [ ] 1x Archival Reference & Schematic Card (`TIME-01`, with exploded planetary gear schematic, Part IDs `TIME-01-xxxxxxx`, and ratio specs)
  - [ ] 1x Clock Mechanics & Elapsed Time Student Activity Guide (`clock_quadrants-pocket-guide.svg`)
  - [ ] 1x Safety & Replacement Service Card
- **Pre-Sealing QA Gate:**
  - [ ] Hands rotate smoothly 360° with positive 12:1 gear engagement; quadrants seat securely
  - [ ] Underside inspection plaque verified: Mirrored `Space Mono Bold` deboss on stand base

---

### 7. Dual Ten-Frames & Carry Shelf Set
- **Packaging:** Profile B Mailer ($8 \times 6 \times 3\text{ in}$ Heavyweight Mailer Box)
- **Target Weight:** ~280 g (9.9 oz) packed
- **Physical Contents:**
  - [ ] 2x 2x5 Ten-Frame Grid Stages
  - [ ] 1x Elevated Regrouping Carry Shelf with dock latch
  - [ ] 20x Bi-Color Tactile Counting Counters (100% clean manipulatives, zero technical codes)
  - [ ] 1x 42mm Gridfinity 3x1 Storage Caddy
- **Printed Collateral & Cards:**
  - [ ] 1x Archival Reference & Schematic Card (`BASE-10`, with stage schematics, Part IDs `BASE-10-xxxxxxx`, and QC checkmarks)
  - [ ] 1x Base-Ten Regrouping & Make-a-Ten Lesson Card (`ten_frame_tray-pocket-guide.svg`)
  - [ ] 1x CPSIA Choking Hazard Card (Ages 6+ notice for counters)
- **Pre-Sealing QA Gate:**
  - [ ] Counter cavities hold counters securely; carry shelf docks firmly into dual frames
  - [ ] Clean Manipulatives Check: Student counters verified free of technical markings
  - [ ] Underside inspection plaque verified: Mirrored `Space Mono Bold` deboss on caddy base

---

### 8. Probability Dice & Modular Spinner Pack
- **Packaging:** Profile A Mailer ($7 \times 5 \times 2\text{ in}$ Crush-Proof Mailer Box)
- **Target Weight:** ~190 g (6.7 oz) packed
- **Physical Contents:**
  - [ ] 1x Ultra-Low-Friction Centered Probability Spinner Base
  - [ ] 4x Interchangeable Sector Discs (4, 6, 8, and 12 sectors)
  - [ ] 5x Mathematical Polyhedral Dice (D4, D6, D8, D10, D12)
  - [ ] 1x 42mm Gridfinity 1x1 Storage Box with magnetic/friction lid
- **Printed Collateral & Cards:**
  - [ ] 1x Archival Reference & Schematic Card (`PROB-01`, with disc exploded diagram and Part IDs)
  - [ ] 1x Theoretical vs. Experimental Probability Pocket Guide (`dice_pack-pocket-guide.svg`)
  - [ ] 1x Safety (Dice choking hazard) Card
- **Pre-Sealing QA Gate:**
  - [ ] Spinner rotates freely for $>8$ seconds on a single flick without axial wobble
  - [ ] Underside inspection plaque verified: Mirrored `Space Mono Bold` deboss on box base

---

### 9. Unit Circle Trigonometry Volvelle
- **Packaging:** Profile A Mailer or Rigid Cardboard Flat Mailer ($7 \times 5\text{ in}$)
- **Target Weight:** ~95 g (3.4 oz) packed
- **Physical Contents:**
  - [ ] 1x Dual-Disc Rotating Volvelle (Stator + Rotor connected via flush eyelet rivet)
  - [ ] Laser-engraved / high-contrast printed degree, radian, $(\cos\theta, \sin\theta)$, and $\tan\theta$ scales
  - [ ] 1x Rigid Protective Stiffener Cardboard Backer
- **Printed Collateral & Cards:**
  - [ ] 1x Archival Reference & Schematic Card (`VOLV-01`, with angle callouts and Part IDs)
  - [ ] 1x Trig Identities & Pythagorean Unit Circle Cheatsheet
- **Pre-Sealing QA Gate:**
  - [ ] Smooth 360° disc rotation; radial viewing windows align precisely with coordinate pairs

---

### 10. 3-in-1 Reconfigurable Stand & TPU Pouch Pack
- **Packaging:** Profile A Mailer ($7 \times 5 \times 2\text{ in}$ Crush-Proof Mailer Box)
- **Target Weight:** ~160 g (5.6 oz) packed
- **Physical Contents:**
  - [ ] 4x Interlocking Puzzle Stand Pieces (`piece_c_bl`, `piece_c_br`, `piece_c_tl`, `piece_c_tr`)
  - [ ] 2x Stand Rail Connectors (`piece_stand_front`, `piece_stand_rear`)
  - [ ] 1x Reversible Shore 95A Flexible TPU Travel Sleeve (dockable in 3-ring binder)
- **Printed Collateral & Cards:**
  - [ ] 1x Dual Incline Stand Assembly Diagram ($78^\circ$ upright vs. $10^\circ$ typing wedge)
  - [ ] 1x Lifetime Guarantee Card

---

### 11. Concrete Math Challenge Deck (60 Challenge Cards)
- **Packaging:** Profile A Mailer ($7 \times 5 \times 2\text{ in}$ Crush-Proof Mailer Box)
- **Target Weight:** ~220 g (7.8 oz) packed
- **Physical Contents:**
  - [ ] 60x Heavyweight Plastic-Coated Challenge Cards ($350\,\text{gsm}$ linen finish, rounded corners)
  - [ ] 1x Rigid 2-Piece Telescoping Storage Box with thumb notches
- **Printed Collateral & Cards:**
  - [ ] 1x CCSS Mathematical Practices & Answer Key Booklet
  - [ ] 1x Classroom Replacement Guarantee Card

---

### 12. Complete 3D Print STL Bundle (Digital Download)
- **Packaging:** Automated Instant Digital Delivery (.ZIP)
- **Target Weight:** 0 g (Digital Delivery)
- **Digital Contents:**
  - [ ] Complete verified STLs for all 8 physical manipulative kits and SC-32 mechanical prototype
  - [ ] 3MF Reference Print Projects with pre-tuned slicer speeds, support-free orientations, and infills
  - [ ] 1x Comprehensive Print Orientation & Slicing PDF Field Manual

---

### 13. Replacement Parts Service Envelope (SKU: REPLACE-01)
- **Packaging:** Profile E Mailer ($6 \times 4.5\text{ in}$ Rigid Stay-Flat Cardboard Mailer Envelope)
- **Target Weight:** ~35 g (1.2 oz) packed
- **Physical Contents:**
  - [ ] 1x 3D Printed Replacement Component (verified against order personalization notes)
  - [ ] Revision tolerance check (matched to customer's stated REV code)
- **Printed Collateral & Cards:**
  - [ ] 1x Thank-You Slip: *"Thanks for keeping your StackCalc kit in action! Need more parts? stackcalc.io"*
- **Pre-Sealing QA Gate:**
  - [ ] Debossed notation is sharp and legible; perimeter chamfers are smooth

---

### 14. Math Domino Studio & 12-Frame Tray Set (SKU: DOMI-01)
- **Packaging:** Profile B Mailer ($8 \times 6 \times 3\text{ in}$ Heavyweight Mailer Box)
- **Target Weight:** ~320 g (11.3 oz) packed
- **Physical Contents:**
  - [ ] 30x Math Dominoes (28 standard double-six [0|0 through 6|6] + 2 blank wildcards [B|B]) with debossed pips and central divider
  - [ ] 1x 12-Frame Ten-Frame Math Tray (10-frame baseline + 2-frame overflow dock)
  - [ ] 1x Doubling Snap Lid with debossed reference scale and snap detents
  - [ ] 1x 42mm Gridfinity 3x1x7U Storage Box with debossed lid and inspection plaque
- **Printed Collateral & Cards:**
  - [ ] 1x Archival Reference & Schematic Card (`DOMI-01`, with exploded isometric schematic, Part IDs `DOMI-01-xxxxxxx`, 30-tile inventory, and replacement instructions)
  - [ ] 1x Math Domino Subitizing & Arithmetic Pocket Guide (`dominoes-pocket-guide.svg`)
  - [ ] 1x Safety Card (Small parts warning: Ages 6+)
- **Pre-Sealing QA Gate:**
  - [ ] Tiles slide smoothly into tray slots and stack neatly inside 3x1x7U storage box
  - [ ] Debossed pips are sharp, distinct, and clean of flash
  - [ ] Doubling lid snaps securely onto tray with audible tactile snap
  - [ ] Underside inspection plaque verified: Mirrored `Space Mono Bold` deboss on storage box base

---

## 7. Maintenance & Image Re-Generation Pipeline

If CAD models or colorway finishes change in the future, regenerate all cropped Etsy square and 4:3 assets automatically using the repository Makefile:

```bash
# Navigate to watch-calc-32 repository
cd /Users/abagher/Documents/GitHub/watch-calc-32

# Re-crop all master renders into Etsy 1:1 Square (2000x2000) and 4:3 (2000x1500)
make crop-images

# Full rebuild of OpenSCAD models, raytraced stills, and Etsy crops:
make images
```

All generated files will update synchronously in both `documentation/etsy/images/` and `stackcalc/docs/assets/renders/etsy/`.

---

## 8. Multi-Marketplace Visual Asset Strategy & Blender Physics Pipeline

StackCalc products are syndicated across Etsy, Amazon Handmade, eBay, and our direct website ([`stackcalc.io`](https://www.stackcalc.io)). Each channel requires distinct visual asset standards:

### 1. Amazon Main Image Compliance Standard (Pure White `#FFFFFF`)
- **TOS Requirement:** Amazon Seller Central and Handmade policies require MAIN listing images to feature a **100% pure white background (`RGB 255, 255, 255` / `#FFFFFF`)**. Images with off-white backgrounds, props, or text overlays are algorithmically suppressed.
- **Implementation (`setup_amazon_white_background`):**
  - World background set to `(1.0, 1.0, 1.0, 1.0)`.
  - Floor plane set as Cycles `is_shadow_catcher = True` to preserve soft, natural contact ambient occlusion shadows without dirtying the white level.
  - Product occupies 85–90% of the frame with zero graphic text overlays.

### 2. 3D-Modeled Environments (Strictly NO AI Generation)
- **Why AI Images are Rejected:** Generative AI tools (Midjourney/Flux/Photoshop) hallucinate geometry, scramble debossed mathematical notation, create impossible gear tooth profiles, and trigger deep skepticism among discerning STEM teachers and engineers.
- **The 3D PBR Environment Standard:** All contextual lifestyle scenes are rendered directly in Blender Cycles using **our authentic OpenSCAD CAD models** resting inside photorealistic 3D-modeled environments:
  - Procedural Scandinavian blonde and honey oak desk surfaces (`create_smooth_oak_desk_material`).
  - Physical drafting tools (aluminum millimeter rulers, self-healing cutting mats).
  - Subtle depth-of-field (`f/3.2` camera aperture) softly blurring classroom background elements while keeping CAD chamfers razor-sharp.

### 3. Bullet Physics Simulation Mandate (Zero Intersecting Boxes)
- **Problem:** Hardcoded static coordinates often result in loose blocks or tiles penetrating tray sidewalls or clipping through box lips.
- **Mandate:** All multi-object Blender scenes must invoke `simulate_rigid_body_settling(scene, passive_objs, active_objs)`:
  - Containers (Gridfinity boxes, calculation stages, desk surfaces) are configured as `PASSIVE` rigid bodies with `MESH` collision shapes.
  - Loose components (polynomial tiles, fraction blocks, counters, dice) are configured as `ACTIVE` rigid bodies with `CONVEX_HULL` shapes.
  - The physics engine steps 35 frames under standard gravity ($g = -9810\,\text{mm/s}^2$) with dampening until equilibrium is reached.
  - Visual transforms are permanently baked (`matrix_world.copy()`) prior to Cycles rendering, guaranteeing **physically valid, non-intersecting geometry**.

---

## 9. Real Physical Product Photography & Digital Darkroom Pipeline

While CAD raytracing and physics settling provide ideal architectural consistency, **real physical photographs of authentic 3D printed parts dramatically outperform synthetic images in conversion rate (CRO)**. Savvy Etsy shoppers, STEM teachers, and school procurement officers actively look for real physical surface textures, genuine matte PEI bed patterns, authentic layer adhesion, and debossed inspection marks.

### 9.1 The "Zero AI Hallucination" Standard
- **Strict Prohibition:** Never use text-to-image generative AI (e.g. Midjourney, Flux, Imagen) to create commercial hero shots. Generative AI hallucinates impossible geometry, distorts debossed typography, and erodes customer trust.
- **The Physical Digital Darkroom:** All commercial studio shots must be generated directly from authentic, bench-photographed hardware using computer vision and digital darkroom processing (`Tools/rendering/enhance_real_photos.py`).

### 9.2 The 5-Stage Retouching & Staging Workflow

```
┌─────────────────────────┐     1. D65 White Balance       ┌─────────────────────────┐
│ Raw Bench Photograph    │ ────────────────────────────► │ Neutral Color Temp      │
│ (Yellow Tungsten Cast)  │     (Gray-world algorithm)     │ (Maple/PEI Restored)    │
└─────────────────────────┘                                └────────────┬────────────┘
                                                                        │
                                2. CLAHE Luminance Micro-Contrast       ▼
                                ────────────────────────────────► ┌─────────────────────────┐
                                (Highlights debossed letters &    │ Matte Texture Pop       │
                                 fuzzy-skin tactile ridges)       │ (Clean Dark Charcoal)   │
                                                                  └────────────┬────────────┘
                                                                               │
                                3. GrabCut Foreground Extraction               ▼
                                ────────────────────────────────► ┌─────────────────────────┐
                                (Feathered sub-pixel alpha mask)  │ Isolated Real Box       │
                                                                  └──────┬───────────┬──────┘
                                                                         │           │
                     4A. Ground Contact Shadow Projection                │           │ 4B. Desk Staging
       ┌─────────────────────────────────────────────────────────────────┘           │
       ▼                                                                             ▼
┌─────────────────────────────────┐                       ┌─────────────────────────────────┐
│ Pure White (#FFFFFF) Studio     │                       │ Classroom Desk In-Situ          │
│ • Amazon/eBay/Etsy main shot    │                       │ • Textured wooden study desk    │
│ • Multi-stage contact AO shadow │                       │ • Soft f/2.8 background bokeh   │
│ • Razor-sharp physical print    │                       │ • Natural warm wood reflections │
└─────────────────────────────────┘                       └─────────────────────────────────┘
```

1. **D65 Daylight Normalization:** Corrects the typical indoor warm tungsten or fluorescent color cast back to neutral daylight (6500K), ensuring accurate plastic and desk color representation.
2. **Micro-Contrast & Texture Extraction:** Applies Contrast Limited Adaptive Histogram Equalization (CLAHE) on the LAB luminance channel ($L^*$) to elevate subtle debossed lettering (`TEN FRAMES`, `StackCalc`), layer lines, and fuzzy-skin matte textures without washing out contrast.
3. **Sub-Pixel Alpha Segmentation:** Uses OpenCV GrabCut with elliptical morphological closing and Gaussian edge feathering to isolate the real 3D printed box without stray halos or burrs.
4. **Physically Grounded Contact Shadows:** Eliminates "floating box" artifacts by extracting the real ground contact polygon ($[x_{min}, y_{contact}]$ to $[x_{max}, y_{contact}]$) and rendering a multi-stage ambient occlusion shadow (tight dark contact line + soft diffused floor penumbra).
5. **Multi-Marketplace Compositing:**
   - **Amazon / eBay / Etsy Main Image:** Scaled and centered with 12–15% breathing room on pure white (`#FFFFFF`).
   - **Contextual In-Situ Image:** Composited onto high-resolution 3D-modeled classroom oak desks with optical depth-of-field blur.
   - **Retouched Bench Hero:** Full-resolution original workshop photo with professional lighting, contrast curve, and lens vignette.

### 9.3 Deployed Real Photo Asset Index (SKU: BASE-10)

All assets are generated in both 1:1 Square ($1600 \times 1600\,\text{px}$) and 4:3 Horizontal ($1600 \times 1200\,\text{px}$) in both Clean and Badged editions:

| Asset Name | Format | Staging Environment | Primary Marketplace Channel |
|---|:---:|---|---|
| `ten-frames-real-front-white-square.png` | 1:1 Square | Pure White `#FFFFFF` | Amazon Main, eBay Main, Etsy Slot 1 |
| `ten-frames-real-angle-white-square.png` | 1:1 Square | Pure White `#FFFFFF` | Amazon Alternate, Etsy Slot 2 |
| `ten-frames-real-angle-white-square-badged.png` | 1:1 Square | Pure White + CMF Badge | Technical Documentation, Red Dot Portfolio |
| `ten-frames-real-front-desk-square.png` | 1:1 Square | Classroom Wooden Desk | Etsy Slot 3, Social Proof, Instagram |
| `ten-frames-real-angle-desk-square-badged.png` | 1:1 Square | Classroom Desk + CMF Badge | Web Catalog Hero, Teacher Brochure |
| `ten-frames-real-front-retouched-4x3.png` | 4:3 Wide | Color-Corrected Workbench | Documentation Banner, Blog Feature |

