---
title: "Chapter 12: Function & Scatter Plotting Engine | SC-32 Manual"
description: "Master the 64-point vector graphics engine, interactive crosshair curve tracing, window scaling, and regression scatter overlays on the StackCalc SC-32."
---

# Chapter 12: Function & Scatter Plotting Engine

## Seeing the Invisible: Why One 64-Point Curve Reveals What a Thousand Numbers Hide

In 1637, French philosopher and mathematician René Descartes published *La Géométrie* {{cite:descartes1637}}, resolving a schism that had divided mathematics since antiquity. Geometry belonged to continuous space—to lines, circles, and figures drawn with straightedge and compass. Algebra belonged to discrete symbolic manipulation—to polynomial balances and abstract quantities. Descartes demonstrated that these two worlds are isomorphic: every algebraic relation $y = f(x)$ defines a geometric locus in coordinate space, and every geometric curve can be interrogated through its coordinates.

Centuries later, an engineer wrestling with complex systems—an oscillating LC circuit, an aerodynamic shockwave boundary, or the decay envelope of an underdamped suspension—faces the inverse dilemma. A stack of discrete numbers on a handheld calculator, no matter how precise, cannot immediately reveal a high-frequency resonance peak, a hidden vertical asymptote, or a saddle point. To see the dynamics of a physical system, one must see its shape.

The StackCalc SC-32 bridges this gap through its dedicated 64-point vector graphics engine (`{{key:PLOT}}`). By transforming the transflective dot-matrix LCD into a miniature Cartesian laboratory, the instrument evaluates 64 discrete mathematical slices across any domain and renders an interpolated continuous curve in under 42 milliseconds. Paired with interactive crosshair reticle tracing, the engineer can walk along the mathematical terrain, reading exact coordinate pairs from the real-time status bar and committing discovered extrema or inflection points directly back into the RPN operational stack with a single keystroke.

{{screenshot:sc32_plot_polynomial|SC-32 64-Point Vector Function Plotter ({{key:PLOT}}): Cubic Polynomial x³ − 6x² + 11x − 6 with Interactive Crosshair}}
*Figure 12.1: The StackCalc SC-32 rendering an interactive 64-point vector curve (`X^3 - 6*X^2 + 11*X - 6`) with real-time coordinate crosshair telemetry in the Paper print theme.*

---

## The Transflective 64-Point Vector Rendering Engine

While the StackCalc SC-32 is engineered primarily as a rapid tactile numerical instrument, its $132 \times 65$ transflective monochrome dot-matrix display features a dedicated **64-Point Vector Graphics Engine (`{{key:PLOT}}`)**, accessed via Right Shift `{{key:↱}}` on the multi-action `{{key:x∥y}}` key (Row 7, Column 3).

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

> **Reflective Daylight Liquid-Crystal Pixels & Bresenham Stepper Quantization:** Why does the SC-32 display remain razor-sharp in direct midday sunlight where smartphone OLED screens wash out? Each pixel cell in a **transflective** (*transmissive + reflective*) liquid-crystal panel sits above a microscopic semi-mirror: outdoors, ambient sunlight passes through the liquid crystal, bounces off the rear reflector, and returns to your eye with zero battery drain; indoors, a warm edge-lit LED waveguide shines upward through the same liquid-crystal shutter. And when Jack Bresenham invented his 1965 integer line-drawing algorithm at IBM to connect $(u_0, v_0) \to (u_1, v_1)$ on a drum plotter, he solved the exact same discrete quantization problem that governs both our **Counting Tiles** grid (*Figure 12.2*) and every modern CNC mill or 3D printer $X/Y$ stepper carriage: by accumulating the integer decision residual $\epsilon = 2\Delta v - \Delta u$, the hardware knows on every horizontal column step whether to fire a vertical step pulse ($v \leftarrow v \pm 1$), tracing a continuous diagonal line using pure integer addition and subtraction.

### Automatic Domain Scaling, Senary-Binary Root Detection & Tangent Overlays
When a mathematical function is plotted via `{{key:PLOT}}` across the graphing viewport:
1. **Domain Bounds Selection:** Domain bounds $[X_{\min}, X_{\max}]$ are read directly from stack registers $(Y, X)$—defaulting automatically to $[-3.0, +3.0]$ whenever $Y = X$ (or configured via `XMIN` and `XMAX` registers on the hardware viewport).
2. **Discrete Grid Evaluation (From the Counting & Array Studio Socket Grid to 64-Column Vector Sampling):** Just as docking $19.0 \times 19.0\text{ mm}$ tiles from the **Counting & Array Studio** into the discrete Miniblock socket grid on the Snapfinity lid—or aligning polynomial factors along the orthogonal axes of the **Algebra Factoring Studio L-Frame Stage**—quantizes continuous coordinates into discrete physical grid cells, the SC-32's hardware viewport sweeps **64 discrete sample columns** across $[X_{\min}, X_{\max}]$:
   $$x_k = X_{\min} + k \left( \frac{X_{\max} - X_{\min}}{63} \right), \quad k = 0, 1, \dots, 63$$
   For sample column $k = 21$ across the default domain $[-3.0, +3.0]$, this affine grid mapping on the 4-register stack illustrates how each pixel column maps to its exact domain abscissa $x_{21} = -1.000000$:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `3 {{key:ENTER}} 3 {{key:+/-}} {{key:-}}` | 0.000000 | 0.000000 | 0.000000 | 6.000000 | Total domain span $X_{\max} - X_{\min} = 3.0 - (-3.0) = 6.0$ |
| 02 | `63 {{key:÷}}` | 0.000000 | 0.000000 | 0.000000 | 0.095238 | Quantized column step $\Delta x = 6.0 / 63 \approx 0.095238$ |
| 03 | `21 {{key:×}}` | 0.000000 | 0.000000 | 0.000000 | 2.000000 | Horizontal displacement $k \cdot \Delta x = 2.0$ at column $k = 21$ |
| 04 | `3 {{key:+/-}} {{key:+}}` | 0.000000 | 0.000000 | 0.000000 | -1.000000 | Sampled domain coordinate $x_{21} = X_{\min} + 2.0 = -1.000000$ |

3. **Automatic Vertical Range Scaling:** The internal min/max scan determines $Y_{\min} = \min(f(x_k))$ and $Y_{\max} = \max(f(x_k))$, ignoring non-finite singularities (`NaN` / $\pm\infty$). If $Y_{\max} - Y_{\min} < 10^{-12}$ (a flat constant line), the vertical range automatically pads to $[y - 1, y + 1]$.
4. **Automatic Root Marker Detection (6-Segment Senary Search + 30-Step Binary Search):** While generating the curve, the plotter automatically scans for zero crossings ($f(x_{k-1}) \cdot f(x_k) \le 0$). For each sign change, it executes a **5-pass Senary Search** (partitioning the interval into 6 equal sub-segments per pass to isolate the sub-interval containing the sign reversal), followed by a **30-iteration Binary Search** (bisection) to pinpoint the exact root $(x_{\text{root}}, 0)$ and place an interactive root marker directly on the curve.
5. **Central-Difference Tangent & Shaded Quadrature Overlays:** When invoked alongside numerical differentiation or Romberg integration (`{{key:∫}}`), the plotter superimposes the exact tangent line $y = f(x_0) + f'(x_0)(x - x_0)$ computed via central difference ($h = 10^{-5}$) or shades the Riemann area columns between $f(x)$ and $y = 0$. When no active equation is selected and at least two statistical data pairs reside in the **50-point scatter ring buffer**, `{{key:PLOT}}` automatically renders a bivariate scatter plot with the least-squares linear regression line $y = mx + b$ superimposed across the data range.
6. **Sub-Frame Latency:** Total plot generation and Bresenham rasterization completes in under **$42\text{ milliseconds}$**.

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

In Plot Mode, the physical keypad dynamically reconfigures into an intuitive navigation controller:

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

### From Visual Curve Inspection to Stack Coordinate Commitment
Plotting a function on the transflective LCD immediately exposes its qualitative behavior—root crossings, asymptotic singularities, local extrema, and Gibbs ringing overshoots—before any numerical solver is invoked. Look at *Figure 12.2*: when you dock $19.0 \times 19.0\text{ mm}$ tiles from the **Counting & Array Studio** into the $3 \times 8$ discrete socket grid on the Snapfinity lid, a continuous diagonal line must step from socket column to socket column by integer grid increments $(\Delta u, \Delta v)$. That physical socket-grid quantization is the exact tactile model of the SC-32's $128 \times 52$ pixel framebuffer and Jack Bresenham's (1965) integer line-drawing algorithm: the plotter evaluates $y = f(x_k)$ at 64 discrete horizontal columns, maps each $(x_k, y_k)$ sample to its nearest integer pixel socket $(u_k, v_k)$, and connects adjacent sockets with 1-pixel staircase steps. Stepping the interactive crosshair reticle along the rasterized curve with `{{key:↓}}` and `{{key:↑}}` displays each sampled $(x, y)$ coordinate pair in real time (just like reading the simultaneous $(\cos\theta, \sin\theta)$ sight-windows of the **Unit Circle Trigonometry Volvelle**). Pressing `{{key:ENTER}}` commits that exact coordinate pair directly into the operational stack ($Y = x, X = y$) so you can launch `{{key:SOLVE}}` or `{{key:∫}}` without retyping a single digit.

{{blocks:counting_tiles_array_3x8|Discrete Grid Sampling and Pixel Quantization Array}}
*Figure 12.2: Discrete grid sampling array: docking $19.0\text{ mm}$ Counting Tiles into discrete grid columns illustrates how mathematical domain intervals map to quantized display pixels before hardware-accelerated Bresenham line interpolation.*

---

### Blind Solver Guesses vs. Visual Viewport Bracketing (`{{key:PLOT}}` $\to$ `{{key:SOLVE}}`)

Coupling the 128×64 viewport reticle directly to Registers $Y$ and $X$ eliminates the disconnected graph-screen menus and manual bound re-entry required on conventional algebraic graphing calculators:

| Challenge / Metric | Conventional Algebraic Calculator (Infix) | Algebraic Strokes | SC-32 RPN Stack Method | SC-32 Strokes | Stack Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **Fourier Series**: Square Wave ($\sin t + \frac{1}{3}\sin 3t + \frac{1}{5}\sin 5t$) | Rigid formula line `Y1 = sin(X) + (1/3)*sin(3*X) + (1/5)*sin(5*X)`. Missing a parenthesis halts with `SYNTAX ERROR`. Repeated point re-evaluations re-parse token tree. | 42 | **Hardware Stack Vector Sampling**: Postfix expression `T SIN T 3 * SIN 3 / + T 5 * SIN 5 / +` evaluates directly on registers. Deterministic sweep in $<42\text{ ms}$; zero parenthesis stack overhead. | 22 | **48% fewer strokes + zero parenthesis syntax errors** |
| **Extrema & Zero Inspection**: Root Bracketing | Graph function, navigate `CALC` $\to$ `zero`, enter Left Bound, Right Bound, Guess via arrow keys. Numerical root is stranded on graph screen; must exit to home screen and re-type coordinate for subsequent integration. | 38 | **Interactive Reticle Stack Commitment**: Trace crosshair with `{{key:↓}}/{{key:↑}}` to visual zero/extrema; tap `{{key:ENTER}}` to commit exact $(x, y)$ coordinates into Registers $Y$ and $X$. Directly invoke `{{key:SOLVE}}` with zero re-entry. | 14 | **63% fewer strokes + direct stack-to-solver pipeline** |
| **Domain Window Sweep**: Dynamic Range Scaling | Open `WINDOW` menu, manually adjust `Xmin`, `Xmax`, `Xscl`, `Ymin`, `Ymax`, `Yscl`. If $Y$ bounds are mismatched, curve clips off-screen; user must execute trial-and-error `ZoomFit`. | 32 | **Stack-Direct Bounds & Hardware Auto-Scale**: Push domain bounds to stack ($Y = X_{\min}, X = X_{\max}$) or store into `XMIN`/`XMAX`; engine automatically calculates $[Y_{\min}, Y_{\max}]$ and auto-scales vertical viewport in $<42\text{ ms}$. | 12 | **62% fewer strokes + automatic optimal vertical scaling** |
| **Scatter Data & Curve Fit**: Regression Overlay | Navigate `STAT` $\to$ `EDIT`, manually populate `L1` and `L2` column tables. Exit to `STAT PLOT`, enable `Plot1`. Navigate `STAT` $\to$ `CALC` $\to$ `LinReg`, paste `L1, L2, Y1`. Prone to dimension mismatch errors. | 46 | **Live Statistical Accumulation (`{{key:Σ+}}`)**: Stream raw $(x, y)$ pairs onto stack and press `{{key:Σ+}}`. Instant correlation $r$ and $R^2$ via `{{key:x²}}`; superimpose linear, exponential, logarithmic, or power regressions directly over scatter dots. | 18 | **61% fewer strokes + zero list-dimension mismatch** |

---

## Window Bounds & Viewport Configuration

You can set the horizontal plotting window $[X_{\min}, X_{\max}]$ in two ways: either push the domain limits directly onto the stack ($Y = X_{\min},\; X = X_{\max}$, which defaults to $[-3.0, +3.0]$ whenever $Y = X$) and press `{{key:PLOT}}`, or store persistent bounds into the named window registers (`XMIN`, `XMAX`, `YMIN`, `YMAX`, `XSCL`, `YSCL`):

| Parameter | Register / Stack | Default Value | Description |
|:---|:---|:---|:---|
| Xmin | Register $Y$ / `XMIN` | `-3.0` (Stack) / `-10.0` (Reg) | Leftmost domain boundary |
| Xmax | Register $X$ / `XMAX` | `+3.0` (Stack) / `+10.0` (Reg) | Rightmost domain boundary |
| Ymin | `YMIN` | (Auto-scaled) | Lower range boundary |
| Ymax | `YMAX` | (Auto-scaled) | Upper range boundary |
| Xscl | `XSCL` | 1.00000000000 | Tick mark spacing along X-axis |
| Yscl | `YSCL` | 1.00000000000 | Tick mark spacing along Y-axis |

For example, to sweep an equation from $-10$ to $+10$ on the fly, simply key `10 {{key:+/-}} {{key:ENTER}} 10 {{key:PLOT}}` (or store `10 {{key:+/-}} {{key:STO}} "XMIN"` and `10 {{key:STO}} "XMAX"` before pressing `{{key:PLOT}}`).

---

## Advanced Statistical Regression Curve Overlays

When performing bivariate data analysis in `{{key:SUMS}}` mode, the SC-32 can superimpose four distinct mathematical curve models directly over your empirical scatter points:

| Model | Formula | Transformation Protocol |
|:---|:---|:---|
| Linear | $y = m x + b$ | Native coordinates: $(x, y)$ |
| Logarithmic | $y = a \ln(x) + b$ | Semi-logarithmic: $(\ln x, y)$ |
| Exponential | $y = a e^{b x}$ | Semi-logarithmic: $(x, \ln y)$ |
| Power | $y = a x^b$ | Log-Log: $(\ln x, \ln y)$ |

### Goodness-of-Fit & Coefficient of Determination ($R^2$)
The correlation coefficient $r$ provided by `{{key:ŷ}}` quantifies the linear association between the transformed coordinates, and squaring $r$ on the stack (`{{key:x²}}`) yields the **Coefficient of Determination ($R^2$)**:

$$R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}} = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$

For the pressure sensor calibration dataset analyzed below ($r = 0.999565$), pressing `{{key:x²}}` immediately gives $R^2 = 0.999130$, confirming that $99.91\%$ of the output voltage variance is explained by applied pressure while the scatter plot lets you inspect the individual residuals visually.

---

## Visual Crosshair Bracketing (`PLOT`) & Analytical Refinement (`SOLVE` & `∫`)

Why pair a 64-column graphical plotter with a 12-digit numerical root solver and integrator? Because human visual intuition and high-precision numerical algorithms have complementary blind spots!

A blind numerical root search (`{{key:SOLVE}}`) or definite integral (`{{key:∫}}`) on an unfamiliar nonlinear function can easily miss a second root, get trapped near a local extremum, or integrate right across a hidden vertical asymptote. Conversely, a 64-column pixel plot (`{{key:PLOT}}`) reveals the global shape of a function in under $42\text{ ms}$, but its horizontal cursor step is quantized to $\Delta x = (X_{\max} - X_{\min})/63$. On the SC-32, you combine both strengths into a seamless two-stage pipeline:
1. **Visual Crosshair Reconnaissance (`{{key:PLOT}}`):** Plot the active `{{key:EQN}}` over $[X_{\min}, X_{\max}]$. The plotter's automatic **6-segment senary + 30-step binary root detector** places visual markers on every zero crossing, while stepping the crosshair reticle with `{{key:↓}}` and `{{key:↑}}` lets you inspect peaks, troughs, and inflection points on the bottom status line.
2. **Direct Stack Handoff to `{{key:SOLVE}}` & `{{key:∫}}` via `{{key:ENTER}}`:** When the crosshair rests near a root or interval bound of interest, pressing `{{key:ENTER}}` exits `{{key:PLOT}}` and pushes the active crosshair coordinates directly onto the operational stack: Register $Y$ receives the horizontal coordinate $x$, and Register $X$ receives the vertical evaluated coordinate $y$. From there, you can immediately invoke Brent's solver (`{{key:SOLVE}}`) or Adaptive Romberg Quadrature (`{{key:∫}}`) to refine that visual reading to full **12-digit analytical precision** without re-typing a single coordinate!

Keep three practical habits in mind when plotting functions: first, make sure the lower domain bound is strictly less than the upper bound ($X_{\min} < X_{\max}$, otherwise `Error 01: INVALID DATA` is reported when `XMIN` $\ge$ `XMAX`); second, check that your angular mode (`{{key:RAD}}` vs. `{{key:DEG}}`) matches your domain bounds when plotting trigonometric waveforms (plotting $\sin x$ over $[-3.14, +3.14]$ while accidentally in Degrees mode will trace only a tiny $6.28^\circ$ ramp near the origin!); and third, whenever an equation hits a pole or undefined domain point (such as $1/0$ or $\ln(-1)$) at one of the 64 sample columns, the Bresenham renderer automatically lifts its virtual pen across the singularity rather than drawing a false vertical line connecting $-\infty$ to $+\infty$.

---

## Visual Reconnaissance and Analytical Refinement Across Engineering Curves

On a conventional algebraic graphing calculator, defining a multi-term Fourier series or transfer function requires typing a deeply nested string of infix parentheses into a small formula editor, where a single mismatched bracket halts the plot with a `SYNTAX ERROR`. On the StackCalc SC-32, equations are evaluated directly on the four hardware stack registers ($X, Y, Z, T$) in under 42 milliseconds {{cite:hp32sii1991}}, and pressing `{{key:ENTER}}` while tracing hands the live $(x, y)$ crosshair coordinates straight back to the stack for 12-digit verification, root-finding (`{{key:SOLVE}}`), or integration (`{{key:∫}}`) {{cite:brent1973,romberg1955}}.

---

### Harmonic Waveforms, Damped Transients & Cartesian Function Plotting

We open by rendering Joseph Fourier's harmonic square-wave synthesis, an underdamped automotive shock-absorber transient, and a Fraunhofer single-slit optical diffraction pattern on the $128 \times 52$ pixel canvas.

#### Square Wave Synthesis via Fourier Harmonics
When Jean-Baptiste Joseph Fourier claimed in 1807 that *any* periodic waveform—even a flat-topped square wave with vertical jumps—could be constructed by adding together smooth sinusoidal waves, his contemporaries Lagrange and Laplace were incredulous. Yet as we stack odd harmonics of decreasing amplitude ($\sin t + \frac{1}{3}\sin 3t + \frac{1}{5}\sin 5t + \dots$), the fundamental $\sin t$ provides the main humps, the third harmonic $\frac{1}{3}\sin(3t)$ carves out the center peak to flatten the plateau, and the fifth harmonic $\frac{1}{5}\sin(5t)$ sharpens the corners while leaving a characteristic ripple across the top. Let's synthesize and plot the three-harmonic square wave across $t \in [-180.0^\circ, +180.0^\circ]$ in Degrees mode (`{{key:DEG}}`):

$$y(t) = \sin(t) + \frac{1}{3}\sin(3t) + \frac{1}{5}\sin(5t)$$

In `{{key:EQN}}` mode, store the postfix expression `T {{key:SIN}} T 3 {{key:×}} {{key:SIN}} 3 {{key:÷}} {{key:+}} T 5 {{key:×}} {{key:SIN}} 5 {{key:÷}} {{key:+}}` under label `FOURIER`, set the domain bounds via `180 {{key:+/-}} {{key:STO}} "XMIN"` and `180 {{key:STO}} "XMAX"`, and press `{{key:PLOT}}`:

| Plot Telemetry | Crosshair Readout | Curve Feature |
| :--- | :--- | :--- |
| **Active Function** | `SIN(X) + SIN(3*X)/3` | Fundamental + odd harmonic square-wave synthesis |
| **Crosshair Cursor** | `X = 90.000000000`, `Y = 0.8666666667` | Central saddle trough between twin local maxima |

Stepping the crosshair with `{{key:↓}}` and `{{key:↑}}` to the center of the positive plateau at $t = 90.0^\circ$ reveals a slight central dimple flanked by two higher Gibbs-overshoot shoulders:
$$y(90^\circ) = \sin(90^\circ) + \frac{1}{3}\sin(270^\circ) + \frac{1}{5}\sin(450^\circ) = 1.0 - 0.333333 + 0.200000 = \mathbf{0.866667}$$
The status bar reads `X: 90.000000000    Y: 0.8666666667`. We can verify that exact harmonic sum at $t = 90^\circ$ on the RPN stack via {{res:sc32_12_plot_01:keys}} $\implies \mathbf{{{res:sc32_12_plot_01:value}}}$:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `90 {{key:SIN}}` | 0.00 | 0.00 | 0.00 | 1.000000 | Fundamental harmonic $\sin(90^\circ) = 1.000000$ |
| 02 | `90 {{key:ENTER}} 3 {{key:×}} {{key:SIN}}` | 0.00 | 0.00 | 1.000000 | -1.000000 | Third harmonic phase $\sin(270^\circ) = -1.000000$; fundamental lifts to Y |
| 03 | `3 {{key:÷}}` | 0.00 | 0.00 | 1.000000 | -0.333333 | Scale third harmonic amplitude $-\frac{1}{3} = -0.333333$ |
| 04 | `{{key:+}}` | 0.00 | 0.00 | 0.00 | 0.666667 | Partial sum of 1st + 3rd harmonics ($0.666667$) |
| 05 | `90 {{key:ENTER}} 5 {{key:×}} {{key:SIN}}` | 0.00 | 0.00 | 0.666667 | 1.000000 | Fifth harmonic phase $\sin(450^\circ) = 1.000000$; partial sum lifts to Y |
| 06 | `5 {{key:÷}}` | 0.00 | 0.00 | 0.666667 | 0.200000 | Scale fifth harmonic amplitude $+\frac{1}{5} = 0.200000$ |
| 07 | `{{key:+}}` | 0.00 | 0.00 | 0.00 | 0.866667 | Three-harmonic square wave trough ordinate $y(90^\circ) = 0.866667$ |

#### Damped Harmonic Oscillator Transient Ringing
When a car tire strikes a speed bump and drops back onto level pavement at $t = 0$, the suspension coil spring tries to bounce the chassis up and down at its damped natural frequency $\omega_d$, while the hydraulic shock absorber dissipates kinetic energy into heat, wrapping the oscillation inside an exponential decay envelope $e^{-\zeta \omega_n t}$:

$$x(t) = e^{-\zeta \omega_n t} \cos(\omega_d t)$$
For an underdamped sports suspension with damping ratio $\zeta = 0.15$, natural frequency $\omega_n = 4.0\text{ rad/s}$ ($\zeta \omega_n = 0.60\text{ s}^{-1}$), and damped frequency $\omega_d = \omega_n\sqrt{1 - \zeta^2} = 3.9546\text{ rad/s}$:
$$x(t) = e^{-0.60 t} \cos(3.9546 t)$$

In Radians mode (`{{key:RAD}}`), enter `T 0.60 {{key:×}} {{key:+/-}} {{key:eˣ}} T 3.9546 {{key:×}} {{key:COS}} {{key:×}}` in `{{key:EQN}}`, set the domain via `0 {{key:STO}} "XMIN"` and `6 {{key:STO}} "XMAX"`, and press `{{key:PLOT}}`:

| Plot Telemetry | Crosshair Readout | Curve Feature |
| :--- | :--- | :--- |
| **Active Function** | `EXP(-0.6*T)*COS(3.9546*T)` | Underdamped second-order exponential ringdown envelope |
| **Crosshair Cursor** | `X = 0.000000000`, `Y = 1.0000000000` | Initial peak displacement at $t = 0$ |

One second after hitting the bump ($t = 1.0\text{ s}$ in `RAD`), the shock absorber has bled the amplitude envelope down to $e^{-0.60} \approx 54.9\%$ while the phase $\omega_d t = 3.9546\text{ rad}$ ($226.6^\circ$) places the suspension near the bottom of its first rebound trough ({{res:sc32_12_plot_02:keys}} $\implies \mathbf{{{res:sc32_12_plot_02:value}}}$):

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `1 {{key:ENTER}} .60 {{key:×}}` | 0.00 | 0.00 | 0.00 | 0.600000 | Damping exponent $\zeta \omega_n t = 0.600000$ at $t = 1.0\text{ s}$ |
| 02 | `{{key:+/-}} {{key:eˣ}}` | 0.00 | 0.00 | 0.00 | 0.548812 | Exponential decay envelope $e^{-0.60} = 0.548812$ |
| 03 | `1 {{key:ENTER}}` | 0.00 | 0.548812 | 1.000000 | 1.000000 | Stage time $t = 1.0\text{ s}$ for oscillatory phase; envelope lifts to Z |
| 04 | `3.9546 {{key:×}}` | 0.00 | 0.00 | 0.548812 | 3.954600 | Damped phase angle $\omega_d t = 3.954600\text{ rad}$; envelope drops to Y |
| 05 | `{{key:COS}}` | 0.00 | 0.00 | 0.548812 | -0.687229 | Cosine carrier $\cos(3.9546\text{ rad}) = -0.687229$ |
| 06 | `{{key:×}}` | 0.00 | 0.00 | 0.00 | -0.377160 | Instantaneous suspension displacement $x(1.0) = -0.377160\text{ m}$ |

#### Sinc Function Diffraction Pattern
Shine a coherent laser beam through a narrow rectangular slit onto a dark wall, or transmit a rectangular digital voltage pulse across a band-limited radio channel, and the resulting wave amplitude profile is governed by the same universal curve—the **sinc function**, which is the Fourier transform of a rectangular window:

$$y(x) = \frac{\sin x}{x}$$
Plotting $y(x) = \frac{\sin x}{x}$ over $x \in [-4\pi, +4\pi]$ (`-12.57 {{key:STO}} "XMIN"`, `12.57 {{key:STO}} "XMAX"`) in Radians mode (`{{key:RAD}}`) reveals the tall central diffraction bright fringe at $x = 0$ ($\lim_{x \to 0} \frac{\sin x}{x} = 1.00$) flanked by alternating positive and negative side lobes that cross zero at every non-zero integer multiple of $\pi$ ($\pm\pi, \pm 2\pi, \pm 3\pi, \pm 4\pi$). At the half-lobe point $x = \pi/2$, keying {{res:sc32_12_plot_07:keys}} yields $\mathbf{{{res:sc32_12_plot_07:value}}}$.

Notice how `{{key:LASTX}}` streamlines evaluating $\operatorname{sinc}(x) = \frac{\sin x}{x}$ at any angle: forming the half-lobe argument `{{key:RAD}} {{key:π}} 2 {{key:÷}}` ($\pi/2 \approx 1.570796\text{ rad}$) and pressing `{{key:SIN}}` evaluates $\sin(\pi/2) = 1.000000$ in Register $X$ while automatically archiving the radian argument $\pi/2$ in `LASTX`. Chaining `{{key:LASTX}} {{key:÷}}` recalls $\pi/2$ into $X$, lifts $1.000000$ into $Y$, and divides to yield the exact half-lobe amplitude $2/\pi$ ($X = \mathbf{0.636620}$, or $-3.92\text{ dB}$) without re-computing $\pi/2$.

---

### Singularities, Bifurcations & Bivariate Scatter Overlays

Next we inspect how the plotter handles rational poles, biochemical saturation plateaus, empirical `{{key:Σ+}}` calibration scatter plots, and quadrature phase circles.

#### Rational Function with Pole & Vertical Asymptote
In optics and control theory, rational functions of the form $f(x) = \frac{1}{x - x_0}$ appear whenever a physical denominator passes through zero—such as thin-lens magnification $M = \frac{f}{f - d_o}$ as an object crosses the focal point $d_o = f$. Let's examine $f(x) = \frac{1}{x - 2}$ over $x \in [0, 4]$:

Because $f(x)$ diverges to $-\infty$ as $x \to 2^-$ and plunges from $+\infty$ as $x \to 2^+$, naive plotting software often connects the two branches with a vertical line straight through $x = 2.0$. The SC-32's singularity guard detects the pole and renders the lower-left and upper-right hyperbolic branches cleanly separated. Sampling the upper branch at $x = 2.5$ (`2.5 {{key:ENTER}} 2 {{key:-}}` $\rightarrow 0.500000$, followed by `{{key:1/x}}`) confirms the ordinate ($X = \mathbf{2.000000}$).

#### Michaelis-Menten Hyperbolic Enzyme Kinetics
In Chapter 9, we linearized enzyme kinetics by taking reciprocals $(1/[S], 1/v)$ for a Lineweaver-Burk regression. With `{{key:PLOT}}`, we can inspect Leonor Michaelis and Maud Menten's untransformed hyperbolic saturation curve directly over $[S] \in [0, 100\text{ mM}]$ for an enzyme with maximum turnover velocity $V_{\max} = 100.0\text{ }\mu\text{mol/min}$ and Michaelis constant $K_m = 15.0\text{ mM}$:

$$v = \frac{V_{\max} [S]}{K_m + [S]}$$
The plotted curve rises steeply near the origin ($v \approx \frac{V_{\max}}{K_m}[S]$ when active sites are mostly empty) and bends smoothly toward the horizontal asymptote $V_{\max} = 100$ as substrate floods the enzyme. Stepping the crosshair to $[S] = K_m = 15.0\text{ mM}$ visually confirms that $K_m$ is the exact substrate concentration where reaction velocity reaches half-maximum ($v = V_{\max}/2 = 50.0\text{ }\mu\text{mol/min}$). On the stack, evaluating the numerator `100 {{key:ENTER}} 15 {{key:×}}` forms $V_{\max}[S] = 1500.00$ in Register $X$ while saving $[S] = 15.0$ in `LASTX`; chaining `{{key:LASTX}} 2 {{key:×}} {{key:÷}}` forms the denominator $15 + 15 = 30.00$ and divides to yield $X = \mathbf{50.000000}$ with `15` typed only once.

#### Bivariate Statistical Scatter Plot: Sensor Calibration
Whenever you calibrate a laboratory sensor via `{{key:Σ+}}` (as in Chapter 9's thermistor and pressure calibration models), glancing at the correlation coefficient $r$ alone is never enough—you also want to *see* the data points against the fitted line to verify that no single point is an outlier or a nonlinear bend. Let's load four piezoresistive pressure sensor calibration pairs—$(10\text{ kPa}, 1.25\text{ V}), (20\text{ kPa}, 2.45\text{ V}), (30\text{ kPa}, 3.80\text{ V}), (40\text{ kPa}, 4.95\text{ V})$—by clearing statistics (`{{key:CLEAR}} {{key:CLΣ}}`), entering `1.25 {{key:ENTER}} 10 {{key:Σ+}}`, `2.45 {{key:ENTER}} 20 {{key:Σ+}}`, `3.80 {{key:ENTER}} 30 {{key:Σ+}}`, `4.95 {{key:ENTER}} 40 {{key:Σ+}}`, and pressing `{{key:PLOT}}` (`STAT`):

| Scatter Telemetry | Statistical Readout | Interpretation |
| :--- | :--- | :--- |
| **Sample Count** | `n = 4` | Four bivariate `(x, y)` calibration pairs accumulated via `{{key:Σ+}}` |
| **Linear Fit** | `m = 0.124500`, `r = 0.999565` | Least-squares trendline overlay with near-unity linearity |

The LCD renders the four $2\times 2$ pixel dot markers—just like docking four **Counting Tiles** at discrete $(x_i, y_i)$ coordinates on the grid—and superimposes the least-squares linear regression trendline $y = 0.1245x + 0.0000$ directly through the cloud:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `{{key:CLEAR}} {{key:CLΣ}}` | 0.00 | 0.00 | 0.00 | 0.00 | Clear statistical accumulators |
| 02 | `1.25 {{key:ENTER}} 10 {{key:Σ+}}` | 0.00 | 0.00 | 1.25 | 1.00 | Pair 1: (10 kPa, 1.25 V); count n = 1 |
| 03 | `2.45 {{key:ENTER}} 20 {{key:Σ+}}` | 0.00 | 1.25 | 2.45 | 2.00 | Pair 2: (20 kPa, 2.45 V); count n = 2 |
| 04 | `3.80 {{key:ENTER}} 30 {{key:Σ+}}` | 1.25 | 2.45 | 3.80 | 3.00 | Pair 3: (30 kPa, 3.80 V); count n = 3 |
| 05 | `4.95 {{key:ENTER}} 40 {{key:Σ+}}` | 2.45 | 3.80 | 4.95 | 4.00 | Pair 4: (40 kPa, 4.95 V); count n = 4 |
| 06 | `{{key:m}}` | 2.45 | 3.80 | 4.95 | 0.1245 | Regression slope m = 0.124500 V/kPa |

#### Lissajous Figure 1:1 Phase Trajectory
In 1857, French physicist Jules Antoine Lissajous bounced a narrow beam of light off mirrors attached to two tuning forks vibrating at right angles, projecting glowing geometric loops onto a lecture-hall screen. Today, electrical engineers perform the same test in oscilloscope $X\text{–}Y$ mode to compare the frequency and phase of two AC signals. When two equal-frequency sinusoids have an exact $90^\circ$ ($\pi/2\text{ rad}$) quadrature phase shift:

$$x(t) = \cos(t), \quad y(t) = \sin(t)$$
the parametric trajectory $(x(t), y(t))$ traces the unit circle $x^2 + y^2 = 1$—the exact electronic counterpart of rotating the **Unit Circle Volvelle** through phase angle $t$ while reading its orthogonal $\cos t$ and $\sin t$ sight-windows simultaneously. In `{{key:RAD}}` mode, evaluating `{{key:π}} 4 {{key:÷}} {{key:ENTER}}` ($t = \pi/4 \approx 0.785398$), pressing `{{key:COS}}` to form $x = \cos(\pi/4) \approx 0.707107$ in $X$ while $t$ waits in $Y$, and executing `{{key:x⇄y}} {{key:SIN}}` resolves $y = \sin(\pi/4)$ in $X$ alongside $x$ in $Y$ ($Y = 0.707107,\; X = \mathbf{0.707107}$)—or without `{{key:ENTER}}` via `{{key:π}} 4 {{key:÷}} {{key:COS}} {{key:LASTX}} {{key:SIN}}`.

---

### Polar Radiation Patterns & Cubic Inflection Geometry

Exploring directional antenna radiation lobes and polynomial concavity transitions.

#### Four-Petal Quadrupole Polar Rose
When RF engineers arrange four antenna elements into a phased quadrupole array—or when an acoustic transducer vibrates in a quadrupole mode—constructive interference beams energy along the four $45^\circ$ diagonal bisectors ($\theta = 45^\circ, 135^\circ, 225^\circ, 315^\circ$), while destructive phase cancellation creates dead-silent nodal lines along the cardinal axes ($\theta = 0^\circ, 90^\circ, 180^\circ, 270^\circ$). Over $\theta \in [0^\circ, 360^\circ]$, the polar radiation gain follows the four-petal rose:

$$r(\theta) = 3 \sin(2\theta)$$

At the first-quadrant diagonal bisector $\theta = 45^\circ$, doubling the azimuth `45 {{key:ENTER}} 2 {{key:×}}` ($2\theta = 90.0^\circ$), taking `{{key:SIN}}` ($\sin 90^\circ = 1.000000$), and scaling by `3 {{key:×}}` (`45 {{key:ENTER}} 2 {{key:×}} {{key:SIN}} 3 {{key:×}}` $\implies \mathbf{3.0000}$) confirms the peak main-lobe gain ($X = \mathbf{3.000000}$) at the tip of the petal.

#### Third-Degree Polynomial Inflection & Concavity Transition
Imagine driving along a highway S-curve modeled by the cubic polynomial over $x \in [0, 4]$:

$$y(x) = x^3 - 6x^2 + 9x + 2$$

The first derivative $y'(x) = 3x^2 - 12x + 9 = 3(x-1)(x-3)$ vanishes at the local hill crest $(1, 6)$ and the valley trough $(3, 2)$. Right in the middle, where the second derivative $y''(x) = 6x - 12 = 0$ vanishes at $x = 2$, lies the **inflection point** $(2, 4)$—the exact point along the S-curve where the road transitions from curving downward (concave-down, $y'' < 0$) to curving upward (concave-up, $y'' > 0$) and your steering wheel passes through dead center.

At the inflection abscissa $x = 2$, writing $y(x)$ in nested Horner form $y(x) = ((x - 6)x + 9)x + 2$ and pre-filling the 4-level stack via `2 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}} 6 {{key:-}} {{key:×}} 9 {{key:+}} {{key:×}} 2 {{key:+}}` evaluates the inflection ordinate ($X = \mathbf{4.000000}$) with `2` typed only once as Register $T$ replicates $x = 2.0$ down the stack on every multiplication:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `2 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}` | 2.000000 | 2.000000 | 2.000000 | 2.000000 | Flood all four stack registers with inflection abscissa $x = 2.0$ |
| 02 | `6 {{key:-}}` | 2.000000 | 2.000000 | 2.000000 | -4.000000 | Innermost Horner factor $x - 6 = -4.0$; Register $T$ replicates $2.0$ |
| 03 | `{{key:×}} 9 {{key:+}}` | 2.000000 | 2.000000 | 2.000000 | 1.000000 | Second Horner stage $(x - 6)x + 9 = 1.0$; $x = 2.0$ drops into $Y$ |
| 04 | `{{key:×}} 2 {{key:+}}` | 2.000000 | 2.000000 | 2.000000 | 4.000000 | Inflection point ordinate $y(2) = ((x - 6)x + 9)x + 2 = 4.000000$ |

---

### Structural Deflection & Torsion Profiles

We conclude by contrasting the cubic-parabolic bending curve of a cantilevered beam against the linear torsional windup of a transmission drive shaft.

#### Euler-Bernoulli Cantilever Beam Deflection Profile
Picture a structural steel balcony I-beam—or an aircraft wing spar—clamped rigidly into a concrete wall at $x = 0$ and supporting a concentrated point load $P$ at its free tip $x = L = 4.0\text{ m}$. Because the wall prevents the root from either sinking ($y(0) = 0$) or tilting ($y'(0) = 0$), integrating the Euler-Bernoulli bending-moment equation $EI y''(x) = P(L - x)$ twice produces the classic cubic-parabolic elastic curve:

$$y(x) = \frac{P x^2}{6 E I} (3L - x)$$

Over $x \in [0, L]$, the beam emerges horizontally from the wall, curves downward with increasing slope as the $x^2$ factor grows, and reaches its maximum tip deflection $\delta_{\max} = \frac{P L^3}{3 E I}$ at $x = L$. Given a flexural rigidity factor $\frac{P}{6EI} = 3.0625 \times 10^{-5}\text{ m}^{-2}$ on a $L = 4.0\text{ m}$ span, evaluating the span factor at the tip (`4 {{key:ENTER}} 3 {{key:×}} 4 {{key:-}}` $\rightarrow 3L - x = 8.0\text{ m}$), multiplying by $x^2$ (`4 {{key:x²}} {{key:×}}` $\rightarrow 128.0\text{ m}^3$), and scaling by `3.0625 {{key:E}} 5 {{key:+/-}} {{key:×}}` yields the exact tip deflection ($X = \mathbf{0.003920}\text{ m} = 3.92\text{ mm}$).
*(**`LASTX` Single-Entry Tip Evaluation:** Keying `3 {{key:ENTER}} 4 {{key:×}} {{key:LASTX}} {{key:-}} {{key:LASTX}} {{key:x²}} {{key:×}} 3.0625 {{key:E}} 5 {{key:+/-}} {{key:×}}` uses `{{key:LASTX}}` twice in succession to recover $x = 4.0\text{ m}$—first after `4 {{key:×}}` and again after `{{key:-}}`—so `4` is typed only once.)*

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `3 {{key:ENTER}} 4 {{key:×}}` | 0.000000 | 0.000000 | 0.000000 | 12.000000 | Compute $3L = 12.0\text{ m}$; tip coordinate $x = 4.0\text{ m}$ archived in `LASTX` |
| 02 | `{{key:LASTX}} {{key:-}}` | 0.000000 | 0.000000 | 0.000000 | 8.000000 | Recall $x = 4.0\text{ m}$ and subtract for span factor $3L - x = 8.0\text{ m}$ |
| 03 | `{{key:LASTX}} {{key:x²}} {{key:×}}` | 0.000000 | 0.000000 | 0.000000 | 128.000000 | Recall $x = 4.0\text{ m}$ again, square to $16.0\text{ m}^2$, and form $x^2(3L - x) = 128.0\text{ m}^3$ |
| 04 | `3.0625 {{key:E}} 5 {{key:+/-}} {{key:×}}` | 0.000000 | 0.000000 | 0.000000 | 0.003920 | Scale by $\frac{P}{6EI} = 3.0625 \times 10^{-5}\text{ m}^{-2}$; tip deflection $\delta_{\max} = 0.003920\text{ m}$ |

#### Elastic Torsion Twist Profile Along a Drive Shaft
Unlike a cantilevered beam whose bending moment varies along its length, a uniform circular drive shaft of polar moment $J$ and shear modulus $G$ transmitting torque $T$ from an engine gearbox ($x = 0$) to a rear differential ($x = 2.50\text{ m}$) experiences the *exact same* internal torque $T$ at every cross-section. Under Saint-Venant pure torsion, the angular twist $\theta(x) = \frac{T x}{J G}$ therefore plots as a straight line through the origin with constant torsional gradient $d\theta/dx = T/(JG) = 0.0045\text{ rad/m}$. Staging the shaft length `2.5 {{key:ENTER}}` ($2.50\text{ m}$), multiplying by the specific twist rate (`0.0045 {{key:×}}` $\rightarrow 0.011250\text{ rad}$), and converting radians to degrees (`180 {{key:×}} {{key:π}} {{key:÷}}`) resolves the total angular windup at the output flange ($X = \mathbf{0.644578}^\circ$).

---

## Further Exploration: Companion Workbooks & Applied Tie-Ins

> *For 27 additional worked engineering problems with full 4-register stack traces, see Chapter 12 of the [SC-32 Scientific Companion Problem & Casebook Workbook](../../curriculum/sc32-scientific-companion-workbook.md#chapter-12).*


To connect the 64-point vector graphics engine (`{{key:PLOT}}`), senary-binary root markers, and `{{key:Σ+}}` scatter overlays with laboratory instrumentation and competition problem sets, explore these companion workbooks:

- **StackCalc Engineering Laboratory Casebook (Module 5: Bode Plots, Filter Synthesis & Transducer Calibration):** Pairs `{{key:PLOT}}` crosshair tracing with `{{key:SOLVE}}` and `{{key:∫}}` to locate $-3\text{ dB}$ passband corners, measure total harmonic distortion (THD) across Fourier partial sums, and audit sensor calibration residuals.
- **Timed STEM Competition & Physics Workbook (Section G: Curve Sketching, Extrema & Parametric Kinematics):** Trains students to bracket polynomial roots visually on the $128 \times 52$ viewport, commit crosshair coordinates to the stack with `{{key:ENTER}}`, and evaluate rational/trigonometric waveforms without re-typing arguments.

### Synthesis Challenge Problems

1. **Single-Entry Michaelis-Menten Velocity at Arbitrary Substrate Concentration:** For an enzyme with $V_{\max} = 100.0\text{ }\mu\text{mol/min}$ and $K_m = 15.0\text{ mM}$, evaluate the reaction velocity $v = \frac{V_{\max}[S]}{K_m + [S]}$ at $[S] = 45.0\text{ mM}$ while typing `45` only once: key `100 {{key:ENTER}} 45 {{key:×}} {{key:LASTX}} 15 {{key:+}} {{key:÷}}` to confirm that `{{key:LASTX}}` recalls $[S] = 45.0$ into the denominator and yields $v = \mathbf{75.000000\text{ }\mu\text{mol/min}}$ ($\frac{3}{4}V_{\max}$ at $[S] = 3K_m$).
2. **Zero-Register RC High-Pass Gain & Phase Angle in One Pass:** At $f = 2000\text{ Hz}$ for a high-pass RC filter with $f_c = 1000\text{ Hz}$, the normalized frequency ratio is $f/f_c = 2.0$. In `{{key:DEG}}` mode, keying `1 {{key:ENTER}} 2000 {{key:ENTER}} 1000 {{key:÷}} {{key:▸θ,r}} {{key:LASTX}} {{key:x⇄y}} {{key:÷}}` uses `{{key:▸θ,r}}` (`y = 1, x = 2`) to place phase lead $\phi = 90^\circ - \arctan(2) = \mathbf{26.565051^\circ}$ in Register $Y$ and $\sqrt{1 + (f/f_c)^2} = \sqrt{5}$ in Register $X$, while `{{key:LASTX}}` recalls $f/f_c = 2.0$ to divide out the passband gain $|H(f)| = \mathbf{0.894427}$ in Register $X$ without using a single storage register.
3. **Single-Entry Euler-Bernoulli Deflection at Midspan ($x = L/2$):** For the Euler-Bernoulli cantilevered beam above ($L = 4.0\text{ m}$, $\frac{P}{6EI} = 3.0625 \times 10^{-5}\text{ m}^{-2}$), evaluate deflection $y(x) = \frac{P}{6EI}(3L - x)x^2$ at midspan $x = 2.0\text{ m}$ by typing `2` only once: key `12 {{key:ENTER}} 2 {{key:-}} {{key:LASTX}} {{key:x²}} {{key:×}} 3.0625 {{key:E}} 5 {{key:+/-}} {{key:×}}` to confirm $y(2.0\text{ m}) = \mathbf{0.001225\text{ m}}$ ($1.225\text{ mm}$, exactly $\frac{5}{16}$ of the tip deflection $\delta_{\max} = 3.92\text{ mm}$).

---

## Summary & Looking Ahead

Pairing the RPN mathematical engine with the 64-point vector curve renderer (`{{key:PLOT}}`) projects analytical formulas onto the $128 \times 52$ transflective viewport. Configuring domain windows ($X_{\min}, X_{\max}$), scaling vertical dynamic ranges, stepping the interactive crosshair (`{{key:↓}}`, `{{key:↑}}`) across local extrema and inflection points, and committing traced coordinates to the stack via `{{key:ENTER}}` bridges visual reconnaissance and 12-digit numerical refinement.

Visual intuition and analytical keystrokes find their ultimate expression when applied to authentic engineering design problems. In **[Chapter 13: Applied STEM Engineering Case Studies](13-applied-stem-case-studies.md)**, you will step into the shoes of multidisciplinary field engineers. You will solve comprehensive multi-page challenges spanning fluid dynamics in 3D printer hotends, multi-stage rocket trajectory integration, acoustic reverberation modeling, optical lens cascades via `{{key:x∥y}}`, and closed-loop civil geodetic survey traverses.
