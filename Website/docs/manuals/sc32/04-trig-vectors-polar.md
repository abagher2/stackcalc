---
title: "Chapter 4: Circular Trigonometry, Vector Projections & Hyperbolic Functions | Thinking in the Stack (SC-32)"
description: "Direct and inverse trigonometry, hyperbolic functions, exact axial angle clamping, polar-to-rectangular 2D vector conversions, and geodetic traverses on the StackCalc SC-32."
---

# Chapter 4: Circular Trigonometry, Vector Projections & Hyperbolic Functions

## Eratosthenes' Shadow, Angular Measure, and the Unit Circle

At local solar noon on the summer solstice of 240 BCE, Eratosthenes of Cyrene, chief librarian of the Great Library of Alexandria, measured the shadow of an upright bronze rod called a *gnomon* in a sunlit courtyard. As preserved in Cleomedes' astronomical treatise *The Heavens* {{cite:cleomedes2004}}, travelers had brought Eratosthenes an observation from the frontier garrison town of Syene (modern Aswan), some five thousand stadia up the Nile to the south: at midday on the summer solstice, vertical stone columns in Syene cast no shadow, and the reflection of the overhead sun shone directly onto the water at the bottom of a deep well.

At that same hour in Alexandria, Eratosthenes observed that his vertical bronze gnomon cast a distinct wedge of shadow across the courtyard paving stones. Measuring the ratio of the shadow's horizontal length to the rod's vertical height, he determined that the sun's rays met the upright rod at an angle equal to one-fiftieth of a full circle:

$$\theta = \frac{360^\circ}{50} = 7.2^\circ$$

A sun standing at the zenith in Syene while inclined $7.2^\circ$ south of the zenith in Alexandria could not be reconciled with both a flat Earth and a distant sun. Because the sun is sufficiently distant that its rays arrive across the Earth as parallel lines, only the curvature of the Earth could tilt Alexandria's vertical rod relative to Syene's vertical well. By Euclid's theorem on alternate interior angles of parallel lines cut by a transversal, the $7.2^\circ$ shadow angle at the tip of the gnomon in Alexandria equaled the central angle subtended at the center of the Earth between Syene and Alexandria. Multiplying the five-thousand-stadia overland distance between the two cities by fifty ($50 \times 5,000 = 250,000\text{ stadia}$, or roughly $40,000\text{ kilometers}$), Eratosthenes determined the circumference of the Earth to within a few percent of modern satellite geodesy from a vertical rod, its shadow, and circular geometry.

Two centuries after Eratosthenes, the astronomer Hipparchus of Nicaea addressed the general problem of translating any central angle on the celestial sphere into a straight-line distance. He inscribed triangles inside a circle of fixed radius and compiled the first table of *chords*, the direct precursor of the modern sine and cosine functions. Five hundred years later in India, astronomers led by Aryabhata halved Hipparchus's chord, observing that the half-chord of a double angle forms the vertical leg of a right triangle inscribed inside a circle of radius $r = 1$. They termed that half-chord *jya-ardha* ("half-bowstring"), which Arabic translators rendered as *jiba*, twelfth-century Latin translators in Toledo rendered as *sinus* ("bay" or "fold"), and modern mathematics shortened to *sine*.

When a circle of radius $r = 1$ is centered at the origin of an $(x, y)$ coordinate plane—the *Unit Circle*—and a radial vector is rotated counterclockwise from the positive horizontal axis through an angle $\theta$, the tip of that vector defines a right triangle of hypotenuse $1$:

$$x = \cos\theta \quad (\text{Horizontal Projection}), \qquad y = \sin\theta \quad (\text{Vertical Projection})$$

$$x^2 + y^2 = \cos^2\theta + \sin^2\theta = 1$$

During the Middle Ages and the Renaissance, Islamic and European astronomers from al-Biruni to Regiomontanus and Johannes Kepler engraved this unit-circle geometry onto brass astrolabes equipped with a sighting arm (*alidade*) and an orthogonal shadow grid. Rather than computing series approximations by hand, a navigator could rotate the radius arm to an angle $\theta$ and read its horizontal and vertical projections off the engraved scales:

{{blocks:sc32_concept_unit_circle_polar|The Unit Circle (r = 1) right-triangle projections (cos θ, sin θ, tan θ) and the SC-32 (Y, X) stack vector plane.}}

Rotating the unit radius arm ($r = 1$) counterclockwise from $0^\circ$ to $30^\circ$ ($\pi/6\text{ rad}$) frames the right-triangle projections on the horizontal and vertical axes:

$$\cos(30^\circ) = \frac{\sqrt{3}}{2} \approx 0.866025, \qquad \sin(30^\circ) = \frac{1}{2} = 0.500000$$

Continuing the rotation through $45^\circ$, where $\cos 45^\circ = \sin 45^\circ = \sqrt{2}/2 \approx 0.707107$, and $60^\circ$, where $\cos 60^\circ = 1/2$ and $\sin 60^\circ = \sqrt{3}/2$, brings the radius vector to the vertical axis at $90^\circ$. There the horizontal projection vanishes to $\cos 90^\circ = 0$ while the vertical projection reaches $\sin 90^\circ = 1$. The third circular ratio, the *tangent* $\tan\theta = \sin\theta / \cos\theta$, takes its name from the Latin *tangens* ("touching"): it measures the vertical intercept cut off by the extended radius line along the vertical tangent line $x = 1$ at the right-hand boundary of the unit circle.

### Degrees, Radians, and Gradians

Before evaluating a trigonometric function, the angular unit that subdivides a full revolution around the unit circle must be selected. The StackCalc SC-32 supports all three standard angular conventions, indicated continuously on the top status bar:

| Angular Mode | LCD Annunciator | Full Circle Revolution | Right Angle | Primary Engineering Field |
| :--- | :---: | :---: | :---: | :--- |
| **Degrees** | `DEG` (Default) | $360^\circ$ | $90^\circ$ | Structural Civil Engineering, Geodesy, Avionics |
| **Radians** | `RAD` | $2\pi \approx 6.283185\text{ rad}$ | $\pi/2 \approx 1.570796\text{ rad}$ | Mathematical Physics, Calculus, Wave Mechanics |
| **Gradians** | `GRAD` | $400\text{ grad}$ | $100\text{ grad}$ | European Surveying, Mining Engineering |

All three conventions remain in engineering use because each arose from a distinct structural symmetry. Four thousand years ago, Babylonian astronomers observed that the sun advances against the background zodiac by roughly one degree per day over a $360$-day schematic year. In sexagesimal (base-$60$) arithmetic, $360$ is a highly composite integer divisible without remainder by $2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120,$ and $180$, so degrees (`DEG`) allow a machinist, surveyor, or navigator to subdivide a circle into halves, thirds, quarters, fifths, sixths, eighths, or twelfths using exact integers.

In mathematical analysis, dividing a circle into $360$ parts is an external convention. Roger Cotes and Leonhard Euler defined radian measure (`RAD`) intrinsically from the circle itself by taking the unit angle $\theta$ as the central angle subtending an arc whose length $s$ equals the radius $r$. Defining an angle as the dimensionless ratio of arc length to radius ($\theta = s / r$) makes one full revolution equal to $2\pi\text{ radians}$ ($\approx 6.283185\text{ rad}$) and one radian equal to $180^\circ / \pi \approx 57.29578^\circ$. Only in radians does the small-angle limit $\lim_{\theta \to 0} (\sin\theta)/\theta$ equal $1$, so that $\frac{d}{d\theta}\sin\theta = \cos\theta$ without introducing a factor of $\pi/180$ into differential equations of harmonic oscillation or wave propagation.

During the French Revolution, the geodesists who established the metric system introduced gradians (`GRAD`) to decimalize angular measure alongside length and mass. By defining a right angle as $100\text{ gradians}$ (*gons*) and a full circle as $400\text{ gradians}$, they tied terrestrial coordinates directly to the meter: because the meter was defined as one ten-millionth of the meridian quadrant from the Equator to the North Pole ($10,000\text{ km}$ per $100\text{ grad}$), one gradian of latitude corresponds to $100\text{ kilometers}$ along a meridian and one centigrad ($0.01\text{ grad}$) corresponds to $1\text{ meter}$.

{{blocks:sc32_rpn_calculation|StackCalc SC-32 Live 4-Level XYZT Stack Hardware Display.}}

The active angular mode determines how the SC-32 interprets circular inputs (`SIN`, `COS`, `TAN`) and what angular units it returns from inverse functions (`ASIN`, `ACOS`, `ATAN`) and rectangular-to-polar conversions (`{{key:▸θ,r}}`). Opening `{{key:MODES}}` (`{{key:↰}}` + `{{key:+/-}}`) switches among `{{key:DEG}}`, `{{key:RAD}}`, and `{{key:GRAD}}` at any time. When a nautical chart or surveyor's plat specifies an angle in sexagesimal degrees-minutes-seconds `D.MMSS`—such as $35^\circ 15' 36''$, keyed as `35.1536`—pressing `{{key:▸HR}}` (shifted above the `5` key) converts Register $X$ in place into decimal degrees (`35.2600°`), while `{{key:▸HMS}}` converts decimal degrees or hours back into `D.MMSS` format. Alongside them above the `6` key, `{{key:▸DEG}}` and `{{key:▸RAD}}` convert Register $X$ between degrees and radians directly without changing the active angular mode.

| Function | Dedicated Keystroke | Arity | Valid Domain | Output Range (in `{{key:DEG}}`) |
| :--- | :--- | :---: | :---: | :---: |
| **Sine** | `{{key:SIN}}` | Unary | $(-\infty, +\infty)$ | $[-1.0, +1.0]$ |
| **Cosine** | `{{key:COS}}` | Unary | $(-\infty, +\infty)$ | $[-1.0, +1.0]$ |
| **Tangent** | `{{key:TAN}}` | Unary | $\theta \ne 90^\circ + k \cdot 180^\circ$ | $(-\infty, +\infty)$ |
| **Arcsine** | `{{key:ASIN}}` | Unary | $[-1.0, +1.0]$ | $[-90^\circ, +90^\circ]$ |
| **Arccosine** | `{{key:ACOS}}` | Unary | $[-1.0, +1.0]$ | $[0^\circ, 180^\circ]$ |
| **Arctangent** | `{{key:ATAN}}` | Unary | $(-\infty, +\infty)$ | $(-90^\circ, +90^\circ)$ |

### Exact Axial Angle Clamping at $90^\circ, 180^\circ,$ and $270^\circ$

Evaluating $\cos(90^\circ)$ in a generic floating-point environment frequently returns a non-zero residual such as $6.123233995736766 \times 10^{-17}$ rather than exact zero. Inside a conventional math library, an angle in degrees is first converted to radians by multiplying by $\pi / 180$, so $90^\circ$ becomes a floating-point approximation to $\pi / 2$. Because $\pi$ is transcendental, its binary expansion does not terminate; an IEEE-754 double-precision register truncates $\pi/2$ after 53 significand bits, producing a value that differs from mathematical $\pi/2$ by approximately $6.123234 \times 10^{-17}\text{ radians}$.

Near $\theta = \pi/2$, the derivative of $\cos\theta$ is $-\sin(\pi/2) = -1$, so evaluating the cosine polynomial on that truncated binary approximation returns the residual $6.123234 \times 10^{-17}$ instead of zero. In a structural stiffness matrix or coordinate transformation, a spurious non-zero entry of $6.12 \times 10^{-17}$ can propagate into subsequent divisions or prevent zero-threshold tests from matching.

To prevent binary radian conversion from perturbing orthogonal geometry, the SC-32 performs *exact axial angle clamping* prior to polynomial evaluation: in Degrees (`DEG`) or Gradians (`GRAD`) mode, integer multiples of a right angle are reduced modulo a full circle so that $\sin(0^\circ) = 0.0$, $\cos(0^\circ) = 1.0$, $\sin(90^\circ) = 1.0$, $\cos(90^\circ) = 0.0$, $\sin(180^\circ) = 0.0$, $\cos(180^\circ) = -1.0$, $\sin(270^\circ) = -1.0$, and $\cos(270^\circ) = 0.0$ return exact IEEE-754 zero and unity values. Likewise, evaluating $\tan(90^\circ)$ or $\tan(270^\circ)$ traps the vertical asymptote with `INVALID DATA` (Code 02) rather than returning a $1.63 \times 10^{16}$ reciprocal of rounding noise, and passing an argument $|x| > 1$ to `{{key:ASIN}}` or `{{key:ACOS}}` raises `INVALID DATA` (Code 02) while preserving the stack registers unchanged.

---

## Triangles, Crosswinds & Resolving 2D Vectors

Across classical mechanics, civil surveying, geometrical optics, and air navigation, two-dimensional problems reduce to two reciprocal operations on the unit circle: resolving a directed magnitude into orthogonal components via $\cos\theta$ and $\sin\theta$, or reconstructing a resultant magnitude and direction from orthogonal components.

### Projecting Forces, Trajectories & Mountain Summits

In the *Two New Sciences* (1638) {{cite:galilei1638}}, Galileo Galilei demonstrated that the parabolic trajectory of a projectile in a uniform gravitational field (neglecting air resistance) is the superposition of two independent orthogonal motions. Horizontally, no net force acts after launch, so the horizontal velocity component $v_{0x} = v_0\cos\theta$ remains constant downrange. Vertically, gravity $g$ produces a constant downward acceleration that decelerates the initial vertical component $v_{0y} = v_0\sin\theta$ until the projectile reaches its apex altitude $H_{\max}$, where the vertical kinetic energy $\frac{1}{2}mv_{0y}^2$ equals the gravitational potential energy $mgH_{\max}$:

$$H_{\max} = \frac{(v_0 \sin\theta)^2}{2g}, \qquad R = \frac{2 v_{0x} v_{0y}}{g} = \frac{v_0^2 \sin(2\theta)}{g}$$

By the double-angle identity $2\sin\theta\cos\theta = \sin(2\theta)$, maximum horizontal range over level ground occurs when $\sin(2\theta) = 1$ ($\theta = 45^\circ$), and any two complementary launch angles summing to $90^\circ$, such as $30^\circ$ and $60^\circ$, produce the same downrange distance $R$.

The same orthogonal resolution governs a mass $m$ sliding down a plane inclined at angle $\theta$ with kinetic friction coefficient $\mu_k$. Gravity acts vertically downward with magnitude $mg$, while the surface constrains motion along the incline. Resolving the gravitational vector into components parallel and normal to the surface shows that $mg\sin\theta$ acts down the slope while $mg\cos\theta$ acts perpendicular to the surface, producing a normal reaction $N = mg\cos\theta$ and an opposing Coulomb friction force $\mu_k N = \mu_k mg\cos\theta$:

$$a = g (\sin\theta - \mu_k \cos\theta)$$

Because the mass $m$ cancels out of both terms, bodies of any mass sharing the same coefficient $\mu_k$ accelerate down the incline at the same rate, and at the critical *angle of repose* where $\sin\theta = \mu_k\cos\theta$ ($\tan\theta = \mu_k$), the downslope gravitational component and upslope friction balance to zero.

When an inaccessible summit cannot be plumbed directly, trigonometry determines its elevation from a surveyed horizontal baseline. During the Great Trigonometrical Survey of India in the 1850s, surveyors determined the altitude of Peak XV (Mount Everest) through *two-station optical leveling*: sighting the vertical elevation angle $\alpha$ to the summit from Station 1, advancing a measured horizontal baseline distance $d$ toward the peak to Station 2, and sighting the steeper elevation angle $\beta$. Because the horizontal distances from the summit's plumb line to the two stations are $x_1 = H\cot\alpha$ and $x_2 = H\cot\beta$, their difference $x_1 - x_2 = d$ eliminates the unmeasured horizontal distance to the mountain's interior plumb line:

$$d = H(\cot\alpha - \cot\beta) \implies H = \frac{d}{\cot\alpha - \cot\beta} = \frac{d}{\frac{1}{\tan\alpha} - \frac{1}{\tan\beta}}$$

Because the cotangent $\cot\theta = 1/\tan\theta$ is the reciprocal of the tangent, dedicated keys for $\sec\theta$, $\csc\theta$, and $\cot\theta$ are unnecessary when `{{key:1/x}}` sits on the primary keypad: inverting each tangent in place via `{{key:TAN}} {{key:1/x}}` converts elevation angles directly into horizontal-to-vertical ratios.

When the horizontal baseline $D$ to the base of a vertical target can be taped directly—as in *forestry timber cruising* with a handheld Suunto clinometer—sighting the inclination angle $\theta_{\text{top}}$ to the tree's crown leader and the depression angle $\theta_{\text{base}}$ to its root collar gives the total tree height $H = D(\tan\theta_{\text{top}} - \tan\theta_{\text{base}})$ (or merchantable bole height when sighted to the upper utilization limit). Conversely, in a *precision toolroom machine shop*, setting up a surface grinder with a hardened steel *sine bar* of center-to-center roller spacing $L$ ($5.0000\text{ in}$ or $10.0000\text{ in}$) uses the vertical sine projection $h = L\sin\theta$ to determine the exact stack of gauge blocks wrung together beneath the raised roller to grind a specified taper angle $\theta$.

Circular projection also governs the period of a simple pendulum: at finite angular amplitude $\theta_0$, the exact gravitational restoring torque $\sin\theta$ is smaller than the linearized approximation $\theta$, lengthening the small-angle period $T_0 = 2\pi\sqrt{L/g}$ according to the leading half-angle sine term $T \approx T_0[1 + \frac{1}{4}\sin^2(\theta_0/2)]$ ($+3.66\%$ at $\theta_0 = 45^\circ$). Christiaan Huygens's 1656 horological analysis expresses the exact period through the complete elliptic integral of the first kind $K(\sin(\theta_0/2))$, which Romberg numerical integration (`{{key:∫}}`) evaluates directly across any release angle.

### Reversing the Projection: Snell's Refraction, Brewster's Angle & the Inverse Tangent

Whereas direct trigonometric functions map an angle to a dimensionless ratio of lengths, *inverse trigonometric functions* (`{{key:ASIN}}`, `{{key:ACOS}}`, `{{key:ATAN}}`) invert that mapping, recovering the geometric angle from a measured ratio of velocities, refractive indices, accelerations, or lengths.

In geometrical optics, a light ray crossing the interface between two transparent media of refractive indices $n_1$ and $n_2$ obeys the law of refraction first formulated in 984 CE in Baghdad by Ibn Sahl (*On Burning Mirrors and Lenses*) and independently rediscovered in Europe by Thomas Harriot (1602) and Willebrord Snell (1621): across the boundary, the product of the refractive index and the sine of the ray angle from the normal remains invariant ($n_1\sin\theta_1 = n_2\sin\theta_2$). Pierre de Fermat later derived this invariance from the Principle of Least Time, given phase velocities $v_1 = c/n_1$ and $v_2 = c/n_2$. When light propagates inside a higher-index optical fiber core ($n_1 > n_2$), a ray meeting the cladding boundary refracts away from the normal; at the *critical angle* $\theta_c$, the refracted ray grazes the interface at $\theta_2 = 90^\circ$ ($\sin 90^\circ = 1$), and `{{key:ASIN}}` recovers the confinement threshold:

$$\theta_c = \arcsin\left(\frac{n_2}{n_1}\right)$$

Rays incident at angles exceeding $\theta_c$ undergo lossless *total internal reflection*, confining optical signals along transoceanic glass fibers.

In 1815, Scottish physicist David Brewster determined the incidence angle $\theta_B$ at which light reflected from a dielectric surface becomes completely polarized parallel to the interface. Brewster found that complete polarization occurs when the reflected and refracted rays are mutually perpendicular ($\theta_B + \theta_2 = 90^\circ$). Because $\sin(90^\circ - \theta_B) = \cos\theta_B$, Snell's relation $n_1\sin\theta_B = n_2\sin\theta_2$ becomes $n_1\sin\theta_B = n_2\cos\theta_B$, expressing the refractive-index ratio as a tangent:

$$\tan\theta_B = \frac{\sin\theta_B}{\cos\theta_B} = \frac{n_2}{n_1} \implies \theta_B = \arctan\left(\frac{n_2}{n_1}\right)$$

Comparing these two optical laws illustrates how the three inverse keys partition the unit circle. Because neither the horizontal projection $\cos\theta$ nor the vertical projection $\sin\theta$ on the unit circle can exceed the unit hypotenuse $1$, `{{key:ASIN}}` and `{{key:ACOS}}` are restricted to arguments within $[-1, +1]$, mapping onto principal ranges $[-90^\circ, +90^\circ]$ and $[0^\circ, 180^\circ]$. By contrast, the tangent ratio $\tan\theta = y/x$ spans all real numbers as a line approaches the vertical axis, so `{{key:ATAN}}` maps $(-\infty, +\infty)$ onto $(-90^\circ, +90^\circ)$ whenever two orthogonal components are divided.

### Oblique Triangles and the Law of Cosines

In geodetic surveying and wave interference, triangles are rarely right-angled. When a surveyor occupies a corner station $C$ and measures straight-line distances $a$ and $b$ to two boundary monuments separated by an included angle $C \ne 90^\circ$, dropping an altitude $h$ from the vertex opposite side $a$ decomposes the oblique triangle into two right triangles. In the inner right triangle containing angle $C$, the vertical altitude has length $h = b\sin C$, while the horizontal projection of side $b$ along side $a$ has length $b\cos C$, so the remaining base of the outer right triangle is $(a - b\cos C)$. Applying the Pythagorean theorem to that outer right triangle and simplifying via $\cos^2 C + \sin^2 C = 1$ yields:

$$c^2 = (a - b\cos C)^2 + (b\sin C)^2 = a^2 + b^2(\cos^2 C + \sin^2 C) - 2ab\cos C$$

Extracting the square root gives the *Law of Cosines*:

$$c = \sqrt{a^2 + b^2 - 2 a b \cos C}$$

Structurally, the Law of Cosines augments the Pythagorean sum $a^2 + b^2$ with the angular projection term $-2ab\cos C$, governing all planar triangles across the full range of angle $C$. When $C = 90^\circ$, $\cos 90^\circ = 0$ and the cross-term vanishes, recovering the Pythagorean theorem ($c = \sqrt{a^2 + b^2}$); when $C < 90^\circ$ (an acute angle), $\cos C > 0$ reduces $c$ below the right-triangle hypotenuse; and when $C > 90^\circ$ (an obtuse angle), $\cos C < 0$ renders $-2ab\cos C$ positive and extends the opposite side $c$.

Replacing the interior angle $C$ with the exterior supplement $180^\circ - \Delta\phi$ reverses the sign of the cosine term and yields the law of *coherent wave interference*: when two acoustic or electromagnetic waves of amplitudes $A_1$ and $A_2$ arrive at a detector with phase difference $\Delta\phi$, their superposed amplitude is the vector resultant of two phasors placed tip-to-tail:

$$A_{\text{resultant}} = \sqrt{A_1^2 + A_2^2 + 2 A_1 A_2 \cos(\Delta\phi)}$$

### The $(Y, X)$ Coordinate Plane: Polar $\leftrightarrow$ Rectangular Vector Conversion

In scalar arithmetic, binary operators treat Registers $Y$ and $X$ as two scalar operands that collapse into a single result. In two-dimensional vector geometry, Registers $Y$ and $X$ operate together as a coordinate pair representing a point or vector in the plane.

Navigators, surveyors, and electrical engineers convert continuously between *polar coordinates* $(r, \theta)$ and *rectangular coordinates* $(x, y)$ because field instruments measure in polar form while vector addition requires rectangular components. When a radar antenna tracks a target, a surveyor sights a monument with a theodolite, or an aircraft instrument panel displays airspeed and heading, the measurement consists of a radial magnitude $r$ and a direction angle $\theta$.

Yet as Simon Stevin demonstrated in 1586 through his *Wreath of Spheres* (*Clootcrans*) equilibrium proof establishing the parallelogram law of forces, non-collinear vectors cannot be summed by adding their scalar magnitudes $r_1 + r_2$. To combine an aircraft's airspeed vector with a crosswind, or to verify that a multi-leg property survey closes back onto its starting monument, each polar vector $(r, \theta)$ must first be resolved into its horizontal component ($x = r\cos\theta$) and vertical component ($y = r\sin\theta$), summed along each orthogonal axis ($\Sigma x, \Sigma y$), and converted back into a resultant magnitude $r$ and direction $\theta$.

On the SC-32 display, Register $X$ occupies Line 1 and Register $Y$ sits directly above it on Line 2. Mapping the horizontal component $x$ (and radial magnitude $r$) to Register $X$ and the vertical component $y$ (and angle $\theta$) to Register $Y$ aligns the display registers with standard $(x, y)$ notation.

The shifted legends above `{{key:1}}` indicate the destination registers directly: for Rectangular $\to$ Polar (`{{key:▸θ,r}}`, Left Shift `{{key:↰}}` above `{{key:1}}`), the first symbol after the arrow ($\theta$) is placed in Register $Y$ and the second symbol ($r$) is placed in Register $X$, so keying `y {{key:ENTER}} x {{key:▸θ,r}}` transforms $(Y = y,\; X = x)$ into $(Y = \theta,\; X = r)$. Conversely, for Polar $\to$ Rectangular (`{{key:▸y,x}}`, Right Shift `{{key:↱}}` above `{{key:1}}`), $y$ is placed in Register $Y$ and $x$ is placed in Register $X$, so keying `θ {{key:ENTER}} r {{key:▸y,x}}` transforms $(Y = \theta,\; X = r)$ into $(Y = y,\; X = x)$ without disturbing Registers $Z$ or $T$:

| Transformation | Dedicated Keystroke | Stack Input ($Y, X$) | Stack Output ($Y, X$) | Mathematical Formula |
| :--- | :--- | :--- | :--- | :--- |
| **Polar to Rectangular** | `{{key:▸y,x}}` | $Y = \theta$ (Angle in active mode)<br>$X = r$ (Radius / Magnitude) | $Y = y = r \sin\theta$<br>$X = x = r \cos\theta$ | $(x, y) = (r\cos\theta, r\sin\theta)$ |
| **Rectangular to Polar** | `{{key:▸θ,r}}` | $Y = y$ (Orthogonal vertical)<br>$X = x$ (Orthogonal horizontal) | $Y = \theta = \operatorname{atan2}(y, x)$<br>$X = r = \sqrt{x^2 + y^2}$ | $(r, \theta) = (\sqrt{x^2+y^2}, \operatorname{atan2}(y, x))$ |

Using `{{key:▸θ,r}}` avoids the quadrant ambiguity and axial singularity of dividing $y / x$ and pressing `{{key:ATAN}}`, which receives only the single scalar quotient $y/x$. In Quadrant III, where both $x = -3$ and $y = -4$ are negative, the quotient $(-4)/(-3) = +1.3333$ is positive, so $\arctan(y/x)$ returns $+53.1301^\circ$ in Quadrant I, an error of $180^\circ$; on the positive or negative vertical axis where $x = 0$ and $y = \pm 10$, dividing $y/x$ halts with `DIVIDE BY 0`. By contrast, `{{key:▸θ,r}}` evaluates the four-quadrant $\operatorname{atan2}(y, x)$ function, inspecting the individual signs of $y$ in Register $Y$ and $x$ in Register $X$ across the full $(-180^\circ, +180^\circ]$ circle:

| Quadrant / Axis | Signs of $(x, y)$ | Four-Quadrant $\operatorname{atan2}(y, x)$ Formula (in `DEG`) | Example Vector $(x, y)$ | Output $(Y = \theta, X = r)$ |
| :--- | :---: | :--- | :---: | :--- |
| **Quadrant I** | $x > 0,\; y \ge 0$ | $\arctan(y/x)$ | $(+3, +4)$ | $\theta = +53.1301^\circ,\; r = 5.0$ |
| **Quadrant II** | $x < 0,\; y \ge 0$ | $\arctan(y/x) + 180^\circ$ | $(-3, +4)$ | $\theta = +126.8699^\circ,\; r = 5.0$ |
| **Quadrant III** | $x < 0,\; y < 0$ | $\arctan(y/x) - 180^\circ$ | $(-3, -4)$ | $\theta = -126.8699^\circ,\; r = 5.0$ |
| **Quadrant IV** | $x > 0,\; y < 0$ | $\arctan(y/x)$ | $(+3, -4)$ | $\theta = -53.1301^\circ,\; r = 5.0$ |
| **Vertical Axes** | $x = 0,\; y \ne 0$ | $+90^\circ$ if $y > 0$, $-90^\circ$ if $y < 0$ | $(0, +10)$ | $\theta = +90.0000^\circ,\; r = 10.0$ |

This three-stage sequence—project via `{{key:▸y,x}}`, sum the orthogonal components, and recombine via `{{key:▸θ,r}}`—applies identically across marine, aeronautical, and structural vector mechanics. When a vessel steers across a tidal current or an aircraft flies at true airspeed $\vec{V}_{\text{air}}$ through a crosswind $\vec{V}_{\text{wind}}$, its ground track is the vector sum $\vec{V}_{\text{ground}} = \vec{V}_{\text{air}} + \vec{V}_{\text{wind}}$, just as two tension forces on a laboratory force table require an equilibrant $\vec{F}_3 = -(\vec{F}_1 + \vec{F}_2)$ for static equilibrium.

When a land surveyor or navigator records the distance $r_i$ and *North Azimuth* $\alpha_i$ (measured clockwise from True North, where $0^\circ = \text{North}$ and $90^\circ = \text{East}$) around a closed property boundary, reflecting the coordinate axes across the $45^\circ$ Northeast diagonal swaps sine and cosine so that Northing latitude is $\Delta N_i = r_i\cos\alpha_i$ and Easting departure is $\Delta E_i = r_i\sin\alpha_i$:

$$\Sigma \Delta N = \sum r_i \cos\alpha_i = 0, \qquad \Sigma \Delta E = \sum r_i \sin\alpha_i = 0$$

Because `{{key:▸y,x}}` evaluates $(Y = r\sin\theta,\; X = r\cos\theta)$, entering a Cartesian angle $\theta$ (counterclockwise from East) places $(Y = \Delta y,\; X = \Delta x)$, whereas entering a surveyor's or pilot's North Azimuth $\alpha$ (clockwise from North) automatically places **Easting departure ($\Delta E = r\sin\alpha$) in Register $Y$** and **Northing latitude ($\Delta N = r\cos\alpha$) in Register $X$**—and pressing `{{key:▸θ,r}}` evaluates $\operatorname{atan2}(\Delta E, \Delta N)$ to recover the true North Azimuth directly! Chaining `{{key:▸y,x}} {{key:Σ+}}` after each course accumulates an entire multi-leg boundary traverse inside the statistical registers without occupying named storage variables.

### Spherical Geodesy, Great-Circle Orthodromes & Avian Celestial Navigation

Over intercontinental distances, planar Cartesian trigonometry must be replaced by spherical geometry. On a spherical Earth of mean radius $R_E = 6,371.0\text{ km}$, the shortest path between two points at latitude/longitude coordinates $(\phi_1, \lambda_1)$ and $(\phi_2, \lambda_2)$ is not a constant-bearing rhumb line (*loxodrome*) on a Mercator projection, but a *great-circle orthodrome*: the arc formed on the surface by a plane passing through both points and the center of the Earth.

The *Spherical Law of Cosines* follows from three-dimensional unit-sphere coordinates. On a sphere of unit radius $r = 1$, a point at latitude $\phi$ and longitude $\lambda$ has polar coordinate $z = \sin\phi$ and equatorial radius $\cos\phi$, which projects onto the equatorial $(x, y)$ axes as $x = \cos\phi\cos\lambda$ and $y = \cos\phi\sin\lambda$:

$$\hat{u}_1 = \begin{bmatrix} \cos\phi_1\cos\lambda_1 \\ \cos\phi_1\sin\lambda_1 \\ \sin\phi_1 \end{bmatrix}, \qquad \hat{u}_2 = \begin{bmatrix} \cos\phi_2\cos\lambda_2 \\ \cos\phi_2\sin\lambda_2 \\ \sin\phi_2 \end{bmatrix}$$

Evaluating the inner product $\hat{u}_1 \cdot \hat{u}_2 = \cos d$ between the two unit vectors and applying the cosine difference identity $\cos\lambda_1\cos\lambda_2 + \sin\lambda_1\sin\lambda_2 = \cos(\lambda_2 - \lambda_1)$ expresses the central geocentric angle $d$ as the sum of the axial projection ($\sin\phi_1\sin\phi_2$) and the equatorial projection ($\cos\phi_1\cos\phi_2\cos\Delta\lambda$):

$$\cos d = \sin\phi_1 \sin\phi_2 + \cos\phi_1 \cos\phi_2 \cos(\lambda_2 - \lambda_1), \qquad D = R_E \times d_{\text{rad}}$$

Because meridians converge toward the poles as $\cos\phi$, the great-circle route between San Francisco ($\phi_1 \approx 37.6^\circ\text{ N}$) and Tokyo ($\phi_2 \approx 35.8^\circ\text{ N}$) arcs northward toward the Aleutian Islands near $50^\circ\text{ N}$, where each degree of longitude spans a shorter arc than at $36^\circ\text{ N}$ and shortens the total path by hundreds of kilometers compared to sailing due west along a parallel of latitude.

The same Spherical Law of Cosines solves the *astronomical triangle* connecting the North Celestial Pole, an observer's zenith at latitude $\phi$, and the sun at seasonal declination $\delta$ and hour angle $\omega$ ($15^\circ$ per hour from local solar noon), determining the solar horizon altitude $\alpha$ and azimuth $\gamma_s$:

$$\sin\alpha = \sin\phi \sin\delta + \cos\phi \cos\delta \cos\omega, \qquad \cos\gamma_s = \frac{\sin\alpha \sin\phi - \sin\delta}{\cos\alpha \cos\phi}$$

Migratory birds combine these same geometric relationships during transoceanic flight. Each autumn, the bar-tailed godwit (*Limosa lapponica*) departs Alaska's tidal flats and flies $11,000\text{ kilometers}$ non-stop across the Pacific Ocean to New Zealand over nine days. Because the sun's azimuth shifts at roughly $15^\circ\text{ per hour}$, maintaining a solar heading requires time-compensated azimuth correction: the godwit couples its internal circadian rhythm with solar elevation and geomagnetic inclination cues to follow a great-circle orthodrome while compensating for crosswind drift (`{{key:▸y,x}}` vector addition).

Where satellite navigation requires sub-meter geodetic accuracy, the spherical model is refined to Isaac Newton's *oblate spheroid*. In the *Principia* (1687), Newton demonstrated that Earth's diurnal rotation causes the equatorial radius to exceed the polar radius by $21.385\text{ km}$—a bulge large enough that if a smartphone GPS receiver treated Earth as a perfect sphere, its map pin at mid-latitudes would miss the street by nearly $20\text{ kilometers}$. The World Geodetic System 1984 (WGS84) reference ellipsoid (equatorial semi-major axis $a = 6,378,137.0\text{ m}$, flattening $f = 1/298.257223563$, first eccentricity squared $e^2 = 2f - f^2 \approx 0.00669437999014$) defines the prime-vertical radius of curvature $N(\phi)$ and Earth-Centered Earth-Fixed coordinates $(X, Y, Z)$ at geodetic latitude $\phi$, longitude $\lambda$, and ellipsoidal height $h$:

$$N(\phi) = \frac{a}{\sqrt{1 - e^2 \sin^2\phi}}, \qquad \begin{bmatrix} X \\ Y \\ Z \end{bmatrix} = \begin{bmatrix} (N(\phi) + h) \cos\phi \cos\lambda \\ (N(\phi) + h) \cos\phi \sin\lambda \\ (N(\phi)(1 - e^2) + h) \sin\phi \end{bmatrix}$$

---

## Hanging Chains, Catenary Arches, and Hyperbolic Functions

### The 1691 Bernoulli Contest, Catenary Chains & the Gateway Arch

A flexible cable or chain suspended between two supports assumes a distinct static equilibrium curve under its own gravitational weight. In the *Two New Sciences* (1638), Galileo Galilei conjectured that a hanging chain forms a quadratic parabola ($y = kx^2$). In 1646, seventeen-year-old Christiaan Huygens proved geometrically that the equilibrium curve of a uniform chain cannot be algebraic, so the analytical form of the curve remained an open problem.

In May 1690, Jakob Bernoulli published a challenge in the *Acta Eruditorum* calling for the exact equation of the hanging chain. Within a year, Christiaan Huygens, Gottfried Wilhelm Leibniz, and Johann Bernoulli solved the problem independently. They showed that a parabola arises only when weight is distributed uniformly per unit of *horizontal span* $dx$, as in a suspension bridge whose level roadway deck hangs from vertical suspenders spaced uniformly along the horizontal axis. In an unburdened flexible chain or overhead transmission line, weight is distributed uniformly per unit of *curved arc length* $ds = \sqrt{1 + (dy/dx)^2}\,dx$ along the conductor itself; near the towers where the inclination is steep, each unit of horizontal span carries a greater length and weight of cable than near the vertex.

Huygens, Leibniz, and Johann Bernoulli formulated the static equilibrium of a chain segment of arc length $s$ measured from the lowest vertex (where the chain is horizontal under tension $T_0$) to a point $(x, y)$ where the tangent makes angle $\psi$ with the horizontal. Because no external horizontal forces act on the segment, the horizontal component of tension $T\cos\psi$ must equal the vertex tension $T_0$ everywhere along the span ($T\cos\psi = T_0$). Vertically, the upward tension component $T\sin\psi$ must balance the gravitational weight $w \cdot s$ of the arc length $s$ suspended below $(x, y)$, where $w$ is the linear weight density in Newtons per meter ($T\sin\psi = w \cdot s$). Dividing the vertical balance by the horizontal balance eliminates the variable tension $T$ and relates the local slope $\frac{dy}{dx} = \tan\psi$ to the arc length $s$:

$$\frac{dy}{dx} = \tan\psi = \frac{w \cdot s}{T_0} = \frac{s}{a}, \qquad \text{where } a = \frac{T_0}{w}$$

Differentiating with respect to $x$ yields the differential equation $\frac{d^2 y}{dx^2} = \frac{1}{a}\frac{ds}{dx} = \frac{1}{a}\sqrt{1 + (dy/dx)^2}$, whose solution is the symmetric combination of rising and decaying exponentials $e^{x/a}$ and $e^{-x/a}$. Huygens termed the curve the *catenary* (from the Latin *catena*, "chain"), corresponding to the *hyperbolic cosine*:

$$\cosh(u) = \frac{e^u + e^{-u}}{2}, \qquad \sinh(u) = \frac{e^u - e^{-u}}{2}, \qquad \tanh(u) = \frac{\sinh(u)}{\cosh(u)} = \frac{e^u - e^{-u}}{e^u + e^{-u}}$$

With the origin placed at the lowest vertex of the span, the vertical sag $y(x)$ follows the hyperbolic cosine while the arc length $s(x)$ measured from the vertex to $x$ follows the hyperbolic sine:

$$y(x) = a\left(\cosh\left(\frac{x}{a}\right) - 1\right), \qquad s(x) = a\sinh\left(\frac{x}{a}\right)$$

These exponential combinations are termed *hyperbolic* functions and share keys with $\sin$, $\cos$, and $\tan$ because whereas the circular functions $(\cos u, \sin u)$ parameterize the unit circle $x^2 + y^2 = 1$ (sweeping out a circular sector of area $u/2$), squaring and subtracting $\cosh u$ and $\sinh u$ shows that $(\cosh u, \sinh u)$ parameterize the right branch of the unit hyperbola $x^2 - y^2 = 1$ (sweeping out a hyperbolic sector of area $u/2$):

$$\cosh^2(u) - \sinh^2(u) = \left(\frac{e^u + e^{-u}}{2}\right)^2 - \left(\frac{e^u - e^{-u}}{2}\right)^2 = \frac{e^{2u} + 2 + e^{-2u} - (e^{2u} - 2 + e^{-2u})}{4} = 1$$

Their derivatives parallel the circular functions without sign reversal on $\frac{d}{du}\cosh u$:

$$\frac{d}{du}\sinh(u) = \cosh(u), \qquad \frac{d}{du}\cosh(u) = +\sinh(u), \qquad \frac{d}{du}\tanh(u) = \operatorname{sech}^2(u) = 1 - \tanh^2(u)$$

Inverting a hanging catenary curve exchanges pure axial tension for pure axial compression without bending moment. As Robert Hooke stated to the Royal Society in 1675, *"As hangs the flexible chain, so but inverted will stand the rigid arch,"* the structural principle applied by architect Eero Saarinen and engineer Hannskarl Bandel in the $192\text{-meter}$ stainless-steel catenary profile of the Gateway Arch in St. Louis.

### Ocean Tsunami Dispersion, Relativistic Rapidity & The HYP Prefix

On the SC-32 keypad, the hyperbolic prefix `{{key:HYP}}` is located on Left Shift `{{key:↰}}` above `{{key:R↓}}`. Pressing `{{key:HYP}}` activates the transient `HYP` annunciator and pairs with the primary keys `{{key:SIN}}`, `{{key:COS}}`, and `{{key:TAN}}` for $\sinh(x)$, $\cosh(x)$, and $\tanh(x)$, or with their Left-Shifted counterparts `{{key:ASIN}}`, `{{key:ACOS}}`, and `{{key:ATAN}}` for the inverse hyperbolic functions (because hyperbolic arguments are dimensionless real numbers, `{{key:HYP}}` operations are independent of `DEG`/`RAD`/`GRAD` angular modes):

| Function | Key Sequence | Mathematical Definition | Valid Domain |
| :--- | :--- | :--- | :---: |
| **Hyperbolic Sine** | `{{key:HYP}} {{key:SIN}}` | $\sinh(x) = \frac{e^x - e^{-x}}{2}$ | $(-\infty, +\infty)$ |
| **Hyperbolic Cosine** | `{{key:HYP}} {{key:COS}}` | $\cosh(x) = \frac{e^x + e^{-x}}{2}$ | $(-\infty, +\infty)$ |
| **Hyperbolic Tangent** | `{{key:HYP}} {{key:TAN}}` | $\tanh(x) = \frac{\sinh(x)}{\cosh(x)}$ | $(-\infty, +\infty)$ |
| **Inverse Sinh** | `{{key:HYP}} {{key:ASIN}}` | $\operatorname{arsinh}(x) = \ln\left(x + \sqrt{x^2 + 1}\right)$ | $(-\infty, +\infty)$ |
| **Inverse Cosh** | `{{key:HYP}} {{key:ACOS}}` | $\operatorname{arcosh}(x) = \ln\left(x + \sqrt{x^2 - 1}\right)$ | $x \ge 1.0$ |
| **Inverse Tanh** | `{{key:HYP}} {{key:ATAN}}` | $\operatorname{artanh}(x) = \frac{1}{2}\ln\left(\frac{1+x}{1-x}\right)$ | $\lvert x\rvert < 1.0$ |

Beyond catenary cables and masonry arches, the hyperbolic tangent $\tanh(u)$ governs physical systems that transition smoothly between linear and saturated asymptotic regimes. When surface gravity waves of wavelength $\lambda$ (wavenumber $k = 2\pi/\lambda$) propagate across an ocean of depth $h$, George Biddell Airy derived from potential-flow boundary conditions at the seabed and free surface that their phase velocity $c_{\text{wave}}$ depends on the hyperbolic tangent of the dimensionless depth-to-wavelength product $kh$:

$$c_{\text{wave}} = \sqrt{\frac{g}{k}\tanh(kh)}$$

In deep water ($kh \gg 1$), $\tanh(kh) \to 1$, so long-wavelength swell travels faster than short-wavelength chop ($c_{\text{wave}} \approx \sqrt{g/k}$). In shallow water—or during a transoceanic tsunami whose wavelength far exceeds the ocean depth ($kh \ll 1$)—$\tanh(kh) \approx kh$, the wavenumber $k$ cancels out of the radical, and the wave propagates across the basin near the non-dispersive shallow-water speed $c_{\text{wave}} \approx \sqrt{gh}$.

The hyperbolic tangent also linearizes relativistic velocity addition. In Galilean kinematics, collinear velocities add linearly ($v_1 + v_2$), which would permit successive boosts to exceed the speed of light $c$. In 1905, Albert Einstein showed that Lorentz transformations combine normalized collinear velocities $\beta_i = v_i/c$ according to $\beta_{\text{total}} = (\beta_1 + \beta_2)/(1 + \beta_1\beta_2)$. Three years later, Hermann Minkowski identified that relation as the hyperbolic tangent addition identity $\tanh(\theta_1 + \theta_2) = (\tanh\theta_1 + \tanh\theta_2)/(1 + \tanh\theta_1\tanh\theta_2)$. Mapping each normalized velocity $\beta = v/c$ to its hyperbolic angle (*rapidity*) $\theta = \operatorname{artanh}(v/c)$ restores additive composition in Minkowski spacetime:

$$\theta_{\text{total}} = \theta_1 + \theta_2 \implies \frac{v_{\text{total}}}{c} = \tanh\left(\operatorname{artanh}\left(\frac{v_1}{c}\right) + \operatorname{artanh}\left(\frac{v_2}{c}\right)\right)$$

Because $\tanh(\theta)$ approaches $1.0$ asymptotically as $\theta \to \infty$, arbitrarily many finite rapidity boosts sum without ever exceeding $c$.

---

## Circular, Vector & Hyperbolic Projections

Applying the unit circle, the $(Y, X)$ vector plane, and the unit hyperbola on the keypad relies on the distinction between single-register circular projections and two-register vector transformations.

First, every circular and hyperbolic key (`{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`, `{{key:ASIN}}`, `{{key:ACOS}}`, `{{key:ATAN}}`, and their `{{key:HYP}}` counterparts) acts as a unary operator on Register $X$ in place and folds its argument via extended-precision Cody-Waite octant reduction without disturbing any physical baseline waiting in Registers $Y, Z,$ or $T$. Second, the coordinate keys shifted above `{{key:1}}`—`{{key:▸θ,r}}` (`y {{key:ENTER}} x {{key:▸θ,r}}`) and `{{key:▸y,x}}` (`θ {{key:ENTER}} r {{key:▸y,x}}`)—couple Registers $Y$ and $X$ as a simultaneous 2D vector pair whose rectangular output $(Y = y, X = x)$ feeds directly into `{{key:Σ+}}`.

### Angular Mode Verification & Direct Circular Projections

Standard surveying, mechanical, and navigational projections operate in Degrees mode (`{{key:DEG}}`) unless radians are explicitly required. Before starting a trigonometric calculation, a two-keystroke check via `{{res:sc32_04_trig_vectors_polar_seq_56:keys}}` confirms the active angular mode: in Degrees mode (`{{key:DEG}}`), $\sin(45^\circ)$ displays the unit-diagonal projection `0.707106781187` ($\sqrt{2}/2$), whereas in radian mode (`{{key:RAD}}`), $\sin(45\text{ rad})$ returns `0.850903524534`.

Planar trigonometric projections execute across Registers $X$ and $Y$ alone while Registers $Z$ and $T$ remain at zero because every circular function key (`{{key:SIN}}`, `{{key:COS}}`, `{{key:TAN}}`) is a unary in-place operator: when an angle is keyed into Register $X$ and `{{key:SIN}}` or `{{key:COS}}` is pressed, the angle is replaced in Register $X$ by its dimensionless unit-circle projection without lifting or disturbing any value waiting in Register $Y$:

* **Galileo's Projectile Apex & Range ($H_{\max} = \frac{(v_0\sin\theta)^2}{2g}$, $R = \frac{v_0^2\sin(2\theta)}{g}$):**
  Under Galileo's orthogonal parabolic decomposition for an artillery shell leaving the muzzle at $v_0 = 85.0\text{ m/s}$ inclined at $\theta = 38.0^\circ$ ($g = 9.80665\text{ m/s}^2$), hold the muzzle speed $85.0\text{ m/s}$ in Register $Y$ while transforming $38^\circ$ in place in Register $X$ into its vertical unit-circle projection $\sin(38^\circ) = 0.615661$. Multiplying those two terms yields the initial vertical climb velocity $v_{0y} = 52.3312\text{ m/s}$, and squaring in place with `{{key:x²}}` produces $v_{0y}^2 = 2,738.5574\text{ m}^2/\text{s}^2$; dividing by $2g = 19.6133\text{ m/s}^2$ gives the apex altitude. For the horizontal downrange impact distance across level terrain, evaluating the double-angle factor $\sin(2\theta) = \sin(76^\circ) = 0.9703$ and scaling by $v_0^2 / g$ resolves $R$ across the lower two registers:
  * **Projectile Apex Altitude ($H_{\max}$):** `{{res:sc32_04_trig_vectors_polar_seq_09:keys}}` $\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_09:value}}\text{ m}}$.
  * **Horizontal Downrange Distance ($R$):** `{{res:sc32_04_trig_vectors_polar_seq_10:keys}}` $\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_10:value}}\text{ m}}$.

* **Inclined-Plane Friction & `LASTX` Angle Recovery ($a = g(\sin\theta - \mu_k\cos\theta)$):**
  Along an inclined ramp where a supply crate slides down a surface tilted at $\theta = 34.0^\circ$ against a kinetic friction coefficient of $\mu_k = 0.22$ ($g = 9.80665\text{ m/s}^2$), two perpendicular projections of gravity compete along the incline: the downslope component $\sin(34^\circ) = 0.5592\,g$ and the normal force $\cos(34^\circ) = 0.8290\,g$, which scales by $\mu_k = 0.22$ into an upslope friction drag of $0.1824\,g$. Place $\sin(34^\circ) = 0.5592$ in Register $Y$, form the friction term $0.22\cos(34^\circ) = 0.1824$ in Register $X$ (recalling $34^\circ$ from `{{key:LASTX}}` if desired so the angle is not keyed twice), subtract them into the net traction factor $0.3768$, and multiply by $g$:
  * **Downhill Crate Acceleration:** `{{res:sc32_04_trig_vectors_polar_seq_23:keys}}` $\to a = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_23:value}}\text{ m/s}^2}$.

* **Two-Station Optical Mountain Triangulation ($H = \frac{d}{\cot\alpha - \cot\beta}$):**
  Applying the Great Trigonometrical Survey baseline formula across a level baseline of $d = 500.0\text{ m}$—measuring elevation angle $\alpha = 24.5^\circ$ at Station 1 and steeper angle $\beta = 31.2^\circ$ at Station 2—invert $\tan(24.5^\circ)$ via `{{key:TAN}} {{key:1/x}}` into $\cot(24.5^\circ) = 2.1943$ in Register $Y$, subtract $\cot(31.2^\circ) = 1.6512$ in Register $X$ to isolate the differential cotangent $\Delta\cot = 0.5431\text{ m/m}$, and use `{{key:x⇄y}}` to divide the $500\text{ m}$ baseline by $0.5431$:
  * **Triangulated Summit Height:** `{{res:sc32_04_trig_vectors_polar_seq_28:keys}}` $\to H = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_28:value}}\text{ meters}}$.

* **Large-Amplitude Pendulum Period Dilation ($T \approx T_0[1 + \frac{1}{4}\sin^2(\theta_0/2)]$):**
  To evaluate Huygens's nonlinear period lengthening for a clock pendulum ($T_0 = 2.000\text{ s}$) released from a $\theta_0 = 45.0^\circ$ amplitude, square the half-angle sine $\sin(22.5^\circ)$ in place to $\sin^2(22.5^\circ) = 0.1464$, scale by $1/4$ and add $1$ to form the dilation factor $1.0366$, and multiply by $T_0 = 2.0\text{ s}$:
  * **Stretched Pendulum Period:** `{{res:sc32_04_trig_vectors_polar_seq_29:keys}}` $\to T = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_29:value}}\text{ seconds}}$ ($+3.66\%$).

* **Multi-Tier Trigonometric Quotients & Nested Radical Cascades:**
  Compound trigonometric ratios and nested radicals such as:

  $$x_1 = \frac{\sin(35^\circ) \cos(42^\circ) + \tan(18^\circ)}{\sqrt{\sin^2(65^\circ) + \cos^2(25^\circ)}}, \qquad x_2 = \sqrt{\cos(28^\circ) + \sqrt{\sin(48^\circ) + \sqrt{\tan(15^\circ)}}}$$

  never touch Register $T$ because every circular function, square, and square root transforms Register $X$ in place. In $x_1$, the numerator folds into $0.7512$ in Register $Y$ while the denominator $\sqrt{\sin^2(65^\circ) + \cos^2(25^\circ)} = 1.2817$ assembles in Register $X$. In the three-level nested radical $x_2$, working from the innermost root outward evaluates $\sqrt{\tan(15^\circ)} = 0.5176$, adds $\sin(48^\circ)$ and takes `{{key:√x}}` ($\to 1.1228$), and adds $\cos(28^\circ)$ before the final `{{key:√x}}`:
  * **Compound Trigonometric Quotient ($x_1$):** `{{res:sc32_04_trig_vectors_polar_seq_40:keys}}` $\to \mathbf{0.5861}$.
  * **Nested Trigonometric Radical ($x_2$):** `{{res:sc32_04_trig_vectors_polar_seq_53:keys}}` $\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_53:value}}}$.

### Inverse Trigonometry & Oblique Triangles on the Stack

Just as `{{key:SIN}}`, `{{key:COS}}`, and `{{key:TAN}}` project an angle onto a dimensionless ratio in Register $X$, the inverse keys `{{key:ASIN}}`, `{{key:ACOS}}`, and `{{key:ATAN}}` recover the geometric angle from a physical ratio directly inside Register $X$:

* **Optical Fiber Critical Angle (`{{key:ASIN}}`) & Banked Highway Super-Elevation (`{{key:ATAN}}`):**
  Applying Ibn Sahl and Snell's total-internal-reflection law to laser light inside a silica optical fiber core ($n_1 = 1.480$) surrounded by glass cladding ($n_2 = 1.450$), divide $n_2 / n_1 = 0.9797$ and tap `{{key:ASIN}}` to find the critical trapping angle $\theta_c$. Similarly, to bank a highway curve of radius $R = 350.0\text{ m}$ for vehicles at $v = 100.0\text{ km/h}$ ($27.78\text{ m/s}$, $g = 9.80665\text{ m/s}^2$), form the lateral acceleration ratio $\tan\theta = \frac{v^2}{gR} = 0.2248$ in Register $X$ and tap `{{key:ATAN}}`:
  * **Optical Fiber Critical Angle ($\theta_c = \arcsin(n_2/n_1)$):** `{{res:sc32_04_trig_vectors_polar_seq_15:keys}}` $\to \theta_c = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_15:value}}^\circ}$.
  * **Zero-Slip Highway Banking Angle ($\theta = \arctan\frac{v^2}{gR}$):** `{{res:sc32_04_trig_vectors_polar_seq_16:keys}}` $\to \theta = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_16:value}}^\circ}$.

* **Four-Register Geocentric Satellite Look-Angle Elevation ($\tan E = \frac{\cos\gamma - R_E/(R_E + h)}{\sin\gamma}$):**
  Contrast that single-ratio highway turn with pointing a ground-station tracking dish at a low-Earth-orbit satellite at altitude $h = 850\text{ km}$ above an Earth of radius $R_E = 6,371\text{ km}$ and geocentric angular separation $\gamma = 18.0^\circ$. This trace (`{{res:sc32_04_trig_vectors_polar_seq_18:keys}}` $\to E = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_18:value}}^\circ}$) engages all four registers ($T, Z, Y, X$) because after $\cos(18^\circ) = 0.9511$ is evaluated on Row 1, computing the Earth-to-orbit radius ratio $\frac{6371}{6371 + 850} = 0.8823$ requires two `{{key:ENTER}}` strokes that lift $0.9511$ up into Register $Z$ and Register $T$. When `{{key:+}}` and `{{key:÷}}` collapse that radius ratio into $0.8823$, Register $T$'s automatic replication copies $0.9511$ back down into Register $Y$ so `{{key:-}}` can form the net vertical clearance $0.9511 - 0.8823 = 0.0688$ in Register $X$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `18 {{key:COS}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.9511$ | Cosine of angular distance $\cos\gamma$ |
| `6371 {{key:ENTER}} 6371 {{key:ENTER}} 850 {{key:+}} {{key:÷}} {{key:-}}` | $0.9511$ | $0.9511$ | $0.9511$ | $0.0688$ | Subtract orbital radius ratio $R_E / (R_E + h)$ |
| `18 {{key:SIN}} {{key:÷}}` | $0.9511$ | $0.9511$ | $0.9511$ | $0.2225$ | Divide by sine $\sin\gamma$ for elevation tangent |
| `{{key:ATAN}}` | $0.9511$ | $0.9511$ | $0.9511$ | **$12.5462$** | Extract ground satellite elevation angle $E$ (degrees) |

* **Keplerian True Anomaly, the Law of Cosines & Wave Interference:**
  Because a satellite in an elliptical orbit ($e = 0.240$) speeds up near perigee and slows down near apogee, Carl Friedrich Gauss's half-angle tangent transformation $\tan(\nu/2) = \sqrt{\frac{1 + e}{1 - e}}\tan(E/2)$ converts Kepler's uniform-circle *eccentric anomaly* $E = 40.0^\circ$ into the *true polar anomaly* $\nu$—the real sky angle from focus to satellite. Similarly, in oblique-triangle surveying and coherent wave superposition—a boundary corner with sides $a = 45.0\text{ m}$ and $b = 62.0\text{ m}$ separated by $C = 48.0^\circ$ ($c = \sqrt{a^2 + b^2 - 2ab\cos C}$), or two coherent sound waves of amplitudes $A_1 = 2.40\text{ Pa}$ and $A_2 = 3.10\text{ Pa}$ interfering at phase angle $\Delta\phi = 55.0^\circ$ ($A_{\text{res}} = \sqrt{A_1^2 + A_2^2 + 2A_1 A_2\cos\Delta\phi}$)—form the Pythagorean sum of squares in Register $Y$, build the $2ab\cos\theta$ cross-term in Register $X$, subtract or add, and press `{{key:√x}}`:
  * **Orbital True Anomaly ($\nu$ at $E = 40^\circ, e = 0.240$):** `{{res:sc32_04_trig_vectors_polar_seq_37:keys}}` $\to \nu = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_37:value}}^\circ}$.
  * **Law of Cosines Boundary Length ($c$):** `{{res:sc32_04_trig_vectors_polar_seq_11:keys}}` $\to c = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_11:value}}\text{ m}}$.
  * **Coherent Acoustic Wave Superposition ($A_{\text{res}}$):** `{{res:sc32_04_trig_vectors_polar_seq_34:keys}}` $\to A_{\text{res}} = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_34:value}}\text{ Pa}}$.

### Catenary Sag, Tsunami Wave Dispersion & Relativistic Rapidity on the Stack

Catenary sag, ocean wave dispersion, and relativistic velocity addition follow the same inside-out hyperbolic evaluation pattern. When a high-voltage transmission cable spans $L = 200\text{ meters}$, its half-span is $x = 100\text{ m}$; with catenary parameter $a = T_0 / w = 800\text{ meters}$, the midpoint sag $y = 800[\cosh(100/800) - 1]$ evaluates from the dimensionless ratio $x/a = 0.125$ outward (`{{key:HYP}} {{key:COS}}`, subtract $1$, and multiply by $800\text{ m}$). In physical oceanography, Airy's wave dispersion equation $c_{\text{wave}} = \sqrt{(g/k)\tanh(kh)}$ across a $h = 4,000\text{ m}$ ocean basin for a tsunami of wavelength $\lambda = 200,000\text{ m}$ ($k = 2\pi/\lambda \approx 0.000031416\text{ m}^{-1}$, $kh = 0.12566$) applies `{{key:HYP}} {{key:TAN}}` to $0.12566$, scales by $g/k$, and takes `{{key:√x}}` to yield a transoceanic wave speed of $c_{\text{wave}} \approx \mathbf{197.53\text{ m/s}}$ ($711.1\text{ km/h}$).

For Einstein and Minkowski's relativistic velocity addition, an interstellar probe cruising at $v_1 = 0.75c$ relative to Earth that launches a probe forward at $v_2 = 0.60c$ relative to the ship converts both speeds to hyperbolic rapidities via `{{key:HYP}} {{key:ATAN}}`, adds them on the stack ($\theta_{\text{total}} = 0.9730 + 0.6931 = 1.6661$), and maps the sum back via `{{key:HYP}} {{key:TAN}}`:
* **Catenary Transmission-Line Sag:** `{{res:sc32_04_trig_vectors_polar_seq_01:keys}}` $\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_01:value}}\text{ m}}$.
* **Relativistic Velocity Addition ($0.75c \oplus 0.60c$):** `{{res:sc32_04_trig_vectors_polar_seq_02:keys}}` $\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_02:value}}\,c}$ ($93.10\%$ of light speed).

### 2D Vector Projections, Wind Triangles, Traverses & 3D Space Frames

The $(Y = \theta, X = r) \leftrightarrow (Y = y, X = x)$ coordinate keys operate directly on Registers $Y$ and $X$. Keying a due-North vector of radius $r = 10$ at $\theta = 90^\circ$ via `{{res:sc32_04_trig_vectors_polar_seq_57:keys}}` verifies the register mapping: because `{{key:▸y,x}}` takes Angle $\theta$ in Register $Y$ and Radius $r$ in Register $X$, the projection places `0.0000` in Register $X$ ($x = 10\cos 90^\circ$) and `10.0000` in Register $Y$ ($y = 10\sin 90^\circ$). Conversely, keying a $3\text{-}4\text{-}5$ right triangle ($y = 4$ in Register $Y$, $x = 3$ in Register $X$) and pressing `{{key:▸θ,r}}` places the angle $\theta = 53.1301^\circ$ in Register $Y$ and the hypotenuse $r = 5.0000$ in Register $X$:

{{res:sc32_phasor_mag:screenshot|Direct rectangular-to-polar vector conversion on the StackCalc SC-32 places the angle θ = 53.1301° in Register Y and the radial magnitude r = 5.0000 in Register X.}}

Four applied vector calculations illustrate how `{{key:▸y,x}}`, `{{key:▸θ,r}}`, `{{key:Σ+}}`, and 3D dot products interact across the registers:

* **AC Electrical Power Triangle ($S = 1,020\text{ VA}$ at $\phi = 32.0^\circ$):**
  When an inductive AC motor draws $I_{\text{rms}} = 8.50\text{ A}$ from a $V_{\text{rms}} = 120.0\text{ V}$ line at a lagging phase angle of $\phi = 32.0^\circ$, total apparent power $S = V_{\text{rms}}I_{\text{rms}} = 1,020\text{ VA}$ splits into horizontal real shaft power $P = S\cos\phi$ (Watts) and vertical reactive magnetic power $Q = S\sin\phi$ ($\text{VAR}$). Duplicating $S = 1,020\text{ VA}$ across the stack and scaling by $\cos(32^\circ)$ and $\sin(32^\circ)$ (`{{res:sc32_04_trig_vectors_polar_seq_19:keys}}`) places $P = \mathbf{865.01\text{ W}}$ in Register $Y$ and $Q = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_19:value}}\text{ VAR}}$ in Register $X$ (or in a single coordinate stroke, keying `32 {{key:ENTER}} 1020 {{key:▸y,x}} {{key:x⇄y}}` resolves both legs onto $(Y, X)$ simultaneously):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `120 {{key:ENTER}} 8.5 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1020.0000$ | Total apparent electrical power $S = V_{\text{rms}} I_{\text{rms}}$ (VA) |
| `{{key:ENTER}} {{key:ENTER}} 32 {{key:COS}} {{key:×}}` | $0.0000$ | $0.0000$ | $1020.0000$ | $865.0091$ | Multiply by power factor $\cos(32^\circ)$ for real power $P$ (W) |
| `{{key:x⇄y}} 32 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $865.0091$ | **$540.5176$** | Multiply by reactive factor $\sin(32^\circ)$ for reactive power $Q$ (VAR) |

* **Aircraft Crosswind Vector Triangle ($\vec{V}_{\text{ground}} = \vec{V}_{\text{air}} + \vec{V}_{\text{wind}}$):**
  For an aircraft flying at true airspeed $V_{\text{air}} = 220.0\text{ kts}$ on North-Azimuth heading $\theta_1 = 45.0^\circ$ with a $35.0\text{-kt}$ downwind drift vector toward azimuth $\theta_2 = 130.0^\circ$ (a wind from $310^\circ$), projecting both vectors via `{{key:▸y,x}}` places Easting velocity in $Y$ and Northing velocity in $X$:
  * **Airspeed Projection ($\theta_1 = 45^\circ, r_1 = 220\text{ kts}$):** `{{res:sc32_04_trig_vectors_polar_seq_03:keys}}` $\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_03:value}}}$ ($V_{\text{air}, E} = 155.5635\text{ kts}$ in $Y$, $V_{\text{air}, N} = 155.5635\text{ kts}$ in $X$; store in `A` and `B`).
  * **Crosswind Projection ($\theta_2 = 130^\circ, r_2 = 35\text{ kts}$):** `{{res:sc32_04_trig_vectors_polar_seq_04:keys}}` $\to$ places $V_{\text{wind}, E} = 26.8116\text{ kts}$ in $Y$ and $V_{\text{wind}, N} = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_04:value}}}\text{ kts}$ in $X$.
  * **Component Summation & Polar Recovery (`{{key:▸θ,r}}`):** Summing components ($V_{\text{ground}, E} = 182.3750\text{ kts}$ in $Y$, $V_{\text{ground}, N} = 133.0659\text{ kts}$ in $X$) and pressing `{{key:▸θ,r}}` yields ground speed $V_{\text{ground}} = \mathbf{225.76\text{ knots}}$ in $X$ and true compass track $\theta_{\text{track}} = \mathbf{53.89^\circ}$ in $Y$.

* **Four-Leg Land Survey Traverse (`{{key:▸y,x}} {{key:Σ+}}`):**
  When walking a four-station closed-loop boundary around a rectangular parcel after clearing statistical memory (`{{key:CLΣ}}`), chaining `{{key:▸y,x}} {{key:Σ+}}` projects each North-Azimuth course $(\alpha_i, r_i)$ into $(\Delta E_i, \Delta N_i)$ and accumulates both coordinates straight into the statistical registers:
  * **Leg 1 ($\alpha = 60^\circ, r = 100\text{ m}$):** `{{res:sc32_04_trig_vectors_polar_seq_05:keys}}` $\to$ projects $(\Delta E = 86.6025\text{ m}, \Delta N = 50.0000\text{ m})$ at station $n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_05:value}}}$.
  * **Leg 2 ($\alpha = 150^\circ, r = 80\text{ m}$):** `{{res:sc32_04_trig_vectors_polar_seq_06:keys}}` $\to$ adds $(\Delta E = 40.0000\text{ m}, \Delta N = -69.2820\text{ m})$ at station $n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_06:value}}}$.
  * **Leg 3 ($\alpha = 240^\circ, r = 100\text{ m}$):** `{{res:sc32_04_trig_vectors_polar_seq_07:keys}}` $\to$ adds $(\Delta E = -86.6025\text{ m}, \Delta N = -50.0000\text{ m})$ at station $n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_07:value}}}$.
  * **Leg 4 ($\alpha = 330^\circ, r = 80\text{ m}$):** `{{res:sc32_04_trig_vectors_polar_seq_08:keys}}` $\to$ adds $(\Delta E = -40.0000\text{ m}, \Delta N = 69.2820\text{ m})$ and closes the loop at $n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_08:value}}}$, where `{{key:SUMS}}` confirms zero closure error ($\Sigma x = \Sigma\Delta N = 0.0000\text{ m}, \Sigma y = \Sigma\Delta E = 0.0000\text{ m}$).

* **Surveyor DMS Bearings (`{{key:▸HR}}`), Highway Curves, Pilot Endurance (`{{key:▸HMS}}`) & CNC Bolt Circles:**
  In field surveying, air navigation, forestry, and toolroom machining, sexagesimal `D.MMSS` / `H.MMSS` conversions (`{{key:▸HR}}` and `{{key:▸HMS}}` above `{{key:5}}`) and polar-rectangular projections (`{{key:▸y,x}}`) eliminate scratchpad conversion tables:
  * **DMS Theodolite Bearing Projection & Horizontal Highway Curve Stakeout:** When a total station records a North-Azimuth bearing of $42^\circ 18' 36''$ (`42.1836`) over a horizontal distance of $125.00\text{ m}$, pressing `{{key:▸HR}}` converts the sexagesimal angle in place to $42.3100^\circ$, and keying `125 {{key:▸y,x}}` resolves the leg into Easting departure $\Delta E = \mathbf{84.1386\text{ m}}$ in Register $Y$ and Northing latitude $\Delta N = \mathbf{92.4392\text{ m}}$ in Register $X$. Similarly, staking out a horizontal circular highway curve of radius $R = 250.00\text{ m}$ and central deflection angle $\Delta = 36^\circ 24' 00''$ (`36.24 {{key:▸HR}}` $\to 36.4000^\circ$) evaluates the long chord $L_c = 2R\sin(\Delta/2) = 500\sin(18.20^\circ) = \mathbf{156.1675\text{ m}}$ and middle ordinate $M = R(1 - \cos(\Delta/2)) = \mathbf{12.5028\text{ m}}$.
  * **Pilot Cockpit Time-En-Route & Fuel Endurance (`{{key:▸HMS}}`):** Flying a $385.0\text{ NM}$ cross-country leg at a groundspeed of $162.0\text{ knots}$ takes $385 / 162 = 2.3765\text{ decimal hours}$. Duplicating that quotient with `{{key:ENTER}}` and pressing `{{key:▸HMS}}` converts Register $X$ into `2.2236` ($2\text{ hr } 22\text{ min } 36\text{ s}$ en route), while swapping via `{{key:x⇄y}}` and multiplying the decimal hours by $14.8\text{ gal/hr}$ fuel flow yields $\mathbf{35.1728\text{ gallons}}$ burned with the `H.MMSS` ETA (`2.2236`) waiting in Register $Y$.
  * **Forestry Clinometer Tree Height & Machinist Sine-Bar / Bolt-Hole Circle Layout:** Sighting a Douglas fir from a horizontal tape distance $D = 30.0\text{ m}$ with clinometer angles $\theta_{\text{top}} = +52.0^\circ$ and $\theta_{\text{base}} = -8.0^\circ$ (`52 {{key:TAN}} 8 {{key:+/-}} {{key:TAN}} {{key:-}} 30 {{key:×}}`) yields a total height of $\mathbf{42.6143\text{ m}}$. In a machine shop, grinding a $14^\circ 15' 00''$ (`14.15 {{key:▸HR}} {{key:SIN}} 5 {{key:×}}`) taper on a $5.0000\text{-inch}$ sine bar requires a $\mathbf{1.2308\text{-inch}}$ gauge-block stack (wrung from $0.1008'' + 0.130'' + 1.000''$ blocks), while indexing the $60^\circ$ hole on a $R = 3.2500\text{-inch}$ bolt circle (`60 {{key:ENTER}} 3.25 {{key:▸y,x}}`) places both milling coordinates directly on $(Y = \mathbf{2.8146\text{ in}},\; X = \mathbf{1.6250\text{ in}})$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `42.1836 {{key:▸HR}}` | $0.0000$ | $0.0000$ | $0.0000$ | $42.3100$ | Convert DMS bearing $42^\circ 18' 36''$ to $42.3100^\circ$ |
| `125 {{key:▸y,x}}` | $0.0000$ | $0.0000$ | $84.1386$ | $92.4392$ | Project $125\text{ m}$ survey course to $(\Delta y, \Delta x)$ (m) |
| `385 {{key:ENTER}} 162 {{key:÷}}` | $84.1386$ | $84.1386$ | $92.4392$ | $2.3765$ | Flight time $385\text{ NM} / 162\text{ kts} = 2.3765\text{ hr}$ |
| `{{key:ENTER}} {{key:▸HMS}}` | $84.1386$ | $92.4392$ | $2.3765$ | $2.2236$ | Convert leg time to `H.MMSS` ($2\text{h } 22\text{m } 36\text{s}$) |
| `{{key:x⇄y}} 14.8 {{key:×}}` | $92.4392$ | $92.4392$ | $2.2236$ | **$35.1728$** | Fuel burn ($35.17\text{ gal}$) in $X$; `H.MMSS` ETA in $Y$ |

* **Mohr's Circle Strain Tensor, 3D Space-Frame Mitre Joints & Transpacific Great Circles:**
  Multi-term directional cosines fold into Register $X$ without overflowing the 4-level stack:
  * **Mohr's Circle Strain Transformation ($\epsilon_{x'} = \frac{\epsilon_x + \epsilon_y}{2} + \frac{\epsilon_x - \epsilon_y}{2}\cos(2\theta) + \frac{\gamma_{xy}}{2}\sin(2\theta)$):** For an aircraft wing rosette with $\epsilon_x = 450\,\mu\epsilon$, $\epsilon_y = 120\,\mu\epsilon$, and $\gamma_{xy} = 280\,\mu\epsilon$ rotated by $\theta = 30.0^\circ$ ($2\theta = 60.0^\circ$), accumulate the mean strain $285.0\,\mu\epsilon$, normal projection $82.5\,\mu\epsilon$, and shear projection $121.24\,\mu\epsilon$ sequentially (`{{res:sc32_04_trig_vectors_polar_seq_33:keys}}` $\to \epsilon_{x'} \approx \mathbf{488.74\,\mu\epsilon}$; `{{key:▸θ,r}}` on $140$ and $165\,\mu\epsilon$ extracts $R_{\text{Mohr}}$ directly).
  * **3D Space-Frame Cauchy-Schwarz Bevel Angle ($\cos\theta = \frac{\vec{A}\cdot\vec{B}}{\lvert\vec{A}\rvert\lvert\vec{B}\rvert}$):** For skew struts $\vec{A} = (4, 6, 8\text{ m})$ ($|\vec{A}|^2 = 116\text{ m}^2$) and $\vec{B} = (2, -3, 5\text{ m})$ ($|\vec{B}|^2 = 38\text{ m}^2$) with dot product $\vec{A}\cdot\vec{B} = 30.0\text{ m}^2$, divide $30.0$ by $\sqrt{116}$ and $\sqrt{38}$ (`{{key:√x}} {{key:÷}}`) and apply `{{key:ACOS}}`: `{{res:sc32_04_trig_vectors_polar_seq_20:keys}}` $\to \theta = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_20:value}}^\circ}$.
  * **Transpacific Great-Circle Orthodrome (San Francisco $\to$ Tokyo Narita):** Applying the Spherical Law of Cosines between SFO ($\phi_1 = 37.6189^\circ\text{ N}, \lambda_1 = -122.3750^\circ\text{ W}$) and NRT ($\phi_2 = 35.7720^\circ\text{ N}, \lambda_2 = 140.3929^\circ\text{ E}$, span $\Delta\lambda = 97.2321^\circ$), form $\sin\phi_1\sin\phi_2 = 0.356820$ (`{{res:sc32_04_trig_vectors_polar_seq_54:keys}}`), assemble $\cos\phi_1\cos\phi_2\cos\Delta\lambda = -0.080904$ (`{{res:sc32_04_trig_vectors_polar_seq_55:keys}}`), sum into $\cos d = 0.275916$, and apply `{{key:ACOS}}` ($\to d = 73.9833^\circ$, or $\mathbf{8,226.6\text{ km}}$ at $R_E = 6,371\text{ km}$).
  * **Heliostat Solar Concentrator Elevation ($\sin\alpha = \sin\phi\sin\delta + \cos\phi\cos\delta\cos\omega$):** At latitude $\phi = 32.0^\circ\text{ N}$, declination $\delta = 18.5^\circ$, and hour angle $\omega = 45.0^\circ$, summing the two spherical projections and pressing `{{key:ASIN}}` (`{{res:sc32_04_trig_vectors_polar_seq_41:keys}}`) locks onto $\alpha \approx \mathbf{47.46^\circ}$ ($47.4611^\circ$).

From Eratosthenes's shadow angle at Alexandria to space-frame bevels and relativistic rapidities, circular and hyperbolic functions project directed quantities onto orthogonal axes, while `{{key:▸y,x}}` and `{{key:▸θ,r}}` unify planar vectors, traverses, and spherical astronomy across $(Y, X)$.
