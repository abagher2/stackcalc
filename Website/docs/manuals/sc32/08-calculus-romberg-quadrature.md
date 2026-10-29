---
title: "Chapter 8: Archimedes' Balance Beam, Central Differences & Romberg Quadrature | Thinking in the Stack (SC-32)"
description: "Central-difference numerical derivatives, Archimedes' method of exhaustion, Lewis Fry Richardson's 4/3 - 1/3 error cancellation, and Werner Romberg's adaptive quadrature on the StackCalc SC-32."
---

# Chapter 8: Archimedes' Balance Beam, Central Differences & Romberg Quadrature

## Symmetric Difference Quotients and Numerical Derivatives

At Launch Complex 39A at Cape Canaveral, when the five Rocketdyne F-1 engines ignite beneath the Apollo Saturn V moon rocket, the first-stage turbopumps deliver fifteen metric tons of kerosene and liquid oxygen per second into the combustion chambers. As hundreds of tons of propellant are expelled through the nozzles, the vehicle mass decreases while engine thrust increases in the thinning upper atmosphere, so acceleration climbs from $1.25\,g$ at liftoff to $4.5\,g$ just before staging.

In the seventeenth century, Isaac Newton and Gottfried Wilhelm Leibniz independently established that continuous motion is governed by two complementary operations—the derivative and the definite integral—linked as inverses by the *Fundamental Theorem of Calculus*. The derivative $\frac{df}{dt}$ measures the instantaneous rate of change: if $x(t)$ is the altitude of the Saturn V at time $t$, its derivative $v(t) = \frac{dx}{dt}$ is the instantaneous vertical velocity, and the derivative of velocity $a(t) = \frac{dv}{dt}$ is the instantaneous acceleration. Conversely, the definite integral $\int_a^b f(t)\,dt$ measures cumulative change across an interval: integrating the area beneath the acceleration curve from ignition ($t = 0$) to first-stage burnout ($t = T$) recovers the total velocity gained by the spacecraft:

$$v(T) = v_0 + \int_0^T a(t)\,dt$$

For the first pillar of calculus, a digital instrument evaluates the *instantaneous slope* (*derivative*) $f'(x)$ of a function at a point $x$ directly from finite differences without symbolic algebra.

### Symmetric Straddling and the Central Difference Formula

In an introductory calculus course, the derivative is defined by stepping a small distance $h$ *forward* to $x + h$ and computing the difference quotient of the *one-sided forward difference*:

$$D_{\text{forward}}(h) = \frac{f(x + h) - f(x)}{h}$$

A one-sided forward difference introduces systematic first-order bias on curved functions. On a curve that bends upward like a parabola ($f''(x) > 0$), the secant chord from $x$ to $x + h$ is systematically *steeper* than the true tangent line at $x$ because the curve rises more rapidly to the right of $x$. By Brook Taylor's 1715 series expansion:

$$f(x + h) = f(x) + f'(x)h + \frac{1}{2}f''(x)h^2 + \frac{1}{6}f'''(x)h^3 + \dots$$

dividing $f(x + h) - f(x)$ by $h$ leaves a one-sided curvature error of $+\frac{1}{2}f''(x)h$ that diminishes only linearly as $\mathcal{O}(h)$. If one attempts to reduce that $\mathcal{O}(h)$ truncation error by choosing a very small step size such as $h = 10^{-11}$, then $f(x + h)$ and $f(x)$ agree to their first eleven digits, and subtracting them destroys most of the calculator's precision through *catastrophic subtraction cancellation*.

Replacing the one-sided forward step with geometric symmetry eliminates that first-order bias. Instead of stepping only to the right, straddle the point $x$ symmetrically by stepping backward to $x - h$ and forward to $x + h$:

$$\begin{aligned}
f(x + h) &= f(x) + f'(x)h + \frac{1}{2}f''(x)h^2 + \frac{1}{6}f'''(x)h^3 + \dots \\
f(x - h) &= f(x) - f'(x)h + \frac{1}{2}f''(x)h^2 - \frac{1}{6}f'''(x)h^3 + \dots
\end{aligned}$$

Subtracting the second equation from the first and dividing by the total span $2h$ forms the *Central Difference Formula*:

$$f'(x) \approx \frac{f(x + h) - f(x - h)}{2h} = f'(x) + \frac{1}{6}f'''(x)h^2 + \mathcal{O}(h^4)$$

The $+\frac{1}{2}f''(x)h^2$ curvature terms on the right and left of $x$ share the same sign and cancel to zero. Geometrically, the chord joining $(x - h, f(x - h))$ and $(x + h, f(x + h))$ runs nearly parallel to the true tangent line at $x$, and for any parabola $f(x) = ax^2 + bx + c$, where $f'''(x) = 0$, the central difference is exact for *any* step size $h$. Because the leading truncation error now scales as $\mathcal{O}(h^2)$ while floating-point rounding error scales as $\varepsilon_{\text{mach}}/h$, the optimal step size lies near the cube root of machine epsilon, $h \approx \varepsilon_{\text{mach}}^{1/3} \approx 10^{-5}$. That balance delivers ten significant digits of derivative accuracy in two function evaluations.

On the SC-32, the four-register stack models this symmetric central difference directly: evaluate the forward point $f(x + h)$ in Register $X$, evaluate the backward point $f(x - h)$ (which lifts $f(x+h)$ into Register $Y$), subtract via `{{key:-}}`, and divide by $2h$ via `{{key:÷}}`. When differentiating $f(x) = e^{2x}$ at the origin $x_0 = 0$, where the exact slope is $f'(0) = 2$, `{{key:LASTX}}` and `{{key:x⇄y}}` streamline the sequence. Keying `2h {{key:ENTER}} {{key:eˣ}} {{key:LASTX}} {{key:+/-}} {{key:eˣ}} {{key:-}} {{key:x⇄y}} {{key:÷}}` reuses the step $2h$ from `{{key:LASTX}}` without re-typing it, or one can evaluate the hyperbolic sine identity $\frac{e^{2h} - e^{-2h}}{2h} = \frac{\sinh(2h)}{h}$ via `{{key:HYP}} {{key:SIN}}`. Adding $f(x+h)$ and $f(x-h)$ instead of subtracting them cancels the odd terms and isolates the *second derivative* $f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2}$.

In mechanical engineering, derivatives in polar coordinates govern James Watt's 1788 centrifugal flyball governor, the spinning brass-weight mechanism that regulated the speed of Industrial Revolution steam engines and prompted James Clerk Maxwell's 1868 formulation of negative-feedback control theory (*"On Governors"*). When a flyweight of mass $m$ rotates at angular speed $\omega$ along a curved cam slot $r(\theta)$, the flyweight simultaneously moves tangentially at speed $v_\theta = r\omega$ and slides radially outward at speed $\dot{r} = \omega\frac{dr}{d\theta}$. Combining those two perpendicular velocity components via the Pythagorean theorem ($v^2 = \dot{r}^2 + (r\omega)^2$) yields its kinetic energy $E_k = \frac{1}{2}m\omega^2\left[\left(\frac{dr}{d\theta}\right)^2 + r(\theta)^2\right]$ at any cam angle $\theta$.

### Five-Point Stencil Acceleration via Richardson Extrapolation

Richardson's error-cancellation principle applies directly to the Taylor expansion of the central-difference derivative $D(h)$:

$$D(h) = \frac{f(x + h) - f(x - h)}{2h} = f'(x) + c_1 h^2 + c_2 h^4 + \dots \qquad \left(\text{where } c_1 = \frac{1}{6}f'''(x)\right)$$

Because the leading error $c_1 h^2$ scales with the *square* of the step size $h$, evaluating the central difference at step $h$ ($D(h)$) and at twice the step $2h$ ($D(2h)$, whose $h^2$ error is $4\times$ larger) cancels the $h^2$ error completely via $\frac{4 D(h) - D(2h)}{3}$:

$$f'(x) \approx \frac{4 D(h) - D(2h)}{3} = \frac{-f(x + 2h) + 8f(x + h) - 8f(x - h) + f(x - 2h)}{12h} + \mathcal{O}(h^4)$$

This *five-point stencil* ($-1,\; +8,\; 0,\; -8,\; +1$ divided by $12h$) combines two central differences at $h$ and $2h$ in the ratio $\frac{4}{3}$ and $-\frac{1}{3}$, which eliminates the third-derivative error $\frac{1}{6}f'''(x)h^2$ and achieves fourth-order accuracy $\mathcal{O}(h^4)$.

### Leibniz's Integral Rule and Parametric Arc Length

Derivatives and integrals also combine directly in arc-length rectification, surfaces of revolution, mechanical work, and root-mean-square power. Christiaan Huygens and Jakob Bernoulli determined the exact length of a curved cable or orbit $y = f(x)$ from $x = a$ to $x = b$ by differential rectification. Over a differential horizontal step $dx$, the curve rises by $dy = f'(x)\,dx$, and by the Pythagorean theorem the diagonal arc element is $ds = \sqrt{dx^2 + dy^2} = \sqrt{1 + [f'(x)]^2}\,dx$. Integrating those differential elements across the interval yields the *Arc Length Formula*:

$$L = \int_a^b \sqrt{1 + \left[f'(x)\right]^2}\,dx \qquad \text{or in polar coordinates:} \qquad L = \int_{\theta_1}^{\theta_2} \sqrt{r(\theta)^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta$$

For a hanging catenary cable $y(x) = a\cosh(x/a)$, its derivative is $y'(x) = \sinh(x/a)$, and by the hyperbolic identity $1 + \sinh^2(x/a) = \cosh^2(x/a)$, the radical simplifies to $\sqrt{1 + [y'(x)]^2} = \cosh(x/a)$. Rotating that arc-length ribbon $ds$ around the $x$-axis (extending Pappus's First Theorem to general curved profiles) sweeps out a frustum ring of radius $y(x)$ and circumference $2\pi y(x)$, which determines the curved surface area of any turned nosecone, parabolic dish, or cooling tower:

$$S = \int_a^b 2\pi\,y(x)\sqrt{1 + \left[y'(x)\right]^2}\,dx$$

In mechanics and electrical engineering, definite integrals accumulate variable forces and thermal power dissipation. When a constant force $F$ displaces a mass through distance $\Delta x$, work is the product $W = F\Delta x$; when the force varies with position $F(x)$—as in a stiffening rally-car suspension spring, gas expanding against a piston ($W = \int_{V_1}^{V_2} P(V)\,dV$), or gravity diminishing with altitude—work is the definite integral $W = \int_{x_1}^{x_2} F(x)\,dx$. Similarly, the instantaneous heating power dissipated by a time-varying voltage $v(t)$ in a $1\,\Omega$ resistor is $v(t)^2$, and the *True Root-Mean-Square* (RMS) voltage is the equivalent DC voltage that delivers the same average thermal energy over a period $T$:

$$V_{\text{rms}} = \sqrt{\frac{1}{T}\int_0^T \left[v(t)\right]^2 dt}$$

For an undistorted sinusoid $v(t) = V_p\sin\theta$, the average of $\sin^2\theta$ is $\frac{1}{2}$, which yields $V_{\text{rms}} = V_p/\sqrt{2} \approx 0.7071\,V_p$. Whenever a varistor, thyristor dimmer, or rectifier clips the waveform, $V_p/\sqrt{2}$ no longer holds, and the integral $\sqrt{\frac{1}{T}\int_0^T v(t)^2\,dt}$ is required.

---

## Parabolic Quadrature and the Composite Trapezoidal Rule

The second pillar of calculus measures the exact area $\int_a^b f(x)\,dx$ enclosed underneath a curved boundary when no elementary geometric formula applies.

### Archimedes' Mental Balance Beam and the $1 + \frac{1}{4} + \frac{1}{16}$ Parabolic Cascade

Around 240 BCE in Syracuse, Archimedes solved a problem that had resisted Greek geometers since Euclid: determining the exact area of the curved *parabolic segment* enclosed between a parabola and a straight secant chord.

In his treatise *Quadrature of the Parabola*—and in a companion manuscript titled *The Method of Mechanical Theorems*, which remained lost until it was discovered beneath the ink of a medieval prayer book (*The Archimedes Palimpsest*) in 1906—Archimedes combined mechanical equilibrium with geometric exhaustion. Before writing his formal geometric proof, Archimedes analyzed the problem using a mental balance beam, suspending thin vertical strips of the parabola from one end of a lever and counterbalancing them against strips of a known triangle at the other end. Comparing the lever arms at every horizontal station $x$ revealed that the curved parabolic segment balanced at four-thirds ($\frac{4}{3}$) the weight of the largest inscribed triangle sharing the same base and apex.

To prove that $\frac{4}{3}$ ratio rigorously by the *method of exhaustion*, Archimedes inscribed a central triangle of area $A_0$ inside the parabola, which left two smaller curved parabolic segments on the left and right. Inside each of those two segments he inscribed a new triangle, and proved from the quadratic law of the parabola that the combined area of the two new triangles equaled one-fourth ($\frac{1}{4} A_0$) of the first triangle. Repeating the construction inside the four remaining segments added $\left(\frac{1}{4}\right)^2 A_0 = \frac{1}{16} A_0$, then $\frac{1}{64} A_0$, and so on in a convergent geometric series:

$$\text{Area} = A_0 \left( 1 + \frac{1}{4} + \frac{1}{16} + \frac{1}{64} + \dots \right) = A_0 \left( \frac{1}{1 - 1/4} \right) = \mathbf{\frac{4}{3} A_0}$$

One scaling ratio governs Archimedes' geometric proof: every time the horizontal span of a parabolic arch is halved ($h \to h/2$), the remaining curved gap between the curve and the straight chord shrinks by a factor of one-fourth ($\frac{1}{4}$).

### Composite Trapezoidal Quadrature and $O(h^2)$ Truncation Error

Archimedes' parabolic scaling ratio carries directly into modern numerical quadrature. To integrate a smooth function $f(x)$ from $x = a$ to $x = b$, one partitions the interval into $N$ equal panels of width $h = \frac{b - a}{N}$. Capping each panel with a flat horizontal top at the left or right endpoint (a *Riemann step rectangle*) leaves a right-triangular gap of width $h$ and height $\Delta y \approx f'(x)h$ on every sloping section of the curve; each panel incurs an $\mathcal{O}(h^2)$ local error, and summing across $N = \frac{b-a}{h}$ panels produces an $\mathcal{O}(h)$ first-order global error.

Connecting each sample point $(x_i, f(x_i))$ to the next point $(x_{i+1}, f(x_{i+1}))$ with a straight diagonal chord instead forms a *trapezoid* of average height $\frac{1}{2}[f(x_i) + f(x_i+1)]$ and area $\frac{h}{2}[f(x_i) + f(x_{i+1})]$. Every interior ordinate $f(x_i)$ is shared by two adjacent trapezoids (counted with weight $\frac{1}{2} + \frac{1}{2} = 1$), whereas the two outer endpoints $f(a)$ and $f(b)$ receive weight $\frac{1}{2}$. Summing all $N$ trapezoids yields the *Composite Trapezoidal Rule*:

$$T(h) = h \left[ \frac{1}{2}f(a) + f(a + h) + f(a + 2h) + \dots + f(b - h) + \frac{1}{2}f(b) \right]$$

The truncation error of flat-topped trapezoids on a smooth curve follows from the geometry of a single narrow panel of width $h$. Over any small span, Taylor's theorem shows that a smooth curve bends locally like a parabola with curvature $f''(x)$, which encloses a thin crescent-shaped parabolic segment of width $h$ between the curve and the straight secant chord of the trapezoid. Because parabolic deflection grows with the square of distance from the midpoint, the maximum vertical sag of the segment at the center of the panel is proportional to $h^2$ (specifically, $\frac{1}{8}f''(x)h^2$). By Archimedes' parabolic area theorem, the area of a parabolic segment is $\frac{2}{3} \times \text{base} \times \text{height}$, so the area of *one* panel's segment scales as $\frac{2}{3} \times h \times \frac{1}{8}f''(x)h^2 = \frac{1}{12}f''(x)h^3 \propto h^3$. Summing these segments across all $N = \frac{b - a}{h}$ panels spanning $[a, b]$ cancels one power of $h$ against $1/h$:

$$\text{Total Trapezoidal Error } E(h) = T(h) - \int_a^b f(x)\,dx \approx \frac{b - a}{12} f''(\xi)\, h^2 \propto \mathcal{O}(h^2)$$

The sign of that error reflects the concavity of the integrand. When a curve is *concave up* ($f''(x) > 0$, such as $e^x$ or $x^2$), the straight secant chord of each trapezoid lies *above* the curve, so $T(h)$ slightly *overestimates* the integral. When a curve is *concave down* ($f''(x) < 0$, such as $\sin x$ on $[0, \pi]$ or $\ln x$), the straight chord passes *beneath* the arch, so $T(h)$ slightly *underestimates* the integral.

The $h^2$ scaling law has a direct consequence: whenever an interval is partitioned into twice as many trapezoids, halving the step width ($h \to h/2$), the total error shrinks by a factor of $\left(\frac{1}{2}\right)^2 = \mathbf{\frac{1}{4}}$, matching Archimedes' 240 BCE ratio. Without extrapolation, that $1/4$ ratio would require $2^{20} \approx 1,048,576\text{ trapezoids}$ to reach twelve decimal digits of precision ($10^{-12} \approx 4^{-20}$). Richardson extrapolation eliminates this bottleneck in four or five halving steps.

---

## The 4/3 Minus 1/3 Extrapolation: Richardson & Romberg Integration

In 1910–1911, the English physicist, meteorologist, and Quaker pacifist Lewis Fry Richardson {{cite:richardson1911}}—who formulated numerical weather prediction by solving fluid-dynamics equations by hand and later analyzed the fractal scaling of coastlines—recognized that the $1/4$ error ratio could be used to cancel the leading truncation term algebraically.

Evaluating the area under a curve first with a coarse step size $h$ produces the trapezoidal estimate $T_{\text{coarse}} = T(h)$, and halving the step size once to $h/2$ produces the fine trapezoidal estimate $T_{\text{fine}} = T(h/2)$.

First, that halving step reuses every previous ordinate. Refining $N$ panels of width $h$ into $2N$ panels of width $h/2$ keeps every sample point of the coarse grid as an even-numbered node of the fine grid:

$$T\!\left(\frac{h}{2}\right) = \frac{1}{2} T(h) + \frac{h}{2} \sum_{m=1}^{N} f\!\left(a + \left(m - \frac{1}{2}\right)h\right)$$

No function evaluation from the earlier pass is discarded; dividing the previous trapezoidal sum $T(h)$ by $2$ and adding the newly sampled midpoints completes the refined sum.

Second, the trapezoidal error expands exclusively in *even* powers of $h$ ($h^2, h^4, h^6, \dots$) with all odd powers ($h^3, h^5, \dots$) absent. In the 1730s, Leonhard Euler and Colin Maclaurin established this symmetry through the *Euler-Maclaurin Summation Formula*:

$$T(h) - \int_a^b f(x)\,dx = \sum_{m=1}^{K} \frac{B_{2m}}{(2m)!} h^{2m} \left[ f^{(2m-1)}(b) - f^{(2m-1)}(a) \right] + \mathcal{O}\!\left(h^{2K+2}\right)$$

where $B_2 = \frac{1}{6},\; B_4 = -\frac{1}{30},\; B_6 = \frac{1}{42},\dots$ are Jakob Bernoulli's numbers. Every odd power of $h$ vanishes identically because on every interior boundary $x_i$ between adjacent panels, the derivative contribution from the right end of panel $i$ ($+f^{(k)}(x_i)$) and the left end of panel $i+1$ ($-f^{(k)}(x_i)$) cancel in a *telescoping sum*, so only the odd-order derivatives at the outer endpoints $x = a$ and $x = b$ multiplied by even powers of $h$ remain:

$$T(h) = I + c_1 h^2 + c_2 h^4 + c_3 h^6 + \dots$$

Because halving the step size ($h \to h/2$) reduces the dominant $c_1 h^2$ error term $E = c_1 h^2$ to one-fourth ($\frac{1}{4}E$) of its previous value while reducing the $c_2 h^4$ term to $\frac{1}{16}$ of its value, the two estimates form a system of two linear equations:

$$\begin{aligned}
T_{\text{coarse}} &= I + E + c_2 h^4 + \mathcal{O}(h^6) \\
T_{\text{fine}} &= I + \frac{1}{4} E + \frac{1}{16} c_2 h^4 + \mathcal{O}(h^6)
\end{aligned}$$

Because the leading error in $T_{\text{fine}}$ is one-fourth the error in $T_{\text{coarse}}$, multiplying the second equation by $4$, subtracting the first equation, and dividing by $3$ eliminates $E$:

$$\frac{4 T_{\text{fine}} - T_{\text{coarse}}}{3} = \frac{4}{3} T_{\text{fine}} - \frac{1}{3} T_{\text{coarse}} = \left(\frac{4}{3} - \frac{1}{3}\right) I + \left(\frac{4}{3}\cdot\frac{1}{4}E - \frac{1}{3}E\right) - \frac{1}{4}c_2 h^4 = \mathbf{I + 0 \cdot E + \mathcal{O}(h^4)}$$

{{blocks:sc32_concept_romberg_quadrature|Symmetric central-difference secant slope cancelation and Romberg trapezoidal halving with Richardson 4^m extrapolation.}}

The leading $h^2$ error vanishes completely. Across a single coarse macro-panel of span $h = b - a$ (subdivided into two sub-steps of width $h/2$ at the midpoint $m = \frac{a+b}{2}$), substituting $T(h) = \frac{h}{2}[f(a) + f(b)]$ and $T(h/2) = \frac{h}{4}[f(a) + 2f(m) + f(b)]$ into Richardson's $\frac{4}{3} - \frac{1}{3}$ combination yields:

$$\frac{4}{3}\left(\frac{h}{4}\big[f(a) + 2f(m) + f(b)\big]\right) - \frac{1}{3}\left(\frac{h}{2}\big[f(a) + f(b)\big]\right) = \frac{h}{6}\Big[ f(a) + 4f(m) + f(b) \Big]$$

Those $1\text{–}4\text{–}1$ weights $\frac{h}{6}[f(a) + 4f(m) + f(b)]$ (with $h = b - a$, or $\frac{\Delta x}{3}$ in terms of the half-step $\Delta x = h/2$) show that Richardson's $\frac{4}{3} - \frac{1}{3}$ combination of two flat-topped trapezoid sums produces *Thomas Simpson's 1743 Parabolic Rule* ($\mathcal{O}(h^4)$), the exact area under a parabola fitted through the left endpoint, the midpoint, and the right endpoint. Because the third derivative $f'''(x)$ of any cubic polynomial $Ax^3 + Bx^2 + Cx + D$ is a constant (so $f'''(b) - f'''(a) = 0$ in the $h^2$ term and $f^{(4)}(x) = 0$ in the $h^4$ term), Simpson's $1\text{–}4\text{–}1$ rule is exact not only for parabolas, but for cubics as well.

In 1955, the German-Norwegian physicist Werner Romberg {{cite:romberg1955}} extended Richardson's elimination beyond the $h^2$ term. Once two Simpson parabolic estimates are available at step sizes $h$ and $h/2$ across a macro-panel of span $h = b - a$ (subdivided into four sub-steps of width $h/4$ at nodes $x_0, x_1, x_2, x_3, x_4$), their leading $c_2 h^4$ errors stand in the ratio $\left(\frac{1}{2}\right)^4 = \frac{1}{16}$. Forming $\frac{16}{15}S_{\text{fine}} - \frac{1}{15}S_{\text{coarse}}$ eliminates the $h^4$ error and produces *George Boole's 5-Point Rule* ($\mathcal{O}(h^6)$) with its $7\text{–}32\text{–}12\text{–}32\text{–}7$ weights (where $\frac{h}{90} = \frac{2(h/4)}{45}$):

$$B = \frac{16 S_{\text{fine}} - S_{\text{coarse}}}{15} = \frac{h}{90}\Big[ 7f(x_0) + 32f(x_1) + 12f(x_2) + 32f(x_3) + 7f(x_4) \Big]$$

Arranging each halving $h_k = (b-a)/2^k$ down a lower-triangular table $R(k, j)$ and sweeping across each row via the universal Richardson recurrence:

$$R(k, j) = R(k, j-1) + \frac{R(k, j-1) - R(k-1, j-1)}{4^j - 1}, \qquad \text{Error} = \mathcal{O}\!\left(h_k^{2j+2}\right), \qquad j = 1 \dots \min(k, 5)$$

creates *Romberg Integration* {{cite:romberg1955}}:

| Column Index | Equivalent Classical Quadrature Rule | Error Order | Extrapolation Multiplier |
| :---: | :--- | :---: | :--- |
| **$j = 0$** | Composite Trapezoidal Rule $T(h_k)$ | $\mathcal{O}(h^2)$ | Base midpoint-reuse column |
| **$j = 1$** | Simpson's $1/3$ Parabolic Rule | $\mathcal{O}(h^4)$ | $\frac{4 R(k,0) - R(k-1,0)}{3}$ (kills $h^2$ error) |
| **$j = 2$** | Boole's 5-Point Rule | $\mathcal{O}(h^6)$ | $\frac{16 R(k,1) - R(k-1,1)}{15}$ (kills $h^4$ error) |
| **$j = 3$** | 9-Point Super-Extrapolation | $\mathcal{O}(h^8)$ | $\frac{64 R(k,2) - R(k-1,2)}{63}$ (kills $h^6$ error) |
| **$j = 4, 5$** | Capped High-Order Limit ($j_{\max} = 5$) | $\mathcal{O}(h^{10}) \to \mathcal{O}(h^{12})$ | Prevents high-degree Runge ringing |

To see the full triangular tableau $R(k, j)$ in action, trace how each row of $\int_0^2 e^x\,dx = e^2 - 1 \approx \mathbf{6.3890560989}$ feeds the next column to the right:

| Row $k$ (Panels $2^k$) | $j = 0$ (Trapezoid $\mathcal{O}(h^2)$) | $j = 1$ (Simpson $\mathcal{O}(h^4)$) | $j = 2$ (Boole $\mathcal{O}(h^6)$) | $j = 3$ ($\mathcal{O}(h^8)$) |
| :--- | :---: | :---: | :---: | :---: |
| **$k = 0$ ($1$ panel)** | $8.38905610$ | — | — | — |
| **$k = 1$ ($2$ panels)** | $6.91280988$ | $6.42072780$ | — | — |
| **$k = 2$ ($4$ panels)** | $6.52161011$ | $6.39121019$ | $6.38924235$ | — |
| **$k = 3$ ($8$ panels)** | $6.42229781$ | $6.38919370$ | $6.38905927$ | $6.38905637$ |

On Row $k = 0$ ($1$ trapezoid, $h_0 = 2.0$), the single trapezoid $R(0,0) = \frac{2}{2}(e^0 + e^2) = 8.38905610$ overshoots the exact integral by $+31.3\%$. On Row $k = 1$ ($2$ trapezoids, $h_1 = 1.0$), adding the single midpoint $e^1$ gives $R(1,0) = 6.91280988$, and applying $\frac{4 R(1,0) - R(0,0)}{3}$ produces the Simpson estimate $R(1,1) = 6.42072780$, which reduces the error tenfold. On Row $k = 2$ ($4$ trapezoids, $h_2 = 0.5$), adding the two quarter-points gives $R(2,0) = 6.52161011$, which extrapolates to $R(2,1) = 6.39121019$ and then $R(2,2) = \frac{16(6.39121019) - 6.42072780}{15} = 6.38924235$, within $0.0029\%$ of the exact value using only $5$ function evaluations. By Row $k = 3$ ($8$ trapezoids, $h_3 = 0.25$), using $9$ function evaluations, $R(3,3) = 6.38905637$ is accurate to seven significant digits, and by Row $k = 4$ ($17$ points), the error drops below $10^{-12}$.

On the SC-32, you run this entire Romberg tableau with three actions: enter the integrand expression into `{{key:EQN}}`, place the lower limit $a$ in Register $Y$ and the upper limit $b$ in Register $X$, and press `{{key:∫}}` (Right Shift on `8`) followed by the dummy variable softkey. The SC-32 caps the Romberg tableau at column $j_{\max} = 5$ ($\mathcal{O}(h^{12})$) and splits wide intervals ($|b - a| > 20$) across logarithmic `1-2-5` decade boundaries because, as German mathematician Carl David Tolmé Runge proved in 1901, fitting a single high-degree polynomial across equally spaced points on a wide interval triggers boundary oscillations (*Runge's Phenomenon*).

When an integrand is a periodic wave such as $\cos^2 x$ or a bell curve whose odd derivatives $f^{(2m-1)}(b) - f^{(2m-1)}(a)$ vanish at both endpoints in the Euler-Maclaurin expansion, the Composite Trapezoidal Rule converges exponentially fast on its own. Following William Kahan's architecture {{cite:kahan1979}}, the SC-32 couples its Romberg stopping tolerance to the active `{{key:DISP}}` format (`FIX`, `SCI`, `ENG`, or `ALL`) and upon completion places the certified integral $I$ in Register $X$ and the estimated truncation uncertainty $\pm\varepsilon$ in Register $Y$, while preserving whatever was previously in Registers $Z$ and $T$ so chained integrals never overwrite the upper stack registers.

---

## Non-Elementary Integrals: Rockets, Dams & Large-Amplitude Pendulums

### Joseph Liouville's Theorem and Non-Elementary Antiderivatives

In first-year calculus courses, nearly every exercise is constructed so that a closed-form symbolic antiderivative $F(x)$ exists for evaluating $F(b) - F(a)$. Yet in 1835, the French mathematician Joseph Liouville proved that while any elementary combination of powers, roots, sines, exponentials, and logarithms can be *differentiated* by mechanical rules, most continuous curves encountered in physics possess no elementary antiderivative.

A simple pendulum of length $L$ has the small-angle period $T_0 = 2\pi\sqrt{L/g}$. In his 1673 *Horologium Oscillatorium*, Christiaan Huygens demonstrated that a real pendulum swinging through a wide release angle $\theta_0$ runs noticeably *slower* than $T_0$ because Galileo's linearized model replaces $\sin\theta$ with $\theta$. Retaining the exact restoring torque $\sin\theta$ in conservation of energy leads to the *Complete Elliptic Integral of the First Kind* (with modulus $k = \sin(\theta_0/2)$):

$$\frac{T(\theta_0)}{T_0} = \frac{2}{\pi} \int_0^{\pi/2} \frac{d\varphi}{\sqrt{1 - k^2 \sin^2\varphi}}$$

Like the perimeter of an ellipse, no finite combination of elementary functions can express that integral, yet Romberg quadrature (`{{key:∫}}`) evaluates it to twelve digits. The same barrier arises across quantum physics, optics, and civil engineering. In 1912, when Peter Debye explained why the heat capacity $C_V(T)$ of a diamond or copper crystal drops as $T^3$ near absolute zero, quantizing the lattice vibrations led to the non-elementary *Debye Integral*:

$$C_V(T) = 9 N k_B \left(\frac{T}{\Theta_D}\right)^3 \int_0^{\Theta_D / T} \frac{x^4 e^x}{\left(e^x - 1\right)^2}\,dx$$

Similarly, integrating Max Planck's spectral radiance across a thermal camera's wavelength window $[\lambda_1, \lambda_2]$ or computing Carl Friedrich Gauss's normal error integral $\frac{1}{\sqrt{2\pi}}\int_a^b e^{-x^2/2}\,dx$ admits no closed-form antiderivative. When coherent light grazes a sharp edge—or when a civil engineer designs a highway exit ramp or roller-coaster loop whose curvature $\kappa(s) \propto s$ increases linearly with arc length $s$ to prevent a sudden lateral jerk—the trajectory follows *Augustin-Jean Fresnel's 1818 Diffraction Integrals*, tracing the double-coiled *Euler-Cornu clothoid spiral*:

$$C(u) = \int_0^u \cos\!\left(\frac{\pi t^2}{2}\right) dt, \qquad S(u) = \int_0^u \sin\!\left(\frac{\pi t^2}{2}\right) dt$$

Even when an integrand *does* admit a symbolic antiderivative, integrating the physical rate law in `{{key:EQN}}` via `{{key:∫}}` avoids algebraic transcription errors. This direct formulation applies to summing the hanging catenary arc length $\int_{-x_0}^{x_0}\cosh(x/a)\,dx$ of a transmission span, the voltage-dependent capacitance droop $C(V) = C_0(1 - \alpha V^2)$ of a ferroelectric $\text{BaTiO}_3$ capacitor {{cite:horowitz2015}}, or the cylindrical velocity rings $\int_0^R 2\pi r\,v(r)\,dr$ of Hagen-Poiseuille laminar pipe flow. In laminar pipe flow, because both the cross-sectional area $\pi R^2$ and the parabolic centerline speed $v_{\max} = \frac{\Delta P}{4\mu L}R^2$ scale with $R^2$, integrating the concentric shells yields *Poiseuille's fourth-power law*:

$$Q = \int_0^R 2\pi r\,v_{\max}\!\left(1 - \frac{r^2}{R^2}\right) dr = \frac{1}{2}\pi R^2 v_{\max} = \frac{\pi \Delta P}{8\mu L}\,R^4$$

Consequently, a $16\%$ plaque constriction to $0.84\,R$ in a human coronary artery cuts blood supply in half ($0.84^4 = \mathbf{0.4979}$), whereas a $19\%$ smooth-muscle dilation to $1.19\,R$ during exercise *doubles* blood flow ($1.19^4 = \mathbf{2.0053}$), because laminar flow integrates across both cross-sectional area and velocity simultaneously.

### Taming Improper Integrals & Singular Endpoints by Substitution

Physical integrals sometimes span an infinite upper limit $[a, \infty)$ or involve an integrand whose value or slope diverges at an endpoint, such as the hydrostatic pressure ribbon $(H - y)\sqrt{8y}$ at the floor $y = 0$ of a parabolic canyon dam or an inverse-square-root cusp $\int_0^b \frac{g(x)}{\sqrt{x}}\,dx$. If an endpoint triggers an explicit division by zero (such as $\frac{\sin x}{x}$ at $x = 0$), the SC-32 halts safely with `DIVIDE BY 0` (Code 01). As analyzed by William Kahan {{cite:kahan1979}} and in Press et al.'s *Numerical Recipes*, two classical variable substitutions inside `{{key:EQN}}` eliminate endpoint singularities and infinite tails before pressing `{{key:∫}}`.

Whenever an integral has an integrable $1/\sqrt{x}$ singularity at $x = 0$ (as occurs when a pendulum reaches its turnaround point or light grazes a caustic), substituting $x = u^2$ introduces $dx = 2u\,du$ in the numerator, which cancels $\sqrt{x} = u$ in the denominator identically:

$$\int_0^b \frac{g(x)}{\sqrt{x}}\,dx = \int_0^{\sqrt{b}} \frac{g(u^2)}{u}\,2u\,du = \int_0^{\sqrt{b}} 2\,g(u^2)\,du$$

For example, $\int_0^1 \frac{\cos x}{\sqrt{x}}\,dx$ diverges to $+\infty$ at $x = 0$, yet entering the smooth transformed integrand $2\cos(u^2)$ into `{{key:EQN}}` as `U {{key:x²}} {{key:COS}} 2 {{key:×}}` in `{{key:RAD}}` mode and integrating over `0 {{key:ENTER}} 1 {{key:∫}} U` converges in four Romberg rows to $1.8090484758$.

Similarly, when integrating a rapidly decaying tail over $[a, \infty)$ with $a > 0$, the reciprocal substitution $x = 1/t$ ($dx = -dt/t^2$) maps the infinite horizon $x \to \infty$ onto the finite interval $[0, 1/a]$ as $t \to 0^+$:

$$\int_a^\infty f(x)\,dx = \int_0^{1/a} \frac{1}{t^2}\,f\!\left(\frac{1}{t}\right) dt$$

Displacing the lower limit from $0$ to $10^{-12}$ (or truncating a Gaussian or exponential tail at $5$ to $8$ characteristic scale lengths where $e^{-x^2/2}$ has already fallen below machine epsilon) lets Romberg's tableau integrate improper tails to full precision.

---

## Central Differences & Adaptive Romberg Quadrature

Both pillars of numerical calculus—central-difference differentiation and adaptive Romberg quadrature—map their two-point geometry onto the lower pair of stack registers (`Y` and `X`) while leaving the upper stack (`Z` and `T`) undisturbed.

For a general integrand $f(x)$ stored inside `{{key:EQN}}` (`{{key:↱}}` + `{{key:STO}}`), complementing direct 3-point Simpson evaluation $(1, 4, 1) \times \frac{h}{6}$ on the stack, the integration bounds $[a, b]$ occupy the lower two registers via `a {{key:ENTER}} b`. Pressing `{{key:∫}}` (above `{{key:8}}`) and selecting the active dummy variable (`X`, `T`, `R`, or `V`) launches the midpoint-reuse trapezoidal cascade and Richardson's $4^j$ extrapolation across `Y` and `X` without disturbing any prior constants or intermediate integrals stored in `Z` and `T`.

{{res:sc32_plot_romberg_shaded:screenshot|The SC-32 transflective display executing active numerical integration of 3x² from 0 to 4 (Area = 64.0) with real-time stack updates and error bound estimation.}}

### Rocket Burnout, Progressive Springs, Hydrostatic Dams & Poiseuille Flow

Unless degrees (`{{key:DEG}}`) are explicitly noted, trigonometric and calculus sequences use radian measure (`{{key:RAD}}`). Because a single Romberg integral consumes only the limits $(a, b)$ in Registers $Y$ and $X$, convergence replaces $(Y, X)$ in place with the *Post-Integration Audit Frame* $(\pm\varepsilon, I)$ while leaving Registers $Z$ and $T$ untouched for multi-integral chaining:

| Stack Register | Post-`{{key:∫}}` Contents | Engineering Purpose & Stack Chaining |
| :---: | :--- | :--- |
| **Register $X$** | **Certified Definite Integral ($I = \int_a^b f(x)\,dx$)** | The final Richardson-extrapolated quadrature result. |
| **Register $Y$** | **Estimated Quadrature Uncertainty ($\pm\varepsilon$)** | Upper bound on absolute truncation error. Swap via `{{key:x⇄y}}` to audit convergence. |
| **Register $Z$** | **Prior Register $Z$ (Preserved)** | Holds whatever was in $Z$ when `{{key:∫}}` was pressed (for example, a first integral $I_1$ lifted into $Z$ by typing `c {{key:ENTER}} d` for a second integral). |
| **Register $T$** | **Prior Register $T$ (Preserved)** | Preserves the top of the stack undisturbed across quadrature passes. |

Five mechanical and fluid accumulation laws show how the analytical smoothness of the integrand governs which column of Romberg's tableau delivers the final answer:

* **Cubic Rocket Thrust & Burnout Profiles (Exact in One Richardson Step at $R(1,1)$):** Because Richardson's first $\frac{4}{3} T(h/2) - \frac{1}{3} T(h)$ column $R(1,1)$ is algebraically identical to Thomas Simpson's parabolic rule—whose fourth-order error $\propto f^{(4)}(\xi)\,h^4$ vanishes identically for every polynomial of degree $3$ or less—any cubic velocity or acceleration law hits machine precision on the very first Romberg row.
  * **Sounding Rocket & Cubic Boost:** If a solid-propellant sounding rocket climbs at $v(t) = 30t - 0.5t^3\text{ m/s}$ over $t \in [0, 6]\text{ s}$, one Simpson pass integrates the burnout altitude $\int_0^6 (30t - 0.5t^3)\,dt = [15t^2 - \frac{1}{8}t^4]_0^6 = 378.0\text{ m}$ ($202.5\text{ m}$ over $[0, 3]\text{ s}$ for $45t - 0.5t^3$). For the cubic boost acceleration $a(t) = 4t^2 - 0.5t^3\text{ m/s}^2$, store `T x² 4 × T 3 yˣ 0.5 × -` in `{{key:EQN}}` and key `0 {{key:ENTER}} 6 {{key:∫}} T` to nail the burnout velocity $\left[\frac{4}{3}t^3 - \frac{1}{8}t^4\right]_0^6 = \mathbf{126.000000000\text{ m/s}}$ in Register $X$ ($\pm\varepsilon = 1.24 \times 10^{-11}$ in Register $Y$).
  * **Liquid-Bipropellant Upper Stage:** When an upper stage expels propellant at a constant mass rate so thrust-to-mass acceleration climbs exponentially as $a(t) = 12.0e^{0.04t} - 9.80665\text{ m/s}^2$ over a $25\text{-second}$ burn, integrating via `0 {{key:ENTER}} 25 {{key:∫}} T` yields $\mathbf{270.3183\text{ m/s}}$ in Register $X$ (matching the analytical antiderivative $\Delta v = 300(e^{1.0} - 1) - 245.16625 = \mathbf{270.3183\text{ m/s}}$, where `{{key:LASTX}}` reuses `25` for the gravity-loss subtraction).
* **Progressive Rally-Car Suspension Springs:** That same exact-cubic property governs the variable-pitch *progressive suspension spring* ($F(x) = 2500x + 40000x^3\text{ N}$) of an off-road rally car. Over small ripples ($x \ll 0.05\text{ m}$), the $2,500\text{ N/m}$ linear rate gives a supple ride; on hard jump landings, the lower coils bind so the $40,000x^3$ stiffening prevents bottoming out (absorbing $[1250x^2 + 10000x^4]_0^{0.50} = 937.5\text{ J}$ over a $0.50\text{ m}$ stroke). At $x = 0.15\text{ m}$, storing `X 2500 × X 3 yˣ 40000 × +` in `{{key:EQN}}` and keying `0 {{key:ENTER}} 0.15 {{key:∫}} X` converges on the first Simpson column to $W = \mathbf{33.187500000\text{ J}}$ ($\pm\varepsilon = 3.55 \times 10^{-12}$ in $Y$), which evaluating $1250x^2 + 10000x^4$ via `{{res:sc32_08_calc_01:keys}}` confirms as $\mathbf{{{res:sc32_08_calc_01:value}}\text{ Joules}}$—$18\%$ above a linear spring's $28.125\text{ J}$.
* **Nonlinear Ferroelectric $\text{BaTiO}_3$ Ceramic Capacitors:** For a Class-II barium titanate ($\text{BaTiO}_3$) ceramic capacitor whose capacitance droops under high DC bias as $C(V) = C_0(1 - \alpha V^2)$ with $C_0 = 10\,\mu\text{F}$ and $\alpha = 10^{-6}\text{ V}^{-2}$ {{cite:horowitz2015}}, integrating the differential energy $dW = C(V)V\,dV = 10^{-5}(V - 10^{-6}V^3)\,dV$ is again a degree-3 polynomial that Simpson's column $R(1,1)$ resolves exactly. Storing `V 3 yˣ 1E-6 × V x⇄y - 10E-6 ×` in `{{key:EQN}}` and integrating over `0 {{key:ENTER}} 500 {{key:∫}} V` reveals a true stored energy of $\mathbf{1.09375\text{ Joules}}$—a $12.5\%$ shortfall below the unadjusted linear estimate $\frac{1}{2}C_0 V^2 = 1.2500\text{ J}$.
* **Parabolic Canyon Spillway Dam (Vertical Square-Root Tangents and Higher Romberg Columns):** Unlike those cubic polynomials, the hydrostatic pressure ribbon $(H - y)\sqrt{8y}$ across a parabolic canyon spillway of width $w(y) = \sqrt{8y}\text{ m}$ and water depth $H = 4.0\text{ m}$ ($\rho g = 9,810\text{ N/m}^3$) carries the singular endpoint derivative $\frac{d}{dy}\sqrt{8y} = \frac{\sqrt{2}}{\sqrt{y}} \to \infty$ at the canyon floor $y = 0$. Because the Euler-Maclaurin endpoint derivatives diverge there, $R(1,1)$ cannot cancel the curvature in one step; instead, Romberg's tableau subdivides the grid and marches to higher columns $R(k, j)$ until the singular boundary panel is pinched down to tolerance. Storing `Y 8 × √x 4 Y - × 9810 ×` in `{{key:EQN}}` and keying `0 {{key:ENTER}} 4 {{key:∫}} Y` converges to $\mathbf{236,773.2915\text{ N}}$ ($\pm\varepsilon = 4.18 \times 10^{-10}$ in Register $Y$).
* **Hagen-Poiseuille Laminar Pipe Flow Across Concentric Rings:** Evaluating Poiseuille's concentric-shell integral $Q = \int_0^R 2\pi r\,v_{\max}(1 - r^2/R^2)\,dr$ for a pipe of radius $R = 0.05\text{ m}$ ($R^2 = 0.0025\text{ m}^2$) and centerline speed $v_{\max} = 1.2\text{ m/s}$ integrates the cubic ring flux $2\pi v_{\max}(r - r^3/R^2)$, whose peak contribution sits at $r = R/\sqrt{3} \approx 0.0289\text{ m}$ where neither the wall shear ($v(R) = 0$) nor the vanishing centerline circumference ($2\pi(0) = 0$) suppresses the flow. Entering `R x² 0.0025 ÷ 1 x⇄y - 1.2 × R × 2 × π ×` into `{{key:EQN}}`, keying `0 {{key:ENTER}} 0.05 {{key:∫}} R` ($\to Q = 0.004712389\text{ m}^3/\text{s}$, $\pm\varepsilon = 1.45 \times 10^{-12}$ in $Y$), and scaling by `1000 {{key:×}}` yields $\mathbf{4.712389\text{ Liters/second}}$.

---

### Transcendental Integrals, Piecewise RMS Waveforms & Chained Centroids

When we move from algebraic profiles to Gaussian bells, exponential lightning surges, hanging catenary cables, and chained integral ratios, both Euler-Maclaurin endpoint behavior and four-register stack preservation come to the fore.

Symmetry and exponential tail cutoffs resolve non-elementary improper integrals over $(-\infty, 0]$ or $[0, \infty)$ directly on $(Y, X)$:

* **Gauss's Normal Bell & Vanishing Euler-Maclaurin Endpoint Derivatives ($\int_{-5}^0 \phi(x)\,dx$):** For the non-elementary standard normal density $\phi(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$, truncating the lower $(-\infty, 0]$ tail at five standard deviations ($x = -5$, where $\phi(-5) \approx 1.487 \times 10^{-6}$) pairs an exponentially small left endpoint with the symmetry peak $x = 0$, where every odd derivative $\phi'(0) = \phi'''(0) = \phi^{(5)}(0) = 0$ vanishes identically. Because the Euler-Maclaurin error series depends only on the odd-order endpoint derivatives $f^{(2m-1)}(b) - f^{(2m-1)}(a)$, storing `X x² 2 ÷ +/- eˣ 2 π × √x ÷` in `{{key:EQN}}` and integrating across `5 {{key:+/-}} {{key:ENTER}} 0 {{key:∫}} X` converges rapidly to $\mathbf{0.4999997133}$ in Register $X$ ($\pm\varepsilon = 2.15 \times 10^{-10}$ in Register $Y$)—rounding to exact `0.500000` in `FIX 6` and missing only the minuscule five-sigma tail $\Phi(-5) = 2.8665 \times 10^{-7}$.
* **Substation MOV Lightning Surge Arrester Across Five Time Constants:** When a lightning stroke drives an $i(t) = I_0 e^{-t/\tau}$ current surge ($I_0 = 10,000\text{ A}$, $\tau = 5 \times 10^{-5}\text{ s}$) through a zinc-oxide Metal-Oxide Varistor (MOV), the charge $Q = \int i(t)\,dt$ absorbed over $[0, 5\tau] = [0, 250\,\mu\text{s}]$ follows from integrating the exponential pulse. Storing `T 5E-5 ÷ +/- eˣ 10000 ×` in `{{key:EQN}}` and keying `0 {{key:ENTER}} 0.00025 {{key:∫}} T` integrates the pulse to $\mathbf{0.496631027\text{ Coulombs}}$ in Register $X$ ($\pm\varepsilon = 1.12 \times 10^{-11}$ in $Y$), which cross-checking $I_0\tau(1 - e^{-5})$ via `{{res:sc32_08_calc_02:keys}}` confirms as $\mathbf{{{res:sc32_08_calc_02:value}}\text{ C}}$ ($1 - e^{-5} = \mathbf{99.326\%}$ of the total charge $I_0\tau = 0.5000\text{ C}$).

All four stack registers $(T, Z, Y, X)$ participate when chaining a Romberg integral into a subsequent calculation or combining two definite integrals on the stack. Applying the hyperbolic arc-length identity $\sqrt{1 + [y'(x)]^2} = \cosh(x/a)$ to a high-voltage transmission cable $y(x) = 800\cosh(x/800)$ spanning $200\text{ m}$ from $x = -100\text{ m}$ to $+100\text{ m}$, integrating `X 800 ÷ HYP COS` via `{{key:∫}} X` places the conductor arc length $L = 200.5212\text{ m}$ in Register $X$ and its uncertainty $8.55 \times 10^{-11}$ in Register $Y$; as we then compute the mid-span sag $\Delta y = 800[\cosh(100/800) - 1] = 6.2581\text{ m}$ in Register $X$, the arc length $200.5212\text{ m}$ stays live in Register $Y$ while the Romberg uncertainty rides up into Registers $Z$ and $T$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `100 {{key:+/-}} {{key:ENTER}} 100` | $0.0000$ | $0.0000$ | $-100.0000$ | $100.0000$ | Tower span interval $[-100, +100]$ |
| `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$8.55 \times 10^{-11}$** | **$200.5212$** | Conductor total arc length (meters) |
| `100 {{key:ENTER}} 800 {{key:÷}} {{key:HYP}} {{key:COS}}` | $8.55 \times 10^{-11}$ | $8.55 \times 10^{-11}$ | $200.5212$ | $1.007823$ | Dimensionless catenary height ratio |
| `1 {{key:-}} 800 {{key:×}}` | $8.55 \times 10^{-11}$ | $8.55 \times 10^{-11}$ | $200.5212$ | **$6.2581$** | Conductor mid-span sag $\Delta y$ (meters) |

In nuclear engineering, a cylindrical heavy-water reactor core of radius $R = 1.80\text{ m}$, height $H = 3.60\text{ m}$, and peak volumetric power density $q_0''' = 120\text{ MW/m}^3$ has radial neutron flux governed by Bessel's drumhead mode $J_0(2.40483\,r/R) \approx 1 - \frac{1}{4}u^2 + \frac{1}{64}u^4$ (with $j_{0,1}/R \approx 1.3361\text{ m}^{-1}$). Integrating the 3-term Horner-nested quartic radial ring integrand `R 1.3361 × x² ENTER ENTER 0.015625 × 0.25 - × 1 + R × 2 × π ×` over `0 {{key:ENTER}} 1.8 {{key:∫}} R` and scaling by the axial cosine factor $\frac{2}{\pi} q_0''' H = \frac{864}{\pi}$ yields $\mathbf{1,263.13\text{ MW}_{\text{th}}}$—within $4.5\%$ of the exact Bessel $J_0$ thermal output $\mathbf{1,208.5866\text{ MW}_{\text{th}}}$ (or reaching $\mathbf{1,204.2\text{ MW}_{\text{th}}}$ when the next Horner term $-\frac{1}{2304}u^6$ is included).

Evaluating the True-RMS heating integral $V_{\text{rms}} = \sqrt{\frac{1}{T}\int_0^T v(t)^2\,dt}$ on a clipped AC waveform shows why you should never integrate across a sharp slope corner in a single Romberg pass. When a protection varistor clips a $V_p = 170\text{ V}$ sine wave flat at $V_c = 136\text{ V}$, the derivative $v'(\theta)$ jumps discontinuously at the clipping knee $\theta_c = \arcsin(136/170) = \arcsin(0.80) = 0.927295\text{ rad}$, violating the smooth Euler-Maclaurin assumptions. Splitting the quarter-cycle $[0, \pi/2]$ right at $\theta_c$—integrating the smooth rising sine squared $(170\sin\theta)^2$ (`X {{key:SIN}} 170 {{key:×}} {{key:x²}}` in `{{key:EQN}}`) over $[0, \theta_c]$ and adding the flat clamped plateau $136^2(\pi/2 - \theta_c)$ on the stack—computes the exact True-RMS voltage without corner ringing:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:RAD}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Radian mode engaged for trig calculus |
| `0 {{key:ENTER}} 0.8 {{key:ASIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.927295$ | Integration bounds $[0, \theta_c]$ via $\theta_c = \arcsin(0.8)$ |
| `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$3.12 \times 10^{-10}$** | **$6463.4190$** | Integral of $(170\sin\theta)^2$ over rising edge |
| `0.8 {{key:ASIN}} {{key:π}} 2 {{key:÷}} {{key:x⇄y}} {{key:-}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | $0.643501$ | Clipped interval $(\pi/2 - \theta_c)$; rising integral stays in $Y$ |
| `136 {{key:x²}} {{key:×}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | **$11902.1965$** | Flat clamped plateau contribution |
| `{{key:+}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | **$18365.6155$** | Total quarter-cycle energy sum |
| `2 {{key:×}} {{key:π}} {{key:÷}} {{key:√x}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | **$108.1292$** | Mean square normalized and root taken ($V_{\text{rms}}$) |

Finally, many engineering quantities are defined as the ratio of two definite integrals. To locate the center of mass $\bar{x} = \frac{\int_0^2 x\lambda(x)\,dx}{\int_0^2 \lambda(x)\,dx}$ of a tapered turbine spar with linear density $\lambda(x) = 1.5 + 0.8x^2\text{ kg/m}$, store the denominator mass $M = \int_0^2 \lambda(x)\,dx = 5.133333\text{ kg}$ in Variable `A`, evaluate the first moment $M_x = \int_0^2 x\lambda(x)\,dx = 6.200000\text{ kg}\cdot\text{m}$, and divide via `{{key:RCL}} A {{key:÷}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0 {{key:ENTER}} 2` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Integration limits $[0, 2]$ |
| `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$3.24 \times 10^{-11}$** | **$5.133333$** | Romberg evaluates rod mass $M$ (kg) |
| `{{key:STO}} A` | $0.0000$ | $0.0000$ | $3.24 \times 10^{-11}$ | $5.133333$ | Store total mass $M$ in Variable A |
| `0 {{key:ENTER}} 2` | $3.24 \times 10^{-11}$ | $5.133333$ | $0.0000$ | $2.0000$ | Reload integration limits $[0, 2]$ |
| `{{key:∫}} X` | $3.24 \times 10^{-11}$ | $5.133333$ | **$1.87 \times 10^{-11}$** | **$6.200000$** | Romberg evaluates first moment $M_x$ |
| `{{key:RCL}} A {{key:÷}}` | $5.133333$ | $5.133333$ | $1.87 \times 10^{-11}$ | **$1.207792$** | Centroid position $\bar{x} = M_x / M$ (meters) |

The same two-pass chaining determines the *optical mode confinement factor* $\Gamma = \int_{-d}^d |E(x)|^2\,dx / \int_{-5d}^{5d} |E(x)|^2\,dx$ of a double-heterostructure gallium arsenide $\text{GaAs}/\text{AlGaAs}$ quantum-well laser diode, where only the central active layer $[-d, +d]$ stimulates emission while the evanescent wings in $[-5d, +5d]$ remain passive. In normalized half-width units $d = 1$, we model the transverse waveguide intensity profile $|E(x)|^2 = 1.23\,\operatorname{sech}^2(1.23\,x)$ by storing `1.23 X 1.23 {{key:×}} {{key:HYP}} {{key:COS}} {{key:x²}} {{key:÷}}` in `{{key:EQN}}`; as soon as the second limits `-5 ENTER 5` are keyed, the first integral `1.6852` rides up into Register $Z$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:+/-}} {{key:ENTER}} 1 {{key:∫}} X` | $0.0000$ | $0.0000$ | $1.25 \times 10^{-11}$ | $1.6852$ | Core field energy over $[-d, d]$ |
| `{{key:STO}} A` | $0.0000$ | $0.0000$ | $1.25 \times 10^{-11}$ | $1.6852$ | Core energy stored in register A |
| `5 {{key:+/-}} {{key:ENTER}} 5 {{key:∫}} X` | $1.25 \times 10^{-11}$ | $1.6852$ | $2.40 \times 10^{-11}$ | $2.0000$ | Total field energy over $[-5d, 5d]$ |
| `{{key:RCL}} A {{key:x⇄y}} {{key:÷}}` | $1.6852$ | $1.6852$ | $2.40 \times 10^{-11}$ | **$0.8426$** | Optical confinement factor $\Gamma = 84.26\%$ |

---

### Central-Difference Derivatives & James Watt's Flyweight Governor

Turning from definite integrals to the symmetric central-difference formulas $f'(x_0) \approx \frac{f(x_0 + h) - f(x_0 - h)}{2h}$ and $f''(x_0) \approx \frac{f(x_0 + h) - 2f(x_0) + f(x_0 - h)}{h^2}$, both operations execute directly on Registers $X$ and $Y$ without disturbing Registers $Z$ or $T$.

First, verify the exact quadratic cancellation property on $f(x) = x^2$ at $x_0 = 3.0$ (where $f'(3.0) = 2(3.0) = 6.0$) using the $\varepsilon_{\text{mach}}^{1/3}$ step size $h = 10^{-5}$ (total span $2h = 0.00002$). Keying `3.00001 {{key:x²}}` places the forward sample $f(x_0 + h) = 9.0000600001$ in Register $X$; keying `2.99999 {{key:x²}} {{key:-}}` lifts the forward sample into Register $Y$, evaluates $f(x_0 - h) = 8.9999400001$ in Register $X$, and subtracts them so the $+\frac{1}{2}f''(x_0)h^2 = 10^{-10}$ curvature terms cancel to leave $\Delta f = 0.0001200000$ in Register $X$; and dividing by the span `0.00002 {{key:÷}}` returns the exact derivative $\mathbf{6.0000000000}$ in Register $X$.

For the exponential benchmark $f(x) = e^{2x}$ at the origin $x_0 = 0$ with step $h = 10^{-5}$ (symmetric exponents $2x_{\pm} = \pm 2h = \pm 0.00002$ and span denominator $2h = 0.00002$), three stack sequences extract both the first slope $f'(0) = 2$ and the second curvature $f''(0) = 4$ across $(Y, X)$:

* **`{{key:LASTX}}` Exponent Reuse:** Key `0.00002 {{key:ENTER}} {{key:eˣ}}` to place $0.00002$ in Register $Y$ and $e^{0.00002} = 1.0000200002$ in Register $X$ while saving $0.00002$ in `LASTX`. Then key `{{key:LASTX}} {{key:+/-}} {{key:eˣ}} {{key:-}}` to form $e^{2h} - e^{-2h} = 0.0000400000$, and finish with `{{key:x⇄y}} {{key:÷}}` to obtain $f'(0) = \mathbf{2.0000000003}$ while typing `0.00002` only once.
* **Hyperbolic Sine Identity:** Because $\frac{e^{2h} - e^{-2h}}{2h} = 2\frac{\sinh(2h)}{2h}$, keying `0.00002 {{key:HYP}} {{key:SIN}} {{key:LASTX}} {{key:÷}} 2 {{key:×}}` evaluates $f'(0) = \mathbf{2.0000000003}$ in seven keystrokes.
* **Second Derivative $f''(x_0) \approx \frac{f(x_0+h) - 2f(x_0) + f(x_0-h)}{h^2}$:** Adding $e^{2h} + e^{-2h} = 2\cosh(2h)$ instead of subtracting them and dividing by $h^2 = 10^{-10}$ via `0.00002 {{key:HYP}} {{key:COS}} 1 {{key:-}} 2 {{key:×}} 1 {{key:E}} 10 {{key:+/-}} {{key:÷}}` recovers the second derivative $f''(0) = \mathbf{4.000000}$.

Finally, evaluating the polar kinetic-energy equation $E_k = \frac{1}{2}m\left(\dot{r}^2 + v_\theta^2\right)$ for James Watt's centrifugal flyball governor on a brass flyweight of mass $m = 4.0\text{ kg}$ whirling at $\omega = 40.0\text{ rad/s}$ along the cam slot $r(\theta) = 0.15 + 0.05\sin(2\theta)\text{ m}$ at $\theta = \pi/6\text{ rad}$ (`{{key:RAD}}` mode) pairs the radial and tangential velocity components directly across `Register Y` and `Register X`:

1. **Radial cam-sliding velocity in Register $Y$ ($\dot{r} = \omega\frac{dr}{d\theta}$):** Storing $\theta = \pi/6 \approx 0.523599\text{ rad}$ via `{{key:RAD}} {{key:π}} 6 {{key:÷}} {{key:STO}} A`, we evaluate the radial slope $\frac{dr}{d\theta} = 0.10\cos(2\theta) = 0.050000\text{ m/rad}$ either analytically via `2 {{key:×}} {{key:COS}} 0.1 {{key:×}}` or numerically to $\mathcal{O}(h^2)$ accuracy via the central difference $\frac{r(\theta + 10^{-5}) - r(\theta - 10^{-5})}{2 \times 10^{-5}} = \mathbf{0.0500000000\text{ m/rad}}$. Multiplying by $\omega = 40\text{ rad/s}$ and squaring via `40 {{key:×}} {{key:x²}}` places the squared radial sliding speed $\dot{r}^2 = (2.0000\text{ m/s})^2 = \mathbf{4.000000\text{ m}^2/\text{s}^2}$ in Register $X$.
2. **Tangential whirl velocity in Register $X$ ($v_\theta = r\omega$) and Total Kinetic Energy:** Keying `{{key:RCL}} A 2 {{key:×}} {{key:SIN}} 0.05 {{key:×}} 0.15 {{key:+}} 40 {{key:×}}` lifts $\dot{r}^2 = 4.000000$ into Register $Y$ while evaluating the radius $r(\pi/6) = 0.193301\text{ m}$ and tangential whirl speed $v_\theta = 40\,r = \mathbf{7.732051\text{ m/s}}$ in Register $X$. Squaring $v_\theta$, adding $\dot{r}^2$ from Register $Y$, and scaling by $\frac{1}{2}m = 2.0\text{ kg}$ via `{{key:x²}} {{key:+}} 2 {{key:×}}` delivers the flyweight's exact kinetic energy $E_k = \mathbf{127.569226\text{ Joules}}$—just as taking the second central difference $V''(\theta) \approx \frac{V(\theta+h) - 2V(\theta) + V(\theta-h)}{h^2}$ of the governor's effective potential $V(\theta) = mgL(1 - \cos\theta) - \frac{1}{2}m\omega^2 L^2\sin^2\theta$ on $(Y, X)$ certifies whether the equilibrium sleeve angle is dynamically stable ($V''(\theta^*) > 0$).

### Display-Coupled Convergence, Chained Integrals & Endpoint Singularities

When integrating complex physical waveforms on the SC-32, four practical stack techniques let you control speed, accuracy, and boundary behavior:

1. **Controlling Quadrature Speed via Display Precision (`{{key:FIX}}`, `{{key:SCI}}`, `{{key:ENG}}`) & Register $Y$ Error Inspection:**
   Following William Kahan's display-coupled stopping rule {{cite:kahan1979}}, the Romberg engine terminates once two successive diagonal extrapolations $|R(k, j) - R(k, j-1)|$ agree within half an ulp of the active display format (`{{key:FIX}} 3` for a rapid 3-digit field check, or `{{key:SCI}} 9` / `{{key:ALL}}` for full 11-to-12-digit certification), writing the converged definite integral into Register $X$ and the final Richardson truncation uncertainty estimate $\pm\varepsilon$ directly into Register $Y$.
2. **Chaining Integrals via Register $Z$:**
   Because post-integration replaces $(Y, X)$ with $(\pm\varepsilon, I)$ while preserving $Z$ and $T$, typing new limits `c {{key:ENTER}} d` lifts your first integral $I_1$ into Register $Z$ (`1.6852` in our laser confinement example) so $I_1$ and $I_2$ sit ready for immediate ratio or sum chaining.
3. **Splitting Oscillatory or Sharp-Peak Integrands:**
   When an integrand contains a narrow spike (such as a high-$Q$ resonance peak at $x = 10$ inside $[0, 100]$), splitting the interval at the peak ($[0, 10]$ and $[10, 100]$) guarantees that the initial panel samples the apex directly.
4. **Handling Removable $0/0$ Endpoints & Singular Cusp Substitutions:**
   Touching a division-by-zero pole such as $\int_0^1 \frac{1}{x}\,dx$ halts with `DIVIDE BY 0` (Code 01, cleared via `{{key:C}}`). For a removable $0/0$ endpoint such as $\operatorname{Si}(\pi) = \int_0^\pi \frac{\sin x}{x}\,dx \approx 1.8519370520$, displacing the lower limit to $a = 10^{-12}$ converges in four rows, while $x = u^2$ or $x = 1/t$ substitutions in `{{key:EQN}}` tame $1/\sqrt{x}$ cusps and semi-infinite tails.

Pairing symmetric central-difference derivatives with Werner Romberg's Richardson extrapolation turns the four-register stack into a numerical calculus laboratory. Whether extracting local rates of change where odd Taylor errors cancel or integrating non-elementary waveforms across recursive trapezoidal panels, both operations return certified floating-point bounds directly on Registers $Y$ and $X$.
