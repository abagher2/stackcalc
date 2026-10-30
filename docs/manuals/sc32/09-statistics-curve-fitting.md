---
title: "Chapter 9: Least Squares, Small Samples & the Geometry of Uncertainty | Thinking in the Stack (SC-32)"
description: "Gauss's 1801 recovery of Ceres, Galton's Quincunx and regression to the mean, Bessel's n - 1 correction, Student's Guinness Brewery t-test, and Weibull reliability on the StackCalc SC-32."
---

# Chapter 9: Least Squares, Small Samples & the Geometry of Uncertainty

## The Lost Planet Ceres, Galton's Quincunx & Bessel's n − 1 Correction

On the night of January 1, 1801, the Italian astronomer and Theatine priest Giuseppe Piazzi peered through his vertical Ramsden circle telescope at the Palermo Observatory in Sicily. While compiling a star catalog in the constellation Taurus, Piazzi noticed a faint, uncataloged eighth-magnitude point of light. The next night, it had shifted slightly against the background stars.

Across a forty-one-day span in January and early February 1801 (recording 24 nights of observations), Piazzi tracked the object before falling ill as it drifted into the daytime glare of the Sun. Piazzi had discovered Ceres, the largest body in the asteroid belt between Mars and Jupiter. Yet Piazzi had observed Ceres across barely three degrees of sky, less than one percent of its full orbit, and every telescope reading was affected by atmospheric refraction, clock drift, and human visual error. When European astronomers attempted to compute Ceres's orbit from three selected observations, their predictions diverged across the sky.

In Göttingen, Carl Friedrich Gauss, then twenty-four, read Piazzi's published sightings and approached the problem from a different premise. Instead of selecting three observations and treating them as exact, Gauss analyzed how random observational errors behave and how all of Piazzi's noisy sightings across that forty-one-day arc could be combined so that their random errors cancel one another.

Over three months in the autumn of 1801, Gauss combined his geometry of elliptical orbits with two foundational principles that established modern statistical inference {{cite:gauss1809}}: the *Method of Least Squares*, which identifies the most probable trajectory through a cloud of noisy measurements as the unique curve that minimizes the sum of the squared residuals (the squared vertical distances between the observed data points and the theoretical curve), and the *Gaussian Law of Error* (the normal distribution), under which small, independent random disturbances cluster symmetrically around the true value according to the exponential-square density $e^{-z^2/2}$.

On December 31, 1801—after first re-sighting the faint object on December 7 and waiting through winter clouds to confirm its motion—the German astronomer Franz Xaver von Zach verified Ceres in the patch of sky in Virgo predicted by Gauss's least-squares calculation, within half a degree of Gauss's coordinates. Gauss had demonstrated that combining noisy measurements mathematically extracts a signal more accurate than any single instrument reading.

### Francis Galton's 1873 Quincunx and the Central Limit Theorem

Gauss's bell curve recurs across the physical and biological sciences, governing astronomical telescope errors, the heights of forest trees, the thermal noise of resistors, and the diameters of machined steel shafts.

In 1873, during a Friday Evening Discourse at the Royal Institution in London, the Victorian polymath Francis Galton demonstrated a tabletop apparatus that made the emergence of the normal curve directly visible: the Quincunx (now known as the Galton Board). Galton constructed a vertical wooden frame behind a pane of glass, with a funnel at the top, twelve staggered horizontal rows of brass pins in the middle (arranged like the five-spot *quincunx* pattern on a die), and a row of narrow vertical compartments at the bottom. When lead shot pellets were poured into the top funnel, each pellet cascaded through the brass pins. At each of the $12$ rows of pins, a falling pellet encountered an independent $50/50$ binary deflection: bounce Left ($L$) or bounce Right ($R$).

As the thousand pellets settled into the vertical compartments at the bottom, they neither formed a flat horizontal layer nor accumulated in an irregular heap; instead, the lead shot consistently formed the smooth, symmetric profile of Gauss's normal curve.

The shape follows from counting the combinatorial paths. For a pellet to land in Slot $0$ at the far left edge, it must bounce Left twelve times in succession ($LLLLLLLLLLLL$), which represents only $\binom{12}{0} = 1\text{ path}$ out of $2^{12} = 4,096$ possible trajectories (probability $0.024\%$). To land in Slot $1$, there are $\binom{12}{1} = 12$ paths. By the time a pellet reaches Slot $6$ in the center—six Left bounces and six Right bounces in any order—there are $\binom{12}{6} = \mathbf{924}$ distinct paths leading to that central compartment.

Galton's Quincunx is a mechanical realization of the Central Limit Theorem (first proved for binomial trials by Abraham de Moivre in 1733 and generalized by Pierre-Simon Laplace in 1810): whenever a measurement is perturbed by a large number of small, independent random disturbances—lathe vibrations, air currents, thermal electron agitation—their sum converges to the Gaussian Normal Probability Density Function (PDF):

$$f(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right), \qquad \phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2 / 2} \quad \left(\text{where } z = \frac{x - \mu}{\sigma}\right)$$

The center of the distribution sits at the mean $\mu$, while its dispersion is governed by the standard deviation $\sigma$ (the horizontal distance from the peak $\mu$ to the two inflection points $x = \mu \pm \sigma$ where the curvature changes sign). Integrating the area under the density curve from $-\infty$ to $z$ gives the cumulative probability $\Phi(z) = \frac{1}{2} + \frac{1}{\sqrt{2\pi}}\int_0^z e^{-t^2/2}\,dt$, which establishes the Empirical Rule ($68.27\%\text{–}95.45\%\text{–}99.73\%$) for the fraction of observations falling within $\pm 1\sigma$, $\pm 2\sigma$, and $\pm 3\sigma$ of the mean.

### Bessel's $n - 1$ Correction and Degrees of Freedom

When a sample of $n$ parts is drawn from a production line, or $n$ sensor readings $x_1, x_2, \dots, x_n$ are recorded, entering each reading into Register $X$ (or a coordinate pair $(y_k, x_k)$ into Registers $Y$ and $X$) and pressing `{{key:Σ+}}` (with `{{key:Σ-}}` available to retract any mistyped reading) updates the SC-32's statistical accumulators. Opening the `{{key:x̄,ȳ}}` menu (`{{key:↱}}` + `{{key:yˣ}}`) returns the sample mean $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$ on softkey `{{key:x̄}}` (and, when each value $x_k$ in $X$ is paired with a weight $w_k$ in $Y$, the weighted mean $\bar{x}_w = \frac{\sum w_k x_k}{\sum w_k}$ on softkey `{{key:x̄w}}`).

Opening the `{{key:s,σ}}` menu (`{{key:↱}}` + `{{key:1/x}}`) to quantify the dispersion of those $n$ numbers around their mean places two standard deviation softkeys side by side: sample standard deviation `{{key:sx}}` (which divides the sum of squared deviations by $n - 1$) and population standard deviation `{{key:σx}}` (which divides by $n$):

$$\sigma_x = \sqrt{\frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n}}, \qquad s_x = \sqrt{\frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n - 1}} = \sqrt{\frac{\Sigma x^2 - \frac{(\Sigma x)^2}{n}}{n - 1}}$$

Gauss's colleague, the astronomer Friedrich Wilhelm Bessel, demonstrated that dividing by $n - 1$ rather than $n$ is required when estimating the variance of an underlying population from a finite sample of size $n$.

Consider first the limiting case of a single observation: when a single shaft ($n = 1$) is pulled from a lathe and its diameter is measured as $x_1 = 25.02\text{ mm}$, the sample average $\bar{x}$ of that single reading is $25.02\text{ mm}$, and the deviation of the point from its own mean is identically zero ($x_1 - \bar{x} = 0$). A single observation provides zero information about process spread, and Bessel's denominator $\frac{0}{1 - 1} = \frac{0}{0}$ reflects this indeterminacy directly (raising `STAT ERROR` if `{{key:sx}}` is pressed at $n = 1$).

For any sample of $n$ points drawn from a population whose *true* center is $\mu$, the same algebraic mechanism applies. Because the true population mean $\mu$ is unknown, squared deviations must be measured around the sample's own average $\bar{x}$. By Gauss's least-squares theorem, the sample mean $\bar{x}$ is the unique value that minimizes the sum of squared deviations $\sum(x_i - c)^2$. Specifically, for any sample:

$$\sum_{i=1}^n (x_i - \bar{x})^2 = \sum_{i=1}^n (x_i - \mu)^2 - n(\bar{x} - \mu)^2 \le \sum_{i=1}^n (x_i - \mu)^2$$

Because the sample average $\bar{x}$ lies at the center of mass of the $n$ sampled points, those sample points always cluster closer to their own sample mean $\bar{x}$ than to the true population center $\mu$ by an expected squared amount of $\sigma^2$, so the expectation of $\sum(x_i - \bar{x})^2$ equals $(n - 1)\sigma^2$. Equivalently, because the $n$ deviations $(x_1 - \bar{x}), \dots, (x_n - \bar{x})$ must sum to zero:

$$\sum_{i=1}^n (x_i - \bar{x}) = 0$$

only $n - 1$ of the deviations are independent ($n - 1$ degrees of freedom); once the first $n - 1$ deviations are specified, the final deviation is fixed. Dividing by $n - 1$ (Bessel's Correction) removes that downward bias.

In manufacturing and laboratory metrology, `{{key:x̄}}` and `{{key:sx}}` govern process capability indices, control charts, and the standard error of the mean. When a CNC lathe machines bearing shafts to a tolerance window $[\text{LSL}, \text{USL}]$, the Six Sigma potential capability $C_p = \frac{\text{USL} - \text{LSL}}{6 s_x}$ measures how many times the natural $6s_x$ distribution span fits inside the specification limits, while the off-center capability index $C_{pk} = \min\!\left(\frac{\text{USL} - \bar{x}}{3s_x}, \frac{\bar{x} - \text{LSL}}{3s_x}\right)$ detects when tool wear shifts the sample mean $\bar{x}$ toward the upper or lower limit.

In May 1924 at Bell Telephone Laboratories, physicist Walter A. Shewhart established statistical process control by proving that adjusting a machine after every random fluctuation ("tampering") doubles the output variance; plotting subgroup averages against $\pm 3\sigma_{\bar{x}}$ control limits $\text{UCL}, \text{LCL} = \bar{\bar{X}} \pm A_2 \bar{R}$ separates stationary random noise from assignable physical faults. Likewise, when astronomers and metrologists average $n = 36$ repeated readings, independent positive and negative errors partially cancel and reduce the standard deviation of the sample average—the Standard Error of the Mean—by the square root of the sample size:

$$\text{SE} = \frac{s_x}{\sqrt{n}}$$

Averaging $n = 36$ readings reduces random uncertainty to $1/\sqrt{36} = 1/6\text{th}$ of a single reading's noise.

---

## Regression to the Mean, Least-Squares Lines & Linearized Curves

Twelve years after building his Quincunx, Francis Galton identified a second statistical phenomenon while analyzing the heights of $930$ adult children and their $205$ pairs of parents in 1886 (*"Regression towards Mediocrity in Hereditary Stature"*). Galton plotted average parent height on the horizontal $x$-axis and adult child height on the vertical $y$-axis, and fitted a straight line through the cloud of points.

Parents who were four inches taller than the population average had tall children, but on average their children were only about *two and a half inches* taller than the mean. Conversely, parents who were four inches shorter than average had children who were taller than their parents and closer to the center of the population. Whenever two variables are imperfectly correlated, extreme observations in $x$ are accompanied on average by less extreme observations in $y$, closer to the population center $(\bar{x}, \bar{y})$. Galton named this phenomenon "regression toward the mean," and fitting a line or curve to noisy data has been termed regression ever since.

{{blocks:sc32_concept_gauss_least_squares|Gauss's method of least squares minimizing squared vertical residuals and the Gaussian normal probability distribution.}}

### Streaming Regression Across Six Statistical Accumulators

Fitting Gauss's least-squares straight line $\hat{y} = m x + b$ through $n$ noisy data pairs $(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)$ also determines Karl Pearson's 1895 Correlation Coefficient $r \in [-1, +1]$, which measures how closely the data cluster along the line: $r = +1$ indicates an exact positive linear relation, $r = -1$ an exact negative linear relation, and $r = 0$ zero linear correlation, while $r^2$ gives the fraction of variance in $y$ explained by $x$. A pocket instrument evaluates all of these quantities across hundreds of points without storing an expanding array of coordinate pairs.

Minimizing the sum of squared vertical errors $\sum_{k=1}^n (y_k - (m x_k + b))^2$ by setting its partial derivatives with respect to $m$ and $b$ to zero compresses the entire dataset into six sufficient statistics {{cite:gauss1809}}:

$$\text{Slope } m = \frac{n \Sigma xy - \Sigma x \, \Sigma y}{n \Sigma x^2 - (\Sigma x)^2}, \qquad \text{Intercept } b = \bar{y} - m \bar{x} = \frac{\Sigma y - m \Sigma x}{n}$$

$$\text{Pearson Correlation } r = \frac{n \Sigma xy - \Sigma x \, \Sigma y}{\sqrt{\left[ n \Sigma x^2 - (\Sigma x)^2 \right] \left[ n \Sigma y^2 - (\Sigma y)^2 \right]}}$$

In those three formulas, the individual data points $(x_k, y_k)$ do not appear separately. The means, standard deviations, least-squares slope $m$, intercept $b$, and correlation $r$ are determined entirely by six running totals, all six of which can be recalled at any moment on the SC-32 through the `{{key:SUMS}}` menu (`{{key:↱}}` + `{{key:Σ+}}`, with softkeys `{{key:Σx}}`, `{{key:Σy}}`, `{{key:Σx²}}`, `{{key:Σy²}}`, `{{key:Σxy}}`, and `{{key:n}}`) {{cite:hp15c1982,hp32sii1991}}:

$$\Sigma x = \sum x_k, \quad \Sigma y = \sum y_k, \quad \Sigma x^2 = \sum x_k^2, \quad \Sigma y^2 = \sum y_k^2, \quad \Sigma xy = \sum x_k y_k, \quad \text{and } n$$

Across $4$ points or $4,000$ points, updating those six registers on each `{{key:Σ+}}` observation retains the exact least-squares geometry of the dataset. If a mistyped entry or electromagnetic spike corrupts a data pair $(x_k, y_k)$, keying that pair into $Y$ and $X$ and pressing `{{key:Σ-}}` subtracts that single observation from the six running sums ($\Sigma x \leftarrow \Sigma x - x_k,\; \Sigma xy \leftarrow \Sigma xy - x_k y_k,\; n \leftarrow n - 1$) without disturbing the remaining readings.

Opening the `{{key:L.R.}}` (Linear Regression) menu (Right Shift `{{key:↱}}` above `{{key:LN}}`) exposes softkeys `{{key:ŷ}}`, `{{key:x̂}}`, `{{key:r}}`, `{{key:m}}`, and `{{key:b}}` for two-way calibration around $\hat{y} = mx + b$. Once a sensor is calibrated across reference pressures or temperatures, `{{key:ŷ}}` forecasts $\hat{y} = mx_0 + b$ at a known stimulus $x_0$, while `{{key:x̂}}` inverts the line $\hat{x} = (y_0 - b)/m$ to recover the unknown physical stimulus from a measured voltage $y_0$.

Because the least-squares line pivots through $(\bar{x}, \bar{y})$ and carries uncertainty in both height and slope, the pointwise Student-$t$ confidence interval (and Working-Hotelling hyperbolic envelope) for the *mean regression line* $E(y \mid x_0)$ flares outward away from the centroid proportional to $s_e\sqrt{\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{\Sigma(x_i - \bar{x})^2}}$, with its minimum width at $x_0 = \bar{x}$. By contrast, the prediction band for a *single future measurement* adds $+1$ inside the radical, $\sqrt{1 + \frac{1}{n} + \dots}$, to account for the variance of an individual observation around the line.

When two variables rise monotonically together along a nonlinear curve—or are measured on an ordinal $1, 2, \dots, n$ ranking scale (such as Mohs scratch hardness versus wear lifetime across ceramic coatings) where linear correlation $r$ is distorted—replacing the raw measurements with their integer ranks and computing the rank differences $d_i = \text{rank}(x_i) - \text{rank}(y_i)$ reduces Pearson's formula to Charles Spearman's 1904 rank correlation:

$$r_s = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}$$

### Bending Curves into Straight Lines: Moore's Law, Barometric Altitude & Wind Turbines

When the physical law governing a dataset is an exponential curve, a power law, or a saturation hyperbola rather than a straight line, the SC-32's RPN stack linearizes the coordinates directly before accumulation. Applying `{{key:LN}}` or `{{key:1/x}}` to the $y$ or $x$ coordinates on the stack *before* pressing `{{key:Σ+}}` maps the nonlinear curve onto a straight line so the transformed parameters can be read from `{{key:m}}` and `{{key:b}}`:

| Physical Model | Governing Equation | Coordinate Transformation | Linearized Straight Line | How Parameters Are Recovered |
| :--- | :--- | :--- | :--- | :--- |
| **Linear** | $y = m x + b$ | $(x, y)$ unchanged | $y = m x + b$ | Slope $= m$, Intercept $= b$ |
| **Exponential** | $y = a e^{b x}$ | $(x,\; \ln y)$ [Semi-Log] | $\ln y = b x + \ln a$ | Rate $b = m$, Initial $a = e^{\text{Intercept}}$ |
| **Power Law** | $y = a x^b$ | $(\ln x,\; \ln y)$ [Log-Log] | $\ln y = b \ln x + \ln a$ | Exponent $b = m$, Scale $a = e^{\text{Intercept}}$ |
| **Logarithmic** | $y = a + b \ln x$ | $(\ln x,\; y)$ | $y = b \ln x + a$ | Scale $b = m$, Offset $a = \text{Intercept}$ |
| **Reciprocal** | $\frac{1}{y} = b x + a$ | $(x,\; 1/y)$ | $\frac{1}{y} = b x + a$ | Slope $= b$, Intercept $= a$ |
| **Hyperbolic** | $y = \frac{x}{a + b x}$ | $(1/x,\; 1/y)$ [Double-Reciprocal] | $\frac{1}{y} = a\left(\frac{1}{x}\right) + b$ | Slope $= a$, Ceiling $1/b$ |

Three coordinate transformations—semi-logarithmic, log-log, and double-reciprocal—linearize common physical laws across science and engineering. Under the semi-logarithmic transformation ($\ln y$ versus $x$), plotting the natural logarithm of the response against an untransformed horizontal variable straightens exponential growth and decay. In 1965, Fairchild Semiconductor co-founder Gordon Moore {{cite:moore1965}} plotted the logarithm of the transistor count $\ln N(t)$ of integrated circuits against the calendar year $t$ and observed the linear trend $\ln N(t) = \ln N_0 + r(t - t_0)$, corresponding to a doubling period $T_{\text{double}} = \frac{\ln 2}{r} \approx 2\text{ years}$ known as Moore's Law.

By Halley and Laplace's barometric formula, atmospheric pressure $P(h) = P_0 e^{-h/H}$ decays exponentially with altitude $h$ (scale height $H \approx 8.4\text{ km}$), so taking `{{key:LN}}` of pressure before pressing `{{key:Σ+}}` converts $\ln P(h) = \ln P_0 - \frac{1}{H}h$ into a straight line of slope `{{key:m}}` $= -1/H$. Similarly, in nuclear medicine, logging $\ln A(t)$ of Technetium-99m ($^{99\text{m}}\text{Tc}$) gamma-ray activity across time $t$ converts Ernest Rutherford and Frederick Soddy's decay law $A(t) = A_0 e^{-\lambda t}$ into a straight line of slope $m = -\lambda$, from which the half-life follows as $t_{1/2} = \frac{\ln 2}{\lambda}$.

Under the log-log transformation ($\ln y$ versus $\ln x$), power laws become linear. Doubling the wind speed $v$ multiplies a wind turbine's electrical output eightfold ($2^3 = 8$) because the mass of air crossing the rotor disk per second grows linearly with wind speed ($\dot{m} = \rho A v$) while the kinetic energy per unit mass grows with the square of wind speed ($\frac{1}{2}v^2$), so total wind power scales with the cube of wind speed: $P(v) = \frac{1}{2}\dot{m}v^2 = k v^3$. Taking `{{key:LN}}` of both power $P$ and wind speed $v$ before pressing `{{key:Σ+}}` transforms $P = k v^m$ into $\ln P = m \ln v + \ln k$, where `{{key:m}}` extracts the power-law exponent $m$ and `{{key:b}} {{key:eˣ}}` recovers the aerodynamic scale factor $k = e^b$.

Under the double-reciprocal transformation ($1/y$ versus $1/x$), saturating hyperbolas become linear. When biochemists Leonor Michaelis and Maud Menten (1913) measured the rate at which a catalytic enzyme processes substrate $[S]$, they found a rectangular hyperbola $v = \frac{V_{\max}[S]}{K_m + [S]}$ that approaches a ceiling $V_{\max}$ as the active sites saturate. In 1934, Hans Lineweaver and Dean Burk showed that taking the reciprocal (`{{key:1/x}}`) of both reaction velocity $v$ and substrate concentration $[S]$ before `{{key:Σ+}}` linearizes the hyperbola:

$$\frac{1}{v} = \left(\frac{K_m}{V_{\max}}\right)\frac{1}{[S]} + \frac{1}{V_{\max}}$$

where the reciprocal of the intercept (`{{key:b}} {{key:1/x}}`) yields the maximum turnover rate $V_{\max} = 1/b$ and multiplying by `{{key:m}}` yields the half-saturation constant $K_m = m \cdot V_{\max}$.

---

## Student's t-Distribution and Small-Sample Inference

Around 1906, at St. James's Gate in Dublin, Arthur Guinness & Son, then the largest brewery in the world, confronted a fundamental question of small-sample inference. Guinness had recruited Oxford-educated chemist William Sealy Gosset as Head Experimental Brewer to apply quantitative quality control to the production of stout.

Gosset needed to determine whether a new variety of Irish barley yielded significantly more malt extract than an existing variety, or whether hop soft-resin content differed between two crop seasons. Classical nineteenth-century statistics, as developed by Carl Friedrich Gauss and Karl Pearson, assumed hundreds or thousands of observations ($n \to \infty$), so that the sample standard deviation $s$ could be substituted for the exact population standard deviation $\sigma$ without introducing additional uncertainty.

In industrial brewing—as in aerospace metallurgy or clinical trials—waiting years to cultivate and malt a thousand test plots of barley was impractical; Gosset typically worked with small experimental batches of $n = 4$ to $10$. When $n$ is small, the sample standard deviation $s$ in the denominator of the standardized score fluctuates randomly from batch to batch alongside the sample mean $\bar{x}$ in the numerator, which causes extreme ratios to occur more frequently than Gauss's normal curve predicts and produces a distribution with heavier tails.

Gosset derived the exact small-sample probability distribution of the ratio $t = \frac{\bar{x} - \mu}{s / \sqrt{n}}$. Because Guinness policy prohibited employees from publishing under their own names to protect trade secrets, Gosset obtained permission from the brewery board to publish his 1908 paper, *"The Probable Error of a Mean,"* in Karl Pearson's journal *Biometrika* under the pseudonym *"Student"* {{cite:student1908}}.

To compare the means of two small experimental groups of sizes $n_1$ and $n_2$, such as tensile test coupons of two candidate aerospace titanium alloys, Student's Two-Sample $t$-Test pools the two sample variances weighted by their Bessel degrees of freedom ($n_1 - 1$ and $n_2 - 1$, with $df = n_1 + n_2 - 2$ total degrees of freedom):

$$s_p = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}, \qquad t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$$

When $|t|$ exceeds the critical Student's $t$-threshold for $df = n_1 + n_2 - 2$, the difference between the sample means is statistically significant relative to the pooled small-sample variance.

### Counting Rare Arrivals & Aging Machines: Poisson (1837) and Weibull (1951)

Two additional probability distributions model discrete random arrivals and the fatigue survival of physical hardware. Whenever independent discrete events occur randomly at a steady average rate $\lambda$ per unit of time or space—photons from a distant nebula striking a detector pixel, cosmic-ray muons registering in a counter, or data packets arriving at an optical network router—the probability of observing $k$ arrivals in a single interval follows the distribution derived in 1837 by French mathematician Siméon Denis Poisson. The Poisson Probability Mass Function (PMF) evaluates on the stack using `{{key:yˣ}}`, `{{key:eˣ}}`, and the factorial key `{{key:x!}}` via Left Shift `{{key:↰}}` above `{{key:1/x}}` or inside the `{{key:PROB}}` menu:

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

In 1898, Russian economist Ladislaus Bortkiewicz demonstrated the empirical accuracy of Poisson's law on rare events by fitting it to twenty years of Prussian cavalry records.

Whereas radioactive decay and Poisson packet arrivals are *memoryless*—a carbon-14 atom that has survived for five thousand years is no more likely to decay in the next minute than a newly formed atom—mechanical ball bearings, jet-engine turbine blades, and stressed steel shafts accumulate microscopic fatigue cracks as operating hours $t$ increase. In 1951, Swedish engineer Waloddi Weibull {{cite:weibull1951}} introduced a survival distribution that encompasses all three regimes of the engineering bathtub reliability curve through a characteristic life scale $\eta$ (the age at which $e^{-1} \approx 36.79\%$ of units survive) and a dimensionless shape parameter $\beta$:

$$R(t) = \exp\left[ -\left(\frac{t}{\eta}\right)^\beta \right]$$

When $\beta < 1$ (the infant mortality or burn-in regime), defective components fail early and the hazard rate *decreases* over time as weak units are eliminated. When $\beta = 1$ (memoryless random failures), the law reduces to the pure exponential $R(t) = e^{-t/\eta}$, where failures occur from random external shocks at a constant hazard rate $1/\eta$. When $\beta > 1$ (aging and fatigue wear-out), the failure hazard accelerates with age as bearings spall and metals fatigue. Taking the double natural logarithm $\ln[-\ln R(t)] = \beta \ln t - \beta \ln \eta$ via `{{key:LN}} {{key:+/-}} {{key:LN}}` transforms Weibull's survival curve into a straight line on the regression stack.

### The Centroid Fulcrum, Lever-Arm Outliers & Residual Audits

Three geometric properties of a least-squares line govern outlier sensitivity, residual variance, and uncertainty propagation. Rewriting $b = \bar{y} - m\bar{x}$ as $\bar{y} = m\bar{x} + b$ shows that every least-squares regression line passes through the centroid $(\bar{x}, \bar{y})$ of the data cloud. Mechanically, the regression line behaves like a rigid beam pivoted on a fulcrum at $(\bar{x}, \bar{y})$ and linked by vertical springs to each data point $(x_i, y_i)$. Because moment equals lever arm times force, any observation near the horizontal extremes where $|x_i - \bar{x}|$ is large acts with a long lever arm and exerts disproportionate leverage on the slope. A single transcription error at an extreme $x_i$ can perturb the slope `{{key:m}}` and correlation `{{key:r}}` substantially, as illustrated by Francis Anscombe's 1973 Quartet, whereas retracting that point via `{{key:Σ-}}` restores the unperturbed fit.

Once $\hat{y} = mx + b$ is fitted through $n$ data pairs, the vertical scatter remaining around the line is quantified by the residual standard error $s_e = \sqrt{\frac{1}{n-2}\sum(y_i - \hat{y}_i)^2}$, where the denominator $n - 2$ reflects the two degrees of freedom consumed in estimating both slope $m$ and intercept $b$. By the orthogonality of the least-squares projection, the total variance decomposes into the explained regression fraction $r^2$ and the unexplained residual fraction $(1 - r^2)$, so $s_e$ can be evaluated directly from the accumulated statistics without re-scanning the $n$ points:

$$\sum_{i=1}^n (y_i - \hat{y}_i)^2 = (n - 1) s_y^2 \left(1 - r^2\right) \implies s_e = s_y \sqrt{\frac{n - 1}{n - 2}\left(1 - r^2\right)}$$

Recalling `{{key:sy}}`, `{{key:r}}`, and `{{key:n}}` from the statistical menus determines the exact residual standard error $s_e$ around the regression line.

Finally, when two independent random variables $X$ and $Y$ with standard uncertainties $\sigma_X$ and $\sigma_Y$ are combined linearly into $Z = aX \pm bY$, their variances add in quadrature ($\sigma_Z = \sqrt{a^2\sigma_X^2 + b^2\sigma_Y^2}$), which corresponds directly to the Pythagorean norm (`{{key:▸θ,r}}` on the stack). For a general differentiable function $Z = g(X, Y)$, Gauss's Law of Error Propagation combines the partial derivatives with the covariance $\operatorname{Cov}(X, Y) = r s_x s_y$:

$$\sigma_Z^2 \approx \left(\frac{\partial g}{\partial X}\right)^2 \sigma_X^2 + \left(\frac{\partial g}{\partial Y}\right)^2 \sigma_Y^2 + 2\left(\frac{\partial g}{\partial X}\right)\left(\frac{\partial g}{\partial Y}\right) r\,\sigma_X \sigma_Y$$

---

## Statistical Accumulators, Probability Distributions & Regression

Because the six first- and second-order moments ($\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$) form a complete set of sufficient statistics for Gaussian means, Bessel variances, and linear least squares, the SC-32 connects the live four-register stack (`X, Y, Z, T`) directly to six 64-bit hardware accumulators (indirect registers `R28` through `R33`).

When logging a bivariate observation $(x_k, y_k)$ after clearing prior runs with `{{key:CLΣ}}`, keying `y_k {{key:ENTER}} x_k {{key:Σ+}}` lifts the vertical response $y_k$ into Register $Y$ and leaves the horizontal predictor $x_k$ in Register $X$, which aligns the display registers $(Y, X)$ with the $(y, x)$ axes of the coordinate plane. For univariate samples $x_k$, keying `x_k {{key:Σ+}}` accumulates along $X$; for weighted averages, placing the weight $w_k$ in Register $Y$ and the reading $x_k$ in Register $X$ accumulates $\sum w_k x_k$ in $\Sigma xy$ and $\sum w_k$ in $\Sigma y$.

Because $(y_k, x_k)$ sit live in the lower two stack registers prior to accumulation, applying `{{key:LN}}` or `{{key:1/x}}` before pressing `{{key:Σ+}}` linearizes exponential, power-law, and Michaelis–Menten hyperbolic models in place before the four Right-Shift statistical menus query the six sums.

{{res:sc32_normal_pdf:screenshot|Standard Normal PDF f(1.0) = exp(−0.5)/√(2π) = 0.241970724519 on the SC-32.}}

### The 6 Statistical Accumulators, Outlier Retraction & Softkey Menus

On the SC-32, pressing `{{key:Σ+}}` commits the coordinate pair $(Y = y_k,\; X = x_k)$ into six non-volatile hardware registers while displaying the updated sample count $n$ in Register $X$ (and preserving `LASTX`):

| Accumulator | Indirect Register | Mathematical Meaning | Primary Statistical Role |
| :---: | :---: | :--- | :--- |
| **$\Sigma x$** | `R29` (`LFU0`) | $\sum x_i$ | Sample mean $\bar{x}$, regression slope $m$ |
| **$\Sigma y$** | `R30` (`LFU1`) | $\sum y_i$ | Sample mean $\bar{y}$, regression intercept $b$, total weight in $\bar{x}_w$ |
| **$\Sigma x^2$** | `R31` (`LFU2`) | $\sum x_i^2$ | $x$-variance and standard deviations ($s_x, \sigma_x$) |
| **$\Sigma y^2$** | `R32` (`LFU3`) | $\sum y_i^2$ | $y$-variance and standard deviations ($s_y, \sigma_y$) |
| **$\Sigma xy$** | `R33` (`LFU4`) | $\sum (x_i \cdot y_i)$ | Bivariate covariance, Pearson $r$, and weighted sum $\sum w_i x_i$ |
| **$n$** | `R28` (`LFU5`) | Sample count | Normalization and Bessel degrees of freedom ($n - 1$) |

Accessed via Right Shift `{{key:↱}}` across the top scientific row, the four statistical menus map onto the six LFU dynamic softkeys (`{{key:LFU0}}` through `{{key:LFU5}}`):

| Sub-Menu | Primary Invocation & Key Position | `{{key:LFU0}}` | `{{key:LFU1}}` | `{{key:LFU2}}` | `{{key:LFU3}}` | `{{key:LFU4}}` | `{{key:LFU5}}` |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Sums Menu** | `{{key:SUMS}}` (above `{{key:Σ+}}`) | `{{key:Σx}}` | `{{key:Σy}}` | `{{key:Σx²}}` | `{{key:Σy²}}` | `{{key:Σxy}}` | `{{key:n}}` |
| **2. Means Menu** | `{{key:x̄,ȳ}}` (above `{{key:yˣ}}`) | `{{key:x̄}}` | `{{key:ȳ}}` | `{{key:x̄w}}` | — | — | — |
| **3. Std Dev Menu** | `{{key:s,σ}}` (above `{{key:1/x}}`) | `{{key:sx}}` | `{{key:sy}}` | `{{key:σx}}` | `{{key:σy}}` | — | — |
| **4. Regression Menu** | `{{key:L.R.}}` (above `{{key:LN}}`) | `{{key:ŷ}}` | `{{key:x̂}}` | `{{key:r}}` | `{{key:m}}` | `{{key:b}}` | — |

If a keystroke slip on the sixth data pair $(x = 15, y = 3.5)$ transposes $y$ into $(x = 15, y = 5.3)$ when the sample count is $n = 6$, `{{key:Σ-}}` excises the erroneous point and splices in the corrected reading without disturbing the first five points:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `5.3 {{key:ENTER}} 15` | $0.0000$ | $0.0000$ | $5.3000$ | $15.0000$ | Key erroneous pair $(x=15, y=5.3)$ |
| `{{key:Σ-}}` | $0.0000$ | $0.0000$ | $5.3000$ | **$5.0000$** | Subtract from accumulators; $n$ decrements to 5 |
| `3.5 {{key:ENTER}} 15` | $0.0000$ | $5.3000$ | $3.5000$ | $15.0000$ | Key corrected pair $(x=15, y=3.5)$ |
| `{{key:Σ+}}` | $0.0000$ | $5.3000$ | $3.5000$ | **$6.0000$** | Accumulate corrected pair; $n$ restored to 6 |

---

### Weighted Sensor Fusion, Six Sigma Capability ($C_p, C_{pk}$), Control Limits & Standard Error

Applying these quality-control and metrological indices ($\bar{x}_w$, $C_p$, $C_{pk}$, Shewhart limits, and $\text{SE} = s/\sqrt{n}$) to shop-floor and observatory measurements shows how the six accumulators feed subsequent stack arithmetic:

For inverse-variance weighted sensor fusion ($\bar{x}_w = \Sigma xy / \Sigma y$), when three observatory instruments measure an astrometric parallax angle—$x_1 = 10\text{ mas}$, $x_2 = 25\text{ mas}$, and $x_3 = 45\text{ mas}$—with inverse-variance precision weights $w_i = 1/\sigma_i^2$ equal to $w_1 = 40$, $w_2 = 60$, and $w_3 = 20\text{ mas}^{-2}$, loading each weight $w_i$ into Register $Y$ and measurement $x_i$ into Register $X$ before pressing `{{key:Σ+}}` accumulates $\Sigma(w_i x_i)$ inside `R33` ($\Sigma xy$) and $\Sigma w_i$ inside `R30` ($\Sigma y$). Opening `{{key:x̄,ȳ}}` and tapping `{{key:x̄w}}` (`{{key:LFU2}}`) computes the minimum-variance fused estimate $\bar{x}_w = \frac{\Sigma xy}{\Sigma y} = \frac{2800}{120} = 23.3333\text{ mas}$, while `{{key:SUMS}}` $\to$ `{{key:Σy}}` (`{{key:LFU1}}`) recalls the combined precision weight $120.0\text{ mas}^{-2}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `{{key:CLΣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Clear all 6 statistical accumulators |
| `40 {{key:ENTER}} 10 {{key:Σ+}}` | $0.0000$ | $0.0000$ | $40.0000$ | $1.0000$ | Sensor 1 logged ($w_1=40, x_1=10;\; n=1$) |
| `60 {{key:ENTER}} 25 {{key:Σ+}}` | $0.0000$ | $40.0000$ | $60.0000$ | $2.0000$ | Sensor 2 logged ($w_2=60, x_2=25;\; n=2$) |
| `20 {{key:ENTER}} 45 {{key:Σ+}}` | $40.0000$ | $60.0000$ | $20.0000$ | $3.0000$ | Sensor 3 logged ($w_3=20, x_3=45;\; n=3$) |
| `{{key:x̄w}}` | $40.0000$ | $60.0000$ | $20.0000$ | **$23.3333$** | Via `{{key:x̄,ȳ}}` $\to$ `{{key:x̄w}}`: inverse-variance weighted mean $\bar{x}_w$ (mas) |
| `{{key:Σy}}` | $60.0000$ | $20.0000$ | $23.3333$ | **$120.0000$** | Via `{{key:SUMS}}` $\to$ `{{key:Σy}}`: total precision weight $\Sigma y = \sum w_i$ ($\text{mas}^{-2}$) |

To evaluate the Six Sigma capability indices $C_p$ and $C_{pk}$ across $n = 10$ CNC-machined bearing shafts specified at $25.00 \pm 0.10\text{ mm}$ ($\text{LSL} = 24.90\text{ mm}$, $\text{USL} = 25.10\text{ mm}$), keying each diameter into Register $X$ and pressing `{{key:Σ+}}` yields sample mean $\bar{x} = \mathbf{25.0300\text{ mm}}$ and Bessel sample spread $s_x = \mathbf{0.018257\text{ mm}}$. Dividing the $0.20\text{ mm}$ tolerance width by $6s_x$ via `{{res:sc32_09_statistics_curve_fitting_seq_03:keys}}` yields potential capability $C_p =$ `{{res:sc32_09_statistics_curve_fitting_seq_03:value}}`, while comparing $\bar{x}$ against $\text{USL} = 25.10\text{ mm}$ via `{{res:sc32_09_statistics_curve_fitting_seq_04:keys}}` yields $C_{pk} =$ `{{res:sc32_09_statistics_curve_fitting_seq_04:value}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `25.02 {{key:Σ+}} 25.04 {{key:Σ+}} 25.01 {{key:Σ+}} 25.03 {{key:Σ+}} 25.05 {{key:Σ+}} 25.02 {{key:Σ+}} 25.00 {{key:Σ+}} 25.04 {{key:Σ+}} 25.03 {{key:Σ+}} 25.06 {{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | Accumulate 10 shaft diameter samples |
| `{{key:x̄,ȳ}} {{key:x̄}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$25.0300$** | Sample mean diameter $\bar{x}$ (mm) |
| `{{key:s,σ}} {{key:sx}}` | $0.0000$ | $0.0000$ | $25.0300$ | **$0.018257$** | Sample standard deviation $s_x$ (mm) |
| `{{res:sc32_09_statistics_curve_fitting_seq_03:keys}}` | $25.0300$ | $25.0300$ | $0.0183$ | **`{{res:sc32_09_statistics_curve_fitting_seq_03:value}}`** | Process capability $C_p = \frac{\text{USL}-\text{LSL}}{6s_x}$ |
| `{{res:sc32_09_statistics_curve_fitting_seq_04:keys}}` | $0.0183$ | $0.0183$ | $1.8258$ | **`{{res:sc32_09_statistics_curve_fitting_seq_04:value}}`** | Process capability index $C_{pk} = \frac{\text{USL}-\bar{x}}{3s_x}$ |

The pair $(C_p = 1.8257,\; C_{pk} = 1.2780)$ provides a direct shop-floor diagnostic: because $C_p > 1.33$, the lathe spindle itself is mechanically tight enough for Six Sigma production, but because $C_{pk} = 1.2780 < 1.33$, thermal tool growth has shifted the process center $+0.030\text{ mm}$ toward the upper limit, which indicates a $-0.030\text{ mm}$ tool-offset correction rather than a spindle rebuild.

* **Shift-Invariance Speed & Numerical Hygiene ($s_{x - c} = s_x$):** Translating an entire dataset by a constant datum $c$ shifts the mean ($\overline{x - c} = \bar{x} - c$) without changing the distances between points ($s_{x - c} = s_x$). You can therefore subtract the $25.00\text{ mm}$ nominal diameter mentally and accumulate only the hundredths of a millimeter with `{{key:Σ+}}`: `2 Σ+ 4 Σ+ 1 Σ+ 3 Σ+ 5 Σ+ 2 Σ+ 0 Σ+ 4 Σ+ 3 Σ+ 6 Σ+`. That shortcut cuts keystrokes in half—returning $\bar{d} = 3.0000 \implies \bar{x} = 25.0300\text{ mm}$ and $s_d = 1.8257 \implies s_x = 0.018257\text{ mm}$—while shielding the one-pass variance sum $\Sigma x^2 - (\Sigma x)^2/n$ from catastrophic cancellation whenever raw readings cluster tightly around a large baseline offset.

Similarly, evaluating Walter Shewhart's $\pm 3\sigma_{\bar{x}}$ control limits $\text{UCL}, \text{LCL} = \bar{\bar{X}} \pm A_2\bar{R}$ around a centerline of $\bar{\bar{X}} = 50.00\text{ mm}$ with subgroup range $\bar{R} = 0.40\text{ mm}$ and $n = 5$ subgroup factor $A_2 = 0.577$ uses `LASTX` to compute both guardrails from a single centerline entry:

$$\text{UCL} = \bar{\bar{X}} + A_2\bar{R}, \qquad \text{LCL} = \bar{\bar{X}} - A_2\bar{R}$$

The sequence `{{res:sc32_09_statistics_curve_fitting_seq_18:keys}}` forms the control half-width $A_2\bar{R} = 0.2308\text{ mm}$, and adding `50.00 {{key:+}}` places the Upper Control Limit at $\text{UCL} = \mathbf{50.2308\text{ mm}}$.

Subtracting that same half-width from the centerline via `{{res:sc32_09_statistics_curve_fitting_seq_19:keys}}` sets the Lower Control Limit at $\text{LCL} = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_19:value}}\text{ mm}}$.

Once $A_2\bar{R} = 0.2308$ sits in Register $X$, keying `50.00 {{key:x⇄y}} {{key:-}}` computes $\text{LCL} = \mathbf{49.7692\text{ mm}}$ while automatically capturing $0.2308$ in `LASTX`; following at once with `{{key:LASTX}} 2 {{key:×}} {{key:+}}` adds $2(A_2\bar{R})$ to step straight across to $\text{UCL} = \mathbf{50.2308\text{ mm}}$ while typing `50.00` only once.

Applying the $\sqrt{n}$ averaging law ($\text{SE} = s/\sqrt{n}$) across $n = 36$ aluminum-alloy tensile yield specimens ($\bar{x} = 120.5\text{ MPa}, s = 8.4\text{ MPa}$) follows the same pattern. Dividing $s = 8.4\text{ MPa}$ by $\sqrt{36} = 6$ with `{{res:sc32_09_statistics_curve_fitting_seq_20:keys}}` reduces the Standard Error of the Mean to $\text{SE} = \mathbf{{{res:sc32_09_statistics_curve_fitting_seq_20:value}}\text{ MPa}}$, and scaling by the two-sided $95\%$ normal multiplier `1.960 {{key:×}}` gives the half-width margin $E = \mathbf{2.7440\text{ MPa}}$.

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
* **Forward & Inverse Calibration (`ŷ` and `x̂`) & Two-Point Table Interpolation:** Keying `25 {{key:L.R.}} {{key:ŷ}}` forecasts $\mathbf{3.1125000000\text{ V}}$ while placing $r = 0.99956481$ in Register $Y$, and keying `4.00 {{key:L.R.}} {{key:x̂}}` inverts the calibration curve to recover $\mathbf{32.128514\text{ kPa}}$. *(Corvallis Two-Point Table Interpolator: Whenever you need to interpolate between two adjacent rows $(x_1, y_1)$ and $(x_2, y_2)$ of a steam or atmosphere lookup table, log both points after `{{key:CLΣ}}` as `y1 ENTER x1 Σ+ y2 ENTER x2 Σ+`. Because two points determine an exact secant line with $r = \pm 1.000000$, querying `ŷ` at $x_0$ performs forward linear interpolation and querying `x̂` at $y_0$ performs inverse linear interpolation without manual difference quotients—and applying `{{key:LN}}` before `Σ+` performs log-linear interpolation across exponential tables.)*
* **Confidence vs. Prediction Margins at the Centroid ($x_0 = \bar{x} = 25\text{ kPa}$):** With residual standard error $s_e = 0.058095\text{ V}$ and two-sided Student-$t$ multiplier $t_{0.025, 2} = 4.303$, the $(x_0 - \bar{x})^2$ tilt term of the Working-Hotelling hyperbolic envelope vanishes at the centroid waist $x_0 = \bar{x}$. Evaluating $E = t_{0.025,2} \cdot s_e / \sqrt{4}$ via `4.303 {{key:ENTER}} 0.058095 {{key:×}} 4 {{key:1/x}} {{key:√x}} {{key:×}}` gives the mean-line confidence margin $E = \mathbf{0.1250\text{ V}}$ ($3.1125 \pm 0.1250\text{ V}$), whereas scaling by $\sqrt{1 + 1/4}$ via `4 {{key:1/x}} 1 {{key:+}} {{key:√x}} 0.058095 {{key:×}} 4.303 {{key:×}}` gives the single-observation prediction margin $E_{\text{pred}} = \mathbf{0.2795\text{ V}}$ ($3.1125 \pm 0.2795\text{ V}$).

In analytical and environmental chemistry, inverse regression calibration (`{{key:L.R.}}` $\to$ `{{key:x̂}}`) is the standard tool for *Beer–Lambert UV-Vis spectrophotometry* ($A = -\log_{10}(I/I_0) = \varepsilon b C + A_{\text{blank}}$). When a water-quality chemist calibrates a $b = 1.00\text{ cm}$ cuvette at $\lambda = 510\text{ nm}$ across four iron(II)–phenanthroline standards—$C_1 = 1.00\text{ mg/L}$ ($A_1 = 0.198$), $C_2 = 2.00\text{ mg/L}$ ($A_2 = 0.395$), $C_3 = 3.00\text{ mg/L}$ ($A_3 = 0.594$), and $C_4 = 4.00\text{ mg/L}$ ($A_4 = 0.791$)—logging each $(A_i, C_i)$ pair with `{{key:Σ+}}` and querying `{{key:r}}` and `{{key:m}}` confirms Beer's law linearity ($r = \mathbf{0.999997}$, absorptivity slope $m = \mathbf{0.197700\text{ L/mg}}$, blank offset $b = \mathbf{0.000250}$). Keying an unknown groundwater sample's absorbance $A_{\text{unk}} = 0.465$ and pressing `{{key:x̂}}` (`{{key:L.R.}}` $\to$ `{{key:LFU1}}`) inverts the calibration line in place to yield $\hat{C} = \mathbf{2.350784\text{ mg/L}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0.000000$ | $0.000000$ | $0.000000$ | $0.000000$ | Clear all 6 statistical accumulators |
| `0.198 {{key:ENTER}} 1 {{key:Σ+}}` | $0.000000$ | $0.000000$ | $0.198000$ | $1.000000$ | Standard 1 ($C_1=1.0\text{ mg/L}, A_1=0.198;\; n=1$) |
| `0.395 {{key:ENTER}} 2 {{key:Σ+}}` | $0.000000$ | $0.198000$ | $0.395000$ | $2.000000$ | Standard 2 ($C_2=2.0\text{ mg/L}, A_2=0.395;\; n=2$) |
| `0.594 {{key:ENTER}} 3 {{key:Σ+}}` | $0.198000$ | $0.395000$ | $0.594000$ | $3.000000$ | Standard 3 ($C_3=3.0\text{ mg/L}, A_3=0.594;\; n=3$) |
| `0.791 {{key:ENTER}} 4 {{key:Σ+}}` | $0.395000$ | $0.594000$ | $0.791000$ | $4.000000$ | Standard 4 ($C_4=4.0\text{ mg/L}, A_4=0.791;\; n=4$) |
| `{{key:r}}` | $0.395000$ | $0.594000$ | $0.791000$ | $0.999997$ | Via `{{key:L.R.}}` $\to$ `{{key:r}}`: Beer-Lambert correlation |
| `{{key:m}}` | $0.594000$ | $0.791000$ | $0.999997$ | $0.197700$ | Via `{{key:L.R.}}` $\to$ `{{key:m}}`: slope $\varepsilon b$ ($\text{L/mg}$) |
| `0.465 {{key:x̂}}` | $0.791000$ | $0.999997$ | $0.197700$ | **$2.350784$** | Via `{{key:L.R.}}` $\to$ `{{key:x̂}}`: unknown concentration ($\text{mg/L}$) |

Evaluating Charles Spearman's rank correlation $r_s = 1 - \frac{6\Sigma d_i^2}{n(n^2-1)}$ across five ceramic coatings ranked on Mohs scratch hardness versus wear lifetime with rank discrepancies $d = (1, -1, 2, -1, -1)$ runs on Registers $X$ and $Y$ while Registers $Z$ and $T$ remain at zero. Here the squared rank differences sum to $\Sigma d_i^2 = 1 + 1 + 4 + 1 + 1 = 8.0$—one-fifth of the antipodal reversal sum $\frac{n(n^2 - 1)}{3} = 40.0$ ($r_s = -1.0$) and well below the uncorrelated expectation $\frac{n(n^2 - 1)}{6} = 20.0$ ($r_s = 0.0$). On the stack, form the numerator $6\Sigma d_i^2 = 48.0000$ in Register $Y$ and the denominator $n(n^2 - 1) = 5(24) = 120.0000$ in Register $X$, divide to isolate the discordance penalty $48 / 120 = 0.4000$, and subtract from unity via `{{res:sc32_09_statistics_curve_fitting_seq_05:keys}}` $\longrightarrow$ $\mathbf{0.6000}$ ($r_s = +0.6000$).

---

### Gaussian Normal Density, Cumulative Probability, Student's t-Test, Poisson & Weibull

Continuous and discrete probability laws—Gauss's normal distribution, Student's two-sample $t$-statistic, Poisson's arrival law, and Weibull's reliability model—evaluate directly on the stack:

Evaluating the Gaussian Normal PDF $f(x; \mu, \sigma)$ at $x = 115$ ($\mu = 100, \sigma = 15$), $f(115; 100, 15) = \frac{1}{15\sqrt{2\pi}}\exp\!\left(-\frac{(115-100)^2}{2(15)^2}\right)$, one standard deviation above the mean ($z = +1.0$) unfolds in two stack stages. First, square the deviation $(115 - 100)^2 = 225.0$ via `{{res:sc32_09_statistics_curve_fitting_seq_11:keys}}`, form the variance denominator $2\sigma^2 = 450.0$ in Register $X$ with `{{res:sc32_09_statistics_curve_fitting_seq_12:keys}}`, and evaluate `{{key:÷}} {{key:+/-}} {{key:eˣ}}` to leave the bell factor $e^{-0.5} = 0.60653066$ on the stack. Second, construct the normalization constant $\sigma\sqrt{2\pi} = 37.59942412$ via `{{res:sc32_09_statistics_curve_fitting_seq_13:keys}}` while $e^{-0.5}$ rides in Register $Y$, and press `{{key:÷}}` to obtain $\mathbf{0.0161313817}$:

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

*(Multiplying $f(115; 100, 15) = 0.0161313817$ by $\sigma = 15$ recovers the standard normal height $\phi(1.0) = \frac{1}{\sqrt{2\pi}}e^{-0.5} = \mathbf{0.2419707245}$ shown on the transflective LCD screenshot.)*

To evaluate the cumulative normal integral $\Phi(1.0) = 0.5 + \frac{1}{\sqrt{2\pi}}\int_0^{1.0} e^{-t^2/2}\,dt$ via Romberg quadrature (`{{key:∫}}`), recall that the left half of the symmetric bell curve from $-\infty$ to $0$ encloses an area of $0.50000000$. Finding $\Phi(z)$ for any $z > 0$ therefore requires only integrating the finite half-bell $\int_0^z e^{-t^2/2}\,dt$ with `X {{key:x²}} 2 {{key:÷}} {{key:+/-}} {{key:eˣ}}` active in `{{key:EQN}}`, dividing by $\sqrt{2\pi}$, and adding $0.5$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `0 {{key:ENTER}} 1.0` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $1.00000000$ | Push integration limits $a=0, b=1.0$ |
| `{{key:∫}}` | $0.00000000$ | $0.00000000$ | $1.15 \times 10^{-12}$ | $0.85562439$ | Select variable `X`: Romberg quadrature $\int_0^1 e^{-t^2/2}\,dt$ |
| `2 {{key:π}} {{key:×}} {{key:√x}} {{key:÷}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $0.34134475$ | Divide by $\sqrt{2\pi}$; area from mean to $Z=1.0$ |
| `0.5 {{key:+}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | **$0.84134475$** | Cumulative probability $\Phi(1.0)$ ($84.13\%$) |

Doubling the central slice $2 \times 0.34134475 = \mathbf{0.68268949}$ confirms the $\pm 1\sigma$ Empirical Rule ($68.27\%$).

Applying Gosset's Student Two-Sample $t$-Test ($df = n_1 + n_2 - 2 = 16$) to Titanium Alloy A ($n_1 = 8$ coupons, $\bar{x}_1 = 450.0\text{ MPa}$, $s_1 = 12.5\text{ MPa}$) against Alloy B ($n_2 = 10$ coupons, $\bar{x}_2 = 468.0\text{ MPa}$, $s_2 = 14.0\text{ MPa}$), the pooled variance $s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$ and $t$-statistic evaluate across Registers $X$ and $Y$ while $Z$ and $T$ remain at zero.

Adding Alloy A's sum of squares $(n_1 - 1)s_1^2 = 7(12.5^2) = 1,093.7500\text{ MPa}^2$ to Alloy B's $(n_2 - 1)s_2^2 = 9(14^2) = 1,764.0000\text{ MPa}^2$ forms $2,857.7500\text{ MPa}^2$, and dividing by $df = 16$ before taking `{{key:√x}}` extracts the pooled standard deviation $s_p = \mathbf{13.364482\text{ MPa}}$ (weighted $9:7$ toward the larger $10\text{-coupon}$ batch). Scaling $s_p$ by $\sqrt{\frac{1}{8} + \frac{1}{10}}$ via `{{key:1/x}}` and `√x` gives the standard error $\text{SE} = \mathbf{6.339330\text{ MPa}}$, and forming $\bar{x}_1 - \bar{x}_2 = -18.0000\text{ MPa}$ before `{{key:x⇄y}} {{key:÷}}` yields Student's $t = \mathbf{-2.839422}$—surpassing the two-sided $95\%$ threshold $t_{0.025, 16} = 2.120$.

Evaluating Poisson's rare-event PMF $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$ for $k = 6$ arrivals when an optical router receives $\lambda = 4.5\text{ packets/ms}$ on average forms the arrival-rate power $\lambda^k = 4.5^6 = 8,303.765625$ in Register $Y$ and the exponential survival factor $e^{-4.5} \approx 0.01110900$ in Register $X$, multiplies to collapse the numerator $\lambda^k e^{-\lambda} = 92.246538$, and divides by $k! = 6! = 720$ without touching Registers $Z$ or $T$ via `{{res:sc32_09_statistics_curve_fitting_seq_06:keys}}` $\longrightarrow$ `{{res:sc32_09_statistics_curve_fitting_seq_06:value}}` ($12.81\%$).

Similarly, Waloddi Weibull's survival law $R(t) = \exp\!\left[-(t/\eta)^\beta\right]$ for a spindle bearing at $t = 3,000\text{ hr}$ ($\eta = 5,000\text{ hr}$, wear-out exponent $\beta = 1.8 > 1$) normalizes service time ($t/\eta = 0.6000$), raises that ratio to $(0.6000)^{1.8} = 0.398660$, and evaluates $\exp(-0.398660)$ in place on Register $X$ via `{{res:sc32_09_statistics_curve_fitting_seq_09:keys}}` $\longrightarrow$ $\mathbf{0.6712}$ ($67.12\%$ survival, or $32.88\%$ cumulative failure risk).

---

### Linearized Curve Fitting: Log-Log Power Laws & Double-Reciprocal Kinetics

Applying the log-log transformation ($\ln P = m\ln v + \ln k$) to fit the wind turbine cubic power law $P = kv^m$ across four wind-tunnel test points $(4, 16), (6, 54), (8, 128), (10, 250)$ transforms both output power $P$ and wind speed $v$ via `{{key:LN}}` right on the stack before tapping `{{key:Σ+}}`. Because unary keys like `{{key:LN}}` and `{{key:1/x}}` terminate digit entry and arm automatic stack lift, `16 {{key:LN}} 4 {{key:LN}} {{key:Σ+}}` needs no `{{key:ENTER}}` between `16 {{key:LN}}` and `4`—typing `4` lifts $\ln(16)$ into Register $Y$ automatically, saving an `{{key:ENTER}}` tap on every data pair. Querying `{{key:L.R.}} {{key:m}}` confirms the cubic exponent $m = \mathbf{3.000000}$, `{{key:b}} {{key:eˣ}}` recovers $k = e^b = \mathbf{0.250000}$, and forecasting output at $12\text{ m/s}$ with `{{res:sc32_09_statistics_curve_fitting_seq_14:keys}}` delivers `{{res:sc32_09_statistics_curve_fitting_seq_14:value}}` kW:

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

Applying the double-reciprocal Lineweaver-Burk transformation ($\frac{1}{v} = \frac{K_m}{V_{\max}}\frac{1}{[S]} + \frac{1}{V_{\max}}$) to a Michaelis-Menten enzyme assay similarly taps `{{key:1/x}}` on each reaction velocity $v_k$ and substrate concentration $[S]_k$ before pressing `{{key:Σ+}}`. Streaming the four double-reciprocal pairs via `{{res:sc32_09_statistics_curve_fitting_seq_17:keys}}` determines the maximum turnover ceiling $V_{\max} = 1/b = \mathbf{0.6346\,\mu\text{M/min}}$ and the half-saturation Michaelis constant $K_m = m \cdot V_{\max} =$ `{{res:sc32_09_statistics_curve_fitting_seq_17:value}}` mM:

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

Finally, the semi-log transformation ($\ln A(t) = \ln A_0 - \lambda t$) applies `{{key:LN}}` solely to the vertical $y$-coordinate before pressing `{{key:Σ+}}`. For four Technetium-99m ($^{99\text{m}}\text{Tc}$) gamma-ray calibration readings—$1000\text{ MBq}$ at $t = 0\text{ hr}$, $794\text{ MBq}$ at $2\text{ hr}$, $630\text{ MBq}$ at $4\text{ hr}$, and $500\text{ MBq}$ at $6\text{ hr}$—clear with `{{key:CLΣ}}`, then stream `1000 LN 0 Σ+`, `794 LN 2 Σ+`, `630 LN 4 Σ+`, and `500 LN 6 Σ+`; tapping `{{key:L.R.}} {{key:m}} {{key:+/-}}` reads the decay constant $\lambda = \mathbf{0.11552\text{ hr}^{-1}}$, dividing $\ln 2$ by $\lambda$ yields the clinical half-life $t_{1/2} = \frac{\ln 2}{\lambda} = \mathbf{6.000\text{ hours}}$, and `{{key:b}} {{key:eˣ}}` recovers $A_0 = \mathbf{1000.1\text{ MBq}}$ (the same semi-log procedure weather-balloon radiosondes use on $\ln P_k$ vs. altitude $h_k$ to calibrate sea-level pressure $P_0 = e^b$ and scale height $H = -1/m$).

In physical chemistry kinetics, pairing `{{key:LN}}` on the vertical rate constant $k_i$ with `{{key:1/x}}` on the horizontal absolute temperature $T_i$ (`k_i {{key:LN}} T_i {{key:1/x}} {{key:Σ+}}`) linearizes Svante Arrhenius's activation law $k = A\exp(-E_a / RT)$ into $\ln k = -\frac{E_a}{R}\left(\frac{1}{T}\right) + \ln A$ across multiple temperature runs without a single `{{key:ENTER}}` tap. Querying `{{key:L.R.}} {{key:m}} {{key:+/-}}` and multiplying by the molar gas constant $R = 8.31446\text{ J/(mol}\cdot\text{K)}$ extracts the least-squares activation barrier $E_a = -m R$ in $\text{J/mol}$, while `{{key:b}} {{key:eˣ}}` recovers the pre-exponential collision frequency factor $A = e^b$ (and the identical $\ln P_i$ vs. $1/T_i$ pairing extracts the molar enthalpy of vaporization $\Delta H_{\text{vap}} = -m R$ from multi-point Clausius–Clapeyron vapor-pressure data).

For fatigue life testing across failure times $t_k$ with empirical survival fractions $R_k$, applying the double-logarithm transform $R_k$ (`LN +/- LN`) into Register $Y$ and $t_k$ (`LN`) into Register $X$ before `{{key:Σ+}}` fits Waloddi Weibull's line $\ln[-\ln R(t)] = \beta \ln t - \beta \ln \eta$, where `{{key:m}}` reads the shape modulus $\beta$ and $\eta = \exp(-b/\beta)$ recovers the characteristic life. Whenever you query Bessel's sample standard deviation `{{key:sx}}` or `{{key:sy}}` with fewer than two observations ($n \le 1$), query `{{key:x̄}}` with $n = 0$, or query regression slope or correlation when all $x$-values are identical ($n\Sigma x^2 - (\Sigma x)^2 = 0$, a vertical line), the SC-32 raises `STAT ERROR` (Code 04), which clears non-destructively via `{{key:C}}` without disturbing the six statistical registers.
