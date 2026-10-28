---
title: "Chapter 5: The Imaginary Number That Keeps the Lights On | Thinking in the Stack (SC-32)"
description: "Explore the geometric discovery of the complex plane, Leonhard Euler's identity, Abraham de Moivre's roots of unity, Charles Proteus Steinmetz's AC phasors, loudspeaker crossovers, and RF transmission lines—followed by the complete SC-32 complex workbench."
---

# Chapter 5: The Imaginary Number That Keeps the Lights On

## Why Multiplying by i Is a 90-Degree Turn, Not an Imaginary Fantasy

Few ideas in high-school mathematics suffer from a worse piece of historical branding than $\sqrt{-1}$. From the moment a student first hears that the square of any positive number is positive ($+3 \times +3 = +9$) and the square of any negative number is *also* positive ($-3 \times -3 = +9$), the square root of a negative number sounds like a contradiction in terms. When the French philosopher and mathematician **René Descartes** encountered roots of negative quantities in his 1637 treatise *La Géométrie*, he dismissed them with a single disparaging adjective: *"imaginary."* The label stuck for four centuries, convincing generations of students that $i = \sqrt{-1}$ is a make-believe algebraic phantom invented solely to torture Algebra II classes.

Yet $\sqrt{-1}$ was not forced upon mathematicians by a philosophical whim—it ambushed them from inside equations whose final answers were unmistakably real. In sixteenth-century Italy, when **Scipione del Ferro**, **Niccolò Fontana ("Tartaglia")**, and **Gerolamo Cardano** discovered the general formula for solving a cubic equation such as $x^3 = 15x + 4$, they stumbled into a baffling paradox. Anyone can check by mental arithmetic that $x = 4$ is a rock-solid real solution ($4^3 = 64 = 15(4) + 4$). Yet when Cardano plugged the coefficients of $x^3 - 15x - 4 = 0$ into his new cubic formula, the path to $x = 4$ led straight through the sum of two "impossible" square roots:

$$x = \sqrt[3]{2 + \sqrt{-121}} + \sqrt[3]{2 - \sqrt{-121}}$$

How could two numbers that supposedly did not exist add together to build the concrete integer $4$? In 1572, the Italian hydraulic engineer **Rafael Bombelli** had the courage to treat $\sqrt{-121}$ as $11\sqrt{-1}$ and follow the rules of ordinary arithmetic wherever they led. Bombelli noticed that if you multiply $(2 + \sqrt{-1})$ by itself three times using $\left(\sqrt{-1}\right)^2 = -1$, you get $(2 + \sqrt{-1})^3 = 2 + 11\sqrt{-1}$, and similarly $(2 - \sqrt{-1})^3 = 2 - 11\sqrt{-1}$. Taking the cube roots and adding them together caused the two opposite $+\sqrt{-1}$ and $-\sqrt{-1}$ terms to annihilate each other in midair:

$$(2 + \sqrt{-1}) + (2 - \sqrt{-1}) = 4$$

To get from one real number to another, algebra had been forced to travel through a hidden second dimension.

### How Wallis, Wessel, Argand, and Gauss Found the Missing Direction

Why did $\sqrt{-1}$ refuse to sit anywhere on the familiar number line? Because the number line is only one-dimensional—and multiplication by a negative number was never just "changing a sign."

In 1685, the English mathematician **John Wallis**—followed over the next century by the Norwegian-Danish surveyor **Caspar Wessel** (1797), the Swiss bookkeeper **Jean-Robert Argand** (1806), and the German prince of mathematics **Carl Friedrich Gauss** (1831)—realized the geometric truth that transforms $\sqrt{-1}$ from an abstract rule into physical common sense.

Stand at the origin $0$ of a flat horizontal road, facing right toward $+1$ (East). Now ask yourself: *What does multiplying by $-1$ actually do to your position?* It does not erase your distance from the origin; it **rotates your vector by $180^\circ$** so that you point straight left toward $-1$ (West). Multiply by $-1$ a second time, and you rotate by another $180^\circ$, completing a $360^\circ$ turn back to $+1$:

$$(-1) \times (-1) = +1 \quad \Longleftrightarrow \quad 180^\circ + 180^\circ = 360^\circ$$

Once you see that multiplying by $-1$ is a **$180^\circ$ half-turn**, the mystery of $i = \sqrt{-1}$ evaporates on the spot. We are looking for an operation $i$ which, when applied **twice in a row** ($i \times i$), produces a $180^\circ$ turn ($-1$). What physical action, done twice in a row, turns you around by $180^\circ$?

**A $90^\circ$ quarter-turn!**

1. **Zero turns ($i^0 = +1$):** Point East along the horizontal real axis at $0^\circ$.
2. **One $90^\circ$ counterclockwise turn ($\times i$):** Rotate $90^\circ$ left. You are no longer on the East-West road at all—you are pointing straight North along a perpendicular vertical axis at $+i$.
3. **Two $90^\circ$ turns ($i \times i = i^2 = -1$):** Rotate by a *second* $90^\circ$ quarter-turn ($90^\circ + 90^\circ = 180^\circ$). You are now pointing straight West along the real axis at **$-1$**. That is the entire reason why $i^2 = -1$: two $90^\circ$ turns make a $180^\circ$ reversal.
4. **Three and four $90^\circ$ turns ($i^3 = -i,\; i^4 = +1$):** A third quarter-turn points straight South at $270^\circ$ ($-i$), and a fourth quarter-turn completes the $360^\circ$ circle back to $+1$.

Gauss proposed that we retire Descartes's misleading word "imaginary" and call $+i$ the **lateral unit**. A **complex number** $z = a + bi$ is simply an address on a two-dimensional plane (the **Complex Plane** or **Argand Diagram**): walk $a$ steps horizontally along the Real axis, then walk $b$ steps vertically along the perpendicular Imaginary axis.

### Unpeeling Complex Arithmetic and the Conjugate Mirror

Because a complex number $z = a + bi$ is a two-component vector on a flat plane, the SC-32 models it directly on the lower two shelves of the stack without locking you into a separate complex mode: **Register $Y$ holds the horizontal Real part ($a$) and Register $X$ holds the vertical Imaginary part ($b$)**. Whenever a second complex number $z_2 = c + di$ is pushed onto the stack, the first complex number lifts cleanly into the upper register pair $(T = a, Z = b)$, so all four registers hold two complete complex numbers at once. Pressing the transient **`{{key:CMPLX}}`** prefix (`{{key:↰}}` + `{{key:STO}}`) right before `{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`, or `{{key:1/x}}` executes the full two-dimensional operation across $(T, Z)$ and $(Y, X)$ in a single step:

- **Addition and Subtraction (`{{key:CMPLX}} {{key:+}}` and `{{key:CMPLX}} {{key:-}}` — Head-to-Tail Vector Translation):** To add $z_1 = a + bi$ in $(T, Z)$ and $z_2 = c + di$ in $(Y, X)$, the calculator combines their horizontal steps in Register $Y$ and their vertical steps in Register $X$:
  $$(a + bi) + (c + di) = (a + c) + (b + d)i$$
- **Multiplication (`{{key:CMPLX}} {{key:×}}` — Scale the Lengths, Add the Angles):** When you multiply $(a + bi)(c + di)$ from the inside out using $i^2 = -1$, the two real products $ac$ and $i^2 bd = -bd$ combine along the horizontal axis, while the two cross-terms $adi$ and $bci$ combine along the vertical axis:
  $$(a + bi)(c + di) = (ac - bd) + (ad + bc)i$$
- **The Complex Conjugate ($z^* = a - bi$), Reciprocal (`{{key:CMPLX}} {{key:1/x}}`), and Division (`{{key:CMPLX}} {{key:÷}}`):** What if you need to divide one complex number by another, such as $\frac{a + bi}{c + di}$? Every complex number $z = c + di$ has a mirror twin across the horizontal real axis called its **complex conjugate**, $z^* = c - di$ (formed on the stack by negating Register $X$ with `{{key:+/-}}`). If $z$ points at an angle of $+\theta$ above the real axis, $z^*$ points at $-\theta$ below it. Multiplying $z$ by its own conjugate cancels their opposite angles ($\theta - \theta = 0^\circ$) and leaves the squared Pythagorean length $|z|^2 = c^2 + d^2$ as a pure real number:
  $$(c + di)(c - di) = c^2 - d^2 i^2 = c^2 + d^2$$
  Multiplying the top and bottom of any complex fraction by the denominator's conjugate $c - di$ clears the imaginary unit from the denominator in a single move—the exact algebra that `{{key:CMPLX}} {{key:1/x}}` and `{{key:CMPLX}} {{key:÷}}` perform automatically:
  $$\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{c^2 + d^2} = \left(\frac{ac + bd}{c^2 + d^2}\right) + \left(\frac{bc - ad}{c^2 + d^2}\right)i$$

### Why Real Shock Absorbers and Skyscrapers Have Complex Eigenvalues

Long before you touch an electrical circuit, this split between the horizontal Real axis and the vertical Imaginary axis governs every oscillating mechanical system around you—from the coil-over suspension of a car hitting a pothole to the giant tuned mass damper swinging inside the top of a skyscraper during a windstorm.

When a mass $m$ attached to a spring of stiffness $k$ and a hydraulic shock absorber of viscous damping $c$ is displaced from rest, Newton's second law writes its motion as $m\ddot{x} + c\dot{x} + kx = 0$. Searching for an exponential motion $x(t) = e^{\lambda t}$ yields the quadratic characteristic equation $m\lambda^2 + c\lambda + k = 0$, whose roots are the system's **eigenvalues**:

$$\lambda = -\frac{c}{2m} \pm \sqrt{\left(\frac{c}{2m}\right)^2 - \frac{k}{m}} = -\alpha \pm i\omega_d$$

Whenever the spring is stiff enough that $k/m > (c/2m)^2$, the number inside the square root is negative, and the eigenvalues become a complex conjugate pair $\lambda = -\alpha \pm i\omega_d$. Why does nature use a two-dimensional complex number to describe a one-dimensional bouncing spring? Because the two axes of the complex plane track two perpendicular physical processes happening at the same time:

1. **The Horizontal Real Axis ($-\alpha = -c/(2m)$ — Irreversible Energy Dissipation):** Viscous oil forced through the piston valves of a shock absorber resists motion in phase with velocity. It permanently removes mechanical energy from the bounce, turning kinetic energy into warm oil so the amplitude decays exponentially as $e^{-\alpha t}$.
2. **The Vertical Imaginary Axis ($\pm i\omega_d$ — Lossless $90^\circ$ Energy Exchange):** The coil spring and the moving mass do not burn up a single joule of heat. Instead, kinetic energy in the moving mass ($\frac{1}{2}mv^2$, which peaks as the car passes through equilibrium) and potential energy in the compressed spring ($\frac{1}{2}kx^2$, which peaks at the top and bottom of the bounce) trade places back and forth **$90^\circ$ out of phase** at angular frequency $\omega_d = \sqrt{k/m - \alpha^2}$.

If the shock absorber seals leak out ($c \to 0$), the real part $-\alpha$ vanishes, the eigenvalue slides onto the pure imaginary axis ($\lambda = \pm i\sqrt{k/m}$), and the car bounces forever. If the shock absorber is stiffened to the critical threshold $c_{\text{crit}} = 2\sqrt{mk}$, the imaginary part $\omega_d$ vanishes, and the chassis glides back to level ground without a single overshoot.

---

## Leonhard Euler's Jewel and De Moivre's Spiral Staircase

In Chapter 3, we watched **Leonhard Euler's** number $e \approx 2.71828$ emerge as the universal base of continuous growth and decay along a straight line. In Chapter 4, we watched $\cos\theta$ and $\sin\theta$ trace circular rotation around a flat unit circle. On the surface, exponential growth (a runaway snowball) and trigonometry (a repeating wheel) look like polar opposites.

In 1748, in his foundational treatise *Introductio in analysin infinitorum* (preceded by English mathematician Roger Cotes's 1714 logarithmic insight $i\theta = \ln(\cos\theta + i\sin\theta)$), Euler asked what happens when you feed an imaginary angle $i\theta$ into the exponential growth function $e^x$. What he uncovered is what Nobel physicist **Richard Feynman** called *"our jewel"* and *"the most remarkable formula in mathematics"*:

$$e^{i\theta} = \cos\theta + i\sin\theta$$

Before Euler published this single equation, mathematicians treated exponential functions ($e^x$, logarithms, and compound interest) and circular trigonometric functions ($\cos\theta, \sin\theta$, chords, and astronomical tables) as two completely separate continents of mathematics. Euler proved that they are secretly **two cross-sections of the exact same complex function**: walk along the horizontal real axis and $e^z$ grows exponentially; turn $90^\circ$ onto the vertical imaginary axis and $e^z$ orbits in a circle!

### Why Continuous Imaginary Growth Turns into a Circle

Why on earth should raising $e \approx 2.71828$ to an imaginary power trace a circle of radius $1$? You can see why from two complementary vantage points—one physical and one algebraic.

First, think about compound growth from the inside out. When a quantity $z(t)$ grows at a real rate $k$, its velocity $dz/dt = k \cdot z$ points in the **exact same direction** as the position vector $z$, pushing the point straight outward away from the origin along a ray. Now replace the real rate $k$ with the imaginary rate $i\omega$:

$$\frac{dz}{dt} = i\omega z$$

Remember what multiplying by $i$ does geometrically: it rotates any vector by **$90^\circ$ counterclockwise**. That means at every single instant, the velocity vector $dz/dt$ of the moving point $z(t) = e^{i\omega t}$ is pointed strictly **perpendicular ($90^\circ$) to its radius vector**—just like a tetherball whipping around a pole or a satellite in a circular orbit around the Earth. Because a force or velocity that acts at $90^\circ$ to the radius neither pushes the point farther from the origin nor pulls it closer, the distance from the origin stays locked at $|e^{i\theta}| = 1$ forever. Instead of growing outward in size, $e^{i\theta}$ sweeps around the unit circle, with horizontal shadow $\cos\theta$ and vertical shadow $i\sin\theta$.

Second, consider what happens when you substitute $x = i\theta$ into the infinite Taylor series for $e^x$ that we met in Chapter 3, unpeeling the powers $i^2 = -1$, $i^3 = -i$, $i^4 = +1$ one term at a time:

$$e^{i\theta} = 1 + i\theta + \frac{(i\theta)^2}{2!} + \frac{(i\theta)^3}{3!} + \frac{(i\theta)^4}{4!} + \frac{(i\theta)^5}{5!} + \dots$$

Group the even powers (which are purely real) and the odd powers (which carry a factor of $i$):

$$e^{i\theta} = \underbrace{\left(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \frac{\theta^6}{6!} + \dots\right)}_{\cos\theta} + i\underbrace{\left(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \frac{\theta^7}{7!} + \dots\right)}_{\sin\theta} = \cos\theta + i\sin\theta$$

When you dial the angle $\theta$ halfway around the unit circle to $\theta = \pi\text{ radians}$ ($180^\circ$), where $\cos\pi = -1$ and $\sin\pi = 0$, Euler's formula lands at $e^{i\pi} = -1$, or in its most famous arrangement:

$$e^{i\pi} + 1 = 0$$

This five-symbol sentence links the additive identity ($0$), the multiplicative identity ($1$), the geometry of the circle ($\pi$), the base of natural growth ($e$), and the $90^\circ$ rotation operator ($i$) with a single addition and equals sign. On the SC-32, placing $0$ in Register $Y$ and $\pi$ in Register $X$ and pressing `{{key:CMPLX}} {{key:eˣ}}` evaluates Euler's formula directly on the stack, while `{{key:CMPLX}} {{key:LN}}` reverses the journey to recover the complex logarithm $\ln(-1) = 0 + i\pi$. Even more startlingly, Euler's formula proves that raising $i$ to the $i$-th power ($i^i$, evaluated via `{{key:CMPLX}} {{key:yˣ}}`) is a **purely real number**: since $i = e^{i\pi/2}$ sits at $90^\circ$ ($\pi/2\text{ rad}$) on the unit circle, raising it to the power $i$ gives $i^i = \left(e^{i\pi/2}\right)^i = e^{i^2 \pi/2} = e^{-\pi/2} \approx 0.207880$.

### Polar Form, Abraham de Moivre's Theorem, and the Roots of Unity

Once Euler's formula is in hand, every nonzero complex number $z = x + iy$ can be written in **polar form** by factoring out its Euclidean distance from the origin, $r = |z| = \sqrt{x^2 + y^2}$, and its phase angle $\theta = \operatorname{atan2}(y, x)$:

$$z = x + iy = r(\cos\theta + i\sin\theta) = r e^{i\theta} = r\angle\theta$$

On the SC-32, the coordinate keys `{{key:▸θ,r}}` and `{{key:▸y,x}}`—paired with `{{key:x⇄y}}` so Gaussian $(Y = \text{Real}, X = \text{Imag})$ aligns with `{{key:▸θ,r}}`'s $(Y = y, X = x)$ input and avoids the **Complementary Angle Trap** of computing $\arctan(\text{Real}/\text{Imag}) = 90^\circ - \theta$—convert directly between rectangular and polar representations on the lower two stack shelves. Writing complex numbers as $r e^{i\theta}$ turns high-school exponents and roots into effortless geometry:

- **Multiplying Two Complex Numbers:** $z_1 z_2 = (r_1 e^{i\theta_1})(r_2 e^{i\theta_2}) = (r_1 r_2) e^{i(\theta_1 + \theta_2)}$. You **multiply the lengths** and **add the angles**.
- **Dividing Two Complex Numbers:** $z_1 / z_2 = (r_1 / r_2) e^{i(\theta_1 - \theta_2)}$. You **divide the lengths** and **subtract the angles**.
- **Abraham de Moivre's Theorem (`{{key:CMPLX}} {{key:yˣ}}` — Powers & Roots):** What happens when you raise $z = r e^{i\theta}$ to the $n$-th power? By the ordinary laws of exponents, $(r e^{i\theta})^n = r^n e^{in\theta}$:
  $$\left[r(\cos\theta + i\sin\theta)\right]^n = r^n\left(\cos(n\theta) + i\sin(n\theta)\right)$$
  Geometrically, raising a complex number to the $n$-th power spirals its radius to $r^n$ while multiplying its angle by $n$.

Going in reverse—taking an **$n$-th root** $\sqrt[n]{z}$—is where De Moivre's theorem reveals why an $n$-th degree equation always has $n$ roots in the complex plane. Because adding full $360^\circ$ ($2\pi\text{ rad}$) turns to an angle leaves a point in the exact same spot ($\theta + 2k\pi$), dividing the angle by $n$ yields **$n$ distinct, equally spaced spokes** around a circle of radius $r^{1/n}$:

$$\sqrt[n]{z} = r^{1/n} \left[\cos\left(\frac{\theta + 2k\pi}{n}\right) + i\sin\left(\frac{\theta + 2k\pi}{n}\right)\right], \qquad k = 0, 1, \dots, n-1$$

For example, when sixteenth-century skeptics worried that taking the square root of $i$ ($\sqrt{i}$) would require inventing a "hyper-imaginary" number outside the complex plane, Gauss pointed out that $i = 1\angle 90^\circ$ has radius $1$ and angle $90^\circ$. Taking its principal square root (`{{key:CMPLX}} {{key:√x}}`) simply takes $\sqrt{1} = 1$ and halves the angle from $90^\circ$ to **$45^\circ$** ($\pi/4\text{ rad}$), landing right inside the complex plane at $\cos 45^\circ + i\sin 45^\circ = \frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2} \approx 0.7071 + 0.7071i$.

Likewise, on the real number line, the cube root of $1$ has only one answer ($1$), and the cube root of $-8$ has only one answer ($-2$). In the complex plane, the **three cube roots of unity** ($z^3 = 1 = e^{i\cdot 2k\pi}$) sit $360^\circ / 3 = 120^\circ$ apart at the corners of an equilateral triangle inscribed in the unit circle:

$$1 = 1\angle 0^\circ, \qquad a = 1\angle 120^\circ = -\frac{1}{2} + i\frac{\sqrt{3}}{2}, \qquad a^2 = 1\angle 240^\circ = -\frac{1}{2} - i\frac{\sqrt{3}}{2}$$

Because those three unit vectors pull outward with equal strength at $0^\circ$, $120^\circ$, and $240^\circ$ like the three symmetrical spokes of a three-pointed star, their vector sum cancels identically to zero ($1 + a + a^2 = 0$). As **Charles LeGeyt Fortescue** proved in 1918, that exact $120^\circ$ three-phase symmetry is why every high-voltage AC transmission tower on Earth carries power across three phase wires ($0^\circ, 120^\circ, 240^\circ$): in a balanced three-phase grid, the three return currents sum to $1 + a + a^2 = 0$ at the transformer neutral, eliminating the need to string a heavy fourth return cable across the countryside.

### Beyond the Unit Circle: Analytic Continuation and Joukowsky Airfoils

Euler's bridge between exponentials and trigonometry even lets us ask questions that sound impossible in high-school trigonometry: *What is the sine or cosine of a complex number $z = x + iy$?*

For any real angle $x$, $\sin x$ and $\cos x$ are trapped forever between $-1$ and $+1$. Yet because $e^{ix} = \cos x + i\sin x$ and $e^{-ix} = \cos x - i\sin x$, adding and subtracting those two equations defines cosine and sine everywhere in the complex plane:

$$\cos z = \frac{e^{iz} + e^{-iz}}{2}, \qquad \sin z = \frac{e^{iz} - e^{-iz}}{2i}$$

When you feed a complex number $z = x + iy$ into these formulas via `{{key:CMPLX}} {{key:SIN}}` or `{{key:CMPLX}} {{key:COS}}`, the imaginary part $iy$ gets multiplied by $i$, turning into a *real* exponential $e^{\mp y}$. Expanding from the inside out shows that complex sine and cosine couple circular oscillation along $x$ with hyperbolic growth ($\cosh y, \sinh y$) along $y$:

$$\sin(x + iy) = \sin x \cosh y + i \cos x \sinh y, \qquad \cos(x + iy) = \cos x \cosh y - i \sin x \sinh y$$

Even when $\cosh y$ makes $\sin z$ and $\cos z$ grow to enormous magnitudes far outside $[-1, +1]$, the principle of **analytic continuation** guarantees that their squares (`{{key:CMPLX}} {{key:x²}}`) still obey Pythagoras's theorem $\sin^2 z + \cos^2 z = 1$ to the last decimal place.

Smooth complex functions also possess a remarkable geometric property called **conformal mapping**: any differentiable complex function $w = f(z)$ preserves the local angles between intersecting curves and automatically satisfies Pierre-Simon Laplace's partial differential equation ($\nabla^2\phi = 0$) governing steady, irrotational fluid flow and electrostatic fields.

Before modern wind tunnels and supercomputers existed, how did early twentieth-century aviation pioneers calculate the aerodynamic lift and pressure distribution around a curved airplane wing? Solving the partial differential equations of fluid flow directly around an asymmetric wing profile by hand was virtually impossible. On the other hand, solving the smooth flow of air around a simple **circular cylinder** in the complex $z$-plane—including a circulating vortex of strength $\Gamma$ that pushes the stagnation points downward—was an easy textbook exercise.

In 1910, the Russian aerodynamicist **Nikolai Zhukovsky (Joukowsky)** discovered a breathtaking mathematical bridge between the circle and the airplane wing. Suppose you take every point $z$ on and around a slightly offset circle in the complex plane (whose center is nudged slightly off the origin so the circle passes through the critical point $z = +c$ and encloses $z = -c$) and simply add $z$ to its own scaled complex reciprocal $c^2/z$:

$$\zeta = z + \frac{c^2}{z}$$

See what this elementary complex arithmetic operation ($\mathbf{z} + c^2 \cdot \frac{1}{\mathbf{z}}$) does to the geometry of the circle:
* Near the right-hand point $z = +c$, where the derivative of the map $d\zeta/dz = 1 - c^2/z^2$ vanishes to zero, the smooth circular arc is pinched and folded into a **razor-sharp trailing edge** at $\zeta = +2c$.
* Near the left-hand side of the circle (which extends slightly past $z = -c$), the circle is puffed outward into a **smooth, rounded leading edge**.
* Shifting the center of the circle slightly upward along the imaginary axis bends the centerline into a **cambered upper and lower wing surface** (**Joukowsky airfoil**).

Because the transformation $\zeta = z + c^2/z$ is conformal everywhere outside the circle, it carries the known, exact streamlines around the circular cylinder directly into the physical airflow around the aircraft wing—allowing **Wilhelm Kutta** and **Nikolai Joukowsky** to prove the foundational **Kutta-Joukowsky Lift Theorem** ($L' = \rho_\infty V_\infty \Gamma$), which dictates how circulation around a wing generates the lift that keeps every airliner in the sky.

---

## How Charles Proteus Steinmetz Ended the War of the Currents

For all its beauty in pure mathematics, the moment when $\sqrt{-1}$ stepped out of the ivory tower to build the modern industrial world arrived in **August 1893** at the International Electrical Congress in Chicago.

Throughout the late 1880s and early 1890s, **Thomas Edison** and **George Westinghouse** (backed by **Nikola Tesla's** polyphase patents) had been locked in the fierce **"War of the Currents."** Edison's direct-current (DC) power stations were mathematically simple—Ohm's law was just $V = I \cdot R$—but because DC voltage could not be stepped up easily, copper wire resistance ($P_{\text{loss}} = I^2 R$) burned up so much energy as heat that Edison's stations could barely reach customers a mile away. Tesla and Westinghouse's **alternating current (AC)** solved the transmission problem overnight: transformers could step AC voltage up to tens of thousands of volts for long-distance lines and step it safely back down for homes and factories.

Yet AC brought a mathematical nightmare that brought electrical engineers to their knees. In a DC circuit, current and voltage march in lockstep. In an AC circuit oscillating at $f = 60\text{ Hz}$ (angular frequency $\omega = 2\pi f$), two reactive components throw voltage and current out of step:

- **Inductors ($L$ — coils and transformer windings):** By Michael Faraday's law of induction, an inductor opposes changes in current, $v_L(t) = L \frac{di}{dt}$. Since the derivative of $\sin(\omega t)$ is $\omega\cos(\omega t) = \omega\sin(\omega t + 90^\circ)$, the voltage across an inductor peaks **$90^\circ$ ahead** of the current.
- **Capacitors ($C$ — parallel plates and cable insulation):** A capacitor opposes changes in voltage, $i_C(t) = C \frac{dv}{dt}$, so the voltage across a capacitor lags **$90^\circ$ behind** the current.

Every time an 1890s engineer tried to calculate the voltages and currents inside an AC power grid containing dozens of generators, transformer coils, and capacitive cables, they had to solve coupled systems of second-order differential equations:

$$L \frac{d^2 q}{dt^2} + R \frac{dq}{dt} + \frac{1}{C} q = V_0 \cos(\omega t + \phi)$$

Combining even three sinusoidal waves of different amplitudes and phase angles by trigonometric identities took pages of error-prone algebra.

Then a 28-year-old German immigrant mathematician named **Charles Proteus Steinmetz**—who had fled Bismarck's Germany in 1889 with a brilliant mind, a deformed spine, and almost no money in his pocket—walked up to the podium in Chicago and read a paper titled *"Complex Quantities and Their Use in Electrical Engineering"* {{cite:steinmetz1893}}.

### Steinmetz's Phasor Miracle: Differential Equations Become High-School Algebra

Steinmetz pointed out something breathtakingly simple. In a steady-state AC grid, every voltage and current is rotating at the exact same angular speed $\omega$. Instead of dragging $\cos(\omega t + \theta)$ through pages of calculus, why not freeze the spinning wheel in a strobe light and represent each sinusoidal wave by a single complex number—a **phasor**—recording its amplitude and starting phase angle?

Even better, think about what happens to a rotating complex exponential $e^{j\omega t}$ (where electrical engineers write $j = \sqrt{-1}$ so it is never confused with electrical current $i$) when you take its time derivative $\frac{d}{dt}$:

$$\frac{d}{dt}\left(e^{j\omega t}\right) = j\omega e^{j\omega t}$$

**Differentiation with respect to time is simply multiplication by $j\omega$!** And integration with respect to time is simply division by $j\omega$ (which, since $1/j = -j$, is a $-90^\circ$ rotation).

At a single stroke, Steinmetz's complex phasors vaporized differential calculus from steady-state AC circuit analysis:

1. **Resistors ($R$)** sit on the horizontal **Real Axis**: $\mathbf{Z}_R = R + j0\,\Omega$ ($0^\circ$ phase shift; electrical energy turns irreversibly into heat).
2. **Inductors ($L$)** point straight up the positive **Imaginary Axis**: $\mathbf{Z}_L = +j X_L = +j\omega L\,\Omega$ ($+90^\circ$ phase lead; magnetic energy exchanges losslessly with the source).
3. **Capacitors ($C$)** point straight down the negative **Imaginary Axis**: $\mathbf{Z}_C = -j X_C = -j\frac{1}{\omega C}\,\Omega$ ($-90^\circ$ phase lag; electric-field energy exchanges losslessly with the source).

For any series RLC branch, the total **complex impedance** $\mathbf{Z}$ is just the vector sum of real resistance and net imaginary reactance:

$$\mathbf{Z} = R + j(X_L - X_C) = R + j\left(\omega L - \frac{1}{\omega C}\right)$$

Examine the imaginary part $\omega L - \frac{1}{\omega C}$: because inductive reactance points straight North ($+j$) and capacitive reactance points straight South ($-j$), at the exact frequency where $\omega_0 L = \frac{1}{\omega_0 C}$—the **resonant frequency** $f_0 = \frac{1}{2\pi\sqrt{LC}}$—the $+j$ and $-j$ reactances cancel each other to zero! That is how every radio tuner and wireless receiver selects one station out of the air.

With Steinmetz's phasors, Ohm's law for AC networks is once again simple complex multiplication ($\mathbf{V} = \mathbf{I} \cdot \mathbf{Z}$), series impedances add ($\mathbf{Z}_{\text{series}} = \mathbf{Z}_1 + \mathbf{Z}_2$), and parallel impedances combine by adding their reciprocal **complex admittances** ($\mathbf{Y} = 1/\mathbf{Z} = G + jB$, where $G$ is conductance in Siemens and $B$ is susceptance in Siemens) or via the SC-32's complex harmonic operator **`{{key:CMPLX}} {{key:x∥y}}`**, which combines $\mathbf{Z}_2$ in $(T, Z)$ and $\mathbf{Z}_1$ in $(Y, X)$ in a single keystroke {{cite:horowitz2015}}:

$$\mathbf{Z}_{\text{parallel}} = \mathbf{Z}_1 \parallel \mathbf{Z}_2 = \frac{1}{\frac{1}{\mathbf{Z}_1} + \frac{1}{\mathbf{Z}_2}} = \frac{\mathbf{Z}_1 \mathbf{Z}_2}{\mathbf{Z}_1 + \mathbf{Z}_2}$$

### The Complex Power Triangle, Power Factor Correction, and Maximum Power Transfer

Steinmetz's complex plane also solved one of the most expensive financial mysteries of the early electric utility industry: **Why did factories filled with induction motors draw huge currents through utility transmission lines while registering surprisingly little energy on a wattmeter?**

Suppose an AC generator delivers an RMS voltage phasor $\mathbf{V} = |\mathbf{V}|\angle\theta_v$ and an RMS current phasor $\mathbf{I} = |\mathbf{I}|\angle\theta_i$ to an industrial motor load $\mathbf{Z} = R + jX_L = |\mathbf{Z}|\angle\theta$ (where $\theta = \theta_v - \theta_i$ is the impedance phase angle by which current lags behind voltage). How do we calculate the electrical power delivered to the factory?

If you multiply $\mathbf{V}$ by $\mathbf{I}$ directly, the phase angles *add* ($\theta_v + \theta_i$), which depends on when you started your stopwatch rather than the physical phase difference between voltage and current. Instead, Steinmetz defined **Complex Apparent Power** $\mathbf{S}$ (measured in **Volt-Amperes, VA**) by multiplying the voltage phasor $\mathbf{V}$ by the **complex conjugate of the current phasor**, $\mathbf{I}^* = |\mathbf{I}|\angle(-\theta_i)$:

$$\mathbf{S} = \mathbf{V} \cdot \mathbf{I}^* = |\mathbf{V}||\mathbf{I}|\angle(\theta_v - \theta_i) = |\mathbf{S}|\cos\theta + j|\mathbf{S}|\sin\theta = P + jQ$$

This product forms the right-angled **Power Triangle** $\mathbf{S} = P + jQ$ in the complex plane—giving full algebraic meaning to the geometric $(P = S\cos\phi,\; Q = S\sin\phi)$ vector projection we solved with `{{key:▸y,x}}` in Chapter 4:
1. **Horizontal Leg — Real (Active) Power $P = |\mathbf{V}||\mathbf{I}|\cos\theta = |\mathbf{I}|^2 R$ (measured in Watts, $\text{W}$):** This is the power consumed by the resistive component $R$—the energy that actually turns the factory's lathe spindles, lifts elevators, and lights incandescent bulbs. The dimensionless cosine factor $\text{PF} = \cos\theta = P / |\mathbf{S}|$ is called the **Power Factor**.
2. **Vertical Leg — Reactive (Quadrature) Power $Q = |\mathbf{V}||\mathbf{I}|\sin\theta = |\mathbf{I}|^2 X$ (measured in Volt-Amperes Reactive, $\text{VAR}$):** This is the invisible energy that sloshes back and forth twice every AC cycle between the power plant's alternators and the magnetic fields of the factory's induction motors ($Q > 0$ for lagging inductive loads; $Q < 0$ for leading capacitive loads). Reactive power performs zero net mechanical work over a cycle, yet the utility company's copper transmission lines still have to carry the extra current required to slosh that magnetic energy back and forth, burning up real $I^2 R_{\text{line}}$ heat in the grid.
3. **Hypotenuse — Apparent Power $|\mathbf{S}| = \sqrt{P^2 + Q^2} = |\mathbf{V}||\mathbf{I}|$ (measured in Volt-Amperes, $\text{VA}$):** Because substation transformers must insulate against total voltage $|\mathbf{V}|$ and their copper windings must carry total current $|\mathbf{I}|$ regardless of phase angle, transformers and backup generators are always rated in **$\text{kVA}$ or $\text{MVA}$** rather than kilowatts.

How do industrial plants eliminate that wasteful reactive current sloshing on the power grid? Through **Power Factor Correction**. Because an induction motor draws lagging inductive reactive power $+jQ_L$, wiring a bank of **shunt capacitors** of equal and opposite leading reactive power $-jQ_C = -jQ_L$ directly across the factory's main busbars supplies the motor's magnetic field locally—canceling the imaginary part $j(Q_L - Q_C) = 0$ so the utility transmission line sees a pure real load with unity power factor ($\cos 0^\circ = 1.000$).

And what if you are designing a weak-signal radio receiver, a solar inverter, or an ultrasonic transducer where the goal is not grid efficiency, but extracting the **maximum possible real power $P_{\text{load}}$** from a source whose internal Thévenin impedance is $\mathbf{Z}_{\text{source}} = R_s + jX_s$? If you connect a load $\mathbf{Z}_{\text{load}} = R_L + jX_L$, the loop current magnitude is $|\mathbf{I}| = \frac{|\mathbf{V}_s|}{\sqrt{(R_s + R_L)^2 + (X_s + X_L)^2}}$, and the real power delivered to the load resistor $R_L$ is:

$$P_{\text{load}} = |\mathbf{I}|^2 R_L = \frac{|\mathbf{V}_s|^2 R_L}{(R_s + R_L)^2 + (X_s + X_L)^2}$$

In the denominator $(R_s + R_L)^2 + (X_s + X_L)^2$, how do you make the reactive term $(X_s + X_L)^2$ as small as possible? Since a square can never be negative, you make it **zero** by choosing the load reactance to be the exact negative of the source reactance: $X_L = -X_s$. Once $X_L + X_s = 0$ is canceled out, calculus shows that $\frac{R_L}{(R_s + R_L)^2}$ reaches its peak when $R_L = R_s$. Put those two conditions together ($R_L = R_s$ and $X_L = -X_s$), and you have the **Complex Conjugate Maximum Power Transfer Theorem**:

$$\mathbf{Z}_{\text{load}} = R_s - jX_s = \mathbf{Z}_{\text{source}}^*$$

To extract every last microwatt from a complex source, the load impedance must be the **complex conjugate mirror twin** of the source impedance!

### Audio Filters, Linkwitz-Riley Crossovers, and Zobel Compensation

Steinmetz's complex impedance ratios also explain how high-fidelity loudspeakers split music into bass for the woofer and treble for the tweeter without carving a hole in the sound {{cite:parker2019}}.

First, a moving-coil loudspeaker driver is not a pure $8\,\Omega$ resistor; its copper voice coil wound around an iron magnet pole has series inductance ($R + j\omega L$), causing its impedance to climb at high frequencies. Audio engineers flatten that rising inductive impedance by wiring a conjugate **Zobel compensation network** ($R - jX_C$) in parallel with the voice coil. When two conjugate impedances $Z_1 = R + jX$ and $Z_2 = R - jX$ sit in parallel, their opposite susceptances $\mp jX / (R^2 + X^2)$ cancel identically, presenting the amplifier with a purely real resistance.

Second, in 1930 the British engineer **Stephen Butterworth** designed the "maximally flat" second-order low-pass filter $H(s) = \frac{1}{s^2 + \sqrt{2}s + 1}$. At the normalized crossover frequency $s = j\omega/\omega_c = j$, the $s^2 = j^2 = -1$ term and the $+1$ constant in the denominator cancel completely:

$$H_{\text{Butter2}}(j) = \frac{1}{(-1 + 1) + j\sqrt{2}} = \frac{1}{j\sqrt{2}} = -\frac{j}{\sqrt{2}} \approx 0 - 0.707107j \quad (-3.01\text{ dB}, \text{ phase } -90^\circ)$$

Why, then, do studio monitor loudspeakers avoid using a single second-order Butterworth crossover between the woofer and tweeter? Compare the phase angles at the crossover frequency: the low-pass woofer filter lags by **$-90^\circ$** ($-j/\sqrt{2}$), whereas the high-pass tweeter filter $\frac{s^2}{s^2 + \sqrt{2}s + 1}$ leads by **$+90^\circ$** ($+j/\sqrt{2}$). Because $-90^\circ$ and $+90^\circ$ are **$180^\circ$ out of phase**, the woofer cone pushes forward at the exact instant the tweeter dome pulls backward, canceling the sound at the crossover frequency.

In 1976, **Siegfried Linkwitz** and **Russ Riley** solved this acoustic mystery using complex squaring: if you cascade *two* second-order Butterworth filters in series (forming a fourth-order **Linkwitz-Riley `LR4` crossover**), you square the complex transfer function at crossover:

$$H_{\text{LR4}}(j) = \left[H_{\text{Butter2}}(j)\right]^2 = \left(-\frac{j}{\sqrt{2}}\right)^2 = \frac{j^2}{2} = -0.5000 + 0.0000j \quad (-6.02\text{ dB}, \text{ phase } -180^\circ)$$

Both the woofer and tweeter now sit at half amplitude ($|H| = 0.5$, or $-6.02\text{ dB}$) and share the **exact same phase**, so their sound waves add in the air back to a flat $0.5 + 0.5 = 1.0$ ($0\text{ dB}$) across the room.

### Coaxial Transmission Lines, Standing Waves, and Phillip Smith's Chart

When frequencies climb from audio kilohertz into radio and microwave megahertz and gigahertz, the wavelength of the electromagnetic wave becomes shorter than the coaxial cable carrying it. Now the cable itself acts as a distributed ladder of series impedance per meter ($Z' = R' + j\omega L'$) and shunt admittance per meter ($Y' = G' + j\omega C'$), which **Oliver Heaviside's telegrapher's equations** combine into the cable's **characteristic impedance**:

$$Z_0 = \sqrt{\frac{R' + j\omega L'}{G' + j\omega C'}}$$

When a radio wave traveling down a $Z_0 = 50\,\Omega$ coaxial line reaches an antenna whose complex load impedance $\mathbf{Z}_L = R_L + jX_L$ does not match $Z_0$, part of the wave bounces back toward the transmitter. In 1939, Bell Labs engineer **Phillip H. Smith** realized that the complex **voltage reflection coefficient** $\mathbf{\Gamma}$ (which Vector Network Analyzers measure as $S_{11}$):

$$\mathbf{\Gamma} = \frac{\mathbf{Z}_L - Z_0}{\mathbf{Z}_L + Z_0}$$

maps every passive impedance ($R_L \ge 0$) inside the unit circle $|\mathbf{\Gamma}| \le 1$, creating the **Smith Chart**. On the stack, subtracting $Z_0$ from the real part $R_L$ in Register $Y$ while recovering $Z_0$ via **`{{key:LASTX}}`** (or adding $2Z_0$) builds both the numerator $\mathbf{Z}_L - Z_0$ in $(T, Z)$ and denominator $\mathbf{Z}_L + Z_0$ in $(Y, X)$ for `{{key:CMPLX}} {{key:÷}}`. Converting $\mathbf{\Gamma}$ to polar magnitude $|\mathbf{\Gamma}|$ via `{{key:x⇄y}} {{key:▸θ,r}}` then gives both the **Return Loss** ($\text{RL} = -20\log_{10}|\mathbf{\Gamma}|$ in dB) and the **Voltage Standing Wave Ratio ($\text{VSWR}$)** along the cable:

$$\text{VSWR} = \frac{1 + |\mathbf{\Gamma}|}{1 - |\mathbf{\Gamma}|}$$

And when an RF engineer needs to match a real antenna impedance $Z_L$ (say $100\,\Omega$) to a feedline $Z_0$ ($50\,\Omega$) without reflections, inserting a **quarter-wave ($\lambda/4$) transmission-line section** of geometric-mean characteristic impedance $Z_{\text{line}} = \sqrt{Z_0 Z_L}$ ($\approx 70.71\,\Omega$, so $Z_{\text{in}} = Z_{\text{line}}^2 / Z_L = Z_0$) cancels the reflected wave through destructive interference—the exact radio-frequency twin of an anti-reflective $\sqrt{n_{\text{air}} n_{\text{glass}}}$ optical coating on a camera lens!

---

## On the Stack: Complex Numbers & AC Phasors Workbench

Consider what our working memory had to hold as we unpeeled every complex problem in this chapter—from Bombelli's cubic and Euler's $e^{i\pi}$ to Steinmetz's parallel impedances and Smith's reflection ratio $\frac{\mathbf{Z}_L - Z_0}{\mathbf{Z}_L + Z_0}$. Unlike a real scalar that needs only a single shelf, a complex number $\mathbf{z} = a + bi$ is a **paired two-dimensional quantity**: a Real part and an Imaginary part traveling together. Because the SC-32 has **four** visible stack registers ($T, Z, Y, X$), pairing the lower two shelves $(Y = \text{Real}, X = \text{Imag})$ for one complex number and the upper two shelves $(T = \text{Real}, Z = \text{Imag})$ for a second complex number turns the four-level stack into a natural two-phasor workbench—with zero complex-mode lockups and zero parentheses.

{{res:sc32_phasor_polar:screenshot|Impedance phasor 3 + j4 rectangular-to-polar conversion on the SC-32, resolving magnitude r = 5 in Register X and phase angle theta = 53.1301 deg in Register Y.}}

### How Two Complex Numbers Fit on Four Registers

Where the 1982 HP-15C hid imaginary components inside a separate parallel stack {{cite:hp15c1982}} and the single-line 1991 HP-32SII stored $(Y = \text{Imag}, X = \text{Real})$ (forcing you to enter $a + bi$ backward as `b ENTER a`), the four-line StackCalc SC-32 pairs **$(Y = \text{Real}, X = \text{Imag})$** directly on the visible display so that keying `a {{key:ENTER}} b` in natural left-to-right reading order places $a$ on Line $Y$ and $b$ on Line $X$:

$$\mathbf{z} = Y + X i$$

| Register / Display | Complex Plane Component | Mathematical Notation | Display Appearance ($z = a + bi$) |
| :--- | :--- | :---: | :--- |
| **Register $Y$ (Line 2)** | Real Part | $\operatorname{Re}(\mathbf{z})$ | $a$ (Upper line on transflective LCD) |
| **Register $X$ (Line 1)** | Imaginary Part | $\operatorname{Im}(\mathbf{z})$ | $b$ (Active prompt line on transflective LCD) |

You never have to lock the SC-32 into a special mode to work with complex numbers. Whenever you want an operator to treat the stack as paired complex numbers, press Left Shift `{{key:↰}}` followed by the transient prefix **`{{key:CMPLX}}`** right before the function key (pressing `{{key:C}}` cancels the prefix if tapped by mistake). Unless a problem explicitly specifies degrees (`{{key:DEG}}`), complex sequences in this workbench assume radian mode (`{{key:RAD}}`). Internally, binary complex division (`{{key:CMPLX}} {{key:÷}}`) uses **Robert L. Smith's (1962) scaling algorithm**, pivoting on $d/c$ or $c/d$ so $c^2 + d^2$ never suffers premature overflow.

Because one complex number occupies two adjacent registers, the four-register stack holds **two complete complex numbers simultaneously**—$\mathbf{z}_2 = T + Zi$ in the upper pair $(T, Z)$ and $\mathbf{z}_1 = Y + Xi$ in the lower pair $(Y, X)$:

| Operation Class | Key Sequence | Input Stack | Output in $(Y, X)$ | Upper Stack $(T, Z)$ |
| :--- | :--- | :--- | :--- | :--- |
| **Complex Negation** | `{{key:CMPLX}} {{key:+/-}}` | $\mathbf{z}_1 = Y + Xi$ | $-Y - Xi$ | Preserved ($T, Z$ unchanged) |
| **Unary Complex Functions** | `{{key:CMPLX}}` + `{{key:√x}}`, `{{key:1/x}}`, `{{key:x²}}`, `{{key:eˣ}}`, `{{key:LN}}`, `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}` | $\mathbf{z}_1 = Y + Xi$ | $f(\mathbf{z}_1)$ | Preserved ($T, Z$ unchanged) |
| **Binary Complex Arithmetic** | `{{key:CMPLX}}` + `{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`, `{{key:yˣ}}` | $\mathbf{z}_2 = T + Zi$, $\mathbf{z}_1 = Y + Xi$ | $\mathbf{z}_2 \mathbin{\text{op}} \mathbf{z}_1$ | 2-level drop ($T \to Z, T$) |
| **Complex Parallel Impedance** | `{{key:CMPLX}} {{key:x∥y}}` | $\mathbf{z}_2 = T + Zi$, $\mathbf{z}_1 = Y + Xi$ | $\dfrac{\mathbf{z}_2 \mathbf{z}_1}{\mathbf{z}_2 + \mathbf{z}_1}$ | 2-level drop ($T \to Z, T$) |

To load $\mathbf{z}_A = a + bi$ into $(T, Z)$ and $\mathbf{z}_B = c + di$ into $(Y, X)$, enter the four numbers in reading order: key `a {{key:ENTER}} b {{key:ENTER}} c {{key:ENTER}} d`, then press `{{key:CMPLX}}` and your binary operator.

Let us begin with the damped mechanical suspension from Section 1 ($m = 2\text{ kg}$, so $2m = 4\text{ kg}$; damping $c = 8\text{ N}\cdot\text{s/m}$; spring stiffness $k = 50\text{ N/m}$, so $\omega_0^2 = k/m = 25\text{ s}^{-2}$), where $\lambda = -\frac{c}{2m} \pm i\sqrt{\frac{k}{m} - \left(\frac{c}{2m}\right)^2} = -2.0 \pm i\sqrt{25 - 4} = -2.0 \pm i\sqrt{21} \approx -2.0 \pm 4.582576i$. Computing the real decay rate $\alpha = -c/(2m) = -2.0\text{ s}^{-1}$ in Register $Y$ and the damped ringing frequency $\omega_d = \sqrt{\omega_0^2 - \alpha^2} = \sqrt{21}\text{ rad/s}$ in Register $X$ places the eigenvalue pair directly on the stack:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `8 {{key:ENTER}} 4 {{key:÷}} {{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-2.0000$ | Real damping rate $\alpha = -c/(2m) = -8/4 = -2.0\text{ s}^{-1}$ |
| `4 {{key:ENTER}} 25 {{key:-}} {{key:+/-}}` | $0.0000$ | $0.0000$ | $-2.0000$ | $21.0000$ | Form $\omega_0^2 - \alpha^2 = 25 - 4 = 21.0\text{ s}^{-2}$ ($\alpha$ lifts to $Y$) |
| `{{key:√x}}` | $0.0000$ | $0.0000$ | $-2.0000$ | **$4.582576$** | Damped angular frequency $\omega_d = 4.5826\text{ rad/s}$ |
| `{{key:SHOW}}` | $0.0000$ | $0.0000$ | **$-2.000000$** | **$4.582576$** | Complex conjugate eigenvalues $\lambda = -2.0 \pm 4.5826i$ |

Next, let us test four foundational complex primitives:

1. **Verifying a Complex Quadratic Root ($z^2 - 4z + 13 = 0$ at $z_1 = 2 + 3i$):** Substituting $z_1 = 2 + 3i$ gives $(2+3i)^2 - 4(2+3i) + 13 = (-5 + 12i) - (8 + 12i) + 13 = 0 + 0i$. Squaring $2 + 3i$ in place (`2 {{key:ENTER}} 3 {{key:CMPLX}} {{key:x²}}`), subtracting $8 + 12i$, and adding $13 + 0i$ verifies zero residual across both registers:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2 {{key:ENTER}} 3` | $0.0000$ | $0.0000$ | $2.0000$ | $3.0000$ | Candidate complex root $z_1 = 2 + 3i$ loaded |
| `{{key:CMPLX}} {{key:x²}}` | $0.0000$ | $0.0000$ | $-5.0000$ | $12.0000$ | Complex square $z_1^2 = -5 + 12i$ in place |
| `8 {{key:ENTER}} 12 {{key:CMPLX}} {{key:-}}` | $-5.0000$ | $-5.0000$ | $-13.0000$ | $0.0000$ | Subtract $4z_1 = 8 + 12i$ |
| `13 {{key:ENTER}} 0 {{key:CMPLX}} {{key:+}}` | $-13.0000$ | $-13.0000$ | **$0.0000$** | **$0.0000$** | Add $13 + 0i$; residual $= 0.0 + 0.0i$ |

2. **Conjugate Multiplication ($z \cdot z^*$ for $z = 6 + 8i$):** Multiplying $z = 6 + 8i$ by its conjugate $z^* = 6 - 8i$ gives $6^2 + 8^2 = 100 + 0i$. Keying `{{res:sc32_05_complex_numbers_phasors_seq_08:keys}}` loads $6 + 8i$ into $(T, Z)$ and $6 - 8i$ into $(Y, X)$ and multiplies them via `{{key:CMPLX}} {{key:×}}`, leaving $(Y = 100.0000,\; X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_08:value}}})$.

3. **Spacecraft Re-Entry Plasma Permittivity ($\epsilon_r = 1 - \frac{\omega_p^2}{\omega(\omega - j\nu)}$):** When a capsule plunges into the upper atmosphere at hypersonic speed, shock heating ionizes the surrounding air into a conducting plasma sheath of plasma frequency $\omega_p$ and electron collision rate $\nu$ that attenuates and reflects telemetry radio waves (causing re-entry radio blackout when $\operatorname{Re}(\epsilon_r) \le 0$). For normalized $\omega_p = 1$, $\omega = 2$, and collision rate $\nu = 0.5$, the denominator is $\omega(\omega - j\nu) = 4.0 - 1.0i$. Inverting $4 - i$ in place via `{{key:CMPLX}} {{key:1/x}}`, negating with `{{key:CMPLX}} {{key:+/-}}`, and adding $1 + 0i$ yields $\epsilon_r = \mathbf{0.764706 - 0.058824i}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4 {{key:ENTER}} 1 {{key:+/-}}` | $0.0000$ | $0.0000$ | $4.0000$ | $-1.0000$ | Scaled denominator $z = 4.0 - 1.0i$ |
| `{{key:CMPLX}} {{key:1/x}} {{key:CMPLX}} {{key:+/-}}` | $0.0000$ | $0.0000$ | $-0.235294$ | $-0.058824$ | Negated reciprocal $-1/(4-i)$ |
| `1 {{key:ENTER}} 0` | $-0.235294$ | $-0.058824$ | $1.0000$ | $0.0000$ | Unit real reference $1.0 + 0i$ in $(Y, X)$ |
| `{{key:CMPLX}} {{key:+}}` | $-0.235294$ | $-0.235294$ | **$0.764706$** | **$-0.058824$** | Add unity: $\epsilon_r = 0.7647 - 0.0588i$ |

4. **Joukowsky Airfoil Mapping ($\zeta = z + 1/z$ at $z = 1.1 + 0.2i$):** Loading $z = 1.1 + 0.2i$ into both $(T, Z)$ and $(Y, X)$ via `1.1 {{key:ENTER}} 0.2 {{key:ENTER}} 1.1 {{key:ENTER}} 0.2 {{key:CMPLX}} {{key:1/x}} {{key:CMPLX}} {{key:+}}` inverts $(Y, X)$ in place ($\to 0.880000 - 0.160000i$) while preserving $z$ in $(T, Z)$, then adds them to map the cylinder point to the airfoil coordinate $(Y = \mathbf{1.980000},\; X = \mathbf{0.040000})$.

### A Live Stack Proof of Euler's Identity

With the SC-32 in **Radians mode (`{{key:RAD}}`)**, we can verify Euler's formula $e^{i\pi} = -1 + 0i$ live on the stack. We enter the pure imaginary exponent $0 + \pi i$ by placing Real $= 0$ in Register $Y$ and Imaginary $= \pi$ in Register $X$, and evaluate `{{res:sc32_05_complex_numbers_phasors_seq_01:keys}}`:

| Keystroke | Register T | Register Z | Register Y (Real) | Register X (Imag) | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Real exponent $0.0$ entered in $X$ (lifts to $Y$ when $\pi$ is pressed) |
| `{{key:π}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.14159265359$ | Imaginary exponent $\pi$ entered in $X$; $0.0$ lifts to $Y$ |
| `{{key:CMPLX}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.14159265359$ | `{{key:CMPLX}}` annunciator illuminated |
| `{{key:eˣ}}` | $0.0000$ | $0.0000$ | **-1.0000000000** | **0.0000000000** | $e^{0 + \pi i} = -1.0 + 0.0i$ |

To complete Euler's Identity $e^{i\pi} + 1 = 0$, we add $+1 + 0i$ via `{{res:sc32_05_complex_numbers_phasors_seq_30:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_30:value}}`**, bringing both Register $Y$ and Register $X$ to exact **$0.0000000000$**. You can also verify the inverse principal complex logarithm $\ln(-1) = i\pi$: keying `{{res:sc32_05_complex_numbers_phasors_seq_31:keys}}` evaluates $e^{i\pi} = -1 + 0i$ via `{{key:CMPLX}} {{key:eˣ}}` and immediately inverts it via `{{key:CMPLX}} {{key:LN}}` to recover $0.0000000000 + 3.1415926536i$.

### De Moivre Powers, Roots of Unity & Complex Trigonometry

In Chapter 4, the Euclidean vector keys `{{key:▸θ,r}}` and `{{key:▸y,x}}` expected vertical $y$ in Register $Y$ and horizontal $x$ in Register $X$. Because Gaussian complex format places Real ($x$) in Register $Y$ and Imaginary ($y$) in Register $X$, **`{{key:x⇄y}}` is the one-keystroke bridge between Gaussian complex $(Y = \text{Real}, X = \text{Imag})$ and polar $(\theta, r)$ coordinates**. (Watch out for the **Complementary Angle Trap**: if you press `{{key:▸θ,r}}` on $(Y = \text{Real}, X = \text{Imag})$ without pressing `{{key:x⇄y}}` first, `{{key:▸θ,r}}` computes $\operatorname{atan2}(\text{Real}, \text{Imag}) = 90^\circ - \theta$, the complementary angle! Always swap with `{{key:x⇄y}}` before `{{key:▸θ,r}}` and after `{{key:▸y,x}}`):

- **Complex $(Y = \text{Real}, X = \text{Imag}) \to$ Polar $(Y = \theta, X = r)$:** Press `{{key:x⇄y}} {{key:▸θ,r}}`.
- **Polar $(Y = \theta, X = r) \to$ Complex $(Y = \text{Real}, X = \text{Imag})$:** Press `{{key:▸y,x}} {{key:x⇄y}}`.

Here is the round-trip conversion of $\mathbf{z} = 3 + 4i$ in `{{key:RAD}}` mode (where $\theta = 0.927295\text{ rad}$ equals the $\theta = 53.1301^\circ$ shown in `{{key:DEG}}` mode in the workbench screenshot above):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3 {{key:ENTER}} 4` | $0.0000$ | $0.0000$ | $3.0000$ | $4.0000$ | Gaussian complex coordinates $(Y=\text{Real}, X=\text{Imag})$ |
| `{{key:x⇄y}} {{key:▸θ,r}}` | $0.0000$ | $0.0000$ | $0.927295$ | **$5.000000$** | Polar conversion: $\theta = 0.9273\text{ rad}$ ($53.1301^\circ$) in $Y$, magnitude $r$ in $X$ |
| `{{key:▸y,x}}` | $0.0000$ | $0.0000$ | $4.000000$ | **$3.000000$** | Rectangular conversion: horizontal $x$ in $X$, vertical $y$ in $Y$ |
| `{{key:x⇄y}}` | $0.0000$ | $0.0000$ | **$3.000000$** | **$4.000000$** | Realign to Gaussian complex format: Real in $Y$, Imag in $X$ |

In **Degrees mode (`{{key:DEG}}`)**, we can use `{{key:▸y,x}} {{key:x⇄y}}` to verify Fortescue's three-phase neutral cancellation $1 + a + a^2 = 0$ for the cube roots of unity $a = 1\angle 120^\circ = -0.5 + 0.866025i$ and $a^2 = 1\angle 240^\circ = -0.5 - 0.866025i$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `120 {{key:ENTER}} 1 {{key:▸y,x}} {{key:x⇄y}}` | $0.0000$ | $0.0000$ | $-0.500000$ | $0.866025$ | Polar to Gaussian: $a = -0.5 + 0.8660i$ |
| `240 {{key:ENTER}} 1 {{key:▸y,x}} {{key:x⇄y}}` | $-0.500000$ | $0.866025$ | $-0.500000$ | $-0.866025$ | Polar to Gaussian: $a^2 = -0.5 - 0.8660i$ |
| `{{key:CMPLX}} {{key:+}}` | $-0.500000$ | $-0.500000$ | $-1.000000$ | $0.000000$ | Complex sum: $a + a^2 = -1.0 + 0.0i$ |
| `1 {{key:ENTER}} 0 {{key:CMPLX}} {{key:+}}` | $-1.000000$ | $-1.000000$ | **$0.000000$** | **$0.000000$** | Add $+1$ reference: $1 + a + a^2 = 0 + 0i$ |

Returning to **Radians mode (`{{key:RAD}}`)**, let us evaluate De Moivre roots, complex powers, and analytic continuation on the stack:

- **Principal Square Root of $i$ ($\sqrt{0 + 1i} = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}i$):** Keying `{{res:sc32_05_complex_numbers_phasors_seq_09:keys}}` bisects the $90^\circ$ angle to $45^\circ$, leaving $Y = \mathbf{0.707107}$ and $X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_09:value}}}$.
- **Principal Cube Root of $-8$ ($8^{1/3}e^{i\pi/3} = 1 + i\sqrt{3}$):** Loading $-8 + 0i$ into $(T, Z)$ with a 6-digit decimal exponent $0.333333 + 0i$ in $(Y, X)$ via `{{res:sc32_05_complex_numbers_phasors_seq_18:keys}}` yields the approximate imaginary part **`{{res:sc32_05_complex_numbers_phasors_seq_18:value}}`** in Register $X$, whereas forming the full-precision rational exponent $1/3 + 0i$ in $(Y, X)$ via `{{res:sc32_05_complex_numbers_phasors_seq_19:keys}}` produces the exact principal root $(Y = \mathbf{1.000000},\; X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_19:value}}})$.
- **General Complex Power $(1 + i)^{(1 - i)}$ and $i^i$:** Loading base $\mathbf{z}_2 = 1 + i$ into $(T, Z)$ and exponent $\mathbf{z}_1 = 1 - i$ into $(Y, X)$ and pressing `{{key:CMPLX}} {{key:yˣ}}` evaluates $e^{(1-i)\ln(1+i)} = \mathbf{2.807879 + 1.317865i}$ (and keying `0 {{key:ENTER}} 1 {{key:ENTER}} 0 {{key:ENTER}} 1 {{key:CMPLX}} {{key:yˣ}}` confirms $i^i = e^{-\pi/2} = \mathbf{0.207880 + 0.000000i}$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:ENTER}} 1 {{key:ENTER}}` | $0.0000$ | $1.0000$ | $1.0000$ | $1.0000$ | Base $z_2 = 1 + i$ loaded into $(T, Z)$ |
| `1 {{key:ENTER}} 1 {{key:+/-}}` | $1.0000$ | $1.0000$ | $1.0000$ | $-1.0000$ | Exponent $z_1 = 1 - i$ loaded into $(Y, X)$ |
| `{{key:CMPLX}} {{key:yˣ}}` | $1.0000$ | $1.0000$ | **$2.807879$** | **$1.317865$** | General complex power $z_2^{z_1}$ evaluated |

- **Complex Sine, Cosine & Analytic Continuation ($\sin^2 z + \cos^2 z = 1$ at $z = 1 + 2i$):** Keying `{{res:sc32_05_complex_numbers_phasors_seq_21:keys}}` evaluates $\sin(1 + 2i) = \sin(1)\cosh(2) + i\cos(1)\sinh(2)$ in place, yielding $(Y = \mathbf{3.165779},\; X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_21:value}}})$. Keying `{{res:sc32_05_complex_numbers_phasors_seq_22:keys}}` evaluates $\cos(1 + 2i) = \cos(1)\cosh(2) - i\sin(1)\sinh(2)$, yielding $(Y = \mathbf{2.032723},\; X = \mathbf{{{res:sc32_05_complex_numbers_phasors_seq_22:value}}})$. Squaring both complex outputs and summing them confirms $\sin^2(1+2i) + \cos^2(1+2i) = 1 + 0i$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3.165779 {{key:ENTER}} 1.959601` | $0.0000$ | $0.0000$ | $3.165779$ | $1.959601$ | Load $\sin(1+2i)$ from above |
| `{{key:CMPLX}} {{key:x²}}` | $0.0000$ | $0.0000$ | $6.182115$ | $12.407147$ | Square complex sine $(\sin z)^2$ |
| `2.032723 {{key:ENTER}} 3.051898 {{key:+/-}}` | $6.182115$ | $12.407147$ | $2.032723$ | $-3.051898$ | Load $\cos(1+2i)$ from above |
| `{{key:CMPLX}} {{key:x²}}` | $6.182115$ | $12.407147$ | $-5.182115$ | $-12.407147$ | Square complex cosine $(\cos z)^2$ |
| `{{key:CMPLX}} {{key:+}}` | $6.182115$ | $6.182115$ | **$1.000000$** | **$0.000000$** | Sum squares: $\sin^2 z + \cos^2 z = 1 + 0i$ |

### AC Impedance, Crossovers & Transmission Lines

Now let us walk through Steinmetz's AC phasor networks, Linkwitz-Riley crossovers, and RF transmission lines on the stack:

1. **Series AC Impedance Addition ($\mathbf{Z}_1 = 8.0 + 4.0i\,\Omega$ and $\mathbf{Z}_2 = 4.0 - 8.0i\,\Omega$):** Keying `{{res:sc32_05_complex_numbers_phasors_seq_02:keys}}` loads $\mathbf{Z}_2$ into $(T, Z)$ and $\mathbf{Z}_1$ into $(Y, X)$ and adds them via `{{key:CMPLX}} {{key:+}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $4.0000$ | $4.0000$ | Real part of $\mathbf{Z}_2$ pushed |
| `8 {{key:+/-}} {{key:ENTER}}` | $0.0000$ | $4.0000$ | $-8.0000$ | $-8.0000$ | Imag part of $\mathbf{Z}_2$ pushed |
| `8 {{key:ENTER}}` | $4.0000$ | $-8.0000$ | $8.0000$ | $8.0000$ | Real part of $\mathbf{Z}_1$ pushed |
| `4` | **$4.0000$** | **$-8.0000$** | **$8.0000$** | **$4.0000$** | Complete 4-register setup |
| `{{key:CMPLX}} {{key:+}}` | $4.0000$ | $4.0000$ | **$12.000000$** | **$-4.000000$** | $\mathbf{Z}_{\text{total}} = 12.0 - 4.0i\,\Omega$ |

2. **Parallel AC Impedance ($\mathbf{Z}_1 = 20 + 15i\,\Omega \parallel \mathbf{Z}_2 = 10 - 25i\,\Omega$):** To inspect the individual branch admittances $\mathbf{Y}_k = 1/\mathbf{Z}_k = G_k + jB_k$ before combining them, first invert Branch 1 via `{{res:sc32_05_complex_numbers_phasors_seq_03:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_03:value}}`** ($\mathbf{Y}_1 = 0.032000 - 0.024000i\,\text{S}$), and then load and invert Branch 2 in place via `{{res:sc32_05_complex_numbers_phasors_seq_04:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_04:value}}`** ($\mathbf{Y}_2 = 0.013793 + 0.034483i\,\text{S}$ while $\mathbf{Y}_1$ rests untouched in $T, Z$). Summing the two admittances and re-inverting via `{{res:sc32_05_complex_numbers_phasors_seq_05:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_05:value}}`** resolves the parallel impedance $\mathbf{Z}_{\text{parallel}} = \mathbf{20.7516 - 4.7507i\,\Omega}$ (which you can also compute in a single stroke via `20 {{key:ENTER}} 15 {{key:ENTER}} 10 {{key:ENTER}} 25 {{key:+/-}} {{key:CMPLX}} {{key:x∥y}}`):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `20 {{key:ENTER}} 15 {{key:CMPLX}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.032000$ | $-0.024000$ | Branch 1 admittance $\mathbf{Y}_1$ in $(Y, X)$ |
| `10 {{key:ENTER}} 25 {{key:+/-}} {{key:CMPLX}} {{key:1/x}}` | $0.032000$ | $-0.024000$ | $0.013793$ | $0.034483$ | $\mathbf{Y}_1$ lifts to $(T, Z)$; $\mathbf{Y}_2$ in $(Y, X)$ |
| `{{key:CMPLX}} {{key:+}}` | $0.032000$ | $0.032000$ | $0.045793$ | $0.010483$ | Sum admittances: $\mathbf{Y}_{\text{parallel}} = \mathbf{Y}_1 + \mathbf{Y}_2$ |
| `{{key:CMPLX}} {{key:1/x}}` | $0.032000$ | $0.032000$ | **$20.7516$** | **$-4.7507$** | Invert admittance: $\mathbf{Z}_{\text{parallel}} = 20.75 - 4.75i\,\Omega$ |

3. **Zobel Conjugate Loudspeaker Compensation ($Z_1 = 3 + 4i\,\Omega \parallel Z_2 = 3 - 4i\,\Omega$):** Because the opposite susceptances $\mp 0.16i\,\text{S}$ cancel, inverting $3 + 4i$, doubling the real conductance $G = 0.12\,\text{S}$, and inverting via `{{res:sc32_05_complex_numbers_phasors_seq_32:keys}}` (or `3 {{key:ENTER}} 4 {{key:ENTER}} 3 {{key:ENTER}} 4 {{key:+/-}} {{key:CMPLX}} {{key:x∥y}}`) yields the purely resistive load **$4.166667\,\Omega$**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3 {{key:ENTER}} 4` | $0.0000$ | $0.0000$ | $3.0000$ | $4.0000$ | Load branch impedance $Z_1 = 3 + 4i$ |
| `{{key:CMPLX}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.120000$ | $-0.160000$ | Invert: $Y_1 = 0.12 - 0.16i\,\text{S}$ |
| `{{key:x⇄y}}` | $0.0000$ | $0.0000$ | $-0.160000$ | $0.120000$ | Swap real conductance to Register $X$ |
| `2 {{key:×}}` | $0.0000$ | $0.0000$ | $-0.160000$ | $0.240000$ | Double conductance (imag parts cancel) |
| `{{key:1/x}}` | $0.0000$ | $0.0000$ | $-0.160000$ | **$4.166667$** | Invert net conductance: $Z_{\text{parallel}} = 4.1667\,\Omega$ |

4. **Thévenin AC Impedance Bridge ($Z_{\text{th}} = (Z_A \parallel Z_C) + (Z_B \parallel Z_D)$):** For $Z_A = 10 + 20i\,\Omega$, $Z_C = 20 + 0i\,\Omega$, $Z_B = 30 - 10i\,\Omega$, and $Z_D = 0 - 25i\,\Omega$, `{{key:CMPLX}} {{key:x∥y}}` resolves each parallel arm in one stroke:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `10 {{key:ENTER}} 20 {{key:ENTER}} 20 {{key:ENTER}} 0` | $10.0000$ | $20.0000$ | $20.0000$ | $0.0000$ | Load branch impedances $Z_A$ and $Z_C$ |
| `{{key:CMPLX}} {{key:x∥y}}` | $10.0000$ | $10.0000$ | $10.7692$ | $6.1538$ | Parallel branch $Z_{AC} = Z_A \parallel Z_C$ |
| `30 {{key:ENTER}} 10 {{key:+/-}} {{key:ENTER}} 0 {{key:ENTER}} 25 {{key:+/-}}` | $30.0000$ | $-10.0000$ | $0.0000$ | $-25.0000$ | Load branch impedances $Z_B$ and $Z_D$ |
| `{{key:CMPLX}} {{key:x∥y}}` | $30.0000$ | $30.0000$ | $8.8235$ | $-14.7059$ | Parallel branch $Z_{BD} = Z_B \parallel Z_D$ |
| `10.7692 {{key:ENTER}} 6.1538 {{key:CMPLX}} {{key:+}}` | $8.8235$ | $8.8235$ | **$19.5928$** | **$-8.5520$** | Sum branches: $Z_{\text{th}} = Z_{BD} + Z_{AC}$ |

*(Tip: To preserve all 16 internal digits of $Z_{AC}$ without re-typing `10.7692` and `6.1538`, either park $Z_{AC}$ in Variables `A` and `B` via `{{key:STO}} B {{key:x⇄y}} {{key:STO}} A` before loading $Z_B$ and $Z_D$, or switch `{{key:FLAGS}}` to `{{key:8-LVL}}` stack mode so $Z_{AC}$ rides up to $(B, A)$ while $Z_B \parallel Z_D$ resolves in $(Y, X)$, then press `{{key:CMPLX}} {{key:+}}` immediately!)*

5. **Butterworth & Linkwitz-Riley (`LR4`) Audio Crossovers and Active Filter Gain:** At normalized cutoff $s = j$, the second-order Butterworth denominator is $B_2(j) = 0 + \sqrt{2}i \approx 0 + 1.414214i$; inverting via `{{res:sc32_05_complex_numbers_phasors_seq_23:keys}}` yields $H_{\text{Butter2}}(j) = \mathbf{0.000000 - 0.707107i}$ ($-3.01\text{ dB}$, $-90^\circ$). Cascading two stages into a Linkwitz-Riley `LR4` crossover squares $0 - i/\sqrt{2}$ in place to give $-0.500000 + 0.000000i$ ($-6.02\text{ dB}$, $-180^\circ$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0 {{key:ENTER}} 2 {{key:√x}} {{key:1/x}} {{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-0.707107$ | Construct exact Butterworth response $0 - i/\sqrt{2}$ |
| `{{key:CMPLX}} {{key:x²}}` | $0.0000$ | $0.0000$ | **$-0.500000$** | **$0.000000$** | Evaluate $[H_{\text{Butter2}}]^2$; Real in $Y$, Imag in $X$ |
| `{{key:x⇄y}} {{key:ABS}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.500000$ | Inspect Real component magnitude $\lvert H\rvert = 0.5$ |
| `{{key:LOG}} 20 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$-6.020600$** | Calculate $-6.02\text{ dB}$ acoustic crossover attenuation |

Similarly, in an inverting operational-amplifier bandpass stage where a virtual-ground summing node forces the closed-loop complex voltage gain to equal the negative impedance ratio $A_v = -\mathbf{Z}_f / \mathbf{Z}_{\text{in}}$, pairing feedback impedance $\mathbf{Z}_f = 5000 - 5000i\,\Omega$ with input impedance $\mathbf{Z}_{\text{in}} = 1000 - 1000i\,\Omega$ via `{{res:sc32_05_complex_numbers_phasors_seq_25:keys}}` evaluates $A_v = -\mathbf{Z}_f / \mathbf{Z}_{\text{in}} = \mathbf{-5.000000}$ + **`{{res:sc32_05_complex_numbers_phasors_seq_25:value}}`** $i$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `5000 {{key:ENTER}} 5000 {{key:+/-}} {{key:ENTER}}` | $0.0000$ | $5000.0000$ | $-5000.0000$ | $-5000.0000$ | Feedback impedance $Z_f$ pushed |
| `1000 {{key:ENTER}} 1000 {{key:+/-}}` | $5000.0000$ | $-5000.0000$ | $1000.0000$ | $-1000.0000$ | Input impedance $Z_{\text{in}}$ in $(Y, X)$ |
| `{{key:CMPLX}} {{key:÷}}` | $5000.0000$ | $5000.0000$ | $5.000000$ | $0.000000$ | Complex ratio $Z_f / Z_{\text{in}} = 5.0 + 0i$ |
| `{{key:CMPLX}} {{key:+/-}}` | $5000.0000$ | $5000.0000$ | **$-5.000000$** | **$0.000000$** | Negate gain: $A_v = -5.0 + 0i$ |

6. **RF Transmission Lines, Reflection Coefficient ($\mathbf{\Gamma}$), $\text{VSWR}$ & Quarter-Wave Matching:** Terminating a $Z_0 = 50\,\Omega$ coax line with a dipole antenna $\mathbf{Z}_L = 75 + 40i\,\Omega$, $\mathbf{\Gamma} = \frac{\mathbf{Z}_L - Z_0}{\mathbf{Z}_L + Z_0} = \frac{25 + 40i}{125 + 40i} = 0.274311 + 0.232221i$, with polar magnitude $|\mathbf{\Gamma}| = 0.359406$. From $|\mathbf{\Gamma}|$, `{{res:sc32_05_complex_numbers_phasors_seq_06:keys}}` gives $\text{VSWR} = \mathbf{2.1221}$ and `{{res:sc32_05_complex_numbers_phasors_seq_07:keys}}` gives Return Loss $\text{RL} = \mathbf{8.89\text{ dB}}$ ($8.8883\text{ dB}$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `25 {{key:ENTER}} 40 {{key:ENTER}}` | $0.0000$ | $25.0000$ | $40.0000$ | $40.0000$ | Numerator $Z_L - Z_0 = (75-50) + 40i$ pushed |
| `125 {{key:ENTER}} 40` | $25.0000$ | $40.0000$ | $125.0000$ | $40.0000$ | Denominator $Z_L + Z_0 = (75+50) + 40i$ in $(Y, X)$ |
| `{{key:CMPLX}} {{key:÷}}` | $25.0000$ | $25.0000$ | **$0.274311$** | **$0.232221$** | Reflection coefficient $\mathbf{\Gamma} = 0.2743 + 0.2322i$ |
| `{{key:x⇄y}} {{key:▸θ,r}}` | $25.0000$ | $25.0000$ | $0.702494$ | **$0.359406$** | Polar: Phase $\theta = 0.702494\text{ rad}$ ($40.25^\circ$) in $Y$, magnitude $\lvert\mathbf{\Gamma}\rvert = 0.3594$ in $X$ |
| `{{key:ENTER}} {{key:ENTER}} 1 {{key:+}} {{key:x⇄y}} 1 {{key:x⇄y}} {{key:-}} {{key:÷}}` | $0.702494$ | $0.702494$ | $0.702494$ | **$2.1221$** | VSWR $= (1+\lvert\mathbf{\Gamma}\rvert)/(1-\lvert\mathbf{\Gamma}\rvert) = 2.1221$ |

For a microwave port with measured VNA reflection $S_{11} = 0.25 - 0.40i$ ($|S_{11}| = 0.471699$), keying `{{res:sc32_05_complex_numbers_phasors_seq_16:keys}}` converts $S_{11}$ to polar magnitude and evaluates Return Loss $\text{RL} = -20\log_{10}|S_{11}| =$ **`{{res:sc32_05_complex_numbers_phasors_seq_16:value}}`** $\text{dB}$. To match a $Z_L = 100\,\Omega$ antenna to a $Z_0 = 50\,\Omega$ line using a quarter-wave section of characteristic impedance $Z_{\text{line}} = \sqrt{50 \times 100} \approx 70.7107\,\Omega$, keying `{{res:sc32_05_complex_numbers_phasors_seq_17:keys}}` verifies $Z_{\text{in}} = Z_{\text{line}}^2 / Z_L = \mathbf{50.0000\,\Omega}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `70.7107` | $0.0000$ | $0.0000$ | $0.0000$ | $70.7107$ | Enter quarter-wave section impedance $Z_{\text{line}}$ |
| `{{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $5000.0031$ | Square section impedance $Z_{\text{line}}^2$ |
| `100 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$50.0000$** | Divide by load resistance $Z_L$; matched $Z_{\text{in}} = 50.0\,\Omega$ |

And for a lossy coaxial line with series impedance $Z' = 0.1 + 2.5i\,\Omega/\text{m}$ and shunt admittance $Y' = 10^{-6} + 10^{-3}i\,\text{S/m}$, dividing via `{{key:CMPLX}} {{key:÷}}` and taking the complex square root via `{{key:CMPLX}} {{key:√x}}` evaluates $Z_0 = \sqrt{Z'/Y'} = \mathbf{50.0095 - 0.9748i\,\Omega}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0.1 {{key:ENTER}} 2.5 {{key:ENTER}}` | $0.0000$ | $0.1000$ | $2.5000$ | $2.5000$ | Load series impedance $Z' = 0.1 + 2.5i$ |
| `1 {{key:E}} 6 {{key:+/-}} {{key:ENTER}} 1 {{key:E}} 3 {{key:+/-}}` | $0.1000$ | $2.5000$ | $1.0000 \times 10^{-6}$ | $1.0000 \times 10^{-3}$ | Load shunt admittance $Y'$ into $(Y, X)$ |
| `{{key:CMPLX}} {{key:÷}}` | $0.1000$ | $0.1000$ | $2499.9975$ | $-97.4999$ | Complex impedance ratio $Z'/Y'$ |
| `{{key:CMPLX}} {{key:√x}}` | $0.1000$ | $0.1000$ | **$50.0095$** | **$-0.9748$** | Characteristic impedance $Z_0 = \sqrt{Z'/Y'}$ |

*(Note: Attempting complex division or `{{key:CMPLX}} {{key:1/x}}` or `{{key:CMPLX}} {{key:LN}}` at the origin $0 + 0i$ halts non-destructively with `DIVIDE BY 0` [Code 01], while unsupported combinations such as `{{key:CMPLX}} {{key:ASIN}}` display `INVALID DATA` [Code 02] until cleared with `{{key:C}}`.)*

---

### Stepping Off the Flat Plane into Three-Dimensional Space

By recognizing $\sqrt{-1}$ as a physical $90^\circ$ rotation, we watched two seemingly separate worlds—exponential growth ($e^x$ from Chapter 3) and circular trigonometry ($\cos\theta + i\sin\theta$ from Chapter 4)—fuse into a single spiral on the flat two-dimensional plane. What began in 1572 as Rafael Bombelli's daring algebra trick to rescue Gerolamo Cardano's cubic formula matured in the hands of John Wallis, Caspar Wessel, Jean-Robert Argand, Carl Friedrich Gauss, and Leonhard Euler into the natural language of waves, oscillations, and alternating-current power grids. Instead of wrestling with pages of trigonometric sum-and-difference identities, Charles Proteus Steinmetz showed that pairing two stack registers as a complex phasor $(Y = \text{Real},\; X = \text{Imaginary})$ turns inductors ($+i\omega L$) and capacitors ($-i/\omega C$) into ordinary resistors that obey Ohm's law and the universal harmonic operator (`{{key:x∥y}}`).

Whenever you work in `{{key:CMPLX}}` mode on the SC-32, keep one unifying geometric picture in mind: **addition and subtraction slide vectors head-to-tail in rectangular coordinates $(x, y)$, while multiplication, division, powers, and roots scale magnitudes and add or divide angles in polar coordinates $(r\angle\theta)$**. Because the four-register stack holds two complete complex numbers simultaneously—$z_2 = T + Zi$ upstairs and $z_1 = Y + Xi$ downstairs—you can step seamlessly between rectangular component sums and polar phase rotations without ever writing down an intermediate coordinate.

Yet we do not live on a flat sheet of paper. Having mastered points, vectors, and rotations on a flat 2D plane, what changes when we step out of the flat page into **three-dimensional solid space**—where doubling the linear dimensions of a creature, a bridge, or a spacecraft multiplies its cross-sectional strength and surface area by four ($2^2$), but multiplies its volume and weight by eight ($2^3$)? In **[Chapter 6: Why Giants Can't Have Ant Legs: Scaling Laws, Solid Geometry & 3D Space](06-geometry-surface-area.md)**, we meet Galileo Galilei's Square-Cube Law, Archimedes' proudest discovery on his Syracuse tombstone, Bonaventura Cavalieri's coin-stack slicing principle, and the art of auditing complex 3D solids and rotational moments of inertia one face at a time.
