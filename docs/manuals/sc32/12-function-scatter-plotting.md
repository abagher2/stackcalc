---
title: "Chapter 12: Seeing the Invisible: From Descartes's Bedroom Ceiling to the Pixel Grid | Thinking in the Stack (SC-32)"
description: "From René Descartes's coordinate plane, Jack Bresenham's line algorithm, and Francis Anscombe's Quartet to vector function graphing and interactive viewport navigation on the StackCalc SC-32."
---

# Chapter 12: Seeing the Invisible: From Descartes's Bedroom Ceiling to the Pixel Grid

## The Fly on René Descartes's Ceiling and the Marriage of Algebra and Geometry

### Morning Meditation at La Flèche: Turning Equations into Curves

As a frail eleven-year-old boarding student at the Jesuit College of La Flèche in Anjou, **René Descartes** was granted an unusual privilege by the rector, Father Charlet: while his classmates rose at five o'clock every morning to recite Latin prayers in unheated stone halls, young René was allowed to remain warm under his blankets until late morning, thinking quietly with his eyes open.

Descartes kept that habit of morning meditation for the rest of his life. According to nineteenth-century mathematical lore, on one such morning as he lay in bed staring up at the corner of his room, a housefly landed on the plastered ceiling and began crawling from tile to tile. Watching the insect wander across the grid, Descartes asked himself how he could tell a friend the exact spot where the fly rested at any instant—and where it was headed next.

Suddenly, the answer flashed before him: if he measured the perpendicular distance $x$ from the left wall and the perpendicular distance $y$ from the back wall, **every position of the fly on the flat ceiling corresponded to a unique pair of numbers $(x, y)$**. Even better, if the fly walked along a straight diagonal line or a smooth circular arc, its two distances $x$ and $y$ obeyed a strict algebraic equation—and conversely, *any* algebraic equation connecting $x$ and $y$ traced a visible geometric curve across the ceiling!

When Descartes published this discovery in **1637** as ***La Géométrie*** {{cite:descartes1637}}—an appendix to his *Discourse on the Method*—he ended a two-thousand-year separation that had divided human thought since antiquity:

- **Ancient Greek Geometry (Euclid, Archimedes, Apollonius)** was rich in visual intuition—circles, triangles, parabolas, and tangent lines drawn with straightedge and compass—but it had almost no symbolic algebra. Proving a new theorem required inventing a custom geometric construction from scratch.
- **Medieval & Renaissance Algebra (al-Khwarizmi, Tartaglia, Cardano, Viète)** was a powerful symbolic machine for balancing unknowns ($x^2, x^3$), but it was blind. An equation sat on the page as a dry string of characters with no visual shape.

Descartes proved that **algebra and geometry are two languages describing the exact same reality**. John Stuart Mill later called analytic geometry *"the greatest single step ever made in the progress of the exact sciences,"* because it gave equations **eyes**—and gave geometric shapes **formulas**.

### Reading the Anatomy of a Curve: Roots, Peaks, Valleys & Inflection Points

Once you translate an algebraic formula $y = f(x)$ into a Cartesian curve across a horizontal $x$-axis (**domain**) and a vertical $y$-axis (**range**)—defined on the SC-32 via the **`{{key:EQN}}`** editor (Right Shift `{{key:↱}}` above `{{key:STO}}`)—every abstract concept from high-school Algebra II, Precalculus, and introductory calculus turns into an unmistakable landmark on a physical landscape:

1. **Zeros / Roots ($f(x) = 0$ — Where the Curve Crosses Sea Level):**
   In Chapter 7, hunting for the roots of a polynomial or transcendental equation meant searching for values of $x$ where $f(x) = 0$. On a Cartesian graph, a root is simply **a shoreline where the terrain crosses sea level** ($y = 0$), switching from negative elevation ($y < 0$, underwater) to positive elevation ($y > 0$, dry land).
2. **Local Maxima & Minima ($f'(x) = 0$ — Mountain Peaks and Valley Floors):**
   In Chapter 8, we saw that the derivative $f'(x)$ measures the instantaneous slope of a curve. As you hike up a mountain, the slope is positive ($f'(x) > 0$); as you descend the far side, the slope is negative ($f'(x) < 0$). At the exact summit of a smooth hill (**local maximum**) or the bottom of a smooth valley (**local minimum**), the ground beneath your boots is momentarily **flat and horizontal** ($f'(x) = 0$).
3. **Inflection Points ($f''(x) = 0$ — Where the Steering Wheel Passes Through Center):**
   What is an **inflection point**, and how can you feel one in your hands? Imagine driving a car along an S-shaped highway curve modeled by the cubic polynomial:

$$y(x) = x^3 - 6x^2 + 9x + 2$$

   Over the first half of the S-curve ($0 \le x < 2$), the road bends clockwise (curving downward on the map, **concave down**, where the second derivative $y''(x) = 6x - 12 < 0$), and your hands hold the steering wheel turned to the right. Over the second half ($2 < x \le 4$), the road bends counterclockwise (**concave up**, $y''(x) > 0$), and your hands hold the steering wheel turned to the left. Right at $x = 2$, where $y''(2) = 6(2) - 12 = 0$ and the road passes through $(2, 4)$, **your steering wheel passes momentarily through dead center** as the curve switches from bending right to bending left.
4. **Vertical & Horizontal Asymptotes (Cliffs and Plateaus):**
   When a rational denominator approaches zero—such as the thin-lens magnification formula $f(x) = \frac{1}{x - 2}$ as an object crosses the focal point $x = 2$—the curve rockets toward $-\infty$ on the left and plunges from $+\infty$ on the right along a **vertical asymptote**. Conversely, when a skydiver steps from a high-altitude balloon under gravity $g$ and quadratic air drag ($v(t) = v_{\text{term}}\tanh(gt/v_{\text{term}})$), or when an uncharged capacitor charges through a resistor toward a supply voltage $V_{\max}$ with RC time constant $\tau$:

$$V(t) = V_{\max}\!\left(1 - e^{-t/\tau}\right)$$

   upward air resistance or capacitor back-voltage gradually balances the driving force, and the curve bends smoothly toward a flat horizontal ceiling—a **horizontal asymptote** at $v = v_{\text{term}}$ or $V = V_{\max}$ as $t \to \infty$.

---

## Rasterization on a Pocket Canvas: Turning Equations into Pixels

### The Paradox of Digital Graphics: Continuous Math on a Discrete Grid

Descartes imagined his coordinate plane as infinitely smooth: between any two points on a line, there are infinitely many closer points. A computer or calculator screen, however, is **discrete**. Inspect a monochrome liquid-crystal display through a magnifying glass, and you will see a chessboard of tiny rectangular liquid-crystal shutters (**pixels**, short for *picture elements*), each of which is either **ON (dark ink)** or **OFF (reflective paper background)**.

That raises a fascinating computer-science question that bridges Chapter 10 (discrete integer bits) and Chapter 8 (continuous functions): **how does a digital processor translate a smooth, continuous mathematical equation $y = f(x)$ into a crisp ribbon of integer pixels in less than a twentieth of a second?**

Inside the SC-32's $132 \times 65\text{ pixel}$ transflective LCD, the graphical plotting viewport dedicates a clean $128 \times 52\text{ pixel}$ active curve canvas directly above the 13-pixel status and coordinate readout bar. Placing the horizontal domain window $[X_{\min}, X_{\max}]$ into Registers $Y$ and $X$ and pressing **`{{key:PLOT}}`** (Right Shift `{{key:↱}}` above `{{key:x∥y}}`) launches the firmware's 100-step Bresenham vector renderer across the 128-column plotting canvas in three clean inside-out stages:

### Stage 1: Slicing the Continuous Domain into Discrete Columns

Suppose you ask the calculator to plot a function $y = f(x)$ across a horizontal world window from $X_{\min} = -3.0$ on the left to $X_{\max} = +3.0$ on the right (a total horizontal span of $\Delta X = X_{\max} - X_{\min} = 6.0$). In firmware, the plotter sweeps $100$ evenly spaced horizontal steps across the 128-column viewport; to illustrate the exact column-sampling algebra on the stack with clean mental fractions, consider a **worked 64-column ($N = 64$, $k = 0, 1, 2, \dots, 63$) affine viewport-mapping benchmark** that divides the span into $N - 1 = 63$ equal steps of width $\Delta x = \frac{X_{\max} - X_{\min}}{63}$:

$$x_k = X_{\min} + k \left(\frac{X_{\max} - X_{\min}}{63}\right), \qquad k = 0, 1, \dots, 63$$

At column $k = 0$ (the left edge), $x_0 = -3.0$; at column $k = 21$ (exact one-third of the way across, since $21 / 63 = 1/3$), $x_{21} = -3.0 + 21 \times \frac{6.0}{63} = -3.0 + 2.0 = -1.0$; and at column $k = 63$ (the right edge), $x_{63} = +3.0$.

### Stage 2: Auto-Scaling & The Affine Viewport Transformation (Flipping the Y-Axis)

As the calculator evaluates $y_k = f(x_k)$ at each sampled horizontal step across the 128-column canvas, it keeps a running record of the lowest value $Y_{\min} = \min(y_k)$ and the highest value $Y_{\max} = \max(y_k)$—cleverly skipping over any sample where the function hits an undefined division by zero (`NaN` or $\pm\infty$) so a single vertical asymptote does not crush the rest of the graph into a flat line.

Now comes a subtle twist that every game programmer and graphics engineer learns on Day One: **in mathematics, $+y$ points UP, but in computer memory, pixel row numbers $v$ count DOWN from the top-left corner of the screen.**

Within the $132 \times 65$ transflective display's active $128 \times 52\text{ pixel}$ graphing viewport (where horizontal pixel columns run from $u = 0$ on the left to $u = 127$ on the right, and vertical pixel rows run from $v = 0$ at the **top** edge to $v = 51$ at the **bottom** edge above the 13-pixel coordinate readout bar), mapping a continuous world point $(x, y)$ onto an integer screen pixel $(u, v)$ requires a two-step **Affine Viewport Transformation**:

$$u = \left\lfloor \frac{x - X_{\min}}{X_{\max} - X_{\min}} \times 127 \right\rfloor, \qquad v = 51 - \left\lfloor \frac{y - Y_{\min}}{Y_{\max} - Y_{\min}} \times 51 \right\rfloor$$

Examine the inside-out structure of both formulas:
1. **Normalize (`[0, 1]`):** Subtract the minimum bound ($x - X_{\min}$ or $y - Y_{\min}$) and divide by the total window span ($X_{\max} - X_{\min}$ or $Y_{\max} - Y_{\min}$). That turns *any* physical units—whether nanometers of optical wavelength, seconds of rocket burn, or millions of dollars—into a universal dimensionless fraction between $0.0$ and $1.0$.
2. **Scale & Invert:** Multiply the horizontal fraction by $127$ pixels; multiply the vertical fraction by $51$ pixels and subtract from $51$ so the highest mathematical peak ($y = Y_{\max}$) lands at the top row of the screen ($v = 0$) and the lowest valley ($y = Y_{\min}$) lands at the bottom row ($v = 51$).

### Stage 3: Jack Bresenham's 1962 Integer Line-Drawing Miracle

Wait: if you only light up the isolated sample dots $(u_k, v_k)$ on the screen, a steep curve—like a high-frequency sine wave or a cubic polynomial—will look like a scattered constellation of disconnected dots with wide vertical gaps between columns.

How do you connect two pixel coordinates $(u_0, v_0)$ and $(u_1, v_1)$ with a continuous, gap-free straight line segment on a square grid?

In **1962**, a twenty-four-year-old engineer named **Jack Elton Bresenham** was working at IBM's computation laboratory in San Jose, California. He wanted to write a program to drive an early CalComp mechanical drum plotter attached to an IBM 1401 computer. There was just one catch: the computer had **no floating-point hardware** and **no fast division instruction**. If the plotter had to compute a floating-point slope $m = \frac{\Delta v}{\Delta u}$ and round decimals at every single pixel step, drawing one graph would take forever.

Bresenham asked a brilliant inside-out question: suppose we are drawing a line that moves $\Delta u = u_1 - u_0$ pixels to the right and rises $\Delta v = |v_1 - v_0|$ pixels vertically (with $\Delta v \le \Delta u$, and swapping the roles of $u$ and $v$ whenever a steep curve segment rises faster than it runs, $\Delta v > \Delta u$). As we step one column to the right ($u \leftarrow u + 1$), the true mathematical line rises by the fraction $\frac{\Delta v}{\Delta u}$ of a pixel. We only need to decide a simple binary question: **is the true line closer to staying on the current pixel row $v$, or stepping one pixel row up ($v \pm 1$)?**

Instead of dividing $\Delta v$ by $\Delta u$ and comparing the fraction against $\frac{1}{2}$ ($0.5$), Bresenham multiplied the entire inequality by $2\Delta u$ to clear the fraction completely. That left an **integer error accumulator**:

$$\epsilon_0 = 2\Delta v - \Delta u$$

- On each horizontal pixel step, if $\epsilon < 0$, the line has not yet crossed the halfway mark: stay on the same row $v$ and add $2\Delta v$ to $\epsilon$.
- If $\epsilon \ge 0$, the line has crossed the halfway mark: step one pixel vertically ($v \leftarrow v \pm 1$) and add $2(\Delta v - \Delta u)$ to $\epsilon$.

Zero fractions, zero floating-point decimals, and zero divisions—just integer addition, subtraction, and a bit-shift by $2$! **Bresenham's Line Algorithm** became one of the foundational pillars of computer graphics, etched into the silicon of every modern graphics card, laser printer, CNC milling controller, and the SC-32's 42-millisecond vector plotting engine {{cite:hp32sii1991}}.

---

## Why Summary Numbers Can Lie: Anscombe's Quartet & Visual Root Bracketing

### Francis Anscombe's 1973 Quartet: Why You Must Always Plot Your Data

In Chapter 9, we saw how Carl Friedrich Gauss's method of least squares distills a cloud of $(x_i, y_i)$ measurements into four clean summary numbers: the sample means $(\bar{x}, \bar{y})$, the sample standard deviations $(s_x, s_y)$, the linear regression line $\hat{y} = m x + b$, and Karl Pearson's correlation coefficient $r$.

By the early 1970s, as mainframe computers made statistical regression effortless, many scientists and economists stopped bothering to graph their data at all—looking only at the printed values of $m, b,$ and $r$.

In **1973**, British statistician **Francis John Anscombe**—founder of Yale University's Department of Statistics—published a four-page paper in *The American Statistician* titled *"Graphs in Statistical Analysis"* that shocked the scientific world. To prove that summary statistics without a visual plot can be dangerously deceptive, Anscombe constructed four small datasets (**Anscombe's Quartet**), each consisting of $n = 11$ coordinate pairs $(x_i, y_i)$.

If you feed all four datasets into a statistical calculator and read only the summary numbers, they look **100% identical**:

| Statistical Metric | Dataset I | Dataset II | Dataset III | Dataset IV |
| :--- | :---: | :---: | :---: | :---: |
| **Sample Size ($n$)** | $11$ | $11$ | $11$ | $11$ |
| **Mean of $x$ ($\bar{x}$) & Variance ($s_x^2$)** | $\bar{x} = 9.0,\; s_x^2 = 11.0$ | $\bar{x} = 9.0,\; s_x^2 = 11.0$ | $\bar{x} = 9.0,\; s_x^2 = 11.0$ | $\bar{x} = 9.0,\; s_x^2 = 11.0$ |
| **Mean of $y$ ($\bar{y}$) & Variance ($s_y^2$)** | $\bar{y} = 7.50,\; s_y^2 = 4.125$ | $\bar{y} = 7.50,\; s_y^2 = 4.125$ | $\bar{y} = 7.50,\; s_y^2 = 4.125$ | $\bar{y} = 7.50,\; s_y^2 = 4.125$ |
| **Least-Squares Line ($\hat{y} = m x + b$)** | $\hat{y} = 0.500x + 3.00$ | $\hat{y} = 0.500x + 3.00$ | $\hat{y} = 0.500x + 3.00$ | $\hat{y} = 0.500x + 3.00$ |
| **Correlation ($r$) & Determination ($R^2$)** | $r = 0.816,\; R^2 = 0.667$ | $r = 0.816,\; R^2 = 0.667$ | $r = 0.816,\; R^2 = 0.667$ | $r = 0.816,\; R^2 = 0.667$ |

An analyst looking only at $m = 0.500$, $b = 3.00$, and $r = 0.816$ would conclude that all four experiments show the exact same moderately strong linear trend. Yet the moment you press **`{{key:PLOT}}`** after accumulating your data pairs with **`{{key:Σ+}}`**, the SC-32 automatically renders a bivariate scatter plot with the least-squares trendline $\hat{y} = 0.500x + 3.00$ overlaid, and four completely different stories appear in less than a second:

- **Dataset I (True Linear Cloud):** Eleven noisy data points scattered naturally around a genuine straight line—the only dataset where linear regression is actually appropriate.
- **Dataset II (The Hidden Parabola):** Eleven points lying on a smooth, noiseless **quadratic arch** that rises to a peak and curves back down. A linear fit is the wrong mathematical model—the data calls for a polynomial or nonlinear curve.
- **Dataset III (The Single Bad Outlier):** Ten points lying on a razor-sharp straight line of slope $0.346$, plus **one single corrupted sensor reading** at $(13, 12.74)$ that yanks the least-squares slope up to $0.500$ and ruins the correlation.
- **Dataset IV (The Leverage Mirage):** Ten points stacked vertically at the exact same $x = 8.0$ (showing *zero* relationship between $x$ and $y$), plus **one isolated point** far to the right at $(19, 12.50)$ that single-handedly fabricates a fake correlation of $r = 0.816$!

Anscombe's Quartet is why a scientist or engineer should never trust a correlation coefficient in the dark: pairing `{{key:Σ+}}` statistical accumulation with `{{key:PLOT}}` lets your eyes verify in an instant whether your data follows a straight line, an exponential curve, a power law, or contains a rogue outlier.

### Visual Root Bracketing & Harmonic Waveforms: Where Vision Guides Precision

Plotting is equally transformative when paired with numerical root-finding (`{{key:SOLVE}}`) and integration (`{{key:∫}}`) {{cite:brent1973,romberg1955}}. Think about the complementary strengths of the human eye and a 12-digit numerical solver:

- **The Eye Sees the Whole Landscape (Global Reconnaissance):** When you plot a wave or polynomial across the 128-column viewport, your eye immediately sees *how many* roots cross the axis, where local peaks and valleys sit, and whether a vertical asymptote lurks inside the interval—preventing the classic blunder of asking a root solver to search an interval that contains no root or jumps across infinity.
- **The Solver Refines One Point to 12 Digits (Local Precision):** A pixel screen has finite horizontal column resolution, whereas Richard Brent's solver and Werner Romberg's integrator operate at full 12-digit precision.

By bisecting and panning the plotted viewport with the six binary-search navigation softkeys (`<`, `|<-`, `OUT`, `IN`, `->|`, `>`) and tapping **`{{key:PLOT}}`** a second time to drop root markers (**`MARK`**), push brackets onto the stack (**`STORE`**) for **`{{key:SOLVE}}`**, or shade definite integrals (**`∫ f(x)`**), you unite global visual insight with 12-digit analytical certainty across every waveform in physics and engineering:

1. **Joseph Fourier's 1807 Harmonic Synthesis:** When French mathematician **Jean-Baptiste Joseph Fourier** announced in 1807 that a flat-topped **square wave** with sharp corners could be built by adding smooth sine waves of odd frequencies:
   $$y(t) = \sin(t) + \frac{1}{3}\sin(3t) + \frac{1}{5}\sin(5t) + \cdots$$
   Lagrange and Laplace could hardly believe it. Plotting just the first three odd harmonics shows *why* Fourier was right: the fundamental $\sin(t)$ forms the main arch, the negative peak of $\frac{1}{3}\sin(3t)$ at $t = 90^\circ$ ($\sin 270^\circ = -1$) presses the middle of the arch down to $1 - \frac{1}{3} = 0.667$, and $\frac{1}{5}\sin(5t)$ lifts the center back up to $1 - \frac{1}{3} + \frac{1}{5} = \mathbf{0.866667}$ while squaring off the shoulders (leaving the famous **Gibbs-phenomenon** ripple ears at the corners).
2. **Damped Harmonic Ringdown:** When an automobile suspension hits a speed bump at $t = 0$, the coil spring oscillates at $\cos(\omega_d t)$ while the hydraulic shock absorber wraps the motion inside an exponential decay envelope $e^{-\zeta\omega_n t}$:
   $$x(t) = e^{-\zeta\omega_n t}\cos(\omega_d t)$$
   Plotting the curve reveals both the oscillation period and how quickly the rebound troughs die away.
3. **Laser Diffraction & The `sinc` Envelope:** When light passes through a narrow slit, interference produces the classic diffraction pattern $y(x) = \frac{\sin x}{x}$, with a tall central bright fringe $\lim_{x \to 0}\frac{\sin x}{x} = 1$ and alternating side lobes that cross zero at every non-zero multiple of $\pi$.
4. **Piecewise & Clipped Waveforms via Relational Indicator Tests (`{{key:x?0}}` and `{{key:x?y}}`):** As we discovered in Chapter 7, the relational test menus **`{{key:x?y}}`** (Left Shift `{{key:↰}}` above `{{key:÷}}`) and **`{{key:x?0}}`** (Right Shift `{{key:↱}}` above `{{key:÷}}`) evaluate inside `{{key:EQN}}` to Kenneth Iverson's Boolean indicator $1.0$ (True) or $0.0$ (False). By combining a smooth curve with the three-keystroke Macaulay ramp idiom (`{{key:ENTER}} {{key:x>0}} {{key:×}}`), you can plot and trace half-wave rectifiers / neural-network ReLU units $y = x[x > 0]$, Zener voltage clippers $v_{\text{out}}(x) = x - \langle x - V_Z \rangle_+$, or multi-branch piecewise engineering laws across the entire 128-column canvas of `{{key:PLOT}}` without switching equations!

---

## On the Stack: Function Graphing, Reticle Tracing & Scatter-Plot Workbench

See how every graphical idea in this chapter flows directly from our inside-out stack philosophy. A two-dimensional point $(x, y)$ on Descartes's ceiling—or a horizontal plotting window $[X_{\min}, X_{\max}]$—is simply a pair of numbers sitting naturally on two adjacent shelves: Register `Y` holds the lower domain bound $X_{\min}$, and Register `X` holds the upper domain bound $X_{\max}$. When you center a feature or drop a pair of markers $[x_1, x_2]$ on the SC-32's `{{key:PLOT}}` viewport and tap `{{key:PLOT}}` $\to$ `STORE` (`{{key:LFU2}}`), the calculator pushes those exact coordinates straight into Registers `Y` and `X`, ready for immediate root refinement via `{{key:SOLVE}}`, area integration via `{{key:∫}}`, or algebraic verification on the stack. Let us step onto the workbench and explore the plotting engine in action.

{{screenshot:sc32_plot_polynomial|The StackCalc SC-32 rendering an interactive vector curve (X³ − 6X² + 11X − 6) via {{key:PLOT}} with real-time coordinate crosshair telemetry.}}

### Viewport Geometry, Affine Column Mapping & Crosshair Controls

Inside the SC-32's $132 \times 65$ transflective monochrome dot-matrix display, the dedicated **Vector Graphics Engine (`{{key:PLOT}}`)**—accessed via Right Shift `{{key:↱}}` above `{{key:x∥y}}` (Row 7, Column 3) {{cite:hp32sii1991}}—renders functions (sampling 100 horizontal steps across the 128-column canvas in firmware) and scatter clouds across a $128 \times 52\text{ pixel}$ active plotting viewport directly above the 13-pixel coordinate telemetry bar.

For our worked 64-column ($N - 1 = 63$, $k \in [0, 63]$) affine viewport-mapping benchmark on the stack at sample column $k = 21$ across the default domain $[-3.0, +3.0]$ ($x_k = X_{\min} + k\frac{X_{\max} - X_{\min}}{63}$), this 4-register trace illustrates how each discrete column maps to its exact domain abscissa $x_{21} = -1.000000$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `3 {{key:ENTER}} 3 {{key:+/-}} {{key:-}}` | 0.000000 | 0.000000 | 0.000000 | 6.000000 | Total domain span $X_{\max} - X_{\min} = 3.0 - (-3.0) = 6.0$ |
| `63 {{key:÷}}` | 0.000000 | 0.000000 | 0.000000 | 0.095238 | Quantized column step $\Delta x = 6.0 / 63 \approx 0.095238$ |
| `21 {{key:×}}` | 0.000000 | 0.000000 | 0.000000 | 2.000000 | Horizontal displacement $k \cdot \Delta x = 2.0$ at column $k = 21$ |
| `3 {{key:+/-}} {{key:+}}` | 0.000000 | 0.000000 | 0.000000 | -1.000000 | Sampled domain coordinate $x_{21} = X_{\min} + 2.0 = -1.000000$ |

The SC-32's **`{{key:PLOT}}`** engine (`Right Shift {{key:↱}} above {{key:x∥y}}`) replaces cumbersome setup forms and manual window-variable entry with a direct, stack-driven graphical architecture:

1. **Stack-Driven Horizontal Domain $[X_{\min}, X_{\max}]$ & Automatic Vertical Autoscaling:** To plot any equation stored in `{{key:EQN}}`, push the lower bound $X_{\min}$ into **Register $Y$** and the upper bound $X_{\max}$ into **Register $X$** (`Xmin {{key:ENTER}} Xmax`), press **`{{key:PLOT}}`** (Right Shift `{{key:↱}}` above `{{key:x∥y}}`), select the equation softkey (`{{key:LFU0}}`–`{{key:LFU5}}`), and tap the independent variable softkey (`X`, `T`, etc.) or `EXEC` (if $Y = X$, the engine defaults to $[-3.0, +3.0]$, or $[-10.0, +10.0]$ via `EXEC`). As the engine sweeps 100 horizontal sample steps across the 128-column viewport, it **automatically autoscales the vertical range $[Y_{\min}, Y_{\max}]$** with a $10\%$ top/bottom margin, printing the live **`[minY, maxY]`** range at the top-right of the LCD and the center $x$-coordinate **`centerX`** at the top-left.
2. **Automatic Senary Root-Marker Detection:** During every plot sweep, the engine partitions $[X_{\min}, X_{\max}]$ into 6 senary sub-intervals, detects sign changes $f(x_k)\cdot f(x_{k+1}) < 0$, refines each zero crossing via 30-step binary bisection to $10^{-10}$, and draws vertical root markers directly on the curve.
3. **The 6 Primary Plot Navigation Softkeys (`{{key:LFU0}}`–`{{key:LFU5}}`):** While a graph is displayed, the six top softkeys form a **Binary-Search Zoom & Pan Toolbar**:
   * **`{{key:LFU0}}` (`<`):** Pan Left by $25\%$ of the current domain width.
   * **`{{key:LFU1}}` (`|<-`):** Bisect Left Half—zooms the domain to the left half $[X_{\min}, X_{\text{center}}]$.
   * **`{{key:LFU2}}` (`OUT`, or `{{key:<-}}` Backspace):** Zoom Out $2\times$ around `centerX`.
   * **`{{key:LFU3}}` (`IN`):** Zoom In $2\times$ ($0.5\times$ width) around `centerX`.
   * **`{{key:LFU4}}` (`->|`):** Bisect Right Half—zooms the domain to the right half $[X_{\text{center}}, X_{\max}]$.
   * **`{{key:LFU5}}` (`>`):** Pan Right by $25\%$ of the current domain width.
4. **The Second-Tap `{{key:PLOT}}` Action Toolbar (`MARK`, `CLEAR`, `STORE`, `∫ f(x)`):** Pressing **`{{key:PLOT}}`** a second time while viewing a graph toggles the 4-action softkey menu:
   * **`{{key:LFU0}}` (`MARK`):** Drops a vertical marker at the current center crosshair `centerX`.
   * **`{{key:LFU1}}` (`CLEAR`):** Clears active plot markers.
   * **`{{key:LFU2}}` (`STORE`):** Pushes the two most recent plot markers $[x_1, x_2]$ (or $(y, x)$ at the center crosshair) directly onto **Registers $Y$ and $X$** of the live RPN stack—giving you an instant visual bracket for **`{{key:SOLVE}}`**.
   * **`{{key:LFU3}}` (`∫ f(x)`):** Executes Romberg quadrature (`{{key:∫}}`) directly between the active markers (or across $[X_{\min}, X_{\max}]$) and shades the area under the curve.
   * Pressing **`{{key:C}}`** exits `{{key:PLOT}}` cleanly back to the stack.

> **Visual Root-Bracketing Recipe (`PLOT` $\to$ `MARK` $\to$ `STORE` $\to$ `SOLVE`):**
> To find a root to 12-digit precision without guessing blind brackets:
> 1. Push your search window $[X_{\min}, X_{\max}]$ onto the stack (`Xmin {{key:ENTER}} Xmax`) and press `{{key:PLOT}}` (Right Shift `{{key:↱}}` above `{{key:x∥y}}`).
> 2. Use the binary-search navigation softkeys (`|<-`, `->|`, `IN`, `<`, `>`) to frame the zero crossing (or drop two markers straddling the crossing via second-tap `{{key:PLOT}}` $\to$ `MARK` on `{{key:LFU0}}`).
> 3. Tap `{{key:PLOT}}` $\to$ `STORE` (`{{key:LFU2}}`) to push the visual bracket $[x_1, x_2]$ directly onto Registers $Y$ and $X$, press `{{key:C}}` to return to the stack, and invoke `{{key:SOLVE}}` (Right Shift `{{key:↱}}` above `{{key:7}}`) to polish the zero crossing to 12-digit accuracy!

### Tracing Cubic Inflections, Fourier Square Waves, Damped Ringdown & `sinc` Lobes

Consider the cubic highway S-curve $y(x) = x^3 - 6x^2 + 9x + 2$ plotted over $x \in [0, 4]$ via `0 {{key:ENTER}} 4 {{key:PLOT}}`: its local maximum rises to $(1, 6)$, its local minimum dips to $(3, 2)$, and its inflection point ($y''(x) = 6x - 12 = 0$) sits midway between them at $x = 2$. Writing $y(x)$ in nested Horner form $y(x) = ((x - 6)x + 9)x + 2$ and pre-filling the 4-level stack evaluates the inflection ordinate ($X = \mathbf{4.000000}$) with `2` typed only once:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `2 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}` | 2.000000 | 2.000000 | 2.000000 | 2.000000 | Flood all four stack registers with inflection abscissa $x = 2.0$ |
| `6 {{key:-}}` | 2.000000 | 2.000000 | 2.000000 | -4.000000 | Innermost Horner factor $x - 6 = -4.0$; Register $T$ replicates $2.0$ |
| `{{key:×}} 9 {{key:+}}` | 2.000000 | 2.000000 | 2.000000 | 1.000000 | Second Horner stage $(x - 6)x + 9 = 1.0$; $x = 2.0$ drops into $Y$ |
| `{{key:×}} 2 {{key:+}}` | 2.000000 | 2.000000 | 2.000000 | 4.000000 | Inflection point ordinate $y(2) = ((x - 6)x + 9)x + 2 = 4.000000$ |

To synthesize and plot Joseph Fourier's three-harmonic square wave $y(t) = \sin(t) + \frac{1}{3}\sin(3t) + \frac{1}{5}\sin(5t)$ across $t \in [-180.0^\circ, +180.0^\circ]$ in Degrees mode (`{{key:DEG}}`), store `T {{key:SIN}} T 3 {{key:×}} {{key:SIN}} 3 {{key:÷}} {{key:+}} T 5 {{key:×}} {{key:SIN}} 5 {{key:÷}} {{key:+}}` in `{{key:EQN}}` (remembering that inside `{{key:EQN}}` mode, each variable `T` is keyed via `{{key:RCL}} T`, i.e., `{{key:RCL}}` followed by `{{key:4}}`), and launch the domain $[-180^\circ, +180^\circ]$ directly from the stack via `180 {{key:+/-}} {{key:ENTER}} 180 {{key:PLOT}}`! Navigating to the center plateau trough at $t = 90.0^\circ$ in `{{key:DEG}}` mode and verifying on the stack via {{res:sc32_12_plot_01:keys}} yields $\mathbf{{{res:sc32_12_plot_01:value}}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `90 {{key:SIN}}` | 0.00 | 0.00 | 0.00 | 1.000000 | Fundamental harmonic $\sin(90^\circ) = 1.000000$ |
| `90 {{key:ENTER}} 3 {{key:×}} {{key:SIN}}` | 0.00 | 0.00 | 1.000000 | -1.000000 | Third harmonic phase $\sin(270^\circ) = -1.000000$; fundamental lifts to Y |
| `3 {{key:÷}}` | 0.00 | 0.00 | 1.000000 | -0.333333 | Scale third harmonic amplitude $-\frac{1}{3} = -0.333333$ |
| `{{key:+}}` | 0.00 | 0.00 | 0.00 | 0.666667 | Partial sum of 1st + 3rd harmonics ($0.666667$) |
| `90 {{key:ENTER}} 5 {{key:×}} {{key:SIN}}` | 0.00 | 0.00 | 0.666667 | 1.000000 | Fifth harmonic phase $\sin(450^\circ) = 1.000000$; partial sum lifts to Y |
| `5 {{key:÷}}` | 0.00 | 0.00 | 0.666667 | 0.200000 | Scale fifth harmonic amplitude $+\frac{1}{5} = 0.200000$ |
| `{{key:+}}` | 0.00 | 0.00 | 0.00 | 0.866667 | Three-harmonic square wave trough ordinate $y(90^\circ) = 0.866667$ |

When an underdamped sports suspension $x(t) = e^{-0.60 t} \cos(3.9546 t)$ ($\zeta = 0.15, \omega_n = 4.0\text{ rad/s}, \omega_d = 3.9546\text{ rad/s}$) is plotted over $t \in [0, 6\text{ s}]$ in Radians mode (`{{key:RAD}}`), the trace shows the cosine oscillation decaying inside its exponential envelope; evaluating the instantaneous displacement at $t = 1.0\text{ s}$ in `RAD` via {{res:sc32_12_plot_02:keys}} yields $\mathbf{{{res:sc32_12_plot_02:value}}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `1 {{key:ENTER}} .60 {{key:×}}` | 0.00 | 0.00 | 0.00 | 0.600000 | Damping exponent $\zeta \omega_n t = 0.600000$ at $t = 1.0\text{ s}$ |
| `{{key:+/-}} {{key:eˣ}}` | 0.00 | 0.00 | 0.00 | 0.548812 | Exponential decay envelope $e^{-0.60} = 0.548812$ |
| `1 {{key:ENTER}}` | 0.00 | 0.548812 | 1.000000 | 1.000000 | Stage time $t = 1.0\text{ s}$ for oscillatory phase; envelope lifts to Z |
| `3.9546 {{key:×}}` | 0.00 | 0.00 | 0.548812 | 3.954600 | Damped phase angle $\omega_d t = 3.954600\text{ rad}$; envelope drops to Y |
| `{{key:COS}}` | 0.00 | 0.00 | 0.548812 | -0.687229 | Cosine carrier $\cos(3.9546\text{ rad}) = -0.687229$ |
| `{{key:×}}` | 0.00 | 0.00 | 0.00 | -0.377160 | Instantaneous suspension displacement $x(1.0) = -0.377160\text{ m}$ |

Plotting the optical diffraction **sinc function** $y(x) = \frac{\sin x}{x}$ over $x \in [-4\pi, +4\pi]$ in Radians mode (`{{key:RAD}}`) reveals the tall central maximum $y(0) \to 1$ flanked by decaying secondary fringes; evaluating the half-lobe point $x = \pi/2$ via {{res:sc32_12_plot_07:keys}} yields $\mathbf{{{res:sc32_12_plot_07:value}}}$ ($2/\pi \approx 0.636620$—or with `{{key:LASTX}}` via `{{key:RAD}} {{key:π}} 2 {{key:÷}} {{key:SIN}} {{key:LASTX}} {{key:÷}}`).

Biochemical and structural curves display equally distinctive silhouettes on the `{{key:PLOT}}` canvas. Plotting Michaelis–Menten enzyme saturation $v = \frac{V_{\max}[S]}{K_m + [S]}$ ($V_{\max} = 100.0\text{ }\mu\text{mol/min}$, $K_m = 15.0\text{ mM}$) over $[S] \in [0, 60]\text{ mM}$ traces a steep initial rise that bends smoothly toward the horizontal asymptote $V_{\max} = 100$, and `{{key:LASTX}}` verifies key landmarks along that curve with $[S]$ typed only once: at $[S] = 15.0\text{ mM}$ ($K_m$, half-saturation), keying `100 {{key:ENTER}} 15 {{key:×}} {{key:LASTX}} 2 {{key:×}} {{key:÷}}` confirms $v = \mathbf{50.000000}$, and at $[S] = 45.0\text{ mM}$ ($3K_m$, three-quarter saturation), keying `100 {{key:ENTER}} 45 {{key:×}} {{key:LASTX}} 15 {{key:+}} {{key:÷}}` confirms $v = \mathbf{75.000000}$. Likewise, plotting an Euler–Bernoulli cantilevered beam $y(x) = \frac{Px^2}{6EI}(3L - x)$ across its $L = 4.0\text{ m}$ span ($\frac{P}{6EI} = 3.0625 \times 10^{-5}\text{ m}^{-2}$) shows the beam emerging horizontally from the clamped wall ($y(0) = y'(0) = 0$) before curving into a cubic bend toward the free tip at $x = 4.0\text{ m}$, where double-`{{key:LASTX}}` recall evaluates the maximum tip deflection with `4` typed only once:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `3 {{key:ENTER}} 4 {{key:×}}` | 0.000000 | 0.000000 | 0.000000 | 12.000000 | Compute $3L = 12.0\text{ m}$; tip coordinate $x = 4.0\text{ m}$ archived in `LASTX` |
| `{{key:LASTX}} {{key:-}}` | 0.000000 | 0.000000 | 0.000000 | 8.000000 | Recall $x = 4.0\text{ m}$ and subtract for span factor $3L - x = 8.0\text{ m}$ |
| `{{key:LASTX}} {{key:x²}} {{key:×}}` | 0.000000 | 0.000000 | 0.000000 | 128.000000 | Recall $x = 4.0\text{ m}$ again, square to $16.0\text{ m}^2$, and form $x^2(3L - x) = 128.0\text{ m}^3$ |
| `3.0625 {{key:E}} 5 {{key:+/-}} {{key:×}}` | 0.000000 | 0.000000 | 0.000000 | 0.003920 | Scale by $\frac{P}{6EI} = 3.0625 \times 10^{-5}\text{ m}^{-2}$; tip deflection $\delta_{\max} = 0.003920\text{ m}$ |

Finally, to plot a **piecewise Zener-diode voltage limiter** $v_{\text{out}}(x) = \min(x, 5.0\text{ V}) = x - \langle x - 5 \rangle_+$ over $x \in [0, 8]\text{ V}$, enter `{{key:RCL}} X  {{key:RCL}} X  5 {{key:-}}  {{key:ENTER}} {{key:x>0}} {{key:×}}  {{key:-}}` in `{{key:EQN}}` and press `0 {{key:ENTER}} 8 {{key:PLOT}}`. Below the $5.0\text{ V}$ breakdown knee (e.g., at $x = 3.2\text{ V}$), `{{key:x>0}}` evaluates to $0$ so the plotted curve rises along a $45^\circ$ ramp ($v_{\text{out}} = 3.2\text{ V}$); above the knee (e.g., at $x = 7.4\text{ V}$), `{{key:x>0}}` evaluates to $1$ and subtracts the $2.4\text{ V}$ excess to clamp the plotted output flat at **$5.000000\text{ V}$**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `3.2 {{key:STO}} X` | 0.000000 | 0.000000 | 0.000000 | 3.200000 | Sample linear ramp below knee ($x = 3.2\text{ V}$) |
| `{{key:RCL}} X 5 {{key:-}}` | 0.000000 | 0.000000 | 3.200000 | -1.800000 | Excess above Zener knee $x - 5 = -1.8\text{ V} < 0$ |
| `{{key:ENTER}} {{key:x>0}} {{key:×}} {{key:-}}` | 0.000000 | 0.000000 | 0.000000 | **3.200000** | Macaulay ramp is $0$; linear output $v_{\text{out}}(3.2) = 3.2\text{ V}$ |
| `7.4 {{key:STO}} X` | 0.000000 | 0.000000 | 3.200000 | 7.400000 | Sample clamped plateau above knee ($x = 7.4\text{ V}$) |
| `{{key:RCL}} X 5 {{key:-}}` | 3.200000 | 3.200000 | 7.400000 | 2.400000 | Excess above Zener knee $x - 5 = +2.4\text{ V} > 0$ |
| `{{key:ENTER}} {{key:x>0}} {{key:×}} {{key:-}}` | 3.200000 | 3.200000 | 3.200000 | **5.000000** | Subtract $2.4 \times 1 = 2.4\text{ V}$; clamped $v_{\text{out}}(7.4) = \mathbf{5.0\text{ V}}$ |

### Visual Overlays (`SOLVE`, `∫`) & Bivariate Scatter Plots (`Σ+` $\to$ `PLOT`)

When invoked alongside numerical root-finding or Adaptive Romberg Quadrature (`{{key:∫}}` via `∫ f(x)` on `{{key:LFU3}}`, as illustrated in Chapter 8) {{cite:brent1973,romberg1955}}, the plotter shades the vertical area columns between $y = f(x)$ and $y = 0$. Likewise, plotting the Standard Normal density $f(z) = \frac{1}{\sqrt{2\pi}}e^{-z^2/2}$ over $Z \in [-3.5\sigma, +3.5\sigma]$ displays the symmetric Gaussian bell curve peaking at $f(0) = 0.3989422804$ with inflection points at $z = \pm 1.0\sigma$:

{{res:sc32_plot_normal_bell:screenshot|SC-32 Vector Plotter displaying the Standard Normal Bell Curve over [-3.5, +3.5].}}

When no active equation is selected and at least two statistical data pairs reside in the **50-point scatter ring buffer** (`{{key:SUMS}}` mode), pressing `{{key:PLOT}}` renders a bivariate scatter plot with linear, logarithmic, exponential, or power trendline overlays. For four piezoresistive pressure sensor calibration pairs—$(10\text{ kPa}, 1.25\text{ V}), (20\text{ kPa}, 2.45\text{ V}), (30\text{ kPa}, 3.80\text{ V}), (40\text{ kPa}, 4.95\text{ V})$—accumulating via `{{key:Σ+}}` and pressing `{{key:m}}` (and `{{key:PLOT}}` to inspect the scatter cloud against the regression line $y = 0.1245x + 0.0000$, $r = 0.999565$, $R^2 = 0.999130$) verifies linearity on the stack:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `{{key:CLEAR}} {{key:CLΣ}}` | 0.00 | 0.00 | 0.00 | 0.00 | Clear statistical accumulators |
| `1.25 {{key:ENTER}} 10 {{key:Σ+}}` | 0.00 | 0.00 | 1.25 | 1.00 | Pair 1: (10 kPa, 1.25 V); count n = 1 |
| `2.45 {{key:ENTER}} 20 {{key:Σ+}}` | 0.00 | 1.25 | 2.45 | 2.00 | Pair 2: (20 kPa, 2.45 V); count n = 2 |
| `3.80 {{key:ENTER}} 30 {{key:Σ+}}` | 1.25 | 2.45 | 3.80 | 3.00 | Pair 3: (30 kPa, 3.80 V); count n = 3 |
| `4.95 {{key:ENTER}} 40 {{key:Σ+}}` | 2.45 | 3.80 | 4.95 | 4.00 | Pair 4: (40 kPa, 4.95 V); count n = 4 |
| `{{key:m}}` | 2.45 | 3.80 | 4.95 | 0.1245 | Regression slope m = 0.124500 V/kPa |

---

### From Visual Curves into the Engineering Wild

With René Descartes's coordinate plane, Jack Bresenham's integer pixel rasterizer, and Francis Anscombe's scatter plots in hand, the foundational toolkit of *Thinking in the Stack* is complete. Look at the arc we have traveled across our first twelve chapters:
* **Chapters 1 and 2** gave us our physical instrument and our mental architecture: the 4-register operational stack ($X, Y, Z, T$), automatic stack lift, Register $T$ replication, `LASTX` argument recovery, and inside-out expression unpeeling.
* **Chapters 3, 4, and 5** unified the three great transcendental families of mathematics: continuous exponential growth and logarithms ($e^x, \ln x$), circular and hyperbolic trigonometry ($\cos\theta, \sin\theta, \cosh x$), and their marriage in the complex phasor plane ($e^{i\theta} = \cos\theta + i\sin\theta$).
* **Chapters 6, 7, 8, and 9** gave us the analytical engines of physical science: 2D and 3D mensuration, Horner polynomials and Richard Brent's root solver (`SOLVE`), numerical derivatives and Werner Romberg's $\frac{4}{3} - \frac{1}{3}$ quadrature (`∫`), and Carl Friedrich Gauss's least-squares statistics (`Σ+`, `L.R.`).
* **Chapters 10, 11, and 12** extended those tools to 36-bit binary computing, financial compounding (`TVM`), and interactive visual graphing (`PLOT`).

Up to this point, however, we have met each branch of mathematics inside its own dedicated chapter—studying logarithms in the logarithm chapter, vectors in the trigonometry chapter, buckling and centroids in the geometry chapter, and regression in the statistics chapter.

What happens when we step out of individual textbook compartments into the **real engineering wild**—where a single design problem on a laboratory workbench or factory floor crosses optics, precision machining tolerances, turbulent pipe flow, structural column buckling, heat-engine thermodynamics, concert-hall acoustics, and orbital mechanics all at once? We open the chief engineer's field notebook in **[Chapter 13: Six Equations That Run the Modern World: Cross-Disciplinary Engineering](13-applied-stem-case-studies.md)**.
