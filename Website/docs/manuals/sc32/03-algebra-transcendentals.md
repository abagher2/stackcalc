---
title: "Chapter 3: Logarithms, Power Laws & Exponential Scaling | Thinking in the Stack (SC-32)"
description: "John Napier's logarithms, Weber-Fechner perception, Kleiber's biological scaling, the 5-domain harmonic operator, Euler's base e, Carbon-14 dating, Newton's cooling law, and Lanczos Gamma factorials on the StackCalc SC-32."
---

# Chapter 3: Logarithms, Power Laws & Exponential Scaling

## John Napier's Logarithms and the Weber-Fechner Law

### Inside Merchiston Castle: Turning Products into Sums

At Merchiston Castle near Edinburgh in the opening years of the seventeenth century, Scottish mathematician John Napier (1550–1617) sought a method to relieve the arithmetic bottleneck of observational astronomy.

Across Europe, astronomers had just inherited the richest body of observational data in history. On the island of Hven in Denmark, Tycho Brahe had spent thirty years measuring the nightly positions of Mars and the stars to within one arcminute. In Prague, Tycho's assistant Johannes Kepler was working to establish that the planets orbit the Sun in ellipses rather than circles. Yet every time Kepler tested an elliptical orbit against Tycho's observations, he had to multiply and divide eight-digit trigonometric chords by hand across nearly a thousand folio pages of dense arithmetic. A single carried-digit error could invalidate months of calculation.

Napier set out to construct a mapping in mathematics that converts multiplication into addition, division into subtraction, and square or cube root extraction into division by $2$ or $3$. Aligning a row of integer exponents above the corresponding powers of two and powers of ten reveals the underlying isomorphism:

| Step Sequence | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Power of $2$ ($2^n$)** | $1$ | $2$ | $4$ | $8$ | $16$ | $32$ | $64$ | $128$ |
| **Power of $10$ ($10^n$)** | $1$ | $10$ | $100$ | $1{,}000$ | $10{,}000$ | $100{,}000$ | $10^6$ | $10^7$ |

To multiply $8 \times 16$ in the middle row, compare the exponents directly above them: $8$ corresponds to exponent $3$ ($2^3$), and $16$ corresponds to exponent $4$ ($2^4$). Adding their exponents ($3 + 4 = 7$) and reading the entry below step $7$ gives $128$ ($8 \times 16 = 128$). That correspondence holds because an exponent counts how many times the base is multiplied by itself:

$$b^x \cdot b^y = b^{x + y}, \qquad \frac{b^x}{b^y} = b^{x - y}, \qquad \left(b^x\right)^n = b^{n x}$$

Napier spent twenty years interpolating the continuous values between the integers through a kinematic model of two points moving simultaneously along straight lines. The first point (the logarithm track) travels along an infinite straight line at a uniform velocity $v_0$, covering equal *arithmetic* increments of distance in equal intervals of time ($0, \Delta x, 2\Delta x, 3\Delta x, \dots$). Simultaneously, the second point (the number track) starts at distance $L$ from a terminal mark and moves toward it at a speed proportional to the distance remaining, covering equal *geometric* ratios in equal intervals of time ($L, L r, L r^2, L r^3, \dots$).

By pairing the arithmetic position of the first point with the geometric position of the second point at every instant, Napier established a continuous correspondence between addition and multiplication. In 1614, three years before his death, he published *Mirifici Logarithmorum Canonis Descriptio* (*Description of the Wonderful Rule of Logarithms*) {{cite:napier1614}}. There he coined the word *logarithm* from the Greek *logos* ("ratio") and *arithmos* ("number") to signify the number that counts ratios. A year later, London geometry professor Henry Briggs traveled to Edinburgh and worked with Napier to normalize logarithms to base $10$, where $\log_{10} 1 = 0$, $\log_{10} 10 = 1$, $\log_{10} 100 = 2$, and $\log_{10} 1000 = 3$.

For any two positive numbers $a$ and $b$, Napier and Briggs's logarithmic function satisfies three algebraic identities:

$$\log(a \cdot b) = \log a + \log b, \qquad \log\left(\frac{a}{b}\right) = \log a - \log b, \qquad \log\left(y^x\right) = x \log y$$

Rather than spending twenty minutes multiplying two eight-digit numbers by hand, an astronomer could look up their two logarithms in Briggs's table, add them in seconds, and read the antilogarithm matching that sum. Extracting a cube root ($\sqrt[3]{y} = y^{1/3}$), which previously required hours of digit-by-digit trial division, reduced to looking up $\log y$ and dividing by $3$. When Kepler received Napier's treatise in 1617, he dedicated his *Ephemerides* to Napier and used logarithmic tables to establish his Third Law of Planetary Motion ($T^2 = a^3$). Two centuries later, Pierre-Simon Laplace summarized the historical impact of the invention: *"Logarithms, by shortening the labors, doubled the life of the astronomer."*

{{blocks:sc32_concept_napier_log_scale|John Napier's logarithmic bridge between geometric multiplication and arithmetic addition, paired with natural exponential decay across characteristic time constants.}}

How does a pocket instrument find any logarithm to 16 digits without storing Henry Briggs's thousand-page book in memory? Following the classical algorithm of William J. Cody and William Waite {{cite:cody1980}}, the SC-32 strips off powers of two—instant in binary floating-point—splitting any positive number $x = m \cdot 2^k$ into its normalized binary significand $m \in [\frac{1}{\sqrt{2}}, \sqrt{2})$ near $1$ and its exact integer binary exponent $k$:

$$\ln\left(m \cdot 2^k\right) = \ln(m) + k \ln(2)$$

Because $m$ is confined to a narrow interval around $1$, the natural logarithm $\ln(m)$ can be expanded in terms of the rapidly converging rational transformation $z = \frac{m - 1}{m + 1}$:

$$\ln(m) = 2\left(z + \frac{z^3}{3} + \frac{z^5}{5} + \frac{z^7}{7} + \dots\right), \qquad \text{where } z = \frac{m - 1}{m + 1}$$

which converges to 16 decimal digits in a small number of odd powers.

### The Weber-Fechner Law of Logarithmic Perception

Logarithms extend well beyond seventeenth-century astronomical tables. In the nineteenth century, German physiologists Ernst Heinrich Weber and Gustav Fechner established a quantitative law of psychophysics: human sensory systems perceive physical stimulus intensity on a logarithmic scale. In a dark room illuminated by a single candle, introducing a second candle doubles the photon flux and produces an unmistakable increase in perceived brightness. In a hall already illuminated by $100$ candles, introducing a $101\text{st}$ candle changes the stimulus by only one percent, and the increment is imperceptible. Sensory receptors respond not to the absolute difference ($+1\text{ candle}$), but to the relative ratio ($\frac{\text{new intensity}}{\text{old intensity}}$). Each tenfold multiplication of physical energy produces one equal perceptual step.

Four standard measurement scales in acoustics, chemistry, seismology, and astrophysics apply this principle directly through the base-10 logarithm key `{{key:LOG}}` and its inverse `{{key:10ˣ}}`, each acting in place on Register $X$ once the underlying physical ratio has been formed across Registers $Y$ and $X$. In acoustics, the faintest pressure fluctuation detectable by the human eardrum has a root-mean-square amplitude of $p_0 = 20\,\mu\text{Pa}$ ($2.0 \times 10^{-5}\text{ Pa}$), whereas a nearby jet engine reaches $20\text{ Pa}$. Between those extremes, acoustic pressure spans a million-fold range ($10^6:1$) and acoustic intensity $I \propto p^2$ spans twelve orders of magnitude ($10^{12}:1$). Along the inner ear, the tapered basilar membrane of the mammalian cochlea maps those twelve orders of magnitude onto the $0\text{ to }120\text{ dB}$ Sound Pressure Level scale:

$$L_p = 20 \log_{10}\left(\frac{p_{\text{rms}}}{p_0}\right)\text{ dB SPL}$$

Evaluating this expression from the inside out places the measured sound pressure $p_{\text{rms}}$ in Register $Y$ and the reference threshold $p_0 = 2.0 \times 10^{-5}\text{ Pa}$ in Register $X$ so `{{key:÷}}` forms the dimensionless pressure ratio in Register $X$. Pressing `{{key:LOG}}` transforms that ratio in place into base-10 orders of magnitude (Bels), and multiplying by $20$ converts the result into decibels (`dB SPL`). That same $60\text{ dB}$ million-fold energy decay threshold defines the Sabine reverberation time $T_{60}$ in architectural acoustics.

In aqueous and clinical chemistry, the molar concentration of hydronium ions $[\text{H}_3\text{O}^+]$ spans fourteen orders of magnitude from strong mineral acid ($10^0\text{ M}$) to concentrated alkali ($10^{-14}\text{ M}$). In 1909, Danish biochemist Søren Peder Lauritz Sørensen at the Carlsberg Laboratory compressed those exponents onto a linear scale by defining $\text{pH} = -\log_{10} a_{\text{H}_3\text{O}^+} \approx -\log_{10}[\text{H}_3\text{O}^+]$, inverted in two keystrokes on Register $X$ via `{{key:+/-}} {{key:10ˣ}}` ($[\text{H}_3\text{O}^+] = 10^{-\text{pH}}$). When a laboratory buffer or human arterial blood plasma equilibrates a weak acid ($[\text{HA}]$ or dissolved $\alpha P_{\text{CO}_2}$) with its conjugate base ($[\text{A}^-]$ or $[\text{HCO}_3^-]$), the *Henderson-Hasselbalch equation* relates the equilibrium $\text{pH}$ to the acid dissociation constant $\text{pK}_a$:

$$\text{pH} = \text{pK}_a + \log_{10}\left(\frac{[\text{A}^-]}{[\text{HA}]}\right)$$

On the stack, dividing the conjugate base concentration in Register $Y$ by the weak acid concentration in Register $X$, pressing `{{key:LOG}}` in place, and adding $\text{pK}_a$ resolves the buffer $\text{pH}$ without intermediate storage.

Two further logarithmic scales govern geophysics and observational astronomy. In 1935, Caltech seismologist Charles F. Richter represented the wide dynamic range of ground motion recorded on Wood-Anderson torsion seismographs by defining local earthquake magnitude as $M_L = \log_{10}(A/A_0)$ (extended to modern Hiroo Kanamori Moment Magnitude $M_w$): each integer step up the magnitude scale corresponds to a tenfold increase in ground-motion amplitude and a $10^{1.5} = 10\sqrt{10} \approx \mathbf{31.62\times}$ increase in released elastic wave energy.

Similarly, around 130 BC the Greek astronomer Hipparchus classified naked-eye stars from First Magnitude (brightest) to Sixth Magnitude (faintest). In 1856, English astronomer Norman Robert Pogson formalized Hipparchus's catalog through the logarithmic relation $m_1 - m_2 = -2.5\log_{10}(F_1/F_2)$, establishing that a 5-magnitude span corresponds to a $100\times$ ($10^2$) ratio in photon flux and that each single magnitude step represents a flux ratio of $100^{1/5} = 10^{0.4} \approx \mathbf{2.5119\times}$.

---

## Power Laws, Biological Scaling & The Universal Harmonic Operator

Once Napier established that $\log(y^x) = x\log y$, raising any positive real number $y$ to an arbitrary fractional or irrational exponent $x$ followed directly from the composition of the logarithm and exponential:

$$y^x = e^{x \ln y} \qquad \text{and} \qquad \sqrt[x]{y} = y^{1/x}$$

On the SC-32, powers, roots, and reciprocals divide into two operational classes: *in-place unary keys* (`{{key:x²}}`, `{{key:√x}}`, `{{key:1/x}}`) that transform Register $X$ in place without disturbing values held in Registers $Y, Z,$ or $T$, and *two-register dyadic keys* (`{{key:yˣ}}`, `{{key:ˣ√y}}`, `{{key:x∥y}}`) that combine Register $Y$ with Register $X$:

| Mathematical Function | Physical Keycap | Arity | Exact Mathematical Definition | Register Stack Effect |
| :--- | :---: | :---: | :--- | :--- |
| **Square** | `{{key:x²}}` | Unary | $f(x) = x^2$ | $X \leftarrow X^2$ |
| **Square Root** | `{{key:√x}}` | Unary | $f(x) = \sqrt{x}, \quad x \ge 0$ | $X \leftarrow \sqrt{X}$ |
| **Reciprocal** | `{{key:1/x}}` | Unary | $f(x) = 1/x, \quad x \ne 0$ | $X \leftarrow 1/X$ |
| **General Power** | `{{key:yˣ}}` | Dyadic | $f(y, x) = y^x = \exp(x \ln y)$ | $X \leftarrow Y^X$ (Dyadic drop) |
| **Arbitrary Root** | `{{key:ˣ√y}}` | Dyadic | $f(y, x) = \sqrt[x]{y} = y^{1/x}$ | $X \leftarrow Y^{1/X}$ (Dyadic drop) |
| **Parallel Harmonic** | `{{key:x∥y}}` | Dyadic | $f(x, y) = \frac{x \cdot y}{x + y}$ | $X \leftarrow \frac{X \cdot Y}{X + Y}$ (Dyadic drop) |

### Kepler's Planets, Kleiber's Mice and Whales, and Relativistic Muons

Fractional exponents such as $y^{2/3}$, $y^{3/4}$, $y^{1.32}$, and $(1 - \beta^2)^{-1/2}$ govern scaling laws across celestial mechanics, physiology, and special relativity. In 1619, Johannes Kepler established that the square of a planet's orbital period $T$ (in Earth years) equals the cube of its semi-major axis $a$ (in Astronomical Units, where $1\text{ AU}$ is the mean Earth-Sun distance). Sixty-eight years later, Isaac Newton derived $T^2 \propto a^3$ from universal gravitation: equating gravitational attraction $G M_{\odot} m / a^2$ with centripetal force $m v^2 / a = m(2\pi a / T)^2 / a$ yields $T^2 = \frac{4\pi^2}{G M_{\odot}} a^3$. Taking the cube root of both sides expresses $T^2 = a^3$ as a $2/3$ fractional power law:

$$a = \left(T^2\right)^{1/3} = \sqrt[3]{T^2} = T^{2/3}$$

This fractional exponent links the unary and dyadic power keys on the keypad: squaring an orbital period $T$ in place in Register $X$ with the unary key `{{key:x²}}` and extracting the third root with the dyadic key `{{key:ˣ√y}}` (or raising $T$ in Register $Y$ directly to the $2/3$ power in Register $X$ with `{{key:yˣ}}`) converts observed sidereal period directly into heliocentric distance.

A second fractional power law governs comparative physiology. In 1932, Swiss agricultural biologist Max Kleiber plotted basal metabolic rate $B$ (in Watts or kilocalories per day) against body mass $M$ across homeothermic mammals ranging from a $20\text{-gram}$ mouse to a $4,000\text{-kilogram}$ elephant ($200,000\times$ more massive). Rather than scaling linearly with mass ($M^1$) or with Euclidean exterior surface area ($M^{2/3} \approx M^{0.67}$), metabolic rate across organisms from unicellular microbes to cetaceans follows the three-quarters power of mass:

$$B = B_0 M^{3/4} = B_0 M^{0.75}$$

As physicists Geoffrey West, James Brown, and Brian Enquist demonstrated, this $3/4$ exponent emerges because biological vascular and bronchial trees are space-filling fractal networks that minimize hydrodynamic pumping work across three spatial dimensions, introducing an effective fourth scaling dimension ($3 / (3 + 1) = 3/4$). Because basal metabolism scales as $M^{0.75}$, an organism $10,000\times$ heavier ($10^4$) requires only $(10^4)^{0.75} = 10^3 = 1,000\times$ the caloric intake, while its heart rate scales as $M^{-1/4}$ ($10\times$ slower), separating the $800\text{-beat-per-minute}$ pulse of a shrew from the sub-$10\text{-beat-per-minute}$ pulse of a blue whale.

A negative half-integer power law governs relativistic particle kinematics. In Earth's stratosphere, $15\text{ kilometers}$ ($15,000\text{ meters}$) above sea level, primary cosmic rays collide with atmospheric nuclei and produce unstable secondary *muons*. In its rest frame, a muon decays with a mean proper lifetime of $\tau_0 = 2.2\text{ microseconds}$ ($2.2 \times 10^{-6}\text{ s}$). Even for a muon descending at $85\%$ of the speed of light ($v = 0.85c \approx 2.55 \times 10^8\text{ m/s}$), Galilean kinematics predicts a mean propagation distance of less than six hundred meters before decay:

$$d_{\text{classical}} = v \cdot \tau_0 = (2.55 \times 10^8\text{ m/s})(2.2 \times 10^{-6}\text{ s}) \approx \mathbf{560\text{ meters}}$$

Without relativistic time dilation, nearly every stratospheric muon would decay more than $14\text{ kilometers}$ above the surface, yet sea-level scintillation detectors record a steady flux of cosmic-ray muons. Under Albert Einstein's 1905 Special Theory of Relativity, invariance of the Minkowski spacetime interval $c^2 \Delta\tau^2 = c^2 \Delta t^2 - \Delta x^2$ across inertial frames dilates the laboratory lifetime $\Delta t = \gamma \Delta\tau$ according to Hendrik Lorentz's factor $\gamma$:

$$\gamma = \frac{1}{\sqrt{1 - \left(\frac{v}{c}\right)^2}} = \left(1 - \beta^2\right)^{-1/2}$$

Structurally, $\gamma$ evaluates as a pure unary chain from the dimensionless velocity ratio $\beta = v/c$ outward: squaring $\beta$ in place with `{{key:x²}}`, subtracting from $1$ to form the proper-time factor $1 - \beta^2$, extracting the length-contraction factor $\sqrt{1 - \beta^2}$ with `{{key:√x}}`, and inverting with `{{key:1/x}}` yields the laboratory time-dilation factor while automatically preserving the length-contraction ratio $1/\gamma$ inside `{{key:LASTX}}`. At $v = 0.999c$, $\gamma$ exceeds $22$ and enables stratospheric muons to reach sea-level detectors.

These three laws illustrate why the SC-32 separates *in-place unary keys* (`{{key:x²}}`, `{{key:√x}}`, `{{key:1/x}}`) from *two-register dyadic keys* (`{{key:yˣ}}`, `{{key:ˣ√y}}`, `{{key:x∥y}}`). When a power or root acts on a single physical quantity already in Register $X$, a unary key transforms that register without `{{key:ENTER}}` and without disturbing values in the upper registers—whether squaring the speed of light $c$ in Einstein's gravitational redshift $z \approx \frac{GM}{Rc^2}$ for light escaping a white dwarf star, squaring molar volume $V$ in Johannes Diderik van der Waals's equation of state $P = \frac{nRT}{V - nb} - \frac{an^2}{V^2}$, or chaining `{{key:√x}}` and `{{key:1/x}}` to compute the electromagnetic skin depth $\delta = \frac{1}{\sqrt{\pi f \mu \sigma}}$ of alternating current in a copper conductor.

Conversely, whenever an equation pairs a base waiting in Register $Y$ with a general fractional exponent or root index formed in Register $X$—as in polytropic gas compression work ($W = \frac{P_1 V_1}{n - 1}[(V_1/V_2)^{n - 1} - 1]$), Weibull wind-speed distributions, or solar air-mass attenuation ($I = I_0 \cdot 0.7^{(\text{AM}^{0.678})}$)—pressing the dyadic key `{{key:yˣ}}` or `{{key:ˣ√y}}` combines Registers $Y$ and $X$ into $Y^X$ or $\sqrt[X]{Y}$ and drops the upper stack by one level. When a rational power or decimal result needs to be inspected as a reduced fraction $a/b$ or mixed number $n\frac{a}{b}$, toggling fraction display mode (`{{key:FDISP}}`) formats Register $X$ as a best rational convergent via Euclid's continued-fraction / Farey algorithm (or to a fixed denominator $1/c$ for $c \in [2, 4095]$ popped from Register $X$ via `{{key:/c}}`), while retaining all 53 bits of floating-point precision internally.

### The Five-Domain Universal Harmonic Operator (`x∥y`)

Extending the parallel reciprocal law ($\frac{1}{T} = \frac{1}{T_1} + \frac{1}{T_2}$), the SC-32 provides a dedicated primary hardware keycap labeled `{{key:x∥y}}` that evaluates the product-over-sum harmonic combination:

$$x \parallel y = \frac{x \cdot y}{x + y} = \left(\frac{1}{x} + \frac{1}{y}\right)^{-1}$$

in a single keystroke across five distinct domains of physics and engineering:

| Physical Domain | What Combines via $x \parallel y = \frac{x y}{x + y}$ | Why the Reciprocal-Sum Law Appears |
| :--- | :--- | :--- |
| **1. Parallel Electrical Resistors** | $R_{\text{eq}} = R_1 \parallel R_2 = \frac{R_1 R_2}{R_1 + R_2}$ | Both resistors share the same voltage $V$, while their currents ($I_i = V/R_i$) add. |
| **2. Thin Optical Lenses & Mirrors** | $f = d_o \parallel d_i = \frac{d_o d_i}{d_o + d_i}$ | Light rays from object distance $d_o$ bend by constant optical power $1/f$ to focus at image distance $d_i$ ($\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$). |
| **3. Capacitors Wired in Series** | $C_{\text{eq}} = C_1 \parallel C_2 = \frac{C_1 C_2}{C_1 + C_2}$ | Series capacitor plates trap the same charge $Q$, while their voltage drops ($V_i = Q/C_i$) add. |
| **4. Mechanical Springs in Series** | $k_{\text{eq}} = k_1 \parallel k_2 = \frac{k_1 k_2}{k_1 + k_2}$ | Two springs hooked end-to-end feel the same tension force $F$, while their stretches ($\Delta x_i = F/k_i$) add. |
| **5. Round-Trip Average Speed** | $v_{\text{avg}} = 2(v_1 \parallel v_2) = \frac{2 v_1 v_2}{v_1 + v_2}$ | Driving $D\text{ miles}$ uphill at $v_1 = 30\text{ mph}$ and $D\text{ miles}$ downhill at $v_2 = 60\text{ mph}$ adds *times* ($D/v_1 + D/v_2$) to give $2(30 \parallel 60) = \mathbf{40\text{ mph}}$ (not $45\text{ mph}$). |

All five systems reduce to $x \parallel y$ because each pairs a shared intensive variable with an additive extensive variable. In a *parallel resistor network*, Kirchhoff's current law requires that the total current $I_{\text{total}} = V / R_{\text{eq}}$ entering a node equal the sum of the branch currents $I_1 + I_2 = V/R_1 + V/R_2$; dividing out the common node voltage $V$ gives $\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2}$. In *series capacitors*, the dual relationship holds: equal displacement charge $\pm Q$ is induced on each capacitor in the chain while the potential drops add ($V_{\text{total}} = V_1 + V_2 \implies \frac{Q}{C_{\text{eq}}} = \frac{Q}{C_1} + \frac{Q}{C_2}$).

In *series Hookean springs*, both springs carry the same axial tension $F$ while their elongations add ($\Delta x_{\text{total}} = \Delta x_1 + \Delta x_2 \implies \frac{F}{k_{\text{eq}}} = \frac{F}{k_1} + \frac{F}{k_2}$), so the combined assembly exhibits a lower effective stiffness than either individual spring. Because $x \parallel y$ is both *commutative* ($x \parallel y = y \parallel x$) and *associative* ($(x \parallel y) \parallel z = x \parallel (y \parallel z)$), three, four, or more parallel branches fold sequentially on the stack with `{{key:x∥y}}` in the same manner as `{{key:+}}` or `{{key:×}}`.

---

## Leonhard Euler's Natural Base e, Carbon-14 & Cooling Coffee

Whereas Henry Briggs's base-10 logarithm (`{{key:LOG}}`) scales by powers of ten, continuous differential equations are governed by the natural base studied by Jacob Bernoulli in 1683 during his analysis of compound interest and designated $e$ by Leonhard Euler in 1727:

$$e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = 1 + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + \frac{1}{4!} + \dots \approx \mathbf{2.718281828459}$$

Bernoulli identified this limit by analyzing an idealized bank paying $100\%$ nominal annual interest on a principal of $\$1.00$ across progressively finer compounding intervals. Compounded once at year's end ($n = 1$), the balance reaches $(1 + 1)^1 = \$2.00$; compounded semiannually ($50\%$ every six months, $n = 2$), it reaches $(1 + \frac{1}{2})^2 = \$2.25$; compounded quarterly ($25\%$ every three months, $n = 4$), it reaches $(1 + \frac{1}{4})^4 \approx \$2.4414$. Increasing the frequency to monthly compounding ($n = 12$) yields $(1 + \frac{1}{12})^{12} \approx \$2.6130$, daily compounding ($n = 365$) yields $(1 + \frac{1}{365})^{365} \approx \$2.7146$, and compounding every second ($n = 31,536,000$)—where growth occurs continuously in direct proportion to the instantaneous balance—drives the terminal value to Euler's constant $e \approx \$2.718281828459\dots$

In mathematical analysis, $e^x$ (`{{key:eˣ}}`) and its inverse $\ln x$ (`{{key:LN}}`) form the *natural* exponential and logarithm because term-by-term differentiation of the factorial power series maps each term $\frac{x^k}{k!}$ to $\frac{k x^{k-1}}{k!} = \frac{x^{k-1}}{(k-1)!}$, reproducing the series unchanged:

$$\frac{d}{dx}\left(1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \dots\right) = 0 + 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots = e^x$$

The function $e^x$ is the unique eigenfunction of the differential operator $\frac{d}{dx}$ with unit eigenvalue: in everyday terms, $e^x$ is the only curve in nature whose steepness (growth rate) at every moment equals its current height. Whenever a physical quantity grows or decays at a rate proportional to its instantaneous magnitude ($\frac{dN}{dt} = \pm \lambda N$), the solution is an exponential in base $e$.

### Willard Libby's Carbon-14 Radiometric Dating

In 1949 at the University of Chicago, physical chemist Willard F. Libby demonstrated that natural logarithmic decay inversion (`{{key:LN}}`) could determine the age of organic archaeological specimens, a contribution recognized with the 1960 Nobel Prize in Chemistry.

Radiocarbon dating relies on an equilibrium between stratospheric production and biological uptake. High in the stratosphere, cosmic-ray neutrons continuously bombard nitrogen-14 nuclei ($^{14}\text{N} + n \to {}^{14}\text{C} + p$) and convert them into radioactive *carbon-14 ($^{14}\text{C}$)* at a nearly constant global rate. Those $^{14}\text{C}$ atoms oxidize into carbon dioxide ($^{14}\text{CO}_2$), mix throughout the atmosphere and oceans, and enter the biosphere through photosynthesis.

So long as a plant or animal remains alive and exchanges carbon with its environment, the ratio of radioactive $^{14}\text{C}$ to stable carbon ($^{12}\text{C}$) in its tissues remains locked to the atmospheric baseline ($N_0 \approx 1\text{ part per trillion}$). Once the organism dies—when a tree is felled for timber or flax is cut for linen—metabolic carbon exchange ceases, and the trapped $^{14}\text{C}$ nuclei undergo beta decay back into nitrogen-14 with a physical Cambridge half-life of $t_{1/2} = 5,730\text{ years}$ (refining Libby's original $5,568\text{-year}$ convention prior to tree-ring calibration):

$$N(t) = N_0 \left(\frac{1}{2}\right)^{t / t_{1/2}} = N_0 e^{-\lambda t}, \qquad \text{where } \lambda = \frac{\ln 2}{t_{1/2}} = \frac{\ln 2}{5730} \approx 1.20968 \times 10^{-4}\text{ yr}^{-1}$$

Solving Libby's exponential decay law for elapsed time $t$ isolates the surviving isotope fraction $N(t)/N_0$ inside the natural logarithm:

$$t = -\frac{\ln\left(N(t)/N_0\right)}{\lambda} = -\frac{\ln\left(N(t)/N_0\right) \times t_{1/2}}{\ln 2}$$

Because $\ln(N(t)/N_0)$ measures the number of elapsed natural $e$-folding lifetimes ($1/\lambda \approx 8,267\text{ years}$), dividing by $\ln 2 \approx 0.69315$ converts those natural decay units into elapsed half-lives, and multiplying by $t_{1/2} = 5,730\text{ years}$ yields the age of the specimen. For Precambrian igneous rocks billions of years old, in which all original carbon-14 has decayed away, geochronologists apply the same `{{key:LN}}` inversion to Potassium-40 ($t_{1/2} = 1.248 \times 10^9\text{ yr}$) decaying into radiogenic Argon-40 trapped within crystalline mineral lattices, while the discrete compound-interest counterpart $t = \frac{\ln 2}{\ln(1+r)}$ gives the exact doubling period of an accumulating reserve.

### Newton's Law of Cooling and Thermal Relaxation

First-order exponential relaxation also governs macroscopic heat transfer. In 1701, Isaac Newton placed a heated iron block in a steady draft and observed that the rate $\frac{dT}{dt}$ at which a warm body loses heat to its surroundings is proportional to the instantaneous temperature excess $\Delta T(t) = T(t) - T_{\text{room}}$ between the body and the ambient air:

$$\frac{d}{dt}\left(T(t) - T_{\text{room}}\right) = -\frac{1}{\tau}\left(T(t) - T_{\text{room}}\right)$$

When a vessel of liquid at $90^\circ\text{C}$ sits in a $20^\circ\text{C}$ room ($\Delta T_0 = 70^\circ\text{C}$), thermal energy transfers rapidly across the boundary layer; once the liquid has cooled to $35^\circ\text{C}$ ($\Delta T = 15^\circ\text{C}$), the rate of heat loss drops nearly fivefold in proportion to the reduced temperature gradient. Integrating Newton's differential equation yields an exponential relaxation curve characterized by the thermal time constant $\tau$:

$$\Delta T(t) = \Delta T_0 e^{-t/\tau} \implies t = -\tau \ln\left(\frac{\Delta T(t)}{\Delta T_0}\right)$$

The identical first-order differential equation governs an electrical RC network discharging through a resistor ($\tau = R C$), where each elapsed time constant $\tau$ reduces the remaining voltage or temperature excess to $1/e \approx 36.79\%$ of its initial value, and decaying to $10\%$ of the initial disturbance requires $-\ln(0.10) = \ln(10) \approx 2.3026$ time constants.

### The Boltzmann Factor in Atmospheric Pressure and Thermal Radiation

Chemical reaction kinetics, reduced-pressure boiling points, barometric pressure at high altitude, and stellar blackbody radiation all depend on a single statistical-mechanical ratio: the competition between an activation or potential energy barrier ($\Delta E$) and thermal agitation energy ($RT$ or $k_B T$) inside the natural exponential (`{{key:eˣ}}`).

In Svante Arrhenius's 1889 reaction-rate law ($k = A \exp(-E_a / RT)$), in solid-state interstitial lattice diffusion ($D = D_0 \exp(-Q / RT)$), and in the Clausius-Clapeyron phase-equilibrium relation ($\ln(P_2/P_1) = -\frac{\Delta H_{\text{vap}}}{R}(\frac{1}{T_2} - \frac{1}{T_1})$), molecules must surmount an energy threshold to react, hop between lattice sites, or escape from a liquid phase into vapor. On the stack, each Boltzmann factor is evaluated from the exponent outward: first form the dimensionless energy-to-temperature ratio $\Delta E / RT$ (or reciprocal-temperature difference $\frac{1}{T_1} - \frac{1}{T_2}$ via two applications of `{{key:1/x}}` and `{{key:-}}`) in Register $X$, negate via `{{key:+/-}}` for a barrier, press `{{key:eˣ}}` to obtain the Boltzmann probability factor in place, and multiply by the pre-exponential coefficient ($A, D_0,$ or $P_1$).

The same exponential law governs planetary atmospheres. Whereas liquid water is nearly incompressible and exhibits a linear increase in hydrostatic pressure with depth, air is a compressible ideal gas whose density $\rho = \frac{PM}{RT}$ is proportional to local pressure $P$. Substituting $\rho$ into the hydrostatic balance $dP = -\rho g\,dh$ yields the isothermal scale-height equation $\frac{dP}{P} = -\frac{Mg}{RT_0}\,dh$, in which gravitational potential energy $Mgh$ competes against thermal energy $RT_0$ so that barometric pressure $P(h) = P_0 e^{-Mgh/RT_0}$ decays exponentially with altitude $h$ and drops to $60.7\%$ of its sea-level value atop the $4,207\text{-meter}$ summit of Mauna Kea.

In solid-state physics and quantum electrodynamics, the Boltzmann factor appears inside the difference $(e^x - 1)$. Across a forward-biased silicon p-n junction ($I = I_s[\exp(V / nV_t) - 1]$) or intrinsic semiconductor bandgap ($n_i = B T^{3/2} \exp(-E_g / 2k_B T)$), electrostatic potential competes against thermal voltage $k_B T/q$. In December 1900, Max Planck placed that same $(e^x - 1)$ factor, with $x = \frac{hc}{\lambda k_B T}$, in the denominator of his blackbody spectral radiance law:

$$B_\lambda(T) = \frac{2 h c^2}{\lambda^5 \left(e^{\frac{h c}{\lambda k_B T}} - 1\right)}$$

resolving the classical ultraviolet divergence and introducing the quantum of action $h$. On the SC-32, evaluating $(e^x - 1)$ first in Register $X$ (`{{key:eˣ}} 1 {{key:-}}`) shifts that quantum denominator into Register $Z$ while $2hc^2 / \lambda^5$ is formed across Registers $Y$ and $X$, before `{{key:x⇄y}} {{key:÷}}` completes the quotient.

Numerical analysts distinguish two separate stages where direct exponential evaluation can lose precision: *inside* the `{{key:eˣ}}` routine on large arguments, and *on the stack* when subtracting $1$ from $e^x$ on small arguments. As William J. Cody and William Waite showed {{cite:cody1980}}, a high-accuracy library routine must first reduce any argument $x$ modulo $\ln 2$ ($x = k\ln 2 + r$, where $|r| \le \frac{1}{2}\ln 2$) using split extended-precision constants $C_1 + C_2 = \ln 2$ before evaluating a minimax approximation on the remainder $r$, avoiding internal range-reduction cancellation.

Separately, evaluating $e^x - 1$ on the stack for a very small argument such as $x = 10^{-10}$ by pressing `{{key:eˣ}}` and subtracting $1$ loses trailing significand bits in floating-point representation: storing $1 + 10^{-10} + \frac{1}{2}10^{-20}\dots$ in a 53-bit IEEE-754 word devotes the leading ten decimal digits of the significand to `1.000000000` and rounds away the $x^2/2$ curvature. For moderate exponents such as a forward-biased Shockley diode ($x = 17.95$) or visible-wavelength Planck radiation ($x = 4.98$), `{{key:eˣ}}` minus $1$ retains full precision; for small arguments $|x| \ll 10^{-5}$ (as in Rayleigh-Jeans radio-frequency astronomy), catastrophic cancellation on the stack is avoided by evaluating the two-term Taylor expansion $e^x - 1 \approx x(1 + x/2)$ or the identity $2 e^{x/2}\sinh(x/2)$ in place.

---

## Factorials, Combinatorics & Extending $n!$ to Fractional Numbers

In combinatorics, the number of distinct top-to-bottom permutations of an ordinary deck of $52$ playing cards follows directly from the multiplication principle. The first position can be filled by any of the $52$ cards; for each of those $52$ possibilities, the second position can be filled by any of the remaining $51$ cards ($52 \times 51$); and continuing down to the final card yields *52 factorial ($52!$)* distinct arrangements:

$$52! = 52 \times 51 \times 50 \times \dots \times 3 \times 2 \times 1 \approx \mathbf{8.0658 \times 10^{67}}$$

That integer, exceeding $8 \times 10^{67}$, surpasses the total number of atoms in the Earth. Even a modest $16 \times 16$ fiber-optic crossbar switch admits $16! = 20,922,789,888,000$ ($\approx 20.92\text{ trillion}$) distinct one-to-one routing configurations.

### Stirling's Asymptotic Formula and the Lanczos Gamma Approximation

On pocket scientific calculators of the 1970s and 1980s, keying `69` `x!` succeeded ($\approx 1.7112 \times 10^{98}$), whereas keying `70` `x!` halted with an `OVERFLOW` error because early BCD displays allocated only two decimal digits (`E99`) to the power-of-ten exponent and could not represent numbers $\ge 10^{100}$, while $70! \approx 1.197857 \times 10^{100}$ exceeds $10^{100}$. Because the SC-32 uses a 64-bit IEEE-754 floating-point core supporting exponents up to $10^{\pm 308}$, its unary `{{key:x!}}` key evaluates $70!$ ($\to 1.1978571670 \times 10^{100}$) in place in Register $X$ up to $170! \approx 7.2574 \times 10^{306}$ without overflow.

For analytical work in statistical mechanics, factorials are approximated asymptotically. In 1730, James Stirling and Abraham de Moivre proved that for large $n$, the factorial grows as $(n/e)^n$ scaled by $\sqrt{2\pi n}$:

$$n! \approx \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$$

Even at $n = 10$ ($10! = 3,628,800$), Stirling's leading term yields $3,598,695.62$, capturing over $99.17\%$ of the exact integer product.

In 1729, Christian Goldbach posed to Leonhard Euler in St. Petersburg the problem of interpolating the discrete factorial $n!$ to non-integer arguments such as $\left(\frac{1}{2}\right)!$. Because a finite product of positive integers has no direct meaning at $n = \frac{1}{2}$, Euler introduced a continuous improper integral, the *Gamma function*:

$$\Gamma(x + 1) = \int_0^\infty t^x e^{-t}\,dt = x\,\Gamma(x)$$

which agrees with the factorial at every non-negative integer ($n! = \Gamma(n+1)$) while extending analytically across real and complex arguments. Substituting $x = \frac{1}{2}$ into Euler's integral and applying the change of variables $t = u^2$ transforms the expression into Carl Friedrich Gauss's error integral $\int_0^\infty e^{-u^2}\,du = \frac{\sqrt{\pi}}{2}$:

$$\left(\frac{1}{2}\right)! = \Gamma\left(\frac{3}{2}\right) = \frac{\sqrt{\pi}}{2} \approx \mathbf{0.886226925453}$$

Once $\left(\frac{1}{2}\right)! = \frac{\sqrt{\pi}}{2}$ is fixed, Euler's functional recurrence $(x+1)! = (x+1)\,x!$ determines the factorial of every half-integer by successive multiplication:

$$\left(\frac{3}{2}\right)! = \frac{3}{2}\frac{\sqrt{\pi}}{2} = \frac{3\sqrt{\pi}}{4}, \qquad \left(\frac{5}{2}\right)! = \frac{5}{2}\cdot\frac{3}{2}\frac{\sqrt{\pi}}{2} = \frac{15\sqrt{\pi}}{8} \approx 3.32335097045$$

To evaluate `{{key:x!}}` for arbitrary real arguments in microseconds, the SC-32 firmware combines floating-point minimax range reduction {{cite:cody1980}} with Cornelius Lanczos's 1964 Chebyshev rational approximation:

$$\Gamma(z + 1) = \sqrt{2\pi}\left(z + g + \frac{1}{2}\right)^{z + 1/2} e^{-(z + g + 1/2)} A_g(z)$$

This unified Gamma routine evaluates both discrete Stirling comparisons and continuous geometric formulas such as the volume of an $n$-dimensional unit ball, $V_n = \frac{\pi^{n/2}}{(n/2)!}$, which increases from $V_2 = \pi \approx 3.1416$ and $V_3 = \frac{4}{3}\pi \approx 4.1888$ to its counterintuitive maximum across all Euclidean dimensions at $n = 5$ ($V_5 = \frac{\pi^{2.5}}{(2.5)!} = \frac{8}{15}\pi^2 \approx 5.2638$) before shrinking toward zero as $n \to \infty$ (because in higher dimensions, nearly all the volume of a cube hides in its distant corners while an inscribed unit ball wastes away).

### Slicing Numbers into Parts (`PARTS`) and Formatting the Display (`DISP`)

Two additional softkey menus handle real-number decomposition and non-destructive display formatting. When an astronomical observation log records $14.736\text{ decimal hours}$ or a marine GPS receiver reports latitude $30.267153^\circ\text{ N}$, a single floating-point value encodes integer units to the left of the radix point and fractional sub-units to the right. The `{{key:PARTS}}` softkey menu (Right Shift `{{key:↱}}` above `{{key:√x}}`) decomposes any value in Register $X$ into its *Integer Part* `IP` and *Fractional Part* `FP` while preserving the original unsplit value in `{{key:LASTX}}`. The same softkey menu provides *Absolute Value* `ABS` for $|x|$ (complementing the change-sign key `{{key:+/-}}`), *Sign* `SGN` for $\pm 1$ or $0$, and the Euclidean *Greatest Common Divisor* `{{key:GCD}}` and *Least Common Multiple* `{{key:LCM}}`:

| Menu Softkey | Operation Name | Mathematical Definition | Example on $X = -14.7360$ |
| :---: | :--- | :--- | :--- |
| **`{{key:IP}}`** | Integer Part | $\operatorname{sgn}(x)\lfloor |x| \rfloor$ (truncation toward zero) | $-14.0000$ |
| **`{{key:FP}}`** | Fractional Part | $x - \operatorname{IP}(x)$ (signed fractional remainder) | $-0.7360$ |
| **`{{key:ABS}}`** | Absolute Value | $|x| = \sqrt{x^2}$ (non-negative magnitude) | $+14.7360$ |
| **`{{key:SGN}}`** | Signum Function | $+1.0$ if $x > 0$, $0.0$ if $x = 0$, $-1.0$ if $x < 0$ | $-1.0000$ |

Because `{{key:IP}}` saves the original unsplit value inside `{{key:LASTX}}`, extracting the integer part (`{{key:IP}}`) in Register $X$, recalling `{{key:LASTX}}` (which lifts the integer hours into Register $Y$), taking the fractional part (`{{key:FP}}`), and multiplying by $60$ separates $14.736\text{ hours}$ into $14\text{ hours}$ in Register $Y$ and $44.16\text{ minutes}$ in Register $X$.

Complementing `{{key:PARTS}}`, the `{{key:DISP}}` menu formats numbers rounded to fixed decimal places via `{{key:FIX}} n`, scientific notation via `{{key:SCI}} n`, engineering multiples-of-three exponents via `{{key:ENG}} n` for SI prefixes such as $\text{pF}, \mu\text{F}, \text{mA}, \text{k}\Omega,$ and $\text{MHz}$, or full 12-digit general precision via `{{key:ALL}}`. Switching the display format never alters or truncates the 64-bit value stored inside the stack registers. For the Beer-Lambert $90\%$ optical absorption depth $z = -\ln(0.10)/\alpha = 0.00005116856\text{ m}$ ($51.169\,\mu\text{m}$) of the carbon-black polymer enclosure, the underlying register value renders across the four display modes as follows:

| Display Mode | Key Sequence | Display Format | How $0.00005116856\text{ m}$ Appears |
| :---: | :--- | :--- | :--- |
| **`FIX 4`** | `{{key:DISP}} {{key:FIX}} 4` | Fixed $n$ digits after decimal point | `0.0001` |
| **`SCI 4`** | `{{key:DISP}} {{key:SCI}} 4` | Scientific $m \times 10^k$ ($1 \le |m| < 10$) | `5.1169E-5` |
| **`ENG 4`** | `{{key:DISP}} {{key:ENG}} 4` | Engineering $m \times 10^{3k}$ (SI prefixes) | `51.169E-6` ($51.169\,\mu\text{m}$) |
| **`ALL`** | `{{key:DISP}} {{key:ALL}}` | Full 12-digit general representation | `5.11685576221E-5` |

---

## Evaluating Powers, Logarithms & Exponential Laws

Physical laws involving powers, logarithms, and exponentials obey a strict constraint of dimensional analysis: the argument of a logarithm or exponential cannot carry raw physical dimensions such as meters, seconds, or Pascals, because the Taylor series $e^x = 1 + x + x^2/2! + x^3/3! + \dots$ would otherwise sum incompatible powers of a unit. Every transcendental expression therefore forms an inner dimensionless ratio—such as $p_{\text{rms}}/p_0$ in acoustics, $N(t)/N_0$ in radiometric dating, $t/\tau$ in thermal relaxation, or $\Delta E/(RT)$ in statistical mechanics—before applying the transcendental function and scaling by an outer physical constant.

This structure maps directly onto the two operator arities of the keypad. Once two quantities of identical dimension are divided to form the dimensionless argument in Register $X$, an in-place unary key (`{{key:LN}}`, `{{key:eˣ}}`, `{{key:LOG}}`, `{{key:10ˣ}}`, `{{key:√x}}`, `{{key:x²}}`, `{{key:1/x}}`, `{{key:x!}}`) transforms Register $X$ in place ($X \leftarrow f(X)$) without requiring `{{key:ENTER}}` and without disturbing any pre-exponential baseline or outer coefficient held in Registers $Y, Z,$ and $T$. Conversely, the dyadic two-register keys (`{{key:yˣ}}`, `{{key:ˣ√y}}`, `{{key:x∥y}}`) combine a base, radicand, or branch impedance waiting in Register $Y$ with the exponent, root index, or parallel partner in Register $X$, dropping the upper stack by one level.

{{res:sc32_db_spl:screenshot|Acoustic sound pressure level 20 * log10(2 / 0.00002) = 100 dB evaluated from the inside out on the SC-32 stack.}}

### In-Place Squares, Reciprocal Roots & Harmonic Parallelism

Putting this unary-versus-dyadic distinction to work across gravitational physics, thermodynamics, electromagnetism, and relativistic kinematics resolves multi-term equations across the lower registers of the stack:

* **Einstein's White-Dwarf Gravitational Redshift ($z \approx \frac{GM}{Rc^2}$):**
  For a photon climbing out of the gravitational well of Sirius B, a solar-mass white dwarf ($M = 1.989 \times 10^{30}\text{ kg}$) packed into a sphere the size of the Earth ($R = 6.4 \times 10^6\text{ m}$, with $G = 6.6743 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2$ and $c = 2.99792 \times 10^8\text{ m/s}$), multiplying $G$ by $M$ on the stack establishes the stellar gravitational parameter $GM_{\odot} = 1.3275 \times 10^{20}\text{ m}^3/\text{s}^2$ in Register $X$, and dividing by the white dwarf's radius $R$ yields the surface gravitational potential $\Phi = 2.0742 \times 10^{13}\text{ J/kg}$. When the speed of light $c$ is keyed next, $\Phi$ lifts into Register $Y$; because the unary key `{{key:x²}}` squares $c$ in place inside Register $X$ ($\to 8.9875 \times 10^{16}\text{ m}^2/\text{s}^2$) without disturbing $\Phi$ in Register $Y$, one division completes the ratio without touching Registers $Z$ or $T$:
  * **Gravitational Redshift:** `{{res:sc32_03_algebra_transcendentals_seq_23:keys}}` $\to z = \mathbf{{{res:sc32_03_algebra_transcendentals_seq_23:value}}}$.

* **Van der Waals Real-Gas Equation of State ($P = \frac{nRT}{V - nb} - \frac{an^2}{V^2}$):**
  Contrast that single-branch ratio with Johannes Diderik van der Waals's 1873 equation of state, where two physical mechanisms compete: the repulsive kinetic pressure amplified by the finite volume $nb$ of the molecules themselves, and the attractive intermolecular cohesion $an^2/V^2$ that pulls molecules back from the container walls.

  For $n = 2.0\text{ mol}$ ($n^2 = 4.0\text{ mol}^2$) compressed into a vessel of volume $V = 0.0050\text{ m}^3$ at $T = 320.0\text{ K}$ ($R = 8.31446\text{ J/(mol}\cdot\text{K)}$, excluded molecular volume $b = 4.27 \times 10^{-5}\text{ m}^3/\text{mol}$, and cohesion constant $a = 0.364\text{ Pa}\cdot\text{m}^6/\text{mol}^2$), assembling the two-part denominator $(V - nb)$ pushes the thermal energy product $nRT = 5,321.2544\text{ J}$ up to Register $T$, where $T$-replication preserves it across the upper registers while the kinetic pressure ($1,082,744.15\text{ Pa}$) and cohesive tension ($58,240.00\text{ Pa}$, simplified by squaring $0.0050$ in place via `{{key:x²}}`) meet in Registers $Y$ and $X$ (`{{res:sc32_03_algebra_transcendentals_seq_40:keys}}` $\to P \approx \mathbf{1,024,504.15\text{ Pa}}$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2 {{key:ENTER}} 8.31446 {{key:×}} 320 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $5321.2544$ | Ideal kinetic energy numerator $n R T$ |
| `0.0050 {{key:ENTER}} 2 {{key:ENTER}} 4.27 {{key:E}} 5 {{key:+/-}} {{key:×}} {{key:-}} {{key:÷}}` | $5321.2544$ | $5321.2544$ | $5321.2544$ | $1082744.1501$ | Divide by free volume $(V - n b)$ for kinetic pressure term |
| `0.364 {{key:ENTER}} 4 {{key:×}} 0.0050 {{key:x²}} {{key:÷}} {{key:-}}` | $5321.2544$ | $5321.2544$ | $5321.2544$ | **$1024504.1501$** | Subtract molecular attraction term $a n^2 / V^2$ for net pressure $P$ (Pa) |

Equally direct is the two-keystroke unary combination `{{key:√x}} {{key:1/x}}`, which turns any inverse square-root law ($1/\sqrt{u}$) into a single-register cascade in Register $X$ without keying a numerator `1`:

* **RF Electromagnetic Skin Depth ($\delta = \frac{1}{\sqrt{\pi f\mu\sigma}}$):**
  When a $f = 100\text{ MHz}$ ($1.0 \times 10^8\text{ Hz}$) radio-frequency current flows through a copper conductor ($\sigma = 5.8 \times 10^7\text{ S/m}$, magnetic permeability $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$), eddy currents crowd the alternating current into a thin outer skin. Multiply $\pi f$, $\mu_0$, and $\sigma$ directly in Register $X$ to build the attenuation product $\pi f\mu_0\sigma = 2.2897 \times 10^{10}\text{ m}^{-2}$, then tap `{{key:√x}} {{key:1/x}}` to extract the root ($151,319.1\text{ m}^{-1}$) and invert it in place into meters before scaling by $10^6$ for micrometers:
  * **Copper Skin Depth:** `{{res:sc32_03_algebra_transcendentals_seq_41:keys}}` $\to \delta = \mathbf{{{res:sc32_03_algebra_transcendentals_seq_41:value}}\,\mu\text{m}}$.

* **Hendrik Lorentz's Relativistic Time Dilation ($\gamma = \frac{1}{\sqrt{1 - (v/c)^2}}$) & Aviation True Airspeed ($V_{\text{TAS}} = \frac{V_{\text{CAS}}}{\sqrt{\sigma}}$):**
  Evaluating stratospheric muon time dilation at $\beta = v/c = 0.85$ demonstrates that same unary chain: square $0.85$ in place with `{{key:x²}}` ($\to 0.7225$), negate and add $1$ to form the proper-time variance $1 - \beta^2 = 0.2775$, and tap `{{key:√x}} {{key:1/x}}` to extract the length-contraction factor $\sqrt{1-\beta^2} = 0.5268$ (saved in `{{key:LASTX}}`) and invert it into $\gamma = 1.8983$ (or $\gamma = \mathbf{5.0252\times}$ at $\beta = 0.98$). In subsonic mountain aviation, because a Pitot-static airspeed indicator senses dynamic pressure $q = \frac{1}{2}\rho V^2$, a pilot departing Leadville, Colorado ($9,934\text{ ft}$, where warm air reduces the density ratio to $\sigma = \rho/\rho_0 = 0.6944$) converts Calibrated Airspeed ($V_{\text{CAS}} = 120.0\text{ kt}$) to True Airspeed via the identical cascade: keying `0.6944 {{key:√x}} {{key:1/x}} 120 {{key:×}}` reveals $V_{\text{TAS}} = \mathbf{144.0000\text{ kt}}$ ($20\%$ faster through the airmass and over the runway in calm air).
  * **Muon Lorentz Factor ($\beta = 0.85$):** `{{res:sc32_03_algebra_transcendentals_seq_42:keys}}` $\to \gamma = \mathbf{{{res:sc32_03_algebra_transcendentals_seq_42:value}}}$.

The dyadic two-register keys (`{{key:yˣ}}`, `{{key:ˣ√y}}`, `{{key:x∥y}}`) combine Register $Y$ and Register $X$ with a one-level stack drop:

* **General Powers (`{{key:yˣ}}`) & Polytropic Gas Compression ($W = \frac{P_1 V_1}{n - 1}\left[(V_1/V_2)^{n - 1} - 1\right]$):**
  To raise a base $y = 2.5$ to an exponent $x = 3.8$, load the base into Register $Y$, key the exponent into Register $X$, and tap `{{key:yˣ}}`. In a mechanical gas compressor operating across a volume ratio $V_1/V_2 = 4.0$ with polytropic exponent $n - 1 = 0.32$ and energetic pre-factor $\frac{P_1 V_1}{n-1} = 15,000\text{ J}$, start inside the brackets: raise $4.0^{0.32} = 1.5583$ with `{{key:yˣ}}`, subtract $1$ to isolate the dimensionless work factor $0.5583$, and multiply by $15,000\text{ J}$:
  * **Pure Power Benchmark ($2.5^{3.8}$):** `{{res:sc32_03_algebra_transcendentals_seq_01:keys}}` $\to \mathbf{{{res:sc32_03_algebra_transcendentals_seq_01:value}}}$.
  * **Polytropic Compression Work:** `{{res:sc32_03_algebra_transcendentals_seq_34:keys}}` $\to \mathbf{{{res:sc32_03_algebra_transcendentals_seq_34:value}}\text{ J}}$.

* **Kepler's Third Law (`{{key:ˣ√y}}`) & Harmonic Round-Trip Speed (`{{key:x∥y}}`):**
  Applying Kepler's fractional-power law $a = \sqrt[3]{T^2}$ to Mars's sidereal period $T = 1.8808\text{ yr}$, square $T$ in place with `{{key:x²}}` ($\to 3.5374\text{ yr}^2$), enter the root index `3`, and tap the dyadic `{{key:ˣ√y}}` key to recover Mars's semi-major axis $a = \mathbf{1.5237\text{ AU}}$. Meanwhile, the round-trip mountain speed law ($30\text{ mph}$ uphill and $60\text{ mph}$ downhill) collapses via `{{key:x∥y}}` and a factor of $2$ into $2(30 \parallel 60) = \mathbf{40.0000\text{ mph}}$.

* **Weibull Wind-Turbine Distribution ($f(v) = \frac{k}{c}(v/c)^{k-1}\exp[-(v/c)^k]$) & Single-Pass Quadratic Sprints:**
  When an equation uses the *same* dimensionless ratio inside both a power law and a stretched exponential—as in Waloddi Weibull's wind-speed density for a turbine at $v = 8.5\text{ m/s}$, scale velocity $c = 9.0\text{ m/s}$, and shape parameter $k = 2.2$—the values $8.5$ and $9.0$ do not need to be keyed twice. Instead, form the normalized wind ratio $v/c = 0.9444$ once and press `{{key:ENTER}}` to duplicate it across the stack.

  Raise the first copy to $k = 2.2$, negate, and fire `{{key:eˣ}}` ($\to 0.4140$) while the saved copy of $v/c = 0.9444$ waits in Register $Y$; swap via `{{key:x⇄y}}` to raise $0.9444$ to $k - 1 = 1.2$ ($\to 0.9337$), multiply the two factors together, and scale by $k/c = 2.2/9.0$. Similarly, in a single-pass quadratic evaluation on $2.4 x^2 + 7.8 x - 15.6 = 0$, starting inside the discriminant radical $\sqrt{b^2 - 4ac} = \sqrt{7.8^2 - 4(2.4)(-15.6)} = 14.5121$, subtracting $b = 7.8$, and dividing by $2a = 4.8$ isolates the positive root in 13 keystrokes without touching a storage register:
  * **Weibull Wind Probability Density:** `{{res:sc32_03_algebra_transcendentals_seq_29:keys}}` $\to f(v) = \mathbf{0.094496\text{ (m/s)}^{-1}}$.
  * **Single-Pass Quadratic Positive Root:** `{{res:sc32_03_algebra_quadratic_sprint:keys}}` $\to x_+ = \mathbf{{{res:sc32_03_algebra_quadratic_sprint:value}}}$.

### Base-10 & Natural Logarithms (`LOG`, `LN`)

Because both `{{key:LOG}}` and `{{key:LN}}` are unary operators that transform Register $X$ in place, logarithmic perception scales and radiometric dating laws evaluate from the physical concentration or activity ratio straight outward:

* **Weber-Fechner Acoustic Decibels & Sabine Reverberation (`{{key:LOG}}`):**
  For a stadium acoustic wave of root-mean-square pressure $p_{\text{rms}} = 1.45\text{ Pa}$ referenced to the $p_0 = 2.0 \times 10^{-5}\text{ Pa}$ cochlear hearing threshold, dividing $p_{\text{rms}}$ by $p_0$ reveals that the pressure wave is $72,500\times$ stronger than the threshold of hearing. Tapping `{{key:LOG}}` compresses that $72,500:1$ ratio in place into $4.8603\text{ Bels}$ (powers of ten), and scaling by $20$ yields the sound pressure level in decibels. In architectural acoustics, a $60\text{ dB}$ ($10^6:1$) drop in sound energy sets Wallace Clement Sabine's $0.161\text{ s/m}$ reverberation constant across a concert hall of volume $V = 4,500\text{ m}^3$ and acoustic absorption $A = 320.0\text{ Sabins}$:
  * **Stadium Sound Pressure Level:** `{{res:sc32_03_algebra_transcendentals_seq_02:keys}}` $\to \mathbf{{{res:sc32_03_algebra_transcendentals_seq_02:value}}\text{ dB SPL}}$.
  * **Sabine Concert Hall Reverberation ($T_{60}$):** `{{res:sc32_03_algebra_transcendentals_seq_21:keys}}` $\to T_{60} = \mathbf{{{res:sc32_03_algebra_transcendentals_seq_21:value}}\text{ s}}$.

* **Henderson-Hasselbalch Buffer Equilibrium & Arterial Blood-Gas Physiology ($\text{pH} = \text{pK}_a + \log_{10}\frac{[\text{A}^-]}{[\text{HA}]}$):**
  In analytical chemistry, when an acetic acid buffer ($\text{pK}_a = 4.76$) pairs conjugate base $[\text{A}^-] = 0.185\text{ M}$ with weak acid $[\text{HA}] = 0.120\text{ M}$, divide the molar ratio $0.185 / 0.120 = 1.5417$ in Register $X$, tap `{{key:LOG}}` ($\to +0.1880\text{ pH units}$) in place, and add $\text{pK}_a = 4.76$:
  * **Buffer Equilibrium pH:** `{{res:sc32_03_algebra_transcendentals_seq_03:keys}}` $\to \mathbf{{{res:sc32_03_algebra_transcendentals_seq_03:value}}}$.

  In pulmonary and critical-care medicine, the carbonic acid–bicarbonate buffer maintains arterial blood plasma near $\text{pH } 7.40$ ($\text{pK}_a = 6.10$, Henry's law $\text{CO}_2$ solubility $\alpha = 0.0301\text{ mmol/(L}\cdot\text{mmHg)}$):
  $$\text{pH} = 6.10 + \log_{10}\!\left(\frac{[\text{HCO}_3^-]}{0.0301 \times P_{\text{CO}_2}}\right), \qquad [\text{H}_3\text{O}^+] = 10^{-\text{pH}}$$
  For an arterial blood-gas panel showing serum bicarbonate $[\text{HCO}_3^-] = 24.0\text{ mmol/L}$ and partial pressure $P_{\text{CO}_2} = 40.0\text{ mmHg}$, evaluating the dissolved $\text{CO}_2$ denominator in Register $X$ while $[\text{HCO}_3^-]$ waits in Register $Y$ yields $\text{pH} = \mathbf{7.3996}$, and inverting Sørensen's scale in place via `{{key:+/-}} {{key:10ˣ}}` (scaled by $10^9\text{ nmol/mol}$) reveals an effective free hydronium concentration of $\mathbf{39.8489\text{ nmol/L}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `24 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $24.0000$ | $24.0000$ | Stage serum bicarbonate $[\text{HCO}_3^-] = 24.0\text{ mmol/L}$ in $Y$ |
| `0.0301 {{key:ENTER}} 40 {{key:×}}` | $0.0000$ | $0.0000$ | $24.0000$ | $1.2040$ | Dissolved carbonic acid $\alpha P_{\text{CO}_2} = 1.2040\text{ mmol/L}$ |
| `{{key:÷}} {{key:LOG}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.2996$ | Base-to-acid ratio $19.9336$ logged in place to $+1.2996$ |
| `6.10 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $7.3996$ | Arterial blood plasma $\text{pH} = 6.10 + 1.2996 = 7.3996$ |
| `{{key:+/-}} {{key:10ˣ}} 1 {{key:E}} 9 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$39.8489$** | Inverse $10^{-\text{pH}} \times 10^9$: free $[\text{H}_3\text{O}^+]$ ($39.85\text{ nmol/L}$) |

* **Willard Libby's Carbon-14 & Potassium-Argon Radiometric Clocks (`{{key:LN}}`):**
  Evaluating Libby's radiocarbon inversion $t = -\ln(N/N_0) t_{1/2} / \ln 2$ for an Ice Age hearth bone retaining $23.4\%$ of its original ${}^{14}\text{C}$ ($N/N_0 = 0.234$, $t_{1/2} = 5,730\text{ yr}$), press `{{key:LN}}` to transform $0.234$ in place into $-1.4524$ natural decay units, multiply by $5,730\text{ yr}$, divide by $\ln(2) = 0.6931$ (computed in Register $X$ via `2 {{key:LN}}` while the numerator waits in Register $Y$), and negate via `{{key:+/-}}` while Registers $Z$ and $T$ remain at zero. For Precambrian volcanic basalt billions of years old, potassium-argon dating ($t = \frac{1}{\lambda}\ln\left(1 + C\frac{^{40}\text{Ar}}{^{40}\text{K}}\right)$ with $^{40}\text{Ar}/{}^{40}\text{K} = 0.0850$, $C = 9.54$, $\lambda = 5.543 \times 10^{-10}\text{ yr}^{-1}$) evaluates from the inner isotope ratio outward:
  * **Carbon-14 Ice Age Hearth Bone ($23.4\%$ remaining):** `{{res:sc32_03_algebra_transcendentals_seq_44:keys}}` $\to \mathbf{12,006.75\text{ years}}$ ($12,006.7541\text{ yr}$).
  * **Potassium-Argon Volcanic Core Age:** `{{res:sc32_03_algebra_transcendentals_seq_06:keys}}` $\to \mathbf{{{res:sc32_03_algebra_transcendentals_seq_06:value}}\text{ years}}$ ($1.071\text{ billion years}$).

Under the first-order relaxation law $t = -\tau \ln(\Delta T/\Delta T_0)$, a two-register logarithmic trace unfolds when an RC timing network with resistance $R = 150\text{ k}\Omega$ ($150,000\,\Omega$) and capacitance $C = 47\,\mu\text{F}$ ($47 \times 10^{-6}\text{ F}$) relaxes to $10\%$ ($0.10$) of its initial step voltage (`{{res:sc32_03_algebra_transcendentals_seq_05:keys}}` $\to \mathbf{{{res:sc32_03_algebra_transcendentals_seq_05:value}}\text{ seconds}}$). Once $R$ and $C$ multiply into the characteristic time constant $\tau = 7.0500\text{ s}$ in Register $X$, keying `0.10` and pressing `{{key:LN}}` lifts $\tau = 7.0500\text{ s}$ into Register $Y$ while transforming $0.10$ in place into $-2.302585$ time constants in Register $X$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `150000 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $150000.000$ | $150000.000$ | Load scale factor $150,000$ |
| `47 {{key:E}} 6 {{key:+/-}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $7.050000$ | Relaxation time constant $\tau = 7.05\text{ s}$ |
| `0.10 {{key:LN}}` | $0.0000$ | $0.0000$ | $7.050000$ | $-2.302585$ | $\ln(0.10)$ natural logarithm |
| `{{key:×}} {{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$16.233225$** | Relaxation time in seconds |

Similarly, at an annual compound growth rate of $r = 7.2\%$, dividing $\ln(2) = 0.6931$ in Register $Y$ by $\ln(1.072) = 0.0695$ in Register $X$ (`{{res:sc32_03_algebra_transcendentals_seq_25:keys}}`) yields the logarithmic doubling time of $\mathbf{{{res:sc32_03_algebra_transcendentals_seq_25:value}}\text{ years}}$, the exact benchmark behind the financial Rule of 72 ($72 / 7.2 = 10.0\text{ years}$).

### Natural Exponentials (`eˣ`) & Boltzmann's Universal Thermal Factor

Across physical chemistry, atmospheric physics, solid-state electronics, and quantum astrophysics, thermal processes share a single algebraic form: Ludwig Boltzmann's thermal activation factor $\exp(-\Delta E / k_B T)$ (or its molar counterpart $\exp(-\Delta E / RT)$), which compares a physical energy barrier $\Delta E$ against the thermal agitation energy $k_B T$ of the surrounding medium. Because `{{key:eˣ}}` is a unary operator on Register $X$, every Boltzmann calculation on the SC-32 follows a single inside-out sequence: assemble the dimensionless energy-to-temperature ratio inside Register $X$ first, fire `{{key:eˣ}}` in place second, and scale by the physical pre-factor third:

* **Arrhenius Chemical Activation Barrier ($E_a = \frac{R\ln(k_2/k_1)}{1/T_1 - 1/T_2}$):**
  Warming a chemical reaction by fifty degrees from $T_1 = 300\text{ K}$ ($k_1 = 3.25 \times 10^{-4}\text{ s}^{-1}$) to $T_2 = 350\text{ K}$ ($k_2 = 2.85 \times 10^{-2}\text{ s}^{-1}$) accelerates the reaction rate nearly ninety-fold. To extract Svante Arrhenius's activation barrier, first form the reciprocal-temperature window $1/300 - 1/350 = 4.7619 \times 10^{-4}\text{ K}^{-1}$ in Register $X$ via two taps of the unary `{{key:1/x}}` key, then evaluate the scaled logarithmic rate ratio $R\ln(k_2/k_1)$ while $4.7619 \times 10^{-4}\text{ K}^{-1}$ waits in Register $Y$, and swap via `{{key:x⇄y}}` before dividing and scaling by $1,000\text{ J/kJ}$ to reveal an activation barrier of $E_a = \mathbf{78.1148\text{ kJ/mol}}$:
  * **Reciprocal-Temperature Window ($\frac{1}{T_1} - \frac{1}{T_2}$):** `{{res:sc32_03_algebra_transcendentals_seq_45:keys}}` $\to 4.7619 \times 10^{-4}\text{ K}^{-1}$.
  * **Logarithmic Rate Numerator ($R\ln(k_2/k_1)$):** `{{res:sc32_03_algebra_transcendentals_seq_46:keys}}` $\to \mathbf{{{res:sc32_03_algebra_transcendentals_seq_46:value}}\text{ J/(mol}\cdot\text{K)}}$.

* **Solid-State Atomic Diffusion ($D = D_0 \exp(-Q / RT)$):**
  When interstitial carbon atoms diffuse through austenite steel inside a $T = 1,200\text{ K}$ heat-treating furnace ($Q = 148,000\text{ J/mol}$, $D_0 = 2.3 \times 10^{-5}\text{ m}^2/\text{s}$, $R = 8.31446\text{ J/(mol}\cdot\text{K)}$), form the dimensionless barrier ratio $Q/(RT) = 14.8336$ in Register $X$, negate and fire `{{key:eˣ}}` to show that only $3.613 \times 10^{-7}$ of lattice vibrations clear the energy jump, and scale by $D_0$:
  * **Carbon-in-Steel Diffusivity:** `{{res:sc32_03_algebra_transcendentals_seq_15:keys}}` $\to D = \mathbf{{{res:sc32_03_algebra_transcendentals_seq_15:value}}\text{ m}^2/\text{s}}$.

* **Clausius-Clapeyron Vapor Pressure ($P_2 = P_1 \exp[-\frac{\Delta H_{\text{vap}}}{R}(\frac{1}{T_2} - \frac{1}{T_1})]$):**
  That identical Boltzmann factor explains why water boils at $60^\circ\text{C}$ ($T_2 = 333.15\text{ K}$) inside a partial vacuum relative to its sea-level boiling point of $100^\circ\text{C}$ ($T_1 = 373.15\text{ K}$, $P_1 = 101.325\text{ kPa}$, molar enthalpy of vaporization $\Delta H_{\text{vap}} = 40,660\text{ J/mol}$). Invert both temperatures with `{{key:1/x}}` and subtract to form $1/T_2 - 1/T_1 = 3.2176 \times 10^{-4}\text{ K}^{-1}$ in Register $X$; multiply by $\Delta H_{\text{vap}}/R = 4,890.275\text{ K}$ for the dimensionless exponent $1.5735$; negate and fire `{{key:eˣ}}` to obtain the vapor-pressure fraction $P_2/P_1 = 0.2073$; and scale by $P_1 = 101.325\text{ kPa}$:
  * **Partial-Vacuum Vapor Pressure:** `{{res:sc32_03_algebra_transcendentals_seq_19:keys}}` $\to P_2 = \mathbf{21.0063\text{ kPa}}$.

* **Isothermal Barometric Scale Height on Mauna Kea ($P = P_0 \exp(-Mgh / RT_0)$):**
  When a mountaineer climbs to the $h = 4,207\text{ m}$ summit of Hawaii's Mauna Kea under the isothermal scale-height model ($M = 0.0289644\text{ kg/mol}$, $g = 9.80665\text{ m/s}^2$, $R = 8.314462\text{ J/(mol}\cdot\text{K)}$, reference temperature $T_0 = 288.15\text{ K}$, $P_0 = 1,013.25\text{ hPa}$), gravitational potential energy $Mgh$ replaces the chemical barrier $\Delta H_{\text{vap}}$. Forming the dimensionless scale-height ratio $\kappa = \frac{Mgh}{RT_0} = 0.4987$, firing `{{key:eˣ}}` on $-\kappa$ ($\to 0.6073$), and scaling by $P_0 = 1,013.25\text{ hPa}$ yields the summit pressure:
  * **Mauna Kea Summit Pressure:** `{{res:sc32_03_algebra_transcendentals_seq_47:keys}}` $\to P = \mathbf{615.3203\text{ hPa}}$.

* **Silicon Intrinsic Carrier Density ($n_i = B T^{3/2} \exp(-E_g / 2k_B T)$) & Shockley Diode ($I = I_s[\exp(V / nV_t) - 1]$):**
  Inside a crystal of pure silicon at room temperature $T = 300\text{ K}$ ($k_B = 8.61733 \times 10^{-5}\text{ eV/K}$, $B = 5.23 \times 10^{15}\text{ cm}^{-3}\text{K}^{-3/2}$, bandgap $E_g = 1.12\text{ eV}$), dividing $E_g$ by $2 k_B T = 0.051704\text{ eV}$ reveals a thermal barrier ratio of $21.6618$; negating, firing `{{key:eˣ}}` ($\to 3.9121 \times 10^{-10}$), and scaling by $T^{3/2} = 300^{1.5}$ and $B$ gives the intrinsic carrier density without touching Registers $Z$ or $T$. Conversely, applying a forward bias of $V = 0.58\text{ V}$ across a Shockley silicon p-n junction ($n = 1.25$, $V_t = 0.025852\text{ V}$, $I_s = 1.8 \times 10^{-11}\text{ A}$) lowers the electrostatic barrier so the Boltzmann exponent $V/(nV_t) = 17.9483$ turns positive; firing `{{key:eˣ}}`, subtracting $1$, and scaling by $I_s$ gives the forward current:
  * **Silicon Intrinsic Carrier Density:** `{{res:sc32_03_algebra_transcendentals_seq_14:keys}}` $\to n_i \approx \mathbf{1.0631 \times 10^{10}\text{ cm}^{-3}}$.
  * **Shockley Diode Forward Current:** `{{res:sc32_03_algebra_transcendentals_seq_09:keys}}` $\to I = \mathbf{{{res:sc32_03_algebra_transcendentals_seq_09:value}}\text{ A}}$ ($1.122\text{ mA}$).

An exponential calculation recruits all four stack registers ($T, Z, Y, X$) when the quantum occupancy factor $(e^x - 1)$ sits in the denominator of a multi-power physical law, as in Max Planck's 1900 blackbody spectral radiance law $B_\lambda(T) = \frac{c_1}{\lambda^5(e^x - 1)}$ at solar green wavelength $\lambda = 500\text{ nm} = 5.0 \times 10^{-7}\text{ m}$ ($c_1 = 2hc^2 = 1.19104 \times 10^{-16}\text{ W}\cdot\text{m}^2/\text{sr}$, dimensionless photon-to-thermal energy ratio $x = \frac{hc}{\lambda k_B T} = 4.98020$).

Evaluating the Bose-Einstein photon denominator $(e^{4.98020} - 1) = 144.5035$ first on Row 1 shifts it up into Registers $Z$ and $T$ while $c_1$ and the fifth-power wavelength $\lambda^5 = 3.1250 \times 10^{-32}\text{ m}^5$ are assembled in Registers $Y$ and $X$, before dropping back into Register $Y$ for a final `{{key:x⇄y}} {{key:÷}}` (`{{res:sc32_03_algebra_transcendentals_seq_13:keys}}` $\to B_\lambda \approx \mathbf{2.6375 \times 10^{13}\text{ W}/(\text{m}^3\cdot\text{sr})}$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4.98020 {{key:eˣ}} 1 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $144.5035$ | Planck photon distribution denominator $(e^x - 1)$ |
| `1.19104 {{key:E}} 16 {{key:+/-}} {{key:ENTER}}` | $0.0000$ | $144.5035$ | $1.1910 \times 10^{-16}$ | $1.1910 \times 10^{-16}$ | Load first radiation constant $2hc^2$ |
| `5.0 {{key:E}} 7 {{key:+/-}} {{key:ENTER}} 5 {{key:yˣ}}` | $144.5035$ | $144.5035$ | $1.1910 \times 10^{-16}$ | $3.1250 \times 10^{-32}$ | Raise wavelength to fifth power $\lambda^5$ |
| `{{key:÷}}` | $144.5035$ | $144.5035$ | $144.5035$ | $3.8113 \times 10^{15}$ | Divide radiation constant $c_1$ by $\lambda^5$ |
| `{{key:x⇄y}} {{key:÷}}` | $144.5035$ | $144.5035$ | $144.5035$ | **$2.6375 \times 10^{13}$** | Divide spectral power by photon denominator for radiance $B_\lambda$ |

### Factorials (`x!`), Lanczos Gamma, and Domain Guard Verification

Across both discrete permutations and continuous integrals, the unary `{{key:x!}}` key invokes Lanczos's rational Gamma engine across both integers and fractions. For a $16\text{-channel}$ photonic crossbar switch, `{{res:sc32_03_algebra_transcendentals_seq_30:keys}}` evaluates $16!$ in place in Register $X$ to display $\mathbf{{{res:sc32_03_algebra_transcendentals_seq_30:value}}}$ ($20,922,789,888,000$) routing states. Passing a half-integer to that same key (`{{res:sc32_03_algebra_transcendentals_seq_04:keys}}` $\to \mathbf{{{res:sc32_03_algebra_transcendentals_seq_04:value}}}$) confirms that Euler's fractional factorial $(1/2)! = \Gamma(3/2)$ matches Gauss's constant $\sqrt{\pi}/2$ (`{{res:sc32_03_algebra_transcendentals_seq_49:keys}}` $\to \mathbf{{{res:sc32_03_algebra_transcendentals_seq_49:value}}}$) to all 12 digits.

That half-integer identity determines the five-dimensional unit hypersphere volume $V_5 = \frac{\pi^{2.5}}{(2.5)!} = \frac{8}{15}\pi^2$: raising $\pi$ to the $2.5$ power in Register $Y$ and dividing by $(2.5)!$ in Register $X$ (`{{res:sc32_03_algebra_transcendentals_seq_31:keys}}`) confirms $V_5 = \mathbf{{{res:sc32_03_algebra_transcendentals_seq_31:value}}}$. Finally, passing an out-of-bounds argument such as a negative number to `{{key:LN}}` (`{{res:sc32_03_algebra_transcendentals_seq_50:keys}}`) triggers `INVALID DATA` (Code 02) without altering Registers $Y, Z,$ or $T$, and tapping `{{key:C}}` clears the banner so the calculation resumes intact.
