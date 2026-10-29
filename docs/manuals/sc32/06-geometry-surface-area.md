---
title: "Chapter 6: The Square-Cube Law, Solid Geometry & Three-Dimensional Space | Thinking in the Stack (SC-32)"
description: "Galileo's Square-Cube Law, Heron's triangle, Ramanujan's ellipse, Archimedes' inscribed sphere and cylinder, Cavalieri's slices, and 3D rotational inertia on the StackCalc SC-32."
---

# Chapter 6: The Square-Cube Law, Solid Geometry & Three-Dimensional Space

## Galileo's Giant and the Square-Cube Law

### Bone Cross-Section Versus Body Mass

A common garden ant hoists a leaf ten times its own body weight, whereas a human athlete struggles to lift a barbell of a single body mass. If a human being were scaled up by a factor of ten into a sixty-foot giant with every proportion of bone, muscle, and sinew held geometrically identical, the giant's femurs would shatter the moment it tried to stand.

In 1638, while confined under house arrest at his villa in Arcetri outside Florence, Galileo Galilei explained this disparity in his final treatise, *Two New Sciences* (*Discorsi e dimostrazioni matematiche intorno a due nuove scienze*) {{cite:galilei1638}}. Galileo demonstrated that nature is governed by a strict geometric asymmetry between area and volume, now known as the *Square-Cube Law*.

When any three-dimensional object, such as an ant, a cathedral column, a spherical fuel tank, or a silicon microprocessor, has every linear dimension (length, width, and height) scaled by a multiplier $\ell$, its area and volume diverge in growth:

$$L \longrightarrow \ell L, \qquad A \propto \ell^2, \qquad V \propto \ell^3, \qquad \frac{A}{V} \propto \frac{\ell^2}{\ell^3} = \frac{1}{\ell}$$

The tensile or compressive strength of a bone or steel column depends on its *cross-sectional area* ($A \propto \ell^2$), because that cross-section is where intermolecular bonds resist the load. Likewise, aerodynamic drag during a fall and the rate at which an organism or machine can shed heat, absorb oxygen across lung membranes, or radiate thermal energy depend on its *exposed surface area* ($A \propto \ell^2$). Yet the gravitational weight the skeleton must support, as well as the metabolic or electrical heat generated inside the body, depends on the number of cells or atoms inside its *enclosed volume* ($V \propto \ell^3$).

When a human being's height, width, and depth are multiplied by $\ell = 10$ to form a sixty-foot giant, the cross-sectional area of the leg bones increases by $10^2 = 100\text{ times}$, whereas the volume and weight increase by $10^3 = 1,000\text{ times}$. Every square centimeter of the giant's bone is subjected to ten times the compressive stress of a normal human femur and fractures under its own weight. Evolutionary biologist J. B. S. Haldane analyzed this biomechanical limit in his 1926 essay *"On Being the Right Size,"* calculating why the sixty-foot Giant Pope and Giant Pagan in *Pilgrim's Progress* would shatter their thighs at every step.

Conversely, as Haldane noted, a mouse or an ant dropped down a thousand-foot mine shaft walks away unharmed: because terminal velocity in air occurs where gravitational weight ($\propto \ell^3$) balances aerodynamic drag ($\propto A v^2 \propto \ell^2 v^2$), terminal impact speed scales as $v_{\text{term}} \propto \sqrt{\ell^3 / \ell^2} = \sqrt{\ell}$. To survive on land, large animals cannot be scaled-up small animals. As Galileo sketched in the margins of *Two New Sciences*, an elephant or a *Brachiosaurus* requires disproportionately thick, pillar-like legs. For the same reason, a civil engineer scaling a tabletop balsa-wood bridge model up by $\ell = 50$ across a river gorge must thicken the steel chords or switch to hollow box girders lest the full-scale span collapse under its own dead weight.

### J. B. S. Haldane's Thermal Wall: Surface Area ($L^2$) vs. Volume ($L^3$)

This same $A/V \propto 1/\ell$ ratio governs thermal survival across biology and modern electronics. Inside a high-performance microprocessor, billions of nanometer-scale transistors switch at gigahertz frequencies and produce localized thermal flux exceeding $100\text{ W/cm}^2$, a power density approaching the heat flux inside a nuclear reactor core. Under Jean-Baptiste Joseph Fourier's Law of Thermal Conduction and Isaac Newton's Law of Cooling {{cite:incropera2007}}, convective heat removal from a solid boundary to a surrounding fluid is proportional to the exposed surface area $A_{\text{surface}}$:

$$\dot{Q} = h \cdot A_{\text{surface}} \cdot (T_{\text{solid}} - T_{\text{fluid}})$$

Because heat generation scales with volume ($\ell^3$) while heat dissipation scales with surface area ($\ell^2$), scaling up any heat-producing body creates a thermal bottleneck. In warm-blooded biology, this scaling contrasts metabolic torpor in hummingbirds with vascular radiators in elephants. A $3\text{-gram}$ ruby-throated hummingbird ($\ell \approx 2\text{ cm}$) has a large surface-area-to-volume ratio ($A/V \propto 1/\ell$). It loses body heat across its skin so rapidly relative to its small thermal mass that its heart must beat $1,200\text{ times per minute}$ by day, and it must enter deep hypothermic *torpor* at night to avoid starving before dawn.

Conversely, a $5,000\text{-kilogram}$ African elephant ($\ell \approx 200\text{ cm}$, a $100\times$ linear scale-up over the hummingbird) generates $100^3 = 1,000,000\times$ the internal metabolic heat while possessing only $100^2 = 10,000\times$ the skin surface area. With $1/100\text{th}$ the relative cooling area, an elephant would overheat if evolution had not departed from geometric similarity by equipping it with thin, vascularized ear-fins that act as biological radiators.

A silicon CPU package faces the same thermal constraint, which engineers resolve with extruded pin-fin arrays. Leaving an aluminum heat spreader as a flat block provides minimal surface area, whereas machining or extruding the aluminum into dozens of thin parallel fins removes volume and mass while multiplying the exposed convective boundary area $A_{\text{surface}}$ by $300\%$ to $2,500\%$. This geometry overcomes Galileo's Square-Cube Law by folding additional surface area into the same footprint.

In real-world mechanical design, aerospace enclosures, heat sinks, and structural castings are never isolated cubes. They are bounded by dozens of planar walls, sloped frustum roofs, cylindrical bosses, and cutout apertures. On the SC-32, you audit a composite solid by using the statistical accumulator `{{key:Σ+}}` as a *surface-area and volume ledger*. First clear the statistical registers with `{{key:CLΣ}}` (`{{key:↰}}` + `{{key:Σ+}}`), then evaluate each rectangular wall, circular boss, or trapezoidal facet on Registers $Y$ and $X$ and add it with `{{key:Σ+}}`, or deduct drilled holes and window cutouts with `{{key:Σ-}}`. Register $X$ counts each finished face group ($n = 1, 2, 3, \dots$) until `{{key:SUMS}}` (`{{key:↱}}` + `{{key:Σ+}}`) and softkey `{{key:Σx}}` recall the grand total.

---

## Heron's Triangle, Ramanujan's Ellipse & Archimedes' Cylinder

To measure triangular land parcels, bolted pipe flanges, planetary oblateness, and curved pressure vessels, mathematicians over two millennia established a body of planar and solid mensuration formulas. Each formula encodes a geometric relation that reduces a multi-step measurement to a direct stack calculation.

### Planar Primitives, Difference-of-Squares Rings & Silver-Ratio Octagons

Every three-dimensional cross-section or enclosure boundary begins with two-dimensional planar figures, ranging from rectangles, triangles, trapezoids, and circles to circular sectors, ellipses, parabolic arches, and cyclic quadrilaterals. On the four-register stack, *factoring differences of squares* ($R^2 - r^2 = (R - r)(R + r)$) and *exploiting geometric symmetry* reduce intricate planar sections to one-pass calculations that require no intermediate scratchpad storage.

The *circular annulus* is the flat ring formed by a pipe flange gasket, a thrust washer, or a hollow cylindrical wall bounded by outer radius $R$ and inner bore radius $r$. Evaluating $\pi R^2 - \pi r^2$ term by term multiplies by $\pi$ twice and loses significant digits when the wall is thin ($R \approx r$), because squaring two nearly equal radii and subtracting them cancels their leading digits. Factoring the difference of squares resolves both issues at once:

$$A = \pi(R^2 - r^2) = \pi(R - r)(R + r) = 2\pi \left(\frac{R + r}{2}\right)(R - r)$$

Geometrically, this factored form says that if you snip a circular ring and unroll it, its exact area equals its *average circumference* $2\pi R_{\text{mean}}$ multiplied by its *radial wall thickness* $t = R - r$. On the SC-32, you can either subtract the squares `R {{key:x²}} r {{key:x²}} {{key:-}} {{key:π}} {{key:×}}` or form $(R - r)$ in Register $Y$ and $(R + r)$ in Register $X$ before pressing `{{key:×}} {{key:π}} {{key:×}}` to preserve full precision on thin-walled aerospace tubing. Deferring the transcendental multiplier $\pi$ until after the radial terms have been combined keeps the intermediate span exact and avoids scaling by $\pi$ twice.

When an instrument cover or structural gusset is a *regular octagon* of side length $s$ rather than a circle, its area follows directly from square dissection without a trigonometric cotangent lookup. A regular octagon is a bounding square of width $(1 + \sqrt{2})s$ that has had four $45^\circ\text{–}45^\circ\text{–}90^\circ$ right-isosceles corner triangles of leg $s/\sqrt{2}$ clipped off its four corners. Each clipped corner has area $\frac{1}{2}(s/\sqrt{2})^2 = \frac{1}{4}s^2$, so all four corners together remove $s^2$ from the bounding square $(1 + \sqrt{2})^2 s^2 = (3 + 2\sqrt{2})s^2$:

$$A = (3 + 2\sqrt{2})s^2 - s^2 = 2(1 + \sqrt{2})s^2 = 2\delta_S s^2 \approx 4.828427 \, s^2$$

where $\delta_S = 1 + \sqrt{2} \approx 2.414214$ is the classical *silver ratio* (`2 {{key:√x}} 1 {{key:+}}`), which satisfies $\delta_S^2 = 2\delta_S + 1$ and $1/\delta_S = \delta_S - 2 = \sqrt{2} - 1$.

### Ramanujan's Ellipse Perimeter & Earth's Equatorial Bulge

One of the great surprises of classical geometry is the stark contrast between the *area* of an ellipse and its *perimeter*. Because an ellipse with semi-major axis $a$ and semi-minor axis $b$ is a circle of radius $b$ stretched along one axis by the factor $a/b$, its area scales by that same factor: $A = \pi b^2 \cdot (a/b) = \pi a b$. Yet if you ask for the *perimeter* (circumference) of that same ellipse, no closed-form expression in elementary functions exists anywhere in mathematics. Setting up the arc-length integral $\int \sqrt{dx^2 + dy^2}$ leads to an irreducible integral that defied Leonhard Euler and Adrien-Marie Legendre and gave *elliptic integrals* their name.

In 1914, the Indian mathematician Srinivasa Ramanujan published a compact algebraic approximation for the perimeter of an ellipse. Ramanujan defined the dimensionless symmetric flattening parameter $h$:

$$h = \frac{(a - b)^2}{(a + b)^2}, \qquad P \approx \pi (a + b) \left[ 1 + \frac{3h}{10 + \sqrt{4 - 3h}} \right]$$

The accuracy of Ramanujan's formula becomes clear when expanding the exact Gauss–Kummer complete elliptic integral for the perimeter of an ellipse as a power series in $h$: $P = \pi(a+b)\left[1 + \frac{1}{4}h + \frac{1}{64}h^2 + \frac{1}{256}h^3 + \frac{25}{16384}h^4 + \frac{49}{65536}h^5 + \dots\right]$. Expanding Ramanujan's nested square root in a Taylor series, $\frac{3h}{10 + \sqrt{4 - 3h}} = \frac{1}{4}h + \frac{1}{64}h^2 + \frac{1}{256}h^3 + \frac{25}{16384}h^4 + \frac{45}{65536}h^5 + \dots$, matches the exact Gauss–Kummer complete elliptic integral through the $h^1, h^2, h^3$, and $h^4$ terms ($\frac{25}{16384}h^4$), first differing at the $h^5$ coefficient ($\frac{45}{65536}h^5$ vs. $\frac{49}{65536}h^5$) by just $\frac{4}{65536} = \frac{1}{16384}h^5$. Even for highly elongated orbits and elliptical machine cams, Ramanujan's formula is accurate to better than a part per million.

That axial difference $(a - b)$ between semi-major and semi-minor axes also governs the shape of rotating planets. As Isaac Newton predicted in Book III of the *Principia* (1687) and Alexis Claude Clairaut formalized in *Théorie de la figure de la terre* (1743), because the Earth rotates once every $23\text{ hours } 56\text{ minutes}$, centrifugal acceleration forces ocean and mantle outward at the equator and deforms our planet from a sphere into an *oblate spheroid* with equatorial semi-major axis $a$ and polar semi-minor axis $b$. Geodesists express this polar compression by the dimensionless *flattening* $f$ and its reciprocal $1/f$ (evaluated on the stack without re-typing $a$ via `b {{key:ENTER}} a {{key:÷}} 1 {{key:x⇄y}} {{key:-}} {{key:1/x}}`):

$$f = \frac{a - b}{a} = 1 - \frac{b}{a}, \qquad \frac{1}{f} = \frac{a}{a - b} = \frac{1}{1 - b/a}$$

Because the Mississippi River flows southward toward Earth's equatorial bulge, its mouth at the Gulf of Mexico sits roughly four miles *farther* from the center of the Earth than its headwaters at Lake Itasca.

### Heron's Semiperimeter Formula & Right-Triangle Incircles

When a surveyor in the field measures the three boundary lengths $(a, b, c)$ of a triangular parcel using a steel tape or laser rangefinder, finding the parcel's area from $A = \frac{1}{2}bh$ would normally require solving for an interior angle via the Law of Cosines and then taking a sine to find the perpendicular altitude $h$.

In the 1st century CE, Heron of Alexandria proved in his *Metrica* (a work rediscovered in a Constantinople manuscript in 1896, though Archimedes likely knew the theorem two centuries earlier) that you can bypass trigonometry completely. Define the *semiperimeter* $s$ as half the triangle's perimeter:

$$s = \frac{a + b + c}{2}, \qquad A = \sqrt{s(s - a)(s - b)(s - c)}$$

Storing the semiperimeter $s$ in Variable `S` (`{{key:STO}} S`) lets you subtract each side in turn and multiply the three excess factors $(s - a)$, $(s - b)$, and $(s - c)$ right on the stack before scaling by $s$ and extracting `{{key:√x}}`. Better still, Heron's radicand contains a built-in physical diagnostic: by the Euclidean *triangle inequality*, the sum of any two sides of a real triangle must exceed the third ($a + b > c$, which means $s > c$ and $(s - c) > 0$). If a misread blueprint specifies three lengths that cannot possibly close into a triangle, such as $3, 4$, and $9$ where $s = 8$ and $(s - 9) = -1 < 0$, the factor $(s - c)$ turns negative and `{{key:√x}}` flags an impossible geometry (`INVALID DATA`).

The semiperimeter $s$ also governs the inscribed circle of a triangle. Dropping an *incircle* of radius $r$ inside any triangle so that it touches all three sides tangentially, and drawing lines from the incenter to the three vertices, partitions the triangle into three smaller triangles of heights $r$ and bases $a, b, c$, whose areas sum to $\frac{1}{2}ar + \frac{1}{2}br + \frac{1}{2}cr = \left(\frac{a+b+c}{2}\right)r = s \cdot r$. Thus, for *every* triangle:

$$A = r \cdot s \implies r = \frac{A}{s}$$

Once Heron's area $A$ sits in Register $X$ and the semiperimeter $s$ still resides in Variable `S` (or in `{{key:LASTX}}` before the square root), a single recall and division (`{{key:RCL}} S {{key:÷}}`) delivers the exact inscribed circle radius $r = A/s$ of *any* triangle. When the triangle happens to be a *right triangle* with orthogonal legs $a$ and $b$ and hypotenuse $c = \sqrt{a^2 + b^2}$ (computed in one keystroke via `{{key:▸θ,r}}`), the tangent segments around the $90^\circ$ corner simplify $r = A/s$ into the linear relation $r = \frac{a + b - c}{2}$: because the two tangent segments at the right angle form a square of side $r$, the remaining segments $(a - r)$ and $(b - r)$ fold onto the hypotenuse so that $(a - r) + (b - r) = c$.

When a parcel's corners are specified by Cartesian survey coordinates $(x_1, y_1)$ and $(x_2, y_2)$ relative to an origin monument, Carl Friedrich Gauss's *Shoelace Theorem* gives the signed parallelogram area spanned by the two vectors as the $2 \times 2$ determinant $D = \det\begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix} = x_1 y_2 - y_1 x_2$ (with triangle area $A = \frac{1}{2}|D|$). That determinant evaluates in seven RPN keystrokes without a single storage register via `x1 {{key:ENTER}} y2 {{key:×}} y1 {{key:ENTER}} x2 {{key:×}} {{key:-}}`, and it likewise solves any $2 \times 2$ simultaneous linear system $a_1 x + b_1 y = c_1,\; a_2 x + b_2 y = c_2$ on the stack via Gabriel Cramer's Rule ($x = \frac{c_1 b_2 - b_1 c_2}{a_1 b_2 - b_1 a_2},\; y = \frac{a_1 c_2 - c_1 a_2}{a_1 b_2 - b_1 a_2}$).

### Cavalieri's Coin Stack, Archimedes' Inscribed Sphere and Cylinder & the Steinmetz Bicylinder

Centuries before Isaac Newton and Gottfried Wilhelm Leibniz codified integral calculus, geometers determined the exact volumes of cones, spheres, paraboloids, and intersecting pipes by comparing cross-sectional slices.

The foundational principle of solid mensuration was formalized in 1635 by Galileo's student Bonaventura Cavalieri, building on methods developed earlier by Archimedes of Syracuse and the 3rd-century Chinese mathematicians Liu Hui and Zu Chongzhi. If twenty coins are stacked into a vertical cylinder on a desk and then nudged sideways so the column leans over or curves into an S-shape, the total volume of the stack does not change by a single cubic millimeter. *Cavalieri's Principle* states that if two solids have the same total height, and if slicing them parallel to their bases at *every* height $z$ reveals cross-sections of identical area $A(z)$ (or a constant ratio of areas), then their total volumes must be identical (or stand in that same ratio).

When the cross-sectional area $A(z)$ of a solid varies as any linear, quadratic, or cubic function of height $z$, English mathematician Thomas Simpson showed in 1743 that you can find the solid's exact volume from just three horizontal slices—the bottom base $A_{\text{bottom}}$, the mid-height slice $A_{\text{mid}}$ (weighted by $4$), and the top roof $A_{\text{top}}$—via *Simpson's Universal Prismoidal Formula*:

$$V = \frac{h}{6}\left(A_{\text{bottom}} + 4A_{\text{mid}} + A_{\text{top}}\right)$$

{{blocks:sc32_concept_cavalieri_simpson|Galileo's square-cube scaling law and Simpson's universal prismoidal three-slice volume formula.}}

Cavalieri's Principle and Simpson's three-slice rule unify the classical volume formulas of solid geometry. When any pyramid or cone is sliced horizontally at distance $z$ below its apex, its linear dimensions grow linearly with $z/h$, so its cross-sectional area grows *quadratically* as $A(z) = A_{\text{base}}(z/h)^2$. Because the average value of $(z/h)^2$ from $0$ to $h$ is $\frac{1}{3}$ (which also follows from dissecting a cube into three identical square pyramids meeting at one corner), *every* cone or pyramid encloses one-third the volume of its bounding prism or cylinder, $V = \frac{1}{3}A_{\text{base}}h$ (`3 {{key:÷}}`), whether its base is a circle, a square, an octagon, or an ellipse ($A_{\text{base}} = \pi ab$, where $V = \frac{1}{3}\pi abh$). Likewise, a *paraboloid of revolution* whose radius grows as $r(z) \propto \sqrt{z}$ has cross-sectional area $A(z) \propto z$, whose average from $0$ to $h$ is one-half ($V = \frac{1}{2}\pi r^2 h$).

Above his war machines, his law of the lever, and his hydrostatics, Archimedes prized his proof in *On the Sphere and Cylinder* (c. 225 BCE): when a sphere of radius $r$ is inscribed inside a right circular cylinder of radius $r$ and height $h = 2r$, both the volume and the total surface area of the sphere equal two-thirds ($\frac{2}{3}$) of the cylinder. Archimedes established this ratio by comparing horizontal slices. When the top hemisphere of radius $r$ is placed beside a cylinder of radius $r$ and height $r$ that has had an inverted $45^\circ$ cone ($r_{\text{cone}}(z) = z$) carved out of its center, and both solids are sliced at height $z$ above the equator, the Pythagorean theorem shows that the hemisphere's slice is a disk of radius $\sqrt{r^2 - z^2}$ and area $\pi(r^2 - z^2)$.

Meanwhile, the punctured cylinder's slice is an annulus of outer radius $r$ and inner hole radius $z$, whose area is also $\pi(r^2 - z^2)$. Because every horizontal slice matches identically, the hemisphere's volume equals the cylinder minus the cone: $\pi r^3 - \frac{1}{3}\pi r^3 = \frac{2}{3}\pi r^3$. Doubling for both hemispheres gives $V_{\text{sphere}} = \frac{4}{3}\pi r^3 = \frac{2}{3}(2\pi r^3) = \frac{2}{3}V_{\text{cylinder}}$, while its surface area $A_{\text{sphere}} = 4\pi r^2$ is likewise $\frac{2}{3}$ of the cylinder's total area ($2\pi r^2 + 2\pi r(2r) = 6\pi r^2$). At Archimedes' request, a sphere inscribed inside a cylinder with the ratio $2:3$ was carved onto his funerary monument in Syracuse, and it was by spotting that carving overgrown with brambles in 75 BCE that the Roman orator Cicero rediscovered Archimedes' forgotten grave.

When two equal circular cylinders of radius $r$ intersect at a $90^\circ$ right angle, as in a high-pressure refinery cross-joint or a Roman groin vault, the common volume forms a Steinmetz bicylinder. Both Archimedes (in *The Method*, preserved on the Archimedes Palimpsest) and Liu Hui (who named the intersection solid the *Mouhefanggai*, or "two square umbrellas") identified a geometric cancellation when a sphere of radius $r$ is inscribed inside the intersection of the two pipes. Slicing the bicylinder horizontally at height $z$, where both cylinders have half-width $\sqrt{r^2 - z^2}$, produces a *square* cross-section of side $2\sqrt{r^2 - z^2}$ and area $4(r^2 - z^2)$, whereas the inscribed sphere's slice is a *circle* of area $\pi(r^2 - z^2)$. At every slice from bottom to top, the bicylinder's square slice is $\frac{4}{\pi}$ times the sphere's circular slice, so by Cavalieri's Principle $\pi$ cancels out of the volume completely:

$$V_{\text{bicylinder}} = \frac{4}{\pi} \left(\frac{4}{3}\pi r^3\right) = \frac{16}{3} r^3, \qquad A_{\text{bicylinder}} = 16 r^2$$

Even though the solid is bounded entirely by curved cylindrical walls, neither its volume nor its surface area contains $\pi$.

When a cone or pyramid is sliced flat at height $h$ before reaching its apex, with bottom radius $R$ and top radius $r$, the resulting conical frustum has volume $V = \frac{1}{3}\pi h(R^2 + Rr + r^2)$, a formula already recorded for square pyramids in the 1850 BCE Moscow Mathematical Papyrus. On the SC-32, squaring $R$ via `R {{key:x²}}` automatically saves $R$ in `{{key:LASTX}}`, so keying `{{key:LASTX}} r {{key:×}} {{key:LASTX}} {{key:x²}} {{key:+}} {{key:+}}` forms the three-term sum $(R^2 + Rr + r^2)$ while typing $R$ and $r$ only once each. Physically, the frustum's volume equals its height $h$ multiplied by the *arithmetic average of three areas*: the bottom base $A_1 = \pi R^2$, the top base $A_2 = \pi r^2$, and their *geometric mean* $\sqrt{A_1 A_2} = \pi Rr$.

The volume coefficient $\frac{\sqrt{2}}{12}a^3$ of a regular tetrahedron of edge length $a$ follows from inscribing it inside a cube. Drawing the face diagonals that connect four alternating corners of a cube of edge length $c = a/\sqrt{2}$ (so each face diagonal has length $\sqrt{2}c = a$) constructs a regular tetrahedron of edge $a$ inside the cube. The space outside the tetrahedron consists of four right-angled corner pyramids, each having three mutually perpendicular legs of length $c$ and volume $\frac{1}{3}\left(\frac{1}{2}c^2\right)c = \frac{1}{6}c^3$. Slicing off those four corners removes $4 \times \frac{1}{6} = \frac{2}{3}$ of the cube, so the central tetrahedron retains $1 - \frac{2}{3} = \frac{1}{3}$ of the cube's volume: $V = \frac{1}{3}c^3 = \frac{1}{3}\left(\frac{a}{\sqrt{2}}\right)^3 = \frac{\sqrt{2}}{12}a^3$.

In the volume ($V = 2\pi^2 R r^2$) and surface area ($A = 4\pi^2 R r$) of a *torus*—an O-ring gasket with major orbit radius $R$ and minor tube cross-section radius $r$—the constant $\pi$ appears *squared* ($\pi^2 \approx 9.8696$, evaluated via `{{key:π}} {{key:x²}}`) because two orthogonal circles are multiplied together. Around 340 CE, Pappus of Alexandria (rediscovered in 1640 by Swiss mathematician Paul Guldin in his *Centrobaryca*, 1635–1641) proved two theorems that link solid mensuration to the *centroid* (center of mass) of a planar figure. Under the First Theorem of Pappus-Guldinus for surface area of revolution, when a planar curve of arc length $L$ is revolved around an external axis in its plane, the surface area swept out equals the curve's length $L$ multiplied by the circumference of the circle $2\pi R_{\text{cm}}$ traveled by its centroid:

$$A = L \cdot \left(2\pi R_{\text{cm}}\right)$$

For a torus, the generating circle has circumference $L = 2\pi r$ and its centroid travels a circle of length $2\pi R$, which yields $A = (2\pi r)(2\pi R) = 4\pi^2 R r$, equivalent to slicing the O-ring open and unrolling it into a straight cylinder of length $2\pi R$. Under the Second Theorem of Pappus-Guldinus for volume of revolution, when a planar region of area $A_{\text{cross}}$ is revolved around an external axis, the volume swept out equals the cross-sectional area $A_{\text{cross}}$ multiplied by the distance $2\pi R_{\text{cm}}$ traveled by its centroid:

$$V = A_{\text{cross}} \cdot \left(2\pi R_{\text{cm}}\right)$$

For the torus, a circular disk of area $A_{\text{cross}} = \pi r^2$ orbits a path of length $2\pi R$, which produces $V = (\pi r^2)(2\pi R) = 2\pi^2 R r^2$ without evaluating an integral.

Whereas two-dimensional space admits infinitely many regular polygons, three-dimensional space permits only five regular convex polyhedra: the 4-faced tetrahedron, 6-faced cube, 8-faced octahedron, 12-faced dodecahedron, and 20-faced icosahedron. In 1750, Leonhard Euler discovered the topological invariant governing every convex polyhedron with $V$ vertices, $E$ edges, and $F$ faces:

$$V - E + F = 2$$

Stretching a polyhedron's wireframe onto a rubber sphere, puncturing one face, and flattening the remaining $F - 1$ faces onto a plane illustrates this invariant: removing each edge merges two faces ($\Delta E = -1, \Delta F = -1$, which preserves $V - E + F$), and contracting a tree of $V$ vertices and $V - 1$ edges to a single point yields $1 - 0 + 1 = 2$.

At every vertex of a convex polyhedron, at least $3$ faces must meet, and their flat corner angles must sum to strictly *less than $360^\circ$* so the faces can fold into a 3D corner rather than lying flat. Equilateral triangles have $60^\circ$ corners, so $3$, $4$, or $5$ of them can fold around a vertex at $180^\circ, 240^\circ,$ or $300^\circ$ to build the tetrahedron, octahedron, and icosahedron. Squares have $90^\circ$ corners, so $3$ meet per vertex at $270^\circ$ to form the cube, while regular pentagons have $108^\circ$ corners, so $3$ meet per vertex at $324^\circ$ to form the dodecahedron. At six sides, three regular hexagons meet at $3 \times 120^\circ = 360^\circ$ and lie flat in a plane, which precludes any regular polyhedron with six or more sides per face.

### Spherical Caps, Girard's Spherical Excess & Asteroid Power Means

Curved shells and planetary surfaces follow three additional mensuration laws for spherical caps, spherical triangles, and triaxial ellipsoids. In petrochemical refineries, liquefied gases are stored inside spherical *Hortonsphere* tanks of radius $R$ because a sphere resists internal pressure with uniform membrane tension (half the hoop stress of a cylinder of equal radius). When an ultrasonic sensor measures liquid depth $h$ at the bottom of the sphere, integrating horizontal disk slices of radius $r^2(z) = R^2 - (R-z)^2 = 2Rz - z^2$ from $z = 0$ to $h$ gives the *spherical cap volume*:

$$V_{\text{cap}} = \int_0^h \pi(2Rz - z^2)\,dz = \pi\left(Rh^2 - \frac{1}{3}h^3\right) = \frac{1}{3}\pi h^2(3R - h)$$

Archimedes also proved that the curved surface area of any spherical cap or zone of thickness $h$ is $A_{\text{zone}} = 2\pi R h$, which depends *only* on the slice thickness $h$ and matches the lateral wall area punched out on the circumscribing cylinder.

On a flat plane, the interior angles of every triangle sum to $180^\circ$ ($\pi\text{ rad}$), whether the triangle is drawn on a postage stamp or across a field. On a curved sphere of radius $R$, however, great-circle paths bow outward, and the interior angles $(\alpha, \beta, \gamma)$ of a *spherical triangle* *always* sum to more than $180^\circ$. Starting at the North Pole, walking south to the Equator along the Prime Meridian, turning $90^\circ$ west along the Equator to $90^\circ\text{ W}$, and turning $90^\circ$ north back to the North Pole traces a spherical triangle with three $90^\circ$ right angles ($\alpha + \beta + \gamma = 270^\circ$) enclosing one-eighth of the globe ($\frac{1}{8}\cdot 4\pi R^2 = \frac{\pi}{2}R^2$).

In 1629, the Dutch-French mathematician Albert Girard proved how the angle sum and area are locked together. Each pair of intersecting great circles forms two crescent-shaped *spherical lunes* of area $A_{\text{lune}} = 2R^2\theta_{\text{rad}}$. By overlaying the three lune pairs covering the three sides of a spherical triangle—which cover the entire sphere once while triple-covering the triangle itself and its antipodal twin—Girard proved that the *spherical excess* $E_{\text{rad}} = (\alpha + \beta + \gamma) - \pi$ is proportional to the triangle's area:

$$E_{\text{rad}} = (\alpha^\circ + \beta^\circ + \gamma^\circ - 180^\circ)\frac{\pi}{180^\circ}, \qquad A_{\text{triangle}} = R^2 E_{\text{rad}}$$

On a sphere, the physical area of a continent-sized survey network follows directly from three angles measured with a theodolite.

Just as the perimeter of a 2D ellipse has no elementary closed form, the surface area of a 3D *triaxial ellipsoid* with semi-axes $(a, b, c)$, the standard shape model for elongated asteroids such as Eros or Toutatis, requires incomplete elliptic integrals. In 2004, Danish mathematician Knud Thomsen showed that taking a power mean of the three projected semi-axis products $(ab, ac, bc)$ with exponent $p = 1.6075$ (reusing the exponent $p$ across all three `{{key:yˣ}}` terms via `{{key:LASTX}}` before inverting with `{{key:1/x}}`):

$$A \approx 4\pi \left(\frac{(ab)^p + (ac)^p + (bc)^p}{3}\right)^{1/p} \qquad (p = 1.6075)$$

approximates the exact elliptic surface integral to within $1.06\%$ across all aspect ratios.

### Shell Surface Area and Infill Volume in Additive Manufacturing

Surface area and enclosed volume govern mass estimation in Fused Deposition Modeling (FDM) additive manufacturing when slicing an engineering enclosure or structural bracket. Unlike a cast-iron or injection-molded part that is $100\%$ solid throughout, a 3D-printed part—like the hollow trabecular wing bones of an albatross or eagle—is a *composite sandwich structure* combining a dense outer skin with a porous core.

During fabrication, the print nozzle first traces $N_{\text{walls}}$ solid perimeter loops (typically $3$ loops at $w_{\text{line}} = 0.45\text{ mm}$ extrusion width, forming a solid outer skin of thickness $t_{\text{shell}} = 1.35\text{ mm}$) across the exterior boundary surface area $A_{\text{surface}}$ to establish a shell volume $V_{\text{shell}} \approx A_{\text{surface}} \cdot t_{\text{shell}}$. The enclosed interior volume $V_{\text{interior}} = V_{\text{total}} - V_{\text{shell}}$ is then filled not with solid polymer, but with a periodic minimal-surface *gyroid* or cubic lattice at $f_{\text{infill}} = 15\%\text{–}25\%$ relative density, contributing core polymer volume $V_{\text{core}} = V_{\text{interior}} \cdot f_{\text{infill}}$. Multiplying the combined shell and core polymer volumes by the filament density $\rho$ (such as $\rho \approx 1.24\text{ g/cm}^3 = 0.00124\text{ g/mm}^3$ for PLA or $1.27\text{ g/cm}^3$ for PETG) gives the mass of the finished part:

$$m_{\text{part}} = \rho \left( A_{\text{surface}} \cdot t_{\text{shell}} + V_{\text{interior}} \cdot f_{\text{infill}} \right)$$

For thin-walled instrument enclosures and structural brackets, over $70\%$ of the polymer mass resides in the outer perimeter skin ($A_{\text{surface}} \cdot t_{\text{shell}}$) rather than the sparse interior infill, so accurate mass estimation begins with a multi-face surface area takeoff via `{{key:Σ+}}` and `{{key:SUMS}}`.

---

## Navigating 3D Space: Euclidean Distance, Centroids & Rotational Inertia

Once the surface area and volume of a three-dimensional body are established, spatial analysis turns to Euclidean distance, center of mass, and rotational moment of inertia.

### The 3D Pythagorean Theorem, Unwrapped Helical Springs & Direction Cosines

On a flat sheet of paper, the distance between two points follows the 2D Pythagorean theorem $r = \sqrt{\Delta x^2 + \Delta y^2}$. Stepping out of the flat plane by rising an elevation $\Delta z$ perpendicular to the floor forms a second right triangle from the floor diagonal $r = \sqrt{\Delta x^2 + \Delta y^2}$ and the vertical rise $\Delta z$, whose hypotenuse is the straight-line *3D Euclidean distance*:

$$d = \sqrt{r^2 + \Delta z^2} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$

On the SC-32, you can evaluate this 3D distance either by summing the three squares (`{{key:x²}}`) or by chaining the polar key `{{key:▸θ,r}}` twice: loading $(\Delta z, \Delta y, \Delta x)$ onto Registers $(Z, Y, X)$ and pressing `{{key:▸θ,r}} {{key:x⇄y}} {{key:R↓}} {{key:▸θ,r}}` collapses $\sqrt{\Delta x^2 + \Delta y^2}$ into $r_{xy}$ on the first tap and combines $r_{xy}$ with $\Delta z$ into $d = \sqrt{r_{xy}^2 + \Delta z^2}$ on the second tap without squaring a single number. Between the two conversions, the first `▸θ,r` leaves the floor radius $r_{xy}$ in Register $X$ and the azimuth angle $\theta$ in Register $Y$ (with $\Delta z$ in Register $Z$), so `x⇄y R↓` rolls $\theta$ into Register $T$ and drops $(\Delta z, r_{xy})$ into Registers $(Y, X)$ for the second `▸θ,r` tap, which also leaves the elevation angle $\phi = \arctan(\Delta z / r_{xy})$ in Register $Y$.

That three-component Pythagorean sum also determines the straight wire blank length $L$ required to wind a *tapered conical compression spring* with bottom radius $R_1$, top radius $R_2$, axial height $h$, and $N$ active coils. Unrolling the conical helix resolves the wire path into three mutually perpendicular components: a circumferential wrap of $N$ full turns at the mean radius $R_m = \frac{1}{2}(R_1 + R_2)$ spanning horizontal distance $\Delta s_\theta = 2\pi N R_m$, an axial climb of vertical rise $\Delta z = h$, and a radial inward taper of spiral step $\Delta r = R_1 - R_2$. Because the circumferential, axial, and radial directions are mutually orthogonal at every point along the wire, the total wire length is their 3D Pythagorean norm:

$$L \approx \sqrt{(2\pi N R_m)^2 + h^2 + (R_1 - R_2)^2}$$

Similarly, when a deep-space radar or robotic gimbal tracks a target at 3D displacement vector $\vec{V} = (\Delta x, \Delta y, \Delta z)$ at total range $d = |\vec{V}| = \sqrt{\Delta x^2 + \Delta y^2 + \Delta z^2}$, dividing each coordinate by the range $d$ produces the three *direction cosines* $(\cos\alpha, \cos\beta, \cos\gamma) = \left(\frac{\Delta x}{d}, \frac{\Delta y}{d}, \frac{\Delta z}{d}\right)$. These direction cosines are the components of the 3D unit pointing vector $\hat{u} = \vec{V}/d$ and obey the 3D Pythagorean identity:

$$\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$$

### The Balance Point of a Composite Structure: Center of Mass

As Archimedes established in *On the Equilibrium of Planes*, the balance point of an asymmetric airplane wing, a welded I-beam girder, or a multi-stage rocket follows from static torque equilibrium. When a body is assembled from $N$ components with masses (or cross-sectional areas) $m_1, m_2, \dots, m_N$ centered at positions $x_1, x_2, \dots, x_N$, each piece exerts a gravitational torque (first moment) $m_k x_k$ about the origin. The composite *center of mass* (*centroid*) $\bar{x}_{\text{cm}}$ is the exact location where a single support fulcrum balances all those torques, defined as the *mass-weighted mean* of the coordinates:

$$\bar{x}_{\text{cm}} = \frac{m_1 x_1 + m_2 x_2 + \dots + m_N x_N}{m_1 + m_2 + \dots + m_N} = \frac{\sum_{k=1}^N m_k x_k}{\sum_{k=1}^N m_k}$$

The SC-32 models composite centroids through its statistical registers: when you place each component's mass (or area) $m_k$ in Register $Y$ and its coordinate $x_k$ in Register $X$, pressing `{{key:Σ+}}` automatically accumulates the torque sum $\sum m_k x_k$ into $\Sigma xy$ and the total mass $\sum m_k$ into $\Sigma y$. Opening the `{{key:x̄,ȳ}}` menu (`{{key:↱}}` + `{{key:yˣ}}`) and pressing the weighted-mean softkey `{{key:x̄w}}` then divides $\Sigma xy / \Sigma y$ in a single keystroke to return $\bar{x}_{\text{cm}}$.

### Rotational Moments of Inertia, Hollow Shafts & the Parallel-Axis Theorem

In linear motion, a $10\text{-kilogram}$ steel block requires the same force to accelerate whether it is shaped like a compact cannonball or a thin bicycle wheel. In *rotational motion*, however, shape and mass distribution determine the inertial resistance.

When a small mass $m$ orbits an axle at radial distance $r$ with angular velocity $\omega\text{ (rad/s)}$, its linear speed is $v = r\omega$, so its kinetic energy is:

$$K = \frac{1}{2} m v^2 = \frac{1}{2} m (r\omega)^2 = \frac{1}{2} \left(m r^2\right) \omega^2$$

Summing $m r^2$ over every particle in a rigid body defines its *rotational moment of inertia* $I = \int r^2\,dm$, so that rotational kinetic energy is $K_{\text{rot}} = \frac{1}{2} I \omega^2$ and angular momentum is $L = I \omega$. Because the radial distance $r$ is *squared* (`{{key:x²}}`), moving a kilogram of mass twice as far from the axis of rotation makes it *four times* harder to spin up or slow down.

That $r^2$ radial weighting governs conservation of angular momentum, flywheel shape factors, off-axis pivots, and hollow shaft stiffness. When a figure skater enters a spin with her arms and free leg extended outward, a large fraction of her mass sits at a substantial radius $r$ from her vertical spin axis, which produces a large moment of inertia $I_{\text{open}}$. Pulling her arms and leg tightly against her chest reduces $r$ by roughly a factor of two and cuts her moment of inertia $I_{\text{closed}} \propto r^2$ by a factor of three or four. Because the ice exerts negligible rotational friction torque, her angular momentum $L = I\omega$ is conserved, and reducing $I$ to one-third forces her spin rate $\omega$ to triple.

For symmetric bodies of total mass $M$ and outer radius $R$, the center-of-mass moment of inertia takes the canonical form $I_{\text{cm}} = k M R^2$, where the dimensionless shape factor $k$ reflects how close the mass lies to the outer boundary: $I_{\text{cm}} = M R^2$ ($k = 1$, all mass at radius $R$) for a thin cylindrical hoop or rim, $I_{\text{cm}} = \frac{1}{2} M (r_1^2 + r_2^2)$ for a thick annular ring of radii $r_1$ and $r_2$, $I_{\text{cm}} = \frac{1}{2} M R^2$ ($k = 0.50$) for a solid uniform cylinder or disk, $I_{\text{cm}} = \frac{2}{3} M R^2$ ($k \approx 0.67$) for a thin spherical shell, $I_{\text{cm}} = \frac{2}{5} M R^2$ ($k = 0.40$) for a solid uniform sphere, and $I_{\text{cm}} = \frac{1}{12} M L^2$ for a slender rod of length $L$ pivoted about its midpoint. Consequently, a mechanical punch-press flywheel concentrates nearly $80\%$ of its cast iron into a thick outer rim supported by a thin inner web so that almost $90\%$ of its mass acts at maximum $r^2$ radius.

When a robotic arm link or pendulum pivots about a shoulder joint displaced by a perpendicular distance $d$ from its centroid rather than about its center of mass, Swiss geometer Jakob Steiner proved that one need not re-integrate $\int r^2\,dm$ from scratch. Because the cross-terms in $(r_{\text{cm}} + d)^2 = r_{\text{cm}}^2 + 2 d\,r_{\text{cm}} + d^2$ integrate to zero around the center of mass ($\int r_{\text{cm}}\,dm = 0$), Jakob Steiner's *Parallel-Axis Theorem* states that the moment of inertia about *any* parallel axis at distance $d$ equals the centroidal inertia plus the inertia of treating the entire body as a point mass at distance $d$:

$$I_{\text{parallel}} = I_{\text{cm}} + M d^2$$

For a slender robotic arm link of mass $m$ and length $L$, shifting the pivot from its midpoint ($I_{\text{cm}} = \frac{1}{12}mL^2$) to its shoulder joint at one end ($d = L/2$) adds $m(L/2)^2 = \frac{1}{4}mL^2 = 3 I_{\text{cm}}$, which quadruples the rotational inertia to $I_{\text{pivot}} = \frac{1}{12}mL^2 + \frac{3}{12}mL^2 = \frac{1}{3}mL^2$.

When a solid steel shaft of radius $R$ twists under engine torque, the metal along the central axis barely displaces ($r \approx 0$), so it carries negligible shear stress while adding dead weight. Because a circular cross-section's area grows as $dA = 2\pi r\,dr$, integrating $r^2\,dA$ from an inner bore radius $R_i$ to an outer skin radius $R_o$ shows that the polar moment of inertia $J$ (which governs torsional stiffness, evaluated via `4 {{key:yˣ}}`) scales with the fourth power of the radius:

$$J = \int_{R_i}^{R_o} r^2 (2\pi r\,dr) = \frac{\pi}{2}\left(R_o^4 - R_i^4\right)$$

Because mass scales with cross-sectional area $(R_o^2 - R_i^2)$ while polar stiffness scales with $(R_o^4 - R_i^4) = (R_o^2 - R_i^2)(R_o^2 + R_i^2)$, boring out the central core where $r$ is small removes dead weight while sacrificing very little torsional rigidity. For a hollow spherical pressure hull (such as a deep-ocean titanium bathysphere bounded by inner radius $R_1$ and outer radius $R_2$), subtracting the inner sphere from the outer sphere scales with the fifth power of radius (`5 {{key:yˣ}}`):

$$I_{\text{shell}} = \frac{2}{5} M \left(\frac{R_2^5 - R_1^5}{R_2^3 - R_1^3}\right)$$

---

## Solid Mensuration, Weighted Centroids & Moments of Inertia

Evaluating planar, volumetric, and inertial formulas on the four-register stack separates into two operational patterns depending on whether the geometry is a single closed-form solid or a multi-part assembly.

For a single geometric primitive—such as the annular pipe flange, the silver-ratio octagon, Heron's triangle via `{{key:STO}} S`, the Moscow Papyrus frustum polynomial $R^2 + Rr + r^2$ via `{{key:LASTX}}`, or the hollow drive shaft's fourth-power polar inertia $J = \frac{\pi}{2}(R_o^4 - R_i^4)$—factoring common multipliers ($\pi$, $\frac{1}{3}\pi h$, or $\frac{3\sqrt{3}}{2}$) to the outside allows the inner dimensional core to accumulate inside Register $X$; Register $Y$ combines terms transiently while Registers $Z$ and $T$ remain untouched.

When auditing a composite structure assembled from multiple boundary facets or sub-masses, clearing the statistical registers with `{{key:CLΣ}}` (`{{key:↰}}` + `{{key:Σ+}}`) couples the live stack to the six statistical accumulators. Evaluating each face group in Register $X$ and pressing `{{key:Σ+}}` (or `{{key:Σ-}}` for drilled cutouts) increments the item counter $n$ in Register $X$ and sums the net area or volume in $\Sigma x$ (`{{key:SUMS}}` $\to$ `{{key:Σx}}`), whereas staging each sub-mass $m_k$ in Register $Y$ and its coordinate $y_k$ in Register $X$ before `{{key:Σ+}}` prepares the first-moment ratio $\bar{y} = \Sigma xy / \Sigma y$ for `{{key:x̄,ȳ}}` $\to$ `{{key:x̄w}}`.

{{res:sc32_surface_area_sigma:screenshot|Surface area of 10x5x4 prism accumulated via Sigma+ → 220}}

### 2D Flanges, Silver-Ratio Octagons, Planetary Oblateness & Heron's Triangle

| Geometric Region | Analytical Area Formula | Factored / Auxiliary Relation | Geometric Origin & Physical Meaning |
| :--- | :--- | :--- | :--- |
| **Rectangle** | $A = l \times w$ | $P = 2(l + w)$ | Cartesian product of orthogonal basis lengths. |
| **Triangle (Base/Height)** | $A = \frac{1}{2} b \times h$ | $A = \frac{1}{2}ab\sin C$ | Exactly half of the circumscribing parallelogram. |
| **Circle** | $A = \pi r^2$ | $C = 2\pi r = \frac{dA}{dr}$ | Integration of concentric thin rings ($dA = 2\pi r\,dr$). |
| **Circular Sector** | $A = \frac{1}{2} r^2 \theta$ ($\theta$ in rad) | $s = r\theta$ | Fractional angular wedge $(\theta / 2\pi)$ of full disk $\pi r^2$. |
| **Circular Segment** | $A = \frac{1}{2} r^2 (\theta - \sin\theta)$ | $c = 2r\sin(\theta/2)$ | Circular sector minus the isosceles chord triangle $\frac{1}{2}r^2\sin\theta$. |
| **Circular Annulus (Ring)** | $A = \pi (R^2 - r^2)$ | $A = \pi(R - r)(R + r)$ | Difference of concentric disks; mean circumference $2\pi\frac{R+r}{2}$ times wall thickness $(R-r)$. |
| **Trapezoid** | $A = \frac{1}{2} (a + b) h$ | $m = \frac{a + b}{2}$ | Average of parallel base lengths multiplied by perpendicular altitude $h$. |
| **Ellipse** | $A = \pi a b$ | $e = \sqrt{1 - (b/a)^2}$ | Circle of radius $b$ stretched along one axis by affine ratio $a/b$. |
| **Parabolic Segment** | $A = \frac{2}{3} b h$ | $A = \frac{4}{3} A_{\text{triangle}}$ | Archimedes' exhaustion proof: $\frac{2}{3}$ of circumscribing box $bh$. |
| **Regular $n$-gon** | $A = \frac{1}{4} n s^2 \cot(\pi/n)$ | $A = \frac{1}{2} P \cdot r_{\text{in}}$ | Sum of $n$ congruent isosceles triangles radiating from the center. |
| **Cyclic Quadrilateral** | $A = \sqrt{(s-a)(s-b)(s-c)(s-d)}$ | $s = \frac{a+b+c+d}{2}$ | Brahmagupta's 628 CE theorem for any four-sided figure inscribed in a circle. |

Applying this inside-out ordering to planar ring, polygon, and geodetic sections keeps every intermediate result within Registers $Y$ and $X$:

* **Bolted ASME B16.5 Neoprene Pipe Flange Gasket ($A = \pi(R^2 - r^2)$):** On a high-pressure flange gasket with outer radius $R = 85.0\text{ mm}$ and inner bore radius $r = 50.0\text{ mm}$, deferring the $\pi$ multiplier avoids scaling both radii separately: square $R^2 = 7,225.0\text{ mm}^2$ in Register $X$, square $r^2 = 2,500.0\text{ mm}^2$ (which lifts $R^2$ into Register $Y$), subtract to collapse the net radial span $4,725.0\text{ mm}^2$ back into Register $X$, and multiply by `{{key:π}}` last (`{{res:sc32_06_geometry_surface_area_seq_01:keys}}` $\longrightarrow$ `{{res:sc32_06_geometry_surface_area_seq_01:value}}`, or $\mathbf{14,844.03\text{ mm}^2} = 148.44\text{ cm}^2$; on thin-walled aerospace shells where $R \approx r$, forming $(R - r)$ in $Y$ and $(R + r)$ in $X$ before multiplying by $\pi$ preserves full guard-digit precision).
* **Regular Octagonal Instrument Bezel ($A = 2(1 + \sqrt{2})s^2$):** For an octagonal cover of side length $s = 65.0\text{ mm}$ ($A = 2\delta_S s^2$), construct twice the silver ratio $2(1 + \sqrt{2}) \approx 4.828427$ in Register $X$ first, then square the side length $65^2 = 4,225.0\text{ mm}^2$ via `{{key:x²}}` (lifting $2\delta_S$ into Register $Y$) and multiply via `{{res:sc32_06_geometry_surface_area_seq_02:keys}}` $\longrightarrow$ `{{res:sc32_06_geometry_surface_area_seq_02:value}}` ($\mathbf{20,400.10\text{ mm}^2}$).
* **Earth's Geodetic Reciprocal Flattening ($1/f = a/(a - b)$):** For the 3-decimal WGS-84 semi-axes $a = 6,378.137\text{ km}$ and $b = 6,356.752\text{ km}$ ($6,356.7523142\text{ km}$ at full geodetic precision, where $1/f = \mathbf{298.257223563}$), subtracting $b$ from $a$ across $(Y, X)$ isolates the equatorial bulge $(a - b) = 21.385\text{ km}$ in Register $X$, dividing by $a = 6,378.137\text{ km}$ forms $f \approx 0.00335286$, and inverting with `{{key:1/x}}` (or evaluating $f = 1 - b/a$ in a single entry per axis) via `{{res:sc32_06_geometry_surface_area_seq_19:keys}}` returns $\mathbf{298.2528}$.

Heron's semiperimeter formula $A = \sqrt{s(s-a)(s-b)(s-c)}$, which on paper appears to need four registers for $s, (s-a), (s-b),$ and $(s-c)$ simultaneously, likewise runs as a Register-$X$ accumulator once the semiperimeter $s = (a+b+c)/2$ is stored in Variable `S` (`{{key:STO}} S`). On a $13\text{–}14\text{–}15\text{ cm}$ machinist's layout triangle, storing $s = 21.0\text{ cm}$ in `S` lets you form $(21 - 13) = 8$, $(21 - 14) = 7$, and $(21 - 15) = 6\text{ cm}$ sequentially in Register $X$, multiply them into $336\text{ cm}^3$, and scale by $s = 21\text{ cm}$ to reach $7,056\text{ cm}^4$ before `{{key:√x}}` extracts $A = 84.0\text{ cm}^2$. On a surveyed triangular parcel with boundary lengths $a = 7.0\text{ m}$, $b = 9.0\text{ m}$, and $c = 12.0\text{ m}$, the stack sequence proceeds in three stages:

1. **Compute and store the semiperimeter $s$:** Sum the three boundary lengths and halve them to place $s = (7 + 9 + 12)/2 = 14.0000\text{ m}$ in Register $X$, then save $s$ in Variable `S` while keeping $14.0000$ live on the stack via `{{res:sc32_06_geometry_surface_area_seq_21:keys}}` {{key:STO}} S $\longrightarrow$ $\mathbf{14.0000\text{ m}}$.
2. **Multiply the three $(s - \text{side})$ excess factors in place:** Subtract the first side via `7 {{key:-}}` ($\to 7.0000\text{ m}$), recall `S` and form the second factor via `{{key:RCL}} S 9 {{key:-}} {{key:×}}` ($\to 35.0000\text{ m}^2$), and form the third factor via `{{key:RCL}} S 12 {{key:-}} {{key:×}}` to accumulate $(s-a)(s-b)(s-c) = 7 \times 5 \times 2 = \mathbf{70.0000\text{ m}^3}$ in Register $X$.
3. **Scale by $s$, extract the root, and find the incircle radius:** Keying `{{key:RCL}} S {{key:×}} {{key:√x}}` multiplies $70.0000 \times 14.0000 = 980.0000\text{ m}^4$ and extracts the parcel area $A = \sqrt{980} = 14\sqrt{5} = \mathbf{31.304952\text{ m}^2}$; dividing immediately by `{{key:RCL}} S {{key:÷}}` yields the inscribed circle radius $r = A/s = \mathbf{2.236068\text{ m}}$ ($\sqrt{5}\text{ m}$).

For the right-angled structural channel with orthogonal legs $a = 15.0\text{ cm}$ and $b = 20.0\text{ cm}$, evaluating the linear tangent relation $r = \frac{a + b - c}{2}$ on $(Y, X)$ begins by converting $(15, 20)$ to polar form via `15 {{key:ENTER}} 20 {{key:▸θ,r}}` to place the hypotenuse $c = 25.0000\text{ cm}$ in Register $X$; forming the leg sum $a + b = 35.0000\text{ cm}$ via `15 {{key:ENTER}} 20 {{key:+}}` lifts $c$ into Register $Y$, and `{{key:x⇄y}} {{key:-}} 2 {{key:÷}}` returns the cooling-pipe inradius $r = \mathbf{5.0000\text{ cm}}$.

---

### Accumulating Composite Surface Areas via Σ+

When stepping from a single planar face to a three-dimensional enclosure or finned casting bounded by many polygon groups, the statistical accumulator `{{key:Σ+}}` replaces manual scratchpad variables with a running ledger:

1. Press `{{key:CLΣ}}` (`{{key:↰}}` + `{{key:Σ+}}`) to zero all six statistical registers ($\Sigma x = 0,\; n = 0$).
2. Evaluate the area $A_1$ of the first face (or symmetric opposing face pair) in Register $X$ and press `{{key:Σ+}}`, which adds $A_1$ into $\Sigma x$ and replaces Register $X$ with the integer face-group counter $n = 1.0$.
3. To deduct a milled window aperture, cooling bore, or mistyped entry, evaluate its area in Register $X$ and press `{{key:Σ-}}`.
4. Press `{{key:SUMS}}` (Right Shift `{{key:↱}}` above `{{key:Σ+}}`) and tap softkey `{{key:Σx}}` (`{{key:LFU0}}`) to recall the net surface area $\Sigma x$ into Register $X$.

Applying this ledger to the StackCalc SC-32 rectangular chassis ($L = 135\text{ mm}$, $W = 70\text{ mm}$, $H = 16\text{ mm}$) for an additive-manufacturing shell takeoff, the six exterior walls group into three opposing pairs ($2 \times 135 \times 70 = 18,900\text{ mm}^2$, $2 \times 135 \times 16 = 4,320\text{ mm}^2$, and $2 \times 70 \times 16 = 2,240\text{ mm}^2$). After `{{key:CLΣ}}`, each pair is evaluated on $(Y, X)$ and committed to $\Sigma x$:

| Keystroke | Register T | Register Z | Register Y | Register X | Accumulator $\Sigma x$ | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `135 {{key:ENTER}} 70 {{key:×}} 2 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $18900.0$ | $0.0$ | Top/Bottom area pair evaluated ($18,900.0\text{ mm}^2$) |
| `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$1.0$** | **$18900.0$** | $n=1$ in Register $X$; first pair accumulated into $\Sigma x$ |
| `135 {{key:ENTER}} 16 {{key:×}} 2 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $4320.0$ | $18900.0$ | Side walls area pair evaluated ($4,320.0\text{ mm}^2$) |
| `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$2.0$** | **$23220.0$** | $n=2$ in Register $X$; running area accumulated into $\Sigma x$ |
| `70 {{key:ENTER}} 16 {{key:×}} 2 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $2240.0$ | $23220.0$ | End caps area pair evaluated ($2,240.0\text{ mm}^2$) |
| `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$3.0$** | **$25460.0$** | $n=3$ in Register $X$; all 6 faces accumulated into $\Sigma x$ |
| `{{key:SUMS}} → Σx` | $0.0$ | $0.0$ | $0.0$ | **$25460.0000$** | $25460.0$ | Tap `{{key:Σx}}` (`{{key:LFU0}}`): total surface area recalled ($25,460.0\text{ mm}^2$) |

The same `{{key:Σ+}}` accumulation tallies curved solids. For a cylindrical lithium battery compartment of radius $r = 15\text{ mm}$ and height $h = 65\text{ mm}$, we sum the two circular end caps ($2\pi r^2 = 450\pi \approx 1,413.7167\text{ mm}^2$) and the unrolled lateral wall ($2\pi r h = 1,950\pi \approx 6,126.1057\text{ mm}^2$):

| Keystroke | Register T | Register Z | Register Y | Register X | Accumulator $\Sigma x$ | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `15 {{key:x²}} {{key:π}} {{key:×}} 2 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $1413.716694$ | $0.0$ | Two circular end caps $2\pi r^2$ evaluated in $\text{mm}^2$ |
| `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$1.0$** | **$1413.716694$** | Accumulate end caps into $\Sigma x$; face-group count $n=1$ in $X$ |
| `2 {{key:π}} {{key:×}} 15 {{key:×}} 65 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $6126.105675$ | $1413.716694$ | Cylindrical lateral wall $2\pi r h$ evaluated in $\text{mm}^2$ |
| `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$2.0$** | **$7539.822369$** | Accumulate lateral wall into $\Sigma x$; face-group count $n=2$ in $X$ |
| `{{key:SUMS}} → Σx` | $0.0$ | $0.0$ | $0.0$ | **$7539.822369$** | $7539.822369$ | Tap `{{key:Σx}}` (`{{key:LFU0}}`): total cylinder surface area recalled ($7,539.82\text{ mm}^2$) |

Because `{{key:Σ+}}` increments the face counter $n$ in Register $X$ while building the running total inside $\Sigma x$, complex multi-step castings and thermal radiators can be audited by stepping around the blueprint and feeding each face group into `{{key:Σ+}}`:

* **Stepped Cast-Iron Machine Bracket ($n = 6$ face groups):** When a base block ($120 \times 80 \times 30\text{ mm}$) is surmounted by a centered boss ($60 \times 40 \times 25\text{ mm}$), subtracting the $60 \times 40\text{ mm}$ boss footprint from the base roof and adding the boss roof back is redundant: viewed from above, the boss roof plus the surrounding ledge form one uninterrupted $120 \times 80 = 9,600.0\text{ mm}^2$ top projection. After `{{key:CLΣ}}`, feed each group into `{{key:Σ+}}`: bottom base ($120 \times 80 = 9,600\text{ mm}^2,\; n=1$), long base walls ($2 \times 120 \times 30 = 7,200\text{ mm}^2,\; n=2$), short base ends ($2 \times 80 \times 30 = 4,800\text{ mm}^2,\; n=3$), long boss walls ($2 \times 60 \times 25 = 3,000\text{ mm}^2,\; n=4$), short boss ends ($2 \times 40 \times 25 = 2,000\text{ mm}^2,\; n=5$), and top projection ($120 \times 80 = 9,600\text{ mm}^2,\; n=6$). Pressing `{{key:SUMS}}` and `{{key:Σx}}` recalls $\Sigma x = \mathbf{36,200.0000\text{ mm}^2}$.
* **8-Fin Extruded Aluminum CPU Heat Sink ($n = 4$ face groups):** A $100 \times 100\text{ mm}$ square aluminum base plate has only $2 \times 10,000 = 20,000\text{ mm}^2$ of top-and-bottom area, whereas extruding $8$ vertical cooling fins ($100\text{ mm}$ long, $35\text{ mm}$ tall, $2\text{ mm}$ thick) out of its upper surface folds four convective face groups into the same footprint. After `{{key:CLΣ}}`, accumulate each group with `{{key:Σ+}}`: the $16$ fin sidewalls ($16 \times 100 \times 35 = 56,000.0\text{ mm}^2,\; n=1$), the $8$ fin top tips ($8 \times 100 \times 2 = 1,600.0\text{ mm}^2,\; n=2$), the valley floor between fins ($100 \times 100 - 1,600 = 8,400.0\text{ mm}^2,\; n=3$), and the bottom mounting plate ($100 \times 100 = 10,000.0\text{ mm}^2,\; n=4$). Recalling `{{key:SUMS}}` $\to$ `{{key:Σx}}` yields $\Sigma x = \mathbf{76,000.0000\text{ mm}^2}$, a $\mathbf{3.8\times}$ ($380\%$) cooling-area gain.
* **Pyramidal Frustum Pavilion Roof:** When a park pavilion is capped by a four-sided hipped pyramidal frustum roof with a $12\text{ m}$ square eaves perimeter, a $4\text{ m}$ square skylight curb at the top, and an inclined slant height of $s = 6.5\text{ m}$, each sloping roof plane is a trapezoid of average width $\frac{1}{2}(12 + 4) = 8.0\text{ m}$ and area $A_{\text{face}} = 8.0 \times 6.5 = 52.0000\text{ m}^2$. After `{{key:CLΣ}}`, multiplying the single-slope trapezoidal area $\frac{12 + 4}{2} \times 6.5 = 52.0\text{ m}^2$ by $4$ in Register $X$ and tapping `{{key:Σ+}}` logs all four identical roof slopes at once: $\Sigma x = \mathbf{208.0000\text{ m}^2}$ ($n = 1$).
* **Galileo's Square Pyramid Surface-to-Volume Ratio ($A/V$):** On a regular right square pyramid of base side $s = 12.0\text{ mm}$ and altitude $h = 8.0\text{ mm}$, the right triangle formed by $h = 8.0\text{ mm}$ and base apothem $s/2 = 6.0\text{ mm}$ has a $6\text{–}8\text{–}10$ slant height of $l = \sqrt{8^2 + 6^2} = 10.0000\text{ mm}$. Multiplying $l = 10.0\text{ mm}$ by the four half-bases $4 \times \frac{1}{2}s = 24.0\text{ mm}$ yields lateral area $A_{\text{lat}} = 240.0000\text{ mm}^2$, and adding the square base $12^2 = 144.0\text{ mm}^2$ via `{{key:x²}}` and `{{key:+}}` gives total surface area $A = 384.0000\text{ mm}^2$ in Register $X$. Evaluating the volume $V = \frac{1}{3}s^2 h = \frac{1}{3}(144)(8) = 384.0000\text{ mm}^3$ lifts $A$ into Register $Y$ while $V$ lands in Register $X$, so pressing `{{key:÷}}` confirms $A/V = \mathbf{1.0000\text{ mm}^{-1}}$ (matching $V = \frac{1}{3} r_{\text{in}} A$ for inradius $r_{\text{in}} = 3.0\text{ mm}$).

---

### 3D Volumes, Conical Frustums, Spherical Caps & Girard's Excess

| 3D Solid Geometry | Analytical Volume Formula | Total External Surface Area Formula | Geometric Origin & Physical Meaning |
| :--- | :--- | :--- | :--- |
| **Rectangular Prism** | $V = l \cdot w \cdot h$ | $A = 2(lw + lh + wh)$ | Extrusion of rectangle $lw$ along $h$; 6 orthogonal faces. |
| **Right Circular Cylinder** | $V = \pi r^2 h$ | $A = 2\pi r^2 + 2\pi r h$ | Extrusion of circular disk $\pi r^2$ along normal axis $h$. |
| **Right Circular Cone** | $V = \frac{1}{3} \pi r^2 h$ | $A = \pi r^2 + \pi r \sqrt{r^2 + h^2}$ | Exactly $\frac{1}{3}$ of bounding cylinder (Eudoxus & Archimedes). |
| **Sphere** | $V = \frac{4}{3} \pi r^3$ | $A = 4\pi r^2 = \frac{dV}{dr}$ | Exactly $\frac{2}{3}$ of circumscribing cylinder in both $V$ and $A$. |
| **Torus (Major $R$, minor $r$)** | $V = 2\pi^2 R r^2$ | $A = 4\pi^2 R r$ | Pappus-Guldinus: Centroid orbit ($2\pi R$) $\times$ disk area ($\pi r^2$) or circumference ($2\pi r$). |
| **Frustum of Right Cone** | $V = \frac{1}{3} \pi h (R^2 + Rr + r^2)$ | $A = \pi(R^2 + r^2) + \pi(R + r)s$ | Height $h$ times average of top area, bottom area, and geometric mean $\pi Rr$. |
| **Spherical Cap (depth $h$)** | $V = \frac{1}{3} \pi h^2 (3R - h)$ | $A_{\text{dome}} = 2\pi R h$ | Horizontal slice of sphere; curved dome area equals wall area of cylinder of height $h$. |
| **Spherical Zone (2 planes)** | $V = \frac{\pi h}{6}(3r_1^2 + 3r_2^2 + h^2)$ | $A_{\text{zone}} = 2\pi R h$ | Slice between two parallel cutting planes through a sphere. |
| **Triaxial Ellipsoid** | $V = \frac{4}{3} \pi a b c$ | $A \approx 4\pi \left(\frac{(ab)^p + (ac)^p + (bc)^p}{3}\right)^{1/p}$ | 3D affine stretch of unit sphere along semi-axes $a, b, c$ ($p \approx 1.6075$). |
| **Paraboloid of Revolution** | $V = \frac{1}{2} \pi r^2 h$ | $A = \frac{\pi r}{6h^2} \left[(r^2 + 4h^2)^{3/2} - r^3\right]$ | Exactly $\frac{1}{2}$ of its bounding cylinder (Archimedes' *On Conoids and Spheroids*). |
| **Steinmetz Bicylinder** | $V = \frac{16}{3} r^3$ | $A = 16 r^2$ | Orthogonal intersection of two equal cylinders of radius $r$; $\pi$ cancels completely. |
| **Universal Prismoid** | $V = \frac{h}{6}(A_{\text{top}} + 4A_{\text{mid}} + A_{\text{bot}})$ | Sum of boundary faces | Exact for any solid whose cross-sectional area $A(z)$ is up to a cubic polynomial in $z$. |
| **Regular Tetrahedron** | $V = \frac{\sqrt{2}}{12} a^3$ | $A = \sqrt{3} a^2$ | 4 equilateral triangular faces; inscribed inside a cube of edge $a/\sqrt{2}$. |
| **Regular Octahedron** | $V = \frac{\sqrt{2}}{3} a^3$ | $A = 2\sqrt{3} a^2$ | 8 equilateral triangular faces; two square pyramids joined base-to-base. |
| **Regular Dodecahedron** | $V = \frac{15 + 7\sqrt{5}}{4} a^3$ | $A = 3\sqrt{25 + 10\sqrt{5}}\,a^2$ | 12 regular pentagonal faces governed by the golden ratio $\phi = \frac{1+\sqrt{5}}{2}$. |
| **Regular Icosahedron** | $V = \frac{5(3 + \sqrt{5})}{12} a^3$ | $A = 5\sqrt{3} a^2$ | 20 equilateral triangular faces; dual polyhedron of the dodecahedron. |

Each single-solid volume and curved-shell formula from Cavalieri's principle unfolds as a one-dimensional sequence inside Register $X$ (using Register $Y$ only transiently as terms combine), without populating Registers $Z$ or $T$:

* **Aerodynamic Elliptic Nose Cone vs. the $\pi$-Free Steinmetz Bicylinder:** For an aerodynamic elliptic nose cone of semi-axes $a = 24.0\text{ mm}$ and $b = 15.0\text{ mm}$ and axial length $h = 50.0\text{ mm}$, Cavalieri's one-third cone factor ($V = \frac{1}{3}\pi abh = 6,000\pi\text{ mm}^3$) evaluates by forming the bounding box product $a \cdot b \cdot h = 18,000.0000\text{ mm}^3$ in Register $X$ and scaling by $\pi / 3$ via `{{key:π}}` to return $\mathbf{18,849.555922\text{ mm}^3}$. On the Steinmetz bicylinder (*Mouhefanggai*) where two equal circular pipes of radius $r = 15.0\text{ mm}$ intersect at right angles, the $\frac{4}{\pi}$ slice ratio already canceled $\pi$, so evaluating $V = \frac{16}{3}r^3 = \frac{16}{3}(3,375)$ via `{{key:yˣ}}` delivers the rational volume $\mathbf{18,000.0\text{ mm}^3}$, while $A = 16r^2 = 16(225)$ via `{{key:x²}}` gives the curved intersection surface area $\mathbf{3,600.0\text{ mm}^2}$.
* **Egyptian Conical Frustum Grain Hopper via `{{key:LASTX}}`:** Applying the Moscow Papyrus frustum polynomial $R^2 + Rr + r^2$ to a grain hopper of bottom radius $R = 1.80\text{ m}$, top throat radius $r = 0.40\text{ m}$, and height $h = 2.50\text{ m}$, squaring $R^2 = 3.24\text{ m}^2$ in Register $X$ saves $1.8$ in `{{key:LASTX}}` to form the geometric-mean cross-product $Rr = 0.72\text{ m}^2$, which in turn saves $0.4$ in `{{key:LASTX}}` to square $r^2 = 0.16\text{ m}^2$. This sequence sums all three terms into $R^2 + Rr + r^2 = 4.1200\text{ m}^2$ while typing `1.8` and `0.4` only once each, before scaling by $\frac{2.5\pi}{3}$ via `{{res:sc32_06_geometry_surface_area_seq_04:keys}}` $\longrightarrow$ `{{res:sc32_06_geometry_surface_area_seq_04:value}}` ($\mathbf{10.7861\text{ m}^3}$).
* **Hollow Hexagonal Brass Bar Stock:** On prismatic machine stock, a hollow hexagonal brass bar ($S = 20.0\text{ mm}$ outer flat-to-corner side, $s = 8.0\text{ mm}$ inner hexagonal bore side, and length $L = 150.0\text{ mm}$) pairs the difference of squares $(S^2 - s^2)$ with the six-equilateral-triangle hexagon constant $C_6 = \frac{3\sqrt{3}}{2} \approx 2.598076$. Subtracting $20^2 - 8^2 = 336.0000\text{ mm}^2$ in Register $X$, scaling by $\frac{3\sqrt{3}}{2}$ into $A_{\text{net}} = 872.953607\text{ mm}^2$, and extruding along $L = 150\text{ mm}$ via `{{res:sc32_06_geometry_surface_area_seq_20:keys}}` yields $\mathbf{130,943.0411\text{ mm}^3}$ ($130.94\text{ cm}^3$; similarly, for a solid steel hex bolt head of side $s = 10.0\text{ mm}$, height $h = 12.0\text{ mm}$, and density $\rho = 7.85\text{ g/cm}^3$, chaining `{{key:√x}} {{key:LASTX}} {{key:×}}` forms $3\sqrt{3}$ without re-typing `3` and yields a mass of $\mathbf{24.4739\text{ grams}}$).
* **Inscribed Regular Tetrahedron:** For a regular tetrahedron of edge length $a = 50.0\text{ mm}$ inscribed inside a cube of edge $a/\sqrt{2}$, multiplying the corner-sliced packing factor $\frac{\sqrt{2}}{12} \approx 0.117851$ by $a^3 = 125,000\text{ mm}^3$ evaluates in five steps via `{{res:sc32_06_geometry_surface_area_seq_11:keys}}` $\longrightarrow$ `{{res:sc32_06_geometry_surface_area_seq_11:value}}` ($\mathbf{14,731.39\text{ mm}^3}$).
* **Spherical Lune Canopy Gores & Albert Girard's Geodetic Excess:** On curved spherical shells, a parachute spherical lune gore panel on a hemispherical canopy of radius $R = 25.0\text{ cm}$ spanning dihedral wedge angle $\theta = 36.0^\circ$ covers $\frac{36^\circ}{360^\circ} = 0.1000$ of the full sphere area $4\pi R^2 = 7,853.981634\text{ cm}^2$, giving $A_{\text{lune}} = \mathbf{785.398163\text{ cm}^2}$. Across a geodetic triangulation network on the curved Earth ($R = 6,371.0\text{ km}$) with measured interior angles $\alpha = 82.5^\circ$, $\beta = 68.2^\circ$, and $\gamma = 44.7^\circ$, summing the three theodolite angles to $195.4000^\circ$ and subtracting $180^\circ$ isolates Girard's spherical excess $E = 15.4000^\circ$ in Register $X$, which converts via $\times \pi / 180$ into $E_{\text{rad}} \approx 0.268781\text{ rad}$ ($2.139\%$ of the globe) and scales by $R^2 = 6,371^2 = 40,589,641\text{ km}^2$ to give $A = R^2 E_{\text{rad}} = \mathbf{10,909,712.33\text{ km}^2}$.
* **Knud Thomsen's Triaxial Asteroid & Hortonsphere Spherical Caps:** Applying Thomsen's power mean ($p = 1.6075$) to a triaxial asteroid with semi-axes $a = 15.0\text{ km}, b = 10.0\text{ km}, c = 6.0\text{ km}$ ($ab = 150, ac = 90, bc = 60$), raising $150^{1.6075}$ with `{{key:yˣ}}` and recalling $p$ from `{{key:LASTX}}` for $90^p$ and $60^p$ averages the three terms on $(Y, X)$, raises that mean to $1/p$ via `{{key:1/x}} {{key:yˣ}}`, and multiplies by $4\pi$ to yield $\mathbf{1,308.90\text{ km}^2}$. For a Hortonsphere tank of radius $R = 4.0\text{ m}$ filled to depth $h = 1.5\text{ m}$, evaluating $V_{\text{cap}} = \frac{1}{3}\pi h^2(3R - h)$ forms $(3R - h) = 10.5\text{ m}$ in Register $X$, recalls $h = 1.5\text{ m}$ from `{{key:LASTX}}` to form $h^2(3R - h) = 23.625\text{ m}^3$, and scales by $\pi / 3$ via `{{res:sc32_06_geometry_surface_area_seq_07:keys}}` $\longrightarrow$ `{{res:sc32_06_geometry_surface_area_seq_07:value}}` ($\mathbf{24.7400\text{ m}^3}$).

---

### 3D Helical Coils, Direction Cosines, Weighted Centroids & Moments of Inertia

In three-dimensional kinematics and structural mechanics, the stack alternates between single-register Pythagorean reductions and four-register composite audits.

For a tapered conical compression spring with base radius $R_1 = 30\text{ mm}$, top radius $R_2 = 10\text{ mm}$ (mean radius $R_m = 20\text{ mm}$), axial height $h = 60\text{ mm}$, and $N = 6\text{ active coils}$, the three orthogonal displacement squares accumulate sequentially in Register $X$ via $L = \sqrt{(2\pi N R_m)^2 + h^2 + (R_1 - R_2)^2}$. Squaring the circumferential wrap $(2\pi N R_m)^2 = (753.9822\text{ mm})^2 = 568,489.2130\text{ mm}^2$ via `{{key:x²}}` in Register $X$, adding the squared axial climb $h^2 = 60^2 = 3,600.0000\text{ mm}^2$ ($\to 572,089.2130\text{ mm}^2$), and adding the squared radial inward taper $(R_1 - R_2)^2 = 20^2 = 400.0000\text{ mm}^2$ ($\to 572,489.2130\text{ mm}^2$) before pressing `{{key:√x}}` yields a developed wire blank of $\mathbf{756.6302\text{ mm}}$—showing that the axial climb and radial taper add $2.65\text{ mm}$ to the flat $753.98\text{ mm}$ circumferential wrap.

Similarly, when a deep-space radar tracks an ascending launch vehicle at 3D displacement vector $\vec{V} = (850, 1100, 550)\text{ m}$, computing the 3D Euclidean range $D = |\vec{V}| = 1,494.9916\text{ m}$, storing it in Variable `D`, and dividing each Cartesian component in turn places all three direction cosines $(\cos\alpha, \cos\beta, \cos\gamma)$ simultaneously across Registers $(Z, Y, X)$ via `{{res:sc32_06_geometry_surface_area_seq_13:keys}}` $\longrightarrow$ $(Z = 0.568565,\; Y = 0.735790,\; X = $ `{{res:sc32_06_geometry_surface_area_seq_13:value}}` $)$.

Locating the composite neutral axis $\bar{y} = \frac{\sum m_i y_i}{\sum m_i}$ of an asymmetric welded steel girder built from three horizontal plates—a bottom flange of $m_1 = 40\text{ kg}$ centered at height $y_1 = 10\text{ mm}$, a vertical web of $m_2 = 60\text{ kg}$ at $y_2 = 160\text{ mm}$, and a top flange of $m_3 = 30\text{ kg}$ at $y_3 = 310\text{ mm}$—engages all four stack registers alongside the statistical accumulators. After `{{key:CLΣ}}`, loading each plate's mass $m_i$ into Register $Y$ and its centroid height $y_i$ into Register $X$ before pressing `{{key:Σ+}}` lifts the previous plate masses into Registers $Z$ and $T$ while Register $X$ counts $n = 1, 2, 3$, and opening `{{key:x̄,ȳ}}` (`{{key:↱}}` + `{{key:yˣ}}`) to tap `{{key:x̄w}}` divides $\Sigma xy / \Sigma y$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0.0$ | $0.0$ | $0.0$ | $0.0$ | Clear all 6 statistical accumulators |
| `40 {{key:ENTER}} 10 {{key:Σ+}}` | $0.0$ | $0.0$ | $40.0$ | $1.0$ | Log bottom flange ($m_1=40\text{ kg}, y_1=10\text{ mm};\; n=1$) |
| `60 {{key:ENTER}} 160 {{key:Σ+}}` | $0.0$ | $40.0$ | $60.0$ | $2.0$ | Log web section ($m_2=60\text{ kg}, y_2=160\text{ mm};\; n=2$) |
| `30 {{key:ENTER}} 310 {{key:Σ+}}` | $40.0$ | $60.0$ | $30.0$ | $3.0$ | Log top flange ($m_3=30\text{ kg}, y_3=310\text{ mm};\; n=3$) |
| `{{key:x̄w}}` | $40.0$ | $60.0$ | $30.0$ | **$148.461538$** | Via `{{key:x̄,ȳ}}` $\to$ `{{key:x̄w}}`: weighted centroid $\bar{y} = 148.4615\text{ mm}$ |

Evaluating rotational moments of inertia ($I = \int r^2\,dm$) maps the canonical shape factors and Steiner's parallel-axis transfer term directly onto the stack:

* **Composite Cast-Iron Punch-Press Flywheel:** On an $85\text{-kg}$ punch-press flywheel assembled from a thick outer rim ($M_{\text{rim}} = 65\text{ kg}$, inner radius $r_1 = 0.28\text{ m}$, outer radius $r_2 = 0.35\text{ m}$) and a solid web disk ($M_{\text{web}} = 20\text{ kg}$, radius $R = 0.28\text{ m}$), sum $r_1^2 + r_2^2 = 0.200900\text{ m}^2$ in Register $X$ and scale by $\frac{1}{2}M_{\text{rim}} = 32.5\text{ kg}$ to store $I_{\text{rim}} = 6.529250\text{ kg}\cdot\text{m}^2$ in `A`. Evaluating $I_{\text{web}} = \frac{1}{2}M_{\text{web}}R^2 = 0.784000\text{ kg}\cdot\text{m}^2$ and recalling `A` to add them via `{{res:sc32_06_geometry_surface_area_seq_16:keys}}` $\longrightarrow$ `{{res:sc32_06_geometry_surface_area_seq_16:value}}` ($I_{\text{total}} = \mathbf{7.313250\text{ kg}\cdot\text{m}^2}$) confirms that the rim supplies $\mathbf{89.3\%}$ of the energy storage.
* **Jakob Steiner's Parallel-Axis Shift on a Robotic Arm Link:** Applying Steiner's parallel-axis theorem ($I_{\text{pivot}} = I_{\text{cm}} + md^2$) to the slender robotic arm link ($m = 3.5\text{ kg}$, length $L = 0.80\text{ m}$, shoulder offset $d = L/2 = 0.40\text{ m}$) executes in two stages across $(Y, X)$. First evaluate the midpoint centroidal inertia $I_{\text{cm}} = \frac{1}{12}mL^2 = 0.186667\text{ kg}\cdot\text{m}^2$ in Register $X$; then form the parallel-axis transfer term $md^2 = 0.560000\text{ kg}\cdot\text{m}^2$ ($= 3\,I_{\text{cm}}$) in Register $X$ while $I_{\text{cm}}$ waits in Register $Y$, and add them via `{{res:sc32_06_geometry_surface_area_seq_17:keys}}` $\longrightarrow$ `{{res:sc32_06_geometry_surface_area_seq_17:value}}` ($I_{\text{pivot}} = \frac{1}{3}mL^2 = \mathbf{0.746667\text{ kg}\cdot\text{m}^2}$).

For the thick-walled titanium bathysphere pressure hull ($R_2 = 1.10\text{ m}$ outer radius, $R_1 = 0.98\text{ m}$ inner cabin radius, and total mass $M = 7,347.74\text{ kg}$ for a Ti-6Al-4V shell of density $\rho = 4,500\text{ kg/m}^3$ and shell volume $V_{\text{shell}} = \frac{4}{3}\pi(R_2^3 - R_1^3) = 1.63283\text{ m}^3$, where substituting $M = \rho V_{\text{shell}}$ cancels $(R_2^3 - R_1^3)$ to leave $I = \frac{8}{15}\pi\rho(R_2^5 - R_1^5)$), evaluating $I_{\text{shell}} = \frac{2}{5}M\frac{R_2^5 - R_1^5}{R_2^3 - R_1^3}$ engages all four stack registers as the fifth-power difference $(R_2^5 - R_1^5) = 0.706589\text{ m}^5$ rides up into Registers $(T, Z, Y)$ while the third-power difference $(R_2^3 - R_1^3) = 0.389808\text{ m}^3$ forms in Register $X$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1.1 {{key:ENTER}} 5 {{key:yˣ}} 0.98 {{key:ENTER}} 5 {{key:yˣ}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.706589$ | Fifth-power difference $(R_2^5 - R_1^5)$ |
| `1.1 {{key:ENTER}} 3 {{key:yˣ}} 0.98 {{key:ENTER}} 3 {{key:yˣ}} {{key:-}}` | $0.706589$ | $0.706589$ | $0.706589$ | $0.389808$ | Third-power difference $(R_2^3 - R_1^3)$ |
| `{{key:÷}}` | $0.706589$ | $0.706589$ | $0.706589$ | $1.812660$ | Ratio $(R_2^5 - R_1^5)/(R_2^3 - R_1^3)$ |
| `7347.74 {{key:×}} 2 {{key:×}} 5 {{key:÷}}` | $0.706589$ | $0.706589$ | $0.706589$ | **$5327.4160$** | Mass moment of inertia $I$ in $\text{kg}\cdot\text{m}^2$ |

Finally, for a hollow steel drive shaft of outer radius $R_o = 40\text{ mm}$ and inner bore radius $R_i = 35\text{ mm}$, the fourth-power polar moment of inertia $J = \frac{\pi}{2}(R_o^4 - R_i^4)$ runs directly on $(Y, X)$ and reflects the algebraic factorization of $R_o^4 - R_i^4$ as a difference of squares of squares:

$$R_o^4 - R_i^4 = \left(R_o^2 - R_i^2\right)\left(R_o^2 + R_i^2\right) = \left(40^2 - 35^2\right)\left(40^2 + 35^2\right) = 375 \times 2,825 = 1,059,375\text{ mm}^4$$

Here the first factor $(R_o^2 - R_i^2) = 375\text{ mm}^2$ is proportional to the cross-sectional steel area ($375 / 1,600 = 23.44\%$ of a solid $40\text{-mm}$ bar), while $(R_o^2 + R_i^2) = 2,825\text{ mm}^2$ weights that steel by its squared radius near the outer wall. Keying `40 {{key:ENTER}} 4 {{key:yˣ}}` evaluates $R_o^4 = 2,560,000.0000\text{ mm}^4$ in Register $X$; keying `35 {{key:ENTER}} 4 {{key:yˣ}} {{key:-}}` subtracts the hollow core $R_i^4 = 1,500,625.0000\text{ mm}^4$ to leave $R_o^4 - R_i^4 = 1,059,375.0000\text{ mm}^4$; and scaling by `{{key:π}} {{key:×}} 2 {{key:÷}}` returns $J = \mathbf{1,664,071.7612\text{ mm}^4}$—retaining $41.38\%$ of the solid shaft's torsional rigidity with less than a quarter of the steel (just as boring out a shaft to $R_i / R_o = 0.76$ removes over half the mass while retaining $1 - 0.76^4 = \mathbf{66.6\%}$ of its torsional stiffness).

Across all composite geometric audits, clearing statistical memory with `{{key:CLΣ}}` isolates each new multi-face or centroid tally, Heron's radical guards against caliper misreads that violate the triangle inequality ($a + b \le c$) by signaling `INVALID DATA` (Code 02, cleared with `{{key:C}}`), and halving blueprint diameters ($D \to R = D/2$) before squaring or cubing prevents four-fold and eight-fold scaling errors.
