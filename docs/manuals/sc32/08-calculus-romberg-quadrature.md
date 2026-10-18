---
title: "Chapter 8: Numerical Calculus & Adaptive Romberg Quadrature | SC-32 Manual"
description: "Master Adaptive Romberg numerical integration [∫], Richardson error cancellation, central-difference numerical differentiation, and applied calculus on the StackCalc SC-32."
---

# Chapter 8: Numerical Calculus & Adaptive Romberg Quadrature

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 CALCULUS // ADAPTIVE ROMBERG INTEGRATION &amp; DERIVATIVES</span>
  <span class="te-viewport-status text-sky-400">● RICHARDSON ERROR EXTRAPOLATION &bull; CENTRAL DIFFERENCE ENGINE &bull; ROCKET THRUST &amp; PROBABILITY INTEGRALS</span>
</div>

## The Application: The Acceleration of the Saturn V & Werner Romberg's Extrapolation

In university calculus, students spend semesters memorizing symbolic anti-derivative techniques: integration by parts, trigonometric substitutions, and partial fractions. Every textbook problem is an artificial puzzle engineered to yield a tidy closed-form formula like $x^3/3$ or $-\cos x$.

Then you step into an aerospace telemetry center or a nuclear fluid dynamics laboratory. **In the real physical universe, almost NO engineering function has a closed-form anti-derivative!**

### The Saturn V Burnout Problem: Integrating Telemetry Under G-Forces

When the five massive Rocketdyne F-1 engines ignite beneath the Apollo Saturn V lunar launch vehicle, they consume fifteen metric tons of kerosene and liquid oxygen every second. As propellants drain from the colossal tanks, the vehicle's thrust-to-weight ratio surges dramatically, pinning the astronauts into their custom contour couches under four and a half times the acceleration of gravity.

Vehicle acceleration $a(t)$ does not follow a sterile, textbook polynomial. It is shaped by supersonic atmospheric compressibility shocks, non-linear atmospheric density gradients, aerodynamic buffet, and propellant sloshing. Real vehicle acceleration is captured not as an equation, but as an empirical **stream of high-frequency telemetry data**.

How fast is the spacecraft travelling when the S-IC first stage burns out at $T = 160\text{ seconds}$? Under the Fundamental Theorem of Calculus, velocity is the definite integral of acceleration:

$$v(T) = v_0 + \int_0^T a(t)\,dt$$

If the flight guidance calculator cannot evaluate that integral with certified numerical precision, engine cut-off will occur fractions of a second too early or too late. A $0.1\%$ velocity shortfall means missing translunar injection entirely and tumbling into the void of deep space.

#### The Trapezoidal Trap: Why Brute Force Fails
Approximating an integral using elementary trapezoidal sums reduces error at a painfully slow pace—proportional to $O(h^2)$, cutting error by a factor of four when slice width is halved. To extract ten decimal digits of precision from a complex curve, a brute-force calculator would need to sample hundreds of thousands of evaluation points, draining battery cells for twenty minutes of continuous calculation.

#### Werner Romberg (1955): Algebraic Error Cancellation
In 1955, Norwegian mathematician Werner Romberg made an extraordinary mathematical breakthrough {{cite:romberg1955}}. By examining the Euler-Maclaurin summation formula, Romberg proved that the truncation error in a composite trapezoidal approximation is not random noise—it is a structured, analytic power series in even powers of the step size:

$$\int_a^b f(t)\,dt = T(h) + c_1 h^2 + c_2 h^4 + c_3 h^6 + \dots$$

Romberg asked a revolutionary question: *Why evaluate millions of microscopic slices when we can take two coarse approximations at step $h$ and step $h/2$, and algebraically combine them to annihilate the dominant $h^2$ error term entirely?*

This is **Richardson extrapolation**. By assembling successive halving approximations into a lower-triangular **Romberg Tableau**, Romberg turned a sluggish $O(h^2)$ crawl into an $O(h^{2k})$ rocket of convergence. Four Romberg step-halvings achieve greater precision than 500,000 brute-force trapezoids.

On the StackCalc SC-32, pressing {{key:∫}} executes Romberg's tableau directly on your operational stack, evaluating non-integrable reality with breathtaking elegance.

<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>{{key:RAD}}</code> (Radians angular mode default; Standard Base-10 Arithmetic; Full 15-digit scientific mantissa <code>{{key:ALL}}</code>). All stack operations assume the default 4-stack XYZT architecture.
</div>

---

## The CRA Pedagogical Progression for Numerical Calculus

Calculus is the mathematical language of continuous change and accumulation. On the StackCalc SC-32, calculus operations follow the **Concrete-Representational-Abstract (CRA)** instructional sequence, translating real-world rates and accumulations into tangible stack interactions:

| Pedagogical Tier | Physical & Cognitive Domain | Implementation on the SC-32 RPN Architecture |
| :--- | :--- | :--- |
| **1. Concrete Level**<br>*(Physical & Empirical Grounding)* | • Physical rate transducers: Telemetry accelerometer sampling vehicle boost acceleration.<br>• Flowmeter measuring non-uniform discharge through a civil culvert.<br>• Spring compression under variable Hooke's displacement.<br>• Physical trapezoidal panels: Visualizing continuous area as an assembly of concrete geometric trapezoids spanning adjacent grid stations. | Direct data sampling from physical instrumentation prior to digital accumulation. |
| **2. Representation Level**<br>*(Stack Register Visualizations)* | • The Romberg Tableau $R(k, j)$: Triangular matrix of successive approximations canceling $h^2, h^4, h^6$ error terms.<br>• Stack register protocol: Integration limits $(a, b)$ loaded into $(Y, X)$; after execution, Register $X$ displays definite integral $I$, Register $Y$ displays error bound $\pm\varepsilon$. | Transflective LCD dot-matrix integration status line and 4-stack preservation. |
| **3. Abstract Level**<br>*(Analytical Theorems & Asymptotic Expansions)* | • Fundamental Theorem of Calculus: $\frac{d}{dx} \left[\int_a^x f(t)\,dt\right] = f(x)$<br>• Euler-Maclaurin asymptotic expansion of numerical quadrature errors:<br>&nbsp;&nbsp;$\int_a^b f(x)\,dx = T(h) + c_1 h^2 + c_2 h^4 + c_3 h^6 + \dots$<br>• Richardson extrapolation: Analytical elimination of dominant truncation powers without requiring infinitesimal step sizes. | Certified 64-bit IEEE-754 adaptive quadrature engine via {{key:∫}}. |

{{blocks:sc32_rpn_calculation|Active RPN Calculation on Transflective LCD}}

{{res:sc32_plot_romberg_shaded:screenshot|SC-32 Vector Plotter: Shaded Definite Integral of 3x^2 from 0 to 4 (Area = 64.0)}}
*Figure 8.1: The SC-32 transflective display executing active numerical integration, demonstrating real-time stack updates and error bound estimation.*

---

## Adaptive Romberg Numerical Quadrature ({{key:∫}})

<div class="admonition tip">
<p class="admonition-title">The Feynman Intuition: The Coastline of Britain &amp; The Richardson Leap</p>
<p>Suppose you set out to measure the perimeter of a rugged, rocky island. You walk along the shore with a 10-meter chain, recording a total distance of 1,000 meters. Next, you re-measure the same coastline with a 5-meter rod. Because the shorter rod fits into small bays and rocky inlets, your measurement increases to 1,200 meters!</p>
<p>Traditional brute-force intuition insists: <em>To find the true, exact value, we must measure with a 1-centimeter ruler, then a 1-millimeter gauge, taking forever.</em></p>
<p>In 1910, English polymath Lewis Fry Richardson discovered a profound mathematical shortcut: <strong>You do not need an infinite number of microscopic rulers!</strong> If you understand mathematically how measurement error scales with the size of your ruler (for instance, error proportional to $h^2, h^4, h^6$), you can algebraically combine your 10-meter and 5-meter measurements to cancel the error completely!</p>
<p>That is Richardson Extrapolation—the analytical engine inside Werner Romberg's 1955 quadrature algorithm. It evaluates a few coarse trapezoids and then uses the geometry of error to vault directly to $10^{-12}$ precision with over $95\%$ fewer function evaluations.</p>
</div>

{{blocks:prime_studio_comparator_stage|Prime Studio Comparator Stage Slide Rule}}
*Figure 8.2: The bilateral Prime Studio slide rule comparator stage physically illustrates logarithmic scaling and proportional interval halving corresponding to Richardson extrapolation steps.*

Definite integrals calculate accumulated physical quantities across continuous domains: total distance traversed under non-constant velocity, mechanical work performed under variable forces, electrical charge accumulated from transient current pulses, and fluid pressure forces exerted across curved dams.

The StackCalc SC-32 evaluates definite integrals using **Adaptive Romberg Numerical Quadrature ({{key:∫}})**:

$$I = \int_a^b f(x) \, dx$$

<div class="admonition note">
<p class="admonition-title">Romberg Quadrature &amp; Richardson Error Extrapolation</p>
<ol>
<li><strong>Successive Step-Size Halving (Trapezoidal Base):</strong><br>
$$h_0 = b - a, \quad h_1 = \frac{h_0}{2}, \quad h_2 = \frac{h_1}{2}, \quad \dots, \quad h_k = \frac{b - a}{2^k}$$</li>
<li><strong>Richardson Extrapolation Tableau:</strong><br>
Base column: $R(k, 0) = \text{Extended Trapezoidal sum at step } h_k$<br>
Recursive update: $$R(k, j) = R(k, j-1) + \frac{R(k, j-1) - R(k-1, j-1)}{4^j - 1}$$
</li>
</ol>

| Column Index | Classical Quadrature Rule Equivalent | Error Order | Convergence Characteristics |
| :---: | :--- | :---: | :--- |
| **$j = 0$** | Extended Composite Trapezoidal Rule | $\mathcal{O}(h^2)$ | Coarse baseline; samples function boundaries and midpoints. |
| **$j = 1$** | Simpson's $1/3$ Parabolic Rule | $\mathcal{O}(h^4)$ | Cancels leading $h^2$ error term via 4:1 weighting. |
| **$j = 2$** | Boole's 5-Point Rule | $\mathcal{O}(h^6)$ | Cancels $h^4$ curvature artifact; achieves 6 digits. |
| **$j = 3$** | High-Order Analytical Extrapolation | $\mathcal{O}(h^8)$ | Sub-ppm precision on smooth transcendentals. |
| **$j = 4$** | Machine Epsilon Extrapolation Limit | $\mathcal{O}(h^{10}) < 10^{-12}$ | Terminates when $\lvert R(k, k) - R(k-1, k-1)\rvert < 10^{-11}$. |

</div>

### The Lower-Triangular Romberg Tableau
As step size $h_k = (b - a)/2^k$ is halved at each row $k$, the algorithm populates the lower-triangular Romberg matrix $R(k, j)$ from left to right. Within 4 to 6 step halvings, the diagonal entry $R(k, k)$ achieves **$10^{-12}$ precision** with over **95% fewer function evaluations** than standard composite quadrature:

| Step Index $k$ | Intervals ($2^k$) | Step Size $h_k$ | Column $j=0$ (Trapezoid) | Column $j=1$ (Simpson) | Column $j=2$ (Boole) | Column $j=3$ (Extrapolated) |
| :---: | :---: | :---: | :--- | :--- | :--- | :--- |
| **$k = 0$** | 1 | $b - a$ | $R(0, 0)$ [Trapezoid] | — | — | — |
| **$k = 1$** | 2 | $(b - a)/2$ | $R(1, 0)$ | $\longrightarrow R(1, 1)$ [Simpson] | — | — |
| **$k = 2$** | 4 | $(b - a)/4$ | $R(2, 0)$ | $\longrightarrow R(2, 1)$ | $\longrightarrow R(2, 2)$ [Boole] | — |
| **$k = 3$** | 8 | $(b - a)/8$ | $R(3, 0)$ | $\longrightarrow R(3, 1)$ | $\longrightarrow R(3, 2)$ | $\longrightarrow R(3, 3)$ |

### Avoidance of Runge's Phenomenon
When engineers attempt high-accuracy quadrature by fitting a high-degree polynomial across equally spaced points (as in high-order Newton-Cotes formulas like Weddle's Rule or 10-point formulas), they encounter **Runge's Phenomenon**: wild polynomial oscillations near the boundaries of the interval that cause numerical error to explode exponentially.

Romberg Quadrature completely eliminates Runge's phenomenon:
1. **Low-Order Local Panels:** It evaluates only stable, piecewise linear trapezoids on local sub-intervals $h_k$.
2. **Global Richardson Convergence:** High-order accuracy is achieved not by increasing polynomial degree across the whole interval, but by extrapolating step sizes $h \to 0$ in the frequency domain.
3. **Monotonic Error Decay:** Each diagonal entry $R(k, k)$ provides a strictly contracting upper error bound without spurious boundary ringing.

### Concrete Romberg Tableau Walkthrough: $\int_0^2 e^x \, dx = e^2 - 1 \approx 6.389056$
Observe how the SC-32 builds the Romberg tableau step-by-step:
* **Step $k=0$ ($h_0 = 2.0$):**
  $$R(0, 0) = \frac{2}{2} [e^0 + e^2] = 1.0 \times [1.0 + 7.389056] = 8.389056$$
* **Step $k=1$ ($h_1 = 1.0$):**
  $$R(1, 0) = \frac{1}{2} R(0, 0) + 1.0 \times e^1 = 4.194528 + 2.718282 = 6.912810$$
  $$R(1, 1) = \frac{4 R(1, 0) - R(0, 0)}{3} = \frac{4(6.912810) - 8.389056}{3} = \frac{27.651240 - 8.389056}{3} = \mathbf{6.420728} \quad (\text{Simpson!})$$
* **Step $k=2$ ($h_2 = 0.5$):**
  $$R(2, 0) = \frac{1}{2} R(1, 0) + 0.5 \times [e^{0.5} + e^{1.5}] = 3.456405 + 0.5[1.648721 + 4.481689] = 6.521610$$
  $$R(2, 1) = \frac{4(6.521610) - 6.912810}{3} = 6.391210$$
  $$R(2, 2) = \frac{16 R(2, 1) - R(1, 1)}{15} = \frac{16(6.391210) - 6.420728}{15} = \mathbf{6.389242} \quad (\text{Boole!})$$

In only 2 step halvings, the error drops from $+31.3\%$ to $+0.0029\%$. By $k=4$, error is below $10^{-12}$.

### Stack Operational Convention for {{key:∫}}
* **Lower Limit $a$:** Placed in Register $Y$.
* **Upper Limit $b$:** Placed in Register $X$.
* **Target Variable of Integration:** Specified as an argument (e.g. `{{key:∫}} X` or `{{key:∫}} T`).
* **Output Display:**
  * **Register $X$ receives:** The evaluated definite integral $I = \int_a^b f(x) dx$.
  * **Register $Y$ receives:** The estimated numerical error bound $\pm \epsilon$.
  * **Registers $Z$ and $T$:** Preserved from prior stack state.

---

## Grounded Case 1: Rocket Motor Burnout Velocity Integration

During the boost phase of a solid-propellant model rocket, combustion chamber pressure and progressive propellant grain geometry produce a non-linear acceleration curve over burn duration $t \in [0, 6]\text{ seconds}$:

$$a(t) = 4 t^2 - 0.5 t^3 \quad (\text{m/s}^2)$$

Determine the rocket's burnout velocity $v_{\text{burn}}$ at $t = 6\text{ seconds}$ by integrating acceleration from $t = 0$ to $t = 6$:

$$v_{\text{burn}} = \int_0^6 \left(4 t^2 - 0.5 t^3\right) \, dt$$

### Analytical Derivation
$$\int_0^6 \left(4 t^2 - 0.5 t^3\right) \, dt = \left[ \frac{4}{3} t^3 - \frac{0.5}{4} t^4 \right]_0^6 = \frac{4}{3}(216) - \frac{1}{8}(1296) = 288.0 - 162.0 = \mathbf{126.0\text{ m/s}}$$

### RPN Keystroke Protocol on the SC-32
1. **Enter Equation into Bank:**
   Press `{{key:EQN}}` to open the Equation Editor. Key the postfix tokens:
   `T {{key:x²}} 4 {{key:×}} T 3 {{key:yˣ}} 0.5 {{key:×}} {{key:-}}`
   Press `{{key:ENTER}}` to save under label `ROCKET`.
2. **Load Integration Limits:**
   Lower limit $a = 0$ into $Y$, upper limit $b = 6$ into $X$:
   `0 {{key:ENTER}} 6`
3. **Execute Romberg Integration:**
   Press `{{key:∫}} T`.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}} 6` | $0.0000$ | $0.0000$ | $0.0000$ | $6.0000$ | Limits: $a=0$ in $Y$, $b=6$ in $X$ |
| 2 | `{{key:∫}} T` | $0.0000$ | $0.0000$ | **$1.2435 \times 10^{-11}$** | **$126.000000000$** | Burnout velocity $v_{\text{burn}}$ in m/s |

| Stack Register | Converged Romberg Output | Physical Meaning |
| :---: | :---: | :--- |
| **`T`** | `0.0000000000` | Cleared top register |
| **`Z`** | `0.0000000000` | Cleared third register |
| **`Y`** | `1.243500e-11` | Estimated Romberg truncation error bound $\pm\varepsilon$ |
| **`X`** | **`126.0000000000`** | Integrated burnout velocity $v_{\text{burn}}$ ($\text{m/s}$) |

The burnout velocity converges to **$126.0\text{ m/s}$** ($453.6\text{ km/h}$) with an estimated error bound under $2 \times 10^{-11}$.

---

## Grounded Case 2: Gaussian Normal CDF & Error Function Integration

The cumulative distribution function (CDF) of the standard Gaussian Normal distribution $\mathcal{N}(0, 1)$ requires evaluating the integral:

$$\Phi(z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^z e^{-t^2 / 2} \, dt$$

Because the Gaussian density has infinite tails, numerical integration evaluates from a lower truncation bound ($a = -5.0$) where the omitted tail area is less than $2.87 \times 10^{-7}$. Evaluate $\Phi(0) = 0.500000$:

$$\Phi(0) \approx \frac{1}{\sqrt{2\pi}} \int_{-5}^0 e^{-x^2 / 2} \, dx$$

### Equation Setup in `{{key:EQN}}`
Tokens: `X {{key:x²}} 2 {{key:÷}} {{key:+/-}} {{key:eˣ}} 2 {{key:π}} {{key:×}} {{key:√x}} {{key:÷}}`
Save as `NORM`.

### Execution
1. Load limits: `5 {{key:+/-}} {{key:ENTER}} 0`
2. Execute: `{{key:∫}} X`

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `5 {{key:+/-}} {{key:ENTER}} 0` | $0.0000$ | $0.0000$ | $-5.0000$ | $0.0000$ | Integration interval $[-5, 0]$ |
| 2 | `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$2.15 \times 10^{-10}$** | **$0.5000000000$** | $\Phi(0) = 0.500000$ |

The SC-32 returns **$0.500000$**, exactly verifying symmetry.

---

## Numerical Differentiation: Central Differences on the RPN Stack

In addition to definite integration, the SC-32 evaluates numerical derivatives to high accuracy using the symmetric **central-difference formula**:

$$f'(x) \approx \frac{f(x + h) - f(x - h)}{2 h}$$
$$f''(x) \approx \frac{f(x + h) - 2 f(x) + f(x - h)}{h^2}$$

<div class="admonition note">
<p class="admonition-title">Central Difference Numerical Differentiation Mechanics</p>
<ol>
<li><strong>First Derivative (Central Difference, $\mathcal{O}(h^2)$):</strong>
$$f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}$$
Because the forward and backward Taylor expansions cancel both $f(x)$ and the even $\frac{1}{2}h^2 f''(x)$ quadratic term, central differencing achieves $\mathcal{O}(h^2)$ accuracy with just two evaluations.</li>
<li><strong>Optimal Step-Size Selection:</strong>
$$h = 10^{-5} \cdot \max(1, |x|)$$
Balances Taylor truncation error $\mathcal{O}(h^2)$ against IEEE-754 floating-point subtraction cancellation.</li>
<li><strong>Higher-Order Richardson Derivative ($\mathcal{O}(h^4)$):</strong>
$$f'(x) \approx \frac{4 D(h/2) - D(h)}{3}$$</li>
</ol>
</div>

### Grounded Test: Central-Difference Derivative of $f(x) = x^2$ at $x = 3.0$
Using step $h = 10^{-5}$ ($x + h = 3.00001$, $x - h = 2.99999$, $2h = 0.00002$):
1. Evaluate $f(x + h)$: `3.00001 {{key:x²}}`
2. Evaluate $f(x - h)$ and subtract: `2.99999 {{key:x²}} {{key:-}}`
3. Divide by $2h$: `0.00002 {{key:÷}}`
* Register $X$ outputs: **$6.0000000000$** ($f'(3) = 2(3) = 6.0$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `3.00001 {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $9.000060$ | Forward point $f(x_0 + h) = 3.00001^2$ |
| 2 | `2.99999 {{key:x²}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.000120$ | Central difference $f(x_0 + h) - f(x_0 - h)$ |
| 3 | `0.00002 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$6.0000000000$** | Central-difference derivative $f'(3) = 6.0$ |

---

## Singularity Handling & Non-Integrable Boundary Detection

When an integrand possesses an essential singularity, pole, or vertical asymptote within the integration interval $[a, b]$, classical numerical quadrature can diverge to infinity.

Consider integrating $f(x) = 1/x$ from $a = 0$ to $b = 1$:
$$\int_0^1 \frac{1}{x} \, dx = [\ln x]_0^1 = 0 - (-\infty) = +\infty$$

### Firmware Singularity Trap
When the Romberg engine evaluates the integrand at $x = 0$, the SC-32 hardware detects division by zero:
1. Halts the trapezoidal accumulation loop immediately.
2. Displays **`Error 02: DIVIDE BY 0`** on the status line.
3. Sets Register $X = 0.0$ and leaves stack registers intact for recovery.

---

## Teaching & Instrument Architecture Notes

### Richardson Extrapolation & Algorithmic Efficiency
In introductory calculus, students learn Riemann sums with left, right, and trapezoidal endpoints. Achieving even four digits of precision with uniform trapezoids requires millions of sub-intervals. Romberg quadrature demonstrates how mathematical insight surpasses brute-force computation: by combining two coarse approximations evaluated at step sizes $h$ and $h/2$, Richardson extrapolation cancels the leading $O(h^2)$ truncation error term algebraically. On the SC-32, students observe that extracting rocket motor burnout velocities ($126.0\text{ m/s}$) converges within a fraction of a second to an error bound of $10^{-11}$.

### Numerical Quadrature in Real-World STEM Modeling
While textbook calculus emphasizes symbolic integration of idealized elementary functions, practical engineering problems routinely involve empirical data, non-linear rate equations, or non-integrable forms. When calculating total impulse or burnout velocity for a solid-fuel motor, published thrust profiles are higher-order polynomials or piecewise spline fits. Similarly, evaluating cumulative normal probabilities requires integrating the Gaussian bell curve over arbitrary bounds. Entering the integrand into the SC-32 and executing Romberg quadrature grounds abstract calculus in direct numerical reality.

### Dual-Register Return & Heritage of the HP-34C
In 1979, the Hewlett-Packard HP-34C became the world's first handheld calculator with numerical integration, engineered under the guidance of Turing Award laureate Prof. William Kahan {{cite:kahan1979}}. StackCalc SC-32 advances this lineage with 64-bit IEEE-754 arithmetic and a dynamic Romberg tableau driving truncation error below $10^{-12}$. Crucially, the SC-32 delivers both the definite integral in Register $X$ and the certified uncertainty bound $\pm\epsilon$ in Register $Y$. Inspecting Register $Y$ after execution provides immediate confirmation of numerical convergence without requiring secondary verification runs.

---

## Diagnostic Checkpoints & Singularity Handling

> [!CHECKPOINT]
> **Diagnostic Checkpoint 8.1: Limit Ordering Convention**  
> Remember the fundamental identity $\int_b^a f(x) dx = -\int_a^b f(x) dx$.
> * Lower limit $a$ must be in Register $Y$.
> * Upper limit $b$ must be in Register $X$.
> * If you enter the upper limit first, the result will have the opposite sign!

> [!CHECKPOINT]
> **Diagnostic Checkpoint 8.2: Angular Mode Discipline in Trig Integrals**  
> All calculus operations involving trigonometric functions (`SIN`, `COS`, `TAN`) mathematically require **Radians mode (`{{key:RAD}}`)**. Because $d/dx[\sin x] = \cos x$ is only valid when $x$ is measured in radians (in degrees, a scaling factor of $\pi/180$ appears), running numerical integration on trig equations in `{{key:DEG}}` produces erroneous results scaled by $(180/\pi)$.

> [!CHECKPOINT]
> **Diagnostic Checkpoint 8.3: Inspection of Error Estimate ($\pm\epsilon$)**  
> After every integration, press `{{key:x⇄y}}` to inspect Register $Y$. If Register $Y$ shows a value like $1.4 \times 10^{-11}$, the integral converged to full precision. If Register $Y$ shows a large value (e.g. $0.05$), the integrand may be highly oscillatory or near a singularity, requiring interval subdivision.

---

## Engineering Design Briefing: Saturn V Rocket Motor Thrust Integration (Problems 8.1 through 8.40)

<div class="admonition warning">
<p class="admonition-title">Inside-Out Stack Architecture: Algebraic Trap vs. RPN Shortcut — Definite Numerical Integration &amp; Richardson Extrapolation</p>
<p><strong>The Algebraic Parenthesis Trap:</strong> Numerical integration of non-linear rate equations (e.g., rocket motor variable thrust $F(t) = k_1 t + k_2 t^3$ or aerodynamic drag) on algebraic calculators requires entering lengthy formula strings into an opaque integration prompt:</p>
<pre><code>fnInt( 2500 * X + 40000 * X ^ 3, X, 0, 0.15 )</code></pre>
<p>If an engineer omits a multiplication symbol or groups an exponent ambiguously, the evaluation either runs indefinitely, drains the battery, or returns an undocumented convergence error without indicating which interval failed {{cite:brent1973}}.</p>
<p><strong>The RPN Stack Shortcut:</strong> The SC-32 executes Adaptive Romberg Quadrature (<code>{{key:∫}}</code>) by combining deterministic postfix equation execution with automated Richardson extrapolation {{cite:romberg1955}}. The user defines the integrand directly in RPN, sets the limits $a$ and $b$ onto the stack, and presses <code>{{key:∫}}</code>. The dual-core engine evaluates step sizes dynamically, eliminates low-order truncation error via $O(h^4) \to O(h^6) \to O(h^8)$ tableau refinement, and returns the certified integral into Register $X$ while depositing the estimated absolute error directly into Register $Y$ for instant stack inspection.</p>
</div>

### The Algebraic Trap vs. StackCalc Superpower Showdown

| Challenge / Metric | Algebraic Trap (TI-84 / Infix) | Algebraic Strokes | StackCalc SC-32 Superpower | SC-32 Strokes | Superpower Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **Definite Numerical Integration**: Variable spring compression work | Menu dive into `[MATH] [9:fnInt(]`, type expression string `2500*X+40000*X^3,X,0,0.15)` (38 strokes). Ambiguous operator precedence between multiplication and exponentiation causes silent evaluation errors or syntax crashes; adaptive Simpson heuristic provides no certified error register on completion. | 38 | **Adaptive Romberg Quadrature (`{{key:∫}}`)**: Define postfix integrand `X 2500 {{key:×}} X 3 {{key:yˣ}} 40000 {{key:×}} {{key:+}}`, push limits `0 {{key:ENTER}} 0.15`, press `{{key:∫}} X` (18 strokes). Richardson tableau extrapolation eliminates $O(h^2), O(h^4), O(h^6)$ error in 3 halving cycles, returning certified $W = 33.1875\text{ J}$ to $X$ and absolute error bound $\pm 3.55 \times 10^{-12}$ to $Y$! | 18 | **53% fewer strokes + certified error bound in $Y$** |
| **Gaussian Normal Probability CDF**: $\Phi(1.96)$ bell curve | Menu dive or catalog search for `normalcdf(0, 1.96, 0, 1)` or nested integration `fnInt(e^(-(X^2)/2)/√(2*π), X, 0, 1.96)` (44 strokes). Opaque black box hides numerical error; parenthesis nesting around negative exponent `-(X^2)/2` frequently misinterprets as `(-X)^2/2` without warning. | 44 | **Non-Integrable Transcendentals via Richardson Extrapolation**: Program standard normal bell `T {{key:x²}} 2 {{key:÷}} {{key:+/-}} {{key:eˣ}} 2 {{key:π}} {{key:×}} {{key:√x}} {{key:÷}}`, push limits `0 {{key:ENTER}} 1.96`, press `{{key:∫}} T` (20 strokes). Converges in $<0.2\text{ s}$ to 12-digit precision ($0.4750021049$), with full stack visibility for direct summation `0.5 {{key:+}}` $\to 0.9750021049$! | 20 | **55% fewer strokes + complete stack transparency** |

---

> **Thematic Arc I — Mechanical Work, Centroids & Definite Polynomial Integrals (Problems 8.1–8.10):** We begin by verifying Richardson-extrapolated Romberg quadrature (`∫f`) against exact analytical antiderivatives in mechanics.

### Problem 8.1: Work Done During Variable Spring Compression
A non-linear progressive suspension spring exerts restoring force $F(x) = k_1 x + k_2 x^3$, where $k_1 = 2,500\text{ N/m}$ and $k_2 = 40,000\text{ N/m}^3$. Calculate work done compressing from $x = 0$ to $x = 0.15\text{ m}$:
$$W = \int_0^{0.15} (2500 x + 40000 x^3) \, dx = \left[ 1250 x^2 + 10000 x^4 \right]_0^{0.15}$$
$$W = 1250(0.0225) + 10000(0.00050625) = 28.125 + 5.0625 = \mathbf{33.1875\text{ Joules}}$$

Program: `X 2500 {{key:×}} X 3 {{key:yˣ}} 40000 {{key:×}} {{key:+}}`. Limits: `0 {{key:ENTER}} 0.15`. Execute: `{{key:∫}} X`.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}} 0.15` | $0.0000$ | $0.0000$ | $0.0000$ | $0.1500$ | Limits $a=0, b=0.15$ |
| 2 | `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$3.55 \times 10^{-12}$** | **$33.187500000$** | Work $W$ in Joules |

**Analytical Stack Verification:** {{res:sc32_08_calc_01:keys}} $\implies \mathbf{{{res:sc32_08_calc_01:value}}\text{ Joules}}$.

---

### Problem 8.2: Total Electrical Charge Accumulated from Exponential Surge
Lightning surge current pulse $I(t) = I_0 e^{-t / \tau}$, with $I_0 = 10,000\text{ A}$ and decay time constant $\tau = 50\,\mu\text{s} = 5.0 \times 10^{-5}\text{ s}$. Total charge transferred from $t = 0$ to $t = 250\,\mu\text{s}$ ($5\tau$):
$$Q = \int_0^{2.5 \cdot 10^{-4}} 10000 e^{-t / 5 \cdot 10^{-5}} \, dt = 10000(5 \cdot 10^{-5}) [1 - e^{-5}] = 0.50 [1 - 0.006738] = \mathbf{0.496631\text{ Coulombs}}$$

Program: `T 5 {{key:E}} 5 {{key:+/-}} {{key:÷}} {{key:+/-}} {{key:eˣ}} 10000 {{key:×}}`. Limits: `0 {{key:ENTER}} 2.5 {{key:E}} 4 {{key:+/-}}`. Execute: `{{key:∫}} T`.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}} 2.5 {{key:E}} 4 {{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.000250$ | Limits $a=0, b=250\,\mu\text{s}$ |
| 2 | `{{key:∫}} T` | $0.0000$ | $0.0000$ | **$1.12 \times 10^{-11}$** | **$0.496631098$** | Charge $Q$ in Coulombs |

**Analytical Stack Verification:** {{res:sc32_08_calc_02:keys}} $\implies \mathbf{{{res:sc32_08_calc_02:value}}\text{ C}}$.

---

### Problem 8.3: Exponential Distribution CDF Integral
Cumulative failure probability $F(t) = \int_0^1 e^{-x} dx$:
$$\int_0^1 e^{-x} \, dx = 1 - e^{-1} \approx 1 - 0.3678794 = \mathbf{0.632120559}$$

Program the integrand into `{{key:EQN}}` as `X {{key:+/-}} {{key:eˣ}}`. Load the integration bounds `0 {{key:ENTER}} 1` $(T: 0.0000, Z: 1.0000, Y: 0.0000, X: 1.0000)$, and press `{{key:∫}} X`. The Romberg engine evaluates the exponential CDF integral, yielding the certified error estimate $4.82 \times 10^{-12}$ in Register $Y$ and the definite integral $1 - e^{-1} \approx \mathbf{0.632120559}$ in Register $X$ $(T: 0.0000, Z: 1.0000, Y: 4.82\times 10^{-12}, X: 0.632120559)$.

**Analytical Stack Verification:** {{res:sc32_08_calc_03:keys}} $\implies \mathbf{{{res:sc32_08_calc_03:value}}}$.

---

### Problem 8.4: Uniform Distribution Probability Integral
$f(x) = 0.10$ over interval $[0, 5]$:
$$\int_0^5 0.10 \, dx = 0.10 \times 5 = \mathbf{0.500000}$$

Program the uniform probability density `0.1` into `{{key:EQN}}`. Push interval limits `0 {{key:ENTER}} 5` $(T: 0.0000, Z: 0.1000, Y: 0.0000, X: 5.0000)$, then execute `{{key:∫}} X`. Because the density is uniform, the initial panel computation is exact, yielding an error bound of $0.0000$ in Register $Y$ and the exact probability $\mathbf{0.500000000}$ in Register $X$ $(T: 0.0000, Z: 0.1000, Y: 0.0000, X: 0.500000000)$.

**Analytical Stack Verification:** {{res:sc32_08_calc_04:keys}} $\implies \mathbf{{{res:sc32_08_calc_04:value}}}$.

---

### Problem 8.5: Gaussian Normal 1-Sigma Confidence Interval ($68.27\%$)
Integrate standard normal PDF from $z = -1.0$ to $z = +1.0$:
$$P(-1 \le Z \le 1) = \frac{1}{\sqrt{2\pi}} \int_{-1}^1 e^{-x^2 / 2} \, dx \approx \mathbf{0.682689492}$$

Program the standard normal curve `NORM`. Push the $1\sigma$ limits `1 {{key:+/-}} {{key:ENTER}} 1` $(T: 0.0000, Z: 0.0000, Y: -1.0000, X: 1.0000)$, then execute `{{key:∫}} X`. The Romberg tableau performs successive Richardson extrapolations across the bell curve, returning error bound $1.85 \times 10^{-11}$ in Register $Y$ and the $68.27\%$ confidence area $\mathbf{0.682689492}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 1.85\times 10^{-11}, X: 0.682689492)$.

---

### Problem 8.6: Gaussian Normal 2-Sigma Confidence Interval ($95.45\%$)
Integrate standard normal PDF from $z = -2.0$ to $z = +2.0$:
$$P(-2 \le Z \le 2) = \frac{1}{\sqrt{2\pi}} \int_{-2}^2 e^{-x^2 / 2} \, dx \approx \mathbf{0.954499736}$$

Using the same `NORM` equation, load the $2\sigma$ limits `2 {{key:+/-}} {{key:ENTER}} 2` $(T: 0.0000, Z: 0.0000, Y: -2.0000, X: 2.0000)$ and press `{{key:∫}} X`. The tableau converges rapidly to error bound $3.14 \times 10^{-11}$ in $Y$ and delivers the two-sided $95.45\%$ confidence integral $\mathbf{0.954499736}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 3.14\times 10^{-11}, X: 0.954499736)$.

---

### Problem 8.7: Gaussian Normal 3-Sigma Confidence Interval ($99.73\%$)
Integrate standard normal PDF from $z = -3.0$ to $z = +3.0$:
$$P(-3 \le Z \le 3) = \frac{1}{\sqrt{2\pi}} \int_{-3}^3 e^{-x^2 / 2} \, dx \approx \mathbf{0.997300204}$$

Push the $3\sigma$ bounds `3 {{key:+/-}} {{key:ENTER}} 3` $(T: 0.0000, Z: 0.0000, Y: -3.0000, X: 3.0000)$ and execute `{{key:∫}} X`. Romberg extrapolation captures the extreme tails to error bound $5.22 \times 10^{-11}$ in $Y$, placing the standard $99.73\%$ confidence area $\mathbf{0.997300204}$ into Register $X$ $(T: 0.0000, Z: 0.0000, Y: 5.22\times 10^{-11}, X: 0.997300204)$.

---

### Problem 8.8: Hydrostatic Fluid Pressure Force on Vertical Parabolic Gate
Water dam gate bounded by $y = 0.5 x^2$ from $y = 0$ to $y = 4.0\text{ m}$. Width $w(y) = 2x = 2\sqrt{2y} = \sqrt{8y}$.
Depth below surface: $h(y) = 4 - y$. Fluid density $\rho = 1,000\text{ kg/m}^3, g = 9.81\text{ m/s}^2$:
$$F = \rho g \int_0^4 (4 - y) \sqrt{8y} \, dy = 9810 \sqrt{8} \int_0^4 (4 y^{1/2} - y^{3/2}) \, dy$$
$$\int_0^4 (4 y^{1/2} - y^{3/2}) \, dy = \left[ \frac{8}{3} y^{3/2} - \frac{2}{5} y^{5/2} \right]_0^4 = \frac{8}{3}(8) - \frac{2}{5}(32) = \frac{64}{3} - \frac{64}{5} = \frac{128}{15} \approx 8.533333$$
$$F = 9810 \times 2.828427 \times 8.533333 = \mathbf{236,778.5\text{ Newtons}} = 236.78\text{ kN}$$

Program: `Y 8 {{key:×}} {{key:√x}} 4 Y {{key:-}} {{key:×}} 9810 {{key:×}}`. Limits: `0 {{key:ENTER}} 4`. Execute: `{{key:∫}} Y`.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}} 4` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | Gate depth interval $[0, 4]$ |
| 2 | `{{key:∫}} Y` | $0.0000$ | $0.0000$ | **$4.18 \times 10^{-10}$** | **$236778.4720$** | Hydrostatic Force in N |

The stack resolves to **$F = 236.78\text{ kN}$**.

---

### Problem 8.9: Center of Mass of Non-Uniform Density Rod
A rigid structural rod of length $L = 2.0\text{ m}$ has non-uniform linear mass density $\lambda(x) = 1.5 + 0.8 x^2\text{ kg/m}$.
Total Mass $M$ and first moment $M_x$ about $x = 0$:
$$M = \int_0^2 (1.5 + 0.8 x^2) \, dx = \left[ 1.5x + \frac{0.8}{3} x^3 \right]_0^2 = 3.0 + \frac{6.4}{3} = \frac{15.4}{3} \approx 5.133333\text{ kg}$$
$$M_x = \int_0^2 x (1.5 + 0.8 x^2) \, dx = \int_0^2 (1.5x + 0.8x^3) \, dx = \left[ 0.75 x^2 + 0.2 x^4 \right]_0^2 = 3.0 + 3.2 = 6.20\text{ kg}\cdot\text{m}$$
$$\bar{x} = \frac{M_x}{M} = \frac{6.20}{5.133333} = \frac{6.20 \times 3}{15.4} = \frac{93}{77} \approx \mathbf{1.207792\text{ meters}}$$

Programs:
- For $M$: `X {{key:x²}} 0.8 {{key:×}} 1.5 {{key:+}}`
- For $M_x$: `X {{key:x²}} 0.8 {{key:×}} 1.5 {{key:+}} X {{key:×}}`

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}} 2` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Integration limits $[0, 2]$ |
| 2 | `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$3.24 \times 10^{-11}$** | **$5.133333$** | Romberg evaluates rod mass $M$ (kg) |
| 3 | `{{key:STO}} A` | $0.0000$ | $0.0000$ | $3.24 \times 10^{-11}$ | $5.133333$ | Store total mass $M$ in Variable A |
| 4 | `0 {{key:ENTER}} 2` | $3.24 \times 10^{-11}$ | $5.133333$ | $0.0000$ | $2.0000$ | Reload integration limits $[0, 2]$ |
| 5 | `{{key:∫}} X` | $3.24 \times 10^{-11}$ | $5.133333$ | **$1.87 \times 10^{-11}$** | **$6.200000$** | Romberg evaluates first moment $M_x$ |
| 6 | `{{key:RCL}} A {{key:÷}}` | $5.133333$ | $5.133333$ | $1.87 \times 10^{-11}$ | **$1.207792$** | Centroid position $\bar{x} = M_x / M$ (meters) |

Register $X$ settles at **$\bar{x} = 1.207792\text{ meters}$**.

---

### Problem 8.10: Laminar Pipe Flow Volume Discharge (Poiseuille Law)
Fluid flows through a circular pipe of radius $R = 0.05\text{ m}$ ($50\text{ mm}$) with parabolic velocity profile $v(r) = v_{\max} (1 - r^2 / R^2)$, where centerline peak velocity $v_{\max} = 1.20\text{ m/s}$.
Total volume discharge $Q$ via surface integration of concentric cylindrical stream tubes:
$$Q = 2\pi \int_0^R v(r) r \, dr = 2\pi v_{\max} \int_0^R \left( r - \frac{r^3}{R^2} \right) dr = 2\pi(1.20) \left[ \frac{R^2}{2} - \frac{R^2}{4} \right] = \frac{1}{2} \pi R^2 v_{\max}$$
$$Q = 0.5 \times \pi \times (0.05^2) \times 1.20 = 0.5 \times \pi \times 0.0025 \times 1.20 = \mathbf{4.712389 \times 10^{-3}\text{ m}^3/\text{s}} = \mathbf{4.712389\text{ L/s}}$$

Program for integrand $2\pi r v(r)$: `R {{key:x²}} 0.0025 {{key:÷}} 1 {{key:x⇄y}} {{key:-}} 1.2 {{key:×}} R {{key:×}} 2 {{key:×}} {{key:π}} {{key:×}}`.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}} 0.05` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0500$ | Pipe radial integration limits $[0, R]$ |
| 2 | `{{key:∫}} R` | $0.0000$ | $0.0000$ | **$1.45 \times 10^{-12}$** | **$0.004712$** | Discharge $Q$ in $\text{m}^3/\text{s}$ |
| 3 | `1000 {{key:×}}` | $0.0000$ | $0.0000$ | $1.45 \times 10^{-12}$ | **$4.712389$** | Convert volumetric flow to Liters/second |

This confirms a final value of **$Q = 4.712389\text{ L/s}$**.

---

> **Thematic Arc II — Signal RMS Power, Blackbody Radiation & Non-Elementary Integrals (Problems 8.11–8.20):** Here adaptive Romberg quadrature shines on elliptic, Gaussian, and Planck integrals that possess no closed-form elementary antiderivative.

### Problem 8.11: RMS Value of Clipped Sinusoidal Voltage Waveform
A $60\text{ Hz}$ AC line voltage $v(t) = V_p \sin(\theta)$ with peak $V_p = 170.0\text{ V}$ is clipped by a metal-oxide varistor (MOV) clamp at $V_c = 0.80 V_p = 136.0\text{ V}$.
The clipping threshold angle occurs at $\sin \theta_c = 0.80 \implies \theta_c = \arcsin(0.80) \approx 0.927295\text{ rad}$.
By quarter-wave symmetry, the mean square value over $[0, \pi/2]$ is:
$$\langle v^2 \rangle = \frac{2}{\pi} \left[ \int_0^{\theta_c} (170 \sin \theta)^2 d\theta + \int_{\theta_c}^{\pi/2} 136^2 d\theta \right]$$
$$\int_0^{0.927295} 28,900 \sin^2 \theta \, d\theta = 28,900 \left[ \frac{\theta}{2} - \frac{\sin 2\theta}{4} \right]_0^{0.927295} = 28,900 [0.463648 - 0.240000] = 6,463.42\text{ V}^2\cdot\text{rad}$$
$$\int_{0.927295}^{\pi/2} 136^2 \, d\theta = 18,496 \left(\frac{\pi}{2} - 0.927295\right) = 18,496(0.643501) = 11,902.19\text{ V}^2\cdot\text{rad}$$
$$\langle v^2 \rangle = \frac{2}{\pi}(6,463.42 + 11,902.19) = \frac{2}{\pi}(18,365.61) = 11,691.88\text{ V}^2$$
$$V_{\text{rms}} = \sqrt{11,691.88} = \mathbf{108.1290\text{ Volts}}$$

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:RAD}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Radian mode engaged for trig calculus |
| 2 | `0 {{key:ENTER}} 0.927295` | $0.0000$ | $0.0000$ | $0.0000$ | $0.927295$ | Integration bounds $[0, \theta_c]$ |
| 3 | `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$3.12 \times 10^{-10}$** | **$6463.4190$** | Integral of $(170\sin\theta)^2$ over rising edge |
| 4 | `{{key:π}} 2 {{key:÷}} 0.927295 {{key:-}}` | $3.12 \times 10^{-10}$ | $3.12 \times 10^{-10}$ | $6463.4190$ | $0.643501$ | Clipped interval $(\pi/2 - \theta_c)$; rising integral stays in $Y$ |
| 5 | `136 {{key:x²}} {{key:×}}` | $3.12 \times 10^{-10}$ | $3.12 \times 10^{-10}$ | $6463.4190$ | **$11902.1945$** | Flat clamped plateau contribution |
| 6 | `{{key:+}}` | $3.12 \times 10^{-10}$ | $3.12 \times 10^{-10}$ | $3.12 \times 10^{-10}$ | **$18365.6135$** | Total quarter-cycle energy sum |
| 7 | `2 {{key:×}} {{key:π}} {{key:÷}} {{key:√x}}` | $3.12 \times 10^{-10}$ | $3.12 \times 10^{-10}$ | $3.12 \times 10^{-10}$ | **$108.1290$** | Mean square normalized and root taken |

The calculation yields **$V_{\text{rms}} = 108.1290\text{ Volts}$**.

---

### Problem 8.12: Polytropic Gas Expansion Work: $P V^{1.4} = C$
An ideal diatomic gas expands reversibly in an insulated cylinder from $V_1 = 0.02\text{ m}^3$ to $V_2 = 0.08\text{ m}^3$. Initial chamber pressure $P_1 = 600.0\text{ kPa} = 600,000\text{ Pa}$. Polytropic index $n = 1.4$.
State constant $C = P_1 V_1^{1.4} = 600,000 \times (0.02)^{1.4} \approx 2,492.357\text{ Pa}\cdot\text{m}^{4.2}$.
Boundary expansion work $W = \int_{V_1}^{V_2} P(V) \, dV$:
$$W = C \int_{0.02}^{0.08} V^{-1.4} \, dV = \frac{P_1 V_1 \left[ 1 - (V_1/V_2)^{0.4} \right]}{0.4} = \frac{12,000 \left[ 1 - (0.25)^{0.4} \right]}{0.4}$$
$$(0.25)^{0.4} \approx 0.57434918 \implies 1 - 0.57434918 = 0.42565082$$
$$W = \frac{12,000 \times 0.42565082}{0.4} = 30,000 \times 0.42565082 = \mathbf{12,769.52\text{ Joules}} = \mathbf{12.7695\text{ kJ}}$$

Program the polytropic integrand `V 1.4 {{key:+/-}} {{key:yˣ}} 2492.357 {{key:×}}` into `{{key:EQN}}`. Enter the cylinder volume limits `0.02 {{key:ENTER}} 0.08` $(T: 0.0000, Z: 0.0000, Y: 0.0200, X: 0.0800)$, and press `{{key:∫}} V` $(T: 0.0000, Z: 0.0000, Y: 2.18\times 10^{-10}, X: 12769.5248)$. Romberg quadrature integrates the non-linear pressure curve, placing error bound $2.18 \times 10^{-10}$ in Register $Y$ and boundary work $12,769.5248\text{ J}$ in Register $X$. Dividing by $1000$ (`1000 {{key:÷}}`) scales the result to kilojoules $(T: 0.0000, Z: 0.0000, Y: 2.18\times 10^{-10}, X: 12.7695)$.

---

### Problem 8.13: Arc Length of Catenary Power Transmission Line
High-voltage transmission conductor suspended between two transmission pylons separated by span $2d = 200.0\text{ m}$ ($x \in [-100, +100]\text{ m}$).
Conductor catenary shape profile: $y(x) = a \cosh(x / a)$ with catenary parameter $a = 800.0\text{ m}$.
Arc length integral $L = \int_{-100}^{100} \sqrt{1 + [y'(x)]^2} \, dx$:
$$\sqrt{1 + \sinh^2(x/800)} = \cosh(x / 800)$$
$$L = \int_{-100}^{100} \cosh(x / 800) \, dx = 2 \times 800 \sinh(100 / 800) = 1600 \sinh(0.125) = 1600(0.12532561) = \mathbf{200.5210\text{ meters}}$$
Mid-span cable sag $\Delta y = y(100) - y(0) = 800[\cosh(0.125) - 1] = 800[1.0078229 - 1] = \mathbf{6.2583\text{ meters}}$.

Program for integrand: `X 800 {{key:÷}} {{key:HYP}} {{key:COS}}`.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `100 {{key:+/-}} {{key:ENTER}} 100` | $0.0000$ | $0.0000$ | $-100.0000$ | $100.0000$ | Tower span interval $[-100, +100]$ |
| 2 | `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$8.55 \times 10^{-11}$** | **$200.5210$** | Conductor total arc length (meters) |
| 3 | `100 {{key:ENTER}} 800 {{key:÷}} {{key:HYP}} {{key:COS}}` | $8.55 \times 10^{-11}$ | $8.55 \times 10^{-11}$ | $200.5210$ | $1.007823$ | Dimensionless catenary height ratio |
| 4 | `1 {{key:-}} 800 {{key:×}}` | $8.55 \times 10^{-11}$ | $8.55 \times 10^{-11}$ | $200.5210$ | **$6.2583$** | Conductor mid-span sag $\Delta y$ (meters) |

Register $X$ settles at Conductor length **$L = 200.5210\text{ m}$**, Sag **$\Delta y = 6.258\text{ m}$**.

---

### Problem 8.14: Surface Area of Paraboloid Radar Dish of Revolution
A parabolic satellite reflector dish is generated by revolving $y = 0.25 x^2$ about the vertical $y$-axis from center $x = 0$ to outer rim radius $R = 2.0\text{ m}$.
Surface area of revolution formula:
$$A = 2\pi \int_0^R x \sqrt{1 + [y'(x)]^2} \, dx = 2\pi \int_0^2 x \sqrt{1 + (0.5 x)^2} \, dx = 2\pi \int_0^2 x \sqrt{1 + 0.25 x^2} \, dx$$
Analytical evaluation via $u = 1 + 0.25 x^2, du = 0.5 x dx \implies x dx = 2 du$:
$$A = 4\pi \int_1^2 u^{1/2} \, du = \frac{8\pi}{3} \left[ u^{3/2} \right]_1^2 = \frac{8\pi}{3} (2\sqrt{2} - 1) = \frac{8\pi}{3}(1.8284271) \approx \mathbf{15.317764\text{ m}^2}$$

Program the integrand `X 0.5 {{key:×}} {{key:x²}} 1 {{key:+}} {{key:√x}} X {{key:×}} 2 {{key:×}} {{key:π}} {{key:×}}` into `{{key:EQN}}`. Enter the reflector radial limits `0 {{key:ENTER}} 2` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 2.0000)$, and press `{{key:∫}} X`. The Romberg engine integrates the surface of revolution, returning error bound $2.14 \times 10^{-10}$ in Register $Y$ and total surface area $\mathbf{15.317764\text{ m}^2}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 2.14\times 10^{-10}, X: 15.317764)$, confirming Reflector surface area **$A = 15.3178\text{ m}^2$**.

---

### Problem 8.15: Thermal Heat Conduction Across Temperature-Dependent Wall
High-temperature furnace wall of thickness $L = 0.20\text{ m}$ and cross-sectional area $A = 10.0\text{ m}^2$.
Material thermal conductivity is temperature-dependent: $k(T) = 0.50 + 0.002 T\text{ W/(m}\cdot\text{K)}$.
Internal hot face $T_1 = 800.0\text{ K}$, exterior cold face $T_2 = 300.0\text{ K}$.
One-dimensional steady heat flow rate $q$ via Fourier's Law:
$$q = \frac{A}{L} \int_{300}^{800} k(T) \, dT = \frac{10.0}{0.20} \int_{300}^{800} (0.50 + 0.002 T) \, dT = 50.0 \left[ 0.50 T + 0.001 T^2 \right]_{300}^{800}$$
$$q = 50.0 \left[ 0.50(500) + 0.001(800^2 - 300^2) \right] = 50.0 [250 + 0.001(640,000 - 90,000)] = 50.0 [250 + 550]$$
$$q = 50.0 \times 800 = \mathbf{40,000.0\text{ Watts}} = \mathbf{40.000\text{ kW}}$$

Program the heat conduction integrand `T 0.002 {{key:×}} 0.5 {{key:+}} 50 {{key:×}}` into `{{key:EQN}}`. Load the boundary temperatures `300 {{key:ENTER}} 800` $(T: 0.0000, Z: 25.0000, Y: 300.0000, X: 800.0000)$, and press `{{key:∫}} T` $(T: 0.0000, Z: 25.0000, Y: 0.0000, X: 40000.0000)$. Because the conductivity varies linearly with temperature, Romberg quadrature achieves machine-precision convergence with error bound $0.0000$ in $Y$ and heat flux $40,000.0\text{ W}$ in $X$. Dividing by $1000$ (`1000 {{key:÷}}`) scales the flux to kilowatts $(T: 25.0000, Z: 25.0000, Y: 0.0000, X: 40.0000)$, confirming Heat conduction rate **$q = 40.000\text{ kW}$**.

---

### Problem 8.16: Fresnel Sine Integral in Diffraction Optics ($S(x)$)
Knife-edge Fresnel diffraction intensity involves the canonical Fresnel sine integral:
$$S(x) = \int_0^x \sin\left(\frac{\pi}{2} t^2\right) dt$$
Evaluate $S(2.0)$ at normalized aperture coordinate $x = 2.0$.

Ensure radian mode is engaged (`{{key:RAD}}`). Program the integrand `T {{key:x²}} {{key:π}} {{key:×}} 2 {{key:÷}} {{key:SIN}}` into `{{key:EQN}}`. Push integration limits `0 {{key:ENTER}} 2` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 2.0000)$ and press `{{key:∫}} T`. Romberg extrapolation integrates the oscillatory sine profile smoothly, yielding certified error bound $1.48 \times 10^{-10}$ in Register $Y$ and the Fresnel sine value $S(2.0) = \mathbf{0.343416}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 1.48\times 10^{-10}, X: 0.343416)$.

---

### Problem 8.17: Fresnel Cosine Integral ($C(x)$)
The companion Fresnel cosine integral describes orthogonal diffraction amplitude:
$$C(x) = \int_0^x \cos\left(\frac{\pi}{2} t^2\right) dt$$
Evaluate $C(2.0)$ at $x = 2.0$. Together with $S(2.0) = 0.343416$, this defines the Cornu spiral phasor position:
$$r = \sqrt{C^2(2) + S^2(2)} = \sqrt{0.488253^2 + 0.343416^2} = \sqrt{0.238391 + 0.117935} = \sqrt{0.356326} \approx \mathbf{0.596930}$$

In radian mode (`{{key:RAD}}`), program the companion cosine integrand `T {{key:x²}} {{key:π}} {{key:×}} 2 {{key:÷}} {{key:COS}}` into `{{key:EQN}}`. Set integration limits `0 {{key:ENTER}} 2` $(T: 0.0000, Z: 1.0000, Y: 0.0000, X: 2.0000)$ and press `{{key:∫}} T` $(T: 0.0000, Z: 1.0000, Y: 2.22\times 10^{-10}, X: 0.488253)$. The Romberg engine evaluates the Fresnel cosine integral, depositing error bound $2.22 \times 10^{-10}$ into $Y$ and $C(2.0) = 0.488253$ into $X$. Squaring, adding the previously stored $S(2.0)^2 = 0.343416^2$, and taking the square root (`{{key:x²}} 0.343416 {{key:x²}} {{key:+}} {{key:√x}}`) yields the Cornu spiral phasor length $\mathbf{0.596930}$ $(T: 1.0000, Z: 1.0000, Y: 2.22\times 10^{-10}, X: 0.596930)$.

---

### Problem 8.18: Gravitational Attraction of Thin Rod on End Particle
A slender spacecraft boom of length $L = 5.0\text{ m}$ and uniform mass $M = 100.0\text{ kg}$ is positioned along the $x$-axis from $x = 1.0\text{ m}$ to $x = 6.0\text{ m}$.
A sensor payload of mass $m = 2.0\text{ kg}$ is positioned at the origin $x = 0$.
Linear mass density $\lambda = M/L = 100.0 / 5.0 = 20.0\text{ kg/m}$.
Gravitational constant $G = 6.6743 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2$.
Newtonian attraction force $F$:
$$F = G m \lambda \int_1^6 \frac{dx}{x^2} = (6.6743 \times 10^{-11}) \times 2.0 \times 20.0 \left[ -\frac{1}{x} \right]_1^6 = 2.66972 \times 10^{-9} \left[ 1 - \frac{1}{6} \right]$$
$$F = 2.66972 \times 10^{-9} \times \frac{5}{6} = \mathbf{2.224767 \times 10^{-9}\text{ Newtons}} = \mathbf{2.224767\text{ nN}}$$

Program the gravitational integrand `X {{key:x²}} {{key:1/x}} 2.66972 {{key:E}} 9 {{key:+/-}} {{key:×}}` into `{{key:EQN}}`. Enter the rod distance limits `1 {{key:ENTER}} 6` $(T: 0.0000, Z: 0.0000, Y: 1.0000, X: 6.0000)$, and press `{{key:∫}} X` $(T: 0.0000, Z: 0.0000, Y: 1.15\times 10^{-16}, X: 2.224767\times 10^{-9})$. Romberg quadrature integrates the inverse-square attraction, yielding error bound $1.15 \times 10^{-16}$ in Register $Y$ and total force $2.224767 \times 10^{-9}\text{ N}$ in Register $X$. Multiplying by $10^9$ (`1 {{key:E}} 9 {{key:×}}`) displays the force in nanonewtons $(T: 0.0000, Z: 0.0000, Y: 1.15\times 10^{-16}, X: 2.224767)$.

---

### Problem 8.19: Fourier Series 1st Harmonic Sine Coefficient ($b_1$)
An odd square wave of fundamental period $2\pi$ has value $+1$ on $(0, \pi)$ and $-1$ on $(-\pi, 0)$.
The fundamental Fourier harmonic sine coefficient $b_1$ is:
$$b_1 = \frac{2}{\pi} \int_0^\pi \sin(x) \, dx = \frac{2}{\pi} \left[ -\cos(x) \right]_0^\pi = \frac{2}{\pi} (1 - (-1)) = \frac{4}{\pi} \approx \mathbf{1.273240}$$

With radian mode engaged (`{{key:RAD}}`), program the harmonic integrand `X {{key:SIN}}` into `{{key:EQN}}`. Load the half-period interval `0 {{key:π}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 3.141593)$ and press `{{key:∫}} X` $(T: 0.0000, Z: 0.0000, Y: 1.82\times 10^{-11}, X: 2.000000)$. The Romberg engine integrates the sine half-wave to error bound $1.82 \times 10^{-11}$ in $Y$ and definite integral $2.000000$ in $X$. Normalizing by the Fourier factor (`2 {{key:×}} {{key:π}} {{key:÷}}`) computes the fundamental amplitude $b_1 = 4/\pi \approx \mathbf{1.273240}$ $(T: 0.0000, Z: 0.0000, Y: 1.82\times 10^{-11}, X: 1.273240)$ ($4/\pi$ peak amplitude).

---

### Problem 8.20: Centrifugal Governor Flyweight Kinetic Energy
A mechanical flyball governor rotor has radial displacement profile $r(\theta) = 0.15 + 0.05 \sin(2\theta)\text{ meters}$ driven at constant angular rate $\omega = 40.0\text{ rad/s}$.
At rotor angle $\theta = \pi/6\text{ rad}$ ($30^\circ$), evaluate radial velocity $\dot{r} = \omega \frac{dr}{d\theta}$ via numerical differentiation, and find the total kinetic energy of a $m = 4.0\text{ kg}$ flyweight:
$$\frac{dr}{d\theta} = 2(0.05) \cos(2\theta) = 0.10 \cos\left(\frac{\pi}{3}\right) = 0.050\text{ m/rad}$$
$$\dot{r} = 40.0 \times 0.050 = 2.00\text{ m/s}$$
$$r\left(\frac{\pi}{6}\right) = 0.15 + 0.05 \sin\left(\frac{\pi}{3}\right) = 0.15 + 0.043301 = 0.193301\text{ m} \implies v_\theta = r \omega = 7.732051\text{ m/s}$$
$$v^2 = \dot{r}^2 + v_\theta^2 = 2.0^2 + (7.732051)^2 = 4.00 + 59.7846 = 63.7846\text{ m}^2/\text{s}^2$$
$$E_k = \frac{1}{2} m v^2 = \frac{1}{2}(4.0)(63.7846) = \mathbf{127.5692\text{ Joules}}$$

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:RAD}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Verify radian mode |
| 2 | `{{key:π}} 6 {{key:÷}} {{key:STO}} A` | $0.0000$ | $0.0000$ | $0.0000$ | $0.523599$ | Angle $\theta = \pi/6$ stored in Var A |
| 3 | `2 {{key:×}} {{key:COS}} 0.1 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.050000$** | Radial rate $dr/d\theta = 0.10\cos(2\theta)$ |
| 4 | `40 {{key:×}} {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$4.000000$** | Radial velocity squared $\dot{r}^2 = (2.0)^2$ |
| 5 | `{{key:RCL}} A 2 {{key:×}} {{key:SIN}} 0.05 {{key:×}} 0.15 {{key:+}} 40 {{key:×}}` | $0.0000$ | $0.0000$ | $4.000000$ | **$7.732051$** | Tangential speed $v_\theta = r \omega$; $\dot{r}^2$ stays in $Y$ |
| 6 | `{{key:x²}} {{key:+}} 2 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$127.569226$** | Kinetic energy $0.5 \times 4 \times (\dot{r}^2 + v_\theta^2)$ (J) |

The stack resolves to Flyweight kinetic energy **$E_k = 127.5692\text{ Joules}$**.

---

> **Thematic Arc III — Reactor Flux Profiles, Central-Difference Derivatives & Sensitivity (Problems 8.21–8.30):** Pairing `∫f` with `d/dx` to evaluate radial power peaking, instantaneous rates of change, and local Taylor linearizations.

### Problem 8.21: Nuclear Fission Core Radial Power Density Integral
A heavy-water moderated reactor core of radius $R = 1.80\text{ m}$ and height $H = 3.60\text{ m}$ exhibits zero-order Bessel radial thermal flux $\phi(r) = \phi_0 J_0(2.405 r / R)$ with center power density $q_0''' = 120.0\text{ MW/m}^3$.
Core cross-sectional thermal output $P'_{\text{th}} = \int_0^R 2\pi r q_0''' J_0(2.405 r / R) \, dr$:
Using $\int_0^R r J_0(\alpha r) dr = \frac{R}{\alpha} J_1(\alpha R) = \frac{1.80^2}{2.405} J_1(2.405) \approx \frac{3.24}{2.405}(0.519147) \approx 0.699411\text{ m}^2$:
$$P'_{\text{th}} = 2\pi(120.0)(0.699411) \approx 527.350\text{ MW/m}$$
With fundamental axial cosine chopping factor $2/\pi \approx 0.636620$, total thermal power output is:
$$P_{\text{th}} = P'_{\text{th}} \times H \times \frac{2}{\pi} = 527.350 \times 3.60 \times 0.636620 \approx \mathbf{1,208.587\text{ MW}}_{\text{th}}$$

Using the 2-term Horner Bessel series $J_0(u) \approx 1 - \frac{1}{4}u^2 + \frac{1}{64}u^4 = u^2(\frac{1}{64}u^2 - \frac{1}{4}) + 1$ with $u = 1.3361 R$, program the radial integrand `R 1.3361 {{key:×}} {{key:x²}} {{key:ENTER}} {{key:ENTER}} 0.015625 {{key:×}} 0.25 {{key:-}} {{key:×}} 1 {{key:+}} R {{key:×}} 2 {{key:×}} {{key:π}} {{key:×}}` into `{{key:EQN}}`. Push core radial limits `0 {{key:ENTER}} 1.8` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.8000)$ and press `{{key:∫}} R` $(T: 0.0000, Z: 0.0000, Y: 1.65\times 10^{-10}, X: 4.394539)$. Romberg quadrature yields error bound $1.65 \times 10^{-10}$ in Register $Y$ and integrated geometric factor $4.394539$ in Register $X$. Scaling by axial height and center power density (`120 {{key:×}} 3.6 {{key:×}} 2 {{key:×}} {{key:π}} {{key:÷}}`) computes total thermal reactor output $\mathbf{1,208.5866\text{ MW}_{\text{th}}}$ $(T: 0.0000, Z: 0.0000, Y: 1.65\times 10^{-10}, X: 1208.5866)$, confirming Total reactor power **$P_{\text{th}} = 1,208.59\text{ MW}_{\text{th}}$**.

---

### Problem 8.22: Sound Exposure Level (SEL) from Transient Flyover Noise
An aircraft flyover noise pulse at an airfield boundary is modeled by acoustic pressure $p(t) = p_0 e^{-t^2 / 20}\text{ Pa}$ with peak pressure $p_0 = 2.00\text{ Pa}$ over $t \in [-15, +15]\text{ s}$.
Reference acoustic pressure $p_{\text{ref}} = 20\,\mu\text{Pa} = 2.0 \times 10^{-5}\text{ Pa}$, reference time $t_0 = 1.0\text{ s}$.
Sound exposure integral $E = \int_{-15}^{15} p^2(t) \, dt = \int_{-15}^{15} 4.0 e^{-t^2 / 10} \, dt$:
$$E \approx 4.0 \sqrt{10\pi} = 4.0 \times 5.604991 = \mathbf{22.41996\text{ Pa}^2\cdot\text{s}}$$
$$\text{SEL} = 10 \log_{10}\left( \frac{E}{p_{\text{ref}}^2 \cdot t_0} \right) = 10 \log_{10}\left( \frac{22.41996}{4.0 \times 10^{-10}} \right) = 10 \log_{10}(5.604991 \times 10^{10}) = \mathbf{107.4857\text{ dBA}}$$

Program the sound power integrand `T {{key:x²}} 10 {{key:÷}} {{key:+/-}} {{key:eˣ}} 4 {{key:×}}` into `{{key:EQN}}`. Set observation limits `15 {{key:+/-}} {{key:ENTER}} 15` $(T: 0.0000, Z: 4.0000, Y: -15.0000, X: 15.0000)$ and press `{{key:∫}} T` $(T: 0.0000, Z: 4.0000, Y: 4.88\times 10^{-11}, X: 22.419964)$. The Romberg engine integrates the flyover acoustic pulse to error bound $4.88 \times 10^{-11}$ in $Y$ and total exposure $E = 22.419964\text{ Pa}^2\cdot\text{s}$ in $X$. Dividing by the reference power and converting to decibels (`4 {{key:E}} 10 {{key:+/-}} {{key:÷}} {{key:LOG}} 10 {{key:×}}`) delivers the certified Sound Exposure Level $\mathbf{107.4857\text{ dBA}}$ $(T: 4.0000, Z: 4.0000, Y: 4.88\times 10^{-11}, X: 107.485743)$, confirming **$\text{SEL} = 107.49\text{ dBA}$**.

---

### Problem 8.23: Aerodynamic Circulation Line Integral (Kutta-Joukowski Lift)
Aerodynamic circulation bound vortex line integral around a transonic wing profile:
$$\Gamma = \oint \vec{v} \cdot d\vec{s} = 45.0\text{ m}^2/\text{s}$$
Freestream airspeed $V_\infty = 60.0\text{ m/s}$, air density $\rho_\infty = 1.225\text{ kg/m}^3$, wing span $b = 12.0\text{ m}$.
Kutta-Joukowski lift per unit span $L'$ and total wing lift $L$:
$$L' = \rho_\infty V_\infty \Gamma = 1.225 \times 60.0 \times 45.0 = \mathbf{3,307.50\text{ N/m}}$$
$$L = L' \times b = 3,307.50 \times 12.0 = \mathbf{39,690.0\text{ Newtons}} = \mathbf{39.69\text{ kN}}$$
Equivalent sustained aircraft mass: $M = L / g = 39,690 / 9.80665 \approx \mathbf{4,047.24\text{ kg}} \approx 4.05\text{ metric tonnes}$.

Execute the Kutta-Joukowski lift product directly on the stack: evaluate freestream momentum `1.225 {{key:ENTER}} 60 {{key:×}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 73.5000)$, multiply by circulation `45 {{key:×}}` to obtain unit span lift $L' = 3,307.50\text{ N/m}$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 3307.5000)$, multiply by wingspan `12 {{key:×}}` for total lift $L = 39,690.0\text{ N}$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 39690.0000)$, and divide by $g$ (`9.80665 {{key:÷}} 1000 {{key:÷}}`) to find sustained mass $\mathbf{4.04724\text{ tonnes}}$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 4.04724)$, confirming Total lift **$L = 39.69\text{ kN}$** ($4.05\text{ tonnes}$).

---

### Problem 8.24: Damped Harmonic Oscillator Energy Dissipated Per Cycle
Viscous dashpot damper force $F_d = c \dot{x}$ with damping coefficient $c = 15.0\text{ N}\cdot\text{s/m}$.
Natural frequency $\omega = 20.0\text{ rad/s}$, harmonic displacement amplitude $X_0 = 0.020\text{ m}$ ($20\text{ mm}$).
Velocity $v(t) = -\omega X_0 \sin(\omega t) = -0.40 \sin(20 t)\text{ m/s}$.
Oscillation period $T = \frac{2\pi}{\omega} = \frac{\pi}{10} \approx 0.314159\text{ s}$.
Energy dissipated per steady-state cycle:
$$\Delta E = \int_0^T c v^2(t) \, dt = 15.0 \int_0^{\pi/10} [ -0.40 \sin(20 t) ]^2 dt = 2.40 \int_0^{\pi/10} \sin^2(20 t) \, dt$$
$$\Delta E = 2.40 \times \left( \frac{T}{2} \right) = 2.40 \times \frac{\pi}{20} = 0.12 \pi \approx \mathbf{0.376991\text{ Joules}}$$

In radian mode (`{{key:RAD}}`), program the dissipation integrand `T 20 {{key:×}} {{key:SIN}} {{key:x²}} 2.4 {{key:×}}` into `{{key:EQN}}`. Enter cycle duration limits `0 {{key:π}} 10 {{key:÷}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.314159)$ and press `{{key:∫}} T`. The Romberg engine integrates the harmonic damping curve, yielding error bound $1.12 \times 10^{-11}$ in Register $Y$ and dissipated energy per cycle $\mathbf{0.376991\text{ Joules}}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 1.12\times 10^{-11}, X: 0.376991)$, confirming Energy loss per cycle **$\Delta E = 0.3770\text{ Joules}$**.

---

### Problem 8.25: Continuous Present Value of Perpetual Cash Flow Stream
Continuous discount rate $r = 0.06$, cash flow intensity $C(t) = 50,000 e^{-0.02 t}$:
$$PV = \int_0^{30} 50000 e^{-0.08 t} \, dt = \frac{50000}{0.08} [1 - e^{-2.4}] = 625,000 [1 - 0.090718] = \mathbf{\$568,301.25}$$

> ***The LASTX Dual-Branch Trick & Continuous Discounting*** — Evaluate exponential decay factor $e^{-rt}$, subtract from unity via `{{key:x⇄y}}`, and scale by annuity intensity directly within the operational stack levels {{cite:hp15c1982}}.

Program the discounted revenue flow `T 0.08 {{key:×}} {{key:+/-}} {{key:eˣ}} 50000 {{key:×}}` into `{{key:EQN}}`. Push interval bounds `0 {{key:ENTER}} 30` $(T: 0.0000, Z: 50000.0000, Y: 0.0000, X: 30.0000)$ and press `{{key:∫}} T`. Romberg quadrature integrates the 30-year exponential stream, placing error bound $4.12 \times 10^{-11}$ in Register $Y$ and continuous present value $\mathbf{\$568,301.25}$ in Register $X$ $(T: 0.0000, Z: 50000.0000, Y: 4.12\times 10^{-11}, X: 568301.25)$.

---

### Problem 8.26: Second Moment of Area of Structural I-Beam Web ($I_{xx}$)
For a vertical steel web of height $h = 300\text{ mm}$ ($y \in [-150, +150]\text{ mm}$) and thickness $t = 10\text{ mm}$, the flexural bending stiffness depends on the second moment of area $I_{xx}$:
$$I_{xx} = \int_{-150}^{150} t y^2 \, dy = 10 \left[ \frac{y^3}{3} \right]_{-150}^{150} = \frac{20}{3}(3,375,000) = \mathbf{22,500,000\text{ mm}^4} = 2.25 \times 10^7\text{ mm}^4$$

Program the area moment integrand `Y {{key:x²}} 10 {{key:×}}` into `{{key:EQN}}`. Load the beam web span limits `150 {{key:+/-}} {{key:ENTER}} 150` $(T: 0.0000, Z: 0.0000, Y: -150.0000, X: 150.0000)$, then press `{{key:∫}} Y`. Romberg integration evaluates the second moment of area, returning error bound $1.85 \times 10^{-10}$ in Register $Y$ and bending moment of inertia $I_{xx} = \mathbf{22,500,000.0\text{ mm}^4}$ ($2.25 \times 10^7\text{ mm}^4$) in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 1.85\times 10^{-10}, X: 22500000.0)$.

---

### Problem 8.27: Radar Cross Section (RCS) of Flat Conducting Plate
Physical-optics surface phase integration over a square flat plate of side $a = 0.50\text{ m}$ (area $A = 0.25\text{ m}^2$) at X-band radar wavelength $\lambda = 0.03\text{ m}$ ($10\text{ GHz}$) yields the peak specular Radar Cross Section:
$$\sigma_{\max} = \frac{4\pi A^2}{\lambda^2} = \frac{4\pi (0.25^2)}{0.0009} = \frac{4\pi(0.0625)}{0.0009} \approx \mathbf{872.66\text{ m}^2} \quad (29.41\text{ dBsm})$$

Evaluate the radar cross section directly on the stack: key `4 {{key:π}} {{key:×}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 12.5664)$, multiply by area squared `0.25 {{key:x²}} {{key:×}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.7854)$, and divide by wavelength squared `0.03 {{key:x²}} {{key:÷}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 872.6646)$, delivering the peak specular RCS $\sigma_{\max} = \mathbf{872.6646\text{ m}^2}$ ($29.41\text{ dBsm}$).

---

### Problem 8.28: Thermal Expansion Clearance of Cryogenic Propellant Line
When a 304 stainless-steel LOX/LN2 transfer line of length $L = 12.0\text{ m}$ is chilled from ambient $293\text{ K}$ down to liquid nitrogen boiling temperature ($77\text{ K}$), the thermal expansion coefficient $\alpha(T)$ varies non-linearly with temperature:
$$\Delta L = L \int_{293}^{77} \alpha(T) \, dT \approx 12.0 \times (-0.00285) = \mathbf{-34.2\text{ mm}}\text{ (axial contraction)}$$
**Engineering Insight:** Reversing the integration limits ($a = 293$ in $Y$, $b = 77$ in $X$) automatically produces the negative sign indicating contraction, reminding bellows designers to provide at least $35\text{ mm}$ of axial expansion-joint travel.

> ***The Inside-Out Integral & Cryogenic Clearance Pipeline*** — Arm the stack with initial and cryogenic terminal temperatures, evaluate polynomial contraction directly in the stack, and scale by line length without register allocation {{cite:hp15c1982}}.

Arm the stack with cryogenic temperature ($77\text{ K}$) and subtract ambient ($293\text{ K}$): `77 {{key:ENTER}} 293 {{key:-}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: -216.0000)$, establishing contraction direction. Scale by the mean secant thermal contraction coefficient `13.1944 {{key:E}} 6 {{key:+/-}} {{key:×}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: -0.002850)$, multiply by line length `12.0 {{key:×}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: -0.034200)$, and convert to millimeters `1000 {{key:×}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: -34.2000)$. The net axial contraction $\Delta L = \mathbf{-34.20\text{ mm}}$ confirms bellows expansion travel without intermediate transcription.

---

### Problem 8.29: Relativistic Proper-Time Velocity Integration
A deep-space probe accelerating at constant proper acceleration $g = 9.81\text{ m/s}^2$ for proper shipboard time $\tau = 1.0\text{ year}$ accumulates Earth coordinate time via the hyperbolic integral:
$$t = \int_0^\tau \cosh\left(\frac{g \tau'}{c}\right) d\tau' = \frac{c}{g} \sinh\left(\frac{g \tau}{c}\right) \implies \mathbf{t = 1.19\text{ years}}$$

Evaluate the dimensionless rapidity $\eta = g\tau/c$ on the stack: `9.81 {{key:ENTER}} 31557600 {{key:×}} 299792458 {{key:÷}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.032650)$. Compute hyperbolic sine `{{key:HYP}} {{key:SIN}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.226215)$, and divide by rapidity via `{{key:LASTX}} {{key:÷}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.1874)$, resolving accumulated Earth coordinate time $t = \mathbf{1.19\text{ years}}$ directly without manual exponential expansion.

---

### Problem 8.30: Planetary Atmospheric Jeans Escape Flux
Integrating the Maxwell-Boltzmann velocity distribution above a planet's escape velocity $v_{\text{esc}}$ (with exobase density $n_0 = 1.0 \times 10^{13}\text{ m}^{-3}$, thermal speed $v_{\text{th}} = 6,356.7\text{ m/s}$, and Jeans parameter $\lambda = (v_{\text{esc}}/v_{\text{th}})^2 = 9.50$) yields the outward molecular escape flux at the exobase:
$$F_J = \frac{n_0 v_{\text{th}}}{2\sqrt{\pi}} (1 + \lambda) e^{-\lambda} = \left(1.7932 \times 10^{16}\right)(10.50) e^{-9.50} \approx \mathbf{1.42 \times 10^{12}\text{ molecules/(m}^2\cdot\text{s)}}$$

Evaluate the Jeans escape tail factor $(1 + \lambda)e^{-\lambda}$ at $\lambda = 9.50$ from the inside out: key `9.5 {{key:+/-}} {{key:eˣ}} 10.5 {{key:×}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.000786)$, multiply by thermal flux density $n_0 v_{\text{th}} = 6.3567 \times 10^{16}$ (`6.3567 {{key:E}} 16 {{key:×}}`), and divide by $2\sqrt{\pi}$ (`{{key:π}} {{key:√x}} 2 {{key:×}} {{key:÷}}`), yielding outward Jeans escape flux $F_J \approx \mathbf{1.42 \times 10^{12}\text{ molecules/(m}^2\cdot\text{s)}}$.
**Normalized Exponential Integral Check ($\int_0^2 e^x dx = e^2 - 1$):** Load $x = 2$, press `{{key:eˣ}}` ($7.389056$), and subtract unity (`{{res:sc32_08_calc_06:keys}}`) $\implies \mathbf{{{res:sc32_08_calc_06:value}}}$.

---

> **Thematic Arc IV — Nonlinear Field Energy, Arc Lengths & Quadrature Sprints (Problems 8.31–8.40):** The final ten problems integrate nonlinear constitutive laws, parabolic cable lengths, and coupled differential-integral checks.

### Problem 8.31: Capacitive Energy Storage in a Non-Linear Ferroelectric Dielectric
High-density ceramic capacitors exhibit voltage-dependent capacitance decay $C(V) = C_0 (1 - \alpha V^2)$ with $C_0 = 10\,\mu\text{F}$ and $\alpha = 10^{-6}\text{ V}^{-2}$. Integrating stored energy $dW = C(V) V dV$ from $0$ to $500\text{ V}$:
$$W = \int_0^{500} C_0 (V - \alpha V^3) \, dV = C_0 \left[ \frac{V^2}{2} - \frac{\alpha V^4}{4} \right]_0^{500} = 10^{-5} [125,000 - 15,625] = \mathbf{1.09375\text{ Joules}}$$
**Engineering Insight:** A naive linear $W = \frac{1}{2} C_0 V^2$ assumption overestimates stored pulse energy by $12.5\%$ ($1.25\text{ J}$ vs. $1.09375\text{ J}$).

> ***The Horner Polynomial Stream & Non-Linear Dielectric Energy*** — Integrate non-linear varactor charging energy $\int C_0(V - \alpha V^3) dV$ directly through the operational stack without parenthesis nesting {{cite:horowitz2015,hp15c1982}}.

Evaluate the linear potential energy factor `500 {{key:x²}} 2 {{key:÷}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 125000.0)$. Compute the dielectric saturation penalty `500 {{key:ENTER}} 4 {{key:yˣ}} 1 {{key:E}} 6 {{key:+/-}} {{key:×}} 4 {{key:÷}}` $(T: 0.0000, Z: 0.0000, Y: 125000.0, X: 15625.0)$, subtract `{{key:-}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 109375.0)$, and scale by base capacitance `10 {{key:E}} 6 {{key:+/-}} {{key:×}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.0938)$, obtaining the true delivered pulse energy $W = \mathbf{1.09375\text{ Joules}}$.

---

### Problem 8.32: Torsional Rigidity of an Elliptical Shaft (Saint-Venant Warping Integral)
Integrating shear stress over an elliptical shaft cross-section with semiaxes $a = 40\text{ mm}$ and $b = 25\text{ mm}$ yields the effective torsional constant $J$:
$$J = \frac{\pi a^3 b^3}{a^2 + b^2} = \frac{\pi (64,000)(15,625)}{1,600 + 625} = \frac{\pi \times 10^9}{2,225} \approx \mathbf{1,411,952\text{ mm}^4}$$

Evaluate the numerator product `40 {{key:ENTER}} 3 {{key:yˣ}} 25 {{key:ENTER}} 3 {{key:yˣ}} {{key:×}} {{key:π}} {{key:×}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 3.1416 \times 10^9)$. Compute denominator $a^2 + b^2$ and divide: `40 {{key:x²}} 25 {{key:x²}} {{key:+}} {{key:÷}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1411951.76)$, delivering torsional rigidity constant $J \approx \mathbf{1,411,952\text{ mm}^4}$.

---

### Problem 8.33: Second-Order Chemical Batch Reactor Residence Time
For an isothermal second-order reaction ($-r_A = k C_{A0}^2 (1-x)^2$) with characteristic rate product $k C_{A0} = \frac{1}{15}\text{ min}^{-1}$ ($0.06667\text{ min}^{-1}$), integrating the design equation from conversion $x = 0$ to $X = 0.75$ gives the required batch residence time:
$$t = \frac{1}{k C_{A0}} \int_0^{0.75} \frac{dx}{(1-x)^2} = 15.0 \left[ \frac{X}{1-X} \right]_{X=0.75} = 15.0 \times \frac{0.75}{0.25} = \mathbf{45.0\text{ minutes}}$$

Evaluate the second-order conversion integral directly on the stack: enter target conversion `0.75 {{key:ENTER}} {{key:ENTER}} 1 {{key:x⇄y}} {{key:-}} {{key:÷}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 3.0000)$ to obtain dimensionless Damköhler number $X/(1-X) = 3.0$, then multiply by characteristic reaction time $(k C_{A0})^{-1} = 15.0\text{ min}$ (`15 {{key:×}}`) to obtain residence time $t = \mathbf{45.0\text{ minutes}}$ (or integrate `1 X {{key:-}} {{key:x²}} {{key:1/x}} 15 {{key:×}}` over `0 {{key:ENTER}} 0.75 {{key:∫}} X` $\to \mathbf{45.000000\text{ min}}$).
**First-Order Harmonic Companion ($\int_1^2 \frac{1}{x} dx = \ln 2$):** Contrast with the first-order half-life integral on the stack: {{res:sc32_08_calc_07:keys}} $\implies \mathbf{{{res:sc32_08_calc_07:value}}}$.

---

### Problem 8.34: Photonic Waveguide Mode Confinement Factor ($\Gamma$)
The fraction of optical power confined inside a semiconductor laser active core of half-width $d$ is the ratio of two Romberg integrals of the transverse electric field intensity $|E(x)|^2$:
$$\Gamma = \frac{\int_{-d}^d |E(x)|^2 \, dx}{\int_{-\infty}^\infty |E(x)|^2 \, dx} = \mathbf{0.8425} \quad (84.25\%\text{ optical confinement})$$
**RPN Workflow:** Integrate the numerator over $[-d, d]$, press `{{key:STO}} A`, integrate over the wide cladding domain $[-5d, 5d]$, and press `{{key:RCL}} A {{key:x⇄y}} {{key:÷}}`.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1 {{key:+/-}} {{key:ENTER}} 1 {{key:∫}} E` | $0.0000$ | $0.0000$ | $1.25 \times 10^{-11}$ | $1.6850$ | Core field energy over $[-d, d]$ |
| 2 | `{{key:STO}} A` | $0.0000$ | $0.0000$ | $1.25 \times 10^{-11}$ | $1.6850$ | Core energy stored in register A |
| 3 | `5 {{key:+/-}} {{key:ENTER}} 5 {{key:∫}} E` | $1.25 \times 10^{-11}$ | $1.6850$ | $2.40 \times 10^{-11}$ | $2.0000$ | Total field energy over $[-5d, 5d]$ |
| 4 | `{{key:RCL}} A {{key:x⇄y}} {{key:÷}}` | $1.6850$ | $1.6850$ | $2.40 \times 10^{-11}$ | **$0.8425$** | Optical confinement factor $\Gamma = 84.25\%$ |

---

### Problem 8.35: Terzaghi Soil Consolidation Degree Integral
Integrating excess pore-water pressure dissipation across a clay layer of drainage thickness $H_d$ at dimensionless time factor $T_v = 0.50$ yields average settlement consolidation:
$$U(T_v) = 1 - \frac{1}{2H_d}\int_0^{2H_d} \frac{u(z, T_v)}{u_0} \, dz \approx 1 - \frac{8}{\pi^2} e^{-\pi^2 (0.50) / 4} \approx \mathbf{76.4\%}$$

Evaluate the consolidation series directly on the stack: compute the exponential decay term `{{key:π}} {{key:x²}} 0.5 {{key:×}} 4 {{key:÷}} {{key:+/-}} {{key:eˣ}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.2911)$, scale by the Fourier attenuation series prefactor `8 {{key:×}} {{key:π}} {{key:x²}} {{key:÷}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.2360)$, and subtract from unity `1 {{key:x⇄y}} {{key:-}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.7640)$, determining consolidation degree $U(0.50) = \mathbf{76.4\%}$.

---

### Problem 8.36: Schuler-Tuned Inertial Navigation Period & Gravity Integral
Integrating gravitational restoring torque around Earth's mean radius $R_E = 6,371\text{ km}$ yields the classic Schuler pendulum period $T_S = 2\pi\sqrt{R_E / g_0} = \mathbf{84.4\text{ minutes}}$, while vertical rocket ascent velocity subtracts the gravity loss integral $\int_0^{t_b} g_0 \, dt = g_0 t_b$ from ideal Tsiolkovsky impulse:

> ***The x⇄y Denominator Flip & Gravity Loss Integral*** — Integrate vertical gravity loss $g_0 t_b$ directly on the stack, swap with ideal rocket impulse via `{{key:x⇄y}}`, and resolve net burnout velocity in a single subtraction step {{cite:munroe2014,hp15c1982}}.

Arm the stack with standard gravity ($g_0 = 9.80665\text{ m/s}^2$) in Register $Y$ and multiply by burn time ($t_b = 6.0\text{ s}$): `9.80665 {{key:ENTER}} 6 {{key:×}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 58.8399)$. Key ideal impulse ($184.8\text{ m/s}$) and execute *The x⇄y Denominator Flip*: `184.8 {{key:x⇄y}}` $(T: 0.0000, Z: 0.0000, Y: 184.8000, X: 58.8399)$. Subtract gravity loss `{{key:-}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 125.9601)$ to resolve net vertical burnout velocity $v = \mathbf{125.9601\text{ m/s}}$.
**Net Vertical Velocity Check ($v_{\text{ideal}} = 184.8\text{ m/s}$, $t_b = 6\text{ s}$):** {{res:sc32_08_calc_08:keys}} $\implies \mathbf{{{res:sc32_08_calc_08:value}}\text{ m/s}}$.

---

### Problem 8.37: Supersonic Sears-Haack Minimum Wave-Drag Body
Evaluating the von Kármán slender-body wave-drag double integral for a minimum-drag Sears-Haack fuselage of length $L = 30.0\text{ m}$, volume $V = 45.0\text{ m}^3$, and flight dynamic pressure $q_\infty = 25,000\text{ Pa}$ yields:
$$D_{\text{wave}} = q_\infty \frac{128 V^2}{\pi L^4} = 25,000 \times \frac{128(2025)}{\pi(810,000)} \approx \mathbf{2,546.48\text{ N}}$$
**Engineering Insight:** Because wave drag scales with $L^{-4}$, lengthening the nose-to-tail fineness ratio by just $10\%$ reduces supersonic wave drag by $1 - 1.10^{-4} = 31.7\%$!

> ***The Constant-in-T Pipeline & Slender Body Aerodynamics*** — Stream body volume squared $V^2$ and fuselage length fourth power $L^4$ across stack levels, resolving minimum wave drag without manual register juggling {{cite:munroe2014,hp15c1982}}.

Stream body parameters across the stack without manual register juggling: evaluate numerator product $128 V^2$ via `128 {{key:ENTER}} 45 {{key:x²}} {{key:×}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 259200.0)$, compute denominator $\pi L^4$ and divide `30 {{key:ENTER}} 4 {{key:yˣ}} {{key:π}} {{key:×}} {{key:÷}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.101859)$, then multiply by dynamic pressure `25000 {{key:×}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 2546.4793)$, resolving minimum wave drag $D_{\text{wave}} \approx \mathbf{2,546.48\text{ N}}$.

---

### Problem 8.38: Stratospheric Ozone Column Integration (Dobson Units)
Integrating satellite UV backscatter ozone number density across 3 stratospheric layers ($45.0 + 195.0 + 60.0\text{ DU}$) from tropopause to $z = 50\text{ km}$ yields total column abundance:
$$\Omega = \int_0^{50\text{ km}} N_{\text{O3}}(z) \, dz = 8.06 \times 10^{22}\text{ molecules/m}^2 \equiv \mathbf{300.0\text{ Dobson Units}}$$
*(where $1\text{ DU} = 2.6867 \times 10^{20}\text{ molecules/m}^2$, equivalent to a $0.01\text{ mm}$ layer of pure ozone at STP).*

***The Column Abundance Integration Pipeline*** — Integrate vertical Dobson unit density profiles directly across atmospheric layers with adaptive Romberg quadrature {{cite:strogatz2019,hp15c1982}}.

Sum discrete atmospheric layer abundances across tropopause, ozone peak, and stratosphere: `45 {{key:ENTER}} 195 {{key:+}} 60 {{key:+}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 300.0000)$, finding total column abundance $\Omega = \mathbf{300.0\text{ DU}}$. Multiply by the physical Dobson unit conversion factor `2.6867 {{key:E}} 20 {{key:×}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 8.0601 \times 10^{22})$, yielding areal column number density $N_{\text{O3}} \approx \mathbf{8.0601 \times 10^{22}\text{ molecules/m}^2}$.

---

### Problem 8.39: High-Speed Sprint: Definite Integral of Cubic Monomial
Evaluate $\int_0^4 3x^2 \, dx = [x^3]_0^4 = 4^3 = \mathbf{64.0}$.
**Romberg Program:** `X {{key:x²}} 3 {{key:×}}`. Limits: `0 {{key:ENTER}} 4`. `{{key:∫}} X` returns **$64.000000$**!
***The Horner Polynomial Stream & Monomial Definite Integral*** — Evaluate antiderivative $[x^3]_0^4 = 4^3$ directly on the operational stack in a single cubic keystroke {{cite:hp15c1982}}.

Position upper integration boundary ($x = 4.0$) into Register $Y$ and cube in place: `4 {{key:ENTER}} 3 {{key:yˣ}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 64.000000)$, evaluating monomial definite integral $\int_0^4 3x^2 dx = 4^3 = \mathbf{64.000000}$ in a single cubic keystroke.
**Analytical Stack Verification:** {{res:sc32_08_calc_05:keys}} $\implies \mathbf{{{res:sc32_08_calc_05:value}}}$.

---

### Problem 8.40: High-Speed Sprint: Central-Difference Derivative of $e^{2x}$
**Rapid Calculation Sprint:** Evaluate $f'(0)$ for $f(x) = e^{2x}$ using step $h = 10^{-5}$.
**Analytical:** $f'(x) = 2 e^{2x} \implies f'(0) = 2.0$.

Evaluate the symmetric central difference $\frac{e^{2h} - e^{-2h}}{2h}$ directly on the RPN stack: key `0.00002 {{key:eˣ}} 0.00002 {{key:+/-}} {{key:eˣ}} {{key:-}} 0.00002 {{key:÷}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 2.000000)$, computing $f'(0) = \mathbf{2.000000}$ to 10 significant digits in a single stack stream.

---

## Summary & Looking Ahead

Chapter 8 elevated the operational stack into the continuous domain of calculus. By combining Richardson extrapolation with adaptive interval halving, the Romberg numerical quadrature engine (`{{key:∫}}`) eliminated truncation error systematically, evaluating definite integrals across rocket burnout thrust profiles, aerodynamic wave-drag envelopes, and stratospheric column densities to 10 decimal digits of precision. Coupled with central-difference numerical differentiation, continuous rate equations and integral accumulations yielded exact answers in seconds.

Calculus provides exact models for deterministic continuous phenomena, but real-world engineering and laboratory science must also grapple with random variation, noisy sensor measurements, and empirical trends. In **Chapter 9: Statistics, Probability Distributions & Regression Curve Fitting**, you will harness the SC-32's six dedicated statistical summation registers ($\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$). You will compute weighted means and standard deviations, perform linear and non-linear regression calibrations, and evaluate continuous Gaussian, Poisson, and Weibull probability distributions directly on the stack.
