---
title: "Appendix D: Keycap Matrix & Layout Directory"
description: "Complete 43-key keypad directory, ergonomic zone layout, primary legends, f-shifted and g-shifted commands, and developmental grade ribbon index for the StackCalc SC-6 Elementary RPN Calculator."
---

# Appendix D: Keycap Matrix & Layout Directory

## Keypad Physical Geometry & Tactile Matrix

The StackCalc SC-6 elementary keypad is designed specifically for young hands, everyday classroom durability, and clear physical feedback on every math operation.

The physical keypad comprises 43 mechanical switch positions organized into three kid-proof, ergonomic functional zones:

{{res:sc6_hero_calculator:screenshot|StackCalc SC-6 Elementary Calculator Faceplate & 43-Key Topography}}
*Figure D.1: StackCalc SC-6 Elementary RPN Calculator physical hardware faceplate render, showing the 43-key layout, double-wide `{{key:ENTER}}`, concrete manipulative mode keys (`{{key:▦}}` Ten-Frame, `{{key:🕒}}` Planetary Clock), and high-contrast `{{key:f}}` and `{{key:g}}` shift legends.*

### Upper Math & Number Sense Zone (Rows 0–2, 6 Columns)
- **Purpose:** Powers, place value (`{{key:PV}}`), fractions (`{{key:a ᵇ/c}}`, `{{key:SIMP}}`), number theory (`{{key:GCF}}`, `{{key:PRIME}}`), and classroom data tools (`{{key:Σ+}}`, `{{key:IQR}}`).

| Row | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 0** | `{{key:x²}}` | `{{key:x!}}` | `{{key:π}}` | `{{key:x³}}` | `{{key:PV}}` | `{{key:$}}` |
| **Row 1** | `{{key:FDISP}}` | `{{key:a ᵇ/c}}` | `{{key:GCF}}` | `{{key:PRIME}}` | `{{key:x⇄y}}` | `{{key:+/-}}` |
| **Row 2** | `{{key:FRQ}}` | `{{key:RNG}}` | `{{key:IQR}}` | `{{key:Σ+}}` | `{{key:N}}` | `{{key:%}}` |

### Concrete Manipulative & Stack Transition Zone (Row 3)
- **ENTER Key:** Double-wide key spanning Columns 0 and 1 (primary RPN stack elevator button positioned right beneath your left thumb), alongside visual mode buttons (`{{key:🕒}}`, `{{key:▦}}`, `{{key:NUM}}`).

| Row | Col 0 & 1 (Double-Wide) | Col 2 | Col 3 | Col 4 | Col 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 3** | `{{key:ENTER}}` | `{{key:🕒}}` | `{{key:▦}}` | `{{key:NUM}}` | `{{key:<-}}` |

### Lower Arithmetic & Geometry Zone (Rows 4–7, 5 Columns)
- **Purpose:** High-visibility digit entry (`0`–`9`), core arithmetic (`÷, ×, -, +`), polyhedral dice (`{{key:🎲}}`), color-coded shift keys (`{{key:f}}`, `{{key:g}}`), and `{{key:C}}` (Clear / Wake / `{{key:?}}` Quiz).

| Row | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 4** | `{{key:🎲}}` | `{{key:7}}` | `{{key:8}}` | `{{key:9}}` | `{{key:÷}}` |
| **Row 5** | `{{key:f}}` (f-Shift) | `{{key:4}}` | `{{key:5}}` | `{{key:6}}` | `{{key:×}}` |
| **Row 6** | `{{key:g}}` (g-Shift) | `{{key:1}}` | `{{key:2}}` | `{{key:3}}` | `{{key:-}}` |
| **Row 7** | `{{key:C}}` (ON) | `{{key:0}}` | `{{key:.}}` | `{{key:≠}}` | `{{key:+}}` |

### Tactile Keys, No-Bounce Typing & Classroom Battery Life
* **Crisp Tactile Click:** Each key uses a responsive tactile switch under a sculpted Shore 90A TPU keycap that gives a clear physical click. Students know right away that a number or operation has been entered without having to guess or press a key twice. (Full mechanical CAD drawings and enclosure files are available at **[stackcalc.io/hardware](https://stackcalc.io/hardware)**.)
* **No-Bounce Typing Protection:** Built-in key filtering registers each press cleanly and blocks accidental double-taps, even when excited students type rapidly during timed math sprints.
* **Instant Wake & Multi-Year Battery Life:** When stored in a backpack or classroom bin, the SC-6 automatically enters a deep power-saving sleep mode after 3 minutes of inactivity while keeping all four stack shelves ($X, Y, Z, T$), memory registers, statistics, and quiz levels safely saved. Tapping `{{key:C}}` (Row 7, Col 0) wakes the calculator instantaneously for months and years of classroom use on a single coin-cell battery.

---

## The Definitive 43-Key Hardware Matrix Directory & Curriculum Index

The table below catalogs every physical switch position, row and column coordinate, keycap legend, `{{key:f}}` and `{{key:g}}` shift combinations, developmental grade ribbon, key code, and direct cross-references to the textbook chapters where each operation is fully explained and practiced:

| Key # | Matrix (R, C) | Primary Legend | `{{key:f}}` Shift | `{{key:g}}` Shift | Grade Ribbon | Code | Primary & Shift Tutorial Links |
| :---: | :---: | :---: | :--- | :--- | :---: | :---: | :--- |
| **1** | R0, C0 | `{{key:x²}}` | `{{key:√x}}` Root | `{{key:yˣ}}` Power | Gr 5–6+ | `0x00` | [Ch 6.3 Square Area](06-geometry-surface-area.md) • [Ch 6.3 Geometric Roots](06-geometry-surface-area.md) • [Ch 4.7 Powers](04-operations-skip-counting.md) |
| **2** | R0, C1 | `{{key:x!}}` | `{{key:nCr}}` Comb | `{{key:nPr}}` Perm | Gr 6+ | `0x01` | [Ch 7.3 Counting Choices & Arrangements](07-data-probability-primes.md) |
| **3** | R0, C2 | `{{key:π}}` | `{{key:e}}` Euler | `{{key:ˣ√y}}` Radic | Gr 5–6+ | `0x02` | [Ch 6.3 Circle Geometry](06-geometry-surface-area.md) • [Ch 6.5 3D Volumes](06-geometry-surface-area.md) |
| **4** | R0, C3 | `{{key:x³}}` | `{{key:10ˣ}}` Exp | `{{key:LOG}}` Base-10 | Gr 5–6+ | `0x03` | [Ch 6.5 3D Volumes](06-geometry-surface-area.md) • [Ch 3.8 Place Value Powers](03-counting-place-value.md) |
| **5** | R0, C4 | `{{key:PV}}` | `{{key:IP}}` Int Part | `{{key:FP}}` Frac Part | Gr 2–4 | `0x04` | [Ch 3.8 Place Value Decomposition](03-counting-place-value.md) • [Ch 5.3 Integer & Frac Parts](05-fractions-decimals-ratios.md) |
| **6** | R0, C5 | `{{key:$}}` | `{{key:ALL}}` Full | `{{key:RND}}` Round | Gr 2–5 | `0x05` | [Ch 3.8 Currency & Place Value](03-counting-place-value.md) • [Ch 4.3 Rounding](04-operations-skip-counting.md) |
| **7** | R1, C0 | `{{key:FDISP}}` | `{{key:1/x}}` Recip | `{{key:/c}}` Denom | Gr 3–5 | `0x10` | [Ch 5.3 Fraction Entry & Toggle](05-fractions-decimals-ratios.md) • [Ch 5.7 Reciprocals & Decimals](05-fractions-decimals-ratios.md) • [Ch 5.6 Fixed Denominator](05-fractions-decimals-ratios.md) |
| **8** | R1, C1 | `{{key:a ᵇ/c}}` | `{{key:d/c}}` Improper | `{{key:SIMP}}` Step | Gr 3–5 | `0x11` | [Ch 5.3 Mixed Numbers](05-fractions-decimals-ratios.md) • [Ch 5.4 Improper Fractions](05-fractions-decimals-ratios.md) • [Ch 5.5 Step-by-Step Simplify: SIMP Reduction](05-fractions-decimals-ratios.md) |
| **9** | R1, C2 | `{{key:GCF}}` | `{{key:LCM}}` Multiple | `{{key:a:b}}` Ratio | Gr 5–6 | `0x12` | [Ch 7.4 Number Theory GCF/LCM](07-data-probability-primes.md) • [Ch 5.8 Ratios & Rates](05-fractions-decimals-ratios.md) |
| **10**| R1, C3 | `{{key:PRIME}}` | `{{key:C.FAC}}` ComFac | `{{key:FACT}}` Tree | Gr 5–6 | `0x13` | [Ch 7.4 Prime Studio & Factorization](07-data-probability-primes.md) |
| **11**| R1, C4 | `{{key:x⇄y}}` | `{{key:R↓}}` Roll Down | `{{key:REP}}` Replicate | Gr 2–4 | `0x14` | [Ch 2.7 Stack Swapping](02-rpn-for-young-learners.md) • [Ch 4.4 Stack Replicator: REP Skip-Counting](04-operations-skip-counting.md) |
| **12**| R1, C5 | `{{key:+/-}}` | `{{key:E}}` Exponent | `{{key:ABS}}` Abs | Gr 5–6 | `0x15` | [Ch 7.6 Signed Numbers](07-data-probability-primes.md) • [Ch 3.9 Scientific Exponents](03-counting-place-value.md) • [Ch 7.6 Absolute Value](07-data-probability-primes.md) |
| **13**| R2, C0 | `{{key:FRQ}}` | `{{key:MED}}` Median | `{{key:MODE}}` Mode | Gr 5–6 | `0x20` | [Ch 7.5 Frequency Tables & Dot Plots](07-data-probability-primes.md) • [Ch 7.5 Median & Mode](07-data-probability-primes.md) |
| **14**| R2, C1 | `{{key:RNG}}` | `{{key:MIN}}` Minimum | `{{key:MAX}}` Maximum | Gr 5–6 | `0x21` | [Ch 7.5 Data Spread & Extremes](07-data-probability-primes.md) |
| **15**| R2, C2 | `{{key:IQR}}` | `{{key:1Q}}` Quartile 1| `{{key:3Q}}` Quartile 3| Gr 6+ | `0x22` | [Ch 7.5 Quartiles & Box Plots](07-data-probability-primes.md) |
| **16**| R2, C3 | `{{key:Σ+}}` | `{{key:Σ-}}` Remove | `{{key:MAD}}` MeanDev | Gr 4–6 | `0x23` | [Ch 6.4 Master Surface Area via Stats](06-geometry-surface-area.md) • [Ch 7.5 Mean Absolute Deviation](07-data-probability-primes.md) |
| **17**| R2, C4 | `{{key:N}}` | `{{key:Σx}}` Total Sum | `{{key:x̄}}` Mean Avg | Gr 5–6 | `0x24` | [Ch 7.5 Sample Count & Arithmetic Mean](07-data-probability-primes.md) |
| **18**| R2, C5 | `{{key:%}}` | `{{key:▸%}}` Dec to Pct | `{{key:%CHG}}` Change | Gr 5–6 | `0x25` | [Ch 5.7 Percentages & Discounts](05-fractions-decimals-ratios.md) |
| **19**| R3, C0-1| `{{key:ENTER}}` | `{{key:LASTX}}` Check | `{{key:SHOW}}` 15-Dig | Gr 3–7 | `0x30` | [Ch 2.2 The Elevator Push](02-rpn-for-young-learners.md) • [Ch 8.2 Quiz Answer Submit](08-math-quiz-engine.md) • [Ch 4.6 Last Number Recall: LASTX Error Check](04-operations-skip-counting.md) • [Ch 3.9 Full Precision](03-counting-place-value.md) |
| **20**| R3, C2 | `{{key:🕒}}` | `{{key:▸HR}}` Decimal | `{{key:▸HMS}}` Clock | Gr 3–5 | `0x32` | [Ch 6.6 Planetary Geared Clock & Time](06-geometry-surface-area.md) |
| **21**| R3, C3 | `{{key:▦}}` | `{{key:LINE}}` Line | `{{key:COUNT}}` Step | Gr 3–5 | `0x33` | [Ch 3.3 Ten-Frame Mode](03-counting-place-value.md) • [Ch 3.6 Number Line](03-counting-place-value.md) • [Ch 3.7 Number Rack](03-counting-place-value.md) |
| **22**| R3, C4 | `{{key:NUM}}` | `{{key:SCI}}` Sci Not | `{{key:FIX}}` Fixed Dec | Gr 3–7 | `0x34` | [Ch 2.2 Numerical 4-Stack Mode](02-rpn-for-young-learners.md) • [Ch 3.9 Scientific Display](03-counting-place-value.md) |
| **23**| R3, C5 | `{{key:<-}}` | `{{key:CSTK}}` Clr Stk | `{{key:CLΣ}}` Clr Stat| Gr 3–7 | `0x35` | [Ch 2.2 Backspace Digit](02-rpn-for-young-learners.md) • [Ch 2.7 Clear Stack](02-rpn-for-young-learners.md) • [Ch 6.4 Clear Stats](06-geometry-surface-area.md) |
| **24**| R4, C0 | `{{key:🎲}}` | `{{key:1…x}}` Random | `{{key:t…x}}` Range | Gr 3–6 | `0x40` | [Ch 7.3 Dice & Probability Trials](07-data-probability-primes.md) |
| **25**| R4, C1 | `{{key:7}}` | `{{key:RECT}}` Area | `{{key:TRI}}` Area | Gr 3–6 | `0x41` | [Ch 3.2 Digit Entry](03-counting-place-value.md) • [Ch 6.3 Rectangle & Triangle Area](06-geometry-surface-area.md) |
| **26**| R4, C2 | `{{key:8}}` | `{{key:CIRC}}` Area | `{{key:HYP}}` Hypoten | Gr 3–6 | `0x42` | [Ch 3.2 Digit Entry](03-counting-place-value.md) • [Ch 6.3 Circle Area & Hypotenuse](06-geometry-surface-area.md) |
| **27**| R4, C3 | `{{key:9}}` | `{{key:PRISM}}` Volume | `{{key:CONE}}` Volume | Gr 3–6 | `0x43` | [Ch 3.2 Digit Entry](03-counting-place-value.md) • [Ch 6.5 Prism & Cone Volume](06-geometry-surface-area.md) |
| **28**| R4, C4 | `{{key:÷}}` | `{{key:MOD}}` Rem | `{{key:÷R}}` Quotient | Gr 3–5 | `0x44` | [Ch 4.5 Division](04-operations-skip-counting.md) • [Ch 4.5 Quotient & Remainder: Simultaneous Quotient & Remainder](04-operations-skip-counting.md) |
| **29**| R5, C0 | `{{key:f}}` (f-Shift)| *(f-Shift Latch)* | *(f-Shift Latch)* | Gr 3–7 | `0x50` | [Keypad Physical Geometry](#keypad-physical-geometry-tactile-matrix) • Primary `{{key:f}}` Shift prefix |
| **30**| R5, C1 | `{{key:4}}` | `{{key:▸g}}` Grams | `{{key:▸oz}}` Ounces | Gr 3–6 | `0x51` | [Ch 3.2 Digit Entry](03-counting-place-value.md) • [Ch 9.3 Filament Mass](09-applied-stem-labs.md) |
| **31**| R5, C2 | `{{key:5}}` | `{{key:▸ft}}` Feet | `{{key:▸mi}}` Miles | Gr 3–6 | `0x52` | [Ch 3.2 Digit Entry](03-counting-place-value.md) • [Ch 9.8 Distance Scaling](09-applied-stem-labs.md) |
| **32**| R5, C3 | `{{key:6}}` | `{{key:▸mL}}` Millilit | `{{key:▸fl}}` Fluid Oz| Gr 3–6 | `0x53` | [Ch 3.2 Digit Entry](03-counting-place-value.md) • [Ch 9.10 Liquid Volumes](09-applied-stem-labs.md) |
| **33**| R5, C4 | `{{key:×}}` | *(Unassigned)* | `{{key:FLAGS}}` Stack | Gr 3–5 | `0x54` | [Ch 4.2 Array Multiplication](04-operations-skip-counting.md) • [Ch 2.6 Configurable Stack Depths](02-rpn-for-young-learners.md) |
| **34**| R6, C0 | `{{key:g}}` (g-Shift)| *(g-Shift Latch)* | *(g-Shift Latch)* | Gr 3–7 | `0x60` | [Keypad Physical Geometry](#keypad-physical-geometry-tactile-matrix) • Secondary `{{key:g}}` Shift prefix |
| **35**| R6, C1 | `{{key:1}}` | `{{key:▸kg}}` Kilograms| `{{key:▸lb}}` Pounds | Gr 3–6 | `0x61` | [Ch 3.2 Digit Entry](03-counting-place-value.md) • [Ch 9.3 Mass Conversions](09-applied-stem-labs.md) |
| **36**| R6, C2 | `{{key:2}}` | `{{key:▸°C}}` Celsius | `{{key:▸°F}}` Fahren | Gr 3–6 | `0x62` | [Ch 3.2 Digit Entry](03-counting-place-value.md) • [Ch 9.7 Thermal Tracking](09-applied-stem-labs.md) |
| **37**| R6, C3 | `{{key:3}}` | `{{key:▸cm}}` Centimet | `{{key:▸in}}` Inches | Gr 3–6 | `0x63` | [Ch 3.2 Digit Entry](03-counting-place-value.md) • [Ch 9.3 Blueprint Sizing](09-applied-stem-labs.md) |
| **38**| R6, C4 | `{{key:-}}` | `{{key:▸L}}` Liters | `{{key:▸gal}}` Gallons | Gr 3–6 | `0x64` | [Ch 4.3 Subtraction](04-operations-skip-counting.md) • [Ch 9.12 Tank Capacity](09-applied-stem-labs.md) |
| **39**| R7, C0 | `{{key:C}}` (ON) | `{{key:?}}` Quiz Sprint| `{{key:OFF}}` Sleep | Gr 3–7 | `0x70` | [Ch 1.4 Cold Boot & Sleep](01-hardware-architecture.md) • [Ch 8.2 Math Quiz Engine](08-math-quiz-engine.md) |
| **40**| R7, C1 | `{{key:0}}` | `{{key:REGS}}` Viewer | *(Unassigned)* | Gr 3–7 | `0x71` | [Ch 3.2 Digit Entry](03-counting-place-value.md) • [Ch 2.6 Stack Viewer](02-rpn-for-young-learners.md) |
| **41**| R7, C2 | `{{key:.}}` | `{{key:0.3̄}}` Repeat | *(Unassigned)* | Gr 3–5 | `0x72` | [Ch 5.3 Decimal & Repeating Notation](05-fractions-decimals-ratios.md) |
| **42**| R7, C3 | `{{key:≠}}` | `{{key:>}}` Greater | `{{key:<}}` Less | Gr 3–5 | `0x73` | [Ch 4.3 Inequality Comparisons](04-operations-skip-counting.md) |
| **43**| R7, C4 | `{{key:+}}` | `{{key:≥}}` Greater/Eq | `{{key:≤}}` Less/Eq | Gr 3–5 | `0x74` | [Ch 4.3 Addition & Inequality Comparisons](04-operations-skip-counting.md) |

---

## Developmental Keycap Ribbon Architecture

The SC-6 physical keyboard supports the full elementary-to-middle school progression through progressive grade-band introduction:

| Curriculum Stage | Core Mathematical Focus | Keycaps Introduced |
| :--- | :--- | :--- |
| **Foundational Fluency** | Concrete counting, make-ten pairing, and tactile arithmetic | `{{key:▦}}` Ten-Frame, `{{key:COUNT}}`, `{{key:LINE}}`, `{{key:+}}`, `{{key:-}}`, `{{key:ENTER}}`, `{{key:C}}`, `{{key:<-}}` |
| **Place Value & Skip-Counting** | Multi-digit decomposition, doubles, and rhythmic counting | `{{key:PV}}` Place Value, `{{key:REP}}` Stack Replicator, `{{key:$}}` Currency, `{{key:x⇄y}}` |
| **Arrays, Area & Fractions** | Grid arrays, time arithmetic, and unit fraction exploration | `{{key:×}}`, `{{key:÷}}`, `{{key:RECT}}`, `{{key:🕒}}` Planetary Clock, `{{key:FDISP}}`, `{{key:.}}` |
| **Grade 4: Division & Fraction Mastery** | Division with remainders and step-by-step fraction reduction | `{{key:÷R}}` Quotient & Remainder, `{{key:a ᵇ/c}}`, `{{key:d/c}}`, `{{key:SIMP}}`, `{{key:LASTX}}` |
| **Grade 5: Unlike Fractions & Surface Area** | Common denominators, 3D volume, and ledger accumulation | `{{key:GCF}}`, `{{key:LCM}}`, `{{key:PRISM}}`, `{{key:Σ+}}` Surface Area Ledger, `{{key:FRQ}}` Tables |
| **Grades 6–7: Number Theory & Sprint** | Negatives, primes, descriptive statistics, and rapid mental math sprints | `{{key:+/-}}`, `{{key:ABS}}`, `{{key:PRIME}}`, `{{key:FACT}}`, `{{key:a:b}}`, `{{key:x²}}`, `{{key:√x}}`, `{{key:IQR}}`, `{{key:MAD}}` |


