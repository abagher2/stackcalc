---
title: "Chapter 9: Bivariate Statistics, Curve Fitting & Linear Regression | Thinking in the Stack (SC-32)"
description: "Master the 6 statistical accumulators, sample vs. population standard deviations, linear regression (m, b, r), prediction estimation, Gaussian Normal PDF, and scatter plotting on the StackCalc SC-32."
---

# Chapter 9: Bivariate Statistics, Curve Fitting & Linear Regression

## The Celestial Drama: How 24-Year-Old Carl Friedrich Gauss Rediscovered Ceres (1801)

On the clear, cold evening of January 1, 1801, Italian astronomer Giuseppe Piazzi peered through his Ramsden circle telescope at the Palermo Observatory in Sicily and spotted a faint, uncataloged eighth-magnitude star moving against the starry backdrop of Taurus. Tracking the mysterious object across forty-one nights, Piazzi realized he had discovered a new wandering celestial body—a dwarf planet orbiting between Mars and Jupiter, which he christened *Ceres Ferdinandea*.

By mid-February, Ceres drifted behind the solar glare of the Sun. Astronomers across Europe attempted to predict where the object would re-emerge in late autumn, but eighteenth-century celestial mechanics required months of continuous observations to determine an elliptical orbit. Piazzi had captured only three degrees of orbital arc—barely one percent of its total trajectory across the heavens. Using traditional circular and paraboloid approximations, Europe's astronomers computed ephemerides that pointed telescopes into empty sky.

Enter twenty-four-year-old **Carl Friedrich Gauss** in Göttingen.

Refusing to treat Piazzi's sparse observations as isolated geometric points, Gauss attacked the problem from a new perspective: **observational uncertainty**. Every telescope reading contained minute human, optical, and atmospheric errors. Rather than searching for a single hypothetical curve passing through fixed points, Gauss sought the unique elliptical orbit that minimized the sum of the squared deviations between prediction and observation.

Over three months in the autumn of 1801, Gauss formulated the **Method of Least Squares** and the **Gaussian Normal Distribution** of measurement errors {{cite:gauss1809}}. When German astronomer Franz Xaver von Zach pointed his telescope into the constellation Virgo on the night of December 31, 1801—guided by Gauss's least-squares ephemeris—Ceres was recovered within half a degree of Gauss's predicted coordinates.

Gauss had demonstrated that statistical aggregation does not blur truth—it reveals the signal buried beneath the noise.

{{blocks:dice_spinner_probability|Dice Spinner Probability Calibration}}
*Figure 9.1: Physical probability mapping and discrete outcome distributions. The random fluctuations of physical trials converge systematically to smooth statistical distributions.*

{{blocks:dice_spinner_craftsmanship|Dice Spinner Mechanical Craftsmanship}}
*Figure 9.2: Precision CNC-machined dice spinner mechanism, demonstrating the physical symmetry and mechanical tolerance analysis required for unbiased stochastic generation.*

### Tower Leveling, Biased Spinner Weights & The Polyhedral Dice Central Limit Bridge

Why do sample means ($\bar{x}$), weighted means ($\bar{x}_w$), and Gaussian bell curves share the same six hardware accumulators ($\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$)? You can verify all three principles physically using the **Counting Tiles** and the **Polyhedral Dice & Modular Spinner**:
1. **Sample Mean ($\bar{x} = \Sigma x / n$) as Physical Tower Leveling:** Dock four unequal towers of $19.0 \times 19.0 \times 7.0\text{ mm}$ counting tiles onto four adjacent sockets of the $6 \times 2$ Snapfinity lid—say heights $3, 5, 6,$ and $10$ tiles ($\Sigma x = 24$ tiles across $n = 4$ columns). If you transfer tiles from the taller columns to the shorter columns until all four towers stand completely flush at the exact same height, every column stands $24 \div 4 = \mathbf{6\text{ tiles}}$ ($42.0\text{ mm}$) tall. The arithmetic mean $\bar{x}$ is literally the **equalized leveling height** of the data columns, and the signed deviations $(x_i - \bar{x}) = (-3, -1, 0, +4)$ sum identically to zero because every tile removed above the $\bar{x} = 6$ plane filled a gap below it.
2. **Weighted Mean ($\bar{x}_w = \Sigma xy / \Sigma y$) on the Biased Spinner Dial:** Snap the **Biased ($\frac{1}{2}\text{–}\frac{1}{4}\text{–}\frac{1}{4}$) Spinner Dial** onto the $1 \times 1$ modular spinner base. Because Sector 1 spans $180^\circ$ ($w_1 = \frac{1}{2}$) while Sectors 2 and 3 span $90^\circ$ each ($w_2 = \frac{1}{4}, w_3 = \frac{1}{4}$), the expected value of a spin is not the unweighted average $(1+2+3)/3 = 2.0$, but the sector-area weighted mean $\bar{x}_w = \frac{0.5(1) + 0.25(2) + 0.25(3)}{0.5 + 0.25 + 0.25} = \mathbf{1.75}$—which the SC-32 computes directly when you enter weight $w_i$ in Register $Y$ and outcome $x_i$ in Register $X$ before pressing `{{key:Σ+}}` and `{{key:x̄,ȳ}} {{key:x̄w}}`.
3. **From Flat Polyhedral Dice to Gauss's Bell Curve:** Roll one volume-equalized $18\text{ mm}$ fair $d6$ die (or polyhedral $d8, d10, d12, d20$): its probability distribution across $1 \dots 6$ is a flat rectangular bar ($p = 1/6$). Roll **two** fair $d6$ dice ($36$ outcomes from $2$ to $12$): stacking outcome towers produces a symmetric **triangular roof** peaking at $7$ ($6/36 = 1/6$). Roll **three or four** fair $d6$ dice together: the sharp triangular peak rounds smoothly into **Carl Friedrich Gauss's bell curve** $f(z) = \frac{1}{\sqrt{2\pi}}e^{-z^2/2}$—demonstrating the Central Limit Theorem directly on the workbench.

Today, an engineer does not need weeks of manual quill-and-ink calculations to perform Gauss's least-squares synthesis. On the StackCalc SC-32, the **dual-variable statistical accumulation engine (`{{key:Σ+}}`)** automates Gauss's discovery directly on the RPN stack. Every time you enter a coordinate pair $(x, y)$ and tap `{{key:Σ+}}`, six dedicated hardware accumulators update instantaneously in continuous CMOS memory, calculating means, sample variances, covariance, and the least-squares regression line with certified 64-bit precision.

---

{{res:sc32_normal_pdf:screenshot|Standard Normal PDF f(1.0) = exp(-0.5)/sqrt(2*pi) = 0.241970724519}}

## The Philosophy of Data in the Stack

In conventional algebraic calculators, statistical analysis is treated as an external, table-bound spreadsheet mode. The user enters a separate data grid, loses sight of the calculation stack, and must memorize cryptic sub-menu codes to retrieve basic parameters.

On the StackCalc SC-32, statistics is a first-class, dynamic extension of the Reverse Polish Notation operational stack. Data coordinates $(x, y)$ are entered directly into Registers $X$ and $Y$, transformed in real time using the full power of transcendental operators (`LN`, `1/x`, `x²`, `√x`), and committed into hardware accumulators with a single tap of `{{key:Σ+}}`.

### The SC-32 Statistical Pipeline

The statistical processing pipeline links the operational stack directly to the six hardware accumulators:

1. **Input Coordinates:** The dependent value $y$ rests in Register $Y$; the independent value $x$ rests in Register $X$.
2. **Commit via `{{key:Σ+}}`:** Pressing `{{key:Σ+}}` updates all six internal statistical registers simultaneously without clearing the display.
3. **Hardware Storage:** Six dedicated 64-bit accumulators maintain the running sums: $\Sigma x$, $\Sigma y$, $\Sigma x^2$, $\Sigma y^2$, $\Sigma xy$, and sample count $n$.
4. **Instant Synthesis:** Dynamic softkey menus provide instantaneous access to means ($\bar{x}, \bar{y}, \bar{x}_w$), standard deviations ($s_x, s_y, \sigma_x, \sigma_y$), and linear regression parameters (slope $m$, intercept $b$, correlation $r$, and predictive estimates $\hat{y}, \hat{x}$).

---

## The 6 Hardware Statistical Accumulators

Statistical modeling on the SC-32 is driven by six dedicated non-volatile accumulator registers maintained continuously in hardware memory:

| Accumulator | Internal Register | Mathematical Meaning | Engineering Application |
| :---: | :---: | :--- | :--- |
| **$\Sigma x$** | `R.Σ1` | Sum of $x$-values: $\sum x_i$ | Sample mean $\bar{x}$, regression slope $m$ |
| **$\Sigma y$** | `R.Σ2` | Sum of $y$-values: $\sum y_i$ | Sample mean $\bar{y}$, regression intercept $b$ |
| **$\Sigma x^2$** | `R.Σ3` | Sum of squared $x$-values: $\sum x_i^2$ | $x$-variance and sample/population standard deviations |
| **$\Sigma y^2$** | `R.Σ4` | Sum of squared $y$-values: $\sum y_i^2$ | $y$-variance and sample/population standard deviations |
| **$\Sigma xy$** | `R.Σ5` | Sum of cross-products: $\sum (x_i \cdot y_i)$ | Bivariate covariance and Pearson correlation coefficient $r$ |
| **$n$** | `R.Σ6` | Total count of accumulated data pairs | Normalization and degrees of freedom ($n - 1$) |

### Streaming Data Into the Six Accumulators (`{{key:Σ+}}` and `{{key:Σ-}}`)
Calibrating precision sensor arrays or analyzing bivariate experimental data on standard calculators requires entering data into a cumbersome matrix spreadsheet editor. Switching between spreadsheet data entry, calculation screens, and regression output interrupts the analytical workflow, and verifying outliers requires navigating multi-tiered setup menus {{cite:gauss1809}}.

How can six numbers in memory remember everything needed to fit a line through a hundred data points without storing the hundred points themselves? The secret of Gauss's least-squares algebra is that the sample means, variances, and regression slope depend only on six running totals: $\Sigma x$, $\Sigma y$, $\Sigma x^2$, $\Sigma y^2$, $\Sigma xy$, and the count $n$.

The SC-32 utilizes these six dedicated hardware accumulators updated instantaneously via the physical coordinate key `{{key:Σ+}}` {{cite:hp15c1982,hp32sii1991}}. You stream each coordinate pair $(x_k, y_k)$ directly from the stack by keying the dependent measurement $y_k$, pressing `{{key:ENTER}}` to lift it into Register $Y$, keying the independent variable $x_k$ into Register $X$, and tapping `{{key:Σ+}}` (Row 1, Column 6). In a single instruction cycle, all six accumulators update in parallel:
$$\Sigma x \leftarrow \Sigma x + x_k, \qquad \Sigma y \leftarrow \Sigma y + y_k, \qquad \Sigma x^2 \leftarrow \Sigma x^2 + x_k^2$$
$$\Sigma y^2 \leftarrow \Sigma y^2 + y_k^2, \qquad \Sigma xy \leftarrow \Sigma xy + (x_k \times y_k), \qquad n \leftarrow n + 1$$

Register $X$ immediately displays the updated sample count $n$ while disabling stack lift so you can type the next $(y, x)$ pair right over it without clearing the screen. Better still, as audited in Appendix A, pressing `{{key:Σ+}}` or `{{key:Σ-}}` **preserves `LASTX`** so your prior arithmetic operand remains untouched.

What if, in the middle of logging a long experimental run, your finger slips on the sixth data pair $(x=15, y=3.5)$—transposing the digits of $y$ so you accidentally enter $(x=15, y=5.3)$? You do not have to clear the dataset (`{{key:CLEAR}}` $\to$ `{{key:CLΣ}}`) and start over from scratch. When the current sample count is $n = 6$, watch how `{{key:Σ-}}` surgically removes the bad point and splices in the true reading without losing the first five points ($\Sigma x \leftarrow \Sigma x - x_k$, $\Sigma y \leftarrow \Sigma y - y_k$, $n \leftarrow n - 1$). Re-entering the erroneous pair `5.3 {{key:ENTER}} 15` and pressing Left Shift `{{key:↰}}` followed by `{{key:Σ-}}` decrements the display to $n = 5$ while cleansing all six accumulators of the transposed point, after which keying the intended reading `3.5 {{key:ENTER}} 15 {{key:Σ+}}` restores $n = 6$ with complete arithmetic fidelity:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `5.3 {{key:ENTER}} 15` | $0.0000$ | $0.0000$ | $5.3000$ | $15.0000$ | Key erroneous pair $(x=15, y=5.3)$ |
| 02 | `{{key:Σ-}}` | $0.0000$ | $0.0000$ | $5.3000$ | **$5.0000$** | Subtract from accumulators; $n$ decrements to 5 |
| 03 | `3.5 {{key:ENTER}} 15` | $0.0000$ | $5.3000$ | $3.5000$ | $15.0000$ | Key corrected pair $(x=15, y=3.5)$ |
| 04 | `{{key:Σ+}}` | $0.0000$ | $5.3000$ | $3.5000$ | **$6.0000$** | Accumulate corrected pair; $n$ restored to 6 |

---

## The Statistical Dynamic Softkey Menus

Once your observations are accumulated, the top six LFU dynamic keys give you one-touch access to every summary statistic:

| Sub-Menu | Primary Invocation | LFU 1 | LFU 2 | LFU 3 | LFU 4 | LFU 5 | LFU 6 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Sums Menu** | `{{key:SUMS}}` | `{{key:Σx}}` | `{{key:Σy}}` | `{{key:Σx²}}` | `{{key:Σy²}}` | `{{key:Σxy}}` | `{{key:n}}` |
| **2. Means Menu** | `{{key:x̄,ȳ}}` | `{{key:x̄}}` | `{{key:ȳ}}` | `{{key:x̄w}}` | — | — | — |
| **3. Std Dev Menu** | `{{key:s,σ}}` | `{{key:sx}}` | `{{key:sy}}` | `{{key:σx}}` | `{{key:σy}}` | — | — |
| **4. Regression Menu** | `{{key:L.R.}}` | `{{key:ŷ}}` | `{{key:x̂}}` | `{{key:r}}` | `{{key:m}}` | `{{key:b}}` | — |

### Means, Weighted Centroids, and the Mystery of Bessel's $n - 1$ Correction

From the `{{key:x̄,ȳ}}` menu, the calculator extracts the unweighted sample means and the weighted mean directly from the running sums:
$$\bar{x} = \frac{\Sigma x}{n}, \qquad \bar{y} = \frac{\Sigma y}{n}, \qquad \bar{x}_w = \frac{\Sigma xy}{\Sigma y}$$
where in a weighted average (`{{key:x̄w}}`), each weight $w_k$ is entered into Register $Y$ and each measurement $x_k$ into Register $X$.

Just as we used `{{key:∫}}` in Chapter 8 to find the center of mass of a continuously varying rod, the SC-32's weighted mean (`{{key:x̄w}}` $= \Sigma xy / \Sigma y$) finds the exact centroid of a composite structural shape made of discrete rectangular plates. Suppose a welded steel beam consists of three flange segments with cross-sectional areas $A_i$ (entered as weights in Register $Y$) and centroid coordinates $x_i$ (entered in Register $X$): Flange 1 with $A_1 = 40\text{ cm}^2$ at $x_1 = 10\text{ cm}$, Flange 2 with $A_2 = 60\text{ cm}^2$ at $x_2 = 25\text{ cm}$, and Flange 3 with $A_3 = 20\text{ cm}^2$ at $x_3 = 45\text{ cm}$. Accumulating each plate as $(y = A_i, x = x_i)$ via `40 {{key:ENTER}} 10 {{key:Σ+}}`, `60 {{key:ENTER}} 25 {{key:Σ+}}`, and `20 {{key:ENTER}} 45 {{key:Σ+}}` lets `{{key:x̄,ȳ}} {{key:x̄w}}` compute the area-weighted centroid **`23.333 cm`** in Register $X$ while `{{key:SUMS}} {{key:Σy}}` reports the total cross-sectional area **`120.0 cm²`**:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `{{key:CLΣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Clear accumulators |
| 02 | `40 {{key:ENTER}} 10 {{key:Σ+}}` | $0.0000$ | $0.0000$ | $40.0000$ | $1.0000$ | Flange 1 logged ($n=1$) |
| 03 | `60 {{key:ENTER}} 25 {{key:Σ+}}` | $0.0000$ | $40.0000$ | $60.0000$ | $2.0000$ | Flange 2 logged ($n=2$) |
| 04 | `20 {{key:ENTER}} 45 {{key:Σ+}}` | $40.0000$ | $60.0000$ | $20.0000$ | $3.0000$ | Flange 3 logged ($n=3$) |
| 05 | `{{key:x̄w}}` | $40.0000$ | $60.0000$ | $20.0000$ | **$23.3333$** | Weighted centroid $\bar{x}_w$ (cm) |
| 06 | `{{key:Σy}}` | $60.0000$ | $20.0000$ | $23.3333$ | **$120.0000$** | Total beam area $\Sigma y$ ($\text{cm}^2$) |

When you open the standard deviation menu (`{{key:s,σ}}`), you are offered two distinct measures of spread: **population standard deviation** ($\sigma_x, \sigma_y$, which divides by $n$) and **sample standard deviation** ($s_x, s_y$, which divides by $n - 1$). Why on earth do statisticians divide by $n - 1$ instead of $n$ when estimating spread from a sample?

Imagine pulling $n = 4$ machined shafts off a lathe that is producing thousands of parts. You want to estimate the spread of the *entire* production run, whose true center $\mu$ you do not know. Because you don't know $\mu$, you are forced to measure each shaft's deviation from your sample's own average, $\bar{x}$. Now remember our **Counting Tiles** leveling experiment from the opening of the chapter: the sample mean $\bar{x}$ is the exact center of balance of your $n$ sample points, which mathematically minimizes $\sum(x_i - \bar{x})^2$. That means your sample points *always* huddle slightly closer to their own sample mean $\bar{x}$ than they do to the true, unknown population mean $\mu$! Even more tellingly, once you know $\bar{x}$ and the first $n - 1$ deviations, the final deviation $x_n - \bar{x}$ is not free to vary—it is completely determined by the balance requirement $\sum_{i=1}^n (x_i - \bar{x}) = 0$. Measuring spread around $\bar{x}$ instead of $\mu$ costs you exactly one **degree of freedom**.

As Gauss's colleague Friedrich Wilhelm Bessel proved, dividing the sum of squared residuals by the remaining $n - 1$ degrees of freedom (**Bessel's correction**) removes this downward bias, giving the unbiased sample standard deviations ($s_x, s_y$):

$$s_x = \sqrt{\frac{\Sigma x^2 - \frac{(\Sigma x)^2}{n}}{n - 1}} = \sqrt{\frac{n \Sigma x^2 - (\Sigma x)^2}{n(n - 1)}}, \qquad s_y = \sqrt{\frac{\Sigma y^2 - \frac{(\Sigma y)^2}{n}}{n - 1}} = \sqrt{\frac{n \Sigma y^2 - (\Sigma y)^2}{n(n - 1)}}$$

When your $n$ observations represent an entire closed population rather than a sample drawn from a larger process, dividing by $n$ yields the exact population standard deviations ($\sigma_x, \sigma_y$):

$$\sigma_x = \sqrt{\frac{\Sigma x^2 - \frac{(\Sigma x)^2}{n}}{n}}, \qquad \sigma_y = \sqrt{\frac{\Sigma y^2 - \frac{(\Sigma y)^2}{n}}{n}}, \qquad s = \sigma \sqrt{\frac{n}{n - 1}}$$

Whenever your data points are a sample drawn from a larger process (calibrating sensors, testing alloy coupons, auditing manufacturing quality), use $s_x$ and $s_y$; when your $n$ numbers are the entire universe of interest, use $\sigma_x$ and $\sigma_y$.

### Six Sigma Process Capability ($C_p, C_{pk}$), Shewhart Control Limits & Standard Error

To see how $\bar{x}$ and Bessel's sample standard deviation $s_x$ work together on the factory floor, consider how Six Sigma process capability ($C_p$ and $C_{pk}$) audits a live production line. Suppose a CNC turning center is machining steel bearing shafts specified at $25.00 \pm 0.10\text{ mm}$ ($\text{LSL} = 24.90\text{ mm}$, $\text{USL} = 25.10\text{ mm}$), and a quality engineer pulls a random sample of $n = 10$ shafts from the output bin, measuring their diameters with a digital micrometer as $25.02, 25.04, 25.01, 25.03, 25.05, 25.02, 25.00, 25.04, 25.03,$ and $25.06\text{ mm}$. Is the lathe's natural $6s_x$ spread narrow enough to fit comfortably inside the $0.20\text{ mm}$ tolerance window ($C_p$), and how badly does the $+0.030\text{ mm}$ tool-wear drift toward the upper limit erode the off-center capability index ($C_{pk}$)? Accumulating the ten shaft diameters via `25.02 {{key:Σ+}} 25.04 {{key:Σ+}} 25.01 {{key:Σ+}} 25.03 {{key:Σ+}} 25.05 {{key:Σ+}}` and `25.02 {{key:Σ+}} 25.00 {{key:Σ+}} 25.04 {{key:Σ+}} 25.03 {{key:Σ+}} 25.06 {{key:Σ+}}` yields the sample mean $\bar{x}$ via `{{key:x̄,ȳ}} {{key:x̄}}` (**`25.0300 mm`**) and the sample standard deviation $s_x$ via `{{key:s,σ}} {{key:sx}}` (**`0.018257 mm`**). Across the tolerance width $\text{USL} - \text{LSL} = 0.20\text{ mm}$, dividing by the $6s_x$ natural process spread via `{{res:sc32_09_statistics_curve_fitting_seq_03:keys}}` confirms a centered capability of $C_p = \frac{0.20}{6 \times 0.018257} =$ **`{{res:sc32_09_statistics_curve_fitting_seq_03:value}}`** ($C_p > 1.33 \implies$ Capable), while comparing the shifted mean against the upper specification wall via `{{res:sc32_09_statistics_curve_fitting_seq_04:keys}}` reveals how tool-wear drift lowers $C_{pk} = \frac{25.10 - 25.030}{3 \times 0.018257}$ to **`{{res:sc32_09_statistics_curve_fitting_seq_04:value}}`**:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `25.02 {{key:Σ+}} 25.04 {{key:Σ+}} 25.01 {{key:Σ+}} 25.03 {{key:Σ+}} 25.05 {{key:Σ+}} 25.02 {{key:Σ+}} 25.00 {{key:Σ+}} 25.04 {{key:Σ+}} 25.03 {{key:Σ+}} 25.06 {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | Accumulate 10 shaft diameter samples |
| 02 | `{{key:x̄,ȳ}} {{key:x̄}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$25.0300$** | Sample mean diameter $\bar{x}$ (mm) |
| 03 | `{{key:s,σ}} {{key:sx}}` | $0.0000$ | $0.0000$ | $25.0300$ | **$0.018257$** | Sample standard deviation $s_x$ (mm) |
| 04 | `{{res:sc32_09_statistics_curve_fitting_seq_03:keys}}` | $25.0300$ | $25.0300$ | $0.0183$ | **`{{res:sc32_09_statistics_curve_fitting_seq_03:value}}`** | Process capability $C_p = \frac{\text{USL}-\text{LSL}}{6s_x}$ |
| 05 | `{{res:sc32_09_statistics_curve_fitting_seq_04:keys}}` | $0.0183$ | $0.0183$ | $1.8258$ | **`{{res:sc32_09_statistics_curve_fitting_seq_04:value}}`** | Process capability index $C_{pk} = \frac{\text{USL}-\bar{x}}{3s_x}$ |

> **3D Printing & CNC Dimensional Tolerances ($42.0\text{ mm}$ Gridfinity & $0.20\text{ mm}$ Slip-Fit Clearance):** Why do our 3D-printed manipulative blocks (*Counting Tiles*, *Place Value Cubes*, *84 mm Fraction Towers*, and *L-Frame Factoring Stage*) and $42.0\text{ mm}$ Gridfinity/Snapfinity lids specify a nominal **$0.20\text{ mm}$ diametral clearance** ($0.10\text{ mm}$ per wall)? A well-calibrated desktop FFF 3D printer exhibits a dimensional standard deviation of $\sigma \approx 0.025\text{ to }0.030\text{ mm}$ due to filament diameter fluctuations and thermal shrinkage. With a $\pm 3\sigma \approx \pm 0.09\text{ mm}$ natural process spread ($6\sigma \approx 0.18\text{ mm}$), a $0.20\text{ mm}$ clearance window achieves $C_{pk} \ge 1.33$: parts never interfere into a jammed press-fit ($< 0.02\text{ mm}$) and never wobble with loose rattle ($> 0.38\text{ mm}$), delivering a crisp tactile slip-fit across thousands of printed classroom tiles.

How does a machinist know *when* to compensate for that $+0.030\text{ mm}$ tool-wear drift without overreacting to normal random chatter? In 1924 at Bell Laboratories, physicist Walter A. Shewhart realized that if factory operators adjust a machine after every tiny random fluctuation, they actually *increase* process variance—whereas waiting until a part goes completely out of spec is too late. Shewhart invented the **$\bar{X}$ control chart**: by pulling small subgroups of $n = 5$ parts at regular intervals, tracking their grand mean $\bar{\bar{X}} = 50.00\text{ mm}$ and average subgroup range $\bar{R} = 0.40\text{ mm}$, and setting $\pm 3\sigma_{\bar{x}}$ guardrails using the control factor $A_2 = 0.577$, operators can distinguish normal background noise from a true tool-wear trend:

$$\text{UCL} = \bar{\bar{X}} + A_2 \bar{R}, \quad \text{LCL} = \bar{\bar{X}} - A_2 \bar{R}$$

In Walter Shewhart's statistical process control framework, the $3\sigma_{\bar{x}}$ control band around the grand process mean $\bar{\bar{X}}$ is estimated from subgroup ranges via $E = A_2 \bar{R}$. Evaluating `{{res:sc32_09_statistics_curve_fitting_seq_18:keys}}` establishes the half-width $A_2 \bar{R} = 0.577 \times 0.40 = 0.2308\text{ mm}$; adding the grand mean via `50.00 {{key:+}}` forms the Upper Control Limit $\text{UCL} = \mathbf{50.2308\text{ mm}}$, and `{{res:sc32_09_statistics_curve_fitting_seq_19:keys}}` yields the Lower Control Limit $\text{LCL} = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_19:value}}\text{ mm}}$. *(**`LASTX` Single-Entry Interval Shortcut:** When $E = 0.2308$ is in Register $X$, keying `50.00 {{key:x⇄y}} {{key:-}}` computes $\text{LCL} = 49.7692\text{ mm}$ in $X$ while preserving $E = 0.2308$ in `LASTX`; following immediately with `{{key:LASTX}} 2 {{key:×}} {{key:+}}` adds $2E = 0.4616$ to jump directly to $\text{UCL} = \mathbf{50.2308\text{ mm}}$—typing $\bar{\bar{X}} = 50.00$ only once and never re-keying $E$.)*

The same Central Limit Theorem explains why averaging $n = 36$ noisy measurements pinpoints a true physical value six times more accurately than a single reading: independent random errors partially cancel one another when averaged, shrinking the **standard error of the mean** as $\text{SE} = s/\sqrt{n}$. For a sample of $n = 36$ measurements with sample mean $\bar{x} = 120.5$ and sample standard deviation $s = 8.4$, the sampling distribution of the mean narrows with $\sqrt{n}$, so executing `{{res:sc32_09_statistics_curve_fitting_seq_20:keys}}` evaluates the standard error $\text{SE} = s / \sqrt{n} = 8.4 / \sqrt{36} = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_20:value}}}$, and scaling by the two-tailed normal quantile `1.960 {{key:×}}` forms the $95\%$ margin of error $E = \mathbf{2.7440}$. Keying `{{res:sc32_09_statistics_curve_fitting_seq_21:keys}}` establishes the upper confidence limit $\bar{x} + E = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_21:value}}}$, and `{{res:sc32_09_statistics_curve_fitting_seq_22:keys}}` resolves the lower confidence limit $\bar{x} - E = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_22:value}}}$. *(**`LASTX` Single-Entry Interval Shortcut:** With $E = 2.7440$ in Register $X$, keying `120.5 {{key:x⇄y}} {{key:-}}` yields the lower bound $\bar{x} - E = \mathbf{117.7560}$ while saving $E = 2.7440$ in `LASTX`, so `{{key:LASTX}} 2 {{key:×}} {{key:+}}` immediately produces the upper bound $\bar{x} + E = \mathbf{123.2440}$ without re-typing `120.5` or `2.7440`. In general, whenever any computed standard error such as $\text{SE} = 1.350$ is already sitting in Register $X$ for a point estimate $\hat{\mu} = 84.625$, keying `1.96 {{key:×}} 84.625 {{key:x⇄y}} {{key:-}}` gives the lower $95\%$ confidence bound $81.9790$ and `{{key:LASTX}} 2 {{key:×}} {{key:+}}` gives the upper bound $87.2710$—typing `84.625` only once and never re-typing the margin of error $E$.)*

---

## Bivariate Linear Regression & Pearson Correlation ($r$)

Now suppose you plot your paired $(x_i, y_i)$ measurements on a sheet of graph paper and want to pass the best possible straight line $y = mx + b$ through the noisy cloud. Imagine attaching a vertical Hookean spring between each data point $(x_i, y_i)$ and a rigid straight rod $y = mx + b$. Because the potential energy stored in a stretched spring is proportional to the *square* of its vertical stretch $(y_i - (mx_i + b))^2$, the rod naturally settles into mechanical equilibrium at the exact slope $m$ and intercept $b$ that minimize the sum of squared vertical residuals. Solving that equilibrium condition yields the ordinary least-squares (OLS) formulas in the `{{key:L.R.}}` menu:

$$\text{Slope } m = \frac{\Sigma xy - \frac{\Sigma x \Sigma y}{n}}{\Sigma x^2 - \frac{(\Sigma x)^2}{n}} = \frac{n \Sigma xy - \Sigma x \Sigma y}{n \Sigma x^2 - (\Sigma x)^2}$$

$$\text{Intercept } b = \bar{y} - m \bar{x} = \frac{\Sigma y - m \Sigma x}{n}$$

$$\text{Pearson Correlation } r = \frac{n \Sigma xy - \Sigma x \Sigma y}{\sqrt{\left[ n \Sigma x^2 - (\Sigma x)^2 \right] \left[ n \Sigma y^2 - (\Sigma y)^2 \right]}}$$

Notice the geometric elegance of the intercept formula $b = \bar{y} - m\bar{x}$: rearranged as $\bar{y} = m\bar{x} + b$, it proves that the least-squares regression line *always* pivots directly through the center of mass $(\bar{x}, \bar{y})$ of your data cloud! Meanwhile, Karl Pearson's correlation coefficient $r \in [-1, +1]$ measures how tightly the data points hug the line, and its square $r^2$ (the coefficient of determination, obtained by pressing `{{key:r}} {{key:x²}}`) tells you the exact fraction of variance in $y$ explained by linear dependence on $x$.

### Prediction Operators ($\hat{y}$ and $\hat{x}$) & Transducer Calibration
Once your calibration line is in memory, the SC-32 turns regression into a live two-way translator between stimuli and responses:
* **Predicting $y$ from a given $x$ ($\hat{y} = mx + b$):** Key in a known $x$ and press `{{key:L.R.}} {{key:ŷ}}`. Register $X$ immediately displays the predicted response $\hat{y}$, while Register $Y$ automatically receives the correlation coefficient $r$ so you can verify fit quality in the same glance.
* **Predicting $x$ from a given $y$ ($\hat{x} = \frac{y - b}{m}$):** Key in a target response $y$ (such as a transducer output voltage) and press `{{key:L.R.}} {{key:x̂}}` to invert the calibration curve and recover the unknown physical input $\hat{x}$.

To see this complete calibration and prediction pipeline at the workbench, consider a silicon piezoresistive pressure sensor mounted inside a hydraulic test manifold. Its Wheatstone bridge outputs a millivolt signal that varies linearly with fluid pressure—plus tiny random fluctuations from thermal noise and ADC quantization. Suppose a metrology engineer calibrates the transducer against four dead-weight hydrostatic pressure standards: $(x_1, y_1) = (10\text{ kPa}, 1.25\text{ V})$, $(x_2, y_2) = (20\text{ kPa}, 2.45\text{ V})$, $(x_3, y_3) = (30\text{ kPa}, 3.80\text{ V})$, and $(x_4, y_4) = (40\text{ kPa}, 4.95\text{ V})$. By streaming these four calibration pairs into the SC-32, we can inspect all six hardware accumulators, extract the sensitivity slope $m$, zero-pressure intercept $b$, and Pearson correlation $r$, predict the output voltage at $25\text{ kPa}$, and invert the calibration curve to find the unknown manifold pressure when the sensor reads $V = 4.00\text{ V}$.

After zeroing the statistical accumulators via {{key:CLEAR}} $\to$ `{{key:CLΣ}}`, we stream each calibration pair $(y_k, x_k)$ onto the stack—keying `1.25 {{key:ENTER}} 10 {{key:Σ+}}`, `2.45 {{key:ENTER}} 20 {{key:Σ+}}`, `3.80 {{key:ENTER}} 30 {{key:Σ+}}`, and `4.95 {{key:ENTER}} 40 {{key:Σ+}}`—as the display counts up the accumulated sample size $n = 1, 2, 3, 4$:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `{{key:CLΣ}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $0.00000000$ | `0.` |
| 02 | `1.25` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $1.25000000$ | `1.25_` |
| 03 | `{{key:ENTER}}` | $0.00000000$ | $0.00000000$ | $1.25000000$ | $1.25000000$ | `1.25_` |
| 04 | `10` | $0.00000000$ | $0.00000000$ | $1.25000000$ | $10.0000000$ | `10._` |
| 05 | `{{key:Σ+}}` | $0.00000000$ | $0.00000000$ | $1.25000000$ | $1.00000000$ | `1.` |
| 06 | `2.45 {{key:ENTER}}` | $0.00000000$ | $1.25000000$ | $2.45000000$ | $2.45000000$ | `2.45_` |
| 07 | `20 {{key:Σ+}}` | $0.00000000$ | $1.25000000$ | $2.45000000$ | $2.00000000$ | `2.` |
| 08 | `3.80 {{key:ENTER}}` | $1.25000000$ | $2.45000000$ | $3.80000000$ | $3.80000000$ | `3.80_` |
| 09 | `30 {{key:Σ+}}` | $1.25000000$ | $2.45000000$ | $3.80000000$ | $3.00000000$ | `3.` |
| 10 | `4.95 {{key:ENTER}}` | $2.45000000$ | $3.80000000$ | $4.95000000$ | $4.95000000$ | `4.95_` |
| 11 | `40 {{key:Σ+}}` | $2.45000000$ | $3.80000000$ | $4.95000000$ | $4.00000000$ | `4.` |

Opening the `{{key:SUMS}}` menu lets us audit all six hardware accumulators at a glance: `{{key:Σx}}` holds **`100.00000000`** kPa, `{{key:Σy}}` holds **`12.45000000`** V, `{{key:Σx²}}` holds **`3000.00000000`**, `{{key:Σy²}}` holds **`46.50750000`**, `{{key:Σxy}}` holds **`373.50000000`**, and `{{key:n}}` confirms **`4`** calibration points. Switching to the linear regression menu (`{{key:L.R.}}`), pressing `{{key:m}}` reveals a sensitivity slope of **`0.1245000000 V/kPa`** ($124.50\text{ mV/kPa}$), pressing `{{key:b}}` returns a zero-pressure intercept of **`0.0000000000 V`**, and pressing `{{key:r}}` reports a Pearson correlation of **`0.9995648074`**. Notice the physical significance of that `0.0000` intercept: even though the individual readings wobbled slightly below and above the line ($2.45\text{ V}$ at $20\text{ kPa}$, $3.80\text{ V}$ at $30\text{ kPa}$), Gauss's least-squares fit proves that the sensor has zero baseline offset error and needs no null trimming.

With the calibration line established, we can translate between pressure and voltage along two complementary pathways. Using the built-in linear regression predictors (`{{key:L.R.}}` $\to$ `{{key:ŷ}}` and `{{key:x̂}}`), keying `25 {{key:L.R.}} {{key:ŷ}}` immediately forecasts **`3.1125000000 V`** at $25\text{ kPa}$ (while Register $Y$ automatically receives Pearson's $r = 0.9995648074$ for instant fit verification), and keying `4.00 {{key:L.R.}} {{key:x̂}}` inverts the line at $4.00\text{ V}$ to recover **`32.128514 kPa`**. Equivalently, we can cross-check both predictions explicitly on the 4-level stack using `{{key:m}}` and `{{key:b}}`: keying `25 {{key:L.R.}} {{key:m}} {{key:×}} {{key:L.R.}} {{key:b}} {{key:+}}` evaluates $\hat{y} = mx + b = \mathbf{3.1125000000\text{ V}}$, while `4.00 {{key:L.R.}} {{key:b}} {{key:-}} {{key:L.R.}} {{key:m}} {{key:÷}}` evaluates $\hat{x} = (y - b)/m = \mathbf{32.128514\text{ kPa}}$. Moreover, as Francis Anscombe famously warned in 1973, a single corrupted outlier at the edge of the domain can wrench a least-squares regression line off course while still leaving a deceptively high correlation coefficient: if the fourth pressure calibration reading at $40\text{ kPa}$ were corrupted by a $+4.00\text{ V}$ electromagnetic transient into $(40, 8.95)$ alongside $(10, 1.25), (20, 2.45), (30, 3.80)$, querying `{{key:r}}` ($0.9277$) and `{{key:m}}` ($0.2445\text{ V/kPa}$) exposes the skewed sensitivity slope immediately, and executing `8.95 {{key:ENTER}} 40 {{key:Σ-}}` followed by `4.95 {{key:ENTER}} 40 {{key:Σ+}}` excises the spike in place and restores the true slope $m = \mathbf{0.1245\text{ V/kPa}}$ without clearing the dataset.

Whether you are correlating student exam performance against study hours or extracting the thermal conductivity of carbon steel from a guarded hot plate, least-squares regression averages out random scatter to isolate the underlying rate constant. Consider an engineering professor who tracks how preparation hours ($x$) relate to midterm exam scores ($y$) across four study cohorts: $(2\text{ hr}, 62\%)$, $(5\text{ hr}, 74\%)$, $(8\text{ hr}, 85\%)$, and $(12\text{ hr}, 96\%)$. Once those four bivariate observations (`62 {{key:ENTER}} 2 {{key:Σ+}}`, `74 {{key:ENTER}} 5 {{key:Σ+}}`, `85 {{key:ENTER}} 8 {{key:Σ+}}`, and `96 {{key:ENTER}} 12 {{key:Σ+}}`) are accumulated, the marginal return on study time (`{{key:m}}` $\rightarrow$ **`3.402 %/hr`**) and baseline preparation score (`{{key:b}}` $\rightarrow$ **`56.29 %`**) are immediately available to the linear predictor `10 {{key:ŷ}}`, which interpolates the expected $10\text{-hour}$ score (**`90.31%`**) in Register $X$ while simultaneously returning Pearson's correlation $r = 0.9960$ in Register $Y$ ($Y = 0.9960,\; X = \mathbf{90.3059}\%$).

In the same way, in 1822 Jean-Baptiste Joseph Fourier established that steady-state heat flux $q''$ ($\text{W/m}^2$) flowing through a solid bar is directly proportional to the temperature gradient $dT/dx$: $q'' = -k (dT/dx)$. By measuring $q''$ across three axial temperature gradients in a metallurgical test rig—$(50\text{ K/m}, 2100\text{ W/m}^2)$, $(100\text{ K/m}, 4220\text{ W/m}^2)$, and $(150\text{ K/m}, 6310\text{ W/m}^2)$—and regressing steady-state heat flux $q''$ ($Y$) against axial temperature gradient $|dT/dx|$ ($X$) via `2100 {{key:ENTER}} 50 {{key:Σ+}}`, `4220 {{key:ENTER}} 100 {{key:Σ+}}`, and `6310 {{key:ENTER}} 150 {{key:Σ+}}`, we average out thermocouple contact noise across multiple power settings and isolate the Fourier thermal conductivity of AISI 1010 carbon steel ($X = \mathbf{42.1000\text{ W/(m}\cdot\text{K)}}$, or **`42.10 W/(m·K)`**) via `{{key:m}}`.

### Working-Hotelling Confidence Bands, Prediction Bands & Spearman's Rank Correlation ($r_s$)

How tightly have the $n = 4$ calibration points of our piezoresistive pressure sensor ($n = 4, \bar{x} = 25.0\text{ kPa}, \hat{y}_0 = 3.1125\text{ V}, s_e = 0.058095\text{ V}$) pinned down the *true average calibration line* $E(y \mid x_0)$ at $x_0 = 25\text{ kPa}$? Because the least-squares line pivots through the centroid $(\bar{x}, \bar{y})$ and can wobble slightly in both height ($\sqrt{1/n}$) and slope, the 95% confidence band around the regression line follows an hourglass-shaped hyperbola that is narrowest right at the center $x_0 = \bar{x}$:

$$\hat{y}_0 \pm t_{\alpha/2, n-2} \cdot s_e \sqrt{\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{\Sigma x^2 - \frac{(\Sigma x)^2}{n}}}$$

Because the hyperbolic Working-Hotelling confidence band reaches its minimum width at the calibration centroid $x_0 = \bar{x} = 25.0\text{ kPa}$ (where $(x_0 - \bar{x})^2 = 0$), the margin of error reduces to $t_{0.025, 2} \cdot s_e \sqrt{1/4} = 4.303 \times 0.058095 \times 0.5 = \mathbf{0.1250\text{ V}}$. Multiplying the critical Student's $t$-quantile by the standard error `4.303 {{key:ENTER}} 0.058095 {{key:×}}` ($X = 0.2500$) and scaling by the centroid sample factor $\sqrt{1/n}$ via `4 {{key:1/x}} {{key:√x}} {{key:×}}` ($X = 0.1250$) places the margin of error $E = \mathbf{0.1250\text{ V}}$ directly in Register $X$. Instead of re-keying $E$ and $\hat{y}_0 = 3.1125\text{ V}$ twice, exploit {{key:x⇄y}} and {{key:LASTX}}: keying `3.1125 {{key:x⇄y}} {{key:-}}` subtracts the waiting $E$ from $\hat{y}_0$ to establish the lower confidence bound $\hat{y}_0 - E = \mathbf{2.9875\text{ V}}$ while automatically saving $E = 0.1250\text{ V}$ in LASTX, and keying `{{key:LASTX}} 2 {{key:×}} {{key:+}}` adds $2E = 0.2500\text{ V}$ to resolve the upper confidence bound $\hat{y}_0 + E = \mathbf{3.2375\text{ V}}$ ($\mathbf{[2.9875\text{ V}, 3.2375\text{ V}]}$) with $\hat{y}_0$ typed once and $E$ never re-typed.

Now contrast that mean-response confidence band with a subtle question that trips up many engineers: instead of bounding the *average line* $E(y \mid x_0)$, what if you want a $95\%$ **prediction band** for a **single future voltage reading** $y_{\text{new}}$ when the manifold is pressurized to $x_0 = 25\text{ kPa}$ tomorrow? A single future reading suffers from two independent sources of uncertainty—the uncertainty in where the true line sits ($\frac{1}{n} + \dots$) *plus* the intrinsic noise of that one new observation ($+1$ inside the square root):

$$s_{\text{pred}} = s_e \sqrt{1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{\Sigma x^2 - \frac{(\Sigma x)^2}{n}}}$$

At the centroid $x_0 = 25\text{ kPa}$, adding unit variance ($+1$) inside the radical yields $s_{\text{pred}} = 0.058095 \times \sqrt{1 + 0.25} = 0.058095 \times 1.118034 = 0.06495\text{ V}$. Evaluating the dispersion factor $\sqrt{1 + 1/n}$ via `4 {{key:1/x}} 1 {{key:+}} {{key:√x}}` ($X = 1.1180$) and scaling by $s_e$ and $t_{0.025, 2}$ (`0.058095 {{key:×}} 4.303 {{key:×}}`) leaves the prediction margin $E_{\text{pred}} = \mathbf{0.2795\text{ V}}$ in Register $X$. Applying the same {{key:LASTX}} interval reflection, key `3.1125 {{key:x⇄y}} {{key:-}}` to obtain the lower prediction limit $\hat{y}_0 - E_{\text{pred}} = \mathbf{2.8330\text{ V}}$ while capturing $E_{\text{pred}}$ in LASTX, then key `{{key:LASTX}} 2 {{key:×}} {{key:+}}` to add $2 E_{\text{pred}}$ and reach the upper prediction limit $\hat{y}_0 + E_{\text{pred}} = \mathbf{3.3920\text{ V}}$ ($\mathbf{[2.8330\text{ V}, 3.3920\text{ V}]}$) without re-keying either operand.

What if two variables clearly rise together—say, the Mohs scratch hardness of five ceramic coatings and their service lifetimes under abrasive wear—but their relationship is strongly curved or measured on an ordinal ranking scale where Pearson's linear correlation $r$ gets distorted? In 1904, English psychologist Charles Spearman showed that if you replace the raw numbers with their integer ranks ($1, 2, \dots, n$) and compute the rank differences $d_i = \text{rank}(x_i) - \text{rank}(y_i)$, Pearson's formula simplifies into the non-parametric **Spearman rank correlation** $r_s$:

$$r_s = 1 - \frac{6 \Sigma d_i^2}{n(n^2 - 1)}$$

For five ceramic coatings whose rank differences are $d = [1, -1, 2, -1, -1]$, the squared rank differences sum to $\Sigma d_i^2 = 1^2 + (-1)^2 + 2^2 + (-1)^2 + (-1)^2 = 8.0$, while the denominator for $n = 5$ is $n(n^2 - 1) = 5(24) = 120$. Evaluating the numerator $6\Sigma d_i^2 = 48$ and denominator $n(n^2-1) = 120$ on the stack and subtracting their quotient $48/120 = 0.40$ from $1$ via `{{res:sc32_09_statistics_curve_fitting_seq_05:keys}}` yields Spearman's rank correlation **`0.6000`**:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `6 {{key:ENTER}} 8 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $48.0000$ | $6 \Sigma d_i^2 = 6 \times 8$ |
| 02 | `5 {{key:ENTER}} 24 {{key:×}}` | $0.0000$ | $0.0000$ | $48.0000$ | $120.0000$ | $n(n^2 - 1) = 5 \times 24$ |
| 03 | `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.4000$ | Quotient $48 / 120 = 0.40$ |
| 04 | `1 {{key:x⇄y}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | **`0.6000`** | Spearman rank correlation $r_s = 1 - 0.40$ |

---

## The Gaussian Normal Distribution, Hypothesis Testing & Reliability Laws

### The Galton Board Quincunx: Why Chaos Gives Birth to the Bell Curve

In 1873, Victorian polymath Francis Galton built a vertical wooden board packed with rows of alternating brass pins—the Quincunx.

He dropped thousands of small steel ball bearings from a single funnel at the top. At each pin, an individual ball has a purely random 50/50 choice: bounce left or bounce right. Down through 12 rows of pins, every single trajectory is wildly unpredictable chaos.

Yet, when the 10,000 balls settle into the vertical glass slots at the bottom, something remarkable happens: they *never* form a flat line. They *never* form a jagged heap. Invariably, with geometric precision, they sculpt the smooth bell curve of Carl Friedrich Gauss.

**Why?** Because to land at the extreme left, a ball must bounce left 12 times in a row (probability 1 in 4,096). But to land in the center, there are 924 different intertwined paths of lefts and rights.

This is the **Central Limit Theorem**: when millions of tiny, independent, random disturbances push against a physical measurement (air molecules, thermal noise, lathe blade vibrations), their sum *always* converges to the Gaussian Normal PDF.

The continuous Gaussian Normal probability density function models stochastic error, dimensional tolerances, sensor noise, and natural phenomena:

$$f(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)$$

where:
* $\mu$ is the distribution mean (center of symmetry).
* $\sigma$ is the standard deviation (scale parameter).
* $Z = \frac{x - \mu}{\sigma}$ is the dimensionless standard score (Z-score).

The normalized standard normal distribution with $\mu = 0$ and $\sigma = 1$ is:
$$\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2 / 2}$$

### Evaluating the Normal PDF on the RPN Stack
On an algebraic calculator, $f(x)$ requires 8 levels of parentheses. On the SC-32, the parenthesis-free RPN stack decomposes the Gaussian density into a five-step linear progression:

1. **Compute $(x - \mu)^2$:** $x$ `{{key:ENTER}}` $\mu$ `{{key:-}} {{key:x²}}`
2. **Compute $2\sigma^2$:** $\sigma$ `{{key:x²}} 2 {{key:×}}`
3. **Exponent argument:** `{{key:÷}} {{key:+/-}} {{key:eˣ}}`
4. **Denominator $\sigma\sqrt{2\pi}$:** $\sigma$ `{{key:ENTER}} 2 {{key:π}} {{key:×}} {{key:√x}} {{key:×}}`
5. **Final PDF quotient:** `{{key:÷}}`

How tall is that Gaussian bell curve at exactly one standard deviation above the mean ($Z = +1.0$, where the curve bends through its inflection point)? On a standardized psychometric or quality-control scale with population mean $\mu = 100$ and standard deviation $\sigma = 15$, let us evaluate the probability density $f(x)$ at $x = 115$ from the inside out with zero parentheses:

$$f(115; 100, 15) = \frac{1}{15\sqrt{2\pi}} \exp\left(-\frac{(115 - 100)^2}{2(15^2)}\right)$$

Working outward from the innermost deviation, we first square the residual $(115 - 100)^2$ via `{{res:sc32_09_statistics_curve_fitting_seq_11:keys}}` ($225.0$), form the variance denominator $2\sigma^2$ via `{{res:sc32_09_statistics_curve_fitting_seq_12:keys}}` ($450.0$), and evaluate the Gaussian exponential factor `{{key:÷}} {{key:+/-}} {{key:eˣ}}` ($0.6065306597$); building the normalization constant $\sigma\sqrt{2\pi}$ in Register $X$ via `{{res:sc32_09_statistics_curve_fitting_seq_13:keys}}` ($37.59942412$) while the exponential factor waits in Register $Y$ and dividing via `{{key:÷}}` resolves the exact probability density **`0.0161313817`**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `115 {{key:ENTER}}` | $0.00000000$ | $0.00000000$ | $115.000000$ | $115.000000$ | `115._` |
| 02 | `100 {{key:-}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $15.0000000$ | `15._` |
| 03 | `{{key:x²}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $225.000000$ | `225._` |
| 04 | `15 {{key:x²}}` | $0.00000000$ | $0.00000000$ | $225.000000$ | $225.000000$ | `225._` |
| 05 | `2 {{key:×}}` | $0.00000000$ | $0.00000000$ | $225.000000$ | $450.000000$ | `450._` |
| 06 | `{{key:÷}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $0.50000000$ | `0.5_` |
| 07 | `{{key:+/-}} {{key:eˣ}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $0.60653066$ | `0.60653066_` |
| 08 | `15 {{key:ENTER}}` | $0.00000000$ | $0.60653066$ | $15.0000000$ | $15.0000000$ | `15._` |
| 09 | `2 {{key:π}}` | $0.60653066$ | $15.0000000$ | $2.00000000$ | $3.14159265$ | `3.14159265_` |
| 10 | `{{key:×}} {{key:√x}}` | $0.60653066$ | $0.60653066$ | $15.0000000$ | $2.50662827$ | `2.50662827_` |
| 11 | `{{key:×}}` | $0.60653066$ | $0.60653066$ | $0.60653066$ | $37.5994241$ | `37.59942412_` |
| 12 | `{{key:÷}}` | $0.60653066$ | $0.60653066$ | $0.60653066$ | $0.01613138$ | `0.0161313817` |

### Cumulative Probability $\Phi(z)$ via Romberg Quadrature
Having found the height of the bell curve at $Z = +1.0$, what fraction of a normal population falls at or below $Z = +1.0$? The cumulative probability $\Phi(z) = P(Z \le z)$ represents the area under the Gaussian curve:
$$\Phi(z) = \frac{1}{2} + \frac{1}{\sqrt{2\pi}} \int_0^z e^{-t^2 / 2} \, dt$$

Because the bell curve is perfectly symmetric about $Z = 0$ (whose left half contains $0.5000000000$ of the area), we can pair Chapter 8's Adaptive Romberg Quadrature (`{{key:∫}}`) over the compact interval $[0, 1.0]$ with simple stack arithmetic to evaluate $\Phi(1.0) = \int_{-\infty}^{1.0} \phi(z)\,dz$:

$$\Phi(1.0) = 0.5000000000 + \frac{1}{\sqrt{2\pi}} \int_0^{1.0} e^{-t^2 / 2} \, dt$$

Integrating the unnormalized Gaussian kernel $\int_0^1 e^{-t^2 / 2} \, dt \approx 0.8556243919$ and multiplying by $\frac{1}{\sqrt{2\pi}} \approx 0.3989422804$ gives $0.3413447460$ for the probability slice between the mean and $+1\sigma$; adding the left-half area $0.5000000000$ yields $\mathbf{0.8413447460}$ ($84.13\%$), confirming the famous $1\sigma$ Empirical Rule ($68.27\% - 95.45\% - 99.73\%$) that $2 \times 34.134\% = 68.27\%$ of a normally distributed population lies within $\pm 1\sigma$ of the mean. With the unnormalized Gaussian integrand $e^{-x^2/2}$ (`X {{key:x²}} 2 {{key:÷}} {{key:+/-}} {{key:eˣ}}`) active in `{{key:EQN}}` mode, four stack steps deliver the cumulative probability:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `0 {{key:ENTER}} 1.0` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $1.00000000$ | Push integration limits $a=0, b=1.0$ |
| 02 | `{{key:∫}}` | $0.00000000$ | $0.00000000$ | $1.15 \times 10^{-12}$ | $0.85562439$ | Romberg quadrature $\int_0^1 e^{-t^2/2}dt$ |
| 03 | `2 {{key:π}} {{key:×}} {{key:√x}} {{key:÷}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $0.34134475$ | Divide by $\sqrt{2\pi}$; area from mean to $Z=1.0$ |
| 04 | `0.5 {{key:+}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | **$0.84134475$** | Cumulative probability $\Phi(1.0)$ ($84.13\%$) |

### William Sealy Gosset's ("Student's") Two-Sample $t$-Test

How do we test whether two small samples genuinely differ when we do not know the true population standard deviation $\sigma$? In 1908, William Sealy Gosset—head experimental brewer at the Guinness brewery in Dublin, publishing under the pseudonym *"Student"* so competitors wouldn't realize Guinness was using statistics to test barley batches—solved this exact problem. Suppose an aerospace metallurgist pulls tensile coupons from two titanium-aluminum alloy heats: Alloy A yields $n_1 = 8$ samples with mean $\bar{x}_1 = 450.0\text{ MPa}$ and standard deviation $s_1 = 12.5\text{ MPa}$, while Alloy B yields $n_2 = 10$ samples with mean $\bar{x}_2 = 468.0\text{ MPa}$ and standard deviation $s_2 = 14.0\text{ MPa}$. Is Alloy B's $+18.0\text{ MPa}$ higher average tensile strength a genuine metallurgical improvement, or just a lucky draw from noisy test coupons? We pool the two sample variances weighted by their Bessel degrees of freedom ($n_1 - 1 = 7$ and $n_2 - 1 = 9$, giving $df = n_1 + n_2 - 2 = 16$) and evaluate Student's $t$-statistic directly on the stack:

$$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}, \qquad t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$$

In the numerator of the pooled variance $s_p^2$, Alloy A contributes $(8 - 1) \times 12.5^2 = 7 \times 156.25 = 1093.75$ and Alloy B contributes $(10 - 1) \times 14.0^2 = 9 \times 196.0 = 1764.0$; dividing their sum by the $df = 8 + 10 - 2 = 16$ combined degrees of freedom gives $s_p^2 = 2857.75 / 16 = 178.609375$, or a pooled standard deviation of $s_p = \sqrt{178.609375} \approx 13.36448\text{ MPa}$. Scaling $s_p$ by the sample-size factor $\sqrt{1/8 + 1/10} = \sqrt{0.225} \approx 0.4743416$ yields a two-sample standard error of $6.33933\text{ MPa}$, so dividing the mean difference $\bar{x}_1 - \bar{x}_2 = 450.0 - 468.0 = -18.0\text{ MPa}$ by $6.33933\text{ MPa}$ produces $t = \mathbf{-2.8394}$. We can synthesize the pooled standard error in Register $X$, stage the mean difference $\bar{x}_1 - \bar{x}_2$ above it, and swap-divide in one continuous RPN stream via `7 {{key:ENTER}} 12.5 {{key:x²}} {{key:×}} 9 {{key:ENTER}} 14 {{key:x²}} {{key:×}} {{key:+}} 16 {{key:÷}} {{key:√x}} 8 {{key:1/x}} 10 {{key:1/x}} {{key:+}} {{key:√x}} {{key:×}} 450 {{key:ENTER}} 468 {{key:-}} {{key:x⇄y}} {{key:÷}}` to obtain **`-2.8394`**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `7 {{key:ENTER}} 12.5 {{key:x²}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1093.7500$ | $(n_1 - 1)s_1^2$ evaluated |
| 2 | `9 {{key:ENTER}} 14 {{key:x²}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2857.7500$ | Add $(n_2 - 1)s_2^2$ numerator sum |
| 3 | `16 {{key:÷}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $13.364482$ | Divide by $df = 16$; $s_p = \sqrt{s_p^2}$ |
| 4 | `8 {{key:1/x}} 10 {{key:1/x}} {{key:+}} {{key:√x}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $6.339330$ | Standard error of difference $SE$ |
| 5 | `450 {{key:ENTER}} 468 {{key:-}}` | $0.0000$ | $0.0000$ | $6.339330$ | $-18.0000$ | Mean difference $\bar{x}_1 - \bar{x}_2$ |
| 6 | `{{key:x⇄y}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$-2.839422$** | Student's $t = -18.0 / SE$ |

The stack resolves to **$t = -2.8394$**; because $|-2.8394|$ exceeds the two-tailed critical threshold $t_{0.025, 16} = 2.120$ at $\alpha = 0.05$, we reject $H_0$ and confirm that Alloy B's higher tensile strength is statistically significant.

### Discrete Arrivals & Aging Survival: Poisson's PMF & Weibull's Reliability Law

Beyond continuous Gaussian measurements and small-sample $t$-tests, engineering reliability often hinges on discrete random arrivals and aging survival curves. Whenever discrete events arrive independently at a constant average rate $\lambda$—photons striking a deep-space CCD pixel, alpha particles clicking in a Geiger counter, or data packets hitting a core network router—the probability of observing exactly $k$ arrivals in a unit time window is governed by Siméon Denis Poisson's 1837 probability mass function (PMF), $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$. Suppose a high-speed optical router receives an average of $\lambda = 4.5\text{ packets/ms}$, and we want to know the probability that a random $1\text{-ms}$ window brings a burst of exactly $k = 6$ packets. Raising the arrival rate $\lambda = 4.5$ to the sixth power, multiplying by the exponential waiting factor $e^{-4.5}$, and dividing by $6!$ via `{{res:sc32_09_statistics_curve_fitting_seq_06:keys}}` determines the exact burst probability **`{{res:sc32_09_statistics_curve_fitting_seq_06:value}}`** ($12.81\%$):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `4.5 {{key:ENTER}}` | $0.00000000$ | $0.00000000$ | $4.50000000$ | $4.50000000$ | `4.5_` |
| 02 | `6 {{key:yˣ}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $8303.76562$ | `8303.76562_` |
| 03 | `4.5 {{key:+/-}}` | $0.00000000$ | $0.00000000$ | $8303.76562$ | $-4.5000000$ | `-4.5_` |
| 04 | `{{key:eˣ}}` | $0.00000000$ | $0.00000000$ | $8303.76562$ | $0.01110900$ | `0.01110900_` |
| 05 | `{{key:×}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $92.2465384$ | `92.2465384_` |
| 06 | `6 {{key:x!}}` | $0.00000000$ | $0.00000000$ | $92.2465384$ | $720.000000$ | `720._` |
| 07 | `{{key:÷}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $0.12812019$ | `0.12812019` |

*(**`LASTX` Single-Entry Poisson Evaluation:** Notice that in $\frac{\lambda^k e^{-\lambda}}{k!}$, both $\lambda = 4.5$ and $k = 6$ appear twice. Keying `4.5 {{key:+/-}} {{key:eˣ}} {{key:LASTX}} {{key:+/-}} 6 {{key:yˣ}} {{key:LASTX}} {{key:x!}} {{key:÷}} {{key:×}}` evaluates $e^{-4.5}$, recovers $-4.5$ from `LASTX` and negates it to $+4.5$, raises $4.5^6$ while saving $6$ in `LASTX`, recalls $6$ from `LASTX` for `{{key:x!}}`, divides $4.5^6 / 6!$, and multiplies by $e^{-4.5}$—typing `4.5` and `6` only once each.)*

While radioactive atoms and Poisson packet arrivals have no memory of how old they are ($\beta = 1$), mechanical ball bearings, turbine blades, and ceramic capacitors wear out over time: the longer a bearing spins under load, the more microscopic subsurface spalling cracks accumulate. In 1951, Swedish engineer Waloddi Weibull unified infant-mortality failures ($\beta < 1$), memoryless random failures ($\beta = 1$), and aging wear-out failures ($\beta > 1$) into a single survival law, $R(t) = \exp\left( -\left(\frac{t}{\eta}\right)^\beta \right)$, where $\eta = 5000\text{ hours}$ is the characteristic life scale parameter (the age at which $e^{-1} \approx 36.79\%$ of bearings survive) and $\beta = 1.8$ is the wear-out shape parameter. What fraction of a fleet of spindle ball bearings will survive to $t = 3000\text{ operating hours}$ without failure? Normalizing the service age by characteristic life ($t/\eta = 3000/5000$), raising that dimensionless life ratio to the wear-out exponent $\beta = 1.8$, and exponentiating the negated hazard via `{{res:sc32_09_statistics_curve_fitting_seq_09:keys}}` reveals a fleet survival probability of **`0.6712`** ($67.12\%$):

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `3000 {{key:ENTER}} 5000 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.6000$ | Operating ratio $t/\eta = 3000/5000 = 0.6$ |
| 02 | `1.8 {{key:yˣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.398660$ | Raise to shape parameter $\beta = 1.8$ ($0.6^{1.8} \approx 0.3987$) |
| 03 | `{{key:+/-}} {{key:eˣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | **`0.6712`** | Weibull reliability $R(3000) = \exp(-0.3987) \approx 0.6712$ ($67.12\%$) |

Even better, when reliability engineers test a fleet of bearings to failure and record their cumulative failure fractions $(t_i, F_i)$ following $R(t) = 1 - F(t) = \exp(-(t/\eta)^\beta)$, taking the double logarithm $y' = \ln(-\ln(1 - F_i))$ (`1 {{key:x⇄y}} {{key:-}} {{key:LN}} {{key:+/-}} {{key:LN}}`) against the log-time $x' = \ln t_i$ (`{{key:LN}} {{key:Σ+}}`) linearizes Weibull's survival curve into the straight line $y' = \beta \ln t - \beta \ln \eta$ right on the stack—so querying `{{key:L.R.}} {{key:m}}` extracts the Weibull wear-out shape parameter $\beta = m$ directly and `{{key:b}} {{key:m}} {{key:÷}} {{key:+/-}} {{key:eˣ}}` recovers the characteristic life $\eta = \exp(-b/m)$.

---

## Non-Linear Transformations via Stack Pre-Processing

Nature rarely limits herself to straight lines. Radioactive isotopes decay exponentially ($y = a e^{bx}$); wind turbines extract aerodynamic power in proportion to the cube of wind speed ($y = a x^b$); and catalytic enzymes saturate along a rectangular hyperbola ($y = \frac{x}{a + bx}$).

On a conventional spreadsheet calculator, fitting a non-linear model forces you to create auxiliary columns or hunt through specialized curve-fit submenus. On the SC-32, because `{{key:Σ+}}` simply accumulates whatever numbers sit in Registers $Y$ and $X$ at the instant you press it, **the RPN stack acts as a live coordinate lens**. Before tapping `{{key:Σ+}}`, you can apply `{{key:LN}}` or `{{key:1/x}}` directly to $y$, $x$, or both—bending an exponential, power-law, or hyperbolic curve into a straight line right on the stack!

| Model | Standard Equation | Stack Pre-Processing | Linearized Fit Equation | Parameters Recovered |
| :--- | :--- | :--- | :--- | :--- |
| **Linear** | $y = m x + b$ | $(y, x)$ unmodified | $y = m x + b$ | $\text{Slope } m, \text{Intercept } b$ |
| **Exponential** | $y = a e^{b x}$ | $y \to \ln(y)$, $x \to x$ | $\ln(y) = \ln(a) + b x$ | $b = \text{Slope } m$, $a = e^{\text{Intercept } b}$ (`{{key:RCL}} b {{key:eˣ}}`) |
| **Power Law** | $y = a x^b$ | $y \to \ln(y)$, $x \to \ln(x)$ | $\ln(y) = \ln(a) + b \ln(x)$ | $b = \text{Slope } m$, $a = e^{\text{Intercept } b}$ (`{{key:RCL}} b {{key:eˣ}}`) |
| **Logarithmic** | $y = a + b \ln(x)$ | $y \to y$, $x \to \ln(x)$ | $y = a + b \ln(x)$ | $b = \text{Slope } m$, $a = \text{Intercept } b$ |
| **Reciprocal** | $\frac{1}{y} = a + b x$ | $y \to 1/y$, $x \to x$ | $\frac{1}{y} = a + b x$ | $b = \text{Slope } m$, $a = \text{Intercept } b$ |
| **Hyperbolic** | $y = \frac{x}{a + b x}$ | $y \to 1/y$, $x \to 1/x$ | $\frac{1}{y} = b + a \left(\frac{1}{x}\right)$ | $a = \text{Slope } m$, $b = \text{Intercept } b$ |

Once you have accumulated the transformed coordinates via `{{key:Σ+}}`, the standard linear regression keys (`{{key:L.R.}} {{key:m}}` and `{{key:b}}`) recover the underlying physical constants immediately:
* **Exponential ($y = a e^{bx}$):** Taking the natural logarithm of $y$ turns multiplication into addition, $\ln y = \ln a + bx$. The exponential rate constant is the slope $b = m$, and exponentiating the intercept (`{{key:b}} {{key:eˣ}}`) recovers the initial amplitude $a = e^b$.
* **Power Law ($y = a x^b$):** Taking `{{key:LN}}` of both $y$ and $x$ maps the power curve onto log-log space, $\ln y = \ln a + b \ln x$. The scaling exponent is the slope $b = m$, and `{{key:b}} {{key:eˣ}}` recovers the proportionality constant $a = e^b$.
* **Logarithmic ($y = a + b\ln x$) & Reciprocal ($1/y = a + bx$):** Transforming only $x \to \ln x$ or $y \to 1/y$ yields the rate parameter directly in the slope $m$ and the baseline offset in the intercept $b$.
* **Hyperbolic ($y = \frac{x}{a + bx}$):** Taking the double reciprocal (`{{key:1/x}}` on both $y$ and $x$, as in Lineweaver-Burk enzyme kinetics) yields $\frac{1}{y} = b + a\left(\frac{1}{x}\right)$, where the slope $m$ recovers $a$ and the intercept $b$ recovers the saturation ceiling.

### Exponential Decay, Wind Turbine Power Laws & Lineweaver-Burk Enzyme Kinetics

Let us test all three coordinate lenses—semi-log (`{{key:LN}}` on $y$), log-log (`{{key:LN}}` on both $y$ and $x$), and double-reciprocal (`{{key:1/x}}` on both $y$ and $x$)—on real laboratory and field telemetry. In nuclear medicine, Technetium-99m ($^{99\text{m}}\text{Tc}$) is the workhorse gamma-ray tracer used in cardiac and bone scans because it decays rapidly enough to minimize patient radiation dose. Suppose a hospital physicist logs four ionization-chamber activity readings over a 6-hour shift: $(0\text{ hr}, 1000\text{ MBq})$, $(2\text{ hr}, 794\text{ MBq})$, $(4\text{ hr}, 630\text{ MBq})$, and $(6\text{ hr}, 500\text{ MBq})$. Clearing the statistical registers via `{{key:CLΣ}}` and taking the natural logarithm (`{{key:LN}}`) of the measured nuclear activity $A(t)$ as each point is entered—`1000 {{key:LN}} 0 {{key:Σ+}}`, `794 {{key:LN}} 2 {{key:Σ+}}`, `630 {{key:LN}} 4 {{key:Σ+}}`, and `500 {{key:LN}} 6 {{key:Σ+}}`—converts first-order Rutherford-Soddy decay $\ln A(t) = \ln A_0 - \lambda t$ into a linear trend whose slope `{{key:L.R.}} {{key:m}}` is $-\lambda =$ **`-0.11552`** $\text{hr}^{-1}$. Computing $\ln 2$ via `2 {{key:LN}}` lifts $-\lambda$ into Register $Y$ ($Y = -0.11552,\; X = 0.69315$), so `{{key:x⇄y}} {{key:+/-}} {{key:÷}}` forms $\ln(2)/\lambda$ directly on the stack to certify the clinical $^{99\text{m}}\text{Tc}$ half-life ($X =$ **`6.000 hours`**).

Now let us apply the log-log lens to see why a wind turbine barely trickles power in a gentle breeze, yet surges into a megawatt powerhouse when the wind speed doubles. Because a cylinder of air of cross-sectional area $A$ moving at speed $v$ delivers a mass flow rate $\dot{m} = \rho A v$, and each kilogram of air carries kinetic energy $\frac{1}{2}v^2$, the mechanical power flowing through the rotor swept area scales as $\frac{1}{2}\dot{m}v^2 \propto v^3$. Suppose field anemometer and generator telemetry log four operating points: $(v_1, P_1) = (4.0\text{ m/s}, 16.0\text{ kW})$, $(v_2, P_2) = (6.0\text{ m/s}, 54.0\text{ kW})$, $(v_3, P_3) = (8.0\text{ m/s}, 128.0\text{ kW})$, and $(v_4, P_4) = (10.0\text{ m/s}, 250.0\text{ kW})$. We can linearize the power law $P = k v^m$ into $\ln P = \ln k + m \ln v$ by pressing `{{key:LN}}` on each coordinate right on the stack before tapping `{{key:Σ+}}`, verifying both the cubic exponent $m$ and the turbine's scaling coefficient $k$.

After clearing the accumulators via `{{key:CLΣ}}` and logging the four log-log pairs (`16 {{key:LN}} 4 {{key:LN}} {{key:Σ+}}`, `54 {{key:LN}} 6 {{key:LN}} {{key:Σ+}}`, `128 {{key:LN}} 8 {{key:LN}} {{key:Σ+}}`, and `250 {{key:LN}} 10 {{key:LN}} {{key:Σ+}}`), querying `{{key:L.R.}} {{key:m}}` confirms the exact cubic power-law exponent (**`3.000000`**), while exponentiating the log-intercept `{{key:b}}` (`-1.386294`) via `{{key:eˣ}}` recovers the aerodynamic scaling coefficient **`0.250000 kW/(m/s)³`** for the empirical law **$P(v) = 0.250 v^3$**. Cubing the rated cut-in wind speed $v = 12.0\text{ m/s}$ and multiplying by the turbine constant via `{{res:sc32_09_statistics_curve_fitting_seq_14:keys}}` then forecasts **`{{res:sc32_09_statistics_curve_fitting_seq_14:value}}`** of electrical output:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `{{key:CLΣ}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $0.00000000$ | Clear all 6 statistical accumulators |
| 02 | `16 {{key:LN}} 4 {{key:LN}} {{key:Σ+}}` | $0.00000000$ | $0.00000000$ | $2.77258872$ | $1.00000000$ | Point 1 logged ($n=1$ in $X$, $\ln P_1$ in $Y$) |
| 03 | `54 {{key:LN}} 6 {{key:LN}} {{key:Σ+}}` | $0.00000000$ | $2.77258872$ | $3.98898405$ | $2.00000000$ | Point 2 logged ($n=2$ in $X$) |
| 04 | `128 {{key:LN}} 8 {{key:LN}} {{key:Σ+}}` | $2.77258872$ | $3.98898405$ | $4.85203026$ | $3.00000000$ | Point 3 logged ($n=3$ in $X$) |
| 05 | `250 {{key:LN}} 10 {{key:LN}} {{key:Σ+}}` | $3.98898405$ | $4.85203026$ | $5.52146092$ | $4.00000000$ | Point 4 logged ($n=4$ in $X$) |
| 06 | `{{key:L.R.}} {{key:m}}` | $3.98898405$ | $4.85203026$ | $5.52146092$ | **$3.00000000$** | Regression slope $m = 3.0$ (cubic power law) |
| 07 | `{{key:b}} {{key:eˣ}}` | $4.85203026$ | $5.52146092$ | $3.00000000$ | **$0.25000000$** | Intercept $b \implies k = e^b = 0.250\text{ kW/(m/s)}^3$ |
| 08 | `12 {{key:ENTER}} 3 {{key:yˣ}} 0.25 {{key:×}}` | $3.00000000$ | $3.00000000$ | $0.25000000$ | **$432.000000$** | Predicted power $P(12) = 0.25 \times 12^3\text{ kW}$ |

Just as `{{key:LN}}` straightens out a power law, `{{key:1/x}}` straightens out biochemical saturation. When you feed increasing concentrations of substrate $[S]$ to a catalytic enzyme, the reaction velocity $v$ follows Leonor Michaelis and Maud Menten's hyperbolic curve $v = \frac{V_{\max} [S]}{K_m + [S]}$. Because the curve bends toward an asymptote $V_{\max}$ that no finite test-tube concentration ever quite reaches, how can you measure $V_{\max}$ and the half-saturation constant $K_m$ accurately? In 1934, Hans Lineweaver and Dean Burk realized that taking the reciprocal (`{{key:1/x}}`) of both sides turns the hyperbola into the straight line $\frac{1}{v} = \frac{K_m}{V_{\max}}\frac{1}{[S]} + \frac{1}{V_{\max}}$. Given four kinetic assays at $([S]_1, v_1) = (2.0\text{ mM}, 0.182\text{ }\mu\text{M/min})$, $([S]_2, v_2) = (4.0\text{ mM}, 0.286\text{ }\mu\text{M/min})$, $([S]_3, v_3) = (8.0\text{ mM}, 0.400\text{ }\mu\text{M/min})$, and $([S]_4, v_4) = (16.0\text{ mM}, 0.471\text{ }\mu\text{M/min})$, streaming the double-reciprocal coordinates $(1/v_k, 1/[S]_k)$ into the accumulators via `{{res:sc32_09_statistics_curve_fitting_seq_17:keys}}` inverts the intercept `{{key:b}}` (`1.5759`) with `{{key:1/x}}` to isolate the maximum turnover velocity $V_{\max} =$ **`0.6346`** $\mu\text{M/min}$ in Register $X$, then queries the slope `{{key:m}}` (`7.7981` $= K_m / V_{\max}$, which lifts $V_{\max}$ into Register $Y$) so a single `{{key:×}}` stroke resolves the Michaelis constant $K_m =$ **`{{res:sc32_09_statistics_curve_fitting_seq_17:value}} mM`**:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `{{key:CLΣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Clear accumulators |
| 02 | `.182 {{key:1/x}} 2.0 {{key:1/x}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $5.4945$ | $1.0000$ | Point 1 logged ($1/v_1$ in $Y$, $1/[S]_1$ in $X$) |
| 03 | `.286 {{key:1/x}} 4.0 {{key:1/x}} {{key:Σ+}}` | $0.0000$ | $5.4945$ | $3.4965$ | $2.0000$ | Point 2 logged |
| 04 | `.400 {{key:1/x}} 8.0 {{key:1/x}} {{key:Σ+}}` | $5.4945$ | $3.4965$ | $2.5000$ | $3.0000$ | Point 3 logged |
| 05 | `.471 {{key:1/x}} 16.0 {{key:1/x}} {{key:Σ+}}` | $3.4965$ | $2.5000$ | $2.1231$ | $4.0000$ | Point 4 logged |
| 06 | `{{key:b}}` | $3.4965$ | $2.5000$ | $2.1231$ | **$1.5759$** | Intercept $1/V_{\max}$ |
| 07 | `{{key:1/x}}` | $3.4965$ | $2.5000$ | $2.1231$ | **$0.6346$** | Maximum velocity $V_{\max}$ ($\mu\text{M/min}$) |
| 08 | `{{key:m}}` | $2.5000$ | $2.1231$ | $0.6346$ | **$7.7981$** | Slope $K_m / V_{\max}$ (lifts $V_{\max}$ into $Y$) |
| 09 | `{{key:×}}` | $2.5000$ | $2.5000$ | $2.1231$ | **$4.9484$** | Michaelis constant $K_m = m \times V_{\max}$ (mM) |

> **Enzyme Active Sites & Saturation Kinetics:** Why does enzyme velocity $v([S])$ curve into a horizontal ceiling instead of rising forever (as we will plot directly on the 64-column viewport in **[Chapter 12](12-function-scatter-plotting.md)**)? An enzyme operates with a fixed number of catalytic active sites. At low substrate concentration ($[S] \ll K_m$), active sites sit idle waiting for substrate molecules to diffuse in, so reaction speed grows linearly with $[S]$ ($v \approx \frac{V_{\max}}{K_m}[S]$). At high substrate concentration ($[S] \gg K_m$), every single active site is continuously occupied—saturated at its maximum molecular turnover ceiling $V_{\max}$—and adding more substrate simply queues molecules outside the catalytic pocket. Taking reciprocals (`{{key:1/x}}`) via Hans Lineweaver and Dean Burk's (1934) transformation maps this saturation hyperbola onto a straight line whose $y$-intercept is $1/V_{\max}$.

### Modal Spreadsheet Lists vs. Streaming `{{key:Σ+}}` Register Accumulation

Streaming bivariate $(x, y)$ observations directly into the SC-32's six statistical accumulators eliminates the modal list-editor navigation required on conventional algebraic calculators:

| Challenge / Metric | Conventional Algebraic Calculator (Infix) | Algebraic Strokes | SC-32 RPN Stack Method | SC-32 Strokes | Stack Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **Bivariate Calibration Entry & Regression**: $(10, 1.25)$ to $(40, 4.95)$ | Open `STAT` $\to$ `Edit`, enter data row-by-row into lists $L_1$ and $L_2$, exit to `STAT` $\to$ `CALC` $\to$ `4:LinReg(ax+b)` $\to$ `Calculate` (36+ strokes). Stack is invisible during entry. | 36 | **Live Accumulator Bus (`{{key:Σ+}}`)**: Key $y$ `{{key:ENTER}}` $x$ `{{key:Σ+}}` directly on the stack (18 strokes). Screen tracks live sample count $n$. Press `{{key:L.R.}} {{key:m}}` and `{{key:b}}` for instant parameters without exiting the calculation. | 18 | **50% fewer strokes + continuous stack visibility** |
| **Outlier Retraction**: Deduct erroneous pair $(15, 5.3)$ from running statistics | Open `STAT` $\to$ `Edit`, scroll down 6 rows in $L_1$ and $L_2$, delete both entries or re-enter entire list, re-run `LinReg` (24 strokes). | 24 | **Instant Retraction (`{{key:Σ-}}`)**: Key `5.3 {{key:ENTER}} 15 {{key:Σ-}}` directly on the stack (6 strokes). All 6 hardware accumulators decrement instantaneously, and $n$ restores to 5. | 6 | **75% fewer strokes + zero list navigation** |
| **Gaussian Normal PDF**: Evaluate $f(115)$ for $\mu = 100, \sigma = 15$ | Formula typing: `1 / ( 1 5 * sqrt ( 2 * pi ) ) * e ^ ( - ( 1 1 5 - 1 0 0 ) ^ 2 / ( 2 * 1 5 ^ 2 ) )` (38 strokes). Requires 6 pairs of nested parentheses; high syntax error risk. | 38 | **Inside-Out Stack Decomposition**: `115 {{key:ENTER}} 100 {{key:-}} {{key:x²}} 15 {{key:x²}} 2 {{key:×}} {{key:÷}} {{key:+/-}} {{key:eˣ}} 15 {{key:÷}} 2 {{key:π}} {{key:×}} {{key:√x}} {{key:÷}}` (22 strokes). Zero parentheses, complete visual inspection of intermediate variance and tail probability. | 22 | **42% fewer strokes + zero parenthesis clutter** |

---

## Numerical Boundary Conditions & Singularity Guards

Before concluding our tour of the six statistical accumulators, it is worth pausing to see how Gauss's least-squares algebra behaves at geometric and sample-size boundaries. What happens if you accidentally log three data points that share the exact same $x$-coordinate—say $(10, 2)$, $(10, 5)$, and $(10, 9)$—and then ask for the linear regression slope `{{key:m}}`? Geometrically, three points stacked vertically above $x = 10$ define a vertical cliff with infinite slope; algebraically, the $x$-variance denominator $n \Sigma x^2 - (\Sigma x)^2$ vanishes identically to zero. Rather than returning a bogus number, the SC-32 flags **`STAT ERROR`** (Code 04) on the display. A single tap of `{{key:C}}` clears the error message while leaving all six accumulators untouched, so you can remove the duplicate reading with `{{key:Σ-}}` or add points across a non-zero $x$-domain.

A similar boundary arises if you try to query the sample standard deviation `{{key:sx}}` or `{{key:sy}}` after logging only a single data point ($n = 1$). Because a lone point sits right on top of its own average ($\bar{x} = x_1$), you have zero remaining degrees of freedom ($n - 1 = 0$) from which to estimate population spread! The calculator properly reports **`STAT ERROR`** (Code 04) until you accumulate at least $n = 2$ observations (though the population spread `{{key:σx}}`, which divides by $n$, evaluates cleanly to $0.0000$). Finally, if you ever calibrate a sensor and notice that the regression slope `{{key:m}}` looks like the *reciprocal* of what you expected—say $8.0321$ instead of $0.1245\text{ V/kPa}$—you have simply swapped the entry order of $x$ and $y$. In the classic RPN convention inherited from the HP-15C and HP-32SII, always key the dependent response $y$ first, press `{{key:ENTER}}` to lift it into Register $Y$, key the independent stimulus $x$ into Register $X$, and tap `{{key:Σ+}}`.

---

## Summary & Looking Ahead

Six dedicated hardware accumulators ($\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$) support bivariate means, sample standard deviations, covariance, and least-squares regression lines on the SC-32 without disturbing user storage registers. Inverse accumulation via `{{key:Σ-}}` excises outliers in place, while `{{key:ŷ}}` and `{{key:x̂}}` convert transducer voltages directly into calibrated physical measurements alongside Gaussian, Poisson, and Weibull probability models.

Continuous distributions and decimal floating-point arithmetic form only half of computational science. Beneath modern instrumentation lies the discrete digital architecture of binary bits, logic words, and memory addresses. In **[Chapter 10: Computer Science, Bases & 36-Bit Integers](10-computer-science-bases.md)**, you will explore the SC-32's authentic 36-bit two's complement integer architecture. You will navigate hexadecimal, decimal, octal, and binary bases while preserving stack integrity, execute modular integer division via `{{key:÷R}}` returning quotient in $X$ and remainder in $Y$, apply word-length masking and arithmetic bit-packing, calculate IPv4 CIDR subnet masks and packed RGB color channels, and master discrete combinatorics.
