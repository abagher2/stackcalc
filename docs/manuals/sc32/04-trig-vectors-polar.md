---
title: "Chapter 4: Trigonometry, Coordinate Systems & 2D Vectors | SC-32 Manual"
description: "Direct and inverse trigonometry, hyperbolic functions, exact axial angle clamping, polar-to-rectangular 2D vector conversions, and geodetic traverses on the StackCalc SC-32."
---

# Chapter 4: Trigonometry, Coordinate Systems & 2D Vectors

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 TRIGONOMETRY // VECTORS &amp; COORDINATE TRANSFORMS</span>
  <span class="te-viewport-status text-sky-400">● 2D POLAR/RECTANGULAR &bull; EXACT AXIAL CLAMPING &bull; GEODETIC TRAVERSE</span>
</div>

## Measuring the Earth with a Shadow: From Eratosthenes and Hipparchus to the Unit Circle Volvelle

In 240 BCE, Eratosthenes of Cyrene, director of the great Library of Alexandria, noticed a curious observation recorded in an ancient papyrus: at solar noon on the summer solstice in Syene (modern Aswan), vertical gnomon pillars cast no shadow, and the midday sun illuminated the deep water at the bottom of a vertical well. Yet five thousand stadia to the north, in Alexandria, a vertical gnomon cast a distinct shadow measuring one-fiftieth of a full circle ($7.2^\circ$). By applying simple angle proportionality, Eratosthenes calculated the Earth's circumference to within a few percentage points of modern satellite geodesy. Two centuries later, Hipparchus of Nicaea compiled the first table of chords—the ancestor of the modern sine function—tabulating celestial positions and laying the mathematical foundation for maritime navigation and astronomical ephemerides.

Trigonometry is not an invention of abstract algebra; it is the geometry of the physical universe, translating circular rotations into linear orthogonal coordinates. On the StackCalc SC-32, trigonometry bridges abstract analytical functions with concrete spatial geometry. For tactile learners, field surveyors, and engineering workstations, our physical 3D-printed **Unit Circle Trigonometry Volvelle** (`unit_circle_volvelle`) provides a rotating dual-dial apparatus linking degree angles, radian sectors, and Cartesian projections $(x, y) = (\cos\theta, \sin\theta)$.

{{blocks:unit_circle_volvelle|Unit Circle Volvelle Technical Resolver}}
*Figure 4.1: The physical Unit Circle Volvelle mechanical resolver provides a tactile analog computing engine, pairing angular degrees and radian arcs directly with orthogonal projections $(x, y) = (\cos\theta, \sin\theta)$ prior to calculator entry.*

| Angular Mode | LCD Annunciator | Full Circle Revolution | Right Angle | Primary Engineering Field |
| :--- | :---: | :---: | :---: | :--- |
| **Degrees** | `DEG` (Default) | $360^\circ$ | $90^\circ$ | Structural Civil Engineering, Geodesy, Avionics |
| **Radians** | `RAD` | $2\pi \approx 6.283185\text{ rad}$ | $\pi/2 \approx 1.570796\text{ rad}$ | Mathematical Physics, Calculus, Wave Mechanics |
| **Gradians** | `GRAD` | $400\text{ grad}$ | $100\text{ grad}$ | European Surveying, Mining Engineering |

### Mode Discipline & Setting
The angular mode defines how the trigonometric functions (`SIN`, `COS`, `TAN`) interpret input values, and what units are produced by inverse trigonometry (`ASIN`, `ACOS`, `ATAN`) and rectangular-to-polar conversion (`{{key:▸θ,r}}`):
* **Degrees Mode (`DEG`):** Press `{{key:↰}}` followed by `{{key:MODES}}`, then press `{{key:DEG}}` (LFU 1). The status line confirms `{{key:DEG}}`.
* **Radians Mode (`RAD`):** Press `{{key:↰}}` followed by `{{key:MODES}}`, then press `{{key:RAD}}` (LFU 2).
* **Gradians Mode (`GRAD`):** Press `{{key:↰}}` followed by `{{key:MODES}}`, then press `{{key:GRAD}}` (LFU 3).

In compliance with our **Mode Discipline Directive**, all problems in this chapter operate strictly in **Degrees mode (`{{key:DEG}}`)** without mid-lesson toggling.

### Instant Angular Conversions
When operating in Degrees mode, convert between angular systems using the stack:
* **Degrees to Radians:** `{{key:π}} {{key:×}} 180 {{key:÷}}` (or multiply by $\pi / 180 \approx 0.0174532925$).
* **Radians to Degrees:** `180 {{key:×}} {{key:π}} {{key:÷}}` (or multiply by $180 / \pi \approx 57.2957795131$).
* **Degrees to Gradians:** `400 {{key:×}} 360 {{key:÷}}` (or multiply by $10/9$).

<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>{{key:DEG}}</code> (Degrees angular mode default; Standard Base-10 Arithmetic; Full 12-digit scientific mantissa <code>{{key:ALL}}</code>).
</div>

---

{{blocks:sc32_rpn_calculation|StackCalc SC-32 Live 4-Level XYZT Stack Hardware Display}}

## Direct & Inverse Trigonometric Functions

The SC-32 provides dedicated hardware keys for the primary trigonometric functions and their inverses:

| Function | Dedicated Keystroke | Arity | Valid Domain | Output Range (in `{{key:DEG}}`) |
| :--- | :--- | :---: | :---: | :---: |
| **Sine** | `{{key:SIN}}` | Unary | $(-\infty, +\infty)$ | $[-1.0, +1.0]$ |
| **Cosine** | `{{key:COS}}` | Unary | $(-\infty, +\infty)$ | $[-1.0, +1.0]$ |
| **Tangent** | `{{key:TAN}}` | Unary | $\theta \ne 90^\circ + k \cdot 180^\circ$ | $(-\infty, +\infty)$ |
| **Arcsine** | `{{key:ASIN}}` | Unary | $[-1.0, +1.0]$ | $[-90^\circ, +90^\circ]$ |
| **Arccosine** | `{{key:ACOS}}` | Unary | $[-1.0, +1.0]$ | $[0^\circ, 180^\circ]$ |
| **Arctangent** | `{{key:ATAN}}` | Unary | $(-\infty, +\infty)$ | $(-90^\circ, +90^\circ)$ |

### Exact Axial Angle Clamping
Because $\pi$ is transcendental, conventional floating-point math libraries frequently evaluate $\cos(90^\circ)$ as an infinitesimal floating-point artifact such as $6.123233995736766 \times 10^{-17}$. In sensitive engineering calculations, this artifact can corrupt subsequent division operations.

The SC-32 firmware implements **Exact Axial Angle Clamping** in its transcendental arithmetic engine:
* $\sin(0^\circ) \equiv 0.0$ and $\cos(0^\circ) \equiv 1.0$
* $\sin(90^\circ) \equiv 1.0$ and $\cos(90^\circ) \equiv 0.0$ (Strictly exact zero!)
* $\sin(180^\circ) \equiv 0.0$ and $\cos(180^\circ) \equiv -1.0$
* $\sin(270^\circ) \equiv -1.0$ and $\cos(270^\circ) \equiv 0.0$
* $\tan(90^\circ)$ and $\tan(270^\circ)$ immediately raise `Error 02: DIVIDE BY 0` rather than returning false giant magnitudes ($1.63 \times 10^{16}$).

---

## Hyperbolic Functions (`{{key:HYP}}`)

Hyperbolic functions describe catenary hanging cables, special relativity velocity additions, and fluid stream lines. The SC-32 accesses hyperbolic functions using the two-key prefix `{{key:HYP}}` followed by the corresponding trigonometric key:

| Function | Key Sequence | Mathematical Definition | Valid Domain |
| :--- | :--- | :--- | :--- |
| **Hyperbolic Sine** | `{{key:HYP}} {{key:SIN}}` | $\sinh(x) = \frac{e^x - e^{-x}}{2}$ | $(-\infty, +\infty)$ |
| **Hyperbolic Cosine** | `{{key:HYP}} {{key:COS}}` | $\cosh(x) = \frac{e^x + e^{-x}}{2}$ | $(-\infty, +\infty)$ |
| **Hyperbolic Tangent** | `{{key:HYP}} {{key:TAN}}` | $\tanh(x) = \frac{\sinh(x)}{\cosh(x)}$ | $(-\infty, +\infty)$ |
| **Inverse Sinh** | `{{key:HYP}} {{key:ASIN}}` | $\operatorname{arsinh}(x) = \ln\left(x + \sqrt{x^2 + 1}\right)$ | $(-\infty, +\infty)$ |
| **Inverse Cosh** | `{{key:HYP}} {{key:ACOS}}` | $\operatorname{arcosh}(x) = \ln\left(x + \sqrt{x^2 - 1}\right)$ | $x \ge 1.0$ |
| **Inverse Tanh** | `{{key:HYP}} {{key:ATAN}}` | $\operatorname{artanh}(x) = \frac{1}{2}\ln\left(\frac{1+x}{1-x}\right)$ | $\lvert x\rvert < 1.0$ |

### Grounded Application 1: Catenary Transmission Line Cable Sag
A high-voltage transmission cable spans $L = 200\text{ meters}$ between two steel towers. The catenary curve parameter is $a = 800\text{ meters}$ ($a = T_0 / w$, where $T_0$ is horizontal cable tension and $w$ is unit weight).
Calculate cable sag $y$ at midpoint $x = 100\text{ meters}$:
$$y = a \left(\cosh\left(\frac{x}{a}\right) - 1\right) = 800 \left(\cosh\left(\frac{100}{800}\right) - 1\right) = 800 \times (\cosh(0.125) - 1)$$

Keystrokes: `{{res:sc32_04_trig_vectors_polar_seq_01:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_01:value}}`**

**Stack Execution & Register Dynamics:**
First, enter the half-span distance $x = 100\text{ m}$ (`100 {{key:ENTER}}`, $T: 0.0000, Z: 0.0000, Y: 100.0000, X: 100.0000$). Divide by catenary parameter $a = 800$ (`800 {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.1250$) to yield the dimensionless argument $x/a = 0.125$. Evaluate the hyperbolic cosine (`{{key:HYP}} {{key:COS}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.0078$), subtract unity (`1 {{key:-}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.007823$), and scale back by parameter $a$ (`800 {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 6.2584$).

The transmission line experiences a midpoint sag of **$6.26\text{ meters}$**.

---

### Grounded Application 2: Relativistic Velocity Addition
In Einstein's Special Theory of Relativity, velocities do not add linearly. Instead, velocity parameterizes via **rapidity** $\theta = \operatorname{atanh}(v/c)$. When two reference frames move with relative velocities $v_1$ and $v_2$, their rapidities add directly:
$$\theta_{\text{total}} = \theta_1 + \theta_2 \implies v_{\text{total}} = c \tanh\left(\operatorname{atanh}\left(\frac{v_1}{c}\right) + \operatorname{atanh}\left(\frac{v_2}{c}\right)\right)$$

An interstellar probe travels at $v_1 = 0.75c$ relative to Earth, and launches a scout missile forward at $v_2 = 0.60c$ relative to the probe. Determine the missile's speed relative to Earth in units of $c$:

Keystrokes: `{{res:sc32_04_trig_vectors_polar_seq_02:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_02:value}}`**

**Stack Execution & Register Dynamics:**
Transform velocity $v_1 = 0.75c$ into its relativistic rapidity parameter (`0.75 {{key:HYP}} {{key:ATAN}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.9730$). Next, compute the rapidity for the second frame $v_2 = 0.60c$ directly onto the stack (`0.60 {{key:HYP}} {{key:ATAN}}`, $T: 0.0000, Z: 0.0000, Y: 0.9730, X: 0.6931$). Sum the collinear rapidities (`{{key:+}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.6661$) to get total rapidity $\theta_{\text{total}} = 1.6661$, and map back to normalized velocity space via hyperbolic tangent (`{{key:HYP}} {{key:TAN}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.9310$).

The missile travels at **$0.931c$** ($93.1\%$ the speed of light), strictly preserving the cosmic speed limit ($v < c$).

---

## 2D Coordinate Transformations: Polar $\leftrightarrow$ Rectangular

The SC-32 provides two-way conversions between Cartesian rectangular coordinates $(x, y)$ and polar vector coordinates $(r, \theta)$:

| Transformation | Dedicated Keystroke | Stack Input ($Y, X$) | Stack Output ($Y, X$) | Mathematical Formula |
| :--- | :--- | :--- | :--- | :--- |
| **Polar to Rectangular** | `{{key:▸y,x}}` | $Y = \theta$ (Angle in active mode)<br>$X = r$ (Radius / Magnitude) | $Y = y = r \sin\theta$<br>$X = x = r \cos\theta$ | $(x, y) = (r\cos\theta, r\sin\theta)$ |
| **Rectangular to Polar** | `{{key:▸θ,r}}` | $Y = y$ (Orthogonal vertical)<br>$X = x$ (Orthogonal horizontal) | $Y = \theta = \operatorname{atan2}(y, x)$<br>$X = r = \sqrt{x^2 + y^2}$ | $(r, \theta) = (\sqrt{x^2+y^2}, \operatorname{atan2}(y, x))$ |

{{res:sc32_phasor_mag:screenshot|Impedance phasor 3 + j4 rectangular-to-polar conversion → r = 5, theta = 53.1301 deg}}
*Figure 4.2: Direct rectangular-to-polar vector conversion on the StackCalc SC-32 places the angle $\theta = 53.1301^\circ$ in Register $Y$ and the radial magnitude $r = 5.0000$ in Register $X$.*

### Grounded Application 3: Aircraft Wind Triangle & Crosswind Correction
A pilot flying an aircraft plans a cross-country leg:
* True Airspeed (TAS): $V_{\text{air}} = 220.0\text{ knots}$
* Desired True Course: $\text{Heading} = 045.0^\circ$ (Northeast)
* Aloft Crosswind: $V_{\text{wind}} = 35.0\text{ knots}$ blowing *from* $310.0^\circ$ (blowing *toward* $130.0^\circ$).

Determine the required ground speed ($V_{\text{ground}}$) and actual ground track angle ($\theta_{\text{track}}$) resulting from vector summation:
$$\vec{V}_{\text{ground}} = \vec{V}_{\text{air}} + \vec{V}_{\text{wind}}$$

#### Step 1: Resolve Airspeed Vector into Rectangular Components
Keystrokes: `{{res:sc32_04_trig_vectors_polar_seq_03:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_03:value}}`**
* $Y = 155.5635\text{ kts}$ (North component $V_{\text{air}, y}$)
* $X = 155.5635\text{ kts}$ (East component $V_{\text{air}, x}$)
Store components: `{{key:STO}} 1 {{key:x⇄y}} {{key:STO}} 2` (Reg 1 = East, Reg 2 = North).

#### Step 2: Resolve Wind Vector into Rectangular Components
Wind blowing from $310^\circ$ travels toward $310^\circ - 180^\circ = 130^\circ$:
Keystrokes: `{{res:sc32_04_trig_vectors_polar_seq_04:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_04:value}}`**
* $Y = 26.8116\text{ kts}$ (North wind component)
* $X = -22.4976\text{ kts}$ (West wind drift component / negative East)

#### Step 3: Vector Summation & Polar Conversion
1. Add East components: `{{key:RCL}} 1 {{key:+}}` $\rightarrow$ $X = 133.0659\text{ kts}$ (Total East velocity)
2. Add North components: `{{key:x⇄y}} {{key:RCL}} 2 {{key:+}}` $\rightarrow$ $X = 182.3751\text{ kts}$ (Total North velocity)
3. Convert back to polar vector:
   `{{key:x⇄y}}` (puts North $y$ in $Y$, East $x$ in $X$) `{{key:▸θ,r}}`
   * **Register X (Ground Speed):** **$225.76\text{ knots}$**
   * **Register Y (Ground Track Angle):** **$53.89^\circ$**

The aircraft makes good a ground speed of **$225.8\text{ knots}$** on a track of **$053.9^\circ$**.

<div class="admonition tip">
<p class="admonition-title">Rapid Calculation &amp; Equation Entry: Instant Vector Summation via Coordinate Conversion</p>
<p>
In rapid calculation sprints and competitive STEM exams, 2D vector addition problems (such as aircraft wind triangles, resultant forces, and surveyor traverses) appear frequently. Solving them algebraically requires tedious $\cos$ and $\sin$ calculations that consume 30+ seconds.
</p>
<p>
On the SC-32, harness <code>{{key:▸y,x}}</code> and <code>{{key:▸θ,r}}</code> to add vectors directly on the stack without writing down a single intermediate component:
</p>
<ol>
  <li><strong>First Vector ($r_1 \angle \theta_1$):</strong> <code>&theta;1 {{key:ENTER}} r1 {{key:▸y,x}}</code> &rarr; $Y = y_1, X = x_1$. Store: <code>{{key:STO}} 1 {{key:x⇄y}} {{key:STO}} 2</code>.</li>
  <li><strong>Second Vector ($r_2 \angle \theta_2$):</strong> <code>&theta;2 {{key:ENTER}} r2 {{key:▸y,x}}</code> &rarr; $Y = y_2, X = x_2$.</li>
  <li><strong>Sum &amp; Convert:</strong> <code>{{key:RCL}} 1 {{key:+}} {{key:x⇄y}} {{key:RCL}} 2 {{key:+}} {{key:x⇄y}} {{key:▸θ,r}}</code>.</li>
</ol>
<p>
In less than 12 seconds, Register $X$ holds resultant magnitude $R$ and Register $Y$ holds heading $\theta$—saving over 20 seconds per sprint problem!
</p>
</div>

### The Algebraic Trap vs. StackCalc Superpower Showdown

| Challenge / Engineering Task | The Algebraic Calculator Trap (TI-84 / Infix) | Algebraic Keystrokes & Clutter | The StackCalc Superpower (RPN Stack + Visual Studio) | StackCalc Keystrokes | The Stack Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **2-Leg Vector Traverse Closure**:<br>$120\text{ m} \angle 35^\circ + 85\text{ m} \angle 110^\circ$ | Separate scalar resolution: `1 2 0 * c o s ( 3 5 ) + 8 5 * c o s ( 1 1 0 ) =`<br>and `1 2 0 * s i n ( 3 5 ) + 8 5 * s i n ( 1 1 0 ) =`<br>then $\sqrt{X^2+Y^2}$ and $\tan^{-1}(Y/X)$.<br>*Trap: Quadrant sign errors, transcription lag, and lost intermediate coordinates.* | 65 | **Coordinate Transformation Bridge**:<br>`35 {{key:ENTER}} 120 {{key:▸y,x}} {{key:STO}} 1 {{key:x⇄y}} {{key:STO}} 2 110 {{key:ENTER}} 85 {{key:▸y,x}} {{key:RCL}} 1 {{key:+}} {{key:x⇄y}} {{key:RCL}} 2 {{key:+}} {{key:x⇄y}} {{key:▸θ,r}}`<br>Instant vector resolution and recombination on stack. | 22 | **66% fewer strokes + automatic 4-quadrant resolve ($164.03\text{ m} \angle 65.04^\circ$)** |
| **Law of Cosines Oblique Side**:<br>$c = \sqrt{a^2 + b^2 - 2ab\cos C}$<br>($a=25, b=36, C=48^\circ$) | `√( 2 5 ^ 2 + 3 6 ^ 2 - 2 * 2 5 * 3 6 * c o s ( 4 8 ) ) =`<br>*Trap: Unbalanced radical parentheses; square root evaluated early on first term if bracket omitted.* | 34 | **Stack Accumulation & Radical**:<br>`25 {{key:x²}} 36 {{key:x²}} {{key:+}} 2 {{key:ENTER}} 25 {{key:×}} 36 {{key:×}} 48 {{key:COS}} {{key:×}} {{key:-}} {{key:√x}}`<br>Evaluates sum of squares, subtracts cross product, and takes square root directly. | 24 | **29% fewer strokes + zero parenthesis nesting & visible intermediate energy states** |

---

## 3D Spherical Trigonometry: Great Circle Distance

On a spherical Earth with mean volumetric radius $R_E = 6,371.0\text{ km}$, the shortest distance between two points $(\phi_1, \lambda_1)$ and $(\phi_2, \lambda_2)$ is along the Great Circle arc:
$$\cos d = \sin\phi_1 \sin\phi_2 + \cos\phi_1 \cos\phi_2 \cos(\lambda_2 - \lambda_1)$$
$$D = R_E \times d_{\text{rad}}$$

Calculate the great circle flight distance between:
* **San Francisco (SFO):** $\phi_1 = 37.6189^\circ\text{ N}, \lambda_1 = -122.3750^\circ\text{ W}$
* **Tokyo Narita (NRT):** $\phi_2 = 35.7720^\circ\text{ N}, \lambda_2 = 140.3929^\circ\text{ E}$

Difference in longitude:
$$\Delta\lambda = 140.3929^\circ - (-122.3750^\circ) = 262.7679^\circ \equiv 360^\circ - 262.7679^\circ = 97.2321^\circ$$

Keystrokes:
1. Product 1 ($\sin\phi_1 \sin\phi_2$):
   `{{res:sc32_04_trig_vectors_polar_seq_54:keys}}` $\rightarrow$ $X = 0.356499$
2. Product 2 ($\cos\phi_1 \cos\phi_2 \cos\Delta\lambda$):
   `{{res:sc32_04_trig_vectors_polar_seq_55:keys}}` $\rightarrow$ $X = -0.081190$
3. Sum and Arccos:
   `{{key:+}} {{key:ACOS}}` $\rightarrow$ $X = 74.0154^\circ$
4. Convert angular distance to kilometers:
   `{{key:π}} {{key:×}} 180 {{key:÷}} 6371 {{key:×}}` $\rightarrow$ **$8,229.4\text{ km}$** ($5,113.5\text{ miles}$)

---

## Applied Civil Geodesy: Closed-Loop Traverse Survey

In civil surveying and geodetics, a closed-loop traverse consists of connected courses where each leg is measured by course distance $r$ and azimuth angle $\theta$. 

A closed boundary must return precisely to its origin station:
$$\Sigma \Delta x = 0 \quad (\text{Departure Closure}), \quad \Sigma \Delta y = 0 \quad (\text{Latitude Closure})$$

### Traverse Boundary Specifications (4 Stations)
* **Leg 1:** Distance $r = 100.0\text{ m}$, Azimuth $\theta = 60.0^\circ$
* **Leg 2:** Distance $r = 80.0\text{ m}$, Azimuth $\theta = 150.0^\circ$
* **Leg 3:** Distance $r = 100.0\text{ m}$, Azimuth $\theta = 240.0^\circ$
* **Leg 4:** Distance $r = 80.0\text{ m}$, Azimuth $\theta = 330.0^\circ$

### RPN Execution Workflow via Stats Accumulator (`{{key:Σ+}}`)
Because `{{key:▸y,x}}` places $\Delta y$ in Register $Y$ and $\Delta x$ in Register $X$, **the output matches the exact $(Y, X)$ statistical input convention for `{{key:Σ+}}`!** You can accumulate survey legs directly into statistical memory with zero stack reordering!

First, clear statistical registers: `{{key:CLΣ}}`

#### Leg 1: $\theta = 60^\circ, r = 100\text{ m}$
Keystrokes: `{{res:sc32_04_trig_vectors_polar_seq_05:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_05:value}}`**

Push angle and radius (`60 {{key:ENTER}} 100`, $T: 0.0000, Z: 0.0000, Y: 60.0000, X: 100.0000$). Execute polar-to-rectangular conversion (`{{key:▸y,x}}`, $T: 0.0000, Z: 0.0000, Y: 86.6025, X: 50.0000$), yielding northing departure $\Delta y = 86.6025\text{ m}$ in Register $Y$ and easting latitude $\Delta x = 50.0000\text{ m}$ in Register $X$. Accumulate into statistical memory (`{{key:Σ+}}`, $n=1$).

#### Leg 2: $\theta = 150^\circ, r = 80\text{ m}$
Keystrokes: `{{res:sc32_04_trig_vectors_polar_seq_06:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_06:value}}`**

Push angle and distance (`150 {{key:ENTER}} 80`, $T: 0.0000, Z: 0.0000, Y: 150.0000, X: 80.0000$). Convert coordinates (`{{key:▸y,x}}`, $T: 0.0000, Z: 0.0000, Y: 40.0000, X: -69.2820$), giving $\Delta y = 40.0000\text{ m}$ and $\Delta x = -69.2820\text{ m}$. Accumulate into survey registers (`{{key:Σ+}}`, $n=2$).

#### Leg 3: $\theta = 240^\circ, r = 100\text{ m}$
Keystrokes: `{{res:sc32_04_trig_vectors_polar_seq_07:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_07:value}}`**

Push bearing and leg distance (`240 {{key:ENTER}} 100`, $T: 0.0000, Z: 0.0000, Y: 240.0000, X: 100.0000$). Transform to rectangular components (`{{key:▸y,x}}`, $T: 0.0000, Z: 0.0000, Y: -86.6025, X: -50.0000$), yielding $\Delta y = -86.6025\text{ m}$ and $\Delta x = -50.0000\text{ m}$. Accumulate (`{{key:Σ+}}`, $n=3$).

#### Leg 4: $\theta = 330^\circ, r = 80\text{ m}$
Keystrokes: `{{res:sc32_04_trig_vectors_polar_seq_08:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_08:value}}`**

Enter closing course and distance (`330 {{key:ENTER}} 80`, $T: 0.0000, Z: 0.0000, Y: 330.0000, X: 80.0000$). Resolve to components (`{{key:▸y,x}}`, $T: 0.0000, Z: 0.0000, Y: -40.0000, X: 69.2820$), producing $\Delta y = -40.0000\text{ m}$ and $\Delta x = 69.2820\text{ m}$. Complete traverse accumulation (`{{key:Σ+}}`, $n=4$).

### Verifying Coordinate Closure & Precision Misclosure
Recall Departure Sum: `{{key:SUMS}}` $\to \Sigma x = 0.0000\text{ m}$  
Recall Latitude Sum: `{{key:SUMS}}` $\to \Sigma y = 0.0000\text{ m}$  
Misclosure Error: $\sqrt{(\Sigma x)^2 + (\Sigma y)^2} = \mathbf{0.0000\text{ m}}$ (Exact mathematical closure!).

### Boundary Perimeter and Enclosed Land Area
* **Perimeter:** $100 + 80 + 100 + 80 = \mathbf{360.0\text{ meters}}$
* **Survey Enclosed Area:** $100 \times 80 = \mathbf{8,000.0\text{ m}^2}$ ($0.80\text{ hectares}$ / $1.977\text{ acres}$).

---

## Diagnostic Checkpoints & Self-Tests

> **Diagnostic Checkpoint 4.1: Angular Mode Verification**
> Key in `{{res:sc32_04_trig_vectors_polar_seq_56:keys}}`.
> *Expected Result:* In Degrees mode (`{{key:DEG}}`), the display reads `0.707106781187`.
> *If you see $0.850903524534$,* your calculator is in Radians mode (`{{key:RAD}}`). Press `{{key:DEG}}` to restore Degrees baseline.

> **Diagnostic Checkpoint 4.2: Polar-to-Rectangular Coordinate Order**
> Key in `{{res:sc32_04_trig_vectors_polar_seq_57:keys}}`.
> *Expected Result:* $X = 0.0000$ and $Y = 10.0000$.
> *If you see $X = 10.0000$ and $Y = 0.0000$,* you loaded the radius into $Y$ and angle into $X$. Always remember the mnemonic: **Angle $\theta$ is in $Y$, Radius $r$ is in $X$**.

---

## Vector Algebra & Spatial Coordinate Rotations

Vector mechanics provides the mathematical language for aerospace guidance, structural statics, and electromagnetic field theory:

<div class="admonition note">
<p class="admonition-title">2D &amp; 3D Vector Operational Conventions</p>
<ol>
  <li><strong>Vector Addition ($\sum \vec{V} = \vec{V}_1 + \vec{V}_2 + \dots$):</strong>
    <ul>
      <li>Convert each polar vector $(r, \theta)$ to Cartesian $(x, y)$ via <code>{{key:▸y,x}}</code>.</li>
      <li>Accumulate directly into statistical memory via <code>{{key:Σ+}}</code> ($y$ in $Y$, $x$ in $X$).</li>
      <li>Resultant components: $\sum x$ in Register $X$, $\sum y$ in Register $Y$ via <code>{{key:SUMS}}</code>.</li>
      <li>Convert back to resultant polar magnitude and bearing via <code>{{key:▸θ,r}}</code>.</li>
    </ul>
  </li>
  <li><strong>2D Coordinate Frame Rotation:</strong>
    $$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$
    Evaluated on the stack in 6 keystrokes using <code>{{key:▸θ,r}}</code>, angular addition of rotation angle $\Delta\theta$, and <code>{{key:▸y,x}}</code>.
  </li>
  <li><strong>3D Vector Magnitude &amp; Direction Cosines:</strong>
    $$|\vec{V}| = \sqrt{V_x^2 + V_y^2 + V_z^2}$$
    Direction cosines: $\cos\alpha = V_x / |\vec{V}|$, $\cos\beta = V_y / |\vec{V}|$, $\cos\gamma = V_z / |\vec{V}|$.
  </li>
</ol>
</div>

---

## Geodetic Coordinate Systems & WGS84 Ellipsoidal Geometry

In precise geodetic surveying and navigation, the Earth is modeled as an oblate reference ellipsoid (WGS84):
* Semi-major equatorial axis: $a = 6,378,137.0\text{ meters}$
* Semi-minor polar axis: $b = 6,356,752.3142\text{ meters}$
* First flattening factor: $f = \frac{a - b}{a} = \frac{1}{298.257223563} \approx 0.00335281066$
* First eccentricity squared: $e^2 = 2f - f^2 = \frac{a^2 - b^2}{a^2} \approx 0.00669437999014$

<div class="admonition note">
<p class="admonition-title">WGS84 Ellipsoidal Geodesic Reference Equations</p>
<ol>
  <li><strong>Prime Vertical Radius of Curvature $N(\phi)$:</strong>
    $$N(\phi) = \frac{a}{\sqrt{1 - e^2 \sin^2\phi}}$$
  </li>
  <li><strong>Meridional Radius of Curvature $M(\phi)$:</strong>
    $$M(\phi) = \frac{a(1 - e^2)}{(1 - e^2 \sin^2\phi)^{3/2}}$$
  </li>
  <li><strong>Cartesian Geocentric Coordinates $(X, Y, Z)$ from Geodetic $(\phi, \lambda, h)$:</strong>
    $$\begin{aligned}
    X &= (N(\phi) + h) \cos\phi \cos\lambda \\
    Y &= (N(\phi) + h) \cos\phi \sin\lambda \\
    Z &= (N(\phi)(1 - e^2) + h) \sin\phi
    \end{aligned}$$
  </li>
</ol>
</div>

---

## Coordinate Transformation & Vector Architecture Notes

### Two-Argument Vector Operations & Stack Invariance
On the SC-32, two-dimensional coordinate transformations (`{{key:▸θ,r}}` and `{{key:▸y,x}}`) operate as true two-argument dyadic transformations on the primary register pair $(Y, X)$. Loading component values requires only keying the orthogonal pair into the stack:
- In rectangular-to-polar conversion (`{{key:▸θ,r}}`), Register $Y$ holds the vertical component ($y$) and Register $X$ holds the horizontal component ($x$). Upon execution, Register $X$ receives the radial vector magnitude $r = \sqrt{x^2 + y^2}$, while Register $Y$ receives the true angle $\theta$.
- In polar-to-rectangular conversion (`{{key:▸y,x}}`), Register $Y$ holds the angle ($\theta$) and Register $X$ holds the radius ($r$). Upon execution, Register $X$ receives the horizontal coordinate $x = r\cos\theta$, and Register $Y$ receives the vertical coordinate $y = r\sin\theta$.

Crucially, both transformations preserve Registers $Z$ and $T$ completely intact, enabling vector components to be computed and manipulated without disturbing ongoing chained calculations.

### Four-Quadrant Sign Integrity via `atan2`
In conventional algebraic calculators, evaluating vector angles using the single-argument inverse tangent $\arctan(y/x)$ introduces a fundamental ambiguity: dividing negative coordinates (such as $y = -4, x = -3$) yields a positive quotient ($+1.3333$), causing $\arctan$ to return $+53.13^\circ$ (Quadrant I) rather than the true vector direction of $-126.87^\circ$ or $233.13^\circ$ (Quadrant III). Correcting this error algebraically requires manual inspection of component signs and conditional quadrant addition rules.

The SC-32's `{{key:▸θ,r}}` primitive implements a full four-quadrant $\text{atan2}(y, x)$ algorithm. Because $y$ and $x$ reside in separate physical registers, the processor examines the mathematical signs of both coordinates independently before calculating the angle. The resulting polar angle $\theta$ is accurately positioned across all four quadrants ($[-180^\circ, +180^\circ]$ or $[-\pi, +\pi]$) without user intervention or post-processing logic.

### Chained Geodetic Traverses and Dead Reckoning
In navigational dead reckoning and land surveying, traverses consist of successive polar course legs (distance $r_i$ and bearing $\theta_i$) that must be accumulated into global Cartesian coordinates (Northing and Easting). On the SC-32, each traverse leg is converted to rectangular offsets via `{{key:▸y,x}}`, added directly to running accumulators, and transformed back into closing bearing and range via `{{key:▸θ,r}}` with zero scratchpad transcription.

### Hyperbolic Functions and Physical Catenaries
Hyperbolic functions (`SINH`, `COSH`, `TANH`) and their inverse counterparts (`ASINH`, `ACOSH`, `ATANH`) are accessed directly using the `{{key:HYP}}` prefix key without mode shifts or menu navigation. These functions operate directly on 64-bit IEEE 754 representations, providing rapid evaluation of physical catenary cable sags ($y = a \cosh(x/a)$), relativistic rapidities, and fluid flow stream functions.

---

## Engineering Design Briefing: Autonomous Geodetic Navigation & Trans-Oceanic Surveying (Problems 4.1 through 4.45)

> **Hands-On Studio Proof: Blocks &rarr; Calculator**  
> Before computing numerical bearings and spherical trigonometry on the SC-32, manipulate physical angle wedges on the Unit Circle Volvelle (`docs/assets/renders/unit-circle-volvelle-hero.png`) and dial in bearings manually (`docs/assets/renders/volvelle-interaction-01.jpg`). Physically rotating through compass quadrants grounds the $(Y, X)$ stack allocation conventions and eliminates sign errors during open-ocean dead reckoning.

The following 45 professional engineering case studies span geodetic traverses, aerospace wind triangle corrections, solar elevation ephemerides, WGS84 ellipsoidal geodesics, and RF antenna phase synthesis.

---

> **Thematic Arc I — Ballistics, Surveying Baselines & Angular Kinematics (Problems 4.1–4.10):** We open in degree and radian modes, resolving projectile trajectories, inclined planes, and optical surveying baselines.

### Problem 4.1: Projectile Trajectory Maximum Height and Range
An artillery shell is fired with muzzle velocity $v_0 = 85.0\text{ m/s}$ at elevation angle $\theta = 38.0^\circ$ ($g = 9.80665\text{ m/s}^2$):
$$H_{\max} = \frac{(v_0 \sin\theta)^2}{2g}, \quad R = \frac{v_0^2 \sin(2\theta)}{g}$$

**Keystrokes for $H_{\max}$:** `{{res:sc32_04_trig_vectors_polar_seq_09:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_09:value}}`**
**Keystrokes for Range $R$:** `{{res:sc32_04_trig_vectors_polar_seq_10:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_10:value}}`**

**4-Level Stack Trace ($H_{\max}$):**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `85` `{{key:ENTER}}` `38` `{{key:SIN}}` `{{key:×}}`| $0.0000$ | $0.0000$ | $0.0000$ | $52.3312$ | Vertical velocity component $v_{0y}$ |
| `{{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2,738.5574$ | $v_{0y}^2$ numerator |
| `2` `{{key:ENTER}}` `9.80665` `{{key:×}}` | $0.0000$ | $0.0000$ | $2738.5574$ | $19.6133$ | Denominator $2g$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$139.6275\text{ m}$** | Peak height $H_{\max}$ |

Range evaluation yields: $R = \mathbf{714.8605\text{ m}}$.

---

### Problem 4.2: Oblique Triangle Solution via Law of Cosines
A triangular boundary survey measures sides $a = 45.0\text{ m}$, $b = 62.0\text{ m}$, and included angle $C = 48.0^\circ$. Find opposing side $c$:
$$c = \sqrt{a^2 + b^2 - 2 a b \cos C} = \sqrt{45^2 + 62^2 - 2(45)(62)\cos(48^\circ)}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_11:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_11:value}}`**

**Stack State Inspection:**
1. $45^2 + 62^2 = 2025 + 3844 = 5869.00$
2. $2(45)(62)\cos(48^\circ) = 5580 \times 0.669131 = 3733.7486$
3. Difference $= 5869 - 3733.7486 = 2135.2514$
4. Square root: $c = \mathbf{46.2088\text{ m}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `45 {{key:x²}} 62 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $5869.0000$ | Sum of squared sides $a^2 + b^2 = 2025 + 3844 = 5869$ |
| 2 | `2 {{key:ENTER}} 45 {{key:×}} 62 {{key:×}} 48 {{key:COS}} {{key:×}}` | $0.0000$ | $0.0000$ | $5869.0000$ | $3733.7488$ | Law of cosines cross-term $2 a b \cos C$ |
| 3 | `{{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2135.2512$ | Quadratic difference $(a^2 + b^2 - 2ab\cos C)$ |
| 4 | `{{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$46.2088$** | Extract square root for side $c$ (m) |

---

### Problem 4.3: Oblique Triangle Law of Sines Angle Determination
In triangle with $a = 45.0\text{ m}$, $b = 62.0\text{ m}$, angle $A = 32.5^\circ$. Find angle $B$:
$$\frac{\sin B}{b} = \frac{\sin A}{a} \implies B = \arcsin\left(\frac{b \sin A}{a}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_12:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_12:value}}^\circ}$.

> ***The LASTX Dual-Branch Trick & Sine Projection*** — Scale side length by opposite angle sine, divide by opposing side $a$, and apply arcsine in place without scratchpad memory {{cite:hp15c1982}}.

Enter side $b = 62.0\text{ m}$ and compute the sine projection of angle $A = 32.5^\circ$ (`62 {{key:ENTER}} 32.5 {{key:SIN}} {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 33.3126$). Divide by opposing side $a = 45.0\text{ m}$ (`45 {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.7403$) to form the ratio $\sin B = 0.7403$. Extract the arcsine directly in place (`{{key:ASIN}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 47.7552$), resolving interior vertex angle $B = \mathbf{47.76^\circ}$.

---

### Problem 4.4: Static Equilibrium of Crane Boom and Cable
Crane boom weight $W = 28.0\text{ kN}$ at angle $\theta = 35.0^\circ$ from horizontal, supported by tie cable at angle $\phi = 25.0^\circ$ to boom. Cable tension:
$$T = \frac{W \cos\theta}{\sin\phi} = \frac{28.0 \cos(35^\circ)}{\sin(25^\circ)}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_13:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_13:value}}\text{ kN}}$.

Load payload weight $W = 28.0\text{ kN}$ and multiply by inclination cosine (`28 {{key:ENTER}} 35 {{key:COS}} {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 22.9363$). Divide by cable angle sine $\sin(25^\circ)$ (`25 {{key:SIN}} {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 54.2718$) to determine guy cable tension $T \approx \mathbf{54.27\text{ kN}}$.

---

### Problem 4.5: Snell's Law of Optical Refraction
Light ray incident from air ($n_1 = 1.000$) into dense flint glass ($n_2 = 1.660$) at incidence angle $\theta_1 = 55.0^\circ$. Find refracted angle $\theta_2$:
$$\sin\theta_2 = \frac{n_1 \sin\theta_1}{n_2} \implies \theta_2 = \arcsin\left(\frac{\sin(55^\circ)}{1.660}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_14:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_14:value}}^\circ}$.

Evaluate incident angle sine (`55 {{key:SIN}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.8192$). Divide by flint glass refractive index $n_2 = 1.660$ (`1.660 {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.4935$). Extract the arcsine in place (`{{key:ASIN}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 29.5686$), yielding refracted ray angle $\theta_2 \approx \mathbf{29.57^\circ}$.

---

### Problem 4.6: Critical Angle for Total Internal Reflection
Fiber optic core ($n_1 = 1.480$) and cladding ($n_2 = 1.450$). Find critical angle $\theta_c$:
$$\theta_c = \arcsin\left(\frac{n_2}{n_1}\right) = \arcsin\left(\frac{1.450}{1.480}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_15:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_15:value}}^\circ}$.

> ***The x⇄y Denominator Flip & Snell Inversion*** — Divide refractive indices via stack swap and take arcsine in place without intermediate scratch registers {{cite:horowitz2015,hp15c1982}}.

Form the core-to-cladding refractive index ratio (`1.450 {{key:ENTER}} 1.480 {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.9797$). Extract the arcsine in place (`{{key:ASIN}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 78.4441$) to determine the total internal reflection critical angle $\theta_c \approx \mathbf{78.44^\circ}$.

---

### Problem 4.7: Highway Super-Elevation Banking Angle
Highway curve radius $R = 350.0\text{ m}$ designed for speed $v = 100.0\text{ km/h} = 27.7778\text{ m/s}$ with zero lateral friction ($g = 9.80665\text{ m/s}^2$):
$$\tan\theta = \frac{v^2}{g R} \implies \theta = \arctan\left(\frac{v^2}{g R}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_16:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_16:value}}^\circ}$.

> ***The Constant-in-T Pipeline & Centripetal Balance*** — Convert highway design speed to SI velocity, square in place, and divide by gravitational centripetal product $g R$ {{cite:ellenberg2014,hp15c1982}}.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `100 {{key:ENTER}} 3.6 {{key:÷}} {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $771.6049$ | Square speed in m/s $(v/3.6)^2$ |
| 2 | `9.80665 {{key:ENTER}} 350 {{key:×}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.2248$ | Divide by centripetal gravity denominator $g R$ |
| 3 | `{{key:ATAN}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$12.6698$** | Extract arctangent for banking angle $\theta$ (degrees) |

---

### Problem 4.8: Traverse Linear Misclosure Precision Ratio
A traverse boundary has total perimeter $P = 1,450.0\text{ m}$. Sum of departures $\Sigma x = +0.038\text{ m}$, sum of latitudes $\Sigma y = -0.024\text{ m}$. Calculate closure precision $1:K$:
$$\text{Misclosure} = \sqrt{(\Sigma x)^2 + (\Sigma y)^2}, \quad K = \frac{P}{\text{Misclosure}}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_17:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_17:value}}`**

Compute the linear misclosure distance from departure and latitude coordinate errors (`0.038 {{key:x²}} 0.024 {{key:x²}} {{key:+}} {{key:√x}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.0449$). Enter total perimeter $P = 1,450\text{ m}$, swap registers to place perimeter in $Y$, and divide (`1450 {{key:x⇄y}} {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 32262.0766$). This yields a closure precision ratio of **$1:32,262$** (exceeding first-order geodetic survey standards).

---

### Problem 4.9: Ground Satellite Elevation Angle
Earth radius $R_E = 6,371\text{ km}$, satellite orbital altitude $h = 850\text{ km}$, angular distance from sub-satellite point $\gamma = 18.0^\circ$:
$$\tan E = \frac{\cos\gamma - \frac{R_E}{R_E + h}}{\sin\gamma}$$

**Keystrokes:**
`{{res:sc32_04_trig_vectors_polar_seq_18:keys}}` $\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_18:value}}^\circ}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `18 {{key:COS}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.9511$ | Cosine of angular distance $\cos\gamma$ |
| 2 | `6371 {{key:ENTER}} 6371 {{key:ENTER}} 850 {{key:+}} {{key:÷}} {{key:-}}` | $0.9511$ | $0.9511$ | $0.9511$ | $0.0688$ | Subtract orbital radius ratio $R_E / (R_E + h)$ |
| 3 | `18 {{key:SIN}} {{key:÷}}` | $0.9511$ | $0.9511$ | $0.9511$ | $0.2225$ | Divide by sine $\sin\gamma$ for elevation tangent |
| 4 | `{{key:ATAN}}` | $0.9511$ | $0.9511$ | $0.9511$ | **$12.5462$** | Extract ground satellite elevation angle $E$ (degrees) |

---

### Problem 4.10: AC Circuit Real Power and Power Factor
Voltage $V_{\text{rms}} = 120.0\text{ V}$, current $I_{\text{rms}} = 8.50\text{ A}$, phase angle $\phi = 32.0^\circ$:
$$P = V_{\text{rms}} I_{\text{rms}} \cos\phi \quad [\text{Watts}], \quad Q = V_{\text{rms}} I_{\text{rms}} \sin\phi \quad [\text{VAR}]$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_19:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_19:value}}`**

The polar-to-rectangular decomposition resolves real power $P = \mathbf{865.0097\text{ W}}$ in Register $X$ and reactive power $Q = \mathbf{540.5218\text{ VAR}}$ in Register $Y$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `120 {{key:ENTER}} 8.5 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1020.0000$ | Total apparent electrical power $S = V_{\text{rms}} I_{\text{rms}}$ (VA) |
| 2 | `{{key:ENTER}} {{key:ENTER}} 32 {{key:COS}} {{key:×}}` | $0.0000$ | $0.0000$ | $1020.0000$ | $865.0091$ | Multiply by power factor $\cos(32^\circ)$ for real power $P$ (W) |
| 3 | `{{key:x⇄y}} 32 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $865.0091$ | **$540.5176$** | Multiply by reactive factor $\sin(32^\circ)$ for reactive power $Q$ (VAR) |

---

> **Thematic Arc II — Spatial Vector Algebra, Coordinate Rotations & Phasor Addition (Problems 4.11–4.20):** Using `→P` and `→R` across Registers $X$ and $Y$, these ten problems convert 2D/3D vector projections and force resultants into two-keystroke hardware idioms.

### Problem 4.11: 3D Vector Dot Product and Enclosed Angle
Two strut vectors $\vec{A} = (4.0, 6.0, 8.0\text{ m})$ and $\vec{B} = (2.0, -3.0, 5.0\text{ m})$:
$$\vec{A} \cdot \vec{B} = A_x B_x + A_y B_y + A_z B_z = (4)(2) + (6)(-3) + (8)(5) = 8 - 18 + 40 = 30.0$$
$$|\vec{A}| = \sqrt{16+36+64} = \sqrt{116} \approx 10.7703, \quad |\vec{B}| = \sqrt{4+9+25} = \sqrt{38} \approx 6.1644$$
$$\theta = \arccos\left(\frac{\vec{A} \cdot \vec{B}}{|\vec{A}| |\vec{B}|}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_20:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_20:value}}^\circ}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `30 {{key:ENTER}} 116 {{key:√x}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.7854$ | Normalize dot product by magnitude $\lvert\vec{A}\rvert = \sqrt{116}$ |
| 2 | `38 {{key:√x}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.4519$ | Normalize by magnitude $\lvert\vec{B}\rvert = \sqrt{38}$ for enclosed cosine |
| 3 | `{{key:ACOS}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$63.1371$** | Extract inverse cosine for 3D enclosed angle $\theta$ (degrees) |

---

### Problem 4.12: Torque Vector Cross Product Magnitude
Lever arm $r = 0.850\text{ m}$, applied force $F = 240.0\text{ N}$ at angle $\theta = 65.0^\circ$:
$$\tau = r \cdot F \cdot \sin\theta$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_21:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_21:value}}\text{ N}\cdot\text{m}}$.

Multiply lever arm by force (`0.850 {{key:ENTER}} 240 {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 204.0000$). Multiply by angle sine (`65 {{key:SIN}} {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 184.8868$) to evaluate tightening torque $\tau \approx \mathbf{184.89\text{ N}\cdot\text{m}}$.

---

### Problem 4.13: Double-Slit Optical Interference Fringe Spacing
Slit separation $d = 0.250\text{ mm} = 2.5 \times 10^{-4}\text{ m}$, laser wavelength $\lambda = 632.8\text{ nm} = 6.328 \times 10^{-7}\text{ m}$, screen distance $L = 1.80\text{ m}$. Find fringe spacing $\Delta y$:
$$\Delta y = \frac{\lambda L}{d}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_22:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_22:value}}\text{ mm}}$.

Evaluate optical path numerator $\lambda L$ (`6.328 {{key:E}} 7 {{key:+/-}} {{key:ENTER}} 1.80 {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.1390 \times 10^{-6}$). Divide by slit separation $d = 0.25\text{ mm}$ (`2.5 {{key:E}} 4 {{key:+/-}} {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.0046$). Scale to millimeters (`1000 {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 4.5562$) to find fringe spacing $\Delta y \approx \mathbf{4.56\text{ mm}}$.

---

### Problem 4.14: Inclined Plane Acceleration with Kinetic Friction
Plane inclination $\theta = 34.0^\circ$, kinetic friction coefficient $\mu_k = 0.22$ ($g = 9.80665\text{ m/s}^2$):
$$a = g (\sin\theta - \mu_k \cos\theta)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_23:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_23:value}}\text{ m/s}^2}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `34 {{key:SIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.5592$ | Gravitational downhill acceleration component $\sin(34^\circ)$ |
| 2 | `34 {{key:COS}} 0.22 {{key:×}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.3768$ | Subtract kinetic friction deceleration $\mu_k \cos(34^\circ)$ |
| 3 | `9.80665 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$3.6952$** | Scale by gravity $g$ for net downhill acceleration $a$ ($\text{m/s}^2$) |

---

### Problem 4.15: Vector Sum of Three Concurrent Forces via `{{key:Σ+}}`
Three coplanar cable forces on a gusset plate:
* $F_1 = 50.0\text{ kN}$ at $\theta_1 = 30.0^\circ$
* $F_2 = 75.0\text{ kN}$ at $\theta_2 = 110.0^\circ$
* $F_3 = 60.0\text{ kN}$ at $\theta_3 = 225.0^\circ$

**Keystrokes:**
1. Clear stats: `{{key:CLΣ}}`
2. Vector 1: `30 {{key:ENTER}} 50 {{key:▸y,x}} {{key:Σ+}}`
3. Vector 2: `110 {{key:ENTER}} 75 {{key:▸y,x}} {{key:Σ+}}`
4. Vector 3: `225 {{key:ENTER}} 60 {{key:▸y,x}} {{key:Σ+}}`
5. Recall sums and resolve:
   `{{key:SUMS}}` $\to \Sigma x = -24.7731\text{ kN}$, $\Sigma y = 53.0506\text{ kN}$
   `{{key:x⇄y}} {{key:▸θ,r}}`

Clear statistical registers (`{{key:CLΣ}}`). For Vector 1, push angle and magnitude, resolve into components, and accumulate (`30 {{key:ENTER}} 50 {{key:▸y,x}} {{key:Σ+}}`, $Y = 25.0000\text{ kN}, X = 43.3013\text{ kN}$, $n=1$). For Vector 2, resolve and accumulate (`110 {{key:ENTER}} 75 {{key:▸y,x}} {{key:Σ+}}`, $Y = 70.4769\text{ kN}, X = -25.6515\text{ kN}$, $n=2$). For Vector 3, resolve and accumulate (`225 {{key:ENTER}} 60 {{key:▸y,x}} {{key:Σ+}}`, $Y = -42.4264\text{ kN}, X = -42.4264\text{ kN}$, $n=3$). Recall accumulated coordinate sums (`{{key:SUMS}}`, $\Sigma x = -24.7731\text{ kN}, \Sigma y = 53.0506\text{ kN}$), swap to place vertical component in $Y$, and convert to polar coordinates (`{{key:x⇄y}} {{key:▸θ,r}}`, $T: 0.0000, Z: 0.0000, Y: 115.01^\circ, X: 58.5444\text{ kN}$), delivering resultant magnitude $R = \mathbf{58.54\text{ kN}}$ at bearing $\theta = \mathbf{115.01^\circ}$.

---

### Problem 4.16: Solar Zenith Angle and Air Mass Coefficient
Sun at elevation $\alpha = 42.0^\circ$. Solar zenith angle $\theta_z = 90^\circ - 42^\circ = 48.0^\circ$:
$$\text{Air Mass } AM = \frac{1}{\cos\theta_z}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_24:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_24:value}}} \approx AM\,1.5$.

Evaluate the solar zenith angle cosine (`48 {{key:COS}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.6691$). Take the reciprocal in place (`{{key:1/x}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.4945$) to directly yield the standard optical air mass coefficient $\text{AM} \approx \mathbf{1.49}$ (AM1.5 standard condition).

---

### Problem 4.17: Catenary Hanging Cable Tension at Support Tower
Cable unit weight $w = 12.5\text{ N/m}$, parameter $a = 600.0\text{ m}$, span $L = 400.0\text{ m}$ (half-span $x = 200.0\text{ m}$):
$$T_0 = w \cdot a = 12.5 \times 600 = 7500.0\text{ N}$$
$$T = T_0 \cosh\left(\frac{x}{a}\right) = 7500 \cosh\left(\frac{200}{600}\right) = 7500 \cosh(0.333333)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_25:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_25:value}}\text{ N}} \approx 7.92\text{ kN}$.

Key half-span distance and catenary parameter to form ratio $x/a$ (`200 {{key:ENTER}} 600 {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.3333$). Evaluate the hyperbolic cosine (`{{key:HYP}} {{key:COS}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.0561$). Multiply by horizontal base tension $H = 7,500\text{ N}$ (`7500 {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 7920.5390$) to obtain total tower cable tension $T \approx \mathbf{7,920.54\text{ N}}$ ($7.92\text{ kN}$).

---

### Problem 4.18: Polar Conic Equation for Elliptical Satellite Orbit
Semi-latus rectum $p = 7,200.0\text{ km}$, orbital eccentricity $e = 0.150$. Find orbital radius at true anomaly $\theta = 60.0^\circ$:
$$r = \frac{p}{1 + e \cos\theta}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_26:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_26:value}}\text{ km}}$.

Evaluate the polar orbit denominator term (`60 {{key:COS}} 0.150 {{key:×}} 1 {{key:+}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.0750$). Load semi-latus rectum $p = 7,200\text{ km}$, exchange registers, and divide (`7200 {{key:x⇄y}} {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 6697.6744$) to determine instantaneous orbital radius $r = \mathbf{6,697.67\text{ km}}$.

---

### Problem 4.19: Nautical Waypoint Bearing and Distance
Course from Station A ($x_1=0, y_1=0$) to Station B ($\Delta x = 45.2\text{ nmi}$ East, $\Delta y = 78.5\text{ nmi}$ North):

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_27:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_27:value}}`**

> ***The Inside-Out Radical & Navigation Baseline*** — Square departure and latitude differences on the stack, sum, and take square root without scratchpad memory {{cite:munroe2014,hp15c1982}}.

Load northing delta and easting delta, then perform rectangular-to-polar conversion (`78.5 {{key:ENTER}} 45.2 {{key:▸θ,r}}`, $T: 0.0000, Z: 0.0000, Y: 60.0668^\circ, X: 90.5831\text{ nmi}$). Register $X$ delivers straight-line waypoint distance $r = \mathbf{90.58\text{ nmi}}$, while Register $Y$ yields cartesian angle $60.07^\circ$ (corresponding to nautical true bearing $90^\circ - 60.07^\circ = \mathbf{029.93^\circ}$).

---

### Problem 4.20: Trigonometric Leveling to Inaccessible Mountain Peak
Two observation stations separated by baseline distance $d = 500.0\text{ m}$. Elevation angle to peak from Station 1 is $\alpha = 24.5^\circ$; from Station 2 (closer) is $\beta = 31.2^\circ$:
$$H = \frac{d}{\cot\alpha - \cot\beta} = \frac{d}{\frac{1}{\tan\alpha} - \frac{1}{\tan\beta}}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_28:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_28:value}}\text{ meters}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `24.5 {{key:TAN}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.1943$ | Invert tangent for Station 1 cotangent $\cot(24.5^\circ)$ |
| 2 | `31.2 {{key:TAN}} {{key:1/x}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.5431$ | Subtract Station 2 cotangent $\cot(31.2^\circ)$ for differential $\Delta\cot$ |
| 3 | `500 {{key:x⇄y}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$920.6349$** | Divide baseline distance $d = 500\text{ m}$ for summit height $H$ (m) |

---

> **Thematic Arc III — Nonlinear Oscillators, Wave Optics & Catenary Cables (Problems 4.21–30):** Hyperbolic and inverse circular functions take center stage to model catenary sag, Snell refraction, and large-angle pendulum corrections.

### Problem 4.21: Large-Amplitude Pendulum Period Correction
Small-angle period $T_0 = 2.000\text{ s}$. For initial release angle $\theta_0 = 45.0^\circ$:
$$T \approx T_0 \left(1 + \frac{1}{4} \sin^2\left(\frac{\theta_0}{2}\right)\right) = 2.0 \left(1 + 0.25 \sin^2(22.5^\circ)\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_29:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_29:value}}\text{ seconds}}$.

Evaluate half-angle sine squared (`22.5 {{key:SIN}} {{key:x²}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.1464$). Apply the non-linear elongation coefficient (`0.25 {{key:×}} 1 {{key:+}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.0366$). Scale by harmonic period $T_0 = 2.0\text{ s}$ (`2.0 {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 2.0732$), yielding the true large-amplitude period $T \approx \mathbf{2.0732\text{ s}}$.

---

### Problem 4.22: Circular Arch Chord Length and Segment Arc Length
Circular arch of radius $R = 25.0\text{ m}$ spanning central angle $\theta = 70.0^\circ$:
$$\text{Chord } c = 2 R \sin\left(\frac{\theta}{2}\right), \quad \text{Arc } s = R \frac{\theta \pi}{180}$$

**Keystrokes for Chord:** `{{res:sc32_04_trig_vectors_polar_seq_30:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_30:value}}\text{ m}}$

Compute arch diameter (`25 {{key:ENTER}} 2 {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 50.0000$). Multiply by half-angle sine (`35 {{key:SIN}} {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 28.6788$), resolving chord span $c \approx \mathbf{28.68\text{ m}}$.

---

### Problem 4.23: Brewster's Angle of Polarization
Laser beam incident on crown glass window ($n = 1.520$ in air):
$$\theta_B = \arctan(n)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_32:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_32:value}}^\circ}$.

Enter refractive index and extract the Brewster angle directly in place ($T: 0.0000, Z: 0.0000, Y: 0.0000, X: 56.6593$), yielding $\theta_B \approx \mathbf{56.66^\circ}$.

---

### Problem 4.24: Strain Gauge Rosette 2D Coordinate Rotation
Measured strains $\epsilon_x = 450\,\mu\epsilon$, $\epsilon_y = 120\,\mu\epsilon$, $\gamma_{xy} = 280\,\mu\epsilon$. Rotate coordinate frame by $\theta = 30.0^\circ$:
$$\epsilon_{x'} = \frac{\epsilon_x + \epsilon_y}{2} + \frac{\epsilon_x - \epsilon_y}{2}\cos(2\theta) + \frac{\gamma_{xy}}{2}\sin(2\theta)$$

**Keystrokes:**
`{{res:sc32_04_trig_vectors_polar_seq_33:keys}}` $\longrightarrow$ $\epsilon_{x'} \approx 285 + 82.5 + 121.24 = \mathbf{488.74\,\mu\epsilon}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `450 {{key:ENTER}} 120 {{key:+}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $285.0000$ | Hydrostatic mean strain $(\epsilon_a + \epsilon_c)/2$ |
| 2 | `450 {{key:ENTER}} 120 {{key:-}} 2 {{key:÷}} 60 {{key:COS}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $367.5000$ | Add normal strain cosine transform $((\epsilon_a - \epsilon_c)/2)\cos(60^\circ)$ |
| 3 | `280 {{key:ENTER}} 2 {{key:÷}} 60 {{key:SIN}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$488.7436$** | Add shear strain sine transform $(\gamma_{xy}/2)\sin(60^\circ)$ for rotated strain $\epsilon_{x'}$ ($\mu\epsilon$) |

---

### Problem 4.25: Wave Superposition with Arbitrary Phase Shift
Two sound waves $A_1 = 2.40\text{ Pa}$ and $A_2 = 3.10\text{ Pa}$ interfering with phase difference $\Delta\phi = 55.0^\circ$:
$$A_{\text{resultant}} = \sqrt{A_1^2 + A_2^2 + 2 A_1 A_2 \cos(\Delta\phi)}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_34:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_34:value}}\text{ Pa}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `2.4 {{key:x²}} 3.1 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $15.3700$ | Sum of squared wave amplitudes $A_1^2 + A_2^2$ |
| 2 | `2 {{key:ENTER}} 2.4 {{key:×}} 3.1 {{key:×}} 55 {{key:COS}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $23.9048$ | Add wave interference cross-term $2 A_1 A_2 \cos(\Delta\phi)$ |
| 3 | `{{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$4.8893$** | Extract square root for superposed wave amplitude $A_{\text{res}}$ |

---

### Problem 4.26: Aircraft Coordinated Turn Radius and G-Load
Aircraft turning at $v = 150.0\text{ kts} = 77.1667\text{ m/s}$ at bank angle $\phi = 45.0^\circ$ ($g = 9.80665\text{ m/s}^2$):
$$R = \frac{v^2}{g \tan\phi}, \quad \text{Load Factor } n = \frac{1}{\cos\phi}$$

**Keystrokes for Radius:** `{{res:sc32_04_trig_vectors_polar_seq_35:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_35:value}}\text{ meters}}$

> ***The Inside-Out Radical & Dynamic G-Load Pipeline*** — Invert banking cosine to extract load factor $n = 1/\cos\theta$, and calculate turn radius from velocity and banking angle without scratchpad memory {{cite:munroe2014,hp15c1982}}.

Square true airspeed in $\text{m/s}$ (`77.1667 {{key:x²}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 5954.6996$). Divide by centripetal gravity acceleration $g \tan\phi$ (`9.80665 {{key:ENTER}} 45 {{key:TAN}} {{key:×}} {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 607.2104$) to yield coordinated turn radius $R \approx \mathbf{607.21\text{ m}}$, while load factor $n = 1/\cos(45^\circ) \approx \mathbf{1.41\,G}$ evaluates directly in place.

---

### Problem 4.27: Keplerian Orbit True Anomaly from Eccentric Anomaly
Eccentricity $e = 0.240$, eccentric anomaly $E = 40.0^\circ$:
$$\tan\left(\frac{\nu}{2}\right) = \sqrt{\frac{1 + e}{1 - e}} \tan\left(\frac{E}{2}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_37:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_37:value}}^\circ}$.

***The LASTX Dual-Branch Trick & Half-Angle Tangent Pipeline*** — Compute orbit eccentricity factors $(1+e)$ and $(1-e)$, take square root of their ratio, and scale by half-angle tangent without re-keying {{cite:gauss1809,hp15c1982}}.

Evaluate the eccentricity ratio factor (`1.240 {{key:ENTER}} 0.760 {{key:÷}} {{key:√x}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.2773$). Multiply by the half-angle tangent (`20 {{key:TAN}} {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.4649$). Extract the arctangent and double (`{{key:ATAN}} 2 {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 49.8685$) to obtain Keplerian true anomaly $\nu \approx \mathbf{49.87^\circ}$.

---

### Problem 4.28: Roof Truss Member Forces via Method of Joints
Ridge joint with vertical downward roof load $P = 15.0\text{ kN}$ balanced by two symmetrical rafters inclined at $\theta = 30.0^\circ$ to horizontal:
$$2 F_{\text{rafter}} \sin\theta = P \implies F_{\text{rafter}} = \frac{P}{2 \sin\theta}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_38:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_38:value}}\text{ kN}}$ compression.

Load downward apex joint load $P = 15.0\text{ kN}$ (`15 {{key:ENTER}}`, $T: 0.0000, Z: 0.0000, Y: 15.0000, X: 15.0000$). Divide by vertical resolution factor $2 \sin(30^\circ)$ (`2 {{key:ENTER}} 30 {{key:SIN}} {{key:×}} {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 15.0000$) to obtain rafter compression $F_{\text{rafter}} = \mathbf{15.00\text{ kN}}$.

---

### Problem 4.29: Helical Compression Spring Wahl Stress Factor
Spring index $C = D / d = 7.50$:
$$K_W = \frac{4C - 1}{4C - 4} + \frac{0.615}{C}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_39:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_39:value}}`**

Compute the curvature numerator term for index $C = 7.5$ (`4 {{key:ENTER}} 7.5 {{key:×}} 1 {{key:-}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 29.0000$). Evaluate and divide by denominator $(4C - 4)$ (`4 {{key:ENTER}} 7.5 {{key:×}} 4 {{key:-}} {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.1154$). Add direct shear correction $0.615/C$ (`0.615 {{key:ENTER}} 7.5 {{key:÷}} {{key:+}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.1974$) to establish Wahl stress factor $K_W = \mathbf{1.1974}$.

---

### Problem 4.30: High-Speed Sprint: Continued Trigonometric Product
**Rapid Calculation Sprint:** Rapid evaluation of the expression:
$$x = \frac{\sin(35^\circ) \cos(42^\circ) + \tan(18^\circ)}{\sqrt{\sin^2(65^\circ) + \cos^2(25^\circ)}}$$

**Keystrokes:**
`{{res:sc32_04_trig_vectors_polar_seq_40:keys}}`

**Stack State Inspection:**
1. $\sin(35^\circ)\cos(42^\circ) \approx 0.426297$
2. $\tan(18^\circ) \approx 0.324920$
3. Numerator $\approx 0.751217$
4. $\sin^2(65^\circ) = 0.821394$, $\cos^2(25^\circ) = 0.821394$
5. Denominator $= \sqrt{1.642788} \approx 1.281713$
6. Quotient: $x = \mathbf{0.586104}$.
Solved in 6 seconds with zero parentheses!

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `35 {{key:SIN}} 42 {{key:COS}} {{key:×}} 18 {{key:TAN}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.7512$ | Trigonometric numerator sum $\sin(35^\circ)\cos(42^\circ) + \tan(18^\circ)$ |
| 2 | `65 {{key:SIN}} {{key:x²}} 25 {{key:COS}} {{key:x²}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.7512$ | $1.2817$ | Denominator quadrature $\sqrt{\sin^2(65^\circ) + \cos^2(25^\circ)}$ |
| 3 | `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.5861$** | Divide numerator by denominator for continued trigonometric quotient |

---

### Expedition 4: Geodetic Coordinate Systems & WGS84 Ellipsoidal Surveying (Problems 4.31–4.45)

> **Thematic Arc IV — Celestial Navigation, Spherical Geodesy & Orbital Flight (Problems 4.31–4.45):** The final fifteen problems apply spherical law-of-cosines chains to solar tracking, great-circle navigation, and atmospheric reentry.

### Problem 4.31: Solar Azimuth Angle Calculation
Latitude $\phi = 32.0^\circ\text{ N}$, solar declination $\delta = 18.5^\circ$, solar hour angle $\omega = 45.0^\circ$ ($3\text{ hours}$ before solar noon). Calculate solar elevation angle $\alpha$ and solar azimuth angle $\gamma_s$:
$$\sin\alpha = \sin\phi \sin\delta + \cos\phi \cos\delta \cos\omega$$
$$\cos\gamma_s = \frac{\sin\alpha \sin\phi - \sin\delta}{\cos\alpha \cos\phi}$$

**Keystrokes:**
`{{res:sc32_04_trig_vectors_polar_seq_41:keys}}`

Evaluate the latitude-declination sine product (`32 {{key:SIN}} 18.5 {{key:SIN}} {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.1681$). Compute and add the hour angle cosine product (`32 {{key:COS}} 18.5 {{key:COS}} {{key:×}} 45 {{key:COS}} {{key:×}} {{key:+}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.7368$). Extract the inverse sine (`{{key:ASIN}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 47.4611$) to evaluate solar altitude elevation angle $\alpha \approx \mathbf{47.46^\circ}$.

---

### Problem 4.32: Coriolis Acceleration Vector on Artillery Projectile
Projectile traveling North at $v = 820.0\text{ m/s}$ at latitude $\phi = 42.0^\circ\text{ N}$. Earth's angular rotation rate $\Omega = 7.2921 \times 10^{-5}\text{ rad/s}$:
$$a_{\text{coriolis}} = 2 \cdot v \cdot \Omega \cdot \sin\phi$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_42:keys}}` $\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_42:value}}\text{ m/s}^2}$ Eastward.

Form the kinematic base product $2v$ (`2 {{key:ENTER}} 820 {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1640.0000$). Multiply by planetary angular rotation rate $\Omega$ (`7.2921 {{key:E}} 5 {{key:+/-}} {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.1196$). Scale by latitude sine (`42 {{key:SIN}} {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.0800$) to determine eastward Coriolis acceleration $a_{\text{coriolis}} \approx \mathbf{0.0800\text{ m/s}^2}$.

---

### Problem 4.33: Involute Gear Tooth Base Pitch and Pressure Angle
Module $m = 4.0\text{ mm}$, tooth count $N = 28$, standard pressure angle $\phi = 20.0^\circ$. Calculate pitch circle diameter $D$, base circle diameter $D_b$, and circular base pitch $p_b$:
$$D = m \cdot N, \quad D_b = D \cos\phi, \quad p_b = \pi \cdot m \cos\phi$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_43:keys}}`$\to D = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_43:value}}\text{ mm}}$

Multiply module by tooth count ($T: 0.0000, Z: 0.0000, Y: 0.0000, X: 112.0000$) to obtain gear pitch diameter $D = \mathbf{112.00\text{ mm}}$, with base diameter $D_b = \mathbf{105.25\text{ mm}}$ and base pitch $p_b = \mathbf{11.81\text{ mm}}$ resolving via standard pressure angle cosine scaling.

---

### Problem 4.34: Supersonic Oblique Shock Wave Wave Angle
Supersonic flight at Mach $M_1 = 2.50$ over a compression wedge with deflection angle $\theta = 15.0^\circ$. Determine shock angle $\beta$ (approximate weak shock solution $\beta \approx 36.94^\circ$):
$$\tan\theta = 2 \cot\beta \left[\frac{M_1^2 \sin^2\beta - 1}{M_1^2 (\gamma + \cos(2\beta)) + 2}\right]$$
Verified on the SC-32 stack for $\beta = 36.94^\circ$:
`2.50` `{{key:ENTER}}` `36.94` `{{key:SIN}}` `{{key:×}}` `{{key:x²}}` `1` `{{key:-}}` $\to 1.2530$.

Evaluate normal Mach velocity component for weak shock angle $\beta = 36.94^\circ$ (`2.50 {{key:ENTER}} 36.94 {{key:SIN}} {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.5024$). Square normal Mach and subtract unity (`{{key:x²}} 1 {{key:-}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.2573$) to yield the shock relation numerator delta $1.2573$.

---

### Problem 4.35: Wind Turbine Blade Angle of Attack and Relative Velocity
Blade station radius $r = 32.0\text{ m}$, rotational speed $\Omega = 1.80\text{ rad/s}$ ($u_{\text{rot}} = \Omega r = 57.6\text{ m/s}$), free-stream wind speed $v_{\text{wind}} = 11.5\text{ m/s}$ with axial induction factor $a = 0.30$ ($v_{\text{axial}} = 11.5(1 - 0.30) = 8.05\text{ m/s}$):
$$W_{\text{rel}} = \sqrt{u_{\text{rot}}^2 + v_{\text{axial}}^2}, \quad \phi_{\text{flow}} = \arctan\left(\frac{v_{\text{axial}}}{u_{\text{rot}}}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_44:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_44:value}}`**

***The Inside-Out Radical & Relative Wind Vector Pipeline*** — Vector-sum axial wind speed and blade rotational tip speed in the stack, extracting relative inflow velocity and blade inflow angle in place {{cite:ellenberg2014,hp15c1982}}.

Combine axial wind velocity and blade tip speed into a 2D vector via rectangular-to-polar conversion (`8.05 {{key:ENTER}} 57.6 {{key:▸θ,r}}`, $T: 0.0000, Z: 0.0000, Y: 7.9560^\circ, X: 58.1598\text{ m/s}$), yielding relative inflow velocity $W_{\text{rel}} \approx \mathbf{58.16\text{ m/s}}$ and flow angle $\phi_{\text{flow}} \approx \mathbf{7.96^\circ}$.

---

### Problem 4.36: Surveying Triangulation Intersection from Two Stations
Baseline between Stations $A$ and $B$ is $b = 1,250.0\text{ m}$. Angles observed to unknown landmark $P$: $\angle A = 58.4^\circ$, $\angle B = 71.2^\circ$. Angle at $P$: $\angle P = 180^\circ - (58.4^\circ + 71.2^\circ) = 50.4^\circ$:
$$\text{Distance } AP = b \frac{\sin B}{\sin P} = 1250 \frac{\sin(71.2^\circ)}{\sin(50.4^\circ)}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_45:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_45:value}}\text{ meters}}$.

***The x⇄y Denominator Flip & Surveying Sine Intersection*** — Evaluate the opposing baseline angle sum, divide sine factors via stack swap, and compute target distance with zero scratch registers {{cite:gauss1809,hp15c1982}}.

Scale baseline distance by opposing angle sine (`1250 {{key:ENTER}} 71.2 {{key:SIN}} {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1183.3116$). Divide by landmark opposing angle sine (`50.4 {{key:SIN}} {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1535.7446$) to find landmark distance $AP \approx \mathbf{1,535.74\text{ m}}$.

---

### Problem 4.37: Celestial Coordinate Conversion (RA/Dec to Alt/Az)
Observer at latitude $\phi = 38.0^\circ\text{ N}$. Star with declination $\delta = 22.5^\circ$ and local hour angle $H = 40.0^\circ$:
$$\sin a = \sin\phi \sin\delta + \cos\phi \cos\delta \cos H$$

**Keystrokes:**
`{{res:sc32_04_trig_vectors_polar_seq_46:keys}}`

Compute celestial pole-altitude product (`38 {{key:SIN}} 22.5 {{key:SIN}} {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.2356$). Add the meridian cosine product (`38 {{key:COS}} 22.5 {{key:COS}} {{key:×}} 40 {{key:COS}} {{key:×}} {{key:+}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.7933$). Extract inverse sine (`{{key:ASIN}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 52.4954$) to determine target horizon altitude $a \approx \mathbf{52.50^\circ}$.

---

### Problem 4.38: Gyroscopic Precession Angular Rate
Rotor mass moment of inertia $I_s = 0.0125\text{ kg}\cdot\text{m}^2$, spin speed $\omega_s = 24,000\text{ rpm} = 2513.27\text{ rad/s}$. Applied disturbance torque $\tau = 0.450\text{ N}\cdot\text{m}$:
$$\Omega_p = \frac{\tau}{I_s \cdot \omega_s}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_47:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_47:value}}\text{ rad/s}} = 0.8207^\circ/\text{s}$.

Load disturbance torque (`0.450 {{key:ENTER}}`, $T: 0.0000, Z: 0.0000, Y: 0.4500, X: 0.4500$). Divide by rotor angular momentum $L = I_s \omega_s$ (`0.0125 {{key:ENTER}} 24000 {{key:ENTER}} 2 {{key:×}} {{key:π}} {{key:×}} 60 {{key:÷}} {{key:×}} {{key:÷}}`, $T: 0.4500, Z: 0.4500, Y: 0.4500, X: 0.0143$) to establish gyroscopic precession angular rate $\Omega_p \approx \mathbf{0.0143\text{ rad/s}}$ ($0.82^\circ/\text{s}$).

---

### Problem 4.39: Quarter-Wave Plate Retardance and Jones Matrix
Ellipticity angle $\chi$ produced by linear polarizer at angle $\theta = 22.5^\circ$ through quarter-wave plate:
$$\sin(2\chi) = \sin(2\theta) \sin\delta$$
For a quarter-wave plate ($\delta = 90.0^\circ$), $\sin\delta = 1.0$:
$$\chi = \frac{1}{2} \arcsin(\sin(45^\circ)) = \frac{45^\circ}{2} = \mathbf{22.50^\circ}$$.

Double the incident polarizer angle (`22.5 {{key:ENTER}} 2 {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 45.0000$). Evaluate quarter-wave plate transmission and take arc sine (`{{key:SIN}} {{key:ASIN}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 45.0000$). Halve the resulting angle (`2 {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 22.5000$) to confirm polarization ellipticity angle $\chi = \mathbf{22.50^\circ}$.

---

### Problem 4.40: Acoustic Directivity Index of Circular Piston Speaker
Loudspeaker piston radius $a = 0.10\text{ m}$ radiating at frequency $f = 2,500\text{ Hz}$ in air ($c = 343\text{ m/s}$):
$$k = \frac{2\pi f}{c} = \frac{2\pi(2500)}{343} \approx 45.7958\text{ m}^{-1}$$
$$k a = 45.7958 \times 0.10 = 4.5796$$
Directivity index for $k a \gg 1$:
$$D_I \approx 10 \log_{10}(ka)^2 = 20 \log_{10}(ka)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_48:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_48:value}}\text{ dB}}$.

Enter dimensionless acoustic parameter $k a = 4.5796$, take the common logarithm, and scale by 20 ($T: 0.0000, Z: 0.0000, Y: 0.0000, X: 13.2166$) to yield circular acoustic piston directivity index $D_I \approx \mathbf{13.22\text{ dB}}$.

---

### Problem 4.41: Ballistic Reentry Trajectory Flight Path Angle
Atmospheric entry interface velocity $v_E = 7,800\text{ m/s}$, radial velocity $v_r = -210\text{ m/s}$, tangential speed $v_\theta = \sqrt{7800^2 - 210^2} \approx 7797.17\text{ m/s}$. Find flight path entry angle $\gamma$:
$$\sin\gamma = \frac{v_r}{v_E} \implies \gamma = \arcsin\left(\frac{-210}{7800}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_49:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_49:value}}^\circ}$.

Compute the ratio of radial to total entry velocity (`210 {{key:+/-}} {{key:ENTER}} 7800 {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: -0.0269$). Extract the flight path angle via inverse tangent (`{{key:ATAN}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: -1.5422$) to establish the shallow atmospheric reentry flight path angle $\gamma \approx \mathbf{-1.54^\circ}$.

---

### Problem 4.42: Circular Roadway Curve Sight Distance
Curve radius $R = 250.0\text{ m}$, obstacle setback distance from centerline $m = 8.5\text{ m}$. Calculate available stopping sight distance $S$:
$$m = R \left(1 - \cos\left(\frac{28.65^\circ S}{R}\right)\right) \implies S = \frac{R}{28.65^\circ} \arccos\left(1 - \frac{m}{R}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_50:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_50:value}}\text{ meters}}$.

Compute the sight distance subtended angle argument (`8.5 {{key:ENTER}} 250 {{key:÷}} {{key:+/-}} 1 {{key:+}} {{key:ACOS}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 14.9836$). Scale by curvature radius and conversion constant (`250 {{key:×}} 28.65 {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 130.7467$) to determine highway stopping sight distance $S \approx \mathbf{130.75\text{ m}}$.

---

### Problem 4.43: Resection Surveying Point Fix (Kaestner Method)
Two known landmarks $L_1 (0, 1000)$ and $L_2 (800, 600)$. Measured subtended angle $\alpha = 42.0^\circ$. Baseline length $b$:
$$b = \sqrt{800^2 + (1000 - 600)^2} = \sqrt{640000 + 160000} = \sqrt{800000} = 894.4272\text{ m}$$
Radius of circumscribing position circle:
$$R_{\text{circ}} = \frac{b}{2 \sin\alpha} = \frac{894.4272}{2 \sin(42^\circ)}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_51:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_51:value}}\text{ meters}}$.

Compute the half-baseline distance (`800000 {{key:√x}} 2 {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 447.2136$). Divide by the subtended sine (`42 {{key:SIN}} {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 668.3502$) to evaluate circumscribing position circle radius $R_{\text{circ}} \approx \mathbf{668.35\text{ m}}$.

---

### Problem 4.44: Elliptical Polarization Axial Ratio from Phasors
Major ellipse axis $E_{\max} = 12.4\text{ V/m}$, minor axis $E_{\min} = 4.2\text{ V/m}$. Calculate axial ratio in decibels:
$$\text{AR}_{\text{dB}} = 20 \log_{10}\left(\frac{E_{\max}}{E_{\min}}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_52:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_52:value}}\text{ dB}}$.

Form the semi-axis amplitude ratio (`12.4 {{key:ENTER}} 4.2 {{key:÷}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 2.9524$). Compute common logarithm and multiply by 20 (`{{key:LOG}} 20 {{key:×}}`, $T: 0.0000, Z: 0.0000, Y: 0.0000, X: 9.4034$) to determine the RF polarization axial ratio $\text{AR}_{\text{dB}} \approx \mathbf{9.40\text{ dB}}$.

---

### Problem 4.45: High-Speed Sprint: Radical Trigonometric Nested Pyramid
**Rapid Calculation Sprint:** Solve the multi-layer nested trigonometric pyramid:
$$x = \sqrt{\cos(28^\circ) + \sqrt{\sin(48^\circ) + \sqrt{\tan(15^\circ)}}}$$

**Keystrokes (Inside-Out):** `{{res:sc32_04_trig_vectors_polar_seq_53:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_53:value}}`**

**Stack State Inspection:**
1. $\tan(15^\circ) \approx 0.267949 \implies \sqrt{0.267949} \approx 0.517638$
2. $\sin(48^\circ) \approx 0.743145 \implies 0.743145 + 0.517638 = 1.260783$
3. $\sqrt{1.260783} \approx 1.122846$
4. $\cos(28^\circ) \approx 0.882948 \implies 0.882948 + 1.122846 = 2.005794$
5. $\sqrt{2.005794} = \mathbf{1.416260}$.
Solved in 6 seconds with total spatial clarity!

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `15 {{key:TAN}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.5176$ | Initial square root tangent $\sqrt{\tan(15^\circ)}$ |
| 2 | `48 {{key:SIN}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.1228$ | Add sine term and extract nested root $\sqrt{\sin(48^\circ) + \dots}$ |
| 3 | `28 {{key:COS}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1.4163$** | Add cosine term and extract outer root for nested trigonometric radical |

---

## Summary & Looking Ahead

Chapter 4 united trigonometric functions and 2D spatial vectors on the RPN stack. By bridging the unit circle to the physical register pair $(Y, X)$, you executed direct and inverse trigonometry, explored hyperbolic projections on physical catenaries, and mastered instantaneous polar-to-rectangular conversions (`{{key:▸θ,r}}`, `{{key:▸y,x}}`) with full four-quadrant $\text{atan2}$ sign integrity. Survey traverses, aerodynamic shock angles, and force resolutions unfolded seamlessly with zero scratchpad bookkeeping.

Yet 2D vectors in Cartesian space represent only the gateway to a deeper mathematical realm: the complex plane. In **Chapter 5: Complex Numbers, Phasors & Impedance**, the coordinate pair $(Y, X)$ is reinterpreted as real and imaginary components ($Y + Xi$). You will unleash the `{{key:CMPLX}}` engine to add, multiply, invert, and exponentiate complex numbers in place, verify Euler's identity ($e^{i\pi} + 1 = 0$), and solve multi-branch AC electrical impedance networks without matrix software.
