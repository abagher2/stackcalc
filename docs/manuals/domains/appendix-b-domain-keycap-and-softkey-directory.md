---
title: "Appendix B: Domain Instrument Keycap & Workspace Directory"
description: "Hardware keycap, Row 0 domain softkey, and register input/output directory for all nine instruments in the StackCalc Domain Series (SC-35 through SC-95)."
---

# Appendix B: Domain Instrument Keycap & Workspace Directory

This directory catalogs the physical keycaps, Row 0 domain softkeys, yellow ({{key:f}}) and blue ({{key:g}}) shift layers, bidirectional Equation Solver Workspaces ({{key:sc35:SOLVE}} / {{key:XEQ}}), and register input-output signatures across all nine instruments in the StackCalc Domain Series (`SC-35` through `SC-95`). Each table lists the pre-execution stack arguments consumed from `Register T`, `Register Z`, `Register Y`, and `Register X` alongside the post-execution results returned to `Register X'` and `Register Y'` and the softkey variable bindings inside each instrument's Equation Solver Workspace.

## Shared Core Keys and Architecture Across All Nine Instruments

Every calculator in the StackCalc Domain Series provides configurable RPN stack depth ({{keycap:4-LV}}, {{keycap:8-LV}}, or {{keycap:INF}} cycled on Flag 5 `5:DEP` inside {{key:FLAGS}}), dual-mode domain keys that combine one-key RPN stack evaluation with a bidirectional Equation Solver Workspace ({{key:sc35:SOLVE}} / {{key:XEQ}}), and non-destructive Live Reference Ledgers ({{key:▦}}) paired with ten general-purpose memory registers (`R₀`–`R₉`):

| Keycap / Sequence | Function Name | Pre-Execution Stack ($Y, X$) | Post-Execution Stack ($Y', X'$) & Architecture Role |
| :--- | :--- | :--- | :--- |
| {{key:ENTER}} | Stack Lift & Duplicate | `Y, X` | `X, X` (prior $Y \to Z$, $Z \to T$; lifts across {{keycap:4-LV}}, {{keycap:8-LV}}, or {{keycap:INF}} via Flag 5 `5:DEP` in {{key:FLAGS}}) |
| {{key:x⇄y}} | Swap Registers $X$ and $Y$ | `Y, X` | `X, Y` ($Z$ and $T$ unchanged) |
| {{key:R↓}} / {{key:R↑}} | Roll Stack Down / Up | `T, Z, Y, X` | `X, T, Z, Y` or `Z, Y, X, T` (cycles active stack window) |
| {{key:<-}} / {{key:C}} | Backspace / Clear $X$ | `Y, X` | `Y, 0.0000` (disables stack lift) |
| {{key:+/-}} | Change Sign / Negate | `Y, X` | `Y, -X` (or two's complement negation {{key:sc16:NEG}} on `SC-16`) |
| {{key:STO}} {{key:0}}–{{key:9}} | Store $X$ in Register $R_n$ | `Y, X` | `Y, X` ($R_n \leftarrow X$) |
| {{key:RCL}} {{key:0}}–{{key:9}} | Recall Register $R_n$ to $X$ | `Y, X` | `X, Rₙ` (lifts stack first) |
| {{key:sc35:SOLVE}} / {{key:XEQ}} | Bidirectional Solver Arm | `Y, X` | Arms Equation Workspace to solve forward or backward for the next softkey pressed |
| Row 0 Softkeys (Cols 0–5) | Contextual Softkeys | `Y, X` | Populates with domain shortcuts when idle, or stores/solves symbolic variables in an active Equation Workspace |
| {{key:0}} `<SOFTKEY>` | Zero-Value Parameter Binding | `0, X` | Explicitly binds $0.0000$ to the variable (indicated by `*` or `•`), enabling exact zero boundary conditions |
| {{key:f}} `<SOFTKEY>` ({{key:↰}}) | Shift-Softkey Variable Unsetting | — | Unbinds and clears the variable from the bound set (displaying `UNSET <VAR>`), freeing it to be solved for |
| {{key:▦}} | Live Reference Ledger | `Y, X` | Opens non-destructive domain reference lookup and ledger (`@COGO`, `@BOM`, `@BK%`, `@PAT`, cash-flow / stats table) |
| {{key:f}} | Yellow Primary Shift | — | Arms yellow shifted legend for next key |
| {{key:g}} | Blue Secondary Shift | — | Arms blue shifted legend for next key |
| {{key:SHOW}} | Full-Precision Mantissa Peek | `Y, X` | Temporarily reveals all 15–17 significant IEEE 754 digits of $X$ |
| {{key:f}} {{key:C}} ({{key:?}}) | Interactive Guided Tutorial Runner | — | Launches on-device step-by-step tutorial runner with 3 guided domain lessons |

### Master Directory of Bidirectional Equation Solver Workspaces

Opening a multi-parameter domain workspace (by pressing the key with $X = 0, Y = 0$ or after {{key:sc35:SOLVE}}) renders its governing law on Line 1 of the display and binds the Row 0 softkeys to its symbolic variables so any parameter can be solved forward or backward via {{key:XEQ}} `<SOFTKEY>` (or {{key:sc35:SOLVE}} `<SOFTKEY>`):

| Instrument | Workspace Key | Governing Equation on Line 1 | Bound Softkeys |
| :--- | :--- | :--- | :--- |
| **SC-35** | {{key:sc35:CRV}} | `L = R × D × π / 180` | {{keycap:L}} arc length • {{keycap:R}} radius • {{keycap:D}} central angle $\Delta$ |
| **SC-35** | {{key:sc35:VCV}} | `E = P + (3×G + H) × L / 8` | {{keycap:E}} midpoint elevation • {{keycap:P}} PVC elevation • {{keycap:G}} entry grade $g_1\%$ • {{keycap:H}} exit grade $g_2\%$ • {{keycap:L}} length stations |
| **SC-35** | {{key:sc35:LVL}} | `E = H + B - F` | {{keycap:E}} elevation • {{keycap:H}} benchmark / HI • {{keycap:B}} backsight • {{keycap:F}} foresight |
| **SC-35** | {{key:sc35:WND}} | `X = V × SIN(A)` | {{keycap:X}} crosswind • {{keycap:V}} wind speed • {{keycap:A}} wind angle $\gamma$ |
| **SC-35** | {{key:sc35:ALT}} | `D = P + 120 × (T - 15)` | {{keycap:D}} density altitude • {{keycap:P}} pressure altitude • {{keycap:T}} OAT ($^\circ\text{C}$) |
| **SC-35** | {{key:sc35:TSD}} | `D = S × T` | {{keycap:D}} distance • {{keycap:S}} speed • {{keycap:T}} time |
| **SC-35** | {{key:sc35:FLW}} | `Q = A × V` | {{keycap:Q}} flow • {{keycap:A}} area • {{keycap:V}} velocity |
| **SC-35** | {{key:sc35:△}} | `A = 0.5 × B × H` | {{keycap:A}} area • {{keycap:B}} base • {{keycap:H}} height |
| **SC-35** | {{key:sc35:CG}} | `M = W × A` | {{keycap:M}} moment • {{keycap:W}} weight • {{keycap:A}} arm station |
| **SC-35** | {{key:sc35:ISC}} | `N = (N1·T2 - N2·T1 + ΔE) / ΔT` | {{keycap:N}} Northing • {{keycap:D}} distance • {{keycap:A}} azimuth |
| **SC-14** | {{key:sc14:AWG}} | `D = 2 × R × L × I / 1000` | {{keycap:D}} drop ($\text{V}$) • {{keycap:R}} $\Omega/\text{kft}$ • {{keycap:L}} one-way run ($\text{ft}$) • {{keycap:I}} load ($\text{A}$) • {{keycap:G}} AWG gauge |
| **SC-14** | {{key:sc14:OFS}} | `T = O / SIN(A)` | {{keycap:T}} center-to-center travel • {{keycap:O}} obstruction offset • {{keycap:A}} bend angle $\theta$ |
| **SC-14** | {{key:sc14:FIT}} | `T = √(R² + O²)` | {{keycap:T}} rolling offset travel • {{keycap:R}} roll offset • {{keycap:O}} height offset |
| **SC-14** | {{key:sc14:BC}} | `C = D × SIN(180 / N)` | {{keycap:C}} chord distance • {{keycap:D}} bolt-circle diameter • {{keycap:N}} hole count |
| **SC-14** | {{key:sc14:Ω}} | `P = V × I` | {{keycap:P}} real power • {{keycap:V}} voltage • {{keycap:I}} current |
| **SC-14** | {{key:sc14:PF}} | `P = V × I × F` | {{keycap:P}} real power • {{keycap:V}} voltage • {{keycap:I}} current • {{keycap:F}} power factor $\cos\phi$ |
| **SC-14** | {{key:sc14:MTR}} | `H = T × N / 5252` | {{keycap:H}} horsepower • {{keycap:T}} torque ($\text{ft}\cdot\text{lb}$) • {{keycap:N}} spindle RPM |
| **SC-14** | {{key:sc14:FLA}} | `I = P × 746 / (1.732 × V × E)` | {{keycap:I}} full-load current • {{keycap:P}} horsepower • {{keycap:V}} voltage • {{keycap:E}} efficiency $\eta$ |
| **SC-14** | {{key:sc14:kVA}} | `S = V × I × 1.732 / 1000` | {{keycap:S}} apparent power ($\text{kVA}$) • {{keycap:V}} voltage • {{keycap:I}} current |
| **SC-14** | {{key:sc14:SFM}} | `N = 3.82 × S / D` | {{keycap:N}} spindle RPM • {{keycap:S}} surface speed $\text{SFM}$ • {{keycap:D}} tool diameter |
| **SC-14** | {{key:sc14:WLD}} | `H = 60 × V × I / (1000 × S)` | {{keycap:H}} heat input ($\text{kJ/in}$) • {{keycap:V}} arc voltage • {{keycap:I}} arc current • {{keycap:S}} travel speed |
| **SC-14** | {{key:sc14:PIP}} | `Q = A × V` | {{keycap:Q}} flow rate • {{keycap:A}} pipe cross-section • {{keycap:V}} fluid velocity |
| **SC-14** | {{key:sc14:Cᵥ}} | `Q = C × √(P / G)` | {{keycap:Q}} flow ($\text{GPM}$) • {{keycap:C}} valve $C_v$ • {{keycap:P}} $\Delta P$ ($\text{psi}$) • {{keycap:G}} specific gravity |
| **SC-14** | {{key:sc14:PMP}} | `P = Q × H / 3960` | {{keycap:P}} hydraulic/brake HP • {{keycap:Q}} flow ($\text{GPM}$) • {{keycap:H}} total dynamic head ($\text{ft}$) |
| **SC-16** | {{key:sc16:PWM}} | `F = C / (P × A)` | {{keycap:F}} PWM freq ($\text{Hz}$) • {{keycap:C}} clock $f_{\text{clk}}$ • {{keycap:P}} prescaler $P_{\text{PSC}}+1$ • {{keycap:A}} period $A_{\text{ARR}}+1$ |
| **SC-16** | {{key:sc16:ADC}} | `D = (V / R) × 2^N` | {{keycap:D}} digital code • {{keycap:V}} input $V_{\text{in}}$ • {{keycap:R}} reference $V_{\text{ref}}$ • {{keycap:N}} bit depth |
| **SC-16** | {{key:sc16:τ}} | `T = R × C` | {{keycap:T}} time constant $\tau$ ($\text{s}$) • {{keycap:R}} series resistance ($\Omega$) • {{keycap:C}} capacitance ($\text{F}$) |
| **SC-16** | {{key:sc16:BPS}} | `D = C / (16 × B)` | {{keycap:D}} baud divisor • {{keycap:C}} clock $f_{\text{clk}}$ • {{keycap:B}} baud rate ($\text{bps}$) |
| **SC-24** | {{key:sc24:FOV}} | `A = 2 × ATAN(W / (2 × F))` | {{keycap:A}} angle of view ($^\circ$) • {{keycap:W}} sensor gate width ($\text{mm}$) • {{keycap:F}} focal length ($\text{mm}$) |
| **SC-24** | {{key:sc24:EV}} | `N² = T × 2^E` | {{keycap:N}} aperture $f$-stop • {{keycap:T}} exposure time ($\text{s}$) • {{keycap:E}} exposure value $\text{EV}_{100}$ |
| **SC-24** | {{key:sc24:DOF}} | `H = F² / (N × C)` | {{keycap:H}} hyperfocal • {{keycap:F}} focal length ($\text{mm}$) • {{keycap:N}} $T$-stop • {{keycap:C}} circle of confusion ($\text{mm}$) |
| **SC-24** | {{key:sc24:TC}} | `F = S × R` | {{keycap:F}} total frame count • {{keycap:S}} elapsed seconds • {{keycap:R}} frame rate ($\text{fps}$) |
| **SC-24** | {{key:sc24:BIT}} | `R = B × F / 8` | {{keycap:R}} data rate ($\text{MB/s}$) • {{keycap:B}} bytes/frame • {{keycap:F}} frame rate ($\text{fps}$) |
| **SC-24** | {{key:sc24:LUX}} | `E = I / D²` | {{keycap:E}} illuminance ($\text{lux}$) • {{keycap:I}} luminous intensity ($\text{cd}$) • {{keycap:D}} distance ($\text{m}$) |
| **SC-50** | {{key:sc50:f₀}} | `F = 1 / (2π√(L×C))` | {{keycap:F}} resonant $f_0$ ($\text{Hz}$) • {{keycap:L}} inductance ($\text{H}$) • {{keycap:C}} capacitance ($\text{F}$) |
| **SC-50** | {{key:sc50:SWR}} | `S = (1 + G) / (1 - G)` | {{keycap:S}} standing wave ratio $\text{VSWR}$ • {{keycap:G}} reflection magnitude $\lvert\Gamma\rvert$ |
| **SC-50** | {{key:sc50:FSL}} | `L = 20LOG(D) + 20LOG(F) + 32.44` | {{keycap:L}} path loss $\text{FSPL}_{\text{dB}}$ • {{keycap:D}} link distance ($\text{km}$) • {{keycap:F}} carrier ($\text{MHz}$) |
| **SC-50** | {{key:sc50:LNK}} | `R = P + G - L` | {{keycap:R}} received $P_{\text{rx}}$ ($\text{dBm}$) • {{keycap:P}} transmit $P_{\text{tx}}$ • {{keycap:G}} net antenna gain • {{keycap:L}} total loss |
| **SC-50** | {{key:sc50:C/B}} | `C = B × LN(1 + S) / LN(2)` | {{keycap:C}} capacity ($\text{bps}$) • {{keycap:B}} bandwidth ($\text{Hz}$) • {{keycap:S}} linear $\text{SNR}$ |
| **SC-50** | {{key:sc50:Z₀}} | `Z = √(S × L)` | {{keycap:Z}} quarter-wave transformer $Z_q$ • {{keycap:S}} source impedance $Z_S$ • {{keycap:L}} load impedance $Z_L$ |
| **SC-50** | {{key:sc50:NF}} | `F = A + (B - 1) / G` | {{keycap:F}} cascaded noise factor • {{keycap:A}} stage 1 noise • {{keycap:B}} stage 2 noise • {{keycap:G}} stage 1 gain |
| **SC-60** | {{key:sc60:MW}} | `W = N × M` | {{keycap:W}} reagent mass ($\text{g}$) • {{keycap:N}} substance quantity ($\text{mol}$) • {{keycap:M}} molar mass ($\text{g/mol}$) |
| **SC-60** | {{key:sc60:PVT}} | `P × V = N × 8.3145 × T` | {{keycap:P}} pressure • {{keycap:V}} volume • {{keycap:N}} moles $n$ • {{keycap:T}} absolute temperature ($\text{K}$) |
| **SC-60** | {{key:sc60:εbc}} | `A = E × B × C` | {{keycap:A}} absorbance • {{keycap:E}} molar absorptivity $\varepsilon$ • {{keycap:B}} path length ($\text{cm}$) • {{keycap:C}} molarity ($\text{M}$) |
| **SC-60** | {{key:sc60:BUF}} | `P = K + LOG(A / H)` | {{keycap:P}} target $\text{pH}$ • {{keycap:K}} acid $\text{p}K_a$ • {{keycap:A}} base $[\text{A}^-]$ • {{keycap:H}} acid $[\text{HA}]$ |
| **SC-60** | {{key:sc60:C₁V₁}} | `C × V = D × U` | {{keycap:C}} stock $C_1$ • {{keycap:V}} aliquot $V_1$ • {{keycap:D}} target $C_2$ • {{keycap:U}} final volume $V_2$ |
| **SC-60** | {{key:sc60:ΔG}} | `G = H - T × S` | {{keycap:G}} Gibbs free energy $\Delta G$ • {{keycap:H}} enthalpy $\Delta H$ • {{keycap:T}} temp ($\text{K}$) • {{keycap:S}} entropy $\Delta S$ |
| **SC-60** | {{key:sc60:E°}} | `E = S - (0.05916 / N) × LOG(Q)` | {{keycap:E}} cell potential • {{keycap:S}} standard $E^\circ$ • {{keycap:N}} electrons transferred • {{keycap:Q}} reaction quotient |
| **SC-60** | {{key:sc60:EQV}} | `A × V = B × U` | {{keycap:A}} acid normality • {{keycap:V}} acid volume • {{keycap:B}} base normality • {{keycap:U}} base volume |
| **SC-60** | {{key:sc60:RXN}} | `N = C × V` | {{keycap:N}} solute moles • {{keycap:C}} molar concentration • {{keycap:V}} volume ($\text{L}$) |
| **SC-60** | {{key:sc60:CAL}} | `Q = M × C × T` | {{keycap:Q}} heat enthalpy • {{keycap:M}} solution mass • {{keycap:C}} specific heat • {{keycap:T}} temperature change $\Delta T$ |
| **SC-60** | {{key:sc60:Eₐ}} | `K = A × EXP(-E / (R × T))` | {{keycap:K}} rate constant $k$ • {{keycap:A}} pre-exponential factor • {{keycap:E}} activation energy $E_a$ • {{keycap:T}} absolute temperature |
| **SC-78** | {{key:sc78:BK%}} | `P = (I / F) × 100` | {{keycap:P}} baker's $\%$ • {{keycap:I}} ingredient weight • {{keycap:F}} total flour weight |
| **SC-78** | {{key:sc78:Tw}} | `W = 3 × D - R - F - M` | {{keycap:W}} water temp $T_w$ • {{keycap:D}} target $\text{DDT}$ • {{keycap:R}} room $T_r$ • {{keycap:F}} flour $T_f$ • {{keycap:M}} friction |
| **SC-78** | {{key:sc78:ABV}} | `A = (O - F) × 131.25` | {{keycap:A}} alcohol by volume $\%$ • {{keycap:O}} original gravity $\text{OG}$ • {{keycap:F}} final gravity $\text{FG}$ |
| **SC-78** | {{key:sc78:IBU}} | `I = W × A × U × 74.89 / V` | {{keycap:I}} bitterness $\text{IBU}$ • {{keycap:W}} hop mass ($\text{oz}$) • {{keycap:A}} alpha acid $\%$ • {{keycap:U}} utilization • {{keycap:V}} volume ($\text{gal}$) |
| **SC-78** | {{key:sc78:MSH}} | `S = (0.2 / R) × (T - G) + T` | {{keycap:S}} strike water temp • {{keycap:R}} water-grist ratio • {{keycap:T}} mash target • {{keycap:G}} dry grain temp |
| **SC-78** | {{key:sc78:CST}} | `P = C / (F / 100)` | {{keycap:P}} menu price • {{keycap:C}} portion cost • {{keycap:F}} target food cost $\%$ |
| **SC-80** | {{key:sc80:BSA}} | `B = √(H × W / 3600)` | {{keycap:B}} BSA ($\text{m}^2$) • {{keycap:H}} height ($\text{cm}$) • {{keycap:W}} weight ($\text{kg}$) • {{keycap:PAT}} patient profile |
| **SC-80** | {{key:sc80:GFR}} | `C = (140-A)×W / (72×S)` | {{keycap:C}} clearance ($\text{mL/min}$) • {{keycap:A}} age ($\text{yr}$) • {{keycap:W}} weight ($\text{kg}$) • {{keycap:S}} $\text{SCr}$ ($\text{mg/dL}$) • {{keycap:PAT}} |
| **SC-80** | {{key:sc80:DRP}} | `R = D × W × 60 / C` | {{keycap:R}} pump rate ($\text{mL/hr}$) • {{keycap:D}} dose ($\text{mcg/kg/min}$) • {{keycap:W}} weight ($\text{kg}$) • {{keycap:C}} concentration ($\text{mcg/mL}$) • {{keycap:PAT}} |
| **SC-80** | {{key:sc80:PK}} | `T = 0.693 × V / C` | {{keycap:T}} half-life $t_{1/2}$ ($\text{hr}$) • {{keycap:V}} volume $V_d$ ($\text{L}$) • {{keycap:C}} clearance $\text{CL}$ ($\text{L/hr}$) |
| **SC-80** | {{key:sc80:IV}} | `R = V / T` | {{keycap:R}} volumetric pump rate ($\text{mL/hr}$) • {{keycap:V}} total bag volume ($\text{mL}$) • {{keycap:T}} infusion time ($\text{hr}$) |
| **SC-80** | {{key:sc80:DOS}} | `T = W × D` | {{keycap:T}} total medication dose ($\text{mg}$) • {{keycap:W}} patient weight ($\text{kg}$) • {{keycap:D}} unit dose ($\text{mg/kg}$) |
| **SC-80** | {{key:sc80:BRN}} | `V = 4 × W × B` | {{keycap:V}} 24-hr fluid volume ($\text{mL}$) • {{keycap:W}} patient weight ($\text{kg}$) • {{keycap:B}} burn surface $\%$ |
| **SC-80** | {{key:sc80:ICU}} | `Q = H × S / 1000` | {{keycap:Q}} cardiac output ($\text{L/min}$) • {{keycap:H}} heart rate • {{keycap:S}} stroke volume ($\text{mL}$) |
| **SC-80** | {{key:sc80:VIL}} | `A = A0 × 2^(-T / H)` | {{keycap:A}} remaining activity • {{keycap:O}} initial activity $A_0$ • {{keycap:T}} elapsed decay time • {{keycap:H}} isotope half-life |
| **SC-95** | {{key:sc95:TVM}} | `PV(1+I)^N + PMT... + FV = 0` | {{keycap:N}} periods • {{keycap:I%}} rate • {{keycap:PV}} present value • {{keycap:PMT}} payment • {{keycap:FV}} future value • {{keycap:END}}/{{keycap:BEG}} |
| **SC-95** | {{key:sc95:CF}} | `V = C × (1 - (1 + R/100)^-N) / (R/100) - I` | {{keycap:V}} net present value • {{keycap:C}} uniform cash flow • {{keycap:R}} discount rate / $\text{IRR}$ ($\%$) • {{keycap:N}} periods • {{keycap:I}} outlay |
| **SC-95** | {{key:sc95:BND}} | `P = C × (1 - (1 + Y/100)^-N) / (Y/100) + F / (1 + Y/100)^N` | {{keycap:P}} bond price • {{keycap:C}} periodic coupon • {{keycap:Y}} periodic yield ($\%$) • {{keycap:N}} periods • {{keycap:F}} par face value |
| **SC-95** | {{key:sc95:DEP}} | `D = (C - S) / L` | {{keycap:D}} annual depreciation • {{keycap:C}} initial asset cost • {{keycap:S}} salvage value • {{keycap:L}} useful life |
| **SC-95** | {{key:sc95:MGN}} | `M = (P - C) / P × 100` | {{keycap:M}} gross margin $\%$ • {{keycap:P}} selling price • {{keycap:C}} unit cost |
| **SC-95** | {{key:sc95:MKP}} | `U = (P - C) / C × 100` | {{keycap:U}} markup on cost $\%$ • {{keycap:P}} selling price • {{keycap:C}} unit cost |
| **SC-95** | {{key:sc95:EAR}} | `E = ((1 + A / (100 × M))^M - 1) × 100` | {{keycap:E}} effective annual rate $\%$ • {{keycap:A}} nominal annual rate • {{keycap:M}} compounding periods |
| **SC-95** | {{key:sc95:CGR}} | `F = P × (1 + R / 100)^N` | {{keycap:F}} future compound value • {{keycap:P}} present base value • {{keycap:R}} annual growth rate $\%$ • {{keycap:N}} years |
| **SC-95** | {{key:sc95:BEP}} | `Q = F / (P - V)` | {{keycap:Q}} breakeven production quantity • {{keycap:F}} total fixed costs • {{keycap:P}} unit price • {{keycap:V}} variable cost |
| **SC-95** | {{key:sc95:EOQ}} | `Q = √(2 × D × S / H)` | {{keycap:Q}} economic order quantity • {{keycap:D}} annual demand • {{keycap:S}} order setup cost • {{keycap:H}} holding cost |
| **SC-95** | {{key:sc95:TAX}} | `T = P × (1 + R / 100)` | {{keycap:T}} total gross price with tax • {{keycap:P}} net pretax price • {{keycap:R}} sales tax rate $\%$ |
| **SC-95** | {{key:sc95:Cpk}} | `C = (U - L) / (6 × S)` | {{keycap:C}} potential capability $C_p$ / $C_{pk}$ • {{keycap:U}} upper tolerance $\text{USL}$ • {{keycap:L}} lower tolerance $\text{LSL}$ • {{keycap:S}} sample standard deviation |
| **SC-95** | {{key:sc95:CI}} | `E = Z × S / √N` | {{keycap:E}} error margin • {{keycap:Z}} normal score $z_{\alpha/2}$ • {{keycap:S}} sample standard deviation • {{keycap:N}} sample size |
| **SC-95** | {{key:sc95:n*}} | `N = (Z × S / E)²` | {{keycap:N}} sample size $n^*$ • {{keycap:Z}} critical quantile $z_{\alpha/2}$ • {{keycap:S}} dispersion $s$ • {{keycap:E}} margin of error |
| **SC-95** | {{key:sc95:pN}} | `P = Φ((X - M) / S)` | {{keycap:P}} cumulative probability • {{keycap:X}} observed value • {{keycap:M}} mean $\mu$ • {{keycap:S}} standard deviation $\sigma$ |

### Built-in Interactive Guided Tutorials ({{key:f}} {{key:C}} / {{key:?}})

Every calculator in the StackCalc Domain Series includes an on-device interactive tutor engine, launched by pressing {{key:f}} {{key:C}} (yellow-shifted {{key:?}}). The runner observes keypresses in real-time, coaching the user step-by-step through foundational RPN mechanics and flagship domain calculations:

| Instrument | Built-in Lesson 1 | Built-in Lesson 2 | Built-in Lesson 3 |
| :--- | :--- | :--- | :--- |
| **SC-35** | **RPN Primer:** Distance and bearing coordinate product | **Field Aviation:** Crosswind component and heading correction | **Spirit Leveling:** Benchmark elevation and differential rod transfer ({{key:sc35:LVL}}) |
| **SC-14** | **RPN Primer:** Single-phase real power ($P = V \times I$) | **Roof Framing:** Rafter run, rise, and hypotenuse geometry | **Voltage Drop:** NEC conductor series drop along long feeders ({{key:sc14:AWG}}) |
| **SC-16** | **RPN Primer:** Hexadecimal address offset accumulation | **CIDR Bitwise:** Netmask synthesis and usable host capacity | **Bitwise Logic:** Multi-byte bitwise AND masking (`0xDEAD AND 0xBEEF`) |
| **SC-24** | **RPN Primer:** Frame count accumulation ($24\text{ fps} \times 5\text{ s}$) | **Audio Exposure:** Base-2 EV balance and rotary shutter angle | **Photometrics:** Inverse-square illuminance and falloff ({{key:sc24:LUX}}) |
| **SC-50** | **RPN Primer:** Transmitter power and antenna gain summation | **RF Physics:** Dipole physical resonance and quarter-wave length | **Path Loss:** Friis free-space microwave link loss ({{key:sc50:FSL}}) |
| **SC-60** | **RPN Primer:** Reagent molar mass to gram conversion | **Lab Molarity:** Solution concentration and primary standards | **Buffer pH:** Henderson–Hasselbalch conjugate equilibrium ({{key:sc60:BUF}}) |
| **SC-78** | **RPN Primer:** Sourdough flour and hydration mass sum | **Brewing ABV:** Hydrometer extract drop and alcohol yield | **Water Temp:** Four-term Desired Dough Temperature balance ({{key:sc78:Tw}}) |
| **SC-80** | **RPN Primer:** Unit dose to total daily administration | **Pediatric Dosing:** Body weight-based milligram calculation | **Vasoactive Drip:** Critical microgram infusion rate ({{key:sc80:DRP}}) |
| **SC-95** | **RPN Primer:** Gross revenue minus expense operating profit | **Margin & Markup:** Selling price versus cost percentage | **Gaussian CDF:** Standard normal cumulative probability tail ({{key:sc95:pN}}) |

### Dynamic Live Reference Ledgers ({{key:▦}})

Pressing {{key:▦}} ({{key:g}} {{key:+/-}}) opens the non-destructive domain reference ledger. Unlike a static table of physical constants, the StackCalc ledger dynamically tracks data accumulated in real time with {{key:sc35:PT+}} or {{key:Σ+}}:

* **SC-35 (`@COGO`):** Accumulates polygon perimeter coordinates, calculates cumulative linear misclosure (`CLOS`), and computes Gauss's Shoelace polygon area (`AREA`) in square feet, acres, and hectares.
* **SC-14 (`@BOM` / Service Sizing):** Sums individual branch circuit loads via {{key:Σ+}}, calculates total load (`TOT LOAD`), applies the NEC 125% continuous duty multiplier (`80% CONT`), and automatically selects the minimum standard service panel rating (`PNL MIN`: 100A, 125A, 200A, 400A).
* **SC-16 (Registers & Cyber):** Decomposes the active register into simultaneous `HEX`, `DEC`, `OCT`, and `BIN` representations, extracts IEEE-754 32/64-bit sign, exponent, and mantissa bitfields, formats fixed-point `Q16.16`, and calculates 4-byte and 8-byte struct alignment padding (`ALIGN 4B`, `ALIGN 8B`).
* **SC-24 (Cinema Production Log):** Logs scene takes with {{key:Σ+}}, tracking total accumulated timecode (`TOTAL TC`), total frames (`TOTAL F`), take count (`TAKES`), average take duration (`AVG TAKE`), camera raw data generated (`DATA GEN` in GB), and remaining card recording runtime (`512G REM` in hours).
* **SC-50 (Smith & Friis Cascade):** Evaluates complex reflection parameters (`|GAMMA|`, `GAMMA ANG`, `VSWR`, `RET LOSS`, normalized $r/z_0$ and $x/z_0$), and sums multi-stage RF amplifiers via {{key:Σ+}} to compute total cascaded gain (`CASC G`) and Friis cascaded noise figure (`CASC NF`).
* **SC-60 (Solution & Formula Mass Breakdown):** Accumulates gravimetric solute masses via {{key:Σ+}} to display solute mass percent (`SOL1 %`, `TOT MASS`), and parses active chemical formulas (`FML`, `MW`) into live per-element mass percentage breakdowns (`H MASS%`, `O MASS%`, etc.).
* **SC-78 (Baking Formula Ledger):** Anchors formula flour weight (`FLOUR`), computes live Baker's percentages for all added ingredients (`ING1 %`, `ING2 %`), and tracks total batch dough weight (`TOT W`).
* **SC-80 (Patient Clinical Dashboard):** Displays the persistent Patient Profile: patient weight (`PAT WT`), height (`PAT HT`), age and sex (`PAT AGE`), serum creatinine (`PAT SCR`), Mosteller Body Surface Area (`PAT BSA`), Devine Ideal Body Weight (`PAT IBW`), and Cockcroft–Gault creatinine clearance (`PAT GFR`).
* **SC-95 (Bivariate Statistics & Regression):** Accumulates $(x, y)$ sample points via {{key:Σ+}}, tracking sample count ($n$), means ($\bar{x}, \bar{y}$), standard deviations ($s_x, s_y$), ordinary least-squares slope ($m$), intercept ($b$), Pearson correlation ($r$), coefficient of determination ($r^2$), and the last 10 points.

---

## Geomatics, Land Surveying, and Flight Navigation Keycaps

On the **SC-35** the Row 1 and Row 2 geomatics keys and shifted trigonometric/navigation operators execute plane coordinate geometry (COGO), horizontal and vertical highway curves, Bowditch traverse closure, sexagesimal angle conversions, and E6B aviation wind-triangle and density-altitude solutions:

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| {{key:sc35:TRV}} / {{key:sc35:PT+}} | Row 1 Col 0 Primary / Row 2 Col 0 Yellow | **Forward Traverse & Station Accumulator:** Consumes distance $D$ and azimuth $\alpha$ to resolve $(\Delta N, \Delta E)$ ({{key:sc35:N⇄E}} swaps Northing/Easting), and {{key:sc35:PT+}} accumulates station coordinates into `@COGO`. |
| {{key:sc35:INV}} / {{key:sc35:CLS}} | Row 1 Col 1 Primary / Blue Shift | **Coordinate Inverse & Bowditch Closure:** Consumes $\Delta N$ ($Y$) and $\Delta E$ ($X$) to return azimuth $\alpha$ and distance $D$; {{key:sc35:CLS}} computes traverse closure error and precision ratio. |
| {{key:sc35:BRG}} / {{key:sc35:N⇄E}} | Row 1 Col 2 Primary / Yellow Shift | **Quadrant Bearing & Axis Swap:** Formats azimuth in $X$ as surveyor quadrant bearing (NE, SE, SW, NW), and {{key:sc35:N⇄E}} swaps active Northing/Easting coordinates. |
| {{key:sc35:ISC}} | Row 4 Col 1 Yellow Shift ({{key:sc35:7}}) | **Bearing-Bearing Intersection Workspace ({{key:sc35:ISC}}):** Solves `N = (N1·T2 - N2·T1 + ΔE) / ΔT` ({{keycap:N}}, {{keycap:D}}, {{keycap:A}}) or solves directly on the stack with bearings in $Y$ and $X$. |
| {{key:sc35:CRV}} / {{key:sc35:STA}} | Row 1 Col 3 Primary / Row 2 Col 1 Blue | **Horizontal Curve Workspace ({{key:sc35:CRV}}) & Stationing:** Solves circular arc `L = R × D × π / 180` ({{keycap:L}}, {{keycap:R}}, {{keycap:D}}) and formats highway stationing `XX+XX.XX`. |
| {{key:sc35:SLP}} / {{key:sc35:VCV}} / {{key:sc35:GR%}} | Row 1 Col 4 (Primary / Yellow / Blue) | **Slope Reduction, Vertical Curve & Grade %:** Reduces slope distance/angle ({{key:sc35:SLP}}), solves parabolic vertical curves ({{key:sc35:VCV}}), and computes percent grade ({{key:sc35:GR%}}). |
| {{key:sc35:LVL}} / {{key:sc35:FLW}} / {{key:sc35:△}} | Row 1 Col 1 Yellow / Row 1 Col 5 (Prim/Blue) | **Differential Leveling ({{key:sc35:LVL}}), Open-Channel Flow ({{key:sc35:FLW}}) & Triangle ({{key:sc35:SOLVE}}):** Solves `E = H + B - F` ({{keycap:E}}, {{keycap:H}}, {{keycap:B}}, {{keycap:F}}), continuity `Q = A × V`, and triangle area `A = 0.5 × B × H`. |
| {{key:sc35:WND}} / {{key:sc35:XWC}} | Row 5 Col 2 (Yellow / Blue Shift) | **E6B Wind Triangle Workspace ({{key:sc35:WND}}) & Crosswind:** Solves `X = V × SIN(A)` ({{keycap:X}}, {{keycap:V}}, {{keycap:A}}) or evaluates crosswind/headwind components on the stack ({{key:sc35:XWC}}). |
| {{key:sc35:▸HR}} / {{key:sc35:▸HMS}} / {{key:sc35:ALT}} | Row 7 Col 3 (Primary / Yellow / Blue) | **Sexagesimal Conversions & Density Altitude ({{key:sc35:ALT}}):** Converts `DDD.MMSS` to decimal degrees/hours ({{key:sc35:▸HR}}) and back ({{key:sc35:▸HMS}}), and solves density altitude `D = P + 120 × (T - 15)` ({{keycap:D}}, {{keycap:P}}, {{keycap:T}}). |
| {{key:sc35:TSD}} / {{key:sc35:CG}} / {{key:sc35:TID}} | Row 2 Col 2 (Primary / Yellow / Blue) | **Time-Speed-Distance ({{key:sc35:TSD}}), Weight & Balance ({{key:sc35:CG}}) & Tidal Height:** Solves `D = S × T` ({{keycap:D}}, {{keycap:S}}, {{keycap:T}}), moment `M = W × A` ({{keycap:M}}, {{keycap:W}}, {{keycap:A}}), and rule-of-twelfths tidal stage ({{key:sc35:TID}}). |
| {{key:sc35:▸HR}} / {{key:sc35:▸HMS}} / {{key:sc35:▸DEG}} / {{key:sc35:▸RAD}} / {{key:sc35:▸GRD}} | Angular & Sexagesimal Shifts | Converts packed sexagesimal `DDD.MMSS` to decimal degrees/hours ({{key:sc35:▸HR}}) and back ({{key:sc35:▸HMS}}), or converts between degrees, radians, and gradians. |
| {{key:sc35:▸θ,r}} / {{key:sc35:▸y,x}} / {{key:sc35:f-i}} | Coordinate & Feet-Inch Shifts | Converts between Rectangular $(Y, X)$ and Polar $(r, \theta)$ coordinates and enters/formats feet-inch-fractions ({{key:sc35:f-i}}). |

---

## Industrial Trades, Electrical, and Mechanical Keycaps

On the **SC-14** the Row 1 and Row 2 electrical, conduit, piping, and machining keys pair with dimensional shift converters to resolve National Electrical Code (NEC) conductor sizing, three-phase power and motor full-load amps, conduit offset bends, industrial process flow, and spindle machining speeds:

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| {{key:sc14:AWG}} / {{key:sc14:MTR}} / {{key:sc14:FLA}} | Row 1 Col 1 (Primary / Yellow / Blue) | **NEC Voltage Drop ({{key:sc14:AWG}}), Motor HP ({{key:sc14:MTR}}) & Full-Load Amps ({{key:sc14:FLA}}):** Looks up NEC Table 8 resistance $R$ ($\Omega/\text{kft}$) and solves `D = 2 × R × L × I / 1000` ({{keycap:D}}, {{keycap:R}}, {{keycap:L}}, {{keycap:I}}, {{keycap:G}}), motor torque `H = T × N / 5252`, and three-phase {{key:sc14:FLA}}. |
| {{key:sc14:OFS}} / {{key:sc14:MIT}} / {{key:sc14:FIT}} | Row 1 Col 2 (Primary / Yellow / Blue) | **Conduit Offset ({{key:sc14:OFS}}), Miter Angle & Pipe Fitting Take-Off:** Solves `T = O / SIN(A)` ({{keycap:T}}, {{keycap:O}}, {{keycap:A}}) on the stack or bidirectionally, miter cut angle ({{key:sc14:MIT}}), and elbow fitting take-off ({{key:sc14:FIT}}). |
| {{key:sc14:PF}} / {{key:sc14:Ω}} / {{key:sc14:kVA}} / {{key:sc14:x∥y}} | Electrical Power & Impedance Keys | **Power Factor ({{key:sc14:PF}}), Ohm's Law ({{key:sc14:XEQ}}), Transformer ({{key:sc14:XEQ}}) & Parallel (`x∥y`):** Solves real power `P = V × I × F` ({{keycap:P}}, {{keycap:V}}, {{keycap:I}}, {{keycap:F}}), `P = V × I`, three-phase `S = V × I × 1.732 / 1000`, and parallel impedance $X \parallel Y = XY/(X+Y)$. |
| {{key:sc14:PIP}} / {{key:sc14:SCH}} / {{key:sc14:WAL}} | Row 1 Col 4 (Primary / Yellow / Blue) | **Pipe Continuity ({{key:sc14:PIP}}), Schedule Lookup & Barlow Wall Thickness:** Solves `Q = A × V` ({{keycap:Q}}, {{keycap:A}}, {{keycap:V}}), pipe internal diameter ({{key:sc14:SCH}}), and pressure wall thickness ({{key:sc14:WAL}}). |
| {{key:sc14:PMP}} / {{key:sc14:TNK}} / {{key:sc14:Cᵥ}} / {{key:sc14:ORF}} / {{key:sc14:NPH}} | Hydraulics & Process Keys | **Pump Power ({{key:sc14:PMP}}), Tank Volume, Valve $C_v$ ({{key:sc14:Cᵥ}}), Orifice & NPSH:** Solves `P = Q × H / 3960` ({{keycap:P}}, {{keycap:Q}}, {{keycap:H}}), `Q = C × √(P / G)` ({{keycap:Q}}, {{keycap:C}}, {{keycap:P}}, {{keycap:G}}),partially filled tank volume ({{key:sc14:TNK}}), orifice flow ({{key:sc14:ORF}}), and net positive suction head ({{key:sc14:NPH}}). |
| {{key:sc14:mA}} / {{key:sc14:RTD}} / {{key:sc14:STM}} | Row 2 Col 2 (Primary / Yellow / Blue) | **4–20 mA Loop Scaling, Callendar–Van Dusen RTD & Saturated Steam:** Converts between $4\text{--}20\text{ mA}$ current and engineering span ({{key:sc14:mA}}), Pt100 RTD resistance/temperature ({{key:sc14:RTD}}), and steam pressure/temperature ({{key:sc14:STM}}). |
| {{key:sc14:SFM}} / {{key:sc14:WLD}} / {{key:sc14:TAP}} / {{key:sc14:RPM}} / {{key:sc14:BC}} | Machining, Welding & Millwright Keys | **Surface Speed ({{key:sc14:SFM}}), Weld Heat ({{key:sc14:WLD}}), Tap Drill, Belt Ratio & Bolt Circle ({{key:sc14:BC}}):** Solves spindle speed `N = 3.82 × S / D` ({{keycap:N}}, {{keycap:S}}, {{keycap:D}}), weld heat input `H = 60 × V × I / (1000 × S)` ({{keycap:H}}, {{keycap:V}}, {{keycap:I}}, {{keycap:S}}), tap drill allowance ({{key:sc14:TAP}}), pulley ratio ({{key:sc14:RPM}}), and bolt-circle chord `C = D × SIN(180 / N)` ({{keycap:C}}, {{keycap:D}}, {{keycap:N}}). |
| {{key:sc14:f-i}} / {{key:sc14:▸mm}} / {{key:sc14:▸in}} / {{key:sc14:▸cm}} / {{key:sc14:▸kW}} / {{key:sc14:▸HP}} / {{key:sc14:▸PSI}} / {{key:sc14:▸kPa}} / {{key:sc14:▸Nm}} / {{key:sc14:▸lbf}} / {{key:sc14:▸GPM}} / {{key:sc14:▸MGD}} | Dimensional & Trade Converters | Enters/formats feet-inch-fractions ({{key:sc14:f-i}}) and converts between metric and US customary length, power, pressure, torque, and flow units. |

---

## Systems Programming, Embedded, and Cyber Operations Keycaps

On the **SC-16** radix and word-architecture keys pair with bitwise logical operators, bit shifts, circular rotations, embedded timer/ADC workspaces, and modular/network keys (while Row 0 softkeys automatically become hexadecimal digits {{keycap:A}}–{{keycap:F}} whenever {{key:sc16:HEX}} mode is active):

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| {{key:sc16:HEX}} / {{key:sc16:DEC}} / {{key:sc16:OCT}} / {{key:sc16:BIN}} | Row 1 Col 1 & Col 5 | Switches display and keypad entry across base-16 hexadecimal (binding softkeys to {{keycap:A}}–{{keycap:F}}), base-10 decimal, base-8 octal, and base-2 binary view. |
| {{key:sc16:WSZ}} / {{key:sc16:UNS}} / {{key:sc16:NEG}} / {{key:sc16:OVF}} | Word Architecture & Sign Keys | Cycles hardware word width across 8-bit, 16-bit, 32-bit, and 64-bit registers ({{key:sc16:WSZ}}), toggles unsigned interpretation ({{key:sc16:UNS}}), applies two's complement negation $-X \equiv \sim X + 1 \pmod{2^W}$ ({{key:sc16:NEG}}), and inspects carry/overflow status ({{key:sc16:OVF}}). |
| {{key:sc16:FLT}} / {{key:sc16:F16}} / {{key:sc16:F64}} / {{key:sc16:Q.n}} / {{key:sc16:FXP}} | Row 1 Col 2 & Row 7 Col 2 | Encodes/decodes IEEE 754 `float32` ({{key:sc16:FLT}}), `float16` ({{key:sc16:F16}}), and `float64` ({{key:sc16:F64}}) bit patterns, and converts real coefficients to/from $Q_{m.n}$ fixed-point integers ({{key:sc16:Q.n}}, {{key:sc16:FXP}}). |
| {{key:sc16:&}} / {{key:sc16:~&}} / {{key:sc16:~}} / {{key:sc16:&#124;}} / {{key:sc16:~&#124;}} / {{key:sc16:⊕}} | Row 2 Cols 3–5 (Primary / Yellow / Blue) | Bitwise logical {{key:sc16:&}}, {{key:sc16:~&}}, {{key:sc16:~}}, {{key:sc16:|}} ({{key:sc16:&#124;}}), {{key:sc16:~|}} ({{key:sc16:~&#124;}}), and {{key:sc16:⊕}} masked to active {{key:sc16:WSZ}}. |
| {{key:sc16:≪}} / {{key:sc16:≫}} / {{key:sc16:ASR}} / {{key:sc16:ROR}} | Row 1 Cols 3–4 (Primary / Yellow / Blue) | Logical shift left ({{key:sc16:≪}}, $Y \ll X$), logical shift right ({{key:sc16:≫}}, $Y \ggg X$), sign-preserving arithmetic shift right ({{key:sc16:ASR}}, $Y \gg X$), and circular bit rotation ({{key:sc16:ROR}}). |
| {{key:sc16:SB}} / {{key:sc16:CB}} / {{key:sc16:B?}} / {{key:sc16:MSK}} | Bitfield Manipulation Keys | Sets ({{key:sc16:SB}}), clears ({{key:sc16:CB}}), or tests ({{key:sc16:B?}}) bit index $X$ in word $Y$, or generates a contiguous $X$-bit mask $2^X - 1$ ({{key:sc16:MSK}}). |
| {{key:sc16:#B}} / {{key:sc16:CLZ}} / {{key:sc16:2ˣ}} / {{key:sc16:lg}} | Bit Counting & Base-2 Keys | Counts set `1`-bits (Hamming weight {{key:sc16:#B}}) or leading zeros ({{key:sc16:CLZ}}) in $X$, and evaluates exact base-2 powers $2^X$ ({{key:sc16:2ˣ}}) and $\log_2(X)$ ({{key:sc16:lg}}). |
| {{key:sc16:PWM}} / {{key:sc16:τ}} / {{key:sc16:ALN}} / {{key:sc16:BPS}} | Row 4 Col 4, Row 3 Col 4 & Row 2 Col 1 | **Timer ({{key:sc16:PWM}}), RC Settling ({{key:sc16:τ}}), Memory Alignment & UART Baud:** Solves `F = C / (P × A)` ({{keycap:F}}, {{keycap:C}}, {{keycap:P}}, {{keycap:A}}), RC time constant `T = R × C` ({{keycap:T}}, {{keycap:R}}, {{keycap:C}}), power-of-two address alignment ({{key:sc16:ALN}}), and UART baud divisor ({{key:sc16:BPS}}). |
| {{key:sc16:ADC}} / {{key:sc16:DAC}} | Mixed-Signal Keys | **ADC Quantization Workspace ({{key:sc16:ADC}}) & DAC Output:** Solves `D = (V / R) × 2^N` ({{keycap:D}}, {{keycap:V}}, {{keycap:R}}, {{keycap:N}}) and reconstructs analog DAC output voltage ({{key:sc16:DAC}}). |
| {{key:sc16:MOD}} / {{key:sc16:÷R}} / {{key:sc16:WSZ}} / {{key:sc16:NET}} / {{key:sc16:CRC}} / {{key:sc16:SWP}} | Row 7 Col 3 & Networking/Data Keys | Evaluates remainder $Y \bmod X$ ({{key:sc16:MOD}}), integer quotient ({{key:sc16:÷R}}), word size cycle ({{key:sc16:WSZ}}), IPv4 {{key:sc16:NET}} host capacity, IEEE 802.3 CRC-32 ({{key:sc16:CRC}}), and endian swap ({{key:sc16:SWP}}). |
| {{key:sc16:▸B}} / {{key:sc16:▸bit}} / {{key:sc16:▸KiB}} / {{key:sc16:▸MiB}} / {{key:sc16:▸GiB}} / {{key:sc16:▸TiB}} / {{key:sc16:▸ms}} / {{key:sc16:▸μs}} / {{key:sc16:▸MHz}} / {{key:sc16:▸GHz}} / {{key:sc16:▸cyc}} / {{key:sc16:▸ns}} | Storage & Clock Converters | Converts between IEC binary storage prefixes ($2^{10}$–$2^{40}$), bytes/bits ($\times 8$), and clock frequency, period, and cycle counts. |

---

## Cinema Optics, Broadcast Timecode, and Sound Keycaps

On the **SC-24** the Row 1 and Row 2 camera, lighting, audio, and DIT keys pair with Row 7 SMPTE timecode solvers to evaluate angle of view, rotary shutter exposure, hyperfocal and depth-of-field lens geometry, mired color-temperature shifts, and location sound acoustics:

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| {{key:sc24:FOV}} / {{key:sc24:▸35}} / {{key:sc24:▸16}} / {{key:sc24:W:H}} | Optics & Format Keys | **Angle of View ({{key:sc24:FOV}}), Crop Factors & Aspect Ratio:** Solves `A = 2 × ATAN(W / (2 × F))` ({{keycap:A}}, {{keycap:W}}, {{keycap:F}}), applies Super-35 ({{key:sc24:▸35}}) and 16mm ({{key:sc24:▸16}}) crop equivalents, and evaluates frame aspect ratio ({{key:sc24:W:H}}). |
| {{key:sc24:EV}} / {{key:sc24:SHT}} / {{key:sc24:GEL}} | Row 1 Col 1 (Primary / Yellow / Blue) | **Exposure Value ({{key:sc24:EV}}), Rotary Shutter & CTO/CTB Gel Mired Shift:** Solves `N² = T × 2^E` ({{keycap:N}}, {{keycap:T}}, {{keycap:E}}), shutter exposure time $t = \theta_{\text{shutter}} / (360 \cdot \text{FPS})$ ({{key:sc24:SHT}}), and mired color shift $10^6/T_2 - 10^6/T_1$ ({{key:sc24:GEL}}). |
| {{key:sc24:LUX}} / {{key:sc24:BM°}} / {{key:sc24:▸fc}} / {{key:sc24:▸lux}} / {{key:sc24:▸MRD}} / {{key:sc24:▸K}} | Photometrics & Color Keys | **Inverse-Square Illuminance ({{key:sc24:LUX}}), Beam Spread & Photometric Units:** Solves `E = I / D²` ({{keycap:E}}, {{keycap:I}}, {{keycap:D}}), luminaire beam diameter ({{key:sc24:BM°}}), footcandles/lux ({{key:sc24:▸fc}}, {{key:sc24:▸lux}}), and mired/Kelvin conversions ({{key:sc24:▸MRD}}, {{key:sc24:▸K}}). |
| {{key:sc24:DOF}} / {{key:sc24:HFD}} / {{key:sc24:DPT}} / {{key:sc24:▸EV}} / {{key:sc24:▸ND}} | Depth of Field & Filter Keys | **Depth of Field ({{key:sc24:DOF}}), Hyperfocal, Diopter & ND Stops:** Solves `H = F² / (N × C)` ({{keycap:H}}, {{keycap:F}}, {{keycap:N}}, {{keycap:C}}), direct hyperfocal distance ({{key:sc24:HFD}}), close-up diopter power ({{key:sc24:DPT}}), and optical density / EV stops ({{key:sc24:▸EV}}, {{key:sc24:▸ND}}). |
| {{key:sc24:dB}} / {{key:sc24:SPL}} / {{key:sc24:λ}} / {{key:sc24:vₛ}} / {{key:sc24:DLY}} / {{key:sc24:SYN}} | Acoustic & Audio Keys | Evaluates decibel voltage/power ratios ({{key:sc24:dB}}), inverse-square SPL attenuation ({{key:sc24:SPL}}), acoustic wavelength ({{key:sc24:λ}}) using speed of sound {{key:sc24:vₛ}}, delay tower alignment ({{key:sc24:DLY}}), and audio-video lip-sync offset ({{key:sc24:SYN}}). |
| {{key:sc24:BIT}} / {{key:sc24:TB}} / {{key:sc24:DMX}} / {{key:sc24:PWR}} / {{key:sc24:W/A}} | DIT Data & Gaffer Power Keys | **Uncompressed Data Rate ({{key:sc24:BIT}}), RAID Capacity, DMX512 & Generator Load:** Solves `R = B × F / 8` ({{keycap:R}}, {{keycap:B}}, {{keycap:F}}), storage footprint ({{key:sc24:TB}}), DMX universe/address ({{key:sc24:DMX}}), and stage tie-in load ({{key:sc24:PWR}}, {{key:sc24:W/A}}). |
| {{key:sc24:TC}} / {{key:sc24:FPS}} / {{key:sc24:DF}} / {{key:sc24:+TC}} / {{key:sc24:-TC}} / {{key:sc24:▸FRM}} / {{key:sc24:▸TC}} | Timecode & Frame-Rate Keys | **SMPTE Timecode Workspace ({{key:sc24:TC}}) & Frame Arithmetic:** Solves `F = S × R` ({{keycap:F}}, {{keycap:S}}, {{keycap:R}}), sets frame rate ({{key:sc24:FPS}}), computes SMPTE 29.97 drop-frame drift ({{key:sc24:DF}}), adds/subtracts timecode ({{key:sc24:+TC}}, {{key:sc24:-TC}}), and converts between frames and `HH:MM:SS:FF` ({{key:sc24:▸FRM}}, {{key:sc24:▸TC}}). |

---

## RF Spectrum, Transmission Lines, and Microwave Keycaps

On the **SC-50** the Row 1 and Row 2 RF propagation, impedance matching, and dynamic range keys pair with bidirectional Equation Workspaces and decibel converters to solve transmission-line standing waves, resonant LC networks, free-space link budgets, cascaded noise figures, Shannon capacity, and radar Doppler shifts:

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| {{key:sc50:dBm}} / {{key:sc50:▸dBm}} / {{key:sc50:▸mW}} / {{key:sc50:▸dBW}} / {{key:sc50:▸dBV}} / {{key:sc50:▸μV}} | Power & Voltage Decibel Keys | Converts linear power in milliwatts/Watts in $X$ to $\text{dBm}$ ($10\log_{10}(P_{\text{mW}})$), inverse $\text{mW}$ ($10^{X/10}$), Watt-referenced $\text{dBW}$ ($P_{\text{dBm}} - 30$), or RMS voltage across active impedance {{key:sc50:Z₀}} ($50\,\Omega$ default). |
| {{key:sc50:SWR}} / {{key:sc50:Γ}} / {{key:sc50:TLN}} / {{key:sc50:COX}} | Impedance & Transmission-Line Keys | **Standing Wave ({{key:sc50:SWR}}) & Quarter-Wave ({{key:sc50:Z₀}}) Workspaces:** Solves `S = (1 + G) / (1 - G)` ({{keycap:S}}, {{keycap:G}}) and quarter-wave transformer `Z = √(S × L)` ({{keycap:Z}}, {{keycap:S}}, {{keycap:L}}), transmission-line electrical length ({{key:sc50:TLN}}), and coaxial attenuation ({{key:sc50:COX}}). |
| {{key:sc50:FSL}} / {{key:sc50:LNK}} / {{key:sc50:F₁}} / {{key:sc50:λ/L}} | Propagation & Antenna Keys | **Friis Path Loss ({{key:sc50:FSL}}), Link Budget ({{key:sc50:LNK}}), Fresnel Zone & Whip Length:** Solves `L = 20LOG(D) + 20LOG(F) + 32.44` ({{keycap:L}}, {{keycap:D}}, {{keycap:F}}), link budget `R = P + G - L` ({{keycap:R}}, {{keycap:P}}, {{keycap:G}}, {{keycap:L}}), first Fresnel zone radius ({{key:sc50:F₁}}), and quarter-wave whip length ({{key:sc50:λ/L}}). |
| {{key:sc50:NF}} / {{key:sc50:IP3}} / {{key:sc50:FDR}} / {{key:sc50:Pₙ}} / {{key:sc50:dBc}} | Receiver Noise & Dynamic Range | **Friis Cascaded Noise ({{key:sc50:NF}}), Cascaded IIP3, SFDR & Thermal Floor:** Solves `F = A + (B - 1) / G` ({{keycap:F}}, {{keycap:A}}, {{keycap:B}}, {{keycap:G}}), cascaded third-order intercept ({{key:sc50:IP3}}), spurious-free dynamic range ({{key:sc50:FDR}}), thermal noise floor $P_n = -174 + 10\log_{10}(B)$ ({{key:sc50:Pₙ}}), and oscillator phase noise ({{key:sc50:dBc}}). |
| {{key:sc50:f₀}} / {{key:sc50:XLC}} / {{key:sc50:PAD}} / {{key:sc50:fc}} / {{key:sc50:EIA}} | Resonance, Reactance & Filter Keys | **LC Tank ({{key:sc50:f₀}}), Reactance, Attenuator Pad & Cutoff:** Solves `F = 1 / (2π√(L×C))` ({{keycap:F}}, {{keycap:L}}, {{keycap:C}}), inductive/capacitive reactance ({{key:sc50:XLC}}), resistive $\pi$/$T$-pad resistors ({{key:sc50:PAD}}), RC/RL $-3\text{ dB}$ cutoff ({{key:sc50:fc}}), and EIA SMD codes ({{key:sc50:EIA}}). |
| {{key:sc50:C/B}} / {{key:sc50:RCS}} / {{key:sc50:Δf}} | Spectrum & Radar Solvers | **Shannon Capacity ({{key:sc50:C/B}}), Radar Range & Doppler Shift:** Solves `C = B × LN(1 + S) / LN(2)` ({{keycap:C}}, {{keycap:B}}, {{keycap:S}}), monostatic radar range/RCS ({{key:sc50:RCS}}), and two-way radar Doppler shift $\Delta f = 2 v f_0 / c$ ({{key:sc50:Δf}}). |
| {{key:sc50:Z₀}} / {{key:sc50:T₀}} / {{key:sc50:c}} / {{key:sc50:kB}} | RF Reference Constants | Recalls or configures characteristic system impedance $Z_0$ ($50\,\Omega$), IEEE reference noise temperature $T_0$ ($290\text{ K}$), speed of light $c$, and Boltzmann constant $k_B$. |

---

## Wet-Lab Chemistry, Stoichiometry, and Spectroscopy Keycaps

On the **SC-60** the Row 1 and Row 2 analytical chemistry keys and bidirectional Equation Workspaces evaluate formula molecular weights, gravimetric molarity, stock aliquot dilutions, Sørensen $\text{pH}$, Henderson–Hasselbalch buffer pairs, Beer–Lambert optical absorbance, chemical thermodynamics, and Nernstian electrochemistry:

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| {{key:sc60:Z}} / {{key:sc60:MW}} / {{key:sc60:w/w}} / {{key:sc60:ISO}} / {{key:sc60:ION}} | Atomic & Gravimetric Keys | **Element Lookup (`Z`), Molar Mass ({{key:sc60:MW}}) & Mass Fraction:** Recalls 118-element IUPAC atomic mass ({{key:sc60:Z}} with $X > 0$) or opens Formula Mode ({{key:sc60:Z}} with $X = 0$; softkeys {{keycap:ALP}}, {{keycap:NUM}}, {{keycap:FML}}), solves `W = N × M` ({{keycap:W}}, {{keycap:N}}, {{keycap:M}}), mass percent ({{key:sc60:w/w}}), isotope decay ({{key:sc60:ISO}}), and polyatomic ion ledger ({{key:sc60:ION}}). |
| {{key:sc60:C₁V₁}} / {{key:sc60:RXN}} / {{key:sc60:w/v}} | Row 2 Col 2 (Primary / Yellow / Blue) | **Dilution ({{key:sc60:C₁V₁}}), Stoichiometry ({{key:sc60:RXN}}) & Weight/Volume %:** Solves `C × V = D × U` ({{keycap:C}}, {{keycap:V}}, {{keycap:D}}, {{keycap:U}}), molar stoichiometry `N = C × V` ({{keycap:N}}, {{keycap:C}}, {{keycap:V}}), and $\%(\text{w/v})$ concentration ({{key:sc60:w/v}}). |
| {{key:sc60:εbc}} / {{key:sc60:%T}} | Row 2 Col 3 (Primary / Yellow) | **Beer–Lambert ({{key:sc60:εbc}}) & Optical Transmittance:** Solves `A = E × B × C` ({{keycap:A}}, {{keycap:E}}, {{keycap:B}}, {{keycap:C}}) and converts percent transmittance $\%T$ to absorbance $A = 2 - \log_{10}(\%T)$ ({{key:sc60:%T}}). |
| {{key:sc60:pH}} / {{key:sc60:EQV}} / {{key:sc60:PVT}} | Row 2 Col 4 (Primary / Yellow / Blue) | **Sørensen pH, Titration ({{key:sc60:EQV}}) & Ideal Gas Workspace ({{key:sc60:PVT}}):** Converts $[\text{H}^+]$ to $\text{pH} = -\log_{10}(X)$ ({{key:sc60:pH}}), solves titration equivalence `A × V = B × U`, and ideal gas law `P × V = N × 8.3145 × T` ({{keycap:P}}, {{keycap:V}}, {{keycap:N}}, {{keycap:T}}). |
| {{key:sc60:BUF}} / {{key:sc60:%Y}} / {{key:sc60:CAL}} | Row 2 Col 5 (Primary / Yellow / Blue) | **Henderson–Hasselbalch Buffer ({{key:sc60:BUF}}), Yield & Calorimetry ({{key:sc60:CAL}}):** Solves buffer `P = K + LOG(A / H)` ({{keycap:P}}, {{keycap:K}}, {{keycap:A}}, {{keycap:H}}), percent yield ({{key:sc60:%Y}}), and heat transfer `Q = M × C × T` ({{keycap:Q}}, {{keycap:M}}, {{keycap:C}}, {{keycap:T}}). |
| {{key:sc60:RCF}} / {{key:sc60:%}} / {{key:sc60:Δ%}} / {{key:sc60:▸M}} | Row 5 Col 2 Yellow & Row 7 Col 3 | **Centrifuge RCF, Percent & Molarity:** Evaluates centrifugal acceleration $\text{RCF} = 1.118 \times 10^{-5} r\,\text{RPM}^2$ ({{key:sc60:RCF}}), percentages ({{key:sc60:%}}, {{key:sc60:Δ%}}), and molar concentration conversions ({{key:sc60:▸M}}). |
| {{key:sc60:Kₑq}} / {{key:sc60:Eₐ}} / {{key:sc60:ΔG}} / {{key:sc60:E°}} / {{key:sc60:t½}} | Row 1 Col 1 Blue & Kinetics/Thermo Keys | **Arrhenius Kinetics Workspace ({{key:sc60:Eₐ}}), Equilibrium & Electrochemistry:** Solves `K = A × EXP(-E / (R × T))` ({{keycap:K}}, {{keycap:A}}, {{keycap:E}}, {{keycap:T}}), equilibrium constant ({{key:sc60:Kₑq}}), Gibbs free energy `G = H - T × S` ({{key:sc60:ΔG}}), standard potential `E = S - (0.05916/N)LOG(Q)` ({{key:sc60:E°}}), and half-life ({{key:sc60:t½}}). |
| {{key:sc60:R}} / {{key:sc60:h}} / {{key:sc60:F}} / {{key:sc60:Nₐ}} / {{key:sc60:kB}} / {{key:sc60:c}} | Fundamental Physical Constants | Recalls CODATA molar gas constant $R$, Planck constant $h$, Faraday constant $F$, Avogadro constant $N_A$, Boltzmann constant $k_B$, and speed of light $c$. |

---

## Commercial Bakery, Fermentation Science, and Brewing Keycaps

On the **SC-78** the Row 1 bakery and culinary yield keys and Row 2 brewing and enology keys pair with bidirectional Equation Workspaces to anchor batch scaling to total flour mass, compute mix water and flake-ice mass from friction and ambient heat, evaluate brewing gravity attenuation, strike water temperature, and hop bitterness, and audit butcher trim yields and menu food cost:

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| {{key:sc78:BK%}} / {{key:sc78:HYD}} / {{key:sc78:SCL}} / {{key:sc78:PAN}} | Baker's Percentage & Scaling Keys | **Baker's % ({{key:sc78:BK%}}), Hydration, Batch Scale & Pan Scaling:** Consumes flour mass ($Y$) and ingredient mass ($X$) or opens `P = (I / F) × 100` ({{keycap:P}}, {{keycap:I}}, {{keycap:F}}), computes dough hydration % ({{key:sc78:HYD}}), scales ingredient weights ({{key:sc78:SCL}}), and scales across pan volumes ({{key:sc78:PAN}}). |
| {{key:sc78:LEV}} / {{key:sc78:PRF}} / {{key:sc78:LV%}} | Row 1 Col 1 (Primary / Yellow / Blue) | **Sourdough Starter ({{key:sc78:LEV}}), Proofing Time & inoculation ({{key:sc78:LV%}}):** Splits levain build mass into flour/water components ({{key:sc78:LEV}}), adjusts fermentation proof time for ambient temperature $Q_{10}$ ({{key:sc78:PRF}}), and computes pre-ferment inoculation % ({{key:sc78:LV%}}). |
| {{key:sc78:Tw}} / {{key:sc78:ΣW}} / {{key:sc78:DIV}} / {{key:sc78:ICE}} | Row 1 Cols 3–4 (Primary / Yellow / Blue) | **Desired Dough Temp ({{key:sc78:Tw}}), Total Weight, Portion Divide & Flake Ice:** Solves `W = 3 × D - R - F - M` ({{keycap:W}}, {{keycap:D}}, {{keycap:R}}, {{keycap:F}}, {{keycap:M}}), computes total dough mass from flour and total baker's % ({{key:sc78:ΣW}}), divides batch into equal loaves ({{key:sc78:DIV}}), and computes flake-ice replacement mass ({{key:sc78:ICE}}). |
| {{key:sc78:ABV}} / {{key:sc78:CHP}} / {{key:sc78:SRM}} / {{key:sc78:BRX}} / {{key:sc78:SGT}} | Gravity, Alcohol & Color Keys | **Alcohol by Volume ({{key:sc78:ABV}}), Chaptalization, Morey SRM & Hydrometer:** Solves `A = (O - F) × 131.25` ({{keycap:A}}, {{keycap:O}}, {{keycap:F}}), sugar addition ({{key:sc78:CHP}}), beer color $\text{SRM} = 1.4922 \cdot \text{MCU}^{0.6859}$ ({{key:sc78:SRM}}), alcohol-corrected refractometer FG ({{key:sc78:BRX}}), and hydrometer temperature correction ({{key:sc78:SGT}}). |
| {{key:sc78:MSH}} / {{key:sc78:SPG}} / {{key:sc78:PU}} | Row 2 Col 4 (Primary / Yellow / Blue) | **Mash Strike ({{key:sc78:MSH}}), Sparge Volume & Pasteurization ({{key:sc78:PU}}):** Solves `S = (0.2 / R) × (T - G) + T` ({{keycap:S}}, {{keycap:R}}, {{keycap:T}}, {{keycap:G}}), boil/sparge volume ({{key:sc78:SPG}}), and thermal pasteurization units ({{key:sc78:PU}}). |
| {{key:sc78:IBU}} / {{key:sc78:CO₂}} / {{key:sc78:PRC}} | Row 2 Col 5 (Primary / Yellow / Blue) | **Hop Bitterness ({{key:sc78:IBU}}), Carbonation & Menu Price ({{key:sc78:PRC}}):** Solves `I = W × A × U × 74.89 / V` ({{keycap:I}}, {{keycap:W}}, {{keycap:A}}, {{keycap:U}}, {{keycap:V}}), keg head pressure ({{key:sc78:CO₂}}), and menu pricing from cost % ({{key:sc78:PRC}}). |
| {{key:sc78:C₁V₁}} / {{key:sc78:TA}} / {{key:sc78:WTR}} / {{key:sc78:SO₂}} / {{key:sc78:ACD}} | Enology, Acid & Water Keys | Solves Pearson dilution `C × V = D × U` ({{key:sc78:C₁V₁}}), titratable acidity ({{key:sc78:TA}}), brewing salt ppm ({{key:sc78:WTR}}), potassium metabisulfite dosage ({{key:sc78:SO₂}}), and acid blend adjustment ({{key:sc78:ACD}}). |
| {{key:sc78:YLD}} / {{key:sc78:MAC}} / {{key:sc78:CST}} / {{key:sc78:%}} / {{key:sc78:Δ%}} / {{key:sc78:a:b}} | Row 1 Col 5 & Row 7 Col 3 | **Butcher Yield ({{key:sc78:YLD}}), Plate Costing ({{key:sc78:CST}}) & Ratios:** Computes edible yield $\text{EP}/\text{AP}\times 100$ ({{key:sc78:YLD}}), Atwater caloric macros ({{key:sc78:MAC}}), solves `P = C / (F / 100)` ({{keycap:P}}, {{keycap:C}}, {{keycap:F}}), percentages, and baker's hydration ratios ({{key:sc78:a:b}}). |
| {{key:sc78:▸Brx}} / {{key:sc78:▸SG}} / {{key:sc78:▸°P}} / {{key:sc78:▸PRF}} / {{key:sc78:TDS}} / {{key:sc78:DTR}} / {{key:sc78:SAL}} / {{key:sc78:SV}} / {{key:sc78:SYR}} / {{key:sc78:Aw}} | Culinary R&D & Sugar Scale Keys | Converts between Brix, Specific Gravity, Plato, and US Proof; evaluates coffee extraction yield ({{key:sc78:TDS}}) and roast development time ratio ({{key:sc78:DTR}}), equilibrium brine salinity ({{key:sc78:SAL}}), sous-vide thermal diffusion ({{key:sc78:SV}}), syrup Brix ({{key:sc78:SYR}}), and water activity ({{key:sc78:Aw}}). |

---

## Clinical Nursing, Hospital Pharmacy, and Infusions Keycaps

On the **SC-80** the Row 1 and Row 2 clinical dosing, clearance, and pharmacy compounding keys pair with the Patient Profile softkey bar ({{keycap:PAT}}: {{keycap:W}}, {{keycap:H}}, {{keycap:A}}, {{keycap:S}}, {{keycap:MALE}}/{{keycap:FEM}}) to evaluate Mosteller body surface area, Devine ideal and adjusted dosing weights, Cockcroft–Gault renal clearance, pediatric maintenance rules, vasoactive pump and gravity drip rates, and one-compartment pharmacokinetics:

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| {{key:sc80:BSA}} / {{key:sc80:IBW}} / {{key:sc80:ABW}} / {{key:sc80:BMI}} | Anthropometric & Dosing Weight Keys | **Mosteller BSA ({{key:sc80:BSA}}), Ideal/Adjusted Weight & BMI:** Consumes height in $\text{cm}$ ($Y$) and weight in $\text{kg}$ ($X$) or solves `B = √(H × W / 3600)` ({{keycap:B}}, {{keycap:H}}, {{keycap:W}}, {{keycap:PAT}}), Devine ideal body weight ({{key:sc80:IBW}}), $40\%$ obese-adjusted dosing weight ({{key:sc80:ABW}}), and Quetelet BMI ({{key:sc80:BMI}}). |
| {{key:sc80:GFR}} / {{keycap:PAT}} | Row 1 Col 2 & Patient Softkey | **Cockcroft–Gault Renal Clearance ({{key:sc80:GFR}}):** Solves `C = ((140 - A) × W) / (72 × S)` ({{keycap:C}}, {{keycap:A}}, {{keycap:W}}, {{keycap:S}}, {{keycap:PAT}}), automatically applying the $\times 0.85$ female sex factor when {{keycap:FEM}} is active in the {{keycap:PAT}} profile. |
| {{key:sc80:DRP}} / {{key:sc80:IV}} / {{key:sc80:gtt}} / {{key:sc80:DOS}} / {{key:sc80:MGH}} | Critical-Care Infusion & Titration Keys | **Vasoactive Drip ({{key:sc80:DRP}}), Volumetric Pump ({{key:sc80:IV}}), Gravity (gtt) & Weight Dose ({{key:sc80:DOS}}):** Solves `R = D × W × 60 / C` ({{keycap:R}}, {{keycap:D}}, {{keycap:W}}, {{keycap:C}}, {{keycap:PAT}}), pump rate `R = V / T` ({{keycap:R}}, {{keycap:V}}, {{keycap:T}}), gravity roller clamp rate $R \times F_{\text{drop}} / 60$ ({{key:sc80:gtt}}), weight-based dose `T = W × D` ({{keycap:T}}, {{keycap:W}}, {{keycap:D}}, {{keycap:PAT}}), and $\text{mg/hr}$ mass rate ({{key:sc80:MGH}}). |
| {{key:sc80:Rx}} / {{key:sc80:ALG}} / {{key:sc80:IST}} / {{key:sc80:VIL}} / {{key:sc80:TPN}} / {{key:sc80:GIR}} | Pharmacy Compounding & Nutrition Keys | Evaluates tablets/volume per dose ({{key:sc80:Rx}}), two-stock alligation alternate ratio ({{key:sc80:ALG}}), sodium chloride isotonicity equivalent ({{key:sc80:IST}}), powder vial reconstitution volume ({{key:sc80:VIL}}), parenteral nutrition non-protein kcal ({{key:sc80:TPN}}), and neonatal glucose infusion rate ({{key:sc80:GIR}}). |
| {{key:sc80:PED}} / {{key:sc80:421}} / {{key:sc80:REE}} / {{key:sc80:VET}} | Pediatric, Metabolic & Veterinary Keys | Computes Clark/Young pediatric dose ({{key:sc80:PED}}), Holliday–Segar 4-2-1 hourly maintenance fluid rate ({{key:sc80:421}}), Mifflin–St Jeor resting energy expenditure ({{key:sc80:REE}}), and Kleiber allometric veterinary metabolic energy $70 \cdot W_{\text{kg}}^{0.75}$ ({{key:sc80:VET}}). |
| {{key:sc80:PK}} / {{key:sc80:EBM}} / {{key:sc80:NNT}} / {{key:sc80:OR}} | Pharmacokinetics & Biostatistics Keys | **One-Compartment Elimination ({{key:sc80:PK}}) & Clinical Epidemiology:** Converts between $k_e$ and $t_{1/2} = \ln(2)/k_e$ on the stack or solves `T = 0.693 × V / C` ({{keycap:T}}, {{keycap:V}}, {{keycap:C}}), and evaluates specificity/NPV ({{key:sc80:EBM}}), number needed to treat ({{key:sc80:NNT}}), and odds ratio ({{key:sc80:OR}}). |
| {{key:sc80:AG}} / {{key:sc80:Ca²⁺}} / {{key:sc80:Na⁺}} / {{key:sc80:OSM}} | Serum Electrolyte & Osmolality Keys | Evaluates serum anion gap $\text{AG} = \text{Na}^+ - (\text{Cl}^- + \text{HCO}_3^-)$ ({{key:sc80:AG}}), Payne albumin-corrected calcium ({{key:sc80:Ca²⁺}}), Katz hyperglycemia-corrected sodium ({{key:sc80:Na⁺}}), and calculated serum osmolality ({{key:sc80:OSM}}). |
| {{key:sc80:ICU}} / {{key:sc80:MAP}} / {{key:sc80:BRN}} / {{key:sc80:ABG}} / {{key:sc80:QTc}} / {{key:sc80:O₂}} | Hemodynamics, Burn & Emergency Keys | **Cardiac Output ({{key:sc80:ICU}}), MAP, Parkland Burn ({{key:sc80:BRN}}) & Respiratory Keys:** Solves `Q = H × S / 1000` ({{keycap:Q}}, {{keycap:H}}, {{keycap:S}}), mean arterial pressure $\text{DBP} + (\text{SBP}-\text{DBP})/3$ ({{key:sc80:MAP}}), Parkland burn fluid `V = 4 × W × B` ({{keycap:V}}, {{keycap:W}}, {{keycap:B}}), Berlin ARDS $P_a\text{O}_2/F_i\text{O}_2$ ratio ({{key:sc80:ABG}}), Bazett $\text{QTc}$ ({{key:sc80:QTc}}), and oxygen cylinder duration ({{key:sc80:O₂}}). |

---

## Quantitative Finance, Actuarial Science, and Six Sigma Keycaps

On the **SC-95** the Row 1 Time Value of Money workspace key ({{key:sc95:TVM}}), Row 1 and Row 2 R-style probability distribution keys, and shifted financial and statistical solvers combine five-variable compound interest, discounted cash-flow and bond valuation, unit-economic accounting, and Six Sigma statistical inference:

| Keycap / Softkey | Layer | Operation & Stack Signature |
| :--- | :--- | :--- |
| {{key:sc95:TVM}} $\to$ {{keycap:N}} {{keycap:I%}} {{keycap:PV}} {{keycap:PMT}} {{keycap:FV}} {{keycap:END}}/{{keycap:BEG}} | Row 1 Col 2 Primary & Softkeys | **Five-Variable TVM Workspace:** Pressing {{key:sc95:TVM}} binds softkeys to {{keycap:N}}, {{keycap:I%}}, {{keycap:PV}}, {{keycap:PMT}}, {{keycap:FV}}, and payment timing {{keycap:END}}/{{keycap:BEG}}; keying `<VALUE>` `<SOFTKEY>` stores a parameter (with `0` binding $0.0000$), {{key:f}} `<SOFTKEY>` unbinds, and {{key:sc95:SOLVE}} `<SOFTKEY>` (or {{key:XEQ}} `<SOFTKEY>`) solves for the unknown. |
| {{key:sc95:AMR}} / {{key:sc95:CF}} / {{key:sc95:EAR}} | Row 1 Col 2 (Yel/Blu) & Row 6 Col 1 Yel | **Loan Amortization, Cash Flows ({{key:sc95:CF}}) & Effective Rate ({{key:sc95:EAR}}):** Computes principal/interest reduction ({{key:sc95:AMR}}), opens discounted cash flows ({{key:sc95:CF}}), or solves `E = ((1 + A / (100 × M))^M - 1) × 100` ({{keycap:E}}, {{keycap:A}}, {{keycap:M}}) via {{key:sc95:EAR}}. |
| {{key:sc95:ROI}} / {{key:sc95:CGR}} / {{key:sc95:WAC}} / {{key:sc95:CAP}} | Capital Budgeting & Return Keys | Return on investment ({{key:sc95:ROI}}), compound annual growth `F = P × (1 + R/100)^N` ({{key:sc95:CGR}}: {{keycap:F}}, {{keycap:P}}, {{keycap:R}}, {{keycap:N}}), WACC ({{key:sc95:WAC}}), and perpetuity capitalization ({{key:sc95:CAP}}). |
| {{key:sc95:MGN}} / {{key:sc95:MKP}} / {{key:sc95:BEP}} / {{key:sc95:EOQ}} / {{key:sc95:DEP}} / {{key:sc95:TAX}} / {{key:sc95:%Σ}} | Commercial & CPA Accounting Keys | Solves gross margin `M = (P - C) / P × 100` ({{key:sc95:MGN}}: {{keycap:M}}, {{keycap:P}}, {{keycap:C}}), markup `U = (P - C) / C × 100` ({{key:sc95:MKP}}: {{keycap:U}}, {{keycap:P}}, {{keycap:C}}), break-even units `Q = F / (P - V)` ({{key:sc95:BEP}}: {{keycap:Q}}, {{keycap:F}}, {{keycap:P}}, {{keycap:V}}), Wilson `Q = √(2×D×S/H)` ({{key:sc95:EOQ}}: {{keycap:Q}}, {{keycap:D}}, {{keycap:S}}, {{keycap:H}}), straight-line depreciation `D = (C - S) / L` ({{key:sc95:DEP}}: {{keycap:D}}, {{keycap:C}}, {{keycap:S}}, {{keycap:L}}), sales tax `T = P × (1 + R/100)` ({{key:sc95:TAX}}: {{keycap:T}}, {{keycap:P}}, {{keycap:R}}), and share of total ({{key:sc95:%Σ}}). |
| {{key:sc95:BND}} (Bond Valuation) | Row 2 Col 1 Blue Shift | **Fixed-Income Bond Workspace ({{key:sc95:BND}}):** Solves `P = C × (1 - (1 + Y/100)^-N) / (Y/100) + F / (1 + Y/100)^N` forward for clean price {{keycap:P}} or backward for periodic yield to maturity {{keycap:Y}}, coupon {{keycap:C}}, remaining periods {{keycap:N}}, or par redemption {{keycap:F}}. |
| {{key:sc95:pN}} / {{key:sc95:qN}} / {{key:sc95:rN}} / {{key:sc95:pt}} / {{key:sc95:qt}} / {{key:sc95:rt}} / {{key:sc95:pχ²}} / {{key:sc95:qχ²}} / {{key:sc95:rχ²}} / {{key:sc95:pF}} / {{key:sc95:qF}} / {{key:sc95:rF}} / {{key:sc95:pB}} / {{key:sc95:qB}} / {{key:sc95:rB}} / {{key:sc95:PDF}} | Row 1 Col 3 & Row 2 Cols 2–5 | **R-Style CDF (`p*`), Inverse Quantile (`q*`), Random Variate (`r*`) & Density (PDF):** Evaluates cumulative probabilities (blue shift), critical quantiles (yellow shift), and random variates (unshifted primary) for Binomial ({{key:sc95:pB}}/{{key:sc95:qB}}/{{key:sc95:rB}}), Normal ({{key:sc95:pN}}/{{key:sc95:qN}}/{{key:sc95:rN}}), Student's $t$ ({{key:sc95:pt}}/{{key:sc95:qt}}/{{key:sc95:rt}}), Chi-square ({{key:sc95:pχ²}}/{{key:sc95:qχ²}}/{{key:sc95:rχ²}}), and Fisher $F$ ({{key:sc95:pF}}/{{key:sc95:qF}}/{{key:sc95:rF}}) distributions, or prefixes with {{key:sc95:PDF}} for point density/mass. |
| {{key:sc95:Σ+}} / {{key:sc95:Σ-}} / {{key:sc95:x̄,ȳ}} / {{key:sc95:MED}} / {{key:sc95:s,σ}} / {{key:sc95:L.R.}} | Summary Statistics & Regression Keys | Accumulates/removes $(x_i, y_i)$ pairs ({{key:sc95:Σ+}}, {{key:sc95:Σ-}}), computes sample means ({{key:sc95:x̄,ȳ}}), median/IQR ({{key:sc95:MED}}), sample/population standard deviations ({{key:sc95:s,σ}}), and opens the least-squares regression menu ({{key:sc95:L.R.}} $\to$ {{keycap:ŷ}}, {{keycap:x̂}}, {{keycap:m}}, {{keycap:b}}, {{keycap:r}}). |
| {{key:sc95:Cpk}} / {{key:sc95:SPC}} / {{key:sc95:CI}} / {{key:sc95:z₀}} / {{key:sc95:t₂}} / {{key:sc95:A/B}} / {{key:sc95:n*}} / {{key:sc95:P&#124;B}} / {{key:sc95:β}} | Six Sigma, Inference & Bayesian Solvers | Solves process capability `C = (U - L) / (6 × S)` ({{key:sc95:Cpk}}: {{keycap:C}}, {{keycap:U}}, {{keycap:L}}, {{keycap:S}}), $3\sigma$ Shewhart control limits ({{key:sc95:SPC}}), confidence margin `E = Z × S / √N` ({{key:sc95:CI}}: {{keycap:E}}, {{keycap:Z}}, {{keycap:S}}, {{keycap:N}}), one-sample $z$-test ({{key:sc95:z₀}}), two-sample $t$-test ({{key:sc95:t₂}}), two-proportion test ({{key:sc95:A/B}}), sample size `N = (Z × S / E)²` ({{key:sc95:n*}}: {{keycap:N}}, {{keycap:Z}}, {{keycap:S}}, {{keycap:E}}), Bayes posterior ({{key:sc95:P&#124;B}}), and three-point Beta-PERT mean `E = (O + 4×M + P) / 6` ({{key:sc95:β}}: {{keycap:E}}, {{keycap:O}}, {{keycap:M}}, {{keycap:P}}). |
| {{key:sc95:%}} / {{key:sc95:Δ%}} / {{key:sc95:%Σ}} | Row 7 Col 3 (Primary / Yellow / Blue) | **Percentage Functions:** Standard percentage ({{key:sc95:%}}), percent change $\Delta\%$ ({{key:sc95:Δ%}}), and percent of total $\%T$ ({{key:sc95:%Σ}}). |
| {{key:sc95:▸YR}} / {{key:sc95:▸YMD}} / {{key:sc95:DT+}} / {{key:sc95:ΔD}} | Row 5 Cols 1–2 Shifted Keys | **Calendar & Day-Count Keys:** Converts day counts to annualized years ({{key:sc95:▸YR}}), toggles ISO `YYYY.MMDD` format ({{key:sc95:▸YMD}}), projects calendar maturity dates ({{key:sc95:DT+}}), and evaluates exact calendar days between dates ({{key:sc95:ΔD}}). |
