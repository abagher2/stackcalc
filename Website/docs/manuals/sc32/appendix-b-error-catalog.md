---
title: "Appendix B: Error Catalog & Singularity Analysis | Thinking in the Stack (SC-32)"
description: "Comprehensive catalog of all 12 hardware error codes, mathematical singularities, and non-destructive recovery procedures on the StackCalc SC-32."
---

# Appendix B: Error Catalog & Singularity Analysis

The StackCalc SC-32 (**Figure B.1**) implements non-destructive error recovery across all arithmetic, transcendental, statistical, financial, and iterative subsystems. Because every RPN operation evaluates one step at a time on Registers $Y$ and $X$, the processor validates the mathematical domain *before* mutating the stack:
1. **Diagnostic Banner & Pre-Mutation Trap:** Posts the descriptive error message to the LCD status line and halts the operation before mutating operational memory.
2. **Register Preservation & Single-Key Dismissal:** Freezes all four operational registers ($X, Y, Z, T$) and `LASTX` without modification; pressing `{{key:C}}` or `{{key:<-}}` clears the error banner without side effects, while pressing any other key clears the banner and executes its normal function.

{{blocks:sc32_exploded_assembly|Exploded hardware assembly showing the internal keypad matrix, display module, and continuous memory architecture.}}

---

## Hardware Error Codes, Boundary Conditions & Recovery Reference

Each of the twelve hardware diagnostic codes (`Code 01` through `Code 12`) preserves the pre-operation state of Registers $X, Y, Z, T$, `LASTX`, and all named storage registers:

| Error Code | Banner Designation | Triggering Domain / Boundary Condition | Stack & Register State | Non-Destructive Recovery Protocol |
| :--- | :--- | :--- | :--- | :--- |
| **Code 01** | `DIVIDE BY 0` | Domain Violation: $Y \div 0$, $1/0$, $\ln(0)$, $\log_{10}(0)$, $0^X$ ($X < 0$), $X \parallel Y$ ($X + Y = 0$), or $\Delta\%$ ($Y = 0$). | Pre-operation $X$ and $Y$ preserved; `LASTX` unchanged. | Press `{{key:C}}`; key non-zero divisor (overwrites $X$) and press `{{key:÷}}`. |
| **Code 02** | `INVALID DATA` | Real-domain violations: $\sqrt{X}$ ($X < 0$), $Y^X$ ($Y < 0, X \notin \mathbb{Z}$), $\ln X$/$\log_{10} X$ ($X < 0$), $\arcsin X$/$\arccos X$ ($\lvert X\rvert > 1$), $\operatorname{acosh} X$ ($X < 1$), $\operatorname{atanh} X$ ($\lvert X\rvert \ge 1$), $\tan((2k+1)90^\circ)$, $X! = \Gamma(X+1)$ at $X \in \{-1, -2, \dots\}$, or $C_{n,r}, P_{n,r}$ domain violations ($r > n$, $n < 0$, or $r < 0$). | All four registers ($X, Y, Z, T$) frozen with offending argument in $X$. | Press `{{key:C}}`; arm `{{key:CMPLX}}` and re-invoke for complex evaluation, or press `{{key:+/-}}`. |
| **Code 03** | `OVERFLOW` | Magnitude exceeds IEEE-754 ceiling $\approx 1.798 \times 10^{308}$ (e.g., $X! > 170!$, $e^X$ for $X > 709.78$, or $10^X$ for $X > 308.25$). | Pre-operation operands remain frozen in $Y$ and $X$. | Press `{{key:C}}`; rescale operands or evaluate in logarithmic space ($\ln(n!)$). |
| **Code 04** | `TOO BIG` | Switching into `HEX`, `OCT`, or `BIN` (`{{key:BASE}}`) while $X$ lies outside signed 36-bit range $[-2^{35}, +2^{35}-1]$. | Full 64-bit floating-point value remains preserved in Register $X$. | Press `{{key:C}}`; stay in `DEC` or reduce modulo $2^{36}$ via `{{key:÷R}}` before base conversion. |
| **Code 05** | `STAT ERROR` | Computing $\bar{x}, \bar{y}$ with $n = 0$; $\sigma_x, \sigma_y$ requested with $n < 1$; sample $s_x, s_y$ with $n < 2$; $\bar{x}_w$ requested with $\Sigma y = 0$; linear regression (`L.R.`) when all $x_i$ are identical ($\sigma_x = 0$); or correlation $r$ or $\hat{x}$ requested when all $y_i$ are identical ($\sigma_y = 0$, $m = 0$). | All 6 statistical accumulators ($\Sigma$) and stack preserved. | Press `{{key:C}}`; accumulate additional $(x_i, y_i)$ pairs via `{{key:Σ+}}`, or use $\sigma_x$ (`{{key:s,σ}}`). |
| **Code 06** | `NO ROOT FOUND` | Convergence Failure: `{{key:SOLVE}}` fails to bracket a sign change $f(a)\cdot f(b) \le 0$ within $50$ expansion steps, or Brent's method completes $100$ iterations without converging to a true root. | Stack and target variable restored to pre-`SOLVE` values; stored `EQN` preserved. | Press `{{key:C}}`; sample $f(x)$ via `{{key:XEQ}}` to locate a sign-change neighborhood, store a closer seed via `{{key:STO}}` + letter, and re-run `{{key:SOLVE}}`. |
| **Code 07** | `A ≠ 0` | Invoking `{{key:XEQ}}` in `{{key:POLY}}` ($Ax^3 + Bx^2 + Cx + D = 0$) when both $A = 0$ and $B = 0$. | Stored coefficients `A`, `B`, `C`, `D` remain untouched. | Press `{{key:C}}`; store non-zero $A$ (cubic) or $B$ (quadratic) and press `{{key:XEQ}}`. |
| **Code 08** | `ERROR 5` | Financial Singularity: Cash-flow sign violation in `{{key:TVM}}` when solving for `N` or `I%` (all nonzero cash flows share the same sign), $N = 0$ when solving for `PMT`/`I%`, or periodic rate $i \le -100\%$. | All five `TVM` registers (`N`, `I%`, `PV`, `PMT`, `FV`) and stack preserved. | Press `{{key:C}}`; negate outflows via `{{key:+/-}}`, re-store, and re-solve. |
| **Code 09** | `MEMORY FULL` | Allocating a 25th equation in `{{key:EQN}}` or exceeding the flash token sector budget. | All 24 existing equations, variables `A`–`Z`, and stack remain preserved. | Press `{{key:C}}`; open `{{key:EQN}}`, select an unused equation, and delete via `{{key:CLEAR}}` $\to$ `{{key:CLEQN}}`. |
| **Code 10** | `TIMEOUT` | Execution Watchdog: Symbolic equation evaluation (`EQN`, `{{key:SOLVE}}`, or `{{key:∫}}`) exceeds the 100,000-instruction-cycle hardware watchdog (e.g., an infinite backward `GTO` loop). | Execution aborted; pre-operation stack preserved. | Press `{{key:C}}`; inspect the active equation in `{{key:EQN}}` and remove any unconditional backward branch loop. |
| **Code 11** | `INTERRUPTED` | Pressing `{{key:C}}` while an iterative `{{key:SOLVE}}`, `{{key:∫}}`, or `{{key:POLY}}` sweep is executing. | Temporary scratch state discarded; $X, Y, Z, T$ restored. | Press `{{key:C}}` once more to clear `INTERRUPTED` and resume keypad operation. |
| **Code 12** | `NO EQN` / `INVALID FOR EQN` / `INTEGER REQUIRED` | Mode / Domain Guard: `{{key:SOLVE}}` or `{{key:∫}}` invoked with an empty equation bank (`NO EQN`); disallowed mode or mutating store command (`{{key:STO}}`) pressed during equation entry (`INVALID FOR EQN`; `{{key:RCL}}` and recall arithmetic `RCL +`/`-`/`×`/`÷` are allowed so iterative `SOLVE`, `∫`, and `PLOT` evaluations remain side-effect-free); or non-integer argument passed to `GCD` or `LCM` (`INTEGER REQUIRED`). | Operands in $Y$ and $X$ remain frozen at pre-operation values. | Press `{{key:C}}`; select a valid equation in `{{key:EQN}}`, replace `{{key:STO}}` with `{{key:RCL}}` inside `EQN`, or strip fractions via `{{key:PARTS}}` $\to$ `{{key:IP}}`. |

## Code 09: MEMORY FULL & SC-32 Hardware Recovery Protocols

The SC-32 stores up to 24 persistent postfix equations in flash memory (`{{key:EQN}}`), alongside 26 variables (`A`–`Z`), pointer `i`, 6 statistical sums, 50 data slots (`DATA0`–`DATA49`), and 5 `TVM` registers. When `MEMORY FULL` (Code 09) occurs, allocation halts before overwriting flash; pressing `{{key:C}}` dismisses the banner, and `{{key:CLEAR}}` $\to$ `{{key:CLEQN}}` reclaims equation slots:

| Reset Level | Keystroke Sequence | Operational Scope & State Preserved |
| :--- | :--- | :--- |
| **1. Soft Status Clear** | Press `{{key:C}}` twice | Cancels active menu prompts, dismisses error banners, and clears pending `{{key:↰}}`/`{{key:↱}}` shifts without erasing variables, statistics, equations, or the stack. |
| **2. Selective Workspace Clear** | `{{key:CLEAR}}` (`{{key:↰}}` + `{{key:<-}}`) | Opens six targeted reset softkeys: `CLEQN` (clears the stored equation bank), `CLVARS` / `CLV` (zeroes `A`–`Z` and `TVM` registers), `CLALL`, `CLSTAT` (zeroes 6 statistical sums, equivalent to `{{key:CLΣ}}`), `CLREGS` (zeroes `A`–`Z` and `TVM` registers), and `CLSTK` (zeroes $T, Z, Y, X$). |
| **3. Full Factory Baseline (`CLALL` / `EXAM`)** | Hold `{{key:C}}` at power-on, or `{{key:CLEAR}}` $\to$ `{{key:CLALL}}` | Erases all variables `A`–`Z`, statistical accumulators, `TVM` registers, stored equations, and the stack, returning angular mode to `DEG` and display format to `ALL`, and verifies the dual $32\text{ KiB}$ flash FNV-1a checksum. |

---

## Mathematical Singularity Conditioning & Overflow Rescaling

When an engineering calculation encounters an IEEE-754 floating-point ceiling (`OVERFLOW`, **Code 03**) or a removable $0/0$ indeterminate form (`DIVIDE BY 0`, **Code 01**), algebraic domain conditioning resolves the expression without losing double-precision significance:

1. **Logarithmic Stirling Rescaling Beyond the $170!$ Factorial Ceiling (`Code 03`, Eq. B.1):** Because $171! \approx 1.241 \times 10^{309}$ exceeds the IEEE-754 double-precision maximum $D_{\max} \approx 1.798 \times 10^{308}$, large combinatorial ratios and hypergeometric probabilities for integer count $n > 170$ are conditioned in natural-logarithm space by converting the product $n! = \prod_{k=1}^n k$ into a sum of logarithms $\ln(n!) = \sum_{k=1}^n \ln k$ and applying Pierre-Simon Laplace and James Stirling's asymptotic series **(Eq. B.1)**:

   $$\ln(n!) = \sum_{k=1}^{n} \ln k \approx n\ln n - n + \frac{1}{2}\ln(2\pi n) + \frac{1}{12n} - \frac{1}{360n^3}$$

   The continuous integral $\int_1^n \ln x\,dx = n\ln n - n$ supplies the dominant growth rate, the half-logarithm $\frac{1}{2}\ln(2\pi n)$ corrects for the trapezoidal midpoint offset across the discrete steps $k = 1 \dots n$, and the reciprocal Bernoulli terms $+\frac{1}{12n} - \frac{1}{360n^3}$ cancel the remaining curvature error to better than $15$ significant digits for $n \ge 10$; dividing $\ln(n!)$ by $\ln 10$ then separates the base-10 exponent $\operatorname{IP}(\log_{10} n!)$ from the mantissa $10^{\operatorname{FP}(\log_{10} n!)}$.

2. **Removable Coordinate Singularities & Secant Regularization (`Code 01`, Eq. B.2):** Near removable $0/0$ singularities—such as the optical diffraction sinc limit $\lim_{x \to 0}\frac{\sin x}{x} = 1$ (for radian angle $x$) or the thermal radiation Planck factor $\lim_{u \to 0}\frac{u}{e^u - 1} = 1$ (for dimensionless photon-energy ratio $u = hc/(\lambda k_B T)$)—direct substitution at $x = 0$ or $u = 0$ traps on `DIVIDE BY 0` (`Code 01`). Dismissing the banner via `{{key:C}}` and perturbing $x$ by $\delta = 10^{-7}$ (or expanding the Maclaurin power series, **Eq. B.2**) cancels the vanishing factor from numerator and denominator to recover full precision on the stack:

   $$\frac{\sin x}{x} = 1 - \frac{x^2}{6} + \frac{x^4}{120} - \mathcal{O}(x^6), \qquad \frac{u}{e^u - 1} = 1 - \frac{u}{2} + \frac{u^2}{12} - \mathcal{O}(u^4)$$

   Factoring out the leading linear term leaves the exact limiting value $1$ at the origin, followed by smooth polynomial corrections ($-x^2/6$ for the symmetric sinc peak and $-u/2 + u^2/12$ for the Rayleigh–Jeans thermal slope) that evaluate without division by zero:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `200 {{key:LN}} 200 {{key:×}} 200 {{key:-}}` | $0$ | $0$ | $0$ | $859.663$ | Leading Stirling terms $n\ln n - n$ for $n = 200$ (beyond $170!$ ceiling) |
| `2 {{key:π}} {{key:×}} 200 {{key:×}} {{key:LN}} 2 {{key:÷}} {{key:+}} 2400 {{key:1/x}} {{key:+}}` | $0$ | $0$ | $0$ | $863.232$ | Add $\frac{1}{2}\ln(2\pi n) + \frac{1}{12n} \approx 3.569$: $\ln(200!) \approx 863.232$ |
| `10 {{key:LN}} {{key:÷}}` | $0$ | $0$ | $0$ | **$374.897$** | Convert to base-10 log: $\log_{10}(200!) \approx 374.897 \implies 200! \approx 7.886 \times 10^{374}$ |
