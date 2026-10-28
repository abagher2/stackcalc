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

Let us start with the first pillar: how does a digital instrument measure the **instantaneous slope (derivative)** $f'(x)$ of a function at a point $x$ without doing symbolic algebra?

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

Compare the $+\frac{1}{2}f''(x)h^2$ curvature terms on the right and left of $x$: **they have the exact same sign and cancel each other out to zero!** Geometrically, the chord joining $(x - h, f(x - h))$ and $(x + h, f(x + h))$ tilts almost parallel to the true tangent line at $x$ (and for any parabola $f(x) = ax^2 + bx + c$, where $f'''(x) = 0$, the central difference is **100% exact** for *any* step size $h$). Because the leading truncation error now scales as $\mathcal{O}(h^2)$ while floating-point rounding error scales as $\varepsilon_{\text{mach}}/h$, the "Goldilocks" step size sits near the cube root of machine epsilon, $h \approx \varepsilon_{\text{mach}}^{1/3} \approx 10^{-5}$—delivering ten significant digits of derivative accuracy in just two function evaluations.

On the SC-32, the four-register stack models this symmetric central difference naturally: you evaluate the forward point $f(x + h)$ in Register $X$, evaluate the backward point $f(x - h)$ (which lifts $f(x+h)$ into Register $Y$), subtract via `{{key:-}}`, and divide by $2h$ via `{{key:÷}}`. When differentiating $f(x) = e^{2x}$ at the origin $x_0 = 0$ (where the exact slope is $f'(0) = 2$), **`{{key:LASTX}}`** and **`{{key:x⇄y}}`** make the workflow even cleaner—keying `2h {{key:ENTER}} {{key:eˣ}} {{key:LASTX}} {{key:+/-}} {{key:eˣ}} {{key:-}} {{key:x⇄y}} {{key:÷}}` reuses the step $2h$ from `{{key:LASTX}}` without re-typing it, or you can invoke the hyperbolic sine identity $\frac{e^{2h} - e^{-2h}}{2h} = \frac{\sinh(2h)}{h}$ directly via `{{key:HYP}} {{key:SIN}}`. (Adding $f(x+h)$ and $f(x-h)$ instead of subtracting them cancels the odd terms and isolates the **second derivative** $f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2}$.)

In mechanical engineering, derivatives in polar coordinates govern **James Watt's 1788 centrifugal flyball governor**—the spinning brass-weight mechanism that regulated the speed of Industrial Revolution steam engines and inspired James Clerk Maxwell's 1868 foundation of negative-feedback control theory (*"On Governors"*). When a flyweight of mass $m$ whirls at angular speed $\omega$ along a curved cam slot $r(\theta)$, the flyweight simultaneously moves tangentially at speed $v_\theta = r\omega$ and slides radially outward at speed $\dot{r} = \omega\frac{dr}{d\theta}$. Combining those two perpendicular velocity components via Pythagoras ($v^2 = \dot{r}^2 + (r\omega)^2$) gives its exact kinetic energy $E_k = \frac{1}{2}m\omega^2\left[\left(\frac{dr}{d\theta}\right)^2 + r(\theta)^2\right]$ at any cam angle $\theta$.

### Why Richardson Extrapolation Also Accelerates Derivatives (The Five-Point Stencil)

Can we apply the same error-cancellation idea to derivatives that we are about to use on integrals? Return to the Taylor expansion of the central-difference derivative $D(h)$:

$$D(h) = \frac{f(x + h) - f(x - h)}{2h} = f'(x) + c_1 h^2 + c_2 h^4 + \dots \qquad \left(\text{where } c_1 = \frac{1}{6}f'''(x)\right)$$

Because the leading error $c_1 h^2$ scales with the **square** of the step size $h$, evaluating the central difference at step $h$ ($D(h)$) and at twice the step $2h$ ($D(2h)$, whose $h^2$ error is $4\times$ larger) lets us cancel the $h^2$ error completely via $\frac{4 D(h) - D(2h)}{3}$:

$$f'(x) \approx \frac{4 D(h) - D(2h)}{3} = \frac{-f(x + 2h) + 8f(x + h) - 8f(x - h) + f(x - 2h)}{12h} + \mathcal{O}(h^4)$$

This **five-point stencil** ($-1,\; +8,\; 0,\; -8,\; +1$ divided by $12h$) combines two central differences at $h$ and $2h$ in the ratio $\frac{4}{3}$ and $-\frac{1}{3}$, annihilating the third-derivative error $\frac{1}{6}f'''(x)h^2$ and jumping straight to fourth-order accuracy $\mathcal{O}(h^4)$.

### Leibniz's Rule & Parametric Arc Length: How Derivatives Feed Integrals

Before we step from derivatives to integrals, consider how the two pillars of calculus work together in geometry and physics:
* **Parametric & Polar Arc Length ($ds = \sqrt{dx^2 + dy^2}$):** How did **Christiaan Huygens** and **Jakob Bernoulli** measure the exact length of a curved cable or orbit $y = f(x)$ from $x = a$ to $x = b$? Over a tiny horizontal step $dx$, the curve rises by $dy = f'(x)\,dx$. By the Pythagorean theorem, the tiny diagonal hypotenuse element is $ds = \sqrt{dx^2 + dy^2} = \sqrt{1 + [f'(x)]^2}\,dx$. Summing those microscopic hypotenuses via the definite integral gives the universal **Arc Length Formula**:
  $$L = \int_a^b \sqrt{1 + \left[f'(x)\right]^2}\,dx \qquad \text{or in polar coordinates:} \qquad L = \int_{\theta_1}^{\theta_2} \sqrt{r(\theta)^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta$$
  For the catenary cable $y(x) = a\cosh(x/a)$ that we met in Chapter 4, its derivative is $y'(x) = \sinh(x/a)$, and by the hyperbolic identity $1 + \sinh^2(x/a) = \cosh^2(x/a)$, the square root simplifies cleanly to $\sqrt{1 + [y'(x)]^2} = \cosh(x/a)$.
* **Pappus & Guldinus's Surface of Revolution:** Rotating that arc-length ribbon $ds$ around the $x$-axis (extending Pappus's First Theorem from Chapter 6 to general curved profiles) sweeps out a frustum ring of radius $y(x)$ and circumference $2\pi y(x)$, giving the exact curved surface area of any turned nosecone, parabolic dish, or cooling tower:
  $$S = \int_a^b 2\pi\,y(x)\sqrt{1 + \left[y'(x)\right]^2}\,dx$$
* **Work of a Variable Force & Root-Mean-Square (RMS) Heating Power:**
  * When a constant force $F$ pushes a mass through distance $\Delta x$, work is simply $W = F\Delta x$. When the force varies with position $F(x)$—like a stiffening rally-car suspension spring, gas expanding against a piston ($W = \int_{V_1}^{V_2} P(V)\,dV$), or gravity weakening with altitude—work is the definite integral $W = \int_{x_1}^{x_2} F(x)\,dx$.
  * Similarly, in electrical engineering, the instantaneous heating power dissipated by a time-varying voltage $v(t)$ in a $1\,\Omega$ resistor is $v(t)^2$. The **True Root-Mean-Square (RMS) voltage** is the DC voltage that delivers the exact same average thermal energy over a period $T$:
    $$V_{\text{rms}} = \sqrt{\frac{1}{T}\int_0^T \left[v(t)\right]^2 dt}$$
    For an undistorted sinusoid $v(t) = V_p\sin\theta$, the average of $\sin^2\theta$ is $\frac{1}{2}$, giving the familiar $V_{\text{rms}} = V_p/\sqrt{2} \approx 0.7071\,V_p$. The moment a varistor, thyristor dimmer, or rectifier clips the waveform, $V_p/\sqrt{2}$ is wrong—and only the integral $\sqrt{\frac{1}{T}\int_0^T v(t)^2\,dt}$ tells the truth.

---

## Trapping Curved Areas: From Archimedes to the Trapezoidal Rule

Now let us turn to the second pillar of calculus: how do we measure the exact area $\int_a^b f(x)\,dx$ trapped underneath a curved boundary when nature gives us no simple geometric formula?

### Archimedes' Mental Balance Beam and the $1 + \frac{1}{4} + \frac{1}{16}$ Parabolic Cascade

Around 240 BCE in Syracuse, **Archimedes** set himself a challenge that had baffled every Greek geometer since Euclid: if a straight chord slices across a parabola, what is the exact area of the curved **parabolic segment** trapped between the chord and the curve?

In his treatise *Quadrature of the Parabola*—and in a secret companion manuscript called *The Method of Mechanical Theorems*, which remained lost for nearly a millennium until it was discovered underneath the ink of a medieval prayer book (*The Archimedes Palimpsest*) in 1906—Archimedes revealed his two-step attack:

1. **The Mental Lever (Weighing Slices in Equilibrium):** Before writing a formal proof, Archimedes imagined hanging thin vertical strips of the parabola from one end of a physical balance beam and counterbalancing them against strips of a known triangle at the other end of the lever. By comparing the lever arms at every horizontal station $x$, he discovered that the curved parabolic segment balanced at **exact four-thirds ($\frac{4}{3}$)** the weight of the largest inscribed triangle sharing the same base and apex!
2. **The Method of Exhaustion (Filling the Curved Gaps with Triangles):** To prove that $\frac{4}{3}$ ratio beyond a shadow of a doubt, Archimedes inscribed a central triangle of area $A_0$ inside the parabola, leaving two smaller curved parabolic slivers on the left and right. Inside each of those two slivers he inscribed a new triangle, and proved by the quadratic law of the parabola that the combined area of the two new triangles was **exact one-fourth ($\frac{1}{4} A_0$)** of the first triangle. Repeating the construction inside the four remaining slivers added $\left(\frac{1}{4}\right)^2 A_0 = \frac{1}{16} A_0$, then $\frac{1}{64} A_0$, and so on in an infinite geometric series:

$$\text{Area} = A_0 \left( 1 + \frac{1}{4} + \frac{1}{16} + \frac{1}{64} + \dots \right) = A_0 \left( \frac{1}{1 - 1/4} \right) = \mathbf{\frac{4}{3} A_0}$$

One crucial number hides inside Archimedes' 2,260-year-old proof: every time you cut the horizontal span of a parabolic arch in half ($h \to h/2$), the leftover curved gap between the curve and your straight chord shrinks by a factor of **one-fourth ($\frac{1}{4}$)**.

### Slicing Any Curve into Trapezoids—And Why the Error Scales as $h^2$

Now let us bring Archimedes' insight into modern numerical calculus. Suppose we want to integrate any smooth function $f(x)$ from $x = a$ to $x = b$ by slicing the interval into $N$ equal panels of width $h = \frac{b - a}{N}$.
* If we cap each panel with a flat horizontal roof at the left or right endpoint (a **Riemann step rectangle**), every sloping section of the curve leaves a large right-triangular air gap of width $h$ and height $\Delta y \approx f'(x)h$ at the top of the rectangle. Each panel suffers an $\mathcal{O}(h^2)$ triangular error, and summing across $N = \frac{b-a}{h}$ panels leaves a crude **$\mathcal{O}(h)$ first-order error**.
* If we instead connect the top of each vertical fencepost $(x_i, f(x_i))$ to the next fencepost $(x_{i+1}, f(x_{i+1}))$ with a straight diagonal chord—forming a **trapezoid** of average height $\frac{1}{2}[f(x_i) + f(x_{i+1})]$ and area $\frac{h}{2}[f(x_i) + f(x_{i+1})]$—every interior fencepost $f(x_i)$ is shared by two neighboring trapezoids (counted with weight $\frac{1}{2} + \frac{1}{2} = 1$), while the two outer endpoints $f(a)$ and $f(b)$ are counted with weight $\frac{1}{2}$. Summing all $N$ trapezoids yields the **Composite Trapezoidal Rule**:

$$T(h) = h \left[ \frac{1}{2}f(a) + f(a + h) + f(a + 2h) + \dots + f(b - h) + \frac{1}{2}f(b) \right]$$

How much error remains when you approximate a smooth curve with flat-topped trapezoids? Examine a single narrow panel of width $h$. Over any small span, Taylor's theorem tells us that a smooth curve bends locally like a parabola with curvature $f''(x)$, leaving a thin, crescent-shaped **"meniscus" sliver** (Archimedes' exact parabolic segment) between the true curve and the straight secant chord of the trapezoid:
1. The **width** of the meniscus sliver is $h$.
2. Because parabolic deflection grows with the square of distance from the midpoint, the maximum vertical **sag (thickness)** of the sliver at the center of the panel is proportional to $h^2$ (specifically, $\frac{1}{8}f''(x)h^2$).
3. By Archimedes' parabolic area theorem, the area of a parabolic segment is $\frac{2}{3} \times \text{base} \times \text{height}$, so the area of **one** meniscus sliver scales as $\frac{2}{3} \times h \times \frac{1}{8}f''(x)h^2 = \frac{1}{12}f''(x)h^3 \propto h^3$.
4. Finally, when we add up the slivers across all $N = \frac{b - a}{h}$ panels spanning the interval $[a, b]$, one power of $h$ cancels against $1/h$:

$$\text{Total Trapezoidal Error } E(h) = T(h) - \int_a^b f(x)\,dx \approx \frac{b - a}{12} f''(\xi)\, h^2 \propto \mathcal{O}(h^2)$$

The sign of that error has a clear geometric meaning. When a curve is **concave up** ($f''(x) > 0$, like $e^x$ or $x^2$), the straight secant chord of each trapezoid stretches *above* the sagging curve, so $T(h)$ slightly **overestimates** the integral. When a curve is **concave down** ($f''(x) < 0$, like $\sin x$ on $[0, \pi]$ or $\ln x$), the straight chord cuts *underneath* the arch, so $T(h)$ slightly **underestimates** the integral.

Most importantly, consider what the $h^2$ scaling law means: whenever you slice an interval into twice as many trapezoids—cutting the step width in half ($h \to h/2$)—the total error shrinks by a factor of $\left(\frac{1}{2}\right)^2 = \mathbf{\frac{1}{4}}$, just as Archimedes found in 240 BCE.

At first glance, that $1/4$ ratio looks like a computational bottleneck. If each doubling of your work only trims the error by a factor of $4$, then to reach twelve decimal digits of precision ($10^{-12} \approx 4^{-20}$) by brute force, you would have to evaluate $2^{20} \approx \mathbf{1,048,576\text{ trapezoids}}$—grinding away for minutes on a pocket processor. How do we leap across twenty doublings in just four or five steps?

---

## The 4/3 Minus 1/3 Miracle: Richardson Extrapolation & Romberg Integration

In 1910, the English physicist, meteorologist, and Quaker pacifist **Lewis Fry Richardson**—who famously dreamed of forecasting the weather by solving fluid-dynamics equations by hand while driving a front-line ambulance in World War I, and who later discovered the fractal scaling of the **Coastline of Britain**—looked at that $1/4$ error ratio and saw not a curse, but an **extraordinary mathematical lever**.

Suppose you measure a rugged coastline—or the area under a curve—first with a coarse step size $h$, giving the trapezoidal estimate $T_{\text{coarse}} = T(h)$, and then you cut the step size in half once to $h/2$, giving the fine trapezoidal estimate $T_{\text{fine}} = T(h/2)$.

First, that halving step is remarkably economical. When you refine $N$ panels of width $h$ into $2N$ panels of width $h/2$, every single vertical fencepost of the coarse grid is *already* an even-numbered fencepost of the fine grid:

$$T\!\left(\frac{h}{2}\right) = \frac{1}{2} T(h) + \frac{h}{2} \sum_{m=1}^{N} f\!\left(a + \left(m - \frac{1}{2}\right)h\right)$$

You never throw away a single function evaluation from your earlier work—you simply divide your previous trapezoidal sum $T(h)$ by $2$ and add the newly sampled midpoints.

Second, why does the trapezoidal error expand purely in **even** powers of $h$ ($h^2, h^4, h^6, \dots$) with no odd powers ($h^3, h^5, \dots$) anywhere in sight? In the 1730s, **Leonhard Euler** and **Colin Maclaurin** proved one of the most celebrated formulas in mathematical analysis—the **Euler-Maclaurin Summation Formula**:

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

**The entire leading $h^2$ error vanishes at a single stroke!** Even more wonderfully, see what happens if we write out $T(h) = \frac{h}{2}[f(a) + f(b)]$ and $T(h/2) = \frac{h}{4}[f(a) + 2f(m) + f(b)]$ (where $m = \frac{a+b}{2}$ is the midpoint) and substitute them into Richardson's $\frac{4}{3} - \frac{1}{3}$ formula:

$$\frac{4}{3}\left(\frac{h}{4}\big[f(a) + 2f(m) + f(b)\big]\right) - \frac{1}{3}\left(\frac{h}{2}\big[f(a) + f(b)\big]\right) = \frac{h}{6}\Big[ f(a) + 4f(m) + f(b) \Big]$$

Those $1\text{–}4\text{–}1$ weights $\frac{h}{6}[f(a) + 4f(m) + f(b)]$ show that Richardson's $\frac{4}{3} - \frac{1}{3}$ combination of two flat-topped trapezoid sums has automatically transformed them into **Thomas Simpson's 1743 Parabolic Rule ($\mathcal{O}(h^4)$)**—the exact area under a smooth parabola fitted through the left endpoint, the midpoint, and the right endpoint. And because the third derivative $f'''(x)$ of any cubic polynomial $Ax^3 + Bx^2 + Cx + D$ is a constant (so $f'''(b) - f'''(a) = 0$ in the $h^2$ term and $f^{(4)}(x) = 0$ in the $h^4$ term), Simpson's $1\text{–}4\text{–}1$ rule is **100% exact not only for parabolas, but for cubics too!**

In 1955, the German-Norwegian physicist **Werner Romberg** {{cite:romberg1955}} realized that you do not have to stop after killing the $h^2$ error. Once you have two Simpson parabolic estimates at step sizes $h$ and $h/2$, their leading $c_2 h^4$ errors stand in the ratio $\left(\frac{1}{2}\right)^4 = \frac{1}{16}$. So taking $\frac{16}{15}S_{\text{fine}} - \frac{1}{15}S_{\text{coarse}}$ annihilates the $h^4$ error and leaps to **George Boole's 5-Point Rule ($\mathcal{O}(h^6)$)** with its classic $7\text{–}32\text{–}12\text{–}32\text{–}7$ weights:

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

$$\begin{array}{c|cccc}
k \text{ (Panels } 2^k\text{)} & j=0 \text{ (Trapezoid } \mathcal{O}(h^2)\text{)} & j=1 \text{ (Simpson } \mathcal{O}(h^4)\text{)} & j=2 \text{ (Boole } \mathcal{O}(h^6)\text{)} & j=3 \text{ (}\mathcal{O}(h^8)\text{)} \\
\hline
k = 0 \text{ (1 panel)} & 8.38905610 & & & \\
k = 1 \text{ (2 panels)} & 6.91280988 & \mathbf{6.42072780} & & \\
k = 2 \text{ (4 panels)} & 6.52161011 & 6.39121019 & \mathbf{6.38924235} & \\
k = 3 \text{ (8 panels)} & 6.42229781 & 6.38919370 & 6.38905927 & \mathbf{6.38905637}
\end{array}$$

* **Row $k = 0$ ($1$ trapezoid, $h_0 = 2.0$):** $R(0,0) = \frac{2}{2}(e^0 + e^2) = \mathbf{8.38905610}$ (a $+31.3\%$ overshoot).
* **Row $k = 1$ ($2$ trapezoids, $h_1 = 1.0$):** Adding the single midpoint $e^1$ gives $R(1,0) = \mathbf{6.91280988}$. Applying $\frac{4 R(1,0) - R(0,0)}{3}$ produces $R(1,1) = \mathbf{6.42072780}$, slashing the error by tenfold.
* **Row $k = 2$ ($4$ trapezoids, $h_2 = 0.5$):** Adding the two quarter-points gives $R(2,0) = 6.52161011 \longrightarrow R(2,1) = 6.39121019 \longrightarrow R(2,2) = \frac{16(6.39121019) - 6.42072780}{15} = \mathbf{6.38924235}$ (within $0.0029\%$ of the exact answer using just $5$ function evaluations).
* **Row $k = 3$ ($8$ trapezoids, $h_3 = 0.25$):** With just $9$ function evaluations, $R(3,3) = \mathbf{6.38905637}$ is already accurate to **seven significant digits**, and by Row $k = 4$ ($17$ points), the error drops below $10^{-12}$—outperforming a million raw trapezoids!

On the SC-32, you run this entire Romberg tableau with three natural actions: enter your integrand expression into **`{{key:EQN}}`**, place the lower limit $a$ in **Register $Y$** and the upper limit $b$ in **Register $X$**, and press **`{{key:∫}}`** (`{{key:↱}}` + `{{key:8}}`) followed by the dummy variable softkey. Why does the SC-32 cap the Romberg tableau at column $j_{\max} = 5$ ($\mathcal{O}(h^{12})$) and split wide intervals ($|b - a| > 20$) across logarithmic `1-2-5` decade boundaries? Because in 1901, German mathematician **Carl David Tolmé Runge** proved that fitting a single ultra-high-degree polynomial across equally spaced points on a wide interval triggers violent boundary oscillations (**Runge's Phenomenon**). Even better, what if your integrand is a periodic wave like $\cos^2 x$ or a bell curve whose odd derivatives $f^{(2m-1)}(b) - f^{(2m-1)}(a)$ nearly vanish at the boundaries? By the Euler-Maclaurin formula above, when endpoint derivatives match, the Composite Trapezoidal Rule converges **exponentially fast** on its own. Following **William Kahan's** architecture {{cite:kahan1979}}, the SC-32 couples its Romberg stopping tolerance directly to your active **`{{key:DISP}}`** format (`{{key:FIX}}`, `{{key:SCI}}`, `{{key:ENG}}`, or `{{key:ALL}}`) and upon completion places the certified integral $I$ in **Register $X$** and the estimated truncation uncertainty $\pm\varepsilon$ in **Register $Y$**, while **preserving whatever was previously in Registers $Z$ and $T$** so chained integrals never clobber your upper stack shelves.

---

## When Textbook Antiderivatives Don't Exist: Rockets, Dams & Pendulums

### Four Physical Problems Beyond Elementary Antiderivatives

In textbook calculus, almost every integral is carefully rigged so that you can find a neat symbolic antiderivative $F(x)$ and plug in $F(b) - F(a)$. In the real physical world, even the simplest machines and natural laws routinely produce integrals that cannot be integrated in elementary closed form—or where numerical quadrature via `{{key:∫}}` is a direct, error-free audit of the physics:

1. **Christiaan Huygens's Large-Angle Grandfather Clock Pendulum (1673) & Catenary Spans:** Every introductory physics student learns Galileo's formula for the period of a pendulum of length $L$: $T_0 = 2\pi\sqrt{L/g}$. Why did **Christiaan Huygens** discover in his 1673 *Horologium Oscillatorium* that a real grandfather clock pendulum swinging through a wide arc $\theta_0$ runs noticeably **slower** than $2\pi\sqrt{L/g}$? Because Galileo's formula assumes $\sin\theta \approx \theta$, which is only true for tiny angles. When a pendulum releases from a large angle $\theta_0$ (say $60^\circ$), conservation of energy leads to the **Complete Elliptic Integral of the First Kind** (with modulus $k = \sin(\theta_0/2)$):
   $$\frac{T(\theta_0)}{T_0} = \frac{2}{\pi} \int_0^{\pi/2} \frac{d\varphi}{\sqrt{1 - k^2 \sin^2\varphi}}$$
   Like the ellipse perimeter in Chapter 6, this integral has **no closed-form elementary antiderivative**—yet `{{key:∫}}` integrates it to 12 digits in a blink. Meanwhile, returning to the hanging **catenary** chain $y(x) = a\cosh(x/a)$ from Chapter 4 (`{{key:HYP}} {{key:COS}}`), when power-grid engineers string a high-voltage transmission cable across a wide river span $[-x_0, +x_0]$, integrating the arc-length integrand $L = \int_{-x_0}^{x_0}\sqrt{1 + [y'(x)]^2}\,dx = \int_{-x_0}^{x_0}\cosh(x/a)\,dx$ determines the exact conductor length required above the straight-line tower span.
2. **Rocket Burnout Velocity, Progressive Rally-Car Springs & Ferroelectric Capacitors:** During the boost phase of a solid-propellant rocket motor with non-linear cubic acceleration $a(t) = c_2 t^2 - c_3 t^3$ (or an upper-stage liquid rocket whose acceleration grows exponentially as propellant mass is expelled), integrating $\int_0^T a(t)\,dt$ gives the exact burnout velocity $\Delta v$. Likewise, integrating the cubic stiffening curve $F(x) = k_1 x + k_3 x^3$ of a desert rally-car **progressive suspension spring** across a compression stroke gives the stored elastic work $W = \int_0^{x_{\max}} F(x)\,dx$—which Romberg hits to full machine precision on its very first Simpson step $R(1,1)$, because Simpson's rule is exact for cubics! And in high-voltage electronics, when a barium titanate ($\text{BaTiO}_3$) ceramic capacitor's capacitance droops under high DC bias as $C(V) = C_0(1 - \alpha V^2)$ {{cite:horowitz2015}}, integrating $W = \int_0^V C(V)V\,dV$ exposes the true stored energy shortfall missed by the naive textbook formula $\frac{1}{2}C_0 V^2$.
3. **Hydrostatic Parabolic Dam Thrust & Hagen-Poiseuille $R^4$ Blood-Vessel Flow:** Picture a vertical steel floodgate set into a parabolic canyon spillway ($y = k x^2$) holding back reservoir water of depth $H$. Near the surface ($y = H$), the gate is wide but water pressure $\rho g(H - y)$ is zero; at the canyon floor ($y = 0$), pressure is maximum but the parabolic arch narrows to a point, so integrating horizontal ribbons $\rho g \int_0^H (H - y)w(y)\,dy$ reveals the total hydrostatic thrust against the gate.
   Similarly, when blood or oil flows smoothly through a circular pipe or artery of radius $R$, fluid at the wall is stationary ($v(R) = 0$) while the center glides at $v_{\max}$ in a parabolic profile $v(r) = v_{\max}(1 - r^2/R^2)$, whose cylindrical-shell integral $\int_0^R 2\pi r\,v(r)\,dr = \frac{1}{2}\pi R^2 v_{\max}$ proves that average laminar speed is half the centerline speed. Because $v_{\max} = \frac{\Delta P}{4\mu L}R^2$ is *also* proportional to $R^2$, **Jean Léonard Marie Poiseuille** and **Gotthilf Hagen** discovered that laminar flow scales with the **fourth power of vessel radius ($Q \propto R^4$)**—meaning a mere $16\%$ plaque constriction ($0.84\,R$) in a human coronary artery cuts blood flow in half ($0.84^4 = \mathbf{0.4979}$), whereas a $19\%$ smooth-muscle dilation ($1.19\,R$) during exercise **doubles** blood supply ($1.19^4 = \mathbf{2.0053}$)!
4. **Bell Curves, Lightning Surges, Clipped AC Waveforms & Chained Integral Ratios:** In the second half of our workbench, we will see how `{{key:∫}}` handles four classic functional patterns across electrical and optical physics:
   * **Rapidly Decaying Tails:** Integrating the non-elementary **Gaussian bell curve** $\frac{1}{\sqrt{2\pi}}\int_{-\infty}^0 e^{-x^2/2}\,dx$ (whose full statistical story unfolds in Chapter 9) and the exponential tail current $i(t) = I_0 e^{-t/\tau}$ conducted by a substation lightning surge arrester.
   * **Piecewise Waveforms with Sharp Corners:** Computing the **True-RMS heating voltage** of an AC line waveform clipped flat by a protection varistor by splitting the integral cleanly at the clipping knee $\theta_c$.
   * **Chained Integral Ratios:** Storing a denominator integral in Variable `A` to evaluate the center of mass $\bar{x} = \frac{\int x\lambda(x)\,dx}{\int \lambda(x)\,dx}$ of a tapered turbine spar and the **optical mode confinement factor** $\Gamma = \frac{\int_{-d}^d |E(x)|^2\,dx}{\int_{-\infty}^\infty |E(x)|^2\,dx}$ of a semiconductor quantum-well laser.

### A Field Guide to Non-Elementary Integrals Across Physics & Engineering

Beyond the twelve workbench benchmarks below, numerical quadrature is the primary analytical engine for four entire branches of physical science where closed-form antiderivatives simply do not exist. In solid-state physics and cryogenics, why does the heat capacity of a diamond or a copper block drop toward zero as $T^3$ near absolute zero, violating the classical Dulong-Petit law? In 1912, **Peter Debye** quantized the acoustic phonon vibrations of a crystal lattice and showed that the internal thermal energy and specific heat $C_V(T)$ of any solid are governed by the non-elementary **Debye Integral**:

$$C_V(T) = 9 N k_B \left(\frac{T}{\Theta_D}\right)^3 \int_0^{\Theta_D / T} \frac{x^4 e^x}{\left(e^x - 1\right)^2}\,dx$$

where $\Theta_D$ is the crystal's Debye temperature ($2,230\text{ K}$ for diamond, $343\text{ K}$ for copper). In the same spirit, integrating **Max Planck's spectral radiance** $\int_{\lambda_1}^{\lambda_2} \frac{c_1 \lambda^{-5}}{e^{c_2/(\lambda T)} - 1}\,d\lambda$ across a finite infrared camera passband $[\lambda_1, \lambda_2]$ measures the exact fraction of thermal radiation captured by a night-vision sensor.

In wave optics and civil highway design, when coherent laser light or a radio wave grazes the sharp edge of a knife blade or mountain ridge, the shadow edge ripples with interference fringes governed by **Augustin-Jean Fresnel's 1818 Diffraction Integrals**:

$$C(u) = \int_0^u \cos\!\left(\frac{\pi t^2}{2}\right) dt, \qquad S(u) = \int_0^u \sin\!\left(\frac{\pi t^2}{2}\right) dt$$

Plotting $(C(u), S(u))$ traces the double-coiled **Euler-Cornu Spiral**, which also serves in highway and roller-coaster engineering as the **clothoid transition curve** whose curvature $\kappa(s) \propto s$ ramps up linearly with arc length $s$ so passengers never feel a sudden lateral jerk when entering a turn.

In electromagnetism and structural mechanics, off-axis magnetic fields around MRI solenoid coils require integrating **Biot and Savart's** elliptic vector law $\mathbf{B} = \frac{\mu_0 I}{4\pi}\oint \frac{d\mathbf{l} \times \mathbf{r}}{r^3}$, while **Alberto Castigliano's 1873 Strain-Energy Theorem** determines the tip deflection $\delta = \int_0^L \frac{M(x)}{EI(x)} \frac{\partial M}{\partial P}\,dx$ of a tapered aircraft wing spar by integrating internal bending energy. And in atmospheric entry and chemical reaction engineering, spacecraft deceleration through an exponential atmosphere depends on the **Exponential Integral** $\operatorname{Ei}(x) = \int_{-\infty}^x \frac{e^t}{t}\,dt$, just as sizing a continuous tubular reactor requires integrating the reciprocal reaction rate $V = F_{A0}\int_0^X \frac{dX}{-r_A(X)}$.

---

## On the Stack: Numerical Derivatives & Romberg Integration Workbench

Both central-difference derivatives and Romberg integration fit the Four-Register Stack (`X, Y, Z, T`) like a glove: when evaluating a derivative, Register $Y$ holds the forward sample $f(x+h)$ while Register $X$ evaluates $f(x-h)$; when evaluating a definite integral $\int_a^b f(x)\,dx$, you place the lower limit $a$ in Register $Y$ and the upper limit $b$ in Register $X$ before pressing `{{key:∫}}`, replacing $(Y, X)$ with the post-integration audit pair ($X = I,\; Y = \pm\varepsilon$) while keeping Registers $Z$ and $T$ intact. Let us step onto the SC-32 calculus workbench and put Romberg's $\frac{4}{3} - \frac{1}{3}$ extrapolation tableau and central-difference derivatives to work on real physical systems.

{{res:sc32_plot_romberg_shaded:screenshot|The SC-32 transflective display executing active numerical integration of 3x^2 from 0 to 4 (Area = 64.0), demonstrating real-time stack updates and error bound estimation.}}

### Rocket Burnout, Progressive Springs, Hydrostatic Dams & Poiseuille Flow

Unless degrees (`{{key:DEG}}`) are explicitly noted, trigonometric and calculus sequences in this workbench use radian mode (`{{key:RAD}}`). When `{{key:∫}}` completes, the stack holds the **Post-Integration Audit Frame**:

| Stack Register | Post-`{{key:∫}}` Contents | Engineering Purpose & Chaining Workflow |
| :---: | :--- | :--- |
| **Register $X$** | **Certified Definite Integral ($I = \int_a^b f(x)\,dx$)** | The final Richardson-extrapolated quadrature result. |
| **Register $Y$** | **Estimated Quadrature Uncertainty ($\pm\varepsilon$)** | Upper bound on absolute truncation error. Swap via `{{key:x⇄y}}` to audit convergence. |
| **Register $Z$** | **Prior Register $Z$ (Preserved)** | Holds whatever was in $Z$ when `{{key:∫}}` was pressed (for example, a first integral $I_1$ lifted into $Z$ by typing `c {{key:ENTER}} d` for a second integral). |
| **Register $T$** | **Prior Register $T$ (Preserved)** | Preserves the top of the stack undisturbed across quadrature passes. |

Let us run our mechanical and fluid quadrature benchmarks on the stack:

1. **Solid Rocket Motor Burnout Velocity ($\int_0^6 (4t^2 - 0.5t^3)\,dt = 126.0\text{ m/s}$):**
   Because the solid propellant grain burns outward along a star-shaped internal perforation before tapering against the insulated steel motor casing, its acceleration profile $a(t) = 4t^2 - 0.5t^3$ is a third-degree cubic polynomial. When you enter the equation in `{{key:EQN}}` as `T {{key:x²}} 4 {{key:×}} T 3 {{key:yˣ}} 0.5 {{key:×}} {{key:-}}`, Romberg's very first Richardson extrapolation column $R(1,1)$ (Simpson's $1/3$ parabolic rule) is already $100\%$ exact on any cubic polynomial:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0 {{key:ENTER}} 6` | $0.0000$ | $0.0000$ | $0.0000$ | $6.0000$ | Limits: $a=0$ in $Y$, $b=6$ in $X$ |
| `{{key:∫}} T` | $0.0000$ | $0.0000$ | **$1.2435 \times 10^{-11}$** | **$126.000000000$** | Burnout velocity $v_{\text{burn}}$ in $X$; error bound $\pm\varepsilon$ in $Y$ |

   For a liquid-bipropellant upper stage whose mass diminishes exponentially as propellant is expelled ($a(t) = 12.0e^{0.04t} - 9.80665\text{ m/s}^2$ over a $25\text{-second}$ burn), you can either integrate the equation directly via `0 {{key:ENTER}} 25 {{key:∫}} T` or cross-check its closed-form antiderivative $\Delta v = \frac{12.0}{0.04}(e^{0.04(25)} - 1) - 9.80665(25)$ on the stack. By keying `0.04 {{key:ENTER}} 25 {{key:×}} {{key:LASTX}} {{key:x⇄y}} {{key:eˣ}} 1 {{key:-}} 300 {{key:×}} {{key:x⇄y}} 9.80665 {{key:×}} {{key:-}}`, `{{key:LASTX}}` recovers the burn duration `25` automatically for the gravity-loss subtraction, confirming the exact burnout velocity **$270.3183\text{ m/s}$** while typing `25` only once.

2. **Progressive Rally-Car Suspension Spring ($W = \int_0^{0.15}(2500x + 40000x^3)\,dx = 33.1875\text{ J}$):**
   Why do off-road desert rally cars use variable-pitch **progressive coil springs** ($F(x) = k_1 x + k_3 x^3$) instead of ordinary linear Hookean springs ($F(x) = k_1 x$)? Over small highway ripples ($x \ll 0.05\text{ m}$), the cubic term $40000x^3$ is negligible and the soft $2500\text{ N/m}$ linear rate gives a supple ride; when the car lands hard off a jump ($x = 0.15\text{ m}$), the closely wound coils bind progressively and the $40000x^3$ cubic stiffening prevents the chassis from bottoming out. With `X 2500 {{key:×}} X 3 {{key:yˣ}} 40000 {{key:×}} {{key:+}}` in `{{key:EQN}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0 {{key:ENTER}} 0.15` | $0.0000$ | $0.0000$ | $0.0000$ | $0.1500$ | Limits $a=0, b=0.15$ |
| `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$3.55 \times 10^{-12}$** | **$33.187500000$** | Work $W$ in Joules |

   Cross-checking the closed-form antiderivative $\frac{1}{2}k_1 x^2 + \frac{1}{4}k_3 x^4 = 1250x^2 + 10000x^4$ at $x = 0.15\text{ m}$ via {{res:sc32_08_calc_01:keys}} confirms $\mathbf{{{res:sc32_08_calc_01:value}}\text{ Joules}}$ (showing that progressive cubic stiffening stores $+18\%$ more impact energy than a linear spring's $28.125\text{ J}$).
   Similarly, in high-voltage pulsed-power electronics, a Class-II ferroelectric barium titanate ($\text{BaTiO}_3$) ceramic capacitor exhibits voltage-dependent dielectric saturation $C(V) = C_0(1 - \alpha V^2)$ with $C_0 = 10\,\mu\text{F}$ and $\alpha = 10^{-6}\text{ V}^{-2}$ {{cite:horowitz2015}}. Integrating the differential energy $dW = C(V)V\,dV = 10^{-5}(V - 10^{-6}V^3)\,dV$ via `V 3 {{key:yˣ}} 1 {{key:E}} 6 {{key:+/-}} {{key:×}} V {{key:x⇄y}} {{key:-}} 10 {{key:E}} 6 {{key:+/-}} {{key:×}}` over `0 {{key:ENTER}} 500 {{key:∫}} V` confirms **$1.09375\text{ Joules}$**—revealing the $12.5\%$ energy deficit relative to the textbook linear formula $\frac{1}{2}C_0 V^2 = 1.2500\text{ J}$.

3. **Hydrostatic Parabolic Spillway Gate ($F = 9810\int_0^4 (4-y)\sqrt{8y}\,dy = 236,778.5\text{ N}$):**
   The integrand $(4 - y)\sqrt{8y}$ requires adaptive higher-order Romberg columns because its derivative with respect to $y$ has a vertical square-root slope $\propto 1/\sqrt{y}$ right at the canyon floor $y = 0$. With `Y 8 {{key:×}} {{key:√x}} 4 Y {{key:-}} {{key:×}} 9810 {{key:×}}` in `{{key:EQN}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0 {{key:ENTER}} 4` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | Gate depth interval $[0, 4]$ |
| `{{key:∫}} Y` | $0.0000$ | $0.0000$ | **$4.18 \times 10^{-10}$** | **$236778.4720$** | Hydrostatic Force in Newtons ($236.78\text{ kN}$) |

4. **Hagen-Poiseuille Laminar Pipe Discharge ($Q = \int_0^{0.05} 2\pi r\cdot 1.2(1 - r^2/0.0025)\,dr = 4.712389\text{ L/s}$):**
   In cylindrical pipe flow, velocity peaks at the centerline ($r = 0$), where the ring circumference $2\pi r$ is zero, and drops to zero at the pipe wall ($r = 0.05\text{ m}$), where the ring circumference is largest—meaning the maximum volumetric contribution $2\pi r\,v(r)$ actually comes from the intermediate radial zone $r = R/\sqrt{3} \approx 0.0289\text{ m}$. With `R {{key:x²}} 0.0025 {{key:÷}} 1 {{key:x⇄y}} {{key:-}} 1.2 {{key:×}} R {{key:×}} 2 {{key:×}} {{key:π}} {{key:×}}` in `{{key:EQN}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0 {{key:ENTER}} 0.05` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0500$ | Pipe radial integration limits $[0, R]$ |
| `{{key:∫}} R` | $0.0000$ | $0.0000$ | **$1.45 \times 10^{-12}$** | **$0.004712$** | Discharge $Q$ in $\text{m}^3/\text{s}$ |
| `1000 {{key:×}}` | $0.0000$ | $0.0000$ | $1.45 \times 10^{-12}$ | **$4.712389$** | Convert volumetric flow to Liters/second |

---

### Transcendental Integrals, Piecewise RMS Waveforms & Chained Centroids

Now let us trace our six transcendental and multi-segment engineering integrals on the stack:

1. **Gaussian Bell Curve Left-Half Symmetry ($\Phi(0) \approx \frac{1}{\sqrt{2\pi}}\int_{-5}^0 e^{-x^2/2}\,dx = 0.500000$):**
   Because the Gaussian density $\phi(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ decays so rapidly that at $x = -5$ its height is already $\phi(-5) \approx 1.487 \times 10^{-6}$ and all its odd derivatives nearly vanish at both $x = -5$ and $x = 0$, the Euler-Maclaurin endpoint correction terms are tiny and Romberg's tableau locks onto the exact left-tail probability $0.500000$. With `X {{key:x²}} 2 {{key:÷}} {{key:+/-}} {{key:eˣ}} 2 {{key:π}} {{key:×}} {{key:√x}} {{key:÷}}` in `{{key:EQN}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `5 {{key:+/-}} {{key:ENTER}} 0` | $0.0000$ | $0.0000$ | $-5.0000$ | $0.0000$ | Integration interval $[-5, 0]$ |
| `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$2.15 \times 10^{-10}$** | **$0.5000000000$** | Cumulative probability $\Phi(0) = 0.500000$ |

2. **Lightning Surge Arrester Charge ($Q = \int_0^{2.5\times 10^{-4}} 10000e^{-t/5\times 10^{-5}}\,dt = 0.496631\text{ C}$):**
   When an atmospheric lightning stroke hits an overhead substation bus, a zinc-oxide Metal-Oxide Varistor (MOV) arrester conducts an exponential tail current $i(t) = I_0 e^{-t/\tau}$ ($I_0 = 10\text{ kA},\; \tau = 50\,\mu\text{s}$) across five time constants ($5\tau = 250\,\mu\text{s}$). With `T 5 {{key:E}} 5 {{key:+/-}} {{key:÷}} {{key:+/-}} {{key:eˣ}} 10000 {{key:×}}` in `{{key:EQN}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0 {{key:ENTER}} 2.5 {{key:E}} 4 {{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.000250$ | Limits $a=0, b=250\,\mu\text{s}$ |
| `{{key:∫}} T` | $0.0000$ | $0.0000$ | **$1.12 \times 10^{-11}$** | **$0.496631098$** | Charge $Q$ in Coulombs |

   Evaluating the closed-form integral $I_0\tau(1 - e^{-5})$ via {{res:sc32_08_calc_02:keys}} confirms $\mathbf{{{res:sc32_08_calc_02:value}}\text{ C}}$ ($99.33\%$ of the infinite-time charge $I_0\tau = 0.5000\text{ C}$).

3. **Catenary Transmission Line Arc Length & Sag ($L = \int_{-100}^{100}\cosh(x/800)\,dx = 200.5210\text{ m}$):**
   The stack lets us compute the exact conductor arc length $L = 200.5210\text{ m}$ via Romberg quadrature (`{{key:∫}} X`) and then immediately compute the mid-span sag $\Delta y = 800[\cosh(100/800) - 1] = 6.2583\text{ m}$ while keeping the arc length visible in Register $Y$. With `X 800 {{key:÷}} {{key:HYP}} {{key:COS}}` in `{{key:EQN}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `100 {{key:+/-}} {{key:ENTER}} 100` | $0.0000$ | $0.0000$ | $-100.0000$ | $100.0000$ | Tower span interval $[-100, +100]$ |
| `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$8.55 \times 10^{-11}$** | **$200.5210$** | Conductor total arc length (meters) |
| `100 {{key:ENTER}} 800 {{key:÷}} {{key:HYP}} {{key:COS}}` | $8.55 \times 10^{-11}$ | $8.55 \times 10^{-11}$ | $200.5210$ | $1.007823$ | Dimensionless catenary height ratio |
| `1 {{key:-}} 800 {{key:×}}` | $8.55 \times 10^{-11}$ | $8.55 \times 10^{-11}$ | $200.5210$ | **$6.2583$** | Conductor mid-span sag $\Delta y$ (meters) |

   For a cylindrical heavy-water nuclear reactor core of radius $R = 1.80\text{ m}$, height $H = 3.60\text{ m}$, and peak volumetric power density $q_0''' = 120\text{ MW/m}^3$, the radial neutron flux follows Friedrich Wilhelm Bessel's fundamental drumhead mode $J_0(2.40483\,r/R) \approx 1 - \frac{1}{4}u^2 + \frac{1}{64}u^4$ (with $j_{0,1}/R = 2.40483/1.80 \approx 1.33601\text{ m}^{-1}$, entered as `1.3361` in the keystroke sequence below). Integrating the Horner-nested radial ring integrand `R 1.3361 {{key:×}} {{key:x²}} {{key:ENTER}} {{key:ENTER}} 0.015625 {{key:×}} 0.25 {{key:-}} {{key:×}} 1 {{key:+}} R {{key:×}} 2 {{key:×}} {{key:π}} {{key:×}}` over `0 {{key:ENTER}} 1.8 {{key:∫}} R` and scaling by the axial cosine factor `120 {{key:×}} 3.6 {{key:×}} 2 {{key:×}} {{key:π}} {{key:÷}}` yields the total reactor thermal output **$1,208.5866\text{ MW}_{\text{th}}$**.

4. **Piecewise MOV-Clipped AC True-RMS Voltage ($V_p = 170\text{ V}$ clipped at $V_c = 136\text{ V}, \theta_c = \arcsin(0.80)$):**
   Why should you never integrate across a sharp corner (where the derivative $f'(x)$ jumps discontinuously) in a single Romberg pass? Because a slope corner violates the smooth Euler-Maclaurin derivative assumptions and forces the Romberg tableau to grind through dozens of sub-panels. Instead, split the quarter-cycle $[0, \pi/2]$ right at the clipping knee $\theta_c = \arcsin(136/170) = \arcsin(0.80) = 0.927295\text{ rad}$: integrate the smooth rising sine squared $(170\sin\theta)^2$ over $[0, \theta_c]$, and add the flat clamped plateau $136^2(\pi/2 - \theta_c)$ directly on the stack. With `X {{key:SIN}} 170 {{key:×}} {{key:x²}}` in `{{key:EQN}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:RAD}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Radian mode engaged for trig calculus |
| `0 {{key:ENTER}} 0.8 {{key:ASIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.927295$ | Integration bounds $[0, \theta_c]$ via $\theta_c = \arcsin(0.8)$ |
| `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$3.12 \times 10^{-10}$** | **$6463.4190$** | Integral of $(170\sin\theta)^2$ over rising edge |
| `0.8 {{key:ASIN}} {{key:π}} 2 {{key:÷}} {{key:x⇄y}} {{key:-}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | $0.643501$ | Clipped interval $(\pi/2 - \theta_c)$; rising integral stays in $Y$ |
| `136 {{key:x²}} {{key:×}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | **$11902.1965$** | Flat clamped plateau contribution |
| `{{key:+}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | **$18365.6155$** | Total quarter-cycle energy sum |
| `2 {{key:×}} {{key:π}} {{key:÷}} {{key:√x}}` | $6463.4190$ | $6463.4190$ | $6463.4190$ | **$108.1292$** | Mean square normalized and root taken ($V_{\text{rms}}$) |

5. **Chained Integrals for Tapered Turbine Spar Centroid ($\lambda(x) = 1.5 + 0.8x^2\text{ kg/m}$ over $[0, 2]\text{ m}$):**
   Whenever a physical property is defined as the **ratio of two definite integrals**—such as a center of mass $\bar{x} = \frac{\int x\lambda(x)\,dx}{\int \lambda(x)\,dx}$, a radius of gyration, or a quantum-mechanical expectation value—store the denominator integral in Variable `A`, evaluate the numerator integral, and divide via `{{key:RCL}} A {{key:÷}}`. Evaluating $M = \int_0^2 \lambda(x)\,dx = 5.133333\text{ kg}$ and $M_x = \int_0^2 x\lambda(x)\,dx = 6.200000\text{ kg}\cdot\text{m}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0 {{key:ENTER}} 2` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Integration limits $[0, 2]$ |
| `{{key:∫}} X` | $0.0000$ | $0.0000$ | **$3.24 \times 10^{-11}$** | **$5.133333$** | Romberg evaluates rod mass $M$ (kg) |
| `{{key:STO}} A` | $0.0000$ | $0.0000$ | $3.24 \times 10^{-11}$ | $5.133333$ | Store total mass $M$ in Variable A |
| `0 {{key:ENTER}} 2` | $3.24 \times 10^{-11}$ | $5.133333$ | $0.0000$ | $2.0000$ | Reload integration limits $[0, 2]$ |
| `{{key:∫}} X` | $3.24 \times 10^{-11}$ | $5.133333$ | **$1.87 \times 10^{-11}$** | **$6.200000$** | Romberg evaluates first moment $M_x$ |
| `{{key:RCL}} A {{key:÷}}` | $5.133333$ | $5.133333$ | $1.87 \times 10^{-11}$ | **$1.207792$** | Centroid position $\bar{x} = M_x / M$ (meters) |

6. **Semiconductor Laser Optical Confinement Factor ($\Gamma = \int_{-d}^d |E(x)|^2\,dx / \int_{-5d}^{5d} |E(x)|^2\,dx$):**
   In a double-heterostructure gallium arsenide ($\text{GaAs}/\text{AlGaAs}$) laser diode, only the fraction $\Gamma$ of the transverse optical wave intensity $|E(x)|^2$ that overlaps the central active quantum-well layer $[-d, +d]$ stimulates laser emission, while the evanescent wings leaking into $[-5d, +5d]$ are passive. Modeling the normalized transverse waveguide mode profile across the spatial coordinate $x$ as $|E(x)|^2 = 1.23\,\operatorname{sech}^2(1.23\,x)$ in normalized half-width units $d = 1$ (entered into `{{key:EQN}}` as `1.23  X 1.23 {{key:×}} {{key:HYP}} {{key:COS}} {{key:x²}} {{key:÷}}`):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:+/-}} {{key:ENTER}} 1 {{key:∫}} X` | $0.0000$ | $0.0000$ | $1.25 \times 10^{-11}$ | $1.6850$ | Core field energy over $[-d, d]$ |
| `{{key:STO}} A` | $0.0000$ | $0.0000$ | $1.25 \times 10^{-11}$ | $1.6850$ | Core energy stored in register A |
| `5 {{key:+/-}} {{key:ENTER}} 5 {{key:∫}} X` | $1.25 \times 10^{-11}$ | $1.6850$ | $2.40 \times 10^{-11}$ | $2.0000$ | Total field energy over $[-5d, 5d]$ |
| `{{key:RCL}} A {{key:x⇄y}} {{key:÷}}` | $1.6850$ | $1.6850$ | $2.40 \times 10^{-11}$ | **$0.8425$** | Optical confinement factor $\Gamma = 84.25\%$ |

---

### Central-Difference Derivatives & James Watt's Flyweight Governor

Now let us turn to numerical differentiation on the stack:

#### Central-Difference Derivative of a Quadratic ($f(x) = x^2$ at $x_0 = 3.0$)

To evaluate the central-difference derivative $f'(3.0) \approx \frac{f(3 + h) - f(3 - h)}{2h}$ on $f(x) = x^2$ with step size $h = 10^{-5}$ (so the total span is $2h = 0.00002$), remember that because the third derivative $f'''(x)$ of a parabola is identically zero, the $\mathcal{O}(h^2)$ central-difference formula has **zero truncation error**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3.00001 {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $9.000060$ | Forward point $f(x_0 + h) = 3.00001^2$ |
| `2.99999 {{key:x²}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.000120$ | Central difference $f(x_0 + h) - f(x_0 - h)$ |
| `0.00002 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$6.0000000000$** | Central-difference derivative $f'(3) = 6.0$ |

#### Exponential Derivative at the Origin ($f(x) = e^{2x}$ at $x_0 = 0$) via `LASTX` & Hyperbolic Sine

Suppose we want the derivative of $f(x) = e^{2x}$ at $x_0 = 0$ using $h = 10^{-5}$ (so $2x_{\pm} = \pm 2h = \pm 0.00002$ and the denominator is $2h = 0.00002$):
* **Method A (`{{key:LASTX}}` Exponent Reuse):** Key `0.00002 {{key:ENTER}} {{key:eˣ}}` (putting $0.00002$ in Register $Y$ and $e^{0.00002} = 1.0000200002$ in Register $X$, while saving $0.00002$ in `LASTX`), then key `{{key:LASTX}} {{key:+/-}} {{key:eˣ}} {{key:-}}` to form $e^{2h} - e^{-2h} = 0.0000400000$, and finish with `{{key:x⇄y}} {{key:÷}}` to obtain **$f'(0) = 2.0000000003$** while typing `0.00002` only once.
* **Method B (Hyperbolic Sine Identity):** Because $\frac{e^{2h} - e^{-2h}}{2h} = 2\frac{\sinh(2h)}{2h}$, keying `0.00002 {{key:HYP}} {{key:SIN}} {{key:LASTX}} {{key:÷}} 2 {{key:×}}` evaluates $f'(0) = \mathbf{2.0000000003}$ in just seven keystrokes.
* **Method C (Second Derivative $f''(x_0) \approx \frac{f(x_0+h) - 2f(x_0) + f(x_0-h)}{h^2}$):** Adding $e^{2h} + e^{-2h} = 2\cosh(2h)$ instead of subtracting them and dividing by $h^2 = 10^{-10}$ via `0.00002 {{key:HYP}} {{key:COS}} 1 {{key:-}} 2 {{key:×}} 1 {{key:E}} 10 {{key:+/-}} {{key:÷}}` recovers the second derivative **$f''(0) = 4.000000$**.

#### James Watt's Centrifugal Flyball Governor ($m = 4.0\text{ kg}, \omega = 40.0\text{ rad/s}$)

Finally, for **James Watt's centrifugal flyball governor** ($m = 4.0\text{ kg}, \omega = 40.0\text{ rad/s}, r(\theta) = 0.15 + 0.05\sin(2\theta)\text{ m}$ at $\theta = \pi/6\text{ rad}$), we combine the radial derivative velocity $\dot{r} = \omega\frac{dr}{d\theta}$ and the tangential velocity $v_\theta = r\omega$ in `{{key:RAD}}` mode:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:RAD}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Verify radian mode |
| `{{key:π}} 6 {{key:÷}} {{key:STO}} A` | $0.0000$ | $0.0000$ | $0.0000$ | $0.523599$ | Angle $\theta = \pi/6$ stored in Var A |
| `2 {{key:×}} {{key:COS}} 0.1 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.050000$** | Radial derivative $dr/d\theta = 0.10\cos(2\theta)$ |
| `40 {{key:×}} {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$4.000000$** | Radial velocity squared $\dot{r}^2 = (2.0)^2$ |
| `{{key:RCL}} A 2 {{key:×}} {{key:SIN}} 0.05 {{key:×}} 0.15 {{key:+}} 40 {{key:×}}` | $0.0000$ | $0.0000$ | $4.000000$ | **$7.732051$** | Tangential speed $v_\theta = r \omega$; $\dot{r}^2$ stays in $Y$ |
| `{{key:x²}} {{key:+}} 2 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$127.569226$** | Kinetic energy $0.5 \times 4 \times (\dot{r}^2 + v_\theta^2)$ (J) |

What if we didn't want to differentiate $r(\theta) = 0.15 + 0.05\sin(2\theta)$ analytically at all? We can evaluate $\frac{dr}{d\theta}$ at $\theta = \pi/6 \approx 0.52359878\text{ rad}$ directly on the stack using the central-difference formula $\frac{r(\theta + 10^{-5}) - r(\theta - 10^{-5})}{2\times 10^{-5}}$, obtaining $\frac{dr}{d\theta} = \mathbf{0.0500000000\text{ m/rad}}$ to ten decimal places.

### Practical Quadrature Hygiene: Display-Coupled Stopping, Chaining & Singularity Traps

When integrating complex physical waveforms on the SC-32, four practical stack techniques let you control speed, accuracy, and boundary behavior:

1. **Controlling Quadrature Speed via Display Precision (`{{key:FIX}}`, `{{key:SCI}}`, `{{key:ENG}}`):**
   Following William Kahan's display-coupled stopping rule {{cite:kahan1979}}, the SC-32 Romberg engine terminates as soon as two successive diagonal extrapolations $|R(k, j) - R(k, j-1)|$ agree to within half an ulp of the currently displayed decimal format:
   * If you need a fast 3-digit field check of a slow transcendental integrand, set `{{key:FIX}} 3` before pressing `{{key:∫}}`.
   * When you want full 11-to-12-digit certification, set `{{key:SCI}} 9` or `{{key:ALL}}`.
2. **Seamless Chaining of Integrals via Register $Z$:**
   Because the post-integration stack frame replaces $(Y, X)$ with $(\pm\varepsilon, I)$ while preserving whatever was previously in Registers $Z$ and $T$, typing two new integration limits `c {{key:ENTER}} d` automatically lifts your first integral $I_1$ into **Register $Z$** (and its uncertainty $\pm\varepsilon_1$ into **Register $T$**). When the second `{{key:∫}}` finishes, $I_1$ is still sitting untouched in Register $Z$ (`1.6850` in our laser confinement example above) while $I_2$ sits in Register $X$, ready for immediate chaining!
3. **Splitting Oscillatory or Sharp-Peak Integrands:**
   If an integrand contains a very narrow spike inside a wide interval (such as a high-$Q$ resonance peak sitting at $x = 10$ inside $[0, 100]$), a coarse initial grid on $[0, 100]$ might step right over the narrow spike. Splitting the interval at the known peak location ($[0, 10]$ and $[10, 100]$) guarantees that the very first Romberg panel samples the peak directly.
4. **Handling Integrand Poles & Endpoint Singularities:**
   Remember that if an integration interval $[a, b]$ passes directly through or touches a division-by-zero pole such as $\int_0^1 \frac{1}{x}\,dx$, the SC-32 halts immediately when sampling the endpoint or midpoint with **`DIVIDE BY 0`** (Code 01, cleared non-destructively via `{{key:C}}` while preserving your limits on the stack). When an integrable improper integral has a removable $0/0$ singularity at an endpoint (such as $\int_0^\pi \frac{\sin x}{x}\,dx$, the **Sine Integral $\operatorname{Si}(\pi) \approx 1.8519370520$**), displacing the lower limit by a tiny positive offset $a = 10^{-12}$ lets Romberg's tableau converge cleanly without triggering a zero-divide trap.

---

### From Smooth Curves to Noisy Human Measurements

Reflect on Chapters 7 and 8: whether we were hunting down the root of Kepler's orbital equation with Richard Brent's hybrid solver or slicing the area under a rocket acceleration curve with Werner Romberg's $\frac{4}{3} - \frac{1}{3}$ Richardson extrapolation, we enjoyed one huge luxury. In every problem so far, **we already knew the exact, smooth mathematical formula $f(x)$ governing the curve**. Because the function $f(x)$ was deterministic and noise-free, evaluating $f(x + h)$ and $f(x - h)$ at closely spaced points allowed Taylor series errors to cancel cleanly to twelve decimal places.

What happens when you step out of the mathematical theorist's study and into an astronomical observatory, a wind tunnel, a metallurgy lab, or a quality-control testing room? In the experimental world, nature never hands you a noiseless formula $y = f(x)$ printed on a silver platter. Instead, she hands you a cloud of **imperfect human measurements**—telescope right-ascension sightings jittering in atmospheric turbulence, strain-gauge voltages quivering with thermal Johnson-Nyquist noise, or steel fatigue coupons that scatter across the graph paper because no two batches of crystalline metal are ever microscopically identical.

When your data points contain random scatter, you cannot simply take $\frac{y_{i+1} - y_{i-1}}{2\Delta x}$ between two neighboring points, because dividing tiny random measurement jitter by a small step $\Delta x$ amplifies the noise into wild, meaningless spikes. Instead of passing a jagged curve through every noisy dot, you need a mathematical way to let the random upward errors and downward errors cancel each other out across the entire dataset—extracting the calm, underlying signal from the storm of measurement uncertainty.

If every single observation contains random error, how can you possibly discover the true physical law hiding underneath the noise? Why does sample standard deviation divide by $n - 1$ instead of $n$? And how can six simple running totals in calculator memory remember the exact best-fit line through a hundred data points without storing the hundred points themselves? In **[Chapter 9: Taming Uncertainty: How Gauss Found a Lost Planet and a Brewery Invented Modern Statistics](09-statistics-curve-fitting.md)**, we travel to Palermo and Göttingen on New Year's Night 1801 to witness the birth of Least Squares, watch lead shot cascade through Sir Francis Galton's Quincunx into the Normal Bell Curve, and meet the Guinness brewery chemist who invented small-sample science.
