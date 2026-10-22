---
title: "Appendix D: Mathematical Constants, SI Units & Master STEM Equation Directory | SC-32 Manual"
description: "Authoritative reference directory of immutable mathematical constants, complete BIPM SI prefixes, exact unit conversions, and 100 master STEM engineering equations with optimal RPN keystrokes for the StackCalc SC-32."
---

# Appendix D: Mathematical Constants, SI Units & Master STEM Equation Directory

{{blocks:sc32_hero_keynote|StackCalc SC-32 Bench Reference}}
*Figure D.1: The StackCalc SC-32 technical reference bench instrument: rapid parenthesis-free evaluation of fundamental engineering and mathematical equations.*

---

## The Architecture of Precision: Constants and Equations in RPN

This appendix catalogs 100 core equations across classical mechanics, electromagnetism, thermodynamics, optics, chemistry, astronomy, and finance, pairing each formula with its physical constants and step-by-step RPN stack execution on the StackCalc SC-32.

### SC-32 Scientific Register Hierarchy & Data Flow

| Register / Bank | Architectural Level | Operational Role & Data Flow |
| :--- | :--- | :--- |
| **Register T** | Top / Constant Buffer | Retains constant factor and replicates on dyadic stack drop |
| **Register Z** | Third Stack Level | Holds intermediate sub-expressions and vector/matrix terms |
| **Register Y** | Second Stack Level | Stores waiting dyadic base, dividend, or coordinate component |
| **Register X** | Active / Display | Direct keyboard entry and live computed result readout |
| **LASTX** | Recovery Buffer | Automatically captures previous $X$ before arithmetic/transcendentals |
| **STATS Bank** | 6 Accumulators | Hardware registers $\Sigma x, \Sigma y, \Sigma x^2, \Sigma y^2, \Sigma xy, n$ |
| **Memory A–Z** | 26 Global Registers | Persistent variable storage via `{{key:STO}}` and `{{key:RCL}}` |

### Scientific Notation, Register Telemetry, and Inside-Out Evaluation
Physical constants spanning dozens of orders of magnitude—such as Planck's constant $6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}$—are entered directly via the exponent key (`6.62607015 {{key:E}} 34 {{key:+/-}}`). As multi-step equations execute, intermediate physical quantities (such as angular frequency $\omega$ in Register $Y$ and capacitance $C$ in Register $X$) remain continuously visible on the $132 \times 65$ transflective LCD, allowing deeply nested blackbody radiation, thermodynamic, and relativistic formulas to be collapsed inside-out without parentheses or scratchpad registers.

---

## Fundamental Mathematical Constants

Unlike empirical physical measurements (such as the Newtonian gravitational constant $G$, the fine-structure constant $\alpha$, or subatomic particle masses, which are periodically revised by international CODATA adjustments and are therefore stated explicitly within individual problem benchmarks in Section D.4), pure mathematical constants are timeless invariants. The table below lists the fundamental mathematical constants and their exact SC-32 RPN generation sequences.

| Constant Name | Symbol | Exact Value (15-Digit Reference) | SC-32 RPN Entry Sequence |
| :--- | :---: | :--- | :--- |
| **Archimedes' Constant** | $\pi$ | `3.14159265358979` | `{{key:π}}` |
| **Euler's Number (Natural Base)** | $e$ | `2.71828182845905` | `1 {{key:eˣ}}` |
| **Golden Ratio** ($\frac{1+\sqrt{5}}{2}$) | $\varphi$ | `1.61803398874989` | `5 {{key:√x}} 1 {{key:+}} 2 {{key:÷}}` |
| **Euler–Mascheroni Constant** | $\gamma$ | `0.57721566490153` | `0.577215664902` |
| **Natural Logarithm of 2** | $\ln 2$ | `0.69314718055995` | `2 {{key:LN}}` |
| **Natural Logarithm of 10** | $\ln 10$ | `2.30258509299405` | `10 {{key:LN}}` |
| **Common Logarithm of $e$** | $\log_{10} e$ | `0.43429448190325` | `1 {{key:eˣ}} {{key:LOG}}` |
| **Pythagorean Constant** | $\sqrt{2}$ | `1.41421356237310` | `2 {{key:√x}}` |
| **Theodorus' Constant** | $\sqrt{3}$ | `1.73205080756888` | `3 {{key:√x}}` |
| **Diagonal of Unit Golden Rectangle** | $\sqrt{5}$ | `2.23606797749979` | `5 {{key:√x}}` |
| **Radians-to-Degrees Factor** ($\frac{180}{\pi}$) | $\text{rad}\to\text{deg}$ | `57.2957795130823` | `1 {{key:->DEG}}` |
| **Degrees-to-Radians Factor** ($\frac{\pi}{180}$) | $\text{deg}\to\text{rad}$ | `0.01745329251994` | `1 {{key:->RAD}}` |

---

## International Standard Unit Conversions & BIPM SI Prefixes

The table below provides the complete set of International Bureau of Weights and Measures (BIPM) SI prefixes—including the `ronna` ($10^{27}$), `quetta` ($10^{30}$), `ronto` ($10^{-27}$), and `quecto` ($10^{-30}$) prefixes adopted at the 27th CGPM—together with their direct `{{key:E}}` exponent keystrokes:

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

### Exact International Unit Definitions & Hardware Conversion Keys

| Physical Quantity | From Unit | To SI Unit | Exact Defining Factor / Formula | Dedicated SC-32 Key |
| :--- | :--- | :--- | :--- | :--- |
| **Length** | Inch (`in`) | Centimeter (`cm`) / Meter (`m`) | $1\text{ in} \equiv 2.54\text{ cm} \equiv 0.0254\text{ m}$ (exact) | `{{key:->cm}}` / `{{key:->in}}` |
| **Length** | Foot (`ft`) | Meter (`m`) | $1\text{ ft} \equiv 0.3048\text{ m}$ (exact) | `0.3048 {{key:×}}` |
| **Length** | Yard (`yd`) | Meter (`m`) | $1\text{ yd} \equiv 0.9144\text{ m}$ (exact) | `0.9144 {{key:×}}` |
| **Length** | Statute Mile (`mi`) | Kilometer (`km`) | $1\text{ mi} \equiv 1.609344\text{ km}$ (exact) | `{{key:->km}}` / `{{key:->mi}}` |
| **Length** | Nautical Mile (`nmi`) | Meter (`m`) | $1\text{ nmi} \equiv 1852\text{ m}$ (exact) | `1852 {{key:×}}` |
| **Mass** | Avoirdupois Pound (`lb`) | Kilogram (`kg`) | $1\text{ lb} \equiv 0.45359237\text{ kg}$ (exact) | `{{key:->kg}}` / `{{key:->lb}}` |
| **Volume** | U.S. Liquid Gallon (`gal`) | Liter (`L`) | $1\text{ gal} \equiv 3.785411784\text{ L}$ (exact, $231\text{ in}^3$) | `{{key:->l}}` / `{{key:->gal}}` |
| **Pressure** | Standard Atmosphere (`atm`) | Pascal (`Pa`) | $1\text{ atm} \equiv 101,325\text{ Pa}$ (exact) | `101325 {{key:×}}` |
| **Pressure** | Bar (`bar`) | Pascal (`Pa`) | $1\text{ bar} \equiv 100,000\text{ Pa}$ (exact) | `1 {{key:E}} 5 {{key:×}}` |
| **Energy** | Thermochemical Calorie (`cal`) | Joule (`J`) | $1\text{ cal}_{\text{th}} \equiv 4.184\text{ J}$ (exact) | `4.184 {{key:×}}` |
| **Energy** | Kilowatt-hour (`kWh`) | Joule (`J`) | $1\text{ kWh} \equiv 3.6 \times 10^6\text{ J}$ (exact) | `3.6 {{key:E}} 6 {{key:×}}` |
| **Temperature** | Fahrenheit (`°F`) | Celsius (`°C`) | $T_{\text{C}} = (T_{\text{F}} - 32) \times \frac{5}{9}$ (exact) | `{{key:->°C}}` / `{{key:->°F}}` |
| **Temperature** | Celsius (`°C`) | Kelvin (`K`) | $T_{\text{K}} = T_{\text{C}} + 273.15$ (exact) | `273.15 {{key:+}}` |
| **Time / Angle** | Sexagesimal (`H.MMSS`) | Decimal (`HR` / `DEG`) | $H + \frac{M}{60} + \frac{S}{3600}$ | `{{key:->HR}}` / `{{key:->HMS}}` |

---

## Master STEM Equation Directory: 100 Essential Bench & Contest Equations

Every equation in this directory is rendered as a numbered display equation (`(Eq. D.1)`–`(Eq. D.100)`) and cross-referenced against the numbered chapter display equations (`(Eq. 0.1)`–`(Eq. 14.43)`), complete with its formal mathematical definition, variable descriptions, physical/geometric motivation, optimal parenthesis-free RPN keystroke sequence, verified numerical benchmark, and stack execution profile.

| Discipline / Subject | Appendix Equations | Chapter Display Equation Cross-References |
|:---|:---|:---|
| 1. Classical Mechanics, Orbital Dynamics & Statics | Equations E.01 – E.10 (`Eq. D.1–D.10`) | Ch. 0 (`Eq. 0.2, 0.4, 0.5, 0.11`); Ch. 2 (`Eq. 2.1–2.12`); Ch. 13 (`Eq. 13.1–13.10`) |
| 2. Fluid Mechanics, Hydraulics & Aerodynamics | Equations E.11 – E.18 (`Eq. D.11–D.18`) | Ch. 0 (`Eq. 0.15, 0.19, 0.21, 0.26`); Ch. 7 (`Eq. 7.12`); Ch. 13 (`Eq. 13.11–13.20`) |
| 3. Thermodynamics, Gas Laws & Heat Transfer | Equations E.19 – E.26 (`Eq. D.19–D.26`) | Ch. 0 (`Eq. 0.6, 0.13, 0.20, 0.22`); Ch. 2 (`Eq. 2.1`); Ch. 3 (`Eq. 3.8–3.22`) |
| 4. Electricity, Magnetism & AC Circuit Analysis | Equations E.27 – E.36 (`Eq. D.27–D.36`) | Ch. 0 (`Eq. 0.3, 0.16, 0.27`); Ch. 2 (`Eq. 2.2`); Ch. 5 (`Eq. 5.1–5.65`) |
| 5. Wave Mechanics, Acoustics & Physical Optics | Equations E.37 – E.44 (`Eq. D.37–D.44`) | Ch. 0 (`Eq. 0.9, 0.12, 0.14, 0.23`); Ch. 2 (`Eq. 2.5`); Ch. 4 (`Eq. 4.1–4.63`) |
| 6. Nuclear, Atomic & Relativistic Physics | Equations E.45 – E.51 (`Eq. D.45–D.51`) | Ch. 0 (`Eq. 0.17`); Ch. 3 (`Eq. 3.25–3.45`); Ch. 8 (`Eq. 8.15–8.40`) |
| 7. Coordinate Geometry, Mensuration & 2D Curved Sections | Equations E.52 – E.66 (`Eq. D.52–D.66`) | Ch. 4 (`Eq. 4.10–4.50`); Ch. 6 (`Eq. 6.1–6.25`); Ch. 12 (`Eq. 12.1–12.25`) |
| 8. 3D Solid Geometry & Mensuration Master Compendium | Equations E.67 – E.72 (`Eq. D.67–D.72`) | Ch. 0 (`Eq. 0.10`); Ch. 6 (`Eq. 6.26–6.50`) |
| 9. Contest Financial Mathematics, Amortization & TVM | Equations E.73 – E.77 (`Eq. D.73–D.77`) | Ch. 0 (`Eq. 0.8`); Ch. 2 (`Eq. 2.3`); Ch. 11 (`Eq. 11.1–11.27`) |
| 10. Chemistry, Electrochemistry, Chemical Kinetics & Biochemistry | Equations E.78 – E.85 (`Eq. D.78–D.85`) | Ch. 0 (`Eq. 0.24`); Ch. 3 (`Eq. 3.46–3.63`); Ch. 9 (`Eq. 9.10`) |
| 11. Probability, Statistics, Quality Control & Information Theory | Equations E.86 – E.93 (`Eq. D.86–D.93`) | Ch. 8 (`Eq. 8.2`); Ch. 9 (`Eq. 9.1–9.43`); Ch. 12 (`Eq. 12.16–12.17`) |
| 12. Structural Mechanics, Semiconductor Electronics, RF & Computer Engineering | Equations E.94 – E.100 (`Eq. D.94–D.100`) | Ch. 0 (`Eq. 0.18`); Ch. 1 (`Eq. 1.1–1.36`); Ch. 7 (`Eq. 7.1–7.52`); Ch. 10 (`Eq. 10.1–10.17`) |

---

### Section 1: Classical Mechanics, Orbital Dynamics & Statics

Equations E.01–E.10 cover linear and rotational kinematics, Newtonian gravitation, orbital trajectories, and structural column buckling.

#### Equation E.01: Kinematic Velocity-Displacement Relation
$$v_f = \sqrt{v_i^2 + 2 a \Delta x}$$
*Variables:* $v_i$ (initial velocity, $\text{m/s}$), $a$ (acceleration, $\text{m/s}^2$), $\Delta x$ (displacement, $\text{m}$).  
*RPN Sequence:* `vi {{key:x²}} 2 {{key:ENTER}} a {{key:×}} dx {{key:×}} {{key:+}} {{key:√x}}`  
*Benchmark:* $v_i = 12.0\text{ m/s}, a = 4.5\text{ m/s}^2, \Delta x = 25.0\text{ m}$.  
*Target Value:* **`19.209373`** $\text{m/s}$.  

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `12 {{key:x²}}` | 0.00 | 0.00 | 0.00 | 144.0000 | Square initial velocity $v_i^2 = 144.0000\text{ m}^2/\text{s}^2$ |
| 02 | `2 {{key:ENTER}} 4.5 {{key:×}}` | 0.00 | 0.00 | 144.0000 | 9.0000 | Double acceleration $2a = 9.0000\text{ m/s}^2$; $v_i^2$ lifts to $Y$ |
| 03 | `25 {{key:×}} {{key:+}}` | 0.00 | 0.00 | 0.00 | 369.0000 | Add $2a\Delta x = 225.0$ to $v_i^2$ for $v_f^2 = 369.0000\text{ m}^2/\text{s}^2$ |
| 04 | `{{key:√x}}` | 0.00 | 0.00 | 0.00 | 19.209373 | Final velocity $v_f = 19.2094\text{ m/s}$ |

---

#### Equation E.02: Projectile Motion Maximum Range
$$R = \frac{v_0^2 \sin(2\theta)}{g}$$
*Variables:* $v_0$ (muzzle velocity, $\text{m/s}$), $\theta$ (launch angle, degrees), $g = 9.80665\text{ m/s}^2$.  
*RPN Sequence in `{{key:DEG}}` Mode:* `v0 {{key:x²}} theta {{key:ENTER}} 2 {{key:×}} {{key:SIN}} {{key:×}} 9.80665 {{key:÷}}`  
*Benchmark:* $v_0 = 45.0\text{ m/s}, \theta = 35.0^\circ$.  
*Target Value:* **`194.0435`** $\text{m}$.  

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `45 {{key:x²}}` | 0.00 | 0.00 | 0.00 | 2025.0000 | Square muzzle velocity $v_0^2 = 2025.0000\text{ m}^2/\text{s}^2$ |
| 02 | `35 {{key:ENTER}} 2 {{key:×}}` | 0.00 | 0.00 | 2025.0000 | 70.0000 | Double launch angle $2\theta = 70.0^\circ$; $v_0^2$ lifts to $Y$ |
| 03 | `{{key:SIN}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 1902.8711 | Numerator $v_0^2 \sin(70^\circ) = 1902.8711\text{ m}^2/\text{s}^2$ |
| 04 | `9.80665 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 194.0435 | Horizontal range $R = 194.0435\text{ m}$ |

---

#### Equation E.03: Centripetal Acceleration & Radial Force
$$F_c = \frac{m v^2}{r}$$
*Variables:* $m$ (mass, $\text{kg}$), $v$ (tangential speed, $\text{m/s}$), $r$ (radius, $\text{m}$).  
*RPN Sequence:* `v {{key:x²}} m {{key:×}} r {{key:÷}}`  
*Benchmark:* $m = 1250\text{ kg}, v = 24.0\text{ m/s}, r = 60.0\text{ m}$.  
*Target Value:* **`12000.0`** $\text{N}$ ($12.0\text{ kN}$) — keying `{{res:sc32_appendix_d_constants_and_equations_seq_01:keys}}` yields `{{res:sc32_appendix_d_constants_and_equations_seq_01:value}}`.

---

#### Equation E.04: Newton's Law of Universal Gravitation
$$F_g = G \frac{m_1 m_2}{r^2}$$
*Variables:* $G = 6.67430 \times 10^{-11}, m_1, m_2 (\text{kg}), r (\text{m})$.  
*RPN Sequence:* `6.67430 {{key:E}} 11 {{key:+/-}} m1 {{key:×}} m2 {{key:×}} r {{key:x²}} {{key:÷}}`  
*Benchmark:* $m_1 = 5.9722 \times 10^{24}, m_2 = 1500, r = 6.771 \times 10^6$.  
*Target Value:* **`13038.58`** $\text{N}$.  

| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `6.67430 {{key:E}} 11 {{key:+/-}} {{key:ENTER}} 5.9722 {{key:E}} 24 {{key:×}} 1500 {{key:×}}` | 0.00 | 0.00 | 0.00 | 5.9791E17 | 5.97910E17 |
| 02 | `6.771 {{key:E}} 6 {{key:x²}}` | 0.00 | 0.00 | 5.9791E17 | 4.5846E13 | 4.58464E13 |
| 03 | `{{key:÷}}` | 0.00 | 0.00 | 0.00 | 13038.58 | 1.30386E4 |

---

#### Equation E.05: Circular Orbital Velocity
$$v = \sqrt{\frac{\mu}{r}}$$
*Variables:* $\mu = 3.986004418 \times 10^{14}\text{ m}^3/\text{s}^2$, $r$ (orbital radius, $\text{m}$).  
*RPN Sequence:* `3.986004418 {{key:E}} 14 {{key:ENTER}} r {{key:÷}} {{key:√x}}`  
*Benchmark:* $r = 6.771 \times 10^6\text{ m}$ ($400\text{ km}$ LEO).  
*Target Value:* **`7672.76`** $\text{m/s}$.

---

#### Equation E.06: Planetary Escape Velocity
$$v_{\text{esc}} = \sqrt{\frac{2 \mu}{r}} = v_{\text{orbital}} \times \sqrt{2}$$
*Variables:* $\mu$ (gravitational parameter), $r$ (radius, $\text{m}$).  
*RPN Sequence:* `2 {{key:ENTER}} mu {{key:×}} r {{key:÷}} {{key:√x}}`  
*Benchmark:* Earth surface $r = 6.371 \times 10^6\text{ m}, \mu = 3.986004418 \times 10^{14}$.  
*Target Value:* **`11186.0`** $\text{m/s}$ ($11.19\text{ km/s}$).

---

#### Equation E.07: Tsiolkovsky Rocket Burnout Equation
$$\Delta v = v_e \ln\left(\frac{m_0}{m_f}\right)$$
*Variables:* $v_e$ (effective exhaust velocity, $\text{m/s}$), $m_0$ (wet mass), $m_f$ (dry mass).  
*RPN Sequence:* `m0 {{key:ENTER}} mf {{key:÷}} {{key:LN}} ve {{key:×}}`  
*Benchmark:* $v_e = 3100\text{ m/s}, m_0 = 45000\text{ kg}, m_f = 6500\text{ kg}$.  
*Target Value:* **`6000.12`** $\text{m/s}$.

---

#### Equation E.08: Rotational Kinetic Energy of Rigid Body
$$E_{\text{rot}} = \frac{1}{2} I \omega^2$$
*Variables:* $I$ (moment of inertia, $\text{kg}\cdot\text{m}^2$), $\omega$ (angular velocity, $\text{rad/s}$).  
*RPN Sequence:* `omega {{key:x²}} I {{key:×}} 2 {{key:÷}}`  
*Benchmark:* $I = 4.25\text{ kg}\cdot\text{m}^2, \omega = 150.0\text{ rad/s}$.  
*Target Value:* **`47812.5`** $\text{J}$ ($47.81\text{ kJ}$).

---

#### Equation E.09: Simple Gravity Pendulum Period
$$T = 2\pi \sqrt{\frac{L}{g}}$$
*Variables:* $L$ (pendulum length, $\text{m}$), $g = 9.80665\text{ m/s}^2$.  
*RPN Sequence:* `L {{key:ENTER}} 9.80665 {{key:÷}} {{key:√x}} 2 {{key:×}} {{key:π}} {{key:×}}`  
*Benchmark:* $L = 0.99362\text{ m}$ (seconds pendulum).  
*Target Value:* **`2.00000`** $\text{s}$.

---

#### Equation E.10: Euler Critical Buckling Load for Slender Column
$$P_{\text{cr}} = \frac{\pi^2 E I}{K^2 L^2}$$
*Variables:* $E$ (Young's modulus, $\text{Pa}$), $I$ (area moment of inertia, $\text{m}^4$), $K$ (effective length factor), $L$ (length, $\text{m}$).  
*RPN Sequence:* `{{key:π}} {{key:x²}} E {{key:×}} I {{key:×}} K {{key:ENTER}} L {{key:×}} {{key:x²}} {{key:÷}}`  
*Benchmark:* $E = 200 \times 10^9\text{ Pa}, I = 6.4 \times 10^{-6}\text{ m}^4, K = 1.0, L = 4.5\text{ m}$.  
*Target Value:* **`623869.6`** $\text{N}$ ($623.87\text{ kN}$).

---

### Section 2: Fluid Mechanics, Hydraulics & Aerodynamics

Equations E.11–E.18 span incompressible pipe flow, viscous friction head loss, open-channel hydraulics, and compressible flight regimes.

#### Equation E.11: Torricelli Efflux Jet Velocity

$$v = \sqrt{2 g h}$$
*Variables:* $g = 9.80665\text{ m/s}^2$, $h$ (fluid head, $\text{m}$).  
*RPN Sequence:* `2 {{key:ENTER}} 9.80665 {{key:×}} h {{key:×}} {{key:√x}}`  
*Benchmark:* $h = 5.0\text{ m}$.  
*Target Value:* **`9.90285`** $\text{m/s}$.  

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `2 {{key:ENTER}} 9.80665 {{key:×}}` | 0.00 | 0.00 | 0.00 | 19.613300 | Double gravitational acceleration $2g = 19.6133\text{ m/s}^2$ |
| 02 | `5 {{key:×}}` | 0.00 | 0.00 | 0.00 | 98.066500 | Scale by fluid head $2gh = 98.0665\text{ m}^2/\text{s}^2$ |
| 03 | `{{key:√x}}` | 0.00 | 0.00 | 0.00 | 9.902853 | Torricelli efflux velocity $v = 9.9029\text{ m/s}$ |

---

#### Equation E.12: Volumetric Flow Continuity Equation
$$Q = A_1 v_1 = \frac{\pi D_1^2}{4} v_1$$
*Variables:* $D$ (pipe diameter, $\text{m}$), $v$ (fluid velocity, $\text{m/s}$).  
*RPN Sequence:* `D {{key:x²}} {{key:π}} {{key:×}} 4 {{key:÷}} v {{key:×}}`  
*Benchmark:* $D = 0.15\text{ m}, v = 2.4\text{ m/s}$.  
*Target Value:* **`0.0424115`** $\text{m}^3/\text{s}$ ($42.41\text{ L/s}$).

---

#### Equation E.13: Reynolds Number for Pipe Flow
$$Re = \frac{\rho v D}{\mu}$$
*Variables:* $\rho$ (fluid density, $\text{kg/m}^3$), $v$ (velocity, $\text{m/s}$), $D$ (diameter, $\text{m}$), $\mu$ (dynamic viscosity, $\text{Pa}\cdot\text{s}$).  
*RPN Sequence:* `rho {{key:ENTER}} v {{key:×}} D {{key:×}} mu {{key:÷}}`  
*Benchmark:* $\rho = 998\text{ kg/m}^3, v = 1.8\text{ m/s}, D = 0.05\text{ m}, \mu = 0.001002\text{ Pa}\cdot\text{s}$.  
*Target Value:* **`89640.7`** (Turbulent regime: $Re > 4000$).

---

#### Equation E.14: Darcy-Weisbach Friction Head Loss
$$h_f = f \frac{L}{D} \frac{v^2}{2 g}$$
*Variables:* $f$ (friction factor), $L$ (length, $\text{m}$), $D$ (diameter, $\text{m}$), $v$ (velocity, $\text{m/s}$), $g = 9.80665$.  
*RPN Sequence:* `f {{key:ENTER}} L {{key:×}} D {{key:÷}} v {{key:x²}} {{key:×}} 2 {{key:÷}} 9.80665 {{key:÷}}`  
*Benchmark:* $f = 0.024, L = 120.0\text{ m}, D = 0.20\text{ m}, v = 2.5\text{ m/s}$.  
*Target Value:* **`4.5887`** $\text{m}$.

---

#### Equation E.15: Manning Formula for Open Channel Uniform Flow
$$v = \frac{1}{n} R_h^{2/3} S^{1/2}$$
*Variables:* $n$ (roughness coefficient), $R_h$ (hydraulic radius, $\text{m}$), $S$ (energy slope).  
*RPN Sequence:* `Rh {{key:ENTER}} 2 {{key:ENTER}} 3 {{key:÷}} {{key:yˣ}} S {{key:√x}} {{key:×}} n {{key:÷}}`  
*Benchmark:* $n = 0.015, R_h = 0.85\text{ m}, S = 0.0025$.  
*Target Value:* **`2.9918`** $\text{m/s}$.

---

#### Equation E.16: Poiseuille Laminar Capillary Flow Rate
$$Q = \frac{\pi r^4 \Delta P}{8 \mu L}$$
*Variables:* $r$ (radius, $\text{m}$), $\Delta P$ (pressure drop, $\text{Pa}$), $\mu$ (viscosity, $\text{Pa}\cdot\text{s}$), $L$ (length, $\text{m}$).  
*RPN Sequence:* `r {{key:ENTER}} 4 {{key:yˣ}} {{key:π}} {{key:×}} dP {{key:×}} 8 {{key:÷}} mu {{key:÷}} L {{key:÷}}`  
*Benchmark:* $r = 0.002\text{ m}, \Delta P = 5000\text{ Pa}, \mu = 0.0035\text{ Pa}\cdot\text{s}, L = 0.50\text{ m}$.  
*Target Value:* **`1.7952 × 10⁻⁵`** $\text{m}^3/\text{s}$.

---

#### Equation E.17: Aerodynamic Dynamic Pressure
$$q = \frac{1}{2} \rho v^2$$
*Variables:* $\rho$ (air density, $\text{kg/m}^3$), $v$ (airspeed, $\text{m/s}$).  
*RPN Sequence:* `v {{key:x²}} rho {{key:×}} 2 {{key:÷}}`  
*Benchmark:* $\rho = 1.225\text{ kg/m}^3, v = 65.0\text{ m/s}$.  
*Target Value:* **`2587.81`** $\text{Pa}$.

---

#### Equation E.18: Compressible Flow Mach Number
$$M = \frac{v}{\sqrt{\gamma R_{\text{specific}} T}}$$
*Variables:* $v$ (velocity, $\text{m/s}$), $\gamma = 1.40$, $R_{\text{specific}} = 287.058\text{ J/(kg}\cdot\text{K)}$, $T$ (temperature, $\text{K}$).  
*RPN Sequence:* `1.4 {{key:ENTER}} 287.058 {{key:×}} T {{key:×}} {{key:√x}} v {{key:x⇄y}} {{key:÷}}`  
*Benchmark:* $v = 240.0\text{ m/s}, T = 245.0\text{ K}$ (cruising altitude).  
*Target Value:* **`0.7651`** (Transonic boundary).

---

### Section 3: Thermodynamics, Gas Laws & Heat Transfer

Equations E.19–E.26 evaluate ideal gas state relations, thermodynamic power cycle efficiencies, radiative and conductive heat transfer, and phase-change energy.

#### Equation E.19: Ideal Gas State Equation
$$P = \frac{n R T}{V}$$
*Variables:* $n$ (moles), $R = 8.314462618\text{ J/(mol}\cdot\text{K)}$, $T$ (temperature, $\text{K}$), $V$ (volume, $\text{m}^3$).  
*RPN Sequence:* `n {{key:ENTER}} 8.314462618 {{key:×}} T {{key:×}} V {{key:÷}}`  
*Benchmark:* $n = 4.5\text{ mol}, T = 350.0\text{ K}, V = 0.035\text{ m}^3$.  
*Target Value:* **`374150.8`** $\text{Pa}$ ($374.15\text{ kPa}$).  

| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `4.5 {{key:ENTER}} 8.314462618 {{key:×}}` | 0.00 | 0.00 | 0.00 | 37.415082 | 37.415082 |
| 02 | `350 {{key:×}}` | 0.00 | 0.00 | 0.00 | 13095.279 | 13095.279 |
| 03 | `.035 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 374150.82 | 374150.8 |

---

#### Equation E.20: Carnot Thermodynamic Cycle Maximum Efficiency
$$\eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H}$$
*Variables:* $T_C$ (cold reservoir, $\text{K}$), $T_H$ (hot reservoir, $\text{K}$).  
*RPN Sequence:* `TC {{key:ENTER}} TH {{key:÷}} 1 {{key:x⇄y}} {{key:-}}`  
*Benchmark:* $T_C = 295.0\text{ K}, T_H = 850.0\text{ K}$.  
*Target Value:* **`0.65294`** ($65.29\%$).

---

#### Equation E.21: Stefan-Boltzmann Total Radiative Power
$$P = \sigma \epsilon A T^4$$
*Variables:* $\sigma = 5.670374419 \times 10^{-8}$, $\epsilon$ (emissivity), $A$ (area, $\text{m}^2$), $T$ (temperature, $\text{K}$).  
*RPN Sequence:* `T {{key:ENTER}} 4 {{key:yˣ}} A {{key:×}} eps {{key:×}} 5.670374419 {{key:E}} 8 {{key:+/-}} {{key:×}}`  
*Benchmark:* $T = 1200.0\text{ K}, A = 1.8\text{ m}^2, \epsilon = 0.85$.  
*Target Value:* **`179830.8`** $\text{W}$ ($179.83\text{ kW}$).

---

#### Equation E.22: Fourier Conduction Heat Transfer Rate
$$q = \frac{k A (T_1 - T_2)}{L}$$
*Variables:* $k$ (thermal conductivity, $\text{W/(m}\cdot\text{K)}$), $A$ (area, $\text{m}^2$), $T_1, T_2$ (temperatures, $\text{K}$), $L$ (thickness, $\text{m}$).  
*RPN Sequence:* `T1 {{key:ENTER}} T2 {{key:-}} k {{key:×}} A {{key:×}} L {{key:÷}}`  
*Benchmark:* $k = 0.75\text{ W/(m}\cdot\text{K)}, A = 15.0\text{ m}^2, T_1 = 295.15\text{ K}, T_2 = 263.15\text{ K}, L = 0.20\text{ m}$.  
*Target Value:* **`1800.0`** $\text{W}$.

---

#### Equation E.23: Newton's Law of Cooling Transient Temperature
$$T(t) = T_{\infty} + (T_0 - T_{\infty}) e^{-k t}$$
*Variables:* $T_\infty$ (ambient temp), $T_0$ (initial temp), $k$ (cooling rate, $\text{s}^{-1}$), $t$ (time, $\text{s}$).  
*RPN Sequence:* `k {{key:+/-}} t {{key:×}} {{key:eˣ}} T0 {{key:ENTER}} Tinf {{key:-}} {{key:×}} Tinf {{key:+}}`  
*Benchmark:* $T_\infty = 20.0^\circ\text{C}, T_0 = 90.0^\circ\text{C}, k = 0.005\text{ s}^{-1}, t = 180.0\text{ s}$.  
*Target Value:* **`48.46`** $^\circ\text{C}$.

---

#### Equation E.24: Logarithmic Mean Temperature Difference (LMTD)
$$\text{LMTD} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)}$$
*Variables:* $\Delta T_1, \Delta T_2$ (terminal temperature differences, $\text{K}$).  
*RPN Sequence:* `dT1 {{key:ENTER}} dT2 {{key:-}} dT1 {{key:ENTER}} dT2 {{key:÷}} {{key:LN}} {{key:÷}}`  
*Benchmark:* $\Delta T_1 = 45.0\text{ K}, \Delta T_2 = 18.0\text{ K}$.  
*Target Value:* **`29.4665`** $\text{K}$.

---

#### Equation E.25: Ideal Brayton Gas Turbine Thermal Efficiency
$$\eta = 1 - \frac{1}{r_p^{(\gamma - 1)/\gamma}}$$
*Variables:* $r_p$ (pressure ratio), $\gamma = 1.40$.  
*RPN Sequence:* `rp {{key:ENTER}} 1.4 {{key:ENTER}} 1 {{key:-}} 1.4 {{key:÷}} {{key:yˣ}} {{key:1/x}} 1 {{key:x⇄y}} {{key:-}}`  
*Benchmark:* $r_p = 16.0, \gamma = 1.40$.  
*Target Value:* **`0.5476`** ($54.76\%$).

---

#### Equation E.26: Latent Heat Phase Transition Energy
$$Q = m L_v$$
*Variables:* $m$ (mass, $\text{kg}$), $L_v$ (latent heat of vaporization, $\text{J/kg}$).  
*RPN Sequence:* `m {{key:ENTER}} Lv {{key:×}}`  
*Benchmark:* $m = 2.5\text{ kg}, L_v = 2.26 \times 10^6\text{ J/kg}$ (water at $100^\circ\text{C}$).  
*Target Value:* **`5650000.0`** $\text{J}$ ($5.65\text{ MJ}$).

---

### Section 4: Electricity, Magnetism & AC Circuit Analysis

Equations E.27–E.36 address DC resistive networks, reactive energy storage, RC/RL transients, RLC resonance, and decibel power ratios.

#### Equation E.27: Ohm's Law and DC Power Dissipation
$$P = I^2 R = \frac{V^2}{R} = V I$$
*Variables:* $V$ (voltage, $\text{V}$), $R$ (resistance, $\Omega$), $I$ (current, $\text{A}$).  
*RPN Sequence:* `V {{key:x²}} R {{key:÷}}`  
*Benchmark:* $V = 120.0\text{ V}, R = 15.0\,\Omega$.  
*Target Value:* **`960.0`** $\text{W}$.

---

#### Equation E.28: Equivalent Resistance of Parallel Networks via `{{key:x∥y}}`
$$R_{\text{eq}} = R_1 \parallel R_2 \parallel R_3 = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}}$$
*Variables:* $R_1, R_2, R_3 (\Omega)$.  
*RPN Sequence:* `R1 {{key:ENTER}} R2 {{key:x∥y}} R3 {{key:x∥y}}`  
*Benchmark:* $R_1 = 100.0\,\Omega, R_2 = 150.0\,\Omega, R_3 = 300.0\,\Omega$.  
*Target Value:* **`50.0`** $\Omega$.  

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `100 {{key:ENTER}}` | 0.00 | 0.00 | 100.0000 | 100.0000 | Stage first parallel branch $R_1 = 100.0\,\Omega$ in $Y$ |
| 02 | `150 {{key:x∥y}}` | 0.00 | 0.00 | 0.00 | 60.0000 | Parallel combination $100 \parallel 150 = 60.0\,\Omega$ |
| 03 | `300 {{key:x∥y}}` | 0.00 | 0.00 | 0.00 | 50.0000 | Parallel combination $60 \parallel 300 = 50.0\,\Omega$ |

---

#### Equation E.29: Electrostatic Energy Stored in Capacitor
$$U_C = \frac{1}{2} C V^2$$
*Variables:* $C$ (capacitance, $\text{F}$), $V$ (voltage, $\text{V}$).  
*RPN Sequence:* `V {{key:x²}} C {{key:×}} 2 {{key:÷}}`  
*Benchmark:* $C = 47.0 \times 10^{-6}\text{ F}, V = 450.0\text{ V}$.  
*Target Value:* **`4.75875`** $\text{J}$.

---

#### Equation E.30: Magnetic Energy Stored in Inductor
$$U_L = \frac{1}{2} L I^2$$
*Variables:* $L$ (inductance, $\text{H}$), $I$ (current, $\text{A}$).  
*RPN Sequence:* `I {{key:x²}} L {{key:×}} 2 {{key:÷}}`  
*Benchmark:* $L = 0.25\text{ H}, I = 6.4\text{ A}$.  
*Target Value:* **`5.12`** $\text{J}$.

---

#### Equation E.31: RC Transient Charging Voltage
$$V_C(t) = V_0 \left(1 - e^{-t / (R C)}\right)$$
*Variables:* $V_0$ (supply voltage), $R (\Omega)$, $C (\text{F})$, $t (\text{s})$.  
*RPN Sequence:* `t {{key:+/-}} R {{key:÷}} C {{key:÷}} {{key:eˣ}} 1 {{key:x⇄y}} {{key:-}} V0 {{key:×}}`  
*Benchmark:* $V_0 = 12.0\text{ V}, R = 10000.0\,\Omega, C = 220.0 \times 10^{-6}\text{ F}, t = 3.5\text{ s}$.  
*Target Value:* **`9.5583`** $\text{V}$.

---

#### Equation E.32: RL Inductive Current Decay
$$I(t) = I_0 e^{-t (R / L)}$$
*Variables:* $I_0$ (initial current), $R (\Omega)$, $L (\text{H})$, $t (\text{s})$.  
*RPN Sequence:* `t {{key:+/-}} R {{key:×}} L {{key:÷}} {{key:eˣ}} I0 {{key:×}}`  
*Benchmark:* $I_0 = 5.0\text{ A}, R = 24.0\,\Omega, L = 0.80\text{ H}, t = 0.05\text{ s}$.  
*Target Value:* **`1.1157`** $\text{A}$.

---

#### Equation E.33: LC Resonant Frequency
$$f_0 = \frac{1}{2 \pi \sqrt{L C}}$$
*Variables:* $L$ (inductance, $\text{H}$), $C$ (capacitance, $\text{F}$).  
*RPN Sequence:* `L {{key:ENTER}} C {{key:×}} {{key:√x}} 2 {{key:×}} {{key:π}} {{key:×}} {{key:1/x}}`  
*Benchmark:* $L = 10.0 \times 10^{-3}\text{ H}, C = 100.0 \times 10^{-12}\text{ F}$.  
*Target Value:* **`159154.9`** $\text{Hz}$ ($159.15\text{ kHz}$).  

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `10 {{key:E}} 3 {{key:+/-}} {{key:ENTER}} 100 {{key:E}} 12 {{key:+/-}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 1.0000E-12 | Product $LC = 1.0 \times 10^{-12}\text{ s}^2$ |
| 02 | `{{key:√x}}` | 0.00 | 0.00 | 0.00 | 1.0000E-6 | Radical $\sqrt{LC} = 1.0 \times 10^{-6}\text{ s}$ |
| 03 | `2 {{key:×}} {{key:π}} {{key:×}} {{key:1/x}}` | 0.00 | 0.00 | 0.00 | 159154.94 | Resonant frequency $f_0 = 159.155\text{ kHz}$ |

---

#### Equation E.34: RLC Series AC Total Impedance
$$Z = \sqrt{R^2 + \left(2 \pi f L - \frac{1}{2 \pi f C}\right)^2}$$
*Variables:* $R (\Omega)$, $L (\text{H})$, $C (\text{F})$, $f (\text{Hz})$.  
*RPN Sequence:* `2 {{key:π}} {{key:×}} f {{key:×}} {{key:STO}} A L {{key:×}} {{key:RCL}} A C {{key:×}} {{key:1/x}} {{key:-}} {{key:x²}} R {{key:x²}} {{key:+}} {{key:√x}}`  
*Benchmark:* $R = 50.0\,\Omega, L = 0.05\text{ H}, C = 10.0 \times 10^{-6}\text{ F}, f = 120.0\text{ Hz}$.  
*Target Value:* **`107.412`** $\Omega$.

---

#### Equation E.35: Quality Factor of Resonant Circuit
$$Q = \frac{1}{R} \sqrt{\frac{L}{C}}$$
*Variables:* $R (\Omega)$, $L (\text{H})$, $C (\text{F})$.  
*RPN Sequence:* `L {{key:ENTER}} C {{key:÷}} {{key:√x}} R {{key:÷}}`  
*Benchmark:* $R = 8.0\,\Omega, L = 2.5 \times 10^{-3}\text{ H}, C = 47.0 \times 10^{-9}\text{ F}$.  
*Target Value:* **`28.813`**.

---

#### Equation E.36: Decibel Power Gain Ratio
$$\text{dB} = 10 \log_{10}\left(\frac{P_2}{P_1}\right)$$
*Variables:* $P_1$ (input power), $P_2$ (output power).  
*RPN Sequence:* `P2 {{key:ENTER}} P1 {{key:÷}} {{key:LOG}} 10 {{key:×}}`  
*Benchmark:* $P_1 = 0.025\text{ W}, P_2 = 120.0\text{ W}$.  
*Target Value:* **`36.8124`** $\text{dB}$.

---

### Section 5: Wave Mechanics, Acoustics & Physical Optics

Equations E.37–E.44 model geometric refraction, thin-lens imaging (`{{key:x∥y}}`), acoustic Doppler shifts, room reverberation, and optical diffraction.

#### Equation E.37: Snell's Law of Refraction
$$\theta_2 = \arcsin\left(\frac{n_1 \sin\theta_1}{n_2}\right)$$
*Variables:* $n_1, n_2$ (refractive indices), $\theta_1$ (angle of incidence, degrees).  
*RPN Sequence in `{{key:DEG}}` Mode:* `theta1 {{key:SIN}} n1 {{key:×}} n2 {{key:÷}} {{key:ASIN}}`  
*Benchmark:* $n_1 = 1.0003\text{ (air)}, n_2 = 1.52\text{ (crown glass)}, \theta_1 = 45.0^\circ$.  
*Target Value:* **`27.7297`** $^\circ$.

---

#### Equation E.38: Gaussian Thin Lens Equation via `{{key:x∥y}}`

$$f = \frac{d_o \cdot d_i}{d_o + d_i} = d_o \parallel d_i$$
*Variables:* $d_o$ (object distance), $d_i$ (image distance).  
*RPN Sequence:* `do {{key:ENTER}} di {{key:x∥y}}`  
*Benchmark:* $d_o = 30.0\text{ cm}, d_i = 60.0\text{ cm}$.  
*Target Value:* **`20.0`** $\text{cm}$.  

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `30 {{key:ENTER}}` | 0.00 | 0.00 | 30.0000 | 30.0000 | Stage object distance $d_o = 30.0\text{ cm}$ in $Y$ |
| 02 | `60 {{key:x∥y}}` | 0.00 | 0.00 | 0.00 | 20.0000 | Thin-lens focal length $f = d_o \parallel d_i = 20.0\text{ cm}$ |

---

#### Equation E.39: Compound Optical Microscope Magnification
$$M = -\left(\frac{L_{\text{tube}}}{f_{\text{obj}}}\right) \left(\frac{d_{\text{near}}}{f_{\text{eye}}}\right)$$
*Variables:* $L_{\text{tube}} = 160\text{ mm}, d_{\text{near}} = 250\text{ mm}$, focal lengths $f_{\text{obj}}, f_{\text{eye}} (\text{mm})$.  
*RPN Sequence:* `160 {{key:ENTER}} fobj {{key:÷}} 250 {{key:ENTER}} feye {{key:÷}} {{key:×}} {{key:+/-}}`  
*Benchmark:* $f_{\text{obj}} = 4.0\text{ mm}, f_{\text{eye}} = 25.0\text{ mm}$.  
*Target Value:* **`-400.0`** ($\times 400$ angular magnification).

---

#### Equation E.40: Acoustic Doppler Frequency Shift (Moving Source)
$$f' = f_0 \left(\frac{v}{v - v_s}\right)$$
*Variables:* $f_0$ (source frequency, $\text{Hz}$), $v = 343.0\text{ m/s}$ (speed of sound), $v_s$ (approach speed, $\text{m/s}$).  
*RPN Sequence:* `343 {{key:ENTER}} vs {{key:-}} 343 {{key:x⇄y}} {{key:÷}} f0 {{key:×}}`  
*Benchmark:* $f_0 = 500.0\text{ Hz}, v_s = 35.0\text{ m/s}$.  
*Target Value:* **`556.818`** $\text{Hz}$.

---

#### Equation E.41: Sound Pressure Decibel Level
$$L_p = 20 \log_{10}\left(\frac{P_{\text{rms}}}{P_0}\right)$$
*Variables:* $P_{\text{rms}} (\text{Pa})$, reference $P_0 = 20.0 \times 10^{-6}\text{ Pa}$.  
*RPN Sequence:* `Prms {{key:ENTER}} 20 {{key:E}} 6 {{key:+/-}} {{key:÷}} {{key:LOG}} 20 {{key:×}}`  
*Benchmark:* $P_{\text{rms}} = 0.632\text{ Pa}$.  
*Target Value:* **`90.0`** $\text{dB}$ SPL.

---

#### Equation E.42: Sabine Reverberation Time for Architectural Enclosure
$$RT_{60} = \frac{0.161 V}{A_{\text{total}}}$$
*Variables:* $V$ (room volume, $\text{m}^3$), $A_{\text{total}} = \sum S_i \alpha_i$ (metric sabins).  
*RPN Sequence:* `0.161 {{key:ENTER}} V {{key:×}} Atot {{key:÷}}`  
*Benchmark:* $V = 850.0\text{ m}^3, A_{\text{total}} = 110.0\text{ sabins}$.  
*Target Value:* **`1.244`** $\text{s}$.

---

#### Equation E.43: Optical Diffraction Grating Wavelength
$$\lambda = \frac{d \sin\theta}{m}$$
*Variables:* $d$ (groove spacing, $\text{m}$), $\theta$ (diffraction angle, degrees), $m$ (diffraction order).  
*RPN Sequence in `{{key:DEG}}` Mode:* `theta {{key:SIN}} d {{key:×}} m {{key:÷}}`  
*Benchmark:* $d = 1.6667 \times 10^{-6}\text{ m}$ ($600\text{ lines/mm}$), $\theta = 22.45^\circ, m = 1$.  
*Target Value:* **`6.365 × 10⁻⁷`** $\text{m}$ ($636.5\text{ nm}$).

---

#### Equation E.44: Numerical Aperture of Optical Fiber
$$NA = \sqrt{n_{\text{core}}^2 - n_{\text{clad}}^2}$$
*Variables:* $n_{\text{core}}, n_{\text{clad}}$ (refractive indices).  
*RPN Sequence:* `ncore {{key:x²}} nclad {{key:x²}} {{key:-}} {{key:√x}}`  
*Benchmark:* $n_{\text{core}} = 1.482, n_{\text{clad}} = 1.450$.  
*Target Value:* **`0.3063`**.

---

### Section 6: Nuclear, Atomic & Relativistic Physics

Equations E.45–E.51 link relativistic mass-energy and Lorentz time dilation with quantum photon energy, de Broglie matter waves, and radioactive decay.

#### Equation E.45: Einstein Mass-Energy Equivalence
$$E = m c^2$$
*Variables:* $m$ (mass, $\text{kg}$), $c = 299,792,458\text{ m/s}$.  
*RPN Sequence:* `299792458 {{key:x²}} m {{key:×}}`  
*Benchmark:* $m = 1.0 \times 10^{-3}\text{ kg}$ ($1\text{ gram}$).  
*Target Value:* **`8.98755 × 10¹³`** $\text{J}$ ($89.88\text{ TJ}$).  

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `299792458 {{key:x²}}` | 0.00 | 0.00 | 0.00 | 8.9876E16 | Square speed of light $c^2 = 8.98755 \times 10^{16}\text{ m}^2/\text{s}^2$ |
| 02 | `1 {{key:E}} 3 {{key:+/-}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 8.9876E13 | Rest-mass energy $E = mc^2 = 8.98755 \times 10^{13}\text{ J}$ |

---

#### Equation E.46: Planck-Einstein Photon Energy
$$E_{\text{photon}} = \frac{h c}{\lambda}$$
*Variables:* $h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}, c = 299,792,458\text{ m/s}, \lambda (\text{m})$.  
*RPN Sequence:* `6.62607015 {{key:E}} 34 {{key:+/-}} {{key:ENTER}} 299792458 {{key:×}} lambda {{key:÷}}`  
*Benchmark:* $\lambda = 500.0 \times 10^{-9}\text{ m}$ (green photon).  
*Target Value:* **`3.9729 × 10⁻¹⁹`** $\text{J}$ ($2.48\text{ eV}$).

---

#### Equation E.47: de Broglie Particle Wavelength
$$\lambda = \frac{h}{m v}$$
*Variables:* $h = 6.62607015 \times 10^{-34}, m (\text{kg}), v (\text{m/s})$.  
*RPN Sequence:* `6.62607015 {{key:E}} 34 {{key:+/-}} {{key:ENTER}} m {{key:÷}} v {{key:÷}}`  
*Benchmark:* $m = 9.1093837 \times 10^{-31}\text{ kg}$ (electron), $v = 2.0 \times 10^6\text{ m/s}$.  
*Target Value:* **`3.6370 × 10⁻¹⁰`** $\text{m}$ ($0.3637\text{ nm}$).

---

#### Equation E.48: Relativistic Lorentz Factor ($\gamma$)
$$\gamma = \frac{1}{\sqrt{1 - \beta^2}} = \frac{1}{\sqrt{1 - (v/c)^2}}$$
*Variables:* $\beta = v / c$.  
*RPN Sequence:* `beta {{key:x²}} 1 {{key:x⇄y}} {{key:-}} {{key:√x}} {{key:1/x}}`  
*Benchmark:* $\beta = 0.95$.  
*Target Value:* **`3.20256`**.  

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `0.95 {{key:x²}}` | 0.00 | 0.00 | 0.00 | 0.902500 | Square normalized velocity $\beta^2 = 0.902500$ |
| 02 | `1 {{key:x⇄y}} {{key:-}}` | 0.00 | 0.00 | 0.00 | 0.097500 | Complement $1 - \beta^2 = 0.097500$ |
| 03 | `{{key:√x}} {{key:1/x}}` | 0.00 | 0.00 | 0.00 | 3.202563 | Lorentz time-dilation factor $\gamma = 3.202563$ |

---

#### Equation E.49: Relativistic Momentum
$$p = \gamma m v = \frac{m v}{\sqrt{1 - (v/c)^2}}$$
*Variables:* $m$ (rest mass), $v$ (velocity).  
*RPN Sequence:* `v {{key:ENTER}} 299792458 {{key:÷}} {{key:x²}} 1 {{key:x⇄y}} {{key:-}} {{key:√x}} m {{key:ENTER}} v {{key:×}} {{key:x⇄y}} {{key:÷}}`  
*Benchmark:* $m = 1.67262 \times 10^{-27}\text{ kg}$ (proton), $v = 0.85 c = 2.548236 \times 10^8\text{ m/s}$.  
*Target Value:* **`8.0906 × 10⁻¹⁹`** $\text{kg}\cdot\text{m/s}$.

---

#### Equation E.50: Radioactive Decay Exponential Law
$$N(t) = N_0 e^{-\lambda t} = N_0 \left(\frac{1}{2}\right)^{t / t_{1/2}}$$
*Variables:* $N_0$ (initial activity), $t_{1/2}$ (half-life), $t$ (elapsed time).  
*RPN Sequence:* `0.5 {{key:ENTER}} t {{key:ENTER}} thalf {{key:÷}} {{key:yˣ}} N0 {{key:×}}`  
*Benchmark:* $N_0 = 10000.0\text{ Bq}, t_{1/2} = 5.27\text{ years}, t = 15.0\text{ years}$ (Cobalt-60).  
*Target Value:* **`1388.9`** $\text{Bq}$.

---

#### Equation E.51: Rydberg Equation for Hydrogen Spectral Series
$$\frac{1}{\lambda} = R_{\infty} \left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)$$
*Variables:* $R_\infty = 1.0973731568 \times 10^7\text{ m}^{-1}$, principal quantum numbers $n_1 < n_2$.  
*RPN Sequence:* `n1 {{key:x²}} {{key:1/x}} n2 {{key:x²}} {{key:1/x}} {{key:-}} 1.0973731568 {{key:E}} 7 {{key:×}} {{key:1/x}}`  
*Benchmark:* $n_1 = 2, n_2 = 3$ (Balmer $H_\alpha$ red line).  
*Target Value:* **`6.5647 × 10⁻⁷`** $\text{m}$ ($656.47\text{ nm}$).

---

### Section 7: Coordinate Geometry, Mensuration & Solid Geometry

Equations E.52–E.66 provide planar and spherical mensuration formulas for polygons, circular segments, ellipses, parabolic arches, and triangle cevians.

#### Equation E.52: Volume and Surface Area of Sphere
$$V = \frac{4}{3} \pi r^3, \quad A = 4 \pi r^2$$
*Variables:* $r$ (radius).  
*RPN Sequences:*  
- Volume: `r {{key:ENTER}} 3 {{key:yˣ}} {{key:π}} {{key:×}} 4 {{key:×}} 3 {{key:÷}}`  
- Area: `r {{key:x²}} {{key:π}} {{key:×}} 4 {{key:×}}`  
*Benchmark:* $r = 7.50\text{ cm}$.  
*Target Values:* Volume = **`1767.146`** $\text{cm}^3$; Area = **`706.858`** $\text{cm}^2$.  
*Stack Trace Table (Volume):*

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `7.5 {{key:ENTER}} 3 {{key:yˣ}}` | 0.00 | 0.00 | 0.00 | 421.8750 | Cube sphere radius $r^3 = 421.8750\text{ cm}^3$ |
| 02 | `{{key:π}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 1325.3594 | Scale by $\pi$: $\pi r^3 = 1325.3594\text{ cm}^3$ |
| 03 | `4 {{key:×}} 3 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 1767.1459 | Sphere volume $V = \frac{4}{3}\pi r^3 = 1767.1459\text{ cm}^3$ |

---

#### Equation E.53: Right Circular Cone Volume & Lateral Surface Area
$$V = \frac{1}{3} \pi r^2 h, \quad A_{\text{lat}} = \pi r \sqrt{r^2 + h^2}$$
*Variables:* $r$ (base radius), $h$ (height).  
*RPN Sequences:*  
- Volume: `r {{key:x²}} h {{key:×}} {{key:π}} {{key:×}} 3 {{key:÷}}`  
- Lateral Area: `r {{key:x²}} h {{key:x²}} {{key:+}} {{key:√x}} r {{key:×}} {{key:π}} {{key:×}}`  
*Benchmark:* $r = 6.0\text{ cm}, h = 14.0\text{ cm}$.  
*Target Values:* Volume = **`527.788`** $\text{cm}^3$; Lateral Area = **`287.015`** $\text{cm}^2$.

---

#### Equation E.54: Frustum of Right Circular Cone Volume
$$V = \frac{1}{3} \pi h (R^2 + R r + r^2)$$
*Variables:* $R$ (lower base radius), $r$ (upper base radius), $h$ (height).  
*RPN Sequence:* `R {{key:x²}} R {{key:ENTER}} r {{key:×}} {{key:+}} r {{key:x²}} {{key:+}} h {{key:×}} 3 {{key:÷}} {{key:π}} {{key:×}}`  
*Benchmark:* $R = 8.0\text{ cm}, r = 3.0\text{ cm}, h = 12.0\text{ cm}$.  
*Target Value:* **`1218.938`** $\text{cm}^3$.  

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `8 {{key:x²}}` | 0.00 | 0.00 | 0.00 | 64.0000 | Lower base radius squared $R^2 = 64.0000\text{ cm}^2$ |
| 02 | `8 {{key:ENTER}} 3 {{key:×}} {{key:+}}` | 0.00 | 0.00 | 0.00 | 88.0000 | Add cross-product $R^2 + Rr = 88.0000\text{ cm}^2$ |
| 03 | `3 {{key:x²}} {{key:+}}` | 0.00 | 0.00 | 0.00 | 97.0000 | Add upper base radius squared $R^2 + Rr + r^2 = 97.0000\text{ cm}^2$ |
| 04 | `12 {{key:×}} 3 {{key:÷}} {{key:π}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 1218.9380 | Frustum volume $V = 1218.9380\text{ cm}^3$ |

---

#### Equation E.55: Torus Volume and Total Surface Area
$$V = 2 \pi^2 R r^2, \quad A = 4 \pi^2 R r$$
*Variables:* $R$ (major radius from center to tube center), $r$ (minor tube radius).  
*RPN Sequences:*  
- Volume: `r {{key:x²}} R {{key:×}} 2 {{key:×}} {{key:π}} {{key:x²}} {{key:×}}`  
- Surface Area: `R {{key:ENTER}} r {{key:×}} 4 {{key:×}} {{key:π}} {{key:x²}} {{key:×}}`  
*Benchmark:* $R = 12.0\text{ cm}, r = 2.5\text{ cm}$.  
*Target Values:* Volume = **`1480.44`** $\text{cm}^3$; Area = **`1184.35`** $\text{cm}^2$.

---

#### Equation E.56: Heron's Formula for Arbitrary Triangle Area
$$A = \sqrt{s(s - a)(s - b)(s - c)}, \quad s = \frac{a + b + c}{2}$$
*Variables:* Side lengths $a, b, c$.  
*RPN Sequence:* `a {{key:ENTER}} b {{key:+}} c {{key:+}} 2 {{key:÷}} {{key:STO}} S a {{key:-}} {{key:RCL}} S b {{key:-}} {{key:×}} {{key:RCL}} S c {{key:-}} {{key:×}} {{key:RCL}} S {{key:×}} {{key:√x}}`  
*Benchmark:* $a = 13.0, b = 14.0, c = 15.0$ (semiperimeter $s = 21.0$).  
*Target Value:* **`84.000`**.  

| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `13 {{key:ENTER}} 14 {{key:+}} 15 {{key:+}} 2 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 21.0000(s) | 21.0000 |
| 02 | `{{key:STO}} S 13 {{key:-}}` | 0.00 | 0.00 | 0.00 | 8.0000(s-a) | 8.0000 |
| 03 | `{{key:RCL}} S 14 {{key:-}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 56.0000 | 56.0000 |
| 04 | `{{key:RCL}} S 15 {{key:-}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 336.0000 | 336.0000 |
| 05 | `{{key:RCL}} S {{key:×}} {{key:√x}}` | 0.00 | 0.00 | 0.00 | 84.0000 | 84.0000 |

---

#### Equation E.57: Law of Cosines for Arbitrary Triangle
$$c = \sqrt{a^2 + b^2 - 2 a b \cos C}$$
*Variables:* Sides $a, b$, included angle $C$ (degrees).  
*RPN Sequence in `{{key:DEG}}` Mode:* `a {{key:x²}} b {{key:x²}} {{key:+}} 2 {{key:ENTER}} a {{key:×}} b {{key:×}} C {{key:COS}} {{key:×}} {{key:-}} {{key:√x}}`  
*Benchmark:* $a = 18.0, b = 25.0, C = 62.0^\circ$.  
*Target Value:* **`22.956`**.

---

#### Equation E.58: Great Circle Spherical Distance (Haversine Formula)
$$d = 2 R \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta\phi}{2}\right) + \cos\phi_1 \cos\phi_2 \sin^2\left(\frac{\Delta\lambda}{2}\right)}\right)$$
*Variables:* $R = 6371.0\text{ km}$, latitudes $\phi_1, \phi_2$, longitudes $\lambda_1, \lambda_2$.  
*RPN Sequence in `{{key:DEG}}` Mode:*  
`phi2 {{key:ENTER}} phi1 {{key:-}} 2 {{key:÷}} {{key:SIN}} {{key:x²}} phi1 {{key:COS}} phi2 {{key:COS}} {{key:×}} lam2 {{key:ENTER}} lam1 {{key:-}} 2 {{key:÷}} {{key:SIN}} {{key:x²}} {{key:×}} {{key:+}} {{key:√x}} {{key:ASIN}} 2 {{key:×}} 6371.0 {{key:×}}`  
*Benchmark:* New York ($40.7128^\circ\text{N}, 74.0060^\circ\text{W}$) to London ($51.5074^\circ\text{N}, 0.1278^\circ\text{W}$).  
*Target Value:* **`5570.2`** $\text{km}$ ($3461.2\text{ miles}$).

---

#### Equation E.59: Circular Sector Area and Arc Length
$$s = r \theta, \quad A = \frac{1}{2} r^2 \theta \quad (\theta\text{ in radians})$$
*Variables:* Radius $r$, central angle $\theta$.  
Direct scaling of circle perimeter ($2\pi r$) and disk area ($\pi r^2$) by aperture fraction $(\theta / 2\pi)$.  
*RPN Sequences:*  
- Arc Length: `r {{key:ENTER}} theta {{key:×}}`  
- Sector Area: `r {{key:x²}} theta {{key:×}} 2 {{key:÷}}`  
*Benchmark:* $r = 12.0\text{ cm}, \theta = 1.047198\text{ rad}$ ($60.0^\circ$).  
*Target Values:* Arc Length = **`12.566`** $\text{cm}$; Area = **`75.398`** $\text{cm}^2$.

---

#### Equation E.60: Circular Segment Area
$$A = \frac{1}{2} r^2 (\theta - \sin\theta) \quad (\theta\text{ in radians})$$
*Variables:* Radius $r$, central angle $\theta$.  
Area of the circular sector minus the internal triangular chord core ($\frac{1}{2} r^2 \sin\theta$). Essential in hydraulic pipe fill levels and pressure vessel liquid volumes.  
*RPN Sequence in `RAD` Mode:* `theta {{key:ENTER}} {{key:SIN}} {{key:-}} r {{key:x²}} {{key:×}} 2 {{key:÷}}`  
*Benchmark:* $r = 8.0\text{ m}, \theta = 1.250\text{ rad}$.  
*Target Value:* **`9.633`** $\text{m}^2$.

---

#### Equation E.61: Circular Annulus & Annular Sector Area
$$A = \pi (R^2 - r^2) = \pi (R - r)(R + r), \quad A_{\text{sector}} = \frac{\theta}{2} (R - r)(R + r)$$
*Variables:* Outer radius $R$, inner bore radius $r$, central angle $\theta$ (radians).  
Difference between concentric disks. Evaluated in RPN via difference-of-squares factorization to preserve precision for thin-walled gaskets ($R \approx r$).  
*RPN Sequence:* `R {{key:ENTER}} r {{key:-}} R {{key:ENTER}} r {{key:+}} {{key:×}} {{key:π}} {{key:×}}`  
*Benchmark:* $R = 15.0\text{ cm}, r = 10.0\text{ cm}$.  
*Target Value:* **`392.699`** $\text{cm}^2$.

---

#### Equation E.62: Ellipse Area & Ramanujan's Second Perimeter Approximation
$$A = \pi a b, \quad h = \frac{(a - b)^2}{(a + b)^2}, \quad P \approx \pi (a + b) \left[ 1 + \frac{3h}{10 + \sqrt{4 - 3h}} \right]$$
*Variables:* Semimajor axis $a$, semiminor axis $b$.  
2D affine dilation of the unit circle. Ramanujan's second formula approximates the complete elliptic integral with sub-ppm accuracy.  
*RPN Sequences:*  
- Area: `a {{key:ENTER}} b {{key:×}} {{key:π}} {{key:×}}`  
- Perimeter: `a {{key:ENTER}} b {{key:-}} a {{key:ENTER}} b {{key:+}} {{key:÷}} {{key:x²}} {{key:STO}} A 3 {{key:×}} 4 {{key:x⇄y}} {{key:-}} {{key:√x}} 10 {{key:+}} {{key:1/x}} 3 {{key:×}} {{key:RCL}} A {{key:×}} 1 {{key:+}} a {{key:ENTER}} b {{key:+}} {{key:×}} {{key:π}} {{key:×}}`  
*Benchmark:* $a = 10.0\text{ cm}, b = 6.0\text{ cm}$.  
*Target Values:* Area = **`188.496`** $\text{cm}^2$; Perimeter = **`51.054`** $\text{cm}$.

---

#### Equation E.63: Parabolic Segment Area (Archimedes' Quadrature)
$$A = \frac{2}{3} b h$$
*Variables:* Base chord width $b$, perpendicular vertex altitude $h$.  
Archimedes' mechanical quadrature: the area under a parabolic arch is exactly $\frac{4}{3}$ of the inscribed triangle ($\frac{1}{2}bh$). Fundamental for beam bending moment diagrams and solar trough reflectors.  
*RPN Sequence:* `b {{key:ENTER}} h {{key:×}} 2 {{key:×}} 3 {{key:÷}}`  
*Benchmark:* $b = 18.0\text{ m}, h = 6.0\text{ m}$.  
*Target Value:* **`72.000`** $\text{m}^2$.

---

#### Equation E.64: Regular $n$-gon Area, Inradius & Circumradius
$$A = \frac{1}{4} n s^2 \cot\left(\frac{\pi}{n}\right), \quad r = \frac{s}{2 \tan(\pi/n)}, \quad R = \frac{s}{2 \sin(\pi/n)}$$
*Variables:* Number of sides $n$, side length $s$.  
Symmetric decomposition into $n$ central isosceles triangles. Dictates bolt head profiles, polygonal extrusions, and crystal lattices.  
*RPN Sequence (Area):* `{{key:π}} n {{key:÷}} {{key:TAN}} {{key:1/x}} s {{key:x²}} {{key:×}} n {{key:×}} 4 {{key:÷}}`  
*Benchmark:* Regular Hexagon ($n = 6$), side $s = 5.0\text{ cm}$.  
*Target Value:* **`64.952`** $\text{cm}^2$.

---

#### Equation E.65: Brahmagupta's Formula & Ptolemy's Theorem for Cyclic Quadrilaterals
$$A = \sqrt{(s-a)(s-b)(s-c)(s-d)}, \quad s = \frac{a+b+c+d}{2}, \quad a c + b d = e f$$
*Variables:* Sides $a, b, c, d$, diagonals $e, f$.  
4-sided cyclic generalization of Heron's formula. Yields maximum enclosure area for any quadrilateral with fixed side lengths.  
*RPN Sequence:* Compute $s \to$ store $\to$ multiply $(s-a)(s-b)(s-c)(s-d) \to$ `{{key:√x}}`.  
*Benchmark:* $a = 3.0, b = 4.0, c = 5.0, d = 6.0$ ($s = 9.0$).  
*Target Value:* **`18.974`**.

---

#### Equation E.66: Stewart's Theorem for Triangle Cevians
$$m a n + d^2 a = b^2 m + c^2 n \implies d = \sqrt{\frac{b^2 m + c^2 n - m a n}{a}}$$
*Variables:* Triangle sides $a, b, c$; cevian of length $d$ dividing side $a$ into segments $m$ and $n$ ($m + n = a$).  
Rotational moment of inertia balance across a triangular plate; resolves medians, angle bisectors, and structural truss struts.  
*Benchmark:* $a = 10.0, b = 8.0, c = 6.0$ (right triangle), median to hypotenuse ($m = 5.0, n = 5.0$).  
*Target Value:* **`5.000`**.

---

### Section 8: 3D Solid Geometry & Mensuration Master Compendium

Equations E.67–E.72 evaluate volumes and surface areas of spherical domes, pyramidal frustums, ellipsoids, paraboloids, and general prismoids.

#### Equation E.67: Spherical Cap (Dome) & Spherical Zone Volume
$$V_{\text{cap}} = \frac{1}{3} \pi h^2 (3 R - h), \quad A_{\text{dome}} = 2 \pi R h$$
$$V_{\text{zone}} = \frac{\pi h}{6} (3 r_1^2 + 3 r_2^2 + h^2)$$
*Variables:* Sphere radius $R$, cap height $h$, zone radii $r_1, r_2$.  
Disk integration of spherical layers via Archimedes' cylinder balance. Essential for liquid propellant tanks, geodesic domes, and acoustic lenses.  
*RPN Sequence (Cap Volume):* `3 {{key:ENTER}} R {{key:×}} h {{key:-}} h {{key:x²}} {{key:×}} {{key:π}} {{key:×}} 3 {{key:÷}}`  
*Benchmark:* Sphere $R = 10.0\text{ cm}$, cap height $h = 3.0\text{ cm}$.  
*Target Values:* Volume = **`254.469`** $\text{cm}^3$; Dome Area = **`188.496`** $\text{cm}^2$.

---

#### Equation E.68: Frustum of Regular Pyramid Volume
$$V = \frac{h}{3} (A_1 + A_2 + \sqrt{A_1 A_2})$$
*Variables:* Lower base area $A_1$, upper base area $A_2$, perpendicular height $h$.  
Heronian mean of cross-sectional areas; models architectural monuments, concrete foundations, and hopper bins.  
*RPN Sequence:* `A1 {{key:ENTER}} A2 {{key:×}} {{key:√x}} A1 {{key:+}} A2 {{key:+}} h {{key:×}} 3 {{key:÷}}`  
*Benchmark:* $A_1 = 36.0\text{ m}^2, A_2 = 16.0\text{ m}^2, h = 9.0\text{ m}$.  
*Target Value:* **`228.000`** $\text{m}^3$.

---

#### Equation E.69: Ellipsoid Volume
$$V = \frac{4}{3} \pi a b c$$
*Variables:* Semimajor axes $a, b, c$.  
3D affine dilation of the unit sphere. Models oblate and prolate planetary bodies, optical ellipsoidal reflectors, and aerodynamic radomes.  
*RPN Sequence:* `a {{key:ENTER}} b {{key:×}} c {{key:×}} {{key:π}} {{key:×}} 4 {{key:×}} 3 {{key:÷}}`  
*Benchmark:* $a = 6.0\text{ cm}, b = 4.0\text{ cm}, c = 3.0\text{ cm}$.  
*Target Value:* **`301.593`** $\text{cm}^3$.

---

#### Equation E.70: Paraboloid of Revolution Volume
$$V = \frac{1}{2} \pi r^2 h$$
*Variables:* Base radius $r$, central depth $h$.  
Archimedes' law of paraboloids: volume is exactly half of the bounding cylinder. Primary profile for radar dishes, headlamp reflectors, and liquid mirror telescopes.  
*RPN Sequence:* `r {{key:x²}} h {{key:×}} {{key:π}} {{key:×}} 2 {{key:÷}}`  
*Benchmark:* $r = 4.0\text{ m}, h = 3.0\text{ m}$.  
*Target Value:* **`75.398`** $\text{m}^3$.

---

#### Equation E.71: Cylindrical Ungula (Hoof) Volume
$$V = \frac{2}{3} r^3 \tan\alpha$$
*Variables:* Cylinder radius $r$, cutting plane angle $\alpha$ passing through base diameter.  
Slicing a circular cylinder with an inclined plane passing directly through its base diameter. Models mitered pipe junctions and fluid flow deflectors.  
*RPN Sequence in `DEG` Mode:* `r {{key:ENTER}} 3 {{key:yˣ}} alpha {{key:TAN}} {{key:×}} 2 {{key:×}} 3 {{key:÷}}`  
*Benchmark:* $r = 6.0\text{ cm}, \alpha = 45.0^\circ$.  
*Target Value:* **`144.000`** $\text{cm}^3$.

---

#### Equation E.72: Universal Prismoidal Formula (Simpson's 3D Rule)
$$V = \frac{h}{6} (A_{\text{top}} + 4 A_{\text{mid}} + A_{\text{bot}})$$
*Variables:* Extrusion height $h$, top area $A_{\text{top}}$, mid-height area $A_{\text{mid}}$, base area $A_{\text{bot}}$.  
Simpson's cubic quadrature along height: exact for any solid whose cross-sectional area varies as a quadratic or cubic polynomial in $z$ (prisms, pyramids, cones, spheres, paraboloids).  
*RPN Sequence:* `Amid {{key:ENTER}} 4 {{key:×}} Atop {{key:+}} Abot {{key:+}} h {{key:×}} 6 {{key:÷}}`  
*Benchmark:* Frustum with $A_{\text{top}} = 16.0, A_{\text{mid}} = 36.0, A_{\text{bot}} = 64.0, h = 6.0$.  
*Target Value:* **`224.000`**.

---

### Section 9: Contest Financial Mathematics, Amortization & TVM

Equations E.73–E.77 summarize closed-form compound-interest recipes for ordinary annuities, loan amortization payments, sinking funds, and perpetuities.

#### Equation E.73: Present Value of an Ordinary Annuity
$$PV = PMT \left[ \frac{1 - (1 + i)^{-N}}{i} \right]$$
*Variables:* Periodic payment $PMT$, rate per period $i$, total periods $N$.  
Sum of discounted future cash flow geometric series. Determines loan balances, actuarial pension reserves, and bond valuation.  
*RPN Sequence:* `1 {{key:ENTER}} i {{key:+}} N {{key:+/-}} {{key:yˣ}} 1 {{key:x⇄y}} {{key:-}} i {{key:÷}} PMT {{key:×}}`  
*Benchmark:* $PMT = 500\text{ USD}, i = 0.005$ ($6\%$ APR monthly), $N = 36\text{ months}$.  
*Target Value:* **`16,429.62`** $\text{USD}$.

---

#### Equation E.74: Future Value of an Ordinary Annuity
$$FV = PMT \left[ \frac{(1 + i)^N - 1}{i} \right]$$
*Variables:* Periodic savings deposit $PMT$, rate per period $i$, total periods $N$.  
Compound growth accumulation of periodic deposits. Solves retirement nest-egg and university savings goals.  
*RPN Sequence:* `1 {{key:ENTER}} i {{key:+}} N {{key:yˣ}} 1 {{key:-}} i {{key:÷}} PMT {{key:×}}`  
*Benchmark:* $PMT = 250\text{ USD}, i = 0.006$ ($7.2\%$ APR monthly), $N = 60\text{ months}$.  
*Target Value:* **`17,984.66`** $\text{USD}$.

---

#### Equation E.75: Loan Amortization Periodic Payment
$$PMT = PV \left[ \frac{i}{1 - (1 + i)^{-N}} \right]$$
*Variables:* Principal loan amount $PV$, interest rate per period $i$, total payment periods $N$.  
Capital recovery factor: inverts annuity PV to find fixed monthly installment liquidating principal and interest.  
*RPN Sequence:* `1 {{key:ENTER}} i {{key:+}} N {{key:+/-}} {{key:yˣ}} 1 {{key:x⇄y}} {{key:-}} i {{key:x⇄y}} {{key:÷}} PV {{key:×}}`  
*Benchmark:* $PV = 25,000\text{ USD}, i = 0.0045$ ($5.4\%$ APR monthly), $N = 48\text{ months}$.  
*Target Value:* **`579.98`** $\text{USD}$.

---

#### Equation E.76: Sinking Fund Periodic Savings Payment
$$PMT = FV \left[ \frac{i}{(1 + i)^N - 1} \right]$$
*Variables:* Target future balance $FV$, interest rate per period $i$, total saving periods $N$.  
Periodic contribution required to accumulate a predetermined future balloon payment or capital equipment replacement fund.  
*RPN Sequence:* `1 {{key:ENTER}} i {{key:+}} N {{key:yˣ}} 1 {{key:-}} i {{key:x⇄y}} {{key:÷}} FV {{key:×}}`  
*Benchmark:* Target $FV = 50,000\text{ USD}, i = 0.005$ ($6\%$ APR monthly), $N = 120\text{ months}$.  
*Target Value:* **`305.10`** $\text{USD}$.

---

#### Equation E.77: Flat & Growing Perpetuities
$$PV_{\text{flat}} = \frac{PMT}{i}, \quad PV_{\text{growing}} = \frac{PMT}{i - g}$$
*Variables:* Annual dividend payment $PMT$, discount rate $i$, constant dividend growth rate $g$ ($i > g$).  
Gordon growth model; sum of infinite geometric cash flow series with continuous compounding. Dictates preferred stock and endowment valuations.  
*RPN Sequences:*  
- Flat: `PMT {{key:ENTER}} i {{key:÷}}`  
- Growing: `PMT {{key:ENTER}} i {{key:ENTER}} g {{key:-}} {{key:÷}}`  
*Benchmark:* $PMT = 1,200\text{ USD/yr}, i = 0.06, g = 0.02$.  
*Target Values:* Flat Perpetuity = **`20,000.00`** $\text{USD}$; Growing Perpetuity = **`30,000.00`** $\text{USD}$.

---

### Section 10: Chemistry, Electrochemistry, Chemical Kinetics & Biochemistry

Equations E.78–E.85 cover aqueous acid-base equilibria, Nernst electrochemical potentials, Arrhenius and Michaelis-Menten kinetics, and spectrophotometric absorbance.

#### Equation E.78: pH & Hydronium Ion Activity
$$\text{pH} = -\log_{10}[\text{H}_3\text{O}^+], \quad [\text{H}_3\text{O}^+] = 10^{-\text{pH}}$$
*Variables:* $[\text{H}_3\text{O}^+]$ (molar hydronium ion concentration, $\text{mol/L}$).  
Sørensen logarithmic acidity scale compressing 14 orders of magnitude of aqueous proton activity into a linear 0–14 bench index.  
*RPN Sequence:* `H3O {{key:LOG}} {{key:+/-}}` (Inverse: `pH {{key:+/-}} {{key:10ˣ}}`)  
*Benchmark:* $[\text{H}_3\text{O}^+] = 3.50 \times 10^{-5}\text{ mol/L}$ (`3.5 {{key:E}} 5 {{key:+/-}} {{key:LOG}} {{key:+/-}}`).  
*Target Value:* **`4.4559`**.

---

#### Equation E.79: Henderson–Hasselbalch Buffer Equilibrium
$$\text{pH} = \text{p}K_a + \log_{10}\left(\frac{[\text{A}^-]}{[\text{HA}]}\right)$$
*Variables:* $\text{p}K_a = -\log_{10} K_a$ (acid dissociation constant), $[\text{A}^-]$ (conjugate base molarity), $[\text{HA}]$ (weak acid molarity).  
Governs blood bicarbonate homeostasis ($\text{pH } 7.40$) and analytical laboratory buffer capacity against strong acid/base perturbations.  
*RPN Sequence:* `[A⁻] {{key:ENTER}} [HA] {{key:÷}} {{key:LOG}} pKa {{key:+}}`  
*Benchmark:* Acetate buffer with $\text{p}K_a = 4.76, [\text{A}^-] = 0.25\text{ M}, [\text{HA}] = 0.15\text{ M}$.  
*Target Value:* **`4.9818`**.

---

#### Equation E.80: Nernst Electrochemical Cell Potential
$$E_{\text{cell}} = E^\circ_{\text{cell}} - \frac{R T}{n F} \ln Q$$
*Variables:* $E^\circ_{\text{cell}}$ (standard cell potential, $\text{V}$), $R = 8.31446\text{ J/(mol}\cdot\text{K)}$, $T$ (temperature, $\text{K}$), $n$ (moles of electrons transferred), $F = 96,485.3\text{ C/mol}$, $Q$ (reaction quotient).  
Links Gibbs free energy driving force ($\Delta G = -n F E_{\text{cell}}$) to real-time reactant/product activity ratios in galvanic batteries and biological ion channels.  
*RPN Sequence:* `8.31446 {{key:ENTER}} T {{key:×}} n {{key:÷}} 96485.3 {{key:÷}} Q {{key:LN}} {{key:×}} E0 {{key:x⇄y}} {{key:-}}`  
*Benchmark:* Daniell $\text{Zn/Cu}$ cell: $E^\circ = 1.100\text{ V}, T = 298.15\text{ K}, n = 2, Q = 0.050$.  
*Target Value:* **`1.1385`** $\text{V}$.

---

#### Equation E.81: Arrhenius Chemical Reaction Rate Constant
$$k = A \exp\left(-\frac{E_a}{R T}\right)$$
*Variables:* $A$ (pre-exponential collision frequency factor, $\text{s}^{-1}$), $E_a$ (activation energy barrier, $\text{J/mol}$), $R = 8.31446\text{ J/(mol}\cdot\text{K)}$, $T$ (absolute temperature, $\text{K}$).  
Boltzmann thermal fraction of molecular collisions possessing sufficient kinetic energy to surmount the transition-state activation barrier.  
*RPN Sequence:* `Ea {{key:ENTER}} 8.31446 {{key:÷}} T {{key:÷}} {{key:+/-}} {{key:eˣ}} A {{key:×}}`  
*Benchmark:* $A = 1.25 \times 10^{11}\text{ s}^{-1}, E_a = 75,000\text{ J/mol}, T = 350.0\text{ K}$.  
*Target Value:* **`0.7937`** $\text{s}^{-1}$.

---

#### Equation E.82: Michaelis–Menten Enzyme Saturation Kinetics
$$v_0 = \frac{V_{\max}[S]}{K_m + [S]}$$
*Variables:* $V_{\max}$ (maximum turnover velocity), $[S]$ (substrate concentration), $K_m$ (Michaelis constant: substrate concentration at $0.5\,V_{\max}$).  
Hyperbolic saturation of catalytic active sites; transitions from first-order kinetics ($v_0 \approx \frac{V_{\max}}{K_m}[S]$) at low $[S]$ to zero-order saturation ($v_0 \to V_{\max}$) at high $[S]$.  
*RPN Sequence:* `Vmax {{key:ENTER}} S {{key:×}} Km {{key:ENTER}} S {{key:+}} {{key:÷}}`  
*Benchmark:* $V_{\max} = 140.0\text{ }\mu\text{M/min}, [S] = 15.0\text{ mM}, K_m = 5.0\text{ mM}$.  
*Target Value:* **`105.0000`** $\mu\text{M/min}$.

---

#### Equation E.83: Beer–Lambert Spectrophotometric Absorbance
$$A = \varepsilon \ell c = -\log_{10}\left(\frac{I}{I_0}\right)$$
*Variables:* $\varepsilon$ (molar absorptivity, $\text{L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}$), $\ell$ (optical cuvette path length, $\text{cm}$), $c$ (molar concentration, $\text{mol/L}$), $I/I_0$ (transmittance $T$).  
Differential photon attenuation through an absorbing solution; fundamental calibration equation for UV-Vis spectrophotometry and pulse oximetry.  
*RPN Sequence:* `eps {{key:ENTER}} l {{key:×}} c {{key:×}}` (Transmittance $T = I/I_0$: `A {{key:+/-}} {{key:10ˣ}}`)  
*Benchmark:* NADH assay at $340\text{ nm}$: $\varepsilon = 6,220\text{ L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}, \ell = 1.00\text{ cm}, c = 8.50 \times 10^{-5}\text{ M}$.  
*Target Value:* $A =$ **`0.5287`** ($T = 29.60\%$).

---

#### Equation E.84: Clausius–Clapeyron Vapor Pressure Scaling
$$P_2 = P_1 \exp\left[\frac{\Delta H_{\text{vap}}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right]$$
*Variables:* $P_1, P_2$ (saturation vapor pressures), $\Delta H_{\text{vap}}$ (molar enthalpy of vaporization, $\text{J/mol}$), $R = 8.31446\text{ J/(mol}\cdot\text{K)}$, $T_1, T_2$ (absolute temperatures, $\text{K}$).  
Governs phase-boundary equilibrium slope ($dP/dT = \Delta H / (T \Delta V)$) for vacuum distillation, autoclave sterilization, and atmospheric meteorology.  
*RPN Sequence:* `T1 {{key:1/x}} T2 {{key:1/x}} {{key:-}} dH {{key:×}} 8.31446 {{key:÷}} {{key:eˣ}} P1 {{key:×}}`  
*Benchmark:* Water: $P_1 = 23.76\text{ Torr}$ at $T_1 = 298.15\text{ K}$, find $P_2$ at $T_2 = 323.15\text{ K}$ ($\Delta H_{\text{vap}} = 43,990\text{ J/mol}$).  
*Target Value:* **`93.7330`** $\text{Torr}$.

---

#### Equation E.85: Debye–Hückel Solution Ionic Strength
$$I = \frac{1}{2}\sum_{i=1}^n c_i z_i^2$$
*Variables:* $c_i$ (molar concentration of ion species $i$, $\text{mol/L}$), $z_i$ (integer charge valency of ion $i$).  
Measures total electrostatic shielding density in electrolyte solutions; multivalent ions ($z_i = \pm 2, \pm 3$) weight quadratically via `{{key:x²}}`.  
*RPN Sequence:* `z1 {{key:x²}} c1 {{key:×}} z2 {{key:x²}} c2 {{key:×}} {{key:+}} 2 {{key:÷}}`  
*Benchmark:* $0.10\text{ M }\text{MgCl}_2$ solution ($c_{\text{Mg}^{2+}} = 0.10\text{ M}, z_1 = +2$; $c_{\text{Cl}^-} = 0.20\text{ M}, z_2 = -1$).  
*Target Value:* **`0.3000`** $\text{mol/L}$.

---

### Section 11: Probability, Statistics, Quality Control & Information Theory

Equations E.86–E.93 address discrete probability distributions, Gaussian confidence intervals, Bayesian inference, Six Sigma capability indices, and Shannon channel capacity.

#### Equation E.86: Binomial Probability Mass Function
$$P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}$$
*Variables:* $n$ (independent Bernoulli trials), $k$ (exact number of successes), $p$ (single-trial success probability).  
Exact discrete probability of observing $k$ successes in $n$ trials using the `PROB` menu `{{key:Cn,r}}` combinatorics softkey.  
*RPN Sequence:* `n {{key:ENTER}} k {{key:Cn,r}} p {{key:ENTER}} k {{key:yˣ}} {{key:×}} 1 {{key:ENTER}} p {{key:-}} n {{key:ENTER}} k {{key:-}} {{key:yˣ}} {{key:×}}`  
*Benchmark:* $n = 10\text{ wafer dies}, k = 3\text{ defects}, p = 0.25$.  
*Target Value:* **`0.2503`** ($25.0282\%$).

---

#### Equation E.87: Poisson Rare-Event Arrival Probability
$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$
*Variables:* $\lambda$ (mean arrival rate per interval), $k$ (observed event count in interval).  
Limiting law of rare independent events: radioactive Geiger-counter clicks, optical shot noise photons, and packet switch arrivals.  
*RPN Sequence:* `lam {{key:ENTER}} k {{key:yˣ}} lam {{key:+/-}} {{key:eˣ}} {{key:×}} k {{key:x!}} {{key:÷}}`  
*Benchmark:* $\lambda = 4.2\text{ photons/ms}, k = 3\text{ photons}$.  
*Target Value:* **`0.1852`** ($18.5165\%$).

---

#### Equation E.88: Gaussian Standard $z$-Score & Confidence Interval Half-Width
$$z = \frac{x - \mu}{\sigma}, \quad E = z_{\alpha/2}\frac{s}{\sqrt{n}}$$
*Variables:* $x$ (observation), $\mu$ (population mean), $\sigma$ (standard deviation), $s$ (sample SD from `{{key:sx}}`), $n$ (sample size), $z_{\alpha/2}$ ($1.9600$ for $95\%$ CI; $2.5758$ for $99\%$ CI).  
Normalizes measurements into dimensionless standard deviation units and bounds the sampling error of the sample mean $\bar{x} \pm E$.  
*RPN Sequences:*  
- $z$-Score: `x {{key:ENTER}} mu {{key:-}} sigma {{key:÷}}`  
- $95\%$ CI Margin $E$: `s {{key:ENTER}} n {{key:√x}} {{key:÷}} 1.96 {{key:×}}`  
*Benchmark:* $s = 8.40\text{ MPa}, n = 49\text{ tensile specimens}, z_{\alpha/2} = 1.96$.  
*Target Value:* Margin of Error $E =$ **`2.3520`** $\text{MPa}$.

---

#### Equation E.89: Bayes' Theorem Diagnostic Posterior Probability
$$P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B \mid A)P(A) + P(B \mid A')P(A')}$$
*Variables:* $P(A)$ (prior prevalence), $P(B \mid A)$ (true-positive sensitivity), $P(B \mid A')$ (false-positive rate), $P(A') = 1 - P(A)$.  
Updates prior belief with conditional likelihood evidence; critical in medical diagnostics, radar target classification, and spam filtering.  
*RPN Sequence:* `PBA {{key:ENTER}} PA {{key:×}} {{key:ENTER}} PBnotA {{key:ENTER}} PnotA {{key:×}} {{key:+}} {{key:÷}}`  
*Benchmark:* $P(A) = 0.01$ prevalence, sensitivity $P(B \mid A) = 0.99$, false-positive rate $P(B \mid A') = 0.05$ ($P(A') = 0.99$).  
*Target Value:* **`0.1667`** ($16.67\%$ posterior probability).

---

#### Equation E.90: Six Sigma Process Capability Index ($C_{pk}$)
$$C_{pk} = \min\left(\frac{\text{USL} - \bar{x}}{3s},\; \frac{\bar{x} - \text{LSL}}{3s}\right)$$
*Variables:* $\text{USL}, \text{LSL}$ (upper/lower engineering specification limits), $\bar{x}$ (process mean via `{{key:x̄}}`), $s$ (process standard deviation via `{{key:sx}}`).  
Measures how many $3\sigma$ half-widths fit between the shifted process center $\bar{x}$ and the nearest tolerance wall ($C_{pk} \ge 1.33$ required for $4\sigma$ manufacturing).  
*RPN Sequence (Upper side):* `USL {{key:ENTER}} xbar {{key:-}} 3 {{key:÷}} s {{key:÷}}`  
*Benchmark:* CNC shaft diameter: $\text{USL} = 10.050\text{ mm}, \text{LSL} = 9.950\text{ mm}, \bar{x} = 10.010\text{ mm}, s = 0.010\text{ mm}$.  
*Target Value:* **`1.3333`**.

---

#### Equation E.91: Shannon Information Entropy (Base-2 Bits)
$$H(X) = -\sum_{i=1}^m p_i \log_2 p_i = -\frac{1}{\ln 2}\sum_{i=1}^m p_i \ln p_i$$
*Variables:* $p_i$ (symbol probability distribution with $\sum p_i = 1$).  
Fundamental theoretical lower bound on average lossless compression bits per symbol across a noisy or noiseless communication source.  
*RPN Sequence (Binary source $p, 1-p$):* `p {{key:ENTER}} {{key:LN}} {{key:×}} 1 {{key:ENTER}} p {{key:-}} {{key:ENTER}} {{key:LN}} {{key:×}} {{key:+}} 2 {{key:LN}} {{key:÷}} {{key:+/-}}`  
*Benchmark:* Biased binary telemetry source with $p_1 = 0.75, p_2 = 0.25$.  
*Target Value:* **`0.8113`** $\text{bits/symbol}$.

---

#### Equation E.92: Shannon–Hartley Channel Capacity Law
$$C = B \log_2\left(1 + \frac{S}{N}\right) = \frac{B \ln(1 + S/N)}{\ln 2}$$
*Variables:* $B$ (channel bandwidth, $\text{Hz}$), $S/N$ (linear signal-to-noise power ratio; from $\text{SNR}_{\text{dB}}$ via `SNR_dB 10 {{key:÷}} {{key:10ˣ}}`).  
Maximum error-free information bit rate transmissible over an additive white Gaussian noise (AWGN) radio or optical channel.  
*RPN Sequence:* `SNR {{key:ENTER}} 1 {{key:+}} {{key:LN}} 2 {{key:LN}} {{key:÷}} B {{key:×}}`  
*Benchmark:* $B = 20.0\text{ MHz}$ Wi-Fi channel with linear $S/N = 31.0$ ($14.91\text{ dB}$).  
*Target Value:* **`100.0000`** $\text{Mbps}$.

---

#### Equation E.93: M/M/1 Queueing Utilization, Queue Length & Latency
$$\rho = \frac{\lambda}{\mu}, \quad L = \frac{\lambda}{\mu - \lambda}, \quad W = \frac{1}{\mu - \lambda}$$
*Variables:* $\lambda$ (mean Poisson arrival rate, $\text{req/s}$), $\mu$ (mean exponential service rate, $\text{req/s}$, with $\mu > \lambda$).  
Little's Law ($L = \lambda W$) and Markovian birth-death steady state for CPU packet schedulers, database connection pools, and toll plazas.  
*RPN Sequence (Mean system occupancy $L$):* `lam {{key:ENTER}} mu {{key:ENTER}} lam {{key:-}} {{key:÷}}` (Mean latency $W$: `mu {{key:ENTER}} lam {{key:-}} {{key:1/x}}`)  
*Benchmark:* $\lambda = 45.0\text{ req/s}, \mu = 60.0\text{ req/s}$.  
*Target Values:* $L =$ **`3.0000`** $\text{requests}$; $W =$ **`0.0667`** $\text{s}$ ($66.7\text{ ms}$).

---

### Section 12: Structural Mechanics, Semiconductor Electronics, RF & Computer Engineering

Equations E.94–E.100 span structural beam deflection, axial Hookean strain, semiconductor diode junctions, op-amp feedback, RF path loss, and parallel computing speedup.

#### Equation E.94: Euler Column Critical Buckling Load
$$P_{\text{cr}} = \frac{\pi^2 E I}{(K L)^2}$$
*Variables:* $E$ (Young's modulus of elasticity, $\text{Pa}$), $I$ (minimum area moment of inertia, $\text{m}^4$), $K$ (effective length factor: $1.0$ pinned-pinned, $2.0$ fixed-free), $L$ (unsupported column length, $\text{m}$).  
Sudden lateral bifurcation instability of slender structural columns under axial compression long before material yield stress is reached.  
*RPN Sequence:* `{{key:π}} {{key:x²}} E {{key:×}} I {{key:×}} K {{key:ENTER}} L {{key:×}} {{key:x²}} {{key:÷}}`  
*Benchmark:* Structural steel column: $E = 200 \times 10^9\text{ Pa}, I = 8.50 \times 10^{-6}\text{ m}^4, K = 1.0, L = 4.0\text{ m}$.  
*Target Value:* **`1.0486e6`** $\text{N}$ ($1,048.6\text{ kN}$).

---

#### Equation E.95: Cantilever & Simply Supported Beam Tip Deflection
$$\delta_{\text{cantilever}} = \frac{F L^3}{3 E I}, \quad \delta_{\text{simple}} = \frac{F L^3}{48 E I}$$
*Variables:* $F$ (point load, $\text{N}$), $L$ (beam span, $\text{m}$), $E$ (Young's modulus, $\text{Pa}$), $I$ (cross-sectional second moment of area, $\text{m}^4$).  
Euler–Bernoulli double integration of bending moment $M(x) = E I \, d^2w/dx^2$; note the cubic sensitivity ($L^3$) to beam span.  
*RPN Sequence (Cantilever):* `L {{key:ENTER}} 3 {{key:yˣ}} F {{key:×}} 3 {{key:÷}} E {{key:÷}} I {{key:÷}}`  
*Benchmark:* $F = 5,000\text{ N}, L = 2.0\text{ m}, E = 200 \times 10^9\text{ Pa}, I = 4.0 \times 10^{-6}\text{ m}^4$.  
*Target Value:* **`0.0167`** $\text{m}$ ($16.67\text{ mm}$).

---

#### Equation E.96: Hooke's Law Axial Stress, Strain & Elastic Elongation
$$\sigma = \frac{F}{A}, \quad \varepsilon = \frac{\Delta L}{L_0}, \quad \Delta L = \frac{F L_0}{A E}$$
*Variables:* $F$ (axial tensile force, $\text{N}$), $L_0$ (unstrained length, $\text{m}$), $A$ (cross-sectional area, $\text{m}^2$), $E$ (Young's modulus, $\text{Pa}$).  
Linear elastic constitutive law ($\sigma = E \varepsilon$) for tie rods, suspension cables, and bolted preload joints.  
*RPN Sequence:* `F {{key:ENTER}} L0 {{key:×}} A {{key:÷}} E {{key:÷}}`  
*Benchmark:* Steel tie rod: $F = 45,000\text{ N}, L_0 = 2.50\text{ m}, A = 3.00 \times 10^{-4}\text{ m}^2, E = 200 \times 10^9\text{ Pa}$.  
*Target Value:* $\Delta L =$ **`0.001875`** $\text{m}$ ($1.875\text{ mm}$; axial stress $\sigma = 150.0\text{ MPa}$).

---

#### Equation E.97: Shockley Semiconductor Diode Current-Voltage Law
$$I_D = I_S \left[\exp\left(\frac{V_D}{n V_T}\right) - 1\right]$$
*Variables:* $I_S$ (reverse saturation current, $\text{A}$), $V_D$ (forward bias voltage, $\text{V}$), $n$ (ideality factor, $1.0\text{–}2.0$), $V_T = k_B T / q \approx 0.02585\text{ V}$ at $300\text{ K}$.  
Carrier diffusion across a $p$-$n$ junction depletion barrier; inside-out RPN evaluation avoids parentheses around the exponential argument.  
*RPN Sequence:* `VD {{key:ENTER}} n {{key:÷}} VT {{key:÷}} {{key:eˣ}} 1 {{key:-}} IS {{key:×}}`  
*Benchmark:* Silicon junction diode: $I_S = 1.0 \times 10^{-12}\text{ A}, V_D = 0.650\text{ V}, n = 1.0, V_T = 0.02585\text{ V}$.  
*Target Value:* **`0.0835`** $\text{A}$ ($83.47\text{ mA}$).

---

#### Equation E.98: Operational Amplifier Closed-Loop Gain & $-3\text{ dB}$ Bandwidth
$$A_{v,\text{non}} = 1 + \frac{R_f}{R_g}, \quad A_{v,\text{inv}} = -\frac{R_f}{R_{\text{in}}}, \quad f_{-3\text{dB}} = \frac{\text{GBWP}}{A_{v,\text{non}}}$$
*Variables:* $R_f$ (feedback resistor, $\Omega$), $R_g$ or $R_{\text{in}}$ (input ground resistor, $\Omega$), $\text{GBWP}$ (gain-bandwidth product, $\text{Hz}$).  
Negative feedback trades open-loop gain for precision closed-loop linearity and extended closed-loop bandwidth $f_{-3\text{dB}}$.  
*RPN Sequence (Non-Inverting Gain & Bandwidth):* `Rf {{key:ENTER}} Rg {{key:÷}} 1 {{key:+}} GBWP {{key:x⇄y}} {{key:÷}}`  
*Benchmark:* $R_f = 90\text{ k}\Omega, R_g = 10\text{ k}\Omega, \text{GBWP} = 10.0\text{ MHz}$.  
*Target Values:* $A_{v,\text{non}} =$ **`10.0000`** ($20.0\text{ dB}$); $f_{-3\text{dB}} =$ **`1.0000`** $\text{MHz}$.

---

#### Equation E.99: Friis Free-Space RF Path Loss ($\text{FSPL}$)
$$\text{FSPL}_{\text{dB}} = 20\log_{10}\left(\frac{4\pi d f}{c}\right)$$
*Variables:* $d$ (line-of-sight range, $\text{m}$), $f$ (carrier frequency, $\text{Hz}$), $c = 2.99792458 \times 10^8\text{ m/s}$.  
Spherical inverse-square wave-front spreading ($1/(4\pi d^2)$) combined with effective isotropic receiving aperture ($\lambda^2 / 4\pi$) for satellite and microwave link budgets.  
*RPN Sequence:* `4 {{key:π}} {{key:×}} d {{key:×}} f {{key:×}} 2.99792458 {{key:E}} 8 {{key:÷}} {{key:LOG}} 20 {{key:×}}`  
*Benchmark:* $d = 1,000\text{ m}$ ($1\text{ km}$), $f = 2.40 \times 10^9\text{ Hz}$ ($2.4\text{ GHz}$ ISM band).  
*Target Value:* **`100.0460`** $\text{dB}$.

---

#### Equation E.100: Amdahl's Law Multiprocessor Speedup & CMOS Dynamic Power
$$S(N) = \frac{1}{(1 - p) + \frac{p}{N}}, \quad P_{\text{dyn}} = \alpha C V_{DD}^2 f$$
*Variables:* $p$ (parallelizable workload fraction), $N$ (processor core count); $\alpha$ (switching activity), $C$ (load capacitance, $\text{F}$), $V_{DD}$ (supply rail, $\text{V}$), $f$ (clock frequency, $\text{Hz}$).  
Shows why serial bottlenecks $(1-p)$ cap parallel scaling at $1/(1-p)$ and why voltage scaling ($V_{DD}^2$) dominates microprocessor thermal design power.  
*RPN Sequences:*  
- Amdahl Speedup $S(N)$: `p {{key:ENTER}} N {{key:÷}} 1 {{key:ENTER}} p {{key:-}} {{key:+}} {{key:1/x}}`  
- CMOS Dynamic Power $P_{\text{dyn}}$: `VDD {{key:x²}} alpha {{key:×}} C {{key:×}} f {{key:×}}`  
*Benchmark:* $p = 0.90$ ($90\%$ parallel code), $N = 16\text{ cores}$.  
*Target Value:* $S(16) =$ **`6.4000`** $\times$ speedup (asymptotic ceiling $S(\infty) = 10.0\times$).

---

## Specialized RPN Idioms & Stack Optimization Patterns

Fluency on the SC-32 comes from recognizing recurring mathematical forms and applying dedicated hardware keys to minimize button presses and eliminate redundant variable stores.

### The Harmonic Mean Idiom (`{{key:x∥y}}`)
The SC-32 provides a dedicated primary key **`{{key:x∥y}}`** which calculates:
$$X = \frac{X \cdot Y}{X + Y} = \frac{1}{\frac{1}{X} + \frac{1}{Y}}$$
In algebraic calculators, entering a reciprocal sum requires 12 to 16 keystrokes with fractions and parentheses. On the SC-32, it takes exactly **one keystroke**:
* **Parallel Resistors:** $R_{\text{eq}} = R_1 \parallel R_2 \parallel R_3$ $\rightarrow$ `R1 {{key:ENTER}} R2 {{key:x∥y}} R3 {{key:x∥y}}`.
* **Series Capacitors:** $C_{\text{eq}} = C_1 \parallel C_2$ $\rightarrow$ `C1 {{key:ENTER}} C2 {{key:x∥y}}`.
* **Thin Lens Optics:** Focal length $f = d_o \parallel d_i$ $\rightarrow$ `do {{key:ENTER}} di {{key:x∥y}}`.
* **Spring Series Compliance:** $k_{\text{eq}} = k_1 \parallel k_2$ $\rightarrow$ `k1 {{key:ENTER}} k2 {{key:x∥y}}`.
* **Reduced Mass in Two-Body Problem:** $\mu = m_1 \parallel m_2$ $\rightarrow$ `m1 {{key:ENTER}} m2 {{key:x∥y}}`.

### The Difference-of-Squares Idiom
When evaluating expressions of the form $a^2 - b^2$ (such as Pythagorean legs $b = \sqrt{c^2 - a^2}$ or numerical aperture $NA = \sqrt{n_1^2 - n_2^2}$):
* **Traditional RPN:** `c {{key:x²}} a {{key:x²}} {{key:-}} {{key:√x}}` (6 keystrokes).
* **Stack Factoring Alternative:** `c {{key:ENTER}} a {{key:ENTER}} {{key:+}} {{key:LASTX}} c {{key:x⇄y}} {{key:-}} {{key:×}} {{key:√x}}`. When numbers are large multi-digit values, entering them once and using `{{key:x⇄y}}` and `{{key:LASTX}}` avoids re-typing.

### Constant Factor Replication in Register T
When evaluating a formula with a repeated scalar factor $K$ across multiple variables (e.g. converting several values from feet to meters using $0.3048$, or multiplying items by sales tax $1.0825$):
1. Load the constant into the stack: `1.0825 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}` (fills $X, Y, Z, T$).
2. Enter Price 1: `10 {{key:×}}` $\rightarrow$ Displays result $10.825$. Register $T$ drops to $Z$ and replicates $1.0825$ in $T$!
3. Enter Price 2: `{{key:CLx}} 25 {{key:×}}` $\rightarrow$ Displays $27.0625$. Register $T$ continues to supply $1.0825$ indefinitely without ever touching memory registers!

---

## Numerical Root-Finding (`{{key:SOLVE}}`) & Quadrature (`{{key:∫}}`) Function Selector

As detailed in [Chapter 7](07-polynomials-brent-solver.md) and [Chapter 8](08-calculus-romberg-quadrature.md), the StackCalc SC-32 provides numerical root-finding via Richard Brent's hybrid inverse-quadratic/secant/bisection algorithm (**`{{key:SOLVE}}`**, Right Shift `{{key:↱}}` + `{{key:7}}`) and adaptive Romberg numerical integration (**`{{key:∫}}`**, Right Shift `{{key:↱}}` + `{{key:8}}`). Both engines evaluate either **user-defined postfix expressions** stored in Equation Mode (**`{{key:EQN}}`**, Right Shift `{{key:↱}}` + `{{key:STO}}`) or **six built-in benchmark templates ($f_0$ through $f_5$)** with Register $Z$ parameter passing:

### SC-32 Numerical Root-Finding & Quadrature Workflows

1. **User-Defined Postfix Equations (`{{key:EQN}}` Mode):** Press `{{key:↱}}` + `{{key:STO}}` (`{{key:EQN}}`) to enter or select a custom RPN expression in variable `X` (for example, `X SQ 2 -` for $f(x) = x^2 - 2$). Exit to the stack, load the bracket or integration limits $[a, b]$ into Registers $Y$ and $X$ (`a {{key:ENTER}} b`), and press `{{key:SOLVE}}` (`{{key:↱}}` + `{{key:7}}`) or `{{key:∫}}` (`{{key:↱}}` + `{{key:8}}`) to solve or integrate the active equation directly.
2. **Built-In Benchmark Templates ($f_0$–$f_5$):** When no custom equation is active (or when selecting a built-in test function), pressing `{{key:SOLVE}}` (`{{key:↱}}` + `{{key:7}}`) or `{{key:∫}}` (`{{key:↱}}` + `{{key:8}}`) accesses the 6-template function selector:
   * `0`: $f_0(x) = x^2 - c$ (where constant $c$ is read from Register $Z$)
   * `1`: $f_1(x) = \cos(x) - x$ (transcendental fixed-point benchmark)
   * `2`: $f_2(x) = \sin(x)$ (trigonometric waveform quadrature)
   * `3`: $f_3(x) = e^{-x^2}$ (Gaussian error-function bell curve)
   * `4`: $f_4(x) = x^3 - 2x - 5$ (Wallis's classical cubic benchmark)
   * `5`: $f_5(x) = \ln(x) - 1$ (Euler natural-base root benchmark)
3. **Execute Brent Root-Finder (`{{key:SOLVE}}`):** Place parameter $c$ in Register $Z$ (if using $f_0$), lower bracket $a$ in Register $Y$, and upper bracket $b$ in Register $X$, then invoke `{{key:SOLVE}}` (for the active `{{key:EQN}}` expression or followed by template digit `0`–`5`). The converged root $x^*$ is returned in Register $X$, the previous iterate in Register $Y$, and residual $f(x^*)$ in Register $Z$.
4. **Execute Romberg Quadrature (`{{key:∫}}`):** Place lower integration limit $a$ in Register $Y$ and upper limit $b$ in Register $X$, then invoke `{{key:∫}}` (for the active `{{key:EQN}}` expression or followed by template digit `0`–`5`). The definite integral $\int_a^b f(x)\,dx$ is returned in Register $X$ with the Richardson truncation error estimate in Register $Y$.

### Benchmark Example: Parabolic Area & Root Verification with Template $f_0(x) = x^2 - c$
To evaluate $\int_0^4 x^2 \, dx = \left[\frac{x^3}{3}\right]_0^4 = 21.3333$ (with $c = 0$ in Register $Z$):
1. Clear stack and load $c = 0$ into $Z$, lower limit $a = 0$ into $Y$, and upper limit $b = 4$ into $X$: `0 {{key:ENTER}} 0 {{key:ENTER}} 4`
2. Press `{{key:∫}} 0` (selects template $f_0(x) = x^2 - 0$).
3. The transflective screen converges via Romberg Richardson extrapolation and returns **`21.3333`** in Register $X$ (multiply by `3 {{key:×}}` for $\int_0^4 3x^2\,dx = 64.0000$).

---

## Storing Physical Constants in Registers A–Z

While pure mathematical invariants ($\pi$ via `{{key:π}}` and $e$ via `1 {{key:eˣ}}`) are permanently hardcoded in firmware, empirical 2022 CODATA physical constants (such as the Planck constant $h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}$, speed of light $c = 2.99792458 \times 10^8\text{ m/s}$, elementary charge $e = 1.602176634 \times 10^{-19}\text{ C}$, molar gas constant $R = 8.314462618\text{ J/(mol}\cdot\text{K)}$, and Avogadro constant $N_A = 6.02214076 \times 10^{23}\text{ mol}^{-1}$) are keyed explicitly via `{{key:E}}` or stored into the 26 non-volatile global letter registers (`{{key:STO}} A` through `{{key:STO}} Z`) for instant single-key recall (`{{key:RCL}} C`, `{{key:RCL}} H`, `{{key:RCL}} R`). Computing physical benchmarks with 4-level stack traces ensures that experimental calculations and textbook derivations match standard reference tables to full floating-point precision without compounding rounding errors.

---

## Numerical Boundary Conditions & Singularity Guards

* **Scientific Exponent Entry Syntax:** Never press `{{key:×}} 10 {{key:yˣ}}` to enter scientific notation; doing so pushes an extra operand onto the stack and consumes two stack levels. Always use the dedicated **`{{key:E}}`** (Exponent) key:
  * **Correct:** `1.602176634 {{key:E}} 19 {{key:+/-}}` (enters a single number into Register $X$).
  * **Incorrect:** `1.602176634 {{key:ENTER}} 10 {{key:ENTER}} 19 {{key:+/-}} {{key:yˣ}} {{key:×}}` (consumes four stack registers and risks stack overflow).
* **Trigonometric Angular Modes in Physical Laws:** Physical formulas involving wave motion, optics, and projectile trajectories require the matching angular mode:
  * **Geometric and Surveying Formulas (Snell's Law, Law of Cosines, Great Circle):** Require Degrees mode (`{{key:MODES}} {{key:DEG}}`).
  * **Analytical Calculus and Fourier Syntheses (Pendulum Period, Harmonic Oscillations):** Require Radians mode (`{{key:MODES}} {{key:RAD}}`).
  Check the `DEG` or `RAD` annunciator at the top of the display before starting a trigonometric sequence.
* **Mathematical Singularity and Boundary Handling:**
  * **Division by Zero ($x / 0$):** Halts execution and displays `DIVIDE BY 0` (Code 01). Press `{{key:C}}` or `{{key:<-}}` to clear the error and restore the prior stack state.
  * **Square Root of a Negative Number ($\sqrt{-x}$):** Displays `INVALID DATA` (Code 02) in Real mode; in Complex mode ({{key:CMPLX}}), returns the pure imaginary result $i\sqrt{x}$ across $(Y, X)$.
  * **Logarithm of a Non-Positive Number ($\ln(0)$ or $\ln(-x)$):** Displays `DIVIDE BY 0` (for $\ln 0$) or `INVALID DATA` (for $\ln(-x)$).

---

For the historical primary sources, foundational numerical analysis papers, and classic engineering handbooks cited throughout this manual and equation directory, continue to **[Appendix E: Primary Sources & Annotated Further Reading Guide](appendix-e-annotated-bibliography.md)**.

