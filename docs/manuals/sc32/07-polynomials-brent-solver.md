---
title: "Chapter 7: Polynomials, Brent-Dekker Solver & Root Finding | SC-32 Manual"
description: "Master Cardano's analytic cubic solver [POLY], Richard Brent's hybrid numerical root solver [SOLVE] with 10^-12 precision, Horner's method, and engineering equation solving on the StackCalc SC-32."
---

# Chapter 7: Polynomials, Brent-Dekker Solver & Root Finding

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 NUMERICAL SOLVERS // POLYNOMIALS &amp; BRENT'S ROOT FINDER</span>
  <span class="te-viewport-status text-sky-400">● CARDANO ANALYTIC CUBIC SOLVER &bull; BRENT-DEKKER HYBRID ALGORITHM &bull; 10⁻¹² CONVERGENCE PRECISION</span>
</div>

## The Application: When Nature Refuses to Factor & Richard Brent's Algorithmic Paranoia

In freshman algebra, textbooks present a comforting illusion: every polynomial factors neatly into integers, and every quadratic yields to the high school quadratic formula:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Students leave school believing that solving equations is simply a matter of finding the right algebraic formula.

Then you enter the physical world of mechanical, chemical, and aerospace engineering. **Real physical equations almost NEVER factor!**

### The Industrial Pipeline Nightmare: The Colebrook-White Dilemma

Consider water surging through a municipal aqueduct or cryogenic kerosene rushing into a rocket turbopump. The friction factor $f$ across the turbulent pipe wall is governed by the landmark Colebrook-White equation (1939):

$$\frac{1}{\sqrt{f}} = -2.0 \log_{10} \left( \frac{\varepsilon}{3.7 D} + \frac{2.51}{\operatorname{Re} \sqrt{f}} \right)$$

Inspect this equation with an analytical eye: the unknown Darcy friction factor $f$ appears on *both* sides of the equals sign—trapped inside an inverse square root on the left, and buried inside both a base-10 logarithm and a square root denominator on the right.

It is mathematically impossible to isolate $f$ using elementary symbolic algebra. There is no closed-form formula. The same mathematical barrier governs Johannes Kepler's equation for planetary orbital mechanics:

$$M = E - e \sin E$$

You cannot isolate the eccentric anomaly $E$ with pencil and paper. To design a municipal water main that withstands water hammer transients, or to steer an interplanetary spacecraft through a gravitational assist, the engineer must solve transcendental equations numerically.

#### The Fatal Flaw of Naive Root Finding
Early computational engineers turned to the classic Newton-Raphson iteration:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Newton-Raphson is quadratic and fast—until the function encounters a local extremum, an inflection point, or an asymptotic plateau where the derivative $f'(x) \approx 0$. When the denominator vanishes, the tangent line becomes nearly horizontal, catapulting the next estimate into numerical oblivion. In an embedded autopilot or real-time chemical process controller, a divergent Newton solver can trigger catastrophic system instability.

#### Richard Brent (1973): The Art of Algorithmic Paranoia
In 1973, Australian mathematician Richard P. Brent published a hybrid root-finding algorithm {{cite:brent1973}} that became the gold standard of scientific computing:
1. **Guaranteed Bracketing:** The solver brackets the root between two endpoints $[a, b]$ where $f(a)$ and $f(b)$ have opposite signs ($f(a) \cdot f(b) < 0$). By the Intermediate Value Theorem, a continuous root is guaranteed to exist within the bracket.
2. **Superlinear Sprint:** Whenever three distinct points are available, Brent's method accelerates using **Inverse Quadratic Interpolation (IQI)**, fitting a sideways parabola $x = P(y)$ through $(f(a), a), (f(b), b),$ and $(f(c), c)$ to leap directly toward $y = 0$.
3. **Algorithmic Paranoia:** Brent implemented unyielding watchdog criteria. If the IQI parabolic leap projects outside the active bracket $[a, b]$, or if it fails to contract the bracket interval by at least $50\%$ every two iterations, the algorithm instantly aborts interpolation and executes a robust **bisection step**.

Brent's method converges to 12 decimal places in under 10 iterations without ever requiring an analytical derivative and without ever diverging. On the StackCalc SC-32, the {{key:SOLVE}} engine embeds Richard Brent's proven numerical architecture into the palm of your hand.

<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>{{key:ALL}}</code> (Full 15-digit internal IEEE-754 mantissa; Standard Base-10 Arithmetic; Radians angular mode for transcendental root solving <code>{{key:RAD}}</code>; Degrees default for geometric polynomials). All stack operations assume the default 4-stack XYZT architecture.
</div>

---

{{res:sc32_cubic_roots:screenshot|Cubic polynomial x^3 - 6x^2 + 11x - 6 = 0 solved via POLY}}

## The CRA Pedagogical Progression for Equation Solving

Root finding is the mathematical art of determining the input values $x^*$ that satisfy the equilibrium equation $f(x^*) = 0$. On the StackCalc SC-32, root finding progresses systematically through the **Concrete-Representational-Abstract (CRA)** pedagogical sequence:

| Pedagogical Tier | Physical & Cognitive Domain | Implementation on the SC-32 RPN Architecture |
| :--- | :--- | :--- |
| **1. Concrete Level**<br>*(Physical & Tactile Grounding)* | • Physical mechanical equilibrium: Neutral axis of a bent beam where tensile and compressive stresses balance to zero.<br>• Pipe friction head loss balancing gravitational elevation drop.<br>• Kepler orbital position where eccentric anomaly matches elapsed flight time.<br>• The sliding interval caliper: Visualizing root bracketing as closing a pair of mechanical sliding calipers around the zero-crossing interval $[a, b]$. | Tactile physical modeling on the Algebra Factoring Stage before executing numeric root solvers. |
| **2. Representation Level**<br>*(Stack Register Visualizations)* | • Transflective LCD Equation Editor token lists:<br>&nbsp;&nbsp;`"X"` `"3"` `"yˣ"` `"2"` `"X"` `"×"` `"-"` `"5"` `"-"` $\implies f(x) = x^3 - 2x - 5$<br>• 4-level stack state tables displaying bracket limits $(a, b)$ in $(Y, X)$, intermediate function evaluations $f(x)$, and superlinear secant updates. | Dynamic bracket contracting on the dot-matrix LCD. |
| **3. Abstract Level**<br>*(Analytical & Hybrid Theorems)* | • Gerolamo Cardano's closed-form cubic solution &amp; François Viète's *casus irreducibilis*.<br>• Richard Brent's hybrid algorithm: Combining guaranteed bisection bounds with the superlinear speed of secant and inverse quadratic interpolation (IQI).<br>• Asymptotic convergence rate: Golden ratio exponent $\phi \approx 1.618034$. | Certified 64-bit IEEE-754 root extraction via {{key:SOLVE}}. |

{{blocks:algebra_factoring_area|Algebra Factoring Stage Root Model}}
*Figure 7.1: The physical Algebra Factoring Stage area model provides geometric grounding for polynomial root extraction, showing the visual decomposition of roots prior to numerical bracketing.*

---

## Characteristic Polynomial Solver (`{{key:POLY}}`)

Root extraction of polynomial characteristic equations is fundamental to structural vibration analysis, aircraft flight control stability, circuit pole-zero placement, and chemical reaction equilibria.

The StackCalc SC-32 features an onboard **Characteristic Polynomial Solver (`{{key:POLY}}`)** mapped to Right Shift `{{key:↱}}` on the `{{key:XEQ}}` key (as specified in the *HP32SII Deviation Rubric*). The engine extracts all real and complex roots for general cubic and quadratic polynomials analytically:

$$A x^3 + B x^2 + C x + D = 0$$

| Interface Element | Display Legend / Key Assignment | Functional Action / Internal Allocation |
| :--- | :--- | :--- |
| **Menu Prompt** | `Ax^3 + Bx^2 + Cx + D = 0` | Prompts for polynomial coefficient entry |
| **LFU Softkeys** | `{{key:A}} {{key:B}} {{key:C}} {{key:D}} {{key:EXEC}} {{key:CLR}}` | Softkey assignments for coefficient entry and execution |
| **Internal Storage: Root 1** | Variables `"1"` (Real), `"2"` (Imaginary) | Stores first calculated root |
| **Internal Storage: Root 2** | Variables `"3"` (Real), `"4"` (Imaginary) | Stores second calculated root |
| **Internal Storage: Root 3** | Variables `"5"` (Real), `"6"` (Imaginary) | Stores third calculated root |
| **Active Stack Output** | Register $Y$: $\operatorname{Re}(\text{Root 1})$, Register $X$: $\operatorname{Im}(\text{Root 1})$ | Primary root delivered directly in $(Y, X)$ Gaussian format |

### Cardano's Analytical Cubic Engine
Unlike numerical approximation methods that can skip closely-spaced roots, oscillate near inflection points, or fail to converge, the `{{key:POLY}}` engine implements **Gerolamo Cardano's closed-form analytic solution**:

1. **Substitution to Depressed Cubic:** Substituting $x = y - \frac{B}{3A}$ eliminates the quadratic term, yielding:
   $$y^3 + 3P y + 2Q = 0$$
   where $P = \frac{3AC - B^2}{9A^2}$ and $Q = \frac{2B^3 - 9ABC + 27A^2D}{54A^3}$.
2. **The Polynomial Discriminant ($\Delta$):**
   $$\Delta = Q^2 + P^3$$
   * **Case 1 ($\Delta > 0$):** One real root and a pair of complex conjugate roots. Solved via Cardano's hyperbolic radicals:
     $$u = \sqrt[3]{-Q + \sqrt{\Delta}}, \quad v = \sqrt[3]{-Q - \sqrt{\Delta}}$$
     $$y_1 = u + v, \quad y_{2,3} = -\frac{u+v}{2} \pm i\frac{\sqrt{3}(u-v)}{2}$$
   * **Case 2 ($\Delta = 0$):** Three real roots, at least two of which are multiple roots.
   * **Case 3 ($\Delta < 0$, *Casus Irreducibilis*):** Three distinct real roots. Solved via François Viète's trigonometric substitution ($y = 2\sqrt{-P}\cos(\theta/3)$).

### Singularity Rule: $A \ne 0$ and Quadratic Embedding ($D = 0$ Default)
The leading cubic coefficient $A$ must be non-zero ($|A| > 10^{-12}$); pressing `{{key:EXEC}}` without entering $A$ (or with $A = 0$) triggers `A ≠ 0`. Importantly, the `{{key:POLY}}` engine **assumes $0$ by default** for any unentered coefficient ($B, C, D$). To solve a quadratic equation $a x^2 + b x + c = 0$ using `{{key:POLY}}`, simply enter `a {{key:A}} b {{key:B}} c {{key:C}}` and press `{{key:EXEC}}`—the engine automatically sets $D = 0$, forming the depressed cubic $a x^3 + b x^2 + c x + 0 = x(a x^2 + b x + c) = 0$ and extracting the trivial root $0$ alongside the two exact quadratic roots in Registers `3` (`{{key:RCL}} 3`) and `5` (`{{key:RCL}} 5`) without requiring you to manually key `0 {{key:D}}`:
$$a x^3 + b x^2 + c x + 0 = x(a x^2 + b x + c) = 0 \implies x = \frac{-b \pm \sqrt{b^2 - 4 a c}}{2 a}$$
Similarly, for a pure cubic such as $x^3 - 8 = 0$, you only need to key `1 {{key:A}} 8 {{key:+/-}} {{key:D}} {{key:EXEC}}`, as $B$ and $C$ default to zero automatically.

---

## Grounded Case 1: Cardano Cubic with Three Real Roots

Solve the cubic characteristic polynomial:
$$x^3 - 6x^2 + 11x - 6 = 0$$
Analytical factorization:
$$(x - 1)(x - 2)(x - 3) = 0 \implies x_1 = 1.0, \quad x_2 = 2.0, \quad x_3 = 3.0$$

### Keystroke Execution
Press `{{key:POLY}}` to open the polynomial workspace on the LFU softkeys:
1. `1` press `{{key:A}}` (Stores $A = 1.0$)
2. `6 {{key:+/-}}` press `{{key:B}}` (Stores $B = -6.0$)
3. `11` press `{{key:C}}` (Stores $C = 11.0$)
4. `6 {{key:+/-}}` press `{{key:D}}` (Stores $D = -6.0$)
5. Press `{{key:EXEC}}` (Evaluates Cardano closed-form roots)

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Coefficient $A = 1.0$ |
| 2 | `6 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-6.0000$ | Coefficient $B = -6.0$ |
| 3 | `11 {{key:C}}` | $0.0000$ | $1.0000$ | $-6.0000$ | $11.0000$ | Coefficient $C = 11.0$ |
| 4 | `6 {{key:+/-}} {{key:D}}` | $1.0000$ | $-6.0000$ | $11.0000$ | $-6.0000$ | Coefficient $D = -6.0$ |
| 5 | `{{key:EXEC}}` | $1.0000$ | $-6.0000$ | **$1.000000$** | **$0.000000$** | Primary root $r_1 = 1.0 + 0.0i$ in $(Y, X)$; roots $1, 2, 3$ stored in vars `1`–`6` |

| Storage Variable | Extracted Value | Polynomial Root Assignment |
| :---: | :---: | :--- |
| **`1` / `2`** | **`1.0000000000` / `0.0000000000`** | Root $r_1 = 1.0 + 0.0i$ (also placed in Registers $Y$ and $X$) |
| **`3` / `4`** | **`2.0000000000` / `0.0000000000`** | Root $r_2 = 2.0 + 0.0i$ |
| **`5` / `6`** | **`3.0000000000` / `0.0000000000`** | Root $r_3 = 3.0 + 0.0i$ |

### Recalling Stored Roots
The roots are placed directly into non-volatile variables `1` through `6`:
* Root 1: `{{key:RCL}} 1` $\rightarrow 1.0$, `{{key:RCL}} 2` $\rightarrow 0.0$ ($1.0 + 0.0i$)
* Root 2: `{{key:RCL}} 3` $\rightarrow 2.0$, `{{key:RCL}} 4` $\rightarrow 0.0$ ($2.0 + 0.0i$)
* Root 3: `{{key:RCL}} 5` $\rightarrow 3.0$, `{{key:RCL}} 6` $\rightarrow 0.0$ ($3.0 + 0.0i$)

---

## Grounded Case 2: Cubic with Complex Conjugate Roots

Solve the cubic equation:
$$x^3 - x^2 + x - 1 = 0 \implies (x - 1)(x^2 + 1) = 0$$
Roots:
$$x_1 = 1.0 + 0.0i, \quad x_2 = 0.0 + 1.0i, \quad x_3 = 0.0 - 1.0i$$

### Keystrokes
Press `{{key:POLY}}`:
1. `1 {{key:A}}`
2. `1 {{key:+/-}} {{key:B}}`
3. `1 {{key:C}}`
4. `1 {{key:+/-}} {{key:D}}`
5. `{{key:EXEC}}`

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Coefficient $A = 1.0$ |
| 2 | `1 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-1.0000$ | Coefficient $B = -1.0$ |
| 3 | `1 {{key:C}}` | $0.0000$ | $1.0000$ | $-1.0000$ | $1.0000$ | Coefficient $C = 1.0$ |
| 4 | `1 {{key:+/-}} {{key:D}}` | $1.0000$ | $-1.0000$ | $1.0000$ | $-1.0000$ | Coefficient $D = -1.0$ |
| 5 | `{{key:EXEC}}` | $1.0000$ | $-1.0000$ | **$1.000000$** | **$0.000000$** | Real $r_1=1$ in $Y$, Imag $r_1=0$ in $X$; conjugate pair $\pm i$ in vars `3`–`6` |

### Verified Output Registers
* Variable `1` (Root 1 Real): **$1.000000$**, Variable `2` (Root 1 Imag): **$0.000000$**
* Variable `3` (Root 2 Real): **$0.000000$**, Variable `4` (Root 2 Imag): **$+1.000000$**
* Variable `5` (Root 3 Real): **$0.000000$**, Variable `6` (Root 3 Imag): **$-1.000000$**

---

## Richard Brent's Numerical Root Finder ({{key:SOLVE}})

For general non-linear, transcendental, or piecewise equations where closed-form algebraic formulas do not exist, the SC-32 provides **Richard Brent's Numerical Root Finder (`{{key:SOLVE}}`)**.

<div class="admonition note">
<p class="admonition-title">Richard Brent's Hybrid Root Solver State Machine (1973)</p>
<ol>
  <li><strong>Initial Bracket Verification:</strong> Confirms sign change across endpoints: $f(a) \cdot f(b) \le 0$ (or conducts an outward geometric/secant search from a single initial guess until a sign change is bracketed).</li>
  <li><strong>Branch Decision:</strong> If three distinct evaluation points $(a, b, c)$ are available, formulate an <strong>Inverse Quadratic Interpolation (IQI)</strong> step. Otherwise, execute a <strong>Secant Method step</strong>.</li>
  <li><strong>Guardrail Test:</strong> Test whether the proposed interpolation step lands strictly within the three-quarter bracket window $((3a+b)/4, b)$ and halves the step size at least every two iterations.
    <ul>
      <li><em>Pass:</em> Accept interpolated estimate.</li>
      <li><em>Fail:</em> Instantly trigger fallback to <strong>Bisection step</strong> ($m = (a + b)/2$).</li>
    </ul>
  </li>
  <li><strong>Convergence Check:</strong> Terminate when bracket interval $|b - a| < 10^{-12}$ or $|f(b)| < 10^{-13}$.</li>
</ol>
</div>

{{blocks:algebra_boxes_hero|Algebra Boxes Studio Kit Hardware}}
*Figure 7.2: The physical Algebra Factoring Stage modular hardware kit, demonstrating precision boundary constraints and mechanical bracketing corresponding to the Brent-Dekker root finding engine.*

### The Three Convergence Mechanics of Brent's Algorithm
1. **Bisection Method:** The robust fallback. Cuts the bracket interval exactly in half: $m = (a + b) / 2$. Guaranteed to converge, but linear ($1\text{ bit of precision per step}$).
2. **Secant Method:** Linear interpolation through points $(a, f(a))$ and $(b, f(b))$. Superlinear convergence ($p = \phi \approx 1.618$).
3. **Inverse Quadratic Interpolation (IQI):** Fits a parabola $x = P(y)$ through three points $(f(a), a), (f(b), b), (f(c), c)$ and evaluates at $y = 0$:
   $$x = \frac{a f(b) f(c)}{(f(a)-f(b))(f(a)-f(c))} + \frac{b f(a) f(c)}{(f(b)-f(a))(f(b)-f(c))} + \frac{c f(a) f(b)}{(f(c)-f(a))(f(c)-f(b))}$$
   Order of convergence $p \approx 1.839$ (approaching quadratic speed without calculating derivatives!).

| Root Finding Algorithm | Asymptotic Order ($p$) | Derivative Required? | Convergence Guarantee | Vulnerability / Failure Risk |
| :--- | :---: | :---: | :---: | :--- |
| **Bisection** | $1.000$ | No | Guaranteed (bracketed) | Slow, linear progress ($1\text{ bit/iteration}$) |
| **Newton-Raphson** | $2.000$ | Yes ($f'(x)$) | Local only | Divergence near $f'(x) \approx 0$; inflection loops |
| **Secant Method** | $1.618$ | No | Local only | Undamped oscillations on non-convex curves |
| **Brent-Dekker** | $1.839$ | No | Guaranteed (bracketed) | **Zero failure** (automatic bisection fallback) |

### The Algebraic Trap vs. StackCalc Superpower Showdown

| Challenge / Metric | Algebraic Trap (TI-84 / Infix) | Algebraic Strokes | StackCalc SC-32 Superpower | SC-32 Strokes | Superpower Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **Transcendental Root Finding**: Colebrook-White friction factor | String entry in numeric solver: `solve(1/√(F) + 2*log(0.001/3.7 + 2.51/(100000*√(F))), F, 0.02)` (54 strokes). Missing or mismatched parenthesis throws syntax error; Newton tangent iteration prone to divergence near asymptotic plateaus. | 54 | **Brent's Hybrid Root Finder (`{{key:SOLVE}}`)**: Define postfix equation in `{{key:EQN}}`, load initial estimate `0.02 {{key:STO}} F`, press `{{key:SOLVE}} F` (24 strokes). Guarded Inverse Quadratic Interpolation contracts interval to $10^{-12}$ in $\le 8$ iterations with guaranteed convergence! | 24 | **56% fewer strokes + guaranteed bisection fallback** |
| **Cubic Characteristic Roots**: $x^3 - 6x^2 + 11x - 6 = 0$ | High-degree numerical approximation or graph tracing; requires setting window, guessing each root separately, and rerunning solver 3 times (48 strokes). Complex conjugate roots invisible. | 48 | **Cardano Analytic Solver (`{{key:POLY}}`)**: Enter coefficients into softkeys `1 {{key:A}} 6 {{key:+/-}} {{key:B}} 11 {{key:C}} 6 {{key:+/-}} {{key:D}}`, press `{{key:EXEC}}` (16 strokes). Closed-form Cardano resolvent delivers all three real/complex roots to $(Y, X)$ and variables 1–6 in $<5\text{ ms}$! | 16 | **67% fewer strokes + all real & complex roots simultaneously** |

---

## Grounded Case 3: Brent's Solver on Wallis's Benchmark Cubic: $x^3 - 2x - 5 = 0$

Solve John Wallis's historic 1685 root-finding benchmark equation (originally used by Isaac Newton and Joseph Raphson to test iterative convergence):
$$f(x) = x^3 - 2x - 5 = 0$$
Initial guess: $x = 2.0$ (where $f(2) = 8 - 4 - 5 = -1.0$).
Known real root: $x^* \approx 2.0945514815423$.

### Keystroke Execution
1. Program equation into `{{key:EQN}}`:
   `X {{key:3}} {{key:yˣ}} 2 {{key:ENTER}} X {{key:×}} {{key:-}} 5 {{key:-}}`
2. Provide initial estimate:
   `2 {{key:STO}} X`
3. Execute Brent's solver:
   `{{key:SOLVE}} X`

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `2 {{key:STO}} X` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Initial guess loaded |
| 2 | `{{key:SOLVE}} X` | $0.0000$ | $0.0000$ | $2.0000$ | **$2.0945514815$** | Initial guess lifts to $Y$; root extracted in $X$ |

The display outputs the root **$x = 2.0945514815$**.

---

## Horner's Method for Polynomial Stack Evaluation

Evaluating a high-degree polynomial in standard algebraic form requires calculating redundant powers $x^2, x^3, \dots, x^n$. **Horner's Method** factors the polynomial into nested linear binomials:

$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0 = (\dots((a_n x + a_{n-1}) x + a_{n-2}) x + \dots + a_1) x + a_0$$

### RPN Stack Elegance of Horner's Method
On the SC-32, Horner's method executes with **zero memory storage registers** and **zero parentheses**. At each stage, keying the multiplier $x = 2.5$ automatically lifts the running polynomial accumulator from Register $X$ into Register $Y$, allowing each nested multiplication and addition to cascade cleanly through the stack.

Evaluate $P(x) = 4x^4 - 3x^3 + 2x^2 - 5x + 7$ at $x = 2.5$:
Nested form: $P(2.5) = (((4(2.5) - 3)(2.5) + 2)(2.5) - 5)(2.5) + 7$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_01:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_01:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `2.5 {{key:ENTER}} 4 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | First term: $a_4 x = 4(2.5) = 10.0$ |
| 2 | `3 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $7.0000$ | Add next coefficient: $10.0 - 3 = 7.0$ |
| 3 | `2.5 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $17.5000$ | Digit entry lifts $7.0$ to $Y$; multiply: $(7.0)(2.5) = 17.5$ |
| 4 | `2 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $19.5000$ | Add next coefficient: $17.5 + 2 = 19.5$ |
| 5 | `2.5 {{key:×}} 5 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $43.7500$ | Lift & multiply: $(19.5)(2.5) - 5 = 43.75$ |
| 6 | `2.5 {{key:×}} 7 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$116.3750$** | Final evaluation: $(43.75)(2.5) + 7 = \mathbf{116.3750}$ |

> [!TIP]
> **HP Purist Tip: The T-Register Replication Stream & Addressable Storage Variant:**
> When evaluating a polynomial at an argument $x$ with many digits (e.g., $x = 2.71828$), classic 4-register RPN masters flood the stack first via `2.71828 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}`. Because Register $T$ replicates downward on every dyadic drop, you stream `4 {{key:×}} 3 {{key:-}} {{key:×}} 2 {{key:+}} {{key:×}} 5 {{key:-}} {{key:×}} 7 {{key:+}}` without ever re-keying $x$ or touching a storage register! Alternatively, store $x$ once via `2.71828 {{key:STO}} A` and evaluate with `4 {{key:RCL}} A {{key:×}} 3 {{key:-}} {{key:RCL}} A {{key:×}} 2 {{key:+}} ...` (no `{{key:ENTER}}` needed before `{{key:RCL}}`).

Total operations: 4 multiplications and 4 additions. Zero powers!

---

## Root-Finding Architecture & Numerical Convergence Notes

### Hybrid Convergence: Brent-Dekker vs. Newton-Raphson
In numerical analysis, classical Newton-Raphson iteration is susceptible to divergence or cyclical oscillation when initial estimates encounter inflection points ($f''(x) = 0$) or vanishing derivatives ($f'(x) \approx 0$). The SC-32 implements the hybrid Brent-Dekker algorithm {{cite:brent1973}}, which guarantees convergence for any continuous function where the root is bracketed. The algorithm opportunistically accelerates convergence using superlinear inverse quadratic interpolation and secant projections, but deterministically reverts to robust interval bisection whenever an interpolated step falls outside the bracket boundaries or fails to reduce the interval by half.

### Cardano Analytical Solvers & Closed-Form Cubics
In addition to general numerical root-finding, the SC-32 incorporates a hardware-accelerated closed-form polynomial solver accessed via `{{key:POLY}}`. Rather than relying on iterative approximations that can stall in local minima, the firmware evaluates cubic and quadratic polynomials through analytical Cardano-Ferrari resolvents. This delivers exact real roots and complex conjugate pairs directly into memory registers in under 5 milliseconds.

### Implicit Nonlinear Formulations & Physical Equilibrium
Real-world engineering systems frequently produce transcendental relations that defy closed-form symbolic inversion—such as Colebrook-White turbulent conduit friction factors, Kepler's transcendental anomaly equation, and Redlich-Kwong real-gas isotherms. The SC-32's `{{key:EQN}}` engine enables engineers to key implicit governing equations directly in standard RPN syntax. Supplying two bounding estimates and invoking `{{key:SOLVE}}` establishes physical equilibrium to 12 significant decimal places without manual algebraic transformations.

### Numerical Precision & Stack State Preservation
The solver state machine operates directly on 64-bit IEEE-754 double-precision representations with an absolute convergence tolerance of $10^{-12}$. Stack state preservation during iterative equation evaluation ensures that initial boundary estimates in Registers $Y$ and $X$ remain accessible, while `{{key:LASTX}}` preserves the pre-operation operand for immediate diagnostic verification.

---

## Diagnostic Checkpoints & Singularity Handling

> [!CHECKPOINT]
> **Diagnostic Checkpoint 7.1: Root Bracketing Sign Condition**  
> For {{key:SOLVE}} to guarantee convergence, initial guesses in $Y$ and $X$ should bracket the root: $f(Y) \cdot f(X) \le 0$. If both guesses produce the same sign, the solver attempts an outward geometric search. If no sign change is found, execution halts with `Error: NO ROOT FOUND`.

> [!CHECKPOINT]
> **Diagnostic Checkpoint 7.2: Polynomial Solver Leading Coefficient $A \ne 0$ & Default 0 Coefficients**  
> When using `{{key:POLY}}`, coefficient $A$ must be non-zero ($A = 0$ or omitting $A$ triggers `A ≠ 0`). Because unentered coefficients assume $0$ by default, solving a quadratic equation $ax^2 + bx + c = 0$ requires keying only $A=a, B=b, C=c$ before pressing `{{key:EXEC}}`; $D$ automatically defaults to $0$, and the two quadratic roots are stored in variables `3` and `5`. Similarly, cubics with zero coefficients (like $x^3 - 8 = 0$) require only entering $A$ and $D$.

> [!CHECKPOINT]
> **Diagnostic Checkpoint 7.3: Multiple / Tangent Roots ($f'(x^*) = 0$)**  
> For tangent roots (e.g. $f(x) = (x - 2)^2 = 0$), $f(x) \ge 0$ everywhere, so no bracket sign change exists. Brent's solver detects the local minimum where $|f(x)| < 10^{-12}$ and returns $x = 2.0$.

## Engineering Design Briefing: Turbulent Municipal Aqueducts & Transonic Aerodynamics (Problems 7.1 through 7.40)

> **Hands-On Studio Proof: Algebra Factoring Tiles &rarr; Calculator**  
> Before running numerical root solvers and Cardano cubic extractions on the SC-32, manipulate physical factoring tiles on the Algebra Factoring Stage (`docs/assets/manuals/algebra_factoring_area.png`) and explore bounded physical intervals with the modular Algebra Boxes kit (`docs/assets/renders/algebra-boxes-hero.png`). Physically establishing signs and geometric root brackets grounds the Brent-Dekker state machine before solving implicit turbulent flow and orbital mechanics equations.

The following 40 professional engineering case studies span turbulent pipeline friction, Keplerian celestial mechanics, real-gas equation of state isotherms, and structural flutter stability.

> **Thematic Arc I — Implicit Transport Equations & Transcendental Root-Finding (Problems 7.1–7.10):** We open with classic implicit engineering correlations—Colebrook-White friction, Kepler anomalies, and transcendental eigenvalues—solved via `SOLVE`.

### Problem 7.1: Colebrook-White Turbulent Pipe Friction Factor
Fluid flows through a rough commercial steel pipe: Reynolds number $\text{Re} = 100,000$, relative roughness $\varepsilon/D = 0.001$. Solve the implicit Colebrook-White equation for Darcy friction factor $f$:
$$\frac{1}{\sqrt{f}} = -2.0 \log_{10}\left(\frac{\varepsilon/D}{3.7} + \frac{2.51}{\text{Re}\sqrt{f}}\right) \implies f(F) = \frac{1}{\sqrt{F}} + 2.0 \log_{10}\left(\frac{0.001}{3.7} + \frac{2.51}{100000\sqrt{F}}\right) = 0$$

Program equation into `{{key:EQN}}` under label `COLE`:
`F {{key:√x}} {{key:1/x}}  0.001 {{key:ENTER}} 3.7 {{key:÷}}  2.51 {{key:ENTER}} 100000 {{key:÷}} F {{key:√x}} {{key:÷}} {{key:+}} {{key:LOG}} 2 {{key:×}} {{key:+}}`

Initial guess: $F = 0.02$. Solve via `{{key:SOLVE}} F`:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0.02 {{key:STO}} F` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0200$ | Initial guess loaded |
| 2 | `{{key:SOLVE}} F` | $0.0000$ | $0.0000$ | $0.0200$ | **$0.022204$** | Darcy friction factor $f$ |

The stack resolves to **$f = 0.022204$** ($2.22 \times 10^{-2}$).

---

### Problem 7.2: Kepler's Equation for Planetary Orbital Anomaly
An Earth observation satellite has orbital eccentricity $e = 0.25$ and mean anomaly $M = 1.20\text{ rad}$. Solve Kepler's equation for eccentric anomaly $E$:
$$f(E) = E - e \sin E - M = E - 0.25 \sin E - 1.20 = 0$$
Set baseline to `{{key:RAD}}`. Program equation: `E  0.25 {{key:ENTER}} E {{key:SIN}} {{key:×}} {{key:-}} 1.20 {{key:-}}`.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1.20 {{key:STO}} E` | $0.0000$ | $0.0000$ | $0.0000$ | $1.2000$ | Initial estimate $E_0 = M$ |
| 2 | `{{key:SOLVE}} E` | $0.0000$ | $0.0000$ | $1.2000$ | **$1.488665$** | Eccentric anomaly $E$ in radians |

Register $X$ settles at **$E = 1.488665\text{ radians}$** ($85.294^\circ$).

---

### Problem 7.3: Van der Waals Real Gas Molar Volume
Carbon dioxide gas ($a = 3.59\text{ L}^2\cdot\text{atm/mol}^2, b = 0.0427\text{ L/mol}$) at temperature $T = 300\text{ K}$ and pressure $P = 50.0\text{ atm}$ ($R = 0.08206\text{ L}\cdot\text{atm/(mol}\cdot\text{K)}$):
$$\left(P + \frac{a}{V^2}\right)(V - b) = R T \implies P V^3 - (P b + R T) V^2 + a V - a b = 0$$
* $A = 50.0$
* $B = -(50 \times 0.0427 + 0.08206 \times 300) = -(2.135 + 24.618) = -26.753$
* $C = 3.59$
* $D = -(3.59 \times 0.0427) = -0.153293$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_09:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_09:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `50 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $50.0000$ | Coefficient $A = 50.0$ |
| 2 | `26.753 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $50.0000$ | $-26.7530$ | Coefficient $B = -26.753$ |
| 3 | `3.59 {{key:C}}` | $0.0000$ | $50.0000$ | $-26.7530$ | $3.5900$ | Coefficient $C = 3.59$ |
| 4 | `0.153293 {{key:+/-}} {{key:D}}`| $50.0000$ | $-26.7530$ | $3.5900$ | $-0.153293$| Coefficient $D = -0.153293$ |
| 5 | `{{key:EXEC}}` | $50.0000$ | $-26.7530$ | **$0.358736$** | **$0.000000$** | Real root in $Y$, Imag in $X$ |
| 6 | `{{key:x⇄y}}` | $50.0000$ | $-26.7530$ | $0.000000$ | **$0.358736$** | Molar volume $V_m$ in Register $X$ |

This confirms a final value of **$V_m = 0.358736\text{ L/mol}$**.

---

### Problem 7.4: Transistor Shockley Diode Operating Point
Diode in series with $R = 1,000\,\Omega$ and source $V_s = 5.0\text{ V}$. Diode saturation current $I_s = 10^{-12}\text{ A}$, thermal voltage $V_T = 0.02585\text{ V}$:
$$f(V) = 5.0 - 1000 \times 10^{-12} (e^{V / 0.02585} - 1) - V = 0$$

Program equation into `{{key:EQN}}` under label `DIODE`.
Initial guess: $0.65\text{ V}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0.65 {{key:STO}} V` | $0.0000$ | $0.0000$ | $0.0000$ | $0.6500$ | Initial estimate loaded |
| 2 | `{{key:SOLVE}} V` | $0.0000$ | $0.0000$ | $0.6500$ | **$0.672944$** | Diode forward voltage $V_D$ |

The calculation yields **$V_D = 0.672944\text{ Volts}$** ($I = 4.327\text{ mA}$).

---

### Problem 7.5: Open Channel Critical Depth (Manning's Equation)
Trapezoidal channel ($b = 3.0\text{ m}, z = 2.0$) carrying discharge $Q = 20.0\text{ m}^3/\text{s}$. Critical flow occurs when:
$$\frac{Q^2 T}{g A^3} = 1 \implies 400(3 + 4 y) - 9.81 (3y + 2y^2)^3 = 0$$

Program into `{{key:EQN}}`. Initial guess: $y = 1.0\text{ m}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1.0 {{key:STO}} Y` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Initial depth estimate |
| 2 | `{{key:SOLVE}} Y` | $0.0000$ | $0.0000$ | $1.0000$ | **$1.258641$** | Critical flow depth $y_c$ |

The stack resolves to **$y_c = 1.258641\text{ meters}$**.

---

### Problem 7.6: Structural Column Buckling Transcendental Mode
Clamped-pinned elastic column eigenvalue equation:
$$\tan(x) - x = 0 \quad (\text{with } x = k L)$$

Set baseline mode to `{{key:RAD}}` and program the characteristic equation into `{{key:EQN}}` under label `BUCK`: `X {{key:TAN}} X {{key:-}}`.

Keying `4.5 {{key:STO}} X` loads initial trial eigenvalue estimate $x_0 = 4.5000\text{ rad}$ into variable $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 4.5000)$. Striking `{{key:SOLVE}} X` executes Brent's hybrid root solver, evaluating $\tan(x) - x$ and rapidly contracting the interval via inverse quadratic interpolation to isolate the first non-trivial buckling root $(T: 0.0000, Z: 0.0000, Y: 4.5000, X: \mathbf{4.493409})$ in Register $X$ ($\approx 1.4303\pi$).

---

### Problem 7.7: Blackbody Planck Peak Wavelength (Wien's Law Derivation)
Maximizing Planck spectral radiance requires solving the transcendental root:
$$5(1 - e^{-x}) - x = 0 \quad (\text{where } x = h c / (\lambda k_B T))$$

Program equation into `{{key:EQN}}` under label `WIEN`: `1 X {{key:+/-}} {{key:eˣ}} {{key:-}} 5 {{key:×}} X {{key:-}}`.

Entering `5.0 {{key:STO}} X` stores initial estimate $x_0 = 5.0$ into variable $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 5.0000)$. Striking `{{key:SOLVE}} X` executes Brent's solver; within 6 iterations of guarded inverse quadratic interpolation, the root converges to $10^{-12}$ precision $(T: 0.0000, Z: 0.0000, Y: 5.0000, X: \mathbf{4.965114})$ in Register $X$.

---

### Problem 7.8: RLC Circuit Natural Resonant Poles (Cubic State Characteristic)
3rd-order system characteristic equation:
$$s^3 + 12 s^2 + 45 s + 50 = 0$$

Analytical factorization yields $(s + 2)(s + 5)^2 = 0$, giving an isolated real pole at $s = -2$ and a critically damped double pole at $s = -5$.

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_10:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_10:value}}`**

In `{{key:POLY}}`, entering `1 {{key:A}} 12 {{key:B}}` loads leading cubic and quadratic coefficients $(T: 0.0000, Z: 0.0000, Y: 1.0000, X: 12.0000)$. Entering `45 {{key:C}} 50 {{key:D}}` loads linear and constant coefficients into parameter memory $(T: 1.0000, Z: 12.0000, Y: 45.0000, X: 50.0000)$. Striking `{{key:EXEC}}` evaluates Cardano closed-form roots, placing the first sorted real root in $(Y, X)$ $(T: 1.0000, Z: 12.0000, Y: \mathbf{-5.000000}, X: \mathbf{0.000000})$ and storing all three real poles ($s_1 = -5.0, s_2 = -5.0, s_3 = -2.0$) in variables `1`, `3`, and `5`.

---

### Problem 7.9: Projectile Launch Angle for Specified Impact Target
Target at distance $x = 1,200\text{ m}$, elevation $y = 150\text{ m}$, muzzle velocity $v_0 = 140\text{ m/s}$. Find launch angle $\theta$:
$$y = x \tan\theta - \frac{g x^2}{2 v_0^2} (1 + \tan^2\theta) \implies 360.3673 u^2 - 1200 u + 510.3673 = 0 \quad (\text{where } u = \tan\theta)$$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_02:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_02:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `360.3673 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $360.3673$ | Quadratic coefficient $A$ |
| 2 | `1200 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $360.3673$ | $-1200.0000$ | Quadratic coefficient $B$ |
| 3 | `510.3673 {{key:C}}` | $0.0000$ | $360.3673$ | $-1200.0000$ | $510.3673$ | Quadratic coefficient $C$ |
| 4 | `0 {{key:D}}` | $360.3673$ | $-1200.0000$ | $510.3673$ | $0.0000$ | Depressed constant (optional; $D$ defaults to $0.0$ if omitted) |
| 5 | `{{key:EXEC}}` | $360.3673$ | $-1200.0000$ | $0.0000$ | $0.0000$ | Roots stored in Regs 1, 3, 5 ($0, u_1, u_2$) |
| 6 | `{{key:RCL}} 3 {{key:ATAN}}` | $-1200.0000$ | $0.0000$ | $0.0000$ | **$26.590116$** | Low trajectory $\theta_1$ in degrees |
| 7 | `{{key:RCL}} 5 {{key:ATAN}}` | $0.0000$ | $0.0000$ | $26.590116$ | **$70.532306$** | High mortar arc $\theta_2$ in degrees |

*(Zero-Default Shortcut)*: Because unentered coefficients in `{{key:POLY}}` default to $0.0$, Step 4 can be skipped entirely—keying `360.3673 {{key:A}} 1200 {{key:+/-}} {{key:B}} 510.3673 {{key:C}} {{key:EXEC}}` directly solves the quadratic, confirming **$\theta_1 = 26.59^\circ$**, **$\theta_2 = 70.53^\circ$**.

---

### Problem 7.10: Adiabatic Flame Temperature Equilibrium
Energy balance equation for methane combustion:
$$H_{\text{prod}}(T) - H_{\text{react}} = 0 \implies 0.05 T^2 + 120 T - 280,000 = 0$$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_11:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_11:value}}`**

In `{{key:POLY}}`, keying `0.05 {{key:A}} 120 {{key:B}}` registers enthalpy temperature coefficients $A$ and $B$ $(T: 0.0000, Z: 0.0000, Y: 0.0500, X: 120.0000)$. Entering `280000 {{key:+/-}} {{key:C}} 0 {{key:D}}` loads enthalpy release $C = -280,000$ and depressed constant $D = 0.0$ $(T: 0.0500, Z: 120.0000, Y: -280000.0000, X: 0.0000)$. Pressing `{{key:EXEC}}` computes Cardano roots; keying `{{key:RCL}} 5` extracts the physical positive adiabatic flame temperature $(T: 120.0000, Z: -3853.3000, Y: 0.0000, X: \mathbf{1453.299832}\text{ K})$ in Register $X$ (with unphysical negative rebound root $-3,853.30\text{ K}$ stored in variable 1), confirming **$T_{\text{flame}} = 1,453.30\text{ Kelvin}$**.

---

> **Thematic Arc II — Characteristic Polynomials, Principal Stresses & Stability Poles (Problems 7.11–7.20):** Switching to the closed-form quadratic and cubic polynomial engine (`POLY`), we extract principal stresses and control-system poles.

### Problem 7.11: Eigenvalues of $3 \times 3$ Symmetric Stress Tensor
Stress tensor with components $\sigma_{xx} = 40, \sigma_{yy} = 20, \sigma_{zz} = 10, \tau_{xy} = 15, \tau_{yz} = 0, \tau_{xz} = 0$:
$$\det(\boldsymbol{\sigma} - \lambda \mathbf{I}) = (10 - \lambda)[(40 - \lambda)(20 - \lambda) - 225] = 0 \implies \lambda^3 - 70 \lambda^2 + 1175 \lambda - 5750 = 0$$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_12:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_12:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1 {{key:A}} 70 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-70.0000$ | Coefficients $A, B$ |
| 2 | `1175 {{key:C}} 5750 {{key:+/-}} {{key:D}}` | $1.0000$ | $-70.0000$ | $1175.0000$ | $-5750.0000$| Coefficients $C, D$ |
| 3 | `{{key:EXEC}}` | $1.0000$ | $-70.0000$ | **$10.000000$** | **$0.000000$** | Minor stress $\sigma_3 = 10.0$ in $Y$; $\sigma_2, \sigma_1$ in vars `3`, `5` |
| 4 | `{{key:RCL}} 5` | $-70.0000$ | $10.0000$ | $0.0000$ | **$48.027756$** | Recall major principal stress $\sigma_1$ into Register $X$ |

This confirms a final value of **$\sigma_1 = 48.03\text{ MPa}$**, **$\sigma_2 = 11.97\text{ MPa}$**, **$\sigma_3 = 10.00\text{ MPa}$**.

---

### Problem 7.12: Submerged Buoyant Float Equilibrium Immersion Depth
Solid wooden sphere of radius $R = 0.50\text{ m}$ and density $\rho_s = 650\text{ kg/m}^3$ floating in water ($\rho_w = 1000\text{ kg/m}^3$). Archimedes principle:
$$h^3 - 3R h^2 + 4 \frac{\rho_s}{\rho_w} R^3 = 0 \implies h^3 - 1.5 h^2 + 0.325 = 0$$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_13:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_13:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1 {{key:A}} 1.5 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-1.5000$ | Coefficients $A, B$ |
| 2 | `0 {{key:C}} 0.325 {{key:D}}` | $1.0000$ | $-1.5000$ | $0.0000$ | $0.3250$ | Coefficients $C, D$ (or omit $C$; omitted terms default to $0$) |
| 3 | `{{key:EXEC}}` | $1.0000$ | $-1.5000$ | $-0.412257$ | $0.0000$ | Roots stored in Regs 1, 3, 5 |
| 4 | `{{key:RCL}} 3` | $-1.5000$ | $-0.412257$ | $0.0000$ | **$0.601390$** | Physical immersion depth in $[0, 2R]$ |

The calculation yields **$h = 0.601390\text{ meters}$**.

---

### Problem 7.13: Bungee Jumper Maximum Cord Stretch
Jumper mass $m = 75\text{ kg}$, unstretched cord length $L = 30\text{ m}$, stiffness $k = 40\text{ N/m}$. Gravitational potential equals elastic energy:
$$20 x^2 - 735.75 x - 22,072.5 = 0$$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_14:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_14:value}}`**

In `{{key:POLY}}`, keying `20 {{key:A}} 735.75 {{key:+/-}} {{key:B}}` loads quadratic coefficient $A = 20.0$ and linear coefficient $B = -735.75$ $(T: 0.0000, Z: 0.0000, Y: 20.0000, X: -735.7500)$. Entering `22072.5 {{key:+/-}} {{key:C}}` stores constant term $C = -22,072.5$ (with cubic constant $D$ defaulting to $0.0$ automatically for depressed quadratic solving, or explicitly keyed as `0 {{key:D}}`) $(T: 20.0000, Z: -735.7500, Y: -22072.5000, X: 0.0000)$. Striking `{{key:EXEC}}` computes Cardano roots; keying `{{key:RCL}} 5` extracts the physical positive maximum dynamic cord elongation $(T: -735.7500, Z: -19.579333, Y: 0.0000, X: \mathbf{56.366833}\text{ m})$ in Register $X$ (with unphysical negative rebound root $-19.5793\text{ m}$ stored in variable 1), confirming **$x = 56.3668\text{ meters}$** (Total fall distance $L + x = 86.37\text{ m}$).

---

### Problem 7.14: Chemical Equilibrium Dissociation Constant ($K_c$)
$N_2 O_4 \rightleftharpoons 2 NO_2$ with $K_c = 0.040$. Initial $[N_2 O_4] = 0.50\text{ M}$:
$$4 x^2 + 0.040 x - 0.020 = 0$$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_15:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_15:value}}`**

In `{{key:POLY}}`, entering `4 {{key:A}} 0.040 {{key:B}}` loads stoichiometry coefficients $A$ and $B$ $(T: 0.0000, Z: 0.0000, Y: 4.0000, X: 0.0400)$. Entering `0.020 {{key:+/-}} {{key:C}}` loads constant $C = -0.020$ (with $D$ defaulting to $0.0$ automatically for depressed quadratic embedding, or explicitly keyed as `0 {{key:D}}`) $(T: 4.0000, Z: 0.0400, Y: -0.0200, X: 0.0000)$. Striking `{{key:EXEC}}` evaluates quadratic roots; keying `{{key:RCL}} 5` isolates the positive dissociated equilibrium concentration $(T: 0.0400, Z: -0.075887, Y: 0.0000, X: \mathbf{0.065887}\text{ M})$ in Register $X$ ($65.89\text{ mM}$).

---

### Problem 7.15: Cantilever Beam Deflection Under Distributed Load
Maximum deflection point of propped cantilever beam requires solving:
$$2 x^3 - 3 L x^2 + L^3 = 0 \implies \text{for } L = 10\text{ m}: \quad 2 x^3 - 30 x^2 + 1000 = 0$$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_16:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_16:value}}`**

In `{{key:POLY}}`, keying `2 {{key:A}} 30 {{key:+/-}} {{key:B}}` registers cubic and quadratic flexural coefficients $(T: 0.0000, Z: 0.0000, Y: 2.0000, X: -30.0000)$. Entering `0 {{key:C}} 1000 {{key:D}}` sets linear coefficient $C = 0.0$ and boundary constant $D = 1000$ $(T: 2.0000, Z: -30.0000, Y: 0.0000, X: 1000.0000)$. Striking `{{key:EXEC}}` runs Cardano's closed-form cubic resolvent, factoring $(x+5)(x-10)^2 = 0$; keying `{{key:RCL}} 3` extracts the physical clamped boundary root $(T: -30.0000, Z: -5.0000, Y: 0.0000, X: \mathbf{10.000000}\text{ m})$ in Register $X$.

---

### Problem 7.16: Rocket Staging Mass Ratio Optimization
Two-stage launch vehicle with payload $m_p = 500\text{ kg}$ and stage structural fractions $\epsilon = 0.10$. Optimal mass distribution requires solving:
$$\lambda^2 - 2 \mu \lambda + \mu = 0 \implies \lambda^2 - 4.828427 \lambda + 2.414214 = 0$$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_03:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_03:value}}`**

In `{{key:POLY}}`, entering `1 {{key:A}} 4.828427 {{key:+/-}} {{key:B}}` enters unit quadratic and negative coupling term $(T: 0.0000, Z: 0.0000, Y: 1.0000, X: -4.828427)$. Entering `2.414214 {{key:C}}` sets structural constant $C = 2.414214$ (with $D$ defaulting to $0.0$ automatically for quadratic solving, or keyed as `0 {{key:D}}`) $(T: 1.0000, Z: -4.828427, Y: 2.414214, X: 0.0000)$. Striking `{{key:EXEC}}` evaluates Cardano roots; keying `{{key:RCL}} 5` yields the optimal stage mass ratio $(T: -4.828427, Z: 0.0000, Y: 0.0000, X: \mathbf{4.261972})$ in Register $X$ (with secondary reciprocal root $\lambda_2 = 0.566455$ in variable 3), confirming **$\lambda = 4.261972$**.

---

### Problem 7.17: Economic Production Batch Size with Deterioration
Cost minimization with exponential decay rate $\theta = 0.05$, setup cost $K = \$250$, demand $D = 10,000\text{ units/yr}$, holding cost $h = \$7.00/\text{unit}\cdot\text{yr}$:
$$Q^* = \sqrt{\frac{2 K D}{h (1 + \theta)}} = \sqrt{\frac{2(250)(10000)}{7(1 + 0.05)}} = \sqrt{\frac{5000000}{7.35}} = \sqrt{680272.11} \approx \mathbf{824.786\text{ units}}$$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_04:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_04:value}}`**

Executing `2 {{key:ENTER}} 250 {{key:×}} 10000 {{key:×}}` evaluates setup inventory numerator product $2KD = 5,000,000.0$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 5000000.0)$. Keying `7 {{key:ENTER}} 1.05 {{key:×}}` computes effective holding cost denominator $h(1+\theta) = 7.3500$ in Register $X$ while numerator waits in $Y$ $(T: 0.0000, Z: 0.0000, Y: 5000000.0, X: 7.3500)$. Striking `{{key:÷}} {{key:√x}}` divides and extracts square root in place, resolving optimal production lot size $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{824.786100})$ directly, confirming **$Q^* = 825\text{ units}$**.

---

### Problem 7.18: Laser Resonator Cavity Gaussian Beam Waist Location
Thermal lens focal length $f = 350\text{ mm}$ inside a symmetric cavity $L = 600\text{ mm}$. Beam waist position root:
$$z_0 = \sqrt{L(2f - L)} = \sqrt{600(700 - 600)} = \sqrt{60,000} \approx \mathbf{244.948974\text{ mm}}$$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_05:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_05:value}}`**

Pushing `350 {{key:ENTER}} 2 {{key:×}} 600 {{key:-}}` evaluates stability difference term $2f - L = 100.0\text{ mm}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 100.0000)$. Keying `600 {{key:×}}` multiplies by cavity length $L$, yielding radicand $L(2f - L) = 60,000.0\text{ mm}^2$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 60000.0000)$. Striking `{{key:√x}}` takes the square root in place, resolving confocal beam waist location $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{244.948974}\text{ mm})$ without scratchpad memory, confirming **$z_0 = 244.95\text{ mm}$**.

---

### Problem 7.19: Centrifugal Pump and Piping System Operating Point
Pump curve $H_p = 60 - 0.002 Q^2$, pipeline head loss $H_s = 15 + 0.005 Q^2$:
$$60 - 0.002 Q^2 = 15 + 0.005 Q^2 \implies 0.007 Q^2 - 45 = 0 \implies Q = \sqrt{45 / 0.007} \approx \mathbf{80.178373\text{ m}^3/\text{hr}}$$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_06:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_06:value}}`**

Running `60 {{key:ENTER}} 15 {{key:-}}` evaluates static head differential $\Delta H = 45.0\text{ m}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 45.0000)$. Keying `0.005 {{key:ENTER}} 0.002 {{key:+}}` computes combined hydraulic loss coefficient $0.0070$ in $X$ with head in $Y$ $(T: 0.0000, Z: 0.0000, Y: 45.0000, X: 0.0070)$. Striking `{{key:÷}} {{key:√x}}` divides and extracts square root, yielding equilibrium pipeline operating discharge $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{80.178373}\text{ m}^3/\text{hr})$, confirming **$Q = 80.18\text{ m}^3/\text{hr}$**.

---

### Problem 7.20: Aerodynamic Drag Crisis Critical Velocity
Sphere diameter $D = 0.15\text{ m}$ in air ($\nu = 1.5 \times 10^{-5}\text{ m}^2/\text{s}$). Drag crisis occurs at $\text{Re}_{\text{crit}} = 3.5 \times 10^5$:
$$v_{\text{crit}} = \frac{\text{Re} \cdot \nu}{D} = \frac{3.5 \times 10^5 \times 1.5 \times 10^{-5}}{0.15} = \frac{5.25}{0.15} = \mathbf{35.0000\text{ m/s}}$$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_07:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_07:value}}`**

Loading `3.5 {{key:E}} 5 {{key:ENTER}} 1.5 {{key:E}} 5 {{key:+/-}} {{key:×}}` multiplies critical Reynolds number by kinematic viscosity, producing momentum circulation product $5.2500\text{ m}^2/\text{s}$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 5.2500)$. Keying `0.15 {{key:÷}}` divides by sphere diameter $D$, directly resolving laminar-to-turbulent transition airspeed $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{35.000000}\text{ m/s})$, confirming **$v_{\text{crit}} = 35.0\text{ m/s}$** ($126.0\text{ km/h}$).

---

> **Thematic Arc III — Chemical Equilibria, Critical Buckling & Economic Optima (Problems 7.21–7.30):** Combining `EQN` expressions with Brent-Dekker bracketing to solve acid-base equilibria, buckling loads, and break-even volumes.

### Problem 7.21: Nuclear Reactor Neutron Flux Critical Dimension
Bare spherical reactor core critical condition: $\frac{\pi}{R} = B_{\text{crit}} = 0.045\text{ cm}^{-1}$:
$$R_{\text{crit}} = \frac{\pi}{0.045} \approx \mathbf{69.813170\text{ cm}}$$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_08:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_08:value}}`**

Evaluating `{{key:π}} 0.045` loads fundamental constant $\pi$ into Register $Y$ and critical geometric buckling $B_{\text{crit}} = 0.045\text{ cm}^{-1}$ into Register $X$ $(T: 0.0000, Z: 0.0000, Y: 3.141593, X: 0.0450)$. Striking `{{key:÷}}` evaluates the ratio in one step, resolving minimum bare spherical core radius $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{69.813170}\text{ cm})$, confirming **$R_{\text{crit}} = 69.81\text{ cm}$**.

---

### Problem 7.22: Non-Linear Torsional Pendulum Oscillation Frequency
Restoring torque $\tau = -k \theta - \alpha \theta^3$. For $k = 10, \alpha = 2$:
$$2 \theta^3 + 10 \theta - 5 = 0$$

**Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_17:keys}}` $\rightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_17:value}}`**

In `{{key:POLY}}`, entering `2 {{key:A}}` loads non-linear cubic coefficient $A = 2.0$ (with quadratic coefficient $B$ defaulting to $0.0$ automatically, or explicitly keyed as `0 {{key:B}}`) $(T: 0.0000, Z: 0.0000, Y: 2.0000, X: 0.0000)$. Entering `10 {{key:C}} 5 {{key:+/-}} {{key:D}}` loads linear restoring torque $C = 10.0$ and external load $D = -5.0$ $(T: 2.0000, Z: 0.0000, Y: 10.0000, X: -5.0000)$. Striking `{{key:EXEC}}` computes Cardano roots; the single real equilibrium deflection angle emerges in Register $Y$ $(T: 2.0000, Z: 0.0000, Y: \mathbf{0.478138}, X: 0.000000)$ with the complex conjugate dynamic mode stored in variables `3`–`6`, or recalled directly via `{{key:RCL}} 1`, confirming **$\theta = 0.478138\text{ radians}$** ($27.40^\circ$).

---

### Problem 7.23: Solar Photovoltaic Cell Fill Factor Root
$V_{\text{oc}} = 0.65\text{ V}, I_{\text{sc}} = 8.5\text{ A}$. Normalized voltage $v_{\text{oc}} = \frac{V_{\text{oc}}}{V_T} = \frac{0.65}{0.02585} \approx 25.145$:
$$\text{Fill Factor } FF = \frac{v_{\text{oc}} - \ln(v_{\text{oc}} + 0.72)}{v_{\text{oc}} + 1} = \frac{25.145 - \ln(25.865)}{26.145} = \frac{25.145 - 3.253}{26.145} = \mathbf{0.8373}$$

> ***The Horner Polynomial Stream & Diode Root Solving*** — Seed open-circuit voltage $V_{\text{oc}} = 0.65\text{ V}$ and short-circuit current in the stack, executing Brent-Dekker root contraction with guaranteed superlinear convergence {{cite:brent1973,hp15c1982}}.

Typing `0.40 {{key:ENTER}} 0.65` primes the stack with the diode conduction voltage bracket $[V_{\min}, V_{\max}]$ $(T: 0.0000, Z: 0.0000, Y: 0.4000, X: 0.6500)$. Striking `{{key:SOLVE}} V` contracts the interval via Brent's hybrid inverse quadratic/bisection algorithm, isolating maximum power point voltage $(T: 0.0000, Z: 0.4000, Y: 0.6500, X: \mathbf{0.541400}\text{ V})$ in 6 iterations without analytical derivatives. Keying `25.145 {{key:ENTER}} 0.72 {{key:+}} {{key:LN}}` evaluates the logarithmic saturation offset $\ln(v_{\text{oc}} + 0.72) \approx 3.2529$ $(T: 0.6500, Z: 0.6500, Y: 0.5414, X: 3.2529)$. Keying `25.145 {{key:x⇄y}} {{key:-}}` evaluates the numerator difference $v_{\text{oc}} - \ln(v_{\text{oc}} + 0.72) \approx 21.8921$ $(T: 0.6500, Z: 0.6500, Y: 0.5414, X: 21.8921)$. Striking `25.145 {{key:ENTER}} 1 {{key:+}} {{key:÷}}` divides by $v_{\text{oc}} + 1 = 26.145$, confirming optimal solar cell fill factor $(T: 0.5414, Z: 0.5414, Y: 0.5414, X: \mathbf{0.837330})$, confirming **$FF = 0.8373$** ($83.73\%$).

---

### Problem 7.24: Friction Clutches Power Transmission Optimum Radius
Flat annular clutch plate: maximum torque capacity occurs when inner radius $r = R / \sqrt{3} \approx \mathbf{0.577350 R}$.

> ***The Inside-Out Radical & Optimal Friction Radius*** — Invert the clutch annular radius ratio squared $1/\sqrt{3}$ directly on the operational stack without scratchpad registers {{cite:hp15c1982}}.

Striking `3 {{key:√x}}` evaluates the radical in place, yielding $\sqrt{3} \approx 1.732051$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.732051)$. Striking `{{key:1/x}}` inverts in place, resolving optimal radius ratio $r_i / r_o = 1/\sqrt{3} \approx 0.577350$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.577350)$. Keying `150 {{key:×}}` scales by outer plate radius $R = 150.0\text{ mm}$, yielding optimal inner contact radius $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{86.602540}\text{ mm})$ without auxiliary memory, confirming **$r_i = 86.6025\text{ mm}$**.

---

### Problem 7.25: Hydraulic Jump Post-Jump Depth (Bélanger Equation)
Upstream flow depth $y_1 = 0.40\text{ m}$, Froude number $\text{Fr}_1 = 4.5$:
$$y_2 = \frac{y_1}{2} (\sqrt{1 + 8 \text{Fr}_1^2} - 1) = \frac{0.40}{2} (\sqrt{1 + 8(20.25)} - 1) = 0.20(\sqrt{163} - 1) = 0.20(12.76715 - 1) = \mathbf{2.3534\text{ meters}}$$

> ***The Inside-Out Radical & Bélanger Hydraulic Jump Pipeline*** — Evaluate Froude radicand $1 + 8\text{Fr}_1^2$ from the innermost core, extract square root, subtract 1, and scale by half upstream depth without scratch memory {{cite:strogatz2019,hp15c1982}}.

Inputting `3.8 {{key:x²}}` squares upstream Froude number $\text{Fr}_1 = 3.80$ to obtain $\text{Fr}_1^2 = 14.440$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 14.4400)$. Striking `8 {{key:×}} 1 {{key:+}}` multiplies by 8 and adds 1, forming Bélanger radicand $1 + 8\text{Fr}_1^2 = 116.5200$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 116.5200)$. Striking `{{key:√x}} 1 {{key:-}}` extracts square root ($\approx 10.7944$) and subtracts 1 to form multiplier factor $9.7944$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 9.7944)$. Striking `0.40 {{key:×}} 2 {{key:÷}}` scales by upstream depth $y_1 = 0.40\text{ m}$ and halves, resolving conjugate subcritical depth $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{1.958900}\text{ m})$ directly, confirming **$y_2 = 1.9589\text{ meters}$**.

---

### Problem 7.26: Acoustical Helmholtz Resonator Volume from Resonance
Neck diameter $d = 30\text{ mm}$ ($A = 706.86\text{ mm}^2$), length $L = 50\text{ mm}$, speed of sound $c = 343\text{ m/s}$. Target resonance $f_0 = 120\text{ Hz}$:
$$f_0 = \frac{c}{2\pi} \sqrt{\frac{A}{V L'}} \implies V = \frac{c^2 A}{4\pi^2 f_0^2 L'}$$
With end-corrected length $L' = 0.050 + 0.85(0.030) = 0.0755\text{ m}$:
$$V = \frac{343^2 \times 7.0686 \cdot 10^{-4}}{4\pi^2 (14400) (0.0755)} = \frac{83.16}{42,912.4} \approx \mathbf{1.9379 \times 10^{-3}\text{ m}^3} = 1.94\text{ liters}$$

Pressing `343 {{key:x²}} 0.00070686 {{key:×}}` squares speed of sound and scales by throat area, forming acoustic numerator product $c^2 A = 83.1618$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 83.1618)$. Keying `2 {{key:π}} {{key:×}} 120 {{key:×}} {{key:x²}} 0.074 {{key:×}}` computes denominator $4\pi^2 f_0^2 L' \approx 42,068.2$ $(T: 0.0000, Z: 0.0000, Y: 83.1618, X: 42068.2)$. Striking `{{key:÷}}` evaluates the chamber volume $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{0.001977}\text{ m}^3)$ ($\approx 1.977\text{ L}$).

---

### Problem 7.27: Relativistic Particle Kinetic Energy from Momentum
Proton ($m_0 c^2 = 938.272\text{ MeV}$) with relativistic momentum $p c = 2,500.0\text{ MeV}$. Total energy:
$$E = \sqrt{(p c)^2 + (m_0 c^2)^2} = \sqrt{2500^2 + 938.272^2} = \sqrt{6250000 + 880354} = \sqrt{7130354} = \mathbf{2,670.272\text{ MeV}}$$
Kinetic energy $K = E - m_0 c^2 = 2670.272 - 938.272 = \mathbf{1,732.000\text{ MeV}}$.

> ***The Inside-Out Radical & Relativistic Energy-Momentum Invariant*** — Square momentum $pc$ and rest mass $m_0 c^2$, sum into total invariant energy squared, extract square root, and subtract rest mass in place without parentheses {{cite:strogatz2019,hp15c1982}}.

Keying `1500 {{key:x²}} 938.272 {{key:x²}} {{key:+}}` computes momentum squared $(pc)^2 = 2,250,000.0\text{ MeV}^2$, rest mass squared, and sums to invariant total energy squared $E^2 \approx 3,130,354.3\text{ MeV}^2$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 3130354.3)$. Striking `{{key:√x}}` extracts total relativistic energy $E \approx 1769.2807\text{ MeV}$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1769.2807)$. Striking `938.272 {{key:-}}` subtracts proton rest energy in place, isolating kinetic energy $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{831.0087}\text{ MeV})$ (for $pc = 1,500\text{ MeV}$).

---

### Problem 7.28: Heat Exchanger Log Mean Temperature Difference (LMTD)
Counter-flow exchanger: $\Delta T_1 = 65^\circ\text{C}, \Delta T_2 = 25^\circ\text{C}$:
$$\text{LMTD} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)} = \frac{65 - 25}{\ln(65 / 25)} = \frac{40}{\ln(2.6)} = \frac{40}{0.955511} = \mathbf{41.8624^\circ\text{C}}$$

> ***The LASTX Dual-Branch Trick & Log Mean Temperature Difference*** — Subtract terminal temperature differentials $\Delta T_1 - \Delta T_2$, recall denominator with `LASTX` or pre-duplicate to evaluate $\ln(\Delta T_1 / \Delta T_2)$ without re-entry {{cite:hp15c1982}}.

Entering `65 {{key:ENTER}} 25 {{key:-}}` computes temperature differential numerator $\Delta T_1 - \Delta T_2 = 40.0^\circ\text{C}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 40.0000)$. Keying `65 {{key:ENTER}} 25 {{key:÷}} {{key:LN}}` evaluates the logarithmic temperature ratio $\ln(\Delta T_1/\Delta T_2) \approx 0.9555$ in $X$ while $40.0$ waits in $Y$ $(T: 0.0000, Z: 0.0000, Y: 40.0000, X: 0.9555)$. Striking `{{key:÷}}` divides numerator by logarithmic factor, resolving log mean temperature difference $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{41.8624^\circ\text{C}})$ directly.

---

### Problem 7.29: Aerodynamic Lift Induced Drag Coefficient
Wing aspect ratio $\text{AR} = 9.5$, Oswald efficiency $e = 0.85$, lift coefficient $C_L = 0.65$:
$$C_{Di} = \frac{C_L^2}{\pi e \text{AR}} = \frac{0.65^2}{\pi(0.85)(9.5)} = \frac{0.4225}{25.3688} = \mathbf{0.016654}$$

Executing `0.65 {{key:x²}}` computes lift coefficient squared $C_L^2 = 0.4225$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.4225)$. Keying `{{key:π}} 9.5 {{key:×}} 0.85 {{key:×}}` evaluates planar denominator $\pi \cdot \text{AR} \cdot e \approx 25.3679$ in $X$ with numerator in $Y$ $(T: 0.0000, Z: 0.0000, Y: 0.4225, X: 25.3679)$. Striking `{{key:÷}}` divides numerator by denominator, yielding induced drag coefficient $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{0.016655})$.

---

### Problem 7.30: Planetary Escaping Orbit Hyperbolic Excess Velocity
Trans-Mars injection burn: geocentric departure velocity $v = 11.45\text{ km/s}$ at parking altitude $r = 6,671\text{ km}$ ($\mu_E = 398,600\text{ km}^3/\text{s}^2$):
$$v_{\infty} = \sqrt{v^2 - \frac{2\mu}{r}} = \sqrt{11.45^2 - \frac{2(398600)}{6671}} = \sqrt{131.1025 - 119.5023} = \sqrt{11.6002} = \mathbf{3.4059\text{ km/s}}$$

***The Inside-Out Radical & Hyperbolic Excess Pipeline*** — Square departure velocity, square escape velocity, subtract to obtain hyperbolic excess energy $v^2 - v_{\text{esc}}^2$, and extract square root in place {{cite:munroe2014,hp15c1982}}.

Pushing `11.45 {{key:x²}}` squares injection burn velocity to obtain $v^2 = 131.1025\text{ km}^2/\text{s}^2$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 131.1025)$. Keying `11.18 {{key:x²}} {{key:-}}` evaluates local escape kinetic term $v_{\text{esc}}^2 = 124.9924\text{ km}^2/\text{s}^2$ and subtracts, establishing hyperbolic excess energy $6.1101\text{ km}^2/\text{s}^2$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 6.1101)$. Striking `{{key:√x}}` takes square root in place, resolving asymptotic interplanetary departure velocity $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{2.4719}\text{ km/s})$ directly.

---

> **Thematic Arc IV — Geotechnical, Compressible Flow & Orbital Solver Applications (Problems 7.31–7.40):** The closing solver arc tackles Rankine earth pressure, Mach-area relations, and geostationary altitude roots.

### Problem 7.31: Soil Mechanics Active Earth Pressure (Rankine Theory)
Internal friction angle $\phi = 32.0^\circ$:
$$K_a = \frac{1 - \sin\phi}{1 + \sin\phi} = \frac{1 - \sin(32^\circ)}{1 + \sin(32^\circ)} = \frac{1 - 0.529919}{1 + 0.529919} = \frac{0.470081}{1.529919} = \mathbf{0.307259}$$

Running `32 {{key:ENTER}} 2 {{key:÷}}` computes half friction angle $\phi/2 = 16.0^\circ$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 16.0000)$. Keying `45 {{key:x⇄y}} {{key:-}}` evaluates slip angle $45^\circ - \phi/2 = 29.0^\circ$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 29.0000)$. Striking `{{key:TAN}} {{key:x²}}` computes tangent and squares in place, directly resolving Rankine active earth pressure coefficient $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{0.307259})$.

---

### Problem 7.32: Viscous Fluid Couette Flow Boundary Layer Thickness
Kinematic viscosity $\nu = 10^{-4}\text{ m}^2/\text{s}$, velocity $U = 2.0\text{ m/s}$, plate distance $h = 0.05\text{ m}$. Reynolds number:
$$\text{Re} = \frac{U h}{\nu} = \frac{2.0 \times 0.05}{10^{-4}} = \mathbf{1,000.0}$$

Loading `0.085 {{key:ENTER}} 2.5 {{key:×}}` loads dynamic viscosity $\mu = 0.085\text{ Pa}\cdot\text{s}$ and scales by velocity $U = 2.50\text{ m/s}$, giving shear product $0.2125\text{ N/m}$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.2125)$. Keying `0.005 {{key:÷}}` divides by gap clearance $h = 0.005\text{ m}$, resolving laminar Couette shear stress $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{42.5000}\text{ Pa})$ directly, confirming **$\tau = 42.50\text{ Pa}$** ($\text{Re} = 1,000.0$).

---

### Problem 7.33: Electrical Skin Depth Resonance
At frequency $f = 13.56\text{ MHz}$ for aluminum ($\sigma = 3.5 \times 10^7\text{ S/m}$):
$$\delta = \frac{1}{\sqrt{\pi f \mu \sigma}} = \mathbf{2.311 \times 10^{-5}\text{ m}} = 23.11\,\mu\text{m}$$

***The Inside-Out Radical & RF Conduction Pipeline*** — Stream frequency, permeability, and conductivity into the electromagnetic attenuation product, take square root, and invert with `{{key:1/x}}` {{cite:horowitz2015,hp15c1982}}.

Evaluating `{{key:π}} 13.56 {{key:E}} 6 {{key:×}}` evaluates angular factor $\pi f \approx 4.2600 \times 10^7\text{ rad/s}$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 4.2600 \times 10^7)$. Keying `4 {{key:π}} {{key:×}} 1 {{key:E}} 7 {{key:+/-}} {{key:×}} {{key:×}}` scales by permeability $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$, yielding $53.5332$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 53.5332)$. Keying `3.5 {{key:E}} 7 {{key:×}}` multiplies by aluminum conductivity $\sigma = 3.5 \times 10^7\text{ S/m}$, giving attenuation product $1.8737 \times 10^9\text{ m}^{-2}$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.8737 \times 10^9)$. Striking `{{key:√x}} {{key:1/x}}` extracts square root and inverts in place, resolving electromagnetic skin depth $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{2.311 \times 10^{-5}}\text{ m})$ ($23.11\,\mu\text{m}$).

---

### Problem 7.34: Atmospheric Barometric Pressure Scale Height
Troposphere temperature $T = 288.15\text{ K}$, molar mass $M = 0.028964\text{ kg/mol}$:
$$H = \frac{R T}{M g} = \frac{8.31446 \times 288.15}{0.028964 \times 9.80665} = \frac{2395.81}{0.28404} = \mathbf{8,434.78\text{ meters}}$$

Typing `8.31446 {{key:ENTER}} 288.15 {{key:×}}` computes thermal gas numerator $RT = 2395.8116\text{ J/mol}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 2395.8116)$. Keying `0.028964 {{key:ENTER}} 9.80665 {{key:×}}` evaluates gravitational denominator $Mg \approx 0.2840\text{ N/mol}$ in $X$ with numerator in $Y$ $(T: 0.0000, Z: 0.0000, Y: 2395.8116, X: 0.2840)$. Striking `{{key:÷}}` divides numerator by denominator, yielding barometric scale height $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{8434.78}\text{ m})$ ($\approx 8.435\text{ km}$).

---

### Problem 7.35: Thin Wall Pressure Vessel Tangential Hoop Stress
Cylindrical pipe with internal pressure $P = 4.5\text{ MPa}$, outer diameter $D = 400\text{ mm}$, wall thickness $t = 8\text{ mm}$:
$$\sigma_{\theta} = \frac{P (D - 2t)}{2 t} = \frac{4.5(384)}{16} = \mathbf{108.0\text{ MPa}}$$

***The LASTX Dual-Branch Trick & Pressure Vessel Sizing*** — Multiply internal pressure by bore diameter and divide by doubled wall thickness directly in the stack without register allocation {{cite:hp15c1982}}.

**Keystrokes:** `400 {{key:ENTER}} 2 {{key:ENTER}} 8 {{key:×}} {{key:-}} 4.5 {{key:×}} 2 {{key:ENTER}} 8 {{key:×}} {{key:÷}}` $\rightarrow$ **`108.0000`**

Inputting `400 {{key:ENTER}} 2 {{key:ENTER}} 8 {{key:×}} {{key:-}}` subtracts double wall thickness $2t = 16\text{ mm}$ from outer diameter $D = 400\text{ mm}$ to yield internal bore diameter $D_i = 384.0\text{ mm}$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 384.0000)$. Keying `4.5 {{key:×}}` multiplies bore diameter by pressure $P = 4.5\text{ MPa}$, producing burst numerator $1728.0\text{ N/mm}$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1728.0000)$. Striking `2 {{key:ENTER}} 8 {{key:×}} {{key:÷}}` evaluates double thickness $16.0\text{ mm}$ and divides, resolving tangential hoop stress $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{108.0000}\text{ MPa})$ directly, confirming **$\sigma_\theta = 108.0\text{ MPa}$**.

---

### Problem 7.36: Gyroscopic Rotor Critical Precession Frequency
Precession angular frequency: $\Omega = \frac{\tau}{I \omega} = \mathbf{0.0450\text{ rad/s}}$.

Pressing `0.85 {{key:ENTER}} 0.012 {{key:ENTER}}` loads applied disturbance torque $\tau = 0.85\text{ N}\cdot\text{m}$ in $Y$ and rotor polar moment of inertia $I = 0.012\text{ kg}\cdot\text{m}^2$ in $X$ $(T: 0.0000, Z: 0.8500, Y: 0.0120, X: 0.0120)$. Keying `15000 {{key:ENTER}} 2 {{key:×}} {{key:π}} {{key:×}} 60 {{key:÷}} {{key:×}}` converts $15,000\text{ RPM}$ into spin velocity $\omega \approx 1570.80\text{ rad/s}$ and multiplies by inertia to establish angular momentum $L = I\omega \approx 18.8496\text{ kg}\cdot\text{m}^2/\text{s}$ $(T: 0.8500, Z: 0.8500, Y: 0.8500, X: 18.8496)$. Striking `{{key:÷}}` divides disturbance torque by angular momentum, yielding gyroscopic precession frequency $(T: 0.8500, Z: 0.8500, Y: 0.8500, X: \mathbf{0.0451}\text{ rad/s})$ ($2.58^\circ/\text{s}$).

---

### Problem 7.37: Compressible Gas Flow Critical Pressure Ratio
Specific heat ratio $\gamma = 1.4$ (air):
$$\frac{P^*}{P_0} = \left(\frac{2}{\gamma + 1}\right)^{\frac{\gamma}{\gamma - 1}} = \left(\frac{2}{2.4}\right)^{3.5} = (0.833333)^{3.5} = \mathbf{0.528282}$$

***The Inside-Out Exponent Ratio & Choked Nozzle Flow*** — Compute stagnation sonic pressure base $2/(\gamma+1)$ and raise to power $\gamma/(\gamma-1)$ inside-out without scratchpad memory {{cite:strogatz2019,hp15c1982}}.

**Keystrokes:** `2 {{key:ENTER}} 1.4 {{key:ENTER}} 1 {{key:+}} {{key:÷}} 1.4 {{key:ENTER}} 1.4 {{key:ENTER}} 1 {{key:-}} {{key:÷}} {{key:yˣ}}` $\rightarrow$ **`0.5283`**

Keying `2 {{key:ENTER}} 1.4 {{key:ENTER}} 1 {{key:+}} {{key:÷}}` divides 2 by $\gamma + 1 = 2.4$ to form stagnation pressure base $2/2.4 \approx 0.833333$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.8333)$. Keying `1.4 {{key:ENTER}} 1.4 {{key:ENTER}} 1 {{key:-}} {{key:÷}}` computes isentropic exponent $\gamma/(\gamma-1) = 3.5000$ in $X$ with base in $Y$ $(T: 0.8333, Z: 0.8333, Y: 0.8333, X: 3.5000)$. Striking `{{key:yˣ}}` raises base to exponent, resolving critical sonic throat pressure ratio $(T: 0.8333, Z: 0.8333, Y: 0.8333, X: \mathbf{0.5283})$ directly ($52.83\%$).

---

### Problem 7.38: Geostationary Orbital Altitude Root
Orbital period $T = 86,164.1\text{ s}$ (sidereal day), standard gravitational parameter $\mu = 3.9860044 \times 10^{14}\text{ m}^3/\text{s}^2$, Earth equatorial radius $R_E = 6,378.14\text{ km}$:
$$r = \left(\frac{\mu T^2}{4\pi^2}\right)^{1/3} = \left(\frac{3.9860044 \cdot 10^{14} \times (86164.1)^2}{4\pi^2}\right)^{1/3} \approx \mathbf{42,164.14\text{ km}}$$
Altitude above equator: $h = 42,164.14 - 6,378.14 = \mathbf{35,786.0\text{ km}}$.

***The Inside-Out Radical & Keplerian Synchronous Radius*** — Evaluate gravitational period product $\mu T^2 / (4\pi^2)$, take cube root in place, and subtract Earth radius without register allocation {{cite:munroe2014,hp15c1982}}.

**Keystrokes:** `3.9860044 {{key:E}} 14 {{key:ENTER}} 86164.1 {{key:x²}} {{key:×}} 4 {{key:÷}} {{key:π}} {{key:x²}} {{key:÷}} 3 {{key:1/x}} {{key:yˣ}} 1000 {{key:÷}} 6378.14 {{key:-}}` $\rightarrow$ **`35786.00`**

Entering `3.9860044 {{key:E}} 14 {{key:ENTER}} 86164.1 {{key:x²}} {{key:×}}` multiplies gravitational parameter $\mu$ by $T^2$, yielding $\mu T^2 \approx 2.9593 \times 10^{24}\text{ m}^5/\text{s}^2$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 2.9593 \times 10^{24})$. Keying `4 {{key:÷}} {{key:π}} {{key:x²}} {{key:÷}}` divides by $4\pi^2$, producing cubed orbital radius $r^3 \approx 7.4960 \times 10^{22}\text{ m}^3$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 7.4960 \times 10^{22})$. Keying `3 {{key:1/x}} {{key:yˣ}}` extracts cube root, resolving geostationary orbital radius $r \approx 42,164,140\text{ m}$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 42164140.0)$. Striking `1000 {{key:÷}} 6378.14 {{key:-}}` converts to kilometers and subtracts Earth radius $R_E$, resolving orbital altitude $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{35786.00}\text{ km})$ directly, confirming **$h = 35,786.0\text{ km}$**.

---

### Problem 7.39: High-Speed Sprint: Cardano Cubic Instant Root
Solve $x^3 - 7x - 6 = 0$. Factorization: $(x+1)(x+2)(x-3) = 0 \implies x_1 = -1, x_2 = -2, x_3 = 3$.
Cardano solver outputs: **$x = 3.0$** in 2 seconds!

***The Horner Polynomial Stream & Cardano Cubic Root*** — Stream cubic polynomial coefficients $x^3 - 7x - 6 = ((x)x - 7)x - 6$ through the stack with alternating multiply and add, finding root $x = 3$ in seconds {{cite:hp15c1982,singh1997}}.

**Keystrokes:** `3 {{key:ENTER}} {{key:ENTER}} {{key:×}} 7 {{key:-}} {{key:×}} 6 {{key:-}}` $\rightarrow$ **`0.0000`**

Executing `3 {{key:ENTER}} {{key:ENTER}} {{key:×}}` loads candidate root $x = 3$ into $Y$ and squares to obtain $x^2 = 9.0000$ in $X$ $(T: 0.0000, Z: 0.0000, Y: 3.0000, X: 9.0000)$. Keying `7 {{key:-}}` subtracts 7 to establish Horner factor $x^2 - 7 = 2.0000$ while $x = 3.0000$ waits in Register $Y$ $(T: 0.0000, Z: 0.0000, Y: 3.0000, X: 2.0000)$. Striking `{{key:×}} 6 {{key:-}}` multiplies directly by the candidate root waiting in $Y$ ($3 \times 2 = 6$) and subtracts 6, confirming exact root residual $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{0.0000})$, confirming **$x = 3.0$** ($f(3) = 0$).

---

### Problem 7.40: High-Speed Sprint: Radical Nested Root Extraction
**Rapid Calculation Sprint:** Find positive roots of biquadratic equation $x^4 - 10 x^2 + 9 = 0$.
Substitute $u = x^2 \implies u^2 - 10 u + 9 = 0 \implies (u-1)(u-9)=0 \implies u=1, 9 \implies x = \mathbf{1.0, 3.0}$.
Solved instantly without pen or paper!

***The Inside-Out Radical & Quartic Root Extraction*** — Transform biquadratic polynomial $x^4 - 10x^2 + 9 = 0$ via quadratic substitution $u = x^2$, evaluate roots with the quadratic formula stream, and extract primary positive roots in place {{cite:strogatz2019,hp15c1982}}.

**Keystrokes:** `10 {{key:x²}} 4 {{key:ENTER}} 9 {{key:×}} {{key:-}} {{key:√x}} 10 {{key:+}} 2 {{key:÷}} {{key:√x}}` $\rightarrow$ **`3.0000`**; `10 {{key:ENTER}} 8 {{key:-}} 2 {{key:÷}} {{key:√x}}` $\rightarrow$ **`1.0000`**

Pushing `10 {{key:x²}} 4 {{key:ENTER}} 9 {{key:×}} {{key:-}} {{key:√x}}` evaluates the discriminant radical $\sqrt{\Delta} = \sqrt{100 - 36} = 8.0000$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 8.0000)$. Keying `10 {{key:+}} 2 {{key:÷}} {{key:√x}}` adds linear coefficient 10 directly to $\sqrt{\Delta}$, halves to $u_1 = 9.0$, and extracts the square root, yielding primary positive root $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{3.0000})$. Keying `10 {{key:ENTER}} 8 {{key:-}} 2 {{key:÷}} {{key:√x}}` evaluates secondary root $u_2 = (10 - 8)/2 = 1.0$ and extracts the square root, yielding second positive root $(T: 0.0000, Z: 0.0000, Y: 3.0000, X: \mathbf{1.0000})$, confirming **$x_1 = 3.0$**, **$x_2 = 1.0$**.

---

## Summary & Looking Ahead

Chapter 7 bridged classical polynomial theory and modern numerical analysis. By chaining synthetic division and Horner's nested polynomial stream through the stack, you evaluated high-order polynomials with minimal keystrokes. You extracted real and complex roots of quadratics and cubics via the hardware polynomial solver (`{{key:POLY}}`), and conquered transcendental equations—from pipe friction factors to transcendental orbital anomalies—using Richard Brent's root finder (`{{key:SOLVE}}`) with guaranteed bracket convergence to $10^{-12}$ accuracy.

Root-finding answers where a function crosses zero, but continuous physical models also require measuring rates of change and accumulating continuous quantities. In **Chapter 8: Calculus, Numerical Derivatives & Romberg Quadrature**, you will take the step into infinitesimal analysis. You will harness the SC-32's Romberg integration engine (`{{key:∫}}`) and Richardson extrapolation to evaluate definite integrals, compute variable rocket motor impulses, and calculate numerical derivatives without manual symbol manipulation.

