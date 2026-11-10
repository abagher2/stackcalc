---
title: "Appendix A: Cross-Domain Formula & Equation Compendium"
description: "Governing equations, physical constants, and stack argument conventions across the nine StackCalc domain calculators (SC-35 through SC-95)."
---

# Appendix A: Cross-Domain Formula & Equation Compendium

This compendium consolidates the governing mathematical identities, physical constants, four-register RPN stack conventions, and bidirectional Equation Solver Workspace schemas across all nine specialized instruments in the StackCalc Domain Series (`SC-35`, `SC-14`, `SC-16`, `SC-24`, `SC-50`, `SC-60`, `SC-78`, `SC-80`, and `SC-95`). Each section summarizes governing equations across the domain calculators so engineers, navigators, clinicians, and analysts can verify input dimensions, immediate stack arguments, and closed-form or numerical solver relationships at a glance.

## Universal Three-Pillar Stack, Precision, and Bidirectional Solver Conventions

Every instrument in the StackCalc Domain Series provides IEEE 754 double-precision floating-point arithmetic ($64\text{-bit}$ word, $53\text{-bit}$ binary significand, providing $15$ to $17$ significant decimal digits) and selectable fixed-width integer arithmetic on the `SC-16`:

1. **Configurable RPN Stack Depth ({{keycap:4-LV}}, {{keycap:8-LV}}, or {{keycap:INF}} via {{key:sc35:FLAGS}}):** Practitioners can operate with a classic four-register $(X, Y, Z, T)$ operational stack ({{keycap:4-LV}}), expand to an eight-register stack ({{keycap:8-LV}}), or enable unbounded stack capacity ({{keycap:INF}}) for multi-branch field derivations. Across all stack configurations, the active four-register window at the bottom of the stack (`Register T`, `Register Z`, `Register Y`, `Register X`) obeys deterministic RPN lift and drop semantics:

| Register | Operational Role | Behavior on Binary Operation ({{key:+}}, {{key:-}}, {{key:×}}, {{key:÷}}, {{key:yˣ}}) | Behavior on {{key:ENTER}} |
| :--- | :--- | :--- | :--- |
| **Register $T$** | Top / 4th Visible Level | Replicates downward into $Z$ ($T' = T$) in {{keycap:4-LV}} mode (or drops from `R5` in {{keycap:8-LV}}/{{keycap:INF}}) | Receives prior $Z$ ($T' = Z$) |
| **Register $Z$** | 3rd Stack Level | Drops into $Y$ ($Z' = T$) | Receives prior $Y$ ($Z' = Y$) |
| **Register $Y$** | 2nd Operand Level | Consumed as left operand ($Y \circ X$); receives prior $Z$ | Replicates $X$ ($Y' = X$) |
| **Register $X$** | Active Display Line | Consumed as right operand; receives result $f(Y, X)$ | Remains in $X$ (lift disabled for next digit) |

2. **Dual-Mode Domain Keys (Immediate RPN Stack Shortcuts + Bidirectional Equation Solver Workspaces):**
   - **Immediate Stack Mode:** Pressing a domain key when arguments are staged in Registers $Z$, $Y$, and $X$ evaluates the forward physical transformation in a single keystroke while automatically injecting embedded physical constants ({{key:sc50:c}}, {{key:sc50:kB}}, {{key:sc60:R}}, {{key:sc60:F}}, {{key:sc35:g₀}}, {{key:sc14:ρw}}) and regulatory lookup tables (NEC Table 8 wire gauges, IUPAC atomic masses).
   - **Bidirectional Equation Solver Workspace ({{key:sc35:SOLVE}} / {{key:XEQ}} + Workspace Softkeys):** Opening a domain key's Equation Workspace renders the governing equation across Line 1 of the LCD and binds the top-row softkeys to its symbolic variables. Storing known values in any order and pressing {{key:sc35:SOLVE}} (or {{key:XEQ}}) followed by the target variable softkey solves the governing law **forward or backward for any unknown parameter** via exact algebraic isolation or Secant–Brent numerical root-finding.
   - **Zero-Value Parameter Binding & Shift-Softkey Unsetting:** Entering `0` into a variable softkey explicitly binds $0.0000$ to that parameter (indicated by `*` or `•`), enabling physical boundary conditions such as $FV = 0$ for fully paid loan amortizations or zero datum elevation. To unbind a variable (freeing it to be solved for as the unknown target), pressing Yellow Shift followed by the variable softkey ({{key:f}} `<SOFTKEY>`) unsets the parameter immediately across all Equation, TVM, and Polynomial workspaces.
3. **Domain Modes, Native Input Parsers, and Live Reference Ledgers ({{key:sc35:▦}}):** Native domain entry modes ({{key:sc35:▸HMS}} via {{key:sc35:▸HR}}/{{key:sc35:▸HMS}}, {{key:sc14:f-i}} via {{key:sc14:f-i}}, {{key:sc16:HEX}}/{{key:sc16:DEC}}/{{key:sc16:OCT}}/{{key:sc16:BIN}} + {{key:sc16:WSZ}} + {{key:sc16:NEG}}, {{key:sc24:TC}} + {{key:sc24:FPS}}, chemical formula entry via {{key:sc60:Z}}) and the non-destructive Reference Table ({{key:sc35:▦}}) maintain live domain ledgers (`@COGO`, `@BK%`, `@PAT`/`@MAR`, and bivariate statistical accumulators).

### Cross-Domain Mathematical Isomorphisms

Across the nine physical trades, identical mathematical structures recur under domain-specific physical variables:

| Mathematical Structure | Governing Law Form | Domain Instantiations Across Units I–IX |
| :--- | :--- | :--- |
| **First-Order Exponential Decay & Discounting** | $y(t) = y_0 \, e^{-\lambda t}$ | **Unit III (`SC-16`):** RC settling $v_C(t) = V_{\text{in}}(1 - e^{-t/\tau})$ ({{key:sc16:τ}}, {{key:sc16:PWM}}, {{key:sc16:BPS}}) • **Unit VI (`SC-60`):** Beer–Lambert transmittance $I/I_0 = 10^{-\varepsilon \ell c}$ ({{key:sc60:εbc}}, {{key:sc60:C₁V₁}}) & Arrhenius kinetics $k = A e^{-E_a/(RT)}$ ({{key:sc60:Eₐ}}, {{key:sc60:t½}}, {{key:sc60:Kₑq}}, {{key:sc60:ΔG}}, {{key:sc60:E°}}) • **Unit VIII (`SC-80`):** One-compartment drug elimination $C(t) = C_0 e^{-k_e t}$ ({{key:sc80:PK}}, {{key:sc80:GFR}}, {{key:sc80:BSA}}, {{key:sc80:IBW}}, {{key:sc80:ABW}}, {{key:sc80:DOS}}, {{key:sc80:DRP}}, {{key:sc80:IV}}) • **Unit IX (`SC-95`):** Multi-period and continuous discounting ({{key:sc95:TVM}}, {{key:sc95:AMR}}, {{key:sc95:CF}}, {{key:sc95:BND}}, {{key:sc95:EAR}}, {{key:sc95:CGR}}, {{key:sc95:ROI}}, {{key:sc95:pN}}, {{key:sc95:qN}}) |
| **Logarithmic Ratio Compression** | $L = \kappa \log_{10}(X / X_{\text{ref}})$ | **Unit IV (`SC-24`):** Acoustic sound pressure level $\text{SPL} = 20\log_{10}(p/p_0)$ ({{key:sc24:SPL}}, {{key:sc24:dB}}, {{key:sc24:EV}}, {{key:sc24:DOF}}, {{key:sc24:FOV}}, {{key:sc24:FOV}}, {{key:sc24:TC}}, {{key:sc24:+TC}}, {{key:sc24:-TC}}, {{key:sc24:FPS}}) • **Unit V (`SC-50`):** RF power ({{key:sc50:dBm}}, {{key:sc50:▸dBm}}), Friis path loss ({{key:sc50:FSL}}, {{key:sc50:LNK}}, {{key:sc50:F₁}}), and noise cascade ({{key:sc50:NF}}, {{key:sc50:Pₙ}}, {{key:sc50:IP3}}, {{key:sc50:FDR}}) • **Unit VI (`SC-60`):** Sørensen acidity $\text{pH} = -\log_{10}[\text{H}^+]$ ({{key:sc60:pH}}, {{key:sc60:pKₐ}}, {{key:sc60:BUF}}, {{key:sc60:EQV}}, {{key:sc60:MW}}, {{key:sc60:w/w}}, {{key:sc60:PVT}}, {{key:sc60:RCF}}) |
| **Shannon Information & Quantization Capacity** | $C = B \log_2(1 + \text{SNR})$ | **Unit III (`SC-16`):** $N$-bit ADC dynamic range ({{key:sc16:ADC}}, {{key:sc16:DAC}}, {{key:sc16:CRC}}, {{key:sc16:NET}}, {{key:sc16:FLT}}, {{key:sc16:END}}, {{key:sc16:#B}}, {{key:sc16:CLZ}}, {{key:sc16:MSK}}, {{key:sc16:SB}}, {{key:sc16:CB}}, {{key:sc16:B?}}) • **Unit V (`SC-50`):** Shannon–Hartley channel capacity ({{key:sc50:C/B}}, {{key:sc50:Δf}}, {{key:sc50:RCS}}, {{key:sc50:f₀}}, {{key:sc50:λ/L}}) |
| **Euclidean & Stoichiometric Decomposition** | $r = \sqrt{x^2 + y^2}$ | **Unit I (`SC-35`):** Survey inverse ({{key:sc35:INV}}, {{key:sc35:TRV}}, {{key:sc35:BRG}}, {{key:sc35:SLP}}, {{key:sc35:GR%}}, {{key:sc35:CUT}}, {{key:sc35:△}}, {{key:sc35:FLW}}) & wind triangle ({{key:sc35:WND}}, {{key:sc35:XWC}}, {{key:sc35:ALT}}, {{key:sc35:TSD}}) • **Unit II (`SC-14`):** Conduit & rafter geometry ({{key:sc14:OFS}}, {{key:sc14:MIT}}, {{key:sc14:FIT}}, {{key:sc14:BC}}, {{key:sc14:SFM}}, {{key:sc14:TAP}}), three-phase power ({{key:sc14:PF}}, {{key:sc14:AWG}}, {{key:sc14:FLA}}, {{key:sc14:MTR}}), and process hydraulics ({{key:sc14:PIP}}, {{key:sc14:Cᵥ}}, {{key:sc14:PMP}}, {{key:sc14:NPH}}, {{key:sc14:mA}}, {{key:sc14:RTD}}) • **Unit V (`SC-50`):** Complex impedance & VSWR ({{key:sc50:CMPLX}}, {{key:sc50:Z₀}}, {{key:sc50:Γ}}, {{key:sc50:SWR}}, {{key:sc50:RL}}, {{key:sc50:Z₀}}) • **Unit VII (`SC-78`):** Culinary & zymurgy scaling ({{key:sc78:BK%}}, {{key:sc78:ΣW}}, {{key:sc78:DIV}}, {{key:sc78:Tw}}, {{key:sc78:ICE}}, {{key:sc78:MSH}}, {{key:sc78:▸SG}}, {{key:sc78:ABV}}, {{key:sc78:IBU}}, {{key:sc78:SRM}}, {{key:sc78:TDS}}, {{key:sc78:YLD}}, {{key:sc78:CST}}, {{key:sc78:PRC}}, {{key:sc78:Aw}}, {{key:sc78:SO₂}}, {{key:sc78:CO₂}}) • **Unit IX (`SC-95`):** Unit economics & Six Sigma ({{key:sc95:MGN}}, {{key:sc95:MKP}}, {{key:sc95:BEP}}, {{key:sc95:EOQ}}, {{key:sc95:Cpk}}, {{key:sc95:SPC}}, {{key:sc95:CI}}, {{key:sc95:z₀}}, {{key:sc95:t₂}}, {{key:sc95:A/B}}, {{key:sc95:n*}}) |

---

---


## Unit I: Geomatics, Land Surveying, and Flight Navigation

The **SC-35** provides dedicated faceplate keys and bidirectional Equation Solver workspaces to execute the governing laws of this domain. Each equation is indexed below with its physical motivation, governing formula, and operational calculator softkeys.

### Eq. 1.1 — Sexagesimal Angular Polynomial

A sexagesimal angle read from a theodolite glass circle or historic deed plat consists of integer degrees $D^\circ$, integer arcminutes $M' \in [0, 59]$, and arcseconds $S'' \in [0, 60)$. Because one degree contains $60$ arcminutes and $60 \times 60 = 3{,}600$ arcseconds, converting between packed sexagesimal notation `DDD.MMSS` (where the first two digits after the decimal point store arcminutes MM and the next two store arcseconds SS, converted directly via {{key:sc35:▸DEG}} / {{key:sc35:▸HR}} and {{key:sc35:▸HMS}}) and decimal degrees $\theta_{\text{dec}}$ evaluates a base-$60$ polynomial:

$$\theta_{\text{dec}} = D + \frac{M}{60} + \frac{S}{3600}$$

In this expression, $D$ is the whole-degree component, $M$ is the arcminute count divided by $60\text{ min/deg}$, and $S$ is the arcsecond count divided by $3{,}600\text{ sec/deg}$. For a historic deed azimuth of $47^\circ 22' 30''$ (written in packed field notation as `47.2230`), dividing the $22$ arcminutes by $60$ yields $0.366667^\circ$, dividing the $30$ arcseconds by $3{,}600$ yields $0.008333^\circ$, and summing with $47^\circ$ via {{key:sc35:▸DEG}} produces $\theta_{\text{dec}} = \mathbf{47.375^\circ}$. Reversing the conversion via {{key:sc35:▸HMS}} on $47.375^\circ$ extracts the integer part $D = 47^\circ$, multiplies the fractional remainder $0.375 \times 60 = 22.5'$ to isolate $M = 22'$, and multiplies the remaining $0.5' \times 60 = 30''$ to recover `47.2230` ($47^\circ 22' 30''$).

* **Calculator Interface:** Primary Key: {{key:sc35:▸HR}} / {{key:sc35:▸HMS}} • Expression / Workspace: `Direct stack conversion` • Softkeys: {{keycap:▸HR}} {{keycap:▸HMS}}


---

### Eq. 1.2 — Ravine Slope Reduction

When the total station on the north rim of the Pine Barrens ravine sights a prism across an inclined **slope distance** $S$ at a vertical slope angle $\nu$ (measured above $+$ or below $-$ the horizontal horizon), legal property boundaries and map projections depend on the flat **horizontal ground distance** $D_H$ and the **vertical elevation difference** $\Delta V$ (operational shorthand {{key:sc35:SLP}}). In this right triangle, the slant laser range forms the hypotenuse; multiplying by the cosine projects the slope down onto the flat horizon, while multiplying by the sine projects the vertical elevation climb:

$$D_H = S \cos(\nu)$$

In this reduction, $S$ is the slant range in Register $Y$, $\nu$ is the vertical inclination angle in Register $X$, $D_H$ is the reduced horizontal distance placed into Register $X$, and $\Delta V$ is the vertical elevation difference placed into Register $Y$. Sighting across the cedar ravine over a slope distance of $S = 412.68\text{ ft}$ at a vertical angle of $\nu = 6^\circ 15' 00''$ (`6.15` in `DDD.MMSS`, or $6.25^\circ$ via {{key:sc35:▸DEG}}) projects a horizontal ground distance of $D_H = \mathbf{410.10\text{ ft}}$ in Register $X$ and a vertical elevation difference of $\Delta V = \mathbf{44.92\text{ ft}}$ in Register $Y$. Across regional surveys, field crews further scale horizontal ground distance to state-plane grid coordinates using the combined factor $k_{\text{comb}} = k_{\text{grid}} \times k_{\text{elev}}$, where elevation factor $k_{\text{elev}} = R_E / (R_E + H + N)$ accounts for mean Earth radius $R_E$, orthometric station elevation $H$, and geoid undulation $N$, linking GPS ellipsoidal heights ($h$) to gravity-based drainage elevation ($H = h - N$).

* **Calculator Interface:** Primary Key: {{key:sc35:SLP}} • Expression / Workspace: `Stack: S in Y, ν in X` • Softkeys: {{keycap:SLP}}


---

### Eq. 1.3 — Forward Coordinate Traverse Projection

In plane surveying, every boundary station is indexed by an ordered pair of orthogonal coordinates $(N, E)$, where **Northing** ($N$) measures distance north of a reference origin and **Easting** ($E$) measures distance east of the origin, while directions are measured as a full-circle **Azimuth** $\alpha \in [0^\circ, 360^\circ)$ clockwise from True North ($0^\circ$). Projecting a known horizontal ground distance $D_H$ along a known clockwise azimuth $\alpha$ from a starting station $A(N_A, E_A)$ to determine the North change ($\Delta N$, **Latitude**), the East change ($\Delta E$, **Departure**), and the target coordinates $B(N_B, E_B)$ constitutes the **Forward Coordinate Geometry Problem** ({{key:sc35:TRV}}). Because azimuth rotates clockwise from the vertical North axis, the trigonometric projections swap roles: cosine governs North-South displacement, while sine governs East-West displacement:

$$\Delta N = D_H \cos(\alpha)$$

The updated station coordinates follow directly by addition: $N_B = N_A + \Delta N$ and $E_B = E_A + \Delta E$. Because $\cos\alpha$ is positive in the northern quadrants ($270^\circ < \alpha < 90^\circ$) and negative in the southern quadrants ($90^\circ < \alpha < 270^\circ$), while $\sin\alpha$ is positive in the eastern quadrants ($0^\circ < \alpha < 180^\circ$) and negative in the western quadrants ($180^\circ < \alpha < 360^\circ$), these North-clockwise projection identities assign the correct algebraic signs in all four compass quadrants without manual lookup tables.

* **Calculator Interface:** Primary Key: {{key:sc35:TRV}} • Expression / Workspace: `Stack: α in Y, D in X` • Softkeys: {{keycap:TRV}}


---

### Eq. 1.4 — Inverse Coordinate Geometry

Running the Forward projection in reverse—starting from two known monument coordinates $(N_A, E_A)$ and $(N_B, E_B)$ and recovering the straight-line horizontal distance $D$ and clockwise North azimuth $\alpha \in [0^\circ, 360^\circ)$ between them—is the **Inverse Coordinate Geometry Problem** ({{key:sc35:INV}}). From the coordinate displacements $\Delta N = N_B - N_A$ and $\Delta E = E_B - E_A$, the Euclidean hypotenuse gives the ground distance $D$. To find the compass heading, the two-argument arctangent—or $\operatorname{atan2}$—asks what direction on the full circle produces that specific ratio of Easting departure to Northing latitude, resolving the quadrant automatically without sign ambiguity:

$$D = \sqrt{(\Delta N)^2 + (\Delta E)^2}$$

Whereas geodetic computations use $0^\circ\text{--}360^\circ$ clockwise azimuths, colonial and modern metes-and-bounds property deeds record directions as **Quadrant Bearings** ({{key:sc35:BRG}}). A quadrant bearing begins on either the **North (`N`)** or **South (`S`)** meridian and turns an acute angle $\theta \in [0^\circ, 90^\circ]$ toward either the **East (`E`)** or **West (`W`)**:

* **Calculator Interface:** Primary Key: {{key:sc35:INV}} • Expression / Workspace: `Stack: ΔN in Y, ΔE in X` • Softkeys: {{keycap:INV}} {{keycap:BRG}}


---

### Eq. 1.5 — Bowditch Compass Rule Closure

In an exact closed polygon of $n$ sides, the vector sum of all North latitudes $\Sigma_{\Delta N} = \sum_{i=1}^n \Delta N_i$ and the vector sum of all East departures $\Sigma_{\Delta E} = \sum_{i=1}^n \Delta E_i$ both equal zero. Because field measurements contain small random optical and atmospheric errors, the accumulated traverse returns to a coordinate slightly displaced from the POB. The hypotenuse of that residual gap is the **Linear Error of Closure** $E_c$ ({{key:sc35:CLS}}), and dividing total perimeter $P = \sum_{i=1}^n D_i$ by $E_c$ defines the **Relative Precision Ratio**. Once closure meets statutory standards, Nathaniel Bowditch's 1807 **Compass Rule** distributes the misclosure across each leg in proportion to its length fraction:

$$E_c = \sqrt{\left(\Sigma_{\Delta N}\right)^2 + \left(\Sigma_{\Delta E}\right)^2}$$

For a four-leg rectangular boundary loop of total perimeter $P = 3{,}200.00\text{ ft}$ whose field measurements return with net latitude misclosure $\Sigma_{\Delta N} = -0.12\text{ ft}$ and net departure misclosure $\Sigma_{\Delta E} = +0.16\text{ ft}$, the linear error of closure is $E_c = \sqrt{(-0.12)^2 + 0.16^2} = \mathbf{0.20\text{ ft}}$ ({{key:sc35:CLS}}), yielding a relative precision ratio of $1 : (3200 / 0.20) = \mathbf{1 : 16{,}000}$.

* **Calculator Interface:** Primary Key: {{key:sc35:CLS}} • Expression / Workspace: `Traverse ledger closure in {{key:sc35:▦}}` • Softkeys: {{keycap:CLS}} {{keycap:PT+}}


---

### Eq. 1.6 — Gauss Shoelace Parcel Area

The additive coordinate corrections for each leg $i$ are $\delta N_i = -\Sigma_{\Delta N}(D_i / P)$ and $\delta E_i = -\Sigma_{\Delta E}(D_i / P)$. From the sequential vertex coordinates $(N_1, E_1), (N_2, E_2), \dots, (N_n, E_n)$ of a closed simple polygon (with $(N_{n+1}, E_{n+1}) = (N_1, E_1)$), **Gauss's Shoelace Formula** crosses adjacent coordinates around the perimeter to evaluate the enclosed planar area $A$ (displayed live as {{key:sc35:△}} alongside {{key:sc35:CLS}} inside the `@COGO` reference table {{key:sc35:▦}}, while {{key:sc35:△}} evaluates right-triangle and sub-parcel areas), which converts to statutory acreage via {{key:sc35:▸ac}} ($43{,}560\text{ ft}^2/\text{acre}$) and metric hectares via {{key:sc35:▸ha}} ($10{,}000\text{ m}^2/\text{ha}$):

$$A = \frac{1}{2} \left\lvert \sum_{i=1}^{n} \left( E_i N_{i+1} - E_{i+1} N_i \right) \right\rvert$$

For a four-leg rectangular boundary loop of total perimeter $P = 3{,}200.00\text{ ft}$ (spanning $600.00\text{ ft}$ North-South by $1{,}000.00\text{ ft}$ East-West) whose field measurements return with net latitude misclosure $\Sigma_{\Delta N} = -0.12\text{ ft}$ and net departure misclosure $\Sigma_{\Delta E} = +0.16\text{ ft}$, the linear error of closure is $E_c = \sqrt{(-0.12)^2 + 0.16^2} = \mathbf{0.20\text{ ft}}$ ({{key:sc35:CLS}}), yielding a relative precision ratio of $1 : (3200 / 0.20) = \mathbf{1 : 16{,}000}$, and Gauss's shoelace sum across the adjusted corners in {{key:sc35:▦}} gives an enclosed area of $A = \mathbf{600{,}000\text{ ft}^2}$, or $600{,}000 / 43{,}560 \approx \mathbf{13.7741\text{ acres}}$ ($5.5742\text{ ha}$).

* **Calculator Interface:** Primary Key: {{key:sc35:△}} • Expression / Workspace: `Gauss Shoelace area in {{key:sc35:▦}}` • Softkeys: {{keycap:△}} {{keycap:▸ac}} {{keycap:▸ha}}


---

### Eq. 1.7 — Bearing-Bearing Coordinate Intersection

When sighting an inaccessible boundary mark or monument $P(N, E)$ from two known baseline control stations $A(N_1, E_1)$ and $B(N_2, E_2)$ along forward azimuths $\alpha_1$ and $\alpha_2$, the lines of sight define simultaneous linear vector equations. Equating coordinates and isolating the distance $d_1$ from Station 1 yields:

$$d_1 = \frac{(E_2 - E_1)\cos\alpha_2 - (N_2 - N_1)\sin\alpha_2}{\sin(\alpha_1 - \alpha_2)}$$

In terms of coordinate differences $\Delta N = N_2 - N_1$ and $\Delta E = E_2 - E_1$ and tangent slopes $T_1 = \tan\alpha_1$ and $T_2 = \tan\alpha_2$, the intersection Northing evaluates directly via the classic surveying formula:

$$N = \frac{N_1 T_2 - N_2 T_1 + \Delta E}{T_2 - T_1}$$

On the SC-35, staging azimuth $\alpha_1$ in Register $Y$ and $\alpha_2$ in Register $X$ before pressing {{key:sc35:ISC}} computes the intersection Northing $N$ into Register $X$ and Easting $E$ into Register $Y$ (with distance $d_1$ in Register $Z$). In the bidirectional Equation Solver Workspace ({{key:sc35:SOLVE}} {{key:sc35:ISC}}), the calculator displays `ISC: INTERSECT` with governing equation `N = (N1·T2 - N2·T1 + ΔE) / ΔT` and softkeys {{keycap:N}}, {{keycap:D}}, and {{keycap:A}}.

* **Calculator Interface:** Primary Key: {{key:sc35:ISC}} • Expression / Workspace: `ISC: N = (N1·T2 - N2·T1 + ΔE) / ΔT` • Softkeys: {{keycap:N}} {{keycap:D}} {{keycap:A}}


---

### Eq. 2.1 — Circular Curve Tangent and Arc Length

Bisecting the central angle $\Delta$ with the radial line from $O$ through the mid-arc apex to PI partitions the layout into two congruent right triangles of half-angle $\Delta / 2$. The tangent setback distance $T$ uses the half-angle tangent to measure how far back along the straight approach road the crew must begin curving, while the circular arc length $L$ scales the central deflection angle in radians by the radius to measure the actual curved centerline pavement:

$$T = R \tan\!\left(\frac{\Delta}{2}\right)$$

In these expressions, $R$ is the centerline radius of curvature in feet, $\Delta$ is the exterior deflection angle in decimal degrees, $T$ is the opposite leg of the right triangle of angle $\Delta / 2$ and adjacent side $R$, $L$ scales the radian measure $\Delta(\pi / 180^\circ)$ by $R$, and the straight-line long chord connecting PC directly to PT doubles the half-chord: $LC = 2 R \sin(\Delta / 2)$. For the Granite Gorge highway curve of radius $R = 1{,}200.00\text{ ft}$ in Register $Y$ and deflection angle $\Delta = 28.5^\circ$ in Register $X$ (half-angle $\Delta / 2 = 14.25^\circ$), pressing {{key:sc35:CRV}} yields the tangent setback distance $T = 1200\tan(14.25^\circ) = \mathbf{304.77\text{ ft}}$ in Register $Y$ and the centerline paving arc length $L = 1200 \times 28.5^\circ \times (\pi / 180^\circ) = \mathbf{596.90\text{ ft}}$ in Register $X$, while the straight-line long chord is $LC = 2400\sin(14.25^\circ) = \mathbf{590.80\text{ ft}}$.

* **Calculator Interface:** Primary Key: {{key:sc35:CRV}} • Expression / Workspace: `CRV: L = R × D × π / 180` • Softkeys: {{keycap:L}} {{keycap:R}} {{keycap:D}}


---

### Eq. 2.2 — Parabolic Vertical Curve Elevation

At the canyon crest, transitioning from an entry grade $g_1$ (in percent grade) at the Point of Vertical Curvature ($\text{PVC}$) to an exit grade $g_2$ over a vertical curve of length $L$ stations ({{key:sc35:VCV}}) traces a second-degree vertical parabola. Because a parabola has a constant second derivative, the rate of vertical curvature remains constant across the entire span, eliminating sudden vertical jolts for traveling vehicles. The elevation at any station $x$ combines the starting elevation, the initial slope, and a quadratic sag-or-crest curvature correction driven by the grade difference:

$$\text{Elev}(x) = \text{PVC} + g_1 x + \left(\frac{g_2 - g_1}{2 L}\right) x^2$$

For a vertical crest curve starting at elevation $\text{PVC} = 425.00\text{ ft}$ with entry grade $g_1 = +2.50\%$, exit grade $g_2 = -1.75\%$, and curve length $L = 8\text{ stations}$ ($800\text{ ft}$), the midpoint elevation at $x = L / 2 = 4\text{ stations}$ is $\text{Elev}(4) = 425.00 + 2.5(4) + \frac{-1.75 - 2.5}{2(8)}(4)^2 = 425.00 + 10.00 - 4.25 = \mathbf{430.75\text{ ft}}$ (and at the end of the curve $x = 8\text{ stations}$, $\text{PVT} = 425.00 + 2.5(8) - 17.00 = \mathbf{428.00\text{ ft}}$).

* **Calculator Interface:** Primary Key: {{key:sc35:VCV}} • Expression / Workspace: `VCV: Parabolic elevation workspace` • Softkeys: `PVC` `g1` `g2` `L`


---

### Eq. 2.3 — Average End-Area Cut Volume

To determine the volume of earth and rock that must be blasted out of the granite hillside, highway engineers approximate the cut as a series of trapezoidal prisms. The average end-area method ({{key:sc35:CUT}}) averages the cross-sectional cut areas $A_1$ and $A_2$ (in square feet) at the beginning and end of each station, multiplying by the interval length $L_{\text{cut}}$ and dividing by $27\text{ ft}^3/\text{yd}^3$ to yield bank volume in cubic yards:

$$V_{\text{cut}} = \frac{A_1 + A_2}{2} \cdot \frac{L_{\text{cut}}}{27}$$

For a vertical crest curve starting at elevation $\text{PVC} = 425.00\text{ ft}$ with entry grade $g_1 = +2.50\%$, exit grade $g_2 = -1.75\%$, and curve length $L = 8\text{ stations}$ ($800\text{ ft}$), the midpoint elevation at $x = L / 2 = 4\text{ stations}$ is $\text{Elev}(4) = 425.00 + 2.5(4) + \frac{-1.75 - 2.5}{2(8)}(4)^2 = 425.00 + 10.00 - 4.25 = \mathbf{430.75\text{ ft}}$ (and at the end of the curve $x = 8\text{ stations}$, $\text{PVT} = 425.00 + 2.5(8) - 17.00 = \mathbf{428.00\text{ ft}}$). Across a $L_{\text{cut}} = 150.0\text{ ft}$ granite bench cut between end areas $A_1 = 320.0\text{ ft}^2$ and $A_2 = 400.0\text{ ft}^2$, {{key:sc35:CUT}} evaluates $V_{\text{cut}} = \frac{320 + 400}{2} \times \frac{150}{27} = \mathbf{2{,}000.00\text{ yd}^3}$.

* **Calculator Interface:** Primary Key: {{key:sc35:CUT}} • Expression / Workspace: `Prism earthwork volume` • Softkeys: {{keycap:CUT}} {{keycap:STA}}


---

### Eq. 2.4 — Three-Wire Differential Spirit Leveling

To carry a vertical elevation from a Benchmark (BM) of known elevation $H = E_{\text{BM}}$ to an uphill Turning Point (TP) or construction stake, a surveyor sets up a compensated optical level midway between the two stations ({{key:sc35:LVL}}). Sighting backward along the horizontal optical plane to a graduated leveling rod held plumb on the benchmark yields the **Backsight** reading $B$, which adds to $H$ to establish the optical **Height of Instrument** ($\text{HI} = H + B$). Turning the telescope forward to a rod held on the new station yields the **Foresight** reading $F$, which subtracts from $\text{HI}$ to determine the new station **Elevation** $E$:

$$\text{HI} = H + B$$

In this differential leveling chain, $H$ is the starting benchmark elevation above mean sea level, $\text{HI}$ is the elevation of the telescope's horizontal line of sight, and $B - F$ is the net vertical rise ($+$) or fall ($-$) between the two rod positions. Setting up above canyon-floor benchmark BM-1 ($H = 4{,}812.40\text{ ft}$) and reading a backsight of $B = 6.85\text{ ft}$ establishes the optical plane at $\text{HI} = 4812.40 + 6.85 = \mathbf{4{,}819.25\text{ ft}}$. Sighting forward to the curve entry stake at PC (Station `124+50.00` via {{key:sc35:STA}}) with a center-wire foresight of $F = 5.42\text{ ft}$ determines the PC pavement elevation as $E = 4819.25 - 5.42 = \mathbf{4{,}813.83\text{ ft}}$.

* **Calculator Interface:** Primary Key: {{key:sc35:LVL}} • Expression / Workspace: `LVL: E = H + B - F` • Softkeys: {{keycap:E}} {{keycap:H}} {{keycap:B}} {{keycap:F}}


---

### Eq. 2.5 — Earth Curvature and Atmospheric Refraction

Because the Earth is an oblate spheroid of mean radius $R_E \approx 20{,}906{,}000\text{ ft}$ ($6{,}371{,}000\text{ m}$), the true level surface curves downward away from the instrument's flat tangent plane by $h_c = D^2 / (2 R_E) \approx 0.667 \cdot D_{\text{miles}}^2\text{ ft}$. Simultaneously, terrestrial atmospheric refraction bends the optical sightline downward toward denser air near the ground, refracting the apparent line of sight upward by approximately one-seventh of curvature ($r \approx 0.093 \cdot D_{\text{miles}}^2\text{ ft}$). Combining physical curvature with atmospheric refraction yields the net vertical drop:

$$h_{cr} = 0.574 \cdot D_{\text{miles}}^2\text{ ft}$$

$$h_{cr} = 0.0675 \cdot D_{\text{km}}^2\text{ m}$$

Carlos points across the canyon reservoir: over an extended 2-mile shot across the lake ($D = 2.0\text{ miles}$), the line of sight dips by $h_{cr} = 0.574 \times (2.0)^2 = 2.296 \approx \mathbf{2.3\text{ ft}}$. Over that single two-mile sightline, the uncorrected rod reading overstates the true elevation by nearly two and a half feet. Sighting across water bodies where balancing backsight and foresight distances is precluded demands subtracting $h_{cr}$ ($E = \text{HI} - (F - h_{cr})$) before staking grade stakes into the subbase.

* **Calculator Interface:** Primary Key: Basic Arithmetic on Stack (`x²`, `×`) • Expression / Workspace: `Stack: D in X, square and multiply by 0.574 (miles) or 0.0675 (km)` • Softkeys: {{keycap:x²}} {{keycap:×}}


---

### Eq. 3.1 — Orthogonal Wind Vector Decomposition

When an aircraft aligns with a runway or flies a cross-country course of heading $\psi_{\text{course}}$, a wind of speed $V_w$ (in knots, converted via {{key:sc35:▸kt}}) blowing from direction $\psi_{\text{wind}}$ forms a relative wind angle $\theta = \psi_{\text{wind}} - \psi_{\text{course}}$ with the flight path. Staging wind speed $V_w$ in Register $Y$ and relative wind angle $\theta$ in Register $X$ and pressing {{key:sc35:WND}} decomposes the wind vector into orthogonal components: the cosine projection governs the longitudinal headwind along the fuselage, while the sine projection governs the lateral crosswind pushing the wings sideways:

$$V_{\text{hw}} = V_w \cos(\theta)$$

With a $V_w = 28\text{ kt}$ wind blowing at $\theta = 40^\circ$ off the course (`28` {{key:sc35:ENTER}} `40` {{key:sc35:WND}}), the instrument places the headwind component $V_{\text{hw}} = 28\cos(40^\circ) = \mathbf{21.45\text{ kt}}$ into Register $Y$ and the crosswind component $V_{\text{xw}} = 28\sin(40^\circ) = \mathbf{18.00\text{ kt}}$ into Register $X$.

* **Calculator Interface:** Primary Key: {{key:sc35:WND}} • Expression / Workspace: `WND: X = V × SIN(A)` • Softkeys: {{keycap:X}} {{keycap:V}} {{keycap:A}}


---

### Eq. 3.2 — Aeronautical Wind Correction Angle

To prevent the crosswind from drifting the aircraft off course, the pilot points the aircraft's nose slightly into the wind. The required crab angle uses the inverse sine—or $\arcsin$—to ask the fundamental question of the unit circle: what crab angle into the wind produces a sideways velocity component that exactly counteracts the crosswind drift? Because the sine of an angle is the perpendicular projection of a unit vector, taking the arcsin of the crosswind-to-airspeed ratio finds the precise nose heading required to keep the aircraft's track pinned to the centerline:

$$\text{WCA} = \arcsin\!\left(\frac{V_{\text{xw}}}{V_{\text{TAS}}}\right)$$

Crabbing into the wind at $V_{\text{TAS}} = 145\text{ kt}$ with $V_{\text{xw}} = 18.00\text{ kt}$ requires $\text{WCA} = \arcsin(18.00 / 145) \approx \mathbf{7.13^\circ}$ ({{key:sc35:ASIN}}), pinning the aircraft's track to the runway centerline.

* **Calculator Interface:** Primary Key: {{key:sc35:XWC}} • Expression / Workspace: `WCA = arcsin(V_xw / V_TAS)` • Softkeys: {{keycap:XWC}} {{keycap:ASIN}}


---

### Eq. 3.3 — Effective Flight Groundspeed

Once the aircraft crabs into the wind, its forward progress along the desired geographic track is the cosine projection of its true airspeed minus the opposing headwind component:

$$\text{GS} = V_{\text{TAS}} \cos(\text{WCA}) - V_{\text{hw}}$$

With a $V_w = 28\text{ kt}$ wind blowing at $\theta = 40^\circ$ off the course (`28` {{key:sc35:ENTER}} `40` {{key:sc35:WND}}), the instrument places the headwind component $V_{\text{hw}} = 28\cos(40^\circ) = \mathbf{21.45\text{ kt}}$ into Register $Y$ and the crosswind component $V_{\text{xw}} = 28\sin(40^\circ) = \mathbf{18.00\text{ kt}}$ into Register $X$. Crabbing into the wind at $V_{\text{TAS}} = 145\text{ kt}$ by $\text{WCA} = \arcsin(18.00 / 145) \approx \mathbf{7.13^\circ}$ ({{key:sc35:ASIN}}) holds the desired track over the ridge at a net ground speed of $\text{GS} = 145\cos(7.13^\circ) - 21.45 \approx 143.88 - 21.45 = \mathbf{122.43\text{ kt}}$.

* **Calculator Interface:** Primary Key: {{key:sc35:TSD}} • Expression / Workspace: `TSD: D = S × T` • Softkeys: {{keycap:D}} {{keycap:S}} {{keycap:T}}


---

### Eq. 3.4 — Barometric Density Altitude

By the ideal gas law ($\rho = P / (R_{\text{specific}} T)$), heating an air parcel at constant pressure causes it to expand and become less dense. Each $1^\circ\text{C}$ of warming above the standard altitude temperature $T_{\text{ISA}}(P) = 15 - 0.002 P$ thins the air by the equivalent of $+120\text{ ft}$ of altitude gain, defining the **Density Altitude** ({{key:sc35:ALT}}) from Pressure Altitude $P$ (in feet) in Register $Y$ and Outside Air Temperature $T$ (in $^\circ\text{C}$) in Register $X$:

$$\text{DA} = P + 120 \times \left(T - T_{\text{ISA}}(P)\right)$$

At the high-desert strip where Pressure Altitude is $P = 6{,}200\text{ ft}$ ($T_{\text{ISA}} = 2.6^\circ\text{C}$) and the afternoon Outside Air Temperature is $T = 28^\circ\text{C}$, the $+25.4^\circ\text{C}$ thermal deviation above standard temperature adds $120 \times 25.4 = +3{,}048\text{ ft}$, raising the true Density Altitude via `6200` {{key:sc35:ENTER}} `28` {{key:sc35:ALT}} to $\text{DA} = 6200 + 3048 = \mathbf{9{,}248\text{ ft}}$ and warning the crew to use high-altitude landing flare speeds and full reverse thrust.

* **Calculator Interface:** Primary Key: {{key:sc35:ALT}} • Expression / Workspace: `ALT: D = P + 120 × (T - 15)` • Softkeys: {{keycap:D}} {{keycap:P}} {{keycap:T}}


---


## Unit II: Industrial Trades, Electrical, and Mechanical

The **SC-14** provides dedicated faceplate keys and bidirectional Equation Solver workspaces to execute the governing laws of this domain. Each equation is indexed below with its physical motivation, governing formula, and operational calculator softkeys.

### Eq. 4.1 — Conductor Circular Mil Area and DC Resistance

In Euclidean geometry, a cylindrical wire of diameter $d$ has cross-sectional area $A = \frac{\pi}{4}d^2$. To eliminate the transcendental factor $\pi/4$ from field cable tables, North American electrical engineering defines the **Circular Mil** ($\text{CM}$) as the area of a circle whose diameter is exactly one mil ($1\text{ mil} = 0.001\text{ in}$), so area in circular mils equals the square of the diameter in mils:

$$\text{CM} = d_{\text{mils}}^2 = \left(1000 \cdot d_{\text{inches}}\right)^2$$

In these expressions, $d_{\text{mils}}$ is the conductor diameter in thousandths of an inch, $L$ is the conductor length in feet, and $K$ is the material's **specific resistance constant** (in $\Omega\cdot\text{cmil/ft}$ at $75^\circ\text{C}$ operating temperature), equal to $K_{\text{Cu}} = 12.9\ \Omega\cdot\text{cmil/ft}$ for uncoated copper and $K_{\text{Al}} = 21.2\ \Omega\cdot\text{cmil/ft}$ for aluminum (both listed in the {{key:sc14:▦}} NEC reference table). Solid and stranded building conductors are indexed on the logarithmic **American Wire Gauge** ({{key:sc14:AWG}}) scale, in which smaller gauge numbers designate thicker conductors that double in cross-sectional area every three gauge steps down. NEC Chapter 9, Table 8 tabulates the direct-current resistance $R_{1000}$ in **ohms per thousand feet** ($\Omega/\text{kft}$ at $75^\circ\text{C}$) alongside NEC Table 310.16 $75^\circ\text{C}$ copper ampacities:

* **Calculator Interface:** Primary Key: {{key:sc14:AWG}} • Expression / Workspace: `NEC Table 8 wire circular mils and resistance` • Softkeys: {{keycap:AWG}} {{keycap:Ω}}


---

### Eq. 4.2 — Single-Phase and Three-Phase Feeder Voltage Drop

When current flows through a long feeder run, the conductor's ohmic resistance converts voltage into waste heat. In a single-phase circuit, current travels out and back, creating a round-trip path of twice the one-way distance. In a balanced three-phase circuit, the three alternating currents are separated by 120 degrees and partially cancel in their return paths, replacing the two-wire factor of two with the geometric ratio $\sqrt{3} \approx 1.732$:

$$V_{\text{drop},1\phi} = \frac{2 \cdot K \cdot L \cdot I}{\text{CM}}$$

On a $480\text{ V}$ three-phase feeder supplying $45\text{ kVA}$ over $L = 220\text{ ft}$ of #6 AWG copper wire ($R_{1000} = 0.491\ \Omega/\text{kft}$, $I_L = 54.13\text{ A}$), {{key:sc14:AWG}} evaluates $V_{\text{drop},3\phi} = \frac{\sqrt{3} \times 0.491 \times 220 \times 54.13}{1000} \approx \mathbf{10.13\text{ V}}$ ($2.11\% \le 3.0\%$).

* **Calculator Interface:** Primary Key: {{key:sc14:AWG}} • Expression / Workspace: `AWG: D = 2 × R × L × I / 1000` • Softkeys: {{keycap:D}} {{keycap:R}} {{keycap:L}} {{keycap:I}}


---

### Eq. 4.3 — Harmonic Parallel Resistance

When two parallel conductors or loads share the current path, total conductance is the sum of their individual conductances. Inverting that sum gives the harmonic mean—the product over the sum:

$$R_1 \parallel R_2 = \frac{R_1 \cdot R_2}{R_1 + R_2}$$

Here $R_{1000}$ is the NEC Table 8 conductor resistance in $\Omega/\text{kft}$, $L$ is the one-way run length in feet, $I$ is the line current in amperes, and $R_1 \parallel R_2 = (R_1^{-1} + R_2^{-1})^{-1}$ is the harmonic-mean parallel operator. On Pier 14's three-phase $480\text{ V}$ crane feeder carrying $I = 90.211\text{ A}$ over $L = 450\text{ ft}$ of #2 AWG copper ($R_{1000} = 0.194\ \Omega/\text{kft}$), the single-phase equivalent drop is $V_{\text{drop},1\phi} = \frac{2 \times 450 \times 90.211 \times 0.194}{1000} \approx 15.75\text{ V}$ and the balanced three-phase line voltage drop is $V_{\text{drop},3\phi} = \frac{\sqrt{3} \times 450 \times 90.211 \times 0.194}{1000} \approx \mathbf{13.64\text{ V}}$ ($2.84\%$ at rated steady current), which spikes to $\mathbf{20.46\text{ V}}$ ($4.26\%$, starving the crane terminals down to $459.5\text{ V}$) during a $150\%$ hoist starting surge. Paralleling two #1/0 AWG conductors per phase ($R_1 = R_2 = 0.122\ \Omega/\text{kft}$, so $0.122 \parallel 0.122 = \mathbf{0.061\ \Omega/\text{kft}}$ via {{key:sc14:x∥y}}) cuts the steady three-phase voltage drop to $\frac{\sqrt{3} \times 450 \times 90.211 \times 0.061}{1000} \approx \mathbf{4.29\text{ V}}$ ($0.89\%$).

* **Calculator Interface:** Primary Key: {{key:sc14:x∥y}} • Expression / Workspace: `Harmonic parallel resistance shortcut` • Softkeys: {{keycap:x∥y}}


---

### Eq. 4.4 — NEC Continuous Load Feeder Ampacity

Under National Electrical Code Article 215.2(A)(1) (and Article 210.19(A)(1) for branch circuits), a continuous load is defined as any load where maximum current continues for three hours or longer. Standard overcurrent protective devices and terminal distribution blocks are rated to carry continuous load at only $80\%$ of their nominal nameplate rating ($1 / 0.80 = 1.25$). Sizing conductors for only $100\%$ of continuous load exposes terminal lugs to chronic thermal fatigue and setscrew loosening from differential thermal expansion. To prevent terminal lug burnout and maintain switchgear within its rated thermal dissipation envelope, feeder conductors must be sized to carry at least $125\%$ of continuous load plus $100\%$ of non-continuous load:

$$I_{\text{min}} = 1.25 \cdot I_{\text{continuous}} + I_{\text{non-continuous}}$$

For Pier 14's crane hoist hydraulic pump drawing $I_{\text{continuous}} = 72.0\text{ A}$ alongside an auxiliary non-continuous service lighting load of $I_{\text{non-continuous}} = 18.0\text{ A}$, the minimum allowable feeder conductor ampacity prior to raceway derating is $I_{\text{min}} = 1.25 \times 72.0 + 18.0 = 90.0 + 18.0 = \mathbf{108.0\text{ A}}$.

* **Calculator Interface:** Primary Key: Continuous Load Scaling on Stack (`1.25` `×` `+`) • Expression / Workspace: `Stack: I_cont in Y, 1.25 in X, multiply and add I_noncont` • Softkeys: {{keycap:×}} {{keycap:+}}


---

### Eq. 4.5 — Alternating Current Power Triangle

In a resistive load such as an immersion heater, alternating current rises and falls in phase with alternating voltage. In an inductive load such as the Pier 14 gantry crane hoist motor, the alternating magnetic field stores and returns reactive energy every quarter-cycle, causing the RMS line current $I$ to lag behind the RMS supply voltage $V$ by a phase angle $\phi$. Because only the current component in phase with voltage ($I\cos\phi$) performs real mechanical or thermal work, AC power forms a right triangle governed by the dimensionless **Power Factor** $\text{PF} = \cos\phi \in [0, 1]$ ({{key:sc14:PF}}), linking **Real Working Power** $P$ (in watts, $\text{W}$, or kilowatts, $\text{kW}$, converted via {{key:sc14:▸kW}} and {{key:sc14:▸HP}}), **Reactive Magnetizing Power** $Q$ (in volt-amperes reactive, $\text{VAR}$, or $\text{kVAR}$), and **Apparent Power** $S$ (in volt-amperes, $\text{VA}$, or $\text{kVA}$):

$$P = S \cos(\phi)$$

In this power triangle, $S$ is the hypotenuse that sizes transformers, switchgear, and feeder conductors, $P$ is the adjacent horizontal leg converted into shaft work and heat, and $Q$ is the opposite vertical leg oscillating between the source and the motor's magnetic field. On Pier 14's crane rated at apparent power $S = 75.0\text{ kVA}$ and lagging power factor $\text{PF} = 0.80$ ($\phi = \arccos(0.80) \approx 36.87^\circ$, $\sin\phi = 0.60$), the real working power is $P = 75.0 \times 0.80 = \mathbf{60.0\text{ kW}}$ ($80.46\text{ HP}$ via {{key:sc14:▸HP}}) and the reactive magnetizing demand is $Q = 75.0 \times 0.60 = \mathbf{45.0\text{ kVAR}}$. Installing a parallel $25.0\text{ kVAR}$ capacitor bank at the crane disconnect supplies $25.0\text{ kVAR}$ locally, reducing net reactive draw from the feeder to $Q_{\text{new}} = 45.0 - 25.0 = 20.0\text{ kVAR}$, shrinking apparent feeder demand to $S_{\text{new}} = \sqrt{60.0^2 + 20.0^2} \approx \mathbf{63.25\text{ kVA}}$, and raising the corrected power factor to $\text{PF}_{\text{new}} = 60.0 / 63.2456 \approx \mathbf{0.9487}$.

* **Calculator Interface:** Primary Key: {{key:sc14:PF}} • Expression / Workspace: `PF: P = V × I × F` • Softkeys: {{keycap:P}} {{keycap:V}} {{keycap:I}} {{keycap:F}}


---

### Eq. 4.6 — Three-Phase Motor Full-Load Current

This geometric ratio $\sqrt{3} \approx 1.73205$ produces the two standard commercial voltage systems in North America: multiplying $V_{LN} = 120\text{ V}$ by $\sqrt{3}$ gives $207.85\text{ V}$ ($208\text{Y}/120\text{ V}$), and multiplying $V_{LN} = 277\text{ V}$ by $\sqrt{3}$ gives $479.78\text{ V}$ ($480\text{Y}/277\text{ V}$). Because each of the three phases delivers apparent power $V_{LN} I_L = (V_{LL}/\sqrt{3})I_L$, total three-phase apparent power across all three phases is $3(V_{LL}/\sqrt{3})I_L = \sqrt{3}\,V_{LL}I_L$. Expressing three-phase apparent power $S_{\text{kVA}}$ in kilovolt-amperes ({{key:sc14:kVA}}) to solve for per-phase line current $I_L$, or converting rated mechanical output horsepower $\text{HP}$ ($1\text{ HP} = 746\text{ W}$) and fractional efficiency $\eta \in (0, 1]$ into three-phase motor **Full-Load Amps** $I_{\text{FLA}}$ ({{key:sc14:FLA}}), gives:

$$I_{\text{FLA}} = \frac{\text{HP} \times 746}{\sqrt{3} \cdot V_{LL} \cdot \eta}$$

For a $30\text{ HP}$ induction motor operating at $480\text{ V}$ with efficiency $\eta = 0.90$ and power factor $0.86$, {{key:sc14:FLA}} evaluates $I_{\text{FLA}} = \frac{30 \times 746}{\sqrt{3} \times 480 \times 0.90 \times 0.86} \approx \mathbf{34.78\text{ A}}$, requiring $125\%$ continuous-duty feeder ampacity of $\mathbf{43.47\text{ A}}$.

* **Calculator Interface:** Primary Key: {{key:sc14:FLA}} • Expression / Workspace: `Three-phase motor full-load amperes` • Softkeys: {{keycap:I}} {{keycap:P}} {{keycap:V}} {{keycap:E}}


---

### Eq. 5.1 — Conduit Offset Travel and Half-Angle Shrinkage

In the right triangle formed by the perpendicular offset depth $O$ (opposite side) and the bend angle $\theta$ (denoted $A$ in the {{key:sc14:OFS}} solver workspace `T = O / SIN(A)` opened via {{key:sc14:OFS}}), the center-to-center **Travel Distance** $T$ along the diagonal pipe between the two bend marks ({{key:sc14:OFS}}) is the cosecant hypotenuse $O\csc\theta$. Because the conduit previously spanned the full length $T$ along the wall but now projects horizontally across only the adjacent side $O\cot\theta$, bending the offset pulls the far end of the pipe backward toward the starting coupling by the axial **Conduit Shrinkage** $S_{\text{shrink}}$, which simplifies by the trigonometric half-angle identity $\csc\theta - \cot\theta = \frac{1 - \cos\theta}{\sin\theta} = \tan(\theta / 2)$:

$$T = \frac{O}{\sin(\theta)} = O \csc(\theta)$$

In these expressions, $O$ is the perpendicular offset depth in inches, $\theta$ is the bender shoe angle in degrees, $T$ is the distance measured along the tubing between the two bend marks, and $S_{\text{shrink}}$ is the length added to the obstruction setback when placing the Obstruction-Approach mark first (while a 3-argument {{key:sc14:OFS}} call with offset $O$ in Register $Z$, angle $\theta$ in Register $Y$, and bender deduct $D$ in Register $X$ returns net travel $T - D$). Standard conduit bender shoes engrave five primary bend angles, each with its cosecant travel multiplier and half-angle tangent shrinkage per inch of offset depth:

* **Calculator Interface:** Primary Key: {{key:sc14:OFS}} • Expression / Workspace: `OFS: T = O / SIN(A)` • Softkeys: {{keycap:T}} {{keycap:O}} {{keycap:A}}


---

### Eq. 5.2 — Compound Rolling Offset Travel

When a conduit run must simultaneously shift vertically by a **Rise** $R_{\text{vert}}$ and horizontally by a lateral **Roll** $R_{\text{horiz}}$ to enter a misaligned cabinet, the two perpendicular displacements form a right triangle in the cross-sectional plane perpendicular to the conduit axis. By the Pythagorean theorem, rotating the conduit bender in that plane aligns the shoe with the **True Offset Depth** $O_{\text{true}}$ ({{key:sc14:FIT}} or {{key:sc14:MIT}}), which then scales by $\csc\theta$ via {{key:sc14:OFS}} to yield the rolling travel distance $T_{\text{roll}}$:

$$O_{\text{true}} = \sqrt{R_{\text{vert}}^2 + R_{\text{horiz}}^2}$$

Here $R_{\text{vert}}$ and $R_{\text{horiz}}$ are the orthogonal vertical and horizontal shifts in inches, $O_{\text{true}}$ is the diagonal offset depth in the rotated bending plane evaluated via {{key:sc14:FIT}} or {{key:sc14:MIT}}, and $T_{\text{roll}}$ is the center-to-center distance between bend marks along the conduit evaluated via {{key:sc14:OFS}}. Where the boiler-room rack rises $R_{\text{vert}} = 6.0\text{ in.}$ and rolls laterally $R_{\text{horiz}} = 8.0\text{ in.}$ into the MCC knockouts, keying `6` {{key:sc14:ENTER}} `8` {{key:sc14:FIT}} returns the true diagonal offset $O_{\text{true}} = \sqrt{6.0^2 + 8.0^2} = \mathbf{10.00\text{ in.}}$, and keying `30` {{key:sc14:OFS}} bends that compound offset at $\theta = 30^\circ$ with a travel distance of $T_{\text{roll}} = 10.00 / \sin(30^\circ) = \mathbf{20.00\text{ in.}}$ between marks.

* **Calculator Interface:** Primary Key: {{key:sc14:FIT}} • Expression / Workspace: `FIT: Rolling compound offset` • Softkeys: {{keycap:FIT}} {{keycap:MIT}}


---

### Eq. 5.3 — Three-Point Saddle Outer Leg Travel

When a conduit strapped flat against a wall must step over a single cylindrical pipe of height $O$ and return to the same mounting surface, electricians form a **Three-Point Saddle** consisting of a center crown bend of angle $\theta_{\text{center}} = 45^\circ$ placed directly over the obstruction centerline, flanked by two symmetric outer return bends of $\theta_{\text{outer}} = \theta_{\text{center}} / 2 = 22.5^\circ$:

$$T_{\text{saddle}} = \frac{O}{\sin(22.5^\circ)} = O \csc(22.5^\circ) \approx 2.6131 \cdot O$$

Total axial shrinkage across both sloped legs adds $S_{\text{saddle}} = 2 \cdot O \tan(11.25^\circ) \approx \frac{3}{16}\text{ in.} \times O$ to the center mark distance. Over the boiler room's $O = 4.0\text{ in.}$ steam pipe centered $120.0\text{ in.}$ ($10\text{ ft } 0\text{ in.}$) down the wall, total saddle shrinkage is $4 \times (3/16\text{ in.}) = \mathbf{0.75\text{ in.}}$ ($3/4\text{ in.}$), placing the center $45^\circ$ mark at $120.75\text{ in.}$ and the two outer $22.5^\circ$ return marks at $T_{\text{saddle}} = 4.0 / \sin(22.5^\circ) \approx \mathbf{10.45\text{ in.}}$ ($10\text{-}7/16\text{ in.}$ via {{key:sc14:f-i}}, or $10.0\text{ in.}$ by the $2.5\times$ field rule) on either side of the center mark.

* **Calculator Interface:** Primary Key: {{key:sc14:OFS}} • Expression / Workspace: `Three-point saddle 45°/22.5° outer travel` • Softkeys: {{keycap:OFS}} {{keycap:f-i}}


---

### Eq. 5.4 — National Electrical Code Cross-Sectional Raceway Fill

Once a conduit run is installed, pulling insulated conductors around multiple bends generates capstan friction proportional to $e^{\mu \Sigma\theta}$ and traps $I^2 R$ heat inside the tube. To prevent insulation abrasion during pulling and ensure adequate air space for heat dissipation, **NEC Chapter 9, Table 1** (accessible directly via {{key:sc14:▦}} on the `SC-14`: `1W FILL = 53% MAX`, `2W FILL = 31% MAX`, `3+W FIL = 40% MAX`) limits the cross-sectional **Conduit Fill Ratio** to $53\%$ for $1$ conductor, $31\%$ for $2$ conductors, and $\mathbf{40\%}$ for $3$ or more conductors:

$$\text{Fill\%} = \left(\frac{\sum_{k=1}^{N} A_{\text{wire},k}}{A_{\text{conduit}}}\right) \times 100\% \le 40\%$$

Here $A_{\text{conduit}}$ is the total internal cross-sectional area of the raceway from NEC Chapter 9, Table 4 (while {{key:sc14:SCH}} and {{key:sc14:WAL}} evaluate pipe inner diameter and wall thickness $OD - ID$), $A_{\text{wire}}$ is the insulated conductor area from NEC Chapter 9, Table 5, and $N_{\max}$ is the maximum whole number of identical conductors permitted at the $40\%$ ceiling:

* **Calculator Interface:** Primary Key: {{key:sc14:AWG}} • Expression / Workspace: `NEC Chapter 9 Table 1 40% raceway fill` • Softkeys: {{keycap:AWG}} {{keycap:▦}}


---

### Eq. 6.1 — Spindle Rotational Speed and Table Feed Rate

When a lathe turns a cylindrical bar of diameter $D$ (in inches) or a milling machine spins an end-mill of diameter $D$ at spindle rotational speed $N$ (in Revolutions Per Minute, $\text{RPM}$), each revolution carries a cutting tooth around the outer circumference $\pi D\text{ inches} = \frac{\pi D}{12}\text{ feet}$. Multiplying by $N\text{ rev/min}$ defines the tangential cutting velocity in **Surface Feet per Minute** ({{key:sc14:SFM}}), and inverting that relation determines the required **Spindle Speed** $N$ ({{key:sc14:SFM}} / {{key:sc14:RPM}}), the linear table **Feed Rate** $F_m$ (in $\text{in/min}$) for a cutter with $Z$ flutes and chip load $f_t$ (in $\text{in/tooth}$), and the $75\%$-thread **Tap Drill Diameter** $D_{\text{tap}}$ ({{key:sc14:TAP}}) for a screw of major diameter $D_{\text{major}}$ and pitch $P_{\text{tpi}}$ (threads per inch, or metric/decimal pitch $p$ when $X \le 3$):

$$N = \frac{12 \cdot \text{SFM}}{\pi \cdot D} \approx \frac{3.8197 \cdot \text{SFM}}{D}$$

The $75\%$ tap drill diameter subtracts one thread pitch from major diameter: $D_{\text{tap}} = D_{\text{major}} - 1/P_{\text{tpi}}$. In these machining equations, $D$ is the cutter or workpiece diameter in inches, $12 / \pi \approx 3.8197186$ ($3.82$ in the {{key:sc14:SFM}} workspace `N = 3.82 × S / D` with softkeys {{keycap:N}}, {{keycap:S}}, {{keycap:D}}) converts feet per minute into inches per revolution, $f_t \cdot Z$ is the linear advance per spindle revolution, and subtracting one pitch length $1 / P_{\text{tpi}}$ from the major diameter $D_{\text{major}}$ yields the standard $75\%$ unified national thread tap drill diameter. While an aluminum roughing pass at $\text{SFM} = 400\text{ ft/min}$ on a $D = 0.500\text{ in.}$ cutter runs at `400` {{key:sc14:ENTER}} `0.5` {{key:sc14:SFM}} $\to \mathbf{3{,}055.77\text{ RPM}}$, milling 4140 steel rated at $\text{SFM} = 100\text{ ft/min}$ with a $D = 0.500\text{ in.}$ 4-flute end-mill and a chip load of $f_t = 0.003\text{ in/tooth}$ requires reducing the spindle speed via `100` {{key:sc14:ENTER}} `0.5` {{key:sc14:SFM}} to $N = \frac{12 \times 100}{\pi \times 0.500} \approx \mathbf{763.94\text{ RPM}}$ and setting the table feed rate to $F_m = 763.9437 \times 0.003 \times 4 \approx \mathbf{9.17\text{ in/min}}$. When taking light radial finishing cuts where radial engagement is under half the cutter diameter ($A_e < D/2$), machinists apply radial chip thinning ($f_{\text{actual}} = f_t / \sqrt{A_e/D}$) to maintain effective chip thickness and prevent tool rubbing and work hardening. Tapping the 1/2-13 UNC flange holes ($D_{\text{major}} = 0.500\text{ in.}$, $P_{\text{tpi}} = 13\text{ TPI}$) via `0.5` {{key:sc14:ENTER}} `13` {{key:sc14:TAP}} requires a tap drill diameter of $D_{\text{tap}} = 0.500 - 1/13 \approx \mathbf{0.4231\text{ in.}}$ ($27/64\text{ in.} = 0.4219\text{ in.}$).

* **Calculator Interface:** Primary Key: {{key:sc14:SFM}} • Expression / Workspace: `SFM: N = 3.82 × S / D` • Softkeys: {{keycap:N}} {{keycap:S}} {{keycap:D}}


---

### Eq. 6.2 — Bolt Circle Chord Spacing

When drilling $N$ equally spaced bolt holes around a pitch circle of diameter $D_{\text{bolt}}$ (radius $R = D_{\text{bolt}}/2$), the central angle between adjacent holes is $\Delta\theta = 360^\circ / N$. Bisecting the isosceles triangle formed by the circle center and two adjacent holes yields two right triangles with half-angle $\frac{\Delta\theta}{2} = \frac{180^\circ}{N}$ and hypotenuse $R = D_{\text{bolt}}/2$:

$$C = 2 R \sin\!\left(\frac{180^\circ}{N}\right) = D_{\text{bolt}} \sin\!\left(\frac{180^\circ}{N}\right)$$

Cartesian hole coordinates follow as $X_k = \frac{D_{\text{bolt}}}{2}\cos(\theta_0 + k \cdot \frac{360^\circ}{N})$ and $Y_k = \frac{D_{\text{bolt}}}{2}\sin(\theta_0 + k \cdot \frac{360^\circ}{N})$. Here $C$ is the straight-line center-to-center **Chord Distance** ({{key:sc14:BC}}, which also opens the {{key:sc14:BC}} workspace `C = D × SIN(180 / N)` with softkeys {{keycap:C}}, {{keycap:D}}, {{keycap:N}}) between adjacent holes used for caliper verification, and $(X_k, Y_k)$ are the Cartesian CNC table coordinates of hole $k \in \{0, 1, \dots, N-1\}$ starting from reference angle $\theta_0$. On an $N = 8\text{-bolt}$ hub with a $D_{\text{bolt}} = 6.00\text{ in.}$ pitch circle ($\frac{180^\circ}{8} = 22.5^\circ$), keying `6` {{key:sc14:ENTER}} `8` {{key:sc14:BC}} returns $C = 6.00\sin(22.5^\circ) \approx \mathbf{2.2961\text{ in.}}$, while on the outer $D_{\text{bolt}} = 10.00\text{ in.}$ steam flange (`10` {{key:sc14:ENTER}} `8` {{key:sc14:BC}}), the chord spacing is $C = 10.00\sin(22.5^\circ) \approx \mathbf{3.8268\text{ in.}}$.

* **Calculator Interface:** Primary Key: {{key:sc14:BC}} • Expression / Workspace: `BC: C = D × SIN(180 / N)` • Softkeys: {{keycap:C}} {{keycap:D}} {{keycap:N}}


---

### Eq. 6.3 — Control Valve Volumetric Flow and Pump Power

In the cooling header supplying the machining center, incompressible fluid of cross-sectional pipe area $A$ moving at velocity $V$ obeys the **Pipe Flow Continuity Law** $Q = A \times V$ ({{key:sc14:PIP}}, opening the {{key:sc14:PIP}} workspace with softkeys {{keycap:Q}}, {{keycap:A}}, {{keycap:V}}). Downstream, a control valve of **Flow Coefficient** $C_v$ ({{key:sc14:Cᵥ}}) passes $Q\text{ GPM}$ ({{key:sc14:▸GPM}}) of fluid of specific gravity $G = \rho / \rho_w$ ({{key:sc14:ρw}}) across pressure drop $\Delta P$ (in $\text{psi}$, {{key:sc14:▸PSI}}), lifting $Q\text{ GPM}$ against $H\text{ feet}$ of total dynamic head requires hydraulic **Pump Power** $P_{\text{BHP}}$ ({{key:sc14:PMP}}, where $33{,}000\text{ ft}\cdot\text{lb/min} \div 8.333\text{ lb/gal} = 3{,}960$), and preventing cavitation at the pump impeller eye requires maintaining **Available Net Positive Suction Head** $\text{NPSH}_a$ ({{key:sc14:NPH}}) above the pump's required threshold:

$$Q = C_v \sqrt{\frac{\Delta P}{G}}$$

Continuity dictates $Q = A \cdot V$, while suction margin follows as $\text{NPSH}_a = P_{\text{atm}} - P_{\text{vap}} \pm z_s - h_f$. In these fluid-power relations, $Q$ scales with pipe area and velocity in {{key:sc14:PIP}} and with the square root of valve pressure drop $\Delta P$ in {{key:sc14:Cᵥ}} ({{key:sc14:Cᵥ}} workspace softkeys {{keycap:Q}}, {{keycap:C}}, {{keycap:P}}, {{keycap:G}}), $P_{\text{BHP}}$ measures the water horsepower delivered by {{key:sc14:PMP}} ({{key:sc14:PMP}} workspace softkeys {{keycap:P}}, {{keycap:Q}}, {{keycap:H}}), and {{key:sc14:NPH}} evaluates available suction head margin so vapor bubbles do not implode against the impeller vanes. Meanwhile, with the fixture's $\varnothing\,2.00\text{ in.}$ hydraulic clamping cylinder ($A_{\text{piston}} = \frac{\pi}{4}(2.00)^2 = \pi \approx 3.1416\text{ in}^2$) pressurized to $P_{\text{psi}} = 1{,}875\text{ psi}$, the clamping force holding the 4140 flange is $F_{\text{clamp}} = 1875 \times \pi \approx \mathbf{5{,}890.49\text{ lbf}}$ ({{key:sc14:▸lbf}}). A coolant control valve with $C_v = 25$ at $\Delta P = 16\text{ psi}$ ($G = 1.0$) delivers $Q = 25\sqrt{16} = \mathbf{100.0\text{ GPM}}$ via `25` {{key:sc14:ENTER}} `16` {{key:sc14:Cᵥ}}, and pumping $Q = 198\text{ GPM}$ against $H = 100\text{ ft}$ of head requires $P_{\text{BHP}} = (198 \times 100)/3960 = \mathbf{5.00\text{ HP}}$ via `198` {{key:sc14:ENTER}} `100` {{key:sc14:PMP}}.

* **Calculator Interface:** Primary Key: {{key:sc14:Cᵥ}} • Expression / Workspace: `CV: Q = C × √(P / G)` • Softkeys: {{keycap:Q}} {{keycap:C}} {{keycap:P}} {{keycap:G}}


---

### Eq. 6.4 — Four-to-Twenty Milliampere Current Scaling

Across the $16.0\text{ mA}$ active span between $4.0\text{ mA}$ ($0\%$) and $20.0\text{ mA}$ ($100\%$), loop current $I_{\text{mA}}$ scales linearly with process percentage $\text{Pct} \in [0, 100]$ via {{key:sc14:mA}}, while an industrial **$\text{Pt100}$ Resistance Temperature Detector** ({{key:sc14:RTD}})—standardized to ice-point resistance $R_0 = 100.0\ \Omega$ at $0^\circ\text{C}$ with IEC 60751 platinum temperature coefficient $\alpha = 0.00385\ \Omega/(\Omega\cdot^\circ\text{C})$—follows the linear Callendar–Van Dusen relation at temperature $T$ (in $^\circ\text{C}$):

$$I_{\text{mA}} = 4.0 + 16.0 \times \left(\frac{\text{Pct}}{100}\right)$$

Here $\text{Pct}$ is the percentage of calibrated transmitter span, $I_{\text{mA}}$ is the loop current in milliamperes evaluated via {{key:sc14:mA}}, and $R(T)$ is the $\text{Pt100}$ sensor resistance in ohms evaluated via {{key:sc14:RTD}}. When the fixture's $0\text{--}3{,}000\text{ psi}$ hydraulic transmitter is pressurized to $1{,}875\text{ psi}$ ($\text{Pct} = (1875 / 3000) \times 100\% = 62.5\%$), keying `62.5` {{key:sc14:mA}} gives the calibrated loop current $I_{\text{mA}} = 4.0 + 16.0(0.625) = \mathbf{14.00\text{ mA}}$ (developing $14.0\text{ mA} \times 250\ \Omega = 3.50\text{ V}$ across the PLC's $250\ \Omega$ sense resistor), confirming that the transmitter is accurate and the intermittent alarm was caused by a loose terminal screw rather than hydraulic pressure loss.

* **Calculator Interface:** Primary Key: {{key:sc14:mA}} • Expression / Workspace: `Four-to-twenty milliampere loop scaling` • Softkeys: {{keycap:mA}} {{keycap:RTD}}


---


## Unit III: Systems Programming, Embedded, and Cyber Operations

The **SC-16** provides dedicated faceplate keys and bidirectional Equation Solver workspaces to execute the governing laws of this domain. Each equation is indexed below with its physical motivation, governing formula, and operational calculator softkeys.

### Eq. 7.1 — Positional Number Base Radix Expansion

In any positional number system of integer radix $b \ge 2$—where $b = 16$ for Hexadecimal ({{key:sc16:HEX}}), $b = 10$ for Decimal ({{key:sc16:DEC}}), $b = 8$ for Octal ({{key:sc16:OCT}}), and $b = 2$ for Binary ({{key:sc16:BIN}})—a $k$-digit word $(d_{k-1} d_{k-2} \dots d_1 d_0)_b$ with digits $d_i \in \{0, 1, \dots, b-1\}$ represents the scalar integer $V$ obtained by summing each digit weighted by its positional power $b^i$:

$$V = \sum_{i=0}^{k-1} d_i \cdot b^i$$

When {{key:sc16:HEX}} mode is active on the `SC-16`, the six top-row softkeys automatically bind to the hexadecimal digits {{keycap:A}}, {{keycap:B}}, {{keycap:C}}, {{keycap:D}}, {{keycap:E}}, and {{keycap:F}} for rapid single-keystroke entry of 16-, 32-, and 64-bit register words. Because $16 = 2^4$, partitioning a binary string into blocks of **four bits (nibbles)** from the least significant bit ($i = 0$) upward maps each 4-bit block $(b_{4m+3} b_{4m+2} b_{4m+1} b_{4m})_2$ with internal weights $(8, 4, 2, 1)$ onto a single hexadecimal digit $H_m \in [0, 15]$ (`0`–`9`, {{keycap:A}}–{{keycap:F}}), while $8 = 2^3$ maps each 3-bit triad onto a single octal digit (`0`–`7`).

* **Calculator Interface:** Primary Key: {{key:sc16:HEX}} / {{key:sc16:DEC}} • Expression / Workspace: `Radix base switching` • Softkeys: {{keycap:HEX}} {{keycap:DEC}} {{keycap:OCT}} {{keycap:BIN}}


---

### Eq. 7.2 — Two's Complement Additive Inversion

In a fixed $W$-bit register ({{key:sc16:WSZ}}), an **Unsigned Integer** ({{key:sc16:UNS}}) assigns positive weight $+2^i$ to every bit $b_i$ from $i = 0$ through $W - 1$. To encode negative numbers without building separate subtraction circuitry, digital processors use **Two's Complement** ({{key:sc16:NEG}}) representation, in which the most significant bit $b_{W-1}$ carries **negative weight $-2^{W-1}$** while the lower $W - 1$ bits retain positive weights $+2^i$. Adding any $W$-bit word $X$ to its bitwise one's complement $\sim X$ ({{key:sc16:~}}, where every `0` flips to `1` and every `1` flips to `0`) produces a word of $W$ ones equal to $2^W - 1$. Adding $1$ yields $X + ((\sim X) + 1) = 2^W \equiv 0 \pmod{2^W}$. Consequently, the additive inverse $-X$ in $W$-bit two's complement ({{key:sc16:NEG}}) is formed by inverting all $W$ bits and adding $1$:

$$-X \equiv 2^W - X \equiv (\sim X) + 1 \pmod{2^W}$$

Because zero (`0x00`) consumes one of the $2^{W-1}$ non-negative bit patterns, every signed $W$-bit two's complement range is asymmetric by one count, extending from $-2^{W-1}$ (`0x80...0`) to $+2^{W-1} - 1$ (`0x7F...F`):

* **Calculator Interface:** Primary Key: {{key:sc16:NEG}} • Expression / Workspace: `Two's complement additive negation` • Softkeys: {{keycap:NEG}} {{keycap:WSZ}} {{keycap:UNS}}


---

### Eq. 7.3 — Contiguous Bitfield Mask Generation

To isolate or modify a multi-bit hardware field of width $w$ bits starting at bit offset $s$, the **Bitfield Mask Generator** ({{key:sc16:MSK}}) shifts $2^w - 1$ ($w$ contiguous `1` bits) left by $s$ positions:

$$\text{MSK}(s, w) = \left((1 \ll w) - 1\right) \ll s$$

The updated register is synthesized via read-modify-write: $R_{\text{updated}} = (R \ \& \ \sim\text{MSK}(s, w)) \mid ((V_{\text{field}} \ll s) \ \& \ \text{MSK}(s, w))$. In this identity, $R$ is the initial control register value, $\text{MSK}(s, w)$ is the positive mask covering bits $[s+w-1 : s]$, $\sim\text{MSK}(s, w)$ is the inverted clear mask with `0`s across the target field and `1`s everywhere else, and $V_{\text{field}} \ll s$ aligns the new setting into position. For our motor controller's 4-bit clock-divider field ($w = 4$) at bit offset $s = 8$ (bits `[11:8]`), the mask is $\text{MSK}(8, 4) = ((1 \ll 4) - 1) \ll 8 = 15 \times 256 = \mathbf{\text{0x0F00}}$ ($3{,}840$). Clearing bits `[11:8]` of `0x00240505` with $\sim\text{0x0F00}$ leaves `0x00240005`, and merging `0xA` shifted left by $8$ (`0x0A00`) via {{key:sc16:&#124;}} yields `0x00240A05` (or $\mathbf{\text{0xA05}}$ on the low 16-bit halfword).

* **Calculator Interface:** Primary Key: {{key:sc16:MSK}} • Expression / Workspace: `Contiguous bitfield mask synthesis` • Softkeys: {{keycap:MSK}} {{keycap:SB}} {{keycap:CB}} {{keycap:B?}}


---

### Eq. 8.1 — IEEE 754 Floating-Point Real Decoding

Once the 32-bit word is in native host order, the **IEEE 754 Single-Precision (`binary32`)** standard ({{key:sc16:FLT}}, alongside half-precision {{key:sc16:F16}} and double-precision {{key:sc16:F64}}) partitions bits `[31:0]` into a 1-bit sign $S \in \{0, 1\}$ at bit 31, an 8-bit unsigned biased exponent $E \in [1, 254]$ at bits `[30:23]` (with bias $127$, so the true binary exponent is $e = E - 127$), and a 23-bit fractional mantissa $M \in [0, 2^{23}-1]$ at bits `[22:0]` with an implicit leading $1$ before the binary point:

$$V_{\text{float}} = (-1)^S \times \left(1 + \frac{M}{2^{23}}\right) \times 2^{E - 127}$$

On microcontrollers without floating-point hardware, **$Q_{m.n}$ Fixed-Point Scaling** ({{key:sc16:Q.n}} and {{key:sc16:FXP}}) instead converts between a real value and an integer scaled by $2^n$: $Q_{\text{int}} = \operatorname{round}(V_{\text{real}} \cdot 2^n)$ and $V_{\text{real}} = Q_{\text{int}} / 2^n$. When the biased exponent bits in an IEEE 754 word are all zero ($E = 0$), the representation shifts into subnormal gradual underflow with an implicit leading zero bit ($v = (-1)^S \times 2^{-126} \times 0.m$), avoiding sudden precision cliffs when subtracting nearly equal quantities. In the byte-swapped 32-bit telemetry word `0x41440000` (`0100 0001 0100 0100 0000 0000 0000 0000`), sign bit $S = 0$ indicates a positive value, biased exponent $E = \text{1000 0010}_2 = 130$ gives true exponent $e = 130 - 127 = +3$, and the fractional mantissa bits `.1000100..._2` evaluate to $2^{-1} + 2^{-5} = 0.5 + 0.03125 = 0.53125$, yielding $V_{\text{float}} = +1.53125 \times 2^3 = \mathbf{+12.25^\circ\text{C}}$ (while `0x41480000` $= 1{,}095{,}237{,}632$ decodes via {{key:sc16:FLT}} to $+1.5625 \times 2^3 = \mathbf{+12.50^\circ\text{C}}$, and pressing {{key:sc16:FLT}} on `12.5` encodes back to `1095237632` $= \text{0x41480000}$).

* **Calculator Interface:** Primary Key: {{key:sc16:FLT}} • Expression / Workspace: `IEEE 754 binary32 encode/decode` • Softkeys: {{keycap:FLT}} {{keycap:F16}} {{keycap:F64}}


---

### Eq. 8.2 — Reflected CRC-32 LFSR Step

To detect burst noise on serial sensor buses and Ethernet links, a **Cyclic Redundancy Check** ({{key:sc16:CRC}}) treats a binary message frame as a polynomial over the two-element Galois field $\text{GF}(2)$, where addition and subtraction are both carry-free {{key:sc16:⊕}} ($\oplus$), and computes the remainder modulo a generator polynomial:
- **8-Bit Sensor Bus `CRC8/CCITT` ($G(x) = x^8 + x^2 + x + 1$, Polynomial `0x07`):** For compact 1-wire and RS-485 sensor headers, each bit shift tests the MSB ($b_7$) of the 8-bit accumulator and XORs with `0x07` when $b_7 = 1$.
- **32-Bit Frame CRC-32 ($G_{\text{ref}} = \text{0xEDB88320}$):** For IEEE 802.3 Ethernet and telemetry frames, starting from $C_0 = \text{0xFFFFFFFF} \oplus X$, the reflected Linear Feedback Shift Register (LFSR) shifts right and XORs with `0xEDB88320` whenever the LSB is `1`, followed by final bitwise inversion $\sim C$:

$$C_{i+1} = \begin{cases} (C_i \ggg 1) \oplus G_{\text{poly}} & \text{if } (C_i \ \& \ 1) = 1 \\ C_i \ggg 1 & \text{if } (C_i \ \& \ 1) = 0 \end{cases}$$

Routing telemetry frames from the RS-485 gateway onto the plant Ethernet backbone requires synthesizing CIDR netmasks and host capacities ({{key:sc16:NET}}) and verifying that the $16\times$ oversampled UART baud clock ({{key:sc16:BPS}}) remains within framing tolerance.

* **Calculator Interface:** Primary Key: {{key:sc16:CRC}} • Expression / Workspace: `Reflected CRC-32 LFSR polynomial step` • Softkeys: {{keycap:CRC}} {{keycap:SWP}}


---

### Eq. 8.3 — CIDR Netmask and Usable Host Capacity

In **Classless Inter-Domain Routing** ({{key:sc16:NET}}), an IPv4 subnet prefix {{key:sc16:NET}} ($P \in [0, 32]$) assigns the upper $P$ bits of a 32-bit IPv4 word to the network mask and leaves $32 - P$ bits for host addresses. Pressing {{key:sc16:NET}} with prefix $P$ in Register $X$ evaluates both the **32-bit Netmask** in Register $Y$ and the **Usable Host Count** $N_{\text{hosts}}$ in Register $X$:

$$\text{Netmask}(P) = \left(2^{32} - 2^{32 - P}\right) = \text{0xFFFFFFFF} \ll (32 - P)$$

For a standard `/24` industrial VLAN (`24` {{key:sc16:NET}}), the 32-bit netmask pushed to Register $Y$ is `4294967040` ($\mathbf{\text{0xFFFFFF00}}$, or `255.255.255.0`) and the usable host count in Register $X$ is $2^{32-24} - 2 = \mathbf{254\text{ hosts}}$ (excluding the `.0` network address and `.255` broadcast address).

* **Calculator Interface:** Primary Key: {{key:sc16:NET}} • Expression / Workspace: `IPv4 netmask and host capacity` • Softkeys: {{keycap:NET}} {{keycap:MOD}}


---

### Eq. 8.4 — Sixteen-Times Oversampled UART Baud Divisor

Because a **Universal Asynchronous Receiver/Transmitter** ({{key:sc16:BPS}}) transmits data without a shared clock wire, the receiver oversamples the incoming line at $16$ times the target symbol rate $B$ (in $\text{bits/s}$) so it can align its sample point with the center ($8\text{th}$ tick) of each bit cell. Dividing the peripheral clock $f_{\text{clk}}$ (in Register $Y$) by $16 \cdot B$ ($B$ in Register $X$) and rounding to the nearest integer yields the hardware baud divisor $D$:

$$D = \operatorname{round}\!\left(\frac{f_{\text{clk}}}{16 \cdot B}\right)$$

where $B_{\text{actual}} = f_{\text{clk}} / (16 \cdot D)$. Here $D$ is the integer value written to the baud-rate register via {{key:sc16:BPS}}, $B_{\text{actual}}$ is the synthesized bit rate, and $\text{Err\%}$ is the fractional clock skew (which must remain within $\pm 2.0\%$ over a 10-bit start-data-stop frame to prevent stop-bit framing errors). On our $f_{\text{clk}} = 48\text{ MHz}$ bus targeting $B = 115{,}200\text{ bps}$, keying `48000000` {{key:sc16:ENTER}} `115200` {{key:sc16:BPS}} evaluates $\frac{48{,}000{,}000}{16 \times 115{,}200} = 26.0417$ and rounds to $D = \mathbf{26}$. The actual baud rate is $\frac{48{,}000{,}000}{16 \times 26} \approx \mathbf{115{,}384.6\text{ bps}}$, a clock drift of $+0.16\%$—proving that the UART timing is well within tolerance and the CRC errors were caused by an un-terminated RS-485 bus end rather than baud-rate skew.

* **Calculator Interface:** Primary Key: {{key:sc16:BPS}} • Expression / Workspace: `BPS: D = C / (16 × B)` • Softkeys: {{keycap:D}} {{keycap:C}} {{keycap:B}}


---

### Eq. 9.1 — Pulse-Width Modulation Carrier Frequency

A hardware timer divides the peripheral bus clock $f_{\text{clk}}$ ({{keycap:C}}, in $\text{Hz}$) through an integer **Prescaler** $P$ ({{keycap:P}}) to produce a counter tick clock $f_{\text{tick}} = f_{\text{clk}} / P$, which then counts up to an integer **Auto-Reload Period** $\text{ARR}$ ({{keycap:A}}) to synthesize a **Pulse-Width Modulation** ({{key:sc16:PWM}}) carrier of frequency $f_{\text{PWM}}$ ({{keycap:F}}):

$$f_{\text{PWM}} = \frac{f_{\text{clk}}}{P \cdot \text{ARR}} \iff \text{ARR} = \frac{f_{\text{clk}}}{P \cdot f_{\text{PWM}}}$$

Duty cycle percentage is governed by the capture-compare threshold: $\text{Duty\%} = (\text{CCR} / \text{ARR}) \times 100\%$. On the immediate RPN stack, pressing {{key:sc16:PWM}} with $f_{\text{clk}}$ in Register $Z$, prescaler $P$ in Register $Y$, and auto-reload period $\text{ARR}$ in Register $X$ computes $f_{\text{PWM}} = f_{\text{clk}} / (P \times \text{ARR})$ and opens the **{{key:sc16:PWM}} Equation Solver Workspace** (`F = C / (P × A)`) with variable softkeys {{keycap:F}}, {{keycap:C}}, {{keycap:P}}, and {{keycap:A}}. Driven by a $f_{\text{clk}} = 48\text{ MHz}$ ($48{,}000{,}000\text{ Hz}$) bus clock with prescaler $P = 48$ and auto-reload period $\text{ARR} = 1{,}000$, keying `48000000` {{key:sc16:ENTER}} `48` {{key:sc16:ENTER}} `1000` {{key:sc16:PWM}} generates $f_{\text{PWM}} = \mathbf{1{,}000.0\text{ Hz}}$ ($1.0\text{ kHz}$). Conversely, when upgrading the servo stage to an ultrasonic $F = 20{,}000\text{ Hz}$ ($20\text{ kHz}$) switching frequency on a $C = 168{,}000{,}000\text{ Hz}$ ($168\text{ MHz}$) timer bus with prescaler $P = 4$, solving `F = C / (P × A)` backward for {{keycap:A}} via {{key:sc16:SOLVE}} {{keycap:A}} yields $\text{ARR} = \frac{168{,}000{,}000}{4 \times 20{,}000} = \mathbf{2{,}100\text{ counts}}$.

* **Calculator Interface:** Primary Key: {{key:sc16:PWM}} • Expression / Workspace: `PWM: F = C / (P × A)` • Softkeys: {{keycap:F}} {{keycap:C}} {{keycap:P}} {{keycap:A}}


---

### Eq. 9.2 — Successive-Approximation ADC Quantization

An $N$-bit **Analog-to-Digital Converter** ({{key:sc16:ADC}}) partitions its full-scale reference voltage $V_{\text{ref}}$ into $2^N$ uniform quantization steps of width $V_{\text{LSB}}$ (the Least Significant Bit voltage), mapping a continuous analog input voltage $V_{\text{in}} \in [0, V_{\text{ref}})$ to the integer digital code $D \in [0, 2^N - 1]$ (while {{key:sc16:DAC}} reconstructs $V_{\text{out}}$ from a 12-bit code):

$$V_{\text{LSB}} = \frac{V_{\text{ref}}}{2^N}$$

In these quantization equations, $N$ is the converter resolution in bits, $2^N$ is the total number of discrete code bins ($4{,}096$ for a 12-bit converter or $65{,}536$ for a 16-bit converter), and $V_{\text{LSB}}$ is the smallest voltage change that increments $D$ by $1$. Because ideal uniform quantization introduces a sawtooth error bounded by $\pm\frac{1}{2} V_{\text{LSB}}$ with root-mean-square noise $V_{q,\text{rms}} = V_{\text{LSB}} / \sqrt{12}$, a full-scale sine wave of RMS amplitude $V_{\text{ref}} / (2\sqrt{2})$ achieves a theoretical Signal-to-Noise-and-Distortion ratio $\text{SINAD}_{\text{dB}} = 6.0206 N + 1.7609\text{ dB}$, defining the converter's **Effective Number of Bits**: $\text{ENOB} = (\text{SINAD}_{\text{dB}} - 1.7609) / 6.0206$.

* **Calculator Interface:** Primary Key: {{key:sc16:ADC}} • Expression / Workspace: `ADC: D = V / R × 2^N` • Softkeys: {{keycap:D}} {{keycap:V}} {{keycap:R}} {{keycap:N}}


---

### Eq. 9.3 — Resistor-Capacitor Filter Cutoff and Exponential Settling

To prevent front-end charge-injection droop from degrading $\text{ENOB}$, the external RC anti-aliasing and sample-and-hold network ({{key:sc16:τ}}) of time constant $\tau = R C$ and $-3\text{ dB}$ cutoff frequency $f_c$ must settle following an input step until tracking error falls below half an LSB:

$$\tau = R \cdot C$$

Full settling requires $t_{\text{acq}} \ge (N + 1)\ln(2)\,\tau$, or at least $9.01$ time constants for a 12-bit converter. On our vibration node's 12-bit {{key:sc16:ADC}} with reference $V_{\text{ref}} = 3.30\text{ V}$, the step size is $V_{\text{LSB}} = 3.30 / 4096 \approx \mathbf{0.80566\text{ mV/LSB}}$ ($805.66\ \mu\text{V}$), a DC bias input of $V_{\text{in}} = 1.65\text{ V}$ maps to mid-scale code $D = \lfloor (1.65 / 3.30) \times 4096 \rfloor = \mathbf{2{,}048}$ (`0x800`), and a live DMA register sample $D = 2{,}894$ (`0xB4E`) inverts in the {{key:sc16:ADC}} workspace (`D = V / R × 2^N`, softkeys {{keycap:D}}, {{keycap:V}}, {{keycap:R}}, {{keycap:N}}) to $V_{\text{in}} = 2894 \times 3.30 / 4096 = \mathbf{2.3316\text{ V}}$.

* **Calculator Interface:** Primary Key: {{key:sc16:τ}} • Expression / Workspace: `RC anti-aliasing cutoff and settling` • Softkeys: {{keycap:τ}} {{keycap:fc}}


---

### Eq. 9.4 — Classless Inter-Domain Routing Host Capacity

In **Classless Inter-Domain Routing** ({{key:sc16:NET}}), a 32-bit IPv4 address written with prefix length {{key:sc16:NET}} ($P \in [0, 32]$) allocates the upper $P$ bits to the fixed **Network Prefix** (where the subnet mask pushed to Register $Y$ has {{key:sc16:#B}} $= P$ leading `1` bits) and leaves $H = 32 - P$ bits for **Host Addresses**:

$$\text{Block Size} = 2^{32 - P}$$

Because the all-zeros host pattern ($0$) is reserved for the **Subnet Network ID** and the all-ones host pattern ($2^{32-P} - 1$) is reserved for the **Subnet Broadcast Address**, pressing {{key:sc16:NET}} on a {{key:sc16:NET}} prefix pushes the 32-bit netmask to Register $Y$ and $N_{\text{hosts}} = 2^{32 - P} - 2$ usable **Host Addresses** to Register $X$. For our factory floor `/26` subnet (`26` {{key:sc16:NET}}, leaving $H = 6$ host bits and fourth-octet mask $256 - 2^6 = 192$, or `255.255.255.192` $= \text{0xFFFFFFC0}$), the total block size is $2^6 = 64$ addresses and the usable capacity is $N_{\text{hosts}} = 64 - 2 = \mathbf{62\text{ usable hosts}}$—accommodating all $54$ vibration nodes and the `.200` gateway with $7$ addresses to spare. Because $\lfloor 200 / 64 \rfloor \times 64 = 3 \times 64 = 192$, the `192.168.10.200/26` block starts at Network ID `192.168.10.192`, spans usable hosts `192.168.10.193` through `192.168.10.254`, and terminates at Broadcast Address `192.168.10.255`.

* **Calculator Interface:** Primary Key: {{key:sc16:NET}} • Expression / Workspace: `CIDR subnet host block sizing` • Softkeys: {{keycap:NET}} {{keycap:#B}} {{keycap:CLZ}}


---

### Eq. 9.5 — Natural Power-of-Two Memory Bus Alignment

Inside system memory, CPU load/store units and DMA engines require packet descriptors to begin at byte addresses $A$ divisible by a power-of-two **Alignment Boundary** $B \in \{2, 4, 8, 16, 32, 64, 4096\}$ ({{key:sc16:ALN}}), or round a minimum ring-buffer size $S$ up to the next power of two $S_{\text{pow2}}$, with binary storage keys ({{key:sc16:▸B}}, {{key:sc16:▸bit}}, {{key:sc16:▸KiB}}, {{key:sc16:▸MiB}}, {{key:sc16:▸GiB}}, {{key:sc16:▸TiB}}) converting between raw bit counts and IEC power-of-two byte capacities ($1\text{ KiB} = 2^{10} = 1{,}024\text{ B}$):

$$A_{\text{aligned}} = \left\lceil \frac{A}{B} \right\rceil \times B = (A + B - 1) \ \& \ \sim(B - 1)$$

Here $(A + B - 1) \ \& \ \sim(B - 1)$ clears the lower $\log_2 B$ address bits to round $A$ up to the next multiple of $B$. Aligning our vibration node's raw 53-byte packet descriptor ($A = 53$) up to a $B = 16\text{-byte}$ DMA burst boundary via `53` {{key:sc16:ENTER}} `16` {{key:sc16:ALN}} yields $A_{\text{aligned}} = \lceil 53 / 16 \rceil \times 16 = 4 \times 16 = \mathbf{64\text{ bytes}}$, while rounding a $300\text{-byte}$ circular sample queue up to the next power of two via `0` {{key:sc16:ENTER}} `300` {{key:sc16:ALN}} yields $S_{\text{pow2}} = 2^9 = \mathbf{512\text{ bytes}}$ ($0.5\text{ KiB}$ via {{key:sc16:▸KiB}}).

* **Calculator Interface:** Primary Key: {{key:sc16:ALN}} • Expression / Workspace: `Power-of-two memory address alignment` • Softkeys: {{keycap:ALN}} {{keycap:▸KiB}}


---

### Eq. 9.6 — High-Speed Synchronous Bus Timing Margins

In high-speed synchronous serial interfaces such as SPI buses, data transfer is referenced to a master clock of period $T_{\text{clk}} = 1 / f_{\text{clk}}$. To guarantee that the receiving flip-flop latches transmitted bits without entering metastability, two timing margins must remain strictly non-negative across worst-case thermal and supply voltage variations:

$$t_{\text{margin,setup}} = T_{\text{clk}} - t_{\text{co,\max}} - t_{\text{prop,\max}} - t_{su} \ge 0$$

$$t_{\text{margin,hold}} = t_{\text{co,\min}} + t_{\text{prop,\min}} - t_h - \Delta t_{\text{skew}} \ge 0$$

Here $t_{su}$ is the required data setup time, $t_h$ is the required data hold time, $t_{\text{co}}$ is the transmitter clock-to-output propagation delay, $t_{\text{prop}}$ is the PCB trace flight time (roughly $160\text{ ps/in}$ on FR-4), and $\Delta t_{\text{skew}}$ is the clock skew. Crucially, hold time violations cannot be cured by reducing clock frequency, demanding careful matching of trace lengths and series damping resistance.

* **Calculator Interface:** Primary Key: Bus Margin Evaluation on Stack (`-`, `+`) • Expression / Workspace: `Stack: T_clk in Z, delays in Y, subtract to find margin` • Softkeys: {{keycap:-}} {{keycap:+}}


---


## Unit IV: Cinema Optics, Broadcast Timecode, and Sound

The **SC-24** provides dedicated faceplate keys and bidirectional Equation Solver workspaces to execute the governing laws of this domain. Each equation is indexed below with its physical motivation, governing formula, and operational calculator softkeys.

### Eq. 10.1 — Sexagesimal Timecode Expansion and Integer Frame Accumulation

To translate between human clock-face notation and raw discrete frame counts, the time address is decomposed hierarchically. Hours are multiplied by thirty-six hundred seconds, minutes by sixty seconds, and whole seconds are added directly, while the trailing frame counter is divided by the project frame rate $R$ to represent the fractional second. Multiplying that continuous time duration by the frame rate accumulates the exact total number of discrete frames exposed since midnight:

$$S = 3600 \cdot \text{HH} + 60 \cdot \text{MM} + \text{SS} + \frac{\text{FF}}{R}$$

Here $S$ is the elapsed duration in seconds ($\text{s}$), $R$ is the frame rate in frames per second ($\text{fps}$), and $F$ is the exact count of frames since `00:00:00:00`. When adding ({{key:sc24:+TC}}) or subtracting ({{key:sc24:-TC}}) two packed timecode durations $A$ and $B$, arithmetic proceeds from right to left across the four radices, carrying $+1\text{ second}$ whenever the frame sum reaches or exceeds $R$, carrying $+1\text{ minute}$ whenever seconds reach $60$, and carrying $+1\text{ hour}$ whenever minutes reach $60$.

* **Calculator Interface:** Primary Key: {{key:sc24:TC}} • Expression / Workspace: `SMPTE timecode sexagesimal frame expansion` • Softkeys: {{keycap:TC}} {{keycap:FPS}}


---

### Eq. 10.2 — Overcrank Speed Magnification and Shutter Exposure Deficit

Because every captured frame must be displayed during playback, the total frame count $F_{\text{total}}$ is conserved across timebases. The speed ramp magnification factor is simply the ratio of acquisition frame rate to projection frame rate: capturing at five times the playback rate stretches physical time fivefold on screen. Because higher frame rates force each individual frame shutter to open for a shorter fraction of a second, the camera sensor receives fewer photons per frame. In photographic exposure, each factor-of-two reduction in integration time represents one full stop of exposure loss; taking the base-two logarithm of the speed ratio yields the exact exposure deficit in Exposure Value stops that must be compensated on set:

$$M_{\text{ramp}} = \frac{R_{\text{shoot}}}{R_{\text{play}}}$$

In these relations, $R_{\text{play}}$ is the base delivery timeline frame rate staged in Register $Y$ (such as $24\text{ fps}$), $R_{\text{shoot}}$ is the camera sensor acquisition rate staged in Register $X$ (such as $60\text{ fps}$ or $120\text{ fps}$), $M_{\text{ramp}}$ is the dimensionless slow-motion playback factor deposited in Register $X$ by {{key:sc24:FPS}}, and $\Delta\text{EV}_{\text{fps}}$ is the exposure stop loss deposited in Register $Y$ by {{key:sc24:FPS}} (because raising the frame rate at a fixed rotary shutter angle shortens each frame's integration time proportionally).

* **Calculator Interface:** Primary Key: {{key:sc24:FPS}} • Expression / Workspace: `Overcrank speed ramp magnification` • Softkeys: {{keycap:FPS}} {{keycap:SHT}}


---

### Eq. 10.3 — NTSC Color Pulldown and Wall-Clock Drift Rate

Because the video frame rate is dialed back by exactly one part in a thousand, each broadcast second takes one thousand and one thousandths of a physical second to pass. A counter that increments thirty whole frames per second therefore lags behind atomic wall-clock time by exactly one tenth of a percent: one second of drift every thousand seconds, accumulating three point six seconds of wall-clock lag across every nominal broadcast hour:

$$R_{\text{NTSC}} = \frac{30}{1.001} = \frac{30{,}000}{1001} \approx 29.97003\text{ fps}$$

In this pulldown relationship, $t_{\text{nominal}} = F / 30$ is the apparent duration indicated by a Non-Drop-Frame (NDF) counter that increments one second every $30$ frames, $t_{\text{real}} = F / R_{\text{NTSC}}$ is the true wall-clock elapsed time in seconds ({{key:sc24:DF}}), and $\Delta t_{\text{drift}} = t_{\text{real}} - t_{\text{nominal}}$ is the cumulative clock error. Similarly, when theatrical $24\text{ fps}$ cinema masters are transferred to NTSC video via $2:3$ telecine pulldown ({{key:sc24:3:2}}), the cinema frame rate is pulled down by $1000/1001$ to $24 / 1.001 \approx 23.976024\text{ fps}$.

* **Calculator Interface:** Primary Key: {{key:sc24:DF}} • Expression / Workspace: `NTSC 29.97 color pulldown clock drift` • Softkeys: {{keycap:DF}} {{keycap:TC}}


---

### Eq. 10.4 — SMPTE Drop-Frame Label Skip and Physical Frame Index

To maintain perfect synchronization without discarding recorded footage, the display skips frame label numbers rather than physical images. Skipping two numbers on nine minutes out of ten, while retaining every number on decade minutes (zero, ten, twenty, thirty, forty, and fifty), drops exactly one hundred eight labels an hour. The physical frame index is evaluated by accumulating one hundred seven thousand eight hundred ninety-two frames per hour, seventeen hundred ninety-eight frames per minute, and adding back two frames for every decade minute boundary:

$$N_{\text{dropped}} = 2 \times \left(M_{\text{total}} - \left\lfloor \frac{M_{\text{total}}}{10} \right\rfloor\right)$$

Here $M_{\text{total}} = 60 \cdot \text{HH} + \text{MM}$ is the total number of elapsed minute boundaries, $N_{\text{dropped}}$ is the cumulative count of skipped frame numbers (labels `:00` and `:01` omitted at the start of every minute except minutes `00`, `10`, `20`, `30`, `40`, and `50`), and $F_{\text{DF}}$ is the exact physical frame index corresponding to a Drop-Frame address `HH:MM:SS;FF` (written by convention with a semicolon before the frame field).

* **Calculator Interface:** Primary Key: {{key:sc24:TC}} • Expression / Workspace: `SMPTE drop-frame label skip compensation` • Softkeys: {{keycap:TC}} {{keycap:+TC}} {{keycap:-TC}}


---

### Eq. 11.1 — Rectilinear Field of View and Scene Coverage

The optical axis bisects the horizontal width $W$ (in $\text{mm}$) of the active sensor or film aperture into two congruent right triangles, each having an opposite leg of half-width $W / 2$ and an adjacent leg of focal length $F$. The ratio of half the sensor width to the focal length forms the tangent of half the angular field of view. The inverse tangent asks what angle produces that specific geometric ratio; doubling that angle yields the full horizontal field of view across the scene:

$$A = 2 \arctan\left(\frac{W}{2F}\right)$$

In these expressions, $W$ is the active horizontal sensor width in $\text{mm}$, $F$ is the lens focal length in $\text{mm}$, $A$ is the horizontal coverage angle in degrees, $s$ is the subject distance along the optical axis, and $K_{\text{crop}}$ scales focal length to its $35\text{ mm}$ Full-Frame ({{key:sc24:▸35}}, $K_{\text{crop}} \approx 1.5\times$ from Super 35) or Super 16 ({{key:sc24:▸16}}, $K_{\text{crop}} \approx 2.88\times$) equivalent angle of view ($F_{\text{equiv}} = F \times K_{\text{crop}}$).

* **Calculator Interface:** Primary Key: {{key:sc24:FOV}} • Expression / Workspace: `FOV: A = 2 × ATAN(W / (2 × F))` • Softkeys: {{keycap:A}} {{keycap:W}} {{keycap:F}}


---

### Eq. 11.2 — Hyperfocal Distance and Conjugate Depth-of-Field Boundaries

Because human visual acuity is finite when viewing a theater screen from a standard seating distance, any blur disk smaller than a critical diameter $C$ (standardized at $C = 0.029\text{ mm}$–$0.030\text{ mm}$ for $35\text{ mm}$ Full-Frame reference gates and $C = 0.025\text{ mm}$ for Super 35 cinema work) appears indistinguishable from a sharp point. The hyperfocal distance is the focus setting that extends acceptable sharpness all the way to optical infinity. It scales with the square of focal length and inversely with the aperture f-number and the permissible Circle of Confusion. Once the hyperfocal distance is known, the near and far limits of acceptable focus form harmonic conjugates around the subject distance. The near limit divides the product of hyperfocal distance and subject distance by their sum, while the far limit divides their product by their difference. When the subject distance reaches the hyperfocal mark, the difference in the denominator becomes zero, pushing the far focus limit out to infinity:

$$H = \frac{F^2}{N \cdot C}$$

Here $F$ is the focal length in $\text{mm}$, $N$ is the f-stop number, $C$ is the Circle of Confusion diameter in $\text{mm}$, $H$ is the hyperfocal distance (in $\text{mm}$ in the {{key:sc24:DOF}} solver workspace, or divided by $1000$ in meters on the immediate stack), and $s$ is the focus distance in the same length units as $H$. When the focus ring is set directly to the hyperfocal mark ($s = H$), the denominator of $D_{\text{far}}$ vanishes ($H - H = 0 \implies D_{\text{far}} \to \infty$) while $D_{\text{near}}$ reduces to $H^2 / (2H) = H / 2$, rendering everything from half the hyperfocal distance to the horizon acceptably sharp.

* **Calculator Interface:** Primary Key: {{key:sc24:DOF}} • Expression / Workspace: `DOF: H = F² / (N × C)` • Softkeys: {{keycap:H}} {{keycap:F}} {{keycap:N}} {{keycap:C}}


---

### Eq. 11.3 — Exposure Value, Rotary Shutter Integration, and Neutral Density

In photography, Exposure Value unifies aperture and shutter time onto a base-two scale. The square of the lens f-number measures the geometric light constriction of the iris. Dividing that squared f-number by the exposure time in seconds gives the relative light demand; taking the base-two logarithm measures this demand in discrete exposure stops. For a cinema camera with a spinning rotary disk shutter, the open shutter angle represents the fraction of a complete three-hundred-sixty-degree circle during which the sensor is exposed. For neutral-density filters, each optical density step of zero point three corresponds to a factor-of-two reduction in transmitted light—one full exposure stop—matching the base-ten logarithm of two:

$$E = \log_2\left(\frac{N^2}{T}\right)$$

In these photometric equations, $N$ is the lens f-number, $T$ is the exposure integration time in seconds, $E$ is the Exposure Value ($\text{EV}_{100}$), $\theta_{\text{shutter}} \in (0^\circ, 360^\circ]$ is the rotary shutter angle, $D$ is the dimensionless neutral-density filter rating ({{key:sc24:▸ND}} converts stops $s$ in Register $X$ into optical density $D = 0.3 \times s$ in Register $X$ and filter factor $2^s$ in Register $Y$), and $T_{\text{trans}} = 2^{-\text{stops}} = 10^{-D}$ is the fractional light transmittance. In cinematography optics, depth of field depends on geometric aperture ($f$-stop $N = f/D$), whereas exposure irradiance depends on photometric transmittance ($T$-stop $T_{\text{stop}} = N / \sqrt{\tau_{\text{trans}}}$).

* **Calculator Interface:** Primary Key: {{key:sc24:EV}} • Expression / Workspace: `EV: N² = T × 2^E` • Softkeys: {{keycap:E}} {{keycap:N}} {{keycap:T}} {{keycap:▸ND}}


---

### Eq. 11.4 — Flicker-Free Shutter Angle and Integration Period

When filming under alternating-current discharge lamps or LED drivers operating at line frequency $f_{\text{line}}$ ($60\text{ Hz}$ in North America or $50\text{ Hz}$ in Europe), the lamp intensity pulses at twice the utility line frequency ($2 f_{\text{line}}$: $120\text{ Hz}$ or $100\text{ Hz}$). Avoiding rolling exposure bands across the frame ({{key:sc24:FLK}}) requires choosing a shutter integration time $T$ that integrates an integer number $k \in \{1, 2, 3, \dots\}$ of half-cycles:

$$T_{\text{flicker-free}} = \frac{k}{2 f_{\text{line}}}$$

$$\theta_{\text{flicker-free}} = 360^\circ \cdot \text{FPS} \cdot \left(\frac{k}{2 f_{\text{line}}}\right)$$

Under North American $60\text{ Hz}$ mains ($120\text{ Hz}$ pulses), shooting at $24\text{ fps}$ with $k = 2$ half-cycles sets $T = 1/60\text{ s}$ ($\theta_{\text{shutter}} = 144^\circ$). Under European $50\text{ Hz}$ mains ($100\text{ Hz}$ pulses), shooting at $24\text{ fps}$ requires an exact integration time of $T = 1/50\text{ s} = 20.0\text{ ms}$, corresponding to the classic European flicker-free rotary shutter angle of $\theta_{\text{shutter}} = \mathbf{172.8^\circ}$.

* **Calculator Interface:** Primary Key: {{key:sc24:SHT}} / {{key:sc24:FLK}} • Expression / Workspace: `SHT: T = θ / (360 × FPS)` • Softkeys: {{keycap:SHT}} {{keycap:FLK}}


---

### Eq. 11.5 — Inverse-Square Illuminance and Micro-Reciprocal Degree Gel Shift

As light radiates from a fixture, its radiant power spreads across an expanding spherical wavefront whose surface area grows with the square of distance. Consequently, illuminance in lux falls off inversely with the square of throw distance. For color temperature, human perception does not see equal Kelvin differences equally: a five-hundred Kelvin shift at warm tungsten temperatures creates a dramatic visual amber cast, whereas the same shift at high daylight temperatures is barely noticeable. Converting absolute Kelvin temperature into its reciprocal multiplied by one million—termed micro-reciprocal degrees or Mireds ($M = 10^6 / T_K$)—makes color filtration additive across the spectrum. Subtracting the source Mired value from the target Mired value specifies the exact corrective gel shift:

$$E_{\text{lx}} = \frac{I}{D^2}$$

Here a positive shift ($\Delta M > 0$) calls for an amber **Color Temperature Orange** (CTO) gel to warm a daylight source toward tungsten, whereas a negative shift ($\Delta M < 0$) calls for a blue **Color Temperature Blue** (CTB) gel to cool a $T_{\text{source}} = 3200\text{ K}$ tungsten lamp ($M_{\text{source}} = 10^6 / 3200 = 312.50\text{ Mireds}$) up to $T_{\text{target}} = 5600\text{ K}$ daylight ($M_{\text{target}} = 10^6 / 5600 = 178.57\text{ Mireds}$), yielding $\Delta M = 178.57 - 312.50 = \mathbf{-133.93\text{ Mireds}}$ (a Full CTB gel).

* **Calculator Interface:** Primary Key: {{key:sc24:LUX}} • Expression / Workspace: `LUX: E = I / D²` • Softkeys: {{keycap:E}} {{keycap:I}} {{keycap:D}} {{keycap:▸fc}}


---

### Eq. 12.1 — Thermal Speed of Sound and Acoustic Propagation Delay

Sound is a mechanical pressure wave passed from air molecule to air molecule. Because higher temperatures increase the thermal speed of gas molecules, the speed of sound rises linearly with temperature, starting at three hundred thirty-one point three meters per second at freezing and adding roughly zero point six meters per second for every degree Celsius of warmth. The acoustic transit time across a venue is simply distance divided by velocity; multiplying by one thousand converts seconds into milliseconds. Dividing sound speed by the acoustic frequency yields the physical wavelength—the spatial distance between adjacent compression peaks:

$$v_s(T_C) = 331.3 + 0.606 \cdot T_C \quad \left[\frac{\text{m}}{\text{s}}\right]$$

In these expressions, $T_C$ is the ambient air temperature in degrees Celsius ($^\circ\text{C}$), $v_s$ is the acoustic phase velocity in $\text{m/s}$ (evaluating to $343.42\text{ m/s} \approx 343\text{ m/s}$ at the standard $20^\circ\text{C}$ room reference recalled by {{key:sc24:vₛ}}), $d$ is the physical distance from the main stage array to the delay tower in meters, $\Delta t_{\text{ms}}$ is the acoustic transit delay in milliseconds ($\text{ms}$), and $\lambda$ is the physical wavelength in meters.

* **Calculator Interface:** Primary Key: {{key:sc24:vₛ}} • Expression / Workspace: `Thermal speed of sound and DSP delay` • Softkeys: {{keycap:vₛ}} {{keycap:DLY}}


---

### Eq. 12.2 — Sabine Reverberation Time

In an enclosed room, sound bounces repeatedly between boundaries, creating a decaying reverberant field. Wallace Clement Sabine's 1898 architectural law states that the time needed for reverberant sound energy to drop by sixty decibels—one millionth of its original power—is directly proportional to the total enclosed air volume and inversely proportional to the total acoustic absorption in metric sabins:

$$RT_{60} = \frac{0.161 \cdot V}{A} = \frac{0.161 \cdot V}{\sum_{i} S_i \alpha_i}$$

For a broadcast studio of volume $V = 2400\text{ m}^3$ treated with acoustic baffles providing $A = 480\text{ metric sabins}$ of absorption, Sabine's formula predicts a tight decay time of $RT_{60} = (0.161 \times 2400) / 480 = \mathbf{0.805\text{ s}}$, while an $f = 68.6\text{ Hz}$ bass note at $v_s = 343\text{ m/s}$ has an acoustic wavelength of $\lambda = 343 / 68.6 = \mathbf{5.00\text{ m}}$ (`68.6` {{key:sc24:λ}}).

* **Calculator Interface:** Primary Key: {{key:sc24:EQN}} • Expression / Workspace: `Sabine reverberation decay time` • Softkeys: `V` `A`


---

### Eq. 12.3 — Spherical Spreading Attenuation and Acoustic Reach

On the logarithmic decibel scale, the attenuation equals twenty times the base-ten logarithm of the distance ratio. Every doubling of distance reduces sound pressure level by six decibels:

$$L_2 = L_1 - 20 \log_{10}\left(\frac{D_2}{D_1}\right)$$

Here $L_1$ is the known Sound Pressure Level in $\text{dBSPL}$ at reference distance $D_1$, and $L_2$ is the Sound Pressure Level at distance $D_2$ (when called with two arguments $D_1$ in $Y$ and $D_2$ in $X$, {{key:sc24:SPL}} returns the relative decibel attenuation $\Delta L = -20\log_{10}(D_2 / D_1)$). Every doubling of distance ($D_2 / D_1 = 2$) reduces sound pressure level by $20\log_{10}(2) \approx \mathbf{6.0206\text{ dB}}$.

* **Calculator Interface:** Primary Key: {{key:sc24:SPL}} • Expression / Workspace: `Spherical acoustic inverse-square decay` • Softkeys: {{keycap:SPL}} {{keycap:dB}}


---

### Eq. 12.4 — Incoherent Acoustic Decibel Addition and Studio Voltage Levels

When independent sound sources radiate into the same space, their pressure waves do not interfere coherently; instead, their acoustic energies add together. To sum two decibel levels, each is divided by ten and raised as a power of ten to recover its linear acoustic power. These powers are added together, and taking ten times the base-ten logarithm yields the combined decibel level. Combining two identical uncorrelated sources always produces a three-decibel increase, reflecting a doubling of total radiated power:

$$L_{\Sigma,\text{incoherent}} = 10 \log_{10}\left(10^{L_1 / 10} + 10^{L_2 / 10}\right)$$

In broadcast audio transmission, electrical peak decibels are monitored alongside integrated Loudness Units relative to Full Scale (LUFS / LKFS under ITU-R BS.1770 and EBU R128), applying K-weighting acoustic filters and gating algorithms to target $-24\text{ LUFS}$ for television broadcast and $-14\text{ LUFS}$ for commercial streaming.

* **Calculator Interface:** Primary Key: {{key:sc24:dB}} • Expression / Workspace: `Incoherent acoustic decibel power summation` • Softkeys: {{keycap:dB}} {{keycap:SPL}}


---


## Unit V: RF Spectrum, Transmission Lines, and Microwave

The **SC-50** provides dedicated faceplate keys and bidirectional Equation Solver workspaces to execute the governing laws of this domain. Each equation is indexed below with its physical motivation, governing formula, and operational calculator softkeys.

### Eq. 13.1 — Decibel-Milliwatt Power Scaling and Root-Mean-Square Line Voltage

Because radio signal powers range across many orders of magnitude, power is expressed logarithmically relative to one milliwatt. Taking ten times the base-ten logarithm of milliwatt power converts linear watts into decibel-milliwatts. Across a transmission line of characteristic impedance $Z_0$, root-mean-square radio-frequency voltage follows Ohm's law, equaling the square root of the power in watts multiplied by the impedance:

$$P_{\text{dBm}} = 10 \log_{10}\left(\frac{P_{\text{mW}}}{1\text{ mW}}\right) = 10 \log_{10}(P_{\text{W}}) + 30$$

In these expressions, $P_{\text{dBm}}$ is the absolute power level in $\text{dBm}$, $P_{\text{mW}}$ is linear power in milliwatts, $P_{\text{W}} = P_{\text{mW}} / 1000$ is linear power in watts, and $Z_0$ is the transmission-line characteristic impedance in ohms ($\Omega$, standardized at $50\ \Omega$ for transmitters and $75\ \Omega$ for video/broadcast coax).

* **Calculator Interface:** Primary Key: {{key:sc50:dBm}} • Expression / Workspace: `Decibel-milliwatt logarithmic power` • Softkeys: {{keycap:dBm}} {{keycap:▸dBm}} {{keycap:▸dBW}}


---

### Eq. 13.2 — Complex Voltage Reflection Coefficient and Standing Wave Ratio

When a guided electromagnetic wave encounters an antenna whose complex impedance differs from the line's characteristic impedance, the boundary conditions of electromagnetism demand that a fraction of the voltage reflect backward. The complex reflection coefficient divides the difference between load impedance and characteristic impedance by their sum. Its magnitude measures the fraction of voltage reflected, while its angle reveals the phase shift:

$$\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0} = |\Gamma| \angle \theta$$

For a load impedance $Z_L = 75 + j50\ \Omega$ on a $Z_0 = 50\ \Omega$ line, {{key:sc50:Γ}} computes $\Gamma = \frac{25 + j50}{125 + j50} \approx 0.3846 + j0.2462$ with magnitude $|\Gamma| = \mathbf{0.4564}$, yielding standing wave ratio $\text{VSWR} = \frac{1 + 0.4564}{1 - 0.4564} \approx \mathbf{2.68\text{ : } 1}$ via {{key:sc50:SWR}}.

* **Calculator Interface:** Primary Key: {{key:sc50:Γ}} • Expression / Workspace: `Complex reflection coefficient and VSWR` • Softkeys: {{keycap:Γ}} {{keycap:SWR}} {{keycap:Z₀}}


---

### Eq. 13.3 — Return Loss and Mismatch Loss

As the reflected voltage wave $V^-$ travels backward and superposes with the incident wave $V^+$, constructive interference produces stationary voltage peaks while destructive interference produces voltage troughs. The ratio of peak to trough voltage is the VSWR. Expressing the fraction of power reflected in decibels yields the Return Loss: twenty times the negative base-ten logarithm of reflection magnitude. Higher return loss means less reflected power and a better match. The reduction in forward power delivered into the antenna is Mismatch Loss, evaluated from ten times the negative base-ten logarithm of one minus the reflected power fraction:

$$\text{RL}_{\text{dB}} = -20 \log_{10}|\Gamma|$$

On real high-frequency transmission lines, distributed series conductor resistance from the radio-frequency skin effect and shunt dielectric conductance attenuate traveling waves exponentially as $e^{-\alpha z}$. In the complex plane, the Smith chart maps reflection coefficient $\Gamma = |\Gamma|e^{j\theta}$ directly to normalized impedance, where line attenuation causes impedance trajectories to spiral inward toward the $50\ \Omega$ center as reflected power diminishes.

* **Calculator Interface:** Primary Key: {{key:sc50:RL}} • Expression / Workspace: `Return loss and mismatch loss` • Softkeys: {{keycap:RL}} {{keycap:SWR}}


---

### Eq. 13.4 — High-Frequency Conductor Skin Depth

In alternating-current circuits at radio and microwave frequencies, oscillating magnetic fields induce localized eddy currents that oppose current flow in the conductor interior, crowding the alternating current toward the outer perimeter. The characteristic depth at which current density drops to $1/e$ ($\approx 36.8\%$) of its surface value is the **Skin Depth** ($\delta$):

$$\delta = \sqrt{\frac{\rho}{\pi f \mu}} = \sqrt{\frac{1}{\pi f \sigma \mu_0 \mu_r}}$$

At $f = 6\text{ GHz}$ ($6 \times 10^9\text{ Hz}$), the skin depth in copper ($\rho \approx 1.68 \times 10^{-8}\ \Omega\cdot\text{m}$) contracts to $\delta \approx \mathbf{0.85\ \mu\text{m}}$. Because over $98\%$ of the RF current travels within $4\delta \approx 3.4\ \mu\text{m}$, microwave waveguides and coaxial center conductors utilize micro-inch silver electroplating ($50\text{--}100\ \mu\text{in}$) over lightweight structural brass or aluminum rather than solid precious metal.

* **Calculator Interface:** Primary Key: Conductor Skin Depth on Stack (`√`, `÷`, `×`) • Expression / Workspace: `Stack: f in Y, resistivity in X, solve for δ` • Softkeys: {{keycap:√x}} {{keycap:÷}} {{keycap:×}}


---

### Eq. 13.5 — Quarter-Wave Matching Transformer and Physical Stub Length

To match a source impedance to a load resistance, a quarter-wave section's characteristic impedance must equal the geometric mean of the two port impedances. The physical length of the stub equals one quarter of the free-space wavelength scaled by the cable's velocity factor:

$$\ell_{\lambda/4} = \frac{\lambda}{4} \cdot \text{VF} = \frac{c}{4 f} \cdot \text{VF}$$

Here $f_{\text{MHz}}$ is the operating frequency in megahertz, $\lambda = c/f = 299.792458 / f_{\text{MHz}}\text{ m}$ is the free-space wavelength in meters, $\text{VF} = 1 / \sqrt{\varepsilon_r}$ is the coaxial cable velocity factor, and $Z_{\text{match}}$ is the geometric-mean characteristic impedance in ohms. At the repeater frequency of $f = 146.0\text{ MHz}$, the free-space wavelength is $\lambda = 299.792458 / 146.0 \approx \mathbf{2.0534\text{ m}}$ and a free-space quarter-wave whip measures $\ell_{\lambda/4} = 2.0534 / 4 \approx \mathbf{0.5133\text{ m}}$ ($51.33\text{ cm}$). Cut from foam-dielectric coaxial cable with velocity factor $\text{VF} = 0.82$, the physical quarter-wave stub length is $0.5133 \times 0.82 \approx \mathbf{0.4209\text{ m}}$ ($42.1\text{ cm}$). To match a $Z_S = 50\ \Omega$ line to a $Z_L = 112.5\ \Omega$ antenna resistance, the required quarter-wave section impedance is $Z_{\text{match}} = \sqrt{50 \times 112.5} = \sqrt{5625} = \mathbf{75.0\ \Omega}$, allowing standard $75\ \Omega$ video coax to serve as an exact quarter-wave transformer.

* **Calculator Interface:** Primary Key: {{key:sc50:TLN}} • Expression / Workspace: `Quarter-wave transformer stub length` • Softkeys: {{keycap:TLN}} {{keycap:λ/L}}


---

### Eq. 13.6 — L-Network Matching Reactances and LC Resonance

The circuit's operating quality factor $Q$ is the square root of the ratio of high resistance to low resistance minus one. The required series reactance equals the quality factor times the lower resistance, while the shunt reactance equals the higher resistance divided by the quality factor. In resonant LC circuits, inductive and capacitive reactances cancel at the resonant frequency $f_0$:

$$Q = \sqrt{\frac{R_{\text{high}}}{R_{\text{low}}} - 1}$$

Consider matching our repeater's resistive component $R_{\text{low}} = 35\ \Omega$ up to $R_{\text{high}} = 50\ \Omega$ at $f = 146.0\text{ MHz}$. The required nodal quality factor is $Q = \sqrt{(50 / 35) - 1} = \sqrt{0.42857} \approx \mathbf{0.6547}$, which specifies a net series inductive reactance of $|X_{\text{series}}| = 0.6547 \times 35 \approx \mathbf{22.91\ \Omega}$ and a shunt capacitive reactance of $|X_{\text{shunt}}| = 50 / 0.6547 \approx \mathbf{76.38\ \Omega}$. Because the iced antenna already exhibits $-j25\ \Omega$ of series capacitive reactance, the series inductor must simultaneously cancel that $-25\ \Omega$ reactance and supply $+22.91\ \Omega$ of net inductive reactance, requiring a total inductive reactance of $X_L = 25 + 22.91 = \mathbf{47.91\ \Omega}$ ($L = 47.91 / (2\pi \times 146 \times 10^6) \approx \mathbf{52.23\text{ nH}}$) paired with a shunt capacitor of $C = 1 / (2\pi \times 146 \times 10^6 \times 76.38) \approx \mathbf{14.27\text{ pF}}$. Similarly, when stepping a $R_{\text{low}} = 10\ \Omega$ power-transistor collector up to $R_{\text{high}} = 50\ \Omega$, the nodal quality factor is $Q = \sqrt{(50/10) - 1} = \mathbf{2.00}$, giving $|X_{\text{series}}| = \mathbf{20.0\ \Omega}$ and $|X_{\text{shunt}}| = \mathbf{25.0\ \Omega}$.

* **Calculator Interface:** Primary Key: {{key:sc50:f₀}} • Expression / Workspace: `F0: F = 1 / (2π√(L×C))` • Softkeys: {{keycap:F}} {{keycap:L}} {{keycap:C}}


---

### Eq. 14.1 — Friis Free-Space Path Loss

In free space, an isotropic antenna radiates power over an expanding sphere of area four pi times distance squared. Because the receiving antenna's effective capture area shrinks with the square of wavelength, the received power fraction falls with the square of distance and the square of frequency. Expressed in decibels with distance in kilometers and frequency in megahertz, Friis's free-space path loss formula adds twenty times the base-ten logarithm of distance, twenty times the logarithm of frequency, and thirty-two point forty-four decibels:

$$\text{FSPL}_{\text{dB}} = 20 \log_{10}(d_{\text{km}}) + 20 \log_{10}(f_{\text{MHz}}) + 32.44$$

In this expression, $d_{\text{km}}$ is the line-of-sight hop distance in kilometers, $f_{\text{MHz}}$ is the carrier frequency in megahertz, and $\text{FSPL}_{\text{dB}}$ is the positive isotropic path attenuation in decibels. Doubling either the hop distance $d_{\text{km}}$ or the carrier frequency $f_{\text{MHz}}$ adds $20\log_{10}(2) \approx \mathbf{6.02\text{ dB}}$ of path loss.

* **Calculator Interface:** Primary Key: {{key:sc50:FSL}} • Expression / Workspace: `FSL: L = 20LOG(D×F) + 32.4` • Softkeys: {{keycap:L}} {{keycap:D}} {{keycap:F}}


---

### Eq. 14.2 — Logarithmic RF Link Budget and Fade Margin

A logarithmic link budget sums all power gains and subtracts all transmission losses along the path. Starting with transmitter output power in decibel-milliwatts, net antenna and amplifier gains in decibels are added, and total path and cable losses in decibels are subtracted. The difference between the resulting received power and the receiver's minimum sensitivity threshold establishes the fade margin against rain attenuation and atmospheric multipath fading:

$$P_{\text{rx,dBm}} = P_{\text{tx,dBm}} + G_{\text{dB}} - L_{\text{dB}}$$

Here $P_{\text{rx,dBm}}$ is the unfaded received signal power in $\text{dBm}$, $S_{\text{min,dBm}}$ is the receiver's minimum sensitivity threshold for a target modulation scheme and bit-error rate, and $M_{\text{fade}}$ is the link's **Fade Margin** in $\text{dB}$ against heavy rain, snow, or atmospheric multipath ducting. Along terrestrial paths, microwave engineers also verify that intervening terrain obstacles maintain at least $60\%$ clearance of the First Fresnel Zone ($r_1 \approx 13.14\sqrt{d_{\text{km}}/(4 f_{\text{GHz}})}\text{ m}$) to prevent destructive diffraction fading.

* **Calculator Interface:** Primary Key: {{key:sc50:LNK}} • Expression / Workspace: `LNK: R = P + G - L` • Softkeys: {{keycap:R}} {{keycap:P}} {{keycap:G}} {{keycap:L}}


---

### Eq. 14.3 — First Fresnel Zone Midpoint Radius and Clearance Criterion

Radio waves do not travel along a hairline ray; they expand through an ellipsoid of constructive phase coherence known as the First Fresnel Zone. Waves passing through the outer boundary of this ellipsoid travel exactly half a wavelength farther than the central ray. At the midpoint of a microwave hop, the radius of this zone scales with the square root of distance divided by carrier frequency. To prevent diffraction fading, the optical sightline must clear all terrain and obstacles by at least sixty percent of the First Fresnel Zone radius:

$$r_1 = \sqrt{\frac{\lambda \cdot d}{4}} = 8.656 \sqrt{\frac{d_{\text{km}}}{f_{\text{GHz}}}}\quad [\text{m}]$$

In this expression, $d_{\text{km}}$ is the total hop length in kilometers, $f_{\text{GHz}}$ is the carrier frequency in gigahertz, $r_1$ is the midpoint cross-sectional radius in meters of the first phase-coherent ellipsoid, and $h_{\text{clear,min}}$ is the required obstacle-free clearance.

* **Calculator Interface:** Primary Key: {{key:sc50:F₁}} • Expression / Workspace: `First Fresnel zone clearance radius` • Softkeys: {{keycap:F₁}} {{keycap:LNK}}


---

### Eq. 15.1 — Johnson–Nyquist Thermal Noise Floor

Thermal agitation of electrons sets the ultimate physical limit on radio reception. At standard room temperature, thermal noise delivers an available power density of roughly minus one hundred seventy-four decibel-milliwatts per hertz of bandwidth. Integrating across the receiver channel bandwidth adds ten times the base-ten logarithm of bandwidth in hertz, establishing the thermal noise floor:

$$N_{\text{floor,dBm}} = 10 \log_{10}(k_B T_0 \cdot 1000) + 10 \log_{10}(B_{\text{Hz}}) \approx -173.977 + 10 \log_{10}(B_{\text{Hz}})$$

Across a $B = 20\text{ MHz}$ channel at reference temperature $T_0 = 290\text{ K}$, {{key:sc50:Pₙ}} evaluates the thermal noise floor as $P_n = -174 + 10\log_{10}(20 \times 10^6) = -174 + 73.01 = \mathbf{-100.99\text{ dBm}}$ (or $\mathbf{-101.0\text{ dBm}}$).

* **Calculator Interface:** Primary Key: {{key:sc50:Pₙ}} • Expression / Workspace: `Johnson–Nyquist thermal noise floor` • Softkeys: {{keycap:Pₙ}} {{keycap:T₀}} {{keycap:kB}}


---

### Eq. 15.2 — Friis Cascaded Noise Factor

In a cascaded receiver chain, each successive stage adds noise. Harald Friis's 1944 cascade law demonstrates that the total noise factor is dominated by the very first amplifier. The first stage's noise factor is transferred directly, while each subsequent stage's excess noise is divided by the linear power gains of all preceding stages. Placing a high-gain, low-noise amplifier at the masthead suppresses downstream cable and receiver noise:

$$F_{\text{tot}} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \dots$$

In this equation, $F_1$ and $G_1$ are the linear noise factor and linear power gain of the very first component following the antenna, and each subsequent stage's excess noise $(F_k - 1)$ is divided by the product of all preceding linear gains $G_1 G_2 \cdots G_{k-1}$. Notice also that a passive lossy component (such as a coaxial cable of insertion loss $L_{\text{dB}}$ at $290\text{ K}$) has linear gain $G_{\text{cable}} = 10^{-L_{\text{dB}} / 10} < 1$ and linear noise factor $F_{\text{cable}} = 1 / G_{\text{cable}} = 10^{+L_{\text{dB}} / 10}$.

* **Calculator Interface:** Primary Key: {{key:sc50:NF}} • Expression / Workspace: `NF: F = A + (B - 1) / G` • Softkeys: {{keycap:F}} {{keycap:A}} {{keycap:B}} {{keycap:G}}


---

### Eq. 15.3 — Spurious-Free Dynamic Range

When strong interfering signals pass through non-linear receiver components, third-order intermodulation distortion rises three times faster in decibels than the fundamental signal. The input third-order intercept point extrapolates where these distortion products would equal the fundamental. Spurious-Free Dynamic Range measures the usable window between the noise floor and the point where distortion products emerge from the noise, spanning exactly two thirds of the difference between the third-order intercept point and the noise floor:

$$\text{SFDR}_{\text{dB}} = \frac{2}{3}\left(\text{IIP3}_{\text{dBm}} - N_{\text{floor,dBm}}\right)$$

For a receiver front-end with $\text{IIP3} = +5.0\text{ dBm}$ and an effective noise floor of $N_{\text{floor}} = -100.0\text{ dBm}$, the spurious-free dynamic range spans $\text{SFDR} = \frac{2}{3}(5.0 - (-100.0)) = \mathbf{70.0\text{ dB}}$.

* **Calculator Interface:** Primary Key: {{key:sc50:IP3}} • Expression / Workspace: `Spurious-free dynamic range and IP3` • Softkeys: {{keycap:IP3}} {{keycap:FDR}}


---

### Eq. 15.4 — Shannon–Hartley Channel Capacity and Spectral Efficiency

The channel capacity in bits per second equals the bandwidth in hertz multiplied by the base-two logarithm of one plus the linear signal-to-noise ratio. The base-two logarithm asks how many bits of information can be reliably encoded into each hertz of channel bandwidth:

$$C = B \log_2\left(1 + \text{SNR}\right) \quad [\text{bps}]$$

Here $B$ is the channel bandwidth in hertz, $\text{SNR}$ is the dimensionless linear signal-to-noise power ratio, $C$ is the maximum theoretical error-free data rate in $\text{bps}$, and $\eta = C / B$ is the **spectral efficiency** in $\text{bits/s/Hz}$. At high signal-to-noise ratios ($\text{SNR} \gg 1$), spectral efficiency grows as $\eta \approx \log_2(\text{SNR}) = \text{SNR}_{\text{dB}} / (10\log_{10} 2) = \text{SNR}_{\text{dB}} / 3.0103\text{ bits/s/Hz}$ per power ratio (or $\text{SNR}_{\text{dB}} / 6.0206$ amplitude bits per sample).

* **Calculator Interface:** Primary Key: {{key:sc50:C/B}} • Expression / Workspace: `C/B: C = B × LOG2(1 + S)` • Softkeys: {{keycap:C}} {{keycap:B}} {{keycap:S}}


---

### Eq. 15.5 — Doppler Velocity Shift and Fourth-Power Radar Echo

When a radio wave is received from a moving transmitter, wave crests are compressed or stretched, shifting the carrier frequency by the ratio of closing velocity to the speed of light. In a monostatic radar, the wave travels out to the target and reflects back, doubling the Doppler frequency shift. Because the wave spreads spherically on both the outbound and return journeys, echo power drops inversely with the fourth power of target range:

$$\Delta f_{\text{1-way}} = \frac{f_0 \cdot v}{c}$$

For our CubeSat transmitting at $f_0 = 437.0\text{ MHz}$ ($4.37 \times 10^8\text{ Hz}$) with a radial closure speed of $v = 7500\text{ m/s}$ (`437` {{key:sc50:ENTER}} `7500` {{key:sc50:Δf}}), the one-way telemetry downlink shift in Register $X$ is $\Delta f_{\text{1-way}} = (4.37 \times 10^8 \times 7500) / 299{,}792{,}458 \approx \mathbf{10{,}932.6\text{ Hz}}$ ($10.93\text{ kHz}$), and the two-way monostatic radar shift in Register $Y$ is $\Delta f_{\text{2-way}} \approx \mathbf{21{,}865.1\text{ Hz}}$ ($21.87\text{ kHz}$). Because two-way radar return scales with $\sigma / ((4\pi)^3 R^4)$ ({{key:sc50:RCS}} with range $R$ in Register $Y$ and cross-section $\sigma$ in Register $X$), doubling a radar's maximum detection range $R_{\max}$ requires increasing transmitter power sixteen-fold ($2^4 = 16$, or $+12.04\text{ dB}$).

* **Calculator Interface:** Primary Key: {{key:sc50:Δf}} • Expression / Workspace: `Doppler frequency shift and radar echo` • Softkeys: {{keycap:Δf}} {{keycap:RCS}}


---


## Unit VI: Wet-Lab Chemistry, Stoichiometry, and Spectroscopy

The **SC-60** provides dedicated faceplate keys and bidirectional Equation Solver workspaces to execute the governing laws of this domain. Each equation is indexed below with its physical motivation, governing formula, and operational calculator softkeys.

### Eq. 16.1 — Gravimetric Solute Mass and Molar Mass Summation

Because chemical reactions occur between individual molecules, chemical amounts are measured in moles. The molar mass of a substance sums the atomic weights of all constituent atoms in its chemical formula. To find the macroscopic mass in grams needed on an analytical balance, the chemical amount in moles is multiplied by the molar mass in grams per mole:

$$M = \sum_{i} \nu_i A_i \quad \left[\frac{\text{g}}{\text{mol}}\right]$$

In these expressions, $\nu_i$ is the integer stoichiometric subscript of element $i$ in the chemical formula, $M$ is the molar mass in $\text{g/mol}$, $n$ is the chemical amount in moles ($\text{mol}$), and $W$ is the physical mass in grams ($\text{g}$) weighed on the balance pan.

* **Calculator Interface:** Primary Key: {{key:sc60:MW}} • Expression / Workspace: `MW: W = N × M` • Softkeys: {{keycap:W}} {{keycap:N}} {{keycap:M}} {{keycap:Z}}


---

### Eq. 16.2 — Elemental Mass Percentage and Hydrate Molar Mass

When verifying elemental purity by combustion analysis or preparing trace-metal media, chemists evaluate the Elemental Mass Percentage $\text{WT\%}_i$ ({{key:sc60:w/w}})—the percentage of one mole's total mass contributed by element $i$. Furthermore, when an inorganic salt crystallizes from water as a hydrate ($\text{Salt} \cdot k\,\text{H}_2\text{O}$) containing $k$ stoichiometric molecules of water ($M(\text{H}_2\text{O}) = 18.015\text{ g/mol}$) locked inside its solid crystal lattice, those water molecules contribute directly to the gravimetric molar mass:

$$\text{WT\%}_i = \frac{\nu_i A_i}{M} \times 100\%$$

$$M_{\text{hydrate}} = M_{\text{anhydrous}} + k \cdot M(\text{H}_2\text{O})$$

In sulfuric acid ($\text{H}_2\text{SO}_4$, $M = 98.072\text{ g/mol}$), hydrogen accounts for $2.056\%$, sulfur for $32.690\%$, and oxygen for $65.254\%$. For hydrates such as sodium phosphate heptahydrate ($\text{Na}_2\text{HPO}_4 \cdot 7\text{H}_2\text{O}$), the seven water molecules add $126.105\text{ g/mol}$ to the anhydrous mass ($141.958\text{ g/mol}$), bringing the total crystalline mass to $268.063\text{ g/mol}$.

* **Calculator Interface:** Primary Key: {{key:sc60:w/w}} / {{key:sc60:MW}} • Expression / Workspace: `Stack: component in Y, total M in X` • Softkeys: {{keycap:w/w}} {{keycap:MW}}


---

### Eq. 16.3 — Volumetric Solution Molarity and Solute Mass

Molarity measures solution concentration as the chemical amount of dissolved solute divided by the total solution volume in liters. To prepare a solution of target molarity, the required dry solute mass is the product of target molarity, final volume, and solute molar mass:

$$C = \frac{n}{V} = \frac{W}{M \cdot V}$$

Here $C$ is the target molar concentration in $\text{mol/L}$ ($\text{M}$), $V$ is the final solution volume in liters ($\text{L}$, where $1\text{ mL} = 10^{-3}\text{ L}$), $n$ is the dissolved solute amount in moles, $M$ is the reagent molar mass in $\text{g/mol}$, and $W$ is the dry mass in grams.

* **Calculator Interface:** Primary Key: {{key:sc60:RXN}} • Expression / Workspace: `RXN: N = C × V` • Softkeys: {{keycap:N}} {{keycap:C}} {{keycap:V}}


---

### Eq. 16.4 — Conservation of Solute Moles in Stock Dilution

Because adding pure water introduces zero additional solute molecules, the total number of solute moles $n_{\text{solute}}$ aspirated in the stock aliquot $V_1$ equals the total number of solute moles present in the final diluted volume $V_2$. Multiplying stock concentration by aliquot volume equals final concentration multiplied by final volume:

$$C_1 V_1 = C_2 V_2 \iff V_1 = \frac{C_2 V_2}{C_1}$$

In this bilateral conservation equation, $C_1$ and $C_2$ may be expressed in any matching concentration unit ($\text{M}, \text{mM}, \mu\text{M}$, or $\text{mg/mL}$) and $V_1$ and $V_2$ in any matching volume unit ($\text{L}, \text{mL}$, or $\mu\text{L}$), while $V_{\text{solvent}}$ is the volume of pure diluent added to bring the aliquot $V_1$ up to the mark $V_2$.

* **Calculator Interface:** Primary Key: {{key:sc60:C₁V₁}} • Expression / Workspace: `C1V1: C × V = D × U` • Softkeys: {{keycap:C}} {{keycap:V}} {{keycap:D}} {{keycap:U}}


---

### Eq. 16.5 — Serial Pipetting Error Propagation

When a technician executes $k$ sequential dilutions using a micropipette whose relative volume delivery uncertainty at each transfer is $\sigma_V / V$, independent random pipetting errors add in quadrature, causing the cumulative relative concentration uncertainty $\sigma_{C_k} / C_k$ after $k$ steps to grow as the square root of the step count:

$$\frac{\sigma_{C_k}}{C_k} \approx \sqrt{k}\,\left(\frac{\sigma_V}{V}\right)$$

A six-step serial dilution ($k = 6$) with a $\pm 1.5\%$ micropipette inflates random concentration error to $\sqrt{6} \times 1.5\% \approx \pm 3.67\%$ (plus six times any systematic calibration bias), demonstrating why analytical chemists prefer single-cut aliquots ({{key:sc60:C₁V₁}}) from primary standards ({{key:sc60:MW}}) whenever possible.

* **Calculator Interface:** Primary Key: `Stack calculation` • Expression / Workspace: `Stack: k in X, SQRT, error in Y, ×` • Softkeys: {{key:√x}} {{key:×}}


---

### Eq. 16.6 — Colligative Freezing Point Depression

Colligative properties depend strictly on the ratio of dissolved solute particles to solvent molecules, independent of solute chemical identity. Dissolved non-volatile solute particles lower the chemical potential of the liquid phase, depressing the equilibrium freezing point according to Sir Charles Blagden's 1788 cryoscopic law:

$$\Delta T_f = i \cdot K_f \cdot m$$

Here $\Delta T_f$ is the freezing point depression in degrees Celsius ($^\circ\text{C}$ or $\text{K}$), $i$ is the dimensionless van 't Hoff dissociation factor ($i=1$ for non-electrolytes, $i \approx 2$ for $\text{NaCl}$, $i \approx 3$ for $\text{CaCl}_2$), $K_f$ is the molal freezing point depression constant ($1.853\ ^\circ\text{C}\cdot\text{kg/mol} \approx 1.86\ ^\circ\text{C}\cdot\text{kg/mol}$ for pure water), and $m$ is solute molality ($\text{mol/kg}$). Analytical chemists use this relation to formulate sub-zero eutectic salt reaction baths (depressing ice baths to $-10^\circ\text{C}$ or down to $-21.1^\circ\text{C}$ with eutectic $\text{NaCl}$) and audit reagent solute purity and molecular weight through precision freezing point osmometry.

* **Calculator Interface:** Primary Key: Cryoscopic Depression on Stack (`×`, {{key:sc60:MW}}) • Expression / Workspace: `Stack: i in Z, Kf in Y, m in X, multiply` • Softkeys: {{keycap:MW}} {{keycap:×}}


---

### Eq. 17.1 — Sørensen Logarithmic Acidity and Acid Dissociation Constant

Because aqueous proton concentrations span fourteen orders of magnitude, Sørensen introduced the pH scale using the negative base-ten logarithm. Taking the negative base-ten logarithm asks what power of ten represents the hydrogen-ion concentration; each one-unit decrease in pH represents a tenfold surge in free proton activity:

$$\text{pH} = -\log_{10}[\text{H}^+] \iff [\text{H}^+] = 10^{-\text{pH}}$$

In these equations, $[\text{H}^+]$ is the molar hydrogen-ion concentration in $\text{mol/L}$, $K_a$ is the equilibrium acid dissociation constant, and $\text{pH} + \text{pOH} = 14.00$ at $25^\circ\text{C}$. A strong acid solution at $[\text{H}^+] = 0.0010\text{ M}$ ($10^{-3}\text{ M}$) has $\text{pH} = \mathbf{3.00}$, while acetic acid with $K_a = 1.75 \times 10^{-5}$ has $\text{p}K_a = -\log_{10}(1.75 \times 10^{-5}) \approx \mathbf{4.757}$.

* **Calculator Interface:** Primary Key: {{key:sc60:pH}} • Expression / Workspace: `Sørensen logarithmic acidity` • Softkeys: {{keycap:pH}} {{keycap:pKₐ}}


---

### Eq. 17.2 — Henderson–Hasselbalch Buffer Equilibrium

The solution pH equals the weak acid's pKa plus the base-ten logarithm of the ratio of conjugate base to weak acid. When base and acid are present in equal amounts, the ratio is one, the logarithm is zero, and pH equals pKa:

$$\text{pH} = \text{p}K_a + \log_{10}\left(\frac{[\text{A}^-]}{[\text{HA}]}\right)$$

Here $[\text{A}^-]$ is the molar concentration of the proton-accepting conjugate base, $[\text{HA}]$ is the molar concentration of the proton-donating weak acid, and $r = [\text{A}^-] / [\text{HA}]$ is the dimensionless conjugate base-to-acid ratio. Notice the structural unity across physical science: just as the Nernst equation shifts electrochemical cell voltage by $(2.3026 R T / n_e F) \log_{10}([\text{Ox}]/[\text{Red}])$ ($59.16\text{ mV}$ per decade at $25^\circ\text{C}$) and decibels measure $10\log_{10}(P_2/P_1)$, the Henderson–Hasselbalch equation shifts chemical proton potential by $1.00\text{ pH unit}$ per decade change in the conjugate ratio $[\text{A}^-]/[\text{HA}]$. Furthermore, because dissociation constants depend on temperature—most notably in amine buffers such as Tris, where a large temperature coefficient of $\Delta \text{p}K_a / \Delta T \approx -0.028 / ^\circ\text{C}$ shifts a benchtop solution from $\text{pH } 7.40$ at $25^\circ\text{C}$ to nearly $\text{pH } 8.0$ in a $4^\circ\text{C}$ cold room—chemists calibrate electrodes and prepare buffers at the intended assay temperature.

* **Calculator Interface:** Primary Key: {{key:sc60:BUF}} • Expression / Workspace: `BUF: P = K + LOG(A/H)` • Softkeys: {{keycap:P}} {{keycap:K}} {{keycap:A}} {{keycap:H}}


---

### Eq. 17.3 — Van Slyke Buffer Capacity and Species Partitioning

The resistance of a conjugate buffer solution to $\text{pH}$ shifts upon addition of strong acid or base is quantified by the Van Slyke Buffer Capacity ($\beta$). Buffer capacity reaches its theoretical maximum $\beta_{\max} \approx 0.576 \cdot C_{\text{total}}$ when weak acid and conjugate base concentrations are exactly equal ($[\text{HA}] = [\text{A}^-]$), which occurs precisely at $\text{pH} = \text{p}K_a$:

$$\beta = 2.303 \cdot C_{\text{total}} \cdot \frac{[\text{HA}][\text{A}^-]}{([\text{HA}] + [\text{A}^-])^2} \le 0.576 \cdot C_{\text{total}}$$

$$[\text{HA}] = \frac{C_{\text{total}}}{1 + 10^{\text{pH} - \text{p}K_a}} \iff [\text{A}^-] = \frac{r \cdot C_{\text{total}}}{1 + r}$$

When solution $\text{pH}$ deviates from $\text{p}K_a$ by more than one full unit (where the base-to-acid ratio exceeds $10:1$ or falls below $1:10$), buffer capacity collapses below $33\%$ of its peak value, defining the practical buffering window as $\text{pH} \in [\text{p}K_a - 1, \text{p}K_a + 1]$.

* **Calculator Interface:** Primary Key: {{key:sc60:BUF}} • Expression / Workspace: `BUF: P = K + LOG(A/H)` • Softkeys: {{keycap:P}} {{keycap:K}} {{keycap:A}} {{keycap:H}}


---

### Eq. 17.4 — Buffer Acid-Spike Shift and Neutralization

The buffer's post-spike pH is evaluated by subtracting the added proton concentration from the initial conjugate base and adding it to the weak acid:

$$\text{pH}_{\text{after acid}} = \text{p}K_a + \log_{10}\left(\frac{[\text{A}^-]_0 - \Delta C_{\text{H}^+}}{[\text{HA}]_0 + \Delta C_{\text{H}^+}}\right)$$

Substituting our initial phosphate concentrations ($[\text{A}^-]_0 = 61.31\text{ mM}$ and $[\text{HA}]_0 = 38.69\text{ mM}$) and the $\Delta C_{\text{H}^+} = 5.0\text{ mM}$ acid spike gives the new concentrations $[\text{A}^-] = 61.31 - 5.0 = 56.31\text{ mM}$ ($0.05631\text{ M}$) and $[\text{HA}] = 38.69 + 5.0 = 43.69\text{ mM}$ ($0.04369\text{ M}$). The new base-to-acid ratio is $r_{\text{new}} = 56.31 / 43.69 \approx \mathbf{1.2889}$, and the resulting solution $\text{pH}$ is:

* **Calculator Interface:** Primary Key: {{key:sc60:BUF}} • Expression / Workspace: `Buffer acid-spike shift and capacity` • Softkeys: {{keycap:BUF}} {{keycap:EQV}}


---

### Eq. 17.5 — Volumetric Titration Equivalence Point

When an analytical chemist standardizes an acid or base by **Volumetric Titration** ({{key:sc60:EQV}}), a burette dispenses a measured volume $V_A$ of titrant of known molarity $C_A$ (producing $\nu_A$ moles of $\text{H}^+$ or $\text{OH}^-$ per formula unit) into a sample volume $V_B$ of unknown molarity $C_B$ (accepting or donating $\nu_B$ equivalents per formula unit). At the stoichiometric **equivalence point**, total acid equivalents equal total base equivalents:

$$\nu_A \cdot C_A \cdot V_A = \nu_B \cdot C_B \cdot V_B \iff C_B = \left(\frac{\nu_A}{\nu_B}\right)\frac{C_A \cdot V_A}{V_B}$$

For a **monoprotic** neutralization ($\nu_A = \nu_B = 1$, such as $\text{HCl} + \text{NaOH} \longrightarrow \text{NaCl} + \text{H}_2\text{O}$), equivalence simplifies to $C_A V_A = C_B V_B$: if $V_A = 24.50\text{ mL}$ of $C_A = 0.1000\text{ M}$ standard $\text{NaOH}$ neutralizes a $V_B = 25.00\text{ mL}$ monoprotic acid sample, the acid molarity is $C_B = (0.1000 \times 24.50) / 25.00 = \mathbf{0.0980\text{ M}}$.

* **Calculator Interface:** Primary Key: {{key:sc60:EQV}} • Expression / Workspace: `Volumetric titration equivalence point` • Softkeys: {{keycap:EQV}} {{keycap:RXN}}


---

### Eq. 18.1 — Beer–Lambert Spectrophotometric Absorbance

Integrating $dI / I = -\alpha c\,dx$ from $x = 0$ to $x = b$ shows that the emergent intensity $I$ and fractional **Transmittance** $T = I / I_0 \in (0, 1]$ decay exponentially with both path length $b$ and concentration $c$. The negative base-ten logarithm transforms this multiplicative attenuation into an additive, linear metric where each unit of absorbance represents one order of magnitude of photon extinction. This gives the **Beer–Lambert Law** ({{key:sc60:εbc}}):

$$A = -\log_{10}(T) = \varepsilon \cdot b \cdot c$$

Inverting the relationship yields the unknown molar concentration directly from the spectrophotometer's optical absorbance reading:

* **Calculator Interface:** Primary Key: {{key:sc60:εbc}} • Expression / Workspace: `EBC: A = E × B × C` • Softkeys: {{keycap:A}} {{keycap:E}} {{keycap:B}} {{keycap:C}} {{keycap:%T}}


---

### Eq. 18.2 — Arrhenius Thermal Reaction Kinetics and Acceleration

The natural exponential function evaluates the Boltzmann fraction of molecular collisions possessing sufficient thermal energy to surmount the reaction barrier $E_a$. The fundamental rate equation is:

$$k = A \exp\left(-\frac{E_a}{R \cdot T}\right)$$

Comparing reaction velocity constants $k_1$ and $k_2$ between two absolute temperatures $T_1$ and $T_2$ yields the **Arrhenius Acceleration Ratio**:

$$\frac{k_2}{k_1} = \exp\left[\frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right]$$

On the SC-60, pressing {{key:SOLVE}} {{key:sc60:Eₐ}} (or {{key:sc60:Eₐ}} with empty stack) launches the bidirectional **Arrhenius Kinetics Equation Solver Workspace** (`ARR: ARRHENIUS`), rendering `K = A × EXP(-E / (R × T))` across Line 1 with softkeys {{keycap:K}}, {{keycap:A}}, {{keycap:E}}, and {{keycap:T}} (with $R = 8.314462618\text{ J}/(\text{mol}\cdot\text{K})$ built into the solver kernel). Immediate stack execution with $E_a$ in Register $Y$ and $T$ in Register $X$ evaluates the Boltzmann exponential factor $\exp(-E_a / (RT))$ directly into Register $X$.

* **Calculator Interface:** Primary Key: {{key:sc60:Eₐ}} • Expression / Workspace: `ARR: K = A × EXP(-E / (R × T))` • Softkeys: {{keycap:K}} {{keycap:A}} {{keycap:E}} {{keycap:T}}


---

### Eq. 18.3 — Relative Centrifugal Force and Rotor Speed

When a centrifuge spins a sample tube at angular velocity $\omega = 2\pi \cdot \text{RPM} / 60$ (in radians per second) at radial distance $r$ from the central spindle axis, the outward centripetal acceleration is $a_c = \omega^2 r$. Dividing this acceleration by standard Earth gravity ($g = 9.80665\text{ m/s}^2 = 980.665\text{ cm/s}^2$) defines the dimensionless **Relative Centrifugal Force** ({{key:sc60:RCF}}, expressed in multiples of Earth gravity, $\times g$):

$$\text{RCF} \approx 1.118 \times 10^{-5} \cdot r_{\text{cm}} \cdot \text{RPM}^2$$

Because centripetal acceleration scales quadratically with angular velocity, solving for the required spindle revolutions per minute takes the square root:

* **Calculator Interface:** Primary Key: {{key:sc60:RCF}} • Expression / Workspace: `Relative centrifugal force and rotor RPM` • Softkeys: {{keycap:RCF}} {{keycap:RPM}}


---


## Unit VII: Commercial Bakery, Fermentation Science, and Brewing

The **SC-78** provides dedicated faceplate keys and bidirectional Equation Solver workspaces to execute the governing laws of this domain. Each equation is indexed below with its physical motivation, governing formula, and operational calculator softkeys.

### Eq. 19.1 — Baker's Percentage Mass Ratio and Ingredient Weight

In the **Baker's Percentage** ({{key:sc78:BK%}}) coordinate system, the combined mass of all milled grain flours introduced into the mixer—high-protein bread flour, stoneground whole wheat, rye, or Khorasan—is defined as the reference flour mass $F$ and assigned $100.0\%$. Each ingredient percentage $P_i$ expresses its weight $I_i$ as a proportion of total flour mass rather than total dough mass, allowing individual ingredient ratios to be modified without perturbing the rest of the formula:

$$P_i = \left(\frac{I_i}{F}\right) \times 100$$

Multiplying the reference flour mass by that percentage yields the required ingredient scaling weight:

* **Calculator Interface:** Primary Key: {{key:sc78:BK%}} • Expression / Workspace: `BK%: P = I / F × 100` • Softkeys: {{keycap:P}} {{keycap:I}} {{keycap:F}} {{keycap:ΣW}}


---

### Eq. 19.2 — Desired Dough Water Temperature and Friction Balance

To maintain a repeatable four-hour bulk fermentation schedule, mixed sourdough must exit the bowl at a target **Desired Dough Temperature** ($D$, typically $24.0^\circ\text{C}$ for country hearth loaves). Under the commercial Three-Factor Rule ({{key:sc78:Tw}}), final dough temperature is governed by an energy balance among ambient room air temperature $R$, stored flour temperature $F$, strike water temperature $W$, and the mechanical friction heat $M$ imparted by mixer shear. Multiplying the target Desired Dough Temperature $D$ by three and subtracting room, flour, and friction temperatures yields the required strike-water temperature:

$$W = 3 D - R - F - M$$

Rearranging the balance enables backward calibration of the mixer's empirical friction factor from measured test-batch temperatures:

* **Calculator Interface:** Primary Key: {{key:sc78:Tw}} • Expression / Workspace: `TW: W = 3×D - R - F - M` • Softkeys: {{keycap:W}} {{keycap:D}} {{keycap:R}} {{keycap:F}} {{keycap:M}}


---

### Eq. 19.3 — Latent-Heat Flake Ice Mass Substitution

When the required strike-water temperature $T_{\text{target}} = W$ falls below the temperature of municipal tap water ($T_{\text{tap}} = 21.0^\circ\text{C}$) and the bakery lacks a refrigerated water chiller, the baker substitutes crushed or flake ice ({{key:sc78:ICE}}) for part of the liquid water mass $W_{\text{water}}$. Liquid water cools sensibly by one kilocalorie per kilogram for each degree Celsius dropped. Solid ice at $0^\circ\text{C}$, by contrast, absorbs approximately eighty kilocalories per kilogram in latent heat solely to undergo the solid-to-liquid phase transition. Dividing the sensible cooling deficit by eighty determines the required flake-ice mass ({{key:sc78:ICE}}):

$$W_{\text{ice}} = \frac{W_{\text{water}} \cdot \left(T_{\text{tap}} - W\right)}{80}$$

The remaining liquid tap-water addition is then simply the difference between total water and ice mass:

* **Calculator Interface:** Primary Key: {{key:sc78:ICE}} • Expression / Workspace: `Latent-heat flake ice mass substitution` • Softkeys: {{keycap:ICE}} {{keycap:Tw}}


---

### Eq. 20.1 — Specific Gravity and Extract Conversion

Degrees Brix and Plato measure the mass percentage of sucrose-equivalent extract in aqueous solution. Because dissolved sugars increase liquid density nonlinearly, converting between refractometric extract and hydrometer Specific Gravity uses the American Society of Brewing Chemists (ASBC) rational relation:

$$\text{SG} = 1 + \frac{B}{258.6 - \left(\frac{B}{258.2}\right) \times 227.1}$$

Inverting the mapping yields the cubic ASBC extract polynomial:

* **Calculator Interface:** Primary Key: {{key:sc78:▸SG}} • Expression / Workspace: `ASBC specific gravity and extract Plato` • Softkeys: {{keycap:▸SG}} {{keycap:▸Brx}} {{keycap:▸°P}}


---

### Eq. 20.2 — Apparent Attenuation and Alcohol by Volume

As yeast ferments the sweet wort from **Original Gravity** ($O$) down to **Final Gravity** ($F$), the percentage of gravity points consumed defines **Apparent Attenuation** ($\text{ATT}_{\%}$):

$$\text{ATT}_{\%} = \left(\frac{O - F}{O - 1.000}\right) \times 100$$

Multiplying that density drop by the stoichiometric fermentation constant $131.25$ determines finished **Alcohol by Volume** ({{key:sc78:ABV}}, $A$) and distilled spirit proof ({{key:sc78:▸PRF}}, $\text{Proof} = 2 \times \text{ABV}_{\%}$):

* **Calculator Interface:** Primary Key: {{key:sc78:ABV}} • Expression / Workspace: `ABV: A = (O - F) × 131.25` • Softkeys: {{keycap:A}} {{keycap:O}} {{keycap:F}}


---

### Eq. 20.3 — Tinseth Hop Bitterness and Utilization Kinetics

One **International Bitterness Unit** ({{key:sc78:IBU}}, $I$) is defined analytically as $1.0\text{ mg}$ of isomerized alpha acids per liter of beer ($1\text{ mg/L}$). Glenn Tinseth's utilization function models the biochemical efficiency of the boil: the exponential gravity factor accounts for the reduced solubility of alpha acids in dense wort, while the time factor captures first-order thermal isomerization asymptotically approaching a practical extraction limit:

$$I = \frac{W_{\text{g}} \cdot A \cdot U \cdot 1000}{V_{\text{L}}}$$

In U.S. customary units ($W_{\text{oz}}$ in ounces, percentage alpha acid $A_{\%}$, and batch volume $V_{\text{gal}}$ in gallons), the conversion factor is $74.89$:

* **Calculator Interface:** Primary Key: {{key:sc78:IBU}} • Expression / Workspace: `IBU: I = W × A × U × 74.89 / V` • Softkeys: {{keycap:I}} {{keycap:W}} {{keycap:A}} {{keycap:U}} {{keycap:V}}


---

### Eq. 21.1 — Compounding Fabrication Yield and Edible Mass

In culinary cost accounting, the gross weight of an untrimmed commodity as delivered by the supplier is the **As-Purchased Mass** ($W_{\text{AP}}$), whereas the net weight of fabricated, cooked food ready for service is the **Edible Portion Mass** ($W_{\text{EP}}$). When a product undergoes $m$ sequential processing stages with individual decimal stage yields $y_1, y_2, \dots, y_m \in (0, 1]$ (where $y_k = 1 - \ell_k$ for stage fractional loss $\ell_k$), mass conservation dictates that the stage yields **multiply geometrically** rather than subtracting linearly:

$$y_{\text{cum}} = \prod_{k=1}^{m} y_k = \prod_{k=1}^{m} \left(1 - \ell_k\right)$$

The resulting cumulative yield decimal $y_{\text{cum}} = Y_{\%} / 100$ determines the edible finished mass $W_{\text{EP}}$ from the gross delivery weight $W_{\text{AP}}$:

* **Calculator Interface:** Primary Key: {{key:sc78:YLD}} • Expression / Workspace: `Butcher fabrication trim yield` • Softkeys: {{keycap:YLD}} {{keycap:SCL}}


---

### Eq. 21.2 — Yield-Adjusted Edible Portion Unit Cost

When an untrimmed commodity is purchased at an **As-Purchased Unit Cost** of $C_{\text{AP}}$ (in dollars per pound or kilogram) and yields a cumulative decimal fraction $y_{\text{cum}} = Y_{\%} / 100 = \prod_{k=1}^m y_k$ of edible product after fabrication and cooking, the entire invoice expenditure must be recovered across the smaller edible mass $W_{\text{EP}}$. Dividing $C_{\text{AP}}$ by $y_{\text{cum}}$ gives the true **Edible Portion Unit Cost** ($C_{\text{EP}}$):

$$C_{\text{EP}} = \frac{C_{\text{AP}}}{y_{\text{cum}}} = \frac{C_{\text{AP}}}{\prod_{k=1}^{m} y_k}$$

Multiplying that edible unit cost by portion serving weight $w_{\text{portion}}$ yields the raw plate protein cost:

* **Calculator Interface:** Primary Key: {{key:sc78:CST}} • Expression / Workspace: `CST: P = C / (F / 100)` • Softkeys: {{keycap:P}} {{keycap:C}} {{keycap:F}}


---

### Eq. 21.3 — Food Cost to Gross Margin Hyperbolic Mapping

Food cost fraction $f$ and gross margin $m$ normalize profit against selling price $P$, whereas markup $u$ normalizes that same profit against kitchen cost $C$. Because margin divides by price and markup divides by cost, their relationship forms a hyperbolic curve with a vertical asymptote as gross margin approaches one hundred percent:

$$f = \frac{C}{P} \iff P = \frac{C}{f} = \frac{C}{1 - m} = C \left(1 + u\right)$$

The inverse transformations convert bidirectionally between gross margin $m$ and markup on cost $u$:

* **Calculator Interface:** Primary Key: {{key:sc78:PRC}} • Expression / Workspace: `Food cost to gross margin hyperbolic mapping` • Softkeys: {{keycap:PRC}} {{keycap:CST}}


---


## Unit VIII: Clinical Nursing, Hospital Pharmacy, and Infusions

The **SC-80** provides dedicated faceplate keys and bidirectional Equation Solver workspaces to execute the governing laws of this domain. Each equation is indexed below with its physical motivation, governing formula, and operational calculator softkeys.

### Eq. 22.1 — Mosteller Body Surface Area and Inversion

Two patients who each weigh $88.0\text{ kg}$ can possess markedly different internal drug distribution volumes. A tall, muscular patient has an expansive vascular bed, high cardiac output, and large hepatic and renal parenchymal mass, whereas a shorter, sedentary patient of the same $88.0\text{ kg}$ weight carries a substantial fraction of mass as poorly perfused adipose tissue. Because extracellular fluid volume, glomerular filtration, and basal metabolic rate correlate closely with external **Body Surface Area** ({{key:sc80:BSA}}, $B$) in square meters ($\text{m}^2$, averaging $1.73\text{ m}^2$ in a reference adult), Robert D. Mosteller (1987) formulated {{key:sc80:BSA}} from patient height $H$ (in $\text{cm}$) and total body weight $W$ (in $\text{kg}$) using the dimensional normalization constant $3600 = 60^2\text{ cm}\cdot\text{kg/m}^4$:

$$B = \sqrt{\frac{H \cdot W}{3600}}$$

Inverting the square root yields the patient mass required to achieve a specified target surface area:

* **Calculator Interface:** Primary Key: {{key:sc80:BSA}} • Expression / Workspace: `BSA: B = √(H × W / 3600)` • Softkeys: {{keycap:B}} {{keycap:H}} {{keycap:W}} {{keycap:PAT}}


---

### Eq. 22.2 — Devine Ideal Body Weight and Adipose Adjustment

When dosing hydrophilic medications that remain inside lean tissue and extracellular water, using raw total body weight ($\text{TBW} = W$) in an overweight patient causes systematic over-dosing. To estimate lean metabolically active mass from skeletal stature alone, Ben Devine (1974) established the **Ideal Body Weight** ({{key:sc80:IBW}}, in $\text{kg}$) equations for adults at least $60\text{ inches}$ ($152.4\text{ cm}$, or $5\text{ feet}$) tall, where $H_{\text{in}} = H / 2.54$ is height in inches, $50.0\text{ kg}$ (male) and $45.5\text{ kg}$ (female) are the baseline lean weights at $60\text{ inches}$, and $2.3\text{ kg/in}$ ($0.9055\text{ kg/cm}$) is the linear lean-mass increment per inch above five feet:

$$\text{IBW}_{\text{male}} = 50.0 + 2.3\left(\frac{H}{2.54} - 60\right)$$

When a patient's total body weight $\text{TBW}$ exceeds $\text{IBW}$ by more than $20\%$, polar antibiotics such as aminoglycosides penetrate roughly $40\%$ into excess adipose extracellular water, which clinical pharmacists capture via **Adjusted Body Weight** ({{key:sc80:ABW}}, in $\text{kg}$) using the empirical adipose distribution factor $0.40$:

* **Calculator Interface:** Primary Key: {{key:sc80:IBW}} • Expression / Workspace: `Devine ideal and adjusted body weight` • Softkeys: {{keycap:IBW}} {{keycap:ABW}} {{keycap:BMI}}


---

### Eq. 22.3 — Cockcroft–Gault Creatinine Clearance Estimation

Creatinine is a nitrogenous breakdown product of creatine phosphate in skeletal muscle, released into blood plasma at a steady daily rate proportional to muscle mass and filtered freely by the renal glomeruli into the urine. At steady state, urinary creatinine excretion matches muscle creatinine production, making **Creatinine Clearance** ({{key:sc80:GFR}}, $C$)—the volume of plasma cleared of creatinine per minute ($\text{mL/min}$)—inversely proportional to steady-state serum creatinine ($S$, in $\text{mg/dL}$). Because skeletal muscle mass and nephron count decline linearly with adult age ($A$, in years), Donald Cockcroft and Henry Gault (1976) formulated bedside {{key:sc80:GFR}} from dosing weight $W$, using the empirical constant $72$ in the denominator and a $0.85$ factor in biological females ({{keycap:FEM}} in {{keycap:PAT}}) to reflect lower average skeletal muscle mass per kilogram:

$$C_{\text{male}} = \frac{\left(140 - A\right) \cdot W}{72 \cdot S}$$

A fifteen percent reduction accounts for lower average muscular mass in biological females:

* **Calculator Interface:** Primary Key: {{key:sc80:GFR}} • Expression / Workspace: `GFR: C = (140 - A) × W / (72 × S)` • Softkeys: {{keycap:C}} {{keycap:A}} {{keycap:W}} {{keycap:S}}


---

### Eq. 22.4 — Holliday–Segar Pediatric 4-2-1 Fluid Maintenance

To replace daily insensible (respiratory and cutaneous) and urinary water losses in hospitalized children and adults, Malcolm Holliday and William Segar (1957) tied basal water requirements to metabolic caloric expenditure across three body-mass tiers, establishing the **4-2-1 Maintenance Fluid Rule** ({{key:sc80:421}}):

$$R_{\text{maint,mL/hr}} = \begin{cases} 4 \cdot W & \text{if } W \le 10 \\ 40 + 2\left(W - 10\right) & \text{if } 10 < W \le 20 \\ 60 + 1\left(W - 20\right) & \text{if } W > 20 \end{cases}$$

Across clinical nutrition ({{key:sc80:REE}}) and veterinary medicine ({{key:sc80:VET}}), basal caloric demand follows Max Kleiber's $3/4$-power allometric **Resting Energy Expenditure** (in $\text{kcal/day}$):

* **Calculator Interface:** Primary Key: {{key:sc80:IV}} • Expression / Workspace: `Holliday–Segar pediatric 4-2-1 fluid rate` • Softkeys: {{keycap:IV}} {{keycap:DOS}}


---

### Eq. 23.1 — Continuous Vasoactive Mass Flux to Volumetric Pump Rate

When a physician orders a continuous weight-based dose $D$ (in $\mu\text{g}\cdot\text{kg}^{-1}\cdot\text{min}^{-1}$) for a patient of body mass $W$ (in $\text{kg}$, pre-populated from {{keycap:PAT}}), multiplying $D \cdot W$ gives the microgram delivery rate per minute ($\mu\text{g/min}$), and multiplying by $60\text{ min/hr}$ yields the hourly microgram flux $\dot{m}_{\text{mcg/hr}} = 60 D W$ (or dividing by $1000\ \mu\text{g/mg}$ via the immediate {{key:sc80:DRP}} stack operator gives the hourly milligram flux $\dot{m}_{\text{mg/hr}} = 0.060 D W$). Dividing the hourly microgram flux by the pharmacy bag's microgram concentration $C = 1000 \cdot (M_{\text{bag,mg}} / V_{\text{bag,mL}})$ (in $\mu\text{g/mL}$) yields the **Volumetric Infusion Pump Rate** $R$ (in $\text{mL/hr}$), while algebraic inversion in the {{key:sc80:DRP}} Solver Workspace solves backward via {{key:sc80:XEQ}} for the **Delivered Dose Rate** $D$ from an observed pump rate $R$:

$$R = \frac{D \cdot W \cdot 60}{C} \iff D = \frac{R \cdot C}{60 \cdot W}$$

The active drug concentration $C$ in micrograms per milliliter reflects the pharmacy bag reconstitution:

* **Calculator Interface:** Primary Key: {{key:sc80:DRP}} • Expression / Workspace: `DRP: R = D × W × 60 / C` • Softkeys: {{keycap:R}} {{keycap:D}} {{keycap:W}} {{keycap:C}}


---

### Eq. 23.2 — Gravity Drop Frequency from Volumetric Flow

Every manual intravenous administration set manufactures its drip-chamber orifice to form drops of a fixed volumetric size, specified by the tubing **Drop Factor** ($DF_{\text{gtt/mL}}$, in drops per milliliter, $\text{gtt/mL}$). Standard adult **macro-drip** sets deliver $10$, $15$, or $20\text{ gtt/mL}$, whereas pediatric and critical-care **micro-drip** sets use a fine stainless-steel needle orifice that delivers $60\text{ gtt/mL}$. Multiplying the hourly volumetric flow rate $R_{\text{mL/hr}}$ by $DF_{\text{gtt/mL}}$ gives drops per hour, and dividing by $60\text{ min/hr}$ yields the **Gravity Drip Rate** ({{key:sc80:gtt}}, $R_{\text{gtt/min}}$, in drops per minute):

$$R_{\text{gtt/min}} = \frac{R_{\text{mL/hr}} \cdot DF_{\text{gtt/mL}}}{60}$$

Notice the geometric elegance of the $60\text{ gtt/mL}$ micro-drip chamber: when $DF_{\text{gtt/mL}} = 60$, the ratio $60 / 60$ equals unity, so $R_{\text{gtt/min}} = R_{\text{mL/hr}}$ numerically. For our ICU transport running at $R_{\text{mL/hr}} = 15.00\text{ mL/hr}$, a macro-drip set with $DF = 15\text{ gtt/mL}$ produces a drip rate via {{key:sc80:gtt}} of $R_{\text{gtt/min}} = (15.00 \times 15) / 60 = \mathbf{3.75\text{ gtt/min}}$, whereas switching to a $60\text{ gtt/mL}$ micro-drip chamber raises the drip frequency to $\mathbf{15.00\text{ gtt/min}}$ (one drop every $4.0\text{ seconds}$).

* **Calculator Interface:** Primary Key: {{key:sc80:gtt}} • Expression / Workspace: `Gravity drop frequency from flow rate` • Softkeys: {{keycap:gtt}} {{keycap:DRP}}


---

### Eq. 23.3 — Mean Arterial Pressure and Parkland Resuscitation

Vasoactive infusions are titrated to restore organ perfusion pressure and cardiac output, while severe thermal burns require high-volume crystalloid infusions to replace capillary plasma leakage. At resting heart rates, the cardiac ventricles spend roughly one-third of each cardiac cycle in systolic ejection ($\text{SBP}$, in $\text{mmHg}$) and two-thirds in diastolic relaxation ($\text{DBP}$, in $\text{mmHg}$), defining **Mean Arterial Pressure** ({{key:sc80:MAP}}, in $\text{mmHg}$):

$$\text{MAP} = \text{DBP} + \frac{1}{3}\left(\text{SBP} - \text{DBP}\right) = \frac{\text{SBP} + 2 \cdot \text{DBP}}{3}$$

Multiplying heart rate $H$ ($\text{bpm}$) by stroke volume $S$ ($\text{mL/beat}$) and dividing by $1000\text{ mL/L}$ gives **Cardiac Output** ({{key:sc80:ICU}}, $Q = H \cdot S / 1000\text{ L/min}$). Simultaneously, Charles Baxter's 1968 **Parkland Formula** ({{key:sc80:BRN}}) sizes the total $24\text{-hour}$ Lactated Ringer's crystalloid resuscitation volume $V$ (in $\text{mL}$) from patient weight $W$ (pre-populated from {{keycap:PAT}}) and the percentage of Total Body Surface Area burned ($B = \%\,\text{TBSA}$, entered as a whole number such as $35$ for $35\%$):

* **Calculator Interface:** Primary Key: {{key:sc80:ICU}} • Expression / Workspace: `Mean arterial pressure and Parkland resuscitation` • Softkeys: {{keycap:ICU}} {{keycap:BRN}}


---

### Eq. 24.1 — One-Compartment First-Order Elimination Kinetics

When an intravenous bolus dose of mass $D$ (in $\text{mg}$) mixes across the **Apparent Volume of Distribution** ($V$, in liters $\text{L}$) cleared at volumetric **Systemic Clearance** rate $C_{\text{CL}}$ (in $\text{L/hr}$), it establishes an initial peak concentration $C_0 = D / V$ (in $\text{mg/L}$). Because the rate of drug elimination $-dM/dt = C_{\text{CL}} \cdot C(t)$ is proportional to instantaneous concentration $C(t)$, plasma concentration decays exponentially according to the first-order **Elimination Rate Constant** ($K$, in $\text{hr}^{-1}$) and **Elimination Half-Life** ($T_{1/2}$, in hours), where $\ln(2) \approx 0.693147$ ({{key:sc80:PK}}):

$$C(t) = C_0 \, e^{-K t}$$

The biological half-life divides the natural logarithm of two by the elimination rate constant:

* **Calculator Interface:** Primary Key: {{key:sc80:PK}} • Expression / Workspace: `PK: T = .69315 × V / C` • Softkeys: {{keycap:T}} {{keycap:V}} {{keycap:C}}


---

### Eq. 24.2 — Multi-Dose Steady-State Accumulation Factor

When the same maintenance dose $D$ is repeated at a fixed dosing interval $\tau$ (in hours), each new dose adds $C_0 = D / V$ on top of the residual trough remaining from all prior doses. After $n$ doses, the finite geometric series $\sum_{j=0}^{n-1} r^j = (1 - r^n)/(1 - r)$ with per-interval survival ratio $r = e^{-K \tau} = 2^{-\tau / T_{1/2}}$ converges as $n \to \infty$ to the **Steady-State Accumulation Factor** $R_{\text{acc}}$, determining the **Steady-State Peak** ($C_{\text{ss,max}}$), **Steady-State Trough** ($C_{\text{ss,min}}$), and **Average Steady-State Concentration** ($C_{\text{ss,avg}}$, which equals $\text{AUC}_{0\to\tau} / \tau$):

$$R_{\text{acc}} = \sum_{j=0}^{\infty} e^{-j K \tau} = \frac{1}{1 - e^{-K \tau}}$$

Multiplying the single-dose peak increment $C_0$ by $R_{\text{acc}}$ gives the steady-state maximum and minimum concentrations:

* **Calculator Interface:** Primary Key: {{key:sc80:PK}} • Expression / Workspace: `Multi-dose steady-state drug accumulation` • Softkeys: {{keycap:PK}} {{keycap:DOS}}


---

### Eq. 24.3 — Bazett Heart Rate-Corrected QT Interval

Alongside blood gas analysis, Henry Cuthbert Bazett's (1920) **Corrected QT Interval** ({{key:sc80:QTc}}, in $\text{ms}$) normalizes ventricular repolarization time $\text{QT}_{\text{ms}}$ to a $60\text{ bpm}$ ($RR = 1.0\text{ s}$) reference by dividing by the square root of the cardiac RR cycle length in seconds:

$$\text{QT}_c = \frac{\text{QT}_{\text{ms}}}{\sqrt{60 / \text{HR}}}$$

With a measured interval $\text{QT} = 380\text{ ms}$ at heart rate $88\text{ bpm}$ ($RR = 60 / 88 \approx 0.6818\text{ s}$), Bazett's formula evaluated via {{key:sc80:QTc}} yields $\text{QT}_c = \frac{380}{\sqrt{0.6818}} \approx \mathbf{460.2\text{ ms}}$, flagging borderline prolongation.

* **Calculator Interface:** Primary Key: {{key:sc80:QTc}} • Expression / Workspace: `Bazett heart rate-corrected QT interval` • Softkeys: {{keycap:QTc}}


---

### Eq. 24.4 — Compressed Medical Oxygen Cylinder Remaining Duration

The **Compressed Oxygen Cylinder Law** ({{key:sc80:O₂}}) relates remaining tank pressure $P_{\text{psi}}$ (above the $200\text{ psi}$ safe residual cushion) and cylinder conversion factor $k_{\text{tank}}$ ($0.28\text{ L/psi}$ for a portable E-cylinder; $3.14\text{ L/psi}$ for a bulk H-cylinder) to delivery flow rate $F$ ($\text{L/min}$) and transport duration $T$ ($\text{min}$):

$$T_{\text{min}} = \frac{\left(P_{\text{psi}} - 200\right) \times 0.28}{F}$$

At $F_i\text{O}_2 = 0.40$, $P_a\text{CO}_2 = 28\text{ mmHg}$, and $P_a\text{O}_2 = 110\text{ mmHg}$, pressing `110` {{key:sc80:ENTER}} `0.40` {{key:sc80:ABG}} gives a Horowitz $P/F$ ratio of $\mathbf{275.0\text{ mmHg}}$, while alveolar oxygen is $P_A\text{O}_2 = 0.40(713) - 28/0.8 = 285.2 - 35.0 = 250.2\text{ mmHg}$, giving $\Delta P_{A-a}\text{O}_2 = 250.2 - 110 = \mathbf{140.2\text{ mmHg}}$. On the ECG monitor ($\text{QT} = 420\text{ ms}$ at $\text{HR} = 96\text{ bpm}$, so $RR = 60/96 = 0.625\text{ s}$), pressing `420` {{key:sc80:ENTER}} `96` {{key:sc80:QTc}} gives $\text{QT}_c = 420 / \sqrt{0.625} = \mathbf{531.26\text{ ms}}$ (alerting the team to pause QT-prolonging antiarrhythmics). Finally, because $T$ and $F$ are reciprocally symmetric in $T \cdot F = (P_{\text{psi}} - 200) \times 0.28$, for the $T = 70.0\text{-minute}$ helicopter transfer with an E-cylinder at $P_{\text{psi}} = 1950\text{ psi}$, pressing `1950` {{key:sc80:ENTER}} `70` {{key:sc80:O₂}} directly yields the maximum safe oxygen flow rate $F = (1950 - 200) \times 0.28 / 70.0 = 490.0 / 70.0 = \mathbf{7.00\text{ L/min}}$.

* **Calculator Interface:** Primary Key: {{key:sc80:O₂}} • Expression / Workspace: `Compressed oxygen cylinder remaining time` • Softkeys: {{keycap:O₂}}


---

### Eq. 24.5 — Radiopharmaceutical Exponential Half-Life Decay

In nuclear pharmacy and hospital radiochemistry, therapeutic and diagnostic radioisotopes (such as Technetium-$99\text{m}$, Fluorine-$18$, and Iodine-$131$) disintegrate via first-order nuclear decay. The instantaneous radioactivity $A(t)$ after elapsed transit or preparation time $T$ depends on the initial calibrated activity $A_0$ and the physical half-life $H = t_{1/2}$:

$$A = A_0 \cdot 2^{-T / H} = A_0 \cdot \exp\left(-\frac{\ln 2}{H} \cdot T\right)$$

Inverting the relationship solves for the required compounding pre-calibration activity $A_0 = A \cdot 2^{T/H}$ needed to deliver a target patient dose at injection time, or evaluates the decay time $T = -H \frac{\ln(A / A_0)}{\ln 2}$.

On the SC-80, staging initial activity $A_0$ in Register $Y$ and elapsed time $T$ in Register $X$ before pressing {{key:sc80:VIL}} calculates the remaining activity $A$ (using isotope half-life $H$ stored in variable `H`, defaulting to $6.0\text{ hours}$ for Technetium-$99\text{m}$). In the bidirectional Equation Solver Workspace ({{key:XEQ}} {{key:sc80:VIL}}), the calculator displays `RAD: DECAY / HL` with governing equation `A = A0 × 2^(-T / H)` and softkeys {{keycap:A}}, {{keycap:O}}, {{keycap:T}}, and {{keycap:H}}.

* **Calculator Interface:** Primary Key: {{key:sc80:VIL}} • Expression / Workspace: `RAD: A = A0 × 2^(-T / H)` • Softkeys: {{keycap:A}} {{keycap:O}} {{keycap:T}} {{keycap:H}}


---


## Unit IX: Quantitative Finance, Actuarial Science, and Six Sigma

The **SC-95** provides dedicated faceplate keys and bidirectional Equation Solver workspaces to execute the governing laws of this domain. Each equation is indexed below with its physical motivation, governing formula, and operational calculator softkeys.

### Eq. 25.1 — Five-Variable Time Value of Money Governing Equation

Across any level-payment financial contract in the {{key:sc95:TVM}} workspace, five parameters are coupled together on softkeys {{keycap:N}}, {{keycap:I%}}, {{keycap:PV}}, {{keycap:PMT}}, and {{keycap:FV}} (alongside payment timing {{keycap:END}}/{{keycap:BEG}}): the total number of compounding or payment periods $N$ ({{keycap:N}}), the periodic interest rate {{keycap:I%}} expressed as a percentage per period where the decimal rate is $i = (\text{I\%})/100$ (obtained from the nominal annual rate by dividing by $M$ compounding periods per year), the initial **Present Value** $\text{PV}$ ({{keycap:PV}}) at $t = 0$, the level periodic **Payment** $\text{PMT}$ ({{keycap:PMT}}) at the end of each period $t = 1, 2, \dots, N$, and the terminal **Future Value** or balloon balance $\text{FV}$ ({{keycap:FV}}) at horizon $t = N$. Discounting each cash flow back to $t = 0$ and summing the finite geometric series $\sum_{t=1}^{N} (1+i)^{-t} = (1 - (1+i)^{-N})/i$ yields the **Time Value of Money Balance Equation**:

$$\text{PV} + \text{PMT}\left(\frac{1 - (1 + i)^{-N}}{i}\right) + \text{FV}(1 + i)^{-N} = 0$$

Compounded forward to future horizon $t = N$, the terminal balance is:

* **Calculator Interface:** Primary Key: {{key:sc95:TVM}} • Expression / Workspace: `TVM: Five-variable financial balance` • Softkeys: {{keycap:N}} {{keycap:I%}} {{keycap:PV}} {{keycap:PMT}} {{keycap:FV}}


---

### Eq. 25.2 — Uniform Series Net Present Value and Internal Rate of Return

When a capital project requires an initial investment $I_0$ at $t = 0$ and generates a uniform net operating cash inflow $C$ across $N$ periods discounted at the firm's opportunity cost of capital (hurdle rate) $r = R / 100$, **Net Present Value** ({{key:sc95:CF}}, opening the {{key:sc95:CF}} Solver Workspace) subtracts $I_0$ from the present value of the cash-flow annuity. A positive $\text{NPV} > 0$ certifies that the asset earns more than the hurdle rate $r$:

$$\text{NPV} = C\left(\frac{1 - (1 + r)^{-N}}{r}\right) - I_0$$

The break-even discount rate $r^*$ at which $\text{NPV}(r^*) = 0$ defines the **Internal Rate of Return** ($\text{IRR}$):

* **Calculator Interface:** Primary Key: {{key:sc95:CF}} • Expression / Workspace: `CF: Net present value and internal rate of return` • Softkeys: {{keycap:V}} {{keycap:C}} {{keycap:R}} {{keycap:N}} {{keycap:I}}


---

### Eq. 25.3 — Breakeven Production Volume and Economic Order Quantity

Simultaneously, a plant with fixed overhead $F_{\text{fixed}}$ and unit contribution margin $M_c = P - V$ reaches its **Breakeven Volume** ({{key:sc95:BEP}}) when gross contribution covers overhead:

$$Q_{\text{BEP}}^* = \frac{F_{\text{fixed}}}{P - V}$$

Ford W. Harris and R. H. Wilson's **Economic Order Quantity** ({{key:sc95:EOQ}}) balances annual setup cost $S$ against unit holding cost $H$ for annual demand $D$:

* **Calculator Interface:** Primary Key: {{key:sc95:BEP}} • Expression / Workspace: `Breakeven production volume and economic order quantity` • Softkeys: {{keycap:BEP}} {{keycap:EOQ}}


---

### Eq. 25.4 — Calendar Day Count and Settlement Date Mathematics

In fixed-income bond valuation, syndicated loan syndication, commercial paper settlement, and interest rate swaps, cash flow payments depend on exact calendar schedules. The SC-95 provides dedicated calendar arithmetic based on Gregorian Julian Day Number ($\text{JDN}$) algorithms:

1. **Days Between Dates ({{key:sc95:ΔD}}):** With settlement date $\text{Date}_1$ in Register $Y$ and maturity date $\text{Date}_2$ in Register $X$ (entered in either standard financial notation `MM.DDYYYY` or international ISO `YYYY.MMDD`), pressing {{key:sc95:ΔD}} evaluates the exact integer elapsed days:

$$\Delta\text{Days} = \text{JDN}(\text{Date}_2) - \text{JDN}(\text{Date}_1)$$

2. **Date Addition ({{key:sc95:DT+}}):** With a start date $\text{Date}_1$ in Register $Y$ and elapsed integer days $n$ in Register $X$ (or vice versa), pressing {{key:sc95:DT+}} projects the forward or backward calendar settlement date, accounting for varying month lengths and leap years:

$$\text{Date}_{\text{target}} = \text{Gregorian}(\text{JDN}(\text{Date}_1) + n)$$

3. **Date Format Conversion ({{key:sc95:▸YMD}}):** Converts a calendar date in Register $X$ between American financial notation `MM.DDYYYY` and ISO standard notation `YYYY.MMDD`.

* **Calculator Interface:** Primary Keys: {{key:sc95:ΔD}} / {{key:sc95:DT+}} / {{key:sc95:▸YMD}} • Expression / Workspace: `Calendar day count and settlement date math` • Softkeys: {{keycap:ΔD}} {{keycap:DT+}} {{keycap:▸YMD}}


---

### Eq. 26.1 — Fixed-Coupon Bond Present Value Pricing

For a bond with par redemption value $F = 100$, periodic coupon payment $C$, and $N$ remaining periods to maturity discounted at periodic **Yield to Maturity** ($y = Y/100$), the fair market **Bond Price** ({{key:sc95:BND}}, $P_{\text{bond}}$) is the sum of the present value of the coupon stream and the discounted par redemption:

$$P_{\text{bond}} = C\left(\frac{1 - (1 + y)^{-N}}{y}\right) + F(1 + y)^{-N}$$

In the United States corporate and Treasury bond markets, a $10\text{-year}$ bond paying a $5.00\%$ annual coupon rate distributes $C_{\text{semi}} = 2.50$ every six months across $N_{\text{semi}} = 20$ semiannual periods at a periodic yield of $Y_{\text{semi}} = Y_{\text{nom}} / 2 = 3.00\%$ ($y = 0.030$), whereas Eurobonds pay $C_{\text{ann}} = 5.00$ once per year across $N_{\text{ann}} = 10$ annual periods at $Y_{\text{ann}} = 6.00\%$ ($y = 0.060$). When the market yield equals the coupon rate ($y = C/F$), $P_{\text{bond}} = 100.00$ (**par**). When $y > C/F$, $P_{\text{bond}} < 100.00$ (**discount**). And when $y < C/F$, $P_{\text{bond}} > 100.00$ (**premium**).

* **Calculator Interface:** Primary Key: {{key:sc95:BND}} • Expression / Workspace: `BND: Fixed-coupon bond present value pricing` • Softkeys: {{keycap:P}} {{keycap:C}} {{keycap:Y}} {{keycap:N}} {{keycap:F}}


---

### Eq. 26.2 — Macaulay Duration, Modified Duration, and Price Sensitivity

In 1938, Frederick Macaulay defined the effective time horizon of a bond—**Macaulay Duration** ($D_{\text{Mac}}$)—as the present-value-weighted average arrival time of its cash flows, which admits a closed-form algebraic expression in terms of periodic coupon rate $c = C/F$, periodic yield $y$, and period count $N$:

$$D_{\text{Mac,periods}} = \frac{1 + y}{y} - \frac{1 + y + N(c - y)}{c\left[(1 + y)^N - 1\right] + y}$$

Dividing Macaulay Duration (in years) by $(1 + y)$ yields the first-derivative price sensitivity with respect to yield, known as **Modified Duration** ($D_{\text{Mod}}$). For large yield shocks ($\Delta y$), incorporating the second-order **Convexity Adjustment** ($C$) restores exact pricing curvature:

$$\frac{\Delta P}{P} \approx -D_{\text{Mod}} \cdot \Delta y + \frac{1}{2} C (\Delta y)^2$$

* **Calculator Interface:** Primary Key: {{key:sc95:BND}} • Expression / Workspace: `Macaulay duration, convexity, and price sensitivity` • Softkeys: {{keycap:BND}} {{keycap:TVM}}


---

### Eq. 26.3 — Black–Scholes European Option Pricing Model

Assuming the underlying asset price $S_t$ follows geometric Brownian motion $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ with annualized volatility $\sigma$ and continuous risk-free interest rate $r$, Fischer Black, Myron Scholes, and Robert Merton proved in 1973 that the drift rate $\mu$ cancels out of a continuously delta-hedged portfolio. The arbitrage-free price of a European **Call Option** ($C_{\text{call}}$) on a non-dividend-paying asset of spot price $S_0$ with strike price $K$ and time to expiration $T$ (in years) is governed by the standard normal cumulative distribution function $\Phi(z) = \text{pnorm}(z)$ ({{key:sc95:pN}}):

$$C_{\text{call}} = S_0 \, \Phi(d_1) - K e^{-rT} \Phi(d_2)$$

The standardized log-moneyness factors $d_1$ and $d_2$ partition the payoff into asset acquisition and strike cash outflow:

* **Calculator Interface:** Primary Key: {{key:sc95:pN}} • Expression / Workspace: `Black–Scholes European option pricing model` • Softkeys: {{keycap:pN}} {{keycap:qN}}


---

### Eq. 26.4 — Put–Call Parity and European Put Valuation

To prevent static arbitrage between a protective put portfolio ($S_0 + P_{\text{put}}$) and a fiduciary call portfolio ($C_{\text{call}} + K e^{-rT}$)—both of which deliver an identical payoff of $\max(S_T, K)$ at expiration $T$—the European **Put Option** ($P_{\text{put}}$) must satisfy Hans Stoll's (1969) **Put–Call Parity** identity:

$$P_{\text{put}} = C_{\text{call}} - S_0 + K e^{-rT}$$

Evaluating under the standard normal integral yields:

* **Calculator Interface:** Primary Key: {{key:sc95:pN}} • Expression / Workspace: `Put–call parity and European put valuation` • Softkeys: {{keycap:pN}} {{keycap:qN}}


---

### Eq. 27.1 — Sample Variance and Ordinary Least-Squares Linear Regression

Given $n$ paired observations $(x_i, y_i)$ accumulated via the statistical summation operator ({{key:sc95:Σ+}}, with relative share {{key:sc95:%Σ}})—where $x_i$ represents elapsed production hours and $y_i$ represents measured shaft diameter—the sample means $(\bar{x}, \bar{y})$ ({{key:sc95:x̄,ȳ}}) and Bessel-corrected sample standard deviations $(s_x, s_y)$ ({{key:sc95:s,σ}}, with $n - 1$ degrees of freedom in the denominator) pair with the sample covariance $s_{xy}$ to determine the ordinary least-squares **Linear Regression** ({{key:sc95:L.R.}}, binding softkeys {{keycap:ŷ}}, {{keycap:x̂}}, {{keycap:m}}, {{keycap:b}}, {{keycap:r}}) slope $m$, intercept $b$, and Pearson correlation coefficient $r$:

$$\bar{y} = \frac{1}{n}\sum_{i=1}^{n} y_i$$

The least-squares drift velocity $m$ and fitted trendline $\hat{y}(x)$ evaluate as:

* **Calculator Interface:** Primary Key: {{key:sc95:L.R.}} • Expression / Workspace: `Sample variance and ordinary least-squares regression` • Softkeys: {{keycap:ŷ}} {{keycap:x̂}} {{keycap:m}} {{keycap:b}} {{keycap:r}}


---

### Eq. 27.2 — Centered and Asymmetric Process Capability Indices

For a manufacturing process with mean $\mu$ and short-term standard deviation $\sigma$ operating between **Lower Specification Limit** $\text{LSL}$ and **Upper Specification Limit** $\text{USL}$, **Process Potential** ($C_p$) divides the blueprint tolerance width $(\text{USL} - \text{LSL})$ by the natural $6\sigma$ process spread ($\pm 3\sigma$). Because $C_p$ ignores where the mean $\mu$ is located, **Centered Process Capability** ($C_{pk}$) evaluates the upper capability $C_{pu}$ and lower capability $C_{pl}$ separately and takes the minimum—measuring the distance from $\mu$ to the *nearer* specification wall in units of $3\sigma$:

$$C_p = \frac{\text{USL} - \text{LSL}}{6\sigma}$$

When the mean shifts from nominal center, the one-sided and centered capability indices are:

* **Calculator Interface:** Primary Key: {{key:sc95:Cpk}} • Expression / Workspace: `Cpk: C = (U - L) / (6 × S)` • Softkeys: {{keycap:C}} {{keycap:U}} {{keycap:L}} {{keycap:S}}


---

### Eq. 27.3 — Gaussian Tail Scrap Rate and Defect Density

To translate $C_p$ and $C_{pk}$ into expected scrap volume in **Defects Per Million Opportunities** (DPMO), the engineer integrates both normal tails outside $[\text{LSL}, \text{USL}]$ via {{key:sc95:pN}} and multiplies by $1{,}000{,}000$:

$$z_{\text{USL}} = \frac{\text{USL} - \mu}{\sigma} = 3 \cdot C_{pu}$$

The cumulative probability in both rejection tails multiplied by one million defines defect rate:

* **Calculator Interface:** Primary Key: {{key:sc95:pN}} • Expression / Workspace: `Gaussian tail integration and defect density DPMO` • Softkeys: {{keycap:pN}} {{keycap:Cpk}}


---


## Master Cross-Domain Formula Directory Table

The following master reference table compiles all 113 governing equations across the nine StackCalc domain instruments, indexing the equation number, physical title, primary governing expression, and operational softkeys:

| Eq. | Domain & Instrument | Physical Descriptive Title | Primary Governing Expression | Dedicated Softkeys & Workspace |
| :--- | :--- | :--- | :--- | :--- |
| **Eq. 1.1** | SC-35 | Sexagesimal Angular Polynomial | $\theta_{\text{dec}} = D + \frac{M}{60} + \frac{S}{3600}$ | {{keycap:▸HR}} {{keycap:▸HMS}} |
| **Eq. 1.2** | SC-35 | Ravine Slope Reduction | $D_H = S \cos(\nu)$ | {{keycap:SLP}} |
| **Eq. 1.3** | SC-35 | Forward Coordinate Traverse Projection | $\Delta N = D_H \cos(\alpha)$ | {{keycap:TRV}} |
| **Eq. 1.4** | SC-35 | Inverse Coordinate Geometry | $D = \sqrt{(\Delta N)^2 + (\Delta E)^2}$ | {{keycap:INV}} {{keycap:BRG}} |
| **Eq. 1.5** | SC-35 | Bowditch Compass Rule Closure | $E_c = \sqrt{\left(\Sigma_{\Delta N}\right)^2 + \left(\Sigma_{\Delta E}\right)^2}$ | {{keycap:CLS}} {{keycap:PT+}} |
| **Eq. 1.6** | SC-35 | Gauss Shoelace Parcel Area | $A = \frac{1}{2} \left\lvert \sum_{i=1}^{n} \left( E_i N_{i+1} - E_{i+1} N_i \right) \right\rvert$ | {{keycap:△}} {{keycap:▸ac}} {{keycap:▸ha}} |
| **Eq. 2.1** | SC-35 | Circular Curve Tangent and Arc Length | $T = R \tan\!\left(\frac{\Delta}{2}\right)$ | {{keycap:L}} {{keycap:R}} {{keycap:D}} |
| **Eq. 2.2** | SC-35 | Parabolic Vertical Curve Elevation | $\text{Elev}(x) = \text{PVC} + g_1 x + \left(\frac{g_2 - g_1}{2 L}\right) x^2$ | `PVC` `g1` `g2` `L` |
| **Eq. 2.3** | SC-35 | Average End-Area Cut Volume | $V_{\text{cut}} = \frac{A_1 + A_2}{2} \cdot \frac{L_{\text{cut}}}{27}$ | {{keycap:CUT}} {{keycap:STA}} |
| **Eq. 2.4** | SC-35 | Three-Wire Differential Spirit Leveling | $\text{HI} = H + B$ | {{keycap:E}} {{keycap:H}} {{keycap:B}} {{keycap:F}} |
| **Eq. 2.5** | SC-35 | Earth Curvature and Atmospheric Refraction | $h_{cr} = 0.574 \cdot D_{\text{miles}}^2\text{ ft}$ | {{keycap:x²}} {{keycap:×}} |
| **Eq. 3.1** | SC-35 | Orthogonal Wind Vector Decomposition | $V_{\text{hw}} = V_w \cos(\theta)$ | {{keycap:X}} {{keycap:V}} {{keycap:A}} |
| **Eq. 3.2** | SC-35 | Aeronautical Wind Correction Angle | $\text{WCA} = \arcsin\!\left(\frac{V_{\text{xw}}}{V_{\text{TAS}}}\right)$ | {{keycap:XWC}} {{keycap:ASIN}} |
| **Eq. 3.3** | SC-35 | Effective Flight Groundspeed | $\text{GS} = V_{\text{TAS}} \cos(\text{WCA}) - V_{\text{hw}}$ | {{keycap:D}} {{keycap:S}} {{keycap:T}} |
| **Eq. 3.4** | SC-35 | Barometric Density Altitude | $\text{DA} = P + 120 \times \left(T - T_{\text{ISA}}(P)\right)$ | {{keycap:D}} {{keycap:P}} {{keycap:T}} |
| **Eq. 4.1** | SC-14 | Conductor Circular Mil Area and DC Resistance | $\text{CM} = d_{\text{mils}}^2 = \left(1000 \cdot d_{\text{inches}}\right)^2$ | {{keycap:AWG}} {{keycap:Ω}} |
| **Eq. 4.2** | SC-14 | Single-Phase and Three-Phase Feeder Voltage Drop | $V_{\text{drop},1\phi} = \frac{2 \cdot K \cdot L \cdot I}{\text{CM}}$ | {{keycap:D}} {{keycap:R}} {{keycap:L}} {{keycap:I}} |
| **Eq. 4.3** | SC-14 | Harmonic Parallel Resistance | $R_1 \parallel R_2 = \frac{R_1 \cdot R_2}{R_1 + R_2}$ | {{keycap:x∥y}} |
| **Eq. 4.4** | SC-14 | NEC Continuous Load Feeder Ampacity | $I_{\text{min}} = 1.25 \cdot I_{\text{continuous}} + I_{\text{non-continuous}}$ | {{keycap:×}} {{keycap:+}} |
| **Eq. 4.5** | SC-14 | Alternating Current Power Triangle | $P = S \cos(\phi)$ | {{keycap:P}} {{keycap:V}} {{keycap:I}} {{keycap:F}} |
| **Eq. 4.6** | SC-14 | Three-Phase Motor Full-Load Current | $I_{\text{FLA}} = \frac{\text{HP} \times 746}{\sqrt{3} \cdot V_{LL} \cdot \eta}$ | {{keycap:I}} {{keycap:P}} {{keycap:V}} {{keycap:E}} |
| **Eq. 5.1** | SC-14 | Conduit Offset Travel and Half-Angle Shrinkage | $T = \frac{O}{\sin(\theta)} = O \csc(\theta)$ | {{keycap:T}} {{keycap:O}} {{keycap:A}} |
| **Eq. 5.2** | SC-14 | Compound Rolling Offset Travel | $O_{\text{true}} = \sqrt{R_{\text{vert}}^2 + R_{\text{horiz}}^2}$ | {{keycap:FIT}} {{keycap:MIT}} |
| **Eq. 5.3** | SC-14 | Three-Point Saddle Outer Leg Travel | $T_{\text{saddle}} = \frac{O}{\sin(22.5^\circ)} = O \csc(22.5^\circ) \approx 2.6131 \cdot O$ | {{keycap:OFS}} {{keycap:f-i}} |
| **Eq. 5.4** | SC-14 | National Electrical Code Cross-Sectional Raceway Fill | $\text{Fill\%} = \left(\frac{\sum_{k=1}^{N} A_{\text{wire},k}}{A_{\text{conduit}}}\right) \times 100\% \le 40\%$ | {{keycap:AWG}} {{keycap:▦}} |
| **Eq. 6.1** | SC-14 | Spindle Rotational Speed and Table Feed Rate | $N = \frac{12 \cdot \text{SFM}}{\pi \cdot D} \approx \frac{3.8197 \cdot \text{SFM}}{D}$ | {{keycap:N}} {{keycap:S}} {{keycap:D}} |
| **Eq. 6.2** | SC-14 | Bolt Circle Chord Spacing | $C = 2 R \sin\!\left(\frac{180^\circ}{N}\right) = D_{\text{bolt}} \sin\!\left(\frac{180^\circ}{N}\right)$ | {{keycap:C}} {{keycap:D}} {{keycap:N}} |
| **Eq. 6.3** | SC-14 | Control Valve Volumetric Flow and Pump Power | $Q = C_v \sqrt{\frac{\Delta P}{G}}$ | {{keycap:Q}} {{keycap:C}} {{keycap:P}} {{keycap:G}} |
| **Eq. 6.4** | SC-14 | Four-to-Twenty Milliampere Current Scaling | $I_{\text{mA}} = 4.0 + 16.0 \times \left(\frac{\text{Pct}}{100}\right)$ | {{keycap:mA}} {{keycap:RTD}} |
| **Eq. 7.1** | SC-16 | Positional Number Base Radix Expansion | $V = \sum_{i=0}^{k-1} d_i \cdot b^i$ | {{keycap:HEX}} {{keycap:DEC}} {{keycap:OCT}} {{keycap:BIN}} |
| **Eq. 7.2** | SC-16 | Two's Complement Additive Inversion | $-X \equiv 2^W - X \equiv (\sim X) + 1 \pmod{2^W}$ | {{keycap:NEG}} {{keycap:WSZ}} {{keycap:UNS}} |
| **Eq. 7.3** | SC-16 | Contiguous Bitfield Mask Generation | $\text{MSK}(s, w) = \left((1 \ll w) - 1\right) \ll s$ | {{keycap:MSK}} {{keycap:SB}} {{keycap:CB}} {{keycap:B?}} |
| **Eq. 8.1** | SC-16 | IEEE 754 Floating-Point Real Decoding | $V_{\text{float}} = (-1)^S \times \left(1 + \frac{M}{2^{23}}\right) \times 2^{E - 127}$ | {{keycap:FLT}} {{keycap:F16}} {{keycap:F64}} |
| **Eq. 8.2** | SC-16 | Reflected CRC-32 LFSR Step | $C_{i+1} = \begin{cases} (C_i \ggg 1) \oplus G_{\text{poly}} & \text{if } (C_i \ \& \ 1) = 1 \\ C_i \ggg 1 & \text{if } (C_i \ \& \ 1) = 0 \end{cases}$ | {{keycap:CRC}} {{keycap:SWP}} |
| **Eq. 8.3** | SC-16 | CIDR Netmask and Usable Host Capacity | $\text{Netmask}(P) = \left(2^{32} - 2^{32 - P}\right) = \text{0xFFFFFFFF} \ll (32 - P)$ | {{keycap:NET}} {{keycap:MOD}} |
| **Eq. 8.4** | SC-16 | Sixteen-Times Oversampled UART Baud Divisor | $D = \operatorname{round}\!\left(\frac{f_{\text{clk}}}{16 \cdot B}\right)$ | {{keycap:D}} {{keycap:C}} {{keycap:B}} |
| **Eq. 9.1** | SC-16 | Pulse-Width Modulation Carrier Frequency | $f_{\text{PWM}} = \frac{f_{\text{clk}}}{P \cdot \text{ARR}} \iff \text{ARR} = \frac{f_{\text{clk}}}{P \cdot f_{\text{PWM}}}$ | {{keycap:F}} {{keycap:C}} {{keycap:P}} {{keycap:A}} |
| **Eq. 9.2** | SC-16 | Successive-Approximation ADC Quantization | $V_{\text{LSB}} = \frac{V_{\text{ref}}}{2^N}$ | {{keycap:D}} {{keycap:V}} {{keycap:R}} {{keycap:N}} |
| **Eq. 9.3** | SC-16 | Resistor-Capacitor Filter Cutoff and Exponential Settling | $\tau = R \cdot C$ | {{keycap:τ}} {{keycap:fc}} |
| **Eq. 9.4** | SC-16 | Classless Inter-Domain Routing Host Capacity | $\text{Block Size} = 2^{32 - P}$ | {{keycap:NET}} {{keycap:#B}} {{keycap:CLZ}} |
| **Eq. 9.5** | SC-16 | Natural Power-of-Two Memory Bus Alignment | $A_{\text{aligned}} = \left\lceil \frac{A}{B} \right\rceil \times B = (A + B - 1) \ \& \ \sim(B - 1)$ | {{keycap:ALN}} {{keycap:▸KiB}} |
| **Eq. 9.6** | SC-16 | High-Speed Synchronous Bus Timing Margins | $t_{\text{margin,setup}} = T_{\text{clk}} - t_{\text{co,\max}} - t_{\text{prop,\max}} - t_{su} \ge 0$ | {{keycap:-}} {{keycap:+}} |
| **Eq. 10.1** | SC-24 | Sexagesimal Timecode Expansion and Integer Frame Accumulation | $S = 3600 \cdot \text{HH} + 60 \cdot \text{MM} + \text{SS} + \frac{\text{FF}}{R}$ | {{keycap:TC}} {{keycap:FPS}} |
| **Eq. 10.2** | SC-24 | Overcrank Speed Magnification and Shutter Exposure Deficit | $M_{\text{ramp}} = \frac{R_{\text{shoot}}}{R_{\text{play}}}$ | {{keycap:FPS}} {{keycap:SHT}} |
| **Eq. 10.3** | SC-24 | NTSC Color Pulldown and Wall-Clock Drift Rate | $R_{\text{NTSC}} = \frac{30}{1.001} = \frac{30{,}000}{1001} \approx 29.97003\text{ fps}$ | {{keycap:DF}} {{keycap:TC}} |
| **Eq. 10.4** | SC-24 | SMPTE Drop-Frame Label Skip and Physical Frame Index | $N_{\text{dropped}} = 2 \times \left(M_{\text{total}} - \left\lfloor \frac{M_{\text{total}}}{10} \right\rfloor\right)$ | {{keycap:TC}} {{keycap:+TC}} {{keycap:-TC}} |
| **Eq. 11.1** | SC-24 | Rectilinear Field of View and Scene Coverage | $A = 2 \arctan\left(\frac{W}{2F}\right)$ | {{keycap:A}} {{keycap:W}} {{keycap:F}} |
| **Eq. 11.2** | SC-24 | Hyperfocal Distance and Conjugate Depth-of-Field Boundaries | $H = \frac{F^2}{N \cdot C}$ | {{keycap:H}} {{keycap:F}} {{keycap:N}} {{keycap:C}} |
| **Eq. 11.3** | SC-24 | Exposure Value, Rotary Shutter Integration, and Neutral Density | $E = \log_2\left(\frac{N^2}{T}\right)$ | {{keycap:E}} {{keycap:N}} {{keycap:T}} {{keycap:▸ND}} |
| **Eq. 11.4** | SC-24 | Flicker-Free Shutter Angle and Integration Period | $T_{180^\circ} = \frac{1}{2 \cdot \text{FPS}}$ | {{keycap:SHT}} {{keycap:FLK}} |
| **Eq. 11.5** | SC-24 | Inverse-Square Illuminance and Micro-Reciprocal Degree Gel Shift | $E_{\text{lx}} = \frac{I}{D^2}$ | {{keycap:E}} {{keycap:I}} {{keycap:D}} {{keycap:▸fc}} |
| **Eq. 12.1** | SC-24 | Thermal Speed of Sound and Acoustic Propagation Delay | $v_s(T_C) = 331.3 + 0.606 \cdot T_C \quad \left[\frac{\text{m}}{\text{s}}\right]$ | {{keycap:vₛ}} {{keycap:DLY}} |
| **Eq. 12.2** | SC-24 | Sabine Reverberation Time | $RT_{60} = \frac{0.161 \cdot V}{A} = \frac{0.161 \cdot V}{\sum_{i} S_i \alpha_i}$ | `V` `A` |
| **Eq. 12.3** | SC-24 | Spherical Spreading Attenuation and Acoustic Reach | $L_2 = L_1 - 20 \log_{10}\left(\frac{D_2}{D_1}\right)$ | {{keycap:SPL}} {{keycap:dB}} |
| **Eq. 12.4** | SC-24 | Incoherent Acoustic Decibel Addition and Studio Voltage Levels | $L_{\Sigma,\text{incoherent}} = 10 \log_{10}\left(10^{L_1 / 10} + 10^{L_2 / 10}\right)$ | {{keycap:dB}} {{keycap:SPL}} |
| **Eq. 13.1** | SC-50 | Decibel-Milliwatt Power Scaling and Root-Mean-Square Line Voltage | $P_{\text{dBm}} = 10 \log_{10}\left(\frac{P_{\text{mW}}}{1\text{ mW}}\right) = 10 \log_{10}(P_{\text{W}}) + 30$ | {{keycap:dBm}} {{keycap:▸dBm}} {{keycap:▸dBW}} |
| **Eq. 13.2** | SC-50 | Complex Voltage Reflection Coefficient and Standing Wave Ratio | $\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0} = \lvert\Gamma\rvert\angle\theta$ | {{keycap:Γ}} {{keycap:SWR}} |
| **Eq. 13.3** | SC-50 | Return Loss and Mismatch Loss | $\text{RL}_{\text{dB}} = -20 \log_{10}\lvert\Gamma\rvert$ | {{keycap:RL}} {{keycap:SWR}} |
| **Eq. 13.4** | SC-50 | High-Frequency Conductor Skin Depth | $\delta = \sqrt{\frac{\rho}{\pi f \mu}} = \sqrt{\frac{1}{\pi f \sigma \mu_0 \mu_r}}$ | {{keycap:√x}} {{keycap:÷}} {{keycap:×}} |
| **Eq. 13.5** | SC-50 | Quarter-Wave Matching Transformer and Physical Stub Length | $\ell_{\lambda/4} = \frac{\lambda}{4} \cdot \text{VF} = \frac{c}{4 f} \cdot \text{VF}$ | {{keycap:TLN}} {{keycap:λ/L}} |
| **Eq. 13.6** | SC-50 | L-Network Matching Reactances and LC Resonance | $Q = \sqrt{\frac{R_{\text{high}}}{R_{\text{low}}} - 1}$ | {{keycap:F}} {{keycap:L}} {{keycap:C}} |
| **Eq. 14.1** | SC-50 | Friis Free-Space Path Loss | $\text{FSPL}_{\text{dB}} = 20 \log_{10}(d_{\text{km}}) + 20 \log_{10}(f_{\text{MHz}}) + 32.44$ | {{keycap:L}} {{keycap:D}} {{keycap:F}} |
| **Eq. 14.2** | SC-50 | Logarithmic RF Link Budget and Fade Margin | $P_{\text{rx,dBm}} = P_{\text{tx,dBm}} + G_{\text{dB}} - L_{\text{dB}}$ | {{keycap:R}} {{keycap:P}} {{keycap:G}} {{keycap:L}} |
| **Eq. 14.3** | SC-50 | First Fresnel Zone Midpoint Radius and Clearance Criterion | $r_1 = \sqrt{\frac{\lambda \cdot d}{4}} = 8.656 \sqrt{\frac{d_{\text{km}}}{f_{\text{GHz}}}}\quad [\text{m}]$ | {{keycap:F₁}} {{keycap:LNK}} |
| **Eq. 15.1** | SC-50 | Johnson–Nyquist Thermal Noise Floor | $N_{\text{floor,dBm}} = 10 \log_{10}(k_B T_0 \cdot 1000) + 10 \log_{10}(B_{\text{Hz}}) \approx -173.977 + 10 \log_{10}(B_{\text{Hz}})$ | {{keycap:Pₙ}} {{keycap:T₀}} {{keycap:kB}} |
| **Eq. 15.2** | SC-50 | Friis Cascaded Noise Factor | $F_{\text{tot}} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \dots$ | {{keycap:F}} {{keycap:A}} {{keycap:B}} {{keycap:G}} |
| **Eq. 15.3** | SC-50 | Spurious-Free Dynamic Range | $\text{SFDR}_{\text{dB}} = \frac{2}{3}\left(\text{IIP3}_{\text{dBm}} - N_{\text{floor,dBm}}\right)$ | {{keycap:IP3}} {{keycap:FDR}} |
| **Eq. 15.4** | SC-50 | Shannon–Hartley Channel Capacity and Spectral Efficiency | $C = B \log_2\left(1 + \text{SNR}\right) \quad [\text{bps}]$ | {{keycap:C}} {{keycap:B}} {{keycap:S}} |
| **Eq. 15.5** | SC-50 | Doppler Velocity Shift and Fourth-Power Radar Echo | $\Delta f_{\text{1-way}} = \frac{f_0 \cdot v}{c}$ | {{keycap:Δf}} {{keycap:RCS}} |
| **Eq. 16.1** | SC-60 | Gravimetric Solute Mass and Molar Mass Summation | $M = \sum_{i} \nu_i A_i \quad \left[\frac{\text{g}}{\text{mol}}\right]$ | {{keycap:W}} {{keycap:N}} {{keycap:M}} {{keycap:Z}} |
| **Eq. 16.2** | SC-60 | Elemental Mass Percentage and Hydrate Molar Mass | $\text{WT\%}_i = \frac{\nu_i A_i}{M} \times 100\%$ | {{keycap:w/w}} {{keycap:MW}} |
| **Eq. 16.3** | SC-60 | Volumetric Solution Molarity and Solute Mass | $C = \frac{n}{V} = \frac{W}{M \cdot V}$ | {{keycap:N}} {{keycap:C}} {{keycap:V}} |
| **Eq. 16.4** | SC-60 | Conservation of Solute Moles in Stock Dilution | $C_1 V_1 = C_2 V_2 \iff V_1 = \frac{C_2 V_2}{C_1}$ | {{keycap:C}} {{keycap:V}} {{keycap:D}} {{keycap:U}} |
| **Eq. 16.5** | SC-60 | Serial Pipetting Error Propagation | $\frac{\sigma_{C_k}}{C_k} \approx \sqrt{k}\,\left(\frac{\sigma_V}{V}\right)$ | {{key:√x}} {{key:×}} |
| **Eq. 16.6** | SC-60 | Colligative Freezing Point Depression | $\Delta T_f = i \cdot K_f \cdot m$ | {{keycap:MW}} {{keycap:×}} |
| **Eq. 17.1** | SC-60 | Sørensen Logarithmic Acidity and Acid Dissociation Constant | $\text{pH} = -\log_{10}[\text{H}^+] \iff [\text{H}^+] = 10^{-\text{pH}}$ | {{keycap:pH}} {{keycap:pKₐ}} |
| **Eq. 17.2** | SC-60 | Henderson–Hasselbalch Buffer Equilibrium | $\text{pH} = \text{p}K_a + \log_{10}\left(\frac{[\text{A}^-]}{[\text{HA}]}\right)$ | {{keycap:P}} {{keycap:K}} {{keycap:A}} {{keycap:H}} |
| **Eq. 17.3** | SC-60 | Van Slyke Buffer Capacity and Species Partitioning | $\beta = 2.303\left([\text{H}^+] + [\text{OH}^-] + \frac{C_{\text{buf}} K_a [\text{H}^+]}{(K_a + [\text{H}^+])^2}\right)$ | {{keycap:BUF}} |
| **Eq. 17.4** | SC-60 | Buffer Acid-Spike Shift and Neutralization | $\Delta\text{pH} = \text{pH}_{\text{new}} - \text{pH}_{\text{init}}$ | {{keycap:BUF}} {{keycap:pH}} |
| **Eq. 17.5** | SC-60 | Volumetric Titration Equivalence Point | $V_{\text{titrant}} = \frac{C_{\text{analyte}} V_{\text{analyte}}}{C_{\text{titrant}}}$ | {{keycap:EQV}} {{keycap:RXN}} |
| **Eq. 18.1** | SC-60 | Beer–Lambert Spectrophotometric Absorbance | $A = -\log_{10}(T) = \varepsilon \cdot b \cdot c$ | {{keycap:A}} {{keycap:E}} {{keycap:B}} {{keycap:C}} {{keycap:%T}} |
| **Eq. 18.2** | SC-60 | Arrhenius Thermal Reaction Acceleration Ratio | $\frac{k_2}{k_1} = \exp\left[\frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right]$ | {{keycap:Eₐ}} {{keycap:R}} |
| **Eq. 18.3** | SC-60 | Relative Centrifugal Force and Rotor Speed | $\text{RCF} \approx 1.118 \times 10^{-5} \cdot r_{\text{cm}} \cdot \text{RPM}^2$ | {{keycap:RCF}} {{keycap:RPM}} |
| **Eq. 19.1** | SC-78 | Baker's Percentage Mass Ratio and Ingredient Weight | $P_i = \left(\frac{I_i}{F}\right) \times 100$ | {{keycap:P}} {{keycap:I}} {{keycap:F}} {{keycap:ΣW}} |
| **Eq. 19.2** | SC-78 | Desired Dough Water Temperature and Friction Balance | $W = 3 D - R - F - M$ | {{keycap:W}} {{keycap:D}} {{keycap:R}} {{keycap:F}} {{keycap:M}} |
| **Eq. 19.3** | SC-78 | Latent-Heat Flake Ice Mass Substitution | $W_{\text{ice}} = \frac{W_{\text{water}} \cdot \left(T_{\text{tap}} - W\right)}{80}$ | {{keycap:ICE}} {{keycap:Tw}} |
| **Eq. 20.1** | SC-78 | Specific Gravity and Extract Conversion | $\text{SG} = 1 + \frac{B}{258.6 - \left(\frac{B}{258.2}\right) \times 227.1}$ | {{keycap:▸SG}} {{keycap:▸Brx}} {{keycap:▸°P}} |
| **Eq. 20.2** | SC-78 | Apparent Attenuation and Alcohol by Volume | $\text{ATT}_{\%} = \left(\frac{O - F}{O - 1.000}\right) \times 100$ | {{keycap:A}} {{keycap:O}} {{keycap:F}} |
| **Eq. 20.3** | SC-78 | Tinseth Hop Bitterness and Utilization Kinetics | $I = \frac{W_{\text{g}} \cdot A \cdot U \cdot 1000}{V_{\text{L}}}$ | {{keycap:I}} {{keycap:W}} {{keycap:A}} {{keycap:U}} {{keycap:V}} |
| **Eq. 21.1** | SC-78 | Compounding Fabrication Yield and Edible Mass | $y_{\text{cum}} = \prod_{k=1}^{m} y_k = \prod_{k=1}^{m} \left(1 - \ell_k\right)$ | {{keycap:YLD}} {{keycap:SCL}} |
| **Eq. 21.2** | SC-78 | Yield-Adjusted Edible Portion Unit Cost | $C_{\text{EP}} = \frac{C_{\text{AP}}}{y_{\text{cum}}} = \frac{C_{\text{AP}}}{\prod_{k=1}^{m} y_k}$ | {{keycap:P}} {{keycap:C}} {{keycap:F}} |
| **Eq. 21.3** | SC-78 | Food Cost to Gross Margin Hyperbolic Mapping | $f = \frac{C}{P} \iff P = \frac{C}{f} = \frac{C}{1 - m} = C \left(1 + u\right)$ | {{keycap:PRC}} {{keycap:CST}} |
| **Eq. 22.1** | SC-80 | Mosteller Body Surface Area and Inversion | $B = \sqrt{\frac{H \cdot W}{3600}}$ | {{keycap:B}} {{keycap:H}} {{keycap:W}} {{keycap:PAT}} |
| **Eq. 22.2** | SC-80 | Devine Ideal Body Weight and Adipose Adjustment | $\text{IBW}_{\text{male}} = 50.0 + 2.3\left(\frac{H}{2.54} - 60\right)$ | {{keycap:IBW}} {{keycap:ABW}} {{keycap:BMI}} |
| **Eq. 22.3** | SC-80 | Cockcroft–Gault Creatinine Clearance Estimation | $C_{\text{male}} = \frac{\left(140 - A\right) \cdot W}{72 \cdot S}$ | {{keycap:C}} {{keycap:A}} {{keycap:W}} {{keycap:S}} |
| **Eq. 22.4** | SC-80 | Holliday–Segar Pediatric 4-2-1 Fluid Maintenance | $R_{\text{maint,mL/hr}} = \begin{cases} 4 \cdot W & \text{if } W \le 10 \\ 40 + 2\left(W - 10\right) & \text{if } 10 < W \le 20 \\ 60 + 1\left(W - 20\right) & \text{if } W > 20 \end{cases}$ | {{keycap:IV}} {{keycap:DOS}} |
| **Eq. 23.1** | SC-80 | Continuous Vasoactive Mass Flux to Volumetric Pump Rate | $R = \frac{D \cdot W \cdot 60}{C} \iff D = \frac{R \cdot C}{60 \cdot W}$ | {{keycap:R}} {{keycap:D}} {{keycap:W}} {{keycap:C}} |
| **Eq. 23.2** | SC-80 | Gravity Drop Frequency from Volumetric Flow | $R_{\text{gtt/min}} = \frac{R_{\text{mL/hr}} \cdot DF_{\text{gtt/mL}}}{60}$ | {{keycap:gtt}} {{keycap:DRP}} |
| **Eq. 23.3** | SC-80 | Mean Arterial Pressure and Parkland Resuscitation | $\text{MAP} = \text{DBP} + \frac{1}{3}\left(\text{SBP} - \text{DBP}\right) = \frac{\text{SBP} + 2 \cdot \text{DBP}}{3}$ | {{keycap:ICU}} {{keycap:BRN}} |
| **Eq. 24.1** | SC-80 | One-Compartment First-Order Elimination Kinetics | $C(t) = C_0 \, e^{-K t}$ | {{keycap:T}} {{keycap:V}} {{keycap:C}} |
| **Eq. 24.2** | SC-80 | Multi-Dose Steady-State Accumulation Factor | $R_{\text{acc}} = \sum_{j=0}^{\infty} e^{-j K \tau} = \frac{1}{1 - e^{-K \tau}}$ | {{keycap:PK}} {{keycap:DOS}} |
| **Eq. 24.3** | SC-80 | Bazett Heart Rate-Corrected QT Interval | $\text{QT}_c = \frac{\text{QT}_{\text{ms}}}{\sqrt{60 / \text{HR}}}$ | {{keycap:QTc}} |
| **Eq. 24.4** | SC-80 | Compressed Medical Oxygen Cylinder Remaining Duration | $T_{\text{min}} = \frac{\left(P_{\text{psi}} - 200\right) \times 0.28}{F}$ | {{keycap:O₂}} |
| **Eq. 25.1** | SC-95 | Five-Variable Time Value of Money Governing Equation | $\text{PV} + \text{PMT}\left(\frac{1 - (1 + i)^{-N}}{i}\right) + \text{FV}(1 + i)^{-N} = 0$ | {{keycap:N}} {{keycap:I%}} {{keycap:PV}} {{keycap:PMT}} {{keycap:FV}} |
| **Eq. 25.2** | SC-95 | Uniform Series Net Present Value and Internal Rate of Return | $\text{NPV} = C\left(\frac{1 - (1 + r)^{-N}}{r}\right) - I_0$ | {{keycap:V}} {{keycap:C}} {{keycap:R}} {{keycap:N}} {{keycap:I}} |
| **Eq. 25.3** | SC-95 | Breakeven Production Volume and Economic Order Quantity | $Q_{\text{BEP}}^* = \frac{F_{\text{fixed}}}{P - V}$ | {{keycap:BEP}} {{keycap:EOQ}} |
| **Eq. 26.1** | SC-95 | Fixed-Coupon Bond Present Value Pricing | $P_{\text{bond}} = C\left(\frac{1 - (1 + y)^{-N}}{y}\right) + F(1 + y)^{-N}$ | {{keycap:P}} {{keycap:C}} {{keycap:Y}} {{keycap:N}} {{keycap:F}} |
| **Eq. 26.2** | SC-95 | Macaulay Duration, Modified Duration, and Price Sensitivity | $D_{\text{Mac,periods}} = \frac{1 + y}{y} - \frac{1 + y + N(c - y)}{c\left[(1 + y)^N - 1\right] + y}$ | {{keycap:BND}} {{keycap:TVM}} |
| **Eq. 26.3** | SC-95 | Black–Scholes European Option Pricing Model | $C_{\text{call}} = S_0 \, \Phi(d_1) - K e^{-rT} \Phi(d_2)$ | {{keycap:pN}} {{keycap:qN}} |
| **Eq. 26.4** | SC-95 | Put–Call Parity and European Put Valuation | $P_{\text{put}} = C_{\text{call}} - S_0 + K e^{-rT}$ | {{keycap:pN}} {{keycap:qN}} |
| **Eq. 27.1** | SC-95 | Sample Variance and Ordinary Least-Squares Linear Regression | $\bar{y} = \frac{1}{n}\sum_{i=1}^{n} y_i$ | {{keycap:ŷ}} {{keycap:x̂}} {{keycap:m}} {{keycap:b}} {{keycap:r}} |
| **Eq. 27.2** | SC-95 | Centered and Asymmetric Process Capability Indices | $C_p = \frac{\text{USL} - \text{LSL}}{6\sigma}$ | {{keycap:C}} {{keycap:U}} {{keycap:L}} {{keycap:S}} |
| **Eq. 27.3** | SC-95 | Gaussian Tail Scrap Rate and Defect Density | $z_{\text{USL}} = \frac{\text{USL} - \mu}{\sigma} = 3 \cdot C_{pu}$ | {{keycap:pN}} {{keycap:Cpk}} |
