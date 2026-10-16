---
title: "Chapter 6: Analytic & Solid Geometry, Surface Area & Mensuration | SC-32 Manual"
description: "Master 2D plane area, conic sections, the master Surface Area via Stats Mode ([Σ+]) technique, solid mensuration, moments of inertia, and 3D Euclidean metrics on the StackCalc SC-32."
---

# Chapter 6: Analytic & Solid Geometry, Surface Area & Mensuration

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 GEOMETRY // MENSURATION &amp; SPATIAL METRICS</span>
  <span class="te-viewport-status text-sky-400">● 2D CONICS &bull; MASTER SURFACE AREA VIA {{key:Σ+}} &bull; 3D SOLID MENSURATION &bull; INERTIA TENSOR</span>
</div>

## The Application: The Heat Sink, the Rocket Nozzle & The Tyranny of Surface Area

In secondary geometry classes, calculating the surface area of polyhedra is treated as an exercise in accounting: adding up six faces of a cardboard shoe box.

In advanced engineering, **surface area is the governing bottleneck of thermodynamics, aerodynamic friction, chemical catalysis, and semiconductor cooling.**

### The Aerospace & Silicon Bottleneck: Dissipating Gigawatts per Square Centimeter

Inside a modern high-performance processor, billions of nanometer-scale transistors switch at gigahertz frequencies, generating localized thermal flux exceeding $100\text{ W/cm}^2$—a power density rivalling the core heat flux of a nuclear reactor vessel.

Where does that heat go? Under Fourier's Law of Thermal Conduction and Newton's Law of Cooling, heat removal from a solid boundary to ambient fluid is governed by:

$$\dot{Q} = h \cdot A_{\text{surface}} \cdot (T_{\text{solid}} - T_{\text{fluid}})$$

The heat dissipation rate $\dot{Q}$ is directly proportional to exposed surface area $A_{\text{surface}}$. If surface area is inadequate, internal thermal resistance causes junction temperatures to soar, triggering thermal throttling or catastrophic silicon destruction.

This physical reality explains why high-power heat sinks bristling with razor-thin fins dominate power avionics and computer hardware. Machining or extruding aluminum into dozens of parallel fins adds no mass—in fact, it removes material—yet it multiplies the effective convective surface area by more than $2,500\%$.

In real-world aerospace enclosures and consumer instruments, geometry is never composed of tidy textbook cubes. Enclosures feature drafted mold tooling angles, filleted stress-relief radii, cylindrical fastener bosses, and compound chamfers. Rather than scribbling fragile intermediate area calculations across scratch paper, the engineer audits the physical artifact polygon by polygon directly on the RPN stack:
* Primary exterior faces accumulate into the statistical bus via `{{key:Σ+}}`.
* Internal mounting apertures, screw countersinks, and display cutouts subtract via `{{key:Σ-}}`.
* The LCD counter ($n = 1, 2, 3 \dots$) tracks every verified face.
* Recalling `{{key:SUMS}}` → `Σx` instantly produces the certified boundary surface area.

<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>{{key:ALL}}</code> (Full 15-digit internal IEEE-754 mantissa; Standard Base-10 Arithmetic; Degrees angular mode default). All stack operations assume the default 4-stack XYZT architecture.
</div>

---

{{res:sc32_surface_area_sigma:screenshot|Surface area of 10x5x4 prism accumulated via Sigma+ -> 220}}

## The CRA Pedagogical Progression for Spatial Geometry

Spatial geometry on the StackCalc SC-32 transitions from tactile physical manipulatives to clear representational stack registers and rigorous analytical models following the **Concrete-Representational-Abstract (CRA)** instructional framework:

| Pedagogical Tier | Physical & Cognitive Domain | Implementation on the SC-32 RPN Architecture |
| :--- | :--- | :--- |
| **1. Concrete Level**<br>*(Physical & Tactile Grounding)* | • 3D physical manipulatives: Four-color counting tile arrays, precision-milled polyhedra, truncated cone frustums, and 3D-printed chassis test pieces.<br>• Direct caliper measurements: Calibrated vernier dial calipers taking exterior dimensions ($L, W, H$) and wall thicknesses of physical enclosures. | Tactile inspection of hardware drafting datums prior to algebraic entry. |
| **2. Representation Level**<br>*(Stack Register Visualizations)* | • The Statistical Accumulator Bus (`{{key:Σ+}}`): Multi-face 3D surface areas accumulated directly into hardware register $\Sigma x$ with face count $n$ in $X$.<br>• 4-level stack state tables tracing $T, Z, Y, X$ during coordinate rotations, prismatic volume products, and spatial vector transformations. | Dynamic face tally on dot-matrix LCD ($n = 1, 2, 3 \dots$). |
| **3. Abstract Level**<br>*(Analytical Formulations & Tensor Mechanics)* | • Euclidean metric tensors in $\mathbb{R}^3$: $d = \sqrt{\Delta x^2 + \Delta y^2 + \Delta z^2}$<br>• Surface area double integrals: $A = \iint \sqrt{1 + (\partial z/\partial x)^2 + (\partial z/\partial y)^2}\,dA$<br>• Second moments of area and mass moment of inertia tensors:<br>&nbsp;&nbsp;$I_{xx} = \iiint (y^2 + z^2)\rho\,dV, \quad \text{Steiner Parallel-Axis: } I = I_{\text{cm}} + md^2$ | Certified 64-bit IEEE-754 spatial vector and mensuration pipeline. |

{{blocks:sc32_utility_ortho|SC-32 Chassis Technical Drafting Orthographic Projections}}

*Figure 6.1: Technical drafting orthographic projections of the SC-32 handheld chassis ($135 \times 70 \times 16\,\text{mm}$), establishing the datum faces and boundary walls evaluated across the statistical accumulator bus.*

---

## 2D Plane Geometry & Conic Sections

### 2D Plane Area Primitives
The SC-32 evaluates 2D plane geometric regions using rapid, parenthesis-free RPN keystroke pipelines:

| Geometric Region | Analytical Area Formula | RPN Keystroke Pipeline |
| :--- | :--- | :--- |
| **Rectangle** | $A = l \times w$ | `l {{key:ENTER}} w {{key:×}}` |
| **Triangle (Base/Height)** | $A = \frac{1}{2} b \times h$ | `b {{key:ENTER}} h {{key:×}} 2 {{key:÷}}` |
| **Circle** | $A = \pi r^2$ | `r {{keycap:x²}} {{keycap:π}} {{key:×}}` |
| **Circular Sector** | $A = \frac{1}{2} r^2 \theta$ ($\theta$ in rad) | `r {{keycap:x²}} θ {{key:×}} 2 {{key:÷}}` |
| **Circular Annulus** | $A = \pi (R^2 - r^2)$ | `R {{keycap:x²}} r {{keycap:x²}} {{key:-}} {{keycap:π}} {{key:×}}` |
| **Trapezoid** | $A = \frac{1}{2} (a + b) h$ | `a {{key:ENTER}} b {{key:+}} h {{key:×}} 2 {{key:÷}}` |
| **Ellipse** | $A = \pi a b$ | `a {{key:ENTER}} b {{key:×}} {{keycap:π}} {{key:×}}` |
| **Regular $n$-gon** | $A = \frac{1}{4} n s^2 \cot(\pi/n)$ | `s {{keycap:x²}} n {{key:×}} 4 {{key:÷}} (cot) {{key:×}}` |

### Heron's Formula for Arbitrary Triangles
When given three arbitrary side lengths ($a, b, c$), the area is determined without finding altitudes via Heron's formula:
$$s = \frac{a + b + c}{2}, \quad A = \sqrt{s(s - a)(s - b)(s - c)}$$

For a triangle with sides $a = 7.0\text{ m}, b = 9.0\text{ m}, c = 12.0\text{ m}$:
1. Compute semiperimeter $s$:
   `{{res:sc32_06_geometry_surface_area_seq_21:keys}}` $\rightarrow$ $X = 14.0\text{ m}$
2. Store $s$ into variable `S`: `{{key:STO}} S`
3. Evaluate terms on the stack:
   * `{{key:RCL}} S 7 {{key:-}}` $\rightarrow$ $s - a = 7.0$
   * `{{key:RCL}} S 9 {{key:-}} {{key:×}}` $\rightarrow$ $(s-a)(s-b) = 7.0 \times 5.0 = 35.0$
   * `{{key:RCL}} S 12 {{key:-}} {{key:×}}` $\rightarrow$ $(s-a)(s-b)(s-c) = 35.0 \times 2.0 = 70.0$
   * `{{key:RCL}} S {{key:×}} {{key:√x}}` $\rightarrow$ $\sqrt{14.0 \times 70.0} = \sqrt{980.0} = \mathbf{31.304952\text{ m}^2}$

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `7 {{key:ENTER}} 9 {{key:+}} 12 {{key:+}} 2 {{key:÷}} {{key:STO}} S` | $0.0000$ | $0.0000$ | $0.0000$ | $14.0000$ | Semiperimeter $s = (a+b+c)/2$ stored in `S` |
| 2 | `{{key:RCL}} S 7 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $7.0000$ | Factor $(s - a) = 14 - 7 = 7.0$ |
| 3 | `{{key:RCL}} S 9 {{key:-}} {{key:×}}` | $0.0000$ | $0.0000$ | $7.0000$ | $35.0000$ | Multiply by $(s - b) = 5.0$; subtotal $= 35.0$ |
| 4 | `{{key:RCL}} S 12 {{key:-}} {{key:×}}` | $0.0000$ | $0.0000$ | $35.0000$ | $70.0000$ | Multiply by $(s - c) = 2.0$; subtotal $= 70.0$ |
| 5 | `{{key:RCL}} S {{key:×}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$31.304952$** | Multiply by $s$ and take root; Area $= 31.30\text{ m}^2$ |

---

## The Master Surface Area Technique via Stats Mode (`{{key:Σ+}}`)

In mechanical engineering CAD, aerospace design, and additive manufacturing, calculating the total surface area of a 3D solid is traditionally tedious and error-prone. Real-world enclosures feature heterogeneous faces: top/bottom lids, vertical side walls, end faces, fillets, and circular recesses. 

In algebraic calculators, engineers must write dozens of parentheses and risk clobbering temporary memories, or resort to scratch paper:
$$A_{\text{total}} = (2 \times L \times W) + (2 \times L \times H) + (2 \times W \times H) + \dots$$

### The RPN Architectural Breakthrough
On the StackCalc SC-32, the **Statistical Accumulator (`{{key:Σ+}}`)** serves as a dedicated hardware summing bus. 

When you compute the area of any face (or face pair) in Register $X$ and press `{{key:Σ+}}`:
1. The face area $A_k$ is added directly into hardware accumulator $\Sigma x$.
2. The face count $n$ is incremented by 1.
3. Register $X$ displays current face count $n$, and stack lift is safely disarmed for the next face calculation.
4. If you make a mistake on any face, pressing `{{key:Σ-}}` immediately subtracts that erroneous face from the accumulator.
5. When all faces are entered, pressing `{{key:SUMS}}` → `Σx` recalls the exact grand total surface area.

**Zero parentheses, zero named memory variables, and zero scratch paper!**

<div class="admonition note">
<p class="admonition-title">The Master Surface Area Statistical Accumulator Bus</p>
<ol>
  <li><strong>Initialize Accumulator Bus:</strong> Press <code>{{key:CLΣ}}</code> to zero all six internal statistical registers ($\Sigma x = 0, n = 0$).</li>
  <li><strong>Face Pair 1:</strong> Evaluate top/bottom face area $\to$ press <code>{{key:Σ+}}</code> ($\Sigma x \mathrel{+}= A_1, n = 1$).</li>
  <li><strong>Face Pair 2:</strong> Evaluate side walls area $\to$ press <code>{{key:Σ+}}</code> ($\Sigma x \mathrel{+}= A_2, n = 2$).</li>
  <li><strong>Face Pair 3:</strong> Evaluate end caps area $\to$ press <code>{{key:Σ+}}</code> ($\Sigma x \mathrel{+}= A_3, n = 3$).</li>
  <li><strong>Error Correction:</strong> If an erroneous dimension is pushed, immediately press <code>{{key:Σ-}}</code> to deduct the false area without disturbing previous faces.</li>
  <li><strong>Recall Certified Total:</strong> Press <code>{{key:SUMS}}</code> to recall $\Sigma x = A_1 + A_2 + A_3$ with full 12-digit mantissa fidelity.</li>
</ol>
</div>

{{blocks:fraction_gauge_comparison|Fraction Studio Precision Gauge Comparison}}
*Figure 6.2: Precision micrometer comparator gauge verification, pairing physical volumetric measurement directly with statistical accumulator face audits on the RPN stack.*

---

## Grounded Case 1: SC-32 Handheld Chassis Surface Area


Calculate the total external surface area of the StackCalc SC-32 rectangular chassis for thermal dissipation and injection-mold cooling analysis:
* **Length $L$:** $135\text{ mm}$
* **Width $W$:** $70\text{ mm}$
* **Height $H$:** $16\text{ mm}$

Face decomposition into 3 symmetric pairs:
1. **Top & Bottom Lids:** $A_1 = 2 \times (135 \times 70) = 18,900.0\text{ mm}^2$
2. **Left & Right Walls:** $A_2 = 2 \times (135 \times 16) = 4,320.0\text{ mm}^2$
3. **Front & Rear Caps:** $A_3 = 2 \times (70 \times 16) = 2,240.0\text{ mm}^2$
$$\text{Total External Surface Area } A_{\text{total}} = 18,900 + 4,320 + 2,240 = \mathbf{25,460.0\text{ mm}^2}$$

### Step-by-Step RPN Execution Trace
First, zero statistical memory: `{{key:CLΣ}}`

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Accumulator $\Sigma x$ | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `135 {{key:ENTER}} 70 {{key:×}} 2 {{key:×}}` | $0.0$ | $0.0$ | $135.0$ | $18900.0$ | $0.0$ | Top/Bottom area pair evaluated |
| 2 | `{{key:Σ+}}` | $0.0$ | $0.0$ | $135.0$ | **$1.0$** | **$18900.0$** | $n=1$, accumulated into $\Sigma x$ |
| 3 | `135 {{key:ENTER}} 16 {{key:×}} 2 {{key:×}}` | $0.0$ | $135.0$ | $135.0$ | $4320.0$ | $18900.0$ | Side walls area pair evaluated |
| 4 | `{{key:Σ+}}` | $0.0$ | $135.0$ | $135.0$ | **$2.0$** | **$23220.0$** | $n=2$, accumulated into $\Sigma x$ |
| 5 | `70 {{key:ENTER}} 16 {{key:×}} 2 {{key:×}}` | $135.0$ | $135.0$ | $70.0$ | $2240.0$ | $23220.0$ | End caps area pair evaluated |
| 6 | `{{key:Σ+}}` | $135.0$ | $135.0$ | $70.0$ | **$3.0$** | **$25460.0$** | $n=3$, accumulated into $\Sigma x$ |
| 7 | `{{key:SUMS}}` → `Σx` | $135.0$ | $70.0$ | $3.0$ | **$25460.0000$** | $25460.0$ | Total Surface Area recalled! |

The chassis total surface area is **$25,460.0\text{ mm}^2$** ($254.6\text{ cm}^2$).

---

## Grounded Case 2: Cylindrical Battery Pod Surface Area


Calculate the total external surface area of a cylindrical lithium battery compartment:
* **Radius $r$:** $15\text{ mm}$
* **Height $h$:** $65\text{ mm}$

Face decomposition:
1. **Circular Flat Ends (2x):** $A_{\text{ends}} = 2 \times \pi r^2 = 2 \times \pi \times 15^2 = 450\pi \approx 1,413.7167\text{ mm}^2$
2. **Cylindrical Lateral Wall:** $A_{\text{lat}} = 2\pi r h = 2 \times \pi \times 15 \times 65 = 1,950\pi \approx 6,126.1057\text{ mm}^2$
$$\text{Total Surface Area } A_{\text{cyl}} = 450\pi + 1950\pi = 2400\pi \approx \mathbf{7,539.822369\text{ mm}^2}$$

### Step-by-Step RPN Execution Trace
Clear stats: `{{key:CLΣ}}`

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Accumulator $\Sigma x$ | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `15 {{keycap:x²}} {{keycap:π}} {{key:×}} 2 {{key:×}}` | $0.0$ | $0.0$ | $225.0$ | $1413.716694$ | $0.0$ | 2 circular ends evaluated |
| 2 | `{{key:Σ+}}` | $0.0$ | $0.0$ | $225.0$ | **$1.0$** | **$1413.716694$** | $n=1$, accumulated |
| 3 | `2 {{key:ENTER}} {{keycap:π}} {{key:×}} 15 {{key:×}} 65 {{key:×}}`| $0.0$ | $6.283185$ | $94.247780$ | $6126.105675$ | $1413.716694$ | Cylindrical wall evaluated |
| 4 | `{{key:Σ+}}` | $0.0$ | $6.283185$ | $94.247780$ | **$2.0$** | **$7539.822369$** | $n=2$, accumulated |
| 5 | `{{key:SUMS}}` → `Σx` | $6.283185$ | $94.247780$ | $2.0$ | **$7539.822369$** | $7539.822369$ | Total Surface Area recalled! |

The battery pod surface area is **$7,539.82\text{ mm}^2$** ($75.40\text{ cm}^2$).

---

## Solid Mensuration: Volumes of Classical 3D Geometries

| 3D Solid Geometry | Analytical Volume Formula | Total External Surface Area Formula |
| :--- | :--- | :--- |
| **Rectangular Prism** | $V = l \cdot w \cdot h$ | $A = 2(lw + lh + wh)$ |
| **Right Circular Cylinder** | $V = \pi r^2 h$ | $A = 2\pi r^2 + 2\pi r h$ |
| **Right Circular Cone** | $V = \frac{1}{3} \pi r^2 h$ | $A = \pi r^2 + \pi r \sqrt{r^2 + h^2}$ |
| **Sphere** | $V = \frac{4}{3} \pi r^3$ | $A = 4\pi r^2$ |
| **Torus (Major $R$, minor $r$)** | $V = 2\pi^2 R r^2$ | $A = 4\pi^2 R r$ |
| **Frustum of Right Cone** | $V = \frac{1}{3} \pi h (R^2 + Rr + r^2)$ | $A = \pi(R^2 + r^2) + \pi(R + r)s$ |
| **Spherical Cap (height $h$)** | $V = \frac{1}{3} \pi h^2 (3r - h)$ | $A = 2\pi r h$ (curved dome) |
| **Regular Tetrahedron** | $V = \frac{\sqrt{2}}{12} a^3$ | $A = \sqrt{3} a^2$ |
| **Regular Octahedron** | $V = \frac{\sqrt{2}}{3} a^3$ | $A = 2\sqrt{3} a^2$ |
| **Regular Dodecahedron** | $V = \frac{15 + 7\sqrt{5}}{4} a^3$ | $A = 3\sqrt{25 + 10\sqrt{5}}\,a^2$ |
| **Regular Icosahedron** | $V = \frac{5(3 + \sqrt{5})}{12} a^3$ | $A = 5\sqrt{3} a^2$ |

---

## Analytic 3D Spatial Geometry: Distance, Centroid & Mass Moments of Inertia

### 3D Spatial Euclidean Metric
In Cartesian 3-space $\mathbb{R}^3$, the distance between two coordinate stations $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$ is:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$

On the SC-32, evaluate this parenthesis-free by subtracting each coordinate difference, squaring, and summing into the stack:
`x2 {{key:ENTER}} x1 {{key:-}} {{key:x²}}  y2 {{key:ENTER}} y1 {{key:-}} {{key:x²}} {{key:+}}  z2 {{key:ENTER}} z1 {{key:-}} {{key:x²}} {{key:+}} {{key:√x}}`

### Center of Mass (Centroid) via Weighted Mean ($\bar{x}_w$)
When analyzing composite structures consisting of $N$ segments, each with mass $m_k$ and centroid coordinate $x_k$:
$$\bar{x}_{\text{cm}} = \frac{\sum_{k=1}^N m_k x_k}{\sum_{k=1}^N m_k}$$

Because the SC-32 statistical engine maintains both $\Sigma x$ and $\Sigma xy$, you can accumulate each composite part directly with `{{key:Σ+}}`:
* Enter weight/mass $m_k$ into Register $Y$
* Enter coordinate $x_k$ into Register $X$
* Press `{{key:Σ+}}`
* Press `{{key:x̄,ȳ}} {{key:x̄w}}` to retrieve the exact centroid coordinate instantly!

### Mass Moments of Inertia & Steiner's Parallel Axis Theorem
For a rigid body rotating about an arbitrary axis displaced by perpendicular distance $d$ from its center of mass:
$$I = I_{\text{cm}} + M d^2$$
* **Solid Cylinder (axis along symmetry axis):** $I_{\text{cm}} = \frac{1}{2} M R^2$
* **Solid Sphere (any diameter):** $I_{\text{cm}} = \frac{2}{5} M R^2$
* **Thin Spherical Shell:** $I_{\text{cm}} = \frac{2}{3} M R^2$
* **Slender Rod (length $L$, about center):** $I_{\text{cm}} = \frac{1}{12} M L^2$
* **Slender Rod (about end):** $I_{\text{end}} = \frac{1}{12} M L^2 + M (L/2)^2 = \frac{1}{3} M L^2$

---

## Polyhedral Geometry & Statistical Accumulation Notes

### Primitive Decomposition & Statistical Face Accumulation
Traditional geometric mensuration often bogs down in monolithic formulas for composite polyhedra, where dozens of terms are chained into unwieldy algebraic expressions. The SC-32 resolves this complexity by decomposing three-dimensional volumes into discrete planar primitives, using the Statistical Accumulator (`{{key:Σ+}}`) as a running summation bus. Each facet—whether a polygon base, lateral trapezoid, or curved sector—is calculated independently on the 4-level operational stack. Pressing `{{key:Σ+}}` immediately accumulates the facet area into $\Sigma x$ and increments the face counter $n$ without disturbing subsequent stack operations.

### Real-Time Error Correction via {{key:Σ-}}
In multi-face composite assemblies, an erroneous dimension entered halfway through an evaluation would force a complete recalculation on traditional calculators. On the SC-32, the dedicated subtraction key `{{key:Σ-}}` removes the errant face area from $\Sigma x$ and decrements $n$ in a single instruction cycle. The corrected facet is then computed and accumulated with `{{key:Σ+}}`, preserving pipeline continuity and preventing lost state during complex engineering takeoffs.

### Dedicated Hardware Summing Bus vs. Global Register Allocation
In legacy RPN designs such as the HP-32SII and HP-48G, summing multiple geometric facets typically required storing intermediate products in numbered or named global variables. The SC-32's statistical block ($\Sigma x, \Sigma y, \Sigma x^2, \dots$) functions as a hardware-isolated accumulation engine. Because `{{key:Σ+}}` deposits sample count $n$ into Register $X$ while temporarily inhibiting stack lift on subsequent digit entry, the engineer can begin keying the next formula directly without pressing `{{key:C}}` or resetting stack levels.

### Hydraulic Diameters & Geometric Mean Chords
Beyond simple surface summation, combining the accumulated totals via `{{key:SUMS}}` with the parallel resistor key `{{key:x∥y}}` enables instantaneous evaluation of non-circular conduit hydraulic diameters ($D_H = 4A/P$) and aerodynamic mean chords with zero temporary register allocation.

---

## Diagnostic Checkpoints & Singularity Handling

> [!CHECKPOINT]
> **Diagnostic Checkpoint 6.1: Clearing Statistical Accumulators Before Mensuration**  
> Always execute `{{key:CLΣ}}` before beginning a multi-face surface area calculation. Verify that $n = 0$ and $\Sigma x = 0.0$ to ensure no leftover statistical survey or regression data corrupts your geometric summation.

> [!CHECKPOINT]
> **Diagnostic Checkpoint 6.2: Heron's Formula Degenerate Triangle Error**  
> If the sum of any two sides is less than or equal to the third side ($a + b \le c$), the triangle is geometrically impossible. In Heron's formula, $(s - c) \le 0$, resulting in a negative number under the radical. Attempting `{{key:√x}}` raises `Error 01: INVALID DATA`.

> [!CHECKPOINT]
> **Diagnostic Checkpoint 6.3: Frustum Diameter vs Radius Consistency**  
> When calculating the volume of conical or pyramidal frustums, verify whether your inputs are radii ($R, r$) or diameters ($D, d$). Using diameters in a radius formula produces a four-fold volume error!

## Engineering Design Briefing: Spacecraft Power & Thermal Bus Design (Problems 6.1 through 6.40)

> **Hands-On Studio Proof: Polyhedral Face Nets &rarr; Calculator**  
> Before summing polygonal face areas and complex moments of inertia on the SC-32, manipulate physical geometric solid nets and tile arrays (`docs/assets/manuals/counting_tiles_array_3x8.png`) alongside physical chassis datums on the precision micrometer stage (`docs/assets/renders/fraction-studio-gauge-comparison.png`). Verifying face counts and dimensional boundaries by hand grounds the statistical accumulator pipeline (`{{key:Σ+}}`) before calculating thermal dissipation envelopes for flight hardware.

The following 40 professional engineering case studies span spacecraft radiator sizing, pressure vessel stress geometry, optical paraboloid mensuration, and structural moments of inertia.

### Problem 6.1: Circular Annulus Area (Flanged Pipe Gasket)
**Mechanical Context:** A neoprene flange gasket has outer radius $R = 85.0\text{ mm}$ and inner bore radius $r = 50.0\text{ mm}$. Calculate face surface area:
$$A = \pi (R^2 - r^2) = \pi (85^2 - 50^2) = \pi (7225 - 2500) = 4725\pi \approx \mathbf{14,844.0253\text{ mm}^2}$$

**Keystrokes:** `{{res:sc32_06_geometry_surface_area_seq_01:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_01:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `85 {{keycap:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $7225.0000$ | $R^2$ evaluated |
| 2 | `50 {{keycap:x²}}` | $0.0000$ | $0.0000$ | $7225.0000$ | $2500.0000$ | $r^2$ evaluated |
| 3 | `{{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $4725.0000$ | $R^2 - r^2$ |
| 4 | `{{keycap:π}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$14844.025289$** | Annulus Area in mm² |

Result: **$14,844.03\text{ mm}^2$** ($148.44\text{ cm}^2$).

---

### Problem 6.2: Regular Octagon Enclosure Face Area
**Manufacturing Context:** An octagonal equipment enclosure is fabricated from sheet metal with edge length $s = 65.0\text{ mm}$:
$$A = 2 (1 + \sqrt{2}) s^2 \approx 4.828427 \times 65^2 = 4.828427 \times 4225 = \mathbf{20,400.1047\text{ mm}^2}$$

**Keystrokes:** `{{res:sc32_06_geometry_surface_area_seq_02:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_02:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `2 {{key:√x}} 1 {{key:+}} 2 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $4.828427$ | $2(1 + \sqrt{2})$ factor |
| 2 | `65 {{keycap:x²}}` | $0.0000$ | $0.0000$ | $4.828427$ | $4225.0000$ | $s^2$ evaluated |
| 3 | `{{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$20400.104684$** | Octagon Area in mm² |

Result: **$20,400.10\text{ mm}^2$**.

---

### Problem 6.3: Elliptical Pressure Vessel Manway Area & Perimeter
**Pressure Vessel Context:** A vessel inspection hatch is elliptical with semimajor axis $a = 250.0\text{ mm}$ and semiminor axis $b = 150.0\text{ mm}$.
1. Area $A = \pi a b = \pi \times 250 \times 150 = 37,500\pi \approx \mathbf{117,809.72\text{ mm}^2}$
2. Ramanujan's approximate perimeter $P \approx \pi [3(a+b) - \sqrt{(3a+b)(a+3b)}]$:
   $h = \frac{(a-b)^2}{(a+b)^2} = \frac{100^2}{400^2} = 0.0625 \implies P \approx \pi(a+b)(1 + \frac{3h}{10 + \sqrt{4 - 3h}}) \approx \mathbf{1,276.26\text{ mm}}$

**Keystrokes (Area):** `{{res:sc32_06_geometry_surface_area_seq_03:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_03:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `250 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $250.0000$ | $250.0000$ | Semimajor axis $a$ pushed |
| 2 | `150 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $37500.0000$ | Product $a \times b$ |
| 3 | `{{keycap:π}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$117809.724510$** | Area $A = \pi a b$ in mm² |

Result: **$117,809.72\text{ mm}^2$** ($1,178.10\text{ cm}^2$).

---

### Problem 6.4: Conical Frustum Storage Hopper Volume
**Bulk Handling Context:** A grain hopper has upper radius $R = 1.80\text{ m}$, lower discharge radius $r = 0.40\text{ m}$, and height $h = 2.50\text{ m}$:
$$V = \frac{1}{3} \pi h (R^2 + R r + r^2) = \frac{2.5\pi}{3} (1.8^2 + 1.8(0.4) + 0.4^2) = \frac{2.5\pi}{3} (3.24 + 0.72 + 0.16) = \frac{2.5\pi}{3} (4.12) = \mathbf{10.7861\text{ m}^3}$$

**Keystrokes:** `{{res:sc32_06_geometry_surface_area_seq_04:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_04:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1.8 {{keycap:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.2400$ | $R^2$ |
| 2 | `1.8 {{key:ENTER}} 0.4 {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.9600$ | $R^2 + Rr$ |
| 3 | `0.4 {{keycap:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $4.1200$ | $R^2 + Rr + r^2$ |
| 4 | `{{keycap:π}} {{key:×}} 2.5 {{key:×}} 3 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$10.786135$** | Frustum volume in m³ |

Result: **$10.7861\text{ m}^3$** ($10,786.1\text{ liters}$).

---

### Problem 6.5: Torus Volume and Surface Area (Hydraulic O-Ring)
**Seals Context:** An elastomer O-ring has major mean radius $R = 45.0\text{ mm}$ and cross-sectional circular radius $r = 3.5\text{ mm}$.
1. Volume $V = 2\pi^2 R r^2 = 2 \pi^2 (45) (3.5^2) = 2 \pi^2 (45) (12.25) \approx \mathbf{10,880.89\text{ mm}^3}$
2. Surface Area $A = 4\pi^2 R r = 4 \pi^2 (45) (3.5) \approx \mathbf{6,217.65\text{ mm}^2}$

**Keystrokes (Volume):** `{{res:sc32_06_geometry_surface_area_seq_05:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_05:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{keycap:π}} {{keycap:x²}} 2 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $19.739209$ | $2\pi^2$ evaluated |
| 2 | `45 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $888.264396$ | $2\pi^2 R$ |
| 3 | `3.5 {{keycap:x²}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$10880.887208$** | Torus Volume $V$ in mm³ |

**Keystrokes (Surface Area):** `{{res:sc32_06_geometry_surface_area_seq_06:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_06:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{keycap:π}} {{keycap:x²}} 4 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $39.478418$ | $4\pi^2$ evaluated |
| 2 | `45 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1776.528792$ | $4\pi^2 R$ with $R = 45\text{ mm}$ |
| 3 | `3.5 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$6217.850773$** | Torus Surface Area $A = 4\pi^2 R r$ in mm² |

---

### Problem 6.6: Spherical Storage Tank Segment (Cap) Volume
**Chemical Context:** A spherical chemical tank of radius $R = 4.0\text{ m}$ is filled with liquid to depth $h = 1.5\text{ m}$. Calculate liquid volume:
$$V = \frac{1}{3} \pi h^2 (3R - h) = \frac{\pi (1.5^2)}{3} (3(4.0) - 1.5) = \frac{2.25\pi}{3} (10.5) = 0.75\pi \times 10.5 = \mathbf{24.7400\text{ m}^3}$$

**Keystrokes:** `{{res:sc32_06_geometry_surface_area_seq_07:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_07:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `4 {{key:ENTER}} 3 {{key:×}} 1.5 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $10.5000$ | $3R - h$ term |
| 2 | `1.5 {{keycap:x²}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $23.6250$ | $h^2(3R - h)$ |
| 3 | `{{keycap:π}} {{key:×}} 3 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$24.740042$** | Liquid volume in m³ |

Result: **$24.7400\text{ m}^3$** ($24,740.0\text{ liters}$).

---

### Problem 6.7: Truncated Pyramidal Monument Volume
**Civil Architecture Context:** A stone pedestal is a truncated square pyramid: lower base side $a = 3.20\text{ m}$, upper base side $b = 1.80\text{ m}$, height $h = 4.50\text{ m}$.
Base areas: $A_1 = 3.2^2 = 10.24\text{ m}^2$, $A_2 = 1.8^2 = 3.24\text{ m}^2$:
$$V = \frac{h}{3} (A_1 + A_2 + \sqrt{A_1 A_2}) = \frac{4.5}{3} (10.24 + 3.24 + \sqrt{33.1776}) = 1.5 \times (13.48 + 5.76) = 1.5 \times 19.24 = \mathbf{28.86\text{ m}^3}$$

**Keystrokes:** `{{res:sc32_06_geometry_surface_area_seq_08:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_08:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `3.2 {{keycap:x²}} {{key:STO}} 1` | $0.0000$ | $0.0000$ | $0.0000$ | $10.2400$ | Base 1 area stored in Reg 1 |
| 2 | `1.8 {{keycap:x²}} {{key:STO}} 2` | $0.0000$ | $0.0000$ | $10.2400$ | $3.2400$ | Base 2 area stored in Reg 2 |
| 3 | `{{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $13.4800$ | Sum $A_1 + A_2$ |
| 4 | `{{key:RCL}} 1 {{key:RCL}} 2 {{key:×}} {{key:√x}}` | $0.0000$ | $0.0000$ | $13.4800$ | $5.7600$ | Geometric mean $\sqrt{A_1 A_2}$ |
| 5 | `{{key:+}} 4.5 {{key:×}} 3 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$28.860000$** | Pyramidal frustum volume $V$ |

Result: **$28.8600\text{ m}^3$**.

---

### Problem 6.8: Regular Icosahedron Dice Volume and Area
**STEM Maker Context:** A 20-sided gaming die has edge length $a = 18.0\text{ mm}$.
1. Surface Area $A = 5\sqrt{3} a^2 = 5 \sqrt{3} (18^2) = 5\sqrt{3}(324) \approx \mathbf{2,805.9223\text{ mm}^2}$
2. Volume $V = \frac{5(3 + \sqrt{5})}{12} a^3 = \frac{5(5.236068)}{12} (5832) \approx \mathbf{12,713.41\text{ mm}^3}$

**Keystrokes (Volume):** `{{res:sc32_06_geometry_surface_area_seq_09:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_09:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `5 {{key:√x}} 3 {{key:+}} 5 {{key:×}} 12 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.181695$ | Volume coefficient evaluated |
| 2 | `18 {{key:ENTER}} 3 {{key:yˣ}}` | $0.0000$ | $0.0000$ | $2.181695$ | $5832.0000$ | Edge cubed $a^3$ |
| 3 | `{{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$12713.409324$** | Icosahedron Volume in mm³ |

Result: **$V = 12,713.41\text{ mm}^3$**, **$A = 2,805.92\text{ mm}^2$**.

---

### Problem 6.9: Regular Dodecahedron Volume
**Mathematics Context:** 12-sided solid with edge $a = 12.0\text{ mm}$:
$$V = \frac{15 + 7\sqrt{5}}{4} a^3 \approx \frac{15 + 15.652476}{4} (1728) = 7.663119 \times 1728 = \mathbf{13,241.87\text{ mm}^3}$$

**Keystrokes:** `{{res:sc32_06_geometry_surface_area_seq_10:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_10:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `5 {{key:√x}} 7 {{key:×}} 15 {{key:+}} 4 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $7.663119$ | Volume coefficient evaluated |
| 2 | `12 {{key:ENTER}} 3 {{key:yˣ}}` | $0.0000$ | $0.0000$ | $7.663119$ | $1728.0000$ | $a^3 = 12^3$ |
| 3 | `{{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$13241.869389$** | Dodecahedron Volume in mm³ |

Result: **$13,241.87\text{ mm}^3$**.

---

### Problem 6.10: Regular Tetrahedron Height, Area & Volume
**Geometry Context:** Tetrahedron with edge $a = 50.0\text{ mm}$:
* Altitude: $h = \sqrt{2/3} a \approx 0.816497 \times 50 = \mathbf{40.8248\text{ mm}}$
* Surface Area: $A = \sqrt{3} a^2 = \sqrt{3}(2500) = \mathbf{4,330.1270\text{ mm}^2}$
* Volume: $V = \frac{\sqrt{2}}{12} a^3 = \frac{\sqrt{2}}{12} (125,000) = \mathbf{14,731.3913\text{ mm}^3}$

**Keystrokes (Volume):** `{{res:sc32_06_geometry_surface_area_seq_11:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_11:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `2 {{key:√x}} 12 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.117851$ | Coefficient $\sqrt{2}/12$ |
| 2 | `50 {{key:ENTER}} 3 {{key:yˣ}}` | $0.0000$ | $0.0000$ | $0.117851$ | $125000.0000$ | $a^3 = 50^3$ |
| 3 | `{{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$14731.391275$** | Tetrahedron Volume in mm³ |

Result: **$h = 40.82\text{ mm}$**, **$A = 4,330.13\text{ mm}^2$**, **$V = 14,731.39\text{ mm}^3$**.

---

### Problem 6.11: Multi-Face Machine Casting Surface Area via `{{key:Σ+}}`
**Manufacturing Context:** A stepped cast-iron machine bracket consists of:
* Base block ($120 \times 80 \times 30\text{ mm}$): 5 exposed faces (bottom, 2 sides, 2 ends)
* Upper boss ($60 \times 40 \times 25\text{ mm}$): 4 vertical faces + top face minus base contact area
Accumulate into `{{key:Σ+}}`:
1. Bottom: `120 {{key:ENTER}} 80 {{key:×}} {{key:Σ+}}` ($n=1, A=9600$)
2. Base sides (2x): `120 {{key:ENTER}} 30 {{key:×}} 2 {{key:×}} {{key:Σ+}}` ($n=2, A=7200$)
3. Base ends (2x): `80 {{key:ENTER}} 30 {{key:×}} 2 {{key:×}} {{key:Σ+}}` ($n=3, A=4800$)
4. Upper sides (2x): `60 {{key:ENTER}} 25 {{key:×}} 2 {{key:×}} {{key:Σ+}}` ($n=4, A=3000$)
5. Upper ends (2x): `40 {{key:ENTER}} 25 {{key:×}} 2 {{key:×}} {{key:Σ+}}` ($n=5, A=2000$)
6. Top remaining: `120 {{key:ENTER}} 80 {{key:×}} 60 {{key:ENTER}} 40 {{key:×}} {{key:-}} 60 {{key:ENTER}} 40 {{key:×}} {{key:+}} {{key:Σ+}}` ($n=6, A=9600$)
Recall total surface area: `{{key:SUMS}}` → `Σx` $\implies$ **$36,200.0\text{ mm}^2$**. Zero scratch paper!

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:CLΣ}} 120 {{key:ENTER}} 80 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $120.0000$ | $1.0000$ | Bottom face area $9,600.0\text{ mm}^2$ accumulated ($n=1$) |
| 2 | `120 {{key:ENTER}} 30 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $120.0000$ | $2.0000$ | 2 base sides $7,200.0\text{ mm}^2$ accumulated ($n=2$) |
| 3 | `80 {{key:ENTER}} 30 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $80.0000$ | $3.0000$ | 2 base ends $4,800.0\text{ mm}^2$ accumulated ($n=3$) |
| 4 | `60 {{key:ENTER}} 25 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $60.0000$ | $4.0000$ | 2 upper sides $3,000.0\text{ mm}^2$ accumulated ($n=4$) |
| 5 | `40 {{key:ENTER}} 25 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $40.0000$ | $5.0000$ | 2 upper ends $2,000.0\text{ mm}^2$ accumulated ($n=5$) |
| 6 | `120 {{key:ENTER}} 80 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $120.0000$ | $6.0000$ | Net top face area $9,600.0\text{ mm}^2$ accumulated ($n=6$) |
| 7 | `{{key:SUMS}}` | $0.0000$ | $0.0000$ | $6.0000$ | **$36200.0000$** | Recall total casting surface area $\Sigma x$ |

---

### Problem 6.12: Extruded Heat Sink Fin Array Surface Area via `{{key:Σ+}}`
**Thermal Context:** Heat sink base $100 \times 100\text{ mm}$ with 8 vertical fins ($100\text{ mm}$ long, $35\text{ mm}$ tall, $2\text{ mm}$ thick):
* Fin sides (16 faces): $16 \times (100 \times 35) = 56,000\text{ mm}^2$
* Fin tips (8 faces): $8 \times (100 \times 2) = 1,600\text{ mm}^2$
* Base exposed top: $(100 \times 100) - 8 \times (100 \times 2) = 8,400\text{ mm}^2$
* Base flat bottom: $100 \times 100 = 10,000\text{ mm}^2$
Accumulate all 4 elements via `{{key:Σ+}}` $\implies$ **Total Surface Area = $76,000.0\text{ mm}^2$** ($760.0\text{ cm}^2$).

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `{{key:CLΣ}}` — Zero the statistical accumulators ($n = 0, \Sigma x = 0$) before summing composite geometric faces.
2. **Evaluate Each Sub-Feature in $(Y, X)$:** Compute each individual face area or sub-volume directly on the RPN stack from the inside out and press `{{key:Σ+}}` to add it into the running $\Sigma x$ register while incrementing the face counter $n$ in Register $X$.
3. `{{key:Σx}}` — Recall the accumulated total surface area or composite volume into Register $X$ without touching general-purpose storage registers.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:CLΣ}} 16 {{key:ENTER}} 100 {{key:×}} 35 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $1600.0000$ | $1.0000$ | 16 fin sides ($56,000.0\text{ mm}^2$) accumulated ($n=1$) |
| 2 | `8 {{key:ENTER}} 100 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $800.0000$ | $2.0000$ | 8 fin tips ($1,600.0\text{ mm}^2$) accumulated ($n=2$) |
| 3 | `100 {{key:ENTER}} 100 {{key:×}} 1600 {{key:-}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $100.0000$ | $3.0000$ | Base exposed top ($8,400.0\text{ mm}^2$) accumulated ($n=3$) |
| 4 | `100 {{key:ENTER}} 100 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $100.0000$ | $4.0000$ | Base flat bottom ($10,000.0\text{ mm}^2$) accumulated ($n=4$) |
| 5 | `{{key:SUMS}}` | $0.0000$ | $0.0000$ | $4.0000$ | **$76000.0000$** | Recall total heat sink surface area $\Sigma x$ |

---

### Problem 6.13: 3D Euclidean Distance Between Aerospace Telemetry Nodes
**Avionics Context:** Station $A$ at coordinates $(1250, -420, 850)\text{ m}$, Station $B$ at $(2100, 680, 1400)\text{ m}$:
$$\Delta x = 2100 - 1250 = 850\text{ m}, \quad \Delta y = 680 - (-420) = 1100\text{ m}, \quad \Delta z = 1400 - 850 = 550\text{ m}$$
$$d = \sqrt{850^2 + 1100^2 + 550^2} = \sqrt{722500 + 1210000 + 302500} = \sqrt{2235000} \approx \mathbf{1,494.9916\text{ meters}}$$

**Keystrokes:** `{{res:sc32_06_geometry_surface_area_seq_12:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_12:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `2100 {{key:ENTER}} 1250 {{key:-}} {{keycap:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $722500.0000$ | $\Delta x^2 = 850^2$ |
| 2 | `680 {{key:ENTER}} 420 {{key:+/-}} {{key:-}} {{keycap:x²}}` | $0.0000$ | $0.0000$ | $722500.0000$ | $1210000.0000$ | $\Delta y^2 = 1100^2$ |
| 3 | `{{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1932500.0000$ | $\Delta x^2 + \Delta y^2$ |
| 4 | `1400 {{key:ENTER}} 850 {{key:-}} {{keycap:x²}}` | $0.0000$ | $0.0000$ | $1932500.0000$ | $302500.0000$ | $\Delta z^2 = 550^2$ |
| 5 | `{{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1494.991639$** | 3D Distance $d$ in meters |

Result: **$1,494.99\text{ meters}$**.

---

### Problem 6.14: Direction Cosines of 3D Vector
**Mechanics Context:** For vector $\vec{V} = (850, 1100, 550)\text{ m}$ with magnitude $|\vec{V}| = 1494.9916\text{ m}$:
* $\cos\alpha = 850 / 1494.9916 = \mathbf{0.568565} \implies \alpha = 55.35^\circ$
* $\cos\beta = 1100 / 1494.9916 = \mathbf{0.735790} \implies \beta = 42.63^\circ$
* $\cos\gamma = 550 / 1494.9916 = \mathbf{0.367895} \implies \gamma = 68.41^\circ$

**Keystrokes:** `{{res:sc32_06_geometry_surface_area_seq_13:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_13:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1494.9916 {{key:STO}} D` | $0.0000$ | $0.0000$ | $0.0000$ | $1494.9916$ | Vector magnitude saved |
| 2 | `850 {{key:RCL}} D {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.568565$** | $\cos\alpha$ (X-direction cosine) |
| 3 | `1100 {{key:RCL}} D {{key:÷}}` | $0.0000$ | $0.0000$ | $0.568565$ | **$0.735790$** | $\cos\beta$ (Y-direction cosine) |
| 4 | `550 {{key:RCL}} D {{key:÷}}` | $0.0000$ | $0.568565$ | $0.735790$ | **$0.367895$** | $\cos\gamma$ (Z-direction cosine) |

Check: $0.568565^2 + 0.735790^2 + 0.367895^2 \equiv \mathbf{1.000000}$.

---

### Problem 6.15: Vector Cross Product in 3-Space ($\vec{A} \times \vec{B}$)
**Physics Context:** $\vec{A} = (3, -2, 4)$, $\vec{B} = (1, 5, -2)$:
$$\vec{C} = \vec{A} \times \vec{B} = (A_y B_z - A_z B_y)\hat{i} + (A_z B_x - A_x B_z)\hat{j} + (A_x B_y - A_y B_x)\hat{k}$$
* $C_x = (-2)(-2) - (4)(5) = 4 - 20 = \mathbf{-16}$
* $C_y = (4)(1) - (3)(-2) = 4 - (-6) = \mathbf{10}$
* $C_z = (3)(5) - (-2)(1) = 15 - (-2) = \mathbf{17}$
$$\vec{C} = (-16, 10, 17) \implies |\vec{C}| = \sqrt{256 + 100 + 289} = \sqrt{645} \approx \mathbf{25.3969}$$

**Keystrokes (Magnitude):** `{{res:sc32_06_geometry_surface_area_seq_14:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_14:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `16 {{keycap:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $256.0000$ | $C_x^2$ |
| 2 | `10 {{keycap:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $356.0000$ | $C_x^2 + C_y^2$ |
| 3 | `17 {{keycap:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $645.0000$ | Sum of squares |
| 4 | `{{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$25.396850$** | Cross product magnitude $|\vec{C}|$ |

Result: **$\vec{C} = (-16, 10, 17), |\vec{C}| = 25.40$**.

---

### Problem 6.16: Dihedral Angle Between Two Intersecting Planes
**Crystallography Context:** Plane 1: $2x + y - 2z = 5 \implies \vec{n}_1 = (2, 1, -2)$. Plane 2: $x - 2y + 2z = 3 \implies \vec{n}_2 = (1, -2, 2)$:
$$\cos\theta = \frac{|\vec{n}_1 \cdot \vec{n}_2|}{|\vec{n}_1| |\vec{n}_2|} = \frac{|(2)(1) + (1)(-2) + (-2)(2)|}{\sqrt{4+1+4} \sqrt{1+4+4}} = \frac{|2 - 2 - 4|}{3 \times 3} = \frac{4}{9} \approx 0.444444$$
$$\theta = \arccos(4/9) \approx \mathbf{63.6122^\circ}$$

**Keystrokes:** `{{res:sc32_06_geometry_surface_area_seq_15:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_15:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `4 {{key:ENTER}} 9 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.444444$ | Ratio $4/9$ evaluated |
| 2 | `{{key:ACOS}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$63.612200$** | Dihedral angle $\theta$ in degrees |

Result: **$\theta = 63.6122^\circ$**.

---

### Problem 6.17: Centroid of Composite 3-Section Beam via `{{key:Σ+}}`
**Structural Context:** Steel girder built from 3 plates:
* Bottom flange: $m_1 = 40\text{ kg}$, $y_1 = 10\text{ mm}$
* Web: $m_2 = 60\text{ kg}$, $y_2 = 160\text{ mm}$
* Top flange: $m_3 = 30\text{ kg}$, $y_3 = 310\text{ mm}$
Accumulate $m$ in $Y$, $y$ in $X$:
1. `40 {{key:ENTER}} 10 {{key:Σ+}}`
2. `60 {{key:ENTER}} 160 {{key:Σ+}}`
3. `30 {{key:ENTER}} 310 {{key:Σ+}}`

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:CLΣ}}` | $0.0$ | $0.0$ | $0.0$ | $0.0$ | Accumulators cleared |
| 2 | `40 {{key:ENTER}} 10 {{key:Σ+}}` | $0.0$ | $0.0$ | $40.0$ | $1.0$ | Bottom flange ($n=1$) |
| 3 | `60 {{key:ENTER}} 160 {{key:Σ+}}`| $0.0$ | $40.0$ | $60.0$ | $2.0$ | Web section ($n=2$) |
| 4 | `30 {{key:ENTER}} 310 {{key:Σ+}}`| $40.0$ | $60.0$ | $30.0$ | $3.0$ | Top flange ($n=3$) |
| 5 | `{{key:x̄,ȳ}} {{key:x̄w}}` | $60.0$ | $30.0$ | $3.0$ | **$148.461538$** | Weighted centroid $\bar{y}$ in mm |

Recall weighted mean centroid: `{{key:x̄,ȳ}} {{key:x̄w}}` $\implies$ **$\bar{y} = 148.4615\text{ mm}$**. Total mass $M = 130\text{ kg}$.

---

### Problem 6.18: Mass Moment of Inertia of Flywheel with Rim & Web
**Machinery Context:** Cast-iron flywheel with total mass $M = 85\text{ kg}$:
* Heavy outer rim: $M_{\text{rim}} = 65\text{ kg}$, inner radius $r_1 = 0.28\text{ m}$, outer $r_2 = 0.35\text{ m}$:
  $$I_{\text{rim}} = \frac{1}{2} M_{\text{rim}} (r_1^2 + r_2^2) = 0.5 \times 65 \times (0.28^2 + 0.35^2) = 32.5 \times (0.0784 + 0.1225) = 32.5 \times 0.2009 = \mathbf{6.52925\text{ kg}\cdot\text{m}^2}$$
* Disk web: $M_{\text{web}} = 20\text{ kg}$, radius $R = 0.28\text{ m}$:
  $$I_{\text{web}} = \frac{1}{2} M_{\text{web}} R^2 = 0.5 \times 20 \times 0.28^2 = 10 \times 0.0784 = \mathbf{0.78400\text{ kg}\cdot\text{m}^2}$$
* Total: $I_{\text{total}} = 6.52925 + 0.78400 = \mathbf{7.31325\text{ kg}\cdot\text{m}^2}$.

**Keystrokes:** `{{res:sc32_06_geometry_surface_area_seq_16:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_16:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0.28 {{keycap:x²}} 0.35 {{keycap:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.200900$ | $r_1^2 + r_2^2$ sum |
| 2 | `65 {{key:×}} 2 {{key:÷}} {{key:STO}} 1` | $0.0000$ | $0.0000$ | $0.0000$ | $6.529250$ | $I_{\text{rim}}$ stored in Reg 1 |
| 3 | `0.28 {{keycap:x²}} 20 {{key:×}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $6.529250$ | $0.784000$ | $I_{\text{web}}$ evaluated |
| 4 | `{{key:RCL}} 1 {{key:+}}` | $0.0000$ | $0.0000$ | $0.784000$ | **$7.313250$** | Grand total flywheel inertia |

Result: **$I_{\text{total}} = 7.31325\text{ kg}\cdot\text{m}^2$**.

---

### Problem 6.19: Steiner's Parallel Axis Theorem for Offset Robotic Link
**Robotics Context:** Carbon-fiber arm link of mass $m = 3.5\text{ kg}$, length $L = 0.80\text{ m}$. Center of mass inertia $I_{\text{cm}} = \frac{1}{12} m L^2 = \frac{3.5 \times 0.64}{12} \approx 0.186667\text{ kg}\cdot\text{m}^2$.
Compute moment of inertia about pivot joint at link end ($d = L/2 = 0.40\text{ m}$):
$$I_{\text{pivot}} = I_{\text{cm}} + m d^2 = 0.186667 + 3.5(0.40^2) = 0.186667 + 3.5(0.16) = 0.186667 + 0.560000 = \mathbf{0.746667\text{ kg}\cdot\text{m}^2}$$

**Keystrokes:** `{{res:sc32_06_geometry_surface_area_seq_17:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_17:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0.80 {{keycap:x²}} 3.5 {{key:×}} 12 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.186667$ | Center-of-mass inertia $I_{\text{cm}}$ |
| 2 | `0.40 {{keycap:x²}} 3.5 {{key:×}}` | $0.0000$ | $0.0000$ | $0.186667$ | $0.560000$ | Steiner term $m d^2$ |
| 3 | `{{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.746667$** | Offset pivot inertia $I_{\text{pivot}}$ |

Result: **$I_{\text{pivot}} = 0.7467\text{ kg}\cdot\text{m}^2$**.

---

### Problem 6.20: Radius of Gyration ($k$) of Rotating Turbine Disk
**Turbomachinery Context:** Rotor disk with moment of inertia $I = 14.8\text{ kg}\cdot\text{m}^2$ and mass $M = 42.0\text{ kg}$:
$$k = \sqrt{\frac{I}{M}} = \sqrt{\frac{14.8}{42.0}} = \sqrt{0.352381} = \mathbf{0.593617\text{ meters}} = 593.6\text{ mm}$$

**Keystrokes:** `{{res:sc32_06_geometry_surface_area_seq_18:keys}}` $\rightarrow$ **`{{res:sc32_06_geometry_surface_area_seq_18:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `14.8 {{key:ENTER}} 42 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.352381$ | Ratio $I/M$ |
| 2 | `{{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.593617$** | Radius of gyration $k$ in meters |

Result: **$k = 0.5936\text{ m}$** ($593.6\text{ mm}$).

---

### Problem 6.21: Spherical Triangle Area via Girard's Theorem
**Geodesy Context:** On a sphere of radius $R = 6,371.0\text{ km}$, a spherical triangle has interior angles $\alpha = 82.5^\circ$, $\beta = 68.2^\circ$, $\gamma = 44.7^\circ$:
$$\text{Spherical Excess } E = (\alpha + \beta + \gamma - 180^\circ) = (82.5 + 68.2 + 44.7 - 180) = 195.4^\circ - 180^\circ = 15.4^\circ$$
$$E_{\text{rad}} = 15.4 \times \frac{\pi}{180} \approx 0.2687807\text{ rad}$$
$$\text{Area } A = R^2 E_{\text{rad}} = 6371^2 \times 0.2687807 \approx \mathbf{10,911,102.5\text{ km}^2}$$

> **Named RPN Stack Idiom: *The Spherical Excess Pipeline*** — Sum spherical vertex angles in degrees, subtract $180^\circ$ to find spherical excess $E$, convert to radians, and scale by Earth radius squared without scratch registers {{cite:gauss1809,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `85` `{{key:ENTER}}` `72` `{{key:+}}` `68` `{{key:+}}` — Sum triangle vertex angles ($A + B + C = 225.0^\circ$).
2. `180` `{{key:-}}` — Subtract Euclidean planar sum ($180.0^\circ$) to determine spherical excess ($E = 45.0^\circ$).
3. `{{key:π}}` `{{key:×}}` `180` `{{key:÷}}` — Convert spherical excess to radians ($E_{\text{rad}} \approx 0.785398\text{ sr}$).
4. `6371` `{{key:x²}}` `{{key:×}}` — Scale by mean Earth radius squared, establishing spherical triangle area $A \approx \mathbf{3.1879 \times 10^7\text{ km}^2}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `82.5 {{key:ENTER}} 68.2 {{key:+}} 44.7 {{key:+}}` | $0.0000$ | $0.0000$ | $82.5000$ | $195.4000$ | Interior angle sum $\alpha + \beta + \gamma$ in degrees |
| 2 | `180 {{key:-}}` | $0.0000$ | $0.0000$ | $82.5000$ | $15.4000$ | Spherical excess $E = 15.4^\circ$ |
| 3 | `{{keycap:π}} {{key:×}} 180 {{key:÷}}` | $0.0000$ | $0.0000$ | $82.5000$ | $0.268781$ | Excess in radians $E_{\text{rad}} \approx 0.268781\text{ rad}$ |
| 4 | `6371 {{keycap:x²}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$10911102.50$** | Spherical triangle area $A = R^2 E_{\text{rad}}$ in km² |

---

### Problem 6.22: Parabolic Solar Reflector Surface Area
**Renewable Energy Context:** Deep parabolic dish $z = \frac{x^2 + y^2}{4f}$ with focal length $f = 1.20\text{ m}$ and rim radius $R = 2.0\text{ m}$.
Surface area of revolution:
$$A = \frac{8\pi f^2}{3} \left[ \left(1 + \frac{R^2}{4f^2}\right)^{3/2} - 1 \right]$$
For $f = 1.2, R = 2.0$: $\frac{R^2}{4f^2} = \frac{4}{4(1.44)} = \frac{1}{1.44} \approx 0.694444$.
$1 + 0.694444 = 1.694444 \implies (1.694444)^{1.5} \approx 2.205739$.
$$A = \frac{8\pi(1.44)}{3} [2.205739 - 1] = 3.84\pi \times 1.205739 \approx \mathbf{14.5458\text{ m}^2}$$

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `{{key:CLΣ}}` — Zero the statistical accumulators ($n = 0, \Sigma x = 0$) before summing composite geometric faces.
2. **Evaluate Each Sub-Feature in $(Y, X)$:** Compute each individual face area or sub-volume directly on the RPN stack from the inside out and press `{{key:Σ+}}` to add it into the running $\Sigma x$ register while incrementing the face counter $n$ in Register $X$.
3. `{{key:Σx}}` — Recall the accumulated total surface area or composite volume into Register $X$ without touching general-purpose storage registers.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `2 {{keycap:x²}} 4 {{key:÷}} 1.2 {{keycap:x²}} {{key:÷}} 1 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.694444$ | Base $(1 + R^2/(4f^2))$ evaluated |
| 2 | `1.5 {{key:yˣ}} 1 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.205739$ | Bracket term $(1 + R^2/(4f^2))^{3/2} - 1$ |
| 3 | `8 {{key:ENTER}} {{keycap:π}} {{key:×}} 1.2 {{keycap:x²}} {{key:×}} 3 {{key:÷}}` | $0.0000$ | $0.0000$ | $1.205739$ | $12.063716$ | Leading factor $8\pi f^2 / 3$ |
| 4 | `{{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$14.545789$** | Parabolic reflector surface area in m² |

---

### Problem 6.23: Ellipsoid Surface Area (Knud Thomsen Approximation)
**Astronomy Context:** Triaxial asteroid with semiaxes $a = 15.0\text{ km}, b = 10.0\text{ km}, c = 6.0\text{ km}$:
$$p \approx 1.6075 \implies A \approx 4\pi \left(\frac{(ab)^p + (ac)^p + (bc)^p}{3}\right)^{1/p}$$
* $ab = 150 \implies 150^{1.6075} \approx 3,178.6$
* $ac = 90 \implies 90^{1.6075} \approx 1,399.7$
* $bc = 60 \implies 60^{1.6075} \approx 729.8$
Sum $= 5,308.1 / 3 = 1,769.37 \implies (1769.37)^{1/1.6075} \approx 103.52$
$A \approx 4\pi \times 103.52 \approx \mathbf{1,300.9\text{ km}^2}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `{{key:CLΣ}}` — Zero the statistical accumulators ($n = 0, \Sigma x = 0$) before summing composite geometric faces.
2. **Evaluate Each Sub-Feature in $(Y, X)$:** Compute each individual face area or sub-volume directly on the RPN stack from the inside out and press `{{key:Σ+}}` to add it into the running $\Sigma x$ register while incrementing the face counter $n$ in Register $X$.
3. `{{key:Σx}}` — Recall the accumulated total surface area or composite volume into Register $X$ without touching general-purpose storage registers.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `150 {{key:ENTER}} 1.6075 {{key:yˣ}}` | $0.0000$ | $0.0000$ | $150.0000$ | $3178.6008$ | $(ab)^p = 150^{1.6075}$ |
| 2 | `90 {{key:ENTER}} 1.6075 {{key:yˣ}} {{key:+}}` | $0.0000$ | $0.0000$ | $90.0000$ | $4578.3371$ | Add $(ac)^p = 90^{1.6075}$ |
| 3 | `60 {{key:ENTER}} 1.6075 {{key:yˣ}} {{key:+}} 3 {{key:÷}}` | $0.0000$ | $0.0000$ | $60.0000$ | $1769.3683$ | Add $(bc)^p$ and divide by 3 |
| 4 | `1 1.6075 {{key:÷}} {{key:yˣ}} 4 {{key:×}} {{keycap:π}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1300.9168$** | Raise to $1/p$ and scale by $4\pi$ (km²) |

---

### Problem 6.24: Hexagonal Bolt Head Volume and Mass
**Mechanical Hardware Context:** Steel hex bolt head ($s = 10.0\text{ mm}$ side length of regular hexagon, height $h = 12.0\text{ mm}$, steel density $\rho = 7.85\text{ g/cm}^3$):
$$A_{\text{hex}} = \frac{3\sqrt{3}}{2} s^2 = \frac{3\sqrt{3}}{2} (100) \approx 259.8076\text{ mm}^2$$
$$V = A_{\text{hex}} \times h = 259.8076 \times 12 = 3,117.69\text{ mm}^3 = 3.11769\text{ cm}^3$$
$$\text{Mass } m = 3.11769 \times 7.85 = \mathbf{24.4739\text{ grams}}$$

> **Named RPN Stack Idiom: *The Inside-Out Radical & Regular Polygon Pipeline*** — Square hex bolt face flat-to-flat span, multiply by polygonal area factor $3\sqrt{3}/2$, and scale by thickness without scratchpad storage {{cite:macaulay2016,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `3` `{{key:√x}}` `3` `{{key:×}}` `2` `{{key:÷}}` — Evaluate regular hexagonal area coefficient ($3\sqrt{3}/2 \approx 2.598076$).
2. `10` `{{key:x²}}` `{{key:×}}` — Square hex edge $s = 10.0\text{ mm}$ and multiply, establishing face area $A \approx 259.81\text{ mm}^2$.
3. `6.5` `{{key:×}}` — Multiply by bolt head height $h = 6.5\text{ mm}$ to find volume $V \approx 1688.75\text{ mm}^3$.
4. `7.85` `{{key:×}}` `1000` `{{key:÷}}` — Scale by steel density ($7.85\text{ g/cm}^3$) to obtain fastener head mass $m \approx \mathbf{13.26\text{ g}}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `3 {{key:√x}} 3 {{key:×}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.598076$ | Regular hex area factor $3\sqrt{3}/2$ |
| 2 | `10 {{keycap:x²}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $259.807621$ | Bolt head face area $A$ in mm² |
| 3 | `12 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3117.691454$ | Volume $V = A \cdot h$ in mm³ |
| 4 | `1000 {{key:÷}} 7.85 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$24.473878$** | Mass in grams ($\rho = 7.85\text{ g/cm}^3$) |

---

### Problem 6.25: Hydraulic Mean Depth & Wetted Perimeter
**Civil Hydraulics Context:** Trapezoidal irrigation canal: bottom width $b = 4.0\text{ m}$, water depth $y = 1.8\text{ m}$, side slope $z = 1.5$ ($1.5\text{ H} : 1\text{ V}$):
* Flow area $A = (b + z y) y = (4.0 + 1.5 \times 1.8) \times 1.8 = (4.0 + 2.7) \times 1.8 = 6.7 \times 1.8 = \mathbf{12.06\text{ m}^2}$
* Wetted perimeter $P = b + 2 y \sqrt{1 + z^2} = 4.0 + 2(1.8)\sqrt{1 + 2.25} = 4.0 + 3.6\sqrt{3.25} \approx 4.0 + 6.49 = \mathbf{10.4892\text{ m}}$
* Hydraulic radius $R_h = A / P = 12.06 / 10.4892 = \mathbf{1.1498\text{ meters}}$

> **Named RPN Stack Idiom: *The x⇄y Denominator Flip & Wetted Perimeter Pipeline*** — Compute open channel flow cross-sectional area, compute wetted boundary perimeter, and divide via stack swap with zero register allocation {{cite:hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `4.5` `{{key:ENTER}}` `1.8` `{{key:×}}` — Compute canal flow area $A = 4.5 \times 1.8 = 8.10\text{ m}^2$.
2. `4.5` `{{key:ENTER}}` `1.8` `{{key:ENTER}}` `2` `{{key:×}}` `{{key:+}}` — Form wetted perimeter $P = 4.5 + 2(1.8) = 8.10\text{ m}$.
3. `{{key:x⇄y}}` `{{key:÷}}` — Swap and divide flow area by wetted perimeter, establishing hydraulic radius $R_h = \mathbf{1.000\text{ m}}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `4 {{key:ENTER}} 1.5 {{key:ENTER}} 1.8 {{key:×}} {{key:+}} 1.8 {{key:×}}` | $0.0000$ | $4.0000$ | $6.7000$ | $12.060000$ | Flow area $A = (b + zy)y$ in m² |
| 2 | `4 {{key:ENTER}} 2 {{key:ENTER}} 1.8 {{key:×}} 1 {{key:ENTER}} 1.5 {{keycap:x²}} {{key:+}} {{key:√x}} {{key:×}} {{key:+}}` | $0.0000$ | $12.060000$ | $4.0000$ | $10.489240$ | Wetted perimeter $P = b + 2y\sqrt{1+z^2}$ in m |
| 3 | `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1.149750$** | Hydraulic radius $R_h = A / P$ in meters |

---

### Problem 6.26: Circular Segment Area (Partially Filled Pipe)
**Fluid Mechanics Context:** Storm sewer diameter $D = 1.20\text{ m}$ ($r = 0.60\text{ m}$). Water depth $d = 0.40\text{ m}$. Subtended angle:
$$\theta = 2 \arccos\left(\frac{r - d}{r}\right) = 2 \arccos\left(\frac{0.2}{0.6}\right) = 2 \arccos(0.333333) = 2(70.5288^\circ) = 141.0575^\circ = 2.461914\text{ rad}$$
$$\text{Area } A = \frac{1}{2} r^2 (\theta - \sin\theta) = 0.5(0.36)(2.461914 - \sin(141.0575^\circ)) = 0.18(2.461914 - 0.628539) = 0.18(1.833375) = \mathbf{0.330008\text{ m}^2}$$

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `120` `{{key:ENTER}}` `{{key:π}}` `{{key:×}}` `180` `{{key:÷}}` — Convert central angle $120.0^\circ$ into radians ($\theta \approx 2.094395\text{ rad}$).
2. `120` `{{key:SIN}}` `{{key:-}}` — Subtract $\sin(120^\circ) \approx 0.866025$ to obtain chord differential factor $1.228370$.
3. `0.75` `{{key:x²}}` `{{key:×}}` `2` `{{key:÷}}` — Multiply by $R^2/2$ with $R = 0.75\text{ m}$, yielding partially filled flow area $A \approx \mathbf{0.3455\text{ m}^2}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0.6 {{key:ENTER}} 0.4 {{key:-}} 0.6 {{key:÷}} {{key:ACOS}} 2 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $141.057559$ | Subtended angle $\theta$ in degrees |
| 2 | `{{key:ENTER}} {{keycap:π}} {{key:×}} 180 {{key:÷}}` | $0.0000$ | $0.0000$ | $141.057559$ | $2.461914$ | Converted angle $\theta_{\text{rad}}$ in radians |
| 3 | `{{key:x⇄y}} {{key:SIN}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.833375$ | Chord term $(\theta_{\text{rad}} - \sin\theta)$ |
| 4 | `0.6 {{keycap:x²}} {{key:×}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.330008$** | Flow cross-sectional area $A$ in m² |

---

### Problem 6.27: Slosh Baffle Circular Perforation Net Area
**Aerospace Fuel Tank Context:** Circular baffle plate $R = 400.0\text{ mm}$ perforated with 48 circular holes of diameter $d = 35.0\text{ mm}$ ($r_h = 17.5\text{ mm}$):
* Solid plate area: $\pi(400^2) = 160,000\pi \approx 502,654.82\text{ mm}^2$
* Perforations total: $48 \times \pi(17.5^2) = 48 \times 306.25\pi = 14,700\pi \approx 46,181.41\text{ mm}^2$
* Net remaining solid area: $(160,000 - 14,700)\pi = 145,300\pi \approx \mathbf{456,473.41\text{ mm}^2}$

> **Named RPN Stack Idiom: *The Σ+ Multi-Face Surface Area Accumulator & Perforation Subtraction*** — Compute tank bulkhead gross area, stream orifice hole areas, and subtract net open area in place {{cite:hp15c1982,munroe2014}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `1.2` `{{key:x²}}` `{{key:π}}` `{{key:×}}` — Calculate gross plate area $A_{\text{gross}} = \pi R^2 \approx 4.5239\text{ m}^2$.
2. `0.04` `{{key:x²}}` `{{key:π}}` `{{key:×}}` — Form area of single perforation $a = \pi r^2 \approx 5.0265 \times 10^{-3}\text{ m}^2$.
3. `120` `{{key:×}}` — Multiply by hole count ($N = 120$), establishing total relief area $A_{\text{holes}} \approx 0.6032\text{ m}^2$.
4. `{{key:-}}` — Subtract perforations from gross area, yielding net structural baffle area $A_{\text{net}} \approx \mathbf{3.9207\text{ m}^2}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `400 {{keycap:x²}} {{keycap:π}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $502654.8246$ | Gross solid circular area $\pi R^2$ in mm² |
| 2 | `17.5 {{keycap:x²}} {{keycap:π}} {{key:×}} 48 {{key:×}}` | $0.0000$ | $0.0000$ | $502654.8246$ | $46181.4120$ | Total perforation area ($48 \times \pi r_h^2$) |
| 3 | `{{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$456473.4126$** | Net solid baffle area $A_{\text{net}}$ in mm² |

---

### Problem 6.28: Conical Spiral (Helix) Arc Length
**Spring Design Context:** Tapered conical coil spring with base radius $R_1 = 30\text{ mm}$, top radius $R_2 = 10\text{ mm}$, height $h = 60\text{ mm}$, $N = 6\text{ active coils}$:
Mean radius $R_m = (30 + 10)/2 = 20\text{ mm}$. Developed coil length:
$$L \approx \sqrt{(2\pi N R_m)^2 + h^2 + (R_1 - R_2)^2} = \sqrt{(2\pi \times 6 \times 20)^2 + 60^2 + 20^2} = \sqrt{753.98^2 + 3600 + 400} \approx \mathbf{756.63\text{ mm}}$$

> **Named RPN Stack Idiom: *The Inside-Out Radical & Spiral Differential Pipeline*** — Integrate differential spiral metric components $(1 + (dr/dt)^2 + r^2(d\theta/dt)^2)$ inside-out without scratch registers {{cite:strogatz2019,hp15c1982}}.

**Keystrokes:** `2 {{key:ENTER}} {{key:π}} {{key:×}} 6 {{key:×}} 20 {{key:×}} {{key:x²}} 60 {{key:x²}} {{key:+}} 30 {{key:ENTER}} 10 {{key:-}} {{key:x²}} {{key:+}} {{key:√x}}` $\rightarrow$ **`756.6302`**

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `2` `{{key:ENTER}}` `{{key:π}}` `{{key:×}}` `6` `{{key:×}}` `20` `{{key:×}}` `{{key:x²}}` — Evaluate circumferential envelope $(2\pi N R_m)^2 \approx 568,489.21\text{ mm}^2$.
2. `60` `{{key:x²}}` `{{key:+}}` — Add squared axial height $h^2 = 3600\text{ mm}^2$ to the running metric.
3. `30` `{{key:ENTER}}` `10` `{{key:-}}` `{{key:x²}}` — Square taper difference $(R_1 - R_2)^2 = 400\text{ mm}^2$.
4. `{{key:+}}` `{{key:√x}}` — Sum all orthogonal terms and extract square root, yielding total wire length $L \approx \mathbf{756.63\text{ mm}}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `2 {{key:ENTER}} {{key:π}} {{key:×}} 6 {{key:×}} 20 {{key:×}} {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $568489.2130$ | Developed circumferential metric $(2\pi N R_m)^2$ |
| 2 | `60 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $572089.2130$ | Accumulate axial rise component $h^2$ |
| 3 | `30 {{key:ENTER}} 10 {{key:-}} {{key:x²}}` | $0.0000$ | $0.0000$ | $572089.2130$ | $400.0000$ | Radial taper variance $(R_1 - R_2)^2$ |
| 4 | `{{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$756.6302$** | Total developed conical coil length in mm |

---

### Problem 6.29: Inscribed and Circumscribed Spheres of Regular Octahedron
**Solid Mensuration Context:** Octahedron with edge length $a = 40.0\text{ mm}$:
* Circumscribed radius: $R = \frac{a}{\sqrt{2}} = \frac{40}{\sqrt{2}} \approx \mathbf{28.2843\text{ mm}}$
* Inscribed radius: $r = \frac{a}{\sqrt{6}} = \frac{40}{\sqrt{6}} \approx \mathbf{16.3299\text{ mm}}$
Ratio $R/r = \sqrt{3} \approx 1.732051$.

> **Named RPN Stack Idiom: *The Inside-Out Radical & Regular Octahedron Spheres*** — Evaluate polyhedral radical factors $a/\sqrt{2}$ and $a/\sqrt{6}$ from the inner root outward, and resolve sphere ratio $R/r = \sqrt{3}$ directly on the operational stack {{cite:hp15c1982,singh1997}}.

**Keystrokes:** `40 {{key:ENTER}} 2 {{key:√x}} {{key:÷}} 40 {{key:ENTER}} 6 {{key:√x}} {{key:÷}} {{key:÷}}` $\rightarrow$ **`1.7321`**

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `40` `{{key:ENTER}}` `2` `{{key:√x}}` `{{key:÷}}` — Compute circumscribed sphere radius ($R = a/\sqrt{2} \approx 28.2843\text{ mm}$).
2. `40` `{{key:ENTER}}` `6` `{{key:√x}}` `{{key:÷}}` — Compute inscribed sphere radius ($r = a/\sqrt{6} \approx 16.3299\text{ mm}$).
3. `{{key:÷}}` — Divide radii to yield exact geometric ratio ($R/r = \sqrt{3} \approx \mathbf{1.7321}$).
4. `{{key:x²}}` — Square the ratio to confirm the invariant $(R/r)^2 = 3.0000$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `40 {{key:ENTER}} 2 {{key:√x}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $28.2843$ | Circumradius $R = a/\sqrt{2}$ in mm |
| 2 | `40 {{key:ENTER}} 6 {{key:√x}} {{key:÷}}` | $0.0000$ | $0.0000$ | $28.2843$ | $16.3299$ | Inradius $r = a/\sqrt{6}$ in mm |
| 3 | `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1.7321$** | Polyhedral sphere ratio $R/r = \sqrt{3}$ |
| 4 | `{{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$3.0000$** | Invariant $(R/r)^2 = 3$ confirmed |

---

### Problem 6.30: Moment of Inertia of Hollow Spherical Pressure Hull
**Submersible Engineering Context:** Titanium bathysphere with outer radius $R_2 = 1.10\text{ m}$, inner radius $R_1 = 0.98\text{ m}$, material density $\rho = 4,500\text{ kg/m}^3$:
$$V = \frac{4}{3}\pi (R_2^3 - R_1^3) = \frac{4}{3}\pi(1.331 - 0.941192) = \frac{4}{3}\pi(0.389808) \approx 1.63283\text{ m}^3$$
$$\text{Mass } M = 1.63283 \times 4500 \approx 7,347.74\text{ kg}$$
$$I = \frac{2}{5} M \frac{R_2^5 - R_1^5}{R_2^3 - R_1^3} = \frac{2}{5}(7347.74) \frac{1.61051 - 0.90392}{0.389808} = 2939.10 \times \frac{0.70659}{0.389808} \approx \mathbf{5,327.42\text{ kg}\cdot\text{m}^2}$$

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `1.2` `{{key:ENTER}}` `5` `{{key:yˣ}}` — Compute outer radius fifth power ($R^5 = 1.2^5 = 2.48832$).
2. `1.15` `{{key:ENTER}}` `5` `{{key:yˣ}}` `{{key:-}}` — Subtract inner radius fifth power ($r^5 \approx 2.01136$) to obtain difference $0.47696$.
3. `1.2` `{{key:ENTER}}` `3` `{{key:yˣ}}` — Form outer radius third power ($R^3 = 1.72800$).
4. `1.15` `{{key:ENTER}}` `3` `{{key:yˣ}}` `{{key:-}}` — Subtract inner radius third power ($r^3 \approx 1.52088$) to obtain difference $0.20712$.
5. `{{key:÷}}` — Divide fifth-power difference by third-power difference, yielding mean radius squared $\approx 2.30282\text{ m}^2$.
6. `2` `{{key:ENTER}}` `5` `{{key:÷}}` `450` `{{key:×}}` `{{key:×}}` — Scale by $(2/5)M$ with $M = 450\text{ kg}$, giving mass moment of inertia $I \approx \mathbf{414.51\text{ kg}\cdot\text{m}^2}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1.1 {{key:ENTER}} 5 {{key:yˣ}} 0.98 {{key:ENTER}} 5 {{key:yˣ}} {{key:-}}` | $0.0000$ | $1.1000$ | $1.610510$ | $0.706590$ | Fifth-power difference $(R_2^5 - R_1^5)$ |
| 2 | `1.1 {{key:ENTER}} 3 {{key:yˣ}} 0.98 {{key:ENTER}} 3 {{key:yˣ}} {{key:-}}` | $0.0000$ | $0.706590$ | $1.331000$ | $0.389808$ | Third-power difference $(R_2^3 - R_1^3)$ |
| 3 | `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.812662$ | Ratio $(R_2^5 - R_1^5)/(R_2^3 - R_1^3)$ |
| 4 | `7347.74 {{key:×}} 2 {{key:×}} 5 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$5327.4219$** | Mass moment of inertia $I$ in $\text{kg}\cdot\text{m}^2$ |

---

### Problem 6.31: Volume of Intersection of Two Cylinders (Steinmetz Solid)
**Mathematics Context:** Two perpendicular intersecting cylinders of equal radius $r = 15.0\text{ mm}$:
$$V = \frac{16}{3} r^3 = \frac{16}{3} (3375) = 16 \times 1125 = \mathbf{18,000.0\text{ mm}^3}$$
Surface area: $A = 16 r^2 = 16(225) = \mathbf{3,600.0\text{ mm}^2}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `16` `{{key:ENTER}}` `3` `{{key:÷}}` — Enter Steinmetz geometric constant ($16/3 \approx 5.333333$).
2. `0.25` `{{key:ENTER}}` `3` `{{key:yˣ}}` — Cube cylinder radius ($r = 0.25\text{ m}$), giving $r^3 = 0.015625\text{ m}^3$.
3. `{{key:×}}` — Multiply to establish intersection volume $V \approx \mathbf{0.083333\text{ m}^3}$ ($83.33\text{ L}$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `16 {{key:ENTER}} 3 {{key:÷}}` | $0.0000$ | $0.0000$ | $16.0000$ | $5.333333$ | Factor $16/3$ evaluated |
| 2 | `15 {{key:ENTER}} 3 {{key:yˣ}} {{key:×}}` | $0.0000$ | $0.0000$ | $5.333333$ | **$18000.0000$** | Steinmetz volume $V = \frac{16}{3}r^3$ in mm³ |
| 3 | `15 {{keycap:x²}} 16 {{key:×}}` | $0.0000$ | $0.0000$ | $18000.0000$ | **$3600.0000$** | Surface area $A = 16 r^2$ in mm² |

---

### Problem 6.32: Prolate Spheroid Volume and Eccentricity
**Aerodynamics Context:** Streamlined airship envelope with semimajor axis $a = 60.0\text{ m}$, equatorial radius $b = 15.0\text{ m}$:
$$V = \frac{4}{3} \pi a b^2 = \frac{4}{3} \pi (60)(15^2) = 80 \pi (225) = 18,000\pi \approx \mathbf{56,548.67\text{ m}^3}$$
$$e = \sqrt{1 - \frac{b^2}{a^2}} = \sqrt{1 - \frac{225}{3600}} = \sqrt{1 - 0.0625} = \sqrt{0.9375} \approx \mathbf{0.968246}$$

> **Named RPN Stack Idiom: *The Inside-Out Radical & Spheroidal Metric Pipeline*** — Compute semi-axis ratio squared $b^2/a^2$, subtract from unity, and extract square root in place to find orbital/geometric eccentricity {{cite:hp15c1982}}.

**Keystrokes:** `4 {{key:ENTER}} 3 {{key:÷}} {{key:π}} {{key:×}} 60 {{key:×}} 15 {{key:x²}} {{key:×}}` $\rightarrow$ **`56548.6678`**; `15 {{key:x²}} 60 {{key:x²}} {{key:÷}} 1 {{key:x⇄y}} {{key:-}} {{key:√x}}` $\rightarrow$ **`0.9682`**

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `4` `{{key:ENTER}}` `3` `{{key:÷}}` `{{key:π}}` `{{key:×}}` — Form geometric sphere-volume constant ($4\pi/3 \approx 4.188790$).
2. `60` `{{key:×}}` `15` `{{key:x²}}` `{{key:×}}` — Multiply by semimajor axis ($a = 60.0\text{ m}$) and $b^2 = 225.0\text{ m}^2$, giving volume ($V \approx \mathbf{56,548.67\text{ m}^3}$).
3. `15` `{{key:x²}}` `60` `{{key:x²}}` `{{key:÷}}` — Form squared axis ratio ($b^2/a^2 = 225/3600 = 0.0625$).
4. `1` `{{key:x⇄y}}` `{{key:-}}` `{{key:√x}}` — Subtract from unity and extract square root to determine prolate eccentricity ($e \approx \mathbf{0.9682}$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `4 {{key:ENTER}} 3 {{key:÷}} {{key:π}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $4.1888$ | Factor $4\pi/3$ in Register $X$ |
| 2 | `60 {{key:×}} 15 {{key:x²}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$56548.6678$** | Prolate volume $V$ in m³ |
| 3 | `15 {{key:x²}} 60 {{key:x²}} {{key:÷}}` | $0.0000$ | $0.0000$ | $56548.6678$ | $0.0625$ | Axis squared ratio $b^2/a^2$ |
| 4 | `1 {{key:x⇄y}} {{key:-}} {{key:√x}}` | $0.0000$ | $0.0000$ | $56548.6678$ | **$0.9682$** | Prolate eccentricity $e = \sqrt{1 - b^2/a^2}$ |

---

### Problem 6.33: Oblate Spheroid Planet Planetary Flattening
**Geophysics Context:** Earth reference ellipsoid: equatorial radius $a = 6,378.137\text{ km}$, polar radius $b = 6,356.752\text{ km}$:
$$\text{Flattening } f = \frac{a - b}{a} = \frac{6378.137 - 6356.752}{6378.137} = \frac{21.385}{6378.137} \approx \mathbf{\frac{1}{298.2572}}$$
Keystrokes: `{{res:sc32_06_geometry_surface_area_seq_19:keys}}`$\implies$ **$298.2572$**.

> **Named RPN Stack Idiom: *The x⇄y Denominator Flip & Planetary Geodesy*** — Compute equatorial minus polar radius difference, enter equatorial radius, and divide via stack swap {{cite:gauss1809,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `6378.137` `{{key:ENTER}}` — Enter equatorial radius ($a = 6378.137\text{ km}$).
2. `6356.752` `{{key:-}}` — Subtract polar radius ($b = 6356.752\text{ km}$) to obtain difference ($a - b = 21.385\text{ km}$).
3. `6378.137` `{{key:x⇄y}}` `{{key:÷}}` — Exchange registers and divide by $a$ to yield flattening factor ($f \approx \mathbf{1/298.257}$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `6378.137 {{key:ENTER}} 6356.752 {{key:-}}` | $0.0000$ | $0.0000$ | $6378.1370$ | $21.3850$ | Equatorial minus polar delta $(a - b)$ in km |
| 2 | `6378.137 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.003353$ | Flattening factor $f = (a - b)/a$ |
| 3 | `{{key:1/x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$298.2572$** | Reciprocal flattening index $1/f$ |

---

### Problem 6.34: Frustum of Pyramidal Roofing Pavilion Surface Area via `{{key:Σ+}}`
**Architecture Context:** Pavilion roof with square bottom $12\text{ m}$, square top $4\text{ m}$, slant height $s = 6.5\text{ m}$.
Each trapezoidal face: $A_{\text{face}} = \frac{1}{2} (12 + 4) \times 6.5 = 8 \times 6.5 = 52.0\text{ m}^2$.
4 lateral faces: $4 \times 52.0 = \mathbf{208.0\text{ m}^2}$.
Accumulated via `{{key:Σ+}}` $\implies$ **$208.0\text{ m}^2$**.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `{{key:CLΣ}}` — Zero the statistical accumulators ($n = 0, \Sigma x = 0$) before summing composite geometric faces.
2. **Evaluate Each Sub-Feature in $(Y, X)$:** Compute each individual face area or sub-volume directly on the RPN stack from the inside out and press `{{key:Σ+}}` to add it into the running $\Sigma x$ register while incrementing the face counter $n$ in Register $X$.
3. `{{key:Σx}}` — Recall the accumulated total surface area or composite volume into Register $X$ without touching general-purpose storage registers.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:CLΣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Clear statistical accumulators |
| 2 | `12 {{key:ENTER}} 4 {{key:+}} 6.5 {{key:×}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $12.0000$ | $52.0000$ | Single trapezoidal face area $A_{\text{face}}$ in m² |
| 3 | `4 {{key:×}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | 4 lateral roof faces ($208.0\text{ m}^2$) accumulated ($n=1$) |
| 4 | `{{key:SUMS}}` | $0.0000$ | $0.0000$ | $1.0000$ | **$208.0000$** | Recall total pavilion roof surface area $\Sigma x$ |

---

### Problem 6.35: Tangent Circles Incircle of Right Triangle
**Geometry Context:** Right triangle with legs $a = 15.0\text{ cm}, b = 20.0\text{ cm}$. Hypotenuse $c = \sqrt{15^2 + 20^2} = 25.0\text{ cm}$.
Inradius:
$$r = \frac{a + b - c}{2} = \frac{15 + 20 - 25}{2} = \frac{10}{2} = \mathbf{5.0000\text{ cm}}$$
Circumradius $R = c/2 = 12.5\text{ cm}$.

> **Named RPN Stack Idiom: *The Inside-Out Radical & Incircle Geometry*** — Compute hypotenuse via inside-out Pythagorean sum, add legs, subtract hypotenuse, and divide by 2 without scratchpad memory {{cite:strogatz2019,hp15c1982}}.

**Keystrokes:** `15 {{key:x²}} 20 {{key:x²}} {{key:+}} {{key:√x}} 15 {{key:ENTER}} 20 {{key:+}} {{key:x⇄y}} {{key:-}} 2 {{key:÷}}` $\rightarrow$ **`5.0000`**

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `15` `{{key:x²}}` `20` `{{key:x²}}` `{{key:+}}` `{{key:√x}}` — Compute hypotenuse ($c = \sqrt{15^2 + 20^2} = 25.0000\text{ cm}$).
2. `15` `{{key:ENTER}}` `20` `{{key:+}}` — Sum legs ($a + b = 35.0000\text{ cm}$) while holding $c$ in Register $Y$.
3. `{{key:x⇄y}}` `{{key:-}}` — Subtract hypotenuse to find perimeter difference ($a + b - c = 10.0000\text{ cm}$).
4. `2` `{{key:÷}}` — Halve the perimeter difference to resolve inradius ($r = \mathbf{5.0000\text{ cm}}$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `15 {{key:x²}} 20 {{key:x²}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $25.0000$ | Hypotenuse $c = \sqrt{a^2 + b^2}$ in cm |
| 2 | `15 {{key:ENTER}} 20 {{key:+}}` | $0.0000$ | $0.0000$ | $25.0000$ | $35.0000$ | Sum of orthogonal legs $a + b$ |
| 3 | `{{key:x⇄y}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | Excess tangent span $(a + b - c)$ |
| 4 | `2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$5.0000$** | Right triangle inradius $r$ in cm |

---

### Problem 6.36: Polar Moment of Inertia of Thin Cylindrical Tube
**Mechanical Driveshaft Context:** Steel drive shaft $D_o = 80.0\text{ mm}$ ($R_o = 40\text{ mm}$), $D_i = 70.0\text{ mm}$ ($R_i = 35\text{ mm}$):
$$J = \frac{\pi}{2} (R_o^4 - R_i^4) = \frac{\pi}{2} (40^4 - 35^4) = \frac{\pi}{2} (2,560,000 - 1,500,625) = \frac{\pi}{2} (1,059,375) \approx \mathbf{1,664,071.76\text{ mm}^4}$$

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `2` `{{key:ENTER}}` `{{key:π}}` `{{key:×}}` — Form circumferential multiplier ($2\pi \approx 6.283185$).
2. `0.15` `{{key:ENTER}}` `3` `{{key:yˣ}}` `{{key:×}}` — Cube mean tube radius $R = 0.15\text{ m}$ ($R^3 = 0.003375\text{ m}^3$) and multiply by $2\pi$.
3. `0.0025` `{{key:×}}` — Scale by wall thickness ($t = 0.0025\text{ m}$), yielding polar moment of inertia ($J \approx \mathbf{5.3014 \times 10^{-5}\text{ m}^4}$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `40 {{key:ENTER}} 4 {{key:yˣ}}` | $0.0000$ | $0.0000$ | $40.0000$ | $2560000.0000$ | Outer radius fourth power $R_o^4$ |
| 2 | `35 {{key:ENTER}} 4 {{key:yˣ}}` | $0.0000$ | $0.0000$ | $2560000.0000$ | $1500625.0000$ | Inner radius fourth power $R_i^4$ |
| 3 | `{{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1059375.0000$ | Difference $(R_o^4 - R_i^4)$ in mm⁴ |
| 4 | `{{keycap:π}} {{key:×}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1664071.7612$** | Polar moment of inertia $J$ in mm⁴ |

---

### Problem 6.37: Elliptic Cone Volume
**Solid Mensuration Context:** Cone with elliptical base ($a = 24.0\text{ mm}, b = 15.0\text{ mm}$) and vertical height $h = 50.0\text{ mm}$:
$$V = \frac{1}{3} \pi a b h = \frac{\pi}{3} (24)(15)(50) = \frac{\pi}{3}(18000) = 6000\pi \approx \mathbf{18,849.5559\text{ mm}^3}$$

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `{{key:π}}` `3` `{{key:÷}}` — Compute conical volume factor ($\pi/3 \approx 1.047198$).
2. `0.30` `{{key:×}}` — Multiply by base semimajor axis ($a = 0.30\text{ m}$).
3. `0.18` `{{key:×}}` — Multiply by base semiminor axis ($b = 0.18\text{ m}$).
4. `0.75` `{{key:×}}` — Scale by vertical height ($h = 0.75\text{ m}$), establishing elliptic cone volume ($V \approx \mathbf{0.042412\text{ m}^3} = 42.41\text{ L}$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `24 {{key:ENTER}} 15 {{key:×}} 50 {{key:×}}` | $0.0000$ | $0.0000$ | $24.0000$ | $18000.0000$ | Product $a \cdot b \cdot h$ evaluated |
| 2 | `{{keycap:π}} {{key:×}} 3 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$18849.555922$** | Elliptic cone volume $V$ in mm³ |

---

### Problem 6.38: Spherical Lune Area
**Geometry Context:** On sphere of radius $R = 25.0\text{ cm}$, a lune has dihedral angle $\theta = 36.0^\circ$:
$$A_{\text{lune}} = 2 R^2 \theta_{\text{rad}} = 4\pi R^2 \left(\frac{\theta^\circ}{360^\circ}\right) = 4\pi(625) \left(\frac{36}{360}\right) = 2500\pi (0.1) = 250\pi \approx \mathbf{785.3982\text{ cm}^2}$$

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `2` `{{key:ENTER}}` — Load the lune doubling factor 2 into $Y$.
2. `0.85` `{{key:x²}}` `{{key:×}}` — Square radius $R = 0.85\text{ m}$ ($0.7225\text{ m}^2$) and multiply by 2 ($1.4450\text{ m}^2$).
3. `36` `{{key:ENTER}}` `{{key:π}}` `{{key:×}}` `180` `{{key:÷}}` — Convert dihedral angle $36.0^\circ$ into radians ($\theta \approx 0.628319\text{ rad}$).
4. `{{key:×}}` — Multiply radial factor by radian angle, delivering spherical lune area ($A \approx \mathbf{0.907920\text{ m}^2}$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `25 {{keycap:x²}} 4 {{key:×}} {{keycap:π}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $7853.981634$ | Full sphere surface area $4\pi R^2$ in cm² |
| 2 | `36 {{key:ENTER}} 360 {{key:÷}}` | $0.0000$ | $0.0000$ | $7853.981634$ | $0.100000$ | Dihedral angle fraction $36^\circ / 360^\circ$ |
| 3 | `{{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$785.398163$** | Spherical lune area $A_{\text{lune}}$ in cm² |

---

### Problem 6.39: High-Speed Sprint: Nested Hexagonal Prismatic Void Volume
**Rapid Calculation Sprint:** Solid regular hexagonal bar of side $S = 20.0\text{ mm}$ with a concentric hexagonal through-hole of side $s = 8.0\text{ mm}$, length $L = 150.0\text{ mm}$.
$$\text{Net Area } A_{\text{net}} = \frac{3\sqrt{3}}{2} (S^2 - s^2) = \frac{3\sqrt{3}}{2} (400 - 64) = \frac{3\sqrt{3}}{2} (336) = 504\sqrt{3} \approx 872.9536\text{ mm}^2$$
$$V_{\text{net}} = 872.9536 \times 150 = \mathbf{130,943.04\text{ mm}^3}$$
Keystrokes: `{{res:sc32_06_geometry_surface_area_seq_20:keys}}`$\implies$ **$130,943.04\text{ mm}^3$** in 5 seconds!

> **Named RPN Stack Idiom: *The Σ+ Multi-Face Surface Area Accumulator & Hexagonal Prism Sprint*** — Accumulate top and bottom regular hexagonal end caps and 6 lateral rectangular facets directly into the stack with zero register allocation {{cite:hp32sii1991}}.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `20 {{keycap:x²}} 8 {{keycap:x²}} {{key:-}}` | $0.0000$ | $0.0000$ | $400.0000$ | $336.0000$ | Hexagonal span difference $(S^2 - s^2)$ |
| 2 | `3 {{key:√x}} {{key:×}} 3 {{key:×}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $872.953607$ | Net hexagonal cross section $A_{\text{net}}$ in mm² |
| 3 | `150 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$130943.041071$** | Prismatic void volume $V_{\text{net}} = A_{\text{net}} \cdot L$ in mm³ |

---

### Problem 6.40: High-Speed Sprint: Radical Pyramid Surface-to-Volume Ratio
**Rapid Calculation Sprint:** Regular right pyramid with square base of side $s = 12.0\text{ mm}$ and height $h = 8.0\text{ mm}$:
* Slant height: $l = \sqrt{h^2 + (s/2)^2} = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = 10.0\text{ mm}$
* Total surface area: $A = s^2 + 4\left(\frac{1}{2} s l\right) = 144 + 2(12)(10) = 144 + 240 = 384.0\text{ mm}^2$
* Pyramidal volume: $V = \frac{1}{3} s^2 h = \frac{1}{3}(144)(8) = 384.0\text{ mm}^3$
* Surface-to-volume ratio: $\frac{A}{V} = \frac{384.0}{384.0} = \mathbf{1.0000\text{ mm}^{-1}}$

> **Named RPN Stack Idiom: *The Inside-Out Radical & Pyramid Surface-to-Volume Ratio*** — Evaluate slant height $\sqrt{h^2 + (s/2)^2}$ from the inside, sum lateral triangular faces and square base, and divide by pyramidal volume $V = s^2 h / 3$ without scratchpad memory {{cite:hp15c1982}}.

**Keystrokes:** `8 {{key:x²}} 12 {{key:ENTER}} 2 {{key:÷}} {{key:x²}} {{key:+}} {{key:√x}} 2 {{key:×}} 12 {{key:×}} 12 {{key:x²}} {{key:+}} 12 {{key:x²}} 8 {{key:×}} 3 {{key:÷}} {{key:÷}}` $\rightarrow$ **`1.0000`**

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `8` `{{key:x²}}` `12` `{{key:ENTER}}` `2` `{{key:÷}}` `{{key:x²}}` `{{key:+}}` `{{key:√x}}` — Square apex height ($64$) and half-base ($36$), sum ($100$), and take root, giving slant height ($l = 10.0000\text{ mm}$).
2. `2` `{{key:×}}` `12` `{{key:×}}` — Multiply slant height by base perimeter factor $2s$, yielding lateral area ($A_{\text{lat}} = 240.0000\text{ mm}^2$).
3. `12` `{{key:x²}}` `{{key:+}}` — Add base area ($s^2 = 144\text{ mm}^2$) to establish total surface area ($A = 384.0000\text{ mm}^2$).
4. `12` `{{key:x²}}` `8` `{{key:×}}` `3` `{{key:÷}}` — Compute volume ($V = s^2 h / 3 = 384.0000\text{ mm}^3$) in $X$ while $A$ rests in $Y$.
5. `{{key:÷}}` — Divide surface area by volume to resolve ratio ($A/V = \mathbf{1.0000\text{ mm}^{-1}}$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `8 {{key:x²}} 12 {{key:ENTER}} 2 {{key:÷}} {{key:x²}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | Slant height $l = \sqrt{h^2 + (s/2)^2}$ |
| 2 | `2 {{key:×}} 12 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $240.0000$ | 4 lateral triangular faces $A_{\text{lat}}$ |
| 3 | `12 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $384.0000$ | Total pyramid surface area $A$ |
| 4 | `12 {{key:x²}} 8 {{key:×}} 3 {{key:÷}}` | $0.0000$ | $0.0000$ | $384.0000$ | $384.0000$ | Pyramid volume $V = s^2 h / 3$ |
| 5 | `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1.0000$** | Surface-to-volume ratio $A/V$ |

---

## Summary & Looking Ahead

Chapter 6 unlocked the geometric power of the RPN stack across planar figures, three-dimensional polyhedra, and spatial coordinate systems. You mastered the signature **Surface Area via Stats Mode (`{{key:Σ+}}`)** technique, piping polygonal face products directly into dedicated hardware accumulators to evaluate complex multi-faceted enclosures without scratchpad notes or parenthesis clutter. By pairing analytic formulas with tactile volume and area decomposition, spatial dimensions translated into compact, deterministic keystroke sequences.

While standard geometric solids possess closed-form algebraic solutions, engineering designs frequently encounter non-linear equilibrium equations and higher-order polynomials where exact radicals do not exist. In **Chapter 7: Characteristic Polynomials & Brent's Numerical Root Solver**, you will transition from static spatial shapes to dynamic root extraction. You will harness Horner's method for instantaneous polynomial evaluation, extract quadratic and cubic roots via `{{key:POLY}}`, and deploy Richard Brent's hybrid root-finding engine (`{{key:SOLVE}}`) to converge on solutions with $10^{-12}$ precision.

