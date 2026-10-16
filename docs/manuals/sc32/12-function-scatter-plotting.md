---
title: "Chapter 12: Function & Scatter Plotting Engine | SC-32 Manual"
description: "Master the 64-point vector graphics engine, interactive crosshair curve tracing, window scaling, and regression scatter overlays on the StackCalc SC-32."
---

# Chapter 12: Function & Scatter Plotting Engine

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 GRAPHICS // VECTOR CURVE &amp; SCATTER PLOTTING ENGINE</span>
  <span class="te-viewport-status text-sky-400">● 64-POINT VECTOR RENDERER &bull; INTERACTIVE CROSSHAIR TRACER &bull; STAT OVERLAYS</span>
</div>

## Seeing the Invisible: Why One 64-Point Curve Reveals What a Thousand Numbers Hide

In the bitter winter of 1637, René Descartes sat inside a stove-heated room in the Netherlands, contemplating a profound schism that had divided natural philosophers since antiquity. Geometry belonged to space—to lines, triangles, and physical bodies drawn with straightedge and compass. Algebra, by contrast, belonged to symbolic computation—to silent numbers, polynomial balances, and abstract equations. Descartes' radical insight in *La Géométrie* was that these two worlds were identical: every algebraic relation $y = f(x)$ describes a living geometric curve in space, and every curve is an infinite continuum of algebraic points.

Centuries later, an engineer wrestling with complex systems—an oscillating LC circuit, an aerodynamic shockwave boundary, or the decay envelope of an underdamped suspension—faces the inverse dilemma. A stack of discrete numbers on a handheld calculator, no matter how precise, cannot immediately reveal a high-frequency resonance peak, a hidden vertical asymptote, or a saddle point. To see the dynamics of a physical system, one must see its shape.

The StackCalc SC-32 bridges this gap through its dedicated 64-point vector graphics engine (`{{key:PLOT}}`). By transforming the transflective dot-matrix LCD into a miniature Cartesian laboratory, the instrument evaluates 64 discrete mathematical slices across any domain and renders an interpolated continuous curve in under 42 milliseconds. Paired with interactive crosshair reticle tracing, the engineer can walk along the mathematical terrain, reading exact coordinate pairs from the real-time status bar and committing discovered extrema or inflection points directly back into the RPN operational stack with a single keystroke.

{{screenshot:sc32_plot_polynomial|SC-32 64-Point Vector Function Plotter ({{key:PLOT}}): Cubic Polynomial x³ − 6x² + 11x − 6 with Interactive Crosshair}}
*Figure 12.1: The StackCalc SC-32 rendering an interactive 64-point vector curve (`X^3 - 6*X^2 + 11*X - 6`) with real-time coordinate crosshair telemetry in the Paper print theme.*

<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>{{key:ALL}}</code> (Full 12-digit scientific mantissa; Standard Base-10 Arithmetic; Degrees angular mode default for surveying/trig; Radians angular mode <code>{{key:RAD}}</code> for periodic signal waveforms). Continuous non-volatile graphics memory preserves window configurations across power cycles.
</div>

---

## The Transflective 64-Point Vector Rendering Engine

While the StackCalc SC-32 is engineered primarily as a rapid tactile numerical instrument, its $132 \times 65$ transflective monochrome dot-matrix display features a dedicated **64-Point Vector Graphics Engine (`{{key:PLOT}}`)**, accessed via Right Shift `{{key:↱}}` on the multi-action `{{key:x∥y}}` key (Row 7, Column 3), as specified in the *HP32SII Deviation Rubric*.

### Viewport Geometry & Pixel Mapping
The physical display is partitioned into two specialized zones:
* **Graphing Viewport ($128 \times 52\text{ pixels}$):** World coordinates $(x, y)$ are projected onto screen pixel coordinates $(u, v)$ via linear transformation:
  $$u = \left\lfloor \frac{x - X_{\min}}{X_{\max} - X_{\min}} \times 127 \right\rfloor$$
  $$v = 51 - \left\lfloor \frac{y - Y_{\min}}{Y_{\max} - Y_{\min}} \times 51 \right\rfloor$$
  where $u \in [0, 127]$ maps horizontally from left to right, and $v \in [0, 51]$ maps vertically from top to bottom.
* **Status Readout Line ($132 \times 13\text{ pixels}$):** The lower 13 vertical pixels ($v \in [52, 64]$) are reserved for coordinate text readouts, equation labels, active mode indicators, and crosshair reticle telemetry rendered in high-contrast monospaced font.

### Vector Line Rasterization & Bresenham Algorithm
Connecting 64 discrete sample points into a continuous graphic curve requires integer line interpolation. The SC-32 graphics pipeline executes a hardware-accelerated **Bresenham Vector Line Algorithm** directly into the 1,072-byte display frame buffer.
Given two adjacent plotted coordinates $(u_0, v_0)$ and $(u_1, v_1)$:
$$\Delta u = |u_1 - u_0|, \quad \Delta v = |v_1 - v_0|$$
The error term $\epsilon = 2\Delta v - \Delta u$ steps across pixel increments without floating-point division, drawing smooth 1-pixel wide line segments that preserve high-frequency crests and steep asymptotes.

### Automatic Domain Scaling
When a mathematical function is plotted:
1. The engine evaluates the target equation at **64 discrete sample points** evenly spaced across the domain $[X_{\min}, X_{\max}]$:
   $$x_k = X_{\min} + k \left( \frac{X_{\max} - X_{\min}}{63} \right), \quad k = 0, 1, \dots, 63$$
2. The internal min/max search algorithm determines $Y_{\min} = \min(f(x_k))$ and $Y_{\max} = \max(f(x_k))$.
3. If $Y_{\max} - Y_{\min} < 10^{-12}$ (a flat constant line), the range automatically pads to $[y - 1, y + 1]$.
4. If the coordinate origin $(0, 0)$ falls within the window, coordinate axes and zero-tick marks are automatically rendered as subtle dotted lines.
5. Total plot generation and rasterization completes in under **$42\text{ milliseconds}$** on the 150 MHz dual-core processor.

### Precision Graphic Plot Visualizations & Coordinate Mapping

The following live screenshots captured directly from the SC-32 rendering engine illustrate the $128 \times 52$ dot-matrix viewport across three foundational mathematical workflows:

#### 1. Polynomial Root & Extrema Inspection (`X^3 - 6*X^2 + 11*X - 6`)
Plotting a cubic polynomial over $X \in [0, 4]$ reveals all three real zero crossings ($x = 1, 2, 3$) and both local extrema at a glance before invoking `{{key:SOLVE}}` or `{{key:POLY}}`:

{{res:sc32_plot_polynomial:screenshot|SC-32 Vector Plotter: Cubic Polynomial Zero Crossings at x = 1, 2, 3}}

#### 2. Shaded Definite Integral Area Under Curve (`3*X^2` on $[0, 4]$)
When plotting an integrand after or during Adaptive Romberg Quadrature (`{{key:∫}}`), the graphing viewport shades the vertical Riemann columns between the curve $y = f(x)$ and the horizontal axis $y = 0$, visually confirming net positive vs. negative area accumulation:

{{res:sc32_plot_romberg_shaded:screenshot|SC-32 Vector Plotter: Shaded Definite Integral of 3x² from 0 to 4 (Area = 64.0)}}

#### 3. Gaussian Normal Probability Density Curve ($Z \in [-3.5, +3.5]$)
Plotting the Standard Normal PDF $f(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$ across $[-3.5\sigma, +3.5\sigma]$ displays the classic symmetric bell curve peaking at $f(0) = 0.3989422804$ with inflection points at $z = \pm 1.0\sigma$:

{{res:sc32_plot_normal_bell:screenshot|SC-32 Vector Plotter: Standard Normal Bell Curve over [-3.5, +3.5]}}

---

## Navigation, Pan & Zoom Control Scheme

In Plot Mode, the physical keypad dynamically reconfigures into an intuitive navigation controller (as specified in the *HP32SII Deviation Rubric*):

| Key | Action | Operational Behavior |
|:---|:---|:---|
| `{{key:PLOT}}` | Enter Plot Mode | Renders active function / data |
| Numpad `{{key:8}}` | Pan Up | Shifts Y-window upward by 25% |
| Numpad `{{key:2}}` | Pan Down | Shifts Y-window downward by 25% |
| Numpad `{{key:4}}` | Pan Left | Shifts X-window left by 25% |
| Numpad `{{key:6}}` | Pan Right | Shifts X-window right by 25% |
| `{{key:+}}` | Zoom In | Contracts window bounds by 50% |
| `{{key:-}}` | Zoom Out | Expands window bounds by 200% |
| `{{keycap:↓}}` (Key 7) | Trace Previous | Moves crosshair left along curve |
| `{{keycap:↑}}` (Key 8) | Trace Next | Moves crosshair right on curve |
| `{{key:ENTER}}` | Commit Coordinates | Copies current (X, Y) to stack |
| `{{key:<-}}` or `{{key:C}}` | Exit Plot | Restores normal RPN stack view |

### The Concrete-Representational-Abstract (CRA) Graphing Continuum
1. **Concrete (The Visual Curve):** The physical LCD displays the continuous curve trajectory, revealing zeros, asymptotic singularities, local maxima, and harmonic overshoots at a glance.
2. **Representational (The Traced Point Reticle):** Tracing the curve with `{{keycap:↓}}` and `{{keycap:↑}}` moves a crosshair cursor along the discrete 64 evaluation points, linking the visual curve to discrete numerical coordinates displayed in the status bar.
3. **Abstract (The Stack Commitment):** Pressing `{{key:ENTER}}` copies the traced coordinates into the operational stack ($Y = x, X = y$), allowing immediate numerical root-finding, integration, or differentiation.

{{blocks:counting_tiles_array_3x8|Discrete Grid Sampling and Pixel Quantization Array}}
*Figure 12.2: Concrete discrete grid sampling array: mapping mathematical domain intervals to quantized display columns before hardware-accelerated Bresenham line interpolation.*


---

## Window Bounds & Viewport Configuration

The graphing window is configured using standard storage registers or the dedicated `{{key:MODES}}` menu:

| Parameter | Register | Default Value | Description |
|:---|:---|:---|:---|
| Xmin | `XMIN` | -10.000000000 | Leftmost domain boundary |
| Xmax | `XMAX` | +10.000000000 | Rightmost domain boundary |
| Ymin | `YMIN` | (Auto-scaled) | Lower range boundary |
| Ymax | `YMAX` | (Auto-scaled) | Upper range boundary |
| Xscl | `XSCL` | 1.00000000000 | Tick mark spacing along X-axis |
| Yscl | `YSCL` | 1.00000000000 | Tick mark spacing along Y-axis |

To set custom window bounds from the stack:
* `10 {{key:+/-}} {{key:STO}} "XMIN"` (Sets $X_{\min} = -10$)
* `10 {{key:STO}} "XMAX"` (Sets $X_{\max} = +10$)
* Press `{{key:PLOT}}` to re-render.

---

## Engineering Design Briefing: Real-Time Telemetry Curve Tracing (Problems 12.1 through 12.38)


<div class="admonition warning">
<p class="admonition-title">The Algebraic Parenthesis Trap vs. The RPN Stack Shortcut: Multi-Point Vector Graphing &amp; Parameter Sweeping</p>
<p><strong>The Algebraic Parenthesis Trap:</strong> On an algebraic graphing calculator, defining an integrand, Fourier harmonic series, or frequency response curve requires entering lengthy strings of nested infix parentheses into a cramped formula editor {{cite:strogatz2019,dijkstra1961}}:</p>
<pre><code>Y1 = ( 1 / ( 1 + ( 2 * 3.14159 * X * 0.001 * 0.0000001 ) ^ 2 ) ^ 0.5 )</code></pre>
<p>Every evaluation point across the domain re-parses this tokenized string, allocating operator stacks and incurring memory churn. If an engineer forgets a single closing parenthesis or mistypes an exponent grouping, the plotting engine halts with an ambiguous <code>SYNTAX ERROR</code> mid-render, leaving a blank viewport and zero diagnostic insight {{cite:parker2019,ellenberg2014}}.</p>
<p><strong>The RPN Stack Shortcut:</strong> On the StackCalc SC-32, function definitions are written in pure postfix Reverse Polish Notation or evaluated as live stack transforms {{cite:hp15c1982,hp32sii1991}}. The 64-point vector engine evaluates expressions from the inside out with zero parenthesis overhead. Because each evaluation directly exercises the four hardware stack registers ($X, Y, Z, T$) with deterministic single-cycle execution, total 64-point sampling and Bresenham rasterization completes in under 42 milliseconds. Tapping <code>{{key:ENTER}}</code> while tracing commits the exact physical coordinates $(x, y)$ back into Registers $Y$ and $X$, allowing immediate chaining into Brent's root solver (<code>{{key:SOLVE}}</code>) or Adaptive Romberg Quadrature (<code>{{key:∫}}</code>) with zero re-entry {{cite:brent1973,romberg1955}}.</p>
</div>


The following 38 reference problems provide complete, publication-grade coverage across polynomial curves, electrical signals, mechanical vibrations, optics, thermodynamics, and bivariate statistical distributions.

---

### Problem 12.1: Square Wave Synthesis via Fourier Harmonics

Synthesize and plot a periodic square wave using the first three odd Fourier harmonics across $t \in [-180.0^\circ, +180.0^\circ]$ in Degrees mode:
$$y(t) = \sin(t) + \frac{1}{3}\sin(3t) + \frac{1}{5}\sin(5t)$$

#### 1. Store Equation in `{{key:EQN}}`
Enter postfix expression under label `FOURIER`:
`T {{key:SIN}} T 3 {{key:×}} {{key:SIN}} 3 {{key:÷}} {{key:+}} T 5 {{key:×}} {{key:SIN}} 5 {{key:÷}} {{key:+}}`

#### 2. Set Domain Bounds & Plot
* `180 {{key:+/-}} {{key:STO}} "XMIN"`
* `180 {{key:STO}} "XMAX"`
* Press `{{key:PLOT}}`

#### 3. Visual Waveform Output:
| Plot Telemetry | Crosshair Readout | Curve Feature |
| :--- | :--- | :--- |
| **Active Function** | `SIN(X) + SIN(3*X)/3` | Fundamental + 3rd harmonic square-wave synthesis |
| **Crosshair Cursor** | `X = 90.000000000`, `Y = 0.8666666667` | Central saddle trough between twin local maxima |

#### 4. Trace Analysis:
Using `{{keycap:↓}}` and `{{keycap:↑}}`, trace to $t = 90.0^\circ$:
$$y(90^\circ) = \sin(90^\circ) + \frac{1}{3}\sin(270^\circ) + \frac{1}{5}\sin(450^\circ) = 1.0 - 0.333333 + 0.200000 = \mathbf{0.866667}$$
The display confirms: `X: 90.000000000    Y: 0.8666666667`.
- **Harmonic Sum Stack Check ($t = 90^\circ$):** {{res:sc32_12_plot_01:keys}} $\implies \mathbf{{{res:sc32_12_plot_01:value}}}$.

#### Stack Trace Table (Evaluating at $t = 90^\circ$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 90 {{key:SIN}} | 0.00 | 0.00 | 0.00 | 1.000000 | 1.000000 |
| 02 | 90 3 {{key:×}} SIN | 0.00 | 0.00 | 1.000000 | -1.000000 | -1.000000 |
| 03 | 3 {{key:÷}} | 0.00 | 0.00 | 1.000000 | -0.333333 | -0.333333 |
| 04 | {{key:+}} | 0.00 | 0.00 | 0.00 | 0.666667 | 0.666667 |
| 05 | 90 5 {{key:×}} SIN | 0.00 | 0.00 | 0.666667 | 1.000000 | 1.000000 |
| 06 | 5 {{key:÷}} | 0.00 | 0.00 | 0.666667 | 0.200000 | 0.200000 |
| 07 | {{key:+}} | 0.00 | 0.00 | 0.00 | 0.866667 | 0.866667 |

---

### Problem 12.2: Damped Harmonic Oscillator Transient Ringing
In automotive suspension dynamics, the transient response of an underdamped shock absorber is modeled by:
$$x(t) = e^{-\zeta \omega_n t} \cos(\omega_d t)$$
With damping ratio $\zeta = 0.15$, natural frequency $\omega_n = 4.0\text{ rad/s}$, damped frequency $\omega_d = 3.9546\text{ rad/s}$:
$$x(t) = e^{-0.60 t} \cos(3.9546 t)$$

#### Baseline Mode: Radians (`{{key:RAD}}`)
1. Program in `{{key:EQN}}`: `T 0.60 {{key:×}} {{key:+/-}} {{key:eˣ}} T 3.9546 {{key:×}} {{key:COS}} {{key:×}}`
2. Domain: `0 {{key:STO}} "XMIN"`, `6 {{key:STO}} "XMAX"`
3. Press `{{key:PLOT}}`.

| Plot Telemetry | Crosshair Readout | Curve Feature |
| :--- | :--- | :--- |
| **Active Function** | `EXP(-0.2*X)*COS(2*X)` | Underdamped second-order exponential envelope |
| **Crosshair Cursor** | `X = 0.000000000`, `Y = 1.0000000000` | Initial peak displacement at $t = 0$ |

#### Stack Trace Table (Evaluating at $t = 1.0\text{ s}$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 1 {{key:ENTER}} .60 {{key:×}} | 0.00 | 0.00 | 1.000000 | 0.600000 | 0.600000_ |
| 02 | {{key:+/-}} {{key:eˣ}} | 0.00 | 0.00 | 1.000000 | 0.548812 | 0.548812 |
| 03 | 1 {{key:ENTER}} | 0.00 | 1.000000 | 0.548812 | 1.000000 | 1.000000_ |
| 04 | 3.9546 {{key:×}} | 0.00 | 1.000000 | 0.548812 | 3.954600 | 3.954600 |
| 05 | {{key:COS}} | 0.00 | 1.000000 | 0.548812 | -0.687229 | -0.687229 |
| 06 | {{key:×}} | 0.00 | 0.00 | 1.000000 | -0.377160 | -0.377160 |

- **Point Evaluation Check ($t = 1.0\text{ s}$ in `RAD`):** {{res:sc32_12_plot_02:keys}} $\implies \mathbf{{{res:sc32_12_plot_02:value}}}$.

---

### Problem 12.3: Cubic Extrema & Root Guess Bracketing for Brent's Solver
Before executing Richard Brent's root finder ({{key:SOLVE}}), plot the polynomial to visually bracket roots:
$$f(x) = x^3 - 3x^2 - 9x + 5 = 0$$

1. Program in `{{key:EQN}}`: `X 3 {{key:yˣ}} 3 X {{key:x²}} {{key:×}} {{key:-}} 9 X {{key:×}} {{key:-}} 5 {{key:+}}`
2. Domain: `4 {{key:+/-}} {{key:STO}} "XMIN"`, `6 {{key:STO}} "XMAX"`
3. Press `{{key:PLOT}}`.

| Plot Telemetry | Crosshair Readout | Curve Feature |
| :--- | :--- | :--- |
| **Active Function** | `X^3 - 6*X^2 + 11*X - 6` | Three real zero crossings at $X = 1, 2, 3$ |
| **Crosshair Cursor** | `X = 0.500000000`, `Y = -0.125000000` | Pre-root bracket inspection prior to `{{key:SOLVE}}` |
The plot visually reveals:
* Local maximum near $x = -1.0$: $f(-1) = 10.0$
* Local minimum near $x = 3.0$: $f(3) = -22.0$
* Three distinct roots: Root 1 in $[-3, -2]$, Root 2 in $[0, 1]$, Root 3 in $[4, 5]$.
Tracing crosshair to $x = 0.50$ and pressing `{{key:ENTER}}` pushes $0.50$ onto the stack. Pressing `{{key:SOLVE}} X` converges to root $x = 0.5185$ in 3 iterations.
- **Crosshair Evaluation Check ($x = 0.50$):** {{res:sc32_12_plot_03:keys}} $\implies \mathbf{{{res:sc32_12_plot_03:value}}}$.

#### Stack Trace Table (Evaluating at $x = 0.50$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .5 {{key:ENTER}} 3 {{key:yˣ}} | 0.00 | 0.00 | 0.500000 | 0.125000 | 0.125000 |
| 02 | 3 .5 {{key:x²}} {{key:×}} | 0.00 | 0.500000 | 0.125000 | 0.750000 | 0.750000 |
| 03 | {{key:-}} | 0.00 | 0.00 | 0.500000 | -0.625000 | -0.625000 |
| 04 | 9 .5 {{key:×}} | 0.00 | 0.500000 | -0.625000 | 4.500000 | 4.500000 |
| 05 | {{key:-}} | 0.00 | 0.00 | 0.500000 | -5.125000 | -5.125000 |
| 06 | 5 {{key:+}} | 0.00 | 0.00 | 0.00 | -0.125000 | -0.125000 |

---

### Problem 12.4: Standard Normal Distribution Bell Curve (Gaussian PDF)
Plot the Gaussian normal distribution curve with mean $\mu = 0$ and standard deviation $\sigma = 1$:
$$f(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}$$

1. Program in `{{key:EQN}}`: `X {{key:x²}} 2 {{key:÷}} {{key:+/-}} {{key:eˣ}} 2 {{key:ENTER}} {{key:π}} {{key:×}} {{key:√x}} {{key:÷}}`
2. Domain: `4 {{key:+/-}} {{key:STO}} "XMIN"`, `4 {{key:STO}} "XMAX"`
3. Press `{{key:PLOT}}`.

| Plot Telemetry | Crosshair Readout | Curve Feature |
| :--- | :--- | :--- |
| **Active Function** | `EXP(-X^2/2)/SQRT(2*π)` | Standard Normal probability density bell curve |
| **Crosshair Cursor** | `X = 0.000000000`, `Y = 0.3989422804` | Global maximum $1/\sqrt{2\pi}$ at mean $\mu = 0$ |
The peak at $x = 0$ renders at $y = \frac{1}{\sqrt{2\pi}} \approx 0.398942$.
- **Inflection Ordinate Check ($x = 1.0$):** {{res:sc32_12_plot_04:keys}} $\implies \mathbf{{{res:sc32_12_plot_04:value}}}$.

#### Stack Trace Table (Evaluating at $x = 1.0$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 1 {{keycap:x²}} 2 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.500000 | 0.500000 |
| 02 | {{key:+/-}} {{key:eˣ}} | 0.00 | 0.00 | 0.00 | 0.606531 | 0.606531 |
| 03 | 2 {{key:ENTER}} π {{key:×}} | 0.00 | 0.00 | 0.606531 | 6.283185 | 6.283185 |
| 04 | {{key:√x}} | 0.00 | 0.00 | 0.606531 | 2.506628 | 2.506628 |
| 05 | {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.241971 | 0.241971 |

---

### Problem 12.5: Low-Pass RC Filter Frequency Bode Magnitude Plot
The voltage gain of a first-order passive low-pass RC filter with cutoff frequency $f_c = 1000\text{ Hz}$ is:
$$|H(f)| = \frac{1}{\sqrt{1 + (f / 1000)^2}}$$
Plot gain across frequency domain $f \in [0, 5000\text{ Hz}]$:
1. Program in `{{key:EQN}}`: `F 1000 {{key:÷}} {{key:x²}} 1 {{key:+}} {{key:√x}} {{key:1/x}}`
2. Domain: `0 {{key:STO}} "XMIN"`, `5000 {{key:STO}} "XMAX"`
3. Press `{{key:PLOT}}`.

| Plot Telemetry | Crosshair Readout | Curve Feature |
| :--- | :--- | :--- |
| **Active Function** | `1/SQRT(1+(X/1000)^2)` | First-order RC low-pass magnitude transfer curve |
| **Crosshair Cursor** | `X = 1000.000000`, `Y = 0.7071067812` | Half-power $-3\text{ dB}$ corner frequency ($1/\sqrt{2}$) |
Trace to $f = 1000\text{ Hz}$: display confirms $y = 0.707107$ (the $-3\text{ dB}$ half-power point).
- **Corner Frequency Check ($f = 1000\text{ Hz}$):** {{res:sc32_12_plot_05:keys}} $\implies \mathbf{{{res:sc32_12_plot_05:value}}}$.

#### Stack Trace Table (Evaluating at $f = 1000\text{ Hz}$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 1000 {{key:ENTER}} | 0.00 | 0.00 | 1000.00 | 1000.00 | 1000.00_ |
| 02 | 1000 {{key:÷}} | 0.00 | 0.00 | 0.00 | 1.000000 | 1.000000 |
| 03 | {{keycap:x²}} 1 {{key:+}} | 0.00 | 0.00 | 0.00 | 2.000000 | 2.000000 |
| 04 | {{key:√x}} | 0.00 | 0.00 | 0.00 | 1.414214 | 1.414214 |
| 05 | {{key:1/x}} | 0.00 | 0.00 | 0.00 | 0.707107 | 0.707107 |

---

### Problem 12.6: High-Pass RC Filter Frequency Response
The high-pass filter frequency response is given by:
$$|H(f)| = \frac{f / f_c}{\sqrt{1 + (f / f_c)^2}}$$
For cutoff frequency $f_c = 1000\text{ Hz}$:
1. Program: `F 1000 {{key:÷}} {{key:STO}} A {{key:x²}} 1 {{key:+}} {{key:√x}} {{key:RCL}} A {{key:x⇄y}} {{key:÷}}`
2. Domain: `0 {{key:STO}} "XMIN"`, `5000 {{key:STO}} "XMAX"`
3. Press `{{key:PLOT}}`.
The curve begins at $0$ at DC ($f=0$), crosses $0.707107$ at $f = 1000\text{ Hz}$, and asymptotically approaches $1.00$ at high frequencies.
- **Octave-Above-Cutoff Check ($f = 2000\text{ Hz}$):** {{res:sc32_12_plot_06:keys}} $\implies \mathbf{{{res:sc32_12_plot_06:value}}}$.

#### Stack Trace Table (Evaluating at $f = 2000\text{ Hz}$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 2000 1000 {{key:÷}} | 0.00 | 0.00 | 0.00 | 2.000000 | 2.000000 |
| 02 | {{key:STO}} A | 0.00 | 0.00 | 0.00 | 2.000000 | 2.000000 |
| 03 | {{keycap:x²}} 1 {{key:+}} {{key:√x}} | 0.00 | 0.00 | 0.00 | 2.236068 | 2.236068 |
| 04 | {{key:RCL}} A | 0.00 | 0.00 | 2.236068 | 2.000000 | 2.000000 |
| 05 | {{key:x⇄y}} {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.894427 | 0.894427 |

---

### Problem 12.7: Sinc Function Diffraction Pattern
In optical slit diffraction and digital communications, the normalized sinc function represents the Fourier transform of a rectangular aperture:
$$y(x) = \frac{\sin x}{x}$$
Plot over $x \in [-4\pi, +4\pi]$ in Radians mode:
1. Domain: `-12.57 {{key:STO}} "XMIN"`, `12.57 {{key:STO}} "XMAX"`
2. Sinc curve exhibits central maximum at $x=0$ ($y=1.00$) and decaying side lobes with zero crossings at $\pm\pi, \pm 2\pi, \pm 3\pi, \pm 4\pi$.
- **Half-Lobe Amplitude Check ($x = \pi/2$):** {{res:sc32_12_plot_07:keys}} $\implies \mathbf{{{res:sc32_12_plot_07:value}}}$.

#### Stack Trace Table (Evaluating at $x = \pi/2 \approx 1.570796$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | {{keycap:π}} 2 {{key:÷}} | 0.00 | 0.00 | 0.00 | 1.570796 | 1.570796 |
| 02 | {{key:ENTER}} | 0.00 | 0.00 | 1.570796 | 1.570796 | 1.570796_ |
| 03 | {{key:SIN}} | 0.00 | 0.00 | 1.570796 | 1.000000 | 1.000000 |
| 04 | {{key:x⇄y}} {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.636620 | 0.636620 |

---

### Problem 12.8: Diode Forward Bias I-V Characteristic (Shockley Equation)
In solid-state semiconductor electronics, junction diode current follows:
$$I = I_s \left( e^{\frac{V}{n V_T}} - 1 \right)$$
For silicon diode with saturation current $I_s = 10^{-12}\text{ A}$, emission coefficient $n = 1.0$, thermal voltage $V_T = 0.026\text{ V}$:
1. Domain: `0 {{key:STO}} "XMIN"`, `0.80 {{key:STO}} "XMAX"`
2. Curve remains nearly zero until the threshold "knee" voltage ($V \approx 0.65\text{ V}$), then skyrockets exponentially.

#### Stack Trace Table (Evaluating at $V = 0.70\text{ V}$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .70 {{key:ENTER}} | 0.00 | 0.00 | 0.700000 | 0.700000 | 0.700000_ |
| 02 | .026 {{key:÷}} | 0.00 | 0.00 | 0.00 | 26.923077 | 26.923077 |
| 03 | {{key:eˣ}} 1 {{key:-}} | 0.00 | 0.00 | 0.00 | 4.914E11 | 4.914E11 |
| 04 | 1 {{key:E}} 12 {{key:+/-}} | 0.00 | 0.00 | 4.914E11 | 1.000E-12 | 1.000E-12 |
| 05 | {{key:×}} | 0.00 | 0.00 | 0.00 | 0.491410 | 0.491410 (A) |

---

### Problem 12.9: Resonant RLC Tank Circuit Frequency Response
The amplitude response of a series RLC resonant circuit is:
$$A(\omega) = \frac{1}{\sqrt{(1 - (\omega/\omega_0)^2)^2 + (2\zeta \omega/\omega_0)^2}}$$
With natural resonance $\omega_0 = 100\text{ rad/s}$ and damping ratio $\zeta = 0.05$ (high Q factor $Q = 10$):
Plot over $\omega \in [50, 150\text{ rad/s}]$: curve displays a razor-sharp resonant peak reaching $A(\omega_0) = \frac{1}{2\zeta} = 10.0$ at $\omega = 100\text{ rad/s}$.

#### Stack Trace Table (Evaluating at resonance $\omega = 100\text{ rad/s}$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 100 100 {{key:÷}} | 0.00 | 0.00 | 0.00 | 1.000000 | 1.000000 |
| 02 | {{keycap:x²}} 1 {{key:x⇄y}} | 0.00 | 0.00 | 1.000000 | 1.000000 | 1.000000 |
| 03 | {{key:-}} {{keycap:x²}} | 0.00 | 0.00 | 0.00 | 0.000000 | 0.000000 |
| 04 | 2 .05 {{key:×}} 1 {{key:×}} | 0.00 | 0.00 | 0.00 | 0.100000 | 0.100000 |
| 05 | {{keycap:x²}} {{key:+}} | 0.00 | 0.00 | 0.00 | 0.010000 | 0.010000 |
| 06 | {{key:√x}} {{key:1/x}} | 0.00 | 0.00 | 0.00 | 10.000000 | 10.000000 |

---

### Problem 12.10: Quadratic Parabola Vertex and Axis of Symmetry
Plot $y = -2x^2 + 8x - 3$ over $x \in [-1, 5]$:
1. Vertex formula: $x_v = -b / (2a) = -8 / (-4) = \mathbf{2.00}$.
2. Maximum value: $y_v = -2(4) + 16 - 3 = \mathbf{5.00}$.
3. Trace confirms vertex at $(2.00, 5.00)$.

#### Stack Trace Table (Evaluating at vertex $x = 2.0$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 2 {{keycap:x²}} 2 {{key:×}} {{key:+/-}} | 0.00 | 0.00 | 0.00 | -8.000000 | -8.000000 |
| 02 | 8 2 {{key:×}} | 0.00 | 0.00 | -8.000000 | 16.000000 | 16.000000 |
| 03 | {{key:+}} 3 {{key:-}} | 0.00 | 0.00 | 0.00 | 5.000000 | 5.000000 |

---

### Problem 12.11: Rational Function with Pole & Vertical Asymptote
Analyze $f(x) = \frac{1}{x - 2}$ over $x \in [0, 4]$:
The function possesses a non-removable pole at $x = 2.0$. The 64-point vector engine automatically clips asymptotic spikes that exceed viewport range, rendering the dual hyperbolic branches without crashing.

#### Stack Trace Table (Evaluating at $x = 2.5$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 2.5 {{key:ENTER}} | 0.00 | 0.00 | 2.500000 | 2.500000 | 2.500000_ |
| 02 | 2 {{key:-}} | 0.00 | 0.00 | 0.00 | 0.500000 | 0.500000 |
| 03 | {{key:1/x}} | 0.00 | 0.00 | 0.00 | 2.000000 | 2.000000 |

---

### Problem 12.12: Radioactive Exponential Decay Curve
Cobalt-60 activity decays according to $A(t) = 100 \times e^{-0.1315 t}$ ($t$ in years):
Plot over $t \in [0, 25\text{ years}]$:
Trace at $t = 5.27\text{ years}$ confirms $A = 50.0\%$ (the half-life).

#### Stack Trace Table (Evaluating at $t = 5.27\text{ yr}$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .1315 {{key:+/-}} | 0.00 | 0.00 | 0.00 | -0.131500 | -0.131500 |
| 02 | 5.27 {{key:×}} | 0.00 | 0.00 | 0.00 | -0.693005 | -0.693005 |
| 03 | {{key:eˣ}} | 0.00 | 0.00 | 0.00 | 0.500072 | 0.500072 |
| 04 | 100 {{key:×}} | 0.00 | 0.00 | 0.00 | 50.007200 | 50.01 (%) |

---

### Problem 12.13: Logistic Population Growth S-Curve (Sigmoidal)
Ecological population growth with carrying capacity $K = 1000$, growth rate $r = 0.5$, initial population $P_0 = 50$:
$$P(t) = \frac{K}{1 + \left(\frac{K - P_0}{P_0}\right) e^{-r t}} = \frac{1000}{1 + 19 e^{-0.5 t}}$$
Plot over $t \in [0, 20]$: curve shows initial exponential growth, an inflection point at $P = 500$ ($t = \ln(19)/0.5 \approx 5.89$), and asymptotic approach to $1000$.

#### Stack Trace Table (Evaluating at inflection $t = 5.88894\text{ s}$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .5 {{key:+/-}} | 0.00 | 0.00 | 0.00 | -0.500000 | -0.500000 |
| 02 | 5.88894 {{key:×}} | 0.00 | 0.00 | 0.00 | -2.944470 | -2.944470 |
| 03 | {{key:eˣ}} 19 {{key:×}} | 0.00 | 0.00 | 0.00 | 1.000000 | 1.000000 |
| 04 | 1 {{key:+}} | 0.00 | 0.00 | 0.00 | 2.000000 | 2.000000 |
| 05 | 1000 {{key:x⇄y}} {{key:÷}} | 0.00 | 0.00 | 0.00 | 500.000000 | 500.000000 |

---

### Problem 12.14: Michaelis-Menten Hyperbolic Enzyme Kinetics
Biochemical reaction velocity as a function of substrate concentration $[S]$:
$$v = \frac{V_{\max} [S]}{K_m + [S]}$$
With $V_{\max} = 100.0\text{ }\mu\text{mol/min}$ and Michaelis constant $K_m = 15.0\text{ mM}$:
Plot over $[S] \in [0, 100\text{ mM}]$:
Trace confirms that at $[S] = K_m = 15.0$, $v = 50.0\text{ }\mu\text{mol/min}$ ($V_{\max}/2$).

#### Stack Trace Table (Evaluating at $[S] = 15.0\text{ mM}$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 100 {{key:ENTER}} | 0.00 | 0.00 | 100.000000 | 100.000000 | 100.000000_ |
| 02 | 15 {{key:×}} | 0.00 | 0.00 | 0.00 | 1500.00000 | 1500.00000 |
| 03 | 15 15 {{key:+}} | 0.00 | 0.00 | 1500.00000 | 30.000000 | 30.000000 |
| 04 | {{key:÷}} | 0.00 | 0.00 | 0.00 | 50.000000 | 50.000000 |

---

### Problem 12.15: Weber-Fechner Acoustic Decibel Curve
Sound pressure level $L_p = 20 \log_{10}(P / P_0)$ where $P_0 = 20\text{ }\mu\text{Pa}$:
Logarithmic compression displays the human ear's vast dynamic range across acoustic pressures.

#### Stack Trace Table (Evaluating at conversational sound $P = 20,000\text{ }\mu\text{Pa} = 0.02\text{ Pa}$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 20000 {{key:ENTER}} | 0.00 | 0.00 | 20000.00 | 20000.00 | 20000.00_ |
| 02 | 20 {{key:÷}} | 0.00 | 0.00 | 0.00 | 1000.00000 | 1000.00000 |
| 03 | {{key:LOG}} | 0.00 | 0.00 | 0.00 | 3.000000 | 3.000000 |
| 04 | 20 {{key:×}} | 0.00 | 0.00 | 0.00 | 60.000000 | 60.00 (dB) |

---

### Problem 12.16: Bivariate Statistical Scatter Plot: Sensor Calibration
Four calibration points entered into statistical memory via `{{key:Σ+}}`:
$(10\text{ kPa}, 1.25\text{ V}), (20\text{ kPa}, 2.45\text{ V}), (30\text{ kPa}, 3.80\text{ V}), (40\text{ kPa}, 4.95\text{ V})$
1. Clear stats: `{{key:CLEAR}} {{key:CLΣ}}`
2. Enter points: `1.25 {{key:ENTER}} 10 {{key:Σ+}}`, `2.45 {{key:ENTER}} 20 {{key:Σ+}}`, `3.80 {{key:ENTER}} 30 {{key:Σ+}}`, `4.95 {{key:ENTER}} 40 {{key:Σ+}}`
3. Press `{{key:PLOT}}` and select `STAT`.

| Scatter Telemetry | Statistical Readout | Interpretation |
| :--- | :--- | :--- |
| **Sample Count** | `n = 4` | Four bivariate `(x, y)` calibration pairs accumulated via `{{key:Σ+}}` |
| **Linear Fit** | `m = 0.124500`, `r = 0.999565` | Least-squares trendline overlay with near-unity linearity |
The LCD renders the four 2×2 dot markers and superimposes the linear regression trendline $y = 0.1245x + 0.0000$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `{{key:CLEAR}} {{key:CLΣ}}` | 0.00 | 0.00 | 0.00 | 0.00 | Clear statistical accumulators |
| 02 | `1.25 {{key:ENTER}} 10 {{key:Σ+}}` | 0.00 | 0.00 | 1.25 | 1.00 | Pair 1: (10 kPa, 1.25 V); count n = 1 |
| 03 | `2.45 {{key:ENTER}} 20 {{key:Σ+}}` | 0.00 | 0.00 | 2.45 | 2.00 | Pair 2: (20 kPa, 2.45 V); count n = 2 |
| 04 | `3.80 {{key:ENTER}} 30 {{key:Σ+}}` | 0.00 | 0.00 | 3.80 | 3.00 | Pair 3: (30 kPa, 3.80 V); count n = 3 |
| 05 | `4.95 {{key:ENTER}} 40 {{key:Σ+}}` | 0.00 | 0.00 | 4.95 | 4.00 | Pair 4: (40 kPa, 4.95 V); count n = 4 |
| 06 | `{{key:m}}` | 0.00 | 0.00 | 4.95 | 0.1245 | Regression slope m = 0.124500 V/kPa |

---

### Problem 12.17: Statistical Residual Plot ($y_i - \hat{y}_i$)
To verify that linear regression errors are normally distributed and homoscedastic, plot residuals:
$$e_i = y_i - \hat{y}(x_i)$$
* $e_1 = 1.25 - 0.1245(10) = 1.25 - 1.245 = \mathbf{+0.005\text{ V}}$
* $e_2 = 2.45 - 0.1245(20) = 2.45 - 2.490 = \mathbf{-0.040\text{ V}}$
* $e_3 = 3.80 - 0.1245(30) = 3.80 - 3.735 = \mathbf{+0.065\text{ V}}$
* $e_4 = 4.95 - 0.1245(40) = 4.95 - 4.980 = \mathbf{-0.030\text{ V}}$
Residual points scatter randomly above and below the zero-error axis, confirming absence of systematic non-linear bias.

> **Named RPN Stack Idiom: *The Residual Scatter Zero-Bias Verification*** — Plot sensor calibration residuals and inspect uniform distribution about the zero-error axis on the dot-matrix display {{cite:ellenberg2014}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Accumulate Sensor Calibration Pairs:** Key each experimental voltage-pressure datum $(x_i, y_i)$ into Registers $Y$ and $X$ and commit via `{{key:Σ+}}`.
2. **Compute Linear Fit & Residual Offsets:** Execute linear regression (`{{key:m}}`, `{{key:b}}`), then evaluate residual differences $e_i = y_i - \hat{y}_i$ directly on the operational stack.
3. **Render Residual Scatter Plot (`{{key:PLOT}}`):** The 64-column engine renders the zero-error baseline and marks individual residual deviations ($+0.005\text{ V}$, $-0.040\text{ V}$, $+0.065\text{ V}$, $-0.030\text{ V}$) confirming random Gaussian noise without systematic sensor curvature.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `1.25 {{key:ENTER}}` | 0.00 | 0.00 | 1.250000 | 1.250000 | Measured voltage y1 = 1.25 V |
| 02 | `10 {{key:ENTER}} 0.1245 {{key:×}}` | 0.00 | 1.250000 | 10.000000 | 1.245000 | Predicted value ŷ(10) = 1.245 V |
| 03 | `{{key:-}}` | 0.00 | 0.00 | 0.00 | 0.005000 | Residual e1 = y1 - ŷ1 = +0.005000 V |
| 04 | `2.45 {{key:ENTER}} 20 {{key:ENTER}} 0.1245 {{key:×}} {{key:-}}` | 0.00 | 0.00 | 0.00 | -0.040000 | Residual e2 = 2.45 - 2.490 = -0.040000 V |

---

### Problem 12.18: Lissajous Figure 1:1 Phase Trajectory
In electrical engineering, comparing two equal-frequency signals with phase shift $\phi = 90^\circ$:
$$x(t) = \cos(t), \quad y(t) = \sin(t)$$
In Parametric Plot mode, this renders a circle of radius 1.

#### Stack Trace Table (Evaluating at $t = \pi/4 \approx 0.785398$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | {{keycap:π}} 4 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.785398 | 0.785398 |
| 02 | {{key:ENTER}} | 0.00 | 0.00 | 0.785398 | 0.785398 | 0.785398_ |
| 03 | {{key:COS}} | 0.00 | 0.00 | 0.785398 | 0.707107 | 0.707107 (X) |
| 04 | {{key:x⇄y}} {{key:SIN}} | 0.00 | 0.00 | 0.707107 | 0.707107 | 0.707107 (Y) |

---

### Problem 12.19: Lissajous Figure 1:2 Harmonic Ratio
Signal frequencies $f_x = 100\text{ Hz}, f_y = 200\text{ Hz}$:
$$x(t) = \sin(t), \quad y(t) = \sin(2t)$$
The parametric trajectory traces a figure-8 ("infinity" symbol $\infty$).

#### Stack Trace Table (Evaluating at $t = \pi/6 \approx 0.523599$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | {{keycap:π}} 6 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.523599 | 0.523599 |
| 02 | {{key:ENTER}} 2 {{key:×}} | 0.00 | 0.00 | 0.523599 | 1.047198 | 1.047198 |
| 03 | {{key:SIN}} | 0.00 | 0.00 | 0.523599 | 0.866025 | 0.866025 (Y) |
| 04 | {{key:x⇄y}} {{key:SIN}} | 0.00 | 0.00 | 0.866025 | 0.500000 | 0.500000 (X) |

---

### Problem 12.20: Acoustic Cardioid Microphone Polar Pattern
In studio acoustics, a cardioid directional microphone exhibits polar sensitivity $r(\theta) = 2(1 - \cos\theta)$ over $\theta \in [0^\circ, 360^\circ]$:
- **Curve Features:** Produces a heart-shaped cardioid with a complete null ($r = 0$) at $\theta = 0^\circ$, side sensitivity $r = 2.0$ at $\theta = \pm 90^\circ$, and peak rear rejection at $\theta = 180^\circ$ ($r = 4.0$).
- **Polar-to-Rectangular Vector Check:** To convert any $(x, y) = (1, 10)$ coordinate on a traced curve into polar magnitude $r = \sqrt{x^2 + y^2}$: {{res:sc32_12_plot_08:keys}} $\implies \mathbf{{{res:sc32_12_plot_08:value}}}$.
- **Step-by-Step RPN Reasoning & Stack Logic:**
  1. `10` — Enter 10 into Register $X$ ($X = 10$).
  2. `{{key:x²}}` — Square Register $X$ in place ($10^2$) $\rightarrow$ ($X = 100$).
  3. `1` — Enter 1 into Register $X$ ($Y = 100, X = 1$).
  4. `{{key:x²}}` — Square Register $X$ in place ($1^2$) $\rightarrow$ ($Y = 100, X = 1$).
  5. `{{key:+}}` — Add squared coordinates ($100 + 1 = 101$) to form the sum of squares.
  6. `{{key:√x}}` — Extract the principal square root $\sqrt{X}$ in place $\rightarrow$ ($X = 10.0499$).

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `10 {{key:x²}}` | 0.00 | 0.00 | 0.00 | 100.000000 | Square y-coordinate: 10^2 = 100 |
| 02 | `1 {{key:x²}}` | 0.00 | 0.00 | 100.000000 | 1.000000 | Square x-coordinate: 1^2 = 1 |
| 03 | `{{key:+}}` | 0.00 | 0.00 | 0.00 | 101.000000 | Sum of squares: 100 + 1 = 101 |
| 04 | `{{key:√x}}` | 0.00 | 0.00 | 0.00 | 10.049876 | Polar radius magnitude: r = 10.049876 |

---

### Problem 12.21: Four-Petal Quadrupole Polar Rose
In antenna array and quadrupole field synthesis, plotting $r(\theta) = 3 \sin(2\theta)$ over $\theta \in [0^\circ, 360^\circ]$:
- **Curve Features:** Renders four symmetric radiation petals of peak length $r_{\max} = 3.0$ oriented along the diagonal axes $\theta = 45^\circ, 135^\circ, 225^\circ, 315^\circ$, separated by zero-field nodal lines along the cardinal axes.
- **RPN Point Check ($\theta = 45^\circ$):** `45 {{key:ENTER}} 2 {{key:×}} {{key:SIN}} 3 {{key:×}}` $\implies \mathbf{3.0000}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `45 {{key:ENTER}}` | 0.00 | 0.00 | 45.000000 | 45.000000 | Load angle theta = 45.0 deg |
| 02 | `2 {{key:×}}` | 0.00 | 0.00 | 0.00 | 90.000000 | Double angle 2*theta = 90.0 deg |
| 03 | `{{key:SIN}}` | 0.00 | 0.00 | 0.00 | 1.000000 | sin(90 deg) = 1.000000 |
| 04 | `3 {{key:×}}` | 0.00 | 0.00 | 0.00 | 3.000000 | Petal peak radius r_max = 3.000000 |

---

### Problem 12.22: Third-Degree Polynomial Inflection & Concavity Transition
Analyze the cubic trajectory $y = x^3 - 6x^2 + 9x + 2$ over $x \in [0, 4]$:
- **First Derivative:** $y' = 3x^2 - 12x + 9 = 3(x-1)(x-3)$ reveals a local maximum at $(1, 6)$ and a local minimum at $(3, 2)$.
- **Second Derivative:** $y'' = 6x - 12 = 0 \implies x = 2$ marks the exact inflection point $(2, 4)$ where the curve transitions from concave-down to concave-up.

> **Named RPN Stack Idiom: *The Cubic Inflection & Extrema Tracer*** — Map third-degree polynomial stationary points and inflection transition in one visual sweep {{cite:strogatz2019}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Program Postfix Polynomial:** Store $x^3 - 6x^2 + 9x + 2$ in `{{key:EQN}}` using Horner streaming: `X 6 {{key:-}} X {{key:×}} 9 {{key:+}} X {{key:×}} 2 {{key:+}}`.
2. **Set Domain Interval $[0, 4]$:** Place lower bound $0$ into $Y$ and upper bound $4$ into $X$ ($0$ `{{key:ENTER}}` $4$), committing to window bounds via `{{key:STO}} "XMIN"` and `{{key:STO}} "XMAX"`.
3. **Render & Reticle Tracing (`{{key:PLOT}}`):** Trace with `{{key:↓}}` and `{{key:↑}}` to identify the local peak at $(1, 6)$, the inflection point at $(2, 4)$, and the local valley at $(3, 2)$ directly from status bar telemetry.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `2 {{key:ENTER}} 6 {{key:-}}` | 0.00 | 0.00 | 2.000000 | -4.000000 | x - 6 = 2 - 6 = -4 |
| 02 | `2 {{key:×}} 9 {{key:+}}` | 0.00 | 0.00 | 0.00 | 1.000000 | x(x - 6) + 9 = -8 + 9 = 1 |
| 03 | `2 {{key:×}} 2 {{key:+}}` | 0.00 | 0.00 | 0.00 | 4.000000 | Inflection point ordinate: y(2) = 4.000000 |

---

### Problem 12.23: Catenary Sag of Overhead Transmission Line
Suspension cable profile:
$$y(x) = a \cosh\left(\frac{x}{a}\right) - a$$
With scale parameter $a = 150\text{ m}$ over span $x \in [-60, +60\text{ m}]$:
At midspan $x = 0$, $y = 0$. At towers $x = \pm 60\text{ m}$, $y = 150(\cosh(0.40) - 1) = 150(1.081072 - 1) = \mathbf{12.16\text{ m}}$ sag.

#### Stack Trace Table (Evaluating at tower $x = 60\text{ m}$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 60 {{key:ENTER}} | 0.00 | 0.00 | 60.00 | 60.00 | 60.00_ |
| 02 | 150 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.400000 | 0.400000 |
| 03 | {{key:HYP}}{{key:COS}} | 0.00 | 0.00 | 0.00 | 1.081072 | 1.081072 |
| 04 | 1 {{key:-}} | 0.00 | 0.00 | 0.00 | 0.081072 | 0.081072 |
| 05 | 150 {{key:×}} | 0.00 | 0.00 | 0.00 | 12.160855 | 12.16 (m) |

---

### Problem 12.24: Gaussian Error Function ($\text{erf}$) Diffusion Profile
In Fickian heat and mass diffusion, concentration across a semi-infinite slab follows the Gaussian error function:
$$\text{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} dt$$
- **Curve Features:** The sigmoidal curve transitions smoothly from $-1.0$ at $-\infty$ to $+1.0$ at $+\infty$, passing through $(0, 0)$ with central inflection slope $\frac{2}{\sqrt{\pi}} \approx \mathbf{1.128379}$ (`{{key:π}} {{key:√x}} 2 {{key:x⇄y}} {{key:÷}}`).

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `{{key:π}}` | 0.00 | 0.00 | 0.00 | 3.141593 | Load constant pi |
| 02 | `{{key:√x}}` | 0.00 | 0.00 | 0.00 | 1.772454 | sqrt(pi) = 1.772454 |
| 03 | `2 {{key:x⇄y}}` | 0.00 | 0.00 | 2.000000 | 1.772454 | Push 2 to X, swap to place 2 in Y |
| 04 | `{{key:÷}}` | 0.00 | 0.00 | 0.00 | 1.128379 | Inflection slope: 2 / sqrt(pi) = 1.128379 |

---

### Problem 12.25: Wien Displacement Blackbody Radiation Curve
Plotting Planck's spectral radiance $B(\lambda, T) \propto \lambda^{-5} / (e^{hc/\lambda k_B T} - 1)$ for a tungsten filament at $T = 3000\text{ K}$:
- **Curve Features:** Displays the steep short-wavelength ultraviolet cutoff (resolving the classical Rayleigh-Jeans catastrophe) and a peak spectral emission at $\lambda_{\max} = \frac{2897.77\,\mu\text{m}\cdot\text{K}}{3000\text{ K}} = \mathbf{0.9659\,\mu\text{m}}$ in the near-infrared.

> **Named RPN Stack Idiom: *The Wien Blackbody Spectral Peak Pipeline*** — Trace Planck's radiation law across wavelengths to isolate peak infrared emission without numerical instability {{cite:strogatz2019}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Program Planck Radiance Function:** Enter spectral formula under `{{key:EQN}}` scaled for tungsten temperature $T = 3000\text{ K}$.
2. **Set Wavelength Domain $[0.1, 3.0\,\mu\text{m}]$:** Key $0.1$ `{{key:ENTER}}` $3.0$ on the stack and assign window boundaries `XMIN` and `XMAX`.
3. **Render & Locate Wien Peak (`{{key:PLOT}}`):** Sweep crosshair to maximum ordinate at $\lambda_{\max} \approx 0.966\,\mu\text{m}$, visually confirming the sharp UV Rayleigh-Jeans cutoff and smooth infrared decay.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `2897.77 {{key:ENTER}}` | 0.00 | 0.00 | 2897.770000 | 2897.770000 | Wien displacement constant b = 2897.77 um*K |
| 02 | `3000 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 0.965923 | Peak emission wavelength: lambda_max = 0.9659 um |

---

### Problem 12.26: Jakob Bernoulli's Lemniscate
In polar coordinates, the locus of points whose product of distances from two foci is constant follows $r^2 = 4 \cos(2\theta)$:
- **Curve Features:** Renders a symmetric figure-eight ribbon spanning $r \in [0, 2.0]$ over $\theta \in [-45^\circ, +45^\circ]$ and $[135^\circ, 225^\circ]$, while regions where $\cos(2\theta) < 0$ are automatically clipped as imaginary branches by the vector plotter.

> **Named RPN Stack Idiom: *The Lemniscate Dual-Lobe Polar Envelope*** — Render Bernoulli's classic figure-eight curve with automatic imaginary branch suppression {{cite:strogatz2012}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Program Polar Lemniscate Formula:** Key $r(\theta) = 2\sqrt{\cos(2\theta)}$ into `{{key:EQN}}` with angular mode set to Degrees (`{{key:DEG}}`).
2. **Set Angular Domain $[-45^\circ, +45^\circ]$:** Set $-45^\circ$ in $Y$ and $+45^\circ$ in $X$ for the primary right petal.
3. **Render Polar Geometry (`{{key:PLOT}}`):** Inspect the smooth double-loop lemniscate; the engine automatically clips non-physical imaginary roots where $\cos(2\theta) < 0$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `30 {{key:ENTER}} 2 {{key:×}}` | 0.00 | 0.00 | 30.000000 | 60.000000 | 2*theta = 60 deg |
| 02 | `{{key:COS}}` | 0.00 | 0.00 | 0.00 | 0.500000 | cos(60 deg) = 0.500000 |
| 03 | `{{key:√x}}` | 0.00 | 0.00 | 0.00 | 0.707107 | sqrt(cos(2*theta)) = 0.707107 |
| 04 | `2 {{key:×}}` | 0.00 | 0.00 | 0.00 | 1.414214 | Polar radius r(30 deg) = 1.414214 |

---

### Problem 12.27: Constant-Pitch Archimedean Spiral
In mechanical scroll compressors and vinyl groove geometry, the polar trajectory $r(\theta) = 0.5 \theta$ ($\theta$ in radians) expands linearly with rotation angle:
- **Curve Features:** Each full $2\pi$ revolution increases the radius by a constant pitch $\Delta r = 0.5(2\pi) = \pi \approx \mathbf{3.1416\text{ mm}}$.

> **Named RPN Stack Idiom: *The Archimedean Constant-Pitch Scroll*** — Verify linear spiral growth across multiple revolutions on the dot-matrix grid.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Program Linear Spiral Equation:** Enter $r(\theta) = 0.5\theta$ in `{{key:EQN}}` with Radians mode (`{{key:RAD}}`) active.
2. **Set Angular Domain $[0, 4\pi]$:** Push $0$ `{{key:ENTER}}` `4 {{key:π}} {{key:×}}` onto the stack and commit to window registers.
3. **Render & Measure Radial Pitch (`{{key:PLOT}}`):** Trace consecutive $2\pi$ wraps to verify constant radial spacing $\Delta r = \pi \approx 3.1416\text{ mm}$ between concentric scroll turns.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `{{key:π}} 2 {{key:×}}` | 0.00 | 0.00 | 3.141593 | 6.283185 | Full revolution theta = 2*pi = 6.283185 rad |
| 02 | `0.5 {{key:×}}` | 0.00 | 0.00 | 0.00 | 3.141593 | Radial pitch: Delta r = 0.5*theta = 3.141593 mm |

---

### Problem 12.28: Supersonic Prandtl-Meyer & Mach Cone Angle Curve
Plotting the supersonic shock wave half-angle $\mu(M) = \arcsin(1 / M)$ against Mach number $M \in [1.0, 5.0]$ in Degrees mode (`M {{key:1/x}} {{key:ASIN}}`):
- **Curve Features:** Starts at a normal sonic wave $\mu(1.0) = 90.0^\circ$, sweeps sharply through $\mu(2.0) = \mathbf{30.0^\circ}$, and narrows to a slender hypersonic cone $\mu(5.0) = \mathbf{11.537^\circ}$.

> **Named RPN Stack Idiom: *The Supersonic Mach Wave Conical Envelope*** — Map compressible flow shock angle decay from sonic boom to hypersonic flight.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Program Mach Angle Equation:** Key `M {{key:1/x}} {{key:ASIN}}` under `{{key:EQN}}` in Degrees mode (`{{key:DEG}}`).
2. **Set Mach Number Domain $[1.0, 5.0]$:** Enter $1.0$ `{{key:ENTER}}` $5.0$ and assign to domain boundaries `XMIN` and `XMAX`.
3. **Render Supersonic Transition (`{{key:PLOT}}`):** Trace crosshair from $\mu(1.0) = 90.0^\circ$ (normal shock) down to $\mu(2.0) = 30.0^\circ$ and $\mu(5.0) = 11.54^\circ$, observing supersonic cone narrowing.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `2 {{key:1/x}}` | 0.00 | 0.00 | 0.00 | 0.500000 | 1/M for Mach 2.0 = 0.500000 |
| 02 | `{{key:ASIN}}` | 0.00 | 0.00 | 0.00 | 30.000000 | Mach wave angle: mu(2.0) = 30.000000 deg |
| 03 | `5 {{key:1/x}}` | 0.00 | 0.00 | 30.000000 | 0.200000 | 1/M for Mach 5.0 = 0.200000 |
| 04 | `{{key:ASIN}}` | 0.00 | 0.00 | 30.000000 | 11.536959 | Hypersonic cone angle: mu(5.0) = 11.536959 deg |

---

### Problem 12.29: Thin-Airfoil Aerodynamic Lift Slope ($C_L$ vs. $\alpha$)
Classical thin-airfoil theory predicts section lift coefficient $C_L(\alpha) = 2\pi \alpha$ (for angle of attack $\alpha$ in radians, or $\frac{2\pi^2}{180}\alpha^\circ \approx 0.10966 \alpha^\circ$):
- **Curve Features:** Plotting over $\alpha \in [-5^\circ, +15^\circ]$ illustrates the linear inviscid lift regime up to $C_L(10^\circ) \approx \mathbf{1.0966}$ prior to boundary-layer flow separation.

> **Named RPN Stack Idiom: *The Aerodynamic Lift Slope Linear Regime*** — Trace theoretical thin-airfoil lift and identify the pre-stall linear envelope {{cite:hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Program Airfoil Lift Slope:** Key $C_L(\alpha) = 0.10966\,\alpha$ into `{{key:EQN}}` for geometric angle of attack $\alpha$ in degrees.
2. **Set Angle-of-Attack Bounds $[-5^\circ, +15^\circ]$:** Key $-5$ `{{key:ENTER}}` $15$ onto the stack and assign window boundaries.
3. **Render Linear Lift Line (`{{key:PLOT}}`):** Trace along the linear lift slope; verify $C_L = 0$ at zero angle of attack and $C_L \approx 1.10$ at $10^\circ$ prior to boundary-layer separation.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `10 {{key:ENTER}}` | 0.00 | 0.00 | 10.000000 | 10.000000 | Angle of attack alpha = 10.0 deg |
| 02 | `0.10966 {{key:×}}` | 0.00 | 0.00 | 0.00 | 1.096600 | Section lift coefficient: C_L = 1.096600 |

---

### Problem 12.30: Van der Waals Real Gas Isotherms
Pressure $P(V) = \frac{R T}{V - b} - \frac{a}{V^2}$:
Isotherms below critical temperature $T_c$ display characteristic van der Waals cubic loops, illustrating liquid-gas phase coexistence.

#### Stack Trace Table (Evaluating $P(V)$ at $V = 0.10\text{ m}^3, T = 300\text{ K}, R=8.314, a=0.36, b=0.04$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 8.314 300 {{key:×}} | 0.00 | 0.00 | 0.00 | 2494.20 | 2494.20 |
| 02 | .10 .04 {{key:-}} | 0.00 | 0.00 | 2494.20 | 0.060000 | 0.060000 |
| 03 | {{key:÷}} | 0.00 | 0.00 | 0.00 | 41570.00 | 41570.00 |
| 04 | .36 .10 {{key:x²}} {{key:÷}} | 0.00 | 0.00 | 41570.00 | 36.00000 | 36.00000 |
| 05 | {{key:-}} | 0.00 | 0.00 | 0.00 | 41534.00 | 41534.00(Pa) |

---

### Problem 12.31: Euler-Bernoulli Cantilever Beam Deflection Profile
Under an end point load $P$, the elastic curve of a cantilevered structural beam of length $L$ and flexural rigidity $EI$ follows:
$$y(x) = \frac{P x^2}{6 E I} (3L - x)$$
- **Curve Features:** Over $x \in [0, L]$, both deflection $y(0) = 0$ and slope $y'(0) = 0$ vanish at the fixed wall, curving parabolically-cubically to maximum tip deflection $\delta_{\max} = \frac{P L^3}{3 E I}$ at $x = L$.

> **Named RPN Stack Idiom: *The Cantilever Cubic Elastic Deflection Profile*** — Verify zero slope at structural anchor and cubic growth to maximum tip deflection {{cite:horowitz2015}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Program Beam Elastic Curve:** Key $y(x) = \frac{P x^2}{6EI}(3L - x)$ in `{{key:EQN}}` for beam length $L = 4.0\text{ m}$.
2. **Set Beam Span Domain $[0, 4.0\text{ m}]$:** Key $0$ `{{key:ENTER}}` $4.0$ on the stack and commit to domain limits `XMIN` and `XMAX`.
3. **Render & Reticle Tip Deflection (`{{key:PLOT}}`):** Trace from the clamped root ($y(0) = 0, y'(0) = 0$) to the free tip $x = 4.0\text{ m}$, verifying maximum deflection $\delta_{\max} = 3.92\text{ mm}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `4 {{key:ENTER}} 3 {{key:×}} 4 {{key:-}}` | 0.00 | 0.00 | 12.000000 | 8.000000 | Evaluate (3L - x) = 12 - 4 = 8.0 m |
| 02 | `4 {{key:x²}}` | 0.00 | 0.00 | 8.000000 | 16.000000 | Evaluate x^2 = 4^2 = 16.0 m^2 |
| 03 | `{{key:×}}` | 0.00 | 0.00 | 0.00 | 128.000000 | x^2 * (3L - x) = 128.0 m^3 |
| 04 | `3.0625 {{key:E}} 5 {{key:+/-}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 0.003920 | Maximum tip deflection: delta_max = 3.92 mm |

---

### Problem 12.32: Elastic Torsion Twist Profile Along a Drive Shaft
For a uniform circular transmission shaft of polar moment $J$ and shear modulus $G$ under torque $T$, the angular twist $\theta(x) = \frac{T x}{J G}$ plots as a straight line through the origin with constant torsional gradient $d\theta/dx = T/(JG)$.

> **Named RPN Stack Idiom: *The Torsional Shear Twist Gradient*** — Trace mechanical drive shaft angular displacement along structural axis.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Program Torsional Gradient Equation:** Key $\theta(x) = \frac{T}{JG}x$ into `{{key:EQN}}`.
2. **Set Shaft Length Domain $[0, L]$:** Key lower boundary $0$ and shaft tip length $L$ into Registers $Y$ and $X$.
3. **Render & Trace Torsion Slope (`{{key:PLOT}}`):** Trace linear twist profile along the shaft length, verifying constant shear stress distribution and tip twist angle.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `2.5 {{key:ENTER}}` | 0.00 | 0.00 | 2.500000 | 2.500000 | Shaft tip position x = 2.50 m |
| 02 | `0.0045 {{key:×}}` | 0.00 | 0.00 | 0.00 | 0.011250 | Angular twist: theta = 0.011250 rad |
| 03 | `180 {{key:×}} {{key:π}} {{key:÷}}` | 0.00 | 0.00 | 0.00 | 0.644578 | Tip twist angle in degrees: 0.6446 deg |

---

### Problem 12.33: Bivariate Scatter Plot: Hooke's Law Spring Calibration
Accumulating four experimental force-displacement pairs $(1\text{ cm}, 4.8\text{ N})$, $(2\text{ cm}, 10.1\text{ N})$, $(3\text{ cm}, 14.9\text{ N})$, and $(4\text{ cm}, 20.2\text{ N})$ via `{{key:Σ+}}` and selecting `{{key:PLOT}}` (`STAT` overlay) renders the four $2\times 2$ data markers alongside the least-squares regression line of slope $k = \mathbf{5.05\text{ N/cm}}$ ($505\text{ N/m}$) and correlation $r = \mathbf{0.9998}$.

> **Named RPN Stack Idiom: *The Bivariate Hooke's Law Calibration Overlay*** — Fit experimental force-displacement points and superimpose spring constant regression line {{cite:ellenberg2014}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Accumulate Experimental Pairs via `{{key:Σ+}}`:** Enter displacement $x$ in $Y$ and load force $F$ in $X$ for all 4 test weights.
2. **Calculate Spring Constant ($k$):** Tap `{{key:m}}` to resolve spring stiffness $k = 5.05\text{ N/cm}$ ($505\text{ N/m}$) and `{{key:r}}` to confirm linear correlation $r = 0.9998$.
3. **Render Scatter & Trendline (`{{key:PLOT}}`):** Select `STAT` overlay to render discrete $2\times 2$ pixel calibration markers overlaid with the continuous linear elastic response line.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `{{key:CLEAR}} {{key:CLΣ}}` | 0.00 | 0.00 | 0.00 | 0.00 | Clear statistical accumulators |
| 02 | `4.8 {{key:ENTER}} 1 {{key:Σ+}}` | 0.00 | 0.00 | 4.80 | 1.00 | Pair 1: (1 cm, 4.8 N); count n = 1 |
| 03 | `10.1 {{key:ENTER}} 2 {{key:Σ+}}` | 0.00 | 0.00 | 10.10 | 2.00 | Pair 2: (2 cm, 10.1 N); count n = 2 |
| 04 | `14.9 {{key:ENTER}} 3 {{key:Σ+}}` | 0.00 | 0.00 | 14.90 | 3.00 | Pair 3: (3 cm, 14.9 N); count n = 3 |
| 05 | `20.2 {{key:ENTER}} 4 {{key:Σ+}}` | 0.00 | 0.00 | 20.20 | 4.00 | Pair 4: (4 cm, 20.2 N); count n = 4 |
| 06 | `{{key:m}}` | 0.00 | 0.00 | 20.20 | 5.050000 | Spring stiffness: k = 5.050000 N/cm |

---

### Problem 12.34: Automotive Kinetic Energy & Braking Distance Parabola
Plotting $E_k(v) = \frac{1}{2} m v^2$ for a $m = 1,200\text{ kg}$ vehicle over speed $v \in [0, 40\text{ m/s}]$ (`V {{key:x²}} 600 {{key:×}}`) visually demonstrates why doubling highway speed from $15\text{ m/s}$ to $30\text{ m/s}$ quadruples kinetic energy from $135\text{ kJ}$ to $\mathbf{540\text{ kJ}}$.

> **Named RPN Stack Idiom: *The Parabolic Kinetic Energy Velocity Scaling*** — Visualize quadratic velocity scaling to highlight braking energy surge at highway speeds {{cite:munroe2014,parker2019}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Program Vehicle Energy Parabola:** Enter $E_k(v) = 600\,v^2$ into `{{key:EQN}}` for $1,200\text{ kg}$ automobile.
2. **Set Velocity Range $[0, 40\text{ m/s}]$:** Key $0$ `{{key:ENTER}}` $40$ onto the stack and assign window boundaries.
3. **Render Quadratic Curve (`{{key:PLOT}}`):** Trace crosshair from $15\text{ m/s}$ ($135\text{ kJ}$) to $30\text{ m/s}$ ($540\text{ kJ}$), verifying that doubling velocity quadruples kinetic energy and braking distance.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `15 {{key:x²}} 600 {{key:×}}` | 0.00 | 0.00 | 225.000000 | 135000.00 | Kinetic energy at 15 m/s: 135,000 J (135 kJ) |
| 02 | `30 {{key:x²}} 600 {{key:×}}` | 0.00 | 0.00 | 900.000000 | 540000.00 | Kinetic energy at 30 m/s: 540,000 J (540 kJ) |
| 03 | `{{key:x⇄y}} {{key:÷}}` | 0.00 | 0.00 | 0.00 | 4.000000 | Energy ratio 540/135 = 4.00x (quadrupled) |

---

### Problem 12.35: Relativistic Lorentz Gamma Factor ($\gamma$)
$$\gamma(v) = \frac{1}{\sqrt{1 - (v/c)^2}}$$
Plotted for velocity ratio $\beta = v/c \in [0.0, 0.99]$:
Remains near $1.0$ at low velocities, curves gently to $1.15$ at $\beta = 0.5$, and explodes asymptotically toward infinity as $\beta \to 1.0$.

#### Stack Trace Table (Evaluating at $\beta = 0.80$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .80 {{keycap:x²}} | 0.00 | 0.00 | 0.00 | 0.640000 | 0.640000 |
| 02 | 1 {{key:x⇄y}} {{key:-}} | 0.00 | 0.00 | 0.00 | 0.360000 | 0.360000 |
| 03 | {{key:√x}} {{key:1/x}} | 0.00 | 0.00 | 0.00 | 1.666667 | 1.666667 |

---

### Problem 12.36: Linear Thermal Dilatation Calibration Curve
Plotting $\Delta L(T) = \alpha L_0 (T - T_0)$ for an aluminum metrology bar ($\alpha = 23.1 \times 10^{-6}\text{ K}^{-1}$, $L_0 = 1.0\text{ m}$) over $T \in [273\text{ K}, 373\text{ K}]$ provides a direct visual reference line of slope $23.1\,\mu\text{m/K}$ ($2.31\text{ mm}$ total expansion over $100\text{ K}$).

> **Named RPN Stack Idiom: *The Thermal Metrology Dilatation Calibration*** — Sweep temperature to plot linear expansion of precision metrology standards.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Program Dilatation Line:** Enter $\Delta L(T) = \alpha L_0 (T - 273.15)$ in `{{key:EQN}}` for $1.0\text{ m}$ aluminum bar.
2. **Set Thermal Range $[273\text{ K}, 373\text{ K}]$:** Key $273$ `{{key:ENTER}}` $373$ onto the stack and assign to `XMIN` and `XMAX`.
3. **Render & Trace Expansion Gradient (`{{key:PLOT}}`):** Trace crosshair across the $100\text{ K}$ span, reading exact linear slope $23.1\,\mu\text{m/K}$ and total dilatation $2.31\text{ mm}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `373 {{key:ENTER}} 273 {{key:-}}` | 0.00 | 0.00 | 373.000000 | 100.000000 | Temperature change Delta T = 100.0 K |
| 02 | `23.1 {{key:E}} 6 {{key:+/-}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 0.002310 | Delta L = alpha * L0 * Delta T = 0.002310 m |
| 03 | `1000 {{key:×}}` | 0.00 | 0.00 | 0.00 | 2.310000 | Total thermal expansion: 2.31 mm |

---

### Problem 12.37: Stefan-Boltzmann Radiative Heat Emission
Power $P(T) = \varepsilon \sigma A T^4$:
Quartic curve demonstrates why radiative heat transfer dominates at high temperatures ($T > 1000\text{ K}$).

#### Stack Trace Table (Evaluating at $T = 1200\text{ K}, \varepsilon = 0.85, A = 0.50\text{ m}^2$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 1200 {{key:ENTER}} 4 {{key:yˣ}} | 0.00 | 0.00 | 0.00 | 2.0736E12 | 2.0736E12 |
| 02 | 5.67037E-8 {{key:×}} | 0.00 | 0.00 | 0.00 | 117580.8 | 117580.8 |
| 03 | .85 {{key:×}} .50 {{key:×}} | 0.00 | 0.00 | 0.00 | 49971.84 | 49971.84 (W) |

---

### Problem 12.38: Newton's Law of Cooling Exponential Asymptote
Plotting $T(t) = T_{\text{env}} + (T_0 - T_{\text{env}}) e^{-k t}$ for a quenched steel billet ($T_0 = 800\text{ K}$, $T_{\text{env}} = 300\text{ K}$, $k = 0.05\text{ s}^{-1}$) over $t \in [0, 100\text{ s}]$ (`T 0.05 {{key:×}} {{key:+/-}} {{key:eˣ}} 500 {{key:×}} 300 {{key:+}}`) illustrates rapid initial heat rejection followed by asymptotic approach to the $300\text{ K}$ ambient floor.

> **Named RPN Stack Idiom: *The Newton Cooling Thermal Transient Asymptote*** — Track quenched metal billet heat rejection to ambient equilibrium {{cite:strogatz2019}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Program Newton Cooling Law:** Enter $T(t) = 300 + 500\,e^{-0.05 t}$ in `{{key:EQN}}`.
2. **Set Quench Time Window $[0, 100\text{ s}]$:** Key $0$ `{{key:ENTER}}` $100$ onto the stack and assign to `XMIN` and `XMAX`.
3. **Render Thermal Decay (`{{key:PLOT}}`):** Trace exponential cooling curve from initial quench temperature $800\text{ K}$ at $t = 0$ toward ambient steady-state asymptote $300\text{ K}$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `20 {{key:ENTER}} 0.05 {{key:×}} {{key:+/-}}` | 0.00 | 0.00 | 20.000000 | -1.000000 | -kt = -0.05 * 20 = -1.0 |
| 02 | `{{key:eˣ}}` | 0.00 | 0.00 | 0.00 | 0.367879 | e^(-1) = 0.367879 |
| 03 | `500 {{key:×}}` | 0.00 | 0.00 | 0.00 | 183.939721 | (T0 - T_env) * e^(-kt) = 183.94 K |
| 04 | `300 {{key:+}}` | 0.00 | 0.00 | 0.00 | 483.939721 | Temperature at t = 20 s: 483.94 K |

---

## Advanced Statistical Regression Curve Overlays

When performing bivariate data analysis in `{{key:SUMS}}` mode, the SC-32 can superimpose four distinct mathematical curve models directly over the scatter points:

| Model | Formula | Transformation Protocol |
|:---|:---|:---|
| Linear | $y = m x + b$ | Native coordinates: $(x, y)$ |
| Logarithmic | $y = a \ln(x) + b$ | Semi-logarithmic: $(\ln x, y)$ |
| Exponential | $y = a e^{b x}$ | Semi-logarithmic: $(x, \ln y)$ |
| Power | $y = a x^b$ | Log-Log: $(\ln x, \ln y)$ |

### Goodness-of-Fit & Coefficient of Determination ($R^2$)
The correlation coefficient $r$ provided by `{{key:ŷ}}` quantifies the linear association between the transformed coordinates. The **Coefficient of Determination ($R^2$)** measures the proportion of variance explained by the model:

$$R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}} = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$

On the SC-32, squaring $r$ on the stack (`{{key:x²}}`) gives $R^2$ immediately. For the calibration dataset in Problem 12.16 ($r = 0.999565$), $R^2 = 0.999130$, proving that $99.91\%$ of output voltage variance is directly explained by applied pressure.

---

## Teaching & Instrument Architecture Notes

### Active Analytical Reticle Tracing & Root-Finding Handoff
In collegiate calculus and laboratory physics curricula, graphical calculation often risks becoming passive visualization: expressions are entered into opaque algebraic buffers, producing a disconnected plot. On the SC-32, the plotting system is designed as an active numerical workbench. The 64-point vector curve engine renders directly across the $132 \times 65$ transflective display in under 42 milliseconds via deterministic single-cycle stack evaluations. While inspecting a curve, moving the reticle with `{{keycap:↓}}` and `{{keycap:↑}}` reads live coordinates, and pressing `{{key:ENTER}}` immediately pushes the exact $(x, y)$ coordinate pair onto the operational stack (horizontal domain coordinate $x$ into Register $Y$, evaluated coordinate $y$ into Register $X$). This eliminates re-entry errors and allows students and engineers to pass graphical visual guesses directly into Brent's root solver (`{{key:SOLVE}}`) or numerical quadrature (`{{key:∫}}`).

### Fourier Waveform Synthesis & Dynamic Modeling
Constructing periodic functions or harmonic series (such as the square wave synthesis in Problem 12.1) using postfix notation allows learners to observe the constructive and destructive interference of Fourier components step by step. Similarly, plotting dynamic models such as logistic population growth or transient RC circuit responses directly reveals mathematical asymptotes, inflection points, and physical saturation ceilings without arbitrary plotting syntax errors.

### Dedicated Frame Buffer & Stack Preservation Architecture
Classic scientific RPN keystroke-programmable calculators (such as the HP-32SII) delivered compact programming but lacked graphic rasterization. The SC-32 marries low-overhead RPN program execution with a dedicated 1,072-byte display buffer. Evaluating 64 discrete domain points directly on hardware registers ($X, Y, Z, T$) bypasses repetitive tokenization and AST parsing, ensuring instantaneous rendering. Committing coordinates back to the stack preserves the four-level register contract, maintaining seamless continuity between visual curve analysis and numerical calculation.

---

## Diagnostic Checkpoints & Singularity Handling

<div class="admonition warning">
<p class="admonition-title">Diagnostic Checkpoint 12.1: Domain Range Singularities ($X_{\min} \ge X_{\max}$)</p>
<p>If you enter $X_{\min} = 10.0$ and $X_{\max} = 10.0$ (or $X_{\min} > X_{\max}$) and press `{{key:PLOT}}`, the calculator alerts `Error 01: INVALID DATA`. The lower domain limit $X_{\min}$ must be strictly less than $X_{\max}$.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Diagnostic Checkpoint 12.2: Extracting Traced Coordinates to the Stack</p>
<p>When tracing a curve with `{{keycap:↓}}` and `{{keycap:↑}}`, pressing `{{key:ENTER}}` exits plot mode and pushes the active crosshair coordinates onto the operational stack:</p>
</div>
> * Register $Y$ receives the horizontal coordinate $x$.
> * Register $X$ receives the vertical evaluated coordinate $y$.
> This allows you to immediately perform arithmetic or numerical root-finding on graphically extracted values.

<div class="admonition warning">
<p class="admonition-title">Diagnostic Checkpoint 12.3: Angular Mode Consistency in Waveform Plotting</p>
<p>When plotting trigonometric functions such as Fourier series or sinc waves over domains involving $\pi$ ($[-3.14, +3.14]$), ensure the calculator is in **Radians mode (`{{key:RAD}}`)**. Plotting over $[-3.14, +3.14]$ while in **Degrees mode (`{{key:DEG}}`)** will evaluate only a tiny $3.14^\circ$ sliver of the cycle!</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Diagnostic Checkpoint 12.4: Out-of-Bounds Arithmetic in Plot Loops</p>
<p>If an equation evaluates to an undefined result (such as $\sqrt{-1}$ without complex mode, or division by zero $\frac{1}{0}$) at one of the 64 sample points, the vector engine flags that point as an open discontinuity and does NOT connect vector lines across the singularity.</p>
</div>

---

## Summary & Looking Ahead

Chapter 12 brought equations to life on the SC-32's transflective graphic LCD. By pairing the RPN mathematical engine with the 64-point vector curve renderer (`{{key:PLOT}}`), you transformed analytical formulas into intuitive visual geometries. You configured domain windows ($X_{\min}, X_{\max}$), scaled vertical dynamic ranges, navigated interactive crosshairs (`{{keycap:↓}}`, `{{keycap:↑}}`) to inspect local extrema and inflection points, and pushed graphical coordinates directly onto the operational stack for subsequent numeric analysis.

Visual intuition and analytical keystrokes find their ultimate expression when applied to authentic engineering design problems. In **Chapter 13: Applied STEM Engineering Case Studies**, you will step into the shoes of multidisciplinary field engineers. You will solve comprehensive multi-page challenges spanning fluid dynamics in 3D printer hotends, multi-stage rocket trajectory integration, acoustic reverberation modeling, optical lens cascades via `{{key:x∥y}}`, and closed-loop civil geodetic survey traverses.
