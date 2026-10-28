---
title: "Chapter 7: The Scandal of the Cubic & The Art of Hunting Roots | Thinking in the Stack (SC-32)"
description: "From al-Khwarizmi's squares and the 1535 Milan cubic duel to Horner's nested evaluation and Richard Brent's hybrid root solver on the StackCalc SC-32."
---

# Chapter 7: The Scandal of the Cubic & The Art of Hunting Roots

## From Al-Khwarizmi's Squares to the 1535 Duel in Milan

Around the year 820 CE, in the House of Wisdom (*Bayt al-Hikma*) in Baghdad, the Persian mathematician and astronomer **Muhammad ibn Musa al-Khwarizmi** wrote a landmark treatise whose title—*Al-Kitāb al-mukhtaṣar fī ḥisāb al-jabr wa'l-muqābala* (*The Compendious Book on Calculation by Completion and Balancing*)—gave every language on Earth the word **algebra** (from *al-jabr*, restoring a broken or subtracted term to the other side of an equation), while his own name, Latinized as *Algoritmi*, gave us the word **algorithm**.

When al-Khwarizmi set out to solve a quadratic equation such as his famous benchmark:

$$x^2 + 10x = 39$$

he did not reach for modern algebraic symbols, because plus signs, minus signs, and exponents would not be invented for another seven hundred years. Even more remarkably, al-Khwarizmi did not view $x^2$ as a number multiplied by itself—he viewed $x^2$ literally as a **physical square** of side $x$, and $10x$ as the area of a rectangle.

How do you find the side $x$ of a square when its area $x^2$ plus $10x$ equals $39$? Follow al-Khwarizmi's geometric recipe:
1. Start with a square of side $x$ and area $x^2$.
2. Split the linear term $10x$ in half into two equal rectangles of width $5$ and length $x$ (each having area $5x$), and attach them to two adjacent edges of the $x \times x$ square.
3. Examine the L-shaped figure (a *gnomon*) you have just built. It is *almost* a larger square of side $(x + 5)$—except that the upper-right corner where the two $5 \times x$ wings meet is missing a little **$5 \times 5$ corner square** of area $25$.
4. Drop a $5 \times 5 = 25$ square into that empty corner to **complete the square**. Because you added $25$ to the geometric figure on the left, add $25$ to the $39$ on the right:

$$(x + 5)^2 = 39 + 25 = 64 = 8^2 \implies x + 5 = 8 \implies \mathbf{x = 3}$$

{{blocks:algebra_factoring_area|Al-Khwarizmi's geometric completion of the square and rectangular factorization of quadratic polynomials.}}

Apply that exact same geometric completion to the general quadratic equation $a x^2 + b x + c = 0$—dividing by $a$, splitting the middle term $(b/a)x$ into two wings of width $\frac{b}{2a}$, and filling the missing corner with $\left(\frac{b}{2a}\right)^2$—and out pops the universal **quadratic formula**:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

### William Kahan's Warning: When the Quadratic Formula Loses Its Mind

Before we leave quadratic equations, modern floating-point computing adds a fascinating plot twist to al-Khwarizmi's formula. As Berkeley numerical analyst **William Kahan** famously demonstrated, the textbook formula $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ contains a hidden numerical trap whenever $b^2$ is much larger than $4ac$ ($b^2 \gg |4ac|$).

Suppose $b > 0$ and $4ac$ is tiny compared to $b^2$. Then $\sqrt{b^2 - 4ac}$ is almost identical to $b$. When you evaluate the root with the plus sign ($-b + \sqrt{b^2 - 4ac}$), you are subtracting two nearly equal numbers—wiping out up to half or more of your calculator's significant digits in a single stroke of **catastrophic cancellation**! How do numerical analysts defeat this trap? You *never* subtract $\sqrt{b^2 - 4ac}$ from a number of the same sign. Instead, you always choose the sign that **adds** the magnitudes together to compute the larger root $x_1$ at full precision, and then find the smaller root $x_2$ by using François Viète's exact root-product identity $x_1 x_2 = \frac{c}{a}$:

$$x_1 = \frac{-b - \operatorname{sgn}(b)\sqrt{b^2 - 4ac}}{2a}, \qquad x_2 = \frac{c}{a \, x_1}$$

Quadratic equations govern two classic inverse problems in mechanics and forensic engineering:
* **The Inverse Ballistic Trajectory Quadratic (Solving Backwards for Launch Angle):** In Chapter 4, we projected where a shell lands when its launch angle $\theta$ is already known. What if we face the *inverse* question: the target coordinates $(x, y)$ are fixed on an elevated ridge at known muzzle speed $v_0$, and we must solve backwards for the required launch angle $\theta$? Substituting the trigonometric identity $\sec^2\theta = 1 + \tan^2\theta$ into Galileo's parabolic trajectory $y = x\tan\theta - \frac{gx^2}{2v_0^2}\sec^2\theta$ turns the unknown launch slope $u = \tan\theta$ into a quadratic equation:
  $$\left(\frac{gx^2}{2v_0^2}\right) u^2 - x u + \left(y + \frac{gx^2}{2v_0^2}\right) = 0$$
  Whenever the target lies within the gun's reach, its two positive roots give the gunner two completely different ways to hit the exact same spot: a flat, fast **low direct-fire trajectory** ($\theta_1 = \arctan u_1$) and a high, arcing **plunging mortar trajectory** ($\theta_2 = \arctan u_2$) that drops down from above.
* **Highway Braking & Reaction Stopping Distance ($d = v_0 t_r + \frac{v_0^2}{2\mu g}$):** When a driver spots a hazard on the highway, the car travels at its initial speed $v_0$ during the human perception-reaction time $t_r$ ($d_{\text{react}} = v_0 t_r$) before the brakes lock and tire-pavement friction $\mu$ decelerates the car to a halt over a kinetic-energy braking distance $d_{\text{brake}} = \frac{v_0^2}{2\mu g}$. When crash investigators measure the total stopping distance $d$ at the scene, reconstructing the car's unknown initial speed $v_0$ requires extracting the positive root of the monic quadratic:
  $$v_0^2 + (2\mu g t_r)\, v_0 - 2\mu g d = 0$$

### The 1535 Milan Duel, Cardano's Oath & the Ghost of Casus Irreducibilis

For seven centuries after al-Khwarizmi, the **cubic equation** ($A x^3 + B x^2 + C x + D = 0$) stood as an impenetrable wall. In 1494, the Franciscan friar Luca Pacioli (Leonardo da Vinci's mathematics collaborator) declared in his *Summa de arithmetica* that solving the general cubic was as impossible with current mathematics as squaring the circle.

Pacioli was wrong. Around 1515, a quiet professor at the University of Bologna named **Scipione del Ferro** discovered how to solve the "depressed" cubic $t^3 + pt = q$ (a cubic with no $t^2$ term). In Renaissance Italy, however, university chairs were not protected by lifelong tenure; a mathematician could be publicly challenged to a high-stakes problem-solving duel, with the loser forfeiting his salary, his reputation, and his professorship. So del Ferro kept his formula a closely guarded trade secret until his deathbed in 1526, when he whispered it to his mediocre student **Antonio Maria Fior**.

Armed with his dead master's secret, Fior began boasting that he alone could solve cubic equations, and in early **1535** he challenged **Niccolò Fontana**—a self-taught mathematical prodigy from Brescia known as **Tartaglia** ("The Stammerer," after a French soldier's saber sliced his jaw and palate during the 1512 sack of Brescia, leaving him with a lifelong speech impediment). Each contestant deposited thirty cubic problems with a notary in Milan and was given fifty days to solve the rival's list.

Fior had set all thirty of his problems as variations of del Ferro's single form $t^3 + pt = q$. Tartaglia, on the other hand, had posed several different families of cubics, including $t^3 + pt^2 = q$. For six weeks Tartaglia struggled in agony until, on the night of **February 12, 1535**—just eight days before the deadline—inspiration struck. By imagining a physical three-dimensional cube of side $(u - v)$ sliced into smaller blocks:

$$(u - v)^3 + 3uv(u - v) = u^3 - v^3$$

Tartaglia saw that if you set $t = u - v$, $3uv = p$, and $u^3 - v^3 = -q$, the cubic $t^3 + pt + q = 0$ collapses into a simple **quadratic equation in $u^3$**! Within two hours Tartaglia solved all thirty of Fior's problems, while Fior failed to solve a single one of Tartaglia's.

News of Tartaglia's triumph electrified the polymath physician, gambler, and algebraist **Gerolamo Cardano** in Milan. In March 1539, Cardano invited Tartaglia to his house and begged for the formula, swearing a solemn oath on the Holy Gospels (and on his honor as a gentleman) never to publish Tartaglia's secret. Tartaglia relented, encoding his rule in a cryptic twenty-five-line Italian poem (*"Quando che'l cubo con le cose appresso..."*).

Combining Tartaglia's poem with his own discovery that *any* full cubic $A x^3 + B x^2 + C x + D = 0$ can be stripped of its quadratic $x^2$ term by sliding the coordinate origin to the curve's point of inflection via $x = t - \frac{B}{3A}$:

$$t^3 + p t + q = 0, \qquad p = \frac{3AC - B^2}{3A^2}, \qquad q = \frac{27A^2D - 9ABC + 2B^3}{27A^3}$$

Cardano—together with his brilliant teenaged servant and pupil **Lodovico Ferrari**, who soon discovered how to solve the fourth-degree **quartic equation** by reducing it to a resolvent cubic—had the complete analytical solution to every polynomial up to degree four. In 1543, Cardano traveled to Bologna, inspected Scipione del Ferro's posthumous papers, and realized that del Ferro had discovered the formula twenty years *before* Tartaglia. Free from his oath (at least in his own mind), Cardano published the complete cubic and quartic solutions in his 1545 masterpiece ***Ars Magna*** (*The Great Art*) {{cite:cardano1545}}, giving credit to both del Ferro and a furious Tartaglia.

Yet inside Cardano's cubic formula lurked a mathematical ghost that gave birth to complex numbers (as we saw in Chapter 5). In Cardano's formula:

$$t = \sqrt[3]{-\frac{q}{2} + \sqrt{\Delta}} + \sqrt[3]{-\frac{q}{2} - \sqrt{\Delta}}, \qquad \text{where } \Delta = \left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3$$

the **cubic discriminant** $\Delta$ governs the nature of the three roots:
* **$\Delta > 0$:** The S-shaped cubic crosses the horizontal axis only once, having **one real root** and **two complex conjugate roots** (formed by rotating $u = \sqrt[3]{-q/2 + \sqrt{\Delta}}$ and $v = \sqrt[3]{-q/2 - \sqrt{\Delta}}$ by the cube roots of unity $\omega = -\frac{1}{2} + i\frac{\sqrt{3}}{2}$ and $\omega^2$).
* **$\Delta = 0$:** The cubic just kisses the horizontal axis tangentially, producing **three real roots with at least one repeated root** (such as the critically damped RLC filter polynomial $s^3 + 12s^2 + 45s + 50 = (s+2)(s+5)^2 = 0$, with a double pole at $s = -5$).
* **$\Delta < 0$ (*Casus Irreducibilis*):** Here was the scandal! Whenever a cubic wiggles across the horizontal axis three times to produce **three distinct real roots** (such as $(x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x - 6 = 0$), the discriminant $\Delta$ under the square root is **strictly negative**. To extract three completely real numbers from Cardano's formula, you are *forced* to walk through the complex plane, taking the cube root of a complex number $r e^{i\theta}$ by De Moivre's angle trisection $r^{1/3}[\cos(\theta/3) + i\sin(\theta/3)]$, where the imaginary parts of the two conjugate cube roots cancel out to zero.

### Viète's Trigonometric Escape, Ferrari's Quartic & the Root-Coefficient Checksums

How did sixteenth-century algebraists verify their roots and bypass the complex radicals of *casus irreducibilis* before complex exponential notation existed, and how does the SC-32 model this entire analytical toolkit?

On the SC-32, pressing **`{{key:POLY}}`** (`{{key:↱}}` + `{{key:XEQ}}`) opens the dedicated analytical polynomial workspace for $Ax^3 + Bx^2 + Cx + D = 0$, mapping the six LFU softkeys to `{{key:A}}`, `{{key:B}}`, `{{key:C}}`, `{{key:D}}`, `{{key:EXEC}}`, and `{{key:CLR}}`. You simply key each coefficient onto the stack and tap its softkey (setting `0 {{key:D}}` to solve a quadratic $Ax^2 + Bx + C = 0$), and when you press `{{key:EXEC}}`, the calculator evaluates the discriminant $\Delta$, places the primary root $r_1$ directly onto the stack in Gaussian complex format ($Y = \text{Real},\; X = \text{Imag}$), and writes all three real or complex roots into numbered variable registers `1` through `6` (`{{key:RCL}} 1` through `{{key:RCL}} 6`).

Behind that single `{{key:EXEC}}` keystroke stand three classical pillars of polynomial theory:

1. **François Viète's Cosine Trisection of the Cubic (1591):** The French cryptographer and algebraist **François Viète** noticed a striking resemblance between the depressed cubic $t^3 + pt + q = 0$ (when $\Delta < 0$, so $p < 0$) and the trigonometric triple-angle identity for cosine:
   $$\cos(3\theta) = 4\cos^3\theta - 3\cos\theta \implies \cos^3\theta - \frac{3}{4}\cos\theta - \frac{1}{4}\cos(3\theta) = 0$$
   By scaling the unknown $t = 2\sqrt{-p/3}\,\cos\theta$, Viète matched the depressed cubic term-for-term against the triple-angle cosine identity, expressing all three real roots directly without a single complex square root:
   $$t_k = 2\sqrt{-\frac{p}{3}} \cos\left(\frac{1}{3}\arccos\left(\frac{3q}{2p}\sqrt{-\frac{3}{p}}\right) - \frac{2\pi k}{3}\right), \qquad k = 0, 1, 2$$
   Geometrically, solving a three-real-root cubic is identical to **trisecting an angle on the unit circle** and projecting the three $120^\circ$-spaced corners of an inscribed equilateral triangle down onto the horizontal real axis.
2. **Lodovico Ferrari's Reduction of the Quartic to a Resolvent Cubic (1540):** Right after Cardano mastered the cubic in 1539, a rival mathematician named Zuanne da Coi challenged Cardano and Tartaglia with a fourth-degree **quartic equation**: $x^4 + 6x^2 + 36 = 60x$. Neither Cardano nor Tartaglia could solve it—until Cardano's eighteen-year-old protégé **Lodovico Ferrari** spotted a two-stage algebraic lockpick.
   After shifting $x$ to remove the $x^3$ term ($x^4 + px^2 + qx + r = 0$), Ferrari moved $px^2 + qx + r$ to the right side, completed the square on the left as $(x^2 + \frac{p}{2})^2$, and introduced an **auxiliary variable $y$** inside the square:
   $$\left(x^2 + \frac{p}{2} + y\right)^2 = (p + 2y)x^2 - qx + \left(\frac{p^2}{4} - r + py + y^2\right)$$
   Notice the right-hand side: it is a simple **quadratic in $x$**. When is a quadratic in $x$ a perfect square $(mx + n)^2$ so that we can take the square root of both sides of the equation? Precisely when its quadratic discriminant $B^2 - 4AC$ equals zero:
   $$q^2 - 4(p + 2y)\left(y^2 + py + \frac{p^2}{4} - r\right) = 0$$
   And what degree is that equation for the helper variable $y$? It is a **third-degree cubic equation**—the **resolvent cubic**—which Cardano's `{{key:POLY}}` solver can already solve. Once one root $y_1$ of the resolvent cubic is found, the quartic splits into two ordinary quadratic equations, giving all four roots.
3. **Viète's Root-Coefficient Checksums (Viète's Formulas):** Whenever `{{key:POLY}}` writes the roots of a cubic ($A x^3 + B x^2 + C x + D = 0$) into variables `1` through `6`, how can you verify in two seconds that your roots are $100\%$ accurate without plugging each root back into the polynomial? Multiply out $A(x - r_1)(x - r_2)(x - r_3) = A x^3 - A(r_1 + r_2 + r_3)x^2 + A(r_1 r_2 + r_2 r_3 + r_3 r_1)x - A r_1 r_2 r_3$ and compare coefficients term by term:
   $$\begin{aligned}
   \text{Sum of Roots (Trace):} &\quad r_1 + r_2 + r_3 = -\frac{B}{A} \\
   \text{Pairwise Products:} &\quad r_1 r_2 + r_2 r_3 + r_3 r_1 = +\frac{C}{A} \\
   \text{Product of Roots (Determinant):} &\quad r_1 \cdot r_2 \cdot r_3 = -\frac{D}{A}
   \end{aligned}$$
   For our benchmark cubic $x^3 - 6x^2 + 11x - 6 = 0$ with roots $1, 2, 3$, recalling and summing `{{key:RCL}} 1 {{key:RCL}} 3 {{key:+}} {{key:RCL}} 5 {{key:+}}` gives $1 + 2 + 3 = 6 = -(-6)/1$, their pairwise product sum is $1(2) + 2(3) + 3(1) = 11 = +11/1$, and their product `{{key:RCL}} 1 {{key:RCL}} 3 {{key:×}} {{key:RCL}} 5 {{key:×}}` is $1 \times 2 \times 3 = 6 = -(-6)/1$. In any **depressed cubic** $t^3 + pt + q = 0$ (where the quadratic coefficient $B = 0$), **the three roots always sum identically to zero** ($t_1 + t_2 + t_3 = 0$), because the coordinate shift $x = t - \frac{B}{3A}$ placed the origin right at the arithmetic average (centroid) of the three roots.

And why did the chain of radical reductions stop forever after Ferrari's degree-4 quartic? For nearly three hundred years after *Ars Magna*, the greatest minds in Europe—including Ehrenfried Walther von Tschirnhaus, Leonhard Euler, and Joseph-Louis Lagrange—hunted for a degree-5 quintic formula ($Ax^5 + Bx^4 + Cx^3 + Dx^2 + Ex + F = 0$). Lagrange noticed a troubling pattern: for a degree-2 quadratic, the resolvent has degree 1; for a degree-3 cubic, Tartaglia's resolvent has degree 2; for a degree-4 quartic, Ferrari's resolvent has degree 3. Each time, the helper equation had *lower* degree than the original problem. Yet when Lagrange applied the same permutation method to a degree-5 quintic, the resolvent equation jumped *up* to degree 6 (with $5!/2 = 60$ alternating permutations).

In **1824**, the twenty-one-year-old Norwegian mathematician **Niels Henrik Abel** proved (building on Paolo Ruffini's 1799 work) that this barrier is absolute—and on the night of May 29, 1832, the twenty-year-old French revolutionary **Évariste Galois** scribbled a frantic letter by candlelight the night before he was fatally shot in a pistol duel at dawn, founding **Group Theory** and proving why: for $n = 2, 3, 4$, the permutation group $S_n$ of the roots breaks down into commutative cyclic pieces ("solvable groups") that correspond to extracting $k$-th roots $\sqrt[k]{\phantom{x}}$. For $n \ge 5$, the alternating group $A_5$ (the $60$ rotational symmetries of a regular icosahedron) is a **simple non-abelian group** that cannot be factored into cyclic steps. **No general radical formula in $+, -, \times, \div$, and $\sqrt[n]{\phantom{x}}$ can ever exist for degree 5 or higher!**

---

## Unpeeling Polynomials from the Inside Out: Horner's Scheme

Even before we try to *solve* a polynomial $P(x) = 0$, how should we *evaluate* a polynomial at a given number $x$?

Suppose you want to evaluate the fourth-degree polynomial:

$$P(x) = 4x^4 - 3x^3 + 2x^2 - 5x + 7 \qquad \text{at } x = 2.5$$

If you evaluate $P(x)$ the way it is written on the page—computing $x^4$, multiplying by $4$, computing $x^3$, multiplying by $3$, computing $x^2$, and so on—you have to compute powers of $x$ over and over again ($4 + 3 + 2 + 1 = 10$ multiplications, or three separate exponentiations). Worse yet, near a root where large positive and negative power terms nearly cancel out, computing $a_n x^n$ separately magnifies floating-point rounding error.

In 1819, the English schoolmaster **William George Horner** (rediscovering a method known to Isaac Newton in 1669 and the 13th-century Chinese algebraist **Qin Jiushao** in his 1247 *Mathematical Treatise in Nine Sections*) noticed what happens when you factor $x$ out from the inside out:

$$P(x) = 4x^4 - 3x^3 + 2x^2 - 5x + 7 = (((4x - 3)x + 2)x - 5)x + 7$$

In **Horner's nested scheme**, every single exponent has vanished. To evaluate any degree-$n$ polynomial at $x$, you start with the leading coefficient $a_n$ and simply repeat a two-beat heartbeat $n$ times:

$$\textbf{Multiply by } x \text{ (`{{key:×}}`),} \quad \textbf{Add the next coefficient (`{{key:+}}` or `{{key:-}}`).}$$

Let us trace that heartbeat mentally on $P(2.5) = (((4(2.5) - 3)(2.5) + 2)(2.5) - 5)(2.5) + 7$:
* Start with $4$, multiply by $2.5$ ($\to 10$), subtract $3$ ($\to \mathbf{7.0}$).
* Multiply by $2.5$ ($\to 17.5$), add $2$ ($\to \mathbf{19.5}$).
* Multiply by $2.5$ ($\to 48.75$), subtract $5$ ($\to \mathbf{43.75}$).
* Multiply by $2.5$ ($\to 109.375$), add $7$ ($\to \mathbf{116.3750}$).

Four multiplications, four additions, zero powers, and zero temporary variables. On the SC-32, you can make Horner's scheme even faster by **flooding all four stack registers with $x$** at the very start via **`x {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}`**. Because the top shelf **Register $T$ replicates its value downward into Register $Z$** every time the stack drops, a fresh copy of $x$ is waiting in Register $Y$ whenever you finish adding a coefficient—turning the four-register stack into an automatic Horner conveyor belt where you never have to re-type $x$!

Better still, the intermediate numbers produced at each beat of Horner's scheme ($4,\; 7.0,\; 19.5,\; 43.75$) are not random scratchpad numbers—they are the exact coefficients of the quotient polynomial $Q(x)$ obtained by **Ruffini-Horner synthetic division** when dividing $P(x)$ by $(x - x_0)$ at $x_0 = 2.5$:

$$P(x) = (x - x_0)\,Q(x) + R = (x - 2.5)\left(4x^3 + 7x^2 + 19.5x + 43.75\right) + 116.3750$$

This Polynomial Remainder Theorem identity $P(x) = (x - x_0)Q(x) + P(x_0)$ gives us three computational superpowers:
* **Polynomial Deflation:** Once you find one exact root $r_1$ of a polynomial (where the remainder $P(r_1) = 0$), the intermediate numbers generated during Horner's evaluation at $r_1$ immediately hand you the deflated degree-$(n-1)$ quotient polynomial $Q(x) = P(x)/(x - r_1)$—allowing you to drop a fourth-degree quartic down to a cubic, or a cubic down to a quadratic.
* **Simultaneous Derivative Evaluation ($P'(x_0) = Q(x_0)$):** Differentiate $P(x) = (x - x_0)Q(x) + P(x_0)$ with respect to $x$ by the product rule:
   $$P'(x) = Q(x) + (x - x_0)Q'(x) \implies P'(x_0) = Q(x_0)$$
   Evaluating the quotient polynomial $Q(x)$ at $x_0$ by running a second Horner pass on the intermediate coefficients gives the exact **calculus derivative $P'(x_0)$** without ever writing down a symbolic derivative formula.
* **Suppression of Catastrophic Cancellation Near Multiple Roots:** In numerical thermodynamics and flight-control engineering—such as evaluating standard-atmosphere pressure-altitude curves $P(h) = a_3 h^3 + a_2 h^2 + a_1 h + a_0$, NASA Glenn molar heat-capacity polynomials $C_p(T)/R = a_0 + a_1 T + a_2 T^2 + a_3 T^3 + a_4 T^4$, or our critically damped RLC filter polynomial near its repeated root $s = -5$—nested Horner evaluation updates the running factor $(s + 5)$ locally at each step rather than subtracting huge, independently rounded powers $s^3$ and $12s^2$.

That same nested-factoring mindset simplifies rational formulas and symmetric high-degree equations across physics:
* **Martin Green's Solar-Cell Fill Factor (1982):** In a silicon photovoltaic cell, the maximum power point satisfies a transcendental diode equation that cannot be inverted in closed form, but Australian solar physicist Martin Green discovered an accurate rational-logarithmic expression in the normalized open-circuit voltage $v_{\text{oc}} = V_{\text{oc}} / V_T$ (evaluated in one pass on the stack by flooding $v_{\text{oc}}$ across all four registers with `{{key:ENTER}} {{key:ENTER}} {{key:ENTER}}`):
  $$\text{Fill Factor } FF = \frac{v_{\text{oc}} - \ln(v_{\text{oc}} + 0.72)}{v_{\text{oc}} + 1}$$
* **Coupled-Oscillator Biquadratic Polynomials:** When two coupled undamped spring-mass pendulums vibrate in their natural normal modes, the eigenvalue equation $\det(\mathbf{K} - \omega^2\mathbf{M}) = 0$ contains only even powers of frequency ($a x^4 + b x^2 + c = 0$), which collapses into a quadratic in $u = x^2$ whose positive square roots $\omega = \sqrt{u}$ give the two normal-mode frequencies.

---

## Why Newton's Method Flies Off Cliffs—And How Richard Brent Tamed It

Abel and Galois proved that we cannot even solve $x^5 - x - 1 = 0$ with a radical formula. And across real-world science and engineering, nature rarely hands us pure polynomials anyway. Physical conservation laws constantly mix algebraic powers $x$ with sines, cosines, exponentials, and logarithms—producing **transcendental equations** where no symbolic manipulation can ever isolate the unknown on one side of the equals sign.

How do you hunt down a root $x^*$ where $f(x^*) = 0$ when algebra cannot isolate $x$? Over three centuries, numerical analysts developed two rival philosophies—one slow and invincible, the other blazingly fast and reckless:

1. **The Tortoise: Bolzano's Intermediate Value Theorem & Bisection ($p = 1.000$):** Suppose a continuous curve $f(x)$ is negative at $x = a$ ($f(a) < 0$, below the axis) and positive at $x = b$ ($f(b) > 0$, above the axis), so that $f(a)\cdot f(b) < 0$. By Bernard Bolzano's **Intermediate Value Theorem** (1817), a continuous curve cannot get from below the horizontal axis to above it without crossing $y = 0$ at least once inside the **bracket** $[a, b]$.
   In the **Bisection Method**, you evaluate the function at the midpoint $m = \frac{1}{2}(a + b)$, check its sign, and throw away whichever half of the interval does not contain the sign change. Every step cuts the uncertainty in half—gaining $1\text{ binary bit}$ of precision per step (linear convergence, order $p = 1.000$). After $40$ bisections, your bracket has shrunk by $2^{-40} \approx 10^{-12}$. Bisection can *never* fail on a bracketed root, but taking $40$ to $50$ function evaluations is a slow trudge.
2. **The Hare: Newton-Raphson ($p = 2.000$) & the Secant Chord ($p \approx 1.618$):** In 1669, **Isaac Newton** (testing John Wallis's cubic benchmark $x^3 - 2x - 5 = 0$ near $x_0 = 2$) and **Joseph Raphson** (1690) proposed sliding down the local tangent line of the curve:
   $$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$
   Near a clean simple root, Newton's method is **quadratically convergent** ($p = 2.000$), **doubling the number of accurate decimal digits on every single step** ($1 \to 2 \to 4 \to 8 \to 16\text{ digits}$). And if you don't want to work out the calculus derivative $f'(x)$ by hand, replacing the tangent slope with the **Secant Chord** through the last two points gives superlinear convergence at the **golden-ratio power** $p = \phi = \frac{1+\sqrt{5}}{2} \approx 1.618$.
   So what is the catch? Look at the denominator $f'(x_n)$ in Newton's formula (or $f(x_n) - f(x_{n-1})$ in the secant formula). If your search ever wanders near a peak, a valley, an inflection plateau, or a horizontal asymptote where the slope flattens out ($f'(x_n) \approx 0$), **the nearly horizontal tangent line shoots off to the horizon, catapulting $x_{n+1}$ miles away from the root or into an infinite loop!**

### Richard Brent's 1973 Masterpiece: Algorithmic Paranoia

In 1973, building on earlier work by Theodorus Dekker, the Australian mathematician **Richard P. Brent** asked a brilliant question in *Algorithms for Minimization Without Derivatives* {{cite:brent1973}}: *Can we combine the invincible safety net of Bisection with the superlinear sprint of Interpolation so that the solver runs at top speed on smooth curves, never requires a derivative, and is mathematically guaranteed never to fly off a cliff?*

Brent's hybrid root-finding algorithm—the engine behind the SC-32's **`{{key:SOLVE}}`** key (`{{key:↱}}` + `{{key:7}}`, paired with the **`{{key:EQN}}`** equation editor)—achieves this through two mechanisms:
* **Sideways Parabolic Fitting (Inverse Quadratic Interpolation, $p \approx 1.839$):** Suppose you have three points $(a, f(a))$, $(b, f(b))$, and $(c, f(c))$ near the root. If you fit an ordinary upright parabola $y = P(x)$ through three points, that parabola might turn around before reaching the $x$-axis and have *no real roots at all*. Brent instead turns his head sideways and fits $x$ as a **Lagrange quadratic polynomial of $y$** ($x = P(y)$) through $(f(a), a)$, $(f(b), b)$, and $(f(c), c)$, and then simply plugs in $y = 0$:
  $$x_{\text{IQI}} = \frac{a f(b) f(c)}{(f(a)-f(b))(f(a)-f(c))} + \frac{b f(a) f(c)}{(f(b)-f(a))(f(b)-f(c))} + \frac{c f(a) f(b)}{(f(c)-f(a))(f(c)-f(b))}$$
  Evaluating a sideways parabola at $y = 0$ is guaranteed to yield a single unique real number $x_{\text{IQI}}$, converging at order $p \approx 1.839$ (nearly doubling the correct digits on every step).
* **The Five Watchdog Tests:** Brent never trusts an interpolated step blindly. At every single iteration, the algorithm keeps the root locked inside a shrinking sign-change cage $[a, b]$ where $f(a)f(b) \le 0$. Whenever Secant or Inverse Quadratic Interpolation proposes a leap $s$, **five watchdog conditions** inspect it: does $s$ land strictly inside the interior three-quarter window $\left(\frac{3a+b}{4}, b\right)$? And is the step contracting the bracket at least twice as fast as the previous steps? The instant an interpolated step tries to jump outside the cage or stalls on a flat plateau, **Brent's watchdog vetoes the interpolation and forces a guaranteed Bisection step $m = \frac{1}{2}(a + b)$!**

| Root-Finding Algorithm | Convergence Order ($p$) | Requires Derivative $f'(x)$? | Guaranteed to Stay in Bracket? | Behavior Near Flat Slopes ($f'(x) \approx 0$) |
| :--- | :---: | :---: | :---: | :--- |
| **Bisection** | $1.000$ | No | Yes (Guaranteed) | Steady ($1\text{ bit/step}$), immune to slope traps |
| **Newton-Raphson** | $2.000$ | Yes | No | Catastrophic divergence when $f'(x) \approx 0$ |
| **Secant Chord** | $1.618$ ($\phi$) | No | No | Can fling iterates far outside the search region |
| **Brent's Hybrid Method** | $1.839$ | No | **Yes (Guaranteed)** | **Instant bisection fallback; zero divergence** |

### Five Real-World Mysteries Where the Unknown Hides Inside the Equation

Once you have both Cardano's `{{key:POLY}}` workspace and Brent's `{{key:SOLVE}}` root hunter in your toolkit, equations across astronomy, fluid mechanics, thermodynamics, and solid mechanics unlock immediately:

1. **Johannes Kepler's Transcendental Equation of Planetary Orbits (1609):** When a planet or satellite travels along an elliptical orbit of eccentricity $e$, **Kepler's Second Law** states that the radius vector from the central body sweeps out equal areas in equal times—the satellite speeds up as it swoops close to periapsis and slows down as it coasts out toward apoapsis. Where along its orbit is the satellite at a given time $t$ after periapsis? In his 1609 *Astronomia Nova*, **Johannes Kepler** showed that the mean time angle $M = \frac{2\pi t}{T}$ (**mean anomaly**) is linked to the geometric position angle $E$ (**eccentric anomaly**) by a deceptively simple equation:
   $$M = E - e \sin E \implies f(E) = E - e\sin E - M = 0$$
   In $E - e\sin E = M$, the angle $E$ sits both *outside* the sine function (as a linear arc) and *inside* the sine function ($\sin E$). Kepler himself lamented in 1609 that no algebraic formula can ever solve this equation for $E$ ("I am sufficiently satisfied that it cannot be solved *a priori*, on account of the different nature of the arc and the sine")—yet entering the residual into `{{key:EQN}}` in `{{key:RAD}}` mode and pressing `{{key:SOLVE}} E` zeroes in on the exact orbital angle in milliseconds.
2. **Cyril Colebrook's Turbulent Pipe Friction Law (1939):** When water or rocket propellant rushes through a commercial steel pipe of diameter $D$ at high Reynolds number $\text{Re}$, what is the Darcy-Weisbach friction factor $f$? Even in violent turbulence, fluid right at the metal wall is brought to a stop by the no-slip condition, creating a microscopic **viscous laminar sublayer** of thickness $\delta_v \propto D / (\text{Re}\sqrt{f})$. When the flow is slow, this smooth viscous cushion buries the rough metal grain peaks ($\varepsilon/D$); as the flow speeds up, the cushion thins until the roughness peaks poke through into the turbulent core and shed eddies. Because the thickness of the shielding cushion itself depends on the friction factor $\sqrt{f}$, **Cyril Colebrook** (1939) {{cite:colebrook1939}} showed that $f$ is trapped on *both* sides of a base-10 logarithm (`{{key:LOG}}`):
   $$\frac{1}{\sqrt{f}} = -2.0 \log_{10} \left( \frac{\varepsilon / D}{3.7} + \frac{2.51}{\text{Re}\sqrt{f}} \right)$$
   Generations of engineers had to squint at logarithmic lines on the **Moody Chart** to estimate $f$; `{{key:SOLVE}}` extracts $f$ directly from Colebrook's implicit law to full precision.
3. **Archimedes' Floating Sphere Equilibrium (Answering Chapter 6's Cliffhanger):** At the end of Chapter 6, we asked how deep ($h$) a solid oak marine buoy sphere of radius $R$ and density $\rho_s$ sinks when floating in water of density $\rho_w$. By **Archimedes' Principle**, the sphere sinks until the volume of its submerged spherical cap $\frac{1}{3}\pi h^2(3R - h)$ equals $\frac{\rho_s}{\rho_w}$ times the total sphere volume $\frac{4}{3}\pi R^3$:
   $$\frac{1}{3}\pi h^2 (3R - h) = \frac{\rho_s}{\rho_w}\left(\frac{4}{3}\pi R^3\right) \implies h^3 - 3R h^2 + 4\left(\frac{\rho_s}{\rho_w}\right)R^3 = 0$$
   Because the polynomial $h^2(3R - h)$ extends mathematically beyond the bottom and top poles of the physical sphere ($0 \le h \le 2R$), this depressed-linear cubic always possesses three real roots (*casus irreducibilis*)—and sorting them in `{{key:POLY}}` isolates the exact physical waterline depth $h$ inside $[0, 2R]$ as the middle root in Variable `3` (`{{key:RCL}} 3`).
4. **Why Twisted Chalk Snaps at a $45^\circ$ Spiral (3D Principal Stress Eigenvalues) & Van der Waals Real Gases:** Take a piece of brittle blackboard chalk between your fingers and twist it in pure torsion. It does not shear off flat at $90^\circ$—it snaps along a clean **$45^\circ$ helical spiral**. Why? Because chalk is weak in tension, and any 3D state of normal and shear stress ($\sigma_{xx}, \sigma_{yy}, \sigma_{zz}, \tau_{xy}, \tau_{yz}, \tau_{xz}$) is secretly equivalent to three pure perpendicular pulls or pushes (**principal stresses** $\sigma_1 \ge \sigma_2 \ge \sigma_3$) along rotated coordinate axes where shear vanishes completely. Setting the determinant $\det(\boldsymbol{\sigma} - \lambda\mathbf{I}) = 0$ produces the **3D stress invariant cubic**:
   $$\lambda^3 - I_1 \lambda^2 + I_2 \lambda - I_3 = 0$$
   whose three real roots in `{{key:POLY}}` deliver the exact principal stresses. Similarly, when a real gas is compressed near its critical point, **Johannes Diderik van der Waals's** equation of state $\left(P + \frac{a}{V^2}\right)(V - b) = RT$ accounts for intermolecular attraction ($a/V^2$) and finite molecular volume ($b$), expanding into the cubic polynomial $PV^3 - (Pb + RT)V^2 + aV - ab = 0$ whose molar volume $V$ can be extracted either analytically via `{{key:POLY}}` or directly in unexpanded form via `{{key:SOLVE}}`.
5. **Diode Load Lines, Open-Channel Critical Depth, Nuclear Criticality & Supersonic Rocket Nozzles:** Whenever a linear circuit, hydraulic channel, or compressible flow crosses a physical threshold, an implicit transcendental or high-degree balance governs the operating point:
   * **William Shockley's Silicon Diode Load Line:** Finding the operating voltage $V$ where a linear series resistor load line $(V_s - V)/R$ intersects the exponential diode current $I_s(e^{V/V_T} - 1)$ requires solving a mixed linear-exponential equation that no logarithm can untangle.
   * **Open-Channel Froude Critical Depth & Nuclear Reactor Buckling:** In civil hydraulics, water pouring over a spillway reaches **critical depth** $y_c$ where flow velocity equals the shallow-water gravity wave speed ($\text{Fr} = \frac{Q}{\sqrt{g A(y)^3 / T(y)}} = 1$), just as a spherical fission reactor core reaches criticality when its radial neutron flux satisfies the buckling eigencondition $\sin(B_g R) = 0$.
   * **Aurel Stodola's De Laval Rocket Nozzle Area-Mach Law:** In compressible gas dynamics, accelerating hot combustion gas through a converging-diverging nozzle links the cross-sectional area ratio $A/A^*$ to the Mach number $M$ via $\frac{A}{A^*} = \frac{1}{M}\left(\frac{2}{\gamma+1}\left[1 + \frac{\gamma-1}{2}M^2\right]\right)^{\frac{\gamma+1}{2(\gamma-1)}}$, whose two roots on either side of the $M = 1$ throat represent the **subsonic diffuser branch** ($M < 1$) and the **supersonic rocket exhaust branch** ($M > 1$).

### A Field Guide to Polynomial & Transcendental Roots Across Science

Beyond our five core case studies, polynomial and implicit equations emerge wherever physical conservation laws balance competing effects. In hydraulics and fluid machinery, when supercritical water rushing down a dam spillway ($\text{Fr}_1 = v_1/\sqrt{gy_1} > 1$) slams into slow downstream river water, it erupts into a standing turbulent shock wave—a **hydraulic jump** whose downstream depth satisfies **Jean-Baptiste Bélanger's 1828 conjugate depth quadratic**:

$$y_2^2 + y_1 y_2 - 2 y_1^2 \text{Fr}_1^2 = 0 \implies y_2 = \frac{y_1}{2}\left(\sqrt{1 + 8\text{Fr}_1^2} - 1\right)$$

In the same way, matching a centrifugal pump's head curve $H_p(Q) = H_0 + b_1 Q - b_2 Q^2$ against a pipeline's frictional head loss $H_{\text{sys}}(Q) = H_{\text{stat}} + k Q^2$ produces the operating-point quadratic $(b_2 + k)Q^2 - b_1 Q - (H_0 - H_{\text{stat}}) = 0$, while terminal settling of a sphere under combined linear Stokes viscous drag and quadratic Newton pressure drag satisfies $c_2 v^2 + c_1 v - W_{\text{buoy}} = 0$.

In thermal physics and acoustics, when Max Planck formulated the quantum law of blackbody radiation in 1900, finding the wavelength $\lambda_{\max}$ where a star's spectrum peaks (**Wien's Displacement Law**) required setting the derivative of $x^5/(e^x - 1)$ to zero—yielding the classic transcendental root equation:

$$5\left(1 - e^{-x}\right) - x = 0 \implies x^* = 4.9651142317$$

Chemical engineers likewise rely on `{{key:SOLVE}}` to extract an unknown outlet temperature difference $\Delta T_2$ from a target **Log Mean Temperature Difference** $\text{LMTD} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)}$ in shell-and-tube heat exchangers, whereas acoustic designers size the throat radius $a$ of a **Helmholtz resonator** of cavity volume $V$ and neck length $L$. Because sound waves radiating from an open neck drag a small plug of outside air back and forth—adding **Lord Rayleigh's radiation end-correction** $L_{\text{eff}} = L + 1.7a$ into the resonance formula $f_0 = \frac{c}{2\pi}\sqrt{\frac{\pi a^2}{V(L + 1.7a)}}$—solving for the required neck radius $a$ reduces to the quadratic $a^2 - \left(\frac{6.8\pi f_0^2 V}{c^2}\right) a - \left(\frac{4\pi f_0^2 V L}{c^2}\right) = 0$.

Across orbital mechanics and structural design, low-degree polynomials govern equilibrium at every scale: finding the **geostationary orbital radius** where a satellite's orbital period matches Earth's sidereal rotation period $T$ is a pure cubic $r^3 - \frac{\mu T^2}{4\pi^2} = 0$; the slow **precession and fast nutation rates** $\Omega$ of a spinning top or spacecraft gyroscope satisfy the quadratic $I_t \Omega^2 - I_p \omega \Omega + M g L = 0$; and **Gabriel Lamé's thick-walled pressure vessel equation** $\sigma_\theta = P_i \frac{R_o^2 + R_i^2}{R_o^2 - R_i^2}$ reduces directly to a quadratic in the wall-thickness ratio $u = R_o/R_i$.

### Inside the Symbolic Equation Bank ({{key:EQN}}): Pure Functions, Step Editing & Iverson Piecewise Logic

Before we hand an implicit equation over to Brent's root hunter, how do we actually enter, inspect, edit, and structure a formula inside the SC-32's **`{{key:EQN}}` workspace** (`{{key:↱}}` + `{{key:STO}}`)—and how can a single RPN equation represent a **piecewise physical law** that changes its mathematical formula across a threshold?

Unlike vintage keystroke-programmable calculators that mixed arithmetic formulas with destructive memory writes and spaghetti-code `GTO` jumps, the SC-32's **24-slot Equation Bank** treats every stored entry (`A` through `Z`, up to $96$ steps per equation) as a **pure, side-effect-free mathematical function**:
* **Creating, Labeling & Navigating Equations (`{{key:EQN}}`, `NEW`, `{{key:LBL}}`, `{{key:↑}}`, `{{key:↓}}`, `{{key:<-}}`):** Pressing `{{key:EQN}}` (`{{key:↱}}` + `{{key:STO}}`) opens the Equation Catalog (`NEW`, `1:A`, `2:B`, … on the top softkeys). Tapping `NEW` (`{{key:LFU0}}`) or pressing `{{key:LBL}}` (`{{key:↰}}` + `{{key:+}}`) prompts **`LBL _`** and automatically arms the `A–Z` Alpha layer so a single tap assigns your equation's letter (`00 LBL A`). As you key in operations, each step is recorded with a line number (`01 RCL X`, `02 x²`, …). When typing a multi-digit constant such as `0.05`, pressing `{{key:ENTER}}` terminates the numeric literal cleanly without inserting an extra stack duplication; pressing `{{key:ENTER}}` a second time inserts an explicit `ENTER` stack-lift step. At any time, `{{key:↑}}` (`{{key:↰}}` + `{{key:8}}`) and `{{key:↓}}` (`{{key:↰}}` + `{{key:7}}`) step the cursor backward and forward through your numbered instructions: typing any key inserts right at the cursor, `{{key:<-}}` deletes the preceding step, and `{{key:RTN}}` (`{{key:↱}}` + `{{key:+}}`), `{{key:EQN}}`, or `{{key:C}}` saves the equation to non-volatile memory.
* **Why `{{key:STO}}` Is Blocked Inside `{{key:EQN}}` (`INVALID FOR EQN`):** Inside an equation, pressing `{{key:RCL}}` followed by a letter (`A`–`Z`, or indirect `(i)`—recall from Chapter 2 that storing a slot number $1\dots 89$ in the index pointer `i` via `{{key:STO}} {{key:.}}` lets `{{key:RCL}} {{key:x∥y}}` dereference `(i)` dynamically) reads that variable onto the stack, and `{{key:RCL}} {{key:+}} A` / `{{key:RCL}} {{key:×}} A` performs in-place recall arithmetic. By contrast, `{{key:STO}}` is intentionally blocked (`INVALID FOR EQN`) so that when `{{key:XEQ}}`, `{{key:FN=}}` (`{{key:↰}}` + `{{key:XEQ}}`), `{{key:SOLVE}}`, `{{key:∫}}`, or `{{key:PLOT}}` evaluates your equation dozens or hundreds of times across an interval, it can never overwrite your stored laboratory constants.
* **Macaulay's Singularity Bracket & Iverson's Indicator Logic (`{{key:x?0}}` and `{{key:x?y}}`):** In 1919, the Cambridge mathematician **William H. Macaulay** solved a headache that had plagued structural engineers since Euler: when a bridge beam carries concentrated point loads or steps in cross-section at stations $a_1, a_2, \dots$, writing a separate differential equation for every span is a nightmare. Macaulay introduced the **singularity ramp bracket** $\langle x - a \rangle_+ = \max(0, x - a)$, which equals $0$ to the left of $x = a$ and turns on smoothly as $(x - a)$ to the right of $x = a$. Four decades later, **Kenneth E. Iverson** (1962) generalized Macaulay's switch into the **Iverson Indicator Bracket $[P] \in \{1, 0\}$**, where any relational proposition $P$ evaluates directly to **`1` if True** and **`0` if False**:
  $$f(x) = f_1(x)\cdot [x \le c] + f_2(x)\cdot [x > c] \qquad \text{or} \qquad \langle u \rangle_+ = u \cdot [u > 0] = \max(0, u)$$
  On the SC-32, when an equation is evaluated, the six unary zero tests in **`{{key:x?0}}`** (`{{key:↱}}` + `{{key:÷}}`: `{{key:x=0}}`, `{{key:x≠0}}`, `{{key:x>0}}`, `{{key:x<0}}`, `{{key:x≥0}}`, `{{key:x≤0}}`) replace Register $X$ in place with `1.0` (True) or `0.0` (False), while the six binary two-register tests in **`{{key:x?y}}`** (`{{key:↰}}` + `{{key:÷}}`: `{{key:x=y}}`, `{{key:x≠y}}`, `{{key:x>y}}`, `{{key:x<y}}`, `{{key:x≥y}}`, `{{key:x≤y}}`) compare Register $X$ against Register $Y$, drop the stack, and place `1.0` or `0.0` in Register $X$. Consequently, on any expression $u$ sitting in Register $X$, the three-keystroke **Macaulay Ramp Idiom** **`{{key:ENTER}} {{key:x>0}} {{key:×}}`** duplicates $u$ into $Y$, converts $X$ into $[u > 0] \in \{0, 1\}$, and multiplies them to produce $\langle u \rangle_+ = \max(0, u)$—allowing you to model bilinear contact springs, progressive tax or tariff brackets, Zener clippers, and piecewise fluid drag laws inside a single continuous `{{key:EQN}}` formula!

### How Brent's Two-Phase Engine and Kahan's Diagnostic Audit Work Together

What happens behind the scenes when you hand an equation $f(x) = 0$ in `{{key:EQN}}` to Brent's `{{key:SOLVE}}` key, and how can you tell with certainty whether the number returned on the screen is a genuine root or a mathematical mirage?

Brent's solver operates as a **two-phase state machine**:
1. **Phase 1 — Guarded Secant & Golden-Ratio Outward Bracket Search:** If you place two initial guesses in **Registers $Y$ and $X$** that already straddle a sign change ($f(a)\cdot f(b) \le 0$), `{{key:SOLVE}}` uses your $(Y, X)$ stack shelves directly as the starting bracket $[a, b]$ and locks the jaws immediately. What if you store only a single seed $x_0$ via `{{key:STO}}` (or two guesses on the same side of the axis where $f(a)\cdot f(b) > 0$)? Phase 1 generates a companion probe ($\Delta = 0.1|x_0|$) and marches outward for up to $50$ steps using clamped secant steps—or expanding by the **golden ratio** $\phi \approx 1.618034$ whenever the slope is flat—while automatically pulling back any probe that steps outside the valid domain of $\ln x$ or $\sqrt{x}$, and detecting even-multiplicity tangent roots like $(x - 2)^2 = 0$ when $|b - a| < 10^{-12}$ and $|f(b)| < 10^{-7}$.
2. **Phase 2 — Inverse Quadratic / Secant Sprint with Five Bisection Watchdogs:** Once a sign change $f(a)\cdot f(b) \le 0$ is caged, Phase 2 attempts **Inverse Quadratic Interpolation (IQI)** whenever three distinct values $(f(a), f(b), f(c))$ are available, or a **Secant Chord** step otherwise. Before accepting the proposed step $s$, Brent's five watchdogs verify that $s$ lies strictly inside the three-quarter window $\left(\frac{3a+b}{4}, b\right)$ and shrinks the step width by at least $50\%$ every two steps; if any check fails, the engine takes a guaranteed **Bisection** step $m = \frac{1}{2}(a + b)$ until $|f(b)| \le 10^{-13}$ or the half-bracket width reaches machine tolerance $\text{tol} = 2\varepsilon_{\text{mach}}|b| + \frac{1}{2}\cdot 10^{-12}$.

Even more importantly, following **William Kahan's** diagnostic solver philosophy, you should always distinguish a genuine crossing root from a discontinuous pole. When `{{key:SOLVE}}` finishes on the SC-32, it writes the converged root $x^*$ into your target variable and pushes $x^*$ onto **Register $X$** while lifting your starting guess (or upper bracket bound) into **Register $Y$** and preserving the prior stack contents in **Registers $Z$ and $T$**. What if your initial bracket accidentally straddled a **vertical asymptote (discontinuous pole)** where the curve jumps from $-\infty$ to $+\infty$, such as $f(x) = \tan x$ across $x = \pi/2$ or $f(x) = \frac{1}{x - 2}$ across $x = 2$? Because $f(x)$ is negative on the left of the pole and positive on the right ($f(a)\cdot f(b) < 0$), bisection will pinch tightly around the pole $x = 2.0000000000$. Because `{{key:SOLVE}}` has already stored $x^*$ in your equation's variable, simply pressing **`{{key:XEQ}}`** (followed by your equation's letter) evaluates the residual $f(x^*)$ directly in Register $X$: at a **true root**, `{{key:XEQ}}` returns $f(x^*) \approx 0$ ($|f(x^*)| \le 10^{-12}$), whereas at a **false pole**, `{{key:XEQ}}` exposes a gigantic residual ($|f(x^*)| \gg 1$, or `DIVIDE BY 0`)!

---

## On the Stack: Horner Polynomials, POLY & Brent's SOLVE Workbench

We now have three complementary tools for polynomial and nonlinear equations: Horner's two-beat rhythm for evaluating polynomials from the inside out via `{{key:ENTER}} {{key:ENTER}} {{key:ENTER}}`, Cardano's analytical `{{key:POLY}}` workspace for extracting all three real or complex roots of a cubic or quadratic at once, and Richard Brent's bracketed `{{key:SOLVE}}` engine for hunting down transcendental roots in `{{key:EQN}}`. Let us step onto the SC-32 workbench and put all three engines through their paces across polynomial evaluations, principal-stress eigenvalues, and implicit engineering conservation laws.

{{res:sc32_cubic_roots:screenshot|Cubic polynomial x^3 - 6x^2 + 11x - 6 = 0 solved via POLY}}

### Horner's Nested Evaluation, T-Register Flooding & Biquadratic Reductions

To evaluate $P(x) = 4x^4 - 3x^3 + 2x^2 - 5x + 7$ at $x = 2.5$ in Horner's nested form $P(2.5) = (((4(2.5) - 3)(2.5) + 2)(2.5) - 5)(2.5) + 7$ with zero parentheses and zero memory registers, keying `{{res:sc32_07_polynomials_brent_solver_seq_01:keys}}` streams directly to **`{{res:sc32_07_polynomials_brent_solver_seq_01:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2.5 {{key:ENTER}} 4 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | First term: $a_4 x = 4(2.5) = 10.0$ |
| `3 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $7.0000$ | Add next coefficient: $10.0 - 3 = 7.0$ |
| `2.5 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $17.5000$ | Digit entry lifts $7.0$ to $Y$; multiply: $(7.0)(2.5) = 17.5$ |
| `2 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $19.5000$ | Add next coefficient: $17.5 + 2 = 19.5$ |
| `2.5 {{key:×}} 5 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $43.7500$ | Lift & multiply: $(19.5)(2.5) - 5 = 43.75$ |
| `2.5 {{key:×}} 7 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$116.3750$** | Final evaluation: $(43.75)(2.5) + 7 = \mathbf{116.3750}$ |

When $x$ has many digits (such as $x = 2.71828$), flood the 4-register stack first via `2.71828 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}`. Because Register $T$ replicates downward on every dyadic drop, you stream `4 {{key:×}} 3 {{key:-}} {{key:×}} 2 {{key:+}} {{key:×}} 5 {{key:-}} {{key:×}} 7 {{key:+}}` without ever re-typing $x$!

That same T-register replication evaluates **Martin Green's solar-cell fill factor** $FF = \frac{v_{\text{oc}} - \ln(v_{\text{oc}} + 0.72)}{v_{\text{oc}} + 1}$ at $v_{\text{oc}} = 25.145$ while typing `25.145` only once: key `25.145 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}`, then `0.72 {{key:+}} {{key:LN}} {{key:-}}` ($\to 21.8921$), and finally `{{key:x⇄y}} 1 {{key:+}} {{key:÷}}` to resolve **$FF = 0.837334$**. Similarly, for the coupled-oscillator **biquadratic** $x^4 - 10x^2 + 9 = 0$ ($u = x^2$), keying `10 {{key:x²}} 4 {{key:ENTER}} 9 {{key:×}} {{key:-}} {{key:√x}}` computes $\sqrt{\Delta} = 8.0000$, `10 {{key:x⇄y}} {{key:+}}` forms $18.0000$ while saving $8.0000$ in `LASTX`, `{{key:LASTX}} 10 {{key:x⇄y}} {{key:-}}` forms $2.0000$, and `2 {{key:÷}} {{key:√x}} {{key:x⇄y}} 2 {{key:÷}} {{key:√x}}` leaves both positive normal-mode frequencies side by side on the stack ($Y = \mathbf{1.0000},\; X = \mathbf{3.0000}$).

---

### Cardano's Analytical Cubic & Quadratic Solver

Pressing `{{key:POLY}}` (`Right Shift {{key:↱}} above {{key:XEQ}}`) opens the analytical polynomial solver for $Ax^3 + Bx^2 + Cx + D = 0$:

| Interface Element | Display Legend / Key Assignment | Functional Action / Internal Allocation |
| :--- | :--- | :--- |
| **Menu Prompt** | `Ax^3 + Bx^2 + Cx + D = 0` | Prompts for polynomial coefficient entry |
| **LFU Softkeys** | `{{key:A}} {{key:B}} {{key:C}} {{key:D}} {{key:EXEC}} {{key:CLR}}` | Softkey assignments for coefficient entry and execution |
| **Internal Storage: Root 1** | Variables `"1"` (Real), `"2"` (Imaginary) | Stores first calculated root (also placed in Registers $Y$ and $X$) |
| **Internal Storage: Root 2** | Variables `"3"` (Real), `"4"` (Imaginary) | Stores second calculated root |
| **Internal Storage: Root 3** | Variables `"5"` (Real), `"6"` (Imaginary) | Stores third calculated root |

Any unentered coefficient defaults to $0.0$ (at least one of $A$ or $B$ must be non-zero, otherwise `{{key:EXEC}}` displays `A ≠ 0`). Let us trace five analytical benchmarks inside `{{key:POLY}}`:

#### Casus Irreducibilis Cubic with Three Distinct Real Roots ($x^3 - 6x^2 + 11x - 6 = 0$)

To see how `{{key:POLY}}` navigates *casus irreducibilis* ($\Delta < 0$) automatically using François Viète's trigonometric cosine trisection, let us solve the classic factored cubic $(x - 1)(x - 2)(x - 3) = x^3 - 6x^2 + 11x - 6 = 0$. Inside `{{key:POLY}}`, load $A = 1$, $B = -6$, $C = 11$, and $D = -6$, then press `{{key:EXEC}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Coefficient $A = 1.0$ |
| `6 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-6.0000$ | Coefficient $B = -6.0$ |
| `11 {{key:C}}` | $0.0000$ | $1.0000$ | $-6.0000$ | $11.0000$ | Coefficient $C = 11.0$ |
| `6 {{key:+/-}} {{key:D}}` | $1.0000$ | $-6.0000$ | $11.0000$ | $-6.0000$ | Coefficient $D = -6.0$ |
| `{{key:EXEC}}` | $1.0000$ | $-6.0000$ | **$1.000000$** | **$0.000000$** | Primary root $r_1 = 1.0 + 0.0i$ in $(Y, X)$; roots $1, 2, 3$ in vars `1`–`6` |

Notice that `{{key:EXEC}}` sorts purely real roots in ascending order ($r_1 = 1.0$ in variables `1, 2`, $r_2 = 2.0$ in variables `3, 4`, and $r_3 = 3.0$ in variables `5, 6`), while placing the real part of $r_1$ in Register $Y$ and its zero imaginary part in Register $X$.

#### Cubic with Complex Conjugate Roots ($x^3 - x^2 + x - 1 = (x-1)(x^2+1) = 0$)

Now watch what happens when the cubic discriminant is strictly positive ($\Delta > 0$), so the cubic crosses the horizontal axis only once at $r_1 = 1.0$ and has a complex conjugate pair $r_{2,3} = 0.0 \pm 1.0i$. Inside `{{key:POLY}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Coefficient $A = 1.0$ |
| `1 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-1.0000$ | Coefficient $B = -1.0$ |
| `1 {{key:C}}` | $0.0000$ | $1.0000$ | $-1.0000$ | $1.0000$ | Coefficient $C = 1.0$ |
| `1 {{key:+/-}} {{key:D}}` | $1.0000$ | $-1.0000$ | $1.0000$ | $-1.0000$ | Coefficient $D = -1.0$ |
| `{{key:EXEC}}` | $1.0000$ | $-1.0000$ | **$1.000000$** | **$0.000000$** | Real $r_1=1$ in $Y$, Imag $r_1=0$ in $X$; conjugate pair $\pm i$ in vars `3`–`6` |

Recalling `{{key:RCL}} 3` ($0.0000$) and `{{key:RCL}} 4` ($+1.0000$) inspects $r_2 = +i$, while `{{key:RCL}} 5` ($0.0000$) and `{{key:RCL}} 6` ($-1.0000$) inspects $r_3 = -i$.

For the boundary case $\Delta = 0$—represented by the critically damped third-order RLC filter polynomial $s^3 + 12s^2 + 45s + 50 = (s+2)(s+5)^2 = 0$—keying `{{res:sc32_07_polynomials_brent_solver_seq_10:keys}}` inside `{{key:POLY}}` returns **`{{res:sc32_07_polynomials_brent_solver_seq_10:value}}`** as the first sorted real root in $(Y = -5.000000,\; X = 0.000000)$, storing both copies of the repeated root ($-5.0, -5.0$) and the simple root ($-2.0$) in variables `1`, `3`, and `5`.

#### 3D Cauchy Principal Stress Eigenvalues ($\lambda^3 - 70\lambda^2 + 1175\lambda - 5750 = 0$)

For a 3D structural steel element with stress invariants $I_1 = 70\text{ MPa}$, $I_2 = 1175\text{ MPa}^2$, and $I_3 = 5750\text{ MPa}^3$, the characteristic polynomial $\det(\boldsymbol{\sigma} - \lambda\mathbf{I}) = \lambda^3 - I_1\lambda^2 + I_2\lambda - I_3 = 0$ is guaranteed by the symmetry of Cauchy's stress tensor to lie in *casus irreducibilis* ($\Delta \le 0$) with three real eigenvalues $\sigma_3 \le \sigma_2 \le \sigma_1$. Entering the invariants into `{{key:POLY}}` via `{{res:sc32_07_polynomials_brent_solver_seq_12:keys}}` returns **`{{res:sc32_07_polynomials_brent_solver_seq_12:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:A}} 70 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-70.0000$ | Coefficients $A, B = -I_1$ |
| `1175 {{key:C}} 5750 {{key:+/-}} {{key:D}}` | $1.0000$ | $-70.0000$ | $1175.0000$ | $-5750.0000$ | Coefficients $C = I_2, D = -I_3$ |
| `{{key:EXEC}}` | $1.0000$ | $-70.0000$ | **$10.000000$** | **$0.000000$** | Minor stress $\sigma_3 = 10.0$ in $Y$; $\sigma_2, \sigma_1$ in vars `3`, `5` |
| `{{key:RCL}} 5` | $-70.0000$ | $10.0000$ | $0.0000$ | **$48.027756$** | Recall major principal stress $\sigma_1$ into Register $X$ |

Once $\sigma_1 = 48.0278\text{ MPa}$ is in Register $X$ and $\sigma_3 = 10.0000\text{ MPa}$ is in Register $Z$, keying `{{key:R↓}} {{key:x⇄y}} {{key:-}} 2 {{key:÷}}` immediately yields Henri Tresca's **maximum shear stress** $\tau_{\max} = \frac{1}{2}(\sigma_1 - \sigma_3) = \mathbf{19.0139\text{ MPa}}$!

#### Archimedes' Floating Oak Sphere Draft ($h^3 - 1.5h^2 + 0.325 = 0$)

For our solid oak marine buoy sphere of radius $R = 0.50\text{ m}$ ($1.00\text{ m}$ diameter) and specific gravity $\rho_s/\rho_w = 0.65$ floating in freshwater, plugging $R = 0.50$ and $\rho_s/\rho_w = 0.65$ into $h^3 - 3Rh^2 + 4(\rho_s/\rho_w)R^3 = 0$ gives $h^3 - 1.5h^2 + 0.325 = 0$. Solving this buoyant spherical-cap equilibrium equation in `{{key:POLY}}` via `{{res:sc32_07_polynomials_brent_solver_seq_13:keys}}` produces **`{{res:sc32_07_polynomials_brent_solver_seq_13:value}}`** ($60.14\%$ of the buoy's diameter submerged, while the algebraic companion roots $-0.4123\text{ m}$ and $1.3109\text{ m}$ lie outside the physical sphere $[0, 1.00\text{ m}]$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:A}} 1.5 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-1.5000$ | Load cubic and quadratic coefficients $A = 1.0,\; B = -1.5$ |
| `0 {{key:C}} 0.325 {{key:D}}` | $1.0000$ | $-1.5000$ | $0.0000$ | $0.3250$ | Load linear and constant coefficients $C = 0.0,\; D = 0.325$ |
| `{{key:EXEC}}` | $1.0000$ | $-1.5000$ | $-0.412257$ | $0.0000$ | Solve cubic; real parts of 3 roots stored in Variables `1`, `3`, `5` |
| `{{key:RCL}} 3` | $-1.5000$ | $-0.412257$ | $0.0000$ | **$0.601390$** | Recall physical immersion depth $h \in [0, 2R]$ from Variable `3` |

#### Tartaglia-Galileo Ballistic Trajectory Quadratic ($360.3673 u^2 - 1200u + 510.3673 = 0$)

For an elevated target at horizontal range $x = 1,200\text{ m}$ and height $y = 150\text{ m}$ engaged at muzzle speed $v_0 = 140\text{ m/s}$ ($\frac{gx^2}{2v_0^2} = 360.3673\text{ m}$), how do you solve a quadratic equation $a u^2 + b u + c = 0$ inside the cubic `{{key:POLY}}` workspace? You have two equally clean options: you can set the cubic coefficient $A = 0$ (`0 {{key:A}}`) and load $(B = a,\; C = b,\; D = c)$ to solve $Bx^2 + Cx + D = 0$ directly, or you can map the quadratic coefficients into $(A = a,\; B = b,\; C = c,\; D = 0)$, which multiplies the quadratic by $u$ to form $u(a u^2 + b u + c) = 0$ (adding a known dummy root at $u = 0$ while placing the two quadratic roots in variables `3` and `5`). Using the shifted $D = 0$ form, executing `{{res:sc32_07_polynomials_brent_solver_seq_02:keys}}` yields **`{{res:sc32_07_polynomials_brent_solver_seq_02:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `360.3673 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $360.3673$ | Quadratic coefficient $A$ |
| `1200 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $360.3673$ | $-1200.0000$ | Quadratic coefficient $B$ |
| `510.3673 {{key:C}}` | $0.0000$ | $360.3673$ | $-1200.0000$ | $510.3673$ | Quadratic coefficient $C$ |
| `0 {{key:D}}` | $360.3673$ | $-1200.0000$ | $510.3673$ | $0.0000$ | Depressed constant ($D$ defaults to $0.0$ if omitted) |
| `{{key:EXEC}}` | $360.3673$ | $-1200.0000$ | $0.0000$ | $0.0000$ | Solve polynomial; real roots $(0, u_1, u_2)$ stored in Variables `1`, `3`, `5` |
| `{{key:RCL}} 3 {{key:ATAN}}` | $-1200.0000$ | $0.0000$ | $0.0000$ | **$26.590116$** | Low direct-fire trajectory $\theta_1$ in degrees |
| `{{key:RCL}} 5 {{key:ATAN}}` | $0.0000$ | $0.0000$ | $26.590116$ | **$70.532306$** | High plunging mortar arc $\theta_2$ in degrees |

Similarly, for our forensic highway braking quadratic $v_0^2 + 20.594\,v_0 - 1166.99 = 0$ ($t_r = 1.5\text{ s},\; \mu = 0.70,\; d = 85.0\text{ m}$), keying `1 {{key:A}} 20.594 {{key:B}} 1166.99 {{key:+/-}} {{key:C}} 0 {{key:D}} {{key:EXEC}} {{key:RCL}} 5` inside `{{key:POLY}}` extracts the positive initial vehicle speed **$v_0 = 25.301\text{ m/s}$** ($91.1\text{ km/h}$).

---

### Hunting Transcendental Roots & Auditing Kahan's Stack with Brent's SOLVE

Let us first compare `{{key:SOLVE}}` and `{{key:POLY}}` side by side on two famous cubics (remembering that inside `{{key:EQN}}`, recalling a variable letter automatically lifts the stack, whereas two consecutive numeric literals require `{{key:ENTER}}` between them so their digits do not concatenate):

1. **John Wallis & Isaac Newton's 1669 Cubic Benchmark ($x^3 - 2x - 5 = 0$):** Programming `X {{key:3}} {{key:yˣ}} 2 {{key:ENTER}} X {{key:×}} {{key:-}} 5 {{key:-}}` into `{{key:EQN}}`, seeding Newton's initial guess `2 {{key:STO}} X`, and pressing `{{key:SOLVE}} X` converges to **$2.0945514815$**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2 {{key:STO}} X` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Initial guess loaded |
| `{{key:SOLVE}} X` | $0.0000$ | $0.0000$ | $2.0000$ | **$2.0945514815$** | Initial guess lifts to $Y$; root extracted in $X$ |

2. **Van der Waals Real Gas Equation for $\text{CO}_2$ ($50V^3 - 26.753V^2 + 3.59V - 0.153293 = 0$):** When $\text{CO}_2$ gas ($a = 3.59\text{ L}^2\cdot\text{atm/mol}^2,\; b = 0.0427\text{ L/mol}$) is compressed to $P = 50\text{ atm}$ at $T = 300\text{ K}$ ($RT = 24.618\text{ L}\cdot\text{atm/mol}$), solving the expanded Van der Waals cubic analytically inside `{{key:POLY}}` with `{{res:sc32_07_polynomials_brent_solver_seq_09:keys}}` delivers **`{{res:sc32_07_polynomials_brent_solver_seq_09:value}}`** ($27\%$ denser than an ideal gas's $RT/P = 0.4924\text{ L/mol}$, and identical to the molar volume $V_m = \mathbf{0.358736\text{ L/mol}}$ obtained by entering the unexpanded Van der Waals balance into `{{key:EQN}}` and running `0.49 {{key:STO}} V {{key:SOLVE}} V`):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `50 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $50.0000$ | Coefficient $A = 50.0$ |
| `26.753 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $50.0000$ | $-26.7530$ | Coefficient $B = -26.753$ |
| `3.59 {{key:C}}` | $0.0000$ | $50.0000$ | $-26.7530$ | $3.5900$ | Coefficient $C = 3.59$ |
| `0.153293 {{key:+/-}} {{key:D}}` | $50.0000$ | $-26.7530$ | $3.5900$ | $-0.153293$ | Coefficient $D = -0.153293$ |
| `{{key:EXEC}}` | $50.0000$ | $-26.7530$ | **$0.358736$** | **$0.000000$** | Real root in $Y$, Imag in $X$ |
| `{{key:x⇄y}}` | $50.0000$ | $-26.7530$ | $0.000000$ | **$0.358736$** | Molar volume $V_m$ in Register $X$ |

Now let us run `{{key:SOLVE}}` on five genuinely transcendental engineering equations:

#### Colebrook-White Turbulent Pipe Friction ($\text{Re} = 100,000,\; \varepsilon/D = 0.001$)

To solve Cyril Colebrook's implicit friction equation $\frac{1}{\sqrt{f}} + 2.0\log_{10}\!\left(\frac{\varepsilon/D}{3.7} + \frac{2.51}{\text{Re}\sqrt{f}}\right) = 0$ without Moody chart interpolation, enter `F {{key:√x}} {{key:1/x}}  0.001 {{key:ENTER}} 3.7 {{key:÷}}  2.51 {{key:ENTER}} 100000 {{key:÷}} F {{key:√x}} {{key:÷}} {{key:+}} {{key:LOG}} 2 {{key:×}} {{key:+}}` in `{{key:EQN}}` and seed the classic turbulent pipe guess $f_0 = 0.02$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0.02 {{key:STO}} F` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0200$ | Initial Moody plateau guess loaded |
| `{{key:SOLVE}} F` | $0.0000$ | $0.0000$ | $0.0200$ | **$0.022204$** | Darcy friction factor $f = 0.022204$ |

#### Kepler's Orbital Anomaly Equation ($E - 0.25\sin E - 1.20 = 0$)

For an Earth-observation satellite in an elliptical orbit of eccentricity $e = 0.25$ at mean anomaly $M = 1.20\text{ rad}$, set angular mode to `{{key:RAD}}`, enter `E  0.25 {{key:ENTER}} E {{key:SIN}} {{key:×}} {{key:-}} 1.20 {{key:-}}` in `{{key:EQN}}`, and seed the mean anomaly $E_0 = M = 1.20\text{ rad}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1.20 {{key:STO}} E` | $0.0000$ | $0.0000$ | $0.0000$ | $1.2000$ | Initial estimate $E_0 = M$ in radians |
| `{{key:SOLVE}} E` | $0.0000$ | $0.0000$ | $1.2000$ | **$1.488665$** | Eccentric anomaly $E$ in radians ($85.294^\circ$) |

#### Shockley Silicon Diode Load Line ($5.0 - 10^{-9}(e^{V/0.02585} - 1) - V = 0$)

For a $V_s = 5.0\text{ V}$ supply driving a silicon diode ($I_s = 10^{-12}\text{ A},\; V_T = 0.02585\text{ V}$) through a $R = 1\text{ k}\Omega$ series load resistor ($I_s R = 10^{-9}\text{ V}$), enter `5  V 0.02585 {{key:÷}} {{key:eˣ}} 1 {{key:-}} 1 {{key:E}} 9 {{key:+/-}} {{key:×}} {{key:-}}  V {{key:-}}` into `{{key:EQN}}`. To avoid exponential overflow on $e^{V/0.02585}$ during Phase 1's outward search, seed `V` right at the physical $0.65\text{ V}$ silicon turn-on knee:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0.65 {{key:STO}} V` | $0.0000$ | $0.0000$ | $0.0000$ | $0.6500$ | Initial estimate loaded |
| `{{key:SOLVE}} V` | $0.0000$ | $0.0000$ | $0.6500$ | **$0.672944$** | Diode forward voltage $V_D$ in Volts |

#### Open-Channel Froude Critical Depth ($400(3 + 4y) - 9.81(3y + 2y^2)^3 = 0$)

For a trapezoidal spillway channel of bottom width $b = 3.0\text{ m}$, side slopes $z = 2.0$, and discharge $Q = 20.0\text{ m}^3/\text{s}$ ($Q^2 = 400$, top width $T(y) = 3 + 4y$, and wetted area $A(y) = 3y + 2y^2$), enter the Froude $\text{Fr} = 1$ residual `3 {{key:ENTER}} 4 {{key:ENTER}} Y {{key:×}} {{key:+}} 400 {{key:×}}  3 {{key:ENTER}} Y {{key:×}}  Y {{key:x²}} 2 {{key:×}} {{key:+}} 3 {{key:yˣ}} 9.81 {{key:×}} {{key:-}}` into `{{key:EQN}}` and seed $y_0 = 1.0\text{ m}$ to locate the critical depth $y_c$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1.0 {{key:STO}} Y` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Initial depth estimate |
| `{{key:SOLVE}} Y` | $0.0000$ | $0.0000$ | $1.0000$ | **$1.258641$** | Critical flow depth $y_c$ in meters |

#### Nuclear Critical Buckling Radius & De Laval Rocket Nozzle Mach Branches

* **Spherical Fission Reactor Critical Radius ($\sin(0.045 R) = 0$):** In `{{key:RAD}}` mode, storing `R 0.045 {{key:×}} {{key:SIN}}` in `{{key:EQN}}` and running `60 {{key:STO}} R {{key:SOLVE}} R` isolates the fundamental buckling zero $0.045 R = \pi$ at **$R_{\text{crit}} = 69.813170\text{ cm}$** (whereas seeding $R_0 = 0$ would stop at the trivial zero $R = 0$).
* **Aurel Stodola's De Laval Nozzle Area-Mach Equation ($\frac{A}{A^*} = 2.50$ for $\gamma = 1.4$):** Storing `M {{key:x²}} 0.2 {{key:×}} 1 {{key:+}} 1.2 {{key:÷}} 3 {{key:yˣ}} M {{key:÷}} 2.50 {{key:-}}` in `{{key:EQN}}`:
  * Seeding above the $M = 1$ sonic throat via `2.5 {{key:STO}} M {{key:SOLVE}} M` isolates the **supersonic rocket exhaust root** **$M_{\text{sup}} = 2.442804$**.
  * Seeding below the $M = 1$ sonic throat via `0.2 {{key:STO}} M {{key:SOLVE}} M` isolates the **subsonic diffuser root** **$M_{\text{sub}} = 0.239541$**.

### Editing & Solving a Piecewise Equation in EQN Mode (`x?0` & `x?y`)

Suppose a precision aerospace isolation mount uses a primary coil spring of stiffness $k_1 = 2,000\text{ N/m}$ up to a clearance gap $x_0 = 0.05\text{ m}$ ($50\text{ mm}$), where a secondary elastomer bump-stop of stiffness $k_2 = 8,000\text{ N/m}$ engages—producing the **piecewise bilinear force law**:

$$F(x) = 2000x + 8000\langle x - 0.05 \rangle_+ = 2000x + 8000(x - 0.05)\cdot[x - 0.05 > 0]$$

To find the exact deflection $x^*$ under a static payload of $F_{\text{target}} = 350\text{ N}$, press `{{key:EQN}}` (`Right Shift {{key:↱}} above {{key:STO}}`), tap `NEW` (`{{key:LFU0}}`), press `A` for `00 LBL A`, and enter the residual $F(x) - 350$ using the three-step Macaulay ramp idiom (`{{key:ENTER}} {{key:x>0}} {{key:×}}`, accessing `{{key:x>0}}` via `{{key:x?0}}` on `Right Shift {{key:↱}} above {{key:÷}}`):

`{{key:RCL}} X  2000 {{key:×}}  {{key:RCL}} X  0.05 {{key:-}}  {{key:ENTER}} {{key:x>0}} {{key:×}}  8000 {{key:×}}  {{key:+}}  350 {{key:-}}  {{key:RTN}}`

Let us trace how this exact stack sequence evaluates to $F(0.03) = 60\text{ N}$ below the gap (where $[x - 0.05 > 0] = 0$) and $F(0.075) = 350\text{ N}$ above the gap (where $[x - 0.05 > 0] = 1$, confirming the root $x^* = \mathbf{0.0750\text{ m}}$ returned by `0.02 {{key:ENTER}} 0.10 {{key:SOLVE}} X`):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0.03 {{key:STO}} X` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0300$ | Test sub-gap deflection $x = 0.03\text{ m}$ |
| `2000 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $60.0000$ | Primary spring force $2000(0.03) = 60\text{ N}$ |
| `{{key:RCL}} X 0.05 {{key:-}}` | $0.0000$ | $0.0000$ | $60.0000$ | $-0.0200$ | Gap clearance $x - 0.05 = -0.02\text{ m} < 0$ |
| `{{key:ENTER}} {{key:x>0}} {{key:×}}` | $0.0000$ | $0.0000$ | $60.0000$ | $0.0000$ | Macaulay bracket $\langle -0.02 \rangle_+ = -0.02 \times 0 = 0$ |
| `8000 {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$60.0000$** | Bump-stop inactive; total force $F(0.03) = 60\text{ N}$ |
| `0.075 {{key:STO}} X` | $0.0000$ | $0.0000$ | $60.0000$ | $0.0750$ | Test post-gap root $x^* = 0.075\text{ m}$ from `SOLVE X` |
| `2000 {{key:×}}` | $0.0000$ | $0.0000$ | $60.0000$ | $150.0000$ | Primary spring force $2000(0.075) = 150\text{ N}$ |
| `{{key:RCL}} X 0.05 {{key:-}}` | $60.0000$ | $60.0000$ | $150.0000$ | $0.0250$ | Gap overrun $x - 0.05 = +0.025\text{ m} > 0$ |
| `{{key:ENTER}} {{key:x>0}} {{key:×}}` | $60.0000$ | $60.0000$ | $150.0000$ | $0.0250$ | Macaulay bracket $\langle +0.025 \rangle_+ = 0.025 \times 1 = 0.025$ |
| `8000 {{key:×}} {{key:+}}` | $60.0000$ | $60.0000$ | $60.0000$ | **$350.0000$** | Bump-stop adds $200\text{ N}$; $F(0.075) = \mathbf{350.0\text{ N}}$ |

Finally, let us summarize the post-`{{key:SOLVE}}` stack state and residual verification workflow:

| Stack / Action | Post-`{{key:SOLVE}}` Contents | Engineering Diagnostic Interpretation |
| :---: | :--- | :--- |
| **Register $X$** | **Converged Root Estimate ($x^*$)** | The final root estimate where $f(x^*)$ crosses or touches zero, also written into the target variable (`A`–`Z`). |
| **Register $Y$** | **Starting Seed or Upper Bracket Bound** | Lifted from Register $X$ when `{{key:SOLVE}}` pushes the converged root $x^*$ onto the stack. |
| **Registers $Z, T$** | **Prior Stack Context (Preserved)** | Any values previously in Registers $Y$ and $Z$ lift into $Z$ and $T$ undisturbed. |
| **`{{key:XEQ}}` Residual Audit** | **Evaluated Function Residual ($f(x^*)$)** | Because $x^*$ is already stored in your equation's target variable, pressing `{{key:XEQ}}` evaluates $f(x^*)$: a true root yields $\lvert f(x^*) \rvert \le 10^{-12}$, whereas an accidental vertical asymptote/pole exposes itself with $\lvert f(x^*) \rvert \gg 1$. |

### Practical Root-Finding Strategy: Bracket Seeding, Multiple Roots & Deflation on the Stack

When tackling unfamiliar nonlinear equations in the lab or field, four practical stack habits make `{{key:POLY}}` and `{{key:SOLVE}}` bulletproof:

1. **Verifying `{{key:POLY}}` Roots Instantly via Viète's Sum-and-Product Checksums:**
   Whenever `{{key:POLY}}` writes the three roots of $Ax^3 + Bx^2 + Cx + D = 0$ into variables `1` (Real 1), `3` (Real 2), and `5` (Real 3), you can verify the trace and determinant in six keystrokes:
   * Keying `{{key:RCL}} 1 {{key:RCL}} 3 {{key:+}} {{key:RCL}} 5 {{key:+}}` must equal $-B/A$ (for our stress tensor cubic $\lambda^3 - 70\lambda^2 + 1175\lambda - 5750 = 0$, $10.0 + 11.972244 + 48.027756 = \mathbf{70.000000}$).
   * Keying `{{key:RCL}} 1 {{key:RCL}} 3 {{key:×}} {{key:RCL}} 5 {{key:×}}` must equal $-D/A$ ($10.0 \times 11.972244 \times 48.027756 = \mathbf{5750.0000}$).
   * And when a cubic has complex conjugate roots $r_{2,3} = \alpha \pm i\beta$ stored in variables `3, 4` and `5, 6`, keying `{{key:RCL}} 4 {{key:RCL}} 3 {{key:▸θ,r}}` (`Left Shift {{key:↰}} above {{key:4}}`) converts $(\text{Re}, \text{Im})$ directly into the polar modulus $|r_2| = \sqrt{\alpha^2 + \beta^2}$ in Register $X$ and phase angle $\theta$ in Register $Y$.
2. **Isolating Specific Branches of Multi-Root Transcendental Equations:**
   Many physical conservation laws have two or more physically meaningful branches—such as the low direct-fire mortar angle vs. high plunging mortar angle, the subsonic vs. supersonic branches of Stodola's rocket nozzle Area-Mach relation ($M^* = 1$ throat sonic point separating $M_{\text{sub}} \in (0, 1)$ from $M_{\text{sup}} > 1$), or the subcritical vs. supercritical conjugate depths in open-channel hydraulics. Whenever an equation has multiple roots, place two bracket bounds $(a, b)$ in Registers $Y$ and $X$ that straddle ONLY the branch you want (for example, `0.05 {{key:ENTER}} 0.95` for the subsonic nozzle branch, or `1.05 {{key:ENTER}} 4.0` for the supersonic nozzle branch) so Brent's solver is locked inside that branch from iteration zero.
3. **Deflating Known Roots to Hunt Additional Roots (`(x - r₁)` Division):**
   Suppose you have found one root $r_1$ of a transcendental or high-degree equation $f(x) = 0$ (stored in Variable `A`) and want to search for a second root $r_2$ without having the solver fall back into the basin of attraction of $r_1$. Simply append `X {{key:RCL}} A {{key:-}} {{key:÷}}` to the end of your equation in `{{key:EQN}}` to form the deflated function $g(x) = \frac{f(x)}{x - r_1}$, removing the zero at $r_1$ completely.
4. **Recognizing `NO ROOT FND` (Code 08) & Even-Multiplicity Tangent Roots:**
   If a curve $f(x)$ stays strictly positive everywhere—such as $f(x) = x^2 + 4 = 0$, which has only complex roots $\pm 2i$—Phase 1's outward golden-ratio search terminates after 50 expansion steps and displays **`NO ROOT FND`** (Code 08, cleared via `{{key:C}}`). Conversely, if a curve merely *kisses* the axis tangentially at an even-multiplicity root such as $(x - 3)^2 = 0$, its derivative $f'(3)$ is zero at the root, so the classic secant slope becomes horizontal; Brent's solver detects the tangent minimum when $|b - a| < 10^{-12}$ and $|f(b)| < 10^{-7}$, or you can solve $f'(x) = 0$ directly to recover full quadratic convergence.

---

### From Where a Curve Crosses Zero to How Fast It Moves

Consider what we have conquered in Chapter 7: give us any continuous curve $f(x)$—whether it is a third-degree stress polynomial, Kepler's elliptical orbit equation, or Colebrook's turbulent pipe law—and we can pinpoint the exact spot $x^*$ where the curve crosses zero.

Yet knowing where a curve sits at a single equilibrium point is only the beginning of physics. Suppose that instead of asking *where* a rising Saturn V rocket crosses a given altitude, we ask two dynamic questions:
1. **How fast is the curve changing at this exact microsecond?** (Its instantaneous slope, or **derivative**, $\frac{df}{dx}$.)
2. **How much total distance, work, or impulse has accumulated underneath the curve from $x = a$ to $x = b$?** (Its curved area, or **definite integral**, $\int_a^b f(x)\,dx$.)

And what do we do when the curve whose area we need to measure—like the large-angle swing of a grandfather clock's pendulum or the velocity profile of a rocket shedding fifteen tons of propellant every second—has no elementary antiderivative in any calculus textbook? In **[Chapter 8: Slicing Infinity: From Archimedes and Saturn V to Romberg's 4/3 − 1/3 Miracle](08-calculus-romberg-quadrature.md)**, we step into the twin engines of calculus and discover how a deceptively simple $\frac{4}{3} - \frac{1}{3}$ weighting trick melts away numerical approximation error.
