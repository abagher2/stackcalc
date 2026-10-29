---
title: "Chapter 5: Complex Numbers, Euler's Identity & Alternating-Current Phasors | Thinking in the Stack (SC-32)"
description: "The geometric discovery of the complex plane, Leonhard Euler's identity, Abraham de Moivre's roots of unity, Charles Proteus Steinmetz's AC phasors, loudspeaker crossovers, and RF transmission lines on the four-register SC-32 complex stack."
---

# Chapter 5: Complex Numbers, Euler's Identity & Alternating-Current Phasors

## Multiplying by i as a Quarter-Turn in the Plane

Few concepts in algebra have been more obscured by historical nomenclature than $\sqrt{-1}$. Because the square of any positive real number is positive ($+3 \times +3 = +9$) and the square of any negative real number is likewise positive ($-3 \times -3 = +9$), no point on the real number line has a negative square. When René Descartes encountered square roots of negative quantities in his 1637 treatise *La Géométrie* {{cite:descartes1637}}, he termed them *"imaginary,"* a label that persisted for four centuries even after complex numbers became central to mathematical physics.

Historically, $\sqrt{-1}$ arose not from quadratic equations, which simply lack real intersections when the parabola lies above the horizontal axis, but from cubic equations whose roots are real. In sixteenth-century Italy, when Scipione del Ferro, Niccolò Fontana (Tartaglia), and Gerolamo Cardano derived the general algebraic solution to the depressed cubic $x^3 = px + q$, they applied it to $x^3 = 15x + 4$. Direct substitution confirms that $x = 4$ is a positive real root ($4^3 = 64 = 15(4) + 4$). Yet substituting the coefficients of $x^3 - 15x - 4 = 0$ into Cardano's formula expressed that real integer as the sum of two radicals involving $\sqrt{-121}$:

$$x = \sqrt[3]{2 + \sqrt{-121}} + \sqrt[3]{2 - \sqrt{-121}}$$

In his 1572 treatise *L'Algebra*, the Italian hydraulic engineer Rafael Bombelli demonstrated that treating $\sqrt{-121}$ as $11\sqrt{-1}$ and applying the ordinary distributive and associative laws of arithmetic resolves the expression consistently. Cubing $(2 + \sqrt{-1})$ with the rule $\left(\sqrt{-1}\right)^2 = -1$ yields $(2 + \sqrt{-1})^3 = 2 + 11\sqrt{-1}$, and cubing the conjugate expression yields $(2 - \sqrt{-1})^3 = 2 - 11\sqrt{-1}$. Extracting the cube roots and summing the two branches cancels the opposite $+\sqrt{-1}$ and $-\sqrt{-1}$ terms:

$$(2 + \sqrt{-1}) + (2 - \sqrt{-1}) = 4$$

Passing from the real coefficients of the cubic to its real root $x = 4$ required algebraic trajectories through a second dimension.

### Wallis, Wessel, Argand, and Gauss: The Perpendicular Direction

The quantity $\sqrt{-1}$ cannot lie on the real line because real numbers span only one dimension, and multiplication by a negative number is geometrically a rotation rather than a reflection. Beginning with John Wallis in 1685 and completed by Caspar Wessel (1797), Jean-Robert Argand (1806), and Carl Friedrich Gauss (1831), mathematicians established the geometric interpretation of complex arithmetic in the plane.

For a unit vector at the origin $0$ directed along the positive real axis toward $+1$ ($0^\circ$), multiplying by $-1$ preserves its unit length while rotating its heading by $180^\circ$ to point along the negative real axis toward $-1$. Multiplying by $-1$ a second time rotates the vector by a further $180^\circ$, completing a $360^\circ$ revolution back to $+1$:

$$(-1) \times (-1) = +1 \quad \Longleftrightarrow \quad 180^\circ + 180^\circ = 360^\circ$$

Interpreting multiplication by $-1$ as a $180^\circ$ half-turn immediately defines $i = \sqrt{-1}$ as a $90^\circ$ counterclockwise quarter-turn. Starting at $i^0 = +1$ along the positive real axis at $0^\circ$, a single multiplication by $i$ rotates the vector $90^\circ$ counterclockwise onto the perpendicular vertical axis at $+i$. A second multiplication ($i \times i = i^2 = -1$) rotates the vector by a second $90^\circ$ quarter-turn ($90^\circ + 90^\circ = 180^\circ$) onto the negative real axis at $-1$; two $90^\circ$ rotations compose into a $180^\circ$ reversal, which is the geometric meaning of $i^2 = -1$. A third quarter-turn ($i^3 = -i$) directs the vector along the negative vertical axis at $270^\circ$, and a fourth quarter-turn ($i^4 = +1$) completes the $360^\circ$ cycle back to $+1$.

Gauss proposed replacing Descartes's term "imaginary" with *lateral unit*. A *complex number* $z = a + bi$ specifies a point or vector in the two-dimensional *Complex Plane* (*Argand Diagram*) through a displacement of $a$ units along the horizontal Real axis and $b$ units along the perpendicular vertical Imaginary axis.

{{blocks:sc32_concept_argand_phasor|Multiplying by i as a 90-degree counterclockwise rotation in the Argand plane, paired with Steinmetz's AC impedance phasor triangle.}}

### Unpeeling Complex Arithmetic and the Conjugate Mirror

Because a complex number $z = a + bi$ is an ordered pair on a two-dimensional plane, the SC-32 holds its horizontal Real component ($a$) in Register $Y$ and its vertical Imaginary component ($b$) in Register $X$, while a second complex operand $z_2 = c + di$ entered into $(Y, X)$ lifts the first operand into $(T = a, Z = b)$. Pressing the transient `{{key:CMPLX}}` prefix (`{{key:↰}}` + `{{key:STO}}`) before `{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`, or `{{key:1/x}}` executes the corresponding two-dimensional operation across the paired registers.

Under complex addition and subtraction (`{{key:CMPLX}} {{key:+}}` and `{{key:CMPLX}} {{key:-}}`), two complex vectors $z_1 = a + bi$ and $z_2 = c + di$ combine by head-to-tail translation, summing their horizontal components and vertical components independently:

$$(a + bi) + (c + di) = (a + c) + (b + d)i$$

Under complex multiplication (`{{key:CMPLX}} {{key:×}}`), expanding the binomial product $(a + bi)(c + di)$ with $i^2 = -1$ groups the two real terms $ac$ and $i^2 bd = -bd$ along the horizontal axis and the two cross-terms $adi$ and $bci$ along the vertical axis:

$$(a + bi)(c + di) = (ac - bd) + (ad + bc)i$$

Complex reciprocals (`{{key:CMPLX}} {{key:1/x}}`) and division (`{{key:CMPLX}} {{key:÷}}`) rely on reflection across the real axis. Every complex number $z = c + di$ has a reflection twin called its *complex conjugate*, $z^* = c - di$, formed by negating the imaginary component with `{{key:+/-}}`. If $z$ lies at angle $+\theta$ relative to the positive real axis, $z^*$ lies at $-\theta$; multiplying $z$ by its conjugate $z^*$ cancels their opposite angles ($\theta - \theta = 0^\circ$) and yields the squared Euclidean modulus $|z|^2 = c^2 + d^2$ as a purely real number:

$$(c + di)(c - di) = c^2 - d^2 i^2 = c^2 + d^2$$

Multiplying the numerator and denominator of a complex quotient $\frac{a + bi}{c + di}$ by the denominator's conjugate $c - di$ reduces the denominator to the real scalar $c^2 + d^2$, which is the algebraic reduction performed by `{{key:CMPLX}} {{key:1/x}}` and `{{key:CMPLX}} {{key:÷}}`:

$$\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{c^2 + d^2} = \left(\frac{ac + bd}{c^2 + d^2}\right) + \left(\frac{bc - ad}{c^2 + d^2}\right)i$$

### Complex Eigenvalues in Damped Springs and Skyscrapers

This orthogonal separation between the horizontal Real axis and the vertical Imaginary axis characterizes linear damped oscillators across mechanical and structural engineering, from vehicle suspension struts to tuned mass dampers in tall buildings.

When a mass $m$ coupled to a spring of stiffness $k$ and a viscous damper of coefficient $c$ is displaced from equilibrium, Newton's second law gives the homogeneous differential equation $m\ddot{x} + c\dot{x} + kx = 0$. Substituting an exponential trial solution $x(t) = e^{\lambda t}$ produces the quadratic characteristic equation $m\lambda^2 + c\lambda + k = 0$, whose roots are the system's *eigenvalues*:

$$\lambda = -\frac{c}{2m} \pm \sqrt{\left(\frac{c}{2m}\right)^2 - \frac{k}{m}} = -\alpha \pm i\omega_d$$

Whenever the restoring stiffness exceeds the damping threshold ($k/m > (c/2m)^2$), the discriminant is negative and the eigenvalues form a complex conjugate pair $\lambda = -\alpha \pm i\omega_d$. The two axes of the complex plane separate the two physical processes acting simultaneously in the oscillator. Along the horizontal Real axis, the attenuation rate $-\alpha = -c/(2m)$ measures irreversible energy dissipation: viscous fluid forced through the damper orifices resists motion in phase with velocity and converts mechanical kinetic energy into heat, so the oscillation envelope decays exponentially as $e^{-\alpha t}$.

Along the vertical Imaginary axis, the damped natural frequency $\pm i\omega_d$ measures lossless quadrature energy exchange: the spring and mass dissipate no heat, exchanging kinetic energy in the moving mass ($\frac{1}{2}mv^2$, which peaks at the equilibrium crossing) with potential energy in the strained spring ($\frac{1}{2}kx^2$, which peaks at the turning points) $90^\circ$ out of phase at angular frequency $\omega_d = \sqrt{k/m - \alpha^2}$.

In the undamped limit ($c \to 0$), the real part $-\alpha$ vanishes, the eigenvalues lie on the imaginary axis ($\lambda = \pm i\sqrt{k/m}$), and the oscillation persists at constant amplitude. At the critical damping threshold $c_{\text{crit}} = 2\sqrt{mk}$, the imaginary part $\omega_d$ vanishes and the displaced mass returns to equilibrium without oscillation.

---

## Euler's Formula and De Moivre's Roots of Unity

Leonhard Euler's constant $e \approx 2.71828$ governs continuous exponential growth and decay along the real line, whereas $\cos\theta$ and $\sin\theta$ parameterize rotation around the unit circle. In his 1748 treatise *Introductio in analysin infinitorum* (building on Roger Cotes's 1714 logarithmic relation $i\theta = \ln(\cos\theta + i\sin\theta)$), Euler evaluated the exponential function $e^z$ for an imaginary argument $z = i\theta$, establishing the fundamental identity of complex analysis:

$$e^{i\theta} = \cos\theta + i\sin\theta$$

Prior to Euler's formulation, exponential functions ($e^x$, logarithms, and compound growth) and circular functions ($\cos\theta, \sin\theta$, and trigonometric tables) were treated as distinct families of transcendental functions. Euler's identity demonstrated that they are orthogonal cross-sections of a single holomorphic function $e^z$ in the complex plane: along the horizontal real axis $e^z$ scales exponentially in magnitude, whereas along the vertical imaginary axis $e^z$ rotates at unit radius around the origin.

### Continuous Imaginary Growth Around the Unit Circle

The unit-circle trajectory of $e^{i\theta}$ follows independently from differential kinematics and from power-series expansion.

In differential kinematics, when a state variable $z(t)$ evolves at a real growth rate $k$, its velocity vector $dz/dt = k \cdot z$ is collinear with the position vector $z$, driving the trajectory radially outward or inward along a straight ray from the origin. Replacing the real rate $k$ with the imaginary rate $i\omega$ gives the differential equation:

$$\frac{dz}{dt} = i\omega z$$

Because multiplication by $i$ rotates any complex vector by $90^\circ$ counterclockwise, the velocity vector $dz/dt$ of $z(t) = e^{i\omega t}$ is at every instant perpendicular ($90^\circ$) to the radius vector $z(t)$, identical to the tangential velocity of uniform circular motion. Because a velocity orthogonal to the radius performs zero radial work and changes the radial distance at rate $\frac{d}{dt}|z|^2 = 0$, the modulus remains invariant at $|e^{i\theta}| = 1$ for all real $\theta$, while the point traces the unit circle with horizontal projection $\cos\theta$ and vertical projection $i\sin\theta$.

Algebraically, substituting $x = i\theta$ into the Maclaurin series for $e^x$ and reducing the powers $i^2 = -1$, $i^3 = -i$, and $i^4 = +1$ yields:

$$e^{i\theta} = 1 + i\theta + \frac{(i\theta)^2}{2!} + \frac{(i\theta)^3}{3!} + \frac{(i\theta)^4}{4!} + \frac{(i\theta)^5}{5!} + \dots$$

Separating the real even-power terms from the imaginary odd-power terms recovers the Maclaurin series for cosine and sine:

$$e^{i\theta} = \underbrace{\left(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \frac{\theta^6}{6!} + \dots\right)}_{\cos\theta} + i\underbrace{\left(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \frac{\theta^7}{7!} + \dots\right)}_{\sin\theta} = \cos\theta + i\sin\theta$$

Evaluating Euler's formula at a half-revolution $\theta = \pi\text{ radians}$ ($180^\circ$), where $\cos\pi = -1$ and $\sin\pi = 0$, gives $e^{i\pi} = -1$, or in homogeneous form:

$$e^{i\pi} + 1 = 0$$

connecting the additive identity $0$, the multiplicative identity $1$, the circle constant $\pi$, the base of natural logarithms $e$, and the imaginary unit $i$. Applying `{{key:CMPLX}} {{key:eˣ}}` to $0 + i\pi$ evaluates Euler's formula directly on the stack, while `{{key:CMPLX}} {{key:LN}}` inverts the mapping to return the principal complex logarithm $\ln(-1) = 0 + i\pi$. At a quarter-turn $\theta = \pi/2$, where $i = e^{i\pi/2}$, raising $i$ to the $i$-th power via `{{key:CMPLX}} {{key:yˣ}}` produces a purely real value: $i^i = \left(e^{i\pi/2}\right)^i = e^{i^2 \pi/2} = e^{-\pi/2} \approx 0.207880$.

### Polar Form, Abraham de Moivre's Theorem, and the Roots of Unity

By Euler's formula, any nonzero complex number $z = x + iy$ can be expressed in *polar form* through its Euclidean modulus $r = |z| = \sqrt{x^2 + y^2}$ and its principal argument $\theta = \operatorname{atan2}(y, x)$:

$$z = x + iy = r(\cos\theta + i\sin\theta) = r e^{i\theta} = r\angle\theta$$

Because the coordinate conversion keys `{{key:▸θ,r}}` and `{{key:▸y,x}}` expect $(Y = y, X = x)$, pairing them with `{{key:x⇄y}}` maps between Gaussian complex coordinates $(Y = \text{Real}, X = \text{Imag})$ and polar coordinates $(Y = \theta, X = r)$ without computing the complementary angle $\arctan(\text{Real}/\text{Imag}) = 90^\circ - \theta$.

In polar form $z = r e^{i\theta}$, multiplication, division, and exponentiation follow directly from the laws of exponents. Multiplying two complex numbers $z_1 z_2 = (r_1 e^{i\theta_1})(r_2 e^{i\theta_2}) = (r_1 r_2) e^{i(\theta_1 + \theta_2)}$ multiplies their moduli and adds their phase angles; dividing two complex numbers $z_1 / z_2 = (r_1 / r_2) e^{i(\theta_1 - \theta_2)}$ divides their moduli and subtracts their phase angles. Raising $z = r e^{i\theta}$ to the $n$-th power (`{{key:CMPLX}} {{key:yˣ}}`) yields *Abraham de Moivre's theorem*, $(r e^{i\theta})^n = r^n e^{in\theta}$:

$$\left[r(\cos\theta + i\sin\theta)\right]^n = r^n\left(\cos(n\theta) + i\sin(n\theta)\right)$$

Geometrically, raising a complex number to the $n$-th power raises its modulus to $r^n$ while multiplying its argument by $n$.

Inverting De Moivre's relation to extract an $n$-th root $\sqrt[n]{z}$ explains why an $n$-th degree polynomial equation has $n$ roots in the complex plane. Because adding integer multiples of a full revolution $2k\pi$ ($360^\circ k$) leaves a complex number unchanged ($\theta + 2k\pi$), dividing the angle by $n$ produces $n$ distinct roots spaced at equal angular intervals of $2\pi/n$ around a circle of radius $r^{1/n}$:

$$\sqrt[n]{z} = r^{1/n} \left[\cos\left(\frac{\theta + 2k\pi}{n}\right) + i\sin\left(\frac{\theta + 2k\pi}{n}\right)\right], \qquad k = 0, 1, \dots, n-1$$

Whereas early algebraists conjectured that extracting the square root of $i$ ($\sqrt{i}$) might require a new class of numbers outside the complex plane, Gauss noted that $i = 1\angle 90^\circ$ has modulus $1$ and argument $90^\circ$: its principal square root (`{{key:CMPLX}} {{key:√x}}`) has modulus $\sqrt{1} = 1$ and half the angle, $45^\circ$ ($\pi/4\text{ rad}$), which lies in the complex plane at $\cos 45^\circ + i\sin 45^\circ = \frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2} \approx 0.7071 + 0.7071i$.

Similarly, whereas the equation $z^3 = 1$ has only the single root $1$ on the real line (and $z^3 = -8$ has only $-2$), in the complex plane the three cube roots of unity ($z^3 = 1 = e^{i\cdot 2k\pi}$) lie $360^\circ / 3 = 120^\circ$ apart at the vertices of an equilateral triangle inscribed in the unit circle:

$$1 = 1\angle 0^\circ, \qquad a = 1\angle 120^\circ = -\frac{1}{2} + i\frac{\sqrt{3}}{2}, \qquad a^2 = 1\angle 240^\circ = -\frac{1}{2} - i\frac{\sqrt{3}}{2}$$

Because those three unit vectors are spaced symmetrically at $0^\circ$, $120^\circ$, and $240^\circ$, their vector sum vanishes identically ($1 + a + a^2 = 0$). As Charles LeGeyt Fortescue demonstrated in 1918, this $120^\circ$ three-phase symmetry is the foundational principle of polyphase AC power transmission: in a balanced three-phase network with phase currents displaced by $0^\circ, 120^\circ,$ and $240^\circ$, the instantaneous return currents sum to $1 + a + a^2 = 0$ at the neutral node, so three conductors transmit polyphase power without a fourth return conductor.

### Beyond the Unit Circle: Analytic Continuation and Joukowsky Airfoils

Euler's exponential relations extend the circular trigonometric functions analytically to arbitrary complex arguments $z = x + iy$. For a real angle $x$, $\sin x$ and $\cos x$ are bounded within $[-1, +1]$; combining $e^{ix} = \cos x + i\sin x$ and $e^{-ix} = \cos x - i\sin x$ defines cosine and sine across the entire complex plane:

$$\cos z = \frac{e^{iz} + e^{-iz}}{2}, \qquad \sin z = \frac{e^{iz} - e^{-iz}}{2i}$$

When a complex argument $z = x + iy$ is evaluated via `{{key:CMPLX}} {{key:SIN}}` or `{{key:CMPLX}} {{key:COS}}`, multiplication of $iy$ by $i$ converts the imaginary coordinate into real exponential factors $e^{\mp y}$, coupling circular oscillation in $x$ with hyperbolic scaling ($\cosh y, \sinh y$) in $y$:

$$\sin(x + iy) = \sin x \cosh y + i \cos x \sinh y, \qquad \cos(x + iy) = \cos x \cosh y - i \sin x \sinh y$$

Even when $\cosh y$ drives the magnitudes of $\sin z$ and $\cos z$ well past $[-1, +1]$, *analytic continuation* preserves the Pythagorean identity $\sin^2 z + \cos^2 z = 1$ across the complex plane. For multivalued inverse and fractional-power functions—the complex natural logarithm $\operatorname{Ln}(\mathbf{z}) = \ln|\mathbf{z}| + i\operatorname{Arg}(\mathbf{z})$, the complex square root $\sqrt{\mathbf{z}} = \sqrt{|\mathbf{z}|}\,e^{i\operatorname{Arg}(\mathbf{z})/2}$, and general complex powers $\mathbf{z}^{\mathbf{w}} = e^{\mathbf{w}\operatorname{Ln}(\mathbf{z})}$—the SC-32 follows William Kahan's 1987 specification (*"Branch Cuts for Complex Elementary Functions"*), restricting the principal argument $\operatorname{Arg}(\mathbf{z})$ to $(-\pi, \pi]$ with a branch cut along the negative real axis $(-\infty, 0)$.

This convention guarantees that `{{key:CMPLX}} {{key:√x}}` always maps into the closed right half-plane $\operatorname{Re}(\sqrt{\mathbf{z}}) \ge 0$ (with $\sqrt{-4 + 0i} = 0 + 2i$ on the upper boundary of the cut), while a Nyquist contour crossing the negative real axis $(-\infty, 0)$ exhibits a $2\pi$ phase transition between $+\pi$ and $-\pi$.

Holomorphic complex functions also define *conformal mappings*: at every point where $f'(z) \ne 0$, a complex mapping $w = f(z)$ preserves local angles between intersecting curves and transforms solutions of Laplace's equation ($\nabla^2\phi = 0$) in one geometry into solutions of Laplace's equation in the mapped geometry.

In 1910, Russian aerodynamicist Nikolai Zhukovsky (Joukowsky) used conformal mapping to reduce the two-dimensional potential flow around an aircraft wing to the known potential flow (with circulation $\Gamma$) around a circular cylinder. Evaluating the sum of a complex coordinate $z$ on an offset circle (passing through the critical point $z = +c$ and enclosing $z = -c$) and its scaled reciprocal $c^2/z$ defines the *Joukowsky transformation*:

$$\zeta = z + \frac{c^2}{z}$$

This rational complex map ($\mathbf{z} + c^2 \cdot \frac{1}{\mathbf{z}}$) transforms the offset circle into an airfoil profile through three geometric effects: at the critical point $z = +c$, where the derivative $d\zeta/dz = 1 - c^2/z^2$ vanishes, the smooth circular boundary folds into a sharp trailing edge at $\zeta = +2c$; on the opposite side of the circle extending slightly beyond $z = -c$, the boundary rounds into a blunt leading edge; and displacing the circle's center slightly above the real axis introduces camber along the chord line. Because $\zeta = z + c^2/z$ is conformal everywhere exterior to the circle, it maps the analytical streamlines around the cylinder directly onto the airflow around the cambered wing and forms the mathematical foundation of the *Kutta-Joukowsky Lift Theorem* ($L' = \rho_\infty V_\infty \Gamma$).

---

## Charles Proteus Steinmetz and the War of the Currents

Complex arithmetic entered electrical power engineering in August 1893 at the International Electrical Congress in Chicago. During the preceding decade, the expansion of electrical distribution had centered on the competition between Thomas Edison's direct-current (DC) networks and George Westinghouse and Nikola Tesla's alternating-current (AC) polyphase networks. In a DC network, steady-state analysis required only scalar Ohm's law ($V = I \cdot R$), but because DC voltage could not be stepped up efficiently with static transformers, resistive line losses ($P_{\text{loss}} = I^2 R$) restricted low-voltage DC distribution to short urban radii. Alternating current enabled high-voltage step-up and step-down transformation over long distances, but introduced phase shifts between voltage and current across reactive elements.

In an AC circuit operating at frequency $f = 60\text{ Hz}$ (angular frequency $\omega = 2\pi f$), inductors and capacitors displace voltage and current by $\pm 90^\circ$. In an inductor ($L$, such as a transformer winding or motor coil), Faraday's law of induction states that induced voltage is proportional to the time derivative of current, $v_L(t) = L \frac{di}{dt}$; because $\frac{d}{dt}\sin(\omega t) = \omega\cos(\omega t) = \omega\sin(\omega t + 90^\circ)$, inductor voltage peaks $90^\circ$ ahead of current. Conversely, in a capacitor ($C$, such as parallel dielectric plates or underground cable insulation), charging current is proportional to the time derivative of voltage, $i_C(t) = C \frac{dv}{dt}$, so capacitor voltage lags $90^\circ$ behind current. Calculating steady-state voltages and currents across multi-branch AC networks therefore required solving coupled systems of linear differential equations with sinusoidal forcing:

$$L \frac{d^2 q}{dt^2} + R \frac{dq}{dt} + \frac{1}{C} q = V_0 \cos(\omega t + \phi)$$

At the 1893 Chicago Congress, Charles Proteus Steinmetz presented *"Complex Quantities and Their Use in Electrical Engineering"* {{cite:steinmetz1893}} and showed how Euler's complex exponential reduces steady-state AC differential equations to complex algebra.

### Steinmetz's Phasor Transform: Turning Differential Equations into Algebra

Steinmetz observed that in a linear AC network driven at a single angular frequency $\omega$, every steady-state voltage and current oscillates at that same angular frequency $\omega$. Rather than carrying explicit $\cos(\omega t + \theta)$ time functions through differential equations, Steinmetz represented each sinusoid by a complex number—a *phasor*—encoding its RMS amplitude and initial phase angle relative to a common reference.

Differentiating a rotating complex exponential $e^{j\omega t}$ with respect to time (where electrical engineering denotes the imaginary unit by $j = \sqrt{-1}$ to reserve $i$ for electrical current) multiplies the phasor by $j\omega$:

$$\frac{d}{dt}\left(e^{j\omega t}\right) = j\omega e^{j\omega t}$$

Time differentiation becomes algebraic multiplication by $j\omega$ (a $+90^\circ$ rotation scaled by $\omega$), while time integration becomes division by $j\omega$ (a $-90^\circ$ rotation, since $1/j = -j$).

Under Steinmetz's transformation, the three passive circuit elements map onto the axes of the complex impedance plane. Resistors ($R$) lie along the positive horizontal Real axis as $\mathbf{Z}_R = R + j0\,\Omega$, introducing $0^\circ$ phase shift and converting electrical energy irreversibly into Joule heat. Inductors ($L$) lie along the positive vertical Imaginary axis as $\mathbf{Z}_L = +j X_L = +j\omega L\,\Omega$, introducing a $+90^\circ$ voltage phase lead as magnetic field energy cycles losslessly between the coil and the source. Capacitors ($C$) lie along the negative vertical Imaginary axis as $\mathbf{Z}_C = -j X_C = -j\frac{1}{\omega C}\,\Omega$, introducing a $-90^\circ$ voltage phase lag as electrostatic field energy cycles losslessly between the plates and the source.

For a series RLC branch, the total *complex impedance* $\mathbf{Z}$ is the vector sum of real resistance and net imaginary reactance:

$$\mathbf{Z} = R + j(X_L - X_C) = R + j\left(\omega L - \frac{1}{\omega C}\right)$$

Because inductive reactance points along $+j$ and capacitive reactance points along $-j$, at the angular frequency where $\omega_0 L = \frac{1}{\omega_0 C}$—the *resonant frequency* $f_0 = \frac{1}{2\pi\sqrt{LC}}$—the opposing imaginary reactances cancel to zero and the net impedance reduces to the real resistance $R$.

With complex phasors, AC Ohm's law takes the multiplicative form $\mathbf{V} = \mathbf{I} \cdot \mathbf{Z}$, series impedances add directly ($\mathbf{Z}_{\text{series}} = \mathbf{Z}_1 + \mathbf{Z}_2$), and parallel impedances combine either by summing their reciprocal *complex admittances* ($\mathbf{Y} = 1/\mathbf{Z} = G + jB$, with conductance $G$ and susceptance $B$ in Siemens) or by applying the complex parallel operator `{{key:CMPLX}} {{key:x∥y}}` {{cite:horowitz2015}}:

$$\mathbf{Z}_{\text{parallel}} = \mathbf{Z}_1 \parallel \mathbf{Z}_2 = \frac{1}{\frac{1}{\mathbf{Z}_1} + \frac{1}{\mathbf{Z}_2}} = \frac{\mathbf{Z}_1 \mathbf{Z}_2}{\mathbf{Z}_1 + \mathbf{Z}_2}$$

### The Complex Power Triangle, Power Factor Correction, and Maximum Power Transfer

Steinmetz's complex representation also resolved an accounting anomaly in early AC power distribution: industrial plants containing large induction motors drew high line currents from utility feeders while registering lower real power consumption on wattmeters.

When an AC source delivers an RMS voltage phasor $\mathbf{V} = |\mathbf{V}|\angle\theta_v$ and an RMS current phasor $\mathbf{I} = |\mathbf{I}|\angle\theta_i$ to an inductive load $\mathbf{Z} = R + jX_L = |\mathbf{Z}|\angle\theta$ (where $\theta = \theta_v - \theta_i$ is the phase lag of current behind voltage), the phase-invariant power product requires complex conjugation. Multiplying $\mathbf{V}$ by $\mathbf{I}$ without conjugation sums their phase angles ($\theta_v + \theta_i$), which varies with the arbitrary choice of time origin $t = 0$. Defining *complex apparent power* $\mathbf{S}$ (in Volt-Amperes, VA) as the product of the voltage phasor $\mathbf{V}$ and the complex conjugate of the current phasor, $\mathbf{I}^* = |\mathbf{I}|\angle(-\theta_i)$, isolates the physical phase difference $\theta = \theta_v - \theta_i$:

$$\mathbf{S} = \mathbf{V} \cdot \mathbf{I}^* = |\mathbf{V}||\mathbf{I}|\angle(\theta_v - \theta_i) = |\mathbf{S}|\cos\theta + j|\mathbf{S}|\sin\theta = P + jQ$$

This complex product defines the right-angled *Power Triangle* $\mathbf{S} = P + jQ$ in the complex plane. The horizontal real leg is the *real (active) power* $P = |\mathbf{V}||\mathbf{I}|\cos\theta = |\mathbf{I}|^2 R$ (in Watts, $\text{W}$), representing the rate at which electrical energy is converted into mechanical shaft work—driving lathe spindles, hoists, and pumps—or dissipated as heat; the dimensionless cosine ratio $\text{PF} = \cos\theta = P / |\mathbf{S}|$ is the *power factor*.

The vertical imaginary leg is the *reactive (quadrature) power* $Q = |\mathbf{V}||\mathbf{I}|\sin\theta = |\mathbf{I}|^2 X$ (in Volt-Amperes Reactive, $\text{VAR}$), measuring the peak rate of lossless energy oscillation twice per AC cycle between the generator and the magnetic fields of inductive loads ($Q > 0$) or the electric fields of capacitive loads ($Q < 0$). Although reactive power performs zero net work over a complete cycle, utility transmission lines must carry the associated quadrature current, incurring real $I^2 R_{\text{line}}$ resistive losses in the distribution grid.

The hypotenuse of the triangle is the *apparent power* $|\mathbf{S}| = \sqrt{P^2 + Q^2} = |\mathbf{V}||\mathbf{I}|$ (in Volt-Amperes, $\text{VA}$); because substation transformers and alternators must be insulated for total voltage $|\mathbf{V}|$ and sized to conduct total current $|\mathbf{I}|$ regardless of phase angle, power equipment is rated in $\text{kVA}$ or $\text{MVA}$ rather than kilowatts. Industrial facilities eliminate quadrature line current through *power factor correction*. Because an induction motor draws lagging reactive power $+jQ_L$, connecting a shunt capacitor bank of equal and opposite leading reactive power $-jQ_C = -jQ_L$ in parallel across the load bus supplies the oscillating magnetic energy locally, canceling the imaginary component $j(Q_L - Q_C) = 0$ so the utility feeder sees a purely resistive load at unity power factor ($\cos 0^\circ = 1.000$).

In low-power RF communications, acoustic transducers, and instrumentation, the design objective shifts from minimizing transmission losses to extracting the maximum real power $P_{\text{load}}$ from a source with fixed internal Thévenin impedance $\mathbf{Z}_{\text{source}} = R_s + jX_s$. Terminating the source with a load $\mathbf{Z}_{\text{load}} = R_L + jX_L$ produces loop current magnitude $|\mathbf{I}| = \frac{|\mathbf{V}_s|}{\sqrt{(R_s + R_L)^2 + (X_s + X_L)^2}}$ and real load power:

$$P_{\text{load}} = |\mathbf{I}|^2 R_L = \frac{|\mathbf{V}_s|^2 R_L}{(R_s + R_L)^2 + (X_s + X_L)^2}$$

Because $(X_s + X_L)^2 \ge 0$ in the denominator, real power is maximized for any $R_L$ by choosing the load reactance equal and opposite to the source reactance ($X_L = -X_s$), canceling the net series reactance to zero. Differentiating the remaining resistive ratio $\frac{R_L}{(R_s + R_L)^2}$ with respect to $R_L$ shows that maximum power occurs when $R_L = R_s$. Combining both conditions ($R_L = R_s$ and $X_L = -X_s$) yields the *Complex Conjugate Maximum Power Transfer Theorem*:

$$\mathbf{Z}_{\text{load}} = R_s - jX_s = \mathbf{Z}_{\text{source}}^*$$

Maximum real power transfer occurs when the load impedance equals the complex conjugate of the source impedance.

### Audio Filters, Linkwitz-Riley Crossovers, and Zobel Compensation

Complex impedance algebra also governs electroacoustic loudspeaker crossovers and impedance-compensation networks {{cite:horowitz2015}}. A moving-coil loudspeaker driver is not a pure $8\,\Omega$ resistance: the copper voice coil wound around the magnet pole piece introduces series inductance ($R + j\omega L$) that causes the driver impedance to rise at high audio frequencies. Flattening that inductive rise requires wiring a conjugate *Zobel compensation network* ($R - jX_C$) in parallel with the driver terminals. When two conjugate impedances $Z_1 = R + jX$ and $Z_2 = R - jX$ are connected in parallel, their opposite susceptances $\mp jX / (R^2 + X^2)$ sum to zero and leave a purely real conductance $2G = \frac{2R}{R^2 + X^2}$ with equivalent resistance $Z_{\text{eq}} = \frac{R^2 + X^2}{2R}$.

In multi-way loudspeaker design, dividing the audio spectrum between a low-frequency woofer and a high-frequency tweeter requires matching both amplitude and phase at the crossover frequency. In 1930, British engineer Stephen Butterworth derived the maximally flat second-order low-pass transfer function $H(s) = \frac{1}{s^2 + \sqrt{2}s + 1}$. At the normalized crossover frequency $s = j\omega/\omega_c = j$, the $s^2 = j^2 = -1$ term and the $+1$ constant in the denominator cancel:

$$H_{\text{Butter2}}(j) = \frac{1}{(-1 + 1) + j\sqrt{2}} = \frac{1}{j\sqrt{2}} = -\frac{j}{\sqrt{2}} \approx 0 - 0.707107j \quad (-3.01\text{ dB}, \text{ phase } -90^\circ)$$

If a single second-order Butterworth low-pass filter feeds the woofer and its high-pass complement $\frac{s^2}{s^2 + \sqrt{2}s + 1}$ feeds the tweeter, the low-pass output lags by $-90^\circ$ ($-j/\sqrt{2}$) at crossover while the high-pass output leads by $+90^\circ$ ($+j/\sqrt{2}$). Because $-90^\circ$ and $+90^\circ$ differ by $180^\circ$, the two acoustic outputs sum to zero at the crossover frequency when connected with identical polarity.

In 1976, Siegfried Linkwitz and Russ Riley resolved this phase opposition by cascading two second-order Butterworth sections in series to form a fourth-order *Linkwitz-Riley* (`LR4`) crossover, squaring the complex transfer function at the crossover frequency:

$$H_{\text{LR4}}(j) = \left[H_{\text{Butter2}}(j)\right]^2 = \left(-\frac{j}{\sqrt{2}}\right)^2 = \frac{j^2}{2} = -0.5000 + 0.0000j \quad (-6.02\text{ dB}, \text{ phase } -180^\circ)$$

At crossover, both the low-pass and high-pass outputs have magnitude $|H| = 0.5$ ($-6.02\text{ dB}$) and identical phase ($-180^\circ$), so their acoustic outputs sum in phase to unity ($0.5 + 0.5 = 1.0$, or $0\text{ dB}$).

### Coaxial Transmission Lines, Standing Waves, and Phillip Smith's Chart

At radio and microwave frequencies where the signal wavelength is comparable to or shorter than the interconnecting conductors, a transmission line acts as a distributed network of series impedance per unit length ($Z' = R' + j\omega L'$) and shunt admittance per unit length ($Y' = G' + j\omega C'$). Oliver Heaviside's telegrapher's equations combine these distributed parameters into the line's *characteristic impedance*:

$$Z_0 = \sqrt{\frac{R' + j\omega L'}{G' + j\omega C'}}$$

When an electromagnetic wave propagating along a feedline of characteristic impedance $Z_0 = 50\,\Omega$ encounters a load or antenna whose complex impedance $\mathbf{Z}_L = R_L + jX_L$ differs from $Z_0$, a portion of the incident wave reflects back toward the source. In 1939, Bell Telephone Laboratories engineer Phillip H. Smith observed that the complex *voltage reflection coefficient* $\mathbf{\Gamma}$ (denoted $S_{11}$ in scattering-parameter measurements):

$$\mathbf{\Gamma} = \frac{\mathbf{Z}_L - Z_0}{\mathbf{Z}_L + Z_0}$$

maps the entire right half-plane of passive impedances ($R_L \ge 0$) onto the unit disk $|\mathbf{\Gamma}| \le 1$, forming the *Smith Chart*. Subtracting $Z_0$ from the real part $R_L$ while recovering $Z_0$ via `{{key:LASTX}}` constructs both $\mathbf{Z}_L - Z_0$ and $\mathbf{Z}_L + Z_0$ for `{{key:CMPLX}} {{key:÷}}`. Converting $\mathbf{\Gamma}$ to polar magnitude $|\mathbf{\Gamma}|$ via `{{key:x⇄y}} {{key:▸θ,r}}` yields both the *return loss* ($\text{RL} = -20\log_{10}|\mathbf{\Gamma}|$ in dB) and the *voltage standing wave ratio* ($\text{VSWR}$):

$$\text{VSWR} = \frac{1 + |\mathbf{\Gamma}|}{1 - |\mathbf{\Gamma}|}$$

To match a resistive antenna load $Z_L$ to a transmission line $Z_0$ without reflection, an RF designer inserts a quarter-wavelength ($\lambda/4$) transformer section whose characteristic impedance is the geometric mean $Z_{\text{line}} = \sqrt{Z_0 Z_L}$, which maps the input impedance to $Z_{\text{in}} = Z_{\text{line}}^2 / Z_L = Z_0$ in exact analogy to a quarter-wave optical anti-reflection coating of refractive index $n_{\text{film}} = \sqrt{n_{\text{air}} n_{\text{glass}}}$.

---

## Gaussian Complex Pairs & Alternating-Current Phasors

Where the 1982 HP-15C hid imaginary components inside a separate parallel stack {{cite:hp15c1982}} and the single-line 1991 HP-32SII stored $(Y = \text{Imag}, X = \text{Real})$ (so that $a + bi$ had to be keyed backward as `b ENTER a`), the four-line StackCalc SC-32 pairs $(Y = \text{Real}, X = \text{Imag})$ across the lower two registers of the display. Keying `a {{key:ENTER}} b` in natural left-to-right reading order places the horizontal Real part $a$ on Line $Y$ and the vertical Imaginary part $b$ on Line $X$.

Pushing a second complex number $c + di$ onto the stack via `a {{key:ENTER}} b {{key:ENTER}} c {{key:ENTER}} d` lifts the first operand into Registers $(T = a, Z = b)$ while the second operand occupies $(Y = c, X = d)$, holding both complex vectors in plain sight simultaneously. Tapping the transient `{{key:CMPLX}}` prefix (`{{key:↰}}` + `{{key:STO}}`) before any arithmetic (`{{key:×}}`, `{{key:÷}}`, `{{key:+}}`, `{{key:-}}`, `{{key:x∥y}}`), power, or trigonometric key executes the full two-dimensional operation across $(T, Z)$ and $(Y, X)$ and writes the result to $(Y = \text{Real}, X = \text{Imag})$ without locking the calculator into a separate complex mode.

{{res:sc32_phasor_polar:screenshot|Impedance phasor 3 + j4 rectangular-to-polar conversion on the SC-32, resolving magnitude r = 5 in Register X and phase angle theta = 53.1301 deg in Register Y.}}

### Pairing Two Complex Numbers Across Four Registers

Within each adjacent register pair, the upper line holds the real projection and the lower line holds the imaginary projection:

$$\mathbf{z} = Y + X i$$

| Register / Display | Complex Plane Component | Mathematical Notation | Display Appearance ($z = a + bi$) |
| :--- | :--- | :---: | :--- |
| **Register $Y$ (Line 2)** | Real Part | $\operatorname{Re}(\mathbf{z})$ | $a$ (Upper line on transflective LCD) |
| **Register $X$ (Line 1)** | Imaginary Part | $\operatorname{Im}(\mathbf{z})$ | $b$ (Active prompt line on transflective LCD) |

Pressing `{{key:C}}` cancels the transient `{{key:CMPLX}}` prefix if tapped by mistake, and complex trigonometric and exponential operations evaluate in radian mode (`{{key:RAD}}`) unless degrees (`{{key:DEG}}`) are selected. Internally, direct unscaled complex division $\frac{a+bi}{c+di} = \frac{(ac+bd) + i(bc-ad)}{c^2+d^2}$ fails whenever $|c|$ or $|d|$ exceeds $\sqrt{\Omega_{\max}} \approx 1.34 \times 10^{154}$, because squaring $c^2 + d^2$ overflows to $\infty$ even when the quotient itself is near unity. To prevent premature overflow above $10^{154}$ or underflow below $10^{-154}$, `{{key:CMPLX}} {{key:÷}}` and `{{key:CMPLX}} {{key:1/x}}` implement Robert L. Smith's 1962 *Algorithm 116* scaling pivot:

$$\frac{a + bi}{c + di} = \begin{cases} \dfrac{a + b(d/c)}{c + d(d/c)} + i\,\dfrac{b - a(d/c)}{c + d(d/c)} & \text{if } |c| \ge |d|, \\[10pt] \dfrac{a(c/d) + b}{c(c/d) + d} + i\,\dfrac{b(c/d) - a}{c(c/d) + d} & \text{if } |d| > |c|. \end{cases}$$

By always forming the smaller-over-larger ratio $r = d/c$ or $r = c/d$ so that $|r| \le 1$, every intermediate product stays bounded within the native exponent range of the operands.

Similarly, `{{key:CMPLX}} {{key:√x}}` avoids catastrophic cancellation in $\sqrt{\frac{|z| + a}{2}}$ when $a < 0$ by evaluating the larger root component first from the scaled hypotenuse $|z| = \operatorname{hypot}(a, b)$ and recovering the smaller component by division:

$$\sqrt{a + bi} = \begin{cases} \sqrt{\dfrac{|z| + a}{2}} + i\,\dfrac{b}{2\sqrt{(|z| + a)/2}} & \text{if } a \ge 0, \\[10pt] \dfrac{|b|}{2\sqrt{(|z| - a)/2}} + i\,\operatorname{sgn}(b)\sqrt{\dfrac{|z| - a}{2}} & \text{if } a < 0. \end{cases}$$

Because one complex number occupies two adjacent registers, the four-register stack holds two complete complex numbers simultaneously—$\mathbf{z}_2 = T + Zi$ in the upper pair $(T, Z)$ and $\mathbf{z}_1 = Y + Xi$ in the lower pair $(Y, X)$:

| Operation Class | Key Sequence | Input Stack | Output in $(Y, X)$ | Upper Stack $(T, Z)$ |
| :--- | :--- | :--- | :--- | :--- |
| **Complex Negation** | `{{key:CMPLX}} {{key:+/-}}` | $\mathbf{z}_1 = Y + Xi$ | $-Y - Xi$ | Preserved ($T, Z$ unchanged) |
| **Unary Complex Functions** | `{{key:CMPLX}}` + `{{key:√x}}`, `{{key:1/x}}`, `{{key:x²}}`, `{{key:eˣ}}`, `{{key:LN}}`, `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}` | $\mathbf{z}_1 = Y + Xi$ | $f(\mathbf{z}_1)$ | Preserved ($T, Z$ unchanged) |
| **Binary Complex Arithmetic** | `{{key:CMPLX}}` + `{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`, `{{key:yˣ}}` | $\mathbf{z}_2 = T + Zi$, $\mathbf{z}_1 = Y + Xi$ | $\mathbf{z}_2 \mathbin{\text{op}} \mathbf{z}_1$ | 2-level drop ($T \to Z, T$) |
| **Complex Parallel Impedance** | `{{key:CMPLX}} {{key:x∥y}}` | $\mathbf{z}_2 = T + Zi$, $\mathbf{z}_1 = Y + Xi$ | $\dfrac{\mathbf{z}_2 \mathbf{z}_1}{\mathbf{z}_2 + \mathbf{z}_1}$ | 2-level drop ($T \to Z, T$) |

This register architecture highlights the distinction between *unary* and *dyadic* complex operations. Whereas the 1982 HP-15C stored imaginary components in a hidden parallel stack accessed via `Re⇄Im`, and the 1-line HP-32SII required tapping `x⇄y` to peek at the real part in Register $Y$, the SC-32's four-line LCD displays both $\operatorname{Re}(\mathbf{z}_1)$ in Register $Y$ and $\operatorname{Im}(\mathbf{z}_1)$ in Register $X$ simultaneously alongside $\mathbf{z}_2 = T + Zi$ in $(T, Z)$.

Because a single complex number $\mathbf{z}_1 = Y + Xi$ lives entirely in the lower two registers of the stack, unary complex operators (such as `{{key:CMPLX}} {{key:eˣ}}`, `LN`, `√x`, `x²`, and `1/x`) transform `Register Y` (Real) and `Register X` (Imaginary) in place while `Register Z` and `Register T` remain untouched, so a second complex number can wait in the upper registers. Dyadic complex operators (such as `{{key:CMPLX}} {{key:×}}`, `÷`, `yˣ`, and `x∥y`), by contrast, engage all four registers simultaneously as two coupled two-dimensional Argand planes, combining $\mathbf{z}_2 = T + Zi$ and $\mathbf{z}_1 = Y + Xi$ into a single complex result in $(Y, X)$.

Because each complex number consumes two real registers, a classic four-register stack (`4-LVL`) acts as a *two-level* complex stack ($\mathbf{z}_1$ in $Y, X$ and $\mathbf{z}_2$ in $T, Z$). Whenever a multi-branch AC network requires holding three or four complex phasors in flight simultaneously, switching `{{key:FLAGS}}` $\to$ `STACK` $\to$ `{{key:8-LVL}}` expands the real stack to eight registers ($R_1\text{--}R_8$), transforming `{{key:CMPLX}}` mode into a true **four-level complex stack** ($\mathbf{z}_1$ in $Y, X$; $\mathbf{z}_2$ in $T, Z$; $\mathbf{z}_3$ in $R_6, R_5$; and $\mathbf{z}_4$ in $R_8, R_7$).

Five complex traces illustrate how $(Y, X)$ and $(T, Z)$ operate together:

* **Damped Mechanical Suspension Eigenvalues ($\lambda = -\frac{c}{2m} \pm i\sqrt{\frac{k}{m} - \left(\frac{c}{2m}\right)^2}$):**
  For an underdamped mechanical shock-absorber suspension ($m = 2\text{ kg}$, so $2m = 4\text{ kg}$; viscous damping $c = 8\text{ N}\cdot\text{s/m}$; spring stiffness $k = 50\text{ N/m}$, so $\omega_0^2 = k/m = 25\text{ s}^{-2}$), the characteristic eigenvalues are $\lambda = -2.0 \pm i\sqrt{25 - 4} = -2.0 \pm i\sqrt{21} \approx -2.0 \pm 4.582576i$. Keying `8 {{key:ENTER}} 4 {{key:÷}} {{key:+/-}}` evaluates the horizontal energy-dissipation rate $\sigma = -\alpha = \mathbf{-2.0000\text{ s}^{-1}}$ in Register $X$. Keying `4 {{key:ENTER}} 25 {{key:-}} {{key:+/-}}` then forms the net oscillatory variance $\omega_0^2 - \alpha^2 = 21.0000\text{ s}^{-2}$ in Register $X$ while lifting the real part $\sigma = -2.0000$ into Register $Y$, and pressing `{{key:√x}}` extracts the vertical damped ringing frequency $\omega_d = \sqrt{21} = \mathbf{4.582576\text{ rad/s}}$ in Register $X$ so the complete eigenvalue pair $Y = -2.000000,\; X = 4.582576$ occupies the lower two registers.

* **Verifying a Complex Quadratic Root ($z^2 - 4z + 13 = 0$ at $z_1 = 2 + 3i$):**
  As soon as we step from assembling a single eigenvalue to verifying a complex root inside $z^2 - 4z + 13 = 0$, both complex register pairs $(T, Z)$ and $(Y, X)$ come into play. Expanding $(2+3i)^2 - 4(2+3i) + 13$ algebraically gives $(-5 + 12i) - (8 + 12i) + 13 = 0 + 0i$. On the stack, squaring $2 + 3i$ in place via `2 {{key:ENTER}} 3 {{key:CMPLX}} {{key:x²}}` transforms $(Y, X)$ into $z_1^2 = -5 + 12i$; keying the linear term `8 {{key:ENTER}} 12` then lifts $-5 + 12i$ into $(T, Z)$ so `{{key:CMPLX}} {{key:-}}` and `13 {{key:ENTER}} 0 {{key:CMPLX}} {{key:+}}` combine both 2D vectors across all four registers:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2 {{key:ENTER}} 3` | $0.0000$ | $0.0000$ | $2.0000$ | $3.0000$ | Candidate complex root $z_1 = 2 + 3i$ loaded |
| `{{key:CMPLX}} {{key:x²}}` | $0.0000$ | $0.0000$ | $-5.0000$ | $12.0000$ | Complex square $z_1^2 = -5 + 12i$ in place |
| `8 {{key:ENTER}} 12 {{key:CMPLX}} {{key:-}}` | $-5.0000$ | $-5.0000$ | $-13.0000$ | $0.0000$ | Subtract $4z_1 = 8 + 12i$ |
| `13 {{key:ENTER}} 0 {{key:CMPLX}} {{key:+}}` | $-13.0000$ | $-13.0000$ | **$0.0000$** | **$0.0000$** | Add $13 + 0i$; residual $= 0.0 + 0.0i$ |

* **Multiplying a Complex Number by Its Conjugate Twin ($z \cdot \bar{z} = (6 + 8i)(6 - 8i)$):**
  When we multiply $z = 6 + 8i$ in $(T, Z)$ by its complex conjugate $z^* = 6 - 8i$ in $(Y, X)$, their opposite phase angles cancel and leave the squared Euclidean norm $6^2 + 8^2 = 100 + 0i$:
  * **Conjugate Norm Product:** `{{res:sc32_05_complex_numbers_phasors_seq_08:keys}}` $\to (Y = 100.0000,\; X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_08:value}}})$.

* **Spacecraft Re-Entry Plasma Permittivity ($\epsilon_r = 1 - \frac{\omega_p^2}{\omega(\omega - j\nu)}$):**
  That conjugate mechanism powers `{{key:CMPLX}} {{key:1/x}}` when modeling hypersonic re-entry plasma blackout. For normalized plasma frequency $\omega_p = 1$, wave frequency $\omega = 2$, and electron collision rate $\nu = 0.5$, the denominator is $\omega(\omega - j\nu) = 4.0 - 1.0i$. Inverting $4 - i$ in place on $(Y, X)$ via `{{key:CMPLX}} {{key:1/x}}`, negating with `{{key:CMPLX}} {{key:+/-}}`, and keying `1 {{key:ENTER}} 0` lifts $-0.235294 - 0.058824i$ into $(T, Z)$ so `{{key:CMPLX}} {{key:+}}` resolves $\epsilon_r = \mathbf{0.764706 - 0.058824i}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4 {{key:ENTER}} 1 {{key:+/-}}` | $0.0000$ | $0.0000$ | $4.0000$ | $-1.0000$ | Scaled denominator $z = 4.0 - 1.0i$ |
| `{{key:CMPLX}} {{key:1/x}} {{key:CMPLX}} {{key:+/-}}` | $0.0000$ | $0.0000$ | $-0.235294$ | $-0.058824$ | Negated reciprocal $-1/(4-i)$ |
| `1 {{key:ENTER}} 0` | $-0.235294$ | $-0.058824$ | $1.0000$ | $0.0000$ | Unit real reference $1.0 + 0i$ in $(Y, X)$ |
| `{{key:CMPLX}} {{key:+}}` | $-0.235294$ | $-0.235294$ | **$0.764706$** | **$-0.058824$** | Add unity: $\epsilon_r = 0.7647 - 0.0588i$ |

* **Conformal Joukowsky Airfoil Map ($\zeta = z + 1/z$ at $z = 1.1 + 0.2i$):**
  Because unary complex operators leave $(T, Z)$ undisturbed, keying `1.1 {{key:ENTER}} 0.2 {{key:ENTER}} 1.1 {{key:ENTER}} 0.2` loads $z$ into both $(T, Z)$ and $(Y, X)$; pressing `{{key:CMPLX}} {{key:1/x}}` inverts only the lower pair $(Y, X) \to 0.880000 - 0.160000i$ while the uninverted $z = 1.1 + 0.2i$ waits in $(T, Z)$, and pressing `{{key:CMPLX}} {{key:+}}` sums them to land at the cambered wing coordinate $(Y = \mathbf{1.980000},\; X = \mathbf{0.040000})$.

### Evaluating Euler's Identity on the Complex Stack

Because `{{key:CMPLX}} {{key:eˣ}}` and `{{key:CMPLX}} {{key:LN}}` are unary complex functions, they transform a complex argument $\mathbf{z} = x + iy$ in place across $(Y, X)$ according to $e^{x + iy} = e^x\cos y + i e^x\sin y$ without disturbing Registers $Z$ and $T$. With the SC-32 in Radians mode (`{{key:RAD}}`), we can verify Euler's formula $e^{i\pi} = -1 + 0i$, Euler's identity $e^{i\pi} + 1 = 0$, and the principal complex logarithm $\operatorname{Ln}(-1) = 0 + i\pi$ in three crisp steps:
* **Half-Turn Rotation ($e^{0 + i\pi}$):** Place the real growth rate $x = 0$ in Register $Y$ and radian angle $y = \pi$ in Register $X$, then fire `{{key:CMPLX}} {{key:eˣ}}`:
  `{{res:sc32_05_complex_numbers_phasors_seq_01:keys}}` $\to (Y = \mathbf{-1.0000000000},\; X = \mathbf{0.0000000000})$.
* **Euler's Five-Constant Identity ($e^{i\pi} + 1 = 0$):** Add the unit real vector $+1 + 0i$ across all four registers:
  `{{res:sc32_05_complex_numbers_phasors_seq_30:keys}}` $\to$ `{{res:sc32_05_complex_numbers_phasors_seq_30:value}}` ($Y = \mathbf{0.0000000000},\; X = \mathbf{0.0000000000}$).
* **Principal Complex Logarithm ($\operatorname{Ln}(-1)$):** Evaluate $e^{i\pi} = -1 + 0i$ and immediately invert it in place via `{{key:CMPLX}} {{key:LN}}` onto the upper lip of William Kahan's branch cut:
  `{{res:sc32_05_complex_numbers_phasors_seq_31:keys}}` $\to (Y = \mathbf{0.0000000000},\; X = \mathbf{3.1415926536})$.

### De Moivre Powers, Roots of Unity & Complex Trigonometry

The Euclidean vector keys `{{key:▸θ,r}}` and `{{key:▸y,x}}` expect vertical $y$ in Register $Y$ and horizontal $x$ in Register $X$. Because Gaussian complex format places Real ($x$) in Register $Y$ and Imaginary ($y$) in Register $X$, `{{key:x⇄y}}` is the one-keystroke bridge between Gaussian complex $(Y = \text{Real}, X = \text{Imag})$ and polar $(\theta, r)$ coordinates: pressing `{{key:x⇄y}} {{key:▸θ,r}}` converts Complex $(Y = \text{Real}, X = \text{Imag})$ to Polar $(Y = \theta, X = r)$, and pressing `{{key:▸y,x}} {{key:x⇄y}}` converts Polar $(Y = \theta, X = r)$ back to Complex $(Y = \text{Real}, X = \text{Imag})$. Swapping with `{{key:x⇄y}}` before `{{key:▸θ,r}}` and after `{{key:▸y,x}}` avoids the *complementary angle trap*, where pressing `{{key:▸θ,r}}` on $(Y = \text{Real}, X = \text{Imag})$ without swapping first computes $\operatorname{atan2}(\text{Real}, \text{Imag}) = 90^\circ - \theta$.

Converting $\mathbf{z} = 3 + 4i$ to polar coordinates and back in `{{key:RAD}}` mode (where $\theta = 0.927295\text{ rad}$ equals $\theta = 53.1301^\circ$ in `{{key:DEG}}` mode) proceeds in four steps:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3 {{key:ENTER}} 4` | $0.0000$ | $0.0000$ | $3.0000$ | $4.0000$ | Gaussian complex coordinates $(Y=\text{Real}, X=\text{Imag})$ |
| `{{key:x⇄y}} {{key:▸θ,r}}` | $0.0000$ | $0.0000$ | $0.927295$ | **$5.000000$** | Polar conversion: $\theta = 0.9273\text{ rad}$ ($53.1301^\circ$) in $Y$, magnitude $r$ in $X$ |
| `{{key:▸y,x}}` | $0.0000$ | $0.0000$ | $4.000000$ | **$3.000000$** | Rectangular conversion: horizontal $x$ in $X$, vertical $y$ in $Y$ |
| `{{key:x⇄y}}` | $0.0000$ | $0.0000$ | **$3.000000$** | **$4.000000$** | Realign to Gaussian complex format: Real in $Y$, Imag in $X$ |

In Degrees mode (`{{key:DEG}}`), we can use `{{key:▸y,x}} {{key:x⇄y}}` to verify Fortescue's three-phase neutral cancellation $1 + a + a^2 = 0$ ($\rightarrow X = \mathbf{0.000000}$) for the cube roots of unity $a = 1\angle 120^\circ = -0.5 + 0.866025i$ and $a^2 = 1\angle 240^\circ = -0.5 - 0.866025i$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `120 {{key:ENTER}} 1 {{key:▸y,x}} {{key:x⇄y}}` | $0.0000$ | $0.0000$ | $-0.500000$ | $0.866025$ | Polar to Gaussian: $a = -0.5 + 0.8660i$ |
| `240 {{key:ENTER}} 1 {{key:▸y,x}} {{key:x⇄y}}` | $-0.500000$ | $0.866025$ | $-0.500000$ | $-0.866025$ | Polar to Gaussian: $a^2 = -0.5 - 0.8660i$ |
| `{{key:CMPLX}} {{key:+}}` | $-0.500000$ | $-0.500000$ | $-1.000000$ | $0.000000$ | Complex sum: $a + a^2 = -1.0 + 0.0i$ |
| `1 {{key:ENTER}} 0 {{key:CMPLX}} {{key:+}}` | $-1.000000$ | $-1.000000$ | **$0.000000$** | **$0.000000$** | Add $+1$ reference: $1 + a + a^2 = 0 + 0i$ |

In Radians mode (`{{key:RAD}}`), `{{key:CMPLX}} {{key:√x}}` and `{{key:CMPLX}} {{key:yˣ}}` evaluate De Moivre's fractional powers directly across the stack:
* **Principal Square Root of $i$ ($\sqrt{0 + 1i} = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}i$):** Bisects the $90^\circ$ ($\pi/2\text{ rad}$) angle to $45^\circ$ in place on $(Y, X)$:
  `{{res:sc32_05_complex_numbers_phasors_seq_09:keys}}` $\to (Y = \mathbf{0.707107},\; X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_09:value}}})$.
* **Principal Cube Root of $-8$ ($8^{1/3}e^{i\pi/3}$):** Loading $-8 + 0i$ into $(T, Z)$ with a 6-digit decimal exponent $0.333333 + 0i$ in $(Y, X)$ gives an approximate root, whereas forming the exact rational exponent $1/3 + 0i$ first lands on the exact principal branch root:
  * **6-Digit Decimal Exponent ($0.333333$):** `{{res:sc32_05_complex_numbers_phasors_seq_18:keys}}` $\to X =$ `{{res:sc32_05_complex_numbers_phasors_seq_18:value}}`.
  * **Full-Precision Rational Exponent ($1/3$):** `{{res:sc32_05_complex_numbers_phasors_seq_19:keys}}` $\to (Y = \mathbf{1.000000},\; X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_19:value}}})$.

Even when both the base $\mathbf{z}_2 = 1 + i$ in $(T, Z)$ and the exponent $\mathbf{z}_1 = 1 - i$ in $(Y, X)$ are complex, pressing `{{key:CMPLX}} {{key:yˣ}}` evaluates $(1 + i)^{(1 - i)} = e^{(1-i)\ln(1+i)} = \mathbf{2.807879 + 1.317865i}$ (and keying `0 {{key:ENTER}} 1 {{key:ENTER}} 0 {{key:ENTER}} 1 {{key:CMPLX}} {{key:yˣ}}` confirms Euler's real-valued identity $i^i = e^{-\pi/2} = \mathbf{0.207880 + 0.000000i}$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:ENTER}} 1 {{key:ENTER}}` | $0.0000$ | $1.0000$ | $1.0000$ | $1.0000$ | Base $z_2 = 1 + i$ loaded into $(T, Z)$ |
| `1 {{key:ENTER}} 1 {{key:+/-}}` | $1.0000$ | $1.0000$ | $1.0000$ | $-1.0000$ | Exponent $z_1 = 1 - i$ loaded into $(Y, X)$ |
| `{{key:CMPLX}} {{key:yˣ}}` | $1.0000$ | $1.0000$ | **$2.807879$** | **$1.317865$** | General complex power $z_2^{z_1}$ evaluated |

To test analytic continuation of the unit-circle identity $\sin^2 z + \cos^2 z = 1$ far outside $[-1, +1]$ at $z = 1 + 2i$, we first evaluate $\sin(1 + 2i) = \sin(1)\cosh(2) + i\cos(1)\sinh(2)$ and $\cos(1 + 2i) = \cos(1)\cosh(2) - i\sin(1)\sinh(2)$:
* **Complex Sine ($\sin(1 + 2i)$):** `{{res:sc32_05_complex_numbers_phasors_seq_21:keys}}` $\to (Y = \mathbf{3.165779},\; X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_21:value}}})$.
* **Complex Cosine ($\cos(1 + 2i)$):** `{{res:sc32_05_complex_numbers_phasors_seq_22:keys}}` $\to (Y = \mathbf{2.032723},\; X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_22:value}}})$.

Because `{{key:CMPLX}} {{key:SIN}}`, `{{key:CMPLX}} {{key:COS}}`, and `{{key:CMPLX}} {{key:x²}}` are unary complex operators on $(Y, X)$, evaluating both branches directly on the 4-register stack lifts $(\sin z)^2$ intact into $(T, Z)$ while $(\cos z)^2$ forms in $(Y, X)$, confirming $\sin^2(1+2i) + \cos^2(1+2i) = 1 + 0i$ without re-typing intermediate decimals:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:RAD}} 1 {{key:ENTER}} 2 {{key:CMPLX}} {{key:SIN}}` | $0.0000$ | $0.0000$ | $3.165779$ | $1.959601$ | Evaluate $\sin(1+2i)$ in $(Y, X)$ |
| `{{key:CMPLX}} {{key:x²}}` | $0.0000$ | $0.0000$ | $6.182115$ | $12.407147$ | Square complex sine $(\sin z)^2$ in place |
| `1 {{key:ENTER}} 2 {{key:CMPLX}} {{key:COS}}` | $6.182115$ | $12.407147$ | $2.032723$ | $-3.051898$ | $(\sin z)^2$ lifts to $(T, Z)$; $\cos(1+2i)$ in $(Y, X)$ |
| `{{key:CMPLX}} {{key:x²}}` | $6.182115$ | $12.407147$ | $-5.182115$ | $-12.407147$ | Square complex cosine $(\cos z)^2$ in place |
| `{{key:CMPLX}} {{key:+}}` | $6.182115$ | $6.182115$ | **$1.000000$** | **$0.000000$** | Sum squares: $\sin^2 z + \cos^2 z = 1 + 0i$ |

### AC Impedance, Crossovers & Transmission Lines

In steady-state AC circuit analysis, series impedances add directly across the complex stack while parallel branches combine through complex reciprocals or `{{key:CMPLX}} {{key:x∥y}}`. When two AC impedances sit in series—say an inductive branch $\mathbf{Z}_1 = 8.0 + 4.0i\,\Omega$ and a capacitive branch $\mathbf{Z}_2 = 4.0 - 8.0i\,\Omega$—their resistances and reactances add component by component (`{{res:sc32_05_complex_numbers_phasors_seq_02:keys}}`), loading $\mathbf{Z}_2$ into $(T, Z)$ and $\mathbf{Z}_1$ into $(Y, X)$ before `{{key:CMPLX}} {{key:+}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $4.0000$ | $4.0000$ | Real part of $\mathbf{Z}_2$ pushed |
| `8 {{key:+/-}} {{key:ENTER}}` | $0.0000$ | $4.0000$ | $-8.0000$ | $-8.0000$ | Imag part of $\mathbf{Z}_2$ pushed |
| `8 {{key:ENTER}}` | $4.0000$ | $-8.0000$ | $8.0000$ | $8.0000$ | Real part of $\mathbf{Z}_1$ pushed |
| `4` | **$4.0000$** | **$-8.0000$** | **$8.0000$** | **$4.0000$** | Complete 4-register setup |
| `{{key:CMPLX}} {{key:+}}` | $4.0000$ | $4.0000$ | **$12.000000$** | **$-4.000000$** | $\mathbf{Z}_{\text{total}} = 12.0 - 4.0i\,\Omega$ |

When two branches are wired in parallel ($\mathbf{Z}_1 = 20 + 15i\,\Omega \parallel \mathbf{Z}_2 = 10 - 25i\,\Omega$), you can either fold both branches in a single dyadic stroke by loading them onto $(T, Z)$ and $(Y, X)$ and pressing `{{key:CMPLX}} {{key:x∥y}}`, or inspect their individual branch admittances $\mathbf{Y}_k = 1/\mathbf{Z}_k = G_k + jB_k$ along the way:
* **Invert Branch 1 ($\mathbf{Y}_1 = 1/\mathbf{Z}_1$):** `{{res:sc32_05_complex_numbers_phasors_seq_03:keys}}` $\to$ `{{res:sc32_05_complex_numbers_phasors_seq_03:value}}` ($\mathbf{Y}_1 = 0.032000 - 0.024000i\,\text{S}$).
* **Invert Branch 2 ($\mathbf{Y}_2 = 1/\mathbf{Z}_2$, while $\mathbf{Y}_1$ waits in $T, Z$):** `{{res:sc32_05_complex_numbers_phasors_seq_04:keys}}` $\to$ `{{res:sc32_05_complex_numbers_phasors_seq_04:value}}` ($\mathbf{Y}_2 = 0.013793 + 0.034483i\,\text{S}$).
* **Sum Admittances & Re-Invert ($\mathbf{Z}_{\text{parallel}} = (\mathbf{Y}_1 + \mathbf{Y}_2)^{-1}$):** `{{res:sc32_05_complex_numbers_phasors_seq_05:keys}}` $\to$ `{{res:sc32_05_complex_numbers_phasors_seq_05:value}}` ($\mathbf{Z}_{\text{parallel}} = \mathbf{20.7516 - 4.7507i\,\Omega}$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `20 {{key:ENTER}} 15 {{key:CMPLX}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.032000$ | $-0.024000$ | Branch 1 admittance $\mathbf{Y}_1$ in $(Y, X)$ |
| `10 {{key:ENTER}} 25 {{key:+/-}} {{key:CMPLX}} {{key:1/x}}` | $0.032000$ | $-0.024000$ | $0.013793$ | $0.034483$ | $\mathbf{Y}_1$ lifts to $(T, Z)$; $\mathbf{Y}_2$ in $(Y, X)$ |
| `{{key:CMPLX}} {{key:+}}` | $0.032000$ | $0.032000$ | $0.045793$ | $0.010483$ | Sum admittances: $\mathbf{Y}_{\text{parallel}} = \mathbf{Y}_1 + \mathbf{Y}_2$ |
| `{{key:CMPLX}} {{key:1/x}}` | $0.032000$ | $0.032000$ | **$20.7516$** | **$-4.7507$** | Invert admittance: $\mathbf{Z}_{\text{parallel}} = 20.75 - 4.75i\,\Omega$ |

In a Zobel conjugate loudspeaker compensation network ($Z_1 = 3 + 4i\,\Omega \parallel Z_2 = 3 - 4i\,\Omega$), where a series resistor-capacitor branch $3 - 4i\,\Omega$ is wired across an inductive voice coil $3 + 4i\,\Omega$, conjugate symmetry lets you solve the network entirely within the lower two stack registers without touching $Z$ or $T$: invert $3 + 4i\,\Omega$ in place on $(Y, X)$ into $Y_1 = 0.120000 - 0.160000i\,\text{S}$, swap the real conductance $G = 0.120000\,\text{S}$ into Register $X$ with `{{key:x⇄y}}` (since the conjugate susceptances $\mp 0.160000i\,\text{S}$ cancel identically), double $G$ to $0.240000\,\text{S}$, and tap `{{key:1/x}}`:
* **Zobel Compensated Loudspeaker Load:** `{{res:sc32_05_complex_numbers_phasors_seq_32:keys}}` $\to 4.166667\,\Omega$.

When an AC network is not symmetric—such as a four-arm Thévenin AC impedance bridge $Z_{\text{th}} = (Z_A \parallel Z_C) + (Z_B \parallel Z_D)$ with $Z_A = 10 + 20i\,\Omega$, $Z_C = 20 + 0i\,\Omega$, $Z_B = 30 - 10i\,\Omega$, and $Z_D = 0 - 25i\,\Omega$—each parallel arm uses the dyadic complex harmonic operator `{{key:CMPLX}} {{key:x∥y}}` across four real registers. Activating the 8-register stack (`{{key:FLAGS}} {{key:8-LVL}}`, providing a four-level complex stack) lets $Z_{AC} = Z_A \parallel Z_C$ ride intact into registers $(R_6, R_5)$ while $Z_B$ and $Z_D$ are loaded, drop back into $(T, Z)$ when `{{key:CMPLX}} {{key:x∥y}}` resolves $Z_{BD}$, and combine directly via `{{key:CMPLX}} {{key:+}}` at full 16-digit internal precision without `STO`/`RCL` or re-typing:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:FLAGS}} {{key:8-LVL}} 10 {{key:ENTER}} 20 {{key:ENTER}} 20 {{key:ENTER}} 0` | $10.0000$ | $20.0000$ | $20.0000$ | $0.0000$ | Enable 8-level stack; load $Z_A$ and $Z_C$ |
| `{{key:CMPLX}} {{key:x∥y}}` | $0.0000$ | $0.0000$ | $10.7692$ | $6.1538$ | Parallel branch $Z_{AC} = Z_A \parallel Z_C$ in $(Y, X)$ |
| `30 {{key:ENTER}} 10 {{key:+/-}} {{key:ENTER}} 0 {{key:ENTER}} 25 {{key:+/-}}` | $30.0000$ | $-10.0000$ | $0.0000$ | $-25.0000$ | Load $Z_B, Z_D$; $Z_{AC}$ rides up to $(R_6, R_5)$ |
| `{{key:CMPLX}} {{key:x∥y}}` | $10.7692$ | $6.1538$ | $8.8235$ | $-14.7059$ | $Z_{BD} = Z_B \parallel Z_D$ in $(Y, X)$; $Z_{AC}$ drops to $(T, Z)$ |
| `{{key:CMPLX}} {{key:+}}` | $0.0000$ | $0.0000$ | **$19.5928$** | **$-8.5520$** | Sum branches: $Z_{\text{th}} = Z_{AC} + Z_{BD}$ |

In a second-order Butterworth low-pass section $H_{\text{Butter2}}(s) = \frac{1}{s^2 + \sqrt{2}s + 1}$, evaluating the normalized crossover frequency $s = j$ cancels $j^2 = -1$ against $+1$ in the denominator and reduces it to $B_2(j) = 0 + \sqrt{2}i$. Inverting that denominator vector in place on $(Y, X)$ via `{{key:CMPLX}} {{key:1/x}}` yields the Butterworth crossover response, and pressing `{{key:CMPLX}} {{key:x²}}` squares it in place to verify the fourth-order Linkwitz-Riley (`LR4`) loudspeaker crossover $(Y = \mathbf{-0.500000},\; X = \mathbf{0.000000}, \text{ or } -6.02\text{ dB at } -180^\circ\text{ phase})$:
* **2nd-Order Butterworth Crossover Response ($1/(j\sqrt{2})$):** `{{res:sc32_05_complex_numbers_phasors_seq_23:keys}}` $\to H_{\text{Butter2}}(j) = \mathbf{0.000000 - 0.707107i}$ ($-3.01\text{ dB}, -90^\circ$).

Likewise, in an inverting operational-amplifier bandpass stage where a virtual-ground summing node sets the closed-loop voltage gain to $A_v = -\mathbf{Z}_f / \mathbf{Z}_{\text{in}}$, pairing feedback impedance $\mathbf{Z}_f = 5000 - 5000i\,\Omega$ in $(T, Z)$ with input impedance $\mathbf{Z}_{\text{in}} = 1000 - 1000i\,\Omega$ in $(Y, X)$ (`{{res:sc32_05_complex_numbers_phasors_seq_25:keys}}`) engages all four registers during `{{key:CMPLX}} {{key:÷}}` and `{{key:CMPLX}} {{key:+/-}}` to determine $A_v = \mathbf{-5.000000} +$ `{{res:sc32_05_complex_numbers_phasors_seq_25:value}}` $i$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `5000 {{key:ENTER}} 5000 {{key:+/-}} {{key:ENTER}}` | $0.0000$ | $5000.0000$ | $-5000.0000$ | $-5000.0000$ | Feedback impedance $Z_f$ pushed |
| `1000 {{key:ENTER}} 1000 {{key:+/-}}` | $5000.0000$ | $-5000.0000$ | $1000.0000$ | $-1000.0000$ | Input impedance $Z_{\text{in}}$ in $(Y, X)$ |
| `{{key:CMPLX}} {{key:÷}}` | $5000.0000$ | $5000.0000$ | $5.000000$ | $0.000000$ | Complex ratio $Z_f / Z_{\text{in}} = 5.0 + 0i$ |
| `{{key:CMPLX}} {{key:+/-}}` | $5000.0000$ | $5000.0000$ | **$-5.000000$** | **$0.000000$** | Negate gain: $A_v = -5.0 + 0i$ |

Finally, in RF transmission-line analysis, when a $Z_0 = 50\,\Omega$ coaxial cable is terminated by a dipole antenna of impedance $\mathbf{Z}_L = 75 + 40i\,\Omega$, loading $\mathbf{Z}_L - Z_0 = 25 + 40i$ into $(T, Z)$ and $\mathbf{Z}_L + Z_0 = 125 + 40i$ into $(Y, X)$ lets `{{key:CMPLX}} {{key:÷}}` resolve the reflection coefficient $\mathbf{\Gamma} = 0.274311 + 0.232221i$ ($|\mathbf{\Gamma}| = 0.359406$, or $|\mathbf{\Gamma}|^2 = 12.92\%$ reflected power):
* **Voltage Standing Wave Ratio ($\text{VSWR} = \frac{1 + |\mathbf{\Gamma}|}{1 - |\mathbf{\Gamma}|}$):** `{{res:sc32_05_complex_numbers_phasors_seq_06:keys}}` $\to \text{VSWR} = \mathbf{2.1221}$.
* **Dipole Antenna Return Loss ($\text{RL} = -20\log_{10}|\mathbf{\Gamma}|$):** `{{res:sc32_05_complex_numbers_phasors_seq_07:keys}}` $\to \text{RL} = \mathbf{8.89\text{ dB}}$ ($8.8883\text{ dB}$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `25 {{key:ENTER}} 40 {{key:ENTER}}` | $0.0000$ | $25.0000$ | $40.0000$ | $40.0000$ | Numerator $Z_L - Z_0 = (75-50) + 40i$ pushed |
| `125 {{key:ENTER}} 40` | $25.0000$ | $40.0000$ | $125.0000$ | $40.0000$ | Denominator $Z_L + Z_0 = (75+50) + 40i$ in $(Y, X)$ |
| `{{key:CMPLX}} {{key:÷}}` | $25.0000$ | $25.0000$ | **$0.274311$** | **$0.232221$** | Reflection coefficient $\mathbf{\Gamma} = 0.2743 + 0.2322i$ |
| `{{key:x⇄y}} {{key:▸θ,r}}` | $25.0000$ | $25.0000$ | $0.702494$ | **$0.359406$** | Polar: Phase $\theta = 0.702494\text{ rad}$ ($40.25^\circ$) in $Y$, magnitude $\lvert\mathbf{\Gamma}\rvert = 0.3594$ in $X$ |
| `{{key:ENTER}} {{key:ENTER}} 1 {{key:+}} {{key:x⇄y}} 1 {{key:x⇄y}} {{key:-}} {{key:÷}}` | $0.702494$ | $0.702494$ | $0.702494$ | **$2.1221$** | VSWR $= (1+\lvert\mathbf{\Gamma}\rvert)/(1-\lvert\mathbf{\Gamma}\rvert) = 2.1221$ |

* **VNA Microwave Port Return Loss ($S_{11} = 0.25 - 0.40i$) & Quarter-Wave ($\lambda/4$) Matching:**
  For $S_{11} = 0.25 - 0.40i$ ($|S_{11}| = 0.471699$, or $22.25\%$ reflected power), convert $S_{11}$ on $(Y, X)$ to polar magnitude via `{{key:x⇄y}} {{key:▸θ,r}}` and evaluate $-20\log_{10}|S_{11}|$; to match a $Z_L = 100\,\Omega$ load to $Z_0 = 50\,\Omega$ via a quarter-wave line ($Z_{\text{line}} = \sqrt{50 \times 100} \approx 70.7107\,\Omega$), square $Z_{\text{line}}$ and divide by $Z_L$:
  * **VNA Port Return Loss:** `{{res:sc32_05_complex_numbers_phasors_seq_16:keys}}` $\to \text{RL} =$ `{{res:sc32_05_complex_numbers_phasors_seq_16:value}}` $\text{dB}$.
  * **Quarter-Wave Transformer Input Impedance ($Z_{\text{in}} = Z_{\text{line}}^2 / Z_L$):** `{{res:sc32_05_complex_numbers_phasors_seq_17:keys}}` $\to 50.0000\,\Omega$ ($\text{VSWR} = 1.0000:1$).

For a lossy coaxial line with series impedance $Z' = 0.1 + 2.5i\,\Omega/\text{m}$ in $(T, Z)$ and shunt admittance $Y' = 10^{-6} + 10^{-3}i\,\text{S/m}$ in $(Y, X)$, `{{key:CMPLX}} {{key:÷}}` followed by `{{key:CMPLX}} {{key:√x}}` evaluates Oliver Heaviside's characteristic impedance $Z_0 = \sqrt{Z'/Y'} = \mathbf{50.0095 - 0.9748i\,\Omega}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0.1 {{key:ENTER}} 2.5 {{key:ENTER}}` | $0.0000$ | $0.1000$ | $2.5000$ | $2.5000$ | Load series impedance $Z' = 0.1 + 2.5i$ |
| `1 {{key:E}} 6 {{key:+/-}} {{key:ENTER}} 1 {{key:E}} 3 {{key:+/-}}` | $0.1000$ | $2.5000$ | $1.0000 \times 10^{-6}$ | $1.0000 \times 10^{-3}$ | Load shunt admittance $Y'$ into $(Y, X)$ |
| `{{key:CMPLX}} {{key:÷}}` | $0.1000$ | $0.1000$ | $2499.9975$ | $-97.4999$ | Complex impedance ratio $Z'/Y'$ |
| `{{key:CMPLX}} {{key:√x}}` | $0.1000$ | $0.1000$ | **$50.0095$** | **$-0.9748$** | Characteristic impedance $Z_0 = \sqrt{Z'/Y'}$ |

Attempting complex division or `{{key:CMPLX}} {{key:1/x}}` or `{{key:CMPLX}} {{key:LN}}` at the origin $0 + 0i$ halts non-destructively with `DIVIDE BY 0` (Code 01), while unsupported combinations such as `{{key:CMPLX}} {{key:ASIN}}` display `INVALID DATA` (Code 02) until cleared with `{{key:C}}`. By pairing two complete Gaussian planes across $(T, Z)$ and $(Y, X)$ on a four-line display, complex arithmetic replaces trigonometric differential equations with direct vector algebra across alternating-current networks, acoustic filters, and transmission lines.
