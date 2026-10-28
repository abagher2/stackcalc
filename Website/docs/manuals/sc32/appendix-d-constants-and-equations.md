---
title: "Appendix D: Mathematical Constants, SI Units & Master STEM Equation Directory | Thinking in the Stack (SC-32)"
description: "Authoritative reference directory of immutable mathematical constants, complete BIPM SI prefixes, exact unit conversions, and 100 master STEM engineering equations with optimal RPN keystrokes for the StackCalc SC-32."
---

# Appendix D: Mathematical Constants, SI Units & Master STEM Equation Directory

## Mathematical Constants, BIPM SI Prefixes & Exact Unit Conversions

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

### Fundamental Mathematical Constants

Unlike empirical physical measurements (such as the Newtonian gravitational constant $G$, the fine-structure constant $\alpha$, or subatomic particle masses, which are periodically revised by international CODATA adjustments and are therefore stated explicitly within individual problem benchmarks in the Master STEM Equation Directory below), pure mathematical constants are timeless invariants. The table below lists the fundamental mathematical constants and their exact SC-32 RPN generation sequences.

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
| **Radians-to-Degrees Factor** ($\frac{180}{\pi}$) | $\text{rad}\to\text{deg}$ | `57.2957795130823` | `1 {{key:▸DEG}}` |
| **Degrees-to-Radians Factor** ($\frac{\pi}{180}$) | $\text{deg}\to\text{rad}$ | `0.01745329251994` | `1 {{key:▸RAD}}` |

### International Standard Unit Conversions & BIPM SI Prefixes

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
| **Length** | Inch (`in`) | Centimeter (`cm`) / Meter (`m`) | $1\text{ in} \equiv 2.54\text{ cm} \equiv 0.0254\text{ m}$ (exact) | `{{key:▸cm}}` / `{{key:▸in}}` |
| **Length** | Foot (`ft`) | Meter (`m`) | $1\text{ ft} \equiv 0.3048\text{ m}$ (exact) | `0.3048 {{key:×}}` |
| **Length** | Yard (`yd`) | Meter (`m`) | $1\text{ yd} \equiv 0.9144\text{ m}$ (exact) | `0.9144 {{key:×}}` |
| **Length** | Statute Mile (`mi`) | Kilometer (`km`) | $1\text{ mi} \equiv 1.609344\text{ km}$ (exact) | `{{key:▸km}}` / `{{key:▸mi}}` |
| **Length** | Nautical Mile (`nmi`) | Meter (`m`) | $1\text{ nmi} \equiv 1852\text{ m}$ (exact) | `1852 {{key:×}}` |
| **Mass** | Avoirdupois Pound (`lb`) | Kilogram (`kg`) | $1\text{ lb} \equiv 0.45359237\text{ kg}$ (exact) | `{{key:▸kg}}` / `{{key:▸lb}}` |
| **Volume** | U.S. Liquid Gallon (`gal`) | Liter (`L`) | $1\text{ gal} \equiv 3.785411784\text{ L}$ (exact, $231\text{ in}^3$) | `{{key:▸l}}` / `{{key:▸gal}}` |
| **Pressure** | Standard Atmosphere (`atm`) | Pascal (`Pa`) | $1\text{ atm} \equiv 101,325\text{ Pa}$ (exact) | `101325 {{key:×}}` |
| **Pressure** | Bar (`bar`) | Pascal (`Pa`) | $1\text{ bar} \equiv 100,000\text{ Pa}$ (exact) | `1 {{key:E}} 5 {{key:×}}` |
| **Energy** | Thermochemical Calorie (`cal`) | Joule (`J`) | $1\text{ cal}_{\text{th}} \equiv 4.184\text{ J}$ (exact) | `4.184 {{key:×}}` |
| **Energy** | Kilowatt-hour (`kWh`) | Joule (`J`) | $1\text{ kWh} \equiv 3.6 \times 10^6\text{ J}$ (exact) | `3.6 {{key:E}} 6 {{key:×}}` |
| **Temperature** | Fahrenheit (`°F`) | Celsius (`°C`) | $T_{\text{C}} = (T_{\text{F}} - 32) \times \frac{5}{9}$ (exact) | `{{key:▸°C}}` / `{{key:▸°F}}` |
| **Temperature** | Celsius (`°C`) | Kelvin (`K`) | $T_{\text{K}} = T_{\text{C}} + 273.15$ (exact) | `273.15 {{key:+}}` |
| **Time / Angle** | Sexagesimal (`H.MMSS`) | Decimal (`HR` / `DEG`) | $H + \frac{M}{60} + \frac{S}{3600}$ | `{{key:▸HR}}` / `{{key:▸HMS}}` |

---

## Master STEM Equation Directory: 100 Essential Equations

Every entry in this directory (`Equations E.01–E.100`) pairs its formal mathematical definition and variable descriptions with its physical or geometric motivation, optimal parenthesis-free RPN keystroke sequence, verified numerical benchmark, and cross-references to the chapters where these models are developed in depth.

| Discipline / Subject | Appendix Equations | Chapter Cross-References |
|:---|:---|:---|
| 1. Classical Mechanics, Orbital Dynamics & Statics | Equations E.01 – E.10 | [Prologue](index.md) • [Ch. 2](02-rpn-stack-dynamics.md) • [Ch. 13](13-applied-stem-case-studies.md) • [Ch. 14](14-uil-contest-playbook.md) |
| 2. Fluid Mechanics, Hydraulics & Aerodynamics | Equations E.11 – E.18 | [Prologue](index.md) • [Ch. 7](07-polynomials-brent-solver.md) • [Ch. 13](13-applied-stem-case-studies.md) |
| 3. Thermodynamics, Gas Laws & Heat Transfer | Equations E.19 – E.26 | [Prologue](index.md) • [Ch. 2](02-rpn-stack-dynamics.md) • [Ch. 3](03-algebra-transcendentals.md) • [Ch. 13](13-applied-stem-case-studies.md) |
| 4. Electricity, Magnetism & AC Circuit Analysis | Equations E.27 – E.36 | [Prologue](index.md) • [Ch. 2](02-rpn-stack-dynamics.md) • [Ch. 3](03-algebra-transcendentals.md) • [Ch. 5](05-complex-numbers-phasors.md) |
| 5. Wave Mechanics, Acoustics & Physical Optics | Equations E.37 – E.44 | [Prologue](index.md) • [Ch. 2](02-rpn-stack-dynamics.md) • [Ch. 4](04-trig-vectors-polar.md) • [Ch. 13](13-applied-stem-case-studies.md) |
| 6. Nuclear, Atomic & Relativistic Physics | Equations E.45 – E.51 | [Prologue](index.md) • [Ch. 3](03-algebra-transcendentals.md) • [Ch. 8](08-calculus-romberg-quadrature.md) • [Ch. 13](13-applied-stem-case-studies.md) |
| 7. Coordinate Geometry, Mensuration & 2D Curved Sections | Equations E.52 – E.66 | [Ch. 4](04-trig-vectors-polar.md) • [Ch. 6](06-geometry-surface-area.md) • [Ch. 12](12-function-scatter-plotting.md) • [Ch. 14](14-uil-contest-playbook.md) |
| 8. 3D Solid Geometry & Mensuration Master Compendium | Equations E.67 – E.72 | [Prologue](index.md) • [Ch. 6](06-geometry-surface-area.md) • [Ch. 14](14-uil-contest-playbook.md) |
| 9. Financial Mathematics, Amortization & Time Value of Money | Equations E.73 – E.77 | [Prologue](index.md) • [Ch. 2](02-rpn-stack-dynamics.md) • [Ch. 11](11-financial-tvm.md) |
| 10. Chemistry, Electrochemistry, Chemical Kinetics & Biochemistry | Equations E.78 – E.85 | [Prologue](index.md) • [Ch. 3](03-algebra-transcendentals.md) • [Ch. 9](09-statistics-curve-fitting.md) • [Ch. 12](12-function-scatter-plotting.md) |
| 11. Probability, Statistics, Quality Control & Information Theory | Equations E.86 – E.93 | [Ch. 8](08-calculus-romberg-quadrature.md) • [Ch. 9](09-statistics-curve-fitting.md) • [Ch. 12](12-function-scatter-plotting.md) |
| 12. Structural Mechanics, Semiconductor Electronics, RF & Computer Engineering | Equations E.94 – E.100 | [Prologue](index.md) • [Ch. 1](01-craftsmanship-hardware.md) • [Ch. 7](07-polynomials-brent-solver.md) • [Ch. 10](10-computer-science-bases.md) • [Ch. 12](12-function-scatter-plotting.md) |

---

### Section 1: Classical Mechanics, Orbital Dynamics & Statics

Equations E.01–E.10 cover linear and rotational kinematics, Newtonian gravitation, orbital trajectories, and structural column buckling.

**Equation E.01 — Kinematic Velocity-Displacement Relation:**
$$v_f = \sqrt{v_i^2 + 2 a \Delta x}$$
With initial velocity $v_i$ ($\text{m/s}$), constant acceleration $a$ ($\text{m/s}^2$), and displacement $\Delta x$ ($\text{m}$).
Eliminates elapsed time $t$ by equating work per unit mass ($a \Delta x$) to the change in specific kinetic energy $\frac{1}{2}(v_f^2 - v_i^2)$, governing braking distances and runway takeoff rolls.  
On the stack, key in `vi {{key:x²}} 2 {{key:ENTER}} a {{key:×}} dx {{key:×}} {{key:+}} {{key:√x}}`.
For the benchmark case ($v_i = 12.0\text{ m/s}, a = 4.5\text{ m/s}^2, \Delta x = 25.0\text{ m}$), this yields **`19.209373`** $\text{m/s}$.

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `12 {{key:x²}}` | 0.00 | 0.00 | 0.00 | 144.0000 | Square initial velocity $v_i^2 = 144.0000\text{ m}^2/\text{s}^2$ |
| `2 {{key:ENTER}} 4.5 {{key:×}}` | 0.00 | 0.00 | 144.0000 | 9.0000 | Double acceleration $2a = 9.0000\text{ m/s}^2$; $v_i^2$ lifts to $Y$ |
| `25 {{key:×}} {{key:+}}` | 0.00 | 0.00 | 0.00 | 369.0000 | Add $2a\Delta x = 225.0$ to $v_i^2$ for $v_f^2 = 369.0000\text{ m}^2/\text{s}^2$ |
| `{{key:√x}}` | 0.00 | 0.00 | 0.00 | 19.209373 | Final velocity $v_f = 19.2094\text{ m/s}$ |

---

**Equation E.02 — Projectile Motion Maximum Range:**
$$R = \frac{v_0^2 \sin(2\theta)}{g}$$
Given muzzle velocity $v_0$ ($\text{m/s}$), launch elevation angle $\theta$ (degrees), and standard gravity $g = 9.80665\text{ m/s}^2$.
Couples vertical time-of-flight ($2v_0\sin\theta / g$) with horizontal ground speed ($v_0\cos\theta$) via the double-angle identity $\sin(2\theta) = 2\sin\theta\cos\theta$, peaking at $\theta = 45^\circ$ in vacuum ballistics.  
In `{{key:DEG}}` Mode, key in `v0 {{key:x²}} theta {{key:ENTER}} 2 {{key:×}} {{key:SIN}} {{key:×}} 9.80665 {{key:÷}}` to obtain **`194.0435`** $\text{m}$ for $v_0 = 45.0\text{ m/s}$ and $\theta = 35.0^\circ$.

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `45 {{key:x²}}` | 0.00 | 0.00 | 0.00 | 2025.0000 | Square muzzle velocity $v_0^2 = 2025.0000\text{ m}^2/\text{s}^2$ |
| `35 {{key:ENTER}} 2 {{key:×}}` | 0.00 | 0.00 | 2025.0000 | 70.0000 | Double launch angle $2\theta = 70.0^\circ$; $v_0^2$ lifts to $Y$ |
| `{{key:SIN}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 1902.8711 | Numerator $v_0^2 \sin(70^\circ) = 1902.8711\text{ m}^2/\text{s}^2$ |
| `9.80665 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 194.0435 | Horizontal range $R = 194.0435\text{ m}$ |

---

**Equation E.03 — Centripetal Acceleration & Radial Force:**
$$F_c = \frac{m v^2}{r}$$
With mass $m$ ($\text{kg}$), tangential speed $v$ ($\text{m/s}$), and turn radius $r$ ($\text{m}$).
Measures the inward radial force required to continually bend a body's velocity vector around a circular arc of curvature $1/r$; doubling cornering speed quadruples lateral tire or rotor blade load.  
Keying `v {{key:x²}} m {{key:×}} r {{key:÷}}` resolves the benchmark case ($m = 1250\text{ kg}, v = 24.0\text{ m/s}, r = 60.0\text{ m}$) via `{{res:sc32_appendix_d_constants_and_equations_seq_01:keys}}` to **`{{res:sc32_appendix_d_constants_and_equations_seq_01:value}}`** $\text{N}$ ($12.0\text{ kN}$).

---

**Equation E.04 — Newton's Law of Universal Gravitation:**
$$F_g = G \frac{m_1 m_2}{r^2}$$
With gravitational constant $G = 6.67430 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2$, masses $m_1, m_2$ ($\text{kg}$), and center-to-center separation $r$ ($\text{m}$).
Inverse-square radial flux law governing planetary orbits, tidal bulges, and spacecraft trajectories across three-dimensional space.  
On the stack, `6.67430 {{key:E}} 11 {{key:+/-}} m1 {{key:×}} m2 {{key:×}} r {{key:x²}} {{key:÷}}` yields **`13038.58`** $\text{N}$ for an $m_2 = 1500\text{ kg}$ spacecraft orbiting Earth ($m_1 = 5.9722 \times 10^{24}\text{ kg}$) at $r = 6.771 \times 10^6\text{ m}$.

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `6.67430 {{key:E}} 11 {{key:+/-}} {{key:ENTER}} 5.9722 {{key:E}} 24 {{key:×}} 1500 {{key:×}}` | 0.00 | 0.00 | 0.00 | 5.9791E17 | Numerator $G m_1 m_2 = 5.97910 \times 10^{17}\text{ N}\cdot\text{m}^2$ |
| `6.771 {{key:E}} 6 {{key:x²}}` | 0.00 | 0.00 | 5.9791E17 | 4.5846E13 | Square orbital radius $r^2 = 4.58464 \times 10^{13}\text{ m}^2$ |
| `{{key:÷}}` | 0.00 | 0.00 | 0.00 | 13038.58 | Gravitational force $F_g = 13,038.58\text{ N}$ |

---

**Equation E.05 — Circular Orbital Velocity:**
$$v = \sqrt{\frac{\mu}{r}}$$
Defined by geocentric gravitational parameter $\mu = GM_\oplus = 3.986004418 \times 10^{14}\text{ m}^3/\text{s}^2$ and orbital radius $r$ ($\text{m}$).
Balances centrifugal acceleration $v^2/r$ against gravity $\mu/r^2$; counterintuitively, satellites in higher orbits travel at *slower* linear speeds.  
Executing `3.986004418 {{key:E}} 14 {{key:ENTER}} r {{key:÷}} {{key:√x}}` at $r = 6.771 \times 10^6\text{ m}$ ($400\text{ km}$ Low Earth Orbit) gives **`7672.76`** $\text{m/s}$.

---

**Equation E.06 — Planetary Escape Velocity:**
$$v_{\text{esc}} = \sqrt{\frac{2 \mu}{r}} = v_{\text{orbital}} \times \sqrt{2}$$
With gravitational parameter $\mu$ ($\text{m}^3/\text{s}^2$) and radial distance $r$ ($\text{m}$).
Minimum parabolic launch speed where kinetic energy $\frac{1}{2}mv^2$ exactly cancels gravitational potential well depth $GMm/r$—always $\sqrt{2} \approx 1.4142$ times the local circular orbital speed.  
Keying `2 {{key:ENTER}} mu {{key:×}} r {{key:÷}} {{key:√x}}` at Earth's mean radius ($r = 6.371 \times 10^6\text{ m}, \mu = 3.986004418 \times 10^{14}$) produces **`11186.0`** $\text{m/s}$ ($11.19\text{ km/s}$).

---

**Equation E.07 — Tsiolkovsky Rocket Burnout Equation:**
$$\Delta v = v_e \ln\left(\frac{m_0}{m_f}\right)$$
With effective exhaust velocity $v_e = I_{\text{sp}} g_0$ ($\text{m/s}$), initial wet mass $m_0$, and final dry burnout mass $m_f$.
Integrates momentum conservation for a variable-mass vehicle; because velocity gain grows only logarithmically with mass ratio $m_0/m_f$, deep-space missions require high-exhaust-velocity engines or multi-stage tank shedding.  
On the stack, `m0 {{key:ENTER}} mf {{key:÷}} {{key:LN}} ve {{key:×}}` evaluates $v_e = 3100\text{ m/s}, m_0 = 45000\text{ kg}, m_f = 6500\text{ kg}$ to **`6000.12`** $\text{m/s}$.

---

**Equation E.08 — Rotational Kinetic Energy of Rigid Body:**
$$E_{\text{rot}} = \frac{1}{2} I \omega^2$$
With mass moment of inertia $I = \int r^2\,dm$ ($\text{kg}\cdot\text{m}^2$) and angular velocity $\omega$ ($\text{rad/s}$).
Rotational twin of $\frac{1}{2}mv^2$; governs energy storage in mechanical flywheels, turbine rotors, and spinning spacecraft reaction wheels.  
Evaluating `omega {{key:x²}} I {{key:×}} 2 {{key:÷}}` for a flywheel with $I = 4.25\text{ kg}\cdot\text{m}^2$ spinning at $\omega = 150.0\text{ rad/s}$ yields **`47812.5`** $\text{J}$ ($47.81\text{ kJ}$).

---

**Equation E.09 — Simple Gravity Pendulum Period:**
$$T = 2\pi \sqrt{\frac{L}{g}}$$
With pivot-to-bob length $L$ ($\text{m}$) and local gravitational acceleration $g = 9.80665\text{ m/s}^2$.
Christiaan Huygens's small-angle isochronism law: the period depends only on length $L$ and gravity $g$, independent of bob mass.  
Keying `L {{key:ENTER}} 9.80665 {{key:÷}} {{key:√x}} 2 {{key:×}} {{key:π}} {{key:×}}` for a Huygens seconds pendulum ($L = 0.99362\text{ m}$, $1\text{ s}$ per half-swing) confirms $T =$ **`2.00000`** $\text{s}$.

---

**Equation E.10 — Euler Critical Buckling Load for Slender Column:**
$$P_{\text{cr}} = \frac{\pi^2 E I}{K^2 L^2}$$
With Young's modulus $E$ ($\text{Pa}$), weak-axis area moment of inertia $I$ ($\text{m}^4$), effective end-restraint factor $K$, and unsupported length $L$ ($\text{m}$).
Shows that slender struts fail by sudden lateral bowing at a load governed entirely by stiffness $EI$ and inverse-square length $1/L^2$ rather than material crushing strength.  
On the stack, `{{key:π}} {{key:x²}} E {{key:×}} I {{key:×}} K {{key:ENTER}} L {{key:×}} {{key:x²}} {{key:÷}}` evaluates $E = 200 \times 10^9\text{ Pa}, I = 6.4 \times 10^{-6}\text{ m}^4, K = 1.0, L = 4.5\text{ m}$ to **`623869.6`** $\text{N}$ ($623.87\text{ kN}$).

---

### Section 2: Fluid Mechanics, Hydraulics & Aerodynamics

Equations E.11–E.18 span incompressible pipe flow, viscous friction head loss, open-channel hydraulics, and compressible flight regimes.

**Equation E.11 — Torricelli Efflux Jet Velocity:**

$$v = \sqrt{2 g h}$$
With gravitational acceleration $g = 9.80665\text{ m/s}^2$ and hydrostatic fluid head $h$ ($\text{m}$).
Evangelista Torricelli's 1643 discovery (a direct corollary of Bernoulli's equation) that water spurting from an orifice at depth $h$ exits at the exact speed of a body falling freely from height $h$.  
Keying `2 {{key:ENTER}} 9.80665 {{key:×}} h {{key:×}} {{key:√x}}` for a tank head of $h = 5.0\text{ m}$ produces **`9.90285`** $\text{m/s}$.

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `2 {{key:ENTER}} 9.80665 {{key:×}}` | 0.00 | 0.00 | 0.00 | 19.613300 | Double gravitational acceleration $2g = 19.6133\text{ m/s}^2$ |
| `5 {{key:×}}` | 0.00 | 0.00 | 0.00 | 98.066500 | Scale by fluid head $2gh = 98.0665\text{ m}^2/\text{s}^2$ |
| `{{key:√x}}` | 0.00 | 0.00 | 0.00 | 9.902853 | Torricelli efflux velocity $v = 9.9029\text{ m/s}$ |

---

**Equation E.12 — Volumetric Flow Continuity Equation:**
$$Q = A_1 v_1 = \frac{\pi D_1^2}{4} v_1$$
With internal pipe diameter $D_1$ ($\text{m}$) and mean cross-sectional velocity $v_1$ ($\text{m/s}$).
Expresses conservation of mass for incompressible fluids: halving a pipe's diameter shrinks its area fourfold and forces flow velocity to quadruple.  
On the stack, `D {{key:x²}} {{key:π}} {{key:×}} 4 {{key:÷}} v {{key:×}}` evaluates a $D = 0.15\text{ m}$ main flowing at $v = 2.4\text{ m/s}$ to **`0.0424115`** $\text{m}^3/\text{s}$ ($42.41\text{ L/s}$).

---

**Equation E.13 — Reynolds Number for Pipe Flow:**
$$Re = \frac{\rho v D}{\mu}$$
With fluid density $\rho$ ($\text{kg/m}^3$), mean velocity $v$ ($\text{m/s}$), hydraulic diameter $D$ ($\text{m}$), and dynamic viscosity $\mu$ ($\text{Pa}\cdot\text{s}$).
Dimensionless ratio of inertial momentum forces to viscous shear damping; pipe flow transitions from smooth laminar sheets ($Re < 2300$) to chaotic turbulent eddies above $Re \approx 4000$.  
Evaluating `rho {{key:ENTER}} v {{key:×}} D {{key:×}} mu {{key:÷}}` for water at $20^\circ\text{C}$ ($\rho = 998\text{ kg/m}^3, v = 1.8\text{ m/s}, D = 0.05\text{ m}, \mu = 0.001002\text{ Pa}\cdot\text{s}$) yields **`89640.7`** (fully turbulent).

---

**Equation E.14 — Darcy-Weisbach Friction Head Loss:**
$$h_f = f \frac{L}{D} \frac{v^2}{2 g}$$
With Moody Darcy friction factor $f$, pipe length $L$ ($\text{m}$), diameter $D$ ($\text{m}$), flow velocity $v$ ($\text{m/s}$), and $g = 9.80665\text{ m/s}^2$.
Quantifies the irreversible pressure head dissipated by wall shear across long pipelines and municipal water mains, scaling quadratically with flow speed $v^2$.  
Keying `f {{key:ENTER}} L {{key:×}} D {{key:÷}} v {{key:x²}} {{key:×}} 2 {{key:÷}} 9.80665 {{key:÷}}` for $f = 0.024, L = 120.0\text{ m}, D = 0.20\text{ m}, v = 2.5\text{ m/s}$ gives $h_f =$ **`4.5887`** $\text{m}$.

---

**Equation E.15 — Manning Formula for Open Channel Uniform Flow:**
$$v = \frac{1}{n} R_h^{2/3} S^{1/2}$$
With Gauckler–Manning channel roughness $n$, hydraulic radius $R_h = A / P_{\text{wet}}$ ($\text{m}$), and longitudinal bed slope $S$.
Empirical gravity-flow law used by civil engineers to size aqueducts, storm drains, and river spillways where free-surface gravity balances bed friction.  
On the stack, `Rh {{key:ENTER}} 2 {{key:ENTER}} 3 {{key:÷}} {{key:yˣ}} S {{key:√x}} {{key:×}} n {{key:÷}}` evaluates $n = 0.015, R_h = 0.85\text{ m}, S = 0.0025$ to **`2.9918`** $\text{m/s}$.

---

**Equation E.16 — Poiseuille Laminar Capillary Flow Rate:**
$$Q = \frac{\pi r^4 \Delta P}{8 \mu L}$$
With tube inner radius $r$ ($\text{m}$), pressure differential $\Delta P$ ($\text{Pa}$), dynamic viscosity $\mu$ ($\text{Pa}\cdot\text{s}$), and tube length $L$ ($\text{m}$).
Hagen–Poiseuille fourth-power law ($r^4$): narrowing a microchannel or human coronary artery by just $16\%$ cuts laminar volumetric throughput in half!  
Executing `r {{key:ENTER}} 4 {{key:yˣ}} {{key:π}} {{key:×}} dP {{key:×}} 8 {{key:÷}} mu {{key:÷}} L {{key:÷}}` for $r = 0.002\text{ m}, \Delta P = 5000\text{ Pa}, \mu = 0.0035\text{ Pa}\cdot\text{s}, L = 0.50\text{ m}$ yields **`1.7952 × 10⁻⁵`** $\text{m}^3/\text{s}$.

---

**Equation E.17 — Aerodynamic Dynamic Pressure:**
$$q = \frac{1}{2} \rho v^2$$
With ambient air density $\rho$ ($\text{kg/m}^3$) and true airspeed $v$ ($\text{m/s}$).
Kinetic energy per unit volume of a moving airstream; measured directly by Pitot-static tubes and multiplied by wing area $S$ and coefficients $C_L, C_D$ to determine aerodynamic lift and drag.  
Keying `v {{key:x²}} rho {{key:×}} 2 {{key:÷}}` at sea level ($\rho = 1.225\text{ kg/m}^3, v = 65.0\text{ m/s}$) returns **`2587.81`** $\text{Pa}$.

---

**Equation E.18 — Compressible Flow Mach Number:**
$$M = \frac{v}{\sqrt{\gamma R_{\text{specific}} T}}$$
With true airspeed $v$ ($\text{m/s}$), diatomic adiabatic index $\gamma = 1.40$, specific gas constant for dry air $R_{\text{specific}} = 287.058\text{ J/(kg}\cdot\text{K)}$, and static temperature $T$ ($\text{K}$).
Compares flight speed against the local acoustic wave speed $a = \sqrt{\gamma R T}$, which drops in the cold stratosphere ($T = 245\text{ K}$) and brings high-altitude airliners near the transonic drag rise.  
Computing the speed of sound first and swapping via `1.4 {{key:ENTER}} 287.058 {{key:×}} T {{key:×}} {{key:√x}} v {{key:x⇄y}} {{key:÷}}` for $v = 240.0\text{ m/s}$ at $T = 245.0\text{ K}$ gives Mach **`0.7651`**.

---

### Section 3: Thermodynamics, Gas Laws & Heat Transfer

Equations E.19–E.26 evaluate ideal gas state relations, thermodynamic power cycle efficiencies, radiative and conductive heat transfer, and phase-change energy.

**Equation E.19 — Ideal Gas State Equation:**
$$P = \frac{n R T}{V}$$
With molar quantity $n$ ($\text{mol}$), universal gas constant $R = 8.314462618\text{ J/(mol}\cdot\text{K)}$, absolute temperature $T$ ($\text{K}$), and vessel volume $V$ ($\text{m}^3$).
Unifies Boyle's, Charles's, and Avogadro's laws by linking macroscopic wall pressure $P$ to the microscopic thermal kinetic energy $nRT$ of colliding gas molecules.  
Keying `n {{key:ENTER}} 8.314462618 {{key:×}} T {{key:×}} V {{key:÷}}` for $n = 4.5\text{ mol}$ at $T = 350.0\text{ K}$ inside $V = 0.035\text{ m}^3$ yields **`374150.8`** $\text{Pa}$ ($374.15\text{ kPa}$).

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `4.5 {{key:ENTER}} 8.314462618 {{key:×}}` | 0.00 | 0.00 | 0.00 | 37.415082 | Molar heat capacity product $nR = 37.4151\text{ J/K}$ |
| `350 {{key:×}}` | 0.00 | 0.00 | 0.00 | 13095.279 | Thermal energy $nRT = 13,095.28\text{ J}$ |
| `.035 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 374150.82 | Ideal gas pressure $P = 374,150.8\text{ Pa}$ |

---

**Equation E.20 — Carnot Thermodynamic Cycle Maximum Efficiency:**
$$\eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H}$$
With cold sink temperature $T_C$ ($\text{K}$) and hot source temperature $T_H$ ($\text{K}$).
Sadi Carnot's Second-Law upper bound on heat-to-work conversion between two thermal reservoirs, proving that zero-entropy-rejection ($100\%$) efficiency would require a $0\text{ K}$ cold sink.  
On the stack, `TC {{key:ENTER}} TH {{key:÷}} 1 {{key:x⇄y}} {{key:-}}` evaluates $T_C = 295.0\text{ K}$ and $T_H = 850.0\text{ K}$ to **`0.65294`** ($65.29\%$).

---

**Equation E.21 — Stefan-Boltzmann Total Radiative Power:**
$$P = \sigma \epsilon A T^4$$
With Stefan–Boltzmann constant $\sigma = 5.670374419 \times 10^{-8}\text{ W/(m}^2\cdot\text{K}^4)$, surface emissivity $\epsilon$, radiating area $A$ ($\text{m}^2$), and absolute temperature $T$ ($\text{K}$).
Integrates Planck's blackbody spectrum over all wavelengths; because radiative heat rejection scales as $T^4$, doubling the absolute temperature of a furnace element or spacecraft radiator multiplies emitted power sixteenfold.  
Executing `T {{key:ENTER}} 4 {{key:yˣ}} A {{key:×}} eps {{key:×}} 5.670374419 {{key:E}} 8 {{key:+/-}} {{key:×}}` for $T = 1200.0\text{ K}, A = 1.8\text{ m}^2, \epsilon = 0.85$ gives **`179830.8`** $\text{W}$ ($179.83\text{ kW}$).

---

**Equation E.22 — Fourier Conduction Heat Transfer Rate:**
$$q = \frac{k A (T_1 - T_2)}{L}$$
With thermal conductivity $k$ ($\text{W/(m}\cdot\text{K)}$), cross-sectional area $A$ ($\text{m}^2$), face temperatures $T_1, T_2$ ($\text{K}$), and wall thickness $L$ ($\text{m}$).
Thermal analog of Ohm's law ($q = \Delta T / R_{\text{th}}$ with $R_{\text{th}} = L / (kA)$), governing building insulation, heat-sink baseplates, and cryogenic Dewar walls.  
Keying `T1 {{key:ENTER}} T2 {{key:-}} k {{key:×}} A {{key:×}} L {{key:÷}}` for a $k = 0.75\text{ W/(m}\cdot\text{K)}, A = 15.0\text{ m}^2, L = 0.20\text{ m}$ masonry wall across $T_1 = 295.15\text{ K}$ and $T_2 = 263.15\text{ K}$ yields **`1800.0`** $\text{W}$.

---

**Equation E.23 — Newton's Law of Cooling Transient Temperature:**
$$T(t) = T_{\infty} + (T_0 - T_{\infty}) e^{-k t}$$
With ambient temperature $T_\infty$, initial object temperature $T_0$, convective time-constant rate $k = hA/(mc_p)$ ($\text{s}^{-1}$), and elapsed time $t$ ($\text{s}$).
Models exponential thermal relaxation of a lumped heat capacity toward surrounding air or quench bath temperature.  
Unpeeling from the exponent outward via `k {{key:+/-}} t {{key:×}} {{key:eˣ}} T0 {{key:ENTER}} Tinf {{key:-}} {{key:×}} Tinf {{key:+}}` for $T_\infty = 20.0^\circ\text{C}, T_0 = 90.0^\circ\text{C}, k = 0.005\text{ s}^{-1}, t = 180.0\text{ s}$ resolves $T(180) =$ **`48.46`** $^\circ\text{C}$.

---

**Equation E.24 — Logarithmic Mean Temperature Difference (LMTD):**
$$\text{LMTD} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)}$$
With hot-to-cold terminal temperature approaches $\Delta T_1$ and $\Delta T_2$ ($\text{K}$ or $^\circ\text{C}$) at the two ends of a heat exchanger.
Exact integrated driving temperature difference across parallel or counterflow shell-and-tube heat exchangers where $\Delta T(x)$ decays exponentially along the tube bundle.  
On the stack, `dT1 {{key:ENTER}} dT2 {{key:-}} dT1 {{key:ENTER}} dT2 {{key:÷}} {{key:LN}} {{key:÷}}` evaluates $\Delta T_1 = 45.0\text{ K}$ and $\Delta T_2 = 18.0\text{ K}$ to **`29.4665`** $\text{K}$.

---

**Equation E.25 — Ideal Brayton Gas Turbine Thermal Efficiency:**
$$\eta = 1 - \frac{1}{r_p^{(\gamma - 1)/\gamma}}$$
With compressor pressure ratio $r_p = P_2 / P_1$ and working-gas specific-heat ratio $\gamma = c_p / c_v = 1.40$.
Explains why modern jet aircraft engines and industrial gas turbines employ multi-stage axial compressors with high pressure ratios $r_p$ to maximize fuel efficiency.  
Keying `rp {{key:ENTER}} 1.4 {{key:ENTER}} 1 {{key:-}} 1.4 {{key:÷}} {{key:yˣ}} {{key:1/x}} 1 {{key:x⇄y}} {{key:-}}` at $r_p = 16.0$ and $\gamma = 1.40$ gives **`0.5476`** ($54.76\%$).

---

**Equation E.26 — Latent Heat Phase Transition Energy:**
$$Q = m L_v$$
With phase-changing mass $m$ ($\text{kg}$) and specific latent heat of vaporization (or fusion) $L_v$ ($\text{J/kg}$).
Isothermal enthalpy absorbed to break intermolecular bonds during boiling or melting without raising thermometer temperature; water's huge $L_v$ drives steam boilers and evaporative cooling towers.  
Multiplying `m {{key:ENTER}} Lv {{key:×}}` for $m = 2.5\text{ kg}$ of water at $100^\circ\text{C}$ ($L_v = 2.26 \times 10^6\text{ J/kg}$) yields **`5650000.0`** $\text{J}$ ($5.65\text{ MJ}$).

---

### Section 4: Electricity, Magnetism & AC Circuit Analysis

Equations E.27–E.36 address DC resistive networks, reactive energy storage, RC/RL transients, RLC resonance, and decibel power ratios.

**Equation E.27 — Ohm's Law and DC Power Dissipation:**
$$P = I^2 R = \frac{V^2}{R} = V I$$
With terminal voltage $V$ ($\text{V}$), resistance $R$ ($\Omega$), and current $I$ ($\text{A}$).
James Prescott Joule and Georg Simon Ohm's law of resistive heating: doubling line voltage across a fixed load resistor quadruples thermal dissipation.  
Keying `V {{key:x²}} R {{key:÷}}` for a $V = 120.0\text{ V}$ heating element of resistance $R = 15.0\,\Omega$ gives **`960.0`** $\text{W}$.

---

**Equation E.28 — Equivalent Resistance of Parallel Networks via `{{key:x∥y}}`:**
$$R_{\text{eq}} = R_1 \parallel R_2 \parallel R_3 = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}}$$
With parallel branch resistances $R_1, R_2, R_3$ ($\Omega$).
Conductances ($G_i = 1/R_i$) add in parallel; the SC-32's hardware `{{key:x∥y}}` key collapses each pair in a single stroke without reciprocals or parentheses.  
Chaining `R1 {{key:ENTER}} R2 {{key:x∥y}} R3 {{key:x∥y}}` for $R_1 = 100.0\,\Omega, R_2 = 150.0\,\Omega, R_3 = 300.0\,\Omega$ yields **`50.0`** $\Omega$.

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `100 {{key:ENTER}}` | 0.00 | 0.00 | 100.0000 | 100.0000 | Stage first parallel branch $R_1 = 100.0\,\Omega$ in $Y$ |
| `150 {{key:x∥y}}` | 0.00 | 0.00 | 0.00 | 60.0000 | Parallel combination $100 \parallel 150 = 60.0\,\Omega$ |
| `300 {{key:x∥y}}` | 0.00 | 0.00 | 0.00 | 50.0000 | Parallel combination $60 \parallel 300 = 50.0\,\Omega$ |

---

**Equation E.29 — Electrostatic Energy Stored in Capacitor:**
$$U_C = \frac{1}{2} C V^2$$
With capacitance $C$ ($\text{F}$) and DC bus voltage $V$ ($\text{V}$).
Integrates $q\,dV = C V\,dV$ as charge builds across dielectric plates; governs pulsed-laser flashlamp banks, defibrillators, and inverter DC links.  
On the stack, `V {{key:x²}} C {{key:×}} 2 {{key:÷}}` evaluates a $C = 47.0 \times 10^{-6}\text{ F}$ bus capacitor charged to $V = 450.0\text{ V}$ to **`4.75875`** $\text{J}$.

---

**Equation E.30 — Magnetic Energy Stored in Inductor:**
$$U_L = \frac{1}{2} L I^2$$
With inductance $L$ ($\text{H}$) and winding current $I$ ($\text{A}$).
Electromagnetic dual of capacitor energy ($\frac{1}{2}CV^2$), storing energy in the magnetic flux field of buck/boost switching converters and superconducting magnets.  
Keying `I {{key:x²}} L {{key:×}} 2 {{key:÷}}` for an $L = 0.25\text{ H}$ choke carrying $I = 6.4\text{ A}$ yields **`5.12`** $\text{J}$.

---

**Equation E.31 — RC Transient Charging Voltage:**
$$V_C(t) = V_0 \left(1 - e^{-t / (R C)}\right)$$
With step supply voltage $V_0$ ($\text{V}$), series resistance $R$ ($\Omega$), capacitance $C$ ($\text{F}$), and elapsed time $t$ ($\text{s}$).
First-order relaxation toward asymptote $V_0$ with time constant $\tau = RC$; reaches $63.2\%$ of full charge at $t = \tau$ and $99.3\%$ at $t = 5\tau$.  
Evaluating `t {{key:+/-}} R {{key:÷}} C {{key:÷}} {{key:eˣ}} 1 {{key:x⇄y}} {{key:-}} V0 {{key:×}}` for $V_0 = 12.0\text{ V}, R = 10000.0\,\Omega, C = 220.0 \times 10^{-6}\text{ F}$ ($\tau = 2.2\text{ s}$) at $t = 3.5\text{ s}$ gives **`9.5583`** $\text{V}$.

---

**Equation E.32 — RL Inductive Current Decay:**
$$I(t) = I_0 e^{-t (R / L)}$$
With initial steady current $I_0$ ($\text{A}$), loop resistance $R$ ($\Omega$), inductance $L$ ($\text{H}$), and time $t$ ($\text{s}$).
Natural exponential decay of magnetic flux with inductive time constant $\tau = L/R$ when a solenoid or relay coil discharges through a flyback path.  
On the stack, `t {{key:+/-}} R {{key:×}} L {{key:÷}} {{key:eˣ}} I0 {{key:×}}` evaluates $I_0 = 5.0\text{ A}, R = 24.0\,\Omega, L = 0.80\text{ H}$ at $t = 0.05\text{ s}$ to **`1.1157`** $\text{A}$.

---

**Equation E.33 — LC Resonant Frequency:**
$$f_0 = \frac{1}{2 \pi \sqrt{L C}}$$
With tank inductance $L$ ($\text{H}$) and capacitance $C$ ($\text{F}$).
Lord Kelvin's oscillatory resonance condition where inductive reactance $\omega_0 L$ exactly cancels capacitive reactance $1/(\omega_0 C)$, setting the carrier frequency of radio tuners and LC oscillators.  
Keying `L {{key:ENTER}} C {{key:×}} {{key:√x}} 2 {{key:×}} {{key:π}} {{key:×}} {{key:1/x}}` for $L = 10.0 \times 10^{-3}\text{ H}$ and $C = 100.0 \times 10^{-12}\text{ F}$ yields **`159154.9`** $\text{Hz}$ ($159.15\text{ kHz}$).

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `10 {{key:E}} 3 {{key:+/-}} {{key:ENTER}} 100 {{key:E}} 12 {{key:+/-}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 1.0000E-12 | Product $LC = 1.0 \times 10^{-12}\text{ s}^2$ |
| `{{key:√x}}` | 0.00 | 0.00 | 0.00 | 1.0000E-6 | Radical $\sqrt{LC} = 1.0 \times 10^{-6}\text{ s}$ |
| `2 {{key:×}} {{key:π}} {{key:×}} {{key:1/x}}` | 0.00 | 0.00 | 0.00 | 159154.94 | Resonant frequency $f_0 = 159.155\text{ kHz}$ |

---

**Equation E.34 — RLC Series AC Total Impedance:**
$$Z = \sqrt{R^2 + \left(2 \pi f L - \frac{1}{2 \pi f C}\right)^2}$$
With resistance $R$ ($\Omega$), inductance $L$ ($\text{H}$), capacitance $C$ ($\text{F}$), and AC excitation frequency $f$ ($\text{Hz}$).
Pythagorean magnitude of the complex impedance phasor $Z = R + j(X_L - X_C)$, where inductive and capacitive reactances pull $180^\circ$ opposite along the imaginary axis.  
Storing $\omega = 2\pi f$ in `A` via `2 {{key:π}} {{key:×}} f {{key:×}} {{key:STO}} A L {{key:×}} {{key:RCL}} A C {{key:×}} {{key:1/x}} {{key:-}} {{key:x²}} R {{key:x²}} {{key:+}} {{key:√x}}` evaluates $R = 50.0\,\Omega, L = 0.05\text{ H}, C = 10.0 \times 10^{-6}\text{ F}, f = 120.0\text{ Hz}$ to **`107.412`** $\Omega$.

---

**Equation E.35 — Quality Factor of Resonant Circuit:**
$$Q = \frac{1}{R} \sqrt{\frac{L}{C}}$$
With series loss resistance $R$ ($\Omega$), inductance $L$ ($\text{H}$), and capacitance $C$ ($\text{F}$).
Ratio of characteristic tank impedance $\sqrt{L/C}$ to dissipative resistance $R$, measuring both energy storage sharpness and the fractional $-3\text{ dB}$ passband width $\Delta f = f_0 / Q$.  
On the stack, `L {{key:ENTER}} C {{key:÷}} {{key:√x}} R {{key:÷}}` evaluates $R = 8.0\,\Omega, L = 2.5 \times 10^{-3}\text{ H}, C = 47.0 \times 10^{-9}\text{ F}$ to $Q =$ **`28.813`**.

---

**Equation E.36 — Decibel Power Gain Ratio:**
$$\text{dB} = 10 \log_{10}\left(\frac{P_2}{P_1}\right)$$
With reference input power $P_1$ ($\text{W}$) and output power $P_2$ ($\text{W}$).
Alexander Graham Bell's logarithmic transmission unit: converts cascaded amplifier gains and cable attenuations from multiplication into simple addition ($+3.01\text{ dB}$ per power doubling, $+10\text{ dB}$ per tenfold gain).  
Keying `P2 {{key:ENTER}} P1 {{key:÷}} {{key:LOG}} 10 {{key:×}}` for $P_1 = 0.025\text{ W}$ amplified to $P_2 = 120.0\text{ W}$ gives **`36.8124`** $\text{dB}$.

---

### Section 5: Wave Mechanics, Acoustics & Physical Optics

Equations E.37–E.44 model geometric refraction, thin-lens imaging (`{{key:x∥y}}`), acoustic Doppler shifts, room reverberation, and optical diffraction.

**Equation E.37 — Snell's Law of Refraction:**
$$\theta_2 = \arcsin\left(\frac{n_1 \sin\theta_1}{n_2}\right)$$
With refractive indices $n_1, n_2$ and incident angle $\theta_1$ (degrees).
Fermat's principle of least time across a dielectric interface: wavefronts bend toward the normal when entering a denser medium ($n_2 > n_1$) and undergo total internal reflection when $(n_1 / n_2)\sin\theta_1 > 1$.  
In `{{key:DEG}}` mode, keying `theta1 {{key:SIN}} n1 {{key:×}} n2 {{key:÷}} {{key:ASIN}}` for a beam entering crown glass ($n_2 = 1.52$) from air ($n_1 = 1.0003$) at $\theta_1 = 45.0^\circ$ gives **`27.7297`** $^\circ$.

---

**Equation E.38 — Gaussian Thin Lens Equation via `{{key:x∥y}}`:**

$$f = \frac{d_o \cdot d_i}{d_o + d_i} = d_o \parallel d_i$$
With object distance $d_o$ and real-image distance $d_i$.
Paraxial wavefront curvature summation ($1/f = 1/d_o + 1/d_i$): a converging lens maps object and image conjugates via the exact harmonic-product algebra of `{{key:x∥y}}`.  
Pressing `do {{key:ENTER}} di {{key:x∥y}}` for $d_o = 30.0\text{ cm}$ and $d_i = 60.0\text{ cm}$ computes a focal length of **`20.0`** $\text{cm}$ in two keystrokes.

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `30 {{key:ENTER}}` | 0.00 | 0.00 | 30.0000 | 30.0000 | Stage object distance $d_o = 30.0\text{ cm}$ in $Y$ |
| `60 {{key:x∥y}}` | 0.00 | 0.00 | 0.00 | 20.0000 | Thin-lens focal length $f = d_o \parallel d_i = 20.0\text{ cm}$ |

---

**Equation E.39 — Compound Optical Microscope Magnification:**
$$M = -\left(\frac{L_{\text{tube}}}{f_{\text{obj}}}\right) \left(\frac{d_{\text{near}}}{f_{\text{eye}}}\right)$$
With mechanical tube length $L_{\text{tube}} = 160\text{ mm}$, standard human near-point distance $d_{\text{near}} = 250\text{ mm}$, and objective/eyepiece focal lengths $f_{\text{obj}}, f_{\text{eye}}$ ($\text{mm}$).
Two-stage optical cascade: the objective lens projects an inverted real intermediate image magnified by $-L_{\text{tube}}/f_{\text{obj}}$, which the ocular magnifies angularly by $d_{\text{near}}/f_{\text{eye}}$.  
On the stack, `160 {{key:ENTER}} fobj {{key:÷}} 250 {{key:ENTER}} feye {{key:÷}} {{key:×}} {{key:+/-}}` for $f_{\text{obj}} = 4.0\text{ mm}$ and $f_{\text{eye}} = 25.0\text{ mm}$ yields **`-400.0`** ($\times 400$ inverted angular magnification).

---

**Equation E.40 — Acoustic Doppler Frequency Shift (Moving Source):**
$$f' = f_0 \left(\frac{v}{v - v_s}\right)$$
With emitted frequency $f_0$ ($\text{Hz}$), speed of sound $v = 343.0\text{ m/s}$, and source approach speed $v_s$ ($\text{m/s}$).
Spatial compression of acoustic wavefronts ahead of an approaching emitter: as $v_s \to v$, the wavelength $\lambda' = (v - v_s)/f_0$ collapses toward the Mach-1 sonic boom barrier.  
Evaluating `343 {{key:ENTER}} vs {{key:-}} 343 {{key:x⇄y}} {{key:÷}} f0 {{key:×}}` for a $f_0 = 500.0\text{ Hz}$ horn approaching at $v_s = 35.0\text{ m/s}$ returns **`556.818`** $\text{Hz}$.

---

**Equation E.41 — Sound Pressure Decibel Level:**
$$L_p = 20 \log_{10}\left(\frac{P_{\text{rms}}}{P_0}\right)$$
With root-mean-square acoustic pressure $P_{\text{rms}}$ ($\text{Pa}$) and human hearing threshold $P_0 = 20.0 \times 10^{-6}\text{ Pa}$ ($20\text{ }\mu\text{Pa}$).
Because acoustic power intensity scales with pressure squared ($I \propto P_{\text{rms}}^2$), a $10\log_{10}(I/I_0)$ power ratio becomes a $20\log_{10}(P_{\text{rms}}/P_0)$ field-amplitude ratio.  
Keying `Prms {{key:ENTER}} 20 {{key:E}} 6 {{key:+/-}} {{key:÷}} {{key:LOG}} 20 {{key:×}}` at $P_{\text{rms}} = 0.632\text{ Pa}$ gives **`90.0`** $\text{dB}$ SPL.

---

**Equation E.42 — Sabine Reverberation Time for Architectural Enclosure:**
$$RT_{60} = \frac{0.161 V}{A_{\text{total}}}$$
With hall volume $V$ ($\text{m}^3$) and total acoustic absorption area $A_{\text{total}} = \sum S_i \alpha_i$ (metric sabins, $\text{m}^2$).
Wallace Clement Sabine's diffuse-field decay law: the time required for reverberant sound energy to drop by $60\text{ dB}$ ($10^{-6}$) scales directly with mean free path ($\propto V/S$) and inversely with wall absorption.  
Running `0.161 {{key:ENTER}} V {{key:×}} Atot {{key:÷}}` for a recital hall of $V = 850.0\text{ m}^3$ and $A_{\text{total}} = 110.0\text{ sabins}$ yields **`1.244`** $\text{s}$.

---

**Equation E.43 — Optical Diffraction Grating Wavelength:**
$$\lambda = \frac{d \sin\theta}{m}$$
With ruling pitch $d$ ($\text{m}$), diffraction angle $\theta$ (degrees), and spectral order $m$.
Constructive Huygens–Fresnel interference across periodic slits: adjacent rays reinforce only when their path-length difference $d\sin\theta$ equals an integer multiple $m\lambda$.  
In `{{key:DEG}}` mode, `theta {{key:SIN}} d {{key:×}} m {{key:÷}}` for a $600\text{ lines/mm}$ grating ($d = 1.6667 \times 10^{-6}\text{ m}$) at $\theta = 22.45^\circ$ ($m = 1$) determines $\lambda =$ **`6.365 × 10⁻⁷`** $\text{m}$ ($636.5\text{ nm}$).

---

**Equation E.44 — Numerical Aperture of Optical Fiber:**
$$NA = \sqrt{n_{\text{core}}^2 - n_{\text{clad}}^2}$$
With core and cladding refractive indices $n_{\text{core}}, n_{\text{clad}}$.
Defines the acceptance cone half-angle ($\sin\theta_{\max} = NA$) within which incident rays stay below the critical angle at the core-cladding boundary for lossless total internal reflection.  
Executing `ncore {{key:x²}} nclad {{key:x²}} {{key:-}} {{key:√x}}` for $n_{\text{core}} = 1.482$ and $n_{\text{clad}} = 1.450$ yields **`0.3063`** ($\theta_{\max} = 17.84^\circ$).

---

### Section 6: Nuclear, Atomic & Relativistic Physics

Equations E.45–E.51 link relativistic mass-energy and Lorentz time dilation with quantum photon energy, de Broglie matter waves, and radioactive decay.

**Equation E.45 — Einstein Mass-Energy Equivalence:**
$$E = m c^2$$
With rest mass $m$ ($\text{kg}$) and vacuum speed of light $c = 299,792,458\text{ m/s}$.
Minkowski four-momentum invariant at zero velocity: even a minute nuclear mass defect $\Delta m$ liberates $\Delta m \cdot c^2 \approx 9 \times 10^{16}\text{ J/kg}$ of binding energy.  
Keying `299792458 {{key:x²}} m {{key:×}}` for $m = 1.0 \times 10^{-3}\text{ kg}$ ($1\text{ gram}$) returns **`8.98755 × 10¹³`** $\text{J}$ ($89.88\text{ TJ}$).

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `299792458 {{key:x²}}` | 0.00 | 0.00 | 0.00 | 8.9876E16 | Square speed of light $c^2 = 8.98755 \times 10^{16}\text{ m}^2/\text{s}^2$ |
| `1 {{key:E}} 3 {{key:+/-}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 8.9876E13 | Rest-mass energy $E = mc^2 = 8.98755 \times 10^{13}\text{ J}$ |

---

**Equation E.46 — Planck-Einstein Photon Energy:**
$$E_{\text{photon}} = \frac{h c}{\lambda}$$
With Planck constant $h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}$, $c = 299,792,458\text{ m/s}$, and wavelength $\lambda$ ($\text{m}$).
Quantization of the electromagnetic field ($E = h\nu = hc/\lambda$): shorter wavelengths pack proportionally higher energy per quantum, governing photoelectric emission and semiconductor bandgaps.  
Evaluating `6.62607015 {{key:E}} 34 {{key:+/-}} {{key:ENTER}} 299792458 {{key:×}} lambda {{key:÷}}` for a green photon ($\lambda = 500.0 \times 10^{-9}\text{ m}$) yields **`3.9729 × 10⁻¹⁹`** $\text{J}$ ($2.48\text{ eV}$).

---

**Equation E.47 — de Broglie Particle Wavelength:**
$$\lambda = \frac{h}{m v}$$
With Planck constant $h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}$, particle mass $m$ ($\text{kg}$), and speed $v$ ($\text{m/s}$).
Wave-particle duality extended to matter: a beam of electrons accelerated to high momentum $p = mv$ exhibits picometer-scale wavelengths, enabling atomic-resolution transmission electron microscopy.  
On the stack, `6.62607015 {{key:E}} 34 {{key:+/-}} {{key:ENTER}} m {{key:÷}} v {{key:÷}}` for an electron ($m = 9.1093837 \times 10^{-31}\text{ kg}$) at $v = 2.0 \times 10^6\text{ m/s}$ gives **`3.6370 × 10⁻¹⁰`** $\text{m}$ ($0.3637\text{ nm}$).

---

**Equation E.48 — Relativistic Lorentz Factor ($\gamma$):**
$$\gamma = \frac{1}{\sqrt{1 - \beta^2}} = \frac{1}{\sqrt{1 - (v/c)^2}}$$
With normalized velocity $\beta = v / c$.
Hyperbolic rotation factor of special relativity: governs proper-time dilation ($\Delta t = \gamma \Delta\tau$) for cosmic-ray muons and relativistic length contraction ($L = L_0 / \gamma$) as $v \to c$.  
Pressing `beta {{key:x²}} 1 {{key:x⇄y}} {{key:-}} {{key:√x}} {{key:1/x}}` at $\beta = 0.95$ computes $\gamma =$ **`3.20256`**.

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `0.95 {{key:x²}}` | 0.00 | 0.00 | 0.00 | 0.902500 | Square normalized velocity $\beta^2 = 0.902500$ |
| `1 {{key:x⇄y}} {{key:-}}` | 0.00 | 0.00 | 0.00 | 0.097500 | Complement $1 - \beta^2 = 0.097500$ |
| `{{key:√x}} {{key:1/x}}` | 0.00 | 0.00 | 0.00 | 3.202563 | Lorentz time-dilation factor $\gamma = 3.202563$ |

---

**Equation E.49 — Relativistic Momentum:**
$$p = \gamma m v = \frac{m v}{\sqrt{1 - (v/c)^2}}$$
With rest mass $m$ ($\text{kg}$) and velocity $v$ ($\text{m/s}$).
As a particle approaches $c$, applied force increases momentum without bound via $\gamma$ rather than accelerating $v$ past $c$, dictating synchrotron magnet rigidity ($B\rho = p/q$).  
Running `v {{key:ENTER}} 299792458 {{key:÷}} {{key:x²}} 1 {{key:x⇄y}} {{key:-}} {{key:√x}} m {{key:ENTER}} v {{key:×}} {{key:x⇄y}} {{key:÷}}` for a proton ($m = 1.67262 \times 10^{-27}\text{ kg}$) at $v = 0.85 c = 2.548236 \times 10^8\text{ m/s}$ yields **`8.0906 × 10⁻¹⁹`** $\text{kg}\cdot\text{m/s}$.

---

**Equation E.50 — Radioactive Decay Exponential Law:**
$$N(t) = N_0 e^{-\lambda t} = N_0 \left(\frac{1}{2}\right)^{t / t_{1/2}}$$
With initial activity $N_0$, half-life $t_{1/2}$, and elapsed time $t$.
Memoryless Poisson nuclear transmutation ($dN/dt = -\lambda N$): each elapsed half-life $t_{1/2} = \ln(2)/\lambda$ halves the surviving parent isotope population.  
Keying `0.5 {{key:ENTER}} t {{key:ENTER}} thalf {{key:÷}} {{key:yˣ}} N0 {{key:×}}` for a Cobalt-60 source ($N_0 = 10000.0\text{ Bq}, t_{1/2} = 5.27\text{ years}$) after $t = 15.0\text{ years}$ returns **`1388.9`** $\text{Bq}$.

---

**Equation E.51 — Rydberg Equation for Hydrogen Spectral Series:**
$$\frac{1}{\lambda} = R_{\infty} \left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)$$
With Rydberg constant $R_\infty = 1.0973731568 \times 10^7\text{ m}^{-1}$ and principal quantum numbers $n_1 < n_2$.
Bohr-orbital energy differences ($\Delta E \propto 1/n_1^2 - 1/n_2^2$) directly predict the discrete emission lines of atomic hydrogen across the Lyman ($n_1=1$), Balmer ($n_1=2$), and Paschen ($n_1=3$) series.  
Evaluating `n1 {{key:x²}} {{key:1/x}} n2 {{key:x²}} {{key:1/x}} {{key:-}} 1.0973731568 {{key:E}} 7 {{key:×}} {{key:1/x}}` for the Balmer $H_\alpha$ red line ($n_1 = 2, n_2 = 3$) gives **`6.5647 × 10⁻⁷`** $\text{m}$ ($656.47\text{ nm}$).

---

### Section 7: Coordinate Geometry, Mensuration & Solid Geometry

Equations E.52–E.66 provide planar and spherical mensuration formulas for polygons, circular segments, ellipses, parabolic arches, and triangle cevians.

**Equation E.52 — Volume and Surface Area of Sphere:**
$$V = \frac{4}{3} \pi r^3, \quad A = 4 \pi r^2$$
With radius $r$.
Archimedes' proudest theorem (engraved on his tomb): a sphere occupies exactly $\frac{2}{3}$ the volume and $\frac{2}{3}$ the total surface area of its circumscribing cylinder, and $dV/dr = 4\pi r^2 = A$.  
On the stack:
- Volume: `r {{key:ENTER}} 3 {{key:yˣ}} {{key:π}} {{key:×}} 4 {{key:×}} 3 {{key:÷}}`  
- Area: `r {{key:x²}} {{key:π}} {{key:×}} 4 {{key:×}}`
For $r = 7.50\text{ cm}$, these sequences evaluate to Volume = **`1767.146`** $\text{cm}^3$ and Area = **`706.858`** $\text{cm}^2$.
*Stack Trace Table (Volume):*

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `7.5 {{key:ENTER}} 3 {{key:yˣ}}` | 0.00 | 0.00 | 0.00 | 421.8750 | Cube sphere radius $r^3 = 421.8750\text{ cm}^3$ |
| `{{key:π}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 1325.3594 | Scale by $\pi$: $\pi r^3 = 1325.3594\text{ cm}^3$ |
| `4 {{key:×}} 3 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 1767.1459 | Sphere volume $V = \frac{4}{3}\pi r^3 = 1767.1459\text{ cm}^3$ |

---

**Equation E.53 — Right Circular Cone Volume & Lateral Surface Area:**
$$V = \frac{1}{3} \pi r^2 h, \quad A_{\text{lat}} = \pi r \sqrt{r^2 + h^2}$$
With base radius $r$ and perpendicular altitude $h$.
By Cavalieri's principle, a cone occupies $\frac{1}{3}$ of its bounding cylinder ($\pi r^2 h$), while its unrolled lateral sheet forms a circular sector of slant radius $\ell = \sqrt{r^2 + h^2}$.  
On the stack:
- Volume: `r {{key:x²}} h {{key:×}} {{key:π}} {{key:×}} 3 {{key:÷}}`  
- Lateral Area: `r {{key:x²}} h {{key:x²}} {{key:+}} {{key:√x}} r {{key:×}} {{key:π}} {{key:×}}`
For $r = 6.0\text{ cm}$ and $h = 14.0\text{ cm}$, these return Volume = **`527.788`** $\text{cm}^3$ and Lateral Area = **`287.015`** $\text{cm}^2$.

---

**Equation E.54 — Frustum of Right Circular Cone Volume:**
$$V = \frac{1}{3} \pi h (R^2 + R r + r^2)$$
With lower base radius $R$, upper base radius $r$, and height $h$.
Circular counterpart to the Moscow Papyrus pyramidal frustum (Chapter 6): averages the bottom disk $\pi R^2$, top disk $\pi r^2$, and their geometric mean $\pi Rr$ across altitude $h$.  
Keying `R {{key:x²}} R {{key:ENTER}} r {{key:×}} {{key:+}} r {{key:x²}} {{key:+}} h {{key:×}} 3 {{key:÷}} {{key:π}} {{key:×}}` for $R = 8.0\text{ cm}, r = 3.0\text{ cm}, h = 12.0\text{ cm}$ yields **`1218.938`** $\text{cm}^3$.

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `8 {{key:x²}}` | 0.00 | 0.00 | 0.00 | 64.0000 | Lower base radius squared $R^2 = 64.0000\text{ cm}^2$ |
| `8 {{key:ENTER}} 3 {{key:×}} {{key:+}}` | 0.00 | 0.00 | 0.00 | 88.0000 | Add cross-product $R^2 + Rr = 88.0000\text{ cm}^2$ |
| `3 {{key:x²}} {{key:+}}` | 0.00 | 0.00 | 0.00 | 97.0000 | Add upper base radius squared $R^2 + Rr + r^2 = 97.0000\text{ cm}^2$ |
| `12 {{key:×}} 3 {{key:÷}} {{key:π}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 1218.9380 | Frustum volume $V = 1218.9380\text{ cm}^3$ |

---

**Equation E.55 — Torus Volume and Total Surface Area:**
$$V = 2 \pi^2 R r^2, \quad A = 4 \pi^2 R r$$
With major centroid radius $R$ and minor tube radius $r$.
Pappus's centroid theorems in action: sweeping a circular cross-section ($\pi r^2$, perimeter $2\pi r$) along a circular orbit of length $2\pi R$ multiplies both measures by $2\pi R$, modeling tokamak plasma chambers and O-ring seals.  
On the stack:
- Volume: `r {{key:x²}} R {{key:×}} 2 {{key:×}} {{key:π}} {{key:x²}} {{key:×}}`  
- Surface Area: `R {{key:ENTER}} r {{key:×}} 4 {{key:×}} {{key:π}} {{key:x²}} {{key:×}}`
For $R = 12.0\text{ cm}$ and $r = 2.5\text{ cm}$, these evaluate to Volume = **`1480.44`** $\text{cm}^3$ and Area = **`1184.35`** $\text{cm}^2$.

---

**Equation E.56 — Heron's Formula for Arbitrary Triangle Area:**
$$A = \sqrt{s(s - a)(s - b)(s - c)}, \quad s = \frac{a + b + c}{2}$$
With triangle side lengths $a, b, c$.
Hero of Alexandria's (*Metrica*, c. 60 CE) intrinsic triangulation formula: computes planar area directly from edge lengths without requiring an altitude or angle measurement.  
Storing semiperimeter $s$ via `a {{key:ENTER}} b {{key:+}} c {{key:+}} 2 {{key:÷}} {{key:STO}} S a {{key:-}} {{key:RCL}} S b {{key:-}} {{key:×}} {{key:RCL}} S c {{key:-}} {{key:×}} {{key:RCL}} S {{key:×}} {{key:√x}}` for the classic $(13, 14, 15)$ Heronian triangle ($s = 21.0$) gives **`84.000`**.

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `13 {{key:ENTER}} 14 {{key:+}} 15 {{key:+}} 2 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 21.0000(s) | Semiperimeter $s = 21.0000$ |
| `{{key:STO}} S 13 {{key:-}}` | 0.00 | 0.00 | 0.00 | 8.0000(s-a) | Store $s$ in `S`; compute $s - a = 8.0000$ |
| `{{key:RCL}} S 14 {{key:-}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 56.0000 | Multiply by $(s - b) = 7.0$: $8 \times 7 = 56.0000$ |
| `{{key:RCL}} S 15 {{key:-}} {{key:×}}` | 0.00 | 0.00 | 0.00 | 336.0000 | Multiply by $(s - c) = 6.0$: $56 \times 6 = 336.0000$ |
| `{{key:RCL}} S {{key:×}} {{key:√x}}` | 0.00 | 0.00 | 0.00 | 84.0000 | Multiply by $s = 21.0$ and take root: Area $A = 84.0000$ |

---

**Equation E.57 — Law of Cosines for Arbitrary Triangle:**
$$c = \sqrt{a^2 + b^2 - 2 a b \cos C}$$
With adjacent sides $a, b$ and included angle $C$ (degrees).
Al-Kashi's oblique generalization of the Pythagorean theorem (Book I, Propositions 12–13 of Euclid's *Elements*): subtracts the vector inner-product projection $2ab\cos C$ to close any SAS triangle.  
In `{{key:DEG}}` mode, `a {{key:x²}} b {{key:x²}} {{key:+}} 2 {{key:ENTER}} a {{key:×}} b {{key:×}} C {{key:COS}} {{key:×}} {{key:-}} {{key:√x}}` for $a = 18.0, b = 25.0, C = 62.0^\circ$ returns **`22.956`**.

---

**Equation E.58 — Great Circle Spherical Distance (Haversine Formula):**
$$d = 2 R \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta\phi}{2}\right) + \cos\phi_1 \cos\phi_2 \sin^2\left(\frac{\Delta\lambda}{2}\right)}\right)$$
With mean Earth radius $R = 6371.0\text{ km}$, latitudes $\phi_1, \phi_2$, and longitudes $\lambda_1, \lambda_2$.
James Inman's (1835) half-versed-sine ("haversine", $\sin^2(\theta/2)$) navigation formula: avoids the catastrophic $\arccos(\approx 1)$ cancellation of the spherical law of cosines at short and antipodal geodesic ranges.  
In `{{key:DEG}}` mode, keying `phi2 {{key:ENTER}} phi1 {{key:-}} 2 {{key:÷}} {{key:SIN}} {{key:x²}} phi1 {{key:COS}} phi2 {{key:COS}} {{key:×}} lam2 {{key:ENTER}} lam1 {{key:-}} 2 {{key:÷}} {{key:SIN}} {{key:x²}} {{key:×}} {{key:+}} {{key:√x}} {{key:ASIN}} 2 {{key:×}} 6371.0 {{key:×}}` from New York ($40.7128^\circ\text{N}, 74.0060^\circ\text{W}$) to London ($51.5074^\circ\text{N}, 0.1278^\circ\text{W}$) yields **`5570.2`** $\text{km}$ ($3461.2\text{ miles}$).

---

**Equation E.59 — Circular Sector Area and Arc Length:**
$$s = r \theta, \quad A = \frac{1}{2} r^2 \theta \quad (\theta\text{ in radians})$$
With parameters Radius $r$, central angle $\theta$.
Direct scaling of circle perimeter ($2\pi r$) and disk area ($\pi r^2$) by aperture fraction $(\theta / 2\pi)$.  
The stack evaluation sequences are:
- Arc Length: `r {{key:ENTER}} theta {{key:×}}`  
- Sector Area: `r {{key:x²}} theta {{key:×}} 2 {{key:÷}}`  
For the benchmark case ($r = 12.0\text{ cm}, \theta = 1.047198\text{ rad}$ ($60.0^\circ$)), this evaluates to Arc Length = **`12.566`** $\text{cm}$; Area = **`75.398`** $\text{cm}^2$.

---

**Equation E.60 — Circular Segment Area:**
$$A = \frac{1}{2} r^2 (\theta - \sin\theta) \quad (\theta\text{ in radians})$$
With parameters Radius $r$, central angle $\theta$.
Area of the circular sector minus the internal triangular chord core ($\frac{1}{2} r^2 \sin\theta$). Essential in hydraulic pipe fill levels and pressure vessel liquid volumes.  
On the stack (in `RAD` Mode), key in `theta {{key:ENTER}} {{key:SIN}} {{key:-}} r {{key:x²}} {{key:×}} 2 {{key:÷}}`.
For the benchmark case ($r = 8.0\text{ m}, \theta = 1.250\text{ rad}$), this evaluates to **`9.633`** $\text{m}^2$.

---

**Equation E.61 — Circular Annulus & Annular Sector Area:**
$$A = \pi (R^2 - r^2) = \pi (R - r)(R + r), \quad A_{\text{sector}} = \frac{\theta}{2} (R - r)(R + r)$$
With parameters Outer radius $R$, inner bore radius $r$, central angle $\theta$ (radians).
Difference between concentric disks. Evaluated in RPN via difference-of-squares factorization to preserve precision for thin-walled gaskets ($R \approx r$).  
On the stack, key in `R {{key:ENTER}} r {{key:-}} R {{key:ENTER}} r {{key:+}} {{key:×}} {{key:π}} {{key:×}}`.
For the benchmark case ($R = 15.0\text{ cm}, r = 10.0\text{ cm}$), this evaluates to **`392.699`** $\text{cm}^2$.

---

**Equation E.62 — Ellipse Area & Ramanujan's Second Perimeter Approximation:**
$$A = \pi a b, \quad h = \frac{(a - b)^2}{(a + b)^2}, \quad P \approx \pi (a + b) \left[ 1 + \frac{3h}{10 + \sqrt{4 - 3h}} \right]$$
With parameters Semimajor axis $a$, semiminor axis $b$.
2D affine dilation of the unit circle. Ramanujan's second formula approximates the complete elliptic integral with sub-ppm accuracy.  
The stack evaluation sequences are:
- Area: `a {{key:ENTER}} b {{key:×}} {{key:π}} {{key:×}}`  
- Perimeter: `a {{key:ENTER}} b {{key:-}} a {{key:ENTER}} b {{key:+}} {{key:÷}} {{key:x²}} {{key:STO}} A 3 {{key:×}} 4 {{key:x⇄y}} {{key:-}} {{key:√x}} 10 {{key:+}} {{key:1/x}} 3 {{key:×}} {{key:RCL}} A {{key:×}} 1 {{key:+}} a {{key:ENTER}} b {{key:+}} {{key:×}} {{key:π}} {{key:×}}`  
For the benchmark case ($a = 10.0\text{ cm}, b = 6.0\text{ cm}$), this evaluates to Area = **`188.496`** $\text{cm}^2$; Perimeter = **`51.054`** $\text{cm}$.

---

**Equation E.63 — Parabolic Segment Area (Archimedes' Quadrature):**
$$A = \frac{2}{3} b h$$
With parameters Base chord width $b$, perpendicular vertex altitude $h$.
Archimedes' mechanical quadrature: the area under a parabolic arch is exactly $\frac{4}{3}$ of the inscribed triangle ($\frac{1}{2}bh$). Fundamental for beam bending moment diagrams and solar trough reflectors.  
On the stack, key in `b {{key:ENTER}} h {{key:×}} 2 {{key:×}} 3 {{key:÷}}`.
For the benchmark case ($b = 18.0\text{ m}, h = 6.0\text{ m}$), this evaluates to **`72.000`** $\text{m}^2$.

---

**Equation E.64 — Regular $n$-gon Area, Inradius & Circumradius:**
$$A = \frac{1}{4} n s^2 \cot\left(\frac{\pi}{n}\right), \quad r = \frac{s}{2 \tan(\pi/n)}, \quad R = \frac{s}{2 \sin(\pi/n)}$$
With parameters Number of sides $n$, side length $s$.
Symmetric decomposition into $n$ central isosceles triangles. Dictates bolt head profiles, polygonal extrusions, and crystal lattices.  
On the stack (Area), key in `{{key:π}} n {{key:÷}} {{key:TAN}} {{key:1/x}} s {{key:x²}} {{key:×}} n {{key:×}} 4 {{key:÷}}`.
For the benchmark case (Regular Hexagon ($n = 6$), side $s = 5.0\text{ cm}$), this evaluates to **`64.952`** $\text{cm}^2$.

---

**Equation E.65 — Brahmagupta's Formula & Ptolemy's Theorem for Cyclic Quadrilaterals:**
$$A = \sqrt{(s-a)(s-b)(s-c)(s-d)}, \quad s = \frac{a+b+c+d}{2}, \quad a c + b d = e f$$
With parameters Sides $a, b, c, d$, diagonals $e, f$.
4-sided cyclic generalization of Heron's formula. Yields maximum enclosure area for any quadrilateral with fixed side lengths.  
On the stack, key in `a {{key:ENTER}} b {{key:+}} c {{key:+}} d {{key:+}} 2 {{key:÷}} {{key:STO}} S a {{key:-}} {{key:RCL}} S b {{key:-}} {{key:×}} {{key:RCL}} S c {{key:-}} {{key:×}} {{key:RCL}} S d {{key:-}} {{key:×}} {{key:√x}}`.
For the benchmark case ($a = 3.0, b = 4.0, c = 5.0, d = 6.0$ ($s = 9.0$)), this evaluates to **`18.974`**.

---

**Equation E.66 — Stewart's Theorem for Triangle Cevians:**
$$m a n + d^2 a = b^2 m + c^2 n \implies d = \sqrt{\frac{b^2 m + c^2 n - m a n}{a}}$$
With parameters Triangle sides $a, b, c$; cevian of length $d$ dividing side $a$ into segments $m$ and $n$ ($m + n = a$).
Rotational moment of inertia balance across a triangular plate; resolves medians, angle bisectors, and structural truss struts.  
On the stack, key in `b {{key:x²}} m {{key:×}} c {{key:x²}} n {{key:×}} {{key:+}} m {{key:ENTER}} a {{key:×}} n {{key:×}} {{key:-}} a {{key:÷}} {{key:√x}}`.
For the benchmark case ($a = 10.0, b = 8.0, c = 6.0$ (right triangle), median to hypotenuse ($m = 5.0, n = 5.0$)), this evaluates to **`5.000`**.

---

### Section 8: 3D Solid Geometry & Mensuration Master Compendium

Equations E.67–E.72 evaluate volumes and surface areas of spherical domes, pyramidal frustums, ellipsoids, paraboloids, and general prismoids.

**Equation E.67 — Spherical Cap (Dome) & Spherical Zone Volume:**
$$V_{\text{cap}} = \frac{1}{3} \pi h^2 (3 R - h), \quad A_{\text{dome}} = 2 \pi R h$$
$$V_{\text{zone}} = \frac{\pi h}{6} (3 r_1^2 + 3 r_2^2 + h^2)$$
With parameters Sphere radius $R$, cap height $h$, zone radii $r_1, r_2$.
Disk integration of spherical layers via Archimedes' cylinder balance. Essential for liquid propellant tanks, geodesic domes, and acoustic lenses.  
On the stack (Cap Volume), key in `3 {{key:ENTER}} R {{key:×}} h {{key:-}} h {{key:x²}} {{key:×}} {{key:π}} {{key:×}} 3 {{key:÷}}`.
For the benchmark case (Sphere $R = 10.0\text{ cm}$, cap height $h = 3.0\text{ cm}$), this evaluates to Volume = **`254.469`** $\text{cm}^3$; Dome Area = **`188.496`** $\text{cm}^2$.

---

**Equation E.68 — Frustum of Regular Pyramid Volume:**
$$V = \frac{h}{3} (A_1 + A_2 + \sqrt{A_1 A_2})$$
With parameters Lower base area $A_1$, upper base area $A_2$, perpendicular height $h$.
Heronian mean of cross-sectional areas; models architectural monuments, concrete foundations, and hopper bins.  
On the stack, key in `A1 {{key:ENTER}} A2 {{key:×}} {{key:√x}} A1 {{key:+}} A2 {{key:+}} h {{key:×}} 3 {{key:÷}}`.
For the benchmark case ($A_1 = 36.0\text{ m}^2, A_2 = 16.0\text{ m}^2, h = 9.0\text{ m}$), this evaluates to **`228.000`** $\text{m}^3$.

---

**Equation E.69 — Ellipsoid Volume:**
$$V = \frac{4}{3} \pi a b c$$
With parameters Semimajor axes $a, b, c$.
3D affine dilation of the unit sphere. Models oblate and prolate planetary bodies, optical ellipsoidal reflectors, and aerodynamic radomes.  
On the stack, key in `a {{key:ENTER}} b {{key:×}} c {{key:×}} {{key:π}} {{key:×}} 4 {{key:×}} 3 {{key:÷}}`.
For the benchmark case ($a = 6.0\text{ cm}, b = 4.0\text{ cm}, c = 3.0\text{ cm}$), this evaluates to **`301.593`** $\text{cm}^3$.

---

**Equation E.70 — Paraboloid of Revolution Volume:**
$$V = \frac{1}{2} \pi r^2 h$$
With parameters Base radius $r$, central depth $h$.
Archimedes' law of paraboloids: volume is exactly half of the bounding cylinder. Primary profile for radar dishes, headlamp reflectors, and liquid mirror telescopes.  
On the stack, key in `r {{key:x²}} h {{key:×}} {{key:π}} {{key:×}} 2 {{key:÷}}`.
For the benchmark case ($r = 4.0\text{ m}, h = 3.0\text{ m}$), this evaluates to **`75.398`** $\text{m}^3$.

---

**Equation E.71 — Cylindrical Ungula (Hoof) Volume:**
$$V = \frac{2}{3} r^3 \tan\alpha$$
With parameters Cylinder radius $r$, cutting plane angle $\alpha$ passing through base diameter.
Slicing a circular cylinder with an inclined plane passing directly through its base diameter. Models mitered pipe junctions and fluid flow deflectors.  
On the stack (in `DEG` Mode), key in `r {{key:ENTER}} 3 {{key:yˣ}} alpha {{key:TAN}} {{key:×}} 2 {{key:×}} 3 {{key:÷}}`.
For the benchmark case ($r = 6.0\text{ cm}, \alpha = 45.0^\circ$), this evaluates to **`144.000`** $\text{cm}^3$.

---

**Equation E.72 — Universal Prismoidal Formula (Simpson's 3D Rule):**
$$V = \frac{h}{6} (A_{\text{top}} + 4 A_{\text{mid}} + A_{\text{bot}})$$
With parameters Extrusion height $h$, top area $A_{\text{top}}$, mid-height area $A_{\text{mid}}$, base area $A_{\text{bot}}$.
Simpson's cubic quadrature along height: exact for any solid whose cross-sectional area varies as a quadratic or cubic polynomial in $z$ (prisms, pyramids, cones, spheres, paraboloids).  
On the stack, key in `Amid {{key:ENTER}} 4 {{key:×}} Atop {{key:+}} Abot {{key:+}} h {{key:×}} 6 {{key:÷}}`.
For the benchmark case (Frustum with $A_{\text{top}} = 16.0, A_{\text{mid}} = 36.0, A_{\text{bot}} = 64.0, h = 6.0$), this evaluates to **`224.000`**.

---

### Section 9: Financial Mathematics, Amortization & Time Value of Money

Equations E.73–E.77 summarize closed-form compound-interest recipes for ordinary annuities, loan amortization payments, sinking funds, and perpetuities.

**Equation E.73 — Present Value of an Ordinary Annuity:**
$$PV = PMT \left[ \frac{1 - (1 + i)^{-N}}{i} \right]$$
With parameters Periodic payment $PMT$, rate per period $i$, total periods $N$.
Sum of discounted future cash flow geometric series. Determines loan balances, actuarial pension reserves, and bond valuation.  
On the stack, key in `1 {{key:ENTER}} i {{key:+}} N {{key:+/-}} {{key:yˣ}} 1 {{key:x⇄y}} {{key:-}} i {{key:÷}} PMT {{key:×}}`.
For the benchmark case ($PMT = 500\text{ USD}, i = 0.005$ ($6\%$ APR monthly), $N = 36\text{ months}$), this evaluates to **`16,429.62`** $\text{USD}$.

---

**Equation E.74 — Future Value of an Ordinary Annuity:**
$$FV = PMT \left[ \frac{(1 + i)^N - 1}{i} \right]$$
With parameters Periodic savings deposit $PMT$, rate per period $i$, total periods $N$.
Compound growth accumulation of periodic deposits. Solves retirement nest-egg and university savings goals.  
On the stack, key in `1 {{key:ENTER}} i {{key:+}} N {{key:yˣ}} 1 {{key:-}} i {{key:÷}} PMT {{key:×}}`.
For the benchmark case ($PMT = 250\text{ USD}, i = 0.006$ ($7.2\%$ APR monthly), $N = 60\text{ months}$), this evaluates to **`17,984.66`** $\text{USD}$.

---

**Equation E.75 — Loan Amortization Periodic Payment:**
$$PMT = PV \left[ \frac{i}{1 - (1 + i)^{-N}} \right]$$
With parameters Principal loan amount $PV$, interest rate per period $i$, total payment periods $N$.
Capital recovery factor: inverts annuity PV to find fixed monthly installment liquidating principal and interest.  
On the stack, key in `1 {{key:ENTER}} i {{key:+}} N {{key:+/-}} {{key:yˣ}} 1 {{key:x⇄y}} {{key:-}} i {{key:x⇄y}} {{key:÷}} PV {{key:×}}`.
For the benchmark case ($PV = 25,000\text{ USD}, i = 0.0045$ ($5.4\%$ APR monthly), $N = 48\text{ months}$), this evaluates to **`579.98`** $\text{USD}$.

---

**Equation E.76 — Sinking Fund Periodic Savings Payment:**
$$PMT = FV \left[ \frac{i}{(1 + i)^N - 1} \right]$$
With parameters Target future balance $FV$, interest rate per period $i$, total saving periods $N$.
Periodic contribution required to accumulate a predetermined future balloon payment or capital equipment replacement fund.  
On the stack, key in `1 {{key:ENTER}} i {{key:+}} N {{key:yˣ}} 1 {{key:-}} i {{key:x⇄y}} {{key:÷}} FV {{key:×}}`.
For the benchmark case (Target $FV = 50,000\text{ USD}, i = 0.005$ ($6\%$ APR monthly), $N = 120\text{ months}$), this evaluates to **`305.10`** $\text{USD}$.

---

**Equation E.77 — Flat & Growing Perpetuities:**
$$PV_{\text{flat}} = \frac{PMT}{i}, \quad PV_{\text{growing}} = \frac{PMT}{i - g}$$
With parameters Annual dividend payment $PMT$, discount rate $i$, constant dividend growth rate $g$ ($i > g$).
Gordon growth model; sum of infinite geometric cash flow series with continuous compounding. Dictates preferred stock and endowment valuations.  
The stack evaluation sequences are:
- Flat: `PMT {{key:ENTER}} i {{key:÷}}`  
- Growing: `PMT {{key:ENTER}} i {{key:ENTER}} g {{key:-}} {{key:÷}}`  
For the benchmark case ($PMT = 1,200\text{ USD/yr}, i = 0.06, g = 0.02$), this evaluates to Flat Perpetuity = **`20,000.00`** $\text{USD}$; Growing Perpetuity = **`30,000.00`** $\text{USD}$.

---

### Section 10: Chemistry, Electrochemistry, Chemical Kinetics & Biochemistry

Equations E.78–E.85 cover aqueous acid-base equilibria, Nernst electrochemical potentials, Arrhenius and Michaelis-Menten kinetics, and spectrophotometric absorbance.

**Equation E.78 — pH & Hydronium Ion Activity:**
$$\text{pH} = -\log_{10}[\text{H}_3\text{O}^+], \quad [\text{H}_3\text{O}^+] = 10^{-\text{pH}}$$
With parameters $[\text{H}_3\text{O}^+]$ (molar hydronium ion concentration, $\text{mol/L}$).
Sørensen logarithmic acidity scale compressing 14 orders of magnitude of aqueous proton activity into a linear 0–14 bench index.  
On the stack, key in `H3O {{key:LOG}} {{key:+/-}}` (Inverse: `pH {{key:+/-}} {{key:10ˣ}}`).
For the benchmark case ($[\text{H}_3\text{O}^+] = 3.50 \times 10^{-5}\text{ mol/L}$ (`3.5 {{key:E}} 5 {{key:+/-}} {{key:LOG}} {{key:+/-}}`)), this evaluates to **`4.4559`**.

---

**Equation E.79 — Henderson–Hasselbalch Buffer Equilibrium:**
$$\text{pH} = \text{p}K_a + \log_{10}\left(\frac{[\text{A}^-]}{[\text{HA}]}\right)$$
With parameters $\text{p}K_a = -\log_{10} K_a$ (acid dissociation constant), $[\text{A}^-]$ (conjugate base molarity), $[\text{HA}]$ (weak acid molarity).
Governs blood bicarbonate homeostasis ($\text{pH } 7.40$) and analytical laboratory buffer capacity against strong acid/base perturbations.  
On the stack, key in `[A⁻] {{key:ENTER}} [HA] {{key:÷}} {{key:LOG}} pKa {{key:+}}`.
For the benchmark case (Acetate buffer with $\text{p}K_a = 4.76, [\text{A}^-] = 0.25\text{ M}, [\text{HA}] = 0.15\text{ M}$), this evaluates to **`4.9818`**.

---

**Equation E.80 — Nernst Electrochemical Cell Potential:**
$$E_{\text{cell}} = E^\circ_{\text{cell}} - \frac{R T}{n F} \ln Q$$
With parameters $E^\circ_{\text{cell}}$ (standard cell potential, $\text{V}$), $R = 8.31446\text{ J/(mol}\cdot\text{K)}$, $T$ (temperature, $\text{K}$), $n$ (moles of electrons transferred), $F = 96,485.3\text{ C/mol}$, $Q$ (reaction quotient).
Links Gibbs free energy driving force ($\Delta G = -n F E_{\text{cell}}$) to real-time reactant/product activity ratios in galvanic batteries and biological ion channels.  
On the stack, key in `8.31446 {{key:ENTER}} T {{key:×}} n {{key:÷}} 96485.3 {{key:÷}} Q {{key:LN}} {{key:×}} E0 {{key:x⇄y}} {{key:-}}`.
For the benchmark case (Daniell $\text{Zn/Cu}$ cell: $E^\circ = 1.100\text{ V}, T = 298.15\text{ K}, n = 2, Q = 0.050$), this evaluates to **`1.1385`** $\text{V}$.

---

**Equation E.81 — Arrhenius Chemical Reaction Rate Constant:**
$$k = A \exp\left(-\frac{E_a}{R T}\right)$$
With parameters $A$ (pre-exponential collision frequency factor, $\text{s}^{-1}$), $E_a$ (activation energy barrier, $\text{J/mol}$), $R = 8.31446\text{ J/(mol}\cdot\text{K)}$, $T$ (absolute temperature, $\text{K}$).
Boltzmann thermal fraction of molecular collisions possessing sufficient kinetic energy to surmount the transition-state activation barrier.  
On the stack, key in `Ea {{key:ENTER}} 8.31446 {{key:÷}} T {{key:÷}} {{key:+/-}} {{key:eˣ}} A {{key:×}}`.
For the benchmark case ($A = 1.25 \times 10^{11}\text{ s}^{-1}, E_a = 75,000\text{ J/mol}, T = 350.0\text{ K}$), this evaluates to **`0.7937`** $\text{s}^{-1}$.

---

**Equation E.82 — Michaelis–Menten Enzyme Saturation Kinetics:**
$$v_0 = \frac{V_{\max}[S]}{K_m + [S]}$$
With parameters $V_{\max}$ (maximum turnover velocity), $[S]$ (substrate concentration), $K_m$ (Michaelis constant: substrate concentration at $0.5\,V_{\max}$).
Hyperbolic saturation of catalytic active sites; transitions from first-order kinetics ($v_0 \approx \frac{V_{\max}}{K_m}[S]$) at low $[S]$ to zero-order saturation ($v_0 \to V_{\max}$) at high $[S]$.  
On the stack, key in `Vmax {{key:ENTER}} S {{key:×}} Km {{key:ENTER}} S {{key:+}} {{key:÷}}`.
For the benchmark case ($V_{\max} = 140.0\text{ }\mu\text{M/min}, [S] = 15.0\text{ mM}, K_m = 5.0\text{ mM}$), this evaluates to **`105.0000`** $\mu\text{M/min}$.

---

**Equation E.83 — Beer–Lambert Spectrophotometric Absorbance:**
$$A = \varepsilon \ell c = -\log_{10}\left(\frac{I}{I_0}\right)$$
With parameters $\varepsilon$ (molar absorptivity, $\text{L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}$), $\ell$ (optical cuvette path length, $\text{cm}$), $c$ (molar concentration, $\text{mol/L}$), $I/I_0$ (transmittance $T$).
Differential photon attenuation through an absorbing solution; fundamental calibration equation for UV-Vis spectrophotometry and pulse oximetry.  
On the stack, key in `eps {{key:ENTER}} l {{key:×}} c {{key:×}}` (Transmittance $T = I/I_0$: `A {{key:+/-}} {{key:10ˣ}}`).
For the benchmark case (NADH assay at $340\text{ nm}$: $\varepsilon = 6,220\text{ L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}, \ell = 1.00\text{ cm}, c = 8.50 \times 10^{-5}\text{ M}$), this evaluates to $A =$ **`0.5287`** ($T = 29.60\%$).

---

**Equation E.84 — Clausius–Clapeyron Vapor Pressure Scaling:**
$$P_2 = P_1 \exp\left[\frac{\Delta H_{\text{vap}}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right]$$
With parameters $P_1, P_2$ (saturation vapor pressures), $\Delta H_{\text{vap}}$ (molar enthalpy of vaporization, $\text{J/mol}$), $R = 8.31446\text{ J/(mol}\cdot\text{K)}$, $T_1, T_2$ (absolute temperatures, $\text{K}$).
Governs phase-boundary equilibrium slope ($dP/dT = \Delta H / (T \Delta V)$) for vacuum distillation, autoclave sterilization, and atmospheric meteorology.  
On the stack, key in `T1 {{key:1/x}} T2 {{key:1/x}} {{key:-}} dH {{key:×}} 8.31446 {{key:÷}} {{key:eˣ}} P1 {{key:×}}`.
For the benchmark case (Water: $P_1 = 23.76\text{ Torr}$ at $T_1 = 298.15\text{ K}$, find $P_2$ at $T_2 = 323.15\text{ K}$ ($\Delta H_{\text{vap}} = 43,990\text{ J/mol}$)), this evaluates to **`93.7330`** $\text{Torr}$.

---

**Equation E.85 — Debye–Hückel Solution Ionic Strength:**
$$I = \frac{1}{2}\sum_{i=1}^n c_i z_i^2$$
With parameters $c_i$ (molar concentration of ion species $i$, $\text{mol/L}$), $z_i$ (integer charge valency of ion $i$).
Measures total electrostatic shielding density in electrolyte solutions; multivalent ions ($z_i = \pm 2, \pm 3$) weight quadratically via `{{key:x²}}`.  
On the stack, key in `z1 {{key:x²}} c1 {{key:×}} z2 {{key:x²}} c2 {{key:×}} {{key:+}} 2 {{key:÷}}`.
For the benchmark case ($0.10\text{ M }\text{MgCl}_2$ solution ($c_{\text{Mg}^{2+}} = 0.10\text{ M}, z_1 = +2$; $c_{\text{Cl}^-} = 0.20\text{ M}, z_2 = -1$)), this evaluates to **`0.3000`** $\text{mol/L}$.

---

### Section 11: Probability, Statistics, Quality Control & Information Theory

Equations E.86–E.93 address discrete probability distributions, Gaussian confidence intervals, Bayesian inference, Six Sigma capability indices, and Shannon channel capacity.

**Equation E.86 — Binomial Probability Mass Function:**
$$P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}$$
With parameters $n$ (independent Bernoulli trials), $k$ (exact number of successes), $p$ (single-trial success probability).
Exact discrete probability of observing $k$ successes in $n$ trials using the `PROB` menu `{{key:Cn,r}}` combinatorics softkey.  
On the stack, key in `n {{key:ENTER}} k {{key:Cn,r}} p {{key:ENTER}} k {{key:yˣ}} {{key:×}} 1 {{key:ENTER}} p {{key:-}} n {{key:ENTER}} k {{key:-}} {{key:yˣ}} {{key:×}}`.
For the benchmark case ($n = 10\text{ wafer dies}, k = 3\text{ defects}, p = 0.25$), this evaluates to **`0.2503`** ($25.0282\%$).

---

**Equation E.87 — Poisson Rare-Event Arrival Probability:**
$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$
With parameters $\lambda$ (mean arrival rate per interval), $k$ (observed event count in interval).
Limiting law of rare independent events: radioactive Geiger-counter clicks, optical shot noise photons, and packet switch arrivals.  
On the stack, key in `lam {{key:ENTER}} k {{key:yˣ}} lam {{key:+/-}} {{key:eˣ}} {{key:×}} k {{key:x!}} {{key:÷}}`.
For the benchmark case ($\lambda = 4.2\text{ photons/ms}, k = 3\text{ photons}$), this evaluates to **`0.1852`** ($18.5165\%$).

---

**Equation E.88 — Gaussian Standard $z$-Score & Confidence Interval Half-Width:**
$$z = \frac{x - \mu}{\sigma}, \quad E = z_{\alpha/2}\frac{s}{\sqrt{n}}$$
With parameters $x$ (observation), $\mu$ (population mean), $\sigma$ (standard deviation), $s$ (sample SD from `{{key:sx}}`), $n$ (sample size), $z_{\alpha/2}$ ($1.9600$ for $95\%$ CI; $2.5758$ for $99\%$ CI).
Normalizes measurements into dimensionless standard deviation units and bounds the sampling error of the sample mean $\bar{x} \pm E$.  
The stack evaluation sequences are:
- $z$-Score: `x {{key:ENTER}} mu {{key:-}} sigma {{key:÷}}`  
- $95\%$ CI Margin $E$: `s {{key:ENTER}} n {{key:√x}} {{key:÷}} 1.96 {{key:×}}`  
For the benchmark case ($s = 8.40\text{ MPa}, n = 49\text{ tensile specimens}, z_{\alpha/2} = 1.96$), this evaluates to Margin of Error $E =$ **`2.3520`** $\text{MPa}$.

---

**Equation E.89 — Bayes' Theorem Diagnostic Posterior Probability:**
$$P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B \mid A)P(A) + P(B \mid A')P(A')}$$
With parameters $P(A)$ (prior prevalence), $P(B \mid A)$ (true-positive sensitivity), $P(B \mid A')$ (false-positive rate), $P(A') = 1 - P(A)$.
Updates prior belief with conditional likelihood evidence; critical in medical diagnostics, radar target classification, and spam filtering.  
On the stack, key in `PBA {{key:ENTER}} PA {{key:×}} {{key:ENTER}} PBnotA {{key:ENTER}} PnotA {{key:×}} {{key:+}} {{key:÷}}`.
For the benchmark case ($P(A) = 0.01$ prevalence, sensitivity $P(B \mid A) = 0.99$, false-positive rate $P(B \mid A') = 0.05$ ($P(A') = 0.99$)), this evaluates to **`0.1667`** ($16.67\%$ posterior probability).

---

**Equation E.90 — Six Sigma Process Capability Index ($C_{pk}$):**
$$C_{pk} = \min\left(\frac{\text{USL} - \bar{x}}{3s},\; \frac{\bar{x} - \text{LSL}}{3s}\right)$$
With parameters $\text{USL}, \text{LSL}$ (upper/lower engineering specification limits), $\bar{x}$ (process mean via `{{key:x̄}}`), $s$ (process standard deviation via `{{key:sx}}`).
Measures how many $3\sigma$ half-widths fit between the shifted process center $\bar{x}$ and the nearest tolerance wall ($C_{pk} \ge 1.33$ required for $4\sigma$ manufacturing).  
On the stack (Upper side), key in `USL {{key:ENTER}} xbar {{key:-}} 3 {{key:÷}} s {{key:÷}}`.
For the benchmark case (CNC shaft diameter: $\text{USL} = 10.050\text{ mm}, \text{LSL} = 9.950\text{ mm}, \bar{x} = 10.010\text{ mm}, s = 0.010\text{ mm}$), this evaluates to **`1.3333`**.

---

**Equation E.91 — Shannon Information Entropy (Base-2 Bits):**
$$H(X) = -\sum_{i=1}^m p_i \log_2 p_i = -\frac{1}{\ln 2}\sum_{i=1}^m p_i \ln p_i$$
With parameters $p_i$ (symbol probability distribution with $\sum p_i = 1$).
Fundamental theoretical lower bound on average lossless compression bits per symbol across a noisy or noiseless communication source.  
On the stack (Binary source $p, 1-p$), key in `p {{key:ENTER}} {{key:LN}} {{key:×}} 1 {{key:ENTER}} p {{key:-}} {{key:ENTER}} {{key:LN}} {{key:×}} {{key:+}} 2 {{key:LN}} {{key:÷}} {{key:+/-}}`.
For the benchmark case (Biased binary telemetry source with $p_1 = 0.75, p_2 = 0.25$), this evaluates to **`0.8113`** $\text{bits/symbol}$.

---

**Equation E.92 — Shannon–Hartley Channel Capacity Law:**
$$C = B \log_2\left(1 + \frac{S}{N}\right) = \frac{B \ln(1 + S/N)}{\ln 2}$$
With parameters $B$ (channel bandwidth, $\text{Hz}$), $S/N$ (linear signal-to-noise power ratio; from $\text{SNR}_{\text{dB}}$ via `SNR_dB 10 {{key:÷}} {{key:10ˣ}}`).
Maximum error-free information bit rate transmissible over an additive white Gaussian noise (AWGN) radio or optical channel.  
On the stack, key in `SNR {{key:ENTER}} 1 {{key:+}} {{key:LN}} 2 {{key:LN}} {{key:÷}} B {{key:×}}`.
For the benchmark case ($B = 20.0\text{ MHz}$ Wi-Fi channel with linear $S/N = 31.0$ ($14.91\text{ dB}$)), this evaluates to **`100.0000`** $\text{Mbps}$.

---

**Equation E.93 — M/M/1 Queueing Utilization, Queue Length & Latency:**
$$\rho = \frac{\lambda}{\mu}, \quad L = \frac{\lambda}{\mu - \lambda}, \quad W = \frac{1}{\mu - \lambda}$$
With parameters $\lambda$ (mean Poisson arrival rate, $\text{req/s}$), $\mu$ (mean exponential service rate, $\text{req/s}$, with $\mu > \lambda$).
Little's Law ($L = \lambda W$) and Markovian birth-death steady state for CPU packet schedulers, database connection pools, and toll plazas.  
On the stack (Mean system occupancy $L$), key in `lam {{key:ENTER}} mu {{key:ENTER}} lam {{key:-}} {{key:÷}}` (Mean latency $W$: `mu {{key:ENTER}} lam {{key:-}} {{key:1/x}}`).
For the benchmark case ($\lambda = 45.0\text{ req/s}, \mu = 60.0\text{ req/s}$), this evaluates to $L =$ **`3.0000`** $\text{requests}$; $W =$ **`0.0667`** $\text{s}$ ($66.7\text{ ms}$).

---

### Section 12: Structural Mechanics, Semiconductor Electronics, RF & Computer Engineering

Equations E.94–E.100 span shaft torsion, structural beam deflection, axial Hookean strain, semiconductor diode junctions, op-amp feedback, RF path loss, and parallel computing speedup.

**Equation E.94 — Cylindrical Shaft Torsional Shear Stress & Angle of Twist:**
$$\tau_{\max} = \frac{T r}{J}, \qquad \theta = \frac{T L}{G J}, \qquad J = \frac{\pi r^4}{2}$$
With parameters $T = 450\text{ N}\cdot\text{m}$ (applied torque), $r = 0.025\text{ m}$ (shaft radius), $L = 1.20\text{ m}$ (length), $G = 79.3\times 10^9\text{ Pa}$ (shear modulus of steel), and polar moment of inertia $J = \frac{\pi (0.025)^4}{2} = 6.1359\times 10^{-7}\text{ m}^4$: on the stack, key in `0.025 {{key:x²}} {{key:x²}} {{key:π}} {{key:×}} 2 {{key:÷}} 450 {{key:x⇄y}} {{key:÷}} 0.025 {{key:×}}` to obtain $\tau_{\max} = \mathbf{1.8335\times 10^7}\text{ Pa}$ ($18.33\text{ MPa}$), and `{{key:LASTX}} {{key:÷}} 1.2 {{key:×}} 79.3 {{key:E}} 9 {{key:÷}}` for $\theta = \mathbf{0.01110}\text{ rad}$ ($0.636^\circ$).

---

**Equation E.95 — Cantilever & Simply Supported Beam Tip Deflection:**
$$\delta_{\text{cantilever}} = \frac{F L^3}{3 E I}, \quad \delta_{\text{simple}} = \frac{F L^3}{48 E I}$$
With parameters $F$ (point load, $\text{N}$), $L$ (beam span, $\text{m}$), $E$ (Young's modulus, $\text{Pa}$), $I$ (cross-sectional second moment of area, $\text{m}^4$).
Euler–Bernoulli double integration of bending moment $M(x) = E I \, d^2w/dx^2$; note the cubic sensitivity ($L^3$) to beam span.  
On the stack (Cantilever), key in `L {{key:ENTER}} 3 {{key:yˣ}} F {{key:×}} 3 {{key:÷}} E {{key:÷}} I {{key:÷}}`.
For the benchmark case ($F = 5,000\text{ N}, L = 2.0\text{ m}, E = 200 \times 10^9\text{ Pa}, I = 4.0 \times 10^{-6}\text{ m}^4$), this evaluates to **`0.0167`** $\text{m}$ ($16.67\text{ mm}$).

---

**Equation E.96 — Hooke's Law Axial Stress, Strain & Elastic Elongation:**
$$\sigma = \frac{F}{A}, \quad \varepsilon = \frac{\Delta L}{L_0}, \quad \Delta L = \frac{F L_0}{A E}$$
With parameters $F$ (axial tensile force, $\text{N}$), $L_0$ (unstrained length, $\text{m}$), $A$ (cross-sectional area, $\text{m}^2$), $E$ (Young's modulus, $\text{Pa}$).
Linear elastic constitutive law ($\sigma = E \varepsilon$) for tie rods, suspension cables, and bolted preload joints.  
On the stack, key in `F {{key:ENTER}} L0 {{key:×}} A {{key:÷}} E {{key:÷}}`.
For the benchmark case (Steel tie rod: $F = 45,000\text{ N}, L_0 = 2.50\text{ m}, A = 3.00 \times 10^{-4}\text{ m}^2, E = 200 \times 10^9\text{ Pa}$), this evaluates to $\Delta L =$ **`0.001875`** $\text{m}$ ($1.875\text{ mm}$; axial stress $\sigma = 150.0\text{ MPa}$).

---

**Equation E.97 — Shockley Semiconductor Diode Current-Voltage Law:**
$$I_D = I_S \left[\exp\left(\frac{V_D}{n V_T}\right) - 1\right]$$
With parameters $I_S$ (reverse saturation current, $\text{A}$), $V_D$ (forward bias voltage, $\text{V}$), $n$ (ideality factor, $1.0\text{–}2.0$), $V_T = k_B T / q \approx 0.02585\text{ V}$ at $300\text{ K}$.
Carrier diffusion across a $p$-$n$ junction depletion barrier; inside-out RPN evaluation avoids parentheses around the exponential argument.  
On the stack, key in `VD {{key:ENTER}} n {{key:÷}} VT {{key:÷}} {{key:eˣ}} 1 {{key:-}} IS {{key:×}}`.
For the benchmark case (Silicon junction diode: $I_S = 1.0 \times 10^{-12}\text{ A}, V_D = 0.650\text{ V}, n = 1.0, V_T = 0.02585\text{ V}$), this evaluates to **`0.0835`** $\text{A}$ ($83.47\text{ mA}$).

---

**Equation E.98 — Operational Amplifier Closed-Loop Gain & $-3\text{ dB}$ Bandwidth:**
$$A_{v,\text{non}} = 1 + \frac{R_f}{R_g}, \quad A_{v,\text{inv}} = -\frac{R_f}{R_{\text{in}}}, \quad f_{-3\text{dB}} = \frac{\text{GBWP}}{A_{v,\text{non}}}$$
With parameters $R_f$ (feedback resistor, $\Omega$), $R_g$ or $R_{\text{in}}$ (input ground resistor, $\Omega$), $\text{GBWP}$ (gain-bandwidth product, $\text{Hz}$).
Negative feedback trades open-loop gain for precision closed-loop linearity and extended closed-loop bandwidth $f_{-3\text{dB}}$.  
On the stack (Non-Inverting Gain & Bandwidth), key in `Rf {{key:ENTER}} Rg {{key:÷}} 1 {{key:+}} GBWP {{key:x⇄y}} {{key:÷}}`.
For the benchmark case ($R_f = 90\text{ k}\Omega, R_g = 10\text{ k}\Omega, \text{GBWP} = 10.0\text{ MHz}$), this evaluates to $A_{v,\text{non}} =$ **`10.0000`** ($20.0\text{ dB}$); $f_{-3\text{dB}} =$ **`1.0000`** $\text{MHz}$.

---

**Equation E.99 — Friis Free-Space RF Path Loss ($\text{FSPL}$):**
$$\text{FSPL}_{\text{dB}} = 20\log_{10}\left(\frac{4\pi d f}{c}\right)$$
With parameters $d$ (line-of-sight range, $\text{m}$), $f$ (carrier frequency, $\text{Hz}$), $c = 2.99792458 \times 10^8\text{ m/s}$.
Spherical inverse-square wave-front spreading ($1/(4\pi d^2)$) combined with effective isotropic receiving aperture ($\lambda^2 / 4\pi$) for satellite and microwave link budgets.  
On the stack, key in `4 {{key:π}} {{key:×}} d {{key:×}} f {{key:×}} 2.99792458 {{key:E}} 8 {{key:÷}} {{key:LOG}} 20 {{key:×}}`.
For the benchmark case ($d = 1,000\text{ m}$ ($1\text{ km}$), $f = 2.40 \times 10^9\text{ Hz}$ ($2.4\text{ GHz}$ ISM band)), this evaluates to **`100.0460`** $\text{dB}$.

---

**Equation E.100 — Amdahl's Law Multiprocessor Speedup & CMOS Dynamic Power:**
$$S(N) = \frac{1}{(1 - p) + \frac{p}{N}}, \quad P_{\text{dyn}} = \alpha C V_{DD}^2 f$$
With parameters $p$ (parallelizable workload fraction), $N$ (processor core count); $\alpha$ (switching activity), $C$ (load capacitance, $\text{F}$), $V_{DD}$ (supply rail, $\text{V}$), $f$ (clock frequency, $\text{Hz}$).
Shows why serial bottlenecks $(1-p)$ cap parallel scaling at $1/(1-p)$ and why voltage scaling ($V_{DD}^2$) dominates microprocessor thermal design power.  
The stack evaluation sequences are:
- Amdahl Speedup $S(N)$: `p {{key:ENTER}} N {{key:÷}} 1 {{key:ENTER}} p {{key:-}} {{key:+}} {{key:1/x}}`  
- CMOS Dynamic Power $P_{\text{dyn}}$: `VDD {{key:x²}} alpha {{key:×}} C {{key:×}} f {{key:×}}`  
For the benchmark case ($p = 0.90$ ($90\%$ parallel code), $N = 16\text{ cores}$), this evaluates to $S(16) =$ **`6.4000`** $\times$ speedup (asymptotic ceiling $S(\infty) = 10.0\times$).

---

## Stack Optimization Idioms, Solver Templates & Boundary Guards

Fluency on the SC-32 comes from recognizing recurring mathematical forms and applying dedicated hardware keys to minimize button presses and eliminate redundant variable stores.

### The Harmonic Mean Idiom (Parallel Operator)
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
When evaluating a formula with a repeated scalar factor $K$ across multiple variables (for example, converting several values from feet to meters using $0.3048$, or multiplying items by the $1.0825$ sales-tax factor traced step-by-step in **[Appendix A, Trace 6](appendix-a-stack-lift-state-machine.md)**):
1. Load the constant into all four stack registers: `1.0825 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}` (fills $X, Y, Z, T$).
2. Enter Price 1: `10 {{key:×}}` $\rightarrow$ Displays result $10.825$. Register $T$ drops into $Z$ while duplicating $1.0825$ in $T$.
3. Enter Price 2: `{{key:CLx}} 25 {{key:×}}` $\rightarrow$ Displays $27.0625$. Because `{{key:CLx}}` disables stack lift so `25` overwrites $X$ in place, Register $T$ continues to feed $1.0825$ downward on every multiplication without ever touching `{{key:STO}}`/`{{key:RCL}}` memory registers.

### Numerical Root-Finding and Quadrature Function Selector

As detailed in [Chapter 7](07-polynomials-brent-solver.md) and [Chapter 8](08-calculus-romberg-quadrature.md), the StackCalc SC-32 provides numerical root-finding via Richard Brent's hybrid inverse-quadratic/secant/bisection algorithm (**`{{key:SOLVE}}`**, Right Shift `{{key:↱}}` above `{{key:7}}`) and adaptive Romberg numerical integration (**`{{key:∫}}`**, Right Shift `{{key:↱}}` above `{{key:8}}`). When a custom equation is active in **`{{key:EQN}}`** (Right Shift `{{key:↱}}` above `{{key:STO}}`), pressing `{{key:SOLVE}}` or `{{key:∫}}` prompts for the target variable softkey (`X`, `T`, etc., as in `{{key:SOLVE}} X`), whereas when no custom equation is selected, pressing `{{key:SOLVE}}` or `{{key:∫}}` followed by digit `0`–`5` invokes the corresponding built-in firmware test template:

1. **User-Defined Postfix Equations (`{{key:EQN}}` Mode):** Enter or select a custom RPN expression in `{{key:EQN}}`, exit to the stack, load the bracket or integration limits $[a, b]$ into Registers $Y$ and $X$ (`a {{key:ENTER}} b`), and press `{{key:SOLVE}}` or `{{key:∫}}` followed by the variable softkey (`X`).
2. **Built-In Benchmark Templates ($f_0$–$f_5$):** Pressing `{{key:SOLVE}}` or `{{key:∫}}` followed by digit `0`–`5` selects: `0` ($f_0(x) = x^2 - c$, with constant $c$ in Register $Z$), `1` ($f_1(x) = \cos(x) - x$), `2` ($f_2(x) = \sin(x)$), `3` ($f_3(x) = e^{-x^2}$), `4` ($f_4(x) = x^3 - 2x - 5$), or `5` ($f_5(x) = \ln(x) - 1$).
3. **Execute Brent Root-Finder (`{{key:SOLVE}}`):** Place parameter $c$ in Register $Z$ (if using $f_0$), lower bracket $a$ in Register $Y$, and upper bracket $b$ in Register $X$, then invoke `{{key:SOLVE}}`. The converged root $x^*$ is returned in Register $X$, the previous iterate in Register $Y$, and residual $f(x^*)$ in Register $Z$.
4. **Execute Romberg Quadrature (`{{key:∫}}`):** Place lower limit $a$ in Register $Y$ and upper limit $b$ in Register $X$, then invoke `{{key:∫}}`. The definite integral $\int_a^b f(x)\,dx$ is returned in Register $X$ with the Richardson truncation error estimate in Register $Y$.

**Benchmark Example — Parabolic Area with Template $f_0(x) = x^2 - c$:** To evaluate $\int_0^4 x^2 \, dx = \left[\frac{x^3}{3}\right]_0^4 = 21.3333$ (with $c = 0$ in Register $Z$), key in `0 {{key:ENTER}} 0 {{key:ENTER}} 4 {{key:∫}} 0` to obtain **`21.3333`** in Register $X$ (multiply by `3 {{key:×}}` for $\int_0^4 3x^2\,dx = 64.0000$).

### Storing Physical Constants & Numerical Boundary Guards

While pure mathematical invariants ($\pi$ via `{{key:π}}` and $e$ via `1 {{key:eˣ}}`) are permanently hardcoded in firmware, empirical 2022 CODATA physical constants (such as the Planck constant $h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}$, speed of light $c = 2.99792458 \times 10^8\text{ m/s}$, elementary charge $e = 1.602176634 \times 10^{-19}\text{ C}$, molar gas constant $R = 8.314462618\text{ J/(mol}\cdot\text{K)}$, and Avogadro constant $N_A = 6.02214076 \times 10^{23}\text{ mol}^{-1}$) are keyed explicitly via `{{key:E}}` or stored into the 26 non-volatile global letter registers (`{{key:STO}} A` through `{{key:STO}} Z`) for instant single-key recall (`{{key:RCL}} C`, `{{key:RCL}} H`, `{{key:RCL}} R`).

* **Scientific Exponent Entry Syntax:** Always use **`{{key:E}}`** (`1.602176634 {{key:E}} 19 {{key:+/-}}` enters a single atomic number into Register $X$), never `{{key:×}} 10 {{key:yˣ}}` (which consumes extra stack registers).
* **Trigonometric Angular Modes:** Surveying, navigation, and Snell's law formulas require Degrees mode (`{{key:MODES}} {{key:DEG}}`), whereas analytical calculus and Fourier oscillations require Radians mode (`{{key:MODES}} {{key:RAD}}`).
* **Non-Destructive Singularity Guards:** Division by zero ($x/0$ or $\ln 0$) displays `DIVIDE BY 0` (Code 01), and $\sqrt{-x}$ or $\ln(-x)$ in Real mode displays `INVALID DATA` (Code 02; in `{{key:CMPLX}}` mode, $\sqrt{-x}$ returns $i\sqrt{x}$ across $(Y, X)$). Press `{{key:C}}` or `{{key:<-}}` to dismiss any error banner without losing your stack.

---

For the historical primary sources, foundational numerical analysis papers, and classic engineering handbooks cited throughout this book and equation directory, continue to **[Appendix E: Primary Sources & Annotated Further Reading Guide](appendix-e-annotated-bibliography.md)**.

