---
title: "Appendix D: Mathematical Constants, SI Units & Master STEM Equation Directory | SC-32 Manual"
description: "Authoritative reference directory of immutable mathematical constants, complete BIPM SI prefixes, exact unit conversions, and 58 master STEM engineering equations with optimal RPN keystrokes for the StackCalc SC-32."
---

# Appendix D: Mathematical Constants, SI Units & Master STEM Equation Directory

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 APPENDIX D // MATHEMATICAL CONSTANTS, SI UNITS &amp; MASTER STEM EQUATION DIRECTORY</span>
  <span class="te-viewport-status text-sky-400">● IMMUTABLE MATHEMATICAL CONSTANTS &bull; 58 STEM EQUATIONS &bull; PARENTHESIS-FREE RPN SEQUENCING</span>
</div>


{{blocks:sc32_hero_keynote|StackCalc SC-32 Bench Reference}}
*Figure D.1: The StackCalc SC-32 technical reference bench instrument: rapid parenthesis-free evaluation of fundamental engineering and mathematical equations.*


<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>DIRECTORY BASELINE:</strong> Immutable mathematical constants; Complete BIPM SI prefixes (10³⁰ to 10⁻³⁰); Exact international unit conversions; Scientific notation entry syntax via <code>{{key:E}}</code>; Full 12-digit mantissa stack precision.
</div>

---

## The Architecture of Precision: Constants and Equations in RPN

A scientific calculator is not merely a tool for performing isolated arithmetic operations; it is a computational laboratory for modeling the physical universe. On the StackCalc SC-32, the synergy of Reverse Polish Notation (RPN), continuous four-register stack visibility ($X, Y, Z, T$), and dedicated scientific functions provides an unparalleled environment for STEM calculations.

<div class="admonition note">
<p class="admonition-title">SC-32 Scientific Register Hierarchy &amp; Data Flow</p>

> [ REGISTER T ]  Top / Constant Buffer  <-- Retains constant factor during drop
> │
> [ REGISTER Z ]  Third Stack Level      <-- Holds intermediate vector/matrix term
> │
> [ REGISTER Y ]  Second Stack Level     <-- Stores dyadic base, dividend, angle
> │
> [ REGISTER X ]  Active / Display       <-- Direct keyboard entry & live readout
>
> [ LASTX REG  ]  Recovery Buffer        <-- Automatically captures previous X
> [ STATS BANK ]  6 Accumulators         <-- Σx, Σy, Σx², Σy², Σxy, n
> [ MEMORY A-Z ]  26 Global Registers    <-- Persistent storage via {{key:STO}} / {{key:RCL}}
</div>

### The Concrete-Representational-Abstract (CRA) Framework
1. **Concrete (Key Entry & Hardware Tactility):** Scientific magnitudes are keyed using the tactile 400g snap-dome keys. Entering a power-of-ten scale factor such as $6.62607015 \times 10^{-34}$ is accomplished cleanly via `6.62607015 {{key:E}} 34 {{key:+/-}}`.
2. **Representational (Four-Register Visual Feedback):** As operations execute, intermediate physical quantities (such as angular frequency $\omega$ in $Y$ and capacitance $C$ in $X$) remain continuously visible on the transflective $132 \times 65$ LCD, eliminating memory ambiguity.
3. **Abstract (Parenthesis-Free Formula Decomposition):** Equations with complex nesting (such as blackbody radiation laws or relativistic Lorentz transformations) are evaluated inside-out or bottom-up, completely avoiding algebraic parentheses.

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

## Master STEM Equation Directory: 58 Essential Bench Equations

Every equation in this directory is presented with its formal mathematical definition, variable descriptions, optimal parenthesis-free RPN keystroke sequence, verified numerical benchmark, and a four-register stack trace.

| Discipline / Subject | Benchmark Equations |
|:---|:---|
| 1. Classical Mechanics, Orbital Dynamics & Statics | Equations E.01 – E.10 |
| 2. Fluid Mechanics, Hydraulics & Aerodynamics | Equations E.11 – E.18 |
| 3. Thermodynamics, Gas Laws & Heat Transfer | Equations E.19 – E.26 |
| 4. Electricity, Magnetism & AC Circuit Analysis | Equations E.27 – E.36 |
| 5. Wave Mechanics, Acoustics & Physical Optics | Equations E.37 – E.44 |
| 6. Nuclear, Atomic & Relativistic Physics | Equations E.45 – E.51 |
| 7. Coordinate Geometry, Mensuration & Solid Geometry | Equations E.52 – E.58 |

---

### Section 1: Classical Mechanics, Orbital Dynamics & Statics

#### Equation E.01: Kinematic Velocity-Displacement Relation
$$v_f = \sqrt{v_i^2 + 2 a \Delta x}$$
*Variables:* $v_i$ (initial velocity, $\text{m/s}$), $a$ (acceleration, $\text{m/s}^2$), $\Delta x$ (displacement, $\text{m}$).  
*RPN Sequence:* `vi {{key:x²}} 2 {{key:ENTER}} a {{key:×}} dx {{key:×}} {{key:+}} {{key:√x}}`  
*Benchmark:* $v_i = 12.0\text{ m/s}, a = 4.5\text{ m/s}^2, \Delta x = 25.0\text{ m}$.  
*Target Value:* **`19.209373`** $\text{m/s}$.  
*Stack Trace Table:*
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 12 {{keycap:x²}} | 0.00 | 0.00 | 0.00 | 144.0000 | 144.0000 |
| 02 | 2 {{key:ENTER}} 4.5 {{key:×}} | 0.00 | 0.00 | 144.0000 | 9.0000 | 9.0000 |
| 03 | 25 {{key:×}} {{key:+}} | 0.00 | 0.00 | 0.00 | 369.0000 | 369.0000 |
| 04 | {{key:√x}} | 0.00 | 0.00 | 0.00 | 19.209373 | 19.2094 |

---

#### Equation E.02: Projectile Motion Maximum Range
$$R = \frac{v_0^2 \sin(2\theta)}{g}$$
*Variables:* $v_0$ (muzzle velocity, $\text{m/s}$), $\theta$ (launch angle, degrees), $g = 9.80665\text{ m/s}^2$.  
*RPN Sequence in `{{key:DEG}}` Mode:* `v0 {{key:x²}} theta {{key:ENTER}} 2 {{key:×}} {{key:SIN}} {{key:×}} 9.80665 {{key:÷}}`  
*Benchmark:* $v_0 = 45.0\text{ m/s}, \theta = 35.0^\circ$.  
*Target Value:* **`194.0435`** $\text{m}$.  
*Stack Trace Table:*
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 45 {{keycap:x²}} | 0.00 | 0.00 | 0.00 | 2025.0000 | 2025.0000 |
| 02 | 35 {{key:ENTER}} 2 {{key:×}} | 0.00 | 0.00 | 2025.0000 | 70.0000 | 70.0000 |
| 03 | {{key:SIN}} {{key:×}} | 0.00 | 0.00 | 0.00 | 1902.8711 | 1902.8711 |
| 04 | 9.80665 {{key:÷}} | 0.00 | 0.00 | 0.00 | 194.0435 | 194.0435 |

---

#### Equation E.03: Centripetal Acceleration & Radial Force
$$F_c = \frac{m v^2}{r}$$
*Variables:* $m$ (mass, $\text{kg}$), $v$ (tangential speed, $\text{m/s}$), $r$ (radius, $\text{m}$).  
*RPN Sequence:* `v {{key:x²}} m {{key:×}} r {{key:÷}}`  
*Benchmark:* $m = 1250\text{ kg}, v = 24.0\text{ m/s}, r = 60.0\text{ m}$.  
*Target Value:* **`12000.0`** $\text{N}$ ($12.0\text{ kN}$).  
*Keystrokes:* `{{res:sc32_appendix_d_constants_and_equations_seq_01:keys}}` $\rightarrow$ `{{res:sc32_appendix_d_constants_and_equations_seq_01:value}}`.

---

#### Equation E.04: Newton's Law of Universal Gravitation
$$F_g = G \frac{m_1 m_2}{r^2}$$
*Variables:* $G = 6.67430 \times 10^{-11}, m_1, m_2 (\text{kg}), r (\text{m})$.  
*RPN Sequence:* `6.67430 {{key:E}} 11 {{key:+/-}} m1 {{key:×}} m2 {{key:×}} r {{key:x²}} {{key:÷}}`  
*Benchmark:* $m_1 = 5.9722 \times 10^{24}, m_2 = 1500, r = 6.771 \times 10^6$.  
*Target Value:* **`13038.58`** $\text{N}$.  
*Stack Trace Table:*
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | G m1 {{key:×}} m2 {{key:×}} | 0.00 | 0.00 | 0.00 | 5.9791E17 | 5.97910E17 |
| 02 | r {{keycap:x²}} | 0.00 | 0.00 | 5.9791E17 | 4.5846E13 | 4.58464E13 |
| 03 | {{key:÷}} | 0.00 | 0.00 | 0.00 | 13038.58 | 1.30386E4 |

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

#### Equation E.11: Torricelli Efflux Jet Velocity

$$v = \sqrt{2 g h}$$
*Variables:* $g = 9.80665\text{ m/s}^2$, $h$ (fluid head, $\text{m}$).  
*RPN Sequence:* `2 {{key:ENTER}} 9.80665 {{key:×}} h {{key:×}} {{key:√x}}`  
*Benchmark:* $h = 5.0\text{ m}$.  
*Target Value:* **`9.90285`** $\text{m/s}$.  
*Stack Trace Table:*
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 2 {{key:ENTER}} 9.80665 {{key:×}} | 0.00 | 0.00 | 0.00 | 19.613300 | 19.613300 |
| 02 | 5 {{key:×}} | 0.00 | 0.00 | 0.00 | 98.066500 | 98.066500 |
| 03 | {{key:√x}} | 0.00 | 0.00 | 0.00 | 9.902853 | 9.902853 |

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

#### Equation E.19: Ideal Gas State Equation
$$P = \frac{n R T}{V}$$
*Variables:* $n$ (moles), $R = 8.314462618\text{ J/(mol}\cdot\text{K)}$, $T$ (temperature, $\text{K}$), $V$ (volume, $\text{m}^3$).  
*RPN Sequence:* `n {{key:ENTER}} 8.314462618 {{key:×}} T {{key:×}} V {{key:÷}}`  
*Benchmark:* $n = 4.5\text{ mol}, T = 350.0\text{ K}, V = 0.035\text{ m}^3$.  
*Target Value:* **`374150.8`** $\text{Pa}$ ($374.15\text{ kPa}$).  
*Stack Trace Table:*
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 4.5 {{key:ENTER}} R {{key:×}} | 0.00 | 0.00 | 0.00 | 37.415082 | 37.415082 |
| 02 | 350 {{key:×}} | 0.00 | 0.00 | 0.00 | 13095.279 | 13095.279 |
| 03 | .035 {{key:÷}} | 0.00 | 0.00 | 0.00 | 374150.82 | 374150.8 |

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
*Stack Trace Table:*
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 100 {{key:ENTER}} | 0.00 | 0.00 | 100.0000 | 100.0000 | 100.0000_ |
| 02 | 150 {{key:x∥y}} | 0.00 | 0.00 | 0.00 | 60.0000 | 60.0000 |
| 03 | 300 {{key:x∥y}} | 0.00 | 0.00 | 0.00 | 50.0000 | 50.0000 |

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
*Stack Trace Table:*
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 10E-3 100E-12 {{key:×}} | 0.00 | 0.00 | 0.00 | 1.0000E-12 | 1.0000E-12 |
| 02 | {{key:√x}} | 0.00 | 0.00 | 0.00 | 1.0000E-6 | 1.0000E-6 |
| 03 | 2 {{key:×}} π {{key:×}} {{key:1/x}} | 0.00 | 0.00 | 0.00 | 159154.94 | 1.59155E5 |

---

#### Equation E.34: RLC Series AC Total Impedance
$$Z = \sqrt{R^2 + \left(2 \pi f L - \frac{1}{2 \pi f C}\right)^2}$$
*Variables:* $R (\Omega)$, $L (\text{H})$, $C (\text{F})$, $f (\text{Hz})$.  
*RPN Sequence:* `2 {{key:ENTER}} {{key:π}} {{key:×}} f {{key:×}} {{key:STO}} 1 L {{key:×}} {{key:RCL}} 1 C {{key:×}} {{key:1/x}} {{key:-}} {{key:x²}} R {{key:x²}} {{key:+}} {{key:√x}}`  
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
*Stack Trace Table:*
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 30 {{key:ENTER}} | 0.00 | 0.00 | 30.0000 | 30.0000 | 30.0000_ |
| 02 | 60 {{key:x∥y}} | 0.00 | 0.00 | 0.00 | 20.0000 | 20.0000 |

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

#### Equation E.45: Einstein Mass-Energy Equivalence
$$E = m c^2$$
*Variables:* $m$ (mass, $\text{kg}$), $c = 299,792,458\text{ m/s}$.  
*RPN Sequence:* `299792458 {{key:x²}} m {{key:×}}`  
*Benchmark:* $m = 1.0 \times 10^{-3}\text{ kg}$ ($1\text{ gram}$).  
*Target Value:* **`8.98755 × 10¹³`** $\text{J}$ ($89.88\text{ TJ}$).  
*Stack Trace Table:*
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 299792458 {{key:x²}} | 0.00 | 0.00 | 0.00 | 8.9876E16 | 8.98755E16 |
| 02 | 1E-3 {{key:×}} | 0.00 | 0.00 | 0.00 | 8.9876E13 | 8.98755E13 |

---

#### Equation E.46: Planck-Einstein Photon Energy
$$E_{\text{photon}} = \frac{h c}{\lambda}$$
*Variables:* $h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}, c = 299,792,458\text{ m/s}, \lambda (\text{m})$.  
*RPN Sequence:* `6.62607015 {{key:E}} 34 {{key:+/-}} 299792458 {{key:×}} lambda {{key:÷}}`  
*Benchmark:* $\lambda = 500.0 \times 10^{-9}\text{ m}$ (green photon).  
*Target Value:* **`3.9729 × 10⁻¹⁹`** $\text{J}$ ($2.48\text{ eV}$).

---

#### Equation E.47: de Broglie Particle Wavelength
$$\lambda = \frac{h}{m v}$$
*Variables:* $h = 6.62607015 \times 10^{-34}, m (\text{kg}), v (\text{m/s})$.  
*RPN Sequence:* `6.62607015 {{key:E}} 34 {{key:+/-}} m {{key:÷}} v {{key:÷}}`  
*Benchmark:* $m = 9.1093837 \times 10^{-31}\text{ kg}$ (electron), $v = 2.0 \times 10^6\text{ m/s}$.  
*Target Value:* **`3.6370 × 10⁻¹⁰`** $\text{m}$ ($0.3637\text{ nm}$).

---

#### Equation E.48: Relativistic Lorentz Factor ($\gamma$)
$$\gamma = \frac{1}{\sqrt{1 - \beta^2}} = \frac{1}{\sqrt{1 - (v/c)^2}}$$
*Variables:* $\beta = v / c$.  
*RPN Sequence:* `beta {{key:x²}} 1 {{key:x⇄y}} {{key:-}} {{key:√x}} {{key:1/x}}`  
*Benchmark:* $\beta = 0.95$.  
*Target Value:* **`3.20256`**.  
*Stack Trace Table:*
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 0.95 {{keycap:x²}} | 0.00 | 0.00 | 0.00 | 0.902500 | 0.902500 |
| 02 | 1 {{key:x⇄y}} {{key:-}} | 0.00 | 0.00 | 0.00 | 0.097500 | 0.097500 |
| 03 | {{key:√x}} {{key:1/x}} | 0.00 | 0.00 | 0.00 | 3.202563 | 3.202563 |

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

#### Equation E.52: Volume and Surface Area of Sphere
$$V = \frac{4}{3} \pi r^3, \quad A = 4 \pi r^2$$
*Variables:* $r$ (radius).  
*RPN Sequences:*  
- Volume: `r {{key:ENTER}} 3 {{key:yˣ}} {{key:π}} {{key:×}} 4 {{key:×}} 3 {{key:÷}}`  
- Area: `r {{key:x²}} {{key:π}} {{key:×}} 4 {{key:×}}`  
*Benchmark:* $r = 7.50\text{ cm}$.  
*Target Values:* Volume = **`1767.146`** $\text{cm}^3$; Area = **`706.858`** $\text{cm}^2$.  
*Stack Trace Table (Volume):*
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 7.5 {{key:ENTER}} 3 {{key:yˣ}} | 0.00 | 0.00 | 0.00 | 421.8750 | 421.8750 |
| 02 | {{keycap:π}} {{key:×}} | 0.00 | 0.00 | 0.00 | 1325.3594 | 1325.359 |
| 03 | 4 {{key:×}} 3 {{key:÷}} | 0.00 | 0.00 | 0.00 | 1767.1459 | 1767.146 |

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
*Stack Trace Table:*
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 8 {{keycap:x²}} | 0.00 | 0.00 | 0.00 | 64.0000 | 64.0000 |
| 02 | 8 {{key:ENTER}} 3 {{key:×}} {{key:+}} | 0.00 | 0.00 | 0.00 | 88.0000 | 88.0000 |
| 03 | 3 {{keycap:x²}} {{key:+}} | 0.00 | 0.00 | 0.00 | 97.0000 | 97.0000 |
| 04 | 12 {{key:×}} 3 {{key:÷}} π {{key:×}} | 0.00 | 0.00 | 0.00 | 1218.9380 | 1218.938 |

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
*RPN Sequence:* `a {{key:ENTER}} b {{key:+}} c {{key:+}} 2 {{key:÷}} {{key:STO}} 1 a {{key:-}} {{key:RCL}} 1 b {{key:-}} {{key:×}} {{key:RCL}} 1 c {{key:-}} {{key:×}} {{key:RCL}} 1 {{key:×}} {{key:√x}}`  
*Benchmark:* $a = 13.0, b = 14.0, c = 15.0$ (semiperimeter $s = 21.0$).  
*Target Value:* **`84.000`**.  
*Stack Trace Table:*
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | a b {{key:+}} c {{key:+}} 2 {{key:÷}} | 0.00 | 0.00 | 0.00 | 21.0000(s) | 21.0000 |
| 02 | {{key:STO}} 1 a {{key:-}} | 0.00 | 0.00 | 0.00 | 8.0000(s-a) | 8.0000 |
| 03 | {{key:RCL}} 1 b {{key:-}} {{key:×}} | 0.00 | 0.00 | 0.00 | 56.0000 | 56.0000 |
| 04 | {{key:RCL}} 1 c {{key:-}} {{key:×}} | 0.00 | 0.00 | 0.00 | 336.0000 | 336.0000 |
| 05 | {{key:RCL}} 1 {{key:×}} {{key:√x}} | 0.00 | 0.00 | 0.00 | 84.0000 | 84.0000 |

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

## Specialized RPN Idioms & Stack Optimization Patterns

Mastery of the SC-32 involves recognizing recurring computational structures and leveraging dedicated hardware keys to minimize button presses and eliminate redundant variable stores.

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

## Equation Bank Programming & Automatic Variable Prompting


The StackCalc SC-32 provides a non-volatile **Equation Bank** accessed via **`{{key:EQN}}`**. Any standard formula can be stored as a symbolic expression and evaluated repeatedly, solved numerically via Brent's root finder, or integrated via Romberg quadrature.

<div class="admonition note">
<p class="admonition-title">Equation Bank Workflow: Entry, Solving &amp; Integration</p>
<ol>
  <li><strong>Create Equation:</strong> <code>{{key:EQN}}</code> &rarr; Type formula using named variables $A$–$Z$. Example: <code>Y = A × X² + B × X + C</code></li>
  <li><strong>Evaluate (Prompt):</strong> <code>{{key:XEQ}}</code> &rarr; SC-32 sequentially prompts: <code>A?</code> &rarr; enter value &rarr; <code>[R/S]</code>, <code>X?</code> &rarr; enter value &rarr; <code>[R/S]</code>, <code>B?</code> &rarr; enter value &rarr; <code>[R/S]</code>, <code>C?</code> &rarr; enter value &rarr; <code>[R/S]</code>. Result displays in Register $X$.</li>
  <li><strong>Numerical Root:</strong> <code>{{key:SOLVE}} X</code> &rarr; Solves for $X$ when $Y = 0$ using Richard Brent's hybrid algorithm.</li>
  <li><strong>Numerical Integral:</strong> <code>{{key:∫}}</code> &rarr; Prompts for variable, lower, upper. Evaluates Romberg adaptive quadrature.</li>
</ol>
</div>

### Benchmark Example: Parabolic Motion Integration
Evaluate $\int_0^4 3 X^2 \, dX = [X^3]_0^4 = 64.0$:
1. Enter Equation mode: `{{key:EQN}}`
2. Enter keystrokes: `3 {{key:ENTER}} X {{key:x²}} {{key:×}}`
3. Assign label: `PARABOLA`
4. Set integration bounds: Lower bound $0.0$, Upper bound $4.0$.
5. Press `{{key:∫}} X`
6. The transflective screen indicates active Romberg convergence steps and halts with **`64.0000`** in Register $X$.

---

## Teaching & Instrument Architecture Notes

### Dimensional Dependency Tracking & Conceptual Grounding
In collegiate engineering and physics education, learners often struggle with algebraic syntax friction, losing sight of physical scaling relationships while navigating nested parentheses. Formulating standard reference equations—from relativistic dynamics to thermodynamic cycles—into step-by-step RPN pipelines reveals physical dimensional dependencies directly. Intermediate operands in Registers $Y$ and $Z$ anchor dimensional analysis, allowing students to inspect intermediate physical products (such as momentum, kinetic energy, or pressure heads) before collapsing terms into final units.

### 2022 CODATA Physical Constants & Verification Precision
The SC-32 hardcodes fundamental physical constants according to the latest 2022 CODATA recommendations (including the Planck constant $h$, speed of light $c$, elementary charge $e$, and Avogadro constant $N_A$). Because these values are defined with exact SI definitions or high-precision mantissas, computing physical benchmarks with 4-level stack traces ensures that experimental calculations and textbook derivations match standard reference tables to full floating-point precision without compounding rounding errors.

### Hardware Stack Persistence & Register Flow Control
Translating multidisciplinary equations into pure postfix execution highlights the architectural efficiency of the 4-register operational stack ($X, Y, Z, T$). In operations requiring constant reuse, filling Register $T$ provides perpetual constant replication, while the single-cycle parallel harmonic key (`{{key:x∥y}}`) and one-touch recovery via `{{key:LASTX}}` eliminate scratchpad register allocation. The deterministic behavior of the stack ensures rapid, error-free execution across all 58 core scientific formulas.

---

## Diagnostic Checkpoints & Singularity Handling

<div class="admonition warning">
<p class="admonition-title">Diagnostic Checkpoint D.1: Scientific Exponent Entry Syntax</p>
<p>Never press `{{key:×}} 10 {{key:yˣ}}` to enter scientific notation! Doing so pushes an extra operator onto the stack, consuming two stack levels.</p>
</div>
> Always use the dedicated **`{{key:E}}`** (Exponent) key:
> * Correct: `1.602176634 {{key:E}} 19 {{key:+/-}}` (Single atomic number entered into Register $X$).  
> * Incorrect: `1.602176634 {{key:ENTER}} 10 {{key:ENTER}} 19 {{key:+/-}} {{key:yˣ}} {{key:×}}` (Consumes 4 stack registers and risks stack overflow).

<div class="admonition warning">
<p class="admonition-title">Diagnostic Checkpoint D.2: Trigonometric Angular Modes in Physical Laws</p>
<p>Physical formulas involving wave motion, optics, and projectile trajectories demand careful attention to the active angular mode:</p>
</div>
> * **Geometric & Surveying Formulas (Snell's Law, Law of Cosines, Great Circle):** Require Degrees mode (`{{key:MODES}} {{key:DEG}}`).
> * **Analytical Calculus & Fourier Syntheses (Pendulum period, Harmonic oscillations):** Require Radians mode (`{{key:MODES}} {{key:RAD}}`).
> Verify the LCD annunciator at the top of the display before running chained trigonometric sequences.

<div class="admonition warning">
<p class="admonition-title">Diagnostic Checkpoint D.3: Mathematical Singularity and Boundary Handling</p>
<p>* **Division by Zero ($x / 0$):** The SC-32 halts chained execution and displays `DIV BY ZERO`. Press `{{key:<-}}` to recover prior stack state.</p>
</div>
> * **Square Root of Negative Real ($\sqrt{-x}$):** In Real mode, displays `INVALID ARG`. In Complex mode ({{key:CMPLX}}), returns pure imaginary result $i\sqrt{x}$ into $(x, y)$ coordinate representation.  
> * **Logarithm of Non-Positive Real ($\ln(0)$ or $\ln(-x)$):** Displays `DOMAIN ERROR`.
