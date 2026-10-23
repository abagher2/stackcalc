---
title: "Chapter 6: Analytic & Solid Geometry, Surface Area & Mensuration | Thinking in the Stack (SC-32)"
description: "Master 2D plane area, conic sections, the master Surface Area via Stats Mode ([Σ+]) technique, solid mensuration, moments of inertia, and 3D Euclidean metrics on the StackCalc SC-32."
---

# Chapter 6: Analytic & Solid Geometry, Surface Area & Mensuration

## The Heat Sink, the Rocket Nozzle & Surface-to-Volume Scaling

In his 1638 treatise *Two New Sciences* (*Discorsi e dimostrazioni matematiche intorno a due nuove scienze*) {{cite:galilei1638}}, **Galileo Galilei** formulated the geometric **Square-Cube Law**: scaling any physical body by a linear factor $\ell$ multiplies its heat-dissipating and load-bearing surface area by the square ($\ell^2$) while multiplying its heat-generating volume and mass by the cube ($\ell^3$). Across biology, thermodynamics, aerodynamic friction, chemical catalysis, and semiconductor cooling, that $A/V \propto \ell^2 / \ell^3 = 1/\ell$ scaling asymmetry is the governing physical bottleneck.

Inside a modern high-performance microprocessor, billions of nanometer-scale transistors switch at gigahertz frequencies, generating localized thermal flux exceeding $100\text{ W/cm}^2$ {{cite:incropera2007}}—a power density approaching the heat flux inside a nuclear reactor core. Under Fourier's Law of Thermal Conduction and Newton's Law of Cooling {{cite:incropera2007}}, convective heat removal from a solid boundary to an ambient fluid is governed by:

$$\dot{Q} = h \cdot A_{\text{surface}} \cdot (T_{\text{solid}} - T_{\text{fluid}})$$

Because the heat dissipation rate $\dot{Q}$ is directly proportional to exposed surface area $A_{\text{surface}}$, inadequate boundary area causes internal junction temperatures to soar. This physical law links microprocessor pin-fin heat sinks directly to biological thermoregulation across the animal kingdom:
* **Why Hummingbirds Enter Torpor While Elephants Grow Ear-Fins:** A $3\text{-gram}$ **ruby-throated hummingbird** ($\ell \approx 2\text{ cm}$) has a massive surface-area-to-volume ratio ($A/V \propto 1/\ell$), radiating body heat so rapidly relative to its tiny thermal mass that its heart must beat $1,200\text{ times per minute}$ by day and plunge into deep hypothermic **torpor** at night to avoid starving. Conversely, a $5,000\text{-kilogram}$ **African elephant** ($\ell \approx 200\text{ cm}$—a $100\times$ linear scale-up that multiplies heat-producing volume by $100^3 = 1,000,000\times$ while multiplying skin area by only $100^2 = 10,000\times$) has $1/100\text{th}$ the relative cooling surface and would fatally overheat without pumping blood through huge, thin, vascularized **ear-fins**.
* **Extruded Silicon Heat Sinks:** A high-power microprocessor faces the exact elephant bottleneck: machining or extruding aluminum into dozens of parallel fins adds no volume—in fact, it removes material—yet it multiplies the effective convective surface area by more than $2,500\%$.

In real-world aerospace enclosures and consumer instruments, geometry is never composed of tidy textbook cubes. Enclosures feature drafted mold tooling angles, filleted stress-relief radii, cylindrical fastener bosses, and compound chamfers. Rather than scribbling fragile intermediate area calculations across scratch paper, the engineer audits the physical artifact polygon by polygon directly on the RPN stack:
* Primary exterior faces accumulate into the statistical bus via `{{key:Σ+}}`.
* Internal mounting apertures, screw countersinks, and display cutouts subtract via `{{key:Σ-}}`.
* The LCD counter ($n = 1, 2, 3 \dots$) tracks every verified face.
* Recalling `{{key:SUMS}}` → `Σx` instantly produces the certified boundary surface area.

---

{{res:sc32_surface_area_sigma:screenshot|Surface area of 10x5x4 prism accumulated via Sigma+ → 220}}

## From Caliper Datums to the Statistical Accumulator Bus

Every spatial mensuration problem begins with physical geometry: measuring the exterior length, width, height, and wall thickness of a machined enclosure, a truncated cone frustum, or a polyhedral truss with vernier calipers. Rather than transcribing individual face measurements onto paper and keying a fragile chain of parenthesized products, the StackCalc SC-32 maps each physical face directly onto the **Statistical Accumulator Bus (`{{key:Σ+}}`)**.

As you compute the area of each boundary face in Register $X$, pressing `{{key:Σ+}}` adds that face area into the dedicated $\Sigma x$ summation register while incrementing the face counter $n$ in Register $X$ ($n = 1, 2, 3, \dots$). You can inspect the running face count on the transflective LCD after every step, recall the accumulated total surface area via `{{key:Σx}}`, and extend the same 4-register pipeline to three-dimensional Euclidean norms $d = \sqrt{\Delta x^2 + \Delta y^2 + \Delta z^2}$ and parallel-axis moments of inertia $I = I_{\text{cm}} + md^2$.

{{blocks:sc32_utility_ortho|SC-32 Chassis Technical Drafting Orthographic Projections}}
*Figure 6.1: Technical drafting orthographic projections of the SC-32 handheld chassis ($135 \times 70 \times 16\,\text{mm}$), establishing the datum faces and boundary walls evaluated across the statistical accumulator bus.*

---

## 2D Plane Geometry, Regular Polygons & Conic Sections

Before accumulating three-dimensional bounding surfaces, we establish the planar area and perimeter primitives that govern individual cross-sections, machine flanges, polygon blanks, and conic slices.

### 2D Plane Area Primitives & Difference-of-Squares Annuli
The SC-32 evaluates 2D plane geometric regions using rapid, parenthesis-free RPN keystroke pipelines. In high-speed STEM tournaments and engineering analysis, these primitives collapse multi-step trigonometric and radical reductions into continuous tactile reductions:

| Geometric Region | Analytical Area Formula | Physical & Geometric Motivation | RPN Keystroke Pipeline |
| :--- | :--- | :--- | :--- |
| **Rectangle** | $A = l \times w$ | Orthogonal Cartesian product of orthogonal basis vectors. | `l {{key:ENTER}} w {{key:×}}` |
| **Triangle (Base/Height)** | $A = \frac{1}{2} b \times h$ | Half of the circumscribing parallelogram. | `b {{key:ENTER}} h {{key:×}} 2 {{key:÷}}` |
| **Circle** | $A = \pi r^2$ | Integration of concentric infinitesimal rings ($dA = 2\pi r dr$). | `r {{key:x²}} {{key:π}} {{key:×}}` |
| **Circular Sector** | $A = \frac{1}{2} r^2 \theta$ ($\theta$ in rad) | Fractional aperture $(\theta / 2\pi)$ scaled to full circle area $\pi r^2$. | `r {{key:x²}} θ {{key:×}} 2 {{key:÷}}` |
| **Circular Segment** | $A = \frac{1}{2} r^2 (\theta - \sin\theta)$ | Sector area minus triangular chord core ($\frac{1}{2} r^2 \sin\theta$). | `θ {{key:ENTER}} {{key:SIN}} {{key:-}} r {{key:x²}} {{key:×}} 2 {{key:÷}}` |
| **Circular Annulus** | $A = \pi (R^2 - r^2) = \pi(R-r)(R+r)$ | Difference of concentric disks; factored via difference-of-squares. | `R {{key:ENTER}} r {{key:-}} R {{key:ENTER}} r {{key:+}} {{key:×}} {{key:π}} {{key:×}}` |
| **Trapezoid** | $A = \frac{1}{2} (a + b) h$ | Average parallel base length multiplied by perpendicular altitude. | `a {{key:ENTER}} b {{key:+}} h {{key:×}} 2 {{key:÷}}` |
| **Ellipse** | $A = \pi a b$ | Area under 2D affine scaling of unit circle by semimajor axes $a, b$. | `a {{key:ENTER}} b {{key:×}} {{key:π}} {{key:×}}` |
| **Parabolic Segment** | $A = \frac{2}{3} b h$ | Archimedes' quadrature: segment is exactly $\frac{4}{3}$ of inscribed triangle. | `b {{key:ENTER}} h {{key:×}} 2 {{key:×}} 3 {{key:÷}}` |
| **Regular $n$-gon** | $A = \frac{1}{4} n s^2 \cot(\pi/n)$ | Decomposition into $n$ congruent central isosceles triangles. | `{{key:π}} n {{key:÷}} {{key:TAN}} {{key:1/x}} s {{key:x²}} {{key:×}} n {{key:×}} 4 {{key:÷}}` |
| **Cyclic Quadrilateral** | $A = \sqrt{(s-a)(s-b)(s-c)(s-d)}$ | Brahmagupta's formula: 4-term cyclic extension of Heron's formula. | Four stack factors multiplied inside-out $\to$ `{{key:√x}}` |

For the master quick-reference tables of all 2D plane sections and perimeter formulas, consult **[Appendix D: Section 7 (Coordinate Geometry, Mensuration & 2D Curved Sections)](appendix-d-constants-and-equations.md)**.

Notice how factoring a circular ring (annulus) simplifies pipe-flange and pressure-vessel calculations. When bolting together an ASME B16.5 high-pressure flange joint, the required bolt preload depends on the seating contact area of the ring-shaped neoprene gasket—an **annulus** bounded by outer radius $R = 85.0\text{ mm}$ and inner pipe bore radius $r = 50.0\text{ mm}$. Rather than multiplying by $\pi$ twice ($\pi R^2 - \pi r^2$), we factor $\pi$ outside the difference of squares:

$$A = \pi (R^2 - r^2) = \pi (85^2 - 50^2) = \pi (7225 - 2500) = 4725\pi \approx \mathbf{14,844.0253\text{ mm}^2}$$

Keying `{{res:sc32_06_geometry_surface_area_seq_01:keys}}` computes the squared outer radius $R^2 = 7,225$ (`85 {{key:x²}}`), subtracts the squared inner bore $r^2 = 2,500$ (`50 {{key:x²}} {{key:-}}`) to leave $4,725.0\text{ mm}^2$ in Register $X$, and scales by `{{key:π}} {{key:×}}` to return **`{{res:sc32_06_geometry_surface_area_seq_01:value}}`** (**$14,844.03\text{ mm}^2$**, or $148.44\text{ cm}^2$). Better still, when $R \approx r$ in thin-walled pressure vessel shells, keying `R {{key:ENTER}} r {{key:-}} R {{key:ENTER}} r {{key:+}} {{key:×}} {{key:π}} {{key:×}}` avoids squaring two nearly equal numbers and preserves full floating-point precision.

What if an enclosure cover is a regular polygon rather than a circular flange? How do you find the area of a regular octagonal sheet-metal face plate of edge length $s = 65.0\text{ mm}$ without looking up trigonometric cotangents? Picture a regular octagon as a bounding square of width $(1 + \sqrt{2})s$ with four $45^\circ$ right-isosceles corner triangles of leg $s/\sqrt{2}$ clipped off the four corners. Subtracting those four corner triangles leaves $A = 2(1 + \sqrt{2})s^2 = 2\delta_S s^2$, where $\delta_S = 1 + \sqrt{2} \approx 2.414214$ is the **silver ratio**:

$$A = 2 (1 + \sqrt{2}) s^2 \approx 4.828427 \times 65^2 = 4.828427 \times 4225 = \mathbf{20,400.1047\text{ mm}^2}$$

Entering `{{res:sc32_06_geometry_surface_area_seq_02:keys}}` builds the octagonal shape multiplier $2(1 + \sqrt{2}) \approx 4.828427$ directly on the stack (`2 {{key:√x}} 1 {{key:+}} 2 {{key:×}}`), squares the edge length $s = 65\text{ mm}$ (`65 {{key:x²}}`), and multiplies (`{{key:×}}`) to yield **`{{res:sc32_06_geometry_surface_area_seq_02:value}}`** (**$20,400.10\text{ mm}^2$**).

### Ramanujan's Ellipse Perimeter & Planetary Oblateness

One of the great surprises of classical geometry is that while the *area* of an ellipse with semi-axes $(a, b)$ is the effortless product $A = \pi a b$ (a circle of radius $b$ stretched along one axis by $a/b$), its *perimeter* has no closed-form expression in elementary functions! Measuring the arc length of an ellipse requires evaluating a complete elliptic integral of the second kind—which is where elliptic integrals got their name.

In 1914, Indian mathematician Srinivasa Ramanujan published a remarkable algebraic approximation that achieves sub-parts-per-million accuracy across nearly all engineering eccentricities by defining the dimensionless flattening parameter $h = \frac{(a - b)^2}{(a + b)^2}$:
$$h = \frac{(a - b)^2}{(a + b)^2}, \qquad P \approx \pi (a + b) \left[ 1 + \frac{3h}{10 + \sqrt{4 - 3h}} \right]$$
On the SC-32 stack, Ramanujan's nested radical evaluates from the inside out without a single parenthesis: form $h = ((a - b)/(a + b))^2$, evaluate $\sqrt{4 - 3h}$ in Register $X$, add $10$ and invert via `{{key:1/x}}`, multiply by $3h$, add $1$, and scale by $\pi(a + b)$.

That same axial difference $(a - b)$ governs planetary geodesy. Because the Earth spins once every $23\text{ hr } 56\text{ min}$, centrifugal acceleration bulges the equator to $a = 6,378.137\text{ km}$ compared to the polar semi-minor axis $b = 6,356.752\text{ km}$—an equatorial bulge of $a - b = 21.385\text{ km}$. Geodesists specify this oblateness by the **reciprocal flattening** $1/f = a / (a - b)$:

$$\text{Flattening } f = \frac{a - b}{a} = 1 - \frac{b}{a} = \frac{6378.137 - 6356.752}{6378.137} = \frac{21.385}{6378.137} \approx \mathbf{\frac{1}{298.2572}}$$

Rather than typing the 7-digit equatorial radius `6378.137` twice, the sequence `{{res:sc32_06_geometry_surface_area_seq_19:keys}}` duplicates $a$ into Register $Z$ on entry: keying `6378.137 {{key:ENTER}} {{key:ENTER}} 6356.752 {{key:-}}` forms $(a - b) = 21.385\text{ km}$ in Register $X$ while $a = 6,378.137\text{ km}$ drops into Register $Y$, and pressing `{{key:x⇄y}} {{key:÷}} {{key:1/x}}` resolves the reciprocal flattening **$298.2572$**—or even more compactly in just 8 keystrokes by rewriting $f = 1 - b/a$ so each radius is entered only once: `6356.752 {{key:ENTER}} 6378.137 {{key:÷}} 1 {{key:x⇄y}} {{key:-}} {{key:1/x}}` ($\to \mathbf{298.2528}$ for the three-decimal polar radius $b = 6356.752\text{ km}$).

### Heron's Formula & Right-Triangle Incircles

When a surveyor or structural engineer measures the three side lengths $(a, b, c)$ of a triangular gusset plate or land parcel, finding a perpendicular altitude $h$ by trigonometry takes extra steps. In the 1st century CE, **Heron of Alexandria** showed in his *Metrica* that the area of any triangle follows directly from its **semiperimeter** $s = (a + b + c)/2$ alone:
$$s = \frac{a + b + c}{2}, \qquad A = \sqrt{s(s - a)(s - b)(s - c)}$$

Suppose a triangular parcel has sides $a = 7.0\text{ m}$, $b = 9.0\text{ m}$, and $c = 12.0\text{ m}$. Watch how storing $s$ in Variable `S` lets you build the four-factor product cleanly on the stack:
1. **Compute and store the semiperimeter $s$:** Key `{{res:sc32_06_geometry_surface_area_seq_21:keys}}` (`7 {{key:ENTER}} 9 {{key:+}} 12 {{key:+}} 2 {{key:÷}}`) to obtain $s = 14.0\text{ m}$ in Register $X$, and store it via `{{key:STO}} S`.
2. **Accumulate the three $(s - \text{side})$ factors:** Since $s = 14.0$ is already sitting in Register $X$, simply key `7 {{key:-}}` to get $(s - a) = 7.0$; then key `{{key:RCL}} S 9 {{key:-}} {{key:×}}` to multiply by $(s - b) = 5.0$ ($\to 35.0$); then key `{{key:RCL}} S 12 {{key:-}} {{key:×}}` to multiply by $(s - c) = 2.0$ ($\to 70.0$).
3. **Multiply by $s$ and extract the root:** Key `{{key:RCL}} S {{key:×}} {{key:√x}}` to evaluate $\sqrt{14.0 \times 70.0} = \sqrt{980.0} = \mathbf{31.304952\text{ m}^2}$:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `7 {{key:ENTER}} 9 {{key:+}} 12 {{key:+}} 2 {{key:÷}} {{key:STO}} S` | $0.0000$ | $0.0000$ | $0.0000$ | $14.0000$ | Semiperimeter $s = (a+b+c)/2$ stored in `S` |
| 2 | `7 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $7.0000$ | Factor $(s - a) = 14 - 7 = 7.0$ directly from $X$ |
| 3 | `{{key:RCL}} S 9 {{key:-}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $35.0000$ | Multiply by $(s - b) = 5.0$; subtotal $= 35.0$ |
| 4 | `{{key:RCL}} S 12 {{key:-}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $70.0000$ | Multiply by $(s - c) = 2.0$; subtotal $= 70.0$ |
| 5 | `{{key:RCL}} S {{key:×}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$31.304952$** | Multiply by $s$ and take root; Area $= 31.30\text{ m}^2$ |

Once you know the semiperimeter $s$ of a triangle, dividing area by semiperimeter ($r = A/s$) gives the radius of its **incircle**—the largest circle that fits inside the three sides. When the triangle is a right-angled structural channel with orthogonal legs $a = 15.0\text{ cm}$ and $b = 20.0\text{ cm}$, what is the radius $r$ of the largest cylindrical coolant pipe that can be tucked inside it? By the two-tangent theorem of Euclidean geometry, the tangent segments from the $90^\circ$ corner to the incircle form a little square of side $r$, while the remaining tangent segments along the legs—$(a - r)$ and $(b - r)$—fold onto the hypotenuse $c = \sqrt{a^2 + b^2} = 25.0\text{ cm}$ so that $c = (a - r) + (b - r)$. Solving for the inradius $r$ yields a wonderfully clean linear formula:

$$r = \frac{a + b - c}{2} = \frac{15 + 20 - 25}{2} = \frac{10}{2} = \mathbf{5.0000\text{ cm}} \qquad (\text{with circumradius } R = \frac{c}{2} = 12.5\text{ cm})$$

Running `15 {{key:x²}} 20 {{key:x²}} {{key:+}} {{key:√x}} 15 {{key:ENTER}} 20 {{key:+}} {{key:x⇄y}} {{key:-}} 2 {{key:÷}}` computes the hypotenuse $c = 25.0\text{ cm}$ in Step 1 (which can also be done via `15 {{key:ENTER}} 20 {{key:▸θ,r}}`), sums the legs $a + b = 35.0\text{ cm}$ in Step 2, subtracts $c$, and halves the result to yield the exact inradius **`5.0000`** (**$r = 5.0000\text{ cm}$**):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `15 {{key:x²}} 20 {{key:x²}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $25.0000$ | Hypotenuse $c = \sqrt{a^2 + b^2}$ in cm |
| 2 | `15 {{key:ENTER}} 20 {{key:+}}` | $0.0000$ | $0.0000$ | $25.0000$ | $35.0000$ | Sum of orthogonal legs $a + b$ |
| 3 | `{{key:x⇄y}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | Excess tangent span $(a + b - c)$ |
| 4 | `2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$5.0000$** | Right triangle inradius $r$ in cm |

---

## The Master Surface Area Technique via Stats Mode (`{{key:Σ+}}`)

In mechanical CAD, thermal design, and additive manufacturing, finding the total exterior surface area of a 3D part is traditionally a bookkeeping headache. Real-world enclosures have top and bottom lids, side walls, end caps, bosses, and cutout apertures. On an algebraic calculator, summing all those faces requires a fragile string of parenthesized products:
$$A_{\text{total}} = (2 \times L \times W) + (2 \times L \times H) + (2 \times W \times H) + \dots$$
where a single mistyped digit at face #5 forces you to re-key the entire expression from the beginning.

### Turning the Statistical Accumulator (`{{key:Σ+}}`) into a Polygon Tally Bus

On the StackCalc SC-32, the **Statistical Accumulator (`{{key:Σ+}}`)** serves as a dedicated hardware summing bus that decouples each face calculation from the running total:

First, press `{{key:CLΣ}}` to clear the six internal statistical registers ($\Sigma x = 0, n = 0$). Next, compute the area $A_1$ of your first face (or symmetric face pair) on the stack and press `{{key:Σ+}}`. That single keystroke adds $A_1$ into the internal $\Sigma x$ summation register, increments the polygon counter to $n = 1$, displays $1.0000$ in Register $X$ so you can verify how many face groups you have tallied, and arms the stack for your next face calculation! If you need to deduct a window cutout or screw bore—or if you accidentally push a wrong dimension—simply compute that area and press `{{key:Σ-}}` to subtract it from $\Sigma x$ without disturbing any previous faces. Once every boundary face has been tallied, pressing `{{key:SUMS}}` recalls the exact total surface area $\Sigma x$ at full 12-digit precision—with **zero parentheses, zero named memory variables, and zero scratch paper**.

{{blocks:fraction_gauge_comparison|Fraction Studio Precision Gauge Comparison}}
*Figure 6.2: Precision micrometer comparator gauge verification, pairing physical volumetric measurement directly with statistical accumulator face audits on the RPN stack.*

### Galileo's Square-Cube Law, L-Frame Annuli & Polyhedral Face Decomposition

To see why surface-area-to-volume scaling and the `{{key:Σ+}}` statistical bus work together so naturally, combine three physical tools from the StackCalc studio kit:
1. **Counting Tiles & Galileo's Square-Cube Asymmetry:** Dock a single $19.0 \times 19.0 \times 7.0\text{ mm}$ ($1\text{U}$) counting tile on the Snapfinity lid: it has $1$ top unit face, $1$ bottom unit face, and $4$ perimeter side edges ($6$ outer block faces). Now dock eight $1\text{U}$ tiles into a $2 \times 2 \times 2$ block prism (four $2\text{-tile}$ towers docked in a $2 \times 2$ square): doubling the block count along each axis ($\ell \to 2\ell$) multiplies the exposed exterior surface area by $2^2 = 4$ ($6 \to 24\text{ exposed block faces}$), while multiplying the internal volume by $2^3 = 8$ ($1 \to 8\text{ tiles}$)—physically demonstrating Galileo's 1638 Square-Cube Law. Conversely, halving the edge length of a unit cube ($\ell \to \frac{1}{2}\ell$) packs **$2^3 = 8$ half-size cubes into each unit volume** while doubling the total exposed surface area ($A/V \to 2\times$), which is why finely divided catalyst pellets, pulmonary alveoli, and pin-fin heat sinks pack massive active surface area into a compact volume.
2. **The Algebra Factoring L-Frame Stage & Difference-of-Squares Annuli:** When evaluating a flanged pipe gasket or hollow structural tube $A = \pi(R^2 - r^2) = \pi(R - r)(R + r)$, docking an $R \times R$ square flat into the $90^\circ$ L-Frame Stage and removing an $r \times r$ corner square leaves an L-shaped gnomon whose two wings rearrange directly into a single $(R - r) \times (R + r)$ rectangle.
3. **Isohedral Polyhedra & Planar Face Accumulation (`{{key:Σ+}}`):** Inspecting the five Platonic polyhedra ($d4$ tetrahedron, $d6$ cube, $d8$ octahedron, $d12$ dodecahedron, and $d20$ icosahedron) among the **Polyhedral Dice** confirms Leonhard Euler's topological invariant ($V - E + F = 2$) and reveals why you never need a monolithic 30-character algebraic formula for surface area: every three-dimensional solid is simply a boundary collection of $F$ planar faces. Computing each planar face (or opposing face pair) on the 4-level stack and pressing `{{key:Σ+}}` accumulates the area into $\Sigma x$ while the LCD counter $n = 1, 2, \dots$ verifies that every face of the solid has been accounted for.

---

### SC-32 Handheld Chassis & Cylindrical Battery Pod Surface Area

Let us put the `{{key:Σ+}}` bus to work by computing the total external surface area of the StackCalc SC-32 rectangular chassis ($L = 135\text{ mm}$, $W = 70\text{ mm}$, $H = 16\text{ mm}$) for passive thermal dissipation and injection-mold cooling analysis. Its six exterior walls group into three opposing pairs:
1. **Top & Bottom Lids:** $A_1 = 2 \times (135 \times 70) = 18,900.0\text{ mm}^2$
2. **Left & Right Side Walls:** $A_2 = 2 \times (135 \times 16) = 4,320.0\text{ mm}^2$
3. **Front & Rear End Caps:** $A_3 = 2 \times (70 \times 16) = 2,240.0\text{ mm}^2$
$$\text{Total External Surface Area } A_{\text{total}} = 18,900 + 4,320 + 2,240 = \mathbf{25,460.0\text{ mm}^2}$$

First, zero statistical memory via `{{key:CLΣ}}`, then compute each face pair and press `{{key:Σ+}}`:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Accumulator $\Sigma x$ | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `135 {{key:ENTER}} 70 {{key:×}} 2 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $18900.0$ | $0.0$ | Top/Bottom area pair evaluated |
| 2 | `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$1.0$** | **$18900.0$** | $n=1$, accumulated into $\Sigma x$ |
| 3 | `135 {{key:ENTER}} 16 {{key:×}} 2 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $4320.0$ | $18900.0$ | Side walls area pair evaluated |
| 4 | `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$2.0$** | **$23220.0$** | $n=2$, accumulated into $\Sigma x$ |
| 5 | `70 {{key:ENTER}} 16 {{key:×}} 2 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $2240.0$ | $23220.0$ | End caps area pair evaluated |
| 6 | `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$3.0$** | **$25460.0$** | $n=3$, accumulated into $\Sigma x$ |
| 7 | `{{key:SUMS}} → Σx` | $0.0$ | $0.0$ | $0.0$ | **$25460.0000$** | $25460.0$ | Total Surface Area recalled |

The chassis total surface area is **$25,460.0\text{ mm}^2$** ($254.6\text{ cm}^2$).

The same `{{key:Σ+}}` workflow applies to curved solids. Consider a cylindrical lithium battery compartment of radius $r = 15\text{ mm}$ and height $h = 65\text{ mm}$. Its total surface area consists of two circular end caps ($A_{\text{ends}} = 2\pi r^2 = 450\pi \approx 1,413.7167\text{ mm}^2$) and one unrolled cylindrical lateral wall ($A_{\text{lat}} = 2\pi r h = 1,950\pi \approx 6,126.1057\text{ mm}^2$):
$$\text{Total Surface Area } A_{\text{cyl}} = 450\pi + 1950\pi = 2400\pi \approx \mathbf{7,539.822369\text{ mm}^2}$$

Clearing stats (`{{key:CLΣ}}`) and accumulating both surfaces via `{{key:Σ+}}` yields **$7,539.82\text{ mm}^2$** ($75.40\text{ cm}^2$):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Accumulator $\Sigma x$ | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `15 {{key:x²}} {{key:π}} {{key:×}} 2 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $1413.716694$ | $0.0$ | 2 circular ends evaluated |
| 2 | `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$1.0$** | **$1413.716694$** | $n=1$, accumulated |
| 3 | `2 {{key:π}} {{key:×}} 15 {{key:×}} 65 {{key:×}}` | $0.0$ | $0.0$ | $0.0$ | $6126.105675$ | $1413.716694$ | Cylindrical wall evaluated |
| 4 | `{{key:Σ+}}` | $0.0$ | $0.0$ | $0.0$ | **$2.0$** | **$7539.822369$** | $n=2$, accumulated |
| 5 | `{{key:SUMS}} → Σx` | $0.0$ | $0.0$ | $0.0$ | **$7539.822369$** | $7539.822369$ | Total Surface Area recalled |

### Stepped Castings, Extruded Heat-Sink Fins & Pyramidal Roofs

What happens when a real-world component is not a single prism, but a stepped casting or an array of cooling fins? To estimate the electroplating bath current for a stepped cast-iron machine bracket consisting of a base block ($120 \times 80 \times 30\text{ mm}$) surmounted by a rectangular boss ($60 \times 40 \times 25\text{ mm}$), we need its total exposed surface area. Look at a geometric shortcut before we even touch a key: the top face of the upper boss ($60 \times 40\text{ mm}$) plus the exposed horizontal ledge of the base block around it ($120 \times 80 - 60 \times 40\text{ mm}$) project together to form one complete $120 \times 80 = 9,600\text{ mm}^2$ top rectangle! We clear statistics (`{{key:CLΣ}}`) and tally all six face groups into `{{key:Σ+}}`:

1. **Bottom Face ($120 \times 80$):** `120 {{key:ENTER}} 80 {{key:×}} {{key:Σ+}}` ($n = 1,\; A = 9,600\text{ mm}^2$)
2. **Base Long Sides ($2 \times 120 \times 30$):** `120 {{key:ENTER}} 30 {{key:×}} 2 {{key:×}} {{key:Σ+}}` ($n = 2,\; A = 7,200\text{ mm}^2$)
3. **Base Ends ($2 \times 80 \times 30$):** `80 {{key:ENTER}} 30 {{key:×}} 2 {{key:×}} {{key:Σ+}}` ($n = 3,\; A = 4,800\text{ mm}^2$)
4. **Upper Boss Sides ($2 \times 60 \times 25$):** `60 {{key:ENTER}} 25 {{key:×}} 2 {{key:×}} {{key:Σ+}}` ($n = 4,\; A = 3,000\text{ mm}^2$)
5. **Upper Boss Ends ($2 \times 40 \times 25$):** `40 {{key:ENTER}} 25 {{key:×}} 2 {{key:×}} {{key:Σ+}}` ($n = 5,\; A = 2,000\text{ mm}^2$)
6. **Combined Top Footprint ($120 \times 80$):** `120 {{key:ENTER}} 80 {{key:×}} {{key:Σ+}}` ($n = 6,\; A = 9,600\text{ mm}^2$)

Recalling `{{key:SUMS}}` ($\Sigma x$) immediately returns **$36,200.0\text{ mm}^2$** while the LCD counter $n = 6.0000$ confirms that all six face groups were tallied:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:CLΣ}} 120 {{key:ENTER}} 80 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Bottom face area $9,600.0\text{ mm}^2$ accumulated ($n=1$) |
| 2 | `120 {{key:ENTER}} 30 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | 2 base sides $7,200.0\text{ mm}^2$ accumulated ($n=2$) |
| 3 | `80 {{key:ENTER}} 30 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.0000$ | 2 base ends $4,800.0\text{ mm}^2$ accumulated ($n=3$) |
| 4 | `60 {{key:ENTER}} 25 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | 2 upper sides $3,000.0\text{ mm}^2$ accumulated ($n=4$) |
| 5 | `40 {{key:ENTER}} 25 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $5.0000$ | 2 upper ends $2,000.0\text{ mm}^2$ accumulated ($n=5$) |
| 6 | `120 {{key:ENTER}} 80 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $6.0000$ | Net top face area $9,600.0\text{ mm}^2$ accumulated ($n=6$) |
| 7 | `{{key:SUMS}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$36200.0000$** | Recall total casting surface area $\Sigma x$ |

That same projection insight reveals how an extruded aluminum heat sink defeats Galileo's Square-Cube bottleneck (from our chapter opening). Consider a $100 \times 100\text{ mm}$ square base plate carrying $8$ vertical cooling fins, each $100\text{ mm}$ long, $35\text{ mm}$ tall, and $2\text{ mm}$ thick. We decompose the heat sink into four surface groups and accumulate them via `{{key:Σ+}}`:
- **16 Vertical Fin Sides:** $16 \times (100 \times 35) = 56,000\text{ mm}^2$
- **8 Fin Top Tips:** $8 \times (100 \times 2) = 1,600\text{ mm}^2$
- **Exposed Valley Floor Between Fins:** $(100 \times 100) - 1,600 = 8,400\text{ mm}^2$
- **Base Flat Bottom:** $100 \times 100 = 10,000\text{ mm}^2$

Just as with the stepped machine casting above, notice that the $8$ fin tips ($1,600\text{ mm}^2$) plus the valley floor ($8,400\text{ mm}^2$) equal the original $10,000\text{ mm}^2$ top footprint—so extruding the $8$ fins adds their $16$ vertical side walls ($56,000\text{ mm}^2$), boosting total surface area from $20,000\text{ mm}^2$ to **$76,000.0\text{ mm}^2$** ($760.0\text{ cm}^2$, a $3.8\times$ thermal multiplier):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:CLΣ}} 16 {{key:ENTER}} 100 {{key:×}} 35 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | 16 fin sides ($56,000.0\text{ mm}^2$) accumulated ($n=1$) |
| 2 | `8 {{key:ENTER}} 100 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | 8 fin tips ($1,600.0\text{ mm}^2$) accumulated ($n=2$) |
| 3 | `100 {{key:ENTER}} 100 {{key:×}} 1600 {{key:-}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.0000$ | Base exposed top ($8,400.0\text{ mm}^2$) accumulated ($n=3$) |
| 4 | `100 {{key:ENTER}} 100 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | Base flat bottom ($10,000.0\text{ mm}^2$) accumulated ($n=4$) |
| 5 | `{{key:SUMS}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$76000.0000$** | Recall total heat sink surface area $\Sigma x$ |

In architectural takeoffs, the `{{key:Σ+}}` bus handles sloped roof planes just as cleanly as orthogonal walls. Suppose a park pavilion is capped by a four-sided hipped pyramidal frustum roof whose base is a $12\text{ m}$ square, top skylight curb is a $4\text{ m}$ square, and inclined slant height along each hip face is $s = 6.5\text{ m}$. Each of the four sloping roof planes is a trapezoid of area $A_{\text{face}} = \frac{1}{2}(12 + 4)\times 6.5 = 52.0\text{ m}^2$. Clearing statistics (`{{key:CLΣ}}`) and accumulating the four roof faces into `{{key:Σ+}}` gives a total standing-seam metal roofing takeoff of **$208.0\text{ m}^2$**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:CLΣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Clear statistical accumulators |
| 2 | `12 {{key:ENTER}} 4 {{key:+}} 6.5 {{key:×}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $52.0000$ | Single trapezoidal face area $A_{\text{face}}$ in m² |
| 3 | `4 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | 4 lateral roof faces ($208.0\text{ m}^2$) accumulated ($n=1$) |
| 4 | `{{key:SUMS}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$208.0000$** | Recall total pavilion roof surface area $\Sigma x$ |

We can even evaluate Galileo's surface-to-volume ratio $A/V$ directly on a regular right square pyramid of base side $s = 12.0\text{ mm}$ and vertical altitude $h = 8.0\text{ mm}$. Notice how the half-base $s/2 = 6.0\text{ mm}$ and altitude $h = 8.0\text{ mm}$ form a $6\text{–}8\text{–}10$ Pythagorean right triangle on each face, giving slant height $l = \sqrt{8^2 + 6^2} = 10.0\text{ mm}$:
- **Total Surface Area:** $A = s^2 + 4\left(\frac{1}{2} s l\right) = 144 + 2(12)(10) = 384.0\text{ mm}^2$
- **Enclosed Volume:** $V = \frac{1}{3} s^2 h = \frac{1}{3}(144)(8) = 384.0\text{ mm}^3$
- **Surface-to-Volume Ratio:** $\frac{A}{V} = \frac{384.0\text{ mm}^2}{384.0\text{ mm}^3} = \mathbf{1.0000\text{ mm}^{-1}}$

Keying `8 {{key:x²}} 12 {{key:ENTER}} 2 {{key:÷}} {{key:x²}} {{key:+}} {{key:√x}} 2 {{key:×}} 12 {{key:×}} 12 {{key:x²}} {{key:+}} 12 {{key:x²}} 8 {{key:×}} 3 {{key:÷}} {{key:÷}}` returns **`1.0000`**. Why do the surface area and volume both equal $384$? Because for any polyhedron circumscribed around an inscribed sphere of radius $r_{\text{in}}$, decomposing the solid into pyramids from the incenter to each face proves that $V = \frac{1}{3} r_{\text{in}} A$, or $\frac{A}{V} = \frac{3}{r_{\text{in}}}$—and here the inscribed sphere has radius $r_{\text{in}} = 3.0\text{ mm}$!

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `8 {{key:x²}} 12 {{key:ENTER}} 2 {{key:÷}} {{key:x²}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | Slant height $l = \sqrt{h^2 + (s/2)^2}$ |
| 2 | `2 {{key:×}} 12 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $240.0000$ | 4 lateral triangular faces $A_{\text{lat}}$ |
| 3 | `12 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $384.0000$ | Total pyramid surface area $A$ |
| 4 | `12 {{key:x²}} 8 {{key:×}} 3 {{key:÷}}` | $0.0000$ | $0.0000$ | $384.0000$ | $384.0000$ | Pyramid volume $V = s^2 h / 3$ |
| 5 | `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1.0000$** | Surface-to-volume ratio $A/V$ |

### Scratchpad Mensuration vs. Register-Preserving Geometric Accumulation

The table below contrasts long algebraic sum-of-products entry against face-by-face accumulation on the SC-32's hardware statistical bus (`{{key:Σ+}}`):

| Challenge / Metric | Conventional Algebraic Calculator (Infix) | Algebraic Strokes | SC-32 RPN Stack Method | SC-32 Strokes | Stack Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **Multi-Face Solid Surface Area**: 6 Faces | String calculation: `12 * 8 + 12 * 5 + 8 * 5 + 0.5 * 8 * 6 + ...` (38 strokes). Typo requires retyping entire 38 characters. | 38 | **Master Surface Area (`{{key:Σ+}}`)**: Key each face on stack, press `{{key:Σ+}}` (22 strokes). Screen tracks face count $n$ and accumulated area $\Sigma x$. Tap `{{key:Σ-}}` to pull back any error. | 22 | **42% fewer strokes + 100% face visibility** |

---

## Solid Mensuration: Classical 3D Volumes, Cavalieri's Principle & Curved Shells

The evaluation of three-dimensional solids in competitive contests and engineering stress analysis demands rapid, error-free reductions. The following master catalog pairs each classical geometry with its physical motivation and optimal RPN evaluation pipeline:

| 3D Solid Geometry | Analytical Volume Formula | Total External Surface Area Formula | Physical & Geometric Motivation |
| :--- | :--- | :--- | :--- |
| **Rectangular Prism** | $V = l \cdot w \cdot h$ | $A = 2(lw + lh + wh)$ | Cartesian volume product; 6 orthogonal bounding faces. |
| **Right Circular Cylinder** | $V = \pi r^2 h$ | $A = 2\pi r^2 + 2\pi r h$ | Extrusion of circular base along normal axis $h$. |
| **Right Circular Cone** | $V = \frac{1}{3} \pi r^2 h$ | $A = \pi r^2 + \pi r \sqrt{r^2 + h^2}$ | Exactly $\frac{1}{3}$ of circumscribed cylinder (Eudoxus-Archimedes). |
| **Sphere** | $V = \frac{4}{3} \pi r^3$ | $A = 4\pi r^2$ | Surface area is derivative of volume with respect to radius $r$. |
| **Torus (Major $R$, minor $r$)** | $V = 2\pi^2 R r^2$ | $A = 4\pi^2 R r$ | **Pappus-Guldinus:** Centroid path ($2\pi R$) $\times$ disk area ($\pi r^2$) or perimeter ($2\pi r$). |
| **Frustum of Right Cone** | $V = \frac{1}{3} \pi h (R^2 + Rr + r^2)$ | $A = \pi(R^2 + r^2) + \pi(R + r)s$ | Truncated cone; factored in RPN via $(R+r)^2 - Rr$. |
| **Spherical Cap (height $h$)** | $V = \frac{1}{3} \pi h^2 (3r - h)$ | $A_{\text{dome}} = 2\pi r h$ | Archimedes' cylinder balance: sliced sphere disk integration. |
| **Spherical Zone (2 bases)** | $V = \frac{\pi h}{6}(3r_1^2 + 3r_2^2 + h^2)$ | $A_{\text{zone}} = 2\pi R h$ | Slice between two parallel cutting planes through a sphere. |
| **Ellipsoid** | $V = \frac{4}{3} \pi a b c$ | $A \approx 4\pi \left(\frac{(ab)^p + (ac)^p + (bc)^p}{3}\right)^{1/p}$ | Affine 3D stretch of sphere along 3 principal orthogonal axes. |
| **Paraboloid of Revolution** | $V = \frac{1}{2} \pi r^2 h$ | $A = \frac{\pi r}{6h^2} \left[(r^2 + 4h^2)^{3/2} - r^3\right]$ | Exactly $\frac{1}{2}$ of bounding cylinder (Archimedes' law of paraboloids). |
| **Cylindrical Ungula (Hoof)** | $V = \frac{2}{3} r^3 \tan\alpha$ | $A_{\text{curved}} = 2 r^2 \tan\alpha$ | Slicing cylinder by an inclined plane passing through base diameter. |
| **Universal Prismoidal Solid** | $V = \frac{h}{6}(A_{\text{top}} + 4A_{\text{mid}} + A_{\text{bot}})$ | Dependent on geometry | Simpson's 3D rule: exact for any solid whose area is a cubic polynomial in $z$. |
| **Regular Tetrahedron** | $V = \frac{\sqrt{2}}{12} a^3$ | $A = \sqrt{3} a^2$ | 4 equilateral triangular faces; self-dual Platonic solid. |
| **Regular Octahedron** | $V = \frac{\sqrt{2}}{3} a^3$ | $A = 2\sqrt{3} a^2$ | 8 equilateral triangular faces; dual of the cube. |
| **Regular Dodecahedron** | $V = \frac{15 + 7\sqrt{5}}{4} a^3$ | $A = 3\sqrt{25 + 10\sqrt{5}}\,a^2$ | 12 regular pentagonal faces; golden ratio $\phi$ geometry. |
| **Regular Icosahedron** | $V = \frac{5(3 + \sqrt{5})}{12} a^3$ | $A = 5\sqrt{3} a^2$ | 20 equilateral triangular faces; dual of the dodecahedron. |

For the master quick-reference tables of all 3D solid mensuration formulas, consult **[Appendix D: Section 8 (3D Solid Mensuration & Revolution Geometry)](appendix-d-constants-and-equations.md)**.

### Cavalieri's Slice Principle, Conical Frustums & the Steinmetz Bicylinder

By Bonaventura Cavalieri's slice principle, any cone or pyramid whose cross-sectional area shrinks quadratically from base to apex as $A(z) = A_{\text{base}}(z/h)^2$ encloses exactly one-third the volume of its bounding prism or cylinder: $V = \frac{1}{3}A_{\text{base}}h$. For an aerodynamic transition nose cone with an elliptical base ($a = 24.0\text{ mm}$, $b = 15.0\text{ mm}$, so $A_{\text{base}} = \pi ab$) and vertical height $h = 50.0\text{ mm}$, the enclosed volume is:

$$V = \frac{1}{3} \pi a b h = \frac{\pi}{3} (24)(15)(50) = \frac{\pi}{3}(18000) = 6000\pi \approx \mathbf{18,849.5559\text{ mm}^3}$$

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `24 {{key:ENTER}} 15 {{key:×}} 50 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $18000.0000$ | Product $a \cdot b \cdot h$ evaluated |
| 2 | `{{key:π}} {{key:×}} 3 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$18849.555922$** | Elliptic cone volume $V$ in mm³ |

Cavalieri's slice principle also unlocks one of the most surprising volumes in solid geometry: when two equal circular pipes of radius $r = 15.0\text{ mm}$ intersect at right angles (forming a groin vault in architecture or a cross-fitting in high-pressure piping), what is the volume and surface area of their common intersection—the **Steinmetz bicylinder**? Archimedes (in *The Method*) and 3rd-century Chinese mathematician Liu Hui (who called it the *Mouhefanggai*, or "two square umbrellas") discovered something astonishing: if you slice the bicylinder horizontally at any height $z$, the cross-section is a **square** of side $2\sqrt{r^2 - z^2}$, whereas the cross-section of an inscribed sphere of radius $r$ at the same height is a **circle** of area $\pi(r^2 - z^2)$. Because the ratio of the square's area to the circle's area is $\frac{4}{\pi}$ at every single slice, Cavalieri's principle guarantees that the total volume of the bicylinder is $\frac{4}{\pi}$ times the sphere's volume $\frac{4}{3}\pi r^3$—causing $\pi$ to cancel out completely!

$$V = \frac{4}{\pi}\left(\frac{4}{3}\pi r^3\right) = \frac{16}{3} r^3 = \frac{16}{3} (15^3) = \mathbf{18,000.0\text{ mm}^3}, \qquad A = 16 r^2 = 16(15^2) = \mathbf{3,600.0\text{ mm}^2}$$

Evaluating `16 {{key:ENTER}} 3 {{key:÷}} 15 {{key:ENTER}} 3 {{key:yˣ}} {{key:×}}` yields the exact rational volume **$18,000.0\text{ mm}^3$**, and `15 {{key:x²}} 16 {{key:×}}` gives the surface area **$3,600.0\text{ mm}^2$**.

What if a cone is sliced flat before reaching its apex? Consider an agricultural grain hopper (or rocket nozzle section) shaped as a **conical frustum**—a cone sliced by two parallel planes—with upper radius $R = 1.80\text{ m}$, lower discharge radius $r = 0.40\text{ m}$, and vertical height $h = 2.50\text{ m}$. Notice the geometric beauty of the frustum volume formula $V = \frac{h}{3}(\pi R^2 + \pi Rr + \pi r^2)$: it is the height $h$ multiplied by the average of three areas—the top circle $\pi R^2$, the bottom circle $\pi r^2$, and their **geometric mean** $\sqrt{(\pi R^2)(\pi r^2)} = \pi Rr$:

$$V = \frac{1}{3} \pi h (R^2 + R r + r^2) = \frac{2.5\pi}{3} (1.8^2 + 1.8(0.4) + 0.4^2) = \frac{2.5\pi}{3} (3.24 + 0.72 + 0.16) = \frac{2.5\pi}{3} (4.12) = \mathbf{10.7861\text{ m}^3}$$

Watch how `{{key:LASTX}}` in the sequence `{{res:sc32_06_geometry_surface_area_seq_04:keys}}` lets you evaluate the entire hopper volume $V = \frac{1}{3}\pi h(R^2 + Rr + r^2)$ while typing `1.8` and `0.4` only once each: keying `1.8 {{key:x²}} {{key:LASTX}} 0.4 {{key:×}} {{key:LASTX}} {{key:x²}} {{key:+}} {{key:+}} {{key:π}} {{key:×}} 2.5 {{key:×}} 3 {{key:÷}}` forms $R^2 + Rr + r^2 = 4.12\text{ m}^2$ in Register $X$ and scales by $\frac{2.5\pi}{3}$ in a single stream to produce **`{{res:sc32_06_geometry_surface_area_seq_04:value}}`** (**$10.7861\text{ m}^3$**, or $10,786.1\text{ liters}$). You can also factor the parenthetical term as $(R+r)^2 - Rr$ via `R {{key:ENTER}} r {{key:ENTER}} {{key:+}} {{key:x²}} {{key:LASTX}} {{key:x⇄y}} {{key:×}} {{key:-}} h {{key:×}} {{key:π}} {{key:×}} 3 {{key:÷}}`, keeping every term inside the 4-register stack with zero register allocation.

### Polyhedral Trusses & Hexagonal Fastener Mass Takeoffs

In structural machining and fastener design, regular polygons extrude into prismatic bars and bolt heads. Because any two concentric regular $n$-gons share the exact same shape factor $C_n$, the net cross-sectional area of a hollow polygonal bar always factors as $C_n(S^2 - s^2)$. For a regular hexagonal brass bar of outer side $S = 20.0\text{ mm}$ with a concentric hexagonal bore of inner side $s = 8.0\text{ mm}$ and length $L = 150.0\text{ mm}$ (where six equilateral triangles of area $\frac{\sqrt{3}}{4}s^2$ give the hexagon constant $C_6 = \frac{3\sqrt{3}}{2}$):

$$\text{Net Area } A_{\text{net}} = \frac{3\sqrt{3}}{2} (S^2 - s^2) = \frac{3\sqrt{3}}{2} (400 - 64) = 504\sqrt{3} \approx 872.9536\text{ mm}^2 \implies V_{\text{net}} = A_{\text{net}} L = \mathbf{130,943.04\text{ mm}^3}$$

Entering `{{res:sc32_06_geometry_surface_area_seq_20:keys}}` evaluates $(S^2 - s^2) = 336.0\text{ mm}^2$, scales by $\frac{3\sqrt{3}}{2}$, and multiplies by $L = 150\text{ mm}$ to produce **$130,943.04\text{ mm}^3$**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `20 {{key:x²}} 8 {{key:x²}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $336.0000$ | Hexagonal span difference $(S^2 - s^2)$ |
| 2 | `3 {{key:√x}} {{key:×}} 3 {{key:×}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $872.953607$ | Net hexagonal cross section $A_{\text{net}}$ in mm² |
| 3 | `150 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$130943.041071$** | Prismatic void volume $V_{\text{net}} = A_{\text{net}} \cdot L$ in mm³ |

Similarly, for a solid steel hex bolt head of side $s = 10.0\text{ mm}$, height $h = 12.0\text{ mm}$, and steel density $\rho = 7.85\text{ g/cm}^3$ ($0.00785\text{ g/mm}^3$), the volume and mass of the bolt head follow directly from $A_{\text{hex}} = \frac{3\sqrt{3}}{2}s^2$:

$$A_{\text{hex}} = \frac{3\sqrt{3}}{2} s^2 = \frac{3\sqrt{3}}{2} (100) \approx 259.8076\text{ mm}^2 \implies V = A_{\text{hex}} h = 3,117.69\text{ mm}^3 = 3.11769\text{ cm}^3$$
$$\text{Mass } m = 3.11769\text{ cm}^3 \times 7.85\text{ g/cm}^3 = \mathbf{24.4739\text{ grams}}$$

On the stack, form the hexagon constant $3\sqrt{3}/2 \approx 2.598076$ via `3 {{key:√x}} {{key:LASTX}} {{key:×}} 2 {{key:÷}}` (using `{{key:LASTX}}` to recover $3$ after taking its square root), multiply by $s^2 = 100\text{ mm}^2$ (`10 {{key:x²}} {{key:×}}`) and height $h = 12\text{ mm}$ (`12 {{key:×}}`), and convert $\text{mm}^3$ to grams via `1000 {{key:÷}} 7.85 {{key:×}}` to obtain **$24.4739\text{ grams}$**.

In three-dimensional space-frame trusses, the simplest and stiffest of the five Platonic solids is the regular tetrahedron. Why does the volume of a regular tetrahedron of edge length $a = 50.0\text{ mm}$ have a factor of $\frac{\sqrt{2}}{12}$? You can inscribe a regular tetrahedron inside a cube of edge $a/\sqrt{2}$ by drawing the face diagonals connecting four alternating corners of the cube. Slicing off the four right-angled corner pyramids—each of volume $\frac{1}{6}\text{cube}$—leaves the central tetrahedron occupying $1 - \frac{4}{6} = \frac{1}{3}$ of the cube's volume, or $V = \frac{1}{3}(a/\sqrt{2})^3 = \frac{\sqrt{2}}{12}a^3$:

$$h = \sqrt{\frac{2}{3}} a \approx \mathbf{40.8248\text{ mm}}, \qquad A = \sqrt{3} a^2 \approx \mathbf{4,330.1270\text{ mm}^2}, \qquad V = \frac{\sqrt{2}}{12} a^3 = \frac{\sqrt{2}}{12} (125,000) \approx \mathbf{14,731.3913\text{ mm}^3}$$

For the enclosed volume, keying `{{res:sc32_06_geometry_surface_area_seq_11:keys}}` evaluates $\sqrt{2}/12 \approx 0.117851$ (`2 {{key:√x}} 12 {{key:÷}}`), cubes the edge length $a = 50\text{ mm}$ (`50 {{key:ENTER}} 3 {{key:yˣ}}` $\to 125,000$), and multiplies (`{{key:×}}`) to return **`{{res:sc32_06_geometry_surface_area_seq_11:value}}`** (**$14,731.39\text{ mm}^3$**).

### Spherical Caps, Lunes, Girard's Spherical Excess & Triaxial Asteroids

When aerospace textile engineers pattern the fabric gores of a hemispherical recovery parachute or a stratospheric weather balloon of radius $R = 25.0\text{ cm}$, each crescent-shaped panel bounded by two meridians separated by dihedral angle $\theta = 36.0^\circ$ is a **spherical lune**. Because $36.0^\circ$ is exactly one-tenth of a full $360^\circ$ revolution, the lune covers one-tenth of the sphere's total area $4\pi R^2$:

$$A_{\text{lune}} = 2 R^2 \theta_{\text{rad}} = 4\pi R^2 \left(\frac{\theta^\circ}{360^\circ}\right) = 4\pi(625) \left(\frac{36}{360}\right) = 2500\pi (0.1) = 250\pi \approx \mathbf{785.3982\text{ cm}^2}$$

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `25 {{key:x²}} 4 {{key:×}} {{key:π}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $7853.981634$ | Full sphere surface area $4\pi R^2$ in cm² |
| 2 | `36 {{key:ENTER}} 360 {{key:÷}}` | $0.0000$ | $0.0000$ | $7853.981634$ | $0.100000$ | Dihedral angle fraction $36^\circ / 360^\circ$ |
| 3 | `{{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$785.398163$** | Spherical lune area $A_{\text{lune}}$ in cm² |

What if a region on a sphere is bounded by three great-circle arcs—a **spherical triangle**? On a flat sheet of paper, the interior angles of every triangle sum to exactly $180^\circ$ ($\pi\text{ rad}$), regardless of how big or small the triangle is. On a curved sphere of radius $R$, however, great-circle geodesics bow outward so that the interior angles $(\alpha, \beta, \gamma)$ of a spherical triangle *always* sum to more than $180^\circ$! In 1629, Dutch-French mathematician **Albert Girard** proved a stunning theorem (the ancestor of the Gauss-Bonnet theorem) by intersecting three pairs of spherical lunes: the **spherical excess** $E_{\text{rad}} = (\alpha + \beta + \gamma - 180^\circ)\frac{\pi}{180^\circ}$ is directly proportional to the triangle's surface area $A = R^2 E_{\text{rad}}$.

Suppose a geodetic survey network on Earth ($R = 6,371.0\text{ km}$) forms a continental spherical triangle with interior angles $\alpha = 82.5^\circ$, $\beta = 68.2^\circ$, and $\gamma = 44.7^\circ$. Let us find the enclosed planetary surface area:

$$\text{Spherical Excess } E = (\alpha + \beta + \gamma - 180^\circ) = (82.5^\circ + 68.2^\circ + 44.7^\circ) - 180^\circ = 195.4^\circ - 180^\circ = 15.4^\circ$$
$$E_{\text{rad}} = 15.4^\circ \times \frac{\pi}{180^\circ} \approx 0.268781\text{ rad} \implies A = R^2 E_{\text{rad}} = 6371^2 \times 0.268781 \approx \mathbf{10,911,102.5\text{ km}^2}$$

Summing the three angles on the stack, subtracting $180^\circ$, converting the $15.4^\circ$ spherical excess into radians, and multiplying by $R^2 = 6,371^2\text{ km}^2$ yields **$10,911,102.50\text{ km}^2$** (roughly the area of Europe):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `82.5 {{key:ENTER}} 68.2 {{key:+}} 44.7 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $195.4000$ | Interior angle sum $\alpha + \beta + \gamma$ in degrees |
| 2 | `180 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $15.4000$ | Spherical excess $E = 15.4^\circ$ |
| 3 | `{{key:π}} {{key:×}} 180 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.268781$ | Excess in radians $E_{\text{rad}} \approx 0.268781\text{ rad}$ |
| 4 | `6371 {{key:x²}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$10911102.50$** | Spherical triangle area $A = R^2 E_{\text{rad}}$ in km² |

In a petrochemical refinery, volatile liquefied gases are stored inside spherical **Hortonsphere** tanks of radius $R = 4.0\text{ m}$ so that membrane tension is uniform in all directions. When an ultrasonic level sensor measures liquid depth $h = 1.5\text{ m}$ at the bottom of the sphere, what volume of liquid sits in the tank? Slicing the sphere into horizontal disks of radius $\sqrt{R^2 - (R-z)^2}$ and integrating from $z = 0$ to $h$ yields Archimedes' **spherical cap** formula:

$$V = \frac{1}{3} \pi h^2 (3R - h) = \frac{\pi (1.5^2)}{3} (3(4.0) - 1.5) = \frac{2.25\pi}{3} (10.5) = 0.75\pi \times 10.5 = \mathbf{24.7400\text{ m}^3}$$

Running `{{res:sc32_06_geometry_surface_area_seq_07:keys}}` forms the factor $(3R - h) = 10.5\text{ m}$ via `4 {{key:ENTER}} 3 {{key:×}} 1.5 {{key:-}}`, recovers $h = 1.5\text{ m}$ from `LASTX` and squares it (`{{key:LASTX}} {{key:x²}} {{key:×}}`), and scales by `{{key:π}} {{key:×}} 3 {{key:÷}}` to deliver **`{{res:sc32_06_geometry_surface_area_seq_07:value}}`** (**$24.7400\text{ m}^3$**, or $24,740.0\text{ liters}$).

What if a celestial body is not a sphere at all, but an irregular asteroid stretched along three unequal axes? While the *volume* of a triaxial ellipsoid with semi-axes $(a, b, c)$ is simply $\frac{4}{3}\pi abc$, its *surface area*—just like the perimeter of an ellipse—has no closed-form expression in elementary functions. In 2004, Danish mathematician Knud Thomsen discovered that taking a power mean of the three projected semi-axis products $(ab, ac, bc)$ with exponent $p = 1.6075$ approximates the exact Legendre elliptic integral to within $1.06\%$ across all aspect ratios! Let us estimate the surface area of a potato-shaped asteroid modeled as a triaxial ellipsoid with semi-axes $a = 15.0\text{ km}$, $b = 10.0\text{ km}$, and $c = 6.0\text{ km}$:

$$p \approx 1.6075 \implies A \approx 4\pi \left(\frac{(ab)^p + (ac)^p + (bc)^p}{3}\right)^{1/p}$$

With projected semi-axis products $ab = 150$, $ac = 90$, and $bc = 60$, notice how `{{key:LASTX}}` lets you raise all three products to the power $p = 1.6075$ without re-typing the exponent: keying `150 {{key:ENTER}} 1.6075 {{key:yˣ}} 90 {{key:LASTX}} {{key:yˣ}} 60 {{key:LASTX}} {{key:yˣ}} {{key:+}} {{key:+}} 3 {{key:÷}} 1.6075 {{key:1/x}} {{key:yˣ}} 4 {{key:×}} {{key:π}} {{key:×}}` averages $3148.23 + 1384.98 + 721.74 = 5254.95 / 3 = 1751.65$, extracts the $1/1.6075$ root ($\to 104.16$), and scales by $4\pi$ to yield an asteroid surface area of **$1,308.90\text{ km}^2$** ($1308.8986\text{ km}^2$).

---

## Analytic 3D Spatial Geometry: Distance, Centroid & Mass Moments of Inertia

Beyond static volumes and surface areas, three-dimensional structural and mechanical design requires spatial distance metrics, composite mass centroids, and rotational moments of inertia.

### 3D Spatial Euclidean Metric, Helical Coils & Direction Cosines

In three-dimensional Cartesian space $\mathbb{R}^3$, the straight-line distance between two coordinate stations $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$ follows the 3D Pythagorean theorem:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$
On the SC-32, you evaluate this parenthesis-free by computing each coordinate difference, squaring it in place, and adding it to the running sum on the stack before extracting the square root:
`x2 {{key:ENTER}} x1 {{key:-}} {{key:x²}}  y2 {{key:ENTER}} y1 {{key:-}} {{key:x²}} {{key:+}}  z2 {{key:ENTER}} z1 {{key:-}} {{key:x²}} {{key:+}} {{key:√x}}`.

That 3D Pythagorean sum also unwraps helical and conical coils in the machine shop. Before winding a tapered conical compression spring (with base radius $R_1 = 30\text{ mm}$, top radius $R_2 = 10\text{ mm}$, axial height $h = 60\text{ mm}$, and $N = 6\text{ active coils}$), a spring maker must cut a straight spring-steel wire blank of length $L$. Unwrapping the conical helix into three orthogonal displacement components—total circumferential travel $2\pi N R_m$ at the mean radius $R_m = (R_1 + R_2)/2 = 20\text{ mm}$, vertical axial rise $h = 60\text{ mm}$, and radial inward taper $R_1 - R_2 = 20\text{ mm}$—turns the arc-length integral into a 3D Pythagorean norm:

$$L \approx \sqrt{(2\pi N R_m)^2 + h^2 + (R_1 - R_2)^2} = \sqrt{(2\pi \times 6 \times 20)^2 + 60^2 + 20^2} = \sqrt{753.98^2 + 3600 + 400} \approx \mathbf{756.63\text{ mm}}$$

Summing the three squared orthogonal displacements via `2 {{key:π}} {{key:×}} 6 {{key:×}} 20 {{key:×}} {{key:x²}} 60 {{key:x²}} {{key:+}} 30 {{key:ENTER}} 10 {{key:-}} {{key:x²}} {{key:+}} {{key:√x}}` returns **`756.6302`** (**$756.63\text{ mm}$**):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `2 {{key:π}} {{key:×}} 6 {{key:×}} 20 {{key:×}} {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $568489.2130$ | Developed circumferential metric $(2\pi N R_m)^2$ |
| 2 | `60 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $572089.2130$ | Accumulate axial rise component $h^2$ |
| 3 | `30 {{key:ENTER}} 10 {{key:-}} {{key:x²}}` | $0.0000$ | $0.0000$ | $572089.2130$ | $400.0000$ | Radial taper variance $(R_1 - R_2)^2$ |
| 4 | `{{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$756.6302$** | Total developed conical coil length in mm |

In three-dimensional spatial tracking, Euclidean distance norms also orient gimbals and structural struts across all three axes simultaneously. Suppose a deep-space tracking radar locks onto an ascending launch vehicle at 3D displacement vector $\vec{V} = (850, 1100, 550)\text{ m}$, whose Euclidean range is $|\vec{V}| = \sqrt{850^2 + 1100^2 + 550^2} = 1,494.9916\text{ m}$. To orient the telemetry gimbal, we need its three **direction cosines**—the components of the unit vector $\hat{u} = \vec{V}/|\vec{V}|$ along the East ($x$), North ($y$), and Zenith ($z$) axes:

$$\cos\alpha = \frac{850}{1494.9916} = \mathbf{0.568565}\;(55.35^\circ), \quad \cos\beta = \frac{1100}{1494.9916} = \mathbf{0.735790}\;(42.63^\circ), \quad \cos\gamma = \frac{550}{1494.9916} = \mathbf{0.367895}\;(68.41^\circ)$$

Executing `{{res:sc32_06_geometry_surface_area_seq_13:keys}}` stores the norm $D = 1494.9916\text{ m}$ in Variable `D` (or recovers it via `{{key:LASTX}}` after each division) and divides each coordinate, leaving all three direction cosines arrayed simultaneously across the stack as $(Z = 0.568565,\; Y = 0.735790,\; X = $ **`{{res:sc32_06_geometry_surface_area_seq_13:value}}`** $)$, where $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1.000000$.

### Center of Mass (Centroid) via Weighted Mean ($\bar{x}_w$)

When an aircraft or structural beam is assembled from $N$ discrete components, each with mass (or cross-sectional area) $m_k$ centered at coordinate $x_k$, the composite center of mass is the **mass-weighted average** of the coordinates:
$$\bar{x}_{\text{cm}} = \frac{\sum_{k=1}^N m_k x_k}{\sum_{k=1}^N m_k}$$
Because the SC-32's statistical engine accumulates both $\Sigma y$ and the cross-product sum $\Sigma xy$ whenever you press `{{key:Σ+}}`, you never need to calculate the numerator and denominator separately! Simply clear statistics (`{{key:CLΣ}}`), load each part's weight or mass $m_k$ into Register $Y$ and its coordinate $x_k$ into Register $X$, and press `{{key:Σ+}}`. Once all parts are entered, pressing `{{key:x̄w}}` (via the `{{key:x̄,ȳ}}` menu) immediately divides $\Sigma(m_k x_k)$ by $\Sigma m_k$ to return the exact centroid coordinate $\bar{x}_{\text{cm}}$.

Suppose an asymmetric welded steel plate girder is fabricated from three horizontal plates: a heavy bottom tension flange ($m_1 = 40\text{ kg}$ centered at height $y_1 = 10\text{ mm}$), a vertical web plate ($m_2 = 60\text{ kg}$ centered at $y_2 = 160\text{ mm}$), and a lighter top flange ($m_3 = 30\text{ kg}$ centered at $y_3 = 310\text{ mm}$). Where does the horizontal neutral axis $\bar{y} = \frac{\sum m_i y_i}{\sum m_i}$ sit? Using the **Weighted Mean (`{{key:x̄w}}`)** technique, we clear statistics (`{{key:CLΣ}}`), load each plate's mass $m_i$ into Register $Y$ and its centroid height $y_i$ into Register $X$, and press `{{key:Σ+}}`:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:CLΣ}}` | $0.0$ | $0.0$ | $0.0$ | $0.0$ | Accumulators cleared |
| 2 | `40 {{key:ENTER}} 10 {{key:Σ+}}` | $0.0$ | $0.0$ | $40.0$ | $1.0$ | Bottom flange ($n=1$) |
| 3 | `60 {{key:ENTER}} 160 {{key:Σ+}}`| $0.0$ | $40.0$ | $60.0$ | $2.0$ | Web section ($n=2$) |
| 4 | `30 {{key:ENTER}} 310 {{key:Σ+}}`| $40.0$ | $60.0$ | $30.0$ | $3.0$ | Top flange ($n=3$) |
| 5 | `{{key:x̄w}}` | $40.0$ | $60.0$ | $30.0$ | **$148.461538$** | Weighted centroid $\bar{y}$ in mm |

Pressing `{{key:x̄w}}` divides $\Sigma(m_i y_i) = 19,300\text{ kg}\cdot\text{mm}$ by total mass $\Sigma m_i = 130\text{ kg}$ to locate the neutral axis at **$\bar{y} = 148.4615\text{ mm}$** ($11.54\text{ mm}$ below the geometric mid-height, pulled downward by the heavier bottom flange). Better still, once that 3-plate girder centroid accumulation (`40 {{key:ENTER}} 10 {{key:Σ+}} 60 {{key:ENTER}} 160 {{key:Σ+}} 30 {{key:ENTER}} 310 {{key:Σ+}}`) and `{{key:x̄w}}` ($\bar{y} = 148.4615\text{ mm}$) have been evaluated, you can verify the Steiner parallel-axis transfer sum $\Sigma m_i (y_i - \bar{y})^2 = \mathbf{1,558,769.23\text{ kg}\cdot\text{mm}^2}$ directly—a technique we will extend in **[Chapter 13: Applied STEM Case Studies](13-applied-stem-case-studies.md)** and **[Chapter 14: Speed & Precision Competition Playbook](14-uil-contest-playbook.md)** to compute composite area moments of inertia $I_{xx} = \Sigma I_i + \Sigma A_i (y_i - \bar{y})^2$ from the hardware statistical registers.

### Mass Moments of Inertia, Hollow Shafts & Steiner's Parallel Axis Theorem

In rotational dynamics, mass alone does not determine how hard it is to spin a flywheel or robot arm; what matters is how far that mass sits from the axis of rotation, weighted by the *square* of the radial distance ($I = \int r^2\,dm$). For symmetric bodies of mass $M$ and outer radius $R$, the center-of-mass moment of inertia takes the form $I_{\text{cm}} = k M R^2$, where the dimensionless geometric factor $k$ measures how concentrated the mass is toward the outer rim: a **solid cylinder** spinning about its symmetry axis has $I_{\text{cm}} = \frac{1}{2}MR^2$; a **solid sphere** (where mass crowds closer to the axis near the poles) has $I_{\text{cm}} = \frac{2}{5}MR^2$; a **thin spherical shell** has $I_{\text{cm}} = \frac{2}{3}MR^2$; and a **slender rod** of length $L$ spinning about its midpoint has $I_{\text{cm}} = \frac{1}{12}ML^2$.

Why do mechanical punch-press flywheels concentrate most of their cast-iron mass in a thick outer rim supported by a thin inner web? Because rotational kinetic energy $\frac{1}{2}I\omega^2$ scales with the *square* of the radius! Consider an $85\text{ kg}$ flywheel consisting of a heavy outer annular rim ($M_{\text{rim}} = 65\text{ kg}$, inner radius $r_1 = 0.28\text{ m}$, outer radius $r_2 = 0.35\text{ m}$) and an inner solid disk web ($M_{\text{web}} = 20\text{ kg}$, radius $R = 0.28\text{ m}$):

$$I_{\text{rim}} = \frac{1}{2} M_{\text{rim}} (r_1^2 + r_2^2) = 0.5(65)(0.28^2 + 0.35^2) = \mathbf{6.52925\text{ kg}\cdot\text{m}^2}, \qquad I_{\text{web}} = \frac{1}{2} M_{\text{web}} R^2 = 0.5(20)(0.28^2) = \mathbf{0.78400\text{ kg}\cdot\text{m}^2}$$
$$I_{\text{total}} = I_{\text{rim}} + I_{\text{web}} = 6.52925 + 0.78400 = \mathbf{7.31325\text{ kg}\cdot\text{m}^2}$$

Evaluating `{{res:sc32_06_geometry_surface_area_seq_16:keys}}` yields **`{{res:sc32_06_geometry_surface_area_seq_16:value}}`** ($I_{\text{total}} = \mathbf{7.31325\text{ kg}\cdot\text{m}^2}$)—showing that even though the outer rim accounts for $76.5\%$ of the flywheel's mass, it contributes **$89.3\%$** of the total rotational inertia:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0.28 {{key:x²}} 0.35 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.200900$ | $r_1^2 + r_2^2$ sum |
| 2 | `65 {{key:×}} 2 {{key:÷}} {{key:STO}} A` | $0.0000$ | $0.0000$ | $0.0000$ | $6.529250$ | $I_{\text{rim}}$ stored in Reg A |
| 3 | `0.28 {{key:x²}} 20 {{key:×}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $6.529250$ | $0.784000$ | $I_{\text{web}}$ evaluated |
| 4 | `{{key:RCL}} A {{key:+}}` | $0.0000$ | $0.0000$ | $6.529250$ | **$7.313250$** | Grand total flywheel inertia |

What if a rotating body pivots about an offset axle displaced by a perpendicular distance $d$ from its center of mass—like a robotic arm link pivoting about its shoulder joint? **Jakob Steiner's Parallel Axis Theorem** proves that you never need to re-integrate over the solid; you simply add the point-mass transfer term $M d^2$ to the centroidal inertia:
$$I = I_{\text{cm}} + M d^2$$
Suppose a carbon-fiber robotic arm link of mass $m = 3.5\text{ kg}$ and length $L = 0.80\text{ m}$ has centroidal moment of inertia $I_{\text{cm}} = \frac{1}{12}mL^2 \approx 0.186667\text{ kg}\cdot\text{m}^2$ about its midpoint. When the servo motor accelerates the link about a pivot joint at one end (displaced by $d = L/2 = 0.40\text{ m}$ from the center of mass), what is the effective rotational inertia $I_{\text{pivot}}$? By Steiner's theorem:

$$I_{\text{pivot}} = I_{\text{cm}} + m d^2 = 0.186667 + 3.5(0.40^2) = 0.186667 + 0.560000 = \mathbf{0.746667\text{ kg}\cdot\text{m}^2}$$

Keying `{{res:sc32_06_geometry_surface_area_seq_17:keys}}` returns **`{{res:sc32_06_geometry_surface_area_seq_17:value}}`**: shifting the pivot from the center of mass to the endpoint adds $md^2 = \frac{1}{4}mL^2 = 3 I_{\text{cm}}$, quadrupling the inertia to $I_{\text{pivot}} = \frac{1}{3}mL^2 = \mathbf{0.7467\text{ kg}\cdot\text{m}^2}$:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0.80 {{key:x²}} 3.5 {{key:×}} 12 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.186667$ | Center-of-mass inertia $I_{\text{cm}}$ |
| 2 | `0.40 {{key:x²}} 3.5 {{key:×}}` | $0.0000$ | $0.0000$ | $0.186667$ | $0.560000$ | Steiner term $m d^2$ |
| 3 | `{{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.746667$** | Offset pivot inertia $I_{\text{pivot}}$ |

Higher-power radius differences govern hollow spherical shells and tubular drive shafts. Consider a deep-ocean titanium bathysphere pressure hull with outer radius $R_2 = 1.10\text{ m}$, inner radius $R_1 = 0.98\text{ m}$, and titanium alloy density $\rho = 4,500\text{ kg/m}^3$. Its shell volume $V = \frac{4}{3}\pi(R_2^3 - R_1^3) \approx 1.63283\text{ m}^3$ gives a hull mass of $M = 7,347.74\text{ kg}$. To design its attitude-control thrusters, we need its rotational moment of inertia $I$ about any diameter—which is simply the inertia of a solid outer sphere minus a solid inner sphere:

$$I = \frac{2}{5} M \frac{R_2^5 - R_1^5}{R_2^3 - R_1^3} = \frac{2}{5}(7347.74) \frac{1.10^5 - 0.98^5}{1.10^3 - 0.98^3} = 2939.10 \times \frac{0.706589}{0.389808} \approx \mathbf{5,327.42\text{ kg}\cdot\text{m}^2}$$

Notice that if you substitute $M = \frac{4}{3}\pi\rho(R_2^3 - R_1^3)$ algebraically, the $(R_2^3 - R_1^3)$ factor cancels completely to leave $I = \frac{8}{15}\pi\rho(R_2^5 - R_1^5)$. When evaluating directly from the known hull mass $M = 7,347.74\text{ kg}$, the fifth-power difference $(R_2^5 - R_1^5) = 0.706589\text{ m}^5$ waits in Register $Y$ while $(R_2^3 - R_1^3) = 0.389808\text{ m}^3$ forms in Register $X$:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1.1 {{key:ENTER}} 5 {{key:yˣ}} 0.98 {{key:ENTER}} 5 {{key:yˣ}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.706589$ | Fifth-power difference $(R_2^5 - R_1^5)$ |
| 2 | `1.1 {{key:ENTER}} 3 {{key:yˣ}} 0.98 {{key:ENTER}} 3 {{key:yˣ}} {{key:-}}` | $0.706589$ | $0.706589$ | $0.706589$ | $0.389808$ | Third-power difference $(R_2^3 - R_1^3)$ |
| 3 | `{{key:÷}}` | $0.706589$ | $0.706589$ | $0.706589$ | $1.812660$ | Ratio $(R_2^5 - R_1^5)/(R_2^3 - R_1^3)$ |
| 4 | `7347.74 {{key:×}} 2 {{key:×}} 5 {{key:÷}}` | $0.706589$ | $0.706589$ | $0.706589$ | **$5327.4160$** | Mass moment of inertia $I$ in $\text{kg}\cdot\text{m}^2$ |

Similarly, why are automotive and helicopter drive shafts hollow tubes rather than solid bars? Because under torsional twist, shear stress increases linearly from zero at the center to a maximum at the outer skin, so the **polar moment of inertia** $J = \int r^2\,dA = \frac{\pi}{2}(R_o^4 - R_i^4)$ scales with the **fourth power** of radius! Consider a hollow steel drive shaft with outer diameter $D_o = 80.0\text{ mm}$ ($R_o = 40\text{ mm}$) and inner bore diameter $D_i = 70.0\text{ mm}$ ($R_i = 35\text{ mm}$):

$$J = \frac{\pi}{2} (R_o^4 - R_i^4) = \frac{\pi}{2} (40^4 - 35^4) = \frac{\pi}{2} (2,560,000 - 1,500,625) = \frac{\pi}{2} (1,059,375) \approx \mathbf{1,664,071.76\text{ mm}^4}$$

Boring out the inner $70\text{ mm}$ core removes $(35/40)^2 = \mathbf{76.6\%}$ of the steel weight while retaining $1 - (35/40)^4 = \mathbf{41.4\%}$ of the solid shaft's torsional stiffness $J$ (and notice on the keypad that `40 {{key:x²}} {{key:x²}}` computes $40^4$ in three strokes):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `40 {{key:ENTER}} 4 {{key:yˣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2560000.0000$ | Outer radius fourth power $R_o^4$ |
| 2 | `35 {{key:ENTER}} 4 {{key:yˣ}}` | $0.0000$ | $0.0000$ | $2560000.0000$ | $1500625.0000$ | Inner radius fourth power $R_i^4$ |
| 3 | `{{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1059375.0000$ | Difference $(R_o^4 - R_i^4)$ in mm⁴ |
| 4 | `{{key:π}} {{key:×}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1664071.7612$** | Polar moment of inertia $J$ in mm⁴ |

---

## 3D Printer Slicing, Perimeter Shells, Gyroid Infill & Filament Mass Takeoff

Why does every Fused Deposition Modeling (FDM) 3D slicer—when preparing the SC-32 enclosure or your $42.0\text{ mm}$ Gridfinity manipulative kits—have to calculate **both** the total exterior surface area $\Sigma A$ (via `{{key:Σ+}}` in the SC-32 handheld chassis surface area takeoff) and the enclosed interior volume $V$?

Unlike an injection-molded or cast metal part that is $100\%$ solid throughout, a 3D-printed engineering structure is a **composite sandwich shell** (just like the avian wing bones in Chapter 1):
1. **Solid Outer Perimeter Shells ($V_{\text{shell}} \approx A_{\text{surface}} \times N_{\text{walls}} \times w_{\text{line}}$):** The slicer first traces $N_{\text{walls}}$ solid perimeter loops (typically $3$ walls at $w_{\text{line}} = 0.45\text{ mm}$ width, for a $1.35\text{ mm}$ skin thickness $t_{\text{shell}}$) over the entire exterior boundary surface area $A_{\text{surface}} = \Sigma x$ accumulated by `{{key:Σ+}}`.
2. **Sparse Internal Gyroid Infill ($V_{\text{core}} = V_{\text{interior}} \times f_{\text{infill}}$):** The enclosed interior volume $V_{\text{interior}} = V_{\text{total}} - V_{\text{shell}}$ is filled not with solid plastic, but with a periodic minimal-surface **gyroid** or cubic lattice at $f_{\text{infill}} = 15\%\text{--}25\%$ relative density.
3. **Total Filament Mass & Spool Length Takeoff:** Multiplying the combined polymer volume by the density of PLA ($\rho \approx 1.24\text{--}1.25\text{ g/cm}^3 = 0.00124\text{ g/mm}^3$, or PETG at $1.27\text{ g/cm}^3$; compare the hexagonal fastener and brass bar mass takeoffs earlier in this chapter) predicts the exact part mass in grams:
   $$m_{\text{part}} = \rho \left( A_{\text{surface}} \cdot t_{\text{shell}} + V_{\text{interior}} \cdot f_{\text{infill}} \right)$$
   For the SC-32 chassis shell ($A_{\text{surface}} = 25,460\text{ mm}^2$ from our chassis surface area audit), over $70\%$ of the structural filament mass resides in the outer surface shell ($A_{\text{surface}} \cdot t_{\text{shell}}$)—explaining why `{{key:Σ+}}` surface area takeoffs are essential for additive manufacturing cost and weight estimation. And if any cutout or aperture needs to be deducted during the takeoff, a single tap of `{{key:Σ-}}` subtracts that face from $\Sigma x$ on the hardware statistical bus.

### Degenerate Triangles, Accumulator Hygiene, and Dimensional Scaling

Three operational checks keep multi-face mensuration and solid geometry audits free of hidden register contamination or dimensional scaling traps. First, always execute `{{key:CLΣ}}` before beginning a multi-face surface area or weighted-centroid calculation, verifying that $n = 0$ and $\Sigma x = 0.0$ so that no leftover statistical survey or regression data from an earlier session corrupts your geometric summation. Second, when evaluating triangle areas via Heron's formula, remember that the three side lengths must obey the Euclidean triangle inequality ($a + b > c$); if a misread caliper measurement ever specifies two sides whose sum is less than or equal to the third side ($a + b \le c$), the factor $(s - c)$ becomes zero or negative, and pressing `{{key:√x}}` on the negative radicand displays `INVALID DATA` (Code 02)—leaving the stack intact so you can press `{{key:C}}` and inspect the non-closing side lengths. Finally, when computing the volume of a cylinder, sphere, or conical frustum from engineering blueprints (which routinely dimension bore diameters $D, d$ rather than radii $R, r$), always halve diameters on entry or divide the final squared-radius product by $4$ (and cubed-radius product by $8$) to avoid a four-fold or eight-fold volume error.

---

## Summary & Looking Ahead

Chapter 6 developed the geometric capabilities of the RPN stack across planar figures, three-dimensional polyhedra, and spatial coordinate systems. You mastered the signature **Surface Area via Stats Mode (`{{key:Σ+}}`)** technique, piping polygonal face products directly into dedicated hardware accumulators to evaluate complex multi-faceted enclosures without scratchpad notes or parenthesis clutter. By pairing analytic formulas with tactile volume and area decomposition, spatial dimensions translated into compact, deterministic keystroke sequences.

While standard geometric solids possess closed-form algebraic solutions, engineering designs frequently encounter non-linear equilibrium equations and higher-order polynomials where exact radicals do not exist. In **[Chapter 7: Characteristic Polynomials & Brent's Numerical Root Solver](07-polynomials-brent-solver.md)**, you will transition from static spatial shapes to dynamic root extraction. You will use Horner's method for nested polynomial evaluation, extract quadratic and cubic roots via `{{key:POLY}}`, and apply Richard Brent's hybrid root-finding engine (`{{key:SOLVE}}`) to converge on solutions to $10^{-12}$ precision.


