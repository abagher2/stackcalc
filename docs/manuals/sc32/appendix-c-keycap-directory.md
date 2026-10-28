---
title: "Appendix C: Keycap Directory, HP-32SII / HP-15C / HP-12C Comparison & How We Built StackCalc | Thinking in the Stack (SC-32)"
description: "Complete 43-key matrix directory, primary, left-shifted, and right-shifted legends, authoritative comparison against the HP-32SII, HP-15C, and HP-12C, and How We Built StackCalc."
---

# Appendix C: Keycap Directory & How We Built StackCalc

---

## Physical Keypad Layout & Functional Guide to the 43 Buttons

A great scientific instrument faces a fundamental human-factors paradox: it must expose dozens of transcendental functions, statistical estimators, coordinate transformations, and numerical solvers without burying everyday arithmetic inside scrolling multi-page menus or crowding the faceplate with a hundred tiny, unpressable keys. The SC-32 resolves this tension through a disciplined **43-key tactile matrix** divided into three ergonomic zones, paired with a consistent **three-layer shift grammar** that lets your fingers locate any function by mathematical association rather than rote memorization.

{{blocks:sc32_utility_ortho|StackCalc SC-32 Scientific RPN Calculator physical faceplate render, showing the 43-key layout, upper dynamic LFU softkeys, double-wide ENTER bar, and high-contrast primary and secondary shift legends.}}

### The Three-Layer Ergonomic Grammar

Below the top row of six dynamic softkeys, each of the 37 main physical keys carries **three coordinated operational meanings**—plus an automatic **alpha character** for variable and equation naming—organized by a strict conceptual rule:

* **Primary Legend (White Center Label — 1 Tap):** Every key's unshifted tap executes the foundational, highest-frequency operation for that position on the faceplate: core transcendental functions (`{{key:√x}}`, `{{key:eˣ}}`, `{{key:LN}}`, `{{key:yˣ}}`, `{{key:1/x}}`, `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`), statistical accumulation (`{{key:Σ+}}`), stack and memory control (`{{key:STO}}`, `{{key:RCL}}`, `{{key:R↓}}`, `{{key:ENTER}}`, `{{key:x⇄y}}`), and immediate postfix arithmetic (`{{key:÷}}`, `{{key:×}}`, `{{key:-}}`, `{{key:+}}`, `{{key:x∥y}}`).
* **Left Shift (`{{key:↰}}` — Mathematical Inverse or Direct Companion):** Tapping `{{key:↰}}` accesses the natural mathematical inverse or twin printed above the upper-left corner of the key. Once you know where a primary function lives, your finger already knows where its inverse lives: `{{key:√x}}` $\leftrightarrow$ `{{key:x²}}`, `{{key:eˣ}}` $\leftrightarrow$ `{{key:10ˣ}}`, `{{key:LN}}` $\leftrightarrow$ `{{key:LOG}}`, `{{key:yˣ}}` $\leftrightarrow$ `{{key:ˣ√y}}`, `{{key:1/x}}` $\leftrightarrow$ `{{key:x!}}`, `{{key:Σ+}}` $\leftrightarrow$ `{{key:Σ-}}`, `{{key:SIN}}` $\leftrightarrow$ `{{key:ASIN}}`, `{{key:COS}}` $\leftrightarrow$ `{{key:ACOS}}`, `{{key:TAN}}` $\leftrightarrow$ `{{key:ATAN}}`, and `{{key:ENTER}}` $\leftrightarrow$ `{{key:LASTX}}` (which recovers the pre-operation operand after any function). Across the lower number pad, `{{key:↰}}` consistently converts imperial inputs **into metric (SI) units** (`{{key:▸km}}`, `{{key:▸kg}}`, `{{key:▸°C}}`, `{{key:▸cm}}`, `{{key:▸l}}`) and polar/decimal formats (`{{key:▸θ,r}}`, `{{key:▸HR}}`, `{{key:▸DEG}}`).
* **Right Shift (`{{key:↱}}` — Modal Workspaces, Solvers & Softkey Menus):** Tapping `{{key:↱}}` elevates that key from a single calculation into a broader analytical workspace or specialized operator printed above the upper-right corner. On the top rows, `{{key:↱}}` opens the context-sensitive softkey menus associated with each key's domain (`PARTS` above `{{key:√x}}`, `PROB` above `{{key:eˣ}}`, `L.R.` above `{{key:LN}}`, `x̄,ȳ` above `{{key:yˣ}}`, `s,σ` above `{{key:1/x}}`, and `SUMS` above `{{key:Σ+}}`). Elsewhere on the keypad, `{{key:↱}}` launches the high-level numerical engines (`{{key:POLY}}`, `{{key:SOLVE}}`, `{{key:∫}}`, `{{key:PLOT}}`, `EQN`), invokes specialized operators (`π`, `{{key:%}}`, `{{key:%CHG}}`, `{{key:ABS}}`, `{{key:÷R}}`, `{{key:SHOW}}`), or converts metric values **into US/Imperial units** (`{{key:▸mi}}`, `{{key:▸lb}}`, `{{key:▸°F}}`, `{{key:▸in}}`, `{{key:▸gal}}`) and rectangular/sexagesimal formats (`{{key:▸y,x}}`, `{{key:▸HMS}}`, `{{key:▸RAD}}`).
* **Alpha Labels (`A`–`Z`, `i`, `(i)`):** Printed to the lower-right of the main keys, the 26 alphabetical register labels (`A` through `Z`) plus the indirect-addressing indicators `i` and `(i)` activate **automatically** whenever a command prompts for a register or program label—such as after pressing `{{key:STO}}`, `{{key:RCL}}`, `{{key:XEQ}}`, `FN=`, `LBL`, `{{key:SOLVE}}`, or `{{key:∫}}`. You never need to toggle an awkward alpha-lock mode just to store a physical constant in Register `G` or solve an equation for variable `T`.

### Upper Function Zone (Rows 0–2, 6 Columns)

The top three rows of the keypad form a compact 6-column scientific command deck positioned directly beneath the transflective display so your eyes can scan the stack and the top keys in a single field of view. **Row 0** (`{{key:LFU0}}` through `{{key:LFU5}}`) acts as a live, context-sensitive **softkey strip**: whenever you open a menu such as `PARTS`, `PROB`, `L.R.`, `BASE`, `MODES`, `DISP`, `FLAGS`, `TVM`, or `POLY`, up to six labeled pills appear along the bottom pixel row of the LCD directly above these six physical keys. Pressing any `{{key:LFU0}}`–`{{key:LFU5}}` button executes the corresponding on-screen command in a single tap without ever hiding the active stack registers.

Immediately below the softkey bar, **Row 1** (`{{key:√x}}`, `{{key:eˣ}}`, `{{key:LN}}`, `{{key:yˣ}}`, `{{key:1/x}}`, `{{key:Σ+}}`) groups every power, root, exponential, logarithmic, reciprocal, and statistical accumulation operator along a single horizontal ridge where your index finger naturally rests. Five of these keys (`{{key:√x}}`, `{{key:eˣ}}`, `{{key:LN}}`, `{{key:1/x}}`, and their `{{key:↰}}` companions `{{key:x²}}`, `{{key:10ˣ}}`, `{{key:LOG}}`, `{{key:x!}}`) are immediate unary transformations that replace $X$ in place while preserving $Y, Z, T$, whereas `{{key:yˣ}}` and `{{key:ˣ√y}}` combine $Y$ and $X$ dyadically ($Y^X$ and $Y^{1/X}$). At the right end of Row 1, `{{key:Σ+}}` (and `{{key:Σ-}}`) feeds $(x, y)$ data pairs into the six statistical accumulators while updating $X$ with the sample count $n$ and disarming stack lift. Notice how the right shifts (`{{key:↱}}`) across Row 1 turn those six keys into a complete statistical and number-theory toolbar: `PARTS`, `PROB`, `L.R.`, `x̄,ȳ`, `s,σ`, and `SUMS`.

**Row 2** (`{{key:STO}}`, `{{key:RCL}}`, `{{key:R↓}}`, `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`) pairs named register management and stack rotation on the left with planar trigonometry on the right. Pressing `{{key:STO}}` or `{{key:RCL}}` followed by any letter key `A`–`Z` stores or recalls a value, and inserting `+`, `-`, `×`, or `÷` before the letter performs non-destructive **Storage or Recall Arithmetic** without cluttering the stack. Their shifted legends unlock two cornerstone workspaces: Left Shift `{{key:↰}}` above `{{key:STO}}` (`CMPLX`) arms the four-register Gaussian complex phasor engine on $(Y, X)$ and $(T, Z)$, while Right Shift `{{key:↱}}` above `{{key:STO}}` (`EQN`) opens the symbolic Equation Bank. Next door, `{{key:R↓}}` and `{{key:R↑}}` (Right Shift `{{key:↱}}` above `{{key:R↓}}`) rotate all four stack registers circularly so you can inspect or reposition any intermediate value, while Left Shift `{{key:↰}}` above `{{key:R↓}}` (`{{key:HYP}}`) serves as the hyperbolic prefix for `{{key:SIN}}`, `{{key:COS}}`, and `{{key:TAN}}` (and their `{{key:↰}}` inverse functions). Finally, the right shifts of the three trig keys place $\pi$ (`{{key:SIN}}`), Kahan's base-preserving percentage `{{key:%}}` (`{{key:COS}}`), and percent change `{{key:%CHG}}` (`{{key:TAN}}`) within instant thumb reach.

| Row | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 0** | `{{key:LFU0}}` | `{{key:LFU1}}` | `{{key:LFU2}}` | `{{key:LFU3}}` | `{{key:LFU4}}` | `{{key:LFU5}}` |
| **Row 1** | `{{key:√x}}` | `{{key:eˣ}}` | `{{key:LN}}` | `{{key:yˣ}}` | `{{key:1/x}}` | `{{key:Σ+}}` |
| **Row 2** | `{{key:STO}}` | `{{key:RCL}}` | `{{key:R↓}}` | `{{key:SIN}}` | `{{key:COS}}` | `{{key:TAN}}` |

### Transition Zone (Row 3)

Row 3 forms the structural and ergonomic bridge between the upper scientific function array and the lower number pad. Anchoring Columns 0 and 1 is the signature double-wide **`{{key:ENTER}}`** bar—the physical fulcrum of Reverse Polish Notation. When you finish typing the first number of a dyadic pair, pressing `{{key:ENTER}}` terminates digit entry, pushes a copy of $X$ up into $Y$ ($T \leftarrow Z, Z \leftarrow Y, Y \leftarrow X$), and deliberately **disables stack lift** so the next number you type cleanly overwrites $X$ in place. Its Left/Right Shift legends above `{{key:ENTER}}` are equally vital: Left Shift `{{key:↰}}` above `{{key:ENTER}}` (`{{key:LASTX}}`) recalls the exact value that was in Register $X$ before the last mathematical operation—allowing instant error recovery or reuse of a shared argument—while Right Shift `{{key:↱}}` above `{{key:ENTER}}` (`{{key:SHOW}}`) temporarily reveals the full 15-digit internal mantissa and exponent of Register $X$ without altering your active `FIX`, `SCI`, or `ENG` display setting.

Immediately to the right of `{{key:ENTER}}` sits **`{{key:x⇄y}}`** (`Row 3, Col 2`), the register-exchange key that gives RPN its algebraic freedom. Whenever you evaluate a complex denominator or subtrahend *first* and then push the numerator or minuend onto the stack, a single tap of `{{key:x⇄y}}` swaps $X$ and $Y$ so `{{key:÷}}`, `{{key:-}}`, or `{{key:yˣ}}` executes in the proper order with zero parentheses; its shifts inspect available memory (`{{key:↰}}` `MEM`) or swap $X$ with any letter register (`{{key:x⇄?}}`). Beside it, **`{{key:+/-}}`** (`Row 3, Col 3`) toggles the sign of the number currently in $X$—or negates the power-of-ten exponent if pressed after `{{key:E}}`—while hosting the angular/radix `MODES` menu on `{{key:↰}}` and direct absolute value `{{key:ABS}}` ($|x|$) on `{{key:↱}}`.

Completing the transition bridge are **`{{key:E}}`** (`Row 3, Col 4`) and **`{{key:<-}}`** (`Row 3, Col 5`). Pressing `{{key:E}}` during number entry transitions from the mantissa to the base-10 exponent ($m \times 10^n$) so you can key physical constants like Planck's constant or Avogadro's number without multiplying by $10^x$; its left shift opens the `DISP` precision menu (`FIX`, `SCI`, `ENG`, `ALL`), and its right shift executes Euclidean integer division with remainder (`{{key:÷R}}`), placing the quotient $\lfloor Y/X \rfloor$ in $X$ and the remainder in $Y$. At the far right, the backspace key **`{{key:<-}}`** adapts to your state: while you are actively typing digits, it erases one character at a time from the right; once a number is finalized on the stack, pressing `{{key:<-}}` acts as `CLx`, zeroing Register $X$ and disabling stack lift without dropping $Y, Z,$ or $T$, while Left Shift `{{key:↰}}` above `{{key:<-}}` opens the selective `CLEAR` menu.

| Row | Col 0 & 1 (Double-Wide) | Col 2 | Col 3 | Col 4 | Col 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 3** | `{{key:ENTER}}` | `{{key:x⇄y}}` | `{{key:+/-}}` | `{{key:E}}` | `{{key:<-}}` |

### Lower Arithmetic Zone (Rows 4–7, 5 Columns)

The lower four rows widen into a generous 5-column pitch engineered for rapid, eyes-free numeric entry and postfix arithmetic. Along the left margin (`Col 0`), four dedicated control keys govern execution and shift state: **`{{key:XEQ}}`** executes stored equations by label (while `{{key:↰}}` `FN=` designates the target equation for solving/integrating and `{{key:↱}}` `POLY` opens the quadratic/cubic root workspace); **`{{key:↰}}`** and **`{{key:↱}}`** act as latching, toggleable left- and right-shift prefixes; and **`{{key:C}}`** (`ON`) wakes the hardware, cancels active prompts, or clears Register $X$ (with `{{key:?}}` for hardware diagnostics and `{{key:↱}}` `OFF` for deep sleep). Along the right margin (`Col 4`), the four foundational dyadic operators—**`{{key:÷}}`**, **`{{key:×}}`**, **`{{key:-}}`**, and **`{{key:+}}`**—fuse $Y$ and $X$ ($Y \div X$, $Y \times X$, $Y - X$, $Y + X$), drop the stack ($Y \leftarrow Z, Z \leftarrow T$), replicate $T$, and leave stack lift armed, while their shifted legends provide relational tests (`x?y`, `x?0`), computer-science integer `BASE` modes and system `FLAGS`, liter/gallon conversions (`{{key:▸l}}`/`{{key:▸gal}}`), and equation labels (`[LBL]`/`[RTN]`).

Across the central `0`–`9` and `.` digit pad (`Cols 1–3`), the shifted legends are organized into four intuitive engineering clusters so you can model physical problems directly on the stack:
* **Calculus, Root-Finding & Plot Navigation (`7` and `8`):** Right-shifting `{{key:7}}` (`{{key:SOLVE}}`) and `{{key:8}}` (`{{key:∫}}`) invokes Richard Brent's root finder and Werner Romberg's adaptive quadrature on the active `FN=` equation using your bounds in $Y$ and $X$, while left-shifting `{{key:7}}` (`{{key:↓}}`) and `{{key:8}}` (`{{key:↑}}`) steps through multi-equation banks or traces plotted curves.
* **2D Vector, Sexagesimal Time & Angular Conversions (`4`, `5`, and `6`):** Key `{{key:4}}` converts between rectangular coordinates $(x, y)$ in $(X, Y)$ and polar phasors $(r, \theta)$ via `{{key:▸θ,r}}` and `{{key:▸y,x}}`. Key `{{key:5}}` translates between `DD.MMSS` sexagesimal angles/timestamps and decimal hours/degrees (`{{key:▸HR}}` $\leftrightarrow$ `{{key:▸HMS}}`), and Key `{{key:6}}` converts between radians and degrees (`{{key:▸DEG}}` $\leftrightarrow$ `{{key:▸RAD}}`).
* **Physical SI $\leftrightarrow$ Imperial Unit Conversions (`9`, `1`, `2`, `3`, and `-`):** Every paired conversion puts the **metric unit on `{{key:↰}}`** and the **imperial unit on `{{key:↱}}`**: distance on `{{key:9}}` (`{{key:▸km}}` $\leftrightarrow$ `{{key:▸mi}}`), mass on `{{key:1}}` (`{{key:▸kg}}` $\leftrightarrow$ `{{key:▸lb}}`), temperature on `{{key:2}}` (`{{key:▸°C}}` $\leftrightarrow$ `{{key:▸°F}}`), length on `{{key:3}}` (`{{key:▸cm}}` $\leftrightarrow$ `{{key:▸in}}`), and fluid volume on `{{key:-}}` (`{{key:▸l}}` $\leftrightarrow$ `{{key:▸gal}}`).
* **Register Inspection, Indirect Addressing (`i`, `(i)`), Relational Tests (`x?y`, `x?0`) & the Harmonic Hub (`0`, `.`, `x∥y`, `÷`):** Key `{{key:0}}` opens the full-screen `REGS` table (`{{key:↰}}`) or single-register `VIEW` (`{{key:↱}}`), while the radix point `{{key:.}}` toggles exact fraction display `{{key:FDISP}}` (`{{key:↰}}`), sets the maximum denominator `/c` (`{{key:↱}}`), and carries the Alpha label **`i`** (the index register). At `Row 7, Col 3` sits the SC-32's signature **`{{key:x∥y}}`** key: a single unshifted tap evaluates the parallel harmonic product $\frac{Y \times X}{Y + X}$; Left/Right Shift above `{{key:x∥y}}` launches the 5-variable **`TVM`** financial solver (`N`, `I%`, `PV`, `PMT`, `FV` on Left Shift `{{key:↰}}` above `{{key:x∥y}}`) and opens the 64-column **`PLOT`** graphing engine (on Right Shift `{{key:↱}}` above `{{key:x∥y}}`); and its Alpha label **`(i)`** dereferences the integer pointer in `i` across all 89 slots of the memory map (`1`–`26` = `A`–`Z`, `27` = `i`, `28`–`33` = statistical sums, `34`–`39` = `POLY` roots, `40`–`89` = raw statistical data points). Meanwhile, the division key **`{{key:÷}}`** (`Row 4, Col 4`) hosts the two six-operator relational comparison menus **`{{key:x?y}}`** (`{{key:↰}}`) and **`{{key:x?0}}`** (`{{key:↱}}`), which flash `YES`/`NO` non-destructively on the live stack and act as $1/0$ Iverson Boolean indicator switches inside `{{key:EQN}}` to model piecewise functions.

| Row | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 4** | `{{key:XEQ}}` | `{{key:7}}` | `{{key:8}}` | `{{key:9}}` | `{{key:÷}}` |
| **Row 5** | `{{key:↰}}` (Left Shift) | `{{key:4}}` | `{{key:5}}` | `{{key:6}}` | `{{key:×}}` |
| **Row 6** | `{{key:↱}}` (Right Shift) | `{{key:1}}` | `{{key:2}}` | `{{key:3}}` | `{{key:-}}` |
| **Row 7** | `{{key:C}}` (ON) | `{{key:0}}` | `{{key:.}}` | `{{key:x∥y}}` | `{{key:+}}` |

### The Definitive 43-Key Directory & Chapter Index

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
| **29**| R5, C0 | `{{key:↰}}` (Left Shift)| *(Left Shift Latch)* | *(Left Shift Latch)* | — | [Physical Keypad Layout](#physical-keypad-layout-functional-guide-to-the-43-buttons) • Primary Left Shift prefix |
| **30**| R5, C1 | `{{key:4}}` | `{{key:▸θ,r}}` Polar | `{{key:▸y,x}}` Rect | `T` | [Ch 2: Digit Entry](02-rpn-stack-dynamics.md) • [Ch 4: Polar & Rectangular Vectors](04-trig-vectors-polar.md) |
| **31**| R5, C2 | `{{key:5}}` | `{{key:▸HR}}` Hours | `{{key:▸HMS}}` Time | `U` | [Ch 2: Digit Entry](02-rpn-stack-dynamics.md) • [Ch 4: Sexagesimal Angles & Time](04-trig-vectors-polar.md) |
| **32**| R5, C3 | `{{key:6}}` | `{{key:▸DEG}}` Angle | `{{key:▸RAD}}` Angle | `V` | [Ch 2: Digit Entry](02-rpn-stack-dynamics.md) • [Ch 4: Angular Conversions](04-trig-vectors-polar.md) |
| **33**| R5, C4 | `{{key:×}}` | `BASE` Menu | `FLAGS` Menu | — | [Ch 2: Multiplication & System Flags](02-rpn-stack-dynamics.md) • [Ch 10: Radix Bases](10-computer-science-bases.md) • [Ch 14: INF Stack & EXAM Mode](14-uil-contest-playbook.md) |
| **34**| R6, C0 | `{{key:↱}}` (Right Shift)| *(Right Shift Latch)* | *(Right Shift Latch)* | — | [Physical Keypad Layout](#physical-keypad-layout-functional-guide-to-the-43-buttons) • Secondary Right Shift prefix |
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

## Architectural Refinements, Dynamic LFU Menus & Complete HP-32SII / HP-15C / HP-12C Comparison

Every decision on the SC-32 keypad is governed by **the Dvorak Principle applied to calculators**: *whereas smartphones, computer terminals, and menu-driven graphing calculators bury operations inside nested menu trees that nobody can memorize, ninety-nine percent of your daily scientific and engineering work on a handheld instrument should require zero menus.* Every high-frequency operation belongs directly under your fingertips as a tactile keystroke.

### Why the HP-32SII Was Chosen Over the HP-15C (And How HP-15C & HP-12C DNA Are Integrated)

Among vintage Hewlett-Packard collectors, the horizontal 1982 **HP-15C Voyager** is often celebrated as the pinnacle of classic RPN calculators, while the 1981 **HP-12C Voyager** remains the undisputed standard of financial computing. Why, then, did we select the 1991 **HP-32SII Pioneer** as the primary structural template for the StackCalc SC-32—and then fold the flagship analytical engines of the HP-15C and HP-12C into that Pioneer layout?

When evaluated as an everyday scientific instrument rather than a museum artifact, the 1991 **HP-32SII Pioneer** holds four decisive advantages over the 1982 **HP-15C**:

1. **One-Handed Portrait Ergonomics:** The HP-15C's wide landscape frame requires two hands (or flat desk placement), whereas the HP-32SII's portrait Pioneer geometry lets your thumb reach every digit, `{{key:ENTER}}`, and arithmetic operator one-handed while your other hand holds a test probe or pencil.
2. **Named Alpha Variables (`A`–`Z`) Instead of Numbered Registers (`R0`–`R9`):** Because the HP-15C had a 7-segment numeric LCD incapable of rendering letters, variables had to be stored in numbered registers (`R0`–`R9`, `.0`–`.9`). The HP-32SII introduced 26 automatic letter registers (`A` through `Z`) so physical formulas ($P, V, n, R, T$) map directly to their textbook symbols.
3. **Readable Symbolic Equations (`EQN`) Instead of Blind Keystroke Subroutines (`LBL 0..9`):** On the HP-15C, `SOLVE` and `∫f(x)` required programming a blind keystroke subroutine (`001- 43 21 0`) under a numbered label. The HP-32SII introduced a symbolic **Equation Bank (`EQN`)** where formulas remain human-readable on screen.
4. **Ten Physical SI $\leftrightarrow$ Imperial Unit Conversions & Native Fractions:** The HP-15C had neither physical unit conversions nor fraction arithmetic. The HP-32SII placed ten direct unit conversions right on the digit keys (`{{key:↰}}` for Metric, `{{key:↱}}` for Imperial) alongside exact rational fractions (`{{key:FDISP}}`, `{{key:/c}}`).

The SC-32 takes that HP-32SII Pioneer foundation, cures its 1-line display keyhole and infix-equation quirk, and integrates the best features of the **HP-15C** and **HP-12C** onto direct shifted keys:

| Architectural Dimension | HP-12C Voyager (1981) | HP-15C Voyager (1982) | HP-32SII Pioneer (1991) | StackCalc SC-32 |
| :--- | :--- | :--- | :--- | :--- |
| **Form Factor & Ergonomics** | Landscape (two-handed) | Landscape (two-handed) | Portrait (one-handed thumb arc) | **Portrait 43-key Pioneer geometry** (one-handed thumb arc) |
| **Display & Stack Visibility** | 1-line, 10-digit 7-seg (`X` only) | 1-line, 10-digit 7-seg (`X` only) | 1-line, 12-char dot-matrix (`X` only) | **4-line $132 \times 65$ transflective LCD** ($T, Z, Y, X$ visible simultaneously) |
| **Softkey Menu Bar** | None | None | Hijacks top row (`√x`..`Σ+`) with 1-line text | **Dedicated 6-key Dynamic LFU Bar (`{{key:LFU0}}`–`{{key:LFU5}}`)** above `√x`..`Σ+` |
| **Operational Stack Depth** | 4-level ($X, Y, Z, T$) | 4-level ($X, Y, Z, T$) | 4-level ($X, Y, Z, T$) | **Selectable `{{key:4-LVL}}` (classic Corvallis), `{{key:8-LVL}}`, or `{{key:INF}}` (999-level LIFO)** |
| **Storage Registers** | `R0`–`R9`, `.0`–`.9` (numbered) | `R0`–`R9`, `.0`–`.9`, `I` (numbered) | `A`–`Z` (26 named letters) + `i`, `(i)` | **`A`–`Z` (26 named letters) + `i`, `(i)` across 89 indirect slots (`R1`–`R89`)** |
| **Equation Bank (`EQN`)** | None (keystroke `R/S` only) | None (keystroke `LBL 0..9` only) | Split personality: Infix `EQN` (`(`, `)`, `=`) | **100% Pure RPN `{{key:EQN}}` Bank** with Iverson Boolean `[x?0]`/`[x?y]` piecewise switches |
| **Root Finder & Calculus** | `IRR` / `NPV` cash-flow only | Brent `SOLVE` & Romberg `∫f(x)` via `LBL` | Brent `SOLVE` & Romberg `∫` via `EQN` | **Brent `{{key:SOLVE}}` & Romberg `{{key:∫}}` via `{{key:EQN}}` + Dedicated Analytic `{{key:POLY}}` (`R34`–`R39`)** |
| **Complex Numbers (`CMPLX`)** | None | Parallel complex stack via `I` / `Re⇄Im` | 4-register $(Y, X)$ & $(T, Z)$ via `CMPLX` prefix | **4-register $(Y, X)$ & $(T, Z)$ via `{{key:CMPLX}}` prefix (including complex `{{key:x∥y}}` & `{{key:POLY}}` roots)** |
| **Time Value of Money (`TVM`)** | Dedicated `n`, `i`, `PV`, `PMT`, `FV` keys | None | None (requires manual keystroke program) | **Built-in 5-Variable `{{key:TVM}}` (`N`, `I%`, `PV`, `PMT`, `FV`, `END/BEG`) on Left Shift `{{key:↰}}` above `{{key:x∥y}}`** |
| **Physical Unit Conversions** | None | `→H.MS`, `→RAD` only | 10 SI $\leftrightarrow$ US keys + polar/HMS/angle | **All 10 SI (`{{key:↰}}`) $\leftrightarrow$ US (`{{key:↱}}`) keys + polar/HMS/angle (`4`, `5`, `6`)** |
| **Exact Fractions & Number Theory** | None | None | `a b/c`, `FDISP`, `/c` | **Exact fractions (`{{key:FDISP}}`, `{{key:/c}}`) + physical `{{key:÷R}}` + `{{key:GCD}}` & `{{key:LCM}}` in `PARTS`** |
| **Parallel / Harmonic Operator** | None | None | None | **Dedicated unshifted `{{key:x∥y}}` key ($\frac{Y \times X}{Y + X}$ for resistors, lenses, capacitors)** |
| **Graphical Plotting & Exam Mode** | None | None | None | **64-column `{{key:PLOT}}` function/scatter canvas (Right Shift `{{key:↱}}` above `{{key:x∥y}}`) + proctored `{{key:EXAM}}` lockdown** |

### Complete Key-by-Key & Shifted-Legend Differences: HP-32SII vs. SC-32

Every primary key, left shift (`{{key:↰}}`, corresponding to the HP-32SII orange shift), right shift (`{{key:↱}}`, corresponding to the HP-32SII blue shift), and alpha legend on the SC-32 matches the 1991 HP-32SII **except** where the SC-32 eliminates legacy infix/keystroke-program boilerplate or adds direct scientific/financial capabilities. The table below documents every single keypad difference:

| Matrix Pos | Key Face (SC-32 vs. HP-32SII) | Left Shift `{{key:↰}}` (SC-32 vs. HP-32SII) | Right Shift `{{key:↱}}` (SC-32 vs. HP-32SII) | Engineering Rationale for the SC-32 Design |
| :---: | :--- | :--- | :--- | :--- |
| **R0, C0–C5** | **`{{key:LFU0}}`–`{{key:LFU5}}`** *(New dedicated row)* | Context softkeys | Context softkeys | Adds 6 dedicated physical softkeys beneath the 4-line LCD so menus never hijack `{{key:√x}}`..`{{key:Σ+}}` (`Row 1`). |
| **R2, C0** | `{{key:STO}}` *(Same)* | `CMPLX` *(Same)* | **`EQN`** *(HP-32SII: unshifted key on R4C0)* | Frees `R4C0` for dedicated `{{key:XEQ}}` / `FN=` / `{{key:POLY}}` while grouping `{{key:STO}}`, `CMPLX`, and `EQN` on one memory/model key. |
| **R2, C1** | `{{key:RCL}}` *(Same)* | **`{{key:RND}}`** *(HP-32SII: inside `PARTS` menu)* | **`[SCRL]`** *(HP-32SII: `MEM`)* | Promotes display-precision rounding (`{{key:RND}}`) out of the `PARTS` submenu onto a 1-shift key, and adds horizontal equation/plot scrolling (`[SCRL]`). |
| **R3, C2** | `{{key:x⇄y}}` *(Same)* | **`MEM`** *(HP-32SII: `x⇄?`)* | **`[x⇄?]`** *(HP-32SII: `K` constant)* | Places `MEM` inspection on `{{key:↰}}` and register swap `[x⇄?]` on `{{key:↱}}`. |
| **R3, C3** | `{{key:+/-}}` *(Same)* | `MODES` *(Same)* | **`{{key:ABS}}` (`\|x\|`)** *(HP-32SII: `(` open paren)* | Pure RPN equations need no infix `(`; promotes Absolute Value (`\|x\|`) from the `PARTS` submenu to a direct keystroke. |
| **R3, C4** | `{{key:E}}` *(Same)* | `DISP` *(Same)* | **`{{key:÷R}}`** *(HP-32SII: `)` close paren)* | Pure RPN equations need no infix `)`; adds Euclidean integer quotient-remainder division ($Y \div X \to Q$ in $X$, $R$ in $Y$). |
| **R3, C5** | `{{key:<-}}` *(Same)* | `CLEAR` *(Same)* | ***(Unassigned)*** *(HP-32SII: `=` equals)* | Relational `=` lives cleanly in `x?y` / `x?0`; leaving Right Shift `{{key:↱}}` above `{{key:<-}}` unassigned prevents accidental clears during fast entry. |
| **R4, C0** | **`{{key:XEQ}}`** *(HP-32SII: `EQN`)* | **`FN=`** *(HP-32SII: `XEQ`)* | **`{{key:POLY}}`** *(HP-32SII: `FN=`)* | Makes `{{key:XEQ}}` a 1-tap primary key, keeps `FN=` on `{{key:↰}}`, and adds the analytic quadratic/cubic `{{key:POLY}}` root solver on `{{key:↱}}`. |
| **R4, C1** | `{{key:7}}` *(Same)* | **`{{key:↓}}`** *(HP-32SII: `DSE` loop)* | `{{key:SOLVE}}` *(Same)* | Replaces legacy keystroke-loop `DSE` with direct downward cursor/trace navigation (`{{key:↓}}`) for `EQN`, `REGS`, and `PLOT`. |
| **R4, C2** | `{{key:8}}` *(Same)* | **`{{key:↑}}`** *(HP-32SII: `ISG` loop)* | `{{key:∫}}` *(Same)* | Replaces legacy keystroke-loop `ISG` with direct upward cursor/trace navigation (`{{key:↑}}`) for `EQN`, `REGS`, and `PLOT`. |
| **R7, C0** | `{{key:C}}` (`ON`) *(Same)* | **`{{key:?}}`** *(HP-32SII: blank)* | `OFF` *(Same)* | Adds instant system status and self-test diagnostics (`{{key:?}}`) on Left Shift `{{key:↰}}` above `{{key:C}}`. |
| **R7, C1** | `{{key:0}}` *(Same)* | **`REGS`** *(HP-32SII: `INPUT`)* | `VIEW` *(Same)* | Replaces line-program `INPUT` with the full-screen `REGS` register browser (`A`–`Z`, `i`) while keeping single-register `VIEW` on `{{key:↱}}`. |
| **R7, C3** | **`{{key:x∥y}}`** *(HP-32SII: `R/S`)* | **`TVM`** *(HP-32SII: `GTO`)* | **`PLOT`** *(HP-32SII: `RTN`)* | Replaces `R/S` and `GTO` with the universal parallel operator `{{key:x∥y}}`, the HP-12C `TVM` financial solver, and the 64-column `PLOT` canvas (preserving Alpha `(i)`). |
| **R7, C4** | `{{key:+}}` *(Same)* | **`[LBL]`** *(HP-32SII: `x²` / `LBL`)* | **`[RTN]`** *(HP-32SII: `√x`)* | Places equation label `[LBL]` and return `[RTN]` cleanly on `{{key:+}}` while keeping `{{key:√x}}` and `{{key:x²}}` paired on `R1C0`. |

### Menu, Equation, Stack-Depth & Memory-Map Enhancements

Beyond the physical keycap legends, the SC-32 expands five internal subsystems while preserving 100% compatibility with classic HP-32SII workflows:

* **Upgraded `PARTS` Menu (Right Shift `{{key:↱}}` above `{{key:√x}}`):** Because `{{key:RND}}` (Left Shift `{{key:↰}}` above `{{key:RCL}}`) and `{{key:ABS}}` (Right Shift `{{key:↱}}` above `{{key:+/-}}`) are promoted to physical keys, the 6-key `PARTS` menu (`{{key:IP}}`, `{{key:FP}}`, `{{key:ABS}}`, `{{key:SGN}}`, `{{key:GCD}}`, `{{key:LCM}}`) retains `ABS` for muscle-memory convenience while adding the Signum function (`{{key:SGN}}`: $-1, 0, +1$), Euclidean Greatest Common Divisor (`{{key:GCD}}`), and Least Common Multiple (`{{key:LCM}}`).
* **Pure RPN Equations & Iverson Piecewise Booleans (`{{key:EQN}}`):** Instead of forcing algebraic infix entry inside `EQN` mode, the SC-32 evaluates equations as pure RPN token streams. Any relational test from `{{key:x?y}}` (Left Shift `{{key:↰}}` above `{{key:÷}}`) or `{{key:x?0}}` (Right Shift `{{key:↱}}` above `{{key:÷}}`) inserted into an equation acts as a non-destructive **Iverson bracket $[P] \in \{1, 0\}$** on Register $X$ (preserving $Y$ and $Z$), enabling branchless piecewise formulas for `{{key:XEQ}}`, `{{key:SOLVE}}`, `{{key:∫}}`, and `{{key:PLOT}}`.
* **Configurable Stack Depth (`4-LVL`, `8-LVL`, `INF`) & Proctored `EXAM` Mode (Right Shift `{{key:↱}}` above `{{key:×}}`):** The `FLAGS` menu preserves user Flags `0`–`9` (`SF`, `CF`, `FS?`) and adds the `STACK` submenu (`2-LVL`, `4-LVL`, `8-LVL`, `INF`, `VIEW`) plus `EXAM` mode. Default `4-LVL` mode preserves exact Corvallis 4-register physics (including top-of-stack $T$-replication on drop), while `8-LVL` and `INF` (999-level LIFO) eliminate register overflow during deeply nested evaluations.
* **36-Bit Signed Two's-Complement `BASE` Arithmetic (Left Shift `{{key:↰}}` above `{{key:×}}`):** Whereas the HP-32SII truncated base conversions to 32-bit unsigned integers, the SC-32 uses a 36-bit two's-complement integer word across `DEC`, `HEX` (9 nibbles), `OCT` (12 full octal digits), and `BIN`.
* **89-Slot Indirect Memory Map (`i` and `(i)`):** Storing an integer pointer $k \in \{1 \dots 89\}$ in the index register `i` (`STO` `{{key:.}}`) and dereferencing `(i)` (`RCL` `{{key:x∥y}}` or `STO` `{{key:x∥y}}`) addresses:
  * `1`–`26`: Named variables `A` through `Z` (`1 = A`, `2 = B`, $\dots$, `26 = Z`).
  * `27`: The index register `i` itself.
  * `28`–`33`: Live statistical accumulators ($n, \sum x, \sum y, \sum x^2, \sum y^2, \sum xy$).
  * `34`–`39`: Analytic polynomial roots from `{{key:POLY}}` ($\text{Re}(r_1), \text{Im}(r_1), \text{Re}(r_2), \text{Im}(r_2), \text{Re}(r_3), \text{Im}(r_3)$).
  * `40`–`89`: Up to 25 raw statistical data pairs $(x_k, y_k)$ accumulated via `{{key:Σ+}}` for scatter plotting (`{{key:PLOT}}`).

### Dynamic LFU Softkey Menus Directory

The six top keys (`{{key:LFU0}}` through `{{key:LFU5}}`) automatically remap depending on the active menu state:

| Menu | LFU0 | LFU1 | LFU2 | LFU3 | LFU4 | LFU5 |
|:---|:---|:---|:---|:---|:---|:---|
| DISP | FIX n | SCI n | ENG n | ALL | (None) | (None) |
| MODES | DEG | RAD | GRAD | . | , | (None) |
| BASE | HEX | DEC | OCT | BIN | (None) | (None) |
| CLEAR | CLEQN | CLVARS | CLALL | CLSTAT (CLΣ) | CLREGS | CLSTK |
| FLAGS | SF n | CF n | FS? n | STACK | EXAM | (More ▸) |
| STACK | 2-LVL | 4-LVL | 8-LVL | INF | VIEW | (None) |
| PARTS | IP | FP | ABS | SGN | GCD | LCM |
| PROB | C n, r | P n, r | x! | RAND | SD | (None) |
| SUMS | Σx | Σy | Σx² | Σy² | Σxy | n |
| x̄,ȳ | x̄ | ȳ | x̄w | (None) | (None) | (None) |
| s,σ | sx | sy | σx | σy | (None) | (None) |
| L.R. | ŷ | x̂ | r | m | b | (None) |
| x?y | x=y | x≠y | x>y | x<y | x≥y | x≤y |
| x?0 | x=0 | x≠0 | x>0 | x<0 | x≥0 | x≤0 |
| TVM | N | I% | PV | PMT | FV | END/BEG |
| POLY | A | B | C | D | EXEC | CLR |
| PLOT (Nav) | `<` | `\|<-` | OUT | IN | `->\|` | `>` |
| PLOT (Opt) | MARK | CLEAR | STORE | ∫ f(x) | (None) | (None) |
| REGS | STACK | STO | STATS | DATA | ▲ | ▼ |

---

## How We Built StackCalc: An Open-Source Engineering Story

Rather than printing pages of static component datasheets in this book, we document the live hardware evolution on **[stackcalc.io/hardware](https://stackcalc.io/hardware)** and in our public engineering build logs on **[Hackaday](https://hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator)**. For students, makers, and working engineers curious about how a modern scientific instrument is conceived, simulated, and manufactured from scratch, here is the story of how StackCalc came to life.

### From a Wristwatch Screen to a Unified Mathematical Engine
StackCalc began with a simple human-factors observation on the tiny screen of a wristwatch: on a $40\text{ mm}$ wrist display, algebraic parentheses and scrolling formula bars are nearly impossible to type accurately, whereas Reverse Polish Notation needs only a clean number pad, `{{key:ENTER}}`, and immediate operators. What started as a pocket and wrist companion for engineers soon revealed a deeper architectural challenge.

A calculator can look visually identical across a wristwatch, a smartphone, a desktop browser, and a physical handheld while subtly disagreeing at the exact edge cases that matter most to a serious user: how `{{key:ENTER}}` disarms stack lift, how an interrupted digit entry interacts with `{{key:x⇄y}}`, how `{{key:LASTX}}` behaves after a unary versus a dyadic operator, or how the stack recovers when an operation hits $\tan(90^\circ)$ or $\ln(0)$. To guarantee that every surface behaves as one mathematical mind, we built a single deterministic state machine at the heart of the project. Whether a keypress originates from a touchscreen tap, a desktop keyboard shortcut, or a physical row-and-column switch contact on the handheld PCB, it steps the exact same four-register automaton before a single pixel is drawn.

### Mathematical Rigor in Silicon: Lanczos, Brent, and Romberg
Building an honest scientific instrument means refusing to take numerical shortcuts. Early in development, we committed that every transcendental function, statistical estimator, root solver, and definite integral on the SC-32 would use classic, peer-reviewed algorithms from the golden age of numerical analysis:

* **Continuous Factorials via Cornelius Lanczos's Gamma Approximation:** Rather than limiting `{{key:x!}}` to a lookup table of whole numbers, the engine evaluates $\Gamma(x+1)$ across the real line using Cornelius Lanczos's Chebyshev rational approximation paired with Euler's reflection formula $\Gamma(z)\Gamma(1-z) = \frac{\pi}{\sin(\pi z)}$, maintaining 15-digit internal precision from fractional half-integers up to $170! \approx 7.2574 \times 10^{306}$.
* **Guaranteed Root-Finding via Richard Brent's Hybrid Algorithm:** Pure Newton–Raphson iteration can fly off to infinity when a curve flattens near a local extremum, while pure bisection crawls at one binary bit per step. Our `{{key:SOLVE}}` engine implements Richard Brent's 1973 hybrid method, which races ahead with inverse quadratic and secant interpolation whenever the curve is well-behaved, yet automatically falls back to a bisection step the instant an iterate threatens to step outside the bracket $[a, b]$ or stall.
* **Adaptive Calculus via Werner Romberg's Richardson Tableau:** When you press `{{key:∫}}`, the calculator does not merely sum crude rectangles. It constructs a triangular Romberg tableau, halving the trapezoidal step size and applying Lewis Fry Richardson's $\frac{4^m T_{k,m-1} - T_{k-1,m-1}}{4^m - 1}$ error-cancellation cascade to strip away successive powers of $h^2, h^4, h^6$ until the integral converges to machine tolerance.

Every one of these numerical engines—alongside William Kahan's compensated summation and base-preserving percentages, Gaussian complex phasor arithmetic, and 36-bit two's-complement word operations—is continuously checked against tens of thousands of reference mathematical vectors so that the numbers on the screen match the equations in this book to the last decimal place.

### Four-Layer Gold-Immersion Hardware, Daylight Optics & Tactile Key-Feel
Translating that software engine into a physical pocket observatory required co-designing electronics, optics, and mechanics as a single sculpture:

* **Four-Layer ENIG Circuit Architecture & Continuous Memory:** The custom four-layer printed circuit board uses an electroless nickel immersion gold (ENIG) surface finish across its switch matrix pads for corrosion-free contact longevity over hundreds of thousands of actuations. Whenever the instrument naps between calculations, it writes atomic, checksum-verified state snapshots—preserving all four stack registers ($T, Z, Y, X$), `LASTX`, the 26 letter registers (`A`–`Z`), all six statistical accumulators, TVM financial registers, and the 24-slot Equation Bank—into alternating non-volatile memory banks so your work is never lost.
* **Reflective Daylight Readability & Tactile Snap-Dome Acoustics:** Instead of a power-hungry smartphone screen that washes out in sunlight and demands nightly charging, the SC-32 pairs a crisp $132 \times 65$ transflective liquid-crystal display with a brushed-aluminum faceplate. Ambient light passes through the liquid-crystal layer and reflects off the internal metallic mirror, growing sharper as the room gets brighter, while precision stainless-steel snap domes beneath the 43 sculpted keycaps deliver a crisp tactile break so your fingertips know a digit has registered before your eyes leave the page.
* **Simulating Silicon & Board-Aware Parametric CAD:** While the four-layer boards were in fabrication, we wired a browser-based hardware simulator directly to a cycle-accurate microcontroller emulator to verify matrix debouncing, sleep wake-up timing, and pixel typography before the first physical board arrived at the bench. As chronicled in our Hackaday engineering logs, our parametric OpenSCAD enclosure scripts read mounting and switch coordinates directly from the KiCad layout—separating mechanical **Guide**, **Capture**, **Stop**, and **Release** geometries so the tapered chassis, faceplate, TPU keypad membrane, and snap-retained cap slide together without a single screw or drop of glue. Complete KiCad schematics, parametric CAD sources, printable `.stl`/`.3mf` files, and firmware build logs are openly published at **[stackcalc.io/downloads](https://stackcalc.io/downloads)** for students, educators, and engineers worldwide. To put these 43 physical keys to work across every major branch of mathematics, physics, engineering, chemistry, and finance, continue to **[Appendix D: Mathematical Constants, SI Units & Master STEM Equation Directory](appendix-d-constants-and-equations.md)**.
