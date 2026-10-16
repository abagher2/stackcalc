---
title: "Chapter 5: Complex Numbers, AC Phasors & Euler's Identity | SC-32 Manual"
description: "Master the classic (Y, X) complex plane convention, [CMPLX] prefix evaluator, live proof of Euler's Identity, AC circuit impedance phasors, RF transmission line reflections, and Smith chart coordinates on the StackCalc SC-32."
---

# Chapter 5: Complex Numbers, AC Phasors & Euler's Identity

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 ADVANCED STEM // COMPLEX NUMBERS &amp; PHASORS</span>
  <span class="te-viewport-status text-sky-400">● (Y, X) GAUSSIAN PLANE &bull; {{key:CMPLX}} PREFIX OPERATOR &bull; EULER'S IDENTITY &bull; AC IMPEDANCE NETWORKS</span>
</div>

## The Application: Steinmetz's AC Miracle & The Electrification of the World

In secondary mathematics, students are routinely told that the imaginary unit $i = \sqrt{-1}$ was invented purely to solve the equation $x^2 + 1 = 0$. Treated this way, complex numbers feel like artificial mathematical games—clever symbols disconnected from physical reality.

Nothing could be further from the truth. **Complex numbers are the mathematical engine that powers every electrical outlet, transmission grid, smartphone radio, and audio speaker on planet Earth.**

### Steinmetz's AC Miracle: Turning Differential Equations into Arithmetic

In the early 1890s, the fierce "War of the Currents" reached its climax. Thomas Edison had blanketed lower Manhattan with direct-current (DC) generating stations, yet DC could travel barely a mile before copper resistance dissipated electric power into useless ambient heat. Nikola Tesla and George Westinghouse championed alternating current (AC), which triumphed on pure physics: high-voltage step-up transformers allowed megawatt power blocks to glide hundreds of miles along slender overhead cables with negligible loss.

Yet while AC was physically superior, it was an engineering nightmare. Alternating current does not flow like laminar water through an open sluice; it is a violent sinusoidal surge sloshing back and forth sixty times a second. Inductors resist changes in current, dragging the current wave behind voltage; capacitors resist changes in voltage, thrusting current ahead. To calculate currents and node voltages across even a modest network with three coils and two capacitor banks, electrical pioneers were forced to assemble and solve labyrinthine systems of coupled second-order differential equations:

$$L \frac{d^2 q}{dt^2} + R \frac{dq}{dt} + \frac{1}{C} q = V_0 \sin(\omega t + \phi)$$

The mathematics was so punishing that the expansion of regional power grids and the design of polyphase induction motors ground nearly to a halt.

Then came the hunchbacked genius of Schenectady. In 1893, at the Chicago World's Fair, Charles Proteus Steinmetz—a four-foot-tall German immigrant mathematician working for General Electric—presented a landmark paper that forever transformed electrical engineering. Steinmetz realized that a physical sinusoidal waveform $v(t) = V_0 \cos(\omega t + \theta)$ was simply the 1D shadow of a 2D vector rotating steadily in the complex plane.

By casting pure ohmic resistance along the real axis and reactive impedance along the orthogonal imaginary axis:

$$\mathbf{Z} = R + j(X_L - X_C) = R + j\left(\omega L - \frac{1}{\omega C}\right)$$

Steinmetz achieved something miraculous: **he banished differential calculus from steady-state circuit analysis**. Ohm's law transformed into simple complex multiplication ($\mathbf{V} = \mathbf{I} \cdot \mathbf{Z}$). Kirchhoff's loop and node laws collapsed into straightforward complex addition ($\sum \mathbf{V} = 0$). In one decisive conceptual leap, months of intractable calculus dissolved into clean complex arithmetic.

On the StackCalc SC-32, Steinmetz's insight lives in hardware:
* **Register $Y$** holds the Real component $\operatorname{Re}(\mathbf{Z})$.
* **Register $X$** holds the Imaginary component $\operatorname{Im}(\mathbf{Z})$.

Press `{{key:CMPLX}} {{key:+}}`, and the SC-32 evaluates full 2D vector phasor addition in microseconds. You are computing on the shoulders of Steinmetz.

<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>{{key:RAD}}</code> (Radians angular mode default; Standard Base-10 Arithmetic; Full 12-digit scientific mantissa <code>{{key:ALL}}</code>). In RF and AC circuit applications where electrical phase angles are conventionally expressed in degrees, problems explicitly declare localized <code>{{key:DEG}}</code> operation.
</div>

---

{{res:sc32_phasor_polar:screenshot|Impedance phasor 3 + j4 rectangular-to-polar conversion -> r = 5, theta = 53.1301 deg}}

## The Concrete-Representational-Abstract (CRA) Architecture of Complex Numbers

Complex numbers are often introduced in secondary and collegiate mathematics as abstract algebraic fictions—mysterious quantities invented solely to solve the unsolvable equation $x^2 + 1 = 0$. On the StackCalc SC-32, complex numbers are approached through the rigorous **Concrete-Representational-Abstract (CRA)** pedagogical sequence, transforming an elusive concept into a tactile, spatial, and computational reality.

| Pedagogical Tier | Physical & Cognitive Domain | Implementation on the SC-32 RPN Architecture |
| :--- | :--- | :--- |
| **1. Concrete Level**<br>*(Physical & Spatial Grounding)* | • Argand orthogonal coordinate plane: 2D vector displacements $(x, y)$.<br>• Physical electrical components: Pure resistance $R$ (horizontal real axis), inductive reactance $+j\omega L$ (positive vertical axis), capacitive reactance $-j/(\omega C)$ (negative vertical axis).<br>• Rotating phasor resolver dial at angular speed $\omega$. | Tactile manipulation on the Unit Circle Volvelle resolver stage before digital keystroke entry. |
| **2. Representation Level**<br>*(Stack Register Visualizations)* | • Classic Corvallis $(Y, X)$ Gaussian plane allocation:<br>&nbsp;&nbsp;Register $Y$: Real component $\operatorname{Re}(\mathbf{z})$<br>&nbsp;&nbsp;Register $X$: Imaginary component $\operatorname{Im}(\mathbf{z})$<br>• Transflective dot-matrix LCD dual-line display:<br>&nbsp;&nbsp;Line 2 ($Y$): `3.0000000000` (Real)<br>&nbsp;&nbsp;Line 1 ($X$): `4.0000000000` (Imaginary) | Dynamic 2-level stack drop and Register $T$ replication on binary complex evaluation. |
| **3. Abstract Level**<br>*(Analytical & Axiomatic Formulations)* | • Euler's formula: $e^{i\theta} = \cos\theta + i\sin\theta$<br>• Field of complex numbers $\mathbb{C} = \{a + bi \mid a, b \in \mathbb{R}, i^2 = -1\}$<br>• Bilinear Möbius transformations on the complex Riemann sphere:<br>&nbsp;&nbsp;$\mathbf{\Gamma} = (\mathbf{Z}_L - Z_0) / (\mathbf{Z}_L + Z_0) \iff$ Smith Chart coordinates | High-speed 64-bit IEEE-754 complex arithmetic pipeline armed via prefix key {{key:CMPLX}}. |

{{blocks:unit_circle_volvelle|Unit Circle Volvelle Complex Phasor Stage}}
*Figure 5.1: The Unit Circle Volvelle resolver establishes a physical bridge to the complex Argand plane, translating angular phase rotation and orthogonal Cartesian projections into Register $Y$ (Real) and Register $X$ (Imaginary) inputs.*

### The Classic $(Y, X)$ Complex Plane Convention
Complex numbers on the StackCalc SC-32 adhere strictly to the classic **$(Y, X)$ rectangular Gaussian plane convention** established on legendary scientific RPN handhelds:

$$\mathbf{z} = Y + X i$$

| Register / Display | Complex Plane Component | Mathematical Notation | Display Appearance ($z = a + bi$) |
| :--- | :--- | :---: | :--- |
| **Register $Y$ (Line 2)** | Real Part | $\operatorname{Re}(\mathbf{z})$ | $a$ (Upper line on transflective LCD) |
| **Register $X$ (Line 1)** | Imaginary Part | $\operatorname{Im}(\mathbf{z})$ | $b$ (Active prompt line on transflective LCD) |

### Why $(Y, X)$?
This allocation provides three vital operational and mathematical advantages:
1. **Direct Coordinate Correspondence:** In standard Euclidean plane graphing, the horizontal coordinate is the abscissa ($x$ or real axis) and the vertical coordinate is the ordinate ($y$ or imaginary axis). On the physical two-line LCD display, Register $Y$ sits directly above Register $X$, creating an intuitive two-element column vector:
   $$\begin{bmatrix} Y \\ X \end{bmatrix} = \begin{bmatrix} \text{Real}(z) \\ \text{Imag}(z) \end{bmatrix}$$
2. **Seamless Polar Transformation Symmetry:** When converting between rectangular and polar forms ($z = r \angle \theta$) via `{{key:▸θ,r}}` and `{{key:▸y,x}}`, entering $(\text{Real in } Y, \text{Imag in } X)$ produces phase angle $\theta = \operatorname{atan2}(X, Y)$ in Register $Y$ and magnitude $|z| = r = \sqrt{Y^2 + X^2}$ in Register $X$.
3. **Zero-Overhead Stack Inspection:** Pressing `{{key:x⇄y}}` toggles between the real and imaginary parts instantly, allowing inspection of full 15-digit internal IEEE-754 precision without disturbing upper stack registers $Z$ and $T$.

---

## The {{key:CMPLX}} Prefix Evaluator Architecture

Rather than trapping the calculator in a modal lock that disables standard arithmetic, the SC-32 features an elegant **prefix evaluator key**: {{key:CMPLX}}.

Pressing Left Shift `{{key:↰}}` followed by `{{key:CMPLX}}` arms the complex arithmetic pipeline for the **immediately following operator or transcendental key**. The `{{key:CMPLX}}` annunciator illuminates on the transflective LCD status line. Pressing `{{key:C}}` disarms the prefix if entered in error, safely preserving the stack.

<div class="admonition note">
<p class="admonition-title">Complex Operator Arity &amp; Stack Dynamics</p>
<ol>
  <li><strong>Unary Complex Operations (<code>{{key:CMPLX}}</code> followed by <code>√x</code>, <code>1/x</code>, <code>x²</code>, <code>eˣ</code>, <code>LN</code>, <code>SIN</code>, <code>COS</code>, <code>TAN</code>):</strong>
    <ul>
      <li>Consumes the single complex operand $\mathbf{z}_1 = Y + Xi$.</li>
      <li>Overwrites registers $(Y, X)$ with the transformed complex result $\mathbf{w} = Y' + X'i$.</li>
      <li>Upper stack registers $Z$ and $T$ remain completely undisturbed on the SC-32 operational stack.</li>
    </ul>
  </li>
  <li><strong>Binary Complex Operations (<code>{{key:CMPLX}}</code> followed by <code>+</code>, <code>-</code>, <code>×</code>, <code>÷</code>, <code>yˣ</code>):</strong>
    <ul>
      <li>Consumes <em>two</em> complex numbers occupying all four stack levels:
        $$\mathbf{z}_2 = T + Zi \quad (\text{first operand in } T \text{ and } Z), \qquad \mathbf{z}_1 = Y + Xi \quad (\text{second operand in } Y \text{ and } X)$$
      </li>
      <li>Evaluates $\mathbf{w} = \mathbf{z}_2 \mathbin{\text{op}} \mathbf{z}_1$.</li>
      <li>Places the resulting complex vector $(Y' = \operatorname{Re}(\mathbf{w}), X' = \operatorname{Im}(\mathbf{w}))$ into $(Y, X)$.</li>
      <li>Drops the stack by two full levels: previous Register $T$ replicates down into both $Z$ and $T$, following the dyadic stack drop invariant.</li>
    </ul>
  </li>
  <li><strong>Complex Sign Toggle (<code>{{key:CMPLX}} {{key:+/-}}</code>):</strong>
    <ul>
      <li>Simultaneously negates both Real ($Y$) and Imaginary ($X$) components in place.</li>
    </ul>
  </li>
</ol>
</div>

### Stack Register Loading Procedure for Binary Complex Operations
To evaluate $\mathbf{w} = \mathbf{z}_A \mathbin{\text{op}} \mathbf{z}_B$ where $\mathbf{z}_A = a + bi$ and $\mathbf{z}_B = c + di$:
1. Enter the first complex operand $\mathbf{z}_A$:
   `a {{key:ENTER}} b {{key:ENTER}}` $\implies$ Real part $a$ lifts to $Z$, Imaginary part $b$ resides in $Y$.
2. Enter the second complex operand $\mathbf{z}_B$:
   `c {{key:ENTER}} d` $\implies$ $a$ lifts to $T$, $b$ lifts to $Z$, $c$ resides in $Y$, $d$ resides in $X$.
3. Stack alignment verification before execution:
   * **Register T:** $a = \text{Re}(\mathbf{z}_A)$
   * **Register Z:** $b = \text{Im}(\mathbf{z}_A)$
   * **Register Y:** $c = \text{Re}(\mathbf{z}_B)$
   * **Register X:** $d = \text{Im}(\mathbf{z}_B)$
4. Execute: `{{key:CMPLX}} [op]` (where `[op]` is `{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`, or `{{key:yˣ}}`).
5. After execution:
   * **Register Y:** $\text{Re}(\mathbf{w})$
   * **Register X:** $\text{Im}(\mathbf{w})$
   * **Registers Z and T:** Replicated copy of previous Register $T$ ($a$).

---

## Live Stack Proof of Euler's Identity: $e^{i\pi} + 1 = 0$

Leonhard Euler's equation links five of the most profound constants in mathematics: $e, i, \pi, 1,$ and $0$.
$$e^{i\theta} = \cos\theta + i\sin\theta \implies e^{i\pi} = \cos\pi + i\sin\pi = -1 + 0i$$

With the SC-32 set to its baseline **Radians mode (`{{key:RAD}}`)**, execute this proof live on the stack. Represent the pure imaginary exponent $i\pi = 0 + \pi i$ by setting **Real $= 0$ in $Y$** and **Imaginary $= \pi$ in $X$**:

**Keystroke Sequence:** `{{res:sc32_05_complex_numbers_phasors_seq_01:keys}}`

| Step | Keystroke | Register T | Register Z | Register Y (Real) | Register X (Imag) | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Real exponent $0.0$ entered in $Y$ |
| 2 | `{{keycap:π}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.14159265359$ | Imaginary exponent $\pi$ entered in $X$ |
| 3 | {{key:CMPLX}} | $0.0000$ | $0.0000$ | $0.0000$ | $3.14159265359$ | `{{keycap:CMPLX}}` annunciator illuminated |
| 4 | `{{key:eˣ}}` | $0.0000$ | $0.0000$ | **-1.0000000000** | **0.0000000000** | $e^{0 + \pi i} = -1.0 + 0.0i$ |

| Stack Register | Value After `{{key:CMPLX}}` `{{key:eˣ}}` | Mathematical Meaning |
| :---: | :---: | :--- |
| **`T`** | `0.0000000000` | Cleared top register |
| **`Z`** | `0.0000000000` | Cleared third register |
| **`Y`** | **`-1.0000000000`** | Real part $\operatorname{Re}(e^{i\pi}) = -1.0$ |
| **`X`** | **`0.0000000000`** | Imaginary part $\operatorname{Im}(e^{i\pi}) = 0.0$ |

{{blocks:sc32_hero_keynote|SC-32 Scientific Instrument Keynote Portrait}}

*Figure 5.2: The SC-32 scientific instrument executing high-precision complex analysis, preserving certified 12-digit IEEE-754 mantissa accuracy across transcendental evaluating pipelines.*

To complete Euler's Identity $e^{i\pi} + 1 = 0$, add the real unit $+1$:
Enter $+1 + 0i$: `{{res:sc32_05_complex_numbers_phasors_seq_30:keys}}`
* Output: Register $Y = \mathbf{0.0000000000}$, Register $X = \mathbf{0.0000000000}$!

---

## Polar $\leftrightarrow$ Rectangular Transformations in the Complex Domain

Complex numbers are routinely interchanged between Cartesian form ($z = x + iy$) and Polar phasor form ($z = r\angle\theta = r e^{i\theta}$):

$$r = |z| = \sqrt{x^2 + y^2}, \quad \theta = \operatorname{atan2}(y, x)$$
$$x = \operatorname{Re}(z) = r\cos\theta, \quad y = \operatorname{Im}(z) = r\sin\theta$$

| Transformation | Key Sequence | Stack Input ($Y, X$) | Stack Output ($Y, X$) | Mathematical Mapping |
| :--- | :--- | :--- | :--- | :--- |
| **Cartesian to Polar** | `{{key:▸θ,r}}` | $Y = x$ (Real part)<br>$X = y$ (Imaginary part) | $Y = \theta$ (Phase angle)<br>$X = r$ (Modulus / Magnitude) | $r = \sqrt{x^2+y^2}, \quad \theta = \operatorname{atan2}(y, x)$ |
| **Polar to Cartesian** | `{{key:▸y,x}}` | $Y = \theta$ (Phase angle)<br>$X = r$ (Modulus / Magnitude) | $Y = y$ (Imaginary part)<br>$X = x$ (Real part) | $x = r\cos\theta, \quad y = r\sin\theta$ |

### Demonstration: Complex Conversion of $z = 3 + 4i$
1. Load $z = 3 + 4i$: `3 {{key:ENTER}} 4`
2. Convert to Polar: `{{key:▸θ,r}}`
   * **Register X (Magnitude $r$):** **$5.0000000000$**
   * **Register Y (Phase $\theta$):** **$0.9272952180\text{ rad}$** ($53.1301^\circ$)
3. Convert back to Rectangular: `{{key:▸y,x}}`
   * **Register X (Real part):** **$3.0000000000$**
   * **Register Y (Imaginary part):** **$4.0000000000$**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `3 {{key:ENTER}} 4` | $0.0000$ | $0.0000$ | $3.0000$ | $4.0000$ | Rectangular coordinates loaded |
| 2 | `{{key:▸θ,r}}` | $0.0000$ | $0.0000$ | $0.927295$ | **$5.000000$** | Polar conversion: $\theta$ in $Y$, magnitude $r$ in $X$ |
| 3 | `{{key:▸y,x}}` | $0.0000$ | $0.0000$ | $4.000000$ | **$3.000000$** | Rectangular conversion: Real in $X$, Imag in $Y$ |


---

## AC Circuit Analysis: Series & Parallel Complex Impedance


In alternating current electrical networks operating at angular frequency $\omega = 2\pi f$:
* **Resistor ($R$):** $\mathbf{Z}_R = R + 0i\,\Omega$
* **Inductor ($L$):** $\mathbf{Z}_L = 0 + j\omega L\,\Omega = 0 + (\omega L)i$
* **Capacitor ($C$):** $\mathbf{Z}_C = 0 - \frac{j}{\omega C}\,\Omega = 0 - \left(\frac{1}{\omega C}\right)i$

### The Algebraic Trap vs. StackCalc Superpower Showdown

| Challenge / Metric | Algebraic Trap (TI-84 / Infix) | Algebraic Strokes | StackCalc SC-32 Superpower | SC-32 Strokes | Superpower Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **AC Impedance**: $(50+j20) \parallel -j15$ | Mode switch $\to$ `( ( 5 0 + 2 0 i ) ^ -1 + ( - 1 5 i ) ^ -1 ) ^ -1 =` (32 strokes). Real and imaginary parts truncated off-screen; angle hidden in sub-menus. | 32 | **$(Y, X)$ Complex Mode**: Enter real and imag directly; combine via `{{key:x∥y}}` $\to$ Register $Y$ shows Real, Register $X$ shows Imag. Tap `{{key:▸θ,r}}` to see $\|Z\|$ and phase $\phi$ simultaneously! | 18 | **44% fewer strokes + simultaneous $\|Z\|$ and $\phi$** |

### Complex Series Impedance Addition
Two circuit elements are connected in series:
* Element 1: $\mathbf{Z}_1 = 8.0 + 4.0i\,\Omega$ (Resistor + Inductor)
* Element 2: $\mathbf{Z}_2 = 4.0 - 8.0i\,\Omega$ (Resistor + Capacitor)

$$\mathbf{Z}_{\text{series}} = \mathbf{Z}_1 + \mathbf{Z}_2 = (8.0 + 4.0) + (4.0 - 8.0)i = 12.0 - 4.0i\,\Omega$$

**Keystroke Sequence:** `{{res:sc32_05_complex_numbers_phasors_seq_02:keys}}`

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `4 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $4.0000$ | $4.0000$ | Real part of $\mathbf{Z}_2$ pushed |
| 2 | `8 {{key:+/-}} {{key:ENTER}}` | $0.0000$ | $4.0000$ | $-8.0000$ | $-8.0000$ | Imag part of $\mathbf{Z}_2$ pushed |
| 3 | `8 {{key:ENTER}}` | $4.0000$ | $-8.0000$ | $8.0000$ | $8.0000$ | Real part of $\mathbf{Z}_1$ pushed |
| 4 | `4` | **$4.0000$** | **$-8.0000$** | **$8.0000$** | **$4.0000$** | Complete 4-register setup |
| 5 | `{{key:CMPLX}} {{key:+}}` | $4.0000$ | $4.0000$ | **$12.000000$** | **$-4.000000$** | $\mathbf{Z}_{\text{total}} = 12.0 - 4.0i\,\Omega$ |

The display confirms **Real $= 12.0\,\Omega$ in $Y$** and **Imaginary $= -4.0\,\Omega$ in $X$**.

---

### Parallel Complex Impedance via Stack Admittance
When two complex impedances are connected in parallel, the equivalent impedance is governed by the reciprocal sum of complex admittances:

$$\mathbf{Y}_{\text{parallel}} = \mathbf{Y}_1 + \mathbf{Y}_2 = \frac{1}{\mathbf{Z}_1} + \frac{1}{\mathbf{Z}_2} \implies \mathbf{Z}_{\text{parallel}} = \frac{1}{\mathbf{Y}_{\text{parallel}}}$$

Consider two parallel branches:
* Branch 1: $\mathbf{Z}_1 = 20.0 + 15.0i\,\Omega$
* Branch 2: $\mathbf{Z}_2 = 10.0 - 25.0i\,\Omega$

**Step 1: Compute Admittance $\mathbf{Y}_1 = 1/\mathbf{Z}_1$:**
Keystrokes: `{{res:sc32_05_complex_numbers_phasors_seq_03:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_03:value}}`**
* Register $Y$ (Real): **$0.032000\,\text{S}$**
* Register $X$ (Imag): **$-0.024000\,\text{S}$**
Store into memory: `{{key:x⇄y}} {{key:STO}} 1 {{key:x⇄y}} {{key:STO}} 2` (Reg 1 = Imag, Reg 2 = Real).

**Step 2: Compute Admittance $\mathbf{Y}_2 = 1/\mathbf{Z}_2$:**
Keystrokes: `{{res:sc32_05_complex_numbers_phasors_seq_04:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_04:value}}`**
* Register $Y$ (Real): **$0.013793\,\text{S}$**
* Register $X$ (Imag): **$+0.034483\,\text{S}$**

**Step 3: Sum Admittances:**
Load $\mathbf{Y}_1$ into $(T, Z)$: `{{key:RCL}} 2 {{key:ENTER}} {{key:RCL}} 1 {{key:CMPLX}} {{key:+}}`
* Register $Y$ (Real): **$0.045793\,\text{S}$**
* Register $X$ (Imag): **$+0.010483\,\text{S}$**

**Step 4: Invert Total Admittance:**
Keystrokes: `{{res:sc32_05_complex_numbers_phasors_seq_05:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_05:value}}`**
* **Register Y (Real):** **$20.7516\,\Omega$**
* **Register X (Imaginary):** **$-4.7507\,\Omega$**

$$\mathbf{Z}_{\text{parallel}} = 20.7516 - 4.7507i\,\Omega$$

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `20 {{key:ENTER}} 15 {{key:CMPLX}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.032000$ | $-0.024000$ | Branch 1 admittance $\mathbf{Y}_1$ in Siemens |
| 2 | `{{key:x⇄y}} {{key:STO}} 1 {{key:x⇄y}} {{key:STO}} 2` | $0.0000$ | $0.0000$ | $0.032000$ | $-0.024000$ | Store $\mathbf{Y}_1$ in Reg 1 (Imag) and Reg 2 (Real) |
| 3 | `10 {{key:ENTER}} 25 {{key:+/-}} {{key:CMPLX}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.013793$ | $0.034483$ | Branch 2 admittance $\mathbf{Y}_2$ in Siemens |
| 4 | `{{key:RCL}} 2 {{key:ENTER}} {{key:RCL}} 1 {{key:CMPLX}} {{key:+}}` | $0.013793$ | $0.013793$ | $0.045793$ | $0.010483$ | Sum admittances: $\mathbf{Y}_{\text{parallel}} = \mathbf{Y}_1 + \mathbf{Y}_2$ |
| 5 | `{{key:CMPLX}} {{key:1/x}}` | $0.013793$ | $0.013793$ | **$20.7516$** | **$-4.7507$** | Invert admittance: $\mathbf{Z}_{\text{parallel}} = 20.75 - 4.75i\,\Omega$ |

---

## RF Transmission Lines, Reflection Coefficient ($\Gamma$), VSWR & Smith Chart

In radio-frequency (RF) and microwave transmission lines, an arbitrary load impedance $\mathbf{Z}_L = R_L + j X_L$ connected to a transmission line of characteristic impedance $Z_0$ (typically $50\,\Omega$) produces reflections.

<div class="admonition note">
<p class="admonition-title">RF Transmission Line Parameter Formulas</p>
<ol>
  <li><strong>Voltage Reflection Coefficient:</strong>
    $$\mathbf{\Gamma} = \frac{\mathbf{Z}_L - Z_0}{\mathbf{Z}_L + Z_0}$$
  </li>
  <li><strong>Normalized Load Impedance:</strong>
    $$\mathbf{z} = \frac{\mathbf{Z}_L}{Z_0} = r + jx$$
  </li>
  <li><strong>Voltage Standing Wave Ratio (VSWR):</strong>
    $$\text{VSWR} = \frac{1 + |\mathbf{\Gamma}|}{1 - |\mathbf{\Gamma}|}$$
  </li>
  <li><strong>Return Loss ($RL$):</strong>
    $$RL = -20 \log_{10} |\mathbf{\Gamma}|\quad (\text{in dB})$$
  </li>
  <li><strong>Mismatch Loss ($ML$):</strong>
    $$ML = -10 \log_{10} \left(1 - |\mathbf{\Gamma}|^2\right)\quad (\text{in dB})$$
  </li>
</ol>
</div>

### Grounded Case: Antenna Feedline Mismatch
An antenna with measured feedpoint impedance $\mathbf{Z}_L = 75.0 + 40.0i\,\Omega$ is connected to a standard $Z_0 = 50.0\,\Omega$ coaxial cable.

**Step 1: Compute Complex Reflection Coefficient $\mathbf{\Gamma}$:**
$$\mathbf{\Gamma} = \frac{(75 + 40i) - 50}{(75 + 40i) + 50} = \frac{25 + 40i}{125 + 40i}$$

1. Load denominator ($125 + 40i$) into $(T, Z)$: `125 {{key:ENTER}} 40 {{key:ENTER}}`
2. Load numerator ($25 + 40i$) into $(Y, X)$: `25 {{key:ENTER}} 40`
3. Execute complex division: `{{key:CMPLX}} {{key:÷}}`
   * **Register Y (Real):** **$0.276274$**
   * **Register X (Imag):** **$0.231713$**
   $$\mathbf{\Gamma} = 0.2763 + 0.2317i$$

**Step 2: Reflection Magnitude $|\Gamma|$ & Phase Angle:**
Press `{{key:▸θ,r}}`
* **Register X ($|\Gamma|$):** **$0.360578$**
* **Register Y ($\theta_\Gamma$):** **$0.697072\text{ rad}$** ($39.94^\circ$)

**Step 3: Voltage Standing Wave Ratio (VSWR):**
$$\text{VSWR} = \frac{1 + 0.360578}{1 - 0.360578} = \frac{1.360578}{0.639422} = \mathbf{2.1278}$$
Keystrokes: `{{res:sc32_05_complex_numbers_phasors_seq_06:keys}}`$\implies$ **$2.1278$**.

**Step 4: Return Loss (dB):**
$$\text{RL} = -20 \log_{10}(0.360578) = \mathbf{8.86\text{ dB}}$$
Keystrokes: `{{res:sc32_05_complex_numbers_phasors_seq_07:keys}}`$\implies$ **$8.8601\text{ dB}$**.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `125 {{key:ENTER}} 40 {{key:ENTER}}` | $0.0000$ | $125.0000$ | $40.0000$ | $40.0000$ | Denominator $(Z_L + Z_0)$ pushed |
| 2 | `25 {{key:ENTER}} 40` | $125.0000$ | $40.0000$ | $25.0000$ | $40.0000$ | Numerator $(Z_L - Z_0)$ loaded into $(Y, X)$ |
| 3 | `{{key:CMPLX}} {{key:÷}}` | $125.0000$ | $125.0000$ | **$0.276274$** | **$0.231713$** | Reflection coefficient $\mathbf{\Gamma} = 0.2763 + 0.2317i$ |
| 4 | `{{key:▸θ,r}}` | $125.0000$ | $125.0000$ | $0.697072$ | **$0.360578$** | Polar: Phase $\theta = 39.94^\circ$, magnitude $|\mathbf{\Gamma}| = 0.3606$ |
| 5 | `1 {{key:ENTER}} {{key:LASTX}} {{key:+}} 1 {{key:ENTER}} {{key:LASTX}} {{key:-}} {{key:÷}}` | $0.0000$ | $0.0000$ | $1.360578$ | **$2.1278$** | VSWR $= (1+|\mathbf{\Gamma}|)/(1-|\mathbf{\Gamma}|) = 2.1278$ |

---

## Complex Powers, Roots of Unity & de Moivre's Theorem

Abraham de Moivre's theorem provides the foundation for finding $n$-th roots and arbitrary powers of complex numbers:

$$z = r e^{i\theta} \implies z^n = r^n e^{i n \theta} = r^n (\cos(n\theta) + i\sin(n\theta))$$
$$\sqrt[n]{z} = r^{1/n} \left[\cos\left(\frac{\theta + 2k\pi}{n}\right) + i\sin\left(\frac{\theta + 2k\pi}{n}\right)\right], \quad k = 0, 1, \dots, n-1$$

### Complex General Power: $(1 + i)^{(1 - i)}$
On the SC-32, the binary complex power operator `{{key:CMPLX}} {{key:yˣ}}` evaluates general complex powers $z_2^{z_1}$:

1. Load base $z_2 = 1 + i$ into $(T, Z)$: `1 {{key:ENTER}} 1 {{key:ENTER}}`
2. Load exponent $z_1 = 1 - i$ into $(Y, X)$: `1 {{key:ENTER}} 1 {{key:+/-}}`
3. Execute: `{{key:CMPLX}} {{key:yˣ}}`
   * **Register Y (Real):** **$2.818047$**
   * **Register X (Imag):** **$1.317855$**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1 {{key:ENTER}} 1 {{key:ENTER}}` | $0.0000$ | $1.0000$ | $1.0000$ | $1.0000$ | Base $z_2 = 1 + i$ loaded into $(T, Z)$ |
| 2 | `1 {{key:ENTER}} 1 {{key:+/-}}` | $1.0000$ | $1.0000$ | $1.0000$ | $-1.0000$ | Exponent $z_1 = 1 - i$ loaded into $(Y, X)$ |
| 3 | `{{key:CMPLX}} {{key:yˣ}}` | $1.0000$ | $1.0000$ | **$2.818047$** | **$1.317855$** | General complex power $z_2^{z_1}$ evaluated |

---

## Complex Numbers & Phasor Architecture Notes

### Gaussian Stack Representation & Vector Duality
In higher mathematics and engineering education, complex numbers often suffer from an algebraic disconnect when treated purely as formal polynomials $(a + bi)(c + di)$. The SC-32's $(Y, X)$ Gaussian plane convention grounds complex values in geometric reality {{cite:hp15c1982}}. By allocating the complex number across two physical registers—$Y = \text{Real}$ and $X = \text{Imaginary}$—complex addition operates directly as 2D vector summation, while complex multiplication executes simultaneous radial scaling ($r_1 \cdot r_2$) and angular rotation ($\theta_1 + \theta_2$).

### Live Verification of Euler's Identity
Evaluating Euler's Identity $e^{i\pi} + 1 = 0$ provides a definitive benchmark for complex transcendental accuracy. Keying `{{res:sc32_05_complex_numbers_phasors_seq_31:keys}}` evaluates $e^{i\pi}$, yielding Register $Y = -1.0000000000$ (Real) and Register $X = 0.0000000000$ (Imaginary). Adding unity ($1$ `{{key:+}}`) collapses the real axis to zero, demonstrating exact floating-point balance without truncation artifacts.

### Reactive Impedance & Phasor Synthesis
In alternating current network analysis, sinusoidal voltages and currents are represented as rotating phasors. Inductive reactance $+j\omega L$ maps natively to a positive imaginary value in Register $X$, while capacitive reactance $-j/(\omega C)$ maps to a negative imaginary value. Series resonance and parallel tank circuit impedances evaluate through `{{key:CMPLX}} {{key:+}}`, `{{key:CMPLX}} {{key:1/x}}`, and `{{key:x∥y}}`, converting multi-term differential AC equations into deterministic stack transitions.

### Transient Prefix Architecture & Stack Drop Dynamics
Unlike calculators that force the instrument into a modal complex environment—distorting basic arithmetic and keyboard layouts—the SC-32 employs the transient prefix `{{key:CMPLX}}`. Complex operations execute as localized vector transforms on the existing 4-level stack. In binary complex evaluations $(z_2 \text{ op } z_1)$, the four registers $(T, Z, Y, X)$ collapse into two, with previous Register $T$ replicating down into $Z$ and $T$. This allows immediate chaining of scalar factors or successive complex impedances without re-keying. Mantissa inspection via `{{key:SHOW}}` reveals full IEEE-754 precision without cosmetic rounding.

---

## Diagnostic Checkpoints & Singularity Handling

> [!CHECKPOINT]
> **Diagnostic Checkpoint 5.1: Complex Prefix Annunciator Arming**  
> Press {{key:CMPLX}}. The LCD annunciator bar displays `{{key:CMPLX}}`. If pressed by mistake, press `{{key:C}}` to cancel without displacing or clearing stack values.

> [!CHECKPOINT]
> **Diagnostic Checkpoint 5.2: Complex Division Operand Alignment**  
> When calculating $\mathbf{z}_{\text{num}} / \mathbf{z}_{\text{den}}$:
> * The **denominator** $\mathbf{z}_{\text{den}}$ must be loaded into Registers $(T, Z)$ first.
> * The **numerator** $\mathbf{z}_{\text{num}}$ must be loaded into Registers $(Y, X)$ second.
> * If the resulting quotient is inverted, recall operands using `{{key:LASTX}}` or swap pairs.

> [!CHECKPOINT]
> **Diagnostic Checkpoint 5.3: Singularity Handling (Division by Zero Complex)**  
> Attempting complex division by $0 + 0i$ (`0 {{key:ENTER}} 0`) immediately halts execution and triggers `Error 02: DIVIDE BY 0`. The stack remains unmodified.

> [!CHECKPOINT]
> **Diagnostic Checkpoint 5.4: Hyperbolic and Inverse Trig Boundary Guards**  
> Under SC-32 firmware specifications, complex domain operations are supported for algebraic powers, roots, exponentials, logs, and direct trigonometric functions (`SIN`, `COS`, `TAN`). Attempting {{key:CMPLX}} {{key:ASIN}}` or {{key:CMPLX}} {{key:HYP}}` raises `Error 01: INVALID DATA`, directing the user to logarithmic conformal mappings.

## Engineering Design Briefing: Precision Audio Crossover & RF Antenna Synthesis (Problems 5.1 through 5.40)

<div class="admonition warning">
<p class="admonition-title">Inside-Out Stack Architecture: Algebraic Trap vs. RPN Shortcut — AC Circuit Phasors &amp; Complex Impedance Matching</p>
<p><strong>The Algebraic Parenthesis Trap:</strong> In AC electrical engineering, determining the equivalent impedance of a parallel RLC branch $Z_{\text{eq}} = \frac{Z_1 Z_2}{Z_1 + Z_2}$ requires evaluating complex numbers in polar or rectangular form {{cite:horowitz2015}}:</p>
<pre><code>Z_eq = ( ( 50 + 25i ) * ( 10 - 40i ) ) / ( ( 50 + 25i ) + ( 10 - 40i ) )</code></pre>
<p>On algebraic scientific calculators, complex arithmetic requires typing clumsy multi-character strings with explicit imaginary unit <code>i</code> keys and double parentheses for every complex operand. A single misplaced parenthesis scrambles real resistance with imaginary reactance, producing erroneous phase angles that can destroy prototype RF amplifier stages {{cite:parker2019}}.</p>
<p><strong>The RPN Stack Shortcut:</strong> On the SC-32, the $(Y, X)$ stack allocation represents the two-dimensional complex plane natively ($Y = \text{Real}, X = \text{Imaginary}$) {{cite:hp15c1982}}. With the dedicated complex evaluator <code>{{key:CMPLX}}</code>, complex multiplication, division, reciprocals, and square roots execute in place. Furthermore, the parallel operator <code>{{key:x∥y}}</code> solves parallel complex impedances in a single keystroke, eliminating 18 algebraic button presses and completely preventing real/imaginary crosstalk.</p>
</div>

Every problem below includes real-world engineering context, mathematical governing equations, complete keystroke sequences, and full 4-level stack state tables ($T, Z, Y, X$).

---

### Problem 5.1: Complex Conjugate Multiplication & Modulus Squared
**Theoretical Context:** For $z = 6 + 8i$, compute the complex conjugate product $z \cdot z^* = |z|^2$:
$$z^* = 6 - 8i \implies z \cdot z^* = 6^2 + 8^2 = 36 + 64 = 100 + 0i$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_08:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_08:value}}`**

Key `6 {{key:ENTER}} 8 {{key:ENTER}}` to position $z = 6 + 8i$ across the stack, then enter the conjugate pair `6 {{key:ENTER}} 8 {{key:+/-}}`, lifting the stack to $(T:6, Z:8, Y:6, X:-8)$. Striking `{{key:CMPLX}} {{key:×}}` multiplies the conjugate pair and drops the stack, leaving $(T:6, Z:6, Y:100.0000, X:0.0000)$.

Result: **$\text{Real} = 100.0$, $\text{Imag} = 0.0$**.

---

### Problem 5.2: Complex Square Root of Pure Imaginary Unit: $\sqrt{i}$
**Theoretical Context:** Evaluate $\sqrt{i} = \sqrt{0 + 1i} = e^{i\pi/4} = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}i \approx 0.707107 + 0.707107i$:

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_09:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_09:value}}`**

Enter the pure imaginary unit $0 + 1i$ with `0 {{key:ENTER}} 1`, placing Real in $Y$ and Imag in $X$ $(T:0, Z:0, Y:0, X:1)$. Press `{{key:CMPLX}} {{key:√x}}` to evaluate the complex square root in place, leaving $(T:0, Z:0, Y:0.707107, X:0.707107)$.

Result: **$0.707107 + 0.707107i$**.

---

### Problem 5.3: Principal Value of Natural Logarithm of Negative Real: $\ln(-5)$
**Theoretical Context:** In complex analysis, $\ln(z) = \ln|z| + i \operatorname{Arg}(z)$. For $z = -5 + 0i$, $|z| = 5$ and $\operatorname{Arg}(z) = \pi$:
$$\ln(-5) = \ln(5) + i\pi \approx 1.609438 + 3.141593i$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_10:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_10:value}}`**

Key `5 {{key:+/-}} {{key:ENTER}} 0` to load $z = -5 + 0i$ into $(Y, X)$. Pressing `{{key:CMPLX}} {{key:LN}}` evaluates the principal complex logarithm, transitioning the stack to $(T:0, Z:0, Y:1.609438, X:3.141593)$.

Result: **$1.609438 + 3.141593i$**.

---

### Problem 5.4: Complex Reciprocal of High-Q Inductor Admittance
**Theoretical Context:** An RF inductor has impedance $\mathbf{Z}_L = 0.5 + 120.0i\,\Omega$. Calculate its complex admittance $\mathbf{Y} = 1/\mathbf{Z}$:
$$\mathbf{Y} = \frac{1}{0.5 + 120i} = \frac{0.5 - 120i}{0.5^2 + 120^2} = \frac{0.5 - 120i}{0.25 + 14400} = 3.4722 \times 10^{-5} - 8.3333 \times 10^{-3}i\,\text{S}$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_11:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_11:value}}`**

Load the inductor impedance via `0.5 {{key:ENTER}} 120`, establishing $(T:0, Z:0, Y:0.5, X:120)$. Press `{{key:CMPLX}} {{key:1/x}}` to invert the complex phasor into admittance in Siemens, arriving at $(T:0, Z:0, Y:3.4722 \times 10^{-5}, X:-8.3333 \times 10^{-3})$.

Result: **$3.4722 \times 10^{-5} - 8.3333 \times 10^{-3}i\,\text{S}$**.

---

### Problem 5.5: Series RLC Circuit Total Impedance
**Electrical Context:** At angular frequency $\omega = 1,000\text{ rad/s}$, a series circuit has $R = 50\,\Omega$, $L = 80\text{ mH}$ ($X_L = \omega L = 80\,\Omega$), and $C = 20\,\mu\text{F}$ ($X_C = 1/(\omega C) = 50\,\Omega$):
$$\mathbf{Z} = R + j(X_L - X_C) = 50 + j(80 - 50) = 50 + 30i\,\Omega$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_12:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_12:value}}`**

Load the series branch $\mathbf{Z}_1$ with `50 {{key:ENTER}} 80 {{key:ENTER}}`, then key $\mathbf{Z}_2$ with `0 {{key:ENTER}} 50 {{key:+/-}}`, priming the 4-level stack to $(T:50, Z:80, Y:0, X:-50)$. Tap `{{key:CMPLX}} {{key:+}}` to execute dyadic phasor addition, leaving $(T:50, Z:50, Y:50.0000, X:30.0000)$.

Result: **$50.0 + 30.0i\,\Omega$**.

---

### Problem 5.6: RLC Circuit Current Phasor via Ohm's Law
**Electrical Context:** The circuit from Problem 5.5 ($\mathbf{Z} = 50 + 30i\,\Omega$) is driven by voltage $\mathbf{V} = 120 + 0i\text{ V}$. Find current phasor $\mathbf{I} = \mathbf{V} / \mathbf{Z}$:
$$\mathbf{I} = \frac{120}{50 + 30i} = \frac{120(50 - 30i)}{2500 + 900} = \frac{6000 - 3600i}{3400} = 1.7647 - 1.0588i\text{ A}$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_13:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_13:value}}`**

Enter denominator $\mathbf{Z}$ via `50 {{key:ENTER}} 30 {{key:ENTER}}` followed by numerator $\mathbf{V}$ via `120 {{key:ENTER}} 0`, giving $(T:50, Z:30, Y:120, X:0)$. Press `{{key:CMPLX}} {{key:÷}}` to evaluate complex Ohm's law, yielding current phasor $(T:50, Z:50, Y:1.764706, X:-1.058824)$.

Result: **$1.7647 - 1.0588i\text{ Amperes}$** ($|\mathbf{I}| = 2.058\text{ A}\angle -30.96^\circ$).

---

### Problem 5.7: AC Apparent, Real, and Reactive Power Complex Vector
**Electrical Context:** Complex apparent power is $\mathbf{S} = \mathbf{V} \cdot \mathbf{I}^*$. For $\mathbf{V} = 120 + 0i\text{ V}$ and $\mathbf{I} = 1.7647 - 1.0588i\text{ A} \implies \mathbf{I}^* = 1.7647 + 1.0588i\text{ A}$:
$$\mathbf{S} = 120 \times (1.7647 + 1.0588i) = 211.7647 + 127.0560i\text{ VA}$$
Real power $P = 211.76\text{ Watts}$, Reactive power $Q = 127.06\text{ VAR}$.

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_14:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_14:value}}`**

Enter voltage $\mathbf{V}$ via `120 {{key:ENTER}} 0 {{key:ENTER}}` and conjugate current $\mathbf{I}^*$ via `1.764706 {{key:ENTER}} 1.058824`, loading $(T:120, Z:0, Y:1.764706, X:1.058824)$. Press `{{key:CMPLX}} {{key:×}}` to evaluate apparent power vector $\mathbf{S}$, resulting in $(T:120, Z:120, Y:211.7647, X:127.0589)$.

Result: **$P = 211.76\text{ W}, Q = 127.06\text{ VAR}$**.

---

### Problem 5.8: Power Factor from Complex Apparent Power
**Power Engineering Context:** For complex power $\mathbf{S} = 211.7647 + 127.0589i\text{ VA}$, compute magnitude $|\mathbf{S}|$ and power factor $\cos\theta$:
$$|\mathbf{S}| = \sqrt{P^2 + Q^2} \approx 247.0\text{ VA}, \quad \text{PF} = \frac{P}{|\mathbf{S}|} = \frac{211.7647}{247.0588} \approx 0.8572$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_15:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_15:value}}`**

Key `211.7647 {{key:ENTER}} 127.0589` into $(Y, X)$, then tap `{{key:▸θ,r}}` to convert to polar form $(T:0, Z:0, Y:0.540420, X:247.0588)$, revealing phase angle in $Y$ and apparent power $|\mathbf{S}|$ in $X$. Tap `{{key:x⇄y}} {{key:COS}}` to extract the lagging power factor, ending with $(T:0, Z:0, Y:247.0588, X:0.857187)$.

Result: **$\text{PF} = 0.8572\text{ (lagging)}$**.

---

### Problem 5.9: Two-Port S-Parameter Reflection Coefficient Transformation
**RF Engineering Context:** S-parameter $S_{11} = 0.25 - 0.40i$. Calculate return loss in dB:
$$|S_{11}| = \sqrt{0.25^2 + (-0.40)^2} = \sqrt{0.0625 + 0.1600} = \sqrt{0.2225} \approx 0.471699$$
$$\text{RL} = -20 \log_{10}(0.471699) = 6.527\text{ dB}$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_16:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_16:value}}`**

Load $S_{11}$ via `0.25 {{key:ENTER}} 0.40 {{key:+/-}}`, then convert to polar magnitude with `{{key:▸θ,r}}`, leaving $(T:0, Z:0, Y:-1.012197, X:0.471699)$. Complete the return loss calculation with `{{keycap:LOG}} 20 {{key:×}} {{key:+/-}}`, producing $(T:0, Z:0, Y:-1.012197, X:6.5269)$.

Result: **$6.5269\text{ dB}$**.

---

### Problem 5.10: Quarter-Wave Transmission Line Impedance Inverter
**RF Context:** A quarter-wave transformer of characteristic impedance $Z_{\text{line}} = 70.71\,\Omega$ terminates in load $Z_L = 100 + 0i\,\Omega$. Calculate input impedance $Z_{\text{in}} = Z_{\text{line}}^2 / Z_L$:
$$Z_{\text{in}} = \frac{70.7107^2}{100.0} = \frac{5000.0}{100.0} = 50.00\,\Omega$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_17:keys}}`$\implies$ **$50.0000\,\Omega$**. Perfect match to a $50\,\Omega$ line.

> **Named RPN Stack Idiom: *The Inside-Out Radical & Transmission Line Pipeline*** — Square characteristic impedance in place and divide load resistance directly without scratchpad memory {{cite:horowitz2015,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `70.7107` — Enter line characteristic impedance ($Z_0 = 70.7107\,\Omega$) into $X$.
2. `{{key:x²}}` — Square characteristic impedance ($Z_0^2 = 5000.00\,\Omega^2$).
3. `100` `{{key:÷}}` — Divide by load resistance ($Z_L = 100.0\,\Omega$), yielding matched input impedance $Z_{\text{in}} = \mathbf{50.00\,\Omega}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `70.7107` | $0.0000$ | $0.0000$ | $0.0000$ | $70.7107$ | Enter line characteristic impedance $Z_0$ |
| 2 | `{{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $5000.0031$ | Square characteristic impedance $Z_0^2$ |
| 3 | `100 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$50.0000$** | Divide by load resistance $Z_L$; matched $Z_{\text{in}} = 50.0\,\Omega$ |

Result: **$50.0000\,\Omega$**.

---

### Problem 5.11: Complex Cube Roots of $-8$: $\sqrt[3]{-8}$
**Theoretical Context:** Solve $z^3 = -8 = 8 e^{i\pi}$. Principal root:
$$z_0 = 8^{1/3} e^{i\pi/3} = 2 \left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right) = 2(0.5 + 0.866025i) = 1.0 + 1.732051i$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_18:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_18:value}}`**
(Using $z_2 = -8$, exponent $z_1 = 1/3 = 0.3333333333$):
Keystrokes: `{{res:sc32_05_complex_numbers_phasors_seq_19:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_19:value}}`**

Load base $z_2 = -8 + 0i$ with `8 {{key:+/-}} {{key:ENTER}} 0 {{key:ENTER}}`, then enter exponent $1/3$ via `0.333333333333 {{key:ENTER}} 0`, establishing $(T:-8, Z:0, Y:0.333333, X:0)$. Tap `{{key:CMPLX}} {{key:yˣ}}` to extract the principal complex cube root, yielding $(T:-8, Z:-8, Y:1.000000, X:1.732051)$.

Result: **$1.000000 + 1.732051i$**.

---

### Problem 5.12: Second Root of Unity from de Moivre
**Theoretical Context:** From Problem 5.11, the real root is $z_1 = -2.0 + 0.0i$, and the third root is $z_2 = 1.0 - 1.732051i$. Confirm $z_1^3$:
Keystrokes: `{{res:sc32_05_complex_numbers_phasors_seq_20:keys}}`$\implies$ **$-8.0000 + 0.0000i$**.

Enter the candidate root $z_1 = -2.0 + 0.0i$ into $(T, Z)$ and the power $3.0 + 0.0i$ into $(Y, X)$ via `2 {{key:+/-}} {{key:ENTER}} 0 {{key:ENTER}} 3 {{key:ENTER}} 0`, creating $(T:-2, Z:0, Y:3, X:0)$. Executing `{{key:CMPLX}} {{key:yˣ}}` confirms $(-2+0i)^3 = -8.0 + 0.0i$, leaving $(T:-2, Z:-2, Y:-8.0000, X:0.0000)$.

Result: **$-8.0000 + 0.0000i$**.

---

### Problem 5.13: Complex Sine Evaluation: $\sin(1 + 2i)$
**Theoretical Context:** $\sin(x + iy) = \sin x \cosh y + i \cos x \sinh y$.
For $x = 1.0\text{ rad}, y = 2.0$:
$$\sin(1) \approx 0.841471, \quad \cosh(2) \approx 3.762196 \implies \text{Real} = 0.841471 \times 3.762196 = 3.165779$$
$$\cos(1) \approx 0.540302, \quad \sinh(2) \approx 3.626860 \implies \text{Imag} = 0.540302 \times 3.626860 = 1.959601$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_21:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_21:value}}`**

Key `1 {{key:ENTER}} 2` to load $1 + 2i$ into $(Y, X)$ $(T:0, Z:0, Y:1, X:2)$. Press `{{key:CMPLX}} {{key:SIN}}` to evaluate complex sine in place, producing $(T:0, Z:0, Y:3.165779, X:1.959601)$.

Result: **$3.165779 + 1.959601i$**.

---

### Problem 5.14: Complex Cosine Evaluation: $\cos(1 + 2i)$
**Theoretical Context:** $\cos(x + iy) = \cos x \cosh y - i \sin x \sinh y$.
$$\text{Real} = \cos(1)\cosh(2) = 0.540302 \times 3.762196 = 2.032723$$
$$\text{Imag} = -\sin(1)\sinh(2) = -0.841471 \times 3.626860 = -3.051898$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_22:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_22:value}}`**

Enter $1 + 2i$ with `1 {{key:ENTER}} 2` $(T:0, Z:0, Y:1, X:2)$ and tap `{{key:CMPLX}} {{key:COS}}`, yielding $(T:0, Z:0, Y:2.032723, X:-3.051898)$.

Result: **$2.032723 - 3.051898i$**.

---

### Problem 5.15: Fundamental Identity Verification: $\sin^2(z) + \cos^2(z) = 1$
**Theoretical Context:** Using results from 5.13 and 5.14, square both complex numbers and add them:
$$\sin^2(1+2i) + \cos^2(1+2i) = 1.000000 + 0.000000i$$
Verified live on the stack with zero drift!

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Load Complex Trigonometric Operand:** Key in $\operatorname{Re}(\sin z)$ and $\operatorname{Im}(\sin z)$ onto the operational stack.
2. `{{key:CMPLX}}` `{{key:x²}}` — Square complex sine in place; $(\sin z)^2$ occupies Registers $(Y, X)$.
3. **Load Complex Cosine Component:** Key in $\operatorname{Re}(\cos z)$ and $\operatorname{Im}(\cos z)$ into $(T, Z)$ and square in place via `{{key:CMPLX}}` `{{key:x²}}`.
4. `{{key:CMPLX}}` `{{key:+}}` — Sum both squared complex phasors; the fundamental identity collapses to $1.000000 + 0.000000i$ with zero numerical drift.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `3.165779 {{key:ENTER}} 1.959601` | $0.0000$ | $0.0000$ | $3.165779$ | $1.959601$ | Load $\sin(1+2i)$ from Problem 5.13 |
| 2 | `{{key:CMPLX}} {{key:x²}}` | $0.0000$ | $0.0000$ | $6.182115$ | $12.407147$ | Square complex sine $(\sin z)^2$ |
| 3 | `2.032723 {{key:ENTER}} 3.051898 {{key:+/-}}` | $6.182115$ | $12.407147$ | $2.032723$ | $-3.051898$ | Load $\cos(1+2i)$ from Problem 5.14 |
| 4 | `{{key:CMPLX}} {{key:x²}}` | $6.182115$ | $12.407147$ | $-5.182115$ | $-12.407147$ | Square complex cosine $(\cos z)^2$ |
| 5 | `{{key:CMPLX}} {{key:+}}` | $6.182115$ | $6.182115$ | **$1.000000$** | **$0.000000$** | Sum squares: $\sin^2 z + \cos^2 z = 1 + 0i$ |

Result: **$1.000000 + 0.000000i$**.

---

### Problem 5.16: Butterworth 2nd-Order Low-Pass Filter Transfer Function
**Acoustics Context:** At cutoff frequency $f_c = 2,500\text{ Hz}$, normalized frequency is $s = j\omega / \omega_c = 0 + 1i$. The 2nd-order Butterworth denominator is $B_2(s) = s^2 + \sqrt{2} s + 1$:
$$s^2 = -1 + 0i, \quad \sqrt{2} s = 0 + 1.414214i \implies B_2(j) = (-1 + 1) + 1.414214i = 0 + 1.414214i$$
$$H(j) = \frac{1}{0 + 1.414214i} = 0 - \frac{1}{\sqrt{2}}i = 0 - 0.707107i \implies |H| = \frac{1}{\sqrt{2}} \approx -3.01\text{ dB}$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_23:keys}}`$\implies$ **$0.000000 - 0.707107i$**.

Load the normalized frequency polynomial $B_2(j) = 0 + 1.414214i$ into $(Y, X)$ via `0 {{key:ENTER}} 1.414214` $(T:0, Z:0, Y:0, X:1.414214)$. Inverting via `{{key:CMPLX}} {{key:1/x}}` directly evaluates the frequency response $H(j) = 0 - 0.707107i$, leaving $(T:0, Z:0, Y:0.000000, X:-0.707107)$.

Result: **$0.000000 - 0.707107i$** ($|H| = 0.707107 \implies \mathbf{-3.01\text{ dB}}$).

---

### Problem 5.17: Linkwitz-Riley 4th-Order Filter (Cascaded Butterworth)
**Audio Context:** $H_{\text{LR4}}(s) = [H_{\text{Butter2}}(s)]^2 = (-0.707107i)^2 = -0.500000 + 0.000000i$.
Magnitude $|H| = 0.5000 \implies 20 \log_{10}(0.5) = -6.02\text{ dB}$ (the acoustic crossover standard).

#### Keystrokes:
`0 {{key:ENTER}} 0.707107 {{key:+/-}} {{key:CMPLX}} {{key:x²}}` $\rightarrow$ Real: **`-0.500000`**, Imag: **`0.000000`**.

#### Stack Trace Table:
| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0 {{key:ENTER}} 0.707107 {{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-0.707107$ | Load Butterworth response $0 - 0.707107i$ |
| 2 | `{{key:CMPLX}} {{key:x²}}` | $0.0000$ | $0.0000$ | **$-0.500000$** | **$0.000000$** | Evaluate $[H_{\text{Butter2}}]^2$; Real in $Y$, Imag in $X$ |
| 3 | `{{key:x⇄y}} {{key:ABS}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.500000$ | Inspect Real component magnitude $|H| = 0.5$ |
| 4 | `{{key:LOG}} 20 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$-6.020600$** | Calculate $-6.02\text{ dB}$ acoustic crossover attenuation |

Result: **$-0.500000 + 0.000000i$** ($|H| = 0.5000 \implies \mathbf{-6.02\text{ dB}}$).

---

### Problem 5.18: Smith Chart Bilinear Transformation
**Microwave Context:** Compute normalized load $z = r + jx$ from reflection coefficient $\Gamma = 0.2 + 0.4i$:
$$z = \frac{1 + \Gamma}{1 - \Gamma} = \frac{1 + 0.2 + 0.4i}{1 - 0.2 - 0.4i} = \frac{1.2 + 0.4i}{0.8 - 0.4i}$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_24:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_24:value}}`**

Load denominator $1 - \Gamma = 0.8 - 0.4i$ via `0.8 {{key:ENTER}} 0.4 {{key:+/-}} {{key:ENTER}}` and numerator $1 + \Gamma = 1.2 + 0.4i$ via `1.2 {{key:ENTER}} 0.4`, loading $(T:0.8, Z:-0.4, Y:1.2, X:0.4)$. Striking `{{key:CMPLX}} {{key:÷}}` evaluates the Möbius transformation to $z = 1.0 + 1.0i$, with the stack resting at $(T:0.8, Z:0.8, Y:1.000000, X:1.000000)$.

Result: **$z = 1.0 + 1.0i$** ($R = Z_0, X = Z_0$).

---

### Problem 5.19: Operational Amplifier Inverting Bandpass Gain
**Analog Electronics Context:** $Z_f = 10\text{ k}\Omega \parallel (C_f = 10\text{ nF})$, $Z_{\text{in}} = 1\text{ k}\Omega + (C_{\text{in}} = 100\text{ nF})$. At $f = 1,591.55\text{ Hz}$ ($\omega = 10,000\text{ rad/s}$):
$$Z_f = \frac{10000}{1 + j(10000)(10^4)(10^{-8})} = \frac{10000}{1 + j} = 5000 - 5000i\,\Omega$$
$$Z_{\text{in}} = 1000 - j\frac{1}{10000 \times 10^{-7}} = 1000 - 1000i\,\Omega$$
$$\text{Gain } A_v = -\frac{Z_f}{Z_{\text{in}}} = -\frac{5000(1 - i)}{1000(1 - i)} = -5.0 + 0i$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_25:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_25:value}}`**

> **Named RPN Stack Idiom: *The Parallel Reciprocal x∥y Shortcut & Complex Branch Reduction*** — Collapse parallel feedback RC admittance and series input impedance across stack registers without scratchpad memory {{cite:horowitz2015,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `5000` `{{key:ENTER}}` — Enter feedback resistance real component ($R_f' = 5000.0\,\Omega$) into $Y$.
2. `5000 {{key:+/-}}` `{{key:ENTER}}` — Key capacitive feedback reactance ($X_f' = -5000.0\,\Omega$), elevating the real part.
3. `1000` `{{key:ENTER}}` — Load input resistance ($R_{\text{in}} = 1000.0\,\Omega$) into $Y$.
4. `1000 {{key:+/-}}` — Enter input capacitive reactance ($X_{\text{in}} = -1000.0\,\Omega$) into $X$.
5. `{{key:CMPLX}}` `{{key:÷}}` — Execute complex division $Z_f / Z_{\text{in}}$ directly, resolving bandpass gain $A_v = -5.0000 + 0.0000i$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `5000 {{key:ENTER}} 5000 {{key:+/-}} {{key:ENTER}}` | $0.0000$ | $5000.0000$ | $-5000.0000$ | $-5000.0000$ | Feedback impedance $Z_f$ pushed |
| 2 | `1000 {{key:ENTER}} 1000 {{key:+/-}}` | $5000.0000$ | $-5000.0000$ | $1000.0000$ | $-1000.0000$ | Input impedance $Z_{\text{in}}$ in $(Y, X)$ |
| 3 | `{{key:CMPLX}} {{key:÷}}` | $5000.0000$ | $5000.0000$ | $5.000000$ | $0.000000$ | Complex ratio $Z_f / Z_{\text{in}} = 5.0 + 0i$ |
| 4 | `{{key:CMPLX}} {{key:+/-}}` | $5000.0000$ | $5000.0000$ | **$-5.000000$** | **$0.000000$** | Negate gain: $A_v = -5.0 + 0i$ |

Result: **$-5.000000 + 0.000000i$**.

---

### Problem 5.20: Acoustic Wave Impedance at Boundary
**Acoustics Context:** Characteristic impedance of air $Z_1 = 415\text{ Pa}\cdot\text{s/m}$, porous fiberglass absorber $Z_2 = 600 - 450i\text{ Pa}\cdot\text{s/m}$. Find acoustic reflection coefficient:
$$\Gamma_a = \frac{Z_2 - Z_1}{Z_2 + Z_1} = \frac{(600 - 415) - 450i}{(600 + 415) - 450i} = \frac{185 - 450i}{1015 - 450i}$$

**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_26:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_26:value}}`**

Key numerator differential impedance $(Z_2 - Z_1) = 185 - 450i$ with `185 {{key:ENTER}} 450 {{key:+/-}} {{key:ENTER}}` and denominator $(Z_2 + Z_1) = 1015 - 450i$ with `1015 {{key:ENTER}} 450 {{key:+/-}}`, yielding $(T:185, Z:-450, Y:1015, X:-450)$. Press `{{key:CMPLX}} {{key:÷}}` to resolve acoustic reflection coefficient $(T:185, Z:185, Y:0.316823, X:-0.302394)$.

Result: **$0.316823 - 0.302394i$** ($|\Gamma_a| = 0.4379 \implies \text{Absorption coefficient } \alpha = 1 - |\Gamma_a|^2 = 0.8082$).

---

### Problem 5.21: Thevenin Equivalent Impedance of Bridge Circuit
**Circuit Context:** A bridge network has branch impedances $Z_A = 10 + 20i$, $Z_B = 30 - 10i$, $Z_C = 20 + 0i$, $Z_D = 0 - 25i$. Thevenin impedance between nodes:
$$Z_{\text{th}} = (Z_A \parallel Z_C) + (Z_B \parallel Z_D)$$
Evaluated using the parallel reciprocal pipeline into Register $Y$ and $X$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Load Complex Operand $z_1$:** Key in $\text{Re}(z_1)$ `{{key:ENTER}}` $\text{Im}(z_1)$ `{{key:ENTER}}` to position the real component in deeper stack memory and the imaginary component in Register $Y$/$Z$.
2. **Load Complex Operand $z_2$ (or Apply Unary `{{key:CMPLX}}`):** Key in $\text{Re}(z_2)$ `{{key:ENTER}}` $\text{Im}(z_2)$ so the complex pair occupies $(Y, X)$ while $z_1$ rests in $(T, Z)$.
3. **Execute `{{key:CMPLX}}` Operation:** Invoke `{{key:CMPLX}}` followed by the target arithmetic/transcendental key; the 4-register stack evaluates both real and imaginary components simultaneously, returning $\text{Re}(\text{result})$ in Register $Y$ and $\text{Im}(\text{result})$ in Register $X$ (swap via `{{key:x⇄y}}` to inspect either axis).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `10 {{key:ENTER}} 20 {{key:ENTER}} 20 {{key:ENTER}} 0` | $10.0000$ | $20.0000$ | $20.0000$ | $0.0000$ | Load branch impedances $Z_A$ and $Z_C$ |
| 2 | `{{key:CMPLX}} {{key:x∥y}}` | $10.0000$ | $10.0000$ | $8.5714$ | $5.7143$ | Parallel branch $Z_{AC} = Z_A \parallel Z_C$ |
| 3 | `30 {{key:ENTER}} 10 {{key:+/-}} {{key:ENTER}} 0 {{key:ENTER}} 25 {{key:+/-}}` | $30.0000$ | $-10.0000$ | $0.0000$ | $-25.0000$ | Load branch impedances $Z_B$ and $Z_D$ |
| 4 | `{{key:CMPLX}} {{key:x∥y}}` | $30.0000$ | $30.0000$ | $5.7143$ | $-2.1429$ | Parallel branch $Z_{BD} = Z_B \parallel Z_D$ |
| 5 | `{{key:CMPLX}} {{key:+}}` | $8.5714$ | $8.5714$ | **$14.2857$** | **$3.5714$** | Thevenin impedance $Z_{\text{th}} = Z_{AC} + Z_{BD}$ |

Result: **$14.2857 + 3.5714i\,\Omega$**.

---

### Problem 5.22: Mutual Inductive Coupling in Transformer
**RF Context:** Primary inductance $L_1 = 50\,\mu\text{H}$, secondary $L_2 = 20\,\mu\text{H}$, coupling factor $k = 0.8$. Mutual inductance $M = k\sqrt{L_1 L_2}$:
$$M = 0.8 \sqrt{50 \times 20} = 0.8 \sqrt{1000} \approx 25.2982\,\mu\text{H}$$
Keystrokes: `{{res:sc32_05_complex_numbers_phasors_seq_27:keys}}`$\implies$ **$25.2982\,\mu\text{H}$**.

> **Named RPN Stack Idiom: *The Inside-Out Radical & Mutual Inductance Pipeline*** — Multiply primary and secondary inductances directly in the stack, extract square root in place, and scale by coupling coefficient without register allocation {{cite:horowitz2015,hp15c1982}}.

Enter `50 {{key:ENTER}} 20 {{key:×}}` to form the inductive product $1000\,\mu\text{H}^2$ in $X$ $(T:0, Z:0, Y:0, X:1000)$, take the square root with `{{key:√x}}` $(T:0, Z:0, Y:0, X:31.6228)$, and scale by coupling coefficient with `0.8 {{key:×}}`, resolving $(T:0, Z:0, Y:0, X:25.2982)$.

Result: **$25.2982\,\mu\text{H}$**.

---

### Problem 5.23: Polyphase 3-Phase Symmetrical Components ($a$-Operator)
**Power Systems Context:** The symmetrical component operator is $a = e^{i 120^\circ} = \cos(120^\circ) + i\sin(120^\circ) = -0.5 + 0.866025i$.
Calculate $a^2$:
$$a^2 = e^{i 240^\circ} = -0.5 - 0.866025i$$
Calculate $1 + a + a^2$:
$$1 + (-0.5 + 0.866025i) + (-0.5 - 0.866025i) = \mathbf{0.000000 + 0.000000i}$$
Zero-sequence summation holds exactly!

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `120` `{{key:ENTER}}` `1` `{{key:▸y,x}}` — Convert polar unit phasor ($1\angle 120^\circ$) to rectangular components; real component $-0.5$ forms in $X$ and imaginary component $0.866025$ in $Y$.
2. `240` `{{key:ENTER}}` `1` `{{key:▸y,x}}` — Convert second phasor ($1\angle 240^\circ$) to rectangular coordinates $(-0.5, -0.866025)$.
3. Sum rectangular components and add unit real reference $1.0$; real and imaginary components sum to $\mathbf{0.000000 + 0.000000i}$, verifying symmetrical zero-sequence balance.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `120 {{key:ENTER}} 1 {{key:▸y,x}}` | $0.0000$ | $0.0000$ | $0.866025$ | $-0.500000$ | Polar to rectangular: $a = -0.5 + 0.8660i$ |
| 2 | `240 {{key:ENTER}} 1 {{key:▸y,x}}` | $0.866025$ | $-0.500000$ | $-0.866025$ | $-0.500000$ | Polar to rectangular: $a^2 = -0.5 - 0.8660i$ |
| 3 | `{{key:x⇄y}} {{key:R↓}} {{key:+}}` | $0.0000$ | $0.866025$ | $-0.866025$ | $-1.000000$ | Real sum: $-0.5 + (-0.5) = -1.0$ |
| 4 | `{{key:x⇄y}} {{key:+}}` | $0.0000$ | $0.0000$ | $-1.000000$ | $0.000000$ | Imaginary sum: $0.8660 - 0.8660 = 0.0$ |
| 5 | `{{key:x⇄y}} 1 {{key:+}} {{key:x⇄y}}` | $0.0000$ | $0.0000$ | **$0.000000$** | **$0.000000$** | Add $+1$ reference: $1 + a + a^2 = 0 + 0i$ |

Result: **$0.000000 + 0.000000i$**.

---

### Problem 5.24: Damped Harmonic Oscillator Complex Eigenvalues
**Mechanics Context:** Mass $m = 2\text{ kg}$, damping $c = 8\text{ N}\cdot\text{s/m}$, stiffness $k = 50\text{ N/m}$:
$$\lambda = -\frac{c}{2m} \pm \sqrt{\left(\frac{c}{2m}\right)^2 - \frac{k}{m}} = -2.0 \pm \sqrt{4 - 25} = -2.0 \pm \sqrt{-21} = -2.0 \pm 4.582576i$$
Natural damped frequency $\omega_d = 4.5826\text{ rad/s}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `8` `{{key:ENTER}}` `4` `{{key:÷}}` `{{key:+/-}}` — Compute real damping attenuation factor $\alpha = -c/(2m) = -8 / 4 = -2.0\text{ s}^{-1}$ in Register $X$.
2. `4` `{{key:ENTER}}` `25` `{{key:-}}` `{{key:+/-}}` `{{key:√x}}` — Evaluate discriminant magnitude $|4 - 25| = 21$ and extract square root, producing damped angular frequency $\omega_d = \sqrt{21} \approx 4.582576\text{ rad/s}$.
3. `{{key:x⇄y}}` — Pair with real component $-2.0$ in Register $Y$ to display the complete conjugate eigenvalue pair $\lambda = -2.0 \pm 4.582576i$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `8 {{key:ENTER}} 4 {{key:÷}} {{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-2.0000$ | Real damping factor $\alpha = -c/(2m) = -2.0\text{ s}^{-1}$ |
| 2 | `4 {{key:ENTER}} 25 {{key:-}} {{key:+/-}}` | $0.0000$ | $0.0000$ | $-2.0000$ | $21.0000$ | Discriminant magnitude $|\Delta| = 21.0$ |
| 3 | `{{key:√x}}` | $0.0000$ | $0.0000$ | $-2.0000$ | **$4.582576$** | Damped angular frequency $\omega_d = 4.5826\text{ rad/s}$ |
| 4 | `{{key:SHOW}}` | $0.0000$ | $0.0000$ | **$-2.000000$** | **$4.582576$** | Complex conjugate eigenvalues $\lambda = -2.0 \pm 4.5826i$ |

Result: **$-2.000000 \pm 4.582576i$**.

---

### Problem 5.25: Waveguide Attenuation and Propagation Constant ($\gamma$)
**Electromagnetics Context:** Propagation constant $\gamma = \alpha + j\beta$. In cutoff band: $\alpha = 14.5\text{ Np/m}, \beta = 0\text{ rad/m}$. Attenuation in decibels per meter:
$$\text{Atten} = 20 \log_{10}(e) \times \alpha = 8.68589 \times 14.5 = \mathbf{125.945\text{ dB/m}}$$

Key `1 {{key:eˣ}} {{key:LOG}} 20 {{key:×}}` to calculate the Nepers-to-dB conversion factor ($8.685890\text{ dB/Np}$) in $X$ $(T:0, Z:0, Y:0, X:8.685890)$, then multiply by attenuation coefficient with `14.5 {{key:×}}`, resolving total attenuation $(T:0, Z:0, Y:0, X:125.945405)$.

Result: **$125.945\text{ dB/m}$**.

---

### Problem 5.26: Plasma Physics Dielectric Permittivity
**Ionosphere Context:** Cold plasma relative permittivity $\epsilon_r = 1 - \frac{\omega_p^2}{\omega(\omega - j\nu)}$.
For $\omega_p = 10^7\text{ rad/s}, \omega = 2 \times 10^7\text{ rad/s}, \nu = 5 \times 10^6\text{ s}^{-1}$:
Denominator $z = 2\cdot 10^7 (2\cdot 10^7 - 5\cdot 10^6 i) = 4\cdot 10^{14} - 1\cdot 10^{14} i$.
Evaluated via `{{key:CMPLX}} {{key:1/x}}` $\implies \epsilon_r = \mathbf{0.7647 - 0.0588i}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. Scale frequency by $10^7$ so $\omega_p = 1, \omega = 2, \nu = 0.5$; denominator becomes $z = 2(2 - 0.5i) = 4.0 - 1.0i$.
2. `4` `{{key:ENTER}}` `1 {{key:+/-}}` — Load denominator components into Registers $(Y = 4.0, X = -1.0)$.
3. `{{key:CMPLX}}` `{{key:1/x}}` — Evaluate complex reciprocal $1/(4-i) = (4+i)/17 = 0.235294 + 0.058824i$.
4. Multiply by $\omega_p^2 = 1.0$ and subtract from unity; relative permittivity converges to $\epsilon_r = \mathbf{0.7647 - 0.0588i}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `4 {{key:ENTER}} 1 {{key:+/-}}` | $0.0000$ | $0.0000$ | $4.0000$ | $-1.0000$ | Scaled denominator $z = 4.0 - 1.0i$ |
| 2 | `{{key:CMPLX}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.235294$ | $0.058824$ | Invert: $1/(4-i) = 0.2353 + 0.0588i$ |
| 3 | `1 {{key:ENTER}} 0` | $0.235294$ | $0.058824$ | $1.0000$ | $0.0000$ | Unit real reference $1.0 + 0i$ in $(Y, X)$ |
| 4 | `{{key:CMPLX}} {{key:-}}` | $0.235294$ | $0.235294$ | **$0.764706$** | **$-0.058824$** | Subtract from unity: $\epsilon_r = 0.7647 - 0.0588i$ |

Result: **$0.764706 - 0.058824i$**.

---

### Problem 5.27: Complex Impedance of Parallel RLC Tank at Resonance
**RF Context:** Tank circuit with $R = 10\text{ k}\Omega, L = 10\,\mu\text{H}, C = 100\text{ pF}$. Resonant frequency $\omega_0 = 1/\sqrt{LC} = 31.6228\text{ Mrad/s}$. At resonance, reactive admittances cancel ($j\omega C + 1/(j\omega L) = 0$), leaving pure resistance:
$$\mathbf{Z}_{\text{tank}} = R = 10,000.0 + 0.0i\,\Omega$$

Evaluate the reactive product with `10 {{key:E}} 6 {{key:+/-}} {{key:ENTER}} 100 {{key:E}} 12 {{key:+/-}} {{key:×}}` $(T:0, Z:0, Y:0, X:1.0 \times 10^{-15})$, extract the resonant frequency with `{{key:√x}} {{key:1/x}}` $(T:0, Z:0, Y:0, X:3.1623 \times 10^7)$, then load the resonant tank impedance `10000 {{key:ENTER}} 0` across $(Y, X)$, confirming purely resistive impedance $(T:0, Z:3.1623 \times 10^7, Y:10000.0000, X:0.0000)$.

Result: **$10,000.0 + 0.0i\,\Omega$**.

---

### Problem 5.28: Conformal Mapping: Joukowsky Airfoil Transformation
**Aerodynamics Context:** Joukowsky transform maps cylinder to airfoil: $\zeta = z + \frac{c^2}{z}$.
For cylinder point $z = 1.1 + 0.2i$ and $c = 1.0$:
$$\frac{1}{z} = \frac{1.1 - 0.2i}{1.21 + 0.04} = \frac{1.1 - 0.2i}{1.25} = 0.88 - 0.16i$$
$$\zeta = (1.1 + 0.2i) + (0.88 - 0.16i) = \mathbf{1.980000 + 0.040000i}$$

Load $z = 1.1 + 0.2i$ via `1.1 {{key:ENTER}} 0.2` $(T:0, Z:0, Y:1.1, X:0.2)$ and invert with `{{key:CMPLX}} {{key:1/x}}` to find $1/z$ $(T:0, Z:0, Y:0.880000, X:-0.160000)$. Reload $z$ into $(Y, X)$ via `1.1 {{key:ENTER}} 0.2` and sum with `{{key:CMPLX}} {{key:+}}`, mapping the airfoil boundary to $(T:0.88, Z:0.88, Y:1.980000, X:0.040000)$.

Result: **$1.980000 + 0.040000i$**.

---

### Problem 5.29: Complex Root Extraction via de Moivre ($z^4 = -16$)
**Algebra Context:** Roots of $z^4 = -16 = 16 e^{i\pi}$:
$r = 16^{1/4} = 2.0$. First root $\theta = \pi/4 = 45^\circ$:
$$z_0 = 2(\cos 45^\circ + i\sin 45^\circ) = \sqrt{2} + i\sqrt{2} \approx 1.414214 + 1.414214i$$
Keystrokes: `{{res:sc32_05_complex_numbers_phasors_seq_28:keys}}`$\implies$ **$1.414214$ in $X$ and $Y$**.

Key the angle and radial modulus `45 {{key:ENTER}} 2` into $(Y, X)$ $(T:0, Z:0, Y:45, X:2)$, then convert from polar to rectangular via `{{key:▸y,x}}`, extracting principal root $z_0 = 1.414214 + 1.414214i$ across $(T:0, Z:0, Y:1.414214, X:1.414214)$.

Result: **$1.414214 + 1.414214i$**.

---

### Problem 5.30: Skin Effect in Solid Copper Conductor
**Electromagnetics Context:** Skin depth $\delta = \sqrt{2/(\omega \mu \sigma)}$. For copper ($\sigma = 5.8 \times 10^7\text{ S/m}$) at $f = 10\text{ MHz}$ ($\omega = 6.283185 \times 10^7\text{ rad/s}$):
$$\delta = \sqrt{\frac{2}{6.283185\cdot 10^7 \times 4\pi\cdot 10^{-7} \times 5.8\cdot 10^7}} \approx 2.089 \times 10^{-5}\text{ m} = \mathbf{20.89\,\mu\text{m}}$$

Form permeability with `4 {{key:π}} {{key:×}} 1 {{key:E}} 7 {{key:+/-}} {{key:×}}` $(T:0, Z:0, Y:0, X:1.2566 \times 10^{-6})$, multiply by frequency and conductivity `6.283185 {{key:E}} 7 {{key:×}} 5.8 {{key:E}} 7 {{key:×}}` $(T:0, Z:0, Y:0, X:4.5828 \times 10^9)$, invert into ratio $2/(\omega\mu\sigma)$ with `2 {{key:x⇄y}} {{key:÷}}` $(T:0, Z:0, Y:0, X:4.3639 \times 10^{-10})$, and take the square root `{{key:√x}}`, arriving at skin depth $(T:0, Z:0, Y:0, X:2.0890 \times 10^{-5})$.

Result: **$\delta = 20.89\,\mu\text{m}$**.

---

### Problem 5.31: Lossy Transmission Line Complex Characteristic Impedance ($Z_0$)
**RF Context:** $R' = 0.1\,\Omega/\text{m}, L' = 0.25\,\mu\text{H/m}, G' = 1\,\mu\text{S/m}, C' = 100\,\text{pF/m}$. At $\omega = 10^7\text{ rad/s}$:
$$Z_0 = \sqrt{\frac{R' + j\omega L'}{G' + j\omega C'}} = \sqrt{\frac{0.1 + 2.5i}{10^{-6} + 10^{-3}i}} \approx \mathbf{49.9985 - 0.9995i\,\Omega}$$

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `0.1` `{{key:ENTER}}` `2.5` — Load transmission line series impedance $Z' = 0.1 + 2.5i$ across Registers $(Y, X)$.
2. `1 {{key:E}} 6 {{key:+/-}}` `{{key:ENTER}}` `1 {{key:E}} 3 {{key:+/-}}` — Load shunt admittance $Y' = 10^{-6} + 10^{-3}i$ into $(Y, X)$, lifting $Z'$ to $(T, Z)$.
3. `{{key:CMPLX}}` `{{key:÷}}` — Execute complex division $Z'/Y' \approx 2499.00 - 99.96i$.
4. `{{key:CMPLX}}` `{{key:√x}}` — Extract complex square root in place; characteristic impedance evaluates to $Z_0 = \mathbf{49.9985 - 0.9995i\,\Omega}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0.1 {{key:ENTER}} 2.5` | $0.0000$ | $0.0000$ | $0.1000$ | $2.5000$ | Load series impedance $Z' = 0.1 + 2.5i$ |
| 2 | `1 {{key:E}} 6 {{key:+/-}} {{key:ENTER}} 1 {{key:E}} 3 {{key:+/-}}` | $0.1000$ | $2.5000$ | $1.0000 \times 10^{-6}$ | $1.0000 \times 10^{-3}$ | Load shunt admittance $Y'$ into $(Y, X)$ |
| 3 | `{{key:CMPLX}} {{key:÷}}` | $0.1000$ | $0.1000$ | $2499.0010$ | $-99.9575$ | Complex impedance ratio $Z'/Y'$ |
| 4 | `{{key:CMPLX}} {{key:√x}}` | $0.1000$ | $0.1000$ | **$49.9985$** | **$-0.9995$** | Characteristic impedance $Z_0 = \sqrt{Z'/Y'}$ |

Result: **$49.9985 - 0.9995i\,\Omega$**.

---

### Problem 5.32: Dispersion Relation in Fiber Optics (Group Velocity Dispersion)
**Photonics Context:** Complex propagation constant $\beta(\omega) = \beta_0 + \beta_1(\omega - \omega_0) + \frac{1}{2}\beta_2(\omega - \omega_0)^2$. Pulse dispersion parameter $D = -2\pi c \beta_2 / \lambda^2$. For $\beta_2 = -20\text{ ps}^2/\text{km}$ at $\lambda = 1.55\,\mu\text{m}$:
$$D = \frac{-2\pi(3\cdot 10^8)(-20\cdot 10^{-27})}{(1.55\cdot 10^{-6})^2} \approx \mathbf{15.68\text{ ps/(nm}\cdot\text{km)}}$$

Compute numerator $2\pi c |\beta_2|$ with `2 {{key:π}} {{key:×}} 3 {{key:E}} 8 {{key:×}} 20 {{key:E}} 27 {{key:+/-}} {{key:×}}` $(T:0, Z:0, Y:0, X:3.7699 \times 10^{-17})$, square wavelength with `1.55 {{key:E}} 6 {{key:+/-}} {{key:x²}}` $(T:0, Z:0, Y:3.7699 \times 10^{-17}, X:2.4025 \times 10^{-12})$, and divide and scale via `{{key:÷}} 1 {{key:E}} 6 {{key:×}}`, arriving at dispersion parameter $(T:0, Z:0, Y:0, X:15.6841)$.

Result: **$15.68\text{ ps/(nm}\cdot\text{km)}$**.

---

### Problem 5.33: Fractional Pole Filter: $s^{0.5}$ Fractional Calculus Impedance
**Control Theory Context:** Warburg impedance in electrochemistry: $\mathbf{Z}_W = \frac{A_W}{\sqrt{\omega}} (1 - j)$.
For $A_W = 200\,\Omega\cdot\text{s}^{-1/2}$ at $\omega = 100\text{ rad/s}$:
$$\mathbf{Z}_W = \frac{200}{10} (1 - j) = \mathbf{20.0000 - 20.0000i\,\Omega}$$

Evaluate $\sqrt{\omega}$ with `100 {{key:√x}}` $(T:0, Z:0, Y:0, X:10)$, compute scale factor $A_W/\sqrt{\omega} = 20\,\Omega$ with `200 {{key:x⇄y}} {{key:÷}}` $(T:0, Z:0, Y:0, X:20)$, and enter resistance and reactance directly `20 {{key:ENTER}} 20 {{key:+/-}}`, confirming Warburg impedance $(T:0, Z:20, Y:20.0000, X:-20.0000)$.

Result: **$20.0000 - 20.0000i\,\Omega$**.

---

### Problem 5.34: Complex Poynting Vector & Electromagnetic Radiation Density
**Antenna Physics Context:** $\mathbf{S}_{\text{cpx}} = \frac{1}{2} \mathbf{E} \times \mathbf{H}^*$. For $\mathbf{E} = 10.0 + 5.0i\text{ V/m}$ and $\mathbf{H} = 0.02 + 0.01i\text{ A/m}$:
$$\mathbf{H}^* = 0.02 - 0.01i \implies \mathbf{E} \cdot \mathbf{H}^* = (10+5i)(0.02-0.01i) = (0.2 + 0.05) + (-0.1 + 0.1)i = 0.25 + 0i$$
Average radiated power: $\text{Re}(\mathbf{S}_{\text{cpx}}) = 0.5 \times 0.25 = \mathbf{0.125\text{ W/m}^2}$.

Load electric field $\mathbf{E}$ via `10 {{key:ENTER}} 5 {{key:ENTER}}` and conjugate magnetic field $\mathbf{H}^*$ via `0.02 {{key:ENTER}} 0.01 {{key:+/-}}`, placing $(T:10, Z:5, Y:0.02, X:-0.01)$. Execute `{{key:CMPLX}} {{key:×}}` to obtain $0.25 + 0i$ $(T:10, Z:10, Y:0.25, X:0)$, and divide by 2 with `2 {{key:÷}}`, giving average radiation density $(T:10, Z:10, Y:0.25, X:0.1250)$.

Result: **$0.125\text{ W/m}^2$**.

---

### Problem 5.35: Sagnac Ring Interferometer Phase Shift
**Avionics Context:** Fiber optic gyroscope: $\Delta\Phi = \frac{8\pi A N}{c \lambda} \Omega$. For coil area $A = 0.01\text{ m}^2$, $N = 1000\text{ turns}$, $\lambda = 1.31\,\mu\text{m}$, rotation rate $\Omega = 1.0\text{ rad/s}$:
$$\Delta\Phi = \frac{8\pi(0.01)(1000)}{(3\cdot 10^8)(1.31\cdot 10^{-6})} \approx \mathbf{0.6402\text{ radians}}$$

Form optical area-turns product with `8 {{key:π}} {{key:×}} 0.01 {{key:×}} 1000 {{key:×}}` $(T:0, Z:0, Y:0, X:251.3274)$, compute $c\lambda$ with `3 {{key:E}} 8 {{key:ENTER}} 1.31 {{key:E}} 6 {{key:+/-}} {{key:×}}` $(T:0, Z:0, Y:251.3274, X:393.0000)$, and divide with `{{key:÷}}`, resolving Sagnac phase shift $(T:0, Z:0, Y:0, X:0.6402)$.

Result: **$0.6402\text{ radians}$**.

---

### Problem 5.36: Transformer T-Model Core Loss Branch
**Power Systems Context:** Parallel magnetizing branch: $R_c = 50\text{ k}\Omega \parallel X_m = 15\text{ k}\Omega$. Total complex excitation admittance:
$$\mathbf{Y}_m = \frac{1}{50000} - j\frac{1}{15000} = 2.0 \times 10^{-5} - 6.6667 \times 10^{-5}i\,\text{S}$$
Impedance: $\mathbf{Z}_m = 1/\mathbf{Y}_m = \mathbf{4,137.93 + 13,793.10i\,\Omega}$.

Key core conductance `50000 {{key:1/x}}` $(T:0, Z:0, Y:0, X:2.0 \times 10^{-5})$ and susceptance `15000 {{key:1/x}} {{key:+/-}}` $(T:0, Z:0, Y:2.0 \times 10^{-5}, X:-6.6667 \times 10^{-5})$, then take complex reciprocal with `{{key:CMPLX}} {{key:1/x}}`, arriving at equivalent branch impedance $(T:0, Z:0, Y:4137.9310, X:13793.1034)$.

Result: **$4,137.93 + 13,793.10i\,\Omega$**.

---

### Problem 5.37: Elliptical Polarization Axial Ratio from Orthogonal E-Phasors
**RF Context:** $\mathbf{E}_x = 10\angle 0^\circ = 10 + 0i$, $\mathbf{E}_y = 6\angle 90^\circ = 0 + 6i$.
Major axis $a = 10.0$, minor axis $b = 6.0$. Axial ratio:
$$\text{AR} = \frac{10.0}{6.0} = 1.6667 \implies \text{AR}_{\text{dB}} = 20 \log_{10}(1.6667) = \mathbf{4.4370\text{ dB}}$$

Key `10 {{key:ENTER}} 6 {{key:÷}}` $(T:0, Z:0, Y:0, X:1.666667)$ to divide the axes, take the base-10 logarithm with `{{key:LOG}}` $(T:0, Z:0, Y:0, X:0.221849)$, and scale with `20 {{key:×}}` to determine polarization axial ratio in decibels $(T:0, Z:0, Y:0, X:4.436975)$.

Result: **$4.4370\text{ dB}$**.

---

### Problem 5.38: Complex Root Finding of Quadratic with Real Coefficients
**Algebra Context:** $z^2 - 4z + 13 = 0$. Roots: $z = \frac{4 \pm \sqrt{16 - 52}}{2} = 2 \pm \sqrt{-9} = 2 \pm 3i$.
Verify root $2 + 3i$: $(2+3i)^2 - 4(2+3i) + 13 = (-5 + 12i) - (8 + 12i) + 13 = \mathbf{0.0 + 0.0i}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `2` `{{key:ENTER}}` `3` — Load candidate complex root $z_1 = 2.0 + 3.0i$ across Registers $(Y, X)$.
2. `{{key:CMPLX}}` `{{key:ENTER}}` — Duplicate the complex number into $(T, Z)$ so both $(T, Z)$ and $(Y, X)$ contain $2.0 + 3.0i$.
3. `{{key:CMPLX}}` `{{key:×}}` — Execute complex square, yielding $z_1^2 = -5.0000 + 12.0000i$ across $(Y, X)$.
4. `8` `{{key:ENTER}}` `12` `{{key:CMPLX}}` `{{key:-}}` `13` `{{key:+}}` — Deduct $4z_1 = 8 + 12i$ and add scalar constant 13; polynomial residual verifies to $\mathbf{0.0000 + 0.0000i}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `2 {{key:ENTER}} 3 {{key:ENTER}}` | $0.0000$ | $2.0000$ | $3.0000$ | $3.0000$ | Candidate complex root $z_1 = 2 + 3i$ pushed |
| 2 | `2 {{key:ENTER}} 3` | $2.0000$ | $3.0000$ | $2.0000$ | $3.0000$ | Duplicate complex pair into $(Y, X)$ |
| 3 | `{{key:CMPLX}} {{key:×}}` | $2.0000$ | $2.0000$ | $-5.0000$ | $12.0000$ | Complex square $z_1^2 = -5 + 12i$ |
| 4 | `8 {{key:ENTER}} 12 {{key:CMPLX}} {{key:-}}` | $-5.0000$ | $-5.0000$ | $-13.0000$ | $0.0000$ | Subtract $4z_1 = 8 + 12i$ |
| 5 | `13 {{key:+}}` | $-5.0000$ | $-5.0000$ | **$0.0000$** | **$0.0000$** | Add scalar 13; residual $= 0.0 + 0.0i$ |

Result: **$0.0000 + 0.0000i$**.

---

### Problem 5.39: High-Speed Sprint: Chained Complex Admittance Evaluation
**Rapid Calculation Context:** Compute the equivalent impedance of $Z_1 = 3 + 4i$ and $Z_2 = 3 - 4i$ in parallel:
$$\frac{1}{Z_{\text{parallel}}} = \frac{1}{3+4i} + \frac{1}{3-4i} = \frac{3-4i}{25} + \frac{3+4i}{25} = \frac{6}{25} \implies Z_{\text{parallel}} = \frac{25}{6} = \mathbf{4.166667\,\Omega}$$
Imaginary parts cancel completely! Keystrokes: `{{res:sc32_05_complex_numbers_phasors_seq_32:keys}}` $\implies$ **$4.166667$**.

> **Named RPN Stack Idiom: *The Parallel Reciprocal x∥y Shortcut & Admittance Sprint*** — Invert conjugate impedances $Z_1 = 3+4i$ and $Z_2 = 3-4i$ directly in the stack; imaginary components cancel automatically, yielding exact parallel resistance in one step {{cite:hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `3` `{{key:ENTER}}` `4` — Place complex branch impedance $Z_1 = 3 + 4i$ across Registers $(Y, X)$.
2. `{{key:CMPLX}}` `{{key:1/x}}` — Take complex reciprocal to obtain admittance $Y_1 = 0.12 - 0.16i\,\text{S}$.
3. `3` `{{key:ENTER}}` `4 {{key:+/-}}` — Enter second impedance branch $Z_2 = 3 - 4i$.
4. `{{key:CMPLX}}` `{{key:1/x}}` — Take complex reciprocal to yield admittance $Y_2 = 0.12 + 0.16i\,\text{S}$.
5. `{{key:CMPLX}}` `{{key:+}}` — Sum admittances; conjugate imaginary reactances cancel, leaving conductance $G = 0.24\,\text{S}$.
6. `{{key:1/x}}` — Invert conductance to obtain net parallel resistance $Z_{\text{parallel}} = \mathbf{4.166667\,\Omega}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `3 {{key:ENTER}} 4` | $0.0000$ | $0.0000$ | $3.0000$ | $4.0000$ | Load branch impedance $Z_1 = 3 + 4i$ |
| 2 | `{{key:CMPLX}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.120000$ | $-0.160000$ | Invert: $Y_1 = 0.12 - 0.16i\,\text{S}$ |
| 3 | `{{key:x⇄y}}` | $0.0000$ | $0.0000$ | $-0.160000$ | $0.120000$ | Swap real conductance to Register $X$ |
| 4 | `2 {{key:×}}` | $0.0000$ | $0.0000$ | $-0.160000$ | $0.240000$ | Double conductance (imag parts cancel) |
| 5 | `{{key:1/x}}` | $0.0000$ | $0.0000$ | $-0.160000$ | **$4.166667$** | Invert net conductance: $Z_{\text{parallel}} = 4.1667\,\Omega$ |

Result: **$4.166667\,\Omega$**.

---

### Problem 5.40: High-Speed Sprint: Radical Exponential Nested Complex Identity
**Rapid Calculation Sprint:** Evaluate $\sqrt{e^{i\pi/2}}$:
$$e^{i\pi/2} = i \implies \sqrt{i} = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}i \approx 0.707107 + 0.707107i$$
**Keystrokes:** `{{res:sc32_05_complex_numbers_phasors_seq_29:keys}}` $\rightarrow$ **`{{res:sc32_05_complex_numbers_phasors_seq_29:value}}`**

> **Named RPN Stack Idiom: *The Inside-Out Radical & Euler Polar Identity*** — Load Euler imaginary exponent $e^{i\pi/2} = i$, extract complex square root directly, and resolve $\sqrt{i} = \sqrt{2}/2 + i\sqrt{2}/2$ without scratchpad memory {{cite:strogatz2019,hp15c1982}}.

Enter imaginary exponent $\pi/2$ via `0 {{key:ENTER}} {{key:π}} 2 {{key:÷}}` $(T:0, Z:0, Y:0, X:1.570796)$, evaluate complex exponential with `{{key:CMPLX}} {{key:eˣ}}` $(T:0, Z:0, Y:0.000000, X:1.000000)$, and extract the square root with `{{key:CMPLX}} {{key:√x}}`, producing $(T:0, Z:0, Y:0.707107, X:0.707107)$ in 4 seconds flat!

Result: **$0.707107 + 0.707107i$**.

Stack outputs: **$Y = 0.707107$**, **$X = 0.707107$** in 4 seconds flat!

---

## Summary & Looking Ahead

Chapter 5 unified complex algebra and alternating current phasor analysis on the operational stack. By treating the physical coordinate pair $(Y, X)$ as real and imaginary components ($Y + Xi$), you executed complex arithmetic, inverted reactive admittances, validated Euler's identity ($e^{i\pi} + 1 = 0$), and solved multi-branch impedance networks in place via `{{key:CMPLX}}`. Without scratchpad bookkeeping or complex-mode matrix software, two-dimensional algebraic quantities flowed through the stack with the speed and certainty of real numbers.

From two-dimensional complex coordinates, the natural progression leads into three-dimensional physical space. In **Chapter 6: Geometry, 3D Spatial Vectors & Surface Area**, you will explore planar areas, composite volumes, and spatial Euclidean metrics. Most powerfully, you will master the flagship **Surface Area via Stats Mode (`{{key:Σ+}}`)** technique, accumulating polygonal face pairs into hardware statistical memory without writing down intermediate terms or nesting parentheses.
