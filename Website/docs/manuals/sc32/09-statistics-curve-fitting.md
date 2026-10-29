---
title: "Chapter 9: Taming Uncertainty: How Gauss Found a Lost Planet and a Brewery Invented Modern Statistics | Thinking in the Stack (SC-32)"
description: "Explore Gauss's 1801 recovery of Ceres, Galton's Quincunx and regression to the mean, Bessel's n - 1 correction, Student's Guinness Brewery t-test, and Weibull reliability on the StackCalc SC-32."
---

# Chapter 9: Taming Uncertainty: How Gauss Found a Lost Planet and a Brewery Invented Modern Statistics

## The Lost Planet Ceres, Galton's Bean Machine & Bessel's n − 1 Mystery

On the cold, crystal-clear New Year's Night of **January 1, 1801**, the Italian astronomer and Theatine monk **Giuseppe Piazzi** peered through his vertical Ramsden circle telescope at the Palermo Observatory in Sicily. While compiling a star catalog in the constellation Taurus, Piazzi noticed a faint, uncataloged eighth-magnitude point of light. The next night, it had shifted slightly against the background stars.

Across a forty-one-day span in January and early February 1801 (recording 24 nights of observations), Piazzi tracked the mysterious wanderer before falling ill and watching his discovery drift into the blinding daytime glare of the Sun. Piazzi had discovered **Ceres**—the largest body in the asteroid belt between Mars and Jupiter. Yet there was a crisis: Piazzi had observed Ceres across barely **three degrees of sky**—less than one percent of its full orbit—and every single telescope reading was slightly blurred by atmospheric refraction, clock drift, and human eyesight. When the leading astronomers of Europe tried to compute Ceres's orbit from Piazzi's observations, their predictions scattered wildly across the heavens. Ceres was lost.

In Göttingen, a twenty-four-year-old mathematician named **Carl Friedrich Gauss** read Piazzi's published sightings and attacked the problem with a revolutionary philosophy. Instead of picking three observations and pretending they were exact, Gauss asked: *How do random observational errors behave, and how can we combine ALL of Piazzi's noisy sightings across that forty-one-day arc so that their random errors cancel one another out?*

Over three intense months in the autumn of 1801, Gauss combined his new geometry of elliptical orbits with two foundational ideas that launched modern data science {{cite:gauss1809}}:
1. **The Method of Least Squares:** The most probable true trajectory through a cloud of noisy measurements is the unique curve that minimizes the **sum of the squares of the residuals** (the squared vertical distances between the observed data points and the theoretical curve).
2. **The Gaussian Law of Error (The Normal Bell Curve):** Small, independent random disturbances cluster symmetrically around the true value according to the exponential-square density $e^{-z^2/2}$.

On the night of **December 31, 1801**—after first re-sighting the faint object on December 7 and waiting through weeks of winter clouds to confirm its motion—the German astronomer Franz Xaver von Zach verified Ceres in the exact patch of sky in Virgo predicted by young Gauss's least-squares calculation, shining within half a degree of Gauss's coordinates! Gauss had proved that combining noisy measurements mathematically does not blur the truth—it extracts a signal cleaner than any single instrument could ever see on its own.

### Sir Francis Galton's 1873 Quincunx: Watching Chaos Sculpt the Bell Curve

Why does Gauss's bell curve appear *everywhere* in nature—governing not only astronomical telescope errors, but the heights of forest trees, the thermal noise of resistors, and the diameters of machined steel shafts?

In **1873**, during a Friday Evening Discourse at the Royal Institution in London, the Victorian explorer and polymath **Sir Francis Galton** unveiled a physical tabletop device that made the birth of the bell curve visible before the audience's eyes: the **Quincunx** (now known as the **Galton Board** or **Bean Machine**).

Galton built a vertical wooden frame behind a pane of glass, with a funnel at the top, twelve staggered horizontal rows of brass pins in the middle (arranged like the five-spot *quincunx* pattern on a die), and a row of narrow vertical glass slots at the bottom. When Galton poured a thousand lead shot pellets into the top funnel, every individual pellet tumbled down through the brass pins in apparent chaos. At each of the $12$ rows of pins, a falling pellet faced an independent $50/50$ binary choice: bounce **Left ($L$)** or bounce **Right ($R$)**.

Yet as the thousand pellets settled into the vertical compartments at the bottom, they *never* formed a flat horizontal layer, and they *never* piled up in a jagged random heap. Every single time, the lead shot sculpted the exact, smooth, symmetric silhouette of **Carl Friedrich Gauss's Normal Bell Curve**.

Why? Count the paths. For a pellet to land in Slot $0$ at the far left edge, it must bounce Left twelve times in a row ($LLLLLLLLLLLL$)—only **$\binom{12}{0} = 1\text{ path}$** out of $2^{12} = 4,096$ possible trajectories (probability $0.024\%$). To land in Slot $1$, there are $\binom{12}{1} = 12$ paths. By the time you reach Slot $6$ right in the center—six Left bounces and six Right bounces in any order—there are **$\binom{12}{6} = \mathbf{924\text{ distinct intertwined paths}}$** leading to that middle slot!

Galton's Quincunx is the physical embodiment of the **Central Limit Theorem** (first proved for binomial coin tosses by Abraham de Moivre in 1733 and generalized by Pierre-Simon Laplace in 1810): whenever a measurement is pushed back and forth by dozens of tiny, independent random disturbances—lathe vibrations, air currents, thermal electron jitter—their sum converges inexorably to the **Gaussian Normal Probability Density Function (PDF)**:

$$f(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right), \qquad \phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2 / 2} \quad \left(\text{where } z = \frac{x - \mu}{\sigma}\right)$$

The center of the bell sits at the mean $\mu$, while its width is set by the **standard deviation** $\sigma$ (the exact horizontal distance from the peak $\mu$ to the two **inflection points** $x = \mu \pm \sigma$ where the bell changes from curving downward like a cap to flaring outward like a skirt). And as we saw with Romberg quadrature in Chapter 8, the area under the bell curve from $-\infty$ to $z$ gives the **cumulative probability** $\Phi(z) = \frac{1}{2} + \frac{1}{\sqrt{2\pi}}\int_0^z e^{-t^2/2}\,dt$, which establishes the **Empirical Rule ($68.27\%\text{–}95.45\%\text{–}99.73\%$)** for the fraction of observations falling within $\pm 1\sigma$, $\pm 2\sigma$, and $\pm 3\sigma$ of the mean.

### The Mystery of Bessel's $n - 1$ Correction: Why Sample Spread Divides by $n - 1$

When you pull a small sample of $n$ parts off a production line—or log $n$ sensor readings—with values $x_1, x_2, \dots, x_n$, entering each reading into Register $X$ (or a coordinate pair $(y_k, x_k)$ into Registers $Y$ and $X$) and pressing `{{key:Σ+}}` (with `{{key:Σ-}}` ready to retract any mistyped reading) updates the SC-32's statistical accumulators. Opening the **`{{key:x̄,ȳ}}` menu** (`{{key:↱}}` + `{{key:yˣ}}`) gives the **sample mean** $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$ on softkey `{{key:x̄}}` (and, when each value $x_k$ in $X$ is paired with a weight $w_k$ in $Y$, the **weighted mean** $\bar{x}_w = \frac{\sum w_k x_k}{\sum w_k}$ on softkey `{{key:x̄w}}`).

Now comes a question that puzzles almost every student of science and engineering: when you open the **`{{key:s,σ}}` menu** (`{{key:↱}}` + `{{key:1/x}}`) to measure how spread out those $n$ numbers are around their mean, why does the SC-32 place **two** standard deviation softkeys side by side—**sample standard deviation** `{{key:sx}}` (which divides the sum of squared deviations by **$n - 1$**) and **population standard deviation** `{{key:σx}}` (which divides by $n$)?

$$\sigma_x = \sqrt{\frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n}}, \qquad s_x = \sqrt{\frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n - 1}} = \sqrt{\frac{\Sigma x^2 - \frac{(\Sigma x)^2}{n}}{n - 1}}$$

Why did Gauss's astronomer friend **Friedrich Wilhelm Bessel** insist on dividing by $n - 1$ instead of $n$ when estimating the spread of a larger population from a sample of size $n$?

Take the extreme case first: suppose you pull just **$n = 1$ single shaft** off a lathe and measure its diameter as $x_1 = 25.02\text{ mm}$. What is the sample average $\bar{x}$ of that one number? It is $25.02\text{ mm}$. How far is your single point from its own average? Zero ($x_1 - \bar{x} = 0$). Does that mean the lathe produces zero variation across thousands of shafts? Of course not. With $n = 1$ observation, you have **zero information about spread**—and Bessel's formula $\frac{0}{1 - 1} = \frac{0}{0}$ honestly refuses to report a bogus zero (triggering `STAT ERROR` if you press `{{key:sx}}` at $n = 1$).

Now examine what happens for any sample of $n$ points drawn from a population whose *true* center is $\mu$. Because we do not know the true population mean $\mu$, we are forced to measure squared deviations around our sample's own average $\bar{x}$. Recall Gauss's least-squares theorem: **the sample mean $\bar{x}$ is the exact number that makes the sum of squared deviations $\sum(x_i - c)^2$ as small as mathematically possible.** Specifically, for any sample:

$$\sum_{i=1}^n (x_i - \bar{x})^2 = \sum_{i=1}^n (x_i - \mu)^2 - n(\bar{x} - \mu)^2 \le \sum_{i=1}^n (x_i - \mu)^2$$

Because the sample average $\bar{x}$ gets pulled right into the middle of whichever $n$ points happened to land in your sample, your sample points *always* huddle closer to their own sample mean $\bar{x}$ than they do to the true population center $\mu$—by an average squared amount of $\sigma^2$, leaving $\sum(x_i - \bar{x})^2$ equal to $(n - 1)\sigma^2$ on average. Equivalently, because the $n$ deviations $(x_1 - \bar{x}), \dots, (x_n - \bar{x})$ must always sum to zero:

$$\sum_{i=1}^n (x_i - \bar{x}) = 0$$

only **$n - 1$** of the deviations are independent (**$n - 1$ degrees of freedom**); once you write down the first $n - 1$ deviations, the last one is completely fixed. Dividing by $n - 1$ (**Bessel's Correction**) removes that downward bias completely!

In manufacturing and laboratory metrology, `{{key:x̄}}` and `{{key:sx}}` drive three everyday quality tools:
* **Six Sigma Process Capability ($C_p$ and $C_{pk}$):** When a CNC lathe machines bearing shafts to a tolerance window $[\text{LSL}, \text{USL}]$, the **potential capability** $C_p = \frac{\text{USL} - \text{LSL}}{6 s_x}$ measures how many times the natural $6s_x$ bell curve fits inside the blueprint walls. Its companion **off-center capability index** $C_{pk} = \min\!\left(\frac{\text{USL} - \bar{x}}{3s_x}, \frac{\bar{x} - \text{LSL}}{3s_x}\right)$ warns the machinist whenever tool wear shifts the sample mean $\bar{x}$ toward the upper or lower wall.
* **Walter Shewhart's 1924 Bell Labs Control Charts ($\text{UCL}, \text{LCL}$):** In May 1924 at Bell Telephone Laboratories, physicist **Walter A. Shewhart** wrote a one-page memorandum that launched statistical process control. Shewhart proved that if operators tweak a machine knob after every tiny random fluctuation ("tampering"), they *double* the variance of the output. By plotting subgroup averages against $\pm 3\sigma_{\bar{x}}$ guardrails $\text{UCL}, \text{LCL} = \bar{\bar{X}} \pm A_2 \bar{R}$, operators leave the process alone inside the guardrails and intervene only when a real physical fault pushes a point across the line.
* **The $\sqrt{n}$ Law of Averaging (Standard Error of the Mean):** Why do astronomers and metrologists average $n = 36$ repeated readings? Because independent positive and negative errors partially cancel out, shrinking the standard deviation of the sample average—the **Standard Error of the Mean**—by the square root of the sample size:
  $$\text{SE} = \frac{s_x}{\sqrt{n}}$$
  Averaging $n = 36$ readings cuts random uncertainty to $1/\sqrt{36} = \mathbf{1/6\text{th}}$ of a single reading's noise.

---

## Regression to the Mean, Least-Squares Lines & Linearized Curves

Twelve years after building his Quincunx, **Sir Francis Galton** made a second historic discovery while studying the heights of $930$ adult children and their $205$ pairs of parents in 1886 (*"Regression towards Mediocrity in Hereditary Stature"*). Galton plotted average parent height on the horizontal $x$-axis and adult child height on the vertical $y$-axis, and drew the best-fit straight line through the cloud of points.

He uncovered a subtle statistical pattern. Parents who were four inches taller than the population average did have tall children—but on average, their children were only about *two and a half inches* taller than the mean. Conversely, parents who were four inches shorter than average had children who were taller than their parents, closer to the center of the population. Whenever two variables are imperfectly correlated, extreme observations in $x$ are followed on average by less extreme observations in $y$, pulled back toward the population center $(\bar{x}, \bar{y})$. Galton called this phenomenon **"regression toward the mean"**—and to this day, fitting any line or curve to noisy data is called **regression**.

{{blocks:sc32_concept_gauss_least_squares|Gauss's method of least squares minimizing squared vertical residuals and the Gaussian normal probability distribution.}}

### How Six Running Totals Remember a Hundred Data Points

Suppose we want to fit Gauss's least-squares straight line $\hat{y} = m x + b$ through $n$ noisy data pairs $(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)$. Alongside the slope and intercept, we also want **Karl Pearson's 1895 Correlation Coefficient** $r \in [-1, +1]$, which measures how tightly the data cloud hugs the straight line: $r = +1$ indicates an exact upward line, $r = -1$ an exact downward line, and $r = 0$ an uncorrelated shotgun cloud, while $r^2$ gives the fraction of variance in $y$ explained by $x$. How does a pocket instrument manage the memory load across hundreds of points?

You might think a calculator would have to store an ever-growing spreadsheet of hundreds of individual $(x_k, y_k)$ pairs in memory. When we minimize the sum of squared vertical errors $\sum_{k=1}^n (y_k - (m x_k + b))^2$ by setting its calculus derivatives with respect to $m$ and $b$ to zero, the algebra reveals a remarkable compression {{cite:gauss1809}}:

$$\text{Slope } m = \frac{n \Sigma xy - \Sigma x \, \Sigma y}{n \Sigma x^2 - (\Sigma x)^2}, \qquad \text{Intercept } b = \bar{y} - m \bar{x} = \frac{\Sigma y - m \Sigma x}{n}$$

$$\text{Pearson Correlation } r = \frac{n \Sigma xy - \Sigma x \, \Sigma y}{\sqrt{\left[ n \Sigma x^2 - (\Sigma x)^2 \right] \left[ n \Sigma y^2 - (\Sigma y)^2 \right]}}$$

In those three formulas, **individual data points $(x_k, y_k)$ never appear anywhere!** Everything about the means, the standard deviations, the least-squares slope $m$, the intercept $b$, and the correlation $r$ is completely determined by just **six running totals**—all six of which you can inspect at any moment on the SC-32 through the **`{{key:SUMS}}` menu** (`{{key:↱}}` + `{{key:Σ+}}`, with softkeys `{{key:Σx}}`, `{{key:Σy}}`, `{{key:Σx²}}`, `{{key:Σy²}}`, `{{key:Σxy}}`, and `{{key:n}}`) {{cite:hp15c1982,hp32sii1991}}:

$$\Sigma x = \sum x_k, \quad \Sigma y = \sum y_k, \quad \Sigma x^2 = \sum x_k^2, \quad \Sigma y^2 = \sum y_k^2, \quad \Sigma xy = \sum x_k y_k, \quad \text{and } n$$

Whether you feed `{{key:Σ+}}` $4$ points or $4,000$ points, updating those six registers on each observation remembers the exact least-squares geometry of the entire dataset. Better still, if an accidental typo or electromagnetic spike corrupts the sixth data pair $(x_k, y_k)$, keying that pair into $Y$ and $X$ and pressing `{{key:Σ-}}` subtracts that single observation out of the six running sums ($\Sigma x \leftarrow \Sigma x - x_k,\; \Sigma xy \leftarrow \Sigma xy - x_k y_k,\; n \leftarrow n - 1$), removing the outlier without touching any of the other readings.

Opening the **`{{key:L.R.}}` (Linear Regression) menu** (Right Shift `{{key:↱}}` above `{{key:LN}}`) exposes softkeys `{{key:ŷ}}`, `{{key:x̂}}`, `{{key:r}}`, `{{key:m}}`, and `{{key:b}}`, supporting two practical workflows around $\hat{y} = mx + b$:
* **Two-Way Calibration (`{{key:ŷ}}` and `{{key:x̂}}`) & Confidence vs. Prediction Bands:** Once a sensor is calibrated across reference pressures or temperatures, you can both **forecast** $\hat{y} = mx_0 + b$ at a known stimulus $x_0$ via `{{key:ŷ}}` and **invert** the line $\hat{x} = (y_0 - b)/m$ via `{{key:x̂}}` to find the unknown physical stimulus from a measured voltage $y_0$. Because the least-squares line pivots through $(\bar{x}, \bar{y})$ and can tilt slightly in slope, the **pointwise Student-$t$ confidence interval (and Working-Hotelling hyperbolic envelope)** for the *average line* $E(y \mid x_0)$ flares outward like an hourglass hyperbola proportional to $s_e\sqrt{\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{\Sigma(x_i - \bar{x})^2}}$, narrowing to a waist right at the centroid $x_0 = \bar{x}$. By contrast, the **prediction band** for a *single future measurement* adds $+1$ inside the radical, $\sqrt{1 + \frac{1}{n} + \dots}$, to account for the scatter of that one new reading around the line.
* **Charles Spearman's Rank Correlation ($r_s$, 1904):** What if two variables rise monotonically together along a steep curve—or are measured on an ordinal $1, 2, \dots, n$ ranking scale (like Mohs scratch hardness vs. wear lifetime across ceramic coatings)—where linear correlation $r$ is skewed? Replacing the raw measurements with their integer ranks and computing the rank differences $d_i = \text{rank}(x_i) - \text{rank}(y_i)$ reduces Pearson's formula to **Spearman's rank correlation**:
  $$r_s = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}$$

### Bending Curves into Straight Lines: Moore's Law, Barometric Altitude & Wind Turbines

What if the physical law governing your data is not a straight line at all, but an **exponential curve**, a **power law**, or a **saturation hyperbola**? Because the SC-32's statistical accumulators sit right on the live RPN stack rather than behind a modal data-entry form, you do not need a separate nonlinear regression mode. By tapping `{{key:LN}}` or `{{key:1/x}}` on your $y$ or $x$ coordinates on the stack *before* pressing `{{key:Σ+}}`, you bend the curve into a straight line and read the transformed parameters from `{{key:m}}` and `{{key:b}}`:

| Physical Model | Governing Equation | Coordinate Transformation | Linearized Straight Line | How Parameters Are Recovered |
| :--- | :--- | :--- | :--- | :--- |
| **Linear** | $y = m x + b$ | $(x, y)$ unchanged | $y = m x + b$ | Slope $= m$, Intercept $= b$ |
| **Exponential** | $y = a e^{b x}$ | $(x,\; \ln y)$ [Semi-Log] | $\ln y = b x + \ln a$ | Rate $b = m$, Initial $a = e^{\text{Intercept}}$ |
| **Power Law** | $y = a x^b$ | $(\ln x,\; \ln y)$ [Log-Log] | $\ln y = b \ln x + \ln a$ | Exponent $b = m$, Scale $a = e^{\text{Intercept}}$ |
| **Logarithmic** | $y = a + b \ln x$ | $(\ln x,\; y)$ | $y = b \ln x + a$ | Scale $b = m$, Offset $a = \text{Intercept}$ |
| **Reciprocal** | $\frac{1}{y} = b x + a$ | $(x,\; 1/y)$ | $\frac{1}{y} = b x + a$ | Slope $= b$, Intercept $= a$ |
| **Hyperbolic** | $y = \frac{x}{a + b x}$ | $(1/x,\; 1/y)$ [Double-Reciprocal] | $\frac{1}{y} = a\left(\frac{1}{x}\right) + b$ | Slope $= a$, Ceiling $1/b$ |

Three classic coordinate lenses illustrate how stack transformations linearize nonlinear laws across science and technology:

1. **The Semi-Log Lens ($\ln y$ vs. $x$): Moore's Law, Barometric Altitude & Radioactive Decay:**
   * In 1965, Fairchild Semiconductor co-founder **Gordon Moore** {{cite:moore1965}} plotted the transistor count $N(t)$ of a microchip against the calendar year $t$ on semi-logarithmic paper, graphing $\ln N$ against $t$. The points fell along a striking straight line, $\ln N(t) = \ln N_0 + r(t - t_0)$, corresponding to a doubling period $T_{\text{double}} = \frac{\ln 2}{r} \approx 2\text{ years}$ now known as **Moore's Law**.
   * As we saw with Halley and Laplace's barometric formula in Chapter 3, atmospheric pressure $P(h) = P_0 e^{-h/H}$ drops exponentially with altitude $h$ (scale height $H \approx 8.4\text{ km}$); taking `{{key:LN}}` of pressure before pressing `{{key:Σ+}}` turns $\ln P(h) = \ln P_0 - \frac{1}{H}h$ into a straight line whose slope `{{key:m}}` is $-1/H$.
   * In nuclear medicine, logging the natural logarithm $\ln A(t)$ of Technetium-99m ($^{99\text{m}}\text{Tc}$) gamma-ray activity across time $t$ turns Ernest Rutherford and Frederick Soddy's exponential decay $A(t) = A_0 e^{-\lambda t}$ into a straight line of slope $m = -\lambda$, from which the clinical half-life follows as $t_{1/2} = \frac{\ln 2}{\lambda}$.
2. **The Log-Log Lens ($\ln y$ vs. $\ln x$): Why Wind Turbines Obey a Cubic Power Law ($P = k v^3$):**
   Why does doubling the wind speed $v$ multiply a wind turbine's electrical output by **eightfold ($2^3 = 8$)**? Because the mass of air hitting the rotor disk per second grows linearly with wind speed ($\dot{m} = \rho A v$), while the kinetic energy carried by each kilogram of air grows with the *square* of wind speed ($\frac{1}{2}v^2$), making total wind power scale with the **cube** of wind speed: $P(v) = \frac{1}{2}\dot{m}v^2 = k v^3$. Taking `{{key:LN}}` of both power $P$ and wind speed $v$ before pressing `{{key:Σ+}}` turns $P = k v^m$ into $\ln P = m \ln v + \ln k$, where `{{key:m}}` extracts the power-law exponent $m$ and `{{key:b}} {{key:eˣ}}` recovers the aerodynamic scale factor $k = e^b$.
3. **The Double-Reciprocal Lens ($1/y$ vs. $1/x$): Lineweaver-Burk Enzyme Saturation (1934):**
   When biochemists **Leonor Michaelis** and **Maud Menten** (1913) measured how fast a catalytic enzyme processes substrate $[S]$, they found a hyperbolic curve $v = \frac{V_{\max}[S]}{K_m + [S]}$ that bends toward a ceiling $V_{\max}$ once every catalytic active site on the enzyme is occupied. In 1934, **Hans Lineweaver** and **Dean Burk** showed that taking the reciprocal (`{{key:1/x}}`) of *both* reaction velocity $v$ and substrate concentration $[S]$ before `{{key:Σ+}}` straightens the hyperbola into:
   $$\frac{1}{v} = \left(\frac{K_m}{V_{\max}}\right)\frac{1}{[S]} + \frac{1}{V_{\max}}$$
   where the reciprocal of the intercept (`{{key:b}} {{key:1/x}}`) gives the maximum molecular turnover speed $V_{\max} = 1/b$ and multiplying by `{{key:m}}` gives the half-saturation constant $K_m = m \cdot V_{\max}$.

---

## The Guinness Brewery Chemist Who Invented Small-Sample Science

Around 1906, at St. James's Gate in Dublin, Ireland, **Arthur Guinness & Son**—then the largest brewery on Earth—faced a classic industrial puzzle. Guinness had hired a brilliant young Oxford-trained chemist and mathematician named **William Sealy Gosset** as Head Experimental Brewer to apply scientific quality control to the brewing of stout.

Gosset wanted to know whether a new variety of Irish barley yielded significantly more malt extract than an old variety, or whether hop soft-resin content differed between two harvests. He looked at the statistical methods of Carl Friedrich Gauss and Karl Pearson, and hit a fundamental barrier. Classical nineteenth-century statistics assumed you had hundreds or thousands of observations ($n \to \infty$), so that your sample standard deviation $s$ could be treated as if it were the exact, noiseless population standard deviation $\sigma$.

In a real brewery, however—just as in aerospace metallurgy or clinical drug trials—you cannot wait twenty years to grow and malt a thousand test fields of barley. Gosset often had only **$n = 4$ to $10$ small experimental batches**. When $n$ is small, the sample standard deviation $s$ in the denominator of your standardized score fluctuates randomly from batch to batch alongside the sample mean $\bar{x}$ in the numerator, making extreme ratios occur more often than Gauss's normal curve predicts (creating a bell curve with heavier, wider tails).

Working at night with stacks of hand-shuffled cardboard slips and a mechanical calculator, Gosset derived the exact small-sample probability distribution of the ratio $t = \frac{\bar{x} - \mu}{s / \sqrt{n}}$. Because Guinness strictly forbade its scientists from publishing research under their own names (after another Guinness chemist had nearly given away a trade secret a few years earlier), Gosset persuaded the brewery board to let him publish his landmark 1908 paper—*"The Probable Error of a Mean"*—in Karl Pearson's journal *Biometrika* under the modest pen name ***"Student"*** {{cite:student1908}}.

To compare the means of two small experimental groups of sizes $n_1$ and $n_2$—such as tensile test coupons of two candidate aerospace titanium alloys—**Student's Two-Sample $t$-Test** combines the two sample variances weighted by their Bessel degrees of freedom ($n_1 - 1$ and $n_2 - 1$, giving $df = n_1 + n_2 - 2$ total degrees of freedom):

$$s_p = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}, \qquad t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$$

When $|t|$ exceeds the critical Student's $t$-threshold for $df = n_1 + n_2 - 2$, the metallurgist knows with high statistical confidence that the strength gain is a genuine physical breakthrough and not a lucky fluke of small samples!

### Counting Rare Arrivals & Aging Machines: Poisson (1837) and Weibull (1951)

Two more probability laws complete the engineer's statistical toolkit—one for discrete random arrivals, and one for the aging and survival of physical hardware:

* **Siméon Denis Poisson's Law of Rare Events (1837):** Whenever independent discrete events occur randomly at a steady average rate $\lambda$ per unit of time or space—photons from a distant nebula striking a telescope pixel, cosmic-ray muons clicking in a detector, or data packets arriving at an optical network router—how likely is a sudden burst of $k$ arrivals in a single interval? In 1837, French mathematician **Siméon Denis Poisson** derived the **Poisson Probability Mass Function (PMF)**, evaluated on the stack using `{{key:yˣ}}`, `{{key:eˣ}}`, and the factorial key `{{key:x!}}` via Left Shift `{{key:↰}}` above `{{key:1/x}}` or inside the `{{key:PROB}}` menu:
  $$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$
  (In 1898, Russian economist Ladislaus Bortkiewicz famously verified Poisson's formula by showing that it predicted with uncanny accuracy the annual number of Prussian cavalry corps soldiers kicked to death by horses over a twenty-year span.)
* **Waloddi Weibull's Aging & Material Fatigue Reliability Law (1951):** Radioactive atoms and Poisson router packets are *memoryless*—a carbon-14 atom that has survived for five thousand years is no more likely to decay in the next minute than a brand-new atom. Mechanical ball bearings, jet-engine turbine blades, and stressed steel shafts are *not* memoryless: as operating hours $t$ accumulate, microscopic fatigue cracks nucleate and grow.
  In 1951, Swedish engineer **Waloddi Weibull** {{cite:weibull1951}} introduced a single, versatile survival equation that unifies all three phases of the engineering **"bathtub reliability curve"** through a characteristic life scale $\eta$ (the age at which $e^{-1} \approx 36.79\%$ of units survive) and a dimensionless **shape parameter $\beta$**:
  $$R(t) = \exp\left[ -\left(\frac{t}{\eta}\right)^\beta \right]$$
  * **$\beta < 1$ (Infant Mortality / Burn-In Phase):** Defective components fail early; the failure rate *decreases* over time as weak units are weeded out.
  * **$\beta = 1$ (Memoryless Random Failures):** The equation reduces to the pure exponential $R(t) = e^{-t/\eta}$; failures occur through random external shocks at constant hazard rate $1/\eta$.
  * **$\beta > 1$ (Aging & Fatigue Wear-Out):** Failure hazard accelerates with age as bearings spall and metals fatigue. Moreover, taking the double natural logarithm $\ln[-\ln R(t)] = \beta \ln t - \beta \ln \eta$ via `{{key:LN}} {{key:+/-}} {{key:LN}}` straightens Weibull's curve into a straight line on the regression stack.

### The Centroid Fulcrum, Lever-Arm Outliers & Residual Audits

Before we step up to the SC-32's statistical workbench, three geometric properties of a least-squares line show how the statistics registers unmask hidden traps in a dataset:

1. **The Regression Line as a Mechanical Seesaw Pivoted at $(\bar{x}, \bar{y})$:**
   Rewriting the least-squares intercept equation $b = \bar{y} - m\bar{x}$ as $\bar{y} = m\bar{x} + b$ proves a fundamental geometric fact: **every least-squares regression line passes right through the center of mass—the centroid $(\bar{x}, \bar{y})$—of the data cloud.** Imagine the regression line as a rigid steel beam resting on a fulcrum pin at $(\bar{x}, \bar{y})$, with a vertical spring connecting the beam to each data point $(x_i, y_i)$. Because rotational torque equals $\text{lever arm} \times \text{force}$, any data point far out near the horizontal edges where $|x_i - \bar{x}|$ is large acts with a **long lever arm** and exerts outsized torque on the line. A single typo at an extreme $x_i$ can yank the slope `{{key:m}}` and correlation `{{key:r}}` dramatically, whereas excising that point via `{{key:Σ-}}` lets the beam snap right back (the exact lever-arm effect behind **Francis Anscombe's 1973 Quartet** in Chapter 12).
2. **The Residual Variance Identity ($s_e^2$) & Why $r^2$ Measures Explained Energy:**
   Once you fit $\hat{y} = mx + b$ through $n$ data pairs, how much vertical scatter remains unexplained around the line? You do not have to loop back through the $n$ points to compute the residual standard error $s_e = \sqrt{\frac{1}{n-2}\sum(y_i - \hat{y}_i)^2}$ (where the denominator **$n - 2$** reflects the fact that estimating *two* parameters—both slope $m$ and intercept $b$—consumes two degrees of freedom). By orthogonality of the least-squares projection, the total variance splits into the explained regression component $r^2$ and the unexplained residual fraction $(1 - r^2)$:
   $$\sum_{i=1}^n (y_i - \hat{y}_i)^2 = (n - 1) s_y^2 \left(1 - r^2\right) \implies s_e = s_y \sqrt{\frac{n - 1}{n - 2}\left(1 - r^2\right)}$$
   Using only `{{key:sy}}`, `{{key:r}}`, and `{{key:n}}` from the statistical menus, you can compute the exact residual standard error $s_e$ around the regression line in seconds!
3. **Propagation of Measurement Uncertainty in Calibration Chains:**
   When two independent random variables $X$ and $Y$ with standard uncertainties $\sigma_X$ and $\sigma_Y$ are combined into $Z = aX \pm bY$, their **variances** add in quadrature ($\sigma_Z = \sqrt{a^2\sigma_X^2 + b^2\sigma_Y^2}$)—the exact statistical twin of the Pythagorean theorem (`{{key:▸θ,r}}` on the stack). And for a general smooth function $Z = g(X, Y)$, **Gauss's Law of Error Propagation** combines the partial derivatives with the covariance $\operatorname{Cov}(X, Y) = r s_x s_y$:
   $$\sigma_Z^2 \approx \left(\frac{\partial g}{\partial X}\right)^2 \sigma_X^2 + \left(\frac{\partial g}{\partial Y}\right)^2 \sigma_Y^2 + 2\left(\frac{\partial g}{\partial X}\right)\left(\frac{\partial g}{\partial Y}\right) r\,\sigma_X \sigma_Y$$

---

## On the Stack: Accumulator Statistics, Normal Probability & Regression

Unlike spreadsheet-style calculators that hide data inside modal tables, the SC-32 connects the live **Four-Register Stack (`X, Y, Z, T`)** directly to **six dedicated 64-bit hardware accumulators** ($\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$):

> **Guided Workflow: Why Bivariate Data Pairs Enter as `y_k ENTER x_k Σ+`**
> 1. **Coordinate-Plane Stack Geometry (`Y = y_k, X = x_k`):** When logging a bivariate observation $(x_k, y_k)$ on the SC-32, you always key **`y_k {{key:ENTER}} x_k {{key:Σ+}}`**. Why $y_k$ first and $x_k$ second? Because `{{key:ENTER}}` lifts the vertical response $y_k$ onto **Shelf $Y$** while leaving the horizontal predictor $x_k$ on **Shelf $X$**—so the register names $(Y, X)$ on the display match the $(y, x)$ axes of the coordinate plane! (For 1D univariate samples $x_k$, simply key `x_k {{key:Σ+}}`; for weighted averages, place the weight $w_k$ in Shelf $Y$ and the reading $x_k$ in Shelf $X$.)
> 2. **On-Stack Linearization Before `{{key:Σ+}}`:** Because $(y_k, x_k)$ sit live on the stack before accumulation, tapping `{{key:LN}}` or `{{key:1/x}}` right before `{{key:Σ+}}` straightens exponential, power-law, and Michaelis–Menten hyperbolic curves without any separate curve-fit mode.
> 3. **Instant Inference from Six Running Sums:** Once your data points are accumulated (after clearing prior runs with `{{key:CLΣ}}`), the four Right-Shift statistical menus turn those six sums into instant inference:
>    * **`{{key:x̄,ȳ}}` (`{{key:↱}}` + `{{key:yˣ}}`):** Sample means `{{key:x̄}}`, `{{key:ȳ}}`, and weighted mean `{{key:x̄w}}` ($\Sigma xy / \Sigma y$).
>    * **`{{key:s,σ}}` (`{{key:↱}}` + `{{key:1/x}}`):** Bessel $(n-1)$ sample standard deviations `{{key:sx}}`, `{{key:sy}}` and population $(n)$ spreads `{{key:σx}}`, `{{key:σy}}`.
>    * **`{{key:L.R.}}` (`{{key:↱}}` + `{{key:LN}}`):** Least-squares slope `{{key:m}}`, vertical intercept `{{key:b}}`, Pearson correlation `{{key:r}}`, forward prediction `{{key:ŷ}}` (from $x_0$ in $X$), and inverse calibration `{{key:x̂}}` (from $y_0$ in $X$).

{{res:sc32_normal_pdf:screenshot|Standard Normal PDF f(1.0) = exp(−0.5)/√(2π) = 0.241970724519 on the SC-32.}}

### The 6 Statistical Accumulators, Outlier Retraction & Softkey Menus

On the SC-32, pressing `{{key:Σ+}}` commits the coordinate pair $(Y = y_k,\; X = x_k)$ into six non-volatile hardware registers while displaying the updated sample count $n$ in Register $X$ (and preserving `LASTX`):

| Accumulator | Internal Register | Mathematical Meaning | Primary Statistical Role |
| :---: | :---: | :--- | :--- |
| **$\Sigma x$** | `R.Σ1` | $\sum x_i$ | Sample mean $\bar{x}$, regression slope $m$ |
| **$\Sigma y$** | `R.Σ2` | $\sum y_i$ | Sample mean $\bar{y}$, regression intercept $b$, total weight in $\bar{x}_w$ |
| **$\Sigma x^2$** | `R.Σ3` | $\sum x_i^2$ | $x$-variance and standard deviations ($s_x, \sigma_x$) |
| **$\Sigma y^2$** | `R.Σ4` | $\sum y_i^2$ | $y$-variance and standard deviations ($s_y, \sigma_y$) |
| **$\Sigma xy$** | `R.Σ5` | $\sum (x_i \cdot y_i)$ | Bivariate covariance, Pearson $r$, and weighted sum $\sum w_i x_i$ |
| **$n$** | `R.Σ6` | Sample count | Normalization and Bessel degrees of freedom ($n - 1$) |

Accessed via Right Shift `{{key:↱}}` across the top scientific row, the four statistical menus map onto the six LFU dynamic softkeys (`{{key:LFU0}}` through `{{key:LFU5}}`):

| Sub-Menu | Primary Invocation & Key Position | `{{key:LFU0}}` | `{{key:LFU1}}` | `{{key:LFU2}}` | `{{key:LFU3}}` | `{{key:LFU4}}` | `{{key:LFU5}}` |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Sums Menu** | `{{key:SUMS}}` (above `{{key:Σ+}}`) | `{{key:Σx}}` | `{{key:Σy}}` | `{{key:Σx²}}` | `{{key:Σy²}}` | `{{key:Σxy}}` | `{{key:n}}` |
| **2. Means Menu** | `{{key:x̄,ȳ}}` (above `{{key:yˣ}}`) | `{{key:x̄}}` | `{{key:ȳ}}` | `{{key:x̄w}}` | — | — | — |
| **3. Std Dev Menu** | `{{key:s,σ}}` (above `{{key:1/x}}`) | `{{key:sx}}` | `{{key:sy}}` | `{{key:σx}}` | `{{key:σy}}` | — | — |
| **4. Regression Menu** | `{{key:L.R.}}` (above `{{key:LN}}`) | `{{key:ŷ}}` | `{{key:x̂}}` | `{{key:r}}` | `{{key:m}}` | `{{key:b}}` | — |

What if your finger slips on the sixth data pair $(x = 15, y = 3.5)$, transposing $y$ so you accidentally enter $(x = 15, y = 5.3)$? When the current sample count is $n = 6$, watch how `{{key:Σ-}}` excises the bad point and splices in the corrected reading without losing the first five points:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `5.3 {{key:ENTER}} 15` | $0.0000$ | $0.0000$ | $5.3000$ | $15.0000$ | Key erroneous pair $(x=15, y=5.3)$ |
| `{{key:Σ-}}` | $0.0000$ | $0.0000$ | $5.3000$ | **$5.0000$** | Subtract from accumulators; $n$ decrements to 5 |
| `3.5 {{key:ENTER}} 15` | $0.0000$ | $5.3000$ | $3.5000$ | $15.0000$ | Key corrected pair $(x=15, y=3.5)$ |
| `{{key:Σ+}}` | $0.0000$ | $5.3000$ | $3.5000$ | **$6.0000$** | Accumulate corrected pair; $n$ restored to 6 |

---

### Weighted Sensor Fusion, Six Sigma Capability ($C_p, C_{pk}$), Control Limits & Standard Error

Four univariate and quality-control workflows illustrate how the six accumulators power laboratory metrology and shop-floor inspection:

In **Inverse-Variance Weighted Laboratory Sensor Fusion ($\bar{x}_w = \Sigma xy / \Sigma y$)**, three independent observatory instruments measure the same astrometric parallax angle—$x_1 = 10\text{ mas}$, $x_2 = 25\text{ mas}$, and $x_3 = 45\text{ mas}$—with different noise levels. Gauss proved that the minimum-variance combined estimate weights each reading by its **inverse variance** $w_i = 1/\sigma_i^2$, here $w_1 = 40$, $w_2 = 60$, and $w_3 = 20\text{ mas}^{-2}$. Load each precision weight $w_i$ into Register $Y$ and its measurement $x_i$ into Register $X$ before pressing `{{key:Σ+}}`. Because `{{key:Σ+}}` accumulates $\Sigma(w_i x_i)$ inside `R.Σ5` ($\Sigma xy$) and $\Sigma w_i$ inside `R.Σ2` ($\Sigma y$), opening `{{key:x̄,ȳ}}` and tapping `{{key:x̄w}}` (`{{key:LFU2}}`) computes the exact inverse-variance fused estimate $\bar{x}_w = \frac{\Sigma xy}{\Sigma y} = \frac{2800}{120} = 23.3333\text{ mas}$. Opening `{{key:SUMS}}` and tapping `{{key:Σy}}` (`{{key:LFU1}}`) then recalls the total combined precision weight $120.0\text{ mas}^{-2}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `{{key:CLΣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Clear all 6 statistical accumulators |
| `40 {{key:ENTER}} 10 {{key:Σ+}}` | $0.0000$ | $0.0000$ | $40.0000$ | $1.0000$ | Sensor 1 logged ($w_1=40, x_1=10;\; n=1$) |
| `60 {{key:ENTER}} 25 {{key:Σ+}}` | $0.0000$ | $40.0000$ | $60.0000$ | $2.0000$ | Sensor 2 logged ($w_2=60, x_2=25;\; n=2$) |
| `20 {{key:ENTER}} 45 {{key:Σ+}}` | $40.0000$ | $60.0000$ | $20.0000$ | $3.0000$ | Sensor 3 logged ($w_3=20, x_3=45;\; n=3$) |
| `{{key:x̄w}}` | $40.0000$ | $60.0000$ | $20.0000$ | **$23.3333$** | Via `{{key:x̄,ȳ}}` $\to$ `{{key:x̄w}}`: inverse-variance weighted mean $\bar{x}_w$ (mas) |
| `{{key:Σy}}` | $60.0000$ | $20.0000$ | $23.3333$ | **$120.0000$** | Via `{{key:SUMS}}` $\to$ `{{key:Σy}}`: total precision weight $\Sigma y = \sum w_i$ ($\text{mas}^{-2}$) |

For a **Six Sigma CNC Lathe Capability Audit ($25.00 \pm 0.10\text{ mm}$, $n = 10$ shafts)**, accumulating univariate measurements $x_1, \dots, x_n$ requires only keying each reading into Register $X$ and pressing `{{key:Σ+}}`. Logging our ten micrometer shaft diameters gives sample mean $\bar{x} = \mathbf{25.0300\text{ mm}}$ and Bessel sample spread $s_x = \mathbf{0.018257\text{ mm}}$. Dividing the $0.20\text{ mm}$ tolerance width by $6s_x$ via `{{res:sc32_09_statistics_curve_fitting_seq_03:keys}}` yields potential capability $C_p =$ **`{{res:sc32_09_statistics_curve_fitting_seq_03:value}}`**, while comparing $\bar{x}$ against the upper specification limit $\text{USL} = 25.10\text{ mm}$ via `{{res:sc32_09_statistics_curve_fitting_seq_04:keys}}` yields $C_{pk} =$ **`{{res:sc32_09_statistics_curve_fitting_seq_04:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `25.02 {{key:Σ+}} 25.04 {{key:Σ+}} 25.01 {{key:Σ+}} 25.03 {{key:Σ+}} 25.05 {{key:Σ+}} 25.02 {{key:Σ+}} 25.00 {{key:Σ+}} 25.04 {{key:Σ+}} 25.03 {{key:Σ+}} 25.06 {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | Accumulate 10 shaft diameter samples |
| `{{key:x̄,ȳ}} {{key:x̄}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$25.0300$** | Sample mean diameter $\bar{x}$ (mm) |
| `{{key:s,σ}} {{key:sx}}` | $0.0000$ | $0.0000$ | $25.0300$ | **$0.018257$** | Sample standard deviation $s_x$ (mm) |
| `{{res:sc32_09_statistics_curve_fitting_seq_03:keys}}` | $25.0300$ | $25.0300$ | $0.0183$ | **`{{res:sc32_09_statistics_curve_fitting_seq_03:value}}`** | Process capability $C_p = \frac{\text{USL}-\text{LSL}}{6s_x}$ |
| `{{res:sc32_09_statistics_curve_fitting_seq_04:keys}}` | $0.0183$ | $0.0183$ | $1.8258$ | **`{{res:sc32_09_statistics_curve_fitting_seq_04:value}}`** | Process capability index $C_{pk} = \frac{\text{USL}-\bar{x}}{3s_x}$ |

The pair $(C_p = 1.8257,\; C_{pk} = 1.2780)$ tells a clear shop-floor story: because $C_p > 1.33$, the lathe spindle itself is mechanically tight enough for Six Sigma production, but because $C_{pk} = 1.2780 < 1.33$, thermal tool growth has shifted the process center $+0.030\text{ mm}$ toward the upper limit—telling the machinist to dial in a $-0.030\text{ mm}$ tool-offset correction rather than rebuilding the spindle.
* **Shift-Invariance Speed & Numerical Hygiene ($s_{x - c} = s_x$):** Translating an entire dataset by a constant datum $c$ shifts the mean ($\overline{x - c} = \bar{x} - c$) without changing the distances between points ($s_{x - c} = s_x$). You can therefore subtract the $25.00\text{ mm}$ nominal diameter mentally and accumulate only the hundredths of a millimeter with `{{key:Σ+}}`: `2 Σ+ 4 Σ+ 1 Σ+ 3 Σ+ 5 Σ+ 2 Σ+ 0 Σ+ 4 Σ+ 3 Σ+ 6 Σ+`. That shortcut cuts keystrokes in half—returning $\bar{d} = 3.0000 \implies \bar{x} = 25.0300\text{ mm}$ and $s_d = 1.8257 \implies s_x = 0.018257\text{ mm}$—while shielding the one-pass variance sum $\Sigma x^2 - (\Sigma x)^2/n$ from catastrophic cancellation whenever raw readings cluster tightly around a large baseline offset.

To establish **Walter Shewhart's $\bar{X}$ Control Limits ($\bar{\bar{X}} = 50.00\text{ mm}, \bar{R} = 0.40\text{ mm}, A_2 = 0.577$)**, we place $\pm 3\sigma_{\bar{x}}$ quality-control guardrails around a centerline of $\bar{\bar{X}} = 50.00\text{ mm}$ using subgroup range $\bar{R} = 0.40\text{ mm}$ and the $n = 5$ subgroup factor $A_2 = 0.577$:

$$\text{UCL} = \bar{\bar{X}} + A_2\bar{R}, \qquad \text{LCL} = \bar{\bar{X}} - A_2\bar{R}$$

The sequence `{{res:sc32_09_statistics_curve_fitting_seq_18:keys}}` forms the control half-width $A_2\bar{R} = 0.2308\text{ mm}$, and adding `50.00 {{key:+}}` places the **Upper Control Limit** at $\text{UCL} = \mathbf{50.2308\text{ mm}}$.

Subtracting that same half-width from the centerline via `{{res:sc32_09_statistics_curve_fitting_seq_19:keys}}` sets the **Lower Control Limit** at $\text{LCL} = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_19:value}}\text{ mm}}$.

Better still, once $A_2\bar{R} = 0.2308$ sits in Register $X$, keying `50.00 {{key:x⇄y}} {{key:-}}` computes $\text{LCL} = \mathbf{49.7692\text{ mm}}$ while automatically capturing $0.2308$ in `LASTX`; following at once with `{{key:LASTX}} 2 {{key:×}} {{key:+}}` adds $2(A_2\bar{R})$ to step straight across to $\text{UCL} = \mathbf{50.2308\text{ mm}}$ while typing `50.00` only once!

Evaluating the **Standard Error of the Mean ($n = 36, \bar{x} = 120.5\text{ MPa}, s = 8.4\text{ MPa}$)** across $n = 36$ aluminum-alloy tensile yield specimens follows the same pattern. Dividing $s = 8.4\text{ MPa}$ by $\sqrt{n}$ with `{{res:sc32_09_statistics_curve_fitting_seq_20:keys}}` reduces the **Standard Error of the Mean** to $\text{SE} = s/\sqrt{n} = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_20:value}}\text{ MPa}}$, and scaling by the two-sided $95\%$ normal multiplier `1.960 {{key:×}}` gives the half-width margin $E = \mathbf{2.7440\text{ MPa}}$.

Adding $E$ to $\bar{x}$ via `{{res:sc32_09_statistics_curve_fitting_seq_21:keys}}` establishes the upper $95\%$ confidence bound $\bar{x} + E = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_21:value}}\text{ MPa}}$, while `{{res:sc32_09_statistics_curve_fitting_seq_22:keys}}` gives the lower bound $\bar{x} - E = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_22:value}}\text{ MPa}}$.

Alternatively, once $E = 2.7440$ sits in Register $X$, key `120.5 {{key:x⇄y}} {{key:+}}` for the upper bound and `{{key:LASTX}} 2 {{key:×}} {{key:-}}` to recover $E$ from `{{key:LASTX}}` and step straight to the lower bound.

---

### Least-Squares Sensor Calibration, Confidence Bands & Spearman Rank Correlation

Streaming the four dead-weight calibration points of our piezoresistive pressure sensor—$10\text{ kPa}$ at $1.25\text{ V}$, $20\text{ kPa}$ at $2.45\text{ V}$, $30\text{ kPa}$ at $3.80\text{ V}$, and $40\text{ kPa}$ at $4.95\text{ V}$—into the accumulators after `{{key:CLΣ}}` builds the regression model on the stack:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $0.00000000$ | Clear all 6 statistical accumulators ($\Sigma x, \Sigma y, \dots = 0$) |
| `1.25` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $1.25000000$ | Enter sensor output voltage $y_1 = 1.25\text{ V}$ |
| `{{key:ENTER}}` | $0.00000000$ | $0.00000000$ | $1.25000000$ | $1.25000000$ | Stage $y_1 = 1.25\text{ V}$ in Register $Y$ |
| `10` | $0.00000000$ | $0.00000000$ | $1.25000000$ | $10.0000000$ | Enter reference pressure $x_1 = 10\text{ kPa}$ in Register $X$ |
| `{{key:Σ+}}` | $0.00000000$ | $0.00000000$ | $1.25000000$ | $1.00000000$ | Accumulate Point 1 $(10, 1.25)$; display sample count $n = 1$ |
| `2.45 {{key:ENTER}}` | $0.00000000$ | $1.25000000$ | $2.45000000$ | $2.45000000$ | Stage voltage $y_2 = 2.45\text{ V}$ in Register $Y$ |
| `20 {{key:Σ+}}` | $0.00000000$ | $1.25000000$ | $2.45000000$ | $2.00000000$ | Accumulate Point 2 $(20, 2.45)$; sample count $n = 2$ |
| `3.80 {{key:ENTER}}` | $1.25000000$ | $2.45000000$ | $3.80000000$ | $3.80000000$ | Stage voltage $y_3 = 3.80\text{ V}$ in Register $Y$ |
| `30 {{key:Σ+}}` | $1.25000000$ | $2.45000000$ | $3.80000000$ | $3.00000000$ | Accumulate Point 3 $(30, 3.80)$; sample count $n = 3$ |
| `4.95 {{key:ENTER}}` | $2.45000000$ | $3.80000000$ | $4.95000000$ | $4.95000000$ | Stage voltage $y_4 = 4.95\text{ V}$ in Register $Y$ |
| `40 {{key:Σ+}}` | $2.45000000$ | $3.80000000$ | $4.95000000$ | $4.00000000$ | Accumulate Point 4 $(40, 4.95)$; sample count $n = 4$ |

Now inspect the accumulated state and calibration predictions across the softkey menus:
* **Raw Accumulator Audit (`{{key:SUMS}}`):** `{{key:Σx}}` $= 100.0$, `{{key:Σy}}` $= 12.45$, `{{key:Σx²}}` $= 3000.0$, `{{key:Σy²}}` $= 46.5075$, `{{key:Σxy}}` $= 373.50$, and `{{key:n}}` $= 4$.
* **Regression Fit (`{{key:L.R.}}`):** `{{key:m}}` $= \mathbf{0.1245000000\text{ V/kPa}}$, `{{key:b}}` $= \mathbf{0.0000000000\text{ V}}$, and `{{key:r}}` $= \mathbf{0.9995648074}$ (so $r^2 = 0.999130$, explaining $99.913\%$ of variance).
* **Forward & Inverse Calibration (`ŷ` and `x̂`) & Two-Point Table Interpolation:** Keying `25 {{key:L.R.}} {{key:ŷ}}` forecasts **`3.1125000000 V`** while placing $r = 0.99956481$ in Register $Y$, and keying `4.00 {{key:L.R.}} {{key:x̂}}` inverts the calibration curve to recover **`32.128514 kPa`**. *(Corvallis Two-Point Table Interpolator: Whenever you need to interpolate between two adjacent rows $(x_1, y_1)$ and $(x_2, y_2)$ of a steam or atmosphere lookup table, log both points after `{{key:CLΣ}}` as `y1 ENTER x1 Σ+ y2 ENTER x2 Σ+`. Because two points determine an exact secant line with $r = \pm 1.000000$, querying `ŷ` at $x_0$ performs **forward linear interpolation** and querying `x̂` at $y_0$ performs **inverse linear interpolation** without manual difference quotients—and applying `{{key:LN}}` before `Σ+` performs log-linear interpolation across exponential tables!)*
* **Confidence vs. Prediction Margins at $x_0 = \bar{x} = 25\text{ kPa}$ ($s_e = 0.058095\text{ V},\; t_{0.025, 2} = 4.303$):**
  * For the **pointwise Student-$t$ confidence interval (and Working-Hotelling hyperbolic envelope)** of the mean line, evaluating $E = t_{0.025,2} \cdot s_e / \sqrt{4}$ via `4.303 {{key:ENTER}} 0.058095 {{key:×}} 4 {{key:1/x}} {{key:√x}} {{key:×}}` gives $E = \mathbf{0.1250\text{ V}}$ ($3.1125 \pm 0.1250\text{ V}$).
  * For the **single-observation prediction band**, scaling by $\sqrt{1 + 1/4}$ via `4 {{key:1/x}} 1 {{key:+}} {{key:√x}} 0.058095 {{key:×}} 4.303 {{key:×}}` gives $E_{\text{pred}} = \mathbf{0.2795\text{ V}}$ ($3.1125 \pm 0.2795\text{ V}$).

For our five ceramic coatings ranked on Mohs scratch hardness versus wear lifetime with rank discrepancies $d = (1, -1, 2, -1, -1)$, **Spearman's rank correlation** $r_s = 1 - \frac{6\Sigma d_i^2}{n(n^2-1)}$ evaluates on Registers $X$ and $Y$ while Registers $Z$ and $T$ remain at zero. Here the squared rank differences sum to $\Sigma d_i^2 = 1 + 1 + 4 + 1 + 1 = 8.0$—one-fifth of the antipodal reversal sum $\frac{n(n^2 - 1)}{3} = 40.0$ ($r_s = -1.0$) and well below the uncorrelated expectation $\frac{n(n^2 - 1)}{6} = 20.0$ ($r_s = 0.0$). On the stack, form the numerator $6\Sigma d_i^2 = 48.0000$ in Register $Y$ and the denominator $n(n^2 - 1) = 5(24) = 120.0000$ in Register $X$, divide to isolate the discordance penalty $48 / 120 = 0.4000$, and subtract from unity:
* **Keystrokes:** `{{res:sc32_09_statistics_curve_fitting_seq_05:keys}}` $\longrightarrow$ **`0.6000`** ($r_s = +0.6000$).

---

### Gaussian Normal Density, Cumulative Probability, Student's t-Test, Poisson & Weibull

Five probability and reliability distributions showcase the stack's scientific, factorial, and Romberg quadrature engines:

Evaluating the **Gaussian Normal PDF at $x = 115$ ($\mu = 100, \sigma = 15$)**, $f(115; 100, 15) = \frac{1}{15\sqrt{2\pi}}\exp\!\left(-\frac{(115-100)^2}{2(15)^2}\right)$, at one standard deviation above the mean ($z = +1.0$) unfolds in two stack stages. First, square the deviation $(115 - 100)^2 = 225.0$ via `{{res:sc32_09_statistics_curve_fitting_seq_11:keys}}`, form the variance denominator $2\sigma^2 = 450.0$ in Register $X$ with `{{res:sc32_09_statistics_curve_fitting_seq_12:keys}}`, and evaluate `{{key:÷}} {{key:+/-}} {{key:eˣ}}` to leave the bell factor $e^{-0.5} = 0.60653066$ on the stack. Second, construct the normalization constant $\sigma\sqrt{2\pi} = 37.59942412$ via `{{res:sc32_09_statistics_curve_fitting_seq_13:keys}}` while $e^{-0.5}$ rides in Register $Y$, and press `{{key:÷}}` to obtain **`0.0161313817`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `115 {{key:ENTER}}` | $0.00000000$ | $0.00000000$ | $115.000000$ | $115.000000$ | Stage observation $x = 115$ in Register $Y$ |
| `100 {{key:-}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $15.0000000$ | Subtract mean $\mu = 100$: deviation $x - \mu = 15.0$ |
| `{{key:x²}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $225.000000$ | Squared deviation $(x - \mu)^2 = 225.0$ |
| `15 {{key:x²}}` | $0.00000000$ | $0.00000000$ | $225.000000$ | $225.000000$ | Variance $\sigma^2 = 15^2 = 225.0$ (lifts $(x-\mu)^2$ to $Y$) |
| `2 {{key:×}}` | $0.00000000$ | $0.00000000$ | $225.000000$ | $450.000000$ | Denominator $2\sigma^2 = 450.0$ |
| `{{key:÷}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $0.50000000$ | Normalized half-square $z^2/2 = 225/450 = 0.50$ |
| `{{key:+/-}} {{key:eˣ}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $0.60653066$ | Gaussian exponential factor $\exp(-0.5) \approx 0.606531$ |
| `15 {{key:ENTER}}` | $0.00000000$ | $0.60653066$ | $15.0000000$ | $15.0000000$ | Stage standard deviation $\sigma = 15$ (lifts $e^{-0.5}$ to $Z$) |
| `2 {{key:π}}` | $0.60653066$ | $15.0000000$ | $2.00000000$ | $3.14159265$ | Load $2$ and $\pi$ onto Registers $Y$ and $X$ |
| `{{key:×}} {{key:√x}}` | $0.60653066$ | $0.60653066$ | $15.0000000$ | $2.50662827$ | Evaluate $\sqrt{2\pi} \approx 2.506628$ |
| `{{key:×}}` | $0.60653066$ | $0.60653066$ | $0.60653066$ | $37.5994241$ | Normalization constant $\sigma\sqrt{2\pi} \approx 37.599424$ |
| `{{key:÷}}` | $0.60653066$ | $0.60653066$ | $0.60653066$ | $0.01613138$ | Gaussian density $f(115; 100, 15) = \mathbf{0.0161313817}$ |

*(Multiplying $f(115; 100, 15) = 0.0161313817$ by $\sigma = 15$ recovers the standard normal height $\phi(1.0) = \frac{1}{\sqrt{2\pi}}e^{-0.5} = \mathbf{0.2419707245}$ shown on the transflective LCD screenshot above.)*

To compute the **Cumulative Normal Probability $\Phi(1.0) = 0.5 + \frac{1}{\sqrt{2\pi}}\int_0^{1.0} e^{-t^2/2}\,dt$ via Romberg Quadrature**, recall from Chapter 8 that the left half of the symmetric bell curve from $-\infty$ to $0$ has area $0.50000000$. Finding $\Phi(z)$ for any $z > 0$ therefore requires only integrating the finite half-bell $\int_0^z e^{-t^2/2}\,dt$, dividing by $\sqrt{2\pi}$, and adding $0.5$. With `X {{key:x²}} 2 {{key:÷}} {{key:+/-}} {{key:eˣ}}` active in `{{key:EQN}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `0 {{key:ENTER}} 1.0` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $1.00000000$ | Push integration limits $a=0, b=1.0$ |
| `{{key:∫}}` | $0.00000000$ | $0.00000000$ | $1.15 \times 10^{-12}$ | $0.85562439$ | Select variable `X`: Romberg quadrature $\int_0^1 e^{-t^2/2}\,dt$ |
| `2 {{key:π}} {{key:×}} {{key:√x}} {{key:÷}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $0.34134475$ | Divide by $\sqrt{2\pi}$; area from mean to $Z=1.0$ |
| `0.5 {{key:+}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | **$0.84134475$** | Cumulative probability $\Phi(1.0)$ ($84.13\%$) |

Doubling the central slice $2 \times 0.34134475 = \mathbf{0.68268949}$ confirms the $\pm 1\sigma$ Empirical Rule ($68.27\%$).

For **William Sealy Gosset's Student Two-Sample $t$-Test ($df = 16$)**, we compare Titanium Alloy A ($n_1 = 8$ tensile coupons, $\bar{x}_1 = 450.0\text{ MPa}$, $s_1 = 12.5\text{ MPa}$) against Titanium Alloy B ($n_2 = 10$ coupons, $\bar{x}_2 = 468.0\text{ MPa}$, $s_2 = 14.0\text{ MPa}$). Notice why Gosset's pooled variance $s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$ and the resulting $t$-statistic evaluate cleanly across Registers $X$ and $Y$ alone while Registers $Z$ and $T$ remain at zero: rather than taking an unweighted average of $s_1^2$ and $s_2^2$, pooling weights each sample variance by its Bessel degrees of freedom ($df_1 = n_1 - 1 = 7$ and $df_2 = n_2 - 1 = 9$), giving the larger $10\text{-coupon}$ batch of Alloy B proportionally greater authority in estimating the shared metallurgical scatter.

Evaluating Alloy A's sum of squared deviations $(n_1 - 1)s_1^2 = 7(12.5^2) = 1,093.7500\text{ MPa}^2$ in Register $X$ and adding Alloy B's contribution $(n_2 - 1)s_2^2 = 9(14^2) = 1,764.0000\text{ MPa}^2$ forms the combined numerator $2,857.7500\text{ MPa}^2$ on the stack. Dividing by the combined $df = 7 + 9 = 16$ degrees of freedom and taking `{{key:√x}}` extracts the pooled standard deviation $s_p = \mathbf{13.364482\text{ MPa}}$ (pulled closer to $s_2 = 14.0\text{ MPa}$ than to $s_1 = 12.5\text{ MPa}$ by the $9:7$ degree-of-freedom weighting).

Scaling $s_p$ by the two-sample uncertainty factor $\sqrt{\frac{1}{8} + \frac{1}{10}}$ via `{{key:1/x}}` and `√x` converts pooled spread into the standard error of the difference between means, $\text{SE} = \mathbf{6.339330\text{ MPa}}$. Forming the mean shift $\bar{x}_1 - \bar{x}_2 = 450.0 - 468.0 = -18.0000\text{ MPa}$ in Register $X$ lifts $\text{SE}$ to Register $Y$, and `{{key:x⇄y}} {{key:÷}}` divides signal by noise to yield Student's $t = \mathbf{-2.839422}$—surpassing the two-sided $95\%$ critical threshold $t_{0.025, 16} = 2.120$ and confirming a genuine alloy strength gain.

To evaluate the **Poisson Packet Arrival PMF ($P(X = 6) = \frac{4.5^6 e^{-4.5}}{6!}$)** when an optical router receives $\lambda = 4.5\text{ packets/ms}$ on average, we form the arrival-rate power $\lambda^k = 4.5^6 = 8,303.765625$ in Register $Y$ and the exponential survival factor $e^{-4.5} \approx 0.01110900$ in Register $X$, multiply to collapse the numerator $\lambda^k e^{-\lambda} = 92.246538$, and divide by the factorial denominator $k! = 6! = 720$ without ever touching Registers $Z$ or $T$:
* **Keystrokes:** `{{res:sc32_09_statistics_curve_fitting_seq_06:keys}}` $\longrightarrow$ **`{{res:sc32_09_statistics_curve_fitting_seq_06:value}}`** ($12.81\%$).

Finally, for **Waloddi Weibull's Spindle Bearing Survival Law ($t = 3,000\text{ hr}, \eta = 5,000\text{ hr}, \beta = 1.8$)**, the stretched-exponential reliability $R(t) = \exp\!\left[-(t/\eta)^\beta\right]$ unpeels from the inside out on Register $X$ without touching Registers $Z$ or $T$. Because the shape modulus $\beta = 1.8$ exceeds unity, the bearing operates in the aging wear-out regime where rolling-contact fatigue cracks nucleate and the hazard rate $h(t) = \frac{\beta}{\eta}(t/\eta)^{\beta - 1}$ climbs as $t^{0.8}$. Normalize service time by characteristic life ($t/\eta = 3000/5000 = 0.6000$), raise that ratio to the fatigue exponent $(0.6000)^{1.8} = 0.398660$, and evaluate $\exp(-0.398660)$ in place on Register $X$:
* **Keystrokes:** `{{res:sc32_09_statistics_curve_fitting_seq_09:keys}}` $\longrightarrow$ **`0.6712`** ($67.12\%$ survival probability, or $32.88\%$ cumulative failure risk before overhaul).

---

### Linearized Curve Fitting on the Stack: Log-Log Power Laws & Double-Reciprocal Kinetics

To fit the **Wind Turbine Cubic Power Law ($P = kv^m$ at $(4, 16), (6, 54), (8, 128), (10, 250)$)** from four wind-tunnel test points, apply `{{key:LN}}` to both output power $P$ and wind speed $v$ right on the stack before tapping `{{key:Σ+}}`. Because unary keys like `{{key:LN}}` and `{{key:1/x}}` terminate digit entry and arm **automatic stack lift**, `16 {{key:LN}} 4 {{key:LN}} {{key:Σ+}}` needs no `{{key:ENTER}}` between `16 {{key:LN}}` and `4`—typing `4` lifts $\ln(16)$ into Register $Y$ automatically, saving an `{{key:ENTER}}` tap on every data pair! Querying `{{key:L.R.}} {{key:m}}` confirms the cubic exponent $m = \mathbf{3.000000}$, `{{key:b}} {{key:eˣ}}` recovers $k = e^b = \mathbf{0.250000}$, and forecasting output at $12\text{ m/s}$ with `{{res:sc32_09_statistics_curve_fitting_seq_14:keys}}` delivers **`{{res:sc32_09_statistics_curve_fitting_seq_14:value}}`** kW:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `{{key:CLΣ}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $0.00000000$ | Clear all 6 statistical accumulators |
| `16 {{key:LN}} 4 {{key:LN}} {{key:Σ+}}` | $0.00000000$ | $0.00000000$ | $2.77258872$ | $1.00000000$ | Point 1 logged ($n=1$ in $X$, $\ln P_1$ in $Y$) |
| `54 {{key:LN}} 6 {{key:LN}} {{key:Σ+}}` | $0.00000000$ | $2.77258872$ | $3.98898405$ | $2.00000000$ | Point 2 logged ($n=2$ in $X$, $\ln P_2$ in $Y$) |
| `128 {{key:LN}} 8 {{key:LN}} {{key:Σ+}}` | $2.77258872$ | $3.98898405$ | $4.85203026$ | $3.00000000$ | Point 3 logged ($n=3$ in $X$, $\ln P_3$ in $Y$) |
| `250 {{key:LN}} 10 {{key:LN}} {{key:Σ+}}` | $3.98898405$ | $4.85203026$ | $5.52146092$ | $4.00000000$ | Point 4 logged ($n=4$ in $X$, $\ln P_4$ in $Y$) |
| `{{key:L.R.}} {{key:m}}` | $3.98898405$ | $4.85203026$ | $5.52146092$ | **$3.00000000$** | Regression slope $m = 3.0$ (cubic power law) |
| `{{key:b}} {{key:eˣ}}` | $4.85203026$ | $5.52146092$ | $3.00000000$ | **$0.25000000$** | Via `{{key:L.R.}}` $\to$ `{{key:b}}` then `{{key:eˣ}}`: scale $k = e^b = 0.250\text{ kW/(m/s)}^3$ |
| `12 {{key:ENTER}} 3 {{key:yˣ}} 0.25 {{key:×}}` | $3.00000000$ | $3.00000000$ | $0.25000000$ | **$432.000000$** | Predicted power $P(12) = 0.25 \times 12^3\text{ kW}$ |

In the same spirit, **Lineweaver-Burk Double-Reciprocal Enzyme Kinetics ($\frac{1}{v} = \frac{K_m}{V_{\max}}\frac{1}{[S]} + \frac{1}{V_{\max}}$)** linearizes a saturating Michaelis-Menten hyperbola when you tap `{{key:1/x}}` on each reaction velocity $v_k$ and substrate concentration $[S]_k$ before pressing `{{key:Σ+}}`. Streaming the four double-reciprocal pairs via `{{res:sc32_09_statistics_curve_fitting_seq_17:keys}}` determines the maximum turnover ceiling $V_{\max} = 1/b = \mathbf{0.6346\,\mu\text{M/min}}$ and the half-saturation Michaelis constant $K_m = m \cdot V_{\max} =$ **`{{res:sc32_09_statistics_curve_fitting_seq_17:value}} mM`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `{{key:CLΣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Clear all 6 statistical accumulators |
| `.182 {{key:1/x}} 2.0 {{key:1/x}} {{key:Σ+}}` | $0.0000$ | $0.0000$ | $5.4945$ | $1.0000$ | Point 1 logged ($1/v_1$ in $Y$, $1/[S]_1$ in $X$; $n=1$) |
| `.286 {{key:1/x}} 4.0 {{key:1/x}} {{key:Σ+}}` | $0.0000$ | $5.4945$ | $3.4965$ | $2.0000$ | Point 2 logged ($1/v_2$ in $Y$, $1/[S]_2$ in $X$; $n=2$) |
| `.400 {{key:1/x}} 8.0 {{key:1/x}} {{key:Σ+}}` | $5.4945$ | $3.4965$ | $2.5000$ | $3.0000$ | Point 3 logged ($1/v_3$ in $Y$, $1/[S]_3$ in $X$; $n=3$) |
| `.471 {{key:1/x}} 16.0 {{key:1/x}} {{key:Σ+}}` | $3.4965$ | $2.5000$ | $2.1231$ | $4.0000$ | Point 4 logged ($1/v_4$ in $Y$, $1/[S]_4$ in $X$; $n=4$) |
| `{{key:b}}` | $3.4965$ | $2.5000$ | $2.1231$ | **$1.5759$** | Via `{{key:L.R.}}` $\to$ `{{key:b}}`: double-reciprocal intercept $1/V_{\max}$ |
| `{{key:1/x}}` | $3.4965$ | $2.5000$ | $2.1231$ | **$0.6346$** | Invert intercept for maximum velocity $V_{\max}$ ($\mu\text{M/min}$) |
| `{{key:m}}` | $2.5000$ | $2.1231$ | $0.6346$ | **$7.7981$** | Via `{{key:L.R.}}` $\to$ `{{key:m}}`: slope $K_m / V_{\max}$ (lifts $V_{\max}$ into $Y$) |
| `{{key:×}}` | $2.5000$ | $2.5000$ | $2.1231$ | **$4.9484$** | Multiply for Michaelis constant $K_m = m \times V_{\max}$ (mM) |

Finally, **Semi-Log Decay, Weibull Reliability Fitting & `STAT ERROR` Protection** follow the same on-stack pattern when only the vertical variable obeys an exponential law $A(t) = A_0 e^{-\lambda t}$. For our nuclear-medicine Technetium-99m ($^{99\text{m}}\text{Tc}$) calibration points—$1000\text{ MBq}$ at $t = 0\text{ hr}$, $794\text{ MBq}$ at $2\text{ hr}$, $630\text{ MBq}$ at $4\text{ hr}$, and $500\text{ MBq}$ at $6\text{ hr}$—apply `{{key:LN}}` solely to the $y$-coordinate before pressing `{{key:Σ+}}`: clear with `{{key:CLΣ}}`, then stream `1000 LN 0 Σ+`, `794 LN 2 Σ+`, `630 LN 4 Σ+`, and `500 LN 6 Σ+`.

Tapping `{{key:L.R.}} {{key:m}} {{key:+/-}}` reads the decay constant $\lambda = \mathbf{0.11552\text{ hr}^{-1}}$, and dividing $\ln 2$ by $\lambda$ converts it into the clinical half-life $t_{1/2} = \frac{\ln 2}{\lambda} = \mathbf{6.000\text{ hours}}$, while `{{key:b}} {{key:eˣ}}` recovers the initial activity $A_0 = \mathbf{1000.1\text{ MBq}}$. Weather-balloon radiosondes use this identical semi-log workflow on $\ln P_k$ versus altitude $h_k$ to calibrate sea-level baseline pressure $P_0 = e^b$ and local scale height $H = -1/m$.

For mechanical fatigue life testing across multiple failure times $t_k$ with empirical survival fractions $R_k$, applying the double-logarithm transform $R_k$ (`LN +/- LN`) into Register $Y$ and $t_k$ (`LN`) into Register $X$ before `{{key:Σ+}}` fits Waloddi Weibull's line $\ln[-\ln R(t)] = \beta \ln t - \beta \ln \eta$, where `{{key:m}}` reads the shape modulus $\beta$ and $\eta = \exp(-b/\beta)$ recovers the characteristic life. Whenever you query Bessel's sample standard deviation `{{key:sx}}` or `{{key:sy}}` with fewer than two observations ($n \le 1$), query `{{key:x̄}}` with $n = 0$, or query regression slope or correlation when all $x$-values are identical ($n\Sigma x^2 - (\Sigma x)^2 = 0$, a vertical line), the SC-32 protects the calculation by raising **`STAT ERROR`** (Code 04), which clears non-destructively via `{{key:C}}` without disturbing your six statistical registers.

---

### From Noisy Measurements to the Switches Inside the Silicon

Every statistical summary in this chapter—from Gauss's least-squares slope $m$ and Pearson's $r$ to Weibull's double-logarithmic reliability line—ultimately commits its state into six 64-bit registers (`R.Σ1` through `R.Σ6`) inside the calculator's silicon core.

What physical mechanism inside that chip stores those running sums, and how does a silent lattice of microscopic transistors add, subtract, and compare numbers when you press a key?

Inside a microcontroller, there are no brass gears, no slide-rule scales, and no ten-fingered decimal wheels—only binary transistor switches that turn **ON (`1`)** or **OFF (`0`)**. How can a collection of two-state switches represent negative numbers without a minus-sign wire? How did George Boole's 1854 algebra of human thought merge with Claude Shannon's 1937 master's thesis to build arithmetic out of logic gates (`AND`, `OR`, `XOR`, `NOT`)? And how do Euclidean remainder division (`÷R`) and discrete combinatorics govern everything from IPv4 network masks to the birthday collision paradox? In **[Chapter 10: Ones, Zeros, and the 36-Bit Machine: From Leibniz and Shannon to Modern Computing](10-computer-science-bases.md)**, we step inside the digital machine itself.
