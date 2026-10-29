---
title: "Appendix B: Error Catalog & Singularity Analysis | Thinking in the Stack (SC-32)"
description: "Comprehensive catalog of all 12 hardware error codes, mathematical singularities, and non-destructive recovery procedures on the StackCalc SC-32."
---

# Appendix B: Error Catalog & Singularity Analysis

{{blocks:sc32_exploded_assembly|Exploded hardware assembly showing the internal keypad matrix, display module, and continuous memory architecture.}}

---

## The Non-Destructive Error Recovery Principle & Domain Singularities

On vintage or poorly engineered consumer calculators, encountering an arithmetic singularity—such as dividing by zero, taking a logarithm of a negative number, or exceeding the floating-point exponent ceiling—triggers a catastrophic reset: the operational display flashes an error code, intermediate calculations are wiped, and the user is forced to re-key multi-step expressions from the beginning.

The StackCalc SC-32 enforces an absolute architectural invariant: **The Non-Destructive Error Recovery Principle**. Because every operation in Reverse Polish Notation evaluates one step at a time on the values sitting in Registers $Y$ and $X$, the processor checks the mathematical domain *before* mutating your stack.

### The Non-Destructive Error Recovery Guarantee

When any of the 12 hardware error conditions occurs:
1. The descriptive error message is posted to the status line of the transflective LCD.
2. The operation causing the exception is halted **before** mutating operational memory.
3. **All four operational stack registers ($X, Y, Z, T$) and `LASTX` are frozen intact.**
4. Pressing `{{key:C}}` or `{{key:<-}}` **dismisses the error banner** and restores your exact prior stack.

You can then inspect your operands, swap values via `{{key:x⇄y}}`, change a sign via `{{key:+/-}}`, or re-key the intended operator **without** losing a single intermediate calculation.

| Feature / Behavior | StackCalc SC-32 | Vintage HP-32SII | Conventional Algebraic Calculator (Infix) |
| :--- | :--- | :--- | :--- |
| **Stack Preservation** | 100% frozen; zero register mutation | Frozen stack | Stack cleared or lost in syntax tree |
| **Recovery Keystroke** | Single `{{key:C}}` or `{{key:<-}}` restores display | `{{key:C}}` or `{{key:<-}}` restores | Requires quitting or clearing editor |
| **Operand Inspection** | Operands remain visible in $X$ and $Y$ | Operands remain | Operands often must be retyped |
| **LASTX Protection** | Prior valid $X$ retained safely | Prior valid $X$ retained | No dedicated `LASTX` register |
| **Shift/Prefix Clearance**| `{{key:C}}` cancels pending prefix harmlessly | `{{key:C}}` cancels | Keypad state unclear |

> **Hardware & Stack Verification:**  
> If you accidentally divide by zero, do **not** turn off the calculator or clear your stack. Press `{{key:C}}`. Your numerator is still resting safely in Register $Y$, and the zero is in Register $X$. You can overwrite the zero or swap registers on the spot.

### Overview of the 12 Hardware Error Codes

Every hardware error code on the SC-32 corresponds to a deterministic mathematical domain singularity or hardware boundary:

| Error Code | Designation | Error Code | Designation | Error Code | Designation |
|:---|:---|:---|:---|:---|:---|
| Code 01 | `DIVIDE BY 0` | Code 05 | `STAT ERROR` | Code 09 | `MEMORY FULL` |
| Code 02 | `INVALID DATA` | Code 06 | `NO ROOT FOUND` | Code 10 | `TIMEOUT` |
| Code 03 | `OVERFLOW` | Code 07 | `A ≠ 0` | Code 11 | `INTERRUPTED` |
| Code 04 | `TOO BIG` | Code 08 | `ERROR 5` *(HP-12C TVM)* | Code 12 | `NO NEG` / `EQN` / `INT` Guards |

---

### Code 01: DIVIDE BY 0 (Division by Zero & Pole Singularities)
* **Why the Singularity Happens:** Division asks how many times a divisor $x$ fits into a dividend $y$. As $x$ shrinks toward zero ($0.1, 0.001, 10^{-12}$), the quotient $y/x$ explodes without bound toward $+\infty$ from one side and $-\infty$ from the other, meaning $y/0$ has no finite value on the real number line. The same vertical asymptote (a *pole singularity*) appears inside disguised quotients across algebra and trigonometry:
  * **Direct Division & Reciprocals:** $y \div 0$ (`{{key:÷}}`), integer remainder division $y \;\text{rem}\; 0$ (`{{key:÷R}}`), or multiplicative reciprocal $1/0$ (`{{key:1/x}}`).
  * **Trigonometric Poles on the Unit Circle:** Because $\tan\theta = \frac{\sin\theta}{\cos\theta}$, evaluating $\tan(90^\circ)$ or $\tan(270^\circ)$ in Degrees mode divides the vertical height $\sin(90^\circ) = 1$ by the horizontal shadow $\cos(90^\circ) = 0$, shooting the tangent line vertically to $\pm\infty$.
  * **Logarithmic Origin Pole:** Evaluating $\ln(0)$ or $\log_{10}(0)$ asks what power of $e$ or $10$ equals zero; as $x \to 0^+$, the logarithm plunges vertically to $-\infty$.
  * **Zero Base with Non-Positive Exponent:** Evaluating $0^y$ for $y \le 0$ (such as $0^{-2} = 1/0^2$) places zero in the denominator.
* **IEEE-754 Protection:** Rather than silently polluting your stack with `NaN` or `Inf` symbols that ruin subsequent calculations, the hardware trap intercepts the operation before mutating any register.
* **Stack State & Recovery Procedure:**
  1. Register $X$ holds `0.0000` (the offending divisor or argument), Register $Y$ holds your original numerator untouched, and `LASTX` preserves the $X$ value from your previous completed calculation.
  2. Press `{{key:C}}` to dismiss the `DIVIDE BY 0` banner.
  3. Key the intended non-zero divisor (e.g., `{{key:1}} {{key:5}}`)—since stack lift remains disabled or overwrites in place after `{{key:C}}`—and press `{{key:÷}}`.

For example, suppose you are computing $\frac{450}{15}$, but mistakenly key $0$ as the divisor:

| Step | Keystroke | Display Output | Register X | Register Y | Register Z |
| :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | `{{key:4}} {{key:5}} {{key:0}} {{key:ENTER}}` | `450.0000` | `450.0000` | `450.0000` | `0.0000` |
| 2 | `{{key:0}} {{key:÷}}` | `DIVIDE BY 0` | `0.0000` | `450.0000` | `0.0000` |
| 3 | `{{key:C}}` | `0.0000` | `0.0000` | `450.0000` | `0.0000` |
| 4 | `{{key:1}} {{key:5}} {{key:÷}}` | `30.0000` | `30.0000` | `0.0000` | `0.0000` |

---

### Code 02: INVALID DATA (Real-Valued Domain Violations)
* **Why the Singularity Happens:** Many mathematical functions are defined only on a specific interval of the real number line $\mathbb{R}$, and stepping outside that interval asks a question that has no real-number answer:
  * **Even Roots of Negative Numbers ($\sqrt{x}$ for $x < 0$):** Because the square of any real number—positive or negative—is always non-negative ($x^2 \ge 0$), no point on the real line squares to $-16$.
  * **Logarithms of Negative Numbers ($\ln x$ or $\log_{10} x$ for $x < 0$):** Because $e \approx 2.718$ and $10$ are strictly positive bases, raising them to any real exponent $y$ always produces a strictly positive result ($e^y > 0$). Thus $\ln x$ exists on the real line only for $x > 0$.
  * **Inverse Sine & Cosine Outside $[-1, +1]$ ($\arcsin x$ or $\arccos x$ for $|x| > 1$):** On the unit circle of radius $1$, the vertical leg $\sin\theta$ and horizontal leg $\cos\theta$ can never exceed the hypotenuse of length $1$. Asking for an angle whose sine is $1.5$ violates the triangle inequality.
  * **Gamma Poles & Combinatorial Boundaries:** Factorials of negative integers $(-n)!$ hit poles of Euler's Gamma function $\Gamma(x+1)$, and combinations $\binom{n}{r}$ (`{{key:Cn,r}}`) or permutations $P(n,r)$ (`{{key:Pn,r}}`) cannot choose $r > n$ items or negative counts.
* **Stack State & Recovery Procedure:**
  1. All four registers remain frozen with the offending argument in Register $X$.
  2. Press `{{key:C}}` to clear the error banner.
  3. **If you intended a complex-plane calculation:** Arm the complex prefix by pressing `{{key:CMPLX}}`, then re-execute the function. For example, with `-16` in $X$, pressing `{{key:CMPLX}} {{key:√x}}` steps off the real line into the Gaussian plane and returns $0 + 4i$ (`0` in $Y$, `4` in $X$).
  4. **If you made a sign error:** Press `{{key:+/-}}` to flip the sign in $X$ and press the function key again.

---

### Code 03: OVERFLOW (Floating-Point Magnitude Ceiling)
* **Why the Singularity Happens:** In 64-bit IEEE-754 double-precision arithmetic, 11 bits are allocated to the binary exponent, providing a maximum finite magnitude of $(2 - 2^{-52}) \times 2^{1023} \approx 1.7976931348623157 \times 10^{308}$. Exponential and factorial functions grow so rapidly that modest inputs cross this threshold:
  * **Factorials (`{{key:x!}}`):** $170! \approx 7.2574 \times 10^{306}$ fits in Register $X$, whereas $171! \approx 1.2410 \times 10^{309}$ exceeds $10^{308}$.
  * **Natural & Common Exponentials:** $e^x$ overflows for $x > 709.782712893384$ ($\ln(1.7977 \times 10^{308})$), and $10^x$ overflows for $x > 308.2547155599167$.
* **Stack State & Recovery Procedure:**
  1. Press `{{key:C}}` to dismiss the `OVERFLOW` banner; your unscaled operands remain intact in $Y$ and $X$.
  2. Work in logarithmic space (for example, using Stirling's approximation $\ln(n!) \approx n\ln n - n + \frac{1}{2}\ln(2\pi n)$ or adding logarithms $\log_{10}(a \times b) = \log_{10} a + \log_{10} b$) so huge exponents never overflow the hardware mantissa.

---

### Code 04: TOO BIG (36-Bit Two's-Complement Word Overflow)
* **Why the Singularity Happens:** When operating in Computer Science integer base modes (`HEX`, `OCT`, `BIN`), the SC-32 models a classic 36-bit signed two's-complement architecture, where 1 bit represents the sign and 35 bits represent magnitude:
  $$\text{Signed 36-Bit Range: } -2^{35} = -34,359,738,368 \;\;(\text{0x800000000}) \;\;\text{to}\;\; +2^{35}-1 = +34,359,738,367 \;\;(\text{0x7FFFFFFFF})$$
  Attempting to switch from `DEC` into `HEX`, `OCT`, or `BIN` while Register $X$ holds a floating-point number outside $[-2^{35}, 2^{35}-1]$ triggers `TOO BIG`.
* **Stack State & Recovery Procedure:**
  1. Press `{{key:C}}` to dismiss the message; your full floating-point value remains intact in Register $X$.
  2. Remain in `{{key:BASE}} {{key:DEC}}` for arbitrary floating-point magnitudes, or reduce the integer modulo $2^{36}$ before converting to hexadecimal or binary.

---

## Statistical, Iterative Solver & Financial Singularity Traps

While Codes 01–04 protect single-step arithmetic and transcendental functions, Codes 05–08 guard multi-variable statistical accumulators, numerical root-finders, polynomial solvers, and compound-interest financial registers.

### Code 05: STAT ERROR (Degrees-of-Freedom & Vertical-Line Singularities)
* **Why the Singularity Happens:** Statistical summaries condense a cloud of $n$ data points into a center and a spread, which requires enough independent observations to define those geometric quantities:
  * **Sample Mean with Empty Data ($n = 0$):** Computing $\bar{x} = \frac{\sum x_i}{n}$ when no points have been accumulated via `{{key:Σ+}}` divides $0/0$.
  * **Sample Standard Deviation with a Single Point ($n < 2$):** Sample standard deviation uses Friedrich Bessel's correction in the denominator:
    $$s_x = \sqrt{\frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n - 1}}$$
    Why $n - 1$ instead of $n$? Because the sample mean $\bar{x}$ is calculated from the data itself, which uses up $1$ degree of freedom. If you have only $n = 1$ data point, that point sits exactly on its own mean ($x_1 = \bar{x}$), giving zero apparent spread and a denominator of $n - 1 = 0$. You need at least $n = 2$ points to measure a distance between measurements!
  * **Linear Regression with Identical $x$-Coordinates ($\sigma_x = 0$):** Fitting a line $\hat{y} = a + bx$ requires at least two distinct $x$-values. If all entered $(x_i, y_i)$ pairs share the same $x$-coordinate, the points stack in a vertical column of infinite slope ($b = \Delta y / 0$), and Pearson's correlation $r = \frac{s_{xy}}{s_x s_y}$ divides by $s_x = 0$.
* **Stack State & Recovery Procedure:**
  1. Press `{{key:C}}` to dismiss; all six statistical accumulators ($\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$) and the stack remain intact.
  2. Inspect your current sample count via `{{key:SUMS}}` (`n` on `{{key:LFU5}}`) and add at least a second distinct data point with `{{key:Σ+}}`, or use population standard deviation $\sigma_x$ (`{{key:s,σ}}` $\to$ `σx`) if a single-point population divisor $n = 1$ is intended.

---

### Code 06: NO ROOT FOUND (Unbracketed Zero-Crossing in Brent's Solver)
* **Why the Singularity Happens:** Richard Brent's hybrid root-finding algorithm (`{{key:SOLVE}}`) combines the guaranteed convergence of bisection with the rapid superlinear speed of secant and inverse quadratic interpolation. By the **Intermediate Value Theorem**, a continuous function $f(x)$ is guaranteed to cross the horizontal axis ($f(x^*) = 0$) inside an interval $[a, b]$ if and only if $f(a)$ and $f(b)$ have *opposite algebraic signs* ($f(a) \cdot f(b) < 0$—one point above the axis, one point below). `NO ROOT FOUND` occurs when:
  * The curve never crosses the real axis at all (for example, $f(x) = x^2 + 4 > 0$ for every real $x$).
  * Your two starting guesses in Registers $Y$ and $X$ sit on the same side of the root ($f(a) \cdot f(b) > 0$), and 100 secant steps fail to locate a sign reversal.
* **Stack State & Recovery Procedure:**
  1. Press `{{key:C}}` to clear the banner; the solver deposits its closest candidate $x$ in Register $X$ while preserving your equation.
  2. Open the interactive graphic plotter via `{{key:PLOT}}` to inspect the curve across $[X_{\min}, X_{\max}]$ and see visually where the graph crosses the horizontal axis.
  3. Exit `{{key:PLOT}}`, enter two new bracket guesses $a$ (`{{key:ENTER}}`) and $b$ that straddle opposite sides of the crossing, and press `{{key:SOLVE}}`.

---

### Code 07: A ≠ 0 (Degenerate Leading Coefficient in POLY Solver)
* **Why the Singularity Happens:** In the characteristic polynomial workspace (`{{key:POLY}}`), a cubic equation $A x^3 + B x^2 + C x + D = 0$ is normalized by dividing through by its highest non-zero leading coefficient ($A$ for a cubic, or $B$ when $A = 0$ for a quadratic). If both $A = 0$ and $B = 0$ (or when a cubic normalization requires a non-zero leading coefficient), dividing by zero is undefined because the polynomial degree collapses.
* **Stack State & Recovery Procedure:**
  1. Press `{{key:C}}` to dismiss; your stored coefficients in `A`, `B`, `C`, and `D` remain untouched.
  2. Store a non-zero leading coefficient and press `{{key:LFU4}}` (`EXEC`). Note that `{{key:POLY}}` solves quadratics $bx^2 + cx + d = 0$ either natively by setting cubic coefficient $A = 0$ (`0 {{key:A}}`) and entering $(B, C, D)$, or by entering $(A, B, C)$ with $D = 0$ (`0 {{key:D}}`, factoring $x(Ax^2 + Bx + C) = 0$). All three analytical roots $(r_1, r_2, r_3)$—including complex conjugate pairs—are written to indirect registers `R34`–`R39` (`34`–`35` for $\text{Re}(r_1), \text{Im}(r_1)$, `36`–`37` for $r_2$, and `38`–`39` for $r_3$) and can be browsed in the `{{key:REGS}}` (`{{key:0}}` or `{{key:MEM}}` $\to$ `REGS`, `STO` tab) catalog or recalled via indirect addressing (`34 {{key:STO}} i`, `{{key:RCL}} (i)`).

---

### Code 08: ERROR 5 (Cash-Flow Sign Violation in Time Value of Money)
* **Why the Singularity Happens:** The Time Value of Money (`{{key:TVM}}`) equation balances present value ($PV$), periodic payments ($PMT$), and future value ($FV$) discounted at periodic rate $i$. The display message `ERROR 5` intentionally preserves the classic HP-12C actuarial error designation for TVM cash-flow sign violations where `PV`, `PMT`, and `FV` all share the same sign:
  $$PV + PMT \left[\frac{1 - (1+i)^{-N}}{i}\right] + FV(1+i)^{-N} = 0$$
  Here the right-hand side is **zero**. If you enter $PV > 0$, $PMT > 0$, and $FV \ge 0$ (all positive), you are asking the solver to find an interest rate where money flows *only toward you* and never leaves your pocket—a sum of strictly positive numbers can never add up to zero for any real interest rate $i > -100\%$.
* **Stack State & Recovery Procedure:**
  1. Press `{{key:C}}` to dismiss; all five financial registers (`N`, `I%`, `PV`, `PMT`, `FV`) remain intact.
  2. Enforce the **Cash-Flow Sign Convention**: cash *received* (such as a loan principal $PV$) is positive, and cash *paid out* (such as monthly mortgage payments $PMT$ or a savings deposit) is negative (`{{key:+/-}}`). Flip the sign of the outflow variable, store it back into its TVM softkey, and solve again.

---

## Memory, Quadrature & Hardware Diagnostic Recovery Protocols

The final four error codes (`Codes 09–12`) handle non-volatile equation bank capacity, numerical integration convergence limits, manual user interrupts, and unsigned educational boundaries, followed by the three hardware reset levels.

### Code 09: MEMORY FULL (Equation Bank Capacity Reached)
* **Triggering Keystrokes:** Pressing `{{key:EQN}}` (Right Shift `{{key:↱}}` above `{{key:STO}}`) and attempting to create a 25th stored equation or exceed the flash equation token budget.
* **Why the Singularity Happens:** The SC-32 stores up to 24 persistent user-defined postfix equations in continuous flash memory (`{{key:EQN}}`). Attempting to allocate a 25th equation slot or exceed the flash sector step budget triggers `MEMORY FULL`.
* **Non-Destructive Recovery:**
  1. Press `{{key:C}}` to dismiss; all existing equations, variables `A`–`Z`, and the stack remain 100% intact.
  2. Open the equation bank (`{{key:EQN}}`), scroll to a temporary or obsolete equation, and delete it via `{{key:CLEAR}}` $\to$ `CLEQN` (`{{key:LFU0}}`).

---

### Code 10: TIMEOUT (Romberg Quadrature Subdivision Exhaustion)
* **Triggering Keystrokes:** Invoking `{{key:∫}}` (Right Shift `{{key:↱}}` above `{{key:8}}`) on an integrand that fails to converge within the maximum Romberg refinement depth.
* **Why the Singularity Happens:** Adaptive Romberg quadrature (`{{key:∫}}`) repeatedly halves the trapezoid width $h_k = (b-a)/2^k$ and applies Richardson $\frac{4^m T_{k,m-1} - T_{k-1,m-1}}{4^m - 1}$ extrapolation until successive diagonal estimates agree to within $\epsilon = 10^{-9}$. If an integrand has a vertical asymptote inside $[a, b]$, a sharp step discontinuity, or violent high-frequency oscillation (such as $\sin(1/x)$ near $x = 0$), the error estimate may not settle within 100,000 function evaluations.
* **Non-Destructive Recovery:**
  1. Press `{{key:C}}` to dismiss; the finest-grid numerical approximation achieved before timeout is preserved in Register $X$.
  2. Split the integration interval $[a, b]$ at the discontinuity or narrow the bounds around smooth sub-intervals, and sum the piecewise integrals on the stack.

---

### Code 11: INTERRUPTED (Clean User Abort of Iterative Engine)
* **Triggering Keystrokes:** Pressing `{{key:C}}` during an active `{{key:SOLVE}}`, `{{key:∫}}`, `{{key:POLY}}`, or `{{key:PLOT}}` sweep.
* **Why the Singularity Happens:** Pressing `{{key:C}}` while the calculator is actively running a multi-step Romberg integral (`{{key:∫}}`), a Brent root search (`{{key:SOLVE}}`), a cubic solve (`{{key:POLY}}`), or a pixel plot sweep (`{{key:PLOT}}`) halts the iterative loop.
* **Non-Destructive Recovery:**
  1. Temporary solver scratch variables are discarded, and your four operational stack registers ($X, Y, Z, T$) are restored to their pre-execution state.
  2. Press `{{key:C}}` once more to clear the `INTERRUPTED` notice and resume calculation.

---

### Code 12: Unsigned Flag 6 (`NO NEG`), Equation & Integer Guard Banners
* **Triggering Keystrokes:** Subtracting $Y < X$ or pressing `{{key:+/-}}` while System Flag 6 (`NO NEG`) is active (`INVALID DATA` on the SC-32; `CANNOT BE < 0` on the elementary SC-6), invoking `{{key:XEQ}}`, `{{key:SOLVE}}`, `{{key:∫}}`, or `{{key:PLOT}}` without an active equation (`NO EQN`) or with a malformed token stream (`INVALID FOR EQN`), or invoking `{{key:GCD}}` / `{{key:LCM}}` in `PARTS` on a fractional operand (`INTEGER REQUIRED`).
* **Why the Singularity Happens:** When Flag 6 (`NO NEG`, the unsigned whole-number arithmetic profile) is active, negative inputs and results ($Y - X < 0$) are blocked at zero. Likewise, equation engines require a valid stored RPN formula in `{{key:EQN}}` (or a built-in template `0`–`5`), and number-theoretic greatest common divisor (`{{key:GCD}}`) and least common multiple (`{{key:LCM}}`) are defined strictly over the ring of integers $\mathbb{Z}$.
* **Non-Destructive Recovery:**
  1. Press `{{key:C}}` to dismiss the diagnostic banner; both $Y$ and $X$ remain untouched.
  2. For `NO NEG`, press `{{key:x⇄y}}` to swap $Y$ and $X$ or clear Flag 6 (`{{key:FLAGS}}` $\to$ `CF 6`); for `NO EQN` / `INVALID FOR EQN`, enter or select a valid equation in `{{key:EQN}}`; and for `INTEGER REQUIRED`, strip fractional parts via `{{key:PARTS}}` $\to$ `{{key:IP}}` before computing `{{key:GCD}}` or `{{key:LCM}}`.

---

### SC-32 Hardware Recovery Protocols

For collegiate and professional engineering examinations, laboratory baseline resets, or power transitions, the SC-32 provides three graduated reset levels:

1. **Soft Status Clear (Non-Destructive):** Press `{{key:C}}` twice. Cancels any active menu prompt, dismisses error banners, and clears pending `{{key:↰}}` or `{{key:↱}}` shift flags without erasing variables, statistical accumulators, or the stack.
2. **Selective Workspace Clear (`{{key:CLEAR}}` Menu):** Press `{{key:CLEAR}}` (Left Shift `{{key:↰}}` above `{{key:<-}}`) to choose a targeted reset on the six top LFU softkeys:
   * `CLEQN` (`{{key:LFU0}}`): Deletes the selected equation in the Equation Bank.
   * `CLVARS` (`{{key:LFU1}}`) / `CLREGS` (`{{key:LFU4}}`): Zeroes letter storage registers `A`–`Z` (and `CLVARS` also zeroes the five `TVM` financial registers `N`, `I%`, `PV`, `PMT`, `FV`).
   * `CLΣ` (`{{key:LFU3}}`): Zeroes the six statistical accumulators ($\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$).
   * `CLSTK` (`{{key:LFU5}}`): Zeroes stack registers $T, Z, Y, X$ while keeping stored variables intact.
3. **Full Factory Baseline Reset (`CLALL`):** Hold `{{key:C}}` while powering on, or press `{{key:CLEAR}}` $\to$ `CLALL` (`{{key:LFU2}}`). Erases all variables `A`–`Z`, statistical accumulators, TVM financial registers, stored equations, and the stack, returning angular mode to `DEG` and display format to `ALL`. On every power-up, the firmware also verifies the cyclic redundancy checksum of its dual non-volatile state slots, automatically falling back to the last verified atomic snapshot if a battery swap occurred mid-write.

---

Every state transition in Appendix A and every singularity trap in Appendix B is triggered through the SC-32's 43-key dual-shifted physical matrix. Turn next to **[Appendix C: Keycap Directory & How We Built StackCalc](appendix-c-keycap-directory.md)** for the complete row-and-column keycap lookup tables and the open-source engineering story behind the instrument.
