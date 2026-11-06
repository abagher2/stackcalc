---
title: "Appendix A: Cross-Domain Governing Equations & Physical Constants"
description: "Complete reference compendium of governing equations, physical constants, and stack argument conventions across the nine StackCalc domain calculators (SC-35 through SC-95)."
---

# Appendix A: Cross-Domain Governing Equations & Physical Constants

> **Who this is for:** Practicing engineers, surveyors, tradespeople, lab analysts, clinicians, and quantitative analysts who need a rapid, single-glance desk reference of the governing mathematical equations, physical constants, and four-register stack (`T, Z, Y, X`) argument conventions across all nine instruments in the StackCalc Domain Series.

---

## 1. Universal RPN Stack & Precision Conventions

Across every instrument in the StackCalc Domain Series, all calculations execute inside a deterministic four-register operational stack (`T, Z, Y, X`) backed by IEEE 754 double-precision floating-point arithmetic (64-bit, 53-bit significand, $\approx 15\text{–}17$ significant decimal digits):

| Register | Operational Role | Behavior on Binary Operation (`+`, `-`, `×`, `÷`, `yˣ`) | Behavior on `ENTER` |
| :--- | :--- | :--- | :--- |
| **Register $T$** | Top / 4th Level | Replicates downward into $Z$ ($T' = T$) when stack drops | Receives prior $Z$ ($T' = Z$) |
| **Register $Z$** | 3rd Stack Level | Drops into $Y$ ($Z' = T$) | Receives prior $Y$ ($Z' = Y$) |
| **Register $Y$** | 2nd Operand Level | Consumed as left operand ($Y \circ X$); receives prior $Z$ | Replicates $X$ ($Y' = X$) |
| **Register $X$** | Active Display Line | Consumed as right operand; receives result $f(Y, X)$ | Remains in $X$ (lift disabled for next digit) |

---

## 2. Geomatics, Land Surveying & Flight Navigation (SC-35)

### 2.1 Sexagesimal Angle Conversion (`D.MMSS`)
Packed sexagesimal format encodes degrees ($D$), arc-minutes ($M \in [0, 59]$), and arc-seconds ($S \in [0, 59.99]$) as $D + M/100 + S/10000$. Conversion to decimal degrees ($\theta_{\text{dec}}$) follows:

$$\theta_{\text{dec}} = D + \frac{M}{60} + \frac{S}{3600}$$

### 2.2 Forward & Inverse Coordinate Geometry (COGO)
Given Station $A$ at $(N_1, E_1)$, horizontal distance $D$, and clockwise North azimuth $\alpha$:

$$N_2 = N_1 + D \cos\alpha, \qquad E_2 = E_1 + D \sin\alpha$$

Given two stations $(N_1, E_1)$ and $(N_2, E_2)$ with $\Delta N = N_2 - N_1$ and $\Delta E = E_2 - E_1$:

$$D = \sqrt{(\Delta N)^2 + (\Delta E)^2}, \qquad \alpha = \operatorname{atan2}(\Delta E, \Delta N) \pmod{360^\circ}$$

### 2.3 Bowditch Compass Rule Traverse Adjustment
For a closed polygon traverse of perimeter $P = \sum D_i$ with linear misclosure $E_{\text{mis}} = \sqrt{(\Sigma \Delta N)^2 + (\Sigma \Delta E)^2}$:

$$\delta N_i = -\Sigma \Delta N \cdot \frac{D_i}{P}, \qquad \delta E_i = -\Sigma \Delta E \cdot \frac{D_i}{P}, \qquad \text{Precision Ratio} = 1 : \frac{P}{E_{\text{mis}}}$$

### 2.4 Aviation Wind Triangle, Crosswind & Density Altitude
With runway heading $\psi$, wind direction $\theta_w$, wind speed $V_w$, and true airspeed $V_{\text{TAS}}$:

$$V_{\text{XW}} = V_w \sin(\theta_w - \psi), \qquad V_{\text{HW}} = V_w \cos(\theta_w - \psi), \qquad \text{WCA} = \arcsin\!\left(\frac{V_{\text{XW}}}{V_{\text{TAS}}}\right)$$

$$\text{PA} = \text{Elev} + 1000 \times (29.92 - \text{Alt}_{\text{inHg}}), \qquad \text{DA} \approx \text{PA} + 120 \times (T_{\text{OAT}} - T_{\text{ISA}})$$

where standard temperature at altitude is $T_{\text{ISA}} = 15^\circ\text{C} - 2^\circ\text{C} \times (\text{PA} / 1000\text{ ft})$.

---

## 3. Industrial Trades, Electrical & Mechanical (SC-14)

### 3.1 Framing Trigonometry & Hip/Valley Rafters
For a roof with unit rise $U$ (inches per $12\text{ in}$ of horizontal run) and span $S$ (where run $R = S/2$):

$$\theta = \arctan\!\left(\frac{U}{12}\right), \qquad L_{\text{common}} = R \sqrt{1 + \left(\frac{U}{12}\right)^2}, \qquad L_{\text{hip}} = R \sqrt{2 + \left(\frac{U}{12}\right)^2}$$

### 3.2 Electrical Conduit Offset Bends & Shrink
To clear an obstruction of height $O$ using two equal bends of angle $\theta$:

$$L_{\text{travel}} = O \cdot \csc\theta = \frac{O}{\sin\theta}, \qquad S_{\text{shrink}} = O \cdot \tan\!\left(\frac{\theta}{2}\right)$$

| Bend Angle ($\theta$) | Travel Multiplier ($\csc\theta$) | Shrink per Inch of Offset ($\tan(\theta/2)$) |
| :--- | :--- | :--- |
| **$10^\circ$** | $5.759 \times O$ | $0.087\text{ in/in}$ ($\approx 1/16\text{ in}$) |
| **$22.5^\circ$** | $2.613 \times O$ | $0.199\text{ in/in}$ ($\approx 3/16\text{ in}$) |
| **$30^\circ$** | $2.000 \times O$ | $0.268\text{ in/in}$ ($\approx 1/4\text{ in}$) |
| **$45^\circ$** | $1.414 \times O$ | $0.414\text{ in/in}$ ($\approx 3/8\text{ in}$) |
| **$60^\circ$** | $1.155 \times O$ | $0.577\text{ in/in}$ ($\approx 9/16\text{ in}$) |

### 3.3 Three-Phase AC Power & NEC Conductor Voltage Drop
For a balanced three-phase load with line-to-line voltage $V_{LL}$, line current $I_L$, power factor $\cos\phi$, one-way run length $L$ (feet), conductor circular mils $\text{CM}$, and resistivity constant $K$ ($12.9\,\Omega\cdot\text{CM/ft}$ for copper, $21.2\,\Omega\cdot\text{CM/ft}$ for aluminum):

$$P_{3\phi} = \sqrt{3} \cdot V_{LL} \cdot I_L \cdot \cos\phi, \qquad V_{\text{drop}, 3\phi} = \frac{\sqrt{3} \cdot K \cdot I_L \cdot L}{\text{CM}}, \qquad V_{\text{drop}, 1\phi} = \frac{2 \cdot K \cdot I_L \cdot L}{\text{CM}}$$

---

## 4. Systems Programming, Embedded & Cyber Operations (SC-16)

### 4.1 Two's Complement Signed Integer Representation
In an $N$-bit word ($N \in \{8, 16, 32, 64\}$), a bit vector $b_{N-1}b_{N-2}\dots b_1 b_0$ represents the signed integer:

$$V_{\text{signed}} = -b_{N-1} 2^{N-1} + \sum_{k=0}^{N-2} b_k 2^k, \qquad -x \equiv (\sim x + 1) \pmod{2^N}$$

### 4.2 IEEE 754 Single-Precision (32-Bit) Floating-Point Layout
For sign bit $s \in \{0, 1\}$, 8-bit biased exponent $E \in [1, 254]$, and 23-bit fractional mantissa $M$:

$$x = (-1)^s \times \left(1 + \frac{M}{2^{23}}\right) \times 2^{E - 127}$$

### 4.3 Cryptographic Modular Exponentiation, Shannon Entropy & CIDR
Fast square-and-multiply modular exponentiation (`[MOD]`, `[yˣ]`):

$$C = M^e \pmod n$$

Shannon information entropy $H(X)$ (bits per symbol) and IPv4 CIDR usable host capacity for prefix $/P$:

$$H(X) = -\sum_{i=1}^{m} p_i \log_2 p_i, \qquad N_{\text{hosts}} = 2^{32 - P} - 2$$

---

## 5. Cinema Optics, Broadcast Timecode & Sound (SC-24)

### 5.1 SMPTE Timecode & NTSC 29.97 Drop-Frame Compensation
Actual NTSC broadcast frame rate is $f_{\text{NTSC}} = 30 \times 1000 / 1001 \approx 29.97002997\text{ fps}$. Over one hour, a nominal $30\text{ fps}$ counter drifts by $+108\text{ frames}$ ($+3.6\text{ s}$). Drop-Frame (`29.97 DF`) drops frame numbers `:00` and `:01` at the start of every minute except minutes divisible by $10$:

$$N_{\text{dropped/hr}} = 60 \times 2 - 6 \times 2 = 108\text{ frames/hr}$$

### 5.2 Hyperfocal Distance, Depth of Field & Rotary Shutter Exposure
For lens focal length $f$, aperture $N$ ($f$-stop or $T$-stop), circle of confusion $c$, and focus distance $d$:

$$H = \frac{f^2}{N \cdot c} + f, \qquad D_{\text{near}} = \frac{H \cdot d}{H + (d - f)}, \qquad D_{\text{far}} = \frac{H \cdot d}{H - (d - f)} \quad (d < H)$$

For frame rate $\text{FPS}$ and rotary shutter angle $\theta_{\text{shutter}}$ (degrees):

$$t_{\text{exp}} = \frac{\theta_{\text{shutter}}}{360^\circ \times \text{FPS}}$$

---

## 6. RF Spectrum, Transmission Lines & Microwave (SC-50)

### 6.1 Decibel Power & Voltage Ratios
$$G_{\text{dB}} = 10 \log_{10}\!\left(\frac{P_2}{P_1}\right) = 20 \log_{10}\!\left(\frac{V_2}{V_1}\right), \qquad P_{\text{dBm}} = 10 \log_{10}\!\left(\frac{P_{\text{watts}}}{1\text{ mW}}\right)$$

### 6.2 Reflection Coefficient ($\Gamma$), VSWR, Return Loss & Mismatch Loss
For characteristic impedance $Z_0$ and load impedance $Z_L$:

$$\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}, \qquad \text{VSWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|}, \qquad \text{RL}_{\text{dB}} = -20 \log_{10}|\Gamma|, \qquad \text{ML}_{\text{dB}} = -10 \log_{10}\!\left(1 - |\Gamma|^2\right)$$

### 6.3 Friis Free-Space Path Loss & Thermal Noise Floor
$$\text{FSPL}_{\text{dB}} = 20 \log_{10}(d) + 20 \log_{10}(f) + 20 \log_{10}\!\left(\frac{4\pi}{c}\right), \qquad N_{\text{dBm}} = -174\text{ dBm/Hz} + 10 \log_{10}(B_{\text{Hz}}) + \text{NF}_{\text{dB}}$$

---

## 7. Wet-Lab Chemistry, Stoichiometry & Spectroscopy (SC-60)

### 7.1 Molarity, Dilutions & Beer-Lambert Spectrophotometry
$$M = \frac{m_{\text{g}}}{\text{MW}_{\text{g/mol}} \times V_{\text{L}}}, \qquad C_1 V_1 = C_2 V_2, \qquad A = -\log_{10}\!\left(\frac{I}{I_0}\right) = \varepsilon \cdot \ell \cdot c$$

### 7.2 pH, Henderson-Hasselbalch Buffers & Arrhenius Kinetics
$$\text{pH} = -\log_{10}[\text{H}^+], \qquad \text{pH} = \text{p}K_a + \log_{10}\!\left(\frac{[\text{A}^-]}{[\text{HA}]}\right), \qquad \ln\!\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$$

where the universal gas constant is $R = 8.3144626\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$ and Avogadro's constant is $N_A = 6.02214076 \times 10^{23}\text{ mol}^{-1}$.

---

## 8. Commercial Bakery, Fermentation Science & Brewing (SC-78)

### 8.1 Baker's Percentage & Desired Dough Temperature (DDT)
$$\text{Baker's \%}_i = \frac{W_i}{W_{\text{total flour}}} \times 100\%, \qquad T_{\text{water}} = 3 \times \text{DDT} - \left(T_{\text{room}} + T_{\text{flour}} + F_{\text{friction}}\right)$$

### 8.2 Brewing Gravity, Alcohol by Volume (ABV), Strike Water & IBUs
$$\text{ABV\%} = (\text{OG} - \text{FG}) \times 131.25, \qquad T_{\text{strike}} = \frac{0.2}{R_{\text{qt/lb}}}\left(T_{\text{target}} - T_{\text{grain}}\right) + T_{\text{target}}$$

$$\text{IBU} = \frac{W_{\text{oz}} \times \text{AA\%} \times U_{\text{Tinseth}} \times 7489}{V_{\text{gal}}}$$

---

## 9. Clinical Nursing, Hospital Pharmacy & Infusions (SC-80)

### 9.1 Body Surface Area (Mosteller) & Ideal / Adjusted Body Weight
$$\text{BSA}\ (\text{m}^2) = \sqrt{\frac{\text{Height}_{\text{cm}} \times \text{Weight}_{\text{kg}}}{3600}}, \qquad \text{ABW}_{\text{kg}} = \text{IBW}_{\text{kg}} + 0.4\left(\text{Actual}_{\text{kg}} - \text{IBW}_{\text{kg}}\right)$$

where Devine Ideal Body Weight is $\text{IBW}_{\text{male}} = 50 + 2.3(H_{\text{in}} - 60)$ and $\text{IBW}_{\text{female}} = 45.5 + 2.3(H_{\text{in}} - 60)$.

### 9.2 Cockcroft-Gault Creatinine Clearance & Infusion Pump Rates
$$\text{CrCl}\ (\text{mL/min}) = \frac{(140 - \text{Age}_{\text{yr}}) \times \text{Weight}_{\text{kg}}}{72 \times \text{SCr}_{\text{mg/dL}}} \times (0.85\text{ if female})$$

$$\text{Rate}\ (\text{mL/hr}) = \frac{\text{Dose}_{\text{mcg/kg/min}} \times \text{Weight}_{\text{kg}} \times 60\text{ min/hr}}{\text{Concentration}_{\text{mcg/mL}}}, \qquad \text{Drops/min} = \frac{V_{\text{mL}} \times D_{\text{gtt/mL}}}{t_{\text{min}}}$$

---

## 10. Quantitative Finance, Actuarial Science & Six Sigma (SC-95)

### 10.1 Compound Time Value of Money (TVM) & Net Present Value (NPV)
$$PV(1 + i)^N + PMT \cdot \frac{(1 + i)^N - 1}{i} \cdot (1 + i \cdot \text{mode}) + FV = 0, \qquad \text{NPV} = CF_0 + \sum_{t=1}^{T} \frac{CF_t}{(1 + r)^t}$$

### 10.2 Six Sigma Process Capability ($C_p$, $C_{pk}$) & Black-Scholes Option Pricing
$$C_p = \frac{\text{USL} - \text{LSL}}{6\hat{\sigma}}, \qquad C_{pk} = \min\!\left(\frac{\text{USL} - \mu}{3\hat{\sigma}},\; \frac{\mu - \text{LSL}}{3\hat{\sigma}}\right)$$

$$C = S_0 \Phi(d_1) - K e^{-rT} \Phi(d_2), \qquad d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}$$
