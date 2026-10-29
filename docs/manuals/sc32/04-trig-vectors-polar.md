---
title: "Chapter 4: Measuring the Cosmos with a Shadow | Thinking in the Stack (SC-32)"
description: "Direct and inverse trigonometry, hyperbolic functions, exact axial angle clamping, polar-to-rectangular 2D vector conversions, and geodetic traverses on the StackCalc SC-32."
---

# Chapter 4: Measuring the Cosmos with a Shadow

## A Stick in Alexandria and the Birth of the Unit Circle

At local solar noon on the summer solstice of 240 BCE, Eratosthenes of Cyrene—chief librarian of the Great Library of Alexandria—walked out into a sunlit courtyard and measured the shadow of an upright bronze rod called a *gnomon*. As preserved in Cleomedes' astronomical treatise *The Heavens* {{cite:cleomedes2004}}, travelers had brought Eratosthenes a curious report from the frontier garrison town of Syene (modern Aswan), some five thousand stadia up the Nile to the south. At midday on the longest day of the year, vertical stone columns in Syene cast no shadow at all, and the reflection of the overhead sun shone straight down to the water at the bottom of a deep well.

Yet at that same hour in Alexandria, Eratosthenes saw that his vertical bronze gnomon cast a crisp wedge of shadow across the courtyard paving stones. Measuring the ratio of the shadow's horizontal length to the rod's vertical height, he found that the sun's rays met the upright rod at an angle equal to one-fiftieth of a full circle:

$$\theta = \frac{360^\circ}{50} = 7.2^\circ$$

Why would the sun stand straight overhead in Syene while leaning $7.2^\circ$ south of the zenith in Alexandria? Eratosthenes realized that two assumptions—a flat Earth and a nearby sun—could never explain the discrepancy together. Because the sun is so extraordinarily distant that its rays arrive at every city on Earth as parallel lines, only the curvature of the Earth itself could tilt Alexandria's vertical rod away from Syene's vertical well. By Euclid's theorem on alternate interior angles of parallel lines cut by a transversal, the $7.2^\circ$ shadow angle at the tip of the gnomon in Alexandria had to equal the central angle subtended at the center of the Earth between Syene and Alexandria! Multiplying the five-thousand-stadia overland distance between the two cities by fifty ($50 \times 5,000 = 250,000\text{ stadia}$, or roughly $40,000\text{ kilometers}$), Eratosthenes measured the circumference of the entire planet to within a percent of modern satellite geodesy—using nothing more than a bronze stick, a shadow, and the geometry of a circle.

Two centuries after Eratosthenes, the astronomer Hipparchus of Nicaea asked how an observer could translate *any* central angle on the celestial sphere into a measurable straight-line distance. He inscribed triangles inside a circle of fixed radius and compiled the ancient world's first table of **chords**—the direct ancestor of the modern sine and cosine functions. Five hundred years later in India, astronomers led by Aryabhata sliced Hipparchus's full chord in half, noticing that the half-chord of a double angle forms the vertical leg of a right triangle inscribed inside a circle of radius $r = 1$. They called that half-chord *jya-ardha* ("half-bowstring"), which Arabic translators rendered as *jiba*, Latin scholars in twelfth-century Toledo mistranslated as *sinus* ("bay" or "fold"), and modern mathematics shortened to **sine**.

Whenever we draw a circle of radius $r = 1$ centered at the origin of an $(x, y)$ coordinate plane—the **Unit Circle**—and sweep a radial pointer counterclockwise from the positive horizontal axis through an angle $\theta$, the tip of that pointer traces out a right triangle whose hypotenuse is $1$:

$$x = \cos\theta \quad (\text{Horizontal Shadow}), \qquad y = \sin\theta \quad (\text{Vertical Height})$$

$$x^2 + y^2 = \cos^2\theta + \sin^2\theta = 1$$

To make that geometry physical during the Middle Ages and the Renaissance, Islamic and European astronomers from al-Biruni to Regiomontanus and Johannes Kepler built brass **astrolabes** and rotating paper **volvelles**: layered circular dials engraved with degree scales around the rim and an orthogonal grid of cosines and sines across the face. Instead of computing five-place series approximations by hand, a navigator could rotate the pointer arm to an angle $\theta$ and read its horizontal and vertical projections right off the engraved plate.

{{blocks:unit_circle_volvelle_30deg|Orthographic diagram of the Unit Circle Volvelle dialed to 30° (π/6 rad), reading off exact horizontal and vertical projections cos(30°) = √3/2 ≈ 0.8660 and sin(30°) = 1/2 = 0.5000.}}

When you grasp the knurled upper pointer ring of the $120\text{ mm}$ *Unit Circle Volvelle* shown in Figure 4.1 and rotate it counterclockwise from $0^\circ$ to $30^\circ$ ($\pi/6\text{ rad}$), the rotating sight window frames the exact right-triangle projections on the lower stator ring:

$$\cos(30^\circ) = \frac{\sqrt{3}}{2} \approx 0.866025, \qquad \sin(30^\circ) = \frac{1}{2} = 0.500000$$

Dialing further counterclockwise through $45^\circ$, where $\cos 45^\circ = \sin 45^\circ = \sqrt{2}/2 \approx 0.707107$, and $60^\circ$, where $\cos 60^\circ = 1/2$ and $\sin 60^\circ = \sqrt{3}/2$, carries the pointer up to the vertical apex at $90^\circ$. There the horizontal shadow vanishes to $\cos 90^\circ = 0$ while the vertical height reaches $\sin 90^\circ = 1$, showing why cosine and sine are the horizontal shadow and vertical altitude of a rotating unit pointer rather than abstract power series. The third circular ratio, the **tangent** $\tan\theta = \sin\theta / \cos\theta$, takes its name from the Latin *tangens* ("touching"): it measures the vertical height cut off by the extended pointer along the vertical line $x = 1$ tangent to the right-hand rim of the circle.

### Why Engineering Keeps Three Ways to Slice a Circle

Before evaluating any trigonometric function, a scientist or engineer must answer a deceptively rich historical question: what unit measures a full turn around the unit circle? The StackCalc SC-32 supports all three classical angular conventions, indicated continuously on the top status bar:

| Angular Mode | LCD Annunciator | Full Circle Revolution | Right Angle | Primary Engineering Field |
| :--- | :---: | :---: | :---: | :--- |
| **Degrees** | `DEG` (Default) | $360^\circ$ | $90^\circ$ | Structural Civil Engineering, Geodesy, Avionics |
| **Radians** | `RAD` | $2\pi \approx 6.283185\text{ rad}$ | $\pi/2 \approx 1.570796\text{ rad}$ | Mathematical Physics, Calculus, Wave Mechanics |
| **Gradians** | `GRAD` | $400\text{ grad}$ | $100\text{ grad}$ | European Surveying, Mining Engineering |

Why have all three systems survived into the twenty-first century? Because each grew out of a different physical symmetry:
* **Degrees (`DEG`):** Four thousand years ago, Babylonian astronomers noticed that the sun advances against the background constellations by roughly one step per day over a $360$-day schematic year. Better still for base-$60$ arithmetic, $360$ is an extraordinarily abundant integer—divisible without remainder by $2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120,$ and $180$. That abundant divisibility lets a carpenter, clockmaker, or navigator divide a roof truss, a clock face, or a compass rose into halves, thirds, quarters, fifths, sixths, eighths, or twelfths using whole numbers.
* **Radians (`RAD`):** To a mathematician or physicist, dividing a circle into $360$ parts is an arbitrary human convention. Roger Cotes and Leonhard Euler asked a more natural geometric question: how large is the angle $\theta$ when the curved arc length $s$ traced along the rim of a circle equals the straight radius $r$ of the circle itself? Defining an angle as the dimensionless ratio of arc length to radius ($\theta = s / r$) makes one full revolution equal to $2\pi\text{ radians}$ ($\approx 6.283185\text{ rad}$) and one radian equal to $180^\circ / \pi \approx 57.29578^\circ$. Only in radians does the small-angle ratio $\lim_{\theta \to 0} (\sin\theta)/\theta$ equal $1$, ensuring that the derivative of $\sin\theta$ is $\cos\theta$ without an awkward $\pi/180$ scale factor trailing behind every harmonic oscillator or electromagnetic wave equation.
* **Gradians (`GRAD`):** During the French Revolution, the architects of the metric system sought to decimalize angles alongside meters and kilograms. By defining a right angle as $100\text{ gradians}$ (*gons*) and a full circle as $400\text{ gradians}$, they linked terrestrial navigation to the metric system: because the meter was originally defined as one ten-millionth of the meridian quadrant from the Equator to the North Pole ($10,000\text{ km}$ per $100\text{ grad}$), **one gradian of latitude equals $100\text{ kilometers}$ on the surface of the Earth**, and one centigrad ($0.01\text{ grad}$) equals $1\text{ meter}$.

{{blocks:sc32_rpn_calculation|StackCalc SC-32 Live 4-Level XYZT Stack Hardware Display.}}

The active angular mode tells the SC-32 how to interpret circular inputs (`SIN`, `COS`, `TAN`) and what angular units to return from inverse functions (`ASIN`, `ACOS`, `ATAN`) and rectangular-to-polar conversions (`{{key:▸θ,r}}`). Opening **`{{key:MODES}}`** (`{{key:↰}}` + `{{key:+/-}}`) lets you switch among `{{key:DEG}}`, `{{key:RAD}}`, and `{{key:GRAD}}` at any time. When a nautical chart or surveyor's plat specifies an angle in Babylonian sexagesimal **degrees-minutes-seconds** `D.MMSS`—such as $35^\circ 15' 36''$, entered as `35.1536`—pressing **`{{key:▸HR}}`** (shifted above the `5` key) converts Register $X$ in place into decimal degrees (`35.2600°`), while **`{{key:▸HMS}}`** packs decimal degrees or hours back into `D.MMSS` format. Alongside them above the `6` key, **`{{key:▸DEG}}`** and **`{{key:▸RAD}}`** convert Register $X$ between degrees and radians on the fly without altering the active angular mode.

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

To prevent binary radian conversion from corrupting orthogonal geometry, the SC-32 performs **Exact Axial Angle Clamping** before evaluating circular series: in Degrees (`DEG`) or Gradians (`GRAD`) mode, quadrantal multiples of a right angle are reduced modulo a full circle so that $\sin(0^\circ) = 0.0$, $\cos(0^\circ) = 1.0$, $\sin(90^\circ) = 1.0$, $\cos(90^\circ) = 0.0$, $\sin(180^\circ) = 0.0$, $\cos(180^\circ) = -1.0$, $\sin(270^\circ) = -1.0$, and $\cos(270^\circ) = 0.0$ return exact IEEE zero and unity values. Likewise, evaluating $\tan(90^\circ)$ or $\tan(270^\circ)$ triggers `DIVIDE BY 0` (Code 01) rather than returning a bogus $1.63 \times 10^{16}$ reciprocal of rounding noise, and passing a magnitude $|x| > 1$ to `{{key:ASIN}}` or `{{key:ACOS}}` displays `INVALID DATA` (Code 02) while leaving your stack completely intact.

---

## Triangles, Crosswinds & Resolving 2D Vectors

Once you see $\cos\theta$ and $\sin\theta$ as the horizontal and vertical shadows of a tilted arrow, dozens of seemingly unrelated problems across physics, civil surveying, optics, and navigation turn out to be variations on a single theme: splitting a slanted vector into perpendicular components, or reconstructing a slanted vector from its perpendicular parts.

### Projecting Forces, Trajectories & Mountain Summits

In the *Two New Sciences* (1638) {{cite:galilei1638}}, Galileo Galilei made a discovery that launched modern mechanics: when a cannonball or an artillery shell flies through the air (neglecting atmospheric drag), its curved parabolic trajectory combines two independent motions occurring simultaneously at right angles. Horizontally, no force acts on the shell after it leaves the muzzle, so its horizontal velocity $v_{0x} = v_0\cos\theta$ remains constant all the way downrange. Vertically, gravity $g$ pulls downward with constant acceleration, slowing the initial vertical climb rate $v_{0y} = v_0\sin\theta$ until the shell momentarily pauses at its apex altitude $H_{\max}$—where all of its vertical kinetic energy $\frac{1}{2}mv_{0y}^2$ has converted into gravitational potential energy $mgH_{\max}$:

$$H_{\max} = \frac{(v_0 \sin\theta)^2}{2g}, \qquad R = \frac{2 v_{0x} v_{0y}}{g} = \frac{v_0^2 \sin(2\theta)}{g}$$

Through the double-angle identity $2\sin\theta\cos\theta = \sin(2\theta)$, that second equation reveals a striking symmetry: on level ground, maximum range occurs when $\sin(2\theta) = 1$, or $\theta = 45^\circ$, and any two complementary launch angles that sum to $90^\circ$—such as a low $30^\circ$ flat trajectory and a high $60^\circ$ mortar lob—land at the same downrange distance $R$!

That same orthogonal decomposition governs a heavy crate sliding down a ramp inclined at an angle $\theta$ with kinetic friction coefficient $\mu_k$. Gravity pulls straight toward the center of the Earth with force $mg$, but the ramp forces the motion along the tilted surface. Splitting gravity into components parallel and perpendicular to the incline shows that $mg\sin\theta$ pulls the crate downhill while $mg\cos\theta$ presses the crate into the planks, generating a normal force $N = mg\cos\theta$ and an uphill Coulomb friction drag $\mu_k N = \mu_k mg\cos\theta$:

$$a = g (\sin\theta - \mu_k \cos\theta)$$

Mass $m$ cancels out of the equation completely: a light wooden box and a heavy iron safe with the same friction coefficient $\mu_k$ accelerate down the ramp at identical rates, and at the critical **angle of repose** where $\sin\theta = \mu_k\cos\theta$ ($\tan\theta = \mu_k$), downhill gravity and uphill friction balance to zero.

What if you cannot reach the object you want to measure at all? During the Great Trigonometrical Survey of India in the 1850s, surveyors could not carry a measuring chain through the glaciers to the base of Peak XV (Mount Everest). Instead, they used **two-station optical leveling**: sighting the vertical elevation angle $\alpha$ to the mountain summit from Station 1, marching a measured horizontal baseline distance $d$ straight toward the peak to Station 2, and sighting the steeper elevation angle $\beta$. Because the unknown horizontal distances from the summit's plumb line to the two stations are $x_1 = H\cot\alpha$ and $x_2 = H\cot\beta$, their difference $x_1 - x_2$ eliminates the inaccessible distance to the mountain completely and leaves only the measured baseline $d$:

$$d = H(\cot\alpha - \cot\beta) \implies H = \frac{d}{\cot\alpha - \cot\beta} = \frac{d}{\frac{1}{\tan\alpha} - \frac{1}{\tan\beta}}$$

Because the keypad needs no dedicated cotangent button when `{{key:1/x}}` sits on the primary plane, you evaluate each cotangent in place via `{{key:TAN}} {{key:1/x}}`, subtract $\cot\beta$ from $\cot\alpha$ on Shelf $X$, type the baseline $d$, and invert the division order with `{{key:x⇄y}} {{key:÷}}`.

Even the ticking of a grandfather clock hides a circular projection: at wider swing amplitudes $\theta_0$, the true restoring force $\sin\theta$ falls slightly below the small-angle approximation $\theta$, stretching the small-angle period $T_0 = 2\pi\sqrt{L/g}$ by the leading half-angle sine factor $T \approx T_0[1 + \frac{1}{4}\sin^2(\theta_0/2)]$ ($+3.66\%$ at $\theta_0 = 45^\circ$). In **Chapter 8**, we will return to Christiaan Huygens's 1656 clockwork discovery and use Romberg numerical integration (`{{key:∫}}`) to integrate the exact complete elliptic integral $K(\sin(\theta_0/2))$ across any swing angle.

### Reversing the Projection: Snell's Refraction, Brewster's Angle & the Inverse Tangent

Direct trigonometric functions take an angle and return a dimensionless ratio of lengths; **inverse trigonometric functions** (`{{key:ASIN}}`, `{{key:ACOS}}`, `{{key:ATAN}}`) run the unit circle in reverse, taking a measured physical ratio of speeds, refractive indices, accelerations, or lengths and recovering the geometric angle hidden inside.

Nowhere is that reversal more vivid than in the behavior of light crossing a boundary between two transparent media of refractive indices $n_1$ and $n_2$. After Claudius Ptolemy measured the bending of light in water, natural philosophers searched for the exact mathematical law of refraction—first discovered in 984 CE in Baghdad by the Persian mathematician and optics pioneer **Ibn Sahl** (*On Burning Mirrors and Lenses*), and independently rediscovered in Europe by **Thomas Harriot** (1602 in London) and **Willebrord Snell** (1621 in Leiden): nature holds constant not the ratio of the angles themselves, but the ratio of their **sines** ($n_1\sin\theta_1 = n_2\sin\theta_2$). When a pulse of laser light travels inside an optical fiber core ($n_1 = 1.480$) surrounded by a glass cladding of slightly lower refractive index ($n_2 = 1.450$), any ray striking the boundary bends away from the normal. At the **critical angle** $\theta_c$, the refracted ray skims right along the glass interface at $\theta_2 = 90^\circ$ ($\sin 90^\circ = 1$), so `{{key:ASIN}}` recovers the exact trapping threshold:

$$\theta_c = \arcsin\left(\frac{n_2}{n_1}\right)$$

Every ray striking the core wall at an angle steeper than $\theta_c$ cannot escape into the cladding at all; it undergoes $100\%$ lossless **Total Internal Reflection**, guiding transoceanic data pulses across thousands of kilometers of glass.

Two centuries after Snell, in 1815, the Scottish physicist **Sir David Brewster** asked a complementary question: at what incidence angle $\theta_B$ does glare reflected off a pane of glass or a sunlit lake become $100\%$ horizontally polarized? Brewster discovered that complete polarization occurs at the exact angle where the reflected ray and the refracted ray meet at a **$90^\circ$ right angle** ($\theta_B + \theta_2 = 90^\circ$). Because the sine of the complementary angle $90^\circ - \theta_B$ equals $\cos\theta_B$, Snell's Law becomes $n_1\sin\theta_B = n_2\cos\theta_B$, turning the ratio of refractive indices into a **tangent**:

$$\tan\theta_B = \frac{\sin\theta_B}{\cos\theta_B} = \frac{n_2}{n_1} \implies \theta_B = \arctan\left(\frac{n_2}{n_1}\right)$$

Compare those two optical equations (`ASIN` vs. `ATAN`) and you can see why the three inverse keys partition geometry into two distinct domains. Because neither the horizontal shadow $\cos\theta$ nor the vertical height $\sin\theta$ on the unit circle can ever exceed the unit hypotenuse $1$, `{{key:ASIN}}` and `{{key:ACOS}}` accept ratios strictly within $[-1, +1]$, mapping onto principal angles $[-90^\circ, +90^\circ]$ and $[0^\circ, 180^\circ]$. By contrast, the tangent slope $\tan\theta = y/x$ can grow arbitrarily steep as a line tilts toward the vertical axis, so `{{key:ATAN}}` maps any real ratio $(-\infty, +\infty)$ smoothly onto $(-90^\circ, +90^\circ)$—making it the universal tool whenever perpendicular forces, velocities, or orbital coordinates are divided one by the other.

### Oblique Triangles and the Law of Cosines

In land surveying and wave physics, nature rarely hands us right-angled triangles. When a surveyor stands at a corner monument $C$ and measures straight-line distances $a$ and $b$ to two boundary markers separated by an included angle $C \ne 90^\circ$, how do we find the opposite side $c$ without a right angle?

Drop a perpendicular altitude $h$ from the tip of side $b$ down to side $a$, splitting the oblique triangle into two right triangles:
* The vertical altitude has height $h = b\sin C$.
* The horizontal shadow of side $b$ along side $a$ has length $b\cos C$, leaving $(a - b\cos C)$ as the base of the outer right triangle.

Now apply the ordinary Pythagorean theorem to that outer right triangle, and watch how the unit-circle identity $\cos^2 C + \sin^2 C = 1$ simplifies the algebra:

$$c^2 = (a - b\cos C)^2 + (b\sin C)^2 = a^2 + b^2(\cos^2 C + \sin^2 C) - 2ab\cos C$$

Taking the square root gives the **Law of Cosines**:

$$c = \sqrt{a^2 + b^2 - 2 a b \cos C}$$

On the SC-32, you never need parentheses or scratch registers to evaluate the Law of Cosines: form the Pythagorean sum $a^2 + b^2$ first (`a {{key:x²}} b {{key:x²}} {{key:+}}`) and let it wait on Shelf $Y$ while you build the cross-term $2ab\cos C$ on Shelf $X$ (`2 {{key:ENTER}} a {{key:×}} b {{key:×}} C {{key:COS}} {{key:×}}`), then finish in two strokes with `{{key:-}} {{key:√x}}`. This single formula unifies all planar triangles:
* When $C = 90^\circ$, $\cos 90^\circ = 0$ and the cross-term vanishes, recovering the Pythagorean theorem ($c = \sqrt{a^2 + b^2}$).
* When $C < 90^\circ$ (an acute angle), $\cos C > 0$ pulls the third side shorter than a right-triangle hypotenuse.
* When $C > 90^\circ$ (an obtuse angle), $\cos C < 0$ makes $-2ab\cos C$ positive, stretching the third side longer!

Flip the minus sign to a plus sign (the supplementary exterior angle $180^\circ - \Delta\phi$), and the same geometry governs **coherent wave interference**: when two acoustic or electromagnetic waves of amplitudes $A_1$ and $A_2$ arrive at a sensor with phase difference $\Delta\phi$, their superposed amplitude is the vector resultant of two rotating phasors placed tip-to-tail:

$$A_{\text{resultant}} = \sqrt{A_1^2 + A_2^2 + 2 A_1 A_2 \cos(\Delta\phi)}$$

### The $(Y, X)$ Coordinate Plane: Polar $\leftrightarrow$ Rectangular Vector Conversion

Up to this point in Volume II, every binary key on the SC-32 has treated Registers $Y$ and $X$ as two scalar numbers waiting to be combined into one. When you work with two-dimensional vectors—forces on a physics laboratory force table, aircraft crosswind velocity triangles, land-surveying boundary traverses, or AC electrical power triangles—Registers $Y$ and $X$ take on a unified geometric identity: **together, the $(Y, X)$ register pair forms a two-dimensional coordinate plane**.

The SC-32 provides two dedicated keys that transform the $(Y, X)$ pair in place between Cartesian rectangular coordinates $(x, y)$ and polar coordinates $(r, \theta)$ without disturbing Registers $Z$ and $T$:

| Transformation | Dedicated Keystroke | Stack Input ($Y, X$) | Stack Output ($Y, X$) | Mathematical Formula |
| :--- | :--- | :--- | :--- | :--- |
| **Polar to Rectangular** | `{{key:▸y,x}}` | $Y = \theta$ (Angle in active mode)<br>$X = r$ (Radius / Magnitude) | $Y = y = r \sin\theta$<br>$X = x = r \cos\theta$ | $(x, y) = (r\cos\theta, r\sin\theta)$ |
| **Rectangular to Polar** | `{{key:▸θ,r}}` | $Y = y$ (Orthogonal vertical)<br>$X = x$ (Orthogonal horizontal) | $Y = \theta = \operatorname{atan2}(y, x)$<br>$X = r = \sqrt{x^2 + y^2}$ | $(r, \theta) = (\sqrt{x^2+y^2}, \operatorname{atan2}(y, x))$ |

Look closely at the mnemonic printed on the key legends: in `{{key:▸y,x}}`, the first letter after the arrow ($y$) lands in Register $Y$ and the second letter ($x$) lands in Register $X$; in `{{key:▸θ,r}}`, the angle $\theta$ lands in Register $Y$ and the radial magnitude $r$ lands in Register $X$.

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

Why is this two-register coordinate plane so fundamental? Because **vectors pointing in different directions can never be added by their magnitudes alone**. In 1586, the Flemish engineer **Simon Stevin** proved this law of nature with his *Wreath of Spheres* (*Clootcrans*) thought experiment, printing the diagram on the title page of his *Beghinselen der Weeghconst* under the motto *"Wonder en is gheen wonder"* ("What appears a wonder is not a wonder"). By draping a closed loop of evenly spaced lead balls over an asymmetric frictionless wedge and noting that a closed necklace cannot spin forever as a perpetual-motion machine, Stevin established the **parallelogram of vectors**. To combine two slanted forces or velocities, you first resolve each arrow into its horizontal ($x = r\cos\theta$) and vertical ($y = r\sin\theta$) components, sum the horizontal and vertical parts separately, and reconstruct the resultant arrow from the summed components.

That three-beat rhythm—**project via `{{key:▸y,x}}`, sum the orthogonal components, and recombine via `{{key:▸θ,r}}`**—unifies vector mechanics across sea, air, and land. When a mariner steers across a tidal current or a pilot flies at true airspeed $\vec{V}_{\text{air}}$ through an upper-level crosswind $\vec{V}_{\text{wind}}$, the craft's true path over the Earth is the vector sum $\vec{V}_{\text{ground}} = \vec{V}_{\text{air}} + \vec{V}_{\text{wind}}$, just as hanging two tension weights on a laboratory force table requires an equal and opposite resultant $\vec{F}_3 = -(\vec{F}_1 + \vec{F}_2)$ to hold the central ring in static equilibrium.

Better still, when a land surveyor walks a multi-leg property boundary and records the distance $r_i$ and compass angle $\theta_i$ of each course, verifying that the boundary closes back onto its starting iron monument requires summing all horizontal Easting departures ($\Sigma\Delta x$) and all vertical Northing latitudes ($\Sigma\Delta y$) around the loop:

$$\Sigma \Delta x = \sum r_i \cos\theta_i = 0, \qquad \Sigma \Delta y = \sum r_i \sin\theta_i = 0$$

Here the SC-32 reveals one of its cleanest architectural symmetries: **because `{{key:▸y,x}}` places $\Delta y$ in Register $Y$ and $\Delta x$ in Register $X$, its output matches the exact $(Y, X)$ input convention of the statistical accumulator key `{{key:Σ+}}`**. Chaining `{{key:▸y,x}} {{key:Σ+}}` after each survey course accumulates an entire four-, ten-, or twenty-leg boundary traverse in statistical memory without touching a single named storage variable!

### Spherical Geodesy, Great-Circle Orthodromes & Avian Celestial Navigation

Once an aircraft, a ship, or a radio link spans thousands of kilometers across an ocean, flat-Earth Cartesian trigonometry breaks down. On a globe of mean radius $R_E = 6,371.0\text{ km}$, the shortest path between two cities at latitude/longitude coordinates $(\phi_1, \lambda_1)$ and $(\phi_2, \lambda_2)$ is not a straight constant-compass line on a flat Mercator map (a *rhumb line* or *loxodrome*), but a **Great-Circle orthodrome**—the arc cut on the surface by a plane slicing through both cities and the center of the Earth.

Where does the **Spherical Law of Cosines** come from? You can derive it in thirty seconds using the 3D unit-sphere projections we just learned! On a unit sphere of radius $r = 1$, a city at latitude $\phi$ and longitude $\lambda$ has vertical polar height $z = \sin\phi$ and equatorial shadow radius $\cos\phi$, which projects onto the $(x, y)$ axes as $x = \cos\phi\cos\lambda$ and $y = \cos\phi\sin\lambda$:

$$\hat{u}_1 = \begin{bmatrix} \cos\phi_1\cos\lambda_1 \\ \cos\phi_1\sin\lambda_1 \\ \sin\phi_1 \end{bmatrix}, \qquad \hat{u}_2 = \begin{bmatrix} \cos\phi_2\cos\lambda_2 \\ \cos\phi_2\sin\lambda_2 \\ \sin\phi_2 \end{bmatrix}$$

Taking the 3D dot product $\hat{u}_1 \cdot \hat{u}_2 = \cos d$ between the two unit vectors and applying the cosine difference identity $\cos\lambda_1\cos\lambda_2 + \sin\lambda_1\sin\lambda_2 = \cos(\lambda_2 - \lambda_1)$ yields the central geocentric angle $d$ as the sum of the polar projection ($\sin\phi_1\sin\phi_2$) and the equatorial projection ($\cos\phi_1\cos\phi_2\cos\Delta\lambda$):

$$\cos d = \sin\phi_1 \sin\phi_2 + \cos\phi_1 \cos\phi_2 \cos(\lambda_2 - \lambda_1), \qquad D = R_E \times d_{\text{rad}}$$

Because longitudinal circles converge toward the poles like the slices of an orange ($\cos\phi < 1$), flying from San Francisco ($\phi_1 \approx 37.6^\circ\text{ N}$) to Tokyo ($\phi_2 \approx 35.8^\circ\text{ N}$) along the Great Circle arcs up toward the Aleutian Islands near $50^\circ\text{ N}$—where each degree of longitude is much shorter than at $36^\circ\text{ N}$—saving hundreds of kilometers of fuel and flight time compared to flying due west along a parallel of latitude!

This same Spherical Law of Cosines solves the **astronomical triangle** linking the North Celestial Pole, an observer's zenith at latitude $\phi$, and the sun at seasonal declination $\delta$ and solar hour angle $\omega$ ($15^\circ$ per hour from solar noon), yielding the sun's horizon elevation angle $\alpha$ and compass azimuth $\gamma_s$:

$$\sin\alpha = \sin\phi \sin\delta + \cos\phi \cos\delta \cos\omega, \qquad \cos\gamma_s = \frac{\sin\alpha \sin\phi - \sin\delta}{\cos\alpha \cos\phi}$$

Long before human aviation, migratory birds mastered all three navigation algorithms—the wind triangle, spherical great-circle orthodromes, and time-compensated solar azimuths. Every autumn, the **bar-tailed godwit** (*Limosa lapponica*) lifts off from Alaska's tidal flats and flies **$11,000\text{ kilometers}$ non-stop across the open Pacific Ocean to New Zealand** in nine days without food, water, or landmarks. Because the sun marches across the sky at $15^\circ\text{ per hour}$, a bird steering by the sun without a clock would spiral off course by $90^\circ$ every six hours; the godwit combines an internal circadian clock with solar elevation/azimuth geometry and retinal magnetoreception to follow a spherical great-circle orthodrome while continuously crabbing into crosswinds (`{{key:▸y,x}}` vector addition) so its ground track lands squarely on its New Zealand estuary.

And when satellite geodesy requires sub-meter precision across the globe, we step from a sphere to Isaac Newton's **oblate spheroid**. In the *Principia* (1687), Newton deduced that Earth's daily centrifugal rotation causes the equator to bulge outward by $21.385\text{ km}$ relative to the poles. Modern GPS/GNSS codifies that shape in the **World Geodetic System 1984 (WGS84)** reference ellipsoid (equatorial semi-major axis $a = 6,378,137.0\text{ m}$, flattening $f = 1/298.257223563$, first eccentricity squared $e^2 = 2f - f^2 \approx 0.00669437999014$), where a receiver at geodetic latitude $\phi$, longitude $\lambda$, and height $h$ has prime-vertical radius of curvature $N(\phi)$ and Earth-Centered Earth-Fixed coordinates $(X, Y, Z)$:

$$N(\phi) = \frac{a}{\sqrt{1 - e^2 \sin^2\phi}}, \qquad \begin{bmatrix} X \\ Y \\ Z \end{bmatrix} = \begin{bmatrix} (N(\phi) + h) \cos\phi \cos\lambda \\ (N(\phi) + h) \cos\phi \sin\lambda \\ (N(\phi)(1 - e^2) + h) \sin\phi \end{bmatrix}$$

---

## Why Hanging Chains Refuse to Form Parabolas: Hyperbolic Functions

### The 1691 Bernoulli Contest, Catenary Chains & the Gateway Arch

Look up at a steel power cable sagging between two transmission towers, or a heavy anchor chain draped between two harbor bollards. What curve does a flexible chain trace when hanging freely under its own weight?

For decades, the greatest minds of the Scientific Revolution got the answer wrong. In his *Two New Sciences* (1638), Galileo Galilei wrote that a hanging chain forms a **parabola** ($y = kx^2$), and for half a century architects and physicists repeated Galileo's claim. Only in 1646 did a seventeen-year-old Dutch student named Christiaan Huygens prove geometrically that a hanging chain cannot possibly be a parabola—a startling refutation that left Europe's finest geometers asking why Galileo's intuition had failed.

In May 1690, the Swiss mathematician Jakob Bernoulli issued a public challenge in the journal *Acta Eruditorum*, daring the mathematicians of Europe to find the true equation of the hanging chain. Within a year, three men solved the challenge independently: **Christiaan Huygens**, **Gottfried Wilhelm Leibniz**, and Jakob's younger brother **Johann Bernoulli**. They proved that a parabola appears only when load is distributed uniformly per unit of *horizontal span* $dx$—as happens in a suspension bridge like the Golden Gate, where the heavy flat roadway deck hangs from vertical suspender cables spaced evenly along the horizontal axis.

In a freely hanging chain or power line, however, there is no roadway deck: the weight is distributed uniformly per unit of *curved arc length* $ds = \sqrt{1 + (dy/dx)^2}\,dx$ along the chain itself! Near the supports, where the chain tilts steeply, each meter of horizontal span contains much more chain—and therefore much more weight—than near the flat bottom of the sag.

Follow how Huygens, Leibniz, and Johann Bernoulli solved the force balance of a chain segment of arc length $s$, measured from the lowest vertex (where the chain hangs flat under horizontal tension $T_0$) up to a point $(x, y)$ where the chain tilts at angle $\psi$:
1. **Horizontal Equilibrium:** Because no horizontal external forces act on the hanging segment, the horizontal component of tension $T\cos\psi$ must balance the bottom tension $T_0$ everywhere along the span:

   $$T\cos\psi = T_0$$

2. **Vertical Equilibrium:** The upward vertical component of tension $T\sin\psi$ must support the downward gravitational weight $w \cdot s$ of the arc length $s$ hanging below $(x, y)$ (where $w$ is the linear weight density in Newtons per meter):

   $$T\sin\psi = w \cdot s$$

3. **Dividing Vertical by Horizontal:** Dividing the second equation by the first eliminates the unknown tension $T$ and links the slope $\frac{dy}{dx} = \tan\psi$ to the arc length $s$:

   $$\frac{dy}{dx} = \tan\psi = \frac{w \cdot s}{T_0} = \frac{s}{a}, \qquad \text{where } a = \frac{T_0}{w}$$

Differentiating with respect to $x$ requires a function whose derivative is related to its own arc length $ds/dx = \sqrt{1 + (dy/dx)^2}$—and as Leibniz and Bernoulli discovered, that function is the symmetric combination of Euler's rising and decaying exponentials $e^{x/a}$ and $e^{-x/a}$, which Huygens christened the **catenary** (from the Latin *catena*, "chain") and which we call the **hyperbolic cosine**:

$$\cosh(u) = \frac{e^u + e^{-u}}{2}, \qquad \sinh(u) = \frac{e^u - e^{-u}}{2}, \qquad \tanh(u) = \frac{\sinh(u)}{\cosh(u)} = \frac{e^u - e^{-u}}{e^u + e^{-u}}$$

With the origin placed at the lowest point of the cable, the vertical sag $y(x)$ follows the hyperbolic cosine while the curved arc length $s(x)$ of cable hanging between the vertex and $x$ follows the hyperbolic sine:

$$y(x) = a\left(\cosh\left(\frac{x}{a}\right) - 1\right), \qquad s(x) = a\sinh\left(\frac{x}{a}\right)$$

Why are these exponential combinations called *hyperbolic* functions, and why do they share keys with $\sin$, $\cos$, and $\tan$? Because whereas the circular functions $(\cos u, \sin u)$ parameterize points on the **unit circle** $x^2 + y^2 = 1$ (sweeping out a circular sector of area $u/2$), squaring and subtracting $\cosh u$ and $\sinh u$ reveals that $(\cosh u, \sinh u)$ parameterize the right-hand branch of the **unit hyperbola** $x^2 - y^2 = 1$ (sweeping out a hyperbolic sector of area $u/2$):

$$\cosh^2(u) - \sinh^2(u) = \left(\frac{e^u + e^{-u}}{2}\right)^2 - \left(\frac{e^u - e^{-u}}{2}\right)^2 = \frac{e^{2u} + 2 + e^{-2u} - (e^{2u} - 2 + e^{-2u})}{4} = 1$$

Better still, their derivatives mirror the circular functions without the minus sign on $\frac{d}{du}\cosh u$:

$$\frac{d}{du}\sinh(u) = \cosh(u), \qquad \frac{d}{du}\cosh(u) = +\sinh(u), \qquad \frac{d}{du}\tanh(u) = \operatorname{sech}^2(u) = 1 - \tanh^2(u)$$

Turn a hanging catenary chain upside down, and every link swaps pure tension for pure compression free of bending torque. That is why Robert Hooke declared to the Royal Society in 1675, *"As hangs the flexible chain, so but inverted will stand the rigid arch,"* and why architect Eero Saarinen and structural engineer Hannskarl Bandel shaped the $192\text{-meter}$ stainless-steel **Gateway Arch in St. Louis** as an inverted hyperbolic cosine catenary.

### Ocean Tsunami Dispersion, Relativistic Rapidity & The HYP Prefix

On the SC-32 keypad, the hyperbolic prefix **`{{key:HYP}}`** lives on Left Shift `{{key:↰}}` above `{{key:R↓}}`. Pressing `{{key:HYP}}` arms the transient `HYP` annunciator and pairs with the primary keys `{{key:SIN}}`, `{{key:COS}}`, and `{{key:TAN}}` for $\sinh(x)$, $\cosh(x)$, and $\tanh(x)$, or with their Left-Shifted inverses `{{key:ASIN}}`, `{{key:ACOS}}`, and `{{key:ATAN}}` for the inverse hyperbolic functions (and because hyperbolic arguments are dimensionless real numbers, `{{key:HYP}}` operations are completely independent of `DEG`/`RAD`/`GRAD` angular modes):

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

  Because $\tanh(\theta)$ approaches $1.0$ asymptotically as $\theta \to \infty$, you can add finite rocket boosts forever and approach closer and closer to $c$ while never crossing the cosmic speed limit.

---

## On the Stack: Circular, Vector & Hyperbolic Projections

Trigonometric and vector calculations on the SC-32 rest on two architectural rules. First, every unary circular (`{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`, `{{key:ASIN}}`, `{{key:ACOS}}`, `{{key:ATAN}}`) and hyperbolic (`{{key:HYP}}`) key transforms Register $X$ in place under the active angular unit (`{{key:DEG}}` for degrees, or radians and gradians when selected), leaving upper shelves untouched for multi-term projections and nested radicals. Second, the coordinate keys `{{key:▸y,x}}` and `{{key:▸θ,r}}` treat the lower two shelves as a two-dimensional plane, mapping polar $(Y = \theta,\; X = r)$ to rectangular $(Y = y,\; X = x)$ so that chaining `{{key:▸y,x}} {{key:Σ+}}` accumulates 2D survey traverses and wind vectors straight into statistical memory.

### Angular Mode Sanity Check & Direct Circular Projections

Throughout the traces below, we operate in **Degrees mode (`{{key:DEG}}`)** unless radians are explicitly required. Before starting a trigonometric calculation, a quick two-keystroke check via `{{res:sc32_04_trig_vectors_polar_seq_56:keys}}` confirms your active mode: in Degrees mode (`{{key:DEG}}`), $\sin(45^\circ)$ displays the familiar unit-diagonal projection `0.707106781187` ($\sqrt{2}/2$), whereas if the calculator was left in radian units from an earlier session, $\sin(45\text{ rad})$ returns `0.850903524534`—a gentle reminder to press `{{key:DEG}}`.

Why do almost all planar trigonometric projections execute across Registers $X$ and $Y$ alone while leaving Registers $Z$ and $T$ completely empty? Because every circular function key (`{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`) is a **unary in-place transformer**: when you type an angle into Register $X$ and press `{{key:SIN}}` or `{{key:COS}}`, the angle is replaced right on Shelf $X$ by its dimensionless unit-circle shadow without lifting or disturbing any number waiting on Shelf $Y$! Walk through five classical projection problems to see how that in-place geometry unfolds on the bottom two shelves.

**Galileo's Projectile Apex & Range ($H_{\max} = \frac{(v_0\sin\theta)^2}{2g}$, $R = \frac{v_0^2\sin(2\theta)}{g}$).** When an artillery shell leaves the muzzle at $v_0 = 85.0\text{ m/s}$ inclined at $\theta = 38.0^\circ$ ($g = 9.80665\text{ m/s}^2$), how high does it climb before gravity brings its vertical ascent to a momentary halt? Running `{{res:sc32_04_trig_vectors_polar_seq_09:keys}}` parks the muzzle speed $85.0\text{ m/s}$ on Shelf $Y$ while transforming $38^\circ$ in place on Shelf $X$ into its vertical unit-circle shadow $\sin(38^\circ) = 0.615661$, without nudging $85.0\text{ m/s}$ into Register $Z$. Multiplying those two terms yields the initial vertical climb velocity $v_{0y} = 52.3312\text{ m/s}$, and squaring in place produces $v_{0y}^2 = 2,738.5574\text{ m}^2/\text{s}^2$—twice the vertical kinetic energy per kilogram of shell.

While that vertical energy waits on Shelf $Y$, forming the gravitational divisor $2g = 19.6133\text{ m/s}^2$ on Shelf $X$ and dividing places the apex altitude **`{{res:sc32_04_trig_vectors_polar_seq_09:value}}`** $\text{m}$ in Register $X$. For the horizontal downrange impact distance across level terrain, evaluating the double-angle factor $\sin(2\theta) = \sin(76^\circ) = 0.9703$ via `{{res:sc32_04_trig_vectors_polar_seq_10:keys}}` similarly resolves $R =$ **`{{res:sc32_04_trig_vectors_polar_seq_10:value}}`** $\text{m}$ across the bottom two shelves.

**Inclined-Plane Friction & Single-Entry `LASTX` Angle Recovery ($a = g(\sin\theta - \mu_k\cos\theta)$).** When a heavy supply crate slides down a loading ramp tilted at $\theta = 34.0^\circ$ against a kinetic friction coefficient of $\mu_k = 0.22$ ($g = 9.80665\text{ m/s}^2$), two perpendicular projections of gravity compete along the planks: the downhill pull $\sin(34^\circ) = 0.5592\,g$ and the normal clamping force $\cos(34^\circ) = 0.8290\,g$, which scales by $\mu_k = 0.22$ into an uphill friction drag of $0.1824\,g$. Running `{{res:sc32_04_trig_vectors_polar_seq_23:keys}}` places $\sin(34^\circ) = 0.5592$ on Shelf $Y$ while building the friction term $0.22\cos(34^\circ) = 0.1824$ on Shelf $X$, subtracts them to isolate the net dimensionless traction factor $0.3768$, and scales by $g = 9.80665\text{ m/s}^2$ to yield a downhill acceleration of $a = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_23:value}}\text{ m/s}^2}$. Better still, because `{{key:SIN}}` saves the raw ramp angle $34.0^\circ$ inside **`{{key:LASTX}}`**, you never have to key the incline angle a second time—recalling `{{key:LASTX}}` right before `{{key:COS}}` recovers $34.0^\circ$ automatically while Registers $Z$ and $T$ remain at zero.

**Two-Station Optical Mountain Triangulation ($H = \frac{d}{\cot\alpha - \cot\beta}$).** Why did we never clutter the SC-32 faceplate with dedicated secant, cosecant, or cotangent keys? Because the primary-plane reciprocal key `{{key:1/x}}` inverts any circular ratio in place on Register $X$. When surveyors sight an inaccessible mountain peak across a level baseline of $d = 500.0\text{ m}$—measuring elevation angle $\alpha = 24.5^\circ$ at Station 1 and steeper angle $\beta = 31.2^\circ$ at Station 2—each cotangent $\cot\theta = x/H$ measures the horizontal ground distance per meter of summit height. Executing `{{res:sc32_04_trig_vectors_polar_seq_28:keys}}` inverts $\tan(24.5^\circ)$ into $\cot(24.5^\circ) = 2.1943$ on Shelf $Y$, subtracts $\cot(31.2^\circ) = 1.6512$ on Shelf $X$ to isolate the **differential cotangent** $\Delta\cot = 0.5431\text{ m/m}$, and uses `{{key:x⇄y}}` to divide the $500\text{ m}$ baseline by $0.5431$, revealing a summit elevation of $H = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_28:value}}\text{ meters}}$.

**Large-Amplitude Pendulum Period Dilation ($T \approx T_0[1 + \frac{1}{4}\sin^2(\theta_0/2)]$).** By the same single-register economy, evaluating the nonlinear period stretch of a grandfather clock pendulum ($T_0 = 2.000\text{ s}$) released from a wide $\theta_0 = 45.0^\circ$ swing (`{{res:sc32_04_trig_vectors_polar_seq_29:keys}}`) squares the half-angle sine $\sin(22.5^\circ)$ in place to $\sin^2(22.5^\circ) = 0.1464$, scales by $1/4$ and adds unity to form the dilation factor $1.0366$, and multiplies by $T_0 = 2.0\text{ s}$ to reveal a $3.66\%$ period stretch to $T = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_29:value}}\text{ seconds}}$.

**Multi-Tier Trigonometric Quotients & Nested Radical Cascades.** Even expressions that look on paper like towering walls of brackets—

$$x_1 = \frac{\sin(35^\circ) \cos(42^\circ) + \tan(18^\circ)}{\sqrt{\sin^2(65^\circ) + \cos^2(25^\circ)}}, \qquad x_2 = \sqrt{\cos(28^\circ) + \sqrt{\sin(48^\circ) + \sqrt{\tan(15^\circ)}}}$$

—never touch Register $T$ because every circular function, square, and square root transforms Register $X$ in place! In the compound fraction $x_1$ (`{{res:sc32_04_trig_vectors_polar_seq_40:keys}}`), the product $\sin(35^\circ)\cos(42^\circ)$ and $\tan(18^\circ)$ fold the entire numerator into a single scalar $0.7512$ on Shelf $X$. As the denominator quadrature $\sqrt{\sin^2(65^\circ) + \cos^2(25^\circ)} = \sqrt{0.8214 + 0.8214} = 1.2817$ then assembles on Shelf $X$ via `{{key:x²}}` and `{{key:√x}}`, that numerator $0.7512$ waits quietly on Shelf $Y$ (momentarily nudging to $Z$ while the two squared terms add) before dividing to **`0.5861`**.

Better yet, in the three-story nested trigonometric radical $x_2$ (`{{res:sc32_04_trig_vectors_polar_seq_53:keys}}`), working from the deepest inner radical outward evaluates $\sqrt{\tan(15^\circ)} = \sqrt{0.2679} = 0.5176$ in Register $X$, adds $\sin(48^\circ) = 0.7431$ and takes the second root to reach $\sqrt{1.2607} = 1.1228$, and adds $\cos(28^\circ) = 0.8829$ before the final `{{key:√x}}` lands on **`{{res:sc32_04_trig_vectors_polar_seq_53:value}}`**—all while Registers $Z$ and $T$ remain at zero across the entire nine-stroke trace!

### Inverse Trigonometry & Oblique Triangles on the Stack

Just as `{{key:SIN}}`, `{{key:COS}}`, and `{{key:TAN}}` project an angle onto a dimensionless ratio in Register $X$, the inverse keys `{{key:ASIN}}`, `{{key:ACOS}}`, and `{{key:ATAN}}` recover the geometric angle from a physical ratio right inside Register $X$—and only call upon upper stack registers when a multi-part geocentric ratio must be assembled first.

**Optical Fiber Critical Angle (`{{key:ASIN}}`).** When a pulse of laser light travels inside a silica optical fiber core of refractive index $n_1 = 1.480$ surrounded by glass cladding of index $n_2 = 1.450$, dividing the cladding index by the core index in `{{res:sc32_04_trig_vectors_polar_seq_15:keys}}` places the critical sine ratio $n_2/n_1 = 0.9797$ in Register $X$. Tapping `{{key:ASIN}}` converts that ratio in place into Snell's critical angle $\theta_c = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_15:value}}^\circ}$—proving that any ray grazing within $90^\circ - 78.44^\circ = 11.56^\circ$ of the fiber wall undergoes $100\%$ lossless Total Internal Reflection.

**Banked Highway Super-Elevation (`{{key:ATAN}}`).** Similarly, when a civil engineer banks an icy highway curve of radius $R = 350.0\text{ m}$ for vehicles traveling at $v = 100.0\text{ km/h}$ ($g = 9.80665\text{ m/s}^2$), the required cross-slope tangent $\tan\theta = \frac{v^2}{gR}$ is the ratio of horizontal centripetal acceleration $v^2/R$ to vertical gravity $g$. Running `{{res:sc32_04_trig_vectors_polar_seq_16:keys}}` converts $100\text{ km/h}$ (divided by $3.6$) into $27.7778\text{ m/s}$, squares it in place to $v^2 = 771.6049\text{ m}^2/\text{s}^2$, divides by $gR = 3,432.3275\text{ m}^2/\text{s}^2$ to isolate the lateral $G$-load ratio $\tan\theta = 0.2248$ in Register $X$, and applies `{{key:ATAN}}` to extract the zero-slip super-elevation angle $\theta = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_16:value}}^\circ}$.

**Four-Register Geocentric Satellite Look-Angle Elevation.** Now contrast that single-ratio highway turn with pointing a ground-station tracking dish at a low-Earth-orbit satellite at altitude $h = 850\text{ km}$ above an Earth of radius $R_E = 6,371\text{ km}$ and geocentric angular separation $\gamma = 18.0^\circ$:

$$\tan E = \frac{\cos\gamma - \frac{R_E}{R_E + h}}{\sin\gamma}$$

Why does this trace (`{{res:sc32_04_trig_vectors_polar_seq_18:keys}}` $\to E = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_18:value}}^\circ}$) actively engage all four registers ($T, Z, Y, X$)? Because after you evaluate the horizon projection $\cos(18^\circ) = 0.9511$ on Row 1, computing the Earth-to-orbit radius ratio $\frac{6371}{6371 + 850} = \frac{6371}{7221} = 0.8823$ requires two `{{key:ENTER}}` strokes that lift $0.9511$ up into Register $Z$ and Register $T$! When `{{key:+}}` and `{{key:÷}}` collapse that radius ratio into $0.8823$, Register $T$'s automatic replication copies $0.9511$ back down into Register $Y$ so `{{key:-}}` can form the net vertical clearance $0.9511 - 0.8823 = 0.0688$ in Register $X$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `18 {{key:COS}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.9511$ | Cosine of angular distance $\cos\gamma$ |
| `6371 {{key:ENTER}} 6371 {{key:ENTER}} 850 {{key:+}} {{key:÷}} {{key:-}}` | $0.9511$ | $0.9511$ | $0.9511$ | $0.0688$ | Subtract orbital radius ratio $R_E / (R_E + h)$ |
| `18 {{key:SIN}} {{key:÷}}` | $0.9511$ | $0.9511$ | $0.9511$ | $0.2225$ | Divide by sine $\sin\gamma$ for elevation tangent |
| `{{key:ATAN}}` | $0.9511$ | $0.9511$ | $0.9511$ | **$12.5462$** | Extract ground satellite elevation angle $E$ (degrees) |

Once the satellite is acquired along an elliptical orbit of eccentricity $e = 0.240$, **Carl Friedrich Gauss's half-angle tangent transformation** $\tan(\nu/2) = \sqrt{\frac{1 + e}{1 - e}}\tan(E/2)$ converts Kepler's eccentric anomaly $E = 40.0^\circ$ into the true polar anomaly $\nu$: evaluating the eccentricity stretch factor $\sqrt{1.240/0.760} \approx 1.2773$, multiplying by $\tan(20^\circ) = 0.3640$, and inverting with `{{key:ATAN}}` before doubling (`{{res:sc32_04_trig_vectors_polar_seq_37:keys}}`) pinpoints the spacecraft at $\nu = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_37:value}}^\circ}$.

**The Law of Cosines ($c = \sqrt{a^2 + b^2 - 2ab\cos C}$).** Why do oblique triangles and interfering acoustic waves need only Shelves $Y$ and $X$ on the SC-32? When a surveyor stands at corner $C$ and sights two boundary markers at $a = 45.0\text{ m}$ and $b = 62.0\text{ m}$ separated by an included angle of $C = 48.0^\circ$ (`{{res:sc32_04_trig_vectors_polar_seq_11:keys}}`), squaring both legs in place and summing them establishes the right-triangle Pythagorean baseline $a^2 + b^2 = 2,025 + 3,844 = 5,869.0000\text{ m}^2$ on Shelf $X$. As you then chain the oblique cosine cross-term $2ab\cos(48^\circ) = 5,580 \times 0.66913 = 3,733.7488\text{ m}^2$ on Shelf $X$, that Pythagorean sum $5,869.0000\text{ m}^2$ waits directly above on Shelf $Y$ (nudging transiently to $Z$ when `2` is entered and dropping back to $Y$ on the first multiplication). Subtracting the acute-angle overlap leaves $c^2 = 2,135.2512\text{ m}^2$ in Register $X$, and `{{key:√x}}` extracts the opposing boundary length $c =$ **`{{res:sc32_04_trig_vectors_polar_seq_11:value}}`** $\text{m}$.

**Coherent Acoustic Wave Superposition ($A_{\text{res}} = \sqrt{A_1^2 + A_2^2 + 2A_1 A_2\cos\Delta\phi}$).** Flipping that minus sign to a plus sign models two coherent sound waves of amplitudes $A_1 = 2.40\text{ Pa}$ and $A_2 = 3.10\text{ Pa}$ arriving at a studio microphone with phase difference $\Delta\phi = 55.0^\circ$ (`{{res:sc32_04_trig_vectors_polar_seq_34:keys}}`). While the incoherent power sum $A_1^2 + A_2^2 = 5.76 + 9.61 = 15.3700\text{ Pa}^2$ waits on Shelf $Y$, the constructive interference cross-term $2(2.4)(3.1)\cos(55^\circ) = 8.5348\text{ Pa}^2$ forms on Shelf $X$, and summing before `{{key:√x}}` extracts the superposed pressure amplitude $\sqrt{23.9048} =$ $\mathbf{{{res:sc32_04_trig_vectors_polar_seq_34:value}}\text{ Pa}}$.

### Catenary Sag, Tsunami Wave Dispersion & Relativistic Rapidity on the Stack

When a high-voltage transmission cable spans $L = 200\text{ meters}$, its half-span is $x = 100\text{ m}$; with catenary parameter $a = T_0 / w = 800\text{ meters}$, the midpoint sag $y = 800[\cosh(100/800) - 1]$ unpeels from the dimensionless ratio $x/a = 0.125$ outward. Running `{{res:sc32_04_trig_vectors_polar_seq_01:keys}}` evaluates $\cosh(0.125) = 1.007823$ via `{{key:HYP}} {{key:COS}}`, subtracts unity to isolate the normalized sag factor $0.007823$, and scales by $a = 800\text{ m}$ to give a midpoint sag of **`{{res:sc32_04_trig_vectors_polar_seq_01:value}}`** meters ($6.26\text{ m}$). In physical oceanography, **Airy's wave dispersion equation** $c_{\text{wave}} = \sqrt{(g/k)\tanh(kh)}$ across a $h = 4,000\text{ m}$ ocean basin for a tsunami of wavelength $\lambda = 200,000\text{ m}$ ($k = 2\pi/\lambda \approx 0.000031416\text{ m}^{-1}$, $kh = 0.12566$) applies `{{key:HYP}} {{key:TAN}}` to $0.12566$, scales by $g/k$, and takes `{{key:√x}}` to reveal a trans-oceanic wave speed of $c_{\text{wave}} \approx \mathbf{197.53\text{ m/s}}$, or $711.1\text{ km/h}$.

For **Einstein and Minkowski's relativistic velocity addition**, an interstellar probe cruising at $v_1 = 0.75c$ relative to Earth that fires a scout missile forward at $v_2 = 0.60c$ relative to the ship adds their hyperbolic rapidities on the stack (`{{res:sc32_04_trig_vectors_polar_seq_02:keys}}`). Applying `{{key:HYP}} {{key:ATAN}}` converts $0.75$ into rapidity $\theta_1 = 0.9730$ and $0.60$ into $\theta_2 = 0.6931$ while lifting $\theta_1$ to Register $Y$; summing the two rapidities to $\theta_{\text{total}} = 1.6661$ and mapping back to normalized velocity via `{{key:HYP}} {{key:TAN}}` shows the missile traveling at **`{{res:sc32_04_trig_vectors_polar_seq_02:value}}`** $c$, or $93.10\%$ of light speed.

### 2D Vector Projections, Wind Triangles, Traverses & 3D Space Frames

You can verify the $(Y = \theta, X = r)$ polar input convention at any time by keying a pure north polar vector of radius $r = 10$ at $\theta = 90^\circ$ via `{{res:sc32_04_trig_vectors_polar_seq_57:keys}}`: because `{{key:▸y,x}}` expects **Angle $\theta$ in Register $Y$ and Radius $r$ in Register $X$**, the projection places `0.0000` in Register $X$ ($x = 10\cos 90^\circ$) and `10.0000` in Register $Y$ ($y = 10\sin 90^\circ$).

{{res:sc32_phasor_mag:screenshot|Direct rectangular-to-polar vector conversion on the StackCalc SC-32 places the angle θ = 53.1301° in Register Y and the radial magnitude r = 5.0000 in Register X.}}

In electrical engineering, when an inductive AC motor draws $I_{\text{rms}} = 8.50\text{ A}$ from a $V_{\text{rms}} = 120.0\text{ V}$ line at a lagging phase angle of $\phi = 32.0^\circ$, the **AC power triangle** splits total apparent power $S = V_{\text{rms}}I_{\text{rms}} = 1,020\text{ VA}$ into two simultaneous orthogonal components that occupy Registers $Y$ and $X$ side by side: horizontal **real shaft power** $P = S\cos\phi$ (in Watts) and vertical **reactive magnetic power** $Q = S\sin\phi$ (in $\text{VAR}$). Duplicating $S = 1,020\text{ VA}$ across the stack and scaling by $\cos(32^\circ)$ and $\sin(32^\circ)$ (`{{res:sc32_04_trig_vectors_polar_seq_19:keys}}`) places $P = \mathbf{865.01\text{ W}}$ in Register $Y$ and $Q =$ **`{{res:sc32_04_trig_vectors_polar_seq_19:value}}`** $\text{VAR}$ in Register $X$ (or in a single coordinate projection, `32 {{key:ENTER}} 1020 {{key:▸y,x}} {{key:x⇄y}}` resolves both legs onto $(Y, X)$ simultaneously):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `120 {{key:ENTER}} 8.5 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1020.0000$ | Total apparent electrical power $S = V_{\text{rms}} I_{\text{rms}}$ (VA) |
| `{{key:ENTER}} {{key:ENTER}} 32 {{key:COS}} {{key:×}}` | $0.0000$ | $0.0000$ | $1020.0000$ | $865.0091$ | Multiply by power factor $\cos(32^\circ)$ for real power $P$ (W) |
| `{{key:x⇄y}} 32 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $865.0091$ | **$540.5176$** | Multiply by reactive factor $\sin(32^\circ)$ for reactive power $Q$ (VAR) |

To solve an **aircraft wind triangle** for a pilot flying at true airspeed $V_{\text{air}} = 220.0\text{ knots}$ on heading $\theta_1 = 45.0^\circ$ while a $35.0\text{-knot}$ crosswind blows toward $\theta_2 = 130.0^\circ$, we project the airspeed vector $(Y = 45^\circ, X = 220\text{ kts})$ via `{{res:sc32_04_trig_vectors_polar_seq_03:keys}}` into **`{{res:sc32_04_trig_vectors_polar_seq_03:value}}`** ($V_{\text{air}, y} = 155.5635\text{ kts}, V_{\text{air}, x} = 155.5635\text{ kts}$) and store those orthogonal components in Variables `A` and `B`. Projecting the crosswind vector via `{{res:sc32_04_trig_vectors_polar_seq_04:keys}}` places $V_{\text{wind}, y} = 26.8116\text{ kts}$ in Register $Y$ and $V_{\text{wind}, x} = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_04:value}}}\text{ kts}$ in Register $X$; recalling `A` and `B` to sum the horizontal and vertical components ($V_{\text{ground}, x} = 133.0659\text{ kts},\; V_{\text{ground}, y} = 182.3750\text{ kts}$) and recombining with `{{key:▸θ,r}}` reveals a **Ground Speed of $V_{\text{ground}} = 225.76\text{ knots}$** in Register $X$ along a **Ground Track of $\theta_{\text{track}} = 53.89^\circ$** in Register $Y$.

When walking a four-station **closed-loop survey traverse** around a rectangular parcel after clearing statistical memory (`{{key:CLΣ}}`), chaining `{{key:▸y,x}} {{key:Σ+}}` accumulates every course's Northing ($\Delta y$) and Easting ($\Delta x$) into the statistical registers:
* **Leg 1 ($\theta = 60^\circ, r = 100\text{ m}$):** Keying `{{res:sc32_04_trig_vectors_polar_seq_05:keys}}` projects $(\Delta y = 86.6025\text{ m}, \Delta x = 50.0000\text{ m})$ into statistical memory ($n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_05:value}}}$).
* **Leg 2 ($\theta = 150^\circ, r = 80\text{ m}$):** Keying `{{res:sc32_04_trig_vectors_polar_seq_06:keys}}` adds $(\Delta y = 40.0000\text{ m}, \Delta x = -69.2820\text{ m})$ at station $n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_06:value}}}$.
* **Leg 3 ($\theta = 240^\circ, r = 100\text{ m}$):** Keying `{{res:sc32_04_trig_vectors_polar_seq_07:keys}}` adds $(\Delta y = -86.6025\text{ m}, \Delta x = -50.0000\text{ m})$ at station $n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_07:value}}}$.
* **Leg 4 ($\theta = 330^\circ, r = 80\text{ m}$):** Keying `{{res:sc32_04_trig_vectors_polar_seq_08:keys}}` ($\Delta y = -40.0000\text{ m}, \Delta x = 69.2820\text{ m}$) closes the boundary loop at $n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_08:value}}}$, where `{{key:SUMS}}` verifies zero closure error ($\Sigma x = 0.0000\text{ m}, \Sigma y = 0.0000\text{ m}$).

Our closing three traces show how tensor rotations, 3D structural mitre joints, and transoceanic great-circle orthodromes fold multi-term directional cosines into Register $X$ without ever overflowing the 4-level stack.

**Christian Otto Mohr's Circle Strain Transformation ($\epsilon_{x'} = \frac{\epsilon_x + \epsilon_y}{2} + \frac{\epsilon_x - \epsilon_y}{2}\cos(2\theta) + \frac{\gamma_{xy}}{2}\sin(2\theta)$).** When an aircraft wing strain-gauge rosette measures planar strains $\epsilon_x = 450\,\mu\epsilon$, $\epsilon_y = 120\,\mu\epsilon$, and engineering shear strain $\gamma_{xy} = 280\,\mu\epsilon$, rotating the reference axes through $\theta = 30.0^\circ$ sweeps the state point through the **double angle $2\theta = 60.0^\circ$** around Mohr's circle. During `{{res:sc32_04_trig_vectors_polar_seq_33:keys}}`, each physical term accumulates sequentially inside Register $X$: averaging $\epsilon_x$ and $\epsilon_y$ first establishes the **hydrostatic mean strain** $\epsilon_{\text{avg}} = 285.0000\,\mu\epsilon$ (the center of Mohr's circle); adding the deviatoric normal projection $\frac{450 - 120}{2}\cos(60^\circ) = 165 \times 0.5 = 82.5000\,\mu\epsilon$ brings the running total to $367.5000\,\mu\epsilon$; and adding the tensorial shear projection $\frac{280}{2}\sin(60^\circ) = 121.2436\,\mu\epsilon$ delivers the rotated normal strain $\epsilon_{x'} \approx \mathbf{488.74\,\mu\epsilon}$ ($488.7436\,\mu\epsilon$). *(To find the maximum principal strain $\epsilon_1 = \epsilon_{\text{avg}} + R_{\text{Mohr}}$ across all angles, feeding the shear half-strain and normal half-difference $165\,\mu\epsilon$—or a high-shear $430\,\mu\epsilon$—into `{{key:▸θ,r}}` extracts the Mohr radius $R_{\text{Mohr}}$, such as $\sqrt{165^2 + 430^2} = 460.98\,\mu\epsilon$ added to $285\,\mu\epsilon$, in a single vector stroke!)*

**3D Space-Frame Cauchy-Schwarz Dot-Product Bevel Angle ($\cos\theta = \frac{\vec{A}\cdot\vec{B}}{\lvert\vec{A}\rvert\lvert\vec{B}\rvert}$).** When a structural machinist mitre-cuts two skew **3D space-frame struts** meeting at a welded node—$\vec{A} = (4.0, 6.0, 8.0\text{ m})$ of squared length $|\vec{A}|^2 = 116\text{ m}^2$ and $\vec{B} = (2.0, -3.0, 5.0\text{ m})$ of squared length $|\vec{B}|^2 = 38\text{ m}^2$, with dot product $\vec{A}\cdot\vec{B} = 4(2) + 6(-3) + 8(5) = 30.0\text{ m}^2$—normalizing the dot product by both vector lengths recovers the enclosed 3D angle $\theta$. In `{{res:sc32_04_trig_vectors_polar_seq_20:keys}}`, the unary `{{key:√x}}` key extracts each vector magnitude in place on Register $X$ right before dividing: dividing $30.0\text{ m}^2$ first by $|\vec{A}| = \sqrt{116} \approx 10.7703\text{ m}$ yields the scalar projection of $\vec{B}$ along $\hat{A}$ ($2.7854\text{ m}$), dividing next by $|\vec{B}| = \sqrt{38} \approx 6.1644\text{ m}$ isolates the dimensionless **directional cosine** $\cos\theta = 0.4519$, and `{{key:ACOS}}` extracts the true 3D bevel angle $\theta = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_20:value}}^\circ}$ (just as $\cos\theta = 0.2588$ on a steeper roof truss yields a $75.0^\circ$ mitre cut) without ever touching Registers $Z$ or $T$.

**Spherical Law of Cosines Across the Pacific.** Finally, to navigate the Great-Circle orthodrome across the Pacific Ocean between **San Francisco (SFO)** at $\phi_1 = 37.6189^\circ\text{ N}, \lambda_1 = -122.3750^\circ\text{ W}$ and **Tokyo Narita (NRT)** at $\phi_2 = 35.7720^\circ\text{ N}, \lambda_2 = 140.3929^\circ\text{ E}$ (westward longitudinal span $\Delta\lambda = 360^\circ - (140.3929^\circ + 122.3750^\circ) = 97.2321^\circ$), we sum the polar and equatorial 3D unit-sphere projections across Registers $Y$ and $X$. First form the vertical polar sine product $\sin\phi_1\sin\phi_2 = 0.356820$ in Register $X$ (`{{res:sc32_04_trig_vectors_polar_seq_54:keys}}`), and then assemble the equatorial cosine projection $\cos\phi_1\cos\phi_2\cos\Delta\lambda = -0.080904$ on Shelf $X$ while $0.356820$ waits above (`{{res:sc32_04_trig_vectors_polar_seq_55:keys}}`). Adding the two projections into $\cos d = 0.275916$ and pressing `{{key:ACOS}}` extracts the central geocentric arc $d = 73.9833^\circ$ in place, which converts to radians ($\times \pi/180$) and scales by Earth's mean radius $R_E = 6,371\text{ km}$ to yield the transpacific great-circle flight distance of **$\mathbf{8,226.6\text{ km}}$**.

**Heliostat Solar Concentrator Tracking.** By the identical two-branch spherical projection, aiming a **heliostat solar concentrator** at latitude $\phi = 32.0^\circ\text{ N}$, solar declination $\delta = 18.5^\circ$, and hour angle $\omega = 45.0^\circ$ evaluates $\sin\phi\sin\delta + \cos\phi\cos\delta\cos\omega = 0.7368$ and applies `{{key:ASIN}}` (`{{res:sc32_04_trig_vectors_polar_seq_41:keys}}`) to lock onto a solar horizon elevation of $\alpha \approx \mathbf{47.46^\circ}$ ($47.4611^\circ$).

---

### When Growth Meets Rotation: The Mystery of √−1

Compare the unit hyperbola of a hanging catenary chain with the unit circle of a rotating wheel:

$$\cosh^2 u - \sinh^2 u = 1 \qquad \text{versus} \qquad \cos^2\theta + \sin^2\theta = 1$$

Those two fundamental curves of nature—one built from real exponentials $\frac{1}{2}(e^u \pm e^{-u})$ that grow without bound, the other tracing periodic sines and cosines around a closed circle—differ by nothing more than a single minus sign!

What algebraic operation could flip that minus sign into a plus sign, bending one-dimensional exponential growth $e^x$ into two-dimensional circular rotation $(\cos\theta, \sin\theta)$? To square a quantity and reverse its sign, we need a number whose square is $-1$.

In sixteenth-century Bologna, Rafael Bombelli confronted that exact riddle while rescuing Gerolamo Cardano's cubic formula from roots of negative numbers. In **[Chapter 5: The Imaginary Number That Keeps the Lights On](05-complex-numbers-phasors.md)**, we will see why multiplying by $i = \sqrt{-1}$ is a physical $90^\circ$ rotation, how Leonhard Euler united growth and rotation in $e^{i\pi} + 1 = 0$, and how Charles Proteus Steinmetz used complex phasors on the $(Y, X)$ stack to electrify the modern world.
