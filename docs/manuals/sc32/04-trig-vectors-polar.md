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

The SC-32 firmware implements **Exact Axial Angle Clamping** in `RPNCore`:
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
| **Hyperbolic Sine** | `{{keycap:HYP}} {{key:SIN}}` | $\sinh(x) = \frac{e^x - e^{-x}}{2}$ | $(-\infty, +\infty)$ |
| **Hyperbolic Cosine** | `{{keycap:HYP}} {{key:COS}}` | $\cosh(x) = \frac{e^x + e^{-x}}{2}$ | $(-\infty, +\infty)$ |
| **Hyperbolic Tangent** | `{{keycap:HYP}} {{key:TAN}}` | $\tanh(x) = \frac{\sinh(x)}{\cosh(x)}$ | $(-\infty, +\infty)$ |
| **Inverse Sinh** | `{{keycap:HYP}} {{key:ASIN}}` | $\operatorname{arsinh}(x) = \ln\left(x + \sqrt{x^2 + 1}\right)$ | $(-\infty, +\infty)$ |
| **Inverse Cosh** | `{{keycap:HYP}} {{key:ACOS}}` | $\operatorname{arcosh}(x) = \ln\left(x + \sqrt{x^2 - 1}\right)$ | $x \ge 1.0$ |
| **Inverse Tanh** | `{{keycap:HYP}} {{key:ATAN}}` | $\operatorname{artanh}(x) = \frac{1}{2}\ln\left(\frac{1+x}{1-x}\right)$ | $|x| < 1.0$ |

### Grounded Application 1: Catenary Transmission Line Cable Sag
A high-voltage transmission cable spans $L = 200\text{ meters}$ between two steel towers. The catenary curve parameter is $a = 800\text{ meters}$ ($a = T_0 / w$, where $T_0$ is horizontal cable tension and $w$ is unit weight).
Calculate cable sag $y$ at midpoint $x = 100\text{ meters}$:
$$y = a \left(\cosh\left(\frac{x}{a}\right) - 1\right) = 800 \left(\cosh\left(\frac{100}{800}\right) - 1\right) = 800 \times (\cosh(0.125) - 1)$$

Keystrokes: `{{res:sc32_04_trig_vectors_polar_seq_01:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_01:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `100 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $100.0000$ | $100.0000$ | Cable half-span $x$ pushed |
| 2 | `800 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.1250$ | Non-dimensional ratio $x/a$ |
| 3 | `{{keycap:HYP}} {{key:COS}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.007822967$ | $\cosh(0.125)$ evaluated |
| 4 | `1 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.007822967$ | Dimensionless sag factor |
| 5 | `800 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$6.258373678\text{ m}$** | Midpoint cable sag |

The transmission line experiences a midpoint sag of **$6.26\text{ meters}$**.

---

### Grounded Application 2: Relativistic Velocity Addition
In Einstein's Special Theory of Relativity, velocities do not add linearly. Instead, velocity parameterizes via **rapidity** $\theta = \operatorname{atanh}(v/c)$. When two reference frames move with relative velocities $v_1$ and $v_2$, their rapidities add directly:
$$\theta_{\text{total}} = \theta_1 + \theta_2 \implies v_{\text{total}} = c \tanh\left(\operatorname{atanh}\left(\frac{v_1}{c}\right) + \operatorname{atanh}\left(\frac{v_2}{c}\right)\right)$$

An interstellar probe travels at $v_1 = 0.75c$ relative to Earth, and launches a scout missile forward at $v_2 = 0.60c$ relative to the probe. Determine the missile's speed relative to Earth in units of $c$:

Keystrokes: `{{res:sc32_04_trig_vectors_polar_seq_02:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_02:value}}`**

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `0.75 {{key:HYP}} {{key:ATAN}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.9730$ | Rapidity $\theta_1 = \operatorname{atanh}(0.75)$ |
| 2 | `0.60 {{key:HYP}} {{key:ATAN}}` | $0.0000$ | $0.0000$ | $0.9730$ | $0.6931$ | Rapidity $\theta_2 = \operatorname{atanh}(0.60)$ |
| 3 | `{{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.6661$ | Combined rapidity $\theta_{\text{total}}$ |
| 4 | `{{key:HYP}} {{key:TAN}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.9310$** | Relativistic velocity $v_{\text{total}} / c$ |

The missile travels at **$0.931c$** ($93.1\%$ the speed of light), strictly preserving the cosmic speed limit ($v < c$).

---

## 2D Coordinate Transformations: Polar $\leftrightarrow$ Rectangular

The SC-32 provides two-way conversions between Cartesian rectangular coordinates $(x, y)$ and polar vector coordinates $(r, \theta)$:

| Transformation | Dedicated Keystroke | Stack Input ($Y, X$) | Stack Output ($Y, X$) | Mathematical Formula |
| :--- | :--- | :--- | :--- | :--- |
| **Polar to Rectangular** | `{{key:▸y,x}}` | $Y = \theta$ (Angle in active mode)<br>$X = r$ (Radius / Magnitude) | $Y = y = r \sin\theta$<br>$X = x = r \cos\theta$ | $(x, y) = (r\cos\theta, r\sin\theta)$ |
| **Rectangular to Polar** | `{{key:▸θ,r}}` | $Y = y$ (Orthogonal vertical)<br>$X = x$ (Orthogonal horizontal) | $Y = \theta = \operatorname{atan2}(y, x)$<br>$X = r = \sqrt{x^2 + y^2}$ | $(r, \theta) = (\sqrt{x^2+y^2}, \operatorname{atan2}(y, x))$ |

{{res:sc32_phasor_mag:screenshot|Impedance phasor 3 + j4 rectangular-to-polar conversion -> r = 5, theta = 53.1301 deg}}
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
* $X = 22.4976\text{ kts}$ (East wind component)

#### Step 3: Vector Summation & Polar Conversion
1. Add East components: `{{key:RCL}} 1 {{key:+}}` $\rightarrow$ $X = 178.0611\text{ kts}$ (Total East velocity)
2. Add North components: `{{key:x⇄y}} {{key:RCL}} 2 {{key:+}}` $\rightarrow$ $X = 182.3751\text{ kts}$ (Total North velocity)
3. Convert back to polar vector:
   `{{key:x⇄y}}` (puts North $y$ in $Y$, East $x$ in $X$) `{{key:▸θ,r}}`
   * **Register X (Ground Speed):** **$254.89\text{ knots}$**
   * **Register Y (Ground Track Angle):** **$45.69^\circ$**

The aircraft makes good a ground speed of **$254.9\text{ knots}$** on a track of **$045.7^\circ$**.

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

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `60 {{key:ENTER}} 100` | $0.0000$ | $0.0000$ | $60.0000$ | $100.0000$ | $\theta$ in $Y$, $r$ in $X$ |
| 2 | `{{key:▸y,x}}` | $0.0000$ | $0.0000$ | **$86.602540$** | **$50.000000$** | $\Delta y = 86.60\text{ m}, \Delta x = 50.00\text{ m}$ |
| 3 | `{{key:Σ+}}` | $0.0000$ | $0.0000$ | $86.602540$ | **$1.0$** | Coordinate accumulated ($n=1$) |

#### Leg 2: $\theta = 150^\circ, r = 80\text{ m}$
Keystrokes: `{{res:sc32_04_trig_vectors_polar_seq_06:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_06:value}}`**

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `150 {{key:ENTER}} 80` | $0.0000$ | $0.0000$ | $150.0000$ | $80.0000$ | $\theta$ in $Y$, $r$ in $X$ |
| 2 | `{{key:▸y,x}}` | $0.0000$ | $0.0000$ | **$40.000000$** | **$-69.282032$** | $\Delta y = 40.00\text{ m}, \Delta x = -69.28\text{ m}$ |
| 3 | `{{key:Σ+}}` | $0.0000$ | $0.0000$ | $40.000000$ | **$1.0$** | Coordinate accumulated ($n=2$) |

* Output: $\Delta y = 40.0000\text{ m}$, $\Delta x = -69.2820\text{ m}$, $n = 2$.

#### Leg 3: $\theta = 240^\circ, r = 100\text{ m}$
Keystrokes: `{{res:sc32_04_trig_vectors_polar_seq_07:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_07:value}}`**

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `240 {{key:ENTER}} 100` | $0.0000$ | $0.0000$ | $240.0000$ | $100.0000$ | $\theta$ in $Y$, $r$ in $X$ |
| 2 | `{{key:▸y,x}}` | $0.0000$ | $0.0000$ | **$-86.602540$** | **$-50.000000$** | $\Delta y = -86.60\text{ m}, \Delta x = -50.00\text{ m}$ |
| 3 | `{{key:Σ+}}` | $0.0000$ | $0.0000$ | $-86.602540$ | **$1.0$** | Coordinate accumulated ($n=3$) |

* Output: $\Delta y = -86.6025\text{ m}$, $\Delta x = -50.0000\text{ m}$, $n = 3$.

#### Leg 4: $\theta = 330^\circ, r = 80\text{ m}$
Keystrokes: `{{res:sc32_04_trig_vectors_polar_seq_08:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_08:value}}`**

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `330 {{key:ENTER}} 80` | $0.0000$ | $0.0000$ | $330.0000$ | $80.0000$ | $\theta$ in $Y$, $r$ in $X$ |
| 2 | `{{key:▸y,x}}` | $0.0000$ | $0.0000$ | **$-40.000000$** | **$69.282032$** | $\Delta y = -40.00\text{ m}, \Delta x = 69.28\text{ m}$ |
| 3 | `{{key:Σ+}}` | $0.0000$ | $0.0000$ | $-40.000000$ | **$1.0$** | Coordinate accumulated ($n=4$) |

* Output: $\Delta y = -40.0000\text{ m}$, $\Delta x = 69.2820\text{ m}$, $n = 4$.

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

## Engineering Design Briefing: Autonomous Geodetic Navigation & Trans-Oceanic Surveying (Problems 4.1 through 4.30)

> **Hands-On Studio Proof: Blocks &rarr; Calculator**  
> Before computing numerical bearings and spherical trigonometry on the SC-32, manipulate physical angle wedges on the Unit Circle Volvelle (`docs/assets/renders/unit-circle-volvelle-hero.png`) and dial in bearings manually (`docs/assets/renders/volvelle-interaction-01.jpg`). Physically rotating through compass quadrants grounds the $(Y, X)$ stack allocation conventions and eliminates sign errors during open-ocean dead reckoning.

The following 30 professional engineering case studies span geodetic traverses, aerospace wind triangle corrections, solar elevation ephemerides, and RF antenna phase synthesis.

---

### Problem 4.1: Projectile Trajectory Maximum Height and Range
**Ballistics Context:** An artillery shell is fired with muzzle velocity $v_0 = 85.0\text{ m/s}$ at elevation angle $\theta = 38.0^\circ$ ($g = 9.80665\text{ m/s}^2$):
$$H_{\max} = \frac{(v_0 \sin\theta)^2}{2g}, \quad R = \frac{v_0^2 \sin(2\theta)}{g}$$

**Keystrokes for $H_{\max}$:** `{{res:sc32_04_trig_vectors_polar_seq_09:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_09:value}}`**
**Keystrokes for Range $R$:** `{{res:sc32_04_trig_vectors_polar_seq_10:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_10:value}}`**

**4-Level Stack Trace ($H_{\max}$):**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `85` `{{key:ENTER}}` `38` `{{key:SIN}}` `{{key:×}}`| $0.0000$ | $0.0000$ | $85.0000$ | $52.3312$ | Vertical velocity component $v_{0y}$ |
| `{{keycap:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2,738.5574$ | $v_{0y}^2$ numerator |
| `2` `{{key:ENTER}}` `9.80665` `{{key:×}}` | $0.0000$ | $2738.5574$ | $2.0000$ | $19.6133$ | Denominator $2g$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$139.6275\text{ m}$** | Peak height $H_{\max}$ |

Range evaluation yields: $R = \mathbf{714.4756\text{ m}}$.

---

### Problem 4.2: Oblique Triangle Solution via Law of Cosines
**Surveying Context:** A triangular boundary survey measures sides $a = 45.0\text{ m}$, $b = 62.0\text{ m}$, and included angle $C = 48.0^\circ$. Find opposing side $c$:
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
**Geometry Context:** In triangle with $a = 45.0\text{ m}$, $b = 62.0\text{ m}$, angle $A = 32.5^\circ$. Find angle $B$:
$$\frac{\sin B}{b} = \frac{\sin A}{a} \implies B = \arcsin\left(\frac{b \sin A}{a}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_12:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_12:value}}^\circ}$.

> **Named RPN Stack Idiom: *The LASTX Dual-Branch Trick & Sine Projection*** — Scale side length by opposite angle sine, divide by adjacent side, and apply arcsine in place without scratchpad memory {{cite:hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `62` `{{key:SIN}}` — Enter base elevation angle ($B = 62.0^\circ$) into $X$ and evaluate sine in place ($\sin(62^\circ) \approx 0.88295$).
2. `37.73` `{{key:×}}` — Scale by opposing side length ($b = 37.73\text{ m}$); oblique triangle sine numerator ($33.3126\text{ m}$) condenses in $X$.
3. `45.0` `{{key:÷}}` — Key reference side length ($a = 45.0\text{ m}$) and divide; target sine value ($\sin A \approx 0.74028$) forms in $X$.
4. `{{key:ASIN}}` — Extract arcsine in place; interior vertex angle ($A = 47.76^\circ$) evaluates without grouping overhead.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `62 {{key:ENTER}} 32.5 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $33.3126$ | Oblique sine projection $b \sin A$ |
| 2 | `45 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.7403$ | Divide by side $a$ for sine ratio $\sin B$ |
| 3 | `{{key:ASIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$47.7552$** | Extract arcsine for interior vertex angle $B$ (degrees) |

---

### Problem 4.4: Static Equilibrium of Crane Boom and Cable
**Structural Statics Context:** Crane boom weight $W = 28.0\text{ kN}$ at angle $\theta = 35.0^\circ$ from horizontal, supported by tie cable at angle $\phi = 25.0^\circ$ to boom. Cable tension:
$$T = \frac{W \cos\theta}{\sin\phi} = \frac{28.0 \cos(35^\circ)}{\sin(25^\circ)}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_13:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_13:value}}\text{ kN}}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `28` `{{key:ENTER}}` — Load suspended payload weight ($W = 28.0\text{ kN}$) into $Y$.
2. `35` `{{key:COS}}` `{{key:×}}` — Key boom inclination angle ($35.0^\circ$) and evaluate cosine; horizontal static moment component ($22.9363\text{ kN}$) forms in $X$.
3. `50` `{{key:SIN}}` `{{key:÷}}` — Key cable tieback angle ($50.0^\circ$), evaluate sine in place, and divide directly; tension in guy cable ($T = 29.94\text{ kN}$) resolves without intermediate registers.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `28 {{key:ENTER}} 35 {{key:COS}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $22.9363$ | Horizontal boom load component $W \cos\theta$ (kN) |
| 2 | `25 {{key:SIN}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$54.2718$** | Divide by cable angle sine $\sin\phi$ for cable tension $T$ (kN) |

---

### Problem 4.5: Snell's Law of Optical Refraction
**Optics Context:** Light ray incident from air ($n_1 = 1.000$) into dense flint glass ($n_2 = 1.660$) at incidence angle $\theta_1 = 55.0^\circ$. Find refracted angle $\theta_2$:
$$\sin\theta_2 = \frac{n_1 \sin\theta_1}{n_2} \implies \theta_2 = \arcsin\left(\frac{\sin(55^\circ)}{1.660}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_14:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_14:value}}^\circ}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `55` `{{key:SIN}}` — Compute incident angle sine ($\sin 55.0^\circ \approx 0.819152$) in place.
2. `1.660` `{{key:÷}}` — Divide by flint glass refractive index ($n_2 = 1.660$); refracted sine ($\sin\theta_2 \approx 0.493465$) appears in $X$.
3. `{{key:ASIN}}` — Extract inverse sine in place; refracted ray angle ($\theta_2 \approx \mathbf{29.57^\circ}$) is evaluated directly.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `55 {{key:SIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.8192$ | Incident ray angle sine $\sin\theta_1$ |
| 2 | `1.660 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.4935$ | Divide by flint glass index $n_2$ for refracted sine |
| 3 | `{{key:ASIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$29.5686$** | Extract inverse sine for refracted ray angle $\theta_2$ (degrees) |

---

### Problem 4.6: Critical Angle for Total Internal Reflection
**Photonics Context:** Fiber optic core ($n_1 = 1.480$) and cladding ($n_2 = 1.450$). Find critical angle $\theta_c$:
$$\theta_c = \arcsin\left(\frac{n_2}{n_1}\right) = \arcsin\left(\frac{1.450}{1.480}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_15:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_15:value}}^\circ}$.

> **Named RPN Stack Idiom: *The x⇄y Denominator Flip & Snell Inversion*** — Divide refractive indices via stack swap and take arcsine in place without intermediate scratch registers {{cite:horowitz2015,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `1.000` `{{key:ENTER}}` — Load ambient air refractive index ($n_2 = 1.000$) into $Y$.
2. `1.460` `{{key:÷}}` — Enter optical fiber silica core index ($n_1 = 1.460$) and divide; critical boundary refraction ratio ($n_2/n_1 = 0.68493$) forms in $X$.
3. `{{key:ASIN}}` — Compute inverse sine in place; total internal reflection critical angle ($\theta_c = 43.23^\circ$) is determined directly.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `1.450 {{key:ENTER}} 1.480 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.9797$ | Core/cladding refractive index ratio $n_2/n_1$ |
| 2 | `{{key:ASIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$78.4441$** | Extract critical angle $\theta_c$ for total internal reflection (degrees) |

---

### Problem 4.7: Highway Super-Elevation Banking Angle
**Transportation Engineering Context:** Highway curve radius $R = 350.0\text{ m}$ designed for speed $v = 100.0\text{ km/h} = 27.7778\text{ m/s}$ with zero lateral friction ($g = 9.80665\text{ m/s}^2$):
$$\tan\theta = \frac{v^2}{g R} \implies \theta = \arctan\left(\frac{v^2}{g R}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_16:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_16:value}}^\circ}$.

> **Named RPN Stack Idiom: *The Constant-in-T Pipeline & Centripetal Balance*** — Convert highway design speed to SI velocity, square in place, and divide by gravitational centripetal product $g R$ {{cite:ellenberg2014,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `110` `{{key:ENTER}}` — Key highway cruise speed ($110.0\text{ km/h}$) into $Y$.
2. `3.6` `{{key:÷}}` — Divide by metric velocity conversion factor ($3.6\text{ km/h per m/s}$); SI speed ($v = 30.5556\text{ m/s}$) condenses in $X$.
3. `{{key:x²}}` — Square velocity in place ($v^2 = 933.6420\text{ m}^2/\text{s}^2$); stack lift lifts numerator to $Y$ automatically.
4. `450` `{{key:ENTER}}` `9.80665` `{{key:×}}` — Evaluate radial gravitational denominator ($g R = 4412.99\text{ m}^2/\text{s}^2$) in place.
5. `{{key:÷}}` — Divide velocity squared by gravitational denominator; required super-elevation tangent ratio ($\tan\theta = 0.211566$) appears in $X$.
6. `{{key:ATAN}}` — Take arctangent in place; roadway banking angle ($\theta = 11.95^\circ$) evaluates without grouping syntax.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `100 {{key:ENTER}} 3.6 {{key:÷}} {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $771.6049$ | Square speed in m/s $(v/3.6)^2$ |
| 2 | `9.80665 {{key:ENTER}} 350 {{key:×}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.2248$ | Divide by centripetal gravity denominator $g R$ |
| 3 | `{{key:ATAN}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$12.6698$** | Extract arctangent for banking angle $\theta$ (degrees) |

---

### Problem 4.8: Traverse Linear Misclosure Precision Ratio
**Civil Geodesy Context:** A traverse boundary has total perimeter $P = 1,450.0\text{ m}$. Sum of departures $\Sigma x = +0.038\text{ m}$, sum of latitudes $\Sigma y = -0.024\text{ m}$. Calculate closure precision $1:K$:
$$\text{Misclosure} = \sqrt{(\Sigma x)^2 + (\Sigma y)^2}, \quad K = \frac{P}{\text{Misclosure}}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_17:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_17:value}}`**

**Stack State Inspection:**
1. Misclosure $= \sqrt{0.001444 + 0.000576} = \sqrt{0.002020} = 0.044944\text{ m}$ ($4.5\text{ cm}$)
2. Ratio $K = 1450 / 0.044944 = \mathbf{32,262}$.
Precision rating: **$1:32,000$** (First-order geodetic survey standard).

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `0.038 {{key:x²}} 0.024 {{key:x²}} {{key:+}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0449$ | Linear traverse misclosure $\sqrt{\Sigma x^2 + \Sigma y^2}$ (m) |
| 2 | `1450 {{key:x⇄y}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$32262.0766$** | Divide perimeter $P = 1450\text{ m}$ by misclosure for precision ratio $1:K$ |

---

### Problem 4.9: Ground Satellite Elevation Angle
**Satellite Communications Context:** Earth radius $R_E = 6,371\text{ km}$, satellite orbital altitude $h = 850\text{ km}$, angular distance from sub-satellite point $\gamma = 18.0^\circ$:
$$\tan E = \frac{\cos\gamma - \frac{R_E}{R_E + h}}{\sin\gamma}$$

**Keystrokes:**
`{{res:sc32_04_trig_vectors_polar_seq_18:keys}}` $\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_18:value}}^\circ}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `42164` `{{key:ENTER}}` — Enter geostationary orbit radius ($r = 42,164\text{ km}$) into $Y$.
2. `38` `{{key:COS}}` `{{key:×}}` — Key ground station latitude angle ($38.0^\circ$) and evaluate cosine; projected orbital coordinate ($33,225.75\text{ km}$) forms in $X$.
3. `6378` `{{key:-}}` — Enter mean Earth radius ($R_E = 6378\text{ km}$) and subtract; horizontal topocentric baseline ($26,847.75\text{ km}$) condenses in $X$.
4. `42164` `{{key:ENTER}}` `38` `{{key:SIN}}` `{{key:×}}` — Evaluate vertical coordinate ($42164 \sin(38^\circ) = 25,959.08\text{ km}$) in place.
5. `{{key:x⇄y}}` `{{key:÷}}` — Swap to place vertical over horizontal baseline and divide; elevation tangent ratio ($0.966899$) occupies $X$.
6. `{{key:ATAN}}` — Take arctangent in place; ground satellite dish elevation angle ($\theta = 44.04^\circ$) is obtained directly.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `18 {{key:COS}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.9511$ | Cosine of angular distance $\cos\gamma$ |
| 2 | `6371 {{key:ENTER}} 6371 {{key:ENTER}} 850 {{key:+}} {{key:÷}} {{key:-}}` | $0.9511$ | $0.9511$ | $0.9511$ | $0.0688$ | Subtract orbital radius ratio $R_E / (R_E + h)$ |
| 3 | `18 {{key:SIN}} {{key:÷}}` | $0.9511$ | $0.9511$ | $0.9511$ | $0.2225$ | Divide by sine $\sin\gamma$ for elevation tangent |
| 4 | `{{key:ATAN}}` | $0.9511$ | $0.9511$ | $0.9511$ | **$12.5462$** | Extract ground satellite elevation angle $E$ (degrees) |

---

### Problem 4.10: AC Circuit Real Power and Power Factor
**Electrical Engineering Context:** Voltage $V_{\text{rms}} = 120.0\text{ V}$, current $I_{\text{rms}} = 8.50\text{ A}$, phase angle $\phi = 32.0^\circ$:
$$P = V_{\text{rms}} I_{\text{rms}} \cos\phi \quad [\text{Watts}], \quad Q = V_{\text{rms}} I_{\text{rms}} \sin\phi \quad [\text{VAR}]$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_19:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_19:value}}`**

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `120` `{{key:ENTER}}` — Load RMS supply voltage ($V_{\text{rms}} = 120.0\text{ V}$) into $Y$.
2. `8.5` `{{key:×}}` — Enter load current ($I_{\text{rms}} = 8.50\text{ A}$) and multiply; total apparent electrical power ($S = 1020.0\text{ VA}$) forms in $X$.
3. `28` `{{key:COS}}` `{{key:×}}` — Enter AC current lag phase angle ($\phi = 28.0^\circ$), evaluate power factor ($\cos(28^\circ) \approx 0.88295$), and multiply; true active electrical power ($P = 900.61\text{ W}$) is evaluated with zero auxiliary memory.

Stack: Real power $P = \mathbf{865.0097\text{ W}}$, Reactive power $Q = \mathbf{540.5218\text{ VAR}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `120 {{key:ENTER}} 8.5 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1020.0000$ | Total apparent electrical power $S = V_{\text{rms}} I_{\text{rms}}$ (VA) |
| 2 | `{{key:ENTER}} {{key:ENTER}} 32 {{key:COS}} {{key:×}}` | $0.0000$ | $0.0000$ | $1020.0000$ | $865.0091$ | Multiply by power factor $\cos(32^\circ)$ for real power $P$ (W) |
| 3 | `{{key:x⇄y}} 32 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $865.0091$ | **$540.5176$** | Multiply by reactive factor $\sin(32^\circ)$ for reactive power $Q$ (VAR) |

---

### Problem 4.11: 3D Vector Dot Product and Enclosed Angle
**Vector Mechanics Context:** Two strut vectors $\vec{A} = (4.0, 6.0, 8.0\text{ m})$ and $\vec{B} = (2.0, -3.0, 5.0\text{ m})$:
$$\vec{A} \cdot \vec{B} = A_x B_x + A_y B_y + A_z B_z = (4)(2) + (6)(-3) + (8)(5) = 8 - 18 + 40 = 30.0$$
$$|\vec{A}| = \sqrt{16+36+64} = \sqrt{116} \approx 10.7703, \quad |\vec{B}| = \sqrt{4+9+25} = \sqrt{38} \approx 6.1644$$
$$\theta = \arccos\left(\frac{\vec{A} \cdot \vec{B}}{|\vec{A}| |\vec{B}|}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_20:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_20:value}}^\circ}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `30 {{key:ENTER}} 116 {{key:√x}} {{key:÷}}` — Load dot product $\vec{A} \cdot \vec{B} = 30.0$ into Register $Y$ and divide by vector magnitude $|\vec{A}| = \sqrt{116} \approx 10.7703$.
2. `38 {{key:√x}} {{key:÷}}` — Divide by opposing vector magnitude $|\vec{B}| = \sqrt{38} \approx 6.1644$ to evaluate directional cosine $\cos\theta \approx 0.4518$.
3. `{{key:ACOS}}` — Extract inverse cosine in place to obtain enclosed spatial strut angle $\theta \approx \mathbf{63.15^\circ}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `30 {{key:ENTER}} 116 {{key:√x}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.7854$ | Normalize dot product by magnitude $|\vec{A}| = \sqrt{116}$ |
| 2 | `38 {{key:√x}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.4519$ | Normalize by magnitude $|\vec{B}| = \sqrt{38}$ for enclosed cosine |
| 3 | `{{key:ACOS}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$63.1371$** | Extract inverse cosine for 3D enclosed angle $\theta$ (degrees) |

---

### Problem 4.12: Torque Vector Cross Product Magnitude
**Mechanical Physics Context:** Lever arm $r = 0.850\text{ m}$, applied force $F = 240.0\text{ N}$ at angle $\theta = 65.0^\circ$:
$$\tau = r \cdot F \cdot \sin\theta$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_21:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_21:value}}\text{ N}\cdot\text{m}}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `0.45` `{{key:ENTER}}` — Enter torque wrench moment lever arm ($r = 0.45\text{ m}$) into $Y$.
2. `185` `{{key:×}}` — Enter applied technician hand force ($F = 185.0\text{ N}$) and multiply; maximum torque product ($83.25\text{ N}\cdot\text{m}$) forms in $X$.
3. `65` `{{key:SIN}}` `{{key:×}}` — Key application angle ($\theta = 65.0^\circ$), evaluate sine in place ($\sin(65^\circ) \approx 0.90631$), and multiply; effective tightening torque ($\tau = 75.45\text{ N}\cdot\text{m}$) is evaluated directly.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `0.850 {{key:ENTER}} 240 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $204.0000$ | Cross product scalar base $r F$ ($0.850\text{ m} \times 240\text{ N}$) |
| 2 | `65 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$184.8868$** | Multiply by sine of angle $\sin(65^\circ)$ for torque magnitude $\tau$ ($\text{N}\cdot\text{m}$) |

---

### Problem 4.13: Double-Slit Optical Interference Fringe Spacing
**Wave Optics Context:** Slit separation $d = 0.250\text{ mm} = 2.5 \times 10^{-4}\text{ m}$, laser wavelength $\lambda = 632.8\text{ nm} = 6.328 \times 10^{-7}\text{ m}$, screen distance $L = 1.80\text{ m}$. Find fringe spacing $\Delta y$:
$$\Delta y = \frac{\lambda L}{d}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_22:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_22:value}}\text{ mm}}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `632.8 {{key:E}} 9 {{key:+/-}}` `{{key:ENTER}}` — Load He-Ne laser emission wavelength ($\lambda = 632.8\text{ nm} = 6.328 \times 10^{-7}\text{ m}$) into $Y$.
2. `1.85` `{{key:×}}` — Enter screen viewing distance ($L = 1.85\text{ m}$) and multiply; optical interference numerator ($1.17068 \times 10^{-6}\text{ m}^2$) forms in $X$.
3. `0.00025` `{{key:÷}}` — Enter double-slit aperture spacing ($d = 0.25\text{ mm} = 2.5 \times 10^{-4}\text{ m}$) and divide directly; optical interference fringe width ($\Delta y = 4.6827 \times 10^{-3}\text{ m} = 4.68\text{ mm}$) evaluates without parenthesis overhead.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `6.328 {{key:E}} 7 {{key:+/-}} {{key:ENTER}} 1.80 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.1390 \times 10^{-6}$ | Optical path numerator $\lambda L$ ($632.8\text{ nm} \times 1.80\text{ m}$) |
| 2 | `2.5 {{key:E}} 4 {{key:+/-}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0046$ | Divide by slit separation $d = 0.25\text{ mm}$ for fringe spacing (m) |
| 3 | `1000 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$4.5562$** | Convert fringe separation $\Delta y$ to millimeters (mm) |

---

### Problem 4.14: Inclined Plane Acceleration with Kinetic Friction
**Classical Mechanics Context:** Plane inclination $\theta = 34.0^\circ$, kinetic friction coefficient $\mu_k = 0.22$ ($g = 9.80665\text{ m/s}^2$):
$$a = g (\sin\theta - \mu_k \cos\theta)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_23:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_23:value}}\text{ m/s}^2}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `34` `{{key:SIN}}` — Compute downhill gravitational slope sine ($\sin 34.0^\circ \approx 0.559193$) in $X$.
2. `34` `{{key:COS}}` `0.22` `{{key:×}}` — Compute normal cosine ($\cos 34.0^\circ \approx 0.829038$) and scale by kinetic friction coefficient ($\mu_k = 0.22$); friction resistance factor ($0.182388$) forms in $X$ while slope sine waits in $Y$.
3. `{{key:-}}` — Subtract friction drag from gravity component; net normalized acceleration factor ($0.376804$) forms in $X$.
4. `9.80665` `{{key:×}}` — Multiply by gravitational acceleration ($g = 9.80665\text{ m/s}^2$); net sled downhill acceleration ($a \approx \mathbf{3.6952\text{ m/s}^2}$) is determined directly.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `34 {{key:SIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.5592$ | Gravitational downhill acceleration component $\sin(34^\circ)$ |
| 2 | `34 {{key:COS}} 0.22 {{key:×}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.3768$ | Subtract kinetic friction deceleration $\mu_k \cos(34^\circ)$ |
| 3 | `9.80665 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$3.6952$** | Scale by gravity $g$ for net downhill acceleration $a$ ($\text{m/s}^2$) |

---

### Problem 4.15: Vector Sum of Three Concurrent Forces via `{{key:Σ+}}`
**Civil Statics Context:** Three coplanar cable forces on a gusset plate:
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
Stack: Resultant magnitude $R = \mathbf{58.5444\text{ kN}}$, Angle $\theta = \mathbf{115.01^\circ}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `30 {{key:ENTER}} 50 {{key:▸y,x}}` | $0.0000$ | $0.0000$ | $25.0000$ | $43.3013$ | Vector 1: Resolve $F_1 = 50\text{ kN}$ at $30^\circ$ into $(y_1, x_1)$ |
| 2 | `110 {{key:ENTER}} 75 {{key:▸y,x}}` | $25.0000$ | $43.3013$ | $70.4769$ | $-25.6515$ | Vector 2: Resolve $F_2 = 75\text{ kN}$ at $110^\circ$ into $(y_2, x_2)$ |
| 3 | `225 {{key:ENTER}} 60 {{key:▸y,x}}` | $70.4769$ | $-25.6515$ | $-42.4264$ | $-42.4264$ | Vector 3: Resolve $F_3 = 60\text{ kN}$ at $225^\circ$ into $(y_3, x_3)$ |
| 4 | `53.0506 {{key:ENTER}} 24.7731 {{key:+/-}} {{key:▸θ,r}}` | $-42.4264$ | $-42.4264$ | $115.0312$ | **$58.5497$** | Accumulated sums $(\Sigma y, \Sigma x)$ converted to polar resultant $(R, \theta)$ |

---

### Problem 4.16: Solar Zenith Angle and Air Mass Coefficient
**Solar Engineering Context:** Sun at elevation $\alpha = 42.0^\circ$. Solar zenith angle $\theta_z = 90^\circ - 42^\circ = 48.0^\circ$:
$$\text{Air Mass } AM = \frac{1}{\cos\theta_z}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_24:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_24:value}}} \approx AM\,1.5$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `48` — Enter 48 into Register $X$ ($X = 48$).
2. `{{key:COS}}` — Evaluate trigonometric $\cos(48)$ in place $\rightarrow$ ($X = 0.6691$).
3. `{{key:1/x}}` — Invert Register $X$ ($1/X$) in place $\rightarrow$ ($X = 1.4945$).

Directly matches the standard AM1.5 solar test condition!

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `48 {{key:COS}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.6691$ | Evaluate solar zenith cosine $\cos(48^\circ)$ |
| 2 | `{{key:1/x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1.4945$** | Take secant for optical air mass coefficient $\text{AM} = 1/\cos Z$ |

---

### Problem 4.17: Catenary Hanging Cable Tension at Support Tower
**Structural Mechanics Context:** Cable unit weight $w = 12.5\text{ N/m}$, parameter $a = 600.0\text{ m}$, span $L = 400.0\text{ m}$ (half-span $x = 200.0\text{ m}$):
$$T_0 = w \cdot a = 12.5 \times 600 = 7500.0\text{ N}$$
$$T = T_0 \cosh\left(\frac{x}{a}\right) = 7500 \cosh\left(\frac{200}{600}\right) = 7500 \cosh(0.333333)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_25:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_25:value}}\text{ N}} \approx 7.92\text{ kN}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `200` `{{key:ENTER}}` — Key the catenary half-span coordinate ($x = 200.0\text{ m}$) into Register $X$ and push to $Y$.
2. `600` `{{key:÷}}` — Supply parameter $a = 600.0\text{ m}$ and divide, yielding normalized coordinate $x/a = 0.333333$.
3. `{{key:HYP}} {{key:COS}}` — Execute the hyperbolic cosine, giving $\cosh(0.333333) \approx 1.05607$.
4. `7500` `{{key:×}}` — Scale by horizontal base tension $T_0 = 7500\text{ N}$, yielding total tower reaction $T \approx \mathbf{7,920.54\text{ N}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `200 {{key:ENTER}} 600 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.3333$ | Dimensionless catenary span parameter $x/a = 200/600$ |
| 2 | `{{key:HYP}} {{key:COS}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0561$ | Hyperbolic cosine $\cosh(x/a)$ |
| 3 | `7500 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$7920.5390$** | Multiply by horizontal tension $H = 7500\text{ N}$ for cable tension $T$ (N) |

---

### Problem 4.18: Polar Conic Equation for Elliptical Satellite Orbit
**Astrodynamics Context:** Semi-latus rectum $p = 7,200.0\text{ km}$, orbital eccentricity $e = 0.150$. Find orbital radius at true anomaly $\theta = 60.0^\circ$:
$$r = \frac{p}{1 + e \cos\theta}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_26:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_26:value}}\text{ km}}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `60` `{{key:COS}}` `0.150` `{{key:×}}` `1` `{{key:+}}` — Take the cosine of true anomaly $\theta = 60^\circ$ ($0.500$), scale by eccentricity $e = 0.150$, and add 1, forming denominator $1 + e\cos\theta = 1.0750$.
2. `7200` `{{key:x⇄y}}` `{{key:÷}}` — Key semi-latus rectum $p = 7200\text{ km}$, exchange registers via `{{key:x⇄y}}` to position $p$ as dividend, and divide to obtain orbital radius $r \approx \mathbf{6,697.67\text{ km}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `60 {{key:COS}} 0.150 {{key:×}} 1 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0750$ | Polar orbital denominator $(1 + e \cos\theta)$ |
| 2 | `7200 {{key:x⇄y}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$6697.6744$** | Divide semi-latus rectum $p = 7200\text{ km}$ for orbital radius $r$ (km) |

---

### Problem 4.19: Nautical Waypoint Bearing and Distance
**Marine Navigation Context:** Course from Station A ($x_1=0, y_1=0$) to Station B ($\Delta x = 45.2\text{ nmi}$ East, $\Delta y = 78.5\text{ nmi}$ North):

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_27:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_27:value}}`**

> **Named RPN Stack Idiom: *The Inside-Out Radical & Navigation Baseline*** — Square departure and latitude differences on the stack, sum, and take square root without scratchpad memory {{cite:munroe2014,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `45` `{{key:ENTER}}` — Push northing delta $\Delta y = 45.0\text{ nmi}$ to Register $Y$.
2. `{{key:x²}}` — Square northing displacement in place ($\Delta y^2 = 2025.0$).
3. `32` `{{key:ENTER}}` — Place easting delta $\Delta x = 32.0\text{ nmi}$ on stack, elevating $\Delta y^2$ to $Z$.
4. `{{key:x²}}` — Square easting displacement ($\Delta x^2 = 1024.0$).
5. `{{key:+}}` — Add quadrature components ($3049.0$).
6. `{{key:√x}}` — Extract square root to yield straight-line nautical distance $d \approx 55.22\text{ nmi}$.

Stack: Distance $r = \mathbf{90.5847\text{ nmi}}$, Heading $\theta = \mathbf{60.07^\circ}$ (Nautical true bearing $030^\circ$ relative to North: $90^\circ - 60.07^\circ = 029.93^\circ$).

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `78.5 {{key:ENTER}} 45.2 {{key:▸θ,r}}` | $0.0000$ | $0.0000$ | $60.0668$ | **$90.5831$** | Convert rectangular coordinate offsets $(\Delta y, \Delta x)$ to distance and bearing |

---

### Problem 4.20: Trigonometric Leveling to Inaccessible Mountain Peak
**Geodesy Context:** Two observation stations separated by baseline distance $d = 500.0\text{ m}$. Elevation angle to peak from Station 1 is $\alpha = 24.5^\circ$; from Station 2 (closer) is $\beta = 31.2^\circ$:
$$H = \frac{d}{\cot\alpha - \cot\beta} = \frac{d}{\frac{1}{\tan\alpha} - \frac{1}{\tan\beta}}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_28:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_28:value}}\text{ meters}}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `24.5` `{{key:TAN}}` `{{key:1/x}}` — Invert the tangent of elevation $\alpha = 24.5^\circ$ to find $\cot\alpha \approx 2.194301$.
2. `31.2` `{{key:TAN}}` `{{key:1/x}}` — Compute $\cot\beta \approx 1.651167$ while preserving $\cot\alpha$ in Register $Y$.
3. `{{key:-}}` — Subtract to find the cotangent difference $\Delta\cot \approx 0.543134$.
4. `500` `{{key:x⇄y}}` `{{key:÷}}` — Enter baseline $d = 500.0\text{ m}$, swap registers to place baseline into the numerator, and divide to yield summit elevation $H \approx \mathbf{920.63\text{ m}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `24.5 {{key:TAN}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.1943$ | Invert tangent for Station 1 cotangent $\cot(24.5^\circ)$ |
| 2 | `31.2 {{key:TAN}} {{key:1/x}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.5431$ | Subtract Station 2 cotangent $\cot(31.2^\circ)$ for differential $\Delta\cot$ |
| 3 | `500 {{key:x⇄y}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$920.6349$** | Divide baseline distance $d = 500\text{ m}$ for summit height $H$ (m) |

---

### Problem 4.21: Large-Amplitude Pendulum Period Correction
**Classical Mechanics Context:** Small-angle period $T_0 = 2.000\text{ s}$. For initial release angle $\theta_0 = 45.0^\circ$:
$$T \approx T_0 \left(1 + \frac{1}{4} \sin^2\left(\frac{\theta_0}{2}\right)\right) = 2.0 \left(1 + 0.25 \sin^2(22.5^\circ)\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_29:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_29:value}}\text{ seconds}}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `22.5` `{{key:SIN}}` `{{key:x²}}` — Evaluate $\sin(22.5^\circ) \approx 0.382683$ and square, giving $\sin^2(\theta_0/2) \approx 0.146447$.
2. `0.25` `{{key:×}}` `1` `{{key:+}}` — Multiply by $1/4$ and add unity, generating the nonlinear elongation coefficient $1.036612$.
3. `2.0` `{{key:×}}` — Scale by small-angle harmonic period $T_0 = 2.000\text{ s}$, yielding the true period $T \approx \mathbf{2.0732\text{ s}}$.

Accounts for non-linear pendulum period elongation.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `22.5 {{key:SIN}} {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.1464$ | Half-angle sine squared $\sin^2(\theta_0/2)$ for $\theta_0 = 45^\circ$ |
| 2 | `0.25 {{key:×}} 1 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0366$ | Quadratic period correction factor $(1 + 0.25 \sin^2(\theta_0/2))$ |
| 3 | `2.0 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$2.0732$** | Scale harmonic period $T_0 = 2.0\text{ s}$ for true period $T$ (s) |

---

### Problem 4.22: Circular Arch Chord Length and Segment Arc Length
**Civil Architecture Context:** Circular arch of radius $R = 25.0\text{ m}$ spanning central angle $\theta = 70.0^\circ$:
$$\text{Chord } c = 2 R \sin\left(\frac{\theta}{2}\right), \quad \text{Arc } s = R \frac{\theta \pi}{180}$$

**Keystrokes for Chord:** `{{res:sc32_04_trig_vectors_polar_seq_30:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_30:value}}\text{ m}}$

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `2` `{{key:ENTER}}` — Place chord multiplier 2 into $Y$.
2. `18.5` `{{key:×}}` — Multiply by radius $R = 18.5\text{ m}$ to form diameter $2R = 37.0\text{ m}$.
3. `75` `{{key:ENTER}}` `2` `{{key:÷}}` — Compute half-angle $\theta/2 = 37.5^\circ$.
4. `{{key:SIN}}` `{{key:×}}` — Take sine ($\approx 0.60876$) and multiply by diameter, giving chord span $c \approx \mathbf{22.52\text{ m}}$.

**Keystrokes for Arc:** `{{res:sc32_04_trig_vectors_polar_seq_31:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_31:value}}\text{ m}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `25 {{key:ENTER}} 2 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $50.0000$ | Arch diameter $2 R = 50\text{ m}$ |
| 2 | `35 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$28.6788$** | Multiply by half-angle sine $\sin(35^\circ)$ for arch chord length $c$ (m) |

---

### Problem 4.23: Brewster's Angle of Polarization
**Laser Optics Context:** Laser beam incident on crown glass window ($n = 1.520$ in air):
$$\theta_B = \arctan(n)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_32:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_32:value}}^\circ}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `1.520` — Enter 1.52 into Register $X$ ($X = 1.52$).
2. `{{key:ATAN}}` — Evaluate inverse trigonometric $\operatorname{atan}(1.52)$ in place $\rightarrow$ ($X = 56.6593$).

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `1.520 {{key:ATAN}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$56.6593$** | Extract Brewster angle $\theta_B = \arctan(n_2/n_1)$ for crown glass (degrees) |

---

### Problem 4.24: Strain Gauge Rosette 2D Coordinate Rotation
**Experimental Mechanics Context:** Measured strains $\epsilon_x = 450\,\mu\epsilon$, $\epsilon_y = 120\,\mu\epsilon$, $\gamma_{xy} = 280\,\mu\epsilon$. Rotate coordinate frame by $\theta = 30.0^\circ$:
$$\epsilon_{x'} = \frac{\epsilon_x + \epsilon_y}{2} + \frac{\epsilon_x - \epsilon_y}{2}\cos(2\theta) + \frac{\gamma_{xy}}{2}\sin(2\theta)$$

**Keystrokes:**
`{{res:sc32_04_trig_vectors_polar_seq_33:keys}}`

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `850` `{{key:ENTER}}` — Enter principal strain $\epsilon_x = 850\,\mu\varepsilon$ and push to $Y$.
2. `250` `{{key:+}}` — Add transverse strain $\epsilon_y = 250\,\mu\varepsilon$, totaling $1100\,\mu\varepsilon$.
3. `2` `{{key:÷}}` — Halve the sum to compute average normal strain $\epsilon_{\text{avg}} = 550\,\mu\varepsilon$.
4. `850` `{{key:ENTER}}` `250` `{{key:-}}` `2` `{{key:÷}}` — Calculate strain difference amplitude $(\epsilon_x - \epsilon_y)/2 = 300\,\mu\varepsilon$.
5. `60` `{{key:COS}}` `{{key:×}}` — Multiply by $\cos(2\theta) = \cos(60^\circ) = 0.500$, giving rotational offset $150\,\mu\varepsilon$.
6. `{{key:+}}` — Sum with $\epsilon_{\text{avg}}$ to establish transformed normal strain $\epsilon_\theta = 700\,\mu\varepsilon$.

Result: $\epsilon_{x'} \approx 285 + 82.5 + 121.24 = \mathbf{488.74\,\mu\epsilon}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `450 {{key:ENTER}} 120 {{key:+}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $285.0000$ | Hydrostatic mean strain $(\epsilon_a + \epsilon_c)/2$ |
| 2 | `450 {{key:ENTER}} 120 {{key:-}} 2 {{key:÷}} 60 {{key:COS}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $367.5000$ | Add normal strain cosine transform $((\epsilon_a - \epsilon_c)/2)\cos(60^\circ)$ |
| 3 | `280 {{key:ENTER}} 2 {{key:÷}} 60 {{key:SIN}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$488.7436$** | Add shear strain sine transform $(\gamma_{xy}/2)\sin(60^\circ)$ for rotated strain $\epsilon_{x'}$ ($\mu\epsilon$) |

---

### Problem 4.25: Wave Superposition with Arbitrary Phase Shift
**Acoustics Context:** Two sound waves $A_1 = 2.40\text{ Pa}$ and $A_2 = 3.10\text{ Pa}$ interfering with phase difference $\Delta\phi = 55.0^\circ$:
$$A_{\text{resultant}} = \sqrt{A_1^2 + A_2^2 + 2 A_1 A_2 \cos(\Delta\phi)}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_34:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_34:value}}\text{ Pa}}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `12` `{{key:ENTER}}` — Enter primary amplitude $A_1 = 12\text{ V}$.
2. `{{key:x²}}` — Square to obtain $A_1^2 = 144\text{ V}^2$.
3. `18` `{{key:ENTER}}` `{{key:x²}}` — Enter and square secondary amplitude $A_2 = 18\text{ V}$ ($324\text{ V}^2$).
4. `{{key:+}}` — Sum squared terms ($468\text{ V}^2$).
5. `2` `{{key:ENTER}}` `12` `{{key:×}}` `18` `{{key:×}}` `45` `{{key:COS}}` `{{key:×}}` — Form cross term $2 A_1 A_2 \cos\Delta\phi \approx 305.47\text{ V}^2$.
6. `{{key:+}}` — Combine with sum of squares ($773.47\text{ V}^2$).
7. `{{key:√x}}` — Extract square root to obtain resultant amplitude $A \approx \mathbf{27.81\text{ V}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `2.4 {{key:x²}} 3.1 {{key:x²}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $15.3700$ | Sum of squared wave amplitudes $A_1^2 + A_2^2$ |
| 2 | `2 {{key:ENTER}} 2.4 {{key:×}} 3.1 {{key:×}} 55 {{key:COS}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $23.9048$ | Add wave interference cross-term $2 A_1 A_2 \cos(\Delta\phi)$ |
| 3 | `{{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$4.8893$** | Extract square root for superposed wave amplitude $A_{\text{res}}$ |

---

### Problem 4.26: Aircraft Coordinated Turn Radius and G-Load
**Flight Dynamics Context:** Aircraft turning at $v = 150.0\text{ kts} = 77.1667\text{ m/s}$ at bank angle $\phi = 45.0^\circ$ ($g = 9.80665\text{ m/s}^2$):
$$R = \frac{v^2}{g \tan\phi}, \quad \text{Load Factor } n = \frac{1}{\cos\phi}$$

**Keystrokes for Radius:** `{{res:sc32_04_trig_vectors_polar_seq_35:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_35:value}}\text{ meters}}$

> **Named RPN Stack Idiom: *The Inside-Out Radical & Dynamic G-Load Pipeline*** — Invert banking cosine to extract load factor $n = 1/\cos\theta$, and calculate turn radius from velocity and banking angle without scratchpad memory {{cite:munroe2014,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `55` `{{key:COS}}` — Compute $\cos(55^\circ) \approx 0.57358$ from bank angle.
2. `{{key:1/x}}` — Invert to determine flight load factor $n \approx 1.7434\,G$.
3. `180` `{{key:ENTER}}` `3.6` `{{key:÷}}` `{{key:x²}}` — Convert speed $180\text{ km/h}$ to $\text{m/s}$ ($50.0$) and square ($2500\text{ m}^2/\text{s}^2$).
4. `9.80665` `{{key:ENTER}}` `55` `{{key:TAN}}` `{{key:×}}` — Calculate centripetal acceleration denominator $g\tan\phi \approx 13.9984\text{ m/s}^2$.
5. `{{key:÷}}` — Divide $v^2$ by acceleration to yield turn radius $R \approx \mathbf{178.59\text{ m}}$.

**Keystrokes for Load Factor:** `{{res:sc32_04_trig_vectors_polar_seq_36:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_36:value}}\,G}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `77.1667 {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $5954.6996$ | Square true airspeed in m/s ($v^2 = (277.8/3.6)^2$) |
| 2 | `9.80665 {{key:ENTER}} 45 {{key:TAN}} {{key:×}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$607.2104$** | Divide by $g \tan\theta$ for coordinated turn radius $R$ (m) |

---

### Problem 4.27: Keplerian Orbit True Anomaly from Eccentric Anomaly
**Orbital Mechanics Context:** Eccentricity $e = 0.240$, eccentric anomaly $E = 40.0^\circ$:
$$\tan\left(\frac{\nu}{2}\right) = \sqrt{\frac{1 + e}{1 - e}} \tan\left(\frac{E}{2}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_37:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_37:value}}^\circ}$.

> **Named RPN Stack Idiom: *The LASTX Dual-Branch Trick & Half-Angle Tangent Pipeline*** — Compute orbit eccentricity factors $(1+e)$ and $(1-e)$, take square root of their ratio, and scale by half-angle tangent without re-keying {{cite:gauss1809,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `1.240 {{key:ENTER}} 0.760 {{key:÷}} {{key:√x}}` — Compute orbit eccentricity ratio $\sqrt{(1+e)/(1-e)} = \sqrt{1.24/0.76} \approx 1.2773$.
2. `20 {{key:TAN}} {{key:×}}` — Scale by eccentric anomaly half-angle tangent $\tan(E/2) = \tan(20^\circ) \approx 0.36397$.
3. `{{key:ATAN}} 2 {{key:×}}` — Extract half-angle arctangent and double in place to obtain true anomaly $\nu \approx \mathbf{50.61^\circ}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `1.240 {{key:ENTER}} 0.760 {{key:÷}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.2773$ | Eccentricity ratio factor $\sqrt{(1+e)/(1-e)}$ for $e=0.24$ |
| 2 | `20 {{key:TAN}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.4649$ | Multiply by half-angle eccentric anomaly tangent $\tan(E/2)$ |
| 3 | `{{key:ATAN}} 2 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$49.8685$** | Extract arctangent and double for true anomaly $\nu$ (degrees) |

---

### Problem 4.28: Roof Truss Member Forces via Method of Joints
**Structural Engineering Context:** Ridge joint with vertical downward roof load $P = 15.0\text{ kN}$ balanced by two symmetrical rafters inclined at $\theta = 30.0^\circ$ to horizontal:
$$2 F_{\text{rafter}} \sin\theta = P \implies F_{\text{rafter}} = \frac{P}{2 \sin\theta}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_38:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_38:value}}\text{ kN}}$ compression.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `15.0` `{{key:ENTER}}` — Enter vertical peak load $P = 15.0\text{ kN}$ into Register $Y$.
2. `30` `{{key:SIN}}` `{{key:÷}}` — Divide by $\sin 30^\circ$ to find rafter compressive resultant $F_{AB} = 30.0\text{ kN}$.
3. `30` `{{key:COS}}` `{{key:×}}` — Multiply rafter thrust by $\cos 30^\circ$ to derive tie rod tension $F_{AC} \approx \mathbf{25.98\text{ kN}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `15 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $15.0000$ | $15.0000$ | Load vertex nodal vertical load $P = 15\text{ kN}$ |
| 2 | `2 {{key:ENTER}} 30 {{key:SIN}} {{key:×}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$15.0000$** | Divide by $2 \sin(30^\circ)$ for truss member force $F$ (kN) |

---

### Problem 4.29: Helical Compression Spring Wahl Stress Factor
**Machine Design Context:** Spring index $C = D / d = 7.50$:
$$K_W = \frac{4C - 1}{4C - 4} + \frac{0.615}{C}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_39:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_39:value}}`**

**Stack State Inspection:**
1. Numerator: $4(7.5) - 1 = 29.0$
2. Denominator: $4(7.5) - 4 = 26.0$
3. First term: $29/26 \approx 1.115385$
4. Second term: $0.615 / 7.5 = 0.082000$
5. Sum: $K_W = \mathbf{1.197385}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `4 {{key:ENTER}} 7.5 {{key:×}} 1 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $29.0000$ | Numerator $(4C - 1)$ for spring index $C = 7.5$ |
| 2 | `4 {{key:ENTER}} 7.5 {{key:×}} 4 {{key:-}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.1154$ | Divide by denominator $(4C - 4)$ for curvature factor |
| 3 | `0.615 {{key:ENTER}} 7.5 {{key:÷}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1.1974$** | Add direct shear correction $0.615/C$ for Wahl stress factor $K_w$ |

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

### Problem 4.31: Solar Azimuth Angle Calculation
**Renewable Energy Context:** Latitude $\phi = 32.0^\circ\text{ N}$, solar declination $\delta = 18.5^\circ$, solar hour angle $\omega = 45.0^\circ$ ($3\text{ hours}$ before solar noon). Calculate solar elevation angle $\alpha$ and solar azimuth angle $\gamma_s$:
$$\sin\alpha = \sin\phi \sin\delta + \cos\phi \cos\delta \cos\omega$$
$$\cos\gamma_s = \frac{\sin\alpha \sin\phi - \sin\delta}{\cos\alpha \cos\phi}$$

**Keystrokes:**
`{{res:sc32_04_trig_vectors_polar_seq_41:keys}}`

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `32` — Enter 32 into Register $X$ ($X = 32$).
2. `{{key:SIN}}` — Evaluate trigonometric $\sin(32)$ in place $\rightarrow$ ($X = 0.5299$).
3. `18.5` — Enter 18.5 into Register $X$ ($Y = 0.5299, X = 18.5$).
4. `{{key:SIN}}` — Evaluate trigonometric $\sin(18.5)$ in place $\rightarrow$ ($Y = 0.5299, X = 0.3173$).
5. `{{key:×}}` — Form product of sine components $\sin\phi \sin\delta$ ($0.5299 \times 0.3173$), holding first term ($X = 0.1681$).
6. `32` — Enter 32 into Register $X$ ($Y = 0.1681, X = 32$).
7. `{{key:COS}}` — Evaluate trigonometric $\cos(32)$ in place $\rightarrow$ ($Y = 0.1681, X = 0.848$).
8. `18.5` — Enter 18.5 into Register $X$ ($Z = 0.1681, Y = 0.848, X = 18.5$).
9. `{{key:COS}}` — Evaluate trigonometric $\cos(18.5)$ in place $\rightarrow$ ($Z = 0.1681, Y = 0.848, X = 0.9483$).
10. `{{key:×}}` — Form product $\cos\phi \cos\delta$ ($0.848 \times 0.9483$), yielding intermediate factor ($Y = 0.1681, X = 0.8042$).
11. `45` — Enter 45 into Register $X$ ($Z = 0.1681, Y = 0.8042, X = 45$).
12. `{{key:COS}}` — Evaluate trigonometric $\cos(45)$ in place $\rightarrow$ ($Z = 0.1681, Y = 0.8042, X = 0.7071$).
13. `{{key:×}}` — Multiply by hour-angle cosine $\cos\omega$ ($0.8042 \times 0.7071$), evaluating second celestial term ($Y = 0.1681, X = 0.5687$).
14. `{{key:+}}` — Sum both celestial terms ($0.1681 + 0.5687$) to obtain $\sin\alpha = 0.7368$.
15. `{{key:ASIN}}` — Evaluate inverse trigonometric $\operatorname{asin}(0.7368)$ in place $\rightarrow$ ($X = 47.4611$).

Stack: Elevation $\alpha = \mathbf{46.5412^\circ}$.
Azimuth evaluation yields: $\gamma_s = \mathbf{112.43^\circ}$ (East of South).

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `32 {{key:SIN}} 18.5 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.1681$ | Spherical latitude-declination sine product $\sin\phi \sin\delta$ |
| 2 | `32 {{key:COS}} 18.5 {{key:COS}} {{key:×}} 45 {{key:COS}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.7368$ | Add hour angle cosine product $\cos\phi \cos\delta \cos h$ |
| 3 | `{{key:ASIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$47.4611$** | Extract inverse sine for solar altitude elevation angle $\alpha$ (degrees) |

---

### Problem 4.32: Coriolis Acceleration Vector on Artillery Projectile
**Ballistics Context:** Projectile traveling North at $v = 820.0\text{ m/s}$ at latitude $\phi = 42.0^\circ\text{ N}$. Earth's angular rotation rate $\Omega = 7.2921 \times 10^{-5}\text{ rad/s}$:
$$a_{\text{coriolis}} = 2 \cdot v \cdot \Omega \cdot \sin\phi$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_42:keys}}` $\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_42:value}}\text{ m/s}^2}$ Eastward.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `2` `{{key:ENTER}}` — Load the kinematic multiplier 2 into $Y$.
2. `7.2921 {{key:E}} 5 {{key:+/-}}` `{{key:×}}` — Multiply by planetary rotation rate $\Omega = 7.2921 \times 10^{-5}\text{ rad/s}$.
3. `850` `{{key:×}}` — Scale by muzzle velocity $v = 850.0\text{ m/s}$ to yield tangential product $0.123966\text{ m/s}^2$.
4. `45` `{{key:SIN}}` `{{key:×}}` — Multiply by $\sin 45^\circ$, delivering lateral Coriolis acceleration $a_c \approx \mathbf{0.08766\text{ m/s}^2}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `2 {{key:ENTER}} 820 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1640.0000$ | Kinematic Coriolis base factor $2 v = 2 \times 820\text{ m/s}$ |
| 2 | `7.2921 {{key:E}} 5 {{key:+/-}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.1196$ | Multiply by Earth angular rate $\Omega = 7.2921 \times 10^{-5}\text{ rad/s}$ |
| 3 | `42 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.0800$** | Multiply by latitude sine $\sin(42^\circ)$ for Coriolis acceleration $a_c$ ($\text{m/s}^2$) |

---

### Problem 4.33: Involute Gear Tooth Base Pitch and Pressure Angle
**Mechanical Design Context:** Module $m = 4.0\text{ mm}$, tooth count $N = 28$, standard pressure angle $\phi = 20.0^\circ$. Calculate pitch circle diameter $D$, base circle diameter $D_b$, and circular base pitch $p_b$:
$$D = m \cdot N, \quad D_b = D \cos\phi, \quad p_b = \pi \cdot m \cos\phi$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_43:keys}}`$\to D = \mathbf{{{res:sc32_04_trig_vectors_polar_seq_43:value}}\text{ mm}}$

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `{{key:π}}` — Push $\pi$ to the bottom of the stack.
2. `4.5` `{{key:×}}` — Multiply by module $m = 4.5\text{ mm}$ to find circular pitch $p \approx 14.1372\text{ mm}$.
3. `20` `{{key:COS}}` `{{key:×}}` — Multiply by $\cos 20^\circ$ to obtain base pitch $p_b \approx \mathbf{13.2846\text{ mm}}$.

`20` `{{key:COS}}` `{{key:×}}` $\to D_b = \mathbf{105.2454\text{ mm}}$
`{{key:π}}` `{{key:ENTER}}` `4` `{{key:×}}` `20` `{{key:COS}}` `{{key:×}}` $\to p_b = \mathbf{11.8087\text{ mm}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `4 {{key:ENTER}} 28 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$112.0000$** | Module times tooth count $m \times z$ for gear pitch diameter $d$ (mm) |

---

### Problem 4.34: Supersonic Oblique Shock Wave Wave Angle
**Aerodynamics Context:** Supersonic flight at Mach $M_1 = 2.50$ over a compression wedge with deflection angle $\theta = 15.0^\circ$. Determine shock angle $\beta$ (approximate weak shock solution $\beta \approx 36.94^\circ$):
$$\tan\theta = 2 \cot\beta \left[\frac{M_1^2 \sin^2\beta - 1}{M_1^2 (\gamma + \cos(2\beta)) + 2}\right]$$
Verified on the SC-32 stack for $\beta = 36.94^\circ$:
`2.50` `{{key:ENTER}}` `36.94` `{{key:SIN}}` `{{key:×}}` `{{key:x²}}` `1` `{{key:-}}` $\to 1.2530$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `2.50` `{{key:ENTER}} 36.94 {{key:SIN}} {{key:×}}` — Enter upstream Mach $M_1 = 2.50$ and multiply by $\sin 36.94^\circ$, establishing normal Mach component $M_{1n} \approx 1.5025$.
2. `{{key:x²}} 1 {{key:-}}` — Square normal Mach ($2.2574$) and subtract unity to yield numerator delta $1.2574$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `2.50 {{key:ENTER}} 36.94 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.5024$ | Upstream Mach normal velocity component $M_1 \sin\beta$ |
| 2 | `{{key:x²}} 1 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1.2573$** | Square normal Mach and subtract unity for oblique shock numerator delta |

---

### Problem 4.35: Wind Turbine Blade Angle of Attack and Relative Velocity
**Aerospace Energy Context:** Blade station radius $r = 32.0\text{ m}$, rotational speed $\Omega = 1.80\text{ rad/s}$ ($u_{\text{rot}} = \Omega r = 57.6\text{ m/s}$), free-stream wind speed $v_{\text{wind}} = 11.5\text{ m/s}$ with axial induction factor $a = 0.30$ ($v_{\text{axial}} = 11.5(1 - 0.30) = 8.05\text{ m/s}$):
$$W_{\text{rel}} = \sqrt{u_{\text{rot}}^2 + v_{\text{axial}}^2}, \quad \phi_{\text{flow}} = \arctan\left(\frac{v_{\text{axial}}}{u_{\text{rot}}}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_44:keys}}` $\rightarrow$ **`{{res:sc32_04_trig_vectors_polar_seq_44:value}}`**

> **Named RPN Stack Idiom: *The Inside-Out Radical & Relative Wind Vector Pipeline*** — Vector-sum axial wind speed and blade rotational tip speed in the stack, extracting relative inflow velocity and blade inflow angle in place {{cite:ellenberg2014,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `12` `{{key:ENTER}}` — Key axial wind speed $v_{\text{wind}} = 12.0\text{ m/s}$.
2. `{{key:x²}}` — Square to obtain $144.0\text{ m}^2/\text{s}^2$.
3. `65` `{{key:ENTER}}` `{{key:x²}}` — Push and square blade tip speed $v_{\text{blade}} = 65.0\text{ m/s}$ ($4225.0$).
4. `{{key:+}}` — Add orthogonal kinetic terms ($4369.0$).
5. `{{key:√x}}` — Extract square root to determine resultant relative inflow velocity $v_{\text{rel}} \approx \mathbf{66.10\text{ m/s}}$.

Stack: Relative wind speed $W_{\text{rel}} = \mathbf{58.1593\text{ m/s}}$, Inflow angle $\phi_{\text{flow}} = \mathbf{7.95^\circ}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `8.05 {{key:ENTER}} 57.6 {{key:▸θ,r}}` | $0.0000$ | $0.0000$ | $7.9560$ | **$58.1598$** | Combine wind velocity and blade speed vectors into relative speed and angle |

---

### Problem 4.36: Surveying Triangulation Intersection from Two Stations
**Geodesy Context:** Baseline between Stations $A$ and $B$ is $b = 1,250.0\text{ m}$. Angles observed to unknown landmark $P$: $\angle A = 58.4^\circ$, $\angle B = 71.2^\circ$. Angle at $P$: $\angle P = 180^\circ - (58.4^\circ + 71.2^\circ) = 50.4^\circ$:
$$\text{Distance } AP = b \frac{\sin B}{\sin P} = 1250 \frac{\sin(71.2^\circ)}{\sin(50.4^\circ)}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_45:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_45:value}}\text{ meters}}$.

> **Named RPN Stack Idiom: *The x⇄y Denominator Flip & Surveying Sine Intersection*** — Evaluate the opposing baseline angle sum, divide sine factors via stack swap, and compute target distance with zero scratch registers {{cite:gauss1809,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `1250 {{key:ENTER}} 71.2 {{key:SIN}} {{key:×}}` — Scale survey baseline distance $b = 1250.0\text{ m}$ by opposing observation angle sine $\sin(71.2^\circ) \approx 0.94665$.
2. `50.4 {{key:SIN}} {{key:÷}}` — Divide by vertex angle sine $\sin(50.4^\circ) \approx 0.77051$ to evaluate landmark distance $AP \approx \mathbf{1535.84\text{ m}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `1250 {{key:ENTER}} 71.2 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1183.3116$ | Baseline opposite sine product $b \sin B$ ($1250\text{ m} \times \sin(71.2^\circ)$) |
| 2 | `50.4 {{key:SIN}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1535.7446$** | Divide by landmark opposing sine $\sin P = \sin(50.4^\circ)$ for distance $AP$ (m) |

---

### Problem 4.37: Celestial Coordinate Conversion (RA/Dec to Alt/Az)
**Astronomy Context:** Observer at latitude $\phi = 38.0^\circ\text{ N}$. Star with declination $\delta = 22.5^\circ$ and local hour angle $H = 40.0^\circ$:
$$\sin a = \sin\phi \sin\delta + \cos\phi \cos\delta \cos H$$

**Keystrokes:**
`{{res:sc32_04_trig_vectors_polar_seq_46:keys}}`

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `38` — Enter 38 into Register $X$ ($X = 38$).
2. `{{key:SIN}}` — Evaluate trigonometric $\sin(38)$ in place $\rightarrow$ ($X = 0.6157$).
3. `22.5` — Enter 22.5 into Register $X$ ($Y = 0.6157, X = 22.5$).
4. `{{key:SIN}}` — Evaluate trigonometric $\sin(22.5)$ in place $\rightarrow$ ($Y = 0.6157, X = 0.3827$).
5. `{{key:×}}` — Form product of sine factors $\sin\phi \sin\delta$ ($0.6157 \times 0.3827$), holding the first summand ($X = 0.2356$).
6. `38` — Enter 38 into Register $X$ ($Y = 0.2356, X = 38$).
7. `{{key:COS}}` — Evaluate trigonometric $\cos(38)$ in place $\rightarrow$ ($Y = 0.2356, X = 0.788$).
8. `22.5` — Enter 22.5 into Register $X$ ($Z = 0.2356, Y = 0.788, X = 22.5$).
9. `{{key:COS}}` — Evaluate trigonometric $\cos(22.5)$ in place $\rightarrow$ ($Z = 0.2356, Y = 0.788, X = 0.9239$).
10. `{{key:×}}` — Form product $\cos\phi \cos\delta$ ($0.788 \times 0.9239$), yielding intermediate factor ($Y = 0.2356, X = 0.728$).
11. `40` — Enter 40 into Register $X$ ($Z = 0.2356, Y = 0.728, X = 40$).
12. `{{key:COS}}` — Evaluate trigonometric $\cos(40)$ in place $\rightarrow$ ($Z = 0.2356, Y = 0.728, X = 0.766$).
13. `{{key:×}}` — Multiply by hour-angle cosine $\cos h$ ($0.728 \times 0.766$), evaluating second term ($Y = 0.2356, X = 0.5577$).
14. `{{key:+}}` — Sum both terms ($0.2356 + 0.5577$) to establish $\sin a = 0.7933$.
15. `{{key:ASIN}}` — Evaluate inverse trigonometric $\operatorname{asin}(0.7933)$ in place $\rightarrow$ ($X = 52.4954$).

Stack: Star altitude angle $a = \mathbf{51.7891^\circ}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `38 {{key:SIN}} 22.5 {{key:SIN}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.2356$ | Celestial sphere pole-altitude product $\sin\phi \sin\delta$ |
| 2 | `38 {{key:COS}} 22.5 {{key:COS}} {{key:×}} 40 {{key:COS}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.7933$ | Add horizontal meridian cosine product $\cos\phi \cos\delta \cos H$ |
| 3 | `{{key:ASIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$52.4954$** | Extract inverse sine for target horizon altitude $a$ (degrees) |

---

### Problem 4.38: Gyroscopic Precession Angular Rate
**Avionics Inertial Context:** Rotor mass moment of inertia $I_s = 0.0125\text{ kg}\cdot\text{m}^2$, spin speed $\omega_s = 24,000\text{ rpm} = 2513.27\text{ rad/s}$. Applied disturbance torque $\tau = 0.450\text{ N}\cdot\text{m}$:
$$\Omega_p = \frac{\tau}{I_s \cdot \omega_s}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_47:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_47:value}}\text{ rad/s}} = 0.8207^\circ/\text{s}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `2.5` `{{key:ENTER}}` — Enter applied torque $\tau = 2.50\text{ N}\cdot\text{m}$.
2. `0.045` `{{key:ENTER}}` — Key polar moment of inertia $I = 0.045\text{ kg}\cdot\text{m}^2$.
3. `12000` `{{key:ENTER}}` `2` `{{key:×}}` `{{key:π}}` `{{key:×}}` `60` `{{key:÷}}` — Convert $12,000\text{ RPM}$ into radians per second ($\omega \approx 1256.64\text{ rad/s}$).
4. `{{key:×}}` — Multiply inertia by spin rate to establish angular momentum $L \approx 56.55\text{ kg}\cdot\text{m}^2/\text{s}$.
5. `{{key:÷}}` — Divide torque by momentum to yield steady precession rate $\Omega_p \approx \mathbf{0.0442\text{ rad/s}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `0.450 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $0.4500$ | $0.4500$ | Load applied rotor torque $\tau = 0.450\text{ N}\cdot\text{m}$ |
| 2 | `0.0125 {{key:ENTER}} 24000 {{key:ENTER}} 2 {{key:×}} {{key:π}} {{key:×}} 60 {{key:÷}} {{key:×}} {{key:÷}}` | $0.4500$ | $0.4500$ | $0.4500$ | **$0.0143$** | Divide by angular momentum $L = I \omega$ for precession rate $\Omega_p$ (rad/s) |

---

### Problem 4.39: Quarter-Wave Plate Retardance and Jones Matrix
**Laser Physics Context:** Ellipticity angle $\chi$ produced by linear polarizer at angle $\theta = 22.5^\circ$ through quarter-wave plate:
$$\sin(2\chi) = \sin(2\theta) \sin\delta$$
For a quarter-wave plate ($\delta = 90.0^\circ$), $\sin\delta = 1.0$:
$$\chi = \frac{1}{2} \arcsin(\sin(45^\circ)) = \frac{45^\circ}{2} = \mathbf{22.50^\circ}$$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `22.5` `{{key:ENTER}} 2 {{key:×}}` — Double incident angle $\theta = 22.5^\circ$ to $45.0^\circ$.
2. `{{key:SIN}} {{key:ASIN}} 2 {{key:÷}}` — Compute sine, apply retardance, take arc sine, and halve, confirming polarization ellipticity $\chi = \mathbf{22.50^\circ}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `22.5 {{key:ENTER}} 2 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $45.0000$ | Double incident polarizer angle $2\theta = 45.0^\circ$ |
| 2 | `{{key:SIN}} {{key:ASIN}}` | $0.0000$ | $0.0000$ | $0.0000$ | $45.0000$ | Evaluate quarter-wave plate transmission and arc sine |
| 3 | `2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$22.5000$** | Halve for polarization ellipticity angle $\chi$ (degrees) |

---

### Problem 4.40: Acoustic Directivity Index of Circular Piston Speaker
**Electroacoustics Context:** Loudspeaker piston radius $a = 0.10\text{ m}$ radiating at frequency $f = 2,500\text{ Hz}$ in air ($c = 343\text{ m/s}$):
$$k = \frac{2\pi f}{c} = \frac{2\pi(2500)}{343} \approx 45.7958\text{ m}^{-1}$$
$$k a = 45.7958 \times 0.10 = 4.5796$$
Directivity index for $k a \gg 1$:
$$D_I \approx 10 \log_{10}(ka)^2 = 20 \log_{10}(ka)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_48:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_48:value}}\text{ dB}}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `4.5796` — Enter 4.5796 into Register $X$ ($X = 4.5796$).
2. `{{key:LOG}}` — Compute base-10 logarithm $\log_{10}(X)$ in place $\rightarrow$ ($X = 0.6608$).
3. `20` `{{key:×}}` — Key decibel power scale factor $20$ and multiply; amplifier voltage gain resolves to $\mathbf{13.2166\text{ dB}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `4.5796 {{key:LOG}} 20 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$13.2166$** | Directivity ratio converted to decibels for circular acoustic piston DI (dB) |

---

### Problem 4.41: Ballistic Reentry Trajectory Flight Path Angle
**Astrodynamics Context:** Atmospheric entry interface velocity $v_E = 7,800\text{ m/s}$, radial velocity $v_r = -210\text{ m/s}$, tangential speed $v_\theta = \sqrt{7800^2 - 210^2} \approx 7797.17\text{ m/s}$. Find flight path entry angle $\gamma$:
$$\sin\gamma = \frac{v_r}{v_E} \implies \gamma = \arcsin\left(\frac{-210}{7800}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_49:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_49:value}}^\circ}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `1450` `{{key:ENTER}}` — Enter vertical descent rate $v_z = 1450.0\text{ m/s}$.
2. `7600` `{{key:÷}}` — Divide by horizontal entry speed $v_x = 7600.0\text{ m/s}$ to find trajectory slope $\tan\gamma \approx 0.190789$.
3. `{{key:ATAN}}` — Evaluate arctangent to calculate flight path entry angle $\gamma \approx \mathbf{10.80^\circ}$.

Presents a classic shallow $1.5^\circ$ entry corridor.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `210 {{key:+/-}} {{key:ENTER}} 7800 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-0.0269$ | Velocity vector vertical/horizontal ratio $v_y/v_x$ |
| 2 | `{{key:ATAN}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$-1.5422$** | Extract flight path angle $\gamma = \arctan(v_y/v_x)$ (degrees) |

---

### Problem 4.42: Circular Roadway Curve Sight Distance
**Highway Engineering Context:** Curve radius $R = 250.0\text{ m}$, obstacle setback distance from centerline $m = 8.5\text{ m}$. Calculate available stopping sight distance $S$:
$$m = R \left(1 - \cos\left(\frac{28.65^\circ S}{R}\right)\right) \implies S = \frac{R}{28.65^\circ} \arccos\left(1 - \frac{m}{R}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_50:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_50:value}}\text{ meters}}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `8` `{{key:ENTER}}` — Enter sight multiplier 8.
2. `350` `{{key:×}}` — Scale by centerline radius $R = 350.0\text{ m}$ to form $2800.0\text{ m}$.
3. `7.5` `{{key:×}}` — Multiply by obstacle lateral setback $m = 7.5\text{ m}$ ($21,000.0\text{ m}^2$).
4. `{{key:√x}}` — Take square root to obtain stopping sight distance $S \approx \mathbf{144.91\text{ m}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `8.5 {{key:ENTER}} 250 {{key:÷}} {{key:+/-}} 1 {{key:+}} {{key:ACOS}}` | $0.0000$ | $0.0000$ | $0.0000$ | $14.9836$ | Sight distance subtended angle $\arccos(1 - m/R)$ |
| 2 | `250 {{key:×}} 28.65 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$130.7467$** | Scale by curvature radius for highway stopping sight distance $S$ (m) |

---

### Problem 4.43: Resection Surveying Point Fix (Kaestner Method)
**Geodesy Context:** Two known landmarks $L_1 (0, 1000)$ and $L_2 (800, 600)$. Measured subtended angle $\alpha = 42.0^\circ$. Baseline length $b$:
$$b = \sqrt{800^2 + (1000 - 600)^2} = \sqrt{640000 + 160000} = \sqrt{800000} = 894.4272\text{ m}$$
Radius of circumscribing position circle:
$$R_{\text{circ}} = \frac{b}{2 \sin\alpha} = \frac{894.4272}{2 \sin(42^\circ)}$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_51:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_51:value}}\text{ meters}}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `800000` — Enter 800000 into Register $X$ ($X = 800000$).
2. `{{key:√x}}` — Extract the principal square root $\sqrt{X}$ in place $\rightarrow$ ($X = 894.4272$).
3. `2` `{{key:÷}}` — Key divisor $2$ and divide to obtain half-baseline distance ($447.2136\text{ m}$) in $X$.
4. `42` — Enter 42 into Register $X$ ($Y = 447.2136, X = 42$).
5. `{{key:SIN}}` — Evaluate trigonometric $\sin(42)$ in place $\rightarrow$ ($Y = 447.2136, X = 0.6691$).
6. `{{key:÷}}` — Divide half-baseline in $Y$ by sine value in $X$ ($447.2136 \div 0.6691$); circumscribing radius resolves to $\mathbf{668.3502\text{ m}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `800000 {{key:√x}} 2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $447.2136$ | Survey resection baseline hypotenuse half-length |
| 2 | `42 {{key:SIN}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$668.3502$** | Divide by subtended sine $\sin(42^\circ)$ for target landmark distance $d$ (m) |

---

### Problem 4.44: Elliptical Polarization Axial Ratio from Phasors
**RF Electromagnetics Context:** Major ellipse axis $E_{\max} = 12.4\text{ V/m}$, minor axis $E_{\min} = 4.2\text{ V/m}$. Calculate axial ratio in decibels:
$$\text{AR}_{\text{dB}} = 20 \log_{10}\left(\frac{E_{\max}}{E_{\min}}\right)$$

**Keystrokes:** `{{res:sc32_04_trig_vectors_polar_seq_52:keys}}`$\to \mathbf{{{res:sc32_04_trig_vectors_polar_seq_52:value}}\text{ dB}}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `8.5` `{{key:ENTER}}` — Enter major axis amplitude $E_a = 8.50\text{ V/m}$.
2. `3.2` `{{key:÷}}` — Divide by minor axis amplitude $E_b = 3.20\text{ V/m}$ to establish linear axial ratio $AR_{\text{lin}} = 2.65625$.
3. `{{key:LOG}}` — Compute common logarithm ($\log_{10}(2.65625) \approx 0.42427$).
4. `20` `{{key:×}}` — Scale by 20 to yield logarithmic axial ratio $AR \approx \mathbf{8.49\text{ dB}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `12.4 {{key:ENTER}} 4.2 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.9524$ | Phasor major/minor semi-axis ratio $E_{\text{max}}/E_{\text{min}}$ |
| 2 | `{{key:LOG}} 20 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$9.4034$** | Logarithmic axial ratio converted to decibels $\text{AR}_{\text{dB}}$ (dB) |

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

## Summary & Looking Ahead

Chapter 4 united trigonometric functions and 2D spatial vectors on the RPN stack. By bridging the unit circle to the physical register pair $(Y, X)$, you executed direct and inverse trigonometry, explored hyperbolic projections on physical catenaries, and mastered instantaneous polar-to-rectangular conversions (`{{key:▸θ,r}}`, `{{key:▸y,x}}`) with full four-quadrant $\text{atan2}$ sign integrity. Survey traverses, aerodynamic shock angles, and force resolutions unfolded seamlessly with zero scratchpad bookkeeping.

Yet 2D vectors in Cartesian space represent only the gateway to a deeper mathematical realm: the complex plane. In **Chapter 5: Complex Numbers, Phasors & Impedance**, the coordinate pair $(Y, X)$ is reinterpreted as real and imaginary components ($Y + Xi$). You will unleash the `{{key:CMPLX}}` engine to add, multiply, invert, and exponentiate complex numbers in place, verify Euler's identity ($e^{i\pi} + 1 = 0$), and solve multi-branch AC electrical impedance networks without matrix software.
