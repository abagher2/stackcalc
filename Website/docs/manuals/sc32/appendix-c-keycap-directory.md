---
title: "Appendix C: Physical Keycap & Softkey Menu Directory | Thinking in the Stack (SC-32)"
description: "Complete 43-key matrix directory, primary, left-shifted, and right-shifted legends, ergonomic zone architecture, and dynamic LFU softkey menus on the StackCalc SC-32."
---

# Appendix C: Physical Keycap & Softkey Menu Directory

The StackCalc SC-32 organizes its 43-key tactile matrix (**Figure C.1**) into three ergonomic zones paired with a three-layer shift grammar that groups functions by mathematical association without deeply nested menu trees.

{{blocks:sc32_utility_ortho|StackCalc SC-32 Scientific RPN Calculator physical faceplate render, showing the 43-key layout, upper dynamic LFU softkeys, double-wide ENTER bar, and high-contrast primary and secondary shift legends.}}

## Three-Zone Keypad Architecture & Shift Grammar

Beneath the top row of six dynamic softkeys (`{{key:LFU0}}`–`{{key:LFU5}}`), each of the 37 main physical keys carries three operational meanings plus an automatic alpha character (`A`–`Z`, `i`, `(i)`):

* **Primary Legend (White Center Label — 1 Tap):** Executes the primary operation for that key position: core transcendentals (`{{key:√x}}`, `{{key:eˣ}}`, `{{key:LN}}`, `{{key:yˣ}}`, `{{key:1/x}}`, `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`), statistical accumulation (`{{key:Σ+}}`), stack and memory control (`{{key:STO}}`, `{{key:RCL}}`, `{{key:R↓}}`, `{{key:ENTER}}`, `{{key:x⇄y}}`), and postfix arithmetic (`{{key:÷}}`, `{{key:×}}`, `{{key:-}}`, `{{key:+}}`, `{{key:x∥y}}`).
* **Left Shift (`{{key:↰}}` — Mathematical Inverse or SI Companion):** Accesses the mathematical inverse printed over the upper-left corner (`{{key:√x}}` $\leftrightarrow$ `{{key:x²}}`, `{{key:eˣ}}` $\leftrightarrow$ `{{key:10ˣ}}`, `{{key:LN}}` $\leftrightarrow$ `{{key:LOG}}`, `{{key:yˣ}}` $\leftrightarrow$ `{{key:ˣ√y}}`, `{{key:1/x}}` $\leftrightarrow$ `{{key:x!}}`, `{{key:Σ+}}` $\leftrightarrow$ `{{key:Σ-}}`, `{{key:SIN}}` $\leftrightarrow$ `{{key:ASIN}}`, `{{key:COS}}` $\leftrightarrow$ `{{key:ACOS}}`, `{{key:TAN}}` $\leftrightarrow$ `{{key:ATAN}}`, `{{key:ENTER}}` $\leftrightarrow$ `{{key:LASTX}}`), complex/hyperbolic prefixes (`{{key:CMPLX}}`, `{{key:HYP}}`), system menus (`MODES`, `DISP`, `CLEAR`, `BASE`, `REGS`, `TVM`), and metric/polar conversions (`{{key:▸km}}`, `{{key:▸kg}}`, `{{key:▸°C}}`, `{{key:▸cm}}`, `{{key:▸l}}`, `{{key:▸θ,r}}`, `{{key:▸HR}}`, `{{key:▸DEG}}`).
* **Right Shift (`{{key:↱}}` — Analytical Workspaces, Solvers & Softkey Menus):** Opens domain softkey menus (`PARTS`, `PROB`, `L.R.`, `x̄,ȳ`, `s,σ`, `SUMS`, `FLAGS`, `x?0`), numerical solvers (`{{key:POLY}}`, `{{key:SOLVE}}`, `{{key:∫}}`, `EQN`), specialized operators (`π`, `{{key:%}}`, `{{key:%CHG}}`, `{{key:ABS}}`, `{{key:÷R}}`, `{{key:SHOW}}`), and imperial/rectangular conversions (`{{key:▸mi}}`, `{{key:▸lb}}`, `{{key:▸°F}}`, `{{key:▸in}}`, `{{key:▸gal}}`, `{{key:▸y,x}}`, `{{key:▸HMS}}`, `{{key:▸RAD}}`).
* **Alpha Labels (`A`–`Z`, `i`, `(i)`):** Activate whenever a command prompts for a register or label (`{{key:STO}}`, `{{key:RCL}}`, `{{key:XEQ}}`, `FN=`, `LBL`, `{{key:SOLVE}}`, `{{key:∫}}`). The `(i)` label on `{{key:x∥y}}` dereferences pointer `i` across all 89 memory slots (`1`–`26` = `A`–`Z`, `27` = `i`, `28`–`33` = statistical sums, `34`–`39` = `POLY` roots, `40`–`89` = `DATA0`–`DATA49`).

| Zone | Rows & Pitch | Architectural Layout |
| :--- | :--- | :--- |
| **Upper Function Zone** | Rows 0–2 (6 Cols) | Row 0: `{{key:LFU0}}`–`{{key:LFU5}}` dynamic softkeys. Row 1: `{{key:√x}}`, `{{key:eˣ}}`, `{{key:LN}}`, `{{key:yˣ}}`, `{{key:1/x}}`, `{{key:Σ+}}`. Row 2: `{{key:STO}}`, `{{key:RCL}}`, `{{key:R↓}}`, `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`. |
| **Transition Zone** | Row 3 (5 Keys / 6 Cols) | Double-wide `{{key:ENTER}}` bar (Cols 0–1), `{{key:x⇄y}}` (Col 2), `{{key:+/-}}` (Col 3), `{{key:E}}` (Col 4), and dual-mode `{{key:<-}}` / `CLx` (Col 5). |
| **Lower Arithmetic Zone** | Rows 4–7 (5 Cols) | Col 0: `{{key:XEQ}}`, `{{key:↰}}`, `{{key:↱}}`, `{{key:C}}`. Cols 1–3: `0`–`9`, `.`, `{{key:x∥y}}`. Col 4: `{{key:÷}}`, `{{key:×}}`, `{{key:-}}`, `{{key:+}}`. |

## Physical Matrix Coordinate Grids by Zone

Row 0 (`{{key:LFU0}}`–`{{key:LFU5}}`) is a context-aware LFU (Least Frequently Used) dynamic softkey strip: in normal state, it surfaces the six functions tracked by the LFU algorithm, and whenever a menu or workspace (such as `PARTS`, `PROB`, `L.R.`, `BASE`, `MODES`, `DISP`, `FLAGS`, `TVM`, or `POLY`) opens, it remaps to that menu's softkey labels along the bottom row of the LCD. Row 1 groups power, exponential, logarithmic, reciprocal, and statistical accumulation operators along a single row, while Row 2 pairs register management (`{{key:STO}}`, `{{key:RCL}}`) and circular stack rotation (`{{key:R↓}}`) with planar trigonometry (`{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`):

| Upper Zone Row | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 0** | `{{key:LFU0}}` | `{{key:LFU1}}` | `{{key:LFU2}}` | `{{key:LFU3}}` | `{{key:LFU4}}` | `{{key:LFU5}}` |
| **Row 1** | `{{key:√x}}` | `{{key:eˣ}}` | `{{key:LN}}` | `{{key:yˣ}}` | `{{key:1/x}}` | `{{key:Σ+}}` |
| **Row 2** | `{{key:STO}}` | `{{key:RCL}}` | `{{key:R↓}}` | `{{key:SIN}}` | `{{key:COS}}` | `{{key:TAN}}` |

Across Row 3, five physical keys bridge the upper 6-column scientific deck and the lower 5-column numeric pad. Anchoring Columns 0–1 is the double-wide `{{key:ENTER}}` bar (`{{key:LASTX}}` on `{{key:↰}}`, `{{key:SHOW}}` on `{{key:↱}}`), flanked by `{{key:x⇄y}}`, `{{key:+/-}}`, `{{key:E}}`, and dual-mode `{{key:<-}}` (character backspace during `EDIT`; `CLx` on a finalized register):

| Transition Row | Col 0 & 1 (Double-Wide) | Col 2 | Col 3 | Col 4 | Col 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 3** | `{{key:ENTER}}` | `{{key:x⇄y}}` | `{{key:+/-}}` | `{{key:E}}` | `{{key:<-}}` |

Rows 4–7 widen into a 5-column numeric and postfix arithmetic grid. Column 0 houses `{{key:XEQ}}` (`FN=` / `POLY`), latching shifts `{{key:↰}}` and `{{key:↱}}`, and `{{key:C}}` (`?` / `OFF`). Column 4 houses `{{key:÷}}`, `{{key:×}}`, `{{key:-}}`, and `{{key:+}}`. Across the central `0`–`9`, `.`, and `{{key:x∥y}}` keys in Columns 1–3, shifted legends provide root finding (`{{key:SOLVE}}` on `{{key:7}}`), Romberg integration (`{{key:∫}}` on `{{key:8}}`), 2D vector and angular conversions (`{{key:4}}`, `{{key:5}}`, `{{key:6}}`), SI $\leftrightarrow$ Imperial unit conversions (`{{key:9}}`, `{{key:1}}`, `{{key:2}}`, `{{key:3}}`, `{{key:-}}`), register inspection (`{{key:0}}`), rational fraction control (`{{key:.}}`), and the 5-variable `TVM` financial workspace (`{{key:x∥y}}`):

| Lower Zone Row | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 4** | `{{key:XEQ}}` | `{{key:7}}` | `{{key:8}}` | `{{key:9}}` | `{{key:÷}}` |
| **Row 5** | `{{key:↰}}` (Left Shift) | `{{key:4}}` | `{{key:5}}` | `{{key:6}}` | `{{key:×}}` |
| **Row 6** | `{{key:↱}}` (Right Shift) | `{{key:1}}` | `{{key:2}}` | `{{key:3}}` | `{{key:-}}` |
| **Row 7** | `{{key:C}}` (ON) | `{{key:0}}` | `{{key:.}}` | `{{key:x∥y}}` | `{{key:+}}` |

---

## The 43-Key Function Directory

The 43-key hardware directory maps every matrix coordinate `(R, C)` across Rows `R0`–`R7` to its primary legend, left shift (`{{key:↰}}`), right shift (`{{key:↱}}`), and alpha register label:

| Key # | Matrix (R, C) | Primary Legend | Left Shift `{{key:↰}}` | Right Shift `{{key:↱}}` | Alpha | Functional Summary |
| :---: | :---: | :--- | :--- | :--- | :---: | :--- |
| **1** | R0, C0 | `{{key:LFU0}}` | Softkey 1 | Softkey 1 | — | Dynamic LFU slot 1 / active softkey menu item 1 |
| **2** | R0, C1 | `{{key:LFU1}}` | Softkey 2 | Softkey 2 | — | Dynamic LFU slot 2 / active softkey menu item 2 |
| **3** | R0, C2 | `{{key:LFU2}}` | Softkey 3 | Softkey 3 | — | Dynamic LFU slot 3 / active softkey menu item 3 |
| **4** | R0, C3 | `{{key:LFU3}}` | Softkey 4 | Softkey 4 | — | Dynamic LFU slot 4 / active softkey menu item 4 |
| **5** | R0, C4 | `{{key:LFU4}}` | Softkey 5 | Softkey 5 | — | Dynamic LFU slot 5 / active softkey menu item 5 |
| **6** | R0, C5 | `{{key:LFU5}}` | Softkey 6 | Softkey 6 | — | Dynamic LFU slot 6 / active softkey menu item 6 |
| **7** | R1, C0 | `{{key:√x}}` | `{{key:x²}}` | `PARTS` Menu | `A` | Square root √x, square x², and number-theory PARTS menu (IP, FP, ABS, SGN, GCD, LCM) |
| **8** | R1, C1 | `{{key:eˣ}}` | `{{key:10ˣ}}` | `PROB` Menu | `B` | Natural exponential eˣ, common antilog 10ˣ, and combinatorics PROB menu (Cn,r, Pn,r, n!, RAND, SD) |
| **9** | R1, C2 | `{{key:LN}}` | `{{key:LOG}}` | `L.R.` Menu | `C` | Natural logarithm LN, base-10 logarithm LOG, and linear regression L.R. menu (ŷ, x̂, r, m, b) |
| **10**| R1, C3 | `{{key:yˣ}}` | `{{key:ˣ√y}}` | `x̄,ȳ` Menu | `D` | Dyadic power yˣ, x-th root ˣ√y, and sample/weighted means menu (x̄, ȳ, x̄w) |
| **11**| R1, C4 | `{{key:1/x}}` | `{{key:x!}}` | `s,σ` Menu | `E` | Reciprocal 1/x, factorial/Gamma x!, and sample/population standard deviation menu (sx, sy, σx, σy) |
| **12**| R1, C5 | `{{key:Σ+}}` | `{{key:Σ-}}` | `SUMS` Menu | `F` | Statistical data accumulation Σ+, removal Σ-, and summation register menu (Σx, Σy, Σx², Σy², Σxy, n) |
| **13**| R2, C0 | `{{key:STO}}` | `CMPLX` Mode | `EQN` Mode | `G` | Store register STO, complex phasor prefix CMPLX, and symbolic RPN Equation Bank EQN |
| **14**| R2, C1 | `{{key:RCL}}` | `{{key:RND}}` Round | `{{key:SCRL}}` Scroll | `H` | Recall register RCL, round mantissa to display precision RND, and scroll long equations |
| **15**| R2, C2 | `{{key:R↓}}` | `{{key:HYP}}` Prefix | `{{key:R↑}}` Roll Up | `I` | Roll stack down R↓, hyperbolic function prefix HYP, and roll stack up R↑ |
| **16**| R2, C3 | `{{key:SIN}}` | `{{key:ASIN}}` | `π` Constant | `J` | Sine SIN, inverse sine ASIN, and 15-digit π constant |
| **17**| R2, C4 | `{{key:COS}}` | `{{key:ACOS}}` | `{{key:%}}` Base Pct | `K` | Cosine COS, inverse cosine ACOS, and Kahan base-preserving percentage % |
| **18**| R2, C5 | `{{key:TAN}}` | `{{key:ATAN}}` | `{{key:%CHG}}` Pct Chg| `L` | Tangent TAN, inverse tangent ATAN, and base-preserving percent change %CHG |
| **19**| R3, C0-1| `{{key:ENTER}}` | `{{key:LASTX}}` | `{{key:SHOW}}` | `M` | Duplicate X to Y and disable lift ENTER, recall prior operand LASTX, and full-precision peek SHOW |
| **20**| R3, C2 | `{{key:x⇄y}}` | `MEM` Specs | `{{key:x⇄?}}` (`x⇄`) | `N` | Swap X and Y registers x⇄y, memory status summary MEM, and exchange X with named register x⇄? |
| **21**| R3, C3 | `{{key:+/-}}` | `MODES` Menu | `{{key:ABS}}` ($\lvert x\rvert$) | `O` | Toggle sign +/-, angular/radix MODES menu (DEG, RAD, GRAD, ., ,), and absolute value $\lvert x\rvert$ |
| **22**| R3, C4 | `{{key:E}}` | `DISP` Menu | `{{key:÷R}}` Div/Rem | `P` | Scientific exponent entry E, display format DISP menu (FIX, SCI, ENG, ALL), and Euclidean quotient/remainder ÷R |
| **23**| R3, C5 | `{{key:<-}}` | `CLEAR` Menu | *(Unassigned)*| — | Digit backspace / clear X register CLx, and selective workspace CLEAR menu |
| **24**| R4, C0 | `{{key:XEQ}}` | `FN=` Define | `POLY` Solver | — | Execute equation XEQ, select target function FN=, and closed-form quadratic/cubic POLY root solver |
| **25**| R4, C1 | `{{key:7}}` | `{{key:↓}}` Step Down| `{{key:SOLVE}}` Brent | `Q` | Digit 7, step down equation/register list ↓, and Richard Brent hybrid root solver SOLVE |
| **26**| R4, C2 | `{{key:8}}` | `{{key:↑}}` Step Up | `{{key:∫}}` Quadrature| `R` | Digit 8, step up equation/register list ↑, and adaptive Romberg numerical integration ∫ |
| **27**| R4, C3 | `{{key:9}}` | `{{key:▸km}}` Conv | `{{key:▸mi}}` Conv | `S` | Digit 9, miles-to-kilometers conversion ▸km, and kilometers-to-miles conversion ▸mi |
| **28**| R4, C4 | `{{key:÷}}` | `x?y` Menu | `x?0` Menu | — | Dyadic division ÷, relational comparison menu x?y, and zero-comparison menu x?0 |
| **29**| R5, C0 | `{{key:↰}}` (Left Shift)| *(Left Shift Latch)* | *(Left Shift Latch)* | — | Primary Left Shift modifier prefix (toggles upper-left key legends) |
| **30**| R5, C1 | `{{key:4}}` | `{{key:▸θ,r}}` Polar | `{{key:▸y,x}}` Rect | `T` | Digit 4, rectangular-to-polar conversion ▸θ,r, and polar-to-rectangular conversion ▸y,x |
| **31**| R5, C2 | `{{key:5}}` | `{{key:▸HR}}` Hours | `{{key:▸HMS}}` Time | `U` | Digit 5, sexagesimal DD.MMSS to decimal hours/degrees ▸HR, and decimal to sexagesimal ▸HMS |
| **32**| R5, C3 | `{{key:6}}` | `{{key:▸DEG}}` Angle | `{{key:▸RAD}}` Angle | `V` | Digit 6, radians-to-degrees conversion ▸DEG, and degrees-to-radians conversion ▸RAD |
| **33**| R5, C4 | `{{key:×}}` | `BASE` Menu | `FLAGS` Menu | — | Dyadic multiplication ×, radix BASE menu (HEX, DEC, OCT, BIN), and system FLAGS / stack-depth menu |
| **34**| R6, C0 | `{{key:↱}}` (Right Shift)| *(Right Shift Latch)* | *(Right Shift Latch)* | — | Secondary Right Shift modifier prefix (toggles upper-right key legends) |
| **35**| R6, C1 | `{{key:1}}` | `{{key:▸kg}}` Mass | `{{key:▸lb}}` Mass | `W` | Digit 1, pounds-to-kilograms conversion ▸kg, and kilograms-to-pounds conversion ▸lb |
| **36**| R6, C2 | `{{key:2}}` | `{{key:▸°C}}` Temp | `{{key:▸°F}}` Temp | `X` | Digit 2, Fahrenheit-to-Celsius conversion ▸°C, and Celsius-to-Fahrenheit conversion ▸°F |
| **37**| R6, C3 | `{{key:3}}` | `{{key:▸cm}}` Length | `{{key:▸in}}` Length | `Y` | Digit 3, inches-to-centimeters conversion ▸cm, and centimeters-to-inches conversion ▸in |
| **38**| R6, C4 | `{{key:-}}` | `{{key:▸l}}` Volume | `{{key:▸gal}}` Volume| — | Dyadic subtraction -, US gallons-to-liters conversion ▸l, and liters-to-US gallons conversion ▸gal |
| **39**| R7, C0 | `{{key:C}}` (ON) | `{{key:?}}` Tutorial | `OFF` Sleep | — | Clear entry / dismiss error / wake hardware C, interactive guided tutorial ?, and power sleep OFF |
| **40**| R7, C1 | `{{key:0}}` | `REGS` Viewer | `VIEW` Single | `Z` | Digit 0, full-screen register browser REGS (STACK, STO, STATS, DATA), and single-register inspect VIEW |
| **41**| R7, C2 | `{{key:.}}` | `{{key:FDISP}}` Frac | `{{key:/c}}` Denom | `i` | Decimal radix point ., toggle rational fraction display FDISP, and set fixed fraction denominator /c |
| **42**| R7, C3 | `{{key:x∥y}}` | `TVM` Solver | `{{key:PLOT}}` Graph | `(i)`| Parallel harmonic operator x∥y, 5-variable TVM financial solver, App-mode function/scatter plotter PLOT (omitted on physical firmware for exam compliance), and indirect address pointer (i) |
| **43**| R7, C4 | `{{key:+}}` | `{{key:LBL}}` Label | `{{key:RTN}}` Return | — | Dyadic addition +, equation label token `LBL`, and subroutine return token `RTN` |

---

## Dynamic LFU Softkey Menus & Analytical Workspaces Directory

The six top keys (`{{key:LFU0}}` through `{{key:LFU5}}`) dynamically remap to on-screen menu labels along the bottom pixel row of the transflective LCD whenever a modal menu or analytical workspace is opened, executing the corresponding softkey action without obscuring the four visible stack registers ($T, Z, Y, X$). In normal calculation mode (`ALL`/`FIX`/`SCI`/`ENG` without an active modal submenu), the six softkey slots display the six most frequently invoked functions, retained by a Least-Frequently-Used (LFU) cache-eviction policy:

| Menu / Workspace | Access Keystroke | Top-Row Softkeys (`LFU0` – `LFU5`) | Default & Execution Behavior |
| :--- | :--- | :--- | :--- |
| **`DISP`** | `{{key:↰}}` + `{{key:E}}` | `FIX n`, `SCI n`, `ENG n`, `ALL` | Default `ALL`; tapping `FIX`, `SCI`, or `ENG` prompts for digit `0`–`9` (`•` marks active format). |
| **`MODES`** | `{{key:↰}}` + `{{key:+/-}}` | `DEG`, `RAD`, `GRAD`, `.`, `,` | Default `DEG` and radix `.`; active angular unit and radix mark carry a bullet (`•`). |
| **`BASE`** | `{{key:↰}}` + `{{key:×}}` | `HEX`, `DEC`, `OCT`, `BIN` | Default `DEC`; re-renders integers in $[-2^{35}, 2^{35}-1]$ (64-bit two's complement for negatives; `HEX` maps Row 1 keys to `A`–`F`). |
| **`CONST`** | Companion / Menu | `π`, `e`, `h`, `c`, `G`, `Na`, `R`, `k` | Pushes fundamental physical/mathematical constants ($\pi, e, h, c, G, N_A, R, k_B$) to $X$ with stack lift. |
| **`CLEAR`** | `{{key:↰}}` + `{{key:<-}}` | `CLEQN`, `CLVARS`, `CLALL`, `CLSTAT`, `CLREGS`, `CLSTK` | Resets the selected subsystem to `0` (`CLSTAT` aliases `{{key:CLΣ}}`) without disturbing other workspaces. |
| **`MEM`** | `{{key:↰}}` + `{{key:x⇄y}}` | `VARS`, `EQN`, `REGS` | Displays available memory and catalogs allocated variable, equation, and register blocks. |
| **`FLAGS`** | `{{key:↱}}` + `{{key:×}}` | `STACK ▸`, `MODE ▸`, `UI ▸`, `EXAM`, `SF`, `CF` | Displays 10-flag status grid (`0:F0`–`9:d/c`) toggled by digits `0`–`9` (or submenus in companion app). |
| **`STACK`** | `FLAGS` $\to$ `STACK` | `2-LVL`, `4-LVL`, `8-LVL`, `INF`, `VIEW` | Default `4-LVL` ($T, Z, Y, X$ with $T$-replication) and `4-LN` four-line view (`VIEW` toggles `1-LN`). |
| **`PARTS`** | `{{key:↱}}` + `{{key:√x}}` | `IP`, `FP`, `ABS`, `SGN`, `GCD`, `LCM` | Monadic `IP`, `FP`, `ABS`, `SGN` act on $X$; dyadic `GCD` and `LCM` reduce integers across $(Y, X)$. |
| **`PROB`** | `{{key:↱}}` + `{{key:eˣ}}` | `Cn,r`, `Pn,r`, `n!`, `RAND`, `SD` | `Cn,r` and `Pn,r` consume $(Y = n,\; X = r)$; `RAND` pushes $U[0,1)$ with stack lift; `SD` seeds generator from $X$ and drops stack. |
| **`SUMS`** | `{{key:↱}}` + `{{key:Σ+}}` | `Σx`, `Σy`, `Σx²`, `Σy²`, `Σxy`, `n` | Recalls the six sufficient statistics (`R28 = n`, `R29 = Σx`, `R30 = Σy`, `R31 = Σx²`, `R32 = Σy²`, `R33 = Σxy`) to $X$ observing stack lift (`Σ+` disables lift so first query overwrites $n$ in $X$ and enables lift). |
| **`x̄,ȳ`** | `{{key:↱}}` + `{{key:yˣ}}` | `x̄`, `ȳ`, `x̄w` | Each softkey places its mean ($\bar{x}$, $\bar{y}$, or $\bar{x}_w = \Sigma xy / \Sigma y$) into $X$ observing stack lift and enables stack lift. |
| **`s,σ`** | `{{key:↱}}` + `{{key:1/x}}` | `sx`, `sy`, `σx`, `σy` | Each softkey places its standard deviation ($s_x$, $s_y$ with $n - 1$, or $\sigma_x$, $\sigma_y$ with $n$) into $X$ observing stack lift and enables stack lift. |
| **`L.R.`** | `{{key:↱}}` + `{{key:LN}}` | `ŷ`, `x̂`, `r`, `m`, `b` | `ŷ` and `x̂` transform $X$ into $\hat{y}(X)$ or $\hat{x}(X)$; `r`, `m`, and `b` push Pearson $r$, slope $m$, or intercept $b$ to $X$ observing stack lift. |
| **`x?y`** | `{{key:↰}}` + `{{key:÷}}` | `x=y`, `x≠y`, `x>y`, `x<y`, `x≥y`, `x≤y` | Compares $X$ against $Y$ (`YES`/`NO` banner interactively; evaluates to `1` when true and `0` when false inside `EQN`). |
| **`x?0`** | `{{key:↱}}` + `{{key:÷}}` | `x=0`, `x≠0`, `x>0`, `x<0`, `x≥0`, `x≤0` | Compares $X$ against $0$ (`YES`/`NO` banner interactively; evaluates to `1` when true and `0` when false inside `EQN`). |
| **`POLY`** | `{{key:↱}}` + `{{key:XEQ}}` | `A`, `B`, `C`, `D`, `CLR` | Unassigned slots default to `0`; typing a value + tapping `A`–`D` stores (`•`) without `STO`/`RCL`; pressing `{{key:XEQ}}` solves cubic/quadratic (`r1` $\to Y, X$; all roots in `REGS` `STO` `R1`–`R6` / `R34`–`R39`). |
| **`TVM`** | `{{key:↰}}` + `{{key:x∥y}}` | `N`, `I%`, `PV`, `PMT`, `FV`, `END/BEG` | Unassigned slots default to `0` (`END` default); typing or computing a value + tapping a softkey stores $X$ (`STO N`, etc.); tapping immediately after another `TVM` softkey solves for that variable without `STO`, `RCL`, or `XEQ`. |
| **`EQN`** | `{{key:↱}}` + `{{key:STO}}` | `NEW`, `[1:Eq₁ … n:Eqₙ]` | Stores up to 24 RPN equations (`A`–`Z`); tapping an equation edits it, while `{{key:XEQ}}`, `{{key:SOLVE}}`, `{{key:∫}}`, and `CLEQN` evaluate, solve, integrate, or clear equations. |
| **`SOLVE`** | `{{key:↱}}` + `{{key:7}}` | `{{key:A}}`, `{{key:B}}`, `...` $\to$ `SOLVE _` | Selects stored equation and target variable (`A`–`Z` key or variable softkey; value + variable softkey stores parameter), prompts `A?`, `B?` ($\to$ `{{key:ENTER}}`/`{{key:XEQ}}`) for unassigned parameters, seeds Brent's solver from $x_0$ (default `0`), and returns $x^* \to X$. |
| **`∫`** | `{{key:↱}}` + `{{key:8}}` | `{{key:A}}`, `{{key:B}}`, `...` $\to$ `∫ _` | Integrates selected equation over $[a, b]$ in $(Y, X)$ with respect to selected variable (`A`–`Z` key or variable softkey), prompts `A?`, `B?` ($\to$ `{{key:ENTER}}`/`{{key:XEQ}}`) for unassigned parameters, and returns $(\pm\varepsilon \to Y,\; I \to X)$. |
| **`PLOT`** | `{{key:↱}}` + `{{key:x∥y}}` | `{{key:A}}`, `{{key:B}}`, `...` (`<`, `\|<-`, `OUT`, `IN`, `->\|`, `>`) | Companion App feature (excluded from physical firmware for exam compliance): plots stored equation across $[\min(Y,X), \max(Y,X)]$ (default $[-3, 3]$, or $[-10, 10]$ via `{{key:XEQ}}`), or plots `Σ+` scatter points when no equations are stored (`CLEQN`). |
| **`REGS`** | `{{key:↰}}` + `{{key:0}}` | `STACK`, `STO`, `STATS`, `DATA`, `▲`, `▼` | Read-only inspector for stack (`T,Z,Y,X,LASTX`), variables/roots (`A`–`Z`, `R1`–`R6` / `R34`–`R39`), statistical sums (`R28`–`R33`), and raw data (`R40`–`R89`). |

From any active softkey submenu, `{{key:C}}` (`EXIT`) dismisses the modal overlay and restores the six LFU telemetry slots along the bottom row without altering Register $X$ or the current stack lift state.

---

## System Flags Directory (`FLAGS` Menu & Flags `0`–`9`)

The key sequence `{{key:↱}}` + `{{key:×}}` (`FLAGS`) opens the System Flags and Configuration workspace. On the StackCalc SC-32, ten persistent system and general-purpose flags (`Flag 0` through `Flag 9`) govern instrument configuration, stack architecture, interface presentation, and rational fraction display formatting. Flags are modified interactively through the `FLAGS` toggle grid (pressing digits `0`–`9` directly on hardware/replica, or using `SF 0`–`SF 9` and `CF 0`–`CF 9` in the companion app):

| Flag # | Engine ID | Default State | Access & Control | Functional Role & Architectural Behavior |
| :---: | :---: | :---: | :--- | :--- |
| **Flag 0** | `0:F0` | `OFF` (`0`) | Digit `0` (`SF 0` / `CF 0`) | **General-Purpose Flag 0:** User-toggleable boolean flag 0 for status tracking. |
| **Flag 1** | `1:F1` | `OFF` (`0`) | Digit `1` (`SF 1` / `CF 1`) | **General-Purpose Flag 1:** Secondary user-toggleable boolean flag 1 for status tracking. |
| **Flag 2** | `2:INT` | `HRD` / `APP` | Digit `2` or `FLAGS` $\to$ `UI` | **Interface Presentation Mode:** Selects between the hardware replica bezel layout (`HRD`/`REPLICA`, `Flag 2 = ON`) and the expanded touch interface (`APP`, `Flag 2 = OFF`) on companion software platforms. |
| **Flag 3** | `3:FACE` | Theme ID | Digit `3` or `FLAGS` $\to$ `FACE` | **Visual Faceplate Selector:** Cycles the active visual faceplate palette (`RETR`, `STLH`, `NOVA`, `SPAC`, `VOYG`, `SYNT`, `ARCD`, `BLCK`) on companion software platforms without altering key coordinates or shift assignments. |
| **Flag 4** | `4:STK` | `4-LN` (`ON`) | Digit `4` or `FLAGS` $\to$ `STACK` $\to$ `VIEW` | **Stack Display Layout (`4-LN` vs. `1-LN`):** When set (`4-LN`), the LCD renders all four operational registers ($T, Z, Y, X$); when cleared (`1-LN`), the display focuses on active Register $X$. |
| **Flag 5** | `5:DEP` | `4-LVL` | Digit `5` or `FLAGS` $\to$ `STACK` (`2-LVL`, `4-LVL`, `8-LVL`, `INF`) | **Operational Stack Depth Selector:** Selects classical 4-register RPN with $T$-replication (`4-LVL`), 2-register (`2-LVL`), 8-register (`8-LVL`), or dynamic 999-level LIFO heap (`INF`). |
| **Flag 6** | `6:MOD` | `SC32` (`OFF`) | Digit `6` or `FLAGS` $\to$ `MODE` | **Instrument Architecture Profile:** Cycles the active calculator model when inside the `FLAGS` menu (`SC-32`, `SC-6`, and domain models). |
| **Flag 7** | `7:FRC` | `OFF` (`0`) | Digit `7` or `{{key:↰}}` + `{{key:.}}` (`FDISP`) | **Rational Fraction Display Mode (`FDISP`):** Toggles Register $X$ between floating-point decimal display (`OFF`) and rational mixed-fraction rendering $a\,\frac{b}{c}$ (`ON`, with default ceiling $c_{\max} = 4,095$). |
| **Flag 8** | `8:/c` | `OFF` (`0`) | Digit `8` or `FLAGS` $\to$ `MODE` | **Factor vs. Best-Fit Denominator Mode (`8:/c`):** When cleared (`OFF`, `PRECISE`), fractions use the best continued-fraction approximation with any denominator $\le c_{\max}$; when set (`ON`, `FACTORS`), fractions round to `/c` ($c_{\max}$) and reduce by $\gcd(n, c_{\max})$ so the denominator is a factor of `/c`. |
| **Flag 9** | `9:d/c` | `OFF` (`0`) | Digit `9` or `FLAGS` $\to$ `MODE` | **Fixed vs. Reduced Denominator Mode (`9:d/c`):** When cleared (`OFF`), rational fractions reduce to lowest terms; when set (`ON`, `FIXED`), fractions retain the unreduced fixed denominator `/c` ($c_{\max}$, e.g., `1 30/60`). |

In addition to individual flag toggles (`0`–`9`, `SF`, `CF`), the `FLAGS` softkey menu provides the **Sanctioned Examination Lockdown (`EXAM`)** toggle. Invoking `EXAM` executes an atomic `CLALL` memory purge (zeroing the operational stack, `LASTX`, all 26 named variables `A`–`Z`, the indirect register `i`, statistical accumulators, and stored equations) and locks the instrument into a verifiable examination compliance state until exited.

Within the symbolic Equation Bank (`{{key:EQN}}`) and interactive stack workflows, conditional piecewise branching is performed directly with the relational test menus `{{key:x?y}}` (`{{key:↰}}` + `{{key:÷}}`) and `{{key:x?0}}` (`{{key:↱}}` + `{{key:÷}}`). Interactively on the keypad, executing a relational test displays `"YES"` or `"NO"` on the status line; inside symbolic `{{key:EQN}}` expressions, each test evaluates to `1` when True and `0` when False. Multiplying two sub-expressions by complementary relational tests (such as `X A x>y` and `X A x≤y`) allows a single stored equation in `{{key:EQN}}` to switch cleanly between two physical regimes—such as Macaulay beam singularity brackets, subsonic vs. supersonic drag laws, or laminar vs. turbulent pipe friction—when evaluated via `{{key:XEQ}}`, `{{key:SOLVE}}`, or `{{key:∫}}`.