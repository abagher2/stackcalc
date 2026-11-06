---
title: "Unit I: Geomatics, Land Surveying & Flight Navigation"
description: "Three narrative-problem chapters covering coordinate geometry (COGO), sexagesimal bearings, polygon traverse closure, circular and vertical route curves, differential spirit leveling, and aeronautical wind triangles on the SC-35."
---

# Unit I: Geomatics, Land Surveying & Flight Navigation

In the autumn of 1763, the English astronomer Charles Mason and the surveyor Jeremiah Dixon landed at Philadelphia with a six-foot brass zenith sector crafted by John Bird and a surveyor's transit fitted with a micrometer screw. Commissioned to resolve an eighty-year border dispute between the Penn and Calvert families across the timbered ridges and tidal marshes of the Chesapeake peninsula, Mason and Dixon could not stretch an iron chain along an idealized paper parallel. In a classroom, points reside on a frictionless Cartesian plane where the horizontal $+x$ axis points East, the vertical $+y$ axis points North, and angles sweep counterclockwise from the positive horizontal axis. In the field, dense forests, steep ravines, and atmospheric refraction force a survey crew to anchor every sightline to the stars and the Earth's rotation axis. Within a decade of Mason and Dixon's survey, the London instrument maker Jesse Ramsden perfected his geared circular dividing engine (1775), engraving brass horizontal circles to fractions of an arcminute so compact optical theodolites could carry celestial meridian accuracy across continents.

Because navigation on land and sea grew around the magnetic compass and the meridian of Polaris, field geometry reverses both reference conventions of the classroom unit circle. When a surveyor levels a theodolite over a brass monument or an aviator reads a directional gyroscope, the zero reference line ($0^\circ$) is **True North** (or Grid North on a planar state projection) rather than East, and the graduated azimuth circle increases **clockwise** through $90^\circ$ at East, $180^\circ$ at South, and $270^\circ$ at West. Starting at the vertical axis and rotating clockwise reflects the coordinate plane across the $45^\circ$ Northeast diagonal and **swaps the roles of sine and cosine**: North-South displacement (**Latitude**, $\Delta N$) projects along the cosine of the azimuth, while East-West displacement (**Departure**, $\Delta E$) projects along the sine of the azimuth. Whenever a coordinate pair must be transposed between $(N, E)$ and $(E, N)$ conventions, the coordinate swap key `{{key:N⇄E}}` (or standard RPN swap `{{key:x⇄y}}`) exchanges Registers $X$ and $Y$ in a single keystroke.

The physical lever arm of a terrestrial sightline also explains why surveyors and navigators preserve **sexagesimal notation** (Degrees, Minutes, and Seconds `DDD.MMSS`, where $1^\circ = 60'$ and $1' = 60''$, converted via `{{key:▸DEG}}`, `{{key:▸HR}}`, and `{{key:▸HMS}}`) alongside architectural **feet, whole inches, and binary fractions** (`{{key:f-i}}`) and historic land units (`{{key:▸ch}}` for 66-foot Gunter's chains, `{{key:▸rod}}` for 16.5-foot rods, `{{key:▸ac}}` for statutory acres, and `{{key:▸ha}}` for metric hectares). One arcsecond ($1'' = 1/3600^\circ$) is the angle subtended by a United States quarter coin viewed from just over three miles ($5\text{ km}$) away. Over a routine boundary sightline of $2{,}000\text{ ft}$, an angular error of a single arcminute ($1'$) shifts the far stake laterally by $2000 \sin(1') \approx 0.582\text{ ft}$ ($\approx 7\text{ inches}$), and an angular rounding error of $0.05^\circ$ ($3'$) displaces a corner monument by nearly two feet.

To support both rapid field reductions and inverse boundary or route design, the **SC-35 Geomatics, Land Surveying & Flight Navigation** instrument combines three architectural pillars: configurable stack depth (`4-LV`, `8-LV`, or `INF` deep stack cycled on Flag 5 `5:DEP` inside `{{key:FLAGS}}` so register capacity is never a bottleneck), dual-mode domain keys that execute immediate stack projections when operands sit in Registers $Y$ and $X$ or open a bidirectional Equation Solver workspace (`{{key:SOLVE}}` / `{{key:XEQ}}` with dynamic softkeys `{{key:LFU0}}`–`{{key:LFU5}}` that morph into variable softkeys inside `TSD`, `FLW`, `LVL`, `TRI`, `CG`, `HCRV`, `WIND`, and `ALT`), and native `DDD.MMSS` / `{{key:f-i}}` parsers paired with the live `@COGO` coordinate and polygon area/closure ledger (`{{key:▦}}`). Across the three narrative chapters of this Unit, we follow the `SC-35` from an 18th-century boundary retracement in the New Jersey Pine Barrens, up a switchback highway alignment and spirit-leveling loop through a granite canyon, and onto the flight deck of a twin-turboprop battling a mountain crosswind at night:

| Chapter | Narrative Problem | Mathematical Concepts | Domain Keys & Workspaces |
| :--- | :--- | :--- | :--- |
| **Chapter 1** | Retracing an 18th-century timber boundary across a steep $6^\circ 15'$ ravine to recover a buried brass monument, check three-wire stadia leveling, and verify parcel acreage | Sexagesimal conversions, slope reduction, North-clockwise forward/inverse COGO, Bowditch closure, three-wire stadia, and Gauss's shoelace formula | `{{key:▸DEG}}`, `{{key:▸HMS}}`, `{{key:▸HR}}`, `{{key:f-i}}`, `{{key:SLP}}`, `{{key:TRV}}`, `{{key:INV}}`, `{{key:BRG}}`, `{{key:PT+}}`, `{{key:CLS}}`, `{{key:△}}`, `{{key:LVL}}`, `{{key:▦}}`, `{{key:▸ac}}`, `{{key:▸ha}}`, `{{key:▸ch}}`, `{{key:▸rod}}` |
| **Chapter 2** | Designing a tangential mountain highway curve ($R = 1{,}200\text{ ft}$, $\Delta = 28.5^\circ$), parabolic vertical curve, and trapezoidal earthwork cut while leveling up the canyon wall | Circular horizontal curve layout, parabolic vertical curve elevations, earthwork prism volume, three-wire stadia spirit leveling, stationing, and roadway grade | `{{key:CRV}}`, `{{key:VCV}}`, `{{key:CUT}}`, `{{key:LVL}}`, `{{key:STA}}`, `{{key:GR%}}`, `{{key:FLW}}`, `{{key:▸m}}`, `{{key:▸GRD}}` |
| **Chapter 3** | Flying a twin-turboprop across a high-desert ridge against a $28\text{ kt}$ wind at $40^\circ$ off course into a $6{,}200\text{ ft}$ pressure-altitude mountain strip at $28^\circ\text{C}$ | Aeronautical velocity vector triangles, crab angle, time-speed-distance endurance, aircraft center-of-gravity moment, and barometric/density altitude | `{{key:WND}}`, `{{key:XWC}}`, `{{key:ALT}}`, `{{key:TSD}}`, `{{key:CG}}`, `{{key:▸NM}}`, `{{key:▸kt}}` |

---

# Chapter 1: The Lost Cornerstone in the Pine Barrens

On a crisp November morning in the Wharton Tract of southern New Jersey's Pine Barrens, a two-person boundary crew stands beside a charred pitch-pine stump with a 1794 metes-and-bounds deed unrolled across the hood of their truck. A timber holding company and the state park service are adjudicating the southeastern corner of a historic bog-iron furnace tract. The original colonial surveyor recorded the boundary in Edmund Gunter's 66-foot chains (`{{key:▸ch}}`), sexagesimal compass bearings (`DDD.MMSS`), and stone-wall offsets measured in feet and fractional inches (`{{key:f-i}}`), terminating at a brass-capped granite cornerstone set beside a cedar creek. Over two centuries of wildfire and alluvial wash have buried the cornerstone beneath three feet of sandy loam on the far side of a cedar-choked ravine.

To recover the buried monument and certify the parcel's legal acreage for the county register of deeds, the party chief cannot stretch a flat steel tape across the gulf. Instead, the crew sets their total station over Witness Station $A$ on the north rim, sights along azimuth $47^\circ 22' 30''$ (`47.2230` in `DDD.MMSS`, or $47.375^\circ$ via `{{key:▸DEG}}`) across an inclined slope distance of $412.68\text{ ft}$ at a vertical slope angle of $6^\circ 15' 00''$ (`6.1500` in `DDD.MMSS`, or $6.25^\circ$), reduces that inclined shot to flat horizontal ground distance $D_H = 410.10\text{ ft}$ and vertical rise $\Delta V = 44.92\text{ ft}$ (`{{key:SLP}}`), and projects North and East coordinates (`{{key:TRV}}`) toward the witness oak on the opposite bluff. From the recovered coordinates of the witness oak and the historic corners, they must compute the inverse azimuth and distance (`{{key:INV}}`, `{{key:BRG}}`) to drive a magnetic locator probe straight down onto the buried brass cap, verify benchmark rod readings with three-wire stadia leveling (`{{key:LVL}}`), close the boundary polygon around the tract (`{{key:PT+}}`, `{{key:CLS}}`), and inspect the enclosed shoelace area (`{{key:▦}}`, `{{key:△}}`, `{{key:▸ac}}`, `{{key:▸ha}}`).

---

## Sexagesimal Sightlines, Slope Reduction, and North-Clockwise Projections

Every boundary retracement begins by translating raw optical circle readings, architectural stone-wall ties, and inclined laser rangefinder shots into consistent decimal degrees and horizontal surveyor's feet on a local tangent plane. Once reduced to the horizontal plane, each sightline projects along the North-clockwise azimuth circle into orthogonal Northing and Easting displacements.

### Sexagesimal Angles, Architectural Lengths, and Ravine Slope Reduction

A sexagesimal angle read from a theodolite glass circle or historic deed plat consists of integer degrees $D^\circ$, integer arcminutes $M' \in [0, 59]$, and arcseconds $S'' \in [0, 60)$. Because one degree contains $60$ arcminutes and $60 \times 60 = 3{,}600$ arcseconds, converting between packed sexagesimal notation `DDD.MMSS` (where the first two digits after the decimal point store arcminutes `MM` and the next two store arcseconds `SS`, converted directly via `{{key:▸DEG}}` / `{{key:▸HR}}` and `{{key:▸HMS}}`) and decimal degrees $\theta_{\text{dec}}$ evaluates the base-$60$ polynomial:

$$\theta_{\text{dec}} = D + \frac{M}{60} + \frac{S}{3600}$$

In this expression, $D$ is the whole-degree component, $M$ is the arcminute count divided by $60\text{ min/deg}$, and $S$ is the arcsecond count divided by $3{,}600\text{ sec/deg}$. For a historic deed azimuth of $47^\circ 22' 30''$ (written in packed field notation as `47.2230`), dividing the $22$ arcminutes by $60$ yields $0.366667^\circ$, dividing the $30$ arcseconds by $3{,}600$ yields $0.008333^\circ$, and summing with $47^\circ$ via `{{key:▸DEG}}` produces $\theta_{\text{dec}} = \mathbf{47.375^\circ}$. Reversing the conversion via `{{key:▸HMS}}` on $47.375^\circ$ extracts the integer part $D = 47^\circ$, multiplies the fractional remainder $0.375 \times 60 = 22.5'$ to isolate $M = 22'$, and multiplies the remaining $0.5' \times 60 = 30''$ to recover `47.2230` ($47^\circ 22' 30''$).

Linear tie measurements between colonial stone walls, iron witness pipes, and Gunter's chain calls ($1\text{ chain} = 4\text{ rods} = 66.0\text{ ft}$, converted via `{{key:▸ch}}` and `{{key:▸rod}}`) require a companion bridge between trades. Geodetic coordinates express length in **surveyor's decimal feet** ($L_{\text{ft}}$, graduated in tenths and hundredths of a foot), whereas structural foundations and masonry ties specify **whole feet $F$, whole inches $I$, and binary fractional inches $N/D$** with denominator $D \in \{2, 4, 8, 16, 32, 64\}$ (operational shorthand `{{key:f-i}}`):

$$L_{\text{ft}} = F + \frac{I + \frac{N}{D}}{12}$$

Here $F$ represents whole feet, $I$ represents whole inches, and $N/D$ represents the binary fraction of an inch divided by $12\text{ in/ft}$. When the 1794 furnace plat calls for a witness offset of $24\text{ ft } 9\text{-}3/8\text{ in}$ from the millrace foundation wall, combining the fractional inch $3/8 = 0.375\text{ in}$ with $9\text{ in}$ gives $9.375\text{ in}$, dividing by $12\text{ in/ft}$ via `{{key:f-i}}` yields $0.78125\text{ ft}$, and adding $24\text{ ft}$ produces the surveyor's coordinate length $L_{\text{ft}} = \mathbf{24.78125\text{ ft}}$.

![Right-triangle trigonometric reduction of inclined slope distance S to horizontal ground distance H and vertical elevation difference V.](../assets/diagrams/domains/diagram_ch01_slope.png)

When the total station on the north rim of the Pine Barrens ravine sights a prism across an inclined **slope distance** $S$ at a vertical slope angle $\nu$ (measured above $+$ or below $-$ the horizontal horizon), legal property boundaries and map projections depend on the flat **horizontal ground distance** $D_H$ and the **vertical elevation difference** $\Delta V$ (operational shorthand `{{key:SLP}}`):

$$D_H = S \cos(\nu), \qquad \Delta V = S \sin(\nu)$$

In this right-triangle reduction, $S$ is the slant range in Register $Y$, $\nu$ is the vertical inclination angle in Register $X$, $D_H$ is the reduced horizontal distance placed into Register $X$, and $\Delta V$ is the vertical elevation difference placed into Register $Y$. Sighting across the cedar ravine over a slope distance of $S = 412.68\text{ ft}$ at a vertical angle of $\nu = 6^\circ 15' 00''$ (`6.15` in `DDD.MMSS`, or $6.25^\circ$ via `{{key:▸DEG}}`) projects a horizontal ground distance of $D_H = \mathbf{410.10\text{ ft}}$ in Register $X$ and a vertical elevation difference of $\Delta V = \mathbf{44.92\text{ ft}}$ in Register $Y$.

### The North-Clockwise Meridian Frame and Forward Coordinate Projection

In plane surveying, every boundary station is indexed by an ordered pair of orthogonal coordinates $(N, E)$, where **Northing** ($N$) measures distance north of a reference origin and **Easting** ($E$) measures distance east of the origin, while directions are measured as a full-circle **Azimuth** $\alpha \in [0^\circ, 360^\circ)$ clockwise from True North ($0^\circ$). Projecting a known horizontal ground distance $D_H$ along a known clockwise azimuth $\alpha$ from a starting station $A(N_A, E_A)$ to determine the North change ($\Delta N$, **Latitude**), the East change ($\Delta E$, **Departure**), and the target coordinates $B(N_B, E_B)$ constitutes the **Forward Coordinate Geometry Problem** (`{{key:TRV}}`):

![North-clockwise geodetic azimuth frame and orthogonal decomposition of sightline distance D into latitude change and departure.](../assets/diagrams/domains/diagram_ch01_fwd_cogo.png)

$$\Delta N = D_H \cos(\alpha), \qquad \Delta E = D_H \sin(\alpha), \qquad N_B = N_A + \Delta N, \qquad E_B = E_A + \Delta E$$

Because $\cos\alpha$ is positive in the northern quadrants ($270^\circ < \alpha < 90^\circ$) and negative in the southern quadrants ($90^\circ < \alpha < 270^\circ$), while $\sin\alpha$ is positive in the eastern quadrants ($0^\circ < \alpha < 180^\circ$) and negative in the western quadrants ($180^\circ < \alpha < 360^\circ$), these North-clockwise projection identities assign the correct algebraic signs in all four compass quadrants without manual lookup tables. This orthogonal decomposition of a polar vector $(\alpha, D_H)$ into coupled cosine and sine components is mathematically identical to decomposing apparent alternating-current power $S$ into real working power $P = S\cos\phi$ and reactive magnetizing power $Q = S\sin\phi$ in Unit II (`SC-14`) or resolving complex impedance reflections in Unit V (`SC-50`).

On the `SC-35`, `{{key:TRV}}` expects the clockwise **Azimuth $\alpha$ in Register $Y$** and the **Horizontal Distance $D_H$ in Register $X$**, pushes the North latitude change $\Delta N = D_H\cos\alpha$ into Register $Y$ and the East departure $\Delta E = D_H\sin\alpha$ into Register $X$, and automatically accumulates the leg into the running traverse registers (`statSumY` for $\Sigma_{\Delta N}$ and `statSumX` for $\Sigma_{\Delta E}$). When our Pine Barrens crew stages the converted azimuth $\alpha = 47.375^\circ$ in Register $Y$ and the reduced horizontal distance $D_H = 410.10\text{ ft}$ in Register $X$ and presses `{{key:TRV}}`, the instrument deposits $\Delta N = 410.10\cos(47.375^\circ) = \mathbf{277.75\text{ ft}}$ into Register $Y$ and $\Delta E = 410.10\sin(47.375^\circ) = \mathbf{301.76\text{ ft}}$ into Register $X$.

---

## Inverse Monument Recovery, Traverse Closure, and Shoelace Acreage

Once the crew carries coordinates across the ravine to the witness oak, they must solve the inverse problem—turning known coordinate pairs back into a compass bearing and tape distance to pinpoint the buried brass cornerstone—check their benchmark rod transfer with three-wire stadia leveling, and close the four-sided perimeter loop to certify its legal area.

### Inverse Coordinate Geometry and Legal Quadrant Bearings

Running the Forward projection in reverse—starting from two known monument coordinates $(N_A, E_A)$ and $(N_B, E_B)$ and recovering the straight-line horizontal distance $D$ and clockwise North azimuth $\alpha \in [0^\circ, 360^\circ)$ between them—is the **Inverse Coordinate Geometry Problem** (`{{key:INV}}`). From the coordinate displacements $\Delta N = N_B - N_A$ in Register $Y$ and $\Delta E = E_B - E_A$ in Register $X$, the Euclidean norm gives $D$ in Register $X$, while the two-argument arctangent resolves the azimuth in Register $Y$:

$$\Delta N = N_B - N_A, \qquad \Delta E = E_B - E_A, \qquad D = \sqrt{(\Delta N)^2 + (\Delta E)^2}, \qquad \alpha = \operatorname{atan2}(\Delta E, \Delta N) \pmod{360^\circ}$$

Whereas geodetic computations use $0^\circ\text{--}360^\circ$ clockwise azimuths, colonial and modern metes-and-bounds property deeds record directions as **Quadrant Bearings** (`{{key:BRG}}`). A quadrant bearing begins on either the **North (`N`)** or **South (`S`)** meridian and turns an acute angle $\theta \in [0^\circ, 90^\circ]$ toward either the **East (`E`)** or **West (`W`)**:

![Four-quadrant surveyor bearing angles (NE, SE, SW, NW) measured acute from the North-South meridian.](../assets/diagrams/domains/diagram_ch01_quadrant_bearings.png)

In Quadrant I (`NE`, $0^\circ \le \alpha \le 90^\circ$), the acute meridian angle is $\theta = \alpha$ (`N θ E`); in Quadrant II (`SE`, $90^\circ < \alpha \le 180^\circ$), $\theta = 180^\circ - \alpha$ (`S θ E`); in Quadrant III (`SW`, $180^\circ < \alpha \le 270^\circ$), $\theta = \alpha - 180^\circ$ (`S θ W`); and in Quadrant IV (`NW`, $270^\circ < \alpha < 360^\circ$), $\theta = 360^\circ - \alpha$ (`N θ W`). Between the recovered Witness Oak at $(N_1 = 1000.00\text{ ft}, E_1 = 1000.00\text{ ft})$ and the historic deed coordinates of the buried Pine Barrens cornerstone at $(N_2 = 640.00\text{ ft}, E_2 = 520.00\text{ ft})$, the coordinate differences $\Delta N = -360.00\text{ ft}$ and $\Delta E = -480.00\text{ ft}$ yield an inverse horizontal distance of $D = \sqrt{(-360.00)^2 + (-480.00)^2} = \mathbf{600.00\text{ ft}}$ ($9.0909\text{ chains}$ via `{{key:▸ch}}`). Because both displacements are negative, the sightline lies in Quadrant III (`SW`) with acute meridian angle $\theta = \arctan(480/360) \approx 53.1301^\circ = 53^\circ 07' 48''$, corresponding to a full-circle azimuth of $\alpha = 180^\circ + 53.1301^\circ = \mathbf{233.1301^\circ}$ and a legal deed bearing of $\mathbf{\text{S } 53^\circ 07' 48'' \text{ W}}$.

### Closed Polygon Traverses, Three-Wire Stadia Leveling, and Shoelace Acreage

With the lost cornerstone uncovered, the survey crew checks the vertical datum from the creek benchmark using three-wire stadia leveling (`{{key:LVL}}`) and walks the closed perimeter loop around the parcel, accumulating each boundary leg into the `@COGO` ledger via `{{key:TRV}}` and `{{key:PT+}}` and closing back onto the Point of Beginning (`POB`).

![Closed three-leg polygon traverse illustrating vector summation and the linear misclosure gap at the Point of Beginning.](../assets/diagrams/domains/diagram_ch01_polygon_traverse.png)

In an exact closed polygon of $n$ sides, the vector sum of all North latitudes $\Sigma_{\Delta N} = \sum_{i=1}^n \Delta N_i$ and the vector sum of all East departures $\Sigma_{\Delta E} = \sum_{i=1}^n \Delta E_i$ both equal zero. Because field measurements contain small random optical and atmospheric errors, the accumulated traverse returns to a coordinate slightly displaced from the `POB`. The hypotenuse of that residual gap is the **Linear Error of Closure** $E_c$ (`{{key:CLS}}`), and dividing total perimeter $P = \sum_{i=1}^n D_i$ by $E_c$ defines the **Relative Precision Ratio**; once closure meets statutory accuracy standards, Nathaniel Bowditch's 1807 **Compass Rule** distributes the misclosure across each leg $i$ in proportion to its length fraction $D_i / P$:

$$E_c = \sqrt{\left(\Sigma_{\Delta N}\right)^2 + \left(\Sigma_{\Delta E}\right)^2}, \qquad \text{Precision Ratio} = 1 : \frac{P}{E_c}, \qquad \delta N_i = -\Sigma_{\Delta N}\!\left(\frac{D_i}{P}\right), \qquad \delta E_i = -\Sigma_{\Delta E}\!\left(\frac{D_i}{P}\right)$$

Here $E_c$ is the linear misclosure magnitude in feet, $P$ is the total polygon perimeter, and $(\delta N_i, \delta E_i)$ are the additive latitude and departure corrections applied to leg $i$. From the sequential vertex coordinates $(N_1, E_1), (N_2, E_2), \dots, (N_n, E_n)$ of a closed simple polygon (with $(N_{n+1}, E_{n+1}) = (N_1, E_1)$), **Gauss's Shoelace Formula** evaluates the enclosed planar area $A$ (displayed live as `AREA` alongside `CLOS` inside the `@COGO` reference table `{{key:▦}}`, while `{{key:△}}` evaluates right-triangle and sub-parcel areas), which converts to statutory acreage via `{{key:▸ac}}` ($43{,}560\text{ ft}^2/\text{acre}$) and metric hectares via `{{key:▸ha}}` ($10{,}000\text{ m}^2/\text{ha}$):

$$A = \frac{1}{2} \left\lvert \sum_{i=1}^{n} \left( E_i N_{i+1} - E_{i+1} N_i \right) \right\rvert, \qquad \text{Acres} = \frac{A_{\text{ft}^2}}{43{,}560}$$

For a four-leg rectangular boundary loop of total perimeter $P = 3{,}200.00\text{ ft}$ (spanning $600.00\text{ ft}$ North-South by $1{,}000.00\text{ ft}$ East-West) whose field measurements return with net latitude misclosure $\Sigma_{\Delta N} = -0.12\text{ ft}$ and net departure misclosure $\Sigma_{\Delta E} = +0.16\text{ ft}$, the linear error of closure is $E_c = \sqrt{(-0.12)^2 + 0.16^2} = \mathbf{0.20\text{ ft}}$ (`{{key:CLS}}`), yielding a relative precision ratio of $1 : (3200 / 0.20) = \mathbf{1 : 16{,}000}$, and Gauss's shoelace sum across the adjusted corners in `{{key:▦}}` gives an enclosed area of $A = \mathbf{600{,}000\text{ ft}^2}$, or $600{,}000 / 43{,}560 \approx \mathbf{13.7741\text{ acres}}$ ($5.5742\text{ ha}$).

---

## Retracing the Pine Barrens Boundary on the Stack and Solver Workspace

On the **SC-35**, two-component survey operators (`{{key:SLP}}`, `{{key:TRV}}`, `{{key:INV}}`) and three-wire stadia leveling (`{{key:LVL}}`) execute immediately on the RPN stack while `{{key:N⇄E}}` and `{{key:x⇄y}}` swap $(N, E) \leftrightarrow (E, N)$ axes whenever needed. At the same time, the `@COGO` reference table (`{{key:▦}}`) provides live polygon `AREA` and `CLOS` readouts, and pressing `{{key:LVL}}` or `{{key:△}}` when $X = 0, Y = 0$ (or after `{{key:SOLVE}}`) opens the bidirectional Equation Solver workspaces (`LVL: E = H + B - F` with variable softkeys `{{keycap:E}}`, `{{keycap:H}}`, `{{keycap:B}}`, `{{keycap:F}}`, and `TRI: A = B × H / 2` with variable softkeys `{{keycap:A}}`, `{{keycap:B}}`, `{{keycap:H}}`):

| Button | Operation | Register Z | Register Y | Register X | Governing Expression |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`{{key:▸DEG}}`** / **`{{key:▸HMS}}`** / **`{{key:▸HR}}`** | Packed Sexagesimal Conversion | — | — | `DDD.MMSS` or $\theta_{\text{dec}}$ | $\theta_{\text{dec}} = D + M/60 + S/3600$ |
| **`{{key:f-i}}`** | Architectural Foot-Inch Parser | — | Feet $F$ | Inches $I$ (or packed) | $L_{\text{ft}} = F + (I + N/D)/12$ |
| **`{{key:SLP}}`** | Slope Distance Reduction | — | Slope $S$ | Inclination $\nu^\circ$ | $Y' = \Delta V = S\sin\nu,\; X' = D_H = S\cos\nu$ |
| **`{{key:TRV}}`** | Forward North-Clockwise COGO | — | Azimuth $\alpha^\circ$ | Distance $D_H$ | $Y' = \Delta N = D_H\cos\alpha,\; X' = \Delta E = D_H\sin\alpha$ (accumulates leg) |
| **`{{key:INV}}`** | Inverse Coordinate Geometry | — | Latitude $\Delta N$ | Departure $\Delta E$ | $Y' = \alpha,\; X' = D = \sqrt{(\Delta N)^2 + (\Delta E)^2}$ |
| **`{{key:BRG}}`** | Acute Quadrant Bearing | — | — | Azimuth $\alpha^\circ$ | Maps $[0^\circ, 360^\circ) \to \theta \in [0^\circ, 90^\circ]$ |
| **`{{key:LVL}}`** | 3-Wire Stadia & Leveling Solver | Top wire $T$ | Mid wire $M$ | Bot wire $B_w$ | $Y' = (T+B_w)/2,\; X' = 100(T-B_w)$; `LVL` workspace (`{{keycap:E}}`, `{{keycap:H}}`, `{{keycap:B}}`, `{{keycap:F}}`) |
| **`{{key:PT+}}`** | Polygon Traverse Accumulator | — | Latitude $\Delta N$ | Departure $\Delta E$ | Appends vertex to `@COGO` (`{{key:▦}}`) & shoelace sum |
| **`{{key:CLS}}`** | Linear Error of Closure | — | $\Sigma_{\Delta N}$ | $\Sigma_{\Delta E}$ | $E_c = \sqrt{(\Sigma_{\Delta N})^2 + (\Sigma_{\Delta E})^2}$ |
| **`{{key:▦}}`** / **`{{key:△}}`** / **`{{key:▸ac}}`** / **`{{key:▸ha}}`** | Polygon `@COGO` Area & Land Units | — | Base $B$ | Height $H$ / $A_{\text{ft}^2}$ | `{{key:▦}}` displays shoelace `AREA` & `CLOS`; `{{key:△}}` opens `TRI` (`{{keycap:A}}`, `{{keycap:B}}`, `{{keycap:H}}`) |

### Reducing the Ravine Slope Shot, Projecting Coordinates, and Checking Three-Wire Stadia

Standing at Witness Station $A$, the party chief begins with the raw ravine sightline from the field book: an azimuth of $47^\circ 22' 30''$ (`47.2230 {{key:▸DEG}}` $= 47.375^\circ$) and an inclined slope distance of $S = 412.68\text{ ft}$ at a slope angle of $6^\circ 15' 00''$ (`6.15 {{key:▸DEG}}` $= 6.25^\circ$). Keying `412.68 {{key:ENTER}} 6.25 {{key:SLP}}` places the vertical rise $\Delta V = \mathbf{44.92\text{ ft}}$ into Register $Y$ and the reduced horizontal distance $D_H = \mathbf{410.10\text{ ft}}$ into Register $X$. Next, placing the azimuth $\alpha = 47.375^\circ$ in Register $Y$ and $D_H = 410.10\text{ ft}$ in Register $X$ and pressing `{{key:TRV}}` pushes the northward latitude change $\Delta N = \mathbf{277.75\text{ ft}}$ into Register $Y$ and the eastward departure $\Delta E = \mathbf{301.76\text{ ft}}$ into Register $X$ while accumulating the leg in `statSumX`/`statSumY`. Finally, reading three-wire stadia crosshair intercepts on the creekside benchmark rod—top wire $7.82\text{ ft}$ in Register $Z$, middle wire $5.42\text{ ft}$ in Register $Y$, and bottom wire $3.02\text{ ft}$ in Register $X$—and pressing `{{key:LVL}}` verifies crosshair balance by placing the expected mid-wire reading $\mathbf{5.42\text{ ft}}$ into Register $Y$ and the horizontal stadia sight distance $100 \times (7.82 - 3.02) = \mathbf{480.00\text{ ft}}$ into Register $X$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `412.68 {{key:ENTER}} 6.25 {{key:SLP}}` | $0$ | $0$ | $44.92$ | $410.10$ | Reduce slope shot to vertical $\Delta V = 44.92\text{ ft}$ ($Y$) and horizontal $D_H = 410.10\text{ ft}$ ($X$) |
| `47.2230 {{key:▸DEG}} {{key:x⇄y}} {{key:TRV}}` | $0$ | $44.92$ | $277.75$ | $301.76$ | Convert $47^\circ 22' 30'' \to 47.375^\circ$ into $Y$, keep $D_H = 410.10$ in $X$, and project $\Delta N = 277.75$, $\Delta E = 301.76$ |
| `7.82 {{key:ENTER}} 5.42 {{key:ENTER}} 3.02 {{key:LVL}}` | $44.92$ | $277.75$ | $5.42$ | **$480.00$** | 3-wire stadia check: expected mid-wire $5.42\text{ ft}$ in $Y$ and stadia distance $480.00\text{ ft}$ in $X$ |

To recover the buried 1794 brass cornerstone at $(N_2 = 640.00\text{ ft}, E_2 = 520.00\text{ ft})$ from the Witness Oak at $(N_1 = 1000.00\text{ ft}, E_1 = 1000.00\text{ ft})$, the crew keys `640 {{key:ENTER}} 1000 {{key:-}} 520 {{key:ENTER}} 1000 {{key:-}} {{key:INV}}`, placing the horizontal stakeout distance $D = \mathbf{600.00\text{ ft}}$ in Register $X$ and the angle in Register $Y$; swapping the azimuth to Register $X$ via `{{key:x⇄y}}` and pressing `{{key:BRG}} {{key:▸HMS}}` converts the direction into the acute Southwest deed bearing `53.0748` ($\mathbf{\text{S } 53^\circ 07' 48'' \text{ W}}$).

### Auditing Traverse Closure in `@COGO` (`{{key:▦}}`) and Solving Sub-Parcel Geometry (`{{key:△}}`, `{{key:LVL}}`)

To close a multi-leg boundary loop and evaluate its enclosed acreage, each `{{key:TRV}}` or `{{key:PT+}}` entry accumulates coordinates into the live `@COGO` ledger. For a three-leg right-triangular sub-parcel starting at $(0, 0)$ with Leg 1 running $300.00\text{ ft}$ at Azimuth $0^\circ$ (Due North), Leg 2 running $400.00\text{ ft}$ at Azimuth $90^\circ$ (Due East), and Leg 3 running $500.00\text{ ft}$ at Azimuth $233.1301^\circ$ back to the origin, staging Azimuth in $Y$ and Distance in $X$ for each `{{key:TRV}}` call populates the live `@COGO` ledger in `{{key:▦}}` (`CLOS = 0`, `AREA = 60000`) and converts the area to acres via `{{key:▸ac}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLEAR}} {{keycap:CLΣ}}` | $0$ | $0$ | $0$ | $0$ | Clear `@COGO` traverse statistical and shoelace vertex registers |
| `0 {{key:ENTER}} 300 {{key:TRV}} {{key:PT+}}` | $0$ | $0$ | $300$ | $1$ | Project Leg 1 ($\alpha_1 = 0^\circ, D_1 = 300 \to \Delta N_1 = 300, \Delta E_1 = 0$) and store Vertex 1 |
| `90 {{key:ENTER}} 400 {{key:TRV}} {{key:PT+}}` | $0$ | $300$ | $0$ | $2$ | Project Leg 2 ($\alpha_2 = 90^\circ, D_2 = 400 \to \Delta N_2 = 0, \Delta E_2 = 400$) and store Vertex 2 |
| `233.1301 {{key:ENTER}} 500 {{key:TRV}} {{key:PT+}}` | $300$ | $0$ | $-300$ | $3$ | Project Leg 3 ($\Delta N_3 = -300, \Delta E_3 = -400$); `{{key:▦}}` reports `CLOS = 0`, `AREA = 60000` |
| `60000 {{key:▸ac}}` | $0$ | $-300$ | $3$ | **$1.3774$** | Convert enclosed shoelace area $60{,}000\text{ ft}^2$ from `{{key:▦}}` to $1.3774\text{ acres}$ |

When the full four-leg Pine Barrens traverse of total perimeter $P = 3{,}200.00\text{ ft}$ returns to the Point of Beginning with net latitude misclosure $\Sigma_{\Delta N} = -0.12\text{ ft}$ and net departure misclosure $\Sigma_{\Delta E} = +0.16\text{ ft}$, pressing `{{key:CLS}}` (or `0.12 {{key:+/-}} {{key:ENTER}} 0.16 {{key:CLS}}`) resolves the linear error of closure $E_c = \mathbf{0.20\text{ ft}}$ in Register $X$, and keying `3200 {{key:x⇄y}} {{key:÷}}` yields the relative precision denominator $\mathbf{16{,}000}$ ($1 : 16{,}000$). Furthermore:
- **Triangle Sub-Parcel Solver (`{{key:△}}`):** If the county register requires carving off a triangular creekside easement of exact area $A = 43{,}560\text{ ft}^2$ ($1.0000\text{ acre}$) along a $B = 300.00\text{ ft}$ baseline, pressing `{{key:SOLVE}} {{key:△}}` opens the **`TRI` Equation Solver Workspace** displaying `A = B × H / 2` with variable softkeys `{{keycap:A}}` (`{{key:LFU0}}`), `{{keycap:B}}` (`{{key:LFU1}}`), and `{{keycap:H}}` (`{{key:LFU2}}`). Storing `43560 {{keycap:A}}` and `300 {{keycap:B}}` and pressing `{{key:SOLVE}} {{keycap:H}}` solves the equation backward to return the required perpendicular easement offset $H = \frac{2 \times 43{,}560}{300} = \mathbf{290.40\text{ ft}}$.
- **Differential Leveling Solver (`{{key:LVL}}`):** Pressing `{{key:SOLVE}} {{key:LVL}}` opens the **`LVL` Equation Solver Workspace** displaying `E = H + B - F` with variable softkeys `{{keycap:E}}` (`{{key:LFU0}}`), `{{keycap:H}}` (`{{key:LFU1}}`), `{{keycap:B}}` (`{{key:LFU2}}`), and `{{keycap:F}}` (`{{key:LFU3}}`), allowing the crew to solve forward for new station elevation $E$ or backward for a target foresight rod reading $F$.

### Try It on the Stack

Use these three boundary retracement exercises to practice slope reduction, coordinate projection, and traverse closure on the stack:

1. **Slope Reduction and Forward Coordinate Projection:** Reduce slope distance $S = 412.68\text{ ft}$ at inclination $\nu = +6^\circ 15' 00''$ (`6.15 {{key:▸DEG}}` $= 6.25^\circ$) via `412.68 {{key:ENTER}} 6.25 {{key:SLP}}` to obtain $D_H = 410.10\text{ ft}$ in Register $X$ and $\Delta V = 44.92\text{ ft}$ in Register $Y$, then place Azimuth $\alpha = 47^\circ 22' 30''$ (`47.2230 {{key:▸DEG}}` $= 47.375^\circ$) in Register $Y$ and $D_H = 410.10\text{ ft}$ in Register $X$ and press `{{key:TRV}}`. *(Verified stack results: $\Delta V = \mathbf{44.92\text{ ft}}$, $D_H = \mathbf{410.10\text{ ft}}$, $\Delta N = \mathbf{277.75\text{ ft}}$ in $Y$, and $\Delta E = \mathbf{301.76\text{ ft}}$ in $X$.)*
2. **Inverse Bearing Between Witness Monuments:** Given two iron boundary pipes at $A(1200.00, 1500.00)$ and $B(1585.20, 1912.60)$, key `1585.20 {{key:ENTER}} 1200 {{key:-}} 1912.60 {{key:ENTER}} 1500 {{key:-}} {{key:INV}}` and `{{key:x⇄y}} {{key:BRG}} {{key:▸HMS}}` to find the boundary length and legal quadrant bearing. *(Verified Register $X$ results: $D \approx \mathbf{564.4624\text{ ft}}$, $\alpha \approx \mathbf{46.9669^\circ}$, packed DMS bearing $\mathbf{46.5801}$ or $\text{N } 46^\circ 58' 01'' \text{ E}$.)*
3. **Traverse Closure Precision and Acreage Conversion:** A four-leg boundary loop of perimeter $P = 2{,}500.00\text{ ft}$ has net misclosures $\Sigma_{\Delta N} = +0.15\text{ ft}$ and $\Sigma_{\Delta E} = -0.20\text{ ft}$ and an enclosed shoelace area in `{{key:▦}}` of $A = 326{,}700\text{ ft}^2$. Key `0.15 {{key:ENTER}} 0.20 {{key:+/-}} {{key:CLS}}` for $E_c$, `2500 {{key:x⇄y}} {{key:÷}}` for the precision ratio, and `326700 {{key:▸ac}}` for acreage. *(Verified Register $X$ results: $E_c = \mathbf{0.25\text{ ft}}$, precision $\mathbf{1 : 10{,}000}$, and $\mathbf{7.5000\text{ acres}}$.)*

Having recovered the Pine Barrens cornerstone and closed the planar boundary traverse, we move from flat timberland into steep mountain terrain in Chapter 2 to fit horizontal and vertical highway curves around a granite bluff, compute earthwork prism volumes, and carry vertical benchmark elevations up a canyon wall.

---

# Chapter 2: Threading the Switchback Grade Through Granite Gorge

High in the Sierra Nevada, a state highway alignment climbing a narrow river canyon encounters an overhanging granite bluff that juts across the projected roadbed. The two straight approach centerlines (tangents) of the mountain highway intersect inside the solid rock face at the Point of Intersection (`PI`) with an exterior deflection angle of $\Delta = 28^\circ 30' 00''$ ($28.5^\circ$). To swing the two-lane roadbed smoothly around the bluff without blasting away half the cliff or exceeding safe centrifugal lateral acceleration for logging trucks, the resident highway engineer specifies a tangent circular curve of centerline radius $R = 1{,}200.00\text{ ft}$.

Before the earthmoving crew can stake the curve or set grade rails for the paving machines, three coupled geometrical problems must be solved in the field. First, the layout crew must determine how far back from the inaccessible `PI` to set the Point of Curvature (`PC`) and Point of Tangency (`PT`) via the tangent distance $T$, how long the curved centerline arc $L$ and straight-line long chord $LC$ will be (`{{key:CRV}}`), how closely the mid-arc apex approaches the granite face via the external secant distance $E$ and middle ordinate $M$, and how to adjust $\Delta$ or $R$ in the `HCRV` solver (`{{keycap:L}}`, `{{keycap:R}}`, `{{keycap:D}}`) if a rockfall barrier restricts the allowable curve length $L$. Second, where the $+2.50\%$ approach grade crests into a $-1.75\%$ downgrade over an $L = 8\text{-station}$ ($800\text{ ft}$) vertical curve beginning at $\text{PVC} = 425.00\text{ ft}$, the crew must compute the parabolic curve elevations (`{{key:VCV}}`) and the trapezoidal prism earthwork volume (`{{key:CUT}}`) in cubic yards. Third, because GPS vertical elevations suffer from multipath reflections beneath the canyon walls, the leveling crew must carry a millimeter-grade vertical datum up from a bronze U.S. Geological Survey benchmark on the canyon floor using differential spirit leveling and three-wire stadia rod checks (`{{key:LVL}}`) and verify the longitudinal road grade (`{{key:GR%}}`) and culvert drainage flow (`{{key:FLW}}`).

---

## Tangential Circular Curves, Vertical Crest Paraboloids, and Earthwork Volumes

When two straight highway or railway centerlines intersect horizontally at a **Point of Intersection (`PI`)** with an exterior deflection angle $\Delta$, engineers fit a tangent circular arc of radius $R$ between the **Point of Curvature (`PC`)** and the **Point of Tangency (`PT`)**; when two longitudinal grades $g_1\%$ and $g_2\%$ meet vertically at a crest or sag, engineers fit a constant-curvature parabola (`{{key:VCV}}`) and tally excavation yardage between cross-sectional end areas (`{{key:CUT}}`).

### Centerline Arc Length, Tangent Distance, and Long Chord Projections

Because the radial lines drawn from the center of curvature $O$ to the tangent points `PC` and `PT` meet the entry and exit tangents at exact right angles ($90^\circ$), the quadrilateral formed by $O$, `PC`, `PI`, and `PT` has interior angles $90^\circ$ at `PC` and `PT` and $180^\circ - \Delta$ at `PI`. Consequently, the central angle subtended at $O$ equals the exterior deflection angle $\Delta$.

![Circular horizontal alignment curve geometry linking the Point of Curvature (PC), Point of Intersection (PI), and Point of Tangency (PT).](../assets/diagrams/domains/diagram_ch01_horiz_curve.png)

Bisecting the central angle $\Delta$ with the radial line from $O$ through the mid-arc apex to `PI` partitions the layout into two congruent right triangles of half-angle $\Delta / 2$, determining the primary horizontal curve elements (`{{key:CRV}}`)—the **Tangent Distance** $T$ from `PC` (or `PT`) to `PI`, the curved centerline **Arc Length** $L$ from `PC` to `PT`, and the straight-line **Long Chord** $LC$ connecting `PC` directly to `PT`:

$$T = R \tan\!\left(\frac{\Delta}{2}\right), \qquad L = R \cdot \Delta \cdot \frac{\pi}{180^\circ}, \qquad LC = 2 R \sin\!\left(\frac{\Delta}{2}\right)$$

In these expressions, $R$ is the centerline radius of curvature in feet, $\Delta$ is the exterior deflection angle in decimal degrees, $T$ is the opposite leg of the right triangle of angle $\Delta / 2$ and adjacent side $R$, $L$ scales the radian measure $\Delta(\pi / 180^\circ)$ by $R$, and $LC$ doubles the half-chord $R\sin(\Delta / 2)$. For the Granite Gorge highway curve of radius $R = 1{,}200.00\text{ ft}$ in Register $Y$ and deflection angle $\Delta = 28.5^\circ$ in Register $X$ (half-angle $\Delta / 2 = 14.25^\circ$), pressing `{{key:CRV}}` yields the tangent setback distance $T = 1200\tan(14.25^\circ) = \mathbf{304.77\text{ ft}}$ in Register $Y$ and the centerline paving arc length $L = 1200 \times 28.5^\circ \times (\pi / 180^\circ) = \mathbf{596.90\text{ ft}}$ in Register $X$, while the straight-line long chord is $LC = 2400\sin(14.25^\circ) = \mathbf{590.80\text{ ft}}$.

### External Clearance, Parabolic Vertical Curves (`{{key:VCV}}`), and Prism Earthwork (`{{key:CUT}}`)

To determine how far the curved roadbed swings inward from the granite point at `PI` and outward from the straight baseline chord connecting `PC` and `PT`, the engineer inspects the radial line from $O$ to `PI`. Subtracting $R$ from the secant hypotenuse $R / \cos(\Delta / 2)$ isolates the **External Distance** $E$, and subtracting $R\cos(\Delta / 2)$ from $R$ isolates the **Middle Ordinate** $M$:

$$E = R \left(\frac{1}{\cos(\Delta / 2)} - 1\right), \qquad M = R \left(1 - \cos\!\left(\frac{\Delta}{2}\right)\right)$$

At the canyon crest, transitioning from an entry grade $g_1$ (in $\text{ft/station}$, i.e., percent grade) at the Point of Vertical Curvature ($\text{PVC}$) to an exit grade $g_2$ over a vertical curve of length $L$ stations (`{{key:VCV}}`) traces the vertical parabola $\text{Elev}(x)$ at distance $x$ stations from $\text{PVC}$, while excavating a rock cut of length $L_{\text{cut}}$ (in feet) between cross-sectional end areas $A_1$ and $A_2$ (in $\text{ft}^2$) yields the average-end-area trapezoidal prism volume $V_{\text{cut}}$ (`{{key:CUT}}`) in bank cubic yards ($1\text{ yd}^3 = 27\text{ ft}^3$):

$$\text{Elev}(x) = \text{PVC} + g_1 x + \left(\frac{g_2 - g_1}{2 L}\right) x^2, \qquad V_{\text{cut}} = \frac{A_1 + A_2}{2} \cdot \frac{L_{\text{cut}}}{27}$$

For a vertical crest curve starting at elevation $\text{PVC} = 425.00\text{ ft}$ with entry grade $g_1 = +2.50\%$, exit grade $g_2 = -1.75\%$, and curve length $L = 8\text{ stations}$ ($800\text{ ft}$), the midpoint elevation at $x = L / 2 = 4\text{ stations}$ is $\text{Elev}(4) = 425.00 + 2.5(4) + \frac{-1.75 - 2.5}{2(8)}(4)^2 = 425.00 + 10.00 - 4.25 = \mathbf{430.75\text{ ft}}$ (and at the end of the curve $x = 8\text{ stations}$, $\text{PVT} = 425.00 + 2.5(8) - 17.00 = \mathbf{428.00\text{ ft}}$). Across a $L_{\text{cut}} = 150.0\text{ ft}$ granite bench cut between end areas $A_1 = 320.0\text{ ft}^2$ and $A_2 = 400.0\text{ ft}^2$, `{{key:CUT}}` evaluates $V_{\text{cut}} = \frac{320 + 400}{2} \times \frac{150}{27} = \mathbf{2{,}000.00\text{ yd}^3}$.

---

## Differential Spirit Leveling, Three-Wire Stadia, and Longitudinal Grade

With the horizontal and vertical curves designed around the bluff, the grading crew transfers benchmark elevations up the canyon wall and verifies the vertical climb rate of the pavement.

### Backsight, Height of Instrument, and Foresight Benchmark Transfers

To carry a vertical elevation from a Benchmark (`BM`) of known elevation $H = E_{\text{BM}}$ to an uphill Turning Point (`TP`) or construction stake, a surveyor sets up a compensated optical level midway between the two stations (`{{key:LVL}}`). Sighting backward along the horizontal optical plane to a graduated leveling rod held plumb on the benchmark yields the **Backsight** reading $B$, which adds to $H$ to establish the optical **Height of Instrument** ($\text{HI} = H + B$); turning the telescope forward to a rod held on the new station yields the **Foresight** reading $F$, which subtracts from $\text{HI}$ to determine the new station **Elevation** $E$:

![Differential spirit leveling sightline connecting Backsight (BS), Height of Instrument (HI), and Foresight (FS) between benchmarks.](../assets/diagrams/domains/diagram_ch01_spirit_leveling.png)

$$\text{HI} = H + B, \qquad E = \text{HI} - F = H + B - F$$

In this differential leveling chain, $H$ is the starting benchmark elevation above mean sea level, $\text{HI}$ is the elevation of the telescope's horizontal line of sight, and $B - F$ is the net vertical rise ($+$) or fall ($-$) between the two rod positions. Setting up above canyon-floor benchmark `BM-1` ($H = 4{,}812.40\text{ ft}$) and reading a backsight of $B = 6.85\text{ ft}$ establishes the optical plane at $\text{HI} = 4812.40 + 6.85 = \mathbf{4{,}819.25\text{ ft}}$; sighting forward to the curve entry stake at `PC` (Station `124+50.00` via `{{key:STA}}`) with a center-wire foresight of $F = 5.42\text{ ft}$ determines the `PC` pavement elevation as $E = 4819.25 - 5.42 = \mathbf{4{,}813.83\text{ ft}}$.

### Three-Wire Stadia Interval Verification and Longitudinal Grade Percentage

To guard against rod reading blunders and balance backsight and foresight distances, precision optical levels engrave two short **stadia crosshairs**—a **Top wire** $T$ and a **Bottom wire** $B_w$—spaced symmetrically above and below the **Middle leveling wire** $M$ at an optical stadia interval factor of $K = 100$. Pushing all three crosshair readings onto the stack ($T$ in $Z$, $M$ in $Y$, $B_w$ in $X$) and pressing `{{key:LVL}}` verifies that the expected mean $(T + B_w)/2$ in Register $Y$ matches $M$ within $0.005\text{ ft}$ and places the horizontal stadia sight distance $D = 100(T - B_w)$ in Register $X$, while comparing the elevation change $\Delta E_{\text{vert}}$ across a horizontal alignment run $L$ defines the longitudinal **Grade Percentage** (`{{key:GR%}}`):

$$\left\lvert M - \frac{T + B_w}{2} \right\rvert \le 0.005\text{ ft}, \qquad D = 100 \times (T - B_w), \qquad \text{GR\%} = \left(\frac{\Delta E_{\text{vert}}}{L}\right) \times 100\%$$

On the canyon benchmark shot with Top wire $T = 7.82\text{ ft}$ in Register $Z$, Middle wire $M = 5.42\text{ ft}$ in Register $Y$, and Bottom wire $B_w = 3.02\text{ ft}$ in Register $X$, pressing `{{key:LVL}}` places the expected mid-wire mean $(7.82 + 3.02)/2 = \mathbf{5.42\text{ ft}}$ in Register $Y$ and the stadia distance $100(7.82 - 3.02) = \mathbf{480.00\text{ ft}}$ in Register $X$. Carrying the level loop up to `PT` across a $+35.814\text{ ft}$ rise over the $L = 596.90\text{ ft}$ curve arc and pressing `{{key:GR%}}` confirms a longitudinal climb of $\text{GR\%} = (35.814 / 596.90) \times 100\% = \mathbf{+6.00\%}$.

---

## Staking the Granite Gorge Alignment on the Stack and Solver Workspace

On the **SC-35**, route geometry, earthwork, and leveling operators work in both immediate RPN stack mode and interactive Equation Solver Workspace mode (`HCRV` on `{{key:CRV}}`, `LVL` on `{{key:LVL}}`, and `FLW` on `{{key:FLW}}`):

| Button | Operation | Register Z | Register Y | Register X | Governing Expression |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`{{key:CRV}}`** | Circular Curve Tangent, Arc & Solver | — | Radius $R$ | Deflection $\Delta^\circ$ | $Y' = T = R\tan(\Delta/2),\; X' = L = R\Delta\pi/180^\circ$; `HCRV` (`{{keycap:L}}`, `{{keycap:R}}`, `{{keycap:D}}`) |
| **`{{key:VCV}}`** | Parabolic Vertical Curve Elevation | $g_1\%$ ($\text{PVC}$ in $T$) | $g_2\%$ | Length $L$ (stns) | $\text{Elev}(x) = \text{PVC} + g_1 x + \frac{g_2 - g_1}{2L}x^2$ |
| **`{{key:CUT}}`** | Trapezoidal Prism Earthwork Volume | Area $A_1\ (\text{ft}^2)$ | Area $A_2\ (\text{ft}^2)$ | Length $L\ (\text{ft})$ | $V = \frac{A_1 + A_2}{2} \cdot \frac{L}{27}\ (\text{yd}^3)$ |
| **`{{key:LVL}}`** | 3-Wire Stadia & Leveling Solver | Top wire $T$ | Mid wire $M$ | Bot wire $B_w$ | $Y' = (T+B_w)/2,\; X' = 100(T-B_w)$; `LVL` (`{{keycap:E}}`, `{{keycap:H}}`, `{{keycap:B}}`, `{{keycap:F}}`) |
| **`{{key:GR%}}`** | Longitudinal Percentage Grade | — | Rise $\Delta E_{\text{vert}}$ | Run $L$ | $\text{GR\%} = (\Delta E_{\text{vert}} / L) \times 100\%$ |
| **`{{key:FLW}}`** | Culvert & Channel Continuity Solver | — | Area $A\ (\text{ft}^2)$ | Velocity $V\ (\text{ft/s})$ | $Q = A \times V\ (\text{ft}^3/\text{s})$; `FLW` (`{{keycap:Q}}`, `{{keycap:A}}`, `{{keycap:V}}`) |
| **`{{key:STA}}`** | Highway Stationing Formatter | — | — | Distance $L_{\text{ft}}$ | Formats $12{,}450.00\text{ ft}$ as `124+50.00` ($124.50\text{ stns}$) |

### Immediate Stack Execution and Inverse Curve Solving in `HCRV` (`{{key:CRV}}`) and `{{key:VCV}}`

To lay out the $R = 1{,}200.00\text{ ft}$ horizontal curve with deflection angle $\Delta = 28.5^\circ$, evaluate the parabolic vertical crest curve ($\text{PVC} = 425.00\text{ ft}$, $g_1 = +2.5\%$, $g_2 = -1.75\%$, $L = 8\text{ stations}$), and compute the $150\text{ ft}$ rock cut volume between end areas $A_1 = 320\text{ ft}^2$ and $A_2 = 400\text{ ft}^2$, the engineer executes:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1200 {{key:ENTER}} 28.5 {{key:CRV}}` | $0$ | $0$ | $304.77$ | $596.90$ | Compute tangent $T = 1200\tan(14.25^\circ) = 304.77\text{ ft}$ ($Y$) and arc $L = 596.90\text{ ft}$ ($X$) |
| `425.00 {{key:ENTER}} 2.5 {{key:ENTER}} 1.75 {{key:+/-}} {{key:ENTER}} 8 {{key:VCV}}` | $0$ | $304.77$ | $596.90$ | $430.75$ | Compute parabolic crest elevation $\text{Elev}(4) = 430.75\text{ ft}$ ($\text{PVT} = 428.00\text{ ft}$ at $x = 8$) |
| `320 {{key:ENTER}} 400 {{key:ENTER}} 150 {{key:CUT}}` | $304.77$ | $596.90$ | $430.75$ | **$2000.00$** | Compute trapezoidal prism volume $V = \frac{320+400}{2}\cdot\frac{150}{27} = 2{,}000.00\text{ yd}^3$ |

Now suppose a canyon rockfall catchment wall restricts the maximum allowable curved roadbed arc length to $L = 450.00\text{ ft}$. Pressing `{{key:SOLVE}} {{key:CRV}}` opens the **Bidirectional `HCRV` Equation Solver Workspace**, displaying `HCRV: HORIZ CURV` and `L = R × Δ × π / 180` on Line 1 with variable softkeys `{{keycap:L}}` (`{{key:LFU0}}`), `{{keycap:R}}` (`{{key:LFU1}}`), and `{{keycap:D}}` (`{{key:LFU2}}`):
- **Inverse Solve for Deflection Angle $\Delta$ (`{{keycap:D}}`):** Keying `450 {{keycap:L}}` (`{{key:LFU0}}`) and `1200 {{keycap:R}}` (`{{key:LFU1}}`) and pressing `{{key:SOLVE}} {{keycap:D}}` (`{{key:LFU2}}`) solves backward for the maximum deflection angle $\Delta = \frac{450 \times 180^\circ}{1200 \pi} \approx \mathbf{21.4859^\circ}$ (`21.2909` via `{{key:▸HMS}}`, or $21^\circ 29' 09''$).
- **Inverse Solve for Curve Radius $R$ (`{{keycap:R}}`):** If the $28.5^\circ$ deflection angle is fixed by the canyon walls (`28.5 {{keycap:D}}`) while $L = 450.00\text{ ft}$ (`450 {{keycap:L}}`), pressing `{{key:SOLVE}} {{keycap:R}}` (`{{key:LFU1}}`) solves backward for the tightened curve radius $R = \frac{450 \times 180^\circ}{28.5^\circ \times \pi} \approx \mathbf{904.6746\text{ ft}}$.

### Running the Three-Wire Canyon Leveling Loop and `LVL` Solver (`{{key:LVL}}`)

At the base of Granite Gorge, the rodman holds the stadia rod on `PC` while the instrument operator reads Top wire $T = 7.82\text{ ft}$, Middle wire $M = 5.42\text{ ft}$, and Bottom wire $B_w = 3.02\text{ ft}$. Loading those three readings in descending order (`7.82 {{key:ENTER}} 5.42 {{key:ENTER}} 3.02 {{key:LVL}}`) verifies rod symmetry, places the expected mid-wire foresight $F = \mathbf{5.42\text{ ft}}$ in Register $Y$ and the stadia distance $D = \mathbf{480.00\text{ ft}}$ in Register $X$, and chains into the benchmark transfer from $H = 4{,}812.40\text{ ft}$ ($B = 6.85\text{ ft}$) and the $+35.814\text{ ft}$ climb over $596.90\text{ ft}$ to `PT`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `7.82 {{key:ENTER}} 5.42 {{key:ENTER}} 3.02 {{key:LVL}}` | $0$ | $0$ | $5.42$ | $480.00$ | Verify 3-wire symmetry; expected mid-wire $F = 5.42\text{ ft}$ in $Y$, distance $D = 480.00\text{ ft}$ in $X$ |
| `{{key:x⇄y}} 4812.40 {{key:ENTER}} 6.85 {{key:+}}` | $0$ | $480.00$ | $5.42$ | $4819.25$ | Compute Height of Instrument $\text{HI} = 4812.40 + 6.85 = 4{,}819.25\text{ ft}$ |
| `{{key:x⇄y}} {{key:-}}` | $0$ | $0$ | $480.00$ | $4813.83$ | Subtract foresight $F = 5.42\text{ ft}$ to find $E_{\text{PC}} = 4{,}813.83\text{ ft}$ |
| `35.814 {{key:ENTER}} 596.90 {{key:GR%}}` | $0$ | $480.00$ | $4813.83$ | **$6.0000$** | Evaluate longitudinal road grade $\text{GR\%} = (35.814 / 596.90) \times 100\% = +6.00\%$ |

In the `LVL` Equation Solver Workspace (`{{key:SOLVE}} {{key:LVL}}`, `E = H + B - F` with variable softkeys `{{keycap:E}}`, `{{keycap:H}}`, `{{keycap:B}}`, `{{keycap:F}}`), the crew can also solve backward for the target foresight rod reading $F$ needed to set a blue-top grading stake at a specified design elevation $E$: storing benchmark elevation `4812.40 {{keycap:H}}`, backsight `6.85 {{keycap:B}}`, and design grade elevation `4813.83 {{keycap:E}}` and pressing `{{key:SOLVE}} {{keycap:F}}` returns the exact target rod reading $F = \mathbf{5.4200\text{ ft}}$.

### Try It on the Stack

Practice circular route curve staking, parabolic vertical curves, and three-wire differential leveling with these three field problems:

1. **Highway Curve Layout from Radius and Deflection Angle:** For a circular alignment with radius $R = 1{,}200.00\text{ ft}$ and deflection angle $\Delta = 28.5^\circ$, evaluate `1200 {{key:ENTER}} 28.5 {{key:CRV}}` to find tangent distance $T$ in Register $Y$ and arc length $L$ in Register $X$, then compute long chord $LC = 2R\sin(14.25^\circ)$. *(Verified stack results: $T = \mathbf{304.77\text{ ft}}$ in $Y$, $L = \mathbf{596.90\text{ ft}}$ in $X$, and $LC \approx \mathbf{590.80\text{ ft}}$.)*
2. **Parabolic Vertical Curve and Earthwork Cut Volume:** Evaluate `425.00 {{key:ENTER}} 2.5 {{key:ENTER}} 1.75 {{key:+/-}} {{key:ENTER}} 8 {{key:VCV}}` for the midpoint parabolic elevation at $x = 4\text{ stations}$, and compute the cubic-yard volume of a $180\text{ ft}$ prism cut between end areas $A_1 = 250\text{ ft}^2$ and $A_2 = 380\text{ ft}^2$ via `250 {{key:ENTER}} 380 {{key:ENTER}} 180 {{key:CUT}}`. *(Verified Register $X$ results: $\text{Elev}(4) = \mathbf{430.75\text{ ft}}$ and $V = \mathbf{2{,}100.00\text{ yd}^3}$.)*
3. **Three-Wire Benchmark Transfer and Grade Check:** Verify foresight stadia wires $T = 7.82\text{ ft}, M = 5.42\text{ ft}, B_w = 3.02\text{ ft}$ via `7.82 {{key:ENTER}} 5.42 {{key:ENTER}} 3.02 {{key:LVL}}`, transfer benchmark elevation $H = 842.15\text{ ft}$ with backsight $B = 5.32\text{ ft}$ in the `LVL` workspace (`842.15 {{keycap:H}} 5.32 {{keycap:B}} 5.42 {{keycap:F}} {{key:SOLVE}} {{keycap:E}}`), and find the grade percentage (`{{key:GR%}}`) of a $-6.00\text{ ft}$ fall over that $480.00\text{ ft}$ stadia distance (`6 {{key:+/-}} {{key:ENTER}} 480 {{key:GR%}}`). *(Verified results: expected mid-wire $\mathbf{5.42\text{ ft}}$ in $Y$, stadia distance $D = \mathbf{480.00\text{ ft}}$ in $X$, $E = \mathbf{842.05\text{ ft}}$, and $\text{GR\%} = \mathbf{-1.2500\%}$.)*

From terrestrial sightlines and canyon switchbacks, we lift off into the third dimension of moving air masses, aircraft weight-and-balance moments, and barometric lapse rates in Chapter 3.

---

# Chapter 3: Night Approach Under a Mountain Crosswind

At dusk over the high desert of eastern Oregon, a twin-turboprop medical transport aircraft cruises at $14{,}200\text{ ft}$ Mean Sea Level (`MSL`) along a desired true course of $045^\circ$ (Northeast) at a True Airspeed of $V_{\text{TAS}} = 145\text{ knots}$ over a $D = 128\text{ NM}$ mountain leg. Ahead lies a high-elevation valley airstrip at a Pressure Altitude of $P = 6{,}200\text{ ft}$, flanked by basalt rimrock. As a dry cold front spills over the Cascades, winds aloft blow at $V_w = 28\text{ knots}$ at an angle of $\theta = 40^\circ$ off the aircraft's nose, while the automated weather station at the destination runway reports a late-afternoon desert Outside Air Temperature of $T = 28^\circ\text{C}$.

Before descending through the mountain pass, the captain must resolve three interconnected flight-deck calculations that have governed air navigation since Lieutenant Philip Dalton patented the circular E-6B flight computer in 1933. First, the pilot must decompose the $28\text{ kt}$ wind at $\theta = 40^\circ$ (`{{key:WND}}`, `{{key:XWC}}`) into its longitudinal headwind component ($21.45\text{ kt}$ in Register $Y$) and lateral crosswind component ($18.00\text{ kt}$ in Register $X$), determine the Wind Correction Angle ($\text{WCA}$) and Ground Speed ($\text{GS}$), and verify via the `TSD` (`D = S × T`) solver (`{{key:TSD}}`, variables `{{keycap:D}}`, `{{keycap:S}}`, `{{keycap:T}}`) that the aircraft can cover the $128\text{ NM}$ leg within its fuel endurance window. Second, after loading a patient litter in the cabin, the crew must verify the aircraft's longitudinal center-of-gravity moment $M = W \times A$ (`{{key:CG}}`, variables `{{keycap:M}}`, `{{keycap:W}}`, `{{keycap:A}}`). Third, because high desert heat ($T = 28^\circ\text{C}$) at Pressure Altitude $P = 6{,}200\text{ ft}$ thins the air column over the runway, the crew must evaluate Density Altitude (`{{key:ALT}}`, variables `{{keycap:D}}`, `{{keycap:P}}`, `{{keycap:T}}`) to determine the aircraft's true landing roll and single-engine climb performance.

---

## Aeronautical Wind Triangles, Crab Angles, and Weight-and-Balance Moments

An aircraft in flight moves within an air mass that is itself moving across the ground. Navigating along a fixed geographic track and maintaining longitudinal pitch stability require decomposing wind vectors into orthogonal headwind and crosswind components and balancing mass moments about the aircraft datum.

### Wind Vector Decomposition, Crosswind Limits, and Wind Correction Angles

When an aircraft aligns with a runway or flies a cross-country course of heading $\psi_{\text{course}}$, a wind of speed $V_w$ (in knots, converted via `{{key:▸kt}}`) blowing from direction $\psi_{\text{wind}}$ forms a relative wind angle $\theta = \psi_{\text{wind}} - \psi_{\text{course}}$ with the flight path. Staging wind speed $V_w$ in Register $Y$ and relative wind angle $\theta$ in Register $X$ and pressing `{{key:WND}}` simultaneously decomposes the wind vector into its longitudinal **Headwind Component** $V_{\text{hw}}$ in Register $Y$ and its lateral **Crosswind Component** $V_{\text{xw}}$ in Register $X$ (while `{{key:XWC}}` isolates the crosswind component directly):

![Aeronautical wind vector decomposition into longitudinal headwind and lateral runway crosswind components.](../assets/diagrams/domains/diagram_ch01_wind_triangle.png)

$$V_{\text{hw}} = V_w \cos(\theta), \qquad V_{\text{xw}} = V_w \sin(\theta), \qquad \text{WCA} = \arcsin\!\left(\frac{V_{\text{xw}}}{V_{\text{TAS}}}\right), \qquad \text{GS} = V_{\text{TAS}} \cos(\text{WCA}) - V_{\text{hw}}$$

In these velocity-triangle equations, $V_{\text{TAS}}$ is the aircraft's True Airspeed through the air mass, $\text{WCA}$ is the **Wind Correction Angle** (crab angle) derived from the Law of Sines so the aircraft's lateral airspeed component $V_{\text{TAS}}\sin(\text{WCA})$ cancels the crosswind drift $V_{\text{xw}}$, and $\text{GS}$ is the resulting Ground Speed along the desired track. With a $V_w = 28\text{ kt}$ wind blowing at $\theta = 40^\circ$ off the course (`28 {{key:ENTER}} 40 {{key:WND}}`), the instrument places the headwind component $V_{\text{hw}} = 28\cos(40^\circ) = \mathbf{21.45\text{ kt}}$ into Register $Y$ and the crosswind component $V_{\text{xw}} = 28\sin(40^\circ) = \mathbf{18.00\text{ kt}}$ into Register $X$. Crabbing into the wind at $V_{\text{TAS}} = 145\text{ kt}$ by $\text{WCA} = \arcsin(18.00 / 145) \approx \mathbf{7.13^\circ}$ (`{{key:ASIN}}`) holds the desired track over the ridge at a net ground speed of $\text{GS} = 145\cos(7.13^\circ) - 21.45 \approx 143.88 - 21.45 = \mathbf{122.43\text{ kt}}$.

### Endurance Time-Speed-Distance (`{{key:TSD}}`) and Aircraft Weight & Balance (`{{key:CG}}`)

Across any navigation leg of distance $D$ (in nautical miles, `{{key:▸NM}}`, where $1\text{ NM} = 6{,}076.12\text{ ft} = 1{,}852\text{ m}$) flown at ground speed $S = \text{GS}$ (in knots, $\text{NM/hr}$) over elapsed time $T$ (in hours), the **Time–Speed–Distance** relation (`{{key:TSD}}`, workspace variables `{{keycap:D}}`, `{{keycap:S}}`, `{{keycap:T}}`) is $D = S \times T$. Simultaneously, loading passengers, medical litters, and fuel aboard the aircraft shifts the longitudinal **Center of Gravity (`{{key:CG}}`)** relative to the manufacturer's reference datum: each item of weight $W$ (in pounds) located at station arm $A$ (in inches aft of datum) generates a pitching **Moment** $M = W \times A$ (`{{key:CG}}`, workspace variables `{{keycap:M}}`, `{{keycap:W}}`, `{{keycap:A}}`), and dividing the total aircraft moment $\Sigma M$ by total gross weight $\Sigma W$ locates the center-of-gravity station $A_{\text{CG}}$:

$$D = S \times T, \qquad M = W \times A, \qquad A_{\text{CG}} = \frac{\sum M_i}{\sum W_i}$$

Over the $D = 128.0\text{ NM}$ mountain leg at ground speed $S = 122.43\text{ kt}$, solving `TSD` (`D = S × T`) for time $T$ yields $T = 128.0 / 122.43 \approx \mathbf{1.0455\text{ hr}}$ ($62.7\text{ min}$). Meanwhile, a $W = 220\text{ lb}$ medical litter locked into cabin station arm $A = 145.0\text{ in}$ adds a pitching moment of $M = 220 \times 145.0 = \mathbf{31{,}900\text{ lb}\cdot\text{in}}$ via `{{key:CG}}`.

---

## International Standard Atmosphere, Pressure Altitude, and Density Altitude

Aerodynamic lift, propeller thrust, and turbine mass flow depend on the local mass density $\rho$ of the air column rather than the geometric height above sea level read from a map.

### Barometric Lapse Rates and Standard Temperature at Altitude

Under the **International Standard Atmosphere (`ISA`)**, standard sea-level barometric pressure is $P_0 = 29.92\text{ inHg}$ ($1013.25\text{ hPa}$) and standard sea-level temperature is $T_0 = 15^\circ\text{C}$ ($59^\circ\text{F}$), with temperature decreasing through the troposphere at a standard lapse rate of $2^\circ\text{C}$ per $1{,}000\text{ ft}$ of pressure altitude $P$:

$$P = E_{\text{field}} + 1000 \times \left(29.92 - \text{AltSet}\right), \qquad T_{\text{ISA}}(P) = 15^\circ\text{C} - 2^\circ\text{C} \times \left(\frac{P}{1000}\right)$$

At our high-desert destination airstrip where the Pressure Altitude is $P = 6{,}200\text{ ft}$, the standard atmospheric temperature for that altitude is $T_{\text{ISA}} = 15 - 2 \times 6.2 = 15 - 12.4 = \mathbf{2.6^\circ\text{C}}$.

### Thermal Expansion and High-Elevation Density Altitude (`{{key:ALT}}`)

By the ideal gas law ($\rho = P / (R_{\text{specific}} T)$, explored at the molecular scale in Unit VI on the `SC-60`), heating an air parcel at constant pressure causes it to expand and become less dense. Each $1^\circ\text{C}$ of warming above the standard altitude temperature $T_{\text{ISA}}(P) = 15 - 0.002 P$ thins the air by the equivalent of $+120\text{ ft}$ of altitude gain, defining the **Density Altitude** (`{{key:ALT}}`) from Pressure Altitude $P$ (in feet) in Register $Y$ and Outside Air Temperature $T$ (in $^\circ\text{C}$) in Register $X$:

$$\text{DA} = P + 120 \times \left(T - T_{\text{ISA}}(P)\right) = P + 120 \times \left(T - \left(15 - 2 \times \frac{P}{1000}\right)\right)$$

At the high-desert strip where Pressure Altitude is $P = 6{,}200\text{ ft}$ ($T_{\text{ISA}} = 2.6^\circ\text{C}$) and the afternoon Outside Air Temperature is $T = 28^\circ\text{C}$, the $+25.4^\circ\text{C}$ thermal deviation above standard temperature adds $120 \times 25.4 = +3{,}048\text{ ft}$, raising the true Density Altitude via `6200 {{key:ENTER}} 28 {{key:ALT}}` to $\text{DA} = 6200 + 3048 = \mathbf{9{,}248\text{ ft}}$ and warning the crew to use high-altitude landing flare speeds and full reverse thrust.

---

## Flying the High-Desert Ridge on the Stack and Solver Workspace

On the **SC-35**, flight-navigation keys operate both as immediate two-register stack shortcuts and as bidirectional Equation Solver workspaces (`WIND` on `{{key:WND}}` with variables `{{keycap:X}}`, `{{keycap:V}}`, `{{keycap:A}}`; `ALT` on `{{key:ALT}}` with variables `{{keycap:D}}`, `{{keycap:P}}`, `{{keycap:T}}`; `TSD` on `{{key:TSD}}` with variables `{{keycap:D}}`, `{{keycap:S}}`, `{{keycap:T}}`; and `CG` on `{{key:CG}}` with variables `{{keycap:M}}`, `{{keycap:W}}`, `{{keycap:A}}`):

| Button | Operation | Register Z | Register Y | Register X | Governing Expression |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`{{key:WND}}`** | Headwind, Crosswind & Solver | — | Wind $V_w\ (\text{kt})$ | Angle $\theta^\circ$ | $Y' = V_w\cos\theta,\; X' = V_w\sin\theta$; `WIND` (`{{keycap:X}}`, `{{keycap:V}}`, `{{keycap:A}}`) |
| **`{{key:XWC}}`** | Crosswind Component | — | Wind $V_w\ (\text{kt})$ | Angle $\theta^\circ$ | $V_{\text{xw}} = V_w\sin(\theta)$ |
| **`{{key:TSD}}`** | Time–Speed–Distance Solver | — | Speed $S\ (\text{kt})$ | Time $T\ (\text{hr})$ | $D = S \times T$; `TSD` workspace (`{{keycap:D}}`, `{{keycap:S}}`, `{{keycap:T}}`) |
| **`{{key:CG}}`** | Weight & Balance Moment Solver | — | Weight $W\ (\text{lb})$ | Arm $A\ (\text{in})$ | $M = W \times A$; `CG` workspace (`{{keycap:M}}`, `{{keycap:W}}`, `{{keycap:A}}`) |
| **`{{key:ALT}}`** | Density Altitude & Solver | — | Press Alt $P\ (\text{ft})$ | OAT $T\ (^\circ\text{C})$ | $\text{DA} = P + 120(T - (15 - 0.002 P))$; `ALT` (`{{keycap:D}}`, `{{keycap:P}}`, `{{keycap:T}}`) |

### Solving the Wind Triangle, Density Altitude, and Weight & Balance on the Stack

Cruising at $V_{\text{TAS}} = 145\text{ kt}$ with a $V_w = 28\text{ kt}$ wind at angle $\theta = 40^\circ$ off course, keying `28 {{key:ENTER}} 40 {{key:WND}}` places the headwind component $V_{\text{hw}} = \mathbf{21.45\text{ kt}}$ in Register $Y$ and the crosswind component $V_{\text{xw}} = \mathbf{18.00\text{ kt}}$ in Register $X$. Dividing $V_{\text{xw}}$ by $145$ and pressing `{{key:ASIN}}` gives the crab angle $\text{WCA} = \mathbf{7.13^\circ}$. Next, keying `6200 {{key:ENTER}} 28 {{key:ALT}}` evaluates the destination Density Altitude $\text{DA} = \mathbf{9{,}248\text{ ft}}$ at Pressure Altitude $P = 6{,}200\text{ ft}$ and $T = 28^\circ\text{C}$, and keying `220 {{key:ENTER}} 145 {{key:CG}}` computes the $31{,}900\text{ lb}\cdot\text{in}$ cabin litter moment:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `28 {{key:ENTER}} 40 {{key:WND}}` | $0$ | $0$ | $21.45$ | $18.00$ | Resolve headwind $V_{\text{hw}} = 21.45\text{ kt}$ in $Y$ and crosswind $V_{\text{xw}} = 18.00\text{ kt}$ in $X$ |
| `145 {{key:÷}} {{key:ASIN}}` | $0$ | $0$ | $21.45$ | $7.13$ | Compute Wind Correction Angle $\text{WCA} = \arcsin(18.00/145) \approx 7.13^\circ$ |
| `6200 {{key:ENTER}} 28 {{key:ALT}}` | $0$ | $21.45$ | $7.13$ | $9248$ | Compute Density Altitude $\text{DA} = 6200 + 120(28 - 2.6) = 9{,}248\text{ ft}$ |
| `220 {{key:ENTER}} 145 {{key:CG}}` | $21.45$ | $7.13$ | $9248$ | **$31900$** | Compute cabin litter moment $M = 220\text{ lb} \times 145\text{ in} = 31{,}900\text{ lb}\cdot\text{in}$ |

### Inverse Solves in the `TSD`, `CG`, `WIND`, and `ALT` Workspaces

To verify fuel endurance, baggage station limits, crosswind limits, and thermal departure ceilings using the **Bidirectional Equation Solver Workspaces**:
- **Inverse Groundspeed Solve in `TSD` (`{{key:TSD}}`, `D = S × T`):** When remaining non-reserve fuel fixes maximum leg endurance time to $T = 0.90\text{ hr}$ ($54.0\text{ min}$) across the $D = 128.0\text{ NM}$ mountain pass leg, opening `{{key:SOLVE}} {{key:TSD}}` displays `D = S × T` with variable softkeys `{{keycap:D}}` (`{{key:LFU0}}`), `{{keycap:S}}` (`{{key:LFU1}}`), and `{{keycap:T}}` (`{{key:LFU2}}`). Keying `128 {{keycap:D}}` and `0.90 {{keycap:T}}` and pressing `{{key:SOLVE}} {{keycap:S}}` (`{{key:LFU1}}`) solves backward for the minimum required groundspeed $S = 128.0 / 0.90 \approx \mathbf{142.2222\text{ kt}}$.
- **Inverse Cargo Weight Limit in `CG` (`{{key:CG}}`, `M = W × A`):** If the aft baggage bay at arm $A = 180.0\text{ in}$ (`180 {{keycap:A}}`) is restricted to a maximum moment contribution of $M = 27{,}000\text{ lb}\cdot\text{in}$ (`27000 {{keycap:M}}`), pressing `{{key:SOLVE}} {{keycap:W}}` solves backward for the maximum allowable aft cargo weight $W = 27{,}000 / 180.0 = \mathbf{150.00\text{ lb}}$.
- **Inverse Temperature Ceiling in `ALT` (`{{key:ALT}}`):** Opening `{{key:SOLVE}} {{key:ALT}}` binds softkeys `{{keycap:D}}` (`{{key:LFU0}}`), `{{keycap:P}}` (`{{key:LFU1}}`), and `{{keycap:T}}` (`{{key:LFU2}}`), allowing the crew to store the maximum chart density altitude `{{keycap:D}}` and pressure altitude `{{keycap:P}}` and press `{{key:SOLVE}} {{keycap:T}}` for the maximum outside air temperature.

### Try It on the Stack

Consolidate your mastery of the `SC-35` flight-navigation keys and solver workspaces with these three cockpit problems:

1. **Wind Vector Decomposition and Crab Angle:** Flying at true airspeed $V_{\text{TAS}} = 145\text{ kt}$ with a $V_w = 28\text{ kt}$ wind at relative angle $\theta = 40^\circ$, key `28 {{key:ENTER}} 40 {{key:WND}}` to find headwind $V_{\text{hw}}$ in Register $Y$ and crosswind $V_{\text{xw}}$ in Register $X$, then key `145 {{key:÷}} {{key:ASIN}}` for $\text{WCA}$. *(Verified stack results: $V_{\text{hw}} = \mathbf{21.45\text{ kt}}$ in $Y$, $V_{\text{xw}} = \mathbf{18.00\text{ kt}}$ in $X$, and $\text{WCA} \approx \mathbf{7.13^\circ}$.)*
2. **Inverse Wind Angle Limit in `WIND` and Density Altitude (`{{key:ALT}}`):** On an aircraft with a $15.0\text{ kt}$ maximum demonstrated crosswind limit (`15 {{keycap:X}}`) landing in a $V = 30.0\text{ kt}$ wind (`30 {{keycap:V}}`), open the `WIND` workspace (`{{key:SOLVE}} {{key:WND}}`) and press `{{key:SOLVE}} {{keycap:A}}` to find the maximum allowable wind angle $\theta_{\max}$; then evaluate `6200 {{key:ENTER}} 28 {{key:ALT}}` for density altitude at $P = 6{,}200\text{ ft}$ and $T = 28^\circ\text{C}$. *(Verified Register $X$ results: $\theta_{\max} = \mathbf{30.00^\circ}$ and $\text{DA} = \mathbf{9{,}248\text{ ft}}$.)*
3. **Endurance Leg Check (`{{key:TSD}}`) and Weight & Balance (`{{key:CG}}`):** Use `{{key:TSD}}` to find the required groundspeed $S$ to cover $D = 165\text{ NM}$ (`165 {{keycap:D}}`) in $T = 1.25\text{ hr}$ (`1.25 {{keycap:T}} {{key:SOLVE}} {{keycap:S}}`), and use `{{key:CG}}` (`350 {{key:ENTER}} 120 {{key:CG}}`) to compute the moment of $350\text{ lb}$ of fuel at station arm $120\text{ in}$. *(Verified Register $X$ results: $S = \mathbf{132.00\text{ kt}}$ and $M = \mathbf{42{,}000\text{ lb}\cdot\text{in}}$.)*

With terrestrial surveying, circular route alignments, and flight-deck vector navigation complete on the `SC-35`, we turn from the open landscape to industrial power distribution, conduit geometry, and machine-shop instrumentation in [Unit II: Electrical Power, Conduit Geometry & Industrial Trades](02-sc14-electrical-trades.md).
