---
title: "Chapter 8: Slicing Infinity: From Archimedes and Saturn V to Romberg's 4/3 − 1/3 Miracle | Thinking in the Stack (SC-32)"
description: "Explore central-difference numerical derivatives, Archimedes' method of exhaustion, Lewis Fry Richardson's 4/3 - 1/3 error cancellation, and Werner Romberg's adaptive quadrature on the StackCalc SC-32."
---

# Chapter 8: Slicing Infinity: From Archimedes and Saturn V to Romberg's 4/3 − 1/3 Miracle

## The Speedometer at a Single Microsecond: Numerical Derivatives

Picture Launch Complex 39A at Cape Canaveral at the moment the five Rocketdyne F-1 engines ignite beneath the Apollo Saturn V moon rocket. Every single second, the first-stage turbopumps hurl **fifteen metric tons** of kerosene and liquid oxygen into the combustion chambers. As hundreds of tons of propellant roar out the nozzles, the rocket becomes lighter and lighter while the engines thrust harder into the thinning upper atmosphere, pinning the astronauts into their couches as acceleration climbs from $1.25\,g$ at liftoff to $4.5\,g$ just before staging.

In the seventeenth century, **Isaac Newton** and **Gottfried Wilhelm Leibniz** independently discovered that the entire universe of continuous motion is governed by two complementary operations—the two pillars of calculus—linked together as exact inverses by the **Fundamental Theorem of Calculus**:

1. **The Derivative ($\frac{df}{dt}$): How fast is a quantity changing at this exact instant?** If $x(t)$ is the altitude of the Saturn V at time $t$, its derivative $v(t) = \frac{dx}{dt}$ is the instantaneous reading on the rocket's vertical speedometer, and the derivative of velocity $a(t) = \frac{dv}{dt}$ is its instantaneous acceleration.
2. **The Definite Integral ($\int_a^b f(t)\,dt$): How much total change has accumulated across an interval?** Run the film backward from rate of change to total accumulation: the area trapped underneath the acceleration curve from ignition ($t = 0$) to first-stage burnout ($t = T$) is the exact velocity gained by the spacecraft:

$$v(T) = v_0 + \int_0^T a(t)\,dt$$

We begin with the first pillar: how does a digital instrument measure the **instantaneous slope (derivative)** $f'(x)$ of a function at a point $x$ without symbolic algebra?

### Why Straddling the Point Squares Your Accuracy: The Central Difference Formula

In a first calculus class, the derivative is defined by stepping a tiny distance $h$ *forward* to $x + h$ and computing the rise over run of the **one-sided forward difference**:

$$D_{\text{forward}}(h) = \frac{f(x + h) - f(x)}{h}$$

Why is that textbook forward difference a poor choice for real numerical computing? Draw a curve that bends upward like a parabola ($f''(x) > 0$), mark a point $x$, and draw the secant chord from $x$ to $x + h$. Because the curve is bending upward to the right of $x$, the forward chord is systematically **steeper** than the true tangent line at $x$. Specifically, by Brook Taylor's 1715 series expansion:

$$f(x + h) = f(x) + f'(x)h + \frac{1}{2}f''(x)h^2 + \frac{1}{6}f'''(x)h^3 + \dots$$

dividing $f(x + h) - f(x)$ by $h$ leaves a lopsided curvature error of $+\frac{1}{2}f''(x)h$ that shrinks only linearly as $\mathcal{O}(h)$. Worse yet, if you try to shrink that $\mathcal{O}(h)$ error by picking a microscopic step size like $h = 10^{-11}$, then $f(x + h)$ and $f(x)$ agree to their first eleven digits—and subtracting them wipes out almost all of your calculator's precision in a single stroke of **catastrophic subtraction cancellation**.

Now see what happens when you replace the lopsided forward step with pure geometric symmetry. Instead of stepping only to the right, **straddle the point $x$ symmetrically** by stepping backward to $x - h$ and forward to $x + h$:

$$\begin{aligned}
f(x + h) &= f(x) + f'(x)h + \frac{1}{2}f''(x)h^2 + \frac{1}{6}f'''(x)h^3 + \dots \\
f(x - h) &= f(x) - f'(x)h + \frac{1}{2}f''(x)h^2 - \frac{1}{6}f'''(x)h^3 + \dots
\end{aligned}$$

Subtract the second equation from the first and divide by the total span $2h$ to form the **Central Difference Formula**:

$$f'(x) \approx \frac{f(x + h) - f(x - h)}{2h} = f'(x) + \frac{1}{6}f'''(x)h^2 + \mathcal{O}(h^4)$$

Compare the $+\frac{1}{2}f''(x)h^2$ curvature terms on the right and left of $x$: **they share the same sign and cancel each other out to zero!** Geometrically, the chord joining $(x - h, f(x - h))$ and $(x + h, f(x + h))$ tilts almost parallel to the true tangent line at $x$—and for any parabola $f(x) = ax^2 + bx + c$, where $f'''(x) = 0$, the central difference is **100% exact** for *any* step size $h$. Because the leading truncation error now scales as $\mathcal{O}(h^2)$ while floating-point rounding error scales as $\varepsilon_{\text{mach}}/h$, the "Goldilocks" step size sits near the cube root of machine epsilon, $h \approx \varepsilon_{\text{mach}}^{1/3} \approx 10^{-5}$. That balance delivers ten significant digits of derivative accuracy in just two function evaluations.

On the SC-32, the four-register stack models this symmetric central difference naturally: you evaluate the forward point $f(x + h)$ in Register $X$, evaluate the backward point $f(x - h)$ (which lifts $f(x+h)$ into Register $Y$), subtract via `{{key:-}}`, and divide by $2h$ via `{{key:÷}}`. When differentiating $f(x) = e^{2x}$ at the origin $x_0 = 0$, where the exact slope is $f'(0) = 2$, **`{{key:LASTX}}`** and **`{{key:x⇄y}}`** streamline the sequence. Keying `2h {{key:ENTER}} {{key:eˣ}} {{key:LASTX}} {{key:+/-}} {{key:eˣ}} {{key:-}} {{key:x⇄y}} {{key:÷}}` reuses the step $2h$ from `{{key:LASTX}}` without re-typing it, or you can evaluate the hyperbolic sine identity $\frac{e^{2h} - e^{-2h}}{2h} = \frac{\sinh(2h)}{h}$ via `{{key:HYP}} {{key:SIN}}`. Adding $f(x+h)$ and $f(x-h)$ instead of subtracting them cancels the odd terms and isolates the **second derivative** $f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2}$.

In mechanical engineering, derivatives in polar coordinates govern **James Watt's 1788 centrifugal flyball governor**—the spinning brass-weight mechanism that regulated the speed of Industrial Revolution steam engines and inspired James Clerk Maxwell's 1868 foundation of negative-feedback control theory (*"On Governors"*). When a flyweight of mass $m$ whirls at angular speed $\omega$ along a curved cam slot $r(\theta)$, the flyweight simultaneously moves tangentially at speed $v_\theta = r\omega$ and slides radially outward at speed $\dot{r} = \omega\frac{dr}{d\theta}$. Combining those two perpendicular velocity components via Pythagoras ($v^2 = \dot{r}^2 + (r\omega)^2$) gives its exact kinetic energy $E_k = \frac{1}{2}m\omega^2\left[\left(\frac{dr}{d\theta}\right)^2 + r(\theta)^2\right]$ at any cam angle $\theta$.

### Why Richardson Extrapolation Also Accelerates Derivatives (The Five-Point Stencil)

Can we apply the same error-cancellation idea to derivatives that we are about to use on integrals? Return to the Taylor expansion of the central-difference derivative $D(h)$:

$$D(h) = \frac{f(x + h) - f(x - h)}{2h} = f'(x) + c_1 h^2 + c_2 h^4 + \dots \qquad \left(\text{where } c_1 = \frac{1}{6}f'''(x)\right)$$

Because the leading error $c_1 h^2$ scales with the **square** of the step size $h$, evaluating the central difference at step $h$ ($D(h)$) and at twice the step $2h$ ($D(2h)$, whose $h^2$ error is $4\times$ larger) lets us cancel the $h^2$ error completely via $\frac{4 D(h) - D(2h)}{3}$:

$$f'(x) \approx \frac{4 D(h) - D(2h)}{3} = \frac{-f(x + 2h) + 8f(x + h) - 8f(x - h) + f(x - 2h)}{12h} + \mathcal{O}(h^4)$$

This **five-point stencil** ($-1,\; +8,\; 0,\; -8,\; +1$ divided by $12h$) combines two central differences at $h$ and $2h$ in the ratio $\frac{4}{3}$ and $-\frac{1}{3}$, annihilating the third-derivative error $\frac{1}{6}f'''(x)h^2$ and jumping straight to fourth-order accuracy $\mathcal{O}(h^4)$.

### Leibniz's Rule & Parametric Arc Length: How Derivatives Feed Integrals

Before we step from derivatives to integrals, look at how the two pillars of calculus work together in geometry and physics:
* **Parametric & Polar Arc Length ($ds = \sqrt{dx^2 + dy^2}$):** How did **Christiaan Huygens** and **Jakob Bernoulli** measure the exact length of a curved cable or orbit $y = f(x)$ from $x = a$ to $x = b$? Over a tiny horizontal step $dx$, the curve rises by $dy = f'(x)\,dx$. By the Pythagorean theorem, the tiny diagonal hypotenuse element is $ds = \sqrt{dx^2 + dy^2} = \sqrt{1 + [f'(x)]^2}\,dx$. Summing those microscopic hypotenuses via the definite integral gives the universal **Arc Length Formula**:
  $$L = \int_a^b \sqrt{1 + \left[f'(x)\right]^2}\,dx \qquad \text{or in polar coordinates:} \qquad L = \int_{\theta_1}^{\theta_2} \sqrt{r(\theta)^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta$$
  For the catenary cable $y(x) = a\cosh(x/a)$ that we met in Chapter 4, its derivative is $y'(x) = \sinh(x/a)$, and by the hyperbolic identity $1 + \sinh^2(x/a) = \cosh^2(x/a)$, the square root collapses to $\sqrt{1 + [y'(x)]^2} = \cosh(x/a)$.
* **Pappus & Guldinus's Surface of Revolution:** Rotating that arc-length ribbon $ds$ around the $x$-axis (extending Pappus's First Theorem from Chapter 6 to general curved profiles) sweeps out a frustum ring of radius $y(x)$ and circumference $2\pi y(x)$, giving the exact curved surface area of any turned nosecone, parabolic dish, or cooling tower:
  $$S = \int_a^b 2\pi\,y(x)\sqrt{1 + \left[y'(x)\right]^2}\,dx$$
* **Work of a Variable Force & Root-Mean-Square (RMS) Heating Power:**
  * When a constant force $F$ pushes a mass through distance $\Delta x$, work is the product $W = F\Delta x$. When the force varies with position $F(x)$—like a stiffening rally-car suspension spring, gas expanding against a piston ($W = \int_{V_1}^{V_2} P(V)\,dV$), or gravity weakening with altitude—work is the definite integral $W = \int_{x_1}^{x_2} F(x)\,dx$.
  * Similarly, in electrical engineering, the instantaneous heating power dissipated by a time-varying voltage $v(t)$ in a $1\,\Omega$ resistor is $v(t)^2$. The **True Root-Mean-Square (RMS) voltage** is the DC voltage that delivers the same average thermal energy over a period $T$:
    $$V_{\text{rms}} = \sqrt{\frac{1}{T}\int_0^T \left[v(t)\right]^2 dt}$$
    For an undistorted sinusoid $v(t) = V_p\sin\theta$, the average of $\sin^2\theta$ is $\frac{1}{2}$, giving the familiar $V_{\text{rms}} = V_p/\sqrt{2} \approx 0.7071\,V_p$. The moment a varistor, thyristor dimmer, or rectifier clips the waveform, $V_p/\sqrt{2}$ is wrong—and only the integral $\sqrt{\frac{1}{T}\int_0^T v(t)^2\,dt}$ tells the truth.

---

## Trapping Curved Areas: From Archimedes to the Trapezoidal Rule

Turn now to the second pillar of calculus: how do we measure the exact area $\int_a^b f(x)\,dx$ trapped underneath a curved boundary when nature gives us no simple geometric formula?

### Archimedes' Mental Balance Beam and the $1 + \frac{1}{4} + \frac{1}{16}$ Parabolic Cascade

Around 240 BCE in Syracuse, **Archimedes** set himself a challenge that had baffled every Greek geometer since Euclid: if a straight chord slices across a parabola, what is the exact area of the curved **parabolic segment** trapped between the chord and the curve?

In his treatise *Quadrature of the Parabola*—and in a secret companion manuscript called *The Method of Mechanical Theorems*, which remained lost for nearly a millennium until it was discovered underneath the ink of a medieval prayer book (*The Archimedes Palimpsest*) in 1906—Archimedes revealed his two-step attack:

1. **The Mental Lever (Weighing Slices in Equilibrium):** Before writing a formal proof, Archimedes imagined hanging thin vertical strips of the parabola from one end of a physical balance beam and counterbalancing them against strips of a known triangle at the other end of the lever. By comparing the lever arms at every horizontal station $x$, he discovered that the curved parabolic segment balanced at **exact four-thirds ($\frac{4}{3}$)** the weight of the largest inscribed triangle sharing the same base and apex!
2. **The Method of Exhaustion (Filling the Curved Gaps with Triangles):** To prove that $\frac{4}{3}$ ratio beyond a shadow of a doubt, Archimedes inscribed a central triangle of area $A_0$ inside the parabola, leaving two smaller curved parabolic slivers on the left and right. Inside each of those two slivers he inscribed a new triangle, and proved by the quadratic law of the parabola that the combined area of the two new triangles was **exact one-fourth ($\frac{1}{4} A_0$)** of the first triangle. Repeating the construction inside the four remaining slivers added $\left(\frac{1}{4}\right)^2 A_0 = \frac{1}{16} A_0$, then $\frac{1}{64} A_0$, and so on in an infinite geometric series:

$$\text{Area} = A_0 \left( 1 + \frac{1}{4} + \frac{1}{16} + \frac{1}{64} + \dots \right) = A_0 \left( \frac{1}{1 - 1/4} \right) = \mathbf{\frac{4}{3} A_0}$$

One crucial number hides inside Archimedes' 2,260-year-old proof: every time you cut the horizontal span of a parabolic arch in half ($h \to h/2$), the leftover curved gap between the curve and your straight chord shrinks by a factor of **one-fourth ($\frac{1}{4}$)**.

### Slicing Any Curve into Trapezoids—And Why the Error Scales as $h^2$

Now bring Archimedes' insight into modern numerical calculus. To integrate any smooth function $f(x)$ from $x = a$ to $x = b$, we begin by slicing the interval into $N$ equal panels of width $h = \frac{b - a}{N}$.
* If we cap each panel with a flat horizontal roof at the left or right endpoint (a **Riemann step rectangle**), every sloping section of the curve leaves a large right-triangular air gap of width $h$ and height $\Delta y \approx f'(x)h$ at the top of the rectangle. Each panel suffers an $\mathcal{O}(h^2)$ triangular error, and summing across $N = \frac{b-a}{h}$ panels leaves a crude **$\mathcal{O}(h)$ first-order error**.
* If we instead connect the top of each vertical fencepost $(x_i, f(x_i))$ to the next fencepost $(x_{i+1}, f(x_{i+1}))$ with a straight diagonal chord—forming a **trapezoid** of average height $\frac{1}{2}[f(x_i) + f(x_i+1)]$ and area $\frac{h}{2}[f(x_i) + f(x_{i+1})]$—every interior fencepost $f(x_i)$ is shared by two neighboring trapezoids (counted with weight $\frac{1}{2} + \frac{1}{2} = 1$), while the two outer endpoints $f(a)$ and $f(b)$ are counted with weight $\frac{1}{2}$. Summing all $N$ trapezoids yields the **Composite Trapezoidal Rule**:

$$T(h) = h \left[ \frac{1}{2}f(a) + f(a + h) + f(a + 2h) + \dots + f(b - h) + \frac{1}{2}f(b) \right]$$

How much error remains when you approximate a smooth curve with flat-topped trapezoids? Examine a single narrow panel of width $h$. Over any small span, Taylor's theorem tells us that a smooth curve bends locally like a parabola with curvature $f''(x)$, leaving a thin, crescent-shaped **"meniscus" sliver** (Archimedes' exact parabolic segment) between the true curve and the straight secant chord of the trapezoid:
1. The **width** of the meniscus sliver is $h$.
2. Because parabolic deflection grows with the square of distance from the midpoint, the maximum vertical **sag (thickness)** of the sliver at the center of the panel is proportional to $h^2$ (specifically, $\frac{1}{8}f''(x)h^2$).
3. By Archimedes' parabolic area theorem, the area of a parabolic segment is $\frac{2}{3} \times \text{base} \times \text{height}$, so the area of **one** meniscus sliver scales as $\frac{2}{3} \times h \times \frac{1}{8}f''(x)h^2 = \frac{1}{12}f''(x)h^3 \propto h^3$.
4. Finally, when we add up the slivers across all $N = \frac{b - a}{h}$ panels spanning the interval $[a, b]$, one power of $h$ cancels against $1/h$:

$$\text{Total Trapezoidal Error } E(h) = T(h) - \int_a^b f(x)\,dx \approx \frac{b - a}{12} f''(\xi)\, h^2 \propto \mathcal{O}(h^2)$$

The sign of that error has a clear geometric meaning. When a curve is **concave up** ($f''(x) > 0$, like $e^x$ or $x^2$), the straight secant chord of each trapezoid stretches *above* the sagging curve, so $T(h)$ slightly **overestimates** the integral. When a curve is **concave down** ($f''(x) < 0$, like $\sin x$ on $[0, \pi]$ or $\ln x$), the straight chord cuts *underneath* the arch, so $T(h)$ slightly **underestimates** the integral.

Most importantly, look at what the $h^2$ scaling law means: whenever you slice an interval into twice as many trapezoids—cutting the step width in half ($h \to h/2$)—the total error shrinks by a factor of $\left(\frac{1}{2}\right)^2 = \mathbf{\frac{1}{4}}$, just as Archimedes found in 240 BCE.

At first glance, that $1/4$ ratio looks like a computational bottleneck. If each doubling of your work only trims the error by a factor of $4$, then to reach twelve decimal digits of precision ($10^{-12} \approx 4^{-20}$) by brute force, you would have to evaluate $2^{20} \approx \mathbf{1,048,576\text{ trapezoids}}$—grinding away for minutes on a pocket processor. How do we leap across twenty doublings in just four or five steps?

---

## The 4/3 Minus 1/3 Miracle: Richardson Extrapolation & Romberg Integration

In 1910–1911, the English physicist, meteorologist, and Quaker pacifist **Lewis Fry Richardson** {{cite:richardson1911}}—who famously dreamed of forecasting the weather by solving fluid-dynamics equations by hand while driving a front-line ambulance in World War I, and who later discovered the fractal scaling of the **Coastline of Britain**—looked at that $1/4$ error ratio and saw not a curse, but an **extraordinary mathematical lever**.

Imagine measuring a rugged coastline—or the area under a curve—first with a coarse step size $h$, giving the trapezoidal estimate $T_{\text{coarse}} = T(h)$, and then cutting the step size in half once to $h/2$, giving the fine trapezoidal estimate $T_{\text{fine}} = T(h/2)$.

First, that halving step wastes nothing. When you refine $N$ panels of width $h$ into $2N$ panels of width $h/2$, every single vertical fencepost of the coarse grid is *already* an even-numbered fencepost of the fine grid:

$$T\!\left(\frac{h}{2}\right) = \frac{1}{2} T(h) + \frac{h}{2} \sum_{m=1}^{N} f\!\left(a + \left(m - \frac{1}{2}\right)h\right)$$

You never throw away a single function evaluation from your earlier work—you divide your previous trapezoidal sum $T(h)$ by $2$ and add the newly sampled midpoints.

Second, why does the trapezoidal error expand exclusively in **even** powers of $h$ ($h^2, h^4, h^6, \dots$) with no odd powers ($h^3, h^5, \dots$) anywhere in sight? In the 1730s, **Leonhard Euler** and **Colin Maclaurin** proved one of the most celebrated formulas in mathematical analysis—the **Euler-Maclaurin Summation Formula**:

$$T(h) - \int_a^b f(x)\,dx = \sum_{m=1}^{K} \frac{B_{2m}}{(2m)!} h^{2m} \left[ f^{(2m-1)}(b) - f^{(2m-1)}(a) \right] + \mathcal{O}\!\left(h^{2K+2}\right)$$

where $B_2 = \frac{1}{6},\; B_4 = -\frac{1}{30},\; B_6 = \frac{1}{42},\dots$ are **Jakob Bernoulli's numbers**. Every odd power of $h$ vanishes identically because on every interior boundary $x_i$ between adjacent panels, the derivative contribution from the right end of panel $i$ ($+f^{(k)}(x_i)$) and the left end of panel $i+1$ ($-f^{(k)}(x_i)$) cancel each other out in a **telescoping sum**, leaving only the odd-order derivatives at the outer endpoints $x = a$ and $x = b$ multiplied by even powers of $h$:

$$T(h) = I + c_1 h^2 + c_2 h^4 + c_3 h^6 + \dots$$

Because halving the step size ($h \to h/2$) shrinks the dominant $c_1 h^2$ error term $E = c_1 h^2$ to **exact one-fourth ($\frac{1}{4}E$)** of its previous size while shrinking the $c_2 h^4$ term to $\frac{1}{16}$ of its size, your two estimates form two simple equations in two unknowns:

$$\begin{aligned}
T_{\text{coarse}} &= I + E + c_2 h^4 + \mathcal{O}(h^6) \\
T_{\text{fine}} &= I + \frac{1}{4} E + \frac{1}{16} c_2 h^4 + \mathcal{O}(h^6)
\end{aligned}$$

Why settle for $T_{\text{fine}}$ with its $\frac{1}{4}E$ leftover error when we know that the error in $T_{\text{fine}}$ is *exactly one-fourth* the error in $T_{\text{coarse}}$? Multiply the second equation by $4$, subtract the first equation, and divide by $3$:

$$\frac{4 T_{\text{fine}} - T_{\text{coarse}}}{3} = \frac{4}{3} T_{\text{fine}} - \frac{1}{3} T_{\text{coarse}} = \left(\frac{4}{3} - \frac{1}{3}\right) I + \left(\frac{4}{3}\cdot\frac{1}{4}E - \frac{1}{3}E\right) - \frac{1}{4}c_2 h^4 = \mathbf{I + 0 \cdot E + \mathcal{O}(h^4)}$$

{{blocks:sc32_concept_romberg_quadrature|Symmetric central-difference secant slope cancelation and Romberg trapezoidal halving with Richardson 4^m extrapolation.}}

**The entire leading $h^2$ error vanishes at a single stroke!** Even more wonderfully, see what happens across a single coarse macro-panel of span $h = b - a$ (subdivided into two sub-steps of width $h/2$ at the midpoint $m = \frac{a+b}{2}$) when we write out $T(h) = \frac{h}{2}[f(a) + f(b)]$ and $T(h/2) = \frac{h}{4}[f(a) + 2f(m) + f(b)]$ and substitute them into Richardson's $\frac{4}{3} - \frac{1}{3}$ formula:

$$\frac{4}{3}\left(\frac{h}{4}\big[f(a) + 2f(m) + f(b)\big]\right) - \frac{1}{3}\left(\frac{h}{2}\big[f(a) + f(b)\big]\right) = \frac{h}{6}\Big[ f(a) + 4f(m) + f(b) \Big]$$

Those $1\text{–}4\text{–}1$ weights $\frac{h}{6}[f(a) + 4f(m) + f(b)]$ (with $h = b - a$, or $\frac{\Delta x}{3}$ in terms of the half-step $\Delta x = h/2$) show that Richardson's $\frac{4}{3} - \frac{1}{3}$ combination of two flat-topped trapezoid sums has automatically transformed them into **Thomas Simpson's 1743 Parabolic Rule ($\mathcal{O}(h^4)$)**—the exact area under a smooth parabola fitted through the left endpoint, the midpoint, and the right endpoint. And because the third derivative $f'''(x)$ of any cubic polynomial $Ax^3 + Bx^2 + Cx + D$ is a constant (so $f'''(b) - f'''(a) = 0$ in the $h^2$ term and $f^{(4)}(x) = 0$ in the $h^4$ term), Simpson's $1\text{–}4\text{–}1$ rule is **100% exact not only for parabolas, but for cubics too!**

In 1955, the German-Norwegian physicist **Werner Romberg** {{cite:romberg1955}} realized that you do not have to stop after killing the $h^2$ error. Once you have two Simpson parabolic estimates at step sizes $h$ and $h/2$ across a macro-panel of span $h = b - a$ (subdivided into four sub-steps of width $h/4$ at nodes $x_0, x_1, x_2, x_3, x_4$), their leading $c_2 h^4$ errors stand in the ratio $\left(\frac{1}{2}\right)^4 = \frac{1}{16}$. So taking $\frac{16}{15}S_{\text{fine}} - \frac{1}{15}S_{\text{coarse}}$ annihilates the $h^4$ error and leaps to **George Boole's 5-Point Rule ($\mathcal{O}(h^6)$)** with its classic $7\text{–}32\text{–}12\text{–}32\text{–}7$ weights (where $\frac{h}{90} = \frac{2(h/4)}{45}$):

$$B = \frac{16 S_{\text{fine}} - S_{\text{coarse}}}{15} = \frac{h}{90}\Big[ 7f(x_0) + 32f(x_1) + 12f(x_2) + 32f(x_3) + 7f(x_4) \Big]$$

Arranging each halving $h_k = (b-a)/2^k$ down a lower-triangular table $R(k, j)$ and sweeping across each row via the universal Richardson recurrence:

$$R(k, j) = R(k, j-1) + \frac{R(k, j-1) - R(k-1, j-1)}{4^j - 1}, \qquad \text{Error} = \mathcal{O}\!\left(h_k^{2j+2}\right), \qquad j = 1 \dots \min(k, 5)$$

creates **Romberg Integration** {{cite:romberg1955}}:

| Column Index | Equivalent Classical Quadrature Rule | Error Order | Extrapolation Multiplier |
| :---: | :--- | :---: | :--- |
| **$j = 0$** | Composite Trapezoidal Rule $T(h_k)$ | $\mathcal{O}(h^2)$ | Base midpoint-reuse column |
| **$j = 1$** | Simpson's $1/3$ Parabolic Rule | $\mathcal{O}(h^4)$ | $\frac{4 R(k,0) - R(k-1,0)}{3}$ (kills $h^2$ error) |
| **$j = 2$** | Boole's 5-Point Rule | $\mathcal{O}(h^6)$ | $\frac{16 R(k,1) - R(k-1,1)}{15}$ (kills $h^4$ error) |
| **$j = 3$** | 9-Point Super-Extrapolation | $\mathcal{O}(h^8)$ | $\frac{64 R(k,2) - R(k-1,2)}{63}$ (kills $h^6$ error) |
| **$j = 4, 5$** | Capped High-Order Limit ($j_{\max} = 5$) | $\mathcal{O}(h^{10}) \to \mathcal{O}(h^{12})$ | Prevents high-degree **Runge ringing** |

To see the full triangular tableau $R(k, j)$ in action, trace how each row of $\int_0^2 e^x\,dx = e^2 - 1 \approx \mathbf{6.3890560989}$ feeds the next column to the right:

| Row $k$ (Panels $2^k$) | $j = 0$ (Trapezoid $\mathcal{O}(h^2)$) | $j = 1$ (Simpson $\mathcal{O}(h^4)$) | $j = 2$ (Boole $\mathcal{O}(h^6)$) | $j = 3$ ($\mathcal{O}(h^8)$) |
| :--- | :---: | :---: | :---: | :---: |
| **$k = 0$ ($1$ panel)** | $8.38905610$ | — | — | — |
| **$k = 1$ ($2$ panels)** | $6.91280988$ | **$6.42072780$** | — | — |
| **$k = 2$ ($4$ panels)** | $6.52161011$ | $6.39121019$ | **$6.38924235$** | — |
| **$k = 3$ ($8$ panels)** | $6.42229781$ | $6.38919370$ | $6.38905927$ | **$6.38905637$** |

* **Row $k = 0$ ($1$ trapezoid, $h_0 = 2.0$):** $R(0,0) = \frac{2}{2}(e^0 + e^2) = \mathbf{8.38905610}$ (a $+31.3\%$ overshoot).
* **Row $k = 1$ ($2$ trapezoids, $h_1 = 1.0$):** Adding the single midpoint $e^1$ gives $R(1,0) = \mathbf{6.91280988}$. Applying $\frac{4 R(1,0) - R(0,0)}{3}$ produces $R(1,1) = \mathbf{6.42072780}$, slashing the error by tenfold.
* **Row $k = 2$ ($4$ trapezoids, $h_2 = 0.5$):** Adding the two quarter-points gives $R(2,0) = 6.52161011 \longrightarrow R(2,1) = 6.39121019 \longrightarrow R(2,2) = \frac{16(6.39121019) - 6.42072780}{15} = \mathbf{6.38924235}$ (within $0.0029\%$ of the exact answer using just $5$ function evaluations).
* **Row $k = 3$ ($8$ trapezoids, $h_3 = 0.25$):** With just $9$ function evaluations, $R(3,3) = \mathbf{6.38905637}$ is already accurate to **seven significant digits**, and by Row $k = 4$ ($17$ points), the error drops below $10^{-12}$—outperforming a million raw trapezoids!

On the SC-32, you run this entire Romberg tableau with three natural actions: enter your integrand expression into **`{{key:EQN}}`**, place the lower limit $a$ in **Register $Y$** and the upper limit $b$ in **Register $X$**, and press **`{{key:∫}}`** (Right Shift on `8`) followed by the dummy variable softkey. Why does the SC-32 cap the Romberg tableau at column $j_{\max} = 5$ ($\mathcal{O}(h^{12})$) and split wide intervals ($|b - a| > 20$) across logarithmic `1-2-5` decade boundaries? Because in 1901, German mathematician **Carl David Tolmé Runge** proved that fitting a single ultra-high-degree polynomial across equally spaced points on a wide interval triggers violent boundary oscillations (**Runge's Phenomenon**).

Even better, what if your integrand is a periodic wave like $\cos^2 x$ or a bell curve whose odd derivatives $f^{(2m-1)}(b) - f^{(2m-1)}(a)$ nearly vanish at the boundaries? By the Euler-Maclaurin formula above, when endpoint derivatives match, the Composite Trapezoidal Rule converges **exponentially fast** on its own. Following **William Kahan's** architecture {{cite:kahan1979}}, the SC-32 couples its Romberg stopping tolerance to your active **`{{key:DISP}}`** format (`FIX`, `SCI`, `ENG`, or `ALL`) and upon completion places the certified integral $I$ in **Register $X$** and the estimated truncation uncertainty $\pm\varepsilon$ in **Register $Y$**, while **preserving whatever was previously in Registers $Z$ and $T$** so chained integrals never clobber your upper stack shelves.

---

## When Textbook Antiderivatives Don't Exist: Rockets, Dams & Pendulums

### Why Simple Curves Defy Elementary Antiderivatives

In first-year calculus courses, nearly every homework problem is carefully selected so that you can find a closed-form symbolic antiderivative $F(x)$ and evaluate $F(b) - F(a)$. Yet in 1835, the French mathematician **Joseph Liouville** proved a sobering theorem: while any elementary combination of powers, roots, sines, exponentials, and logarithms can be *differentiated* by mechanical rules, the vast majority of continuous curves encountered in physics **possess no elementary antiderivative at all**.

Take the humble grandfather clock. Every introductory physics student learns Galileo's small-angle formula for a pendulum of length $L$: $T_0 = 2\pi\sqrt{L/g}$. Why did **Christiaan Huygens** discover in his 1673 *Horologium Oscillatorium* that a real pendulum swinging through a wide release angle $\theta_0$ runs noticeably *slower* than $T_0$? Because Galileo's formula replaces $\sin\theta$ with $\theta$. Retaining the exact restoring torque $\sin\theta$ in conservation of energy leads to the **Complete Elliptic Integral of the First Kind** (with modulus $k = \sin(\theta_0/2)$):

$$\frac{T(\theta_0)}{T_0} = \frac{2}{\pi} \int_0^{\pi/2} \frac{d\varphi}{\sqrt{1 - k^2 \sin^2\varphi}}$$

Just like the perimeter of an ellipse in Chapter 6, no finite combination of elementary functions can ever express that integral—yet Romberg quadrature (`{{key:∫}}`) evaluates it to twelve digits in milliseconds. The same barrier arises across quantum physics, optics, and civil engineering. In 1912, when **Peter Debye** explained why the heat capacity $C_V(T)$ of a diamond or copper crystal drops as $T^3$ near absolute zero, quantizing the lattice vibrations led to the non-elementary **Debye Integral**:

$$C_V(T) = 9 N k_B \left(\frac{T}{\Theta_D}\right)^3 \int_0^{\Theta_D / T} \frac{x^4 e^x}{\left(e^x - 1\right)^2}\,dx$$

just as integrating **Max Planck's** spectral radiance across a thermal camera's wavelength window $[\lambda_1, \lambda_2]$ or computing **Carl Friedrich Gauss's** normal error bell $\frac{1}{\sqrt{2\pi}}\int_a^b e^{-x^2/2}\,dx$ defies symbolic antidifferentiation. When coherent light grazes a sharp edge—or when a civil engineer designs a highway exit ramp or roller-coaster loop whose curvature $\kappa(s) \propto s$ ramps up linearly with arc length $s$ so passengers never feel a sudden lateral jerk—the trajectory follows **Augustin-Jean Fresnel's 1818 Diffraction Integrals**, tracing the double-coiled **Euler-Cornu clothoid spiral**:

$$C(u) = \int_0^u \cos\!\left(\frac{\pi t^2}{2}\right) dt, \qquad S(u) = \int_0^u \sin\!\left(\frac{\pi t^2}{2}\right) dt$$

Even when an integrand *does* admit a symbolic antiderivative, integrating the physical rate law in `{{key:EQN}}` via `{{key:∫}}` avoids algebraic transcription errors. That convenience applies whether you are summing the hanging catenary arc length $\int_{-x_0}^{x_0}\cosh(x/a)\,dx$ of a transmission span, the voltage-dependent capacitance droop $C(V) = C_0(1 - \alpha V^2)$ of a ferroelectric $\text{BaTiO}_3$ capacitor {{cite:horowitz2015}}, or the cylindrical velocity rings $\int_0^R 2\pi r\,v(r)\,dr$ of **Hagen-Poiseuille** laminar pipe flow. In laminar pipe flow, because both the cross-sectional area $\pi R^2$ and the parabolic centerline speed $v_{\max} = \frac{\Delta P}{4\mu L}R^2$ scale with $R^2$, integrating the concentric shells yields **Poiseuille's fourth-power law**:

$$Q = \int_0^R 2\pi r\,v_{\max}\!\left(1 - \frac{r^2}{R^2}\right) dr = \frac{1}{2}\pi R^2 v_{\max} = \frac{\pi \Delta P}{8\mu L}\,R^4$$

Why does a $16\%$ plaque constriction to $0.84\,R$ in a human coronary artery cut blood supply in half ($0.84^4 = \mathbf{0.4979}$), whereas a $19\%$ smooth-muscle dilation to $1.19\,R$ during exercise **doubles** blood flow ($1.19^4 = \mathbf{2.0053}$)? Because nature integrates across both radius and velocity at once!

### Taming Improper Integrals & Singular Endpoints by Substitution

What happens when a physical integral has an infinite upper limit $[a, \infty)$ or an integrand whose value or slope blows up at an endpoint, such as the hydrostatic pressure ribbon $(H - y)\sqrt{8y}$ at the floor $y = 0$ of a parabolic canyon dam or an inverse-square-root cusp $\int_0^b \frac{g(x)}{\sqrt{x}}\,dx$? If an endpoint triggers an actual division by zero (such as $\frac{\sin x}{x}$ at $x = 0$), the SC-32 halts safely with **`DIVIDE BY 0`** (Code 01). As codified in the Corvallis *HP-15C Advanced Functions Handbook* and Press et al.'s *Numerical Recipes*, two classical variable substitutions inside `{{key:EQN}}` melt endpoint singularities and infinite tails away before pressing `{{key:∫}}`:

1. **Squaring Away Inverse-Square-Root Cusps ($x = u^2,\; dx = 2u\,du$):** Whenever an integral has an integrable $1/\sqrt{x}$ infinity at $x = 0$ (as happens when a pendulum reaches its turnaround point or light grazes a caustic), substituting $x = u^2$ introduces $dx = 2u\,du$ in the numerator, which cancels $\sqrt{x} = u$ in the denominator identically:
   $$\int_0^b \frac{g(x)}{\sqrt{x}}\,dx = \int_0^{\sqrt{b}} \frac{g(u^2)}{u}\,2u\,du = \int_0^{\sqrt{b}} 2\,g(u^2)\,du$$
   For example, $\int_0^1 \frac{\cos x}{\sqrt{x}}\,dx$ blows up to $+\infty$ at $x = 0$, yet entering the smooth transformed integrand $2\cos(u^2)$ into `{{key:EQN}}` as `U {{key:x²}} {{key:COS}} 2 {{key:×}}` in `{{key:RAD}}` mode and integrating over `0 {{key:ENTER}} 1 {{key:∫}} U` converges in just four Romberg rows to **`1.8090484758`**.
2. **Folding Semi-Infinite Rays onto a Finite Interval ($x = 1/t,\; dx = -dt/t^2$):** When integrating a rapidly decaying tail over $[a, \infty)$ with $a > 0$, substituting $x = 1/t$ maps the infinite horizon $x \to \infty$ to $t \to 0^+$:
   $$\int_a^\infty f(x)\,dx = \int_0^{1/a} \frac{1}{t^2}\,f\!\left(\frac{1}{t}\right) dt$$
   Displacing the lower limit from $0$ to $10^{-12}$ (or truncating a Gaussian or exponential tail at $5$ to $8$ characteristic scale lengths where $e^{-x^2/2}$ has already fallen below machine epsilon) lets Romberg's tableau integrate improper tails to full precision.

---

## On the Stack: Central Differences & Romberg Quadrature

On the SC-32, numerical calculus maps its two-point geometry onto the lower pair of stack registers (`Y` and `X`) while leaving the upper stack (`Z` and `T`) undisturbed:

> **Guided Workflow: Three Steps to Romberg Quadrature (`{{key:∫}}`)**
> 1. **Step 1 — Define the Integrand $f(x)$:** Enter your integrand expression in **`{{key:EQN}}`** (`{{key:↱}}` + `{{key:STO}}`)—or, for a quick manual check on the stack, evaluate the endpoints and midpoint directly with Thomas Simpson's 3-point weights $(1, 4, 1) \times \frac{h}{6}$.
> 2. **Step 2 — Seed the Integration Limits $[a, b]$ on the Stack:** Key the lower limit $a$ into **Register $Y$** and the upper limit $b$ into **Register $X$** via `a {{key:ENTER}} b`.
> 3. **Step 3 — Invoke `{{key:∫}}` (above `{{key:8}}`):** Press `{{key:∫}}` and tap the dummy variable of integration (`X`, `T`, `R`, or `V`). When Richardson's $4^m$ extrapolation converges, the certified definite integral $I = \int_a^b f(x)\,dx$ lands in **Register $X$** and the Romberg truncation error bound $\pm\varepsilon$ lands in **Register $Y$**, while **Registers $Z$ and $T$ remain untouched** for multi-integral chaining!

{{res:sc32_plot_romberg_shaded:screenshot|The SC-32 transflective display executing active numerical integration of 3x² from 0 to 4 (Area = 64.0), demonstrating real-time stack updates and error bound estimation.}}

### Rocket Burnout, Progressive Springs, Hydrostatic Dams & Poiseuille Flow

Unless degrees (`{{key:DEG}}`) are explicitly noted, trigonometric and calculus sequences in this workbench use radian mode (`{{key:RAD}}`). Notice why a single isolated Romberg integral never needs a four-column stack table filled with zeros in Registers $T$ and $Z$: when you key in the integration limits `a {{key:ENTER}} b` and press `{{key:∫}}`, only **Registers $Y$ and $X$** participate in the call, and when extrapolation converges, `{{key:∫}}` replaces $(Y, X)$ in place with the **Post-Integration Audit Frame** $(\pm\varepsilon, I)$ while leaving Registers $Z$ and $T$ untouched for multi-integral chaining:

| Stack Register | Post-`{{key:∫}}` Contents | Engineering Purpose & Chaining Workflow |
| :---: | :--- | :--- |
| **Register $X$** | **Certified Definite Integral ($I = \int_a^b f(x)\,dx$)** | The final Richardson-extrapolated quadrature result. |
| **Register $Y$** | **Estimated Quadrature Uncertainty ($\pm\varepsilon$)** | Upper bound on absolute truncation error. Swap via `{{key:x⇄y}}` to audit convergence. |
| **Register $Z$** | **Prior Register $Z$ (Preserved)** | Holds whatever was in $Z$ when `{{key:∫}}` was pressed (for example, a first integral $I_1$ lifted into $Z$ by typing `c {{key:ENTER}} d` for a second integral). |
| **Register $T$** | **Prior Register $T$ (Preserved)** | Preserves the top of the stack undisturbed across quadrature passes. |

Five mechanical and fluid accumulation laws show how the analytical smoothness of the integrand governs which column of Romberg's tableau delivers the final answer:

* **Cubic Rocket Thrust & Burnout Profiles (Exact in One Richardson Step at $R(1,1)$):** Because Richardson's first $\frac{4}{3} T(h/2) - \frac{1}{3} T(h)$ column $R(1,1)$ is algebraically identical to Thomas Simpson's parabolic rule—whose fourth-order error $\propto f^{(4)}(\xi)\,h^4$ vanishes identically for every polynomial of degree $3$ or less—any cubic velocity or acceleration law hits machine precision on the very first Romberg row!
  * **Sounding Rocket & Cubic Boost:** If a solid-propellant sounding rocket climbs at $v(t) = 30t - 0.5t^3\text{ m/s}$ over $t \in [0, 6]\text{ s}$, one Simpson pass integrates the burnout altitude $\int_0^6 (30t - 0.5t^3)\,dt = [15t^2 - \frac{1}{8}t^4]_0^6 = 378.0\text{ m}$ ($202.5\text{ m}$ over $[0, 3]\text{ s}$ for $45t - 0.5t^3$). For the cubic boost acceleration $a(t) = 4t^2 - 0.5t^3\text{ m/s}^2$, store `T x² 4 × T 3 yˣ 0.5 × -` in `{{key:EQN}}` and key `0 {{key:ENTER}} 6 {{key:∫}} T` to nail the burnout velocity $\left[\frac{4}{3}t^3 - \frac{1}{8}t^4\right]_0^6 = \mathbf{126.000000000\text{ m/s}}$ in Register $X$ ($\pm\varepsilon = 1.24 \times 10^{-11}$ in Register $Y$).
  * **Liquid-Bipropellant Upper Stage:** When an upper stage expels propellant at a constant mass rate so thrust-to-mass acceleration climbs exponentially as $a(t) = 12.0e^{0.04t} - 9.80665\text{ m/s}^2$ over a $25\text{-second}$ burn, integrating via `0 {{key:ENTER}} 25 {{key:∫}} T` yields **$270.3183\text{ m/s}$** in Register $X$ (matching the analytical antiderivative $\Delta v = 300(e^{1.0} - 1) - 245.16625 = \mathbf{270.3183\text{ m/s}}$, where `{{key:LASTX}}` reuses `25` for the gravity-loss subtraction).
* **Progressive Rally-Car Suspension Springs ($W = 33.1875\text{ J}$):** That same exact-cubic property governs the variable-pitch **progressive suspension spring** ($F(x) = 2500x + 40000x^3\text{ N}$) of an off-road rally car. Over small ripples ($x \ll 0.05\text{ m}$), the $2,500\text{ N/m}$ linear rate gives a supple ride; on hard jump landings, the lower coils bind so the $40,000x^3$ stiffening prevents bottoming out (absorbing $[1250x^2 + 10000x^4]_0^{0.50} = 937.5\text{ J}$ over a $0.50\text{ m}$ stroke).
  * **Romberg & Analytical Cross-Check ($x = 0.15\text{ m}$):** Storing `X 2500 × X 3 yˣ 40000 × +` in `{{key:EQN}}` and keying `0 {{key:ENTER}} 0.15 {{key:∫}} X` converges on the first Simpson column to $W = \mathbf{33.187500000\text{ J}}$ ($\pm\varepsilon = 3.55 \times 10^{-12}$ in $Y$), which evaluating $1250x^2 + 10000x^4$ via `{{res:sc32_08_calc_01:keys}}` confirms as $\mathbf{{{res:sc32_08_calc_01:value}}\text{ Joules}}$—$18\%$ above a linear spring's $28.125\text{ J}$.
* **Nonlinear Ferroelectric $\text{BaTiO}_3$ Ceramic Capacitors ($W = 1.09375\text{ J}$):** When a Class-II ferroelectric barium titanate ($\text{BaTiO}_3$) ceramic capacitor saturates under high DC bias as $C(V) = C_0(1 - \alpha V^2)$ with $C_0 = 10\,\mu\text{F}$ and $\alpha = 10^{-6}\text{ V}^{-2}$ {{cite:horowitz2015}}, its differential energy is $dW = C(V)V\,dV = 10^{-5}(V - 10^{-6}V^3)\,dV$.
  * **Setup & Keystrokes:** Store `V 3 yˣ 1E-6 × V x⇄y - 10E-6 ×` in `{{key:EQN}}` and integrate over `0 {{key:ENTER}} 500 {{key:∫}} V` to reveal a true stored energy of **$1.09375\text{ Joules}$**—a $12.5\%$ shortfall below the naive linear estimate $\frac{1}{2}C_0 V^2 = 1.2500\text{ J}$.
* **Parabolic Canyon Spillway Dam (Why Vertical Square-Root Tangents Exercise Higher Romberg Columns):** Why doesn't every integral stop at Row $k = 1$? A vertical floodgate in a **parabolic canyon spillway** of width $w(y) = \sqrt{8y}\text{ m}$ holding back $H = 4.0\text{ m}$ of water ($\rho g = 9,810\text{ N/m}^3$) carries total hydrostatic load $F = 9810\int_0^4 (4-y)\sqrt{8y}\,dy$. Because $(4 - y)\sqrt{8y}$ has an **infinite vertical derivative** $\frac{d}{dy}\sqrt{8y} = \frac{\sqrt{2}}{\sqrt{y}} \to \infty$ at the canyon floor $y = 0$, the Euler-Maclaurin endpoint derivatives blow up and $R(1,1)$ cannot cancel the curvature in one step. Instead, Romberg's tableau subdivides the grid and marches to higher columns $R(k, j)$ until the singular boundary panel is pinched down:
  * **Setup & Keystrokes:** Store `Y 8 × √x 4 Y - × 9810 ×` in `{{key:EQN}}` and key `0 {{key:ENTER}} 4 {{key:∫}} Y` $\longrightarrow$ **$236,773.2915\text{ N}$** ($\pm\varepsilon = 4.18 \times 10^{-10}$ in Register $Y$).
* **Hagen-Poiseuille Laminar Pipe Flow Across Concentric Rings ($4.712389\text{ L/s}$):** In cylindrical **Hagen-Poiseuille laminar pipe flow** of radius $R = 0.05\text{ m}$ ($R^2 = 0.0025\text{ m}^2$) and centerline speed $v_{\max} = 1.2\text{ m/s}$, viscous shear locks velocity to zero at the wall ($r = R$) while the fast centerline core ($r = 0$) has zero circumference ($2\pi r = 0$). Multiplying the parabolic speed $v(r) = v_{\max}(1 - r^2/R^2)$ by $2\pi r$ gives the cubic volumetric ring integrand $2\pi v_{\max}(r - r^3/R^2)$, whose peak contribution sits at $r = R/\sqrt{3} \approx 0.0289\text{ m}$.
  * **Setup & Keystrokes:** Enter `R x² 0.0025 ÷ 1 x⇄y - 1.2 × R × 2 × π ×` into `{{key:EQN}}`, key `0 {{key:ENTER}} 0.05 {{key:∫}} R` ($\to Q = 0.004712389\text{ m}^3/\text{s}$, $\pm\varepsilon = 1.45 \times 10^{-12}$ in $Y$), and scale by `1000 {{key:×}}` $\longrightarrow$ **$4.712389\text{ Liters/second}$**.

---

### Transcendental Integrals, Piecewise RMS Waveforms & Chained Centroids

When we move from algebraic profiles to Gaussian bells, exponential lightning surges, hanging catenary cables, and chained integral ratios, both Euler-Maclaurin endpoint behavior and four-register stack preservation come to the fore.

First, look at how **symmetry and exponential tail cutoffs** tame non-elementary improper integrals over $(-\infty, 0]$ or $[0, \infty)$ right on $(Y, X)$:

* **Gauss's Normal Bell & Vanishing Euler-Maclaurin Endpoint Derivatives ($\int_{-5}^0 \phi(x)\,dx = 0.4999997133$):** The standard normal probability density $\phi(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ has no elementary antiderivative, and its lower tail stretches to $-\infty$. Yet at $x = -5$ (five standard deviations below the mean), $\phi(-5) \approx 1.487 \times 10^{-6}$ has already decayed by six orders of magnitude, while at the symmetry peak $x = 0$ every odd derivative $\phi'(0) = \phi'''(0) = \phi^{(5)}(0) = 0$ vanishes identically! Because the Euler-Maclaurin error series depends only on the odd-order derivatives $f^{(2m-1)}(b) - f^{(2m-1)}(a)$ at the two endpoints, storing `X x² 2 ÷ +/- eˣ 2 π × √x ÷` in `{{key:EQN}}` and integrating across `5 {{key:+/-}} {{key:ENTER}} 0 {{key:∫}} X` converges rapidly to **$0.4999997133$** in Register $X$ ($\pm\varepsilon = 2.15 \times 10^{-10}$ in Register $Y$)—rounding to exact `0.500000` in `FIX 6` and missing only the minuscule five-sigma tail $\Phi(-5) = 2.8665 \times 10^{-7}$.
* **Substation MOV Lightning Surge Arrester Across Five Time Constants ($0.496631027\text{ C}$):** When a direct lightning stroke drives an $i(t) = I_0 e^{-t/\tau}$ current surge ($I_0 = 10\text{ kA} = 10,000\text{ A}$, decay time constant $\tau = 50\,\mu\text{s} = 5 \times 10^{-5}\text{ s}$) through a substation zinc-oxide Metal-Oxide Varistor (MOV), how much total electrical charge $Q = \int i(t)\,dt$ must the varistor blocks absorb during the five-time-constant active clamping window $[0, 5\tau] = [0, 250\,\mu\text{s}]$?
  * **Romberg & Closed-Form Cross-Check:** Storing `T 5E-5 ÷ +/- eˣ 10000 ×` in `{{key:EQN}}` and keying `0 {{key:ENTER}} 0.00025 {{key:∫}} T` integrates the exponential pulse to **$0.496631027\text{ Coulombs}$** in Register $X$ ($\pm\varepsilon = 1.12 \times 10^{-11}$ in Register $Y$). Cross-checking the closed-form antiderivative $I_0\tau(1 - e^{-5})$ on the stack via `{{res:sc32_08_calc_02:keys}}` confirms $\mathbf{{{res:sc32_08_calc_02:value}}\text{ C}}$—showing that five time constants capture $1 - e^{-5} = \mathbf{99.326\%}$ of the infinite-time lightning charge $I_0\tau = 0.5000\text{ C}$.

Now watch what happens across all four stack registers $(T, Z, Y, X)$ when we chain a Romberg integral into a subsequent calculation or combine two definite integrals on the stack. For a high-voltage transmission cable hanging in a **catenary** curve $y(x) = 800\cosh(x/800)$ across a $200\text{-meter}$ river span from $x = -100\text{ m}$ to $+100\text{ m}$, integrating `X 800 ÷ HYP COS` via `{{key:∫}} X` places the conductor arc length $L = 200.5212\text{ m}$ in Register $X$ and its uncertainty $8.55 \times 10^{-11}$ in Register $Y$; as we then compute the mid-span sag $\Delta y = 800[\cosh(100/800) - 1] = 6.2581\text{ m}$ in Register $X$, the arc length $200.5212\text{ m}$ stays live in Register $Y$ while the Romberg uncertainty rides up into Registers $Z$ and $T$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `100 {{key:+/-}} {{key:ENTER}} 100` | $0.0000$ | $0.0000$ | $-100.0000$ | $100.0000$ | Tower span interval $[-100, +100]$ |
| `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$8.55 \times 10^{-11}$** | **$200.5212$** | Conductor total arc length (meters) |
| `100 {{key:ENTER}} 800 {{key:÷}} {{key:HYP}} {{key:COS}}` | $8.55 \times 10^{-11}$ | $8.55 \times 10^{-11}$ | $200.5212$ | $1.007823$ | Dimensionless catenary height ratio |
| `1 {{key:-}} 800 {{key:×}}` | $8.55 \times 10^{-11}$ | $8.55 \times 10^{-11}$ | $200.5212$ | **$6.2581$** | Conductor mid-span sag $\Delta y$ (meters) |

In nuclear engineering, a cylindrical heavy-water reactor core of radius $R = 1.80\text{ m}$, height $H = 3.60\text{ m}$, and peak volumetric power density $q_0''' = 120\text{ MW/m}^3$ has radial neutron flux governed by Bessel's drumhead mode $J_0(2.40483\,r/R) \approx 1 - \frac{1}{4}u^2 + \frac{1}{64}u^4$ (with $j_{0,1}/R \approx 1.3361\text{ m}^{-1}$). Integrating the 3-term Horner-nested quartic radial ring integrand `R 1.3361 × x² ENTER ENTER 0.015625 × 0.25 - × 1 + R × 2 × π ×` over `0 {{key:ENTER}} 1.8 {{key:∫}} R` and scaling by the axial cosine factor $\frac{2}{\pi} q_0''' H = \frac{864}{\pi}$ yields **$1,263.13\text{ MW}_{\text{th}}$**—within $4.5\%$ of the exact Bessel $J_0$ thermal output **$1,208.5866\text{ MW}_{\text{th}}$** (or reaching **$1,204.2\text{ MW}_{\text{th}}$** when the next Horner term $-\frac{1}{2304}u^6$ is included).

Analyzing **piecewise clipped AC waveforms and chained integral ratios** shows why you should never integrate across a sharp slope corner in a single Romberg pass. When a protection varistor clips a $V_p = 170\text{ V}$ AC sine wave flat at $V_c = 136\text{ V}$, the derivative $v'(\theta)$ jumps discontinuously at the clipping knee $\theta_c = \arcsin(136/170) = \arcsin(0.80) = 0.927295\text{ rad}$, violating the smooth Euler-Maclaurin assumptions. Splitting the quarter-cycle $[0, \pi/2]$ right at $\theta_c$—integrating the smooth rising sine squared $(170\sin\theta)^2$ (`X {{key:SIN}} 170 {{key:×}} {{key:x²}}` in `{{key:EQN}}`) over $[0, \theta_c]$ and adding the flat clamped plateau $136^2(\pi/2 - \theta_c)$ on the stack—computes the exact **True-RMS voltage** without corner ringing:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:RAD}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Radian mode engaged for trig calculus |
| `0 {{key:ENTER}} 0.8 {{key:ASIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.927295$ | Integration bounds $[0, \theta_c]$ via $\theta_c = \arcsin(0.8)$ |
| `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$3.12 \times 10^{-10}$** | **$6463.4190$** | Integral of $(170\sin\theta)^2$ over rising edge |
| `0.8 {{key:ASIN}} {{key:π}} 2 {{key:÷}} {{key:x⇄y}} {{key:-}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | $0.643501$ | Clipped interval $(\pi/2 - \theta_c)$; rising integral stays in $Y$ |
| `136 {{key:x²}} {{key:×}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | **$11902.1965$** | Flat clamped plateau contribution |
| `{{key:+}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | **$18365.6155$** | Total quarter-cycle energy sum |
| `2 {{key:×}} {{key:π}} {{key:÷}} {{key:√x}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | **$108.1292$** | Mean square normalized and root taken ($V_{\text{rms}}$) |

Finally, many engineering quantities are defined as the **ratio of two definite integrals**. To locate the center of mass $\bar{x} = \frac{\int_0^2 x\lambda(x)\,dx}{\int_0^2 \lambda(x)\,dx}$ of a tapered turbine spar with linear density $\lambda(x) = 1.5 + 0.8x^2\text{ kg/m}$, store the denominator mass $M = \int_0^2 \lambda(x)\,dx = 5.133333\text{ kg}$ in Variable `A`, evaluate the first moment $M_x = \int_0^2 x\lambda(x)\,dx = 6.200000\text{ kg}\cdot\text{m}$, and divide via `{{key:RCL}} A {{key:÷}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0 {{key:ENTER}} 2` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Integration limits $[0, 2]$ |
| `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$3.24 \times 10^{-11}$** | **$5.133333$** | Romberg evaluates rod mass $M$ (kg) |
| `{{key:STO}} A` | $0.0000$ | $0.0000$ | $3.24 \times 10^{-11}$ | $5.133333$ | Store total mass $M$ in Variable A |
| `0 {{key:ENTER}} 2` | $3.24 \times 10^{-11}$ | $5.133333$ | $0.0000$ | $2.0000$ | Reload integration limits $[0, 2]$ |
| `{{key:∫}} X` | $3.24 \times 10^{-11}$ | $5.133333$ | **$1.87 \times 10^{-11}$** | **$6.200000$** | Romberg evaluates first moment $M_x$ |
| `{{key:RCL}} A {{key:÷}}` | $5.133333$ | $5.133333$ | $1.87 \times 10^{-11}$ | **$1.207792$** | Centroid position $\bar{x} = M_x / M$ (meters) |

The same two-pass chaining determines the **optical mode confinement factor** $\Gamma = \int_{-d}^d |E(x)|^2\,dx / \int_{-5d}^{5d} |E(x)|^2\,dx$ of a double-heterostructure gallium arsenide $\text{GaAs}/\text{AlGaAs}$ quantum-well laser diode, where only the central active layer $[-d, +d]$ stimulates emission while the evanescent wings in $[-5d, +5d]$ remain passive. In normalized half-width units $d = 1$, we model the transverse waveguide intensity profile $|E(x)|^2 = 1.23\,\operatorname{sech}^2(1.23\,x)$ by storing `1.23 X 1.23 {{key:×}} {{key:HYP}} {{key:COS}} {{key:x²}} {{key:÷}}` in `{{key:EQN}}`; as soon as the second limits `-5 ENTER 5` are keyed, the first integral `1.6852` rides up into Register $Z$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:+/-}} {{key:ENTER}} 1 {{key:∫}} X` | $0.0000$ | $0.0000$ | $1.25 \times 10^{-11}$ | $1.6852$ | Core field energy over $[-d, d]$ |
| `{{key:STO}} A` | $0.0000$ | $0.0000$ | $1.25 \times 10^{-11}$ | $1.6852$ | Core energy stored in register A |
| `5 {{key:+/-}} {{key:ENTER}} 5 {{key:∫}} X` | $1.25 \times 10^{-11}$ | $1.6852$ | $2.40 \times 10^{-11}$ | $2.0000$ | Total field energy over $[-5d, 5d]$ |
| `{{key:RCL}} A {{key:x⇄y}} {{key:÷}}` | $1.6852$ | $1.6852$ | $2.40 \times 10^{-11}$ | **$0.8426$** | Optical confinement factor $\Gamma = 84.26\%$ |

---

### Central-Difference Derivatives & James Watt's Flyweight Governor

Turning from definite integrals back to instantaneous rates of change ($\frac{df}{dx}$), notice why symmetric central-difference derivatives $f'(x_0) \approx \frac{f(x_0 + h) - f(x_0 - h)}{2h}$ and second derivatives $f''(x_0) \approx \frac{f(x_0 + h) - 2f(x_0) + f(x_0 - h)}{h^2}$ execute directly on **Registers $X$ and $Y$** without ever needing Registers $Z$ or $T$.

First, verify the **central-difference derivative of a parabola** ($f(x) = x^2$ at $x_0 = 3.0$, where the exact slope is $f'(3.0) = 2(3.0) = 6.0$) at the optimal $\varepsilon_{\text{mach}}^{1/3}$ step size $h = 10^{-5}$ (total span $2h = 0.00002$). Because the third derivative of any quadratic polynomial is identically zero ($f'''(x) = 0$), the $+\frac{1}{2}f''(x_0)h^2$ upward curvature errors at $x_0 + h = 3.00001$ and $x_0 - h = 2.99999$ cancel each other out completely: keying `3.00001 {{key:x²}}` places the forward sample $f(x_0 + h) = 9.0000600001$ in Register $X$; keying `2.99999 {{key:x²}} {{key:-}}` lifts the forward sample into Register $Y$, evaluates $f(x_0 - h) = 8.9999400001$ in Register $X$, and subtracts them so the $10^{-10}$ quadratic curvature terms annihilate each other to leave $\Delta f = 0.0001200000$ in Register $X$; and dividing by the span `0.00002 {{key:÷}}` returns the exact derivative **$6.0000000000$** in Register $X$.

When differentiating the **exponential curve at the origin** ($f(x) = e^{2x}$ at $x_0 = 0$) with step $h = 10^{-5}$ (so the symmetric exponents are $2x_{\pm} = \pm 2h = \pm 0.00002$ and the span denominator is $2h = 0.00002$), three stack workflows extract both the first slope $f'(0) = 2$ and the second curvature $f''(0) = 4$ across $(Y, X)$:
* **Method A — `{{key:LASTX}}` Exponent Reuse:** Key `0.00002 {{key:ENTER}} {{key:eˣ}}` to place $0.00002$ in Register $Y$ and $e^{0.00002} = 1.0000200002$ in Register $X$ while saving $0.00002$ in `LASTX`. Then key `{{key:LASTX}} {{key:+/-}} {{key:eˣ}} {{key:-}}` to form $e^{2h} - e^{-2h} = 0.0000400000$, and finish with `{{key:x⇄y}} {{key:÷}}` to obtain **$f'(0) = 2.0000000003$** while typing `0.00002` only once.
* **Method B — Hyperbolic Sine Identity:** Because $\frac{e^{2h} - e^{-2h}}{2h} = 2\frac{\sinh(2h)}{2h}$, keying `0.00002 {{key:HYP}} {{key:SIN}} {{key:LASTX}} {{key:÷}} 2 {{key:×}}` evaluates $f'(0) = \mathbf{2.0000000003}$ in seven keystrokes.
* **Method C — Second Derivative $f''(x_0) \approx \frac{f(x_0+h) - 2f(x_0) + f(x_0-h)}{h^2}$:** Adding $e^{2h} + e^{-2h} = 2\cosh(2h)$ instead of subtracting them and dividing by $h^2 = 10^{-10}$ via `0.00002 {{key:HYP}} {{key:COS}} 1 {{key:-}} 2 {{key:×}} 1 {{key:E}} 10 {{key:+/-}} {{key:÷}}` recovers the second derivative **$f''(0) = 4.000000$**.

Finally, in mechanical feedback control, **James Watt's 1788 centrifugal flyball governor** regulates engine speed through the balance of polar derivatives on `Register X` and `Register Y`. As a brass flyweight of mass $m = 4.0\text{ kg}$ whirls at angular speed $\omega = 40.0\text{ rad/s}$ along a curved cam slot $r(\theta) = 0.15 + 0.05\sin(2\theta)\text{ m}$ at inclination angle $\theta = \pi/6\text{ rad}$ in `{{key:RAD}}` mode, its total kinetic energy $E_k = \frac{1}{2}m\left(\dot{r}^2 + v_\theta^2\right)$ couples two perpendicular velocities across $(Y, X)$:
1. **Radial cam-sliding velocity in Register $Y$ ($\dot{r} = \omega\frac{dr}{d\theta}$):** Storing $\theta = \pi/6 \approx 0.523599\text{ rad}$ via `{{key:RAD}} {{key:π}} 6 {{key:÷}} {{key:STO}} A`, we evaluate the radial slope $\frac{dr}{d\theta} = 0.10\cos(2\theta) = 0.050000\text{ m/rad}$ either analytically via `2 {{key:×}} {{key:COS}} 0.1 {{key:×}}` or numerically to $\mathcal{O}(h^2)$ accuracy via the central difference $\frac{r(\theta + 10^{-5}) - r(\theta - 10^{-5})}{2 \times 10^{-5}} = \mathbf{0.0500000000\text{ m/rad}}$. Multiplying by $\omega = 40\text{ rad/s}$ and squaring via `40 {{key:×}} {{key:x²}}` places the squared radial sliding speed $\dot{r}^2 = (2.0000\text{ m/s})^2 = \mathbf{4.000000\text{ m}^2/\text{s}^2}$ in Register $X$.
2. **Tangential whirl velocity in Register $X$ ($v_\theta = r\omega$) and Total Kinetic Energy:** Keying `{{key:RCL}} A 2 {{key:×}} {{key:SIN}} 0.05 {{key:×}} 0.15 {{key:+}} 40 {{key:×}}` lifts $\dot{r}^2 = 4.000000$ into Register $Y$ while evaluating the radius $r(\pi/6) = 0.193301\text{ m}$ and tangential whirl speed $v_\theta = 40\,r = \mathbf{7.732051\text{ m/s}}$ in Register $X$. Squaring $v_\theta$, adding $\dot{r}^2$ from Register $Y$, and scaling by $\frac{1}{2}m = 2.0\text{ kg}$ via `{{key:x²}} {{key:+}} 2 {{key:×}}` delivers the flyweight's exact kinetic energy $E_k = \mathbf{127.569226\text{ Joules}}$—just as taking the second central difference $V''(\theta) \approx \frac{V(\theta+h) - 2V(\theta) + V(\theta-h)}{h^2}$ of the governor's effective potential $V(\theta) = mgL(1 - \cos\theta) - \frac{1}{2}m\omega^2 L^2\sin^2\theta$ on $(Y, X)$ certifies whether the equilibrium sleeve angle is dynamically stable ($V''(\theta^*) > 0$).

### Practical Quadrature Hygiene: Display-Coupled Stopping, Chaining & Singularity Traps

When integrating complex physical waveforms on the SC-32, four practical stack techniques let you control speed, accuracy, and boundary behavior:

1. **Controlling Quadrature Speed via Display Precision (`{{key:FIX}}`, `{{key:SCI}}`, `{{key:ENG}}`):**
   Following William Kahan's display-coupled stopping rule {{cite:kahan1979}}, the SC-32 Romberg engine terminates as soon as two successive diagonal extrapolations $|R(k, j) - R(k, j-1)|$ agree to within half an ulp of the currently displayed decimal format:
   * If you need a fast 3-digit field check of a slow transcendental integrand, set `{{key:FIX}} 3` before pressing `{{key:∫}}`.
   * When you want full 11-to-12-digit certification, set `{{key:SCI}} 9` or `{{key:ALL}}`.
2. **Chaining Integrals via Register $Z$:**
   Because the post-integration stack frame replaces $(Y, X)$ with $(\pm\varepsilon, I)$ while preserving whatever was previously in Registers $Z$ and $T$, typing two new integration limits `c {{key:ENTER}} d` automatically lifts your first integral $I_1$ into **Register $Z$** (and its uncertainty $\pm\varepsilon_1$ into **Register $T$**). When the second `{{key:∫}}` finishes, $I_1$ is still sitting untouched in Register $Z$ (`1.6852` in our laser confinement example above) while $I_2$ sits in Register $X$, ready for chaining!
3. **Splitting Oscillatory or Sharp-Peak Integrands:**
   If an integrand contains a narrow spike inside a wide interval—such as a high-$Q$ resonance peak sitting at $x = 10$ inside $[0, 100]$—a coarse initial grid on $[0, 100]$ might step right over the spike. Splitting the interval at the known peak location ($[0, 10]$ and $[10, 100]$) guarantees that the initial Romberg panel samples the peak at its apex.
4. **Handling Removable $0/0$ Endpoints & Singular Cusp Substitutions:**
   If an integration interval $[a, b]$ touches a division-by-zero pole such as $\int_0^1 \frac{1}{x}\,dx$, the SC-32 halts with **`DIVIDE BY 0`** (Code 01, cleared non-destructively via `{{key:C}}`). For a removable $0/0$ endpoint singularity such as the **Sine Integral** $\operatorname{Si}(\pi) = \int_0^\pi \frac{\sin x}{x}\,dx \approx 1.8519370520$, displacing the lower limit to $a = 10^{-12}$ lets Romberg converge in four rows—while for integrable $1/\sqrt{x}$ cusps or semi-infinite $[a, \infty)$ tails, applying the $x = u^2$ or $x = 1/t$ variable substitutions inside `{{key:EQN}}` restores smooth, rapid convergence.

---

### From Smooth Curves to Noisy Human Measurements

Whether differentiating James Watt's governor cam $r(\theta)$ across a $2 \times 10^{-5}\text{ rad}$ span or cancelling $h^2$ meniscus errors across Romberg's $\frac{4}{3} - \frac{1}{3}$ tableau, every calculation in this chapter relied on one unspoken luxury: **we already knew the exact, smooth mathematical formula $f(x)$ governing the curve**. Because $f(x)$ was deterministic and noise-free, sampling $f(x + h)$ and $f(x - h)$ at closely spaced points allowed Taylor series errors to cancel to twelve decimal places.

What happens when you step out of the mathematical theorist's study and into an astronomical observatory, a wind tunnel, a metallurgy lab, or a quality-control testing room? In the experimental world, nature never hands you a noiseless formula $y = f(x)$ printed on a silver platter. Instead, she hands you a cloud of **imperfect human measurements**—telescope right-ascension sightings jittering in atmospheric turbulence, strain-gauge voltages quivering with thermal Johnson-Nyquist noise, or steel fatigue coupons that scatter across the graph paper because no two batches of crystalline metal are ever microscopically identical.

When your data points contain random scatter, you cannot take $\frac{y_{i+1} - y_{i-1}}{2\Delta x}$ between two neighboring points, because dividing tiny random measurement jitter by a small step $\Delta x$ amplifies the noise into wild, meaningless spikes. Instead of passing a jagged curve through every noisy dot, you need a mathematical way to let the random upward errors and downward errors cancel each other out across the entire dataset—extracting the calm, underlying signal from the storm of measurement uncertainty.

If every single observation contains random error, how can you possibly discover the true physical law hiding underneath the noise? Why does sample standard deviation divide by $n - 1$ instead of $n$? And how can six simple running totals in calculator memory remember the exact best-fit line through a hundred data points without storing the hundred points themselves? In **[Chapter 9: Taming Uncertainty: How Gauss Found a Lost Planet and a Brewery Invented Modern Statistics](09-statistics-curve-fitting.md)**, we travel to Palermo and Göttingen on New Year's Night 1801 to witness the birth of Least Squares, watch lead shot cascade through Sir Francis Galton's Quincunx into the Normal Bell Curve, and meet the Guinness brewery chemist who invented small-sample science.
