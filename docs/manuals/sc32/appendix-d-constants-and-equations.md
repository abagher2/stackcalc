---
title: "Appendix D: Constants, Equations & Worked-Example Keystroke Directory | Thinking in the Stack (SC-32)"
description: "Authoritative reference directory of mathematical constants, exact 2019 SI and CODATA physical constants, BIPM SI prefixes, and complete chapter-by-chapter worked-example keystroke sequences on the StackCalc SC-32."
---

# Appendix D: Constants, Equations & Worked-Example Keystroke Directory

This directory compiles the operational register hierarchy of the StackCalc SC-32, fundamental mathematical invariants, exact 2019 SI and CODATA 2022 physical constants, BIPM metric prefixes, exact international unit conversion factors, and the complete worked-example keystroke sequences.

## Operational Register Hierarchy

The SC-32 register architecture partitions storage across the operational stack, recovery buffer, statistical accumulators, global variables, indirect pointer, financial registers, and symbolic equation bank:

| Register / Bank | Architectural Level | Operational Role & Data Flow |
| :--- | :--- | :--- |
| **Register T** | Top / Constant Buffer | Retains constant factor and replicates on dyadic stack drop (`4-LVL` mode) |
| **Register Z** | Third Stack Level | Holds intermediate sub-expressions and vector/matrix terms |
| **Register Y** | Second Stack Level | Stores waiting dyadic base, dividend, or real/polar coordinate component |
| **Register X** | Active / Display | Direct keyboard entry and live computed result readout |
| **LASTX** | Recovery Buffer | Captures previous $X$ before arithmetic and transcendental operations |
| **STATS Bank** | 6 Accumulators | Hardware registers ($n, \Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy$ at $R_{28}\dots R_{33}$) |
| **Memory A–Z** | 26 Global Registers | Persistent variable storage via `{{key:STO}}` and `{{key:RCL}}` (indirect slots `R1`–`R26`) |
| **Index `i` & `(i)`** | 89-Slot Pointer | Indirect pointer `i` (`R27`) addressing `A`–`Z`, `STATS`, `POLY` roots (`R34`–`R39`), and `DATA0`–`DATA49` (`R40`–`R89`) |
| **TVM Bank** | 5 Financial Registers | Dedicated actuarial workspace `N`, `I%`, `PV`, `PMT`, `FV` (`END`/`BEG` mode) |
| **EQN Bank** | 24 Equation Slots | Non-volatile RPN equation storage evaluated via `{{key:XEQ}}`, `{{key:SOLVE}}`, and `{{key:∫}}` |

## Fundamental Mathematical Constants

Physical constants spanning many orders of magnitude are entered as atomic floating-point literals via `{{key:E}}` (for example, `6.62607015 {{key:E}} 34 {{key:+/-}}` for Planck's constant $h$), keeping Registers $Y, Z,$ and $T$ undisturbed:

| Constant Name | Symbol | Exact Value (15-Digit Reference) | SC-32 RPN Entry Sequence |
| :--- | :---: | :--- | :--- |
| **Archimedes' Constant** | $\pi$ | `3.14159265358979` | `{{key:π}}` |
| **Euler's Number (Natural Base)** | $e$ | `2.71828182845905` | `1 {{key:eˣ}}` |
| **Golden Ratio** ($\frac{1+\sqrt{5}}{2}$) | $\varphi$ | `1.61803398874989` | `5 {{key:√x}} 1 {{key:+}} 2 {{key:÷}}` |
| **Euler–Mascheroni Constant** | $\gamma$ | `0.57721566490153` | `0.57721566490153` |
| **Natural Logarithm of 2** | $\ln 2$ | `0.69314718055995` | `2 {{key:LN}}` |
| **Natural Logarithm of 10** | $\ln 10$ | `2.30258509299405` | `10 {{key:LN}}` |
| **Common Logarithm of $e$** | $\log_{10} e$ | `0.43429448190325` | `1 {{key:eˣ}} {{key:LOG}}` |
| **Pythagorean Constant** | $\sqrt{2}$ | `1.41421356237310` | `2 {{key:√x}}` |
| **Theodorus' Constant** | $\sqrt{3}$ | `1.73205080756888` | `3 {{key:√x}}` |
| **Diagonal of Unit Golden Rectangle** | $\sqrt{5}$ | `2.23606797749979` | `5 {{key:√x}}` |
| **Radians-to-Degrees Factor** ($\frac{180}{\pi}$) | $\text{rad}\to\text{deg}$ | `57.2957795130823` | `1 {{key:▸DEG}}` |
| **Degrees-to-Radians Factor** ($\frac{\pi}{180}$) | $\text{deg}\to\text{rad}$ | `0.01745329251994` | `1 {{key:▸RAD}}` |

## Exact 2019 SI & CODATA 2022 Physical Constants

Under the May 20, 2019 SI Redefinition (26th CGPM), seven defining constants ($c, h, e, k_B, N_A, \Delta\nu_{\text{Cs}}, K_{\text{cd}}$) and their combinations ($R = N_A k_B$, $F = N_A e$, $\sigma = \frac{2\pi^5 k_B^4}{15 c^2 h^3}$) are exact numerical invariants, complemented by CODATA 2022 constants:

| Physical Constant | Symbol | Numerical Value & SI Unit | Status | SC-32 RPN Entry Sequence |
| :--- | :---: | :--- | :---: | :--- |
| **Speed of Light in Vacuum** | $c$ | $299{,}792{,}458\text{ m/s}$ | Exact | `299792458` |
| **Planck Constant** | $h$ | $6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}$ | Exact | `6.62607015 {{key:E}} 34 {{key:+/-}}` |
| **Reduced Planck Constant** ($h/2\pi$) | $\hbar$ | $1.054571817 \times 10^{-34}\text{ J}\cdot\text{s}$ | Exact | `6.62607015 {{key:E}} 34 {{key:+/-}} {{key:ENTER}} 2 {{key:÷}} {{key:π}} {{key:÷}}` |
| **Elementary Charge** | $e$ | $1.602176634 \times 10^{-19}\text{ C}$ | Exact | `1.602176634 {{key:E}} 19 {{key:+/-}}` |
| **Boltzmann Constant** | $k_B$ | $1.380649 \times 10^{-23}\text{ J/K}$ | Exact | `1.380649 {{key:E}} 23 {{key:+/-}}` |
| **Avogadro Constant** | $N_A$ | $6.02214076 \times 10^{23}\text{ mol}^{-1}$ | Exact | `6.02214076 {{key:E}} 23` |
| **Molar Gas Constant** ($N_A k_B$) | $R$ | $8.314462618\text{ J/(mol}\cdot\text{K)}$ | Exact | `8.314462618` |
| **Faraday Constant** ($N_A e$) | $F$ | $96{,}485.33212\text{ C/mol}$ | Exact | `96485.33212` |
| **Stefan–Boltzmann Constant** | $\sigma$ | $5.670374419 \times 10^{-8}\text{ W/(m}^2\cdot\text{K}^4)$ | Exact | `5.670374419 {{key:E}} 8 {{key:+/-}}` |
| **Standard Acceleration of Gravity** | $g_0$ | $9.80665\text{ m/s}^2$ | Exact | `9.80665` |
| **Standard Atmosphere** | $\text{atm}$ | $101{,}325\text{ Pa}$ | Exact | `101325` |
| **Newtonian Gravitational Constant** | $G$ | $6.67430 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2$ | CODATA | `6.67430 {{key:E}} 11 {{key:+/-}}` |
| **Geocentric Gravitational Parameter** | $\mu_\oplus$ | $3.986004418 \times 10^{14}\text{ m}^3/\text{s}^2$ | IAU/IUGG | `3.986004418 {{key:E}} 14` |
| **Vacuum Electric Permittivity** | $\varepsilon_0$ | $8.8541878188 \times 10^{-12}\text{ F/m}$ | CODATA | `8.8541878188 {{key:E}} 12 {{key:+/-}}` |
| **Vacuum Magnetic Permeability** | $\mu_0$ | $1.25663706127 \times 10^{-6}\text{ N/A}^2$ | CODATA | `1.25663706127 {{key:E}} 6 {{key:+/-}}` |
| **Coulomb Constant** ($1/4\pi\varepsilon_0$) | $k_e$ | $8.9875517923 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$ | CODATA | `8.9875517923 {{key:E}} 9` |
| **Electron Rest Mass** | $m_e$ | $9.1093837139 \times 10^{-31}\text{ kg}$ | CODATA | `9.1093837139 {{key:E}} 31 {{key:+/-}}` |
| **Proton Rest Mass** | $m_p$ | $1.67262192595 \times 10^{-27}\text{ kg}$ | CODATA | `1.67262192595 {{key:E}} 27 {{key:+/-}}` |
| **Unified Atomic Mass Constant** | $u$ | $1.66053906892 \times 10^{-27}\text{ kg}$ | CODATA | `1.66053906892 {{key:E}} 27 {{key:+/-}}` |
| **Rydberg Constant** | $R_\infty$ | $1.097373156816 \times 10^7\text{ m}^{-1}$ | CODATA | `1.097373156816 {{key:E}} 7` |

## BIPM SI Prefixes & Exact International Unit Conversions

The twenty-four BIPM metric prefixes (spanning $10^{30}$ `quetta` to $10^{-30}$ `quecto`) and exact international unit conversion factors map to `{{key:E}}` scientific exponent entry and the SC-32's dedicated conversion keys:

| Macro Prefix | Symbol | Factor | SC-32 Keystroke | Micro Prefix | Symbol | Factor | SC-32 Keystroke |
| :--- | :---: | :---: | :--- | :--- | :---: | :---: | :--- |
| **quetta** | `Q` | $10^{30}$ | `1 {{key:E}} 30` | **deci** | `d` | $10^{-1}$ | `1 {{key:E}} 1 {{key:+/-}}` |
| **ronna** | `R` | $10^{27}$ | `1 {{key:E}} 27` | **centi** | `c` | $10^{-2}$ | `1 {{key:E}} 2 {{key:+/-}}` |
| **yotta** | `Y` | $10^{24}$ | `1 {{key:E}} 24` | **milli** | `m` | $10^{-3}$ | `1 {{key:E}} 3 {{key:+/-}}` |
| **zetta** | `Z` | $10^{21}$ | `1 {{key:E}} 21` | **micro** | `μ` | $10^{-6}$ | `1 {{key:E}} 6 {{key:+/-}}` |
| **exa** | `E` | $10^{18}$ | `1 {{key:E}} 18` | **nano** | `n` | $10^{-9}$ | `1 {{key:E}} 9 {{key:+/-}}` |
| **peta** | `P` | $10^{15}$ | `1 {{key:E}} 15` | **pico** | `p` | $10^{-12}$ | `1 {{key:E}} 12 {{key:+/-}}` |
| **tera** | `T` | $10^{12}$ | `1 {{key:E}} 12` | **femto** | `f` | $10^{-15}$ | `1 {{key:E}} 15 {{key:+/-}}` |
| **giga** | `G` | $10^{9}$ | `1 {{key:E}} 9` | **atto** | `a` | $10^{-18}$ | `1 {{key:E}} 18 {{key:+/-}}` |
| **mega** | `M` | $10^{6}$ | `1 {{key:E}} 6` | **zepto** | `z` | $10^{-21}$ | `1 {{key:E}} 21 {{key:+/-}}` |
| **kilo** | `k` | $10^{3}$ | `1 {{key:E}} 3` | **yocto** | `y` | $10^{-24}$ | `1 {{key:E}} 24 {{key:+/-}}` |
| **hecto** | `h` | $10^{2}$ | `1 {{key:E}} 2` | **ronto** | `r` | $10^{-27}$ | `1 {{key:E}} 27 {{key:+/-}}` |
| **deka** | `da` | $10^{1}$ | `1 {{key:E}} 1` | **quecto** | `q` | $10^{-30}$ | `1 {{key:E}} 30 {{key:+/-}}` |

| Physical Quantity | From Unit | To SI Unit | Exact Defining Factor / Formula | Dedicated SC-32 Key |
| :--- | :--- | :--- | :--- | :--- |
| **Length** | Inch (`in`) | Centimeter (`cm`) / Meter (`m`) | $1\text{ in} \equiv 2.54\text{ cm} \equiv 0.0254\text{ m}$ (exact) | `{{key:▸cm}}` / `{{key:▸in}}` |
| **Length** | Foot (`ft`) | Meter (`m`) | $1\text{ ft} \equiv 0.3048\text{ m}$ (exact) | `0.3048 {{key:×}}` |
| **Length** | Statute Mile (`mi`) | Kilometer (`km`) | $1\text{ mi} \equiv 1.609344\text{ km}$ (exact) | `{{key:▸km}}` / `{{key:▸mi}}` |
| **Length** | Nautical Mile (`nmi`) | Meter (`m`) | $1\text{ nmi} \equiv 1852\text{ m}$ (exact) | `1852 {{key:×}}` |
| **Length** | Astronomical Unit (`au`) | Meter (`m`) | $1\text{ au} \equiv 149{,}597{,}870{,}700\text{ m}$ (exact) | `1.495978707 {{key:E}} 11 {{key:×}}` |
| **Mass** | Avoirdupois Pound (`lb`) | Kilogram (`kg`) | $1\text{ lb} \equiv 0.45359237\text{ kg}$ (exact) | `{{key:▸kg}}` / `{{key:▸lb}}` |
| **Volume** | U.S. Liquid Gallon (`gal`) | Liter (`L`) | $1\text{ gal} \equiv 3.785411784\text{ L}$ (exact, $231\text{ in}^3$) | `{{key:▸l}}` / `{{key:▸gal}}` |
| **Pressure** | Standard Atmosphere (`atm`) | Pascal (`Pa`) | $1\text{ atm} \equiv 101{,}325\text{ Pa}$ (exact) | `101325 {{key:×}}` |
| **Pressure** | Millimeter of Mercury (`Torr`) | Pascal (`Pa`) | $1\text{ Torr} \equiv \frac{101{,}325}{760}\text{ Pa} \approx 133.322368\text{ Pa}$ | `101325 {{key:ENTER}} 760 {{key:÷}} {{key:×}}` |
| **Energy** | Thermochemical Calorie (`cal`) | Joule (`J`) | $1\text{ cal}_{\text{th}} \equiv 4.184\text{ J}$ (exact) | `4.184 {{key:×}}` |
| **Energy** | Electronvolt (`eV`) | Joule (`J`) | $1\text{ eV} \equiv 1.602176634 \times 10^{-19}\text{ J}$ (exact) | `1.602176634 {{key:E}} 19 {{key:+/-}} {{key:×}}` |
| **Power** | Mechanical Horsepower (`hp`) | Watt (`W`) | $1\text{ hp} \equiv 550\text{ ft}\cdot\text{lbf/s} \approx 745.699872\text{ W}$ | `745.699872 {{key:×}}` |
| **Temperature** | Fahrenheit (`°F`) | Celsius (`°C`) | $T_{\text{C}} = (T_{\text{F}} - 32) \times \frac{5}{9}$ (exact) | `{{key:▸°C}}` / `{{key:▸°F}}` |
| **Temperature** | Celsius (`°C`) | Kelvin (`K`) | $T_{\text{K}} = T_{\text{C}} + 273.15$ (exact) | `273.15 {{key:+}}` |
| **Time / Angle** | Sexagesimal (`H.MMSS`) | Decimal (`HR` / `DEG`) | $H + \frac{M}{60} + \frac{S}{3600}$ | `{{key:▸HR}}` / `{{key:▸HMS}}` |
| **Plane Angle** | Degree (`deg`) | Radian (`rad`) | $\theta_{\text{rad}} = \theta_{\text{deg}} \times \frac{\pi}{180}$ | `{{key:▸RAD}}` / `{{key:▸DEG}}` |
| **Coordinates** | Rectangular $(x, y)$ | Polar $(r, \theta)$ | $r = \sqrt{x^2+y^2},\; \theta = \operatorname{atan2}(y, x)$ | `{{key:▸θ,r}}` / `{{key:▸y,x}}` |

---

## Standard Library Reference Equations

The Standard Library formulas across Chapters 1–14 derive from eight governing analytical identities **(Eq. D.1)**–**(Eq. D.8)**:

* **Eq. D.1 — Harmonic Parallel Synthesis (Electrical Impedance, Thin Lenses & Work-Rate Networks):** Combines two reciprocal-adding quantities $x$ and $y$ (such as parallel resistors $R_1 \dots R_n$, series capacitors, or optical object/image distances) into their equivalent harmonic product $x \parallel y$ by dividing the product $yx$ by the sum $y + x$:

$$x \parallel y = \left(x^{-1} + y^{-1}\right)^{-1} = \frac{y x}{y + x}, \qquad R_{\text{eq}} = R_1 \parallel R_2 \parallel \dots \parallel R_n$$

* **Eq. D.2 — Planar Vector & Complex Phasor Euler Transformation:** Maps a 2D vector or AC impedance phasor $z$ between rectangular components $(x, y)$ (real resistance $x$, imaginary reactance $y$) and polar coordinates $(r, \theta)$ (Euclidean magnitude $r$ and four-quadrant phase angle $\theta$):

$$z = x + i y = r e^{i\theta} = r(\cos\theta + i\sin\theta), \qquad r = \sqrt{x^2 + y^2}, \qquad \theta = \operatorname{atan2}(y, x)$$

* **Eq. D.3 — Chemical Thermodynamics, Nernst Electrochemistry & Arrhenius Kinetics:** Links reaction Gibbs free energy $\Delta G$ (from standard state $\Delta G^\circ$) and electrochemical cell potential $E$ (from standard potential $E^\circ$ across $n$ moles of electrons and Faraday constant $F$) to the reaction quotient $Q$ at absolute temperature $T$ and gas constant $R$, alongside the exponential Arrhenius rate constant $k(T)$ governed by pre-exponential collision frequency $A$ and activation energy barrier $E_a$:

$$\Delta G = \Delta G^\circ + R T \ln Q, \qquad E = E^\circ - \frac{R T}{n F}\ln Q, \qquad k(T) = A \exp\!\left(-\frac{E_a}{R T}\right)$$

* **Eq. D.4 — Simpson's Prismoidal Solid Volume & Steiner's Parallel-Axis Inertia:** Evaluates the exact volume $V_{\text{prismoid}}$ of a solid of height $h$ from its bottom, mid-height, and top cross-sectional areas ($A_{\text{bottom}}, A_{\text{mid}}, A_{\text{top}}$), and shifts a body's center-of-mass moment of inertia $I_{\text{cm}}$ across a parallel axis offset by distance $d$ by adding the transfer term $m d^2$ (or $A d^2$ for planar cross-sections):

$$V_{\text{prismoid}} = \frac{h}{6}\bigl(A_{\text{bottom}} + 4A_{\text{mid}} + A_{\text{top}}\bigr), \qquad I_{\text{axis}} = I_{\text{cm}} + m d^2$$

* **Eq. D.5 — Horner's Nested Polynomial Evaluation:** Factors a degree-$n$ polynomial $P(x)$ with coefficients $a_n, a_{n-1}, \dots, a_0$ into $n$ alternating inner multiplications and additions so $P(x)$ evaluates left-to-right without computing separate powers $x^k$:

$$P(x) = a_n x^n + \dots + a_1 x + a_0 = \bigl(\dots((a_n x + a_{n-1})x + a_{n-2})x + \dots + a_1\bigr)x + a_0$$

* **Eq. D.6 — Romberg Richardson Extrapolation Quadrature & Brent's Root Isolation:** Cancels leading $\mathcal{O}(h^{2m})$ discretization error between successive trapezoidal refinements $R(n-1, m-1)$ and $R(n, m-1)$ via the $4^m - 1$ Richardson weight to integrate $\int_a^b f(x)\,dx$, and isolates a root $f(x^*) = 0$ on a sign-change bracket $[a, b]$:

$$R(n, m) = R(n, m-1) + \frac{R(n, m-1) - R(n-1, m-1)}{4^m - 1}, \qquad f(x^*) = 0 \;\;\text{on}\;\; [a, b]$$

* **Eq. D.7 — Ordinary Least-Squares (OLS) Linear Regression & Weighted Mean:** Fits the linear calibration line $\hat{y} = mx + b$ (with slope $m$ and intercept $b$) and weighted mean $\bar{x}_w$ from the six hardware statistical accumulators ($n, \Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy$):

$$\hat{y} = m x + b, \qquad m = \frac{n\Sigma xy - \Sigma x\,\Sigma y}{n\Sigma x^2 - (\Sigma x)^2}, \qquad b = \frac{\Sigma y - m\Sigma x}{n}, \qquad \bar{x}_w = \frac{\Sigma x y}{\Sigma y}$$

* **Eq. D.8 — Five-Variable Time Value of Money (TVM) Cash-Flow Conservation Law:** Balances initial Present Value $\text{PV}$, level periodic payment $\text{PMT}$ (with timing flag $s = 0$ for end-of-period `END` or $s = 1$ for beginning-of-period `BEG`), and terminal Future Value $\text{FV}$ across $N$ compounding periods at periodic interest rate $i = \text{I\%}/100$:

$$\text{PV} + \text{PMT}\,(1 + i s)\left[\frac{1 - (1 + i)^{-N}}{i}\right] + \text{FV}\,(1 + i)^{-N} = 0$$

Whether invoked from the keypad via `{{key:x∥y}}` **(Eq. D.1)**, `{{key:▸θ,r}}`/`{{key:CMPLX}}` **(Eq. D.2)**, `{{key:LN}}`/`{{key:eˣ}}` **(Eq. D.3)**, `{{key:POLY}}` **(Eq. D.5)**, `{{key:SOLVE}}`/`{{key:∫}}` **(Eq. D.6)**, `{{key:Σ+}}`/`{{key:L.R.}}` **(Eq. D.7)**, or `{{key:TVM}}` **(Eq. D.8)**, or loaded into the symbolic Equation Bank (`{{key:EQN}}`) for multi-variable root-finding, every Standard Library equation evaluates in postfix order across Registers $T, Z, Y,$ and $X$ with full IEEE-754 double-precision fidelity.

---

## Chapter-by-Chapter Worked-Example Keystroke Directory

Each worked example is accompanied by its governing expression, complete step-by-step RPN keystroke sequence, and verified three-decimal Register $X$ result.

### Chapters 1–4: Hardware, RPN Stack Dynamics, Transcendentals & Trigonometry

| Chapter & Worked Problem | Governing Expression | Complete SC-32 RPN Keystroke Sequence | Verified Result ($\approx 3\text{ dec}$) |
| :--- | :--- | :--- | :---: |
| **Ch 1: Beer–Lambert Optical Absorption** | $\alpha = -\frac{10^4}{d_{\mu\text{m}}}\ln(T_{\text{opt}})$ | `0.10 {{key:LN}} 450 {{key:÷}} {{key:+/-}} 10000 {{key:×}}` | $\approx 51.169\text{ cm}^{-1}$ |
| **Ch 1: RC Switch Debounce Time** | $t = -R C \ln(1 - V_{\text{IH}}/V_{\text{DD}})$ | `2.1 {{key:ENTER}} 3.3 {{key:÷}} {{key:+/-}} 1 {{key:+}} {{key:LN}} {{key:+/-}} 100000 {{key:×}} 1 {{key:E}} 7 {{key:+/-}} {{key:×}} 1000 {{key:×}}` | $\approx 10.116\text{ ms}$ |
| **Ch 1: Simply-Supported Chassis Rib Deflection** | $\delta = \frac{F L^3}{48 E I},\; I = \frac{b h^3}{12}$ | `15 {{key:ENTER}} 2.5 {{key:ENTER}} 3 {{key:yˣ}} {{key:×}} 12 {{key:÷}} 3.92 {{key:ENTER}} 60 {{key:ENTER}} 3 {{key:yˣ}} {{key:×}} 48 {{key:ENTER}} 3500 {{key:×}} {{key:÷}} {{key:x⇄y}} {{key:÷}}` | $\approx 0.258\text{ mm}$ |
| **Ch 1: Pre-Flight Unit Manifest** | $52\text{ gal}\times 6\text{ lb/gal} \to \text{kg},\; 52\text{ gal}\to\text{L},\; 86^\circ\text{F}\to^\circ\text{C},\; 25.4\text{ cm}\to\text{in}$ | `52 {{key:ENTER}} 6 {{key:×}} {{key:▸kg}} 52 {{key:▸l}} 86 {{key:▸°C}} 25.4 {{key:▸in}}` | $T \approx 141.521,\; Z \approx 196.841,\; Y = 30,\; X = 10$ |
| **Ch 1: Thévenin CR2032 Internal Resistance** | $R_{\text{int}} = \frac{V_1 - V_2}{I_2 - I_1}$ | `2.94 {{key:ENTER}} 2.685 {{key:-}} 0.0182 {{key:ENTER}} 0.0048 {{key:-}} {{key:÷}}` | $\approx 19.03\ \Omega$ |
| **Ch 2: Two-Branch Rational Quotient** | $\frac{60 \times 2.5 + 35 \times 4}{18 - 5.5}$ | `60 {{key:ENTER}} 2.5 {{key:×}} 35 {{key:ENTER}} 4 {{key:×}} {{key:+}} 18 {{key:ENTER}} 5.5 {{key:-}} {{key:÷}}` | $23.2$ |
| **Ch 2: Golden Ratio Continued Fraction** | $1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + 1}}}}$ | `1 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}} {{key:+}} {{key:1/x}} {{key:+}} {{key:1/x}} {{key:+}} {{key:1/x}} {{key:+}} {{key:1/x}} {{key:+}}` | $1.625$ |
| **Ch 2: Work-Rate Parallel Pump Synthesis** | $T_{\text{fill}} = 30 \parallel 45 = \frac{30 \times 45}{30 + 45}$ | `30 {{key:ENTER}} 45 {{key:x∥y}}` | $18\text{ min}$ |
| **Ch 2: Kennelly $\Delta \to \text{Y}$ Star Impedance** | $R_a = \frac{R_{12}R_{31}}{S},\; R_b = \frac{R_{12}R_{23}}{S}$ ($S = 135$) | `30 {{key:ENTER}} 60 {{key:×}} 30 {{key:ENTER}} 45 {{key:+}} 60 {{key:+}} {{key:÷}} {{key:LASTX}} 30 {{key:ENTER}} 45 {{key:×}} {{key:x⇄y}} {{key:÷}}` | $R_a \approx 13.333,\; R_b = 10\ \Omega$ |
| **Ch 2: Cubic Horner Evaluation via `T`** | $P(x) = ((2x - 5)x + 3)x + 7$ at $x=3.5$ | `3.5 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}} 2 {{key:×}} 5 {{key:-}} {{key:×}} 3 {{key:+}} {{key:×}} 7 {{key:+}}` | $42$ |
| **Ch 3: Acoustic Sound Pressure Level** | $L_p = 20\log_{10}(p / p_0)$ | `2 {{key:ENTER}} 2 {{key:E}} 5 {{key:+/-}} {{key:÷}} {{key:LOG}} 20 {{key:×}}` | $100\text{ dB}$ |
| **Ch 3: Goldman–Hodgkin–Katz Potential** | $V_m = \frac{RT}{F}\ln\left(\frac{11.6}{189.98}\right)$ | `4 {{key:ENTER}} 0.04 {{key:ENTER}} 145 {{key:×}} {{key:+}} 0.45 {{key:ENTER}} 4 {{key:×}} {{key:+}} 140 {{key:ENTER}} 0.04 {{key:ENTER}} 12 {{key:×}} {{key:+}} 0.45 {{key:ENTER}} 110 {{key:×}} {{key:+}} {{key:÷}} {{key:LN}} 26.727 {{key:×}}` | $\approx -74.726\text{ mV}$ |
| **Ch 3: Counter-Flow Heat Exchanger LMTD** | $\Delta T_{\text{LMTD}} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)}$ ($85, 25\text{ K}$) | `85 {{key:ENTER}} 25 {{key:-}} {{key:LASTX}} 85 {{key:x⇄y}} {{key:÷}} {{key:LN}} {{key:÷}}` | $\approx 49.029\text{ K}$ |
| **Ch 3: Planck Spectral Radiance** | $B_\lambda = \frac{2hc^2/\lambda^5}{e^{hc/(\lambda k_B T)} - 1}$ | `4.98 {{key:eˣ}} 1 {{key:-}} 1.191 {{key:E}} 16 {{key:+/-}} {{key:ENTER}} 3.125 {{key:E}} 32 {{key:+/-}} {{key:÷}} {{key:x⇄y}} {{key:÷}}` | $\approx 2.638 \times 10^{13}$ |
| **Ch 3: Van der Waals Forward Pressure** | $P = \frac{nRT}{V - nb} - \frac{an^2}{V^2}$ | `2 {{key:ENTER}} 8.31446 {{key:×}} 320 {{key:×}} 0.005 {{key:ENTER}} 2 {{key:ENTER}} 4.27 {{key:E}} 5 {{key:+/-}} {{key:×}} {{key:-}} {{key:÷}} 0.364 {{key:ENTER}} 4 {{key:×}} 0.005 {{key:x²}} {{key:÷}} {{key:-}}` | $\approx 1{,}024{,}504.15\text{ Pa}$ |
| **Ch 3: Leading Digits of Giant Power $7^{400}$** | $L = 400\log_{10} 7 \implies 10^{\operatorname{FP}(L)} \times 10^{\operatorname{IP}(L)}$ | `7 {{key:LOG}} 400 {{key:×}} {{key:PARTS}} {{key:IP}} {{key:LASTX}} {{key:PARTS}} {{key:FP}} {{key:10ˣ}}` | $Y = 338$ ($339\text{ digits}$), $X \approx 1.095$ |
| **Ch 4: Surveyor Traverse Leg Projection** | $42^\circ 18' 36''$ over $125\text{ m}$ | `{{key:MODES}} {{key:DEG}} 42.1836 {{key:▸HR}} 125 {{key:▸y,x}}` | $\Delta N \approx 92.439,\; \Delta E \approx 84.143\text{ m}$ |
| **Ch 4: Aviation Wind-Triangle Groundspeed** | $\vec{V}_g = \vec{V}_a + \vec{V}_w$ | `{{key:MODES}} {{key:DEG}} 45 {{key:ENTER}} 220 {{key:▸y,x}} 130 {{key:ENTER}} 35 {{key:▸y,x}} {{key:x⇄y}} {{key:R↓}} {{key:+}} {{key:x⇄y}} {{key:R↑}} {{key:+}} {{key:x⇄y}} {{key:▸θ,r}}` | $\approx 225.759\text{ kt}$ at $53.884^\circ$ |
| **Ch 4: Catenary Transmission Line Sag** | $S = a\left[\cosh\left(\frac{L}{2a}\right) - 1\right]$ | `100 {{key:ENTER}} 800 {{key:÷}} {{key:HYP}} {{key:COS}} 1 {{key:-}} 800 {{key:×}}` | $\approx 6.258\text{ m}$ |
| **Ch 4: Keplerian Polar Conic Radius** | $r(\nu) = \frac{a(1 - e^2)}{1 + e\cos\nu}$ ($a=1.524, e=0.093$) | `{{key:MODES}} {{key:DEG}} 60 {{key:COS}} 0.093 {{key:×}} 1 {{key:+}} 1.524 {{key:ENTER}} 1 {{key:ENTER}} 0.093 {{key:x²}} {{key:-}} {{key:×}} {{key:x⇄y}} {{key:÷}}` | $\approx 1.444\text{ AU}$ |

### Chapters 5–8: Complex Phasors, Mensuration, Root-Finding & Quadrature

| Chapter & Worked Problem | Governing Expression | Complete SC-32 RPN Keystroke Sequence | Verified Result ($\approx 3\text{ dec}$) |
| :--- | :--- | :--- | :---: |
| **Ch 5: Complex Multiplication** | $(3 + j4)(1 - j2)$ | `3 {{key:ENTER}} 4 {{key:ENTER}} 1 {{key:ENTER}} 2 {{key:+/-}} {{key:CMPLX}} {{key:×}}` | $11 - j2$ ($Y=11, X=-2$) |
| **Ch 5: Parallel AC Branch Impedance** | $Z_{\text{eq}} = (20 + j15) \parallel (10 - j25)$ | `20 {{key:ENTER}} 15 {{key:ENTER}} 10 {{key:ENTER}} 25 {{key:+/-}} {{key:CMPLX}} {{key:x∥y}}` | $20.75 - j4.75\ \Omega$ |
| **Ch 5: Joukowsky Airfoil Conformal Map** | $w = \zeta + \frac{1}{\zeta}$ for $\zeta = 1.1 + j0.2$ | `1.1 {{key:ENTER}} 0.2 {{key:ENTER}} 1.1 {{key:ENTER}} 0.2 {{key:CMPLX}} {{key:1/x}} {{key:CMPLX}} {{key:+}}` | $1.98 + j0.04$ ($Y=1.98, X=0.04$) |
| **Ch 5: RF Transmission Line Reflection** | $\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}$ for $75 + j40\,\Omega$ on $50\,\Omega$ | `25 {{key:ENTER}} 40 {{key:ENTER}} 125 {{key:ENTER}} 40 {{key:CMPLX}} {{key:÷}} {{key:x⇄y}} {{key:▸θ,r}}` | $\lvert\Gamma\rvert \approx 0.359,\; \theta \approx 40.25^\circ$ |
| **Ch 6: Heron's Triangle Area** | $A = \sqrt{s(s-a)(s-b)(s-c)}$ for $(13, 14, 15)$ | `21 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}} 13 {{key:-}} {{key:×}} {{key:x⇄y}} 14 {{key:-}} {{key:×}} {{key:x⇄y}} 15 {{key:-}} {{key:×}} {{key:√x}}` | $84\text{ m}^2$ |
| **Ch 6: Conical Frustum Volume via `LASTX`** | $V = \frac{\pi h}{3}(R^2 + Rr + r^2)$ ($1.8, 0.4, 2.5\text{ m}$) | `1.8 {{key:x²}} {{key:LASTX}} 0.4 {{key:×}} {{key:LASTX}} {{key:x²}} {{key:+}} {{key:+}} 2.5 {{key:×}} {{key:π}} {{key:×}} 3 {{key:÷}}` | $\approx 10.786\text{ m}^3$ |
| **Ch 6: Welded I-Beam Centroid (`x̄w`)** | $\bar{y} = \frac{\sum m_i y_i}{\sum m_i}$ | `{{key:CLEAR}} {{key:CLΣ}} 40 {{key:ENTER}} 10 {{key:Σ+}} 60 {{key:ENTER}} 160 {{key:Σ+}} 30 {{key:ENTER}} 310 {{key:Σ+}} {{key:x̄,ȳ}} {{key:x̄w}}` | $\bar{y} \approx 148.462\text{ mm}$ |
| **Ch 6: Ramanujan Ellipse Perimeter** | $P \approx \pi(a+b)\left[1 + \frac{3h}{10+\sqrt{4-3h}}\right]$ ($a=10, b=5$) | `10 {{key:ENTER}} 5 {{key:-}} 10 {{key:ENTER}} 5 {{key:+}} {{key:÷}} {{key:x²}} 3 {{key:×}} {{key:ENTER}} {{key:ENTER}} 4 {{key:x⇄y}} {{key:-}} {{key:√x}} 10 {{key:+}} {{key:÷}} 1 {{key:+}} 15 {{key:×}} {{key:π}} {{key:×}}` | $\approx 48.442\text{ cm}$ |
| **Ch 7: Quartic Horner Evaluation via `T`** | $P(x) = (((4x-3)x+2)x-5)x+7$ at $2.5$ | `2.5 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}} 4 {{key:×}} 3 {{key:-}} {{key:×}} 2 {{key:+}} {{key:×}} 5 {{key:-}} {{key:×}} 7 {{key:+}}` | $116.375$ |
| **Ch 7: Green's Solar Fill Factor via `T`** | $FF = \frac{v_{\text{oc}} - \ln(v_{\text{oc}} + 0.72)}{v_{\text{oc}} + 1}$ at $25.145$ | `25.145 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}} 0.72 {{key:+}} {{key:LN}} {{key:-}} {{key:x⇄y}} 1 {{key:+}} {{key:÷}}` | $\approx 0.837$ |
| **Ch 7: *Casus Irreducibilis* Cubic (`POLY`)** | $x^3 - 6x^2 + 11x - 6 = 0$ | `{{key:POLY}} {{key:CLR}} 1 {{key:A}} 6 {{key:+/-}} {{key:B}} 11 {{key:C}} 6 {{key:+/-}} {{key:D}} {{key:XEQ}}` | $r_1 = 1,\; r_2 = 2,\; r_3 = 3$ |
| **Ch 7: Cauchy 3D Principal Stress Cubic** | $\lambda^3 - 70\lambda^2 + 1175\lambda - 5750 = 0$ | `{{key:POLY}} {{key:CLR}} 1 {{key:A}} 70 {{key:+/-}} {{key:B}} 1175 {{key:C}} 5750 {{key:+/-}} {{key:D}} {{key:XEQ}}` | $\sigma_3 = 10,\; \sigma_1 \approx 48.028\text{ MPa}$ |
| **Ch 7: Archimedes Floating Sphere (`POLY`)** | $h^3 - 1.5h^2 + 0.325 = 0$ ($C = 0$ default) | `{{key:POLY}} {{key:CLR}} 1 {{key:A}} 1.5 {{key:+/-}} {{key:B}} 0.325 {{key:D}} {{key:XEQ}}` | $h \approx 0.601\text{ m}$ |
| **Ch 7: Kepler's Anomaly via `SOLVE`** | $E - 0.25\sin E - 1.20 = 0$ (`RAD`) | `EQN`: `RCL E 0.25 ENTER RCL E SIN × - 1.20 -` $\to$ `1.2 {{key:STO}} E {{key:SOLVE}} E` | $E^* \approx 1.448\text{ rad}$ |
| **Ch 7: Colebrook Turbulent Friction Factor** | $\frac{1}{\sqrt{f}} + 2\log_{10}\left(\frac{0.001}{3.7} + \frac{2.51}{10^5\sqrt{f}}\right) = 0$ | `EQN`: `RCL F √x 1/x 0.001 ENTER 3.7 ÷ 2.51 ENTER 100000 ÷ RCL F √x ÷ + LOG 2 × +` $\to$ `0.02 {{key:STO}} F {{key:SOLVE}} F` | $f^* \approx 0.022$ |
| **Ch 8: Central-Difference Derivative** | $f'(2) \approx \frac{f(2.01) - f(1.99)}{0.02}$ for $x^3 - 2x$ | `2.01 {{key:ENTER}} 3 {{key:yˣ}} 2.01 {{key:ENTER}} 2 {{key:×}} {{key:-}} 1.99 {{key:ENTER}} 3 {{key:yˣ}} 1.99 {{key:ENTER}} 2 {{key:×}} {{key:-}} {{key:-}} 0.02 {{key:÷}}` | $\approx 10$ |
| **Ch 8: Simpson Three-Point Parabolic Rule** | $W = \frac{h}{3}[F(0) + 4F(0.075) + F(0.15)]$ ($h=0.075$) | `0.075 {{key:ENTER}} {{key:ENTER}} 3 {{key:yˣ}} 40000 {{key:×}} {{key:x⇄y}} 2500 {{key:×}} {{key:+}} 4 {{key:×}} 0.15 {{key:ENTER}} {{key:ENTER}} 3 {{key:yˣ}} 40000 {{key:×}} {{key:x⇄y}} 2500 {{key:×}} {{key:+}} {{key:+}} 0.075 {{key:×}} 3 {{key:÷}}` | $\approx 33.188\text{ J}$ |
| **Ch 8: Gaussian Normal Probability `∫`** | $\int_{-5}^0 \frac{1}{\sqrt{2\pi}}e^{-x^2/2}\,dx$ | `EQN`: `RCL X x² 2 ÷ +/- eˣ 2 ENTER π × √x ÷` $\to$ `5 {{key:+/-}} {{key:ENTER}} 0 {{key:∫}} X` | $\approx 0.5$ |
| **Ch 8: Huygens Wide-Angle Pendulum `∫`** | $\frac{2}{\pi}\int_0^{\pi/2}(1 - 0.25\sin^2\varphi)^{-1/2}\,d\varphi$ | `{{key:MODES}} {{key:RAD}}` `EQN`: `1 RCL X SIN x² 0.25 × - √x 1/x` $\to$ `0 {{key:ENTER}} {{key:π}} 2 {{key:÷}} {{key:∫}} X 2 {{key:×}} {{key:π}} {{key:÷}}` | $\approx 1.073$ |

### Chapters 9–11: Statistics, Discrete Radices & Financial TVM

| Chapter & Worked Problem | Governing Expression | Complete SC-32 RPN Keystroke Sequence | Verified Result ($\approx 3\text{ dec}$) |
| :--- | :--- | :--- | :---: |
| **Ch 9: Univariate Sample Mean & Std Dev** | $\bar{x},\; s_x$ for $10$ CNC shafts ($25.00\text{–}25.06\text{ mm}$) | `{{key:CLEAR}} {{key:CLΣ}} 25.02 {{key:Σ+}} 25.04 {{key:Σ+}} 25.01 {{key:Σ+}} 25.03 {{key:Σ+}} 25.05 {{key:Σ+}} 25.02 {{key:Σ+}} 25 {{key:Σ+}} 25.04 {{key:Σ+}} 25.03 {{key:Σ+}} 25.06 {{key:Σ+}} {{key:x̄,ȳ}} {{key:x̄}} {{key:s,σ}} {{key:sx}}` | $\bar{x} = 25.03,\; s_x \approx 0.018\text{ mm}$ |
| **Ch 9: Bivariate OLS Calibration & `ŷ`** | Fit $\{(10, 1.25), (20, 2.45), (30, 3.8), (40, 4.95)\}$ | `{{key:CLEAR}} {{key:CLΣ}} 1.25 {{key:ENTER}} 10 {{key:Σ+}} 2.45 {{key:ENTER}} 20 {{key:Σ+}} 3.8 {{key:ENTER}} 30 {{key:Σ+}} 4.95 {{key:ENTER}} 40 {{key:Σ+}} 25 {{key:L.R.}} {{key:ŷ}}` | $\hat{y}(25) \approx 3.113\text{ V}$ |
| **Ch 9: Michaelis–Menten Velocity (`LASTX`)** | $v_0 = \frac{V_{\max}c}{K_m + c}$ ($V_{\max}=120, K_m=4.2, c=8.5$) | `120 {{key:ENTER}} 8.5 {{key:×}} {{key:LASTX}} 4.2 {{key:+}} {{key:÷}}` | $\approx 80.315\ \mu\text{M/min}$ |
| **Ch 9: Arrhenius Activation Energy Fit** | $\ln k = \ln A - \frac{E_a}{R}\left(\frac{1}{T}\right)$ | Transform $x_i = 1/T_i,\; y_i = \ln k_i \to$ `{{key:Σ+}}` $\to$ `{{key:L.R.}} {{key:m}} 8.314 {{key:×}} {{key:+/-}}` | $E_a$ in $\text{J/mol}$ |
| **Ch 10: Euclid's Clock-Domain `GCD` & `LCM`** | $\operatorname{GCD}(1071, 462),\; \operatorname{LCM}(1071, 462)$ | `1071 {{key:ENTER}} 462 {{key:PARTS}} {{key:GCD}}` and `1071 {{key:ENTER}} 462 {{key:PARTS}} {{key:LCM}}` | $\text{GCD} = 21,\; \text{LCM} = 23{,}562$ |
| **Ch 10: Combinatorial RAID & Failover** | $\binom{12}{5}$ and $P(12, 5)$ | `12 {{key:ENTER}} 5 {{key:PROB}} {{key:Cn,r}}` and `12 {{key:ENTER}} 5 {{key:PROB}} {{key:Pn,r}}` | $792$ and $95{,}040$ |
| **Ch 10: IPv4 Base-256 Octet Unpacking** | $3{,}232{,}235{,}777 \to 192.168.1.1$ | `3232235777 {{key:ENTER}} 256 {{key:÷R}} 256 {{key:÷R}} 256 {{key:÷R}}` | $X=192, Y=168, Z=1, T=1$ |
| **Ch 10: `RGB565` 16-Bit Pixel Packing** | $(31 \ll 11) \mid (21 \ll 5) \mid 6$ in `HEX` | `{{key:BASE}} {{key:HEX}} 1F {{key:ENTER}} 800 {{key:×}} 15 {{key:ENTER}} 20 {{key:×}} {{key:+}} 6 {{key:+}}` | `FAA6h` ($64{,}166_{10}$) |
| **Ch 10: IEEE-754 `binary32` Unpacking** | Unpack `C0C80000h` ($-6.25_{10}$) | `{{key:BASE}} {{key:HEX}} C0C80000 {{key:ENTER}} 800000 {{key:÷R}} 100 {{key:÷R}} {{key:BASE}} {{key:DEC}}` | $X=1, Y=129, Z=4{,}718{,}592$ |
| **Ch 10: Modular Exponentiation ($7^8 \bmod 1000$)** | $\left(\left(7^2\right)^2 \bmod 1000\right)^2 \bmod 1000$ | `7 {{key:x²}} {{key:x²}} 1000 {{key:÷R}} {{key:x⇄y}} {{key:x²}} 1000 {{key:÷R}} {{key:x⇄y}}` | $801$ |
| **Ch 11: Base-Preserving Markup & `%CHG`** | $\Delta\%(40 \to 46)$ and $8.25\%$ tax on $\$85$ | `40 {{key:ENTER}} 46 {{key:%CHG}}` and `85 {{key:ENTER}} 8.25 {{key:%}} {{key:+}}` | $+15\%$ and $\approx \$92.013$ |
| **Ch 11: 30-Year Mortgage Payment (`TVM`)** | $N=360, I\%=6.5/12, \text{PV}=400{,}000, \text{FV}=0$ | `{{key:TVM}} 360 {{key:N}} 6.5 {{key:ENTER}} 12 {{key:÷}} {{key:I%}} 400000 {{key:PV}} 0 {{key:FV}} {{key:PMT}}` | $\approx -\$2{,}528.272$ |
| **Ch 11: Corporate Bond Semi-Annual YTM** | $N=20, \text{PV}=-942.5, \text{PMT}=27.5, \text{FV}=1000$ | `{{key:TVM}} 20 {{key:N}} 942.5 {{key:+/-}} {{key:PV}} 27.5 {{key:PMT}} 1000 {{key:FV}} {{key:I%}} 2 {{key:×}}` | $\approx 6.283\%\text{ yr}^{-1}$ |
| **Ch 11: Sharpe Ratio & Kelly Fraction** | $S_p = \frac{R_p - R_f}{\sigma_p},\; \tfrac{1}{2}f^* = \tfrac{1}{2}\!\left(p - \frac{q}{b}\right)$ | `18.4 {{key:ENTER}} 4.2 {{key:-}} 11.5 {{key:÷}}` and `0.58 {{key:ENTER}} 0.42 {{key:ENTER}} 1.5 {{key:÷}} {{key:-}} 2 {{key:÷}}` | $S_p \approx 1.235,\; \tfrac{1}{2}f^* = 0.15$ |

### Chapters 12–14: Curve Profiling, Coupled Engineering Laws & High-Speed Synthesis

| Chapter & Worked Problem | Governing Expression | Complete SC-32 RPN Keystroke Sequence | Verified Result ($\approx 3\text{ dec}$) |
| :--- | :--- | :--- | :---: |
| **Ch 12: Cubic Inflection & Value via `T`** | $f(x) = ((x - 6)x + 9)x + 1$ at $x_{\text{infl}} = 2$ | `2 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}} 6 {{key:-}} {{key:×}} 9 {{key:+}} {{key:×}} 1 {{key:+}}` | $f(2) = 3$ |
| **Ch 12: Perforated Gusset Centroid (`Σ-`)** | $120 \times 80$ plate ($x_1=60$) minus $r=20$ hole ($x_2=85$) | `{{key:CLEAR}} {{key:CLΣ}} 120 {{key:ENTER}} 80 {{key:×}} 60 {{key:Σ+}} 20 {{key:x²}} {{key:π}} {{key:×}} 85 {{key:Σ-}} {{key:x̄,ȳ}} {{key:x̄w}}` | $\bar{x} \approx 56.235\text{ mm}$ |
| **Ch 12: Simpson's Prismoidal Embankment** | $V = \frac{L}{6}(A_1 + 4A_m + A_2)$ ($A_1=24, A_m=45.5, A_2=76, L=30$) | `24 {{key:ENTER}} 45.5 {{key:ENTER}} 4 {{key:×}} {{key:+}} 76 {{key:+}} 30 {{key:×}} 6 {{key:÷}}` | $1{,}410\text{ m}^3$ |
| **Ch 12: Cylindrical Vessel Hoop Stress** | $\sigma_{\text{hoop}} = \frac{pr}{t}$ ($p=2.4\text{ MPa}, r=0.45\text{ m}, t=9\text{ mm}$) | `2.4 {{key:ENTER}} 0.45 {{key:×}} 0.009 {{key:÷}}` | $120\text{ MPa}$ |
| **Ch 13: Manning Open-Channel Discharge** | $Q = \frac{1}{n} A R_h^{2/3} S^{1/2}$ | `4 {{key:ENTER}} 1.5 {{key:×}} {{key:ENTER}} 4 {{key:ENTER}} 1.5 {{key:ENTER}} 2 {{key:×}} {{key:+}} {{key:÷}} 2 {{key:ENTER}} 3 {{key:÷}} {{key:yˣ}} 1.6 {{key:E}} 3 {{key:+/-}} {{key:√x}} {{key:×}} 0.013 {{key:÷}} {{key:×}}` | $\approx 16.659\text{ m}^3/\text{s}$ |
| **Ch 13: Insulated Steam-Pipe Heat Loss** | $q = \frac{\Delta T}{R_{\text{cond}} + R_{\text{conv}}}$ | `0.09 {{key:ENTER}} 0.05 {{key:÷}} {{key:LN}} 2 {{key:÷}} {{key:π}} {{key:÷}} 0.042 {{key:÷}} 10 {{key:÷}} 2 {{key:π}} {{key:×}} 0.09 {{key:×}} 10 {{key:×}} 12 {{key:×}} {{key:1/x}} {{key:+}} 180 {{key:ENTER}} 20 {{key:-}} {{key:x⇄y}} {{key:÷}}` | $\approx 673.762\text{ W}$ |
| **Ch 13: Matched Bridged-T Attenuator** | $R_1 = Z_0(K-1),\; R_2 = \frac{Z_0}{K-1}$ | `600 {{key:ENTER}} 12 {{key:ENTER}} 20 {{key:÷}} {{key:10ˣ}} 1 {{key:-}} {{key:×}} 600 {{key:LASTX}} {{key:÷}}` | $R_1 \approx 1{,}788.643\ \Omega,\; R_2 \approx 201.27\ \Omega$ |
| **Ch 13: Geodetic EDM Curvature Reduction** | $\Delta V = S\sin\alpha + \frac{1-k}{2R_\oplus}(S\cos\alpha)^2$ | `{{key:MODES}} {{key:DEG}} 7.2436 {{key:▸HR}} 4850 {{key:▸y,x}} {{key:x²}} 1 {{key:ENTER}} 0.13 {{key:-}} {{key:×}} 2 {{key:÷}} 6371000 {{key:÷}} {{key:+}}` | $\approx 627.077\text{ m}$ |
| **Ch 13: Compound Microscope Magnification** | $M_{\text{tot}} = \left(-\frac{d_{i1}}{d_{o1}}\right)\left(-\frac{d_{i2}}{d_{o2}}\right)$ | `16 {{key:1/x}} 17.2 {{key:1/x}} {{key:-}} {{key:1/x}} 17.2 {{key:÷}} {{key:+/-}} 25 {{key:1/x}} 250 {{key:+/-}} {{key:1/x}} {{key:-}} {{key:1/x}} 250 {{key:x⇄y}} {{key:÷}} {{key:×}}` | $\approx -146.667\times$ |
| **Ch 14: Two-Branch Rational Quotient ($Q_3$)** | $\frac{4.82 \times 10^3 - 195}{\sqrt{84.6} + 12.7^2}$ | `4.82 {{key:E}} 3 {{key:ENTER}} 195 {{key:-}} 84.6 {{key:√x}} 12.7 {{key:x²}} {{key:+}} {{key:÷}}` | $\approx 27.128$ |
| **Ch 14: Single-Entry Conical Frustum (`LASTX`)** | $V = \frac{\pi h}{3}(R^2 + Rr + r^2)$ ($8.5, 4.2, 14\text{ cm}$) | `8.5 {{key:x²}} {{key:LASTX}} 4.2 {{key:×}} {{key:LASTX}} {{key:x²}} {{key:+}} {{key:+}} 14 {{key:×}} {{key:π}} {{key:×}} 3 {{key:÷}}` | $\approx 1{,}841.246\text{ cm}^3$ |
| **Ch 14: Lucas's Cannonball Pyramid Sum** | $\sum_{k=1}^{24} k^2 = \frac{24(25)(49)}{6} = 70^2$ | `24 {{key:ENTER}} 25 {{key:×}} 49 {{key:×}} 6 {{key:÷}} {{key:√x}}` | $\Sigma = 4{,}900,\; \sqrt{\Sigma} = 70$ |
| **Ch 14: Nested Radical Pyramid** | $\sqrt{17 + \sqrt{29 + \sqrt{83}}}$ | `83 {{key:√x}} 29 {{key:+}} {{key:√x}} 17 {{key:+}} {{key:√x}}` | $\approx 4.814$ |
| **Ch 14: Multi-Branch `INF` Parallel Load** | $20 \parallel 30 \parallel 60 \parallel 40 \parallel 120$ | `{{key:FLAGS}} {{key:STACK}} {{key:INF}} 20 {{key:ENTER}} 30 {{key:ENTER}} 60 {{key:ENTER}} 40 {{key:ENTER}} 120 {{key:x∥y}} {{key:x∥y}} {{key:x∥y}} {{key:x∥y}}` | $7.5\ \Omega$ |
