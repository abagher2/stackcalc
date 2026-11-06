---
title: "Appendix B: Master Row 0 Softkey & Shifted Keycap Directory"
description: "Complete hardware keycap, Row 0 domain softkey, and register input/output directory for all nine instruments in the StackCalc Domain Series (SC-35 through SC-95)."
---

# Appendix B: Master Row 0 Softkey & Shifted Keycap Directory

> **Who this is for:** Operators, educators, and engineers who want a complete hardware keycap and Row 0 domain softkey directory across all nine StackCalc Domain Series instruments, showing exact pre-execution stack arguments ($Z, Y, X$) and post-execution outputs ($Y', X'$).

---

## 1. Shared Core Keys Across All Nine Instruments

Every calculator in the StackCalc Domain Series shares the same physical core keypad layout for stack manipulation, register storage, and arithmetic:

| Keycap / Sequence | Function Name | Pre-Execution Stack ($Y, X$) | Post-Execution Stack ($Y', X'$) |
| :--- | :--- | :--- | :--- |
| `[ENTER]` | Stack Lift & Duplicate | `Y, X` | `X, X` (prior $Y \to Z$, $Z \to T$) |
| `[x⇄y]` | Swap Registers $X$ and $Y$ | `Y, X` | `X, Y` ($Z$ and $T$ unchanged) |
| `[R↓]` | Roll Stack Downward | `T, Z, Y, X` | `X, T, Z, Y` |
| `[←]` / `[C]` | Backspace / Clear $X$ | `Y, X` | `Y, 0.0000` (disables stack lift) |
| `[+/-]` | Change Sign / Negate | `Y, X` | `Y, -X` |
| `[STO] [0]–[9]` | Store $X$ in Register $R_n$ | `Y, X` | `Y, X` ($R_n \leftarrow X$) |
| `[RCL] [0]–[9]` | Recall Register $R_n$ to $X$ | `Y, X` | `X, Rₙ` (lifts stack first) |
| `[f]` | Yellow Primary Shift | — | Arms yellow shifted legend for next key |
| `[g]` | Blue Secondary Shift | — | Arms blue shifted legend for next key |
| `[SHOW]` | Full-Precision Mantissa Peek | `Y, X` | Temporarily reveals all 15 significant digits of $X$ |

---

## 2. SC-35 Geomatics, Land Surveying & Flight Navigation

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| `[FWD]` | Row 0 Softkey (Col 0) | **Forward Traverse:** Consumes distance $D$ ($Y$) and azimuth $\alpha$ ($X$); returns $\Delta E$ in $Y'$ and $\Delta N$ in $X'$. |
| `[INV]` | Row 0 Softkey (Col 1) | **Coordinate Inverse:** Consumes $\Delta N$ ($Y$) and $\Delta E$ ($X$); returns azimuth $\alpha \in [0^\circ, 360^\circ)$ in $Y'$ and horizontal distance $D$ in $X'$. |
| `[BRG]` | Row 0 Softkey (Col 2) | **Quadrant Bearing:** Formats azimuth in $X$ as surveyor quadrant bearing (`NE`, `SE`, `SW`, `NW`) and degree-minute-second components. |
| `[WND]` | Row 0 Softkey (Col 3) | **E6B Wind Triangle:** Decomposes wind speed/angle into headwind ($Y'$) and crosswind ($X'$) components, or solves Wind Correction Angle (`WCA`). |
| `[ISA]` | Row 0 Softkey (Col 4) | **ISA & Density Altitude:** Computes Pressure Altitude (`PA`) and Density Altitude (`DA`) from elevation, altimeter setting, and OAT. |
| `[trav]` | Row 0 Softkey (Col 5) | **Bowditch Traverse Accumulator:** Accumulates station leg $(\Delta N_i, \Delta E_i, D_i)$ and computes closure error and precision ratio. |
| `[f] [→HR]` | Yellow Shift | Converts packed sexagesimal `D.MMSS` in $X$ to decimal degrees/hours. |
| `[g] [→HMS]` | Blue Shift | Converts decimal degrees/hours in $X$ to packed sexagesimal `D.MMSS`. |
| `[g] [POL]` | Blue Shift | Rectangular $(Y, X)$ to Polar: magnitude $r \to X'$, angle $\theta \to Y'$. |
| `[f] [REC]` | Yellow Shift | Polar $(Y, X)$ to Rectangular: $x = r\cos\theta \to X'$, $y = r\sin\theta \to Y'$. |

---

## 3. SC-14 Industrial Trades, Electrical & Mechanical

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| `[RUN]` | Row 0 Softkey (Col 0) | Stores or solves horizontal framing run $R$ in feet-inches-fractions (`FT-IN`). |
| `[RISE]` | Row 0 Softkey (Col 1) | Stores or solves vertical rise from unit pitch ($U/12$) and run $R$. |
| `[DIAG]` | Row 0 Softkey (Col 2) | Computes common rafter diagonal $\sqrt{\text{Run}^2 + \text{Rise}^2}$ in `FT-IN` (`[g] [HIP]` for hip/valley). |
| `[BEND]` | Row 0 Softkey (Col 3) | **Conduit Offset Solver:** Consumes offset $O$ ($Y$) and bend angle $\theta$ ($X$); returns travel length $L_{\text{travel}}$ in $X'$ and shrink $S$ in $Y'$. |
| `[VD]` | Row 0 Softkey (Col 4) | **NEC Voltage Drop:** Computes conductor voltage drop $V_{\text{drop}}$ and terminal voltage from current $I$, one-way distance $L$, and AWG wire gauge. |
| `[TBL]` | Row 0 Softkey (Col 5) | **Trade Lookup Table:** Recalls NEC Chapter 9 circular mils / ampacity and ANSI drill-tap allowances. |
| `[f] [3PH÷]` | Yellow Shift | Divides apparent three-phase power $S$ ($Y$) by $\sqrt{3} \cdot V_{LL}$ ($X$) to return line current $I_L$ in $X'$. |
| `[f] [→mm]` | Yellow Shift | Converts decimal or fractional inches in $X$ to exact millimeters ($\times 25.4$). |
| `[g] [→in]` | Blue Shift | Converts millimeters in $X$ to decimal and nearest $1/16\text{ in}$ fractional inches. |

---

## 4. SC-16 Systems Programming, Embedded & Cyber Operations

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| `[HEX]` | Row 0 Softkey (Col 0) | Switches display and keypad entry to base-16 hexadecimal (`0`–`9`, `A`–`F`). |
| `[DEC]` | Row 0 Softkey (Col 1) | Switches display to signed/unsigned base-10 decimal integer or float mode. |
| `[BIN]` | Row 0 Softkey (Col 2) | Switches display to base-2 binary bit-grouped view (`[g] [OCT]` for base-8 octal). |
| `[WSZ]` | Row 0 Softkey (Col 3) | Cycles hardware word width across `8-bit`, `16-bit`, `32-bit`, and `64-bit` registers. |
| `[ENDN]` | Row 0 Softkey (Col 4) | Swaps byte endianness (`BSWAP16`, `BSWAP32`, `BSWAP64`) of integer in $X$. |
| `[FLT]` | Row 0 Softkey (Col 5) | Reinterprets 32-bit hex word in $X$ as an IEEE 754 `float32` value (and vice versa). |
| `[f] [AND]` / `[OR]` / `[XOR]` | Yellow Shift | Bitwise logical `AND`, `OR`, or `XOR` between $Y$ and $X$ masked to active word width. |
| `[f] [NOT]` | Yellow Shift | Bitwise one's complement ($\sim X$) masked to active word width (`[+/-]` for two's complement). |
| `[g] [SL]` / `[SR]` / `[ASR]` | Blue Shift | Logical shift left (`<<`), logical shift right (`>>>`), and arithmetic shift right (`>>`). |
| `[g] [RL]` / `[RR]` | Blue Shift | Circular bit rotate left (`ROL`) and rotate right (`ROR`) by $X$ bit positions. |
| `[MOD]` | Primary Key | Computes $Y \bmod X$ (`[MOD]` followed by `[yˣ]` executes $Z^Y \bmod X$). |

---

## 5. SC-24 Cinema Optics, Broadcast Timecode & Sound

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| `[TC]` | Row 0 Softkey (Col 0) | Toggles `HH:MM:SS:FF` SMPTE timecode entry and arithmetic mode. |
| `[FPS]` | Row 0 Softkey (Col 1) | Cycles frame rate across `23.976`, `24.00`, `25.00`, `29.97 DF`, `29.97 NDF`, `30.00`, and `60.00` fps. |
| `[DOF]` | Row 0 Softkey (Col 2) | **Depth of Field Solver:** Consumes focal length $f$ ($Z$), $T$-stop ($Y$), and focus distance $d$ ($X$); returns hyperfocal $H$, near limit $D_{\text{near}}$, and far limit $D_{\text{far}}$. |
| `[EXP]` | Row 0 Softkey (Col 3) | **Exposure & Shutter Solver:** Computes exposure time $t_{\text{exp}}$ or T-stop compensation across FPS, shutter angle, and ND filters. |
| `[AUD]` | Row 0 Softkey (Col 4) | **Acoustic Delay & Wavelength:** Computes sound propagation delay ($\text{ms}$) and frame offset for distance $d$ at ambient temperature $T$. |
| `[dB⊕]` | Row 0 Softkey (Col 5) | **Incoherent Decibel Power Sum:** Computes $10\log_{10}(10^{Y/10} + 10^{X/10})$ for combining two audio/noise sources in dB. |

---

## 6. SC-50 RF Spectrum, Transmission Lines & Microwave

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| `[dBm]` | Row 0 Softkey (Col 0) | Converts power in Watts/milliwatts in $X$ to $\text{dBm}$ ($10\log_{10}(P / 1\text{ mW})$). |
| `[→W]` | Row 0 Softkey (Col 1) | Converts power level in $\text{dBm}$ in $X$ to linear power in Watts ($10^{(X-30)/10}$). |
| `[SWR]` | Row 0 Softkey (Col 2) | Converts load impedance $Z_L$ or reflection magnitude $|\Gamma|$ in $X$ to standing wave ratio $\text{VSWR}$. |
| `[FSPL]` | Row 0 Softkey (Col 3) | **Friis Path Loss:** Consumes link distance $d$ ($Y$) and frequency $f$ ($X$); returns free-space path loss $\text{FSPL}_{\text{dB}}$ in $X'$. |
| `[SMTH]` | Row 0 Softkey (Col 4) | **L-Network Impedance Matcher:** Consumes $Z_0$ ($Z$), $R_L$ ($Y$), and $X_L$ ($X$); returns series/shunt matching reactances and $L, C$ values. |
| `[NF]` | Row 0 Softkey (Col 5) | **Friis Cascade Noise Figure & Thermal Floor:** Computes cascaded noise figure or receiver noise floor $N_{\text{dBm}}$ for bandwidth $B$. |
| `[f] [RL]` / `[ML]` | Yellow Shift | Converts VSWR or $|\Gamma|$ in $X$ directly to Return Loss ($\text{RL}_{\text{dB}}$) or Mismatch Loss ($\text{ML}_{\text{dB}}$). |

---

## 7. SC-60 Wet-Lab Chemistry, Stoichiometry & Spectroscopy

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| `[MW]` | Row 0 Softkey (Col 0) | Computes or recalls molecular weight ($\text{g/mol}$) from atomic masses (`[C]`, `[H]`, `[N]`, `[O]`, `[Na]`, `[Cl]`, `[P]`, `[S]`). |
| `[MOL]` | Row 0 Softkey (Col 1) | Solves mass $m_{\text{g}} = M \times \text{MW} \times V_{\text{L}}$ or molarity $M$ from mass, molecular weight, and volume. |
| `[C₁V₁]` | Row 0 Softkey (Col 2) | **Dilution Solver:** Consumes stock $C_1$ ($Z$), target $C_2$ ($Y$), and target volume $V_2$ ($X$); returns stock aliquot $V_1$ in $X'$ and diluent volume $V_2 - V_1$ in $Y'$. |
| `[pH]` | Row 0 Softkey (Col 3) | Converts $[\text{H}^+]$ molarity in $X$ to $\text{pH} = -\log_{10}(X)$ (`[g] [10⁻ˣ]` for inverse). |
| `[BUFF]` | Row 0 Softkey (Col 4) | **Henderson-Hasselbalch Buffer:** Consumes $\text{p}K_a$ ($Z$), target $\text{pH}$ ($Y$), and total molarity $C_{\text{tot}}$ ($X$); returns $[\text{HA}]$ and $[\text{A}^-]$. |
| `[ABS]` | Row 0 Softkey (Col 5) | **Beer-Lambert Law:** Converts percent transmittance $\%T$ to absorbance $A = 2 - \log_{10}(\%T)$ or solves concentration $c = A / (\varepsilon \ell)$. |
| `[TITR]` | Shifted Solver | Computes equivalence-point volume $V_{\text{eq}}$ and titration curve pH from titrant and analyte volumes/molarities. |

---

## 8. SC-78 Commercial Bakery, Fermentation Science & Brewing

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| `[FLR]` | Row 0 Softkey (Col 0) | Sets total flour weight ($100\%$ Baker's Percentage reference base) from Register $X$. |
| `[BKR%]` | Row 0 Softkey (Col 1) | Converts ingredient percentage in $X$ to batch weight (or batch weight to Baker's $\%$). |
| `[DDT]` | Row 0 Softkey (Col 2) | **Desired Dough Temperature:** Consumes target $\text{DDT}$ ($T$), room temp ($Z$), flour temp ($Y$), and mixer friction ($X$); returns required water temperature $T_{\text{water}}$. |
| `[ABV]` | Row 0 Softkey (Col 3) | **Fermentation Gravity Solver:** Consumes Original Gravity $\text{OG}$ ($Y$) and Final Gravity $\text{FG}$ ($X$); returns $\text{ABV\%}$ in $X'$ and apparent attenuation in $Y'$. |
| `[STRK]` | Row 0 Softkey (Col 4) | **Mash Strike Water:** Consumes grist ratio $R$ ($Z$), grain temp ($Y$), and target mash rest temp ($X$); returns strike water temperature $T_{\text{strike}}$. |
| `[IBU]` | Row 0 Softkey (Col 5) | **Tinseth Hop Bitterness:** Computes International Bitterness Units ($\text{IBU}$) from hop mass, alpha-acid $\%$, boil time, wort gravity, and batch volume. |

---

## 9. SC-80 Clinical Nursing, Hospital Pharmacy & Infusions

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| `[BSA]` | Row 0 Softkey (Col 0) | **Mosteller BSA:** Consumes patient height in $\text{cm}$ ($Y$) and weight in $\text{kg}$ ($X$); returns Body Surface Area ($\text{m}^2$) in $X'$. |
| `[IBW]` | Row 0 Softkey (Col 1) | **Devine Ideal & Adjusted Body Weight:** Computes $\text{IBW}_{\text{kg}}$ and $\text{ABW}_{\text{kg}}$ from patient sex, height, and actual weight. |
| `[CrCl]` | Row 0 Softkey (Col 2) | **Cockcroft-Gault Renal Clearance:** Consumes age ($Z$), weight in $\text{kg}$ ($Y$), and serum creatinine $\text{SCr}$ ($X$); returns $\text{CrCl}$ ($\text{mL/min}$). |
| `[MCG]` | Row 0 Softkey (Col 3) | **Weight-Based IV Titration:** Converts ordered dose ($\text{mcg/kg/min}$), patient weight ($\text{kg}$), and bag concentration ($\text{mcg/mL}$) to pump rate ($\text{mL/hr}$). |
| `[GTT]` | Row 0 Softkey (Col 4) | **Gravity IV Drip Rate:** Consumes infusion rate in $\text{mL/hr}$ ($Y$) and tubing drop factor in $\text{gtt/mL}$ ($X$); returns rounded whole drops per minute ($\text{gtt/min}$). |
| `[PED]` | Row 0 Softkey (Col 5) | **Pediatric Safe-Dose Guardrail:** Verifies ordered dose against $\text{mg/kg/day}$ safe range and computes liquid suspension volume ($\text{mL/dose}$). |

---

## 10. Quantitative Finance, Actuarial Science & Six Sigma (SC-95)

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| `[N]` / `[I/Y]` / `[PV]` / `[PMT]` / `[FV]` | Row 0 Softkeys (Cols 0–4) | **Five-Key TVM Solver:** If preceded by numeric entry, stores $X$ into that TVM variable; if pressed after another TVM key, solves for that variable using signed cash-flow convention. |
| `[CPK]` | Row 0 Softkey (Col 5) | **Six Sigma Process Capability:** Consumes $\text{LSL}$ ($T$), $\text{USL}$ ($Z$), sample mean $\mu$ ($Y$), and standard deviation $\hat{\sigma}$ ($X$); returns $C_{pk}$ in $X'$ and $C_p$ in $Y'$. |
| `[f] [I%YR]` | Yellow Shift | Divides annual nominal rate in $Y$ by compounding periods per year in $X$ and stores periodic rate in `[I/Y]`. |
| `[f] [AMRT]` | Yellow Shift | Computes principal paid ($\Delta\text{Prin}$), interest paid ($\Delta\text{Int}$), and remaining balance over payment range $[p_1, p_2]$. |
| `[f] [NPV]` / `[IRR]` | Yellow Shift | Computes Net Present Value or Internal Rate of Return across cash-flow series $CF_0, CF_1, \dots, CF_T$. |
| `[g] [NormCDF]` / `[InvNorm]` | Blue Shift | Standard normal cumulative probability $\Phi(z)$ and inverse quantile $\Phi^{-1}(p)$. |
