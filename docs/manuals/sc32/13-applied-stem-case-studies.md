---
title: "Chapter 13: Applied STEM Engineering Case Studies | SC-32 Manual"
description: "Comprehensive publication-grade engineering case studies across fluid dynamics, thermodynamics, audio crossovers, optical matrices, geodesy, orbital mechanics, beam deflection, and chemical kinetics on the StackCalc SC-32."
---

# Chapter 13: Applied STEM Engineering Case Studies

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 ENGINEERING LABS // APPLIED STEM CASE STUDIES</span>
  <span class="te-viewport-status text-sky-400">● 100% UNIT TEST VERIFIED &bull; ADDITIVE MANUFACTURING &bull; ACOUSTICS &bull; GEODESY &bull; ORBITS</span>
</div>

---

## The Chief Engineer's Pocket Notebook: The Physical Reality of G-Forces, Thermal Expansion, and Tolerance Stacks

Before the advent of ubiquitous laptop CAD suites and cloud finite-element solvers, the hallmark of the master engineer was a leather-bound pocket notebook paired with a precision handheld calculator. Whether standing beneath the roaring cryogenic test stand of the Saturn V at Rocketdyne, walking the catwalk of a high-temperature ethylene cracking plant, or sighting through a theodolite across an alpine triangulation ridge, the chief engineer understood a fundamental truth: physical reality does not wait for a simulation grid to mesh.

In the physical world, thermal expansion shears bolts that look adequate on paper. Non-Newtonian shear thinning clogs micro-extrusion nozzles in additive manufacturing. High-frequency RF phase angles destroy amplifier efficiency if line impedances mismatch by even a few milliohms. In these critical environments, the StackCalc SC-32 serves not merely as an arithmetic tool, but as a live tactile flight deck for dimensional verification and physical intuition.

Every case study in this chapter is taken from authentic field engineering practice—from the fluid dynamics of melted thermoplastic beads in precision 3D printing to Hohmann orbital transfers, Romberg quadrature of rocket burnout velocities, and geodetic azimuth closures. By structuring physical equations into lean, parenthesis-free RPN operational stacks, you preserve intermediate variables directly in physical registers, ensuring that numbers never lose their connection to physical dimensions, forces, and material limits.

{{blocks:planetary_geared_clock_330|Planetary Gear Train and Mechanical Kinematics Blueprint}}
*Figure 13.1: Mechanical kinematics and planetary gear train architecture: precision mechanical reduction, torque transmission, and physical tolerance stacks calculated in real time.*

{{res:sc32_thin_lens:screenshot|Thin lens focal length 1/f = 1/30 + 1/60 solved via [x||y] -> 20.0000}}

<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>CASE STUDY BASELINE MODES:</strong><br>
  • <strong>Cases 1–2 (Fluids &amp; Thermodynamics):</strong> <code>{{key:ALL}}</code> (Standard scientific mantissa, base-10 arithmetic).<br>
  • <strong>Case 3 (Audio Engineering &amp; RF Filters):</strong> <code>{{key:RAD}}</code> (Radians angular mode for complex filter phasors).<br>
  • <strong>Case 4 (Optical Engineering):</strong> <code>{{key:ALL}}</code> (Parallel harmonic key <code>{{key:x∥y}}</code>).<br>
  • <strong>Case 5 (Civil Surveying &amp; Geodesy):</strong> <code>{{key:DEG}}</code> (Degrees angular mode for field azimuths).<br>
  • <strong>Case 6 (Orbital Mechanics &amp; Astrodynamics):</strong> <code>{{key:RAD}}</code> (Radians angular mode for orbital flight dynamics).<br>
  • <strong>Cases 7–10 (Structural, Nuclear, Chemical, Geotech, Acoustics):</strong> <code>{{key:ALL}}</code>.
</div>

## Engineering Design Briefing: The Chief Engineer's Master Case Studies


<div class="admonition warning">
<p class="admonition-title">The Algebraic Parenthesis Trap vs. The RPN Stack Shortcut: Multidisciplinary STEM Pipelines</p>
<p><strong>The Algebraic Parenthesis Trap:</strong> In multidisciplinary field engineering—whether evaluating the Rocket Tsiolkovsky delta-V equation $\Delta v = v_e \ln(m_0/m_f)$, Gaussian thin lens combinations $\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$, or Euler column buckling loads $P_{\text{cr}} = \frac{\pi^2 E I}{L^2}$—an algebraic calculator forces the practitioner into an unnatural syntax ritual {{cite:munroe2014,parker2019}}:</p>
<pre><code>P_cr = ( 3.14159 ^ 2 * ( 200 * 10 ^ 9 ) * ( 4.85 * 10 ^ -6 ) ) / ( 6.5 ^ 2 )</code></pre>
<p>Every parenthesis level introduces mental friction. If a field engineer drops an exponent grouping or misplaces a sign while standing on a construction scaffolding or at an engine test stand, the calculation silently diverges by orders of magnitude or crashes with a syntax fault {{cite:sweller1988,miller1956}}.</p>
<p><strong>The RPN Stack Shortcut:</strong> On the StackCalc SC-32, physical systems map directly to the 4-register operational stack ($X, Y, Z, T$) with zero parentheses {{cite:hp15c1982,hp32sii1991}}. The engineer computes parameters from the inside out: structural area moment $I$ is multiplied by elastic modulus $E$ in place; $\pi^2$ scales the numerator directly in Register $X$; and dividing by the squared column length $L^2$ resolves the critical load in a single keystroke. For parallel impedances or optical thin lens conjugates, the dedicated harmonic operator <code>{{key:x∥y}}</code> compresses 12 algebraic button presses into a single tactile stroke {{cite:horowitz2015}}.</p>
</div>

---

## Case Study 1: Fluid Mechanics & 3D Printing Extrusion Dynamics

In additive manufacturing, print failures, skipped extruder steps, and layer delamination occur when the volumetric melt capacity of the hotend heater block is exceeded.

<div class="admonition note">
<p class="admonition-title">Hotend Extrusion Bead Fluid Dynamics Model</p>

| Extrusion Parameter | Symbol & Formula | Verified Value |
| :--- | :--- | :--- |
| **Line Width** | $w$ | $0.45\text{ mm}$ |
| **Layer Height** | $h$ | $0.20\text{ mm}$ |
| **Cross-Sectional Bead Area** | $A = w \times h = 0.45 \times 0.20$ | $0.09\text{ mm}^2$ |
| **Printhead Linear Velocity** | $v$ | $180\text{ mm/s}$ |
| **Volumetric Flow Rate** | $\dot{Q} = A \times v = 0.09 \times 180$ | **$16.2\text{ mm}^3\text{/s}$** |
</div>

### Problem 1.1: Volumetric Melt Flow Rate Threshold
A 3D printer equipped with a nominal $0.40\text{ mm}$ brass nozzle deposits lines at a sliced width $w = 0.45\text{ mm}$ and layer height $h = 0.20\text{ mm}$ at print speed $v = 180.0\text{ mm/s}$. Determine if this exceeds the hotend maximum volumetric flow threshold $\dot{Q}_{\max} = 16.2\text{ mm}^3/\text{s}$:
$$\dot{Q} = w \times h \times v = 0.45 \times 0.20 \times 180.0$$

#### Keystrokes:
`{{res:sc32_13_applied_stem_case_studies_seq_03:keys}}` $\rightarrow$ **`{{res:sc32_13_applied_stem_case_studies_seq_03:value}}`**.

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .45 {{key:ENTER}} | 0.00 | 0.00 | 0.450000 | 0.450000 | 0.450000_ |
| 02 | .20 {{key:×}} | 0.00 | 0.00 | 0.00 | 0.090000 | 0.090000 |
| 03 | 180 {{key:×}} | 0.00 | 0.00 | 0.00 | 16.200000 | 16.200000 |

---

### Problem 1.2: Maximum Permissible Print Speed Inversion
Given a hotend volumetric flow limit of $\dot{Q} = 16.2\text{ mm}^3/\text{s}$, line width $w = 0.45\text{ mm}$, and layer height $h = 0.20\text{ mm}$, determine the maximum permissible linear speed:
$$v_{\max} = \frac{\dot{Q}}{w \times h} = 16.2 \div 0.45 \div 0.20 = \mathbf{180.0\text{ mm/s}}$$

#### Keystrokes:
`{{res:sc32_13_applied_stem_case_studies_seq_04:keys}}` $\rightarrow$ **`{{res:sc32_13_applied_stem_case_studies_seq_04:value}}`**.

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 16.2 {{key:ENTER}} | 0.00 | 0.00 | 16.200000 | 16.200000 | 16.200000_ |
| 02 | .45 {{key:÷}} | 0.00 | 0.00 | 0.00 | 36.000000 | 36.000000 |
| 03 | .20 {{key:÷}} | 0.00 | 0.00 | 0.00 | 180.000000 | 180.000000 |

---

### Problem 1.3: Filament Part Mass & Feeder Drive Linear Speed
A technical instrument enclosure has solid volume $V = 125.0\text{ cm}^3$ ($125,000\text{ mm}^3$). Using technical PLA with density $\rho = 1.24\text{ g/cm}^3$:
1. Total part mass: $m = 125 \times 1.24 = \mathbf{155.0\text{ grams}}$.
2. Standard $1.75\text{ mm}$ filament (radius $r = 0.875\text{ mm}$) has cross-sectional area:
   $$A_f = \pi r^2 = \pi \times 0.875^2 \approx 2.405282\text{ mm}^2$$
3. Linear feed velocity $v_f$ of the extruder drive gear at maximum flow ($16.2\text{ mm}^3/\text{s}$):
   $$v_f = \frac{\dot{Q}}{A_f} = \frac{16.2}{\pi \times 0.875^2} \approx \mathbf{6.735177\text{ mm/s}}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 16.2 {{key:ENTER}} | 0.00 | 0.00 | 16.200000 | 16.200000 | 16.200000_ |
| 02 | .875 {{keycap:x²}} | 0.00 | 16.200000 | 16.200000 | 0.765625 | 0.765625 |
| 03 | {{keycap:π}} {{key:×}} | 0.00 | 0.00 | 16.200000 | 2.405282 | 2.405282 |
| 04 | {{key:÷}} | 0.00 | 0.00 | 0.00 | 6.735177 | 6.735177 |

---

### Problem 1.4: Torricelli Efflux Tank Draining Velocity

A cylindrical fluid storage tank maintains an open liquid column height $h = 5.0\text{ meters}$. Standard acceleration of gravity $g = 9.80665\text{ m/s}^2$. Determine the efflux velocity $v$:
$$v = \sqrt{2 g h} = \sqrt{2 \times 9.80665 \times 5.0} = \sqrt{98.0665} \approx \mathbf{9.90285\text{ m/s}}$$

#### Keystrokes:
`{{res:sc32_13_applied_stem_case_studies_seq_05:keys}}` $\rightarrow$ **`{{res:sc32_13_applied_stem_case_studies_seq_05:value}}`**.

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 2 {{key:ENTER}} | 0.00 | 0.00 | 2.000000 | 2.000000 | 2.000000_ |
| 02 | 9.80665 {{key:×}} | 0.00 | 0.00 | 0.00 | 19.613300 | 19.613300 |
| 03 | 5 {{key:×}} | 0.00 | 0.00 | 0.00 | 98.066500 | 98.066500 |
| 04 | {{key:√x}} | 0.00 | 0.00 | 0.00 | 9.902853 | 9.902853 |

---

### Problem 1.5: Darcy-Weisbach Friction Head Loss in Piping
Water at $20^\circ\text{C}$ flows at velocity $v = 2.40\text{ m/s}$ through a commercial steel pipe with length $L = 85.0\text{ m}$ and inner diameter $D = 0.15\text{ m}$. Darcy friction factor $f = 0.0192$:
$$h_f = f \frac{L}{D} \frac{v^2}{2g} = 0.0192 \times \frac{85.0}{0.15} \times \frac{2.40^2}{2 \times 9.80665} \approx \mathbf{3.1977\text{ meters}}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .0192 {{key:ENTER}} | 0.00 | 0.00 | 0.019200 | 0.019200 | 0.019200_ |
| 02 | 85 {{key:×}} .15 {{key:÷}} | 0.00 | 0.00 | 0.00 | 10.880000 | 10.880000 |
| 03 | 2.4 {{keycap:x²}} {{key:×}} | 0.00 | 0.00 | 0.00 | 62.668800 | 62.668800 |
| 04 | 2 {{key:÷}} 9.80665 {{key:÷}} | 0.00 | 0.00 | 0.00 | 3.197693 | 3.197693 (m) |

---

### Problem 1.6: Infill Grid Volume Integration & Spool Consumption
A rectangular drone chassis housing has outer bounding box dimensions $140\text{ mm} \times 90\text{ mm} \times 35\text{ mm}$. The part is sliced with 3 solid perimeter walls ($2.0\text{ mm}$ thick) consuming $85,000\text{ mm}^3$, while the internal cavity ($355,000\text{ mm}^3$) is filled with a $25\%$ gyroid infill density ($\rho_{\text{infill}} = 0.25$). Technical polymer density is $\rho = 1.25\text{ g/cm}^3$ ($0.00125\text{ g/mm}^3$):
$$V_{\text{total}} = V_{\text{walls}} + \rho_{\text{infill}} \times V_{\text{cavity}} = 85,000 + (0.25 \times 355,000) = 85,000 + 88,750 = \mathbf{173,750\text{ mm}^3}$$
$$M_{\text{part}} = V_{\text{total}} \times \rho = 173,750 \times 0.00125 \approx \mathbf{217.19\text{ grams}}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 355000 {{key:ENTER}} | 0.00 | 0.00 | 355000.0 | 355000.0 | 355000.0_ |
| 02 | .25 {{key:×}} | 0.00 | 0.00 | 0.00 | 88750.00 | 88750.00 |
| 03 | 85000 {{key:+}} | 0.00 | 0.00 | 0.00 | 173750.0 | 173750.0(mm³) |
| 04 | .00125 {{key:×}} | 0.00 | 0.00 | 0.00 | 217.1875 | 217.19 (g) |

---

### Problem 1.7: Extruder Stepper Motor Pulse Rate
The extruder drive gear has an effective calibration constant of $415.0\text{ steps/mm}$. At the maximum volumetric feed velocity $v_f = 6.735177\text{ mm/s}$ (derived in Problem 1.3), determine the command step pulse frequency $f_{\text{step}}$:
$$f_{\text{step}} = v_f \times \text{steps/mm} = 6.735177 \times 415.0 \approx \mathbf{2,795.10\text{ Hz}}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 6.735177{{key:ENTER}} | 0.00 | 0.00 | 6.735177 | 6.735177 | 6.735177_ |
| 02 | 415.0 {{key:×}} | 0.00 | 0.00 | 0.00 | 2795.0985 | 2795.10 (Hz) |

---

{{blocks:clock_gear_stages_macro|Precision Machined Gear Stages and Mechanical Tolerances}}
*Figure 13.2: Macro view of precision machined mechanical gear stages: high-stress tooth profiles and thermal expansion clearances verified against field calculations.*


## Case Study 2: Thermodynamics & Heat Transfer

### Problem 2.1: Carnot Heat Engine Efficiency Upper Bound
Calculate maximum theoretical thermodynamic efficiency of a geothermal binary power plant operating between vapor temperature $T_H = 185^\circ\text{C}$ and cooling water sink $T_C = 22^\circ\text{C}$:
$$T_H = 185 + 273.15 = 458.15\text{ K}, \quad T_C = 22 + 273.15 = 295.15\text{ K}$$
$$\eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H} = 1 - \frac{295.15}{458.15} = 0.355778 \quad (\mathbf{35.58\%})$$

#### Keystrokes:
`{{res:sc32_13_applied_stem_case_studies_seq_02:keys}}` $\rightarrow$ **`{{res:sc32_13_applied_stem_case_studies_seq_02:value}}`**.

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 22 273.15 {{key:+}} | 0.00 | 0.00 | 0.00 | 295.150000 | 295.150000 |
| 02 | 185 273.15 {{key:+}} | 0.00 | 0.00 | 295.150000 | 458.150000 | 458.150000 |
| 03 | {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.644221 | 0.644221 |
| 04 | 1 {{key:x⇄y}} {{key:-}} | 0.00 | 0.00 | 0.00 | 0.355778 | 0.355778 |

---

### Problem 2.2: Ideal Brayton Gas Turbine Cycle Thermal Efficiency
An industrial gas turbine operates on the ideal Brayton cycle with compressor pressure ratio $r_p = 14.5$ and air specific heat ratio $\gamma = 1.40$:
$$\eta_{\text{Brayton}} = 1 - \frac{1}{r_p^{(\gamma - 1)/\gamma}} = 1 - \frac{1}{(14.5)^{(0.40/1.40)}} \approx \mathbf{53.41\%}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 14.5 {{key:ENTER}} | 0.00 | 0.00 | 14.500000 | 14.500000 | 14.500000_ |
| 02 | .40 1.40 {{key:÷}} | 0.00 | 14.500000 | 14.500000 | 0.285714 | 0.285714 |
| 03 | {{key:yˣ}} {{key:1/x}} | 0.00 | 0.00 | 0.00 | 0.465870 | 0.465870 |
| 04 | 1 {{key:x⇄y}} {{key:-}} | 0.00 | 0.00 | 0.00 | 0.534130 | 0.534130 |

---

### Problem 2.3: Counterflow Heat Exchanger Log-Mean Temperature Difference (LMTD)
A counterflow shell-and-tube heat exchanger cools lube oil from $T_{h1} = 120^\circ\text{C}$ to $T_{h2} = 65^\circ\text{C}$ using cooling water entering at $T_{c1} = 20^\circ\text{C}$ and exiting at $T_{c2} = 45^\circ\text{C}$.
$$\Delta T_1 = T_{h1} - T_{c2} = 120 - 45 = 75^\circ\text{C}$$
$$\Delta T_2 = T_{h2} - T_{c1} = 65 - 20 = 45^\circ\text{C}$$
$$\text{LMTD} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)} = \frac{75 - 45}{\ln(75 / 45)} = \frac{30}{\ln(1.666667)} \approx \mathbf{58.73^\circ\text{C}}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 75 {{key:ENTER}} | 0.00 | 0.00 | 75.000000 | 75.000000 | 75.000000_ |
| 02 | 45 {{key:ENTER}} | 0.00 | 75.000000 | 45.000000 | 45.000000 | 45.000000_ |
| 03 | {{key:-}} | 0.00 | 0.00 | 0.00 | 30.000000 | 30.000000 |
| 04 | 75 45 {{key:÷}} LN | 0.00 | 0.00 | 30.000000 | 0.510826 | 0.510826 |
| 05 | {{key:÷}} | 0.00 | 0.00 | 0.00 | 58.728461 | 58.728461(°C) |

---

### Problem 2.4: Composite Wall Conduction Heat Flux
A furnace wall consists of $L_1 = 0.15\text{ m}$ firebrick ($k_1 = 1.2\text{ W/m}\cdot\text{K}$) and $L_2 = 0.05\text{ m}$ insulating mineral wool ($k_2 = 0.04\text{ W/m}\cdot\text{K}$). Inner temperature $T_{\text{in}} = 850^\circ\text{C}$, outer temperature $T_{\text{out}} = 50^\circ\text{C}$:
$$R_{\text{total}} = \frac{L_1}{k_1} + \frac{L_2}{k_2} = \frac{0.15}{1.2} + \frac{0.05}{0.04} = 0.125 + 1.250 = \mathbf{1.375\text{ m}^2\text{K/W}}$$
$$q'' = \frac{\Delta T}{R_{\text{total}}} = \frac{850 - 50}{1.375} = \frac{800}{1.375} \approx \mathbf{581.82\text{ W/m}^2}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .15 1.2 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.125000 | 0.125000 |
| 02 | .05 .04 {{key:÷}} | 0.00 | 0.00 | 0.125000 | 1.250000 | 1.250000 |
| 03 | {{key:+}} | 0.00 | 0.00 | 0.00 | 1.375000 | 1.375000 |
| 04 | 850 50 {{key:-}} | 0.00 | 0.00 | 1.375000 | 800.000000 | 800.000000 |
| 05 | {{key:x⇄y}} {{key:÷}} | 0.00 | 0.00 | 0.00 | 581.818182 | 581.82(W/m²) |

---

### Problem 2.5: Rankine Steam Power Cycle Thermal Efficiency
In a subcritical Rankine steam cycle, high-pressure steam enters the turbine at enthalpy $h_1 = 3,450.0\text{ kJ/kg}$ and expands to condenser pressure with enthalpy $h_2 = 2,180.0\text{ kJ/kg}$. The feedwater pump consumes work $w_p = 15.0\text{ kJ/kg}$ to pressurize liquid from $h_3 = 190.0\text{ kJ/kg}$ to boiler inlet state $h_4 = 205.0\text{ kJ/kg}$.
1. Net turbine work output:
   $$w_{\text{net}} = (h_1 - h_2) - w_p = (3450.0 - 2180.0) - 15.0 = 1270.0 - 15.0 = \mathbf{1,255.0\text{ kJ/kg}}$$
2. Heat input supplied by the boiler:
   $$q_{\text{in}} = h_1 - h_4 = 3450.0 - 205.0 = \mathbf{3,245.0\text{ kJ/kg}}$$
3. Thermal efficiency:
   $$\eta_{\text{Rankine}} = \frac{w_{\text{net}}}{q_{\text{in}}} = \frac{1255.0}{3245.0} \approx \mathbf{38.67\%}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 3450 2180 {{key:-}} | 0.00 | 0.00 | 0.00 | 1270.0000 | 1270.0000 |
| 02 | 15 {{key:-}} | 0.00 | 0.00 | 0.00 | 1255.0000 | 1255.0000 |
| 03 | 3450 205 {{key:-}} | 0.00 | 0.00 | 1255.0000 | 3245.0000 | 3245.0000 |
| 04 | {{key:÷}} 100 {{key:×}} | 0.00 | 0.00 | 0.00 | 38.674884 | 38.67 (%) |

---

### Problem 2.6: Otto Cycle Internal Combustion Efficiency vs. Compression Ratio
The theoretical thermal efficiency of an internal combustion Otto cycle engine depends solely on compression ratio $r = V_{\max} / V_{\min}$ and air specific heat ratio $\gamma = 1.40$:
$$\eta_{\text{Otto}} = 1 - \frac{1}{r^{\gamma - 1}}$$
For a high-performance racing engine with compression ratio $r = 11.5$:
$$\eta_{\text{Otto}} = 1 - \frac{1}{11.5^{0.40}} = 1 - \frac{1}{2.65839} = 1 - 0.376167 = \mathbf{62.38\%}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 11.5 {{key:ENTER}} | 0.00 | 0.00 | 11.500000 | 11.500000 | 11.500000_ |
| 02 | .40 {{key:yˣ}} | 0.00 | 0.00 | 0.00 | 2.658390 | 2.658390 |
| 03 | {{key:1/x}} | 0.00 | 0.00 | 0.00 | 0.376167 | 0.376167 |
| 04 | 1 {{key:x⇄y}} {{key:-}} | 0.00 | 0.00 | 0.00 | 0.623833 | 0.623833(62%) |

---

## Case Study 3: Audio Engineering & Crossover Networks

### Problem 3.1: 2nd-Order Butterworth Crossover Filters
Crossover frequency $f_c = 2500\text{ Hz}$, driver nominal impedance $R = 8.0\,\Omega$:
$$L = \frac{R \sqrt{2}}{2\pi f_c} = \frac{8 \sqrt{2}}{2\pi \times 2500} \approx \mathbf{0.720253\text{ mH}}$$
$$C = \frac{1}{2\pi \sqrt{2} R f_c} = \frac{1}{2\pi \sqrt{2} \times 8 \times 2500} \approx \mathbf{5.62698\text{ }\mu\text{F}}$$

#### Stack Trace Table (Inductor $L$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 8 {{key:ENTER}} 2 {{key:√x}} {{key:×}} | 0.00 | 0.00 | 8.000000 | 11.313708 | 11.313708 |
| 02 | 2 {{key:÷}} | 0.00 | 0.00 | 0.00 | 5.656854 | 5.656854 |
| 03 | {{keycap:π}} {{key:÷}} | 0.00 | 0.00 | 0.00 | 1.800633 | 1.800633 |
| 04 | 2500 {{key:÷}} | 0.00 | 0.00 | 0.00 | 7.2025E-4 | 7.20253E-4(H) |

---

### Problem 3.2: 4th-Order Linkwitz-Riley Crossover ($24\text{ dB/octave}$)
For $f_c = 2500\text{ Hz}, R = 8.0\,\Omega$:
$$L_{LR4} = \frac{R}{\pi f_c} = \frac{8.0}{\pi \times 2500} \approx \mathbf{1.01859\text{ mH}}$$
$$C_{LR4} = \frac{1}{4\pi R f_c} = \frac{1}{4\pi \times 8.0 \times 2500} \approx \mathbf{3.97887\text{ }\mu\text{F}}$$

#### Stack Trace Table (Capacitor $C_{LR4}$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 4 {{key:ENTER}} π {{key:×}} | 0.00 | 0.00 | 4.000000 | 12.566371 | 12.566371 |
| 02 | 8 {{key:×}} 2500 {{key:×}} | 0.00 | 0.00 | 0.00 | 251327.41 | 251327.41 |
| 03 | {{key:1/x}} | 0.00 | 0.00 | 0.00 | 3.97887E-6 | 3.97887E-6(F) |

---

### Problem 3.3: Parallel Speaker Driver Impedance Matching via `{{key:x∥y}}`
An $8.0\,\Omega$ mid-bass woofer is wired in parallel with a $16.0\,\Omega$ subwoofer driver:
$$Z_{\text{eq}} = 8 \parallel 16 = \frac{8 \times 16}{8 + 16} = \frac{128}{24} = \mathbf{5.333333\,\Omega}$$
Chained load ($8\,\Omega \parallel 8\,\Omega \parallel 4\,\Omega$): `{{res:sc32_13_applied_stem_case_studies_seq_06:keys}}` $\rightarrow$ **`{{res:sc32_13_applied_stem_case_studies_seq_06:value}}`**.

> **Named RPN Stack Idiom: *The Parallel Reciprocal x∥y Shortcut*** — Cascade parallel acoustic impedances and driver voice coils in a single continuous stream without reciprocal intermediate storage {{cite:horowitz2015,hp32sii1991}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `8` `{{key:ENTER}}` — Enter first parallel speaker driver voice coil impedance ($8.0\,\Omega$) into Register $Y$.
2. `8` `{{key:x∥y}}` — Combine second $8.0\,\Omega$ parallel driver using the harmonic operator to obtain the intermediate branch impedance ($4.0\,\Omega$).
3. `4` `{{key:x∥y}}` — Pipe the final $4.0\,\Omega$ low-frequency branch into the network; total parallel acoustic load evaluates to $\mathbf{2.0000\,\Omega}$.

#### Stack Trace Table:
| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 8 {{key:ENTER}} | 0.00 | 0.00 | 8.000000 | 8.000000 | First mid-bass driver impedance (8.0 Ω) entered into Y |
| 02 | 8 {{key:x∥y}} | 0.00 | 0.00 | 0.00 | 4.000000 | Parallel combination of two 8.0 Ω drivers yields 4.0 Ω |
| 03 | 4 {{key:x∥y}} | 0.00 | 0.00 | 0.00 | 2.000000 | Parallel combination with 4.0 Ω subwoofer yields 2.0 Ω load |

---

### Problem 3.4: Complex AC Impedance Addition via {{key:CMPLX}}
Branch 1 impedance $Z_1 = 8 + 4i\,\Omega$ ($Y = 8, X = 4$).  
Branch 2 impedance $Z_2 = 4 - 8i\,\Omega$ ($Y = 4, X = -8$).  
Total series impedance: $Z_{\text{total}} = (8 + 4i) + (4 - 8i) = \mathbf{12 - 4i\,\Omega}$.

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 4 {{key:ENTER}} 8 {{key:+/-}} 8 {{key:ENTER}} 4 | 4.00 | -8.00 | 8.00 | 4.00 | 4.00_ |
| 02 | {{key:CMPLX}}{{key:+}} | 0.00 | 0.00 | 12.000000 | -4.000000 | 12.00 -4.00i |

---

### Problem 3.5: Zobel Network Dynamic Impedance Equalizer
Dynamic loudspeaker voice coils exhibit rising inductive impedance at high frequencies ($Z(f) = R_e + j\omega L_e$). A Zobel network placed in parallel with the driver flattens the impedance back to pure resistance $R_e$:
$$R_z = 1.25 \times R_e, \quad C_z = \frac{L_e}{R_z^2}$$
For a woofer with DC voice coil resistance $R_e = 6.4\,\Omega$ and voice coil inductance $L_e = 0.85\text{ mH}$ ($0.00085\text{ H}$):
1. Zobel resistor: $R_z = 1.25 \times 6.4 = \mathbf{8.00\,\Omega}$.
2. Zobel capacitor:
   $$C_z = \frac{0.00085}{8.0^2} = \frac{0.00085}{64.0} \approx \mathbf{13.281\text{ }\mu\text{F}}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 6.4 {{key:ENTER}} | 0.00 | 0.00 | 6.400000 | 6.400000 | 6.400000_ |
| 02 | 1.25 {{key:×}} | 0.00 | 0.00 | 0.00 | 8.000000 | 8.000000 (Ω) |
| 03 | {{keycap:x²}} | 0.00 | 0.00 | 0.00 | 64.000000 | 64.000000 |
| 04 | .00085{{key:x⇄y}} {{key:÷}} | 0.00 | 0.00 | 0.00 | 1.3281E-5 | 1.32812E-5(F) |
| 05 | 1 {{key:E}} 6 {{key:×}} | 0.00 | 0.00 | 0.00 | 13.281250 | 13.28 (μF) |

---

### Problem 3.6: Bridged-T Audio Attenuator Network Pad
Design a $10.0\text{ dB}$ symmetrical $Z_0 = 600.0\,\Omega$ constant-impedance bridged-T attenuator pad for professional studio line levels:
1. Voltage attenuation ratio:
   $$K = 10^{\text{dB} / 20} = 10^{10 / 20} = 10^{0.50} \approx \mathbf{3.162278}$$
2. Bridged series resistor:
   $$R_1 = Z_0 (K - 1) = 600 \times (3.162278 - 1) = 600 \times 2.162278 \approx \mathbf{1,297.37\,\Omega}$$
3. Shunt grounded resistor:
   $$R_2 = \frac{Z_0}{K - 1} = \frac{600}{2.162278} \approx \mathbf{277.49\,\Omega}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 10 20 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.500000 | 0.500000 |
| 02 | 10 {{key:x⇄y}} {{key:yˣ}} | 0.00 | 0.00 | 0.00 | 3.162278 | 3.162278 (K) |
| 03 | 1 {{key:-}} | 0.00 | 0.00 | 0.00 | 2.162278 | 2.162278 |
| 04 | 600 {{key:ENTER}} | 0.00 | 0.00 | 2.162278 | 600.0000 | 600.0000_ |
| 05 | {{key:×}} | 0.00 | 0.00 | 0.00 | 1297.3666 | 1297.37 (Ω) |
| 06 | 600 2.1623 {{key:÷}} | 0.00 | 0.00 | 0.00 | 277.4851 | 277.49 (Ω) |

---

## Case Study 4: Optical Engineering & Lens Systems


### Problem 4.1: Thin Lens Focal Length via Harmonic Key `{{key:x∥y}}`
Gaussian lens formula: $\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i} \implies f = d_o \parallel d_i$.
Object distance $d_o = 30.0\text{ cm}$, real image distance $d_i = 60.0\text{ cm}$:
`{{res:sc32_13_applied_stem_case_studies_seq_07:keys}}` $\rightarrow$ **`{{res:sc32_13_applied_stem_case_studies_seq_07:value}}`**.

> **Named RPN Stack Idiom: *The Optical Conjugate Harmonic Shortcut*** — Evaluate thin-lens Gaussian conjugate distances $1/f = 1/d_o + 1/d_i$ using the single-cycle parallel harmonic key {{cite:horowitz2015}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `30` `{{key:ENTER}}` — Enter optical object distance ($d_o = 30.0\text{ cm}$) into Register $Y$.
2. `60` `{{key:x∥y}}` — Enter real image distance ($d_i = 60.0\text{ cm}$) and execute harmonic shortcut; effective lens focal length evaluates directly to $\mathbf{20.00\text{ cm}}$ in Register $X$.

#### Stack Trace Table:
| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 30 {{key:ENTER}} | 0.00 | 0.00 | 30.000000 | 30.000000 | Object distance d_o = 30.0 cm entered into Y |
| 02 | 60 {{key:x∥y}} | 0.00 | 0.00 | 0.00 | 20.000000 | Image distance d_i = 60.0 cm combined; f = 20.00 cm in X |

---

### Problem 4.2: Compound Two-Lens Microscope Magnification
Objective focal length $f_{\text{obj}} = 4.0\text{ mm}$, eyepiece focal length $f_{\text{eye}} = 25.0\text{ mm}$, optical tube length $L = 160.0\text{ mm}$, near point $N = 250.0\text{ mm}$:
$$M_{\text{total}} = M_{\text{obj}} \times M_{\text{eye}} = \left(\frac{L}{f_{\text{obj}}}\right) \times \left(\frac{N}{f_{\text{eye}}}\right) = \left(\frac{160}{4}\right) \times \left(\frac{250}{25}\right) = 40 \times 10 = \mathbf{400.0\text{x}}$$

#### Keystrokes:
`{{res:sc32_13_applied_stem_case_studies_seq_08:keys}}` $\rightarrow$ **`{{res:sc32_13_applied_stem_case_studies_seq_08:value}}`**.

> **Named RPN Stack Idiom: *The Multi-Stage Optical Magnification Cascade*** — Evaluate objective magnification and eyepiece ocular power in separate stack registers and multiply in place.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `160` `{{key:ENTER}} 4 {{key:÷}}` — Compute objective magnification from tube length ($160.0\text{ mm}$) and objective focal length ($4.0\text{ mm}$), yielding $M_{\text{obj}} = 40.0$ in Register $X$.
2. `250` `{{key:ENTER}} 25 {{key:÷}}` — Push standard near point ($250.0\text{ mm}$), elevating $40.0$ into $Y$, and divide by ocular focal length ($25.0\text{ mm}$) to yield ocular magnification $M_{\text{eye}} = 10.0$ in $X$.
3. `{{key:×}}` — Multiply objective and ocular factors; compound microscope power evaluates to $\mathbf{400.0\text{x}}$ without intermediate scratch storage.

#### Stack Trace Table:
| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 160 {{key:ENTER}} | 0.00 | 0.00 | 160.0000 | 160.0000 | Tube length L = 160.0 mm entered |
| 02 | 4 {{key:÷}} | 0.00 | 0.00 | 0.00 | 40.000000 | Objective magnification M_obj = 40.0x |
| 03 | 250 {{key:ENTER}} | 0.00 | 0.00 | 40.000000 | 250.0000 | Near point N = 250.0 mm entered, M_obj lifts to Y |
| 04 | 25 {{key:÷}} | 0.00 | 0.00 | 40.000000 | 10.000000 | Eyepiece magnification M_eye = 10.0x |
| 05 | {{key:×}} | 0.00 | 0.00 | 0.00 | 400.0000 | Compound microscope magnification M_total = 400.0x |

---

### Problem 4.3: Snell's Law & Total Internal Reflection Critical Angle
Light propagates from optical glass ($n_1 = 1.52$) into air ($n_2 = 1.00$). Determine the critical angle $\theta_c$:
$$\theta_c = \arcsin\left(\frac{n_2}{n_1}\right) = \arcsin\left(\frac{1.00}{1.52}\right) = \arcsin(0.657895) \approx \mathbf{41.14^\circ}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 1 {{key:ENTER}} | 0.00 | 0.00 | 1.000000 | 1.000000 | 1.000000_ |
| 02 | 1.52 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.657895 | 0.657895 |
| 03 | {{key:ASIN}} | 0.00 | 0.00 | 0.00 | 41.139502 | 41.14 (°) |

---

### Problem 4.4: Numerical Aperture & Light Acceptance Angle of Optical Fiber
A multi-mode step-index silica optical fiber has core refractive index $n_{\text{core}} = 1.482$ and cladding refractive index $n_{\text{clad}} = 1.460$:
1. Numerical Aperture ($NA$):
   $$NA = \sqrt{n_{\text{core}}^2 - n_{\text{clad}}^2} = \sqrt{1.482^2 - 1.460^2} = \sqrt{2.196324 - 2.131600} = \sqrt{0.064724} \approx \mathbf{0.2544}$$
2. Maximum acceptance half-angle in air ($\theta_{\max}$):
   $$\theta_{\max} = \arcsin(NA) = \arcsin(0.254409) \approx \mathbf{14.74^\circ}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 1.482 {{keycap:x²}} | 0.00 | 0.00 | 0.00 | 2.196324 | 2.196324 |
| 02 | 1.460 {{keycap:x²}} | 0.00 | 0.00 | 2.196324 | 2.131600 | 2.131600 |
| 03 | {{key:-}} {{key:√x}} | 0.00 | 0.00 | 0.00 | 0.254409 | 0.254409(NA) |
| 04 | {{key:ASIN}} | 0.00 | 0.00 | 0.00 | 14.738910 | 14.74 (°) |

---

### Problem 4.5: Thick Lens Equivalent Focal Length (Gullstrand Formula)
A thick biconvex crown glass lens has front radius $R_1 = 50.0\text{ mm}$, rear radius $R_2 = -80.0\text{ mm}$, center thickness $d = 12.0\text{ mm}$, and refractive index $n = 1.520$. Gullstrand's lens maker formula states:
$$\frac{1}{f} = (n - 1) \left[ \frac{1}{R_1} - \frac{1}{R_2} + \frac{(n - 1) d}{n R_1 R_2} \right]$$
1. Front surface power: $(n - 1) / R_1 = 0.520 / 50 = 0.010400\text{ mm}^{-1}$.
2. Rear surface power: $-(n - 1) / R_2 = -0.520 / (-80) = 0.006500\text{ mm}^{-1}$.
3. Thickness coupling term:
   $$\frac{(n - 1)^2 d}{n R_1 R_2} = \frac{0.520^2 \times 12.0}{1.520 \times 50.0 \times (-80.0)} = \frac{3.2448}{-6080.0} = -0.00053368\text{ mm}^{-1}$$
4. Total optical power: $P = 0.010400 + 0.006500 - 0.00053368 = 0.01636632\text{ mm}^{-1}$.
5. Equivalent focal length: $f = 1 / P \approx \mathbf{61.10\text{ mm}}$.

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .520 50 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.010400 | 0.010400 |
| 02 | .520 80 {{key:÷}} {{key:+}} | 0.00 | 0.00 | 0.00 | 0.016900 | 0.016900 |
| 03 | .520 {{key:x²}} 12 {{key:×}} | 0.00 | 0.016900 | 0.016900 | 3.244800 | 3.244800 |
| 04 | 1.52 50 {{key:×}} 80 {{key:×}} | 0.00 | 0.016900 | 3.244800 | 6080.0000 | 6080.0000 |
| 05 | {{key:÷}} {{key:-}} | 0.00 | 0.00 | 0.00 | 0.016366 | 0.016366 |
| 06 | {{key:1/x}} | 0.00 | 0.00 | 0.00 | 61.101083 | 61.10 (mm) |

---

## Case Study 5: Orbital Mechanics & Rocket Flight Dynamics


### Problem 5.1: Hohmann Transfer Orbit $\Delta v$ (LEO to GEO)
Earth gravitational parameter $\mu = 3.986004 \times 10^{14}\text{ m}^3/\text{s}^2$.  
Initial LEO radius $r_1 = 6.678 \times 10^6\text{ m}$ ($h = 300\text{ km}$).  
Target GEO radius $r_2 = 4.2164 \times 10^7\text{ m}$ ($h = 35,786\text{ km}$).  
Transfer semi-major axis $a = (r_1 + r_2)/2 = 2.4421 \times 10^7\text{ m}$.
1. Initial circular velocity: $v_{c1} = \sqrt{\mu / r_1} = \mathbf{7,725.82\text{ m/s}}$.
2. Transfer ellipse insertion: $v_{tx1} = \sqrt{\mu(2/r_1 - 1/a)} = \mathbf{10,151.62\text{ m/s}}$.
3. Periapsis impulse: $\Delta v_1 = 10,151.62 - 7,725.82 = \mathbf{2,425.80\text{ m/s}}$.
4. Apoapsis circularization: $\Delta v_2 = 3,074.66 - 1,609.91 = \mathbf{1,464.75\text{ m/s}}$.
5. Total mission $\Delta v$: $\Delta v_{\text{total}} = 2,425.80 + 1,464.75 = \mathbf{3,890.55\text{ m/s}}$ ($3.891\text{ km/s}$).

#### Keystrokes (Delta-V Impulses & Total Mission Budget):
`10151.62 {{key:ENTER}} 7725.82 {{key:-}} 3074.66 {{key:ENTER}} 1609.91 {{key:-}} {{key:+}}` $\rightarrow$ **`3890.550000`**

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 10151.62 {{key:ENTER}} | 0.00 | 0.00 | 10151.620000 | 10151.620000 | 10151.620000_ |
| 02 | 7725.82 {{key:-}} | 0.00 | 0.00 | 0.00 | 2425.800000 | 2425.800000 (Δv₁) |
| 03 | 3074.66 {{key:ENTER}} | 0.00 | 2425.800000 | 3074.660000 | 3074.660000 | 3074.660000_ |
| 04 | 1609.91 {{key:-}} | 0.00 | 0.00 | 2425.800000 | 1464.750000 | 1464.750000 (Δv₂) |
| 05 | {{key:+}} | 0.00 | 0.00 | 0.00 | 3890.550000 | 3890.550000 (Δv_tot) |

---

### Problem 5.2: Tsiolkovsky Multistage Rocket Equation
A two-stage vehicle injects a communications satellite into orbit:
* Stage 1: Exhaust $v_{e1} = 2,950\text{ m/s}$, mass ratio $m_{01}/m_{f1} = 220,000 / 48,000 = 4.5833$:
  $$\Delta v_1 = 2950 \times \ln(4.5833) = \mathbf{4,491.56\text{ m/s}}$$
* Stage 2: Exhaust $v_{e2} = 3,420\text{ m/s}$, mass ratio $m_{02}/m_{f2} = 38,000 / 6,200 = 6.1290$:
  $$\Delta v_2 = 3420 \times \ln(6.1290) = \mathbf{6,200.75\text{ m/s}}$$
* Gravity/drag losses $\Delta v_{\text{loss}} = 1,350\text{ m/s}$. Net orbital velocity:
  $$v_{\text{net}} = 4,491.56 + 6,200.75 - 1,350 = \mathbf{9,342.31\text{ m/s}}$$

> **Named RPN Stack Idiom: *The Multi-Stage Tsiolkovsky Delta-V Accumulator*** — Evaluate sequential stage mass ratios and exhaust velocities in place, summing orbital velocity increments directly {{cite:munroe2014}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Stage 1 Velocity Increment:** Key wet-to-dry mass ratio $220,000 / 48,000$, take natural log, and multiply by exhaust velocity $v_{e1} = 2,950\text{ m/s}$; Stage 1 impulse $\Delta v_1 = 4,491.56\text{ m/s}$ forms in Register $X$.
2. **Stage 2 Velocity Increment & Sum:** Key Stage 2 mass ratio $38,000 / 6,200$, take natural log, and multiply by $v_{e2} = 3,420\text{ m/s}$; Stage 2 impulse $\Delta v_2 = 6,200.75\text{ m/s}$ adds directly to Stage 1 in $Y$, yielding gross velocity $10,692.31\text{ m/s}$ in $X$.
3. **Deduct Atmospheric & Gravity Losses:** Key total trajectory losses $\Delta v_{\text{loss}} = 1,350\text{ m/s}$ and subtract; net orbital insertion velocity resolves to $\mathbf{9,342.31\text{ m/s}}$ with zero intermediate re-entry.

#### Stack Trace Table:
| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 4.5833 {{key:LN}} | 0.00 | 0.00 | 0.00 | 1.522562 | Stage 1 mass ratio natural logarithm ln(m_01/m_f1) |
| 02 | 2950 {{key:×}} | 0.00 | 0.00 | 0.00 | 4491.5583 | Stage 1 velocity increment Δv_1 = 4491.56 m/s |
| 03 | 6.1290 {{key:LN}} | 0.00 | 0.00 | 4491.5583 | 1.813031 | Stage 2 mass ratio ln(m_02/m_f2), Δv_1 lifts to Y |
| 04 | 3420 {{key:×}} | 0.00 | 0.00 | 4491.5583 | 6200.7490 | Stage 2 velocity increment Δv_2 = 6200.75 m/s |
| 05 | {{key:+}} | 0.00 | 0.00 | 0.00 | 10692.307 | Gross orbital velocity sum (10,692.31 m/s) |
| 06 | 1350 {{key:-}} | 0.00 | 0.00 | 0.00 | 9342.3073 | Deduct trajectory losses; net orbital v_net = 9,342.31 m/s |

---

### Problem 5.3: Rocket Motor Burnout Velocity via Romberg Quadrature
Integrate thrust acceleration $a(t) = 4t^2 - 0.5t^3$ from $t = 0$ to $t = 6.0\text{ seconds}$:
$$\Delta v = \int_0^6 (4t^2 - 0.5t^3) dt = \left[ \frac{4}{3}t^3 - \frac{1}{8}t^4 \right]_0^6 = \frac{4}{3}(216) - \frac{1}{8}(1296) = 288 - 162 = \mathbf{126.0\text{ m/s}}$$
Executed in `{{key:EQN}}` via {{key:∫}}: engine converges to exactly **`126.0000 m/s`**.

> **Named RPN Stack Idiom: *The Romberg Rocket Burnout Quadrature*** — Integrate polynomial thrust acceleration across burn time interval $[0, t_{\text{burn}}]$ via adaptive Richardson extrapolation {{cite:romberg1955,richardson1911}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Program Acceleration Integrand in `{{key:EQN}}`:** Key thrust profile $a(t) = 4t^2 - 0.5t^3$ into equation memory: `4 T {{key:x²}} {{key:×}} 0.5 T 3 {{key:yˣ}} {{key:×}} {{key:-}}`.
2. **Set Burn Time Bounds on Stack:** Key ignition time $t = 0.0\text{ s}$ into $Y$ and burnout cutoff $t = 6.0\text{ s}$ into $X$ ($0$ `{{key:ENTER}}` $6$).
3. **Execute Adaptive Quadrature (`{{key:∫}}`):** Richardson extrapolation iteratively bisects the trapezoidal grid, converging to the exact closed-form burnout velocity $\Delta v = \mathbf{126.0000\text{ m/s}}$ in Register $X$.

#### Stack Trace Table:
| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 0 {{key:ENTER}} | 0.00 | 0.00 | 0.000000 | 0.000000 | Ignition time lower bound t = 0.0 s in Y |
| 02 | 6 {{key:ENTER}} | 0.00 | 0.00 | 0.000000 | 6.000000 | Burnout cutoff upper bound t = 6.0 s in X |
| 03 | {{key:∫}} T | 0.00 | 0.00 | 1.2435E-11 | 126.000000 | Converged Romberg definite integral Δv = 126.0000 m/s |

---

### Problem 5.4: Gravitational Escape Velocity from Earth and Mars
Planetary surface escape velocity is given by $v_{\text{esc}} = \sqrt{\frac{2\mu}{r}}$:
1. Earth ($\mu = 3.986004 \times 10^{14}\text{ m}^3/\text{s}^2, r = 6.378 \times 10^6\text{ m}$):
   $$v_{\text{esc},\oplus} = \sqrt{\frac{2 \times 3.986004 \times 10^{14}}{6.378 \times 10^6}} \approx \mathbf{11,185.96\text{ m/s}} \quad (\mathbf{11.19\text{ km/s}})$$
2. Mars ($\mu_{\text{Mars}} = 4.282837 \times 10^{13}\text{ m}^3/\text{s}^2, r_{\text{Mars}} = 3.3895 \times 10^6\text{ m}$):
   $$v_{\text{esc,Mars}} = \sqrt{\frac{2 \times 4.282837 \times 10^{13}}{3.3895 \times 10^6}} \approx \mathbf{5,026.91\text{ m/s}} \quad (\mathbf{5.03\text{ km/s}})$$

#### Stack Trace Table (Earth $v_{\text{esc}}$):
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 2 {{key:ENTER}} | 0.00 | 0.00 | 2.000000 | 2.000000 | 2.000000_ |
| 02 | 3.986004E14 {{key:×}} | 0.00 | 0.00 | 0.00 | 7.972008E14 | 7.972008E14 |
| 03 | 6.378E6 {{key:÷}} | 0.00 | 0.00 | 0.00 | 1.24992E8 | 1.249923E8 |
| 04 | {{key:√x}} | 0.00 | 0.00 | 0.00 | 11179.995 | 11185.96(m/s) |

---

### Problem 5.5: Kepler's Third Law Geostationary Orbital Radius
For a satellite in circular orbit around Earth, the sidereal rotational period of Earth is $T = 86,164.09\text{ seconds}$ (23 hours, 56 minutes, 4.09 seconds). Using Kepler's Third Law:
$$a = \left( \frac{\mu T^2}{4\pi^2} \right)^{1/3} = \left( \frac{3.986004 \times 10^{14} \times (86164.09)^2}{4\pi^2} \right)^{1/3} \approx \mathbf{42,164,140\text{ meters}} \quad (\mathbf{42,164.14\text{ km}})$$
Subtracting Earth's mean equatorial radius ($6,378.14\text{ km}$) yields the geostationary orbital altitude $h_{\text{GEO}} = \mathbf{35,786.0\text{ km}}$.

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 86164.09{{keycap:x²}} | 0.00 | 0.00 | 0.00 | 7.42425E9 | 7.424249E9 |
| 02 | 3.986004E14 {{key:×}} | 0.00 | 0.00 | 0.00 | 2.95931E24 | 2.959310E24 |
| 03 | 4 {{key:÷}} π {{key:x²}} {{key:÷}} | 0.00 | 0.00 | 0.00 | 7.49603E22 | 7.496030E22 |
| 04 | 3 {{key:1/x}} {{key:yˣ}} | 0.00 | 0.00 | 0.00 | 4.21641E7 | 42164140 (m) |
| 05 | 6.37814E6 {{key:-}} | 0.00 | 0.00 | 0.00 | 3.57860E7 | 35786000 (m) |

---

{{blocks:unit_circle_volvelle|Geodetic Azimuth and Harmonic Volvelle Instrumentation}}
*Figure 13.3: Geodetic polar coordinates and navigational vector resolution: transforming azimuth angles and spherical arc distances into Cartesian survey grids.*


## Case Study 6: Civil Surveying & Geodetic Traversing


### Problem 6.1: Closed-Loop Traverse Coordinate Closures
Traverse polygon with 4 stations ($r$ in meters, $\theta$ in degrees):
* Leg 1: $r=100.0, \theta=60^\circ \implies \Delta x = 50.0000, \Delta y = 86.6025$
* Leg 2: $r=80.0, \theta=150^\circ \implies \Delta x = -69.2820, \Delta y = 40.0000$
* Leg 3: $r=100.0, \theta=240^\circ \implies \Delta x = -50.0000, \Delta y = -86.6025$
* Leg 4: $r=80.0, \theta=330^\circ \implies \Delta x = 69.2820, \Delta y = -40.0000$

Accumulated directly via `{{key:▸y,x}} {{key:Σ+}}`:
* Departure sum $\Sigma x = 0.0000\text{ m}$.
* Latitude sum $\Sigma y = 0.0000\text{ m}$.
* Misclosure error $E = \sqrt{\Sigma x^2 + \Sigma y^2} = \mathbf{0.0000\text{ m}}$.
* Enclosed rectangular area: $100 \times 80 = \mathbf{8,000.0\text{ m}^2}$.

> **Named RPN Stack Idiom: *The Polar-to-Rectangular Traverse Closure Accumulator*** — Convert field azimuth bearings to latitude/departure increments and accumulate total loop closure in statistical registers {{cite:hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Transform Polar Leg to Rectangular Coordinates:** Key station distance $r$ in $Y$ and azimuth angle $\theta$ in $X$, executing `{{key:▸y,x}}` to split distance into latitude $\Delta y$ and departure $\Delta x$.
2. **Accumulate Vector Displacements via `{{key:Σ+}}`:** Commit each station displacement into hardware summation registers; departures and latitudes accumulate in separate accumulators.
3. **Inspect Loop Misclosure Error:** Read accumulated sums; net departure $\Sigma x = 0.0000\text{ m}$ and latitude $\Sigma y = 0.0000\text{ m}$ yield zero linear misclosure error $E = 0.0000\text{ m}$, confirming mathematically closed traverse geometry.

#### Stack Trace Table:
| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 60 {{key:ENTER}} 100 {{key:▸y,x}} | 0.00 | 0.00 | 86.602540 | 50.000000 | Leg 1: Δy = 86.6025 m (lat), Δx = 50.0000 m (dep) |
| 02 | {{key:Σ+}} | 0.00 | 86.602540 | 50.000000 | 1.000000 | Accumulate Leg 1 into stat memory; n = 1 in X |
| 03 | 150 {{key:ENTER}} 80 {{key:▸y,x}} | 0.00 | 0.00 | 40.000000 | -69.282032 | Leg 2: Δy = 40.0000 m (lat), Δx = -69.2820 m (dep) |
| 04 | {{key:Σ+}} | 0.00 | 40.000000 | -69.282032 | 2.000000 | Accumulate Leg 2 into stat memory; n = 2 in X |
| 05 | 240 {{key:ENTER}} 100 {{key:▸y,x}} | 0.00 | 0.00 | -86.602540 | -50.000000 | Leg 3: Δy = -86.6025 m (lat), Δx = -50.0000 m (dep) |
| 06 | {{key:Σ+}} | 0.00 | -86.602540 | -50.000000 | 3.000000 | Accumulate Leg 3 into stat memory; n = 3 in X |
| 07 | 330 {{key:ENTER}} 80 {{key:▸y,x}} | 0.00 | 0.00 | -40.000000 | 69.282032 | Leg 4: Δy = -40.0000 m (lat), Δx = 69.2820 m (dep) |
| 08 | {{key:Σ+}} | 0.00 | -40.000000 | 69.282032 | 4.000000 | Accumulate Leg 4 into stat memory; n = 4 in X |

---

### Problem 6.2: Meridian Convergence & True vs. Magnetic Azimuth
A geodetic survey line in Texas has a measured magnetic azimuth $\alpha_{\text{mag}} = 142.35^\circ$. The local magnetic declination is $\delta = 4.12^\circ\text{ E}$ (East declination is added), and grid convergence angle is $\gamma = -1.25^\circ$:
$$\alpha_{\text{true}} = \alpha_{\text{mag}} + \delta = 142.35^\circ + 4.12^\circ = \mathbf{146.47^\circ}$$
$$\alpha_{\text{grid}} = \alpha_{\text{true}} - \gamma = 146.47^\circ - (-1.25^\circ) = \mathbf{147.72^\circ}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 142.35 {{key:ENTER}} | 0.00 | 0.00 | 142.3500 | 142.3500 | 142.3500_ |
| 02 | 4.12 {{key:+}} | 0.00 | 0.00 | 0.00 | 146.4700 | 146.4700 (°) |
| 03 | 1.25 {{key:+/-}} {{key:-}} | 0.00 | 0.00 | 0.00 | 147.7200 | 147.7200 (°) |

---

### Problem 6.3: Bowditch Compass Rule Linear Misclosure Balancing
A field traverse leg has raw measured length $L_1 = 250.0\text{ ft}$ along a total perimeter $L_{\text{total}} = 1,250.0\text{ ft}$. The total survey departure misclosure is $E_x = +0.15\text{ ft}$. Calculate the Bowditch proportional departure correction $C_{x1}$:
$$C_{x1} = - E_x \times \left( \frac{L_1}{L_{\text{total}}} \right) = -0.15 \times \left( \frac{250.0}{1250.0} \right) = -0.15 \times 0.20 = \mathbf{-0.030\text{ ft}}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .15 {{key:+/-}} | 0.00 | 0.00 | 0.00 | -0.150000 | -0.150000 |
| 02 | 250 {{key:×}} | 0.00 | 0.00 | 0.00 | -37.50000 | -37.50000 |
| 03 | 1250 {{key:÷}} | 0.00 | 0.00 | 0.00 | -0.030000 | -0.03000 (ft) |

---

## Case Study 7: Structural Mechanics & Beam Deflection

### Problem 7.1: Euler Column Buckling Critical Load
Support column length $L = 6.5\text{ m}$, $E = 200.0\text{ GPa}$, $I = 4.85 \times 10^{-6}\text{ m}^4$, pinned ends ($K=1.0$):
$$P_{\text{cr}} = \frac{\pi^2 E I}{L^2} = \frac{\pi^2 \times (200 \times 10^9) \times (4.85 \times 10^{-6})}{6.5^2} \approx \mathbf{226.59\text{ kN}}$$
With safety factor $SF = 2.5$: $P_{\text{allow}} = 226.59 \div 2.5 = \mathbf{90.64\text{ kN}}$.

> **Named RPN Stack Idiom: *The Euler Column Critical Buckling Threshold*** — Cascade elastic flexural stiffness and column height in the operational stack to determine structural stability limits {{cite:parker2019}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Evaluate Flexural Rigidity Numerator ($\pi^2 E I$):** Key `{{key:π}} {{key:x²}}`, enter elastic modulus $E = 200.0\text{ GPa}$, multiply, enter moment of inertia $I = 4.85 \times 10^{-6}\text{ m}^4$, and multiply; flexural stiffness numerator ($9.5739 \times 10^6\text{ N}\cdot\text{m}^2$) forms in Register $X$.
2. **Divide by Squared Column Height ($L^2$):** Enter column span $L = 6.5\text{ m}$, square via `{{key:x²}}` ($42.25\text{ m}^2$), and divide; critical Euler buckling threshold resolves to $P_{\text{cr}} = \mathbf{226.59\text{ kN}}$ in Register $X$.
3. **Apply Factor of Safety:** Enter design factor of safety $SF = 2.5$ and divide; allowable structural axial service load evaluates to $\mathbf{90.64\text{ kN}}$ in Register $X$.

#### Stack Trace Table:
| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | {{keycap:π}} {{keycap:x²}} | 0.00 | 0.00 | 0.00 | 9.869604 | π² evaluated in place |
| 02 | 200E9 {{key:×}} | 0.00 | 0.00 | 0.00 | 1.973921E12 | Scale by elastic modulus E = 200 GPa |
| 03 | 4.85E-6 {{key:×}} | 0.00 | 0.00 | 0.00 | 9.573516E6 | Scale by moment of inertia I; numerator π²EI (N·m²) |
| 04 | 6.5 {{keycap:x²}} | 0.00 | 0.00 | 9.573516E6 | 42.250000 | Column length squared L² (m²), numerator lifts to Y |
| 05 | {{key:÷}} | 0.00 | 0.00 | 0.00 | 226592.10 | Critical Euler buckling load P_cr = 226.59 kN |
| 06 | 2.5 {{key:÷}} | 0.00 | 0.00 | 0.00 | 90636.840 | Safety factor SF = 2.5; allowable load P_allow = 90.64 kN |

---

### Problem 7.2: Center Point Load Beam Deflection
Simply supported steel beam of span $L = 4.0\text{ m}$, $E = 200\text{ GPa}$, $I = 8.5 \times 10^{-6}\text{ m}^4$, center point load $P = 5,000\text{ N}$:
$$\delta_{\max} = \frac{P L^3}{48 E I} = \frac{5000 \times 4^3}{48 \times (200 \times 10^9) \times (8.5 \times 10^{-6})} \approx \mathbf{0.003922\text{ m}} \quad (\mathbf{3.92\text{ mm}})$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 4 3 {{key:yˣ}} 5000 {{key:×}} | 0.00 | 0.00 | 0.00 | 320000.00 | 320000.00 |
| 02 | 48 {{key:÷}} | 0.00 | 0.00 | 0.00 | 6666.6667 | 6666.6667 |
| 03 | 200 {{key:E}} 9 {{key:÷}} | 0.00 | 0.00 | 0.00 | 3.3333E-8 | 3.3333E-8 |
| 04 | 8.5{{key:E}}6 {{key:+/-}} {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.00392157 | 0.003922 (m) |

---

### Problem 7.3: Uniform Distributed Load Maximum Bending Moment
A simply supported floor girder spans $L = 8.0\text{ meters}$ supporting a combined dead and live distributed load $w = 24.5\text{ kN/m}$ ($24,500\text{ N/m}$). Calculate the maximum bending moment $M_{\max}$ at midspan:
$$M_{\max} = \frac{w L^2}{8} = \frac{24500 \times 8.0^2}{8} = 24500 \times 8 = \mathbf{196,000\text{ N}\cdot\text{m}} \quad (\mathbf{196.0\text{ kN}\cdot\text{m}})$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 24500 {{key:ENTER}} | 0.00 | 0.00 | 24500.00 | 24500.00 | 24500.00_ |
| 02 | 8 {{keycap:x²}} {{key:×}} | 0.00 | 0.00 | 0.00 | 1568000.0 | 1568000.0 |
| 03 | 8 {{key:÷}} | 0.00 | 0.00 | 0.00 | 196000.00 | 196000.0(N·m) |

---

### Problem 7.4: Cantilever Beam Maximum Tip Deflection Under Uniform Load
A balcony cantilever beam of length $L = 2.5\text{ m}$ carries uniform distributed load $w = 3,200\text{ N/m}$. The beam is structural steel with $E = 200.0\text{ GPa}$ ($200 \times 10^9\text{ Pa}$) and second moment of area $I = 1.65 \times 10^{-5}\text{ m}^4$. Maximum tip deflection is:
$$\delta_{\max} = \frac{w L^4}{8 E I} = \frac{3200 \times 2.5^4}{8 \times (200 \times 10^9) \times (1.65 \times 10^{-5})} = \frac{3200 \times 39.0625}{26,400,000} \approx \mathbf{0.004735\text{ m}} \quad (\mathbf{4.74\text{ mm}})$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 2.5 {{key:ENTER}} 4 {{key:yˣ}} | 0.00 | 0.00 | 2.500000 | 39.062500 | 39.062500 |
| 02 | 3200 {{key:×}} | 0.00 | 0.00 | 0.00 | 125000.00 | 125000.00 |
| 03 | 8 {{key:÷}} 200E9 {{key:÷}} | 0.00 | 0.00 | 0.00 | 7.8125E-11 | 7.8125E-11 |
| 04 | 1.65E-5 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.00473485 | 0.004735 (m) |

---

## Case Study 8: Chemical Kinetics & Thermochemistry

### Problem 8.1: Arrhenius Activation Energy ($E_a$)
Gas-phase reaction rate constants:
* At $T_1 = 300\text{ K}$: $k_1 = 2.15 \times 10^{-4}\text{ s}^{-1}$
* At $T_2 = 350\text{ K}$: $k_2 = 4.80 \times 10^{-2}\text{ s}^{-1}$
Universal gas constant $R = 8.314462\text{ J/(mol}\cdot\text{K)}$:
$$E_a = \frac{R \ln(k_2 / k_1)}{\frac{1}{T_1} - \frac{1}{T_2}} = \frac{8.314462 \times \ln(0.048 / 0.000215)}{\frac{1}{300} - \frac{1}{350}} \approx \mathbf{94.43\text{ kJ/mol}}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .048 .000215 {{key:÷}} | 0.00 | 0.00 | 0.00 | 223.255814 | 223.255814 |
| 02 | {{key:LN}} 8.31446 {{key:×}} | 0.00 | 0.00 | 0.00 | 44.966940 | 44.966940 |
| 03 | 300 {{key:1/x}} 350 {{key:1/x}} {{key:-}} | 0.00 | 0.00 | 44.966940 | 4.7619E-4 | 4.7619E-4 |
| 04 | {{key:÷}} 1000 {{key:÷}} | 0.00 | 0.00 | 0.00 | 94.430582 | 94.43(kJ/mol) |

---

### Problem 8.2: Standard Gibbs Free Energy & Equilibrium Constant
For the chemical synthesis of ammonia ($\text{N}_2 + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3$) at temperature $T = 298.15\text{ K}$, the thermodynamic equilibrium constant is $K_p = 5.8 \times 10^5$. Calculate the standard Gibbs free energy change $\Delta G^\circ$:
$$\Delta G^\circ = - R T \ln K_p = - 8.314462 \times 298.15 \times \ln(5.8 \times 10^5) \approx \mathbf{-32,897.4\text{ J/mol}} \quad (\mathbf{-32.90\text{ kJ/mol}})$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 5.8 {{key:E}} 5 | 0.00 | 0.00 | 0.00 | 580000.0 | 580000.0_ |
| 02 | {{key:LN}} | 0.00 | 0.00 | 0.00 | 13.270783 | 13.270783 |
| 03 | 8.314462 {{key:×}} | 0.00 | 0.00 | 0.00 | 110.33943 | 110.33943 |
| 04 | 298.15 {{key:×}} | 0.00 | 0.00 | 0.00 | 32897.701 | 32897.70 |
| 05 | {{key:+/-}} 1000 {{key:÷}} | 0.00 | 0.00 | 0.00 | -32.897701 | -32.90(kJ/mol |

---

### Problem 8.3: Nernst Electrochemical Cell Potential
A galvanic Daniell cell ($\text{Zn} + \text{Cu}^{2+} \rightleftharpoons \text{Zn}^{2+} + \text{Cu}$) has standard cell potential $E^\circ = 1.100\text{ V}$ with $n = 2\text{ electrons transferred}$ at $T = 298.15\text{ K}$. Faraday constant $F = 96,485.33\text{ C/mol}$. The electrolyte concentrations are $[\text{Zn}^{2+}] = 0.50\text{ M}$ and $[\text{Cu}^{2+}] = 0.010\text{ M}$ (reaction quotient $Q = 0.50 / 0.010 = 50.0$):
$$E = E^\circ - \frac{R T}{n F} \ln Q = 1.100 - \frac{8.314462 \times 298.15}{2 \times 96485.33} \ln(50.0) = 1.100 - (0.012845 \times 3.912023) \approx \mathbf{1.0497\text{ V}}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 50 {{key:LN}} | 0.00 | 0.00 | 0.00 | 3.912023 | 3.912023 |
| 02 | 8.314462 {{key:×}} | 0.00 | 0.00 | 0.00 | 32.526365 | 32.526365 |
| 03 | 298.15 {{key:×}} | 0.00 | 0.00 | 0.00 | 9697.7358 | 9697.7358 |
| 04 | 2 {{key:÷}} 96485.3 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.050255 | 0.050255 (V) |
| 05 | 1.100 {{key:x⇄y}} {{key:-}} | 0.00 | 0.00 | 0.00 | 1.049745 | 1.049745 (V) |

---

## Case Study 9: Nuclear Physics & Radioactive Decay

### Problem 9.1: Cobalt-60 Half-Life Decay Constant & Activity
Half-life $t_{1/2} = 5.2714\text{ years}$. Initial activity $A_0 = 500.0\text{ Curies}$.
1. Decay constant: $\lambda = \frac{\ln 2}{5.2714} \approx \mathbf{0.131492\text{ yr}^{-1}}$.
2. Activity after $t = 12.0\text{ years}$:
   $$A(12) = 500 \times e^{-0.131492 \times 12} = 500 \times e^{-1.5779} \approx \mathbf{103.11\text{ Curies}}$$

#### Keystrokes (Decay Constant $\lambda$ & Remaining Activity $A(12)$):
`2 {{key:LN}} 5.2714 {{key:÷}} 12 {{key:×}} {{key:+/-}} {{key:eˣ}} 500 {{key:×}}` $\rightarrow$ **`103.203578`**

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 2 {{key:LN}} | 0.00 | 0.00 | 0.00 | 0.693147 | 0.693147 |
| 02 | 5.2714 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.131492 | 0.131492 (λ) |
| 03 | 12 {{key:×}} | 0.00 | 0.00 | 0.00 | 1.577905 | 1.577905 |
| 04 | {{key:+/-}} {{key:eˣ}} | 0.00 | 0.00 | 0.00 | 0.206407 | 0.206407 |
| 05 | 500 {{key:×}} | 0.00 | 0.00 | 0.00 | 103.203578 | 103.20 (Ci) |

---

### Problem 9.2: Carbon-14 Archeological Radiocarbon Dating
Living plant tissue maintains a steady Carbon-14 activity of $A_0 = 15.3\text{ disintegrations/min}\cdot\text{g of carbon}$. An ancient timber specimen excavated from a ceremonial structure exhibits an activity of $A(t) = 9.4\text{ dpm/g}$. Using the true physical **Cambridge $^{14}\text{C}$ half-life** $t_{1/2} = 5,730\text{ years}$ ($\lambda = \ln 2 / 5730 \approx 0.00012097\text{ yr}^{-1}$; note that uncalibrated archaeological laboratory reports use the conventional $5,568\text{-year}$ Libby half-life prior to `IntCal20` calibration):
$$t = - \frac{1}{\lambda} \ln\left(\frac{A(t)}{A_0}\right) = - \frac{5730}{\ln 2} \ln\left(\frac{9.4}{15.3}\right) = -8266.64 \times (-0.487144) \approx \mathbf{4,027.0\text{ years}}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 9.4 15.3 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.614379 | 0.614379 |
| 02 | {{key:LN}} | 0.00 | 0.00 | 0.00 | -0.487144 | -0.487144 |
| 03 | 5730 {{key:×}} | 0.00 | 0.00 | 0.00 | -2791.334 | -2791.334 |
| 04 | 2 {{key:LN}} {{key:÷}} | 0.00 | 0.00 | 0.00 | -4027.014 | -4027.014 |
| 05 | {{key:+/-}} | 0.00 | 0.00 | 0.00 | 4027.0141 | 4027.0 (yr) |

---

### Problem 9.3: Gamma Ray Shielding & Lead Half-Value Layer (HVL)
Cobalt-60 emits energetic gamma photons ($1.17\text{ MeV}$ and $1.33\text{ MeV}$) with linear attenuation coefficient $\mu = 0.650\text{ cm}^{-1}$ in lead shielding.
1. Half-Value Layer thickness:
   $$\text{HVL} = \frac{\ln 2}{\mu} = \frac{0.693147}{0.650} \approx \mathbf{1.0664\text{ cm}}$$
2. Required thickness $x$ to reduce radiation intensity by a factor of 100 ($I / I_0 = 0.01$):
   $$x = - \frac{\ln(0.01)}{\mu} = \frac{4.605170}{0.650} \approx \mathbf{7.0849\text{ cm}}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .01 {{key:LN}} | 0.00 | 0.00 | 0.00 | -4.605170 | -4.605170 |
| 02 | .650 {{key:÷}} | 0.00 | 0.00 | 0.00 | -7.084877 | -7.084877 |
| 03 | {{key:+/-}} | 0.00 | 0.00 | 0.00 | 7.084877 | 7.0849 (cm) |

---

## Case Study 10: Architectural Acoustics & Environmental Noise

### Problem 10.1: Sabine Reverberation Time ($RT_{60}$)
Lecture hall volume $V = 675.0\text{ m}^3$ ($15\text{ m} \times 10\text{ m} \times 4.5\text{ m}$). Total absorption $A_{\text{total}} = 152.75\text{ metric Sabins}$:
$$RT_{60} = \frac{0.161 \times V}{A_{\text{total}}} = \frac{0.161 \times 675.0}{152.75} \approx \mathbf{0.7115\text{ seconds}}$$
Keystrokes: `{{res:sc32_13_applied_stem_case_studies_seq_01:keys}}`$\rightarrow$ **`{{res:sc32_13_applied_stem_case_studies_seq_01:value}}`** (Ideal for speech intelligibility).

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `.161` `{{key:ENTER}}` — Enter empirical Sabine reverberation constant ($0.161$) into Register $Y$.
2. `675` `{{key:×}}` — Push room volume ($V = 675.0\text{ m}^3$) and scale directly to obtain room acoustic power ($108.675$) in $X$.
3. `152.75` `{{key:÷}}` — Enter total metric absorption ($A = 152.75\text{ Sabins}$) and divide, yielding $RT_{60} = \mathbf{0.7115\text{ s}}$.

#### Stack Trace Table:
| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | .161 {{key:ENTER}} | 0.00 | 0.00 | 0.161000 | 0.161000 | Empirical Sabine reverberation constant entered |
| 02 | 675 {{key:×}} | 0.00 | 0.00 | 0.00 | 108.67500 | Scale by room volume V = 675.0 m³ |
| 03 | 152.75 {{key:÷}} | 0.00 | 0.00 | 0.00 | 0.711457 | Divide total absorption A = 152.75 Sabins; RT_60 = 0.7115 s |

---

### Problem 10.2: Decibel Addition of Incoherent Environmental Noise Sources
An industrial shop floor operates three loud machines with sound pressure levels: Machine 1: $L_1 = 88.0\text{ dBA}$, Machine 2: $L_2 = 91.0\text{ dBA}$, Machine 3: $L_3 = 85.0\text{ dBA}$. Determine the combined acoustic noise level $L_{\Sigma}$:
$$L_{\Sigma} = 10 \log_{10} \left( 10^{88/10} + 10^{91/10} + 10^{85/10} \right) = 10 \log_{10}(6.3096 \times 10^8 + 1.2589 \times 10^9 + 3.1623 \times 10^8) \approx \mathbf{93.43\text{ dBA}}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 8.8 {{keycap:10ˣ}} | 0.00 | 0.00 | 0.00 | 6.30957E8 | 6.30957E8 |
| 02 | 9.1 {{keycap:10ˣ}} {{key:+}} | 0.00 | 0.00 | 0.00 | 1.88988E9 | 1.88988E9 |
| 03 | 8.5 {{keycap:10ˣ}} {{key:+}} | 0.00 | 0.00 | 0.00 | 2.20611E9 | 2.20611E9 |
| 04 | {{key:LOG}} 10 {{key:×}} | 0.00 | 0.00 | 0.00 | 93.436270 | 93.44 (dBA) |

---

### Problem 10.3: Inverse Square Law Acoustic Attenuation with Distance
An outdoor emergency warning siren emits sound level $L_1 = 105.0\text{ dB}$ measured at distance $r_1 = 10.0\text{ meters}$. Assuming spherical propagation without ground reflections, determine sound pressure level $L_2$ at distance $r_2 = 120.0\text{ meters}$:
$$L_2 = L_1 - 20 \log_{10}\left(\frac{r_2}{r_1}\right) = 105.0 - 20 \log_{10}\left(\frac{120.0}{10.0}\right) = 105.0 - 20 \log_{10}(12.0) = 105.0 - 21.5836 \approx \mathbf{83.42\text{ dB}}$$

#### Stack Trace Table:
| STEP | KEYSTROKE | REGISTER T | REGISTER Z | REGISTER Y | REGISTER X | DISPLAY |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 120 10 {{key:÷}} | 0.00 | 0.00 | 0.00 | 12.000000 | 12.000000 |
| 02 | {{key:LOG}} | 0.00 | 0.00 | 0.00 | 1.079181 | 1.079181 |
| 03 | 20 {{key:×}} | 0.00 | 0.00 | 0.00 | 21.583625 | 21.583625 |
| 04 | 105 {{key:x⇄y}} {{key:-}} | 0.00 | 0.00 | 0.00 | 83.416375 | 83.42 (dB) |

---

## Case Study 11: The Practicing Engineer's Benchtop Pocket Reference

*Benchtop Design Briefing:* A practicing mechanical, electrical, or systems engineer rarely has time to boot a workstation CAD/FEA suite during a prototype design review on the shop floor. Two operations recur across nearly every hardware discipline: **Root-Sum-Square (RSS) statistical tolerance stacking** and **harmonic parallel combination (`{{key:x∥y}}`)**.

### Problem 11.1: Statistical Root-Sum-Square (RSS) Mechanical Tolerance Stackup
A precision bearing shaft assembly stacks three CNC-machined shoulder dimensions with bilateral $3\sigma$ tolerances: $\sigma_1 = \pm 0.04\text{ mm}$, $\sigma_2 = \pm 0.03\text{ mm}$, and $\sigma_3 = \pm 0.12\text{ mm}$.
* **Worst-Case Linear Stackup:** $0.04 + 0.03 + 0.12 = \pm 0.190\text{ mm}$ (overly conservative, forcing expensive grinding operations).
* **Statistical RSS Stackup ($\sigma_{\text{RSS}} = \sqrt{\sigma_1^2 + \sigma_2^2 + \sigma_3^2}$):**
  * **Keystrokes:** `{{res:sc32_13_eng_rss_tolerance:keys}}` $\rightarrow$ **`±{{res:sc32_13_eng_rss_tolerance:value}}`** ($31.6\%$ tighter than worst-case, validating standard turning tolerances!).

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `0.04` — Enter 0.04 into Register $X$ ($X = 0.04$).
2. `{{key:x²}}` — Square Register $X$ in place ($0.04^2$) $\rightarrow$ ($X = 0.0016$).
3. `0.03` — Enter 0.03 into Register $X$ ($Y = 0.0016, X = 0.03$).
4. `{{key:x²}}` — Square Register $X$ in place ($0.03^2$) $\rightarrow$ ($Y = 0.0016, X = 0.0009$).
5. `{{key:+}}` — Sum squared tolerances ($0.0016 + 0.0009 = 0.0025$).
6. `0.12` — Enter 0.12 into Register $X$ ($Y = 0.0025, X = 0.12$).
7. `{{key:x²}}` — Square Register $X$ in place ($0.12^2$) $\rightarrow$ ($Y = 0.0025, X = 0.0144$).
8. `{{key:+}}` — Sum third squared tolerance ($0.0025 + 0.0144 = 0.0169$).
9. `{{key:√x}}` — Extract the principal square root $\sqrt{X}$ in place $\rightarrow$ ($X = 0.13$).

#### Stack Trace Table:
| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 0.04 {{keycap:x²}} | 0.00 | 0.00 | 0.00 | 0.001600 | Square first tolerance σ_1 = 0.04 mm |
| 02 | 0.03 {{keycap:x²}} | 0.00 | 0.00 | 0.001600 | 0.000900 | Square second tolerance σ_2 = 0.03 mm, σ_1² lifts to Y |
| 03 | {{key:+}} | 0.00 | 0.00 | 0.00 | 0.002500 | Sum squared intermediate tolerances |
| 04 | 0.12 {{keycap:x²}} | 0.00 | 0.00 | 0.002500 | 0.014400 | Square third tolerance σ_3 = 0.12 mm, sum lifts to Y |
| 05 | {{key:+}} | 0.00 | 0.00 | 0.00 | 0.016900 | Sum all squared tolerances (total variance) |
| 06 | {{key:√x}} | 0.00 | 0.00 | 0.00 | 0.130000 | Principal square root; statistical RSS σ_RSS = ±0.130 mm |

---

### Problem 11.2: Cross-Discipline Isomorphism of the Parallel Key (`{{key:x∥y}}`)
Because the SC-32 elevates $x \parallel y = \frac{1}{1/x + 1/y} = \frac{xy}{x+y}$ to a primary function key, a practicing engineer solves five distinct physical domains with the exact same 3-keystroke gesture:
1. **Parallel Resistors ($R_1 \parallel R_2$):** `100 {{key:ENTER}} 250 {{key:x∥y}}` $\rightarrow$ $71.43\text{ }\Omega$.
2. **Series Capacitors ($C_1 = 47\text{ }\mu\text{F}$ in series with $C_2 = 22\text{ }\mu\text{F}$):**
   * **Keystrokes:** `{{res:sc32_13_eng_series_capacitors:keys}}` $\rightarrow$ **`{{res:sc32_13_eng_series_capacitors:value}}`**.
3. **Series Mechanical Springs ($k_1$ in series with $k_2$):** $k_{\text{eq}} = k_1 \parallel k_2$.
4. **Parallel Thermal Spreading Paths ($\theta_{JA,1} \parallel \theta_{JA,2}$):** $\theta_{\text{eq}} = \theta_1 \parallel \theta_2$.
5. **Gaussian Thin Lens Focal Length ($\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$):** $f = d_o \parallel d_i$.

#### Stack Trace Table (Series Capacitors $C_1 \parallel C_2$):
| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | 47 {{key:ENTER}} | 0.00 | 0.00 | 47.000000 | 47.000000 | First capacitor C_1 = 47 μF entered into Y |
| 02 | 22 {{key:x∥y}} | 0.00 | 0.00 | 0.00 | 14.985507 | Harmonic parallel operator yields series C_eq = 14.99 μF |

---

## Teaching & Instrument Architecture Notes

### Cross-Disciplinary Mathematical Isomorphisms via `{{key:x∥y}}`
In engineering education, students frequently encounter identical mathematical harmonic structures masked by disparate domain-specific notations. The Gaussian thin-lens equation ($\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$), parallel electrical resistance ($R_1 \parallel R_2$), series mechanical spring compliance ($k_{\text{eq}} = k_1 \parallel k_2$), and parallel thermal spreading resistance ($\theta_{\text{eq}} = \theta_1 \parallel \theta_2$) all share the exact harmonic mean formulation $f(x, y) = \frac{xy}{x+y}$. By providing the dedicated hardware operator `{{key:x∥y}}`, the SC-32 enables students and engineers to execute these computations in three keystrokes without intermediate reciprocal transformations. Eliminating syntax overhead reinforces structural intuition and dimensional consistency across physical disciplines.

### Applied Multiphysics Modeling & Parameter Grounding
Connecting mathematical principles directly to physical hardware parameters grounds theoretical problem-solving. Evaluating volumetric melt constraints ($16.2\text{ mm}^3/\text{s}$) in fused filament fabrication prevents extruder slippage; evaluating orbital velocity increments via Tsiolkovsky's equation ($\Delta v = v_e \ln(m_0/m_f)$) or Vis-viva orbital energy states bridges classical Newtonian mechanics and space mission telemetry; and modeling reverberation decay times ($RT_{60}$) grounds differential wave attenuation in architectural spaces.

### Flight-Deck Stack Dynamics & Numerical Stability
Classic scientific instruments (such as the HP-41C and HP-42S) established RPN as the gold standard for aerospace and field engineering due to stack determinism and transparent error propagation. On the SC-32, evaluating complex physical pipelines—such as polar coordinate traverse closures via `{{key:▸y,x}} {{key:Σ+}}` or rocket burnout velocities via Romberg quadrature—utilizes the 4-level stack as an immediate telemetry register set. Register $X$ displays current status while Registers $Y, Z, T$ preserve upstream physical constraints without volatile memory allocation.

---

## Diagnostic Checkpoints & Singularity Handling

<div class="admonition warning">
<p class="admonition-title">Diagnostic Checkpoint 13.1: Angular Mode Discipline in Surveying & Flight</p>
<p>Civil surveying traverse calculations (Case 6) require **Degrees mode (`{{key:DEG}}`)** for field compass azimuths. Conversely, orbital mechanics and sinusoidal harmonic phasors require **Radians mode (`{{key:RAD}}`)**. Always verify the active annunciator before executing trigonometric conversions.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Diagnostic Checkpoint 13.2: Temperature Scales in Thermodynamic Cycles</p>
<p>In Carnot, Brayton, and Arrhenius equations (Cases 2 & 8), temperatures MUST be entered in absolute thermodynamic temperature (**Kelvin**). Entering temperatures in Celsius ($^\circ\text{C}$) yields meaningless or negative efficiencies!</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Diagnostic Checkpoint 13.3: Thin Lens Inversion Singularity ($d_o = f$)</p>
<p>When an object is placed exactly at the focal point of a lens ($d_o = f$), the image forms at infinity ($d_i = \infty$). Attempting to compute $d_i$ via $\frac{f \times d_o}{d_o - f}$ triggers division by zero (`ERROR 0: DIVIDE BY ZERO`).</p>
</div>

---

## Summary & Looking Ahead

Chapter 13 demonstrated the power of Reverse Polish Notation across multifaceted, real-world engineering disciplines. From optimizing volumetric extrusion rates in additive manufacturing and integrating multi-stage rocket trajectories with Tsiolkovsky's equation, to designing second-order acoustic crossover networks, analyzing structural column buckling, and closing geodetic surveying traverses, you experienced how the 4-register stack operates as a real-time engineering telemetry buffer. By exploiting harmonic parallel combinations via `{{key:x∥y}}` and preserving physical invariants across chained calculations, complex engineering designs resolved without cognitive friction.

With complete mastery of physical hardware, transcendental mathematics, numerical solvers, and applied engineering disciplines, one final proving ground remains: extreme-speed execution under competitive examination pressure. In **Chapter 14: High-Speed Equation Entry & Inside-Out Calculation Mastery**, you will master the art of the 30-minute, 70-problem sprint. You will deploy inside-out sight-reading, parenthesis-free continued fractions, radical pyramid cascades, and official proctor baseline resets to execute calculations with championship velocity and unshakeable accuracy.

