---
title: "Chapter 8: Numerical Calculus & Adaptive Romberg Quadrature | SC-32 Manual"
description: "Master Adaptive Romberg numerical integration [∫], Richardson error cancellation, central-difference numerical differentiation, and applied calculus on the StackCalc SC-32."
---

# Chapter 8: Numerical Calculus & Adaptive Romberg Quadrature

## The Acceleration of the Saturn V & Werner Romberg's Extrapolation

When the five massive Rocketdyne F-1 engines ignite beneath the Apollo Saturn V lunar launch vehicle at Kennedy Space Center, they consume fifteen metric tons of RP-1 kerosene and liquid oxygen every second. As propellants drain from the tanks, the vehicle's thrust-to-weight ratio surges, pinning the crew into their contour couches under $4.5\,g$. Vehicle acceleration $a(t)$ does not follow a clean textbook polynomial; it is governed by transonic compressibility shocks, atmospheric density gradients, aerodynamic buffet, and propellant sloshing. Nor do the fundamental integrals of probability ($e^{-x^2}$), nonlinear pendulum dynamics (complete elliptic integrals), or thermal physics (Planck blackbody radiation) possess closed-form elementary antiderivatives.

How fast is the spacecraft travelling when the S-IC first stage burns out at $T = 160\text{ seconds}$? Under the Fundamental Theorem of Calculus, velocity is the definite integral of acceleration:

$$v(T) = v_0 + \int_0^T a(t)\,dt$$

If the flight guidance calculator cannot evaluate that integral with certified numerical precision, engine cut-off will occur fractions of a second too early or too late. A $0.1\%$ velocity shortfall means missing translunar injection entirely and tumbling into the void of deep space.

### The Trapezoidal Trap: Why Doubling the Slices Cuts the Error by One-Fourth
Why is brute-force numerical integration so painfully slow? Imagine slicing the area under a smooth curve $f(t)$ into flat-topped trapezoids of width $h$. Over any narrow panel, a smooth curve bends locally like a parabola, leaving a thin, crescent-shaped "meniscus" sliver between the true curve and the straight secant chord of the trapezoid. Because the chord spans a width $h$ and the parabolic sag in the middle is proportional to $h^2$, the area of each individual meniscus sliver scales as $\text{width} \times \text{sag} \propto h^3$. When you add up all $N = (b - a)/h$ panels across the interval, the total truncation error scales as $N \times h^3 \propto h^2$.

That $O(h^2)$ scaling law carries both bad news and a hidden mathematical gift. The bad news is that if you want to brute-force your way to ten decimal digits of precision using plain trapezoids, halving the step width $h \to h/2$ only shrinks the error to $\left(\frac{1}{2}\right)^2 = \frac{1}{4}$ of its previous size. To squeeze ten digits out of a stubborn integral, a naive calculator would have to evaluate hundreds of thousands of microscopic slices, draining battery cells for twenty minutes of continuous crunching.

### Lewis Fry Richardson & Werner Romberg: The $4/3 - 1/3$ Error-Cancellation Miracle
The hidden gift in that $1/4$ ratio was spotted first by English polymath Lewis Fry Richardson in 1910 and generalized into an automated quadrature algorithm by Norwegian physicist Werner Romberg in 1955 {{cite:romberg1955}}. By examining the Euler-Maclaurin summation formula, Romberg noted that the truncation error in a composite trapezoidal sum $T(h)$ is not random noise—it is a clean, deterministic power series in even powers of the step size $h$:

$$\int_a^b f(t)\,dt = T(h) + c_1 h^2 + c_2 h^4 + c_3 h^6 + \dots$$

Suppose you compute a coarse trapezoidal estimate $T_{\text{coarse}} = T(h)$ and then halve the step size once to get a fine estimate $T_{\text{fine}} = T(h/2)$. Because halving $h$ shrinks the dominant $c_1 h^2$ error term by an exact factor of $1/4$, your two estimates look like a system of two equations:

$$T_{\text{coarse}} \approx I - E, \qquad T_{\text{fine}} \approx I - \frac{1}{4}E$$

Romberg posed a deceptively simple question: *If the fine estimate has exactly one-fourth the leading error of the coarse estimate, why not combine them algebraically to knock out $E$ completely?* Multiply the fine estimate by $\frac{4}{3}$ and subtract $\frac{1}{3}$ of the coarse estimate:

$$\frac{4}{3} T_{\text{fine}} - \frac{1}{3} T_{\text{coarse}} = \frac{4 T(h/2) - T(h)}{3} = I + \mathcal{O}(h^4)$$

The dominant $h^2$ error term vanishes at a single stroke! And you don't have to stop there: by arranging successive halvings into a lower-triangular **Romberg Tableau**, the same Richardson extrapolation recipe cancels the $h^4$ term ($\frac{16 R_2 - R_1}{15}$), then the $h^6$ term ($\frac{64 R_3 - R_2}{63}$), turning a sluggish $O(h^2)$ crawl into an $O(h^{2k})$ rocket of convergence. Just four or five Romberg step-halvings achieve greater precision than 500,000 brute-force trapezoids.

On the StackCalc SC-32, pressing {{key:∫}} executes Romberg's tableau directly on your operational stack, evaluating non-integrable reality with breathtaking speed and returning both the integral and its certified uncertainty bound. Unless degrees (`{{key:DEG}}`) are explicitly noted, trigonometric and calculus sequences in this chapter assume radian mode (`{{key:RAD}}`).

---

## From Physical Rate Transducers to Romberg Tableau Quadrature

Every definite integral in engineering measures a physical accumulation: an inertial accelerometer integrating rocket boost thrust into velocity, an acoustic flowmeter totaling storm discharge across a culvert weir, or a variable-rate spring storing mechanical work $W = \int_a^b F(x)\,dx$ as it compresses. Geometrically, partitioning the domain $[a, b]$ into trapezoidal panels approximates the area under the curve, with truncation error governed by the Euler-Maclaurin asymptotic expansion $T(h) + c_1 h^2 + c_2 h^4 + c_3 h^6 + \dots$.

On the StackCalc SC-32, you stage the lower and upper integration limits $(a, b)$ directly into Registers $Y$ and $X$ before invoking `{{key:∫}}`. Behind that single keystroke, the calculator constructs the triangular Romberg tableau $R(k, j)$, applying Richardson extrapolation to cancel successive $h^2, h^4, h^6$ error terms without brute-force sub-stepping, and returns the converged integral $I$ in Register $X$ alongside its uncertainty bound $\pm\varepsilon$ in Register $Y$.

{{blocks:sc32_rpn_calculation|Active RPN Calculation on Transflective LCD}}

{{res:sc32_plot_romberg_shaded:screenshot|SC-32 Vector Plotter: Shaded Definite Integral of 3x^2 from 0 to 4 (Area = 64.0)}}
*Figure 8.1: The SC-32 transflective display executing active numerical integration, demonstrating real-time stack updates and error bound estimation.*

---

## Adaptive Romberg Numerical Quadrature ({{key:∫}})

### The Feynman Intuition: The Coastline of Britain & The Richardson Leap

Suppose you set out to measure the perimeter of a rugged, rocky island. You walk along the shore with a 10-meter chain, recording a total distance of 1,000 meters. Next, you re-measure the same coastline with a 5-meter rod. Because the shorter rod fits into small bays and rocky inlets, your measurement increases to 1,200 meters.

Traditional brute-force intuition insists: *To find the true, exact value, we must measure with a 1-centimeter ruler, then a 1-millimeter gauge, taking forever.*

In 1910, English polymath Lewis Fry Richardson discovered a profound mathematical shortcut: **You do not need an infinite number of microscopic rulers.** If you understand mathematically how measurement error scales with the size of your ruler (for instance, error proportional to $h^2, h^4, h^6$), you can algebraically combine your 10-meter and 5-meter measurements to cancel the error completely.

That is Richardson Extrapolation—the analytical engine inside Werner Romberg's 1955 quadrature algorithm. It evaluates a few coarse trapezoids and then uses the geometry of error to vault directly to $10^{-12}$ precision with over $95\%$ fewer function evaluations.

{{blocks:fraction_studio_common_denominator|84 mm Fraction Towers: Proportional Step-Tower Heights (42 mm, 28 mm, 21 mm, 14 mm) Modeling Riemann Quadrature}}
*Figure 8.2: The 84 mm Fraction Towers ($\frac{1}{2} = 42\text{ mm}$, $\frac{1}{3} = 28\text{ mm}$, $\frac{1}{4} = 21\text{ mm}$, $\frac{1}{6} = 14\text{ mm}$) physically illustrate harmonic step-rectangles ($1/x$), trapezoidal chord slanting, and proportional interval halving corresponding to Richardson extrapolation steps.*

### From Physical Fraction-Tower Step Rectangles to Romberg Extrapolation

To see why Romberg's quadrature converges orders of magnitude faster than textbook Riemann sums, dock the physical **84 mm Fraction Towers** upright in decreasing order along the $3 \times 1$ Gridfinity lid tray (*Figure 8.2*). The set contains 78 stackable $19.0 \times 19.0\text{ mm}$ Miniblock fraction blocks engineered around an **$84.0\text{ mm}$ master unit datum** ($1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \frac{1}{5}, \frac{1}{6}, \frac{1}{7}, \frac{1}{8}, \frac{1}{9}, \frac{1}{10}, \frac{1}{11}, \frac{1}{12}$, each bearing 4-face debossed fraction, decimal, percent, and `.1.n` keystroke markings):
* $1\text{ whole tower} = 84.0\text{ mm}$ at $x = 1$
* $\frac{1}{2}\text{ tower} = 42.0\text{ mm}$ at $x = 2$
* $\frac{1}{3}\text{ tower} = 28.0\text{ mm}$ at $x = 3$
* $\frac{1}{4}\text{ tower} = 21.0\text{ mm}$ at $x = 4$
* $\frac{1}{6}\text{ tower} = 14.0\text{ mm}$ at $x = 6$
* $\frac{1}{8}\text{ tower} = 10.5\text{ mm}$ at $x = 8$
* $\frac{1}{12}\text{ tower} = 7.0\text{ mm}$ at $x = 12$

Notice what curve the visible heights of those $19.0 \times 19.0\text{ mm}$ columns trace: because each $\frac{1}{n}$ block has exact physical height $H(n) = \frac{84.0\text{ mm}}{n}$, docking them side-by-side along the $3 \times 1$ Gridfinity lid tray traces out the exact rectangular hyperbola $f(x) = \frac{1}{x}$—the canonical curve whose definite integral defines the natural logarithm $\ln b - \ln a = \int_a^b \frac{dx}{x}$.
1. **The Riemann Step Column ($\mathcal{O}(h)$ Error):** When you dock the flat-topped Miniblock towers ($1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \frac{1}{6}$) side-by-side along the socket rail, their flat $19.0 \times 19.0\text{ mm}$ horizontal roofs form a jagged **Riemann step function**. Between the $42.0\text{ mm}$ roof of the $\frac{1}{2}$ block and the $28.0\text{ mm}$ roof of the $\frac{1}{3}$ block sits a $14.0\text{ mm}$ vertical cliff—leaving a coarse triangular air gap whose area error shrinks only linearly as $\mathcal{O}(h)$.
2. **The Trapezoidal Chord ($\mathcal{O}(h^2)$ Error):** Now lay a straightedge diagonally from the $42.0\text{ mm}$ upper edge of the $\frac{1}{2}$ tower to the $28.0\text{ mm}$ edge of the $\frac{1}{3}$ tower, and down to the $21.0\text{ mm}$ edge of the $\frac{1}{4}$ tower. Slanting the flat step tops into **trapezoids** eliminates the large triangular staircase steps in a single stroke. Only a thin, crescent-shaped **meniscus sliver** remains between the straight secant chord and the bowed belly of the $1/x$ curve, reducing the error to $\mathcal{O}(h^2)$.
3. **Romberg's Half-Width Extrapolation ($\mathcal{O}(h^4) \to \mathcal{O}(h^{12})$):** Next, compare a coarse block span of width $h$ (say from $x = 2$ to $x = 4$, using the $\frac{1}{2}$ and $\frac{1}{4}$ towers) against the half-width subdivision $h/2$ that inserts the $\frac{1}{3} = 28.0\text{ mm}$ midpoint tower at $x = 3$ (or subdivides $\frac{1}{2} \to \frac{1}{4} \to \frac{1}{8}$ and $\frac{1}{3} \to \frac{1}{6} \to \frac{1}{12}$). Because a smooth curve looks locally like a parabola on a small interval, halving the step width $h \to h/2$ shrinks the curved meniscus error by an exact geometric ratio of $\left(\frac{1}{2}\right)^2 = \frac{1}{4}$. Werner Romberg realized that taking $\frac{4 T(h/2) - T(h)}{3}$ subtracts out that $\frac{1}{4}$ meniscus sliver *completely*, leaping from straight-topped trapezoids ($\mathcal{O}(h^2)$) to parabolic Simpson arches ($\mathcal{O}(h^4)$), Boole's 5-point splines ($\mathcal{O}(h^6)$), and up to $\mathcal{O}(h^{12})$ without requiring microscopic subdivisions.

Definite integrals calculate accumulated physical quantities across continuous domains: total distance traversed under non-constant velocity, mechanical work performed under variable forces, electrical charge accumulated from transient current pulses, and fluid pressure forces exerted across curved dams. The StackCalc SC-32 evaluates definite integrals using **Adaptive Romberg Numerical Quadrature ({{key:∫}})**:

$$I = \int_a^b f(x) \, dx$$

When you ask the SC-32 to integrate $I = \int_a^b f(x)\,dx$, the calculator does not blindly chop the interval $[a, b]$ into thousands of tiny pieces from the start. Instead, it begins with a single wide trapezoid spanning the entire interval $h_0 = b - a$, and then halves the step width row by row ($h_k = (b - a)/2^k$ for $k = 1 \dots 8$). Because every old boundary point is also a boundary point of the next finer grid, the base trapezoidal column $R(k, 0)$ never wastes a single function call: it simply takes half of the previous trapezoidal sum and adds the newly sampled midpoints:

$$R(k, 0) = \frac{1}{2}R(k-1, 0) + h_k \sum_{i=0}^{2^{k-1}-1} f(a + (2i+1)h_k)$$

Once a new trapezoidal row $R(k, 0)$ is in hand, Richardson extrapolation sweeps across the row from left to right. The first extrapolation ($j = 1$) combines the fine and coarse trapezoids via $\frac{4 R(k, 0) - R(k-1, 0)}{3}$ to cancel the $\mathcal{O}(h^2)$ error—which is algebraically identical to **Simpson's $1/3$ Parabolic Rule** ($\mathcal{O}(h^4)$). The second column ($j = 2$) combines two Simpson estimates via $\frac{16 R(k, 1) - R(k-1, 1)}{15}$ to cancel the $\mathcal{O}(h^4)$ term, matching **Boole's 5-Point Rule** ($\mathcal{O}(h^6)$). In general, each step to the right applies the universal Richardson recurrence:

$$R(k, j) = R(k, j-1) + \frac{R(k, j-1) - R(k-1, j-1)}{4^j - 1}, \quad j = 1 \dots \min(k, 5)$$

By capping the tableau width at column $j_{\max} = 5$ ($\mathcal{O}(h^{12})$), the engine achieves 11 to 12 digits of precision on smooth curves while preventing high-degree polynomial ringing on steep peaks. Better still, the stopping criterion adapts automatically to your display mode (`FIX`, `SCI`, `ENG`, or `ALL`), halting as soon as the discrepancy between adjacent tableau entries falls below $\varepsilon_{\text{rel}} = \max(10^{-11}, 10^{-\max(5, \text{places}+3)})$ (or $10^{-11}$ in `ALL` mode, with an absolute floor of $10^{-13}$ for $k \ge 3$).

| Column Index | Classical Quadrature Rule Equivalent | Error Order | Convergence Characteristics |
| :---: | :--- | :---: | :--- |
| **$j = 0$** | Extended Composite Trapezoidal Rule | $\mathcal{O}(h^2)$ | Coarse baseline; samples function boundaries and midpoints. |
| **$j = 1$** | Simpson's $1/3$ Parabolic Rule | $\mathcal{O}(h^4)$ | Cancels leading $h^2$ error term via 4:1 weighting. |
| **$j = 2$** | Boole's 5-Point Rule | $\mathcal{O}(h^6)$ | Cancels $h^4$ curvature artifact; achieves 6 digits. |
| **$j = 3$** | High-Order Analytical Extrapolation | $\mathcal{O}(h^8)$ | Sub-ppm precision on smooth transcendentals. |
| **$j = 4, 5$** | Capped Richardson Limit ($j_{\max} = 5$) | $\mathcal{O}(h^{10}) \to \mathcal{O}(h^{12})$ | Caps column order at $\mathcal{O}(h^{12})$ to prevent Runge ringing on sharp peaks. |

### The Lower-Triangular Romberg Tableau
As step size $h_k = (b - a)/2^k$ is halved at each row $k$, the algorithm populates the lower-triangular Romberg matrix $R(k, j)$ from left to right. Within 4 to 6 step halvings, the entry $R(k, \min(k, 5))$ achieves **$10^{-11}$ to $10^{-12}$ precision** with over **95% fewer function evaluations** than standard composite quadrature:

| Step Index $k$ | Intervals ($2^k$) | Step Size $h_k$ | Column $j=0$ (Trapezoid) | Column $j=1$ (Simpson) | Column $j=2$ (Boole) | Column $j=3$ (Extrapolated) |
| :---: | :---: | :---: | :--- | :--- | :--- | :--- |
| **$k = 0$** | 1 | $b - a$ | $R(0, 0)$ [Trapezoid] | — | — | — |
| **$k = 1$** | 2 | $(b - a)/2$ | $R(1, 0)$ | $\longrightarrow R(1, 1)$ [Simpson] | — | — |
| **$k = 2$** | 4 | $(b - a)/4$ | $R(2, 0)$ | $\longrightarrow R(2, 1)$ | $\longrightarrow R(2, 2)$ [Boole] | — |
| **$k = 3$** | 8 | $(b - a)/8$ | $R(3, 0)$ | $\longrightarrow R(3, 1)$ | $\longrightarrow R(3, 2)$ | $\longrightarrow R(3, 3)$ |

### Avoidance of Runge's Phenomenon & Wide-Interval `1-2-5` Decade Partitioning
When engineers attempt high-accuracy quadrature by fitting a high-degree polynomial across equally spaced points (as in high-order Newton-Cotes formulas like Weddle's Rule or 10-point formulas), they encounter **Runge's Phenomenon**: wild polynomial oscillations near the boundaries of the interval that cause numerical error to explode exponentially.

The SC-32 Romberg engine eliminates Runge's phenomenon through three architectural safeguards:
1. **Low-Order Local Panels & Capped Extrapolation ($j_{\max} = 5$):** It evaluates stable piecewise-linear trapezoids on local sub-intervals $h_k$ and caps Richardson extrapolation at column $j = 5$ ($\mathcal{O}(h^{12})$), preventing high-degree polynomial ringing on steep peaks.
2. **Wide-Interval `1-2-5` Decade Partitioning ($|b - a| > 20$):** For compact intervals ($|b - a| \le 20$), a single Romberg panel suffices. For wide or semi-infinite intervals ($|b - a| > 20$), the engine automatically partitions $[a, b]$ at logarithmic `1-2-5` decade boundaries ($\pm 1, \pm 2, \pm 5 \times 10^m$ across 16 decades, plus $0$ if the interval crosses the origin) with up to 3 levels of recursive midpoint subdivision and a zero-mass tail short-circuit ($k \ge 2$).
3. **Monotonic Error Bound in Register $Y$:** Each panel tracks $\varepsilon = \max(|R(k, m) - R(k, m-1)|, |R(k, m) - R(k-1, \dots)|)$ and deposits the total error estimate directly into Register $Y$.

To watch the SC-32 build this Romberg tableau step-by-step on a familiar curve, consider the exponential integral $\int_0^2 e^x \, dx = e^2 - 1 \approx 6.389056$. At step $k=0$ ($h_0 = 2.0$), a single wide trapezoid spanning $[0, 2]$ gives $R(0, 0) = \frac{2}{2} [e^0 + e^2] = 1.0 \times [1.0 + 7.389056] = 8.389056$, overshooting the true area by $+31.3\%$. Halving the interval once at step $k=1$ ($h_1 = 1.0$) samples the midpoint $e^1$ to form $R(1, 0) = \frac{1}{2} R(0, 0) + 1.0 \times e^1 = 4.194528 + 2.718282 = 6.912810$, and combining the two trapezoids via Richardson's $4/3 - 1/3$ rule immediately leaps to the Simpson parabolic estimate $R(1, 1) = \frac{4 R(1, 0) - R(0, 0)}{3} = \frac{27.651240 - 8.389056}{3} = \mathbf{6.420728}$. Halving once more at step $k=2$ ($h_2 = 0.5$) adds the two quarter-point samples $e^{0.5}$ and $e^{1.5}$ to give $R(2, 0) = 3.456405 + 0.5[1.648721 + 4.481689] = 6.521610$, refines the Simpson column to $R(2, 1) = \frac{4(6.521610) - 6.912810}{3} = 6.391210$, and applies the $16/15 - 1/15$ Boole extrapolation to reach $R(2, 2) = \frac{16(6.391210) - 6.420728}{15} = \mathbf{6.389242}$. In only two step halvings, the error drops from $+31.3\%$ to $+0.0029\%$, and by $k=4$ the discrepancy is below $10^{-12}$.

### Stack Operational Convention for {{key:∫}}
Because Reverse Polish Notation treats integration limits as ordinary numbers on the stack rather than arguments trapped inside a parenthesis string, staging a definite integral feels as natural as dividing two numbers. You simply key the lower limit $a$, press `{{key:ENTER}}` to lift it into Register $Y$, key the upper limit $b$ into Register $X$, and press `{{key:∫}}` followed by the variable of integration (such as `{{key:∫}} X` or `{{key:∫}} T`). When the Romberg tableau converges, Register $X$ displays the evaluated definite integral $I = \int_a^b f(x)\,dx$, while Register $Y$ receives the certified numerical uncertainty bound $\pm\epsilon$ so a single tap of `{{key:x⇄y}}` lets you audit how tightly the integral converged.

---

### Rocket Motor Burnout Velocity Integration

To see how effortless this stack workflow feels in practice, consider the boost phase of a solid-propellant model rocket. As the internal star-perforated propellant grain burns outward, combustion chamber pressure and expanding surface area produce a non-linear acceleration curve over the burn duration $t \in [0, 6]\text{ seconds}$:

$$a(t) = 4 t^2 - 0.5 t^3 \quad (\text{m/s}^2)$$

How fast is the rocket climbing when the propellant burns out at $t = 6\text{ seconds}$? By the Fundamental Theorem of Calculus, we integrate acceleration from ignition ($t = 0$) to burnout ($t = 6$), which analytically evaluates to $\left[ \frac{4}{3} t^3 - \frac{0.5}{4} t^4 \right]_0^6 = \frac{4}{3}(216) - \frac{1}{8}(1296) = 288.0 - 162.0 = \mathbf{126.0\text{ m/s}}$:

$$v_{\text{burn}} = \int_0^6 \left(4 t^2 - 0.5 t^3\right) \, dt$$

On the SC-32, we open the Equation Editor (`{{key:EQN}}`), key the postfix integrand `T {{key:x²}} 4 {{key:×}} T 3 {{key:yˣ}} 0.5 {{key:×}} {{key:-}}`, and press `{{key:ENTER}}` to save it under the label `ROCKET`. Staging the lower limit $a = 0$ into Register $Y$ and the upper limit $b = 6$ into Register $X$ via `0 {{key:ENTER}} 6` and pressing `{{key:∫}} T` launches the Romberg quadrature engine:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}} 6` | $0.0000$ | $0.0000$ | $0.0000$ | $6.0000$ | Limits: $a=0$ in $Y$, $b=6$ in $X$ |
| 2 | `{{key:∫}} T` | $0.0000$ | $0.0000$ | **$1.2435 \times 10^{-11}$** | **$126.000000000$** | Burnout velocity $v_{\text{burn}}$ in $X$; error bound $\pm\varepsilon$ in $Y$ |

The burnout velocity in Register $X$ converges to **$126.0\text{ m/s}$** ($453.6\text{ km/h}$), while Register $Y$ reports the adaptive Romberg truncation error bound ($\pm 1.2435 \times 10^{-11}\text{ m/s}$, inspectable via `{{key:x⇄y}}`). In propulsion and structural analysis, engineers frequently cross-check numerical quadrature against closed-form antiderivatives directly on the 4-level stack: evaluating the factored antiderivative $F(t) = t^3\!\left(\frac{4}{3} - \frac{1}{8}t\right)$ at $t = 6\text{ s}$ while typing `6` only once via `4 {{key:ENTER}} 3 {{key:÷}} 6 {{key:ENTER}} 8 {{key:÷}} {{key:LASTX}} {{key:x⇄y}} {{key:-}} {{key:x⇄y}} 3 {{key:yˣ}} {{key:×}}` (or directly `6 {{key:ENTER}} 3 {{key:yˣ}} 4 {{key:×}} 3 {{key:÷}} {{key:LASTX}} {{key:LASTX}} {{key:×}} {{key:×}} 0.125 {{key:×}} {{key:-}}`) confirms **$126.0000\text{ m/s}$** in Register $X$ with zero solver iteration.

---

### Gaussian Normal CDF & Error Function Integration

A polynomial like $4t^2 - 0.5t^3$ is a warm-up where we can check Romberg against a pencil-and-paper antiderivative. Now let us turn Romberg loose on the most famous non-integrable curve in science: Carl Friedrich Gauss's bell curve. No finite combination of polynomials, roots, logarithms, or exponentials can express the antiderivative of $e^{-t^2/2}$ in elementary closed form—yet every quality engineer, physicist, and statistician needs its cumulative area:

$$\Phi(z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^z e^{-t^2 / 2} \, dt$$

Because the Gaussian density drops off faster than any simple exponential in the tails, integrating from a lower bound of $a = -5.0$ (five standard deviations below the mean, where the omitted tail area is less than $2.87 \times 10^{-7}$) captures the cumulative probability to full working precision. Let us verify that integrating up to the center of the bell ($z = 0$) returns exactly half of the total probability, $\Phi(0) = 0.500000$:

$$\Phi(0) \approx \frac{1}{\sqrt{2\pi}} \int_{-5}^0 e^{-x^2 / 2} \, dx$$

By storing the normalized Gaussian density `X {{key:x²}} 2 {{key:÷}} {{key:+/-}} {{key:eˣ}} 2 {{key:π}} {{key:×}} {{key:√x}} {{key:÷}}` under the label `NORM` in `{{key:EQN}}`, we can stage the integration interval `5 {{key:+/-}} {{key:ENTER}} 0` across Registers $Y$ and $X$ and press `{{key:∫}} X` to integrate the bell curve directly on the stack:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `5 {{key:+/-}} {{key:ENTER}} 0` | $0.0000$ | $0.0000$ | $-5.0000$ | $0.0000$ | Integration interval $[-5, 0]$ |
| 2 | `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$2.15 \times 10^{-10}$** | **$0.5000000000$** | $\Phi(0) = 0.500000$ |

The SC-32 returns **$0.500000$**, confirming the exact left-half symmetry of the normal bell curve without needing a printed statistical lookup table.

---

## Numerical Differentiation: Central Differences on the RPN Stack

If numerical integration is the art of accumulating smooth areas, numerical differentiation is the art of measuring an instantaneous slope without falling into a floating-point trap. Suppose you want the derivative $f'(x)$ of a curve at a point $x$, and you try the textbook one-sided forward difference $\frac{f(x+h) - f(x)}{h}$. Geometrically, stepping only to the right draws a lopsided secant chord: if the curve bends upward ($f''(x) > 0$), the forward chord systematically overshoots the true tangent slope by $\frac{1}{2}h f''(x)$, giving a sluggish $\mathcal{O}(h)$ error. Worse, if you try to brute-force that error away by making $h$ microscopic—say $h = 10^{-11}$—then $f(x+h)$ and $f(x)$ agree to their first 11 digits, and subtracting them wipes out almost all your significant figures in **catastrophic subtraction cancellation**!

### Central Difference Numerical Differentiation Mechanics

The remedy is pure geometric symmetry. Instead of stepping only forward from $x$ to $x + h$, straddle the point symmetrically by stepping backward to $x - h$ and forward to $x + h$:

$$f'(x) \approx \frac{f(x + h) - f(x - h)}{2 h}$$
$$f''(x) \approx \frac{f(x + h) - 2 f(x) + f(x - h)}{h^2}$$

Why does straddling the point work such magic? Expand $f(x + h)$ and $f(x - h)$ in Taylor series around $x$: on the right, the curve bends away from the tangent line by $+\frac{1}{2}h^2 f''(x) + \frac{1}{6}h^3 f'''(x)$; on the left, it bends by $+\frac{1}{2}h^2 f''(x) - \frac{1}{6}h^3 f'''(x)$. When you subtract $f(x - h)$ from $f(x + h)$, both $f(x)$ *and* the even quadratic curvature term $\frac{1}{2}h^2 f''(x)$ cancel out identically! The secant chord joining $(x - h, f(x - h))$ to $(x + h, f(x + h))$ runs nearly parallel to the true tangent at $x$, leaping to $\mathcal{O}(h^2)$ accuracy with just two function evaluations.

Because the truncation error now shrinks as $h^2$ while floating-point roundoff grows as $\varepsilon_{\text{mach}}/h$, the optimal step size sits near the cube root of machine epsilon ($\varepsilon_{\text{mach}}^{1/3} \approx 6 \times 10^{-6}$). The SC-32's internal derivative routine (and its plot tangent-line overlay) selects the symmetric step $h = 10^{-5}$ ($2h = 2 \times 10^{-5}$), hitting up to 10 digits of derivative accuracy without triggering subtraction cancellation. And if you ever need even higher precision from two moderate step sizes $h$ and $h/2$, the exact same Richardson combination we used for Romberg integration—$f'(x) \approx \frac{4 D(h/2) - D(h)}{3}$—cancels the $\mathcal{O}(h^2)$ derivative error term to reach $\mathcal{O}(h^4)$.

To test this symmetric straddle on the parabola $f(x) = x^2$ at $x = 3.0$ using step $h = 10^{-5}$ ($x + h = 3.00001$, $x - h = 2.99999$, and $2h = 0.00002$), we square the forward point `3.00001 {{key:x²}}`, square and subtract the backward point `2.99999 {{key:x²}} {{key:-}}`, and divide by the symmetric span `0.00002 {{key:÷}}`, which delivers the exact slope **$6.0000000000$** ($f'(3) = 2(3) = 6.0$) in Register $X$:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `3.00001 {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $9.000060$ | Forward point $f(x_0 + h) = 3.00001^2$ |
| 2 | `2.99999 {{key:x²}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.000120$ | Central difference $f(x_0 + h) - f(x_0 - h)$ |
| 3 | `0.00002 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$6.0000000000$** | Central-difference derivative $f'(3) = 6.0$ |

---

## Survey of Numerical Quadrature Across Engineering

Adaptive Romberg quadrature (`{{key:∫}}`), Richardson extrapolation, and central-difference differentiation apply directly across three major engineering domains:

1. **Mechanical Work, Centroids, Fluid Hydrostatics & Aerodynamic Circulation**:
   - *Non-Linear Mechanical Work & Structural Moments*: Compressing a progressive suspension spring ($F(x) = k_1 x + k_2 x^3$) stores elastic potential energy $W = \int_a^b F(x)\,dx$, while evaluating the mass $M = \int_0^L \lambda(x)\,dx$ and first moment $M_x = \int_0^L x\lambda(x)\,dx$ of a variable-density rod locates its centroid $\bar{x} = M_x/M$. Integrating $y^2$ across a structural I-beam web gives its flexural second moment of area $I_{xx} = \int_{-h/2}^{h/2} t y^2\,dy$, and integrating the Saint-Venant warping stress across an elliptical shaft with semiaxes $(a,b)$ yields its torsional rigidity $J = \frac{4a^2 b^3}{a^2+b^2}\int_{-1}^{1}(1-u^2)^{3/2}\,du = \frac{\pi a^3 b^3}{a^2+b^2}$.
   - *Hydrostatics, Poiseuille Pipe Discharge & Elliptic Wing Lift*: Integrating depth-weighted hydrostatic pressure across a parabolic dam gate yields total force $F = \rho g \int_0^H (H-y)w(y)\,dy$, and integrating concentric laminar velocity shells $v(r) = v_{\max}(1 - r^2/R^2)$ across a circular pipe gives Poiseuille volumetric discharge $Q = 2\pi\int_0^R v(r)r\,dr$. Across an aircraft wingspan $b$, integrating Prandtl's elliptic bound circulation $\Gamma(y) = \Gamma_0\sqrt{1 - (2y/b)^2}$ via Kutta-Joukowski's theorem yields total aerodynamic lift $L = \rho_\infty V_\infty \int_{-b/2}^{b/2}\Gamma(y)\,dy$, while integrating von Kármán's slender-body area distribution $S(u) = S_{\max}(1-u^2)^{3/2}$ determines the volume and supersonic wave drag $D_{\text{wave}} = q_\infty \frac{128 V^2}{\pi L^4}$ of a Sears-Haack fuselage.
   - *Oscillator Dissipation & Kinematic Sensitivity*: Integrating viscous damper power $c\dot{x}^2(t)$ over one period gives cycle energy loss $\Delta E = \int_0^T c\dot{x}^2\,dt$, while central-difference differentiation evaluates instantaneous radial velocity $\dot{r} = \omega\,dr/d\theta$ for rotating flyweight governors.

2. **Electromagnetics, Optics, Signal Processing & Acoustics**:
   - *Transient Surge Charge, Non-Linear Dielectrics & Clipped AC RMS Power*: Integrating an exponential lightning current pulse yields transferred charge $Q = \int_0^T I_0 e^{-t/\tau}\,dt$, and integrating voltage-dependent capacitance $C(V) = C_0(1 - \alpha V^2)$ gives the true stored energy $W = \int_0^V C(v)v\,dv$ in a ferroelectric ceramic capacitor. For an AC line waveform clipped at threshold angle $\theta_c = \arcsin(V_c/V_p)$, quarter-wave quadrature evaluates the true RMS voltage $V_{\text{rms}} = \sqrt{\frac{2}{\pi}\left[\int_0^{\theta_c}(V_p\sin\theta)^2\,d\theta + \int_{\theta_c}^{\pi/2} V_c^2\,d\theta\right]}$, while integrating $\frac{2}{\pi}\int_0^\pi f(x)\sin(nx)\,dx$ extracts Fourier harmonic coefficients.
   - *Fresnel Diffraction, Waveguide Confinement, Physical-Optics RCS & Acoustic Exposure*: Knife-edge optical diffraction relies on the non-elementary Fresnel sine and cosine integrals $S(x) = \int_0^x \sin(\frac{\pi}{2}t^2)\,dt$ and $C(x) = \int_0^x \cos(\frac{\pi}{2}t^2)\,dt$ along the Cornu spiral. In photonics and electromagnetics, the ratio of core-to-total field integrals $\Gamma = \int_{-d}^d |E(x)|^2\,dx / \int_{-\infty}^\infty |E(x)|^2\,dx$ defines slab-waveguide mode confinement, physical-optics surface phase integration determines the specular radar cross section $\sigma_{\max} = 4\pi A^2/\lambda^2$ of a conducting plate, and integrating transient squared acoustic pressure $E = \int_{-T}^T p^2(t)\,dt$ establishes aircraft Sound Exposure Level (SEL).

3. **Thermodynamics, Nuclear/Chemical Reactors, Geotechnics & Astrodynamics**:
   - *Polytropic Work, Variable-Conductivity Heat Flux & Cryogenic Contraction*: Reversible gas expansion integrates $W = \int_{V_1}^{V_2} C V^{-n}\,dV$, Fourier conduction across a temperature-dependent refractory wall integrates $q = \frac{A}{L}\int_{T_1}^{T_2} k(T)\,dT$, and chilling a stainless-steel propellant line from ambient $T_1$ to cryogenic $T_2$ integrates thermal strain $\Delta L = L\int_{T_1}^{T_2}\alpha(T)\,dT$ (where $T_2 < T_1$ naturally produces the negative contraction sign).
   - *Reactor Flux Peaking, Chemical Conversion & Soil Consolidation*: Integrating radial Bessel thermal neutron flux $\phi(r) = \phi_0 J_0(2.405r/R)$ across a cylindrical reactor core yields total thermal power $P_{\text{th}}$, integrating $(k C_{A0})^{-1}\int_0^X (1-x)^{-2}\,dx$ determines second-order batch reactor residence time, and integrating normalized excess pore-water pressure across a drainage layer yields Terzaghi's degree of soil consolidation $U(T_v)$.
   - *Atmospheric Column Abundance, Jeans Escape & Relativistic Ascent*: Integrating stratospheric UV backscatter profiles $D(z)$ via Romberg's parabolic column $R(1,1)$ yields total ozone abundance in Dobson Units, integrating the Maxwell-Boltzmann tail $\int_\lambda^\infty u e^{-u}\,du = (1+\lambda)e^{-\lambda}$ gives planetary atmospheric Jeans escape flux, integrating $\int_0^{t_b}(a_{\text{ideal}}(t) - g_0)\,dt$ accounts for vertical rocket gravity loss, and integrating the Lorentz factor $\int_0^\tau \cosh(g\tau'/c)\,d\tau'$ maps shipboard proper time to Earth coordinate time.

### Nested Quadrature Menus vs. Direct Stack Limits (`{{key:d/dx}}` & `{{key:∫}}`)

Comparing modal algebraic quadrature commands against the SC-32's stack-limit workflow illustrates both the keystroke savings and the error-visibility advantage of Romberg integration:

| Challenge / Metric | Conventional Algebraic Calculator (Infix) | Algebraic Strokes | SC-32 RPN Stack Method | SC-32 Strokes | Stack Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **Definite Numerical Integration**: Variable spring compression work | Menu dive into `[MATH] [9:fnInt(]`, type the 4-argument comma-delimited command for $\int_0^{0.15}(2500x + 40000x^3)\,dx$ (38 strokes). The integrand is locked inside the command line and cannot be evaluated or differentiated without re-typing; the returned scalar provides no certified error bound register on completion. | 38 | **Adaptive Romberg Quadrature (`{{key:∫}}`)**: Define postfix integrand `X 2500 {{key:×}} X 3 {{key:yˣ}} 40000 {{key:×}} {{key:+}}`, push limits `0 {{key:ENTER}} 0.15`, press `{{key:∫}} X` (18 strokes). Richardson tableau extrapolation eliminates $O(h^2), O(h^4), O(h^6)$ error in 3 halving cycles, returning certified $W = 33.1875\text{ J}$ to $X$ and absolute error bound $\pm 3.55 \times 10^{-12}$ to $Y$. | 18 | **53% fewer strokes + certified error bound in $Y$** |
| **Gaussian Normal Probability CDF**: $\Phi(1.96)$ bell curve | Menu dive or catalog search for the normal CDF command or a nested integration call for $\frac{1}{\sqrt{2\pi}}\int_0^{1.96} e^{-x^2/2}\,dx$ (44 strokes). Deep parenthesis nesting around the fractional exponent and normalization factor invites entry errors, and the black-box scalar hides the numerical quadrature residual. | 44 | **Non-Integrable Transcendentals via Richardson Extrapolation**: Program standard normal bell `T {{key:x²}} 2 {{key:÷}} {{key:+/-}} {{key:eˣ}} 2 {{key:π}} {{key:×}} {{key:√x}} {{key:÷}}`, push limits `0 {{key:ENTER}} 1.96`, press `{{key:∫}} T` (20 strokes). Converges in $<0.2\text{ s}$ to 12-digit precision ($0.4750021049$), with full stack visibility for direct summation `0.5 {{key:+}}` $\to 0.9750021049$. | 20 | **55% fewer strokes + complete stack transparency** |

---

## Numerical Boundary Conditions & Singularity Guards

Before launching into field integrals, three operational habits will save you from sign reversals, radian scaling errors, and hidden poles. First, because a definite integral accumulates signed displacement from $a$ to $b$, reversing the limits reverses the sign of the integral ($\int_b^a f(x)\,dx = -\int_a^b f(x)\,dx$). Always stage the starting lower limit $a$ in Register $Y$ and the ending upper limit $b$ in Register $X$ before pressing `{{key:∫}}`—though as we saw in the thermodynamic survey above, when a physical process genuinely cools downward from $T_1 = 300\text{ K}$ to a cryogenic $T_2 = 77\text{ K}$, placing $300$ in $Y$ and $77$ in $X$ naturally produces the negative thermal contraction sign!

Second, all calculus operations involving trigonometric functions (`SIN`, `COS`, `TAN`) mathematically require **Radians mode (`{{key:RAD}}`)**. Because the fundamental identity $\frac{d}{dx}[\sin x] = \cos x$ holds only when $x$ is measured in dimensionless radians (where arc length equals radius times angle; in degrees, an extra factor of $\pi/180$ appears), integrating a trigonometric expression while accidentally in `{{key:DEG}}` mode will scale your result by an erroneous factor of $180/\pi \approx 57.2958$. Third, cultivate the habit of tapping `{{key:x⇄y}}` after every integration to peek at the uncertainty bound $\pm\epsilon$ waiting in Register $Y$. A tiny residual such as $1.4 \times 10^{-11}$ confirms that the Romberg tableau converged cleanly to machine precision; a larger residual (say $0.05$) warns you that the integrand is sharply kinked, highly oscillatory, or passing near a vertical asymptote and would benefit from splitting the integration interval at the kink.

What happens if you accidentally ask the calculator to integrate right onto or across a pole where the area is infinite? Consider integrating the rectangular hyperbola $f(x) = 1/x$ all the way down to the vertical asymptote at $a = 0$:

$$\int_0^1 \frac{1}{x} \, dx = [\ln x]_0^1 = 0 - (-\infty) = +\infty$$

As soon as the Romberg engine samples the left endpoint $x = 0$, the SC-32 hardware catches the division by zero, halts the trapezoidal loop immediately, displays **`Error 02: DIVIDE BY 0`** on the status line, and leaves your stack registers intact. A single tap of `{{key:C}}` clears the error banner so you can adjust the lower bound away from the singularity (for instance, integrating from $a = 1$ to $b = e$ to recover $\ln e = 1.0000$).

### Post-Integration Stack Contents & Display-Controlled Tolerance

Where do your integration limits go after `{{key:∫}}` finishes? Following the classic HP-34C and HP-32SII quadrature architecture (Chapter 15 and Appendix B of the *HP-32SII Owner's Manual*), the SC-32 does not discard your interval endpoints. Instead, it organizes all four stack registers into a structured **Post-Integration Audit & Chaining Frame** that leaves the integral, its uncertainty bound, and both limits right at your fingertips:

| Stack Register | Post-`{{key:∫}}` Contents | Engineering Purpose & Chaining Workflow |
| :---: | :--- | :--- |
| **Register $X$** | **Certified Definite Integral ($I = \int_a^b f(x)\,dx$)** | The final Richardson-extrapolated quadrature result, ready for immediate arithmetic scaling or storage. |
| **Register $Y$** | **Estimated Quadrature Uncertainty ($\pm\varepsilon$)** | Upper bound on absolute truncation error $\max(\lvert R(k,m) - R(k,m-1) \rvert)$. Swap via `{{key:x⇄y}}` to audit convergence. |
| **Register $Z$** | **Upper Limit of Integration ($b$)** | Preserves the upper endpoint $b$ so multi-segment piecewise integrals $[a, b] \to [b, c]$ can be chained without re-typing $b$. |
| **Register $T$** | **Lower Limit of Integration ($a$)** | Preserves the lower endpoint $a$ at the top of the stack for interval verification. |

That register layout is a gift whenever you integrate a piecewise physical waveform—such as a multi-stage rocket burn or an AC voltage wave whose peaks are clipped flat at angle $\theta_c$, as we will analyze shortly for an overdriven sinusoid. Once you finish integrating the first segment over $[a, b]$, the upper endpoint $b$ is already waiting in Register $Z$. Rolling the stack down twice (`{{key:R↓}} {{key:R↓}}`) drops $b$ straight into Register $X$; typing the next upper endpoint $c$ automatically lifts $b$ into Register $Y$, staging $[b, c]$ for the second `{{key:∫}}` pass without ever re-typing $b$.

Just as thoughtfully, the SC-32 adapts its quadrature work effort to the precision you actually need. Imagine you are in a wind tunnel integrating an empirical aerodynamic drag curve whose pressure sensors are only accurate to three significant figures ($C_D \approx 0.34 \pm 0.01$). Forcing the quadrature engine to refine that noisy empirical curve to twelve decimal places would waste time chasing phantom digits. Following William Kahan's display-coupled stopping rule {{cite:kahan1979}}, the SC-32 links the Romberg convergence tolerance $\varepsilon_{\text{rel}}$ to your active display setting. In **`{{key:ALL}}` mode**, the Romberg tableau refines all the way down to machine convergence ($\varepsilon_{\text{rel}} = 10^{-11}$, absolute floor $10^{-13}$), delivering 11 to 12 certified digits. When you switch to **`{{key:FIX}} n`, `{{key:SCI}} n`, or `{{key:ENG}} n` mode**, the calculator scales its adaptive stopping threshold to $\varepsilon_{\text{rel}} = \max(10^{-11}, 10^{-\max(5, n+3)})$—finishing even faster on rough field curves while **still depositing the exact numerical truncation bound $\pm\varepsilon$ into Register $Y$** so you can always see how many digits are mathematically certified.

---

## Numerical Derivatives and Romberg Integrals Across Physics and Engineering

Numerical integration of non-linear rate equations (such as variable suspension restoring force $F(x) = 2500x + 40000x^3$ or aerodynamic drag) on algebraic calculators requires navigating modal sub-menus and entering multi-argument formula strings with nested parentheses and comma-delimited bounds:

$$\operatorname{fnInt}\!\left(2500x + 40000x^3,\, x,\, 0,\, 0.15\right)$$
If an engineer misplaces a parenthesis or comma delimiter across a nested integrand, the evaluation fails with a syntax error or returns a single scalar approximation with no indication of the truncation uncertainty {{cite:brent1973}}.

The SC-32 executes Adaptive Romberg Quadrature (`{{key:∫}}`) by combining deterministic postfix equation execution with automated Richardson extrapolation {{cite:romberg1955}}. The user defines the integrand directly in RPN, sets the limits $a$ and $b$ onto the stack, and presses `{{key:∫}}`. The dual-core engine evaluates step sizes dynamically, eliminates low-order truncation error via $O(h^4) \to O(h^6) \to O(h^8)$ tableau refinement, and returns the certified integral into Register $X$ while depositing the estimated absolute error directly into Register $Y$ for instant stack inspection.

---

### Mechanical Work, Centroids & Definite Polynomial Integrals

Let us begin with five physical accumulation investigations—compressing a rally-car coil spring, absorbing a lightning strike in a substation arrester, holding back a reservoir behind a parabolic dam gate, balancing a tapered structural spar, and measuring laminar flow through a pipe—where we can watch Adaptive Romberg Quadrature (`{{key:∫}}`) converge and then cross-check its answer against closed-form antiderivatives on the 4-level stack.

If you equip a desert rally car with a simple linear coil spring ($F = k_1 x$), soft coils that ride plushly over small washboard ripples will slam violently into the bump stops on a hard landing, whereas stiff coils will rattle the chassis over every pebble. Suspension engineers solve this dilemma by winding **progressive-rate springs** whose coils bind closer together under compression, adding a cubic stiffening term $F(x) = k_1 x + k_2 x^3$. With linear stiffness $k_1 = 2,500\text{ N/m}$ and cubic stiffening $k_2 = 40,000\text{ N/m}^3$, how much mechanical energy (work $W = \int F(x)\,dx$) is stored in the steel when the suspension compresses from $x = 0$ to $x = 0.15\text{ m}$? Analytically, integrating across the stroke gives:
$$W = \int_0^{0.15} (2500 x + 40000 x^3) \, dx = \left[ 1250 x^2 + 10000 x^4 \right]_0^{0.15}$$
$$W = 1250(0.0225) + 10000(0.00050625) = 28.125 + 5.0625 = \mathbf{33.1875\text{ Joules}}$$

Once the progressive restoring-force curve `X 2500 {{key:×}} X 3 {{key:yˣ}} 40000 {{key:×}} {{key:+}}` is stored in `{{key:EQN}}`, pushing the compression bounds `0 {{key:ENTER}} 0.15` onto the stack and invoking `{{key:∫}} X` integrates the non-linear stiffness directly across the stroke:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}} 0.15` | $0.0000$ | $0.0000$ | $0.0000$ | $0.1500$ | Limits $a=0, b=0.15$ |
| 2 | `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$3.55 \times 10^{-12}$** | **$33.187500000$** | Work $W$ in Joules |

We can cross-check the quadrature result against the closed-form antiderivative $1250x^2 + 10000x^4$ right on the stack by squaring and raising the $0.15\text{ m}$ stroke via {{res:sc32_08_calc_01:keys}}, which accumulates the linear and cubic potential-energy contributions to confirm $\mathbf{{{res:sc32_08_calc_01:value}}\text{ Joules}}$. Notice why Romberg quadrature hits all 10 decimal digits of $33.1875\text{ J}$ on its very first Richardson extrapolation column $R(1, 1)$: because Simpson's parabolic column ($j = 1$, error order $\mathcal{O}(h^4)$) is mathematically exact for every cubic polynomial, halving the interval once from $h_0 = 0.15\text{ m}$ to $h_1 = 0.075\text{ m}$—just like inserting the midpoint column in our **84 mm Fraction Towers** step model—cancels the parabolic and cubic meniscus error to zero.

From mechanical energy stored in steel coils, let us turn to electrical charge surging through a power grid. When a bolt of lightning strikes an overhead transmission tower, the current spikes almost instantaneously to $I_0 = 10,000\text{ A}$ and then decays exponentially as $I(t) = I_0 e^{-t/\tau}$ with a time constant of $\tau = 50\,\mu\text{s}$ ($5.0 \times 10^{-5}\text{ s}$). Whether the substation's surge arrester survives the strike depends not merely on the peak amperage, but on the total electrical charge $Q = \int I(t)\,dt$ (in Coulombs) that the metal-oxide blocks must conduct to ground. Integrating the surge pulse over five time constants from $t = 0$ to $t = 250\,\mu\text{s}$ ($2.5 \times 10^{-4}\text{ s}$) captures $1 - e^{-5} \approx 99.33\%$ of the total lightning impulse:
$$Q = \int_0^{2.5 \cdot 10^{-4}} 10000 e^{-t / 5 \cdot 10^{-5}} \, dt = 10000(5 \cdot 10^{-5}) [1 - e^{-5}] = 0.50 [1 - 0.006738] = \mathbf{0.496631\text{ Coulombs}}$$

After entering the exponential surge current `T 5 {{key:E}} 5 {{key:+/-}} {{key:÷}} {{key:+/-}} {{key:eˣ}} 10000 {{key:×}}` into the equation bank, loading the five-time-constant window `0 {{key:ENTER}} 2.5 {{key:E}} 4 {{key:+/-}}` and executing `{{key:∫}} T` sweeps the decaying tail:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}} 2.5 {{key:E}} 4 {{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.000250$ | Limits $a=0, b=250\,\mu\text{s}$ |
| 2 | `{{key:∫}} T` | $0.0000$ | $0.0000$ | **$1.12 \times 10^{-11}$** | **$0.496631098$** | Charge $Q$ in Coulombs |

Evaluating the closed-form exponential integral $I_0 \tau (1 - e^{-5})$ from the inside out via {{res:sc32_08_calc_02:keys}} forms the surviving tail fraction $e^{-5}$ first, subtracts it from unity, and scales by the $0.50\text{ C}$ asymptotic charge product $I_0\tau$ to verify $\mathbf{{{res:sc32_08_calc_02:value}}\text{ C}}$.

Integrals are equally indispensable when geometry and pressure vary simultaneously across space. Picture a vertical steel floodgate set into a parabolic canyon spillway ($y = 0.5 x^2$) holding back $4.0\text{ m}$ of reservoir water. Calculating the total horizontal water force pushing against the gate involves a tug-of-war between two changing geometries: near the water's surface ($y = 4.0\text{ m}$), the parabolic gate is widest ($w(y) = 2x = \sqrt{8y}$), but the water depth $h(y) = 4 - y$ and hydrostatic pressure $\rho g h(y)$ are nearly zero; down near the riverbed ($y = 0$), the water pressure is crushing, but the parabolic arch narrows to a point. Slicing the gate into horizontal ribbons of height $dy$ and integrating pressure times area across $y \in [0, 4.0]\text{ m}$ (with $\rho = 1,000\text{ kg/m}^3$ and $g = 9.81\text{ m/s}^2$) reveals the exact thrust the gate hinges must withstand:
$$F = \rho g \int_0^4 (4 - y) \sqrt{8y} \, dy = 9810 \sqrt{8} \int_0^4 (4 y^{1/2} - y^{3/2}) \, dy$$
$$\int_0^4 (4 y^{1/2} - y^{3/2}) \, dy = \left[ \frac{8}{3} y^{3/2} - \frac{2}{5} y^{5/2} \right]_0^4 = \frac{8}{3}(8) - \frac{2}{5}(32) = \frac{64}{3} - \frac{64}{5} = \frac{128}{15} \approx 8.533333$$
$$F = 9810 \times 2.828427 \times 8.533333 = \mathbf{236,778.5\text{ Newtons}} = 236.78\text{ kN}$$

Programming the depth-weighted hydrostatic ribbon integrand `Y 8 {{key:×}} {{key:√x}} 4 Y {{key:-}} {{key:×}} 9810 {{key:×}}` into `{{key:EQN}}`, setting the vertical depth span `0 {{key:ENTER}} 4`, and pressing `{{key:∫}} Y` integrates the fractional-power profile in a single pass:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}} 4` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | Gate depth interval $[0, 4]$ |
| 2 | `{{key:∫}} Y` | $0.0000$ | $0.0000$ | **$4.18 \times 10^{-10}$** | **$236778.4720$** | Hydrostatic Force in N |

The stack resolves to **$F = 236.78\text{ kN}$**—equivalent to the weight of 24 metric tons pressing horizontally against the gate.

What if an engineering calculation requires the ratio of *two* definite integrals? Suppose you are balancing a $2.0\text{-meter}$ centrifugally cast turbine spar whose linear mass density thickens quadratically from root to tip according to $\lambda(x) = 1.5 + 0.8 x^2\text{ kg/m}$. If you place a fulcrum at the geometric midpoint ($x = 1.0\text{ m}$), the heavy tip will immediately tip the rod over. To find the true balance point (the center of mass $\bar{x} = M_x / M$), we evaluate two definite integrals on the stack—first integrating $\lambda(x)$ to find the total mass $M$ (and storing it in variable `A`), then integrating the lever-arm moment $x\,\lambda(x)$ to find $M_x$ and dividing by `{{key:RCL}} A`:
$$M = \int_0^2 (1.5 + 0.8 x^2) \, dx = \left[ 1.5x + \frac{0.8}{3} x^3 \right]_0^2 = 3.0 + \frac{6.4}{3} = \frac{15.4}{3} \approx 5.133333\text{ kg}$$
$$M_x = \int_0^2 x (1.5 + 0.8 x^2) \, dx = \int_0^2 (1.5x + 0.8x^3) \, dx = \left[ 0.75 x^2 + 0.2 x^4 \right]_0^2 = 3.0 + 3.2 = 6.20\text{ kg}\cdot\text{m}$$
$$\bar{x} = \frac{M_x}{M} = \frac{6.20}{5.133333} = \frac{6.20 \times 3}{15.4} = \frac{93}{77} \approx \mathbf{1.207792\text{ meters}}$$

Using `X {{key:x²}} 0.8 {{key:×}} 1.5 {{key:+}}` for the linear mass density $M$ and appending `X {{key:×}}` (`X {{key:x²}} 0.8 {{key:×}} 1.5 {{key:+}} X {{key:×}}`) for the first moment $M_x$, the two Romberg passes chain directly through Variable `A`:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}} 2` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Integration limits $[0, 2]$ |
| 2 | `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$3.24 \times 10^{-11}$** | **$5.133333$** | Romberg evaluates rod mass $M$ (kg) |
| 3 | `{{key:STO}} A` | $0.0000$ | $0.0000$ | $3.24 \times 10^{-11}$ | $5.133333$ | Store total mass $M$ in Variable A |
| 4 | `0 {{key:ENTER}} 2` | $3.24 \times 10^{-11}$ | $5.133333$ | $0.0000$ | $2.0000$ | Reload integration limits $[0, 2]$ |
| 5 | `{{key:∫}} X` | $3.24 \times 10^{-11}$ | $5.133333$ | **$1.87 \times 10^{-11}$** | **$6.200000$** | Romberg evaluates first moment $M_x$ |
| 6 | `{{key:RCL}} A {{key:÷}}` | $5.133333$ | $5.133333$ | $1.87 \times 10^{-11}$ | **$1.207792$** | Centroid position $\bar{x} = M_x / M$ (meters) |

Register $X$ settles at **$\bar{x} = 1.207792\text{ meters}$**—shifted $20.8\%$ past the geometric midpoint toward the denser tip.

The same radial weighting principle governs fluid flow through pipes and blood vessels. When a viscous fluid flows smoothly through a circular pipe of radius $R = 0.05\text{ m}$ ($50\text{ mm}$), the outermost boundary layer clings motionless to the pipe wall ($v(R) = 0$) while the central core glides fastest at $v_{\max} = 1.20\text{ m/s}$, sculpting a parabolic velocity profile $v(r) = v_{\max}(1 - r^2/R^2)$. Because velocity changes continuously with radius $r$, we cannot simply multiply pipe area by centerline speed; instead, we slice the flow into concentric cylindrical shells of circumference $2\pi r$ and thickness $dr$, and integrate across $r \in [0, R]$:
$$Q = 2\pi \int_0^R v(r) r \, dr = 2\pi v_{\max} \int_0^R \left( r - \frac{r^3}{R^2} \right) dr = 2\pi(1.20) \left[ \frac{R^2}{2} - \frac{R^2}{4} \right] = \frac{1}{2} \pi R^2 v_{\max}$$
$$Q = 0.5 \times \pi \times (0.05^2) \times 1.20 = 0.5 \times \pi \times 0.0025 \times 1.20 = \mathbf{4.712389 \times 10^{-3}\text{ m}^3/\text{s}} = \mathbf{4.712389\text{ L/s}}$$

Entering the cylindrical-shell integrand $2\pi r v(r)$ into `{{key:EQN}}` as `R {{key:x²}} 0.0025 {{key:÷}} 1 {{key:x⇄y}} {{key:-}} 1.2 {{key:×}} R {{key:×}} 2 {{key:×}} {{key:π}} {{key:×}}` and integrating from the pipe centerline to the inner wall (`0 {{key:ENTER}} 0.05`) sums the concentric flow shells:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}} 0.05` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0500$ | Pipe radial integration limits $[0, R]$ |
| 2 | `{{key:∫}} R` | $0.0000$ | $0.0000$ | **$1.45 \times 10^{-12}$** | **$0.004712$** | Discharge $Q$ in $\text{m}^3/\text{s}$ |
| 3 | `1000 {{key:×}}` | $0.0000$ | $0.0000$ | $1.45 \times 10^{-12}$ | **$4.712389$** | Convert volumetric flow to Liters/second |

This confirms a final discharge of **$Q = 4.712389\text{ L/s}$**—demonstrating Hagen-Poiseuille's classic theorem that mean laminar pipe velocity equals exactly half the centerline maximum ($v_{\text{avg}} = \frac{1}{2}v_{\max}$), verifiable in closed form via `0.05 {{key:x²}} {{key:π}} {{key:×}} 1.2 {{key:×}} 2 {{key:÷}} 1000 {{key:×}}` ($\mathbf{4.712389\text{ L/s}}$).

> **Cardiovascular Physiology & Poiseuille's Fourth-Power Law ($R^4$):** Because the centerline velocity $v_{\max} = \frac{\Delta P}{4\mu L}R^2$ is itself proportional to $R^2$, substituting $v_{\max}$ into $Q = \frac{1}{2}\pi R^2 v_{\max}$ reveals the full Hagen-Poiseuille law $Q = \frac{\pi \Delta P}{8\mu L}R^4$: **laminar flow conductance scales with the fourth power of vessel radius ($R^4$)**. In human arterioles and coronary arteries, a seemingly modest $16\%$ radial constriction ($0.84\,R$) cuts blood flow in half (`0.84 {{key:x²}} {{key:x²}}` $\implies \mathbf{0.4979}$), whereas a $19\%$ smooth-muscle vasodilation ($1.19\,R$) during exercise doubles oxygen delivery to working muscles (`1.19 {{key:x²}} {{key:x²}}` $\implies \mathbf{2.0053}$).

---

### Signal RMS Power, Catenary Spans & Polar Governor Kinematics

Now we step beyond pure polynomials into trigonometric, hyperbolic, and polar kinematics—evaluating the true heating power of a clipped AC waveform, the sag and arc length of a suspended high-voltage transmission cable, and the kinetic energy of a whirling steam-engine flyweight.

When an overdriven audio amplifier or a protective metal-oxide varistor (MOV) surge clamp chops the top and bottom peaks off a $60\text{ Hz}$ AC line waveform $v(\theta) = V_p \sin\theta$ ($V_p = 170.0\text{ V}$, normal $V_{\text{rms}} = 170/\sqrt{2} = 120.21\text{ V}$) at a flat ceiling of $V_c = 0.80 V_p = 136.0\text{ V}$, what is the true Root-Mean-Square (RMS) voltage delivered to the load? In radians mode (`{{key:RAD}}`), the wave rises sinusoidally until it hits the clamp at phase angle $\theta_c = \arcsin(0.80) \approx 0.927295\text{ rad}$, and then rides flat at $136.0\text{ V}$ until the quarter-wave peak $\pi/2$. Integrating $(170\sin\theta)^2$ across the rising edge $[0, \theta_c]$ via `{{key:∫}} X` and adding the rectangular plateau area $136^2(\pi/2 - \theta_c)$ right on the stack reveals the exact RMS voltage:
$$\langle v^2 \rangle = \frac{2}{\pi} \left[ \int_0^{\theta_c} (170 \sin \theta)^2 d\theta + \int_{\theta_c}^{\pi/2} 136^2 d\theta \right]$$
$$\int_0^{\theta_c} 28,900 \sin^2 \theta \, d\theta = 28,900 \left[ \frac{\theta}{2} - \frac{\sin 2\theta}{4} \right]_0^{\theta_c} = 28,900 [0.463648 - 0.240000] = 6,463.4190\text{ V}^2\cdot\text{rad}$$
$$\int_{\theta_c}^{\pi/2} 136^2 \, d\theta = 18,496 \left(\frac{\pi}{2} - \arcsin(0.80)\right) = 18,496(0.643501) = 11,902.1965\text{ V}^2\cdot\text{rad}$$
$$\langle v^2 \rangle = \frac{2}{\pi}(6,463.4190 + 11,902.1965) = \frac{2}{\pi}(18,365.6155) = 11,691.9125\text{ V}^2$$
$$V_{\text{rms}} = \sqrt{11,691.9125} = \mathbf{108.1292\text{ Volts}}$$

Programming the rising-edge squared voltage integrand into `{{key:EQN}}` as `X {{key:SIN}} 170 {{key:×}} {{key:x²}}` and engaging `{{key:RAD}}` mode lets us integrate the rising sinusoid and add the clipped plateau directly on the stack:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:RAD}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Radian mode engaged for trig calculus |
| 2 | `0 {{key:ENTER}} 0.8 {{key:ASIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.927295$ | Integration bounds $[0, \theta_c]$ via $\theta_c = \arcsin(0.8)$ |
| 3 | `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$3.12 \times 10^{-10}$** | **$6463.4190$** | Integral of $(170\sin\theta)^2$ over rising edge |
| 4 | `0.8 {{key:ASIN}} {{key:π}} 2 {{key:÷}} {{key:x⇄y}} {{key:-}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | $0.643501$ | Clipped interval $(\pi/2 - \theta_c)$; rising integral stays in $Y$ |
| 5 | `136 {{key:x²}} {{key:×}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | **$11902.1965$** | Flat clamped plateau contribution |
| 6 | `{{key:+}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | **$18365.6155$** | Total quarter-cycle energy sum |
| 7 | `2 {{key:×}} {{key:π}} {{key:÷}} {{key:√x}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | **$108.1292$** | Mean square normalized and root taken |

The calculation yields **$V_{\text{rms}} = 108.1292\text{ Volts}$** (compared to $120.21\text{ V}_{\text{rms}}$ unclipped, showing why true-RMS digital multimeters are essential on non-sinusoidal MOV-clamped lines).

From the alternating current flowing *inside* a transmission line, let us step back and look at the physical curve of the heavy cable itself hanging between two steel towers. Galileo once conjectured that a heavy chain hanging between two supports traces a parabola, but in 1691 Jakob and Johann Bernoulli, Gottfried Wilhelm Leibniz, and Christiaan Huygens proved that gravity pulls a flexible cable into a hyperbolic cosine **catenary**, $y(x) = a\cosh(x/a)$. When power-grid engineers string a high-voltage aluminum-conductor steel-reinforced (ACSR) transmission cable across a $200.0\text{-meter}$ river span ($x \in [-100, +100]\text{ m}$) with catenary tension-to-weight parameter $a = 800.0\text{ m}$, they must compute both the exact length of cable to reel out ($L = \int_{-100}^{100} \sqrt{1 + [y'(x)]^2}\,dx$) and the mid-span sag $\Delta y$ so the line maintains safe ground clearance:
$$\sqrt{1 + \sinh^2(x/800)} = \cosh(x / 800)$$
$$L = \int_{-100}^{100} \cosh(x / 800) \, dx = 2 \times 800 \sinh(100 / 800) = 1600 \sinh(0.125) = 1600(0.12532561) = \mathbf{200.5210\text{ meters}}$$
Meanwhile, the mid-span cable sag evaluates to $\Delta y = y(100) - y(0) = 800[\cosh(0.125) - 1] = 800[1.0078229 - 1] = \mathbf{6.2583\text{ meters}}$. Defining the hyperbolic differential arc-length integrand `X 800 {{key:÷}} {{key:HYP}} {{key:COS}}` in `{{key:EQN}}` lets us integrate across the symmetric river span `100 {{key:+/-}} {{key:ENTER}} 100` and then evaluate the mid-span sag directly on the stack:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `100 {{key:+/-}} {{key:ENTER}} 100` | $0.0000$ | $0.0000$ | $-100.0000$ | $100.0000$ | Tower span interval $[-100, +100]$ |
| 2 | `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$8.55 \times 10^{-11}$** | **$200.5210$** | Conductor total arc length (meters) |
| 3 | `100 {{key:ENTER}} 800 {{key:÷}} {{key:HYP}} {{key:COS}}` | $8.55 \times 10^{-11}$ | $8.55 \times 10^{-11}$ | $200.5210$ | $1.007823$ | Dimensionless catenary height ratio |
| 4 | `1 {{key:-}} 800 {{key:×}}` | $8.55 \times 10^{-11}$ | $8.55 \times 10^{-11}$ | $200.5210$ | **$6.2583$** | Conductor mid-span sag $\Delta y$ (meters) |

Register $X$ settles at conductor length **$L = 200.5210\text{ m}$** and mid-span sag **$\Delta y = 6.258\text{ m}$** (note that in Step 4, because `800 {{key:÷}}` saved $800$ in `LASTX` before `{{key:HYP}} {{key:COS}}` overwrote `LASTX` with $0.125$, you can also inspect the dimensionless ratio $d/a = 0.125$ at any time).

Just as arc length combines horizontal and vertical differentials via Pythagoras ($\sqrt{1 + [y'(x)]^2}$), rotational kinematics in polar coordinates combines radial derivative speed and tangential speed on the stack. Imagine a $4.0\text{-kilogram}$ brass flyweight inside a mechanical speed governor spinning at a constant angular velocity of $\omega = 40.0\text{ rad/s}$ while sliding along a cam slot whose radius varies with angle as $r(\theta) = 0.15 + 0.05\sin(2\theta)\text{ meters}$. Because the flyweight is simultaneously whirling azimuthally at speed $v_\theta = r\omega$ and sliding radially outward at speed $\dot{r} = \omega\frac{dr}{d\theta}$, its total velocity squared in polar coordinates is the Pythagorean sum $v^2 = \dot{r}^2 + (r\omega)^2$. Working in `{{key:RAD}}` mode, let us evaluate $\frac{dr}{d\theta}$ at $\theta = \pi/6\text{ rad}$ ($30^\circ$) and combine both orthogonal velocity components right on the stack to find the flyweight's kinetic energy:
$$\frac{dr}{d\theta} \approx \frac{r(\theta + h) - r(\theta - h)}{2h} = 2(0.05) \cos(2\theta) = 0.10 \cos\left(\frac{\pi}{3}\right) = 0.050\text{ m/rad}$$
$$\dot{r} = 40.0 \times 0.050 = 2.00\text{ m/s}$$
$$r\left(\frac{\pi}{6}\right) = 0.15 + 0.05 \sin\left(\frac{\pi}{3}\right) = 0.15 + 0.043301 = 0.193301\text{ m} \implies v_\theta = r \omega = 7.732051\text{ m/s}$$
$$v^2 = \dot{r}^2 + v_\theta^2 = 2.0^2 + (7.732051)^2 = 4.00 + 59.7846 = 63.7846\text{ m}^2/\text{s}^2$$
$$E_k = \frac{1}{2} m v^2 = \frac{1}{2}(4.0)(63.7846) = \mathbf{127.5692\text{ Joules}}$$

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:RAD}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Verify radian mode |
| 2 | `{{key:π}} 6 {{key:÷}} {{key:STO}} A` | $0.0000$ | $0.0000$ | $0.0000$ | $0.523599$ | Angle $\theta = \pi/6$ stored in Var A |
| 3 | `2 {{key:×}} {{key:COS}} 0.1 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.050000$** | Radial derivative $dr/d\theta = 0.10\cos(2\theta)$ |
| 4 | `40 {{key:×}} {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$4.000000$** | Radial velocity squared $\dot{r}^2 = (2.0)^2$ |
| 5 | `{{key:RCL}} A 2 {{key:×}} {{key:SIN}} 0.05 {{key:×}} 0.15 {{key:+}} 40 {{key:×}}` | $0.0000$ | $0.0000$ | $4.000000$ | **$7.732051$** | Tangential speed $v_\theta = r \omega$; $\dot{r}^2$ stays in $Y$ |
| 6 | `{{key:x²}} {{key:+}} 2 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$127.569226$** | Kinetic energy $0.5 \times 4 \times (\dot{r}^2 + v_\theta^2)$ (J) |

The stack resolves to flyweight kinetic energy **$E_k = 127.5692\text{ Joules}$**, orthogonally summing the radial and azimuthal velocity components in Polar kinematics without intermediate scratch notes.

> **James Watt's Flyball Governor & Negative-Feedback Control:** Patented by James Watt in 1788 to regulate steam engines, the centrifugal flyball governor is the mechanical ancestor of modern negative-feedback control theory (later analyzed mathematically by James Clerk Maxwell in his 1868 paper *"On Governors"*). As engine speed $\omega$ rises, outward centrifugal acceleration swings the heavy flyweights to a larger radius $r(\theta)$, lifting a collar linkage that throttles down the steam intake valve; when load increases and $\omega$ drops, gravity pulls the flyweights inward, opening the throttle to restore equilibrium speed automatically.

---

### Reactor Flux Profiles & Relativistic Worldlines

In nuclear engineering and relativistic astrodynamics, integrals govern how neutron flux distributes thermal power across a reactor core and how shipboard proper time maps to Earth coordinate time during near-lightspeed travel.

Inside a cylindrical heavy-water nuclear reactor core of radius $R = 1.80\text{ m}$ and height $H = 3.60\text{ m}$, thermal neutrons diffuse outward from the fuel assemblies and vanish at the outer boundary, shaping the radial neutron flux into Friedrich Wilhelm Bessel's zero-order standing wave $\phi(r) = \phi_0 J_0(2.405 r / R)$. Although the center of the core runs hottest at $q_0''' = 120.0\text{ MW/m}^3$, the outer rings carry much greater cylindrical circumference $2\pi r$. To determine the total thermal megawatts the primary coolant loop must remove, we integrate $2\pi r q_0''' J_0(2.405 r / R)$ from the core axis ($r = 0$) to the vessel wall ($r = R$) and multiply by the axial cosine peaking factor $2/\pi$:
$$P'_{\text{th}} = \int_0^R 2\pi r q_0''' J_0(2.405 r / R) \, dr$$
Using $\int_0^R r J_0(\alpha r) dr = \frac{R}{\alpha} J_1(\alpha R) = \frac{1.80^2}{2.405} J_1(2.405) \approx \frac{3.24}{2.405}(0.519147) \approx 0.699411\text{ m}^2$, the linear power density is $P'_{\text{th}} = 2\pi(120.0)(0.699411) \approx 527.350\text{ MW/m}$, and scaling by the fundamental axial cosine chopping factor $2/\pi \approx 0.636620$ gives the total thermal power output:
$$P_{\text{th}} = P'_{\text{th}} \times H \times \frac{2}{\pi} = 527.350 \times 3.60 \times 0.636620 \approx \mathbf{1,208.587\text{ MW}}_{\text{th}}$$

Representing the cylindrical neutron-diffusion eigenmode $J_0(u) \approx 1 - \frac{1}{4}u^2 + \frac{1}{64}u^4 = u^2(\frac{1}{64}u^2 - \frac{1}{4}) + 1$ ($u = 1.3361 R$) in nested Horner form as `R 1.3361 {{key:×}} {{key:x²}} {{key:ENTER}} {{key:ENTER}} 0.015625 {{key:×}} 0.25 {{key:-}} {{key:×}} 1 {{key:+}} R {{key:×}} 2 {{key:×}} {{key:π}} {{key:×}}` in `{{key:EQN}}` allows direct radial quadrature from the core centerline to the extrapolated boundary `0 {{key:ENTER}} 1.8` ($X = 1.8000$). Executing `{{key:∫}} R` ($Y = 1.65\times 10^{-10},\; X = 4.394539$) integrates the effective radial area $2\pi\int_0^R r J_0(\alpha r)\,dr = 4.394539\text{ m}^2$ in $X$ with truncation residual $1.65 \times 10^{-10}$ in $Y$, and scaling by peak volumetric power density and axial cosine chopping factor (`120 {{key:×}} 3.6 {{key:×}} 2 {{key:×}} {{key:π}} {{key:÷}}`) yields the total reactor thermal rating $\mathbf{1,208.5866\text{ MW}_{\text{th}}}$ (**$P_{\text{th}} = 1,208.59\text{ MW}_{\text{th}}$**).

Now imagine harnessing nuclear propulsion to send an interstellar probe away from Earth under a continuous $1\,g$ thrust ($g = 9.81\text{ m/s}^2$ as felt by the crew's feet on the deck) for $\tau = 1.0\text{ year}$ ($31,557,600\text{ s}$) of shipboard proper time. In Newtonian mechanics, a year at $1\,g$ would accelerate the ship to $1.033\,c$, breaking the cosmic speed limit! In Einstein's special relativity, the ship's rapidity $\eta = g\tau/c = 1.032650$ grows linearly with proper time while the Lorentz time-dilation factor stretches as $\gamma(\tau') = \cosh(g\tau'/c)$. How much time $t$ elapses on Mission Control's clocks back on Earth during that single year of crew time? Integrating the Lorentz factor across $\tau' \in [0, 1.0]\text{ year}$ along the Rindler worldline gives:
$$t = \int_0^\tau \cosh\left(\frac{g \tau'}{c}\right) d\tau' = \frac{c}{g} \sinh\left(\frac{g \tau}{c}\right) \implies \mathbf{t = 1.1874\text{ years}}$$

Programming `T 1.032650 {{key:×}} {{key:HYP}} {{key:COS}}` into `{{key:EQN}}` and integrating over `0 {{key:ENTER}} 1` ($X = 1.0000$) via `{{key:∫}} T` ($Y = 2.31\times 10^{-12},\; X = 1.187445$) yields the elapsed Earth coordinate time $t = \mathbf{1.1874\text{ years}}$. Notice how the closed-form verification on the stack exploits `{{key:LASTX}}`: evaluating rapidity $\eta = g\tau/c$ via `9.81 {{key:ENTER}} 31557600 {{key:×}} 299792458 {{key:÷}}` ($X = 1.032648$) and taking `{{key:HYP}} {{key:SIN}}` ($X = 1.226215$) preserves $\eta$ inside `LASTX`, so `{{key:LASTX}} {{key:÷}}` ($X = 1.187445$) forms $\sinh(\eta)/\eta$ without re-computing $g/c$.

---

### Nonlinear Field Energy, Photonic Waveguides & Derivative Sprints

Our final three investigations tackle a famous solid-state electronics trap—voltage saturation in ferroelectric capacitors—alongside optical mode confinement inside a semiconductor laser waveguide and a high-speed central-difference derivative benchmark.

In introductory physics, every capacitor has a fixed value $C_0$ and stores energy $W = \frac{1}{2}C_0 V^2$. In real-world high-voltage design, however, compact Class-II ceramic capacitors made from ferroelectric barium titanate ($\text{BaTiO}_3$, such as X7R dielectrics) suffer electric-dipole domain-wall pinning under high DC bias fields: their differential capacitance $C(V) = dQ/dV$ droops as $C(V) = C_0(1 - \alpha V^2)$, where $C_0 = 10\,\mu\text{F}$ and $\alpha = 10^{-6}\text{ V}^{-2}$. If you charge this capacitor to $500\text{ V}$ to fire a pulsed xenon flashlamp, how much energy $W = \int_0^{500} C(V)V\,dV$ is actually stored in the dielectric?
$$W = \int_0^{500} C_0 (V - \alpha V^3) \, dV = C_0 \left[ \frac{V^2}{2} - \frac{\alpha V^4}{4} \right]_0^{500} = 10^{-5} [125,000 - 15,625] = \mathbf{1.09375\text{ Joules}}$$
A naive linear $W = \frac{1}{2} C_0 V^2$ assumption overestimates stored pulse energy by $12.5\%$ ($1.25\text{ J}$ vs. $1.09375\text{ J}$) {{cite:horowitz2015}}. Programming the differential work integrand `V 3 {{key:yˣ}} 1 {{key:E}} 6 {{key:+/-}} {{key:×}} V {{key:x⇄y}} {{key:-}} 10 {{key:E}} 6 {{key:+/-}} {{key:×}}` into `{{key:EQN}}` and integrating across `0 {{key:ENTER}} 500` ($X = 500.0000$) via `{{key:∫}} V` ($Y = 1.42\times 10^{-13},\; X = 1.0938$) captures the exact recoverable pulse energy $W = \mathbf{1.09375\text{ Joules}}$, which matches the analytical stack verification (`500 {{key:x²}} 2 {{key:÷}}` ($Y = 1.0938,\; X = 125000.0$) followed by `500 {{key:ENTER}} 4 {{key:yˣ}} 1 {{key:E}} 6 {{key:+/-}} {{key:×}} 4 {{key:÷}} {{key:-}}` ($X = 109375.0$) and `10 {{key:E}} 6 {{key:+/-}} {{key:×}}` ($X = 1.0938$)).

Once that capacitor fires the laser's pump current, how tightly is the resulting optical wave confined inside the laser's active layer? Inside a double-heterostructure semiconductor diode laser, the active quantum-well or slab core of half-width $d$ is sub-micron thin, so part of the guided optical wave $|E(x)|^2$ spills outward as an evanescent tail into the passive cladding layers. Because only the photons riding *inside* the active core $[-d, d]$ can stimulate new laser emission, photonics engineers must calculate the **optical mode confinement factor** $\Gamma$—the ratio of the core intensity integral to the total cross-sectional intensity integral:
$$\Gamma = \frac{\int_{-d}^d |E(x)|^2 \, dx}{\int_{-\infty}^\infty |E(x)|^2 \, dx} = \mathbf{0.8425} \quad (84.25\%\text{ optical confinement})$$
By integrating the optical field intensity over the active core $[-d, d]$ first, storing that core energy in Register `A` via `{{key:STO}} A`, integrating across the wide cladding domain $[-5d, 5d]$, and dividing via `{{key:RCL}} A {{key:x⇄y}} {{key:÷}}`, the stack yields the mode confinement factor directly:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1 {{key:+/-}} {{key:ENTER}} 1 {{key:∫}} E` | $0.0000$ | $0.0000$ | $1.25 \times 10^{-11}$ | $1.6850$ | Core field energy over $[-d, d]$ |
| 2 | `{{key:STO}} A` | $0.0000$ | $0.0000$ | $1.25 \times 10^{-11}$ | $1.6850$ | Core energy stored in register A |
| 3 | `5 {{key:+/-}} {{key:ENTER}} 5 {{key:∫}} E` | $1.25 \times 10^{-11}$ | $1.6850$ | $2.40 \times 10^{-11}$ | $2.0000$ | Total field energy over $[-5d, 5d]$ |
| 4 | `{{key:RCL}} A {{key:x⇄y}} {{key:÷}}` | $1.6850$ | $1.6850$ | $2.40 \times 10^{-11}$ | **$0.8425$** | Optical confinement factor $\Gamma = 84.25\%$ |

To close the chapter, suppose you are in a timed calculation sprint and need the instantaneous rate of change $f'(0)$ of an exponential growth curve $f(x) = e^{2x}$—whose analytical derivative is $f'(x) = 2 e^{2x} \implies f'(0) = 2.0$—using a central-difference step of $h = 10^{-5}$ ($2h = 0.00002$). To compute the symmetric central difference $\frac{e^{2h} - e^{-2h}}{2h}$ at $2h = 0.00002$ without re-keying the perturbation step, combine `{{key:ENTER}}` stack duplication with `{{key:LASTX}}` argument recovery: keying `0.00002 {{key:ENTER}} {{key:eˣ}} {{key:LASTX}} {{key:+/-}} {{key:eˣ}} {{key:-}} {{key:x⇄y}} {{key:÷}}` ($X = 2.000000$) duplicates $2h = 0.00002$ into Register $Y$, computes $e^{0.00002}$ while saving $0.00002$ in `LASTX`, recalls and negates `LASTX` to form $e^{-0.00002}$, subtracts the two exponentials, and swaps the waiting denominator $0.00002$ from $Y$ into $X$ for division—computing $f'(0) = \mathbf{2.000000}$ to 10 significant digits with `0.00002` typed only once. (Equivalently, using the hyperbolic identity $\frac{e^{2h} - e^{-2h}}{2h} = 2\,\frac{\sinh(2h)}{2h}$, keying `0.00002 {{key:HYP}} {{key:SIN}} {{key:LASTX}} {{key:÷}} 2 {{key:×}}` ($X = 2.000000$) recovers $2h$ directly from `LASTX` in just 7 keystrokes.)

---

## Further Exploration: Companion Workbooks & Applied Tie-Ins

> *For 27 additional worked engineering problems with full 4-register stack traces, see Chapter 8 of the [SC-32 Scientific Companion Problem & Casebook Workbook](../../curriculum/sc32-scientific-companion-workbook.md#chapter-08).*


To extend the Romberg quadrature and central-difference pipelines developed in this chapter into full multi-stage system designs and timed contest drills, consult the following companion volumes in the StackCalc documentation suite:

- **StackCalc Aerospace & Propulsion Casebook (Module 4: Trajectory & Thermal Protection Integrals):** Pairs the `{{key:SOLVE}}` root-finder from Chapter 7 with `{{key:∫}}` Romberg integration to determine burnout altitude, re-entry ablation heat load, and compressible Prandtl-Meyer expansion envelopes directly on the 4-level stack.
- **Timed STEM Competition & Science Sprint Workbook (Section D: Definite Integrals, Arc Lengths & Taylor Sensitivity):** Features 50 timed quadrature and central-difference speed drills demonstrating when 2-point Gauss-Legendre evaluation or a single Richardson extrapolation step $R(1,1) = (4R(1,0) - R(0,0))/3$ achieves contest-grade 3-significant-digit accuracy in under 8 seconds.

### Synthesis Challenge Problems

1. **Coupled Root-Finding & Quadrature (Escape-Velocity Burn Cutoff):** A thruster provides time-varying acceleration $a(t) = 12.0 e^{0.04 t} - 9.80665\text{ m/s}^2$. Use `{{key:∫}} T` to verify the net velocity gained over $t \in [0, 25]\text{ s}$, then use `{{key:LASTX}}` to evaluate the closed-form antiderivative $\frac{12.0}{0.04}(e^{0.04 t} - 1) - 9.80665\,t$ at $t = 25\text{ s}$ by typing `25` only once (`0.04 {{key:ENTER}} 25 {{key:×}} {{key:LASTX}} {{key:x⇄y}} {{key:eˣ}} 1 {{key:-}} 300 {{key:×}} {{key:x⇄y}} 9.80665 {{key:×}} {{key:-}}` $\to \mathbf{270.3183\text{ m/s}}$).
2. **Richardson $O(h^4)$ Derivative Extrapolation on the Stack:** Evaluate the central difference $D(h) = \frac{\sin(1 + h) - \sin(1 - h)}{2h}$ at $h_1 = 0.1$ and $h_2 = 0.05$, and apply the Richardson combination $\frac{4 D(h_2) - D(h_1)}{3}$ on the stack to match $\cos(1) = 0.5403023059$ to 10 digits without shrinking $h$ into the catastrophic cancellation regime.
3. **Single-Entry Sinc & Hyperbolic Ratio Evaluation:** For small arguments $u = 0.0035$, evaluate both $\frac{\sin u}{u}$ and $\frac{\sinh u}{u}$ on the stack using `{{key:LASTX}}` (`0.0035 {{key:SIN}} {{key:LASTX}} {{key:÷}}` and `0.0035 {{key:HYP}} {{key:SIN}} {{key:LASTX}} {{key:÷}}`), and compare their Taylor deviations $\mp u^2/6$ without re-keying `0.0035`.

---

## Summary & Looking Ahead

Combining Richardson extrapolation with adaptive interval halving allows the Romberg numerical quadrature engine (`{{key:∫}}`) to eliminate truncation error systematically, evaluating definite integrals across rocket burnout thrust profiles, aerodynamic wave-drag envelopes, and stratospheric column densities to 10 decimal digits of precision. Coupled with central-difference numerical differentiation, continuous rate equations and integral accumulations resolve in seconds on the four-level stack.

Calculus provides exact models for deterministic continuous phenomena, but real-world engineering and laboratory science must also grapple with random variation, noisy sensor measurements, and empirical trends. In **[Chapter 9: Statistics, Probability Distributions & Regression Curve Fitting](09-statistics-curve-fitting.md)**, you will work with the SC-32's six statistical summation registers ($\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$). You will compute weighted means and standard deviations, perform linear and non-linear regression calibrations, and evaluate continuous Gaussian, Poisson, and Weibull probability distributions directly on the stack.
