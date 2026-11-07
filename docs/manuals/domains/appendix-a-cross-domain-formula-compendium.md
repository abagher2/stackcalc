---
title: "Appendix A: Cross-Domain Formula & Equation Compendium"
description: "Complete reference compendium of governing equations, physical constants, and stack argument conventions across the nine StackCalc domain calculators (SC-35 through SC-95, Units I–IX, Chapters 1–27)."
---

# Appendix A: Cross-Domain Formula & Equation Compendium

This compendium consolidates the governing mathematical identities, physical constants, four-register RPN stack conventions, and bidirectional Equation Solver Workspace schemas across all nine specialized instruments in the StackCalc Domain Series (`SC-35`, `SC-14`, `SC-16`, `SC-24`, `SC-50`, `SC-60`, `SC-78`, `SC-80`, and `SC-95`). Each section summarizes the first-principles equations derived across Units I through IX (Chapters 1 through 27) so engineers, navigators, clinicians, and analysts can verify input dimensions, immediate stack arguments, and closed-form or numerical solver relationships at a glance.

## Universal Three-Pillar Stack, Precision, and Bidirectional Solver Conventions

Every instrument in the StackCalc Domain Series shares a common **three-pillar computational architecture** backed by IEEE 754 double-precision floating-point arithmetic ($64\text{-bit}$ word, $53\text{-bit}$ binary significand, providing $15$ to $17$ significant decimal digits) and selectable fixed-width integer arithmetic on the `SC-16`:

1. **Configurable RPN Stack Depth ({{keycap:4-LV}}, {{keycap:8-LV}}, or {{keycap:INF}} via {{key:sc35:FLAGS}}):** Practitioners can operate with a classic four-register $(X, Y, Z, T)$ operational stack ({{keycap:4-LV}}), expand to an eight-register stack ({{keycap:8-LV}}), or enable unbounded stack capacity ({{keycap:INF}}) for multi-branch field derivations. Across all stack configurations, the active four-register window at the bottom of the stack (`Register T`, `Register Z`, `Register Y`, `Register X`) obeys deterministic RPN lift and drop semantics:

| Register | Operational Role | Behavior on Binary Operation ({{key:+}}, {{key:-}}, {{key:×}}, {{key:÷}}, {{key:yˣ}}) | Behavior on {{key:ENTER}} |
| :--- | :--- | :--- | :--- |
| **Register $T$** | Top / 4th Visible Level | Replicates downward into $Z$ ($T' = T$) in {{keycap:4-LV}} mode (or drops from `R5` in {{keycap:8-LV}}/{{keycap:INF}}) | Receives prior $Z$ ($T' = Z$) |
| **Register $Z$** | 3rd Stack Level | Drops into $Y$ ($Z' = T$) | Receives prior $Y$ ($Z' = Y$) |
| **Register $Y$** | 2nd Operand Level | Consumed as left operand ($Y \circ X$); receives prior $Z$ | Replicates $X$ ($Y' = X$) |
| **Register $X$** | Active Display Line | Consumed as right operand; receives result $f(Y, X)$ | Remains in $X$ (lift disabled for next digit) |

2. **Dual-Mode Domain Keys (Immediate RPN Stack Shortcuts + Bidirectional Equation Solver Workspaces):**
   - **Immediate Stack Mode:** Pressing a domain key when arguments are staged in Registers $Z$, $Y$, and $X$ evaluates the forward physical transformation in a single keystroke while automatically injecting embedded physical constants ({{key:sc50:c}}, {{key:sc50:kB}}, {{key:sc60:R}}, {{key:sc60:F}}, {{key:sc35:g₀}}, {{key:sc14:ρw}}) and regulatory lookup tables (NEC Table 8 wire gauges, IUPAC atomic masses).
   - **Bidirectional Equation Solver Workspace ({{key:sc35:SOLVE}} / {{key:XEQ}} + Softkeys {{keycap:LFU0}}–{{keycap:LFU5}}):** Opening a domain key's Equation Workspace renders the governing equation across Line 1 of the LCD and binds the six top-row softkeys ({{keycap:LFU0}}–{{keycap:LFU5}}) to its symbolic variables. Storing known values in any order and pressing {{key:sc35:SOLVE}} (or {{key:XEQ}}) followed by the target variable softkey solves the governing law **forward or backward for any unknown parameter** via exact algebraic isolation or Secant–Brent numerical root-finding.
3. **Domain Modes, Native Input Parsers, and Live Reference Ledgers ({{key:sc35:▦}}):** Native domain entry modes ({{key:sc35:▸HMS}} via {{key:sc35:▸HR}}/{{key:sc35:▸HMS}}, {{key:sc14:f-i}} via {{key:sc14:f-i}}, {{key:sc16:HEX}}/{{key:sc16:DEC}}/{{key:sc16:OCT}}/{{key:sc16:BIN}} + {{key:sc16:WSZ}} + {{key:sc16:NEG}}, {{key:sc24:TC}} + {{key:sc24:FPS}}, chemical formula entry via {{key:sc60:Z}}) and the non-destructive Reference Table ({{key:sc35:▦}}) maintain live domain ledgers (`@COGO`, `@BK%`, `@PAT`/`@MAR`, and bivariate statistical accumulators).

### Cross-Domain Mathematical Isomorphisms

Across the nine physical trades, identical mathematical structures recur under domain-specific physical variables:

| Mathematical Structure | Governing Law Form | Domain Instantiations Across Units I–IX |
| :--- | :--- | :--- |
| **First-Order Exponential Decay & Discounting** | $y(t) = y_0 \, e^{-\lambda t}$ | **Unit III (`SC-16`):** RC settling $v_C(t) = V_{\text{in}}(1 - e^{-t/\tau})$ ({{key:sc16:τ}}, {{key:sc16:PWM}}, {{key:sc16:BPS}}) • **Unit VI (`SC-60`):** Beer–Lambert transmittance $I/I_0 = 10^{-\varepsilon \ell c}$ ({{key:sc60:εbc}}, {{key:sc60:εbc}}, {{key:sc60:C₁V₁}}) & Arrhenius kinetics $k = A e^{-E_a/(RT)}$ ({{key:sc60:Eₐ}}, {{key:sc60:t½}}, {{key:sc60:Kₑq}}, {{key:sc60:ΔG}}, {{key:sc60:E°}}) • **Unit VIII (`SC-80`):** One-compartment drug elimination $C(t) = C_0 e^{-k_e t}$ ({{key:sc80:PK}}, {{key:sc80:GFR}}, {{key:sc80:BSA}}, {{key:sc80:IBW}}, {{key:sc80:ABW}}, {{key:sc80:DOS}}, {{key:sc80:DRP}}, {{key:sc80:IV}}) • **Unit IX (`SC-95`):** Multi-period and continuous discounting ({{key:sc95:TVM}}, {{key:sc95:AMR}}, {{key:sc95:CF}}, {{key:sc95:BND}}, {{key:sc95:EAR}}, {{key:sc95:CGR}}, {{key:sc95:ROI}}, {{key:sc95:pN}}, {{key:sc95:qN}}) |
| **Logarithmic Ratio Compression** | $L = \kappa \log_{10}(X / X_{\text{ref}})$ | **Unit IV (`SC-24`):** Acoustic sound pressure level $\text{SPL} = 20\log_{10}(p/p_0)$ ({{key:sc24:SPL}}, {{key:sc24:dB}}, {{key:sc24:SPL}}, {{key:sc24:EV}}, {{key:sc24:DOF}}, {{key:sc24:FOV}}, {{key:sc24:FOV}}, {{key:sc24:TC}}, {{key:sc24:+TC}}, {{key:sc24:-TC}}, {{key:sc24:FPS}}) • **Unit V (`SC-50`):** RF power ({{key:sc50:dBm}}, {{key:sc50:▸dBm}}, {{key:sc50:dBm}}), Friis path loss ({{key:sc50:FSL}}, {{key:sc50:LNK}}, {{key:sc50:LNK}}, {{key:sc50:F₁}}), and noise cascade ({{key:sc50:NF}}, {{key:sc50:Pₙ}}, {{key:sc50:IP3}}, {{key:sc50:FDR}}) • **Unit VI (`SC-60`):** Sørensen acidity $\text{pH} = -\log_{10}[\text{H}^+]$ ({{key:sc60:pH}}, {{key:sc60:pKₐ}}, {{key:sc60:BUF}}, {{key:sc60:EQV}}, {{key:sc60:MW}}, {{key:sc60:MW}}, {{key:sc60:w/w}}, {{key:sc60:PVT}}, {{key:sc60:RCF}}) |
| **Shannon Information & Quantization Capacity** | $C = B \log_2(1 + \text{SNR})$ | **Unit III (`SC-16`):** $N$-bit ADC dynamic range ({{key:sc16:ADC}}, {{key:sc16:DAC}}, {{key:sc16:CRC}}, {{key:sc16:NET}}, {{key:sc16:FLT}}, {{key:sc16:END}}, {{key:sc16:#B}}, {{key:sc16:CLZ}}, {{key:sc16:MSK}}, {{key:sc16:SB}}, {{key:sc16:CB}}, {{key:sc16:B?}}) • **Unit V (`SC-50`):** Shannon–Hartley channel capacity ({{key:sc50:C/B}}, {{key:sc50:Δf}}, {{key:sc50:RCS}}, {{key:sc50:f₀}}, {{key:sc50:f₀}}, {{key:sc50:λ/L}}) |
| **Euclidean & Stoichiometric Decomposition** | $r = \sqrt{x^2 + y^2}$ | **Unit I (`SC-35`):** Survey inverse ({{key:sc35:INV}}, {{key:sc35:TRV}}, {{key:sc35:BRG}}, {{key:sc35:SLP}}, {{key:sc35:GR%}}, {{key:sc35:CUT}}, {{key:sc35:△}}, {{key:sc35:FLW}}) & wind triangle ({{key:sc35:WND}}, {{key:sc35:XWC}}, {{key:sc35:WND}}, {{key:sc35:ALT}}, {{key:sc35:TSD}}) • **Unit II (`SC-14`):** Conduit & rafter geometry ({{key:sc14:OFS}}, {{key:sc14:MIT}}, {{key:sc14:FIT}}, {{key:sc14:BC}}, {{key:sc14:SFM}}, {{key:sc14:TAP}}), three-phase power ({{key:sc14:PF}}, {{key:sc14:PF}}, {{key:sc14:PF}}, {{key:sc14:PF}}, {{key:sc14:AWG}}, {{key:sc14:FLA}}, {{key:sc14:MTR}}), and process hydraulics ({{key:sc14:PIP}}, {{key:sc14:Cᵥ}}, {{key:sc14:PMP}}, {{key:sc14:NPH}}, {{key:sc14:mA}}, {{key:sc14:RTD}}) • **Unit V (`SC-50`):** Complex impedance & VSWR ({{key:sc50:CMPLX}}, {{key:sc50:Z₀}}, {{key:sc50:Γ}}, {{key:sc50:SWR}}, {{key:sc50:RL}}, {{key:sc50:RL}}, {{key:sc50:Z₀}}) • **Unit VII (`SC-78`):** Culinary & zymurgy scaling ({{key:sc78:BK%}}, {{key:sc78:BK%}}, {{key:sc78:ΣW}}, {{key:sc78:DIV}}, {{key:sc78:Tw}}, {{key:sc78:ICE}}, {{key:sc78:MSH}}, {{key:sc78:▸SG}}, {{key:sc78:ABV}}, {{key:sc78:IBU}}, {{key:sc78:SRM}}, {{key:sc78:TDS}}, {{key:sc78:YLD}}, {{key:sc78:CST}}, {{key:sc78:PRC}}, {{key:sc78:Aw}}, {{key:sc78:SO₂}}, {{key:sc78:CO₂}}) • **Unit IX (`SC-95`):** Unit economics & Six Sigma ({{key:sc95:MGN}}, {{key:sc95:MKP}}, {{key:sc95:BEP}}, {{key:sc95:EOQ}}, {{key:sc95:Cpk}}, {{key:sc95:SPC}}, {{key:sc95:CI}}, {{key:sc95:z₀}}, {{key:sc95:t₂}}, {{key:sc95:A/B}}, {{key:sc95:n*}}) |

---

## Geomatics, Land Surveying, and Flight Navigation

Covered in [Unit I, Chapters 1–3](01-sc35-geomatics-navigation.md), the **SC-35** geomatics and flight-navigation instrument links sexagesimal angular encoding (`DDD.MMSS` via {{key:sc35:▸HR}} and {{key:sc35:▸HMS}}), plane coordinate geometry ({{key:sc35:TRV}}, {{key:sc35:INV}}, {{key:sc35:PT+}}, {{key:sc35:CLS}}), horizontal and vertical highway curves ({{key:sc35:CRV}}, {{key:sc35:VCV}}), differential leveling ({{key:sc35:LVL}}), and atmospheric flight mechanics ({{key:sc35:TSD}}, {{key:sc35:WND}}, {{key:sc35:XWC}}, {{key:sc35:ALT}}, {{key:sc35:CG}}).

### Sexagesimal Angle Conversion and Horizontal/Vertical Curves

Packed sexagesimal format (`DDD.MMSS`) encodes integer degrees $D$, arc-minutes $M \in [0, 59]$, and arc-seconds $S \in [0, 59.99]$ as $D + M/100 + S/10{,}000$, converting to decimal degrees $\theta_{\text{dec}}$ ({{key:sc35:▸HR}}, with inverse {{key:sc35:▸HMS}}), while the {{key:sc35:CRV}} ({{key:sc35:CRV}}) Equation Workspace (`L = R × D × π / 180` on {{keycap:LFU0}}–{{keycap:LFU2}}: {{keycap:L}}, {{keycap:R}}, {{keycap:D}}) relates circular arc length $L$, radius $R$, tangent $T = R\tan(D/2)$, and central deflection angle $D$:

$$\theta_{\text{dec}} = D + \frac{M}{60} + \frac{S}{3600}, \qquad L = R \cdot D_{\text{deg}} \cdot \frac{\pi}{180^\circ}, \qquad T = R \tan\!\left(\frac{D}{2}\right)$$

### Forward and Inverse Coordinate Geometry

Given a known survey station $A$ at coordinates $(N_1, E_1)$, horizontal leg distance $D$, and clockwise North azimuth $\alpha$, forward traverse ({{key:sc35:TRV}}) computes the target station $(N_2, E_2)$, whereas inverse traverse ({{key:sc35:INV}}) recovers $D$ and $\alpha$ from coordinate differences $\Delta N = N_2 - N_1$ and $\Delta E = E_2 - E_1$:

$$N_2 = N_1 + D \cos\alpha, \qquad E_2 = E_1 + D \sin\alpha, \qquad D = \sqrt{(\Delta N)^2 + (\Delta E)^2}, \qquad \alpha = \operatorname{atan2}(\Delta E, \Delta N) \pmod{360^\circ}$$

### Bowditch Compass Rule Traverse Adjustment

For a closed polygon traverse ({{key:sc35:PT+}}, {{key:sc35:CLS}}, and the `@COGO` ledger in {{key:sc35:▦}}) of total perimeter $P = \sum D_i$ with linear misclosure $E_{\text{mis}} = \sqrt{(\Sigma \Delta N)^2 + (\Sigma \Delta E)^2}$, the Bowditch compass rule distributes closure corrections $(\delta N_i, \delta E_i)$ in proportion to leg length $D_i$:

$$\delta N_i = -\Sigma \Delta N \cdot \frac{D_i}{P}, \qquad \delta E_i = -\Sigma \Delta E \cdot \frac{D_i}{P}, \qquad \text{Precision Ratio} = 1 : \frac{P}{E_{\text{mis}}}$$

### Aviation Wind Triangle, Crosswind, and Density Altitude

With runway or course heading $\psi$, wind direction $\theta_w$ ($A = \theta_w - \psi$), wind speed $V_w$, and true airspeed $V_{\text{TAS}}$, the wind-triangle solver ({{key:sc35:WND}}, opening the {{key:sc35:WND}} workspace `X = V × SIN(A)` on {{keycap:X}}, {{keycap:V}}, {{keycap:A}}) and {{key:sc35:XWC}} decompose crosswind $V_{\text{XW}}$, headwind $V_{\text{HW}}$, and wind correction angle $\text{WCA}$, while the atmospheric solver ({{key:sc35:ALT}}, opening the {{key:sc35:ALT}} workspace `D = P + 120 × (T - 15)` on {{keycap:D}}, {{keycap:P}}, {{keycap:T}}) computes Pressure Altitude $P$ (in feet) and Density Altitude $D$ from field elevation $\text{Elev}$, altimeter setting $\text{Alt}_{\text{inHg}}$, outside air temperature $T$ ($^\circ\text{C}$), and standard temperature $T_{\text{ISA}} = 15^\circ\text{C} - 2^\circ\text{C} \times (P / 1000\text{ ft})$:

$$V_{\text{XW}} = V_w \sin(\theta_w - \psi), \qquad V_{\text{HW}} = V_w \cos(\theta_w - \psi), \qquad \text{WCA} = \arcsin\!\left(\frac{V_{\text{XW}}}{V_{\text{TAS}}}\right)$$

$$P = \text{Elev} + 1000 \times (29.92 - \text{Alt}_{\text{inHg}}), \qquad D \approx P + 120 \times (T - T_{\text{ISA}})$$

---

## Industrial Trades, Electrical, and Mechanical

Covered in [Unit II, Chapters 4–6](02-sc14-electrical-trades.md), the **SC-14** industrial trades calculator combines feet-inch-fraction ({{key:sc14:f-i}}) carpentry layout, electrical conduit offset geometry ({{key:sc14:OFS}}, {{key:sc14:MIT}}, {{key:sc14:FIT}}), National Electrical Code (NEC) power and conductor drop formulas ({{key:sc14:Ω}}, {{key:sc14:PF}}, {{key:sc14:AWG}}, {{key:sc14:FLA}}, {{key:sc14:kVA}}), and industrial process flow ({{key:sc14:PIP}}, {{key:sc14:PMP}}, {{key:sc14:Cᵥ}}, {{key:sc14:SFM}}, {{key:sc14:WLD}}, {{key:sc14:mA}}).

### Framing Trigonometry and Rafter Layout

For a pitched roof with unit rise $U$ (inches of vertical rise per $12\text{ in}$ of horizontal run) and building span $S$ (where half-span run is $R = S/2$), the framing and diagonal keys ({{key:sc14:MIT}}, {{key:sc14:FIT}}, {{key:sc14:f-i}}) evaluate roof pitch angle $\theta$, common rafter length $L_{\text{common}}$, and $45^\circ$ hip or valley rafter length $L_{\text{hip}}$:

$$\theta = \arctan\!\left(\frac{U}{12}\right), \qquad L_{\text{common}} = R \sqrt{1 + \left(\frac{U}{12}\right)^2}, \qquad L_{\text{hip}} = R \sqrt{2 + \left(\frac{U}{12}\right)^2}$$

### Electrical Conduit Offset Bends and Shrink

To clear a mechanical obstruction of height $O$ using two equal conduit bends of angle $A = \theta$ ({{key:sc14:OFS}}, with {{key:sc14:OFS}} Equation Workspace `T = O / SIN(A)` binding {{keycap:T}}, {{keycap:O}}, {{keycap:A}} on {{keycap:LFU0}}–{{keycap:LFU2}}), the center-to-center travel distance $T = L_{\text{travel}}$ along the pipe and the axial conduit pull-back shrink $S_{\text{shrink}}$ follow cosecant and half-angle tangent scaling:

$$T = O \cdot \csc\theta = \frac{O}{\sin\theta}, \qquad S_{\text{shrink}} = O \cdot \tan\!\left(\frac{\theta}{2}\right)$$

| Bend Angle ($\theta$) | Travel Multiplier ($\csc\theta$) | Shrink per Inch of Offset ($\tan(\theta/2)$) |
| :--- | :--- | :--- |
| **$10^\circ$** | $5.759 \times O$ | $0.087\text{ in/in}$ ($\approx 1/16\text{ in}$) |
| **$22.5^\circ$** | $2.613 \times O$ | $0.199\text{ in/in}$ ($\approx 3/16\text{ in}$) |
| **$30^\circ$** | $2.000 \times O$ | $0.268\text{ in/in}$ ($\approx 1/4\text{ in}$) |
| **$45^\circ$** | $1.414 \times O$ | $0.414\text{ in/in}$ ($\approx 3/8\text{ in}$) |
| **$60^\circ$** | $1.155 \times O$ | $0.577\text{ in/in}$ ($\approx 9/16\text{ in}$) |

### Three-Phase AC Power, Conductor Voltage Drop, and Control Valve Flow

For a balanced load with line-to-line voltage $V_{LL}$, line current $I_L$, power factor $F = \cos\phi$, one-way conduit run length $L$ (in feet), conductor cross-section $\text{CM}$ (in circular mils), and resistivity constant $K$ ($12.9\,\Omega\cdot\text{CM/ft}$ for copper or $21.2\,\Omega\cdot\text{CM/ft}$ for aluminum), active power ({{key:sc14:PF}} Equation Workspace `P = V × I × F`, alongside {{key:sc14:FLA}} and {{key:sc14:kVA}}) and conductor voltage drop ({{key:sc14:AWG}} Equation Workspace `D = 2 × R × L × I / 1000` on {{keycap:LFU0}}–{{keycap:LFU4}}: {{keycap:D}}, {{keycap:R}}, {{keycap:L}}, {{keycap:I}}, {{keycap:G}}, plus control valve flow `Q = C × √(P / G)` under {{key:sc14:Cᵥ}}) are:

$$P_{3\phi} = \sqrt{3} \cdot V_{LL} \cdot I_L \cdot \cos\phi, \qquad V_{\text{drop}, 3\phi} = \frac{\sqrt{3} \cdot K \cdot I_L \cdot L}{\text{CM}}, \qquad D = \frac{2 \cdot K \cdot I_L \cdot L}{\text{CM}} = \frac{2 \cdot R_{\Omega/\text{kft}} \cdot L \cdot I_L}{1000}$$

---

## Systems Programming, Embedded, and Cyber Operations

Covered in [Unit III, Chapters 7–9](03-sc16-systems-cyber.md), the **SC-16** systems and cybersecurity instrument operates on selectable fixed-width integer words (8-bit, 16-bit, 32-bit, 64-bit via {{key:sc16:WSZ}} and unsigned mode {{key:sc16:UNS}}), radix bases ({{key:sc16:HEX}}, {{key:sc16:DEC}}, {{key:sc16:OCT}}, {{key:sc16:BIN}}), IEEE 754 binary floating-point encodings ({{key:sc16:FLT}}, {{key:sc16:F16}}, {{key:sc16:F64}}), embedded timer/ADC peripherals ({{key:sc16:PWM}}, {{key:sc16:BPS}}, {{key:sc16:ADC}}, {{key:sc16:DAC}}, {{key:sc16:τ}}), and network addressing ({{key:sc16:NET}}, {{key:sc16:CRC}}, {{key:sc16:MOD}}).

### Two's Complement Signed Integer Representation and Bitwise Operators

In an $N$-bit word ($N \in \{8, 16, 32, 64\}$, cycled via {{key:sc16:WSZ}}), a binary bit vector $b_{N-1}b_{N-2}\dots b_1 b_0$ represents the signed integer value $V_{\text{signed}}$, where two's complement negation ({{key:sc16:NEG}} / {{key:+/-}}) adds $1$ to the bitwise one's complement ({{key:sc16:~}}) modulo $2^N$, and shift/mask operators ({{key:sc16:≪}}, {{key:sc16:≫}}, {{key:sc16:ASR}}, {{key:sc16:ROR}}, {{key:sc16:SB}}, {{key:sc16:CB}}, {{key:sc16:B?}}, {{key:sc16:MSK}}, {{key:sc16:&}}, {{keycap:|}}, {{key:sc16:⊕}}, {{key:sc16:~&}}, {{key:sc16:~|}}, {{key:sc16:#B}}, {{key:sc16:CLZ}}) manipulate individual register fields:

$$V_{\text{signed}} = -b_{N-1} 2^{N-1} + \sum_{k=0}^{N-2} b_k 2^k, \qquad -x \equiv (\sim x + 1) \pmod{2^N}$$

### IEEE 754 Single-Precision Floating-Point Layout and Embedded Timer/PWM Synthesis

For a 32-bit `float32` word ({{key:sc16:FLT}}, paired with byte-order swap {{key:sc16:SWP}}) partitioned into sign bit $s \in \{0, 1\}$ (bit 31), 8-bit biased exponent $E \in [1, 254]$ (bits 30–23), and 23-bit significand mantissa $M$ (bits 22–0), the real value $x$ and the hardware timer PWM frequency ({{key:sc16:PWM}} Equation Workspace `F = C / (P × A)` binding {{keycap:F}}, {{keycap:C}}, {{keycap:P}}, {{keycap:A}} on {{keycap:LFU0}}–{{keycap:LFU3}}, alongside {{key:sc16:BPS}} divisor `D = C / (16 × B)`) are:

$$x = (-1)^s \times \left(1 + \frac{M}{2^{23}}\right) \times 2^{E - 127}, \qquad F = \frac{C}{P \cdot A}, \qquad \text{BRR} = \frac{f_{\text{clk}}}{16 \times f_{\text{baud}}}$$

### Mixed-Signal ADC Quantization, RC Settling, Modular Cryptography, and CIDR

An $N$-bit successive-approximation ADC ({{key:sc16:ADC}} Equation Workspace `D = V / R × 2^N` binding {{keycap:D}}, {{keycap:V}}, {{keycap:R}}, {{keycap:N}} on {{keycap:LFU0}}–{{keycap:LFU3}}) maps analog input $V$ against reference $R$ with ideal signal-to-noise ratio $\text{SNR}_{\text{dB}} = 6.0206\,N + 1.7609\text{ dB}$ and Effective Number of Bits $\text{ENOB} = (\text{SINAD} - 1.7609)/6.0206$, while the RC anti-aliasing filter ({{key:sc16:τ}} {{key:sc16:τ}} Equation Workspace `T = R × C` binding {{keycap:T}}, {{keycap:R}}, {{keycap:C}} on {{keycap:LFU0}}–{{keycap:LFU2}}) requires $t_{\text{acq}} \ge (N + 1)\ln(2)\,\tau$ to settle within $\frac{1}{2}\text{ LSB}$. In network and cryptographic analysis ({{key:sc16:MOD}}, {{key:sc16:CRC}}, {{key:sc16:NET}}, {{key:sc16:▸KiB}}, {{key:sc16:▸MHz}}, {{key:sc16:▸ns}}), modular arithmetic, Shannon entropy $H(X)$, and IPv4 subnet host capacity follow:

$$D = \left\lfloor \frac{V}{R} \cdot 2^N \right\rfloor, \qquad t_{\text{acq}} \ge (N + 1)\ln(2)\,R C, \qquad C = M^e \pmod n, \qquad H(X) = -\sum_{i=1}^{m} p_i \log_2 p_i, \qquad N_{\text{hosts}} = 2^{32 - P} - 2$$

---

## Cinema Optics, Broadcast Timecode, and Sound

Covered in [Unit IV, Chapters 10–12](04-sc24-cinema-broadcast.md), the **SC-24** motion-picture and broadcast calculator unites SMPTE frame-accurate timecode arithmetic ({{key:sc24:TC}}, {{key:sc24:FPS}}, {{key:sc24:DF}}, {{key:sc24:+TC}}, {{key:sc24:-TC}}), geometrical camera optics ({{key:sc24:FOV}}, {{key:sc24:DOF}}, {{key:sc24:HFD}}), rotary shutter exposure ({{key:sc24:EV}}, {{key:sc24:SHT}}, {{key:sc24:LUX}}, {{key:sc24:GEL}}), and acoustic and data propagation ({{key:sc24:dB}}, {{key:sc24:SPL}}, {{key:sc24:DLY}}, {{key:sc24:BIT}}).

### SMPTE Timecode and NTSC Drop-Frame Compensation

Color NTSC broadcast video runs at $f_{\text{NTSC}} = 30 \times 1000 / 1001 \approx 29.97002997\text{ fps}$, causing a nominal $30\text{ fps}$ frame counter to drift by $+108\text{ frames}$ ($+3.6\text{ s}$) per hour. SMPTE `29.97 DF` Drop-Frame timecode ({{key:sc24:TC}}, {{key:sc24:FPS}}, {{key:sc24:DF}}, with {{key:sc24:TC}} Equation Workspace `F = S × R` on {{keycap:F}}, {{keycap:S}}, {{keycap:R}}) reconciles wall-clock time by skipping frame labels `:00` and `:01` at the start of every minute except minutes divisible by $10$:

$$N_{\text{dropped/hr}} = 60 \times 2 - 6 \times 2 = 108\text{ frames/hr}, \qquad F = S \times R$$

### Hyperfocal Distance, Depth of Field, and Rotary Shutter Exposure

For lens focal length $F$, sensor width $W$, aperture $N$ ($f$-stop or photometric $T$-stop), sensor circle of confusion $C$, focus distance $d$, frame rate $R$, and rotary shutter angle $\theta_{\text{shutter}}$ (in degrees), the optical solvers ({{key:sc24:FOV}} `A = 2 × ATAN(W / (2 × F))`, {{key:sc24:DOF}} `H = F² / (N × C)`, {{key:sc24:EV}} `N² = T × 2^E`, {{key:sc24:SHT}}, and {{key:sc24:LUX}} `E = I / D²`) evaluate field of view $A$, hyperfocal distance $H$, near and far depth-of-field limits $D_{\text{near}}$ and $D_{\text{far}}$, and frame exposure time $T$:

$$A = 2\arctan\!\left(\frac{W}{2F}\right), \qquad H = \frac{F^2}{N \cdot C}, \qquad D_{\text{near}} = \frac{H \cdot d}{H + (d - F)}, \qquad D_{\text{far}} = \frac{H \cdot d}{H - (d - F)} \quad (d < H), \qquad T = \frac{\theta_{\text{shutter}}}{360^\circ \times R}$$

---

## RF Spectrum, Transmission Lines, and Microwave

Covered in [Unit V, Chapters 13–15](05-sc50-rf-spectrum.md), the **SC-50** radio-frequency and microwave engineering instrument evaluates logarithmic power ratios ({{key:sc50:dBm}}, {{key:sc50:▸dBm}}, {{key:sc50:dBm}}, {{key:sc50:▸dBW}}, {{key:sc50:▸dBV}}, {{key:sc50:▸μV}}), resonant LC and waveguide structures ({{key:sc50:f₀}}, {{key:sc50:fc}}, {{key:sc50:λ/L}}), transmission-line impedance mismatches ({{key:sc50:Γ}}, {{key:sc50:SWR}}, {{key:sc50:TLN}}), free-space link budgets ({{key:sc50:FSL}}, {{key:sc50:LNK}}, {{key:sc50:F₁}}), and receiver noise and channel capacity ({{key:sc50:Pₙ}}, {{key:sc50:NF}}, {{key:sc50:C/B}}, {{key:sc50:RCS}}, {{key:sc50:Δf}}, {{key:sc50:IP3}}, {{key:sc50:FDR}}).

### Decibel Power Ratios and Resonant LC Tank Circuits

Logarithmic gain $G_{\text{dB}}$ relates power ratio $P_2 / P_1$ and equal-impedance voltage ratio $V_2 / V_1$, while absolute power $P_{\text{dBm}}$ ({{key:sc50:dBm}}, {{key:sc50:▸dBm}}, with inverse {{key:sc50:dBm}} and watt-referenced {{key:sc50:▸dBW}}) references linear power to $1\text{ mW}$ ($0.001\text{ W}$), and the resonant tank solver ({{key:sc50:f₀}} {{key:sc50:f₀}} Equation Workspace `F = 1 / (2π√(L×C))` binding {{keycap:F}}, {{keycap:L}}, {{keycap:C}} on {{keycap:LFU0}}–{{keycap:LFU2}}) relates resonant frequency $F$, inductance $L$, and capacitance $C$:

$$G_{\text{dB}} = 10 \log_{10}\!\left(\frac{P_2}{P_1}\right) = 20 \log_{10}\!\left(\frac{V_2}{V_1}\right), \qquad P_{\text{dBm}} = 10 \log_{10}\!\left(\frac{P_{\text{mW}}}{1\text{ mW}}\right) = P_{\text{dBW}} + 30, \qquad F = \frac{1}{2\pi\sqrt{L C}}$$

### Reflection Coefficient, Standing Wave Ratio, and Quarter-Wave Matching

For a transmission line of characteristic impedance $Z_0$ ({{key:sc50:Z₀}}, defaulting to $50\,\Omega$) terminated in load impedance $Z_L$, the reflection coefficient $G = \lvert\Gamma\rvert$ ({{key:sc50:Γ}}) governs Voltage Standing Wave Ratio $S = \text{VSWR}$ ({{key:sc50:SWR}} Equation Workspace `S = (1 + G) / (1 - G)` binding {{keycap:S}}, {{keycap:G}} on {{keycap:LFU0}}–{{keycap:LFU1}}), quarter-wave transformer impedance $Z = \sqrt{S \cdot L}$ ({{key:sc50:TLN}} {{key:sc50:Z₀}} workspace on {{keycap:Z}}, {{keycap:S}}, {{keycap:L}}), Return Loss $\text{RL}_{\text{dB}}$, and Mismatch Loss $\text{ML}_{\text{dB}}$:

$$\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}, \qquad S = \frac{1 + \lvert\Gamma\rvert}{1 - \lvert\Gamma\rvert}, \qquad \text{RL}_{\text{dB}} = -20 \log_{10}\lvert\Gamma\rvert, \qquad \text{ML}_{\text{dB}} = -10 \log_{10}\!\left(1 - \lvert\Gamma\rvert^2\right)$$

### Friis Free-Space Path Loss, Thermal Noise Floor, Shannon Capacity, and Doppler Shift

Across a line-of-sight propagation link of distance $D$ at carrier frequency $F$ (with speed of light {{key:sc50:c}} $c = 2.99792458 \times 10^8\text{ m/s}$), {{key:sc50:FSL}} (Equation Workspace `L = 20LOG(D×F) + 32.4` binding {{keycap:L}}, {{keycap:D}}, {{keycap:F}} on {{keycap:LFU0}}–{{keycap:LFU2}}) and {{key:sc50:LNK}} (`R = P + G - L` binding {{keycap:R}}, {{keycap:P}}, {{keycap:G}}, {{keycap:L}} on {{keycap:LFU0}}–{{keycap:LFU3}}) compute Free-Space Path Loss $L$ and received power $R$; {{key:sc50:Pₙ}} and {{key:sc50:NF}} (`F = A + (B - 1) / G` on {{keycap:F}}, {{keycap:A}}, {{keycap:B}}, {{keycap:G}}) evaluate the thermal noise floor $P_n$ at {{key:sc50:T₀}} $T_0 = 290\text{ K}$ ($k_B T_0 = -174\text{ dBm/Hz}$ via Boltzmann constant {{key:sc50:kB}}) and Friis cascaded noise factor. And {{key:sc50:C/B}} (`C = B × LOG2(1 + S)` on {{keycap:LFU0}}–{{keycap:LFU2}}: {{keycap:C}}, {{keycap:B}}, {{keycap:S}}) and {{key:sc50:Δf}} solve Shannon–Hartley channel capacity and monostatic radar Doppler shift:

$$L_{\text{FSPL,dB}} = 20 \log_{10}(D_{\text{km}}) + 20 \log_{10}(F_{\text{MHz}}) + 32.44, \qquad P_{n,\text{dBm}} = -174\text{ dBm/Hz} + 10 \log_{10}(B_{\text{Hz}}) + \text{NF}_{\text{dB}}$$

$$C = B \log_2(1 + S), \qquad \Delta f_{\text{radar}} = \frac{2 \, v_r \, f_0}{c}, \qquad r_{F_1} = 17.32\sqrt{\frac{d_{\text{km}}}{4 \, f_{\text{GHz}}}}$$

---

## Wet-Lab Chemistry, Stoichiometry, and Spectroscopy

Covered in [Unit VI, Chapters 16–18](06-sc60-chemistry-wetlab.md), the **SC-60** analytical chemistry and biochemistry instrument connects gravimetric stoichiometry ({{key:sc60:MW}}, {{key:sc60:Z}}, {{key:sc60:RXN}}, {{key:sc60:w/w}}), serial dilutions and titrations ({{key:sc60:C₁V₁}}, {{key:sc60:EQV}}), Beer–Lambert spectrophotometry ({{key:sc60:εbc}}, {{key:sc60:%T}}), acid-base buffer equilibria ({{key:sc60:pH}}, {{key:sc60:pKₐ}}, {{key:sc60:BUF}}), and chemical thermodynamics and kinetics ({{key:sc60:PVT}}, {{key:sc60:ΔG}}, {{key:sc60:E°}}, {{key:sc60:CAL}}, {{key:sc60:Eₐ}}, {{key:sc60:RCF}}).

### Molarity, Dilutions, and Beer–Lambert Spectrophotometry

Solution molarity $C$ ({{key:sc60:RXN}} Equation Workspace `N = C × V` on {{keycap:N}}, {{keycap:C}}, {{keycap:V}} and {{key:sc60:MW}} `W = N × M` on {{keycap:W}}, {{keycap:N}}, {{keycap:M}}) relates solute mass $W$, molar mass $M$ ({{key:sc60:MW}} / {{key:sc60:Z}}), moles $N$, and solution volume $V$. Stock dilution ({{key:sc60:C₁V₁}} `C × V = D × U` on {{keycap:C}}, {{keycap:V}}, {{keycap:D}}, {{keycap:U}}) conserves solute moles across concentrations $C, D$ and volumes $V, U$. And optical absorbance $A$ ({{key:sc60:εbc}} {{key:sc60:εbc}} Equation Workspace `A = E × B × C` binding {{keycap:A}}, {{keycap:E}}, {{keycap:B}}, {{keycap:C}} on {{keycap:LFU0}}–{{keycap:LFU3}}, alongside {{key:sc60:%T}}) links transmitted intensity $I / I_0$ to molar absorptivity $E = \varepsilon$, path length $B = b$, and concentration $C = c$:

$$N = \frac{W}{M} = C \cdot V, \qquad C \cdot V = D \cdot U, \qquad A = -\log_{10}\!\left(\frac{I}{I_0}\right) = E \cdot B \cdot C$$

### Acid-Base Buffers, Thermodynamics, and Arrhenius Activation Kinetics

Aqueous acidity ({{key:sc60:pH}}) and weak-acid buffer equilibria ({{key:sc60:BUF}}, with Equation Workspace `P = K + LOG(A/H)` binding {{keycap:P}}, {{keycap:K}}, {{keycap:A}}, {{keycap:H}} on {{keycap:LFU0}}–{{keycap:LFU3}}) follow Sørensen's logarithmic scale and the Henderson–Hasselbalch equation for conjugate pair $[\text{A}^-] / [\text{HA}]$ around $\text{p}K_a$, while {{key:sc60:PVT}} (`P × V = N × R × T`), {{key:sc60:ΔG}} (`G = H - T × S`), {{key:sc60:E°}} (`E = S - (.0592/N)LOG(Q)`), {{key:sc60:CAL}} (`Q = M × C × T`), and {{key:sc60:Eₐ}} relate thermodynamic state functions via universal gas constant {{key:sc60:R}} $R = 8.3144626\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$, Faraday's constant {{key:sc60:F}} $F = 96{,}485.33\text{ C/mol}$, and Avogadro's constant {{key:sc60:Nₐ}} $N_A = 6.02214076 \times 10^{23}\text{ mol}^{-1}$:

$$\text{pH} = -\log_{10}[\text{H}^+], \qquad P = K + \log_{10}\!\left(\frac{A}{H}\right), \qquad \ln\!\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$$

---

## Commercial Bakery, Fermentation Science, and Brewing

Covered in [Unit VII, Chapters 19–21](07-sc78-culinary-brewing.md), the **SC-78** culinary and fermentation instrument standardizes flour-referenced baker's percentages ({{key:sc78:BK%}}, {{key:sc78:HYD}}, {{key:sc78:LV%}}, {{key:sc78:ΣW}}, {{key:sc78:SCL}}, {{key:sc78:DIV}}), dough thermal balance ({{key:sc78:Tw}}, {{key:sc78:ICE}}), mash strike temperatures ({{key:sc78:MSH}}), wort attenuation ({{key:sc78:ABV}}, {{key:sc78:▸SG}}, {{key:sc78:▸Brx}}, {{key:sc78:▸°P}}, {{key:sc78:SGT}}), hop bitterness ({{key:sc78:IBU}}, {{key:sc78:SRM}}, {{key:sc78:CO₂}}), and butcher yield costing ({{key:sc78:YLD}}, {{key:sc78:CST}}, {{key:sc78:PRC}}, {{key:sc78:Aw}}, {{key:sc78:SO₂}}).

### Baker's Percentage, Dough Thermodynamics, and Culinary Yield Costing

Baker's percentage ({{key:sc78:BK%}} Equation Workspace `P = I / F × 100` on {{keycap:P}}, {{keycap:I}}, {{keycap:F}}, paired with {{key:sc78:ΣW}}, {{key:sc78:SCL}}, and {{key:sc78:DIV}}) expresses each ingredient weight $I$ as a percentage $P$ of total flour mass $F$. The five-variable Desired Dough Temperature balance ({{key:sc78:Tw}} {{key:sc78:Tw}} Workspace `W = 3×D - R - F - M` on {{keycap:W}}, {{keycap:D}}, {{keycap:R}}, {{keycap:F}}, {{keycap:M}}) and flake-ice substitution ({{key:sc78:ICE}}) govern mixer calorimetry. And butcher trim yield $Y_{\%}$ ({{key:sc78:YLD}}) and food cost ({{key:sc78:CST}} `P = C / (F / 100)` on {{keycap:P}}, {{keycap:C}}, {{keycap:F}}, paired with {{key:sc78:PRC}}) govern menu pricing:

$$P = \frac{I}{F} \times 100\%, \qquad W = 3 D - R - F - M, \qquad W_{\text{ice}} = \frac{W_{\text{water}}\left(T_{\text{tap}} - W\right)}{80}$$

$$Y_{\%} = \frac{W_{\text{EP}}}{W_{\text{AP}}} \times 100\%, \qquad C_{\text{EP}} = \frac{C_{\text{AP}}}{Y_{\%}/100}, \qquad P = \frac{C}{F / 100}$$

### Brewing Gravity, Strike Water, and Hop Bitterness

During wort mashing and fermentation, {{key:sc78:ABV}} (`A = (O - F) × 131.25` on {{keycap:A}}, {{keycap:O}}, {{keycap:F}}) evaluates Alcohol by Volume ($A$) from Original Gravity ($O$) and Final Gravity ($F$), {{key:sc78:MSH}} (`S = .2/R×(T-G)+T` on {{keycap:S}}, {{keycap:R}}, {{keycap:T}}, {{keycap:G}}) solves mash strike water temperature $S$ from water-to-grist ratio $R$, dry grain temperature $G$, and target rest temperature $T$, and {{key:sc78:IBU}} (`I = W×A×U×74.89/V` on {{keycap:I}}, {{keycap:W}}, {{keycap:A}}, {{keycap:U}}, {{keycap:V}}) evaluates Glenn Tinseth's International Bitterness Units from hop weight $W$, alpha-acid rating $A$, decimal utilization $U$, and batch volume $V$:

$$A = (O - F) \times 131.25, \qquad S = \frac{0.2}{R}\left(T - G\right) + T, \qquad I = \frac{W \cdot A \cdot U \cdot 74.89}{V}$$

---

## Clinical Nursing, Hospital Pharmacy, and Infusions

Covered in [Unit VIII, Chapters 22–24](08-sc80-clinical-pharmacy.md), the **SC-80** clinical nursing and hospital pharmacy calculator implements persistent Patient Profile biometrics ({{keycap:PAT}}: {{keycap:W}}, {{keycap:H}}, {{keycap:A}}, {{keycap:S}}, {{keycap:MALE}}/{{keycap:FEM}}), anthropometric dosing-weight corrections ({{key:sc80:BSA}}, {{key:sc80:BMI}}, {{key:sc80:IBW}}, {{key:sc80:ABW}}), glomerular filtration estimation ({{key:sc80:GFR}}), first-order compartment kinetics ({{key:sc80:PK}}), intravenous pump titrations ({{key:sc80:DRP}}, {{key:sc80:IV}}, {{key:sc80:DOS}}, {{key:sc80:gtt}}, {{key:sc80:BRN}}, {{key:sc80:ICU}}), and acid-base electrolyte homeostasis ({{key:sc80:AG}}, {{key:sc80:Ca²⁺}}, {{key:sc80:Na⁺}}, {{key:sc80:OSM}}, {{key:sc80:ABG}}, {{key:sc80:QTc}}, {{key:sc80:O₂}}).

### Body Surface Area and Dosing Weight Corrections

For a patient of height $H$ (in $\text{cm}$, where $H_{\text{in}} = H / 2.54$) and total body weight $W$ (in $\text{kg}$), {{key:sc80:BSA}} (`B = √(H × W / 3600)` on {{keycap:B}}, {{keycap:H}}, {{keycap:W}}, {{keycap:PAT}}) evaluates Robert Mosteller's surface area ($\text{m}^2$), {{key:sc80:IBW}} evaluates Ben Devine's lean Ideal Body Weight ($\text{IBW}_{\text{male}} = 50 + 2.3(H_{\text{in}} - 60)$ and $\text{IBW}_{\text{female}} = 45.5 + 2.3(H_{\text{in}} - 60)$), and {{key:sc80:ABW}} blends $40\%$ of excess adipose mass into Adjusted Body Weight $\text{ABW}$:

$$B = \sqrt{\frac{H \times W}{3600}}, \qquad \text{ABW} = \text{IBW} + 0.40\left(W - \text{IBW}\right)$$

### Renal Clearance, Intravenous Infusions, Compartment Kinetics, and Anion Gap

Given chronological age $A$, dosing weight $W$, and steady-state serum creatinine $S$, {{key:sc80:GFR}} (`C = (140-A)W/(72×S)` on {{keycap:C}}, {{keycap:A}}, {{keycap:W}}, {{keycap:S}}, {{keycap:PAT}}) evaluates Donald Cockcroft and Henry Gault's glomerular filtration estimate ($\text{mL/min}$); {{key:sc80:DRP}} (`R = D × W × 60 / C` on {{keycap:R}}, {{keycap:D}}, {{keycap:W}}, {{keycap:C}}, {{keycap:PAT}}), {{key:sc80:IV}} (`R = V / T` on {{keycap:R}}, {{keycap:V}}, {{keycap:T}}), {{key:sc80:DOS}} (`T = W × D` on {{keycap:T}}, {{keycap:W}}, {{keycap:D}}, {{keycap:PAT}}), and {{key:sc80:gtt}} convert weight-based vasoactive orders ($D$) and bag concentrations ($C$) into volumetric pump rates ($R$) and gravity drop rates ($\text{gtt/min}$). And {{key:sc80:PK}} (`T = .69315 × V / C` on {{keycap:T}}, {{keycap:V}}, {{keycap:C}}), {{key:sc80:AG}}, and {{key:sc80:Ca²⁺}} govern one-compartment elimination and serum electroneutrality:

$$C = \frac{(140 - A) \times W}{72 \times S} \times (0.85\text{ if female})$$

$$R = \frac{D \times W \times 60}{C}, \qquad R_{\text{gtt/min}} = \frac{R_{\text{mL/hr}} \times DF_{\text{gtt/mL}}}{60}$$

$$T_{1/2} = \frac{\ln(2) \cdot V}{C_{\text{CL}}} = \frac{\ln(2)}{K}, \qquad \text{AG} = [\text{Na}^+] - \left([\text{Cl}^-] + [\text{HCO}_3^-]\right), \qquad \text{Ca}_{\text{corr}} = \text{Ca}_{\text{meas}} + 0.8\left(4.0 - \text{Alb}\right)$$

---

## Quantitative Finance, Actuarial Science, and Six Sigma

Covered in [Unit IX, Chapters 25–27](09-sc95-finance-statistics.md), the **SC-95** quantitative finance and statistical inference instrument unites multi-period cash-flow discounting ({{key:sc95:TVM}}, {{key:sc95:AMR}}, {{key:sc95:CF}}, {{key:sc95:CGR}}, {{key:sc95:ROI}}), fixed-income bond pricing and yield ({{key:sc95:BND}}), unit economics ({{key:sc95:MGN}}, {{key:sc95:MKP}}, {{key:sc95:BEP}}, {{key:sc95:EOQ}}, {{key:sc95:DEP}}, {{key:sc95:EAR}}, {{key:sc95:TAX}}), direct faceplate R-style probability distributions ({{key:sc95:pN}}, {{key:sc95:qN}}, {{key:sc95:rN}}, {{key:sc95:pt}}, {{key:sc95:qt}}, {{key:sc95:rt}}, {{key:sc95:pχ²}}, {{key:sc95:qχ²}}, {{key:sc95:rχ²}}, {{key:sc95:pF}}, {{key:sc95:qF}}, {{key:sc95:rF}}, {{key:sc95:pB}}, {{key:sc95:qB}}, {{key:sc95:rB}}, {{key:sc95:PDF}}), and Six Sigma process capability ({{key:sc95:Cpk}}, {{key:sc95:SPC}}, {{key:sc95:z₀}}, {{key:sc95:t₂}}, {{key:sc95:A/B}}, {{key:sc95:CI}}, {{key:sc95:n*}}).

### Compound Time Value of Money, Bond Valuation, and Net Present Value

Across $N$ compounding periods at periodic interest rate $i = \text{I\%}/100$ with payment timing indicator $\text{mode} \in \{0, 1\}$ ({{keycap:END}} $= 0$, {{keycap:BEG}} $= 1$), the five softkeys ({{keycap:N}}, {{keycap:I%}}, {{keycap:PV}}, {{keycap:PMT}}, {{keycap:FV}} under {{key:sc95:TVM}}) enforce cash-flow conservation between Present Value $\text{PV}$, periodic payment $\text{PMT}$, and Future Value $\text{FV}$. In the {{key:sc95:CF}} ({{key:sc95:CF}}) Equation Workspace (`V = C×(1-(1+R/100)⁻ᴺ)/(R/100) - I` binding {{keycap:V}}, {{keycap:C}}, {{keycap:R}}, {{keycap:N}}, {{keycap:I}} on {{keycap:LFU0}}–{{keycap:LFU4}}) and the {{key:sc95:BND}} Equation Workspace (`P = C×(1-(1+Y/100)⁻ᴺ)/(Y/100) + F×(1+Y/100)⁻ᴺ` binding {{keycap:P}}, {{keycap:C}}, {{keycap:Y}}, {{keycap:N}}, {{keycap:F}} on {{keycap:LFU0}}–{{keycap:LFU4}}), Secant–Brent numerical root-finding solves forward for price/value or backward for internal yield:

$$\text{PV}(1 + i)^N + \text{PMT} \cdot \frac{(1 + i)^N - 1}{i} \cdot (1 + i \cdot \text{mode}) + \text{FV} = 0, \qquad V = C \cdot \frac{1 - (1 + r)^{-N}}{r} - I$$

$$P = C \cdot \frac{1 - (1 + y)^{-N}}{y} + \frac{F}{(1 + y)^N}, \qquad D_{\text{Mac}} = \frac{1}{P} \sum_{t=1}^{N} \frac{t \cdot CF_t}{(1 + y)^t}, \qquad D_{\text{Mod}} = \frac{D_{\text{Mac}}}{1 + y}$$

### Six Sigma Process Capability, Sample Size Planning, and Black–Scholes Option Valuation

For a manufacturing process with mean $\mu$ and standard deviation $S = \hat{\sigma}$ operating between specification limits $L = \text{LSL}$ and $U = \text{USL}$, {{key:sc95:Cpk}} (`C = (U - L) / (6×S)` on {{keycap:C}}, {{keycap:U}}, {{keycap:L}}, {{keycap:S}}) evaluates potential capability $C_p$ and centered capability $C_{pk}$, while the sample-size solver ({{key:sc95:n*}} {{key:sc95:n*}} Equation Workspace `N = (Z × S / E)²` binding {{keycap:N}}, {{keycap:Z}}, {{keycap:S}}, {{keycap:E}} on {{keycap:LFU0}}–{{keycap:LFU3}}) relates sample size $N$, critical quantile $Z = z_{\alpha/2}$ ({{key:sc95:qN}} / {{key:sc95:qt}}), dispersion $S$, and margin of error $E$ ({{key:sc95:CI}}). In continuous-time finance, the Black–Scholes–Merton equations price European call and put options from spot price $S_0$, strike $K$, risk-free rate $r$, volatility $\sigma$, expiration $T$, and the standard normal cumulative integral $\Phi(z)$ ({{key:sc95:pN}}):

$$C_p = \frac{U - L}{6S}, \qquad C_{pk} = \min\!\left(\frac{U - \mu}{3S},\; \frac{\mu - L}{3S}\right), \qquad N = \left(\frac{Z \cdot S}{E}\right)^2$$

$$C_{\text{call}} = S_0 \Phi(d_1) - K e^{-rT} \Phi(d_2), \qquad P_{\text{put}} = K e^{-rT}\Phi(-d_2) - S_0\Phi(-d_1), \qquad d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}$$
