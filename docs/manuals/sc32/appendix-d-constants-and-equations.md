---
title: "Appendix D: Mathematical Constants, SI Units & STEM Equations | Thinking in the Stack (SC-32)"
description: "Authoritative reference directory of immutable mathematical constants, complete BIPM SI prefixes, exact unit conversions, and 100 STEM engineering equations with optimal RPN keystrokes for the StackCalc SC-32."
---

# Appendix D: Mathematical Constants, SI Units & STEM Equations

## Mathematical Constants, BIPM SI Prefixes & Exact Unit Conversions

One hundred core equations across classical mechanics, electromagnetism, thermodynamics, optics, chemistry, astronomy, and finance pair each formula with its physical constants and step-by-step RPN stack execution on the StackCalc SC-32.

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
Physical constants spanning dozens of orders of magnitude (such as Planck's constant $6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}$) are entered directly via the exponent key (`6.62607015 {{key:E}} 34 {{key:+/-}}`). As multi-step equations execute, intermediate physical quantities (such as angular frequency $\omega$ in Register $Y$ and capacitance $C$ in Register $X$) remain continuously visible on the $132 \times 65$ transflective LCD, so deeply nested blackbody radiation, thermodynamic, and relativistic formulas collapse inside-out without parentheses or scratchpad registers.

### Fundamental Mathematical & Exact 2019 SI Physical Constants

Under the May 20, 2019 SI Redefinition (26th CGPM), seven defining constants of nature are fixed as exact numerical invariants with zero measurement uncertainty: the vacuum speed of light ($c = 299,792,458\text{ m/s}$), Planck's constant ($h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}$), elementary charge ($e = 1.602176634 \times 10^{-19}\text{ C}$), Boltzmann's constant ($k_B = 1.380649 \times 10^{-23}\text{ J/K}$), Avogadro's constant ($N_A = 6.02214076 \times 10^{23}\text{ mol}^{-1}$), the molar gas constant ($R = N_A k_B = 8.314462618\text{ J/(mol}\cdot\text{K)}$), and the Stefan–Boltzmann constant ($\sigma = \frac{2\pi^5 k_B^4}{15 c^2 h^3} = 5.670374419 \times 10^{-8}\text{ W/(m}^2\cdot\text{K}^4)$).

Alongside these exact invariants stand the CODATA 2022 experimentally measured constants—the Newtonian gravitational constant ($G = 6.67430 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2$), vacuum permittivity ($\varepsilon_0 = 8.8541878188 \times 10^{-12}\text{ F/m}$), and vacuum permeability ($\mu_0 = 1.25663706127 \times 10^{-6}\text{ N/A}^2$)—and the fundamental mathematical constants with their SC-32 RPN generation sequences:

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

### International Standard Unit Conversions & BIPM SI Prefixes

The International Bureau of Weights and Measures (BIPM) defines the complete set of SI prefixes—including the `ronna` ($10^{27}$), `quetta` ($10^{30}$), `ronto` ($10^{-27}$), and `quecto` ($10^{-30}$) prefixes adopted at the 27th CGPM—together with their direct `{{key:E}}` exponent keystrokes:

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

## Fundamental Equations of Science and Engineering

### Classical Mechanics, Orbital Dynamics & Statics

#### Kinematic Velocity-Displacement Relation
$$v_f = \sqrt{v_i^2 + 2 a \Delta x}$$
Derived by eliminating elapsed time $t$ between the velocity-time and position-time equations, this work-energy identity equates the specific work $a \Delta x$ performed by a constant acceleration $a$ ($\text{m/s}^2$) over a displacement $\Delta x$ ($\text{m}$) to the gain in kinetic energy per unit mass $\frac{1}{2}(v_f^2 - v_i^2)$ from initial speed $v_i$ ($\text{m/s}$). Because $v_f^2$ grows linearly with stopping or takeoff distance $\Delta x$, doubling a vehicle's initial velocity requires four times the braking distance under fixed deceleration.

On the SC-32 stack, squaring $v_i$ in place first and allowing automatic stack lift to hold $v_i^2$ in Register $Y$ while forming $2a\Delta x$ in Register $X$ (`vi {{key:x²}} 2 {{key:ENTER}} a {{key:×}} dx {{key:×}} {{key:+}} {{key:√x}}`) evaluates the benchmark takeoff roll ($v_i = 12.0\text{ m/s}, a = 4.5\text{ m/s}^2, \Delta x = 25.0\text{ m}$, where $v_i^2 = 144.0\text{ m}^2/\text{s}^2$ and $2a\Delta x = 225.0\text{ m}^2/\text{s}^2$) to `19.209373` $\text{m/s}$.

---

#### Projectile Motion Maximum Range
$$R = \frac{v_0^2 \sin(2\theta)}{g}$$
For a projectile launched over level ground in a vacuum with muzzle speed $v_0$ ($\text{m/s}$) and elevation angle $\theta$ (degrees) under standard gravity $g = 9.80665\text{ m/s}^2$, the horizontal range multiplies the vertical flight time $2v_0\sin\theta / g$ by the constant horizontal ground speed $v_0\cos\theta$. Collapsing $2\sin\theta\cos\theta$ through the trigonometric double-angle identity $\sin(2\theta)$ proves both that maximum range occurs at $\theta = 45^\circ$ (where $\sin 90^\circ = 1$) and that complementary launch angles $\theta$ and $90^\circ - \theta$ strike the exact same downrange point. In `{{key:DEG}}` mode, squaring $v_0$ first so it waits in Register $Y$ while doubling and taking the sine of $\theta$ (`v0 {{key:x²}} theta {{key:ENTER}} 2 {{key:×}} {{key:SIN}} {{key:×}} 9.80665 {{key:÷}}`) resolves $v_0 = 45.0\text{ m/s}$ and $\theta = 35.0^\circ$ ($v_0^2 \sin 70^\circ = 1902.8776\text{ m}^2/\text{s}^2$) to `194.0395` $\text{m}$.

---

#### Centripetal Acceleration & Radial Force
$$F_c = \frac{m v^2}{r}$$
Christian Huygens proved in *Horologium Oscillatorium* (1673) that deflecting a body of mass $m$ ($\text{kg}$) along a circular arc of radius $r$ ($\text{m}$) at constant tangential speed $v$ ($\text{m/s}$) requires a continuous inward radial acceleration $a_c = v^2 / r$ perpendicular to the velocity vector. Because lateral force scales quadratically with speed $v^2$ and inversely with turn radius $r$, doubling cornering velocity quadruples tire lateral shear or turbine blade root tension, whereas doubling the turn radius halves the load. Squaring $v$ immediately in Register $X$ before multiplying by mass and dividing by radius (`v {{key:x²}} m {{key:×}} r {{key:÷}}`) resolves a cornering vehicle ($m = 1250\text{ kg}, v = 24.0\text{ m/s}, r = 60.0\text{ m}$) via `{{res:sc32_appendix_d_constants_and_equations_seq_01:keys}}` to `{{res:sc32_appendix_d_constants_and_equations_seq_01:value}}` $\text{N}$ ($12.0\text{ kN}$).

---

#### Newton's Law of Universal Gravitation
$$F_g = G \frac{m_1 m_2}{r^2}$$
Isaac Newton's *Principia* (1687) unified terrestrial weight and celestial mechanics by demonstrating that any two spherically symmetric masses $m_1$ and $m_2$ ($\text{kg}$) separated by center-to-center distance $r$ ($\text{m}$) attract each other with a force proportional to the universal gravitational constant $G = 6.67430 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2$. The inverse-square $1/r^2$ geometric dilution reflects conservation of gravitational flux across concentric spherical shells of surface area $4\pi r^2$ in three-dimensional space. Entering the numerator product $G m_1 m_2$ via the scientific exponent key `{{key:E}}` and dividing by $r^2$ (`6.67430 {{key:E}} 11 {{key:+/-}} {{key:ENTER}} m1 {{key:×}} m2 {{key:×}} r {{key:x²}} {{key:÷}}`) for an $m_2 = 1500\text{ kg}$ spacecraft orbiting Earth ($m_1 = 5.9722 \times 10^{24}\text{ kg}$) at $r = 6.771 \times 10^6\text{ m}$ yields an orbital attraction of `13041.44` $\text{N}$.

---

#### Circular Orbital Velocity
$$v = \sqrt{\frac{\mu}{r}}$$
Equating the inward gravitational pull $\mu / r^2$—where $\mu = GM_\oplus = 3.986004418 \times 10^{14}\text{ m}^3/\text{s}^2$ is Earth's standard geocentric gravitational parameter—to the centripetal acceleration $v^2 / r$ required to maintain a circular orbit of radius $r$ ($\text{m}$) yields the local circular orbital speed. Because $r$ appears in the denominator under the radical, orbital mechanics exhibits the paradoxical property that spacecraft in higher-altitude orbits travel at slower linear velocities than those in low Earth orbit. Dividing $\mu$ by $r$ and extracting the square root in place (`3.986004418 {{key:E}} 14 {{key:ENTER}} r {{key:÷}} {{key:√x}}`) for a $400\text{ km}$ Low Earth Orbit ($r = 6.771 \times 10^6\text{ m}$) returns `7672.60` $\text{m/s}$.

---

#### Planetary Escape Velocity
$$v_{\text{esc}} = \sqrt{\frac{2 \mu}{r}} = v_{\text{orbital}} \times \sqrt{2}$$
A spacecraft escapes a central gravitational field of parameter $\mu$ ($\text{m}^3/\text{s}^2$) from radial distance $r$ ($\text{m}$) onto a zero-total-energy parabolic trajectory when its specific kinetic energy $\frac{1}{2}v_{\text{esc}}^2$ exactly balances the local gravitational potential well depth $\mu / r$. Regardless of the planet's mass or radius, the local escape speed is always exactly $\sqrt{2} \approx 1.41421$ times the circular orbital velocity at that same altitude. Evaluating the quotient under the radical directly on the stack (`2 {{key:ENTER}} mu {{key:×}} r {{key:÷}} {{key:√x}}`) from Earth's mean surface radius ($r = 6.371 \times 10^6\text{ m}, \mu = 3.986004418 \times 10^{14}\text{ m}^3/\text{s}^2$) yields `11186.1` $\text{m/s}$ ($11.19\text{ km/s}$).

---

#### Tsiolkovsky Rocket Burnout Equation
$$\Delta v = v_e \ln\left(\frac{m_0}{m_f}\right)$$
Konstantin Tsiolkovsky's 1903 differential momentum integration governs a rocket expelling propellant at effective exhaust velocity $v_e = I_{\text{sp}} g_0$ ($\text{m/s}$) as vehicle mass decreases from initial wet mass $m_0$ to final dry burnout mass $m_f$. Because ideal velocity change $\Delta v$ grows only with the natural logarithm of the mass ratio $m_0 / m_f$, achieving orbital or interplanetary velocities requires either high-specific-impulse propulsion ($v_e$) or staging to jettison empty structural mass along the ascent. Forming the mass ratio in Register $X$, taking `{{key:LN}}`, and scaling by $v_e$ (`m0 {{key:ENTER}} mf {{key:÷}} {{key:LN}} ve {{key:×}}`) for $v_e = 3100\text{ m/s}, m_0 = 45000\text{ kg}, m_f = 6500\text{ kg}$ yields `5998.07` $\text{m/s}$.

---

#### Rotational Kinetic Energy of Rigid Body
$$E_{\text{rot}} = \frac{1}{2} I \omega^2$$
Summing the translational kinetic energy $\frac{1}{2} dm (\omega r)^2$ of every differential mass element across a rigid rotor replaces linear mass $m$ with the mass moment of inertia $I = \int r^2\,dm$ ($\text{kg}\cdot\text{m}^2$) and linear speed $v$ with angular velocity $\omega$ ($\text{rad/s}$). Because geometric mass distribution scales $I$ with the square of radial distance $r^2$ while spin rate enters as $\omega^2$, energy-storage flywheels and satellite reaction wheels concentrate rim mass at the outer periphery and spin at high angular speeds. Squaring $\omega$ first on Register $X$ and multiplying by $I/2$ (`omega {{key:x²}} I {{key:×}} 2 {{key:÷}}`) for a rotor with $I = 4.25\text{ kg}\cdot\text{m}^2$ at $\omega = 150.0\text{ rad/s}$ gives `47812.5` $\text{J}$ ($47.81\text{ kJ}$).

---

#### Simple Gravity Pendulum Period
$$T = 2\pi \sqrt{\frac{L}{g}}$$
Under the small-angle linearization $\sin\theta \approx \theta$, the restoring gravitational torque on a simple pendulum of pivot-to-bob length $L$ ($\text{m}$) in local gravity $g = 9.80665\text{ m/s}^2$ forms a harmonic oscillator of angular frequency $\omega_0 = \sqrt{g/L}$. As Galileo observed and Christiaan Huygens formalized, the bob mass cancels out of both the gravitational restoring force and the inertial acceleration, so the round-trip period $T$ depends solely on $L$ and $g$. Computing the inner ratio $L/g$, taking its square root, and scaling by $2\pi$ (`L {{key:ENTER}} 9.80665 {{key:÷}} {{key:√x}} 2 {{key:×}} {{key:π}} {{key:×}}`) for a Huygens seconds pendulum ($L = 0.99362\text{ m}$, beating $1\text{ s}$ per half-swing) confirms $T =$ `2.00000` $\text{s}$.

---

#### Euler Critical Buckling Load for Slender Column
$$P_{\text{cr}} = \frac{\pi^2 E I}{K^2 L^2}$$
Leonhard Euler's 1744 eigenvalue analysis of the elastic elastica shows that a slender compression strut of Young's modulus $E$ ($\text{Pa}$), minimum weak-axis area moment of inertia $I$ ($\text{m}^4$), unsupported length $L$ ($\text{m}$), and effective end-restraint factor $K$ (where $K = 1.0$ for pinned-pinned ends and $K = 0.5$ for fixed-fixed ends) bifurcates into lateral bending long before reaching the material's compressive yield stress. Because the critical load $P_{\text{cr}}$ depends solely on flexural rigidity $EI$ and drops inversely with the square of effective length $(KL)^2$, doubling a column's unbraced span cuts its buckling capacity fourfold.

Forming the numerator $\pi^2 E I$ in Register $Y$ and dividing by $(KL)^2$ (`{{key:π}} {{key:x²}} E {{key:×}} I {{key:×}} K {{key:ENTER}} L {{key:×}} {{key:x²}} {{key:÷}}`) for a steel column ($E = 200 \times 10^9\text{ Pa}, I = 6.4 \times 10^{-6}\text{ m}^4, K = 1.0, L = 4.5\text{ m}$) yields `623856.5` $\text{N}$ ($623.86\text{ kN}$).

---

### Fluid Mechanics, Hydraulics & Aerodynamics


#### Torricelli Efflux Jet Velocity
$$v = \sqrt{2 g h}$$
Evangelista Torricelli demonstrated in 1643—a result later recognized as a direct application of Daniel Bernoulli's streamline energy conservation between a free reservoir surface and an open atmospheric discharge jet—that liquid under hydrostatic head $h$ ($\text{m}$) exits a sharp orifice at the exact speed acquired by a body falling freely from height $h$ under gravity $g = 9.80665\text{ m/s}^2$. Because efflux velocity grows only with the square root of head $\sqrt{h}$, quadrupling the liquid depth in a gravity-fed tank is required to double the nozzle discharge speed. Multiplying $2g$ by head $h$ and extracting the square root in place (`2 {{key:ENTER}} 9.80665 {{key:×}} h {{key:×}} {{key:√x}}`) for a tank head of $h = 5.0\text{ m}$ ($2gh = 98.0665\text{ m}^2/\text{s}^2$) yields `9.90285` $\text{m/s}$.

---

#### Volumetric Flow Continuity Equation
$$Q = A_1 v_1 = \frac{\pi D_1^2}{4} v_1$$
For an incompressible fluid moving through a circular conduit of internal diameter $D_1$ ($\text{m}$) at mean cross-sectional velocity $v_1$ ($\text{m/s}$), conservation of mass requires the volumetric flow rate $Q$ ($\text{m}^3/\text{s}$) to remain invariant across every cross-section ($A_1 v_1 = A_2 v_2$). Because circular cross-sectional area $A_1 = \frac{\pi}{4}D_1^2$ scales with the square of diameter, tapering a nozzle to half its upstream diameter reduces the flow area fourfold and forces the fluid velocity to quadruple. Squaring $D_1$ first on Register $X$ and scaling by $\frac{\pi}{4} v_1$ (`D {{key:x²}} {{key:π}} {{key:×}} 4 {{key:÷}} v {{key:×}}`) for a $D_1 = 0.15\text{ m}$ supply main flowing at $v_1 = 2.4\text{ m/s}$ yields `0.0424115` $\text{m}^3/\text{s}$ ($42.41\text{ L/s}$).

---

#### Reynolds Number for Pipe Flow
$$Re = \frac{\rho v D}{\mu}$$
Introduced by George Gabriel Stokes and popularized by Osborne Reynolds's 1883 dye-filament pipe experiments, the dimensionless Reynolds number measures the ratio of convective inertial momentum ($\rho v^2 / D$) to Newtonian viscous shear stress ($\mu v / D^2$) for a fluid of density $\rho$ ($\text{kg/m}^3$) and dynamic viscosity $\mu$ ($\text{Pa}\cdot\text{s}$) flowing at speed $v$ ($\text{m/s}$) through hydraulic diameter $D$ ($\text{m}$). Internal pipe flow remains smooth and laminar below $Re \approx 2300$, passes through an intermittent transitional regime, and becomes fully turbulent with chaotic eddy mixing above $Re \approx 4000$. Chaining the inertial numerator and dividing by viscosity (`rho {{key:ENTER}} v {{key:×}} D {{key:×}} mu {{key:÷}}`) for water at $20^\circ\text{C}$ ($\rho = 998\text{ kg/m}^3, v = 1.8\text{ m/s}, D = 0.05\text{ m}, \mu = 0.001002\text{ Pa}\cdot\text{s}$) gives $Re =$ `89640.7` (fully turbulent).

---

#### Darcy-Weisbach Friction Head Loss
$$h_f = f \frac{L}{D} \frac{v^2}{2 g}$$
Formulated by Henry Darcy and Julius Weisbach, this foundational hydraulic loss equation expresses the irreversible pressure head $h_f$ ($\text{m}$ of fluid column) dissipated by wall shear across a pipe of length $L$ ($\text{m}$) and diameter $D$ ($\text{m}$) carrying flow at velocity $v$ ($\text{m/s}$) under gravity $g = 9.80665\text{ m/s}^2$, where $f$ is the dimensionless Darcy friction factor from the Colebrook-White or Moody chart. Because head loss scales with the aspect ratio $L/D$ and the velocity head $v^2 / (2g)$, doubling volumetric throughput in a fixed conduit quadruples frictional pumping head. Evaluating the dimensionless geometric factor $f L / D$ first and multiplying by $v^2 / (2g)$ (`f {{key:ENTER}} L {{key:×}} D {{key:÷}} v {{key:x²}} {{key:×}} 2 {{key:÷}} 9.80665 {{key:÷}}`) for $f = 0.024, L = 120.0\text{ m}, D = 0.20\text{ m}, v = 2.5\text{ m/s}$ yields $h_f =$ `4.5887` $\text{m}$.

---

#### Manning Formula for Open Channel Uniform Flow
$$v = \frac{1}{n} R_h^{2/3} S^{1/2}$$
Irish engineer Robert Manning's 1889 empirical correlation governs steady, uniform, free-surface gravity flow in aqueducts, storm culverts, and natural riverbeds, balancing the downslope gravitational component $S = \Delta z / L$ against boundary roughness $n$ across a channel of hydraulic radius $R_h = A / P_{\text{wet}}$ ($\text{m}$, the cross-sectional flow area divided by wetted perimeter, with SI unit factor $k_n = 1.0\text{ m}^{1/3}/\text{s}$ or U.S. customary factor $1.4859\text{ ft}^{1/3}/\text{s}$). Deep, compact channels with a large hydraulic radius $R_h$ minimize wall drag per unit flow area, accelerating mean velocity as $R_h^{2/3}$. Raising $R_h$ to the $\frac{2}{3}$ power via `{{key:yˣ}}`, multiplying by $\sqrt{S}$, and dividing by Gauckler–Manning roughness $n$ (`Rh {{key:ENTER}} 2 {{key:ENTER}} 3 {{key:÷}} {{key:yˣ}} S {{key:√x}} {{key:×}} n {{key:÷}}`) for a concrete-lined canal ($n = 0.015, R_h = 0.85\text{ m}, S = 0.0025$) produces `2.9911` $\text{m/s}$.

---

#### Poiseuille Laminar Capillary Flow Rate
$$Q = \frac{\pi r^4 \Delta P}{8 \mu L}$$
Derived independently by Jean Léonard Marie Poiseuille and Gotthilf Hagen from the exact parabolic velocity profile $u(r)$ of steady laminar flow ($Re < 2300$), this law relates volumetric throughput $Q$ ($\text{m}^3/\text{s}$) to pressure drop $\Delta P$ ($\text{Pa}$) across a cylindrical capillary tube of inner radius $r$ ($\text{m}$) and length $L$ ($\text{m}$) filled with fluid of viscosity $\mu$ ($\text{Pa}\cdot\text{s}$). Because both the cross-sectional area ($\propto r^2$) and the peak centerline velocity ($\propto r^2$) scale quadratically with radius, laminar conductance varies with the fourth power $r^4$—meaning a $16\%$ constriction in a microfluidic channel or coronary artery cuts volumetric flow in half.

Raising $r$ to the fourth power first and chaining the remaining factors (`r {{key:ENTER}} 4 {{key:yˣ}} {{key:π}} {{key:×}} dP {{key:×}} 8 {{key:÷}} mu {{key:÷}} L {{key:÷}}`) for $r = 0.002\text{ m}, \Delta P = 5000\text{ Pa}, \mu = 0.0035\text{ Pa}\cdot\text{s}, L = 0.50\text{ m}$ yields $1.7952 \times 10^{-5}$ $\text{m}^3/\text{s}$.

---

#### Aerodynamic Dynamic Pressure
$$q = \frac{1}{2} \rho v^2$$
In subsonic aerodynamics, dynamic pressure $q$ ($\text{Pa}$) represents the kinetic energy per unit volume of an airstream of density $\rho$ ($\text{kg/m}^3$) moving at true airspeed $v$ ($\text{m/s}$), measured physically as the differential pressure between a forward-facing Pitot stagnation port and a flush static pressure port. Aerodynamic lift $L = q S C_L$ and parasitic drag $D = q S C_D$ scale directly with $q$, explaining why aircraft flying in thin high-altitude air ($\rho \ll \rho_0$) must maintain a much higher true airspeed $v$ to preserve the same indicated dynamic pressure and stall margin. Squaring airspeed $v$ in Register $X$ and multiplying by $\rho / 2$ (`v {{key:x²}} rho {{key:×}} 2 {{key:÷}}`) at standard sea level ($\rho = 1.225\text{ kg/m}^3, v = 65.0\text{ m/s}$) returns `2587.81` $\text{Pa}$.

---

#### Compressible Flow Mach Number
$$M = \frac{v}{\sqrt{\gamma R_{\text{specific}} T}}$$
Named after Austrian physicist Ernst Mach, the Mach number $M$ normalizes true flight speed $v$ ($\text{m/s}$) by the local speed of sound $a = \sqrt{\gamma R_{\text{specific}} T}$ in an ideal gas of adiabatic index $\gamma = 1.40$, specific gas constant $R_{\text{specific}} = 287.058\text{ J/(kg}\cdot\text{K)}$ for dry air, and absolute static temperature $T$ ($\text{K}$). Because acoustic wave propagation speed depends exclusively on the square root of absolute temperature $\sqrt{T}$, the speed of sound drops from $340.3\text{ m/s}$ at sea level ($288.15\text{ K}$) to $313.8\text{ m/s}$ in the cold stratosphere ($245.0\text{ K}$), bringing cruising airliners near the transonic compressibility threshold ($M \approx 0.8$).

Computing the acoustic denominator $\sqrt{\gamma R T}$ first in Register $X$, entering $v$, and swapping via `{{key:x⇄y}}` (`1.4 {{key:ENTER}} 287.058 {{key:×}} T {{key:×}} {{key:√x}} v {{key:x⇄y}} {{key:÷}}`) for $v = 240.0\text{ m/s}$ at $T = 245.0\text{ K}$ yields Mach `0.7649`.

---

### Thermodynamics, Gas Laws & Heat Transfer


#### Ideal Gas State Equation
$$P = \frac{n R T}{V}$$
By synthesizing Robert Boyle's isothermal compression law, Jacques Charles's isobaric expansion law, and Amedeo Avogadro's molar volume hypothesis, Émile Clapeyron's ideal gas equation relates the absolute pressure $P$ ($\text{Pa}$) exerted on a vessel of volume $V$ ($\text{m}^3$) to the molar quantity $n$ ($\text{mol}$), the exact 2019 SI molar gas constant $R = N_A k_B = 8.314462618\text{ J/(mol}\cdot\text{K)}$, and the absolute temperature $T$ ($\text{K}$). Microscopically, the numerator $nRT$ measures two-thirds of the total translational kinetic energy of the enclosed gas molecules colliding elastically against the container walls. Chaining the thermal energy product $nRT$ in Register $X$ before dividing by volume $V$ (`n {{key:ENTER}} 8.314462618 {{key:×}} T {{key:×}} V {{key:÷}}`) for $n = 4.5\text{ mol}$ at $T = 350.0\text{ K}$ inside $V = 0.035\text{ m}^3$ ($nRT = 13,095.28\text{ J}$) yields `374150.8` $\text{Pa}$ ($374.15\text{ kPa}$).

---

#### Carnot Thermodynamic Cycle Maximum Efficiency
$$\eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H}$$
Sadi Carnot's 1824 treatise *Réflexions sur la puissance motrice du feu* established that no heat engine operating between a hot thermal reservoir at absolute temperature $T_H$ ($\text{K}$) and a cold rejection sink at $T_C$ ($\text{K}$) can exceed the reversible isothermal-isentropic cycle efficiency $\eta_{\text{Carnot}}$. Because the Second Law of Thermodynamics mandates that entropy extracted from the hot source ($Q_H / T_H$) must be discharged into the cold sink ($Q_C / T_C \ge Q_H / T_H$), achieving $100\%$ thermal efficiency would require either an infinitely hot heat source or an unachievable absolute-zero sink ($T_C = 0\text{ K}$). Computing the absolute temperature ratio $T_C / T_H$ first and subtracting from unity via `{{key:x⇄y}}` (`TC {{key:ENTER}} TH {{key:÷}} 1 {{key:x⇄y}} {{key:-}}`) for $T_C = 295.0\text{ K}$ and $T_H = 850.0\text{ K}$ yields `0.65294` ($65.29\%$).

---

#### Stefan-Boltzmann Total Radiative Power
$$P = \sigma \epsilon A T^4$$
Derived by Jozef Stefan (1879) and Ludwig Boltzmann (1884) and later anchored to quantum mechanics by integrating Max Planck's spectral blackbody distribution over all frequencies and solid angles, this law expresses the total electromagnetic thermal power $P$ ($\text{W}$) radiated by a body of surface area $A$ ($\text{m}^2$), gray-body emissivity $\epsilon \in (0, 1]$, and absolute temperature $T$ ($\text{K}$), where $\sigma = 5.670374419 \times 10^{-8}\text{ W/(m}^2\cdot\text{K}^4)$. Because radiative emission scales with the fourth power of absolute temperature ($T^4$), doubling the temperature of a vacuum furnace filament or deep-space radiator panel multiplies its radiant heat rejection sixteenfold.

Raising $T$ to the fourth power first and multiplying by $A$, $\epsilon$, and $\sigma$ (`T {{key:ENTER}} 4 {{key:yˣ}} A {{key:×}} eps {{key:×}} 5.670374419 {{key:E}} 8 {{key:+/-}} {{key:×}}`) for $T = 1200.0\text{ K}, A = 1.8\text{ m}^2, \epsilon = 0.85$ gives `179898.7` $\text{W}$ ($179.90\text{ kW}$).

---

#### Fourier Conduction Heat Transfer Rate
$$q = \frac{k A (T_1 - T_2)}{L}$$
Jean-Baptiste Joseph Fourier's 1822 *Théorie analytique de la chaleur* established that steady-state conductive heat flow $q$ ($\text{W}$) across a planar slab of thermal conductivity $k$ ($\text{W/(m}\cdot\text{K)}$), cross-sectional area $A$ ($\text{m}^2$), and thickness $L$ ($\text{m}$) is directly proportional to the face-to-face temperature difference $T_1 - T_2$ ($\text{K}$). Writing the relation in thermal-circuit form $q = (T_1 - T_2) / R_{\text{th}}$ with thermal resistance $R_{\text{th}} = L / (kA)$ provides an exact mathematical parallel to Ohm's law for multi-layer building envelopes, semiconductor package baseplates, and cryogenic Dewar insulation. Forming the temperature drop $T_1 - T_2$ first and scaling by $k A / L$ (`T1 {{key:ENTER}} T2 {{key:-}} k {{key:×}} A {{key:×}} L {{key:÷}}`) for a masonry wall ($k = 0.75\text{ W/(m}\cdot\text{K)}, A = 15.0\text{ m}^2, L = 0.20\text{ m}$) spanning $T_1 = 295.15\text{ K}$ to $T_2 = 263.15\text{ K}$ yields `1800.0` $\text{W}$.

---

#### Newton's Law of Cooling Transient Temperature
$$T(t) = T_{\infty} + (T_0 - T_{\infty}) e^{-k t}$$
When a thermally conductive body with low internal Biot number ($\text{Bi} = h L_c / k \ll 0.1$) cools or warms from initial temperature $T_0$ in a convective bath of ambient temperature $T_\infty$, its temperature excess $T(t) - T_\infty$ decays exponentially at rate $k = hA / (m c_p)$ ($\text{s}^{-1}$) over elapsed time $t$ ($\text{s}$). Because the instantaneous cooling rate $dT/dt = -k(T - T_\infty)$ is proportional to the remaining thermal excess, each elapsed time constant $\tau = 1/k$ reduces the temperature gap to $e^{-1} \approx 36.79\%$ of its initial value. Evaluating inside-out from the decay factor $e^{-kt}$ outward (`k {{key:+/-}} {{key:ENTER}} t {{key:×}} {{key:eˣ}} T0 {{key:ENTER}} Tinf {{key:-}} {{key:×}} Tinf {{key:+}}`, or `k {{key:+/-}} {{key:ENTER}} t {{key:×}} {{key:eˣ}} N0 {{key:×}}` when $T_\infty = 0$) for $T_\infty = 20.0^\circ\text{C}, T_0 = 90.0^\circ\text{C}, k = 0.005\text{ s}^{-1}, t = 180.0\text{ s}$ resolves $T(180) =$ `48.46` $^\circ\text{C}$.

---

#### Logarithmic Mean Temperature Difference (LMTD)
$$\text{LMTD} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)}$$
In a parallel-flow or counterflow heat exchanger where the local fluid-to-fluid temperature approach $\Delta T(x)$ varies from $\Delta T_1$ at the inlet header to $\Delta T_2$ at the outlet header ($\text{K}$ or $^\circ\text{C}$), the local heat flux $dq = U \Delta T(x)\,dA$ causes $\Delta T(x)$ to decay exponentially along the exchanger length. Integrating that exponential profile yields the logarithmic mean temperature difference $\text{LMTD}$ for $q = U A \cdot \text{LMTD}$, which is always strictly less than the simple arithmetic average $(\Delta T_1 + \Delta T_2)/2$ whenever $\Delta T_1 \ne \Delta T_2$. Computing the terminal difference $\Delta T_1 - \Delta T_2$ in Register $Y$ and dividing by the natural logarithm of the terminal ratio $\ln(\Delta T_1 / \Delta T_2)$ (`dT1 {{key:ENTER}} dT2 {{key:-}} dT1 {{key:ENTER}} dT2 {{key:÷}} {{key:LN}} {{key:÷}}`) for $\Delta T_1 = 45.0\text{ K}$ and $\Delta T_2 = 18.0\text{ K}$ gives `29.4665` $\text{K}$.

---

#### Ideal Brayton Gas Turbine Thermal Efficiency
$$\eta = 1 - \frac{1}{r_p^{(\gamma - 1)/\gamma}}$$
Named after George Brayton, the ideal open or closed gas-turbine power cycle compresses intake gas isentropically across pressure ratio $r_p = P_2 / P_1$, adds heat at constant pressure in the combustor, and expands the hot gas isentropically through a power turbine, where $\gamma = c_p / c_v$ is the specific-heat ratio ($\gamma = 1.40$ for diatomic air). Because the isentropic temperature ratio across the compressor equals $T_2 / T_1 = r_p^{(\gamma-1)/\gamma}$, raising the overall compressor pressure ratio $r_p$ directly increases thermal efficiency and explains why modern turbofan cores operate at pressure ratios exceeding $40:1$. Forming the exponent $(\gamma - 1)/\gamma$ on the stack, raising $r_p$ via `{{key:yˣ}}`, taking the reciprocal, and subtracting from unity (`rp {{key:ENTER}} 1.4 {{key:ENTER}} 1 {{key:-}} 1.4 {{key:÷}} {{key:yˣ}} {{key:1/x}} 1 {{key:x⇄y}} {{key:-}}`) at $r_p = 16.0$ and $\gamma = 1.40$ yields `0.5471` ($54.71\%$).

---

#### Latent Heat Phase Transition Energy
$$Q = m L_v$$
Discovered by Joseph Black in 1761, latent heat $Q$ ($\text{J}$) represents the isothermal enthalpy required to break or reform intermolecular bonds across a first-order phase transition of mass $m$ ($\text{kg}$) with specific latent heat of vaporization (or fusion) $L_v$ ($\text{J/kg}$) while the thermodynamic temperature remains pinned at the boiling or melting point. Water's exceptionally high hydrogen-bond enthalpy of vaporization ($L_v = 2.26 \times 10^6\text{ J/kg}$ at $100^\circ\text{C}$—more than five times the sensible heat needed to warm liquid water from $0^\circ\text{C}$ to $100^\circ\text{C}$) underpins industrial steam Rankine boilers, heat pipes, and evaporative cooling towers. Multiplying mass $m$ by $L_v$ (`m {{key:ENTER}} Lv {{key:×}}`) for $m = 2.5\text{ kg}$ of boiling water at $100^\circ\text{C}$ yields `5650000.0` $\text{J}$ ($5.65\text{ MJ}$).

---

### Electricity, Magnetism & AC Circuit Analysis


#### Ohm's Law and DC Power Dissipation
$$P = I^2 R = \frac{V^2}{R} = V I$$
Combining Georg Simon Ohm's linear conduction law ($V = IR$) with James Prescott Joule's calorimetric heating law ($P = VI$) expresses the thermal power $P$ ($\text{W}$) dissipated in a resistive load $R$ ($\Omega$) under terminal voltage $V$ ($\text{V}$) and current $I$ ($\text{A}$). Because $P = V^2 / R$ scales quadratically with applied voltage across a fixed resistance (and $P = I^2 R$ scales quadratically with line current along a transmission cable), doubling supply voltage quadruples resistive heating, whereas stepping transmission voltage up tenfold reduces $I^2 R$ grid losses a hundredfold for the same delivered power. Squaring $V$ in Register $X$ and dividing by $R$ (`V {{key:x²}} R {{key:÷}}`) for a $V = 120.0\text{ V}$ heating element of resistance $R = 15.0\,\Omega$ yields `960.0` $\text{W}$.

---

#### Equivalent Resistance of Parallel Networks via x∥y
$$R_{\text{eq}} = R_1 \parallel R_2 \parallel R_3 = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}}$$
When resistive branches $R_1, R_2, R_3$ ($\Omega$) share a common terminal node pair, Kirchhoff's current law dictates that their individual conductances $G_i = 1 / R_i$ ($\text{S}$) sum linearly, so the combined equivalent resistance $R_{\text{eq}}$ is always strictly smaller than the smallest individual branch resistor. Rather than keying three reciprocals, two additions, and a final reciprocal, the SC-32's dedicated hardware parallel operator `{{key:x∥y}}` evaluates $X \cdot Y / (X + Y)$ in a single keystroke and associatively chains across any number of branches. Keying `R1 {{key:ENTER}} R2 {{key:x∥y}} R3 {{key:x∥y}}` for $R_1 = 100.0\,\Omega, R_2 = 150.0\,\Omega, R_3 = 300.0\,\Omega$ collapses $100 \parallel 150 = 60.0\,\Omega$ on the first press and $60 \parallel 300 =$ `50.0` $\Omega$ on the second.

---

#### Electrostatic Energy Stored in Capacitor
$$U_C = \frac{1}{2} C V^2$$
Charging a capacitor of capacitance $C$ ($\text{F}$) to terminal voltage $V$ ($\text{V}$) requires moving incremental charge $dq = C\,dv$ against the rising potential $v$, so integrating $\int_0^V C v\,dv$ yields the stored electrostatic field energy $U_C$ ($\text{J}$) with its characteristic factor of $\frac{1}{2}$ (the remaining half of the energy $C V^2$ supplied by a fixed-voltage DC source is dissipated as heat in the charging resistance). Because stored energy scales quadratically with voltage $V^2$, high-voltage pulsed-laser flashlamp banks, medical defibrillators, and EV traction-inverter DC-link capacitors pack substantial energy into compact dielectric volumes. Squaring $V$ first on Register $X$ and multiplying by $C/2$ (`V {{key:x²}} C {{key:×}} 2 {{key:÷}}`) for a $C = 47.0 \times 10^{-6}\text{ F}$ bus capacitor charged to $V = 450.0\text{ V}$ gives `4.75875` $\text{J}$.

---

#### Magnetic Energy Stored in Inductor
$$U_L = \frac{1}{2} L I^2$$
As the electromagnetic dual of a capacitor's electric field energy, establishing a current $I$ ($\text{A}$) through an inductor of self-inductance $L$ ($\text{H}$) requires doing work against Faraday's counter-EMF $v_L = L\,di/dt$, integrating $\int_0^I L i\,di$ into magnetic flux energy $U_L$ ($\text{J}$) stored within the core air gap and winding field. Because magnetic energy scales with $I^2$ and cannot change discontinuously without generating a destructive voltage spike ($v_L = L\,di/dt$), buck/boost switching regulators and solenoid drivers require freewheeling diodes or synchronous switches to commutate inductor current safely. Squaring $I$ in place and scaling by $L/2$ (`I {{key:x²}} L {{key:×}} 2 {{key:÷}}`) for an $L = 0.25\text{ H}$ filter choke carrying $I = 6.4\text{ A}$ yields `5.12` $\text{J}$.

---

#### RC Transient Charging Voltage
$$V_C(t) = V_0 \left(1 - e^{-t / (R C)}\right)$$
Applying a step supply voltage $V_0$ ($\text{V}$) through series resistance $R$ ($\Omega$) into an initially uncharged capacitor $C$ ($\text{F}$) produces a first-order differential relaxation governed by the time constant $\tau = R C$ ($\text{s}$). As the capacitor voltage $V_C(t)$ rises, the voltage drop $V_0 - V_C(t)$ driving charging current through $R$ decays exponentially, bringing $V_C(t)$ to $63.21\%$ of $V_0$ at $t = 1\tau$, $95.02\%$ at $t = 3\tau$, and $99.33\%$ at $t = 5\tau$. Evaluating from the dimensionless exponent $-t / (RC)$ outward (`t {{key:+/-}} {{key:ENTER}} R {{key:÷}} C {{key:÷}} {{key:eˣ}} {{key:+/-}} 1 {{key:+}} V0 {{key:×}}`) for $V_0 = 12.0\text{ V}, R = 10000.0\,\Omega, C = 220.0 \times 10^{-6}\text{ F}$ ($\tau = 2.2\text{ s}$) at $t = 3.5\text{ s}$ gives `9.5551` $\text{V}$.

---

#### RL Inductive Current Decay
$$I(t) = I_0 e^{-t (R / L)}$$
When an inductor $L$ ($\text{H}$) carrying steady initial current $I_0$ ($\text{A}$) is switched across a dissipative loop resistance $R$ ($\Omega$) at $t = 0$, its collapsing magnetic flux sustains current that decays exponentially with inductive time constant $\tau = L / R$ ($\text{s}$). Unlike an RC circuit where larger resistance slows the transient ($\tau = RC$), increasing loop resistance $R$ in an RL flyback path dissipates stored magnetic energy $\frac{1}{2}LI_0^2$ faster and shortens the decay time constant $\tau = L/R$. Forming the negative exponent $-t R / L$ first and scaling by $I_0$ (`t {{key:+/-}} {{key:ENTER}} R {{key:×}} L {{key:÷}} {{key:eˣ}} I0 {{key:×}}`, or `t {{key:+/-}} {{key:ENTER}} R {{key:×}} L {{key:÷}} {{key:eˣ}} {{key:+/-}} 1 {{key:+}} V {{key:×}} R {{key:÷}}` for step energization) for $I_0 = 5.0\text{ A}, R = 24.0\,\Omega, L = 0.80\text{ H}$ at $t = 0.05\text{ s}$ yields `1.1157` $\text{A}$.

---

#### LC Resonant Frequency
$$f_0 = \frac{1}{2 \pi \sqrt{L C}}$$
William Thomson (Lord Kelvin) derived in 1853 that an undamped tank circuit of inductance $L$ ($\text{H}$) and capacitance $C$ ($\text{F}$) exchanges energy harmonically between its magnetic and electric fields at the natural frequency $f_0$ ($\text{Hz}$) where inductive reactance $X_L = 2\pi f_0 L$ and capacitive reactance $X_C = 1 / (2\pi f_0 C)$ are equal in magnitude and opposite in phase. Because $f_0$ varies inversely with $\sqrt{LC}$, sweeping a variable tuning capacitor across a four-to-one capacitance ratio tunes an AM or HF radio receiver across a two-to-one frequency octave. Multiplying $L$ by $C$, taking `{{key:√x}}`, scaling by $2\pi$, and inverting via `{{key:1/x}}` (`L {{key:ENTER}} C {{key:×}} {{key:√x}} 2 {{key:×}} {{key:π}} {{key:×}} {{key:1/x}}`) for $L = 10.0 \times 10^{-3}\text{ H}$ and $C = 100.0 \times 10^{-12}\text{ F}$ ($\sqrt{LC} = 1.0 \times 10^{-6}\text{ s}$) yields `159154.9` $\text{Hz}$ ($159.15\text{ kHz}$).

---

#### RLC Series AC Total Impedance
$$Z = \sqrt{R^2 + \left(2 \pi f L - \frac{1}{2 \pi f C}\right)^2}$$
In steady-state sinusoidal AC analysis at frequency $f$ ($\text{Hz}$), a series branch of resistance $R$ ($\Omega$), inductance $L$ ($\text{H}$), and capacitance $C$ ($\text{F}$) presents complex impedance $\mathbf{Z} = R + j(X_L - X_C)$, where inductive reactance $X_L = 2\pi f L$ leads current by $+90^\circ$ and capacitive reactance $X_C = 1/(2\pi f C)$ lags by $-90^\circ$. Because the two reactive components lie $180^\circ$ apart along the imaginary axis, they partially or completely cancel each other before combining in quadrature with real resistance $R$. Storing angular frequency $\omega = 2\pi f$ in register `A` to evaluate $X_L - X_C$ without re-keying $2\pi f$ (`2 {{key:π}} {{key:×}} f {{key:×}} {{key:STO}} A L {{key:×}} {{key:RCL}} A C {{key:×}} {{key:1/x}} {{key:-}} {{key:x²}} R {{key:x²}} {{key:+}} {{key:√x}}`) for $R = 50.0\,\Omega, L = 0.05\text{ H}, C = 10.0 \times 10^{-6}\text{ F}, f = 120.0\text{ Hz}$ gives `107.293` $\Omega$.

---

#### Quality Factor of Resonant Circuit
$$Q = \frac{1}{R} \sqrt{\frac{L}{C}}$$
Introduced by K. S. Johnson at Western Electric in 1914, the dimensionless quality factor $Q$ of a series RLC resonator measures $2\pi$ times the ratio of peak energy stored in the reactive tank to the energy dissipated per cycle in series resistance $R$ ($\Omega$), expressed directly as the characteristic impedance $\sqrt{L/C}$ divided by $R$. High-$Q$ resonators exhibit both sharp spectral selectivity—with half-power ($-3\text{ dB}$) fractional bandwidth $\Delta f / f_0 = 1/Q$—and a resonant voltage magnification across $L$ and $C$ equal to $Q$ times the source excitation voltage. Computing the characteristic impedance $\sqrt{L/C}$ first and dividing by $R$ (`L {{key:ENTER}} C {{key:÷}} {{key:√x}} R {{key:÷}}`) for $R = 8.0\,\Omega, L = 2.5 \times 10^{-3}\text{ H}, C = 47.0 \times 10^{-9}\text{ F}$ yields $Q =$ `28.829`.

---

#### Decibel Power Gain Ratio
$$\text{dB} = 10 \log_{10}\left(\frac{P_2}{P_1}\right)$$
Originated at Bell Telephone Laboratories in the 1920s to quantify signal loss per mile of standard telephone cable, the decibel ($\text{dB}$, one-tenth of a bel) expresses the ratio of output power $P_2$ ($\text{W}$) to reference input power $P_1$ ($\text{W}$) on a base-$10$ logarithmic scale. Mapping power ratios through $10\log_{10}(\cdot)$ converts long chains of cascaded RF amplifier gains, mixer conversion losses, and waveguide attenuations from multi-step multiplications into simple algebraic additions ($+3.0103\text{ dB}$ per power doubling and $+10\text{ dB}$ per decade). Dividing $P_2$ by $P_1$, pressing `{{key:LOG}}`, and scaling by $10$ (`P2 {{key:ENTER}} P1 {{key:÷}} {{key:LOG}} 10 {{key:×}}`) for $P_1 = 0.025\text{ W}$ amplified to $P_2 = 120.0\text{ W}$ gives `36.8124` $\text{dB}$.

---

### Wave Mechanics, Acoustics & Physical Optics


#### Snell's Law of Refraction
$$\theta_2 = \arcsin\left(\frac{n_1 \sin\theta_1}{n_2}\right)$$
First discovered by Ibn Sahl in 984 CE and rediscovered by Willebrord Snellius in 1621, Snell's law follows from Pierre de Fermat's principle of least optical time across a boundary separating dielectric media of refractive indices $n_1 = c / v_1$ and $n_2 = c / v_2$. Continuity of tangential phase velocity along the interface forces an incident ray at angle $\theta_1$ (measured from the surface normal) to bend toward the normal when entering a denser medium ($n_2 > n_1$) and causes total internal reflection when propagating from a denser to a rarer medium at angles where $(n_1 / n_2)\sin\theta_1 > 1$. In `{{key:DEG}}` mode, taking $\sin\theta_1$, scaling by the index ratio $n_1 / n_2$, and applying `{{key:ASIN}}` (`theta1 {{key:SIN}} n1 {{key:×}} n2 {{key:÷}} {{key:ASIN}}`) for a beam entering crown glass ($n_2 = 1.52$) from air ($n_1 = 1.0003$) at $\theta_1 = 45.0^\circ$ gives `27.7297` $^\circ$.

---

#### Gaussian Thin Lens Equation via x∥y
$$f = \frac{d_o \cdot d_i}{d_o + d_i} = d_o \parallel d_i$$
In Carl Friedrich Gauss's paraxial optics approximation, a thin converging lens of focal length $f$ adds optical power $1/f$ to the diverging spherical wavefront curvature $1/d_o$ from an object at distance $d_o$ to focus a real conjugate image at distance $d_i$ according to $1/f = 1/d_o + 1/d_i$. Because the reciprocal sum of conjugate distances is algebraically identical to two parallel resistors, the SC-32's hardware `{{key:x∥y}}` operator solves thin-lens and spherical-mirror imaging in a single keystroke without reciprocals. Entering `do {{key:ENTER}} di {{key:x∥y}}` for an object at $d_o = 30.0\text{ cm}$ projecting a real image at $d_i = 60.0\text{ cm}$ directly returns the focal length $f =$ `20.0` $\text{cm}$.

---

#### Compound Optical Microscope Magnification
$$M = -\left(\frac{L_{\text{tube}}}{f_{\text{obj}}}\right) \left(\frac{d_{\text{near}}}{f_{\text{eye}}}\right)$$
A standard compound microscope achieves high overall angular magnification $M$ by cascading two positive lens stages separated by the mechanical tube length $L_{\text{tube}} = 160\text{ mm}$: a short-focal-length objective lens ($f_{\text{obj}}$, $\text{mm}$) projects a real, inverted intermediate image magnified laterally by $-L_{\text{tube}} / f_{\text{obj}}$, and an eyepiece ($f_{\text{eye}}$, $\text{mm}$) acts as a simple magnifier referenced to the human eye's relaxed near point $d_{\text{near}} = 250\text{ mm}$. Multiplying the objective's lateral magnification by the ocular's angular magnification (`160 {{key:ENTER}} fobj {{key:÷}} 250 {{key:ENTER}} feye {{key:÷}} {{key:×}} {{key:+/-}}`) for an $f_{\text{obj}} = 4.0\text{ mm}$ ($40\times$) objective paired with an $f_{\text{eye}} = 25.0\text{ mm}$ ($10\times$) ocular yields `-400.0` ($\times 400$ inverted angular magnification).

---

#### Acoustic Doppler Frequency Shift (Moving Source)
$$f' = f_0 \left(\frac{v}{v - v_s}\right)$$
Christian Doppler's 1842 principle explains why an acoustic source emitting at rest frequency $f_0$ ($\text{Hz}$) while advancing toward a stationary observer at speed $v_s$ ($\text{m/s}$) through air of sound speed $v = 343.0\text{ m/s}$ crowds successive wave crests closer together in space. Because the emitter chases its own outgoing wavefronts, the compressed wavelength ahead of the source shrinks to $\lambda' = (v - v_s)/f_0$, raising the observed pitch $f' = v / \lambda'$ hyperbolically until wavefronts pile up into a Mach-1 shock cone as $v_s \to v$. Forming the relative velocity $v - v_s$ first, dividing into $v$ via `{{key:x⇄y}}`, and scaling by $f_0$ (`343 {{key:ENTER}} vs {{key:-}} 343 {{key:x⇄y}} {{key:÷}} f0 {{key:×}}`) for an $f_0 = 500.0\text{ Hz}$ train horn approaching at $v_s = 35.0\text{ m/s}$ returns `556.818` $\text{Hz}$.

---

#### Sound Pressure Decibel Level
$$L_p = 20 \log_{10}\left(\frac{P_{\text{rms}}}{P_0}\right)$$
Acoustic Sound Pressure Level ($L_p$, in $\text{dB SPL}$) compares the root-mean-square pressure fluctuation $P_{\text{rms}}$ ($\text{Pa}$) of a sound wave against the internationally standardized threshold of human hearing at $1\text{ kHz}$, $P_0 = 20.0 \times 10^{-6}\text{ Pa}$ ($20\text{ }\mu\text{Pa}$). Because acoustic power intensity $I = P_{\text{rms}}^2 / (\rho c)$ is proportional to the square of pressure amplitude, the $10\log_{10}(I / I_0)$ power-ratio definition pulls the exponent of $2$ out front to become $20\log_{10}(P_{\text{rms}} / P_0)$, where every tenfold increase in pressure corresponds to $+20\text{ dB}$. Dividing $P_{\text{rms}}$ by $20\text{ }\mu\text{Pa}$, pressing `{{key:LOG}}`, and multiplying by $20$ (`Prms {{key:ENTER}} 20 {{key:E}} 6 {{key:+/-}} {{key:÷}} {{key:LOG}} 20 {{key:×}}`) at $P_{\text{rms}} = 0.632\text{ Pa}$ gives `90.0` $\text{dB}$ SPL.

---

#### Sabine Reverberation Time for Architectural Enclosure
$$RT_{60} = \frac{0.161 V}{A_{\text{total}}}$$
Pioneering architectural acoustician Wallace Clement Sabine established in 1898 that the reverberation time $RT_{60}$ ($\text{s}$)—the duration required for diffuse reverberant sound energy in a room of volume $V$ ($\text{m}^3$) to decay by $60\text{ dB}$ (one-millionth of its initial intensity) after a source stops—is directly proportional to room volume and inversely proportional to the effective absorption area $A_{\text{total}} = \sum S_i \alpha_i$ (in metric sabins, $\text{m}^2$). Physically, a larger room volume increases the mean free path $4V/S$ between wall reflections, whereas acoustic panels of high absorption coefficient $\alpha_i$ drain energy faster at each bounce (with empirical constant $0.161\text{ s/m}$ at $20^\circ\text{C}$). Multiplying $0.161$ by $V$ and dividing by $A_{\text{total}}$ (`0.161 {{key:ENTER}} V {{key:×}} Atot {{key:÷}}`) for a recital hall of $V = 850.0\text{ m}^3$ and $A_{\text{total}} = 110.0\text{ sabins}$ yields `1.244` $\text{s}$.

---

#### Optical Diffraction Grating Wavelength
$$\lambda = \frac{d \sin\theta}{m}$$
When collimated light illuminates a diffraction grating ruled with periodic slit spacing $d$ ($\text{m}$), each groove acts as a coherent Huygens secondary wavelet emitter across all outgoing angles $\theta$ (degrees). Adjacent wavelets interfere constructively only at discrete angles where their geometric path-length difference $d\sin\theta$ equals an integer multiple $m\lambda$ ($m = \pm 1, \pm 2, \dots$) of the optical wavelength $\lambda$ ($\text{m}$), dispersing polychromatic light into separated spectral orders. In `{{key:DEG}}` mode, evaluating $\sin\theta$ first, multiplying by grating pitch $d$, and dividing by order $m$ (`theta {{key:SIN}} d {{key:×}} m {{key:÷}}`) for a $600\text{ lines/mm}$ grating ($d = 1.6667 \times 10^{-6}\text{ m}$) at first-order angle $\theta = 22.45^\circ$ ($m = 1$) determines $\lambda =$ $6.365 \times 10^{-7}$ $\text{m}$ ($636.5\text{ nm}$).

---

#### Numerical Aperture of Optical Fiber
$$NA = \sqrt{n_{\text{core}}^2 - n_{\text{clad}}^2}$$
For a step-index optical fiber with core refractive index $n_{\text{core}}$ surrounded by lower-index cladding $n_{\text{clad}}$, Snell's law at the entrance face combined with the critical angle $\sin\theta_c = n_{\text{clad}} / n_{\text{core}}$ at the core-cladding wall defines the dimensionless Numerical Aperture $NA = n_0 \sin\theta_{\max}$. Any ray entering the fiber end-face within the acceptance cone half-angle $\theta_{\max} = \arcsin(NA)$ strikes the internal core wall shallower than the critical angle and propagates down the waveguide via lossless total internal reflection. Squaring both refractive indices, subtracting, and taking the square root (`ncore {{key:x²}} nclad {{key:x²}} {{key:-}} {{key:√x}}`) for $n_{\text{core}} = 1.482$ and $n_{\text{clad}} = 1.450$ yields $NA =$ `0.3063` ($\theta_{\max} = 17.84^\circ$).

---

### Nuclear, Atomic & Relativistic Physics


#### Einstein Mass-Energy Equivalence
$$E = m c^2$$
Albert Einstein's September 1905 paper demonstrated that rest mass $m$ ($\text{kg}$) is a concentrated reservoir of internal energy $E$ ($\text{J}$) scaled by the square of the exact vacuum speed of light $c = 299,792,458\text{ m/s}$, representing the zero-momentum case of the relativistic energy-momentum invariant $E^2 = (pc)^2 + (mc^2)^2$. Because the conversion factor $c^2 = 8.98755179 \times 10^{16}\text{ J/kg}$ is immense, a nuclear fission or fusion reaction that converts even a tiny mass defect $\Delta m$ of $1.0\text{ gram}$ ($1.0 \times 10^{-3}\text{ kg}$) into kinetic and radiative energy releases macroscopic power on the scale of a city's daily electrical consumption. Squaring $c$ in Register $X$ and multiplying by $m$ (`299792458 {{key:x²}} m {{key:×}}`) for $m = 1.0 \times 10^{-3}\text{ kg}$ yields $8.98755 \times 10^{13}$ $\text{J}$ ($89.88\text{ TJ}$).

---

#### Planck-Einstein Photon Energy
$$E_{\text{photon}} = \frac{h c}{\lambda}$$
Max Planck's 1900 resolution of the ultraviolet blackbody catastrophe and Albert Einstein's 1905 explanation of the photoelectric effect established that electromagnetic radiation of wavelength $\lambda$ ($\text{m}$) and frequency $\nu = c / \lambda$ is emitted and absorbed in discrete quanta of energy $E_{\text{photon}} = h\nu$, where $h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}$ and $c = 299,792,458\text{ m/s}$. Because photon energy varies inversely with wavelength $\lambda$, a single short-wavelength ultraviolet or X-ray photon can eject a bound inner-shell electron that no intensity of long-wavelength infrared illumination could ever dislodge.

Forming the universal constant product $hc = 1.98644586 \times 10^{-25}\text{ J}\cdot\text{m}$ on the stack and dividing by $\lambda$ (`6.62607015 {{key:E}} 34 {{key:+/-}} {{key:ENTER}} 299792458 {{key:×}} lambda {{key:÷}}`) for a green photon ($\lambda = 500.0 \times 10^{-9}\text{ m}$) yields $3.9729 \times 10^{-19}$ $\text{J}$ ($2.48\text{ eV}$).

---

#### de Broglie Particle Wavelength
$$\lambda = \frac{h}{m v}$$
In his 1924 doctoral thesis, Louis de Broglie extended wave-particle duality from massless photons ($p = h/\lambda$) to massive matter particles, proposing that any particle of mass $m$ ($\text{kg}$) moving at non-relativistic speed $v$ ($\text{m/s}$) with momentum $p = mv$ possesses an intrinsic matter-wave wavelength $\lambda = h / p$, where $h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}$. While macroscopic objects have immeasurably small wavelengths, electrons accelerated across kilovolt potentials exhibit sub-nanometer de Broglie wavelengths shorter than interatomic crystal spacings and support atomic-scale diffraction and transmission electron microscopy. Dividing Planck's constant $h$ sequentially by mass $m$ and velocity $v$ (`6.62607015 {{key:E}} 34 {{key:+/-}} {{key:ENTER}} m {{key:÷}} v {{key:÷}}`) for an electron ($m = 9.1093837 \times 10^{-31}\text{ kg}$) traveling at $v = 2.0 \times 10^6\text{ m/s}$ gives $3.6370 \times 10^{-10}$ $\text{m}$ ($0.3637\text{ nm}$).

---

#### Relativistic Lorentz Factor ($\gamma$)
$$\gamma = \frac{1}{\sqrt{1 - \beta^2}} = \frac{1}{\sqrt{1 - (v/c)^2}}$$
Hendrik Lorentz and Albert Einstein showed that invariance of the spacetime interval $ds^2 = (c\,dt)^2 - dx^2$ across inertial reference frames moving at relative velocity $v$ requires scaling time and space coordinates by the Lorentz factor $\gamma$, parameterized by the dimensionless speed ratio $\beta = v / c \in [0, 1)$. Near everyday speeds ($\beta \ll 1$), $\gamma \approx 1 + \frac{1}{2}\beta^2$ is indistinguishable from unity, but as $\beta \to 1$, $\gamma$ diverges toward infinity—dilating the proper lifetime $\Delta t = \gamma \Delta\tau$ of high-energy atmospheric muons and contracting longitudinal lengths $L = L_0 / \gamma$. Squaring $\beta$ in Register $X$, subtracting from $1$ via `{{key:x⇄y}}`, taking `{{key:√x}}`, and inverting via `{{key:1/x}}` (`beta {{key:x²}} 1 {{key:x⇄y}} {{key:-}} {{key:√x}} {{key:1/x}}`) at $\beta = 0.95$ ($1 - \beta^2 = 0.0975$) computes $\gamma =$ `3.20256`.

---

#### Relativistic Momentum
$$p = \gamma m v = \frac{m v}{\sqrt{1 - (v/c)^2}}$$
In special relativity, conservation of four-momentum across collisions requires the spatial momentum of a particle of rest mass $m$ ($\text{kg}$) moving at speed $v$ ($\text{m/s}$) to scale with the Lorentz factor as $p = \gamma m v$ rather than the Newtonian $mv$. As $v$ approaches the speed of light $c = 299,792,458\text{ m/s}$, continuous force application ($F = dp/dt$) pumps energy into the diverging $\gamma$ factor rather than pushing $v$ past $c$, which directly determines the magnetic bending rigidity $B\rho = p / q$ required to steer relativistic protons inside a synchrotron ring. Computing the radical $\sqrt{1 - (v/c)^2}$ first, forming $mv$, and dividing via `{{key:x⇄y}}` (`v {{key:ENTER}} 299792458 {{key:÷}} {{key:x²}} 1 {{key:x⇄y}} {{key:-}} {{key:√x}} m {{key:ENTER}} v {{key:×}} {{key:x⇄y}} {{key:÷}}`) for a proton ($m = 1.67262 \times 10^{-27}\text{ kg}$) at $v = 0.85 c = 2.548236 \times 10^8\text{ m/s}$ yields $8.0906 \times 10^{-19}$ $\text{kg}\cdot\text{m/s}$.

---

#### Radioactive Decay Exponential Law
$$N(t) = N_0 e^{-\lambda t} = N_0 \left(\frac{1}{2}\right)^{t / t_{1/2}}$$
Ernest Rutherford and Frederick Soddy established in 1902 that radioactive transmutation is a memoryless quantum tunneling process in which each unstable nucleus has a constant probability $\lambda = \ln(2) / t_{1/2}$ per unit time of decaying, independent of its age. Integrating $dN/dt = -\lambda N$ from an initial population or activity $N_0$ over elapsed time $t$ shows that every elapsed half-life $t_{1/2}$ reduces the surviving radioisotope inventory by an exact factor of two. Raising $0.5$ to the elapsed half-life count $t / t_{1/2}$ and scaling by $N_0$ (`0.5 {{key:ENTER}} t {{key:ENTER}} thalf {{key:÷}} {{key:yˣ}} N0 {{key:×}}`, or `k {{key:+/-}} {{key:ENTER}} t {{key:×}} {{key:eˣ}} N0 {{key:×}}` when given decay rate $k = \lambda$) for a Cobalt-60 source ($N_0 = 10000.0\text{ Bq}, t_{1/2} = 5.27\text{ years}$) after $t = 15.0\text{ years}$ returns `1390.5` $\text{Bq}$.

---

#### Rydberg Equation for Hydrogen Spectral Series
$$\frac{1}{\lambda} = R_{\infty} \left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)$$
Formulated empirically by Johannes Rydberg in 1888 and derived from first principles by Niels Bohr's 1913 quantized angular-momentum model of the hydrogen atom, this relation gives the vacuum wavelength $\lambda$ ($\text{m}$) of photons emitted or absorbed when an electron transitions between principal quantum shells $n_1$ and $n_2$ ($n_1 < n_2$), where $R_\infty = \frac{m_e e^4}{8 \varepsilon_0^2 h^3 c} = 1.0973731568 \times 10^7\text{ m}^{-1}$. Because bound orbital energies scale inversely with the square of the shell index ($E_n = -13.6\text{ eV}/n^2$), transitions terminating on $n_1 = 1, 2, 3$ generate the ultraviolet Lyman, visible Balmer, and infrared Paschen series respectively.

Computing the reciprocal-square difference $1/n_1^2 - 1/n_2^2$, multiplying by $R_\infty$, and pressing `{{key:1/x}}` (`n1 {{key:x²}} {{key:1/x}} n2 {{key:x²}} {{key:1/x}} {{key:-}} 1.0973731568 {{key:E}} 7 {{key:×}} {{key:1/x}}`) for the Balmer $H_\alpha$ red line ($n_1 = 2, n_2 = 3$) gives $6.5611 \times 10^{-7}$ $\text{m}$ ($656.11\text{ nm}$ with $R_\infty$, or $656.47\text{ nm}$ with reduced-mass $R_H$).

---

### Euclidean Mensuration, Trigonometry & Coordinate Geometry


#### Volume and Surface Area of Sphere
$$V = \frac{4}{3} \pi r^3, \quad A = 4 \pi r^2$$
In *On the Sphere and Cylinder* (c. 225 BCE)—the geometric ratio Archimedes regarded as his crowning achievement—he proved that a sphere of radius $r$ occupies exactly two-thirds of the volume ($\pi r^2 \cdot 2r = 2\pi r^3$) and two-thirds of the total closed surface area ($2\pi r^2 + 2\pi r \cdot 2r = 6\pi r^2$) of its circumscribing right circular cylinder. Differentiating $V(r) = \frac{4}{3}\pi r^3$ with respect to $r$ recovers $dV/dr = 4\pi r^2 = A$, because an infinitesimal radial expansion $dr$ adds a spherical shell of volume $A\,dr$. Cubing $r$ on the stack via `r {{key:ENTER}} 3 {{key:yˣ}} {{key:π}} {{key:×}} 4 {{key:×}} 3 {{key:÷}}` for volume and squaring via `r {{key:x²}} {{key:π}} {{key:×}} 4 {{key:×}}` for surface area at $r = 7.50\text{ cm}$ ($r^3 = 421.875\text{ cm}^3$) yields Volume = `1767.146` $\text{cm}^3$ and Area = `706.858` $\text{cm}^2$.

---

#### Right Circular Cone Volume & Lateral Surface Area
$$V = \frac{1}{3} \pi r^2 h, \quad A_{\text{lat}} = \pi r \sqrt{r^2 + h^2}$$
First established by Eudoxus of Cnidus via the method of exhaustion, a right circular cone of base radius $r$ and perpendicular altitude $h$ encloses exactly one-third the volume of its bounding cylinder $\pi r^2 h$ because horizontal cross-sectional disks shrink quadratically with distance from the apex ($\int_0^h (z/h)^2 dz = h/3$). Unrolling the conical sheet along a generator of Pythagorean slant height $\ell = \sqrt{r^2 + h^2}$ produces a planar circular sector of radius $\ell$ and arc length $2\pi r$, whose area is $\frac{1}{2}(2\pi r)\ell = \pi r\sqrt{r^2 + h^2}$. Evaluating volume via `r {{key:x²}} h {{key:×}} {{key:π}} {{key:×}} 3 {{key:÷}}` and lateral area via `r {{key:x²}} h {{key:x²}} {{key:+}} {{key:√x}} r {{key:×}} {{key:π}} {{key:×}}` for $r = 6.0\text{ cm}$ and $h = 14.0\text{ cm}$ returns Volume = `527.788` $\text{cm}^3$ and Lateral Area = `287.108` $\text{cm}^2$.

---

#### Frustum of Right Circular Cone Volume
$$V = \frac{1}{3} \pi h (R^2 + R r + r^2)$$
Slicing a right circular cone parallel to its base at height $h$ leaves a conical frustum bounded by lower radius $R$ and upper radius $r$—the circular counterpart of the ancient Egyptian Moscow Mathematical Papyrus (Problem 14, c. 1850 BCE) pyramidal frustum. Rather than multiplying $h$ by the arithmetic mean of the two end disks, exact integration over the linearly tapering radius $r(z)$ averages three equally weighted disks: the bottom base $\pi R^2$, the top base $\pi r^2$, and their geometric mean $\pi Rr$. Accumulating the quadratic sum $R^2 + Rr + r^2$ in Register $X$ before scaling by $\frac{1}{3}\pi h$ (`R {{key:x²}} R {{key:ENTER}} r {{key:×}} {{key:+}} r {{key:x²}} {{key:+}} h {{key:×}} 3 {{key:÷}} {{key:π}} {{key:×}}`) for $R = 8.0\text{ cm}, r = 3.0\text{ cm}, h = 12.0\text{ cm}$ ($R^2 + Rr + r^2 = 97.0\text{ cm}^2$) yields `1218.938` $\text{cm}^3$.

---

#### Torus Volume and Total Surface Area
$$V = 2 \pi^2 R r^2, \quad A = 4 \pi^2 R r$$
By Pappus of Alexandria's centroid theorems (Book VII of the *Collection*, c. 340 CE), revolving a planar circular cross-section of minor tube radius $r$ (area $\pi r^2$, perimeter $2\pi r$) around an external coplanar axis at major centroid radius $R$ ($R \ge r$) sweeps out a volume equal to the cross-sectional area times the centroid path length $2\pi R$, and a surface area equal to the perimeter times $2\pi R$. Because inward curvature on the inner equator ($R - r$) exactly cancels outward curvature on the outer equator ($R + r$), the torus behaves metrically like a straight cylinder of radius $r$ and length $2\pi R$, governing toroidal inductors, O-ring elastomer seals, and tokamak fusion vessels.

Evaluating `r {{key:x²}} R {{key:×}} 2 {{key:×}} {{key:π}} {{key:x²}} {{key:×}}` for volume and `R {{key:ENTER}} r {{key:×}} 4 {{key:×}} {{key:π}} {{key:x²}} {{key:×}}` for surface area at $R = 12.0\text{ cm}$ and $r = 2.5\text{ cm}$ yields Volume = `1480.44` $\text{cm}^3$ and Area = `1184.35` $\text{cm}^2$.

---

#### Heron's Formula for Arbitrary Triangle Area
$$A = \sqrt{s(s - a)(s - b)(s - c)}, \quad s = \frac{a + b + c}{2}$$
Recorded by Heron of Alexandria in Book I of his *Metrica* (c. 60 CE), this intrinsic distance formula determines the planar area $A$ of any triangle directly from its three edge lengths $a, b, c$ and semiperimeter $s = (a + b + c)/2$ without requiring an interior angle or dropped altitude. Each factor $(s - a), (s - b), (s - c)$ represents the tangent segment from a vertex to the inscribed circle of inradius $r = A / s$, and their product vanishes whenever the triangle degenerates into a collinear segment ($a + b = c$). Computing semiperimeter $s$ once, storing it in register `S`, and forming the four-term product under the radical (`a {{key:ENTER}} b {{key:+}} c {{key:+}} 2 {{key:÷}} {{key:STO}} S a {{key:-}} {{key:RCL}} S b {{key:-}} {{key:×}} {{key:RCL}} S c {{key:-}} {{key:×}} {{key:RCL}} S {{key:×}} {{key:√x}}`) for the classic $(13, 14, 15)$ Heronian triangle ($s = 21.0$, factors $21 \times 8 \times 7 \times 6 = 7056$) gives `84.000`.

---

#### Law of Cosines for Arbitrary Triangle
$$c = \sqrt{a^2 + b^2 - 2 a b \cos C}$$
Generalized from Book II, Propositions 12–13 of Euclid's *Elements* by the Persian astronomer Jamshīd al-Kāshī in 1427, the Law of Cosines resolves the third side $c$ of any oblique triangle from two adjacent sides $a, b$ and their included angle $C$ (degrees). Subtracting the Euclidean inner-product projection $2ab\cos C$ from the Pythagorean sum $a^2 + b^2$ accounts for acute ($C < 90^\circ$, where $\cos C > 0$ shortens $c$) and obtuse ($C > 90^\circ$, where $\cos C < 0$ lengthens $c$) vertex geometry, collapsing to $c = \sqrt{a^2 + b^2}$ at $C = 90^\circ$. In `{{key:DEG}}` mode, summing $a^2 + b^2$ in Register $Y$, subtracting $2ab\cos C$, and taking `{{key:√x}}` (`a {{key:x²}} b {{key:x²}} {{key:+}} 2 {{key:ENTER}} a {{key:×}} b {{key:×}} C {{key:COS}} {{key:×}} {{key:-}} {{key:√x}}`) for $a = 18.0, b = 25.0, C = 62.0^\circ$ returns `22.945`.

---

#### Great Circle Spherical Distance (Haversine Formula)
$$d = 2 R \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta\phi}{2}\right) + \cos\phi_1 \cos\phi_2 \sin^2\left(\frac{\Delta\lambda}{2}\right)}\right)$$
Introduced by James Inman in his 1835 *Navigation and Nautical Astronomy*, the haversine formula computes the shortest geodesic arc $d$ across a sphere of mean Earth radius $R = 6371.0\text{ km}$ between coordinates $(\phi_1, \lambda_1)$ and $(\phi_2, \lambda_2)$ using half-versed sines $\text{hav}(\theta) = \sin^2(\theta/2)$ of the latitude difference $\Delta\phi = \phi_2 - \phi_1$ and longitude difference $\Delta\lambda = \lambda_2 - \lambda_1$. Expressing central angle entirely in terms of $\sin^2(\Delta/2)$ avoids the severe floating-point cancellation that plagues the spherical law of cosines $\arccos(\sin\phi_1\sin\phi_2 + \cos\phi_1\cos\phi_2\cos\Delta\lambda)$ when two waypoints lie only meters or kilometers apart ($\cos\theta \approx 0.99999999$).

In `{{key:DEG}}` mode, evaluating the two haversine terms from the inside out and converting the half-central angle to radians via `{{key:▸RAD}}` (`phi2 {{key:ENTER}} phi1 {{key:-}} 2 {{key:÷}} {{key:SIN}} {{key:x²}} phi1 {{key:COS}} phi2 {{key:COS}} {{key:×}} lam2 {{key:ENTER}} lam1 {{key:-}} 2 {{key:÷}} {{key:SIN}} {{key:x²}} {{key:×}} {{key:+}} {{key:√x}} {{key:ASIN}} {{key:▸RAD}} 2 {{key:×}} 6371.0 {{key:×}}`) from New York ($40.7128^\circ\text{N}, 74.0060^\circ\text{W}$) to London ($51.5074^\circ\text{N}, 0.1278^\circ\text{W}$) yields `5570.2` $\text{km}$ ($3461.2\text{ miles}$).

---

#### Circular Sector Area and Arc Length
$$s = r \theta, \quad A = \frac{1}{2} r^2 \theta \quad (\theta\text{ in radians})$$
Because radian measure defines a central angle $\theta$ (in $\text{rad}$) as the dimensionless ratio of subtended arc length $s$ to radius $r$, a circular sector occupying fraction $\theta / (2\pi)$ of a complete turn has arc length $s = (\theta / 2\pi)(2\pi r) = r\theta$ and enclosed pie-slice area $A = (\theta / 2\pi)(\pi r^2) = \frac{1}{2}r^2\theta$. By a direct structural parallel to linear kinematics ($v = at$ and $x = \frac{1}{2}at^2$), integrating circumferential arc length $r\theta$ radially from $0$ to $r$ produces $\int_0^r \rho\theta\,d\rho = \frac{1}{2}r^2\theta$. Multiplying `r {{key:ENTER}} theta {{key:×}}` for arc length or `r {{key:x²}} theta {{key:×}} 2 {{key:÷}}` for sector area at $r = 12.0\text{ cm}$ and $\theta = 1.047198\text{ rad}$ ($60.0^\circ$, convert via `60 {{key:▸RAD}}`) yields Arc Length = `12.566` $\text{cm}$ and Sector Area = `75.398` $\text{cm}^2$.

---

#### Circular Segment Area
$$A = \frac{1}{2} r^2 (\theta - \sin\theta) \quad (\theta\text{ in radians})$$
A circular segment—the region bounded by a secant chord and its subtended arc of central angle $\theta$ (in radians) on a circle of radius $r$—is obtained by subtracting the area of the central isosceles triangle $\frac{1}{2}r^2\sin\theta$ from the full circular sector $\frac{1}{2}r^2\theta$. Civil and process engineers rely on this difference to calibrate the liquid volume inside partially filled horizontal cylindrical storage tanks and storm sewers as a function of wetted angle $\theta = 2\arccos((r - h)/r)$. In `{{key:RAD}}` mode, duplicating $\theta$ with `{{key:ENTER}}` to form $\theta - \sin\theta$ before multiplying by $r^2 / 2$ (`theta {{key:ENTER}} {{key:SIN}} {{key:-}} r {{key:x²}} {{key:×}} 2 {{key:÷}}`) for $r = 8.0\text{ m}$ and $\theta = 1.250\text{ rad}$ gives `9.633` $\text{m}^2$.

---

#### Circular Annulus & Annular Sector Area
$$A = \pi (R^2 - r^2) = \pi (R - r)(R + r), \quad A_{\text{sector}} = \frac{\theta}{2} (R - r)(R + r)$$
The planar ring (annulus) between two concentric circles of outer radius $R$ and inner bore radius $r$ has area $\pi(R^2 - r^2)$, while a sector subtending central angle $\theta$ ($\text{rad}$) encloses $A_{\text{sector}} = \frac{\theta}{2}(R^2 - r^2)$. Factoring the difference of squares as $(R - r)(R + r)$ reveals that the annulus area equals the radial wall thickness $w = R - r$ multiplied by the mean circumference $2\pi r_{\text{mean}} = \pi(R + r)$, and prevents loss of significant digits when evaluating thin-walled pipe cross-sections where $R \approx r$. Forming $(R - r)$ and $(R + r)$ on the stack and scaling by $\pi$ (`R {{key:ENTER}} r {{key:-}} R {{key:ENTER}} r {{key:+}} {{key:×}} {{key:π}} {{key:×}}`) for $R = 15.0\text{ cm}$ and $r = 10.0\text{ cm}$ evaluates to `392.699` $\text{cm}^2$.

---

#### Ellipse Area & Ramanujan's Second Perimeter Approximation
$$A = \pi a b, \quad h = \frac{(a - b)^2}{(a + b)^2}, \quad P \approx \pi (a + b) \left[ 1 + \frac{3h}{10 + \sqrt{4 - 3h}} \right]$$
Because an ellipse of semimajor axis $a$ and semiminor axis $b$ ($a \ge b$) is a uniform vertical scaling of a circle of radius $a$ by the aspect ratio $b/a$, its enclosed area scales exact circle area $\pi a^2$ to $A = \pi a b$. By contrast, its arc-length perimeter $P = 4a E(e)$ requires the complete elliptic integral of the second kind and admits no elementary closed form; however, Srinivasa Ramanujan's 1914 second rational approximation in terms of the symmetric oblateness parameter $h = (a - b)^2 / (a + b)^2$ matches the exact elliptic integral up to the $h^5$ Maclaurin term (accurate to better than $0.0004\%$ even at aspect ratios of $3:1$).

Evaluating area via `a {{key:ENTER}} b {{key:×}} {{key:π}} {{key:×}}` and storing $h$ in `A` to unpeel Ramanujan's fraction inside-out (`a {{key:ENTER}} b {{key:-}} a {{key:ENTER}} b {{key:+}} {{key:÷}} {{key:x²}} {{key:STO}} A 3 {{key:×}} 4 {{key:x⇄y}} {{key:-}} {{key:√x}} 10 {{key:+}} {{key:1/x}} 3 {{key:×}} {{key:RCL}} A {{key:×}} 1 {{key:+}} a {{key:ENTER}} b {{key:+}} {{key:×}} {{key:π}} {{key:×}}`) for $a = 10.0\text{ cm}, b = 6.0\text{ cm}$ ($h = 0.0625$) yields Area = `188.496` $\text{cm}^2$ and Perimeter = `51.054` $\text{cm}$.

---

#### Parabolic Segment Area (Archimedes' Quadrature)
$$A = \frac{2}{3} b h$$
In *Quadrature of the Parabola* (c. 240 BCE)—the earliest known summation of an infinite geometric series ($1 + \frac{1}{4} + \frac{1}{16} + \dots = \frac{4}{3}$)—Archimedes proved that the planar region bounded by a parabola and a chord of width $b$ with perpendicular vertex sagitta $h$ encloses exactly four-thirds the area of the inscribed triangle ($\frac{1}{2}bh$), or two-thirds the area of the circumscribing rectangle ($bh$). Structural engineers use this exact $\frac{2}{3}bh$ factor daily when integrating parabolic shear-stress distributions across rectangular beams and parabolic bending-moment diagrams under uniform loading. Multiplying base $b$ by height $h$ and scaling by $2/3$ (`b {{key:ENTER}} h {{key:×}} 2 {{key:×}} 3 {{key:÷}}`) for an arch of span $b = 18.0\text{ m}$ and rise $h = 6.0\text{ m}$ gives `72.000` $\text{m}^2$.

---

#### Regular $n$-gon Area, Inradius & Circumradius
$$A = \frac{1}{4} n s^2 \cot\left(\frac{\pi}{n}\right), \quad r = \frac{s}{2 \tan(\pi/n)}, \quad R = \frac{s}{2 \sin(\pi/n)}$$
Connecting the center of a regular $n$-sided polygon of edge length $s$ to its $n$ vertices partitions the figure into $n$ congruent isosceles triangles, each with central apex angle $2\pi / n$ ($\text{rad}$), base $s$, apothem (inradius) $r = \frac{s}{2}\cot(\pi/n)$, and circumradius $R = \frac{s}{2}\csc(\pi/n)$. Summing the $n$ sub-triangles yields $A = n(\frac{1}{2} s r) = \frac{1}{4} n s^2 \cot(\pi/n)$, which converges smoothly to $\pi r^2$ as $n \to \infty$ and sizes hexagonal bolt flats ($n = 6$), octagonal architectural piers ($n = 8$), and milled polygonal shafts. In `{{key:RAD}}` mode, evaluating $\cot(\pi / n)$ via the reciprocal of tangent (`{{key:RAD}} {{key:π}} n {{key:÷}} {{key:TAN}} {{key:1/x}} s {{key:x²}} {{key:×}} n {{key:×}} 4 {{key:÷}}`) for a regular hexagon ($n = 6, s = 5.0\text{ cm}$) yields `64.952` $\text{cm}^2$.

---

#### Brahmagupta's Formula & Ptolemy's Theorem for Cyclic Quadrilaterals
$$A = \sqrt{(s-a)(s-b)(s-c)(s-d)}, \quad s = \frac{a+b+c+d}{2}, \quad a c + b d = e f$$
Derived by the Indian mathematician Brahmagupta in his *Brāhmasphuṭasiddhānta* (628 CE), this formula gives the exact area $A$ of any cyclic quadrilateral—a four-sided polygon of side lengths $a, b, c, d$ inscribed within a circle—in terms of its semiperimeter $s = (a + b + c + d)/2$, while Claudius Ptolemy's theorem (*Almagest*, c. 150 CE) relates the opposite-side products to the interior diagonals $e, f$ via $ac + bd = ef$. By Bretschneider's identity, a cyclic quadrilateral encloses the strictly maximum possible area of any quadrilateral formed from four fixed edge lengths, and setting $d = 0$ immediately recovers Heron's triangle formula.

Storing semiperimeter $s$ in register `S` and multiplying the four residual factors (`a {{key:ENTER}} b {{key:+}} c {{key:+}} d {{key:+}} 2 {{key:÷}} {{key:STO}} S a {{key:-}} {{key:RCL}} S b {{key:-}} {{key:×}} {{key:RCL}} S c {{key:-}} {{key:×}} {{key:RCL}} S d {{key:-}} {{key:×}} {{key:√x}}`) for $a = 3.0, b = 4.0, c = 5.0, d = 6.0$ ($s = 9.0$) evaluates to `18.974`.

---

#### Stewart's Theorem for Triangle Cevians
$$m a n + d^2 a = b^2 m + c^2 n \implies d = \sqrt{\frac{b^2 m + c^2 n - m a n}{a}}$$
Published by Matthew Stewart in 1746 (and memorized across generations by the Gaelic-flavored mnemonic *"A man and his dad put a bomb in the sink"*: $m a n + d a d = b m b + c n c$), this theorem gives the length $d$ of any internal cevian segment from a triangle vertex to a point dividing the opposite base $a$ into adjacent sub-segments $m$ and $n$ ($m + n = a$). Applying the Law of Cosines to the two supplementary sub-triangles sharing the cevian foot eliminates the supplementary cosines $\cos\theta + \cos(\pi - \theta) = 0$ and yields a single master formula for triangle medians ($m = n = a/2$), angle bisectors ($m/n = c/b$), and internal structural truss web members.

Forming $b^2 m + c^2 n - m a n$ on the stack, dividing by $a$, and taking `{{key:√x}}` (`b {{key:x²}} m {{key:×}} c {{key:x²}} n {{key:×}} {{key:+}} m {{key:ENTER}} a {{key:×}} n {{key:×}} {{key:-}} a {{key:÷}} {{key:√x}}`) for the median to the hypotenuse of a $(6, 8, 10)$ right triangle ($a = 10.0, b = 8.0, c = 6.0, m = 5.0, n = 5.0$) confirms $d =$ `5.000`.

---

### Three-Dimensional Solid Geometry & Mensuration


#### Spherical Cap (Dome) & Spherical Zone Volume
$$V_{\text{cap}} = \frac{1}{3} \pi h^2 (3 R - h), \quad A_{\text{dome}} = 2 \pi R h$$
$$V_{\text{zone}} = \frac{\pi h}{6} (3 r_1^2 + 3 r_2^2 + h^2)$$
Integrating horizontal disk cross-sections $\pi(R^2 - z^2)\,dz$ from $z = R - h$ to the pole $z = R$ of a sphere of radius $R$ yields the volume $V_{\text{cap}}$ of a spherical cap of sagitta height $h$, while Archimedes' cylinder-projection theorem proves that the curved dome surface area $A_{\text{dome}} = 2\pi R h$ equals the lateral area of a slice of height $h$ on the circumscribing cylinder of radius $R$. When a spherical shell is truncated between two parallel planes separated by thickness $h$ with cut radii $r_1$ and $r_2$, the enclosed spherical zone volume $V_{\text{zone}}$ sizes cryogenic rocket tank bulkheads, architectural domes, and thick optical meniscus lenses.

Evaluating cap volume from the inside out via `3 {{key:ENTER}} R {{key:×}} h {{key:-}} h {{key:x²}} {{key:×}} {{key:π}} {{key:×}} 3 {{key:÷}}` (and dome area via `2 {{key:π}} {{key:×}} R {{key:×}} h {{key:×}}`) for $R = 10.0\text{ cm}$ and $h = 3.0\text{ cm}$ returns Volume = `254.469` $\text{cm}^3$ and Dome Area = `188.496` $\text{cm}^2$.

---

#### Frustum of Regular Pyramid Volume
$$V = \frac{h}{3} (A_1 + A_2 + \sqrt{A_1 A_2})$$
For any pyramidal or conical frustum of perpendicular altitude $h$ bounded by parallel, geometrically similar lower and upper base polygons of areas $A_1$ and $A_2$, cross-sectional area varies quadratically with elevation $z$, so exact integration yields $h$ times the Heronian mean $\frac{1}{3}(A_1 + A_2 + \sqrt{A_1 A_2})$. Setting $A_1 = \pi R^2$ and $A_2 = \pi r^2$ immediately recovers the circular cone frustum, whereas setting $A_2 = 0$ recovers the full pyramid volume $\frac{1}{3} A_1 h$ and furnishes a single unified formula for tapered concrete bridge piers, pedestal footings, and bulk grain hoppers. Computing the geometric mean $\sqrt{A_1 A_2}$ first on the stack and adding $A_1$ and $A_2$ before scaling by $h/3$ (`A1 {{key:ENTER}} A2 {{key:×}} {{key:√x}} A1 {{key:+}} A2 {{key:+}} h {{key:×}} 3 {{key:÷}}`) for $A_1 = 36.0\text{ m}^2, A_2 = 16.0\text{ m}^2, h = 9.0\text{ m}$ yields `228.000` $\text{m}^3$.

---

#### Ellipsoid Volume
$$V = \frac{4}{3} \pi a b c$$
A general triaxial ellipsoid defined by $(x/a)^2 + (y/b)^2 + (z/c)^2 \le 1$ is obtained by applying a three-dimensional linear transformation with Jacobian determinant $\det(\mathbf{J}) = abc$ to the unit sphere $x'^2 + y'^2 + z'^2 \le 1$ of volume $\frac{4}{3}\pi$. Scaling the unit sphere along the three orthogonal semiaxes $a, b, c$ yields $V = \frac{4}{3}\pi a b c$, which collapses to an oblate or prolate spheroid when two axes are equal ($a = b$, as in the WGS-84 reference geoid of Earth) and to a sphere when $a = b = c = r$. Chaining the product of the three semiaxes and scaling by $\frac{4}{3}\pi$ (`a {{key:ENTER}} b {{key:×}} c {{key:×}} {{key:π}} {{key:×}} 4 {{key:×}} 3 {{key:÷}}`) for $a = 6.0\text{ cm}, b = 4.0\text{ cm}, c = 3.0\text{ cm}$ gives `301.593` $\text{cm}^3$.

---

#### Paraboloid of Revolution Volume
$$V = \frac{1}{2} \pi r^2 h$$
In *On Conoids and Spheroids*, Archimedes demonstrated that revolving a parabola around its symmetry axis to form a circular paraboloid of rim radius $r$ and axial depth $h$ encloses exactly one-half the volume of its circumscribing cylinder ($\pi r^2 h$). The simple factor of $\frac{1}{2}$ arises because the cross-sectional disk area $A(z) = \pi [r(z)]^2 = \pi (r^2 / h) z$ grows strictly *linearly* with axial distance $z$ from the vertex ($0 \le z \le h$), so its average cross-section is just the midpoint disk $\frac{1}{2}\pi r^2$. Squaring rim radius $r$ in Register $X$ and multiplying by $\frac{1}{2}\pi h$ (`r {{key:x²}} h {{key:×}} {{key:π}} {{key:×}} 2 {{key:÷}}`) for a parabolic reflector or nosecone of $r = 4.0\text{ m}$ and $h = 3.0\text{ m}$ yields `75.398` $\text{m}^3$.

---

#### Cylindrical Ungula (Hoof) Volume
$$V = \frac{2}{3} r^3 \tan\alpha$$
When a right circular cylinder of radius $r$ is severed by an oblique plane that passes directly through a diameter of the circular base at inclination angle $\alpha$ (degrees), the wedge-shaped solid cut off is known in classical solid mensuration as a *cylindrical ungula* (from the Latin for a horse's hoof). Slicing the ungula perpendicular to the base diameter produces a family of similar right triangles of base $x = \sqrt{r^2 - y^2}$ and height $z = x\tan\alpha$, whose integral $\int_{-r}^r \frac{1}{2}(r^2 - y^2)\tan\alpha\,dy = \frac{2}{3}r^3\tan\alpha$ is completely free of $\pi$. In `{{key:DEG}}` mode, cubing $r$ and multiplying by $\frac{2}{3}\tan\alpha$ (`r {{key:ENTER}} 3 {{key:yˣ}} alpha {{key:TAN}} {{key:×}} 2 {{key:×}} 3 {{key:÷}}`) for $r = 6.0\text{ cm}$ and $\alpha = 45.0^\circ$ evaluates to exactly `144.000` $\text{cm}^3$.

---

#### Universal Prismoidal Formula (Simpson's 3D Rule)
$$V = \frac{h}{6} (A_{\text{top}} + 4 A_{\text{mid}} + A_{\text{bot}})$$
Because Thomas Simpson's $1:4:1$ parabolic quadrature rule integrates any polynomial of degree three or less with zero truncation error, the prismoidal formula gives the *exact* volume of any solid of altitude $h$—including spheres, spherical segments, cones, pyramids, frustums, wedges, paraboloids, hyperboloids, and civil highway earthwork prismoids—whose horizontal cross-sectional area $A(z)$ is a quadratic or cubic function of height $z$, using only the top area $A_{\text{top}}$, bottom area $A_{\text{bot}}$, and exact mid-plane area $A_{\text{mid}}$ at $z = h/2$. Here $A_{\text{mid}}$ is the true geometric cross-section at mid-height (not the average of $A_{\text{top}}$ and $A_{\text{bot}}$).

Scaling $A_{\text{mid}}$ by $4$ first, adding $A_{\text{top}}$ and $A_{\text{bot}}$, and multiplying by $h/6$ (`Amid {{key:ENTER}} 4 {{key:×}} Atop {{key:+}} Abot {{key:+}} h {{key:×}} 6 {{key:÷}}`) for a square frustum with $A_{\text{top}} = 16.0, A_{\text{mid}} = 36.0, A_{\text{bot}} = 64.0, h = 6.0$ yields `224.000`.

---

### Financial Mathematics, Amortization & Time Value of Money


#### Present Value of an Ordinary Annuity
$$PV = PMT \left[ \frac{1 - (1 + i)^{-N}}{i} \right]$$
Summing the finite geometric progression $\sum_{k=1}^N PMT (1 + i)^{-k}$ of $N$ equal end-of-period cash flows $PMT$ discounted at periodic compound interest rate $i$ yields the closed-form present-value annuity factor $[1 - (1+i)^{-N}] / i$. Financially, the numerator $1 - (1+i)^{-N}$ represents the difference between a perpetual stream of payments ($PMT / i$) and the present value of an identical perpetuity deferred by $N$ periods, pricing fixed-rate mortgages, equipment leases, and level-coupon bond streams. Evaluating the discount factor $(1 + i)^{-N}$ first on the stack, subtracting from unity via `{{key:x⇄y}}`, dividing by $i$, and scaling by $PMT$ (`1 {{key:ENTER}} i {{key:+}} N {{key:+/-}} {{key:yˣ}} 1 {{key:x⇄y}} {{key:-}} i {{key:÷}} PMT {{key:×}}`) for $PMT = 500\text{ USD}, i = 0.005$ ($6\%$ APR compounded monthly), and $N = 36\text{ months}$ yields `16,435.51` $\text{USD}$.

---

#### Future Value of an Ordinary Annuity
$$FV = PMT \left[ \frac{(1 + i)^N - 1}{i} \right]$$
Compounding $N$ regular end-of-period deposits $PMT$ forward at periodic interest rate $i$ sums the geometric series $\sum_{k=0}^{N-1} PMT(1 + i)^k$ into the accumulated terminal balance $FV = PV (1 + i)^N$. Because the compound growth factor $(1 + i)^N$ grows exponentially with horizon $N$, interest earned on prior interest eventually dominates the linear sum of raw principal contributions $N \cdot PMT$ in long-term retirement accounts and capital reserve funds. Forming $(1 + i)^N$, subtracting $1$, dividing by $i$, and multiplying by $PMT$ (`1 {{key:ENTER}} i {{key:+}} N {{key:yˣ}} 1 {{key:-}} i {{key:÷}} PMT {{key:×}}`) for $PMT = 250\text{ USD}, i = 0.006$ ($7.2\%$ APR monthly), and $N = 60\text{ months}$ yields `17,991.18` $\text{USD}$.

---

#### Loan Amortization Periodic Payment
$$PMT = PV \left[ \frac{i}{1 - (1 + i)^{-N}} \right]$$
Inverting the present-value annuity relation multiplies the initial borrowed principal $PV$ by the capital-recovery factor $i / [1 - (1+i)^{-N}]$ to determine the level periodic installment $PMT$ that retires both accruing interest and principal in exactly $N$ compounding periods. Early in an amortization schedule, the interest charge $i \cdot B_{k-1}$ consumes the majority of each payment $PMT$, whereas the principal reduction $PMT - i \cdot B_{k-1}$ accelerates exponentially toward the end of the loan term. Computing the denominator $1 - (1+i)^{-N}$ first, dividing into $i$ via `{{key:x⇄y}}`, and multiplying by $PV$ (`1 {{key:ENTER}} i {{key:+}} N {{key:+/-}} {{key:yˣ}} 1 {{key:x⇄y}} {{key:-}} i {{key:x⇄y}} {{key:÷}} PV {{key:×}}`) for $PV = 25,000\text{ USD}, i = 0.0045$ ($5.4\%$ APR monthly), and $N = 48\text{ months}$ gives `580.27` $\text{USD}$.

---

#### Sinking Fund Periodic Savings Payment
$$PMT = FV \left[ \frac{i}{(1 + i)^N - 1} \right]$$
Inverting the future-value annuity relation determines the uniform end-of-period contribution $PMT$ required to accumulate a scheduled target sum $FV$ over $N$ periods at periodic compound rate $i$. An algebraic identity links the capital-recovery and sinking-fund factors, $i / [1 - (1+i)^{-N}] = i + i / [(1+i)^N - 1]$, showing that amortizing a loan $PV$ is mathematically equivalent to paying interest-only $i \cdot PV$ each period while depositing into a sinking fund that accumulates $FV = PV$ at maturity. Forming $(1 + i)^N - 1$ in Register $X$, dividing into $i$ via `{{key:x⇄y}}`, and scaling by $FV$ (`1 {{key:ENTER}} i {{key:+}} N {{key:yˣ}} 1 {{key:-}} i {{key:x⇄y}} {{key:÷}} FV {{key:×}}`) for a target $FV = 50,000\text{ USD}$ at $i = 0.005$ ($6\%$ APR monthly) over $N = 120\text{ months}$ yields `305.10` $\text{USD}$.

---

#### Flat & Growing Perpetuities
$$PV_{\text{flat}} = \frac{PMT}{i}, \quad PV_{\text{growing}} = \frac{PMT}{i - g}$$
As the horizon $N \to \infty$, the discount term $(1 + i)^{-N}$ vanishes for any positive discount rate $i > 0$, collapsing the present value of an infinite stream of level cash flows $PMT$ to $PV_{\text{flat}} = PMT / i$. When the cash flow grows geometrically at rate $g$ per period ($PMT_k = PMT(1 + g)^{k-1}$ with $i > g$), Myron Gordon's 1956 dividend-discount summation of $\sum_{k=1}^\infty PMT (1+g)^{k-1}/(1+i)^k$ subtracts $g$ directly from the discount denominator to give $PV_{\text{growing}} = PMT / (i - g)$, valuing university endowments, preferred shares, and capitalized real estate. Dividing `PMT {{key:ENTER}} i {{key:÷}}` for a flat perpetuity or `PMT {{key:ENTER}} i {{key:ENTER}} g {{key:-}} {{key:÷}}` for a growing perpetuity at $PMT = 1,200\text{ USD/yr}, i = 0.06, g = 0.02$ returns Flat Perpetuity = `20,000.00` $\text{USD}$ and Growing Perpetuity = `30,000.00` $\text{USD}$.

---

### Chemistry, Electrochemistry, Chemical Kinetics & Biochemistry


#### pH & Hydronium Ion Activity
$$\text{pH} = -\log_{10}[\text{H}_3\text{O}^+], \quad [\text{H}_3\text{O}^+] = 10^{-\text{pH}}$$
Introduced by Danish biochemist Søren Peder Lauritz Sørensen at the Carlsberg Laboratory in 1909, the $\text{pH}$ scale (*pondus hydrogenii*) maps the aqueous molar activity of solvated hydronium ions $[\text{H}_3\text{O}^+]$ ($\text{mol/L}$) onto a negative base-$10$ logarithm. Because aqueous proton concentrations span more than fourteen orders of magnitude from $1\text{ M}$ strong acids ($\text{pH } 0$) to $1\text{ M}$ strong bases ($\text{pH } 14$, anchored by water's autoionization product $K_w = [\text{H}_3\text{O}^+][\text{OH}^-] = 10^{-14}$ at $25^\circ\text{C}$), every unit decrease in $\text{pH}$ represents a tenfold increase in acidity. Keying `H3O {{key:LOG}} {{key:+/-}}` (or inverting via `pH {{key:+/-}} {{key:10ˣ}}`) for $[\text{H}_3\text{O}^+] = 3.50 \times 10^{-5}\text{ mol/L}$ (`3.5 {{key:E}} 5 {{key:+/-}} {{key:LOG}} {{key:+/-}}`) yields $\text{pH} =$ `4.4559`.

---

#### Henderson–Hasselbalch Buffer Equilibrium
$$\text{pH} = \text{p}K_a + \log_{10}\left(\frac{[\text{A}^-]}{[\text{HA}]}\right)$$
Derived by Lawrence Joseph Henderson (1908) and Karl Albert Hasselbalch (1916) by taking the negative common logarithm of the weak-acid dissociation equilibrium $K_a = [\text{H}_3\text{O}^+][\text{A}^-] / [\text{HA}]$, this equation relates solution $\text{pH}$ to the acid's $\text{p}K_a = -\log_{10} K_a$ and the molar ratio of conjugate base $[\text{A}^-]$ to undissociated weak acid $[\text{HA}]$. Because $\log_{10}([\text{A}^-]/[\text{HA}])$ has its flattest slope when $[\text{A}^-] = [\text{HA}]$, a buffer resists $\text{pH}$ excursions most strongly within $\pm 1$ unit of $\text{pH} = \text{p}K_a$, governing both laboratory Tris/acetate buffers and human arterial blood bicarbonate homeostasis ($\text{pH } 7.40$).

Dividing conjugate base molarity by weak acid molarity, taking `{{key:LOG}}`, and adding $\text{p}K_a$ (`A_base {{key:ENTER}} HA {{key:÷}} {{key:LOG}} pKa {{key:+}}`) for an acetate buffer ($\text{p}K_a = 4.76, [\text{A}^-] = 0.25\text{ M}, [\text{HA}] = 0.15\text{ M}$) gives `4.9818`.

---

#### Nernst Electrochemical Cell Potential
$$E_{\text{cell}} = E^\circ_{\text{cell}} - \frac{R T}{n F} \ln Q$$
Walther Nernst derived in 1889 how the electromotive force $E_{\text{cell}}$ ($\text{V}$) of a galvanic cell or ion-selective membrane departs from its standard-state potential $E^\circ_{\text{cell}}$ ($\text{V}$) as a function of absolute temperature $T$ ($\text{K}$), the stoichiometric number of electrons transferred $n$, the Faraday constant $F = N_A e = 96,485.3\text{ C/mol}$, the gas constant $R = 8.31446\text{ J/(mol}\cdot\text{K)}$, and the reaction quotient $Q$ of product-to-reactant activities. Derived directly from the Gibbs free energy identity $\Delta G = \Delta G^\circ + RT\ln Q$ via $\Delta G = -n F E_{\text{cell}}$, the Nernst equation shows that cell voltage drops to zero ($E_{\text{cell}} = 0$) once the redox reaction reaches chemical equilibrium ($Q = K_{\text{eq}}$).

Forming the thermal voltage factor $RT / (nF)$ first, multiplying by $\ln Q$, and subtracting from $E^\circ_{\text{cell}}$ via `{{key:x⇄y}}` (`8.31446 {{key:ENTER}} T {{key:×}} n {{key:÷}} 96485.3 {{key:÷}} Q {{key:LN}} {{key:×}} E0 {{key:x⇄y}} {{key:-}}`) for a Daniell $\text{Zn/Cu}$ cell ($E^\circ_{\text{cell}} = 1.100\text{ V}, T = 298.15\text{ K}, n = 2, Q = 0.050$) yields `1.1385` $\text{V}$.

---

#### Arrhenius Chemical Reaction Rate Constant
$$k = A \exp\left(-\frac{E_a}{R T}\right)$$
Svante Arrhenius demonstrated in 1889 that the rate constant $k$ ($\text{s}^{-1}$ for a first-order reaction) of a thermally activated chemical process equals the pre-exponential collision-and-orientation frequency factor $A$ ($\text{s}^{-1}$) weighted by the Boltzmann factor $\exp[-E_a / (RT)]$, where $E_a$ ($\text{J/mol}$) is the molar activation energy barrier, $R = 8.314462618\text{ J/(mol}\cdot\text{K)}$, and $T$ ($\text{K}$) is absolute temperature. Because $T$ sits in the denominator of a negative exponent, even a modest $10\text{ K}$ rise near room temperature for a typical $E_a \approx 50$–$80\text{ kJ/mol}$ barrier roughly doubles or triples the fraction of molecular collisions energetic enough to cross the transition state.

Evaluating the dimensionless barrier ratio $-E_a / (RT)$ first, exponentiating via `{{key:eˣ}}`, and scaling by $A$ (`Ea {{key:ENTER}} 8.314462618 {{key:÷}} T {{key:÷}} {{key:+/-}} {{key:eˣ}} A {{key:×}}`) for $A = 1.25 \times 10^{11}\text{ s}^{-1}, E_a = 75,000\text{ J/mol}, T = 350.0\text{ K}$ gives $k =$ `0.8017` $\text{s}^{-1}$.

---

#### Michaelis–Menten Enzyme Saturation Kinetics
$$v_0 = \frac{V_{\max}[S]}{K_m + [S]}$$
Formulated by Leonor Michaelis and Maud Menten in 1913 from the quasi-steady-state formation and breakdown of an enzyme–substrate complex $E + S \rightleftharpoons ES \to E + P$, this rectangular hyperbola relates initial catalytic reaction velocity $v_0$ to substrate concentration $[S]$, maximum turnover velocity $V_{\max} = k_{\text{cat}}[E]_{\text{total}}$, and the Michaelis constant $K_m$ (the substrate concentration at which $v_0 = \frac{1}{2}V_{\max}$). At trace substrate levels ($[S] \ll K_m$), active sites are mostly empty and reaction rate scales linearly as first-order kinetics $v_0 \approx (V_{\max}/K_m)[S]$; at high substrate excess ($[S] \gg K_m$), every catalytic site is saturated and $v_0$ plateaus asymptotically at zero-order ceiling $V_{\max}$.

Forming the numerator $V_{\max}[S]$ in Register $Y$ and dividing by $K_m + [S]$ (`Vmax {{key:ENTER}} S {{key:×}} Km {{key:ENTER}} S {{key:+}} {{key:÷}}`) for $V_{\max} = 140.0\text{ }\mu\text{M/min}, [S] = 15.0\text{ mM}, K_m = 5.0\text{ mM}$ yields `105.0000` $\mu\text{M/min}$.

---

#### Beer–Lambert Spectrophotometric Absorbance
$$A = \varepsilon \ell c = -\log_{10}\left(\frac{I}{I_0}\right)$$
Developed successively by Pierre Bouguer (1729), Johann Heinrich Lambert (1760), and August Beer (1852), the Beer–Lambert law states that monochromatic light of incident intensity $I_0$ passing through a homogeneous absorbing solution of molar concentration $c$ ($\text{mol/L}$) and cuvette path length $\ell$ ($\text{cm}$) suffers differential attenuation $dI / I = -\ln(10)\varepsilon c\,dx$, where $\varepsilon$ ($\text{L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}$) is the wavelength-specific molar absorptivity. Because transmitted intensity $I = I_0 10^{-\varepsilon \ell c}$ decays exponentially with concentration, defining spectrophotometric absorbance as $A = -\log_{10}(I / I_0)$ produces a strictly linear calibration curve $A = \varepsilon \ell c$ for quantitative chemical assays.

Multiplying `eps {{key:ENTER}} l {{key:×}} c {{key:×}}` (and recovering transmittance $T = I/I_0$ via `A {{key:+/-}} {{key:10ˣ}}`) for an NADH enzymatic assay at $340\text{ nm}$ ($\varepsilon = 6,220\text{ L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}, \ell = 1.00\text{ cm}, c = 8.50 \times 10^{-5}\text{ M}$) gives $A =$ `0.5287` ($T = 29.60\%$).

---

#### Clausius–Clapeyron Vapor Pressure Scaling
$$P_2 = P_1 \exp\left[\frac{\Delta H_{\text{vap}}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right]$$
Rudolf Clausius and Émile Clapeyron showed that along a liquid–vapor phase-equilibrium boundary where molar vapor volume vastly exceeds liquid volume ($\Delta V_{\text{vap}} \approx RT/P$), the thermodynamic slope $dP / dT = \Delta H_{\text{vap}} / (T\Delta V_{\text{vap}})$ integrates assuming constant molar enthalpy of vaporization $\Delta H_{\text{vap}}$ ($\text{J/mol}$) and $R = 8.314462618\text{ J/(mol}\cdot\text{K)}$ to link saturation vapor pressures $P_1, P_2$ at absolute temperatures $T_1, T_2$ ($\text{K}$). Because saturation vapor pressure rises exponentially with $-1/T$, this relation predicts both the depressed boiling point of water at high mountain elevations and the vacuum pressure required for low-temperature solvent distillation.

Subtracting the reciprocal temperatures $1/T_1 - 1/T_2$ via `{{key:1/x}}`, scaling by $\Delta H_{\text{vap}} / R$, exponentiating, and multiplying by $P_1$ (`T1 {{key:1/x}} T2 {{key:1/x}} {{key:-}} dH {{key:×}} 8.314462618 {{key:÷}} {{key:eˣ}} P1 {{key:×}}`) for water ($P_1 = 23.76\text{ Torr}$ at $T_1 = 298.15\text{ K}$, $T_2 = 323.15\text{ K}$, $\Delta H_{\text{vap}} = 43,990\text{ J/mol}$) yields $P_2 =$ `93.7702` $\text{Torr}$.

---

#### Debye–Hückel Solution Ionic Strength
$$I = \frac{1}{2}\sum_{i=1}^n c_i z_i^2$$
Introduced by Gilbert N. Lewis and Merle Randall in 1921 and grounded in electrostatic statistical mechanics by Peter Debye and Erich Hückel in 1923, the ionic strength $I$ ($\text{mol/L}$) of an electrolyte solution sums the molar concentration $c_i$ ($\text{mol/L}$) of every dissolved cationic and anionic species weighted by the square of its integer charge valency $z_i$ (divided by $2$ because both positive cations and negative anions contribute to the screening cloud). Because both the Coulomb force on an ion and the Boltzmann clustering of counter-ions scale linearly with charge $z_i$, multivalent ions ($z_i = \pm 2, \pm 3$) contract the Debye screening length $\kappa^{-1} \propto 1/\sqrt{I}$ four to nine times as strongly as monovalent salts at equal molarity.

Squaring each ion charge $z_i$ before multiplying by concentration $c_i$ (`z1 {{key:x²}} c1 {{key:×}} z2 {{key:x²}} c2 {{key:×}} {{key:+}} 2 {{key:÷}}`) for $0.10\text{ M }\text{MgCl}_2$ ($c_{\text{Mg}^{2+}} = 0.10\text{ M}, z_1 = +2$; $c_{\text{Cl}^-} = 0.20\text{ M}, z_2 = -1$) evaluates to `0.3000` $\text{mol/L}$.

---

### Probability, Statistics, Quality Control & Information Theory


#### Binomial Probability Mass Function
$$P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}$$
Derived by Jacob Bernoulli in *Ars Conjectandi* (1713), the binomial probability mass function gives the exact probability of observing $k$ successes across $n$ independent, identically distributed Bernoulli trials when each trial succeeds with probability $p \in [0, 1]$ and fails with probability $q = 1 - p$. Any specific ordered sequence of $k$ successes and $n - k$ failures occurs with product probability $p^k (1 - p)^{n-k}$, and the binomial coefficient $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ (computed directly via the `PROB` menu `{{key:Cn,r}}` key without overflowing intermediate factorials) counts how many distinct permutations share that exact tally. Evaluating $\binom{n}{k}$ first and multiplying by $p^k$ and $(1 - p)^{n-k}$ (`n {{key:ENTER}} k {{key:Cn,r}} p {{key:ENTER}} k {{key:yˣ}} {{key:×}} 1 {{key:ENTER}} p {{key:-}} n {{key:ENTER}} k {{key:-}} {{key:yˣ}} {{key:×}}`) for $n = 10\text{ wafer dies}, k = 3\text{ defects}, p = 0.25$ yields `0.2503` ($25.0282\%$).

---

#### Poisson Rare-Event Arrival Probability
$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$
Siméon Denis Poisson derived in 1837 that as the number of trials $n \to \infty$ and the per-trial probability $p \to 0$ with expected count $\lambda = np$ held constant, the binomial distribution converges to this single-parameter law for the probability of observing $k \in \{0, 1, 2, \dots\}$ independent random events within a fixed time or space interval of mean arrival rate $\lambda$. Because a memoryless Poisson process has variance equal to its mean ($\sigma^2 = \mu = \lambda$), this distribution governs shot-noise photon arrivals on a photodiode, radioactive disintegration counts, cosmic-ray bit flips, and unscheduled packet arrivals at a network switch. Raising $\lambda$ to power $k$, multiplying by $e^{-\lambda}$, and dividing by $k!$ (`lam {{key:ENTER}} k {{key:yˣ}} lam {{key:+/-}} {{key:eˣ}} {{key:×}} k {{key:x!}} {{key:÷}}`) for $\lambda = 4.2\text{ photons/ms}$ and $k = 3\text{ photons}$ gives `0.1852` ($18.5165\%$).

---

#### Gaussian Standard $z$-Score & Confidence Interval Half-Width

$$z = \frac{x - \mu}{\sigma}, \quad E = z_{\alpha/2}\frac{s}{\sqrt{n}}$$

Standardizing a normally distributed observation $x$ by subtracting the population mean $\mu$ and dividing by standard deviation $\sigma$ maps any Gaussian variable onto the dimensionless unit normal distribution $\mathcal{N}(0, 1)$, while the Central Limit Theorem guarantees that the sample mean $\bar{x}$ of $n$ independent measurements with sample standard deviation $s$ (`{{key:sx}}`) has standard error $\text{SE} = s / \sqrt{n}$. Multiplying $s / \sqrt{n}$ by the two-sided critical quantile $z_{\alpha/2}$ ($1.9600$ for a $95\%$ confidence interval or $2.5758$ for $99\%$) yields the confidence interval half-width $E$, where quadrupling the sample size $n$ is required to halve the margin of error. Computing `x {{key:ENTER}} mu {{key:-}} sigma {{key:÷}}` for a $z$-score or `s {{key:ENTER}} n {{key:√x}} {{key:÷}} 1.96 {{key:×}}` for the $95\%$ confidence half-width with $s = 8.40\text{ MPa}, n = 49\text{ tensile specimens}, z_{\alpha/2} = 1.96$ returns $E =$ `2.3520` $\text{MPa}$.

---

#### Bayes' Theorem Diagnostic Posterior Probability
$$P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B \mid A)P(A) + P(B \mid A')P(A')}$$
Communicated posthumously by Richard Price in 1763, Thomas Bayes's theorem inverts conditional probabilities by dividing the joint true-positive probability $P(B \mid A)P(A)$ by the total probability $P(B) = P(B \mid A)P(A) + P(B \mid A')P(A')$ of observing a positive test or sensor alarm $B$ across both the true state $A$ (prior prevalence $P(A)$) and its complement $A'$ ($P(A') = 1 - P(A)$). When screening for a low-prevalence defect or condition ($P(A) \ll 1$), even a small false-positive rate $P(B \mid A')$ applied to the vast healthy population $P(A')$ can outnumber true positives $P(B \mid A)P(A)$ in the denominator.

Duplicating the true-positive product $P(B \mid A)P(A)$ on the stack with `{{key:ENTER}}` so it serves in both numerator and denominator (`PBA {{key:ENTER}} PA {{key:×}} {{key:ENTER}} PBnotA {{key:ENTER}} PnotA {{key:×}} {{key:+}} {{key:÷}}`) for $P(A) = 0.01$, sensitivity $P(B \mid A) = 0.99$, and false-positive rate $P(B \mid A') = 0.05$ ($P(A') = 0.99$) yields `0.1667` ($16.67\%$ posterior probability).

---

#### Six Sigma Process Capability Index ($C_{pk}$)
$$C_{pk} = \min\left(\frac{\text{USL} - \bar{x}}{3s},\; \frac{\bar{x} - \text{LSL}}{3s}\right)$$
In statistical process control (SPC) and semiconductor/mechanical manufacturing, the process capability index $C_{pk}$ compares the distance from the sample process mean $\bar{x}$ (`{{key:x̄}}`) to the nearer engineering tolerance boundary—either the Upper Specification Limit ($\text{USL}$) or Lower Specification Limit ($\text{LSL}$)—against the $3s$ one-sided natural process spread, where $s$ (`{{key:sx}}`) is the sample standard deviation. Unlike $C_p = (\text{USL} - \text{LSL})/(6s)$, which assumes a perfectly centered process, $C_{pk}$ penalizes off-center mean drift: $C_{pk} = 1.00$ corresponds to a $\pm 3\sigma$ ($99.73\%$ yield) boundary, $C_{pk} = 1.33$ is the standard $\pm 4\sigma$ industrial acceptance benchmark, and $C_{pk} = 2.00$ defines centered $\pm 6\sigma$ capability.

Evaluating the closer upper limit via `USL {{key:ENTER}} xbar {{key:-}} 3 {{key:÷}} s {{key:÷}}` for a CNC shaft ($\text{USL} = 10.050\text{ mm}, \text{LSL} = 9.950\text{ mm}, \bar{x} = 10.010\text{ mm}, s = 0.010\text{ mm}$) gives $C_{pk} =$ `1.3333`.

---

#### Shannon Information Entropy (Base-2 Bits)

$$H(X) = -\sum_{i=1}^m p_i \log_2 p_i = -\frac{1}{\ln 2}\sum_{i=1}^m p_i \ln p_i$$

In his 1948 monograph *A Mathematical Theory of Communication*, Claude Elwood Shannon defined the entropy $H(X)$ (in $\text{bits/symbol}$ when using base-$2$ logarithms) of a discrete random source emitting symbols $x_1, \dots, x_m$ with probabilities $p_1, \dots, p_m$ ($\sum p_i = 1$) as the expected self-information $\mathbb{E}[-\log_2 p_i]$. By Shannon's source coding theorem, $H(X)$ sets the exact theoretical lower bound on the average number of bits per symbol required for lossless compression (approached by Huffman and arithmetic coding), peaking at $\log_2 m\text{ bits}$ when all $m$ symbols are equiprobable and vanishing when one outcome is certain ($p_i = 1$). Summing $p_i \ln p_i$ on the stack and dividing by $-\ln 2$ (`p {{key:ENTER}} {{key:LN}} {{key:×}} 1 {{key:ENTER}} p {{key:-}} {{key:ENTER}} {{key:LN}} {{key:×}} {{key:+}} 2 {{key:LN}} {{key:÷}} {{key:+/-}}`) for a biased binary telemetry source ($p_1 = 0.75, p_2 = 0.25$) yields `0.8113` $\text{bits/symbol}$.

---

#### Shannon–Hartley Channel Capacity Law
$$C = B \log_2\left(1 + \frac{S}{N}\right) = \frac{B \ln(1 + S/N)}{\ln 2}$$
Building on Ralph Hartley's pulse-level signaling rate and Nyquist's $2B$ sampling theorem, Claude Shannon proved that a communication channel of analog bandwidth $B$ ($\text{Hz}$) corrupted by additive white Gaussian noise (AWGN) of mean noise power $N$ can transmit information with arbitrarily low bit-error probability at any rate up to the capacity ceiling $C$ ($\text{bits/s}$), where $S/N$ is the linear signal-to-noise power ratio. Because bandwidth $B$ scales capacity linearly whereas signal-to-noise ratio $S/N$ sits inside a base-$2$ logarithm, power-starved deep-space transponders and spread-spectrum links trade wider bandwidth for exponentially lower transmit power.

Converting $S/N$ via $\ln(1 + S/N) / \ln 2$ and multiplying by $B$ (`SNR {{key:ENTER}} 1 {{key:+}} {{key:LN}} 2 {{key:LN}} {{key:÷}} B {{key:×}}`, or from decibels via `SNR_dB {{key:ENTER}} 10 {{key:÷}} {{key:10ˣ}} 1 {{key:+}} {{key:LN}} 2 {{key:LN}} {{key:÷}} B {{key:×}}`) for a $B = 20.0\text{ MHz}$ channel at linear $S/N = 31.0$ ($14.91\text{ dB}$) gives `100.0000` $\text{Mbps}$.

---

#### M/M/1 Queueing Utilization, Queue Length & Latency
$$\rho = \frac{\lambda}{\mu}, \quad L = \frac{\lambda}{\mu - \lambda}, \quad W = \frac{1}{\mu - \lambda}$$
In Agner Krarup Erlang's and David George Kendall's Markovian $M/M/1$ single-server queueing model, independent Poisson requests arriving at mean rate $\lambda$ ($\text{req/s}$) are processed by a server with exponentially distributed service times of mean completion rate $\mu$ ($\text{req/s}$, requiring server utilization $\rho = \lambda / \mu < 1$ for steady-state stability). Solving the birth–death balance equations yields the mean number of requests in the system $L = \rho / (1 - \rho) = \lambda / (\mu - \lambda)$ and—via John Little's universal conservation law $L = \lambda W$—the mean end-to-end response latency $W = 1 / (\mu - \lambda)$ (queuing wait plus service time), which diverges hyperbolically as utilization $\rho$ approaches $100\%$.

Evaluating `lam {{key:ENTER}} mu {{key:ENTER}} lam {{key:-}} {{key:÷}}` for $L$ and `mu {{key:ENTER}} lam {{key:-}} {{key:1/x}}` for $W$ at $\lambda = 45.0\text{ req/s}$ and $\mu = 60.0\text{ req/s}$ ($\rho = 75\%$) yields $L =$ `3.0000` $\text{requests}$ and $W =$ `0.0667` $\text{s}$ ($66.7\text{ ms}$).

---

### Structural Mechanics, Semiconductor Electronics, RF & Computer Engineering


#### Cylindrical Shaft Torsional Shear Stress & Angle of Twist
$$\tau_{\max} = \frac{T r}{J}, \qquad \theta = \frac{T L}{G J}, \qquad J = \frac{\pi r^4}{2}$$
Charles-Augustin de Coulomb's torsion theory shows that twisting a solid circular shaft of radius $r$ ($\text{m}$), length $L$ ($\text{m}$), and shear modulus $G$ ($\text{Pa}$) under torque $T$ ($\text{N}\cdot\text{m}$) produces a shear strain distribution that grows linearly from zero along the neutral axis to a peak outer-fiber shear stress $\tau_{\max} = T r / J$, where $J = \int_0^r \rho^2 (2\pi\rho\,d\rho) = \frac{1}{2}\pi r^4$ ($\text{m}^4$) is the polar moment of inertia. Because $J$ scales with the fourth power of radius ($r^4$), doubling a drive shaft's diameter reduces peak shear stress eightfold ($\propto 1/r^3$) and cuts total elastic twist angle $\theta = TL/(GJ)$ ($\text{rad}$) sixteenfold ($\propto 1/r^4$).

Computing $J = \frac{1}{2}\pi r^4$ first to obtain $\tau_{\max}$ (`r {{key:x²}} {{key:x²}} {{key:π}} {{key:×}} 2 {{key:÷}} T {{key:x⇄y}} {{key:÷}} r {{key:×}}`) and recovering $T/J$ via `{{key:LASTX}}` for twist angle (`{{key:LASTX}} {{key:÷}} L {{key:×}} G {{key:÷}}`) at $T = 450\text{ N}\cdot\text{m}, r = 0.025\text{ m}, L = 1.20\text{ m}, G = 79.3 \times 10^9\text{ Pa}$ ($J = 6.1359 \times 10^{-7}\text{ m}^4$) yields $\tau_{\max} =$ $1.8335 \times 10^{7}$ $\text{Pa}$ ($18.33\text{ MPa}$) and $\theta =$ `0.01110` $\text{rad}$ ($0.636^\circ$).

---

#### Cantilever & Simply Supported Beam Tip Deflection
$$\delta_{\text{cantilever}} = \frac{F L^3}{3 E I}, \quad \delta_{\text{simple}} = \frac{F L^3}{48 E I}$$
Integrating the Euler–Bernoulli elastic beam differential equation $EI\,d^2w/dx^2 = M(x)$ twice across a span $L$ ($\text{m}$) of Young's modulus $E$ ($\text{Pa}$) and cross-sectional area moment of inertia $I$ ($\text{m}^4$) subjected to a concentrated point load $F$ ($\text{N}$) shows that maximum transverse deflection $\delta$ ($\text{m}$) grows with the *cube* of span length ($L^3$) and inversely with flexural rigidity $EI$. Supporting the beam at both ends with a mid-span load reduces the peak bending moment from $FL$ to $FL/4$ and halves the effective half-span integration length, so a simply supported beam is sixteen times stiffer ($\frac{1}{48}$ vs. $\frac{1}{3}$) than an end-loaded cantilever of identical span.

Cubing $L$ on the stack and scaling by $F / (3EI)$ (`L {{key:ENTER}} 3 {{key:yˣ}} F {{key:×}} 3 {{key:÷}} E {{key:÷}} I {{key:÷}}`) for a cantilever with $F = 5,000\text{ N}, L = 2.0\text{ m}, E = 200 \times 10^9\text{ Pa}, I = 4.0 \times 10^{-6}\text{ m}^4$ yields `0.0167` $\text{m}$ ($16.67\text{ mm}$).

---

#### Hooke's Law Axial Stress, Strain & Elastic Elongation
$$\sigma = \frac{F}{A}, \quad \varepsilon = \frac{\Delta L}{L_0}, \quad \Delta L = \frac{F L_0}{A E}$$
Combining Robert Hooke's 1678 linear spring law (*"ut tensio, sic vis"*) with Thomas Young's 1807 material modulus $E = \sigma / \varepsilon$ ($\text{Pa}$) relates engineering axial stress $\sigma = F / A$ ($\text{Pa}$) and dimensionless engineering strain $\varepsilon = \Delta L / L_0$ across a prismatic bar of unstrained length $L_0$ ($\text{m}$) and cross-sectional area $A$ ($\text{m}^2$) under axial load $F$ ($\text{N}$). Writing $\Delta L = F / (AE / L_0)$ identifies $k = AE / L_0$ ($\text{N/m}$) as the exact axial spring stiffness of structural tension rods, suspension cables, and preloaded bolted joints below the proportional elastic limit.

Multiplying $F$ by $L_0$ and dividing sequentially by $A$ and $E$ (`F {{key:ENTER}} L0 {{key:×}} A {{key:÷}} E {{key:÷}}`) for a steel tie rod ($F = 45,000\text{ N}, L_0 = 2.50\text{ m}, A = 3.00 \times 10^{-4}\text{ m}^2, E = 200 \times 10^9\text{ Pa}$) yields $\Delta L =$ `0.001875` $\text{m}$ ($1.875\text{ mm}$, at axial stress $\sigma = 150.0\text{ MPa}$).

---

#### Shockley Semiconductor Diode Current-Voltage Law
$$I_D = I_S \left[\exp\left(\frac{V_D}{n V_T}\right) - 1\right]$$
Derived by William Shockley in 1949 from minority-carrier injection and diffusion across a semiconductor $p$-$n$ depletion region, this equation relates diode current $I_D$ ($\text{A}$) to applied junction voltage $V_D$ ($\text{V}$), reverse saturation current $I_S$ ($\text{A}$), emission ideality factor $n \in [1, 2]$, and the thermal voltage $V_T = k_B T / q$ ($\approx 25.85\text{ mV}$ at $T = 300\text{ K}$). Under forward bias ($V_D \gg V_T$), the exponential term dominates unity and produces a slope of $\ln(10) n V_T \approx 59.5\text{ mV}$ per decade of current at room temperature ($n = 1$), whereas under reverse bias ($V_D < -4V_T$), current saturates at the tiny leakage floor $-I_S$.

Dividing $V_D$ by $n$ and $V_T$, exponentiating via `{{key:eˣ}}`, subtracting $1$, and multiplying by $I_S$ (`VD {{key:ENTER}} n {{key:÷}} VT {{key:÷}} {{key:eˣ}} 1 {{key:-}} IS {{key:×}}`) for a silicon junction ($I_S = 1.0 \times 10^{-12}\text{ A}, V_D = 0.650\text{ V}, n = 1.0, V_T = 0.02585\text{ V}$) gives `0.0832` $\text{A}$ ($83.25\text{ mA}$).

---

#### Operational Amplifier Closed-Loop Gain & $-3\text{ dB}$ Bandwidth
$$A_{v,\text{non}} = 1 + \frac{R_f}{R_g}, \quad A_{v,\text{inv}} = -\frac{R_f}{R_{\text{in}}}, \quad f_{-3\text{dB}} = \frac{\text{GBWP}}{A_{v,\text{non}}}$$
By applying Harold Stephen Black's 1927 negative-feedback principle to an operational amplifier with high open-loop differential gain $A_{\text{OL}} \gg 10^5$, a resistive voltage divider of feedback resistor $R_f$ ($\Omega$) and ground or input resistor $R_g, R_{\text{in}}$ ($\Omega$) forces the inverting input to track the non-inverting input, pinning closed-loop voltage gain solely to precision passive resistor ratios. Because dominant-pole internal compensation rolls off open-loop gain at $-20\text{ dB/decade}$ above the first pole, the product of closed-loop noise gain $A_{v,\text{non}}$ and $-3\text{ dB}$ bandwidth $f_{-3\text{dB}}$ remains constant at the amplifier's unity-gain bandwidth product $\text{GBWP}$ ($\text{Hz}$).

Computing $A_{v,\text{non}} = 1 + R_f / R_g$ first and dividing into $\text{GBWP}$ via `{{key:x⇄y}}` (`Rf {{key:ENTER}} Rg {{key:÷}} 1 {{key:+}} GBWP {{key:x⇄y}} {{key:÷}}`) for $R_f = 90\text{ k}\Omega, R_g = 10\text{ k}\Omega, \text{GBWP} = 10.0\text{ MHz}$ yields $A_{v,\text{non}} =$ `10.0000` ($20.0\text{ dB}$) and $f_{-3\text{dB}} =$ `1.0000` $\text{MHz}$.

---

#### Friis Free-Space RF Path Loss ($\text{FSPL}$)
$$\text{FSPL}_{\text{dB}} = 20\log_{10}\left(\frac{4\pi d f}{c}\right)$$
Derived by Harald Trap Friis at Bell Labs in 1946, the free-space path loss $\text{FSPL}_{\text{dB}}$ quantifies the ratio of transmitted to received power between two isotropic antennas separated by unobstructed line-of-sight distance $d$ ($\text{m}$) at carrier frequency $f$ ($\text{Hz}$) with vacuum light speed $c = 2.99792458 \times 10^8\text{ m/s}$ ($\lambda = c/f$). Physically, $(4\pi d / \lambda)^2$ combines two distinct factors: spherical wavefront spreading over area $4\pi d^2$ and the frequency-dependent effective capture aperture $A_e = \lambda^2 / (4\pi)$ of an isotropic reference dipole—explaining why doubling either link distance $d$ or carrier frequency $f$ adds $6.02\text{ dB}$ of attenuation between isotropic antennas.

Multiplying $4\pi d f$, dividing by $c$, taking `{{key:LOG}}`, and scaling by $20$ (`4 {{key:π}} {{key:×}} d {{key:×}} f {{key:×}} 2.99792458 {{key:E}} 8 {{key:÷}} {{key:LOG}} 20 {{key:×}}`) for $d = 1,000\text{ m}$ ($1\text{ km}$) at $f = 2.40 \times 10^9\text{ Hz}$ ($2.4\text{ GHz}$) yields `100.0520` $\text{dB}$.

---

#### Amdahl's Law Multiprocessor Speedup & CMOS Dynamic Power
$$S(N) = \frac{1}{(1 - p) + \frac{p}{N}}, \quad P_{\text{dyn}} = \alpha C V_{DD}^2 f$$
Gene Amdahl demonstrated in 1967 that if a fraction $p \in [0, 1]$ of a program's execution time can be parallelized across $N$ processor cores while the remaining serial fraction $(1 - p)$ must execute sequentially, overall speedup $S(N)$ is bounded above by the serial ceiling $S(\infty) = 1 / (1 - p)$ regardless of how many cores are added. Simultaneously, because synchronous CMOS gates charge and discharge load capacitance $C$ ($\text{F}$) at clock frequency $f$ ($\text{Hz}$) and switching activity factor $\alpha$, dynamic power $P_{\text{dyn}} = \alpha C V_{DD}^2 f$ grows quadratically with supply voltage $V_{DD}$ ($\text{V}$)—driving modern architectures to scale performance via parallel cores at reduced $V_{DD}$ and $f$ rather than pushing single-core clock rates.

Evaluating `p {{key:ENTER}} N {{key:÷}} 1 {{key:ENTER}} p {{key:-}} {{key:+}} {{key:1/x}}` for Amdahl speedup (or `VDD {{key:x²}} alpha {{key:×}} C {{key:×}} f {{key:×}}` for CMOS power) at $p = 0.90$ ($90\%$ parallelizable) and $N = 16\text{ cores}$ gives $S(16) =$ `6.4000` $\times$ speedup (asymptotic ceiling $S(\infty) = 10.0\times$).

---

## Stack Optimization Idioms, Solver Templates & Boundary Guards

Fluency on the SC-32 comes from recognizing recurring mathematical forms and applying dedicated hardware keys to minimize button presses and eliminate redundant variable stores.

### The Harmonic Mean Idiom (Parallel Operator)
The SC-32 provides a dedicated primary key `{{key:x∥y}}` which calculates:
$$X = \frac{X \cdot Y}{X + Y} = \frac{1}{\frac{1}{X} + \frac{1}{Y}}$$
In algebraic calculators, entering a reciprocal sum requires 12 to 16 keystrokes with fractions and parentheses. On the SC-32, it takes one keystroke:
* **Parallel Resistors:** $R_{\text{eq}} = R_1 \parallel R_2 \parallel R_3$ $\rightarrow$ `R1 {{key:ENTER}} R2 {{key:x∥y}} R3 {{key:x∥y}}`.
* **Series Capacitors:** $C_{\text{eq}} = C_1 \parallel C_2$ $\rightarrow$ `C1 {{key:ENTER}} C2 {{key:x∥y}}`.
* **Thin Lens Optics:** Focal length $f = d_o \parallel d_i$ $\rightarrow$ `do {{key:ENTER}} di {{key:x∥y}}`.
* **Spring Series Compliance:** $k_{\text{eq}} = k_1 \parallel k_2$ $\rightarrow$ `k1 {{key:ENTER}} k2 {{key:x∥y}}`.
* **Reduced Mass in Two-Body Problem:** $\mu = m_1 \parallel m_2$ $\rightarrow$ `m1 {{key:ENTER}} m2 {{key:x∥y}}`.

### The Difference-of-Squares Idiom
When evaluating expressions of the form $\sqrt{c^2 - a^2}$ (such as Pythagorean legs $b = \sqrt{c^2 - a^2}$ or numerical aperture $NA = \sqrt{n_1^2 - n_2^2}$):
* **Traditional RPN:** `c {{key:x²}} a {{key:x²}} {{key:-}} {{key:√x}}` (6 keystrokes).
* **Single-Entry Stack Factoring Idiom:** `c {{key:ENTER}} {{key:ENTER}} a {{key:-}} {{key:x⇄y}} {{key:LASTX}} {{key:+}} {{key:×}} {{key:√x}}`. Entering multi-digit operands $c$ and $a$ only once and factoring $\sqrt{(c-a)(c+a)}$ via `{{key:x⇄y}}` and `{{key:LASTX}}` avoids re-typing and prevents catastrophic cancellation when $c \approx a$.

### Constant Factor Replication in Register T
When evaluating a formula with a repeated scalar factor $K$ across multiple inputs (such as converting feet to meters with $0.3048$, or applying a $1.0825$ sales-tax factor):
1. Fill all four stack registers: `1.0825 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}` ($X, Y, Z, T$).
2. Price 1: `10 {{key:×}}` $\rightarrow$ $10.825$; Register $T$ drops into $Z$ while duplicating $1.0825$ in $T$.
3. Price 2: `{{key:CLx}} 25 {{key:×}}` $\rightarrow$ $27.0625$; `{{key:CLx}}` disables stack lift so `25` overwrites $X$ and $T$ feeds $1.0825$ downward on every `{{key:×}}` without `{{key:STO}}`/`{{key:RCL}}`.

### Numerical Root-Finding and Quadrature Function Selector

The SC-32 provides root-finding via Richard Brent's hybrid algorithm (`{{key:SOLVE}}`) and adaptive Romberg quadrature (`{{key:∫}}`) across equations stored in the 24-slot Equation Bank (`{{key:EQN}}`, labeled `A`–`Z`):

1. **User Equations (`{{key:EQN}}`):** Enter or select an RPN expression in `{{key:EQN}}`, stage initial guesses or integration limits $[a, b]$ in Registers $Y$ and $X$ (`a {{key:ENTER}} b`, or seed the target variable via `{{key:STO}}`), and press `{{key:SOLVE}}` or `{{key:∫}}` followed by the equation label (`A`–`Z`) and variable softkey (`X`, `T`, etc.).
2. **Closed-Form Polynomials (`{{key:POLY}}`):** For quadratics $Ax^2 + Bx + C = 0$ (`0 {{key:D}}`) and cubics $Ax^3 + Bx^2 + Cx + D = 0$, press `{{key:POLY}}` (`{{key:↱}}` + `{{key:XEQ}}`), load coefficients `A`–`D`, and tap `EXEC` to compute all real and complex conjugate roots in closed form (stored in indirect registers `R34`–`R39`).
3. **Brent Solver (`{{key:SOLVE}}`):** Pushes the converged root $x^*$ onto Register $X$ while lifting prior stack registers into $Y, Z, T$ (`{{key:STO}} X` followed by `{{key:XEQ}}` audits the residual $f(x^*)$).
4. **Romberg Quadrature (`{{key:∫}}`):** With integration limits $[a, b]$ in $(Y, X)$, returns the definite integral $\int_a^b f(x)\,dx$ in Register $X$ and the Richardson error estimate $\lvert\epsilon\rvert$ in Register $Y$.

### Storing Physical Constants & Numerical Boundary Guards

Mathematical invariants ($\pi$ via `{{key:π}}` and $e$ via `1 {{key:eˣ}}`) are hardcoded in firmware. Exact 2019 SI defined constants ($h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}$, $c = 2.99792458 \times 10^8\text{ m/s}$, $e = 1.602176634 \times 10^{-19}\text{ C}$, $k_B = 1.380649 \times 10^{-23}\text{ J/K}$, $R = 8.314462618\text{ J/(mol}\cdot\text{K)}$, $N_A = 6.02214076 \times 10^{23}\text{ mol}^{-1}$) and CODATA 2022 constants ($G, \varepsilon_0, \mu_0$) are keyed via `{{key:E}}` or stored into the 26 non-volatile registers (`{{key:STO}} A`–`Z`) for recall (`{{key:RCL}} C`, `{{key:RCL}} H`, `{{key:RCL}} R`).

* **Scientific Exponent Syntax:** Use `{{key:E}}` (`1.602176634 {{key:E}} 19 {{key:+/-}}` enters one atomic value in $X$), never `{{key:×}} 10 {{key:yˣ}}`.
* **Angular Modes:** Surveying, navigation, and Snell's law require Degrees (`{{key:MODES}} {{key:DEG}}`); calculus and Fourier formulas require Radians (`{{key:MODES}} {{key:RAD}}`).
* **Singularity Guards:** Division by zero ($x/0$ or $\ln 0$) shows `DIVIDE BY 0` (Code 01), and $\sqrt{-x}$ in Real mode shows `INVALID DATA` (Code 02; in `{{key:CMPLX}}`, $\sqrt{-x}$ returns $i\sqrt{x}$ across $Y, X$). Press `{{key:C}}` or `{{key:<-}}` to dismiss without losing stack state.

