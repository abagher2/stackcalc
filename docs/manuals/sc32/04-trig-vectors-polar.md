---
title: "Chapter 4: Trigonometry, Coordinate Systems & 2D Vectors | SC-32 Manual"
description: "Direct and inverse trigonometry, hyperbolic functions, exact axial angle clamping, polar-to-rectangular 2D vector conversions, and geodetic traverses on the StackCalc SC-32."
---

# Chapter 4: Trigonometry, Coordinate Systems & 2D Vectors

## Measuring the Earth with a Shadow: From Eratosthenes and Hipparchus to the Unit Circle Volvelle

In 240 BCE, Eratosthenes of Cyrene, chief librarian of Alexandria, used a geometric observation preserved in Cleomedes' *The Heavens* {{cite:cleomedes2004}}: at solar noon on the summer solstice in Syene (modern Aswan), vertical gnomon pillars cast no shadow, and the midday sun illuminated the water at the bottom of a deep vertical well. Yet five thousand stadia to the north, in Alexandria, a vertical gnomon cast a distinct shadow measuring one-fiftieth of a full circle ($7.2^\circ$). By applying alternate interior angles of parallel rays, Eratosthenes calculated the Earth's circumference to within a few percent of modern satellite geodesy. Two centuries later, Hipparchus of Nicaea compiled the first table of chords—the ancestor of the modern sine function—tabulating celestial positions and laying the mathematical foundation for maritime navigation and astronomical ephemerides.

Trigonometry translates circular rotations into linear orthogonal coordinates. On the StackCalc SC-32, trigonometric functions pair directly with our 3D-printed *Unit Circle Volvelle* and the four $90^\circ$ quadrant sectors of the *Planetary Geared Clock*.

{{blocks:unit_circle_volvelle|Unit Circle Volvelle Technical Resolver}}
*Figure 4.1: The physical Unit Circle Volvelle mechanical resolver provides a tactile analog computing engine, pairing angular degrees and radian arcs directly with orthogonal projections $(x, y) = (\cos\theta, \sin\theta)$ prior to calculator entry.*

When you grasp the knurled upper pointer ring of the $120\text{ mm}$ *Unit Circle Volvelle* and rotate it counterclockwise from $0^\circ$ to $30^\circ$ ($\pi/6\text{ rad}$), the rotating sight window frames the exact right-triangle projections on the lower stator ring: the horizontal cosine leg $\cos(30^\circ) = \frac{\sqrt{3}}{2} \approx 0.8660$ along the $x$-axis and the vertical sine altitude $\sin(30^\circ) = \frac{1}{2} = 0.5000$ along the $y$-axis. Dialing further through $45^\circ$ ($\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}$) and $60^\circ$ ($\frac{1}{2}, \frac{\sqrt{3}}{2}$) up to $90^\circ$ ($(0, 1)$, matching the first removable $90^\circ$ quadrant sector of the *Planetary Geared Clock*) reveals why cosine and sine are not abstract power series—they are the horizontal shadow and vertical height of a rotating pointer of radius $r = 1$. On the SC-32 keypad, the two-argument coordinate keys `{{key:▸y,x}}` (Polar $\to$ Rectangular) and `{{key:▸θ,r}}` (Rectangular $\to$ Polar) automate the Volvelle directly across Registers $Y$ and $X$.

{{blocks:unit_circle_volvelle_30deg|Unit Circle Volvelle: Dialed to 30° (π/6) Showing Right-Triangle Projections cos(30°) = √3/2 and sin(30°) = 1/2}}
*Figure 4.2: Orthographic diagram of the Unit Circle Volvelle dialed to $30^\circ$ ($\pi/6\text{ rad}$), reading off exact horizontal and vertical projections $\cos(30^\circ) = \sqrt{3}/2 \approx 0.8660$ and $\sin(30^\circ) = 1/2 = 0.5000$.*

| Angular Mode | LCD Annunciator | Full Circle Revolution | Right Angle | Primary Engineering Field |
| :--- | :---: | :---: | :---: | :--- |
| **Degrees** | `DEG` (Default) | $360^\circ$ | $90^\circ$ | Structural Civil Engineering, Geodesy, Avionics |
| **Radians** | `RAD` | $2\pi \approx 6.283185\text{ rad}$ | $\pi/2 \approx 1.570796\text{ rad}$ | Mathematical Physics, Calculus, Wave Mechanics |
| **Gradians** | `GRAD` | $400\text{ grad}$ | $100\text{ grad}$ | European Surveying, Mining Engineering |

### Angular Mode Conventions (`{{key:DEG}}`, `{{key:RAD}}`, `{{key:GRAD}}`)

Why does engineering preserve three different ways to slice a circle? Each system grew out of a distinct physical symmetry. The Babylonians divided the circle into $360^\circ$ to match the roughly $360\text{ days}$ of the solar year and because $360$ is divisible by every integer from $1$ to $10$ except $7$, making it effortless to partition structural trusses and compass bearings into whole degrees. Mathematicians and physicists prefer **radians** ($2\pi\text{ rad}$ per revolution), where an angle is defined purely as the dimensionless ratio of arc length to radius ($\theta = s / r$); only in radians does the derivative of $\sin\theta$ equal $\cos\theta$ without an awkward $\pi/180$ scale factor trailing behind every differential equation. And during the French Revolution, metric reformers introduced **gradians** (`GRAD`, or *gons*), dividing each right angle into $100\text{ grad}$ ($400\text{ grad}$ per full circle) so that $1\text{ grad}$ of latitude along a planetary meridian equaled $100\text{ kilometers}$ on the Earth's surface.

The active angular mode tells the SC-32 how to interpret inputs to `{{key:SIN}}`, `{{key:COS}}`, and `{{key:TAN}}`, and what angular units to return from inverse functions (`{{key:ASIN}}`, `{{key:ACOS}}`, `{{key:ATAN}}`) and rectangular-to-polar conversions (`{{key:▸θ,r}}`). To switch modes at any time, press `{{key:↰}}` followed by `{{key:MODES}}`, then select `{{key:DEG}}` (LFU 1), `{{key:RAD}}` (LFU 2), or `{{key:GRAD}}` (LFU 3); the top status bar immediately updates its annunciator. Throughout this chapter, we work in **Degrees mode (`{{key:DEG}}`)** unless radians are explicitly required by an angular velocity or wave-phase formula. When you need to convert an angle in Register $X$ without changing the calculator's mode, simply scale by the half-turn identity $180^\circ = \pi\text{ rad} = 200\text{ grad}$: multiply by $\pi/180$ (`{{key:π}} {{key:×}} 180 {{key:÷}}`) to convert degrees to radians, by $180/\pi$ (`180 {{key:×}} {{key:π}} {{key:÷}}`) to convert radians to degrees, or by $400/360$ (`400 {{key:×}} 360 {{key:÷}}`) to convert degrees to gradians.

---

{{blocks:sc32_rpn_calculation|StackCalc SC-32 Live 4-Level XYZT Stack Hardware Display}}

## Direct & Inverse Trigonometric Functions

Every trigonometric key on the SC-32 is a unary operator: it consumes the angle or ratio sitting in Register $X$ and replaces it in place with the transformed value, leaving Registers $Y, Z,$ and $T$ untouched while preserving your original input in `LASTX`.

| Function | Dedicated Keystroke | Arity | Valid Domain | Output Range (in `{{key:DEG}}`) |
| :--- | :--- | :---: | :---: | :---: |
| **Sine** | `{{key:SIN}}` | Unary | $(-\infty, +\infty)$ | $[-1.0, +1.0]$ |
| **Cosine** | `{{key:COS}}` | Unary | $(-\infty, +\infty)$ | $[-1.0, +1.0]$ |
| **Tangent** | `{{key:TAN}}` | Unary | $\theta \ne 90^\circ + k \cdot 180^\circ$ | $(-\infty, +\infty)$ |
| **Arcsine** | `{{key:ASIN}}` | Unary | $[-1.0, +1.0]$ | $[-90^\circ, +90^\circ]$ |
| **Arccosine** | `{{key:ACOS}}` | Unary | $[-1.0, +1.0]$ | $[0^\circ, 180^\circ]$ |
| **Arctangent** | `{{key:ATAN}}` | Unary | $(-\infty, +\infty)$ | $(-90^\circ, +90^\circ)$ |

### Exact Axial Angle Clamping

Try evaluating $\cos(90^\circ)$ on a standard computer spreadsheet or a conventional floating-point calculator, and you will often get a tiny ghost number like $6.123233995736766 \times 10^{-17}$ instead of zero. Why? Because converting $90^\circ$ into radians requires multiplying by $\pi / 2$, and since $\pi$ is transcendental, its binary floating-point representation must be truncated after 53 bits. When the cosine power series evaluates that slightly imperfect binary approximation of $\pi/2$, it lands just shy of the zero crossing. In a structural truss matrix or an orbital coordinate rotation, a false non-zero residual of $6.12 \times 10^{-17}$ can silently corrupt subsequent divisions or prevent zero-detection guards from firing.

To prevent binary radian conversion from polluting orthogonal geometry, the SC-32 firmware performs **Exact Axial Angle Clamping** before evaluating circular series: in Degrees or Gradians mode, quadrantal angles are reduced modulo a full turn so that $\sin(0^\circ) = 0.0$, $\cos(0^\circ) = 1.0$, $\sin(90^\circ) = 1.0$, $\cos(90^\circ) = 0.0$, $\sin(180^\circ) = 0.0$, $\cos(180^\circ) = -1.0$, $\sin(270^\circ) = -1.0$, and $\cos(270^\circ) = 0.0$ return exact IEEE zero and unity values. Likewise, evaluating $\tan(90^\circ)$ or $\tan(270^\circ)$ immediately triggers `Error 02: DIVIDE BY 0` rather than returning a bogus $1.63 \times 10^{16}$ reciprocal of rounding noise.

---

## Hyperbolic Functions (`{{key:HYP}}`)

Whereas the circular functions $\cos\theta$ and $\sin\theta$ parameterize the unit circle $x^2 + y^2 = 1$, the **hyperbolic functions** $\cosh x$ and $\sinh x$ parameterize the unit hyperbola $x^2 - y^2 = 1$ using symmetric and antisymmetric combinations of Euler's natural exponential $e^x$ and $e^{-x}$. Because they are pure exponential functions of a dimensionless real number rather than geometric angles, hyperbolic operations ignore the `DEG`/`RAD`/`GRAD` annunciator altogether. On the SC-32, pressing the `{{key:HYP}}` prefix key followed by `{{key:SIN}}`, `{{key:COS}}`, or `{{key:TAN}}` (or `{{key:↰}}` then `{{key:HYP}}` for the inverse hyperbolic functions) evaluates these curves directly in Register $X$:

| Function | Key Sequence | Mathematical Definition | Valid Domain |
| :--- | :--- | :--- | :--- |
| **Hyperbolic Sine** | `{{key:HYP}} {{key:SIN}}` | $\sinh(x) = \frac{e^x - e^{-x}}{2}$ | $(-\infty, +\infty)$ |
| **Hyperbolic Cosine** | `{{key:HYP}} {{key:COS}}` | $\cosh(x) = \frac{e^x + e^{-x}}{2}$ | $(-\infty, +\infty)$ |
| **Hyperbolic Tangent** | `{{key:HYP}} {{key:TAN}}` | $\tanh(x) = \frac{\sinh(x)}{\cosh(x)}$ | $(-\infty, +\infty)$ |
| **Inverse Sinh** | `{{key:HYP}} {{key:ASIN}}` | $\operatorname{arsinh}(x) = \ln\left(x + \sqrt{x^2 + 1}\right)$ | $(-\infty, +\infty)$ |
| **Inverse Cosh** | `{{key:HYP}} {{key:ACOS}}` | $\operatorname{arcosh}(x) = \ln\left(x + \sqrt{x^2 - 1}\right)$ | $x \ge 1.0$ |
| **Inverse Tanh** | `{{key:HYP}} {{key:ATAN}}` | $\operatorname{artanh}(x) = \frac{1}{2}\ln\left(\frac{1+x}{1-x}\right)$ | $\lvert x\rvert < 1.0$ |

### Catenary Transmission Line Cable Sag

Galileo originally guessed that a flexible chain hanging under its own weight between two supports forms a parabola. In 1691, Jakob Bernoulli challenged the mathematicians of Europe to find the true curve, and Christiaan Huygens, Gottfried Wilhelm Leibniz, and Johann Bernoulli independently proved that a uniform cable hangs in a **catenary** (from the Latin *catena*, chain)—a hyperbolic cosine curve $y(x) = a(\cosh(x/a) - 1)$. A parabola occurs only when weight is distributed uniformly per unit *horizontal* span (as in the roadway deck of a suspension bridge); when weight is distributed uniformly along the *arc length* of the cable itself, the balance between constant horizontal tension $T_0$ and accumulating vertical gravity weight $w\cdot s$ forces the slope to grow as $\sinh(x/a)$ and the elevation to follow $\cosh(x/a)$.

Consider a high-voltage transmission cable spanning $L = 200\text{ meters}$ between two steel towers, with catenary parameter $a = T_0 / w = 800\text{ meters}$ (the ratio of horizontal tension $T_0$ to linear weight density $w$). Let us calculate the vertical sag $y$ at the half-span distance $x = 100\text{ meters}$ from the low point:
$$y = a \left(\cosh\left(\frac{x}{a}\right) - 1\right) = 800 \left(\cosh\left(\frac{100}{800}\right) - 1\right) = 800 \times (\cosh(0.125) - 1)$$

Working from the inside of the catenary argument outward, we first enter the half-span distance $x = 100\text{ m}$ (`100 {{key:ENTER}}`) and divide by the catenary parameter $a = 800\text{ m}$ (`800 {{key:÷}}`) to leave the dimensionless ratio $x/a = 0.125$ in Register $X$. Evaluating the hyperbolic cosine (`{{key:HYP}} {{key:COS}}`, giving $1.007823$), subtracting unity to isolate the dimensionless vertical rise (`1 {{key:-}}`, leaving $0.007823$), and scaling back by $a = 800\text{ m}$ (`800 {{key:×}}`) in `{{res:sc32_04_trig_vectors_polar_seq_01:keys}}` reveals a midpoint sag of **`{{res:sc32_04_trig_vectors_polar_seq_01:value}}`** meters ($6.26\text{ m}$).

---

### Relativistic Velocity Addition

Hyperbolic functions also govern the geometry of spacetime. In Einstein's Special Theory of Relativity, collinear velocities cannot simply be added ($v_1 + v_2$), or two objects moving at $0.75c$ and $0.60c$ would appear to exceed the speed of light ($1.35c$). In 1908, Hermann Minkowski showed that Lorentz boosts are actually **hyperbolic rotations** in spacetime: if we map every normalized velocity $\beta = v/c$ into a hyperbolic angle called **rapidity**, $\theta = \operatorname{atanh}(v/c)$, then rapidities add linearly! To combine two collinear velocities $v_1$ and $v_2$, you simply convert each into its rapidity via $\operatorname{atanh}$, add the two rapidities together on the stack, and take $\tanh$ of the sum to return to ordinary velocity:
$$\theta_{\text{total}} = \theta_1 + \theta_2 \implies v_{\text{total}} = c \tanh\left(\operatorname{atanh}\left(\frac{v_1}{c}\right) + \operatorname{atanh}\left(\frac{v_2}{c}\right)\right)$$

Suppose an interstellar probe travels at $v_1 = 0.75c$ relative to Earth and launches a scout missile forward at $v_2 = 0.60c$ relative to the probe. Let us find the missile's speed relative to Earth in units of $c$:

First, transform the probe's velocity $v_1 = 0.75c$ into its rapidity (`0.75 {{key:HYP}} {{key:ATAN}}`), placing $\theta_1 = 0.9730$ in Register $X$. Next, type `0.60` and convert the missile's relative velocity into rapidity (`{{key:HYP}} {{key:ATAN}}`); automatic stack lift pushes $\theta_1 = 0.9730$ into Register $Y$ while $\theta_2 = 0.6931$ forms in Register $X$. Pressing `{{key:+}}` adds the two rapidities into $\theta_{\text{total}} = 1.6661$, and `{{key:HYP}} {{key:TAN}}` in the full sequence `{{res:sc32_04_trig_vectors_polar_seq_02:keys}}` maps that total rapidity back below the speed of light—showing that the missile travels at **`{{res:sc32_04_trig_vectors_polar_seq_02:value}}`** $c$ ($93.10\%$ of $c$). Because $\tanh(\theta)$ asymptotically approaches $1.0$ as $\theta \to \infty$, no sum of finite rapidities can ever breach the cosmic speed limit.

---

## 2D Coordinate Transformations: Polar $\leftrightarrow$ Rectangular

Up to this point, every operator we have used has treated Registers $Y$ and $X$ as two separate numbers waiting to be combined into one. When you work with 2D vectors—forces on a gusset plate, aircraft velocity triangles, survey legs, or AC phasors—Registers $Y$ and $X$ take on a unified geometric meaning: **together, the $(Y, X)$ register pair forms a two-dimensional coordinate plane**.

The SC-32 provides two dedicated keys that transform the $(Y, X)$ pair in place between Cartesian rectangular coordinates $(x, y)$ and polar coordinates $(r, \theta)$ without disturbing Registers $Z$ and $T$:

| Transformation | Dedicated Keystroke | Stack Input ($Y, X$) | Stack Output ($Y, X$) | Mathematical Formula |
| :--- | :--- | :--- | :--- | :--- |
| **Polar to Rectangular** | `{{key:▸y,x}}` | $Y = \theta$ (Angle in active mode)<br>$X = r$ (Radius / Magnitude) | $Y = y = r \sin\theta$<br>$X = x = r \cos\theta$ | $(x, y) = (r\cos\theta, r\sin\theta)$ |
| **Rectangular to Polar** | `{{key:▸θ,r}}` | $Y = y$ (Orthogonal vertical)<br>$X = x$ (Orthogonal horizontal) | $Y = \theta = \operatorname{atan2}(y, x)$<br>$X = r = \sqrt{x^2 + y^2}$ | $(r, \theta) = (\sqrt{x^2+y^2}, \operatorname{atan2}(y, x))$ |

Notice the mnemonic printed right on the key labels: in `{{key:▸y,x}}`, the first letter after the arrow ($y$) lands in Register $Y$ and the second letter ($x$) lands in Register $X$; in `{{key:▸θ,r}}`, the angle $\theta$ lands in Register $Y$ and the radial magnitude $r$ lands in Register $X$. Better still, `{{key:▸θ,r}}` uses the full four-quadrant $\operatorname{atan2}(y, x)$ function rather than a naive $\arctan(y/x)$: by inspecting the individual signs of $y$ and $x$, it automatically places $(-3, -4)$ in the third quadrant ($-126.87^\circ$) instead of mistaking it for the first quadrant ($+53.13^\circ$).

{{res:sc32_phasor_mag:screenshot|Impedance phasor 3 + j4 rectangular-to-polar conversion → r = 5, theta = 53.1301 deg}}
*Figure 4.3: Direct rectangular-to-polar vector conversion on the StackCalc SC-32 places the angle $\theta = 53.1301^\circ$ in Register $Y$ and the radial magnitude $r = 5.0000$ in Register $X$.*

### Aircraft Wind Triangle & Crosswind Correction

To see how `{{key:▸y,x}}` and `{{key:▸θ,r}}` turn a tedious trigonometric problem into a clean visual workflow, picture an aircraft flying a cross-country leg through an upper-level crosswind. The pilot holds a true airspeed of $V_{\text{air}} = 220.0\text{ knots}$ on a northeast heading of $045.0^\circ$, while a crosswind of $V_{\text{wind}} = 35.0\text{ knots}$ blows *from* $310.0^\circ$ (which means the air mass itself is moving *toward* $310.0^\circ - 180^\circ = 130.0^\circ$). What ground speed $V_{\text{ground}}$ and actual ground track angle $\theta_{\text{track}}$ result from the vector sum $\vec{V}_{\text{ground}} = \vec{V}_{\text{air}} + \vec{V}_{\text{wind}}$?

Instead of writing down four separate sine and cosine products on scratch paper, we simply project both polar vectors into rectangular $(y, x)$ components on the stack, add their horizontal and vertical parts, and convert back to polar form:

#### Step 1: Resolve Airspeed Vector into Rectangular Components
Loading the heading $\theta_1 = 45^\circ$ into $Y$ and airspeed $r_1 = 220\text{ kts}$ into $X$ via `{{res:sc32_04_trig_vectors_polar_seq_03:keys}}` splits the aircraft vector into **`{{res:sc32_04_trig_vectors_polar_seq_03:value}}`** ($Y = 155.5635\text{ kts}$ for $V_{\text{air}, y}$ and $X = 155.5635\text{ kts}$ for $V_{\text{air}, x}$). We park those two components in Variables `A` and `B` via `{{key:STO}} A {{key:x⇄y}} {{key:STO}} B`.

#### Step 2: Resolve Wind Vector into Rectangular Components
With the wind blowing toward $130^\circ$ at $35\text{ kts}$, executing `{{res:sc32_04_trig_vectors_polar_seq_04:keys}}` immediately resolves the wind components ($Y = 26.8116\text{ kts}$ and $X = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_04:value}}}\text{ kts}$).

#### Step 3: Vector Summation & Polar Conversion
Now we combine the two component pairs and project back into polar coordinates:
1. Add the $x$-components: `{{key:RCL}} A {{key:+}}` $\rightarrow X = 133.0659\text{ kts}$.
2. Swap and add the $y$-components: `{{key:x⇄y}} {{key:RCL}} B {{key:+}}` $\rightarrow X = 182.3751\text{ kts}$.
3. Restore $(Y = y, X = x)$ order and convert back to polar: `{{key:x⇄y}} {{key:▸θ,r}}`, which places the resultant **Ground Speed $V_{\text{ground}} = 225.76\text{ knots}$** in Register $X$ and the **Ground Track Angle $\theta_{\text{track}} = 53.89^\circ$** in Register $Y$.

#### Rapid Calculation & Equation Entry: Instant Vector Summation via Coordinate Conversion

Whenever you face a 2D vector addition problem—whether an aircraft wind triangle, coplanar cable tensions on a crane hook, or a two-leg boundary traverse—this three-beat rhythm (`{{key:▸y,x}}` to decompose, `+` to sum, `{{key:▸θ,r}}` to recombine) saves over twenty seconds compared to manual sine/cosine entry:
1. **Decompose the First Vector ($r_1 \angle \theta_1$):** Key $\theta_1$ `{{key:ENTER}}` $r_1$ `{{key:▸y,x}}` $\to (Y = y_1, X = x_1)$, and store via `{{key:STO}} A {{key:x⇄y}} {{key:STO}} B`.
2. **Decompose the Second Vector ($r_2 \angle \theta_2$):** Key $\theta_2$ `{{key:ENTER}}` $r_2$ `{{key:▸y,x}}` $\to (Y = y_2, X = x_2)$.
3. **Sum & Recombine:** Key `{{key:RCL}} A {{key:+}} {{key:x⇄y}} {{key:RCL}} B {{key:+}} {{key:x⇄y}} {{key:▸θ,r}}` to read resultant magnitude $R$ in Register $X$ and four-quadrant angle $\theta$ in Register $Y$.

### Component-by-Component Trigonometry vs. Direct Vector Stack Conversion

The table below contrasts scalar component-by-component trigonometric entry against direct two-register polar-to-rectangular vector transformations on the SC-32 stack.

| Challenge / Engineering Task | Conventional Algebraic Calculator (Infix) | Algebraic Keystrokes & Clutter | The StackCalc Stack Advantage (RPN Stack + Visual Studio) | StackCalc Keystrokes | The Stack Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **2-Leg Vector Traverse Closure**:<br>$120\text{ m} \angle 35^\circ + 85\text{ m} \angle 110^\circ$ | Separate scalar resolution: `1 2 0 * c o s ( 3 5 ) + 8 5 * c o s ( 1 1 0 ) =`<br>and `1 2 0 * s i n ( 3 5 ) + 8 5 * s i n ( 1 1 0 ) =`<br>then $\sqrt{X^2+Y^2}$ and $\tan^{-1}(Y/X)$.<br>*Trap: Quadrant sign errors, transcription lag, and lost intermediate coordinates.* | 65 | **Coordinate Transformation Bridge**:<br>`35 {{key:ENTER}} 120 {{key:▸y,x}} {{key:STO}} A {{key:x⇄y}} {{key:STO}} B 110 {{key:ENTER}} 85 {{key:▸y,x}} {{key:RCL}} A {{key:+}} {{key:x⇄y}} {{key:RCL}} B {{key:+}} {{key:x⇄y}} {{key:▸θ,r}}`<br>Instant vector resolution and recombination on stack. | 22 | **66% fewer strokes + automatic 4-quadrant resolve ($164.03\text{ m} \angle 65.04^\circ$)** |
| **Law of Cosines Oblique Side**:<br>$c = \sqrt{a^2 + b^2 - 2ab\cos C}$<br>($a=25, b=36, C=48^\circ$) | `√( 2 5 ^ 2 + 3 6 ^ 2 - 2 * 2 5 * 3 6 * c o s ( 4 8 ) ) =`<br>*Trap: Unbalanced radical parentheses; square root evaluated early on first term if bracket omitted.* | 34 | **Stack Accumulation & Radical**:<br>`25 {{key:x²}} 36 {{key:x²}} {{key:+}} 2 {{key:ENTER}} 25 {{key:×}} 36 {{key:×}} 48 {{key:COS}} {{key:×}} {{key:-}} {{key:√x}}`<br>Evaluates sum of squares, subtracts cross product, and takes square root directly. | 24 | **29% fewer strokes + zero parenthesis nesting & visible intermediate energy states** |

---

## 3D Spherical Trigonometry: Great Circle Distance

Once a flight path or radio link spans thousands of kilometers across an ocean, flat-Earth Cartesian trigonometry breaks down. On a sphere of mean volumetric radius $R_E = 6,371.0\text{ km}$, the shortest path between two points $(\phi_1, \lambda_1)$ and $(\phi_2, \lambda_2)$ is not a straight line on a Mercator chart (a constant-compass *rhumb line*), but a **Great Circle orthodrome**—the arc formed by slicing the globe with a plane passing through both cities and the center of the Earth. By the **Spherical Law of Cosines**, the central angle $d$ subtended at the Earth's core between latitude/longitude pairs $(\phi_1, \lambda_1)$ and $(\phi_2, \lambda_2)$ is the sum of their polar projection ($\sin\phi_1\sin\phi_2$) and their equatorial projection ($\cos\phi_1\cos\phi_2\cos\Delta\lambda$):
$$\cos d = \sin\phi_1 \sin\phi_2 + \cos\phi_1 \cos\phi_2 \cos(\lambda_2 - \lambda_1), \quad D = R_E \times d_{\text{rad}}$$

Let us compute the trans-Pacific Great Circle flight distance between **San Francisco (SFO)** ($\phi_1 = 37.6189^\circ\text{ N}, \lambda_1 = -122.3750^\circ\text{ W}$) and **Tokyo Narita (NRT)** ($\phi_2 = 35.7720^\circ\text{ N}, \lambda_2 = 140.3929^\circ\text{ E}$). Across the International Date Line, their longitudinal separation is $\Delta\lambda = 360^\circ - (140.3929^\circ - (-122.3750^\circ)) = 360^\circ - 262.7679^\circ = 97.2321^\circ$.

On the SC-32 stack, the two product terms form cleanly in Registers $Y$ and $X$:
1. **Polar Sine Product ($\sin\phi_1 \sin\phi_2$):** Key `{{res:sc32_04_trig_vectors_polar_seq_54:keys}}` to leave $0.356499$ in Register $X$.
2. **Equatorial Cosine Product ($\cos\phi_1 \cos\phi_2 \cos\Delta\lambda$):** Key `{{res:sc32_04_trig_vectors_polar_seq_55:keys}}` to push $0.356499$ into Register $Y$ while forming $-0.081190$ in Register $X$.
3. **Central Angle $d$:** Press `{{key:+}} {{key:ACOS}}` to add the two projections ($\cos d = 0.275309$) and extract the central geocentric angle $d = 74.0154^\circ$.
4. **Arc Length in Kilometers:** Convert degrees to radians and scale by $R_E = 6,371\text{ km}$ via `{{key:π}} {{key:×}} 180 {{key:÷}} 6371 {{key:×}}`, yielding **$8,229.4\text{ km}$** ($5,113.5\text{ statute miles}$)—which explains why a trans-Pacific flight from San Francisco to Tokyo curves north toward the Aleutian Islands rather than flying due west across the mid-Pacific.

---

## Applied Civil Geodesy: Closed-Loop Traverse Survey

Now what if you need to add not just two vectors, but four, ten, or twenty vectors in a row—as a land surveyor does when walking the perimeter of a property boundary? Storing components in named variables `A` and `B` works well for two vectors, but the SC-32 has an even cleaner architectural link built into its firmware: **because `{{key:▸y,x}}` places $\Delta y$ in Register $Y$ and $\Delta x$ in Register $X$, its output matches the exact $(Y, X)$ input convention of the statistical accumulator key `{{key:Σ+}}`**.

In civil surveying, a closed-loop traverse is a chain of boundary courses where each leg is measured by its length $r$ and compass angle $\theta$. For the boundary to close back onto its starting monument without a gap, the sum of all horizontal departures ($\Sigma \Delta x$) and the sum of all vertical latitudes ($\Sigma \Delta y$) must both vanish:
$$\Sigma \Delta x = 0 \quad (\text{Departure Closure}), \quad \Sigma \Delta y = 0 \quad (\text{Latitude Closure})$$

Let us walk a four-station rectangular parcel—**Leg 1** ($r = 100.0\text{ m}$ at $\theta = 60.0^\circ$), **Leg 2** ($r = 80.0\text{ m}$ at $\theta = 150.0^\circ$), **Leg 3** ($r = 100.0\text{ m}$ at $\theta = 240.0^\circ$), and **Leg 4** ($r = 80.0\text{ m}$ at $\theta = 330.0^\circ$)—by clearing the statistical registers (`{{key:CLΣ}}`) and chaining `{{key:▸y,x}} {{key:Σ+}}` on each leg:

#### Leg 1: $\theta = 60^\circ, r = 100\text{ m}$
Push angle and distance (`60 {{key:ENTER}} 100` so $Y = 60.0000, X = 100.0000$). Executing `{{res:sc32_04_trig_vectors_polar_seq_05:keys}}` projects latitude $\Delta y = 86.6025\text{ m}$ into Register $Y$ and departure $\Delta x = 50.0000\text{ m}$ into Register $X$, and accumulates both components into statistical memory ($n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_05:value}}}$).

#### Leg 2: $\theta = 150^\circ, r = 80\text{ m}$
Pushing the second course (`150 {{key:ENTER}} 80`), converting to components (`{{key:▸y,x}}`, giving $\Delta y = 40.0000\text{ m}$ in $Y$ and $\Delta x = -69.2820\text{ m}$ in $X$), and accumulating via `{{res:sc32_04_trig_vectors_polar_seq_06:keys}}` increments the station counter to $n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_06:value}}}$.

#### Leg 3: $\theta = 240^\circ, r = 100\text{ m}$
Pushing the return course (`240 {{key:ENTER}} 100`), transforming (`{{key:▸y,x}}`, giving $\Delta y = -86.6025\text{ m}$ in $Y$ and $\Delta x = -50.0000\text{ m}$ in $X$), and accumulating via `{{res:sc32_04_trig_vectors_polar_seq_07:keys}}` advances the traverse to $n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_07:value}}}$.

#### Leg 4: $\theta = 330^\circ, r = 80\text{ m}$
Entering the closing leg (`330 {{key:ENTER}} 80`), projecting (`{{key:▸y,x}}`, producing $\Delta y = -40.0000\text{ m}$ in $Y$ and $\Delta x = 69.2820\text{ m}$ in $X$), and completing `{{res:sc32_04_trig_vectors_polar_seq_08:keys}}` closes the four-station loop at $n = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_08:value}}}$.

### Verifying Coordinate Closure & Precision Misclosure

With all four legs accumulated, recalling the statistical sums (`{{key:SUMS}}`) places $\Sigma x = 0.0000\text{ m}$ and $\Sigma y = 0.0000\text{ m}$ onto the stack, confirming a linear misclosure error of $\sqrt{(\Sigma x)^2 + (\Sigma y)^2} = \mathbf{0.0000\text{ m}}$ around the $360.0\text{ m}$ perimeter ($8,000.0\text{ m}^2$ or $0.80\text{ hectares}$ of enclosed area). In real field surveys where terrain tape sag or atmospheric refraction leaves a small non-zero residual $(\Sigma y, \Sigma x)$, pressing `{{key:▸θ,r}}` on those recalled sums immediately gives the exact magnitude and bearing of the survey misclosure vector.

---

## Vector Algebra & Spatial Coordinate Rotations

Stepping back from individual survey traverses, three vector patterns recur across structural statics, robotics, and aerospace guidance on the SC-32 stack:

First, **multi-vector addition** ($\sum \vec{V} = \vec{V}_1 + \vec{V}_2 + \dots$) always follows the `{{key:▸y,x}} {{key:Σ+}}` pipeline we just used: decompose each polar vector $(r, \theta)$ into Cartesian $(y, x)$ via `{{key:▸y,x}}`, press `{{key:Σ+}}` to add both components into the statistical registers, recall $(\Sigma y, \Sigma x)$ via `{{key:SUMS}}`, and press `{{key:▸θ,r}}` to read off the resultant magnitude and direction.

Second, **2D coordinate frame rotation**—evaluating the orthogonal rotation matrix
$$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$
requires four trig evaluations and two sums on an algebraic calculator, but takes just six keystrokes on the SC-32: convert $(y, x)$ to polar via `{{key:▸θ,r}}`, swap `{{key:x⇄y}}` to bring the angle into Register $X$, add the rotation angle $\Delta\theta$, swap `{{key:x⇄y}}` back, and press `{{key:▸y,x}}` to project the rotated coordinates $(y', x')$.

Third, in **3D space-frame mechanics**, the Euclidean norm $|\vec{V}| = \sqrt{V_x^2 + V_y^2 + V_z^2}$ is computed either by summing the three squares (`x² +`) and pressing `{{key:√x}}`, or by chaining `{{key:▸θ,r}}` twice (converting $(V_x, V_y)$ to planar radius $r_{xy}$ in $X$, loading $V_z$, and pressing `{{key:▸θ,r}}` again to get the 3D magnitude in $X$ and elevation angle in $Y$), from which the direction cosines follow directly as $\cos\alpha = V_x / |\vec{V}|$, $\cos\beta = V_y / |\vec{V}|$, and $\cos\gamma = V_z / |\vec{V}|$.

---

## Geodetic Coordinate Systems & WGS84 Ellipsoidal Geometry

In the *Principia* (1687), Isaac Newton reasoned that because the Earth rotates once every sidereal day, centrifugal acceleration at the equator must cause our planet to bulge outward into an **oblate spheroid**—a sphere flattened slightly at the poles. Modern satellite navigation (GPS/GNSS) codifies Newton's insight in the **World Geodetic System 1984 (WGS84)** reference ellipsoid, whose equatorial semi-major axis $a = 6,378,137.0\text{ m}$ exceeds its polar semi-minor axis $b = 6,356,752.3142\text{ m}$ by $21.385\text{ kilometers}$, corresponding to a flattening factor $f = (a - b)/a = 1 / 298.257223563 \approx 0.00335281066$ and first eccentricity squared $e^2 = 2f - f^2 = (a^2 - b^2)/a^2 \approx 0.00669437999014$.

Because an oblate ellipsoid is flatter near the poles and more curved across the equator in the north-south plane, a point at geodetic latitude $\phi$ has two distinct principal radii of curvature: the **prime vertical radius of curvature** $N(\phi)$ (measured East-West perpendicular to the meridian) and the **meridional radius of curvature** $M(\phi)$ (measured North-South along the meridian):
$$N(\phi) = \frac{a}{\sqrt{1 - e^2 \sin^2\phi}}, \qquad M(\phi) = \frac{a(1 - e^2)}{(1 - e^2 \sin^2\phi)^{3/2}}$$
Once $N(\phi)$ is evaluated on the stack for a receiver at geodetic latitude $\phi$, longitude $\lambda$, and ellipsoidal height $h$, its 3D Earth-Centered, Earth-Fixed (ECEF) Cartesian coordinates $(X, Y, Z)$ follow directly by projecting $(N(\phi) + h)\cos\phi$ onto the equatorial $(\cos\lambda, \sin\lambda)$ axes via `{{key:▸y,x}}`:
$$\begin{aligned}
X &= (N(\phi) + h) \cos\phi \cos\lambda \\
Y &= (N(\phi) + h) \cos\phi \sin\lambda \\
Z &= (N(\phi)(1 - e^2) + h) \sin\phi
\end{aligned}$$

---

## Epicyclic Planetary Gears & Avian Celestial Navigation

Mechanical gear trains and biological navigation systems both rely on continuous angular projections and spherical coordinate geometry:

### Epicyclic Planetary Gear Reduction & Circular Phasors
How do the discrete tooth ratios of a mechanical clock translate into continuous trigonometric waves $(\cos\omega t, \sin\omega t)$? Inside the 3D-printed *Planetary Geared Clock*, the minute hand and hour hand rotate around the exact same central shaft at a coupled **$12:1$ angular velocity reduction** ($\omega_{\text{hour}} = \frac{1}{12}\omega_{\text{minute}}$):
1. **Sun, Planet & Fixed Ring Gears:** When you turn the central **sun gear** (attached to the minute hand at $\omega_{\text{minute}} = 360^\circ/\text{hr}$), its involute teeth drive the orbiting **planet gears** inside a stationary outer internal **ring gear**. Because the outer ring gear is fixed to the clock frame, the planet gears must walk around the inside of the ring, carrying the **planet carrier arm** (attached to the hour hand) forward at $\omega_{\text{hour}} = 30^\circ/\text{hr}$—a single $30^\circ$ hour sector for every full $360^\circ$ sweep of the minute hand.
2. **From Gear Teeth to Orthogonal Projections:** Coupling the *Planetary Geared Clock* with the *Unit Circle Volvelle* turns angular rotation $\theta = \omega t$ into two perpendicular linear shadows: horizontal position $x(t) = r\cos(\omega t)$ in Register $X$ and vertical altitude $y(t) = r\sin(\omega t)$ in Register $Y$ via `{{key:▸y,x}}`, while `{{key:▸θ,r}}` recovers the four-quadrant phase angle $\theta = \operatorname{atan2}(y, x)$ and radius $r = \sqrt{x^2 + y^2}$ without disturbing Registers $Z$ and $T$.

### How Migratory Birds Navigate: Great-Circle Orthodromes, Crosswind Drift & Time-Compensated Sun Compasses
The three core navigation problems in this chapter—the **Aircraft Wind Triangle**, **Spherical Great-Circle Distance** (San Francisco to Tokyo), and **Solar Azimuth Ephemerides** (explored in the solar azimuth calculation below)—are solved every autumn by one of evolution's greatest navigators: the **bar-tailed godwit** (*Limosa lapponica*).
* **Great-Circle Orthodromes Across the Pacific:** Departing Alaska's tidal flats, bar-tailed godwits fly **$11,000\text{ km}$ non-stop over open ocean to New Zealand** in nine days without food, water, or landmarks—following spherical great-circle orthodromes ($\cos d = \sin\phi_1\sin\phi_2 + \cos\phi_1\cos\phi_2\cos\Delta\lambda$) where the optimal compass bearing shifts continuously with latitude.
* **Time-Compensated Solar Azimuth (`{{key:▸HMS}}` / `{{key:▸HR}}`) & Crosswind Vector Correction (`{{key:▸y,x}}` / `{{key:▸θ,r}}`):** Because the sun marches across the sky at an average angular rate of $15.0^\circ\text{ per hour}$ ($\omega = 15^\circ \times \Delta t_{\text{hr}}$), a bird steering by the sun without a clock would spiral off course by $90^\circ$ every six hours. Migratory birds combine an internal circadian clock (`{{key:▸HMS}}` $\leftrightarrow$ `{{key:▸HR}}`) with the sun's elevation and azimuth and cryptochrome retinal magnetoreception to hold true heading—while continuously crabbing into crosswinds (`{{key:▸y,x}}` vector summation) so their ground track $\vec{V}_{\text{ground}} = \vec{V}_{\text{air}} + \vec{V}_{\text{wind}}$ lands directly on their wintering estuary.

---

## Numerical Domain Guards & Boundary Verification

> **Angular Mode Verification**
> Key in `{{res:sc32_04_trig_vectors_polar_seq_56:keys}}`.
> *Expected Result:* In Degrees mode (`{{key:DEG}}`), the display reads `0.707106781187`.
> *If you see $0.850903524534$,* your calculator is in Radians mode (`{{key:RAD}}`). Press `{{key:DEG}}` to restore Degrees baseline.

> **Polar-to-Rectangular Coordinate Order**
> Key in `{{res:sc32_04_trig_vectors_polar_seq_57:keys}}`.
> *Expected Result:* $X = 0.0000$ and $Y = 10.0000$.
> *If you see $X = 10.0000$ and $Y = 0.0000$,* you loaded the radius into $Y$ and angle into $X$. Always remember the mnemonic: **Angle $\theta$ is in $Y$, Radius $r$ is in $X$**.

---

## Navigating Waves, Orbits, and 3D Force Vectors on the Stack

To see how trigonometric functions and coordinate projections behave across real engineering workflows, the sixteen scenarios below progress from ballistic parabolas and optical waveguides to 3D space-frame vectors, Mohr's strain circle, and spherical celestial navigation. Notice how every model decomposes an angled physical quantity into orthogonal components on the stack before recombining them.

### Ballistics, Surveying Baselines & Angular Kinematics

We begin in Degrees mode (`{{key:DEG}}`), resolving projectile trajectories, oblique survey triangles, optical critical angles, banked highway curves, satellite look angles, and AC power triangles.

#### Projectile Trajectory Maximum Height and Range

Galileo discovered that in the absence of air drag, projectile motion separates into two independent orthogonal components: constant horizontal velocity $v_{0x} = v_0\cos\theta$ and uniformly decelerated vertical motion $v_{0y} = v_0\sin\theta$ under gravity $g$. An artillery shell is fired with muzzle velocity $v_0 = 85.0\text{ m/s}$ at an elevation angle $\theta = 38.0^\circ$ ($g = 9.80665\text{ m/s}^2$). What are its apex altitude $H_{\max}$ (where vertical kinetic energy converts entirely into potential energy $mgh$) and its horizontal range $R$ across level ground?

$$H_{\max} = \frac{(v_0 \sin\theta)^2}{2g}, \quad R = \frac{v_0^2 \sin(2\theta)}{g}$$

For the apex height $H_{\max}$, we project the vertical muzzle velocity $v_{0y} = 85\sin(38^\circ) = 52.3312\text{ m/s}$, square it in place, and divide by $2g$ via `{{res:sc32_04_trig_vectors_polar_seq_09:keys}}` to reach **`{{res:sc32_04_trig_vectors_polar_seq_09:value}}`** $\text{m}$:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `85 {{key:ENTER}} 38 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $52.3312$ | Vertical velocity component $v_{0y}$ |
| `{{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2,738.5574$ | $v_{0y}^2$ numerator |
| `2 {{key:ENTER}} 9.80665 {{key:×}}` | $0.0000$ | $0.0000$ | $2738.5574$ | $19.6133$ | Denominator $2g$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$139.6275\text{ m}$** | Peak height $H_{\max}$ |

Evaluating the double-angle range equation with $\sin(2\theta) = \sin(76^\circ)$ via `{{res:sc32_04_trig_vectors_polar_seq_10:keys}}` yields a downrange impact distance of $R =$ **`{{res:sc32_04_trig_vectors_polar_seq_10:value}}`** $\text{m}$.

#### Oblique Triangle Solution via Law of Cosines

When a civil surveyor stands at a corner monument and measures the distances to two boundary markers across a pond—$a = 45.0\text{ m}$ and $b = 62.0\text{ m}$, separated by an included horizontal angle of $C = 48.0^\circ$—the triangle is oblique rather than right-angled. The **Law of Cosines** generalizes the Pythagorean theorem by subtracting the projection cross-term $2ab\cos C$ (which vanishes when $C = 90^\circ$):

$$c = \sqrt{a^2 + b^2 - 2 a b \cos C} = \sqrt{45^2 + 62^2 - 2(45)(62)\cos(48^\circ)}$$

On the stack, the Pythagorean sum $a^2 + b^2 = 5869$ waits in Register $Y$ while the cosine cross-term $2ab\cos C = 3733.7488$ builds in Register $X$, so executing `{{res:sc32_04_trig_vectors_polar_seq_11:keys}}` subtracts the cross-term and extracts the opposing boundary length $c =$ **`{{res:sc32_04_trig_vectors_polar_seq_11:value}}`** $\text{m}$:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `45 {{key:x²}} 62 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $5869.0000$ | Sum of squared sides $a^2 + b^2 = 2025 + 3844 = 5869$ |
| 2 | `2 {{key:ENTER}} 45 {{key:×}} 62 {{key:×}} 48 {{key:COS}} {{key:×}}` | $0.0000$ | $0.0000$ | $5869.0000$ | $3733.7488$ | Law of cosines cross-term $2 a b \cos C$ |
| 3 | `{{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2135.2512$ | Quadratic difference $(a^2 + b^2 - 2ab\cos C)$ |
| 4 | `{{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$46.2088$** | Extract square root for side $c$ (m) |

#### Critical Angle for Total Internal Reflection

How does an optical fiber trap a pulse of laser light inside a flexible glass thread across thousands of kilometers of ocean floor? By Snell's Law ($n_1\sin\theta_1 = n_2\sin\theta_2$), light traveling from a higher-index glass core ($n_1 = 1.480$) toward a lower-index cladding ($n_2 = 1.450$) bends away from the normal until, at the **critical angle** $\theta_c$, the refracted ray skims the interface at $\theta_2 = 90^\circ$ ($\sin\theta_2 = 1$). Any ray striking the wall at an angle steeper than $\theta_c$ undergoes $100\%$ lossless **Total Internal Reflection**:

$$\theta_c = \arcsin\left(\frac{n_2}{n_1}\right) = \arcsin\left(\frac{1.450}{1.480}\right)$$

Dividing the cladding index by the core index (`1.450 {{key:ENTER}} 1.480 {{key:÷}}`, placing $0.9797$ in Register $X$) and pressing `{{key:ASIN}}` in `{{res:sc32_04_trig_vectors_polar_seq_15:keys}}` yields $\theta_c = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_15:value}}^\circ}$—meaning any ray propagating within $90^\circ - \theta_c = 11.56^\circ$ of the fiber axis is permanently trapped inside the core. And because `{{key:ASIN}}` saves the index ratio $n_2/n_1 = 0.979730$ in `LASTX`, keying `{{key:LASTX}} {{key:x²}} 1 {{key:x⇄y}} {{key:-}} {{key:√x}}` immediately computes $\cos\theta_c = \sqrt{1 - (n_2/n_1)^2}$ for the fiber's numerical aperture.

#### Highway Super-Elevation Banking Angle

If a car rounds a flat curve on glare ice, it skids outward off the road because there is no lateral tire friction to supply the inward centripetal force $mv^2/R$. Civil highway engineers eliminate this hazard by **banking** (super-elevating) the roadway by an angle $\theta$ so that the inward horizontal component of the road's normal force ($N\sin\theta$) provides the exact centripetal acceleration needed while the vertical component ($N\cos\theta = mg$) supports the vehicle's weight. For a highway curve of radius $R = 350.0\text{ m}$ designed for $v = 100.0\text{ km/h}$ ($27.7778\text{ m/s}$, with $g = 9.80665\text{ m/s}^2$), what banking angle $\theta$ reduces lateral tire friction to zero?

$$\tan\theta = \frac{v^2}{g R} \implies \theta = \arctan\left(\frac{v^2}{g R}\right)$$

Converting $100\text{ km/h}$ into meters per second (`100 {{key:ENTER}} 3.6 {{key:÷}}`), squaring in place, and dividing by $gR$ in `{{res:sc32_04_trig_vectors_polar_seq_16:keys}}` yields the dimensionless lateral acceleration ratio $v^2/(gR) = 0.2248\,g$, and pressing `{{key:ATAN}}` extracts the ideal super-elevation angle $\theta = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_16:value}}^\circ}$:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `100 {{key:ENTER}} 3.6 {{key:÷}} {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $771.6049$ | Square speed in m/s $(v/3.6)^2$ |
| 2 | `9.80665 {{key:ENTER}} 350 {{key:×}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.2248$ | Divide by centripetal gravity denominator $g R$ |
| 3 | `{{key:ATAN}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$12.6698$** | Extract arctangent for banking angle $\theta$ (degrees) |

#### Ground Satellite Elevation Angle

A low-Earth-orbit imaging satellite circles at altitude $h = 850\text{ km}$ above an Earth of radius $R_E = 6,371\text{ km}$. When the satellite's ground track is displaced by a central geocentric angle $\gamma = 18.0^\circ$ from a tracking station, at what look-angle elevation $E$ above the local horizon must the station's dish antenna point? Applying oblique triangle geometry to the Earth-center, ground-station, and satellite triangle yields:

$$\tan E = \frac{\cos\gamma - \frac{R_E}{R_E + h}}{\sin\gamma}$$

After computing $\cos(18^\circ) = 0.9511$ in Step 1, we form the nadir-to-orbit radius ratio $R_E/(R_E + h) = 6371 / (6371 + 850)$ in Step 2 (note that `6371 {{key:ENTER}} {{key:ENTER}} 850 {{key:+}} {{key:÷}} {{key:-}}` can duplicate `6371` without re-typing it), divide by $\sin(18^\circ)$ in Step 3, and press `{{key:ATAN}}` in `{{res:sc32_04_trig_vectors_polar_seq_18:keys}}` to obtain the antenna horizon elevation $E = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_18:value}}^\circ}$:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `18 {{key:COS}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.9511$ | Cosine of angular distance $\cos\gamma$ |
| 2 | `6371 {{key:ENTER}} 6371 {{key:ENTER}} 850 {{key:+}} {{key:÷}} {{key:-}}` | $0.9511$ | $0.9511$ | $0.9511$ | $0.0688$ | Subtract orbital radius ratio $R_E / (R_E + h)$ |
| 3 | `18 {{key:SIN}} {{key:÷}}` | $0.9511$ | $0.9511$ | $0.9511$ | $0.2225$ | Divide by sine $\sin\gamma$ for elevation tangent |
| 4 | `{{key:ATAN}}` | $0.9511$ | $0.9511$ | $0.9511$ | **$12.5462$** | Extract ground satellite elevation angle $E$ (degrees) |

#### AC Circuit Real Power and Power Factor

When an inductive AC motor draws $I_{\text{rms}} = 8.50\text{ A}$ from a $V_{\text{rms}} = 120.0\text{ V}$ line with a lagging phase angle of $\phi = 32.0^\circ$, the total **apparent power** $S = V_{\text{rms}} I_{\text{rms}} = 1,020\text{ VA}$ splits into two orthogonal legs of a right triangle: **real power** $P = S\cos\phi$ (which performs mechanical shaft work and dissipates heat, measured in Watts) and **reactive power** $Q = S\sin\phi$ (which sloshes back and forth between the source and the motor's magnetic field each half-cycle, measured in VAR):

$$P = V_{\text{rms}} I_{\text{rms}} \cos\phi \quad [\text{Watts}], \quad Q = V_{\text{rms}} I_{\text{rms}} \sin\phi \quad [\text{VAR}]$$

Just as dialing the *Unit Circle Volvelle* to $\phi = 32^\circ$ projects the radial pointer onto its horizontal cosine and vertical sine axes, you can resolve the power triangle on the stack via `{{res:sc32_04_trig_vectors_polar_seq_19:keys}}` by duplicating $S = 1,020\text{ VA}$ (`{{key:ENTER}} {{key:ENTER}}`) and scaling by $\cos(32^\circ)$ and $\sin(32^\circ)$ to place real power $P = \mathbf{865.01\text{ W}}$ in Register $Y$ and reactive power $Q =$ **`{{res:sc32_04_trig_vectors_polar_seq_19:value}}`** $\text{VAR}$ in Register $X$, or in a single coordinate projection by keying `32 {{key:ENTER}} 1020 {{key:▸y,x}}`:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `120 {{key:ENTER}} 8.5 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1020.0000$ | Total apparent electrical power $S = V_{\text{rms}} I_{\text{rms}}$ (VA) |
| 2 | `{{key:ENTER}} {{key:ENTER}} 32 {{key:COS}} {{key:×}}` | $0.0000$ | $0.0000$ | $1020.0000$ | $865.0097$ | Multiply by power factor $\cos(32^\circ)$ for real power $P$ (W) |
| 3 | `{{key:x⇄y}} 32 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $865.0097$ | **$540.5176$** | Multiply by reactive factor $\sin(32^\circ)$ for reactive power $Q$ (VAR) |

---

### Spatial Vector Algebra, Coordinate Rotations & Phasor Addition

These next three models extend trigonometric projections to 3D space-frame gusset angles, inclined-plane friction dynamics, and two-station optical leveling to an inaccessible mountain summit.

#### 3D Vector Dot Product and Enclosed Angle

When fabricating a 3D tubular space-frame node, a machinist must mitre-cut the true spatial bevel angle $\theta$ between two non-coplanar struts $\vec{A} = (4.0, 6.0, 8.0\text{ m})$ and $\vec{B} = (2.0, -3.0, 5.0\text{ m})$. Even though the struts point skew in three dimensions, they span a unique plane whose enclosed angle $\theta$ is given by the Cauchy-Schwarz dot-product identity:

$$\vec{A} \cdot \vec{B} = A_x B_x + A_y B_y + A_z B_z = (4)(2) + (6)(-3) + (8)(5) = 8 - 18 + 40 = 30.0$$
$$|\vec{A}| = \sqrt{16+36+64} = \sqrt{116} \approx 10.7703, \quad |\vec{B}| = \sqrt{4+9+25} = \sqrt{38} \approx 6.1644$$
$$\theta = \arccos\left(\frac{\vec{A} \cdot \vec{B}}{|\vec{A}| |\vec{B}|}\right)$$

Rather than computing $|\vec{A}|\cdot|\vec{B}|$ in a separate register, dividing the scalar dot product $30.0$ sequentially by $\sqrt{116}$ and then by $\sqrt{38}$ in `{{res:sc32_04_trig_vectors_polar_seq_20:keys}}` forms $\cos\theta = 0.4519$ directly in Register $X$, and pressing `{{key:ACOS}}` extracts the true 3D intersection angle $\theta = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_20:value}}^\circ}$:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `30 {{key:ENTER}} 116 {{key:√x}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.7854$ | Normalize dot product by magnitude $\lvert\vec{A}\rvert = \sqrt{116}$ |
| 2 | `38 {{key:√x}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.4519$ | Normalize by magnitude $\lvert\vec{B}\rvert = \sqrt{38}$ for enclosed cosine |
| 3 | `{{key:ACOS}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$63.1371$** | Extract inverse cosine for 3D enclosed angle $\theta$ (degrees) |

#### Inclined Plane Acceleration with Kinetic Friction

A crate sliding down a ramp inclined at $\theta = 34.0^\circ$ with kinetic friction coefficient $\mu_k = 0.22$ ($g = 9.80665\text{ m/s}^2$) experiences a tug-of-war between the downhill tangential component of gravity ($g\sin\theta$) and the uphill Coulomb friction drag ($\mu_k g\cos\theta$, proportional to the normal force $mg\cos\theta$):

$$a = g (\sin\theta - \mu_k \cos\theta)$$

Evaluating $\sin(34^\circ) = 0.5592$, subtracting $0.22\cos(34^\circ) = 0.1824$ (where you can also use `{{key:LASTX}} {{key:COS}}` after `34 {{key:SIN}}` to avoid re-keying $34^\circ$), and multiplying by $g = 9.80665\text{ m/s}^2$ via `{{res:sc32_04_trig_vectors_polar_seq_23:keys}}` yields a net downhill acceleration of $a = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_23:value}}\text{ m/s}^2}$:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `34 {{key:SIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.5592$ | Gravitational downhill acceleration component $\sin(34^\circ)$ |
| 2 | `34 {{key:COS}} 0.22 {{key:×}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.3768$ | Subtract kinetic friction deceleration $\mu_k \cos(34^\circ)$ |
| 3 | `9.80665 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$3.6952$** | Scale by gravity $g$ for net downhill acceleration $a$ ($\text{m/s}^2$) |

#### Trigonometric Leveling to Inaccessible Mountain Peak

How did 19th-century surveyors measure the height of Mount Everest from the plains of India when they could not chain a tape to the base of the peak? By sighting vertical elevation angles $\alpha$ and $\beta$ from two collinear stations separated by a known horizontal baseline $d$: since the unknown horizontal distances from the summit plumb line are $x_1 = H\cot\alpha$ and $x_2 = H\cot\beta$, their difference is simply the baseline $d = H(\cot\alpha - \cot\beta)$. For a baseline $d = 500.0\text{ m}$ with elevation angles $\alpha = 24.5^\circ$ (Station 1) and $\beta = 31.2^\circ$ (Station 2, closer to the peak), find the summit height $H$ above the instrument horizon:

$$H = \frac{d}{\cot\alpha - \cot\beta} = \frac{d}{\frac{1}{\tan\alpha} - \frac{1}{\tan\beta}}$$

On the stack, each cotangent is simply `{{key:TAN}} {{key:1/x}}`. Subtracting $\cot(31.2^\circ)$ from $\cot(24.5^\circ)$ leaves the differential cotangent $\Delta\cot = 0.5431$ in Register $X$, and dividing it into the $500\text{ m}$ baseline via `{{res:sc32_04_trig_vectors_polar_seq_28:keys}}` reveals a summit elevation of $H = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_28:value}}\text{ meters}}$:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `24.5 {{key:TAN}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.1943$ | Invert tangent for Station 1 cotangent $\cot(24.5^\circ)$ |
| 2 | `31.2 {{key:TAN}} {{key:1/x}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.5431$ | Subtract Station 2 cotangent $\cot(31.2^\circ)$ for differential $\Delta\cot$ |
| 3 | `500 {{key:x⇄y}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$920.6349$** | Divide baseline distance $d = 500\text{ m}$ for summit height $H$ (m) |

---

### Nonlinear Oscillators, Wave Optics & Tensor Rotations

The next five analyses apply trigonometric power series, double-angle tensor rotations, and Gauss's half-angle anomaly identity to nonlinear pendulums, Mohr's strain circle, acoustic interference, and elliptical orbits.

#### Large-Amplitude Pendulum Period Correction

Introductory physics courses teach that a pendulum's period $T_0 = 2\pi\sqrt{L/g}$ is independent of amplitude—a property Galileo noticed watching a swinging cathedral lamp in Pisa. In reality, that *isochronism* holds only for tiny angles where $\sin\theta \approx \theta$. At larger release angles $\theta_0$, the true restoring torque $-mgL\sin\theta$ is weaker than the linear Hooke approximation $-mgL\theta$, causing the pendulum to linger near its turning points. Expanding the complete elliptic integral $K(\sin(\theta_0/2))$ yields Legendre's first-order period correction. For a clock pendulum with small-angle period $T_0 = 2.000\text{ s}$ released from $\theta_0 = 45.0^\circ$, find the true period $T$:

$$T \approx T_0 \left(1 + \frac{1}{4} \sin^2\left(\frac{\theta_0}{2}\right)\right) = 2.0 \left(1 + 0.25 \sin^2(22.5^\circ)\right)$$

Evaluating the half-angle sine squared (`22.5 {{key:SIN}} {{key:x²}}` $\to 0.1464$), multiplying by the elliptic coefficient $1/4$ and adding unity (`0.25 {{key:×}} 1 {{key:+}}` $\to 1.0366$), and scaling by $T_0 = 2.0\text{ s}$ in `{{res:sc32_04_trig_vectors_polar_seq_29:keys}}` reveals a $3.66\%$ period dilation of $T = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_29:value}}\text{ seconds}}$—enough to make a grandfather clock lose nearly $53\text{ minutes}$ per day!

#### Strain Gauge Rosette 2D Coordinate Rotation

When an aircraft wing skin is instrumented with a three-element strain gauge rosette, the gauges measure normal strains $\epsilon_x = 450\,\mu\epsilon$ and $\epsilon_y = 120\,\mu\epsilon$ along with engineering shear strain $\gamma_{xy} = 280\,\mu\epsilon$. What is the normal strain $\epsilon_{x'}$ along a rivet line rotated by $\theta = 30.0^\circ$? Because planar strain is a symmetric second-order tensor rather than a first-order vector (stretching a sheet equally along $+x$ and $-x$ returns to the exact same state after a $180^\circ$ rotation, not $360^\circ$), rotating the physical axes by $\theta = 30^\circ$ rotates the state point around **Mohr's circle** by the double angle $2\theta = 60^\circ$ about the hydrostatic mean strain $(\epsilon_x + \epsilon_y)/2$:

$$\epsilon_{x'} = \frac{\epsilon_x + \epsilon_y}{2} + \frac{\epsilon_x - \epsilon_y}{2}\cos(2\theta) + \frac{\gamma_{xy}}{2}\sin(2\theta)$$

On the stack, computing the hydrostatic mean strain $285\,\mu\epsilon$ first and adding the deviatoric normal cosine projection $82.5\,\mu\epsilon$ and shear sine projection $121.2436\,\mu\epsilon$ via `{{res:sc32_04_trig_vectors_polar_seq_33:keys}}` resolves the rotated normal strain $\epsilon_{x'} \approx 285 + 82.5 + 121.24 = \mathbf{488.74\,\mu\epsilon}$:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `450 {{key:ENTER}} 120 {{key:+}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $285.0000$ | Hydrostatic mean strain $(\epsilon_a + \epsilon_c)/2$ |
| 2 | `450 {{key:ENTER}} 120 {{key:-}} 2 {{key:÷}} 60 {{key:COS}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $367.5000$ | Add normal strain cosine transform $((\epsilon_a - \epsilon_c)/2)\cos(60^\circ)$ |
| 3 | `280 {{key:ENTER}} 2 {{key:÷}} 60 {{key:SIN}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$488.7436$** | Add shear strain sine transform $(\gamma_{xy}/2)\sin(60^\circ)$ for rotated strain $\epsilon_{x'}$ ($\mu\epsilon$) |

#### Wave Superposition with Arbitrary Phase Shift

When two coherent acoustic waves of the same frequency—with pressure amplitudes $A_1 = 2.40\text{ Pa}$ and $A_2 = 3.10\text{ Pa}$—arrive at a microphone with a relative phase difference of $\Delta\phi = 55.0^\circ$, their amplitudes add as rotating phasor vectors rather than simple scalars. By the exterior-angle Law of Cosines, the total intensity $A_{\text{res}}^2$ equals the incoherent power sum $A_1^2 + A_2^2$ plus the coherent interference cross-term $+2A_1 A_2\cos(\Delta\phi)$:

$$A_{\text{resultant}} = \sqrt{A_1^2 + A_2^2 + 2 A_1 A_2 \cos(\Delta\phi)}$$

Accumulating the incoherent power sum $A_1^2 + A_2^2 = 15.37\text{ Pa}^2$ in Step 1, adding the interference cross-term $2(2.4)(3.1)\cos(55^\circ) = 8.5348\text{ Pa}^2$ in Step 2, and extracting the square root in `{{res:sc32_04_trig_vectors_polar_seq_34:keys}}` yields the superposed acoustic pressure amplitude $A_{\text{res}} = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_34:value}}\text{ Pa}}$:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `2.4 {{key:x²}} 3.1 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $15.3700$ | Sum of squared wave amplitudes $A_1^2 + A_2^2$ |
| 2 | `2 {{key:ENTER}} 2.4 {{key:×}} 3.1 {{key:×}} 55 {{key:COS}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $23.9048$ | Add wave interference cross-term $2 A_1 A_2 \cos(\Delta\phi)$ |
| 3 | `{{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$4.8893$** | Extract square root for superposed wave amplitude $A_{\text{res}}$ |

#### Keplerian Orbit True Anomaly from Eccentric Anomaly

In orbital mechanics, solving Kepler's Equation (which we will automate with `{{key:SOLVE}}` in Chapter 7) yields a satellite's **eccentric anomaly** $E$—an auxiliary angle measured from the geometric *center* of the elliptical orbit. To point a telescope or tracking radar from the gravitating *focus* (where the central planet sits), we must convert $E$ into the physical **true anomaly** $\nu$. Carl Friedrich Gauss derived a half-angle tangent transformation that maps $E$ to $\nu$ across the entire orbit $(-\pi, \pi)$ without quadrant ambiguity. For an orbit with eccentricity $e = 0.240$ at eccentric anomaly $E = 40.0^\circ$, find the true anomaly $\nu$:

$$\tan\left(\frac{\nu}{2}\right) = \sqrt{\frac{1 + e}{1 - e}} \tan\left(\frac{E}{2}\right)$$

Evaluating the eccentricity stretch factor $\sqrt{(1+e)/(1-e)} = \sqrt{1.240/0.760}$ (`1.240 {{key:ENTER}} 0.760 {{key:÷}} {{key:√x}}` $\to 1.2773$—or directly from $e = 0.24$ via `1 {{key:ENTER}} 0.24 {{key:+}} 1 {{key:LASTX}} {{key:-}} {{key:÷}} {{key:√x}}`), multiplying by $\tan(E/2) = \tan(20^\circ)$ (`20 {{key:TAN}} {{key:×}}` $\to 0.4649$), and inverting via `{{key:ATAN}} 2 {{key:×}}` in `{{res:sc32_04_trig_vectors_polar_seq_37:keys}}` determines the satellite's true anomaly $\nu = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_37:value}}^\circ}$ ahead of periapsis.

#### Continued Trigonometric Product

Before moving to celestial navigation, let us test our stack discipline on a composite trigonometric fraction that combines products, sums, and root-sum-square quadrature:

$$x = \frac{\sin(35^\circ) \cos(42^\circ) + \tan(18^\circ)}{\sqrt{\sin^2(65^\circ) + \cos^2(25^\circ)}}$$

Notice a delightful geometric identity hiding in the denominator: because $25^\circ$ and $65^\circ$ are complementary angles ($25^\circ + 65^\circ = 90^\circ$), cofunction symmetry guarantees $\cos(25^\circ) = \sin(65^\circ)$, so the denominator is simply $\sqrt{2}\,\sin(65^\circ)$. Even when keyed straight through on the stack via `{{res:sc32_04_trig_vectors_polar_seq_40:keys}}`, the numerator waits patiently in Register $Y$ while the denominator quadrature forms in Register $X$ with zero parentheses:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `35 {{key:SIN}} 42 {{key:COS}} {{key:×}} 18 {{key:TAN}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.7512$ | Trigonometric numerator sum $\sin(35^\circ)\cos(42^\circ) + \tan(18^\circ)$ |
| 2 | `65 {{key:SIN}} {{key:x²}} 25 {{key:COS}} {{key:x²}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.7512$ | $1.2817$ | Denominator quadrature $\sqrt{\sin^2(65^\circ) + \cos^2(25^\circ)}$ |
| 3 | `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.5861$** | Divide numerator by denominator for continued trigonometric quotient |

---

### Celestial Navigation, Spherical Geodesy & Radical Cascades

Our closing pair of models concludes our trigonometric tour with spherical solar tracking and an inside-out nested trigonometric radical.

#### Solar Azimuth Angle Calculation

To steer a two-axis solar concentrator (or a migratory bird's time-compensated sun compass) at latitude $\phi = 32.0^\circ\text{ N}$ when the sun's seasonal declination is $\delta = 18.5^\circ$ and the solar hour angle is $\omega = 45.0^\circ$ ($3\text{ hours}$ before local solar noon, at $15^\circ\text{ per hour}$), we solve the **astronomical triangle** linking the North Celestial Pole, the observer's zenith, and the sun. Applying the Spherical Law of Cosines gives the sun's elevation angle $\alpha$ above the horizon and its compass azimuth $\gamma_s$:

$$\sin\alpha = \sin\phi \sin\delta + \cos\phi \cos\delta \cos\omega, \qquad \cos\gamma_s = \frac{\sin\alpha \sin\phi - \sin\delta}{\cos\alpha \cos\phi}$$

Evaluating the polar sine product $\sin\phi\sin\delta$ (`32 {{key:SIN}} 18.5 {{key:SIN}} {{key:×}}` $\to 0.1681$), adding the diurnal equatorial cosine product $\cos\phi\cos\delta\cos\omega$ (`32 {{key:COS}} 18.5 {{key:COS}} {{key:×}} 45 {{key:COS}} {{key:×}} {{key:+}}` $\to 0.7368$), and extracting the arcsine via `{{res:sc32_04_trig_vectors_polar_seq_41:keys}}` resolves the solar elevation $\alpha \approx \mathbf{47.46^\circ}$ ($47.4611^\circ$)—while `LASTX` automatically preserves $\sin\alpha = 0.7368$ ready for the azimuth formula.

#### Radical Trigonometric Nested Pyramid

Finally, consider a nested trigonometric radical pyramid that would require three layers of nested parentheses on an algebraic keypad:

$$x = \sqrt{\cos(28^\circ) + \sqrt{\sin(48^\circ) + \sqrt{\tan(15^\circ)}}}$$

By starting at the innermost $\tan(15^\circ)$ and peeling each square-root shell outward via `{{res:sc32_04_trig_vectors_polar_seq_53:keys}}`, the entire three-tier radical resolves to **`{{res:sc32_04_trig_vectors_polar_seq_53:value}}`** in nine keystrokes while never occupying more than two stack registers:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `15 {{key:TAN}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.5176$ | Initial square root tangent $\sqrt{\tan(15^\circ)}$ |
| 2 | `48 {{key:SIN}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.1228$ | Add sine term and extract nested root $\sqrt{\sin(48^\circ) + \dots}$ |
| 3 | `28 {{key:COS}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1.4163$** | Add cosine term and extract outer root for nested trigonometric radical |

---

## Further Exploration: Companion Workbooks & Applied Tie-Ins

> *For 29 additional worked engineering problems with full 4-register stack traces, see Chapter 4 of the [SC-32 Scientific Companion Problem & Casebook Workbook](../../curriculum/sc32-scientific-companion-workbook.md).*


The trigonometric and vector primitives developed in Chapter 4 form the backbone of surveying, astrodynamics, and structural statics across the **StackCalc Engineering & Speed Competition Workbooks**:

- **Geodetic Surveying & Celestial Navigation**: In **[Chapter 13: Applied STEM Case Studies](13-applied-stem-case-studies.md)** and **[Chapter 14: Speed & Precision Competition Playbook](14-uil-contest-playbook.md)**, you will chain `{{key:▸y,x}}`, `{{key:Σ+}}`, and `{{key:▸θ,r}}` to close multi-leg boundary traverses, apply Bowditch compass-rule adjustments, and solve great-circle Haversine routing.
- **AC Phasor & Impedance Transition**: In **[Chapter 5: Complex Numbers, Phasors & Impedance](05-complex-numbers-phasors.md)** and **[Chapter 13: Applied STEM Case Studies](13-applied-stem-case-studies.md)**, the 2D vector pair $(Y, X)$ is promoted into a full complex field where multiplication automatically scales magnitudes and adds phase angles.

### Synthesis Challenge Problems

1. **Zero-Re-Entry Inclined Plane Angle & Acceleration:** For $\theta = 34^\circ$ and $\mu_k = 0.22$ (from the inclined-plane friction analysis above), evaluate $a = g(\sin\theta - \mu_k\cos\theta)$ by typing `34` only once: key `34 {{key:SIN}} {{key:LASTX}} {{key:COS}} 0.22 {{key:×}} {{key:-}} 9.80665 {{key:×}}` ($\to \mathbf{3.6952\text{ m/s}^2}$).
2. **Single-Keystroke Power Triangle Decomposition:** Rather than computing $P = S\cos\phi$ and $Q = S\sin\phi$ separately as in our AC power triangle analysis, load angle $\phi = 32^\circ$ into $Y$ and apparent power $S = 1020\text{ VA}$ into $X$ and press `{{key:▸y,x}}` (`32 {{key:ENTER}} 1020 {{key:▸y,x}}`) to project both $Y = 540.52\text{ VAR}$ and $X = 865.01\text{ W}$ simultaneously.
3. **Closed-Loop 4-Leg Traverse Misclosure:** Accumulate a 4-leg survey traverse into `{{key:CLΣ}}` using `{{key:▸y,x}} {{key:Σ+}}`: Leg 1 ($120\text{ m}$ at $40^\circ$), Leg 2 ($95\text{ m}$ at $135^\circ$), Leg 3 ($130\text{ m}$ at $225^\circ$), and Leg 4 ($88.15\text{ m}$ at $310.4^\circ$). Recall `{{key:SUMS}}` and press `{{key:x⇄y}} {{key:▸θ,r}}` to inspect the linear closure vector in millimeters.

---

## Summary & Looking Ahead

Chapter 4 united trigonometric functions and 2D spatial vectors on the RPN stack. By bridging the unit circle to the physical register pair $(Y, X)$, you executed direct and inverse trigonometry, explored hyperbolic projections on physical catenaries, and mastered instantaneous polar-to-rectangular conversions (`{{key:▸θ,r}}`, `{{key:▸y,x}}`) with full four-quadrant $\text{atan2}$ sign integrity. Survey traverses, aerodynamic shock angles, and force resolutions unfolded directly on the stack with zero scratchpad bookkeeping.

Yet 2D vectors in Cartesian space represent only the gateway to a deeper mathematical realm: the complex plane. In **[Chapter 5: Complex Numbers, Phasors & Impedance](05-complex-numbers-phasors.md)**, the coordinate pair $(Y, X)$ is reinterpreted as real and imaginary components ($Y + Xi$). You will apply the `{{key:CMPLX}}` engine to add, multiply, invert, and exponentiate complex numbers in place, verify Euler's identity ($e^{i\pi} + 1 = 0$), and solve multi-branch AC electrical impedance networks without matrix software.

