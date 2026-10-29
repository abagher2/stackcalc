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

* **Primary Legend (White Center Label — 1 Tap):** Every key's unshifted tap executes the foundational, highest-frequency operation for that position on the faceplate. These include core transcendental functions (`{{key:√x}}`, `{{key:eˣ}}`, `{{key:LN}}`, `{{key:yˣ}}`, `{{key:1/x}}`, `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`) and statistical accumulation (`{{key:Σ+}}`), alongside stack and memory control (`{{key:STO}}`, `{{key:RCL}}`, `{{key:R↓}}`, `{{key:ENTER}}`, `{{key:x⇄y}}`) and immediate postfix arithmetic (`{{key:÷}}`, `{{key:×}}`, `{{key:-}}`, `{{key:+}}`, `{{key:x∥y}}`).
* **Left Shift (`{{key:↰}}` — Mathematical Inverse or Direct Companion):** Tapping `{{key:↰}}` accesses the natural mathematical inverse or twin printed above the upper-left corner of the key. Once you know where a primary function lives, your finger already knows where its inverse lives: `{{key:√x}}` $\leftrightarrow$ `{{key:x²}}`, `{{key:eˣ}}` $\leftrightarrow$ `{{key:10ˣ}}`, `{{key:LN}}` $\leftrightarrow$ `{{key:LOG}}`, `{{key:yˣ}}` $\leftrightarrow$ `{{key:ˣ√y}}`, `{{key:1/x}}` $\leftrightarrow$ `{{key:x!}}`, `{{key:Σ+}}` $\leftrightarrow$ `{{key:Σ-}}`, `{{key:SIN}}` $\leftrightarrow$ `{{key:ASIN}}`, `{{key:COS}}` $\leftrightarrow$ `{{key:ACOS}}`, `{{key:TAN}}` $\leftrightarrow$ `{{key:ATAN}}`, and `{{key:ENTER}}` $\leftrightarrow$ `{{key:LASTX}}` to recover the pre-operation operand after any function. Across the lower number pad, `{{key:↰}}` consistently converts imperial inputs **into metric (SI) units** (`{{key:▸km}}`, `{{key:▸kg}}`, `{{key:▸°C}}`, `{{key:▸cm}}`, `{{key:▸l}}`) and polar/decimal formats (`{{key:▸θ,r}}`, `{{key:▸HR}}`, `{{key:▸DEG}}`).
* **Right Shift (`{{key:↱}}` — Modal Workspaces, Solvers & Softkey Menus):** Tapping `{{key:↱}}` elevates that key from a single calculation into a broader analytical workspace or specialized operator printed above the upper-right corner. On the top rows, `{{key:↱}}` opens the context-sensitive softkey menus associated with each key's domain: `PARTS` above `{{key:√x}}`, `PROB` above `{{key:eˣ}}`, `L.R.` above `{{key:LN}}`, `x̄,ȳ` above `{{key:yˣ}}`, `s,σ` above `{{key:1/x}}`, and `SUMS` above `{{key:Σ+}}`. Elsewhere on the keypad, `{{key:↱}}` launches the high-level numerical engines (`{{key:POLY}}`, `{{key:SOLVE}}`, `{{key:∫}}`, `{{key:PLOT}}`, `EQN`) and invokes specialized operators (`π`, `{{key:%}}`, `{{key:%CHG}}`, `{{key:ABS}}`, `{{key:÷R}}`, `{{key:SHOW}}`). On the digit pad, `{{key:↱}}` converts metric values **into US/Imperial units** (`{{key:▸mi}}`, `{{key:▸lb}}`, `{{key:▸°F}}`, `{{key:▸in}}`, `{{key:▸gal}}`) and rectangular/sexagesimal formats (`{{key:▸y,x}}`, `{{key:▸HMS}}`, `{{key:▸RAD}}`).
* **Alpha Labels (`A`–`Z`, `i`, `(i)`):** Printed to the lower-right of the main keys, the 26 alphabetical register labels `A` through `Z` plus the indirect-addressing indicators `i` and `(i)` activate **automatically** whenever a command prompts for a register or program label, such as after pressing `{{key:STO}}`, `{{key:RCL}}`, `{{key:XEQ}}`, `FN=`, `LBL`, `{{key:SOLVE}}`, or `{{key:∫}}`. You never need to toggle an awkward alpha-lock mode just to store a physical constant in Register `G` or solve an equation for variable `T`.

### Upper Function Zone (Rows 0–2, 6 Columns)

The top three rows of the keypad form a compact 6-column scientific command deck positioned beneath the transflective display so your eyes can scan the stack and the top keys in a single field of view. **Row 0** (`{{key:LFU0}}` through `{{key:LFU5}}`) is a dedicated, context-aware **LFU (Least Frequently Used) dynamic softkey strip**: in normal state, it dynamically surfaces the six functions tracked by the LFU algorithm, and whenever you open a menu or workspace such as `PARTS`, `PROB`, `L.R.`, `BASE`, `MODES`, `DISP`, `FLAGS`, `TVM`, or `POLY`, it remaps to that menu's softkey labels along the bottom pixel row of the LCD. Pressing any `{{key:LFU0}}`–`{{key:LFU5}}` button executes the corresponding on-screen command in a single tap without hiding the active stack registers or hijacking the fixed scientific keys below.

Below the softkey bar, **Row 1** (`{{key:√x}}`, `{{key:eˣ}}`, `{{key:LN}}`, `{{key:yˣ}}`, `{{key:1/x}}`, `{{key:Σ+}}`) groups every power, root, exponential, logarithmic, reciprocal, and statistical accumulation operator along a single horizontal ridge where your index finger naturally rests. Four of these keys (`{{key:√x}}`, `{{key:eˣ}}`, `{{key:LN}}`, `{{key:1/x}}`) and their `{{key:↰}}` companions (`{{key:x²}}`, `{{key:10ˣ}}`, `{{key:LOG}}`, `{{key:x!}}`) are immediate unary transformations that replace $X$ in place while preserving $Y, Z, T$. By contrast, `{{key:yˣ}}` and `{{key:ˣ√y}}` combine $Y$ and $X$ dyadically as $Y^X$ and $Y^{1/X}$. At the right end of Row 1, `{{key:Σ+}}` and `{{key:Σ-}}` feed $(x, y)$ data pairs into the six statistical accumulators while updating $X$ with the sample count $n$ and disarming stack lift. The right shifts (`{{key:↱}}`) across Row 1 turn those six keys into a complete statistical and number-theory toolbar: `PARTS`, `PROB`, `L.R.`, `x̄,ȳ`, `s,σ`, and `SUMS`.

**Row 2** (`{{key:STO}}`, `{{key:RCL}}`, `{{key:R↓}}`, `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`) pairs named register management and stack rotation on the left with planar trigonometry on the right. Pressing `{{key:STO}}` or `{{key:RCL}}` followed by any letter key `A`–`Z` stores or recalls a value, and inserting `+`, `-`, `×`, or `÷` before the letter performs non-destructive **Storage or Recall Arithmetic** without cluttering the stack. Their shifted legends unlock two cornerstone workspaces: Left Shift `{{key:↰}}` above `{{key:STO}}` (`CMPLX`) arms the four-register Gaussian complex phasor engine on $(Y, X)$ and $(T, Z)$, while Right Shift `{{key:↱}}` above `{{key:STO}}` (`EQN`) opens the symbolic Equation Bank. Next door, `{{key:R↓}}` and its right shift `{{key:R↑}}` rotate all four stack registers circularly so you can inspect or reposition any intermediate value. Left Shift `{{key:↰}}` above `{{key:R↓}}` (`{{key:HYP}}`) serves as the hyperbolic prefix for `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`, and their `{{key:↰}}` inverse functions. Finally, the right shifts of the three trig keys place $\pi$ above `{{key:SIN}}`, Kahan's base-preserving percentage `{{key:%}}` above `{{key:COS}}`, and percent change `{{key:%CHG}}` above `{{key:TAN}}` within thumb reach.

| Row | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 0** | `{{key:LFU0}}` | `{{key:LFU1}}` | `{{key:LFU2}}` | `{{key:LFU3}}` | `{{key:LFU4}}` | `{{key:LFU5}}` |
| **Row 1** | `{{key:√x}}` | `{{key:eˣ}}` | `{{key:LN}}` | `{{key:yˣ}}` | `{{key:1/x}}` | `{{key:Σ+}}` |
| **Row 2** | `{{key:STO}}` | `{{key:RCL}}` | `{{key:R↓}}` | `{{key:SIN}}` | `{{key:COS}}` | `{{key:TAN}}` |

### Transition Zone (Row 3)

Row 3 forms the structural and ergonomic bridge between the upper scientific function array and the lower number pad. Anchoring Columns 0 and 1 is the signature double-wide **`{{key:ENTER}}`** bar—the physical fulcrum of Reverse Polish Notation. When you finish typing the first number of a dyadic pair, pressing `{{key:ENTER}}` terminates digit entry, pushes a copy of $X$ up into $Y$ ($T \leftarrow Z, Z \leftarrow Y, Y \leftarrow X$), and deliberately **disables stack lift** so the next number you type overwrites $X$ in place. Its shifted legends above `{{key:ENTER}}` are equally vital. Left Shift `{{key:↰}}` (`{{key:LASTX}}`) recalls the exact value that was in Register $X$ before the last mathematical operation for error recovery or reuse of a shared argument, while Right Shift `{{key:↱}}` (`{{key:SHOW}}`) temporarily reveals the full 15-digit internal mantissa and exponent of Register $X$ without altering your active `FIX`, `SCI`, or `ENG` display setting.

To the right of `{{key:ENTER}}` sits **`{{key:x⇄y}}`** at Row 3, Col 2, the register-exchange key that gives RPN its algebraic freedom. Whenever you evaluate a complex denominator or subtrahend *first* and then push the numerator or minuend onto the stack, a single tap of `{{key:x⇄y}}` swaps $X$ and $Y$ so `{{key:÷}}`, `{{key:-}}`, or `{{key:yˣ}}` executes in the proper order without parentheses. Its shifted functions inspect available memory (`{{key:↰}}` `MEM`) or swap $X$ with any letter register (`{{key:x⇄?}}`). Beside it at Row 3, Col 3, **`{{key:+/-}}`** toggles the sign of the number currently in $X$—or negates the power-of-ten exponent if pressed after `{{key:E}}`—while hosting the angular/radix `MODES` menu on `{{key:↰}}` and absolute value `{{key:ABS}}` ($|x|$) on `{{key:↱}}`.

Completing the transition bridge are **`{{key:E}}`** at Row 3, Col 4 and **`{{key:<-}}`** at Row 3, Col 5. Pressing `{{key:E}}` during number entry transitions from the mantissa to the base-10 exponent ($m \times 10^n$) so you can key physical constants like Planck's constant or Avogadro's number without multiplying by $10^x$. Its left shift opens the `DISP` precision menu (`FIX`, `SCI`, `ENG`, `ALL`), and its right shift executes Euclidean integer division with remainder (`{{key:÷R}}`), placing the quotient $\lfloor Y/X \rfloor$ in $X$ and the remainder in $Y$. At the far right, the backspace key **`{{key:<-}}`** adapts to your state: while you are actively typing digits, it erases one character at a time from the right. Once a number is finalized on the stack, pressing `{{key:<-}}` acts as `CLx`, zeroing Register $X$ and disabling stack lift without dropping $Y, Z,$ or $T$, while Left Shift `{{key:↰}}` opens the selective `CLEAR` menu.

| Row | Col 0 & 1 (Double-Wide) | Col 2 | Col 3 | Col 4 | Col 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 3** | `{{key:ENTER}}` | `{{key:x⇄y}}` | `{{key:+/-}}` | `{{key:E}}` | `{{key:<-}}` |

### Lower Arithmetic Zone (Rows 4–7, 5 Columns)

The lower four rows widen into a generous 5-column pitch engineered for rapid, eyes-free numeric entry and postfix arithmetic. Along the left margin in Column 0, four dedicated control keys govern execution and shift state. **`{{key:XEQ}}`** executes stored equations by label, while its shifts designate the target equation `FN=` on `{{key:↰}}` and open the quadratic/cubic `POLY` root workspace on `{{key:↱}}`. Below it, **`{{key:↰}}`** and **`{{key:↱}}`** act as latching, toggleable left- and right-shift prefixes. At the bottom-left corner, **`{{key:C}}`** (`ON`) wakes the hardware, cancels active prompts, or clears Register $X$, with `{{key:?}}` on `{{key:↰}}` for hardware diagnostics and `OFF` on `{{key:↱}}` for deep sleep. Along the right margin in Column 4, the four foundational dyadic operators—**`{{key:÷}}`**, **`{{key:×}}`**, **`{{key:-}}`**, and **`{{key:+}}`**—fuse $Y$ and $X$, drop the stack ($Y \leftarrow Z, Z \leftarrow T$), replicate $T$, and leave stack lift armed. Their shifted legends provide relational tests (`x?y`, `x?0`), computer-science integer `BASE` modes and system `FLAGS`, liter/gallon conversions (`{{key:▸l}}`/`{{key:▸gal}}`), and equation labels (`[LBL]`/`[RTN]`).

Across the central `0`–`9` and `.` digit pad in Columns 1–3, the shifted legends are organized into four intuitive engineering clusters so you can model physical problems on the stack:
* **Calculus, Root-Finding & Plot Navigation (`7` and `8`):** Right-shifting `{{key:7}}` (`{{key:SOLVE}}`) and `{{key:8}}` (`{{key:∫}}`) invokes Richard Brent's root finder and Werner Romberg's adaptive quadrature on the active `FN=` equation using your bounds in $Y$ and $X$. Left-shifting `{{key:7}}` (`{{key:↓}}`) and `{{key:8}}` (`{{key:↑}}`) steps through multi-equation banks or traces plotted curves.
* **2D Vector, Sexagesimal Time & Angular Conversions (`4`, `5`, and `6`):** Key `{{key:4}}` converts between rectangular coordinates $(x, y)$ in $(X, Y)$ and polar phasors $(r, \theta)$ via `{{key:▸θ,r}}` and `{{key:▸y,x}}`. Key `{{key:5}}` translates between `DD.MMSS` sexagesimal angles/timestamps and decimal hours/degrees (`{{key:▸HR}}` $\leftrightarrow$ `{{key:▸HMS}}`), and Key `{{key:6}}` converts between radians and degrees (`{{key:▸DEG}}` $\leftrightarrow$ `{{key:▸RAD}}`).
* **Physical SI $\leftrightarrow$ Imperial Unit Conversions (`9`, `1`, `2`, `3`, and `-`):** Every paired conversion puts the **metric unit on `{{key:↰}}`** and the **imperial unit on `{{key:↱}}`**. Distance sits on `{{key:9}}` (`{{key:▸km}}` $\leftrightarrow$ `{{key:▸mi}}`), mass on `{{key:1}}` (`{{key:▸kg}}` $\leftrightarrow$ `{{key:▸lb}}`), and temperature on `{{key:2}}` (`{{key:▸°C}}` $\leftrightarrow$ `{{key:▸°F}}`), followed by length on `{{key:3}}` (`{{key:▸cm}}` $\leftrightarrow$ `{{key:▸in}}`) and fluid volume on `{{key:-}}` (`{{key:▸l}}` $\leftrightarrow$ `{{key:▸gal}}`).
* **Register Inspection, Indirect Addressing (`i`, `(i)`), Relational Tests (`x?y`, `x?0`) & the Harmonic Hub (`0`, `.`, `x∥y`, `÷`):** Key `{{key:0}}` opens the full-screen `REGS` table (`{{key:↰}}`) or single-register `VIEW` (`{{key:↱}}`). Next to it, the radix point `{{key:.}}` toggles exact fraction display `{{key:FDISP}}` (`{{key:↰}}`), sets the maximum denominator `/c` (`{{key:↱}}`), and carries the Alpha label **`i`** for the index register. At Row 7, Col 3 sits the SC-32's signature **`{{key:x∥y}}`** key: a single unshifted tap evaluates the parallel harmonic product $\frac{Y \times X}{Y + X}$, while its shifted planes launch the 5-variable **`TVM`** financial solver (`N`, `I%`, `PV`, `PMT`, `FV`, `END/BEG` on `{{key:↰}}`) and open the 128-column, $128 \times 52\text{ px}$ **`PLOT`** graphing engine (`{{key:↱}}`). Its Alpha label **`(i)`** dereferences the integer pointer in `i` across all 89 slots of the memory map: `1`–`26` = `A`–`Z`, `27` = `i`, `28`–`33` = statistical sums, `34`–`39` = `POLY` roots, and `40`–`89` = raw statistical data points. Meanwhile, the division key **`{{key:÷}}`** at Row 4, Col 4 hosts the two six-operator relational comparison menus **`{{key:x?y}}`** (`{{key:↰}}`) and **`{{key:x?0}}`** (`{{key:↱}}`), which flash `YES`/`NO` non-destructively on the live stack and act as $1/0$ Iverson Boolean indicator switches inside `{{key:EQN}}` to model piecewise functions.

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

Every decision on the SC-32 keypad is governed by **the Dvorak Principle applied to calculators**: *whereas smartphones, computer terminals, and menu-driven graphing calculators bury operations inside nested menu trees that nobody can memorize, ninety-nine percent of your daily scientific and engineering work on a handheld instrument should require zero menus.* Every high-frequency operation belongs under your fingertips as a tactile keystroke.

### Why the HP-32SII Serves as the Structural Foundation

As explored in **[Chapter 1](01-craftsmanship-hardware.md)**, the 1991 **HP-32SII Pioneer** provides a uniquely versatile ergonomic and symbolic foundation for a modern RPN scientific instrument. Its one-handed portrait geometry keeps the digit pad, `{{key:ENTER}}`, and arithmetic column inside the natural sweep of a single thumb. At the same time, its 26 automatic alpha variables (`A`–`Z`) and human-readable **Equation Bank (`{{key:EQN}}`)** replace anonymous register numbers (`R0`–`R9`) and blind keystroke subroutines (`LBL 0..9`), while eight SI $\leftrightarrow$ Imperial unit conversions (expanded to ten on the SC-32) and native rational fractions (`{{key:FDISP}}`, `{{key:/c}}`) sit right on the number pad. The SC-32 preserves that 1991 Pioneer matrix while curing its 1-line display keyhole and infix-equation split personality. It also integrates the flagship analytical engines of the **1982 HP-15C Voyager** (`{{key:SOLVE}}`, `{{key:∫}}`, `{{key:CMPLX}}`), a dedicated SC-32 closed-form quadratic/cubic **`{{key:POLY}}`** engine, and the **1981 HP-12C Voyager** financial toolkit (`{{key:TVM}}`, `{{key:%}}`, `{{key:%CHG}}`) onto shifted keys:

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
| **Time Value of Money (`TVM`)** | Dedicated `n`, `i`, `PV`, `PMT`, `FV` keys | None | None (requires manual keystroke program) | **Built-in 5-Variable `{{key:TVM}}` (`N`, `I%`, `PV`, `PMT`, `FV`, `END/BEG`) on `{{key:x∥y}}`** |
| **Physical Unit Conversions** | None | `→H.MS`, `→RAD` only | 8 SI $\leftrightarrow$ US keys + polar/HMS/angle | **10 SI (`{{key:↰}}`) $\leftrightarrow$ US (`{{key:↱}}`) keys (adds `km` $\leftrightarrow$ `mi` on `9`) + polar/HMS/angle** |
| **Exact Fractions & Number Theory** | None | None | `a b/c`, `FDISP`, `/c`; `PARTS` menu | **Exact fractions (`{{key:FDISP}}`, `{{key:/c}}`), direct `{{key:÷R}}` & `{{key:ABS}}` keys (`GCD`/`LCM` in `PARTS` softkey menu)** |
| **Parallel / Harmonic Operator** | None | None | None | **Dedicated unshifted `{{key:x∥y}}` key ($\frac{Y \times X}{Y + X}$ for resistors, lenses, capacitors)** |
| **Graphical Plotting & Exam Mode** | None | None | None | **128-column ($128 \times 52\text{ px}$) `{{key:PLOT}}` function/scatter canvas (`{{key:x∥y}}`) + proctored `{{key:EXAM}}` lockdown** |

### Complete Key-by-Key & Menu Differences: HP-32SII vs. SC-32

Every primary key, left shift (`{{key:↰}}`, corresponding to the HP-32SII orange shift), right shift (`{{key:↱}}`, corresponding to the HP-32SII blue shift), and alpha legend on the SC-32 behaves identically to the 1991 HP-32SII **except** for the intentional hardware and menu additions listed below:

| Position / Menu | Key Face (SC-32 vs. HP-32SII) | Left Shift `{{key:↰}}` (SC-32 vs. HP-32SII) | Right Shift `{{key:↱}}` (SC-32 vs. HP-32SII) | Engineering Rationale for the SC-32 Design |
| :---: | :--- | :--- | :--- | :--- |
| **R0, C0–C5** | **`{{key:LFU0}}`–`{{key:LFU5}}`** *(New dedicated row)* | Dynamic LFU / Menu softkeys | Dynamic LFU / Menu softkeys | Reserves 6 dedicated physical softkeys beneath the 4-line LCD (showing 6 dynamic LFU functions in normal state and menu labels in menus) so menus never hijack `{{key:√x}}`..`{{key:Σ+}}` (`Row 1`). |
| **R3, C3** | `{{key:+/-}}` *(Same)* | `MODES` *(Adds `.` / `,` radix)* | **`{{key:ABS}}` (`\|x\|`)** *(HP-32SII: `(` open paren)* | Parentheses are unnecessary in RPN mode; places Absolute Value (`\|x\|`) on a direct right-shifted key while also retaining `ABS` inside the `PARTS` softkey menu. |
| **R3, C4** | `{{key:E}}` *(Same)* | `DISP` *(Same)* | **`{{key:÷R}}`** *(HP-32SII: `)` close paren)* | Parentheses are unnecessary in RPN mode; adds Euclidean integer division (`÷R`: quotient in $X$, remainder in $Y$) as a direct key. |
| **R3, C5** | `{{key:<-}}` *(Same)* | `CLEAR` *(Expanded menu)* | ***(Unassigned)*** *(HP-32SII: `=` equals)* | Infix `=` is not needed in RPN mode; leaving Right-Shift `{{key:<-}}` unassigned prevents accidental clears during fast entry. |
| **R4, C0** | `{{key:XEQ}}` *(Same)* | `FN=` *(Same)* | **`{{key:POLY}}`** *(HP-32SII: no direct key)* | Adds the closed-form quadratic/cubic `{{key:POLY}}` coefficient entry and root solver (`A`, `B`, `C`, `D`, `EXEC`, `CLR`) on `BLUE + XEQ`. |
| **R4, C3** | `{{key:9}}` *(Same)* | **`{{key:▸km}}`** *(HP-32SII: blank)* | **`{{key:▸mi}}`** *(HP-32SII: blank)* | Adds direct kilometer $\leftrightarrow$ mile unit conversions (`{{key:▸km}}` on `{{key:↰}}`, `{{key:▸mi}}` on `{{key:↱}}`) on `{{key:9}}`. |
| **R7, C1** | `{{key:0}}` *(Same)* | **`REGS`** *(HP-32SII: `INPUT`)* | `VIEW` *(Same)* | Repurposes programming-only `INPUT` to the `REGS` register viewer while keeping single-variable `VIEW` on `{{key:↱}}`. |
| **R7, C3** | **`{{key:x∥y}}`** *(HP-32SII: `R/S`)* | **`TVM`** *(HP-32SII: `PRGM`)* | **`PLOT`** *(HP-32SII: `PSE`)* | Repurposes `R/S` (`PRGM`/`PSE`) to Primary `{{key:x∥y}}`, Left-Shift `TVM` financial solver, Right-Shift `PLOT` canvas, and Alpha `(i)`. |
| **R7, C4** | `{{key:+}}` *(Same)* | `[LBL]` *(Restored for `EQN`)* | `[RTN]` *(Same)* | Retains `[LBL]` on Left-Shift `{{key:+}}` so stored RPN equations can begin with an explicit single-letter label. |
| **`PARTS` Menu** | Trigger: `Right-Shift {{key:√x}}` | HP-32SII: `IP`, `FP`, `ABS` | **SC-32 adds `SGN`, `GCD`, `LCM`** | Places `SGN`, `GCD`, and `LCM` inside the 6-item `PARTS` softkey menu (`IP`, `FP`, `ABS`, `SGN`, `GCD`, `LCM`; only the elementary SC-6 has physical `GCF`/`LCM` buttons). |
| **`CLEAR` Menu** | Trigger: `Left-Shift {{key:<-}}` | HP-32SII: `CLx`, `CLVARS`, `CLΣ`, `ALL` | **SC-32: `CLEQN`, `CLVARS`, `CLALL`, `CLΣ`, `CLREGS`, `CLSTK`** | Expands `CLEAR` to six softkeys (plus `FIN` inside `TVM` to zero `N`, `I%`, `PV`, `PMT`, `FV` while preserving `END`/`BEG`). |
| **`FLAGS` Menu** | Trigger: `Right-Shift {{key:×}}` | HP-32SII: `SF n`, `CF n`, `FS? n`, `FC? n` | **SC-32 adds `4-LVL`, `8-LVL`, `INF`, `EXAM`** | Extends `FLAGS` with selectable stack depth (`4-LVL`, `8-LVL`, `INF`) and proctored `EXAM` lockdown. |
| **`EQN` Mode** | Trigger: `Right-Shift {{key:STO}}` | HP-32SII: Infix strings (`SIN(X)+1`) | **SC-32: RPN step entry + `EQN_NEW`/`EQN_EDIT`** | Stores and edits equations as pure RPN instruction steps with LFU softkeys (`EQN_NEW`, `EQN_EDIT`). |

### Seven Architectural Enhancements Over the Vintage HP-32SII

Beyond the physical keycap legends, the SC-32 expands seven core subsystems while preserving 100% compatibility with classic HP-32SII workflows:

* **Four-Line Stack Display & Dedicated 6-Key LFU Bar (`R0, C0–C5`):** Replaces the HP-32SII's single-line 12-character LCD with a $132 \times 65\text{ px}$ transflective 4-line stack view ($T, Z, Y, X$) paired with six physical LFU softkeys (`{{key:LFU0}}`–`{{key:LFU5}}`), so active submenus never hijack `{{key:√x}}`..`{{key:Σ+}}`.
* **Pure RPN Equations & Iverson Piecewise Booleans (`{{key:EQN}}`):** Evaluates stored equations as pure, side-effect-free RPN token streams rather than infix strings. Relational tests from `{{key:x?y}}` and `{{key:x?0}}` (`R4C4`) act as non-destructive **Iverson indicator brackets $[P] \in \{1, 0\}$** on Register $X$ (preserving $Y$ and $Z$), enabling branchless piecewise formulas across `{{key:XEQ}}`, `{{key:SOLVE}}`, `{{key:∫}}`, and `{{key:PLOT}}`.
* **Direct `|x|` & `÷R` Keys and Expanded `PARTS` Softkey Menu (`R1C0`, `R3C3–C4`):** Reclaiming infix `(` and `)` on Row 3 places Absolute Value `{{key:ABS}}` (`|x|`) and Euclidean quotient-remainder division `{{key:÷R}}` on direct right-shifted keys, while the `PARTS` softkey menu (`Right-Shift {{key:√x}}`) retains the HP-32SII's `IP`, `FP`, and `ABS` softkeys (`LFU0`–`LFU2`) and adds Signum (`SGN`), Greatest Common Divisor (`GCD`), and Least Common Multiple (`LCM`) on `LFU3`–`LFU5` (unlike the elementary SC-6, where `GCF` and `LCM` are physical keys).
* **Analytic `POLY` Root Workspace & `TVM` Financial Engine (`R4C0`, `R7C3`):** Adds a closed-form quadratic and cubic polynomial solver (`{{key:POLY}}`: `A`, `B`, `C`, `D`, `EXEC`, `CLR`) that writes all real and complex conjugate roots to `R34`–`R39`, alongside a 5-variable HP-12C `{{key:TVM}}` solver (`N`, `I%`, `PV`, `PMT`, `FV`, `END/BEG`).
* **128-Column Graphical `PLOT` Viewport (`R7C3`):** Adds a $128 \times 52\text{ px}$ function and statistical scatter-plot canvas with interactive cursor trace (`{{key:↓}}`, `{{key:↑}}`, `[SCRL]`), root-bracketing markers (`MARK`, `STORE`), and shaded definite-integral preview (`∫ f(x)`).
* **Configurable Stack Depth (`4-LVL`, `8-LVL`, `INF`) & Proctored `EXAM` Mode (`R5C4`):** The `FLAGS` menu preserves user Flags `0`–`9` (`SF`, `CF`, `FS?`) and adds the `STACK` submenu (`2-LVL`, `4-LVL`, `8-LVL`, `INF`, `VIEW`) plus proctored `EXAM` lockdown. Default `4-LVL` mode preserves exact Corvallis 4-register physics (including top-of-stack $T$-replication on drop), while `8-LVL` and `INF` (999-level LIFO) eliminate register overflow during deeply nested evaluations.
* **36-Bit Signed Two's-Complement `BASE` Arithmetic & 89-Slot Indirect Memory Map (`i`, `(i)`):** Expands integer `BASE` operations (`DEC`, `HEX`, `OCT`, `BIN`) from 32-bit unsigned truncation to a 36-bit signed two's-complement word (9 hex nibbles, 12 octal digits). Integer pointers $k \in \{1 \dots 89\}$ stored in `i` (`STO` `{{key:.}}`) and dereferenced via `(i)` (`RCL` `{{key:x∥y}}` or `STO` `{{key:x∥y}}`) address:
  * `1`–`26`: Named variables `A` through `Z` (`1 = A`, `2 = B`, $\dots$, `26 = Z`), plus `27` for the index register `i` itself.
  * `28`–`33`: Live statistical accumulators (`n, Σx, Σx², Σy, Σy², Σxy` in the `STATS` register browser; arranged as `Σx, Σy, Σx², Σy², Σxy, n` on the `SUMS` softkey bar).
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

A calculator can look visually identical across a wristwatch, a smartphone, a desktop browser, and a physical handheld while subtly disagreeing at the edge cases that matter most to a serious user. Those subtleties govern how `{{key:ENTER}}` disarms stack lift, how an interrupted digit entry interacts with `{{key:x⇄y}}`, how `{{key:LASTX}}` behaves after a unary versus a dyadic operator, and how the stack recovers when an operation hits $\tan(90^\circ)$ or $\ln(0)$. To guarantee that every surface behaves as one mathematical mind, we built a single deterministic state machine at the heart of the project. Whether a keypress originates from a touchscreen tap, a desktop keyboard shortcut, or a physical row-and-column switch contact on the handheld PCB, it steps the same four-register automaton before a single pixel is drawn.

### Mathematical Rigor in Silicon: Lanczos, Brent, and Romberg
Building an honest scientific instrument means refusing to take numerical shortcuts. Early in development, we committed that every transcendental function, statistical estimator, root solver, and definite integral on the SC-32 would use classic, peer-reviewed algorithms from the golden age of numerical analysis:

* **Continuous Factorials via Cornelius Lanczos's Gamma Approximation:** Rather than limiting `{{key:x!}}` to a lookup table of whole numbers, the engine evaluates $\Gamma(x+1)$ across the real line using Cornelius Lanczos's Chebyshev rational approximation paired with Euler's reflection formula $\Gamma(z)\Gamma(1-z) = \frac{\pi}{\sin(\pi z)}$, maintaining 15-digit internal precision from fractional half-integers up to $170! \approx 7.2574 \times 10^{306}$.
* **Guaranteed Root-Finding via Richard Brent's Hybrid Algorithm:** Pure Newton–Raphson iteration can fly off to infinity when a curve flattens near a local extremum, while pure bisection crawls at one binary bit per step. Our `{{key:SOLVE}}` engine implements Richard Brent's 1973 hybrid method, which races ahead with inverse quadratic and secant interpolation whenever the curve is well-behaved, yet automatically falls back to a bisection step the instant an iterate threatens to step outside the bracket $[a, b]$ or stall.
* **Adaptive Calculus via Werner Romberg's Richardson Tableau:** When you press `{{key:∫}}`, the calculator does not stop at summing crude rectangles. It constructs a triangular Romberg tableau, halving the trapezoidal step size and applying Lewis Fry Richardson's $\frac{4^m T_{k,m-1} - T_{k-1,m-1}}{4^m - 1}$ error-cancellation cascade to strip away successive powers of $h^2, h^4, h^6$ until the integral converges to machine tolerance.

Every one of these numerical engines—alongside William Kahan's compensated summation and base-preserving percentages, Gaussian complex phasor arithmetic, and 36-bit two's-complement word operations—is continuously checked against tens of thousands of reference mathematical vectors so that the numbers on the screen match the equations in this book to the last decimal place.

### Four-Layer Gold-Immersion Hardware, Daylight Optics & Tactile Key-Feel
Translating that software engine into a physical pocket observatory required co-designing electronics, optics, and mechanics as a single sculpture:

* **Four-Layer ENIG Circuit Architecture & Continuous Memory:** The custom four-layer printed circuit board uses an electroless nickel immersion gold (ENIG) surface finish across its switch matrix pads for corrosion-free contact longevity over hundreds of thousands of actuations. Whenever the instrument naps between calculations, it writes atomic, checksum-verified state snapshots—preserving all four stack registers ($T, Z, Y, X$), `LASTX`, the 26 letter registers (`A`–`Z`), all six statistical accumulators, TVM financial registers, and the 24-slot Equation Bank—into alternating non-volatile memory banks so your work is never lost.
* **Reflective Daylight Readability & Tactile Snap-Dome Acoustics:** Instead of a power-hungry smartphone screen that washes out in sunlight and demands nightly charging, the SC-32 pairs a crisp $132 \times 65$ transflective liquid-crystal display with a brushed-aluminum faceplate. Ambient light passes through the liquid-crystal layer and reflects off the internal metallic mirror, growing sharper as the room gets brighter, while precision stainless-steel snap domes beneath the 43 sculpted keycaps deliver a crisp tactile break so your fingertips know a digit has registered before your eyes leave the page.
* **Simulating Silicon & Board-Aware Parametric CAD:** While the four-layer boards were in fabrication, we wired a browser-based hardware simulator to a cycle-accurate microcontroller emulator to verify matrix debouncing, sleep wake-up timing, and pixel typography before the first physical board arrived at the bench. As chronicled in our Hackaday engineering logs, our parametric OpenSCAD enclosure scripts read mounting and switch coordinates from the KiCad layout—separating mechanical **Guide**, **Capture**, **Stop**, and **Release** geometries so the tapered chassis, faceplate, TPU keypad membrane, and snap-retained cap slide together without a single screw or drop of glue. Complete KiCad schematics, parametric CAD sources, printable `.stl`/`.3mf` files, and firmware build logs are openly published at **[stackcalc.io/downloads](https://stackcalc.io/downloads)** for students, educators, and engineers worldwide. To put these 43 physical keys to work across every major branch of mathematics, physics, engineering, chemistry, and finance, continue to **[Appendix D: Mathematical Constants, SI Units & Master STEM Equation Directory](appendix-d-constants-and-equations.md)**.
