---
title: "Chapter 7: Polynomials, Brent-Dekker Solver & Root Finding | SC-32 Manual"
description: "Master Cardano's analytic cubic solver [POLY], Richard Brent's hybrid numerical root solver [SOLVE] with 10^-12 precision, Horner's method, and engineering equation solving on the StackCalc SC-32."
---

# Chapter 7: Polynomials, Brent-Dekker Solver & Root Finding

## Transcendental Root-Finding & Richard Brent's Hybrid Method

Across an eleven-hundred-year mathematical arc—from **Muhammad ibn Musa al-Khwarizmi's** geometric completing-the-square algorithms in 820 AD Baghdad (`{{key:POLY}}` degree 2) and **Gerolamo Cardano's** closed-form cubic and quartic radical solutions in *Ars Magna* (1545) {{cite:cardano1545}} (`{{key:POLY}}` degrees 3–4) to **Niels Henrik Abel's** 1824 impossibility theorem proving that no general radical formula exists for polynomials of degree 5 or higher—algebraists sought to isolate unknown roots through finite chains of arithmetic and $n$-th roots. Yet in mechanical, chemical, and aerospace engineering, physical conservation laws routinely couple polynomials with logarithms, exponentials, and trigonometric functions that cannot be inverted symbolically at all.

### Turbulent Pipe Flow & The Colebrook-White Implicit Equation

Consider water surging through a municipal aqueduct or cryogenic kerosene rushing into a rocket turbopump. The friction factor $f$ across the turbulent pipe wall is governed by Cyril F. Colebrook's landmark 1939 equation {{cite:colebrook1939}}:

$$\frac{1}{\sqrt{f}} = -2.0 \log_{10} \left( \frac{\varepsilon}{3.7 D} + \frac{2.51}{\operatorname{Re} \sqrt{f}} \right)$$

Inspect this equation with an analytical eye: the unknown Darcy friction factor $f$ appears on *both* sides of the equals sign—trapped inside an inverse square root on the left, and buried inside both a base-10 logarithm and a square root denominator on the right.

It is mathematically impossible to isolate $f$ using elementary symbolic algebra. There is no closed-form formula. The same mathematical barrier governs Johannes Kepler's equation for planetary orbital mechanics:

$$M = E - e \sin E$$

You cannot isolate the eccentric anomaly $E$ with pencil and paper. To design a municipal water main that withstands water hammer transients, or to steer an interplanetary spacecraft through a gravitational assist, the engineer must solve transcendental equations numerically.

### The Fatal Flaw of Naive Root Finding
Early computational engineers turned to the classic Newton-Raphson iteration:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Newton-Raphson is quadratic and fast—until the function encounters a local extremum, an inflection point, or an asymptotic plateau where the derivative $f'(x) \approx 0$. When the denominator vanishes, the tangent line becomes nearly horizontal, catapulting the next estimate into numerical oblivion. In an embedded autopilot or real-time chemical process controller, a divergent Newton solver can trigger catastrophic system instability.

### Richard Brent (1973): The Art of Algorithmic Paranoia
In 1973, the Australian mathematician Richard P. Brent asked a deceptively simple question: can we build a root finder that runs nearly as fast as Newton-Raphson on smooth curves, requires no analytical derivative, and is mathematically guaranteed never to diverge on pathological functions? His answer—published in *Algorithms for Minimization Without Derivatives* {{cite:brent1973}}—became the universal standard of numerical computing through what might be called **algorithmic paranoia**.

Brent begins by enclosing the root inside a tight bracket $[a, b]$ where $f(a)$ and $f(b)$ have opposite signs ($f(a) \cdot f(b) < 0$). Because a continuous curve cannot cross from negative to positive without passing through zero, the Intermediate Value Theorem guarantees that a true root lies trapped inside the interval. Whenever three distinct sample points are available, Brent's algorithm sprints toward that root using **Inverse Quadratic Interpolation (IQI)**—fitting a sideways parabola $x = P(y)$ through $(f(a), a)$, $(f(b), b)$, and $(f(c), c)$ and evaluating it directly at $y = 0$. Left unchecked, a parabolic fit can occasionally shoot wild, so Brent wrapped the interpolator in unyielding watchdog tests: if a proposed parabolic leap lands outside the active bracket $[a, b]$, or if it fails to shrink the bracket width by at least $50\%$ every two steps, the solver immediately overrides the interpolation and takes a rock-solid **bisection step** at the midpoint.

The result is the best of both worlds. Brent's method converges to 12 decimal places in fewer than 10 iterations on well-behaved engineering equations, yet falls back to the ironclad safety of bisection the instant a curve turns steep or flat. On the StackCalc SC-32, pressing `{{key:SOLVE}}` puts Richard Brent's hybrid architecture directly at your fingertips.

---

{{res:sc32_cubic_roots:screenshot|Cubic polynomial x^3 - 6x^2 + 11x - 6 = 0 solved via POLY}}

## Physical Equilibrium, Root Bracketing, and Hybrid Solvers

Root finding determines the equilibrium state $x^*$ where opposing physical forces cancel to zero: the neutral axis of a loaded structural beam where tensile and compressive stresses balance, the hydraulic flow rate where Darcy-Weisbach pipe friction matches gravitational head drop, or the orbital eccentric anomaly $E$ that satisfies Kepler's time equation $f(x^*) = 0$. Physically, bracketing a root is identical to closing the jaws of a vernier caliper around the zero-crossing interval $[a, b]$ where the residual flips sign.

On the StackCalc SC-32, you load those two bracket bounds $(a, b)$ directly into Registers $Y$ and $X$ and enter the governing postfix expression into the Equation Editor. For cubic and quadratic characteristic equations, `{{key:POLY}}` extracts all real and complex roots analytically via Cardano's and Viète's closed-form resolvents; for arbitrary transcendental equations, `{{key:SOLVE}}` drives Richard Brent's hybrid algorithm, combining the guaranteed enclosure of bisection with the superlinear $\phi \approx 1.618$ convergence of secant and inverse quadratic interpolation.

{{blocks:algebra_factoring_area|Algebra Factoring Stage Root Model}}
*Figure 7.1: Geometric decomposition of polynomial roots on the Algebra Factoring Stage, illustrating factor dimensions prior to numerical bracketing.*

---

## Characteristic Polynomial Solver (`{{key:POLY}}`)

Root extraction of polynomial characteristic equations is fundamental to structural vibration analysis, aircraft flight control stability, circuit pole-zero placement, and chemical reaction equilibria.

The StackCalc SC-32 features an onboard **Characteristic Polynomial Solver (`{{key:POLY}}`)** mapped to Right Shift `{{key:↱}}` on the `{{key:XEQ}}` key. The engine extracts all real and complex roots for general cubic and quadratic polynomials analytically:

$$A x^3 + B x^2 + C x + D = 0$$

| Interface Element | Display Legend / Key Assignment | Functional Action / Internal Allocation |
| :--- | :--- | :--- |
| **Menu Prompt** | `Ax^3 + Bx^2 + Cx + D = 0` | Prompts for polynomial coefficient entry |
| **LFU Softkeys** | `{{key:A}} {{key:B}} {{key:C}} {{key:D}} {{key:EXEC}} {{key:CLR}}` | Softkey assignments for coefficient entry and execution |
| **Internal Storage: Root 1** | Variables `"1"` (Real), `"2"` (Imaginary) | Stores first calculated root |
| **Internal Storage: Root 2** | Variables `"3"` (Real), `"4"` (Imaginary) | Stores second calculated root |
| **Internal Storage: Root 3** | Variables `"5"` (Real), `"6"` (Imaginary) | Stores third calculated root |
| **Active Stack Output** | Register $Y$: $\operatorname{Re}(\text{Root 1})$, Register $X$: $\operatorname{Im}(\text{Root 1})$ | Primary root delivered directly in $(Y, X)$ Gaussian format |

### Cardano's Analytical Cubic & Quadratic Engine
Numerical root finders are indispensable for transcendental curves, but when an engineer faces a cubic or quadratic characteristic polynomial, iterative guessing has blind spots: a numerical search can step right over two closely-spaced resonant poles, stall near an inflection point, or miss complex conjugate roots that govern underdamped oscillatory stability. To eliminate those blind spots, the `{{key:POLY}}` engine implements **Gerolamo Cardano's closed-form analytic cubic resolvent** alongside a native complex quadratic solver.

When the leading cubic coefficient $A$ is non-zero, Cardano's method begins with a geometric coordinate shift $x = t - \frac{B}{3A}$ that slides the horizontal origin directly onto the cubic's point of inflection. That single substitution annihilates the quadratic $x^2$ term and reduces the general cubic to the clean **depressed cubic**:

$$t^3 + p t + q = 0, \qquad p = \frac{3AC - B^2}{3A^2}, \qquad q = \frac{27A^2D - 9ABC + 2B^3}{27A^3}$$

The qualitative character of the three roots is governed entirely by the **cubic discriminant**:

$$\Delta = \left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3$$

To evaluate the depressed roots without numerical branch cuts, the SC-32 computes the complex radical $u = \sqrt[3]{-q/2 + \sqrt{\Delta}}$ via polar De Moivre trisection ($r^{1/3}[\cos(\theta/3) + i\sin(\theta/3)]$) and pairs it with $v = \frac{-p/3}{u}$ (or $\sqrt[3]{-q/2 - \sqrt{\Delta}}$ when $|u| \le 10^{-14}$), rotating in the complex plane by the primitive cube roots of unity $\omega = -\frac{1}{2} + i\frac{\sqrt{3}}{2}$ and $\omega^2$. When $\Delta > 0$, the cubic crosses the horizontal axis only once, yielding one real root ($t_1 = u + v$) and a complex conjugate pair ($t_{2,3} = \omega u + \omega^2 v,\; \omega^2 u + \omega v$). When $\Delta = 0$, the curve is tangent to the axis, producing three real roots with at least one repeated root. Most intriguing of all is $\Delta < 0$—the famous *casus irreducibilis* that mystified sixteenth-century algebraists because the expression $\sqrt{\Delta}$ becomes purely imaginary precisely when all three roots of the cubic are real and distinct! As Rafael Bombelli and François Viète discovered, taking the polar cube root of those complex conjugates trisects their phase angle ($\cos(\theta/3)$) so their imaginary parts cancel out completely, leaving all three distinct real roots with residuals $< 10^{-12}$ clamped cleanly to zero and sorted with real roots first.

### Singularity Rule ($A \ne 0$ or $B \ne 0$), Native Quadratic Fallback & Quadratic Embedding ($D = 0$ Default)
Because a polynomial requires at least a quadratic or cubic leading term, at least one of $A$ or $B$ must be non-zero; pressing `{{key:EXEC}}` when both $A = 0$ and $B = 0$ triggers `A ≠ 0`. Any coefficient you do not explicitly enter **defaults to $0$**, which gives you two convenient ways to solve a quadratic equation $a x^2 + b x + c = 0$. In **quadratic embedding**, you simply enter the quadratic coefficients into the first three softkeys via `a {{key:A}} b {{key:B}} c {{key:C}} {{key:EXEC}}`; with $D = 0$ by default, the solver factors $a x^3 + b x^2 + c x = x(a x^2 + b x + c) = 0$, extracting the trivial root $0$ alongside the two exact quadratic roots in variables `3` (`{{key:RCL}} 3`) and `5` (`{{key:RCL}} 5`):

$$a x^3 + b x^2 + c x + 0 = x(a x^2 + b x + c) = 0 \implies x = \frac{-b \pm \sqrt{b^2 - 4 a c}}{2 a}$$

Alternatively, in **native quadratic fallback**, you leave $A = 0$ and enter `b {{key:B}} c {{key:C}} d {{key:D}} {{key:EXEC}}`, which invokes the closed-form complex quadratic formula $x = \frac{-C \pm \sqrt{C^2 - 4BD}}{2B}$ directly across variables `1`–`4`. The same zero-default rule streamlines sparse cubics: to solve a pure cubic such as $x^3 - 8 = 0$, you only need to key `1 {{key:A}} 8 {{key:+/-}} {{key:D}} {{key:EXEC}}`, since $B$ and $C$ default to zero automatically.

---

### Cardano Cubic with Three Real Roots

Suppose a three-mass mechanical oscillator or a 3D principal stress state has the cubic characteristic polynomial:
$$x^3 - 6x^2 + 11x - 6 = 0$$
Factoring by inspection shows three distinct real roots:
$$(x - 1)(x - 2)(x - 3) = 0 \implies x_1 = 1.0, \quad x_2 = 2.0, \quad x_3 = 3.0$$

To extract all three roots analytically on the stack, press `{{key:POLY}}` to open the polynomial workspace on the LFU softkeys. Key `1` and press `{{key:A}}` to store the cubic coefficient $A = 1.0$, key `6 {{key:+/-}}` and press `{{key:B}}` to store $B = -6.0$, key `11` and press `{{key:C}}` to store $C = 11.0$, and key `6 {{key:+/-}}` and press `{{key:D}}` to store $D = -6.0$. Pressing `{{key:EXEC}}` immediately evaluates Cardano's closed-form resolvent:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Coefficient $A = 1.0$ |
| 2 | `6 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-6.0000$ | Coefficient $B = -6.0$ |
| 3 | `11 {{key:C}}` | $0.0000$ | $1.0000$ | $-6.0000$ | $11.0000$ | Coefficient $C = 11.0$ |
| 4 | `6 {{key:+/-}} {{key:D}}` | $1.0000$ | $-6.0000$ | $11.0000$ | $-6.0000$ | Coefficient $D = -6.0$ |
| 5 | `{{key:EXEC}}` | $1.0000$ | $-6.0000$ | **$1.000000$** | **$0.000000$** | Primary root $r_1 = 1.0 + 0.0i$ in $(Y, X)$; roots $1, 2, 3$ stored in vars `1`–`6` |

Upon pressing `{{key:EXEC}}`, the Cardano analytical solver simultaneously writes all three complex root pairs $(r_k = \operatorname{Re} + i\operatorname{Im})$ into numbered storage registers `1` through `6`:

| Storage Variable | Extracted Value | Polynomial Root Assignment |
| :---: | :---: | :--- |
| **`1` / `2`** | **`1.0000000000` / `0.0000000000`** | Root $r_1 = 1.0 + 0.0i$ (also placed in Registers $Y$ and $X$) |
| **`3` / `4`** | **`2.0000000000` / `0.0000000000`** | Root $r_2 = 2.0 + 0.0i$ |
| **`5` / `6`** | **`3.0000000000` / `0.0000000000`** | Root $r_3 = 3.0 + 0.0i$ |

Because all three roots are stored in non-volatile variables `1` through `6`, you can recall any root to the active stack at will: `{{key:RCL}} 1` and `{{key:RCL}} 2` recall the real and imaginary parts of Root 1 ($1.0 + 0.0i$), `{{key:RCL}} 3` and `{{key:RCL}} 4` recall Root 2 ($2.0 + 0.0i$), and `{{key:RCL}} 5` and `{{key:RCL}} 6` recall Root 3 ($3.0 + 0.0i$).

### Cubic with Complex Conjugate Roots

Now consider a system that combines one real decay mode with an undamped oscillatory pair:
$$x^3 - x^2 + x - 1 = 0 \implies (x - 1)(x^2 + 1) = 0$$
Its exact roots are one real root and two purely imaginary conjugate roots:
$$x_1 = 1.0 + 0.0i, \quad x_2 = 0.0 + 1.0i, \quad x_3 = 0.0 - 1.0i$$

Press `{{key:POLY}}`, load the alternating coefficients with `1 {{key:A}}`, `1 {{key:+/-}} {{key:B}}`, `1 {{key:C}}`, and `1 {{key:+/-}} {{key:D}}`, and press `{{key:EXEC}}`:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Coefficient $A = 1.0$ |
| 2 | `1 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-1.0000$ | Coefficient $B = -1.0$ |
| 3 | `1 {{key:C}}` | $0.0000$ | $1.0000$ | $-1.0000$ | $1.0000$ | Coefficient $C = 1.0$ |
| 4 | `1 {{key:+/-}} {{key:D}}` | $1.0000$ | $-1.0000$ | $1.0000$ | $-1.0000$ | Coefficient $D = -1.0$ |
| 5 | `{{key:EXEC}}` | $1.0000$ | $-1.0000$ | **$1.000000$** | **$0.000000$** | Real $r_1=1$ in $Y$, Imag $r_1=0$ in $X$; conjugate pair $\pm i$ in vars `3`–`6` |

The real root $r_1 = 1.000000 + 0.000000i$ is delivered immediately to $(Y, X)$ and stored in Variables `1` and `2`, while the complex conjugate pair is written cleanly into Variables `3` and `4` ($\operatorname{Re} = \mathbf{0.000000},\; \operatorname{Im} = \mathbf{+1.000000}$) and Variables `5` and `6` ($\operatorname{Re} = \mathbf{0.000000},\; \operatorname{Im} = \mathbf{-1.000000}$).

---

## Richard Brent's Numerical Root Finder ({{key:SOLVE}})

For general non-linear, transcendental, or piecewise equations where closed-form algebraic formulas do not exist, the SC-32 provides **Richard Brent's Numerical Root Finder (`{{key:SOLVE}}`)**.

### Richard Brent's Two-Phase Hybrid Root Solver State Machine (1973)

When you invoke `{{key:SOLVE}}`, the SC-32 executes a two-phase state machine modeled directly on Brent's 1973 algorithm. In **Phase 1 (Guarded Secant & Golden-Ratio Outward Bracket Search)**, the engine starts from your initial guess $x_0$ (generating a companion probe via $\Delta = 0.1|x_0|$ for $|x_0| < 1$ or $0.1$, or adopting the $(Y, X)$ stack bounds if $x_0$ lies outside the valid domain) and checks whether $f(a)$ and $f(b)$ already have opposite signs. If $f(a) \cdot f(b) > 0$, it marches outward for up to 50 steps using clamped secant steps—or golden-ratio $\phi = 1.61803398875$ expansion whenever $|f(b) - f(a)| \le 10^{-14}$. If a trial step crosses a domain boundary such as $\ln x$ or $\sqrt{x}$ for $x \le 0$, automatic domain recovery pulls the step back inside the valid region, while tangent even-multiplicity roots are captured automatically when $|b - a| < 10^{-12}$ and $|f(b)| < 10^{-7}$.

Once a sign change $f(a) \cdot f(b) \le 0$ is bracketed, the solver enters **Phase 2 (Inverse Quadratic & Secant Interpolation)** for up to 100 iterations. Whenever three distinct function values $(f(a), f(b), f(c))$ are available ($|f(a)-f(c)| > 10^{-15}$ and $|f(b)-f(c)| > 10^{-15}$), the solver computes an **Inverse Quadratic Interpolation (IQI)** step; otherwise, it computes a **Linear Secant step**. Before accepting that interpolated estimate $s$, the engine enforces **Brent's five bisection watchdog conditions**: $s$ must land strictly inside the three-quarter window $\left(\frac{3a+b}{4}, b\right)$, it must contract the step size by at least $50\%$ compared to the prior step ($|b-c|$ after bisection or $|c-d|$ after interpolation), and the step must exceed the machine-epsilon threshold $\text{tol} = 2\varepsilon_{\text{mach}}|b| + \frac{1}{2}\cdot 10^{-12}$. If any one of those five conditions fails, the solver immediately rejects interpolation and executes a guaranteed **Bisection step** $s = \frac{1}{2}(a + b)$, terminating as soon as $|f(b)| \le 10^{-13}$ or the half-bracket width satisfies $\frac{1}{2}|a - b| \le \text{tol}$.

{{blocks:algebra_boxes_hero|Algebra Boxes Studio Kit Hardware}}
*Figure 7.2: The physical Algebra Factoring Studio hardware kit, showing the 40 stackable Miniblock tiles ($+x^2/-x^2$ flats, $+x/-x$ rods, and $+1/-1$ unit tiles) and the interlocking $90^\circ$ L-Frame Factoring Stage.*

### From Al-Khwarizmi's Factoring Tiles to Zero-Pair Root Bracketing on the $90^\circ$ L-Frame Stage

Why do closed-form algebraic solvers (`{{key:POLY}}`) and bracketed numerical solvers (`{{key:SOLVE}}`) complement each other so naturally? Because they represent the two foundational physical operations of the **Algebra Factoring Studio** (*Figure 7.1* and *Figure 7.2*): **completing a rectangular area inside the $90^\circ$ L-Frame Factoring Stage** and **zero-pair sign cancellation across $+1/-1$ and $+x/-x$ tiles**.

The Algebra Factoring Studio kit contains 40 stackable Miniblock algebra tiles engineered around a $7.0\text{ mm}$ visible step height: four $x^2$ square flats ($38.6 \times 38.6\text{ mm}$, two positive $+x^2$ and two negative $-x^2$), twelve $x$ linear rods ($38.6 \times 19.0\text{ mm}$, six positive $+x$ and six negative $-x$), and twenty-four unit tiles ($19.0 \times 19.0\text{ mm}$, twelve positive $+1$ and twelve negative $-1$), all docking into a two-rail interlocking $90^\circ$ L-Frame Factoring Stage with a horizontal `base_rail` for the first linear factor $(x + a)$ and a perpendicular vertical `height_rail` for the second linear factor $(x + b)$.

In 820 AD in Baghdad, the Persian mathematician **Muhammad ibn Musa al-Khwarizmi** wrote *Al-Kitāb al-mukhtaṣar fī ḥisāb al-jabr wa'l-muqābala*—the treatise that gave the world both the word *algebra* (*al-jabr*, restoration) and the word *algorithm* (from his Latinized name, *Algoritmi*). When al-Khwarizmi solved quadratic equations such as $x^2 + 4x = 5$ (or his classic $x^2 + 10x = 39$), he possessed no modern symbolic formula. Instead, he solved the polynomial literally by docking physical **Algebra Factoring Tiles** into the corner of the $90^\circ$ L-Frame Stage. You begin by docking one $+x^2$ square flat ($38.6 \times 38.6\text{ mm}$) snugly into the $90^\circ$ origin corner where the horizontal `base_rail` and vertical `height_rail` interlock. Next, you split the linear term $4x$ symmetrically into two equal wings, placing two $+x$ rods ($38.6 \times 19.0\text{ mm}$ each) along the right edge of the $+x^2$ flat and two $+x$ rods along the top edge to form an L-shaped gnomon of area $x^2 + 2x + 2x$. Inspecting the upper-right corner where the two $+x$ wings meet reveals an unmistakable $2 \times 2$ square notch waiting to be filled: docking **four $+1$ unit tiles** ($19.0 \times 19.0\text{ mm}$ each) into that corner literally *completes the square* into a flush $(x + 2) \times (x + 2)$ square on the stage. Adding those same four $+1$ unit tiles to the right-hand side yields $(x + 2)^2 = 5 + 4 = 9 = 3^2$, exposing $x + 2 = 3 \implies \mathbf{x = 1}$ (and similarly for al-Khwarizmi's $x^2 + 10x = 39$, splitting $10x$ into two $5 \times x$ wings leaves a $5 \times 5 = 25$ corner square so $(x + 5)^2 = 39 + 25 = 64 \implies \mathbf{x = 3}$).

What if a polynomial has mixed signs, such as $x^2 + x - 6 = (x + 3)(x - 2) = 0$? When you place $x + 3$ along the `base_rail` and $x - 2$ along the `height_rail`, the interior of the L-Frame Stage contains one $+x^2$ flat, three $+x$ rods, two $-x$ rods, and six $-1$ unit tiles. Stacking the two $-x$ rods directly on top of two $+x$ rods demonstrates **zero-pair cancellation**: each $(+x, -x)$ pair annihilates to zero, leaving the net polynomial $x^2 + x - 6$.

That same **zero-pair cancellation** explains Richard Brent's root-bracketing theorem ($f(a) \cdot f(b) \le 0$) when `{{key:SOLVE}}` attacks a transcendental equation. At the lower bracket endpoint $x = a$ where $f(a) < 0$, the evaluated residual leaves an uncancelled stack of **negative ($-1$) unit tiles**, whereas at the upper bracket endpoint $x = b$ where $f(b) > 0$, the evaluated residual leaves an uncancelled stack of **positive ($+1$) unit tiles**. By Bolzano's **Intermediate Value Theorem**, as $x$ sweeps continuously across $[a, b]$ from a negative $-1$ tile residual to a positive $+1$ tile residual, there must exist an exact root $x^* \in [a, b]$ where every $+1$ and $-1$ contribution forms a complete zero-pair and the residual stack vanishes to the bare stage floor ($f(x^*) = 0$).

### The Three Convergence Mechanics of Brent's Algorithm
Brent's hybrid solver shifts seamlessly among three classic root-finding gears depending on the local geometry of $f(x)$. Its safety net is the **Bisection Method**, which cuts the bracket interval exactly in half at $m = (a + b) / 2$; bisection is guaranteed to converge on any continuous sign-change bracket, though at a steady linear pace of $1\text{ bit}$ of precision per iteration ($p = 1.000$). When two distinct sample points are available, the solver can accelerate into the **Secant Method**, drawing a straight chord through $(a, f(a))$ and $(b, f(b))$ to achieve superlinear golden-ratio convergence ($p = \phi \approx 1.618$). And whenever three distinct sample points $(f(a), a)$, $(f(b), b)$, and $(f(c), c)$ are available, the engine shifts into top gear—**Inverse Quadratic Interpolation (IQI)**—fitting a Lagrange parabola $x = P(y)$ sideways as a function of $y$ and evaluating it directly at $y = 0$:

$$x = \frac{a f(b) f(c)}{(f(a)-f(b))(f(a)-f(c))} + \frac{b f(a) f(c)}{(f(b)-f(a))(f(b)-f(c))} + \frac{c f(a) f(b)}{(f(c)-f(a))(f(c)-f(b))}$$

Because fitting $x$ as a quadratic function of $y$ guarantees a single unique crossing of the $y = 0$ axis, IQI reaches an asymptotic order of convergence $p \approx 1.839$—approaching the quadratic speed of Newton-Raphson without ever computing a derivative.

| Root Finding Algorithm | Asymptotic Order ($p$) | Derivative Required? | Convergence Guarantee | Vulnerability / Failure Risk |
| :--- | :---: | :---: | :---: | :--- |
| **Bisection** | $1.000$ | No | Guaranteed (bracketed) | Slow, linear progress ($1\text{ bit/iteration}$) |
| **Newton-Raphson** | $2.000$ | Yes ($f'(x)$) | Local only | Divergence near $f'(x) \approx 0$; inflection loops |
| **Secant Method** | $1.618$ | No | Local only | Undamped oscillations on non-convex curves |
| **Brent-Dekker** | $1.839$ | No | Guaranteed (bracketed) | **Zero failure** (automatic bisection fallback) |

---

### Brent's Solver on Wallis's Benchmark Cubic: $x^3 - 2x - 5 = 0$

In 1685, John Wallis proposed a deceptively simple cubic equation that Isaac Newton and Joseph Raphson adopted as the historic benchmark for testing iterative root-finding convergence:
$$f(x) = x^3 - 2x - 5 = 0$$
Starting from Newton's initial estimate $x = 2.0$ (where $f(2) = 8 - 4 - 5 = -1.0$), we can extract the classic real root $x^* \approx 2.0945514815423$ by programming the postfix residual `X {{key:3}} {{key:yˣ}} 2 {{key:ENTER}} X {{key:×}} {{key:-}} 5 {{key:-}}` into `{{key:EQN}}`, seeding the initial estimate with `2 {{key:STO}} X`, and executing Brent's solver with `{{key:SOLVE}} X`:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `2 {{key:STO}} X` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Initial guess loaded |
| 2 | `{{key:SOLVE}} X` | $0.0000$ | $0.0000$ | $2.0000$ | **$2.0945514815$** | Initial guess lifts to $Y$; root extracted in $X$ |

The display outputs the root **$x = 2.0945514815$**. Because the SC-32 includes *both* an analytical Cardano cubic engine (`{{key:POLY}}`) and Richard Brent's numerical root finder (`{{key:SOLVE}}`), any cubic equation can be audited along two completely independent mathematical pathways. On **Wallis's benchmark ($x^3 - 2x - 5 = 0$)** above, `{{key:SOLVE}}` bracketed the real root numerically to `2.0945514815`; if you instead press `{{key:POLY}}` and enter the cubic coefficients (`1 {{key:A}} 0 {{key:B}} 2 {{key:+/-}} {{key:C}} 5 {{key:+/-}} {{key:D}} {{key:EXEC}}`), Cardano's closed-form radical formula extracts the exact same real root **$2.0945514815$** in Register $Y$ while simultaneously revealing the complex conjugate pair $-1.047276 \pm 1.135940i$ in variables `3`–`6`. Conversely, in the **Van der Waals real-gas equation of state (explored below)**, expanding $\left(P + \frac{a}{V^2}\right)(V - b) = RT$ for compressed $\text{CO}_2$ ($P = 50\text{ atm}, T = 300\text{ K}$) into $50V^3 - 26.753V^2 + 3.59V - 0.153293 = 0$ lets `{{key:POLY}}` solve it in closed form for **$V_m = 0.358736\text{ L/mol}$**, whereas programming the unexpanded balance $\left(50 + \frac{3.59}{V^2}\right)(V - 0.0427) - 24.618 = 0$ directly into `{{key:EQN}}` and running `0.49 {{key:STO}} V {{key:SOLVE}} V` reaches the exact same **$0.358736\text{ L/mol}$** without expanding a single term by hand.

### Manual Root Iteration vs. Hardware `{{key:POLY}}` & `{{key:SOLVE}}` Workflows

The table below compares parenthesized solver string entry and manual root graphing against the SC-32's dedicated `{{key:SOLVE}}` and `{{key:POLY}}` engines:

| Challenge / Metric | Conventional Algebraic Calculator (Infix) | Algebraic Strokes | SC-32 RPN Stack Method | SC-32 Strokes | Stack Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **Transcendental Root Finding**: Colebrook-White friction factor | String entry in numeric solver: `solve(1/√(F) + 2*log(0.001/3.7 + 2.51/(100000*√(F))), F, 0.02)` (54 strokes). Missing or mismatched parenthesis throws syntax error; Newton tangent iteration prone to divergence near asymptotic plateaus. | 54 | **Brent's Hybrid Root Finder (`{{key:SOLVE}}`)**: Define postfix equation in `{{key:EQN}}`, load initial estimate `0.02 {{key:STO}} F`, press `{{key:SOLVE}} F` (24 strokes). Guarded Inverse Quadratic Interpolation contracts interval to $10^{-12}$ in $\le 8$ iterations with guaranteed convergence. | 24 | **56% fewer strokes + guaranteed bisection fallback** |
| **Cubic Characteristic Roots**: $x^3 - 6x^2 + 11x - 6 = 0$ | High-degree numerical approximation or graph tracing; requires setting window, guessing each root separately, and rerunning solver 3 times (48 strokes). Complex conjugate roots invisible. | 48 | **Cardano Analytic Solver (`{{key:POLY}}`)**: Enter coefficients into softkeys `1 {{key:A}} 6 {{key:+/-}} {{key:B}} 11 {{key:C}} 6 {{key:+/-}} {{key:D}}`, press `{{key:EXEC}}` (16 strokes). Closed-form Cardano resolvent delivers all three real/complex roots to $(Y, X)$ and variables 1–6 in $<5\text{ ms}$. | 16 | **67% fewer strokes + all real & complex roots simultaneously** |

---

## Horner's Method for Polynomial Stack Evaluation

Evaluating a high-degree polynomial in standard algebraic form requires calculating redundant powers $x^2, x^3, \dots, x^n$. **Horner's Method** factors the polynomial into nested linear binomials:

$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0 = (\dots((a_n x + a_{n-1}) x + a_{n-2}) x + \dots + a_1) x + a_0$$

### RPN Stack Elegance of Horner's Method
On the SC-32, Horner's method executes with **zero memory storage registers** and **zero parentheses**. At each stage, keying the multiplier $x = 2.5$ automatically lifts the running polynomial accumulator from Register $X$ into Register $Y$, allowing each nested multiplication and addition to cascade cleanly through the stack.

To evaluate $P(x) = 4x^4 - 3x^3 + 2x^2 - 5x + 7$ at $x = 2.5$ in nested form $P(2.5) = (((4(2.5) - 3)(2.5) + 2)(2.5) - 5)(2.5) + 7$, keying `{{res:sc32_07_polynomials_brent_solver_seq_01:keys}}` streams directly to **`{{res:sc32_07_polynomials_brent_solver_seq_01:value}}`**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `2.5 {{key:ENTER}} 4 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | First term: $a_4 x = 4(2.5) = 10.0$ |
| 2 | `3 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $7.0000$ | Add next coefficient: $10.0 - 3 = 7.0$ |
| 3 | `2.5 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $17.5000$ | Digit entry lifts $7.0$ to $Y$; multiply: $(7.0)(2.5) = 17.5$ |
| 4 | `2 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $19.5000$ | Add next coefficient: $17.5 + 2 = 19.5$ |
| 5 | `2.5 {{key:×}} 5 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $43.7500$ | Lift & multiply: $(19.5)(2.5) - 5 = 43.75$ |
| 6 | `2.5 {{key:×}} 7 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$116.3750$** | Final evaluation: $(43.75)(2.5) + 7 = \mathbf{116.3750}$ |

When evaluating a polynomial at an argument $x$ with many digits (e.g., $x = 2.71828$), classic 4-register RPN masters flood the stack first via `2.71828 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}`. Because Register $T$ replicates downward on every dyadic drop, you stream `4 {{key:×}} 3 {{key:-}} {{key:×}} 2 {{key:+}} {{key:×}} 5 {{key:-}} {{key:×}} 7 {{key:+}}` without ever re-keying $x$ or touching a storage register. Alternatively, store $x$ once via `2.71828 {{key:STO}} A` and evaluate with `4 {{key:RCL}} A {{key:×}} 3 {{key:-}} {{key:RCL}} A {{key:×}} 2 {{key:+}} ...` (no `{{key:ENTER}}` needed before `{{key:RCL}}`). Either way, the entire degree-4 polynomial requires only 4 multiplications and 4 additions, with zero exponentiations.

---

## Survey of Polynomial & Implicit Equations Across Engineering
Across fluid hydraulics, thermodynamics, electromagnetics, and astrodynamics, physical conservation laws routinely produce multi-degree polynomials or implicit transcendental equations that call for `{{key:POLY}}`, Horner's nested evaluation, or Richard Brent's `{{key:SOLVE}}` engine.

In **fluid and open-channel hydraulics**, conserving specific momentum across an open-channel hydraulic jump with upstream supercritical depth $y_1$ and Froude number $\text{Fr}_1 = v_1 / \sqrt{g y_1}$ produces the **Bélanger conjugate depth quadratic**:

$$y_2^2 + y_1 y_2 - \frac{2 q^2}{g y_1} = y_2^2 + y_1 y_2 - 2 y_1^2 \text{Fr}_1^2 = 0$$

whose positive subcritical conjugate root $y_2 = \frac{y_1}{2}\left(\sqrt{1 + 8\text{Fr}_1^2} - 1\right)$ can be extracted directly via `{{key:POLY}}` or stack evaluation. Likewise, equating a centrifugal pump impeller head curve $H_p(Q) = H_0 + b_1 Q - b_2 Q^2$ to a turbulent pipeline resistance curve $H_s(Q) = H_{\text{stat}} + k Q^2$ produces a quadratic polynomial $(b_2 + k)Q^2 - b_1 Q - (H_0 - H_{\text{stat}}) = 0$ for the operating flow rate $Q$. Planar **Couette-Poiseuille channel flow** under an adverse pressure gradient $dp/dx$ follows the parabolic velocity profile $u(y) = \frac{1}{2\mu}\frac{dp}{dx}(y^2 - h y) + \frac{U}{h}y$, terminal particle settling under combined linear Stokes and quadratic Newton drag satisfies $c_2 v^2 + c_1 v - W = 0$, and implicit turbulent pipe friction obeys the transcendental **Colebrook-White** equation.

In **thermodynamics, acoustics, and electromagnetics**, real-gas isotherms obey the cubic **van der Waals** polynomial $P V^3 - (Pb + RT)V^2 + aV - ab = 0$, while standard-atmosphere pressure-altitude profiles $P(h) = a_3 h^3 + a_2 h^2 + a_1 h + a_0$ and polynomial heat-capacity curves evaluate cleanly via **Horner's nested scheme**. In counter-flow heat exchangers, solving for an unknown terminal temperature difference $\Delta T_2$ from a target **Log Mean Temperature Difference** $\text{LMTD} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)}$ requires Brent's `{{key:SOLVE}}` engine, as do Wien's spectral peak root $5(1 - e^{-x}) - x = 0$ and the Shockley diode load-line equation, while **Green's empirical rational fill-factor equation** $FF = \frac{v_{\text{oc}} - \ln(v_{\text{oc}} + 0.72)}{v_{\text{oc}} + 1}$ evaluates solar cell efficiency from normalized open-circuit voltage $v_{\text{oc}} = V_{\text{oc}} / V_T$. Even acoustic resonators lead directly to quadratics: in a cylindrical **Helmholtz resonator** of volume $V$ and neck length $L$, incorporating Rayleigh's radiation end-correction $L' = L + 1.7a$ alongside throat area $A = \pi a^2$ in $f_0 = \frac{c}{2\pi}\sqrt{\frac{A}{V L'}}$ produces an explicit quadratic equation for the neck radius $a$:

$$a^2 - \left(\frac{6.8\pi f_0^2 V}{c^2}\right) a - \left(\frac{4\pi f_0^2 V L}{c^2}\right) = 0$$

alongside RLC circuit state poles, high-frequency **Kelvin skin-depth AC resistance** quadratics, and **Gaussian laser cavity beam-waist** stability equations ($z^2 - L z + z_0^2 = 0$, where $z_0^2 = L(2f - L)$) solved via `{{key:POLY}}`.

In **relativistic mechanics, astrodynamics, and structural/geotechnical buckling**, substituting total relativistic energy $E = K + m_0 c^2$ into Einstein's invariant $E^2 - (pc)^2 - (m_0 c^2)^2 = 0$ yields the quadratic kinetic-energy polynomial:

$$K^2 + 2(m_0 c^2) K - (pc)^2 = 0$$

which extracts kinetic energy $K$ from momentum $pc$. In orbital and compressible-flow mechanics, **Kepler's anomaly equation** $M = E - e\sin E$ and the **de Laval supersonic nozzle Area-Mach relation** $\frac{A}{A^*} = \frac{1}{M}\left[\frac{2}{\gamma+1}\left(1 + \frac{\gamma-1}{2}M^2\right)\right]^{\frac{\gamma+1}{2(\gamma-1)}}$ require `{{key:SOLVE}}`, whereas the **vis-viva hyperbolic excess velocity** quadratic $v_\infty^2 - v^2 + \frac{2\mu}{r} = 0$, the **geostationary orbital radius pure cubic** $r^3 - \frac{\mu T^2}{4\pi^2} = 0$, and the **gyroscopic nutation-precession characteristic quadratic** $I_t \Omega^2 - I_p \omega \Omega + M g L = 0$ yield directly to `{{key:POLY}}`, joined in solid mechanics by 3D principal stress tensor cubics, Euler/cantilever beam deflection polynomials, **Lamé thick-walled cylinder** wall-thickness quadratics, **Rankine Mohr-Coulomb slip-plane** quadratics ($\tan^2\theta + 2\tan\phi\tan\theta - 1 = 0$, where $K_a = \tan^2\theta$), **annular clutch torque** cubics, and **nuclear reactor critical buckling** equations.

---

### Root Brackets, Degenerate Leading Coefficients, and Tangent Extrema

Understanding how `{{key:SOLVE}}` and `{{key:POLY}}` behave at mathematical boundaries lets you diagnose any equation immediately. For `{{key:SOLVE}}` to guarantee convergence via the Intermediate Value Theorem, your initial guesses in Registers $Y$ and $X$ should bracket the root so that $f(Y) \cdot f(X) \le 0$. If both initial guesses share the same sign, Phase 1 automatically launches a guarded secant and golden-ratio outward search; if the curve never crosses zero (for example, $e^x + 1 = 0$), execution halts after 50 expansion steps with `Error: NO ROOT FOUND`, leaving your stack registers preserved until you press `{{key:C}}` to clear the banner. What if the root is an even-multiplicity tangent root such as $f(x) = (x - 2)^2 = 0$, where $f(x) \ge 0$ everywhere and no sign-change bracket exists? During Phase 1, the guarded secant contraction detects the stationary minimum when $|b - a| < 10^{-12}$ and $|f(b)| < 10^{-7}$ (or immediately if $|f(b)| \le 10^{-13}$) and returns $x = 2.0$.

Similarly, when using `{{key:POLY}}`, at least one of the leading coefficients $A$ or $B$ must be non-zero; pressing `{{key:EXEC}}` when both $A = 0$ and $B = 0$ displays `A ≠ 0` (which clears non-destructively with `{{key:C}}`). Because unentered coefficients default to $0$, you can solve a quadratic equation $ax^2 + bx + c = 0$ either by keying $A = a, B = b, C = c$ before pressing `{{key:EXEC}}` ($D$ defaults to $0$, storing the two quadratic roots in variables `3` and `5`) or by keying $B = a, C = b, D = c$ to invoke the native quadratic fallback, while sparse cubics like $x^3 - 8 = 0$ require entering only $A$ and $D$.

### Interpreting the Stack After {{key:SOLVE}}: Roots, Poles, and Local Extrema

In the spirit of William Kahan's diagnostic solver architecture (introduced in the HP-34C and refined in Chapter 14 and Appendix B of the *HP-32SII Owner's Manual*), `{{key:SOLVE}}` never acts as an opaque black box. When root-finding terminates, the SC-32 populates the operational stack with a complete **three-register diagnostic audit** so you can immediately distinguish a true physical zero from an even-multiplicity tangent root or a discontinuous vertical asymptote (pole):

| Stack Register | Post-`{{key:SOLVE}}` Contents | Engineering Diagnostic Interpretation |
| :---: | :--- | :--- |
| **Register $X$** | **Converged Root Estimate ($x^*$)** | The final abscissa estimate where $f(x^*)$ crosses or touches zero, also written directly into the target solver variable. |
| **Register $Y$** | **Previous Bracket Iterate ($x_{\text{prev}}$)** | The companion bracket bound or prior secant/IQI iterate. When $\lvert X - Y \rvert \le 10^{-12}$, the bracket jaws have pinched tightly around $x^*$. (When called from a single seed in `STO` workflow, $Y$ retains the initial seed for immediate step inspection.) |
| **Register $Z$** | **Evaluated Function Residual ($f(x^*)$)** | The value of your residual expression evaluated at $x = x^*$. Inspect via `{{key:R↓}} {{key:R↓}}`: a true zero-crossing yields $\lvert Z \rvert \le 10^{-12}$. |

Inspecting those three registers after `{{key:SOLVE}}` finishes tells you the exact geometry of the root. At a **verified simple root** ($f(x^*) = 0,\; f'(x^*) \ne 0$), the bracket has contracted to machine precision ($X \approx Y$ within $10^{-12}$) and rolling down twice (`{{key:R↓}} {{key:R↓}}`) shows that the residual in Register $Z$ vanishes ($|Z| \le 10^{-12}$), confirming complete zero-pair cancellation between positive and negative terms. At an **even-multiplicity tangent root** such as $f(x) = (x - 2)^2 = 0$, the curve touches the horizontal axis without crossing it ($f(x) \ge 0$ everywhere), so no sign-change bracket exists; during Phase 1, the guarded secant contraction pinches onto the vertex and terminates when the step width satisfies $|b - a| < 10^{-12}$ and the residual in Register $Z$ satisfies $|Z| < 10^{-7}$ (typically $\sim 10^{-12}$ to $10^{-8}$ because squaring a perturbation of size $10^{-6}$ already reaches $10^{-12}$).

What if your initial bracket accidentally straddles a **discontinuous pole or vertical asymptote**, such as $\tan x$ at $x = \pi/2$ or $f(x) = \frac{1}{x - 2}$? Because $f(a)$ is large and negative ($-\infty$) on one side of the odd-order pole while $f(b)$ is large and positive ($+\infty$) on the other, $f(a) \cdot f(b) < 0$ is satisfied and bisection repeatedly halves the interval toward the singularity until $X$ and $Y$ pinch together on opposite sides of the asymptote. Rolling the stack down twice (`{{key:R↓}} {{key:R↓}}`) to inspect Register $Z$ immediately exposes the impostor: instead of $Z \approx 0$, **Register $Z$ holds an enormous residual ($|Z| \gg 1$, often $10^{11}$ or larger)**. Finally, when a nonlinear equation possesses multiple physical branches—such as the subsonic diffuser root ($M_{\text{sub}} < 1$) and supersonic exhaust root ($M_{\text{sup}} > 1$) of Stodola's de Laval nozzle equation later in this chapter, or the tranquil versus rapid alternate depths of a hydraulic weir—you can use **two-guess directed bracketing** to steer `{{key:SOLVE}}` into the exact branch you want by placing the **lower guess $a$ in Register $Y$** and the **upper guess $b$ in Register $X$** (or seeding the target variable directly inside the desired basin of attraction) before pressing `{{key:SOLVE}}`.

---

## Solving Implicit Fluid, Thermodynamic, and Orbital Equations in Hardware

Now let us apply `{{key:SOLVE}}`, `{{key:POLY}}`, and T-register Horner evaluation to implicit hydraulic friction, orbital anomalies, real-gas isotherms, structural stress eigenvalues, and compressible nozzle flow.

### Implicit Transport Equations & Transcendental Root-Finding

With both Cardano's closed-form polynomial engine (`{{key:POLY}}`) and Brent's bracketed root-finder (`{{key:SOLVE}}`) in hand, we can tackle the classic implicit correlations of fluid transport, orbital mechanics, and thermodynamics—equations where the physical quantity we seek appears entangled on both sides of a logarithm, a trigonometric sine, or a cubic equation of state.

Consider fluid flowing through a rough commercial steel pipe at Reynolds number $\text{Re} = 100,000$ and relative roughness $\varepsilon/D = 0.001$. Why can't the pipe's Darcy-Weisbach friction factor $f$ be isolated explicitly with ordinary algebra? Even inside a violently turbulent pipe at $\text{Re} = 100,000$, fluid right against the steel wall is brought to a complete halt by the no-slip boundary condition, forming a paper-thin **viscous laminar sublayer** whose thickness scales inversely with wall shear ($\delta_v \propto D / (\text{Re}\sqrt{f})$). When flow is slow, this laminar cushion covers the microscopic cast-iron or steel roughness bumps ($\varepsilon/D = 0.001$), and friction depends only on viscosity ($\text{Re}\sqrt{f}$); when flow speeds up, the sublayer thins until the roughness peaks poke through like mountain ranges into the core flow, shedding turbulent eddies that depend on $\varepsilon/D$. Because the thickness of the laminar blanket itself depends on the friction factor $\sqrt{f}$ it is trying to shield, viscous shear and form drag are coupled on both sides of the logarithm inside Cyril Colebrook and Cedric White's (1937) implicit logarithmic law—the analytic foundation of the Moody chart:
$$\frac{1}{\sqrt{f}} = -2.0 \log_{10}\left(\frac{\varepsilon/D}{3.7} + \frac{2.51}{\text{Re}\sqrt{f}}\right) \implies f(F) = \frac{1}{\sqrt{F}} + 2.0 \log_{10}\left(\frac{0.001}{3.7} + \frac{2.51}{100000\sqrt{F}}\right) = 0$$

Entering the residual expression into `{{key:EQN}}` under label `COLE` as `F {{key:√x}} {{key:1/x}}  0.001 {{key:ENTER}} 3.7 {{key:÷}}  2.51 {{key:ENTER}} 100000 {{key:÷}} F {{key:√x}} {{key:÷}} {{key:+}} {{key:LOG}} 2 {{key:×}} {{key:+}}` and seeding the typical fully rough Moody plateau $F = 0.02$ before invoking `{{key:SOLVE}} F` converges rapidly:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0.02 {{key:STO}} F` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0200$ | Initial guess loaded |
| 2 | `{{key:SOLVE}} F` | $0.0000$ | $0.0000$ | $0.0200$ | **$0.022204$** | Darcy friction factor $f$ |

The stack resolves to **$f = 0.022204$** ($2.22 \times 10^{-2}$), with the initial seed $0.0200$ retained in Register $Y$ for immediate convergence inspection.

A similar self-referential coupling arises in orbital mechanics when an Earth observation satellite follows an elliptical orbit of eccentricity $e = 0.25$ and has swept out a mean anomaly $M = 1.20\text{ rad}$ since periapsis. Because angular momentum $h = r^2 \dot{\nu}$ is conserved under Kepler's Second Law, time elapsed since periapsis is proportional to swept elliptical sector area rather than central angle, yielding Johannes Kepler's (1609) famous transcendental equation relating mean anomaly $M$ to eccentric anomaly $E$:
$$f(E) = E - e \sin E - M = E - 0.25 \sin E - 1.20 = 0$$
With the angular baseline set to `{{key:RAD}}` and the residual `E  0.25 {{key:ENTER}} E {{key:SIN}} {{key:×}} {{key:-}} 1.20 {{key:-}}` loaded into `{{key:EQN}}`, seeding $E_0 = M = 1.20$ drives Brent's solver straight to the eccentric anomaly:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1.20 {{key:STO}} E` | $0.0000$ | $0.0000$ | $0.0000$ | $1.2000$ | Initial estimate $E_0 = M$ |
| 2 | `{{key:SOLVE}} E` | $0.0000$ | $0.0000$ | $1.2000$ | **$1.488665$** | Eccentric anomaly $E$ in radians |

Register $X$ settles at **$E = 1.488665\text{ radians}$** ($85.294^\circ$), exceeding $M$ by $e\sin E = 0.288665\text{ rad}$ because the satellite moves faster than its mean angular rate near periapsis.

When an implicit state equation can be cleared of fractions into a cubic polynomial, we have the luxury of choosing between `{{key:POLY}}` and `{{key:SOLVE}}`. Suppose carbon dioxide gas ($a = 3.59\text{ L}^2\cdot\text{atm/mol}^2, b = 0.0427\text{ L/mol}$) is compressed to temperature $T = 300\text{ K}$ and pressure $P = 50.0\text{ atm}$ ($R = 0.08206\text{ L}\cdot\text{atm/(mol}\cdot\text{K)}$). Near the critical isotherm ($T_c \approx 304.1\text{ K}$ for $\text{CO}_2$), intermolecular London dispersion attractions ($a/V^2$) and finite hard-sphere excluded volume ($b$) cause severe deviation from the ideal gas law ($V_{\text{ideal}} = RT/P = 0.4924\text{ L/mol}$), expanding Johannes Diderik van der Waals's equation of state into a cubic polynomial in molar volume $V$:
$$\left(P + \frac{a}{V^2}\right)(V - b) = R T \implies P V^3 - (P b + R T) V^2 + a V - a b = 0$$
Substituting the physical constants gives the cubic coefficients $A = P = 50.0$, $B = -(P b + R T) = -(50 \times 0.0427 + 0.08206 \times 300) = -(2.135 + 24.618) = -26.753$, $C = a = 3.59$, and $D = -a b = -(3.59 \times 0.0427) = -0.153293$. Loading these coefficients into `{{key:POLY}}` via `{{res:sc32_07_polynomials_brent_solver_seq_09:keys}}` delivers **`{{res:sc32_07_polynomials_brent_solver_seq_09:value}}`**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `50 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $50.0000$ | Coefficient $A = 50.0$ |
| 2 | `26.753 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $50.0000$ | $-26.7530$ | Coefficient $B = -26.753$ |
| 3 | `3.59 {{key:C}}` | $0.0000$ | $50.0000$ | $-26.7530$ | $3.5900$ | Coefficient $C = 3.59$ |
| 4 | `0.153293 {{key:+/-}} {{key:D}}`| $50.0000$ | $-26.7530$ | $3.5900$ | $-0.153293$| Coefficient $D = -0.153293$ |
| 5 | `{{key:EXEC}}` | $50.0000$ | $-26.7530$ | **$0.358736$** | **$0.000000$** | Real root in $Y$, Imag in $X$ |
| 6 | `{{key:x⇄y}}` | $50.0000$ | $-26.7530$ | $0.000000$ | **$0.358736$** | Molar volume $V_m$ in Register $X$ |

This confirms a final value of **$V_m = 0.358736\text{ L/mol}$** (a compressibility factor $Z = PV_m / RT = 0.7286$, reflecting strong attractive clustering at $50\text{ atm}$). Notice how the closed-form **`{{key:POLY}}`** solver above extracts the root of the expanded cubic $50V^3 - 26.753V^2 + 3.59V - 0.153293 = 0$ analytically via Cardano's formula (`0.358736 L/mol`), whereas the numerical **`{{key:SOLVE}}`** engine lets you enter the raw physical Van der Waals balance $\left(50 + \frac{3.59}{V^2}\right)(V - 0.0427) - 24.618 = 0$ into `{{key:EQN}}` (`50 3.59 {{key:ENTER}} V {{key:x²}} {{key:÷}} {{key:+}} V 0.0427 {{key:-}} {{key:×}} 24.618 {{key:-}}`) without multiplying out a single coefficient—converging from `0.49 {{key:STO}} V {{key:SOLVE}} V` to the identical **$V_m = 0.358736\text{ L/mol}$**.

Returning to genuinely transcendental equations where polynomial expansion is impossible, consider a silicon $p\text{-}n$ junction diode sitting in series with load resistor $R = 1,000\,\Omega$ and DC bias source $V_s = 5.0\text{ V}$, with reverse saturation current $I_s = 10^{-12}\text{ A}$ and room-temperature thermal voltage $V_T = k_B T / q = 0.02585\text{ V}$. Because Kirchhoff's linear load line $I = (V_s - V)/R$ intersects William Shockley's exponential minority-carrier injection law $I = I_s(e^{V/V_T} - 1)$, the quiescent operating voltage $V_D$ is governed by an implicit transcendental equation:
$$f(V) = 5.0 - 1000 \times 10^{-12} (e^{V / 0.02585} - 1) - V = 0$$

With this residual stored in `{{key:EQN}}` under label `DIODE` and seeded at the standard silicon forward turn-on knee of $0.65\text{ V}$, `{{key:SOLVE}}` pinpoints the exact intersection of the linear resistor and exponential junction:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0.65 {{key:STO}} V` | $0.0000$ | $0.0000$ | $0.0000$ | $0.6500$ | Initial estimate loaded |
| 2 | `{{key:SOLVE}} V` | $0.0000$ | $0.0000$ | $0.6500$ | **$0.672944$** | Diode forward voltage $V_D$ |

The calculation yields **$V_D = 0.672944\text{ Volts}$** (quiescent loop current $I_D = (5.0 - 0.672944)/1000 = 4.327\text{ mA}$).

Even high-degree algebraic equations are often cleaner to solve directly in their unexpanded physical form via `{{key:SOLVE}}`. Take a trapezoidal hydraulic spillway channel of bottom width $b = 3.0\text{ m}$ and side-slope ratio $z = 2.0\text{ (H:V)}$ carrying volumetric discharge $Q = 20.0\text{ m}^3/\text{s}$. Specific energy $E = y + \frac{Q^2}{2gA(y)^2}$ reaches its minimum—and the Froude number $\text{Fr} = \frac{Q\sqrt{T(y)}}{\sqrt{g A(y)^3}}$ passes through unity between tranquil subcritical and rapid supercritical flow—when top width $T(y) = b + 2zy = 3 + 4y$ and wetted cross-sectional area $A(y) = by + zy^2 = 3y + 2y^2$ satisfy the critical-flow condition:

$$\frac{Q^2 T}{g A^3} = 1 \implies 400(3 + 4 y) - 9.81 (3y + 2y^2)^3 = 0$$

Entering that unexpanded balance into `{{key:EQN}}` and seeding an initial depth estimate of $y = 1.0\text{ m}$ locates the critical flow depth without expanding a sixth-degree polynomial:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1.0 {{key:STO}} Y` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Initial depth estimate |
| 2 | `{{key:SOLVE}} Y` | $0.0000$ | $0.0000$ | $1.0000$ | **$1.258641$** | Critical flow depth $y_c$ |

The stack resolves to **$y_c = 1.258641\text{ meters}$**. Why is the Froude number $\text{Fr} = v / \sqrt{g D_h} = 1$ (where hydraulic depth $D_h = A/T$, or $y$ in a wide rectangular channel) the exact tipping point of open-channel hydraulics? Because $c = \sqrt{g D_h}$ is the **propagation speed of a shallow-water gravity wave**. Just as Mach $1$ ($M = v/c_{\text{sound}} = 1$) marks the sonic barrier where air flows faster than pressure waves can propagate upstream, $\text{Fr} = 1$ ($y = y_c = 1.2586\text{ m}$) is the critical depth where water velocity $v = Q/A$ matches the surface wave speed $c = \sqrt{g A / T}$. Upstream of a spillway where $y > y_c$ ($\text{Fr} < 1$, tranquil subcritical flow), surface ripples can travel upstream to warn approaching water of an obstacle; down the chute where $y < y_c$ ($\text{Fr} > 1$, rapid supercritical flow), ripples are swept downstream, and the flow can only decelerate back to tranquil depth through a standing shock wave—a **turbulent hydraulic jump**.

When our governing equation is a third-order linear differential system or a quadratic ballistic trajectory, `{{key:POLY}}` gives us all roots simultaneously so we can inspect repeated poles or alternate physical trajectories. Suppose a third-order linear passive RLC filter network has the Laplace-domain characteristic denominator polynomial:

$$s^3 + 12 s^2 + 45 s + 50 = 0$$

Analytical factorization yields $(s + 2)(s + 5)^2 = 0$, giving an isolated real pole at $s = -2\text{ Np/s}$ and a critically damped double pole at $s = -5\text{ Np/s}$ where the cubic discriminant $\Delta = 0$ sits precisely on the boundary between overdamped real poles and underdamped complex conjugate oscillations. Inside `{{key:POLY}}`, keying `{{res:sc32_07_polynomials_brent_solver_seq_10:keys}}` loads the leading cubic and quadratic coefficients via `1 {{key:A}} 12 {{key:B}}` ($Y = 1.0000,\; X = 12.0000$) and the linear and constant terms via `45 {{key:C}} 50 {{key:D}}` ($Y = 45.0000,\; X = 50.0000$). Pressing `{{key:EXEC}}` evaluates Cardano's closed-form roots, returning **`{{res:sc32_07_polynomials_brent_solver_seq_10:value}}`** as the first sorted real root in $(Y, X)$ ($Y = \mathbf{-5.000000},\; X = \mathbf{0.000000}$) and storing all three real poles ($s_1 = -5.0, s_2 = -5.0, s_3 = -2.0$) in variables `1`, `3`, and `5`.

Similarly, when an artillery battery must strike an elevated ridge target at horizontal range $x = 1,200\text{ m}$ and elevation $y = 150\text{ m}$ with muzzle velocity $v_0 = 140\text{ m/s}$, substituting the trigonometric identity $\sec^2\theta = 1 + \tan^2\theta$ into the parabolic ballistic trajectory eliminates time of flight and transforms the launch slope $u = \tan\theta$ into the classic Tartaglia-Galileo ballistic quadratic:

$$y = x \tan\theta - \frac{g x^2}{2 v_0^2} (1 + \tan^2\theta) \implies 360.3673 u^2 - 1200 u + 510.3673 = 0 \quad (\text{where } u = \tan\theta)$$

Solving this quadratic in `{{key:POLY}}` and converting the slope roots via `{{key:ATAN}}` with `{{res:sc32_07_polynomials_brent_solver_seq_02:keys}}` yields **`{{res:sc32_07_polynomials_brent_solver_seq_02:value}}`**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `360.3673 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $360.3673$ | Quadratic coefficient $A$ |
| 2 | `1200 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $360.3673$ | $-1200.0000$ | Quadratic coefficient $B$ |
| 3 | `510.3673 {{key:C}}` | $0.0000$ | $360.3673$ | $-1200.0000$ | $510.3673$ | Quadratic coefficient $C$ |
| 4 | `0 {{key:D}}` | $360.3673$ | $-1200.0000$ | $510.3673$ | $0.0000$ | Depressed constant (optional; $D$ defaults to $0.0$ if omitted) |
| 5 | `{{key:EXEC}}` | $360.3673$ | $-1200.0000$ | $0.0000$ | $0.0000$ | Roots stored in Regs 1, 3, 5 ($0, u_1, u_2$) |
| 6 | `{{key:RCL}} 3 {{key:ATAN}}` | $-1200.0000$ | $0.0000$ | $0.0000$ | **$26.590116$** | Low direct-fire trajectory $\theta_1$ in degrees |
| 7 | `{{key:RCL}} 5 {{key:ATAN}}` | $0.0000$ | $0.0000$ | $26.590116$ | **$70.532306$** | High plunging mortar arc $\theta_2$ in degrees |

Because unentered coefficients in `{{key:POLY}}` default to $0.0$, Step 4 can be skipped entirely—keying `360.3673 {{key:A}} 1200 {{key:+/-}} {{key:B}} 510.3673 {{key:C}} {{key:EXEC}}` directly solves the quadratic, confirming **$\theta_1 = 26.59^\circ$** (flat direct trajectory) and **$\theta_2 = 70.53^\circ$** (high plunging mortar trajectory).

---

### Characteristic Polynomials, Principal Stresses & Stability Poles

This ability of `{{key:POLY}}` to deliver all three roots of a cubic in sorted order shines brightest when every root has an independent physical meaning—as in 3D continuum mechanics and hydrostatics.

Consider a structural steel element subjected to a 3D Cauchy stress tensor (in $\text{MPa}$) with normal components $\sigma_{xx} = 40, \sigma_{yy} = 20, \sigma_{zz} = 10$ and in-plane shear $\tau_{xy} = 15$ ($\tau_{yz} = \tau_{xz} = 0$). Setting the characteristic determinant $\det(\boldsymbol{\sigma} - \lambda \mathbf{I}) = 0$ expresses the principal stresses via the three coordinate-frame stress invariants $I_1 = \text{tr}(\boldsymbol{\sigma}) = 70\text{ MPa}$, $I_2 = 1175\text{ MPa}^2$, and $I_3 = \det(\boldsymbol{\sigma}) = 5750\text{ MPa}^3$:

$$\det(\boldsymbol{\sigma} - \lambda \mathbf{I}) = (10 - \lambda)[(40 - \lambda)(20 - \lambda) - 225] = 0 \implies \lambda^3 - 70 \lambda^2 + 1175 \lambda - 5750 = 0$$

Entering these invariants into `{{key:POLY}}` via `{{res:sc32_07_polynomials_brent_solver_seq_12:keys}}` returns **`{{res:sc32_07_polynomials_brent_solver_seq_12:value}}`**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1 {{key:A}} 70 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-70.0000$ | Coefficients $A, B = -I_1$ |
| 2 | `1175 {{key:C}} 5750 {{key:+/-}} {{key:D}}` | $1.0000$ | $-70.0000$ | $1175.0000$ | $-5750.0000$| Coefficients $C = I_2, D = -I_3$ |
| 3 | `{{key:EXEC}}` | $1.0000$ | $-70.0000$ | **$10.000000$** | **$0.000000$** | Minor stress $\sigma_3 = 10.0$ in $Y$; $\sigma_2, \sigma_1$ in vars `3`, `5` |
| 4 | `{{key:RCL}} 5` | $-70.0000$ | $10.0000$ | $0.0000$ | **$48.027756$** | Recall major principal stress $\sigma_1$ into Register $X$ |

This confirms all three ordered principal stresses: **$\sigma_1 = 48.03\text{ MPa}$**, **$\sigma_2 = 11.97\text{ MPa}$**, and **$\sigma_3 = 10.00\text{ MPa}$** (satisfying $\sigma_1 + \sigma_2 + \sigma_3 = I_1 = 70.00\text{ MPa}$).

A depressed-linear cubic arises just as naturally when a solid oak marine buoy sphere of radius $R = 0.50\text{ m}$ and density $\rho_s = 650\text{ kg/m}^3$ floats in freshwater ($\rho_w = 1000\text{ kg/m}^3$). By Archimedes' principle (*On Floating Bodies*), equating the submerged spherical cap volume $V_{\text{cap}}(h) = \frac{\pi h^2}{3}(3R - h)$ to the displaced water volume $\frac{\rho_s}{\rho_w} \left(\frac{4}{3}\pi R^3\right)$ yields a cubic polynomial for the equilibrium draft $h$:
$$h^3 - 3R h^2 + 4 \frac{\rho_s}{\rho_w} R^3 = 0 \implies h^3 - 1.5 h^2 + 0.325 = 0$$

Solving this cubic in `{{key:POLY}}` with `{{res:sc32_07_polynomials_brent_solver_seq_13:keys}}` produces **`{{res:sc32_07_polynomials_brent_solver_seq_13:value}}`**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1 {{key:A}} 1.5 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-1.5000$ | Coefficients $A, B$ |
| 2 | `0 {{key:C}} 0.325 {{key:D}}` | $1.0000$ | $-1.5000$ | $0.0000$ | $0.3250$ | Coefficients $C, D$ (or omit $C$; omitted terms default to $0$) |
| 3 | `{{key:EXEC}}` | $1.0000$ | $-1.5000$ | $-0.412257$ | $0.0000$ | Roots stored in Regs 1, 3, 5 |
| 4 | `{{key:RCL}} 3` | $-1.5000$ | $-0.412257$ | $0.0000$ | **$0.601390$** | Physical immersion depth in $[0, 2R]$ |

The middle root in variable `3` gives the physical immersion depth **$h = 0.601390\text{ meters}$** ($60.14\%$ of the $1.00\text{ m}$ diameter, whereas the negative root $-0.4123\text{ m}$ and super-diameter root $1.3109\text{ m}$ lie outside the physical cap domain $0 \le h \le 1.0\text{ m}$).

---

### Chemical Equilibria, Critical Buckling & Economic Optima

We can also pair `{{key:EQN}}` root-finding with T-register stack replication to solve eigenvalue boundary conditions and rational device approximations. For an unreflected bare spherical thermal fission reactor core with critical geometric buckling $B_{\text{crit}} = 0.045\text{ cm}^{-1}$ (where material buckling $B_m^2 = (\nu\Sigma_f - \Sigma_a)/D$ equals geometric buckling $B_g^2$), solving the Helmholtz one-group neutron diffusion equation $\nabla^2\phi + B_{\text{crit}}^2\phi = 0$ yields the radial flux eigenmode $\phi(r) = \Phi_0 \frac{\sin(B_{\text{crit}} r)}{r}$, which vanishes at the extrapolated critical radius $R_{\text{crit}}$ where $\sin(0.045 R) = 0$:
$$f(R) = \sin(0.045 R) = 0 \implies R_{\text{crit}} = \frac{\pi}{0.045} \approx \mathbf{69.813170\text{ cm}}$$

In `{{key:RAD}}` mode, storing `R 0.045 {{key:×}} {{key:SIN}}` inside `{{key:EQN}}`, seeding the initial radius estimate $R_0 = 60.0\text{ cm}$ near the first non-trivial zero (`R > 0`) via `60 {{key:STO}} R`, and executing `{{key:SOLVE}} R` isolates the critical core radius ($Y = 60.0000,\; X = \mathbf{69.813170}\text{ cm}$), or **$R_{\text{crit}} = 69.81\text{ cm}$**.

When an implicit transcendental root is needed repeatedly in field design, engineers often construct rational polynomial-logarithmic approximations that can be evaluated in a single pass with T-register replication. Building from our earlier Shockley diode operating point ($V_{\text{oc}} = 0.65\text{ V}, V_T = 0.02585\text{ V}$, normalized open-circuit voltage $v_{\text{oc}} = \frac{V_{\text{oc}}}{V_T} = \frac{0.65}{0.02585} = 25.145$), Martin Green's (1982) semi-empirical rational formula approximates the transcendental maximum-power-point root $v_{\text{mp}} + \ln(1 + v_{\text{mp}}) = v_{\text{oc}}$ to yield the photovoltaic cell fill factor $FF = \frac{V_{\text{mp}} I_{\text{mp}}}{V_{\text{oc}} I_{\text{sc}}}$:
$$\text{Fill Factor } FF = \frac{v_{\text{oc}} - \ln(v_{\text{oc}} + 0.72)}{v_{\text{oc}} + 1} = \frac{25.145 - \ln(25.865)}{26.145} = \frac{25.145 - 3.2529}{26.145} = \mathbf{0.8373}$$

Because $v_{\text{oc}} = 25.145$ appears in three distinct sub-expressions, we flood the 4-level stack via `25.145 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}` so `25.145` is typed only **once**. Next, `0.72 {{key:+}} {{key:LN}} {{key:-}}` adds $0.72$, takes the natural logarithm $\ln(25.865) \approx 3.2529$, and subtracts it from the copy of $v_{\text{oc}}$ waiting in Register $Y$ while Register $T$ continually replenishes $25.1450$ downward ($X = 21.8921$). Finally, `{{key:x⇄y}} 1 {{key:+}} {{key:÷}}` swaps the fresh copy of $v_{\text{oc}}$ from $Y$ into $X$, adds $1$ to form the denominator $26.145$, and divides in place to resolve the solar cell fill factor ($X = \mathbf{0.837334}$), or **$FF = 0.8373$** ($83.73\%$). *(You can equally avoid re-entry via `{{key:LASTX}}` by keying `0.72 {{key:ENTER}} 25.145 {{key:+}} {{key:LASTX}} {{key:x⇄y}} {{key:LN}} {{key:-}}` and dividing by $v_{\text{oc}} + 1$.)*

---

### Geotechnical, Compressible Flow & Orbital Solver Applications

Our closing sequence brings together Rankine earth-pressure quadratics, supersonic de Laval nozzle branch selection, and biquadratic normal-mode extraction on the raw stack.

For cohesionless granular backfill with internal friction angle $\phi = 32.0^\circ$ ($2\tan 32^\circ = 1.249739$) behind a smooth retaining wall, William J. M. Rankine's (1857) plastic limit equilibrium requires Mohr's stress circle to touch the Coulomb failure envelope $\tau = \sigma\tan\phi$. Expressing the conjugate failure-plane inclination tangent $u = \tan(45^\circ - \phi/2) = \sqrt{K_a}$ via the double-angle tangent identity yields a monic quadratic equation:
$$u^2 + (2\tan\phi) u - 1 = 0 \implies u^2 + 1.249739 u - 1 = 0 \implies K_a = u^2 = \mathbf{0.307259}$$

In `{{key:POLY}}`, `1 {{key:A}} 1.249739 {{key:B}}` loads $A = 1.0$ and the frictional coupling $B = 2\tan(32^\circ) = 1.249739$, while `1 {{key:+/-}} {{key:C}} {{key:EXEC}}` sets $C = -1.0$ and extracts the roots ($Y = -1.8040,\; X = 0.0000$). Just as completing the square on the **$90^\circ$ L-Frame Factoring Stage** writes $(u + \tan\phi)^2 = 1 + \tan^2\phi = \sec^2\phi$, `{{key:RCL}} 5 {{key:x²}}` recalls the positive slip-angle tangent $u = \sec\phi - \tan\phi = \tan(29^\circ) = 0.554309$ and squares it in place to obtain the Rankine active earth pressure coefficient ($X = \mathbf{0.307258}$), yielding **$K_a = 0.307259$** (while squaring the negative root $-1.804048 = -\tan(61^\circ)$ in variable 1 directly yields the passive earth pressure coefficient $K_p = 1/K_a = 3.254587$).

What happens when an implicit conservation law has two distinct physical branches on opposite sides of a sonic throat? For isentropic air flow ($\gamma = 1.4$, critical sonic throat pressure ratio $\frac{P^*}{P_0} = \left(\frac{2}{\gamma+1}\right)^{\gamma/(\gamma-1)} = 0.528282$) expanding through a converging-diverging de Laval rocket nozzle with exit-to-throat area ratio $\frac{A}{A^*} = 2.50$, the exit Mach number $M$ satisfies the implicit Stodola Area-Mach relation—which possesses both a subsonic diffuser branch ($M_{\text{sub}} \approx 0.2395$) and a supersonic rocket-exhaust branch ($M_{\text{sup}} > 1$):
$$f(M) = \frac{1}{M}\left(\frac{1 + 0.2 M^2}{1.2}\right)^3 - 2.50 = 0 \implies M_{\text{sup}} = \mathbf{2.442804}$$

With `M {{key:x²}} 0.2 {{key:×}} 1 {{key:+}} 1.2 {{key:÷}} 3 {{key:yˣ}} M {{key:÷}} 2.50 {{key:-}}` entered into `{{key:EQN}}`, seeding the initial estimate $M_0 = 2.50$ on the supersonic side of the sonic throat minimum ($M = 1.0$) via `2.5 {{key:STO}} M` and pressing `{{key:SOLVE}} M` isolates the supersonic exit Mach number ($Y = 2.5000,\; X = \mathbf{2.442804}$) in Register $X$.

Finally, when two coupled undamped spring-mass oscillators or an LC ladder filter vibrate in their natural normal modes, the eigenvalue determinant $\det(\mathbf{K} - x^2 \mathbf{M}) = 0$ contains only squared frequencies $u = x^2$, producing an even **biquadratic characteristic polynomial** such as $x^4 - 10 x^2 + 9 = 0$:

$$u = x^2 \implies u^2 - 10 u + 9 = 0 \implies (u - 1)(u - 9) = 0 \implies u = 1, 9 \implies x = \mathbf{1.0, 3.0}$$

Instead of calling a menu solver, you can extract both positive biquadratic roots simultaneously on the main stack by evaluating the quadratic numerator branches $10 \pm \sqrt{\Delta}$ with `{{key:LASTX}}` so the discriminant radical $\sqrt{\Delta} = 8.0000$ is never re-typed. First, `10 {{key:x²}} 4 {{key:ENTER}} 9 {{key:×}} {{key:-}} {{key:√x}}` evaluates the discriminant radical $\sqrt{\Delta} = \sqrt{100 - 36} = 8.0000$ in Register $X$. Next, `10 {{key:x⇄y}} {{key:+}}` forms the upper numerator $10 + 8 = 18.0000$ in Register $X$ while automatically preserving $\sqrt{\Delta} = 8.0000$ inside `LASTX`. Recalling `{{key:LASTX}} 10 {{key:x⇄y}} {{key:-}}` brings $\sqrt{\Delta} = 8.0000$ back from `LASTX` (lifting $18.0000$ into $Y$) and forms the lower numerator $10 - 8 = 2.0000$ in Register $X$. Then `2 {{key:÷}} {{key:√x}}` halves $2.0000$ to $u_2 = 1.0000$ and extracts the square root to place the fundamental mode $x_2 = 1.0000$ in Register $X$. Finally, `{{key:x⇄y}} 2 {{key:÷}} {{key:√x}}` swaps $18.0000$ into $X$, halves to $u_1 = 9.0000$, and extracts the square root, leaving both positive biquadratic roots side by side on the stack ($Y = \mathbf{1.0000},\; X = \mathbf{3.0000}$) for **$x_1 = 3.0$** and **$x_2 = 1.0$** with zero manual re-entry.

---

## Further Exploration: Companion Workbooks & Applied Tie-Ins

> *For 26 additional worked engineering problems with full 4-register stack traces, see Chapter 7 of the [SC-32 Scientific Companion Problem & Casebook Workbook](../../curriculum/sc32-scientific-companion-workbook.md).*


To push the SC-32's closed-form Cardano/Viète cubic engine (`{{key:POLY}}`), T-register Horner streams, and Richard Brent's hybrid bracketed solver (`{{key:SOLVE}}`) further across fluid mechanics, thermodynamics, and astrodynamics, explore these three synthesis challenges:

### Synthesis Challenge Problems

1. **T-Register Simultaneous Horner Evaluation of $P(x)$ and $P'(x)$**:
   For any cubic $P(x) = a_3 x^3 + a_2 x^2 + a_1 x + a_0$, verify how flooding $x$ across the stack with `x {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}` evaluates $P(x)$ in exactly $3$ multiplies and $3$ additions without ever re-typing $x$ or touching memory registers `0`–`9`. Compare your Horner residual at the double root $x = -5$ of the RLC circuit characteristic polynomial ($s^3 + 12s^2 + 45s + 50 = 0$) against naive term-by-term power evaluation (`{{key:yˣ}}`) to observe how nested synthetic division suppresses floating-point cancellation near multiple roots.
2. **Subsonic vs. Supersonic Compressible Flow Branches in `SOLVE`**:
   Re-run the Stodola de Laval nozzle Area-Mach equation ($A/A^* = 2.50$) with an initial subsonic seed `0.2 {{key:STO}} M {{key:SOLVE}} M` instead of `2.5 {{key:STO}} M`. Verify that Brent's solver converges cleanly to the subsonic venturi-diffuser root **$M_{\text{sub}} = 0.239541$**, demonstrating how your initial seed steers `{{key:SOLVE}}` across the sonic throat extremum at $M = 1.0$.
3. **Redlich-Kwong vs. Van der Waals Supercritical Compressibility**:
   Using the cubic `{{key:POLY}}` workflow from the Van der Waals real-gas analysis above, compare the molar volume of $\text{CO}_2$ at $T = 300\text{ K}, P = 50\text{ atm}$ ($V_m = 0.358736\text{ L/mol}$) against the lower-pressure regime $P = 10\text{ atm}$, and observe how the cubic discriminant transitions from a single real supercritical/gas root ($\Delta > 0$) to three real roots ($\Delta < 0$, liquid, metastable, and vapor) when cooled below the critical point.

---

## Summary & Looking Ahead

Chapter 7 bridged classical polynomial theory and modern numerical analysis. By chaining synthetic division and Horner's nested polynomial stream through the stack, you evaluated high-order polynomials with minimal keystrokes. You extracted real and complex roots of quadratics and cubics via the hardware polynomial solver (`{{key:POLY}}`), and conquered transcendental equations—from pipe friction factors to transcendental orbital anomalies—using Richard Brent's root finder (`{{key:SOLVE}}`) with guaranteed bracket convergence to $10^{-12}$ accuracy.

Root-finding answers where a function crosses zero, but continuous physical models also require measuring rates of change and accumulating continuous quantities. In **[Chapter 8: Calculus, Numerical Derivatives & Romberg Quadrature](08-calculus-romberg-quadrature.md)**, you will take the step into infinitesimal analysis. You will use the SC-32's Romberg integration engine (`{{key:∫}}`) and Richardson extrapolation to evaluate definite integrals, compute variable rocket motor impulses, and calculate numerical derivatives.

