---
title: "Chapter 12: Analytic Geometry, Composite Areas & Integral Mensuration | Thinking in the Stack (SC-32)"
description: "From René Descartes's coordinate plane and Gauss's Shoelace polygon theorem to composite section and surface-area takeoffs via Σ+/Σ−, area-weighted centroids, definite-integral area (∫), and surfaces of revolution on the StackCalc SC-32."
---

# Chapter 12: Analytic Geometry, Composite Areas & Integral Mensuration

## René Descartes's Coordinate Plane, Gauss's Shoelace Theorem & Analytic Loci

### Algebraic Equations as Geometric Loci

During his years as a boarding student at the College of La Flèche in Anjou, René Descartes was granted an unusual privilege by the rector, Father Charlet: while his classmates rose at five o'clock every morning to recite Latin prayers in unheated stone halls, young René was allowed to remain warm under his blankets until late morning, thinking quietly with his eyes open.

Descartes kept that habit of morning meditation for the rest of his life. Observing the orthogonal grid of ceiling tiles and wall joints in his room—and investigating Pappus of Alexandria's classical locus problem—Descartes considered how to specify the exact position of a moving point on a flat plane at any instant, and how to measure the geometric region enclosed by its path.

He realized that if he measured the perpendicular distance $x$ from a horizontal reference axis and the perpendicular distance $y$ from a second reference axis, every position on the plane corresponded to a unique pair of numbers $(x, y)$. If the point moved along a straight diagonal line, a polygonal boundary, or a smooth parabolic arch, its two distances $x$ and $y$ obeyed a strict algebraic equation; conversely, *any* algebraic equation connecting $x$ and $y$ defined a geometric boundary across the plane whose intercepts, peaks, enclosed area, and surface of revolution could be calculated directly from its coordinates.

When Descartes published this discovery in 1637 as *La Géométrie* {{cite:descartes1637}}, an appendix to his *Discourse on the Method*, he ended a two-thousand-year separation that had divided mathematical thought since antiquity. Ancient Greek geometry, as practiced by Euclid, Archimedes, and Apollonius, was rich in spatial intuition with circles, triangles, parabolas, and tangent lines drawn by straightedge and compass, yet it possessed almost no symbolic algebra, so proving a new mensuration theorem required inventing a custom geometric dissection from scratch. Conversely, medieval and Renaissance algebra, developed by al-Khwarizmi, Tartaglia, Cardano, and Viète, provided a symbolic calculus for balancing unknowns ($x^2, x^3$), yet an equation sat on the page as an abstract string of characters divorced from spatial area and volume.

Descartes proved that algebra and geometry are two languages describing one underlying reality. John Stuart Mill later called analytic geometry *"the greatest single step ever made in the progress of the exact sciences,"* because it allowed every geometric boundary, cross-sectional area, and three-dimensional shell to be analyzed with the full precision of numerical algebra.

### Reading the Anatomy of a Boundary Curve: Roots, Peaks, Valleys & Inflection Points

Once a physical boundary or structural profile $y = f(x)$ is expressed across a horizontal abscissa $x$ and a vertical ordinate $y$, stored on the SC-32 inside the `{{key:EQN}}` bank (`{{key:↱}}` + `{{key:STO}}`) {{cite:hp32sii1991}}, every geometric landmark that bounds an enclosed area corresponds to an exact algebraic condition on $f(x)$ and its derivatives.

Hunting for the roots or zeros of a boundary equation means solving for the abscissas $x$ where $f(x) = 0$ via `{{key:SOLVE}}` {{cite:brent1973}}. In planar mensuration and integral calculus, a root is a shoreline where the profile crosses the reference axis ($y = 0$) and switches from negative elevation ($y < 0$, below the datum) to positive elevation ($y > 0$, above the datum). Whenever an engineer computes the total unsigned area between a wave or beam profile and the $x$-axis, locating the exact zero crossings first via `{{key:SOLVE}}` is essential so that positive lobes above the axis and negative lobes below the axis do not cancel each other out during integration.

Along a smooth boundary curve, the first derivative $f'(x)$ measures the local tangent slope: along a rising ramp, $f'(x) > 0$, and along a descending slope, $f'(x) < 0$. At the exact crown of an arch (*local maximum*) or the bottom of a sag trough (*local minimum*), the tangent line is momentarily horizontal ($f'(x) = 0$).

An *inflection point* marks a reversal in the sign of curvature along a structural profile, such as an S-shaped highway transition ramp or a reverse-curve viaduct arch modeled by a general cubic polynomial:

$$y(x) = a x^3 + b x^2 + c x + d, \qquad y''(x) = 6ax + 2b$$

Wherever the second derivative is negative ($y''(x) < 0$), the tangent slope decreases with $x$ and the arch bends downward (*concave down*); wherever the second derivative is positive ($y''(x) > 0$), the tangent slope increases with $x$ and the trough bends upward (*concave up*). At the unique abscissa $x_{\text{infl}} = -\frac{b}{3a}$ where $y''(x_{\text{infl}}) = 0$, the bending moment passes through zero as the profile reverses its direction of curvature, forming the exact geometric center of symmetry between the cubic's local peak and local valley.

Vertical and horizontal asymptotes govern the bounding envelopes of rational and exponential profiles. When a rational denominator approaches zero, such as the thin-lens magnification law $f(x) = \frac{1}{x - 2}$ as an object crosses the focal point $x = 2$, the ordinate diverges toward $\pm\infty$ along a *vertical asymptote*. Conversely, when a falling body approaches terminal velocity $v(t) = v_{\text{term}}\tanh(gt/v_{\text{term}})$, or when an uncharged capacitor charges through a resistor toward supply voltage $V_{\max}$ with RC time constant $\tau$:

$$V(t) = V_{\max}\!\left(1 - e^{-t/\tau}\right)$$

the profile approaches a flat horizontal ceiling—a *horizontal asymptote* at $V = V_{\max}$ as $t \to \infty$—and the area trapped *between* the charging curve and that horizontal ceiling, $\int_0^\infty [V_{\max} - V(t)]\,dt = V_{\max}\tau$, measures the total magnetic flux-linkage or charge deficit required to reach steady state.

### Carl Friedrich Gauss's Shoelace Theorem & the Trapezoidal Surveyor's Ledger

Before turning to curved boundaries that require integral calculus, Descartes's coordinate plane provides an exact algebraic method for computing the area of *any* flat polygon—however irregular—directly from the $(x_k, y_k)$ coordinates of its corners.

Suppose a civil engineer or land surveyor records the $n$ boundary monuments $(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)$ in order around the perimeter of a polygonal parcel, closing the loop back to $(x_{n+1}, y_{n+1}) = (x_1, y_1)$ (whether counterclockwise in math coordinates $(x, y)$ or clockwise in surveyor coordinates $(N, E)$, since taking the absolute value $|A|$ at the end makes the area invariant to traversal direction). As Carl Friedrich Gauss formalized in his geodetic survey lectures, dropping vertical plumb lines from each boundary segment $(x_k, y_k) \to (x_{k+1}, y_{k+1})$ down to the $x$-axis partitions the parcel into a signed ring of vertical trapezoids of width $\Delta x_k = x_k - x_{k+1}$ and mean altitude $\bar{y}_k = \frac{1}{2}(y_k + y_{k+1})$. Expanding and canceling the symmetric $x_k y_k$ terms yields *Gauss's Shoelace Formula* (also known as Meister's 1769 determinant formula):

$$A = \frac{1}{2}\left|\sum_{k=1}^{n} \left(x_k y_{k+1} - x_{k+1} y_k\right)\right| = \frac{1}{2}\left|\sum_{k=1}^{n} (x_k - x_{k+1})(y_k + y_{k+1})\right|$$

Both expressions evaluate cleanly on the SC-32 by coupling the 4-register stack to the statistical accumulator `{{key:Σ+}}` (and `{{key:Σ-}}`). For each directed edge from vertex $k$ to vertex $k+1$, you form the $2 \times 2$ cross-product $x_k y_{k+1} - x_{k+1} y_k$ (or the doubled trapezoid $(x_k - x_{k+1})(y_k + y_{k+1})$) on Registers $Y$ and $X$ and press `{{key:Σ+}}`. Register $X$ increments the edge counter $n = 1, 2, \dots, N$ so you never lose your place along the survey traverse, and pressing `{{key:SUMS}}` $\to$ `{{key:Σx}}` followed by `2 {{key:÷}} {{key:ABS}}` delivers the exact enclosed area of the polygon.

---

## Composite Shapes, Cutout Apertures & Surface Area Takeoffs in `STAT` Mode

### Additive and Subtractive Dissection of Composite Cross-Sections (`Σ+` and `Σ−`)

In structural, mechanical, and architectural engineering, real-world cross-sections and three-dimensional enclosures are rarely single textbook primitives. A bridge gusset plate, an aircraft bulkhead rib, or a cast-aluminum gearbox housing is a *composite region* built by welding or extruding simple outer shapes (rectangles, right triangles, trapezoids, circular sectors, and parabolic spandrels) and then milling out interior lightening holes, bolt bores, and cooling slots.

Rather than writing down intermediate sub-areas on scrap paper—which invites transcription errors and rounding drift—the SC-32's statistical registers (`{{key:Σ+}}`, `{{key:Σ-}}`, and `{{key:SUMS}}`) act as an dedicated *additive and subtractive mensuration ledger*:

1. **Zero the Ledger (`{{key:CLΣ}}`):** Press `{{key:↰}}` + `{{key:Σ+}}` (`{{key:CLΣ}}`) to clear all six statistical registers ($\Sigma x = \Sigma y = \Sigma x^2 = \Sigma y^2 = \Sigma xy = n = 0$).
2. **Accumulate Solid Sub-Regions (`{{key:Σ+}}`):** Evaluate the area $A_k$ of each positive sub-shape (or the surface area of each exterior wall group) in Register $X$ and press `{{key:Σ+}}`. The calculator adds $A_k$ into $\Sigma x$ at full 15-digit internal precision and displays the running feature count $n = 1, 2, 3, \dots$ in Register $X$.
3. **Deduct Cutouts, Bores & Apertures (`{{key:Σ-}}`):** Whenever a blueprint specifies a drilled bolt circle, a rectangular inspection window, or a chamfered corner cutout, evaluate its positive area $A_{\text{cutout}}$ in Register $X$ and press Left Shift `{{key:↰}}` + `{{key:Σ+}}` (`{{key:Σ-}}` via the primary `Σ-` shifted key, or negate with `{{key:+/-}}` before `{{key:Σ+}}`). Using `{{key:Σ-}}` subtracts $A_{\text{cutout}}$ directly from $\Sigma x$ (and decrements $n$), whereas using `{{key:+/-}} {{key:Σ+}}` subtracts the cutout area from $\Sigma x$ while *incrementing* the audited feature count $n$ so that $n$ equals the total number of blueprint features verified.
4. **Recall Net Area & Convert to Mass or Coating Volume (`{{key:SUMS}}` $\to$ `{{key:Σx}}`):** Press Right Shift `{{key:↱}}` + `{{key:Σ+}}` (`{{key:SUMS}}`) and tap softkey `{{key:Σx}}` (`{{key:LFU0}}`) to place the net composite area $A_{\text{net}} = \sum A_{\text{solid}} - \sum A_{\text{cutout}}$ onto Register $X$, ready to multiply by plate thickness $t$ and material density $\rho$ for structural mass, or by paint/anodizing film thickness for surface treatment takeoffs.

{{blocks:sc32_concept_composite_area_integral|Composite plate and cutout dissection via Σ+ / Σ− and x̄w paired with continuous definite-integral area between curves via SOLVE and ∫.}}

### Simultaneous Net Area & Composite Centroid Auditing (`Σy` and `x̄w`)

When designing an eccentric machine bracket, a retaining wall cross-section, or a ship's hull frame, knowing the total cross-sectional area $A_{\text{net}}$ is only half the problem: you must also locate the *area centroid* $(\bar{x}, \bar{y})$ through which the resultant axial load or hydrostatic force acts, and about which the section's bending stiffness (second moment of area $I = \sum (I_{c,k} + A_k d_k^2)$) is referenced.

Because `{{key:Σ+}}` is a *bivariate* accumulator that processes Register $Y$ and Register $X$ together, the SC-32 can compute **both the net composite area and the exact composite centroid in a single pass** without typing a single sub-area twice:

$$\bar{x} = \frac{\sum_{k=1}^{m} A_k x_k}{\sum_{k=1}^{m} A_k} = \frac{\Sigma xy}{\Sigma y}, \qquad A_{\text{net}} = \sum_{k=1}^{m} A_k = \Sigma y$$

Here is how the two-register mapping works on the stack:
* For each solid sub-shape $k$, place its **area weight $A_k$ in Register $Y$** and its **centroid coordinate $x_k$ in Register $X$** (`A_k {{key:ENTER}} x_k {{key:Σ+}}`), since the SC-32's weighted mean `{{key:x̄w}}` divides $\Sigma xy / \Sigma y$ using Register $Y$ as the weight and Register $X$ as the coordinate.
* For a cutout hole or slot of area $A_{\text{hole}}$ centered at $x_{\text{hole}}$, either place the negative area $-A_{\text{hole}}$ (`{{key:+/-}}`) in Register $Y$ and $x_{\text{hole}}$ in Register $X$ before pressing `{{key:Σ+}}`, or place $+A_{\text{hole}}$ in Register $Y$ and $x_{\text{hole}}$ in Register $X$ and press `{{key:Σ-}}`! Both paths subtract $A_{\text{hole}}$ from $\Sigma y$ and subtract the cutout's first moment $A_{\text{hole}} x_{\text{hole}}$ from $\Sigma xy$.
* When all sub-shapes and cutouts have been logged:
  1. Open `{{key:SUMS}}` (`{{key:↱}}` + `{{key:Σ+}}`) and tap **`{{key:Σy}}` (`{{key:LFU1}}`)** to recall the **net composite area $A_{\text{net}} = \sum A_k$** into Register $X$.
  2. Open `{{key:SUMS}}` and tap **`{{key:Σxy}}` (`{{key:LFU4}}`)** if you need the raw **first moment of area $Q = \sum A_k x_k$** (used in beam shear-flow formula $\tau = \frac{VQ}{It}$).
  3. Open `{{key:x̄,ȳ}}` (`{{key:↱}}` + `{{key:yˣ}}`) and tap **`{{key:x̄w}}` (`{{key:LFU2}}`)** to compute the **composite centroid $\bar{x} = \frac{\Sigma xy}{\Sigma y}$** in a single keystroke!

### Classical Composite Primitives & Archimedes' Parabolic Spandrels

To dissect curved as well as polygonal plates using `{{key:Σ+}}` and `{{key:Σ-}}`, Table 12.1 catalogs the exact area $A$ and centroid coordinates $(\bar{x}, \bar{y})$ of the fundamental engineering sub-regions (including Archimedes' $\frac{2}{3}bh$ parabolic arch and its complementary $\frac{1}{3}bh$ parabolic spandrel, which allow curved architectural fillets and streamlined fairings to be audited inside `STAT` mode alongside rectangles and circles):

| Sub-Region Primitive | Enclosed Area $A$ | Centroid Location $(\bar{x}, \bar{y})$ | Mensuration Rule & Stack Entry Idiom |
| :--- | :--- | :--- | :--- |
| **Rectangle ($b \times h$)** | $A = b h$ | $\left(\frac{b}{2},\; \frac{h}{2}\right)$ | From corner origin; `b ENTER h ×` |
| **Right Triangle ($b \times h$)** | $A = \frac{1}{2} b h$ | $\left(\frac{b}{3},\; \frac{h}{3}\right)$ | One-third of leg lengths from the $90^\circ$ corner |
| **Trapezoid ($a \parallel b$, height $h$)** | $A = \frac{a + b}{2} h$ | $\bar{y} = \frac{h}{3}\left(\frac{2a + b}{a + b}\right)$ | Height above base $b$ (where $a$ is top width) |
| **Full Circle / Bore ($r$)** | $A = \pi r^2$ | $(x_c,\; y_c)$ | Deduct drilled bores via `r x² π × Σ-` |
| **Semicircle (radius $r$)** | $A = \frac{1}{2}\pi r^2$ | $\bar{y} = \frac{4r}{3\pi} \approx 0.424413\,r$ | Measured perpendicular from flat diameter base |
| **Quarter-Circle Fillet ($r$)** | $A = \frac{1}{4}\pi r^2$ | $\bar{x} = \bar{y} = \frac{4r}{3\pi} \approx 0.424413\,r$ | Measured from the two orthogonal straight radii |
| **Circular Sector (angle $2\alpha$ rad)** | $A = \alpha r^2$ | $\bar{x} = \frac{2r\sin\alpha}{3\alpha}$ | Along symmetry bisector from vertex ($\alpha$ in rad) |
| **Parabolic Arch ($y = h(1 - x^2/b^2),\; x \in [-b,b]$)** | $A = \frac{2}{3} (2b) h$ | $\bar{y} = \frac{2}{5} h = 0.4000\,h$ | Archimedes' $\frac{2}{3}$ rule across full span $2b$ |
| **Parabolic Spandrel ($y = \frac{h}{b^2}x^2$)** | $A = \frac{1}{3} b h$ | $\left(\frac{3}{4}b,\; \frac{3}{10}h\right)$ | Complementary corner fillet outside a parabola |

### Francis Anscombe's 1973 Quartet: Auditing `Σ+` Residuals on the Stack

The same six statistical registers ($\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$) that accumulate composite areas and centroids also drive Carl Friedrich Gauss's method of least squares (`{{key:L.R.}}` above `{{key:LN}}`). When an engineer feeds $(x_i, y_i)$ calibration pairs—such as surface area versus convective heat dissipation, or pressure versus transducer voltage—into `{{key:Σ+}}`, the `{{key:L.R.}}` menu distills the cloud into the linear regression slope $m$ (`{{key:m}}`), vertical intercept $b$ (`{{key:b}}`), and Karl Pearson's correlation coefficient $r$ (`{{key:r}}`).

In 1973, British statistician Francis John Anscombe, founder of Yale University's Department of Statistics, published a landmark paper in *The American Statistician* titled *"Graphs in Statistical Analysis"* demonstrating why an analyst must never accept $m, b,$ and $r$ blindly without auditing the individual data residuals. Anscombe constructed four small datasets (*Anscombe's Quartet*), each consisting of $n = 11$ coordinate pairs $(x_i, y_i)$, whose summary statistics are identical to three decimal places:

| Statistical Metric | Dataset I | Dataset II | Dataset III | Dataset IV |
| :--- | :---: | :---: | :---: | :---: |
| **Sample Size ($n$)** | $11$ | $11$ | $11$ | $11$ |
| **Mean of $x$ ($\bar{x}$) & Variance ($s_x^2$)** | $\bar{x} = 9.0,\; s_x^2 = 11.0$ | $\bar{x} = 9.0,\; s_x^2 = 11.0$ | $\bar{x} = 9.0,\; s_x^2 = 11.0$ | $\bar{x} = 9.0,\; s_x^2 = 11.0$ |
| **Mean of $y$ ($\bar{y}$) & Variance ($s_y^2$)** | $\bar{y} = 7.50,\; s_y^2 = 4.125$ | $\bar{y} = 7.50,\; s_y^2 = 4.125$ | $\bar{y} = 7.50,\; s_y^2 = 4.125$ | $\bar{y} = 7.50,\; s_y^2 = 4.125$ |
| **Least-Squares Line ($\hat{y} = m x + b$)** | $\hat{y} = 0.500x + 3.00$ | $\hat{y} = 0.500x + 3.00$ | $\hat{y} = 0.500x + 3.00$ | $\hat{y} = 0.500x + 3.00$ |
| **Correlation ($r$) & Determination ($R^2$)** | $r = 0.816,\; R^2 = 0.667$ | $r = 0.816,\; R^2 = 0.667$ | $r = 0.816,\; R^2 = 0.667$ | $r = 0.816,\; R^2 = 0.667$ |

Despite sharing $\hat{y} = 0.500x + 3.00$ and $r = 0.816$, the four datasets represent completely different physical mechanisms:
* **Dataset I (Genuine Noisy Linear Trend):** Eleven measurements scattered naturally around a straight line, with small, unpatterned residuals $e_i = y_i - \hat{y}(x_i)$ of alternating sign across the domain.
* **Dataset II (Smooth Quadratic Parabola):** A noiseless parabolic arch $y = -0.125x^2 + 2.75x - 6.00$ that rises to a peak at $x = 11.0$ ($y = 9.13$) and bends back down at $x = 14.0$ ($y = 8.10$).
* **Dataset III (Exact Line Plus One Corrupted Outlier):** Ten points lying on a tight straight line of slope $m = 0.345$, plus a single corrupted sensor reading at $(13.0, 12.74)$ that wrenches the least-squares slope up to $0.500$.
* **Dataset IV (Vertical Cluster Plus One Leverage Point):** Ten points stacked vertically at $x = 8.0$ with zero correlation, plus one isolated point at $(19.0, 12.50)$ that single-handedly fabricates $r = 0.816$.

On a non-graphing scientific instrument like the SC-32, you unmask all three pathologies in seconds using a **Three-Point Stack Residual Audit** via `{{key:L.R.}}` $\to$ `{{key:ŷ}}` (`{{key:LFU0}}`) and `{{key:REGS}}` (`{{key:↰}}` + `{{key:0}}`, `DATA` tab):
1. **Check the Endpoints and Midpoint via `{{key:ŷ}}`:** After accumulating your pairs with `{{key:Σ+}}`, evaluate the linear prediction $\hat{y}$ at the left endpoint ($x = 4$), the midpoint ($x = 11$), and the right endpoint ($x = 14$) by keying `x {{key:L.R.}} {{key:ŷ}}` and subtracting from the measured $y_i$. In Dataset II, the residuals $e_i = y_i - \hat{y}_i$ at $x = (4, 11, 14)$ follow a systematic **negative–positive–negative arch** ($-1.89, +0.63, -1.90$), immediately diagnosing concave-down quadratic curvature ($y''(x) < 0$) without drawing a single pixel!
2. **Test Log/Power Linearization or Remove a Suspect Outlier via `{{key:Σ-}}`:** In Dataset III, inspecting the raw pairs in the `DATA` tab of `{{key:REGS}}` (indirect slots `40`–`89`) spots the spike at $(13.0, 12.74)$. Keying `12.74 {{key:ENTER}} 13 {{key:Σ-}}` removes that single corrupted pair from the accumulators in place, and tapping `{{key:L.R.}}` $\to$ `{{key:r}}` watches the correlation jump from $r = 0.816$ to **$r = 0.99999$**, proving that the remaining ten measurements obey a pure linear law.

---

## Tying Definite Integration (`∫`) to Planar Area, Cross-Sections & Surface Area of Revolution

### From Discrete `Σ+` Sums to Continuous Romberg Quadrature (`∫`)

Whereas `{{key:Σ+}}` and `{{key:Σ-}}` sum the areas of discrete polygons, circles, and parabolic spandrels, continuous boundaries—such as hydrofoil ribs, sinusoidal corrugated roofing, Gaussian probability bells, and exponentially flared horn reflectors—require summing infinitely many infinitesimal vertical strips of width $dx$.

As established in Chapter 8, Werner Romberg's adaptive quadrature engine (`{{key:∫}}`, Right Shift `{{key:↱}}` above `{{key:8}}`) {{cite:romberg1955,kahan1979}} automates this transition from discrete summation to continuous mensuration:
1. Store the boundary profile $f(x)$ in the `{{key:EQN}}` bank (`{{key:↱}}` + `{{key:STO}}`) as a pure RPN token stream, and press `{{key:ENTER}}` (or `{{key:XEQ}}` / `FN=` if selecting from multiple equations).
2. Stage the lower abscissa bound $a$ in Register $Y$ and the upper abscissa bound $b$ in Register $X$ via `a {{key:ENTER}} b`.
3. Press `{{key:∫}}` and tap the dummy variable softkey (`X`, `T`, etc.). Upon convergence, the SC-32 places the **certified area $A = \int_a^b f(x)\,dx$ in Register $X$** and the **uncertainty bound $\pm\varepsilon$ in Register $Y$**, while leaving Registers $Z$ and $T$ completely untouched!

Because Registers $Z$ and $T$ are preserved across every `{{key:∫}}` execution, you can **combine discrete geometric areas and continuous integrals directly on the stack or inside `{{key:Σ+}}`**: evaluate a curved fairing or arch area via `a {{key:ENTER}} b {{key:∫}} X`, press `{{key:Σ+}}` to log that curved area into $\Sigma x$, and then add rectangular base plates or deduct circular bolt holes via `{{key:Σ-}}` in the very same statistical ledger!

### Area Between Intersecting Curves & Root-Bracketed Mensuration (`SOLVE` $\to$ `∫`)

When a planar cross-section is bounded above by an upper curve $y_{\text{upper}} = f(x)$ and below by a lower chord or curve $y_{\text{lower}} = g(x)$—such as a crescent-shaped turbine blade profile, a meniscus lens cross-section, or an arched masonry rib over a sloped ramp—the vertical height of the strip at any abscissa $x$ is the difference $h(x) = f(x) - g(x)$. The net enclosed area between their intersection points $x_1$ and $x_2$ is:

$$A = \int_{x_1}^{x_2} \bigl[f(x) - g(x)\bigr]\,dx$$

Notice that the integrand $h(x) = f(x) - g(x)$ serves a **dual role** on the SC-32:
1. **The Intersection Condition ($h(x) = 0$):** At the left and right corners where the upper and lower curves meet, their vertical separation vanishes: $f(x) - g(x) = 0$.
2. **The Area Integrand ($\int h(x)\,dx$):** Between those two corners, integrating that *exact same equation* $h(x) = f(x) - g(x)$ accumulates the enclosed cross-sectional area!

This duality creates a closed **Solve-then-Integrate workflow** using a single `{{key:EQN}}` entry:
* **Step 1 (Define the Difference Profile once in `{{key:EQN}}`):** Enter $h(x) = f(x) - g(x)$ into `{{key:EQN}}`. For example, to find the area trapped between the parabolic arch $f(x) = 4x - x^2$ and the inclined chord $g(x) = 0.5x$ (shown in Panel B of the concept diagram above), enter $h(x) = 4x - x^2 - 0.5x = 3.5x - x^2$ in Horner RPN form as `3.5 X - X ×`.
* **Step 2 (Find the Intersection Bounds via `{{key:SOLVE}}`):** The left intersection sits at the origin $x_1 = 0$. To find the right intersection $x_2$ near `[3, 4]`, key `3 {{key:ENTER}} 4 {{key:SOLVE}} X`, which refines the exact intersection root $x_2 = \mathbf{3.500000}$ into Register $X$.
* **Step 3 (Integrate Across the Exact Root via `{{key:x⇄y}}` and `{{key:∫}}`):** With $x_2 = 3.500000$ already sitting in Register $X$, simply key `0 {{key:x⇄y}} {{key:∫}} X` to place $(Y = 0,\; X = 3.5)$ on the stack and integrate the *same* active equation $3.5x - x^2$ from $0$ to $3.5$. Romberg's first Simpson column $R(1,1)$ returns the exact enclosed area:

$$A = \int_0^{3.5} \left(3.5x - x^2\right)dx = \left[\frac{3.5}{2}x^2 - \frac{1}{3}x^3\right]_0^{3.5} = \frac{3.5^3}{6} = \frac{343}{48} \approx \mathbf{7.145833}$$

And if you press `{{key:FDISP}}` (`{{key:↰}}` + `{{key:.}}`), the SC-32 reduces `7.1458333333` into the exact rational fraction **`7 7/48`** ($\frac{343}{48}$)!

### Arc Length & Surface Area of Revolution via `∫`

Integral calculus also extends Chapter 6's solid mensuration formulas to the **arc length $L$** and **3D surface area of revolution $S$** of any smooth profile $y = f(x)$ over $x \in [a, b]$.

When a curve $y = f(x)$ steps horizontally by $dx$ and rises vertically by $dy = f'(x)\,dx$, the Pythagorean theorem gives the infinitesimal chord length $ds = \sqrt{dx^2 + dy^2} = \sqrt{1 + [f'(x)]^2}\,dx$. Revolving that infinitesimal arc segment $ds$ around the $x$-axis sweeps out a thin conical frustum ribbon of radius $y = f(x)$, circumference $2\pi f(x)$, and slant width $ds$, whose lateral surface area is $dS = 2\pi f(x)\,ds$. Integrating from $x = a$ to $x = b$ yields the two classic integral mensuration formulas of Huygens, Leibniz, and Euler:

$$L = \int_a^b \sqrt{1 + \bigl[f'(x)\bigr]^2}\,dx, \qquad S_{\text{rev}} = 2\pi \int_a^b f(x)\sqrt{1 + \bigl[f'(x)\bigr]^2}\,dx$$

Similarly, if a planar profile $y = f(x)$ is revolved around the *vertical* $y$-axis over radius $x \in [a, b]$ (such as a parabolic microwave dish antenna $z(r) = \frac{r^2}{4F}$ of focal length $F$ and aperture radius $R$, where $z'(r) = \frac{r}{2F}$), each concentric ring at radius $r$ has circumference $2\pi r$ and slant width $ds = \sqrt{1 + (r/2F)^2}\,dr$:

$$S_{\text{dish}} = 2\pi \int_0^R r\sqrt{1 + \left(\frac{r}{2F}\right)^2}\,dr = \frac{8\pi F^2}{3}\left[\left(1 + \frac{R^2}{4F^2}\right)^{3/2} - 1\right]$$

By storing the integrand $r\sqrt{1 + [z'(r)]^2}$ in `{{key:EQN}}`, running `a {{key:ENTER}} b {{key:∫}} R`, and multiplying the resulting integral in Register $X$ by `2 {{key:×}} {{key:π}} {{key:×}}`, you can compute the exact 3D surface area of arbitrary aerodynamic nose cones, hyperbolic cooling towers, bell nozzles, and catenary domes that have no elementary closed-form formula.

---

## Worked Stack Traces: Composite Area Ledgers, Curve Profiles & Integral Mensuration

### Composite Structural Gusset Plate with Cutout Bore (`Σ+`, `Σ−`, and `x̄w`)

Consider the composite steel structural gusset plate illustrated in Panel A of our concept diagram:
* **Sub-region 1 (Base Rectangle):** Width $b_1 = 120.0\text{ mm}$, height $h_1 = 80.0\text{ mm}$ ($x \in [0, 120],\ y \in [0, 80]$), with area $A_1 = 120 \times 80 = 9,600.0\text{ mm}^2$ and centroid at $x_1 = 60.0\text{ mm}$.
* **Sub-region 2 (Triangular Nose):** Right triangle extending from $x = 120.0\text{ mm}$ to $x = 180.0\text{ mm}$ (base $b_2 = 60.0\text{ mm}$, height $h_2 = 80.0\text{ mm}$), with area $A_2 = \frac{1}{2}(60)(80) = 2,400.0\text{ mm}^2$ and centroid one-third of its base from the $x = 120\text{ mm}$ weld line: $x_2 = 120 + \frac{60}{3} = 140.0\text{ mm}$.
* **Sub-region 3 (Drilled Bolt Bore Cutout):** Circular hole of radius $r = 20.0\text{ mm}$ centered at $x_3 = 50.0\text{ mm}$, removing area $A_3 = \pi (20^2) = 400\pi \approx 1,256.637061\text{ mm}^2$.

To tally the **net surface area of one face** ($A_{\text{net}} = A_1 + A_2 - A_3 = 12,000 - 400\pi = \mathbf{10,743.362939\text{ mm}^2}$) using the univariate `{{key:Σ+}}` / `{{key:Σ-}}` ledger, clear the statistical registers with `{{key:CLΣ}}`, add the rectangle and triangle with `{{key:Σ+}}`, deduct the circular bore with `{{key:Σ-}}`, and recall `{{key:SUMS}}` $\to$ `{{key:Σx}}`. Because `{{key:Σ+}}` and `{{key:Σ-}}` disarm stack lift after displaying the count $n$ in Register $X$, typing the first dimension of the next sub-shape overwrites $n$ in place so Registers $Y, Z,$ and $T$ stay at zero throughout the entire takeoff:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `{{key:CLEAR}} {{key:CLΣ}}` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | Zero all 6 statistical accumulators ($\Sigma x = 0, n = 0$) |
| `120 {{key:ENTER}} 80 {{key:×}} {{key:Σ+}}` | 0.000000 | 0.000000 | 0.000000 | 1.000000 | Add rectangle $A_1 = 9,600\text{ mm}^2$ into $\Sigma x$; $n = 1$ (lift disarmed) |
| `60 {{key:ENTER}} 80 {{key:×}} 2 {{key:÷}} {{key:Σ+}}` | 0.000000 | 0.000000 | 0.000000 | 2.000000 | Overwrite $n=1$; add triangle $A_2 = 2,400\text{ mm}^2$ ($\Sigma x = 12,000$); $n = 2$ |
| `20 {{key:x²}} {{key:π}} {{key:×}} {{key:Σ-}}` | 0.000000 | 0.000000 | 0.000000 | 1.000000 | Overwrite $n=2$; deduct bore $A_3 = 400\pi = 1,256.637061\text{ mm}^2$ from $\Sigma x$ |
| `{{key:SUMS}} {{key:Σx}}` | 0.000000 | 0.000000 | 0.000000 | **10743.362939** | Recall net composite plate area $A_{\text{net}} = 10,743.3629\text{ mm}^2$ |

Now watch how the **bivariate weighted-centroid method** (`A_k {{key:ENTER}} x_k {{key:Σ+}}`) computes *both* that same net area $A_{\text{net}} = 10,743.3629\text{ mm}^2$ (in $\Sigma y$) and the exact horizontal balance point $\bar{x} = \frac{9600(60) + 2400(140) - 400\pi(50)}{10743.362939} = \frac{849,168.1469}{10,743.362939} = \mathbf{79.041186\text{ mm}}$ (via `{{key:x̄,ȳ}}` $\to$ `{{key:x̄w}}`):
1. Clear `{{key:CLΣ}}`, then log the rectangle: `9600 {{key:ENTER}} 60 {{key:Σ+}}` ($n = 1$).
2. Log the triangular nose: `2400 {{key:ENTER}} 140 {{key:Σ+}}` ($n = 2$).
3. Log the circular bore cutout centered at $x_3 = 50\text{ mm}$: `20 {{key:x²}} {{key:π}} {{key:×}} 50 {{key:Σ-}}`.
4. Tap `{{key:x̄,ȳ}}` $\to$ `{{key:x̄w}}` (`{{key:LFU2}}`) to read the exact composite centroid $\bar{x} = \mathbf{79.041186\text{ mm}}$, and tap `{{key:SUMS}}` $\to$ `{{key:Σy}}` (`{{key:LFU1}}`) to read the net area $A_{\text{net}} = \mathbf{10,743.362939\text{ mm}^2}$!

### Evaluating Cubic Arch Inflections, Harmonic Series, Damped Envelopes & `sinc` Lobes

When analyzing continuous engineering profiles—whether computing ordinances along an arch, verifying integrands before pressing `{{key:∫}}`, or evaluating peak heights at critical points—Horner's nested form and `{{key:LASTX}}` keep every calculation inside the 4-register stack without scratchpad variables.

First, when laying out equally spaced suspension-bridge hanger stations, CNC toolpath passes, or trapezoidal integration nodes across an interval $[X_{\min}, X_{\max}]$ partitioned into $N - 1$ equal panels:

$$x_k = X_{\min} + k \left(\frac{X_{\max} - X_{\min}}{N - 1}\right), \qquad k = 0, 1, \dots, N - 1$$

Because each arithmetic step in $x_k = X_{\min} + k\frac{X_{\max} - X_{\min}}{N - 1}$ transforms a single scalar in place—from total span to panel width to horizontal displacement to world coordinate—the entire calculation executes inside Register $X$ while Registers $Y$, $Z$, and $T$ remain at zero. Across a $64\text{-point}$ ($N - 1 = 63$) domain spanning $[-3.0, +3.0]$ at station $k = 21$ (one-third of the span from the left boundary), keying `3 {{key:ENTER}} 3 {{key:+/-}} {{key:-}}` computes the total span $X_{\max} - X_{\min} = 6.000000$ in Register $X$. Dividing by `63 {{key:÷}}` forms the panel width $\Delta x = 6.0 / 63 \approx 0.095238$, scaling by `21 {{key:×}}` advances $k \cdot \Delta x = 2.000000$ units rightward, and adding the left boundary via `3 {{key:+/-}} {{key:+}}` lands at the exact abscissa $x_{21} = -1.000000$.

Second, take the cubic highway S-curve profile $y(x) = x^3 - 6x^2 + 9x + 2$ spanning $x \in [0, 4]$: its local maximum rises to $(1, 6)$, its local minimum dips to $(3, 2)$, and its inflection point ($y''(x) = 6x - 12 = 0$) sits midway between them at $x = 2$. Because a cubic polynomial is odd-symmetric around its inflection point $(x_{\text{infl}}, y_{\text{infl}}) = (2, 4)$, the area under $y(x)$ across any interval symmetric about $x = 2$ (such as $[0, 4]$) equals the base width $4.0$ multiplied by the inflection ordinate $y(2) = 4.0$ ($\int_0^4 (x^3 - 6x^2 + 9x + 2)\,dx = 4 \times 4 = 16.000000$). Writing $y(x)$ in nested Horner form $y(x) = ((x - 6)x + 9)x + 2$ and pre-filling the 4-level stack evaluates that inflection ordinate ($X = 4.000000$) with `2` typed only once:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `2 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}` | 2.000000 | 2.000000 | 2.000000 | 2.000000 | Flood all four stack registers with inflection abscissa $x = 2.0$ |
| `6 {{key:-}}` | 2.000000 | 2.000000 | 2.000000 | -4.000000 | Innermost Horner factor $x - 6 = -4.0$; Register $T$ replicates $2.0$ |
| `{{key:×}} 9 {{key:+}}` | 2.000000 | 2.000000 | 2.000000 | 1.000000 | Second Horner stage $(x - 6)x + 9 = 1.0$; $x = 2.0$ drops into $Y$ |
| `{{key:×}} 2 {{key:+}}` | 2.000000 | 2.000000 | 2.000000 | 4.000000 | Inflection point ordinate $y(2) = ((x - 6)x + 9)x + 2 = 4.000000$ |

Third, four classical periodic and decaying waveforms illustrate how ordinate verification on the stack pairs with definite-integral area (`{{key:∫}}`):

* **Joseph Fourier's Odd-Harmonic Square Wave Synthesis:** When Jean-Baptiste Joseph Fourier announced in 1807 that a flat-topped square wave of height $\frac{\pi}{4}$ could be synthesized by summing smooth odd-harmonic sine waves:

$$y_K(t) = \sum_{m=1}^{K} \frac{\sin((2m - 1)t)}{2m - 1} = \sin(t) + \frac{1}{3}\sin(3t) + \frac{1}{5}\sin(5t) + \cdots$$

each odd harmonic $\frac{1}{2m-1}\sin((2m-1)t)$ contributes positive half-cycle area $\int_0^\pi \frac{\sin((2m-1)t)}{2m-1}\,dt = \frac{2}{(2m-1)^2}$, summing across all odd integers to Euler's $\sum_{m=1}^\infty \frac{2}{(2m-1)^2} = \frac{\pi^2}{4}$ (matching the rectangle $\pi \times \frac{\pi}{4}$). At the midpoint of the plateau ($t = 90.0^\circ = \pi/2$), successive odd harmonics alternate in sign ($+1 - \frac{1}{3} + \frac{1}{5} - \cdots \to \frac{\pi}{4}$). Evaluating the three-harmonic plateau ordinate at $t = 90.0^\circ$ on the stack via `{{res:sc32_12_plot_01:keys}}` needs only Registers $Y$ and $X$ while $Z$ and $T$ stay at zero: the fundamental crest $\sin(90^\circ) = +1.000000$ sits in Register $Y$ while the third-harmonic trough $\frac{1}{3}\sin(270^\circ) = -0.333333$ forms in Register $X$ and folds down to $0.666667$, after which adding $+\frac{1}{5}\sin(450^\circ) = +0.200000$ lifts the plateau center to `{{res:sc32_12_plot_01:value}}`.
* **Underdamped Mechanical Ringdown Envelope:** When an underdamped sports suspension $x(t) = e^{-\zeta\omega_n t}\cos(\omega_d t) = e^{-0.60 t} \cos(3.9546 t)$ ($\zeta = 0.15, \omega_n = 4.0\text{ rad/s}, \omega_d = 3.9546\text{ rad/s}$) responds to a step impulse in Radians mode (`{{key:RAD}}`), evaluating the instantaneous displacement at $t = 1.0\text{ s}$ via `{{res:sc32_12_plot_02:keys}}` yields `{{res:sc32_12_plot_02:value}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `1 {{key:ENTER}} .60 {{key:×}}` | 0.00 | 0.00 | 0.00 | 0.600000 | Damping exponent $\zeta \omega_n t = 0.600000$ at $t = 1.0\text{ s}$ |
| `{{key:+/-}} {{key:eˣ}}` | 0.00 | 0.00 | 0.00 | 0.548812 | Exponential decay envelope $e^{-0.60} = 0.548812$ |
| `1 {{key:ENTER}}` | 0.00 | 0.548812 | 1.000000 | 1.000000 | Stage time $t = 1.0\text{ s}$ for oscillatory phase; envelope lifts to Z |
| `3.9546 {{key:×}}` | 0.00 | 0.00 | 0.548812 | 3.954600 | Damped phase angle $\omega_d t = 3.954600\text{ rad}$; envelope drops to Y |
| `{{key:COS}}` | 0.00 | 0.00 | 0.548812 | -0.687229 | Cosine carrier $\cos(3.9546\text{ rad}) = -0.687229$ |
| `{{key:×}}` | 0.00 | 0.00 | 0.00 | -0.377160 | Instantaneous suspension displacement $x(1.0) = -0.377160\text{ m}$ |

* **Fraunhofer Single-Slit Diffraction `sinc` Function ($y(x) = \frac{\sin x}{x}$):** In physical optics, coherent light passing through a narrow slit produces the amplitude profile $y(x) = \frac{\sin x}{x}$, with a central principal maximum $\lim_{x \to 0}\frac{\sin x}{x} = 1$ and side lobes that cross zero at every non-zero multiple of $\pi$ (enclosing the Sine Integral area $\operatorname{Si}(\pi) = \int_0^\pi \frac{\sin x}{x}\,dx \approx 1.851937052$, evaluated via `0.000001 {{key:ENTER}} {{key:π}} {{key:∫}} X`). Evaluating the half-lobe ordinate at $x = \pi/2$ in Radians mode (`{{key:RAD}}`) via `{{res:sc32_12_plot_07:keys}}` yields `{{res:sc32_12_plot_07:value}}` ($2/\pi \approx 0.636620$, where recalling $x = \pi/2$ from `{{key:LASTX}}` right after evaluating $\sin(\pi/2)$ divides $\sin(x)/x$ without retyping the angle).

### Biochemical Saturation, Cantilever Beam Deflection & Piecewise Iverson Profiles

Biochemical reaction kinetics, structural beam deflection curves, and piecewise voltage clippers likewise pair single-register `{{key:LASTX}}` evaluation on the stack with `{{key:EQN}}` integration:

* **Michaelis–Menten Enzyme Saturation Hyperbola ($v = \frac{V_{\max}[S]}{K_m + [S]}$):** For an enzyme with maximum turnover rate $V_{\max} = 100.0\text{ }\mu\text{mol/min}$ and half-saturation constant $K_m = 15.0\text{ mM}$, the reaction curve climbs steeply near the origin where active sites are abundant, then bends toward the horizontal asymptote $V_{\max} = 100$. Using `{{key:LASTX}}` verifies the two reference points along that hyperbola with $[S]$ typed only once while leaving Registers $Z$ and $T$ at zero: at half-saturation $[S] = K_m = 15.0\text{ mM}$, multiplying $100 \times 15$ and recalling $[S] = 15.0\text{ mM}$ from `{{key:LASTX}}` to form $K_m + [S] = 30.0\text{ mM}$ confirms $v = 50.000000\text{ }\mu\text{mol/min}$ ($\frac{1}{2}V_{\max}$); at $[S] = 3K_m = 45.0\text{ mM}$, the same `{{key:LASTX}}` recall divides $100 \times 45$ by $45 + 15 = 60.0\text{ mM}$ to confirm $v = 75.000000\text{ }\mu\text{mol/min}$ ($\frac{3}{4}V_{\max}$).
* **Euler–Bernoulli Cantilevered Beam Deflection Curve ($y(x) = \frac{Px^2}{6EI}(3L - x)$):** Across an $L = 4.0\text{ m}$ cantilever span ($\frac{P}{6EI} = 3.0625 \times 10^{-5}\text{ m}^{-2}$, or in normalized form $0.5x^2(12-x)$ entered in `{{key:EQN}}` as `12 X - X x² × 0.5 ×`), the elastic curve emerges horizontally from the clamped wall at $x = 0$ ($y(0) = y'(0) = 0$) before bowing cubically toward the free tip at $x = 4.0\text{ m}$. Because `{{key:LASTX}}` retains $x = 4.0\text{ m}$ after forming $3L = 3 \times 4.0 = 12.0\text{ m}$, the tip-deflection verification stays inside Register $X$ ($Y = Z = T = 0$): recalling `{{key:LASTX}}` twice subtracts $x = 4.0$ for $3L - x = 8.000000\text{ m}$ and squares $x^2 = 16.0\text{ m}^2$ via `{{key:x²}}` to form $x^2(3L - x) = 128.000000\text{ m}^3$, which scales by $3.0625 \times 10^{-5}\text{ m}^{-2}$ to resolve the tip sag $\delta_{\max} = 0.003920\text{ m}$ ($3.92\text{ mm}$).
* **Piecewise Zener-Diode Limiter & Trapezoidal Area via Iverson Booleans (`{{key:x>0}}`):** Inside `{{key:EQN}}`, the relational test menus `{{key:x?y}}` and `{{key:x?0}}` evaluate to Kenneth Iverson's Boolean indicator $1.0$ (True) or $0.0$ (False) in Register $X$ while preserving Registers $Y$ and $Z$. Combining a linear ramp with the three-keystroke Macaulay bracket idiom (`{{key:ENTER}} {{key:x>0}} {{key:×}}`) models a piecewise Zener-diode voltage limiter—acting like an electronic pressure-relief valve or surge protector that passes normal voltages untouched and clips any spike above $5.0\text{ V}$—via $v_{\text{out}}(x) = \min(x, 5.0\text{ V}) = x - \langle x - 5 \rangle_+$ over $x \in [0, 8]\text{ V}$ (`{{key:RCL}} X  {{key:RCL}} X  5 {{key:-}}  {{key:ENTER}} {{key:x>0}} {{key:×}}  {{key:-}}`, whose enclosed area over $[0, 8]$ is the $[0, 5]$ triangle $12.5$ plus the $[5, 8]$ rectangle $15.0$, or $A = 27.500000\text{ V}^2$). Below the $5.0\text{ V}$ knee (at $x = 3.2\text{ V}$), `{{key:x>0}}` evaluates to $0$ so $v_{\text{out}} = 3.2\text{ V}$; above the knee (at $x = 7.4\text{ V}$), `{{key:x>0}}` evaluates to $1$ and subtracts the $2.4\text{ V}$ excess to clamp the output flat at $5.000000\text{ V}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `3.2 {{key:STO}} X` | 0.000000 | 0.000000 | 0.000000 | 3.200000 | Sample linear ramp below knee ($x = 3.2\text{ V}$) |
| `{{key:RCL}} X 5 {{key:-}}` | 0.000000 | 0.000000 | 3.200000 | -1.800000 | Excess above Zener knee $x - 5 = -1.8\text{ V} < 0$ |
| `{{key:ENTER}} {{key:x>0}} {{key:×}} {{key:-}}` | 0.000000 | 0.000000 | 0.000000 | **3.200000** | Macaulay ramp is $0$; linear output $v_{\text{out}}(3.2) = 3.2\text{ V}$ |
| `7.4 {{key:STO}} X` | 0.000000 | 0.000000 | 3.200000 | 7.400000 | Sample clamped plateau above knee ($x = 7.4\text{ V}$) |
| `{{key:RCL}} X 5 {{key:-}}` | 3.200000 | 3.200000 | 7.400000 | 2.400000 | Excess above Zener knee $x - 5 = +2.4\text{ V} > 0$ |
| `{{key:ENTER}} {{key:x>0}} {{key:×}} {{key:-}}` | 3.200000 | 3.200000 | 3.200000 | **5.000000** | Subtract $2.4 \times 1 = 2.4\text{ V}$; clamped $v_{\text{out}}(7.4) = \mathbf{5.0\text{ V}}$ |

### Parabolic Dish Surface Area of Revolution & Bivariate Calibration Auditing

To see how surface area of revolution (`{{key:∫}}`) and closed-form mensuration cross-check each other on the stack, consider a parabolic solar concentrator dish $z(r) = \frac{r^2}{4F}$ with focal length $F = 1.0\text{ m}$ and outer rim radius $R = 1.5\text{ m}$ (where $z'(r) = 0.5r$ and the radial slant factor is $\sqrt{1 + 0.25r^2}$):
1. **Continuous Integral Evaluation via `{{key:EQN}}` and `{{key:∫}}`:** Store the radial surface-area integrand $r\sqrt{1 + 0.25r^2}$ in `{{key:EQN}}` as `R x² 0.25 × 1 + √x R ×`. Stage the radial bounds `0 {{key:ENTER}} 1.5` and press `{{key:∫}} R` to obtain the radial integral $I = \int_0^{1.5} r\sqrt{1 + 0.25r^2}\,dr = \mathbf{1.270833333\text{ m}^2}$ in Register $X$, then scale by `2 {{key:×}} {{key:π}} {{key:×}}` to obtain the exact 3D reflective dish surface area $S_{\text{dish}} = \mathbf{7.984881\text{ m}^2}$.
2. **Closed-Form Verification on the Stack:** Evaluating $\frac{8\pi F^2}{3}\left[(1 + R^2/4F^2)^{3/2} - 1\right]$ for $F = 1.0\text{ m}$ and $R = 1.5\text{ m}$ forms $1 + \frac{2.25}{4} = 1.5625 = \left(\frac{5}{4}\right)^2$, whose $3/2$ power (`1.5 {{key:yˣ}}`) is $\left(\frac{5}{4}\right)^3 = \frac{125}{64} = 1.953125$. Subtracting $1$ leaves $\frac{61}{64} = 0.953125$, and multiplying by $\frac{8\pi}{3}$ (`8 {{key:×}} {{key:π}} {{key:×}} 3 {{key:÷}}`) confirms $S_{\text{dish}} = \frac{61\pi}{24} = \mathbf{7.984881\text{ m}^2}$—an $12.96\%$ surface-area increase over the flat circular aperture $\pi R^2 = 7.068583\text{ m}^2$!

Finally, when auditing experimental $(x_k, y_k)$ calibration data accumulated via `{{key:Σ+}}`—where up to 25 bivariate pairs reside in indirect slots `40`–`89` (`DATA0`–`DATA49` under `{{key:REGS}}`)—combining `{{key:L.R.}}` slope/correlation checks (`{{key:m}}`, `{{key:r}}`) with predicted-value residual checks (`{{key:ŷ}}`) verifies that a sensor response is genuinely linear across its operating span. Take four piezoresistive pressure sensor calibration pairs: $(10\text{ kPa}, 1.25\text{ V}), (20\text{ kPa}, 2.45\text{ V}), (30\text{ kPa}, 3.80\text{ V}), (40\text{ kPa}, 4.95\text{ V})$. Accumulating the pairs via `{{key:Σ+}}` and querying `{{key:L.R.}}` $\to$ `{{key:m}}` yields the least-squares sensitivity $m = 0.124500\text{ V/kPa}$ ($y = 0.1245x + 0.0000$, $r = 0.999565$, $R^2 = 0.999130$), while checking `20 {{key:L.R.}} {{key:ŷ}}` ($\to 2.4900\text{ V}$) and `30 {{key:L.R.}} {{key:ŷ}}` ($\to 3.7350\text{ V}$) confirms that the residuals alternate cleanly without parabolic drift:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `{{key:CLEAR}} {{key:CLΣ}}` | 0.00 | 0.00 | 0.00 | 0.00 | Clear statistical accumulators |
| `1.25 {{key:ENTER}} 10 {{key:Σ+}}` | 0.00 | 0.00 | 1.25 | 1.00 | Pair 1: (10 kPa, 1.25 V); count n = 1 |
| `2.45 {{key:ENTER}} 20 {{key:Σ+}}` | 0.00 | 1.25 | 2.45 | 2.00 | Pair 2: (20 kPa, 2.45 V); count n = 2 |
| `3.80 {{key:ENTER}} 30 {{key:Σ+}}` | 1.25 | 2.45 | 3.80 | 3.00 | Pair 3: (30 kPa, 3.80 V); count n = 3 |
| `4.95 {{key:ENTER}} 40 {{key:Σ+}}` | 2.45 | 3.80 | 4.95 | 4.00 | Pair 4: (40 kPa, 4.95 V); count n = 4 |
| `{{key:m}}` | 2.45 | 3.80 | 4.95 | 0.1245 | Regression slope m = 0.124500 V/kPa |

By uniting Descartes's analytic coordinate geometry, Gauss's Shoelace polygon theorem, additive and subtractive composite area ledgers (`{{key:Σ+}}`, `{{key:Σ-}}`, `{{key:x̄w}}`), and Romberg's definite integral (`{{key:∫}}`), the SC-32 turns every planar cross-section and three-dimensional surface of revolution into a direct, verifiable four-register stack calculation.
