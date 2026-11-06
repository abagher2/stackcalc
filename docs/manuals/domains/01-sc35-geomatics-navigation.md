---
title: "SC-35 Geomatics, Land Surveying & Flight Navigation"
description: "An applied introduction to the mathematics of land surveying, coordinate geometry (COGO), curves, and aeronautical navigation on the StackCalc 35 RPN calculator."
---

# SC-35 Geomatics, Land Surveying & Flight Navigation

> **Who this is for:** Anyone who knows high school trigonometry and vectors, but has ever wondered how a surveyor turns a tripod on a muddy hillside into legal property boundaries, or how an airplane pilot navigates across a continent without drifting off course in the wind.

---

## 1. Mapping a World That Refuses to Stand Still

If you took geometry in school, you learned to plot points on a neat Cartesian plane: $x$ goes to the right, $y$ goes up, and angles turn counterclockwise starting from the positive $x$-axis.

Then you step outside with a tripod, and the real world immediately breaks all three rules:
1. **North is up, not East.** In land surveying and aviation, $0^\circ$ points straight toward North.
2. **Angles turn clockwise, like a clock face.** $90^\circ$ is East, $180^\circ$ is South, and $270^\circ$ is West.
3. **The ground is not flat.** The earth is a bumpy, curved spheroid, and every measurement you make with a laser, tape, or compass accumulates physical error.

Centuries ago, when young surveyors like George Washington paced out Virginia valley tracts with a 66-foot iron chain, or when sea captains like Nathaniel Bowditch steered sailing ships by the stars, they faced the same fundamental challenge: **How do you keep small measurement errors from compounding into legal and physical disasters?** 

If a boundary line is off by just a quarter of a degree, that error acts like a giant lever arm. Over a half-mile run, a property fence drifts by dozens of feet, overlapping a neighbor's land and sparking bitter legal disputes. In the air, a five-degree wind error over a three-hour flight can put an airplane fifty miles off course over fuel-empty wilderness.

The **StackCalc 35 (SC-35)** is designed specifically to tame this geometry. Instead of forcing you to balance parentheses or convert sexagesimal degrees in your head while standing in the rain or turbulence, it puts coordinate geometry (COGO), horizontal curve design, differential leveling, and wind-triangle vector calculations directly into a fast, transparent 4-level RPN stack.

### Why Not Just Use a Phone App?

Modern surveyors have $\$30{,}000$ robotic total stations, and pilots carry iPad tablets running GPS moving maps. Why does anyone want a dedicated pocket instrument?

- **Sunlight, Rain, and Gloves:** Capacitive phone screens wash out in harsh desert glare, register phantom touches in the rain, and refuse to work when you are wearing heavy leather work gloves or flight mittens. The SC-35 uses high-contrast reflective optics and crisp tactile mechanical keys you can feel through a glove.
- **The Legal Reality of Old Deeds:** Modern GPS gives coordinates in decimal degrees and $360^\circ$ azimuths. But real property deeds recorded fifty or a hundred years ago are written in **Quadrant Bearings**: *"Thence South $42^\circ 15' 30''$ West, $324.50\text{ feet}$"*. Re-tracing a boundary requires typing quadrant angles directly.
- **Licensing Exam Rules:** The National Council of Examiners for Engineering and Surveying (NCEES) strictly bans smartphones, cellular tablets, and graphing calculators from Fundamentals of Surveying (FS) exams. Candidates must know how to solve traverse loops on a dedicated, approved instrument.

---

## 2. Core Concepts: How Surveyors and Pilots Think

### Concept 1: The Compass Clock and Sexagesimal Angles

In high school math, you convert $125^\circ 30'$ into $125.5^\circ$ before pressing `[SIN]`. But in surveying and navigation, angles are always read from optical theodolites, compass circles, and navigation charts in **Degrees, Minutes, and Seconds ($DDD^\circ MM' SS''$)**:
- $1^\circ = 60 \text{ arcminutes } (')$
- $1' = 60 \text{ arcseconds } ('')$

On the SC-35, you don't need multi-key menu conversions. You enter sexagesimal angles as a single decimal number in canonical **`DDD.MMSS`** format:
- $125^\circ 30' 45''$ is entered directly as `125.3045`.
- $45^\circ 05' 12''$ is entered as `45.0512`.

Softkey 5 (`DMS` / `DEG`) toggles the calculator between sexagesimal and decimal degrees instantly.

#### Why the Trig Functions Swap Places
Because surveying azimuths measure clockwise from North ($+y$) rather than counterclockwise from East ($+x$), the trigonometric coordinate displacements swap roles:
- **Departure (East displacement):** $\Delta E = \text{Distance} \cdot \sin(\text{Azimuth})$
- **Latitude (North displacement):** $\Delta N = \text{Distance} \cdot \cos(\text{Azimuth})$

If you enter an azimuth of $90^\circ$ (due East), $\sin(90^\circ) = 1$ and $\cos(90^\circ) = 0$, so all your travel becomes East departure with zero North latitude.

```
                     North (0°)
                         ^
                         |        * Point B (E_B, N_B)
                         |       /
                         |      / Distance (D)
                         |  θ  / 
                         | ^  /   ΔN = D * cos(θ)
                         | | /
                         +----------> East (90°)
                   Point A (0, 0)   ΔE = D * sin(θ)
```

### Concept 2: The Two Fundamental Vector Problems (Forward & Inverse COGO)

Every land survey and aerial flight path comes down to two reciprocal questions:
1. **Forward COGO:** *"I am at point A. If I walk $500\text{ feet}$ along azimuth $045^\circ$, what are my new coordinates?"*
   $$E_B = E_A + D\sin\theta, \quad N_B = N_A + D\cos\theta$$
2. **Inverse COGO:** *"I have point A and point B on a map. What direction must I head, and how far must I travel to get from A to B?"*
   $$\Delta E = E_B - E_A, \quad \Delta N = N_B - N_A$$
   $$\text{Distance} = \sqrt{\Delta E^2 + \Delta N^2}, \quad \text{Azimuth} = \operatorname{atan2}(\Delta E, \Delta N)$$

On the SC-35, pressing `[ FWD ]` takes coordinates and vectors and outputs new coordinates; pressing `[ INV ]` takes two coordinate pairs and outputs distance and bearing in one keystroke.

### Concept 3: Traverse Misclosure and the Shoelace Formula

When a survey crew walks around a parcel of land and returns to the starting benchmark, the sum of all North departures ($\sum \Delta N$) and East departures ($\sum \Delta E$) should theoretically equal zero. In practice, slight optical and taping tolerances leave a small gap: the **linear error of closure ($c$)**:

$$c = \sqrt{\left(\sum \Delta E\right)^2 + \left(\sum \Delta N\right)^2}$$

If the crew walked $2{,}500\text{ feet}$ in total perimeter, and the closure error is $0.15\text{ feet}$, the precision ratio is:

$$\text{Precision} = \frac{2500}{0.15} \approx 16{,}667 \implies \mathbf{1:16{,}667}$$

This exceeds the standard $1:10{,}000$ legal code requirement for suburban boundary surveys.

To find the enclosed acreage, the SC-35 applies **Gauss's Shoelace Formula** across the sequential coordinates as they are entered into the `Σ+` register:

$$\text{Area} = \frac{1}{2} \left| \sum_{i=1}^{n-1} (E_i N_{i+1} - E_{i+1} N_i) + (E_n N_1 - E_1 N_n) \right|$$

Dividing square feet by $43{,}560$ yields acres.

### Concept 4: The Wind Triangle and Ground Speed

When an airplane flies through the atmosphere, the air mass itself is moving over the ground. The aircraft's actual path across the countryside (**Ground Track**) is the vector sum of its **True Airspeed Vector** ($\vec{V}_{\text{TAS}}$) and the **Wind Vector** ($\vec{V}_{\text{wind}}$).

```
          True Airspeed (TAS) along Heading (TH)
        *----------------------------------------->
         \                                       /
   Wind   \                                     / 
   Vector  \                                   / Ground Track & Speed (GS)
            v                                 v
```

By applying the Law of Sines to the triangle:
- **Wind Correction Angle (WCA):** The angle the nose of the plane must be turned *into* the wind so the airplane doesn't drift sideways off course.
- **Ground Speed (GS):** The actual speed the plane covers ground over the trees and runways.

---

## 3. Real-World Field Walkthroughs

### Field Case 1: Checking a Disputed Rural Boundary (`r/Surveying`)

A land surveyor is verifying a boundary line between two iron boundary monuments.
- Benchmark 1 is at coordinates: $1000.00\text{ N}, 1000.00\text{ E}$.
- Benchmark 2 is at coordinates: $1385.20\text{ N}, 1412.60\text{ E}$.
What is the exact boundary distance and quadrant bearing between the monuments?

#### How to Solve It on the SC-35
1. Compute $\Delta E = 1412.60 - 1000.00 = 412.60\text{ ft}$.
2. Compute $\Delta N = 1385.20 - 1000.00 = 385.20\text{ ft}$.
3. Enter into the RPN stack:
   - `412.60` `[ENTER]` `385.20`
4. Tap `[g] [POL]` (Rectangular to Polar / Inverse COGO):
   - Register $X$ displays: **`564.4842`** (Distance in feet).
   - Register $Y$ displays: **`46.9745`** (Azimuth in decimal degrees: $46.97^\circ$).
5. Convert decimal degrees to sexagesimal:
   - Tap `[f] [→HR]` $\to$ Register $Y$ shows **`46.5828`** ($46^\circ 58' 28''$).
6. Press `[BRG]` then `[g] [SHOW]`:
   - The LCD transiently displays: **`N 46° 58' 28" E`** (The exact quadrant bearing to write on the legal map).

---

### Field Case 2: Flying with a $25\text{-Knot}$ Crosswind (`r/flying`)

You are cruising in a light aircraft at a True Airspeed of $120\text{ knots}$ heading on a True Course of $070^\circ$. Flight Service reports winds aloft at $120^\circ$ at $25\text{ knots}$.
What heading should you fly, and what is your actual ground speed?

#### Step-by-Step Mechanics
1. **Find the Wind Angle:** $120^\circ - 070^\circ = 50^\circ$ (wind is blowing from $50^\circ$ to your right).
2. **Find the Crosswind Component:**
   - `25` `[ENTER]` `50` `[SIN]` `[×]` $\to$ **`19.15 knots`**.
3. **Find the Headwind Component:**
   - `25` `[ENTER]` `50` `[COS]` `[×]` $\to$ **`16.07 knots`**.
4. **Compute the Wind Correction Angle (WCA):**
   - $\sin(WCA) = \frac{19.15}{120} = 0.1596$
   - `19.15` `[ENTER]` `120` `[÷]` `[g] [ASIN]` $\to$ **`+9.18°`**.
   - You must turn $9.2^\circ$ right into the wind: **Heading = $079.2^\circ$**.
5. **Compute Actual Ground Speed:**
   - $GS = 120 \cdot \cos(9.18^\circ) - 16.07 = 118.46 - 16.07 = \mathbf{102.39\text{ knots}}$.

---

## 4. Try It Yourself: Practice Problems

### Problem 1: Circular Highway Curve Tangent
A civil engineering plan calls for a highway curve with an intersection deflection angle $\Delta = 36^\circ 30' 00''$ ($36.5^\circ$) and a centerline radius $R = 1{,}200.00\text{ ft}$.
Calculate the tangent distance $T = R \tan(\Delta / 2)$.
*(Solution: $\Delta / 2 = 18.25^\circ$. $1200 \times \tan(18.25^\circ) = \mathbf{395.73\text{ ft}}$.)*

### Problem 2: Differential Leveling Loop
At setup 1, your optical level sights a rod on Bench Mark 1 (Elevation $= 842.15\text{ ft}$) with a backsight ($BS$) of $5.32\text{ ft}$. The foresight ($FS$) to Turning Point 1 is $6.88\text{ ft}$.
What is the height of instrument ($HI$) and the elevation of Turning Point 1?
*(Solution: $HI = 842.15 + 5.32 = \mathbf{847.47\text{ ft}}$. Elevation = $847.47 - 6.88 = \mathbf{840.59\text{ ft}}$.)*

### Problem 3: Density Altitude Check
An airport is at $3{,}500\text{ ft}$ elevation. On a hot summer day, ambient temperature is $35^\circ\text{C}$ ($95^\circ\text{F}$) with an altimeter setting of $29.72\text{ inHg}$.
Standard pressure altitude $PA = 3500 + (29.92 - 29.72) \times 1000 = 3{,}700\text{ ft}$.
Standard temperature at $3{,}700\text{ ft}$ is $15 - 2 \times 3.7 = 7.6^\circ\text{C}$.
Calculate Density Altitude: $DA = PA + 120 \times (T_{\text{actual}} - T_{\text{standard}})$.
*(Solution: $DA = 3700 + 120 \times (35 - 7.6) = \mathbf{6{,}988\text{ ft}}$. The airplane will perform on takeoff as if it were nearly $7{,}000$ feet up!)*
