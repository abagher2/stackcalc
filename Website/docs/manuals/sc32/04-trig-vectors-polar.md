---
title: "Chapter 4: Measuring the Cosmos with a Shadow | Thinking in the Stack (SC-32)"
description: "Direct and inverse trigonometry, hyperbolic functions, exact axial angle clamping, polar-to-rectangular 2D vector conversions, and geodetic traverses on the StackCalc SC-32."
---

# Chapter 4: Measuring the Cosmos with a Shadow

## A Stick in Alexandria and the Birth of the Unit Circle

At local solar noon on the summer solstice of 240 BCE, Eratosthenes of Cyrene—chief librarian of the Great Library of Alexandria—walked out into a sunlit courtyard and measured the shadow of an upright bronze rod called a *gnomon*. As preserved in Cleomedes' astronomical treatise *The Heavens* {{cite:cleomedes2004}}, travelers had brought Eratosthenes a curious report from the frontier garrison town of Syene (modern Aswan), some five thousand stadia up the Nile to the south: at midday on the longest day of the year, vertical stone columns in Syene cast no shadow at all, and the reflection of the overhead sun shone straight down to the water at the bottom of a deep vertical well.

Yet at that exact same hour in Alexandria, Eratosthenes saw that his vertical bronze gnomon cast a crisp wedge of shadow across the courtyard paving stones. Measuring the ratio of the shadow's horizontal length to the rod's vertical height, he found that the sun's rays met the upright rod at an angle equal to one-fiftieth of a full circle:

$$\theta = \frac{360^\circ}{50} = 7.2^\circ$$

Why would the sun stand directly overhead in Syene while leaning $7.2^\circ$ south of the zenith in Alexandria? Eratosthenes realized that two assumptions—a flat Earth and a nearby sun—could never explain the discrepancy together. Because the sun is so extraordinarily distant that its rays arrive at every city on Earth as parallel lines, only the curvature of the Earth itself could tilt Alexandria's vertical rod away from Syene's vertical well. By Euclid's theorem on alternate interior angles of parallel lines cut by a transversal, the $7.2^\circ$ shadow angle at the tip of the gnomon in Alexandria had to equal the central angle subtended at the very center of the Earth between Syene and Alexandria! Multiplying the five-thousand-stadia overland distance between the two cities by fifty ($50 \times 5,000 = 250,000\text{ stadia}$, or roughly $40,000\text{ kilometers}$), Eratosthenes measured the circumference of the entire planet to within a percent of modern satellite geodesy—using nothing more than a bronze stick, a shadow, and the geometry of a circle.

Two centuries after Eratosthenes, the astronomer Hipparchus of Nicaea asked how an observer could translate *any* central angle on the celestial sphere into a measurable straight-line distance. He inscribed triangles inside a circle of fixed radius and compiled the ancient world's first table of **chords**—the direct ancestor of the modern sine and cosine functions. Five hundred years later in India, astronomers led by Aryabhata sliced Hipparchus's full chord in half, noticing that the half-chord of a double angle forms the vertical leg of a right triangle inscribed inside a circle of radius $r = 1$. They called that half-chord *jya-ardha* ("half-bowstring"), which Arabic translators rendered as *jiba*, Latin scholars in twelfth-century Toledo mistranslated as *sinus* ("bay" or "fold"), and modern mathematics shortened to **sine**.

Whenever we draw a circle of radius $r = 1$ centered at the origin of an $(x, y)$ coordinate plane—the **Unit Circle**—and sweep a radial pointer counterclockwise from the positive horizontal axis through an angle $\theta$, the tip of that pointer traces out a right triangle whose hypotenuse is $1$:

$$x = \cos\theta \quad (\text{Horizontal Shadow}), \qquad y = \sin\theta \quad (\text{Vertical Height})$$

$$x^2 + y^2 = \cos^2\theta + \sin^2\theta = 1$$

To make that geometry physical during the Middle Ages and the Renaissance, Islamic and European astronomers from al-Biruni to Regiomontanus and Johannes Kepler built brass **astrolabes** and rotating paper **volvelles**: layered circular dials engraved with degree scales around the rim and an orthogonal grid of cosines and sines across the face. Instead of computing five-place series approximations by hand, a navigator could rotate the pointer arm to an angle $\theta$ and read its horizontal and vertical projections directly off the engraved plate.

{{blocks:unit_circle_volvelle_30deg|Orthographic diagram of the Unit Circle Volvelle dialed to 30° (π/6 rad), reading off exact horizontal and vertical projections cos(30°) = √3/2 ≈ 0.8660 and sin(30°) = 1/2 = 0.5000.}}

When you grasp the knurled upper pointer ring of the $120\text{ mm}$ *Unit Circle Volvelle* shown in Figure 4.1 and rotate it counterclockwise from $0^\circ$ to $30^\circ$ ($\pi/6\text{ rad}$), the rotating sight window frames the exact right-triangle projections on the lower stator ring:

$$\cos(30^\circ) = \frac{\sqrt{3}}{2} \approx 0.866025, \qquad \sin(30^\circ) = \frac{1}{2} = 0.500000$$

Dialing further counterclockwise through $45^\circ$ ($\cos 45^\circ = \sin 45^\circ = \sqrt{2}/2 \approx 0.707107$) and $60^\circ$ ($\cos 60^\circ = 1/2$, $\sin 60^\circ = \sqrt{3}/2$) up to $90^\circ$—where the horizontal shadow vanishes ($\cos 90^\circ = 0$) and the vertical height reaches the top of the circle ($\sin 90^\circ = 1$)—reveals why cosine and sine are not abstract power series. They are the horizontal shadow and vertical altitude of a rotating pointer of unit length. And the third fundamental circular ratio, the **tangent** ($\tan\theta = \sin\theta / \cos\theta$), gets its name from the Latin *tangens* ("touching"): it is the vertical height cut off by the extended pointer along the vertical line $x = 1$ that touches the right-hand rim of the unit circle.

### Why Engineering Keeps Three Ways to Slice a Circle

Before evaluating any trigonometric function, a scientist or engineer must answer a deceptively rich historical question: what unit measures a full turn around the unit circle? The StackCalc SC-32 supports all three classical angular conventions, indicated continuously on the top status bar:

| Angular Mode | LCD Annunciator | Full Circle Revolution | Right Angle | Primary Engineering Field |
| :--- | :---: | :---: | :---: | :--- |
| **Degrees** | `DEG` (Default) | $360^\circ$ | $90^\circ$ | Structural Civil Engineering, Geodesy, Avionics |
| **Radians** | `RAD` | $2\pi \approx 6.283185\text{ rad}$ | $\pi/2 \approx 1.570796\text{ rad}$ | Mathematical Physics, Calculus, Wave Mechanics |
| **Gradians** | `GRAD` | $400\text{ grad}$ | $100\text{ grad}$ | European Surveying, Mining Engineering |

Why have all three systems survived into the twenty-first century? Because each grew out of a different physical symmetry:
* **Degrees (`DEG`):** Four thousand years ago, Babylonian astronomers noticed that the sun advances against the background constellations by roughly one step per day over a $360$-day schematic year. Better still for base-$60$ arithmetic, $360$ is an extraordinarily abundant integer—divisible without remainder by $2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120,$ and $180$. That makes it effortless to divide a structural roof truss, a clock face, or a compass rose into halves, thirds, quarters, fifths, sixths, eighths, or twelfths using whole numbers.
* **Radians (`RAD`):** To a mathematician or physicist, dividing a circle into $360$ parts is an arbitrary human convention. Roger Cotes and Leonhard Euler asked a more natural geometric question: how large is the angle $\theta$ when the curved arc length $s$ traced along the rim of a circle equals the straight radius $r$ of the circle itself? Defining an angle as the dimensionless ratio of arc length to radius ($\theta = s / r$) makes one full revolution equal to $2\pi\text{ radians}$ ($\approx 6.283185\text{ rad}$) and one radian equal to $180^\circ / \pi \approx 57.29578^\circ$. Only in radians does the small-angle ratio $\lim_{\theta \to 0} (\sin\theta)/\theta$ equal $1$, ensuring that the derivative of $\sin\theta$ is simply $\cos\theta$ without an awkward $\pi/180$ scale factor trailing behind every harmonic oscillator or electromagnetic wave equation.
* **Gradians (`GRAD`):** During the French Revolution, the architects of the metric system sought to decimalize angles alongside meters and kilograms. By defining a right angle as $100\text{ gradians}$ (*gons*) and a full circle as $400\text{ gradians}$, they linked terrestrial navigation directly to the metric system: because the meter was originally defined as one ten-millionth of the meridian quadrant from the Equator to the North Pole ($10,000\text{ km}$ per $100\text{ grad}$), **one gradian of latitude equals $100\text{ kilometers}$ on the surface of the Earth**, and one centigrad ($0.01\text{ grad}$) equals exactly $1\text{ meter}$.

{{blocks:sc32_rpn_calculation|StackCalc SC-32 Live 4-Level XYZT Stack Hardware Display.}}

The active angular mode tells the SC-32 how to interpret inputs to `{{key:SIN}}`, `{{key:COS}}`, and `{{key:TAN}}`, and what angular units to return from inverse functions (`{{key:ASIN}}`, `{{key:ACOS}}`, `{{key:ATAN}}`) and rectangular-to-polar conversions (`{{key:▸θ,r}}`). Through **`{{key:MODES}}`** (Left Shift `{{key:↰}}` above `{{key:+/-}}`), you can select `{{key:DEG}}`, `{{key:RAD}}`, or `{{key:GRAD}}` at any time. Even better, when a nautical chart, surveyor's plat, or astronomical ephemeris gives an angle in Babylonian sexagesimal **degrees-minutes-seconds** (`D.MMSS`, such as $35^\circ 15' 36''$ entered as `35.1536`), pressing **`{{key:▸HR}}`** (Left Shift `{{key:↰}}` above `{{key:5}}`) converts Register $X$ in place into decimal degrees (`35.2600°`) for trigonometric evaluation, while **`{{key:▸HMS}}`** (Right Shift `{{key:↱}}` above `{{key:5}}`) packs any decimal degree or hour value back into `D.MMSS` format—and **`{{key:▸DEG}}`** / **`{{key:▸RAD}}`** (Left Shift `{{key:↰}}` / Right Shift `{{key:↱}}` above `{{key:6}}`) convert Register $X$ directly between degrees and radians without changing the active angular mode.

| Function | Dedicated Keystroke | Arity | Valid Domain | Output Range (in `{{key:DEG}}`) |
| :--- | :--- | :---: | :---: | :---: |
| **Sine** | `{{key:SIN}}` | Unary | $(-\infty, +\infty)$ | $[-1.0, +1.0]$ |
| **Cosine** | `{{key:COS}}` | Unary | $(-\infty, +\infty)$ | $[-1.0, +1.0]$ |
| **Tangent** | `{{key:TAN}}` | Unary | $\theta \ne 90^\circ + k \cdot 180^\circ$ | $(-\infty, +\infty)$ |
| **Arcsine** | `{{key:ASIN}}` | Unary | $[-1.0, +1.0]$ | $[-90^\circ, +90^\circ]$ |
| **Arccosine** | `{{key:ACOS}}` | Unary | $[-1.0, +1.0]$ | $[0^\circ, 180^\circ]$ |
| **Arctangent** | `{{key:ATAN}}` | Unary | $(-\infty, +\infty)$ | $(-90^\circ, +90^\circ)$ |

### Why Standard Spreadsheets Get $\cos(90^\circ)$ Wrong: Exact Axial Angle Clamping

Try evaluating $\cos(90^\circ)$ on a standard computer spreadsheet or a conventional floating-point calculator, and you will often get a tiny ghost number like $6.123233995736766 \times 10^{-17}$ instead of zero. Why does a $90^\circ$ right angle leave a lingering residual on a modern processor?

Because inside a standard floating-point library, every angle in degrees is first converted into radians by multiplying by $\pi / 180$, so $90^\circ$ becomes an approximation to $\pi / 2$. Since $\pi$ is a transcendental number, its binary representation never terminates; an IEEE 754 double-precision register must truncate $\pi/2$ after 53 binary significand bits, landing at a number that differs from the true mathematical $\pi/2$ by roughly $6.123234 \times 10^{-17}\text{ radians}$. Near $\theta = \pi/2$, the slope of $\cos\theta$ is $-\sin(\pi/2) = -1$, so when the cosine polynomial evaluates that slightly imperfect binary approximation of $\pi/2$, it faithfully returns that exact truncation residual instead of zero! In a structural truss stiffness matrix or an orbital coordinate rotation, a false non-zero residual of $6.12 \times 10^{-17}$ can silently pollute subsequent divisions or prevent zero-detection guards from firing.

To prevent binary radian conversion from corrupting orthogonal geometry, the SC-32 performs **Exact Axial Angle Clamping** before evaluating circular series: in Degrees (`DEG`) or Gradians (`GRAD`) mode, quadrantal multiples of a right angle are reduced exactly modulo a full circle so that $\sin(0^\circ) = 0.0$, $\cos(0^\circ) = 1.0$, $\sin(90^\circ) = 1.0$, $\cos(90^\circ) = 0.0$, $\sin(180^\circ) = 0.0$, $\cos(180^\circ) = -1.0$, $\sin(270^\circ) = -1.0$, and $\cos(270^\circ) = 0.0$ return exact IEEE zero and unity values. Likewise, evaluating $\tan(90^\circ)$ or $\tan(270^\circ)$ immediately triggers `DIVIDE BY 0` (Code 01) rather than returning a bogus $1.63 \times 10^{16}$ reciprocal of rounding noise, and passing a magnitude $|x| > 1$ to `{{key:ASIN}}` or `{{key:ACOS}}` displays `INVALID DATA` (Code 02) while leaving your stack completely intact.

---

## Triangles, Crosswinds & Resolving 2D Vectors

Once you see $\cos\theta$ and $\sin\theta$ as the horizontal and vertical shadows of a tilted arrow, dozens of seemingly unrelated problems across physics, civil surveying, optics, and navigation turn out to be variations on a single theme: splitting a slanted vector into perpendicular components, or reconstructing a slanted vector from its perpendicular parts.

### Projecting Forces, Trajectories & Mountain Summits

In the *Two New Sciences* (1638), Galileo Galilei made a discovery that launched modern mechanics: when a cannonball or an artillery shell flies through the air (neglecting atmospheric drag), its curved parabolic trajectory is actually two simple motions occurring simultaneously at right angles. Horizontally, no force acts on the shell after it leaves the muzzle, so its horizontal velocity $v_{0x} = v_0\cos\theta$ remains constant all the way downrange. Vertically, gravity $g$ pulls downward with constant acceleration, slowing the initial vertical climb rate $v_{0y} = v_0\sin\theta$ until the shell momentarily pauses at its apex altitude $H_{\max}$—where all of its vertical kinetic energy $\frac{1}{2}mv_{0y}^2$ has converted into gravitational potential energy $mgH_{\max}$:

$$H_{\max} = \frac{(v_0 \sin\theta)^2}{2g}, \qquad R = \frac{2 v_{0x} v_{0y}}{g} = \frac{v_0^2 \sin(2\theta)}{g}$$

Notice what that second equation reveals through the double-angle identity $2\sin\theta\cos\theta = \sin(2\theta)$: on level ground, maximum range occurs when $\sin(2\theta) = 1$, or $\theta = 45^\circ$, and any two complementary launch angles that sum to $90^\circ$—such as a low $30^\circ$ flat trajectory and a high $60^\circ$ mortar lob—land at the exact same downrange distance $R$!

That same orthogonal decomposition governs a heavy crate sliding down a ramp inclined at an angle $\theta$ with kinetic friction coefficient $\mu_k$. Gravity pulls straight toward the center of the Earth with force $mg$, but the ramp forces the motion along the tilted surface. Splitting gravity into components parallel and perpendicular to the incline shows that $mg\sin\theta$ pulls the crate downhill while $mg\cos\theta$ presses the crate into the planks, generating a normal force $N = mg\cos\theta$ and an uphill Coulomb friction drag $\mu_k N = \mu_k mg\cos\theta$:

$$a = g (\sin\theta - \mu_k \cos\theta)$$

On the SC-32 stack, notice how `{{key:LASTX}}` lets you evaluate both projections while typing the ramp angle $\theta$ only once: pressing `{{key:SIN}}` replaces $\theta$ in Register $X$ with $\sin\theta$ while saving $\theta$ in `{{key:LASTX}}`, so keying `{{key:LASTX}} {{key:COS}}` immediately forms $\cos\theta$ on Shelf $X$ while $\sin\theta$ waits on Shelf $Y$ (`θ {{key:SIN}} {{key:LASTX}} {{key:COS}} μ {{key:×}} {{key:-}} g {{key:×}}`).

What if you cannot reach the object you want to measure at all? During the Great Trigonometrical Survey of India in the 1850s, surveyors could not carry a measuring chain through the glaciers to the base of Peak XV (Mount Everest). Instead, they used **two-station optical leveling**: sighting the vertical elevation angle $\alpha$ to the mountain summit from Station 1, marching forward a measured horizontal baseline distance $d$ directly toward the peak to Station 2, and sighting the steeper elevation angle $\beta$. Because the unknown horizontal distances from the summit's plumb line to the two stations are $x_1 = H\cot\alpha$ and $x_2 = H\cot\beta$, their difference $x_1 - x_2$ eliminates the inaccessible distance to the mountain completely and leaves only the measured baseline $d$:

$$d = H(\cot\alpha - \cot\beta) \implies H = \frac{d}{\cot\alpha - \cot\beta} = \frac{d}{\frac{1}{\tan\alpha} - \frac{1}{\tan\beta}}$$

Because the keypad needs no dedicated cotangent button when `{{key:1/x}}` sits on the primary plane, you evaluate each cotangent in place via `{{key:TAN}} {{key:1/x}}`, subtract $\cot\beta$ from $\cot\alpha$ on Shelf $X$, type the baseline $d$, and invert the division order with `{{key:x⇄y}} {{key:÷}}`.

Even the ticking of a grandfather clock hides a circular projection: at wider swing amplitudes $\theta_0$, the true restoring force $\sin\theta$ falls slightly below the small-angle approximation $\theta$, stretching the small-angle period $T_0 = 2\pi\sqrt{L/g}$ by the leading half-angle sine factor $T \approx T_0[1 + \frac{1}{4}\sin^2(\theta_0/2)]$ ($+3.66\%$ at $\theta_0 = 45^\circ$). In **Chapter 8**, we will return to Christiaan Huygens's 1656 clockwork discovery and use Romberg numerical integration (`{{key:∫}}`) to integrate the exact complete elliptic integral $K(\sin(\theta_0/2))$ across any swing angle.

### Reversing the Projection: Fiber Optics, Banked Highways & Satellite Orbits

Direct trigonometric functions take an angle and return a dimensionless ratio of lengths; **inverse trigonometric functions** (`{{key:ASIN}}`, `{{key:ACOS}}`, `{{key:ATAN}}`) take a physical ratio of speeds, refractive indices, accelerations, or orbital radii and recover the geometric angle hidden inside:
* **Fiber-Optic Total Internal Reflection (`{{key:ASIN}}`):** When a pulse of laser light travels inside an optical fiber core of refractive index $n_1 = 1.480$ surrounded by a glass cladding of slightly lower refractive index $n_2 = 1.450$, Snell's Law ($n_1\sin\theta_1 = n_2\sin\theta_2$) states that any ray striking the core-cladding boundary bends away from the normal. At the **critical angle** $\theta_c$, the refracted ray skims right along the glass interface at $\theta_2 = 90^\circ$ ($\sin\theta_2 = 1$), so:

  $$\theta_c = \arcsin\left(\frac{n_2}{n_1}\right)$$

  Every light ray striking the wall at an angle steeper than $\theta_c$ cannot escape into the cladding at all; it reflects $100\%$ losslessly back into the core, guiding data pulses across oceans.
* **Banked Highway Curves (`{{key:ATAN}}`):** When an automobile or high-speed train rounds a curve of radius $R$ at speed $v$ on glare ice, lateral tire friction vanishes. By tilting (banking) the roadway cross-slope at an angle $\theta$, civil engineers use the inward horizontal component of the road's normal force ($N\sin\theta = mv^2/R$) to supply the centripetal acceleration while the vertical component ($N\cos\theta = mg$) supports the vehicle's weight. Dividing the horizontal equation by the vertical equation cancels both the vehicle's mass $m$ and the normal force $N$:

  $$\tan\theta = \frac{v^2}{g R} \implies \theta = \arctan\left(\frac{v^2}{g R}\right)$$

  Because mass cancels completely, a fully loaded freight truck and a lightweight passenger sedan traveling at design speed $v$ experience zero side-slip on the exact same banking angle $\theta$.
* **Satellite Ground-Station Look Angle & Gauss's Orbital Anomaly (`{{key:ATAN}}`):** When a satellite orbits at altitude $h$ above an Earth of radius $R_E$ at a central geocentric angle $\gamma$ away from a ground tracking station, resolving the triangle formed by the Earth's center, the ground dish, and the satellite gives the antenna's horizon look-angle elevation $E$:

  $$\tan E = \frac{\cos\gamma - \frac{R_E}{R_E + h}}{\sin\gamma}$$

  And along an elliptical orbit of eccentricity $e$, Carl Friedrich Gauss's half-angle tangent transformation converts Kepler's auxiliary **eccentric anomaly** $E$ (measured from the center of the ellipse) into the true polar angle $\nu$ (**true anomaly**, measured from the gravitating focus) without quadrant ambiguity:

  $$\tan\left(\frac{\nu}{2}\right) = \sqrt{\frac{1 + e}{1 - e}}\tan\left(\frac{E}{2}\right)$$

### Oblique Triangles and the Law of Cosines

In land surveying and wave physics, nature rarely hands us right-angled triangles. Suppose a surveyor stands at a corner monument $C$ and measures straight-line distances $a$ and $b$ to two boundary markers separated by an included angle $C \ne 90^\circ$. How do we find the opposite side $c$ without a right angle?

Drop a perpendicular altitude $h$ from the tip of side $b$ down to side $a$, splitting the oblique triangle into two right triangles:
* The vertical altitude has height $h = b\sin C$.
* The horizontal shadow of side $b$ along side $a$ has length $b\cos C$, leaving $(a - b\cos C)$ as the base of the outer right triangle.

Now apply the ordinary Pythagorean theorem to that outer right triangle, and watch how the unit-circle identity $\cos^2 C + \sin^2 C = 1$ simplifies the algebra:

$$\begin{aligned}
c^2 &= (a - b\cos C)^2 + (b\sin C)^2 \\
&= a^2 - 2ab\cos C + b^2\cos^2 C + b^2\sin^2 C \\
&= a^2 + b^2(\cos^2 C + \sin^2 C) - 2ab\cos C \\
&= a^2 + b^2 - 2ab\cos C
\end{aligned}$$

Taking the square root gives the **Law of Cosines**:

$$c = \sqrt{a^2 + b^2 - 2 a b \cos C}$$

On the SC-32, you never need parentheses or scratch registers to evaluate the Law of Cosines: form the Pythagorean sum $a^2 + b^2$ first (`a {{key:x²}} b {{key:x²}} {{key:+}}`) and let it wait on Shelf $Y$ while you build the cross-term $2ab\cos C$ on Shelf $X$ (`2 {{key:ENTER}} a {{key:×}} b {{key:×}} C {{key:COS}} {{key:×}}`), then finish in two strokes with `{{key:-}} {{key:√x}}`. Notice how this single formula unifies all planar triangles:
* When $C = 90^\circ$, $\cos 90^\circ = 0$ and the cross-term vanishes, recovering the Pythagorean theorem ($c = \sqrt{a^2 + b^2}$).
* When $C < 90^\circ$ (an acute angle), $\cos C > 0$ pulls the third side shorter than a right-triangle hypotenuse.
* When $C > 90^\circ$ (an obtuse angle), $\cos C < 0$ makes $-2ab\cos C$ positive, stretching the third side longer!

Flip the minus sign to a plus sign (the supplementary exterior angle $180^\circ - \Delta\phi$), and the exact same equation governs **coherent wave interference**: when two acoustic or electromagnetic waves of amplitudes $A_1$ and $A_2$ arrive at a sensor with phase difference $\Delta\phi$, their superposed amplitude is the vector resultant of two rotating phasors placed tip-to-tail:

$$A_{\text{resultant}} = \sqrt{A_1^2 + A_2^2 + 2 A_1 A_2 \cos(\Delta\phi)}$$

### The $(Y, X)$ Coordinate Plane: Polar $\leftrightarrow$ Rectangular Vector Conversion

Up to this point in Volume II, every binary key on the SC-32 has treated Registers $Y$ and $X$ as two scalar numbers waiting to be combined into one. When you work with two-dimensional vectors—forces on a physics laboratory force table, aircraft crosswind velocity triangles, land-surveying boundary traverses, or AC electrical power triangles—Registers $Y$ and $X$ take on a unified geometric identity: **together, the $(Y, X)$ register pair forms a two-dimensional coordinate plane**.

The SC-32 provides two dedicated keys that transform the $(Y, X)$ pair in place between Cartesian rectangular coordinates $(x, y)$ and polar coordinates $(r, \theta)$ without disturbing Registers $Z$ and $T$:

| Transformation | Dedicated Keystroke | Stack Input ($Y, X$) | Stack Output ($Y, X$) | Mathematical Formula |
| :--- | :--- | :--- | :--- | :--- |
| **Polar to Rectangular** | `{{key:▸y,x}}` | $Y = \theta$ (Angle in active mode)<br>$X = r$ (Radius / Magnitude) | $Y = y = r \sin\theta$<br>$X = x = r \cos\theta$ | $(x, y) = (r\cos\theta, r\sin\theta)$ |
| **Rectangular to Polar** | `{{key:▸θ,r}}` | $Y = y$ (Orthogonal vertical)<br>$X = x$ (Orthogonal horizontal) | $Y = \theta = \operatorname{atan2}(y, x)$<br>$X = r = \sqrt{x^2 + y^2}$ | $(r, \theta) = (\sqrt{x^2+y^2}, \operatorname{atan2}(y, x))$ |

Look closely at the mnemonic printed directly on the key legends: in `{{key:▸y,x}}`, the first letter after the arrow ($y$) lands in Register $Y$ and the second letter ($x$) lands in Register $X$; in `{{key:▸θ,r}}`, the angle $\theta$ lands in Register $Y$ and the radial magnitude $r$ lands in Register $X$.

Even more importantly, why is `{{key:▸θ,r}}` vastly safer than dividing $y / x$ and pressing `{{key:ATAN}}`? Because a single-argument $\arctan(y/x)$ only sees the *quotient* of $y$ and $x$:
* In Quadrant III, where both $x = -3$ and $y = -4$ are negative, the quotient $(-4)/(-3) = +1.3333$ is positive, so $\arctan(y/x)$ blindly returns $+53.1301^\circ$ (Quadrant I)—an error of $180^\circ$!
* Worse yet, on the positive or negative vertical axis where $x = 0$ and $y = \pm 10$, dividing $y/x$ crashes with `DIVIDE BY 0`!

By contrast, `{{key:▸θ,r}}` evaluates the full **four-quadrant $\operatorname{atan2}(y, x)$ function**, inspecting the separate signs of $y$ in Register $Y$ and $x$ in Register $X$ across the entire $(-180^\circ, +180^\circ]$ circle:

| Quadrant / Axis | Signs of $(x, y)$ | Four-Quadrant $\operatorname{atan2}(y, x)$ Formula (in `DEG`) | Example Vector $(x, y)$ | Output $(Y = \theta, X = r)$ |
| :--- | :---: | :--- | :---: | :--- |
| **Quadrant I** | $x > 0,\; y \ge 0$ | $\arctan(y/x)$ | $(+3, +4)$ | $\theta = +53.1301^\circ,\; r = 5.0$ |
| **Quadrant II** | $x < 0,\; y \ge 0$ | $\arctan(y/x) + 180^\circ$ | $(-3, +4)$ | $\theta = +126.8699^\circ,\; r = 5.0$ |
| **Quadrant III** | $x < 0,\; y < 0$ | $\arctan(y/x) - 180^\circ$ | $(-3, -4)$ | $\theta = -126.8699^\circ,\; r = 5.0$ |
| **Quadrant IV** | $x > 0,\; y < 0$ | $\arctan(y/x)$ | $(+3, -4)$ | $\theta = -53.1301^\circ,\; r = 5.0$ |
| **Vertical Axes** | $x = 0,\; y \ne 0$ | $+90^\circ$ if $y > 0$, $-90^\circ$ if $y < 0$ | $(0, +10)$ | $\theta = +90.0000^\circ,\; r = 10.0$ |

Let us see how pairing `{{key:▸y,x}}` and `{{key:▸θ,r}}` solves four classic vector problems across physics and engineering:

1. **The AC Power Triangle ($P, Q, S$):** When an inductive AC motor draws current $I_{\text{rms}}$ from a voltage line $V_{\text{rms}}$ with a lagging phase angle $\phi$, the total **apparent power** $S = V_{\text{rms}} I_{\text{rms}}$ (in volt-amperes, $\text{VA}$) is the hypotenuse of a right triangle whose horizontal cosine leg is **real power** $P = S\cos\phi$ (in Watts, which performs mechanical shaft work) and whose vertical sine leg is **reactive power** $Q = S\sin\phi$ (in $\text{VAR}$, which sloshes energy back and forth into the magnetic field each cycle). Loading $\phi$ into $Y$ and $S$ into $X$ and pressing `{{key:▸y,x}}` resolves both $Q$ and $P$ simultaneously.
2. **Aircraft Crosswind Crab-Angle & Wind-Triangle Navigation:** Picture a pilot flying a cross-country leg at true airspeed $V_{\text{air}} = 220\text{ knots}$ on a northeast heading of $45^\circ$ while a $35\text{-knot}$ upper-level crosswind blows from $310^\circ$ (pushing the air mass toward $130^\circ$). Why does an airplane pointed at $45^\circ$ drift sideways across the ground? Because the aircraft moves through an ocean of air that is itself moving over the terrain:

   $$\vec{V}_{\text{ground}} = \vec{V}_{\text{air}} + \vec{V}_{\text{wind}}$$

   Similarly, in high-school and university physics laboratories, students test **static equilibrium on a circular Force Table** by hanging weights from two pulleys at angles $\theta_1$ and $\theta_2$ and finding the exact magnitude and opposite angle of the third "equilibrant" tension vector $\vec{F}_3 = -(\vec{F}_1 + \vec{F}_2)$ needed to center the central brass ring. On the SC-32, both the pilot's wind triangle and the physics force table follow the exact same three-beat rhythm: decompose each polar vector via `{{key:▸y,x}}`, add the $x$- and $y$-components, and recombine via `{{key:▸θ,r}}`.
3. **Land Surveying Closed-Loop Traverses (`{{key:▸y,x}} {{key:Σ+}}`):** What if a land surveyor walks a four-, ten-, or twenty-leg property boundary and needs to sum every course $(r_i, \theta_i)$ around the loop to verify that the horizontal departures ($\Sigma\Delta x$) and vertical latitudes ($\Sigma\Delta y$) close back to zero at the starting iron monument?

   $$\Sigma \Delta x = \sum r_i \cos\theta_i = 0, \qquad \Sigma \Delta y = \sum r_i \sin\theta_i = 0$$

   Here the SC-32 reveals one of its cleanest architectural symmetries: **because `{{key:▸y,x}}` places $\Delta y$ in Register $Y$ and $\Delta x$ in Register $X$, its output matches the exact $(Y, X)$ input convention of the statistical accumulator key `{{key:Σ+}}`**. Chaining `{{key:▸y,x}} {{key:Σ+}}` after each survey leg accumulates the entire boundary traverse in statistical memory without touching a single named storage variable!
4. **Tensor Rotations (Mohr's Circle) & 3D Space-Frame Angles:** When rotating a 2D vector $(x, y)$ through an angle $\Delta\theta$, converting to polar (`{{key:▸θ,r}}`), adding $\Delta\theta$ to the angle in Register $Y$, and projecting back (`{{key:▸y,x}}`) applies the $2\times 2$ orthogonal rotation matrix in six keystrokes. When rotating a second-order planar strain tensor $(\epsilon_x, \epsilon_y, \gamma_{xy})$ measured by an aircraft wing strain-gauge rosette through an angle $\theta$, why does the state point rotate around Christian Otto Mohr's 1882 **Mohr's circle** at the **double angle $2\theta$**? Because projecting both the stress/strain vector *and* the normal area element across $\theta$ produces $\cos^2\theta = \frac{1 + \cos(2\theta)}{2}$ and $\sin\theta\cos\theta = \frac{\sin(2\theta)}{2}$—meaning a $90^\circ$ rotation in physical space ($\epsilon_x \leftrightarrow \epsilon_y$) corresponds to a $180^\circ$ rotation to the opposite side of Mohr's circle about the hydrostatic mean strain $(\epsilon_x + \epsilon_y)/2$:

   $$\epsilon_{x'} = \frac{\epsilon_x + \epsilon_y}{2} + \frac{\epsilon_x - \epsilon_y}{2}\cos(2\theta) + \frac{\gamma_{xy}}{2}\sin(2\theta)$$

   And when a machinist mitre-cuts two skew 3D space-frame struts $\vec{A} = (A_x, A_y, A_z)$ and $\vec{B} = (B_x, B_y, B_z)$, the Cauchy-Schwarz dot product extracts the true spatial intersection angle $\theta$ directly on the stack:

   $$\theta = \arccos\left(\frac{\vec{A} \cdot \vec{B}}{|\vec{A}|\,|\vec{B}|}\right) = \arccos\left(\frac{A_x B_x + A_y B_y + A_z B_z}{\sqrt{A_x^2 + A_y^2 + A_z^2}\sqrt{B_x^2 + B_y^2 + B_z^2}}\right)$$

### Spherical Geodesy, Great-Circle Orthodromes & Avian Celestial Navigation

Once an aircraft, a ship, or a radio link spans thousands of kilometers across an ocean, flat-Earth Cartesian trigonometry breaks down. On a globe of mean radius $R_E = 6,371.0\text{ km}$, the shortest path between two cities at latitude/longitude coordinates $(\phi_1, \lambda_1)$ and $(\phi_2, \lambda_2)$ is not a straight constant-compass line on a flat Mercator map (a *rhumb line* or *loxodrome*), but a **Great-Circle orthodrome**—the arc cut on the surface by a plane slicing through both cities and the center of the Earth.

Where does the **Spherical Law of Cosines** come from? You can derive it in thirty seconds using the 3D unit-sphere projections we just learned! On a unit sphere of radius $r = 1$, a city at latitude $\phi$ and longitude $\lambda$ has vertical polar height $z = \sin\phi$ and equatorial shadow radius $\cos\phi$, which projects onto the $(x, y)$ axes as $x = \cos\phi\cos\lambda$ and $y = \cos\phi\sin\lambda$:

$$\hat{u}_1 = \begin{bmatrix} \cos\phi_1\cos\lambda_1 \\ \cos\phi_1\sin\lambda_1 \\ \sin\phi_1 \end{bmatrix}, \qquad \hat{u}_2 = \begin{bmatrix} \cos\phi_2\cos\lambda_2 \\ \cos\phi_2\sin\lambda_2 \\ \sin\phi_2 \end{bmatrix}$$

Taking the 3D dot product $\hat{u}_1 \cdot \hat{u}_2 = \cos d$ between the two unit vectors and applying the cosine difference identity $\cos\lambda_1\cos\lambda_2 + \sin\lambda_1\sin\lambda_2 = \cos(\lambda_2 - \lambda_1)$ immediately gives the central geocentric angle $d$ as the sum of the polar projection ($\sin\phi_1\sin\phi_2$) and the equatorial projection ($\cos\phi_1\cos\phi_2\cos\Delta\lambda$):

$$\cos d = \sin\phi_1 \sin\phi_2 + \cos\phi_1 \cos\phi_2 \cos(\lambda_2 - \lambda_1), \qquad D = R_E \times d_{\text{rad}}$$

Because longitudinal circles converge toward the poles like the slices of an orange ($\cos\phi < 1$), flying from San Francisco ($\phi_1 \approx 37.6^\circ\text{ N}$) to Tokyo ($\phi_2 \approx 35.8^\circ\text{ N}$) along the Great Circle arcs up toward the Aleutian Islands near $50^\circ\text{ N}$—where each degree of longitude is much shorter than at $36^\circ\text{ N}$—saving hundreds of kilometers of fuel and flight time compared to flying due west along a parallel of latitude!

That exact same Spherical Law of Cosines solves the **astronomical triangle** linking the North Celestial Pole, an observer's zenith at latitude $\phi$, and the sun at seasonal declination $\delta$ and solar hour angle $\omega$ ($15^\circ$ per hour from solar noon), yielding the sun's horizon elevation angle $\alpha$ and compass azimuth $\gamma_s$:

$$\sin\alpha = \sin\phi \sin\delta + \cos\phi \cos\delta \cos\omega, \qquad \cos\gamma_s = \frac{\sin\alpha \sin\phi - \sin\delta}{\cos\alpha \cos\phi}$$

Even more remarkably, nature mastered all three navigation algorithms—the wind triangle, spherical great-circle orthodromes, and time-compensated solar azimuths—millions of years before human aviation. Every autumn, the **bar-tailed godwit** (*Limosa lapponica*) lifts off from Alaska's tidal flats and flies **$11,000\text{ kilometers}$ non-stop across the open Pacific Ocean to New Zealand** in nine days without food, water, or landmarks. Because the sun marches across the sky at $15^\circ\text{ per hour}$, a bird steering by the sun without a clock would spiral off course by $90^\circ$ every six hours; the godwit combines an internal circadian clock with solar elevation/azimuth geometry and retinal magnetoreception to follow a spherical great-circle orthodrome while continuously crabbing into crosswinds (`{{key:▸y,x}}` vector addition) so its ground track lands squarely on its New Zealand estuary.

And when satellite geodesy requires sub-meter precision across the globe, we step from a sphere to Isaac Newton's **oblate spheroid**. In the *Principia* (1687), Newton deduced that Earth's daily centrifugal rotation causes the equator to bulge outward by $21.385\text{ km}$ relative to the poles. Modern GPS/GNSS codifies that shape in the **World Geodetic System 1984 (WGS84)** reference ellipsoid (equatorial semi-major axis $a = 6,378,137.0\text{ m}$, flattening $f = 1/298.257223563$, first eccentricity squared $e^2 = 2f - f^2 \approx 0.00669437999014$), where a receiver at geodetic latitude $\phi$, longitude $\lambda$, and height $h$ has prime-vertical radius of curvature $N(\phi)$ and Earth-Centered Earth-Fixed coordinates $(X, Y, Z)$:

$$N(\phi) = \frac{a}{\sqrt{1 - e^2 \sin^2\phi}}, \qquad \begin{bmatrix} X \\ Y \\ Z \end{bmatrix} = \begin{bmatrix} (N(\phi) + h) \cos\phi \cos\lambda \\ (N(\phi) + h) \cos\phi \sin\lambda \\ (N(\phi)(1 - e^2) + h) \sin\phi \end{bmatrix}$$

---

## Why Hanging Chains Refuse to Form Parabolas: Hyperbolic Functions

### The 1691 Bernoulli Contest, Catenary Chains & the Gateway Arch

Look up at a steel power cable sagging between two transmission towers, or a heavy anchor chain draped between two harbor bollards. What curve does a flexible chain trace when hanging freely under its own weight?

For decades, the greatest minds of the Scientific Revolution got the answer wrong. In his *Two New Sciences* (1638), Galileo Galilei wrote that a hanging chain forms a **parabola** ($y = kx^2$), and for half a century architects and physicists repeated Galileo's claim. Only in 1646 did a seventeen-year-old Dutch student named Christiaan Huygens prove geometrically that a hanging chain cannot possibly be a parabola—a startling refutation that left Europe's finest geometers asking why Galileo's intuition had failed.

In May 1690, the Swiss mathematician Jakob Bernoulli issued a public challenge in the journal *Acta Eruditorum*, daring the mathematicians of Europe to find the true equation of the hanging chain. Within a year, three men solved the challenge independently: **Christiaan Huygens**, **Gottfried Wilhelm Leibniz**, and Jakob's younger brother **Johann Bernoulli**. They proved that a parabola appears only when load is distributed uniformly per unit of *horizontal span* $dx$—as happens in a suspension bridge like the Golden Gate, where the heavy flat roadway deck hangs from vertical suspender cables spaced evenly along the horizontal axis.

In a freely hanging chain or power line, however, there is no roadway deck: the weight is distributed uniformly per unit of *curved arc length* $ds = \sqrt{1 + (dy/dx)^2}\,dx$ along the chain itself! Near the supports, where the chain tilts steeply, each meter of horizontal span contains much more chain—and therefore much more weight—than near the flat bottom of the sag.

Let us trace how Huygens, Leibniz, and Johann Bernoulli solved the force balance of a chain segment of arc length $s$ measured from the lowest point (where the chain is horizontal and the tension is purely horizontal, $T_0$) up to a point $(x, y)$ where the chain tilts at angle $\psi$:
1. **Horizontal Equilibrium:** Because no horizontal external forces act on the hanging segment, the horizontal component of tension $T\cos\psi$ must balance the bottom tension $T_0$ everywhere along the span:

   $$T\cos\psi = T_0$$

2. **Vertical Equilibrium:** The upward vertical component of tension $T\sin\psi$ must support the downward gravitational weight $w \cdot s$ of the arc length $s$ hanging below $(x, y)$ (where $w$ is the linear weight density in Newtons per meter):

   $$T\sin\psi = w \cdot s$$

3. **Dividing Vertical by Horizontal:** Dividing the second equation by the first eliminates the unknown tension $T$ and links the slope $\frac{dy}{dx} = \tan\psi$ directly to the arc length $s$:

   $$\frac{dy}{dx} = \tan\psi = \frac{w \cdot s}{T_0} = \frac{s}{a}, \qquad \text{where } a = \frac{T_0}{w}$$

Differentiating with respect to $x$ requires a function whose derivative is related to its own arc length $ds/dx = \sqrt{1 + (dy/dx)^2}$—and as Leibniz and Bernoulli discovered, that function is the symmetric combination of Euler's rising and decaying exponentials $e^{x/a}$ and $e^{-x/a}$, which Huygens christened the **catenary** (from the Latin *catena*, "chain") and which we call the **hyperbolic cosine**:

$$\cosh(u) = \frac{e^u + e^{-u}}{2}, \qquad \sinh(u) = \frac{e^u - e^{-u}}{2}, \qquad \tanh(u) = \frac{\sinh(u)}{\cosh(u)} = \frac{e^u - e^{-u}}{e^u + e^{-u}}$$

With the origin placed at the lowest point of the cable, the vertical sag $y(x)$ follows the hyperbolic cosine while the curved arc length $s(x)$ of cable hanging between the vertex and $x$ follows the hyperbolic sine:

$$y(x) = a\left(\cosh\left(\frac{x}{a}\right) - 1\right), \qquad s(x) = a\sinh\left(\frac{x}{a}\right)$$

Why are these exponential combinations called *hyperbolic* functions, and why do they share keys with $\sin$, $\cos$, and $\tan$? Because whereas the circular functions $(\cos u, \sin u)$ parameterize points on the **unit circle** $x^2 + y^2 = 1$ (sweeping out a circular sector of area $u/2$), squaring and subtracting $\cosh u$ and $\sinh u$ reveals that $(\cosh u, \sinh u)$ parameterize the right-hand branch of the **unit hyperbola** $x^2 - y^2 = 1$ (sweeping out a hyperbolic sector of area $u/2$):

$$\cosh^2(u) - \sinh^2(u) = \left(\frac{e^u + e^{-u}}{2}\right)^2 - \left(\frac{e^u - e^{-u}}{2}\right)^2 = \frac{e^{2u} + 2 + e^{-2u} - (e^{2u} - 2 + e^{-2u})}{4} = 1$$

Better still, notice how their derivatives mirror the circular functions without the minus sign on $\frac{d}{du}\cosh u$:

$$\frac{d}{du}\sinh(u) = \cosh(u), \qquad \frac{d}{du}\cosh(u) = +\sinh(u), \qquad \frac{d}{du}\tanh(u) = \operatorname{sech}^2(u) = 1 - \tanh^2(u)$$

Turn a hanging catenary chain upside down, and every link swaps pure tension for pure compression with zero bending torque. That is why Robert Hooke declared to the Royal Society in 1675, *"As hangs the flexible chain, so but inverted will stand the rigid arch,"* and why architect Eero Saarinen and structural engineer Hannskarl Bandel shaped the $192\text{-meter}$ stainless-steel **Gateway Arch in St. Louis** as an inverted hyperbolic cosine catenary.

### Ocean Tsunami Dispersion, Relativistic Rapidity & The HYP Prefix

On the SC-32 keypad, the hyperbolic prefix **`{{key:HYP}}`** lives on Left Shift `{{key:↰}}` above `{{key:R↓}}`. Pressing `{{key:HYP}}` arms the transient `HYP` annunciator and pairs directly with the primary keys `{{key:SIN}}`, `{{key:COS}}`, and `{{key:TAN}}` for $\sinh(x)$, $\cosh(x)$, and $\tanh(x)$, or with their Left-Shifted inverses `{{key:ASIN}}`, `{{key:ACOS}}`, and `{{key:ATAN}}` for the inverse hyperbolic functions (and because hyperbolic arguments are dimensionless real numbers, `{{key:HYP}}` operations are completely independent of `DEG`/`RAD`/`GRAD` angular modes):

| Function | Key Sequence | Mathematical Definition | Valid Domain |
| :--- | :--- | :--- | :---: |
| **Hyperbolic Sine** | `{{key:HYP}} {{key:SIN}}` | $\sinh(x) = \frac{e^x - e^{-x}}{2}$ | $(-\infty, +\infty)$ |
| **Hyperbolic Cosine** | `{{key:HYP}} {{key:COS}}` | $\cosh(x) = \frac{e^x + e^{-x}}{2}$ | $(-\infty, +\infty)$ |
| **Hyperbolic Tangent** | `{{key:HYP}} {{key:TAN}}` | $\tanh(x) = \frac{\sinh(x)}{\cosh(x)}$ | $(-\infty, +\infty)$ |
| **Inverse Sinh** | `{{key:HYP}} {{key:ASIN}}` | $\operatorname{arsinh}(x) = \ln\left(x + \sqrt{x^2 + 1}\right)$ | $(-\infty, +\infty)$ |
| **Inverse Cosh** | `{{key:HYP}} {{key:ACOS}}` | $\operatorname{arcosh}(x) = \ln\left(x + \sqrt{x^2 - 1}\right)$ | $x \ge 1.0$ |
| **Inverse Tanh** | `{{key:HYP}} {{key:ATAN}}` | $\operatorname{artanh}(x) = \frac{1}{2}\ln\left(\frac{1+x}{1-x}\right)$ | $\lvert x\rvert < 1.0$ |

Beyond hanging cables and masonry arches, the **hyperbolic tangent** $\tanh(u)$ governs two dramatic transitions in nature whenever a physical system saturates smoothly between two regimes:
* **Ocean Surface Waves and Tsunamis:** When surface gravity waves of wavelength $\lambda$ (wavenumber $k = 2\pi/\lambda$) travel across an ocean of depth $h$, George Biddell Airy proved that their phase speed $c_{\text{wave}}$ depends on the hyperbolic tangent of the depth-to-wavelength ratio $kh$:

  $$c_{\text{wave}} = \sqrt{\frac{g}{k}\tanh(kh)}$$

  In deep water ($kh \gg 1$), $\tanh(kh) \to 1$, so long-wavelength swell outruns short chop ($c_{\text{wave}} \approx \sqrt{g/k}$). In shallow water—or during a trans-oceanic **tsunami** whose wavelength $\lambda = 200\text{ km}$ vastly exceeds the $4\text{-km}$ ocean depth ($kh \ll 1$)—$\tanh(kh) \approx kh$, the wavenumber $k$ cancels completely, and the wave races across the Pacific at the shallow-water limit $c_{\text{wave}} \approx \sqrt{gh} \approx 200\text{ m/s}$ ($720\text{ km/h}$, the speed of a jet airliner!).
* **Einstein's Relativistic Speed Limit and Minkowski Rapidities:** In Newtonian physics, if a spacecraft flies at $v_1 = 0.75c$ relative to Earth and fires a probe forward at $v_2 = 0.60c$ relative to the ship, Galilean addition predicts $0.75c + 0.60c = 1.35c$—faster than light! In 1905, Albert Einstein showed that spacetime Lorentz transformations combine collinear velocities via $v_{\text{total}}/c = (\beta_1 + \beta_2)/(1 + \beta_1\beta_2)$. Three years later, Hermann Minkowski recognized that formula as the hyperbolic tangent addition identity! If you map every normalized speed $\beta = v/c$ into its hyperbolic angle (**rapidity**) $\theta = \operatorname{artanh}(v/c)$, then rapidities add linearly:

  $$\theta_{\text{total}} = \theta_1 + \theta_2 \implies \frac{v_{\text{total}}}{c} = \tanh\left(\operatorname{artanh}\left(\frac{v_1}{c}\right) + \operatorname{artanh}\left(\frac{v_2}{c}\right)\right)$$

  Because $\tanh(\theta)$ approaches $1.0$ asymptotically as $\theta \to \infty$, you can add finite rocket boosts forever and approach closer and closer to $c$ without ever crossing the cosmic speed limit.

---

## On the Stack: Trigonometry, Vectors & Hyperbolic Workbench

With the geometry of the unit circle, the $(Y, X)$ vector plane, spherical orthodromes, and the unit hyperbola in hand, let us step to the StackCalc SC-32 workbench and execute these projections directly on the four-register stack. Because every unary circular and hyperbolic key transforms Register $X$ in place while `{{key:▸y,x}}` and `{{key:▸θ,r}}` rotate and project the $(Y, X)$ coordinate plane directly into statistical memory, multi-step surveying, ballistics, and navigation formulas unfold without a single pair of parentheses.

### Angular Mode Sanity Check & Direct Circular Projections

Throughout this workbench, we operate in **Degrees mode (`{{key:DEG}}`)** unless radians are explicitly required. Before starting a trigonometric calculation, a quick two-keystroke check via `{{res:sc32_04_trig_vectors_polar_seq_56:keys}}` confirms your active mode: in Degrees mode (`{{key:DEG}}`), $\sin(45^\circ)$ displays the familiar unit-diagonal projection `0.707106781187` ($\sqrt{2}/2$), whereas if the calculator was left in radian units from an earlier session, $\sin(45\text{ rad})$ returns `0.850903524534`—a gentle reminder to press `{{key:DEG}}`.

1. **Projectile Ballistics (Apex Height & Downrange Distance):** Suppose an artillery shell is fired with muzzle velocity $v_0 = 85.0\text{ m/s}$ at an elevation angle $\theta = 38.0^\circ$ ($g = 9.80665\text{ m/s}^2$). What are its apex altitude $H_{\max} = (v_0\sin\theta)^2 / (2g)$ and its horizontal range $R = v_0^2\sin(2\theta)/g$ across level ground? For the apex height $H_{\max}$, we project the vertical muzzle velocity $v_{0y} = 85\sin(38^\circ) = 52.3312\text{ m/s}$, square it in place, and divide by $2g$ via `{{res:sc32_04_trig_vectors_polar_seq_09:keys}}` to reach **`{{res:sc32_04_trig_vectors_polar_seq_09:value}}`** $\text{m}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `85 {{key:ENTER}} 38 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $52.3312$ | Vertical velocity component $v_{0y}$ |
| `{{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2,738.5574$ | $v_{0y}^2$ numerator |
| `2 {{key:ENTER}} 9.80665 {{key:×}}` | $0.0000$ | $0.0000$ | $2738.5574$ | $19.6133$ | Denominator $2g$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$139.6275\text{ m}$** | Peak height $H_{\max}$ |

   Evaluating the double-angle range equation with $\sin(2\theta) = \sin(76^\circ)$ via `{{res:sc32_04_trig_vectors_polar_seq_10:keys}}` yields a downrange impact distance of $R =$ **`{{res:sc32_04_trig_vectors_polar_seq_10:value}}`** $\text{m}$.

2. **Inclined-Plane Friction Dynamics:** Sliding a crate down a ramp inclined at $\theta = 34.0^\circ$ with kinetic friction coefficient $\mu_k = 0.22$ ($g = 9.80665\text{ m/s}^2$), evaluating $\sin(34^\circ) = 0.5592$, subtracting $0.22\cos(34^\circ) = 0.1824$, and multiplying by $g = 9.80665\text{ m/s}^2$ via `{{res:sc32_04_trig_vectors_polar_seq_23:keys}}` yields a net downhill acceleration of $a = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_23:value}}\text{ m/s}^2}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `34 {{key:SIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.5592$ | Gravitational downhill acceleration component $\sin(34^\circ)$ |
| `34 {{key:COS}} 0.22 {{key:×}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.3768$ | Subtract kinetic friction deceleration $\mu_k \cos(34^\circ)$ |
| `9.80665 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$3.6952$** | Scale by gravity $g$ for net downhill acceleration $a$ ($\text{m/s}^2$) |

   Notice how `{{key:LASTX}}` lets you evaluate $a = g(\sin\theta - \mu_k\cos\theta)$ by typing the incline angle `34` only once: keying `34 {{key:SIN}} {{key:LASTX}} {{key:COS}} 0.22 {{key:×}} {{key:-}} 9.80665 {{key:×}}` recalls $34^\circ$ directly from `LASTX` after `{{key:SIN}}` and lands on the exact same $\mathbf{3.6952\text{ m/s}^2}$ acceleration.

3. **Two-Station Optical Leveling to an Inaccessible Mountain Summit:** Sighting across a horizontal baseline $d = 500.0\text{ m}$ with elevation angles $\alpha = 24.5^\circ$ (Station 1) and $\beta = 31.2^\circ$ (Station 2, closer to the peak), each cotangent on the stack is simply `{{key:TAN}} {{key:1/x}}`. Subtracting $\cot(31.2^\circ)$ from $\cot(24.5^\circ)$ leaves $\Delta\cot = 0.5431$ in Register $X$, and dividing it into the $500\text{ m}$ baseline via `{{res:sc32_04_trig_vectors_polar_seq_28:keys}}` reveals a summit elevation of $H = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_28:value}}\text{ meters}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `24.5 {{key:TAN}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.1943$ | Invert tangent for Station 1 cotangent $\cot(24.5^\circ)$ |
| `31.2 {{key:TAN}} {{key:1/x}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.5431$ | Subtract Station 2 cotangent $\cot(31.2^\circ)$ for differential $\Delta\cot$ |
| `500 {{key:x⇄y}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$920.6349$** | Divide baseline distance $d = 500\text{ m}$ for summit height $H$ (m) |

4. **Nonlinear Pendulum Period Dilation:** Releasing a clock pendulum of small-angle period $T_0 = 2.000\text{ s}$ from a wide swing amplitude of $\theta_0 = 45.0^\circ$, evaluating the half-angle sine squared (`22.5 {{key:SIN}} {{key:x²}}` $\to 0.1464$), multiplying by $1/4$ and adding unity (`0.25 {{key:×}} 1 {{key:+}}` $\to 1.0366$), and scaling by $T_0 = 2.0\text{ s}$ in `{{res:sc32_04_trig_vectors_polar_seq_29:keys}}` reveals a $3.66\%$ period dilation of $T = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_29:value}}\text{ seconds}}$.

5. **Composing Unary Trig Operators Inside Fractions & Nested Radicals:** Because `{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`, `{{key:x²}}`, and `{{key:√x}}` all act on Register $X$ in place without disturbing upper shelves, even multi-tier trigonometric fractions and nested radicals unfold in a single left-to-right pass:

   $$x_1 = \frac{\sin(35^\circ) \cos(42^\circ) + \tan(18^\circ)}{\sqrt{\sin^2(65^\circ) + \cos^2(25^\circ)}}, \qquad x_2 = \sqrt{\cos(28^\circ) + \sqrt{\sin(48^\circ) + \sqrt{\tan(15^\circ)}}}$$

   In $x_1$, the numerator waits patiently in Register $Y$ while the denominator quadrature forms in Register $X$ via `{{res:sc32_04_trig_vectors_polar_seq_40:keys}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `35 {{key:SIN}} 42 {{key:COS}} {{key:×}} 18 {{key:TAN}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.7512$ | Trigonometric numerator sum $\sin(35^\circ)\cos(42^\circ) + \tan(18^\circ)$ |
| `65 {{key:SIN}} {{key:x²}} 25 {{key:COS}} {{key:x²}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.7512$ | $1.2817$ | Denominator quadrature $\sqrt{\sin^2(65^\circ) + \cos^2(25^\circ)}$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.5861$** | Divide numerator by denominator for continued trigonometric quotient |

   And in the nested radical $x_2$, starting at the innermost $\tan(15^\circ)$ and peeling each square-root shell outward via `{{res:sc32_04_trig_vectors_polar_seq_53:keys}}` resolves **`{{res:sc32_04_trig_vectors_polar_seq_53:value}}`** in nine keystrokes while never occupying more than two stack registers:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `15 {{key:TAN}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.5176$ | Initial square root tangent $\sqrt{\tan(15^\circ)}$ |
| `48 {{key:SIN}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.1228$ | Add sine term and extract nested root $\sqrt{\sin(48^\circ) + \dots}$ |
| `28 {{key:COS}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1.4163$** | Add cosine term and extract outer root for nested trigonometric radical |

### Inverse Trigonometry & Oblique Triangles on the Stack

1. **Snell's Law & Fiber-Optic Total Internal Reflection (`{{key:ASIN}}`):** Guiding light inside a glass fiber core ($n_1 = 1.480$) surrounded by cladding ($n_2 = 1.450$), dividing the cladding index by the core index (`1.450 {{key:ENTER}} 1.480 {{key:÷}}`, placing $0.9797$ in Register $X$) and pressing `{{key:ASIN}}` in `{{res:sc32_04_trig_vectors_polar_seq_15:keys}}` yields $\theta_c = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_15:value}}^\circ}$—meaning any ray propagating within $90^\circ - \theta_c = 11.56^\circ$ of the fiber axis undergoes $100\%$ lossless Total Internal Reflection.
2. **Banked Highway Curve Super-Elevation (`{{key:ATAN}}`):** Designing a highway curve of radius $R = 350.0\text{ m}$ for $v = 100.0\text{ km/h}$ ($27.7778\text{ m/s}$, with $g = 9.80665\text{ m/s}^2$), converting $100\text{ km/h}$ into meters per second (`100 {{key:ENTER}} 3.6 {{key:÷}}`), squaring in place, and dividing by $gR$ in `{{res:sc32_04_trig_vectors_polar_seq_16:keys}}` yields the lateral acceleration ratio $v^2/(gR) = 0.2248\,g$, and pressing `{{key:ATAN}}` extracts the ideal super-elevation angle $\theta = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_16:value}}^\circ}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `100 {{key:ENTER}} 3.6 {{key:÷}} {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $771.6049$ | Square speed in m/s $(v/3.6)^2$ |
| `9.80665 {{key:ENTER}} 350 {{key:×}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.2248$ | Divide by centripetal gravity denominator $g R$ |
| `{{key:ATAN}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$12.6698$** | Extract arctangent for banking angle $\theta$ (degrees) |

3. **Satellite Ground-Station Look-Angle Elevation (`{{key:ATAN}}`) & Gauss's Orbital Anomaly:** Tracking a low-Earth-orbit satellite at altitude $h = 850\text{ km}$ above an Earth of radius $R_E = 6,371\text{ km}$ at geocentric angle $\gamma = 18.0^\circ$, computing $\cos(18^\circ) = 0.9511$ first, subtracting $R_E/(R_E + h) = 6371 / (6371 + 850)$, dividing by $\sin(18^\circ)$, and pressing `{{key:ATAN}}` in `{{res:sc32_04_trig_vectors_polar_seq_18:keys}}` yields the antenna horizon elevation $E = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_18:value}}^\circ}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `18 {{key:COS}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.9511$ | Cosine of angular distance $\cos\gamma$ |
| `6371 {{key:ENTER}} 6371 {{key:ENTER}} 850 {{key:+}} {{key:÷}} {{key:-}}` | $0.9511$ | $0.9511$ | $0.9511$ | $0.0688$ | Subtract orbital radius ratio $R_E / (R_E + h)$ |
| `18 {{key:SIN}} {{key:÷}}` | $0.9511$ | $0.9511$ | $0.9511$ | $0.2225$ | Divide by sine $\sin\gamma$ for elevation tangent |
| `{{key:ATAN}}` | $0.9511$ | $0.9511$ | $0.9511$ | **$12.5462$** | Extract ground satellite elevation angle $E$ (degrees) |

   Along an elliptical orbit of eccentricity $e = 0.240$ at eccentric anomaly $E = 40.0^\circ$, evaluating the stretch factor $\sqrt{1.240/0.760} \approx 1.2773$, multiplying by $\tan(20^\circ)$, and inverting via `{{key:ATAN}} 2 {{key:×}}` in `{{res:sc32_04_trig_vectors_polar_seq_37:keys}}` determines the satellite's true anomaly $\nu = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_37:value}}^\circ}$.

4. **Law of Cosines (Survey Boundary & Acoustic Wave Superposition):** Sighting two survey boundary markers at $a = 45.0\text{ m}$ and $b = 62.0\text{ m}$ separated by an included angle of $C = 48.0^\circ$, the Pythagorean sum $a^2 + b^2 = 5869$ waits in Register $Y$ while the cosine cross-term $2ab\cos C = 3733.7488$ builds in Register $X$, so executing `{{res:sc32_04_trig_vectors_polar_seq_11:keys}}` subtracts the cross-term and extracts the opposing boundary length $c =$ **`{{res:sc32_04_trig_vectors_polar_seq_11:value}}`** $\text{m}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `45 {{key:x²}} 62 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $5869.0000$ | Sum of squared sides $a^2 + b^2 = 2025 + 3844 = 5869$ |
| `2 {{key:ENTER}} 45 {{key:×}} 62 {{key:×}} 48 {{key:COS}} {{key:×}}` | $0.0000$ | $0.0000$ | $5869.0000$ | $3733.7488$ | Law of cosines cross-term $2 a b \cos C$ |
| `{{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2135.2512$ | Quadratic difference $(a^2 + b^2 - 2ab\cos C)$ |
| `{{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$46.2088$** | Extract square root for side $c$ (m) |

   Similarly, when two coherent acoustic waves with pressure amplitudes $A_1 = 2.40\text{ Pa}$ and $A_2 = 3.10\text{ Pa}$ arrive at a microphone with phase difference $\Delta\phi = 55.0^\circ$, accumulating $A_1^2 + A_2^2 = 15.37\text{ Pa}^2$ first, adding $2(2.4)(3.1)\cos(55^\circ) = 8.5348\text{ Pa}^2$, and extracting the square root in `{{res:sc32_04_trig_vectors_polar_seq_34:keys}}` yields the superposed acoustic pressure amplitude $A_{\text{res}} = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_34:value}}\text{ Pa}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2.4 {{key:x²}} 3.1 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $15.3700$ | Sum of squared wave amplitudes $A_1^2 + A_2^2$ |
| `2 {{key:ENTER}} 2.4 {{key:×}} 3.1 {{key:×}} 55 {{key:COS}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $23.9048$ | Add wave interference cross-term $2 A_1 A_2 \cos(\Delta\phi)$ |
| `{{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$4.8893$** | Extract square root for superposed wave amplitude $A_{\text{res}}$ |

### Catenary Sag, Tsunami Wave Dispersion & Relativistic Rapidity on the Stack

1. **Catenary Transmission Line Cable Sag & Ocean Tsunami Dispersion:** Stringing a high-voltage transmission cable across a $L = 200\text{ meter}$ span ($x = 100\text{ m}$ half-span) with catenary parameter $a = T_0 / w = 800\text{ meters}$, we evaluate $y = 800(\cosh(100/800) - 1)$ from the inside outward: entering $x = 100\text{ m}$ (`100 {{key:ENTER}}`), dividing by $a = 800\text{ m}$ (`800 {{key:÷}}` $\to 0.125$), evaluating the hyperbolic cosine (`{{key:HYP}} {{key:COS}}` $\to 1.007823$), subtracting unity (`1 {{key:-}}` $\to 0.007823$), and scaling back by $a = 800\text{ m}$ (`800 {{key:×}}`) in `{{res:sc32_04_trig_vectors_polar_seq_01:keys}}` reveals a midpoint sag of **`{{res:sc32_04_trig_vectors_polar_seq_01:value}}`** meters ($6.26\text{ m}$). Likewise, for Airy's ocean wave speed $c_{\text{wave}} = \sqrt{(g/k)\tanh(kh)}$ across a $h = 4,000\text{ m}$ ocean basin for a tsunami of wavelength $\lambda = 200,000\text{ m}$ ($k = 2\pi/\lambda \approx 0.000031416\text{ m}^{-1}$, so $kh = 0.12566$), keying `0.12566 {{key:HYP}} {{key:TAN}} 9.80665 {{key:×}} 0.000031416 {{key:÷}} {{key:√x}}` evaluates $\tanh(kh)$ in place, scales by $g/k$, and extracts the square root to yield $c_{\text{wave}} \approx \mathbf{197.53\text{ m/s}}$ ($711.1\text{ km/h}$).
2. **Relativistic Velocity Addition:** When an interstellar probe traveling at $v_1 = 0.75c$ relative to Earth launches a scout missile forward at $v_2 = 0.60c$ relative to the probe, we transform $v_1 = 0.75c$ into its rapidity (`0.75 {{key:HYP}} {{key:ATAN}}` $\to \theta_1 = 0.9730$), type `0.60` and convert the missile's relative velocity into rapidity (`{{key:HYP}} {{key:ATAN}}` $\to \theta_2 = 0.6931$ with $\theta_1$ lifted to $Y$), press `{{key:+}}` ($\theta_{\text{total}} = 1.6661$), and press `{{key:HYP}} {{key:TAN}}` in the full sequence `{{res:sc32_04_trig_vectors_polar_seq_02:keys}}` to find that the missile travels at **`{{res:sc32_04_trig_vectors_polar_seq_02:value}}`** $c$ ($93.10\%$ of $c$).

### 2D Vector Projections, Wind Triangles, Traverses & Spherical Geodesy

You can verify the $(Y = \theta, X = r)$ polar input convention at any time by keying a pure north polar vector of radius $r = 10$ at $\theta = 90^\circ$ via `{{res:sc32_04_trig_vectors_polar_seq_57:keys}}`: because `{{key:▸y,x}}` expects **Angle $\theta$ in Register $Y$ and Radius $r$ in Register $X$**, the projection places `0.0000` in Register $X$ ($x = 10\cos 90^\circ$) and `10.0000` in Register $Y$ ($y = 10\sin 90^\circ$).

{{res:sc32_phasor_mag:screenshot|Direct rectangular-to-polar vector conversion on the StackCalc SC-32 places the angle θ = 53.1301° in Register Y and the radial magnitude r = 5.0000 in Register X.}}

1. **Resolving the AC Power Triangle ($P, Q, S$):** Driving an inductive AC motor that draws $I_{\text{rms}} = 8.50\text{ A}$ from a $V_{\text{rms}} = 120.0\text{ V}$ line ($S = 1,020\text{ VA}$) at phase angle $\phi = 32.0^\circ$, executing `{{res:sc32_04_trig_vectors_polar_seq_19:keys}}` duplicates $S = 1,020\text{ VA}$ and scales by $\cos(32^\circ)$ and $\sin(32^\circ)$ to place real power $P = \mathbf{865.01\text{ W}}$ in Register $Y$ and reactive power $Q =$ **`{{res:sc32_04_trig_vectors_polar_seq_19:value}}`** $\text{VAR}$ in Register $X$. (Or in a single coordinate projection via `32 {{key:ENTER}} 1020 {{key:▸y,x}}`, which places the sine component $Q = S\sin 32^\circ = 540.52\text{ VAR}$ in Register $Y$ and the cosine component $P = S\cos 32^\circ = 865.01\text{ W}$ in Register $X$; tapping `{{key:x⇄y}}` swaps them to match the manual table below):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `120 {{key:ENTER}} 8.5 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1020.0000$ | Total apparent electrical power $S = V_{\text{rms}} I_{\text{rms}}$ (VA) |
| `{{key:ENTER}} {{key:ENTER}} 32 {{key:COS}} {{key:×}}` | $0.0000$ | $0.0000$ | $1020.0000$ | $865.0097$ | Multiply by power factor $\cos(32^\circ)$ for real power $P$ (W) |
| `{{key:x⇄y}} 32 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $865.0097$ | **$540.5176$** | Multiply by reactive factor $\sin(32^\circ)$ for reactive power $Q$ (VAR) |

2. **Aircraft Wind Triangle & Crosswind Correction:** Flying at true airspeed $V_{\text{air}} = 220.0\text{ knots}$ on heading $\theta_1 = 45.0^\circ$ while a $35.0\text{-knot}$ wind blows toward $\theta_2 = 130.0^\circ$, loading $\theta_1 = 45^\circ$ into $Y$ and $r_1 = 220\text{ kts}$ into $X$ via `{{res:sc32_04_trig_vectors_polar_seq_03:keys}}` splits the aircraft vector into **`{{res:sc32_04_trig_vectors_polar_seq_03:value}}`** ($Y = 155.5635\text{ kts}$ for $V_{\text{air}, y}$ and $X = 155.5635\text{ kts}$ for $V_{\text{air}, x}$), which we park in Variables `A` and `B` via `{{key:STO}} A {{key:x⇄y}} {{key:STO}} B`. Next, executing `{{res:sc32_04_trig_vectors_polar_seq_04:keys}}` resolves the wind components into Register $Y = 26.8116\text{ kts}$ and Register $X = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_04:value}}}\text{ kts}$. Adding the $x$- and $y$-components (`{{key:RCL}} A {{key:+}} {{key:x⇄y}} {{key:RCL}} B {{key:+}} {{key:x⇄y}}`) and pressing `{{key:▸θ,r}}` yields **Ground Speed $V_{\text{ground}} = 225.76\text{ knots}$** in Register $X$ and **Ground Track Angle $\theta_{\text{track}} = 53.89^\circ$** in Register $Y$.

3. **Closed-Loop Survey Traverse (`{{key:▸y,x}} {{key:Σ+}}`):** Walking a four-station rectangular parcel—**Leg 1** ($r = 100.0\text{ m}$ at $\theta = 60.0^\circ$), **Leg 2** ($r = 80.0\text{ m}$ at $\theta = 150.0^\circ$), **Leg 3** ($r = 100.0\text{ m}$ at $\theta = 240.0^\circ$), and **Leg 4** ($r = 80.0\text{ m}$ at $\theta = 330.0^\circ$)—after clearing statistical memory (`{{key:CLΣ}}`):
   * **Leg 1 ($\theta = 60^\circ, r = 100\text{ m}$):** Push `60 {{key:ENTER}} 100` and execute `{{res:sc32_04_trig_vectors_polar_seq_05:keys}}` to project $\Delta y = 86.6025\text{ m}$ into $Y$ and $\Delta x = 50.0000\text{ m}$ into $X$ and accumulate both into statistical memory ($n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_05:value}}}$).
   * **Leg 2 ($\theta = 150^\circ, r = 80\text{ m}$):** Push `150 {{key:ENTER}} 80` and execute `{{res:sc32_04_trig_vectors_polar_seq_06:keys}}` ($\Delta y = 40.0000\text{ m}, \Delta x = -69.2820\text{ m}$) to advance the station counter to $n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_06:value}}}$.
   * **Leg 3 ($\theta = 240^\circ, r = 100\text{ m}$):** Push `240 {{key:ENTER}} 100` and execute `{{res:sc32_04_trig_vectors_polar_seq_07:keys}}` ($\Delta y = -86.6025\text{ m}, \Delta x = -50.0000\text{ m}$) to advance to $n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_07:value}}}$.
   * **Leg 4 ($\theta = 330^\circ, r = 80\text{ m}$):** Push `330 {{key:ENTER}} 80` and execute `{{res:sc32_04_trig_vectors_polar_seq_08:keys}}` ($\Delta y = -40.0000\text{ m}, \Delta x = 69.2820\text{ m}$) to close the four-station loop at $n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_08:value}}}$, where `{{key:SUMS}}` confirms $\Sigma x = 0.0000\text{ m}$ and $\Sigma y = 0.0000\text{ m}$.

4. **Mohr's Circle Strain Transformation & 3D Space-Frame Bevel Angle:** Rotating an aircraft wing strain-gauge rosette with $\epsilon_x = 450\,\mu\epsilon$, $\epsilon_y = 120\,\mu\epsilon$, and $\gamma_{xy} = 280\,\mu\epsilon$ through $\theta = 30.0^\circ$ ($2\theta = 60.0^\circ$), computing the hydrostatic mean strain $285\,\mu\epsilon$ and adding the normal cosine projection $82.5\,\mu\epsilon$ and shear sine projection $121.2436\,\mu\epsilon$ via `{{res:sc32_04_trig_vectors_polar_seq_33:keys}}` resolves $\epsilon_{x'} \approx \mathbf{488.74\,\mu\epsilon}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `450 {{key:ENTER}} 120 {{key:+}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $285.0000$ | Hydrostatic mean strain $(\epsilon_x + \epsilon_y)/2$ |
| `450 {{key:ENTER}} 120 {{key:-}} 2 {{key:÷}} 60 {{key:COS}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $367.5000$ | Add normal strain cosine transform $((\epsilon_x - \epsilon_y)/2)\cos(60^\circ)$ |
| `280 {{key:ENTER}} 2 {{key:÷}} 60 {{key:SIN}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$488.7436$** | Add shear strain sine transform $(\gamma_{xy}/2)\sin(60^\circ)$ for rotated strain $\epsilon_{x'}$ ($\mu\epsilon$) |

   Joining two skew 3D space-frame struts $\vec{A} = (4.0, 6.0, 8.0\text{ m})$ (squared length $|\vec{A}|^2 = 4^2 + 6^2 + 8^2 = 116$, so $|\vec{A}| = \sqrt{116}$) and $\vec{B} = (2.0, -3.0, 5.0\text{ m})$ (squared length $|\vec{B}|^2 = 2^2 + (-3)^2 + 5^2 = 38$, so $|\vec{B}| = \sqrt{38}$) with dot product $\vec{A}\cdot\vec{B} = 4(2) + 6(-3) + 8(5) = 8 - 18 + 40 = 30.0$, dividing $30.0$ sequentially by $\sqrt{116}$ and $\sqrt{38}$ in `{{res:sc32_04_trig_vectors_polar_seq_20:keys}}` forms $\cos\theta = 0.4519$ in Register $X$, and `{{key:ACOS}}` extracts the true 3D intersection angle $\theta = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_20:value}}^\circ}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `30 {{key:ENTER}} 116 {{key:√x}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.7854$ | Normalize dot product by magnitude $\lvert\vec{A}\rvert = \sqrt{116}$ |
| `38 {{key:√x}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.4519$ | Normalize by magnitude $\lvert\vec{B}\rvert = \sqrt{38}$ for enclosed cosine |
| `{{key:ACOS}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$63.1371$** | Extract inverse cosine for 3D enclosed angle $\theta$ (degrees) |

5. **Great-Circle Distance (SFO to Tokyo) & Solar Horizon Elevation:** Between **San Francisco (SFO)** ($\phi_1 = 37.6189^\circ\text{ N}, \lambda_1 = -122.3750^\circ\text{ W}$) and **Tokyo Narita (NRT)** ($\phi_2 = 35.7720^\circ\text{ N}, \lambda_2 = 140.3929^\circ\text{ E}$, where crossing the $180^\circ$ International Date Line across the Pacific gives a westward longitudinal span of $\Delta\lambda = 360^\circ - (140.3929^\circ + 122.3750^\circ) = 97.2321^\circ$):
   * **Polar Sine Product ($\sin\phi_1 \sin\phi_2$):** Key `{{res:sc32_04_trig_vectors_polar_seq_54:keys}}` to leave $0.356499$ in Register $X$.
   * **Equatorial Cosine Product ($\cos\phi_1 \cos\phi_2 \cos\Delta\lambda$):** Key `{{res:sc32_04_trig_vectors_polar_seq_55:keys}}` to push $0.356499$ into Register $Y$ while forming $-0.081190$ in Register $X$.
   * **Central Angle & Arc Distance:** Press `{{key:+}} {{key:ACOS}}` to extract $d = 74.0154^\circ$, and scale by $(\pi/180) \times 6,371\text{ km}$ (`{{key:π}} {{key:×}} 180 {{key:÷}} 6371 {{key:×}}`) to obtain **$8,229.4\text{ km}$**.
   * **Solar Concentrator Elevation ($\phi = 32.0^\circ\text{ N}, \delta = 18.5^\circ, \omega = 45.0^\circ$):** Evaluating $\sin\phi\sin\delta + \cos\phi\cos\delta\cos\omega$ and extracting the arcsine via `{{res:sc32_04_trig_vectors_polar_seq_41:keys}}` resolves the sun's horizon elevation $\alpha \approx \mathbf{47.46^\circ}$ ($47.4611^\circ$).

---

### When Growth Meets Rotation: The Mystery of √−1

Look back for a moment at the two seemingly separate worlds we explored in Chapter 3 and Chapter 4. In Chapter 3, Jacob Bernoulli's compound-interest constant $e$ drove laws of **pure growth and decay** along a straight one-dimensional line—bacteria doubling in a flask, carbon-14 decaying in an ancient timber, or a hot coffee mug cooling toward room temperature. In Chapter 4, Eratosthenes' shadow and Hipparchus's chords drove laws of **pure rotation and oscillation** around a circle—a pointer sweeping endlessly through $\cos\theta$ and $\sin\theta$ without ever growing larger or smaller.

Even inside Chapter 4, we caught a tantalizing hint that those two worlds are secretly related: when Huygens, Leibniz, and Johann Bernoulli solved the hanging catenary chain, they found that the hyperbolic functions $\cosh u = (e^u + e^{-u})/2$ and $\sinh u = (e^u - e^{-u})/2$ satisfy $\cosh^2 u - \sinh^2 u = 1$—an equation identical to the unit circle $\cos^2\theta + \sin^2\theta = 1$ except for a single minus sign!

What could possibly turn a minus sign into a plus sign, bending one-dimensional exponential growth $e^x$ into two-dimensional circular rotation $(\cos\theta, \sin\theta)$?

The answer was uncovered in sixteenth-century Bologna by Rafael Bombelli while wrestling with an algebraic riddle that had baffled mathematicians for two thousand years: what number, when multiplied by itself, equals $-1$? In **[Chapter 5: The Imaginary Number That Keeps the Lights On](05-complex-numbers-phasors.md)**, we will see how Leonhard Euler fed $\sqrt{-1}$ into the exponential function $e^{i\theta}$ and discovered the most celebrated equation in all of mathematics ($e^{i\pi} + 1 = 0$)—and how electrical engineer Charles Proteus Steinmetz used that exact marriage of growth and rotation to tame the alternating-current power grid on the $(Y, X)$ stack.
