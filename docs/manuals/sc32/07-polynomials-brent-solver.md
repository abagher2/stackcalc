---
title: "Chapter 7: The Scandal of the Cubic & The Art of Hunting Roots | Thinking in the Stack (SC-32)"
description: "From al-Khwarizmi's squares and the 1535 Milan cubic duel to Horner's nested evaluation and Richard Brent's hybrid root solver on the StackCalc SC-32."
---

# Chapter 7: The Scandal of the Cubic & The Art of Hunting Roots

## From Al-Khwarizmi's Squares to the 1535 Duel in Milan

Around the year 820 CE, in Baghdad's House of Wisdom (*Bayt al-Hikma*), the Persian mathematician and astronomer **Muhammad ibn Musa al-Khwarizmi** wrote a landmark treatise: *Al-Kitāb al-mukhtaṣar fī ḥisāb al-jabr wa'l-muqābala* (*The Compendious Book on Calculation by Completion and Balancing*). Its title gave every language on Earth the word **algebra**—from *al-jabr*, restoring a subtracted term to the opposite side of an equation—while his own name, Latinized as *Algoritmi*, gave us the word **algorithm**.

When al-Khwarizmi set out to solve a quadratic equation such as his famous benchmark:

$$x^2 + 10x = 39$$

he did not reach for modern algebraic symbols, because plus signs, minus signs, and exponents would not be invented for another seven hundred years. Even more striking to modern eyes, al-Khwarizmi did not view $x^2$ as an abstract number multiplied by itself—he viewed $x^2$ as a **physical square** of side $x$, and $10x$ as the area of a rectangle.

How do you find the side $x$ of a square when its area $x^2$ plus $10x$ equals $39$? Follow al-Khwarizmi's geometric recipe:
1. Start with a square of side $x$ and area $x^2$.
2. Split the linear term $10x$ in half into two equal rectangles of width $5$ and length $x$ (each having area $5x$), and attach them to two adjacent edges of the $x \times x$ square.
3. Examine the L-shaped figure (a *gnomon*) you have just built. It is *almost* a larger square of side $(x + 5)$—except that the upper-right corner where the two $5 \times x$ wings meet is missing a little **$5 \times 5$ corner square** of area $25$.
4. Drop a $5 \times 5 = 25$ square into that empty corner to **complete the square**. Because you added $25$ to the geometric figure on the left, add $25$ to the $39$ on the right:

$$(x + 5)^2 = 39 + 25 = 64 = 8^2 \implies x + 5 = 8 \implies \mathbf{x = 3}$$

{{blocks:sc32_concept_khwarizmi_brent|Al-Khwarizmi's geometric completion of the square (820 CE) and Richard Brent's root-hunting bracket cage (SOLVE).}}

Apply that same geometric completion to the general quadratic equation $a x^2 + b x + c = 0$—dividing by $a$, splitting the middle term $(b/a)x$ into two wings of width $\frac{b}{2a}$, and filling the missing corner with $\left(\frac{b}{2a}\right)^2$—and out pops the universal **quadratic formula**:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

### William Kahan's Warning: When the Quadratic Formula Loses Its Mind

Before we leave quadratic equations, modern floating-point computing adds a fascinating plot twist to al-Khwarizmi's formula. As Berkeley numerical analyst **William Kahan** famously demonstrated, the textbook formula $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ contains a hidden numerical trap whenever $b^2$ is much larger than $4ac$ ($b^2 \gg |4ac|$).

When $b > 0$ and $4ac$ is tiny compared to $b^2$, the radical $\sqrt{b^2 - 4ac}$ is almost identical to $b$. When you evaluate the root with the plus sign ($-b + \sqrt{b^2 - 4ac}$), you are subtracting two nearly equal numbers—wiping out up to half or more of your calculator's significant digits in a single stroke of **catastrophic cancellation**! How do numerical analysts defeat this trap? As codified by William Kahan and in Press, Teukolsky, Vetterling, and Flannery's *Numerical Recipes*, you *never* subtract $\sqrt{b^2 - 4ac}$ from a number of the same sign. Instead, you form the **Citardauq ("Quadratic" spelled backward) intermediate quantity $q$** by always choosing the sign that **adds** the magnitudes together, and then extract the larger root $x_1 = q/a$ and the smaller root $x_2 = c/q$ via François Viète's exact root-product identity $x_1 x_2 = \frac{c}{a}$:

$$q = -\frac{1}{2}\Big(b + \operatorname{sgn}(b)\sqrt{b^2 - 4ac}\Big), \qquad x_1 = \frac{q}{a}, \qquad x_2 = \frac{c}{q}$$

Because $q$ is formed by pure magnitude addition (`b {{key:x²}} 4 {{key:ENTER}} a {{key:×}} c {{key:×}} {{key:-}} {{key:√x}} |b| {{key:+}} 2 {{key:÷}}` with sign $-\operatorname{sgn}(b)$), both $x_1 = q/a$ and $x_2 = c/q$ retain every last guard digit of precision even when $b^2$ exceeds $4ac$ by ten orders of magnitude!

Quadratic equations govern two classic inverse problems in mechanics and forensic engineering:
* **The Inverse Ballistic Trajectory Quadratic (Solving Backwards for Launch Angle):** In Chapter 4, we projected where a shell lands when its launch angle $\theta$ is already known. What if we face the *inverse* question: the target coordinates $(x, y)$ are fixed on an elevated ridge at known muzzle speed $v_0$, and we must solve backwards for the required launch angle $\theta$? Substituting the trigonometric identity $\sec^2\theta = 1 + \tan^2\theta$ into Galileo's parabolic trajectory $y = x\tan\theta - \frac{gx^2}{2v_0^2}\sec^2\theta$ turns the unknown launch slope $u = \tan\theta$ into a quadratic equation:
  $$\left(\frac{gx^2}{2v_0^2}\right) u^2 - x u + \left(y + \frac{gx^2}{2v_0^2}\right) = 0$$
  Whenever the target lies within the gun's reach, its two positive roots give the gunner two distinct paths to the same coordinates: a flat, fast **low direct-fire trajectory** ($\theta_1 = \arctan u_1$) and a high, arcing **plunging mortar trajectory** ($\theta_2 = \arctan u_2$) that drops down from above.
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

On the SC-32, pressing **`{{key:POLY}}`** (`{{key:↱}}` + `{{key:XEQ}}`) opens the dedicated analytical polynomial workspace for $Ax^3 + Bx^2 + Cx + D = 0$, mapping the six LFU softkeys to `{{key:A}}`, `{{key:B}}`, `{{key:C}}`, `{{key:D}}`, `{{key:EXEC}}`, and `{{key:CLR}}`. Key each coefficient onto the stack and tap its softkey, setting `0 {{key:D}}` whenever you want to solve a quadratic $Ax^2 + Bx + C = 0$. Pressing `{{key:EXEC}}` evaluates the discriminant $\Delta$, places the primary root $r_1$ onto the stack in Gaussian complex format ($Y = \text{Real},\; X = \text{Imag}$), and writes all three real or complex roots into numbered variable registers `1` through `6` (`{{key:RCL}} 1` through `{{key:RCL}} 6`).

Behind that single `{{key:EXEC}}` keystroke stand three classical pillars of polynomial theory:

1. **François Viète's Cosine Trisection of the Cubic (1593):** The French cryptographer and algebraist **François Viète** spotted a striking resemblance between the depressed cubic $t^3 + pt + q = 0$ (when $\Delta < 0$, so $p < 0$) and the trigonometric triple-angle identity for cosine:
   $$\cos(3\theta) = 4\cos^3\theta - 3\cos\theta \implies \cos^3\theta - \frac{3}{4}\cos\theta - \frac{1}{4}\cos(3\theta) = 0$$
   By scaling the unknown $t = 2\sqrt{-p/3}\,\cos\theta$, Viète matched the depressed cubic term-for-term against the triple-angle cosine identity, expressing all three real roots in closed form without a single complex square root:
   $$t_k = 2\sqrt{-\frac{p}{3}} \cos\left(\frac{1}{3}\arccos\left(\frac{3q}{2p}\sqrt{-\frac{3}{p}}\right) - \frac{2\pi k}{3}\right), \qquad k = 0, 1, 2$$
   Geometrically, solving a three-real-root cubic is identical to **trisecting an angle on the unit circle** and projecting the three $120^\circ$-spaced corners of an inscribed equilateral triangle down onto the horizontal real axis.
2. **Lodovico Ferrari's Reduction of the Quartic to a Resolvent Cubic (1540):** Right after Cardano mastered the cubic in 1539, a rival mathematician named Zuanne da Coi challenged Cardano and Tartaglia with a fourth-degree **quartic equation**: $x^4 + 6x^2 + 36 = 60x$. Neither Cardano nor Tartaglia could solve it—until Cardano's eighteen-year-old protégé **Lodovico Ferrari** spotted a two-stage algebraic lockpick.
   After shifting $x$ to remove the $x^3$ term ($x^4 + px^2 + qx + r = 0$), Ferrari moved $px^2 + qx + r$ to the right side, completed the square on the left as $(x^2 + \frac{p}{2})^2$, and introduced an **auxiliary variable $y$** inside the square:
   $$\left(x^2 + \frac{p}{2} + y\right)^2 = (p + 2y)x^2 - qx + \left(\frac{p^2}{4} - r + py + y^2\right)$$
   Examine the right-hand side: it is an ordinary **quadratic in $x$**. When is a quadratic in $x$ a perfect square $(mx + n)^2$ so that we can take the square root of both sides of the equation? Precisely when its quadratic discriminant $B^2 - 4AC$ equals zero:
   $$q^2 - 4(p + 2y)\left(y^2 + py + \frac{p^2}{4} - r\right) = 0$$
   And what degree is that equation for the helper variable $y$? It is a **third-degree cubic equation**—the **resolvent cubic**—which Cardano's `{{key:POLY}}` solver can already solve. Once one root $y_1$ of the resolvent cubic is found, the quartic splits into two ordinary quadratic equations, giving all four roots.
3. **Viète's Root-Coefficient Checksums (Viète's Formulas):** Whenever `{{key:POLY}}` writes the roots of a cubic ($A x^3 + B x^2 + C x + D = 0$) into variables `1` through `6`, how can you verify in two seconds that your roots are $100\%$ accurate without plugging each root back into the polynomial? Multiply out $A(x - r_1)(x - r_2)(x - r_3) = A x^3 - A(r_1 + r_2 + r_3)x^2 + A(r_1 r_2 + r_2 r_3 + r_3 r_1)x - A r_1 r_2 r_3$ and compare the **sum of roots (trace)**, **pairwise product sum**, and **product of roots (determinant)** term by term:
   $$r_1 + r_2 + r_3 = -\frac{B}{A}, \qquad r_1 r_2 + r_2 r_3 + r_3 r_1 = +\frac{C}{A}, \qquad r_1 \cdot r_2 \cdot r_3 = -\frac{D}{A}$$
   For our benchmark cubic $x^3 - 6x^2 + 11x - 6 = 0$ with roots $1, 2, 3$, recalling and summing `{{key:RCL}} 1 {{key:RCL}} 3 {{key:+}} {{key:RCL}} 5 {{key:+}}` gives the trace $1 + 2 + 3 = 6 = -(-6)/1$. Likewise, their pairwise product sum is $1(2) + 2(3) + 3(1) = 11 = +11/1$, and their determinant product `{{key:RCL}} 1 {{key:RCL}} 3 {{key:×}} {{key:RCL}} 5 {{key:×}}` is $1 \times 2 \times 3 = 6 = -(-6)/1$. In any **depressed cubic** $t^3 + pt + q = 0$ (where $B = 0$), **the three roots always sum identically to zero** ($t_1 + t_2 + t_3 = 0$), because the coordinate shift $x = t - \frac{B}{3A}$ placed the origin right at the centroid of the three roots.

And why did the chain of radical reductions stop forever after Ferrari's degree-4 quartic? For nearly three hundred years after *Ars Magna*, the greatest minds in Europe—including Ehrenfried Walther von Tschirnhaus, Leonhard Euler, and Joseph-Louis Lagrange—hunted for a degree-5 quintic formula ($Ax^5 + Bx^4 + Cx^3 + Dx^2 + Ex + F = 0$). Lagrange spotted a troubling pattern: for a degree-2 quadratic, the resolvent has degree 1; for a degree-3 cubic, Tartaglia's resolvent has degree 2; for a degree-4 quartic, Ferrari's resolvent has degree 3. Each time, the helper equation had *lower* degree than the original problem. Yet when Lagrange applied the same permutation method to a degree-5 quintic, the resolvent equation jumped *up* to degree 6 (with $5!/2 = 60$ alternating permutations).

In **1824**, the twenty-one-year-old Norwegian mathematician **Niels Henrik Abel** built on Paolo Ruffini's 1799 work to prove that this barrier is absolute. Eight years later, on the night of May 29, 1832, the twenty-year-old French revolutionary **Évariste Galois** scribbled a frantic letter by candlelight hours before he was fatally shot in a pistol duel at dawn, founding **Group Theory** and explaining why. For degrees $n = 2, 3, 4$, the permutation group $S_n$ of the roots breaks down into commutative cyclic pieces ("solvable groups") that correspond to extracting $k$-th roots $\sqrt[k]{\phantom{x}}$. For $n \ge 5$, however, the alternating group $A_5$—the $60$ rotational symmetries of a regular icosahedron—is a **simple non-abelian group** that cannot be factored into cyclic steps. **No general radical formula in $+, -, \times, \div$, and $\sqrt[n]{\phantom{x}}$ can ever exist for degree 5 or higher!**

---

## Unpeeling Polynomials from the Inside Out: Horner's Scheme

Even before we try to *solve* a polynomial $P(x) = 0$, how should we *evaluate* a polynomial at a given number $x$?

Take the fourth-degree polynomial:

$$P(x) = 4x^4 - 3x^3 + 2x^2 - 5x + 7 \qquad \text{at } x = 2.5$$

If you evaluate $P(x)$ the way it is written on the page—computing $x^4$, multiplying by $4$, computing $x^3$, multiplying by $3$, computing $x^2$, and so on—you have to compute powers of $x$ over and over again ($4 + 3 + 2 + 1 = 10$ multiplications, or three separate exponentiations). Worse yet, near a root where large positive and negative power terms nearly cancel out, computing $a_n x^n$ separately magnifies floating-point rounding error.

In 1819, the English schoolmaster **William George Horner** (rediscovering a method known to Isaac Newton in 1669 and the 13th-century Chinese algebraist **Qin Jiushao** in his 1247 *Mathematical Treatise in Nine Sections*) showed what happens when you factor $x$ out from the inside out:

$$P(x) = 4x^4 - 3x^3 + 2x^2 - 5x + 7 = (((4x - 3)x + 2)x - 5)x + 7$$

In **Horner's nested scheme**, every single exponent has vanished. To evaluate any degree-$n$ polynomial at $x$, you start with the leading coefficient $a_n$ and repeat a two-beat rhythm $n$ times:

$$\textbf{Multiply by } x \text{ (`{{key:×}}`),} \quad \textbf{Add the next coefficient (`{{key:+}}` or `{{key:-}}`).}$$

Walk through that two-beat rhythm on $P(2.5) = (((4(2.5) - 3)(2.5) + 2)(2.5) - 5)(2.5) + 7$:
* Start with $4$, multiply by $2.5$ ($\to 10$), subtract $3$ ($\to \mathbf{7.0}$).
* Multiply by $2.5$ ($\to 17.5$), add $2$ ($\to \mathbf{19.5}$).
* Multiply by $2.5$ ($\to 48.75$), subtract $5$ ($\to \mathbf{43.75}$).
* Multiply by $2.5$ ($\to 109.375$), add $7$ ($\to \mathbf{116.3750}$).

Four multiplications, four additions, zero powers, and zero temporary variables. On the SC-32, you can make Horner's scheme even faster by **flooding all four stack registers with $x$** at the outset via **`x {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}`**. Because the top shelf **Register $T$ replicates its value downward into Register $Z$** every time the stack drops, a fresh copy of $x$ is waiting in Register $Y$ whenever you finish adding a coefficient—turning the four-register stack into an automatic Horner conveyor belt where you never have to re-type $x$!

Better still, the intermediate numbers produced at each beat of Horner's scheme ($4,\; 7.0,\; 19.5,\; 43.75$) are not random scratchpad numbers—they are the exact coefficients of the quotient polynomial $Q(x)$ obtained by **Ruffini-Horner synthetic division** when dividing $P(x)$ by $(x - x_0)$ at $x_0 = 2.5$:

$$P(x) = (x - x_0)\,Q(x) + R = (x - 2.5)\left(4x^3 + 7x^2 + 19.5x + 43.75\right) + 116.3750$$

This Polynomial Remainder Theorem identity $P(x) = (x - x_0)Q(x) + P(x_0)$ gives us three computational superpowers:
* **Polynomial Deflation:** Once you find one exact root $r_1$ of a polynomial (where the remainder $P(r_1) = 0$), the intermediate numbers generated during Horner's evaluation at $r_1$ hand you the deflated degree-$(n-1)$ quotient polynomial $Q(x) = P(x)/(x - r_1)$—allowing you to drop a fourth-degree quartic down to a cubic, or a cubic down to a quadratic.
* **Simultaneous Derivative Evaluation ($P'(x_0) = Q(x_0)$):** Differentiate $P(x) = (x - x_0)Q(x) + P(x_0)$ with respect to $x$ by the product rule:
   $$P'(x) = Q(x) + (x - x_0)Q'(x) \implies P'(x_0) = Q(x_0)$$
   Evaluating the quotient polynomial $Q(x)$ at $x_0$ by running a second Horner pass on the intermediate coefficients gives the exact **calculus derivative $P'(x_0)$** without writing down a symbolic derivative formula.
* **Suppression of Catastrophic Cancellation Near Multiple Roots:** This stability is vital in numerical thermodynamics and flight-control engineering, where computers evaluate standard-atmosphere pressure-altitude curves $P(h) = a_3 h^3 + a_2 h^2 + a_1 h + a_0$ and NASA Glenn molar heat-capacity fits $C_p(T)/R = a_0 + a_1 T + a_2 T^2 + a_3 T^3 + a_4 T^4$. Near a repeated root such as $s = -5$ in our critically damped RLC filter, nested Horner evaluation updates the local factor $(s + 5)$ at each step instead of subtracting large, independently rounded powers $s^3$ and $12s^2$.

That same nested-factoring mindset simplifies rational formulas and symmetric high-degree equations across physics:
* **Martin Green's Solar-Cell Fill Factor (1982):** In a silicon photovoltaic cell, the maximum power point satisfies a transcendental diode equation that cannot be inverted in closed form, but Australian solar physicist Martin Green discovered an accurate rational-logarithmic expression in the normalized open-circuit voltage $v_{\text{oc}} = V_{\text{oc}} / V_T$ (evaluated in one pass on the stack by flooding $v_{\text{oc}}$ across all four registers with `{{key:ENTER}} {{key:ENTER}} {{key:ENTER}}`):
  $$\text{Fill Factor } FF = \frac{v_{\text{oc}} - \ln(v_{\text{oc}} + 0.72)}{v_{\text{oc}} + 1}$$
* **Coupled-Oscillator Biquadratic Polynomials:** When two coupled undamped spring-mass pendulums vibrate in their natural normal modes, the eigenvalue equation $\det(\mathbf{K} - \omega^2\mathbf{M}) = 0$ contains only even powers of frequency ($a x^4 + b x^2 + c = 0$), which collapses into a quadratic in $u = x^2$ whose positive square roots $\omega = \sqrt{u}$ give the two normal-mode frequencies.

---

## Why Newton's Method Flies Off Cliffs—And How Richard Brent Tamed It

Abel and Galois proved that we cannot even solve $x^5 - x - 1 = 0$ with a radical formula. And across real-world science and engineering, nature rarely hands us pure polynomials anyway. Physical conservation laws constantly mix algebraic powers $x$ with sines, cosines, exponentials, and logarithms—producing **transcendental equations** where no symbolic manipulation can ever isolate the unknown on one side of the equals sign.

How do you hunt down a root $x^*$ where $f(x^*) = 0$ when algebra cannot isolate $x$? Over three centuries, numerical analysts developed two rival philosophies—one slow and invincible, the other blazingly fast and reckless:

1. **The Tortoise — Bolzano's Intermediate Value Theorem & Bisection:** Suppose a continuous curve $f(x)$ lies below the axis at $x = a$ with $f(a) < 0$ and above it at $x = b$ with $f(b) > 0$, giving opposite signs $f(a)\cdot f(b) < 0$. Bernard Bolzano's 1817 **Intermediate Value Theorem** guarantees that the curve cannot pass from negative to positive without crossing $y = 0$ at least once inside the **bracket** $[a, b]$.
   In the **Bisection Method**, you evaluate the function at the midpoint $m = \frac{1}{2}(a + b)$, check its sign, and throw away whichever half of the interval does not contain the sign change. Every step cuts the uncertainty in half—gaining $1\text{ binary bit}$ of precision per step (linear convergence, order $p = 1.000$). After $40$ bisections, your bracket has shrunk by $2^{-40} \approx 10^{-12}$. Bisection can *never* fail on a bracketed root, but taking $40$ to $50$ function evaluations is a slow trudge.
2. **The Hare — Newton-Raphson & the Secant Chord:** In 1669, **Isaac Newton**—testing John Wallis's cubic benchmark $x^3 - 2x - 5 = 0$ near $x_0 = 2$—and **Joseph Raphson** in 1690 proposed sliding down the local tangent line of the curve:
   $$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$
   Near a clean simple root, Newton's method is **quadratically convergent** ($p = 2.000$), **doubling the number of accurate decimal digits on every single step** ($1 \to 2 \to 4 \to 8 \to 16\text{ digits}$). And if you don't want to work out the calculus derivative $f'(x)$ by hand, replacing the tangent slope with the **Secant Chord** through the last two points gives superlinear convergence at the **golden-ratio power** $p = \phi = \frac{1+\sqrt{5}}{2} \approx 1.618$.
   So what is the catch? Look at the denominator $f'(x_n)$ in Newton's formula (or $f(x_n) - f(x_{n-1})$ in the secant formula). If your search ever wanders near a peak, a valley, an inflection plateau, or a horizontal asymptote where the slope flattens out ($f'(x_n) \approx 0$), **the nearly horizontal tangent line shoots off to the horizon, catapulting $x_{n+1}$ miles away from the root or into an infinite loop!**

### Richard Brent's 1973 Masterpiece: Algorithmic Paranoia

In 1973, building on earlier work by Theodorus Dekker, the Australian mathematician **Richard P. Brent** asked a brilliant question in *Algorithms for Minimization Without Derivatives* {{cite:brent1973}}: *Can we combine the invincible safety net of Bisection with the superlinear sprint of Interpolation so that the solver runs at top speed on smooth curves, never requires a derivative, and is mathematically guaranteed never to fly off a cliff?* Six years later, UC Berkeley numerical analyst **William M. Kahan** {{cite:kahan1979}} adapted this Dekker–Brent hybrid philosophy for Hewlett-Packard's pocket **`SOLVE`** key—debuting on the 1979 HP-34C, carried into the 1982 HP-15C Voyager {{cite:hp15c1982}}, and paired with symbolic equations on the 1991 HP-32SII Pioneer {{cite:hp32sii1991}}.

Brent's hybrid root-finding algorithm—the engine behind the SC-32's 64-bit **`{{key:SOLVE}}`** key (`{{key:↱}}` + `{{key:7}}`, paired with the **`{{key:EQN}}`** equation editor)—achieves this through two mechanisms:
* **Sideways Parabolic Fitting (Inverse Quadratic Interpolation, $p \approx 1.839$):** Given three distinct points $(a, f(a))$, $(b, f(b))$, and $(c, f(c))$ near the root, fitting an ordinary upright parabola $y = P(x)$ can fail whenever its vertex turns around before reaching the $x$-axis, leaving *no real roots at all*. Brent instead turns his head sideways and fits $x$ as a **Lagrange quadratic polynomial of $y$** ($x = P(y)$) through $(f(a), a)$, $(f(b), b)$, and $(f(c), c)$, and then evaluates that sideways curve at $y = 0$:
  $$x_{\text{IQI}} = \frac{a f(b) f(c)}{(f(a)-f(b))(f(a)-f(c))} + \frac{b f(a) f(c)}{(f(b)-f(a))(f(b)-f(c))} + \frac{c f(a) f(b)}{(f(c)-f(a))(f(c)-f(b))}$$
  Evaluating a sideways parabola at $y = 0$ is guaranteed to yield a single unique real number $x_{\text{IQI}}$, converging at order $p \approx 1.839$ (nearly doubling the correct digits on every step).
* **The Five Watchdog Tests:** Brent never trusts an interpolated step blindly. At every single iteration, the algorithm keeps the root locked inside a shrinking sign-change cage $[a, b]$ where $f(a)f(b) \le 0$. Whenever Secant or Inverse Quadratic Interpolation proposes a leap $s$, **five watchdog conditions** inspect it: does $s$ land strictly inside the interior three-quarter window $\left(\frac{3a+b}{4}, b\right)$? And is the step contracting the bracket at least twice as fast as the previous steps? The instant an interpolated step tries to jump outside the cage or stalls on a flat plateau, **Brent's watchdog vetoes the interpolation and forces a guaranteed Bisection step $m = \frac{1}{2}(a + b)$!**

| Root-Finding Algorithm | Convergence Order ($p$) | Requires Derivative $f'(x)$? | Guaranteed to Stay in Bracket? | Behavior Near Flat Slopes ($f'(x) \approx 0$) |
| :--- | :---: | :---: | :---: | :--- |
| **Bisection** | $1.000$ | No | Yes (Guaranteed) | Steady ($1\text{ bit/step}$), immune to slope traps |
| **Newton-Raphson** | $2.000$ | Yes | No | Catastrophic divergence when $f'(x) \approx 0$ |
| **Secant Chord** | $1.618$ ($\phi$) | No | No | Can fling iterates far outside the search region |
| **Brent's Hybrid Method** | $1.839$ | No | **Yes (Guaranteed)** | **Instant bisection fallback; zero divergence** |

### Where the Unknown Hides: Four Classic Transcendental Equations of Science and Engineering

Why do so many fundamental laws of physics refuse to hand us an explicit formula $x = \dots$? Whenever nature couples two different geometric or physical mechanisms inside the same conservation balance, the unknown gets trapped simultaneously inside two incompatible mathematical operations—so no algebraic manipulation on Earth can ever isolate $x$ on one side of the equals sign:

1. **Kepler's Orbital Anomaly ($E - e \sin E = M$):** In his 1609 *Astronomia Nova*, **Johannes Kepler** discovered that as a planet sweeps out equal areas in equal times along an ellipse of eccentricity $e$, its uniform clock angle $M = \frac{2\pi t}{T}$ (**mean anomaly**) and its geometric position angle $E$ (**eccentric anomaly**) obey $E - e\sin E - M = 0$. Because the unknown angle $E$ appears simultaneously as a linear algebraic arc outside the sine function and as a trigonometric phase inside $\sin E$, Kepler lamented that the equation *"cannot be solved a priori, on account of the different nature of the arc and the sine."*
2. **Colebrook–White Turbulent Pipe Friction ($1/\sqrt{f}$):** When water or rocket propellant rushes through a rough pipe of diameter $D$ at high Reynolds number $\text{Re}$, a microscopic viscous sublayer of thickness $\delta_v \propto D/(\text{Re}\sqrt{f})$ cushions the pipe wall. Because the thickness of that protective cushion depends on the very Darcy–Weisbach friction factor $f$ we are trying to find, **Cyril Colebrook** (1939) {{cite:colebrook1939}} showed that $\sqrt{f}$ is trapped both outside and inside a base-$10$ logarithm:
   $$\frac{1}{\sqrt{f}} = -2.0 \log_{10} \left( \frac{\varepsilon / D}{3.7} + \frac{2.51}{\text{Re}\sqrt{f}} \right)$$
   For generations before pocket numerical solvers, hydraulic engineers had to squint at the logarithmic curves of the **Moody Chart** to estimate $f$.
3. **Planck's Blackbody Radiation & Wien's Displacement Law ($(5 - x)e^x = 5$):** When **Max Planck** (1900) derived the quantum spectrum of starlight, $I(\lambda) \propto \lambda^{-5}/(e^{hc/\lambda k_B T} - 1)$, locating the peak wavelength $\lambda_{\max}$ required setting the derivative to zero. That differentiation traps the dimensionless photon energy $x = hc/(\lambda_{\max} k_B T)$ both inside the exponential $e^x$ and as an algebraic factor $(5 - x)$ outside it: $(5 - x)e^x = 5$ (or $5(1 - e^{-x}) - x = 0$), whose root $x^* = \mathbf{4.9651142317}$ sets the color temperature of every star in the cosmos.
4. **Shockley's Silicon Diode Load Line ($I_D(V)$):** When a DC voltage source $V_s$ drives a semiconductor junction diode through a series load resistor $R$, Kirchhoff's voltage law $(V_s - V)/R = I_s(e^{V/V_T} - 1)$ pits a straight-line resistor drop against **William Shockley's** exponential diode wall—trapping the junction voltage $V$ both linearly outside the exponential and thermally inside $e^{V/V_T}$.

Even when a physical balance remains purely algebraic, 3D geometry and conservation laws routinely lift the problem into a cubic polynomial whose roots carry direct physical meaning:
* **Archimedes' Floating Sphere ($h^3 - 3Rh^2 + 4(\rho_s/\rho_w)R^3 = 0$):** Answering the cliffhanger from the end of Chapter 6, a sphere of radius $R$ and density $\rho_s$ sinks in water of density $\rho_w$ until its submerged cap volume $\frac{1}{3}\pi h^2(3R - h)$ balances $\frac{\rho_s}{\rho_w}(\frac{4}{3}\pi R^3)$—a cubic whose middle root (`{{key:RCL}} 3` in `{{key:POLY}}`) is the exact waterline draft $h \in [0, 2R]$.
* **3D Cauchy Principal Stresses & Van der Waals Real Gases:** Twisting a piece of brittle blackboard chalk snaps it along a $45^\circ$ helix governed by the three real eigenvalues of the Cauchy stress cubic $\lambda^3 - I_1\lambda^2 + I_2\lambda - I_3 = 0$, while compressing a real gas near its critical point obeys **Johannes Diderik van der Waals's** cubic equation of state $\left(P + \frac{a}{V^2}\right)(V - b) = RT$.

### Conditioning of Multiple Roots & Why Deflation Order Matters

Before we step into the equation editor, **James H. Wilkinson**—Alan Turing's colleague on the Pilot ACE computer and the founder of modern backward error analysis—uncovered a crucial geometrical contrast between simple crossings and repeated roots. At a clean **simple root** where the curve crosses the axis with non-zero slope ($f'(x^*) \ne 0$), a tiny vertical rounding fuzz of size $\varepsilon_{\text{mach}} \approx 10^{-16}$ in evaluating $f(x)$ shifts the horizontal zero crossing by at most $\Delta x \approx \frac{\varepsilon_{\text{mach}}}{|f'(x^*)|}$. At an **$m$-fold repeated root** where the curve flattens out and kisses the axis tangentially as $f(x) \approx c(x - x^*)^m$, however, solving $|c(x - x^*)^m| \le \varepsilon_{\text{mach}}$ reveals **Wilkinson's Root Conditioning Law**:

$$\Delta x \approx \left(\frac{\varepsilon_{\text{mach}}}{|c|}\right)^{1/m}$$

For a double tangent root ($m = 2$, such as $(x - 3)^2 = 0$), the horizontal uncertainty widens to the **square root of machine epsilon** ($\varepsilon_{\text{mach}}^{1/2} \approx 10^{-8}$), creating a microscopic flat plateau where half the digits of precision vanish into floating-point noise; for a triple root ($m = 3$), precision drops to $\varepsilon_{\text{mach}}^{1/3} \approx 10^{-5}$. Worse still, if you deflate a high-degree polynomial $P(x)$ down to $Q(x) = P(x)/(x - r_1)$ by dividing out its *largest* root $|r_1|$ first, small rounding errors contaminate the lower coefficients of $Q(x)$ and perturb the remaining roots. Always deflate roots in **increasing order of magnitude** ($|r_1| \le |r_2| \le \dots$), and when hunting an even-multiplicity tangent minimum, solve the derivative $f'(x) = 0$ to restore full simple-root conditioning!

### Inside the Symbolic Equation Bank (EQN): Pure Functions, Step Editing & Iverson Piecewise Logic

Before we hand an implicit equation over to Brent's root hunter, how do we enter, inspect, edit, and structure a formula inside the SC-32's **`{{key:EQN}}` workspace** (`{{key:↱}}` + `{{key:STO}}`)—and how can a single RPN equation represent a **piecewise physical law** that changes its mathematical formula across a threshold?

Unlike vintage keystroke-programmable calculators that mixed arithmetic formulas with destructive memory writes and spaghetti-code `GTO` jumps, the SC-32's **24-slot Equation Bank** treats every stored entry (`A` through `Z`, up to $96$ steps per equation) as a **pure, side-effect-free mathematical function**:
* **Creating, Labeling & Navigating Equations:** Pressing `{{key:EQN}}` opens the Equation Catalog (`NEW`, `1:A`, `2:B`, … on the top softkeys). Tapping `NEW` (`{{key:LFU0}}`) or pressing `{{key:LBL}}` (Left Shift on `+`) prompts **`LBL _`** and automatically arms the `A–Z` Alpha layer so a single tap assigns your equation's letter (`00 LBL A`). As you key in operations, each step is recorded with a line number (`01 RCL X`, `02 x²`, …). When typing a multi-digit constant such as `0.05`, pressing `{{key:ENTER}}` terminates the numeric literal without duplicating the stack, whereas a second tap inserts an explicit `ENTER` step. At any time, `{{key:↑}}` and `{{key:↓}}` (Left Shift on `8` and `7`) step the cursor backward and forward through your numbered instructions: typing any key inserts right at the cursor, `{{key:<-}}` deletes the preceding step, and `{{key:RTN}}` (Right Shift on `+`) or `{{key:C}}` saves the equation to non-volatile memory.
* **Why `STO` Is Blocked Inside `EQN` (`INVALID FOR EQN`):** Inside an equation, pressing `{{key:RCL}}` followed by a letter (`A`–`Z`, or indirect `(i)`—recall from Chapter 2 that storing a slot number $1\dots 89$ in the index pointer `i` via `STO .` lets `RCL x∥y` dereference `(i)` dynamically) reads that variable onto the stack, and `RCL + A` or `RCL × A` performs in-place recall arithmetic. By contrast, `{{key:STO}}` is intentionally blocked (`INVALID FOR EQN`) so that when `{{key:XEQ}}`, `{{key:FN=}}`, `{{key:SOLVE}}`, `{{key:∫}}`, or `{{key:PLOT}}` evaluates your equation dozens or hundreds of times across an interval, it can never overwrite your stored laboratory constants.
* **Macaulay's Singularity Bracket & Iverson's Indicator Logic (`x?0` and `x?y`):** In 1919, the Cambridge mathematician **William H. Macaulay** solved a headache that had plagued structural engineers since Euler: when a bridge beam carries concentrated point loads or steps in cross-section at stations $a_1, a_2, \dots$, writing a separate differential equation for every span is a nightmare. Macaulay introduced the **singularity ramp bracket** $\langle x - a \rangle_+ = \max(0, x - a)$, which equals $0$ to the left of $x = a$ and turns on smoothly as $(x - a)$ to the right of $x = a$. Four decades later, **Kenneth E. Iverson** (1962) generalized Macaulay's switch into the **Iverson Indicator Bracket $[P] \in \{1, 0\}$**, where any relational proposition $P$ evaluates to **`1` if True** and **`0` if False**:
  $$f(x) = f_1(x)\cdot [x \le c] + f_2(x)\cdot [x > c] \qquad \text{or} \qquad \langle u \rangle_+ = u \cdot [u > 0] = \max(0, u)$$
  On the SC-32, the **`{{key:x?0}}`** menu (Right Shift on `{{key:÷}}`) provides six unary zero comparisons (`x=0`, `x≠0`, `x>0`, `x<0`, `x≥0`, and `x≤0`), each replacing Register $X$ in place with `1.0` for True or `0.0` for False. Its companion **`{{key:x?y}}`** menu (Left Shift on `÷`) offers the six binary two-register comparisons (`x=y`, `x≠y`, `x>y`, `x<y`, `x≥y`, and `x≤y`), which compare Register $X$ against Register $Y$, drop the stack, and leave `1.0` or `0.0` in Register $X$. Consequently, on any expression $u$ sitting in Register $X$, the three-keystroke **Macaulay Ramp Idiom** **`{{key:ENTER}} {{key:x>0}} {{key:×}}`** duplicates $u$ into $Y$, converts $X$ into $[u > 0] \in \{0, 1\}$, and multiplies them to produce $\langle u \rangle_+ = \max(0, u)$—allowing you to model bilinear contact springs, progressive tax or tariff brackets, Zener clippers, and piecewise fluid drag laws inside a single continuous `EQN` formula!

### How Brent's Two-Phase Engine and Kahan's Diagnostic Audit Work Together

What happens behind the scenes when you hand an equation $f(x) = 0$ in `{{key:EQN}}` to Brent's `{{key:SOLVE}}` key, and how can you tell with certainty whether the number returned on the screen is a genuine root or a mathematical mirage?

Brent's solver operates as a **two-phase state machine**:
1. **Phase 1 — Guarded Secant & Golden-Ratio Outward Bracket Search:** If you place two initial guesses in **Registers $Y$ and $X$** that already straddle a sign change ($f(a)\cdot f(b) \le 0$), `{{key:SOLVE}}` adopts your $(Y, X)$ stack shelves as the starting bracket $[a, b]$ and locks the cage at once. What if you store only a single seed $x_0$ via `{{key:STO}}`, or two guesses on the same side of the axis where $f(a)\cdot f(b) > 0$? Phase 1 generates a companion probe ($\Delta = 0.1|x_0|$) and marches outward for up to $50$ steps using clamped secant steps, or expanding by the **golden ratio** $\phi \approx 1.618034$ whenever the slope is flat. Along the way, it pulls back any probe that steps outside the domain of $\ln x$ or $\sqrt{x}$, and it detects even-multiplicity tangent roots like $(x - 2)^2 = 0$ whenever $|b - a| < 10^{-12}$ and $|f(b)| < 10^{-7}$.
2. **Phase 2 — Inverse Quadratic / Secant Sprint with Five Bisection Watchdogs:** Once a sign change $f(a)\cdot f(b) \le 0$ is caged, Phase 2 attempts **Inverse Quadratic Interpolation (IQI)** whenever three distinct values $(f(a), f(b), f(c))$ are available, or a **Secant Chord** step otherwise. Before accepting the proposed step $s$, Brent's five watchdogs verify that $s$ lies strictly inside the three-quarter window $\left(\frac{3a+b}{4}, b\right)$ and shrinks the step width by at least $50\%$ every two steps; if any check fails, the engine takes a guaranteed **Bisection** step $m = \frac{1}{2}(a + b)$ until $|f(b)| \le 10^{-13}$ or the half-bracket width reaches machine tolerance $\text{tol} = 2\varepsilon_{\text{mach}}|b| + \frac{1}{2}\cdot 10^{-12}$.

Even more importantly, following **William Kahan's** diagnostic solver philosophy, you should always distinguish a genuine crossing root from a discontinuous pole. When `{{key:SOLVE}}` finishes on the SC-32, it writes the converged root $x^*$ into your target variable and pushes $x^*$ onto **Register $X$** while lifting your starting guess (or upper bracket bound) into **Register $Y$** and preserving the prior stack contents in **Registers $Z$ and $T$**.

What if your initial bracket accidentally straddled a **vertical asymptote (discontinuous pole)** where the curve jumps from $-\infty$ to $+\infty$, such as $f(x) = \tan x$ across $x = \pi/2$ or $f(x) = \frac{1}{x - 2}$ across $x = 2$? Because $f(x)$ is negative on the left of the pole and positive on the right ($f(a)\cdot f(b) < 0$), bisection will pinch tightly around the pole $x = 2.0000000000$. Because `SOLVE` has already stored $x^*$ in your equation's variable, pressing **`{{key:XEQ}}`** followed by your equation's letter evaluates the residual $f(x^*)$ in Register $X$: at a **true root**, it returns $f(x^*) \approx 0$ ($|f(x^*)| \le 10^{-12}$), whereas at a **false pole**, it exposes a gigantic residual ($|f(x^*)| \gg 1$, or `DIVIDE BY 0`)!

---

## On the Stack: Horner Evaluation, Cardano's POLY & Brent's SOLVE

Every root-finding problem on the SC-32 begins by choosing between closed-form polynomial algebra (`{{key:POLY}}`) and bracketed numerical root-hunting (`{{key:SOLVE}}`):

> **Guided Root-Finding Workflow: `{{key:POLY}}` vs. `{{key:SOLVE}}`**
> 1. **Path 1 — Closed-Form Polynomial Roots (`{{key:POLY}}`):** When your equation is a quadratic ($ax^2 + bx + c = 0$) or a cubic ($Ax^3 + Bx^2 + Cx + D = 0$) with known coefficients, you do not even need to type an equation into `{{key:EQN}}`! Open `{{key:POLY}}` (above `{{key:XEQ}}`), enter the coefficients from highest degree down onto the softkeys (`a {{key:A}} b {{key:B}} c {{key:C}} 0 {{key:D}}` for a quadratic, or `A {{key:A}} B {{key:B}} C {{key:C}} D {{key:D}}` for a cubic—which also pushes `A, B, C, D` down the four-level stack), and press `{{key:EXEC}}` to extract all real and complex roots directly via the Citardauq quadratic and Cardano–Viète cubic formulas into the scrollable root display and root registers `1` through `6` (indirect `R34`–`R39`).
> 2. **Path 2 — Brent's Numerical Root-Finder (`{{key:SOLVE}}`):** When your equation is transcendental or higher-degree, follow three natural steps:
>    * **Step 1 (Define Residual $f(X) = 0$):** Store the expression $\text{LHS} - \text{RHS}$ in `{{key:EQN}}` (`{{key:↱}}` + `{{key:STO}}`).
>    * **Step 2 (Seed the Bracket on $Y$ and $X$):** Key two bracket guesses $[a, b]$ onto Register $Y$ and Register $X$ via `a {{key:ENTER}} b` (or store a single starting seed via `a {{key:STO}} X`).
>    * **Step 3 (Invoke `{{key:SOLVE}}` & Audit with `{{key:XEQ}}`):** Press `{{key:SOLVE}}` (above `{{key:7}}`) and tap your target variable letter (`X`). The converged root $x^*$ lands in **Register $X$** (with your bracket partner in **Register $Y$**), and tapping `{{key:XEQ}}` verifies that the residual $|f(x^*)| \le 10^{-12}$ is a true zero crossing rather than a vertical pole!

{{res:sc32_cubic_roots:screenshot|Cubic polynomial x^3 - 6x^2 + 11x - 6 = 0 solved via POLY}}

### Horner's Nested Evaluation, T-Register Flooding & Biquadratic Reductions

Evaluating $P(x) = 4x^4 - 3x^3 + 2x^2 - 5x + 7$ at $x = 2.5$ in Horner's nested form $P(2.5) = (((4(2.5) - 3)(2.5) + 2)(2.5) - 5)(2.5) + 7$ requires zero parentheses and zero memory registers, and you can execute it on the SC-32 in **two complementary ways** depending on whether you want a two-register accumulator or a four-register automatic constant dispenser:

1. **Method A — Running Accumulator in Register $X$ (Using Only Registers $X$ and $Y$):** When $x = 2.5$ is short to key in, we accumulate the Ruffini-Horner synthetic-division coefficients directly in Register $X$ while leaving Registers $Z$ and $T$ at zero:
   * **First Horner Stage ($b_3$):** Multiplying the leading coefficient by $x$ ($4 \times 2.5 = 10.0000$) and subtracting $3$ forms the first synthetic-division quotient coefficient $b_3 = 4(2.5) - 3 = \mathbf{7.0000}$ in Register $X$.
   * **Second Horner Stage ($b_2$):** Multiplying by $2.5$ (which lifts $7.0000$ transiently into Register $Y$ and forms $17.5000$) and adding $2$ produces the second quotient coefficient $b_2 = 7.0(2.5) + 2 = \mathbf{19.5000}$ in Register $X$.
   * **Third Horner Stage ($b_1$):** Multiplying by $2.5$ and subtracting $5$ yields the linear quotient coefficient $b_1 = 19.5(2.5) - 5 = \mathbf{43.7500}$ in Register $X$.
   * **Final Remainder ($b_0 = P(2.5)$):** One final multiply-and-add step ($43.75 \times 2.5 + 7$) completes the polynomial remainder:
     * **Keystrokes:** `{{res:sc32_07_polynomials_brent_solver_seq_01:keys}}` $\longrightarrow$ $P(2.5) =$ **`{{res:sc32_07_polynomials_brent_solver_seq_01:value}}`** (**$116.3750$**).
2. **Method B — Flooding All Four Stack Registers (`2.5 ENTER ENTER ENTER`):** Why type `2.5` four separate times—or worse, re-type a long transcendental evaluation point like $x = 2.718281828$—when the top of the four-level stack is a sticky constant dispenser? If you first fill all four registers $(T, Z, Y, X)$ with $x$ by pressing `2.5 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}`, then every time `{{key:×}}` consumes the copy of $x$ in Register $Y$ and drops the stack, **Register $T$ automatically clones a fresh copy of $x = 2.5$ downward into Register $Z$**! You start with `4 × 3 -` ($\to 7.0000$ in $X$, with $2.5$ already waiting in $Y, Z, T$), and then stream `× 2 + × 5 - × 7 +` ($\to \mathbf{116.3750}$) without ever re-typing `2.5` once!

That same T-register replication evaluates **Martin Green's solar-cell fill factor** $FF = \frac{v_{\text{oc}} - \ln(v_{\text{oc}} + 0.72)}{v_{\text{oc}} + 1}$ at $v_{\text{oc}} = 25.145$ while typing `25.145` only once: after flooding the stack with three taps of `{{key:ENTER}}`, adding $0.72$, taking `{{key:LN}}`, and subtracting from the waiting copy of $v_{\text{oc}}$ in Register $Y$ forms the numerator $21.8921$ in Register $X$, while a fresh copy of $v_{\text{oc}}$ drops into Register $Y$ ready for `{{key:x⇄y}}`, $+ 1$, and `{{key:÷}}` to resolve **$FF = 0.837334$**. Similarly, for the coupled-oscillator **biquadratic** $x^4 - 10x^2 + 9 = 0$ ($u = x^2$), evaluating the quadratic radical $\sqrt{\Delta} = \sqrt{10^2 - 4(9)} = 8.0000$ on the stack and pairing it with $10$ via `{{key:LASTX}}` forms $10 \pm 8 = \{18.0000, 2.0000\}$ across Registers $Y$ and $X$; halving both roots ($u_1 = 9, u_2 = 1$) and taking `{{key:√x}}` leaves both positive normal-mode frequencies side by side on the stack ($Y = \mathbf{1.0000},\; X = \mathbf{3.0000}$).

---

### Cardano's Analytical Cubic & Quadratic Solver

Pressing `{{key:POLY}}` (Right Shift `{{key:↱}}` above `{{key:XEQ}}`) opens the analytical polynomial solver for $Ax^3 + Bx^2 + Cx + D = 0$:

| Interface Element | Display Legend / Key Assignment | Functional Action / Internal Allocation |
| :--- | :--- | :--- |
| **Menu Prompt** | `Ax^3 + Bx^2 + Cx + D = 0` | Prompts for polynomial coefficient entry |
| **LFU Softkeys** | `{{key:A}} {{key:B}} {{key:C}} {{key:D}} {{key:EXEC}} {{key:CLR}}` | Softkey assignments for coefficient entry and execution |
| **Internal Storage: Root 1** | Variables `"1"` (Real), `"2"` (Imaginary) | Stores first calculated root (also placed in Registers $Y$ and $X$) |
| **Internal Storage: Root 2** | Variables `"3"` (Real), `"4"` (Imaginary) | Stores second calculated root |
| **Internal Storage: Root 3** | Variables `"5"` (Real), `"6"` (Imaginary) | Stores third calculated root |

Any unentered coefficient defaults to $0.0$ (at least one of $A$ or $B$ must be non-zero, otherwise `{{key:EXEC}}` displays `A ≠ 0`). Five analytical benchmarks inside `{{key:POLY}}` show how the solver handles real, complex, and repeated roots.

Our first test is a *casus irreducibilis* **cubic with three distinct real roots**: the factored benchmark $(x - 1)(x - 2)(x - 3) = x^3 - 6x^2 + 11x - 6 = 0$, where $\Delta < 0$ and `{{key:POLY}}` applies François Viète's trigonometric cosine trisection.

Inside `{{key:POLY}}`, load the four coefficients $A = 1$, $B = -6$, $C = 11$, and $D = -6$ onto their top-row softkeys, then press `{{key:EXEC}}` to project the three unit-circle vertices onto the real axis:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Coefficient $A = 1.0$ |
| `6 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-6.0000$ | Coefficient $B = -6.0$ |
| `11 {{key:C}}` | $0.0000$ | $1.0000$ | $-6.0000$ | $11.0000$ | Coefficient $C = 11.0$ |
| `6 {{key:+/-}} {{key:D}}` | $1.0000$ | $-6.0000$ | $11.0000$ | $-6.0000$ | Coefficient $D = -6.0$ |
| `{{key:EXEC}}` | $1.0000$ | $-6.0000$ | **$1.000000$** | **$0.000000$** | Primary root $r_1 = 1.0 + 0.0i$ in $(Y, X)$; roots $1, 2, 3$ in vars `1`–`6` |

Here `{{key:EXEC}}` sorts all three real roots in ascending order ($r_1 = 1.0$ in variables `1, 2`, $r_2 = 2.0$ in variables `3, 4`, and $r_3 = 3.0$ in variables `5, 6`), while placing the real part of $r_1$ in Register $Y$ and its zero imaginary part in Register $X$.

In the positive-discriminant regime ($\Delta > 0$), a **cubic with complex conjugate roots** such as $x^3 - x^2 + x - 1 = (x - 1)(x^2 + 1) = 0$ crosses the horizontal axis only once at $r_1 = 1.0$, pairing that real intercept with the pure imaginary roots $r_{2,3} = 0.0 \pm 1.0i$. Loading its four alternating coefficients inside `{{key:POLY}}` separates the real crossing on the stack from the complex conjugate pair stored in the numbered registers:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Coefficient $A = 1.0$ |
| `1 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-1.0000$ | Coefficient $B = -1.0$ |
| `1 {{key:C}}` | $0.0000$ | $1.0000$ | $-1.0000$ | $1.0000$ | Coefficient $C = 1.0$ |
| `1 {{key:+/-}} {{key:D}}` | $1.0000$ | $-1.0000$ | $1.0000$ | $-1.0000$ | Coefficient $D = -1.0$ |
| `{{key:EXEC}}` | $1.0000$ | $-1.0000$ | **$1.000000$** | **$0.000000$** | Real $r_1=1$ in $Y$, Imag $r_1=0$ in $X$; conjugate pair $\pm i$ in vars `3`–`6` |

Recalling `{{key:RCL}} 3` and `{{key:RCL}} 4` returns the real and imaginary parts $0.0000$ and $+1.0000$ of $r_2 = +i$, while `{{key:RCL}} 5` and `{{key:RCL}} 6` return $0.0000$ and $-1.0000$ for its conjugate $r_3 = -i$.

At the critical-damping boundary $\Delta = 0$—represented by the third-order RLC filter polynomial $s^3 + 12s^2 + 45s + 50 = (s+2)(s+5)^2 = 0$—the solver stores both copies of the double pole ($-5.0, -5.0$) and the simple pole ($-2.0$) across variables `1`, `3`, and `5`, while placing the first sorted real root in $(Y = -5.000000,\; X = 0.000000)$ (`{{res:sc32_07_polynomials_brent_solver_seq_10:keys}}` $\longrightarrow$ **`{{res:sc32_07_polynomials_brent_solver_seq_10:value}}`**).

For the **3D Cauchy principal stress eigenvalues** ($\lambda^3 - 70\lambda^2 + 1175\lambda - 5750 = 0$) of a structural steel element with tensor invariants $I_1 = 70\text{ MPa}$, $I_2 = 1175\text{ MPa}^2$, and $I_3 = 5750\text{ MPa}^3$, the symmetry of Cauchy's stress tensor guarantees that $\det(\boldsymbol{\sigma} - \lambda\mathbf{I}) = 0$ lies in *casus irreducibilis* ($\Delta \le 0$). Because all three eigenvalues $\sigma_3 \le \sigma_2 \le \sigma_1$ are real, loading those invariants into `{{key:POLY}}` with `{{res:sc32_07_polynomials_brent_solver_seq_12:keys}}` isolates the major principal stress **`{{res:sc32_07_polynomials_brent_solver_seq_12:value}}` MPa** in Variable `5`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:A}} 70 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-70.0000$ | Coefficients $A, B = -I_1$ |
| `1175 {{key:C}} 5750 {{key:+/-}} {{key:D}}` | $1.0000$ | $-70.0000$ | $1175.0000$ | $-5750.0000$ | Coefficients $C = I_2, D = -I_3$ |
| `{{key:EXEC}}` | $1.0000$ | $-70.0000$ | **$10.000000$** | **$0.000000$** | Minor stress $\sigma_3 = 10.0$ in $Y$; $\sigma_2, \sigma_1$ in vars `3`, `5` |
| `{{key:RCL}} 5` | $-70.0000$ | $10.0000$ | $0.0000$ | **$48.027756$** | Recall major principal stress $\sigma_1$ into Register $X$ |

Once $\sigma_1 = 48.0278\text{ MPa}$ is in Register $X$ and $\sigma_3 = 10.0000\text{ MPa}$ is in Register $Z$, keying `{{key:R↓}} {{key:x⇄y}} {{key:-}} 2 {{key:÷}}` yields Henri Tresca's **maximum shear stress** $\tau_{\max} = \frac{1}{2}(\sigma_1 - \sigma_3) = \mathbf{19.0139\text{ MPa}}$!

Determining **Archimedes' floating oak sphere draft** ($h^3 - 1.5h^2 + 0.325 = 0$) for a solid oak marine buoy of radius $R = 0.50\text{ m}$ ($1.00\text{ m}$ diameter) and specific gravity $\rho_s/\rho_w = 0.65$ floating in freshwater substitutes $R = 0.50$ and $\rho_s/\rho_w = 0.65$ into $h^3 - 3Rh^2 + 4(\rho_s/\rho_w)R^3 = 0$. Inside `{{key:POLY}}`, the sequence `{{res:sc32_07_polynomials_brent_solver_seq_13:keys}}` identifies the physical waterline draft **`{{res:sc32_07_polynomials_brent_solver_seq_13:value}}` m** in Variable `3`—showing that $60.14\%$ of the buoy's diameter sits submerged, while the algebraic companion roots $-0.4123\text{ m}$ and $1.3109\text{ m}$ lie outside the physical sphere $[0, 1.00\text{ m}]$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1 {{key:A}} 1.5 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $1.0000$ | $-1.5000$ | Load cubic and quadratic coefficients $A = 1.0,\; B = -1.5$ |
| `0 {{key:C}} 0.325 {{key:D}}` | $1.0000$ | $-1.5000$ | $0.0000$ | $0.3250$ | Load linear and constant coefficients $C = 0.0,\; D = 0.325$ |
| `{{key:EXEC}}` | $1.0000$ | $-1.5000$ | $-0.412257$ | $0.0000$ | Solve cubic; real parts of 3 roots stored in Variables `1`, `3`, `5` |
| `{{key:RCL}} 3` | $-1.5000$ | $-0.412257$ | $0.0000$ | **$0.601390$** | Recall physical immersion depth $h \in [0, 2R]$ from Variable `3` |

Solving the **Tartaglia-Galileo ballistic trajectory quadratic** ($360.3673 u^2 - 1200u + 510.3673 = 0$) for an elevated target at horizontal range $x = 1,200\text{ m}$ and height $y = 150\text{ m}$ with muzzle speed $v_0 = 140\text{ m/s}$ ($\frac{gx^2}{2v_0^2} = 360.3673\text{ m}$) highlights two ways to handle a quadratic $a u^2 + b u + c = 0$ inside `{{key:POLY}}`. You can either set the cubic coefficient $A = 0$ (`0 {{key:A}}`) and load $(B = a,\; C = b,\; D = c)$ to solve $Bx^2 + Cx + D = 0$, or map the coefficients into $(A = a,\; B = b,\; C = c,\; D = 0)$ to solve $u(a u^2 + b u + c) = 0$, parking a dummy root at $u = 0$ in Variable `1` and placing the two quadratic roots in Variables `3` and `5`. With the shifted $D = 0$ layout, `{{res:sc32_07_polynomials_brent_solver_seq_02:keys}}` recovers the low direct-fire angle **`{{res:sc32_07_polynomials_brent_solver_seq_02:value}}`°** before `{{key:RCL}} 5 {{key:ATAN}}` reveals the high mortar arc:

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

Before turning to transcendental functions, we can compare `{{key:SOLVE}}` and `{{key:POLY}}` side by side on two famous cubics—remembering that inside `{{key:EQN}}`, recalling a variable letter automatically lifts the stack, whereas two consecutive numeric literals require `{{key:ENTER}}` between them so their digits do not concatenate.

Take **John Wallis and Isaac Newton's 1669 cubic benchmark** ($x^3 - 2x - 5 = 0$), the equation Newton solved by hand starting from $x_0 = 2$ to demonstrate his tangent-line method. Why did Cardano's formula feel so cumbersome here? Because $p = -2$ and $q = -5$ give a positive discriminant $\Delta = (-5/2)^2 + (-2/3)^3 = \frac{625}{100} - \frac{8}{27} = \frac{643}{108} > 0$, forcing you to evaluate the sum of two nested cube roots $\sqrt[3]{\frac{5}{2} + \sqrt{\frac{643}{108}}} + \sqrt[3]{\frac{5}{2} - \sqrt{\frac{643}{108}}}$. In `{{key:EQN}}`, by contrast, you write the residual $f(x) = x^3 - 2x - 5 = (x^2 - 2)x - 5$ directly in Horner nested form as `X x² 2 - X × 5 -`.

At $x = 2$, $f(2) = 8 - 4 - 5 = -1 < 0$; at $x = 3$, $f(3) = 27 - 6 - 5 = +16 > 0$. You can either place the two-guess bracket $[2, 3]$ on $(Y, X)$ via `2 {{key:ENTER}} 3 {{key:SOLVE}} X`, or store Newton's single seed `2 {{key:STO}} X` and press `SOLVE X`. Phase 1 marches outward to cage the sign change, and Phase 2's inverse quadratic interpolation sprints to the root $x^* = \mathbf{2.0945514815}$ in Register $X$ while lifting the starting seed $2.0000$ into Register $Y$ (with $Z = 0.0000$ and `{{key:XEQ}}` confirming a machine-zero residual $|f(x^*)| < 10^{-15}$).

Next, **Johannes Diderik van der Waals's real-gas cubic** models carbon dioxide ($\text{CO}_2$, with intermolecular attraction parameter $a = 3.59\text{ L}^2\cdot\text{atm/mol}^2$ and molecular co-volume $b = 0.0427\text{ L/mol}$) compressed to $P = 50\text{ atm}$ at $T = 300\text{ K}$, where $RT = 24.618\text{ L}\cdot\text{atm/mol}$. Clearing the $V^2$ denominator from $\left(P + \frac{a}{V^2}\right)(V - b) = RT$ yields the expanded cubic $50V^3 - 26.753V^2 + 3.59V - 0.153293 = 0$. Inside `{{key:POLY}}`, loading those four coefficients (`{{res:sc32_07_polynomials_brent_solver_seq_09:keys}}`) populates all four stack registers and finds the real molar volume **`{{res:sc32_07_polynomials_brent_solver_seq_09:value}}` L/mol**—some $27\%$ denser than the ideal-gas prediction $V_{\text{ideal}} = RT/P = 0.4924\text{ L/mol}$ because intermolecular attraction pulls the $\text{CO}_2$ molecules together at $50\text{ atm}$, and matching to the last decimal place the $V_m = \mathbf{0.358736\text{ L/mol}}$ obtained by entering the unexpanded physical balance `(50 + 3.59/V^2)(V - 0.0427) - 24.618` directly into `{{key:EQN}}` and running `0.49 {{key:STO}} V {{key:SOLVE}} V`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `50 {{key:A}}` | $0.0000$ | $0.0000$ | $0.0000$ | $50.0000$ | Coefficient $A = 50.0$ |
| `26.753 {{key:+/-}} {{key:B}}` | $0.0000$ | $0.0000$ | $50.0000$ | $-26.7530$ | Coefficient $B = -26.753$ |
| `3.59 {{key:C}}` | $0.0000$ | $50.0000$ | $-26.7530$ | $3.5900$ | Coefficient $C = 3.59$ |
| `0.153293 {{key:+/-}} {{key:D}}` | $50.0000$ | $-26.7530$ | $3.5900$ | $-0.153293$ | Coefficient $D = -0.153293$ |
| `{{key:EXEC}}` | $50.0000$ | $-26.7530$ | **$0.358736$** | **$0.000000$** | Real root in $Y$, Imag in $X$ |
| `{{key:x⇄y}}` | $50.0000$ | $-26.7530$ | $0.000000$ | **$0.358736$** | Molar volume $V_m$ in Register $X$ |

Where Brent's `{{key:SOLVE}}` engine becomes irreplaceable is on **implicit transcendental conservation laws**, where the unknown is trapped simultaneously inside two incompatible mathematical operations. Notice why these single-seed or two-guess `SOLVE` runs don't need repetitive two-row stack tables: once you write the residual $f(x) = \text{LHS} - \text{RHS} = 0$ in `{{key:EQN}}` and choose a physically sensible seed or bracket $[a, b]$ on $(Y, X)$, `SOLVE` always returns the same clean diagnostic frame—the converged root $x^*$ in **Register $X$**, your starting guess (or bracket partner) lifted into **Register $Y$**, and your prior stack preserved in **Registers $Z$ and $T$**, ready for an instant **`{{key:XEQ}}`** residual verification ($|f(x^*)| \le 10^{-12}$):

* **Cyril Colebrook's Turbulent Pipe Friction Factor ($f = 0.022204$):** In commercial steel piping at Reynolds number $\text{Re} = 100,000$ and relative roughness $\varepsilon/D = 0.001$, the Darcy-Weisbach friction factor $f$ resists closed-form inversion because $\sqrt{f}$ appears both outside the base-$10$ logarithm as transmission resistance $1/\sqrt{f}$ and inside the logarithm as the viscous sublayer thickness $2.51/(\text{Re}\sqrt{f})$:
  $$g(f) = \frac{1}{\sqrt{f}} + 2.0\log_{10}\!\left(\frac{\varepsilon/D}{3.7} + \frac{2.51}{\text{Re}\sqrt{f}}\right) = 0$$
  * **Setup & Keystrokes:** Store `F √x 1/x  0.001 ENTER 3.7 ÷  2.51 ENTER 100000 ÷ F √x ÷ + LOG 2 × +` in `{{key:EQN}}`. Because $1/\sqrt{f}$ blows up as $f \to 0^+$ and $\sqrt{f}$ is undefined for $f < 0$, seed `F` inside the physical Moody turbulent range $[0.008, 0.08]$ (or bracket `0.01 {{key:ENTER}} 0.05` on $Y, X$). Keying `0.02 {{key:STO}} F {{key:SOLVE}} F` lifts $0.0200$ into Register $Y$ and converges in milliseconds to $f^* = \mathbf{0.022204}$ in Register $X$.
* **Johannes Kepler's Elliptical Orbital Anomaly ($E = 1.488665\text{ rad}$):** Tracking an Earth-observation satellite along an elliptical orbit of eccentricity $e = 0.25$ at mean clock anomaly $M = 1.20\text{ rad}$ in `{{key:RAD}}` mode requires solving $f(E) = E - 0.25\sin E - 1.20 = 0$. Since $|\sin E| \le 1$, the physical root is always trapped inside $[M - e,\; M + e] = [0.95,\; 1.45]\text{ rad}$.
  * **Setup & Keystrokes:** Store `E  0.25 ENTER E SIN × - 1.20 -` in `{{key:EQN}}`, then seed the mean anomaly via `1.20 {{key:STO}} E {{key:SOLVE}} E` to lock onto $E^* = \mathbf{1.488665\text{ rad}}$ ($85.294^\circ$) in five iterations.
* **William Shockley's Silicon Diode Load Line ($V_D = 0.672944\text{ V}$):** When a $V_s = 5.0\text{ V}$ DC supply drives a silicon junction diode ($I_s = 10^{-12}\text{ A}$, thermal voltage $V_T = 0.02585\text{ V}$) through an $R = 1\text{ k}\Omega$ series load resistor ($I_s R = 10^{-9}\text{ V}$), Kirchhoff's voltage law $5.0 - 1000\,I_D - V_D = 0$ pits a linear resistor droop against an exponential current wall:
  $$f(V) = 5.0 - 10^{-9}\left(e^{V/0.02585} - 1\right) - V = 0$$
  If an unguarded Newton solver starts at $V_0 = 0\text{ V}$, the flat diode slope flings the next guess to $V_1 = +5.0\text{ V}$, where $e^{5.0 / 0.02585} = e^{193.4} \approx 10^{84}$!
  * **Setup & Keystrokes:** Store `5  V 0.02585 ÷ eˣ 1 - 1E-9 × -  V -` in `{{key:EQN}}`, then seed near the physical silicon turn-on knee via `0.65 {{key:STO}} V {{key:SOLVE}} V` (or bracket `[0.5, 0.8]` on $Y, X$) to pin down $V_D^* = \mathbf{0.672944\text{ V}}$ (loop current $I_D = 4.3271\text{ mA}$).
* **Open-Channel Froude Critical Depth ($y_c = 1.258641\text{ m}$):** When $Q = 20.0\text{ m}^3/\text{s}$ ($Q^2 = 400$) of floodwater rushes through a trapezoidal concrete spillway of bottom width $b = 3.0\text{ m}$ and side slopes $z = 2.0$, the critical depth $y_c$ where the surface wave speed matches the flow velocity ($\text{Fr} = 1$) satisfies $f(y) = Q^2 T(y) - g A(y)^3 = 400(3 + 4y) - 9.81(3y + 2y^2)^3 = 0$—a sixth-degree polynomial that lies beyond Abel and Galois's degree-4 radical limit and beyond degree-3 `{{key:POLY}}`.
  * **Setup & Keystrokes:** Record the factored balance `3 ENTER 4 ENTER Y × + 400 ×  3 ENTER Y ×  Y x² 2 × + 3 yˣ 9.81 × -` directly in `{{key:EQN}}`, then key `1.0 {{key:STO}} Y {{key:SOLVE}} Y` to converge to $y_c^* = \mathbf{1.258641\text{ m}}$.
* **Selecting Physical Branches in Multi-Root Equations (Nuclear Buckling & De Laval Nozzles):** Whenever a transcendental equation possesses multiple roots across separate physical regimes, your starting seed or $(Y, X)$ bracket determines which branch `{{key:SOLVE}}` locks onto:
  * **Nuclear Critical Buckling Radius:** For a spherical fission reactor core whose radial neutron flux vanishes at $\sin(0.045 R) = 0$ in `{{key:RAD}}` mode, storing `R 0.045 × SIN` in `{{key:EQN}}` and seeding `60 {{key:STO}} R {{key:SOLVE}} R` isolates the fundamental buckling mode $0.045 R = \pi$ at **$R_{\text{crit}} = 69.813170\text{ cm}$** (avoiding the trivial origin $R = 0$).
  * **Aurel Stodola's De Laval Rocket Nozzle:** The area-Mach relation $\frac{1}{M}\left(\frac{1 + 0.2M^2}{1.2}\right)^3 - 2.50 = 0$ for area ratio $A/A^* = 2.50$ and $\gamma = 1.4$—entered in `{{key:EQN}}` as `M x² 0.2 × 1 + 1.2 ÷ 3 yˣ M ÷ 2.50 -`—has two positive roots separated by the sonic throat $M = 1$. Seeding above the throat via `2.5 {{key:STO}} M {{key:SOLVE}} M` (or bracketing `1.1 ENTER 4.0` on $Y, X$) converges to the **supersonic rocket exhaust branch** **$M_{\text{sup}} = 2.442804$**, while seeding below the throat via `0.2 {{key:STO}} M {{key:SOLVE}} M` (or bracketing `0.05 ENTER 0.95`) isolates the **subsonic diffuser branch** **$M_{\text{sub}} = 0.239541$**.

### Editing & Solving a Piecewise Equation in EQN Mode (`x?0` & `x?y`)

In a spacecraft payload isolation mount, a primary coil spring of stiffness $k_1 = 2,000\text{ N/m}$ carries the load up to a clearance gap $x_0 = 0.05\text{ m}$ ($50\text{ mm}$), where a secondary elastomer bump-stop of stiffness $k_2 = 8,000\text{ N/m}$ engages—producing the **piecewise bilinear force law**:

$$F(x) = 2000x + 8000\langle x - 0.05 \rangle_+ = 2000x + 8000(x - 0.05)\cdot[x - 0.05 > 0]$$

To find the exact deflection $x^*$ under a static payload of $F_{\text{target}} = 350\text{ N}$, press `{{key:EQN}}` (Right Shift `{{key:↱}}` above `{{key:STO}}`), tap `NEW` (`{{key:LFU0}}`), press `A` for `00 LBL A`, and enter the residual $F(x) - 350$ using the three-step Macaulay ramp idiom (`{{key:ENTER}} {{key:x>0}} {{key:×}}`, accessing `{{key:x>0}}` via `{{key:x?0}}` on Right Shift `{{key:↱}}` above `{{key:÷}}`):

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

The table below summarizes the post-`{{key:SOLVE}}` stack state and William Kahan's residual verification workflow:

| Stack / Action | Post-`{{key:SOLVE}}` Contents | Engineering Diagnostic Interpretation |
| :---: | :--- | :--- |
| **Register $X$** | **Converged Root Estimate ($x^*$)** | The final root estimate where $f(x^*)$ crosses or touches zero, also written into the target variable (`A`–`Z`). |
| **Register $Y$** | **Starting Seed or Upper Bracket Bound** | Lifted from Register $X$ when `{{key:SOLVE}}` pushes the converged root $x^*$ onto the stack. |
| **Registers $Z, T$** | **Prior Stack Context (Preserved)** | Any values previously in Registers $Y$ and $Z$ lift into $Z$ and $T$ undisturbed. |
| **`{{key:XEQ}}` Residual Audit** | **Evaluated Function Residual ($f(x^*)$)** | Because $x^*$ is already stored in your equation's target variable, pressing `{{key:XEQ}}` evaluates $f(x^*)$: a true root yields $\lvert f(x^*) \rvert \le 10^{-12}$, whereas an accidental vertical asymptote/pole exposes itself with $\lvert f(x^*) \rvert \gg 1$. |

### Practical Root-Finding Strategy: Bracket Seeding, Multiple Roots & Deflation on the Stack

When tackling unfamiliar nonlinear equations in the lab or field, four practical stack habits make `{{key:POLY}}` and `{{key:SOLVE}}` bulletproof:

1. **Verifying `{{key:POLY}}` Roots via Viète's Sum-and-Product Checksums:**
   Whenever `{{key:POLY}}` writes the three roots of $Ax^3 + Bx^2 + Cx + D = 0$ into variables `1` (Real 1), `3` (Real 2), and `5` (Real 3), you can verify the trace and determinant in six keystrokes:
   * Keying `{{key:RCL}} 1 {{key:RCL}} 3 {{key:+}} {{key:RCL}} 5 {{key:+}}` must equal $-B/A$ (for our stress tensor cubic $\lambda^3 - 70\lambda^2 + 1175\lambda - 5750 = 0$, $10.0 + 11.972244 + 48.027756 = \mathbf{70.000000}$).
   * Keying `{{key:RCL}} 1 {{key:RCL}} 3 {{key:×}} {{key:RCL}} 5 {{key:×}}` must equal $-D/A$ ($10.0 \times 11.972244 \times 48.027756 = \mathbf{5750.0000}$).
   * And when a cubic has complex conjugate roots $r_{2,3} = \alpha \pm i\beta$ stored in variables `3, 4` and `5, 6`, keying `{{key:RCL}} 4 {{key:RCL}} 3 {{key:▸θ,r}}` (Left Shift `{{key:↰}}` above `{{key:4}}`) converts $(\text{Re}, \text{Im})$ into the polar modulus $|r_2| = \sqrt{\alpha^2 + \beta^2}$ in Register $X$ and phase angle $\theta$ in Register $Y$.
2. **Isolating Specific Branches of Multi-Root Transcendental Equations:**
   Many physical conservation laws have two or more physically meaningful branches—such as the low direct-fire mortar angle vs. high plunging mortar angle, the subsonic vs. supersonic branches of Stodola's rocket nozzle Area-Mach relation ($M^* = 1$ throat sonic point separating $M_{\text{sub}} \in (0, 1)$ from $M_{\text{sup}} > 1$), or the subcritical vs. supercritical conjugate depths in open-channel hydraulics. Whenever an equation has multiple roots, place two bracket bounds $(a, b)$ in Registers $Y$ and $X$ that straddle ONLY the branch you want (for example, `0.05 {{key:ENTER}} 0.95` for the subsonic nozzle branch, or `1.05 {{key:ENTER}} 4.0` for the supersonic nozzle branch) so Brent's solver is locked inside that branch from iteration zero.
3. **Deflating Known Roots to Hunt Additional Roots (`(x - r₁)` Division):**
   Suppose you have isolated a first root $r_1$ of a transcendental or high-degree equation $f(x) = 0$, stored it in Variable `A`, and now wish to hunt for a second root $r_2$ without falling back into the basin of attraction of $r_1$. Appending `X {{key:RCL}} A {{key:-}} {{key:÷}}` to the end of your equation in `{{key:EQN}}` forms the deflated function $g(x) = \frac{f(x)}{x - r_1}$, dividing out the zero at $r_1$.
4. **Recognizing `NO ROOT FND` (Code 08) & Tangent Extrema:**
   If a curve $f(x)$ stays strictly positive everywhere—such as $f(x) = x^2 + 4 = 0$, which has only complex roots $\pm 2i$—Phase 1's outward golden-ratio search terminates after 50 expansion steps and displays **`NO ROOT FND`** (Code 08, cleared via `{{key:C}}`). Conversely, when a curve kisses the axis tangentially at an even-multiplicity root such as $f(x) = (x - 3)^2 = 0$, Brent's solver flags the tangent minimum once $|b - a| < 10^{-12}$ and $|f(b)| < 10^{-7}$, or you can bypass the $\varepsilon_{\text{mach}}^{1/m}$ conditioning plateau altogether by solving the derivative $f'(x) = 0$ instead.

---

### From Where a Curve Crosses Zero to How Fast It Moves

Pinpointing the deflection $x^* = 0.0750\text{ m}$ where our spacecraft payload spring balances a $350\text{ N}$ load—or the Mach number $M_{\text{sup}} = 2.442804$ inside a De Laval rocket nozzle—answers a static equilibrium question: *where* does a continuous curve $f(x)$ cross a target threshold? Yet knowing where a curve sits at equilibrium is only the beginning of physics. What happens when we ask how fast a rising Saturn V rocket is accelerating at this microsecond (its instantaneous slope, or **derivative**, $\frac{df}{dx}$), or how much total distance, work, or impulse has accumulated underneath the curve from $x = a$ to $x = b$ (its curved area, or **definite integral**, $\int_a^b f(x)\,dx$)?

And what do we do when the curve whose area we need to measure—like the large-angle swing of a pendulum or a rocket shedding fifteen tons of propellant per second—has no elementary antiderivative in any calculus textbook? In **[Chapter 8: Slicing Infinity: From Archimedes and Saturn V to Romberg's 4/3 − 1/3 Miracle](08-calculus-romberg-quadrature.md)**, we step into the twin engines of calculus and discover how a deceptively simple $\frac{4}{3} - \frac{1}{3}$ weighting trick melts away numerical approximation error.
