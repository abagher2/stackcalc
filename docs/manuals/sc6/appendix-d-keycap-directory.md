---
title: "Appendix D: Keycap Matrix & Layout Directory | SC-6 Elementary Manual"
description: "Complete 43-key matrix directory, physical dimensions, electrical row/column pin assignments, primary legends, `f`-shifted and `g`-shifted commands, and developmental grade ribbon index for the StackCalc SC-6 Elementary RPN Calculator."
---

# Appendix D: Keycap Matrix & Layout Directory

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-6 HARDWARE // APPENDIX D: 43-KEY MATRIX &amp; DEVELOPMENTAL SHIFT DIRECTORY</span>
  <span class="te-viewport-status text-emerald-400">● 43 PHYSICAL SWITCHES &bull; 8×6 ELECTRICAL SCAN MATRIX &bull; COMPLETE SHIFT &amp; GRADE RIBBON DIRECTORY</span>
</div>

<div class="p-4 rounded-xl bg-slate-900 border border-emerald-500/30 mb-8 font-mono text-xs text-emerald-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>{{key:NUM}}</code> (Standard 4-stack XYZT decimal arithmetic; 2-digit fixed display default; visual modes toggleable via <code>{{key:▦}}</code>, <code>{{key:🕒}}</code>, and <code>{{keycap:LINE}}</code>).
</div>

---

## Keypad Physical Geometry & Tactile Matrix

The StackCalc SC-6 elementary human-machine interface is engineered specifically for young hands, high durability in classroom maker environments, and immediate tactile validation of mathematical operations.

The physical keypad comprises 43 mechanical switch positions organized into three kid-proof, ergonomic functional zones:

{{res:sc6_hero_calculator:screenshot|StackCalc SC-6 Elementary Calculator Faceplate & 43-Key Topography}}
*Figure D.1: StackCalc SC-6 Elementary RPN Calculator physical hardware faceplate render, showing the 43-key layout, double-wide {{key:ENTER}}, concrete manipulative mode keys ({{key:▦}} Ten-Frame, {{key:🕒}} Planetary Clock), and high-contrast `{{key:f}}` and `{{key:g}}` shift legends.*

<div class="admonition note">
<p class="admonition-title">StackCalc SC-6 Physical Keypad Topology</p>

#### Upper Math & Number Sense Zone (Rows 0–2, 6 Columns)
- **Pitch:** 11.50 mm horizontal pitch, 11.30 mm vertical pitch
- **Keycaps:** 10.40 mm round cylindrical concave tops with 0.40 mm dished depth

| Row | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 0** | `{{key:x²}}` | `{{key:x!}}` | `{{key:π}}` | `{{key:x³}}` | `{{key:PV}}` | `{{key:$}}` |
| **Row 1** | `{{key:FDISP}}` | `{{key:a ᵇ/c}}` | `{{key:GCF}}` | `{{key:PRIME}}` | `{{key:x⇄y}}` | `{{key:+/-}}` |
| **Row 2** | `{{key:FRQ}}` | `{{key:RNG}}` | `{{key:IQR}}` | `{{key:Σ+}}` | `{{key:N}}` | `{{key:%}}` |

#### Concrete Manipulative & Stack Transition Zone (Row 3)
- **ENTER Key:** Double-wide 21.90 mm × 10.40 mm spanning Columns 0 and 1 (primary RPN stack commit target positioned directly beneath left thumb).

| Row | Col 0 & 1 (Double-Wide) | Col 2 | Col 3 | Col 4 | Col 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 3** | `{{key:ENTER}}` | `{{key:🕒}}` | `{{key:▦}}` | `{{key:NUM}}` | `{{key:<-}}` |

#### Lower Arithmetic & Geometry Zone (Rows 4–7, 5 Columns)
- **Pitch:** Generous 13.80 mm horizontal pitch, 11.30 mm vertical pitch
- Dedicated power switch at Row 7, Col 0 serves as `{{key:C}}` and quiz launcher.

| Row | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 4** | `{{key:🎲}}` | `{{key:7}}` | `{{key:8}}` | `{{key:9}}` | `{{key:÷}}` |
| **Row 5** | `{{key:f}}` (f-Shift) | `{{key:4}}` | `{{key:5}}` | `{{key:6}}` | `{{key:×}}` |
| **Row 6** | `{{key:g}}` (g-Shift) | `{{key:1}}` | `{{key:2}}` | `{{key:3}}` | `{{key:-}}` |
| **Row 7** | `{{key:C}}` (ON) | `{{key:0}}` | `{{key:.}}` | `{{key:≠}}` | `{{key:+}}` |
</div>

### Tactile Snap-Dome Mechanics & Debouncing Algorithm
* **Actuation Force:** $400\,\text{g}$ tactile stainless steel snap domes providing an unambiguous mechanical snap threshold. This physical click reinforces the sensory loop, reassuring students that an entry has registered without double-tapping.
* **Key Travel:** $0.35\,\text{mm}$ short-stroke actuation ensuring zero lost motion.
* **Firmware Debounce Architecture:** Eager actuation on leading falling edge ($0\,\text{ms}$ latency) followed by a $20\,\text{ms}$ lockout window. This completely eliminates accidental double-strike bounce artifacts even when excited students rapidly enter numbers.

---

## Electrical Matrix & Keypad Scanning Bus

The switch matrix is wired as an $8 \times 6$ crossbar scanned by the dual-core 32-bit microcontroller:

* **Row Lines (Strobed Outputs):** GPIO pins `[6, 7, 8, 9, 10, 14, 18, 19]`. Strobed low sequentially in round-robin sequence at $1\,\text{kHz}$ scanning frequency.
* **Column Lines (Sensed Inputs):** GPIO pins `[11, 12, 13, 15, 16, 17]`. Pulled high internally by $50\,\text{k}\Omega$ resistors; active-low detection.
* **Hardware Sleep Wake Interrupt:** Row 7, Column 0 (`{{key:C}}`/ON switch) is routed to an asynchronous edge-triggered interrupt. When the calculator is in deep $11.8\,\mu\text{A}$ sleep inside a backpack or desk cubby, depressing this key immediately wakes the system clock within $5\,\text{ms}$.

---

## The Definitive 43-Key Hardware Matrix Directory & Curriculum Index

The table below catalogs every physical switch position, electrical matrix coordinate, laser-foamed keycap legend, `{{key:f}}` and `{{key:g}}` shift combinations, developmental grade ribbon, internal scancode, and direct cross-references to the textbook chapters where each operation is fully explained and practiced:

| Key # | Matrix (R, C) | Primary Legend | `{{key:f}}` Shift | `{{key:g}}` Shift | Grade Ribbon | Code | Primary & Shift Tutorial Links |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **1** | R0, C0 | `{{key:x²}}` | `{{keycap:√x}}` Root | `{{keycap:yˣ}}` Power | Gr 5–6+ | `0x00` | [Ch 6.2 Square Area](06-geometry-surface-area.md) &bull; [Ch 6.3 Geometric Roots](06-geometry-surface-area.md) &bull; [Ch 4.4 Powers](04-operations-skip-counting.md) |
| **2** | R0, C1 | `{{key:x!}}` | `{{keycap:nCr}}` Comb | `{{keycap:nPr}}` Perm | Gr 6+ | `0x01` | [Ch 7.4 Polyhedral Combinatorics](07-data-probability-primes.md) |
| **3** | R0, C2 | `{{key:π}}` | `{{keycap:e}}` Euler | `{{keycap:ˣ√y}}` Radic | Gr 5–6+ | `0x02` | [Ch 6.4 Circle Geometry](06-geometry-surface-area.md) &bull; [Ch 6.5 Constant E](06-geometry-surface-area.md) |
| **4** | R0, C3 | `{{key:x³}}` | `{{keycap:10ˣ}}` Exp | `{{keycap:LOG}}` Base-10 | Gr 5–6+ | `0x03` | [Ch 6.6 3D Volumes](06-geometry-surface-area.md) &bull; [Ch 3.2 Place Value Powers](03-counting-place-value.md) |
| **5** | R0, C4 | `{{key:PV}}` | `{{keycap:IP}}` Int Part | `{{keycap:FP}}` Frac Part | Gr 2–4 | `0x04` | [Ch 3.1 Place Value Decomposition](03-counting-place-value.md) &bull; [Ch 5.3 Integer & Frac Parts](05-fractions-decimals-ratios.md) |
| **6** | R0, C5 | `{{key:$}}` | `{{keycap:ALL}}` Full | `{{keycap:RND}}` Round | Gr 2–5 | `0x05` | [Ch 3.4 Currency Arithmetic](03-counting-place-value.md) &bull; [Ch 4.3 Rounding](04-operations-skip-counting.md) |
| **7** | R1, C0 | `{{key:FDISP}}` | `{{keycap:1/x}}` Recip | `{{keycap:/c}}` Denom | Gr 3–5 | `0x10` | [Ch 5.1 Fraction Entry & Toggle](05-fractions-decimals-ratios.md) &bull; [Ch 5.2 Reciprocals](05-fractions-decimals-ratios.md) &bull; [Ch 5.3 Fixed Denominator](05-fractions-decimals-ratios.md) |
| **8** | R1, C1 | `{{key:a ᵇ/c}}` | `{{keycap:d/c}}` Improper | `{{keycap:SIMP}}` Step | Gr 3–5 | `0x11` | [Ch 5.1 Mixed Numbers](05-fractions-decimals-ratios.md) &bull; [Ch 5.1 Improper Fractions](05-fractions-decimals-ratios.md) &bull; [Ch 5.2 Superpower 3: SIMP Reduction](05-fractions-decimals-ratios.md) |
| **9** | R1, C2 | `{{key:GCF}}` | `{{keycap:LCM}}` Multiple | `{{keycap:a:b}}` Ratio | Gr 5–6 | `0x12` | [Ch 7.3 Number Theory GCF/LCM](07-data-probability-primes.md) &bull; [Ch 5.4 Ratios & Rates](05-fractions-decimals-ratios.md) |
| **10**| R1, C3 | `{{key:PRIME}}` | `{{keycap:C.FAC}}` ComFac | `{{keycap:FACT}}` Tree | Gr 5–6 | `0x13` | [Ch 7.3 Prime Studio & Factorization](07-data-probability-primes.md) |
| **11**| R1, C4 | `{{key:x⇄y}}` | `{{keycap:R↓}}` Roll Down | `{{keycap:REP}}` Ladder | Gr 2–4 | `0x14` | [Ch 2.3 Stack Swapping](02-rpn-for-young-learners.md) &bull; [Ch 4.1 Superpower 1: REP Skip-Counting](04-operations-skip-counting.md) |
| **12**| R1, C5 | `{{key:+/-}}` | `{{keycap:E}}` Exponent | `[\|x\|]` Abs | Gr 5–6 | `0x15` | [Ch 2.4 Negative Numbers](02-rpn-for-young-learners.md) &bull; [Ch 3.3 Scientific Exponents](03-counting-place-value.md) &bull; [Ch 2.4 Absolute Value](02-rpn-for-young-learners.md) |
| **13**| R2, C0 | `{{key:FRQ}}` | `{{keycap:MED}}` Median | `{{keycap:MODE}}` Mode | Gr 5–6 | `0x20` | [Ch 7.1 Frequency Tables & Dot Plots](07-data-probability-primes.md) &bull; [Ch 7.2 Median & Mode](07-data-probability-primes.md) |
| **14**| R2, C1 | `{{key:RNG}}` | `{{keycap:MIN}}` Minimum | `{{keycap:MAX}}` Maximum | Gr 5–6 | `0x21` | [Ch 7.2 Data Spread & Extremes](07-data-probability-primes.md) |
| **15**| R2, C2 | `{{key:IQR}}` | `{{keycap:1Q}}` Quartile 1| `{{keycap:3Q}}` Quartile 3| Gr 6+ | `0x22` | [Ch 7.2 Quartiles & Box Plots](07-data-probability-primes.md) |
| **16**| R2, C3 | `{{key:Σ+}}` | `{{keycap:Σ-}}` Remove | `{{keycap:MAD}}` MeanDev | Gr 4–6 | `0x23` | [Ch 6.2 Master Surface Area via Stats](06-geometry-surface-area.md) &bull; [Ch 7.2 Mean Absolute Deviation](07-data-probability-primes.md) |
| **17**| R2, C4 | `{{key:N}}` | `{{keycap:Σx}}` Total Sum | `{{keycap:x̄}}` Mean Avg | Gr 5–6 | `0x24` | [Ch 7.1 Sample Count & Arithmetic Mean](07-data-probability-primes.md) |
| **18**| R2, C5 | `{{key:%}}` | `{{keycap:▸%}}` Dec to Pct | `{{keycap:%CHG}}` Change | Gr 5–6 | `0x25` | [Ch 5.5 Percentages & Discounts](05-fractions-decimals-ratios.md) |
| **19**| R3, C0-1| `{{key:ENTER}}` | `{{key:LASTX}}` Check | `{{keycap:SHOW}}` 15-Dig | Gr K–6 | `0x30` | [Ch 2.1 The Elevator Push](02-rpn-for-young-learners.md) &bull; [Ch 4.2 Superpower 4: LASTX Error Check](04-operations-skip-counting.md) &bull; [Ch 3.3 Full Precision](03-counting-place-value.md) |
| **20**| R3, C2 | `{{key:🕒}}` | `{{keycap:▸HR}}` Decimal | `{{keycap:▸HMS}}` Clock | Gr 3–5 | `0x32` | [Ch 6.7 Planetary Geared Clock Modulo-60](06-geometry-surface-area.md) |
| **21**| R3, C3 | `{{key:▦}}` | `{{keycap:LINE}}` Line | `{{keycap:COUNT}}` Step | Gr K–2 | `0x33` | [Ch 3.1 Ten-Frame Mode](03-counting-place-value.md) &bull; [Ch 3.2 Number Line](03-counting-place-value.md) &bull; [Ch 3.1 Step Counter](03-counting-place-value.md) |
| **22**| R3, C4 | `{{key:NUM}}` | `{{keycap:SCI}}` Sci Not | `{{keycap:FIX}}` Dec Dec | Gr K–6 | `0x34` | [Ch 2.2 Numerical 4-Stack Mode](02-rpn-for-young-learners.md) &bull; [Ch 3.3 Scientific Display](03-counting-place-value.md) |
| **23**| R3, C5 | `{{key:<-}}` | `{{keycap:CSTK}}` Clr Stk | `{{keycap:CLΣ}}` Clr Stat| Gr K–6 | `0x35` | [Ch 2.1 Backspace Digit](02-rpn-for-young-learners.md) &bull; [Ch 2.2 Clear Stack](02-rpn-for-young-learners.md) &bull; [Ch 6.2 Clear Stats](06-geometry-surface-area.md) |
| **24**| R4, C0 | `{{key:🎲}}` | `{{keycap:1…x}}` PRNG | `{{keycap:t…x}}` Range | Gr 3–6 | `0x40` | [Ch 7.4 Dice & Probability Trials](07-data-probability-primes.md) |
| **25**| R4, C1 | `{{key:7}}` | `{{keycap:RECT}}` Area | `{{keycap:TRI}}` Area | Gr K–4 | `0x41` | [Ch 3.1 Digit Entry](03-counting-place-value.md) &bull; [Ch 6.1 Rectangle & Triangle Area](06-geometry-surface-area.md) |
| **26**| R4, C2 | `{{key:8}}` | `{{keycap:CIRC}}` Area | `{{keycap:HYP}}` Hypoten | Gr K–5 | `0x42` | [Ch 3.1 Digit Entry](03-counting-place-value.md) &bull; [Ch 6.1 Circle Area & Hypotenuse](06-geometry-surface-area.md) |
| **27**| R4, C3 | `{{key:9}}` | `{{keycap:PRISM}}` Volume | `{{keycap:CONE}}` Volume | Gr K–5 | `0x43` | [Ch 3.1 Digit Entry](03-counting-place-value.md) &bull; [Ch 6.6 Prism & Cone Volume](06-geometry-surface-area.md) |
| **28**| R4, C4 | `{{key:÷}}` | `{{keycap:MOD}}` Rem | `{{keycap:÷R}}` Quotient | Gr 3–5 | `0x44` | [Ch 4.1 Division](04-operations-skip-counting.md) &bull; [Ch 4.2 Superpower 2: Simultaneous Quotient & Remainder](04-operations-skip-counting.md) |
| **29**| R5, C0 | `{{key:f}}` (f-Shift)| *(f-Shift Latch)* | *(f-Shift Latch)* | Gr K–6 | `0x50` | [Sec D.1 Latch Hardware](#d1-keypad-physical-geometry-tactile-matrix) &bull; Primary `{{key:f}}` Shift prefix |
| **30**| R5, C1 | `{{key:4}}` | `{{keycap:▸g}}` Grams | `{{keycap:▸oz}}` Ounces | Gr K–4 | `0x51` | [Ch 3.1 Digit Entry](03-counting-place-value.md) &bull; [Ch 9.1 Filament Mass](09-applied-stem-labs.md) |
| **31**| R5, C2 | `{{key:5}}` | `{{keycap:▸ft}}` Feet | `{{keycap:▸mi}}` Miles | Gr K–4 | `0x52` | [Ch 3.1 Digit Entry](03-counting-place-value.md) &bull; [Ch 9.2 Distance Scaling](09-applied-stem-labs.md) |
| **32**| R5, C3 | `{{key:6}}` | `{{keycap:▸mL}}` Millilit | `{{keycap:▸fl}}` Fluid Oz| Gr K–4 | `0x53` | [Ch 3.1 Digit Entry](03-counting-place-value.md) &bull; [Ch 9.3 Liquid Volumes](09-applied-stem-labs.md) |
| **33**| R5, C4 | `{{key:×}}` | *(Unassigned)* | `{{keycap:FLAGS}}` Stack | Gr 3–5 | `0x54` | [Ch 4.1 Array Multiplication](04-operations-skip-counting.md) &bull; [Ch 2.2 Configurable Stack Depths](02-rpn-for-young-learners.md) |
| **34**| R6, C0 | `{{key:g}}` (g-Shift)| *(g-Shift Latch)* | *(g-Shift Latch)* | Gr K–6 | `0x60` | [Sec D.1 Latch Hardware](#d1-keypad-physical-geometry-tactile-matrix) &bull; Secondary `{{key:g}}` Shift prefix |
| **35**| R6, C1 | `{{key:1}}` | `{{keycap:▸kg}}` Kilograms| `{{keycap:▸lb}}` Pounds | Gr K–4 | `0x61` | [Ch 3.1 Digit Entry](03-counting-place-value.md) &bull; [Ch 9.1 Mass Conversions](09-applied-stem-labs.md) |
| **36**| R6, C2 | `{{key:2}}` | `{{keycap:▸°C}}` Celsius | `{{keycap:▸°F}}` Fahren | Gr K–4 | `0x62` | [Ch 3.1 Digit Entry](03-counting-place-value.md) &bull; [Ch 9.5 Thermal Tracking](09-applied-stem-labs.md) |
| **37**| R6, C3 | `{{key:3}}` | `{{keycap:▸cm}}` Centimet | `{{keycap:▸in}}` Inches | Gr K–4 | `0x63` | [Ch 3.1 Digit Entry](03-counting-place-value.md) &bull; [Ch 9.1 Blueprint Sizing](09-applied-stem-labs.md) |
| **38**| R6, C4 | `{{key:-}}` | `{{keycap:▸L}}` Liters | `{{keycap:▸gal}}` Gallons | Gr K–4 | `0x64` | [Ch 2.1 Subtraction](02-rpn-for-young-learners.md) &bull; [Ch 9.3 Tank Capacity](09-applied-stem-labs.md) |
| **39**| R7, C0 | `{{key:C}}` (ON) | `{{keycap:?}}` Quiz Sprint| `{{keycap:OFF}}` Sleep | Gr K–6 | `0x70` | [Ch 1.1 Cold Boot & Sleep](01-hardware-architecture.md) &bull; [Ch 8.1 Math Quiz Engine](08-math-quiz-engine.md) |
| **40**| R7, C1 | `{{key:0}}` | `{{keycap:REGS}}` Viewer | *(Unassigned)* | Gr K–6 | `0x71` | [Ch 3.1 Digit Entry](03-counting-place-value.md) &bull; [Ch 2.2 Memory Registers](02-rpn-for-young-learners.md) |
| **41**| R7, C2 | `{{key:.}}` | `{{keycap:0.3̄}}` Repeat | *(Unassigned)* | Gr 3–5 | `0x72` | [Ch 5.1 Decimal & Repeating Notation](05-fractions-decimals-ratios.md) |
| **42**| R7, C3 | `{{key:≠}}` | `{{keycap:>}}` Greater | `{{keycap:<}}` Less | Gr 1–4 | `0x73` | [Ch 8.2 Quiz Answer Submit](08-math-quiz-engine.md) &bull; [Ch 4.3 Inequality Comparisons](04-operations-skip-counting.md) |
| **43**| R7, C4 | `{{key:+}}` | `{{keycap:≥}}` Greater/Eq | `{{keycap:≤}}` Less/Eq | Gr K–4 | `0x74` | [Ch 2.1 Addition](02-rpn-for-young-learners.md) &bull; [Ch 4.3 Inequality Comparisons](04-operations-skip-counting.md) |

---

## Developmental Keycap Ribbon Architecture

The SC-6 physical keyboard supports the full elementary-to-middle school progression through progressive pedagogical gating:

| Grade Level | Pedagogical Focus | Unlocked Keycaps Suite |
| :--- | :--- | :--- |
| **Grade K–1: Sensory Foundations** | Concrete counting, make-ten pairing, and tactile arithmetic | `{{key:▦}}` Ten-Frame, `{{keycap:COUNT}}`, `{{keycap:LINE}}`, `{{key:+}}`, `{{key:-}}`, `{{key:ENTER}}`, `{{key:C}}`, `{{key:<-}}` |
| **Grade 2: Place Value & Skip-Counting** | Multi-digit decomposition, doubles, and rhythmic counting | `{{key:PV}}` Place Value, `{{keycap:REP}}` Skip-Counting, `{{key:$}}` Currency, `{{key:x⇄y}}` |
| **Grade 3: Arrays, Area & Fractions** | Grid arrays, time arithmetic, and unit fraction exploration | `{{key:×}}`, `{{key:÷}}`, `{{keycap:RECT}}`, `{{key:🕒}}` Planetary Clock, `{{key:FDISP}}`, `[. n . d]` |
| **Grade 4: Division & Fraction Mastery** | Division with remainders and step-by-step fraction reduction | `{{keycap:÷R}}` Quotient & Remainder, `{{key:a ᵇ/c}}`, `{{keycap:d/c}}`, `{{keycap:SIMP}}`, `{{key:LASTX}}` |
| **Grade 5: Unlike Fractions & Surface Area** | Common denominators, 3D volume, and ledger accumulation | `{{key:GCF}}`, `{{keycap:LCM}}`, `{{keycap:PRISM}}`, `{{key:Σ+}}` Surface Area Ledger, `{{key:FRQ}}` Tables |
| **Grade 6+: Number Theory & Sprint** | Negatives, primes, descriptive statistics, and rapid mental math sprints | `{{key:+/-}}`, `[\|x\|]`, `{{key:PRIME}}`, `{{keycap:FACT}}`, `{{keycap:a:b}}`, `{{key:x²}}`, `{{keycap:√x}}`, `{{key:IQR}}`, `{{keycap:MAD}}` |

---

## Verification & Firmware Implementation Reference

The 43-key matrix pinouts, electrical scanning bus, and shift mappings are verified in:
* The SC-6 Core Keymap Specification (`StackCalc6KeyMap`)
* The SC-6 Laser Topography Generator (`generate_laser_svg.py --sc6`)
* The SC-6 Decal Topography Matrix (`layout_data_sc6.json`)
