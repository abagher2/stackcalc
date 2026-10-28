---
title: "Chapter 6: Why Giants Can't Have Ant Legs: Scaling Laws, Solid Geometry & 3D Space | Thinking in the Stack (SC-32)"
description: "Explore Galileo's Square-Cube Law, Heron's triangle, Ramanujan's ellipse, Archimedes' sphere-and-cylinder tombstone, Cavalieri's slices, and 3D rotational inertia on the StackCalc SC-32."
---

# Chapter 6: Why Giants Can't Have Ant Legs: Scaling Laws, Solid Geometry & 3D Space

## Galileo's Giant and the Tyranny of the Square-Cube Law

### Why Ants Survive Any Fall While Giants Shatter Their Own Bones

Why can a common garden ant effortlessly lift a leaf ten times its own body weight, while a human being struggles to lift a single barbell of equivalent body mass? And if you were to scale a human being up by a factor of ten into a sixty-foot mythical giant—keeping every proportion of bone, muscle, and sinew geometrically identical—why would the giant's femurs shatter the very instant it tried to stand up?

In 1638, while confined under house arrest at his villa in Arcetri outside Florence, **Galileo Galilei** answered both questions in his final treatise, *Two New Sciences* (*Discorsi e dimostrazioni matematiche intorno a due nuove scienze*) {{cite:galilei1638}}. Galileo realized that nature is governed by a relentless geometric asymmetry between area and volume, now known as the **Square-Cube Law**.

Suppose you take any three-dimensional object—an ant, a cathedral column, a spherical fuel tank, or a silicon microprocessor—and scale every linear dimension (length, width, and height) by a multiplier $\ell$:

$$L \longrightarrow \ell L, \qquad A \propto \ell^2, \qquad V \propto \ell^3, \qquad \frac{A}{V} \propto \frac{\ell^2}{\ell^3} = \frac{1}{\ell}$$

The tensile or compressive strength of a bone or steel column depends on its **cross-sectional area** ($A \propto \ell^2$), because that cross-section is where intermolecular bonds resist the load. Likewise, aerodynamic drag during a fall and the rate at which an organism or machine can shed heat, absorb oxygen across lung membranes, or radiate thermal energy depend on its **exposed surface area** ($A \propto \ell^2$). Yet the gravitational weight the skeleton must support—and the metabolic or electrical heat generated inside the body—depends on the number of cells or atoms inside its **enclosed volume** ($V \propto \ell^3$).

Multiply a human being's height, width, and depth by $\ell = 10$ to make a sixty-foot giant, and the cross-sectional area of the giant's leg bones increases by $10^2 = 100\text{ times}$. But the giant's volume and weight increase by $10^3 = 1,000\text{ times}$! Every square centimeter of the giant's bone is suddenly crushed under ten times the stress of a normal human femur, snapping under its own weight—a biomechanical catastrophe famously dramatized by evolutionary biologist **J. B. S. Haldane** in his classic 1926 essay *"On Being the Right Size"* when he calculated why the sixty-foot Giant Pope and Giant Pagan in *Pilgrim's Progress* would shatter their thighs at every step. Conversely, as Haldane noted, you can drop a mouse or an ant down a thousand-foot mine shaft and watch it walk away unharmed: because terminal velocity in air occurs where gravitational weight ($\propto \ell^3$) balances aerodynamic drag ($\propto A v^2 \propto \ell^2 v^2$), terminal impact speed scales as $v_{\text{term}} \propto \sqrt{\ell^3 / \ell^2} = \sqrt{\ell}$. To survive on land, large animals cannot simply be scaled-up small animals: as Galileo sketched in the margins of *Two New Sciences*, an elephant or a *Brachiosaurus* must have disproportionately thick, pillar-like legs, just as a civil engineer scaling a tabletop balsa-wood bridge model up by $\ell = 50$ across a river gorge must thicken the steel chords or switch to hollow box girders lest the full-scale span collapse under its own dead weight.

### J. B. S. Haldane's Thermal Wall: Surface Area ($L^2$) vs. Volume ($L^3$)

That exact same $A/V \propto 1/\ell$ ratio governs thermal survival across biology and modern electronics. Inside a high-performance microprocessor, billions of nanometer-scale transistors switch at gigahertz frequencies, generating localized thermal flux exceeding $100\text{ W/cm}^2$ {{cite:incropera2007}}—a power density approaching the heat flux inside a nuclear reactor core. Under Jean-Baptiste Joseph Fourier's Law of Thermal Conduction and Isaac Newton's Law of Cooling {{cite:incropera2007}}, convective heat removal from a solid boundary to a surrounding fluid is proportional to the exposed surface area $A_{\text{surface}}$:

$$\dot{Q} = h \cdot A_{\text{surface}} \cdot (T_{\text{solid}} - T_{\text{fluid}})$$

Because heat generation scales with volume ($\ell^3$) while heat dissipation scales with surface area ($\ell^2$), scaling up any heat-producing body creates a thermal bottleneck:

* **Why Hummingbirds Enter Torpor While Elephants Grow Ear-Fins:** A $3\text{-gram}$ **ruby-throated hummingbird** ($\ell \approx 2\text{ cm}$) has an enormous surface-area-to-volume ratio ($A/V \propto 1/\ell$). It loses body heat across its skin so rapidly relative to its tiny thermal mass that its heart must beat $1,200\text{ times per minute}$ by day, and it must plunge into deep hypothermic **torpor** at night just to avoid starving before dawn. Conversely, a $5,000\text{-kilogram}$ **African elephant** ($\ell \approx 200\text{ cm}$—a $100\times$ linear scale-up over the hummingbird) generates $100^3 = 1,000,000\times$ the internal metabolic heat while possessing only $100^2 = 10,000\times$ the skin surface area. With $1/100\text{th}$ the relative cooling area, an elephant would fatally overheat if evolution had not broken geometric similarity by equipping it with huge, paper-thin, vascularized **ear-fins** that act as biological radiators.
* **Why Microprocessors Sprout Extruded Pin-Fin Forests:** A silicon CPU package faces the exact same dilemma as the elephant. If you leave an aluminum heat spreader as a flat block, its surface area is tiny. By machining or extruding the aluminum into dozens of thin parallel fins, you actually *remove* volume and mass while multiplying the exposed convective boundary area $A_{\text{surface}}$ by $300\%$ to $2,500\%$—cheating Galileo's Square-Cube Law by folding extra surface area into the same footprint.

In real-world mechanical design, aerospace enclosures, heat sinks, and structural castings are never single textbook cubes. They are bounded by dozens of planar walls, sloped frustum roofs, cylindrical bosses, and cutout apertures. On the SC-32, auditing a complex solid is modeled by turning the statistical accumulator key **`{{key:Σ+}}`** into a **Master Surface-Area & Volume Basket**: after clearing the registers with `{{key:CLΣ}}` (`{{key:↰}}` + `{{key:Σ+}}`), you compute each rectangular wall, circular boss, or trapezoidal facet right on Registers $Y$ and $X$ and toss it into `{{key:Σ+}}` (or subtract drilled holes and window apertures with `{{key:Σ-}}`), watching Register $X$ count each finished face group ($n = 1, 2, 3, \dots$) until `{{key:SUMS}}` (`{{key:↱}}` + `{{key:Σ+}}`) and softkey `{{key:Σx}}` recall the grand total with zero scratch paper.

---

## From Heron's Triangle and Ramanujan's Ellipse to Archimedes' Tombstone

To measure the world—whether surveying a triangular land parcel, bolted pipe flanges, planetary oblateness, or curved pressure vessels—mathematicians over two millennia uncovered a treasury of planar and solid mensuration formulas. Each formula hides a piece of geometric insight that transforms a difficult measurement into an effortless stack calculation.

### Planar Primitives, Difference-of-Squares Rings & Silver-Ratio Octagons

Every three-dimensional cross-section or enclosure boundary begins with two-dimensional planar figures—from simple rectangles, triangles, trapezoids, and circles to circular sectors, ellipses, parabolic arches, and cyclic quadrilaterals. On the four-register stack, two algebraic habits—**factoring differences of squares** ($R^2 - r^2 = (R - r)(R + r)$) and **exploiting geometric symmetry**—transform even intricate planar sections into effortless, one-pass calculations that never require intermediate scratchpad storage.

Consider the **Circular Annulus**—the flat ring formed by a pipe flange gasket, a thrust washer, or a hollow cylindrical wall bounded by outer radius $R$ and inner bore radius $r$. Computing $\pi R^2 - \pi r^2$ directly multiplies by $\pi$ twice and is numerically dangerous when the wall is very thin ($R \approx r$), because squaring two nearly equal numbers and subtracting them throws away significant digits. Factoring the difference of squares solves both problems at a stroke:

$$A = \pi(R^2 - r^2) = \pi(R - r)(R + r) = 2\pi \left(\frac{R + r}{2}\right)(R - r)$$

Geometrically, this factored form says that if you snip a circular ring and unroll it, its exact area is simply its **average circumference** $2\pi R_{\text{mean}}$ multiplied by its **radial wall thickness** $t = R - r$. On the SC-32, you can either subtract the squares `R {{key:x²}} r {{key:x²}} {{key:-}} {{key:π}} {{key:×}}` or form $(R - r)$ in Register $Y$ and $(R + r)$ in Register $X$ before pressing `{{key:×}} {{key:π}} {{key:×}}` to preserve full precision on thin-walled aerospace tubing. For an ASME B16.5 high-pressure neoprene flange gasket with outer radius $R = 85.0\text{ mm}$ and inner bore radius $r = 50.0\text{ mm}$, factoring $\pi$ outside $(85^2 - 50^2) = 7,225 - 2,500 = 4,725\text{ mm}^2$ immediately yields $4,725\pi \approx \mathbf{14,844.0253\text{ mm}^2}$.

What if an instrument cover or structural gusset is a **regular octagon** of side length $s = 65.0\text{ mm}$ rather than a circle? You do not need to look up a trigonometric cotangent to find its area. Picture a regular octagon as a bounding square of width $(1 + \sqrt{2})s$ that has had four $45^\circ\text{–}45^\circ\text{–}90^\circ$ right-isosceles corner triangles of leg $s/\sqrt{2}$ clipped off its four corners. Each clipped corner has area $\frac{1}{2}(s/\sqrt{2})^2 = \frac{1}{4}s^2$, so all four corners together remove exactly $s^2$ from the bounding square $(1 + \sqrt{2})^2 s^2 = (3 + 2\sqrt{2})s^2$:

$$A = (3 + 2\sqrt{2})s^2 - s^2 = 2(1 + \sqrt{2})s^2 = 2\delta_S s^2 \approx 4.828427 \, s^2$$

where $\delta_S = 1 + \sqrt{2} \approx 2.414214$ is the classical **silver ratio** (`2 {{key:√x}} 1 {{key:+}}`). Multiplying $2(1 + \sqrt{2})$ by $65^2 = 4,225\text{ mm}^2$ (`65 {{key:x²}} {{key:×}}`) gives the exact octagonal area $\mathbf{20,400.1047\text{ mm}^2}$.

### Ramanujan's Ellipse Perimeter & Earth's Equatorial Bulge

One of the great surprises of classical geometry is the stark contrast between the *area* of an ellipse and its *perimeter*. Because an ellipse with semi-major axis $a$ and semi-minor axis $b$ is simply a circle of radius $b$ stretched along one axis by the factor $a/b$, its area scales by that exact same factor: $A = \pi b^2 \cdot (a/b) = \pi a b$. Yet if you ask for the **perimeter (circumference)** of that same ellipse, no closed-form expression in elementary functions exists anywhere in mathematics. Setting up the arc-length integral $\int \sqrt{dx^2 + dy^2}$ leads to an irreducible integral that defied Leonhard Euler and Adrien-Marie Legendre—and is, in fact, the very reason **elliptic integrals** were given their name.

In 1914, the self-taught Indian mathematical genius **Srinivasa Ramanujan** published an algebraic approximation of breathtaking accuracy. Ramanujan defined the dimensionless symmetric flattening parameter $h$:

$$h = \frac{(a - b)^2}{(a + b)^2}, \qquad P \approx \pi (a + b) \left[ 1 + \frac{3h}{10 + \sqrt{4 - 3h}} \right]$$

Why is Ramanujan's formula so extraordinarily accurate? If you expand the exact complete elliptic integral for the perimeter of an ellipse as a power series in $h$, it begins $P = \pi(a+b)\left[1 + \frac{1}{4}h + \frac{1}{64}h^2 + \frac{1}{256}h^3 + \frac{25}{16384}h^4 + \dots\right]$. When you expand Ramanujan's nested square root $\frac{3h}{10 + \sqrt{4 - 3h}}$ in a Taylor series, it matches the exact elliptic integral cleanly through the $h^1$, $h^2$, and $h^3$ terms, missing the $h^4$ coefficient by just $\frac{1}{16384}$! Even for highly elongated orbits and elliptical machine cams, Ramanujan's formula is accurate to better than a part per million.

That axial difference $(a - b)$ between semi-major and semi-minor axes also governs the shape of our own planet. As Isaac Newton predicted in Book III of the *Principia* (1687), because the Earth rotates once every $23\text{ hours } 56\text{ minutes}$, centrifugal acceleration flings ocean and mantle outward at the equator, deforming our planet from a sphere into an **oblate spheroid**. In the modern WGS-84 geodetic standard, Earth's equatorial semi-major axis is $a = 6,378.137\text{ km}$ while its polar semi-minor axis is $b = 6,356.752\text{ km}$—meaning the equator bulges $a - b = 21.385\text{ km}$ farther from Earth's center than the poles. Geodesists express this oblateness by the **flattening** $f$ and its reciprocal $1/f$ (evaluated on the stack without re-typing $a$ via `b {{key:ENTER}} a {{key:÷}} 1 {{key:x⇄y}} {{key:-}} {{key:1/x}}`):

$$f = \frac{a - b}{a} = 1 - \frac{b}{a} = \frac{6378.137 - 6356.752}{6378.137} = \frac{21.385}{6378.137} \approx \frac{1}{\mathbf{298.2572}}$$

Because the Mississippi River flows southward toward the equatorial bulge, its mouth at the Gulf of Mexico actually sits roughly four miles *farther* from the center of the Earth than its headwaters at Lake Itasca.

### Heron's Semiperimeter Formula & Right-Triangle Incircles

Suppose a surveyor in the field measures the three boundary lengths of a triangular parcel—say $a = 7.0\text{ m}$, $b = 9.0\text{ m}$, and $c = 12.0\text{ m}$—using a steel tape or laser rangefinder. Finding the parcel's area from $A = \frac{1}{2}bh$ would normally require solving for an interior angle via the Law of Cosines and then taking a sine to find the perpendicular altitude $h$.

In the 1st century CE, **Heron of Alexandria** proved in his *Metrica* (a work rediscovered in a Constantinople manuscript in 1896, though Archimedes likely knew the theorem two centuries earlier) that you can bypass trigonometry completely. Define the **semiperimeter** $s$ as half the triangle's perimeter:

$$s = \frac{a + b + c}{2}, \qquad A = \sqrt{s(s - a)(s - b)(s - c)}$$

For our $7\text{–}9\text{–}12\text{ m}$ parcel, storing the semiperimeter $s = (7 + 9 + 12)/2 = 14.0\text{ m}$ in Variable `S` (`{{key:STO}} S`) lets you subtract each side and multiply the three excess factors $(s - a) = 7.0$, $(s - b) = 5.0$, and $(s - c) = 2.0$ right on the stack, whose product with $s$ is $14 \times 7 \times 5 \times 2 = 980$, yielding $A = \sqrt{980} = 14\sqrt{5} \approx \mathbf{31.304952\text{ m}^2}$ via `{{key:√x}}`. Better still, Heron's radicand contains a built-in physical diagnostic: by the Euclidean **triangle inequality**, the sum of any two sides of a real triangle must exceed the third ($a + b > c$, which means $s > c$ and $(s - c) > 0$). If a misread blueprint specifies three lengths that cannot possibly close into a triangle—such as $3, 4$, and $9$—then $(s - c)$ turns negative and `{{key:√x}}` immediately flags an impossible geometry (`INVALID DATA`).

Why does the semiperimeter $s$ appear so naturally inside triangle geometry? Drop an **incircle** of radius $r$ inside any triangle so that it touches all three sides tangentially, and draw lines from the incenter to the three vertices. Those lines partition the triangle into three smaller triangles of heights $r$ and bases $a, b, c$, whose areas sum to $\frac{1}{2}ar + \frac{1}{2}br + \frac{1}{2}cr = \left(\frac{a+b+c}{2}\right)r = s \cdot r$. Thus, for *every* triangle:

$$A = r \cdot s \implies r = \frac{A}{s}$$

Once Heron's area $A$ sits in Register $X$ and the semiperimeter $s$ still resides in Variable `S` (or in `{{key:LASTX}}` before the square root), a single recall and division (`{{key:RCL}} S {{key:÷}}`) delivers the exact inscribed circle radius $r = 31.304952 / 14 = 2.236068\text{ m}$ of *any* triangle. When the triangle happens to be a **right triangle** with orthogonal legs $a$ and $b$ and hypotenuse $c = \sqrt{a^2 + b^2}$ (computed in one keystroke via `{{key:▸θ,r}}`), the tangent segments around the $90^\circ$ corner simplify $r = A/s$ into the rapid linear mental shortcut $r = \frac{a + b - c}{2}$ (whose full geometric dissection we will explore in **Chapter 14**). For a right-angled structural channel with legs $a = 15.0\text{ cm}$, $b = 20.0\text{ cm}$, and hypotenuse $c = 25.0\text{ cm}$, the largest cylindrical cooling pipe that can nestle inside the channel has radius $r = (15 + 20 - 25)/2 = \mathbf{5.0000\text{ cm}}$.

### Cavalieri's Coin Stack, Archimedes' Tombstone & the Steinmetz Bicylinder

Stepping from flat planes into three-dimensional solids, how did mathematicians find the exact volumes of cones, spheres, paraboloids, and intersecting pipes centuries before Isaac Newton and Gottfried Wilhelm Leibniz codified integral calculus?

The secret weapon behind classical solid mensuration was formalized in 1635 by Galileo's student **Bonaventura Cavalieri**, though **Archimedes of Syracuse** and the 3rd-century Chinese mathematicians **Liu Hui** and **Zu Chongzhi** wielded it with astonishing virtuosity. Imagine stacking twenty quarters into a neat vertical cylinder on your desk, and then nudging the coins sideways so the stack leans over or winds into an S-curve. Did the volume of the stack change? Not by a single cubic millimeter. **Cavalieri's Principle** states that if two solids have the same total height, and if slicing them parallel to their bases at *every* height $z$ reveals cross-sections of identical area $A(z)$ (or a constant ratio of areas), then their total volumes must be identical (or stand in that exact same ratio).

See what Cavalieri's Principle unlocks across solid geometry and how each solid maps onto the stack:

1. **Why Every Cone and Pyramid Is One-Third of Its Box ($V = \frac{1}{3}A_{\text{base}}h$):** Slice any pyramid or cone horizontally at distance $z$ below its apex. Because linear dimensions grow linearly with $z/h$, the cross-sectional area grows *quadratically*: $A(z) = A_{\text{base}}(z/h)^2$. Since the average value of $(z/h)^2$ from $0$ to $h$ is $\frac{1}{3}$ (which you can also see geometrically by dissecting a cube into three identical square pyramids meeting at one corner), *every* cone or pyramid—whether its base is a circle, a square, an octagon, or an aerodynamic ellipse ($A_{\text{base}} = \pi ab$, giving $V = \frac{1}{3}\pi abh$)—encloses exactly one-third the volume of its bounding prism or cylinder (`3 {{key:÷}}`). Likewise, a **paraboloid of revolution** whose radius grows as $r(z) \propto \sqrt{z}$ has cross-sectional area $A(z) \propto z$, whose average from $0$ to $h$ is exactly **one-half** ($V = \frac{1}{2}\pi r^2 h$).
2. **Archimedes' Tombstone (The Sphere vs. The Cylinder):** What was the single theorem Archimedes was proudest of in his entire life? Not his war machines, nor his lever, nor his crown buoyancy test, but his proof in *On the Sphere and Cylinder* (c. 225 BCE) that if you place a sphere of radius $r$ snugly inside a right circular cylinder of radius $r$ and height $h = 2r$, **both the volume and the total surface area of the sphere are exactly two-thirds ($\frac{2}{3}$) of the cylinder!**
   * How did Archimedes see it via slices? Take the top hemisphere of radius $r$, place it next to a cylinder of radius $r$ and height $r$ that has had an inverted $45^\circ$ cone ($r_{\text{cone}}(z) = z$) carved out of its center, and slice both solids at height $z$ above the equator. By the Pythagorean theorem, the hemisphere's slice is a disk of radius $\sqrt{r^2 - z^2}$ and area $\pi(r^2 - z^2)$. Meanwhile, the punctured cylinder's slice is an annulus of outer radius $r$ and inner hole radius $z$, whose area is also $\pi(r^2 - z^2)$. Because every horizontal slice matches identically, the hemisphere's volume equals the cylinder minus the cone: $\pi r^3 - \frac{1}{3}\pi r^3 = \frac{2}{3}\pi r^3$. Doubling for both hemispheres gives $V_{\text{sphere}} = \frac{4}{3}\pi r^3 = \frac{2}{3}(2\pi r^3) = \frac{2}{3}V_{\text{cylinder}}$, while its surface area $A_{\text{sphere}} = 4\pi r^2$ is likewise $\frac{2}{3}$ of the cylinder's total area ($2\pi r^2 + 2\pi r(2r) = 6\pi r^2$). At Archimedes' request, a sphere inscribed inside a cylinder with the ratio $2:3$ was carved onto his tombstone in Syracuse—and it was by spotting that very carving overgrown with brambles in 75 BCE that the Roman orator Cicero rediscovered Archimedes' forgotten grave.
3. **The Steinmetz Bicylinder (*Mouhefanggai*) Where $\pi$ Cancels Out:** What happens when two equal circular cylinders of radius $r$ intersect at a $90^\circ$ right angle—like a cross-joint in high-pressure refinery piping or a classical Roman groin vault? Both Archimedes (in *The Method*, preserved only on the famous Archimedes Palimpsest) and Liu Hui (who named the intersection solid the *Mouhefanggai*, or "two square umbrellas") noticed a miracle when you inscribe a sphere of radius $r$ inside the intersection of the two pipes. Slice the bicylinder horizontally at height $z$: because both cylinders have half-width $\sqrt{r^2 - z^2}$ at height $z$, their intersection is a **square** of side $2\sqrt{r^2 - z^2}$ and area $4(r^2 - z^2)$, whereas the inscribed sphere's slice is a **circle** of area $\pi(r^2 - z^2)$. At every single slice from bottom to top, the bicylinder's square slice is exactly $\frac{4}{\pi}$ times the sphere's circular slice. By Cavalieri's Principle, the total volume of the intersecting cylinders is $\frac{4}{\pi}$ times the sphere's volume—causing $\pi$ to cancel out completely:

$$V_{\text{bicylinder}} = \frac{4}{\pi} \left(\frac{4}{3}\pi r^3\right) = \frac{16}{3} r^3, \qquad A_{\text{bicylinder}} = 16 r^2$$

Even though the solid is bounded entirely by curved cylindrical walls, neither its volume nor its surface area contains $\pi$!

4. **Conical Frustums & the Egyptian *Seked* Pyramid:** When a cone or pyramid is sliced flat at height $h$ before reaching its apex, leaving bottom radius $R$ and top radius $r$, its volume is $V = \frac{1}{3}\pi h(R^2 + Rr + r^2)$—a formula already known for square pyramids in the 1850 BCE Moscow Mathematical Papyrus. On the SC-32, squaring $R$ via `R {{key:x²}}` automatically saves $R$ in **`{{key:LASTX}}`**, so keying `{{key:LASTX}} r {{key:×}} {{key:LASTX}} {{key:x²}} {{key:+}} {{key:+}}` forms the three-term sum $(R^2 + Rr + r^2)$ while typing $R$ and $r$ only once each. Physically, the frustum's volume is simply its height $h$ multiplied by the **arithmetic average of three areas**: the bottom base $A_1 = \pi R^2$, the top base $A_2 = \pi r^2$, and their **geometric mean** $\sqrt{A_1 A_2} = \pi Rr$.
5. **Inscribing a Regular Tetrahedron Inside a Cube:** Why does the volume of a regular tetrahedron of edge length $a$ contain the mysterious coefficient $\frac{\sqrt{2}}{12}a^3$? Draw the face diagonals connecting four alternating corners of a cube whose edge length is $c = a/\sqrt{2}$ (so each face diagonal has length $\sqrt{2}c = a$). Those six face diagonals form a regular tetrahedron of edge $a$ sitting snugly inside the cube. The space outside the tetrahedron consists of four right-angled corner pyramids, each having three mutually perpendicular legs of length $c$ and volume $\frac{1}{3}\left(\frac{1}{2}c^2\right)c = \frac{1}{6}c^3$. Slicing off those four corners removes $4 \times \frac{1}{6} = \frac{2}{3}$ of the cube, leaving the central tetrahedron with $1 - \frac{2}{3} = \frac{1}{3}$ of the cube's volume: $V = \frac{1}{3}c^3 = \frac{1}{3}\left(\frac{a}{\sqrt{2}}\right)^3 = \frac{\sqrt{2}}{12}a^3$.
6. **Pappus of Alexandria's Centroid Revolution Theorems (Why a Torus Has $\pi^2$):** Consider the volume ($V = 2\pi^2 R r^2$) and surface area ($A = 4\pi^2 R r$) of a **torus**—a doughnut or O-ring gasket with major orbit radius $R$ and minor tube cross-section radius $r$. Why does $\pi$ appear *squared* ($\pi^2 \approx 9.8696$, evaluated via `{{key:π}} {{key:x²}}`) inside a doughnut?
   Around 340 CE, **Pappus of Alexandria** (rediscovered in 1615 by Swiss mathematician **Paul Guldin**) proved two sweeping theorems that link solid mensuration directly to the **centroid (center of mass)** we study in Section 3:
   * **First Theorem of Pappus-Guldinus (Surface Area of Revolution):** When a planar curve of arc length $L$ is revolved around an external axis in its plane, the surface area swept out equals the curve's length $L$ multiplied by the **circumference of the circle $2\pi R_{\text{cm}}$ traveled by its centroid**:
     $$A = L \cdot \left(2\pi R_{\text{cm}}\right)$$
     For a torus, the generating circle has circumference $L = 2\pi r$ and its centroid travels a circle of length $2\pi R$, giving $A = (2\pi r)(2\pi R) = 4\pi^2 R r$—exactly as if you sliced the rubber O-ring open and unrolled it into a straight cylinder of length $2\pi R$.
   * **Second Theorem of Pappus-Guldinus (Volume of Revolution):** When a planar region of area $A_{\text{cross}}$ is revolved around an external axis, the volume swept out equals the cross-sectional area $A_{\text{cross}}$ multiplied by the **distance $2\pi R_{\text{cm}}$ traveled by its centroid**:
     $$V = A_{\text{cross}} \cdot \left(2\pi R_{\text{cm}}\right)$$
     For our torus, a circular disk of area $A_{\text{cross}} = \pi r^2$ orbits a path of length $2\pi R$, yielding $V = (\pi r^2)(2\pi R) = 2\pi^2 R r^2$ without evaluating a single integral.
7. **Leonhard Euler's Polyhedral Formula ($V - E + F = 2$) & Why Only Five Platonic Solids Exist:** Why did Plato, Euclid, and Johannes Kepler find that all of three-dimensional space permits **only five regular convex polyhedra** (the Platonic solids: the 4-faced tetrahedron, 6-faced cube, 8-faced octahedron, 12-faced dodecahedron, and 20-faced icosahedron), whereas two-dimensional space permits infinitely many regular polygons?
   In 1750, **Leonhard Euler** discovered the topological invariant governing every convex polyhedron with $V$ vertices, $E$ edges, and $F$ faces:
   $$V - E + F = 2$$
   Imagine stretching a polyhedron's wireframe onto a rubber balloon, puncturing one face, and flattening the remaining $F - 1$ faces onto a table: removing each edge merges two faces ($\Delta E = -1, \Delta F = -1$, keeping $V - E + F$ constant), and contracting a tree of $V$ vertices and $V - 1$ edges down to a single point leaves $1 - 0 + 1 = 2$. Furthermore, at every vertex of a convex polyhedron, at least $3$ faces must meet, and the sum of their flat corner angles must be strictly **less than $360^\circ$** (otherwise the faces flatten into a floor tile pattern and cannot fold up into a 3D corner). Because equilateral triangles have $60^\circ$ corners, you can fold $3$, $4$, or $5$ of them around a vertex ($180^\circ, 240^\circ, 300^\circ < 360^\circ$) to build the tetrahedron, octahedron, and icosahedron; squares ($90^\circ$) allow $3$ per vertex ($270^\circ$) to build the cube; and regular pentagons ($108^\circ$) allow $3$ per vertex ($324^\circ$) to build the dodecahedron. By the time you reach hexagons ($3 \times 120^\circ = 360^\circ$), the corners lie completely flat like a honeycomb—closing the door on regular polyhedra forever!

### Spherical Caps, Girard's Spherical Excess & Asteroid Power Means

Curved shells and planetary surfaces bring three more geometric gems:

* **Spherical Caps & Hortonsphere Storage Tanks:** In petrochemical refineries, liquefied gases are stored inside giant spherical **Hortonsphere** tanks of radius $R$ because a sphere resists internal pressure with uniform membrane tension (half the hoop stress of a cylinder of equal radius). When an ultrasonic sensor measures liquid depth $h$ at the bottom of the sphere, integrating horizontal disk slices of radius $r^2(z) = R^2 - (R-z)^2 = 2Rz - z^2$ from $z = 0$ to $h$ gives the **spherical cap volume**:
  $$V_{\text{cap}} = \int_0^h \pi(2Rz - z^2)\,dz = \pi\left(Rh^2 - \frac{1}{3}h^3\right) = \frac{1}{3}\pi h^2(3R - h)$$
  Even more remarkably, Archimedes proved that the curved surface area of any spherical cap or zone of thickness $h$ is $A_{\text{zone}} = 2\pi R h$—depending *only* on the slice thickness $h$, and identical to the lateral wall area punched out on the circumscribing cylinder.
* **Spherical Lunes & Albert Girard's Spherical Excess (1629):** On a flat plane, the interior angles of every triangle sum to $180^\circ$ ($\pi\text{ rad}$), whether the triangle is drawn on a postage stamp or across a football field. On a curved sphere of radius $R$, however, great-circle paths bow outward, and the interior angles $(\alpha, \beta, \gamma)$ of a **spherical triangle** *always* sum to more than $180^\circ$. For instance, if you start at the North Pole, walk south to the Equator along the Prime Meridian, turn $90^\circ$ west along the Equator to $90^\circ\text{ W}$, and turn $90^\circ$ north back to the North Pole, you have traced a spherical triangle with **three $90^\circ$ right angles** ($\alpha + \beta + \gamma = 270^\circ$) enclosing one-eighth of the globe ($\frac{1}{8}\cdot 4\pi R^2 = \frac{\pi}{2}R^2$).
  In 1629, the Dutch-French mathematician **Albert Girard** proved how the angle sum and area are locked together. Each pair of intersecting great circles forms two crescent-shaped **spherical lunes** of area $A_{\text{lune}} = 2R^2\theta_{\text{rad}}$. By overlaying the three lune pairs covering the three sides of a spherical triangle—which cover the entire sphere once while triple-covering the triangle itself and its antipodal twin—Girard proved that the **spherical excess** $E_{\text{rad}} = (\alpha + \beta + \gamma) - \pi$ is directly proportional to the triangle's area:
  $$E_{\text{rad}} = (\alpha^\circ + \beta^\circ + \gamma^\circ - 180^\circ)\frac{\pi}{180^\circ}, \qquad A_{\text{triangle}} = R^2 E_{\text{rad}}$$
  On a sphere, you can determine the physical area of a continent-sized survey network simply by measuring three angles with a theodolite!
* **Knud Thomsen's Triaxial Asteroid Formula (2004):** Just as the perimeter of a 2D ellipse has no elementary closed form, the surface area of a 3D **triaxial ellipsoid** with semi-axes $(a, b, c)$—the standard shape model for potato-shaped asteroids like Eros or Toutatis—requires incomplete elliptic integrals. In 2004, Danish mathematician **Knud Thomsen** showed that taking a power mean of the three projected semi-axis products $(ab, ac, bc)$ with exponent $p = 1.6075$ (reusing the exponent $p$ across all three `{{key:yˣ}}` terms via `{{key:LASTX}}` before inverting with `{{key:1/x}}`):
  $$A \approx 4\pi \left(\frac{(ab)^p + (ac)^p + (bc)^p}{3}\right)^{1/p} \qquad (p = 1.6075)$$
  approximates the exact elliptic surface integral to within $1.06\%$ across all aspect ratios.

### Why 3D Printer Slicers Need Both Surface Area and Volume

To see how surface area and enclosed volume join forces in modern manufacturing, consider what happens inside a Fused Deposition Modeling (FDM) 3D printer slicer when preparing an engineering enclosure or structural bracket. Unlike a cast-iron or injection-molded part that is $100\%$ solid throughout, a 3D-printed part—like the hollow trabecular wing bones of an albatross or eagle—is a **composite sandwich structure**:

1. **Solid Outer Perimeter Shells ($V_{\text{shell}} \approx A_{\text{surface}} \cdot t_{\text{shell}}$):** The print nozzle first traces $N_{\text{walls}}$ solid perimeter loops (typically $3$ loops at $w_{\text{line}} = 0.45\text{ mm}$ extrusion width, forming a solid outer skin of thickness $t_{\text{shell}} = 1.35\text{ mm}$) across the entire exterior boundary surface area $A_{\text{surface}}$.
2. **Sparse Internal Gyroid Lattice Core ($V_{\text{core}} = V_{\text{interior}} \cdot f_{\text{infill}}$):** The enclosed interior volume $V_{\text{interior}} = V_{\text{total}} - V_{\text{shell}}$ is filled not with solid polymer, but with a periodic minimal-surface **gyroid** or cubic lattice at $f_{\text{infill}} = 15\%\text{–}25\%$ relative density.
3. **Total Filament Mass Takeoff:** Multiplying the combined shell and core polymer volumes by the filament density $\rho$ (such as $\rho \approx 1.24\text{ g/cm}^3 = 0.00124\text{ g/mm}^3$ for PLA or $1.27\text{ g/cm}^3$ for PETG) gives the exact mass of the finished part:

$$m_{\text{part}} = \rho \left( A_{\text{surface}} \cdot t_{\text{shell}} + V_{\text{interior}} \cdot f_{\text{infill}} \right)$$

For thin-walled enclosures like the SC-32 handheld chassis ($A_{\text{surface}} = 25,460\text{ mm}^2$), over $70\%$ of the polymer mass lives in the outer perimeter skin ($A_{\text{surface}} \cdot t_{\text{shell}}$) rather than the interior infill—which is why fast, accurate multi-face surface area takeoffs with `{{key:Σ+}}` and `{{key:SUMS}}` are indispensable on the shop floor.

---

## Navigating 3D Space: Euclidean Distance, Centroids & Rotational Inertia

Once we know the size and shape of a three-dimensional body, how do we locate it in space, find its balance point, and predict how hard it is to spin?

### The 3D Pythagorean Theorem, Unwrapped Helical Springs & Direction Cosines

In Chapter 4, we found the distance between two points on a flat sheet of paper via the 2D Pythagorean theorem $r = \sqrt{\Delta x^2 + \Delta y^2}$. If we now step out of the flat plane by rising an elevation $\Delta z$ perpendicular to the floor, the floor diagonal $r = \sqrt{\Delta x^2 + \Delta y^2}$ and the vertical rise $\Delta z$ form a second right triangle whose hypotenuse is the straight-line **3D Euclidean distance**:

$$d = \sqrt{r^2 + \Delta z^2} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$

On the SC-32, you can evaluate this 3D distance either by summing the three squares (`{{key:x²}}`) or by **chaining the polar key `{{key:▸θ,r}}` twice**: loading $(\Delta z, \Delta y, \Delta x)$ onto Registers $(Z, Y, X)$ and pressing `{{key:▸θ,r}} {{key:x⇄y}} {{key:R↓}} {{key:▸θ,r}}` collapses $\sqrt{\Delta x^2 + \Delta y^2}$ into $r_{xy}$ on the first tap and combines $r_{xy}$ with $\Delta z$ into $d = \sqrt{r_{xy}^2 + \Delta z^2}$ on the second tap without squaring a single number! Why do `{{key:x⇄y}} {{key:R↓}}` sit between the two `{{key:▸θ,r}}` taps? Because the first `{{key:▸θ,r}}` leaves the 2D floor radius $r_{xy} = \sqrt{\Delta x^2 + \Delta y^2}$ in Register $X$ and the horizontal azimuth angle $\theta$ in Register $Y$ (with $\Delta z$ waiting above in Register $Z$), so `{{key:x⇄y}} {{key:R↓}}` rolls the unneeded azimuth $\theta$ out of the way into Register $T$ and drops $(\Delta z, r_{xy})$ cleanly into Registers $(Y, X)$ for the second `{{key:▸θ,r}}` tap—which even leaves the 3D elevation angle $\phi = \arctan(\Delta z / r_{xy})$ in Register $Y$!

That three-component Pythagorean sum also solves a classic machine-shop puzzle: how long a piece of straight spring-steel wire $L$ must you cut to wind a **tapered conical compression spring** with bottom radius $R_1$, top radius $R_2$, axial height $h$, and $N$ active coils? Imagine unrolling the conical helix into three mutually perpendicular motions:
* **Circumferential wrap:** $N$ full turns at the mean radius $R_m = \frac{1}{2}(R_1 + R_2)$, covering horizontal distance $\Delta s_\theta = 2\pi N R_m$.
* **Axial climb:** Vertical rise $\Delta z = h$.
* **Radial inward taper:** Inward spiral step $\Delta r = R_1 - R_2$.

Because the circumferential, axial, and radial directions are mutually orthogonal at every point along the wire, the total wire length is simply their 3D Pythagorean norm:

$$L \approx \sqrt{(2\pi N R_m)^2 + h^2 + (R_1 - R_2)^2}$$

Similarly, when a deep-space radar or robotic gimbal tracks a target at 3D displacement vector $\vec{V} = (\Delta x, \Delta y, \Delta z)$ at total range $d = |\vec{V}| = \sqrt{\Delta x^2 + \Delta y^2 + \Delta z^2}$, dividing each coordinate by the range $d$ produces the three **direction cosines** $(\cos\alpha, \cos\beta, \cos\gamma) = \left(\frac{\Delta x}{d}, \frac{\Delta y}{d}, \frac{\Delta z}{d}\right)$—the components of the 3D unit pointing vector $\hat{u} = \vec{V}/d$, which obey the 3D Pythagorean identity:

$$\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$$

### The Balance Point of a Composite Structure: Center of Mass

Where is the single point at which an asymmetric airplane wing, a welded I-beam girder, or a multi-stage rocket balances? As Archimedes established in *On the Equilibrium of Planes*, if a body is assembled from $N$ components with masses (or cross-sectional areas) $m_1, m_2, \dots, m_N$ centered at positions $x_1, x_2, \dots, x_N$, each piece exerts a gravitational torque (first moment) $m_k x_k$ about the origin. The composite **center of mass (centroid)** $\bar{x}_{\text{cm}}$ is the exact location where a single support fulcrum balances all those torques—the **mass-weighted mean** of the coordinates:

$$\bar{x}_{\text{cm}} = \frac{m_1 x_1 + m_2 x_2 + \dots + m_N x_N}{m_1 + m_2 + \dots + m_N} = \frac{\sum_{k=1}^N m_k x_k}{\sum_{k=1}^N m_k}$$

The SC-32 models composite centroids directly through its statistical registers: when you place each component's mass (or area) $m_k$ in **Register $Y$** and its coordinate $x_k$ in **Register $X$**, pressing **`{{key:Σ+}}`** automatically accumulates the torque sum $\sum m_k x_k$ into $\Sigma xy$ and the total mass $\sum m_k$ into $\Sigma y$. Opening the **`{{key:x̄,ȳ}}` menu** (`{{key:↱}}` + `{{key:yˣ}}`) and pressing the weighted-mean softkey **`{{key:x̄w}}`** then divides $\Sigma xy / \Sigma y$ in a single keystroke to return $\bar{x}_{\text{cm}}$!

### Why Figure Skaters Spin Faster & Why Drive Shafts Are Hollow: Moments of Inertia

In linear motion, a $10\text{-kilogram}$ steel block requires the same force to accelerate whether it is shaped like a compact cannonball or a long thin bicycle wheel. In **rotational motion**, however, shape and mass distribution change everything.

Suppose a small mass $m$ orbits an axle at radial distance $r$ with angular velocity $\omega\text{ (rad/s)}$. Its linear speed is $v = r\omega$, so its kinetic energy is:

$$K = \frac{1}{2} m v^2 = \frac{1}{2} m (r\omega)^2 = \frac{1}{2} \left(m r^2\right) \omega^2$$

Summing $m r^2$ over every particle in a rigid body defines its **rotational moment of inertia** $I = \int r^2\,dm$, so that rotational kinetic energy is $K_{\text{rot}} = \frac{1}{2} I \omega^2$ and angular momentum is $L = I \omega$. Notice that the radial distance $r$ is **squared** (`{{key:x²}}`). Moving a kilogram of mass twice as far from the axis of rotation makes it *four times* harder to spin up or slow down.

Once you see that $r^2$ weighting, half of mechanical and structural engineering suddenly clicks into focus:

* **Why a Spinning Figure Skater Blurs Into a Vortex:** When an Olympic figure skater enters a scratch spin with her arms and free leg extended outward, a significant fraction of her mass sits at a large radius $r$ from her vertical spin axis, giving her a large moment of inertia $I_{\text{open}}$. When she pulls her arms and leg tightly against her chest, she reduces $r$ by roughly a factor of two, cutting her moment of inertia $I_{\text{closed}} \propto r^2$ by a factor of three or four. Because the ice exerts almost zero rotational friction torque, her angular momentum $L = I\omega$ is conserved—so cutting $I$ to one-third forces her spin rate $\omega$ to **triple** on the spot!
* **Why Flywheels Put Their Iron in the Outer Rim:** For symmetric bodies of total mass $M$ and outer radius $R$, the center-of-mass moment of inertia is $I_{\text{cm}} = k M R^2$, where the dimensionless shape factor $k$ tells us how close the mass sits to the outer boundary:
  * **Thin cylindrical hoop or rim:** $I_{\text{cm}} = M R^2$ ($k = 1$, all mass at radius $R$)
  * **Thick annular ring (radii $r_1, r_2$):** $I_{\text{cm}} = \frac{1}{2} M (r_1^2 + r_2^2)$
  * **Solid uniform cylinder or disk:** $I_{\text{cm}} = \frac{1}{2} M R^2$ ($k = 0.50$)
  * **Thin spherical shell:** $I_{\text{cm}} = \frac{2}{3} M R^2$ ($k \approx 0.67$)
  * **Solid uniform sphere:** $I_{\text{cm}} = \frac{2}{5} M R^2$ ($k = 0.40$)
  * **Slender rod of length $L$ (about midpoint):** $I_{\text{cm}} = \frac{1}{12} M L^2$
  A mechanical punch-press flywheel concentrates nearly $80\%$ of its cast iron into a thick outer rim supported by a thin inner web so that almost $90\%$ of its mass works at maximum $r^2$ leverage.
* **Jakob Steiner's Parallel-Axis Theorem ($I = I_{\text{cm}} + M d^2$):** What if a robotic arm link or pendulum does not spin around its own center of mass, but pivots about a shoulder joint displaced by a perpendicular distance $d$ from its centroid? Swiss geometer **Jakob Steiner** proved that you never need to re-integrate $\int r^2\,dm$ from scratch. Because the cross-terms in $(r_{\text{cm}} + d)^2 = r_{\text{cm}}^2 + 2 d\,r_{\text{cm}} + d^2$ integrate to zero around the center of mass ($\int r_{\text{cm}}\,dm = 0$), the moment of inertia about *any* parallel axis at distance $d$ is simply the centroidal inertia plus the inertia of treating the entire body as a point mass at distance $d$:
  $$I_{\text{parallel}} = I_{\text{cm}} + M d^2$$
  For a slender robotic arm link of mass $m$ and length $L$, shifting the pivot from its midpoint ($I_{\text{cm}} = \frac{1}{12}mL^2$) to its shoulder joint at one end ($d = L/2$) adds $m(L/2)^2 = \frac{1}{4}mL^2 = 3 I_{\text{cm}}$, **quadrupling** the rotational inertia to $I_{\text{pivot}} = \frac{1}{12}mL^2 + \frac{3}{12}mL^2 = \frac{1}{3}mL^2$.
* **Why Bicycle Frames, I-Beams & Helicopter Drive Shafts Hollow Out Their Cores:** When a solid steel shaft of radius $R$ twists under engine torque, the metal right along the central axis barely moves at all ($r \approx 0$), carrying almost zero shear stress while adding dead weight. Because a circular cross-section's area grows as $dA = 2\pi r\,dr$, integrating $r^2\,dA$ from an inner bore radius $R_i$ to an outer skin radius $R_o$ shows that the **polar moment of inertia** $J$ (which governs torsional stiffness, evaluated via `4 {{key:yˣ}}`) scales with the **fourth power** of the radius:
  $$J = \int_{R_i}^{R_o} r^2 (2\pi r\,dr) = \frac{\pi}{2}\left(R_o^4 - R_i^4\right)$$
  For a drive shaft of outer radius $R_o = 40\text{ mm}$, boring out an inner core of radius $R_i = 35\text{ mm}$ removes $(35/40)^2 = \mathbf{76.6\%}$ of the steel weight while sacrificing only $(35/40)^4 = 58.6\%$ of the solid shaft's stiffness—leaving a featherweight tube that retains **$41.4\%$** of the solid bar's torsional rigidity with less than a quarter of the mass! And for a hollow spherical pressure hull (like a deep-ocean titanium bathysphere bounded by inner radius $R_1$ and outer radius $R_2$), subtracting the inner sphere from the outer sphere scales with the **fifth power** of radius (`5 {{key:yˣ}}`):
  $$I_{\text{shell}} = \frac{2}{5} M \left(\frac{R_2^5 - R_1^5}{R_2^3 - R_1^3}\right)$$

---

## On the Stack: Solid Mensuration, Centroids & 3D Space Workbench

With Galileo's scaling laws, Cavalieri's cross-sectional slices, and Steiner's rotational inertia principles in hand, let us step up to the SC-32 workbench and put them into action. Across every multi-face enclosure, composite girder centroid, and multi-component flywheel below, the workflow follows the same rhythm: we evaluate each geometric primitive—a rectangle, a trapezoid, a circle, or an $mr^2$ inertia term—on the Four-Register Stack (`X, Y, Z, T`), while the hardware **Statistical Accumulator Bus** ($\Sigma x, \Sigma y, \Sigma xy, n$) acts as our dedicated geometric tally sheet—counting every face ($n = 1, 2, 3, \dots$), summing exterior areas via `{{key:Σ+}}`, deducting window cutouts via `{{key:Σ-}}`, and computing mass-weighted centroids via `{{key:x̄w}}` in a single continuous flow.

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
| **Parabolic Segment** | $A = \frac{2}{3} b h$ | $A = \frac{4}{3} A_{\text{triangle}}$ | Archimedes' exhaustion proof: $\frac{2}{3}$ of circumscribing box $bh$ (proved via geometric exhaustion in Chapter 8). |
| **Regular $n$-gon** | $A = \frac{1}{4} n s^2 \cot(\pi/n)$ | $A = \frac{1}{2} P \cdot r_{\text{in}}$ | Sum of $n$ congruent isosceles triangles radiating from the center. |
| **Cyclic Quadrilateral** | $A = \sqrt{(s-a)(s-b)(s-c)(s-d)}$ | $s = \frac{a+b+c+d}{2}$ | Brahmagupta's 628 CE theorem for any four-sided figure inscribed in a circle. |

For the complete reference tables of all 2D plane sections and perimeter formulas, consult **[Appendix D: Section 7 (Coordinate Geometry, Mensuration & 2D Curved Sections)](appendix-d-constants-and-equations.md)**.

Let us begin on the flat plane with our bolted ASME B16.5 neoprene pipe flange gasket—an **annulus** bounded by outer radius $R = 85.0\text{ mm}$ and inner bore radius $r = 50.0\text{ mm}$:

$$A = \pi (R^2 - r^2) = \pi (85^2 - 50^2) = \pi (7225 - 2500) = 4725\pi \approx \mathbf{14,844.0253\text{ mm}^2}$$

Keying `{{res:sc32_06_geometry_surface_area_seq_01:keys}}` computes the squared outer radius $R^2 = 7,225$ (`85 {{key:x²}}`), subtracts the squared inner bore $r^2 = 2,500$ (`50 {{key:x²}} {{key:-}}`) to leave $4,725.0\text{ mm}^2$ in Register $X$, and scales by `{{key:π}} {{key:×}}` to return **`{{res:sc32_06_geometry_surface_area_seq_01:value}}`** (**$14,844.03\text{ mm}^2$**, or $148.44\text{ cm}^2$). When $R \approx r$ in thin-walled pressure vessel shells, keying `R {{key:ENTER}} r {{key:-}} R {{key:ENTER}} r {{key:+}} {{key:×}} {{key:π}} {{key:×}}` evaluates the factored difference-of-squares $\pi(R-r)(R+r)$ directly.

For a regular octagonal sheet-metal face plate of edge length $s = 65.0\text{ mm}$ ($A = 2(1 + \sqrt{2})s^2 \approx 4.828427 \times 4225 = \mathbf{20,400.1047\text{ mm}^2}$), entering `{{res:sc32_06_geometry_surface_area_seq_02:keys}}` builds the silver-ratio octagonal multiplier $2(1 + \sqrt{2}) \approx 4.828427$ directly on the stack (`2 {{key:√x}} 1 {{key:+}} 2 {{key:×}}`), squares the edge length $s = 65\text{ mm}$ (`65 {{key:x²}}`), and multiplies (`{{key:×}}`) to yield **`{{res:sc32_06_geometry_surface_area_seq_02:value}}`** (**$20,400.10\text{ mm}^2$**).

To evaluate Earth's WGS-84 **reciprocal flattening** $1/f = a / (a - b) = 6378.137 / (6378.137 - 6356.752) \approx \mathbf{298.2572}$ without typing the 7-digit equatorial radius `6378.137` twice, the sequence `{{res:sc32_06_geometry_surface_area_seq_19:keys}}` duplicates $a$ into Register $Z$ on entry: keying `6378.137 {{key:ENTER}} {{key:ENTER}} 6356.752 {{key:-}}` forms $(a - b) = 21.385\text{ km}$ in Register $X$ while $a = 6,378.137\text{ km}$ drops into Register $Y$, and pressing `{{key:x⇄y}} {{key:÷}} {{key:1/x}}` resolves the reciprocal flattening **$298.2572$** (or in 8 strokes via $f = 1 - b/a$: `6356.752 {{key:ENTER}} 6378.137 {{key:÷}} 1 {{key:x⇄y}} {{key:-}} {{key:1/x}}`).

Now let us evaluate **Heron's formula** $A = \sqrt{s(s-a)(s-b)(s-c)}$ for our triangular land parcel with sides $a = 7.0\text{ m}$, $b = 9.0\text{ m}$, and $c = 12.0\text{ m}$:
1. **Compute and store the semiperimeter $s$:** Key `{{res:sc32_06_geometry_surface_area_seq_21:keys}}` (`7 {{key:ENTER}} 9 {{key:+}} 12 {{key:+}} 2 {{key:÷}}`) to obtain $s = 14.0\text{ m}$ in Register $X$, and store it via `{{key:STO}} S`.
2. **Accumulate the three $(s - \text{side})$ factors:** Since $s = 14.0$ is already in Register $X$, key `7 {{key:-}}` to get $(s - a) = 7.0$; then `{{key:RCL}} S 9 {{key:-}} {{key:×}}` to multiply by $(s - b) = 5.0$ ($\to 35.0$); then `{{key:RCL}} S 12 {{key:-}} {{key:×}}` to multiply by $(s - c) = 2.0$ ($\to 70.0$).
3. **Multiply by $s$ and extract the root:** Key `{{key:RCL}} S {{key:×}} {{key:√x}}` to evaluate $\sqrt{14.0 \times 70.0} = \sqrt{980.0} = \mathbf{31.304952\text{ m}^2}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `7 {{key:ENTER}} 9 {{key:+}} 12 {{key:+}} 2 {{key:÷}} {{key:STO}} S` | $0.0000$ | $0.0000$ | $0.0000$ | $14.0000$ | Semiperimeter $s = (a+b+c)/2$ stored in `S` |
| `7 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $7.0000$ | Factor $(s - a) = 14 - 7 = 7.0$ directly from $X$ |
| `{{key:RCL}} S 9 {{key:-}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $35.0000$ | Multiply by $(s - b) = 5.0$; subtotal $= 35.0$ |
| `{{key:RCL}} S 12 {{key:-}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $70.0000$ | Multiply by $(s - c) = 2.0$; subtotal $= 70.0$ |
| `{{key:RCL}} S {{key:×}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$31.304952$** | Multiply by $s$ and take root; Area $= 31.30\text{ m}^2$ |

For our right-angled structural channel with legs $a = 15.0\text{ cm}$ and $b = 20.0\text{ cm}$, the incircle radius $r = (a + b - c)/2$ evaluates directly on the stack:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `15 {{key:x²}} 20 {{key:x²}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $25.0000$ | Hypotenuse $c = \sqrt{a^2 + b^2}$ in cm |
| `15 {{key:ENTER}} 20 {{key:+}}` | $0.0000$ | $0.0000$ | $25.0000$ | $35.0000$ | Sum of orthogonal legs $a + b$ |
| `{{key:x⇄y}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | Excess tangent span $(a + b - c)$ |
| `2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$5.0000$** | Right triangle inradius $r = 5.0000\text{ cm}$ |

*(Speed-Calculation Tip: In timed mathematics competitions, you can replace the first row's five-keystroke Pythagorean sum `15 {{key:x²}} 20 {{key:x²}} {{key:+}} {{key:√x}}` with `15 {{key:ENTER}} 20 {{key:▸θ,r}}` (`Left Shift {{key:↰}} above {{key:4}}`), computing the hypotenuse $c = \sqrt{15^2 + 20^2} = 25.0000\text{ cm}$ in a single polar-conversion tap without squaring each leg separately!)*

---

### The Master Surface Area Technique via the Statistical Bus

On the SC-32, the **Statistical Accumulator (`{{key:Σ+}}`)** turns multi-face surface area takeoffs into an error-proof polygon tally:
1. Press `{{key:CLΣ}}` to clear the six statistical registers ($\Sigma x = 0, n = 0$).
2. Compute the area $A_1$ of your first face (or symmetric face pair) in Register $X$ and press `{{key:Σ+}}`. That adds $A_1$ into $\Sigma x$ and displays the face-group counter $n = 1.0000$ in Register $X$.
3. To deduct a window aperture or screw cutout—or undo a mistyped face—compute its area and press `{{key:Σ-}}`.
4. Press `{{key:SUMS}}` (Right Shift `{{key:↱}}` above `{{key:Σ+}}`) and tap `{{key:Σx}}` (`{{key:LFU0}}`) to recall the certified total surface area $\Sigma x$ into Register $X$.

Let us audit the total external surface area of the StackCalc SC-32 rectangular chassis ($L = 135\text{ mm}$, $W = 70\text{ mm}$, $H = 16\text{ mm}$), whose six walls form three opposing pairs ($2 \times 135 \times 70 = 18,900\text{ mm}^2$, $2 \times 135 \times 16 = 4,320\text{ mm}^2$, and $2 \times 70 \times 16 = 2,240\text{ mm}^2$). After `{{key:CLΣ}}`, we accumulate all three pairs:

| Keystroke | Register T | Register Z | Register Y | Register X | Accumulator $\Sigma x$ | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `135 {{key:ENTER}} 70 {{key:×}} 2 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $18900.0$ | $0.0$ | Top/Bottom area pair evaluated ($18,900.0\text{ mm}^2$) |
| `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$1.0$** | **$18900.0$** | $n=1$ in Register $X$; first pair accumulated into $\Sigma x$ |
| `135 {{key:ENTER}} 16 {{key:×}} 2 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $4320.0$ | $18900.0$ | Side walls area pair evaluated ($4,320.0\text{ mm}^2$) |
| `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$2.0$** | **$23220.0$** | $n=2$ in Register $X$; running area accumulated into $\Sigma x$ |
| `70 {{key:ENTER}} 16 {{key:×}} 2 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $2240.0$ | $23220.0$ | End caps area pair evaluated ($2,240.0\text{ mm}^2$) |
| `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$3.0$** | **$25460.0$** | $n=3$ in Register $X$; all 6 faces accumulated into $\Sigma x$ |
| `{{key:SUMS}} → Σx` | $0.0$ | $0.0$ | $0.0$ | **$25460.0000$** | $25460.0$ | Tap `{{key:Σx}}` (`{{key:LFU0}}`): total surface area recalled ($25,460.0\text{ mm}^2$) |

The same `{{key:Σ+}}` workflow tallies curved solids. For a cylindrical lithium battery compartment of radius $r = 15\text{ mm}$ and height $h = 65\text{ mm}$, we sum the two circular end caps ($2\pi r^2 = 450\pi \approx 1,413.7167\text{ mm}^2$) and the unrolled lateral wall ($2\pi r h = 1,950\pi \approx 6,126.1057\text{ mm}^2$):

| Keystroke | Register T | Register Z | Register Y | Register X | Accumulator $\Sigma x$ | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `15 {{key:x²}} {{key:π}} {{key:×}} 2 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $1413.716694$ | $0.0$ | Two circular end caps $2\pi r^2$ evaluated in $\text{mm}^2$ |
| `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$1.0$** | **$1413.716694$** | Accumulate end caps into $\Sigma x$; face-group count $n=1$ in $X$ |
| `2 {{key:π}} {{key:×}} 15 {{key:×}} 65 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $6126.105675$ | $1413.716694$ | Cylindrical lateral wall $2\pi r h$ evaluated in $\text{mm}^2$ |
| `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$2.0$** | **$7539.822369$** | Accumulate lateral wall into $\Sigma x$; face-group count $n=2$ in $X$ |
| `{{key:SUMS}} → Σx` | $0.0$ | $0.0$ | $0.0$ | **$7539.822369$** | $7539.822369$ | Tap `{{key:Σx}}` (`{{key:LFU0}}`): total cylinder surface area recalled ($7,539.82\text{ mm}^2$) |

What about a stepped cast-iron machine bracket consisting of a base block ($120 \times 80 \times 30\text{ mm}$) surmounted by a rectangular boss ($60 \times 40 \times 25\text{ mm}$)? Because the top face of the upper boss ($60 \times 40\text{ mm}$) plus the exposed horizontal ledge of the base block around it ($120 \times 80 - 60 \times 40\text{ mm}$) project together to form one complete $120 \times 80 = 9,600\text{ mm}^2$ top footprint, we tally all six face groups cleanly:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}} 120 {{key:ENTER}} 80 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Bottom face area $9,600.0\text{ mm}^2$ accumulated ($n=1$) |
| `120 {{key:ENTER}} 30 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | 2 base sides $7,200.0\text{ mm}^2$ accumulated ($n=2$) |
| `80 {{key:ENTER}} 30 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.0000$ | 2 base ends $4,800.0\text{ mm}^2$ accumulated ($n=3$) |
| `60 {{key:ENTER}} 25 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | 2 upper sides $3,000.0\text{ mm}^2$ accumulated ($n=4$) |
| `40 {{key:ENTER}} 25 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $5.0000$ | 2 upper ends $2,000.0\text{ mm}^2$ accumulated ($n=5$) |
| `120 {{key:ENTER}} 80 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $6.0000$ | Net top face area $9,600.0\text{ mm}^2$ accumulated ($n=6$) |
| `{{key:SUMS}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$36200.0000$** | Tap `{{key:Σx}}` (`{{key:LFU0}}`): recall total casting surface area $\Sigma x = 36,200.0\text{ mm}^2$ |

Now let us audit the **extruded aluminum heat sink** from our opening story: a $100 \times 100\text{ mm}$ square base plate carrying $8$ vertical cooling fins, each $100\text{ mm}$ long, $35\text{ mm}$ tall, and $2\text{ mm}$ thick. Decomposing the heat sink into $16$ vertical fin sides ($56,000\text{ mm}^2$), $8$ fin top tips ($1,600\text{ mm}^2$), the exposed valley floor ($8,400\text{ mm}^2$), and the flat bottom ($10,000\text{ mm}^2$) shows how the $8$ fins multiply the cooling area to **$76,000.0\text{ mm}^2$** ($3.8\times$ the bare plate):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}} 16 {{key:ENTER}} 100 {{key:×}} 35 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | 16 fin sides ($56,000.0\text{ mm}^2$) accumulated ($n=1$) |
| `8 {{key:ENTER}} 100 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | 8 fin tips ($1,600.0\text{ mm}^2$) accumulated ($n=2$) |
| `100 {{key:ENTER}} 100 {{key:×}} 1600 {{key:-}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.0000$ | Base exposed top ($8,400.0\text{ mm}^2$) accumulated ($n=3$) |
| `100 {{key:ENTER}} 100 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | Base flat bottom ($10,000.0\text{ mm}^2$) accumulated ($n=4$) |
| `{{key:SUMS}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$76000.0000$** | Tap `{{key:Σx}}` (`{{key:LFU0}}`): recall total heat sink surface area $\Sigma x = 76,000.0\text{ mm}^2$ |

For a park pavilion capped by a four-sided hipped pyramidal frustum roof (base $12\text{ m}$ square, top skylight curb $4\text{ m}$ square, and inclined slant height $s = 6.5\text{ m}$), each sloping roof plane is a trapezoid of area $A_{\text{face}} = \frac{1}{2}(12 + 4)\times 6.5 = 52.0\text{ m}^2$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Clear statistical accumulators |
| `12 {{key:ENTER}} 4 {{key:+}} 6.5 {{key:×}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $52.0000$ | Single trapezoidal face area $A_{\text{face}}$ in m² |
| `4 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | 4 lateral roof faces ($208.0\text{ m}^2$) accumulated ($n=1$) |
| `{{key:SUMS}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$208.0000$** | Tap `{{key:Σx}}` (`{{key:LFU0}}`): recall total pavilion roof surface area $\Sigma x = 208.0\text{ m}^2$ |

And for a regular right square pyramid of base side $s = 12.0\text{ mm}$ and altitude $h = 8.0\text{ mm}$ (where slant height $l = \sqrt{8^2 + 6^2} = 10.0\text{ mm}$, $A = 144 + 240 = 384.0\text{ mm}^2$, and $V = \frac{1}{3}(144)(8) = 384.0\text{ mm}^3$, because its inscribed sphere has radius $r_{\text{in}} = 3V/A = 3.0\text{ mm}$), we compute Galileo's surface-to-volume ratio $A/V = \mathbf{1.0000\text{ mm}^{-1}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `8 {{key:x²}} 12 {{key:ENTER}} 2 {{key:÷}} {{key:x²}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | Slant height $l = \sqrt{h^2 + (s/2)^2}$ |
| `2 {{key:×}} 12 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $240.0000$ | 4 lateral triangular faces $A_{\text{lat}}$ |
| `12 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $384.0000$ | Total pyramid surface area $A$ |
| `12 {{key:x²}} 8 {{key:×}} 3 {{key:÷}}` | $0.0000$ | $0.0000$ | $384.0000$ | $384.0000$ | Pyramid volume $V = s^2 h / 3$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1.0000$** | Surface-to-volume ratio $A/V$ |

---

### 3D Volumes, Conical Frustums, Spherical Caps & Girard's Excess

| 3D Solid Geometry | Analytical Volume Formula | Total External Surface Area Formula | Geometric Origin & Physical Meaning |
| :--- | :--- | :--- | :--- |
| **Rectangular Prism** | $V = l \cdot w \cdot h$ | $A = 2(lw + lh + wh)$ | Extrusion of rectangle $lw$ along $h$; 6 orthogonal faces. |
| **Right Circular Cylinder** | $V = \pi r^2 h$ | $A = 2\pi r^2 + 2\pi r h$ | Extrusion of circular disk $\pi r^2$ along normal axis $h$. |
| **Right Circular Cone** | $V = \frac{1}{3} \pi r^2 h$ | $A = \pi r^2 + \pi r \sqrt{r^2 + h^2}$ | Exactly $\frac{1}{3}$ of bounding cylinder (Eudoxus & Archimedes). |
| **Sphere** | $V = \frac{4}{3} \pi r^3$ | $A = 4\pi r^2 = \frac{dV}{dr}$ | Exactly $\frac{2}{3}$ of circumscribing cylinder in both $V$ and $A$. |
| **Torus (Major $R$, minor $r$)** | $V = 2\pi^2 R r^2$ | $A = 4\pi^2 R r$ | **Pappus-Guldinus:** Centroid orbit ($2\pi R$) $\times$ disk area ($\pi r^2$) or circumference ($2\pi r$). |
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

For the complete reference catalog of 3D solid mensuration formulas, consult **[Appendix D: Section 8 (3D Solid Mensuration & Revolution Geometry)](appendix-d-constants-and-equations.md)**.

Let us evaluate our three-dimensional solids on the stack:

1. **Elliptic Nose Cone ($a = 24.0\text{ mm}, b = 15.0\text{ mm}, h = 50.0\text{ mm}$):** By Cavalieri's Principle, $V = \frac{1}{3}\pi abh = 6000\pi \approx \mathbf{18,849.5559\text{ mm}^3}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `24 {{key:ENTER}} 15 {{key:×}} 50 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $18000.0000$ | Product $a \cdot b \cdot h$ evaluated |
| `{{key:π}} {{key:×}} 3 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$18849.555922$** | Elliptic cone volume $V$ in mm³ |

2. **Steinmetz Bicylinder ($r = 15.0\text{ mm}$):** Evaluating `16 {{key:ENTER}} 3 {{key:÷}} 15 {{key:ENTER}} 3 {{key:yˣ}} {{key:×}}` yields the exact rational volume $V = \frac{16}{3}r^3 = \mathbf{18,000.0\text{ mm}^3}$, and `15 {{key:x²}} 16 {{key:×}}` gives the surface area $A = 16r^2 = \mathbf{3,600.0\text{ mm}^2}$.
3. **Conical Frustum Grain Hopper ($R = 1.80\text{ m}, r = 0.40\text{ m}, h = 2.50\text{ m}$):** Watch how `{{key:LASTX}}` in the sequence `{{res:sc32_06_geometry_surface_area_seq_04:keys}}` evaluates $V = \frac{1}{3}\pi h(R^2 + Rr + r^2)$ while typing `1.8` and `0.4` only once each: keying `1.8 {{key:x²}} {{key:LASTX}} 0.4 {{key:×}} {{key:LASTX}} {{key:x²}} {{key:+}} {{key:+}} {{key:π}} {{key:×}} 2.5 {{key:×}} 3 {{key:÷}}` forms $R^2 + Rr + r^2 = 4.12\text{ m}^2$ in Register $X$ and scales by $\frac{2.5\pi}{3}$ to produce **`{{res:sc32_06_geometry_surface_area_seq_04:value}}`** (**$10.7861\text{ m}^3$**).
4. **Hollow Hexagonal Brass Bar ($S = 20.0\text{ mm}, s = 8.0\text{ mm}, L = 150.0\text{ mm}$):** With hexagon shape constant $C_6 = \frac{3\sqrt{3}}{2}$, entering `{{res:sc32_06_geometry_surface_area_seq_20:keys}}` computes $V_{\text{net}} = \frac{3\sqrt{3}}{2}(S^2 - s^2)L = \mathbf{130,943.04\text{ mm}^3}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `20 {{key:x²}} 8 {{key:x²}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $336.0000$ | Hexagonal span difference $(S^2 - s^2)$ |
| `3 {{key:√x}} {{key:×}} 3 {{key:×}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $872.953607$ | Net hexagonal cross section $A_{\text{net}}$ in mm² |
| `150 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$130943.041071$** | Prismatic net volume $V_{\text{net}} = A_{\text{net}} \cdot L$ in mm³ |

   *(For a solid steel hex bolt head of side $s = 10.0\text{ mm}$, height $h = 12.0\text{ mm}$, and density $\rho = 7.85\text{ g/cm}^3$, keying `3 {{key:√x}} {{key:LASTX}} {{key:×}} 2 {{key:÷}} 10 {{key:x²}} {{key:×}} 12 {{key:×}} 1000 {{key:÷}} 7.85 {{key:×}}` gives mass **$24.4739\text{ grams}$**.)*
5. **Regular Tetrahedron ($a = 50.0\text{ mm}$):** Keying `{{res:sc32_06_geometry_surface_area_seq_11:keys}}` evaluates $V = \frac{\sqrt{2}}{12}a^3 = \frac{\sqrt{2}}{12}(125,000)$ via `2 {{key:√x}} 12 {{key:÷}} 50 {{key:ENTER}} 3 {{key:yˣ}} {{key:×}}` to return **`{{res:sc32_06_geometry_surface_area_seq_11:value}}`** (**$14,731.39\text{ mm}^3$**).
6. **Parachute Spherical Lune ($R = 25.0\text{ cm}, \theta = 36.0^\circ$):** Covering $\frac{36^\circ}{360^\circ} = 0.10$ of the sphere's area $4\pi R^2$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `25 {{key:x²}} 4 {{key:×}} {{key:π}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $7853.981634$ | Full sphere surface area $4\pi R^2$ in cm² |
| `36 {{key:ENTER}} 360 {{key:÷}}` | $0.0000$ | $0.0000$ | $7853.981634$ | $0.100000$ | Dihedral angle fraction $36^\circ / 360^\circ$ |
| `{{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$785.398163$** | Spherical lune area $A_{\text{lune}}$ in cm² |

7. **Albert Girard's Continental Spherical Triangle ($R = 6,371.0\text{ km},\; \alpha = 82.5^\circ, \beta = 68.2^\circ, \gamma = 44.7^\circ$):** With spherical excess $E = 195.4^\circ - 180^\circ = 15.4^\circ \approx 0.268781\text{ rad}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `82.5 {{key:ENTER}} 68.2 {{key:+}} 44.7 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $195.4000$ | Interior angle sum $\alpha + \beta + \gamma$ in degrees |
| `180 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $15.4000$ | Spherical excess $E = 15.4^\circ$ |
| `{{key:π}} {{key:×}} 180 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.268781$ | Excess in radians $E_{\text{rad}} \approx 0.268781\text{ rad}$ |
| `6371 {{key:x²}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$10911102.50$** | Spherical triangle area $A = R^2 E_{\text{rad}}$ in km² |

8. **Hortonsphere Spherical Cap ($R = 4.0\text{ m}, h = 1.5\text{ m}$):** Running `{{res:sc32_06_geometry_surface_area_seq_07:keys}}` forms $(3R - h) = 10.5\text{ m}$ via `4 {{key:ENTER}} 3 {{key:×}} 1.5 {{key:-}}`, recovers $h = 1.5\text{ m}$ from `LASTX` and squares it (`{{key:LASTX}} {{key:x²}} {{key:×}}`), and scales by `{{key:π}} {{key:×}} 3 {{key:÷}}` to deliver **`{{res:sc32_06_geometry_surface_area_seq_07:value}}`** (**$24.7400\text{ m}^3$**).
9. **Knud Thomsen's Asteroid Surface Area ($a = 15.0\text{ km}, b = 10.0\text{ km}, c = 6.0\text{ km}$):** With $ab = 150, ac = 90, bc = 60$ and $p = 1.6075$, keying `150 {{key:ENTER}} 1.6075 {{key:yˣ}} 90 {{key:LASTX}} {{key:yˣ}} 60 {{key:LASTX}} {{key:yˣ}} {{key:+}} {{key:+}} 3 {{key:÷}} 1.6075 {{key:1/x}} {{key:yˣ}} 4 {{key:×}} {{key:π}} {{key:×}}` uses `{{key:LASTX}}` to reuse the exponent $1.6075$, returning **$1,308.90\text{ km}^2$**.

---

### 3D Helical Coils, Direction Cosines, Weighted Centroids & Moments of Inertia

For our tapered conical compression spring ($R_1 = 30\text{ mm}, R_2 = 10\text{ mm}, R_m = 20\text{ mm}, h = 60\text{ mm}, N = 6\text{ coils}$), we sum the three squared orthogonal displacements $L = \sqrt{(2\pi N R_m)^2 + h^2 + (R_1 - R_2)^2}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2 {{key:π}} {{key:×}} 6 {{key:×}} 20 {{key:×}} {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $568489.2130$ | Developed circumferential metric $(2\pi N R_m)^2$ |
| `60 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $572089.2130$ | Accumulate axial rise component $h^2$ |
| `30 {{key:ENTER}} 10 {{key:-}} {{key:x²}}` | $0.0000$ | $0.0000$ | $572089.2130$ | $400.0000$ | Radial taper variance $(R_1 - R_2)^2$ |
| `{{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$756.6302$** | Total developed conical coil length ($756.63\text{ mm}$) |

For a deep-space radar tracking an ascending launch vehicle at $\vec{V} = (850, 1100, 550)\text{ m}$ ($|\vec{V}| = 1,494.9916\text{ m}$), executing `{{res:sc32_06_geometry_surface_area_seq_13:keys}}` stores the norm $D = 1494.9916\text{ m}$ in Variable `D` and divides each coordinate, leaving all three direction cosines arrayed across the stack as $(Z = 0.568565,\; Y = 0.735790,\; X = $ **`{{res:sc32_06_geometry_surface_area_seq_13:value}}`** $)$.

To locate the composite neutral axis $\bar{y} = \frac{\sum m_i y_i}{\sum m_i}$ of a welded steel girder built from three horizontal plates ($m_1 = 40\text{ kg}$ at $y_1 = 10\text{ mm}$; $m_2 = 60\text{ kg}$ at $y_2 = 160\text{ mm}$; $m_3 = 30\text{ kg}$ at $y_3 = 310\text{ mm}$), we clear statistics (`{{key:CLΣ}}`), load each plate's mass $m_i$ into Register $Y$ and height $y_i$ into Register $X$, press `{{key:Σ+}}`, and open `{{key:x̄,ȳ}}` (`Right Shift {{key:↱}} above {{key:yˣ}}`) to tap the **Weighted Mean (`{{key:x̄w}}`, `{{key:LFU2}}`)**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0.0$ | $0.0$ | $0.0$ | $0.0$ | Clear all 6 statistical accumulators |
| `40 {{key:ENTER}} 10 {{key:Σ+}}` | $0.0$ | $0.0$ | $40.0$ | $1.0$ | Log bottom flange ($m_1=40\text{ kg}, y_1=10\text{ mm};\; n=1$) |
| `60 {{key:ENTER}} 160 {{key:Σ+}}` | $0.0$ | $40.0$ | $60.0$ | $2.0$ | Log web section ($m_2=60\text{ kg}, y_2=160\text{ mm};\; n=2$) |
| `30 {{key:ENTER}} 310 {{key:Σ+}}` | $40.0$ | $60.0$ | $30.0$ | $3.0$ | Log top flange ($m_3=30\text{ kg}, y_3=310\text{ mm};\; n=3$) |
| `{{key:x̄w}}` | $40.0$ | $60.0$ | $30.0$ | **$148.461538$** | Via `{{key:x̄,ȳ}}` $\to$ `{{key:x̄w}}`: weighted centroid $\bar{y} = 148.4615\text{ mm}$ |

Finally, let us trace our four rotational and polar moment of inertia benchmarks:

1. **Composite Cast-Iron Flywheel ($M_{\text{rim}} = 65\text{ kg}, r_1 = 0.28\text{ m}, r_2 = 0.35\text{ m}$; $M_{\text{web}} = 20\text{ kg}, R = 0.28\text{ m}$):** Evaluating `{{res:sc32_06_geometry_surface_area_seq_16:keys}}` yields **`{{res:sc32_06_geometry_surface_area_seq_16:value}}`** ($I_{\text{total}} = \mathbf{7.31325\text{ kg}\cdot\text{m}^2}$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0.28 {{key:x²}} 0.35 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.200900$ | Evaluate inner and outer squared radii sum $r_1^2 + r_2^2$ |
| `65 {{key:×}} 2 {{key:÷}} {{key:STO}} A` | $0.0000$ | $0.0000$ | $0.0000$ | $6.529250$ | Compute annular rim inertia $I_{\text{rim}}$ and store in Variable A |
| `0.28 {{key:x²}} 20 {{key:×}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $6.529250$ | $0.784000$ | Evaluate solid inner web disk inertia $I_{\text{web}} = \frac{1}{2}M_{\text{web}}R^2$ |
| `{{key:RCL}} A {{key:+}}` | $0.0000$ | $0.0000$ | $6.529250$ | **$7.313250$** | Add $I_{\text{rim}} + I_{\text{web}}$ for total flywheel inertia in $\text{kg}\cdot\text{m}^2$ |

2. **Steiner's Parallel-Axis Theorem on a Robotic Arm Link ($m = 3.5\text{ kg}, L = 0.80\text{ m}, d = 0.40\text{ m}$):** Keying `{{res:sc32_06_geometry_surface_area_seq_17:keys}}` returns **`{{res:sc32_06_geometry_surface_area_seq_17:value}}`** ($I_{\text{pivot}} = I_{\text{cm}} + md^2 = \mathbf{0.746667\text{ kg}\cdot\text{m}^2}$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0.80 {{key:x²}} 3.5 {{key:×}} 12 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.186667$ | Center-of-mass inertia $I_{\text{cm}}$ |
| `0.40 {{key:x²}} 3.5 {{key:×}}` | $0.0000$ | $0.0000$ | $0.186667$ | $0.560000$ | Steiner transfer term $m d^2$ |
| `{{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.746667$** | Offset pivot inertia $I_{\text{pivot}}$ |

3. **Titanium Bathysphere Pressure Hull ($R_2 = 1.10\text{ m}, R_1 = 0.98\text{ m}, M = 7,347.74\text{ kg}$):** Here the hull mass $M = 7,347.74\text{ kg}$ is the mass of the Ti-6Al-4V titanium alloy spherical shell ($\rho = 4,500\text{ kg/m}^3$ multiplied by the shell volume $V_{\text{shell}} = \frac{4}{3}\pi(R_2^3 - R_1^3) = 1.63283\text{ m}^3$; note that when the alloy density $\rho$ is given directly rather than total mass $M$, substituting $M = \frac{4}{3}\pi\rho(R_2^3 - R_1^3)$ cancels the cubic factor $(R_2^3 - R_1^3)$ completely, leaving the one-step formula $I = \frac{8}{15}\pi\rho(R_2^5 - R_1^5)$!). Evaluating $I = \frac{2}{5}M\frac{R_2^5 - R_1^5}{R_2^3 - R_1^3}$ from the known mass $M$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1.1 {{key:ENTER}} 5 {{key:yˣ}} 0.98 {{key:ENTER}} 5 {{key:yˣ}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.706589$ | Fifth-power difference $(R_2^5 - R_1^5)$ |
| `1.1 {{key:ENTER}} 3 {{key:yˣ}} 0.98 {{key:ENTER}} 3 {{key:yˣ}} {{key:-}}` | $0.706589$ | $0.706589$ | $0.706589$ | $0.389808$ | Third-power difference $(R_2^3 - R_1^3)$ |
| `{{key:÷}}` | $0.706589$ | $0.706589$ | $0.706589$ | $1.812660$ | Ratio $(R_2^5 - R_1^5)/(R_2^3 - R_1^3)$ |
| `7347.74 {{key:×}} 2 {{key:×}} 5 {{key:÷}}` | $0.706589$ | $0.706589$ | $0.706589$ | **$5327.4160$** | Mass moment of inertia $I$ in $\text{kg}\cdot\text{m}^2$ |

4. **Hollow Steel Drive Shaft Polar Moment of Inertia ($R_o = 40\text{ mm}, R_i = 35\text{ mm}$):** Evaluating $J = \frac{\pi}{2}(R_o^4 - R_i^4)$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `40 {{key:ENTER}} 4 {{key:yˣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2560000.0000$ | Outer radius fourth power $R_o^4$ |
| `35 {{key:ENTER}} 4 {{key:yˣ}}` | $0.0000$ | $0.0000$ | $2560000.0000$ | $1500625.0000$ | Inner radius fourth power $R_i^4$ |
| `{{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1059375.0000$ | Difference $(R_o^4 - R_i^4)$ in mm⁴ |
| `{{key:π}} {{key:×}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1664071.7612$** | Polar moment of inertia $J$ in mm⁴ |

Always remember three operational habits when auditing geometry on the stack: clear statistical memory with `{{key:CLΣ}}` before starting any new multi-face or centroid tally; remember that Heron's formula signals `INVALID DATA` (Code 02, cleared with `{{key:C}}`) if a misread caliper measurement violates the triangle inequality ($a + b \le c$); and always halve blueprint bore diameters ($D \to R = D/2$) before squaring or cubing so you never introduce a four-fold or eight-fold scaling error.

---

### When the Unknown Refuses to Sit Alone

Notice a quiet luxury we enjoyed across every geometric formula in this chapter. Whether we wanted the area of an octagon, the volume of a conical frustum, the surface area of an asteroid, or the rotational inertia of a bathysphere, the unknown quantity we were looking for—$A$, $V$, $\bar{y}$, or $I$—always sat **alone on the left-hand side of the equals sign**. All we had to do was combine the known dimensions on the right-hand side.

What happens when we turn one of Archimedes' formulas inside out? Suppose you already know the volume of water displaced by a floating oak sphere of radius $R = 0.50\text{ m}$, and you want to solve for the depth $h$ to which the sphere sinks inside the spherical cap formula $V = \frac{1}{3}\pi h^2(3R - h)$. Suddenly, the unknown depth $h$ is no longer sitting alone—it is tangled up in both a squared term $h^2$ and a cubed term $h^3$:

$$h^3 - 3R h^2 + \frac{3V}{\pi} = 0$$

Worse still, what if the unknown $x$ is trapped on both sides of a logarithm or a sine wave, where no algebraic manipulation on Earth can isolate it? In **[Chapter 7: The Scandal of the Cubic & The Art of Hunting Roots](07-polynomials-brent-solver.md)**, we step into one of the most dramatic detective stories in the history of mathematics—from a ninth-century court scholar completing physical squares in Baghdad and a high-stakes sixteenth-century public duel in Milan over the secret of the cubic, to the modern hybrid root-finding engine that hunts down any unknown to twelve decimal places.
