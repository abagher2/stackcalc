---
title: "Appendix A: Formal Stack-Lift State Machine | Thinking in the Stack (SC-32)"
description: "The definitive 43-key tabular reference for the StackCalc SC-32 Stack Lift State Machine, categorizing Stack Lift enablement, LASTX updates, and register delta effects."
---

# Appendix A: Formal Stack-Lift State Machine

The operational registers ($X, Y, Z, T$) of a Reverse Polish Notation (RPN) processor form a four-level last-in, first-out (LIFO) evaluation stack (**Figure A.1**), with $X$ as the active bottom display register, $Y$ as the second operative register, $Z$ as the third, and $T$ as the top constant register.

{{blocks:sc32_concept_stack_elevator|The four-register operational stack (X, Y, Z, T) and LASTX audit register during stack-lift and dyadic drop transitions.}}

On the SC-32, Register $X$ is governed by a deterministic George H. Mealy (1955) finite-state automaton $(Q, \Sigma, \Delta, \delta, \lambda)$ called the Stack Lift Automaton—defined by a finite set of internal stack-lift states $Q = \{\text{EDIT}, \text{ARMED}, \text{DISABLED}\}$, an input alphabet $\Sigma$ of physical keystrokes, an output alphabet $\Delta$ of register-transfer operations, a state-transition function $\delta: Q \times \Sigma \to Q$ mapping the current state and keystroke to the next state, and an output function $\lambda: Q \times \Sigma \to \Delta$ specifying the immediate register transformation—preserving the classical four-register state-transition rules of the **HP-35**, **HP-15C**, and **HP-32SII** {{cite:hamblin1957,cochran1972,hp15c1982,hp32sii1991}}:

* **`EDIT` (Building a Number):** Digit keys (`{{key:0}}`–`{{key:9}}`, `{{key:.}}`) append to Register $X$ without disturbing $Y, Z,$ or $T$.
* **`ARMED` (`Lift = TRUE`):** Pressing any operator (such as `{{key:+}}`, `{{key:×}}`, `{{key:√x}}`, `{{key:SIN}}`, or `{{key:LN}}`) terminates digit entry, writes the result into $X$, and arms lift. The next digit key pushes $T \leftarrow Z, Z \leftarrow Y, Y \leftarrow X$ before starting a new number in $X$.
* **`DISABLED` (`Lift = FALSE`):** Set by `{{key:ENTER}}` (duplicates $Y \leftarrow X$ and disarms lift), `{{key:<-}}` (`CLx`), `{{key:C}}`, and `{{key:Σ+}}`/`{{key:Σ-}}`. Prefix keys (`{{key:↰}}`, `{{key:↱}}`, `{{key:E}}`) preserve `Lift`.

---

## Definitive 43-Key Physical Matrix Audit Table

Each physical key position across Rows `R0`–`R7` executes a deterministic stack-lift transition, `LASTX` update, and four-register transformation vector:

| Key Position | Primary Legend | Stack Lift | LASTX | Register Delta Transformation | Operational Description |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **R0, C0–C5** | `{{key:LFU0}}`–`{{key:LFU5}}` | Preserves | No | Context dependent | Softkey Menu / Dynamic LFU Slots 1–6 |
| **R1, C0** | `{{key:√x}}` | **Enables** | **Yes** | $X \leftarrow \sqrt{X}; Y, Z, T \text{ unch}$ | Unary square root |
| **R1, C1** | `{{key:eˣ}}` | **Enables** | **Yes** | $X \leftarrow e^X; Y, Z, T \text{ unch}$ | Unary natural exponential |
| **R1, C2** | `{{key:LN}}` | **Enables** | **Yes** | $X \leftarrow \ln X; Y, Z, T \text{ unch}$ | Unary natural logarithm |
| **R1, C3** | `{{key:yˣ}}` | **Enables** | **Yes** | $X \leftarrow Y^X; Y \leftarrow Z; Z \leftarrow T; T \leftarrow T$ | Dyadic power; stack drops |
| **R1, C4** | `{{key:1/x}}` | **Enables** | **Yes** | $X \leftarrow 1/X; Y, Z, T \text{ unch}$ | Unary reciprocal |
| **R1, C5** | `{{key:Σ+}}` | **Disables** | No | $X \leftarrow n; Y, Z, T \text{ unch}; \Sigma \text{ updated}$ | Statistical accumulation |
| **R2, C0** | `{{key:STO}}` | **Enables** | No | $X \to \text{Var}[k]$ (or $\text{Var}[k] \leftarrow \text{Var}[k]\text{ op }X$); $\text{Stack unch}$ | Store $X$ or in-place store arithmetic (`+,-,×,÷`) |
| **R2, C1** | `{{key:RCL}}` | **Enables** | No / **Yes** | If Lift: pushes stack, $X \leftarrow \text{Var}[k]$; `RCL op k` updates $X \leftarrow X\text{ op }\text{Var}[k]$ in place ($Y,Z,T\text{ unch}$) | Recall variable $k$ or in-place recall arithmetic (`+,-,×,÷`) |
| **R2, C2** | `{{key:R↓}}` | **Enables** | No | $X \leftarrow Y; Y \leftarrow Z; Z \leftarrow T; T \leftarrow X$ | Roll stack down circularly |
| **R2, C3–C5**| `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}` | **Enables** | **Yes** | $X \leftarrow \operatorname{trig}(X); Y, Z, T \text{ unch}$ | Planar sine, cosine, tangent |
| **R3, C0–1**| `{{key:ENTER}}` | **Disables** | No | $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X; X \leftarrow X$ | Duplicate $X \to Y$; disable lift |
| **R3, C2** | `{{key:x⇄y}}` | **Enables** | No | $X \leftarrow Y; Y \leftarrow X; Z, T \text{ unch}$ | Swap Registers $X$ and $Y$ |
| **R3, C3** | `{{key:+/-}}` | **Preserves** (Both) | **Yes** / No | $X \leftarrow -X; Y, Z, T \text{ unch}$ | Toggle sign (`LASTX` saved on finalized stack; unchanged in `EDIT`) |
| **R3, C4** | `{{key:E}}` | Preserves | No | Arms exponent buffer | Scientific exponent separator |
| **R3, C5** | `{{key:<-}}` | Preserves / **Disables** | No | Backspace in `EDIT`; $X \leftarrow 0$ as `CLx` | Backspace / Clear $X$ |
| **R4, C0** | `{{key:XEQ}}` | Preserves | No | Context dependent | Execute selected equation |
| **R4–R7, C1–C3**| `{{key:0}}`–`{{key:9}}`, `{{key:.}}` | (Consumes Lift) | No | If Lift: $T \leftarrow Z; Z \leftarrow Y; Y \leftarrow X$; $X \leftarrow d$ | Numeric digit and radix entry |
| **R4, C4** | `{{key:÷}}` | **Enables** | **Yes** | $X \leftarrow Y \div X; Y \leftarrow Z; Z \leftarrow T; T \leftarrow T$ | Dyadic division; stack drops |
| **R5, C0** | `{{key:↰}}` | Preserves | No | Arms left-shift modifier | Primary shift prefix |
| **R5, C4** | `{{key:×}}` | **Enables** | **Yes** | $X \leftarrow Y \times X; Y \leftarrow Z; Z \leftarrow T; T \leftarrow T$ | Dyadic multiplication; drops |
| **R6, C0** | `{{key:↱}}` | Preserves | No | Arms right-shift modifier | Secondary shift prefix |
| **R6, C4** | `{{key:-}}` | **Enables** | **Yes** | $X \leftarrow Y - X; Y \leftarrow Z; Z \leftarrow T; T \leftarrow T$ | Dyadic subtraction; drops |
| **R7, C0** | `{{key:C}}` (ON) | **Disables** | No | Clears entry or dismisses error | Clear / Power wake |
| **R7, C3** | `{{key:x∥y}}` | **Enables** | **Yes** | $X \leftarrow \frac{Y \times X}{Y + X}; Y \leftarrow Z; Z \leftarrow T; T \leftarrow T$ | Parallel harmonic product |
| **R7, C4** | `{{key:+}}` | **Enables** | **Yes** | $X \leftarrow Y + X; Y \leftarrow Z; Z \leftarrow T; T \leftarrow T$ | Dyadic addition; stack drops |

---

## Left-Shifted (↰) & Right-Shifted (↱) Operations

All physical unit conversions (`{{key:▸km}}`/`{{key:▸mi}}`, `{{key:▸kg}}`/`{{key:▸lb}}`, `{{key:▸°C}}`/`{{key:▸°F}}`, `{{key:▸cm}}`/`{{key:▸in}}`, `{{key:▸l}}`/`{{key:▸gal}}`) and angle/time conversions (`{{key:▸HR}}`/`{{key:▸HMS}}`, `{{key:▸DEG}}`/`{{key:▸RAD}}`) act as unary operators ($X \leftarrow f(X), \text{LASTX} \leftarrow X, \text{Lift} \leftarrow \text{TRUE}$):

| Host Key | Shift | Function | Stack Lift | LASTX | Register Delta Transformation & Notes |
| :--- | :---: | :--- | :---: | :---: | :--- |
| `{{key:√x}}` | `{{key:↰}}` / `{{key:↱}}` | `x²` / `PARTS` | **Enables** / Preserves | **Yes** / No | $X \leftarrow X^2$ / Opens `IP, FP, ABS, SGN, GCD, LCM` menu |
| `{{key:eˣ}}` | `{{key:↰}}` / `{{key:↱}}` | `10ˣ` / `PROB` | **Enables** / Preserves | **Yes** / No | $X \leftarrow 10^X$ / Opens `Cn,r, Pn,r, n!, RAND, SD` menu |
| `{{key:LN}}` | `{{key:↰}}` / `{{key:↱}}` | `LOG` / `L.R.` | **Enables** / Preserves | **Yes** / No | $X \leftarrow \log_{10} X$ / Opens linear regression `ŷ, x̂, r, m, b` |
| `{{key:yˣ}}` | `{{key:↰}}` / `{{key:↱}}` | `ˣ√y` / `x̄,ȳ` | **Enables** / Preserves | **Yes** / No | $X \leftarrow Y^{1/X}$ (drops stack) / Opens means `x̄, ȳ, x̄w` |
| `{{key:1/x}}` | `{{key:↰}}` / `{{key:↱}}` | `x!` / `s,σ` | **Enables** / Preserves | **Yes** / No | $X \leftarrow \Gamma(X+1)$ / Opens standard deviations `sx, sy, σx, σy` |
| `{{key:Σ+}}` | `{{key:↰}}` / `{{key:↱}}` | `Σ-` / `SUMS` | **Disables** / Preserves | No / No | $X \leftarrow n-1$ (decrements $\Sigma$) / Opens `Σx, Σy, Σx², Σy², Σxy, n` |
| `{{key:STO}}` | `{{key:↰}}` / `{{key:↱}}` | `CMPLX` / `EQN` | **Enables** / Preserves | No / No | Arms Gaussian $(Y,X)$ complex prefix / Opens Equation Bank |
| `{{key:RCL}}` | `{{key:↰}}` / `{{key:↱}}` | `RND` / `SCRL` | **Enables** / Preserves | **Yes** / No | Rounds $X$ to display setting / Scrolls long equations |
| `{{key:R↓}}` | `{{key:↰}}` / `{{key:↱}}` | `HYP` / `R↑` | Preserves / **Enables** | No / No | Arms hyperbolic prefix / Circular roll up ($X \leftarrow T, Y \leftarrow X, Z \leftarrow Y, T \leftarrow Z$) |
| `{{key:SIN}}` | `{{key:↰}}` / `{{key:↱}}` | `ASIN` / `π` | **Enables** / **Enables** | **Yes** / No | $X \leftarrow \arcsin X$ / Loads $\pi \to X$ (lifts stack if Lift = TRUE; arms Lift = TRUE) |
| `{{key:COS}}` | `{{key:↰}}` / `{{key:↱}}` | `ACOS` / `%` | **Enables** / **Enables** | **Yes** / **Yes** | $X \leftarrow \arccos X$ / Kahan base-preserving $X \leftarrow (Y\cdot X)/100$ |
| `{{key:TAN}}` | `{{key:↰}}` / `{{key:↱}}` | `ATAN` / `%CHG` | **Enables** / **Enables** | **Yes** / **Yes** | $X \leftarrow \arctan X$ / Base-preserving $X \leftarrow 100(X-Y)/Y$ |
| `{{key:ENTER}}`| `{{key:↰}}` / `{{key:↱}}` | `LASTX` / `SHOW` | **Enables** / Preserves | No / No | Pushes `LASTX` into $X$ / Full 15-digit mantissa peek |
| `{{key:x⇄y}}` | `{{key:↰}}` / `{{key:↱}}` | `MEM` / `x⇄?` | Preserves / **Enables** | No / No | Opens `VARS, EQN, REGS` memory catalog / Swaps $X \leftrightarrow \text{Var}[k]$ |
| `{{key:+/-}}` | `{{key:↰}}` / `{{key:↱}}` | `MODES` / `ABS` ($\lvert x\rvert$) | Preserves / **Enables** | No / **Yes** | Opens `DEG, RAD, GRAD` menu / Unary $X \leftarrow \lvert X\rvert$ |
| `{{key:E}}` | `{{key:↰}}` / `{{key:↱}}` | `DISP` / `÷R` | Preserves / **Enables** | No / **Yes** | Opens `FIX, SCI, ENG, ALL` / $X \leftarrow \operatorname{trunc}(Y/X), Y \leftarrow \text{rem}(Y,X)$ |
| `{{key:<-}}` | `{{key:↰}}` / `{{key:↱}}` | `CLEAR` / — | Preserves / Preserves | No / No | Opens `CLEQN, CLVARS, CLALL, CLΣ, CLREGS, CLSTK` |
| `{{key:XEQ}}` | `{{key:↰}}` / `{{key:↱}}` | `FN=` / `POLY` | Preserves / Preserves | No / No | Selects target equation / Opens cubic solver (`A B C D CLR`; press `{{key:XEQ}}` to solve) |
| `{{key:7}}` | `{{key:↰}}` / `{{key:↱}}` | `↓` / `SOLVE` | Preserves / **Enables** | No / No | Steps down list / Brent root solver ($X \leftarrow x^*$) |
| `{{key:8}}` | `{{key:↰}}` / `{{key:↱}}` | `↑` / `∫` | Preserves / **Enables** | No / No | Steps up list / Romberg integral ($X \leftarrow \int_Y^X f(t)\,dt, Y \leftarrow \lvert\epsilon\rvert$) |
| `{{key:9}}` | `{{key:↰}}` / `{{key:↱}}` | `▸km` / `▸mi` | **Enables** / **Enables** | **Yes** / **Yes** | Unary distance conversion: $X \leftarrow 1.609344\,X$ / $X \leftarrow X / 1.609344$ |
| `{{key:÷}}` | `{{key:↰}}` / `{{key:↱}}` | `x?y` / `x?0` | Preserves / Preserves | No / No | Relational test menus (`=`, `≠`, `>`, `<`, `≥`, `≤`; return `1`/`0` inside `EQN`) |
| `{{key:4}}` | `{{key:↰}}` / `{{key:↱}}` | `▸θ,r` / `▸y,x` | **Enables** / **Enables** | **Yes** / **Yes** | Rect $(Y=y, X=x) \leftrightarrow$ Polar $(Y=\theta, X=r)$; $Z, T\text{ unch}$ |
| `{{key:5}}` | `{{key:↰}}` / `{{key:↱}}` | `▸HR` / `▸HMS` | **Enables** / **Enables** | **Yes** / **Yes** | Sexagesimal `D.MMSS` $\to$ decimal `HR` / decimal $\to$ `D.MMSS` |
| `{{key:6}}` | `{{key:↰}}` / `{{key:↱}}` | `▸DEG` / `▸RAD` | **Enables** / **Enables** | **Yes** / **Yes** | Unary angular conversion: $X \leftarrow 180\,X/\pi$ / $X \leftarrow \pi\,X/180$ |
| `{{key:×}}` | `{{key:↰}}` / `{{key:↱}}` | `BASE` / `FLAGS` | Preserves / Preserves | No / No | Radix menu (`HEX, DEC, OCT, BIN`) / System flags & `STACK` |
| `{{key:1}}` | `{{key:↰}}` / `{{key:↱}}` | `▸kg` / `▸lb` | **Enables** / **Enables** | **Yes** / **Yes** | Unary mass conversion: $X \leftarrow 0.45359237\,X$ / $X \leftarrow X / 0.45359237$ |
| `{{key:2}}` | `{{key:↰}}` / `{{key:↱}}` | `▸°C` / `▸°F` | **Enables** / **Enables** | **Yes** / **Yes** | Unary temperature conversion: $X \leftarrow \frac{5}{9}(X-32)$ / $X \leftarrow \frac{9}{5}X + 32$ |
| `{{key:3}}` | `{{key:↰}}` / `{{key:↱}}` | `▸cm` / `▸in` | **Enables** / **Enables** | **Yes** / **Yes** | Unary length conversion: $X \leftarrow 2.54\,X$ / $X \leftarrow X / 2.54$ |
| `{{key:-}}` | `{{key:↰}}` / `{{key:↱}}` | `▸l` / `▸gal` | **Enables** / **Enables** | **Yes** / **Yes** | Unary volume conversion: $X \leftarrow 3.785411784\,X$ / $X \leftarrow X / 3.785411784$ |
| `{{key:C}}` | `{{key:↰}}` / `{{key:↱}}` | `?` / `OFF` | Preserves / Preserves | No / No | Interactive guided tutorial `?` / Power sleep `OFF` |
| `{{key:0}}` | `{{key:↰}}` / `{{key:↱}}` | `REGS` / `VIEW` | Preserves / Preserves | No / No | Full register viewer (`STACK, STO, STATS, DATA`) / Single view |
| `{{key:.}}` | `{{key:↰}}` / `{{key:↱}}` | `FDISP` / `/c` | Preserves / **Enables** | No / No | Toggles fraction display (Flag 7) / Sets max denominator $c \leftarrow \lfloor\lvert X\rvert\rfloor$ and drops $X$ (if $\ge 2$) or recalls $c \to X$ (if $1$) |
| `{{key:x∥y}}` | `{{key:↰}}` / `{{key:↱}}` | `TVM` / `PLOT` | Preserves / Preserves | No / No | Opens 5-variable `TVM` financial workspace / App-mode `PLOT` workspace (excluded from physical firmware for exam compliance) |
| `{{key:+}}` | `{{key:↰}}` / `{{key:↱}}` | `LBL` / `RTN` | Preserves / Preserves | No / No | Inserts label token `LBL` / subroutine return token `RTN` in `EQN` |

## Formal Register Delta Algebra & Configurable Stack Depth

With the four-register operational state vector written as $\mathbf{S} = [X, Y, Z, T]^T$ alongside the audit register $\text{LASTX}$ and boolean stack-lift latch $\mathcal{L}_{\text{lift}} \in \{\text{TRUE}, \text{FALSE}\}$, every unary operator $f(X)$, dyadic operator $g(Y, X)$, and stack-duplication keystroke `{{key:ENTER}}` executes one of three deterministic vector transitions **(Eq. A.1)**–**(Eq. A.3)**:

$$\mathbf{S}_{\text{unary}}' = \begin{bmatrix} f(X) \\ Y \\ Z \\ T \end{bmatrix}, \qquad \text{LASTX}' \leftarrow X, \qquad \mathcal{L}_{\text{lift}}' \leftarrow \text{TRUE}$$

$$\mathbf{S}_{\text{dyadic}}' = \begin{bmatrix} g(Y, X) \\ Z \\ T \\ T \end{bmatrix}, \qquad \text{LASTX}' \leftarrow X, \qquad \mathcal{L}_{\text{lift}}' \leftarrow \text{TRUE}$$

$$\mathbf{S}_{\text{ENTER}}' = \begin{bmatrix} X \\ X \\ Y \\ Z \end{bmatrix}, \qquad \text{LASTX}' \leftarrow \text{LASTX}, \qquad \mathcal{L}_{\text{lift}}' \leftarrow \text{FALSE}$$

Each vector equation specifies the complete post-keystroke register state:
* **Unary In-Place Transformation (Eq. A.1):** A single-operand function $f(X)$ (such as `{{key:√x}}`, `{{key:LN}}`, `{{key:SIN}}`, or `{{key:1/x}}`) overwrites Register $X$ with $f(X)$ while leaving the upper registers $Y, Z,$ and $T$ completely untouched, snapshots the pre-operation value of $X$ into `LASTX`, and sets $\mathcal{L}_{\text{lift}}' \leftarrow \text{TRUE}$ so the next number typed will lift $f(X)$ into Register $Y$.
* **Dyadic Collapse & Top-Register Replication (Eq. A.2):** A two-operand binary operation $g(Y, X)$ (such as `{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`, `{{key:yˣ}}`, or `{{key:x∥y}}`) consumes $Y$ and $X$ to write $g(Y, X)$ into Register $X$, drops the upper stack downward by one level ($Y' \leftarrow Z$ and $Z' \leftarrow T$) while retaining the top register ($T' \leftarrow T$, enabling automatic constant replication across Horner polynomials and repeated scaling factors), saves the consumed $X$ operand into `LASTX`, and sets $\mathcal{L}_{\text{lift}}' \leftarrow \text{TRUE}$.
* **Explicit Stack Push & Lift Disarm (Eq. A.3):** Pressing `{{key:ENTER}}` pushes the stack upward by one register ($T' \leftarrow Z,\; Z' \leftarrow Y,\; Y' \leftarrow X$, discarding the old $T$) so that $X$ is duplicated in both Registers $X$ and $Y$, leaves `LASTX` unchanged, and sets $\mathcal{L}_{\text{lift}}' \leftarrow \text{FALSE}$ so that the next digit keystroke overwrites the temporary copy in Register $X$ rather than lifting the stack a second time.

Under `{{key:FLAGS}}` $\to$ `STACK` (Flag 5), operational depth can be switched among four deterministic stack profiles:

| Stack Profile | Active Registers | Top-of-Stack Drop Rule | Primary Engineering Use Case |
| :---: | :--- | :--- | :--- |
| **`2-LVL`** | $X, Y$ | Top-register replication ($Y' \leftarrow Y$) on dyadic drop | Minimalist two-operand accumulator workflows |
| **`4-LVL`** (Default) | $X, Y, Z, T$ | $Z' \leftarrow T,\; T' \leftarrow T$ ($T$-replication) | Classical 4-register RPN, Horner evaluation, constant scaling |
| **`8-LVL`** | $X, Y, Z, 4 \dots 7, T$ | $7' \leftarrow T,\; T' \leftarrow T$ ($T$-replication) | Four-level complex phasor networks (`CMPLX`) and 8-register expressions |
| **`INF`** | $X, Y, Z, 4 \dots 999$ (999-register dynamic stack) | Dyadic drops pull zero-initialized upper levels ($T' \leftarrow R_5$) without duplicating $T$ at level 4 | Arbitrary-depth expression trees and multi-branch series |

For the Horner cubic $P(x) = ((2x - 5)x + 3)x + 7$ at $x = 3$, the four-register trace shows how `{{key:ENTER}}` (`DISABLES` lift, **Eq. A.3**) and dyadic operators (`ENABLES` lift with $T$-replication, **Eq. A.2**) cooperate across all four registers:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}} 2` | $3$ | $3$ | $3$ | $2$ | Fill stack with $x = 3$; disabling lift after third `ENTER` lets `2` overwrite $X$ |
| `{{key:×}} 5 {{key:-}}` | $3$ | $3$ | $3$ | $1$ | First Horner stage $2(3) - 5 = 1$; $T$-replication preserves $x = 3$ in $Y, Z, T$ |
| `{{key:×}} 3 {{key:+}}` | $3$ | $3$ | $3$ | $6$ | Second Horner stage $1(3) + 3 = 6$; $x = 3$ remains staged in Register $Y$ |
| `{{key:×}} 7 {{key:+}}` | $3$ | $3$ | $3$ | **$25$** | Final cubic evaluation $P(3) = 6(3) + 7 = 25$ with $x = 3$ still in $Y, Z, T$ |
