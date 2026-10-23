---
title: "Appendix C: Keycap Directory & How We Built StackCalc | Thinking in the Stack (SC-32)"
description: "Complete 43-key matrix directory, primary, left-shifted (`[↰]`), and right-shifted (`[↱]`) legends, and How We Built StackCalc (open-source hardware, cross-surface simulation, and Hackaday build logs)."
---

# Appendix C: Keycap Directory & How We Built StackCalc

---

## Keypad Layout & Functional Zones

The SC-32 keypad is organized into 43 tactile switch positions across three functional zones for rapid eyes-on-the-page calculation:

{{blocks:sc32_utility_ortho|StackCalc SC-32 Scientific Calculator Faceplate and 43-Key Topography}}
*Figure C.1: StackCalc SC-32 Scientific RPN Calculator physical faceplate render, showing the 43-key layout, upper dynamic LFU softkeys, double-wide {{key:ENTER}}, and high-contrast left (`{{key:↰}}`) and right (`{{key:↱}}`) shift legends.*

### Upper Function Zone (Rows 0–2, 6 Columns)

The top three rows group the six context-sensitive LFU softkeys (`Row 0`) directly above the primary transcendental, statistical, and trigonometric keys (`Rows 1–2`):

| Row | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 0** | `{{key:LFU0}}` | `{{key:LFU1}}` | `{{key:LFU2}}` | `{{key:LFU3}}` | `{{key:LFU4}}` | `{{key:LFU5}}` |
| **Row 1** | `{{key:√x}}` | `{{key:eˣ}}` | `{{key:LN}}` | `{{key:yˣ}}` | `{{key:1/x}}` | `{{key:Σ+}}` |
| **Row 2** | `{{key:STO}}` | `{{key:RCL}}` | `{{key:R↓}}` | `{{key:SIN}}` | `{{key:COS}}` | `{{key:TAN}}` |

### Transition Zone (Row 3)

Row 3 bridges the upper scientific function array and the lower number pad, placing the double-wide `{{key:ENTER}}` bar (spanning Columns 0 and 1) directly beneath the thumb alongside register swap, sign change, scientific exponent entry, and non-destructive backspace:

| Row | Col 0 & 1 (Double-Wide) | Col 2 | Col 3 | Col 4 | Col 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 3** | `{{key:ENTER}}` | `{{key:x⇄y}}` | `{{key:+/-}}` | `{{key:E}}` | `{{key:<-}}` |

### Lower Arithmetic Zone (Rows 4–7, 5 Columns)

The lower four rows use a wider 5-column spacing for fast touch-entry of digits and arithmetic operators, with left shift (`{{key:↰}}`), right shift (`{{key:↱}}`), and `{{key:C}}` (`ON`) aligned along the left margin:

| Row | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 4** | `{{key:XEQ}}` | `{{key:7}}` | `{{key:8}}` | `{{key:9}}` | `{{key:÷}}` |
| **Row 5** | `{{key:↰}}` (Left Shift) | `{{key:4}}` | `{{key:5}}` | `{{key:6}}` | `{{key:×}}` |
| **Row 6** | `{{key:↱}}` (Right Shift) | `{{key:1}}` | `{{key:2}}` | `{{key:3}}` | `{{key:-}}` |
| **Row 7** | `{{key:C}}` (ON) | `{{key:0}}` | `{{key:.}}` | `{{key:x∥y}}` | `{{key:+}}` |

---

## The Definitive 43-Key Directory & Chapter Index

The table below catalogs every key position, primary legend, left `{{key:↰}}` and right `{{key:↱}}` shift combinations, alpha character, and direct cross-references to the chapters where each operation is explained and practiced:

| Key # | Matrix (R, C) | Primary Legend | Left Shift `{{key:↰}}` | Right Shift `{{key:↱}}` | Alpha | Primary & Shift Tutorial Links |
| :---: | :---: | :--- | :--- | :--- | :---: | :--- |
| **1** | R0, C0 | `{{key:LFU0}}` | Softkey 1 | Softkey 1 | — | [Dynamic LFU Softkey Menus](#dynamic-lfu-softkey-menus-directory) • [Ch 1: Screen & Stack](01-craftsmanship-hardware.md) |
| **2** | R0, C1 | `{{key:LFU1}}` | Softkey 2 | Softkey 2 | — | [Dynamic LFU Softkey Menus](#dynamic-lfu-softkey-menus-directory) • [Ch 1: Screen & Stack](01-craftsmanship-hardware.md) |
| **3** | R0, C2 | `{{key:LFU2}}` | Softkey 3 | Softkey 3 | — | [Dynamic LFU Softkey Menus](#dynamic-lfu-softkey-menus-directory) • [Ch 1: Screen & Stack](01-craftsmanship-hardware.md) |
| **4** | R0, C3 | `{{key:LFU3}}` | Softkey 4 | Softkey 4 | — | [Dynamic LFU Softkey Menus](#dynamic-lfu-softkey-menus-directory) • [Ch 1: Screen & Stack](01-craftsmanship-hardware.md) |
| **5** | R0, C4 | `{{key:LFU4}}` | Softkey 5 | Softkey 5 | — | [Dynamic LFU Softkey Menus](#dynamic-lfu-softkey-menus-directory) • [Ch 1: Screen & Stack](01-craftsmanship-hardware.md) |
| **6** | R0, C5 | `{{key:LFU5}}` | Softkey 6 | Softkey 6 | — | [Dynamic LFU Softkey Menus](#dynamic-lfu-softkey-menus-directory) • [Ch 1: Screen & Stack](01-craftsmanship-hardware.md) |
| **7** | R1, C0 | `{{key:√x}}` | `{{key:x²}}` | `PARTS` Menu | `A` | [Ch 3: Powers, Roots & PARTS](03-algebra-transcendentals.md) |
| **8** | R1, C1 | `{{key:eˣ}}` | `{{key:10ˣ}}` | `PROB` Menu | `B` | [Ch 3: Exponentials](03-algebra-transcendentals.md) • [Ch 10: Combinatorics](10-computer-science-bases.md) |
| **9** | R1, C2 | `{{key:LN}}` | `{{key:LOG}}` | `L.R.` Menu | `C` | [Ch 3: Logarithms](03-algebra-transcendentals.md) • [Ch 9: Linear Regression](09-statistics-curve-fitting.md) |
| **10**| R1, C3 | `{{key:yˣ}}` | `{{key:ˣ√y}}` | `x̄,ȳ` Menu | `D` | [Ch 3: Powers & Roots](03-algebra-transcendentals.md) • [Ch 9: Sample Means](09-statistics-curve-fitting.md) |
| **11**| R1, C4 | `{{key:1/x}}` | `{{key:x!}}` | `s,σ` Menu | `E` | [Ch 3: Reciprocals & Factorials](03-algebra-transcendentals.md) • [Ch 9: Standard Deviation](09-statistics-curve-fitting.md) |
| **12**| R1, C5 | `{{key:Σ+}}` | `{{key:Σ-}}` | `SUMS` Menu | `F` | [Ch 6: Surface Area](06-geometry-surface-area.md) • [Ch 9: Statistical Accumulators](09-statistics-curve-fitting.md) |
| **13**| R2, C0 | `{{key:STO}}` | `CMPLX` Mode | `EQN` Mode | `G` | [Ch 2: Storage Registers](02-rpn-stack-dynamics.md) • [Ch 5: Complex Phasors](05-complex-numbers-phasors.md) • [Ch 8: Equations](08-calculus-romberg-quadrature.md) |
| **14**| R2, C1 | `{{key:RCL}}` | `{{key:RND}}` Round | `[SCRL]` Scroll | `H` | [Ch 2: Recall Arithmetic](02-rpn-stack-dynamics.md) • [Ch 3: Rounding](03-algebra-transcendentals.md) • [Ch 12: Plot Pan](12-function-scatter-plotting.md) |
| **15**| R2, C2 | `{{key:R↓}}` | `{{key:HYP}}` Prefix | `{{key:R↑}}` Roll Up | `I` | [Ch 2: Stack Rolls](02-rpn-stack-dynamics.md) • [Ch 4: Hyperbolic Functions](04-trig-vectors-polar.md) |
| **16**| R2, C3 | `{{key:SIN}}` | `{{key:ASIN}}` | `π` Constant | `J` | [Ch 4: Trigonometry](04-trig-vectors-polar.md) • [Ch 3: Pi Constant](03-algebra-transcendentals.md) |
| **17**| R2, C4 | `{{key:COS}}` | `{{key:ACOS}}` | `{{key:%}}` Base Pct | `K` | [Ch 4: Trigonometry](04-trig-vectors-polar.md) • [Ch 11: Base-Preserving Percent](11-financial-tvm.md) |
| **18**| R2, C5 | `{{key:TAN}}` | `{{key:ATAN}}` | `{{key:%CHG}}` Pct Chg| `L` | [Ch 4: Trigonometry](04-trig-vectors-polar.md) • [Ch 11: Percent Change](11-financial-tvm.md) |
| **19**| R3, C0-1| `{{key:ENTER}}` | `{{key:LASTX}}` | `{{key:SHOW}}` | `M` | [Ch 2: Stack Lift, LASTX & Full Precision](02-rpn-stack-dynamics.md) |
| **20**| R3, C2 | `{{key:x⇄y}}` | `MEM` Specs | `[x⇄?]` Swap Reg| `N` | [Ch 2: Register Swap & Memory Exchange](02-rpn-stack-dynamics.md) |
| **21**| R3, C3 | `{{key:+/-}}` | `MODES` Menu | `{{key:ABS}}` Abs | `O` | [Ch 2: Sign Change](02-rpn-stack-dynamics.md) • [Ch 4: Angular Modes](04-trig-vectors-polar.md) • [Ch 3: Absolute Value](03-algebra-transcendentals.md) |
| **22**| R3, C4 | `{{key:E}}` | `DISP` Menu | `{{key:÷R}}` Div/Rem | `P` | [Ch 3: Scientific Notation & Display](03-algebra-transcendentals.md) • [Ch 10: Integer Division](10-computer-science-bases.md) |
| **23**| R3, C5 | `{{key:<-}}` | `CLEAR` Menu | *(Unassigned)*| — | [Ch 2: Backspace & Stack Clear](02-rpn-stack-dynamics.md) |
| **24**| R4, C0 | `{{key:XEQ}}` | `FN=` Define | `POLY` Solver | — | [Ch 8: Equation Execution](08-calculus-romberg-quadrature.md) • [Ch 7: Cubic Solver](07-polynomials-brent-solver.md) |
| **25**| R4, C1 | `{{key:7}}` | `{{key:↓}}` Trace Down| `{{key:SOLVE}}` Brent | `Q` | [Ch 2: Digit Entry](02-rpn-stack-dynamics.md) • [Ch 12: Plot Trace](12-function-scatter-plotting.md) • [Ch 7: Brent Solver](07-polynomials-brent-solver.md) |
| **26**| R4, C2 | `{{key:8}}` | `{{key:↑}}` Trace Up | `{{key:∫}}` Quadrature| `R` | [Ch 2: Digit Entry](02-rpn-stack-dynamics.md) • [Ch 12: Plot Trace](12-function-scatter-plotting.md) • [Ch 8: Romberg Integration](08-calculus-romberg-quadrature.md) |
| **27**| R4, C3 | `{{key:9}}` | `{{key:▸km}}` Conv | `{{key:▸mi}}` Conv | `S` | [Ch 2: Digit Entry](02-rpn-stack-dynamics.md) • [Ch 13: Geodesy Conversions](13-applied-stem-case-studies.md) |
| **28**| R4, C4 | `{{key:÷}}` | `x?y` Menu | `x?0` Menu | — | [Ch 2: Division & Stack Comparisons](02-rpn-stack-dynamics.md) |
| **29**| R5, C0 | `{{key:↰}}` (Left Shift)| *(Left Shift Latch)* | *(Left Shift Latch)* | — | [Keypad Layout](#keypad-layout-functional-zones) • Primary Left Shift prefix |
| **30**| R5, C1 | `{{key:4}}` | `{{key:▸θ,r}}` Polar | `{{key:▸y,x}}` Rect | `T` | [Ch 2: Digit Entry](02-rpn-stack-dynamics.md) • [Ch 4: Polar & Rectangular Vectors](04-trig-vectors-polar.md) |
| **31**| R5, C2 | `{{key:5}}` | `{{key:▸HR}}` Hours | `{{key:▸HMS}}` Time | `U` | [Ch 2: Digit Entry](02-rpn-stack-dynamics.md) • [Ch 4: Sexagesimal Angles & Time](04-trig-vectors-polar.md) |
| **32**| R5, C3 | `{{key:6}}` | `{{key:▸DEG}}` Angle | `{{key:▸RAD}}` Angle | `V` | [Ch 2: Digit Entry](02-rpn-stack-dynamics.md) • [Ch 4: Angular Conversions](04-trig-vectors-polar.md) |
| **33**| R5, C4 | `{{key:×}}` | `BASE` Menu | `FLAGS` Menu | — | [Ch 2: Multiplication & System Flags](02-rpn-stack-dynamics.md) • [Ch 10: Radix Bases](10-computer-science-bases.md) |
| **34**| R6, C0 | `{{key:↱}}` (Right Shift)| *(Right Shift Latch)* | *(Right Shift Latch)* | — | [Keypad Layout](#keypad-layout-functional-zones) • Secondary Right Shift prefix |
| **35**| R6, C1 | `{{key:1}}` | `{{key:▸kg}}` Mass | `{{key:▸lb}}` Mass | `W` | [Ch 2: Digit Entry](02-rpn-stack-dynamics.md) • [Ch 13: Mass Conversions](13-applied-stem-case-studies.md) |
| **36**| R6, C2 | `{{key:2}}` | `{{key:▸°C}}` Temp | `{{key:▸°F}}` Temp | `X` | [Ch 2: Digit Entry](02-rpn-stack-dynamics.md) • [Ch 13: Temperature Conversions](13-applied-stem-case-studies.md) |
| **37**| R6, C3 | `{{key:3}}` | `{{key:▸cm}}` Length | `{{key:▸in}}` Length | `Y` | [Ch 2: Digit Entry](02-rpn-stack-dynamics.md) • [Ch 13: Dimensional Conversions](13-applied-stem-case-studies.md) |
| **38**| R6, C4 | `{{key:-}}` | `{{key:▸l}}` Volume | `{{key:▸gal}}` Volume| — | [Ch 2: Subtraction](02-rpn-stack-dynamics.md) • [Ch 13: Fluid Volume Conversions](13-applied-stem-case-studies.md) |
| **39**| R7, C0 | `{{key:C}}` (ON) | `{{key:?}}` Diagnostics| `OFF` Sleep | — | [Ch 1: Instant-On Wake & Clear](01-craftsmanship-hardware.md) |
| **40**| R7, C1 | `{{key:0}}` | `REGS` Viewer | `VIEW` Single | `Z` | [Ch 2: Digit Entry & Register Inspection](02-rpn-stack-dynamics.md) |
| **41**| R7, C2 | `{{key:.}}` | `{{key:FDISP}}` Frac | `{{key:/c}}` Denom | `i` | [Ch 2: Radix Point](02-rpn-stack-dynamics.md) • [Ch 3: Exact Fractions](03-algebra-transcendentals.md) |
| **42**| R7, C3 | `{{key:x∥y}}` | `TVM` Solver | `PLOT` Mode | `(i)`| [Ch 3: Parallel Operator](03-algebra-transcendentals.md) • [Ch 11: TVM Solver](11-financial-tvm.md) • [Ch 12: Function Plotting](12-function-scatter-plotting.md) |
| **43**| R7, C4 | `{{key:+}}` | `[LBL]` Label | `[RTN]` Return | — | [Ch 2: Addition](02-rpn-stack-dynamics.md) • [Ch 8: Equation Labels](08-calculus-romberg-quadrature.md) |

---

## Authoritative HP32SII Deviations Master Index

The SC-32 intentionally deviates from the 1991 vintage HP-32SII to streamline direct RPN engineering workflows:

1. **`{{key:↱}}` + `+/-` = `|x|` (Absolute Value):**
   * *HP32SII Original:* `(` (open parenthesis for algebraic equation editor).
   * *SC-32 Rationale:* Parentheses are redundant in direct RPN mode; direct absolute value is far more useful in applied engineering.
2. **`{{key:↱}}` + `E` = `÷R` (Integer Division & Remainder):**
   * *HP32SII Original:* `)` (close parenthesis for algebraic equation editor).
   * *SC-32 Rationale:* Returns integer quotient in $X$ and remainder in $Y$ in a single keystroke.
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

## How We Built StackCalc: Open-Source Hardware & Hackaday Build Logs

Rather than printing pages of static component datasheets in this book, we document the live hardware evolution on **[stackcalc.io/hardware](https://stackcalc.io/hardware)** and in our public engineering build logs on **[Hackaday](https://hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator)**. Here is a summary of how we used open-source hardware engineering, cross-surface simulation, and 3D-printable prototyping to build the StackCalc architecture from the ground up:

### Why We Started on the Apple Watch—and Built One Calculator Core for Every Surface
StackCalc began with a simple observation on the tiny screen of an Apple Watch: on a wrist-sized display, algebraic parentheses and scrolling formula bars are almost impossible to type accurately, whereas Reverse Polish Notation needs only a number pad, `{{key:ENTER}}`, and immediate operators.

Very quickly, a deeper design challenge appeared. A calculator can look visually consistent across a Watch, an iPhone, an iPad, and a physical handheld while subtly disagreeing at the exact moments that teach a learner how stack calculation works: `{{key:ENTER}}` stack lift, an interrupted digit buffer, an error recovery state, or `{{key:LASTX}}` preservation. To guarantee that every instrument behaves identically, a single deterministic state machine drives every surface. Whether a keypress originates from a wrist tap, a touchscreen button, or a physical row-and-column switch contact, it triggers the exact same 4-register transition before any screen renders a pixel.

### Non-Volatile State Preservation & Continuous Memory
An engineering calculator is only as trustworthy as its memory between sessions. If a calculator loses its stack or statistical accumulators when its display goes to sleep, the engineer is forced right back to scratch paper:

* **Atomic State Snapshots:** Whenever the SC-32 enters low-power sleep—or immediately following a state change—it writes all four stack registers ($T, Z, Y, X$), `LAST x`, the 27 alphabetical storage registers (`A`–`Z` and `i`), the six bivariate statistical accumulators, active display formatting flags, and stored equations into alternating non-volatile memory slots protected by a cyclic redundancy checksum.
* **Non-Destructive Error Recovery:** If an evaluation encounters an undefined operation (`DIVIDE BY 0`, `INVALID DATA`, or `NO ROOT FOUND`), the stack freezes in place before consuming the operands. Tapping `{{key:C}}` (`ON`) or `{{key:<-}}` clears the banner and leaves your original numbers intact in $Y$ and $X$.

### Simulating Hardware in Software Before Board Bring-Up
While the custom PCB was in fabrication, we built a thin browser-based hardware simulator wired directly to a compiled microcontroller emulator. Instead of calling high-level software functions, clicking a key in the browser simulator looks up the physical row-and-column coordinate in the shared key manifest, injects that electrical matrix contact into emulator memory, steps the compiled firmware image, and streams changed $132 \times 65$ display frames back to the screen. That allowed us to verify matrix scanning, continuous-memory ping-pong slots, and pixel rendering long before the first physical board arrived at the bench.

### Board-Aware 3D Printing & Tool-Free Sliding Assembly
As chronicled in our Hackaday logs (*"How the PCB Design Shapes a Printed Calculator"* and *"A Tool-Free Calculator Built Around a Sliding Assembly"*), the physical enclosure was never drawn as an empty decorative shell. Instead, our parametric CAD scripts read fixed coordinates directly from the KiCad circuit board layout so that rails, display openings, and switch clearances stay locked to the actual board datum:

* **Four Mechanical Functions Separated:** The 3D-printed prototype consists of four interlocking parts—a tapered chassis, a unified faceplate, a flexible TPU keypad membrane (modeled across a 280-condition press-angle and offset parameter sweep), and a snap-retained top cap. By separating **Guide** (generous rail lead-ins), **Capture** (sliding channel overlap), **Stop** (positive seating shoulders), and **Release** (deliberate service catches), the assembly slides together and reopens without buried screws or prying against the display.
* **Open Printable Files & Live Build Logs:** Complete 3D-printable `.stl` and PrusaSlicer `.3mf` project files, classroom manipulative packs, and ongoing hardware test records are freely available at **[stackcalc.io/downloads](https://stackcalc.io/downloads)** and **[hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator](https://hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator)**.

---

To put these 43 physical keys to work across every major branch of mathematics, physics, engineering, and finance, continue to **[Appendix D: Mathematical Constants, SI Units & Master STEM Equation Directory](appendix-d-constants-and-equations.md)**.



