---
title: "StackCalc Domain Calculator Series: Field Applied Mathematics & Professional Manuals"
description: "A comprehensive applied mathematics introduction to the 9 StackCalc domain calculators (SC-35, SC-14, SC-16, SC-24, SC-50, SC-60, SC-78, SC-80, SC-95)."
---

# StackCalc Domain Calculator Series
## When Mathematics Meets the Physical Trades

> **Who this series is for:** You already know how algebra, trigonometry, vectors, and logarithms work on paper. But how does an electrician turn right triangles into bent steel pipes thirty feet in the air? How does an artisan baker use percentages where the total is $197\%$? Why does an ICU nurse use square roots of height and weight to protect an elderly patient's kidneys? And why does a radio engineer care about waves reflecting backward down a coaxial cable?

---

### The Philosophy: Mathematics Grounded in Physical Reality

Pure mathematics is clean, timeless, and abstract. But when math steps out of the lecture hall and onto a job site, it hits the friction of the real world:
- Heat dissipates in copper wires.
- Measurement errors compound across property lines.
- Microprocessors overflow when numbers exceed silicon registers.
- Yeast fermentation speeds up when a mixer blade gets warm.
- Sound waves collide in echoes and phase cancellations.

For decades, professionals in these fields used specialized pocket slide rules, tables, or legendary instruments like the **HP-35**, **HP-16C**, and **HP-12C**. 

The **StackCalc Domain Series** expands that heritage into nine specialized physical and software instruments. Each calculator takes the timeless power of the 4-level Reverse Polish Notation (RPN) stack and customizes its keys, constants, and display for the natural rhythm of a specific craft.

Every instrument in the series shares five core engineering principles:

1. **Pure Scalar Stack (`X`, `Y:`, `Z:`, `T:`):** Calculations are never blocked by clunky unit-mismatch errors. The numbers are clean, double-precision scalars.
2. **Top-Zero Suppression:** Empty stack registers above your active numbers stay silent, keeping the screen uncluttered.
3. **Dedicated Table Inspector (`TBL` via `[g] [+/-]`):** Lookup tables (AWG wire ampacities, periodic table molar masses, hop yields, and pipe dimensions) are accessible instantly without modifying your working stack.
4. **Physical Row 0 Softkeys:** Six dedicated keys align with LCD screen slots for 1-tap parameter workspaces.
5. **Non-Destructive Inspection (`SHOW`):** Transiently displays deep analytical breakdowns (like quadrant bearings, IEEE-754 float bitfields, or kitchen utensil equivalents) and returns to the stack untouched.

---

### Discipline Chapters & Overviews

```
documentation/manuals/domains/
├── 01-sc35-geomatics-navigation.md  # Land Surveying, Civil COGO & Flight Navigation
├── 02-sc14-electrical-trades.md     # Electrical Feeder Sizing, Conduit Bending & Machining
├── 03-sc16-systems-cyber.md         # Embedded Firmware, Two's Complement & IEEE-754 Floats
├── 04-sc24-cinema-broadcast.md      # Cinema Optics, SMPTE Timecode & Sound Acoustics
├── 05-sc50-rf-spectrum.md           # RF Microwaves, VSWR, Return Loss & Smith Charts
├── 06-sc60-chemistry-wetlab.md      # Molecular Weights, Dilutions, pH & Buffer Solutions
├── 07-sc78-culinary-brewing.md      # Baker's Percentages, Dough Thermodynamics & Brewing
├── 08-sc80-clinical-pharmacy.md     # Patient Biometrics, BSA, Renal Dosing & IV Infusions
└── 09-sc95-finance-statistics.md    # 5-Key TVM, Cash Flows, Six Sigma & R Distributions
```

#### [Chapter 1: SC-35 Geomatics, Land Surveying & Flight Navigation](01-sc35-geomatics-navigation.md)
*Mapping a World That Refuses to Stand Still*
- **The Core Puzzle:** Why do surveyors swap sine and cosine compared to standard math, and why do historic property deeds use quadrant bearings ($\text{S } 45^\circ \text{ W}$) instead of $0\text{--}360^\circ$ angles?
- **Key Concepts:** Sexagesimal $DDD.MMSS$ angles, Forward and Inverse Coordinate Geometry (COGO), traverse loop closure with Gauss's Shoelace polygon area, and solving aerodynamic crosswind drift.

#### [Chapter 2: SC-14 Industrial Trades, Electrical & Mechanical Handbook](02-sc14-electrical-trades.md)
*When Ohm's Law Meets Heavy Copper*
- **The Core Puzzle:** Why does a vacuum cleaner dim your living room lamp, and how do electricians use cosecant multipliers to bend rigid steel conduit around ceiling beams?
- **Key Concepts:** Conductor resistance and Circular Mils ($CM$), single-phase and 3-phase voltage drop ($VD = 2KIL/CM$), the geometric $\sqrt{3} \approx 1.732$ factor of 3-phase AC power, and CNC surface feet per minute ($SFM$).

#### [Chapter 3: SC-16 Systems Programming, Embedded & Cyber Operations](03-sc16-systems-cyber.md)
*When Numbers Hit the Silicon Ceiling*
- **The Core Puzzle:** Why do digital odometers and computer registers roll over to zero, and how did a 16-bit integer overflow destroy the Ariane 5 rocket?
- **Key Concepts:** Two's complement signed integer mechanics, speaking in hexadecimal (base-16 nibbles), memory alignment padding gaps, and dissecting single-precision IEEE-754 floating-point bits.

#### [Chapter 4: SC-24 Cinema Optics, Broadcast Timecode & Sound Handbook](04-sc24-cinema-broadcast.md)
*When Light and Sound Become Numbers*
- **The Core Puzzle:** Why does North American television run at $29.97\text{ frames per second}$ instead of $30.00$, and why are two people shouting together only $3\text{ dB}$ louder than one?
- **Key Concepts:** SMPTE drop-frame drift compensation, circle of confusion and hyperfocal depth-of-field, Exposure Value ($EV$) photometrics, and logarithmic acoustic decibel summing ($dB\oplus$).

#### [Chapter 5: SC-50 RF Spectrum, Transmission Lines & Microwave Handbook](05-sc50-rf-spectrum.md)
*When Wires Stop Acting Like Wires*
- **The Core Puzzle:** Why do high-frequency radio waves bounce backward down an antenna cable like an echo in a canyon, and how does a mismatched antenna melt an expensive transmitter transistor?
- **Key Concepts:** Characteristic impedance ($50\,\Omega$ vs. $75\,\Omega$), reflection coefficient ($\Gamma$), Voltage Standing Wave Ratio ($VSWR$), folding the infinite impedance plane into a Smith Chart circle, and Friis cascaded receiver noise.

#### [Chapter 6: SC-60 Wet-Lab Chemistry, Stoichiometry & Spectroscopy](06-sc60-chemistry-wetlab.md)
*Counting What You Cannot See*
- **The Core Puzzle:** How do analytical chemists translate an exact count of trillions of invisible molecules into a pile of white powder on a lab balance?
- **Key Concepts:** IUPAC molar mass summation ($m = C \cdot V \cdot MW$), serial dilution ($C_1 V_1 = C_2 V_2$), logarithmic pH scales, Henderson-Hasselbalch biochemical buffer design, and the Beer-Lambert spectrophotometry law.

#### [Chapter 7: SC-78 Commercial Bakery, Fermentation Science & Brewing](07-sc78-culinary-brewing.md)
*When the Kitchen Becomes a Laboratory*
- **The Core Puzzle:** Why is measuring flour by volume a trap, and why do commercial bakeries anchor flour at $100\%$ so that recipes can total $197\%$?
- **Key Concepts:** Baker's Percentages ($BK\%$), Desired Dough Water Temperature ($T_W$) with spiral-mixer friction compensation, equilibrium meat curing salinity, and brewing specific gravity ($SG, ^\circ\text{P}, ABV$).

#### [Chapter 8: SC-80 Clinical Nursing, Hospital Pharmacy & Infusions](08-sc80-clinical-pharmacy.md)
*When a Decimal Point Means Everything*
- **The Core Puzzle:** Why is dosing a drug purely by body weight dangerous, and why do cancer chemotherapy and critical care medications scale with surface area ($m^2$)?
- **Key Concepts:** The persistent Patient Profile (`@PAT`), Mosteller Body Surface Area, Cockcroft-Gault Creatinine Clearance ($CrCl$) for aging kidneys, and microgram weight-based infusion pump titrations ($\mu\text{g/kg/min}$).

#### [Chapter 9: SC-95 Quantitative Finance, Actuarial Science & Six Sigma](09-sc95-finance-statistics.md)
*The Cost of Tomorrow: Time, Uncertainty, and Capital*
- **The Core Puzzle:** Why is $\$10{,}000$ today worth more than $\$10{,}000$ in ten years, and how do industrial engineers know if a factory process is producing defect-free parts?
- **Key Concepts:** The William Kahan 5-key TVM system ($PV, i, N, PMT, FV$), discounted cash flows (NPV and IRR), bond pricing, and Six Sigma process capability indices ($C_p, C_{pk}$).

---

### Verification Suite & Source Grounding

Every calculation, keystroke sequence, and formula documented in these chapters is tested against our automated test suites in `watch-calc-32`:
- `DomainSoftkeyAndInputModeTests.swift`: Validates softkey layouts and input modes across all 9 domain models.
- `DomainForumIntegrationTests.swift`: Validates real-world problem solutions from practitioner forums.
- `ModelMatrixTests.swift`: Confirms 100% key coordinate invariance across the calculator family.
