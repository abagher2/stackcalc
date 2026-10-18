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

Alongside the cubic polynomial root and extrema inspection shown in the chapter opening figure above (`X^3 - 6*X^2 + 11*X - 6` over $X \in [0, 4]$, revealing zero crossings at $x = 1, 2, 3$), the following live screenshots illustrate two additional mathematical workflows on the $128 \times 52$ dot-matrix viewport:

#### 1. Shaded Definite Integral Area Under Curve (`3*X^2` on $[0, 4]$)
When plotting an integrand after or during Adaptive Romberg Quadrature (`{{key:∫}}`), the graphing viewport shades the vertical Riemann columns between the curve $y = f(x)$ and the horizontal axis $y = 0$, visually confirming net positive vs. negative area accumulation:

{{res:sc32_plot_romberg_shaded:screenshot|SC-32 Vector Plotter: Shaded Definite Integral of 3x² from 0 to 4 (Area = 64.0)}}

#### 2. Gaussian Normal Probability Density Curve ($Z \in [-3.5, +3.5]$)
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
| `{{key:↓}}` (Key 7) | Trace Previous | Moves crosshair left along curve |
| `{{key:↑}}` (Key 8) | Trace Next | Moves crosshair right on curve |
| `{{key:ENTER}}` | Commit Coordinates | Copies current (X, Y) to stack |
| `{{key:<-}}` or `{{key:C}}` | Exit Plot | Restores normal RPN stack view |

### The Concrete-Representational-Abstract (CRA) Graphing Continuum
1. **Concrete (The Visual Curve):** The physical LCD displays the continuous curve trajectory, revealing zeros, asymptotic singularities, local maxima, and harmonic overshoots at a glance.
2. **Representational (The Traced Point Reticle):** Tracing the curve with `{{key:↓}}` and `{{key:↑}}` moves a crosshair cursor along the discrete 64 evaluation points, linking the visual curve to discrete numerical coordinates displayed in the status bar.
3. **Abstract (The Stack Commitment):** Pressing `{{key:ENTER}}` copies the traced coordinates into the operational stack ($Y = x, X = y$), allowing immediate numerical root-finding, integration, or differentiation.

{{blocks:counting_tiles_array_3x8|Discrete Grid Sampling and Pixel Quantization Array}}
*Figure 12.2: Concrete discrete grid sampling array: mapping mathematical domain intervals to quantized display columns before hardware-accelerated Bresenham line interpolation.*

---

### The Algebraic Trap vs. StackCalc Superpower Showdown

| Challenge / Metric | Algebraic Trap (TI-84 / Infix) | Algebraic Strokes | StackCalc SC-32 Superpower | SC-32 Strokes | Superpower Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **Fourier Series**: Square Wave ($\sin t + \frac{1}{3}\sin 3t + \frac{1}{5}\sin 5t$) | Rigid formula line `Y1 = sin(X) + (1/3)*sin(3*X) + (1/5)*sin(5*X)`. Missing a parenthesis halts with `SYNTAX ERROR`. Repeated point re-evaluations re-parse token tree. | 42 | **Hardware Stack Vector Sampling**: Postfix expression `T SIN T 3 * SIN 3 / + T 5 * SIN 5 / +` evaluates directly on registers. Deterministic 64-point sweep in $<42\text{ ms}$; zero parenthesis stack overhead. | 22 | **48% fewer strokes + zero parenthesis syntax errors** |
| **Extrema & Zero Inspection**: Root Bracketing | Graph function, navigate `CALC` $\to$ `zero`, enter Left Bound, Right Bound, Guess via arrow keys. Numerical root is stranded on graph screen; must exit to home screen and re-type coordinate for subsequent integration. | 38 | **Interactive Reticle Stack Commitment**: Trace crosshair with `{{key:↓}}/{{key:↑}}` to visual zero/extrema; tap `{{key:ENTER}}` to commit exact $(x, y)$ coordinates into Registers $Y$ and $X$. Directly invoke `{{key:SOLVE}}` with zero re-entry. | 14 | **63% fewer strokes + direct stack-to-solver pipeline** |
| **Domain Window Sweep**: Dynamic Range Scaling | Open `WINDOW` menu, manually adjust `Xmin`, `Xmax`, `Xscl`, `Ymin`, `Ymax`, `Yscl`. If $Y$ bounds are mismatched, curve clips off-screen; user must execute trial-and-error `ZoomFit`. | 32 | **Stack-Direct Bounds & Hardware Auto-Scale**: Push domain bounds to stack `0 {{key:STO}} "XMIN" 10 {{key:STO}} "XMAX"`; engine automatically calculates $[Y_{\min}, Y_{\max}]$ across 64 samples and auto-scales vertical viewport in $<42\text{ ms}$. | 12 | **62% fewer strokes + automatic optimal vertical scaling** |
| **Scatter Data & Curve Fit**: Regression Overlay | Navigate `STAT` $\to$ `EDIT`, manually populate `L1` and `L2` column tables. Exit to `STAT PLOT`, enable `Plot1`. Navigate `STAT` $\to$ `CALC` $\to$ `LinReg`, paste `L1, L2, Y1`. Prone to dimension mismatch errors. | 46 | **Live Statistical Accumulation (`{{key:Σ+}}`)**: Stream raw $(x, y)$ pairs onto stack and press `{{key:Σ+}}`. Instant correlation $r$ and $R^2$ via `{{key:x²}}`; superimpose linear, exponential, logarithmic, or power regressions directly over scatter dots. | 18 | **61% fewer strokes + zero list-dimension mismatch** |

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
In collegiate calculus and laboratory physics curricula, graphical calculation often risks becoming passive visualization: expressions are entered into opaque algebraic buffers, producing a disconnected plot. On the SC-32, the plotting system is designed as an active numerical workbench. The 64-point vector curve engine renders directly across the $132 \times 65$ transflective display in under 42 milliseconds via deterministic single-cycle stack evaluations. While inspecting a curve, moving the reticle with `{{key:↓}}` and `{{key:↑}}` reads live coordinates, and pressing `{{key:ENTER}}` immediately pushes the exact $(x, y)$ coordinate pair onto the operational stack (horizontal domain coordinate $x$ into Register $Y$, evaluated coordinate $y$ into Register $X$). This eliminates re-entry errors and allows students and engineers to pass graphical visual guesses directly into Brent's root solver (`{{key:SOLVE}}`) or numerical quadrature (`{{key:∫}}`).

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
<p>When tracing a curve with `{{key:↓}}` and `{{key:↑}}`, pressing `{{key:ENTER}}` exits plot mode and pushes the active crosshair coordinates onto the operational stack:</p>
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

> **Thematic Arc I — Harmonic Waveforms, Damped Transients & Cartesian Function Plotting (Problems 12.1–12.10):** We open by rendering Fourier partials, RLC ringdown envelopes, and transfer functions on the $128 \times 64$ pixel canvas.

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
Using `{{key:↓}}` and `{{key:↑}}`, trace to $t = 90.0^\circ$:
$$y(90^\circ) = \sin(90^\circ) + \frac{1}{3}\sin(270^\circ) + \frac{1}{5}\sin(450^\circ) = 1.0 - 0.333333 + 0.200000 = \mathbf{0.866667}$$
The display confirms: `X: 90.000000000    Y: 0.8666666667`.
**Harmonic Sum Stack Check ($t = 90^\circ$):** {{res:sc32_12_plot_01:keys}} $\implies \mathbf{{{res:sc32_12_plot_01:value}}}$.

| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 90 {{key:SIN}} | 0.00 | 0.00 | 0.00 | 1.000000 | 1.000000 |
| 02 | 90 {{key:ENTER}} 3 {{key:×}} {{key:SIN}} | 0.00 | 0.00 | 1.000000 | -1.000000 | -1.000000 |
| 03 | 3 {{key:÷}} | 0.00 | 0.00 | 1.000000 | -0.333333 | -0.333333 |
| 04 | {{key:+}} | 0.00 | 0.00 | 0.00 | 0.666667 | 0.666667 |
| 05 | 90 {{key:ENTER}} 5 {{key:×}} {{key:SIN}} | 0.00 | 0.00 | 0.666667 | 1.000000 | 1.000000 |
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
| **Active Function** | `EXP(-0.6*T)*COS(3.9546*T)` | Underdamped second-order exponential envelope |
| **Crosshair Cursor** | `X = 0.000000000`, `Y = 1.0000000000` | Initial peak displacement at $t = 0$ |

| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 1 {{key:ENTER}} .60 {{key:×}} | 0.00 | 0.00 | 0.00 | 0.600000 | 0.600000_ |
| 02 | {{key:+/-}} {{key:eˣ}} | 0.00 | 0.00 | 0.00 | 0.548812 | 0.548812 |
| 03 | 1 {{key:ENTER}} | 0.00 | 0.548812 | 1.000000 | 1.000000 | 1.000000_ |
| 04 | 3.9546 {{key:×}} | 0.00 | 0.00 | 0.548812 | 3.954600 | 3.954600 |
| 05 | {{key:COS}} | 0.00 | 0.00 | 0.548812 | -0.687229 | -0.687229 |
| 06 | {{key:×}} | 0.00 | 0.00 | 0.00 | -0.377160 | -0.377160 |

**Point Evaluation Check ($t = 1.0\text{ s}$ in `RAD`):** {{res:sc32_12_plot_02:keys}} $\implies \mathbf{{{res:sc32_12_plot_02:value}}}$.

---

### Problem 12.3: Cubic Extrema & Root Guess Bracketing for Brent's Solver
Before executing Richard Brent's root finder ({{key:SOLVE}}), plot the polynomial to visually bracket roots:
$$f(x) = x^3 - 3x^2 - 9x + 5 = 0$$

1. Program in `{{key:EQN}}`: `X 3 {{key:yˣ}} 3 X {{key:x²}} {{key:×}} {{key:-}} 9 X {{key:×}} {{key:-}} 5 {{key:+}}`
2. Domain: `4 {{key:+/-}} {{key:STO}} "XMIN"`, `6 {{key:STO}} "XMAX"`
3. Press `{{key:PLOT}}`.

| Plot Telemetry | Crosshair Readout | Curve Feature |
| :--- | :--- | :--- |
| **Active Function** | `X^3 - 3*X^2 - 9*X + 5` | Three real zero crossings in $[-3,-2], [0,1], [4,5]$ |
| **Crosshair Cursor** | `X = 0.500000000`, `Y = -0.125000000` | Pre-root bracket inspection prior to `{{key:SOLVE}}` |

The plot visually reveals:
* Local maximum near $x = -1.0$: $f(-1) = 10.0$
* Local minimum near $x = 3.0$: $f(3) = -22.0$
* Three distinct roots: Root 1 in $[-3, -2]$, Root 2 in $[0, 1]$, Root 3 in $[4, 5]$.
Tracing crosshair to $x = 0.50$ and pressing `{{key:ENTER}}` pushes $0.50$ onto the stack. Pressing `{{key:SOLVE}} X` converges to root $x = 0.5185$ in 3 iterations.
**Crosshair Evaluation Check ($x = 0.50$):** {{res:sc32_12_plot_03:keys}} $\implies \mathbf{{{res:sc32_12_plot_03:value}}}$.

| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .5 {{key:ENTER}} 3 {{key:yˣ}} | 0.00 | 0.00 | 0.00 | 0.125000 | 0.125000 |
| 02 | 3 {{key:ENTER}} .5 {{key:x²}} {{key:×}} | 0.00 | 0.00 | 0.125000 | 0.750000 | 0.750000 |
| 03 | {{key:-}} | 0.00 | 0.00 | 0.00 | -0.625000 | -0.625000 |
| 04 | 9 {{key:ENTER}} .5 {{key:×}} | 0.00 | 0.00 | -0.625000 | 4.500000 | 4.500000 |
| 05 | {{key:-}} | 0.00 | 0.00 | 0.00 | -5.125000 | -5.125000 |
| 06 | 5 {{key:+}} | 0.00 | 0.00 | 0.00 | -0.125000 | -0.125000 |

---

### Problem 12.4: Standard Normal Distribution Bell Curve (Gaussian PDF)
Plot the Gaussian normal distribution curve with mean $\mu = 0$ and standard deviation $\sigma = 1$:
$$f(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}$$

1. Program in `{{key:EQN}}`: `X {{key:x²}} 2 {{key:÷}} {{key:+/-}} {{key:eˣ}} 2 {{key:π}} {{key:×}} {{key:√x}} {{key:÷}}`
2. Domain: `4 {{key:+/-}} {{key:STO}} "XMIN"`, `4 {{key:STO}} "XMAX"`
3. Press `{{key:PLOT}}`.

| Plot Telemetry | Crosshair Readout | Curve Feature |
| :--- | :--- | :--- |
| **Active Function** | `EXP(-X^2/2)/SQRT(2*π)` | Standard Normal probability density bell curve |
| **Crosshair Cursor** | `X = 0.000000000`, `Y = 0.3989422804` | Global maximum $1/\sqrt{2\pi}$ at mean $\mu = 0$ |

The peak at $x = 0$ renders at $y = \frac{1}{\sqrt{2\pi}} \approx 0.398942$.
**Inflection Ordinate Check ($x = 1.0$):** {{res:sc32_12_plot_04:keys}} $\implies \mathbf{{{res:sc32_12_plot_04:value}}}$.

| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 1 {{key:x²}} 2 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.500000 | 0.500000 |
| 02 | {{key:+/-}} {{key:eˣ}} | 0.00 | 0.00 | 0.00 | 0.606531 | 0.606531 |
| 03 | 2 {{key:π}} {{key:×}} | 0.00 | 0.00 | 0.606531 | 6.283185 | 6.283185 |
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
**Corner Frequency Check ($f = 1000\text{ Hz}$):** {{res:sc32_12_plot_05:keys}} $\implies \mathbf{{{res:sc32_12_plot_05:value}}}$.

| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 1000 {{key:ENTER}} | 0.00 | 0.00 | 1000.00 | 1000.00 | 1000.00_ |
| 02 | 1000 {{key:÷}} | 0.00 | 0.00 | 0.00 | 1.000000 | 1.000000 |
| 03 | {{key:x²}} 1 {{key:+}} | 0.00 | 0.00 | 0.00 | 2.000000 | 2.000000 |
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
**Octave-Above-Cutoff Check ($f = 2000\text{ Hz}$):** {{res:sc32_12_plot_06:keys}} $\implies \mathbf{{{res:sc32_12_plot_06:value}}}$.

Keying `2000 {{key:ENTER}} 1000 {{key:÷}} {{key:STO}} A` computes normalized frequency ratio $(2.00)$ in $X$ and stores it in variable $A$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 2.000000)$. Striking `{{key:x²}} 1 {{key:+}} {{key:√x}}` calculates denominator impedance modulus $\sqrt{1 + 2^2} = \sqrt{5} \approx 2.236068$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 2.236068)$. Recalling and dividing `{{key:RCL}} A {{key:x⇄y}} {{key:÷}}` resolves the high-pass transfer magnitude $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{0.894427})$.

---

### Problem 12.7: Sinc Function Diffraction Pattern
In optical slit diffraction and digital communications, the normalized sinc function represents the Fourier transform of a rectangular aperture:
$$y(x) = \frac{\sin x}{x}$$
Plot over $x \in [-4\pi, +4\pi]$ in Radians mode:
1. Domain: `-12.57 {{key:STO}} "XMIN"`, `12.57 {{key:STO}} "XMAX"`
2. Sinc curve exhibits central maximum at $x=0$ ($y=1.00$) and decaying side lobes with zero crossings at $\pm\pi, \pm 2\pi, \pm 3\pi, \pm 4\pi$.
**Half-Lobe Amplitude Check ($x = \pi/2$):** {{res:sc32_12_plot_07:keys}} $\implies \mathbf{{{res:sc32_12_plot_07:value}}}$.

Entering `{{key:RAD}} {{key:π}} 2 {{key:÷}}` computes the half-lobe argument $\pi/2 \approx 1.570796\text{ rad}$ in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 1.570796)$. Striking `{{key:SIN}}` evaluates numerator $\sin(\pi/2) = 1.000000$ in $X$ while preserving $\pi/2$ in `LASTX` $(T: 0.00, Z: 0.00, Y: 0.00, X: 1.000000)$. Recalling and dividing via `{{key:LASTX}} {{key:÷}}` lifts $1.000000$ into $Y$, restores $\pi/2$ into $X$, and divides to resolve the normalized sinc half-lobe amplitude $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{0.636620})$.

---

### Problem 12.8: Diode Forward Bias I-V Characteristic (Shockley Equation)
In solid-state semiconductor electronics, junction diode current follows:
$$I = I_s \left( e^{\frac{V}{n V_T}} - 1 \right)$$
For silicon diode with saturation current $I_s = 10^{-12}\text{ A}$, emission coefficient $n = 1.0$, thermal voltage $V_T = 0.026\text{ V}$:
1. Domain: `0 {{key:STO}} "XMIN"`, `0.80 {{key:STO}} "XMAX"`
2. Curve remains nearly zero until the threshold "knee" voltage ($V \approx 0.65\text{ V}$), then skyrockets exponentially.

| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .70 {{key:ENTER}} | 0.00 | 0.00 | 0.700000 | 0.700000 | 0.700000_ |
| 02 | .026 {{key:÷}} | 0.00 | 0.00 | 0.00 | 26.923077 | 26.923077 |
| 03 | {{key:eˣ}} 1 {{key:-}} | 0.00 | 0.00 | 0.00 | 4.9266E11 | 4.9266E11 |
| 04 | 1 {{key:E}} 12 {{key:+/-}} | 0.00 | 0.00 | 4.9266E11 | 1.000E-12 | 1.000E-12 |
| 05 | {{key:×}} | 0.00 | 0.00 | 0.00 | 0.492656 | 0.492656 (A) |

---

### Problem 12.9: Resonant RLC Tank Circuit Frequency Response
The amplitude response of a series RLC resonant circuit is:
$$A(\omega) = \frac{1}{\sqrt{(1 - (\omega/\omega_0)^2)^2 + (2\zeta \omega/\omega_0)^2}}$$
With natural resonance $\omega_0 = 100\text{ rad/s}$ and damping ratio $\zeta = 0.05$ (high Q factor $Q = 10$):
Plot over $\omega \in [50, 150\text{ rad/s}]$: curve displays a razor-sharp resonant peak reaching $A(\omega_0) = \frac{1}{2\zeta} = 10.0$ at $\omega = 100\text{ rad/s}$.

| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 100 {{key:ENTER}} 100 {{key:÷}} | 0.00 | 0.00 | 0.00 | 1.000000 | 1.000000 |
| 02 | {{key:x²}} 1 {{key:x⇄y}} | 0.00 | 0.00 | 1.000000 | 1.000000 | 1.000000 |
| 03 | {{key:-}} {{key:x²}} | 0.00 | 0.00 | 0.00 | 0.000000 | 0.000000 |
| 04 | 2 {{key:ENTER}} .05 {{key:×}} 1 {{key:×}} | 0.00 | 0.00 | 0.00 | 0.100000 | 0.100000 |
| 05 | {{key:x²}} {{key:+}} | 0.00 | 0.00 | 0.00 | 0.010000 | 0.010000 |
| 06 | {{key:√x}} {{key:1/x}} | 0.00 | 0.00 | 0.00 | 10.000000 | 10.000000 |

---

### Problem 12.10: Quadratic Parabola Vertex and Axis of Symmetry
Plot $y = -2x^2 + 8x - 3$ over $x \in [-1, 5]$:
1. Vertex formula: $x_v = -b / (2a) = -8 / (-4) = \mathbf{2.00}$.
2. Maximum value: $y_v = -2(4) + 16 - 3 = \mathbf{5.00}$.
3. Trace confirms vertex at $(2.00, 5.00)$.

| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 2 {{key:x²}} 2 {{key:×}} {{key:+/-}} | 0.00 | 0.00 | 0.00 | -8.000000 | -8.000000 |
| 02 | 8 {{key:ENTER}} 2 {{key:×}} | 0.00 | 0.00 | -8.000000 | 16.000000 | 16.000000 |
| 03 | {{key:+}} 3 {{key:-}} | 0.00 | 0.00 | 0.00 | 5.000000 | 5.000000 |

---

> **Thematic Arc II — Singularities, Bifurcations & Bivariate Scatter Overlays (Problems 12.11–12.20):** Inspecting poles, inflection points, and experimental `Σ+` scatter clouds overlaid with least-squares regression lines.

### Problem 12.11: Rational Function with Pole & Vertical Asymptote
Analyze $f(x) = \frac{1}{x - 2}$ over $x \in [0, 4]$:
The function possesses a non-removable pole at $x = 2.0$. The 64-point vector engine automatically clips asymptotic spikes that exceed viewport range, rendering the dual hyperbolic branches without crashing.

Executing `2.5 {{key:ENTER}} 2 {{key:-}}` evaluates denominator offset $(0.500000)$ in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 0.500000)$. Striking `{{key:1/x}}` computes the reciprocal pole value $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{2.000000})$.

---

### Problem 12.12: Radioactive Exponential Decay Curve
Cobalt-60 activity decays according to $A(t) = 100 \times e^{-0.1315 t}$ ($t$ in years):
Plot over $t \in [0, 25\text{ years}]$:
Trace at $t = 5.27\text{ years}$ confirms $A = 50.0\%$ (the half-life).

Pushing `.1315 {{key:+/-}} 5.27 {{key:×}}` forms the exponential exponent $-0.693005$ $(T: 0.00, Z: 0.00, Y: 0.00, X: -0.693005)$. Striking `{{key:eˣ}}` yields the decayed fraction $(0.500072)$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 0.500072)$. Scaling `100 {{key:×}}` resolves remaining radioactivity $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{50.01}\%)$.

---

### Problem 12.13: Logistic Population Growth S-Curve (Sigmoidal)
Ecological population growth with carrying capacity $K = 1000$, growth rate $r = 0.5$, initial population $P_0 = 50$:
$$P(t) = \frac{K}{1 + \left(\frac{K - P_0}{P_0}\right) e^{-r t}} = \frac{1000}{1 + 19 e^{-0.5 t}}$$
Plot over $t \in [0, 20]$: curve shows initial exponential growth, an inflection point at $P = 500$ ($t = \ln(19)/0.5 \approx 5.89$), and asymptotic approach to $1000$.

Running `.5 {{key:+/-}} 5.88894 {{key:×}} {{key:eˣ}} 19 {{key:×}}` evaluates denominator exponential factor $(1.000000)$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 1.000000)$. Adding `1 {{key:+}}` yields total denominator $(2.000000)$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 2.000000)$. Keying capacity and dividing `1000 {{key:x⇄y}} {{key:÷}}` resolves the inflection population $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{500.000000})$.

---

### Problem 12.14: Michaelis-Menten Hyperbolic Enzyme Kinetics
Biochemical reaction velocity as a function of substrate concentration $[S]$:
$$v = \frac{V_{\max} [S]}{K_m + [S]}$$
With $V_{\max} = 100.0\text{ }\mu\text{mol/min}$ and Michaelis constant $K_m = 15.0\text{ mM}$:
Plot over $[S] \in [0, 100\text{ mM}]$:
Trace confirms that at $[S] = K_m = 15.0$, $v = 50.0\text{ }\mu\text{mol/min}$ ($V_{\max}/2$).

Loading `100 {{key:ENTER}} 15 {{key:×}}` evaluates numerator product $(1500.00)$ in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 1500.00)$. Evaluating denominator `15 {{key:ENTER}} 15 {{key:+}}` gives $30.00$ in $X$ while freezing $1500.00$ in $Y$ $(T: 0.00, Z: 0.00, Y: 1500.00, X: 30.00)$. Striking `{{key:÷}}` resolves half-maximal enzyme velocity $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{50.000000}\text{ }\mu\text{mol/min})$.

---

### Problem 12.15: Weber-Fechner Acoustic Decibel Curve
Sound pressure level $L_p = 20 \log_{10}(P / P_0)$ where $P_0 = 20\text{ }\mu\text{Pa}$:
Logarithmic compression displays the human ear's vast dynamic range across acoustic pressures.

Evaluating `20000 {{key:ENTER}} 20 {{key:÷}}` evaluates pressure ratio $(1000.00)$ in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 1000.00)$. Striking `{{key:LOG}}` computes base-10 logarithm $(3.000000)$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 3.000000)$. Scaling by `20 {{key:×}}` yields conversational acoustic sound level $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{60.00}\text{ dB})$.

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
| 03 | `2.45 {{key:ENTER}} 20 {{key:Σ+}}` | 0.00 | 1.25 | 2.45 | 2.00 | Pair 2: (20 kPa, 2.45 V); count n = 2 |
| 04 | `3.80 {{key:ENTER}} 30 {{key:Σ+}}` | 1.25 | 2.45 | 3.80 | 3.00 | Pair 3: (30 kPa, 3.80 V); count n = 3 |
| 05 | `4.95 {{key:ENTER}} 40 {{key:Σ+}}` | 2.45 | 3.80 | 4.95 | 4.00 | Pair 4: (40 kPa, 4.95 V); count n = 4 |
| 06 | `{{key:m}}` | 2.45 | 3.80 | 4.95 | 0.1245 | Regression slope m = 0.124500 V/kPa |

---

### Problem 12.17: Statistical Residual Plot ($y_i - \hat{y}_i$)
To verify that linear regression errors are normally distributed and homoscedastic, plot residuals:
$$e_i = y_i - \hat{y}(x_i)$$
* $e_1 = 1.25 - 0.1245(10) = 1.25 - 1.245 = \mathbf{+0.005\text{ V}}$
* $e_2 = 2.45 - 0.1245(20) = 2.45 - 2.490 = \mathbf{-0.040\text{ V}}$
* $e_3 = 3.80 - 0.1245(30) = 3.80 - 3.735 = \mathbf{+0.065\text{ V}}$
* $e_4 = 4.95 - 0.1245(40) = 4.95 - 4.980 = \mathbf{-0.030\text{ V}}$
Residual points scatter randomly above and below the zero-error axis, confirming absence of systematic non-linear bias.

> ***The Residual Scatter Zero-Bias Verification*** — Plot sensor calibration residuals and inspect uniform distribution about the zero-error axis on the dot-matrix display {{cite:ellenberg2014}}.

Entering measured voltage `1.25 {{key:ENTER}}` places $1.25$ into $Y$ $(T: 0.0000, Z: 0.0000, Y: 1.250000, X: 1.250000)$. Evaluating predicted value `10 {{key:ENTER}} 0.1245 {{key:×}}` gives $\hat{y}_1 = 1.245000$ in $X$ $(T: 0.0000, Z: 0.000000, Y: 1.250000, X: 1.245000)$. Subtracting `{{key:-}}` yields residual $e_1 = y_1 - \hat{y}_1$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{+0.005000}\text{ V})$. Repeating for pair 2 `2.45 {{key:ENTER}} 20 {{key:ENTER}} 0.1245 {{key:×}} {{key:-}}` yields $e_2$ $(T: 0.0050, Z: 0.0050, Y: 0.0050, X: \mathbf{-0.040000}\text{ V})$.

---

### Problem 12.18: Lissajous Figure 1:1 Phase Trajectory
In electrical engineering, comparing two equal-frequency signals with phase shift $\phi = 90^\circ$:
$$x(t) = \cos(t), \quad y(t) = \sin(t)$$
In Parametric Plot mode, this renders a circle of radius 1.

In `{{key:RAD}}` mode, evaluating phase parameter `{{key:π}} 4 {{key:÷}} {{key:ENTER}}` places $t = \pi/4 \approx 0.785398$ into both $Y$ and $X$ $(T: 0.00, Z: 0.00, Y: 0.785398, X: 0.785398)$. Striking `{{key:COS}}` computes horizontal coordinate $x = \cos(\pi/4) \approx 0.707107$ in $X$ while freezing $t$ in $Y$ $(T: 0.00, Z: 0.00, Y: 0.785398, X: 0.707107)$. Executing `{{key:x⇄y}} {{key:SIN}}` evaluates vertical coordinate $y = \sin(\pi/4)$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.707107, X: \mathbf{0.707107})$, confirming circular trajectory.

---

### Problem 12.19: Lissajous Figure 1:2 Harmonic Ratio
Signal frequencies $f_x = 100\text{ Hz}, f_y = 200\text{ Hz}$:
$$x(t) = \sin(t), \quad y(t) = \sin(2t)$$
The parametric trajectory traces a figure-8 ("infinity" symbol $\infty$).

In `{{key:RAD}}` mode, keying `{{key:π}} 6 {{key:÷}} {{key:ENTER}}` places $t = \pi/6 \approx 0.523599$ into both $Y$ and $X$ $(T: 0.00, Z: 0.00, Y: 0.523599, X: 0.523599)$. Duplicating, doubling, and taking sine via `{{key:ENTER}} 2 {{key:×}} {{key:SIN}}` evaluates vertical harmonic coordinate $y = \sin(2t) \approx 0.866025$ in $X$ while freezing $t$ in $Y$ $(T: 0.00, Z: 0.00, Y: 0.523599, X: 0.866025)$. Swapping and taking sine `{{key:x⇄y}} {{key:SIN}}` resolves fundamental horizontal coordinate $x = \sin(t) = \mathbf{0.500000}$ in $X$ while preserving $y = 0.866025$ in $Y$ $(T: 0.00, Z: 0.00, Y: 0.866025, X: 0.500000)$, tracing the classic figure-8 contour.

---

### Problem 12.20: Acoustic Cardioid Microphone Polar Pattern
In studio acoustics, a cardioid directional microphone exhibits polar sensitivity $r(\theta) = 2(1 - \cos\theta)$ over $\theta \in [0^\circ, 360^\circ]$:
**Curve Features:** Produces a heart-shaped cardioid with a complete null ($r = 0$) at $\theta = 0^\circ$, side sensitivity $r = 2.0$ at $\theta = \pm 90^\circ$, and peak rear rejection at $\theta = 180^\circ$ ($r = 4.0$).
**Polar-to-Rectangular Vector Check:** To convert any $(x, y) = (1, 10)$ coordinate on a traced curve into polar magnitude $r = \sqrt{x^2 + y^2}$: {{res:sc32_12_plot_08:keys}} $\implies \mathbf{{{res:sc32_12_plot_08:value}}}$.

Squaring ordinate `10 {{key:x²}}` places $100.000000$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 100.000000)$. Keying abscissa and squaring `1 {{key:x²}}` places $1.000000$ in $X$ while lifting $100.000000$ to $Y$ $(T: 0.00, Z: 0.00, Y: 100.000000, X: 1.000000)$. Striking `{{key:+}}` yields the coordinate sum of squares $(101.000000)$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 101.000000)$. Extracting square root `{{key:√x}}` resolves polar radius magnitude $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{10.049876})$.

---

> **Thematic Arc III — Polar Radiation Patterns, Parametric Lissajous Figures & Phase Portraits (Problems 12.21–12.30):** Exploring antenna lobes, orbital conics, and phase-space trajectories.

### Problem 12.21: Four-Petal Quadrupole Polar Rose
In antenna array and quadrupole field synthesis, plotting $r(\theta) = 3 \sin(2\theta)$ over $\theta \in [0^\circ, 360^\circ]$:
**Curve Features:** Renders four symmetric radiation petals of peak length $r_{\max} = 3.0$ oriented along the diagonal axes $\theta = 45^\circ, 135^\circ, 225^\circ, 315^\circ$, separated by zero-field nodal lines along the cardinal axes.
**RPN Point Check ($\theta = 45^\circ$):** `45 {{key:ENTER}} 2 {{key:×}} {{key:SIN}} 3 {{key:×}}` $\implies \mathbf{3.0000}$.

Loading angle and doubling `45 {{key:ENTER}} 2 {{key:×}}` yields $2\theta = 90.0^\circ$ in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 90.000000)$. Striking `{{key:SIN}}` evaluates $\sin(90^\circ) = 1.000000$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 1.000000)$. Scaling by `3 {{key:×}}` resolves the maximum petal radius $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{3.000000})$.

---

### Problem 12.22: Third-Degree Polynomial Inflection & Concavity Transition
Analyze the cubic trajectory $y = x^3 - 6x^2 + 9x + 2$ over $x \in [0, 4]$:
**First Derivative:** $y' = 3x^2 - 12x + 9 = 3(x-1)(x-3)$ reveals a local maximum at $(1, 6)$ and a local minimum at $(3, 2)$.
**Second Derivative:** $y'' = 6x - 12 = 0 \implies x = 2$ marks the exact inflection point $(2, 4)$ where the curve transitions from concave-down to concave-up.

> ***The Cubic Inflection & Extrema Tracer*** — Map third-degree polynomial stationary points and inflection transition in one visual sweep {{cite:strogatz2019}}.

Loading inflection abscissa `2 {{key:ENTER}} 6 {{key:-}}` evaluates $x - 6 = -4$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.000000, X: -4.000000)$. Chaining Horner terms `2 {{key:×}} 9 {{key:+}}` yields $x(x - 6) + 9 = 1.000000$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 1.000000)$. Finalizing polynomial `2 {{key:×}} 2 {{key:+}}` computes the exact inflection ordinate $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{4.000000})$.

---

### Problem 12.23: Catenary Sag of Overhead Transmission Line
Suspension cable profile:
$$y(x) = a \cosh\left(\frac{x}{a}\right) - a$$
With scale parameter $a = 150\text{ m}$ over span $x \in [-60, +60\text{ m}]$:
At midspan $x = 0$, $y = 0$. At towers $x = \pm 60\text{ m}$, $y = 150(\cosh(0.40) - 1) = 150(1.081072 - 1) = \mathbf{12.16\text{ m}}$ sag.

| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 60 {{key:ENTER}} | 0.00 | 0.00 | 60.00 | 60.00 | 60.00_ |
| 02 | 150 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.400000 | 0.400000 |
| 03 | {{key:HYP}} {{key:COS}} | 0.00 | 0.00 | 0.00 | 1.081072 | 1.081072 |
| 04 | 1 {{key:-}} | 0.00 | 0.00 | 0.00 | 0.081072 | 0.081072 |
| 05 | 150 {{key:×}} | 0.00 | 0.00 | 0.00 | 12.160855 | 12.16 (m) |

---

### Problem 12.24: Gaussian Error Function ($\text{erf}$) Diffusion Profile
In Fickian heat and mass diffusion, concentration across a semi-infinite slab follows the Gaussian error function:
$$\text{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} dt$$
**Curve Features:** The sigmoidal curve transitions smoothly from $-1.0$ at $-\infty$ to $+1.0$ at $+\infty$, passing through $(0, 0)$ with central inflection slope $\frac{2}{\sqrt{\pi}} \approx \mathbf{1.128379}$ (`{{key:π}} {{key:√x}} 2 {{key:x⇄y}} {{key:÷}}`).

Typing `{{key:π}} {{key:√x}}` computes $\sqrt{\pi} \approx 1.772454$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 1.772454)$. Loading constant and swapping `2 {{key:x⇄y}}` positions $2.00$ in $Y$ and $\sqrt{\pi}$ in $X$ $(T: 0.00, Z: 0.00, Y: 2.000000, X: 1.772454)$. Striking `{{key:÷}}` evaluates central inflection slope $2/\sqrt{\pi}$ $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{1.128379})$.

---

### Problem 12.25: Wien Displacement Blackbody Radiation Curve
Plotting Planck's spectral radiance $B(\lambda, T) \propto \lambda^{-5} / (e^{hc/\lambda k_B T} - 1)$ for a tungsten filament at $T = 3000\text{ K}$:
**Curve Features:** Displays the steep short-wavelength ultraviolet cutoff (resolving the classical Rayleigh-Jeans catastrophe) and a peak spectral emission at $\lambda_{\max} = \frac{2897.77\,\mu\text{m}\cdot\text{K}}{3000\text{ K}} = \mathbf{0.9659\,\mu\text{m}}$ in the near-infrared.

> ***The Wien Blackbody Spectral Peak Pipeline*** — Trace Planck's radiation law across wavelengths to isolate peak infrared emission without numerical instability {{cite:strogatz2019}}.

Loading Wien displacement constant `2897.77 {{key:ENTER}}` places $2897.77\,\mu\text{m}\cdot\text{K}$ in $Y$ $(T: 0.00, Z: 0.00, Y: 2897.770000, X: 2897.770000)$. Keying filament temperature and dividing `3000 {{key:÷}}` computes peak spectral wavelength $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{0.965923}\,\mu\text{m})$, confirming peak infrared emission.

---

### Problem 12.26: Jakob Bernoulli's Lemniscate
In polar coordinates, the locus of points whose product of distances from two foci is constant follows $r^2 = 4 \cos(2\theta)$:
**Curve Features:** Renders a symmetric figure-eight ribbon spanning $r \in [0, 2.0]$ over $\theta \in [-45^\circ, +45^\circ]$ and $[135^\circ, 225^\circ]$, while regions where $\cos(2\theta) < 0$ are automatically clipped as imaginary branches by the vector plotter.

> ***The Lemniscate Dual-Lobe Polar Envelope*** — Render Bernoulli's classic figure-eight curve with automatic imaginary branch suppression {{cite:strogatz2012}}.

Inputting `30 {{key:ENTER}} 2 {{key:×}}` evaluates doubled angle $2\theta = 60.0^\circ$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.000000, X: 60.000000)$. Striking `{{key:COS}}` computes $\cos(60^\circ) = 0.500000$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 0.500000)$. Striking `{{key:√x}} 2 {{key:×}}` resolves the polar radius $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{1.414214})$.

---

### Problem 12.27: Constant-Pitch Archimedean Spiral
In mechanical scroll compressors and vinyl groove geometry, the polar trajectory $r(\theta) = 0.5 \theta$ ($\theta$ in radians) expands linearly with rotation angle:
**Curve Features:** Each full $2\pi$ revolution increases the radius by a constant pitch $\Delta r = 0.5(2\pi) = \pi \approx \mathbf{3.1416\text{ mm}}$.

> ***The Archimedean Constant-Pitch Scroll*** — Verify linear spiral growth across multiple revolutions on the dot-matrix grid.

Evaluating full turn `{{key:π}} 2 {{key:×}}` places $2\pi \approx 6.283185\text{ rad}$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.000000, X: 6.283185)$. Scaling `0.5 {{key:×}}` calculates radial pitch increment $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{3.141593}\text{ mm})$, verifying constant spiral pitch.

---

### Problem 12.28: Supersonic Prandtl-Meyer & Mach Cone Angle Curve
Plotting the supersonic shock wave half-angle $\mu(M) = \arcsin(1 / M)$ against Mach number $M \in [1.0, 5.0]$ in Degrees mode (`M {{key:1/x}} {{key:ASIN}}`):
**Curve Features:** Starts at a normal sonic wave $\mu(1.0) = 90.0^\circ$, sweeps sharply through $\mu(2.0) = \mathbf{30.0^\circ}$, and narrows to a slender hypersonic cone $\mu(5.0) = \mathbf{11.537^\circ}$.

***The Supersonic Mach Wave Conical Envelope*** — Map compressible flow shock angle decay from sonic boom to hypersonic flight.

For Mach 2: Inverting Mach number `2 {{key:1/x}}` yields $0.500000$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 0.500000)$. Striking `{{key:ASIN}}` evaluates supersonic shock cone half-angle $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{30.000000}^\circ)$. For Mach 5: Inverting `5 {{key:1/x}}` yields $0.200000$ in $X$ while freezing $30^\circ$ in $Y$ $(T: 0.00, Z: 0.00, Y: 30.000000, X: 0.200000)$. Striking `{{key:ASIN}}` resolves hypersonic cone angle $(T: 0.00, Z: 0.00, Y: 30.000000, X: \mathbf{11.536959}^\circ)$.

---

### Problem 12.29: Thin-Airfoil Aerodynamic Lift Slope ($C_L$ vs. $\alpha$)
Classical thin-airfoil theory predicts section lift coefficient $C_L(\alpha) = 2\pi \alpha$ (for angle of attack $\alpha$ in radians, or $\frac{2\pi^2}{180}\alpha^\circ \approx 0.10966 \alpha^\circ$):
**Curve Features:** Plotting over $\alpha \in [-5^\circ, +15^\circ]$ illustrates the linear inviscid lift regime up to $C_L(10^\circ) \approx \mathbf{1.0966}$ prior to boundary-layer flow separation.

***The Aerodynamic Lift Slope Linear Regime*** — Trace theoretical thin-airfoil lift and identify the pre-stall linear envelope {{cite:hp15c1982}}.

Loading angle of attack `10 {{key:ENTER}}` places $10.0^\circ$ in $Y$ $(T: 0.00, Z: 0.00, Y: 10.000000, X: 10.000000)$. Multiplying by theoretical lift slope `0.10966 {{key:×}}` evaluates inviscid section lift $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{1.096600})$.

---

### Problem 12.30: Van der Waals Real Gas Isotherms
Pressure $P(V) = \frac{R T}{V - b} - \frac{a}{V^2}$:
Isotherms below critical temperature $T_c$ display characteristic van der Waals cubic loops, illustrating liquid-gas phase coexistence.

Multiplying `8.314 {{key:ENTER}} 300 {{key:×}}` evaluates $RT = 2494.20$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.000, X: 2494.20)$. Calculating volume offset `.10 {{key:ENTER}} .04 {{key:-}}` yields $V - b = 0.060000$ in $X$ while lifting $2494.20$ to $Y$ $(T: 0.00, Z: 0.00, Y: 2494.20, X: 0.060000)$. Dividing `{{key:÷}}` gives $41570.00\text{ Pa}$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 41570.00)$. Evaluating attraction term `.36 {{key:ENTER}} .10 {{key:x²}} {{key:÷}}` gives $36.00\text{ Pa}$ in $X$ while freezing $41570.00$ in $Y$ $(T: 0.00, Z: 0.00, Y: 41570.00, X: 36.00)$. Striking `{{key:-}}` yields net real gas pressure $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{41534.00}\text{ Pa})$.

---

> **Thematic Arc IV — Structural Profiles, Visual Root-Bracketing & Quadrature Verification (Problems 12.31–12.38):** The final eight problems use the interactive crosshair cursor to bracket roots for `SOLVE` and bound domains for `∫f`.

### Problem 12.31: Euler-Bernoulli Cantilever Beam Deflection Profile
Under an end point load $P$, the elastic curve of a cantilevered structural beam of length $L$ and flexural rigidity $EI$ follows:
$$y(x) = \frac{P x^2}{6 E I} (3L - x)$$
**Curve Features:** Over $x \in [0, L]$, both deflection $y(0) = 0$ and slope $y'(0) = 0$ vanish at the fixed wall, curving parabolically-cubically to maximum tip deflection $\delta_{\max} = \frac{P L^3}{3 E I}$ at $x = L$.

***The Cantilever Cubic Elastic Deflection Profile*** — Verify zero slope at structural anchor and cubic growth to maximum tip deflection {{cite:horowitz2015}}.

Evaluating geometric factor `4 {{key:ENTER}} 3 {{key:×}} 4 {{key:-}}` yields $3L - x = 8.0\text{ m}$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.000000, X: 8.000000)$. Squaring position and multiplying `4 {{key:x²}} {{key:×}}` forms $x^2(3L - x) = 128.0\text{ m}^3$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 128.000000)$. Scaling by beam compliance `3.0625 {{key:E}} 5 {{key:+/-}} {{key:×}}` resolves maximum tip deflection $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{0.003920}\text{ m} \implies 3.92\text{ mm})$.

---

### Problem 12.32: Elastic Torsion Twist Profile Along a Drive Shaft
For a uniform circular transmission shaft of polar moment $J$ and shear modulus $G$ under torque $T$, the angular twist $\theta(x) = \frac{T x}{J G}$ plots as a straight line through the origin with constant torsional gradient $d\theta/dx = T/(JG)$.

***The Torsional Shear Twist Gradient*** — Trace mechanical drive shaft angular displacement along structural axis.

Entering shaft tip coordinate `2.5 {{key:ENTER}}` places $2.50\text{ m}$ in $Y$ $(T: 0.00, Z: 0.00, Y: 2.500000, X: 2.500000)$. Multiplying by torsional gradient `0.0045 {{key:×}}` evaluates twist $(0.011250\text{ rad})$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 0.011250)$. Converting to degrees `180 {{key:×}} {{key:π}} {{key:÷}}` resolves the shaft tip angular deflection $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{0.644578}^\circ)$.

---

### Problem 12.33: Bivariate Scatter Plot: Hooke's Law Spring Calibration
Accumulating four experimental force-displacement pairs $(1\text{ cm}, 4.8\text{ N})$, $(2\text{ cm}, 10.1\text{ N})$, $(3\text{ cm}, 14.9\text{ N})$, and $(4\text{ cm}, 20.2\text{ N})$ via `{{key:Σ+}}` and selecting `{{key:PLOT}}` (`STAT` overlay) renders the four $2\times 2$ data markers alongside the least-squares regression line of slope $k = \mathbf{5.05\text{ N/cm}}$ ($510\text{ N/m}$) and correlation $r = \mathbf{0.9998}$.

***The Bivariate Hooke's Law Calibration Overlay*** — Fit experimental force-displacement points and superimpose spring constant regression line {{cite:ellenberg2014}}.

Clearing stats `{{key:CLEAR}} {{key:CLΣ}}` initializes registers $(T: 0.00, Z: 0.00, Y: 0.00, X: 0.00)$. Accumulating test weights `4.8 {{key:ENTER}} 1 {{key:Σ+}}`, `10.1 {{key:ENTER}} 2 {{key:Σ+}}`, `14.9 {{key:ENTER}} 3 {{key:Σ+}}`, and `20.2 {{key:ENTER}} 4 {{key:Σ+}}` stages 4 points in memory $(n = 4)$. Striking `{{key:m}}` extracts linear regression slope $(T: 10.10, Z: 14.90, Y: 20.20, X: \mathbf{5.100000}\text{ N/cm})$, verifying Hooke's spring constant $k = 510\text{ N/m}$ with near-perfect correlation $r = 0.9998$.

---

### Problem 12.34: Automotive Kinetic Energy & Braking Distance Parabola
Plotting $E_k(v) = \frac{1}{2} m v^2$ for a $m = 1,200\text{ kg}$ vehicle over speed $v \in [0, 40\text{ m/s}]$ (`V {{key:x²}} 600 {{key:×}}`) visually demonstrates why doubling highway speed from $15\text{ m/s}$ to $30\text{ m/s}$ quadruples kinetic energy from $135\text{ kJ}$ to $\mathbf{540\text{ kJ}}$.

***The Parabolic Kinetic Energy Velocity Scaling*** — Visualize quadratic velocity scaling to highlight braking energy surge at highway speeds {{cite:munroe2014,parker2019}}.

Evaluating kinetic energy at $15\text{ m/s}$: `15 {{key:x²}} 600 {{key:×}}` gives $E_{k,1} = 135,000\text{ J}$ $(135\text{ kJ})$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.000000, X: 135000.00)$. Evaluating kinetic energy at $30\text{ m/s}$: `30 {{key:x²}} 600 {{key:×}}` gives $E_{k,2} = 540,000\text{ J}$ $(540\text{ kJ})$ in $X$ while lifting $E_{k,1}$ to $Y$ $(T: 0.00, Z: 0.000000, Y: 135000.00, X: 540000.00)$. Striking `{{key:x⇄y}} {{key:÷}}` resolves the energy scaling ratio $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{4.000000}\text{x})$, proving that doubling velocity quadruples braking kinetic energy.

---

### Problem 12.35: Relativistic Lorentz Gamma Factor ($\gamma$)
$$\gamma(v) = \frac{1}{\sqrt{1 - (v/c)^2}}$$
Plotted for velocity ratio $\beta = v/c \in [0.0, 0.99]$:
Remains near $1.0$ at low velocities, curves gently to $1.15$ at $\beta = 0.5$, and explodes asymptotically toward infinity as $\beta \to 1.0$.

| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .80 {{key:x²}} | 0.00 | 0.00 | 0.00 | 0.640000 | 0.640000 |
| 02 | 1 {{key:x⇄y}} {{key:-}} | 0.00 | 0.00 | 0.00 | 0.360000 | 0.360000 |
| 03 | {{key:√x}} {{key:1/x}} | 0.00 | 0.00 | 0.00 | 1.666667 | 1.666667 |

---

### Problem 12.36: Linear Thermal Dilatation Calibration Curve
Plotting $\Delta L(T) = \alpha L_0 (T - T_0)$ for an aluminum metrology bar ($\alpha = 23.1 \times 10^{-6}\text{ K}^{-1}$, $L_0 = 1.0\text{ m}$) over $T \in [273\text{ K}, 373\text{ K}]$ provides a direct visual reference line of slope $23.1\,\mu\text{m/K}$ ($2.31\text{ mm}$ total expansion over $100\text{ K}$).

***The Thermal Metrology Dilatation Calibration*** — Sweep temperature to plot linear expansion of precision metrology standards.

Evaluating temperature span `373 {{key:ENTER}} 273 {{key:-}}` yields $\Delta T = 100.0\text{ K}$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.000000, X: 100.000000)$. Multiplying thermal coefficient `23.1 {{key:E}} 6 {{key:+/-}} {{key:×}}` gives thermal elongation $\Delta L = 0.002310\text{ m}$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 0.002310)$. Scaling `1000 {{key:×}}` resolves total bar dilatation $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{2.310000}\text{ mm})$.

---

### Problem 12.37: Stefan-Boltzmann Radiative Heat Emission
Power $P(T) = \varepsilon \sigma A T^4$:
Quartic curve demonstrates why radiative heat transfer dominates at high temperatures ($T > 1000\text{ K}$).

Raising temperature to fourth power `1200 {{key:ENTER}} 4 {{key:yˣ}}` yields $T^4 = 2.0736 \times 10^{12}\text{ K}^4$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 2.0736\text{E}12)$. Multiplying by Stefan-Boltzmann constant `5.67037 {{key:E}} 8 {{key:+/-}} {{key:×}}` gives blackbody surface emission $(117580.8\text{ W/m}^2)$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 117580.8)$. Factoring emissivity and area `.85 {{key:×}} .50 {{key:×}}` resolves net radiated thermal power $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{49971.84}\text{ W} \approx 50.0\text{ kW})$.

---

### Problem 12.38: Newton's Law of Cooling Exponential Asymptote
Plotting $T(t) = T_{\text{env}} + (T_0 - T_{\text{env}}) e^{-k t}$ for a quenched steel billet ($T_0 = 800\text{ K}$, $T_{\text{env}} = 300\text{ K}$, $k = 0.05\text{ s}^{-1}$) over $t \in [0, 100\text{ s}]$ (`T 0.05 {{key:×}} {{key:+/-}} {{key:eˣ}} 500 {{key:×}} 300 {{key:+}}`) illustrates rapid initial heat rejection followed by asymptotic approach to the $300\text{ K}$ ambient floor.

***The Newton Cooling Thermal Transient Asymptote*** — Track quenched metal billet heat rejection to ambient equilibrium {{cite:strogatz2019}}.

Evaluating exponent argument at $t = 20\text{ s}$: `20 {{key:ENTER}} 0.05 {{key:×}} {{key:+/-}}` gives $-kt = -1.000000$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.000000, X: -1.000000)$. Evaluating exponential `{{key:eˣ}}` yields $e^{-1} \approx 0.367879$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 0.367879)$. Scaling initial temperature drop `500 {{key:×}}` gives $183.939721\text{ K}$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 183.939721)$. Adding ambient temperature `300 {{key:+}}` yields the transient billet temperature $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{483.939721}\text{ K})$.

---

## Summary & Looking Ahead

Chapter 12 brought equations to life on the SC-32's transflective graphic LCD. By pairing the RPN mathematical engine with the 64-point vector curve renderer (`{{key:PLOT}}`), you transformed analytical formulas into intuitive visual geometries. You configured domain windows ($X_{\min}, X_{\max}$), scaled vertical dynamic ranges, navigated interactive crosshairs (`{{key:↓}}`, `{{key:↑}}`) to inspect local extrema and inflection points, and pushed graphical coordinates directly onto the operational stack for subsequent numeric analysis.

Visual intuition and analytical keystrokes find their ultimate expression when applied to authentic engineering design problems. In **Chapter 13: Applied STEM Engineering Case Studies**, you will step into the shoes of multidisciplinary field engineers. You will solve comprehensive multi-page challenges spanning fluid dynamics in 3D printer hotends, multi-stage rocket trajectory integration, acoustic reverberation modeling, optical lens cascades via `{{key:x∥y}}`, and closed-loop civil geodetic survey traverses.
