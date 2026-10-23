---
title: "Chapter 5: Complex Numbers, AC Phasors & Euler's Identity | SC-32 Manual"
description: "Master the classic (Y, X) complex plane convention, [CMPLX] prefix evaluator, live proof of Euler's Identity, AC circuit impedance phasors, RF transmission line reflections, and Smith chart coordinates on the StackCalc SC-32."
---

# Chapter 5: Complex Numbers, AC Phasors & Euler's Identity

## Steinmetz's AC Phasors & The Geometry of $\sqrt{-1}$

In August 1893, at the International Electrical Congress held during the Chicago World's Columbian Exposition, German-American mathematician and electrical engineer **Charles Proteus Steinmetz** stunned the assembly with a landmark paper, *"Complex Quantities and Their Use in Electrical Engineering"* {{cite:steinmetz1893}}, proving that the imaginary unit $i = \sqrt{-1}$ (written $j$ in electrical engineering to avoid confusion with current $i$) is a physical $90^\circ$ counterclockwise rotation operator that turns differential equations into simple complex arithmetic.

At the height of the 1890s "War of the Currents," Thomas Edison's direct-current (DC) generating stations could transmit power barely a mile before copper resistance dissipated electrical energy into ambient heat, whereas Nikola Tesla and George Westinghouse's alternating current (AC) used high-voltage step-up transformers to carry megawatts across hundreds of miles with minimal loss. Yet AC networks posed a formidable mathematical barrier: inductors resist changes in current, dragging the current wave $90^\circ$ behind voltage, while capacitors resist changes in voltage, advancing current $90^\circ$ ahead. Calculating currents and node voltages across even a modest network of coils and capacitor banks forced electrical pioneers to solve coupled second-order differential equations:

$$L \frac{d^2 q}{dt^2} + R \frac{dq}{dt} + \frac{1}{C} q = V_0 \sin(\omega t + \phi)$$

Steinmetz demonstrated that any steady-state sinusoidal waveform $v(t) = V_0 \cos(\omega t + \theta)$ can be represented algebraically as a complex phasor—the horizontal projection of a two-dimensional vector rotating at angular frequency $\omega$ in the complex plane. By casting ohmic resistance along the real axis and reactive impedance along the orthogonal imaginary axis:

$$\mathbf{Z} = R + j(X_L - X_C) = R + j\left(\omega L - \frac{1}{\omega C}\right)$$

Steinmetz eliminated differential calculus from steady-state AC circuit analysis. Ohm's law became complex multiplication ($\mathbf{V} = \mathbf{I} \cdot \mathbf{Z}$), and Kirchhoff's loop and node laws became complex addition ($\sum \mathbf{V} = 0$).

On the StackCalc SC-32, Steinmetz's phasor geometry maps directly onto the operational stack:
* **Register $Y$** holds the Real component $\operatorname{Re}(\mathbf{Z})$.
* **Register $X$** holds the Imaginary component $\operatorname{Im}(\mathbf{Z})$.

Press `{{key:CMPLX}} {{key:+}}`, and the SC-32 evaluates full 2D vector phasor addition in microseconds. Unless a problem specifies degrees (`{{key:DEG}}`) for an electrical or RF phase angle, angular-frequency and Euler-identity sequences in this chapter assume radian mode (`{{key:RAD}}`).

---

{{res:sc32_phasor_polar:screenshot|Impedance phasor 3 + j4 rectangular-to-polar conversion → r = 5, theta = 53.1301 deg}}

## Phasor Geometry, Stack Registers, and the Complex Plane

In electrical, mechanical, and acoustic engineering, a complex number $\mathbf{z} = a + jb$ is a physical two-dimensional vector: horizontal resistance $R$ along the real axis coupled with inductive reactance $+j\omega L$ or capacitive reactance $-j/(\omega C)$ along the vertical quadrature axis.

### Why Multiplying by $i = \sqrt{-1}$ Is a Physical $90^\circ$ Rotation

Why does the square of the imaginary unit equal negative one ($i^2 = -1$)? If you only look at a one-dimensional number line, no positive or negative real number squared can ever land on $-1$. Consider instead the *Unit Circle Volvelle* and the four removable $90^\circ$ quadrant sectors of the *Planetary Geared Clock*:
1. **One $90^\circ$ Turn ($\times i$):** Point the Volvelle dial along the positive real axis at $0^\circ$ ($+1$). Multiplying by $i$ does not stretch or shrink the pointer—it physically **rotates the pointer $90^\circ$ ($\pi/2\text{ rad}$) counterclockwise** across the first quadrant sector of the *Planetary Geared Clock* to point straight up along the vertical imaginary axis ($0 + 1i$).
2. **Two $90^\circ$ Turns ($i \times i = -1$):** Rotate the Volvelle dial by a *second* $90^\circ$ quadrant ($90^\circ + 90^\circ = 180^\circ$, or $\pi\text{ rad}$). Where is the pointer aiming now? Straight left along the negative real axis at **$-1$**. That is why $i^2 = -1$: two $90^\circ$ quarter-turns make a $180^\circ$ half-turn reversal.
3. **Continuous Rotation & Euler's Identity ($e^{i\theta} = \cos\theta + i\sin\theta$):** Rotating a third $90^\circ$ quadrant reaches $270^\circ$ ($i^3 = -i$), and a fourth $90^\circ$ quadrant completes the $360^\circ$ circle ($i^4 = +1$). More generally, dialing the Volvelle through *any* continuous angle $\theta$ traces Leonhard Euler's 1748 formula $e^{i\theta} = \cos\theta + i\sin\theta$, projecting the horizontal real part $\cos\theta$ into Register $Y$ and the vertical imaginary part $\sin\theta$ into Register $X$.

On the StackCalc SC-32, this two-dimensional geometry maps directly onto the lower two registers of the operational stack. Register $Y$ (Line 2 of the transflective LCD) holds the real component $\operatorname{Re}(\mathbf{z})$, while Register $X$ (Line 1) holds the imaginary component $\operatorname{Im}(\mathbf{z})$. With the `{{key:CMPLX}}` prefix key, the 64-bit IEEE-754 engine treats the $(Y, X)$ register pair as a unified complex value—collapsing Euler's identity $e^{i\theta} = \cos\theta + i\sin\theta$, phasor impedances, and Smith Chart reflection coefficients $\mathbf{\Gamma} = (\mathbf{Z}_L - Z_0)/(\mathbf{Z}_L + Z_0)$ in a single keystroke.

### Automotive Shock Absorbers, Tuned Mass Dampers & $90^\circ$ Reactive Energy Exchange
Why do electrical circuits, automotive coil-over suspensions, and skyscraper tuned mass dampers all obey the exact same complex plane arithmetic? Because every oscillating physical system separates energy into two orthogonal channels corresponding to the horizontal and vertical axes of the *Unit Circle Volvelle*:
* **The Real Axis (Register $Y$ — Irreversible Heat Dissipation):** Resistance $R$ in an electrical circuit or viscous oil damping $c$ inside an **automotive hydraulic shock absorber** acts in phase with velocity ($0^\circ$). It permanently removes energy from the oscillation, converting electrical current or road-bump kinetic energy into irreversible thermal heat.
* **The Imaginary Axis (Register $X$ — $90^\circ$ Lossless Reactive Energy Exchange):** Multiplying by $j\omega$ rotates phase by $90^\circ$ on the *Unit Circle Volvelle* because velocity is $90^\circ$ ahead of displacement and acceleration is $90^\circ$ ahead of velocity. An inductor ($+j\omega L$) or moving mass ($+j\omega m$) stores kinetic/magnetic energy, while a capacitor ($-j/(\omega C)$) or coil spring ($-j k/\omega$) stores potential/electric energy at $-90^\circ$. Neither dissipates a single microwatt of heat; instead, reactive energy **exchanges losslessly back and forth** between kinetic and potential storage twice every cycle—and at resonance ($\omega_0 = 1/\sqrt{LC} = \sqrt{k/m}$), the $+j$ and $-j$ reactances cancel in Register $X$.

{{blocks:unit_circle_volvelle|Unit Circle Volvelle Complex Phasor Stage}}
*Figure 5.1: The Unit Circle Volvelle resolver translates angular phase rotation and orthogonal Cartesian projections directly into Register $Y$ (Real) and Register $X$ (Imaginary) inputs.*

### The Classic $(Y, X)$ Complex Plane Convention
Complex numbers on the StackCalc SC-32 adhere strictly to the classic **$(Y, X)$ rectangular Gaussian plane convention** established on legendary scientific RPN handhelds:

$$\mathbf{z} = Y + X i$$

| Register / Display | Complex Plane Component | Mathematical Notation | Display Appearance ($z = a + bi$) |
| :--- | :--- | :---: | :--- |
| **Register $Y$ (Line 2)** | Real Part | $\operatorname{Re}(\mathbf{z})$ | $a$ (Upper line on transflective LCD) |
| **Register $X$ (Line 1)** | Imaginary Part | $\operatorname{Im}(\mathbf{z})$ | $b$ (Active prompt line on transflective LCD) |

### Why $(Y, X)$?
This allocation provides three vital operational and mathematical advantages:
1. **Direct Coordinate Correspondence:** In standard Euclidean plane graphing, the horizontal coordinate is the abscissa ($x$ or real axis) and the vertical coordinate is the ordinate ($y$ or imaginary axis). On the physical two-line LCD display, Register $Y$ sits directly above Register $X$, creating an intuitive two-element column vector:
   $$\begin{bmatrix} Y \\ X \end{bmatrix} = \begin{bmatrix} \text{Real}(z) \\ \text{Imag}(z) \end{bmatrix}$$
2. **Polar Transformation Symmetry:** When converting between rectangular and polar forms ($z = r \angle \theta$) via `{{key:▸θ,r}}` and `{{key:▸y,x}}`, swapping Gaussian $(Y=\text{Real}, X=\text{Imag})$ via `{{key:x⇄y}}` aligns horizontal $x$ in Register $X$ and vertical $y$ in Register $Y$, producing phase angle $\theta = \operatorname{atan2}(Y, X)$ in Register $Y$ and magnitude $|z| = r = \operatorname{hypot}(X, Y)$ in Register $X$.
3. **Zero-Overhead Stack Inspection & Overflow-Safe Division:** Pressing `{{key:x⇄y}}` toggles between the real and imaginary parts instantly, allowing inspection of full 15-digit internal IEEE-754 precision without disturbing upper stack registers $Z$ and $T$. Internally, binary complex division (`{{key:CMPLX}} {{key:÷}}`) executes **Robert L. Smith's (1962) scaling algorithm**, pivoting on the ratio $r = d/c$ (when $|c| \ge |d|$) or $r = c/d$ (when $|d| > |c|$) so that $c^2 + d^2$ never suffers premature floating-point overflow or underflow.

---

## The {{key:CMPLX}} Prefix Evaluator Architecture

On many algebraic calculators, working with complex numbers requires switching the entire machine into a restricted "Complex Mode" that disables statistical and vector keys, and typing out parenthesized strings like `(20+15i)/(10-25i)` where a single missing bracket mixes real resistance with imaginary reactance.

The SC-32 takes a much cleaner architectural approach: the transient **prefix key `{{key:CMPLX}}`**. You never have to lock the calculator into a special mode. Whenever you want to treat the numbers on the stack as complex phasors rather than real scalars, you simply press Left Shift `{{key:↰}}` followed by `{{key:CMPLX}}` right before pressing the operator or function key. The `{{key:CMPLX}}` annunciator lights up on the top status bar for that single operation (and if you tap `{{key:CMPLX}}` by mistake, pressing `{{key:C}}` cancels the prefix without disturbing a single digit on the stack).

### How Two Complex Numbers Fit on a Four-Register Stack

To picture how `{{key:CMPLX}}` works, look at the four shelves of the RPN stack ($T, Z, Y, X$). Because one complex number $\mathbf{z} = \text{Real} + \text{Imag}\cdot i$ occupies **two adjacent shelves** (with its Real part on the upper shelf and its Imaginary part on the lower shelf), our four-register stack is the exact height needed to hold **two complete complex numbers at the same time**:
$$\mathbf{z}_A = T + Zi \quad (\text{upper register pair } T, Z), \qquad \mathbf{z}_B = Y + Xi \quad (\text{lower register pair } Y, X)$$

Once you see the four registers as two stacked complex pairs—$\mathbf{z}_A$ sitting in $(T, Z)$ above $\mathbf{z}_B$ sitting in $(Y, X)$—every complex operation follows the same natural rhythm as real RPN arithmetic:

- **Unary Complex Functions (`{{key:CMPLX}}` followed by `{{key:√x}}`, `{{key:1/x}}`, `{{key:x²}}`, `{{key:eˣ}}`, `{{key:LN}}`, `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`, or `{{key:+/-}}`):** A unary complex operation acts *only* on the lower pair $\mathbf{z}_1 = Y + Xi$, replacing $(Y, X)$ in place with $f(\mathbf{z}_1)$ while leaving the upper pair $(T, Z)$ completely untouched! That architectural guarantee is huge: it means you can keep one complex number parked safely in $(T, Z)$ while you invert, square, or take the square root of a second complex number in $(Y, X)$.
- **Binary Complex Arithmetic (`{{key:CMPLX}}` followed by `{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`, `{{key:yˣ}}`, or `{{key:x∥y}}`):** A binary complex operation combines the upper complex number $\mathbf{z}_2 = T + Zi$ with the lower complex number $\mathbf{z}_1 = Y + Xi$ to form $\mathbf{w} = \mathbf{z}_2 \mathbin{\text{op}} \mathbf{z}_1$ (including direct parallel impedance $\mathbf{z}_2 \parallel \mathbf{z}_1 = \frac{\mathbf{z}_2 \mathbf{z}_1}{\mathbf{z}_2 + \mathbf{z}_1}$ via `{{key:CMPLX}} {{key:x∥y}}`). The resulting Real and Imaginary parts land in $(Y, X)$, and the upper stack drops by two levels (replicating the old Register $T$ into both $T$ and $Z$).

| Operation Class | Key Sequence | Input Stack | Output in $(Y, X)$ | Upper Stack $(T, Z)$ |
| :--- | :--- | :--- | :--- | :--- |
| **Complex Negation** | `{{key:CMPLX}} {{key:+/-}}` | $\mathbf{z}_1 = Y + Xi$ | $-Y - Xi$ | Preserved ($T, Z$ unchanged) |
| **Unary Complex Functions** | `{{key:CMPLX}}` + `{{key:√x}}`, `{{key:1/x}}`, `{{key:x²}}`, `{{key:eˣ}}`, `{{key:LN}}`, `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}` | $\mathbf{z}_1 = Y + Xi$ | $f(\mathbf{z}_1)$ | Preserved ($T, Z$ unchanged) |
| **Binary Complex Arithmetic** | `{{key:CMPLX}}` + `{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`, `{{key:yˣ}}` | $\mathbf{z}_2 = T + Zi$, $\mathbf{z}_1 = Y + Xi$ | $\mathbf{z}_2 \mathbin{\text{op}} \mathbf{z}_1$ | 2-level drop ($T \to Z, T$) |
| **Complex Parallel Impedance** | `{{key:CMPLX}} {{key:x∥y}}` | $\mathbf{z}_2 = T + Zi$, $\mathbf{z}_1 = Y + Xi$ | $\dfrac{\mathbf{z}_2 \mathbf{z}_1}{\mathbf{z}_2 + \mathbf{z}_1}$ | 2-level drop ($T \to Z, T$) |

### Loading Two Complex Numbers onto the Stack

How do you load $\mathbf{z}_A = a + bi$ and $\mathbf{z}_B = c + di$ so that $\mathbf{z}_A$ sits in $(T, Z)$ and $\mathbf{z}_B$ sits in $(Y, X)$? Just enter the four numbers in reading order ($a$, then $b$, then $c$, then $d$) separated by `{{key:ENTER}}`:
1. **Load the first complex number $\mathbf{z}_A = a + bi$:** Key `a {{key:ENTER}} b {{key:ENTER}}`. The second `{{key:ENTER}}` parks $b$ in $Y$ (with $a$ in $Z$) so the next digit you type will lift both $a$ and $b$ upward.
2. **Load the second complex number $\mathbf{z}_B = c + di$:** Key `c {{key:ENTER}} d`. Typing `c` lifts $a \to T$ and $b \to Z$, and pressing `{{key:ENTER}} d` places $c$ in $Y$ and $d$ in $X$ without needing a trailing `{{key:ENTER}}`.
3. **Execute:** With $(T = a,\; Z = b,\; Y = c,\; X = d)$, press `{{key:CMPLX}}` followed by your binary operator (`{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`, `{{key:yˣ}}`, or `{{key:x∥y}}`) to leave $\operatorname{Re}(\mathbf{w})$ in Register $Y$ and $\operatorname{Im}(\mathbf{w})$ in Register $X$.

---

## Live Stack Proof of Euler's Identity: $e^{i\pi} + 1 = 0$

Richard Feynman called Leonhard Euler's 1748 equation "the most remarkable formula in mathematics" because it unites the five fundamental constants of arithmetic, algebra, geometry, and analysis—$0, 1, i, \pi,$ and $e$—in a single breath:
$$e^{i\theta} = \cos\theta + i\sin\theta \implies e^{i\pi} = \cos\pi + i\sin\pi = -1 + 0i$$

Why is $e^{i\pi}$ equal to $-1$? In Chapter 3 we saw that $e^x$ is the result of continuous growth when the growth rate is in phase with the current state. When you multiply the growth rate by $i$, the rate of change is rotated $90^\circ$ perpendicular to the radius vector—like the velocity of a satellite in a circular orbit! Instead of growing outward in magnitude, the point $e^{i\theta}$ sweeps around the unit circle at unit radius, and after an arc of $\theta = \pi\text{ radians}$ ($180^\circ$), it lands on the opposite side of the circle at $-1 + 0i$.

With the SC-32 in **Radians mode (`{{key:RAD}}`)**, we can watch this rotation happen live on the stack. We represent the pure imaginary exponent $0 + \pi i$ by placing **Real $= 0$ in Register $Y$** and **Imaginary $= \pi$ in Register $X$**, and then evaluate the complex exponential via `{{res:sc32_05_complex_numbers_phasors_seq_01:keys}}`:

| Step | Keystroke | Register T | Register Z | Register Y (Real) | Register X (Imag) | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Real exponent $0.0$ entered in $X$ (lifts to $Y$ when $\pi$ is pressed) |
| 2 | `{{key:π}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.14159265359$ | Imaginary exponent $\pi$ entered in $X$; $0.0$ lifts to $Y$ |
| 3 | `{{key:CMPLX}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.14159265359$ | `{{key:CMPLX}}` annunciator illuminated |
| 4 | `{{key:eˣ}}` | $0.0000$ | $0.0000$ | **-1.0000000000** | **0.0000000000** | $e^{0 + \pi i} = -1.0 + 0.0i$ |

After Step 4, Register $Y$ holds the exact real component $\operatorname{Re}(e^{i\pi}) = -1.0000000000$ and Register $X$ holds the imaginary component $\operatorname{Im}(e^{i\pi}) = 0.0000000000$.

{{blocks:sc32_hero_keynote|SC-32 Scientific Instrument Keynote Portrait}}
*Figure 5.2: The SC-32 scientific instrument executing high-precision complex analysis, preserving certified 12-digit IEEE-754 mantissa accuracy across transcendental evaluating pipelines.*

To complete Euler's Identity $e^{i\pi} + 1 = 0$, we add the complex real unit $+1 + 0i$ via `{{res:sc32_05_complex_numbers_phasors_seq_30:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_30:value}}`**, bringing both Register $Y$ and Register $X$ to exact **$0.0000000000$**.

---

## Polar $\leftrightarrow$ Rectangular Transformations in the Complex Domain

In AC circuit and RF analysis, we constantly switch between two views of the same complex number: **rectangular form** ($\mathbf{z} = x + iy$, which makes series addition effortless) and **polar phasor form** ($\mathbf{z} = r\angle\theta = r e^{i\theta}$, which reveals the physical voltage/current magnitude $r$ and phase angle $\theta$):
$$r = |z| = \sqrt{x^2 + y^2}, \quad \theta = \operatorname{atan2}(y, x), \qquad x = \operatorname{Re}(z) = r\cos\theta, \quad y = \operatorname{Im}(z) = r\sin\theta$$

| Transformation | Key Sequence | Stack Input ($Y, X$) | Stack Output ($Y, X$) | Mathematical Mapping |
| :--- | :--- | :--- | :--- | :--- |
| **Cartesian to Polar** | `{{key:▸θ,r}}` | $Y = y$ (Vertical / Imaginary)<br>$X = x$ (Horizontal / Real) | $Y = \theta$ (Phase angle)<br>$X = r$ (Modulus / Magnitude) | $r = \operatorname{hypot}(X, Y), \quad \theta = \operatorname{atan2}(Y, X)$ |
| **Polar to Cartesian** | `{{key:▸y,x}}` | $Y = \theta$ (Phase angle)<br>$X = r$ (Modulus / Magnitude) | $Y = y$ (Vertical / Imaginary)<br>$X = x$ (Horizontal / Real) | $x = r\cos\theta, \quad y = r\sin\theta$ |

### The `{{key:x⇄y}}` Bridge: Converting $z = 3 + 4i$

Look closely at the table above and notice one subtle detail: in Chapter 4, the Euclidean vector keys `{{key:▸θ,r}}` and `{{key:▸y,x}}` placed the vertical component $y$ in Register $Y$ and the horizontal component $x$ in Register $X$. In Gaussian complex arithmetic ($\mathbf{z} = Y + Xi$), however, the Real part ($x$) sits in Register $Y$ and the Imaginary part ($y$) sits in Register $X$. Therefore, **pressing `{{key:x⇄y}}` is the one-keystroke bridge between Gaussian complex $(Y = \text{Real}, X = \text{Imag})$ order and Euclidean $(Y = y, X = x)$ polar conversion**:

- **From Complex $(Y = \text{Real}, X = \text{Imag})$ to Polar $(\theta, r)$:** Press `{{key:x⇄y}} {{key:▸θ,r}}`.
- **From Polar $(Y = \theta, X = r)$ to Complex $(Y = \text{Real}, X = \text{Imag})$:** Press `{{key:▸y,x}} {{key:x⇄y}}`.

Let us trace a round-trip conversion of $\mathbf{z} = 3 + 4i$ on the stack:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `3 {{key:ENTER}} 4` | $0.0000$ | $0.0000$ | $3.0000$ | $4.0000$ | Gaussian complex coordinates $(Y=\text{Real}, X=\text{Imag})$ |
| 2 | `{{key:x⇄y}} {{key:▸θ,r}}` | $0.0000$ | $0.0000$ | $0.927295$ | **$5.000000$** | Polar conversion: $\theta$ in $Y$, magnitude $r$ in $X$ |
| 3 | `{{key:▸y,x}}` | $0.0000$ | $0.0000$ | $4.000000$ | **$3.000000$** | Rectangular conversion: horizontal $x$ in $X$, vertical $y$ in $Y$ |
| 4 | `{{key:x⇄y}}` | $0.0000$ | $0.0000$ | **$3.000000$** | **$4.000000$** | Realign to Gaussian complex format: Real in $Y$, Imag in $X$ |

---

## AC Circuit Analysis: Series & Parallel Complex Impedance

In an alternating-current network driven at angular frequency $\omega = 2\pi f$, every passive component maps to a point in the complex impedance plane: a **resistor** ($R$) sits on the positive real axis at $\mathbf{Z}_R = R + 0i\,\Omega$; an **inductor** ($L$) points straight up the positive imaginary axis at $\mathbf{Z}_L = 0 + j\omega L\,\Omega$ (because Faraday's law $v = L\,di/dt$ multiplies by $j\omega$, advancing voltage $90^\circ$ ahead of current); and a **capacitor** ($C$) points straight down the negative imaginary axis at $\mathbf{Z}_C = 0 - j/(\omega C)\,\Omega$ (dragging voltage $90^\circ$ behind current).

### Complex Series Impedance Addition

When two AC branches are wired in series—say, an inductive coil $\mathbf{Z}_1 = 8.0 + 4.0i\,\Omega$ followed by a capacitive load $\mathbf{Z}_2 = 4.0 - 8.0i\,\Omega$—the same current flows through both, so their impedances add component by component:
$$\mathbf{Z}_{\text{series}} = \mathbf{Z}_1 + \mathbf{Z}_2 = (8.0 + 4.0) + (4.0 - 8.0)i = 12.0 - 4.0i\,\Omega$$

Loading $\mathbf{Z}_2$ into $(T, Z)$ and $\mathbf{Z}_1$ into $(Y, X)$ and summing in the complex plane via `{{res:sc32_05_complex_numbers_phasors_seq_02:keys}}` resolves both components simultaneously:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `4 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $4.0000$ | $4.0000$ | Real part of $\mathbf{Z}_2$ pushed |
| 2 | `8 {{key:+/-}} {{key:ENTER}}` | $0.0000$ | $4.0000$ | $-8.0000$ | $-8.0000$ | Imag part of $\mathbf{Z}_2$ pushed |
| 3 | `8 {{key:ENTER}}` | $4.0000$ | $-8.0000$ | $8.0000$ | $8.0000$ | Real part of $\mathbf{Z}_1$ pushed |
| 4 | `4` | **$4.0000$** | **$-8.0000$** | **$8.0000$** | **$4.0000$** | Complete 4-register setup |
| 5 | `{{key:CMPLX}} {{key:+}}` | $4.0000$ | $4.0000$ | **$12.000000$** | **$-4.000000$** | $\mathbf{Z}_{\text{total}} = 12.0 - 4.0i\,\Omega$ |

The display immediately shows **Real $= 12.0\,\Omega$ in Register $Y$** and **Imaginary $= -4.0\,\Omega$ in Register $X$**.

---

### Parallel Complex Impedance via Stack Admittance

What if two reactive branches—$\mathbf{Z}_1 = 20.0 + 15.0i\,\Omega$ and $\mathbf{Z}_2 = 10.0 - 25.0i\,\Omega$—are wired in *parallel* across the same voltage source? Now their currents add, which means their reciprocal **complex admittances** ($\mathbf{Y} = 1/\mathbf{Z} = G + jB$, measured in Siemens) add directly:
$$\mathbf{Y}_{\text{parallel}} = \mathbf{Y}_1 + \mathbf{Y}_2 = \frac{1}{\mathbf{Z}_1} + \frac{1}{\mathbf{Z}_2} \implies \mathbf{Z}_{\text{parallel}} = \frac{1}{\mathbf{Y}_{\text{parallel}}}$$

Watch how the unary in-place architecture of `{{key:CMPLX}} {{key:1/x}}` lets you solve this entire parallel network on the 4-register stack without touching a single memory register:

1. **Invert Branch 1 in $(Y, X)$:** Key `{{res:sc32_05_complex_numbers_phasors_seq_03:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_03:value}}`**. This converts $\mathbf{Z}_1 = 20 + 15i\,\Omega$ into its complex admittance $\mathbf{Y}_1 = 0.032000 - 0.024000i\,\text{S}$ in $(Y, X)$.
2. **Load and Invert Branch 2 (Automatically Lifting $\mathbf{Y}_1$ into $(T, Z)$):** Key `{{res:sc32_05_complex_numbers_phasors_seq_04:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_04:value}}`**. Typing `10 {{key:ENTER}} 25 {{key:+/-}}` lifts $\mathbf{Y}_1$ cleanly into the upper registers $(T = 0.032000,\; Z = -0.024000)$, and pressing `{{key:CMPLX}} {{key:1/x}}` inverts $\mathbf{Z}_2$ in place into $\mathbf{Y}_2 = 0.013793 + 0.034483i\,\text{S}$ in $(Y, X)$ without disturbing $(T, Z)$!
3. **Sum Admittances and Invert Back to Ohms:** Key `{{res:sc32_05_complex_numbers_phasors_seq_05:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_05:value}}`**. `{{key:CMPLX}} {{key:+}}` adds the two admittances into $\mathbf{Y}_{\text{parallel}} = 0.045793 + 0.010483i\,\text{S}$, and `{{key:CMPLX}} {{key:1/x}}` inverts that total admittance back into the equivalent parallel impedance $\mathbf{Z}_{\text{parallel}} = \mathbf{20.7516 - 4.7507i\,\Omega}$ (which you can also compute in a single stroke via `20 {{key:ENTER}} 15 {{key:ENTER}} 10 {{key:ENTER}} 25 {{key:+/-}} {{key:CMPLX}} {{key:x∥y}}`):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `20 {{key:ENTER}} 15 {{key:CMPLX}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.032000$ | $-0.024000$ | Branch 1 admittance $\mathbf{Y}_1$ in $(Y, X)$ |
| 2 | `10 {{key:ENTER}} 25 {{key:+/-}} {{key:CMPLX}} {{key:1/x}}` | $0.032000$ | $-0.024000$ | $0.013793$ | $0.034483$ | $\mathbf{Y}_1$ lifts to $(T, Z)$; $\mathbf{Y}_2$ in $(Y, X)$ |
| 3 | `{{key:CMPLX}} {{key:+}}` | $0.032000$ | $0.032000$ | $0.045793$ | $0.010483$ | Sum admittances: $\mathbf{Y}_{\text{parallel}} = \mathbf{Y}_1 + \mathbf{Y}_2$ |
| 4 | `{{key:CMPLX}} {{key:1/x}}` | $0.032000$ | $0.032000$ | **$20.7516$** | **$-4.7507$** | Invert admittance: $\mathbf{Z}_{\text{parallel}} = 20.75 - 4.75i\,\Omega$ |

---

## RF Transmission Lines, Reflection Coefficient ($\Gamma$), VSWR & Smith Chart

When an electromagnetic wave travels down a coaxial cable of characteristic impedance $Z_0$ (typically $50\,\Omega$) and strikes an antenna whose load impedance $\mathbf{Z}_L = R_L + jX_L$ does not match $Z_0$, boundary conditions for voltage and current cannot be satisfied by a forward wave alone. Part of the incident wave bounces back toward the transmitter—just like a beam of light partially reflecting off a glass window when the refractive index jumps.

In 1939, Bell Labs engineer Phillip H. Smith showed that the entire semi-infinite right half of the complex impedance plane ($R_L \ge 0$) can be mapped inside the unit circle via a bilinear Möbius transformation, defining the complex **voltage reflection coefficient** $\mathbf{\Gamma}$ (whose polar plot is the famous **Smith Chart**):
$$\mathbf{\Gamma} = \frac{\mathbf{Z}_L - Z_0}{\mathbf{Z}_L + Z_0} = \frac{\mathbf{z} - 1}{\mathbf{z} + 1}, \quad \text{where } \mathbf{z} = \frac{\mathbf{Z}_L}{Z_0} = r + jx$$
When the load is perfectly matched ($\mathbf{Z}_L = Z_0$), $\mathbf{\Gamma} = 0$ sits at the exact bullseye center of the Smith Chart and $100\%$ of power enters the antenna. When a mismatch is present ($0 < |\mathbf{\Gamma}| \le 1$), the interfering forward and reflected waves set up a stationary interference pattern along the coax whose peak-to-trough voltage ratio is the **Voltage Standing Wave Ratio (VSWR)**, while the reflected power fraction $|\mathbf{\Gamma}|^2$ determines the **Return Loss ($RL$)** and **Mismatch Loss ($ML$)**:
$$\text{VSWR} = \frac{1 + |\mathbf{\Gamma}|}{1 - |\mathbf{\Gamma}|}, \qquad RL = -20 \log_{10} |\mathbf{\Gamma}|\;\text{(dB)}, \qquad ML = -10 \log_{10} \left(1 - |\mathbf{\Gamma}|^2\right)\;\text{(dB)}$$

### Antenna Feedline Mismatch

Suppose an dipole antenna with measured feedpoint impedance $\mathbf{Z}_L = 75.0 + 40.0i\,\Omega$ is connected to a $Z_0 = 50.0\,\Omega$ coaxial feedline. Subtracting and adding the real $50\,\Omega$ characteristic impedance gives the complex numerator $\mathbf{Z}_L - Z_0 = 25 + 40i\,\Omega$ and denominator $\mathbf{Z}_L + Z_0 = 125 + 40i\,\Omega$:
$$\mathbf{\Gamma} = \frac{(75 + 40i) - 50}{(75 + 40i) + 50} = \frac{25 + 40i}{125 + 40i}$$

We load the numerator into $(T, Z)$ (`25 {{key:ENTER}} 40 {{key:ENTER}}`), the denominator into $(Y, X)$ (`125 {{key:ENTER}} 40`), and press `{{key:CMPLX}} {{key:÷}}` to obtain $\mathbf{\Gamma} = \mathbf{0.274311 + 0.232221i}$. Swapping to polar coordinates via `{{key:x⇄y}} {{key:▸θ,r}}` immediately reveals the reflection magnitude $|\mathbf{\Gamma}| = \mathbf{0.359406}$ in Register $X$ and phase angle $\theta_\Gamma = 0.702494\text{ rad}$ ($40.25^\circ$) in Register $Y$. From $|\mathbf{\Gamma}| = 0.359406$, the standing wave ratio follows as `{{res:sc32_05_complex_numbers_phasors_seq_06:keys}}` $\implies \text{VSWR} = \mathbf{2.1221}$, and the return loss as `{{res:sc32_05_complex_numbers_phasors_seq_07:keys}}` $\implies RL = \mathbf{8.89\text{ dB}}$ ($8.8883\text{ dB}$):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `25 {{key:ENTER}} 40 {{key:ENTER}}` | $0.0000$ | $25.0000$ | $40.0000$ | $40.0000$ | Numerator $(Z_L - Z_0)$ pushed |
| 2 | `125 {{key:ENTER}} 40` | $25.0000$ | $40.0000$ | $125.0000$ | $40.0000$ | Denominator $(Z_L + Z_0)$ loaded into $(Y, X)$ |
| 3 | `{{key:CMPLX}} {{key:÷}}` | $25.0000$ | $25.0000$ | **$0.274311$** | **$0.232221$** | Reflection coefficient $\mathbf{\Gamma} = 0.2743 + 0.2322i$ |
| 4 | `{{key:x⇄y}} {{key:▸θ,r}}` | $25.0000$ | $25.0000$ | $0.702494$ | **$0.359406$** | Polar: Phase $\theta = 0.702494\text{ rad}$ ($40.25^\circ$) in $Y$, magnitude $\lvert\mathbf{\Gamma}\rvert = 0.3594$ in $X$ |
| 5 | `{{key:ENTER}} {{key:ENTER}} 1 {{key:+}} {{key:x⇄y}} 1 {{key:x⇄y}} {{key:-}} {{key:÷}}` | $0.702494$ | $0.702494$ | $0.702494$ | **$2.1221$** | VSWR $= (1+\lvert\mathbf{\Gamma}\rvert)/(1-\lvert\mathbf{\Gamma}\rvert) = 2.1221$ |

---

## Complex Powers, Roots of Unity & de Moivre's Theorem

Because Euler's formula writes any complex number in polar form as $z = r e^{i\theta}$, raising a complex number to the $n$-th power simply raises its radius to $r^n$ while multiplying its angle by $n\theta$ (**Abraham de Moivre's theorem**), and taking an $n$-th root divides its angle into $n$ equally spaced spokes around the circle:
$$z = r e^{i\theta} \implies z^n = r^n e^{i n \theta} = r^n (\cos(n\theta) + i\sin(n\theta))$$
$$\sqrt[n]{z} = r^{1/n} \left[\cos\left(\frac{\theta + 2k\pi}{n}\right) + i\sin\left(\frac{\theta + 2k\pi}{n}\right)\right], \quad k = 0, 1, \dots, n-1$$

Even more generally, on the SC-32 the binary complex power operator `{{key:CMPLX}} {{key:yˣ}}` evaluates $\mathbf{z}_2^{\mathbf{z}_1} = e^{\mathbf{z}_1 \ln(\mathbf{z}_2)}$ when *both* the base and the exponent are complex numbers! To evaluate $(1 + i)^{(1 - i)}$, we load the base $\mathbf{z}_2 = 1 + i$ into $(T, Z)$ (`1 {{key:ENTER}} 1 {{key:ENTER}}`), load the exponent $\mathbf{z}_1 = 1 - i$ into $(Y, X)$ (`1 {{key:ENTER}} 1 {{key:+/-}}`), and press `{{key:CMPLX}} {{key:yˣ}}` to obtain **$2.807879 + 1.317865i$**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1 {{key:ENTER}} 1 {{key:ENTER}}` | $0.0000$ | $1.0000$ | $1.0000$ | $1.0000$ | Base $z_2 = 1 + i$ loaded into $(T, Z)$ |
| 2 | `1 {{key:ENTER}} 1 {{key:+/-}}` | $1.0000$ | $1.0000$ | $1.0000$ | $-1.0000$ | Exponent $z_1 = 1 - i$ loaded into $(Y, X)$ |
| 3 | `{{key:CMPLX}} {{key:yˣ}}` | $1.0000$ | $1.0000$ | **$2.807879$** | **$1.317865$** | General complex power $z_2^{z_1}$ evaluated |

---

## Complex Parallel Impedance: Admittance Inversion vs. Direct `CMPLX x∥y`

Across AC circuit analysis, RF impedance matching, and electro-acoustics, the SC-32's transient `{{key:CMPLX}}` prefix gives you two complementary ways to evaluate parallel complex impedances in Registers $(Y, X)$.

When you want to inspect the physical **conductance $G$ and susceptance $B$** of each parallel branch ($\mathbf{Y}_k = 1/\mathbf{Z}_k = G_k + jB_k$), use **Reciprocal Admittance Summation (`{{key:CMPLX}} {{key:1/x}}`)**. For $\mathbf{Z}_1 = 20 + 15i\,\Omega$ and $\mathbf{Z}_2 = 10 - 25i\,\Omega$, inverting each branch in place shows you the inductive admittance $\mathbf{Y}_1 = 0.0320 - 0.0240i\,\text{S}$ and capacitive admittance $\mathbf{Y}_2 = 0.0138 + 0.0345i\,\text{S}$ before you add (`{{key:CMPLX}} {{key:+}}`) and invert back (`{{key:CMPLX}} {{key:1/x}}`) to get $\mathbf{Z}_{\text{parallel}} = \mathbf{20.7516 - 4.7507i\,\Omega}$. Similarly, in the conjugate Zobel loudspeaker network analyzed at the close of this chapter ($\mathbf{Z}_1 = 3 + 4i$, $\mathbf{Z}_2 = 3 - 4i$), admittance inversion exposes why the opposite susceptances $\mp 0.16i\,\text{S}$ cancel identically, leaving pure real conductance $2G = 0.24\,\text{S} \implies \mathbf{4.166667\,\Omega}$.

When you simply want the equivalent parallel impedance in the fewest keystrokes, use the **Single-Stroke Complex Parallel Operator (`{{key:CMPLX}} {{key:x∥y}}`)**: load $\mathbf{Z}_1$ into $(T, Z)$ and $\mathbf{Z}_2$ into $(Y, X)$ (`20 {{key:ENTER}} 15 {{key:ENTER}} 10 {{key:ENTER}} 25 {{key:+/-}}`) and press `{{key:CMPLX}} {{key:x∥y}}` to evaluate $\frac{\mathbf{Z}_1 \mathbf{Z}_2}{\mathbf{Z}_1 + \mathbf{Z}_2} = \mathbf{20.7516 - 4.7507i\,\Omega}$ in one operation, saving eight keystrokes.

The same dual-pathway verification certifies complex exponentials and logarithms: keying `{{res:sc32_05_complex_numbers_phasors_seq_31:keys}}` evaluates $e^{i\pi}$ via `{{key:CMPLX}} {{key:eˣ}}` to yield $-1.0000000000 + 0.0000000000i$, which can be inverted immediately via `{{key:CMPLX}} {{key:LN}}` to recover $0.0000000000 + 3.1415926536i$.

### Manual Real-Imaginary Foil Expansion vs. Paired-Register `{{key:CMPLX}}` Arithmetic

The table below compares parenthesized complex-number string entry on an algebraic calculator against direct two-register $(Y, X)$ phasor evaluation on the SC-32 stack:

| Challenge / Metric | Conventional Algebraic Calculator (Infix) | Algebraic Strokes | SC-32 RPN Stack Method | SC-32 Strokes | Stack Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **AC Impedance**: $(50+j20) \parallel -j15$ | Mode switch $\to$ `( ( 5 0 + 2 0 i ) ^ -1 + ( - 1 5 i ) ^ -1 ) ^ -1 =` (32 strokes). Real and imaginary parts truncated off-screen; angle hidden in sub-menus. | 32 | **$(Y, X)$ Complex Mode**: Enter real and imag directly; combine via `{{key:x∥y}}` $\to$ Register $Y$ shows Real, Register $X$ shows Imag. Tap `{{key:▸θ,r}}` to see $\lvert Z\rvert$ and phase $\phi$ simultaneously. | 18 | **44% fewer strokes + simultaneous $\lvert Z\rvert$ and $\phi$** |

---

### Poles, Branch Cuts, and Non-Destructive Complex Recovery

Because complex arithmetic pairs two registers for every operand, the SC-32 firmware enforces strict boundary guards to keep the $(T, Z)$ and $(Y, X)$ register pairs synchronized. Pressing `{{key:CMPLX}}` illuminates the `{{key:CMPLX}}` annunciator in the status bar for the next operation only; if you tap `{{key:CMPLX}}` by mistake, pressing `{{key:C}}` cancels the prefix cleanly without displacing or clearing a single stack value. When evaluating a complex quotient $\mathbf{z}_{\text{num}} / \mathbf{z}_{\text{den}}$ via `{{key:CMPLX}} {{key:÷}}`, always load the numerator $\mathbf{z}_{\text{num}}$ into Registers $(T, Z)$ first and the denominator $\mathbf{z}_{\text{den}}$ into Registers $(Y, X)$ second; if you ever enter them in reverse order, you do not need to re-type the four components—simply press `{{key:CMPLX}} {{key:1/x}}` to take the complex reciprocal of $(Y, X)$ in place!

What happens at a pole or singularity in the complex plane? Attempting complex division by the origin $0 + 0i$ (`0 {{key:ENTER}} 0` followed by `{{key:CMPLX}} {{key:÷}}` or `{{key:CMPLX}} {{key:1/x}}`) immediately halts execution and triggers `Error 02: DIVIDE BY 0`, leaving your four stack registers completely unmodified until you press `{{key:C}}` to clear the error banner. Likewise, while the SC-32 supports complex algebraic powers, roots, exponentials, natural logarithms, and direct circular functions (`SIN`, `COS`, `TAN`), attempting an unsupported combination such as `{{key:CMPLX}} {{key:ASIN}}` or `{{key:CMPLX}} {{key:HYP}}` raises `Error 01: INVALID DATA` non-destructively so you can evaluate the corresponding logarithmic conformal mapping directly on the stack.

## AC Power Grids, Impedance Matching, and RF Transmission Lines in the Complex Plane

In AC electrical engineering, determining the equivalent impedance of a parallel RLC branch $Z_{\text{eq}} = \frac{Z_1 Z_2}{Z_1 + Z_2}$ requires evaluating complex numbers in polar or rectangular form {{cite:horowitz2015}}:

$$Z_{\text{eq}} = \frac{(50 + 25i) \times (10 - 40i)}{(50 + 25i) + (10 - 40i)}$$
On algebraic scientific calculators, complex arithmetic requires typing clumsy multi-character strings with explicit imaginary unit `i` keys and double parentheses for every complex operand. A single misplaced parenthesis scrambles real resistance with imaginary reactance, producing erroneous phase angles that can destroy prototype RF amplifier stages {{cite:parker2019}}.

On the SC-32, the $(Y, X)$ stack allocation represents the two-dimensional complex plane natively ($Y = \text{Real},\; X = \text{Imaginary}$) {{cite:hp15c1982}}. With the dedicated complex evaluator `{{key:CMPLX}}`, complex multiplication, division, reciprocals, and square roots execute in place. In addition, the parallel operator `{{key:x∥y}}` solves parallel complex impedances in a single keystroke, eliminating 18 algebraic button presses and completely preventing real/imaginary crosstalk.

---

### Complex Arithmetic Primitives & De Moivre Roots in `CMPLX` Mode

We begin by exercising the paired $(Y, X)$ complex plane architecture on conjugate products, principal square roots, microwave scattering parameters, and quarter-wave transmission line transformers. In the complex plane, a number $z = x + iy = r e^{i\theta}$ and its **complex conjugate** $z^* = x - iy = r e^{-i\theta}$ are mirror reflections across the real axis. When you multiply them together, their opposite phase angles cancel ($\theta + (-\theta) = 0^\circ$), collapsing the product onto the positive real axis at the squared Euclidean length $|z|^2 = x^2 + y^2$. For $z = 6 + 8i$, let us verify that $z \cdot z^*$ lands on the real axis with zero imaginary residual:

$$z^* = 6 - 8i \implies z \cdot z^* = 6^2 + 8^2 = 36 + 64 = 100 + 0i$$

Keying `6 {{key:ENTER}} 8 {{key:ENTER}}` loads $z = 6 + 8i$ into the upper register pair $(T, Z)$, and entering the conjugate pair `6 {{key:ENTER}} 8 {{key:+/-}}` into $(Y, X)$ followed by `{{key:CMPLX}} {{key:×}}` in `{{res:sc32_05_complex_numbers_phasors_seq_08:keys}}` multiplies $(T + Zi)(Y + Xi)$ and drops the stack by two levels, leaving $(Y = 100.0000,\; X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_08:value}}})$—confirming **$\text{Real} = 100.0$, $\text{Imag} = 0.0$**.

When 16th-century algebraists first encountered $i = \sqrt{-1}$, critics feared that taking the square root of $i$ itself ($\sqrt{i}$) would require inventing yet another "more imaginary" dimension outside the complex plane. Carl Friedrich Gauss and Jean-Robert Argand proved that the complex plane is algebraically closed: on the *Unit Circle Volvelle*, $i = 0 + 1i$ is simply a unit vector pointing straight up at $90^\circ$ ($\pi/2\text{ rad}$), so taking its principal square root takes the square root of its unit length ($\sqrt{1} = 1$) while bisecting its angle in half to **$45^\circ$** ($\pi/4\text{ rad}$) in the first quadrant—the exact $45^\circ$ phase angle of Warburg electrochemical diffusion and RF skin-effect impedance:

$$\sqrt{i} = \sqrt{0 + 1i} = e^{i\pi/4} = \cos\left(\frac{\pi}{4}\right) + i\sin\left(\frac{\pi}{4}\right) = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}i \approx 0.707107 + 0.707107i$$

Entering the pure imaginary unit $0 + 1i$ with `0 {{key:ENTER}} 1` (placing Real $= 0$ in $Y$ and Imag $= 1$ in $X$) and executing `{{res:sc32_05_complex_numbers_phasors_seq_09:keys}}` evaluates the complex square root in place, leaving $Y = \mathbf{0.707107}$ and $X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_09:value}}}$.

In radio-frequency engineering, that same $(Y, X)$ complex plane bridges directly to polar reflection metrics via `{{key:x⇄y}} {{key:▸θ,r}}`. When an RF engineer characterizes a microwave filter or cellular antenna on a Vector Network Analyzer (VNA), the instrument measures the input **scattering parameter** $S_{11}$—the complex ratio of the reflected voltage wave to the incident voltage wave. Suppose a port exhibits $S_{11} = 0.25 - 0.40i$. What is its **Return Loss ($\text{RL}$)** in decibels (how many dB the reflected wave is suppressed below the incident carrier)?

$$|S_{11}| = \sqrt{0.25^2 + (-0.40)^2} = \sqrt{0.0625 + 0.1600} = \sqrt{0.2225} \approx 0.471699$$
$$\text{RL} = -20 \log_{10}(0.471699) = 6.527\text{ dB}$$

Loading $S_{11}$ via `0.25 {{key:ENTER}} 0.40 {{key:+/-}}` and bridging to polar coordinates with `{{key:x⇄y}} {{key:▸θ,r}}` leaves phase $\theta = -1.012197\text{ rad}$ ($-58.0^\circ$) in Register $Y$ and reflection magnitude $|S_{11}| = 0.471699$ in Register $X$. Completing the sequence `{{res:sc32_05_complex_numbers_phasors_seq_16:keys}}` converts that magnitude directly into Return Loss $\text{RL} =$ **`{{res:sc32_05_complex_numbers_phasors_seq_16:value}}`** $\text{dB}$ (and if you also need the standing wave ratio $\text{VSWR} = (1+|S_{11}|)/(1-|S_{11}|) = 2.786$, pressing `{{key:LASTX}}` right after `{{key:LOG}}` recovers $|S_{11}|$).

Once a reflection mismatch is measured, how do you match a $Z_L = 100\,\Omega$ patch antenna to a $Z_0 = 50\,\Omega$ transmitter feedline without lumped inductors or capacitors? A transmission line segment of length $\ell = \lambda/4$ ($90^\circ$ of electrical phase shift one way, or $180^\circ$ round-trip across the Smith Chart) acts as a hardware **impedance inverter** $Z_{\text{in}} = Z_{\text{line}}^2 / Z_L$. Choosing the quarter-wave section's characteristic impedance as the geometric mean $Z_{\text{line}} = \sqrt{Z_0 Z_L} = \sqrt{50 \times 100} \approx 70.7107\,\Omega$ transforms the $100\,\Omega$ load into an exact $50\,\Omega$ input match:

$$Z_{\text{in}} = \frac{70.7107^2}{100.0} = \frac{5000.0}{100.0} = 50.00\,\Omega$$

Squaring $Z_{\text{line}} = 70.7107\,\Omega$ in place and dividing by $Z_L = 100\,\Omega$ via `{{res:sc32_05_complex_numbers_phasors_seq_17:keys}}` confirms the **$50.0000\,\Omega$** impedance match:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `70.7107` | $0.0000$ | $0.0000$ | $0.0000$ | $70.7107$ | Enter line characteristic impedance $Z_0$ |
| 2 | `{{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $5000.0031$ | Square characteristic impedance $Z_0^2$ |
| 3 | `100 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$50.0000$** | Divide by load resistance $Z_L$; matched $Z_{\text{in}} = 50.0\,\Omega$ |

---

### Complex Roots, Analytic Continuation & Audio Crossover Filters

The next seven models explore de Moivre's principal roots, complex circular functions (where sines and cosines can grow larger than $1$), and the transfer functions of Butterworth and Linkwitz-Riley loudspeaker crossovers. On the real number line, the equation $z^3 = -8$ has the familiar negative root $z = -2$. In the complex plane, however, $-8$ sits on the negative real axis at polar angle $\theta = \pi\text{ rad}$ ($180^\circ$): $z^3 = 8 e^{i\pi}$. By de Moivre's theorem, its three cube roots sit at the vertices of an equilateral triangle on a circle of radius $8^{1/3} = 2$, starting with the **principal root** at one-third of the angle ($\theta_0 = \pi/3 = 60^\circ$):

$$z_0 = 8^{1/3} e^{i\pi/3} = 2 \left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right) = 2(0.5 + 0.866025i) = 1.0 + 1.732051i$$

Loading the base $z_2 = -8 + 0i$ into $(T, Z)$ (`8 {{key:+/-}} {{key:ENTER}} 0 {{key:ENTER}}`) and evaluating the cube root via `{{res:sc32_05_complex_numbers_phasors_seq_18:keys}}` yields **`{{res:sc32_05_complex_numbers_phasors_seq_18:value}}`** in Register $X$, or forming the exact rational exponent $z_1 = 1/3 + 0i$ in $(Y, X)$ via `{{res:sc32_05_complex_numbers_phasors_seq_19:keys}}` evaluates the principal branch $e^{(1/3)\ln(-8)} = 2 e^{i\pi/3}$ to full precision, yielding $(Y = \mathbf{1.000000},\; X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_19:value}}})$.

Stepping from algebraic roots to complex trigonometry reveals an even deeper surprise. For a real angle $x$, $\sin x$ is trapped forever between $-1$ and $+1$. What happens when we feed a complex argument $z = x + iy = 1 + 2i$ into `{{key:CMPLX}} {{key:SIN}}`? By Euler's definition $\sin z = (e^{iz} - e^{-iz})/(2i)$, the imaginary component $iy$ becomes a real exponential $e^{\mp y}$, coupling circular oscillation along $x$ with hyperbolic growth ($\cosh y, \sinh y$) along $y$—which is why $\sin(1 + 2i)$ has a magnitude greater than $3.7$!

$$\sin(x + iy) = \sin x \cosh y + i \cos x \sinh y$$
$$\text{Real} = \sin(1)\cosh(2) \approx 0.841471 \times 3.762196 = 3.165779, \quad \text{Imag} = \cos(1)\sinh(2) \approx 0.540302 \times 3.626860 = 1.959601$$

Keying `1 {{key:ENTER}} 2` to load $1 + 2i$ into $(Y, X)$ and executing `{{res:sc32_05_complex_numbers_phasors_seq_21:keys}}` evaluates the complex sine in place, producing $(Y = \mathbf{3.165779},\; X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_21:value}}})$. By the same Euler expansion, the complex cosine $\cos(x + iy)$ describes damped standing waves on lossy transmission lines and evanescent waveguide modes:

$$\cos(x + iy) = \cos x \cosh y - i \sin x \sinh y$$
$$\text{Real} = \cos(1)\cosh(2) = 0.540302 \times 3.762196 = 2.032723, \quad \text{Imag} = -\sin(1)\sinh(2) = -0.841471 \times 3.626860 = -3.051898$$

Entering $1 + 2i$ and evaluating the complex cosine via `{{res:sc32_05_complex_numbers_phasors_seq_22:keys}}` yields $(Y = \mathbf{2.032723},\; X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_22:value}}})$. Even though $\sin(1+2i)$ and $\cos(1+2i)$ in our complex sine and cosine evaluations above grew far outside $[-1, +1]$, the principle of **analytic continuation** guarantees that the Pythagorean identity $\sin^2 z + \cos^2 z = 1$ still holds across the entire complex plane! Let us square both complex outputs and add them together on the stack:

$$\sin^2(1+2i) + \cos^2(1+2i) = (6.182115 + 12.407147i) + (-5.182115 - 12.407147i) = 1.000000 + 0.000000i$$

Notice how the large $\pm 12.407147i$ imaginary cross-terms cancel each other while $6.182115 - 5.182115$ collapses back to $1.000000$ (and if you chain the calculation directly from $z = 1+2i$ via `1 {{key:ENTER}} 2 {{key:CMPLX}} {{key:SIN}} {{key:CMPLX}} {{key:x²}} 1 {{key:ENTER}} 2 {{key:CMPLX}} {{key:COS}} {{key:CMPLX}} {{key:x²}} {{key:CMPLX}} {{key:+}}`, it holds to full 64-bit precision):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `3.165779 {{key:ENTER}} 1.959601` | $0.0000$ | $0.0000$ | $3.165779$ | $1.959601$ | Load $\sin(1+2i)$ from above |
| 2 | `{{key:CMPLX}} {{key:x²}}` | $0.0000$ | $0.0000$ | $6.182115$ | $12.407147$ | Square complex sine $(\sin z)^2$ |
| 3 | `2.032723 {{key:ENTER}} 3.051898 {{key:+/-}}` | $6.182115$ | $12.407147$ | $2.032723$ | $-3.051898$ | Load $\cos(1+2i)$ from above |
| 4 | `{{key:CMPLX}} {{key:x²}}` | $6.182115$ | $12.407147$ | $-5.182115$ | $-12.407147$ | Square complex cosine $(\cos z)^2$ |
| 5 | `{{key:CMPLX}} {{key:+}}` | $6.182115$ | $6.182115$ | **$1.000000$** | **$0.000000$** | Sum squares: $\sin^2 z + \cos^2 z = 1 + 0i$ |

This same complex cancellation governs the frequency response of analog audio filters. In 1930, British engineer Stephen Butterworth designed the "maximally flat" low-pass filter $H(s) = 1 / (s^2 + \sqrt{2}s + 1)$ so that passband ripple vanishes completely. At the normalized cutoff frequency $s = j\omega/\omega_c = 0 + 1i$ (e.g., $f_c = 2,500\text{ Hz}$), the $s^2 = -1$ term and the $+1$ constant in the denominator $B_2(j) = s^2 + \sqrt{2}s + 1$ cancel identically, leaving only the damping term $0 + j\sqrt{2}$:

$$s^2 = -1 + 0i, \quad \sqrt{2} s = 0 + 1.414214i \implies B_2(j) = (-1 + 1) + 1.414214i = 0 + 1.414214i$$
$$H(j) = \frac{1}{0 + 1.414214i} = 0 - \frac{1}{\sqrt{2}}i = 0 - 0.707107i \implies |H| = \frac{1}{\sqrt{2}} \approx -3.01\text{ dB}$$

Loading $B_2(j) = 0 + 1.414214i$ into $(Y, X)$ and inverting in place via `{{res:sc32_05_complex_numbers_phasors_seq_23:keys}}` (or exact `0 {{key:ENTER}} 2 {{key:√x}} {{key:CMPLX}} {{key:1/x}}`) directly evaluates the complex transfer function $H(j) = \mathbf{0.000000 - 0.707107i}$—showing both the $-3.01\text{ dB}$ half-power attenuation ($|H| = 1/\sqrt{2}$) and the $-90^\circ$ phase lag at crossover.

Why, then, do studio monitor loudspeakers rarely use a single 2nd-order Butterworth crossover? Because at the crossover frequency $s = j$, the low-pass output lags by $-90^\circ$ ($-i/\sqrt{2}$) while the high-pass output leads by $+90^\circ$ ($+i/\sqrt{2}$)—a $180^\circ$ phase opposition that causes a deep acoustic cancellation null! In 1976, Siegfried Linkwitz and Russ Riley solved this by cascading *two* 2nd-order Butterworth filters in series (`LR4`), squaring the transfer function so both drivers sit at $-6.02\text{ dB}$ ($|H| = 0.5$) and are in phase at $-180^\circ$, summing acoustically back to unity gain ($0.5 + 0.5 = 1.0$, $0\text{ dB}$):

$$H_{\text{LR4}}(j) = [H_{\text{Butter2}}(j)]^2 = \left(-\frac{i}{\sqrt{2}}\right)^2 = -0.500000 + 0.000000i \implies 20 \log_{10}(0.5) = -6.02\text{ dB}$$

Constructing $-i/\sqrt{2}$ in $(Y, X)$ with full precision and squaring in place via `0 {{key:ENTER}} 2 {{key:√x}} {{key:1/x}} {{key:+/-}} {{key:CMPLX}} {{key:x²}}` lands on exact Real **`-0.500000`** and Imag **`0.000000`**, from which `{{key:x⇄y}} {{key:ABS}} {{key:LOG}} 20 {{key:×}}` confirms the $-6.0206\text{ dB}$ crossover attenuation:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}} 2 {{key:√x}} {{key:1/x}} {{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-0.707107$ | Construct exact Butterworth response $0 - i/\sqrt{2}$ |
| 2 | `{{key:CMPLX}} {{key:x²}}` | $0.0000$ | $0.0000$ | **$-0.500000$** | **$0.000000$** | Evaluate $[H_{\text{Butter2}}]^2$; Real in $Y$, Imag in $X$ |
| 3 | `{{key:x⇄y}} {{key:ABS}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.500000$ | Inspect Real component magnitude $\lvert H\rvert = 0.5$ |
| 4 | `{{key:LOG}} 20 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$-6.020600$** | Calculate $-6.02\text{ dB}$ acoustic crossover attenuation |

When implementing active audio filters with operational amplifiers, complex impedance ratios determine the stage gain. Suppose an inverting active bandpass filter uses a parallel RC feedback network $Z_f = 10\text{ k}\Omega \parallel 10\text{ nF}$ and a series RC input network $Z_{\text{in}} = 1\text{ k}\Omega + 100\text{ nF}$. At the center angular frequency $\omega = 10,000\text{ rad/s}$ ($f = 1,591.55\text{ Hz}$), where $1/(\omega C_f) = 10\text{ k}\Omega$ and $1/(\omega C_{\text{in}}) = 1\text{ k}\Omega$, the feedback and input impedances are $Z_f = 5000 - 5000i\,\Omega$ and $Z_{\text{in}} = 1000 - 1000i\,\Omega$, giving a complex voltage gain $A_v = -Z_f / Z_{\text{in}}$ of:

$$Z_f = \frac{10000}{1 + j} = 5000 - 5000i\,\Omega, \quad Z_{\text{in}} = 1000 - 1000i\,\Omega \implies A_v = -\frac{Z_f}{Z_{\text{in}}} = -\frac{5000(1 - i)}{1000(1 - i)} = -5.0 + 0i$$

Because both networks share the exact same $-45^\circ$ phase angle at $\omega_0 = 10,000\text{ rad/s}$, executing `{{res:sc32_05_complex_numbers_phasors_seq_25:keys}}` cancels their reactive phase shifts completely via complex division and negation, yielding pure inverting gain $A_v = \mathbf{-5.000000}$ + **`{{res:sc32_05_complex_numbers_phasors_seq_25:value}}`** $i$ ($13.98\text{ dB}$):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `5000 {{key:ENTER}} 5000 {{key:+/-}} {{key:ENTER}}` | $0.0000$ | $5000.0000$ | $-5000.0000$ | $-5000.0000$ | Feedback impedance $Z_f$ pushed |
| 2 | `1000 {{key:ENTER}} 1000 {{key:+/-}}` | $5000.0000$ | $-5000.0000$ | $1000.0000$ | $-1000.0000$ | Input impedance $Z_{\text{in}}$ in $(Y, X)$ |
| 3 | `{{key:CMPLX}} {{key:÷}}` | $5000.0000$ | $5000.0000$ | $5.000000$ | $0.000000$ | Complex ratio $Z_f / Z_{\text{in}} = 5.0 + 0i$ |
| 4 | `{{key:CMPLX}} {{key:+/-}}` | $5000.0000$ | $5000.0000$ | **$-5.000000$** | **$0.000000$** | Negate gain: $A_v = -5.0 + 0i$ |

---

### Bridge Circuits, Three-Phase Power & Conformal Mapping

The next five scenarios extend complex stack arithmetic to AC impedance bridges, three-phase power grids, mechanical suspension eigenvalues, ionized plasma sheaths, and Joukowsky airfoil aerodynamics. To find the Thévenin output impedance looking into the detector terminals of an AC impedance bridge with upper and lower arms $Z_A = 10 + 20i\,\Omega$, $Z_C = 20 + 0i\,\Omega$ on the left and $Z_B = 30 - 10i\,\Omega$, $Z_D = 0 - 25i\,\Omega$ on the right, we short the excitation source and evaluate the series sum of two parallel complex branches:

$$Z_{\text{th}} = (Z_A \parallel Z_C) + (Z_B \parallel Z_D) = \left(\frac{140 + 80i}{13}\right) + \left(\frac{150 - 250i}{17}\right) \approx 19.5928 - 8.5520i\,\Omega$$

Look at how the SC-32's native complex parallel key `{{key:CMPLX}} {{key:x∥y}}` simplifies this bridge: instead of computing $(Z_A Z_C)/(Z_A + Z_C)$ by hand, `{{key:CMPLX}} {{key:x∥y}}` resolves each parallel arm in a single stroke:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `10 {{key:ENTER}} 20 {{key:ENTER}} 20 {{key:ENTER}} 0` | $10.0000$ | $20.0000$ | $20.0000$ | $0.0000$ | Load branch impedances $Z_A$ and $Z_C$ |
| 2 | `{{key:CMPLX}} {{key:x∥y}}` | $10.0000$ | $10.0000$ | $10.7692$ | $6.1538$ | Parallel branch $Z_{AC} = Z_A \parallel Z_C$ |
| 3 | `30 {{key:ENTER}} 10 {{key:+/-}} {{key:ENTER}} 0 {{key:ENTER}} 25 {{key:+/-}}` | $30.0000$ | $-10.0000$ | $0.0000$ | $-25.0000$ | Load branch impedances $Z_B$ and $Z_D$ |
| 4 | `{{key:CMPLX}} {{key:x∥y}}` | $30.0000$ | $30.0000$ | $8.8235$ | $-14.7059$ | Parallel branch $Z_{BD} = Z_B \parallel Z_D$ |
| 5 | `10.7692 {{key:ENTER}} 6.1538 {{key:CMPLX}} {{key:+}}` | $8.8235$ | $8.8235$ | **$19.5928$** | **$-8.5520$** | Sum branches: $Z_{\text{th}} = Z_{BD} + Z_{AC}$ |

Stepping from laboratory bridge circuits to continental utility grids raises a classic question of electrical power engineering: why can a high-voltage three-phase transmission tower carry megawatts of power across three phase wires without needing a fourth neutral return cable? In 1918, Charles LeGeyt Fortescue introduced **symmetrical components** using the $120^\circ$ complex phase rotator $a = e^{i 120^\circ} = \cos(120^\circ) + i\sin(120^\circ) = -0.5 + 0.866025i$ and $a^2 = e^{i 240^\circ} = -0.5 - 0.866025i$. Because the three unit phasors $1$, $a$, and $a^2$ point $120^\circ$ apart like the three spokes of a Mercedes star, their vector sum vanishes identically ($1 + a + a^2 = 0$), meaning balanced three-phase currents cancel at the neutral point:

$$a = -0.5 + 0.866025i, \quad a^2 = -0.5 - 0.866025i \implies 1 + a + a^2 = \mathbf{0.000000 + 0.000000i}$$

In Degrees mode (`{{key:DEG}}`), we project the two unit phasors $1\angle 120^\circ$ and $1\angle 240^\circ$ into Gaussian complex coordinates via `{{key:▸y,x}} {{key:x⇄y}}`, sum them via `{{key:CMPLX}} {{key:+}}`, and add the reference phase $1 + 0i$ to verify exact zero-sequence cancellation:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `120 {{key:ENTER}} 1 {{key:▸y,x}} {{key:x⇄y}}` | $0.0000$ | $0.0000$ | $-0.500000$ | $0.866025$ | Polar to Gaussian: $a = -0.5 + 0.8660i$ |
| 2 | `240 {{key:ENTER}} 1 {{key:▸y,x}} {{key:x⇄y}}` | $-0.500000$ | $0.866025$ | $-0.500000$ | $-0.866025$ | Polar to Gaussian: $a^2 = -0.5 - 0.8660i$ |
| 3 | `{{key:CMPLX}} {{key:+}}` | $-0.500000$ | $-0.500000$ | $-1.000000$ | $0.000000$ | Complex sum: $a + a^2 = -1.0 + 0.0i$ |
| 4 | `1 {{key:ENTER}} 0 {{key:CMPLX}} {{key:+}}` | $-1.000000$ | $-1.000000$ | **$0.000000$** | **$0.000000$** | Add $+1$ reference: $1 + a + a^2 = 0 + 0i$ |

Returning to Radians mode (`{{key:RAD}}`), complex conjugate pairs also govern the transient response of mechanical suspensions. Consider an underdamped mechanical suspension with sprung mass $m = 2\text{ kg}$, shock-absorber viscous damping $c = 8\text{ N}\cdot\text{s/m}$, and spring stiffness $k = 50\text{ N/m}$. Substituting $x(t) = e^{\lambda t}$ into $m\ddot{x} + c\dot{x} + kx = 0$ yields the complex conjugate eigenvalues $\lambda = -\alpha \pm j\omega_d$:

$$\lambda = -\frac{c}{2m} \pm \sqrt{\left(\frac{c}{2m}\right)^2 - \frac{k}{m}} = -2.0 \pm \sqrt{4 - 25} = -2.0 \pm \sqrt{-21} = -2.0 \pm 4.582576i$$

Computing the real damping rate $\alpha = -c/(2m) = -2.0\text{ s}^{-1}$ in Register $Y$ and the damped ringing frequency $\omega_d = \sqrt{21} \approx \mathbf{4.582576\text{ rad/s}}$ in Register $X$ places the complete complex eigenvalue pair $\lambda = -2.0 \pm 4.5826i$ right on the stack:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `8 {{key:ENTER}} 4 {{key:÷}} {{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-2.0000$ | Real damping factor $\alpha = -c/(2m) = -2.0\text{ s}^{-1}$ |
| 2 | `4 {{key:ENTER}} 25 {{key:-}} {{key:+/-}}` | $0.0000$ | $0.0000$ | $-2.0000$ | $21.0000$ | Discriminant magnitude $\lvert\Delta\rvert = 21.0$ |
| 3 | `{{key:√x}}` | $0.0000$ | $0.0000$ | $-2.0000$ | **$4.582576$** | Damped angular frequency $\omega_d = 4.5826\text{ rad/s}$ |
| 4 | `{{key:SHOW}}` | $0.0000$ | $0.0000$ | **$-2.000000$** | **$4.582576$** | Complex conjugate eigenvalues $\lambda = -2.0 \pm 4.5826i$ |

Look at the physical meaning of the two registers in Step 4: Register $Y$ ($\alpha = -2.0\text{ s}^{-1}$) is the **viscous shock-absorber decay rate** set by oil forced through piston orifices ($c = 8\text{ N}\cdot\text{s/m}$), which dissipates road-impact energy into heat so the chassis settles in $\tau = 1/|\alpha| = 0.50\text{ s}$; Register $X$ ($\omega_d = 4.5826\text{ rad/s}$) is the **reactive ringing frequency** at which kinetic energy in the $2\text{ kg}$ sprung mass and potential energy in the $50\text{ N/m}$ coil spring exchange back and forth $90^\circ$ out of phase. If the shock absorber seals leak ($c \to 0$), the eigenvalue slides horizontally onto the pure imaginary axis ($\lambda = \pm j\omega_n = \pm 5.0i\text{ rad/s}$) and the car bounces indefinitely; if damping is increased to $c_{\text{crit}} = 2\sqrt{mk} = 20\text{ N}\cdot\text{s/m}$ ($\zeta = 1$), the imaginary part in Register $X$ vanishes ($\omega_d = 0$) for deadbeat critical damping.

A similar division between real storage and imaginary collisional loss appears when a spacecraft re-enters the atmosphere wrapped in an ionized plasma sheath (or when shortwave radio bounces off the ionosphere). Free electrons oscillate at the plasma frequency $\omega_p$ while colliding with neutral gas atoms at collision frequency $\nu$. In the Appleton-Hartree Drude model, these collisions make the plasma's relative permittivity $\epsilon_r$ complex:

$$\epsilon_r = 1 - \frac{\omega_p^2}{\omega(\omega - j\nu)}$$

For $\omega_p = 10^7\text{ rad/s}$, wave frequency $\omega = 2 \times 10^7\text{ rad/s}$, and collision rate $\nu = 5 \times 10^6\text{ s}^{-1}$, normalizing all frequencies by $\omega_p = 10^7\text{ rad/s}$ gives $\omega_p = 1, \omega = 2, \nu = 0.5$, so the normalized denominator is $\omega(\omega - j\nu) = 2(2 - 0.5i) = 4.0 - 1.0i$. Inverting $4 - i$ in place via `{{key:CMPLX}} {{key:1/x}}`, negating with `{{key:CMPLX}} {{key:+/-}}`, and adding $1 + 0i$ yields $\epsilon_r = \mathbf{0.764706 - 0.058824i}$ (where the real part $< 1$ bends radio waves via refraction and the imaginary part measures collisional attenuation):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `4 {{key:ENTER}} 1 {{key:+/-}}` | $0.0000$ | $0.0000$ | $4.0000$ | $-1.0000$ | Scaled denominator $z = 4.0 - 1.0i$ |
| 2 | `{{key:CMPLX}} {{key:1/x}} {{key:CMPLX}} {{key:+/-}}` | $0.0000$ | $0.0000$ | $-0.235294$ | $-0.058824$ | Negated reciprocal $-1/(4-i)$ |
| 3 | `1 {{key:ENTER}} 0` | $-0.235294$ | $-0.058824$ | $1.0000$ | $0.0000$ | Unit real reference $1.0 + 0i$ in $(Y, X)$ |
| 4 | `{{key:CMPLX}} {{key:+}}` | $-0.235294$ | $-0.235294$ | **$0.764706$** | **$-0.058824$** | Add unity: $\epsilon_r = 0.7647 - 0.0588i$ |

Even subsonic aerodynamics owes its classic wing profiles to complex reciprocals. How did early aerodynamicists calculate the lift of a curved airplane wing before wind tunnels and supercomputers? In 1910, Russian aviation pioneer Nikolai Zhukovsky (Joukowsky) discovered that the analytic complex mapping $\zeta = z + c^2/z$ **conformally maps** the simple, exact streamline flow around a slightly offset circular cylinder in the $z$-plane into the cambered, rounded-leading-edge, sharp-trailing-edge profile of an aircraft wing in the $\zeta$-plane! Because every differentiable complex function satisfies Laplace's equation ($\nabla^2\phi = 0$), transforming the circle automatically transforms the airflow streamlines around the wing. For a cylinder boundary point $z = 1.1 + 0.2i$ with scale $c = 1.0$, the corresponding airfoil coordinate $\zeta$ follows directly from adding $z$ and its complex reciprocal $1/z$:

$$\frac{1}{z} = \frac{1.1 - 0.2i}{1.21 + 0.04} = \frac{1.1 - 0.2i}{1.25} = 0.88 - 0.16i \implies \zeta = z + \frac{1}{z} = (1.1 + 0.2i) + (0.88 - 0.16i) = \mathbf{1.980000 + 0.040000i}$$

By loading $z = 1.1 + 0.2i$ into both $(T, Z)$ and $(Y, X)$ (`1.1 {{key:ENTER}} 0.2 {{key:ENTER}} 1.1 {{key:ENTER}} 0.2`), inverting $(Y, X)$ in place with `{{key:CMPLX}} {{key:1/x}}` ($\to 0.880000 - 0.160000i$), and adding the two together with `{{key:CMPLX}} {{key:+}}`, the Joukowsky transform maps the cylinder point to the airfoil surface at $(Y = \mathbf{1.980000},\; X = \mathbf{0.040000})$.

---

### RF Transmission Lines, Eigenvalue Audits & Zobel Networks

Our closing trio applies complex square roots, complex squaring, and conjugate admittance cancellation to lossy telegrapher's transmission lines, quadratic complex roots, and constant-resistance Zobel loudspeaker networks. In an ideal lossless coaxial cable ($R' = G' = 0$), the characteristic impedance $Z_0 = \sqrt{L'/C'}$ is a pure real resistance ($50\,\Omega$). In a real physical cable with series copper resistance $R' = 0.1\,\Omega/\text{m}$, inductance $L' = 0.25\,\mu\text{H/m}$, dielectric shunt conductance $G' = 1\,\mu\text{S/m}$, and capacitance $C' = 100\,\text{pF/m}$ operating at $\omega = 10^7\text{ rad/s}$, Oliver Heaviside's telegrapher's equations yield a **complex characteristic impedance**:

$$Z_0 = \sqrt{\frac{R' + j\omega L'}{G' + j\omega C'}} = \sqrt{\frac{0.1 + 2.5i}{10^{-6} + 10^{-3}i}} \approx \mathbf{50.0095 - 0.9748i\,\Omega}$$

Loading the series impedance per meter $Z' = 0.1 + 2.5i$ into $(T, Z)$, the shunt admittance per meter $Y' = 10^{-6} + 10^{-3}i$ into $(Y, X)$, dividing via `{{key:CMPLX}} {{key:÷}}`, and taking the complex square root via `{{key:CMPLX}} {{key:√x}}` reveals how copper loss perturbs $Z_0$ to $\mathbf{50.0095 - 0.9748i\,\Omega}$:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0.1 {{key:ENTER}} 2.5 {{key:ENTER}}` | $0.0000$ | $0.1000$ | $2.5000$ | $2.5000$ | Load series impedance $Z' = 0.1 + 2.5i$ |
| 2 | `1 {{key:E}} 6 {{key:+/-}} {{key:ENTER}} 1 {{key:E}} 3 {{key:+/-}}` | $0.1000$ | $2.5000$ | $1.0000 \times 10^{-6}$ | $1.0000 \times 10^{-3}$ | Load shunt admittance $Y'$ into $(Y, X)$ |
| 3 | `{{key:CMPLX}} {{key:÷}}` | $0.1000$ | $0.1000$ | $2499.9975$ | $-97.4999$ | Complex impedance ratio $Z'/Y'$ |
| 4 | `{{key:CMPLX}} {{key:√x}}` | $0.1000$ | $0.1000$ | **$50.0095$** | **$-0.9748$** | Characteristic impedance $Z_0 = \sqrt{Z'/Y'}$ |

Next, consider how `{{key:CMPLX}} {{key:x²}}` verifies complex conjugate roots of a polynomial before we automate higher-order root finding in Chapter 7. The characteristic polynomial $z^2 - 4z + 13 = 0$ has negative discriminant $\Delta = 16 - 52 = -36$, yielding the complex conjugate roots $z = (4 \pm \sqrt{-36})/2 = 2 \pm 3i$. Let us substitute $z_1 = 2 + 3i$ directly back into $z^2 - 4z + 13$ on the stack to watch the real and imaginary parts cancel simultaneously to zero:

$$(2+3i)^2 - 4(2+3i) + 13 = (-5 + 12i) - (8 + 12i) + 13 = \mathbf{0.0 + 0.0i}$$

Squaring $z_1 = 2 + 3i$ in place (`2 {{key:ENTER}} 3 {{key:CMPLX}} {{key:x²}}` $\to -5 + 12i$), subtracting $4z_1 = 8 + 12i$ (`8 {{key:ENTER}} 12 {{key:CMPLX}} {{key:-}}` $\to -13 + 0i$), and adding $13 + 0i$ (`13 {{key:ENTER}} 0 {{key:CMPLX}} {{key:+}}`) verifies zero residual across both registers ($Y = \mathbf{0.0000},\; X = \mathbf{0.0000}$):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `2 {{key:ENTER}} 3` | $0.0000$ | $0.0000$ | $2.0000$ | $3.0000$ | Candidate complex root $z_1 = 2 + 3i$ loaded |
| 2 | `{{key:CMPLX}} {{key:x²}}` | $0.0000$ | $0.0000$ | $-5.0000$ | $12.0000$ | Complex square $z_1^2 = -5 + 12i$ in place |
| 3 | `8 {{key:ENTER}} 12 {{key:CMPLX}} {{key:-}}` | $-5.0000$ | $-5.0000$ | $-13.0000$ | $0.0000$ | Subtract $4z_1 = 8 + 12i$ |
| 4 | `13 {{key:ENTER}} 0 {{key:CMPLX}} {{key:+}}` | $-13.0000$ | $-13.0000$ | **$0.0000$** | **$0.0000$** | Add $13 + 0i$; residual $= 0.0 + 0.0i$ |

Finally, audio engineers wire a **Zobel impedance-compensation network** ($R - jX_C$) in parallel with an inductive loudspeaker voice coil ($R + jX_L$) so that the amplifier sees a purely resistive load. Let us compute the parallel combination of conjugate branches $Z_1 = 3 + 4i\,\Omega$ and $Z_2 = 3 - 4i\,\Omega$:

$$\frac{1}{Z_{\text{parallel}}} = \frac{1}{3+4i} + \frac{1}{3-4i} = \frac{3-4i}{25} + \frac{3+4i}{25} = \frac{6}{25} \implies Z_{\text{parallel}} = \frac{25}{6} = \mathbf{4.166667\,\Omega}$$

Because the opposite susceptances $\mp 4/25 = \mp 0.16i\,\text{S}$ cancel identically when the two conjugate admittances are added, we only need to invert $Z_1 = 3 + 4i$ (`3 {{key:ENTER}} 4 {{key:CMPLX}} {{key:1/x}}` $\to Y = 0.120000,\; X = -0.160000$), swap the real conductance $G = 0.12\,\text{S}$ into Register $X$ (`{{key:x⇄y}}`), double it (`2 {{key:×}}`), and invert (`{{key:1/x}}`) via `{{res:sc32_05_complex_numbers_phasors_seq_32:keys}}` to obtain $Z_{\text{parallel}} = \mathbf{4.166667\,\Omega}$ (or in one stroke via `3 {{key:ENTER}} 4 {{key:ENTER}} 3 {{key:ENTER}} 4 {{key:+/-}} {{key:CMPLX}} {{key:x∥y}}`):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `3 {{key:ENTER}} 4` | $0.0000$ | $0.0000$ | $3.0000$ | $4.0000$ | Load branch impedance $Z_1 = 3 + 4i$ |
| 2 | `{{key:CMPLX}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.120000$ | $-0.160000$ | Invert: $Y_1 = 0.12 - 0.16i\,\text{S}$ |
| 3 | `{{key:x⇄y}}` | $0.0000$ | $0.0000$ | $-0.160000$ | $0.120000$ | Swap real conductance to Register $X$ |
| 4 | `2 {{key:×}}` | $0.0000$ | $0.0000$ | $-0.160000$ | $0.240000$ | Double conductance (imag parts cancel) |
| 5 | `{{key:1/x}}` | $0.0000$ | $0.0000$ | $-0.160000$ | **$4.166667$** | Invert net conductance: $Z_{\text{parallel}} = 4.1667\,\Omega$ |

---

## Further Exploration: Companion Workbooks & Applied Tie-Ins

> *For 21 additional worked engineering problems with full 4-register stack traces, see Chapter 5 of the [SC-32 Scientific Companion Problem & Casebook Workbook](../../curriculum/sc32-scientific-companion-workbook.md).*


The dual-register complex engine (`{{key:CMPLX}}`) mastered in Chapter 5 powers AC network synthesis, microwave S-parameters, and quantum wave-mechanics across the **StackCalc Engineering & Speed Competition Workbooks**:

- **RF Impedance Matching & Control Systems**: In **[Chapter 13: Applied STEM Case Studies](13-applied-stem-case-studies.md)**, you will combine `{{key:CMPLX}} {{key:x∥y}}`, `{{key:CMPLX}} {{key:1/x}}`, and `{{key:▸θ,r}}` to design L-network Smith Chart impedance matchers, evaluate Bode gain/phase margins, and solve 3-phase fault currents.
- **Characteristic Roots & Eigenvalues**: In **[Chapter 7: Characteristic Polynomials & Brent's Numerical Root Solver](07-polynomials-brent-solver.md)** and **[Chapter 14: Speed & Precision Competition Playbook](14-uil-contest-playbook.md)**, complex conjugate poles emerging from `{{key:POLY}}` flow directly into $(Y, X)$ for frequency-response verification.

### Synthesis Challenge Problems

1. **Zero-Re-Entry Joukowsky Airfoil Map:** Map cylinder coordinate $z = 1.1 + 0.2i$ to $\zeta = z + 1/z$ (from the Joukowsky airfoil analysis above) by loading $z$ into both $(T, Z)$ and $(Y, X)$ before inverting: key `1.1 {{key:ENTER}} 0.2 {{key:ENTER}} 1.1 {{key:ENTER}} 0.2 {{key:CMPLX}} {{key:1/x}} {{key:CMPLX}} {{key:+}}` ($\to Y = \mathbf{1.980000},\; X = \mathbf{0.040000}$).
2. **Single-Keystroke Conjugate Parallel Zobel Network:** Verify the conjugate Zobel loudspeaker network above ($Z_1 = 3 + 4i$ in parallel with $Z_2 = 3 - 4i$) using the native complex parallel key: `3 {{key:ENTER}} 4 {{key:ENTER}} 3 {{key:ENTER}} 4 {{key:+/-}} {{key:CMPLX}} {{key:x∥y}}` ($\to Y = \mathbf{4.166667},\; X = \mathbf{0.000000}$).
3. **Real-Power Equivalence of $i^i$:** Evaluate Euler's famous real value $i^i = e^{-\pi/2} \approx 0.207880$ in `{{key:CMPLX}}` mode by loading $z = 0 + 1i$ into both $(T, Z)$ and $(Y, X)$ and pressing `{{key:CMPLX}} {{key:yˣ}}`: `0 {{key:ENTER}} 1 {{key:ENTER}} 0 {{key:ENTER}} 1 {{key:CMPLX}} {{key:yˣ}}` ($\to Y = \mathbf{0.207880},\; X = \mathbf{0.000000}$).

---

## Summary & Looking Ahead

Chapter 5 unified complex algebra and alternating current phasor analysis on the operational stack. By treating the physical coordinate pair $(Y, X)$ as real and imaginary components ($Y + Xi$), you executed complex arithmetic, inverted reactive admittances, validated Euler's identity ($e^{i\pi} + 1 = 0$), and solved multi-branch impedance networks in place via `{{key:CMPLX}}`. Without scratchpad bookkeeping or complex-mode matrix software, two-dimensional algebraic quantities flowed through the stack with the speed and certainty of real numbers.

Yet every two-dimensional electromagnetic phasor, Linkwitz-Riley audio crossover wave, and damped mechanical oscillation studied in this chapter must ultimately live inside—and radiate from—a **three-dimensional physical structure**: a bass-reflex loudspeaker cabinet, an extruded aluminum RF heat sink, a titanium pressure hull, or a 3D-printed instrument shell. In **[Chapter 6: Analytic & Solid Geometry, Surface Area & Mensuration](06-geometry-surface-area.md)**, we step from the 2D complex plane into 3D physical space to calculate the planar areas, enclosed volumes, rotational moments of inertia, and convective cooling boundaries of those enclosures—using the **Surface Area via Stats Mode (`{{key:Σ+}}`)** technique to accumulate multi-faceted solids on the hardware statistical bus without scratch paper or parentheses.

