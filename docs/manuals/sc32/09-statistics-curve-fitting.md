---
title: "Chapter 9: Bivariate Statistics, Curve Fitting & Linear Regression | SC-32 Manual"
description: "Master the 6 statistical accumulators, sample vs. population standard deviations, linear regression (m, b, r), prediction estimation, Gaussian Normal PDF, and scatter plotting on the StackCalc SC-32."
---

# Chapter 9: Bivariate Statistics, Curve Fitting & Linear Regression

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 STATISTICS // BIVARIATE DATA, PROBABILITY &amp; REGRESSION ANALYSIS</span>
  <span class="te-viewport-status text-sky-400">● 6 STATISTICAL ACCUMULATORS &bull; SAMPLE VS. POPULATION METRICS &bull; GAUSSIAN PDF &bull; PREDICTION ENGINE</span>
</div>

## The Celestial Drama: How 24-Year-Old Carl Friedrich Gauss Rediscovered Ceres (1801)

On the clear, cold evening of January 1, 1801, Italian astronomer Giuseppe Piazzi peered through his Ramsden circle telescope at the Palermo Observatory in Sicily and spotted a faint, uncataloged eighth-magnitude star moving against the starry backdrop of Taurus. Tracking the mysterious object across forty-one nights, Piazzi realized he had discovered a new wandering celestial body—a dwarf planet orbiting between Mars and Jupiter, which he christened *Ceres Ferdinandea*.

Then catastrophe struck.

By mid-February, Ceres drifted behind the blinding solar glare of the Sun. Astronomers across Europe desperately attempted to predict where the object would re-emerge in late autumn. But eighteenth-century celestial mechanics required months of continuous observations to calculate an elliptical orbit. Piazzi had captured only three degrees of orbital arc—barely one percent of its total trajectory across the heavens. Using traditional orbital approximations, Europe's foremost mathematicians computed orbits that pointed telescopes into empty sky. Ceres appeared irrevocably lost in the void.

Enter twenty-four-year-old **Carl Friedrich Gauss** in Göttingen.

Refusing to treat Piazzi's sparse observations as sterile, isolated geometric points, Gauss attacked the problem from a radically new perspective: **observational uncertainty**. Every telescope reading contained minute human, optical, and atmospheric errors. Rather than searching for a single hypothetical curve that passed exactly through flawed points, Gauss sought the unique elliptical orbit that minimized the sum of the squared deviations between prediction and observation.

In a whirlwind of superhuman arithmetic over three months in the autumn of 1801, Gauss invented the **Method of Least Squares** entirely in his head, along with what we now recognize as the **Gaussian Normal Distribution** of measurement errors {{cite:gauss1809}}. When German astronomer Franz Xaver von Zach pointed his telescope into the constellation Virgo on the night of December 31, 1801—guided exclusively by Gauss's least-squares predictions—Ceres was rediscovered within half a degree of Gauss's coordinates.

Gauss had demonstrated that statistical aggregation does not blur truth—it reveals the signal buried beneath the noise.

{{blocks:dice_spinner_probability|Dice Spinner Probability Calibration}}
*Figure 9.1: Physical probability mapping and discrete outcome distributions. The random fluctuations of physical trials converge systematically to smooth statistical distributions.*

{{blocks:dice_spinner_craftsmanship|Dice Spinner Mechanical Craftsmanship}}
*Figure 9.2: Precision CNC-machined dice spinner mechanism, demonstrating physical symmetry and mechanical tolerance analysis required for unbiased stochastic generation.*

Today, an engineer does not need weeks of manual quill-and-ink calculations to perform Gauss's least-squares synthesis. On the StackCalc SC-32, the **dual-variable statistical accumulation engine (`{{key:Σ+}}`)** automates Gauss's discovery directly on the RPN stack. Every time you enter a coordinate pair $(x, y)$ and tap `{{key:Σ+}}`, six dedicated hardware accumulators update instantaneously in continuous CMOS memory, calculating means, sample variances, covariance, and the least-squares regression line with certified 64-bit precision.

<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>{{key:ALL}}</code> (Full 15-digit internal IEEE-754 mantissa; Standard Base-10 Arithmetic; Degrees angular mode default). All stack operations assume the default 4-stack XYZT architecture.
</div>

---

{{res:sc32_normal_pdf:screenshot|Standard Normal PDF f(1.0) = exp(-0.5)/sqrt(2*pi) = 0.241970724519}}

## The Philosophy of Data in the Stack

In conventional algebraic calculators, statistical analysis is treated as an external, table-bound spreadsheet mode. The user enters a separate data grid, loses sight of the calculation stack, and must memorize cryptic sub-menu codes to retrieve basic parameters.

On the StackCalc SC-32, statistics is a first-class, dynamic extension of the Reverse Polish Notation operational stack. Data coordinates $(x, y)$ are entered directly into Registers $X$ and $Y$, transformed in real time using the full power of transcendental operators (`LN`, `1/x`, `x²`, `√x`), and committed into hardware accumulators with a single tap of `{{key:Σ+}}`.

### The SC-32 Statistical Pipeline

The statistical processing pipeline operates seamlessly between the operational stack and hardware accumulators:

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

### Data Entry Protocol: `{{key:Σ+}}`
Data pairs $(x_k, y_k)$ are entered according to the classic RPN convention:
1. Key in $y_k$ and press `{{key:ENTER}}` to push into Register $Y$.
2. Key in $x_k$ into Register $X$.
3. Press `{{key:Σ+}}` (Row 1, Column 6).

Upon pressing `{{key:Σ+}}`:
$$\Sigma x \leftarrow \Sigma x + x_k$$
$$\Sigma y \leftarrow \Sigma y + y_k$$
$$\Sigma x^2 \leftarrow \Sigma x^2 + x_k^2$$
$$\Sigma y^2 \leftarrow \Sigma y^2 + y_k^2$$
$$\Sigma xy \leftarrow \Sigma xy + (x_k \times y_k)$$
$$n \leftarrow n + 1$$

Register $X$ displays the current integer sample count $n$. Stack lift is disabled so that the next data pair can be typed immediately without clearing the display.

### Correcting Data Entry Errors: `{{key:Σ-}}`
If you mistype a data pair, re-enter the exact incorrect pair ($y \text{ in } Y, x \text{ in } X$) and press Left Shift `{{key:↰}}` followed by `{{key:Σ-}}`. The accumulators subtract the erroneous values and decrement $n$, restoring statistical integrity without restarting the dataset:
$$\Sigma x \leftarrow \Sigma x - x_k, \quad \Sigma y \leftarrow \Sigma y - y_k, \quad n \leftarrow n - 1$$

### Invariant Note on `LASTX`
As audited in Appendix A, pressing `{{key:Σ+}}` or `{{key:Σ-}}` **preserves `LASTX`**. It does not overwrite the previous arithmetic operand in `LASTX`.

### Clearing Statistics: {{key:CLEAR}} $\to$ `{{key:CLΣ}}`
Pressing Right Shift `{{key:↱}}` followed by `{{key:CLEAR}}` and selecting `{{key:CLΣ}}` (or invoking the dedicated statistical clear sequence) zeroes all six statistical registers.

---

## The Statistical Dynamic Softkey Menus

The SC-32 provides dedicated statistical softkey menus on the top 6 LFU dynamic keys:

| Sub-Menu | Primary Invocation | LFU 1 | LFU 2 | LFU 3 | LFU 4 | LFU 5 | LFU 6 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Sums Menu** | `{{key:SUMS}}` | `{{key:Σx}}` | `{{key:Σy}}` | `{{key:Σx²}}` | `{{key:Σy²}}` | `{{key:Σxy}}` | `{{key:n}}` |
| **2. Means Menu** | `{{key:x̄,ȳ}}` | `{{key:x̄}}` | `{{key:ȳ}}` | `{{key:x̄w}}` | — | — | — |
| **3. Std Dev Menu** | `{{key:s,σ}}` | `{{key:sx}}` | `{{key:sy}}` | `{{key:σx}}` | `{{key:σy}}` | — | — |
| **4. Regression Menu** | `{{key:L.R.}}` | `{{key:ŷ}}` | `{{key:x̂}}` | `{{key:r}}` | `{{key:m}}` | `{{key:b}}` | — |

### Mathematical Definitions

#### Sample Means ($\bar{x}, \bar{y}$)
$$\bar{x} = \frac{\Sigma x}{n}, \quad \bar{y} = \frac{\Sigma y}{n}$$

#### Weighted Mean ($\bar{x}_w$)
When $y_k$ represents the weighting factor (e.g., credit hours, mass, probability) and $x_k$ is the measurement:
$$\bar{x}_w = \frac{\Sigma xy}{\Sigma y}$$

#### Sample Standard Deviations ($s_x, s_y$)
Unbiased estimator using Bessel's correction with $n - 1$ degrees of freedom:
$$s_x = \sqrt{\frac{\Sigma x^2 - \frac{(\Sigma x)^2}{n}}{n - 1}} = \sqrt{\frac{n \Sigma x^2 - (\Sigma x)^2}{n(n - 1)}}$$
$$s_y = \sqrt{\frac{\Sigma y^2 - \frac{(\Sigma y)^2}{n}}{n - 1}} = \sqrt{\frac{n \Sigma y^2 - (\Sigma y)^2}{n(n - 1)}}$$

#### Population Standard Deviations ($\sigma_x, \sigma_y$)
Assumes the data set constitutes the entirety of the target population with $n$ degrees of freedom:
$$\sigma_x = \sqrt{\frac{\Sigma x^2 - \frac{(\Sigma x)^2}{n}}{n}}, \quad \sigma_y = \sqrt{\frac{\Sigma y^2 - \frac{(\Sigma y)^2}{n}}{n}}$$

#### Relationship Between Sample and Population Metrics
$$s = \sigma \sqrt{\frac{n}{n - 1}}$$

---

## Bivariate Linear Regression & Pearson Correlation ($r$)

Bivariate linear regression fits the best-fit line $y = m x + b$ using ordinary least squares (OLS) minimization of vertical squared residuals:

$$\text{Slope } m = \frac{\Sigma xy - \frac{\Sigma x \Sigma y}{n}}{\Sigma x^2 - \frac{(\Sigma x)^2}{n}} = \frac{n \Sigma xy - \Sigma x \Sigma y}{n \Sigma x^2 - (\Sigma x)^2}$$

$$\text{Intercept } b = \bar{y} - m \bar{x} = \frac{\Sigma y - m \Sigma x}{n}$$

$$\text{Pearson Correlation } r = \frac{n \Sigma xy - \Sigma x \Sigma y}{\sqrt{\left[ n \Sigma x^2 - (\Sigma x)^2 \right] \left[ n \Sigma y^2 - (\Sigma y)^2 \right]}}$$

The coefficient of determination $r^2$ represents the proportion of variance in $y$ predictable from $x$.

### Prediction Operators ($\hat{y}$ and $\hat{x}$)
* **Predicting $y$ from a given $x$ ($\hat{y}$):** Key in known $x$ and press `{{key:L.R.}} {{key:ŷ}}`:
  $$\hat{y} = m x + b$$
  In the SC-32 engine, `{{key:ŷ}}` returns the predicted $\hat{y}$ in Register $X$ and places the correlation coefficient $r$ in Register $Y$! This allows instant assessment of prediction quality without additional keystrokes.
* **Predicting $x$ from a given $y$ ($\hat{x}$):** Key in known $y$ and press `{{key:L.R.}} {{key:x̂}}`:
  $$\hat{x} = \frac{y - b}{m}$$

---

## The Gaussian Normal Distribution & Probability Density Function (PDF)

<div class="admonition tip">
<p class="admonition-title">The Galton Board Quincunx: Why Chaos Gives Birth to the Bell Curve</p>
<p>In 1873, Victorian polymath Francis Galton built a vertical wooden board packed with rows of alternating brass pins—the Quincunx.</p>
<p>He dropped thousands of small steel ball bearings from a single funnel at the top. At each pin, an individual ball has a purely random 50/50 choice: bounce left or bounce right. Down through 12 rows of pins, every single trajectory is wildly unpredictable chaos.</p>
<p>Yet, when the 10,000 balls settle into the vertical glass slots at the bottom, something magical happens: they <em>never</em> form a flat line. They <em>never</em> form a jagged heap. Invariably, with breathtaking geometric precision, they sculpt the smooth, silky bell curve of Carl Friedrich Gauss!</p>
<p><strong>Why?</strong> Because to land at the extreme left, a ball must bounce left 12 times in a row (probability 1 in 4,096). But to land in the center, there are 924 different intertwined paths of lefts and rights!</p>
<p>This is the <strong>Central Limit Theorem</strong>: when millions of tiny, independent, random disturbances push against a physical measurement (air molecules, thermal noise, lathe blade vibrations), their sum <em>always</em> converges to the Gaussian Normal PDF.</p>
</div>

The continuous Gaussian Normal probability density function models stochastic error, dimensional tolerances, sensor noise, and natural phenomena:

$$f(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)$$

where:
* $\mu$ is the distribution mean (center of symmetry).
* $\sigma$ is the standard deviation (scale parameter).
* $Z = \frac{x - \mu}{\sigma}$ is the dimensionless standard score (Z-score).

The normalized standard normal distribution with $\mu = 0$ and $\sigma = 1$ is:
$$\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2 / 2}$$

### Evaluating the Normal PDF on the RPN Stack
Evaluating $f(x)$ on an algebraic calculator requires 8 levels of parentheses. On the SC-32, the parenthesis-free RPN stack decomposes the equation into an elegant, linear progression:

> Step 1: Compute (x - μ)²:      x {{key:ENTER}} μ {{key:-}} {{key:x²}}
> Step 2: Compute 2σ²:           σ {{key:x²}} 2 {{key:×}}
> Step 3: Exponent argument:     {{key:÷}} {{key:+/-}} {{key:eˣ}}
> Step 4: Denominator σ√(2π):    σ {{key:ENTER}} 2 {{key:π}} {{key:×}} {{key:√x}} {{key:×}}
> Step 5: Final PDF quotient:    {{key:÷}}

### Cumulative Probability $\Phi(z)$ via Romberg Quadrature
The cumulative probability $\Phi(z) = P(Z \le z)$ represents the area under the Gaussian curve:
$$\Phi(z) = \frac{1}{2} + \frac{1}{\sqrt{2\pi}} \int_0^z e^{-t^2 / 2} \, dt$$

The SC-32's adaptive Romberg numerical quadrature solver {{key:∫}} evaluates this integral directly to 10 decimal places, reproducing the classic Empirical Rule ($68.27\% - 95.45\% - 99.73\%$).

---

## Non-Linear Transformations via Stack Pre-Processing

When empirical phenomena obey exponential, power, or logarithmic laws, the user can linearize data pairs on the stack *prior* to pressing `{{key:Σ+}}`.

| Model | Standard Equation | Stack Pre-Processing | Linearized Fit Equation | Parameters Recovered |
| :--- | :--- | :--- | :--- | :--- |
| **Linear** | $y = m x + b$ | $(y, x)$ unmodified | $y = m x + b$ | $\text{Slope } m, \text{Intercept } b$ |
| **Exponential** | $y = a e^{b x}$ | $y \to \ln(y)$, $x \to x$ | $\ln(y) = \ln(a) + b x$ | $b = \text{Slope } m$, $a = e^{\text{Intercept } b}$ (`{{key:RCL}} b {{key:eˣ}}`) |
| **Power Law** | $y = a x^b$ | $y \to \ln(y)$, $x \to \ln(x)$ | $\ln(y) = \ln(a) + b \ln(x)$ | $b = \text{Slope } m$, $a = e^{\text{Intercept } b}$ (`{{key:RCL}} b {{key:eˣ}}`) |
| **Logarithmic** | $y = a + b \ln(x)$ | $y \to y$, $x \to \ln(x)$ | $y = a + b \ln(x)$ | $b = \text{Slope } m$, $a = \text{Intercept } b$ |
| **Reciprocal** | $\frac{1}{y} = a + b x$ | $y \to 1/y$, $x \to x$ | $\frac{1}{y} = a + b x$ | $b = \text{Slope } m$, $a = \text{Intercept } b$ |
| **Hyperbolic** | $y = \frac{x}{a + b x}$ | $y \to 1/y$, $x \to 1/x$ | $\frac{1}{y} = b + a \left(\frac{1}{x}\right)$ | $a = \text{Slope } m$, $b = \text{Intercept } b$ |

After performing linear regression on transformed coordinates:
* For Exponential: $b = \text{Slope } m$, and scaling factor $a = e^{\text{Intercept } b}$ (`{{key:RCL}} b {{key:eˣ}}`).
* For Power Law: $b = \text{Slope } m$, and coefficient $a = e^{\text{Intercept } b}$ (`{{key:RCL}} b {{key:eˣ}}`).
* For Logarithmic: $b = \text{Slope } m$, and additive constant $a = \text{Intercept } b$.
* For Reciprocal: $b = \text{Slope } m$, and baseline offset $a = \text{Intercept } b$.
* For Hyperbolic: $a = \text{Slope } m$, and asymptotic factor $b = \text{Intercept } b$.

### The Algebraic Trap vs. StackCalc Superpower Showdown

| Challenge / Metric | Algebraic Trap (TI-84 / Infix) | Algebraic Strokes | StackCalc SC-32 Superpower | SC-32 Strokes | Superpower Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **Bivariate Calibration Entry & Regression**: $(10, 1.25)$ to $(40, 4.95)$ | Open `STAT` $\to$ `Edit`, enter data row-by-row into lists $L_1$ and $L_2$, exit to `STAT` $\to$ `CALC` $\to$ `4:LinReg(ax+b)` $\to$ `Calculate` (36+ strokes). Stack is invisible during entry. | 36 | **Live Accumulator Bus (`{{key:Σ+}}`)**: Key $y$ `{{key:ENTER}}` $x$ `{{key:Σ+}}` directly on the stack (18 strokes). Screen tracks live sample count $n$. Press `{{key:L.R.}} {{key:m}}` and `{{key:b}}` for instant parameters without exiting calculation! | 18 | **50% fewer strokes + continuous stack visibility** |
| **Outlier Retraction**: Deduct erroneous pair $(15, 5.3)$ from running statistics | Open `STAT` $\to$ `Edit`, scroll down 6 rows in $L_1$ and $L_2$, delete both entries or re-enter entire list, re-run `LinReg` (24 strokes). | 24 | **Instant Retraction (`{{key:Σ-}}`)**: Key `5.3 {{key:ENTER}} 15 {{key:Σ-}}` directly on the stack (6 strokes). All 6 hardware accumulators decrement instantaneously, and $n$ restores to 5. | 6 | **75% fewer strokes + zero list navigation** |
| **Gaussian Normal PDF**: Evaluate $f(115)$ for $\mu = 100, \sigma = 15$ | Formula typing: `1 / ( 1 5 * sqrt ( 2 * pi ) ) * e ^ ( - ( 1 1 5 - 1 0 0 ) ^ 2 / ( 2 * 1 5 ^ 2 ) )` (38 strokes). Requires 6 pairs of nested parentheses; high syntax error risk. | 38 | **Inside-Out Stack Decomposition**: `115 ENTER 100 - x² 15 x² 2 × ÷ +/- eˣ 15 ENTER 2 ENTER π × √x × ÷` (20 strokes). Zero parentheses, complete visual inspection of intermediate variance and tail probability. | 20 | **47% fewer strokes + zero parenthesis clutter** |

---

## Diagnostic Checkpoints & Singularity Handling

> [!CHECKPOINT]
> **Diagnostic Checkpoint 9.1: Zero Variance Singularity (`STAT ERROR`)**  
> If all entered $x$-values are identical (e.g., $(10, 2), (10, 5), (10, 9)$), attempting to solve for linear regression slope `{{key:m}}` triggers `STAT ERROR`.  
> *Cause:* The denominator $n \Sigma x^2 - (\Sigma x)^2 = 0$, representing an infinite vertical slope.  
> *Remedy:* Press `{{key:C}}` to dismiss the error message. Ensure $x$-coordinates span a non-zero domain.

> [!CHECKPOINT]
> **Diagnostic Checkpoint 9.2: Single-Point Standard Deviation (`STAT ERROR`)**  
> Attempting to compute sample standard deviations `{{key:sx}}` or `{{key:sy}}` with only $n = 1$ point triggers `STAT ERROR`.  
> *Cause:* Division by degrees of freedom $n - 1 = 0$.  
> *Remedy:* Accumulate at least two distinct data points before querying sample metrics.

> [!CHECKPOINT]
> **Diagnostic Checkpoint 9.3: Coordinate Orientation Diagnostic Verification**  
> If the linear regression slope on a sensor calibration displays as an inverse value (e.g. $8.0321$ instead of $m = 0.1245$), the $(x, y)$ coordinate entry order was inverted. In the standard RPN convention, key the dependent variable $y$ first, press `{{key:ENTER}}`, key the independent variable $x$, and tap `{{key:Σ+}}`.

---

## Teaching & Instrument Architecture Notes

### Least-Squares Geometry & Data Hygiene via {{key:Σ-}}
In secondary and university statistics, linear regression is frequently treated as a routine calculation: entering data, pressing compute, and recording $m$, $b$, and $r$. At its core, least-squares regression balances variance across bivariate distributions by minimizing the sum of squared vertical residuals $\sum (y_i - \hat{y}_i)^2$. Demonstrating this with collinear data ($r = 1.0000$) and observing the effect of a single outlier point illustrates outlier sensitivity directly. Furthermore, data hygiene is maintained through `{{key:Σ-}}`: re-entering an errant point and pressing `{{key:Σ-}}` performs exact inverse subtraction across all six accumulators, restoring pristine statistics without navigating multi-tiered spreadsheet menus.

### Sensor Calibration & Coordinate Orientation Discipline
Practical empirical science relies on sensor calibration. By logging transducer voltage against known physical reference states (such as temperature baths or hydrostatic pressures) and keying points with $y$ `{{key:ENTER}}` $x$ `{{key:Σ+}}`, the linear calibration slope $m$ and intercept $b$ are determined via `{{key:L.R.}}`. The estimation keys `{{key:ŷ}}` and `{{key:x̂}}` then translate raw voltages directly into physical quantities. The standard RPN coordinate convention positions the dependent variable $y$ in Register $Y$ and the independent variable $x$ in Register $X$. If a user inadvertently keys $x$ first, the resulting slope is inverted ($1/m$), which is diagnosed immediately and corrected with `{{key:x⇄y}}`.

### Dedicated Hardware Accumulators & LASTX Preservation
On vintage RPN calculators (such as the HP-32SII and HP-15C), statistical summation overwrote user storage registers $R_0$ through $R_5$, erasing user-stored matrix coefficients or intermediate constants. The SC-32 resolves this limitation by isolating its six 64-bit statistical accumulators ($\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$) from general user storage registers ($R_{00} \dots R_{29}$). Furthermore, tapping `{{key:Σ+}}` or `{{key:Σ-}}` preserves `{{key:LASTX}}` intact without overwriting your prior arithmetic operand, maintaining computational continuity across mixed scientific workflows.

---

## Engineering Design Briefing: The Astronomical Observatory & Semiconductor Quality Fab (Problems 9.1 through 9.45)

<div class="admonition warning">
<p class="admonition-title">Inside-Out Stack Architecture: Algebraic Trap vs. RPN Shortcut — Bivariate Calibration &amp; Real-Time Accumulator Registers</p>
<p><strong>The Algebraic Parenthesis Trap:</strong> Calibrating precision sensor arrays or analyzing bivariate experimental data on standard calculators requires entering data into a cumbersome matrix spreadsheet editor. Switching between spreadsheet data entry, calculation screens, and regression output disrupts cognitive flow, and verifying outliers requires navigating multi-tiered setup menus {{cite:gauss1809}}.</p>
<p><strong>The RPN Stack Shortcut:</strong> The SC-32 utilizes six dedicated hardware accumulators ($\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$) updated instantaneously via the physical coordinate key <code>{{key:Σ+}}</code> {{cite:hp15c1982,hp32sii1991}}. The engineer keys coordinate pairs directly into Registers $Y$ and $X$ and taps <code>{{key:Σ+}}</code>. Linear, exponential, logarithmic, and power curve fits are queried immediately from the keyboard without clearing the stack. Outliers are removed with equal simplicity using <code>{{key:Σ-}}</code>, updating regression slopes and correlation coefficients in under 5 milliseconds.</p>
</div>

The following 43 reference problems provide exhaustive coverage across industrial calibration, quality control, biomechanics, electrical engineering, materials science, and contest mathematics.

---

> **Thematic Arc I — Sensor Calibration & Ordinary Least-Squares Linear Regression (Problems 9.1–9.10):** We open by accumulating paired laboratory calibration data via `Σ+` and extracting slope, intercept, and Pearson $r$ in single keystrokes.

### Problem 9.1: Precision Piezoresistive Pressure Sensor Calibration
A piezoresistive pressure transducer is calibrated against hydrostatic standards across four reference pressures:
* $(x_1, y_1) = (10\text{ kPa}, 1.25\text{ V})$
* $(x_2, y_2) = (20\text{ kPa}, 2.45\text{ V})$
* $(x_3, y_3) = (30\text{ kPa}, 3.80\text{ V})$
* $(x_4, y_4) = (40\text{ kPa}, 4.95\text{ V})$

Determine the six hardware accumulators, slope $m$, intercept $b$, correlation $r$, predict voltage at $25\text{ kPa}$, and determine pressure when $V = 4.00\text{ V}$.

**Keystrokes:**
1. Clear statistics: {{key:CLEAR}} $\to$ `{{key:CLΣ}}`
2. Point 1: `1.25 {{key:ENTER}} 10 {{key:Σ+}}`
3. Point 2: `2.45 {{key:ENTER}} 20 {{key:Σ+}}`
4. Point 3: `3.80 {{key:ENTER}} 30 {{key:Σ+}}`
5. Point 4: `4.95 {{key:ENTER}} 40 {{key:Σ+}}`

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

#### Accumulator Audit:
* Press `{{key:SUMS}}`:
  * `{{key:Σx}}`: **`100.00000000`** kPa
  * `{{key:Σy}}`: **`12.45000000`** V
  * `{{key:Σx²}}`: **`3000.00000000`**
  * `{{key:Σy²}}`: **`46.50750000`**
  * `{{key:Σxy}}`: **`373.50000000`**
  * `{{key:n}}`: **`4`**

#### Regression Parameters:
* Slope $m$: `{{key:L.R.}} {{key:m}}` $\rightarrow$ **`0.1245000000 V/kPa`** ($124.50\text{ mV/kPa}$)
* Intercept $b$: `{{key:b}}` $\rightarrow$ **`0.0000000000 V`**
* Correlation $r$: `{{key:r}}` $\rightarrow$ **`0.9995648074`**

#### Estimations:
* Voltage at $25\text{ kPa}$: `25 {{key:L.R.}} {{key:ŷ}}` $\rightarrow$ **`3.1125000000 V`** (Register $Y$ holds $r = 0.9995648074$)
* Pressure at $4.00\text{ V}$: `4.00 {{key:L.R.}} {{key:x̂}}` $\rightarrow$ **`32.128514 kPa`**

> **Classroom Mentor Note:** Notice the pedagogical beauty of `0.0000` intercept. The sensor exhibits ideal zero-offset behavior without software trimming!

---

### Problem 9.2: Gaussian Normal PDF Evaluation at $Z = +1.0$
In a standardized cognitive intelligence metric with population mean $\mu = 100$ and standard deviation $\sigma = 15$, determine the probability density $f(x)$ for an individual score of $x = 115$ ($Z = +1.0$).

$$f(115; 100, 15) = \frac{1}{15\sqrt{2\pi}} \exp\left(-\frac{(115 - 100)^2}{2(15^2)}\right)$$

**Keystrokes:**
1. `{{res:sc32_09_statistics_curve_fitting_seq_11:keys}}` $\rightarrow$ $225.0$
2. `{{res:sc32_09_statistics_curve_fitting_seq_12:keys}}` $\rightarrow$ $450.0$
3. `{{key:÷}} {{key:+/-}} {{key:eˣ}}` $\rightarrow$ $0.6065306597$
4. `{{res:sc32_09_statistics_curve_fitting_seq_13:keys}}` $\rightarrow$ $37.59942412$
5. `{{key:÷}}` $\rightarrow$ **`0.0161313817`**

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

---

### Problem 9.3: Gaussian Normal PDF Peak at the Mean ($Z = 0$)
Calculate the maximum height (mode) of the normal distribution for $\mu = 100, \sigma = 15$ at $x = 100$.

$$f(100) = \frac{1}{15\sqrt{2\pi}} e^0 = \frac{1}{15\sqrt{2\pi}}$$

**Keystrokes:** `{{res:sc32_09_statistics_curve_fitting_seq_01:keys}}` $\rightarrow$ **`{{res:sc32_09_statistics_curve_fitting_seq_01:value}}`**

> ***The Inside-Out Radical & Gaussian Normal Peak Pipeline*** — Evaluate $\sqrt{2\pi}$ in place, scale by standard deviation $\sigma$, and invert directly with `{{key:1/x}}` without parentheses {{cite:gauss1809,hp15c1982}}.

Keying `15 {{key:ENTER}}` places $\sigma = 15.0$ in Register $Y$ and $X$ $(T: 0.0000, Z: 0.0000, Y: 15.0000, X: 15.0000)$. Keying `2 {{key:π}} {{key:×}} {{key:√x}}` calculates the radical normalizer $\sqrt{2\pi} \approx 2.5066$ in Register $X$, preserving $\sigma = 15.0$ in Register $Y$ $(T: 0.0000, Z: 0.0000, Y: 15.0000, X: 2.5066)$. Striking `{{key:×}}` multiplies $Y$ and $X$, forming the dispersion denominator $\sigma\sqrt{2\pi} \approx 37.5994$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 37.5994)$. Pressing `{{key:1/x}}` takes the reciprocal in place, yielding the peak modal probability density $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{0.02659615})$.

At the mean, the exponential term collapses to $e^0 = 1$. The entire density resolves in 7 keystrokes with zero scratch registers.

---

### Problem 9.4: Gaussian Normal PDF at $Z = +2.0$ ($x = 130$)
Calculate the probability density for a score two standard deviations above the mean ($x = 130$).

$$f(130) = \frac{1}{15\sqrt{2\pi}} e^{-2^2 / 2} = \frac{e^{-2}}{15\sqrt{2\pi}}$$

**Keystrokes:** `{{res:sc32_09_statistics_curve_fitting_seq_02:keys}}` $\rightarrow$ **`{{res:sc32_09_statistics_curve_fitting_seq_02:value}}`**

> ***The Inside-Out Exponential & Standardized Deviation*** — Compute standard normal tail factor $e^{-Z^2/2}$ in place and divide by dispersion denominator directly within the 4-register stack {{cite:ellenberg2014,hp15c1982}}.

Entering `2 {{key:+/-}} {{key:eˣ}}` evaluates the Gaussian tail exponential factor $e^{-2} \approx 0.135335$ directly into Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.1353)$. Keying `15 {{key:ENTER}} 2 {{key:π}} {{key:×}} {{key:√x}} {{key:×}}` builds the full Gaussian dispersion denominator $15\sqrt{2\pi} \approx 37.5994$ in Register $X$, lifting the tail exponential factor into Register $Y$ $(T: 0.1353, Z: 0.1353, Y: 0.1353, X: 37.5994)$. Striking `{{key:÷}}` divides the tail factor by the dispersion denominator, resolving the exact tail probability density $(T: 0.1353, Z: 0.1353, Y: 0.1353, X: \mathbf{0.00359940})$.

---

### Problem 9.5: Cumulative Normal Probability via Romberg Quadrature ($Z = 1.0$)
Evaluate the cumulative probability $\Phi(1.0) = \int_{-\infty}^{1.0} \phi(z)\,dz$.
By symmetry:
$$\Phi(1.0) = 0.5000000000 + \frac{1}{\sqrt{2\pi}} \int_0^{1.0} e^{-t^2 / 2} \, dt$$

#### Analytical Integral:
$$\int_0^1 e^{-t^2 / 2} \, dt \approx 0.8556243919$$
Scaling factor: $\frac{1}{\sqrt{2\pi}} \approx 0.3989422804$.
Area above mean: $0.8556243919 \times 0.3989422804 = 0.3413447460$.
Total cumulative probability: $0.5000000000 + 0.3413447460 = \mathbf{0.8413447460}$ ($84.13\%$).
This confirms that $2 \times 34.134\% = 68.27\%$ of the population lies within $\pm 1\sigma$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `0 {{key:ENTER}} 1.0` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $1.00000000$ | Push integration limits $a=0, b=1.0$ |
| 02 | `{{key:∫}}` | $0.00000000$ | $0.00000000$ | $1.15 \times 10^{-12}$ | $0.85562439$ | Romberg quadrature $\int_0^1 e^{-t^2/2}dt$ |
| 03 | `2 {{key:π}} {{key:×}} {{key:√x}} {{key:÷}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $0.34134475$ | Divide by $\sqrt{2\pi}$; area from mean to $Z=1.0$ |
| 04 | `0.5 {{key:+}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | **$0.84134475$** | Cumulative probability $\Phi(1.0)$ ($84.13\%$) |

---

### Problem 9.6: Cumulative Normal Probability Critical Z-Score ($Z = 1.96$)
Evaluate $\Phi(1.96)$ for the two-tailed 95% confidence interval ($\alpha = 0.05$).

$$\int_0^{1.96} e^{-t^2/2} \, dt = 1.1906427$$
Scaling by $1/\sqrt{2\pi}$: $1.1906427 \times 0.39894228 = 0.475000$.
Cumulative probability: $0.500000 + 0.475000 = \mathbf{0.975000}$ ($97.50\%$).

Executing `0 {{key:ENTER}} 1.96` loads integration limits $a = 0$ in $Y$ and $b = 1.96$ in $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.9600)$. Pressing `{{key:∫}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.19064270)$ runs adaptive Romberg quadrature on $e^{-t^2/2}$, placing the converged integral $1.19064270$ in Register $X$ and the truncation error estimate ($2.04 \times 10^{-12}$) in Register $Y$. Keying `2 {{key:π}} {{key:×}} {{key:√x}} {{key:÷}}` divides the integral by $\sqrt{2\pi}$, yielding the one-tailed probability above the mean: $0.47500000$ in Register $X$. Striking `0.5 {{key:+}}` adds the lower half-plane probability, resolving the cumulative standard score $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{0.97500000})$ ($97.50\%$).

---

### Problem 9.7: Cumulative Normal Probability at $Z = 2.576$ (99% Two-Tailed)
Evaluate $\Phi(2.576)$ ($\alpha = 0.01$).

$$\int_0^{2.576} e^{-t^2/2} \, dt = 1.240767$$
Scaling: $1.240767 \times 0.39894228 = 0.495000$.
Cumulative probability: $0.500000 + 0.495000 = \mathbf{0.995000}$ ($99.50\%$).

Pushing `0 {{key:ENTER}} 2.576` establishes interval $[0, 2.576]$ across Registers $Y$ and $X$. Pressing `{{key:∫}}` $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.24076700)$ executes Romberg integration, returning definite integral $1.24076700$ in Register $X$. Keying `2 {{key:π}} {{key:×}} {{key:√x}} {{key:÷}}` normalizes by $\sqrt{2\pi}$ in place, producing one-sided deviation probability $0.49500000$ in $X$. Striking `0.5 {{key:+}}` computes the total cumulative distribution function value $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{0.99500000})$ ($99.50\%$).

---

### Problem 9.8: Wind Turbine Aerodynamic Power Curve (Cubic Power Law)
Wind turbine mechanical output power obeys $P = k v^3$. Given empirical measurements:
* $(v_1, P_1) = (4.0\text{ m/s}, 16.0\text{ kW})$
* $(v_2, P_2) = (6.0\text{ m/s}, 54.0\text{ kW})$
* $(v_3, P_3) = (8.0\text{ m/s}, 128.0\text{ kW})$
* $(v_4, P_4) = (10.0\text{ m/s}, 250.0\text{ kW})$

Linearize via $(x' = \ln v, y' = \ln P)$ and extract exponent $m$ and scaling coefficient $k$.

**Keystrokes:**
1. `{{key:CLΣ}}`
2. Point 1: `16 {{key:LN}} 4 {{key:LN}} {{key:Σ+}}`
3. Point 2: `54 {{key:LN}} 6 {{key:LN}} {{key:Σ+}}`
4. Point 3: `128 {{key:LN}} 8 {{key:LN}} {{key:Σ+}}`
5. Point 4: `250 {{key:LN}} 10 {{key:LN}} {{key:Σ+}}`
6. Slope: `{{key:L.R.}} {{key:m}}` $\rightarrow$ **`3.000000`** (Exact cubic power!)
7. Intercept: `{{key:b}}` $\rightarrow$ **`-1.386294`**
8. Scaling factor: `{{key:eˣ}}` $\rightarrow$ **`0.250000 kW/(m/s)³`**

Empirical model: **$P(v) = 0.250 v^3$**.
Predict power at cut-in rated speed $v = 12.0\text{ m/s}$:
`{{res:sc32_09_statistics_curve_fitting_seq_14:keys}}` $\rightarrow$ **`{{res:sc32_09_statistics_curve_fitting_seq_14:value}}`**.

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

---

### Problem 9.9: Semiconductor Diode Shockley I-V Curve (Exponential Fit)
A silicon diode satisfies $I = I_s e^{V / V_T}$.
* $(V_1, I_1) = (0.55\text{ V}, 0.24\text{ mA})$
* $(V_2, I_2) = (0.60\text{ V}, 1.65\text{ mA})$
* $(V_3, I_3) = (0.65\text{ V}, 11.40\text{ mA})$
* $(V_4, I_4) = (0.70\text{ V}, 78.50\text{ mA})$

**Keystrokes:**
1. `{{key:CLΣ}}`
2. `.24 {{key:LN}} .55 {{key:Σ+}}`
3. `1.65 {{key:LN}} .60 {{key:Σ+}}`
4. `11.40 {{key:LN}} .65 {{key:Σ+}}`
5. `78.50 {{key:LN}} .70 {{key:Σ+}}`
6. Slope: `{{key:L.R.}} {{key:m}}` $\rightarrow$ **`38.6015`** ($\text{V}^{-1}$)
7. Thermal voltage: `{{key:1/x}}` $\rightarrow$ **`0.025905 V`** ($25.91\text{ mV}$ at $300\text{ K}$)
8. Intercept: `{{key:b}}` $\rightarrow$ **`-22.6583`**
9. Reverse saturation current $I_s$: `{{key:eˣ}}` $\rightarrow$ $\mathbf{1.444 \times 10^{-10}\text{ mA}}$ ($1.444 \times 10^{-13}\text{ A}$).

Transforming currents via `{{key:LN}}` before coordinate accumulation linearizes the exponential Shockley equation into the six hardware accumulators. Querying `{{key:L.R.}} {{key:m}}` resolves the regression slope $m = 1/V_T = 38.6015\text{ V}^{-1}$ in Register $X$. Inverting via `{{key:1/x}}` immediately isolates thermal voltage $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{0.02590572}\text{ V})$. Pressing `{{key:b}} {{key:eˣ}}` extracts the vertical intercept $\ln I_s = -22.6583$ and exponentiates in place to reveal reverse saturation current $I_s = 1.444 \times 10^{-10}\text{ mA}$ without writing down intermediate logarithms.

---

### Problem 9.10: Michaelis-Menten Enzyme Kinetics (Lineweaver-Burk Double Reciprocal)
Enzyme reaction velocity $v$ follows $v = \frac{V_{\max} [S]}{K_m + [S]}$, linearized as $\frac{1}{v} = \frac{K_m}{V_{\max}}\frac{1}{[S]} + \frac{1}{V_{\max}}$.
* $([S]_1, v_1) = (2.0\text{ mM}, 0.182\text{ }\mu\text{M/min})$
* $([S]_2, v_2) = (4.0\text{ mM}, 0.286\text{ }\mu\text{M/min})$
* $([S]_3, v_3) = (8.0\text{ mM}, 0.400\text{ }\mu\text{M/min})$
* $([S]_4, v_4) = (16.0\text{ mM}, 0.471\text{ }\mu\text{M/min})$

**Keystrokes:**
1. `{{key:CLΣ}}`
2. `.182 {{key:1/x}} 2.0 {{key:1/x}} {{key:Σ+}}`
3. `.286 {{key:1/x}} 4.0 {{key:1/x}} {{key:Σ+}}`
4. `.400 {{key:1/x}} 8.0 {{key:1/x}} {{key:Σ+}}`
5. `.471 {{key:1/x}} 16.0 {{key:1/x}} {{key:Σ+}}`
6. Intercept: `{{key:b}}` $\rightarrow$ **`1.5759`** ($1/V_{\max}$)
7. $V_{\max} = 1/b$: `{{key:1/x}}` $\rightarrow$ **`0.6346`** $\mu\text{M/min}$
8. Slope: `{{key:m}}` $\rightarrow$ **`7.7981`** ($K_m / V_{\max}$)
9. $K_m = m \times V_{\max}$: `{{key:×}}` $\rightarrow$ **`4.9484 mM`** (Single-key dyadic multiplication!).

**Keystrokes:** `{{res:sc32_09_statistics_curve_fitting_seq_17:keys}}` $\rightarrow$ **`{{res:sc32_09_statistics_curve_fitting_seq_17:value}} mM`**

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

---

> **Thematic Arc II — Linearized Exponential, Logarithmic & Power-Law Models (Problems 9.11–9.20):** By transforming variables on the stack before `Σ+`, we fit radioactive decay, Enzyme kinetics, and Weibull failure data.

### Problem 9.11: Radioactive Decay Half-Life ($N = N_0 e^{-\lambda t}$)
Activity measurements of Technetium-99m over time:
* $(0\text{ hr}, 1000\text{ MBq})$
* $(2\text{ hr}, 794\text{ MBq})$
* $(4\text{ hr}, 630\text{ MBq})$
* $(6\text{ hr}, 500\text{ MBq})$

**Keystrokes:**
1. `{{key:CLΣ}}`
2. `1000 {{key:LN}} 0 {{key:Σ+}}`
3. `794 {{key:LN}} 2 {{key:Σ+}}`
4. `630 {{key:LN}} 4 {{key:Σ+}}`
5. `500 {{key:LN}} 6 {{key:Σ+}}`
6. Slope: `{{key:L.R.}} {{key:m}}` $\rightarrow$ **`-0.11552`** $\text{hr}^{-1}$ ($\lambda$)
7. Half-life $t_{1/2} = \frac{\ln 2}{\lambda}$: `2 {{key:LN}} {{key:x⇄y}} {{key:+/-}} {{key:÷}}` $\rightarrow$ **`6.000 hours`**.

Natural log transforms $\ln(N)$ linearize the exponential decay into slope $m = -\lambda$. Querying `{{key:L.R.}} {{key:m}}` places $-\lambda = -0.11552\text{ hr}^{-1}$ in Register $X$. Keying `2 {{key:LN}}` evaluates $\ln 2 \approx 0.69315$, lifting $-\lambda$ into Register $Y$ $(T: 0.0000, Z: 0.0000, Y: -0.11552, X: 0.69315)$. Striking `{{key:x⇄y}} {{key:+/-}} {{key:÷}}` exchanges registers, negates the denominator to positive $\lambda$, and divides, displaying certified radioisotope half-life $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{6.0000}\text{ hours})$ directly.

---

### Problem 9.12: Arrhenius Chemical Reaction Activation Energy
Reaction rate constant $k$ measured at different Kelvin temperatures:
$\ln k = \ln A - \frac{E_a}{R}\frac{1}{T}$
* $(T_1, k_1) = (300\text{ K}, 0.0014\text{ s}^{-1})$
* $(T_2, k_2) = (320\text{ K}, 0.0082\text{ s}^{-1})$
* $(T_3, k_3) = (340\text{ K}, 0.0385\text{ s}^{-1})$

Stack entry: $y' = \ln k, x' = 1/T$.
1. `.0014 {{key:LN}} 300 {{key:1/x}} {{key:Σ+}}`
2. `.0082 {{key:LN}} 320 {{key:1/x}} {{key:Σ+}}`
3. `.0385 {{key:LN}} 340 {{key:1/x}} {{key:Σ+}}`
4. Slope: `{{key:m}}` $\rightarrow$ **`-8451.92 K`** (equals $-E_a / R$)
5. Activation energy $E_a$: `8.314462618 {{key:×}} {{key:+/-}}` $\rightarrow$ **`70,273 J/mol`** ($70.27\text{ kJ/mol}$).

Dual transformation (`LN` on rate constant $k$ in $Y$, `1/x` on absolute temperature $T$ in $X$) maps raw kinetics into linear Arrhenius coordinates. Querying `{{key:m}}` returns slope $m = -E_a / R = -8451.92\text{ K}$ in Register $X$. Keying molar gas constant `8.314462618 {{key:×}} {{key:+/-}}` scales and negates the slope in a single dyadic product, yielding activation energy $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{70273.15}\text{ J/mol})$ with zero scratchpad memory.

---

### Problem 9.13: Hooke's Law Spring Constant Calibration
Force $F$ vs. elongation $\Delta x$:
* $(0.02\text{ m}, 5.0\text{ N})$
* $(0.04\text{ m}, 9.9\text{ N})$
* $(0.06\text{ m}, 15.1\text{ N})$
* $(0.08\text{ m}, 20.0\text{ N})$

1. `5.0 {{key:ENTER}} .02 {{key:Σ+}}`
2. `9.9 {{key:ENTER}} .04 {{key:Σ+}}`
3. `15.1 {{key:ENTER}} .06 {{key:Σ+}}`
4. `20.0 {{key:ENTER}} .08 {{key:Σ+}}`
5. Spring constant $k = m$: `{{key:L.R.}} {{key:m}}` $\rightarrow$ **`250.5 N/m`**
6. Intercept: `{{key:b}}` $\rightarrow$ **`-0.03 N`**
7. Correlation: `{{key:r}}` $\rightarrow$ **`0.99998`**.

Accumulating $(F_i, \Delta x_i)$ pairs directly commits running linear coordinates into the hardware registers. Querying `{{key:L.R.}} {{key:m}}` resolves spring constant $k = 250.5000\text{ N/m}$ in Register $X$. Pressing `{{key:b}}` extracts initial preload offset $b = -0.0300\text{ N}$, while `{{key:r}}` certifies near-perfect linearity with $r = 0.99998$.

---

### Problem 9.14: Precision Resistor Ohm's Law V-I Sweep
Voltage vs. Current across precision shunt:
* $(I = 0.10\text{ A}, V = 1.002\text{ V})$
* $(I = 0.20\text{ A}, V = 2.005\text{ V})$
* $(I = 0.50\text{ A}, V = 5.012\text{ V})$

1. `1.002 {{key:ENTER}} .10 {{key:Σ+}}`
2. `2.005 {{key:ENTER}} .20 {{key:Σ+}}`
3. `5.012 {{key:ENTER}} .50 {{key:Σ+}}`
4. Resistance $R = m$: `{{key:m}}` $\rightarrow$ **`10.0250 Ω`**.

Keying voltage in $Y$ and current in $X$ accumulates $V$-$I$ coordinate pairs. Pressing `{{key:m}}` extracts the regression slope $dV/dI$, resolving the four-wire precision shunt resistance $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{10.0250}\ \Omega)$ instantaneously.

---

### Problem 9.15: NTC Thermistor Beta Parameter Extraction
Thermistor resistance $R = R_0 e^{\beta (1/T - 1/T_0)}$ linearized as $\ln R = C + \beta (1/T)$.
* $(T_1 = 273.15\text{ K}, R_1 = 32,650\text{ }\Omega)$
* $(T_2 = 298.15\text{ K}, R_2 = 10,000\text{ }\Omega)$
* $(T_3 = 323.15\text{ K}, R_3 = 3,530\text{ }\Omega)$

1. `32650 {{key:LN}} 273.15 {{key:1/x}} {{key:Σ+}}`
2. `10000 {{key:LN}} 298.15 {{key:1/x}} {{key:Σ+}}`
3. `3530 {{key:LN}} 323.15 {{key:1/x}} {{key:Σ+}}`
4. Slope $\beta = m$: `{{key:m}}` $\rightarrow$ **`3924.95 K`**.

Pre-transforming $(R, T)$ into $(\ln R, 1/T)$ before statistical accumulation fits the exponential Steinhart-Hart curve to linear accumulators. Querying `{{key:m}}` yields the thermistor material constant $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{3924.95}\text{ K})$ directly.

---

### Problem 9.16: Boyle's Law Isothermal Gas Compression
Ideal gas isothermal pressure-volume relation: $\ln P = \ln C - \ln V$.
* $(V = 100\text{ mL}, P = 1.00\text{ atm})$
* $(V = 50\text{ mL}, P = 2.01\text{ atm})$
* $(V = 25\text{ mL}, P = 3.98\text{ atm})$

1. `1.00 {{key:LN}} 100 {{key:LN}} {{key:Σ+}}`
2. `2.01 {{key:LN}} 50 {{key:LN}} {{key:Σ+}}`
3. `3.98 {{key:LN}} 25 {{key:LN}} {{key:Σ+}}`
4. Slope: `{{key:m}}` $\rightarrow$ **`-0.9962`** (Confirms $P \propto V^{-1}$)
5. Intercept: `{{key:b}} {{key:eˣ}}` $\rightarrow$ **`98.5946 atm·mL`** ($C = e^b$).

Logging both pressure and volume verifies power-law behavior. Tapping `{{key:m}}` returns slope $m = -0.9962 \approx -1.0$. Striking `{{key:b}} {{key:eˣ}}` recovers the isothermal compression constant $(T: 0.0000, Z: 0.0000, Y: -0.9964, X: \mathbf{98.5946}\text{ atm}\cdot\text{mL})$.

---

### Problem 9.17: Acoustic Inverse Square Law
Sound intensity $I = \frac{P}{4\pi r^2} \implies \ln I = \ln K - 2 \ln r$.
* $(r = 1\text{ m}, I = 100\text{ W/m}^2)$
* $(r = 2\text{ m}, I = 25\text{ W/m}^2)$
* $(r = 4\text{ m}, I = 6.25\text{ W/m}^2)$

1. `100 {{key:LN}} 1 {{key:LN}} {{key:Σ+}}`
2. `25 {{key:LN}} 2 {{key:LN}} {{key:Σ+}}`
3. `6.25 {{key:LN}} 4 {{key:LN}} {{key:Σ+}}`
4. Slope: `{{key:m}}` $\rightarrow$ **`-2.000000`** (Exact inverse-square exponent!).

Natural logarithmic coordinates linearize spherical geometric spreading. Tapping `{{key:m}}` confirms the geometric attenuation power $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{-2.000000})$ with zero residual error.

---

### Problem 9.18: Traffic Flow Greenshields Model
Speed $v$ vs. Density $k$: $v = v_f (1 - k / k_j) = v_f - (v_f / k_j) k$.
* $(k = 20\text{ veh/mi}, v = 55\text{ mph})$
* $(k = 40\text{ veh/mi}, v = 42\text{ mph})$
* $(k = 60\text{ veh/mi}, v = 28\text{ mph})$
* $(k = 80\text{ veh/mi}, v = 15\text{ mph})$

1. `55 {{key:ENTER}} 20 {{key:Σ+}}`
2. `42 {{key:ENTER}} 40 {{key:Σ+}}`
3. `28 {{key:ENTER}} 60 {{key:Σ+}}`
4. `15 {{key:ENTER}} 80 {{key:Σ+}}`
5. Free-flow speed $v_f = b$: `{{key:b}}` $\rightarrow$ **`68.3000 mph`**
6. Jam density $k_j = -b / m$: `{{key:b}} {{key:m}} {{key:÷}} {{key:+/-}}` $\rightarrow$ **`102.2388 veh/mi`**.

Entering four empirical highway speed-density coordinates into the statistical registers computes OLS parameters in continuous memory. Striking `{{key:b}}` displays unobstructed free-flow speed $v_f = 68.3000\text{ mph}$. Dividing intercept by slope (`{{key:m}} {{key:÷}}`) and negating via `{{key:+/-}}` solves for theoretical gridlock jam density $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{102.2388}\text{ veh/mi})$.

---

### Problem 9.19: Centroid of a Composite Structural T-Beam
Determine horizontal centroid $\bar{x}$ of three flange segments with areas $A_i$ and centroid locations $x_i$:
* Flange 1: $A_1 = 40\text{ cm}^2, x_1 = 10\text{ cm}$
* Flange 2: $A_2 = 60\text{ cm}^2, x_2 = 25\text{ cm}$
* Flange 3: $A_3 = 20\text{ cm}^2, x_3 = 45\text{ cm}$

Accumulate as $(y = A_i, x = x_i)$:
1. `40 {{key:ENTER}} 10 {{key:Σ+}}`
2. `60 {{key:ENTER}} 25 {{key:Σ+}}`
3. `20 {{key:ENTER}} 45 {{key:Σ+}}`
4. Weighted centroid $\bar{x}_w$: `{{key:x̄,ȳ}} {{key:x̄w}}` $\rightarrow$ **`23.333 cm`**
5. Total Area $\Sigma y$: `{{key:SUMS}} {{key:Σy}}` $\rightarrow$ **`120.0 cm²`**.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `{{key:CLΣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Clear accumulators |
| 02 | `40 {{key:ENTER}} 10 {{key:Σ+}}` | $0.0000$ | $0.0000$ | $40.0000$ | $1.0000$ | Flange 1 logged ($n=1$) |
| 03 | `60 {{key:ENTER}} 25 {{key:Σ+}}` | $0.0000$ | $40.0000$ | $60.0000$ | $2.0000$ | Flange 2 logged ($n=2$) |
| 04 | `20 {{key:ENTER}} 45 {{key:Σ+}}` | $40.0000$ | $60.0000$ | $20.0000$ | $3.0000$ | Flange 3 logged ($n=3$) |
| 05 | `{{key:x̄w}}` | $40.0000$ | $60.0000$ | $20.0000$ | **$23.3333$** | Weighted centroid $\bar{x}_w$ (cm) |
| 06 | `{{key:Σy}}` | $60.0000$ | $20.0000$ | $23.3333$ | **$120.0000$** | Total beam area $\Sigma y$ ($\text{cm}^2$) |

---

### Problem 9.20: Weighted University Course GPA
Calculate semester GPA given courses with credits $c_i$ and grades $g_i$:
* Calculus: 4 credits, Grade 3.7
* Physics: 4 credits, Grade 3.3
* Literature: 3 credits, Grade 4.0
* Chemistry Lab: 1 credit, Grade 3.0

Accumulate $(y = \text{credits}, x = \text{grade})$:
1. `4 {{key:ENTER}} 3.7 {{key:Σ+}}`
2. `4 {{key:ENTER}} 3.3 {{key:Σ+}}`
3. `3 {{key:ENTER}} 4.0 {{key:Σ+}}`
4. `1 {{key:ENTER}} 3.0 {{key:Σ+}}`
5. Weighted GPA: `{{key:x̄w}}` $\rightarrow$ **`3.5833`**.

Entering courses as $(c_i, g_i)$ accumulates total grade points in $\Sigma xy$ and total credits in $\Sigma y$. Striking `{{key:x̄w}}` evaluates weighted semester GPA $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{3.5833})$ in place.

---

> **Thematic Arc III — Metrology Uncertainty, Outlier Rejection & Hypothesis Audits (Problems 9.21–9.30):** Using `Σ-` to excise corrupted measurements in place and propagating standard errors of the mean.

### Problem 9.21: Student Exam Score vs. Study Time
* $(x = 2\text{ hr}, y = 62\%)$
* $(x = 5\text{ hr}, y = 74\%)$
* $(x = 8\text{ hr}, y = 85\%)$
* $(x = 12\text{ hr}, y = 96\%)$

1. `62 {{key:ENTER}} 2 {{key:Σ+}}`
2. `74 {{key:ENTER}} 5 {{key:Σ+}}`
3. `85 {{key:ENTER}} 8 {{key:Σ+}}`
4. `96 {{key:ENTER}} 12 {{key:Σ+}}`
5. Slope: `{{key:m}}` $\rightarrow$ **`3.402 %/hr`**
6. Intercept: `{{key:b}}` $\rightarrow$ **`56.29 %`**
7. Predict score for 10 hours: `10 {{key:ŷ}}` $\rightarrow$ **`90.31%`**.

Linear regression accumulates hours vs score. Tapping `{{key:m}}` returns $m = 3.4018\text{ \%/hr}$, `{{key:b}}` yields baseline $56.2877\%$, and keying `10 {{key:ŷ}}` predicts $(T: 3.4018, Z: 56.2877, Y: 0.9960, X: \mathbf{90.3059}\%)$ for 10 hours of study.

---

### Problem 9.22: Heat Conduction Fourier Thermal Conductivity
Heat flux $q''$ vs. temperature gradient $dT/dx$: $q'' = -k (dT/dx)$.
* $(dT/dx = 50\text{ K/m}, q'' = 2100\text{ W/m}^2)$
* $(dT/dx = 100\text{ K/m}, q'' = 4220\text{ W/m}^2)$
* $(dT/dx = 150\text{ K/m}, q'' = 6310\text{ W/m}^2)$

1. `2100 {{key:ENTER}} 50 {{key:Σ+}}`
2. `4220 {{key:ENTER}} 100 {{key:Σ+}}`
3. `6310 {{key:ENTER}} 150 {{key:Σ+}}`
4. Thermal conductivity $k = m$: `{{key:m}}` $\rightarrow$ **`42.10 W/(m·K)`** (AISI 1010 carbon steel).

Entering temperature gradient in $X$ and heat flux in $Y$ yields Fourier conduction slope $q''/(dT/dx) = k$. Striking `{{key:m}}` confirms steel conductivity $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{42.1000}\text{ W/(m}\cdot\text{K)})$ instantly.

---

### Problem 9.23: Concrete Compressive Strength Aging
Compressive strength follows logarithmic curing: $\sigma(t) = a + b \ln(t)$.
* $(t = 3\text{ days}, \sigma = 18.0\text{ MPa})$
* $(t = 7\text{ days}, \sigma = 26.5\text{ MPa})$
* $(t = 14\text{ days}, \sigma = 33.2\text{ MPa})$
* $(t = 28\text{ days}, \sigma = 40.0\text{ MPa})$

Stack entry: $(y = \sigma, x' = \ln t)$.
1. `18.0 {{key:ENTER}} 3 {{key:LN}} {{key:Σ+}}`
2. `26.5 {{key:ENTER}} 7 {{key:LN}} {{key:Σ+}}`
3. `33.2 {{key:ENTER}} 14 {{key:LN}} {{key:Σ+}}`
4. `40.0 {{key:ENTER}} 28 {{key:LN}} {{key:Σ+}}`
5. Slope: `{{key:m}}` $\rightarrow$ **`9.836 MPa`**
6. Intercept: `{{key:b}}` $\rightarrow$ **`7.261 MPa`**
7. Predict 56-day strength: `{{res:sc32_09_statistics_curve_fitting_seq_15:keys}}` $\rightarrow$ **`{{res:sc32_09_statistics_curve_fitting_seq_15:value}}`**.

Entering $(y=\sigma, x'=\ln t)$ linearizes log curing. Slope `{{key:m}}` yields $9.8361\text{ MPa}$, and keying `56 {{key:LN}} {{key:ŷ}}` extrapolates 56-day compressive strength $(T: 0.0000, Z: 9.8361, Y: 1.0000, X: \mathbf{46.8487}\text{ MPa})$.

---

### Problem 9.24: Photovoltaic Solar Cell Irradiance vs. Current
Solar short-circuit current $I_{sc}$ vs. solar irradiance $G$ ($\text{W/m}^2$):
* $(G = 200, I_{sc} = 1.82\text{ A})$
* $(G = 500, I_{sc} = 4.54\text{ A})$
* $(G = 800, I_{sc} = 7.28\text{ A})$
* $(G = 1000, I_{sc} = 9.10\text{ A})$

1. `1.82 {{key:ENTER}} 200 {{key:Σ+}}`
2. `4.54 {{key:ENTER}} 500 {{key:Σ+}}`
3. `7.28 {{key:ENTER}} 800 {{key:Σ+}}`
4. `9.10 {{key:ENTER}} 1000 {{key:Σ+}}`
5. Responsivity: `{{key:m}}` $\rightarrow$ **`0.00910 A/(W/m²)`** ($9.10\text{ mA/(W/m²)}$)
6. Intercept: `{{key:b}}` $\rightarrow$ **`0.000 A`**.

Bivariate data entry of irradiance $G$ and photocurrent $I_{sc}$ yields linear responsivity. Striking `{{key:m}}` extracts slope $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{0.0091}\text{ A/(W/m}^2))$ ($9.10\text{ mA/(W/m}^2)$) with zero dark-current offset ($b = 0.0000$).

---

### Problem 9.25: Centrifugal Pump Head Loss Curve
Pump head follows $H = H_0 - A Q^2$. Linearize via $(y = H, x' = Q^2)$:
* $(Q = 10\text{ gpm}, H = 98.0\text{ ft})$
* $(Q = 20\text{ gpm}, H = 92.0\text{ ft})$
* $(Q = 30\text{ gpm}, H = 82.0\text{ ft})$

1. `98.0 {{key:ENTER}} 10 {{key:x²}} {{key:Σ+}}`
2. `92.0 {{key:ENTER}} 20 {{key:x²}} {{key:Σ+}}`
3. `82.0 {{key:ENTER}} 30 {{key:x²}} {{key:Σ+}}`
4. Shutoff head $H_0 = b$: `{{key:b}}` $\rightarrow$ **`100.0 ft`**
5. Loss coefficient $A = -m$: `{{key:m}}` $\rightarrow$ **`-0.020 ft/gpm²`**.

Pre-squaring flow rates ($Q^2$) linearizes Darcy-Weisbach quadratic head loss. Striking `{{key:b}}` recovers shutoff head $H_0 = 100.0000\text{ ft}$, while `{{key:m}}` isolates friction loss coefficient $(T: 0.0000, Z: 0.0000, Y: 100.0000, X: \mathbf{-0.0200}\text{ ft/gpm}^2)$.

---

### Problem 9.26: Laminar Pipe Friction vs. Reynolds Number
Laminar Darcy friction $f = 64 / Re \implies \ln f = \ln 64 - \ln Re$.
* $(Re = 400, f = 0.160)$
* $(Re = 800, f = 0.080)$
* $(Re = 1600, f = 0.040)$

1. `.160 {{key:LN}} 400 {{key:LN}} {{key:Σ+}}`
2. `.080 {{key:LN}} 800 {{key:LN}} {{key:Σ+}}`
3. `.040 {{key:LN}} 1600 {{key:LN}} {{key:Σ+}}`
4. Slope: `{{key:m}}` $\rightarrow$ **`-1.000000`**
5. Intercept: `{{key:b}} {{key:eˣ}}` $\rightarrow$ **`64.0000`** ($e^b$).

Log-log entry linearizes $f = 64/Re$. Tapping `{{key:m}}` gives exact inverse power $m = -1.0000$, and `{{key:b}} {{key:eˣ}}` confirms the theoretical laminar coefficient $(T: 0.0000, Z: 0.0000, Y: -1.0000, X: \mathbf{64.0000})$.

---

### Problem 9.27: Aerodynamic Drag vs. Airspeed
$F_d = C v^2 \implies \ln F_d = \ln C + 2 \ln v$.
* $(v = 10\text{ m/s}, F_d = 25\text{ N})$
* $(v = 20\text{ m/s}, F_d = 100\text{ N})$
* $(v = 30\text{ m/s}, F_d = 225\text{ N})$

1. `25 {{key:LN}} 10 {{key:LN}} {{key:Σ+}}`
2. `100 {{key:LN}} 20 {{key:LN}} {{key:Σ+}}`
3. `225 {{key:LN}} 30 {{key:LN}} {{key:Σ+}}`
4. Slope: `{{key:m}}` $\rightarrow$ **`2.000000`** (Exact quadratic velocity dependence)
5. Coefficient: `{{key:b}} {{key:eˣ}}` $\rightarrow$ **`0.2500 N/(m/s)²`**.

Log-log coordinates verify quadratic velocity scaling $F_d = C v^2$. Slope `{{key:m}}` yields $2.0000$, and striking `{{key:b}} {{key:eˣ}}` isolates the aerodynamic drag coefficient $(T: 0.0000, Z: 0.0000, Y: 2.0000, X: \mathbf{0.2500}\text{ N/(m/s)}^2)$.

---

### Problem 9.28: Cantilever Beam Deflection Elasticity
Point load deflection $\delta = \frac{P L^3}{3 E I}$.
Given $L = 2.0\text{ m}, I = 5 \times 10^{-6}\text{ m}^4$:
* $(P = 500\text{ N}, \delta = 0.00127\text{ m})$
* $(P = 1000\text{ N}, \delta = 0.00254\text{ m})$
* $(P = 1500\text{ N}, \delta = 0.00381\text{ m})$

1. `.00127 {{key:ENTER}} 500 {{key:Σ+}}`
2. `.00254 {{key:ENTER}} 1000 {{key:Σ+}}`
3. `.00381 {{key:ENTER}} 1500 {{key:Σ+}}`
4. Compliance $m = \frac{\delta}{P}$: `{{key:m}}` $\rightarrow$ $\mathbf{2.54 \times 10^{-6}\text{ m/N}}$
5. Young's modulus $E = \frac{L^3}{3 I m}$:
   `{{res:sc32_09_statistics_curve_fitting_seq_16:keys}}` $\rightarrow$ **`{{res:sc32_09_statistics_curve_fitting_seq_16:value}}`** ($210\text{ GPa}$, Structural Steel).

Load-deflection pairs yield beam compliance slope $m = 2.54 \times 10^{-6}\text{ m/N}$. Keying $L^3/(3Im)$ in place solves for Young's modulus $(T: 0.0000, Z: 0.0000, Y: 2.54 \times 10^{-6}, X: \mathbf{2.0997 \times 10^{11}}\text{ Pa})$ ($210\text{ GPa}$, structural steel).

---

### Problem 9.29: Pharmacokinetic Drug Washout Clearance
Blood concentration $C(t) = C_0 e^{-k_e t}$.
* $(t = 1\text{ hr}, C = 45.2\text{ mg/L})$
* $(t = 3\text{ hr}, C = 24.8\text{ mg/L})$
* $(t = 6\text{ hr}, C = 10.1\text{ mg/L})$

1. `45.2 {{key:LN}} 1 {{key:Σ+}}`
2. `24.8 {{key:LN}} 3 {{key:Σ+}}`
3. `10.1 {{key:LN}} 6 {{key:Σ+}}`
4. Elimination rate $k_e = -m$: `{{key:m}}` $\rightarrow$ **`-0.2997 hr^{-1}`**
5. Elimination half-life: `2 {{key:LN}} {{key:x⇄y}} {{key:+/-}} {{key:÷}}` $\rightarrow$ **`2.3129 hours`**.

Semi-log accumulation of drug concentration over time (`{{key:m}}`) yields elimination rate $k_e = -m = 0.2997\text{ hr}^{-1}$. Dividing $\ln 2$ by $k_e$ (`2 {{key:LN}} {{key:x⇄y}} {{key:+/-}} {{key:÷}}`) computes biological elimination half-life $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{2.3129}\text{ hours})$ directly.

---

### Problem 9.30: Financial Stock Beta in Capital Asset Pricing Model (CAPM)
Calculate stock volatility Beta ($\beta$) against market benchmark:
* Month 1: Market excess return $x = 2.0\%$, Stock excess return $y = 3.1\%$
* Month 2: $x = -1.5\%, y = -2.2\%$
* Month 3: $x = 4.0\%, y = 5.8\%$
* Month 4: $x = -3.0\%, y = -4.4\%$

1. `3.1 {{key:ENTER}} 2.0 {{key:Σ+}}`
2. `-2.2 {{key:ENTER}} -1.5 {{key:Σ+}}`
3. `5.8 {{key:ENTER}} 4.0 {{key:Σ+}}`
4. `-4.4 {{key:ENTER}} -3.0 {{key:Σ+}}`
5. Beta $\beta = m$: `{{key:m}}` $\rightarrow$ **`1.468`** (High-beta growth asset)
6. Alpha $\alpha = b$: `{{key:b}}` $\rightarrow$ **`0.045%`**.

Entering market excess returns in $X$ and asset excess returns in $Y$ establishes CAPM regression. Striking `{{key:m}}` extracts systematic volatility Beta $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: \mathbf{1.4676})$, while `{{key:b}}` isolates Jensen's Alpha ($0.045\%$).

---

> **Thematic Arc IV — Six Sigma Quality Control, Combinatorics & Probability Distributions (Problems 9.31–9.45):** The closing fifteen problems unite `nPr`, `nCr`, `x!`, and normal/Poisson tail probabilities for manufacturing quality assurance.

### Problem 9.31: Six Sigma Process Capability ($C_p$ and $C_{pk}$)
Shaft machining dataset ($n = 10$):
$25.02, 25.04, 25.01, 25.03, 25.05, 25.02, 25.00, 25.04, 25.03, 25.06\text{ mm}$.
Specifications: $\text{USL} = 25.10\text{ mm}, \text{LSL} = 24.90\text{ mm}$.

Accumulate data points (single variable: enter 1 in $Y$ as dummy or simply key in $x$ then `{{key:Σ+}}`):
1. `25.02 {{key:Σ+}} 25.04 {{key:Σ+}} 25.01 {{key:Σ+}} 25.03 {{key:Σ+}} 25.05 {{key:Σ+}}`
2. `25.02 {{key:Σ+}} 25.00 {{key:Σ+}} 25.04 {{key:Σ+}} 25.03 {{key:Σ+}} 25.06 {{key:Σ+}}`
3. Sample mean $\bar{x}$: `{{key:x̄,ȳ}} {{key:x̄}}` $\rightarrow$ **`25.0300 mm`**
4. Sample standard deviation $s_x$: `{{key:s,σ}} {{key:sx}}` $\rightarrow$ **`0.018257 mm`**
5. Tolerance width $\text{USL} - \text{LSL} = 0.20\text{ mm}$.
6. Process capability $C_p = \frac{0.20}{6 \times 0.018257}$:
   `{{res:sc32_09_statistics_curve_fitting_seq_03:keys}}` $\rightarrow$ **`{{res:sc32_09_statistics_curve_fitting_seq_03:value}}`** ($C_p > 1.33 \implies$ Capable!)
7. $C_{pk} = \frac{25.10 - 25.030}{3 \times 0.018257}$:
   `{{res:sc32_09_statistics_curve_fitting_seq_04:keys}}` $\rightarrow$ **`{{res:sc32_09_statistics_curve_fitting_seq_04:value}}`**.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `25.02 {{key:Σ+}} 25.04 {{key:Σ+}} 25.01 {{key:Σ+}} 25.03 {{key:Σ+}} 25.05 {{key:Σ+}} 25.02 {{key:Σ+}} 25.00 {{key:Σ+}} 25.04 {{key:Σ+}} 25.03 {{key:Σ+}} 25.06 {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | Accumulate 10 shaft diameter samples |
| 02 | `{{key:x̄,ȳ}} {{key:x̄}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$25.0300$** | Sample mean diameter $\bar{x}$ (mm) |
| 03 | `{{key:s,σ}} {{key:sx}}` | $0.0000$ | $0.0000$ | $25.0300$ | **$0.018257$** | Sample standard deviation $s_x$ (mm) |
| 04 | `{{res:sc32_09_statistics_curve_fitting_seq_03:keys}}` | $25.0300$ | $25.0300$ | $0.0183$ | **`{{res:sc32_09_statistics_curve_fitting_seq_03:value}}`** | Process capability $C_p = \frac{\text{USL}-\text{LSL}}{6s_x}$ |
| 05 | `{{res:sc32_09_statistics_curve_fitting_seq_04:keys}}` | $0.0183$ | $0.0183$ | $1.8258$ | **`{{res:sc32_09_statistics_curve_fitting_seq_04:value}}`** | Process capability index $C_{pk} = \frac{\text{USL}-\bar{x}}{3s_x}$ |

---

### Problem 9.32: Statistical Quality Control Shewhart $\bar{X}$-Chart Limits
For subgroup size $n = 5$, factor $A_2 = 0.577$.
Grand mean $\bar{\bar{X}} = 50.00\text{ mm}$, mean range $\bar{R} = 0.40\text{ mm}$.
$$\text{UCL} = \bar{\bar{X}} + A_2 \bar{R}, \quad \text{LCL} = \bar{\bar{X}} - A_2 \bar{R}$$

**Compute Margin of Control:** Key `{{res:sc32_09_statistics_curve_fitting_seq_18:keys}}` to compute $A_2 \bar{R} = 0.577 \times 0.40 = 0.2308$, yielding $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.2308)$. **Form Upper Control Limit ($\text{UCL}$):** Add the grand mean via `50.00 {{key:+}}`, evaluating $\text{UCL} = 50.00 + 0.2308 = \mathbf{50.2308\text{ mm}}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 50.2308)$. **Form Lower Control Limit ($\text{LCL}$):** Key `{{res:sc32_09_statistics_curve_fitting_seq_19:keys}}` to subtract the margin from the grand mean, yielding $\text{LCL} = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_19:value}}\text{ mm}}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 50.2308, X: {{res:sc32_09_statistics_curve_fitting_seq_19:value}})$.

---

### Problem 9.33: Standard Error of the Mean & 95% Confidence Interval
Given sample mean $\bar{x} = 120.5$, sample standard deviation $s = 8.4$, sample size $n = 36$.
Standard error $\text{SE} = \frac{s}{\sqrt{n}}$.
Critical $Z = 1.960$. Margin of error $E = 1.960 \times \text{SE}$.

**Evaluate Standard Error:** Key `{{res:sc32_09_statistics_curve_fitting_seq_20:keys}}` to compute $\text{SE} = s / \sqrt{n} = 8.4 / \sqrt{36} = 1.4$, holding $\text{SE} = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_20:value}}}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: {{res:sc32_09_statistics_curve_fitting_seq_20:value}})$. **Compute Margin of Error:** Multiply by critical $Z = 1.960$ via `1.960 {{key:×}}` to establish $E = \mathbf{2.7440}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 2.7440)$. **Form Confidence Bounds:** Key `{{res:sc32_09_statistics_curve_fitting_seq_21:keys}}` to evaluate lower bound $\mathbf{{{res:sc32_09_statistics_curve_fitting_seq_21:value}}}$ $(T: 0.0000, Z: 0.0000, Y: 2.7440, X: {{res:sc32_09_statistics_curve_fitting_seq_21:value}})$, then key `{{res:sc32_09_statistics_curve_fitting_seq_22:keys}}` to obtain upper bound $\mathbf{{{res:sc32_09_statistics_curve_fitting_seq_22:value}}}$ in Register $X$.

---

### Problem 9.34: Live Data Correction via `{{key:Σ-}}`
Suppose while entering data pair $(x=15, y=3.5)$, you accidentally entered $(x=15, y=5.3)$.
Current sample count is $n = 6$.

#### Recovery Procedure:
1. Re-enter the erroneous pair: `5.3 {{key:ENTER}} 15`
2. Press Left Shift `{{key:↰}}` then `{{key:Σ-}}`
3. The display shows $n = 5$, and all accumulators are cleansed of the erroneous values.
4. Enter the correct pair: `3.5 {{key:ENTER}} 15 {{key:Σ+}}`
5. The display returns to $n = 6$ with complete arithmetic fidelity.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `5.3 {{key:ENTER}} 15` | $0.0000$ | $0.0000$ | $5.3000$ | $15.0000$ | Key erroneous pair $(x=15, y=5.3)$ |
| 02 | `{{key:Σ-}}` | $0.0000$ | $0.0000$ | $5.3000$ | **$5.0000$** | Subtract from accumulators; $n$ decrements to 5 |
| 03 | `3.5 {{key:ENTER}} 15` | $0.0000$ | $5.3000$ | $3.5000$ | $15.0000$ | Key corrected pair $(x=15, y=3.5)$ |
| 04 | `{{key:Σ+}}` | $0.0000$ | $5.3000$ | $3.5000$ | **$6.0000$** | Accumulate corrected pair; $n$ restored to 6 |

---

### Problem 9.35: Vector Graphic Scatter Plotting & Trendline Overlay
*Accessible via Right Shift `{{key:↱}}` then `{{key:PLOT}}`*

After accumulating bivariate datasets, pressing `{{key:PLOT}}` transitions the high-contrast dot-matrix display to the 64-point vector curve engine:
* The independent variable $x$ scales along the horizontal axis ($X_{\min} \to X_{\max}$).
* The dependent variable $y$ scales along the vertical axis ($Y_{\min} \to Y_{\max}$).
* Each accumulated point appears as a $2\times 2$ pixel reticle.
* The linear regression line $y = m x + b$ is rendered as an uninterrupted 1-pixel vector trendline across the display field.
* Navigation:
  * Press `{{key:4}}` to pan left, `{{key:6}}` to pan right.
  * Press `{{key:8}}` to pan up, `{{key:2}}` to pan down.
  * Press `{{key:+}}` to zoom in, `{{key:-}}` to zoom out.
  * Press `{{key:C}}` to exit plot mode and return to the RPN stack.

**Engage Graphical Plot Engine:** Press `{{key:PLOT}}` to launch the 64-point vector scatter renderer. Operational stack registers $(T, Z, Y, X)$ are preserved intact in background memory while the display shows the bivariate data points and linear regression trendline. **Interactive Coordinate Navigation:** Use directional controls `{{key:4}}`/`{{key:6}}` (pan $X$), `{{key:8}}`/`{{key:2}}` (pan $Y$), and `{{key:+}}`/`{{key:-}}` (zoom domain/range). All adjustments manipulate viewport transform scaling without perturbing numerical stack contents $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.0000)$. **Return to Stack Execution:** Press `{{key:C}}` to dismiss the vector graphic viewport and seamlessly restore active RPN register monitoring.

---

### Problem 9.36: Residual Analysis and Standard Error of the Estimate ($s_e$)
In linear regression $y = m x + b$, the standard error of the estimate measures the dispersion of observed values around the regression line:
$$s_e = \sqrt{\frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{n - 2}} = \sqrt{\frac{\Sigma y^2 - b \Sigma y - m \Sigma xy}{n - 2}}$$

For the pressure sensor dataset from Problem 9.1:
* $n = 4$, degrees of freedom $n - 2 = 2$
* $\Sigma y = 12.45$, $\Sigma y^2 = 46.5075$, $\Sigma xy = 373.5$
* $m = 0.1245$, $b = 0.0000$

Compute residual sum of squares:
$$\text{SS}_{\text{res}} = 46.5075 - 0.0000(12.45) - 0.1245(373.5) = 46.5075 - 46.50075 = 0.00675\text{ V}^2$$
$$s_e = \sqrt{\frac{0.00675}{2}} = \sqrt{0.003375} \approx 0.05809\text{ V}$$

**Keystrokes:** `{{res:sc32_09_statistics_curve_fitting_seq_23:keys}}` $\rightarrow$ **`{{res:sc32_09_statistics_curve_fitting_seq_23:value}}`**

> ***The Inside-Out Radical & Standard Error Pipeline*** — Stream bivariate sums through residual variance formula $\frac{\Sigma y^2 - b\Sigma y - m\Sigma xy}{n-2}$ and extract square root in place {{cite:hp15c1982}}.

**Load Sum of Squares:** Key `46.5075 {{key:ENTER}}` to place $\Sigma y^2$ on the stack $(T: 0.0000, Z: 0.0000, Y: 46.5075, X: 46.5075)$. **Compute Residual Sum of Squares:** Key `0.1245 {{key:ENTER}} 373.5 {{key:×}} {{key:-}}` to subtract $m \Sigma xy = 0.1245 \times 373.5 = 46.50075$ from $\Sigma y^2$, leaving residual sum of squares $\text{SS}_{\text{res}} = 0.00675$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.00675)$. **Divide by Degrees of Freedom & Root:** Key `2 {{key:÷}}` to form variance $s_e^2 = 0.003375$, followed by `{{key:√x}}` to extract $s_e = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_23:value}}\text{ V}}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: {{res:sc32_09_statistics_curve_fitting_seq_23:value}})$.

---

### Problem 9.37: Two-Sample Pooled Variance and Student's $t$-Test
Compare the mean tensile strengths of two alloy formulations:
* Alloy A: $n_1 = 8$, mean $\bar{x}_1 = 450.0\text{ MPa}$, standard deviation $s_1 = 12.5\text{ MPa}$
* Alloy B: $n_2 = 10$, mean $\bar{x}_2 = 468.0\text{ MPa}$, standard deviation $s_2 = 14.0\text{ MPa}$

Pooled variance:
$$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$$
Student's $t$-statistic for difference in means:
$$t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$$

#### Step 1: Compute Pooled Variance $s_p^2$:
* $(8 - 1) \times 12.5^2 = 7 \times 156.25 = 1093.75$
* $(10 - 1) \times 14.0^2 = 9 \times 196.0 = 1764.0$
* Degrees of freedom: $8 + 10 - 2 = 16$
* $s_p^2 = (1093.75 + 1764.0) / 16 = 2857.75 / 16 = 178.609375$
* $s_p = \sqrt{178.609375} \approx 13.36448\text{ MPa}$

#### Step 2: Compute $t$-Statistic:
* Standard error: $s_p \times \sqrt{1/8 + 1/10} = 13.36448 \times \sqrt{0.125 + 0.10} = 13.36448 \times \sqrt{0.225} = 13.36448 \times 0.4743416 = 6.33933\text{ MPa}$
* $t = (450.0 - 468.0) / 6.33933 = -18.0 / 6.33933 = \mathbf{-2.8394}$

At $\alpha = 0.05$ with $df = 16$, critical $t_{0.025} = 2.120$. Since $|-2.8394| > 2.120$, the difference in alloy strengths is statistically significant!

**Keystrokes:** `7 {{key:ENTER}} 12.5 {{key:x²}} {{key:×}} 9 {{key:ENTER}} 14 {{key:x²}} {{key:×}} {{key:+}} 16 {{key:÷}} {{key:√x}} 8 {{key:1/x}} 10 {{key:1/x}} {{key:+}} {{key:√x}} {{key:×}} 450 {{key:ENTER}} 468 {{key:-}} {{key:x⇄y}} {{key:÷}}` $\rightarrow$ **`-2.8394`**.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes & State Analysis |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `7 {{key:ENTER}} 12.5 {{key:x²}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1093.7500$ | $(n_1 - 1)s_1^2$ evaluated |
| 2 | `9 {{key:ENTER}} 14 {{key:x²}} {{key:×}} {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2857.7500$ | Add $(n_2 - 1)s_2^2$ numerator sum |
| 3 | `16 {{key:÷}} {{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $13.364482$ | Divide by $df = 16$; $s_p = \sqrt{s_p^2}$ |
| 4 | `8 {{key:1/x}} 10 {{key:1/x}} {{key:+}} {{key:√x}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $6.339330$ | Standard error of difference $SE$ |
| 5 | `450 {{key:ENTER}} 468 {{key:-}}` | $0.0000$ | $0.0000$ | $6.339330$ | $-18.0000$ | Mean difference $\bar{x}_1 - \bar{x}_2$ |
| 6 | `{{key:x⇄y}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$-2.839422$** | Student's $t = -18.0 / SE$ |

The stack resolves to **$t = -2.8394$** ($|t| > 2.120 \implies$ reject $H_0$).

---

### Problem 9.38: Confidence Band for Mean Response at Specific $x_0$
In linear regression, the 95% confidence interval for the true mean response $E(y \mid x_0)$ is:
$$\hat{y}_0 \pm t_{\alpha/2, n-2} \cdot s_e \sqrt{\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{\Sigma x^2 - \frac{(\Sigma x)^2}{n}}}$$

For the sensor in Problem 9.1 at $x_0 = 25\text{ kPa}$:
* $n = 4, \bar{x} = 25.0, s_e = 0.058095\text{ V}$
* Notice that at $x_0 = \bar{x} = 25.0$, the distance term $(x_0 - \bar{x})^2 = 0$!
* Margin of error reduces to: $t_{0.025, 2} \cdot s_e \sqrt{1/4} = 4.303 \times 0.058095 \times 0.5 = \mathbf{0.1250\text{ V}}$.
* Mean prediction: $\hat{y} = 3.1125\text{ V}$.
* 95% Confidence Interval: $[3.1125 - 0.1250, 3.1125 + 0.1250] = \mathbf{[2.9875\text{ V}, 3.2375\text{ V}]}$.

**Scale Critical $t$ by Standard Error:** Key `4.303 {{key:ENTER}} 0.058095 {{key:×}}` to compute $t \cdot s_e = 4.303 \times 0.058095 = 0.24998$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.24998)$. **Apply Centroid Sample Factor:** Key `4 {{key:1/x}} {{key:√x}} {{key:×}}` to multiply by $\sqrt{1/4} = 0.5$, obtaining margin of error $E = \mathbf{0.12499}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.12499)$. **Form Lower & Upper Mean Confidence Bounds:** Key `3.1125 {{key:ENTER}} 0.1250 {{key:-}}` to calculate the lower bound $[3.1125 - 0.1250] = \mathbf{2.9875\text{ V}}$ $(T: 0.0000, Z: 0.0000, Y: 0.1250, X: 2.9875)$, then add the margin via `3.1125 {{key:ENTER}} 0.1250 {{key:+}}` to obtain the upper bound $\mathbf{3.2375\text{ V}}$.

---

### Problem 9.39: Prediction Band for an Individual Future Observation
For an individual future measurement $y_{\text{new}}$ at $x_0$, the error variance includes the intrinsic observation noise:
$$s_{\text{pred}} = s_e \sqrt{1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{\Sigma x^2 - \frac{(\Sigma x)^2}{n}}}$$
At $x_0 = 25\text{ kPa}$:
$$s_{\text{pred}} = 0.058095 \times \sqrt{1 + 0.25} = 0.058095 \times \sqrt{1.25} = 0.058095 \times 1.118034 = 0.06495\text{ V}$$
Margin of error ($t = 4.303$): $4.303 \times 0.06495 = \mathbf{0.2795\text{ V}}$.
95% Prediction Interval: $[3.1125 - 0.2795, 3.1125 + 0.2795] = \mathbf{[2.8330\text{ V}, 3.3920\text{ V}]}$.

**Compute Prediction Dispersion Factor:** Key `4 {{key:1/x}} 1 {{key:+}} {{key:√x}}` to evaluate $\sqrt{1 + 1/n} = \sqrt{1.25} = 1.118034$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 1.118034)$. **Scale by Standard Error & Critical $t$:** Key `0.058095 {{key:×}} 4.303 {{key:×}}` to obtain individual prediction margin $E_{\text{pred}} = \mathbf{0.27949\text{ V}}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.27949)$. **Compute 95% Prediction Interval Limits:** Key `3.1125 {{key:ENTER}} 0.2795 {{key:-}}` to establish the lower prediction bound $[3.1125 - 0.2795] = \mathbf{2.8330\text{ V}}$ $(T: 0.0000, Z: 0.0000, Y: 0.2795, X: 2.8330)$, then compute `3.1125 {{key:ENTER}} 0.2795 {{key:+}}` to reach the upper prediction bound $\mathbf{3.3920\text{ V}}$.

---

### Problem 9.40: Spearman Rank Correlation via Monotonic Ranking
When two variables have a non-linear but monotonic relationship, evaluate Spearman rank correlation $r_s$:
$$r_s = 1 - \frac{6 \Sigma d_i^2}{n(n^2 - 1)}$$
Given rank differences $d_i$ across 5 items: $d = [1, -1, 2, -1, -1]$:
* Squared differences: $1^2 + (-1)^2 + 2^2 + (-1)^2 + (-1)^2 = 1 + 1 + 4 + 1 + 1 = 8.0$
* $n = 5 \implies n(n^2 - 1) = 5(24) = 120$
* $6 \times 8 / 120 = 48 / 120 = 0.40$
* $r_s = 1 - 0.40 = \mathbf{0.6000}$.

**Keystrokes:** `{{res:sc32_09_statistics_curve_fitting_seq_05:keys}}` $\rightarrow$ **`0.6000`**

> ***The x⇄y Subtraction Inversion & Monotonic Rank Correlation*** — Scale squared rank differences by 6, divide by $n(n^2 - 1)$, and subtract from unity via `{{key:x⇄y}}` without scratch registers {{cite:ellenberg2014,hp15c1982}}.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `6 {{key:ENTER}} 8 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $48.0000$ | $6 \Sigma d_i^2 = 6 \times 8$ |
| 02 | `5 {{key:ENTER}} 24 {{key:×}}` | $0.0000$ | $0.0000$ | $48.0000$ | $120.0000$ | $n(n^2 - 1) = 5 \times 24$ |
| 03 | `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.4000$ | Quotient $48 / 120 = 0.40$ |
| 04 | `1 {{key:x⇄y}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | **`0.6000`** | Spearman rank correlation $r_s = 1 - 0.40$ |

---

### Problem 9.41: Poisson Distribution Probability Mass Function (PMF)
In a telecommunications network router, packet arrivals follow a Poisson distribution with average arrival rate $\lambda = 4.5\text{ packets/ms}$.
Calculate the probability of receiving exactly $k = 6$ packets in a 1-ms interval:
$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

**Keystrokes:** `{{res:sc32_09_statistics_curve_fitting_seq_06:keys}}` $\rightarrow$ **`{{res:sc32_09_statistics_curve_fitting_seq_06:value}}`** ($12.81\%$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `4.5 {{key:ENTER}}` | $0.00000000$ | $0.00000000$ | $4.50000000$ | $4.50000000$ | `4.5_` |
| 02 | `6 {{key:yˣ}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $8303.76562$ | `8303.76562_` |
| 03 | `4.5 {{key:+/-}}` | $0.00000000$ | $0.00000000$ | $8303.76562$ | $-4.5000000$ | `-4.5_` |
| 04 | `{{key:eˣ}}` | $0.00000000$ | $0.00000000$ | $8303.76562$ | $0.01110900$ | `0.01110900_` |
| 05 | `{{key:×}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $92.2465384$ | `92.2465384_` |
| 06 | `6 {{key:x!}}` | $0.00000000$ | $0.00000000$ | $92.2465384$ | $720.000000$ | `720._` |
| 07 | `{{key:÷}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $0.12812019$ | `0.12812019` |

---

### Problem 9.42: Binomial Distribution Probability via Combinatorics `{{key:Cn,r}}`
In an automated manufacturing testing line, component defect probability is $p = 0.03$. In a batch of $n = 20$ components, calculate the probability of observing exactly $k = 2$ defective units:
$$P(X = 2) = \binom{20}{2} (0.03)^2 (0.97)^{18}$$

**Keystrokes:** `{{res:sc32_09_statistics_curve_fitting_seq_07:keys}}` $\rightarrow$ **`{{res:sc32_09_statistics_curve_fitting_seq_07:value}}`**; `{{res:sc32_09_statistics_curve_fitting_seq_08:keys}}` $\rightarrow$ **`{{res:sc32_09_statistics_curve_fitting_seq_08:value}}`**

Key `20 {{key:ENTER}} 2 {{key:PROB}} {{key:Cn,r}}` to compute combinations $\binom{20}{2} = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_07:value}}}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 190.0000)$. Key `.03 {{key:x²}} {{key:×}}` to multiply by $p^2 = 0.03^2 = 0.0009$, yielding $190 \times 0.0009 = 0.1710$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.1710)$. Key `.97 {{key:ENTER}} 18 {{key:yˣ}} {{key:×}}` to multiply by $(1 - p)^{18} = 0.97^{18} \approx 0.5779$, yielding final binomial probability $P(X = 2) = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_08:value}}}$ ($9.88\%$) in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: {{res:sc32_09_statistics_curve_fitting_seq_08:value}})$.

---

### Problem 9.43: Hypergeometric Sampling Without Replacement
In a batch of $N = 50$ aerospace fasteners, $K = 6$ are defective. A quality inspector selects $n = 5$ fasteners at random without replacement. Find the probability that exactly $k = 1$ selected fastener is defective:
$$P(X = 1) = \frac{\binom{K}{k} \binom{N - K}{n - k}}{\binom{N}{n}} = \frac{\binom{6}{1} \binom{44}{4}}{\binom{50}{5}}$$

**Keystrokes:** `{{res:sc32_09_statistics_curve_fitting_seq_24:keys}}`; `{{res:sc32_09_statistics_curve_fitting_seq_25:keys}}`; `{{res:sc32_09_statistics_curve_fitting_seq_26:keys}} {{key:÷}}` $\rightarrow$ **`0.384426`**

Key `6 {{key:ENTER}} 1 {{key:PROB}} {{key:Cn,r}}` to evaluate $\binom{6}{1} = 6.0000$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 6.0000)$. Key `44 {{key:ENTER}} 4 {{key:PROB}} {{key:Cn,r}} {{key:×}}` to calculate $\binom{44}{4} = 135751$ and multiply by 6, yielding numerator $814506.0$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 814506.0000)$. Key `50 {{key:ENTER}} 5 {{key:PROB}} {{key:Cn,r}} {{key:÷}}` to compute total sample space $\binom{50}{5} = 2118760$ and divide in place to form $P(X = 1) = \mathbf{0.384426}$ ($38.44\%$) in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.384426)$.

---

### Problem 9.44: Weibull Reliability & Failure Rate Analysis
The two-parameter Weibull reliability function models fatigue life in mechanical ball bearings:
$$R(t) = \exp\left( -\left(\frac{t}{\eta}\right)^\beta \right)$$
where $\eta = 5000\text{ hours}$ (characteristic life scale parameter) and $\beta = 1.8$ (shape parameter / wear-out phase).
Calculate reliability $R(t)$ at $t = 3000\text{ operating hours}$:

**Keystrokes:** `{{res:sc32_09_statistics_curve_fitting_seq_09:keys}}` $\rightarrow$ **`0.6712`** ($67.12\%$ survival probability).

> ***The Inside-Out Exponential & Weibull Survival Pipeline*** — Form normalized operating time ratio $t/\eta$, raise to shape parameter $\beta$ in place, negate, and exponentiate without parentheses {{cite:hp15c1982}}.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `3000 {{key:ENTER}} 5000 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.6000$ | Operating ratio $t/\eta = 3000/5000 = 0.6$ |
| 02 | `1.8 {{key:yˣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.398660$ | Raise to shape parameter $\beta = 1.8$ ($0.6^{1.8} \approx 0.3987$) |
| 03 | `{{key:+/-}} {{key:eˣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | **`0.6712`** | Weibull reliability $R(3000) = \exp(-0.3987) \approx 0.6712$ ($67.12\%$) |

---

### Problem 9.45: Log-Normal Aerosol Droplet Size Distribution
In medical nebulizer sprays, aerosol droplet diameters $D$ follow a log-normal distribution with geometric mean $\mu_{\ln} = \ln(4.5\text{ }\mu\text{m}) = 1.504077$ and geometric standard deviation $\sigma_{\ln} = 0.35$.
Calculate the probability density for a droplet of diameter $D = 5.0\text{ }\mu\text{m}$:
$$f(D) = \frac{1}{D \sigma_{\ln} \sqrt{2\pi}} \exp\left( -\frac{(\ln D - \mu_{\ln})^2}{2\sigma_{\ln}^2} \right)$$

**Keystrokes:** `{{res:sc32_09_statistics_curve_fitting_seq_27:keys}}`; `{{res:sc32_09_statistics_curve_fitting_seq_28:keys}}`; `{{res:sc32_09_statistics_curve_fitting_seq_10:keys}}` $\rightarrow$ **`{{res:sc32_09_statistics_curve_fitting_seq_10:value}}`**

Key `5.0 {{key:LN}} 1.504077 {{key:-}} {{key:x²}}` to compute $(\ln 5.0 - 1.504077)^2 \approx 0.011101$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.011101)$. Key `.35 {{key:x²}} 2 {{key:×}} {{key:÷}} {{key:+/-}} {{key:eˣ}}` to divide by $2\sigma_{\ln}^2 = 2 \times 0.35^2 = 0.245$, negate, and exponentiate, yielding $\exp(-0.045310) \approx 0.955701$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.955701)$. Key `5.0 {{key:ENTER}} .35 {{key:×}} 2 {{key:π}} {{key:×}} {{key:√x}} {{key:×}} {{key:÷}}` to divide by the normalization factor $5.0 \times 0.35 \times \sqrt{2\pi} \approx 4.3866$, arriving at $f(5.0) = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_10:value}}\ \mu\text{m}^{-1}}$ in Register $X$ $(T: 0.9557, Z: 0.9557, Y: 0.9557, X: {{res:sc32_09_statistics_curve_fitting_seq_10:value}})$.

---

## Summary & Looking Ahead

Chapter 9 established rigorous data reduction, regression analysis, and empirical modeling on the SC-32. You harnessed the six dedicated hardware statistical accumulators ($\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$) to compute bivariate means, sample standard deviations, covariance, and least-squares regression lines without disturbing user storage registers. Through `{{key:Σ-}}`, you maintained pristine data hygiene, while `{{key:ŷ}}` and `{{key:x̂}}` converted transducer voltages into physical measurements. You then extended statistical theory into probability distributions, evaluating Gaussian normal PDFs, Poisson arrival rates, and Weibull reliability life cycles in place.

Continuous distributions and decimal floating-point arithmetic form only half of computational science. Beneath modern instrumentation lies the discrete digital architecture of binary bits, logic words, and memory addresses. In **Chapter 10: Computer Science, Bases & 36-Bit Integers**, you will explore the SC-32's authentic 36-bit two's complement integer architecture. You will navigate hexadecimal, decimal, octal, and binary bases while preserving stack integrity, execute modular integer division via `{{key:÷R}}` returning quotient in $X$ and remainder in $Y$, harness word length clipping and mathematical bit-packing without dedicated Boolean keys, calculate IPv4 CIDR subnet masks and packed RGB color channels, and master discrete combinatorics.
