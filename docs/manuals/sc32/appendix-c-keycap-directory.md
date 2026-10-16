---
title: "Appendix C: Keycap Matrix & Layout Directory | SC-32 Manual"
description: "Complete 43-key matrix directory, physical dimensions, electrical row/column pin assignments, and primary, left-shifted (`[↰]`), and right-shifted (`[↱]`) legends for the StackCalc SC-32."
---

# Appendix C: Keycap Matrix & Layout Directory

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 HARDWARE // APPENDIX C: 43-KEY MATRIX DIRECTORY</span>
  <span class="te-viewport-status text-sky-400">● 43 PHYSICAL SWITCHES &bull; 8×6 ELECTRICAL SCAN MATRIX &bull; COMPLETE SHIFT DIRECTORY</span>
</div>

<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>{{key:ALL}}</code> (Full 12-digit scientific mantissa; Standard Base-10 Arithmetic; Degrees angular mode default).
</div>

---

## Keypad Physical Geometry & Tactile Matrix

The SC-32 human-machine interface is engineered for tactile feedback and high-speed data entry during rapid calculation sprints and professional engineering field calculations. 

The physical keypad comprises 43 mechanical switch positions organized into three ergonomic functional zones:

{{blocks:sc32_utility_ortho|StackCalc SC-32 Scientific Calculator Faceplate and 43-Key Topography}}
*Figure C.1: StackCalc SC-32 Scientific RPN Calculator physical hardware faceplate render, showing the 43-key layout, upper dynamic LFU softkeys, double-wide {{key:ENTER}}, and high-contrast left (`{{key:↰}}`) and right (`{{key:↱}}`) shift legends.*

<div class="admonition note">
<p class="admonition-title">StackCalc SC-32 Physical Keypad Topology</p>

> **UPPER FUNCTION ZONE (Rows 0 - 2, 6 Columns):**
> • Pitch: 11.50 mm horizontal pitch, 11.30 mm vertical pitch
> • Keycaps: 10.40 mm round cylindrical concave tops with 0.40 mm dished depth
>
> {{key:LFU0}}      {{key:LFU1}}      {{key:LFU2}}      {{key:LFU3}}      {{key:LFU4}}      {{key:LFU5}}      Row 0
> {{key:√x}}        {{key:eˣ}}        {{key:LN}}        {{key:yˣ}}        {{key:1/x}}       {{key:Σ+}}        Row 1
> {{key:STO}}       {{key:RCL}}       {{key:R↓}}        {{key:SIN}}       {{key:COS}}       {{key:TAN}}       Row 2
>
> TRANSITION ZONE (Row 3):
> • ENTER key: Double-wide 21.90 mm × 10.40 mm spanning Columns 0 and 1
> • Primary RPN stack commit target positioned directly beneath left thumb
>
> {{key:ENTER}}       {{key:x⇄y}}       {{key:+/-}}       {{key:E}}         {{key:<-}}        Row 3
>
> LOWER ARITHMETIC ZONE (Rows 4 - 7, 5 Columns):
> • Pitch: Generous 13.80 mm horizontal pitch, 11.30 mm vertical pitch
> • Dedicated power switch at Row 7, Col 0 serves as {{key:C}} and hardware sleep wake
>
> {{key:XEQ}}       {{key:7}}         {{key:8}}         {{key:9}}         {{key:÷}}                     Row 4
> `{{key:↰}}` (Left Shift)   {{key:4}}         {{key:5}}         {{key:6}}         {{key:×}}                     Row 5
> `{{key:↱}}` (Right Shift)   {{key:1}}         {{key:2}}         {{key:3}}         {{key:-}}                     Row 6
> {{key:C}} (ON)    {{key:0}}         {{key:.}}         {{key:x∥y}}       {{key:+}}                     Row 7
</div>

### Tactile Snap-Dome Mechanics & Debouncing Algorithm
* **Actuation Force:** $400\,\text{g}$ tactile stainless steel snap domes providing an unambiguous mechanical snap threshold.
* **Key Travel:** $0.35\,\text{mm}$ short-stroke actuation ensuring zero lost motion.
* **Firmware Debounce Architecture:** Eager actuation on leading falling edge ($0\,\text{ms}$ latency) followed by a $20\,\text{ms}$ lockout window. This eliminates double-strike bounce artifacts even under aggressive 50-problem contest bursts.

---


## Electrical Matrix & Keypad Scanning Bus

The switch matrix is wired as an $8 \times 6$ crossbar scanned by the dual-core 32-bit microcontroller:

* **Row Lines (Strobed Outputs):** GPIO pins `[6, 7, 8, 9, 10, 14, 18, 19]`. Strobed low sequentially in round-robin sequence at $1\,\text{kHz}$ scanning frequency.
* **Column Lines (Sensed Inputs):** GPIO pins `[11, 12, 13, 15, 16, 17]`. Pulled high internally by $50\,\text{k}\Omega$ resistors; active-low detection.
* **Hardware Sleep Wake Interrupt:** Row 7, Column 0 (`{{key:C}}`/ON switch) is routed to an asynchronous edge-triggered interrupt. When the calculator is in deep $11.8\,\mu\text{A}$ sleep, depressing this key immediately wakes the system clock within $5\,\text{ms}$.

---

## The Definitive 43-Key Hardware Matrix Directory & Chapter Index

The table below catalogs every physical switch position, electrical matrix coordinate, laser-foamed keycap legend, left `{{key:↰}}` and right `{{key:↱}}` shift combinations, alpha character, internal scancode, and direct cross-references to the textbook chapters where each operation is fully explained and practiced:

| Key # | Matrix (R, C) | Primary Legend | Left Shift `{{key:↰}}` | Right Shift `{{key:↱}}` | Alpha | Code | Primary & Shift Tutorial Links |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **1** | R0, C0 | `{{key:LFU0}}` | Softkey 1 | Softkey 1 | — | `0x00` | [Sec C.5](#c5-dynamic-lfu-softkey-menus-directory) &bull; [Ch 1.6 Display](01-craftsmanship-hardware.md#16-high-contrast-transflective-graphic-lcd-architecture) |
| **2** | R0, C1 | `{{key:LFU1}}` | Softkey 2 | Softkey 2 | — | `0x01` | [Sec C.5](#c5-dynamic-lfu-softkey-menus-directory) &bull; [Ch 1.6 Display](01-craftsmanship-hardware.md#16-high-contrast-transflective-graphic-lcd-architecture) |
| **3** | R0, C2 | `{{key:LFU2}}` | Softkey 3 | Softkey 3 | — | `0x02` | [Sec C.5](#c5-dynamic-lfu-softkey-menus-directory) &bull; [Ch 1.6 Display](01-craftsmanship-hardware.md#16-high-contrast-transflective-graphic-lcd-architecture) |
| **4** | R0, C3 | `{{key:LFU3}}` | Softkey 4 | Softkey 4 | — | `0x03` | [Sec C.5](#c5-dynamic-lfu-softkey-menus-directory) &bull; [Ch 1.6 Display](01-craftsmanship-hardware.md#16-high-contrast-transflective-graphic-lcd-architecture) |
| **5** | R0, C4 | `{{key:LFU4}}` | Softkey 5 | Softkey 5 | — | `0x04` | [Sec C.5](#c5-dynamic-lfu-softkey-menus-directory) &bull; [Ch 1.6 Display](01-craftsmanship-hardware.md#16-high-contrast-transflective-graphic-lcd-architecture) |
| **6** | R0, C5 | `{{key:LFU5}}` | Softkey 6 | Softkey 6 | — | `0x05` | [Sec C.5](#c5-dynamic-lfu-softkey-menus-directory) &bull; [Ch 1.6 Display](01-craftsmanship-hardware.md#16-high-contrast-transflective-graphic-lcd-architecture) |
| **7** | R1, C0 | `{{key:√x}}` | `{{keycap:x²}}` | `PARTS` Menu | `A` | `0x10` | [Ch 3.1 Powers & Roots](03-algebra-transcendentals.md#31-powers-roots-reciprocals-parallel-operations) &bull; [Ch 3.3 PARTS](03-algebra-transcendentals.md#33-number-parts-functions-g-parts) |
| **8** | R1, C1 | `{{key:eˣ}}` | `{{keycap:10ˣ}}` | `PROB` Menu | `B` | `0x11` | [Ch 3.2 Logs & Exponentials](03-algebra-transcendentals.md#32-logarithms-exponentials-natural-constants) &bull; [Ch 10.3 Bit-Fields](10-computer-science-bases.md#bit-field-extraction-shifting-masking-on-the-rpn-stack) |
| **9** | R1, C2 | `{{key:LN}}` | `{{keycap:LOG}}` | `L.R.` Menu | `C` | `0x12` | [Ch 3.2 Logs & Exponentials](03-algebra-transcendentals.md#32-logarithms-exponentials-natural-constants) &bull; [Ch 9.4 Regression](09-statistics-curve-fitting.md#94-bivariate-linear-regression-pearson-correlation-r) |
| **10**| R1, C3 | `{{key:yˣ}}` | `{{keycap:ˣ√y}}` | `x̄,ȳ` Menu | `D` | `0x13` | [Ch 3.1 Powers & Roots](03-algebra-transcendentals.md#31-powers-roots-reciprocals-parallel-operations) &bull; [Ch 9.3 Stats Means](09-statistics-curve-fitting.md#93-the-statistical-dynamic-softkey-menus) |
| **11**| R1, C4 | `{{key:1/x}}` | `{{keycap:x!}}` | `s,σ` Menu | `E` | `0x14` | [Ch 3.1 Reciprocals](03-algebra-transcendentals.md#31-powers-roots-reciprocals-parallel-operations) &bull; [Ch 3.4 Factorials](03-algebra-transcendentals.md#34-factorials-the-lanczos-gamma-extension-70) &bull; [Ch 9.3 Std Dev](09-statistics-curve-fitting.md#93-the-statistical-dynamic-softkey-menus) |
| **12**| R1, C5 | `{{key:Σ+}}` | `{{keycap:Σ-}}` | `SUMS` Menu | `F` | `0x15` | [Ch 6.3 Surface Area](06-geometry-surface-area.md#63-the-master-surface-area-technique-via-stats-mode) &bull; [Ch 9.2 Accumulators](09-statistics-curve-fitting.md#92-the-6-hardware-statistical-accumulators) |
| **13**| R2, C0 | `{{key:STO}}` | `CMPLX` Mode | `EQN` Mode | `G` | `0x20` | [Ch 2.12 Registers](02-rpn-stack-dynamics.md#212-the-golden-rules-of-stack-conservation) &bull; [Ch 5.2 CMPLX](05-complex-numbers-phasors.md#52-the-f-cmplx-prefix-evaluator-architecture) &bull; [Ch 8.1 EQN](08-calculus-romberg-quadrature.md#81-the-cra-pedagogical-progression-for-numerical-calculus) |
| **14**| R2, C1 | `{{key:RCL}}` | `{{keycap:RND}}` Round | `[SCRL]` Scroll | `H` | `0x21` | [Ch 2.12 Registers](02-rpn-stack-dynamics.md#212-the-golden-rules-of-stack-conservation) &bull; [Ch 3.3 PARTS](03-algebra-transcendentals.md#33-number-parts-functions-g-parts) &bull; [Ch 12.2 Plot Pan](12-function-scatter-plotting.md#122-navigation-pan-zoom-control-scheme) |
| **15**| R2, C2 | `{{key:R↓}}` | `{{keycap:HYP}}` Prefix | `{{keycap:R↑}}` Roll Up | `I` | `0x22` | [Ch 2.6 Stack Rolls](02-rpn-stack-dynamics.md#26-stack-manipulation-keys-architectural-elegance) &bull; [Ch 4.3 Hyperbolics](04-trig-vectors-polar.md#43-hyperbolic-functions-hyp) |
| **16**| R2, C3 | `{{key:SIN}}` | `{{keycap:ASIN}}` | `π` Constant | `J` | `0x23` | [Ch 4.2 Trig](04-trig-vectors-polar.md#42-direct-inverse-trigonometric-functions) &bull; [Ch 3.2 Pi](03-algebra-transcendentals.md#32-logarithms-exponentials-natural-constants) |
| **17**| R2, C4 | `{{key:COS}}` | `{{keycap:ACOS}}` | `{{keycap:%}}` Base Pct | `K` | `0x24` | [Ch 4.2 Trig](04-trig-vectors-polar.md#42-direct-inverse-trigonometric-functions) &bull; [Ch 11.2 Percent](11-financial-tvm.md#112-the-base-preserving-percentage-invariant) |
| **18**| R2, C5 | `{{key:TAN}}` | `{{keycap:ATAN}}` | `{{keycap:%CHG}}` Pct Chg| `L` | `0x25` | [Ch 4.2 Trig](04-trig-vectors-polar.md#42-direct-inverse-trigonometric-functions) &bull; [Ch 11.3 Percent Change](11-financial-tvm.md#113-period-over-period-year-over-year-performance-chg) |
| **19**| R3, C0-1| `{{key:ENTER}}` | `{{keycap:LASTX}}` | `{{keycap:SHOW}}` | `M` | `0x30` | [Ch 2.3 Elevator Lift](02-rpn-stack-dynamics.md#23-stack-lift-mechanics-the-elevator-metaphor) &bull; [Ch 2.7 LASTX](02-rpn-stack-dynamics.md#27-the-lastx-register-error-recovery-archetypes) &bull; [Ch 2.8 SHOW](02-rpn-stack-dynamics.md#28-the-show-key-15-digit-precision-inspection) |
| **20**| R3, C2 | `{{key:x⇄y}}` | `MEM` Specs | `[x⇄?]` Swap Reg| `N` | `0x32` | [Ch 2.6 Swap XY](02-rpn-stack-dynamics.md#26-stack-manipulation-keys-architectural-elegance) &bull; [Ch 1.7 Memory Map](01-craftsmanship-hardware.md#17-dual-slot-ping-pong-continuous-flash-memory-nvm) |
| **21**| R3, C3 | `{{key:+/-}}` | `MODES` Menu | `[\|x\|]` Abs | `O` | `0x33` | [Ch 2.1 Sign Change](02-rpn-stack-dynamics.md#21-the-core-axiom-operands-precede-operators) &bull; [Ch 4.1 Angular Modes](04-trig-vectors-polar.md#41-the-unit-circle-volvelle-angular-modes) &bull; [Ch 3.3 Abs](03-algebra-transcendentals.md#33-number-parts-functions-g-parts) |
| **22**| R3, C4 | `{{key:E}}` | `DISP` Menu | `{{keycap:÷R}}` Div/Rem | `P` | `0x34` | [Ch 3.5 Scientific Notation](03-algebra-transcendentals.md#35-display-formatting-modes-fix-sci-eng-all) &bull; [Ch 10.1 Div/Rem](10-computer-science-bases.md#101-the-36-bit-twos-complement-integer-architecture) |
| **23**| R3, C5 | `{{key:<-}}` | `CLEAR` Menu | *(Unassigned)*| — | `0x35` | [Ch 2.1 Backspace](02-rpn-stack-dynamics.md#21-the-core-axiom-operands-precede-operators) &bull; [Ch 2.6 Clear Stack](02-rpn-stack-dynamics.md#26-stack-manipulation-keys-architectural-elegance) |
| **24**| R4, C0 | `{{key:XEQ}}` | `FN=` Define | `POLY` Solver | — | `0x40` | [Ch 8.1 EQN Execute](08-calculus-romberg-quadrature.md#81-the-cra-pedagogical-progression-for-numerical-calculus) &bull; [Ch 7.2 Cubic Solver](07-polynomials-brent-solver.md#72-characteristic-polynomial-solver-g-poly) |
| **25**| R4, C1 | `{{key:7}}` | `{{keycap:↓}}` Trace Down| `{{keycap:SOLVE}}` Brent | `Q` | `0x41` | [Ch 2.1 Digit Entry](02-rpn-stack-dynamics.md#21-the-core-axiom-operands-precede-operators) &bull; [Ch 12.2 Plot Pan](12-function-scatter-plotting.md#122-navigation-pan-zoom-control-scheme) &bull; [Ch 7.5 Brent](07-polynomials-brent-solver.md#75-richard-brents-numerical-root-finder-g-solve) |
| **26**| R4, C2 | `{{key:8}}` | `{{keycap:↑}}` Trace Up | `{{keycap:∫}}` Quadrature| `R` | `0x42` | [Ch 2.1 Digit Entry](02-rpn-stack-dynamics.md#21-the-core-axiom-operands-precede-operators) &bull; [Ch 12.2 Plot Pan](12-function-scatter-plotting.md#122-navigation-pan-zoom-control-scheme) &bull; [Ch 8.2 Romberg](08-calculus-romberg-quadrature.md#82-adaptive-romberg-numerical-quadrature-g) |
| **27**| R4, C3 | `{{key:9}}` | `{{keycap:▸km}}` Conv | `{{keycap:▸mi}}` Conv | `S` | `0x43` | [Ch 2.1 Digit Entry](02-rpn-stack-dynamics.md#21-the-core-axiom-operands-precede-operators) &bull; [Ch 13.6 Geodesy](13-applied-stem-case-studies.md#136-case-study-6-civil-surveying-geodetic-traversing) |
| **28**| R4, C4 | `{{key:÷}}` | `x?y` Menu | `x?0` Menu | — | `0x44` | [Ch 2.4 Division](02-rpn-stack-dynamics.md#24-dyadic-stack-drop-mechanics) &bull; [Ch 14 Rapid Calculation](14-uil-contest-playbook.md) |
| **29**| R5, C0 | `{{key:↰}}` (Left Shift)| *(Left Shift Latch)* | *(Left Shift Latch)* | — | `0x50` | [Sec C.1 Latch Hardware](#c1-keypad-physical-geometry-tactile-matrix) &bull; Primary Left Shift prefix |
| **30**| R5, C1 | `{{key:4}}` | `{{keycap:▸θ,r}}` Polar | `{{keycap:▸y,x}}` Rect | `T` | `0x51` | [Ch 2.1 Digit Entry](02-rpn-stack-dynamics.md#21-the-core-axiom-operands-precede-operators) &bull; [Ch 4.4 Coordinate Transforms](04-trig-vectors-polar.md#44-2d-coordinate-transformations-polar-leftrightarrow-rectangular) |
| **31**| R5, C2 | `{{key:5}}` | `{{keycap:▸HR}}` Hours | `{{keycap:▸HMS}}` Time | `U` | `0x52` | [Ch 2.1 Digit Entry](02-rpn-stack-dynamics.md#21-the-core-axiom-operands-precede-operators) &bull; [Ch 4.5 Spherical Trig](04-trig-vectors-polar.md#45-3d-spherical-trigonometry-great-circle-distance) |
| **32**| R5, C3 | `{{key:6}}` | `{{keycap:▸DEG}}` Angle | `{{keycap:▸RAD}}` Angle | `V` | `0x53` | [Ch 2.1 Digit Entry](02-rpn-stack-dynamics.md#21-the-core-axiom-operands-precede-operators) &bull; [Ch 4.1 Angular Modes](04-trig-vectors-polar.md#41-the-unit-circle-volvelle-angular-modes) |
| **33**| R5, C4 | `{{key:×}}` | `BASE` Menu | `FLAGS` Menu | — | `0x54` | [Ch 2.4 Product](02-rpn-stack-dynamics.md#24-dyadic-stack-drop-mechanics) &bull; [Ch 10.2 Bases](10-computer-science-bases.md#102-dynamic-base-modes-hex-dec-oct-bin) &bull; [Ch 2.9 Flags](02-rpn-stack-dynamics.md#29-configurable-stack-depths-4-lv-8-lv-and-inf-modes) |
| **34**| R6, C0 | `{{key:↱}}` (Right Shift)| *(Right Shift Latch)* | *(Right Shift Latch)* | — | `0x60` | [Sec C.1 Latch Hardware](#c1-keypad-physical-geometry-tactile-matrix) &bull; Secondary Right Shift prefix |
| **35**| R6, C1 | `{{key:1}}` | `{{keycap:▸kg}}` Mass | `{{keycap:▸lb}}` Mass | `W` | `0x61` | [Ch 2.1 Digit Entry](02-rpn-stack-dynamics.md#21-the-core-axiom-operands-precede-operators) &bull; [Ch 13.5 Rocket Flight](13-applied-stem-case-studies.md#135-case-study-5-orbital-mechanics-rocket-flight-dynamics) |
| **36**| R6, C2 | `{{key:2}}` | `{{keycap:▸°C}}` Temp | `{{keycap:▸°F}}` Temp | `X` | `0x62` | [Ch 2.1 Digit Entry](02-rpn-stack-dynamics.md#21-the-core-axiom-operands-precede-operators) &bull; [Ch 13.2 Thermodynamics](13-applied-stem-case-studies.md#132-case-study-2-thermodynamics-heat-transfer) |
| **37**| R6, C3 | `{{key:3}}` | `{{keycap:▸cm}}` Length | `{{keycap:▸in}}` Length | `Y` | `0x63` | [Ch 2.1 Digit Entry](02-rpn-stack-dynamics.md#21-the-core-axiom-operands-precede-operators) &bull; [Ch 13.1 3D Printing](13-applied-stem-case-studies.md#131-case-study-1-fluid-mechanics-3d-printing-extrusion-dynamics) |
| **38**| R6, C4 | `{{key:-}}` | `{{keycap:▸l}}` Volume | `{{keycap:▸gal}}` Volume| — | `0x64` | [Ch 2.4 Subtraction](02-rpn-stack-dynamics.md#24-dyadic-stack-drop-mechanics) &bull; [Ch 13.1 Flow Rates](13-applied-stem-case-studies.md#131-case-study-1-fluid-mechanics-3d-printing-extrusion-dynamics) |
| **39**| R7, C0 | `{{key:C}}` (ON) | `{{keycap:?}}` Diagnostics| `OFF` Sleep | — | `0x70` | [Ch 1.1 Cold Boot](01-craftsmanship-hardware.md#11-dual-core-silicon-architecture-cold-boot-dynamics) &bull; [Ch 1.8 Self-Tests](01-craftsmanship-hardware.md#18-diagnostic-checkpoints-self-test-protocols) |
| **40**| R7, C1 | `{{key:0}}` | `REGS` Viewer | `VIEW` Single | `Z` | `0x71` | [Ch 2.1 Digit Entry](02-rpn-stack-dynamics.md#21-the-core-axiom-operands-precede-operators) &bull; [Ch 2.12 Variables](02-rpn-stack-dynamics.md#212-the-golden-rules-of-stack-conservation) |
| **41**| R7, C2 | `{{key:.}}` | `{{keycap:FDISP}}` Frac | `{{keycap:/c}}` Denom | `i` | `0x72` | [Ch 2.1 Radix Point](02-rpn-stack-dynamics.md#21-the-core-axiom-operands-precede-operators) &bull; [Ch 3.5 Fractions](03-algebra-transcendentals.md#35-display-formatting-modes-fix-sci-eng-all) |
| **42**| R7, C3 | `{{key:x∥y}}` | `TVM` Solver | `PLOT` Mode | `(i)`| `0x73` | [Ch 3.1 Parallel / Thin Lens](03-algebra-transcendentals.md#31-powers-roots-reciprocals-parallel-operations) &bull; [Ch 11.5 TVM](11-financial-tvm.md#115-the-5-variable-time-value-of-money-tvm-architecture) &bull; [Ch 12.1 Vector Plot](12-function-scatter-plotting.md#121-the-transflective-64-point-vector-rendering-engine) |
| **43**| R7, C4 | `{{key:+}}` | `[LBL]` Label | `[RTN]` Return | — | `0x74` | [Ch 2.4 Addition](02-rpn-stack-dynamics.md#24-dyadic-stack-drop-mechanics) &bull; [Ch 8.1 Equations](08-calculus-romberg-quadrature.md#81-the-cra-pedagogical-progression-for-numerical-calculus) |

---

## Authoritative HP32SII Deviations Master Index

The SC-32 intentionally deviates from the 1988 vintage HP-32SII in exact alignment with the project button rubric:

1. **`{{key:↱}}` + `+/-` = `|x|` (Absolute Value):**
   * *HP32SII Original:* `(` (open parenthesis for algebraic equation editor).
   * *SC-32 Rationale:* Parentheses are redundant in direct RPN mode; direct absolute value is far more useful in applied engineering.
2. **`{{key:↱}}` + `E` = `÷R` (Integer Division & Remainder):**
   * *HP32SII Original:* `)` (close parenthesis for algebraic equation editor).
   * *SC-32 Rationale:* Returns integer quotient in $Y$ and remainder in $X$ in a single keystroke.
3. **`{{key:↱}}` + `<-` = Unassigned:**
   * *HP32SII Original:* `=` (equals for algebraic equation editor).
   * *SC-32 Rationale:* Equality comparison belongs in the `x?y` and `x?0` menus; left unassigned.
4. **`{{key:↰}}` + `0` = `REGS` (Register Viewer):**
   * *HP32SII Original:* `INPUT` (program input prompt).
   * *SC-32 Rationale:* Programming prompts are replaced by dynamic equation parameters; `REGS` allows instant inspection of all variables.
5. **Key `Row 7, Col 3` (Multi-Action Key):**
   * *HP32SII Original:* `R/S` (Run/Stop program execution).
   * *SC-32 Assignment:* Primary: `x∥y`, Left Shift `{{key:↰}}`: `TVM`, Right Shift `{{key:↱}}`: `PLOT`, Alpha: `(i)`.
   * *SC-32 Rationale:* Traditional line programming is replaced by RPN step equations, numerical quadrature, root finding, and financial solvers.
6. **`{{key:↰}}` + `+` = `LBL`:**
   * Restored equation safety key ensuring equations retain explicit labels.
7. **`{{key:↱}}` + `XEQ` = `POLY`:**
   * Cubic polynomial solver workspace (`A B C D EXEC CLR` on LFU softkeys).
8. **Top 6 LFU Dynamic Softkeys:**
   * Context-aware softkey strip permanently positioned above the primary math rows.

---

## Dynamic LFU Softkey Menus Directory

The six top keys (`{{key:LFU0}}` through `{{key:LFU5}}`) automatically remap depending on active menu state:

| Menu | LFU0 | LFU1 | LFU2 | LFU3 | LFU4 | LFU5 |
|:---|:---|:---|:---|:---|:---|:---|
| DISP | FIX n | SCI n | ENG n | ALL | (None) | (None) |
| MODES | DEG | RAD | GRAD | . | , | (None) |
| BASE | HEX | DEC | OCT | BIN | (None) | (None) |
| CLEAR | CLEQN | CLVARS | CLALL | CLΣ | CLREGS | CLSTK |
| FLAGS | SF n | CF n | FS? n | 4-LVL | 8-LVL | INF |
| PARTS | IP | FP | ABS | SGN | GCD | LCM |
| PROB | Cn,r | Pn,r | x! | RAND | (None) | (None) |
| SUMS | Σx | Σy | Σx² | Σy² | Σxy | n |
| x̄,ȳ | x̄ | ȳ | x̄w | (None) | (None) | (None) |
| s,σ | sx | sy | σx | σy | (None) | (None) |
| L.R. | ŷ | x̂ | r | m | b | (None) |
| TVM | N | I% | PV | PMT | FV | END/BEG |
| POLY | A | B | C | D | EXEC | CLR |

---

## Verification & Firmware Implementation Reference

The 43-key matrix pinouts, electrical scanning bus, and shift mappings are verified in:
* `Hardware/sc32_faceplate.kicad_pcb`
* `Hardware/sc32_schematic.kicad_sch`
* `Firmware/hardware_wrapper.c`
* `watch-calc-32/documentation/button_rubric.md`
