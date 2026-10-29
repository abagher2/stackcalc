---
title: "Chapter 7: Polynomial Evaluation, Cardano's Cubic & Brent's Root-Finder | Thinking in the Stack (SC-32)"
description: "Al-Khwarizmi's completion of the square, the 1535 Milan cubic contest, Horner's nested evaluation, and Richard Brent's hybrid root solver on the StackCalc SC-32."
---

# Chapter 7: Polynomial Evaluation, Cardano's Cubic & Brent's Root-Finder

## Al-Khwarizmi's Squares and the 1535 Contest in Milan

Around the year 820 CE, in Baghdad's House of Wisdom (*Bayt al-Hikma*), the Persian mathematician and astronomer Muhammad ibn Musa al-Khwarizmi wrote the foundational treatise *Al-Kitāb al-mukhtaṣar fī ḥisāb al-jabr wa'l-muqābala* (*The Compendious Book on Calculation by Completion and Balancing*). Its title gave every language on Earth the word *algebra*, from *al-jabr* (restoring a subtracted term to the opposite side of an equation), while his own name, Latinized as *Algoritmi*, gave us the word *algorithm*.

When al-Khwarizmi set out to solve a quadratic equation such as his canonical benchmark:

$$x^2 + 10x = 39$$

he did not reach for modern algebraic symbols, because plus signs, minus signs, and exponents would not be invented for another seven hundred years. Notably, al-Khwarizmi did not view $x^2$ as an abstract number multiplied by itself; he viewed $x^2$ as a *physical square* of side $x$, and $10x$ as the area of a rectangle.

To find the side $x$ of a square when its area $x^2$ plus $10x$ equals $39$, al-Khwarizmi constructed a geometric figure in four steps. He began with a central square of side $x$ and area $x^2$, then split the linear term $10x$ in half into two equal rectangles of width $5$ and length $x$ (each having area $5x$) and attached them to two adjacent edges of the $x \times x$ square. The resulting L-shaped figure (a *gnomon*) forms a larger square of side $(x + 5)$ except that the upper-right corner where the two $5 \times x$ wings meet is missing a $5 \times 5$ corner square of area $25$. Dropping a $5 \times 5 = 25$ square into that empty corner *completes the square*, and adding the same $25$ to the $39$ on the right balances the areas:

$$(x + 5)^2 = 39 + 25 = 64 = 8^2 \implies x + 5 = 8 \implies \mathbf{x = 3}$$

{{blocks:sc32_concept_khwarizmi_brent|Al-Khwarizmi's geometric completion of the square (820 CE) and Richard Brent's root-hunting bracket cage (SOLVE).}}

Applying that same geometric completion to the general quadratic equation $a x^2 + b x + c = 0$—dividing by $a$, splitting the middle term $(b/a)x$ into two wings of width $\frac{b}{2a}$, and filling the missing corner with $\left(\frac{b}{2a}\right)^2$—yields the universal *quadratic formula*:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

### William Kahan's Warning: Catastrophic Cancellation in the Quadratic Formula

In finite-precision floating-point arithmetic, al-Khwarizmi's quadratic formula requires careful numerical handling. As Berkeley numerical analyst William Kahan demonstrated, the standard formula $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ contains a numerical instability whenever $b^2$ is much larger than $4ac$ ($b^2 \gg |4ac|$).

When $b > 0$ and $4ac$ is tiny compared to $b^2$, the radical $\sqrt{b^2 - 4ac}$ is nearly equal to $b$. Evaluating the root with the plus sign ($-b + \sqrt{b^2 - 4ac}$) subtracts two nearly equal numbers and cancels up to half or more of the calculator's significant digits through *catastrophic cancellation*. As codified by William Kahan and in Press, Teukolsky, Vetterling, and Flannery's *Numerical Recipes*, avoiding this loss of significance requires never subtracting $\sqrt{b^2 - 4ac}$ from a number of the same sign. Instead, one forms the *Citardauq* ("Quadratic" spelled backward) intermediate quantity $q$ by choosing the sign that *adds* the magnitudes together, and then extracts the larger root $x_1 = q/a$ and the smaller root $x_2 = c/q$ via François Viète's root-product identity $x_1 x_2 = \frac{c}{a}$:

$$q = -\frac{1}{2}\Big(b + \operatorname{sgn}(b)\sqrt{b^2 - 4ac}\Big), \qquad x_1 = \frac{q}{a}, \qquad x_2 = \frac{c}{q}$$

Because $q$ is formed by pure magnitude addition (`b {{key:x²}} 4 {{key:ENTER}} a {{key:×}} c {{key:×}} {{key:-}} {{key:√x}} |b| {{key:+}} 2 {{key:÷}}` with sign $-\operatorname{sgn}(b)$), both $x_1 = q/a$ and $x_2 = c/q$ retain every guard digit of precision even when $b^2$ exceeds $4ac$ by ten orders of magnitude.

Quadratic equations govern two classic inverse problems in mechanics and forensic engineering: inverse ballistic trajectories and highway stopping distance reconstruction. Whereas forward ballistics projects where a shell lands when its launch angle $\theta$ is already known, the inverse ballistic problem fixes the target coordinates $(x, y)$ on an elevated ridge at known muzzle speed $v_0$ and solves backward for the required launch angle $\theta$. Substituting the trigonometric identity $\sec^2\theta = 1 + \tan^2\theta$ into Galileo's parabolic trajectory $y = x\tan\theta - \frac{gx^2}{2v_0^2}\sec^2\theta$ converts the unknown launch slope $u = \tan\theta$ into a quadratic equation:

$$\left(\frac{gx^2}{2v_0^2}\right) u^2 - x u + \left(y + \frac{gx^2}{2v_0^2}\right) = 0$$

Whenever the target lies within range, its two positive roots give the gunner two distinct paths to the same coordinates: a flat, fast low direct-fire trajectory ($\theta_1 = \arctan u_1$) and a high, arcing plunging mortar trajectory ($\theta_2 = \arctan u_2$) that descends from above. A similar quadratic governs highway braking and reaction stopping distance ($d = v_0 t_r + \frac{v_0^2}{2\mu g}$). When a driver spots a hazard on the highway, the vehicle travels at its initial speed $v_0$ during the human perception-reaction time $t_r$ ($d_{\text{react}} = v_0 t_r$) before the brakes lock and tire-pavement friction $\mu$ decelerates the vehicle to a halt over a kinetic-energy braking distance $d_{\text{brake}} = \frac{v_0^2}{2\mu g}$. When crash investigators measure the total stopping distance $d$ at the scene, reconstructing the vehicle's unknown initial speed $v_0$ requires extracting the positive root of the monic quadratic:

$$v_0^2 + (2\mu g t_r)\, v_0 - 2\mu g d = 0$$

### The 1535 Milanese Cubic Contest, Cardano's Formula & Casus Irreducibilis

For seven centuries after al-Khwarizmi, the *cubic equation* ($A x^3 + B x^2 + C x + D = 0$) stood unsolved. In 1494, the Franciscan friar Luca Pacioli (Leonardo da Vinci's mathematics collaborator) declared in his *Summa de arithmetica* that solving the general cubic was as impossible with existing mathematics as squaring the circle.

Pacioli was mistaken. Around 1515, Bologna mathematics professor Scipione del Ferro discovered how to solve the "depressed" cubic $t^3 + pt = q$ (a cubic with no $t^2$ term). In Renaissance Italy, however, university chairs were not protected by lifelong tenure; a mathematician could be publicly challenged to a high-stakes problem-solving contest in which the loser forfeited his salary, reputation, and professorship. Consequently, del Ferro kept his unpublished solution confidential until his deathbed in 1526, when he entrusted the manuscript to his student Antonio Maria Fior.

Possessing his late master's confidential formula, Fior began boasting that he alone could solve cubic equations, and in early 1535 he challenged Venetian mathematician Niccolò Fontana, born in Brescia and known as Tartaglia ("The Stammerer," after a French soldier's saber wounded his jaw and palate during the 1512 sack of Brescia and left him with a permanent speech impediment). Each contestant deposited thirty cubic problems with a notary in Milan and was given fifty days to solve the rival's list.

Fior had set all thirty of his problems as variations of del Ferro's single form $t^3 + pt = q$. Tartaglia, on the other hand, had posed several different families of cubics, including $t^3 + pt^2 = q$. On the night of February 12, 1535, eight days before the deadline, Tartaglia discovered the general reduction by dissecting a three-dimensional cube of side $(u - v)$ into smaller blocks:

$$(u - v)^3 + 3uv(u - v) = u^3 - v^3$$

Tartaglia saw that setting $t = u - v$, $3uv = p$, and $u^3 - v^3 = -q$ reduces the cubic $t^3 + pt + q = 0$ to a *quadratic equation in $u^3$*. Within two hours Tartaglia solved all thirty of Fior's problems, whereas Fior failed to solve a single one of Tartaglia's.

News of Tartaglia's victory reached the Milanese physician and algebraist Gerolamo Cardano. In March 1539, Cardano invited Tartaglia to his house and requested the formula, pledging not to publish Tartaglia's method. Tartaglia relented and encoded his rule in a twenty-five-line Italian poem (*"Quando che'l cubo con le cose appresso..."*).

Cardano then combined Tartaglia's rule with his own discovery that *any* full cubic $A x^3 + B x^2 + C x + D = 0$ can be stripped of its quadratic $x^2$ term by translating the coordinate origin to the curve's point of inflection via $x = t - \frac{B}{3A}$:

$$t^3 + p t + q = 0, \qquad p = \frac{3AC - B^2}{3A^2}, \qquad q = \frac{27A^2D - 9ABC + 2B^3}{27A^3}$$

Cardano and his pupil Lodovico Ferrari, who soon discovered how to solve the fourth-degree *quartic equation* by reducing it to a resolvent cubic, now possessed the complete analytical solution to every polynomial up to degree four. In 1543, Cardano traveled to Bologna, inspected Scipione del Ferro's posthumous papers, and verified that del Ferro had discovered the formula twenty years *before* Tartaglia. Considering himself released from his pledge, Cardano published the complete cubic and quartic solutions in his 1545 treatise *Ars Magna* (*The Great Art*) {{cite:cardano1545}}, crediting both del Ferro and Tartaglia.

Inside Cardano's cubic formula appeared an algebraic paradox that led to the discovery of complex numbers:

$$t = \sqrt[3]{-\frac{q}{2} + \sqrt{\Delta}} + \sqrt[3]{-\frac{q}{2} - \sqrt{\Delta}}, \qquad \text{where } \Delta = \left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3$$

Here the *cubic discriminant* $\Delta$ governs the nature of the three roots across three distinct regimes. When $\Delta > 0$, the S-shaped cubic crosses the horizontal axis only once and has *one real root* and *two complex conjugate roots*, formed by rotating $u = \sqrt[3]{-q/2 + \sqrt{\Delta}}$ and $v = \sqrt[3]{-q/2 - \sqrt{\Delta}}$ by the cube roots of unity $\omega = -\frac{1}{2} + i\frac{\sqrt{3}}{2}$ and $\omega^2$. When $\Delta = 0$, the cubic touches the horizontal axis tangentially and produces *three real roots with at least one repeated root*, as in the critically damped RLC filter polynomial $s^3 + 12s^2 + 45s + 50 = (s+2)(s+5)^2 = 0$ with a double pole at $s = -5$.

When $\Delta < 0$, the regime known as *casus irreducibilis*, the cubic crosses the horizontal axis three times to produce *three distinct real roots* (such as $(x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x - 6 = 0$), yet the discriminant $\Delta$ under the square root is *strictly negative*. Extracting those three real numbers from Cardano's formula requires passing through the complex plane and taking the cube root of a complex number $r e^{i\theta}$ by De Moivre's angle trisection $r^{1/3}[\cos(\theta/3) + i\sin(\theta/3)]$, where the imaginary parts of the two conjugate cube roots cancel to zero.

### Viète's Trigonometric Escape, Ferrari's Quartic & the Root-Coefficient Checksums

Sixteenth-century algebraists bypassed the complex radicals of *casus irreducibilis* through trigonometry and verified their roots through symmetric coefficient identities, methods that form the foundation of the SC-32's analytical solver.

On the SC-32, pressing `{{key:POLY}}` (`{{key:↱}}` + `{{key:XEQ}}`) opens the dedicated analytical polynomial workspace for $Ax^3 + Bx^2 + Cx + D = 0$, mapping the six LFU softkeys to `{{key:A}}`, `{{key:B}}`, `{{key:C}}`, `{{key:D}}`, `{{key:EXEC}}`, and `{{key:CLR}}`. Key each coefficient onto the stack and tap its softkey, setting `0 {{key:D}}` whenever you want to solve a quadratic $Ax^2 + Bx + C = 0$. Pressing `{{key:EXEC}}` evaluates the discriminant $\Delta$, places the primary root $r_1$ onto the stack in Gaussian complex format ($Y = \text{Real},\; X = \text{Imag}$), and writes all three real or complex roots into numbered variable registers `1` through `6` (`{{key:RCL}} 1` through `{{key:RCL}} 6`).

Behind that single `{{key:EXEC}}` keystroke stand three classical results of polynomial theory: François Viète's trigonometric trisection, Lodovico Ferrari's quartic resolvent, and Viète's root-coefficient relations. In 1593, the French cryptographer and algebraist François Viète noted the structural correspondence between the depressed cubic $t^3 + pt + q = 0$ (when $\Delta < 0$, so $p < 0$) and the trigonometric triple-angle identity for cosine:

$$\cos(3\theta) = 4\cos^3\theta - 3\cos\theta \implies \cos^3\theta - \frac{3}{4}\cos\theta - \frac{1}{4}\cos(3\theta) = 0$$

By scaling the unknown as $t = 2\sqrt{-p/3}\,\cos\theta$, Viète matched the depressed cubic term-for-term against the triple-angle cosine identity and expressed all three real roots in closed form without complex square roots:

$$t_k = 2\sqrt{-\frac{p}{3}} \cos\left(\frac{1}{3}\arccos\left(\frac{3q}{2p}\sqrt{-\frac{3}{p}}\right) - \frac{2\pi k}{3}\right), \qquad k = 0, 1, 2$$

Geometrically, solving a three-real-root cubic is equivalent to *trisecting an angle on the unit circle* and projecting the three $120^\circ$-spaced vertices of an inscribed equilateral triangle onto the horizontal real axis.

Right after Cardano mastered the cubic in 1539, Venetian mathematics teacher Zuanne da Coi challenged Cardano and Tartaglia with a fourth-degree *quartic equation*: $x^4 + 6x^2 + 36 = 60x$. In 1540, Cardano's pupil Lodovico Ferrari solved it by reducing the quartic to a resolvent cubic. After shifting $x$ to remove the $x^3$ term ($x^4 + px^2 + qx + r = 0$), Ferrari moved $px^2 + qx + r$ to the right side, completed the square on the left as $(x^2 + \frac{p}{2})^2$, and introduced an *auxiliary variable $y$* inside the square:

$$\left(x^2 + \frac{p}{2} + y\right)^2 = (p + 2y)x^2 - qx + \left(\frac{p^2}{4} - r + py + y^2\right)$$

The right-hand side is an ordinary *quadratic in $x$*, which becomes a perfect square $(mx + n)^2$—so that the square root can be taken on both sides—precisely when its quadratic discriminant $B^2 - 4AC$ equals zero:

$$q^2 - 4(p + 2y)\left(y^2 + py + \frac{p^2}{4} - r\right) = 0$$

That condition for the auxiliary variable $y$ is a *third-degree cubic equation*, the *resolvent cubic*, which Cardano's `{{key:POLY}}` solver can solve directly. Once one root $y_1$ of the resolvent cubic is found, the quartic splits into two ordinary quadratic equations that yield all four roots.

Whenever `{{key:POLY}}` writes the roots of a cubic ($A x^3 + B x^2 + C x + D = 0$) into variables `1` through `6`, Viète's root-coefficient formulas verify the roots immediately without substituting each value back into the polynomial. Expanding $A(x - r_1)(x - r_2)(x - r_3) = A x^3 - A(r_1 + r_2 + r_3)x^2 + A(r_1 r_2 + r_2 r_3 + r_3 r_1)x - A r_1 r_2 r_3$ and matching coefficients term by term yields the *sum of roots* (*trace*), *pairwise product sum*, and *product of roots* (*determinant*):

$$r_1 + r_2 + r_3 = -\frac{B}{A}, \qquad r_1 r_2 + r_2 r_3 + r_3 r_1 = +\frac{C}{A}, \qquad r_1 \cdot r_2 \cdot r_3 = -\frac{D}{A}$$

For our benchmark cubic $x^3 - 6x^2 + 11x - 6 = 0$ with roots $1, 2, 3$, recalling and summing `{{key:RCL}} 1 {{key:RCL}} 3 {{key:+}} {{key:RCL}} 5 {{key:+}}` gives the trace $1 + 2 + 3 = 6 = -(-6)/1$. Likewise, their pairwise product sum is $1(2) + 2(3) + 3(1) = 11 = +11/1$, and their determinant product `{{key:RCL}} 1 {{key:RCL}} 3 {{key:×}} {{key:RCL}} 5 {{key:×}}` is $1 \times 2 \times 3 = 6 = -(-6)/1$. In any *depressed cubic* $t^3 + pt + q = 0$ (where $B = 0$), the three roots always sum identically to zero ($t_1 + t_2 + t_3 = 0$), because the coordinate shift $x = t - \frac{B}{3A}$ places the origin at the centroid of the three roots.

That chain of radical reductions stopped permanently after Ferrari's degree-4 quartic. For nearly three hundred years after *Ars Magna*, European mathematicians—including Ehrenfried Walther von Tschirnhaus, Leonhard Euler, and Joseph-Louis Lagrange—sought a general degree-5 quintic formula ($Ax^5 + Bx^4 + Cx^3 + Dx^2 + Ex + F = 0$). Lagrange identified the underlying obstacle: for a degree-2 quadratic, the resolvent has degree 1; for a degree-3 cubic, Tartaglia's resolvent has degree 2; for a degree-4 quartic, Ferrari's resolvent has degree 3. In each case, the auxiliary equation had *lower* degree than the original polynomial. Yet when Lagrange applied the same permutation method to a degree-5 quintic, the resolvent equation jumped *up* to degree 6 (with $5!/2 = 60$ alternating permutations).

In 1824, Norwegian mathematician Niels Henrik Abel built on Paolo Ruffini's 1799 work to prove that this barrier is absolute. Eight years later, on the night of May 29, 1832, French mathematician Évariste Galois wrote a testamentary letter summarizing his discoveries on the eve of his death at age twenty, founding *Group Theory* and explaining the structural cause. For degrees $n = 2, 3, 4$, the permutation group $S_n$ of the roots decomposes into commutative cyclic quotients ("solvable groups") that correspond to extracting $k$-th roots $\sqrt[k]{\phantom{x}}$. For $n \ge 5$, however, the alternating group $A_5$, which is isomorphic to the $60$ rotational symmetries of a regular icosahedron, is a *simple non-abelian group* that cannot be factored into cyclic steps. No general radical formula in $+, -, \times, \div$, and $\sqrt[n]{\phantom{x}}$ can exist for degree 5 or higher.

---

## Unpeeling Polynomials from the Inside Out: Horner's Scheme

Before solving a polynomial equation $P(x) = 0$, one needs an efficient, numerically stable method to evaluate $P(x)$ at any argument $x = x_0$.

Consider the general fourth-degree quartic polynomial:

$$P(x) = a_4 x^4 + a_3 x^3 + a_2 x^2 + a_1 x + a_0$$

Evaluating $P(x)$ term by term as written—computing $x^4$, multiplying by $a_4$, computing $x^3$, multiplying by $a_3$, computing $x^2$, and so on—repeats power computations unnecessarily ($4 + 3 + 2 + 1 = 10$ multiplications, or three separate exponentiations). Worse, near a root where large positive and negative power terms nearly cancel, computing $a_n x^n$ separately magnifies floating-point rounding error.

In 1819, the English schoolmaster William George Horner (rediscovering a method known to Isaac Newton in 1669 and the 13th-century Chinese algebraist Qin Jiushao in his 1247 *Mathematical Treatise in Nine Sections*) showed what happens when $x$ is factored from the inside out:

$$P(x) = a_4 x^4 + a_3 x^3 + a_2 x^2 + a_1 x + a_0 = \Big(\big((a_4 x + a_3)x + a_2\big)x + a_1\Big)x + a_0$$

In *Horner's nested scheme*, every explicit exponent vanishes. To evaluate any degree-$n$ polynomial at $x_0$, you start with the leading coefficient $b_n = a_n$ and repeat a two-step linear recurrence $b_k = b_{k+1} x_0 + a_k$ exactly $n$ times, multiplying the running value by $x_0$ (`{{key:×}}`) and adding the next coefficient $a_k$ (`{{key:+}}` or `{{key:-}}`). Across the four nested stages of a quartic $P(x_0) = (((a_4 x_0 + a_3)x_0 + a_2)x_0 + a_1)x_0 + a_0$, the running accumulator in Register $X$ starts with $b_4 = a_4$, multiplies by $x_0$, and adds $a_3$ in the first stage to form $b_3 = a_4 x_0 + a_3$; multiplies $b_3$ by $x_0$ and adds $a_2$ in the second stage to form $b_2 = b_3 x_0 + a_2$; multiplies $b_2$ by $x_0$ and adds $a_1$ in the third stage to form $b_1 = b_2 x_0 + a_1$; and finally multiplies $b_1$ by $x_0$ and adds $a_0$ to reach the remainder $b_0 = b_1 x_0 + a_0 = P(x_0)$.

This recurrence requires four multiplications, four additions, zero powers, and zero temporary variables. On the SC-32, Horner's scheme runs even faster when all four stack registers are filled with $x_0$ at the outset via `x0 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}`. Because the top register $T$ replicates its value downward into Register $Z$ every time the stack drops, a fresh copy of $x_0$ awaits in Register $Y$ whenever a coefficient addition completes, so the four-register stack operates as an automatic Horner recurrence pipeline without re-typing $x_0$.

Furthermore, the intermediate values $(b_4, b_3, b_2, b_1)$ produced at each step of Horner's recurrence have direct algebraic meaning: they are the exact coefficients of the cubic quotient polynomial $Q(x)$ obtained by *Ruffini-Horner synthetic division* when dividing $P(x)$ by $(x - x_0)$:

$$P(x) = (x - x_0)\,Q(x) + b_0 = (x - x_0)\left(b_4 x^3 + b_3 x^2 + b_2 x + b_1\right) + P(x_0)$$

This Polynomial Remainder Theorem identity $P(x) = (x - x_0)Q(x) + P(x_0)$ provides polynomial deflation, simultaneous derivative evaluation, and suppression of catastrophic cancellation near multiple roots. Once one exact root $r_1$ of a polynomial is found (where the remainder $P(r_1) = 0$), the intermediate numbers generated during Horner's evaluation at $r_1$ supply the deflated degree-$(n-1)$ quotient polynomial $Q(x) = P(x)/(x - r_1)$, which reduces a fourth-degree quartic to a cubic or a cubic to a quadratic. Differentiating $P(x) = (x - x_0)Q(x) + P(x_0)$ with respect to $x$ by the product rule yields:

$$P'(x) = Q(x) + (x - x_0)Q'(x) \implies P'(x_0) = Q(x_0)$$

Evaluating the quotient polynomial $Q(x)$ at $x_0$ by running a second Horner pass on the intermediate coefficients therefore gives the exact derivative $P'(x_0)$ without a separate symbolic derivative formula. In computational thermodynamics and flight-control engineering—where computers evaluate standard-atmosphere pressure-altitude curves $P(h) = a_3 h^3 + a_2 h^2 + a_1 h + a_0$ and NASA Glenn molar heat-capacity fits $C_p(T)/R = a_0 + a_1 T + a_2 T^2 + a_3 T^3 + a_4 T^4$—nested Horner evaluation also suppresses cancellation near repeated roots such as $s = -5$ in the critically damped RLC filter by updating the local factor $(s + 5)$ at each step instead of subtracting large, independently rounded powers $s^3$ and $12s^2$.

That same nested-factoring approach simplifies rational formulas and symmetric high-degree equations across physics. In a silicon photovoltaic cell, the maximum power point satisfies a transcendental diode equation that cannot be inverted in closed form, but Australian solar physicist Martin Green (1982) established an accurate rational-logarithmic expression in the normalized open-circuit voltage $v_{\text{oc}} = V_{\text{oc}} / V_T$, evaluated in one pass on the stack by replicating $v_{\text{oc}}$ across all four registers with `{{key:ENTER}} {{key:ENTER}} {{key:ENTER}}`:

$$\text{Fill Factor } FF = \frac{v_{\text{oc}} - \ln(v_{\text{oc}} + 0.72)}{v_{\text{oc}} + 1}$$

Similarly, when two coupled undamped spring-mass pendulums vibrate in their natural normal modes, the eigenvalue equation $\det(\mathbf{K} - \omega^2\mathbf{M}) = 0$ forms a biquadratic polynomial containing only even powers of frequency ($a x^4 + b x^2 + c = 0$), which reduces to a quadratic in $u = x^2$ whose positive square roots $\omega = \sqrt{u}$ give the two normal-mode frequencies.

---

## Tangent Instabilities in Newton's Method and Brent's Hybrid Algorithm

Abel and Galois proved that $x^5 - x - 1 = 0$ cannot be solved with a radical formula, and in applied physics and engineering, governing laws rarely appear as pure polynomials. Physical conservation laws routinely combine algebraic powers $x$ with sines, cosines, exponentials, and logarithms in *transcendental equations* where no symbolic manipulation can isolate the unknown on one side of the equals sign.

Isolating a root $x^*$ where $f(x^*) = 0$ when symbolic algebra cannot invert $f(x)$ led numerical analysts to two contrasting approaches: interval bisection and local tangent or secant extrapolation. When a continuous curve $f(x)$ lies below the axis at $x = a$ with $f(a) < 0$ and above it at $x = b$ with $f(b) > 0$, so that $f(a)\cdot f(b) < 0$, Bernard Bolzano's 1817 *Intermediate Value Theorem* guarantees that the curve crosses $y = 0$ at least once inside the *bracket* $[a, b]$. The *Bisection Method* evaluates the function at the midpoint $m = \frac{1}{2}(a + b)$, inspects its sign, and discards whichever half does not contain the sign change. Every step halves the uncertainty and gains $1\text{ binary bit}$ of precision per step (linear convergence, order $p = 1.000$). After $40$ bisections, the bracket shrinks by $2^{-40} \approx 10^{-12}$, though requiring $40$ to $50$ evaluations makes bisection slow.

To accelerate convergence, Isaac Newton in 1669 (testing John Wallis's cubic benchmark $x^3 - 2x - 5 = 0$ near $x_0 = 2$) and Joseph Raphson in 1690 proposed following the local tangent line of the curve:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Near a simple root, the Newton-Raphson method is *quadratically convergent* ($p = 2.000$) and doubles the number of accurate decimal digits on every step ($1 \to 2 \to 4 \to 8 \to 16\text{ digits}$). When the analytic derivative $f'(x)$ is unavailable, replacing the tangent slope with the *Secant Chord* through the last two iterates yields superlinear convergence at the *golden-ratio exponent* $p = \phi = \frac{1+\sqrt{5}}{2} \approx 1.618$. The vulnerability of Newton-Raphson and the Secant Method lies in the slope denominator $f'(x_n)$ (or $f(x_n) - f(x_{n-1})$). Whenever an iterate lands near a local extremum, an inflection plateau, or a horizontal asymptote where the slope flattens out ($f'(x_n) \approx 0$), the nearly horizontal tangent line projects the next estimate $x_{n+1}$ far outside the region of interest or into an oscillatory cycle.

### Richard Brent's 1973 Hybrid Root-Finding Algorithm

In 1973, building on earlier work by Theodorus Dekker, the Australian mathematician Richard P. Brent demonstrated in *Algorithms for Minimization Without Derivatives* {{cite:brent1973}} how to combine the guaranteed bracketing of Bisection with the superlinear convergence of Interpolation so that the solver achieves rapid convergence on smooth curves, requires no derivatives, and never diverges outside its bracket. Six years later, UC Berkeley numerical analyst William M. Kahan {{cite:kahan1979}} adapted this Dekker–Brent hybrid philosophy for Hewlett-Packard's pocket `SOLVE` key, which debuted on the 1979 HP-34C, continued into the 1982 HP-15C Voyager {{cite:hp15c1982}}, and paired with symbolic equations on the 1991 HP-32SII Pioneer {{cite:hp32sii1991}}.

Brent's hybrid root-finding algorithm, which drives the SC-32's 64-bit `{{key:SOLVE}}` key (`{{key:↱}}` + `{{key:7}}`, paired with the `{{key:EQN}}` equation editor), combines inverse quadratic interpolation with five acceptance tests. Given three distinct points $(a, f(a))$, $(b, f(b))$, and $(c, f(c))$ near the root, fitting an ordinary upright parabola $y = P(x)$ can fail whenever its vertex turns around before reaching the $x$-axis and yields no real roots. Brent instead fits $x$ sideways as a *Lagrange quadratic polynomial of $y$* ($x = P(y)$) through $(f(a), a)$, $(f(b), b)$, and $(f(c), c)$, and then evaluates that sideways curve at $y = 0$:

$$x_{\text{IQI}} = \frac{a f(b) f(c)}{(f(a)-f(b))(f(a)-f(c))} + \frac{b f(a) f(c)}{(f(b)-f(a))(f(b)-f(c))} + \frac{c f(a) f(b)}{(f(c)-f(a))(f(c)-f(b))}$$

Evaluating a sideways parabola at $y = 0$ always yields a single unique real number $x_{\text{IQI}}$ and converges at order $p \approx 1.839$, nearly doubling the number of significant digits per step.

Rather than accepting every interpolated step unconditionally, the algorithm keeps the root enclosed inside a contracting sign-change bracket $[a, b]$ where $f(a)f(b) \le 0$. Whenever Secant or Inverse Quadratic Interpolation proposes a trial step $s$, five acceptance conditions verify that $s$ falls strictly inside the interior three-quarter window $\left(\frac{3a+b}{4}, b\right)$ and that consecutive steps contract the bracket by at least half every two iterations. If an interpolated step attempts to leave the bracket or stalls on a flat plateau, the algorithm rejects the interpolation and executes a bisection step $m = \frac{1}{2}(a + b)$.

| Root-Finding Algorithm | Convergence Order ($p$) | Derivative $f'(x)$ Required | Bracket Guarantee | Behavior Near Flat Slopes ($f'(x) \approx 0$) |
| :--- | :---: | :---: | :---: | :--- |
| **Bisection** | $1.000$ | No | Yes (Guaranteed) | Steady ($1\text{ bit/step}$), immune to slope traps |
| **Newton-Raphson** | $2.000$ | Yes | No | Catastrophic divergence when $f'(x) \approx 0$ |
| **Secant Chord** | $1.618$ ($\phi$) | No | No | Can fling iterates far outside the search region |
| **Brent's Hybrid Method** | $1.839$ | No | **Yes (Guaranteed)** | **Instant bisection fallback; zero divergence** |

### Where the Unknown Hides: Four Classic Transcendental Equations of Science and Engineering

Fundamental laws across physics and engineering routinely resist closed-form inversion because they couple two distinct physical mechanisms inside the same conservation balance and trap the unknown simultaneously inside two incompatible mathematical operations. In orbital mechanics, Johannes Kepler showed in his 1609 *Astronomia Nova* that as a planet sweeps out equal areas in equal times along an ellipse of eccentricity $e$, its uniform clock angle $M = \frac{2\pi t}{T}$ (*mean anomaly*) and its geometric position angle $E$ (*eccentric anomaly*) satisfy $E - e\sin E - M = 0$. Because the unknown angle $E$ appears simultaneously as a linear algebraic arc outside the sine function and as a trigonometric phase inside $\sin E$, Kepler observed that the equation *"cannot be solved a priori, on account of the different nature of the arc and the sine."*

A similar implicit coupling governs turbulent pipe flow. When water or rocket propellant flows through a rough pipe of diameter $D$ at high Reynolds number $\text{Re}$, a viscous sublayer of thickness $\delta_v \propto D/(\text{Re}\sqrt{f})$ cushions the pipe wall. Because the thickness of that sublayer depends on the Darcy–Weisbach friction factor $f$ itself, Cyril Colebrook (1939) {{cite:colebrook1939}} showed that $\sqrt{f}$ appears both outside and inside a base-$10$ logarithm, which hydraulic engineers historically estimated from the logarithmic curves of the *Moody Chart*:

$$\frac{1}{\sqrt{f}} = -2.0 \log_{10} \left( \frac{\varepsilon / D}{3.7} + \frac{2.51}{\text{Re}\sqrt{f}} \right)$$

In quantum radiation and semiconductor physics, exponential and linear terms couple in the same way. When Max Planck (1900) derived the blackbody spectrum $I(\lambda) \propto \lambda^{-5}/(e^{hc/\lambda k_B T} - 1)$, locating the Wien peak wavelength $\lambda_{\max}$ by setting the derivative to zero coupled the dimensionless photon energy $x = hc/(\lambda_{\max} k_B T)$ inside the exponential $e^x$ and in the algebraic factor $(5 - x)$ outside it, $(5 - x)e^x = 5$ (or $5(1 - e^{-x}) - x = 0$), whose root $x^* = 4.9651142317$ sets the Wien displacement constant of stellar spectra. Likewise, when a DC voltage source $V_s$ drives a semiconductor junction diode through a series load resistor $R$, Kirchhoff's voltage law $(V_s - V)/R = I_s(e^{V/V_T} - 1)$ balances a linear resistor voltage drop against William Shockley's exponential diode current and traps the junction voltage $V$ both linearly and exponentially.

Even when a physical balance remains purely algebraic, three-dimensional geometry and conservation laws routinely produce cubic polynomials whose roots carry direct physical meaning. By Archimedes' buoyancy law, a sphere of radius $R$ and density $\rho_s$ sinks in water of density $\rho_w$ until its submerged cap volume $\frac{1}{3}\pi h^2(3R - h)$ balances $\frac{\rho_s}{\rho_w}(\frac{4}{3}\pi R^3)$, which forms the cubic $h^3 - 3Rh^2 + 4(\rho_s/\rho_w)R^3 = 0$ whose middle root (`{{key:RCL}} 3` in `{{key:POLY}}`) is the physical waterline draft $h \in [0, 2R]$. In continuum mechanics and thermodynamics, twisting a brittle rod fractures it along a $45^\circ$ helix governed by the three real eigenvalues of the Cauchy stress cubic $\lambda^3 - I_1\lambda^2 + I_2\lambda - I_3 = 0$, while compressing a real gas near its critical point follows Johannes Diderik van der Waals's cubic equation of state $\left(P + \frac{a}{V^2}\right)(V - b) = RT$.

### Multiple-Root Conditioning and Polynomial Deflation Order

James H. Wilkinson, Alan Turing's colleague on the Pilot ACE computer and the founder of modern backward error analysis, established the conditioning contrast between simple crossings and repeated roots. At a *simple root* where the curve crosses the axis with non-zero slope ($f'(x^*) \ne 0$), a vertical rounding perturbation of size $\varepsilon_{\text{mach}} \approx 10^{-16}$ in evaluating $f(x)$ shifts the horizontal zero crossing by at most $\Delta x \approx \frac{\varepsilon_{\text{mach}}}{|f'(x^*)|}$. At an *$m$-fold repeated root* where the curve touches the axis tangentially as $f(x) \approx c(x - x^*)^m$, solving $|c(x - x^*)^m| \le \varepsilon_{\text{mach}}$ yields *Wilkinson's Root Conditioning Law*:

$$\Delta x \approx \left(\frac{\varepsilon_{\text{mach}}}{|c|}\right)^{1/m}$$

For a double tangent root ($m = 2$, such as $(x - 3)^2 = 0$), the horizontal uncertainty widens to the square root of machine epsilon ($\varepsilon_{\text{mach}}^{1/2} \approx 10^{-8}$), where half the digits of precision are lost to floating-point rounding noise; for a triple root ($m = 3$), precision drops to $\varepsilon_{\text{mach}}^{1/3} \approx 10^{-5}$. Similarly, deflating a high-degree polynomial $P(x)$ to $Q(x) = P(x)/(x - r_1)$ by dividing out its *largest* root $|r_1|$ first contaminates the lower coefficients of $Q(x)$ with rounding errors and perturbs the remaining roots. Deflating roots in *increasing order of magnitude* ($|r_1| \le |r_2| \le \dots$) preserves coefficient accuracy, and solving the derivative $f'(x) = 0$ at an even-multiplicity tangent minimum restores simple-root conditioning.

### Inside the Symbolic Equation Bank (EQN): Pure Functions, Step Editing & Iverson Piecewise Logic

The SC-32's `{{key:EQN}}` workspace (`{{key:↱}}` + `{{key:STO}}`) provides a structured environment for entering, inspecting, and editing symbolic RPN formulas, including *piecewise physical laws* that change behavior across a threshold. Unlike keystroke-programmable calculators that mix arithmetic formulas with destructive memory writes and unconditional `GTO` jumps, the SC-32's 24-slot Equation Bank treats every stored entry (`A` through `Z`, up to $96$ steps per equation) as a *pure, side-effect-free mathematical function*.

Pressing `{{key:EQN}}` opens the Equation Catalog (`NEW`, `1:A`, `2:B`, … on the top softkeys). Tapping `NEW` (`{{key:LFU0}}`) or pressing `{{key:LBL}}` (Left Shift on `+`) prompts `LBL _` and arms the `A–Z` Alpha layer so a single tap assigns the equation's letter (`00 LBL A`). As operations are keyed in, each step is recorded with a line number (`01 RCL X`, `02 x²`, …). When typing a multi-digit constant such as `0.05`, pressing `{{key:ENTER}}` terminates the numeric literal without duplicating the stack, whereas a second tap inserts an explicit `ENTER` step. At any time, `{{key:↑}}` and `{{key:↓}}` (Left Shift on `8` and `7`) step the cursor backward and forward through the numbered instructions: typing any key inserts at the cursor, `{{key:<-}}` deletes the preceding step, and `{{key:RTN}}` (Right Shift on `+`) or `{{key:C}}` saves the equation to non-volatile memory.

Inside an equation, pressing `{{key:RCL}}` followed by a letter (`A`–`Z`, or indirect `(i)`, where storing a slot number $1\dots 89$ in the index pointer `i` via `STO .` lets `RCL x∥y` dereference `(i)` dynamically) reads that variable onto the stack, and `RCL + A` or `RCL × A` performs in-place recall arithmetic. By contrast, `{{key:STO}}` is blocked (`INVALID FOR EQN`) so that when `{{key:XEQ}}`, `{{key:FN=}}`, `{{key:SOLVE}}`, `{{key:∫}}`, or `{{key:PLOT}}` evaluates an equation repeatedly across an interval, it cannot overwrite stored laboratory constants.

In 1919, the Cambridge mathematician William H. Macaulay introduced a compact notation for piecewise structural loads: when a bridge beam carries concentrated point loads or steps in cross-section at stations $a_1, a_2, \dots$, writing a separate differential equation for every span is cumbersome. Macaulay defined the *singularity ramp bracket* $\langle x - a \rangle_+ = \max(0, x - a)$, which equals $0$ to the left of $x = a$ and turns on as $(x - a)$ to the right of $x = a$. Four decades later, Kenneth E. Iverson (1962) generalized Macaulay's switch into the *Iverson Indicator Bracket* $[P] \in \{1, 0\}$, where any relational proposition $P$ evaluates to `1` if True and `0` if False:

$$f(x) = f_1(x)\cdot [x \le c] + f_2(x)\cdot [x > c] \qquad \text{or} \qquad \langle u \rangle_+ = u \cdot [u > 0] = \max(0, u)$$

On the SC-32, the `{{key:x?0}}` menu (Right Shift on `{{key:÷}}`) provides six unary zero comparisons (`x=0`, `x≠0`, `x>0`, `x<0`, `x≥0`, and `x≤0`), each replacing Register $X$ in place with `1.0` for True or `0.0` for False. Its companion `{{key:x?y}}` menu (Left Shift on `÷`) offers the six binary two-register comparisons (`x=y`, `x≠y`, `x>y`, `x<y`, `x≥y`, and `x≤y`), which compare Register $X$ against Register $Y$, drop the stack, and leave `1.0` or `0.0` in Register $X$. Consequently, on any expression $u$ sitting in Register $X$, the three-keystroke *Macaulay ramp idiom* `{{key:ENTER}} {{key:x>0}} {{key:×}}` duplicates $u$ into $Y$, converts $X$ into $[u > 0] \in \{0, 1\}$, and multiplies them to produce $\langle u \rangle_+ = \max(0, u)$. This construction models bilinear contact springs, progressive tax or tariff brackets, Zener clippers, and piecewise fluid drag laws inside a single continuous `EQN` formula.

### Brent's Two-Phase Convergence and Kahan's Stack Residual Audit

When `{{key:SOLVE}}` evaluates an equation $f(x) = 0$ stored in `{{key:EQN}}`, it executes a two-phase bracketing state machine followed by William Kahan's post-convergence stack audit. In the first phase, if two initial guesses placed in Registers $Y$ and $X$ already straddle a sign change ($f(a)\cdot f(b) \le 0$), `{{key:SOLVE}}` adopts the $(Y, X)$ stack registers as the starting bracket $[a, b]$ immediately. When given only a single seed $x_0$ via `{{key:STO}}`, or two guesses on the same side of the axis where $f(a)\cdot f(b) > 0$, an outward search generates a companion probe ($\Delta = 0.1|x_0|$) and advances outward for up to $50$ steps using clamped secant steps, or expanding by the *golden ratio* $\phi \approx 1.618034$ whenever the slope is flat. Along the way, the search retracts any probe that steps outside the domain of $\ln x$ or $\sqrt{x}$, and it detects even-multiplicity tangent roots such as $(x - 2)^2 = 0$ whenever $|b - a| < 10^{-12}$ and $|f(b)| < 10^{-7}$.

In the second phase, once a sign change $f(a)\cdot f(b) \le 0$ is bracketed, the solver attempts *Inverse Quadratic Interpolation* (IQI) whenever three distinct values $(f(a), f(b), f(c))$ are available, or a *Secant Chord* step otherwise. Before accepting the proposed step $s$, Brent's five acceptance tests verify that $s$ lies strictly inside the three-quarter window $\left(\frac{3a+b}{4}, b\right)$ and reduces the step width by at least $50\%$ every two steps; if any check fails, the engine executes a *Bisection* step $m = \frac{1}{2}(a + b)$ until $|f(b)| \le 10^{-13}$ or the half-bracket width reaches machine tolerance $\text{tol} = 2\varepsilon_{\text{mach}}|b| + \frac{1}{2}\cdot 10^{-12}$.

Following William Kahan's diagnostic solver design, the final stack state distinguishes a genuine root from a discontinuous pole. When `{{key:SOLVE}}` finishes on the SC-32, it writes the converged root $x^*$ into the target variable, pushes $x^*$ into Register $X$, lifts the starting guess (or upper bracket bound) into Register $Y$, and preserves the prior stack contents in Registers $Z$ and $T$.

If an initial bracket straddles a *vertical asymptote* (*discontinuous pole*) where the curve jumps from $-\infty$ to $+\infty$, such as $f(x) = \tan x$ across $x = \pi/2$ or $f(x) = \frac{1}{x - 2}$ across $x = 2$, the opposite signs $f(a)\cdot f(b) < 0$ on either side of the discontinuity cause bisection to contract around the pole $x = 2.0000000000$. Because `SOLVE` has already stored $x^*$ in the equation's variable, pressing `{{key:XEQ}}` followed by the equation's letter evaluates the residual $f(x^*)$ in Register $X$: at a *true root*, it returns $f(x^*) \approx 0$ ($|f(x^*)| \le 10^{-12}$), whereas at a *false pole*, it reveals a large residual ($|f(x^*)| \gg 1$, or `DIVIDE BY 0`).

---

## Horner Evaluation, Cardano's Cubic Solver & Brent's Root-Finder

On the SC-32 stack, root-finding separates polynomial problems of degree two or three from higher-degree and transcendental conservation laws.

When the governing relation is a quadratic ($ax^2 + bx + c = 0$) or cubic ($Ax^3 + Bx^2 + Cx + D = 0$) with explicit numerical coefficients, the `{{key:POLY}}` workspace (above `{{key:XEQ}}`) bypasses symbolic equation entry altogether. Loading the coefficients from highest degree down onto the softkeys (`A {{key:A}} B {{key:B}} C {{key:C}} D {{key:D}}`) pushes all four coefficients onto Registers $(T, Z, Y, X)$, and pressing `{{key:EXEC}}` dispatches directly to the Citardauq quadratic or Cardano–Viète cubic formulas; the solver returns the primary root in $(Y = \text{Real},\; X = \text{Imag})$ and populates root registers `1` through `6` (indirect `R34`–`R39`).

When Abel and Galois's degree barrier or a transcendental coupling of algebraic, trigonometric, and exponential terms rules out closed-form extraction, the problem moves to `{{key:EQN}}` (`{{key:↱}}` + `{{key:STO}}`) and Brent's `{{key:SOLVE}}` engine (above `{{key:7}}`). Defining the residual $f(X) = \text{LHS} - \text{RHS} = 0$ in `{{key:EQN}}`, staging a two-guess bracket $[a, b]$ across Registers $Y$ and $X$ (or storing a single seed via `{{key:STO}}`), and invoking `{{key:SOLVE}}` places the converged root $x^*$ in Register $X$ with its bracket companion in Register $Y$, ready for an immediate `{{key:XEQ}}` residual check.

{{res:sc32_cubic_roots:screenshot|Cubic polynomial x^3 - 6x^2 + 11x - 6 = 0 solved via POLY}}

### Horner's Nested Evaluation, T-Register Flooding & Biquadratic Reductions

For the fourth-degree polynomial $P(x) = 4x^4 - 3x^3 + 2x^2 - 5x + 7 = (((4x - 3)x + 2)x - 5)x + 7$ evaluated at $x_0 = 2.5$, where synthetic division yields $P(x) = (x - 2.5)(4x^3 + 7x^2 + 19.5x + 43.75) + 116.3750$, the four-register stack supports two execution patterns depending on whether $x_0 = 2.5$ is keyed at each stage or dispensed from Register $T$:

1. **Running Accumulator in Register $X$ (Using Only Registers $X$ and $Y$):** When $x = 2.5$ is short to key in, the Ruffini-Horner synthetic-division coefficients accumulate sequentially in Register $X$ while Registers $Z$ and $T$ remain at zero:
   * **First Horner Stage ($b_3$):** Multiplying the leading coefficient by $x$ ($4 \times 2.5 = 10.0000$) and subtracting $3$ forms the first synthetic-division quotient coefficient $b_3 = 4(2.5) - 3 = \mathbf{7.0000}$ in Register $X$.
   * **Second Horner Stage ($b_2$):** Multiplying by $2.5$ (which lifts $7.0000$ transiently into Register $Y$ and forms $17.5000$) and adding $2$ produces the second quotient coefficient $b_2 = 7.0(2.5) + 2 = \mathbf{19.5000}$ in Register $X$.
   * **Third Horner Stage ($b_1$):** Multiplying by $2.5$ and subtracting $5$ yields the linear quotient coefficient $b_1 = 19.5(2.5) - 5 = \mathbf{43.7500}$ in Register $X$.
   * **Final Remainder ($b_0 = P(2.5)$):** One final multiply-and-add step ($43.75 \times 2.5 + 7$) via `{{res:sc32_07_polynomials_brent_solver_seq_01:keys}}` completes the polynomial remainder $P(2.5) =$ `{{res:sc32_07_polynomials_brent_solver_seq_01:value}}` ($\mathbf{116.3750}$).
2. **Flooding All Four Stack Registers (`2.5 ENTER ENTER ENTER`):** Rather than keying `2.5` four separate times—or re-typing a nine-digit evaluation point such as $x = 2.718281828$—filling all four registers $(T, Z, Y, X)$ with $x$ via `2.5 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}` turns Register $T$ into an automatic constant dispenser. Every time `{{key:×}}` consumes the copy of $x$ in Register $Y$ and drops the stack, Register $T$ clones a fresh copy of $x = 2.5$ downward into Register $Z$. Starting with `4 × 3 -` ($\to 7.0000$ in $X$, with $2.5$ waiting in $Y, Z, T$) and streaming `× 2 + × 5 - × 7 +` reaches $\mathbf{116.3750}$ without re-typing `2.5`.

Applying that same T-register replication to Martin Green's rational-logarithmic solar-cell fill factor $FF = \frac{v_{\text{oc}} - \ln(v_{\text{oc}} + 0.72)}{v_{\text{oc}} + 1}$ at $v_{\text{oc}} = 25.145$ requires keying `25.145` only once: after flooding the stack with three taps of `{{key:ENTER}}`, adding $0.72$, taking `{{key:LN}}`, and subtracting from the waiting copy of $v_{\text{oc}}$ in Register $Y$ forms the numerator $21.8921$ in Register $X$, while a fresh copy of $v_{\text{oc}}$ drops into Register $Y$ ready for `{{key:x⇄y}}`, $+ 1$, and `{{key:÷}}` to resolve $FF = \mathbf{0.837334}$.

Similarly, on the coupled-oscillator biquadratic $x^4 - 10x^2 + 9 = 0$ ($u = x^2$), evaluating the quadratic radical $\sqrt{\Delta} = \sqrt{10^2 - 4(9)} = 8.0000$ on the stack and pairing it with $10$ via `{{key:LASTX}}` forms $10 \pm 8 = \{18.0000, 2.0000\}$ across Registers $Y$ and $X$; halving both roots ($u_1 = 9, u_2 = 1$) and taking `{{key:√x}}` leaves both positive normal-mode frequencies side by side on the stack ($Y = \mathbf{1.0000},\; X = \mathbf{3.0000}$).

---

### Cardano's Analytical Cubic & Quadratic Solver

Inside `{{key:POLY}}` (Right Shift `{{key:↱}}` above `{{key:XEQ}}`), the softkeys and variable registers map the coefficients and extracted roots of $Ax^3 + Bx^2 + Cx + D = 0$ as follows:

| Interface Element | Display Legend / Key Assignment | Functional Action / Internal Allocation |
| :--- | :--- | :--- |
| **Menu Prompt** | `Ax^3 + Bx^2 + Cx + D = 0` | Prompts for polynomial coefficient entry |
| **LFU Softkeys** | `{{key:A}} {{key:B}} {{key:C}} {{key:D}} {{key:EXEC}} {{key:CLR}}` | Softkey assignments for coefficient entry and execution |
| **Internal Storage: Root 1** | Variables `"1"` (Real), `"2"` (Imaginary) | Stores first calculated root (also placed in Registers $Y$ and $X$) |
| **Internal Storage: Root 2** | Variables `"3"` (Real), `"4"` (Imaginary) | Stores second calculated root |
| **Internal Storage: Root 3** | Variables `"5"` (Real), `"6"` (Imaginary) | Stores third calculated root |

Any unentered coefficient defaults to $0.0$ (at least one of $A$ or $B$ must be non-zero, otherwise `{{key:EXEC}}` displays `A ≠ 0`). Evaluating representative cubics and quadratics shows how `{{key:POLY}}` dispatches across the three discriminant regimes ($\Delta < 0$, $\Delta > 0$, and $\Delta = 0$).

On the *casus irreducibilis* benchmark $(x - 1)(x - 2)(x - 3) = x^3 - 6x^2 + 11x - 6 = 0$ ($\Delta < 0$), `{{key:POLY}}` executes Viète's trigonometric cosine trisection.

Inside `{{key:POLY}}`, loading the four coefficients $A = 1$, $B = -6$, $C = 11$, and $D = -6$ onto their top-row softkeys and pressing `{{key:EXEC}}` projects the three unit-circle vertices onto the real axis:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Coefficient $A = 1.0$ |
| `6 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-6.0000$ | Coefficient $B = -6.0$ |
| `11 {{key:C}}` | $0.0000$ | $1.0000$ | $-6.0000$ | $11.0000$ | Coefficient $C = 11.0$ |
| `6 {{key:+/-}} {{key:D}}` | $1.0000$ | $-6.0000$ | $11.0000$ | $-6.0000$ | Coefficient $D = -6.0$ |
| `{{key:EXEC}}` | $1.0000$ | $-6.0000$ | **$1.000000$** | **$0.000000$** | Primary root $r_1 = 1.0 + 0.0i$ in $(Y, X)$; roots $1, 2, 3$ in vars `1`–`6` |

Here `{{key:EXEC}}` sorts all three real roots in ascending order ($r_1 = 1.0$ in variables `1, 2`, $r_2 = 2.0$ in variables `3, 4`, and $r_3 = 3.0$ in variables `5, 6`), while placing the real part of $r_1$ in Register $Y$ and its zero imaginary part in Register $X$.

In the positive-discriminant regime ($\Delta > 0$), a cubic with complex conjugate roots such as $x^3 - x^2 + x - 1 = (x - 1)(x^2 + 1) = 0$ crosses the horizontal axis only once at $r_1 = 1.0$, pairing that real intercept with the pure imaginary roots $r_{2,3} = 0.0 \pm 1.0i$. Loading its four alternating coefficients inside `{{key:POLY}}` separates the real crossing on the stack from the complex conjugate pair stored in the numbered registers:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Coefficient $A = 1.0$ |
| `1 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-1.0000$ | Coefficient $B = -1.0$ |
| `1 {{key:C}}` | $0.0000$ | $1.0000$ | $-1.0000$ | $1.0000$ | Coefficient $C = 1.0$ |
| `1 {{key:+/-}} {{key:D}}` | $1.0000$ | $-1.0000$ | $1.0000$ | $-1.0000$ | Coefficient $D = -1.0$ |
| `{{key:EXEC}}` | $1.0000$ | $-1.0000$ | **$1.000000$** | **$0.000000$** | Real $r_1=1$ in $Y$, Imag $r_1=0$ in $X$; conjugate pair $\pm i$ in vars `3`–`6` |

Recalling `{{key:RCL}} 3` and `{{key:RCL}} 4` returns the real and imaginary parts $0.0000$ and $+1.0000$ of $r_2 = +i$, while `{{key:RCL}} 5` and `{{key:RCL}} 6` return $0.0000$ and $-1.0000$ for its conjugate $r_3 = -i$.

At the critical-damping boundary $\Delta = 0$—represented by the third-order RLC filter polynomial $s^3 + 12s^2 + 45s + 50 = (s+2)(s+5)^2 = 0$—the solver stores both copies of the double pole ($-5.0, -5.0$) and the simple pole ($-2.0$) across variables `1`, `3`, and `5`, while placing the first sorted real root in $(Y = -5.000000,\; X = 0.000000)$ (`{{res:sc32_07_polynomials_brent_solver_seq_10:keys}}` $\longrightarrow$ `{{res:sc32_07_polynomials_brent_solver_seq_10:value}}`).

For the 3D Cauchy principal stress cubic ($\lambda^3 - 70\lambda^2 + 1175\lambda - 5750 = 0$) of a structural steel element with tensor invariants $I_1 = 70\text{ MPa}$, $I_2 = 1175\text{ MPa}^2$, and $I_3 = 5750\text{ MPa}^3$, the symmetry of Cauchy's stress tensor guarantees $\Delta \le 0$ so all three eigenvalues $\sigma_3 \le \sigma_2 \le \sigma_1$ are real. Loading those invariants into `{{key:POLY}}` with `{{res:sc32_07_polynomials_brent_solver_seq_12:keys}}` isolates the major principal stress `{{res:sc32_07_polynomials_brent_solver_seq_12:value}}` $\text{MPa}$ in Variable `5`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:A}} 70 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-70.0000$ | Coefficients $A, B = -I_1$ |
| `1175 {{key:C}} 5750 {{key:+/-}} {{key:D}}` | $1.0000$ | $-70.0000$ | $1175.0000$ | $-5750.0000$ | Coefficients $C = I_2, D = -I_3$ |
| `{{key:EXEC}}` | $1.0000$ | $-70.0000$ | **$10.000000$** | **$0.000000$** | Minor stress $\sigma_3 = 10.0$ in $Y$; $\sigma_2, \sigma_1$ in vars `3`, `5` |
| `{{key:RCL}} 5` | $-70.0000$ | $10.0000$ | $0.0000$ | **$48.027756$** | Recall major principal stress $\sigma_1$ into Register $X$ |

Once $\sigma_1 = 48.0278\text{ MPa}$ sits in Register $X$ and $\sigma_3 = 10.0000\text{ MPa}$ sits in Register $Z$, keying `{{key:R↓}} {{key:x⇄y}} {{key:-}} 2 {{key:÷}}` yields Henri Tresca's *maximum shear stress* $\tau_{\max} = \frac{1}{2}(\sigma_1 - \sigma_3) = \mathbf{19.0139\text{ MPa}}$.

Applying Archimedes' floating-sphere buoyancy cubic $h^3 - 3Rh^2 + 4(\rho_s/\rho_w)R^3 = 0$ to a solid oak marine buoy of radius $R = 0.50\text{ m}$ ($1.00\text{ m}$ diameter) and specific gravity $\rho_s/\rho_w = 0.65$ produces $h^3 - 1.5h^2 + 0.325 = 0$. Inside `{{key:POLY}}`, the sequence `{{res:sc32_07_polynomials_brent_solver_seq_13:keys}}` isolates the physical waterline draft `{{res:sc32_07_polynomials_brent_solver_seq_13:value}}` $\text{m}$ in Variable `3`, which shows that $60.14\%$ of the buoy's diameter sits submerged while the algebraic companion roots $-0.4123\text{ m}$ and $1.3109\text{ m}$ lie outside the physical sphere $[0, 1.00\text{ m}]$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:A}} 1.5 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-1.5000$ | Load cubic and quadratic coefficients $A = 1.0,\; B = -1.5$ |
| `0 {{key:C}} 0.325 {{key:D}}` | $1.0000$ | $-1.5000$ | $0.0000$ | $0.3250$ | Load linear and constant coefficients $C = 0.0,\; D = 0.325$ |
| `{{key:EXEC}}` | $1.0000$ | $-1.5000$ | $-0.412257$ | $0.0000$ | Solve cubic; real parts of 3 roots stored in Variables `1`, `3`, `5` |
| `{{key:RCL}} 3` | $-1.5000$ | $-0.412257$ | $0.0000$ | **$0.601390$** | Recall physical immersion depth $h \in [0, 2R]$ from Variable `3` |

Evaluating the inverse ballistic trajectory quadratic ($360.3673 u^2 - 1200u + 510.3673 = 0$) for an elevated target at horizontal range $x = 1,200\text{ m}$ and height $y = 150\text{ m}$ with muzzle speed $v_0 = 140\text{ m/s}$ ($\frac{gx^2}{2v_0^2} = 360.3673\text{ m}$) illustrates two ways to enter a quadratic $a u^2 + b u + c = 0$ inside `{{key:POLY}}`. Setting the cubic coefficient $A = 0$ (`0 {{key:A}}`) and loading $(B = a,\; C = b,\; D = c)$ solves $Bx^2 + Cx + D = 0$ directly, whereas mapping the coefficients into $(A = a,\; B = b,\; C = c,\; D = 0)$ solves $u(a u^2 + b u + c) = 0$; this layout places a dummy root at $u = 0$ in Variable `1` and stores the two quadratic roots in Variables `3` and `5`. With the $D = 0$ layout, `{{res:sc32_07_polynomials_brent_solver_seq_02:keys}}` recovers the low direct-fire angle `{{res:sc32_07_polynomials_brent_solver_seq_02:value}}`$^\circ$ before `{{key:RCL}} 5 {{key:ATAN}}` reveals the high mortar arc:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `360.3673 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $360.3673$ | Quadratic coefficient $A$ |
| `1200 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $360.3673$ | $-1200.0000$ | Quadratic coefficient $B$ |
| `510.3673 {{key:C}}` | $0.0000$ | $360.3673$ | $-1200.0000$ | $510.3673$ | Quadratic coefficient $C$ |
| `0 {{key:D}}` | $360.3673$ | $-1200.0000$ | $510.3673$ | $0.0000$ | Depressed constant ($D$ defaults to $0.0$ if omitted) |
| `{{key:EXEC}}` | $360.3673$ | $-1200.0000$ | $0.0000$ | $0.0000$ | Solve polynomial; real roots $(0, u_1, u_2)$ stored in Variables `1`, `3`, `5` |
| `{{key:RCL}} 3 {{key:ATAN}}` | $-1200.0000$ | $0.0000$ | $0.0000$ | **$26.590116$** | Low direct-fire trajectory $\theta_1$ in degrees |
| `{{key:RCL}} 5 {{key:ATAN}}` | $0.0000$ | $0.0000$ | $26.590116$ | **$70.532306$** | High plunging mortar arc $\theta_2$ in degrees |

Similarly, on the forensic highway braking quadratic $v_0^2 + 20.594\,v_0 - 1166.99 = 0$ ($t_r = 1.5\text{ s},\; \mu = 0.70,\; d = 85.0\text{ m}$), keying `1 {{key:A}} 20.594 {{key:B}} 1166.99 {{key:+/-}} {{key:C}} 0 {{key:D}} {{key:EXEC}} {{key:RCL}} 5` inside `{{key:POLY}}` extracts the positive initial vehicle speed $v_0 = \mathbf{25.301\text{ m/s}}$ ($91.1\text{ km/h}$).

---

### Hunting Transcendental Roots & Auditing Kahan's Stack with Brent's SOLVE

Comparing `{{key:SOLVE}}` and `{{key:POLY}}` side by side on two physical cubics shows how the symbolic equation solver complements closed-form extraction—noting that inside `{{key:EQN}}`, recalling a variable letter automatically lifts the stack, whereas two consecutive numeric literals require `{{key:ENTER}}` between them so their digits do not concatenate.

On John Wallis and Isaac Newton's 1669 cubic benchmark ($x^3 - 2x - 5 = 0$), hand-evaluating Cardano's formula is cumbersome because $p = -2$ and $q = -5$ yield a positive discriminant $\Delta = (-5/2)^2 + (-2/3)^3 = \frac{643}{108} > 0$, requiring the sum of two nested cube roots $\sqrt[3]{\frac{5}{2} + \sqrt{\frac{643}{108}}} + \sqrt[3]{\frac{5}{2} - \sqrt{\frac{643}{108}}}$. In `{{key:EQN}}`, the residual $f(x) = (x^2 - 2)x - 5$ enters directly in Horner nested form as `X x² 2 - X × 5 -`.

Because $f(2) = -1 < 0$ and $f(3) = +16 > 0$, either staging the two-guess bracket $[2, 3]$ on $(Y, X)$ via `2 {{key:ENTER}} 3 {{key:SOLVE}} X` or storing Newton's single seed `2 {{key:STO}} X` and pressing `SOLVE X` converges to $x^* = \mathbf{2.0945514815}$ in Register $X$ while lifting the starting seed $2.0000$ into Register $Y$ (with $Z = 0.0000$ and `{{key:XEQ}}` confirming a machine-zero residual $|f(x^*)| < 10^{-15}$).

Similarly, applying van der Waals's real-gas equation of state $\left(P + \frac{a}{V^2}\right)(V - b) = RT$ to carbon dioxide ($\text{CO}_2$, $a = 3.59\text{ L}^2\cdot\text{atm/mol}^2$, $b = 0.0427\text{ L/mol}$) compressed to $P = 50\text{ atm}$ at $T = 300\text{ K}$ ($RT = 24.618\text{ L}\cdot\text{atm/mol}$) clears the $V^2$ denominator to form the expanded cubic $50V^3 - 26.753V^2 + 3.59V - 0.153293 = 0$. Inside `{{key:POLY}}`, loading those four coefficients (`{{res:sc32_07_polynomials_brent_solver_seq_09:keys}}`) finds the real molar volume `{{res:sc32_07_polynomials_brent_solver_seq_09:value}}` $\text{L/mol}$—$27\%$ denser than the ideal-gas estimate $V_{\text{ideal}} = RT/P = 0.4924\text{ L/mol}$ and matching the $V_m = \mathbf{0.358736\text{ L/mol}}$ obtained by entering `(50 + 3.59/V^2)(V - 0.0427) - 24.618` into `{{key:EQN}}` and running `0.49 {{key:STO}} V {{key:SOLVE}} V`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `50 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $50.0000$ | Coefficient $A = 50.0$ |
| `26.753 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $50.0000$ | $-26.7530$ | Coefficient $B = -26.753$ |
| `3.59 {{key:C}}` | $0.0000$ | $50.0000$ | $-26.7530$ | $3.5900$ | Coefficient $C = 3.59$ |
| `0.153293 {{key:+/-}} {{key:D}}` | $50.0000$ | $-26.7530$ | $3.5900$ | $-0.153293$ | Coefficient $D = -0.153293$ |
| `{{key:EXEC}}` | $50.0000$ | $-26.7530$ | **$0.358736$** | **$0.000000$** | Real root in $Y$, Imag in $X$ |
| `{{key:x⇄y}}` | $50.0000$ | $-26.7530$ | $0.000000$ | **$0.358736$** | Molar volume $V_m$ in Register $X$ |

On coupled transcendental conservation laws, Brent's `{{key:SOLVE}}` engine resolves the unknowns directly from their `{{key:EQN}}` residuals, returning the converged root $x^*$ in Register $X$, lifting the starting seed or bracket bound into Register $Y$, and preserving Registers $Z$ and $T$ for an immediate `{{key:XEQ}}` residual check ($|f(x^*)| \le 10^{-12}$):

* **Cyril Colebrook's Turbulent Pipe Friction Equation:** Evaluating the Colebrook–White turbulent pipe equation in commercial steel piping at Reynolds number $\text{Re} = 100,000$ and relative roughness $\varepsilon/D = 0.001$ brings both terms of the implicit balance onto one side of the equals sign:
  $$g(f) = \frac{1}{\sqrt{f}} + 2.0\log_{10}\!\left(\frac{\varepsilon/D}{3.7} + \frac{2.51}{\text{Re}\sqrt{f}}\right) = 0$$
  Store `F √x 1/x  0.001 ENTER 3.7 ÷  2.51 ENTER 100000 ÷ F √x ÷ + LOG 2 × +` in `{{key:EQN}}`. Because $1/\sqrt{f}$ diverges as $f \to 0^+$ and $\sqrt{f}$ is undefined for $f < 0$, seed `F` inside the physical Moody turbulent regime $[0.008, 0.08]$ (or bracket `0.01 {{key:ENTER}} 0.05` on $Y, X$). Keying `0.02 {{key:STO}} F {{key:SOLVE}} F` lifts $0.0200$ into Register $Y$ and converges to $f^* = \mathbf{0.022204}$ in Register $X$.
* **Johannes Kepler's Elliptical Orbital Anomaly ($E - e\sin E = M$):** Applying Kepler's equation $E - e\sin E - M = 0$ to an Earth-observation satellite with orbital eccentricity $e = 0.25$ at mean anomaly $M = 1.20\text{ rad}$ in `{{key:RAD}}` mode yields $f(E) = E - 0.25\sin E - 1.20 = 0$. Since $|\sin E| \le 1$, the physical root is guaranteed to lie inside $[M - e,\; M + e] = [0.95,\; 1.45]\text{ rad}$; storing `E  0.25 ENTER E SIN × - 1.20 -` in `{{key:EQN}}` and seeding the mean anomaly via `1.20 {{key:STO}} E {{key:SOLVE}} E` converges to $E^* = \mathbf{1.488665\text{ rad}}$ ($85.294^\circ$) in five iterations.
* **William Shockley's Silicon Diode Load Line:** For the DC diode load-line circuit ($V_s = 5.0\text{ V}$, saturation current $I_s = 10^{-12}\text{ A}$, thermal voltage $V_T = 0.02585\text{ V}$, and series load resistor $R = 1\text{ k}\Omega$ giving $I_s R = 10^{-9}\text{ V}$), Kirchhoff's loop residual is:
  $$f(V) = 5.0 - 10^{-9}\left(e^{V/0.02585} - 1\right) - V = 0$$
  Whereas an unguarded Newton iteration from $V_0 = 0\text{ V}$ shoots along the flat diode tangent to $V_1 = +5.0\text{ V}$ ($e^{5.0 / 0.02585} \approx 10^{84}$), Brent's bracket watchdogs keep the iterate inside the physical voltage drop. Storing `5  V 0.02585 ÷ eˣ 1 - 1E-9 × -  V -` in `{{key:EQN}}` and seeding near the silicon turn-on knee via `0.65 {{key:STO}} V {{key:SOLVE}} V` (or bracketing `[0.5, 0.8]` on $Y, X$) yields $V_D^* = \mathbf{0.672944\text{ V}}$ (loop current $I_D = 4.3271\text{ mA}$).
* **Open-Channel Froude Critical Depth:** When $Q = 20.0\text{ m}^3/\text{s}$ ($Q^2 = 400$) of floodwater rushes through a trapezoidal concrete spillway of bottom width $b = 3.0\text{ m}$ and side slopes $z = 2.0$, the critical depth $y_c$ where the surface wave speed matches the flow velocity ($\text{Fr} = 1$) satisfies $f(y) = Q^2 T(y) - g A(y)^3 = 400(3 + 4y) - 9.81(3y + 2y^2)^3 = 0$—a sixth-degree polynomial that lies beyond Abel and Galois's degree-4 radical limit and beyond degree-3 `{{key:POLY}}`. Recording the factored balance `3 ENTER 4 ENTER Y × + 400 ×  3 ENTER Y ×  Y x² 2 × + 3 yˣ 9.81 × -` directly in `{{key:EQN}}` and keying `1.0 {{key:STO}} Y {{key:SOLVE}} Y` converges to $y_c^* = \mathbf{1.258641\text{ m}}$.
* **Selecting Physical Branches in Multi-Root Equations (Nuclear Buckling & De Laval Nozzles):** Whenever a transcendental equation possesses multiple roots across separate physical regimes, your starting seed or $(Y, X)$ bracket determines which branch `{{key:SOLVE}}` locks onto:
  * **Nuclear Critical Buckling Radius:** For a spherical fission reactor core whose radial neutron flux vanishes at $\sin(0.045 R) = 0$ in `{{key:RAD}}` mode, storing `R 0.045 × SIN` in `{{key:EQN}}` and seeding `60 {{key:STO}} R {{key:SOLVE}} R` isolates the fundamental buckling mode $0.045 R = \pi$ at $R_{\text{crit}} = \mathbf{69.813170\text{ cm}}$ (avoiding the trivial origin $R = 0$).
  * **Aurel Stodola's De Laval Rocket Nozzle:** The area-Mach relation $\frac{1}{M}\left(\frac{1 + 0.2M^2}{1.2}\right)^3 - 2.50 = 0$ for area ratio $A/A^* = 2.50$ and $\gamma = 1.4$—entered in `{{key:EQN}}` as `M x² 0.2 × 1 + 1.2 ÷ 3 yˣ M ÷ 2.50 -`—has two positive roots separated by the sonic throat $M = 1$. Seeding above the throat via `2.5 {{key:STO}} M {{key:SOLVE}} M` (or bracketing `1.1 ENTER 4.0` on $Y, X$) converges to the supersonic rocket exhaust branch $M_{\text{sup}} = \mathbf{2.442804}$, while seeding below the throat via `0.2 {{key:STO}} M {{key:SOLVE}} M` (or bracketing `0.05 ENTER 0.95`) isolates the subsonic diffuser branch $M_{\text{sub}} = \mathbf{0.239541}$.

### Editing & Solving a Piecewise Equation in EQN Mode (`x?0` & `x?y`)

Applying the Macaulay singularity ramp idiom (`{{key:ENTER}} {{key:x>0}} {{key:×}}`) to a spacecraft payload isolation mount—where a primary coil spring of stiffness $k_1 = 2,000\text{ N/m}$ carries the load up to a clearance gap $x_0 = 0.05\text{ m}$ ($50\text{ mm}$) before a secondary elastomer bump-stop of stiffness $k_2 = 8,000\text{ N/m}$ engages—models the bilinear force law inside a single continuous equation:

$$F(x) = 2000x + 8000\langle x - 0.05 \rangle_+ = 2000x + 8000(x - 0.05)\cdot[x - 0.05 > 0]$$

To find the deflection $x^*$ under a static payload of $F_{\text{target}} = 350\text{ N}$, press `{{key:EQN}}` (Right Shift `{{key:↱}}` above `{{key:STO}}`), tap `NEW` (`{{key:LFU0}}`), press `A` for `00 LBL A`, and enter the residual $F(x) - 350$ using `{{key:x>0}}` from `{{key:x?0}}` (Right Shift `{{key:↱}}` above `{{key:÷}}`):

`{{key:RCL}} X  2000 {{key:×}}  {{key:RCL}} X  0.05 {{key:-}}  {{key:ENTER}} {{key:x>0}} {{key:×}}  8000 {{key:×}}  {{key:+}}  350 {{key:-}}  {{key:RTN}}`

Below the gap at $x = 0.03\text{ m}$, the indicator $[x - 0.05 > 0]$ evaluates to $0$ so $F(0.03) = 60\text{ N}$. Above the gap at $x^* = \mathbf{0.0750\text{ m}}$—the root returned by `0.02 {{key:ENTER}} 0.10 {{key:SOLVE}} X`—the indicator flips to $1$ and the bump-stop adds $200\text{ N}$ to reach $F(0.075) = 350\text{ N}$:

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

After `{{key:SOLVE}}` terminates, the four-register stack preserves both the root estimate and the diagnostic context for William Kahan's residual check:

| Stack / Action | Post-`{{key:SOLVE}}` Contents | Engineering Diagnostic Interpretation |
| :---: | :--- | :--- |
| **Register $X$** | **Converged Root Estimate ($x^*$)** | The final root estimate where $f(x^*)$ crosses or touches zero, also written into the target variable (`A`–`Z`). |
| **Register $Y$** | **Starting Seed or Upper Bracket Bound** | Lifted from Register $X$ when `{{key:SOLVE}}` pushes the converged root $x^*$ onto the stack. |
| **Registers $Z, T$** | **Prior Stack Context (Preserved)** | Any values previously in Registers $Y$ and $Z$ lift into $Z$ and $T$ undisturbed. |
| **`{{key:XEQ}}` Residual Audit** | **Evaluated Function Residual ($f(x^*)$)** | Because $x^*$ is already stored in your equation's target variable, pressing `{{key:XEQ}}` evaluates $f(x^*)$: a true root yields $\lvert f(x^*) \rvert \le 10^{-12}$, whereas an accidental vertical asymptote/pole exposes itself with $\lvert f(x^*) \rvert \gg 1$. |

### Practical Root-Finding Strategy: Bracket Seeding, Multiple Roots & Deflation on the Stack

Four stack techniques reinforce `{{key:POLY}}` and `{{key:SOLVE}}` when auditing nonlinear equations:

1. **Verifying `{{key:POLY}}` Roots via Viète's Sum-and-Product Checksums:**
   Whenever `{{key:POLY}}` writes the three roots of $Ax^3 + Bx^2 + Cx + D = 0$ into variables `1` (Real 1), `3` (Real 2), and `5` (Real 3), Viète's trace and determinant relations verify the roots in six keystrokes:
   * Keying `{{key:RCL}} 1 {{key:RCL}} 3 {{key:+}} {{key:RCL}} 5 {{key:+}}` must equal $-B/A$ (for the Cauchy stress cubic $\lambda^3 - 70\lambda^2 + 1175\lambda - 5750 = 0$, $10.0 + 11.972244 + 48.027756 = \mathbf{70.000000}$).
   * Keying `{{key:RCL}} 1 {{key:RCL}} 3 {{key:×}} {{key:RCL}} 5 {{key:×}}` must equal $-D/A$ ($10.0 \times 11.972244 \times 48.027756 = \mathbf{5750.0000}$).
   * When a cubic has complex conjugate roots $r_{2,3} = \alpha \pm i\beta$ stored in variables `3, 4` and `5, 6`, keying `{{key:RCL}} 4 {{key:RCL}} 3 {{key:▸θ,r}}` (Left Shift `{{key:↰}}` above `{{key:4}}`) converts $(\text{Re}, \text{Im})$ into the polar modulus $|r_2| = \sqrt{\alpha^2 + \beta^2}$ in Register $X$ and phase angle $\theta$ in Register $Y$.
2. **Isolating Specific Branches of Multi-Root Transcendental Equations:**
   Whenever an equation has multiple roots across distinct physical regimes—such as low direct-fire vs. high mortar trajectories, subsonic vs. supersonic Mach branches across the $M^* = 1$ nozzle throat, or subcritical vs. supercritical conjugate depths in open-channel hydraulics—place two bracket bounds $(a, b)$ in Registers $Y$ and $X$ that straddle only the desired branch (for example, `0.05 {{key:ENTER}} 0.95` for the subsonic nozzle branch, or `1.05 {{key:ENTER}} 4.0` for the supersonic branch) so Brent's solver remains locked inside that interval from iteration zero.
3. **Deflating Known Roots to Hunt Additional Roots ($(x - r_1)$ Division):**
   Once a first root $r_1$ of a transcendental or high-degree equation $f(x) = 0$ is isolated and stored in Variable `A` (deflating in increasing order of magnitude $|r_1| \le |r_2|$ to preserve Wilkinson conditioning), appending `X {{key:RCL}} A {{key:-}} {{key:÷}}` to the end of the equation in `{{key:EQN}}` forms the deflated function $g(x) = \frac{f(x)}{x - r_1}$, dividing out the zero at $r_1$ so a second `{{key:SOLVE}}` pass cannot fall back into the first root's basin of attraction.
4. **Recognizing `NO ROOT FND` (Code 08) & Tangent Extrema:**
   If a curve $f(x)$ stays strictly positive everywhere—such as $f(x) = x^2 + 4 = 0$, which has only complex roots $\pm 2i$—the outward golden-ratio search terminates after 50 expansion steps and displays `NO ROOT FND` (Code 08, cleared via `{{key:C}}`). Conversely, when a curve touches the axis tangentially at an even-multiplicity root such as $f(x) = (x - 3)^2 = 0$, Brent's solver detects the tangent minimum once $|b - a| < 10^{-12}$ and $|f(b)| < 10^{-7}$, or solving the derivative $f'(x) = 0$ restores simple-root conditioning directly.

Together, Horner's nested recurrence, Cardano and Viète's closed-form `{{key:POLY}}` solver, and Richard Brent's bracketed `{{key:SOLVE}}` algorithm span both halves of algebraic and transcendental root-finding. Where radical formulas end at degree four, hybrid inverse-quadratic and bisection bracketing takes over, resolving implicit conservation laws to machine precision without sacrificing guaranteed convergence.
