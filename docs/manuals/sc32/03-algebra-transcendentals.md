---
title: "Chapter 3: The Shortcut That Doubled the Lifespan of Astronomers | Thinking in the Stack (SC-32)"
description: "John Napier's logarithms, Weber-Fechner perception, Kleiber's biological scaling, the 5-domain harmonic operator, Euler's base e, Carbon-14 dating, Newton's cooling law, and Lanczos Gamma factorials on the StackCalc SC-32."
---

# Chapter 3: The Shortcut That Doubled the Lifespan of Astronomers

## The Scottish Baron Who Turned Multiplication into Addition

### Inside Merchiston Castle: Turning Products into Sums

In the damp stone tower of Merchiston Castle near Edinburgh, Scotland, in the opening years of the seventeenth century, a fifty-year-old Scottish landowner and amateur mathematician named **John Napier** (1550–1617) sat watching the scientific revolution grind to a halt.

Across Europe, astronomers had just inherited the richest treasure of observational data in human history. On the island of Hven in Denmark, Tycho Brahe had spent thirty years measuring the nightly positions of Mars and the stars to within one arcminute. In Prague, Tycho's young assistant **Johannes Kepler** was trying to prove that the planets orbit the Sun not in perfect circles, but in ellipses. Yet every time Kepler tested an elliptical orbit against Tycho's observations, he had to multiply and divide eight-digit trigonometric numbers by hand—filling nearly a thousand folio pages of dense arithmetic by candlelight. A single carried-digit mistake on page four hundred ruined months of work.

Napier asked himself a daring question: *Is there a secret tunnel in mathematics that turns multiplication into simple addition, division into subtraction, and square or cube roots into division by $2$ or $3$?*

Look at a simple row of powers of two or powers of ten—something every high-school Algebra II student writes in the margin of a notebook:

$$\begin{array}{ccccccccc}
\text{Exponent (Steps):} & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\text{Power of } 2: & 1 & 2 & 4 & 8 & 16 & 32 & 64 & 128 \\
\text{Power of } 10: & 1 & 10 & 100 & 1{,}000 & 10{,}000 & 100{,}000 & 1{,}000{,}000 & 10{,}000{,}000
\end{array}$$

Suppose you want to multiply $8 \times 16$ in the middle row. Examine the exponents directly above them: $8$ is step $3$ ($2^3$), and $16$ is step $4$ ($2^4$). When you **add** their exponents ($3 + 4 = 7$) and look directly below step $7$, you find **$128$** ($8 \times 16 = 128$)!

Why did that work? Because an exponent counts *how many times* you multiply by the base:

$$b^x \cdot b^y = b^{x + y}, \qquad \frac{b^x}{b^y} = b^{x - y}, \qquad \left(b^x\right)^n = b^{n x}$$

Napier spent twenty years filling in the gaps between the whole numbers by imagining two runners moving simultaneously along straight tracks:
* **Runner A (The Logarithm Track):** Runs along an infinite straight line at a completely constant speed $v_0$, covering equal **arithmetic** increments of distance in equal ticks of time ($0, \Delta x, 2\Delta x, 3\Delta x, \dots$).
* **Runner B (The Number Track):** Starts at distance $L$ from a finish line and runs toward the finish line at a speed proportional to the distance still remaining—covering equal **geometric** ratios in equal ticks of time ($L, L r, L r^2, L r^3, \dots$).

By pairing the arithmetic position of Runner A with the geometric position of Runner B at every instant, Napier constructed a continuous bridge between addition and multiplication. In 1614, three years before his death, he published *Mirifici Logarithmorum Canonis Descriptio* ("Description of the Wonderful Rule of Logarithms") {{cite:napier1614}}, coining the word **logarithm** from the Greek *logos* (ratio) and *arithmos* (number)—literally "the number that counts how many ratios." A year later, London geometry professor **Henry Briggs** made the long summer journey by stagecoach to Edinburgh and worked with Napier to anchor logarithms to **base $10$** ($\log_{10} 1 = 0$, $\log_{10} 10 = 1$, $\log_{10} 100 = 2$, $\log_{10} 1000 = 3$).

For any two positive numbers $a$ and $b$, Napier and Briggs's bridge obeys three golden laws:

$$\log(a \cdot b) = \log a + \log b, \qquad \log\left(\frac{a}{b}\right) = \log a - \log b, \qquad \log\left(y^x\right) = x \log y$$

Instead of spending twenty minutes multiplying two eight-digit numbers by hand, an astronomer could look up their two logarithms in Briggs's table, **add** them in ten seconds, and look up the number matching that sum. Even better, taking a **cube root** ($\sqrt[3]{y} = y^{1/3}$)—a grueling medieval extraction that took hours by hand—became as simple as looking up $\log y$ and dividing by $3$. When Kepler received Napier's book in 1617, he was overjoyed, dedicating his *Ephemerides* to the Scottish baron and using logarithms to discover his Third Law of Planetary Motion ($T^2 = a^3$). Two centuries later, the French astronomer Pierre-Simon Laplace wrote the ultimate tribute: *"Logarithms, by shortening the labors, doubled the life of the astronomer."*

How does a modern scientific instrument like the SC-32 evaluate `{{key:LN}}` and `{{key:LOG}}` to full 53-bit IEEE-754 accuracy across three hundred orders of magnitude? Following the classical algorithm of **William J. Cody and William Waite** {{cite:cody1980}}, the processor splits any positive floating-point number $x = m \cdot 2^k$ into its normalized binary significand $m \in [\frac{1}{\sqrt{2}}, \sqrt{2})$ and its exact integer binary exponent $k$:

$$\ln\left(m \cdot 2^k\right) = \ln(m) + k \ln(2)$$

Because $m$ is now squeezed into a tight neighborhood around $1$, the natural logarithm $\ln(m)$ can be expanded in terms of the rapidly converging rational transformation $z = \frac{m - 1}{m + 1}$:

$$\ln(m) = 2\left(z + \frac{z^3}{3} + \frac{z^5}{5} + \frac{z^7}{7} + \dots\right), \qquad \text{where } z = \frac{m - 1}{m + 1}$$

which converges to 16 decimal digits in just a handful of odd powers.

### The Weber-Fechner Law: Why Your Ears and Eyes Are Logarithmic

Logarithms are not merely a historical shortcut for 17th-century astronomers. In the nineteenth century, German physiologists Ernst Heinrich Weber and Gustav Fechner discovered a startling fact about the human brain: **nearly every human sense perceives the physical world on a base-10 logarithmic scale!**

Suppose you are sitting in a dark room holding a single lit birthday candle, and someone brings in a second candle. The room looks dramatically brighter. Now suppose you are standing under $100$ lit candles, and someone brings in candle number $101$. Can your eyes even tell the difference? Not at all. Your senses do not respond to the *absolute difference* ($+1\text{ candle}$); they respond to the **percentage ratio** ($\frac{\text{new intensity}}{\text{old intensity}}$). Every time physical energy multiplies by $10$, your brain perceives one equal step of loudness or brightness.

That is why four of the most famous scales in secondary and collegiate science are modeled on the SC-32 with the base-10 logarithm key `{{key:LOG}}` (and inverted with `{{key:10ˣ}}`), each operating in place on Register $X$ after you form the physical ratio on the bottom two shelves:
1. **Acoustic Decibels ($\text{dB SPL}$):**  
   Between the faintest rustle of dry leaves that the human eardrum can detect ($p_0 = 20\,\mu\text{Pa} = 2.0 \times 10^{-5}\text{ Pa}$) and the roar of a stadium concert or jet engine ($20\text{ Pa}$), air-pressure waves span a million-fold range ($10^6:1$), and sound *energy* ($I \propto p^2$) spans a **trillion-fold range ($10^{12}:1$)**! Inside your inner ear, the tapered basilar membrane of the **mammalian cochlea** acts as a mechanical base-10 logarithm calculator, compressing twelve orders of magnitude into the comfortable $0\text{ to }120\text{ dB}$ **Sound Pressure Level** scale:
   $$L_p = 20 \log_{10}\left(\frac{p_{\text{rms}}}{p_0}\right)\text{ dB SPL}$$
   To model this equation on the SC-32 from the **inside out**, you first place the measured sound pressure $p_{\text{rms}}$ on Shelf $Y$ and the hearing threshold $p_0 = 2.0 \times 10^{-5}\text{ Pa}$ on Shelf $X$ so `{{key:÷}}` reveals the raw physical pressure ratio in Register $X$. Next, a single tap of `{{key:LOG}}` compresses that ratio in place into base-10 orders of magnitude (Bels), and multiplying by $20$ scales the result into decibels (`dB SPL`). *(In **Chapter 13**, we will see how a $60\text{ dB}$ million-fold energy decay threshold governs room reverberation in architectural acoustics.)*
2. **Chemistry's $\text{pH}$ and Henderson-Hasselbalch Buffers:**  
   In chemistry, the concentration of hydronium ions $[\text{H}_3\text{O}^+]$ in water spans fourteen orders of magnitude from battery acid ($10^0\text{ M}$) to drain cleaner ($10^{-14}\text{ M}$). In 1909, Danish biochemist Søren Peder Lauritz Sørensen tamed those exponents by defining $\text{pH} = -\log_{10}[\text{H}_3\text{O}^+]$. When your blood or a laboratory buffer solution mixes a weak acid ($[\text{HA}]$) with its conjugate base ($[\text{A}^-]$), the **Henderson-Hasselbalch equation** gives the equilibrium $\text{pH}$:
   $$\text{pH} = \text{pK}_a + \log_{10}\left(\frac{[\text{A}^-]}{[\text{HA}]}\right)$$
   On the stack, you divide the conjugate base concentration in $Y$ by the weak acid concentration in $X$, tap `{{key:LOG}}` to transform the ratio in place, and add $\text{pK}_a$.
3. **Earthquake Richter Magnitudes ($M_L = \log_{10}(A/A_0)$):**  
   In 1935, Caltech seismologist Charles F. Richter tamed the vast range of ground motion recorded on Wood-Anderson torsion seismographs by defining earthquake magnitude as a base-10 logarithm (`{{key:LOG}}`): every whole-number step up the Richter scale means the ground shakes **$10\times$ farther** in amplitude and releases $10^{1.5} = 10\sqrt{10} \approx \mathbf{31.62\times}$ more elastic wave energy!
4. **Hipparchus and Pogson's Stellar Brightness Scale ($m_1 - m_2 = -2.5\log_{10}(F_1/F_2)$):**  
   Around 130 BC, the Greek astronomer Hipparchus ranked naked-eye stars from "First Magnitude" (the brightest) down to "Sixth Magnitude" (the faintest). In 1856, English astronomer Norman Robert Pogson discovered that Hipparchus's eye had naturally sorted stars by a base-10 logarithm: a 5-magnitude difference corresponds to a **$100\times$ ($10^2$) ratio in photon flux**, so each single magnitude step is a brightness ratio of $100^{1/5} = 10^{0.4} \approx \mathbf{2.5119\times}$.

---

## Power Laws, Biological Scaling & The Universal Harmonic Operator

Once Napier showed that $\log(y^x) = x\log y$, raising any positive number $y$ to *any* fractional or decimal power $x$ became possible:

$$y^x = e^{x \ln y} \qquad \text{and} \qquad \sqrt[x]{y} = y^{1/x}$$

On the SC-32, powers, roots, and reciprocals divide into two clean groups: **in-place unary keys** (`{{key:x²}}`, `{{key:√x}}`, `{{key:1/x}}`) that transform Shelf $X$ immediately without disturbing anything waiting upstairs in $Y, Z,$ or $T$, and **two-register dyadic keys** (`{{key:yˣ}}`, `{{key:ˣ√y}}`, `{{key:x∥y}}`) that combine Shelf $Y$ and Shelf $X$:

| Mathematical Function | Physical Keycap | Arity | Exact Mathematical Definition | Register Stack Effect |
| :--- | :---: | :---: | :--- | :--- |
| **Square** | `{{key:x²}}` | Unary | $f(x) = x^2$ | $X \leftarrow X^2$ |
| **Square Root** | `{{key:√x}}` | Unary | $f(x) = \sqrt{x}, \quad x \ge 0$ | $X \leftarrow \sqrt{X}$ |
| **Reciprocal** | `{{key:1/x}}` | Unary | $f(x) = 1/x, \quad x \ne 0$ | $X \leftarrow 1/X$ |
| **General Power** | `{{key:yˣ}}` | Dyadic | $f(y, x) = y^x = \exp(x \ln y)$ | $X \leftarrow Y^X$ (Dyadic drop) |
| **Arbitrary Root** | `{{key:ˣ√y}}` | Dyadic | $f(y, x) = \sqrt[x]{y} = y^{1/x}$ | $X \leftarrow Y^{1/X}$ (Dyadic drop) |
| **Parallel Harmonic** | `{{key:x∥y}}` | Dyadic | $f(x, y) = \frac{x \cdot y}{x + y}$ | $X \leftarrow \frac{X \cdot Y}{X + Y}$ (Dyadic drop) |

### Kepler's Planets, Kleiber's Mice and Whales, and Relativistic Muons

Why do fractional exponents like $y^{2/3}$, $y^{3/4}$, $y^{1.32}$, and $(1 - \beta^2)^{-1/2}$ appear everywhere in nature, and how does the SC-32 model them on its four shelves?

- **Kepler's Third Law ($T^2 = a^3 \implies a = T^{2/3}$):**  
  In 1619, Johannes Kepler discovered that the square of a planet's orbital period $T$ (in Earth years) equals the cube of its semi-major axis $a$ (its average distance from the Sun in Astronomical Units, where $1\text{ AU}$ is the Earth-Sun distance). Why $T^2 \propto a^3$? Sixty-eight years later, Isaac Newton showed that balancing gravitational pull $G M_{\odot} m / a^2$ against centripetal force $m v^2 / a = m(2\pi a / T)^2 / a$ immediately yields $T^2 = \frac{4\pi^2}{G M_{\odot}} a^3$.

  Taking the cube root of both sides turns $T^2 = a^3$ into a $2/3$ fractional power law:

  $$a = \left(T^2\right)^{1/3} = \sqrt[3]{T^2} = T^{2/3}$$

  On the SC-32, you can model $T^{2/3}$ in two ways: either square Mars's orbital period ($T = 1.8808\text{ Earth years}$) in place on Shelf $X$ with the unary key `{{key:x²}}` ($\to 3.5374$) and extract the cube root via the dyadic key `{{key:ˣ√y}}` (with `3` in Register $X$), or raise $T$ in Register $Y$ directly to the fractional exponent $2/3$ in Register $X$ with `{{key:yˣ}}` to find Mars's orbital radius $a = 1.5237\text{ AU}$.

- **Max Kleiber's $\frac{3}{4}$-Power Law of Life ($B \propto M^{3/4}$):**  
  In 1932, Swiss agricultural biologist **Max Kleiber** plotted the daily resting metabolic heat production $B$ (in Watts or kilocalories per day) against body mass $M$ across warm-blooded animals ranging from a $20\text{-gram}$ mouse to a $4,000\text{-kilogram}$ elephant ($200,000\times$ heavier). You might expect an elephant to burn $200,000\times$ as much energy as a mouse ($M^1$), or perhaps scale with external skin surface area ($M^{2/3} \approx M^{0.67}$) to shed body heat. Instead, Kleiber discovered that across almost all living organisms on Earth—from bacteria to blue whales—metabolic rate scales with the **three-quarters power of mass**:

  $$B = B_0 M^{3/4} = B_0 M^{0.75}$$

  Why $3/4$? As physicists Geoffrey West, James Brown, and Brian Enquist later showed, biological circulatory and respiratory trees are space-filling fractal networks that minimize pumping energy across three spatial dimensions, endowing life with an effective fourth scale dimension ($3 / (3 + 1) = 3/4$). Because metabolism scales as $M^{0.75}$, an animal $10,000\times$ heavier ($10^4$) needs only $(10^4)^{0.75} = 10^3 = 1,000\times$ as much food—and its heart rate scales as $M^{-1/4}$ ($10\times$ slower), which is why a tiny shrew's heart races at $800\text{ beats per minute}$ while a blue whale's heart beats fewer than $10\text{ times a minute}$.

- **Why Cosmic-Ray Muons Survive to Reach the Ocean ($\gamma = \frac{1}{\sqrt{1 - (v/c)^2}}$):**  
  Here is one of the most dramatic detective stories in modern physics. High in Earth's stratosphere, $15\text{ kilometers}$ ($15,000\text{ meters}$) above sea level, incoming cosmic rays collide with air nuclei and create unstable subatomic particles called **muons**. In a laboratory rest frame, a muon decays in an average proper lifetime of only $\tau_0 = 2.2\text{ microseconds}$ ($2.2 \times 10^{-6}\text{ s}$).
  Now do the classical multiplication in your head: even if a muon travels downward at $85\%$ of the speed of light ($v = 0.85c \approx 2.55 \times 10^8\text{ m/s}$), how far can it get in $2.2\text{ microseconds}$ before disintegrating?

  $$d_{\text{classical}} = v \cdot \tau_0 = (2.55 \times 10^8\text{ m/s})(2.2 \times 10^{-6}\text{ s}) \approx \mathbf{560\text{ meters}}$$

  By classical Newtonian physics, almost every single muon should vanish more than $14\text{ kilometers}$ above our heads—and yet detectors at sea level count cosmic-ray muons raining down on our beaches every second! Why? Because by **Albert Einstein's 1905 Special Theory of Relativity**, time itself slows down for a fast-moving clock by **Hendrik Lorentz's time-dilation factor $\gamma$**:

  $$\gamma = \frac{1}{\sqrt{1 - \left(\frac{v}{c}\right)^2}}$$

  Follow how the SC-32 unpeels $\gamma$ from the **inside out** on Shelf $X$ for $v/c = 0.85$:
  1. Start at the deepest inner ratio ($0.85$) and **square** it in place with `{{key:x²}}` ($0.85^2 = 0.7225$).
  2. Negate with `{{key:+/-}}` and add $1$ ($1 - 0.7225 = 0.2775$).
  3. Extract the **square root** in place with `{{key:√x}}` ($\sqrt{0.2775} \approx 0.5268$—from the muon's perspective, the atmosphere is length-contracted to $52.68\%$ of its rest thickness).
  4. Flip it upside down with the **reciprocal** key `{{key:1/x}}` ($1 / 0.5268 = \mathbf{1.8983}$)—stretching the muon's apparent lifetime while `{{key:LASTX}}` automatically retains the length-contraction factor $1/\gamma = 0.5268$. At $v = 0.999c$, $\gamma$ leaps past $22$, allowing muons to reach the ocean floor.

Notice the shared structural rhythm running through Kepler's orbits, Kleiber's metabolic scaling, and Einstein's relativistic muons. That rhythm explains why the SC-32 deliberately separates **in-place unary keys** (`{{key:x²}}`, `{{key:√x}}`, `{{key:1/x}}`) from **two-register dyadic keys** (`{{key:yˣ}}`, `{{key:ˣ√y}}`, `{{key:x∥y}}`). Whenever a power or root acts on a single physical term right where it sits—such as squaring the speed of light $c$ in Einstein's gravitational redshift ($z \approx \frac{GM}{Rc^2}$) for light climbing out of a dense white dwarf star, squaring molar volume $V$ in Johannes Diderik van der Waals's cohesive pressure correction ($P = \frac{nRT}{V - nb} - \frac{an^2}{V^2}$), or taking the reciprocal square root `{{key:√x}}` `{{key:1/x}}` for the electromagnetic skin depth $\delta = \frac{1}{\sqrt{\pi f \mu \sigma}}$ of alternating current crowding into the outer surface of a copper wire—an in-place unary key transforms Register $X$ immediately without touching `{{key:ENTER}}` or disturbing upper registers.

Conversely, whenever an equation pairs a base waiting on Shelf $Y$ with a general fractional exponent or root index you just formed on Shelf $X$—as in polytropic gas compression work ($W = \frac{P_1 V_1}{n - 1}[(V_1/V_2)^{n - 1} - 1]$), stretched-exponential atmospheric wind profiles, or solar air-mass attenuation ($I = I_0 \cdot 0.7^{(\text{AM}^{0.678})}$)—pressing the dyadic key `{{key:yˣ}}` or `{{key:ˣ√y}}` fuses $Y$ and $X$ into $Y^X$ or $\sqrt[X]{Y}$ and drops the upper stack by one floor. And whenever you want to inspect a rational power or decimal result as a reduced fraction $a/b$ or mixed number $n\frac{a}{b}$ (up to a configurable denominator ceiling set via `{{key:/c}}`, Right Shift `{{key:↱}}` above `{{key:.}}`), toggling fraction display mode (`{{key:FDISP}}`, Left Shift `{{key:↰}}` above `{{key:.}}`) formats Register $X$ as an exact rational approximation using Euclid's continued-fraction algorithm while keeping all 53 bits of floating-point precision underneath.

### The Five-Domain Universal Harmonic Operator (`x∥y`)

In Chapter 2, we met the two-pipe reservoir puzzle ($\frac{1}{T} = \frac{1}{T_1} + \frac{1}{T_2}$). Why did we give the SC-32 a dedicated primary hardware keycap labeled **`{{key:x∥y}}`** that computes the product-over-sum harmonic combination:

$$x \parallel y = \frac{x \cdot y}{x + y} = \left(\frac{1}{x} + \frac{1}{y}\right)^{-1}$$

in a single keystroke? Because **five seemingly unrelated chapters of a physics textbook all obey this exact same mathematical identity**:

| Physical Domain | What Combines via $x \parallel y = \frac{x y}{x + y}$ | Why the Reciprocal-Sum Law Appears |
| :--- | :--- | :--- |
| **1. Parallel Electrical Resistors** | $R_{\text{eq}} = R_1 \parallel R_2 = \frac{R_1 R_2}{R_1 + R_2}$ | Both resistors share the same voltage $V$, while their currents ($I_i = V/R_i$) add. |
| **2. Thin Optical Lenses & Mirrors** | $f = d_o \parallel d_i = \frac{d_o d_i}{d_o + d_i}$ | Light rays from object distance $d_o$ bend by constant optical power $1/f$ to focus at image distance $d_i$ ($\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$). |
| **3. Capacitors Wired in Series** | $C_{\text{eq}} = C_1 \parallel C_2 = \frac{C_1 C_2}{C_1 + C_2}$ | Series capacitor plates trap the exact same charge $Q$, while their voltage drops ($V_i = Q/C_i$) add. |
| **4. Mechanical Springs in Series** | $k_{\text{eq}} = k_1 \parallel k_2 = \frac{k_1 k_2}{k_1 + k_2}$ | Two springs hooked end-to-end feel the same tension force $F$, while their stretches ($\Delta x_i = F/k_i$) add. |
| **5. Round-Trip Average Speed** | $v_{\text{avg}} = 2(v_1 \parallel v_2) = \frac{2 v_1 v_2}{v_1 + v_2}$ | Driving $D\text{ miles}$ uphill at $v_1 = 30\text{ mph}$ and $D\text{ miles}$ downhill at $v_2 = 60\text{ mph}$ adds *times* ($D/v_1 + D/v_2$), giving $2(30 \parallel 60) = \mathbf{40\text{ mph}}$ (not $45\text{ mph}$). |

Consider why all five laws collapse into $x \parallel y$:
* In a **parallel resistor network**, Kirchhoff's current law states that the total current $I_{\text{total}} = V / R_{\text{eq}}$ splitting at a node is the sum of the branch currents $I_1 + I_2 = V/R_1 + V/R_2$. Dividing out the common voltage $V$ gives $\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2}$.
* In **series capacitors**, the exact opposite duality holds: the same displacement charge $+Q$ and $-Q$ is induced on each capacitor in the chain, while the voltages add ($V_{\text{total}} = V_1 + V_2 \implies \frac{Q}{C_{\text{eq}}} = \frac{Q}{C_1} + \frac{Q}{C_2}$).
* In **series Hookean springs**, both springs experience the same tension force $F$, while their physical elongations add ($\Delta x_{\text{total}} = \Delta x_1 + \Delta x_2 \implies \frac{F}{k_{\text{eq}}} = \frac{F}{k_1} + \frac{F}{k_2}$), making the combined spring *softer* than either individual spring.
* Because $x \parallel y$ is both **commutative** ($x \parallel y = y \parallel x$) and **associative** ($(x \parallel y) \parallel z = x \parallel (y \parallel z)$), you can chain three, four, or ten parallel branches on the stack with `{{key:x∥y}}` just as effortlessly as chaining `{{key:+}}` or `{{key:×}}`.

Seeing that a glass camera lens, two coil springs, two parallel resistors, and a mountain road trip are all disguised versions of $x \parallel y$ is one of the great "aha!" moments of mathematical maturity.

---

## Leonhard Euler's Natural Base e, Carbon-14 & Cooling Coffee

While Henry Briggs's base-10 logarithm (`{{key:LOG}}`) is ideal for counting powers of ten, nature itself has a favorite base—a mysterious, unending number studied by **Jacob Bernoulli** in 1683 while analyzing compound interest and named **$e$** by the great Swiss mathematician **Leonhard Euler** in 1727:

$$e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = 1 + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + \frac{1}{4!} + \dots \approx \mathbf{2.718281828459}$$

Where does $e$ come from? Imagine a generous bank in 17th-century Basel that pays $100\%$ nominal interest per year on $\$1.00$:
- If the bank compounds interest **once** at the end of the year, you get $(1 + 1)^1 = \$2.00$.
- If it compounds **twice** a year ($50\%$ every six months), you get $(1 + \frac{1}{2})^2 = \$2.25$.
- If it compounds **quarterly** ($25\%$ every three months, $n = 4$), you get $(1 + \frac{1}{4})^4 \approx \$2.4414$.
- If it compounds **monthly** ($n = 12$), you get $(1 + \frac{1}{12})^{12} \approx \$2.6130$.
- If it compounds **every day** ($n = 365$), you get $(1 + \frac{1}{365})^{365} \approx \$2.7146$.
- If it compounds **every second** ($n = 31,536,000$)—growing continuously at every instant in proportion to its current size—your $\$1.00$ approaches Euler's limit **$e \approx \$2.718281828459\dots$**

Why do physicists, chemists, and biologists call $e^x$ (`{{key:eˣ}}`) and its inverse $\ln x$ (`{{key:LN}}`) the **natural** exponential and logarithm? Because when you differentiate the infinite factorial series for $e^x$ term by term, every power $\frac{x^k}{k!}$ steps down to $\frac{k x^{k-1}}{k!} = \frac{x^{k-1}}{(k-1)!}$, reproducing the exact same series:

$$\frac{d}{dx}\left(1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \dots\right) = 0 + 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots = e^x$$

The function $e^x$ is the only curve in the universe whose **rate of change (slope) at every point is equal to its own height**! Whenever anything in nature grows or decays at a rate proportional to how much of it is present right now ($\frac{dN}{dt} = \pm \lambda N$), Euler's base $e$ is the law that governs it.

### Willard Libby's 1949 Carbon-14 Time Machine

In 1949, at the University of Chicago, physical chemist **Willard F. Libby** realized that Euler's natural logarithm (`{{key:LN}}`) could turn every piece of ancient wood, linen, charcoal, or bone on Earth into a nuclear stopwatch—an insight that won him the 1960 Nobel Prize in Chemistry.

Here is how Libby's clock works:
1. High in the stratosphere, cosmic-ray neutrons continuously bombard nitrogen-14 atoms ($^{14}\text{N} + n \to {}^{14}\text{C} + p$), converting them into radioactive **carbon-14 ($^{14}\text{C}$)** at a steady global rate.
2. Those $^{14}\text{C}$ atoms oxidize into carbon dioxide ($^{14}\text{CO}_2$), mix throughout the atmosphere and oceans, and enter the food chain through photosynthesis. As long as a tree, a sheep, or a human being is alive—breathing air and eating plants—the ratio of radioactive $^{14}\text{C}$ to normal stable carbon ($^{12}\text{C}$) in its tissues stays locked to the atmosphere's equilibrium baseline ($N_0 \approx 1\text{ part per trillion}$).
3. The instant the tree is chopped down for a prehistoric campfire or woven into the flax linen wrappings of the **Dead Sea Scrolls**, photosynthesis and metabolism stop. No fresh $^{14}\text{C}$ ever enters the sample again. From that day forward, its trapped $^{14}\text{C}$ nuclei undergo beta decay back into nitrogen-14 with a physical (**Cambridge**) half-life of **$t_{1/2} = 5,730\text{ years}$**:

   $$N(t) = N_0 \left(\frac{1}{2}\right)^{t / t_{1/2}} = N_0 e^{-\lambda t}, \qquad \text{where } \lambda = \frac{\ln 2}{t_{1/2}} = \frac{\ln 2}{5730} \approx 1.20968 \times 10^{-4}\text{ yr}^{-1}$$

To invert that equation on the SC-32 from the **inside out** and read the age $t$ of an Ice Age hearth bone that retains **$23.4\%$** of its original $^{14}\text{C}$ ($N(t)/N_0 = 0.234$):

$$t = -\frac{\ln(N(t)/N_0)}{\lambda} = -\frac{\ln(0.234) \times 5730}{\ln 2}$$

1. Start inside the logarithm with the surviving fraction ($0.234$) on Shelf $X$ and press `{{key:LN}}` to take its **natural logarithm** in place ($\ln(0.234) = -1.4524\text{ natural decay units}$).
2. Multiply by the half-life ($5,730\text{ years}$), divide by $\ln 2 \approx 0.6931$ (computed right on Shelf $X$ via `2 {{key:LN}}` while the numerator waits in $Y$), and flip the minus sign with `{{key:+/-}}`: the bone is **$12,006.75\text{ years old}$**, dating straight to the end of the last Ice Age. *(For volcanic rocks billions of years old, geologists use the same `{{key:LN}}` law on Potassium-40 decaying into Argon-40 gas trapped inside cooled lava crystals, while in **Chapter 11** we will see how the exact logarithmic doubling law $t = \frac{\ln 2}{\ln(1+r)}$ underpins compound-interest growth.)*

### Newton's Law of Cooling: Why Hot Coffee Cools Fastest in the First Five Minutes

You do not need a nuclear physics lab to watch $e^{-t/\tau}$ in action; you can observe it on your kitchen table every morning.

In 1701, **Isaac Newton** placed a glowing-hot iron block in a steady breeze and observed that the rate $\frac{dT}{dt}$ at which a warm object loses heat to its surroundings is directly proportional to the **temperature difference** $\Delta T(t) = T(t) - T_{\text{room}}$ between the object and the surrounding room air:

$$\frac{d}{dt}\left(T(t) - T_{\text{room}}\right) = -\frac{1}{\tau}\left(T(t) - T_{\text{room}}\right)$$

- When a fresh cup of coffee is piping hot ($90^\circ\text{C}$ in a $20^\circ\text{C}$ room, so $\Delta T_0 = 70^\circ\text{C}$), heat pours out into the room rapidly.
- Twenty minutes later, when the coffee has cooled to $35^\circ\text{C}$ ($\Delta T = 15^\circ\text{C}$), it loses heat almost five times more slowly.

Because the rate of cooling is proportional to the remaining temperature excess, integrating that differential equation yields a pure exponential relaxation curve with characteristic thermal time constant $\tau$:

$$\Delta T(t) = \Delta T_0 e^{-t/\tau} \implies t = -\tau \ln\left(\frac{\Delta T(t)}{\Delta T_0}\right)$$

Whether a cup of coffee is relaxing toward room temperature or an electrical timing circuit with time constant $\tau = 7.05\text{ s}$ is relaxing to $10\%$ of its initial state ($\Delta T / \Delta T_0 = 0.10$), multiplying $\tau = 7.05\text{ s}$ on Shelf $Y$ by $\ln(0.10) = -2.3026$ on Shelf $X$ and tapping `{{key:+/-}}` reveals that $90\%$ of the relaxation finishes in $t = 16.23\text{ seconds}$.

### How the Stack Models the Boltzmann Factor: From Mountain Air to Quantum Starlight

Why does food spoil four times faster on a warm picnic table than in a refrigerator? Why does water boil at only $60^\circ\text{C}$ inside a vacuum chamber? Why is a mountaineer gasping for breath atop Hawaii's $4,207\text{-meter}$ Mauna Kea? And why does a silicon solar cell or a glowing star obey the exact same exponential curve?

Every one of those phenomena is governed by a universal competition between **barrier energy ($\Delta E$)** and **thermal motion ($RT$ or $kT$)** inside Ludwig Boltzmann's and Leonhard Euler's natural exponential (`{{key:eˣ}}`):
- **Chemical & Solid-State Activation Barriers ($\exp(-E_a / RT)$):**  
  In **Svante Arrhenius's 1889 activation law** ($k = A \exp(-E_a / RT)$), in solid-state atomic diffusion ($D = D_0 \exp(-Q / RT)$), and in the **Clausius-Clapeyron vapor-pressure equation** ($\ln(P_2/P_1) = -\frac{\Delta H_{\text{vap}}}{R}(\frac{1}{T_2} - \frac{1}{T_1})$), molecules must clear an energy barrier to react, hop through a crystal lattice, or escape from a liquid into a vapor. On the SC-32 stack, you always model a Boltzmann factor from the **exponent outward**: form the dimensionless energy-to-temperature ratio $\Delta E / RT$ (or reciprocal-temperature difference $\frac{1}{T_1} - \frac{1}{T_2}$ via two taps of `{{key:1/x}}` and `{{key:-}}`) right on Shelf $X$, press `{{key:+/-}}` if it is a decay barrier, tap `{{key:eˣ}}` to convert the dimensionless exponent into a probability factor in place, and multiply by the pre-exponential baseline ($A, D_0,$ or $P_1$).
- **Barometric Altitude ($P(h) = P_0 e^{-Mgh/RT}$):**  
  In the ocean, water is nearly incompressible, so hydrostatic pressure grows *linearly* with depth. Air, however, is a compressible ideal gas whose density $\rho = \frac{PM}{RT}$ is proportional to pressure $P$ itself. Substituting $\rho$ into the hydrostatic balance gives $\frac{dP}{P} = -\frac{Mg}{RT}\,dh$: here gravitational potential energy $Mgh$ competes against thermal energy $RT$, causing atmospheric pressure to drop **exponentially** with altitude $h$ and leaving only $60.7\%$ of sea-level air atop Mauna Kea.
- **Semiconductors & Max Planck's 1900 Quantum Law ($e^x - 1$):**  
  Across a silicon p-n diode ($I = I_s[\exp(V / nV_t) - 1]$) or intrinsic silicon bandgap ($n_i = B T^{3/2} \exp(-E_g / 2kT)$), electrostatic potential competes against thermal voltage $kT/q$. And in December 1900, when **Max Planck** placed that same $(e^x - 1)$ expression—with $x = \frac{hc}{\lambda kT}$—in the denominator of his blackbody spectral radiance law,

  $$B_\lambda(T) = \frac{2 h c^2}{\lambda^5 \left(e^{\frac{h c}{\lambda k T}} - 1\right)}$$

  he prevented the classical ultraviolet catastrophe and launched quantum mechanics! On the SC-32, evaluating $(e^x - 1)$ first on Shelf $X$ (`{{key:eˣ}} 1 {{key:-}}`) lets that quantum denominator ride up to Shelf $Z$ while you compute $2hc^2 / \lambda^5$ on Shelves $Y$ and $X$, before a final swap-and-divide (`{{key:x⇄y}} {{key:÷}}`) unites them. *(See **On the Stack** below for the complete worked tables across all of these systems.)*

> **Why High-Precision Calculators Guard Against Catastrophic Cancellation:**  
> Numerical analysts distinguish two separate places where careless exponential evaluation loses precision: **inside** the `{{key:eˣ}}` algorithm on large arguments, and **on the stack** when subtracting $1$ from $e^x$ on tiny arguments. First, as **William J. Cody and William Waite** demonstrated in their classic 1980 manual {{cite:cody1980}}, a high-precision math engine must reduce any argument $x$ modulo $\ln 2$ (`x = k * ln(2) + r`, where $|r| \le \frac{1}{2}\ln 2$) using split extended-precision constants $C_1 + C_2 = \ln 2$ before evaluating a minimax polynomial on the reduced remainder $r$, preventing internal range-reduction cancellation. Second, what happens on the stack if you evaluate $e^x - 1$ for a tiny number like $x = 10^{-10}$ by pressing `{{key:eˣ}} 1 {{key:-}}`? Even if `{{key:eˣ}}` computes $e^{10^{-10}}$ accurately, storing $1 + 10^{-10} + \frac{1}{2}10^{-20}\dots$ into a 53-bit IEEE-754 register forces the leading `1.000000000` to consume the first ten decimal digits of the mantissa, rounding away the delicate $x^2/2$ curvature before you ever press `1 {{key:-}}`! For moderate exponents like our Shockley diode ($x = 17.95$) or visible-light Planck law ($x = 4.98$), `{{key:eˣ}} 1 {{key:-}}` retains full accuracy; for tiny arguments $|x| \ll 10^{-5}$ (such as long-wavelength Rayleigh-Jeans radio astronomy), you avoid **catastrophic cancellation** on the stack by evaluating the two-term Taylor series $e^x - 1 \approx x + \frac{1}{2}x^2 = x(1 + x/2)$ or the exact identity $2 e^{x/2}\sinh(x/2)$ directly.

---

## Factorials, Combinatorics & Extending n! to Fractional Numbers

Suppose you pick up an ordinary deck of $52$ playing cards and give it a thorough shuffle. How many different top-to-bottom orders can those $52$ cards land in?

- The top card can be any of the **$52$** cards.
- For each of those $52$ choices, the second card can be any of the remaining **$51$** cards ($52 \times 51$).
- Continuing down to the last card gives **52 factorial ($52!$)** possible arrangements:

$$52! = 52 \times 51 \times 50 \times \dots \times 3 \times 2 \times 1 \approx \mathbf{8.0658 \times 10^{67}}$$

That number—an $8$ followed by sixty-seven zeros—is larger than the total number of atoms in the entire Earth! Every time you thoroughly shuffle a fair deck of $52$ cards, you are almost certainly holding a card sequence that has never existed before in human history. Even a modest $16 \times 16$ fiber-optic crossbar switch has $16! = 20,922,789,888,000$ ($\approx 20.92\text{ trillion}$) distinct one-to-one routing configurations.

### Breaking the Vintage $69!$ Barrier, Stirling's Asymptotic Formula, and Lanczos's Gamma Engine

If you ever played with a pocket scientific calculator in the 1970s or 1980s, you probably discovered a famous quirk: typing `69` `x!` worked fine ($\approx 1.7112 \times 10^{98}$), but typing `70` `x!` crashed with an `OVERFLOW` error. Why? Because vintage calculators allocated only two decimal digits (`E99`) for the power-of-ten exponent, so they could not display any number $\ge 10^{100}$ (a googol), and $70! \approx 1.197857 \times 10^{100}$ steps right past $10^{100}$. Because the SC-32 uses a 64-bit IEEE-754 floating-point core supporting exponents up to $10^{\pm 308}$, its unary `{{key:x!}}` key evaluates $70!$ ($\to 1.1978571670 \times 10^{100}$) in place on Shelf $X$—all the way up to $170! \approx 7.2574 \times 10^{306}$—without overflowing.

How did physicists in statistical mechanics estimate $n!$ before 64-bit calculators? In 1730, the Scottish mathematician **James Stirling** and Abraham de Moivre proved that for large $n$, the factorial grows as $(n/e)^n$ multiplied by $\sqrt{2\pi n}$:

$$n! \approx \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$$

Even at a modest integer like $n = 10$ ($10! = 3,628,800$), Stirling's formula gives $3,598,695.62$—capturing over $99.17\%$ of the true value in a single smooth expression.

Even more intriguing is a puzzle that Christian Goldbach posed to twenty-two-year-old **Leonhard Euler** in 1729: *What does $\left(\frac{1}{2}\right)!$ mean?*

How can you multiply all the whole numbers from $1$ up to $\frac{1}{2}$? Euler solved the riddle by discovering a continuous integral—the **Gamma function**:

$$\Gamma(x + 1) = \int_0^\infty t^x e^{-t}\,dt = x\,\Gamma(x)$$

that passes smoothly through every integer factorial ($n! = \Gamma(n+1)$) while defining factorials for fractions as well. When you substitute $x = \frac{1}{2}$ into Euler's integral and change variables to $t = u^2$, the integral turns into Carl Friedrich Gauss's famous bell-curve integral $\int_0^\infty e^{-u^2}\,du = \frac{\sqrt{\pi}}{2}$:

$$\left(\frac{1}{2}\right)! = \Gamma\left(\frac{3}{2}\right) = \frac{\sqrt{\pi}}{2} \approx \mathbf{0.886226925453}$$

The factorial of one-half is half the square root of $\pi$! To compute `{{key:x!}}` for both integers and fractional numbers on the SC-32 in microseconds, the firmware uses Hungarian physicist **Cornelius Lanczos's 1964 Chebyshev rational approximation** {{cite:cody1980}}—which lets you compute everything from Stirling factorial comparisons to the volume of a five-dimensional unit hypersphere ($V_5 = \frac{\pi^{2.5}}{(2.5)!} = \frac{8}{15}\pi^2 \approx 5.2638$, the dimension where a unit ball's volume reaches its maximum across all dimensions $n$).

### Slicing Numbers into Parts (`PARTS`) and Formatting the Display (`DISP`)

Rounding out our algebraic toolkit are two practical conveniences for science and engineering:
- **Number Parts (`{{key:PARTS}}`: `IP`, `FP`, `ABS`, `SGN`, `GCD`, `LCM`):**  
  When an astronomical telescope log reports $14.736\text{ decimal hours}$ or a marine GPS receiver streams latitude $30.267153^\circ\text{ N}$, a single floating-point number packs whole units to the left of the decimal point and fractional sub-units to the right. The `{{key:PARTS}}` menu (Right Shift `{{key:↱}}` above `{{key:√x}}`) splits any number in Shelf $X$ into its **Integer Part (`IP`)** and **Fractional Part (`FP`)** while preserving the original unsplit number inside `{{key:LASTX}}`, alongside **Absolute Value (`ABS`, $|x|$)**, **Sign (`SGN`, $\pm 1$ or $0$)**, and Euclidean **Greatest Common Divisor (`{{key:GCD}}`)** and **Least Common Multiple (`{{key:LCM}}`)**:

| Menu Softkey | Operation Name | Mathematical Definition | Example on $X = -14.7360$ |
| :---: | :--- | :--- | :--- |
| **`{{key:IP}}`** | Integer Part | $\operatorname{sgn}(x)\lfloor |x| \rfloor$ (truncation toward zero) | $-14.0000$ |
| **`{{key:FP}}`** | Fractional Part | $x - \operatorname{IP}(x)$ (signed fractional remainder) | $-0.7360$ |
| **`{{key:ABS}}`** | Absolute Value | $|x| = \sqrt{x^2}$ (non-negative magnitude) | $+14.7360$ |
| **`{{key:SGN}}`** | Signum Function | $+1.0$ if $x > 0$, $0.0$ if $x = 0$, $-1.0$ if $x < 0$ | $-1.0000$ |

  Because `{{key:IP}}` saves the original unsplit number inside `{{key:LASTX}}`, extracting the integer part (`{{key:IP}}`) onto Shelf $X$, recalling `{{key:LASTX}}` (which lifts the whole hours to Shelf $Y$), taking the fractional part (`{{key:FP}}`), and scaling by $60$ cleanly splits $14.736\text{ hours}$ into $14\text{ hours}$ in Register $Y$ and $44.16\text{ minutes}$ in Register $X$.
- **Non-Destructive Display Formatting (`{{key:DISP}}`: `{{key:FIX}}`, `{{key:SCI}}`, `{{key:ENG}}`, `{{key:ALL}}`):**  
  Accessed via **`{{key:DISP}}`** (Left Shift `{{key:↰}}` above `{{key:E}}`), whether you display numbers rounded to fixed decimal places (`{{key:FIX}} n`), scientific notation (`{{key:SCI}} n`), engineering multiples-of-three exponents (`{{key:ENG}} n` for $\text{pF}, \text{nH}, \mu\text{F}, \text{mA}, \text{k}\Omega, \text{MHz}$), or full 12-digit general display (`{{key:ALL}}`), **changing the display mode never alters or truncates the 64-bit precision stored inside the stack registers**. Recall the Beer-Lambert optical absorption length $1/\alpha = 0.00005116855\text{ m}$ ($51.169\,\mu\text{m}$) we computed for our transflective polarizer film in Chapter 1; here is how that exact same register value appears across all four display modes:

| Display Mode | Key Sequence | Display Format | How $0.00005116855\text{ m}$ Appears |
| :---: | :--- | :--- | :--- |
| **`FIX 4`** | `{{key:DISP}} {{key:FIX}} 4` | Fixed $n$ digits after decimal point | `0.0001` |
| **`SCI 4`** | `{{key:DISP}} {{key:SCI}} 4` | Scientific $m \times 10^k$ ($1 \le |m| < 10$) | `5.1169E-5` |
| **`ENG 4`** | `{{key:DISP}} {{key:ENG}} 4` | Engineering $m \times 10^{3k}$ (SI prefixes) | `51.169E-6` ($51.169\,\mu\text{m}$) |
| **`ALL`** | `{{key:DISP}} {{key:ALL}}` | Full 12-digit general representation | `5.11685525285E-5` |

---

## On the Stack: Powers, Logarithms & Transcendentals Workbench

Think back over every law we just met—from gravitational redshift $z = \frac{GM}{Rc^2}$ and muon time dilation $\gamma = \frac{1}{\sqrt{1 - (v/c)^2}}$ to acoustic decibels $L_p = 20\log_{10}(p/p_0)$, Carbon-14 dating $t = -\frac{\ln(N/N_0) \times 5730}{\ln 2}$, and Planck's blackbody spectrum. In every single case, nature asks us to evaluate an inner ratio or exponent *first*, apply a logarithm, exponential, or power *second*, and scale by the outer constant *third*. Let us now step into the Chapter 3 Workbench and execute all thirty verified transcendental sequences on the SC-32 stack.

{{res:sc32_db_spl:screenshot|Acoustic sound pressure level 20 * log10(2 / 0.00002) = 100 dB evaluated from the inside out on the SC-32 stack.}}

### In-Place Squares, Reciprocal Roots, Dyadic Powers & `x∥y`

1. **White Dwarf Gravitational Redshift ($z \approx \frac{GM}{Rc^2}$):**  
   Climbing out of a solar-mass white dwarf ($M = 1.989 \times 10^{30}\text{ kg}$, radius $R = 6.4 \times 10^6\text{ m}$, with $G = 6.6743 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2$ and $c = 2.99792 \times 10^8\text{ m/s}$), squaring $c^2$ in place via `{{res:sc32_03_algebra_transcendentals_seq_23:keys}}` yields $z = \mathbf{{{res:sc32_03_algebra_transcendentals_seq_23:value}}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `6.6743 {{key:E}} 11 {{key:+/-}} {{key:ENTER}} 1.989 {{key:E}} 30 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.3275 \times 10^{20}$ | Gravitational parameter $G M_{\odot}$ |
| `6.4 {{key:E}} 6 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0742 \times 10^{13}$ | Divide by white dwarf radius $R$ for gravitational potential $\Phi$ |
| `2.99792 {{key:E}} 8 {{key:x²}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$2.3079 \times 10^{-4}$** | Divide by speed of light squared $c^2$ for fractional redshift $z$ |

2. **Cohesive Intermolecular Pressure Correction ($P = \frac{nRT}{V - nb} - \frac{an^2}{V^2}$):**  
   Compressing $n = 2.0\text{ mol}$ ($n^2 = 4.0\text{ mol}^2$) of real gas into $V = 0.0050\text{ m}^3$ at $T = 320.0\text{ K}$ with universal gas constant $R = 8.31446\text{ J/(mol}\cdot\text{K)}$, excluded volume $b = 4.27 \times 10^{-5}\text{ m}^3/\text{mol}$, and cohesion constant $a = 0.364\text{ Pa}\cdot\text{m}^6/\text{mol}^2$, evaluating the kinetic term first and subtracting $an^2/V^2$ via `{{res:sc32_03_algebra_transcendentals_seq_40:keys}}` confirms $P \approx \mathbf{1,024,504.15\text{ Pa}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2 {{key:ENTER}} 8.31446 {{key:×}} 320 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $5321.2544$ | Ideal kinetic energy numerator $n R T$ |
| `0.0050 {{key:ENTER}} 2 {{key:ENTER}} 4.27 {{key:E}} 5 {{key:+/-}} {{key:×}} {{key:-}} {{key:÷}}` | $5321.2544$ | $5321.2544$ | $5321.2544$ | $1082744.1501$ | Divide by free volume $(V - n b)$ for kinetic pressure term |
| `0.364 {{key:ENTER}} 4 {{key:×}} 0.0050 {{key:x²}} {{key:÷}} {{key:-}}` | $5321.2544$ | $5321.2544$ | $5321.2544$ | **$1024504.1501$** | Subtract molecular attraction term $a n^2 / V^2$ for net pressure $P$ (Pa) |

3. **RF Electromagnetic Skin Depth ($\delta = \frac{1}{\sqrt{\pi f\mu\sigma}}$):**  
   At $f = 1.0 \times 10^8\text{ Hz}$ in copper ($\sigma = 5.8 \times 10^7\text{ S/m}$, with free-space magnetic permeability $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$), multiplying inside Register $X$ and tapping `{{key:√x}} {{key:1/x}}` in `{{res:sc32_03_algebra_transcendentals_seq_41:keys}}` yields $\mathbf{{{res:sc32_03_algebra_transcendentals_seq_41:value}}\,\mu\text{m}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:π}} 1 {{key:E}} 8 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.1416 \times 10^{8}$ | Angular frequency $\pi f$ at $100\text{ MHz}$ |
| `4 {{key:π}} {{key:×}} 1 {{key:E}} 7 {{key:+/-}} {{key:×}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $394.7842$ | Multiply by magnetic permeability $\mu_0 = 4\pi \times 10^{-7}$ |
| `5.8 {{key:E}} 7 {{key:×}} {{key:√x}} {{key:1/x}}` | $0.0000$ | $0.0000$ | $0.0000$ | $6.6085 \times 10^{-6}$ | Multiply by copper conductivity $\sigma$ and take reciprocal root $\delta$ (m) |
| `1 {{key:E}} 6 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$6.6085$** | Convert skin depth $\delta$ to micrometers ($\mu\text{m}$) |

4. **Cosmic-Ray Muon Time Dilation ($\gamma = \frac{1}{\sqrt{1 - (v/c)^2}}$):**  
   Hurtling through the stratosphere at $\beta = v/c = 0.85$, keying `{{res:sc32_03_algebra_transcendentals_seq_42:keys}}` resolves the Lorentz factor to **`{{res:sc32_03_algebra_transcendentals_seq_42:value}}`** while preserving the length-contraction ratio $1/\gamma = 0.5268$ in `{{key:LASTX}}`.

5. **Dyadic Powers (`yˣ`, `ˣ√y`), Harmonic Speed (`x∥y`) & the 13-Keystroke Quadratic Sprint:**  
   * **Fractional Power Scaling ($\Phi = 2.5^{3.8}$):** Loading base $2.5$ into Register $Y$ and exponent $3.8$ into Register $X$ via `{{res:sc32_03_algebra_transcendentals_seq_01:keys}}` produces **`{{res:sc32_03_algebra_transcendentals_seq_01:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:2}} {{key:.}} {{key:5}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.5000$ | Enter base $y$ |
| `{{key:ENTER}}` | $0.0000$ | $0.0000$ | $2.5000$ | $2.5000$ | Stack lift disabled; $y$ pushed to $Y$ |
| `{{key:3}} {{key:.}} {{key:8}}` | $0.0000$ | $0.0000$ | $2.5000$ | $3.8000$ | Overwrite $X$ with exponent $x$ |
| `{{key:yˣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$32.5216096641$** | Evaluates $2.5^{3.8}$; Stack lift armed |

   * **Polytropic Gas Compression Work ($W = \frac{P_1 V_1}{n-1}[(V_1/V_2)^{n-1} - 1]$):** Compressing a gas across volume ratio $V_1/V_2 = 4.0$ with polytropic exponent $n - 1 = 0.32$ and pre-factor $P_1 V_1 / (n-1) = 15,000\text{ J}$, `{{res:sc32_03_algebra_transcendentals_seq_34:keys}}` yields **`{{res:sc32_03_algebra_transcendentals_seq_34:value}}`** $\text{J}$.
   * **Kepler's Third Law for Mars ($a = \sqrt[3]{T^2}$) & Round-Trip Harmonic Speed ($2(v_1 \parallel v_2)$):** Given Mars's orbital period $T = 1.8808\text{ yr}$, keying `1.8808 {{key:x²}} 3 {{key:ˣ√y}}` squares $T$ in place ($\to 3.5374$) and extracts the cube root to return Mars's semi-major axis $a = \mathbf{1.5237\text{ AU}}$. And for the round-trip harmonic speed puzzle ($30\text{ mph}$ uphill and $60\text{ mph}$ downhill), keying `30 {{key:ENTER}} 60 {{key:x∥y}} 2 {{key:×}}` forms $30 \parallel 60 = 20\text{ mph}$ in one stroke of `{{key:x∥y}}` and doubles it to $\mathbf{40.0000\text{ mph}}$.
   * **Stretched-Exponential Boundary-Layer Profile ($f(v) = \frac{k}{c}(v/c)^{k-1}\exp[-(v/c)^k]$):** At wind speed $v = 8.5\text{ m/s}$, scale velocity $c = 9.0\text{ m/s}$, and shape parameter $k = 2.2$, duplicating $v/c = 0.9444$ across the stack via `{{res:sc32_03_algebra_transcendentals_seq_29:keys}}` confirms $\mathbf{0.094496\text{ (m/s)}^{-1}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `8.5 {{key:ENTER}} 9.0 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.9444$ | Normalized velocity ratio $v/c$ |
| `{{key:ENTER}} {{key:ENTER}} 2.2 {{key:yˣ}} {{key:+/-}} {{key:eˣ}}` | $0.0000$ | $0.0000$ | $0.9444$ | $0.4140$ | Stretched exponential factor $\exp(-(v/c)^k)$ |
| `{{key:x⇄y}} 1.2 {{key:yˣ}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.3866$ | Multiply by power-law velocity term $(v/c)^{k-1}$ |
| `2.2 {{key:ENTER}} 9.0 {{key:÷}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.0945$** | Scale by shape/scale ratio $k/c$ for density $f(v)$ |

   * **13-Keystroke Quadratic Sprint ($2.4 x^2 + 7.8 x - 15.6 = 0$):** Evaluating the discriminant $\sqrt{b^2 - 4ac} = \sqrt{7.8^2 - 4(2.4)(-15.6)} = 14.5121$ from the inside out first (`7.8 {{key:x²}} 4 {{key:ENTER}} 2.4 {{key:×}} 15.6 {{key:×}} {{key:+}} {{key:√x}}`), subtracting $b = 7.8$, and dividing by $2a = 4.8$ via `{{res:sc32_03_algebra_quadratic_sprint:keys}}` delivers $x_+ =$ **`{{res:sc32_03_algebra_quadratic_sprint:value}}`** in 13 keystrokes without touching a storage register.

### Base-10 & Natural Logarithms (`LOG`, `LN`)

1. **Stadium Sound Pressure Level ($L_p = 20\log_{10}(p_{\text{rms}}/p_0)$), 60 dB ($10^{-6}$) Acoustic Energy Decay Preview, and Buffer $\text{pH}$:**  
   Measuring an acoustic wave of $p_{\text{rms}} = 1.45\text{ Pa}$ relative to the human hearing threshold $p_0 = 2.0 \times 10^{-5}\text{ Pa}$, `{{res:sc32_03_algebra_transcendentals_seq_02:keys}}` resolves $L_p =$ **`{{res:sc32_03_algebra_transcendentals_seq_02:value}}`** $\text{dB SPL}$. As a preview of **Chapter 13's** architectural acoustics case study—where a $60\text{ dB}$ ($10^{-6}$) decay in sound energy ($\ln(10^6) = 6\ln 10 \approx 13.8155$) sets the $0.161\text{ s/m}$ reverberation constant across a room of volume $V = 4,500\text{ m}^3$ and acoustic absorption $A = 320.0\text{ Sabins}$—keying `{{res:sc32_03_algebra_transcendentals_seq_21:keys}}` yields $T_{60} =$ **`{{res:sc32_03_algebra_transcendentals_seq_21:value}}`** $\text{s}$. And in an acetic acid buffer ($\text{pK}_a = 4.76$, $[\text{A}^-] = 0.185\text{ M}$, $[\text{HA}] = 0.120\text{ M}$), `{{res:sc32_03_algebra_transcendentals_seq_03:keys}}` yields $\text{pH} =$ **`{{res:sc32_03_algebra_transcendentals_seq_03:value}}`**.

2. **Willard Libby's Carbon-14 Radiometric Dating ($t = -\frac{\ln(0.234) \times 5730}{\ln 2}$):**  
   Executing `{{res:sc32_03_algebra_transcendentals_seq_44:keys}}` dates the Ice Age hearth specimen to **$12,006.75\text{ years}$**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0.234 {{key:LN}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-1.4524$ | Evaluate natural logarithm $\ln(0.234)$ of surviving $^{14}\text{C}$ fraction |
| `5730 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-8322.4478$ | Multiply by Cambridge carbon-14 half-life ($t_{1/2} = 5,730\text{ yr}$) |
| `2 {{key:LN}}` | $0.0000$ | $0.0000$ | $-8322.4478$ | $0.6931$ | Lift numerator to $Y$ and form half-life decay divisor $\ln(2)$ in $X$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-12006.7541$ | Divide by $\ln(2)$ to convert natural decay units into elapsed years |
| `{{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$12006.7541$** | Negate decay sign for positive radiometric specimen age (years) |

3. **Potassium-Argon Geochronology ($t = \frac{1}{\lambda}\ln\left(1 + C\frac{^{40}\text{Ar}}{^{40}\text{K}}\right)$), Exponential Relaxation ($\tau = 7.05\text{ s}$), and Exact Logarithmic Doubling:**  
   Dating a Precambrian basalt core with measured daughter-to-parent isotope ratio $^{40}\text{Ar}/{}^{40}\text{K} = 0.0850$ (where $C = \lambda_{\text{total}}/\lambda_{\text{EC}} = 9.54$ is the $^{40}\text{K} \to {}^{40}\text{Ar}$ electron-capture branching factor and $\lambda = 5.543 \times 10^{-10}\text{ yr}^{-1}$ is the total decay rate), `{{res:sc32_03_algebra_transcendentals_seq_06:keys}}` resolves the rock's solidification age to **`{{res:sc32_03_algebra_transcendentals_seq_06:value}}`** years ($1.071\text{ billion years}$). Watching a thermal or RC system relax to $10\%$ of its initial excess with time constant $\tau = (150 \times 10^3)(47 \times 10^{-6}) = 7.05\text{ s}$, `{{res:sc32_03_algebra_transcendentals_seq_05:keys}}` yields **`{{res:sc32_03_algebra_transcendentals_seq_05:value}}`** seconds:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `150000 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $150000.000$ | $150000.000$ | Load scale factor $150,000$ |
| `47 {{key:E}} 6 {{key:+/-}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $7.050000$ | Relaxation time constant $\tau = 7.05\text{ s}$ |
| `0.10 {{key:LN}}` | $0.0000$ | $0.0000$ | $7.050000$ | $-2.302585$ | $\ln(0.10)$ natural logarithm |
| `{{key:×}} {{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$16.233225$** | Relaxation time in seconds |

   And compounding at an annual growth rate of $r = 7.2\%$, exact logarithmic doubling $t = \frac{\ln 2}{\ln(1.072)}$ via `{{res:sc32_03_algebra_transcendentals_seq_25:keys}}` resolves to **`{{res:sc32_03_algebra_transcendentals_seq_25:value}}`** years (a benchmark we will revisit in **Chapter 11** when we derive the classical Rule of 72).

### Natural Exponentials (`eˣ`) in Kinetics, Atmospheres & Quantum Physics

1. **Arrhenius Activation Energy ($E_a = \frac{R\ln(k_2/k_1)}{1/T_1 - 1/T_2}$) & Carbon Diffusion in Steel ($D = D_0 e^{-Q/RT}$):**  
   * **Two-Temperature Arrhenius Activation Barrier:** Heating a reaction from $T_1 = 300\text{ K}$ ($k_1 = 3.25 \times 10^{-4}\text{ s}^{-1}$) to $T_2 = 350\text{ K}$ ($k_2 = 2.85 \times 10^{-2}\text{ s}^{-1}$), keying `{{res:sc32_03_algebra_transcendentals_seq_45:keys}}` first forms the reciprocal-temperature difference $(1/T_1 - 1/T_2) \approx 0.000476\text{ K}^{-1}$ in Register $X$. Next, `{{res:sc32_03_algebra_transcendentals_seq_46:keys}}` computes the scaled logarithmic rate ratio $R\ln(k_2/k_1) = \mathbf{{{res:sc32_03_algebra_transcendentals_seq_46:value}}\text{ J/(mol}\cdot\text{K)}}$ while $(1/T_1 - 1/T_2)$ waits in Register $Y$, so `{{key:x⇄y}} {{key:÷}} 1000 {{key:÷}}` reveals the activation energy $E_a = \mathbf{78.1148\text{ kJ/mol}}$.
   * **Solid-State Carbon Diffusion in Austenite Steel:** At furnace temperature $T = 1,200\text{ K}$ ($Q = 148,000\text{ J/mol}$, $D_0 = 2.3 \times 10^{-5}\text{ m}^2/\text{s}$, $R = 8.31446\text{ J/(mol}\cdot\text{K)}$), `{{res:sc32_03_algebra_transcendentals_seq_15:keys}}` yields diffusivity $D =$ **`{{res:sc32_03_algebra_transcendentals_seq_15:value}}`** $\text{m}^2/\text{s}$.

2. **Clausius-Clapeyron Boiling Pressure & Mauna Kea Barometric Altimetry:**  
   At $T = 333.15\text{ K}$ ($60^\circ\text{C}$) relative to $T_0 = 373.15\text{ K}$ ($100^\circ\text{C}$, $P_0 = 101.325\text{ kPa}$, $\Delta H_{\text{vap}} = 40,660\text{ J/mol}$), `{{res:sc32_03_algebra_transcendentals_seq_19:keys}}` resolves vapor pressure to $\mathbf{21.0063\text{ kPa}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `333.15 {{key:1/x}} 373.15 {{key:1/x}} {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.2176 \times 10^{-4}$ | Reciprocal temperature differential $(1/T_1 - 1/T_2)$ |
| `40660 {{key:ENTER}} 8.31446 {{key:÷}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.5735$ | Scale by enthalpy of vaporization $\Delta H_{\text{vap}}/R$ |
| `{{key:+/-}} {{key:eˣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.2073$ | Clausius-Clapeyron exponential pressure factor |
| `101.325 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$21.0063$** | Scale by reference pressure $P_1$ for vapor pressure $P_2$ (kPa) |

   And climbing to the summit of Mauna Kea ($h = 4,207\text{ m}$, with dry-air molar mass $M = 0.0289644\text{ kg/mol}$, gravity $g = 9.80665\text{ m/s}^2$, gas constant $R = 8.314462\text{ J/(mol}\cdot\text{K)}$, sea-level temperature $T_0 = 288.15\text{ K}$, and baseline pressure $P_0 = 1013.25\text{ hPa}$, giving dimensionless scale height ratio $\kappa = \frac{Mgh}{RT_0} \approx 0.4988$), keying `0.0289644 {{key:ENTER}} 9.80665 {{key:×}} 4207 {{key:×}} 8.314462 {{key:÷}} 288.15 {{key:÷}}` followed by `{{res:sc32_03_algebra_transcendentals_seq_47:keys}}` yields summit pressure $X = \mathbf{615.3168\text{ hPa}}$.

3. **Shockley Diode Law, Silicon Bandgap Carriers & Planck's Blackbody Spectrum:**  
   Biasing a silicon p-n junction at forward voltage $V = 0.58\text{ V}$ (ideality factor $n = 1.25$, thermal voltage $V_t = 0.025852\text{ V}$, saturation current $I_s = 1.8 \times 10^{-11}\text{ A}$), `{{res:sc32_03_algebra_transcendentals_seq_09:keys}}` yields **`{{res:sc32_03_algebra_transcendentals_seq_09:value}}`** $\text{A}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0.58 {{key:ENTER}} 1.25 {{key:÷}} 0.025852 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $17.9483$ | Chain division for diode activation argument $V/(n V_t)$ |
| `{{key:eˣ}} 1 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $6.2353 \times 10^{7}$ | Exponential emission factor $(e^{V/nV_t} - 1)$ |
| `1.8 {{key:E}} 11 {{key:+/-}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.0011$** | Scale by saturation current $I_s$ for forward current $I$ (A) |

   Thermally exciting intrinsic carriers $n_i = B T^{3/2} \exp(-E_g / 2kT)$ across the silicon bandgap ($E_g = 1.12\text{ eV}$) at room temperature $T = 300\text{ K}$ (with Boltzmann constant $k = 8.61733 \times 10^{-5}\text{ eV/K}$ and density-of-states coefficient $B = 5.23 \times 10^{15}\text{ cm}^{-3}\text{K}^{-3/2}$), `{{res:sc32_03_algebra_transcendentals_seq_14:keys}}` resolves $n_i \approx \mathbf{1.0631 \times 10^{10}\text{ cm}^{-3}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1.12 {{key:ENTER}} 2 {{key:ENTER}} 8.61733 {{key:E}} 5 {{key:+/-}} {{key:×}} 300 {{key:×}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $21.6618$ | Bandgap thermal activation exponent $E_g/(2 k T)$ |
| `{{key:+/-}} {{key:eˣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.9121 \times 10^{-10}$ | Boltzmann activation factor $\exp(-E_g/2kT)$ |
| `300 {{key:ENTER}} 1.5 {{key:yˣ}} {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0328 \times 10^{-6}$ | Scale by density-of-states temperature factor $T^{3/2}$ |
| `5.23 {{key:E}} 15 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$1.0631 \times 10^{10}$** | Multiply by material coefficient for intrinsic carrier density $n_i$ ($\text{cm}^{-3}$) |

   And evaluating Max Planck's solar blackbody spectral radiance $B_\lambda(T) = \frac{c_1}{\lambda^5(e^x - 1)}$ at green wavelength $\lambda = 500\text{ nm} = 5.0 \times 10^{-7}\text{ m}$ (with first radiation constant $c_1 = 2hc^2 = 1.19104 \times 10^{-16}\text{ W}\cdot\text{m}^2/\text{sr}$ and dimensionless photon-energy ratio $x = \frac{hc}{\lambda kT} = 4.98020$), `{{res:sc32_03_algebra_transcendentals_seq_13:keys}}` resolves $B_\lambda \approx \mathbf{2.6375 \times 10^{13}\text{ W}/(\text{m}^3\cdot\text{sr})}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4.98020 {{key:eˣ}} 1 {{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $144.5035$ | Planck photon distribution denominator $(e^x - 1)$ |
| `1.19104 {{key:E}} 16 {{key:+/-}} {{key:ENTER}}` | $0.0000$ | $144.5035$ | $1.1910 \times 10^{-16}$ | $1.1910 \times 10^{-16}$ | Load first radiation constant $2hc^2$ |
| `5.0 {{key:E}} 7 {{key:+/-}} {{key:ENTER}} 5 {{key:yˣ}}` | $144.5035$ | $144.5035$ | $1.1910 \times 10^{-16}$ | $3.1250 \times 10^{-32}$ | Raise wavelength to fifth power $\lambda^5$ |
| `{{key:÷}}` | $144.5035$ | $144.5035$ | $144.5035$ | $3.8113 \times 10^{15}$ | Divide radiation constant $c_1$ by $\lambda^5$ |
| `{{key:x⇄y}} {{key:÷}}` | $144.5035$ | $144.5035$ | $144.5035$ | **$2.6375 \times 10^{13}$** | Divide spectral power by photon denominator for radiance $B_\lambda$ |

### Factorials (`x!`), Lanczos Gamma, and Domain Guard Verification

* **16-Channel Photonic Crossbar Permutations ($16!$):** Evaluating `{{res:sc32_03_algebra_transcendentals_seq_30:keys}}` computes $16!$ in place to display **`{{res:sc32_03_algebra_transcendentals_seq_30:value}}`** ($20,922,789,888,000$).
* **Half-Integer Gamma Verification ($\left(\frac{1}{2}\right)! = \frac{\sqrt{\pi}}{2}$):** Evaluating `{{res:sc32_03_algebra_transcendentals_seq_48:keys}}` (or decimal `{{res:sc32_03_algebra_transcendentals_seq_04:keys}}` $\to$ **`{{res:sc32_03_algebra_transcendentals_seq_04:value}}`**) matches Gauss's analytical constant `{{res:sc32_03_algebra_transcendentals_seq_49:keys}}` $\to$ **`{{res:sc32_03_algebra_transcendentals_seq_49:value}}`** to all 12 displayed digits.
* **5D Unit Hypersphere Volume ($V_5 = \frac{\pi^{2.5}}{(2.5)!} = \frac{8}{15}\pi^2$):** Raising $\pi$ to the $2.5$ power and dividing by Lanczos's fractional factorial $(2.5)!$ via `{{res:sc32_03_algebra_transcendentals_seq_31:keys}}` yields **`{{res:sc32_03_algebra_transcendentals_seq_31:value}}`**.
* **Non-Destructive Domain Protection:** Attempting a real logarithm of a negative number via `{{res:sc32_03_algebra_transcendentals_seq_50:keys}}` halts with `INVALID DATA` (Code 02) before altering Registers $Y, Z,$ or $T$; tapping `{{key:C}}` clears the banner cleanly.

---

### From Straight-Line Growth to the Circle

In Chapter 3, we watched John Napier's logarithms and Leonhard Euler's natural exponential $e^x$ tame continuous growth and decay along a straight line—measuring everything from the age of the Dead Sea Scrolls and the cooling of a morning cup of coffee to the roar of a stadium and the combinations of a shuffled deck of cards.

Yet nature does not merely grow along a straight line. Planets sweep around ellipses, ocean waves rise and fall, pendulums swing, and aircraft crab into crosswinds across a curved Earth. What happens when we wrap a straight number line around a **circle**? In **[Chapter 4: Measuring the Cosmos with a Shadow](04-trig-vectors-polar.md)**, our story opens in 240 BC in Alexandria, where Eratosthenes measured the circumference of the entire Earth using the noon shadow of a single vertical bronze stick.
