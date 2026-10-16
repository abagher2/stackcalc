---
title: "Chapter 3: Algebra, Transcendentals & Display Formatting | SC-32 Manual"
description: "Powers, roots, logarithms, exponentials, number parts (IP, FP, ABS, SGN), large factorials up to 70!, and display formatting modes on the StackCalc SC-32."
---

# Chapter 3: Algebra, Transcendentals & Display Formatting

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 ALGEBRA // TRANSCENDENTALS &amp; NUMERICAL PARTS</span>
  <span class="te-viewport-status text-sky-400">● IEEE-754 EXTENDED ENGINE &bull; 70! EXPONENT PRESERVATION &bull; DISPLAY ARCHITECTURE</span>
</div>

## John Napier's 20-Year Labor (1614): How Logarithms Doubled the Lifespan of Astronomers, and Cody & Waite's Range Reduction

In the damp stone halls of Merchiston Castle near Edinburgh, Scotland, in the early decades of the seventeenth century, Scottish mathematician and baron **John Napier** (1550–1617) sat watching the intellectual crisis of his era unfold. Across Europe, the scientific revolution was stalling—not for lack of astronomical genius, but under the sheer, crushing burden of arithmetic.

Johannes Kepler, Tycho Brahe, and contemporary naval navigators were going blind by candlelight, spending months manually multiplying eight-digit sines and chords to determine planetary orbits and guide merchant fleets across uncharted oceans. A single calculation error on the four-hundredth page of an orbital ephemeris could invalidate a year of painstaking sky observations.

Napier dedicated twenty grueling years of his life to a singular obsession: could the brutal labor of multiplication be transformed into simple addition?

In 1614, Napier published his masterpiece, *Mirifici Logarithmorum Canonis Descriptio* ("Description of the Wonderful Rule of Logarithms") {{cite:napier1614}}. By mapping numbers into geometric ratios and continuous flow distances, Napier discovered that:
$$\log(a \cdot b) = \log a + \log b \qquad \text{and} \qquad \log\left(\frac{a}{b}\right) = \log a - \log b$$

The effect on science was explosive. Calculations that previously took astronomers four exhausting weeks could now be executed in an afternoon. Decades later, the great French mathematician Pierre-Simon Laplace observed that Napier's logarithms, *"by shortening the labors, doubled the life of the astronomer."*

{{blocks:counting_tiles_distributive_4color|4-Color Distributive Geometric Polynomial Area}}
<div class="text-center font-mono text-xs text-slate-400 mb-6">Figure 3.1: The physical distributive area model: geometric decomposition of multi-digit polynomial multiplication into visual sub-rectangles.</div>

Three and a half centuries later, the battle for logarithmic precision moved from quill and paper into silicon microcode. When evaluating exponential ($e^x$), logarithmic ($\ln x$), and power ($y^x$) functions on digital computers, naive textbook Taylor series suffer from **catastrophic cancellation**—the complete annihilation of significant digits when subtracting nearly equal floating-point numbers.

In 1980, William J. Cody and William Waite published their landmark treatise, *Software Manual for the Elementary Functions* {{cite:cody1980}}, solving the range reduction problem. They demonstrated that before evaluating transcendentals, the argument $x$ must be rigorously reduced to a primary kernel $[-\ln 2 / 2, +\ln 2 / 2]$ using extended-precision constants, preserving all 53 bits of IEEE-754 mantissa. The StackCalc SC-32 builds directly upon this intellectual lineage, providing transcendentals and powers that guarantee 12 visible decimal digits of monotonic precision across all engineering domains.

<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>{{key:ALL}}</code> (Full 12-digit scientific mantissa; Standard Base-10 Arithmetic; Degrees angular mode default).
</div>

---

{{res:sc32_db_spl:screenshot|Acoustic sound pressure level 20 * log10(2 / 0.00002) = 100 dB}}



## Powers, Roots, Reciprocals & Parallel Operations

The StackCalc SC-32 provides direct hardware primitives for power, root, reciprocal, and parallel combination operations, executing in under 14 clock cycles on the 150 MHz dual-core silicon:

| Mathematical Function | Physical Keycap | Arity | Exact Mathematical Definition | Register Stack Effect |
| :--- | :---: | :---: | :--- | :--- |
| **Square** | `{{keycap:x²}}` | Unary | $f(x) = x^2$ | $X \leftarrow X^2$ |
| **Square Root** | `{{key:√x}}` | Unary | $f(x) = \sqrt{x}, \quad x \ge 0$ | $X \leftarrow \sqrt{X}$ |
| **Reciprocal** | `{{key:1/x}}` | Unary | $f(x) = 1/x, \quad x \ne 0$ | $X \leftarrow 1/X$ |
| **General Power** | `{{key:yˣ}}` | Dyadic | $f(y, x) = y^x = \exp(x \ln y)$ | $X \leftarrow Y^X$ (Dyadic drop) |
| **Arbitrary Root** | `{{keycap:ˣ√y}}` | Dyadic | $f(y, x) = \sqrt[x]{y} = y^{1/x}$ | $X \leftarrow Y^{1/X}$ (Dyadic drop) |
| **Parallel Harmonic** | `{{key:x∥y}}` | Dyadic | $f(x, y) = \frac{x \cdot y}{x + y}$ | $X \leftarrow \frac{X \cdot Y}{X + Y}$ (Dyadic drop) |


### `{{key:x²}}` (Square) and `{{key:√x}}` (Square Root)
* **Mathematical Definition:** $x^2 = x \times x$ and $\sqrt{x} = x^{1/2}$.
* **Conceptual Intuition:** Essential for quadratic formula solutions ($x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$), Euclidean norms ($r = \sqrt{x^2 + y^2}$), kinetic energy ($E_k = \frac{1}{2}mv^2$), and electrical RMS power ($P = I_{\text{rms}}^2 R$).
* **Singularity Behavior:** If $x < 0$ in real mode, `{{key:√x}}` throws `Error 01: INVALID DATA`. In Complex Mode ({{key:CMPLX}}), the square root seamlessly transitions to the complex plane: $\sqrt{-4} = 0.0000 + 2.0000i$.

### `{{key:1/x}}` (Reciprocal)
* **Mathematical Definition:** $f(x) = \frac{1}{x} = x^{-1}$.
* **Conceptual Intuition:** Provides rapid inversion of ratios, conversion from frequency to period ($T = 1/f$), optical focal power in diopters ($D = 1/f$), and conductance from resistance ($G = 1/R$).
* **Singularity Behavior:** If $x = 0$, `{{key:1/x}}` throws `Error 02: DIVIDE BY 0`.

### `{{key:yˣ}}` (General Power)
* **Mathematical Definition:** Evaluates $Y^X = \exp(X \ln Y)$.
* **Stack Layout:** The base $y$ must reside in Register $Y$; the exponent $x$ must reside in Register $X$.
* **Stack Dynamics:** Dyadic operation. $Y$ and $X$ are popped, $Y^X$ is loaded into $X$, $Z$ drops down to $Y$, and $T$ drops into $Z$ while replicating itself into $T$.

#### Worked Example: Non-Integer Exponentiation $2.5^{3.8}$
Calculate the Stefan-Boltzmann radiation scaling parameter:
$$\Phi = 2.5^{3.8}$$

Keystrokes: `{{res:sc32_03_algebra_transcendentals_seq_01:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_01:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `{{key:2}} {{key:.}} {{key:5}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.5000$ | Enter base $y$ |
| 2 | `{{key:ENTER}}` | $0.0000$ | $0.0000$ | $2.5000$ | $2.5000$ | Stack lift disabled; $y$ pushed to $Y$ |
| 3 | `{{key:3}} {{key:.}} {{key:8}}` | $0.0000$ | $0.0000$ | $2.5000$ | $3.8000$ | Overwrite $X$ with exponent $x$ |
| 4 | `{{key:yˣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$32.5216096641$** | Evaluates $2.5^{3.8}$; Stack lift armed |

### `{{key:ˣ√y}}` (Arbitrary Radical Root)
* **Mathematical Definition:** Evaluates $\sqrt[X]{Y} = Y^{1/X}$.
* **Stack Layout:** Radicand $Y$ in Register $Y$; root index $X$ in Register $X$.
* **Physical Engineering Use:** Determining compound annual growth rates (CAGR) over $n$ periods, polytropic gas expansion coefficients ($P V^n = C \implies V = \sqrt[n]{C/P}$), and geometric mean calculations.

### `{{key:x∥y}}` (Parallel Harmonic Combination)
* **Mathematical Definition:** Evaluates the harmonic mean product-over-sum:
  $$x \parallel y = \frac{x \times y}{x + y} = \frac{1}{\frac{1}{x} + \frac{1}{y}}$$
* **Physical Domain Universality:**
  * **Electrical Engineering:** Equivalent resistance of two parallel resistors ($R_{\text{eq}} = R_1 \parallel R_2$).
  * **Mechanical Engineering:** Combined spring constant of two springs in series ($k_{\text{eq}} = k_1 \parallel k_2$).
  * **Optics & Photonics:** Thin-lens focal length equation ($\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i} \implies f = d_o \parallel d_i$).
  * **Fluid Dynamics:** Fluid conductances in series pipe restrictions ($C_{\text{eq}} = C_1 \parallel C_2$).
  * **Kinematics:** Average round-trip speed over equal distances ($v_{\text{avg}} = 2(v_1 \parallel v_2)$).

<div class="admonition tip">
<p class="admonition-title">Rapid Calculation &amp; Equation Entry: Chained Quadratic Formula &amp; Law of Cosines Sprint</p>
<p>
In high-speed calculation sprints and competitive STEM exams, quadratic equations $a x^2 + b x + c = 0$ must be solved in under 6 seconds without writing intermediate terms on scratch paper. Take $2.4 x^2 + 7.8 x - 15.6 = 0$:
</p>
<p>
Evaluate the discriminant radical and chain directly into the positive root:
<br>
<code>7.8 {{key:ENTER}} {{key:x²}} 4 {{key:ENTER}} 2.4 {{key:×}} 15.6 {{key:+/-}} {{key:×}} {{key:-}} {{key:√x}}</code> &rarr; $\sqrt{b^2 - 4ac} \approx 14.5093$
<br>
Now apply $-b$ and $2a$ without touching storage registers:
<br>
<code>7.8 {{key:-}} 2 {{key:÷}} 2.4 {{key:÷}}</code> &rarr; <strong>$1.3978$</strong> (positive root in 14 keystrokes, 0 parentheses!).
</p>
<p>
Similarly for the Law of Cosines $c = \sqrt{a^2 + b^2 - 2ab\cos C}$: evaluate $a^2$, then $b^2$, add them, push $2ab\cos C$, subtract, and press <code>{{key:√x}}</code> in a continuous fluid cascade.
</p>
</div>

---

## Logarithms, Exponentials & Natural Constants

Logarithmic functions translate multiplicative physical phenomena into linear scales, serving as the mathematical backbone for acoustics, chemistry, thermodynamics, and signal processing:

| Function | Keystroke | Arity | Valid Domain | Inverse Function |
| :--- | :--- | :--- | :--- | :--- |
| **Natural Logarithm** | `{{key:LN}}` | Unary | $x > 0$ | Natural Exponential `{{key:eˣ}}` |
| **Natural Exponential** | `{{key:eˣ}}` | Unary | $-708 < x < 709$ | Natural Logarithm `{{key:LN}}` |
| **Common Logarithm** | `{{keycap:LOG}}` | Unary | $x > 0$ | Base-10 Exponential `{{keycap:10ˣ}}` |
| **Base-10 Exponential** | `{{keycap:10ˣ}}` | Unary | $-308 < x < 308$ | Common Logarithm `{{keycap:LOG}}` |
| **Euler's Number $e$** | `{{key:E}}` | $0$-ary | Constant ($\approx 2.718281828459$) | N/A |
| **Archimedes' Constant $\pi$** | `{{keycap:π}}` | $0$-ary | Constant ($\approx 3.141592653590$) | N/A |

{{blocks:algebra_lframe_grid_hero|Algebra L-Frame Grid Hardware Stage}}
*Figure 3.2: The Algebra L-Frame Grid hardware stage provides physical boundary constraints for polynomial factoring, linking tactile coordinate geometry directly to RPN stack transcendentals.*


### Mathematical Formulations
$$\ln x = \int_1^x \frac{1}{t}\,dt, \quad e^x = \sum_{k=0}^{\infty} \frac{x^k}{k!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$$
$$\log_{10} x = \frac{\ln x}{\ln 10}, \quad 10^x = e^{x \ln 10}$$

### Grounded Application 1: Radioactive Decay & Carbon-14 Dating
The radioactive decay of unstable carbon-14 ($^{14}\text{C}$) follows first-order exponential kinetics:
$$N(t) = N_0 e^{-\lambda t}$$
where the true physical (**Cambridge**) half-life is $t_{1/2} = 5,730 \pm 40\text{ years}$ (Godwin, 1962). The physical decay constant $\lambda$ is:
$$\lambda = \frac{\ln 2}{t_{1/2}} = \frac{\ln 2}{5730} \approx 1.20968 \times 10^{-4}\text{ yr}^{-1}$$

> [!NOTE]
> **Radiometric Convention — Cambridge ($5,730\text{ yr}$) vs. Libby ($5,568\text{ yr}$) Half-Life:**  
> In physical nuclear chemistry, the true mean half-life of $^{14}\text{C}$ is the **Cambridge half-life** ($5,730\text{ yr}$), which we use here to compute true physical decay time under constant atmospheric production. Note that in archaeological reporting (Stuiver & Polach, 1977), uncalibrated "Conventional Radiocarbon Ages (Years BP)" are historically calculated using Willard Libby's original $5,568\text{-year}$ half-life prior to applying dendrochronological calibration curves (`IntCal20`).

An archaeological bone specimen unearthed at an ancient dwelling retains **$23.4\%$ of its original $^{14}\text{C}$** content ($N(t)/N_0 = 0.234$). Determine the elapsed physical decay age of the artifact:
$$t = -\frac{\ln(N(t)/N_0)}{\lambda} = -\frac{\ln(0.234) \times 5730}{\ln 2}$$

#### Solution Pathway A: Step-by-Step Stack Inspection
1. Enter the remaining fraction: `0.234` `{{key:LN}}` $\rightarrow$ $X = -1.452434$
2. Enter the half-life and multiply: `5730` `{{key:×}}` $\rightarrow$ $X = -8322.447816$
3. Enter 2 and take natural log: `2` `{{key:LN}}` $\rightarrow$ $X = 0.693147$, $Y = -8322.447816$
4. Divide and negate: `{{key:÷}}` `{{key:+/-}}` $\rightarrow$ **$12,006.75\text{ years}$**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & Pedagogical State |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `0.234` `{{key:LN}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-1.4524$ | Remaining proportion and $\ln(0.234)$ |
| 2 | `5730` `{{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-8322.4478$ | Product with Cambridge half-life |
| 3 | `2` `{{key:LN}}` | $0.0000$ | $0.0000$ | $-8322.4478$ | $0.6931$ | Base 2 and $\ln(2)$ divisor |
| 4 | `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-12006.7541$ | Quotient |
| 5 | `{{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$12006.7541$** | Artifact age in years |

The bone is approximately **$12,007\text{ years old}$**.

#### Solution Pathway B: High-Speed Chained Contest Shortcut
`{{res:sc32_03_algebra_transcendentals_seq_44:keys}}`  
Total Keystrokes: 15. Zero parentheses, zero temporary storage registers.

---

### Grounded Application 2: Acoustic Sound Pressure Level (dB SPL)
Human hearing perceives sound pressure logarithmically. The sound pressure level (SPL) in decibels is defined relative to the threshold of hearing at $1\text{ kHz}$:
$$L_p = 20 \log_{10}\left(\frac{p_{\text{rms}}}{p_0}\right)\text{ dB SPL}$$
where $p_0 = 20\,\mu\text{Pa} = 2.0 \times 10^{-5}\text{ Pa}$.

An acoustic engineer measures an RMS sound pressure of **$p_{\text{rms}} = 1.45\text{ Pa}$** directly in front of a stadium loudspeaker array. Determine the sound pressure level in dB SPL:
$$L_p = 20 \log_{10}\left(\frac{1.45}{2.0 \times 10^{-5}}\right)$$

Keystrokes: `{{res:sc32_03_algebra_transcendentals_seq_02:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_02:value}}`**

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `1.45 {{key:ENTER}} 2.0 {{key:E}} 5 {{key:+/-}} {{key:÷}}` divides measured acoustic pressure by reference threshold $p_0 = 20\,\mu\text{Pa}$, yielding relative pressure ratio $72,500.0$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 72500.0000)$.
2. Striking `{{key:LOG}} 20 {{key:×}}` computes the decade power and scales by $20\text{ dB/decade}$, resolving stadium acoustic sound pressure level directly as $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{97.2068}\text{ dB SPL})$.

The stadium speaker produces **$97.2\text{ dB SPL}$**, indicating a high-intensity sound level requiring hearing protection during extended exposure.

---

### Grounded Application 3: Chemical pH & Henderson-Hasselbalch Buffer
In analytical chemistry, the acidity of an aqueous solution is governed by the hydronium ion activity:
$$\text{pH} = -\log_{10}[\text{H}_3\text{O}^+]$$
For a buffer solution containing a weak acid ($\text{HA}$) and its conjugate base ($\text{A}^-$), the pH is predicted by the Henderson-Hasselbalch equation:
$$\text{pH} = \text{pK}_a + \log_{10}\left(\frac{[\text{A}^-]}{[\text{HA}]}\right)$$

Calculate the pH of an acetic acid buffer system with:
* Acid dissociation constant: $\text{pK}_a = 4.76$
* Sodium acetate concentration: $[\text{A}^-] = 0.185\text{ M}$
* Acetic acid concentration: $[\text{HA}] = 0.120\text{ M}$

Keystrokes: `{{res:sc32_03_algebra_transcendentals_seq_03:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_03:value}}`**

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `0.185 {{key:ENTER}} 0.120 {{key:÷}}` forms the conjugate base-to-acid ratio $[\text{A}^-]/[\text{HA}] \approx 1.5417$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.5417)$.
2. Striking `{{key:LOG}} 4.76 {{key:+}}` computes the logarithmic ratio ($\approx 0.1880$) and sums baseline dissociation constant $\text{pK}_a = 4.76$, yielding buffer equilibrium $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{4.9480})$ with zero scratchpad memory.

The buffer stabilizes at **$\text{pH} = 4.95$**.

---

### Grounded Application 4: Arrhenius Chemical Reaction Kinetics
The temperature dependence of chemical reaction rate constants is governed by the Arrhenius equation:
$$k = A \exp\left(-\frac{E_a}{R T}\right)$$
Taking the natural logarithm of the ratio between two temperatures $T_1$ and $T_2$:
$$\ln\left(\frac{k_2}{k_1}\right) = -\frac{E_a}{R} \left(\frac{1}{T_2} - \frac{1}{T_1}\right) = \frac{E_a}{R} \left(\frac{1}{T_1} - \frac{1}{T_2}\right)$$
Solving for the activation energy $E_a$:
$$E_a = \frac{R \ln(k_2 / k_1)}{\frac{1}{T_1} - \frac{1}{T_2}}$$
where universal gas constant $R = 8.314462\text{ J}/(\text{mol}\cdot\text{K})$.

A polymerization reaction exhibits rate constants:
* $k_1 = 3.25 \times 10^{-4}\text{ s}^{-1}$ at $T_1 = 300\text{ K}$ ($27^\circ\text{C}$)
* $k_2 = 2.85 \times 10^{-2}\text{ s}^{-1}$ at $T_2 = 350\text{ K}$ ($77^\circ\text{C}$)

Determine the activation energy $E_a$ in $\text{kJ/mol}$:

Keystrokes:
1. Calculate denominator: `{{res:sc32_03_algebra_transcendentals_seq_45:keys}}` $\rightarrow$ $X = 0.00047619$
2. Calculate numerator: `{{res:sc32_03_algebra_transcendentals_seq_46:keys}}` $\rightarrow$ $X = 37207.24$
3. Divide numerator by denominator: `{{key:x⇄y}} {{key:÷}}` $\rightarrow$ $X = 78135.21\text{ J/mol}$
4. Convert to $\text{kJ/mol}$: `1000 {{key:÷}}` $\rightarrow$ **$78.14\text{ kJ/mol}$**

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `300 {{key:1/x}} 350 {{key:1/x}} {{key:-}}` evaluates reciprocal temperature difference $(1/T_1 - 1/T_2) \approx 0.000476\text{ K}^{-1}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.0005)$.
2. Keying `2.85 {{key:E}} 2 {{key:+/-}} {{key:ENTER}} 3.25 {{key:E}} 4 {{key:+/-}} {{key:÷}} {{key:LN}} 8.314462 {{key:×}}` evaluates numerator energy product $R \ln(k_2/k_1) \approx 37,207.24\text{ J/mol}$ while temperature denominator waits in $Y$ $(T: 0.0000, Z: 0.0000, Y: 0.0005, X: 37207.2435)$.
3. Striking `{{key:x⇄y}} {{key:÷}} 1000 {{key:÷}}` swaps, divides numerator by denominator, and converts to $\text{kJ/mol}$, producing activation energy $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{78.1352}\text{ kJ/mol})$.

---

### Grounded Application 5: Barometric Altimetry Formula
Atmospheric pressure drops exponentially with altitude above sea level:
$$P(h) = P_0 \exp\left(-\frac{M g h}{R T}\right)$$
where:
* Sea level pressure: $P_0 = 1013.25\text{ hPa}$
* Molar mass of Earth's air: $M = 0.0289644\text{ kg/mol}$
* Gravitational acceleration: $g = 9.80665\text{ m/s}^2$
* Gas constant: $R = 8.314462\text{ J}/(\text{mol}\cdot\text{K})$
* Mean atmospheric temperature: $T = 288.15\text{ K}$ ($15^\circ\text{C}$)

Determine the atmospheric pressure atop Hawaii's Mauna Kea Observatory at altitude $h = 4,207\text{ meters}$:

The exponential scale factor exponent is:
$$\kappa = \frac{M g h}{R T} = \frac{0.0289644 \times 9.80665 \times 4207}{8.314462 \times 288.15}$$

Keystrokes:
`{{res:sc32_03_algebra_transcendentals_seq_47:keys}}`

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `0.0289644 {{key:ENTER}} 9.80665 {{key:×}} 4207 {{key:×}} 8.314462 {{key:÷}} 288.15 {{key:÷}}` evaluates dimensionless potential scale height exponent $\kappa \approx 0.4988$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.4988)$.
2. Striking `{{key:+/-}} {{key:eˣ}} 1013.25 {{key:×}}` computes attenuation factor $e^{-\kappa} \approx 0.6073$ and scales by sea-level pressure $1013.25\text{ hPa}$, yielding summit barometric pressure $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{615.3168}\text{ hPa})$.

Atop Mauna Kea, atmospheric pressure is **$615.3\text{ hPa}$** (approx. $60.7\%$ of sea level pressure), explaining why astronomical observatories require supplemental oxygen equipment for summit personnel.

---

## Number Parts Functions (`{{key:PARTS}}`)

The SC-32 provides four hardware numerical decomposition primitives via Right Shift `{{key:↱}}` followed by `{{key:PARTS}}`:

| Primitive | Engine Implementation | Example Input | Result Produced | Mathematical Operation |
| :--- | :--- | :---: | :---: | :--- |
| **`IP` (INTG)** | `x.rounded(.towardZero)` | `-42.785` | `-42.0` | Integer Part truncation toward zero |
| **`FP` (FRAC)** | `x.truncatingRemainder(divBy: 1)` | `-42.785` | `-0.785` | Signed fractional remainder ($x - \text{IP}(x)$) |
| **`ABS`** | `abs(x)` | `-42.785` | `42.785` | Absolute magnitude ($\|x\| = \sqrt{x^2}$) |
| **`SGN`** | `copysign(1.0, x)` ($0 \to 0$) | `-42.785` | `-1.0` | Signum orientation vector ($\{-1, 0, +1\}$) |

{{blocks:algebra_factoring_area|Algebra Factoring Area Model}}
*Figure 3.3: The physical Algebra Factoring Stage area model $(x+2)(x+3) = x^2 + 5x + 6$, demonstrating visual and tactile decomposition alongside the SC-32 numerical parts engine.*


### Definitions & Bit-Level Invariants
1. **`IP` (Integer Part):** Truncates any decimal fractional value toward zero:
   $$\text{IP}(x) = \begin{cases} \lfloor x \rfloor & x \ge 0 \\ \lceil x \rceil & x < 0 \end{cases}$$
2. **`FP` (Fractional Part):** The signed remainder after extracting the integer component:
   $$\text{FP}(x) = x - \text{IP}(x)$$
   *Bit-Level Identity Guarantee:* For any floating-point number $x$, the identity:
   $$\text{IP}(x) + \text{FP}(x) \equiv x$$
   is preserved down to the 53rd bit of the IEEE-754 mantissa.
3. **`ABS` (Absolute Value):** Clears the sign bit of Register $X$, guaranteeing non-negative magnitude: $|x| = \sqrt{x^2}$.
4. **`SGN` (Signum):** Returns the unit orientation vector of Register $X$:
   $$\text{sgn}(x) = \begin{cases} +1.0 & x > 0 \\ 0.0 & x = 0 \\ -1.0 & x < 0 \end{cases}$$

### Practical Application: Decomposing Decimal Hours into Hours, Minutes, and Seconds
An astronomical tracking observation records an elapsed telescope exposure time of **$14.736\text{ decimal hours}$**. Convert this value into integer hours, integer minutes, and decimal seconds:

Keystrokes:
1. Store initial value: `14.736 {{key:STO}} 0`
2. Extract hours: `{{key:PARTS}} {{key:IP}}` $\rightarrow$ **$14\text{ hours}$**
3. Extract minutes: `{{key:RCL}} 0 {{key:PARTS}} {{key:FP}} 60 {{key:×}}` $\rightarrow$ $X = 44.16\text{ minutes}$
4. Extract integer minutes: `{{key:ENTER}} {{key:PARTS}} {{key:IP}}` $\rightarrow$ **$44\text{ minutes}$**
5. Extract seconds: `{{key:x⇄y}} {{key:PARTS}} {{key:FP}} 60 {{key:×}}` $\rightarrow$ **$9.60\text{ seconds}$**

The exposure time is precisely **$14\text{ hours}, 44\text{ minutes}, 9.6\text{ seconds}$**.

---

## Factorials & The Lanczos Gamma Extension ($70!$)

The SC-32 factorial key `{{key:x!}}` evaluates both discrete integer factorials and continuous real values via the **Lanczos 9-term approximation to the Euler Gamma function**:
$$x! = \Gamma(x + 1) = \int_0^{\infty} t^x e^{-t}\,dt$$

<div class="admonition note">
<p class="admonition-title">Lanczos Gamma Convergence &amp; 70! Exponent Preservation</p>
<ul>
  <li><strong>Discrete Integers ($n = 0, 1, 2 \dots 70$):</strong> Evaluates exact factorial products $n! = \prod_{k=1}^n k = 1 \times 2 \times 3 \times \dots \times n$.</li>
  <li><strong>Real &amp; Non-Integer Arguments ($x \in \mathbb{R}$):</strong> Evaluates the continuous Euler Gamma function $\Gamma(x + 1) = \int_0^\infty t^x e^{-t}\,dt$ via a 9-pole Lanczos rational approximation yielding certified relative accuracy exceeding $10^{-15}$.</li>
  <li><strong>The $70!$ Exponent Breakthrough:</strong> Evaluates $70! = 1.197857166996989 \times 10^{100}$ seamlessly, transcending the vintage 2-digit exponent ceiling ($9.999999999 \times 10^{99}$) that halted classic pocket machines at $69!$.</li>
</ul>
</div>

### The 70! Overflow Barrier
Most vintage calculators overflow at $69! \approx 1.711224524 \times 10^{98}$ because their internal registers only allocate 2 decimal digits for the base-10 exponent (`E00` to `E99`).

The SC-32 features 16-bit signed binary exponent packing (supporting exponents up to $\pm 308$). It computes:
$$70! = 1.197857166996989 \times 10^{100}$$
Display: `1.1978571670 E100`

### Non-Integer Arguments (Half-Integers)
Evaluating `{{res:sc32_03_algebra_transcendentals_seq_48:keys}}` computes $\Gamma(1.5)$:
$$\left(\frac{1}{2}\right)! = \Gamma\left(\frac{3}{2}\right) = \frac{\sqrt{\pi}}{2} \approx 0.886226925453$$

Keystrokes: `{{res:sc32_03_algebra_transcendentals_seq_04:keys}}`$\rightarrow$ Display: **`{{res:sc32_03_algebra_transcendentals_seq_04:value}}`**  
Verify via Pi constant: `{{res:sc32_03_algebra_transcendentals_seq_49:keys}}` $\rightarrow$ Display: **`{{res:sc32_03_algebra_transcendentals_seq_49:value}}`**. The two calculations match to the 12th decimal place!

---

## Display Formatting Modes (`FIX`, `SCI`, `ENG`, `ALL`)

The SC-32 provides four display formatting modes accessed via Left Shift `{{key:↰}}` followed by `{{key:DISP}}`:

| Mode | Invocation Syntax | Display Example for `1234.5678` | Engine Presentation Behavior |
| :--- | :--- | :--- | :--- |
| **`FIX`** | {{key:FIX}}` n` | `1234.57` (for $n=2$) | Fixed decimal places ($0 \le n \le 9$) with standard half-up rounding |
| **`SCI`** | {{key:SCI}}` n` | `1.23 E03` (for $n=2$) | Normalized scientific notation: single non-zero leading digit |
| **`ENG`** | {{key:ENG}}` n` | `1.23 E03` (for $n=2$) | Engineering notation: power-of-10 exponent forced to a multiple of 3 |
| **`ALL`** | `{{key:ALL}}` | `1234.5678` | Full mantissa precision displayed; suppresses trailing zeros |

### The Non-Destructive Display Invariant
> [!NOTE] **Core Architectural Invariant:**  
> Changing the display formatting mode **never modifies or truncates the internal precision of the numbers stored in Registers $X, Y, Z, T$**. The floating-point mantissa retains full 64-bit IEEE-754 precision (15–17 decimal digits). Formatting alters only the visual presentation on the LCD.

### Engineering Notation (`ENG`) in Electronic Circuits
In electronic engineering, physical quantities align with metric engineering prefixes (pico $10^{-12}$, nano $10^{-9}$, micro $10^{-6}$, milli $10^{-3}$, kilo $10^3$, mega $10^6$, giga $10^9$).

Setting `{{key:ENG}} 2` ensures that the exponent is always forced to a multiple of 3:
* Evaluating capacitor impedance: $X = 0.0000047 \implies$ Display: `4.70 E-06` ($4.7\,\mu\text{F}$).
* Evaluating RF carrier frequency: $X = 145000000 \implies$ Display: `145.00 E06` ($145\text{ MHz}$).

---

## Diagnostic Checkpoints & Self-Tests

> **Diagnostic Checkpoint 3.1: Logarithm Domain Protection**
> Attempt to evaluate $\ln(-5)$ by entering `{{res:sc32_03_algebra_transcendentals_seq_50:keys}}`.
> *Expected Result:* The display halts with `Error 01: INVALID DATA`. Press `{{key:C}}` to clear the error state. Notice that the prior stack contents in $Y, Z,$ and $T$ were preserved intact.

> **Diagnostic Checkpoint 3.2: Exponent Overflow Boundary**
> Enter `1 {{key:E}} 308` and press `{{key:ENTER}} 10 {{key:×}}`.
> *Expected Result:* The display reports `Error 03: OVERFLOW`. The SC-32 guards against silent infinity corruption by flagging any arithmetic operation that exceeds the IEEE-754 binary64 range ($1.797 \times 10^{308}$).

---

## Special Functions, Numerical Conditioning & Error Propagation

To maintain 12-digit certified accuracy across the entire floating-point domain, the SC-32 mathematical engine implements specialized numerical algorithms that protect against catastrophic loss of significance.

<div class="admonition warning">
<p class="admonition-title">Transcendental Conditioning &amp; Catastrophic Cancellation</p>
<ol>
  <li><strong>The Condition Number of a Function:</strong>
    $$C(x) = \left| \frac{x f'(x)}{f(x)} \right|$$
    When $C(x) \gg 1$, minute input perturbations produce massive relative output swings. For the exponential function $f(x) = e^x$, $C(x) = |x|$. As $x$ grows large, maintaining 12-digit certified precision demands Cody &amp; Waite range reduction modulo $\ln 2$ with extended mantissa arithmetic.</li>
  <li><strong>Catastrophic Cancellation in $e^x - 1$:</strong>
    For small arguments $|x| < 10^{-4}$, naive floating-point evaluation of $e^x$ rounds to $1.0000\dots$, discarding the lowest significand bits. Subtracting $1$ subsequently cancels all significant leading bits, leaving only numerical truncation noise. The SC-32 mathematical engine incorporates Cody &amp; Waite polynomial branches and an internal <code>expm1(x)</code> series expansion ($x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$) when $|x| \ll 1$.</li>
  <li><strong>Lanczos &amp; Stirling Asymptotic Accuracy:</strong>
    For large factorials, Stirling's expansion $n! \sim \sqrt{2\pi n}\,(n/e)^n (1 + \frac{1}{12n} + \dots)$ is superseded by the SC-32's 9-pole rational Chebyshev approximation, maintaining relative truncation error strictly below $10^{-15}$ across both real and complex domains.</li>
</ol>
</div>

---

## Engineering Design Briefing: Deep Space Telemetry & Acoustic Decibel Engineering (Problems 3.1 through 3.30)

> **Hands-On Studio Proof: Blocks &rarr; Calculator**  
> Before running numerical logarithms and exponential cascades on the SC-32, manipulate physical logarithmic rods on the bilateral Prime Studio comparator stage (`docs/assets/manuals/prime_studio_comparator_stage.png`) and factoring tiles on the Algebra L-Frame Grid (`docs/assets/renders/algebra-lframe-grid-hero.png`). Visualizing exponential scale dilation and polynomial factoring areas physically grounds the 64-bit IEEE-754 mantissa transformations executed on the RPN stack.

The following 30 professional engineering case studies span deep space telemetry, acoustic decibel attenuation, chemical kinetics, and mechanical spring dynamics.


---

### Problem 3.1: RC Low-Pass Filter Discharge Time Constant
**Electrical Engineering Context:** An RC timing network ($R = 150\text{ k}\Omega$, $C = 47\,\mu\text{F}$, $\tau = RC = 7.05\text{ s}$) discharges from $V_0 = 12.0\text{ V}$. Find time $t$ required for capacitor voltage to decay to $10\%$ of initial voltage ($V/V_0 = 0.10$):
$$V(t) = V_0 e^{-t/\tau} \implies t = - \tau \ln(0.10) = - (150 \times 10^3)(47 \times 10^{-6}) \ln(0.10)$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_05:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_05:value}}`**

**4-Level Stack Trace:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `150000` `{{key:ENTER}}` | $0.0000$ | $0.0000$ | $150000.000$ | $150000.000$ | Load resistance $R$ in $\Omega$ |
| `47` `{{key:E}}` `6` `{{key:+/-}}` `{{key:×}}`| $0.0000$ | $0.0000$ | $0.0000$ | $7.050000$ | Time constant $\tau = RC = 7.05\text{ s}$ |
| `0.10` `{{key:LN}}` | $0.0000$ | $0.0000$ | $7.050000$ | $-2.302585$ | $\ln(0.10)$ natural logarithm |
| `{{key:×}}` `{{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$16.233225$** | Discharge time in seconds |

> **Homeschooler Diagnostic Checkpoint 3.3:**
> Did your screen display $Y = 7.0500$ and $X = -2.3026$ after pressing `{{key:LN}}`?
> *If you see $X = -1.0000$,* you pressed `{{key:LOG}}` (common base-10 log) instead of `{{key:LN}}` (natural log). Press `{{key:LASTX}}` and press `{{key:LN}}` to recover.

---

### Problem 3.2: Geological Age via Potassium-Argon ($^{40}\text{K} \to {}^{40}\text{Ar}$) Dating
**Geophysics Context:** Volcanic basalt contains atomic ratio $^{40}\text{Ar} / {}^{40}\text{K} = 0.0850$. With decay constant $\lambda = 5.543 \times 10^{-10}\text{ yr}^{-1}$ and branching ratio coefficient $C = 9.54$:
$$t = \frac{1}{\lambda} \ln\left(1 + C \cdot \frac{{}^{40}\text{Ar}}{{}^{40}\text{K}}\right) = \frac{\ln(1 + 9.54 \times 0.0850)}{5.543 \times 10^{-10}}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_06:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_06:value}}`**

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `9.54 {{key:ENTER}} 0.0850 {{key:×}} 1 {{key:+}}` evaluates the accumulation argument $(1 + C \cdot \text{ratio}) = 1.8109$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.8109)$.
2. Striking `{{key:LN}} 5.543 {{key:E}} 10 {{key:+/-}} {{key:÷}}` takes the natural logarithm ($\approx 0.5938$) and divides by decay constant $\lambda$, resolving rock formation age $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{1.0713 \times 10^{9}}\text{ yr})$ ($1.071\text{ billion years}$) without scratchpad registers.

---

### Problem 3.3: Blood Bicarbonate Buffer System pH
**Biomedical Physiology Context:** Human blood plasma maintains pH via the carbonic acid-bicarbonate buffer ($\text{pK}_a = 6.10$). Clinical blood gas analysis measures bicarbonate $[\text{HCO}_3^-] = 24.0\text{ mEq/L}$ and dissolved carbon dioxide $[\text{CO}_2] = 1.20\text{ mEq/L}$:
$$\text{pH} = \text{pK}_a + \log_{10}\left(\frac{[\text{HCO}_3^-]}{[\text{CO}_2]}\right) = 6.10 + \log_{10}\left(\frac{24.0}{1.20}\right)$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_07:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_07:value}}`**.

> **Named RPN Stack Idiom: *The x⇄y Denominator Flip & Logarithmic Buffer Ratio*** — Compute base-to-acid ratio directly on the stack, take $\log_{10}$ in place, and add $\text{pK}_a$ without parentheses {{cite:hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `24.0 {{key:ENTER}} 1.20 {{key:÷}}` loads bicarbonate concentration ($24.0\text{ mEq/L}$) into $Y$, enters dissolved carbon dioxide ($1.20\text{ mEq/L}$), and divides, forming clinical buffer ratio $20.00$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 20.0000)$.
2. Striking `{{key:LOG}} 6.10 {{key:+}}` computes $\log_{10}(20.0) \approx 1.3010$ and adds baseline dissociation constant $\text{pK}_a = 6.10$, yielding physiological arterial blood pH $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{7.4010})$ without grouping syntax.

---

### Problem 3.4: Fiber Optic Cable Total Attenuation & Output Power
**Telecommunications Context:** Optical pulse of power $P_{\text{in}} = 15.0\text{ mW}$ transmitted through single-mode silica fiber of length $L = 65.0\text{ km}$ with attenuation coefficient $\alpha = 0.22\text{ dB/km}$:
$$\text{Loss}_{\text{dB}} = \alpha \cdot L = 0.22 \times 65.0 = 14.30\text{ dB}$$
$$P_{\text{out}} = P_{\text{in}} \cdot 10^{-\text{Loss}_{\text{dB}} / 10} = 15.0 \cdot 10^{-1.430}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_08:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_08:value}}`**$\text{ mW} = 556.7\,\mu\text{W}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `0.22 {{key:ENTER}} 65 {{key:×}} 10 {{key:÷}} {{key:+/-}}` computes total insertion loss ($14.30\text{ dB}$) and scales to negative decade exponent $-\text{Loss}/10 = -1.4300$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: -1.4300)$.
2. Striking `{{key:10ˣ}} 15 {{key:×}}` evaluates power transmission throughput factor ($10^{-1.43} \approx 0.0372$) and scales by launch power $15.0\text{ mW}$, resolving received detector power $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{0.5573}\text{ mW})$ ($557.3\,\mu\text{W}$).

---

### Problem 3.5: Photovoltaic Cell Shockley Diode Equation
**Semiconductor Physics Context:** A silicon solar cell with reverse saturation current $I_s = 1.8 \times 10^{-11}\text{ A}$ operates at $T = 300\text{ K}$ with ideality factor $n = 1.25$ ($k T / q = 0.025852\text{ V}$ at $300\text{ K}$). Find forward current at terminal voltage $V = 0.58\text{ V}$:
$$I = I_s \left[\exp\left(\frac{V}{n \cdot V_t}\right) - 1\right] = 1.8 \times 10^{-11} \left[\exp\left(\frac{0.58}{1.25 \times 0.025852}\right) - 1\right]$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_09:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_09:value}}`**

> **Named RPN Stack Idiom: *The Inside-Out Exponential Diode Pipeline*** — Compute the junction voltage ratio $V/(n V_t)$ inside-out via single-`ENTER` chain division, exponentiate, subtract 1, and scale by saturation current without scratchpad storage {{cite:horowitz2015,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `0.58` `{{key:ENTER}}` — Load solar cell forward bias terminal potential ($V = 0.58\text{ V}$) into $Y$.
2. `1.25` `{{key:÷}}` `0.025852` `{{key:÷}}` — Chain divide by ideality factor ($n = 1.25$) and thermal voltage ($V_t = 0.025852\text{ V}$); dimensionless diode activation argument ($V/(nV_t) \approx 17.9483$) occupies $X$.
3. `{{key:eˣ}}` `1` `{{key:-}}` — Evaluate natural exponential in place ($e^{17.9483} \approx 6.2351 \times 10^7$) and subtract unity reference.
4. `1.8 {{key:E}} 11 {{key:+/-}}` `{{key:×}}` — Scale by reverse saturation current ($I_s = 1.8 \times 10^{-11}\text{ A}$); generated photovoltaic forward current ($I = 1.1223 \times 10^{-3}\text{ A} = 1.122\text{ mA}$) evaluates without grouping overhead.

Stack: Exponent $= 17.9483$, $e^{17.9483} \approx 6.235 \times 10^7$, Current $I \approx \mathbf{0.001122\text{ A}} = 1.122\text{ mA}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `0.58 {{key:ENTER}} 1.25 {{key:÷}} 0.025852 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $17.9483$ | Chain division for diode activation argument $V/(n V_t)$ |
| 2 | `{{key:eˣ}} 1 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $6.2353 \times 10^{7}$ | Exponential emission factor $(e^{V/nV_t} - 1)$ |
| 3 | `1.8 {{key:E}} 11 {{key:+/-}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.0011$** | Scale by saturation current $I_s$ for forward current $I$ (A) |

---

### Problem 3.6: Tsiolkovsky Rocket Equation Burnout Velocity
**Aerospace Context:** Single-stage orbital rocket with effective exhaust velocity $v_e = 3,150\text{ m/s}$ and mass ratio $m_0 / m_f = 9.20$ ($m_0 = \text{wet mass}, m_f = \text{dry mass}$):
$$\Delta v = v_e \ln\left(\frac{m_0}{m_f}\right)$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_10:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_10:value}}`**$\text{ m/s} \approx 6.99\text{ km/s}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `9.20 {{key:LN}}` evaluates the natural logarithm of the propellant mass ratio $\ln(9.20) \approx 2.2192$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 2.2192)$.
2. Striking `3150 {{key:×}}` scales by effective exhaust velocity $v_e = 3150\text{ m/s}$, producing total mission burnout velocity increment $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{6990.4910}\text{ m/s})$ ($\approx 6.99\text{ km/s}$) in two keystrokes.

---

### Problem 3.7: Richter Earthquake Seismic Energy Ratio
**Seismology Context:** Gutenberg-Richter relation comparing seismic energy released by a magnitude $M_2 = 7.8$ earthquake versus an $M_1 = 5.2$ earthquake:
$$\frac{E_2}{E_1} = 10^{1.5 (M_2 - M_1)}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_11:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_11:value}}`**.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `7.8 {{key:ENTER}} 5.2 {{key:-}} 1.5 {{key:×}}` evaluates the seismic magnitude difference ($\Delta M = 2.6$) and multiplies by slope $1.5$, forming decade energy exponent $3.9000$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 3.9000)$.
2. Striking `{{key:10ˣ}}` exponentiates in place, yielding relative radiated seismic energy ratio $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{7943.2823})$—proving a 2.6-magnitude difference releases nearly 8,000 times more destructive energy {{cite:ellenberg2014}}.

The magnitude 7.8 earthquake releases nearly 8,000 times more seismic energy!

---

### Problem 3.8: Barometric Altitude Determination from Pressure
**Aviation Context:** Aircraft altimeter reads static ambient pressure $P = 725.0\text{ hPa}$ ($P_0 = 1013.25\text{ hPa}$, scale height $H_s = 8434\text{ meters}$):
$$h = - H_s \ln\left(\frac{P}{P_0}\right)$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_12:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_12:value}}`**$\text{ meters} \approx 9,275\text{ ft}$.

> **Named RPN Stack Idiom: *The LASTX Dual-Branch Trick & Logarithmic Pressure Scale*** — Form static pressure ratio $P/P_0$, take natural log in place, and scale by atmospheric scale height with zero scratch registers {{cite:hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `725 {{key:ENTER}} 1013.25 {{key:÷}} {{key:LN}}` computes static ambient pressure ratio $P/P_0 \approx 0.7155$ and takes the natural logarithm ($-0.3347$) in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: -0.3347)$.
2. Striking `8434 {{key:×}} {{key:+/-}}` scales by atmospheric scale height $H_s = 8434\text{ m}$ and negates, resolving true barometric altitude $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{2823.2529}\text{ m})$ ($\approx 9,263\text{ ft}$) directly.

---

### Problem 3.9: Planck Blackbody Spectral Radiance
**Quantum Physics Context:** Spectral radiance of solar photosphere ($T = 5778\text{ K}$) at green peak $\lambda = 500\text{ nm} = 5.0 \times 10^{-7}\text{ m}$:
$$B_\lambda(T) = \frac{2 h c^2}{\lambda^5 \left(e^{\frac{h c}{\lambda k T}} - 1\right)}$$
Given: $c_1 = 2 h c^2 = 1.19104 \times 10^{-16}\text{ W}\cdot\text{m}^2$, $c_2 = h c / k = 0.0143878\text{ m}\cdot\text{K}$.
Exponent: $x = \frac{c_2}{\lambda T} = \frac{0.0143878}{5.0 \times 10^{-7} \times 5778} = 4.98020$.

**Keystrokes:**
`{{res:sc32_03_algebra_transcendentals_seq_13:keys}}`

> **Named RPN Stack Idiom: *The Inside-Out Exponential & Fifth-Power Radiation Ratio*** — Evaluate the photon energy ratio $hc/(\lambda k T)$ from within, exponentiate, subtract 1, and divide the radiation constant without register allocation {{cite:strogatz2019,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `0.0143878` `{{key:ENTER}}` — Key second radiation constant ($c_2 = hc/k = 0.0143878\text{ m}\cdot\text{K}$) into $Y$.
2. `5.0 {{key:E}} 7 {{key:+/-}}` `{{key:÷}}` — Enter green peak wavelength ($\lambda = 500\text{ nm} = 5.0 \times 10^{-7}\text{ m}$) and divide; intermediate wavelength constant forms in $X$.
3. `5778` `{{key:÷}}` — Enter solar photosphere temperature ($T = 5778\text{ K}$) and divide; dimensionless exponential argument ($x = 4.98020$) forms in $X$.
4. `{{key:eˣ}}` `1` `{{key:-}}` — Exponentiate and subtract 1 in place; quantum denominator factor ($e^x - 1 \approx 144.5035$) appears in $X$.
5. `1.19104 {{key:E}} 16 {{key:+/-}}` `{{key:ENTER}}` — Load first radiation constant ($c_1 = 2hc^2 = 1.19104 \times 10^{-16}\text{ W}\cdot\text{m}^2$) into $Y$, holding quantum factor in $Z$.
6. `5.0 {{key:E}} 7 {{key:+/-}}` `{{key:ENTER}}` `5` `{{key:yˣ}}` — Raise wavelength to fifth power ($\lambda^5 = 3.125 \times 10^{-32}\text{ m}^5$) in place.
7. `{{key:÷}}` — Divide $c_1$ by $\lambda^5$; raw emissive power density ($3.8113 \times 10^{15}$) condenses into $X$.
8. `{{key:x⇄y}}` `{{key:÷}}` — Swap and divide by quantum denominator; peak spectral solar radiance ($B_\lambda = 2.6375 \times 10^{13}\text{ W/(m}^3\cdot\text{sr)}$) yields the final radiance.

Result: $B_\lambda \approx \mathbf{2.632 \times 10^{13}\text{ W}/(\text{m}^3\cdot\text{sr})}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `4.98020 {{key:eˣ}} 1 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $144.5035$ | Planck photon distribution denominator $(e^x - 1)$ |
| 2 | `1.19104 {{key:E}} 16 {{key:+/-}} {{key:ENTER}}` | $0.0000$ | $144.5035$ | $1.1910 \times 10^{-16}$ | $1.1910 \times 10^{-16}$ | Load first radiation constant $2hc^2$ |
| 3 | `5.0 {{key:E}} 7 {{key:+/-}} {{key:ENTER}} 5 {{key:yˣ}} {{key:÷}}` | $144.5035$ | $144.5035$ | $144.5035$ | $3.8113 \times 10^{15}$ | Divide by wavelength to fifth power $\lambda^5$ |
| 4 | `{{key:x⇄y}} {{key:÷}}` | $144.5035$ | $144.5035$ | $144.5035$ | **$2.6375 \times 10^{13}$** | Divide spectral power by photon denominator for radiance $B_\lambda$ |

---

### Problem 3.10: Semiconductor Intrinsic Carrier Concentration
**Materials Science Context:** Silicon intrinsic carrier density at $T = 300\text{ K}$ ($B = 5.23 \times 10^{15}\text{ cm}^{-3}\text{K}^{-3/2}$, bandgap $E_g = 1.12\text{ eV}$, $k = 8.61733 \times 10^{-5}\text{ eV/K}$):
$$n_i = B T^{3/2} \exp\left(-\frac{E_g}{2 k T}\right)$$

**Keystrokes:**
`{{res:sc32_03_algebra_transcendentals_seq_14:keys}}`

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `1.12` `{{key:ENTER}}` — Enter silicon bandgap energy ($E_g = 1.12\text{ eV}$) into $Y$.
2. `2` `{{key:ENTER}}` — Key thermal pairing factor ($2$) into $Y$.
3. `8.61733 {{key:E}} 5 {{key:+/-}}` `{{key:×}}` — Multiply by Boltzmann constant in eV ($k = 8.61733 \times 10^{-5}\text{ eV/K}$); thermal constant forms in $X$.
4. `300` `{{key:×}}` — Scale by room temperature ($T = 300\text{ K}$); bandgap thermal denominator ($2kT = 0.051704\text{ eV}$) forms in $X$.
5. `{{key:÷}}` — Divide bandgap by thermal denominator; normalized activation ratio ($21.6618$) appears in $X$.
6. `{{key:+/-}}` `{{key:eˣ}}` — Negate and exponentiate in place; Boltzmann distribution factor ($\exp(-E_g/2kT) \approx 3.9124 \times 10^{-10}$) forms in $X$.
7. `5.23 {{key:E}} 15` `{{key:×}}` — Multiply by material density constant ($B = 5.23 \times 10^{15}\text{ cm}^{-3}\text{K}^{-3/2}$); prefactor product ($2.0462 \times 10^6$) occupies $X$.
8. `300` `{{key:ENTER}}` `1.5` `{{key:yˣ}}` — Evaluate temperature density growth ($T^{3/2} = 300^{1.5} \approx 5196.15$) in place.
9. `{{key:×}}` — Multiply by temperature factor; intrinsic carrier density ($n_i = 1.0632 \times 10^{10}\text{ cm}^{-3}$) is evaluated with zero auxiliary memory.

Result: $n_i \approx \mathbf{1.045 \times 10^{10}\text{ cm}^{-3}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `1.12 {{key:ENTER}} 2 {{key:ENTER}} 8.61733 {{key:E}} 5 {{key:+/-}} {{key:×}} 300 {{key:×}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $21.6618$ | Bandgap thermal activation exponent $E_g/(2 k T)$ |
| 2 | `{{key:+/-}} {{key:eˣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.9121 \times 10^{-10}$ | Boltzmann activation factor $\exp(-E_g/2kT)$ |
| 3 | `300 {{key:ENTER}} 1.5 {{key:yˣ}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0328 \times 10^{-6}$ | Scale by density-of-states temperature factor $T^{3/2}$ |
| 4 | `5.23 {{key:E}} 15 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1.0631 \times 10^{10}$** | Multiply by material coefficient for intrinsic carrier density $n_i$ ($\text{cm}^{-3}$) |

---

### Problem 3.11: Arrhenius Diffusion Coefficient in Austenite Steel
**Metallurgy Context:** Carbon diffusion in FCC iron at $T = 1200\text{ K}$ ($D_0 = 2.3 \times 10^{-5}\text{ m}^2/\text{s}$, activation energy $Q = 148\text{ kJ/mol} = 148,000\text{ J/mol}$, $R = 8.31446\text{ J/mol}\cdot\text{K}$):
$$D = D_0 \exp\left(-\frac{Q}{R T}\right)$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_15:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_15:value}}`** $\times 10^{-12}\text{ m}^2/\text{s}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `148000 {{key:ENTER}} 8.31446 {{key:ENTER}} 1200 {{key:×}} {{key:÷}}` evaluates the activation exponent $Q/(RT) \approx 14.8336$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 14.8336)$.
2. Striking `{{key:+/-}} {{key:eˣ}} 2.3 {{key:E}} 5 {{key:+/-}} {{key:×}}` negates, exponentiates to Boltzmann probability $3.6129 \times 10^{-7}$, and scales by pre-exponential $D_0$, resolving carbon diffusivity $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{8.3096 \times 10^{-12}}\text{ m}^2/\text{s})$ without scratchpad memory.

---

### Problem 3.12: Astronomical Apparent Magnitude and Stellar Luminosity
**Astrophysics Context:** Sirius ($m_1 = -1.46$) vs Polaris ($m_2 = +1.98$). Find luminosity brightness ratio:
$$\frac{L_1}{L_2} = 10^{0.4 (m_2 - m_1)}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_16:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_16:value}}`**.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `1.98 {{key:ENTER}} 1.46 {{key:+/-}} {{key:-}} 0.4 {{key:×}}` evaluates apparent magnitude difference $\Delta m = 3.44$ and multiplies by $0.4$, forming decade luminance exponent $1.3760$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.3760)$.
2. Striking `{{key:10ˣ}}` exponentiates in place, yielding visual brightness ratio $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{23.7684})$—proving Sirius shines nearly 24 times brighter than Polaris with zero scratchpad memory.

Sirius appears $\approx 23.8$ times brighter than Polaris.

---

### Problem 3.13: Permeability and Darcy Fluid Flow in Porous Sandstone
**Petroleum Geology Context:** Core plug ($L = 0.050\text{ m}$, cross-section $A = 0.00125\text{ m}^2$) under pressure drop $\Delta P = 250\text{ kPa} = 250,000\text{ Pa}$ with crude oil viscosity $\mu = 0.035\text{ Pa}\cdot\text{s}$ produces volumetric flow $Q = 1.8 \times 10^{-7}\text{ m}^3/\text{s}$. Find permeability $k$ in Darcy ($1\text{ D} = 9.86923 \times 10^{-13}\text{ m}^2$):
$$k = \frac{Q \cdot \mu \cdot L}{A \cdot \Delta P}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_17:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_17:value}}`**$\text{ Darcy}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `1.8 {{key:E}} 7 {{key:+/-}} {{key:ENTER}} 0.035 {{key:×}} 0.050 {{key:×}}` forms Darcy numerator $Q \mu L = 3.15 \times 10^{-10}\text{ N}\cdot\text{s}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 3.1500 \times 10^{-10})$.
2. Keying `0.00125 {{key:ENTER}} 250000 {{key:×}} {{key:÷}}` builds denominator $A \Delta P = 312.5\text{ N}$ and divides, yielding SI permeability $1.0080 \times 10^{-12}\text{ m}^2$ in $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.0080 \times 10^{-12})$.
3. Striking `9.86923 {{key:E}} 13 {{key:+/-}} {{key:÷}}` converts to Darcys, displaying sandstone core permeability $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{1.0214}\text{ Darcy})$ directly.

---

### Problem 3.14: Shannon-Hartley Information Capacity Limit
**Information Theory Context:** Channel bandwidth $B = 20.0\text{ MHz} = 2.0 \times 10^7\text{ Hz}$ with signal-to-noise ratio $\text{SNR} = 30.0\text{ dB}$ ($\text{SNR}_{\text{linear}} = 10^{30/10} = 1000$):
$$C = B \log_2(1 + \text{SNR}) = B \frac{\ln(1 + \text{SNR})}{\ln 2}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_18:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_18:value}}`**$\text{ Mbps}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `1001 {{key:LN}} 2 {{key:LN}} {{key:÷}}` evaluates base-2 spectral efficiency $\log_2(1001) \approx 9.9672\text{ bits/s/Hz}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 9.9672)$.
2. Striking `20 {{key:E}} 6 {{key:×}} 1 {{key:E}} 6 {{key:÷}}` scales by bandwidth $B = 20\text{ MHz}$ and normalizes to Mbps, resolving channel capacity $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{199.3445}\text{ Mbps})$ with zero parenthetical overhead.

---

### Problem 3.15: Clausius-Clapeyron Saturated Vapor Pressure
**Thermodynamic Chemistry Context:** Water vapor pressure at $T = 333.15\text{ K}$ ($60.0^\circ\text{C}$), given enthalpy of vaporization $\Delta H_{\text{vap}} = 40,660\text{ J/mol}$, normal boiling point $T_0 = 373.15\text{ K}$ at $P_0 = 101.325\text{ kPa}$, $R = 8.31446\text{ J/mol}\cdot\text{K}$:
$$\ln\left(\frac{P}{P_0}\right) = -\frac{\Delta H_{\text{vap}}}{R} \left(\frac{1}{T} - \frac{1}{T_0}\right)$$

**Keystrokes:**
`{{res:sc32_03_algebra_transcendentals_seq_19:keys}}`

> **Named RPN Stack Idiom: *The x⇄y Denominator Flip & Vapor Pressure Pipeline*** — Invert absolute temperatures to evaluate the thermal differential $(1/T_0 - 1/T)$, scale by vaporization enthalpy, and exponentiate to find saturated vapor pressure without scratch registers {{cite:hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `373.15` `{{key:1/x}}` — Load reciprocal of normal boiling point ($1/T_0 = 1/373.15 = 2.67988 \times 10^{-3}\text{ K}^{-1}$) into $X$.
2. `393.15` `{{key:1/x}}` — Key operating autoclave temperature and invert ($1/T = 1/393.15 = 2.54356 \times 10^{-3}\text{ K}^{-1}$); stack lift preserves $1/T_0$ in $Y$.
3. `{{key:-}}` — Subtract reciprocal temperatures; inverse thermal span ($1.36323 \times 10^{-4}\text{ K}^{-1}$) forms in $X$.
4. `40660` `{{key:ENTER}}` `8.31446` `{{key:÷}}` — Evaluate molar enthalpy factor ($\Delta H_{\text{vap}}/R = 40,660 / 8.31446 = 4890.27\text{ K}$) in place.
5. `{{key:×}}` — Multiply enthalpy factor by thermal span; logarithmic vapor pressure factor ($\ln(P/P_0) = 0.66665$) appears in $X$.
6. `{{key:eˣ}}` — Exponentiate in place; relative pressure ratio ($P/P_0 = 1.9477$) condenses in $X$.
7. `101.325` `{{key:×}}` — Scale by standard atmospheric pressure ($P_0 = 101.325\text{ kPa}$); autoclave saturated steam pressure ($P = 197.35\text{ kPa}$) evaluates without grouping syntax.

Result: $P \approx \mathbf{19.923\text{ kPa}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `333.15 {{key:1/x}} 373.15 {{key:1/x}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.2176 \times 10^{-4}$ | Reciprocal temperature differential $(1/T_1 - 1/T_2)$ |
| 2 | `40660 {{key:ENTER}} 8.31446 {{key:÷}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.5735$ | Scale by enthalpy of vaporization $\Delta H_{\text{vap}}/R$ |
| 3 | `{{key:+/-}} {{key:eˣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.2073$ | Clausius-Clapeyron exponential pressure factor |
| 4 | `101.325 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$21.0063$** | Scale by reference pressure $P_1$ for vapor pressure $P_2$ (kPa) |

---

### Problem 3.16: Chemical Reaction Equilibrium Constant from $\Delta G^\circ$
**Physical Chemistry Context:** Standard Gibbs free energy change $\Delta G^\circ = -33.3\text{ kJ/mol} = -33300\text{ J/mol}$ at $T = 298.15\text{ K}$:
$$K = \exp\left(-\frac{\Delta G^\circ}{R T}\right)$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_20:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_20:value}}`**.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `33300 {{key:ENTER}}` loads the standard reaction Gibbs free energy change $\Delta G^\circ = 33,300\text{ J/mol}$ into Register $Y$ and replicates into $X$ $(T: 0.0000, Z: 0.0000, Y: 33300.0000, X: 33300.0000)$.
2. Keying `8.31446 {{key:ENTER}} 298.15 {{key:×}} {{key:÷}}` evaluates the ambient thermal energy denominator $R T \approx 2478.96\text{ J/mol}$ and divides into $\Delta G^\circ$, yielding dimensionless reaction exponent $13.4331$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 13.4331)$.
3. Striking `{{key:eˣ}}` exponentiates in place, producing equilibrium constant $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{6.8220 \times 10^5})$—confirming the reaction runs to near completion with zero auxiliary memory.

---

### Problem 3.17: Sabine Reverberation Time in Auditorium
**Architectural Acoustics Context:** Hall volume $V = 4500\text{ m}^3$ with total acoustic absorption $A = 320.0\text{ m}^2\text{ Sabins}$:
$$T_{60} = \frac{0.161 \cdot V}{A}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_21:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_21:value}}`**$\text{ seconds}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `0.161 {{key:ENTER}} 4500 {{key:×}}` primes the architectural constant and scales by auditorium volume, producing volumetric absorption numerator $724.5000\text{ m}^3\cdot\text{s/m}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 724.5000)$.
2. Striking `320 {{key:÷}}` divides directly by room absorption area $A = 320\text{ Sabins}$, evaluating Sabine reverberation time $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{2.2641}\text{ s})$ without scratchpad memory.

---

### Problem 3.18: Beam Elastic Curve Cubic Deflection
**Structural Engineering Context:** Deflection at $x = 2.0\text{ m}$ on a simply supported beam ($L = 6.0\text{ m}$, uniform load $w = 8.5\text{ kN/m} = 8500\text{ N/m}$, $E I = 1.2 \times 10^7\text{ N}\cdot\text{m}^2$):
$$\delta(x) = \frac{w x}{24 E I} (L^3 - 2 L x^2 + x^3)$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_22:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_22:value}}`**$\text{ m}$.

> **Named RPN Stack Idiom: *The Polynomial Inside-Out Evaluation*** — Evaluate nested beam geometry $(L^3 - 2Lx^2 + x^3)$ inside-out and scale by uniform distributed load without parenthesis nesting {{cite:hp32sii1991}}.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `6 {{key:ENTER}} 3 {{key:yˣ}}` evaluates span cube $L^3 = 216.0000$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 216.0000)$.
2. Keying `2 {{key:ENTER}} 6 {{key:×}} 2 {{key:x²}} {{key:×}} {{key:-}}` evaluates quadratic term $2 L x^2 = 48.0000$ and subtracts from $L^3$, leaving $168.0000$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 168.0000)$.
3. Striking `2 {{key:ENTER}} 3 {{key:yˣ}} {{key:+}}` adds cubic term $x^3 = 8.0000$, resolving geometric bracket $(L^3 - 2 L x^2 + x^3) = 176.0000$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 176.0000)$.
4. Striking `8500 {{key:ENTER}} 2 {{key:×}} {{key:×}}` multiplies by distributed load $w = 8500\text{ N/m}$ and coordinate $x = 2.0\text{ m}$, forming $2.9920 \times 10^6\text{ N}\cdot\text{m}^2$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 2.9920 \times 10^6)$.
5. Striking `24 {{key:ENTER}} 1.2 {{key:E}} 7 {{key:×}} {{key:÷}}` builds flexural stiffness denominator $24 E I = 2.88 \times 10^8\text{ N}\cdot\text{m}^2$ and divides, yielding elastic deflection $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{0.0104}\text{ m} \approx 10.39\text{ mm})$.

---

### Problem 3.19: Gravitational Redshift Frequency Shift
**General Relativity Context:** Photon emitted from white dwarf surface ($M = 1.989 \times 10^{30}\text{ kg}$, radius $R = 6.4 \times 10^6\text{ m}$, $G = 6.6743 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2$, $c = 2.99792 \times 10^8\text{ m/s}$):
$$z = \frac{\Delta f}{f} \approx \frac{G M}{R c^2}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_23:keys}}`$\to \mathbf{{{res:sc32_03_algebra_transcendentals_seq_23:value}}} \approx 2.309 \times 10^{-4}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `6.6743 {{key:E}} 11 {{key:+/-}}` `{{key:ENTER}}` — Prime the stack with universal gravitational constant ($G = 6.6743 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2$) in $Y$.
2. `1.989 {{key:E}} 30` `{{key:×}}` — Key stellar mass ($M = 1.989 \times 10^{30}\text{ kg}$) and multiply; gravitational coupling numerator ($1.3275 \times 10^{20}\text{ m}^3/\text{s}^2$) forms in $X$.
3. `6.4 {{key:E}} 6` `{{key:ENTER}}` — Key white dwarf radius ($R = 6.4 \times 10^6\text{ m}$) into $Y$.
4. `2.99792 {{key:E}} 8` `{{key:x²}}` — Key speed of light and square in place ($c^2 = 8.98755 \times 10^{16}\text{ m}^2/\text{s}^2$); stack lift preserves $R$ in $Y$.
5. `{{key:×}}` — Multiply stellar radius by $c^2$; relativistic denominator ($5.7520 \times 10^{23}\text{ m}^3/\text{s}^2$) occupies $X$ while numerator waits in $Y$.
6. `{{key:÷}}` — Divide gravitational numerator by relativistic denominator; dimensionless gravitational redshift parameter ($z = 2.3079 \times 10^{-4}$) is determined directly.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `6.6743 {{key:E}} 11 {{key:+/-}} {{key:ENTER}} 1.989 {{key:E}} 30 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.3275 \times 10^{20}$ | Gravitational parameter $G M_{\odot}$ |
| 2 | `6.4 {{key:E}} 6 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0742 \times 10^{13}$ | Divide by white dwarf radius $R$ for gravitational potential $\Phi$ |
| 3 | `2.99792 {{key:E}} 8 {{key:x²}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$2.3079 \times 10^{-4}$** | Divide by speed of light squared $c^2$ for fractional redshift $z$ |

---

### Problem 3.20: Radiative Cooling Time of Molten Metal Droplet
**Thermal Radiation Context:** Droplet cooling from $T_1 = 1500\text{ K}$ to $T_2 = 1000\text{ K}$ into ambient vacuum ($T_{\text{env}} \approx 0\text{ K}$):
$$t = \frac{\rho \cdot c_p \cdot r}{3 \varepsilon \sigma} \left(\frac{1}{T_2^3} - \frac{1}{T_1^3}\right)$$
For iron droplet: $\rho = 7800\text{ kg/m}^3, c_p = 450\text{ J/kg}\cdot\text{K}, r = 0.0015\text{ m}, \varepsilon = 0.80, \sigma = 5.67037 \times 10^{-8}$.

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_24:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_24:value}}`**$\text{ seconds}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `1000 {{key:ENTER}} 3 {{key:yˣ}} {{key:1/x}} 1500 {{key:ENTER}} 3 {{key:yˣ}} {{key:1/x}} {{key:-}}` evaluates inverse cube temperature difference $(1/T_2^3 - 1/T_1^3) \approx 7.0370 \times 10^{-10}\text{ K}^{-3}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 7.0370 \times 10^{-10})$.
2. Keying `7800 {{key:ENTER}} 450 {{key:×}} 0.0015 {{key:×}} {{key:×}}` multiplies by thermal mass parameter $\rho c_p r = 5.265 \times 10^3$, giving numerator $3.7050 \times 10^{-6}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 3.7050 \times 10^{-6})$.
3. Striking `3 {{key:ENTER}} 0.80 {{key:×}} 5.67037 {{key:E}} 8 {{key:+/-}} {{key:×}} {{key:÷}}` builds radiation denominator $3 \varepsilon \sigma \approx 1.3609 \times 10^{-7}$ and divides, calculating droplet radiative cooling time $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{27.2249}\text{ s})$ with zero scratchpad memory.

---

### Problem 3.21: Compound Doubling Time: Rule of 72 vs. Exact Logarithm
**Financial Mathematics Context:** At annual interest rate $r = 7.2\%$:
* Rule of 72 approximation: $t_{\text{approx}} = 72 / 7.2 = \mathbf{10.0\text{ years}}$
* Exact exponential doubling: $t_{\text{exact}} = \frac{\ln 2}{\ln(1 + 0.072)}$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_25:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_25:value}}`**$\text{ years}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `2 {{key:LN}}` evaluates the natural logarithm of doubling $\ln 2 \approx 0.6931$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.6931)$.
2. Striking `1.072 {{key:LN}} {{key:÷}}` pushes $\ln 2$ to $Y$, evaluates annual continuous growth $\ln(1.072) \approx 0.0695$, and divides, obtaining exact doubling period $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{9.9696}\text{ years})$.

Error in the empirical rule is under $0.31\%$.

---

### Problem 3.22: Dynamic Range and Theoretical SNR of 24-Bit Digital Audio
**Acoustic Signal Processing Context:** Standard linear PCM quantizer with $N = 24\text{ bits}$:
$$\text{SNR}_{\text{dB}} = 6.0206 N + 1.7609\text{ dB}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_26:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_26:value}}`**$\text{ dB}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `6.0206 {{key:ENTER}} 24 {{key:×}}` evaluates raw dynamic range from bit depth $6.0206 \times 24 = 144.4944\text{ dB}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 144.4944)$.
2. Striking `1.7609 {{key:+}}` adds quantization noise floor correction constant, evaluating maximum theoretical SNR $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{146.2553}\text{ dB})$ in place.

---

### Problem 3.23: Fermi-Dirac Semiconductor Electron Distribution
**Solid State Physics Context:** State energy above Fermi level $\Delta E = E - E_F = 0.050\text{ eV}$ at room temperature $T = 300\text{ K}$ ($k T = 0.025852\text{ eV}$):
$$f(E) = \frac{1}{1 + \exp\left(\frac{E - E_F}{k T}\right)}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_27:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_27:value}}`** ($12.63\%$).

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `0.050 {{key:ENTER}} 0.025852 {{key:÷}}` computes normalized Fermi level offset $(E - E_F)/(kT) \approx 1.9341$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.9341)$.
2. Striking `{{key:eˣ}} 1 {{key:+}} {{key:1/x}}` evaluates exponential Boltzmann factor, adds Fermi exclusion unity ($7.9177$), and takes the reciprocal, determining electron occupation probability $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{0.1263} = 12.63\%)$ without parenthesis grouping.

---

### Problem 3.24: Viscous Pressure Drop in Poiseuille Laminar Capillary Flow
**Fluid Mechanics Context:** Fluid viscosity $\mu = 0.0025\text{ Pa}\cdot\text{s}$, tube length $L = 0.20\text{ m}$, radius $R = 0.0005\text{ m}$, flow rate $Q = 1.5 \times 10^{-8}\text{ m}^3/\text{s}$:
$$\Delta P = \frac{8 \mu L Q}{\pi R^4}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_28:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_28:value}}`**$\text{ Pa}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `8 {{key:ENTER}} 0.0025 {{key:×}} 0.20 {{key:×}} 1.5 {{key:E}} 8 {{key:+/-}} {{key:×}}` accumulates Hagen-Poiseuille numerator $8 \mu L Q = 6.0000 \times 10^{-11}\text{ N}\cdot\text{m}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 6.0000 \times 10^{-11})$.
2. Keying `{{key:π}} {{key:÷}} 0.0005 {{key:ENTER}} 4 {{key:yˣ}} {{key:÷}}` divides by geometric circle factor $\pi$ and capillary radius fourth power $R^4 = 6.25 \times 10^{-14}\text{ m}^4$, evaluating viscous laminar pressure drop $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{305.5775}\text{ Pa})$ with zero auxiliary registers.

---

### Problem 3.25: Weibull Distribution Probability Density for Wind Turbine Speed
**Reliability & Energy Context:** Wind speed $v = 8.5\text{ m/s}$ modeled by Weibull PDF with shape parameter $k = 2.2$ and scale parameter $c = 9.0\text{ m/s}$:
$$f(v) = \frac{k}{c} \left(\frac{v}{c}\right)^{k - 1} \exp\left[-\left(\frac{v}{c}\right)^k\right]$$

**Keystrokes:**
`{{res:sc32_03_algebra_transcendentals_seq_29:keys}}`

> **Named RPN Stack Idiom: *The Inside-Out Exponential & Dual-Power Pipeline*** — Compute normalized wind speed $v/c$, evaluate both the linear power $(v/c)^{k-1}$ and exponential power $(v/c)^k$ across stack levels without scratchpad memory {{cite:ellenberg2014,hp15c1982}}.

Result: $f(8.5) \approx \mathbf{0.098485\text{ (m/s)}^{-1}}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `8.5 {{key:ENTER}} 9.0 {{key:÷}}` — Compute normalized wind speed ratio $v/c = 8.5/9.0 \approx 0.944444$.
2. `{{key:ENTER}} {{key:ENTER}} 2.2 {{key:yˣ}} {{key:+/-}} {{key:eˣ}}` — Replicate ratio on stack, raise to shape parameter $k = 2.2$, and exponentiate for Weibull tail $\exp(-(v/c)^k) \approx 0.4144$.
3. `{{key:x⇄y}} 1.2 {{key:yˣ}} {{key:×}}` — Retrieve ratio from stack, raise to $(k - 1) = 1.2$, and multiply by exponential tail.
4. `2.2 {{key:ENTER}} 9.0 {{key:÷}} {{key:×}}` — Scale by shape-to-scale ratio $k/c \approx 0.2444$ to yield probability density $f(8.5) \approx \mathbf{0.098485\text{ (m/s)}^{-1}}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `8.5 {{key:ENTER}} 9.0 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.9444$ | Normalized wind speed ratio $v/c$ |
| 2 | `{{key:ENTER}} {{key:ENTER}} 2.2 {{key:yˣ}} {{key:+/-}} {{key:eˣ}}` | $0.0000$ | $0.0000$ | $0.9444$ | $0.4140$ | Weibull exponential factor $\exp(-(v/c)^k)$ |
| 3 | `{{key:x⇄y}} 1.2 {{key:yˣ}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.3866$ | Multiply by power-law velocity term $(v/c)^{k-1}$ |
| 4 | `2.2 {{key:ENTER}} 9.0 {{key:÷}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.0945$** | Scale by shape/scale ratio $k/c$ for probability density $f(v)$ |

---

### Problem 3.26: Decomposing GPS Coordinates via Number Parts (`IP`, `FP`)
**Geodesy Context:** Latitude GPS readout $= 30.267153^\circ\text{ N}$. Decompose into degrees, arcminutes, and arcseconds:

**Keystrokes:**
1. Store: `30.267153 {{key:STO}} 1`
2. Degrees: `{{key:PARTS}} {{key:IP}}` $\rightarrow$ **$30^\circ$**
3. Arcminutes: `{{key:RCL}} 1 {{key:PARTS}} {{key:FP}} 60 {{key:×}} {{key:ENTER}} {{key:PARTS}} {{key:IP}}` $\rightarrow$ **$16'$**
4. Arcseconds: `{{key:x⇄y}} {{key:PARTS}} {{key:FP}} 60 {{key:×}}` $\rightarrow$ **$1.75''$**

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `30.267153 {{key:ENTER}} {{key:PARTS}} {{key:IP}}` loads latitude and isolates integer degrees $(T: 0.0000, Z: 0.0000, Y: 30.2672, X: \mathbf{30.0000^\circ})$.
2. Keying `30.267153 {{key:PARTS}} {{key:FP}} 60 {{key:×}}` extracts fractional degrees and scales to arcminutes $16.0292'$, followed by `{{key:PARTS}} {{key:IP}}` to extract integer minutes $(T: 30.2672, Z: 30.2672, Y: 30.0000, X: \mathbf{16.0000'})$.
3. Striking `16.02918 {{key:PARTS}} {{key:FP}} 60 {{key:×}}` extracts fractional arcminutes and multiplies by 60 to yield arcseconds $(T: 30.0000, Z: 30.0000, Y: 16.0000, X: \mathbf{1.7508''})$, resolving $30^\circ 16' 1.75''\text{ N}$.

---

### Problem 3.27: Combinatorial Permutations of 16-Port Network Switch
**Computer Science Context:** Number of unique routing permutations across 16 ports ($16!$):

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_30:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_30:value}}`** $\times 10^{13}$ ($20.92\text{ trillion paths}$).

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `16 {{key:x!}}` evaluates factorial $16!$ in place in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{2.0923 \times 10^{13}})$, computing all $20.92$ trillion port routing combinations instantly without stack displacement.

---

### Problem 3.28: 5-Dimensional Sphere Volume via Half-Integer Gamma
**Higher Geometry Context:** Volume of a 5D unit hypersphere:
$$V_5 = \frac{\pi^{5/2}}{\Gamma\left(\frac{5}{2} + 1\right)} = \frac{\pi^{2.5}}{(2.5)!}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_31:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_31:value}}`**.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `{{key:π}} {{key:ENTER}} 2.5 {{key:yˣ}}` evaluates volumetric numerator $\pi^{2.5} \approx 17.4934$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 17.4934)$.
2. Striking `2.5 {{key:x!}} {{key:÷}}` enters half-integer argument $2.5$, evaluates gamma factor $\Gamma(3.5) = 2.5! \approx 3.3234$ via Lanczos expansion, and divides, obtaining 5-sphere volume $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{5.2638})$ directly.

---

### Problem 3.29: Parallel Conductance and Characteristic Admittance
**RF Transmission Line Context:** Shunt conductance $G = 0.020\text{ S}$ in parallel with susceptance $B = 0.015\text{ S}$. Find equivalent magnitude:
$$|Y| = \sqrt{G^2 + B^2}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_32:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_32:value}}`**$\text{ S} = 25.0\text{ mS}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `0.020 {{key:x²}} 0.015 {{key:x²}} {{key:+}}` computes $G^2 = 4.0000 \times 10^{-4}$ and sums orthogonal susceptance $B^2 = 2.2500 \times 10^{-4}$, giving sum of squares $6.2500 \times 10^{-4}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 6.2500 \times 10^{-4})$.
2. Striking `{{key:√x}}` extracts square root in place, evaluating total admittance magnitude $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{0.0250}\text{ S} = 25.0\text{ mS})$.

---

### Problem 3.30: High-Speed Sprint: Continued Power Pyramid
**Rapid Calculation Sprint:** Rapid evaluation of the power tower:
$$x = \left(2.4^{1.8}\right)^{\sqrt{3.5}}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_33:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_33:value}}`**

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `2.4 {{key:ENTER}} 1.8 {{key:yˣ}}` evaluates base power $2.4^{1.8} \approx 4.8348$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 4.8348)$.
2. Striking `3.5 {{key:√x}} {{key:yˣ}}` pushes base to $Y$, takes root $\sqrt{3.5} \approx 1.8708$, and raises base to radical exponent, evaluating the power pyramid $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{19.0703})$ in four seconds.

---

### Problem 3.31: Polytropic Gas Compression Work
**Thermodynamic Process Context:** Gas with polytropic index $n = 1.32$ compresses from $V_1 = 0.040\text{ m}^3$ at $P_1 = 120\text{ kPa}$ to $V_2 = 0.010\text{ m}^3$:
$$W = \frac{P_1 V_1}{n - 1} \left[ \left(\frac{V_1}{V_2}\right)^{n - 1} - 1 \right]$$
Here $n - 1 = 0.32$, $V_1 / V_2 = 4.0$.

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_34:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_34:value}}`**$\text{ J}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `4.0 {{key:ENTER}} 0.32 {{key:yˣ}} 1 {{key:-}}` evaluates compression expansion factor $(4.0^{0.32} - 1) \approx 0.5583$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.5583)$.
2. Keying `120000 {{key:ENTER}} 0.040 {{key:×}} 0.32 {{key:÷}} {{key:×}}` evaluates state energy factor $P_1 V_1 / (n - 1) = 15,000\text{ J}$ and multiplies by expansion factor, resolving polytropic compression work $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{8374.9374}\text{ J} \approx 8.375\text{ kJ})$.

---

### Problem 3.32: Acoustic Sound Intensity Level in Air
**Acoustics Context:** Sound wave carrying acoustic intensity $I = 0.0035\text{ W/m}^2$ relative to reference threshold $I_0 = 1.0 \times 10^{-12}\text{ W/m}^2$:
$$L_I = 10 \log_{10}\left(\frac{I}{I_0}\right)$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_35:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_35:value}}`**$\text{ dB SIL}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `0.0035 {{key:ENTER}} 1 {{key:E}} 12 {{key:+/-}} {{key:÷}}` computes sound intensity ratio $I/I_0 = 3.5000 \times 10^9$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 3.5000 \times 10^9)$.
2. Striking `{{key:LOG}} 10 {{key:×}}` evaluates common logarithm $\log_{10}(3.5 \times 10^9) \approx 9.5441$ and scales by 10, determining decibel sound level $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{95.4407}\text{ dB SIL})$ directly.

---

### Problem 3.33: Bragg's X-Ray Crystal Diffraction Wavelength
**Crystallography Context:** First-order diffraction ($n = 1$) from crystal lattice planes with spacing $d = 0.282\text{ nm} = 2.82 \times 10^{-10}\text{ m}$ at grazing angle $\theta = 15.8^\circ$:
$$\lambda = 2 d \sin\theta$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_36:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_36:value}}`** $\times 10^{-10}\text{ m} = 0.1536\text{ nm}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `2 {{key:ENTER}} 2.82 {{key:E}} 10 {{key:+/-}} {{key:×}}` evaluates grating distance factor $2 d = 5.6400 \times 10^{-10}\text{ m}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 5.6400 \times 10^{-10})$.
2. Striking `15.8 {{key:SIN}} {{key:×}}` pushes $2d$ to $Y$, computes $\sin(15.8^\circ) \approx 0.2723$, and multiplies, yielding X-ray diffraction wavelength $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{1.5357 \times 10^{-10}}\text{ m} = 0.1536\text{ nm})$.

---

### Problem 3.34: Radiogenic Daughter Isotope Accumulation Kinetics
**Nuclear Geochemistry Context:** Growth of stable radiogenic daughter atoms $D(t)$ from parent $P_0 = 1.0 \times 10^{15}\text{ atoms}$ with decay constant $\lambda = 1.42 \times 10^{-11}\text{ yr}^{-1}$ over elapsed time $t = 2.5 \times 10^9\text{ years}$:
$$D(t) = P_0 \left(1 - e^{-\lambda t}\right)$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_37:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_37:value}}`** $\times 10^{13}\text{ daughter atoms}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `1.42 {{key:E}} 11 {{key:+/-}} {{key:ENTER}} 2.5 {{key:E}} 9 {{key:×}}` computes dimensionless decay exponent $\lambda t = 0.0355$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.0355)$.
2. Striking `{{key:+/-}} {{key:eˣ}} 1 {{key:-}} {{key:+/-}}` evaluates parent survival fraction $e^{-\lambda t} \approx 0.9651$ and inverts across unity to give daughter fraction $0.0349$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.0349)$.
3. Striking `1 {{key:E}} 15 {{key:×}}` scales by initial parent inventory $P_0 = 10^{15}$, yielding daughter accumulation $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{3.4877 \times 10^{13}}\text{ atoms})$ without memory registers.

---

### Problem 3.35: High-Speed Sprint: Radical Exponential Continued Fraction
**Rapid Calculation Sprint:** Solve the complex transcendental expression:
$$x = \sqrt{e^{1.4} + \ln\left(15 + \sqrt{220}\right)}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_38:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_38:value}}`**

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `220 {{key:√x}} 15 {{key:+}} {{key:LN}}` evaluates root $\sqrt{220} \approx 14.8324$, adds 15 ($29.8324$), and takes natural log, producing $3.3956$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 3.3956)$.
2. Striking `1.4 {{key:eˣ}} {{key:+}} {{key:√x}}` evaluates exponential $e^{1.4} \approx 4.0552$, sums inner terms ($7.4508$), and extracts square root, calculating result $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{2.7296})$ in five seconds.

---

### Problem 3.36: Thermal Noise Power Density (Johnson-Nyquist Noise)
**RF Telecommunications Context:** Available noise power per hertz in an antenna at $T = 290.0\text{ K}$ ($k_B = 1.380649 \times 10^{-23}\text{ J/K}$):
$$P_n / B = k_B T \quad [\text{W/Hz}]$$
Express in $\text{dBm/Hz}$ ($P_{\text{dBm}} = 10 \log_{10}(P / 10^{-3})$):

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_39:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_39:value}}`**$\text{ dBm/Hz}$.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `1.380649 {{key:E}} 23 {{key:+/-}} {{key:ENTER}} 290 {{key:×}} 0.001 {{key:÷}}` evaluates thermal noise power $k_B T \approx 4.0039 \times 10^{-21}\text{ W/Hz}$ and normalizes to $1\text{ mW}$ reference, leaving $4.0039 \times 10^{-18}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 4.0039 \times 10^{-18})$.
2. Striking `{{key:LOG}} 10 {{key:×}}` takes decadic log $\log_{10}(4.0039 \times 10^{-18}) \approx -17.3975$ and multiplies by 10, resolving noise spectral density floor $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{-173.9752}\text{ dBm/Hz})$ directly.

---

### Problem 3.37: Van der Waals Gas Pressure Equation
**Physical Chemistry Context:** Moles $n = 2.0$, volume $V = 0.0050\text{ m}^3$, temperature $T = 320.0\text{ K}$, van der Waals constants for $\text{CO}_2$: $a = 0.364\text{ Pa}\cdot\text{m}^6/\text{mol}^2$, $b = 4.27 \times 10^{-5}\text{ m}^3/\text{mol}$, $R = 8.31446\text{ J/mol}\cdot\text{K}$:
$$P = \frac{n R T}{V - n b} - \frac{a n^2}{V^2}$$

**Keystrokes:**
`{{res:sc32_03_algebra_transcendentals_seq_40:keys}}`

> **Named RPN Stack Idiom: *The LASTX Dual-Branch Trick & Equation of State Pipeline*** — Compute the kinetic repulsive pressure term $nRT/(V - nb)$, compute the intermolecular attractive term $an^2/V^2$ across stack levels, and subtract directly with zero register allocation {{cite:hp15c1982}}.

Result: $P \approx \mathbf{1,027,346\text{ Pa}} \approx 1.027\text{ MPa}$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `2 {{key:ENTER}} 8.31446 {{key:×}} 320 {{key:×}}` — Evaluate kinetic energy numerator $nRT = (2)(8.31446)(320) = 5321.25\text{ J}$.
2. `0.0050 {{key:ENTER}} 2 {{key:ENTER}} 4.27 {{key:E}} 5 {{key:+/-}} {{key:×}} {{key:-}} {{key:÷}}` — Compute effective free volume $(V - nb) = 0.0049146\text{ m}^3$ and divide, yielding repulsive kinetic pressure $1,082,744\text{ Pa}$.
3. `0.364 {{key:ENTER}} 4 {{key:×}} 0.0050 {{key:x²}} {{key:÷}} {{key:-}}` — Compute attractive intermolecular term $an^2/V^2 = 58,240\text{ Pa}$ and subtract to evaluate van der Waals pressure $P \approx \mathbf{1,027,346\text{ Pa}} \approx 1.027\text{ MPa}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `2 {{key:ENTER}} 8.31446 {{key:×}} 320 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $5321.2544$ | Ideal kinetic energy numerator $n R T$ |
| 2 | `0.0050 {{key:ENTER}} 2 {{key:ENTER}} 4.27 {{key:E}} 5 {{key:+/-}} {{key:×}} {{key:-}} {{key:÷}}` | $5321.2544$ | $5321.2544$ | $5321.2544$ | $1082744.1501$ | Divide by free volume $(V - n b)$ for kinetic pressure term |
| 3 | `0.364 {{key:ENTER}} 4 {{key:×}} 0.0050 {{key:x²}} {{key:÷}} {{key:-}}` | $5321.2544$ | $5321.2544$ | $5321.2544$ | **$1024504.1501$** | Subtract molecular attraction term $a n^2 / V^2$ for van der Waals pressure $P$ (Pa) |

---

### Problem 3.38: Skin Depth in Good Conductor at RF Frequencies
**Electromagnetics Context:** Copper conductivity $\sigma = 5.8 \times 10^7\text{ S/m}$, permeability $\mu = 4\pi \times 10^{-7}\text{ H/m}$ at carrier frequency $f = 100.0\text{ MHz} = 1.0 \times 10^8\text{ Hz}$:
$$\delta = \frac{1}{\sqrt{\pi f \mu \sigma}}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_41:keys}}`$\to \mathbf{{{res:sc32_03_algebra_transcendentals_seq_41:value}}\,\mu\text{m}}$.

> **Named RPN Stack Idiom: *The Inside-Out Radical & Electromagnetic Penetration Pipeline*** — Stream frequency, permeability, and conductivity into the radicand product $\pi f \mu \sigma$, extract the square root in place, and invert with `{{key:1/x}}` without parenthesis buffering {{cite:horowitz2015,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `{{key:π}}` — Load circle constant $\pi$ into $X$.
2. `1 {{key:E}} 8` `{{key:×}}` — Enter RF carrier frequency ($f = 100.0\text{ MHz} = 1.0 \times 10^8\text{ Hz}$) and multiply; frequency factor ($3.1416 \times 10^8\text{ s}^{-1}$) forms in $X$.
3. `4` `{{key:ENTER}}` `{{key:π}}` `{{key:×}}` `1 {{key:E}} 7 {{key:+/-}}` `{{key:×}}` — Evaluate magnetic permeability of free space ($\mu = 4\pi \times 10^{-7}\text{ H/m} \approx 1.2566 \times 10^{-6}\text{ H/m}$) in place.
4. `{{key:×}}` — Multiply frequency factor by permeability; electromagnetic induction product occupies $X$.
5. `5.8 {{key:E}} 7` `{{key:×}}` — Scale by copper bulk electrical conductivity ($\sigma = 5.8 \times 10^7\text{ S/m}$); total skin-depth radicand product ($2.2902 \times 10^{10}\text{ m}^{-2}$) appears in $X$.
6. `{{key:√x}}` — Extract square root in place; inverse penetration depth ($1.5133 \times 10^5\text{ m}^{-1}$) condenses in $X$.
7. `{{key:1/x}}` — Take reciprocal in place; high-frequency RF skin depth ($\delta = 6.6079 \times 10^{-6}\text{ m} = 6.61\,\mu\text{m}$) evaluates without grouping syntax.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | `{{key:π}} {{key:ENTER}} 1 {{key:E}} 8 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.1416 \times 10^{8}$ | Angular frequency $\pi f$ at $100\text{ MHz}$ |
| 2 | `4 {{key:ENTER}} {{key:π}} {{key:×}} 1 {{key:E}} 7 {{key:+/-}} {{key:×}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $394.7842$ | Multiply by magnetic permeability $\mu_0 = 4\pi \times 10^{-7}$ |
| 3 | `5.8 {{key:E}} 7 {{key:×}} {{key:√x}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $6.6085 \times 10^{-6}$ | Multiply by copper conductivity $\sigma$ and take reciprocal root $\delta$ (m) |
| 4 | `1 {{key:E}} 6 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$6.6085$** | Convert skin depth $\delta$ to micrometers ($\mu\text{m}$) |

---

### Problem 3.39: Relativistic Lorentz Factor & Time Dilation
**Special Relativity Context:** Particle speed $v = 0.85 c$ ($v/c = 0.85$):
$$\gamma = \frac{1}{\sqrt{1 - (v/c)^2}}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_42:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_42:value}}`**.

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `0.85 {{key:x²}} 1 {{key:-}} {{key:+/-}}` squares velocity ratio ($0.7225$), subtracts from 1.0, and negates, forming relativistic radical core $1 - \beta^2 = 0.2775$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.2775)$.
2. Striking `{{key:√x}} {{key:1/x}}` extracts root $\sqrt{0.2775} \approx 0.5268$ and takes reciprocal, calculating Lorentz factor $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{1.8983})$—showing time dilates by $1.90\times$ without parenthesis buffering.

---

### Problem 3.40: High-Speed Sprint: Chained Logarithmic Power Tower
**Rapid Calculation Sprint:** Solve the expression:
$$x = \frac{\ln(4.5^3) + \log_{10}(1200)}{\sqrt[3]{18.5}}$$

**Keystrokes:** `{{res:sc32_03_algebra_transcendentals_seq_43:keys}}` $\rightarrow$ **`{{res:sc32_03_algebra_transcendentals_seq_43:value}}`**

**Step-by-Step RPN Reasoning & Stack Dynamics:**
1. Keying `4.5 {{key:LN}} 3 {{key:×}} 1200 {{key:LOG}} {{key:+}}` computes $3 \ln(4.5) \approx 4.5122$ and adds common logarithm $\log_{10}(1200) \approx 3.0792$, forming numerator $7.5914$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 7.5914)$.
2. Striking `18.5 {{key:ENTER}} 3 {{key:ˣ√y}} {{key:÷}}` lifts numerator to $Y$, evaluates cube root $\sqrt[3]{18.5} \approx 2.6447$, and divides, obtaining quotient $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{2.8703})$ in six seconds flat.

---

## Computational Accuracy & Transcendental Architecture Notes

### In-Place Monadic Evaluation & Stack Preservation
On the SC-32, transcendental functions (`{{key:LN}}`, `{{key:LOG}}`, `{{key:eˣ}}`, `{{key:10ˣ}}`, `{{key:√x}}`, `{{key:1/x}}`, and `{{key:x!}}`) operate monadically directly on Register $X$. These operations do not lift or drop the operational stack: Registers $Y, Z,$ and $T$ retain their values unmodified, allowing intermediate parameters to wait undisturbed in upper registers while functions execute.

Furthermore, every monadic evaluation automatically copies the prior argument into `{{key:LASTX}}`. If an incorrect function is applied or if the argument is needed for a subsequent term (such as evaluating $\frac{e^x - 1}{x}$ or verifying inverse pairs), pressing `{{key:LASTX}}` restores the original value without requiring memory registers or recalculation.

### Range Reduction & 64-Bit Chebyshev Approximations
Transcendental calculations near domain boundaries frequently expose numerical instability in lower-precision calculators. To maintain IEEE 754 double-precision accuracy (53 mantissa bits, guaranteeing 15–17 decimal digits of precision), the SC-32 employs Cody-Waite range reduction combined with high-order Chebyshev and rational Lanczos polynomial approximations. 

Whether calculating the natural logarithm of arguments close to unity ($\ln(1 + \epsilon)$), computing the factorial of large integers, or evaluating the Gamma function for half-integers ($\Gamma(3.5) = 2.5! = \frac{15}{8}\sqrt{\pi}$), relative truncation errors remain strictly bounded below $10^{-15}$. Pressing `{{key:SHOW}}` displays the complete internal mantissa, providing full transparency into intermediate numeric states.

### Domain Boundaries and Stack Integrity
When a calculation encounters a mathematical singularity—such as $\ln(0)$, $\log_{10}(-5)$, or division by zero—the SC-32 halts evaluation and raises a diagnostic code (`Error 01: INVALID DATA`) without corrupting or resetting the operational stack. Pressing `{{key:C}}` clears the error status and restores display visibility to Register $X$, preserving upper stack contents ($Y, Z, T$) intact so the practitioner can inspect and correct the offending value.

### Engineering & Scientific Notation Formatting
Display modes (`{{key:FIX}}`, `{{key:SCI}}`, `{{key:ENG}}`, and `{{key:ALL}}`) govern how numbers are rendered without altering internal 64-bit precision. In physical sciences and electrical engineering, `{{key:ENG}}` mode constrains exponent values to multiples of three ($10^3, 10^6, 10^{-3}, 10^{-6}, 10^{-9}$), directly matching standard SI metric prefixes (kilo, mega, micro, nano, pico) and eliminating manual exponent translation errors during field work.

---

## Summary & Looking Ahead

Chapter 3 expanded the operational stack into the continuous domain of algebra and transcendentals. You explored in-place monadic transformations, arbitrary powers and fractional roots, natural and common logarithms across wide dynamic ranges, and factorials extending smoothly into the half-integer Gamma domain. With IEEE-754 64-bit precision, in-place evaluation preserves upper stack registers ($Y, Z, T$) untouched, while `{{key:SHOW}}` and display formats (`{{key:FIX}}`, `{{key:SCI}}`, `{{key:ENG}}`, `{{key:ALL}}`) adapt readouts directly to engineering disciplines.

Linear and exponential scales are only part of the physical world; nature also rotates, oscillates, and points through multi-dimensional space. In **Chapter 4: Trigonometry, Vectors & Polar Transformations**, you will step onto the unit circle, navigating degree, radian, and gradian angular modes. You will harness direct and inverse trigonometric functions, hyperbolic projections, and instantaneous rectangular-to-polar conversions to decompose forces, track geodetic traverses, and navigate 2D vector spaces on the stack.