---
title: "Chapter 12: Cartesian Coordinates, Pixel Rasterization & Visual Analysis | Thinking in the Stack (SC-32)"
description: "From René Descartes's coordinate plane, Jack Bresenham's line algorithm, and Francis Anscombe's Quartet to vector function graphing and interactive viewport navigation on the StackCalc SC-32."
---

# Chapter 12: Cartesian Coordinates, Pixel Rasterization & Visual Analysis

## René Descartes's Coordinate Plane and the Geometry of Functions

### Algebraic Equations as Geometric Loci

During his years as a boarding student at the College of La Flèche in Anjou, René Descartes was granted an unusual privilege by the rector, Father Charlet: while his classmates rose at five o'clock every morning to recite Latin prayers in unheated stone halls, young René was allowed to remain warm under his blankets until late morning, thinking quietly with his eyes open.

Descartes kept that habit of morning meditation for the rest of his life. Observing the orthogonal grid of ceiling tiles and wall joints in his room—and investigating Pappus of Alexandria's classical locus problem—Descartes considered how to specify the exact position of a moving point on a flat plane at any instant, and how to describe the path it traced.

He realized that if he measured the perpendicular distance $x$ from a horizontal reference axis and the perpendicular distance $y$ from a second reference axis, every position on the plane corresponded to a unique pair of numbers $(x, y)$. If the point moved along a straight diagonal line or a smooth circular arc, its two distances $x$ and $y$ obeyed a strict algebraic equation; conversely, *any* algebraic equation connecting $x$ and $y$ traced a visible geometric curve across the plane.

When Descartes published this discovery in 1637 as *La Géométrie* {{cite:descartes1637}}, an appendix to his *Discourse on the Method*, he ended a two-thousand-year separation that had divided mathematical thought since antiquity. Ancient Greek geometry, as practiced by Euclid, Archimedes, and Apollonius, was rich in visual intuition with circles, triangles, parabolas, and tangent lines drawn by straightedge and compass, yet it possessed almost no symbolic algebra, so proving a new theorem required inventing a custom geometric construction from scratch. Conversely, medieval and Renaissance algebra, developed by al-Khwarizmi, Tartaglia, Cardano, and Viète, provided a symbolic calculus for balancing unknowns ($x^2, x^3$), yet an equation sat on the page as a dry string of characters with no visual shape.

Descartes proved that algebra and geometry are two languages describing one underlying reality. John Stuart Mill later called analytic geometry *"the greatest single step ever made in the progress of the exact sciences,"* because it gave equations eyes and gave geometric shapes formulas.

### Reading the Anatomy of a Curve: Roots, Peaks, Valleys & Inflection Points

Once an algebraic formula $y = f(x)$ is translated into a Cartesian curve across a horizontal $x$-axis (domain) and a vertical $y$-axis (range), defined on the SC-32 via the `{{key:EQN}}` editor, every analytical feature from Algebra II, Precalculus, and introductory calculus corresponds to a distinct geometric contour along the curve.

Hunting for the roots or zeros of a polynomial or transcendental equation means searching for values of $x$ where $f(x) = 0$. On a Cartesian graph, a root is a shoreline where the terrain crosses sea level ($y = 0$) and switches from negative elevation ($y < 0$, underwater) to positive elevation ($y > 0$, dry land). Along a smooth curve, the first derivative $f'(x)$ measures the instantaneous slope: as an observer climbs a hill, the slope is positive ($f'(x) > 0$), and on the descent down the far side, the slope is negative ($f'(x) < 0$). At the exact summit of a smooth hill (*local maximum*) or the bottom of a smooth valley (*local minimum*), the tangent line is momentarily flat and horizontal ($f'(x) = 0$).

An *inflection point* marks a reversal in the sign of curvature along a smooth trajectory, such as an S-shaped highway transition modeled by a general cubic polynomial:

$$y(x) = a x^3 + b x^2 + c x + d, \qquad y''(x) = 6ax + 2b$$

Wherever the second derivative is negative ($y''(x) < 0$), the tangent slope decreases with $x$ and the curve bends downward (*concave down*); wherever the second derivative is positive ($y''(x) > 0$), the tangent slope increases with $x$ and the curve bends upward (*concave up*). At the unique abscissa $x_{\text{infl}} = -\frac{b}{3a}$ where $y''(x_{\text{infl}}) = 0$, the curvature passes through zero as the trajectory reverses its direction of bend, which forms the exact geometric point of symmetry between the cubic's local peak and local valley.

Vertical and horizontal asymptotes bound the extreme behavior of rational and exponential functions. When a rational denominator approaches zero, such as the thin-lens magnification formula $f(x) = \frac{1}{x - 2}$ as an object crosses the focal point $x = 2$, the curve diverges toward $-\infty$ on the left and plunges from $+\infty$ on the right along a *vertical asymptote*. Conversely, when a skydiver falls under gravity $g$ and quadratic air drag ($v(t) = v_{\text{term}}\tanh(gt/v_{\text{term}})$), or when an uncharged capacitor charges through a resistor toward a supply voltage $V_{\max}$ with RC time constant $\tau$:

$$V(t) = V_{\max}\!\left(1 - e^{-t/\tau}\right)$$

upward air resistance or capacitor back-voltage gradually balances the driving force, and the curve approaches a flat horizontal ceiling—a *horizontal asymptote* at $v = v_{\text{term}}$ or $V = V_{\max}$ as $t \to \infty$.

---

## Rasterization on a Pocket Canvas: Turning Equations into Pixels

### The Paradox of Digital Graphics: Continuous Math on a Discrete Grid

Descartes imagined his coordinate plane as infinitely smooth: between any two points on a line, there are infinitely many closer points. A digital screen, however, is discrete. Inspect any monochrome liquid-crystal display through a magnifying glass, and you will see a chessboard of tiny rectangular liquid-crystal shutters—pixels, short for *picture elements*. Those shutters are arranged in $N_x$ horizontal columns $u = 0, 1, \dots, N_x - 1$ and $N_y$ vertical rows $v = 0, 1, \dots, N_y - 1$. At any instant, each cell is switched either ON as dark ink or OFF as reflective paper background.

Bridging continuous analysis and discrete display hardware requires translating a smooth mathematical equation $y = f(x)$ into a crisp ribbon of integer pixels in less than a twentieth of a second across three inside-out stages.

### Slicing a Continuous Domain into $N_x$ Discrete Columns

To plot a function $y = f(x)$ across a horizontal world window from $X_{\min}$ on the left to $X_{\max}$ on the right (a total horizontal span of $\Delta X = X_{\max} - X_{\min}$), a digital rasterizer slices the continuous interval into discrete sample columns separated by a uniform step width $\Delta x = \frac{X_{\max} - X_{\min}}{N_x - 1}$:

$$x_k = X_{\min} + k \left(\frac{X_{\max} - X_{\min}}{N_x - 1}\right), \qquad k = 0, 1, \dots, N_x - 1$$

Each column index $k$ advances the world abscissa linearly from $x_0 = X_{\min}$ at the left border to $x_{N_x - 1} = X_{\max}$ at the right border. By the Nyquist-Shannon sampling theorem, uniform column spacing $\Delta x$ can faithfully resolve spatial angular frequencies up to the Nyquist limit $\omega_{\max} = \frac{\pi}{\Delta x}$ (at least two pixel samples per oscillation period). Whenever a high-frequency waveform such as $\sin(\omega x)$ oscillates with period $T = \frac{2\pi}{\omega} < 2\Delta x$, multiple cycles fold inside a single column step and beat against the pixel grid at a lower alias frequency $\omega_{\text{alias}} = |\omega - 2\pi m / \Delta x|$. Halving the domain span $\Delta X$ via binary zoom-in cuts $\Delta x$ in half and restores true phase resolution across the oscillatory carrier.

### Affine Viewport Mapping and Inverted Screen Coordinates

As the rasterizer evaluates $y_k = f(x_k)$ at each sampled abscissa, it tracks the lowest value $Y_{\min} = \min(y_k)$ and the highest value $Y_{\max} = \max(y_k)$, skipping any sample where the function hits an undefined division by zero (`NaN` or $\pm\infty$) so a single vertical asymptote does not crush the rest of the curve into a flat line.

A fundamental coordinate inversion arises between analytic geometry and digital display memory: in Descartes's mathematics, $+y$ points upward, whereas in computer memory, pixel row numbers $v$ count downward from the top-left corner of the screen. This convention dates to 1930s cathode-ray television tubes (`CRT`s), which swept their electron beams from left to right and from top to bottom across the phosphor glass; when the first digital framebuffers were wired in the 1960s, engineers numbered video memory rows in the exact top-to-bottom order the scanbeam painted the screen ($v = 0$ at the top ceiling down to $v = N_y - 1$ at the bottom floor). Mapping a continuous world point $(x, y)$ onto an integer screen pixel $(u, v)$ across an $N_x \times N_y$ viewport therefore requires a two-step Affine Viewport Transformation:

$$u = \left\lfloor \frac{x - X_{\min}}{X_{\max} - X_{\min}} \times (N_x - 1) \right\rfloor, \qquad v = (N_y - 1) - \left\lfloor \frac{y - Y_{\min}}{Y_{\max} - Y_{\min}} \times (N_y - 1) \right\rfloor$$

Both formulas evaluate from the inside out in two stages. First, normalization onto $[0, 1]$ subtracts the minimum bound ($x - X_{\min}$ or $y - Y_{\min}$) and divides by the total window span ($X_{\max} - X_{\min}$ or $Y_{\max} - Y_{\min}$), mapping any dimensional domain onto a dimensionless fraction between $0.0$ and $1.0$. Second, scaling and vertical inversion multiply the horizontal fraction by $N_x - 1$ columns to obtain $u$, while multiplying the vertical fraction by $N_y - 1$ rows and subtracting from $N_y - 1$ places the highest mathematical peak $y = Y_{\max}$ at the top row $v = 0$ and the lowest valley $y = Y_{\min}$ at the bottom row $v = N_y - 1$.

### Jack Bresenham's 1962 Integer Line-Drawing Algorithm

Illuminating only the isolated sample dots $(u_k, v_k)$ on the screen leaves a steep curve, such as a high-frequency sine wave or a cubic polynomial, looking like a scattered constellation of disconnected dots with wide vertical gaps between columns. Rendering a continuous curve requires connecting each pair of adjacent pixel coordinates $(u_0, v_0)$ and $(u_1, v_1)$ with a gap-free straight line segment on a square grid.

In 1962, IBM engineer Jack Elton Bresenham, working at the San Jose computation laboratory, developed a line-drawing routine for a CalComp mechanical drum plotter attached to an IBM 1401 computer. Because the machine lacked floating-point hardware and fast division instructions, computing a floating-point slope $m = \frac{\Delta v}{\Delta u}$ and rounding decimals at every pixel step was prohibitively slow.

Bresenham framed the geometry from the inside out. Take a segment that moves $\Delta u = u_1 - u_0$ pixels to the right and rises $\Delta v = |v_1 - v_0|$ pixels vertically, assuming $\Delta v \le \Delta u$ (or swapping $u$ and $v$ whenever a steep segment rises faster than it runs). Each horizontal step $u \leftarrow u + 1$ causes the true mathematical line to rise by the fraction $\frac{\Delta v}{\Delta u}$ of a pixel. At each column, the hardware makes a binary decision between staying on the current pixel row $v$ and stepping one pixel row vertically to $v \pm 1$.

Instead of dividing $\Delta v$ by $\Delta u$ and comparing the fraction against $\frac{1}{2}$ ($0.5$), Bresenham multiplied the entire inequality by $2\Delta u$ to clear the fraction completely. That produced an integer error accumulator:

$$\epsilon_0 = 2\Delta v - \Delta u$$

On each horizontal pixel step, if $\epsilon < 0$, the line has not yet crossed the halfway mark, so the rasterizer stays on the same row $v$ and adds $2\Delta v$ to $\epsilon$. Conversely, if $\epsilon \ge 0$, the line has crossed the halfway mark, so the rasterizer steps one pixel vertically ($v \leftarrow v \pm 1$) and adds $2(\Delta v - \Delta u)$ to $\epsilon$. Using only integer addition, subtraction, and a bit-shift by $2$ without fractions, floating-point decimals, or divisions, Bresenham's Line Algorithm became a foundational routine of computer graphics, implemented in silicon across graphics processors, laser printers, CNC milling controllers, and the SC-32's 42-millisecond vector plotting engine {{cite:hp32sii1991}}.

---

## Anscombe's Quartet, Visual Root Bracketing & Harmonic Waveforms

### Francis Anscombe's 1973 Quartet: Four Datasets with Identical Summary Statistics

Carl Friedrich Gauss's method of least squares distills a cloud of $(x_i, y_i)$ measurements into four clean summary numbers: the sample means $(\bar{x}, \bar{y})$, the sample standard deviations $(s_x, s_y)$, the linear regression line $\hat{y} = m x + b$, and Karl Pearson's correlation coefficient $r$. By the early 1970s, as mainframe computers automated least-squares regression, many scientists and economists stopped graphing their data and inspected only the printed values of $m, b,$ and $r$.

In 1973, British statistician Francis John Anscombe, founder of Yale University's Department of Statistics, published a four-page paper in *The American Statistician* titled *"Graphs in Statistical Analysis"* demonstrating the necessity of visual inspection in regression analysis. To show that summary statistics without a visual plot can be deceptive, Anscombe constructed four small datasets (Anscombe's Quartet), each consisting of $n = 11$ coordinate pairs $(x_i, y_i)$.

If you feed all four datasets into a statistical calculator and read only the summary numbers, they look 100% identical:

| Statistical Metric | Dataset I | Dataset II | Dataset III | Dataset IV |
| :--- | :---: | :---: | :---: | :---: |
| **Sample Size ($n$)** | $11$ | $11$ | $11$ | $11$ |
| **Mean of $x$ ($\bar{x}$) & Variance ($s_x^2$)** | $\bar{x} = 9.0,\; s_x^2 = 11.0$ | $\bar{x} = 9.0,\; s_x^2 = 11.0$ | $\bar{x} = 9.0,\; s_x^2 = 11.0$ | $\bar{x} = 9.0,\; s_x^2 = 11.0$ |
| **Mean of $y$ ($\bar{y}$) & Variance ($s_y^2$)** | $\bar{y} = 7.50,\; s_y^2 = 4.125$ | $\bar{y} = 7.50,\; s_y^2 = 4.125$ | $\bar{y} = 7.50,\; s_y^2 = 4.125$ | $\bar{y} = 7.50,\; s_y^2 = 4.125$ |
| **Least-Squares Line ($\hat{y} = m x + b$)** | $\hat{y} = 0.500x + 3.00$ | $\hat{y} = 0.500x + 3.00$ | $\hat{y} = 0.500x + 3.00$ | $\hat{y} = 0.500x + 3.00$ |
| **Correlation ($r$) & Determination ($R^2$)** | $r = 0.816,\; R^2 = 0.667$ | $r = 0.816,\; R^2 = 0.667$ | $r = 0.816,\; R^2 = 0.667$ | $r = 0.816,\; R^2 = 0.667$ |

An analyst looking only at $m = 0.500$, $b = 3.00$, and $r = 0.816$ would conclude that all four experiments show an identical, moderately strong linear trend. Yet the moment you press `{{key:PLOT}}` after accumulating your data pairs with `{{key:Σ+}}`, the SC-32 renders a bivariate scatter plot with the least-squares trendline $\hat{y} = 0.500x + 3.00$ overlaid, and four distinct structural patterns appear in less than a second.

Dataset I is a true linear cloud of eleven noisy data points scattered naturally around a genuine straight line, the only dataset where a linear model fits the underlying physics. Dataset II is a smooth, noiseless quadratic parabola that rises to a peak and curves back down, where a linear fit is the wrong mathematical model. Dataset III consists of ten points lying on a straight line of slope $0.346$, plus one corrupted sensor reading at $(13, 12.74)$ that pulls the least-squares slope up to $0.500$ and distorts the correlation. Dataset IV stacks ten points vertically at $x = 8.0$ with zero relationship between $x$ and $y$, plus one isolated leverage point far to the right at $(19, 12.50)$ that single-handedly fabricates a spurious correlation of $r = 0.816$.

Anscombe's Quartet demonstrates why a scientist or engineer should never trust a correlation coefficient in isolation: pairing `{{key:Σ+}}` statistical accumulation with `{{key:PLOT}}` verifies immediately whether experimental data follows a straight line, an exponential curve, or a power law, or contains a single rogue outlier.

### Visual Root Bracketing & Harmonic Waveforms: Where Vision Guides Precision

Plotting is equally valuable when paired with numerical root-finding (`{{key:SOLVE}}`) and integration (`{{key:∫}}`) {{cite:brent1973,romberg1955}}, combining visual inspection with 12-digit numerical refinement. When you plot a wave or polynomial across the 128-column viewport, global visual reconnaissance shows at a glance how many roots cross the axis, where local peaks and valleys sit, and whether a vertical asymptote lies inside the interval, preventing the error of asking a root solver to search an interval that contains no root or jumps across infinity. Conversely, because a pixel screen has finite horizontal column resolution, Richard Brent's solver and Werner Romberg's integrator then refine any bracketed point or area to full 12-digit local precision.

You can pan and bisect the plotted viewport with the six binary-search navigation softkeys (`<`, `|<-`, `OUT`, `IN`, `->|`, `>`). Tapping `{{key:PLOT}}` a second time then lets you drop root markers via `MARK`, push bracket bounds onto the stack via `STORE` for `{{key:SOLVE}}`, or shade definite integrals via `∫ f(x)`, uniting global visual reconnaissance with 12-digit analytical precision across four classic waveforms.

When French mathematician Jean-Baptiste Joseph Fourier announced in 1807 that a flat-topped *square wave* with discontinuous vertical jumps could be synthesized by summing smooth sine waves of odd harmonic frequencies:

$$y_K(t) = \sum_{m=1}^{K} \frac{\sin((2m - 1)t)}{2m - 1} = \sin(t) + \frac{1}{3}\sin(3t) + \frac{1}{5}\sin(5t) + \cdots$$

Lagrange and Laplace rejected the claim on the grounds that smooth sinusoids could never reproduce a sharp corner. Plotting the partial sums reveals how odd harmonics constructively square off the waveform: at the midpoint of the positive plateau ($t = \pi/2$), successive odd harmonics alternate in sign ($+1 - \frac{1}{3} + \frac{1}{5} - \cdots$, converging to Gregory and Leibniz's $\frac{\pi}{4}$), which flattens the central crest while compressing the transition slope at $t = 0$ and $t = \pi$ and producing Henry Wilbraham's (1848) and J. Willard Gibbs's (1899) universal $8.95\%$ overshoot horns beside each jump discontinuity.

In mechanical vibration analysis, when an underdamped suspension encounters a step impulse at $t = 0$, the elastic restoring element oscillates at $\cos(\omega_d t)$ while viscous damping wraps the motion inside an exponential decay envelope $e^{-\zeta\omega_n t}$:

$$x(t) = e^{-\zeta\omega_n t}\cos(\omega_d t)$$

Plotting this damped harmonic ringdown reveals both the oscillation period and the rate at which successive rebound troughs decay. In physical optics, when coherent light passes through a narrow slit, interference produces the diffraction pattern $y(x) = \frac{\sin x}{x}$, with a central principal maximum $\lim_{x \to 0}\frac{\sin x}{x} = 1$ and alternating side lobes that cross zero at every non-zero multiple of $\pi$. Finally, the relational test menus `{{key:x?y}}` and `{{key:x?0}}` evaluate inside `{{key:EQN}}` to Kenneth Iverson's Boolean indicator $1.0$ (True) or $0.0$ (False). Combining a smooth curve with the three-keystroke Macaulay ramp idiom (`{{key:ENTER}} {{key:x>0}} {{key:×}}`) plots and traces half-wave rectifiers and neural-network ReLU units $y = x[x > 0]$, Zener voltage clippers $v_{\text{out}}(x) = x - \langle x - V_Z \rangle_+$, or multi-branch piecewise engineering laws across the entire 128-column canvas of `{{key:PLOT}}` without switching equations.

---

## Function Graphing, Reticle Tracing & Scatter Plots

A horizontal plotting window $[X_{\min}, X_{\max}]$—like a Cartesian point $(x, y)$ on Descartes's ceiling—occupies two adjacent stack registers: Register `Y` holds the lower domain bound $X_{\min}$, and Register `X` holds the upper domain bound $X_{\max}$. Instead of burying window bounds inside a modal setup form, `{{key:PLOT}}` reads $[X_{\min}, X_{\max}]$ straight from Registers `Y` and `X` and autoscales the vertical range automatically. Conversely, when you frame a zero crossing or drop two markers $[x_1, x_2]$ on the canvas and tap `{{key:PLOT}}` $\to$ `STORE` (`{{key:LFU2}}`), the plotter writes those coordinates back into Registers `Y` and `X` for 12-digit root refinement via `{{key:SOLVE}}` or Romberg integration via `{{key:∫}}`.

Every graphing session follows a direct stack-to-viewport cycle. First, define an analytical expression $f(X)$ in `{{key:EQN}}`, or accumulate $(y_k, x_k)$ sample pairs via `{{key:Σ+}}` in `{{key:SUMS}}` mode when plotting experimental scatter data with regression overlays. Second, stage the left domain bound $X_{\min}$ in Register `Y` and the right domain bound $X_{\max}$ in Register `X` via `Xmin {{key:ENTER}} Xmax`. Third, press `{{key:PLOT}}` (Right Shift `{{key:↱}}` above `{{key:x∥y}}`) to rasterize the curve, navigate with the binary-search zoom and pan softkeys, and tap `{{key:PLOT}}` a second time to mark roots, push brackets back to the stack via `STORE`, or shade definite integrals via `∫ f(x)`.

{{res:sc32_plot_polynomial:screenshot|The StackCalc SC-32 rendering an interactive vector curve (X³ − 6X² + 11X − 6) via {{key:PLOT}} with real-time coordinate crosshair telemetry.}}

### Viewport Geometry, Affine Column Mapping & Crosshair Controls

Inside the SC-32's $132 \times 65$ transflective monochrome dot-matrix display, the Vector Graphics Engine (`{{key:PLOT}}`) is accessed via Right Shift `{{key:↱}}` above `{{key:x∥y}}` (Row 7, Column 3) {{cite:hp32sii1991}}. It dedicates a $128 \times 52\text{ pixel}$ active plotting viewport ($N_x = 128$ columns $u \in [0, 127]$ and $N_y = 52$ rows $v \in [0, 51]$) right above the 13-pixel coordinate telemetry bar. During each sweep, firmware samples 100 horizontal steps and maps each point via $u = \lfloor \frac{x - X_{\min}}{X_{\max} - X_{\min}} \times 127 \rfloor$ and $v = 51 - \lfloor \frac{y - Y_{\min}}{Y_{\max} - Y_{\min}} \times 51 \rfloor$.

Because each arithmetic step in the affine column-to-coordinate mapping $x_k = X_{\min} + k\frac{X_{\max} - X_{\min}}{N - 1}$ transforms a single scalar in place—from total span to column step to horizontal displacement to world abscissa—the entire calculation executes inside Register $X$ while Registers $Y$, $Z$, and $T$ remain at zero.

Across a $64\text{-column}$ ($N - 1 = 63$) benchmark spanning the default domain $[-3.0, +3.0]$ at sample column $k = 21$ (one-third of the way across the screen from the left border, or analogously across the $[-10.0, +10.0]$ `EXEC` domain), keying `3 {{key:ENTER}} 3 {{key:+/-}} {{key:-}}` computes the total horizontal span $X_{\max} - X_{\min} = 6.000000$ in Register $X$. Dividing by `63 {{key:÷}}` quantizes the per-column step $\Delta x = 6.0 / 63 \approx 0.095238$, scaling by `21 {{key:×}}` advances $k \cdot \Delta x = 2.000000$ units rightward from the left edge, and adding the left boundary via `3 {{key:+/-}} {{key:+}}` lands at the exact world coordinate $x_{21} = -1.000000$ displayed by the crosshair telemetry bar.

Four subsystem stages coordinate domain sampling, root detection, and softkey navigation inside `{{key:PLOT}}`:

1. **Stack-Driven Horizontal Domain $[X_{\min}, X_{\max}]$ & Automatic Vertical Autoscaling:** To plot any equation stored in `{{key:EQN}}`, push the lower bound $X_{\min}$ into Register $Y$ and the upper bound $X_{\max}$ into Register $X$ via `Xmin {{key:ENTER}} Xmax`. Press `{{key:PLOT}}`, select the equation softkey (`{{key:LFU0}}`–`{{key:LFU5}}`), and tap the independent variable softkey or `EXEC` (if $Y = X$, the domain defaults to $[-3.0, +3.0]$, or $[-10.0, +10.0]$ via `EXEC`). As the engine sweeps 100 horizontal sample steps across the 128-column viewport, it automatically autoscales the vertical range $[Y_{\min}, Y_{\max}]$ with a $10\%$ top/bottom margin, printing `[minY, maxY]` at the top-right of the LCD and `centerX` at the top-left.
2. **Automatic Senary Root-Marker Detection:** During every plot sweep, the engine partitions $[X_{\min}, X_{\max}]$ into 6 senary sub-intervals, detects sign changes $f(x_k)\cdot f(x_{k+1}) < 0$, refines each zero crossing via 30-step binary bisection to $10^{-10}$, and draws vertical root markers on the curve.
3. **The 6 Primary Plot Navigation Softkeys (`{{key:LFU0}}`–`{{key:LFU5}}`):** While a graph is displayed, the six top softkeys form a binary-search zoom and pan toolbar:
   * **`{{key:LFU0}}` (`<`):** Pan Left by $25\%$ of the current domain width.
   * **`{{key:LFU1}}` (`|<-`):** Bisect Left Half—zooms the domain to the left half $[X_{\min}, X_{\text{center}}]$.
   * **`{{key:LFU2}}` (`OUT`, or `{{key:<-}}` Backspace):** Zoom Out $2\times$ around `centerX`.
   * **`{{key:LFU3}}` (`IN`):** Zoom In $2\times$ ($0.5\times$ width) around `centerX`.
   * **`{{key:LFU4}}` (`->|`):** Bisect Right Half—zooms the domain to the right half $[X_{\text{center}}, X_{\max}]$.
   * **`{{key:LFU5}}` (`>`):** Pan Right by $25\%$ of the current domain width.
4. **The Second-Tap `{{key:PLOT}}` Action Toolbar (`MARK`, `CLEAR`, `STORE`, `∫ f(x)`):** Pressing `{{key:PLOT}}` a second time while viewing a graph toggles the 4-action softkey menu:
   * **`{{key:LFU0}}` (`MARK`):** Drops a vertical marker at the current center crosshair `centerX`.
   * **`{{key:LFU1}}` (`CLEAR`):** Clears active plot markers.
   * **`{{key:LFU2}}` (`STORE`):** Pushes the two most recent plot markers $[x_1, x_2]$ (or $(y, x)$ at the center crosshair) onto Registers $Y$ and $X$ of the live RPN stack—giving you a visual bracket for `{{key:SOLVE}}`.
   * **`{{key:LFU3}}` (`∫ f(x)`):** Executes Romberg quadrature (`{{key:∫}}`) between the active markers (or across $[X_{\min}, X_{\max}]$) and shades the area under the curve.
   * **Exit to Stack (`{{key:C}}`):** Pressing `{{key:C}}` exits `{{key:PLOT}}` back to the live stack.

This bidirectional register transfer turns root-finding into a closed visual-analytical loop across four steps:
1. **Frame the Search Domain:** Push the initial window $[X_{\min}, X_{\max}]$ onto Registers $Y$ and $X$ (`Xmin {{key:ENTER}} Xmax`) and press `{{key:PLOT}}` to inspect all sign-change markers across the viewport.
2. **Isolate the Zero Crossing:** Use the binary-search navigation softkeys (`|<-`, `->|`, `IN`, `<`, `>`) to frame the target root, or drop two markers straddling the axis crossing via second-tap `{{key:PLOT}}` $\to$ `MARK` (`{{key:LFU0}}`).
3. **Transfer the Bracket & Solve:** Tap `{{key:PLOT}}` $\to$ `STORE` (`{{key:LFU2}}`) to push the bracket $[x_1, x_2]$ into Registers $Y$ and $X$, exit via `{{key:C}}`, and press `{{key:SOLVE}}` to refine the root to 12 digits without risking divergence on nearby extrema or asymptotes.

### Tracing Cubic Inflections, Fourier Square Waves, Damped Ringdown & `sinc` Lobes

Take the cubic highway S-curve $y(x) = x^3 - 6x^2 + 9x + 2$ plotted over $x \in [0, 4]$ via `0 {{key:ENTER}} 4 {{key:PLOT}}`: its local maximum rises to $(1, 6)$, its local minimum dips to $(3, 2)$, and its inflection point ($y''(x) = 6x - 12 = 0$) sits midway between them at $x = 2$. Writing $y(x)$ in nested Horner form $y(x) = ((x - 6)x + 9)x + 2$ and pre-filling the 4-level stack evaluates the inflection ordinate ($X = 4.000000$) with `2` typed only once:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `2 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}` | 2.000000 | 2.000000 | 2.000000 | 2.000000 | Flood all four stack registers with inflection abscissa $x = 2.0$ |
| `6 {{key:-}}` | 2.000000 | 2.000000 | 2.000000 | -4.000000 | Innermost Horner factor $x - 6 = -4.0$; Register $T$ replicates $2.0$ |
| `{{key:×}} 9 {{key:+}}` | 2.000000 | 2.000000 | 2.000000 | 1.000000 | Second Horner stage $(x - 6)x + 9 = 1.0$; $x = 2.0$ drops into $Y$ |
| `{{key:×}} 2 {{key:+}}` | 2.000000 | 2.000000 | 2.000000 | 4.000000 | Inflection point ordinate $y(2) = ((x - 6)x + 9)x + 2 = 4.000000$ |

To synthesize and plot Joseph Fourier's three-harmonic square wave $y(t) = \sin(t) + \frac{1}{3}\sin(3t) + \frac{1}{5}\sin(5t)$ across $t \in [-180.0^\circ, +180.0^\circ]$ in Degrees mode (`{{key:DEG}}`), store the three-harmonic sum in `{{key:EQN}}` (where the angle variable `T` is entered via `{{key:RCL}} T`) and launch the domain from the stack via `180 {{key:+/-}} {{key:ENTER}} 180 {{key:PLOT}}`. On the $128 \times 52\text{-pixel}$ viewport, you immediately see how Fourier's odd harmonics flatten the central crest while carving twin Gibbs-phenomenon ears—the $9\%$ overshoot horns that rise beside each vertical jump discontinuity.

Evaluating the center of that plateau at $t = 90.0^\circ$ on the stack via `{{res:sc32_12_plot_01:keys}}` needs only Registers $Y$ and $X$ while $Z$ and $T$ stay at zero: the fundamental crest $\sin(90^\circ) = +1.000000$ sits in Register $Y$ while the inverted third-harmonic trough $\frac{1}{3}\sin(270^\circ) = -0.333333$ forms in Register $X$ and folds down to $0.666667$, after which adding the fifth-harmonic peak $+\frac{1}{5}\sin(450^\circ) = +0.200000$ lifts the plateau center back to `{{res:sc32_12_plot_01:value}}`.

When an underdamped sports suspension $x(t) = e^{-0.60 t} \cos(3.9546 t)$ ($\zeta = 0.15, \omega_n = 4.0\text{ rad/s}, \omega_d = 3.9546\text{ rad/s}$) is plotted over $t \in [0, 6\text{ s}]$ in Radians mode (`{{key:RAD}}`), the trace shows the cosine oscillation decaying inside its exponential envelope; evaluating the instantaneous displacement at $t = 1.0\text{ s}$ in `RAD` via `{{res:sc32_12_plot_02:keys}}` yields `{{res:sc32_12_plot_02:value}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `1 {{key:ENTER}} .60 {{key:×}}` | 0.00 | 0.00 | 0.00 | 0.600000 | Damping exponent $\zeta \omega_n t = 0.600000$ at $t = 1.0\text{ s}$ |
| `{{key:+/-}} {{key:eˣ}}` | 0.00 | 0.00 | 0.00 | 0.548812 | Exponential decay envelope $e^{-0.60} = 0.548812$ |
| `1 {{key:ENTER}}` | 0.00 | 0.548812 | 1.000000 | 1.000000 | Stage time $t = 1.0\text{ s}$ for oscillatory phase; envelope lifts to Z |
| `3.9546 {{key:×}}` | 0.00 | 0.00 | 0.548812 | 3.954600 | Damped phase angle $\omega_d t = 3.954600\text{ rad}$; envelope drops to Y |
| `{{key:COS}}` | 0.00 | 0.00 | 0.548812 | -0.687229 | Cosine carrier $\cos(3.9546\text{ rad}) = -0.687229$ |
| `{{key:×}}` | 0.00 | 0.00 | 0.00 | -0.377160 | Instantaneous suspension displacement $x(1.0) = -0.377160\text{ m}$ |

Plotting the optical diffraction sinc function $y(x) = \frac{\sin x}{x}$ over $x \in [-4\pi, +4\pi]$ in Radians mode (`{{key:RAD}}`) reveals the tall central maximum $y(0) \to 1$ flanked by decaying secondary fringes; evaluating the half-lobe point $x = \pi/2$ via `{{res:sc32_12_plot_07:keys}}` yields `{{res:sc32_12_plot_07:value}}` ($2/\pi \approx 0.636620$, where recalling $x = \pi/2$ from `{{key:LASTX}}` right after evaluating $\sin(\pi/2)$ divides $\sin(x)/x$ without retyping the angle).

Biochemical and structural curves display equally distinctive silhouettes across the $128 \times 52\text{-pixel}$ `{{key:PLOT}}` canvas—and both evaluate on the stack with `{{key:LASTX}}` while leaving Registers $Z$ and $T$ completely at zero:
* **Michaelis–Menten Enzyme Saturation Hyperbola ($v = \frac{V_{\max}[S]}{K_m + [S]}$):** Plotted over $[S] \in [0, 60]\text{ mM}$ for $V_{\max} = 100.0\text{ }\mu\text{mol/min}$ and $K_m = 15.0\text{ mM}$, the reaction curve climbs steeply near the origin where active sites are abundant, then bends into a saturation plateau toward the horizontal asymptote $V_{\max} = 100$. Using `{{key:LASTX}}` verifies the two reference points along that hyperbola with $[S]$ typed only once: at half-saturation $[S] = K_m = 15.0\text{ mM}$, multiplying $100 \times 15$ and recalling $[S] = 15.0\text{ mM}$ from `{{key:LASTX}}` to form $K_m + [S] = 30.0\text{ mM}$ confirms $v = 50.000000\text{ }\mu\text{mol/min}$ ($\frac{1}{2}V_{\max}$); at $[S] = 3K_m = 45.0\text{ mM}$, the same `{{key:LASTX}}` recall divides $100 \times 45$ by $45 + 15 = 60.0\text{ mM}$ to confirm $v = 75.000000\text{ }\mu\text{mol/min}$ ($\frac{3}{4}V_{\max}$).
* **Euler–Bernoulli Cantilevered Beam Deflection Curve ($y(x) = \frac{Px^2}{6EI}(3L - x)$):** Plotted across its $L = 4.0\text{ m}$ span ($\frac{P}{6EI} = 3.0625 \times 10^{-5}\text{ m}^{-2}$, or in normalized form `0.5*X^2*(6-X)` over $x \in [0, 2]$ via `0 {{key:ENTER}} 2 {{key:PLOT}}`), the elastic curve emerges horizontally from the clamped wall at $x = 0$ ($y(0) = y'(0) = 0$) before bowing cubically toward the free tip at $x = 4.0\text{ m}$. Because `{{key:LASTX}}` retains $x = 4.0\text{ m}$ after forming $3L = 3 \times 4.0 = 12.0\text{ m}$, the tip-deflection verification stays inside Register $X$ ($Y = Z = T = 0$): recalling `{{key:LASTX}}` twice subtracts $x = 4.0$ for $3L - x = 8.000000\text{ m}$ and squares $x^2 = 16.0\text{ m}^2$ via `{{key:x²}}` to form $x^2(3L - x) = 128.000000\text{ m}^3$, which scales by $3.0625 \times 10^{-5}\text{ m}^{-2}$ to resolve the tip sag $\delta_{\max} = 0.003920\text{ m}$ ($3.92\text{ mm}$).

Finally, to plot a piecewise Zener-diode voltage limiter $v_{\text{out}}(x) = \min(x, 5.0\text{ V}) = x - \langle x - 5 \rangle_+$ over $x \in [0, 8]\text{ V}$, enter `{{key:RCL}} X  {{key:RCL}} X  5 {{key:-}}  {{key:ENTER}} {{key:x>0}} {{key:×}}  {{key:-}}` in `{{key:EQN}}` and press `0 {{key:ENTER}} 8 {{key:PLOT}}`. Below the $5.0\text{ V}$ breakdown knee (e.g., at $x = 3.2\text{ V}$), `{{key:x>0}}` evaluates to $0$ so the plotted curve rises along a $45^\circ$ ramp ($v_{\text{out}} = 3.2\text{ V}$); above the knee (e.g., at $x = 7.4\text{ V}$), `{{key:x>0}}` evaluates to $1$ and subtracts the $2.4\text{ V}$ excess to clamp the plotted output flat at $5.000000\text{ V}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `3.2 {{key:STO}} X` | 0.000000 | 0.000000 | 0.000000 | 3.200000 | Sample linear ramp below knee ($x = 3.2\text{ V}$) |
| `{{key:RCL}} X 5 {{key:-}}` | 0.000000 | 0.000000 | 3.200000 | -1.800000 | Excess above Zener knee $x - 5 = -1.8\text{ V} < 0$ |
| `{{key:ENTER}} {{key:x>0}} {{key:×}} {{key:-}}` | 0.000000 | 0.000000 | 0.000000 | **3.200000** | Macaulay ramp is $0$; linear output $v_{\text{out}}(3.2) = 3.2\text{ V}$ |
| `7.4 {{key:STO}} X` | 0.000000 | 0.000000 | 3.200000 | 7.400000 | Sample clamped plateau above knee ($x = 7.4\text{ V}$) |
| `{{key:RCL}} X 5 {{key:-}}` | 3.200000 | 3.200000 | 7.400000 | 2.400000 | Excess above Zener knee $x - 5 = +2.4\text{ V} > 0$ |
| `{{key:ENTER}} {{key:x>0}} {{key:×}} {{key:-}}` | 3.200000 | 3.200000 | 3.200000 | **5.000000** | Subtract $2.4 \times 1 = 2.4\text{ V}$; clamped $v_{\text{out}}(7.4) = \mathbf{5.0\text{ V}}$ |

### Visual Overlays (`SOLVE`, `∫`) & Bivariate Scatter Plots (`Σ+` $\to$ `PLOT`)

When invoked alongside numerical root-finding or Adaptive Romberg Quadrature (`{{key:∫}}` via `∫ f(x)` on `{{key:LFU3}}`) {{cite:brent1973,romberg1955}}, the plotter shades the vertical area columns between $y = f(x)$ and $y = 0$. Likewise, plotting the Standard Normal density $f(z) = \frac{1}{\sqrt{2\pi}}e^{-z^2/2}$ over $Z \in [-3.5\sigma, +3.5\sigma]$ displays the symmetric Gaussian bell curve peaking at $f(0) = 0.3989422804$ with inflection points at $z = \pm 1.0\sigma$:

{{res:sc32_plot_normal_bell:screenshot|SC-32 Vector Plotter displaying the Standard Normal Bell Curve over [-3.5, +3.5].}}

When no active equation is selected and at least two statistical data pairs reside in the 50-point scatter ring buffer (`{{key:SUMS}}` mode), pressing `{{key:PLOT}}` renders a bivariate scatter plot with linear, logarithmic, exponential, or power trendline overlays. Take the four piezoresistive pressure sensor calibration pairs: $(10\text{ kPa}, 1.25\text{ V}), (20\text{ kPa}, 2.45\text{ V}), (30\text{ kPa}, 3.80\text{ V}), (40\text{ kPa}, 4.95\text{ V})$. Applying Francis Anscombe's visual rule—accumulating the pairs via `{{key:Σ+}}`, checking `{{key:m}}`, and pressing `{{key:PLOT}}` to inspect the 4-point scatter cloud against the overlaid regression line ($y = 0.1245x + 0.0000$, $r = 0.999565$, $R^2 = 0.999130$)—confirms visually that the transducer response is genuinely linear rather than a curved or outlier-skewed artifact:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `{{key:CLEAR}} {{key:CLΣ}}` | 0.00 | 0.00 | 0.00 | 0.00 | Clear statistical accumulators |
| `1.25 {{key:ENTER}} 10 {{key:Σ+}}` | 0.00 | 0.00 | 1.25 | 1.00 | Pair 1: (10 kPa, 1.25 V); count n = 1 |
| `2.45 {{key:ENTER}} 20 {{key:Σ+}}` | 0.00 | 1.25 | 2.45 | 2.00 | Pair 2: (20 kPa, 2.45 V); count n = 2 |
| `3.80 {{key:ENTER}} 30 {{key:Σ+}}` | 1.25 | 2.45 | 3.80 | 3.00 | Pair 3: (30 kPa, 3.80 V); count n = 3 |
| `4.95 {{key:ENTER}} 40 {{key:Σ+}}` | 2.45 | 3.80 | 4.95 | 4.00 | Pair 4: (40 kPa, 4.95 V); count n = 4 |
| `{{key:m}}` | 2.45 | 3.80 | 4.95 | 0.1245 | Regression slope m = 0.124500 V/kPa |

By uniting Descartes's coordinate geometry and Bresenham's integer rasterization on the $128 \times 52\text{-pixel}$ canvas, `{{key:PLOT}}` bridges qualitative curve inspection with 12-digit numerical verification. Inspecting the global silhouette of a function or scatter cloud first—and then passing reticle coordinates directly into `{{key:SOLVE}}`, `{{key:∫}}`, or `{{key:L.R.}}`—ensures that high-precision algorithms always operate on well-understood physical behavior.
