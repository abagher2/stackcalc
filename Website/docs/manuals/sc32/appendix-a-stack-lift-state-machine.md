---
title: "Appendix A: Formal Stack-Lift State Machine | Thinking in the Stack (SC-32)"
description: "The definitive 43-key tabular reference for the StackCalc SC-32 Stack Lift State Machine, categorizing Stack Lift enablement, LASTX updates, and register delta effects."
---

# Appendix A: Formal Stack-Lift State Machine

## State-Machine Architecture & Register Transitions

The four operational registers ($X, Y, Z, T$) of a Reverse Polish Notation (RPN) processor form a four-register last-in, first-out (LIFO) evaluation stack, with $X$ as the active bottom display register, $Y$ as the second operative register, $Z$ as the third, and $T$ as the top constant register.

Across the four-register stack, every completed result resides in the primary working register, Register $X$, while intermediate subtotals wait in the upper registers ($Y, Z, T$). In an ordinary algebraic calculator, the display register is passive: if you want to compute $(14 \times 25) + (36 \times 48)$, you must either open nested parentheses or copy `350` onto scratch paper before typing `36`. On the SC-32, Register $X$ is governed by a deterministic George H. Mealy (1955) finite-state automaton $(Q, \Sigma, \Delta, \delta, \lambda)$ called the Stack Lift Automaton. Its internal state set $Q = \{\text{EDIT}, \text{ARMED}, \text{DISABLED}\}$ and keystroke alphabet $\Sigma$ jointly determine both the next state $\delta(q, \sigma)$ and the immediate register transformation $\lambda(q, \sigma)$ in $\mathcal{O}(1)$ time:

* **Building a Number (`EDIT` / Digit Entry Active):** While you are tapping digits (`{{key:3}}`, `{{key:6}}`, `{{key:.}}`, `{{key:5}}`), characters append directly to the active input buffer in Register $X$. Each digit appends to the right of the previous digit in Register $X$ without disturbing Registers $Y$, $Z$, or $T$.
* **Stack Lift Armed (`ARMED` / `Lift = TRUE`):** The moment you press any mathematical operator (`{{key:+}}`, `{{key:×}}`, `{{key:√x}}`, `{{key:SIN}}`, `{{key:LN}}`), the calculator terminates digit entry, writes the evaluated result into Register $X$, and arms the stack-lift state (`Lift = TRUE`). You do not need to press `{{key:ENTER}}` to protect that result. Pressing the next digit key (`{{key:0}}`–`{{key:9}}` or `{{key:.}}`) triggers an automatic stack-lift transition, pushing the finished result in Register $X$ up to Register $Y$ ($Y \leftarrow X, Z \leftarrow Y, T \leftarrow Z$) before starting your new number in $X$.
* **Stack Lift Neutral (`DISABLED` / `Lift = FALSE`):** We press `{{key:ENTER}}` only to separate two numbers typed *back-to-back* with no operator between them (such as `14` followed by `25`). Pressing `{{key:ENTER}}` pushes `14` up to Register $Y$, leaves a duplicate copy in $X$, and disables stack lift (`Lift = FALSE`) so the first digit of `25` overwrites $X$ in place without pushing a second `14` into $Z$.

Rooted in the Corvallis engineering specifications of the HP-15C and HP-32SII {{cite:hp15c1982,hp32sii1991}}, this Mealy automaton executes every register transition deterministically without operator-precedence buffers or parenthesis stacks.

### Stack Lift Transition Diagram

| Current State | Triggering Keystroke Class | Next State | Stack Register Effect |
| :--- | :--- | :--- | :--- |
| **LIFT ARMED** (`Lift = TRUE`) | First digit (`{{key:0}}`–`{{key:9}}`, `{{key:.}}`) | **EDIT BUFFER** | Pushes stack up (`X → Y → Z → T`) before writing new digit |
| **EDIT BUFFER** (In Progress) | Any function/operator (`{{key:+}}`, `{{key:×}}`, `{{key:√x}}`) | **LIFT ARMED** (`Lift = TRUE`) | Terminates digit entry, evaluates result into `X`, and arms stack lift |
| **EDIT BUFFER** or **LIFT ARMED** | `{{key:ENTER}}`, `{{key:CLx}}`, `{{key:Σ+}}` | **LIFT DISABLED** (`Lift = FALSE`) | Next digit typed will overwrite `X` in place without lifting `Y` |
| **LIFT DISABLED** (`Lift = FALSE`) | `{{key:x⇄y}}`, `{{key:R↓}}`, `{{key:R↑}}`, or operator | **LIFT ARMED** (`Lift = TRUE`) | Re-arms stack lift for subsequent numeric entry |

### The Three Keystroke Classes

Every key on the 43-button matrix belongs to one of three deterministic state-transition classes:

1. **Enables Stack Lift (`Lift = TRUE`):** Nearly all mathematical operators (`+`, `-`, `×`, `÷`, `√x`, `SIN`, `LN`, etc.), constants (`{{key:π}}`), recalls (`{{key:RCL}}`, `{{key:LASTX}}`), and stack permutations (`{{key:R↓}}`, `{{key:R↑}}`, `{{key:x⇄y}}`) set `Lift = TRUE`. The next digit key pushes $T \leftarrow Z, Z \leftarrow Y, Y \leftarrow X$ (discarding the old $T$ in `4-LVL` mode) before writing the new digit into $X$.
2. **Disables Stack Lift (`Lift = FALSE`):** Established exclusively by `{{key:ENTER}}` (the Stack Entry Invariant, which duplicates $Y \leftarrow X$ and disarms lift so the second operand overwrites $X$), `{{key:C}}` / `{{key:<-}}` (`CLx`), and statistical accumulation (`{{key:Σ+}}`, `{{key:Σ-}}`). The next digit key overwrites Register $X$ in place while leaving $Y, Z,$ and $T$ untouched.
3. **Preserves Stack Lift (State Unchanged):** Prefix and modal keys (`{{key:↰}}`, `{{key:↱}}`, `{{key:STO}}`, `{{key:E}}`, softkey menu openers, and `{{key:+/-}}` during active `EDIT` digit entry—whereas pressing `{{key:+/-}}` on a finalized register enables stack lift) leave the active stack-lift flag unaltered.

Because every operator sets the `Lift` flag deterministically upon completion, intermediate results never require explicit parentheses or scratchpad storage; tracking whether an operation enables or disables stack lift prevents accidental operand duplication.

---

### Definitive 43-Key Physical Matrix Audit Table

All 43 physical switch positions of the SC-32 keypad are indexed by electrical scan coordinate (`Row, Col`), primary legend, and post-execution Stack Lift state:

| Key Position | Primary Legend | Stack Lift Status | Updates LASTX | Register Delta Transformation | Operational Description |
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
| **Row 3, Col 3** | `{{key:+/-}}` | Preserves (in `EDIT`) / **Enables** | **Yes** (finalized) / No (`EDIT`) | $X \leftarrow -X; Y, Z, T \text{ unch}$ | Toggle arithmetic sign of active number |
| **Row 3, Col 4** | `{{key:E}}` | Preserves | No | Arms scientific exponent entry buffer | Exponent entry separator |
| **Row 3, Col 5** | `{{key:<-}}` | Preserves (in `EDIT`) / **Disables** (as `CLx`) | No | Deletes trailing digit in `EDIT`; sets $X \leftarrow 0$ as `CLx` | Dual-mode backspace / Clear $X$ |
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

## Shifted Operations & Formal Register Delta Algebra

Every shifted key on the SC-32 adheres strictly to the Stack Lift Automaton. Tables A.1 and A.2 catalog the mathematical, stack-control, and modal left-shifted (`{{key:↰}}`, Primary Shift) and right-shifted (`{{key:↱}}`, Secondary Shift) operations—while the ten physical unit conversion keys (`{{key:▸km}}`/`{{key:▸mi}}`, `{{key:▸kg}}`/`{{key:▸lb}}`, `{{key:▸°C}}`/`{{key:▸°F}}`, `{{key:▸cm}}`/`{{key:▸in}}`, `{{key:▸l}}`/`{{key:▸gal}}`) and angle/time conversions (`{{key:▸HR}}`/`{{key:▸HMS}}`, `{{key:▸DEG}}`/`{{key:▸RAD}}`) act as unary in-place transformations ($X \leftarrow f(X), \text{LASTX} \leftarrow X$) that arm stack lift—followed by the formal vector algebra of register transformations:

### Table A.1: Left-Shifted Operations (Primary Shift)

| Shifted Combination | Function Name | Stack Lift Status | Updates LASTX | Register Delta Transformation | Operational Notes |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `{{key:√x}}` | `x²` | **Enables** | **Yes** | $X \leftarrow X^2; Y, Z, T \text{ unch}$ | Unary square |
| `{{key:eˣ}}` | `10ˣ` | **Enables** | **Yes** | $X \leftarrow 10^X; Y, Z, T \text{ unch}$ | Unary common exponential |
| `{{key:LN}}` | `LOG` | **Enables** | **Yes** | $X \leftarrow \log_{10} X; Y, Z, T \text{ unch}$ | Unary common logarithm |
| `{{key:yˣ}}` | `ˣ√y` | **Enables** | **Yes** | $X \leftarrow Y^{1/X}; Y \leftarrow Z; Z \leftarrow T; T \leftarrow T$ | Dyadic $x$-th root of $y$; stack drops |
| `{{key:1/x}}` | `x!` | **Enables** | **Yes** | $X \leftarrow \Gamma(X+1); Y, Z, T \text{ unch}$ | Factorial / Gamma function |
| `{{key:Σ+}}` | `Σ-` | **Disables** | No (Preserved) | $X \leftarrow n-1; Y, Z, T \text{ unch}; \Sigma \text{ decremented}$ | Statistical correction; disables lift |
| `{{key:STO}}` | `CMPLX` | Preserves | No | Sets one-shot complex evaluator prefix | Arms Gaussian plane arithmetic |
| `{{key:R↓}}` | `HYP` | Preserves | No | Sets hyperbolic prefix flag | Arms hyperbolic evaluation |
| `{{key:SIN}}` | `ASIN` | **Enables** | **Yes** | $X \leftarrow \arcsin X; Y, Z, T \text{ unch}$ | Inverse sine in active angular mode |
| `{{key:COS}}` | `ACOS` | **Enables** | **Yes** | $X \leftarrow \arccos X; Y, Z, T \text{ unch}$ | Inverse cosine in active angular mode |
| `{{key:TAN}}` | `ATAN` | **Enables** | **Yes** | $X \leftarrow \arctan X; Y, Z, T \text{ unch}$ | Inverse tangent in active angular mode |
| `{{key:ENTER}}` | `LASTX` | **Enables** | No | $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X; X \leftarrow \text{LASTX}$ | Recalls prior $X$; pushes stack upward |
| `{{key:+/-}}` | `MODES` | Preserves | No | Menu: `DEG`, `RAD`, `GRAD`, `.`, `,` | Modal angular and radix settings |
| `{{key:E}}` | `DISP` | Preserves | No | Menu: `FIX n`, `SCI n`, `ENG n`, `ALL` | Non-destructive display precision |
| `{{key:<-}}` | `CLEAR` | Preserves | No | Menu: `CLEQN`, `CLVARS`, `CLALL`, `CLΣ`, `CLREGS`, `CLSTK` | Selective memory wipe menu |
| `{{key:÷}}` | `x?y` | Preserves | No | Comparison menu: `x=y`, `x≠y`, `x>y`, etc. | Conditional branching tests |
| `{{key:4}}` | `▸θ,r` | **Enables** | **Yes** | $X' \leftarrow \sqrt{X^2+Y^2};\; Y' \leftarrow \text{atan2}(Y, X);\; L \leftarrow X$ | Rectangular to polar conversion |
| `{{key:×}}` | `BASE` | Preserves | No | Menu: `HEX`, `DEC`, `OCT`, `BIN` | Integer base switching menu |
| `{{key:0}}` | `REGS` | Preserves | No | Displays register viewer table | Full-screen register browser (`STACK`, `STO`, `STATS`, `DATA`) |
| `{{key:.}}` | `FDISP` | Preserves | No | Toggles fraction display mode (Flag 7) | Rational fraction representation |
| `{{key:x∥y}}` | `TVM` | Preserves | No | Opens 5-variable TVM workspace | 5-variable Time Value of Money solver |
| `{{key:+}}` | `LBL` | Preserves | No | Prompts for equation label letter | Inserts equation label token in `EQN` mode |

### Table A.2: Right-Shifted Operations (Secondary Shift)

| Shifted Combination | Function Name | Stack Lift Status | Updates LASTX | Register Delta Transformation | Operational Notes |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `{{key:√x}}` | `PARTS` | Preserves | No | Menu: `IP`, `FP`, `ABS`, `SGN`, `GCD`, `LCM` | Number theory and decomposition |
| `{{key:eˣ}}` | `PROB` | Preserves | No | Menu: `Cn,r`, `Pn,r`, `x!`, `RAND`, `SD` | Combinatorics and probability |
| `{{key:LN}}` | `L.R.` | Preserves | No | Menu: `ŷ`, `x̂`, `r`, `m`, `b` | Linear regression estimates & slope |
| `{{key:yˣ}}` | `x̄,ȳ` | Preserves | No | Menu: `x̄`, `ȳ`, `x̄w` | Sample and weighted means |
| `{{key:1/x}}` | `s,σ` | Preserves | No | Menu: `sx`, `sy`, `σx`, `σy` | Sample and population std dev |
| `{{key:Σ+}}` | `SUMS` | Preserves | No | Menu: `Σx`, `Σy`, `Σx²`, `Σy²`, `Σxy`, `n` | Statistical accumulator viewer |
| `{{key:STO}}` | `EQN` | Preserves | No | Enters postfix Equation Bank editor | User-defined RPN equations |
| `{{key:R↓}}` | `R↑` | **Enables** | No | $X \leftarrow T; Y \leftarrow X; Z \leftarrow Y; T \leftarrow Z$ | Circular roll stack upward |
| `{{key:SIN}}` | `π` | **Enables** | No | $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X; X \leftarrow \pi$ | Pushes $\pi$ constant onto stack |
| `{{key:COS}}` | `%` | **Enables** | **Yes** | $X \leftarrow (Y \times X)/100; Y, Z, T \text{ unch}$ | Kahan base-preserving percentage |
| `{{key:TAN}}` | `%CHG` | **Enables** | **Yes** | $X \leftarrow 100(X - Y)/Y; Y, Z, T \text{ unch}$ | Base-preserving percent change |
| `{{key:ENTER}}` | `SHOW` | Preserves | No | Renders 15-digit internal mantissa | Non-destructive temporary peek |
| `{{key:+/-}}` | `ABS` | **Enables** | **Yes** | $X \leftarrow \lvert X\rvert; Y, Z, T \text{ unch}$ | Unary absolute value magnitude |
| `{{key:E}}` | `÷R` | **Enables** | **Yes** | $X \leftarrow \operatorname{trunc}(Y/X); Y \leftarrow \text{rem}(Y, X); Z, T \text{ unch}$ | Integer quotient ($X$) & remainder ($Y$) |
| `{{key:<-}}` | *(None)* | Preserves | No | Unassigned | Intentionally unassigned to prevent accidental clear |
| `{{key:XEQ}}` | `POLY` | Preserves | No | Dynamic cubic solver workspace (`A B C D EXEC CLR`)| Closed-form quadratic and cubic root workspace |
| `{{key:7}}` | `SOLVE` | **Enables** | No | $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X; X \leftarrow x^*$ | Richard Brent hybrid root solver |
| `{{key:8}}` | `∫` | **Enables** | No | $X \leftarrow \int_Y^X f(t)\,dt; Y \leftarrow \lvert\epsilon\rvert$ | Adaptive Romberg quadrature |
| `{{key:÷}}` | `x?0` | Preserves | No | Comparison menu: `x=0`, `x≠0`, `x>0`, etc. | Zero-relative comparison tests |
| `{{key:4}}` | `▸y,x` | **Enables** | **Yes** | $X' \leftarrow X\cos Y;\; Y' \leftarrow X\sin Y;\; L \leftarrow X$ | Polar to rectangular conversion |
| `{{key:×}}` | `FLAGS` | Preserves | No | Menu: `SF n`, `CF n`, `FS? n`, `STACK` (`2/4/8-LVL`, `INF`), `EXAM` | System flags & stack size |
| `{{key:.}}` | `/c` | **Enables** | No | Pops $c \in [2, 4095]$ from $X$; drops stack | Fixed fraction denominator ($1/c$) |
| `{{key:x∥y}}` | *(None)* | Preserves | No | Unassigned on physical non-graphing hardware | Intentionally unassigned (`TVM` sits on `{{key:↰}}`) |

### The Formal Register Delta Algebra

To verify calculation sequences with mathematical certainty, the effect of any operator $\Omega$ on the four-register stack $\mathbf{S} = [X, Y, Z, T]^T$ is expressed as a matrix or functional transformation $\mathbf{S}' = \mathbf{f}_\Omega(\mathbf{S})$:

* **Unary Operators ($f(X)$):** Functions such as `{{key:√x}}`, `{{key:1/x}}`, `{{key:eˣ}}`, `{{key:LN}}`, `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`, `{{key:x²}}`, `{{key:10ˣ}}`, `{{key:LOG}}`, `{{key:x!}}`, and `{{key:|x|}}` transform $X$ in place while leaving $Y, Z, T$ undisturbed:
  $$\begin{bmatrix} X' \\ Y' \\ Z' \\ T' \end{bmatrix} = \begin{bmatrix} f(X) \\ Y \\ Z \\ T \end{bmatrix}, \quad \text{LASTX}' = X, \quad \text{Lift}' = \text{TRUE}$$
* **Dyadic Operators ($f(Y, X)$):** Binary operators (`{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`, `{{key:yˣ}}`, `{{key:ˣ√y}}`, and `{{key:x∥y}}`) combine $Y$ and $X$ into $X$, drop $Z \to Y$, and replicate $T \to Z$:
  $$\begin{bmatrix} X' \\ Y' \\ Z' \\ T' \end{bmatrix} = \begin{bmatrix} f(Y, X) \\ Z \\ T \\ T \end{bmatrix}, \quad \text{LASTX}' = X, \quad \text{Lift}' = \text{TRUE}$$
* **Circular Stack Rotations (`{{key:R↓}}`, `{{key:R↑}}`, `{{key:x⇄y}}`):** Rearrange registers without altering numerical values or updating `LASTX`, while arming stack lift ($\text{Lift}' = \text{TRUE}$):
  $$\mathbf{S}'_{\text{R}\downarrow} = \begin{bmatrix} Y \\ Z \\ T \\ X \end{bmatrix}, \qquad \mathbf{S}'_{\text{R}\uparrow} = \begin{bmatrix} T \\ X \\ Y \\ Z \end{bmatrix}, \qquad \mathbf{S}'_{x\leftrightarrow y} = \begin{bmatrix} Y \\ X \\ Z \\ T \end{bmatrix}$$
* **Stack Duplication (`{{key:ENTER}}`):** Pushes the stack upward while replicating $X$ into $Y$ and disarming stack lift:
  $$\begin{bmatrix} X' \\ Y' \\ Z' \\ T' \end{bmatrix} = \begin{bmatrix} X \\ X \\ Y \\ Z \end{bmatrix}, \quad \text{LASTX}' = \text{LASTX}, \quad \text{Lift}' = \text{FALSE}$$

During any dyadic operation in `4-LVL` mode, Register $T$ drops into $Z$ while $T$ retains its original value ($T' \leftarrow T$). This top-register constant replication invariant allows a constant stored in $T$ to be reused across an unbounded series of operations without re-entry.

---

## Comprehensive Stack Lift Traces

Twelve operational traces illustrate the Stack Lift Automaton across representative engineering calculations. Multi-register expression traces display the full four-register stack (`Register T, Register Z, Register Y, Register X`), focused state-machine traces highlight the active `Stack Lift Flag` alongside the working and auxiliary registers (`LASTX`, `Register Z`, or `Stat Register n`), and compact dyadic traces display the lower three registers (`Register X, Register Y, Register Z`).

### Chained Arithmetic Without Intermediary ENTER
Calculate: $(14 \times 25) + (36 \times 48)$

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:1}} {{key:4}}` | `0` | `0` | `0` | `14` | First operand keyed (`EDIT`) |
| `{{key:ENTER}}` | `0` | `0` | `14` | `14` | Stack pushed; $X$ copied to $Y$ (`DISABLED`) |
| `{{key:2}} {{key:5}}` | `0` | `0` | `14` | `25` | Overwrites $X$ in place (`EDIT`); $Y$ preserved |
| `{{key:×}}` | `0` | `0` | `0` | `350` | $14 \times 25 = 350$; stack drops (`ARMED`) |
| `{{key:3}} {{key:6}}` | `0` | `0` | `350` | `36` | **No ENTER needed:** `ARMED` lift pushes `350` into $Y$ (`EDIT`) |
| `{{key:ENTER}}` | `0` | `350` | `36` | `36` | Pushes `350` into $Z$ (`DISABLED`) |
| `{{key:4}} {{key:8}}` | `0` | `350` | `36` | `48` | Overwrites $X$ (`EDIT`); registers $Y$ and $Z$ preserved |
| `{{key:×}}` | `0` | `0` | `350` | `1728` | $36 \times 48 = 1728$; $Z$ drops to $Y$ (`ARMED`) |
| `{{key:+}}` | `0` | `0` | `0` | `2078` | $350 + 1728 = 2078$; final sum in $X$ (`ARMED`) |

---

### The ENTER Lift-Disable Invariant
Demonstrating why pressing `{{key:ENTER}}` prevents accidental stack duplication.

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:5}} {{key:0}}` | `0` | `0` | `0` | `50` | Base value entered (`EDIT`) |
| `{{key:ENTER}}` | `0` | `0` | `50` | `50` | `DISABLED`; $X$ duplicated into $Y$ |
| `{{key:8}}` | `0` | `0` | `50` | `8` | Digit `8` replaces $X$ in place (`EDIT`) without pushing stack |
| `{{key:+}}` | `0` | `0` | `0` | `58` | Addition yields `58`; stack lift `ARMED` |

---

### LASTX Dyadic Operator Correction
The user intends to compute $100 \times 8 = 800$, but accidentally hits `{{key:÷}}`, producing $12.5$. The error is corrected without re-keying $100$ or $8$:

| Step | Keystroke | Stack Lift Flag | Register X | Register Y | LASTX | Operational Commentary |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:1}} {{key:0}} {{key:0}} {{key:ENTER}}`| `DISABLED` | `100` | `100` | `0` | Operands staged |
| 2 | `{{key:8}} {{key:÷}}` | `ARMED` | `12.5000` | `0` | `8` | Error: Divided instead of multiplied |
| 3 | `{{key:LASTX}}` | `ARMED` | `8` | `12.5000` | `8` | Recalls operand `8` that caused the operation |
| 4 | `{{key:×}}` | `ARMED` | `100.0000` | `0` | `8` | Multiplies $12.5 \times 8$ to recover original numerator $100$ |
| 5 | `{{key:LASTX}}` | `ARMED` | `8` | `100.0000` | `8` | Recalls operand `8` once more |
| 6 | `{{key:×}}` | `ARMED` | `800.0000` | `0` | `8` | Multiplies $100 \times 8$ to achieve intended target $800$ |

---

### CLx Stack Lift Disabling
Demonstrating how `{{key:CLx}}` clears an erroneous entry without collapsing or dropping upper registers:

| Step | Keystroke | Stack Lift Flag | Register X | Register Y | Register Z | Operational Commentary |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:1}} {{key:5}} {{key:0}} {{key:ENTER}}`| `DISABLED` | `150` | `150` | `0` | Operand staged |
| 2 | `{{key:9}} {{key:9}} {{key:9}}` | `EDIT` | `999` | `150` | `0` | User mistypes second operand |
| 3 | `{{key:CLx}}` | **`DISABLED`** | `0` | `150` | `0` | `{{key:CLx}}` zeroes $X$ and sets state to `DISABLED` (`Lift = FALSE`) |
| 4 | `{{key:2}} {{key:5}}` | `EDIT` | `25` | `150` | `0` | Typing `25` overwrites zero in place |
| 5 | `{{key:-}}` | `ARMED` | `125` | `0` | `0` | $150 - 25 = 125$ |

---

### Unary Function Lift Re-Arming
Unary functions evaluate in place on Register $X$ and re-arm stack lift so subsequent inputs push automatically:

| Step | Keystroke | Stack Lift Flag | Register X | Register Y | Operational Commentary |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `{{key:1}} {{key:6}}` | `EDIT` | `16` | `0` | Raw value entered |
| 2 | `{{key:√x}}` | **`ARMED`** | `4` | `0` | $\sqrt{16} = 4$; Lift flag `ARMED` (`Lift = TRUE`) |
| 3 | `{{key:9}}` | `EDIT` | `9` | `4` | Inputting `9` triggers lift push; $4 \to Y$ |
| 4 | `{{key:+}}` | `ARMED` | `13` | `0` | $4 + 9 = 13$ |

---

### Constant Factor Calculation via T-Replication
Compute sales tax ($8.25\%$, multiplier $1.0825$) on three amounts: $\$15.00$, $\$24.50$, and $\$80.00$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:1}} {{key:.}} {{key:0}} {{key:8}} {{key:2}} {{key:5}}` | `0` | `0` | `0` | `1.0825` | Tax factor keyed into $X$ |
| `{{key:ENTER}} {{key:ENTER}} {{key:ENTER}}` | `1.0825` | `1.0825` | `1.0825` | `1.0825` | Stack flooded with constant factor |
| `{{key:1}} {{key:5}} {{key:×}}` | **`1.0825`** | `1.0825` | `1.0825` | `16.2375` | $15 \times 1.0825$; $T$ replicates into $Z$ and $Y$ |
| `{{key:C}} {{key:2}} {{key:4}} {{key:.}} {{key:5}} {{key:×}}` | **`1.0825`** | `1.0825` | `1.0825` | `26.5213` | `C` clears $X$ (disabling lift); $24.5 \times 1.0825$; $T$ replicates |
| `{{key:C}} {{key:8}} {{key:0}} {{key:×}}` | **`1.0825`** | `1.0825` | `1.0825` | `86.6000` | `C` clears $X$; $80 \times 1.0825$; constant remains active |

---

### Statistical Accumulation and Non-Destructive Stack Isolation
Entering pairs $(x, y) = (10, 25)$ into statistical memory:

| Step | Keystroke | Stack Lift Flag | Register X | Register Y | Stat Register $n$ | Operational Commentary |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:2}} {{key:5}} {{key:ENTER}}` | `DISABLED` | `25` | `25` | `0` | $y$-coordinate pushed to $Y$ |
| 2 | `{{key:1}} {{key:0}}` | `EDIT` | `10` | `25` | `0` | $x$-coordinate keyed into $X$ |
| 3 | `{{key:Σ+}}` | **`DISABLED`** | `1` | `25` | `1` | Register $X$ shows sample count $n=1$; lift `DISABLED` |
| 4 | `{{key:3}} {{key:5}}` | `EDIT` | `35` | `25` | `1` | Next $y$ overwrites $X$ directly without stack lift |

---

### Complex Number Evaluation via CMPLX
Compute $(3 + 4i) + (5 - 2i)$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:3}} {{key:ENTER}} {{key:4}}` | `0` | `0` | `3` (Real) | `4` (Imag) | First complex number staged in $(Y, X)$ |
| `{{key:ENTER}}` | `0` | `3` | `4` | `4` | Single `ENTER` lifts $(3, 4)$ to $(Z, Y)$ and disables lift |
| `{{key:5}} {{key:ENTER}} {{key:2}} {{key:+/-}}` | `3` | `4` | `5` | `-2` | `5` overwrites $X$; `ENTER 2 +/-` lifts $(3, 4)$ to $(T, Z)$ |
| `{{key:CMPLX}} {{key:+}}` | `3` | `3` | `8` (Real) | `2` (Imag) | Vector sum: $(3+5) + (4-2)i = 8 + 2i$; $T$ replicates |

---

### Parallel Resistance via the Harmonic Operator
Calculate parallel equivalent of $30\,\Omega$ and $60\,\Omega$:

| Step | Keystroke | Register X | Register Y | Register Z | Operational Commentary |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `{{key:3}} {{key:0}} {{key:ENTER}}` | `30` | `30` | `0` | First resistor staged |
| 2 | `{{key:6}} {{key:0}}` | `60` | `30` | `0` | Second resistor keyed |
| 3 | `{{key:x∥y}}` | `20.0000` | `0` | `0` | Single-keystroke harmonic calculation: $\frac{30 \times 60}{30 + 60} = 20\,\Omega$ |

---

### Integer Division with Remainder
Divide $29$ by $6$ to find quotient and integer remainder:

| Step | Keystroke | Register X | Register Y | Register Z | Operational Commentary |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `{{key:2}} {{key:9}} {{key:ENTER}}` | `29` | `29` | `0` | Dividend staged in $Y$ |
| 2 | `{{key:6}}` | `6` | `29` | `0` | Divisor in $X$ |
| 3 | `{{key:÷R}}` | `4` (Quotient) | `5` (Remainder) | `0` | $29 = 4 \times 6 + 5$; quotient in $X$, remainder in $Y$ |

---

### Absolute Value Evaluation
Compute $|-45.75|$:

| Step | Keystroke | Register X | Register Y | Operational Commentary |
| :---: | :--- | :---: | :---: | :--- |
| 1 | `{{key:4}} {{key:5}} {{key:.}} {{key:7}} {{key:5}} {{key:+/-}}`| `-45.75` | `0` | Negative operand entered |
| 2 | `{{key:ABS}}` | `45.75` | `0` | Instant absolute value; stack lift armed |
| 3 | `{{key:1}} {{key:0}} {{key:×}}` | `457.50` | `0` | Multiplies without needing `{{key:ENTER}}` |

---

### Dynamic Stack Depth Expansion (4-LVL vs. 8-LVL vs. INF)
Under extended system flags (`{{key:FLAGS}}`), the user can expand the stack beyond 4 levels:
* **`4-LVL` (Classic HP):** 4 registers ($X, Y, Z, T$). $T$ replicated on drop; values pushed off $T$ are discarded.
* **`8-LVL` (Extended STEM):** 8 registers ($X, Y, Z, T, R_5, R_6, R_7, R_8$). Deeper parenthetical evaluations can occur without variable storage. $R_8$ replicated on drop.
* **`INF` (Infinite Dynamic):** Dynamic LIFO stack scaling up to 999 levels (`RPNCore` ceiling). Stack drop pulls upper elements down without top-register replication.

#### Stack Depth Architecture Comparison (After Keying `2 ENTER 3 ENTER 4 ENTER 5 ENTER 6 ENTER 7`)

| Level | 4-Level Stack (`4-LVL`) | 8-Level Stack (`8-LVL`) | Infinite Stack (`INF`) |
| :--- | :--- | :--- | :--- |
| **Top / Level 8** | — *(No $R_8$; ceiling at $T$)* | `R8 = 0` *(Top Replicator)* | Dynamic Stack Top (up to Level 999) |
| **Level 7** | — | `R7 = 0` | $\dots$ *(Empty until pushed)* |
| **Level 6** | — *(`2` pushed off $T$)* | `R6 = 2` *(Preserved above $T$)* | `Level 6 = 2` *(Preserved in LIFO heap)* |
| **Level 5** | — *(`3` pushed off $T$)* | `R5 = 3` *(Preserved above $T$)* | `Level 5 = 3` *(Preserved in LIFO heap)* |
| **Level 4** | `T = 4` *(Constant Replicator)* | `T (R4) = 4` | `Level 4 (T) = 4` |
| **Level 3** | `Z = 5` *(Third Operative)* | `Z (R3) = 5` | `Level 3 (Z) = 5` |
| **Level 2** | `Y = 6` *(Second Operative)* | `Y (R2) = 6` | `Level 2 (Y) = 6` |
| **Level 1 (Display)** | `X = 7` *(Primary Display)* | `X (R1) = 7` *(Primary Display)* | `Level 1 (X) = 7` *(Primary Display)* |
