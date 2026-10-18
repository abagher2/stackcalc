---
title: "Appendix B: Error Catalog & Singularity Analysis | SC-32 Manual"
description: "Comprehensive catalog of all 12 hardware error codes, mathematical singularities, and non-destructive recovery procedures on the StackCalc SC-32."
---

# Appendix B: Error Catalog & Singularity Analysis

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 HARDWARE // APPENDIX B: ERROR CATALOG &amp; RECOVERY</span>
  <span class="te-viewport-status text-sky-400">● 12 HARDWARE ERROR CODES &bull; MATHEMATICAL SINGULARITIES &bull; NON-DESTRUCTIVE RECOVERY</span>
</div>

{{blocks:sc32_exploded_assembly|StackCalc SC-32 Internal Hardware Assembly}}
*Figure B.1: Exploded hardware assembly showing dual-slot non-volatile EEPROM and power-fail protection circuits.*

<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>{{key:ALL}}</code> (Full 12-digit scientific mantissa; Standard Base-10 Arithmetic; Degrees angular mode default).
</div>

---

## The Non-Destructive Error Recovery Principle

On vintage or poorly engineered consumer calculators, encountering an arithmetic singularity (such as division by zero or a domain overflow) triggers a catastrophic reset: the operational display flashes an error code, intermediate calculations are wiped, and the user is forced to re-key multi-step expressions from the beginning.

The StackCalc SC-32 enforces an absolute architectural invariant: **The Non-Destructive Error Recovery Principle**.

<div class="admonition note">
<p class="admonition-title">The Non-Destructive Error Recovery Guarantee</p>
<p>When any of the 12 hardware error conditions occurs:</p>
<ol>
  <li>The error message is posted to the status line of the transflective LCD.</li>
  <li>The operation causing the error is halted <strong>before</strong> mutating operational memory.</li>
  <li><strong>All four operational stack registers ($X, Y, Z, T$) are frozen intact.</strong></li>
  <li>Pressing <code>{{key:C}}</code> or <code>{{key:<-}}</code> <strong>dismisses the error</strong> and restores your exact prior stack.</li>
</ol>
<p>You can immediately inspect operands, swap values via <code>{{key:x⇄y}}</code>, or re-key the correct operator <strong>without</strong> losing a single intermediate calculation!</p>
</div>

### Architectural Comparison: Error Handling Across Calculators

| Feature / Behavior | StackCalc SC-32 | Vintage HP-32SII | Consumer Algebraic (TI-84 / Casio) |
| :--- | :--- | :--- | :--- |
| **Stack Preservation** | 100% frozen; zero register mutation | Frozen stack | Stack cleared or lost in syntax tree |
| **Recovery Keystroke** | Single `{{key:C}}` or `{{key:<-}}` restores display | `{{key:C}}` or `{{key:<-}}` restores | Requires quitting or clearing editor |
| **Operand Inspection** | Operands remain in $X$ and $Y$ | Operands remain | Operands often must be retyped |
| **LASTX Protection** | Prior valid $X$ retained safely | Prior valid $X$ retained | No dedicated `LASTX` register |
| **Shift/Prefix Clearance**| `{{key:C}}` cancels pending prefix harmlessly | `{{key:C}}` cancels | Keypad state unclear |

<div class="admonition tip">
<p class="admonition-title">Homeschooler & Student Verification:</p>
<p>If you accidentally divide by zero, do **not panic**! Do not turn off the calculator. Simply press `{{key:C}}`. Your numerator is still resting safely in Register $Y$, and the zero is in Register $X$. You can change the zero or swap registers immediately!</p>
</div>
---

## Comprehensive Catalog of All 12 Hardware Errors

Every hardware error code on the SC-32 corresponds to a deterministic mathematical domain singularity or hardware constraint boundary.

| Error Code | Designation | Error Code | Designation | Error Code | Designation |
|:---|:---|:---|:---|:---|:---|
| Code 01 | `DIVIDE BY 0` | Code 05 | `STAT ERROR` | Code 09 | `MEMORY FULL` |
| Code 02 | `INVALID DATA` | Code 06 | `NO ROOT FOUND` | Code 10 | `TIMEOUT` |
| Code 03 | `OVERFLOW` | Code 07 | `A ≠ 0` | Code 11 | `INTERRUPTED` |
| Code 04 | `TOO BIG` | Code 08 | `ERROR 5` | Code 12 | `CANNOT BE < 0` |

---

### Code 01: `DIVIDE BY 0`
* **Mathematical Classification:** Essential singularity, pole of order 1, or undefined limit.
* **Triggering Conditions:**
  * Direct division: $y \div 0$
  * Multiplicative reciprocal: $1/0$
  * Logarithmic singularity: $\ln(0)$ or $\log_{10}(0)$ ($\lim_{x \to 0^+} \ln x = -\infty$)
  * Zero base with non-positive exponent: $0^y$ where $y \le 0$
  * Trigonometric poles: $\tan(90^\circ)$, $\tan(270^\circ)$, $\cot(0^\circ)$, $\sec(90^\circ)$, $\csc(0^\circ)$
* **IEEE-754 Representation:** Hardware trap prevents creation of unsigned or signed IEEE-754 $\pm\infty$ or NaN in user registers.
* **Stack State upon Error:**
  * Register $X$: `0.0000` (the invalid divisor or argument)
  * Register $Y$: Original numerator (e.g., $145.80$)
  * Registers $Z, T$: Undisturbed
  * `LASTX`: Unaltered (preserves the $X$ value from the prior successful calculation)
* **Keystroke Recovery Procedure:**
  1. Press `{{key:C}}` to dismiss the `DIVIDE BY 0` banner.
  2. The display reveals `0.0000` in $X$ and your numerator in $Y$.
  3. Key the intended non-zero divisor (e.g., `{{key:1}} {{key:2}}`).
  4. Press `{{key:÷}}`. The calculation completes normally.

#### Worked Diagnostic Example: Division by Zero Recovery
Compute $\frac{450}{15}$, but mistakenly key $0$ as the divisor:

| Step | Keystroke | Display Output | Register X | Register Y | Register Z |
| :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | `{{key:4}} {{key:5}} {{key:0}} {{key:ENTER}}` | `450.0000` | `450.0000` | `450.0000` | `0.0000` |
| 2 | `{{key:0}} {{key:÷}}` | `DIVIDE BY 0` | `0.0000` | `450.0000` | `0.0000` |
| 3 | `{{key:C}}` | `0.0000` | `0.0000` | `450.0000` | `0.0000` |
| 4 | `{{key:1}} {{key:5}} {{key:÷}}` | `30.0000` | `30.0000` | `0.0000` | `0.0000` |

---

### Code 02: `INVALID DATA`
* **Mathematical Classification:** Function domain violation in the real field $\mathbb{R}$.
* **Triggering Conditions:**
  * Square root of negative number in real mode: $\sqrt{-x}$ where $x < 0$
  * Logarithm of negative number: $\ln(-x)$ or $\log_{10}(-x)$
  * Inverse trigonometric domain limits: $\arcsin(x)$ or $\arccos(x)$ where $|x| > 1.0$
  * Factorial of non-integer or negative integer: $(-n)!$ or non-positive integer gamma poles
  * Combinatorics boundaries: $nCr$ or $nPr$ where $r > n$, $n < 0$, or $r < 0$
  * Negative base with non-integer exponent: $(-2)^{0.5}$
* **Stack State upon Error:** All registers frozen. Offending argument rests in $X$.
* **Keystroke Recovery Procedure:**
  1. Press `{{key:C}}` to clear the message.
  2. If a complex result was desired, arm the complex prefix: press `{{key:CMPLX}}, then re-execute the function. For example, {{key:CMPLX}} {{key:√x}}` converts $\sqrt{-16}$ into $0 + 4i$.
  3. If the input was erroneous, press `{{key:+/-}}` to invert the sign or re-key the argument.

---

### Code 03: `OVERFLOW`
* **Mathematical Classification:** Magnitude exceeds IEEE-754 double-precision representation limits.
* **Triggering Conditions:**
  * Absolute value $|x| > 1.7976931348623157 \times 10^{308}$
  * Factorial $n!$ for $n > 170$
  * Exponential $e^x$ for $x > 709.782712893384$
  * Power $10^x$ for $x > 308.2547155599167$
* **Stack State upon Error:** All registers frozen. Operands preserved prior to exponential scaling.
* **Keystroke Recovery Procedure:**
  1. Press `{{key:C}}` to dismiss.
  2. Scale the calculation by factoring out exponential powers (e.g., convert units from meters to kilometers, or compute logarithms first: $\ln(a \times b) = \ln a + \ln b$).

---

### Code 04: `TOO BIG`
* **Mathematical Classification:** Integer boundary overflow in the 36-bit two's complement integer architecture.
* **Triggering Conditions:**
  * Entering or computing an integer value outside the range $[-2^{35}, 2^{35}-1]$:
    $$\text{Lower Limit: } -34,359,738,368 \quad (0\text{x}800000000)$$
    $$\text{Upper Limit: } +34,359,738,367 \quad (0\text{x}7FFFFFFFF)$$
  * Integer multiplications or power-of-two scaling that push values beyond the signed 36-bit range.
  * Attempting to switch base (`HEX`, `OCT`, `BIN`) with a floating-point number whose integer magnitude exceeds 36 bits.
* **Stack State upon Error:** Operands preserved in full floating-point representation.
* **Keystroke Recovery Procedure:**
  1. Press `{{key:C}}` to dismiss.
  2. Switch to standard decimal floating-point mode via `{{key:BASE}} {{key:DEC}}`.
  3. Apply modulo $2^{36}$ or scale values appropriately.

---

### Code 05: `STAT ERROR`
* **Mathematical Classification:** Statistical degrees-of-freedom singularity or vertical geometric degeneracy.
* **Triggering Conditions:**
  * Requesting sample means (`{{key:x̄,ȳ}} {{key:x̄}}`) when sample count $n = 0$.
  * Requesting sample standard deviations ($s_x, s_y$) or linear regression (`{{key:L.R.}}`) when $n < 2$ (degrees of freedom $\nu = n - 1 \le 0$).
  * Linear regression with zero variance in $x$ ($\sum x^2 - \frac{(\sum x)^2}{n} = 0$), corresponding to a perfectly vertical line where slope $m = \infty$.
  * Correlation coefficient $r$ with zero variance in $y$ or $x$.
* **Stack State upon Error:** Statistical accumulators intact. Stack preserved.
* **Keystroke Recovery Procedure:**
  1. Press `{{key:C}}` to dismiss.
  2. Accumulate additional distinct data points using `{{key:Σ+}}`.
  3. Inspect accumulators via `{{key:SUMS}}` to verify data entry integrity.

---

### Code 06: `NO ROOT FOUND`
* **Mathematical Classification:** Root-finder iteration exhaustion or failure to bracket zero-crossing.
* **Triggering Conditions:**
  * Richard Brent's hybrid root solver ({{key:SOLVE}}) executes 100 iterations without bracketing a sign change or satisfying convergence tolerance ($\epsilon = 10^{-12}$).
  * The target equation has no real roots (e.g., $x^2 + 4 = 0$ in real domain).
  * The initial guesses in $X$ and $Y$ bracket a local minimum above the $x$-axis or a local maximum below the $x$-axis without crossing zero.
* **Stack State upon Error:** Best candidate approximation returned in Register $X$. Stack preserved.
* **Keystroke Recovery Procedure:**
  1. Press `{{key:C}}` to clear.
  2. Press `{{key:x∥y}}` (`PLOT`) to visually graph the function on the LCD and inspect its zero-crossings.
  3. Supply two new initial guesses that clearly straddle opposite sides of the root ($f(a) \cdot f(b) < 0$).
  4. Press {{key:SOLVE}} again.

---

### Code 07: `A ≠ 0`
* **Mathematical Classification:** Cubic polynomial degeneracy.
* **Triggering Conditions:**
  * Characteristic cubic polynomial solver (`{{key:XEQ}}` $\to$ `POLY`) is executed (`EXEC`) without entering leading coefficient $A$, or with $A = 0$ ($0x^3 + Bx^2 + Cx + D = 0$).
* **Stack State upon Error:** Stored coefficients in registers $A, B, C, D$ remain intact.
* **Keystroke Recovery Procedure:**
  1. Press `{{key:C}}` to dismiss.
  2. If solving a cubic, enter the non-zero leading coefficient into `A` and press `EXEC` (omitted coefficients $B, C, D$ assume $0$ by default).
  3. If solving a quadratic equation $a x^2 + b x + c = 0$, enter $A=a, B=b, C=c$ and press `EXEC` (where $D$ automatically defaults to $0$). Roots are deposited in variables `3` and `5`.

---

### Code 08: `ERROR 5`
* **Mathematical Classification:** Non-convergent cash flow in Time Value of Money (TVM) compound interest iteration.
* **Triggering Conditions:**
  * Unsolvable TVM financial configuration where cash flows cannot be balanced by any real interest rate $I\% \ge -100\%$.
  * All cash flow variables ($PV, PMT, FV$) entered with the identical mathematical sign (e.g., all positive), violating the fundamental cash flow sign convention that inflows must balance outflows.
* **Stack State upon Error:** Financial registers $N, I\%YR, PV, PMT, FV$ remain frozen.
* **Keystroke Recovery Procedure:**
  1. Press `{{key:C}}` to dismiss.
  2. Verify the cash flow signs: money leaving your hands (investments, loan payments) must be keyed negative (`{{key:+/-}}`), while money received (loan proceeds, withdrawals) must be positive.
  3. Clear financial memory if starting a fresh problem via `{{key:CLEAR}} {{key:CLALL}}`.

---

### Code 09: `MEMORY FULL`
* **Mathematical Classification:** Hardware non-volatile memory or equation bank exhaustion.
* **Triggering Conditions:**
  * Attempting to store a 25th equation when the hardware limit of 24 equations is reached.
  * Equation step allocation exceeds available flash sector storage.
* **Stack State upon Error:** Existing equations and stack remain 100% intact.
* **Keystroke Recovery Procedure:**
  1. Press `{{key:C}}` to dismiss.
  2. Enter equation catalog, select obsolete or temporary equations, and delete them using `{{key:CLEAR}} {{key:CLEQN}}`.

---

### Code 10: `TIMEOUT`
* **Mathematical Classification:** Numerical algorithm cycle exhaustion.
* **Triggering Conditions:**
  * Romberg numerical quadrature (`{{key:XEQ}}` $\to$ `{{key:∫}}`) exceeds 100,000 sub-interval function evaluations without reaching Richardson extrapolation tolerance.
  * Occurs with functions possessing infinite derivatives, sharp step discontinuities, or high-frequency oscillations (e.g., $\sin(1/x)$ near $x = 0$).
* **Stack State upon Error:** Current best numerical approximation preserved in $X$.
* **Keystroke Recovery Procedure:**
  1. Press `{{key:C}}` to dismiss.
  2. Narrow the integration interval $[a, b]$ to isolate smooth regions, or decompose the integral into piecewise segments around the singularity.

---

### Code 11: `INTERRUPTED`
* **Mathematical Classification:** Asynchronous user abort.
* **Triggering Conditions:**
  * The user presses `{{key:C}}` during a running Romberg integration, Brent's root search, cubic solve, or graphic plot render.
* **Stack State upon Error:** Completely clean operational state. Intermediate solver values cleared; user registers frozen at pre-execution state.
* **Keystroke Recovery Procedure:**
  1. Press `{{key:C}}` to return directly to interactive RPN calculation.

---

### Code 12: `CANNOT BE < 0`
* **Mathematical Classification:** Unsigned integer underflow in educational / elementary mode.
* **Triggering Conditions:**
  * Subtracting a larger unsigned whole number from a smaller unsigned whole number ($Y < X$ on `{{key:-}}`) while operating in constrained elementary educational profile.
* **Stack State upon Error:** Operands $X$ and $Y$ preserved.
* **Keystroke Recovery Procedure:**
  1. Press `{{key:C}}` to dismiss.
  2. Press `{{key:x⇄y}}` to exchange operands, or switch to standard signed scientific mode.

---

## Hardware Reset, Diagnostics & Recovery Protocols

For standardized collegiate exams (such as AP, SAT, or FE exams), laboratory baseline resets, or severe power anomalies, the SC-32 provides hardware-level diagnostic and memory wipe sequences:

<div class="admonition note">
<p class="admonition-title">SC-32 Hardware Recovery Protocols</p>
<ol>
  <li><strong>Soft Reset (Status Clear):</strong> Press <code>{{key:C}}</code> twice. Cancels active prompts, dismisses error banners, and clears pending shift flags without erasing variables or the stack.</li>
  <li><strong>Memory Initialization (Factory Baseline Reset):</strong> Hold <code>{{key:C}}</code> while powering on, or press <code>{{key:CLEAR}} {{key:CLALL}}</code>. Erases all variables A-Z, statistical accumulators, TVM registers, and stack. Resets angular mode to DEGREES, display format to ALL.</li>
  <li><strong>Dual-Slot NVM Ping-Pong Recovery:</strong> On boot, the microcontroller validates both non-volatile memory slots via 32-bit FNV-1a checksums. If the active slot fails due to battery removal during a write cycle, the firmware automatically rolls back to the standby slot, preventing data corruption.</li>
</ol>
</div>

---

## Verification & Implementation Parity

All 12 hardware error traps, non-destructive register preservation guarantees, and dual-slot FNV-1a non-volatile memory rollback protocols are continuously verified across the SC-32 hardware and firmware verification suites.
