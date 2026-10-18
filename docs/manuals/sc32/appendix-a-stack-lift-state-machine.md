---
title: "Appendix A: Stack Lift State Machine Audit | SC-32 Manual"
description: "The definitive 43-key tabular audit of the StackCalc SC-32 Stack Lift State Machine, categorizing Stack Lift enablement, LASTX updates, and register delta effects."
---

# Appendix A: Stack Lift State Machine Audit

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 SPECIFICATION // APPENDIX A: STACK LIFT AUTOMATA</span>
  <span class="te-viewport-status text-sky-400">● 43-KEY HARDWARE MATRIX AUDIT &bull; LASTX TRANSITIONS &bull; REGISTER DELTA ALGEBRA</span>
</div>

{{blocks:sc32_utility_ortho|StackCalc SC-32 Hardware Architecture}}
*Figure A.1: Orthogonal engineering projection of the StackCalc SC-32 hardware architecture and operational interface.*

<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>{{key:ALL}}</code> (Full 12-digit scientific mantissa; Standard Base-10 Arithmetic; Degrees angular mode default).
</div>

---

## Theoretical Foundation of Stack Lift

In Reverse Polish Notation (RPN), the four operational registers—designated **$X$ (Bottom/Display)**, **$Y$ (Second)**, **$Z$ (Third)**, and **$T$ (Top)**—are governed by an autonomous finite state machine known as the **Stack Lift Automaton**. 

Unlike algebraic calculators that require dynamic operator precedence stacks and recursive parenthesis parsing trees, an RPN architecture maintains execution immediacy: every keystroke maps directly to a deterministic state transition in constant time $\mathcal{O}(1)$. Rooted in the classic Corvallis engineering specifications of the HP-15C and HP-32SII {{cite:hp15c1982,hp32sii1991}}, this state machine eliminates ambiguity while providing complete computational transparency.

<div class="admonition note">
<p class="admonition-title">Stack Lift Transition Diagram</p>

| Current State | Triggering Keystroke Class | Next State | Stack Register Effect |
| :--- | :--- | :--- | :--- |
| **LIFT ARMED** (`Lift = TRUE`) | First digit (`{{key:0}}`–`{{key:9}}`, `{{key:.}}`) | **EDIT BUFFER** | Pushes stack up (`X → Y → Z → T`) before writing new digit |
| **EDIT BUFFER** (In Progress) | Any function/operator (`{{key:+}}`, `{{key:×}}`, `{{key:√x}}`) | **LIFT ARMED** (`Lift = TRUE`) | Terminates digit entry, evaluates result into `X`, and arms stack lift |
| **EDIT BUFFER** or **LIFT ARMED** | `{{key:ENTER}}`, `{{key:CLx}}`, `{{key:Σ+}}` | **LIFT DISABLED** (`Lift = FALSE`) | Next digit typed will overwrite `X` in place without lifting `Y` |
| **LIFT DISABLED** (`Lift = FALSE`) | `{{key:x⇄y}}`, `{{key:R↓}}`, `{{key:R↑}}`, or operator | **LIFT ARMED** (`Lift = TRUE`) | Re-arms stack lift for subsequent numeric entry |

</div>

### The Three State Categories

At any discrete operational moment, the calculator's internal control register holds a single boolean flag: `stackLiftEnabled`. This flag dictates the stack's reaction when the user initiates numeric data entry:

1. **Enables Stack Lift (`stackLiftEnabled = true`):**
   * Subsequent numeric keypresses (digits `0`–`9`, decimal point `.`, or `E`) push the entire stack upward before writing the new digit into Register $X$.
   * Register movement: $T \leftarrow Z$, $Z \leftarrow Y$, $Y \leftarrow X$, and $X \leftarrow \text{digit}$.
   * The former Top register ($T$) is discarded off the top of the stack.
   * This is the default armed state produced by nearly all mathematical functions (`+`, `-`, `×`, `÷`, `√x`, `SIN`, `LN`, etc.) and stack rolls (`{{key:R↓}}`, `{{key:R↑}}`, `{{key:x⇄y}}`).

2. **Disables Stack Lift (`stackLiftEnabled = false`):**
   * Subsequent numeric keypresses overwrite Register $X$ directly **without** pushing the upper registers upward.
   * Register movement: $X \leftarrow \text{digit}$, while $Y$, $Z$, and $T$ remain completely undisturbed.
   * This state is deliberately established by `{{key:ENTER}}`, `{{key:CLx}}` (Clear X), and statistical accumulation `{{key:Σ+}}`.
   * **The Pedagogical Invariant:** The `{{key:ENTER}}` key duplicates $X$ into $Y$ ($Y \leftarrow X$) and immediately disables stack lift so that the very next number keyed replaces the duplicate in $X$ while preserving the operand in $Y$.

3. **Preserves Stack Lift (`stackLiftEnabled` unchanged):**
   * Non-operational or modifier keystrokes (such as prefix keys `{{key:↰}}` and `{{key:↱}}`, `{{key:STO}}`, `{{key:+/-}}`, and `{{key:E}}`) leave the state of the stack lift flag unaltered.

> [!NOTE]
> The Stack Lift Automaton guarantees that intermediate results never need to be explicitly saved or parenthesized. Understanding whether an operation enables or disables stack lift eliminates 100% of operand duplication errors.

---

{{res:sc32_hero_stack:screenshot|StackCalc SC-32 Four-Level RPN Stack Display}}

## Definitive 43-Key Physical Matrix Audit Table

The table below catalogs all 43 physical switch positions of the SC-32 hardware keypad, documenting their electrical scan coordinates, primary function, stack lift effect, whether `LASTX` is updated, and the exact register transformation:

| Key Position | Primary Legend | Stack Lift Status | Updates LASTX? | Register Delta Transformation | Operational Description |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Row 0, Col 0** | `{{key:LFU0}}` | Preserves | No | Context dependent | Softkey Menu Item 1 / Dynamic LFU Slot 1 |
| **Row 0, Col 1** | `{{key:LFU1}}` | Preserves | No | Context dependent | Softkey Menu Item 2 / Dynamic LFU Slot 2 |
| **Row 0, Col 2** | `{{key:LFU2}}` | Preserves | No | Context dependent | Softkey Menu Item 3 / Dynamic LFU Slot 3 |
| **Row 0, Col 3** | `{{key:LFU3}}` | Preserves | No | Context dependent | Softkey Menu Item 4 / Dynamic LFU Slot 4 |
| **Row 0, Col 4** | `{{key:LFU4}}` | Preserves | No | Context dependent | Softkey Menu Item 5 / Dynamic LFU Slot 5 |
| **Row 0, Col 5** | `{{key:LFU5}}` | Preserves | No | Context dependent | Softkey Menu Item 6 / Dynamic LFU Slot 6 |
| **Row 1, Col 0** | `{{key:√x}}` | **Enables** | **Yes** | $X \leftarrow \sqrt{X}; Y, Z, T \text{ unch}$ | Unary square root; captures prior $X$ |
| **Row 1, Col 1** | `{{key:eˣ}}` | **Enables** | **Yes** | $X \leftarrow e^X; Y, Z, T \text{ unch}$ | Unary natural exponential; captures prior $X$ |
| **Row 1, Col 2** | `{{key:LN}}` | **Enables** | **Yes** | $X \leftarrow \ln X; Y, Z, T \text{ unch}$ | Unary natural logarithm; captures prior $X$ |
| **Row 1, Col 3** | `{{key:yˣ}}` | **Enables** | **Yes** | $X \leftarrow Y^X; Y \leftarrow Z; Z \leftarrow T; T \leftarrow T$ | Dyadic power; stack drops; $T$ replicated |
| **Row 1, Col 4** | `{{key:1/x}}` | **Enables** | **Yes** | $X \leftarrow 1/X; Y, Z, T \text{ unch}$ | Unary reciprocal; captures prior $X$ |
| **Row 1, Col 5** | `{{key:Σ+}}` | **Disables** | No (Preserved) | $X \leftarrow n; Y, Z, T \text{ unch}; \Sigma \text{ accums updated}$ | Statistical data accumulation; disables lift |
| **Row 2, Col 0** | `{{key:STO}}` | Preserves | No | $X \to \text{Var}[k]; \text{Stack unch}$ | Store $X$ into designated variable |
| **Row 2, Col 1** | `{{key:RCL}}` | **Enables** | No | $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X; X \leftarrow \text{Var}[k]$ | Recall variable $k$ (pushes stack upward) |
| **Row 2, Col 2** | `{{key:R↓}}` | **Enables** | No | $X \leftarrow Y; Y \leftarrow Z; Z \leftarrow T; T \leftarrow X$ | Roll stack down (circular rotation) |
| **Row 2, Col 3** | `{{key:SIN}}` | **Enables** | **Yes** | $X \leftarrow \sin X; Y, Z, T \text{ unch}$ | Trigonometric sine in active angular mode |
| **Row 2, Col 4** | `{{key:COS}}` | **Enables** | **Yes** | $X \leftarrow \cos X; Y, Z, T \text{ unch}$ | Trigonometric cosine in active angular mode |
| **Row 2, Col 5** | `{{key:TAN}}` | **Enables** | **Yes** | $X \leftarrow \tan X; Y, Z, T \text{ unch}$ | Trigonometric tangent in active angular mode |
| **Row 3, Col 0-1**| `{{key:ENTER}}` | **Disables** | No | $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X; X \leftarrow X$ | Duplicate $X \to Y$; disable stack lift |
| **Row 3, Col 2** | `{{key:x⇄y}}` | **Enables** | No | $X \leftarrow Y; Y \leftarrow X; Z, T \text{ unch}$ | Exchange Registers $X$ and $Y$ |
| **Row 3, Col 3** | `{{key:+/-}}` | Preserves | No | $X \leftarrow -X; Y, Z, T \text{ unch}$ | Toggle arithmetic sign of active number |
| **Row 3, Col 4** | `{{key:E}}` | Preserves | No | Arms scientific exponent entry buffer | Exponent entry separator |
| **Row 3, Col 5** | `{{key:<-}}` | Preserves | No | Deletes trailing character from buffer | Backspace digit editor |
| **Row 4, Col 0** | `{{key:XEQ}}` | Preserves | No | Context dependent | Execute designated program or equation |
| **Row 4, Col 1** | `{{key:7}}` | (Consumes Lift)| No | If Lift: $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X$; $X \leftarrow 7$ | Digit input 7 |
| **Row 4, Col 2** | `{{key:8}}` | (Consumes Lift)| No | If Lift: $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X$; $X \leftarrow 8$ | Digit input 8 |
| **Row 4, Col 3** | `{{key:9}}` | (Consumes Lift)| No | If Lift: $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X$; $X \leftarrow 9$ | Digit input 9 |
| **Row 4, Col 4** | `{{key:÷}}` | **Enables** | **Yes** | $X \leftarrow Y \div X; Y \leftarrow Z; Z \leftarrow T; T \leftarrow T$ | Dyadic division; stack drops; $T$ replicated |
| **Row 5, Col 0** | `{{key:↰}}` (Left Shift) | Preserves | No | Arms left-shifted alternate functions | Primary shift prefix modifier |
| **Row 5, Col 1** | `{{key:4}}` | (Consumes Lift)| No | If Lift: $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X$; $X \leftarrow 4$ | Digit input 4 |
| **Row 5, Col 2** | `{{key:5}}` | (Consumes Lift)| No | If Lift: $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X$; $X \leftarrow 5$ | Digit input 5 |
| **Row 5, Col 3** | `{{key:6}}` | (Consumes Lift)| No | If Lift: $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X$; $X \leftarrow 6$ | Digit input 6 |
| **Row 5, Col 4** | `{{key:×}}` | **Enables** | **Yes** | $X \leftarrow Y \times X; Y \leftarrow Z; Z \leftarrow T; T \leftarrow T$ | Dyadic multiplication; stack drops |
| **Row 6, Col 0** | `{{key:↱}}` (Right Shift) | Preserves | No | Arms right-shifted alternate functions | Secondary shift prefix modifier |
| **Row 6, Col 1** | `{{key:1}}` | (Consumes Lift)| No | If Lift: $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X$; $X \leftarrow 1$ | Digit input 1 |
| **Row 6, Col 2** | `{{key:2}}` | (Consumes Lift)| No | If Lift: $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X$; $X \leftarrow 2$ | Digit input 2 |
| **Row 6, Col 3** | `{{key:3}}` | (Consumes Lift)| No | If Lift: $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X$; $X \leftarrow 3$ | Digit input 3 |
| **Row 6, Col 4** | `{{key:-}}` | **Enables** | **Yes** | $X \leftarrow Y - X; Y \leftarrow Z; Z \leftarrow T; T \leftarrow T$ | Dyadic subtraction; stack drops |
| **Row 7, Col 0** | `{{key:C}}` (ON) | **Disables** | No | Clears active entry or dismisses error | Clear entry / Hardware power wake |
| **Row 7, Col 1** | `{{key:0}}` | (Consumes Lift)| No | If Lift: $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X$; $X \leftarrow 0$ | Digit input 0 |
| **Row 7, Col 2** | `{{key:.}}` | (Consumes Lift)| No | If Lift: $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X$; $X \leftarrow 0.$ | Decimal radix point input |
| **Row 7, Col 3** | `{{key:x∥y}}` | **Enables** | **Yes** | $X \leftarrow \frac{Y \times X}{Y + X}; Y \leftarrow Z; Z \leftarrow T; T \leftarrow T$ | Dyadic parallel harmonic operator; drops |
| **Row 7, Col 4** | `{{key:+}}` | **Enables** | **Yes** | $X \leftarrow Y + X; Y \leftarrow Z; Z \leftarrow T; T \leftarrow T$ | Dyadic addition; stack drops; $T$ replicated |

---

## Shifted Operations & Menu Audit

Every shifted key on the SC-32 adheres strictly to the Stack Lift Automaton. The tables below catalog all left-shifted (`{{key:↰}}`, Yellow Primary) and right-shifted (`{{key:↱}}`, Blue Secondary) operations, noting intentional deviations from the vintage HP-32SII:

### Table A.1: Left-Shifted Operations (`{{key:↰}}`, Yellow Primary)

| Shifted Combination | Function Name | Stack Lift Status | Updates LASTX? | Register Delta Transformation | Notes & Deviations |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `{{key:√x}}` | `x²` | **Enables** | **Yes** | $X \leftarrow X^2; Y, Z, T \text{ unch}$ | Unary square |
| `{{key:eˣ}}` | `10ˣ` | **Enables** | **Yes** | $X \leftarrow 10^X; Y, Z, T \text{ unch}$ | Unary common exponential |
| `{{key:LN}}` | `LOG` | **Enables** | **Yes** | $X \leftarrow \log_{10} X; Y, Z, T \text{ unch}$ | Unary common logarithm |
| `{{key:yˣ}}` | `ˣ√y` | **Enables** | **Yes** | $X \leftarrow Y^{1/X}; Y \leftarrow Z; Z \leftarrow T; T \leftarrow T$ | Dyadic $x$-th root of $y$; stack drops |
| `{{key:1/x}}` | `x!` | **Enables** | **Yes** | $X \leftarrow \Gamma(X+1); Y, Z, T \text{ unch}$ | Factorial / Gamma function |
| `{{key:Σ+}}` | `Σ-` | **Disables** | No (Preserved) | $X \leftarrow n-1; Y, Z, T \text{ unch}; \Sigma \text{ decremented}$ | Statistical correction; disables lift |
| `{{key:SIN}}` | `ASIN` | **Enables** | **Yes** | $X \leftarrow \arcsin X; Y, Z, T \text{ unch}$ | Inverse sine in active angular mode |
| `{{key:COS}}` | `ACOS` | **Enables** | **Yes** | $X \leftarrow \arccos X; Y, Z, T \text{ unch}$ | Inverse cosine in active angular mode |
| `{{key:TAN}}` | `ATAN` | **Enables** | **Yes** | $X \leftarrow \arctan X; Y, Z, T \text{ unch}$ | Inverse tangent in active angular mode |
| `{{key:x⇄y}}` | `LASTX` | **Enables** | No | $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X; X \leftarrow \text{LASTX}$ | Recalls prior $X$; pushes stack upward |
| `{{key:+/-}}` | `MODES` | Preserves | No | Menu: `DEG`, `RAD`, `GRAD`, `.`, `,` | Modal angular and radix settings |
| `{{key:E}}` | `DISP` | Preserves | No | Menu: `FIX n`, `SCI n`, `ENG n`, `ALL` | Non-destructive display precision |
| `{{key:<-}}` | `CLEAR` | Preserves | No | Menu: `CLEQN`, `CLVARS`, `CLALL`, `CLΣ`, `CLREGS`, `CLSTK` | Selective memory wipe menu |
| `{{key:÷}}` | `x?y` | Preserves | No | Comparison menu: `x=y`, `x≠y`, `x>y`, etc. | Conditional branching tests |
| `{{key:×}}` | `BASE` | Preserves | No | Menu: `HEX`, `DEC`, `OCT`, `BIN` | Integer base switching menu |
| `{{key:-}}` | `->POL` | **Enables** | **Yes** | $X \leftarrow \sqrt{X^2+Y^2}; Y \leftarrow \text{atan2}(Y, X); Z, T \text{ unch}$ | Rectangular to polar conversion |
| `{{key:+}}` | `LBL` | Preserves | No | Prompts for equation label letter | Restored intentional deviation |
| `{{key:0}}` | `REGS` | Preserves | No | Displays register viewer table | Restored intentional deviation |
| `{{key:.}}` | `FDISP` | Preserves | No | Toggles fraction display mode (Flag 7) | Educational fraction representation |
| `{{key:x∥y}}` | `TVM` | Preserves | No | Opens 5-variable TVM workspace | `YELLOW + x∥y` deviation |

### Table A.2: Right-Shifted Operations (`{{key:↱}}`, Blue Secondary)

| Shifted Combination | Function Name | Stack Lift Status | Updates LASTX? | Register Delta Transformation | Notes & Deviations |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `{{key:√x}}` | `PARTS` | Preserves | No | Menu: `IP`, `FP`, `ABS`, `SGN`, `GCD`, `LCM` | Number theory and decomposition |
| `{{key:eˣ}}` | `PROB` | Preserves | No | Menu: `Cn,r`, `Pn,r`, `x!`, `RAND` | Combinatorics and probability |
| `{{key:LN}}` | `L.R.` | Preserves | No | Menu: `ŷ`, `x̂`, `r`, `m`, `b` | Linear regression estimates & slope |
| `{{key:yˣ}}` | `x̄,ȳ` | Preserves | No | Menu: `x̄`, `ȳ`, `x̄w` | Sample and weighted means |
| `{{key:1/x}}` | `s,σ` | Preserves | No | Menu: `sx`, `sy`, `σx`, `σy` | Sample and population std dev |
| `{{key:Σ+}}` | `SUMS` | Preserves | No | Menu: `Σx`, `Σy`, `Σx²`, `Σy²`, `Σxy`, `n` | Statistical accumulator viewer |
| `{{key:R↓}}` | `R↑` | **Enables** | No | $X \leftarrow T; Y \leftarrow X; Z \leftarrow Y; T \leftarrow Z$ | Circular roll stack upward |
| `{{key:SIN}}` | `HYP` | Preserves | No | Sets hyperbolic prefix flag | Arms hyperbolic evaluation |
| `{{key:x⇄y}}` | `SHOW` | Preserves | No | Renders 15-digit internal mantissa | Non-destructive temporary peek |
| `{{key:+/-}}` | `&#124;x&#124;` | **Enables** | **Yes** | $X \leftarrow \lvert X\rvert; Y, Z, T \text{ unch}$ | Absolute value (HP32SII deviation) |
| `{{key:E}}` | `÷R` | **Enables** | **Yes** | $X \leftarrow \lfloor Y/X \rfloor; Y \leftarrow \text{rem}(Y, X); Z \leftarrow T; T \leftarrow T$ | Integer division & remainder (Deviation) |
| `{{key:<-}}` | *(None)* | Preserves | No | Unassigned | Deliberate blank slot (Deviation) |
| `{{key:XEQ}}` | `POLY` | Preserves | No | Dynamic cubic solver workspace (`A B C D EXEC CLR`)| Restored intentional deviation |
| `{{key:÷}}` | `x?0` | Preserves | No | Comparison menu: `x=0`, `x≠0`, `x>0`, etc. | Zero-relative comparison tests |
| `{{key:×}}` | `FLAGS` | Preserves | No | Menu: `SF n`, `CF n`, `FS? n`, `4-LVL`, `8-LVL`, `INF` | System flags & stack size |
| `{{key:-}}` | `->REC` | **Enables** | **Yes** | $X \leftarrow X\cos Y; Y \leftarrow X\sin Y; Z, T \text{ unch}$ | Polar to rectangular conversion |
| `{{key:0}}` | `CMPLX` | Preserves | No | Sets one-shot complex evaluator prefix | Arms Gaussian plane arithmetic |
| `{{key:.}}` | `/c` | Preserves | No | Sets maximum fraction denominator | Denominator limiter (e.g. 16 for /16) |
| `{{key:x∥y}}` | `PLOT` | Preserves | No | Enters graphic curve and scatter plotter | Graphic LCD vector plot engine |

---

## The Formal Register Delta Algebra

To verify calculation pipelines with mathematical certainty, the effect of any operator $\Omega$ on the four-register stack $\mathbf{S} = [X, Y, Z, T]^T$ is expressed as a matrix or functional transformation $\mathbf{S}' = \mathbf{f}_\Omega(\mathbf{S})$.

### Unary Operators ($f(X)$)
Unary functions include `{{key:√x}}`, `{{key:1/x}}`, `{{key:eˣ}}`, `{{key:LN}}`, `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`, `{{key:x²}}`, `{{key:10ˣ}}`, `{{key:LOG}}`, `{{key:x!}}`, and `{{key:|x|}}`:
$$\begin{bmatrix} X' \\ Y' \\ Z' \\ T' \end{bmatrix} = \begin{bmatrix} f(X) \\ Y \\ Z \\ T \end{bmatrix}, \quad \text{LASTX}' = X, \quad \text{Lift}' = \text{TRUE}$$

### Dyadic Operators ($f(Y, X)$)
Standard binary operators include `{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`, `{{key:yˣ}}`, `{{key:ˣ√y}}`, and `{{key:x∥y}}`:
$$\begin{bmatrix} X' \\ Y' \\ Z' \\ T' \end{bmatrix} = \begin{bmatrix} f(Y, X) \\ Z \\ T \\ T \end{bmatrix}, \quad \text{LASTX}' = X, \quad \text{Lift}' = \text{TRUE}$$

> [!IMPORTANT]
> **The Top-Register Constant Replication Invariant:** Observe that during any dyadic operation, Register $T$ drops into $Z$, while $T$ retains its original value ($T' \leftarrow T$). This structural invariant allows a constant stored in $T$ to be reused indefinitely across an unbounded series of operations without re-entry!

### Circular Stack Rotations
Rotations rearrange registers without altering numerical values or updating `LASTX`:
* **Roll Down (`{{key:R↓}}`):**
  $$\begin{bmatrix} X' \\ Y' \\ Z' \\ T' \end{bmatrix} = \begin{bmatrix} Y \\ Z \\ T \\ X \end{bmatrix}, \quad \text{LASTX}' = \text{LASTX}, \quad \text{Lift}' = \text{TRUE}$$
* **Roll Up (`{{key:R↑}}`):**
  $$\begin{bmatrix} X' \\ Y' \\ Z' \\ T' \end{bmatrix} = \begin{bmatrix} T \\ X \\ Y \\ Z \end{bmatrix}, \quad \text{LASTX}' = \text{LASTX}, \quad \text{Lift}' = \text{TRUE}$$
* **Exchange $X$ and $Y$ (`{{key:x⇄y}}`):**
  $$\begin{bmatrix} X' \\ Y' \\ Z' \\ T' \end{bmatrix} = \begin{bmatrix} Y \\ X \\ Z \\ T \end{bmatrix}, \quad \text{LASTX}' = \text{LASTX}, \quad \text{Lift}' = \text{TRUE}$$

### Stack Elevator (`{{key:ENTER}}`)
The `{{key:ENTER}}` operation pushes the stack while replicating $X$ into $Y$:
$$\begin{bmatrix} X' \\ Y' \\ Z' \\ T' \end{bmatrix} = \begin{bmatrix} X \\ X \\ Y \\ Z \end{bmatrix}, \quad \text{LASTX}' = \text{LASTX}, \quad \text{Lift}' = \text{FALSE}$$

---

## Twelve Comprehensive Stack Lift Trace Walkthroughs

The following fully traced pedagogical scenarios demonstrate how the Stack Lift Automaton behaves across real-world operational challenges.

### Trace 1: Chained Arithmetic Without Intermediary `{{key:ENTER}}`
Calculate: $(14 \times 25) + (36 \times 48)$

| Step | Keystroke | Stack Lift Flag | Register X | Register Y | Register Z | Register T | Pedagogical Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:1}} {{key:4}}` | Armed (True) | `14` | `0` | `0` | `0` | First operand keyed |
| 2 | `{{key:ENTER}}` | **Disarmed (False)**| `14` | `14` | `0` | `0` | Stack pushed; $X$ copied to $Y$; lift disabled |
| 3 | `{{key:2}} {{key:5}}` | Inactive | `25` | `14` | `0` | `0` | Overwrites $X$; $Y$ preserved |
| 4 | `{{key:×}}` | **Armed (True)** | `350` | `0` | `0` | `0` | $14 \times 25 = 350$; stack drops; lift armed! |
| 5 | `{{key:3}} {{key:6}}` | Inactive | `36` | `350` | `0` | `0` | **No ENTER needed!** Armed lift pushes `350` into $Y$ |
| 6 | `{{key:ENTER}}` | **Disarmed (False)**| `36` | `36` | `350` | `0` | Pushes `350` into $Z$; lift disabled |
| 7 | `{{key:4}} {{key:8}}` | Inactive | `48` | `36` | `350` | `0` | Overwrites $X$; registers $Y$ and $Z$ preserved |
| 8 | `{{key:×}}` | **Armed (True)** | `1728` | `350` | `0` | `0` | $36 \times 48 = 1728$; $Z$ drops to $Y$ |
| 9 | `{{key:+}}` | **Armed (True)** | `2078` | `0` | `0` | `0` | $350 + 1728 = 2078$; final sum in $X$ |

---

### Trace 2: The `{{key:ENTER}}` Lift-Disable Invariant
Demonstrating why pressing `{{key:ENTER}}` prevents accidental stack duplication.

| Step | Keystroke | Stack Lift Flag | Register X | Register Y | Register Z | Register T | Pedagogical Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:5}} {{key:0}}` | Armed (True) | `50` | `0` | `0` | `0` | Base value entered |
| 2 | `{{key:ENTER}}` | **Disarmed (False)**| `50` | `50` | `0` | `0` | Lift disarmed; $X$ duplicated |
| 3 | `{{key:8}}` | Inactive | `8` | `50` | `0` | `0` | Digit `8` replaces $X$ directly without push |
| 4 | `{{key:+}}` | **Armed (True)** | `58` | `0` | `0` | `0` | Addition yields 58; lift re-armed |

---

### Trace 3: `{{key:LASTX}}` Dyadic Operator Correction
The user intends to compute $100 \times 8 = 800$, but accidentally hits `{{key:÷}}`, producing $12.5$. The error is corrected instantly without re-keying $100$ or $8$:

| Step | Keystroke | Stack Lift Flag | Register X | Register Y | LASTX | Pedagogical Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:1}} {{key:0}} {{key:0}} {{key:ENTER}}`| False | `100` | `100` | `0` | Operands staged |
| 2 | `{{key:8}} {{key:÷}}` | True | `12.5000` | `0` | `8` | Error: Divided instead of multiplied! |
| 3 | {{key:LASTX}} | True | `8` | `12.5000` | `8` | Recalls operand `8` that caused the operation |
| 4 | `{{key:×}}` | True | `100.0000` | `0` | `8` | Multiplies $12.5 \times 8$ to recover original numerator $100$ |
| 5 | {{key:LASTX}} | True | `8` | `100.0000` | `8` | Recalls operand `8` once more |
| 6 | `{{key:×}}` | True | `800.0000` | `0` | `8` | Multiplies $100 \times 8$ to achieve intended target $800$ |

---

### Trace 4: `{{key:CLx}}` Stack Lift Disabling
Demonstrating how `{{key:CLx}}` clears an erroneous entry without collapsing or dropping upper registers:

| Step | Keystroke | Stack Lift Flag | Register X | Register Y | Register Z | Pedagogical Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:1}} {{key:5}} {{key:0}} {{key:ENTER}}`| False | `150` | `150` | `0` | Operand staged |
| 2 | `{{key:9}} {{key:9}} {{key:9}}` | Inactive | `999` | `150` | `0` | User mistypes second operand |
| 3 | `{{key:CLEAR}} {{key:CLx}}` | **Disarmed (False)**| `0` | `150` | `0` | `{{key:CLx}}` zeroes $X$ and sets Lift = FALSE |
| 4 | `{{key:2}} {{key:5}}` | Inactive | `25` | `150` | `0` | Typing `25` overwrites zero directly |
| 5 | `{{key:-}}` | True | `125` | `0` | `0` | $150 - 25 = 125$ |

---

### Trace 5: Unary Function Lift Re-arming
Unary functions compute instantly on Register $X$ and re-arm stack lift so subsequent inputs push automatically:

| Step | Keystroke | Stack Lift Flag | Register X | Register Y | Pedagogical Notes |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `{{key:1}} {{key:6}}` | Armed | `16` | `0` | Raw value entered |
| 2 | `{{key:√x}}` | **Armed (True)** | `4` | `0` | $\sqrt{16} = 4$; Lift flag armed |
| 3 | `{{key:9}}` | Inactive | `9` | `4` | Inputting `9` triggers lift push! $4 \to Y$ |
| 4 | `{{key:+}}` | Armed | `13` | `0` | $4 + 9 = 13$ |

---

### Trace 6: Constant Factor Calculation via T-Replication
Compute sales tax ($8.25\%$, multiplier $1.0825$) on three amounts: $\$15.00$, $\$24.50$, and $\$80.00$:

| Step | Keystroke | Register X | Register Y | Register Z | Register T | Pedagogical Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:1}} {{key:.}} {{key:0}} {{key:8}} {{key:2}} {{key:5}}` | `1.0825` | `0` | `0` | `0` | Tax factor keyed |
| 2 | `{{key:ENTER}} {{key:ENTER}} {{key:ENTER}}` | `1.0825` | `1.0825` | `1.0825` | `1.0825` | Stack flooded with factor |
| 3 | `{{key:1}} {{key:5}} {{key:×}}` | `16.2375` | `1.0825` | `1.0825` | **`1.0825`**| $15 \times 1.0825$; $T$ replicates into $Z$ and $Y$! |
| 4 | `{{key:C}} {{key:2}} {{key:4}} {{key:.}} {{key:5}} {{key:×}}` | `26.5213` | `1.0825` | `1.0825` | **`1.0825`**| `C` clears $X$ (disabling lift); $24.5 \times 1.0825$; $T$ replicates! |
| 5 | `{{key:C}} {{key:8}} {{key:0}} {{key:×}}` | `86.6000` | `1.0825` | `1.0825` | **`1.0825`**| `C` clears $X$; $80 \times 1.0825$; constant remains active! |

---

### Trace 7: Statistical Accumulation `{{key:Σ+}}` and Non-Destructive Stack Isolation
Entering pairs $(x, y) = (10, 25)$ into statistical memory:

| Step | Keystroke | Stack Lift Flag | Register X | Register Y | Stat Register $n$ | Pedagogical Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:2}} {{key:5}} {{key:ENTER}}` | False | `25` | `25` | `0` | $y$-coordinate pushed to $Y$ |
| 2 | `{{key:1}} {{key:0}}` | Inactive | `10` | `25` | `0` | $x$-coordinate keyed into $X$ |
| 3 | `{{key:Σ+}}` | **Disarmed (False)**| `1` | `25` | `1` | Registers $X$ shows sample count $n=1$; lift disabled |
| 4 | `{{key:3}} {{key:5}}` | Inactive | `35` | `25` | `1` | Next $y$ overwrites $X$ directly without stack lift! |

---

### Trace 8: Complex Number Evaluation via {{key:CMPLX}}
Compute $(3 + 4i) + (5 - 2i)$:

| Step | Keystroke | Register X | Register Y | Register Z | Register T | Pedagogical Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:3}} {{key:ENTER}} {{key:4}}` | `4` (Imag) | `3` (Real) | `0` | `0` | First complex number staged in $(Y, X)$ |
| 2 | `{{key:ENTER}}` | `4` | `4` | `3` | `0` | Single `ENTER` lifts $(3, 4)$ to $(Z, Y)$ and disables lift |
| 3 | `{{key:5}} {{key:ENTER}} {{key:2}} {{key:+/-}}`| `-2` | `5` | `4` | `3` | `5` overwrites $X$; `ENTER 2 +/-` lifts $(3, 4)$ to $(T, Z)$! |
| 4 | `{{key:CMPLX}} {{key:+}}` | `2` (Imag) | `8` (Real) | `3` | `3` | Vector sum: $(3+5) + (4-2)i = 8 + 2i$; $T$ replicates into $Z, T$ |

---

### Trace 9: Parallel Resistance via Primary `{{key:x∥y}}`
Calculate parallel equivalent of $30\,\Omega$ and $60\,\Omega$:

| Step | Keystroke | Register X | Register Y | Register Z | Pedagogical Notes |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `{{key:3}} {{key:0}} {{key:ENTER}}` | `30` | `30` | `0` | First resistor staged |
| 2 | `{{key:6}} {{key:0}}` | `60` | `30` | `0` | Second resistor keyed |
| 3 | `{{key:x∥y}}` | `20.0000` | `0` | `0` | Single-keystroke harmonic calculation: $\frac{30 \times 60}{30 + 60} = 20\,\Omega$ |

---

### Trace 10: Integer Division with Remainder `{{key:E}}` (`÷R`)
Divide $29$ by $6$ to find quotient and integer remainder:

| Step | Keystroke | Register X | Register Y | Register Z | Pedagogical Notes |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `{{key:2}} {{key:9}} {{key:ENTER}}` | `29` | `29` | `0` | Dividend staged in $Y$ |
| 2 | `{{key:6}}` | `6` | `29` | `0` | Divisor in $X$ |
| 3 | `{{key:E}}` (` {{key:÷}} R`) | `4` (Quotient) | `5` (Remainder) | `0` | $29 = 4 \times 6 + 5$; quotient in $X$, remainder in $Y$ |

---

### Trace 11: Absolute Value `{{key:+/-}}` (`|x|`)
Compute $|-45.75|$:

| Step | Keystroke | Register X | Register Y | Pedagogical Notes |
| :---: | :--- | :---: | :---: | :--- |
| 1 | `{{key:4}} {{key:5}} {{key:.}} {{key:7}} {{key:5}} {{key:+/-}}`| `-45.75` | `0` | Negative operand entered |
| 2 | `{{key:+/-}}` (`&#124;x&#124;`) | `45.75` | `0` | Instant absolute value; stack lift armed |
| 3 | `{{key:1}} {{key:0}} {{key:×}}` | `457.50` | `0` | Multiplies without needing `{{key:ENTER}}` |

---

### Trace 12: Dynamic Stack Depth Expansion (`4-LVL` vs `8-LVL` vs `INF`)
Under extended system flags (`{{key:FLAGS}}`), the user can expand the stack beyond 4 levels:
* **`4-LVL` (Classic HP):** 4 registers ($X, Y, Z, T$). $T$ replicated on drop; values pushed off $T$ are discarded.
* **`8-LVL` (Extended STEM):** 8 registers ($X, Y, Z, T, A, B, C, D$). Deeper parenthetical evaluations can occur without variable storage. $D$ replicated on drop.
* **`INF` (Infinite Dynamic):** Dynamic heap allocation. Stack grows unboundedly until system memory limit. Stack drop pulls previous elements down without replication.

<div class="admonition note">
<p class="admonition-title">Stack Depth Architecture Comparison</p>

| Level | 4-Level Stack (`4-LVL`) | 8-Level Stack (`8-LVL`) | Infinite Stack (`INF`) |
| :--- | :--- | :--- | :--- |
| **Top / Level 8** | — | `D:` Level 8 Register | Dynamic Heap Top ($N$) |
| **Level 7** | — | `C:` Level 7 Register | $\dots$ |
| **Level 6** | — | `B:` Level 6 Register | Level 5 Register |
| **Level 5** | — | `A:` Level 5 Register | Level 4 Register |
| **Level 4** | `T:` Constant Replicator | `T:` Level 4 Register | Level 3 Register |
| **Level 3** | `Z:` Third Operative | `Z:` Level 3 Register | Level 2 Register |
| **Level 2** | `Y:` Second Operative | `Y:` Level 2 Register | Level 1 Register |
| **Level 1 (Display)** | `X:` Primary Display | `X:` Level 1 (Display) | Level 0 (Primary Display) |

</div>

---

## Verification & Implementation Invariants

Every state transition of the Stack Lift Automaton—including `Neutral`, `LiftEnabled`, `LiftDisabled`, and `BuildingNumber` transitions across all 43 physical keys and shifted operations—is continuously verified against classical Hewlett-Packard RPN register semantics and deterministic firmware regression suites.
