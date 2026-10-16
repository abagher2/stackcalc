---
title: "Appendix C: Formulas, Conversions & Prime Catalogs"
description: "Comprehensive elementary mathematical reference catalog: geometric formulas with 4-register RPN stack traces, bidirectional unit conversion matrices, divisibility algorithms, and complete prime number directory under 200 for the StackCalc SC-6."
---

# Appendix C: Formulas, Conversions & Prime Catalogs

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">MATHEMATICAL ENGINE // APPENDIX C</span>
  <span class="te-viewport-status text-emerald-400">● 2D &bull; 3D GEOMETRY &bull; ACCUMULATOR STATS &bull; UNIT CONVERSIONS &bull; PRIMES UNDER 200 &bull; EUCLIDEAN GCF/LCM</span>
</div>

> CHAPTER BASELINE MODE: {{key:NUM}}
> Hardware Precision Reference • Zero Mode Dependencies

<div class="admonition note">
<p class="admonition-title">Unlocked Keycaps Ribbon — Students, Engineers &amp; Mathletes</p>
<p>
• <strong>Geometry Stack Templates:</strong> Complete RPN keystroke sequences and 4-register elevator stack traces ($T, Z, Y, X$) for all elementary 2D perimeters/areas and 3D volumes/surface areas.<br>
• <strong>Polyhedron Surface Area Accumulator:</strong> Zero-scratch-paper multi-face surface area evaluation via statistical memory <code>{{key:Σ+}}</code> and <code>{{key:Σx}}</code>.<br>
• <strong>Bidirectional Unit Conversions:</strong> High-precision conversion factors across Length, Mass/Weight, Capacity/Liquid Volume, Area, Speed, Pressure, Time, and Temperature ($F \leftrightarrow C \leftrightarrow K$).<br>
• <strong>Prime Directory &amp; Divisibility:</strong> Full catalog of all 46 primes under 200 with binary/hex encodings, Sieve of Eratosthenes walk-through, hardware prime factorization via <code>{{key:PRIME}}</code> and <code>{{key:FACT}}</code>, algorithmic divisibility tests, and Euclidean GCF/LCM duality via <code>{{key:÷R}}</code>.
</p>
</div>

---

## The RPN Formula Advantage

In standard elementary textbooks, geometric formulas and unit conversions are presented in algebraic notation with tangled parentheses:

$$A = \frac{1}{2}bh \qquad V = \frac{4}{3}\pi r^3 \qquad C = \frac{5}{9}(F - 32) \qquad A = \pi r \left(r + \sqrt{h^2 + r^2}\right)$$

When elementary students attempt to enter these formulas into conventional algebraic calculators, syntax errors frequently arise from misplaced parentheses, incorrect order-of-operation hierarchies, or premature rounding of intermediate values.

On the **StackCalc SC-6**, grounded in Jan Łukasiewicz’s parenthesis-free notation {{cite:lukasiewicz1924}} and Kathy Hamrick’s history of RPN calculator architecture {{cite:hamrick1980}}, the four-register automatic operational stack ($X, Y, Z, T$) eliminates parentheses entirely. Following David Macaulay’s cutaway principles {{cite:macaulay2016}}, intermediate values remain clearly visible on upper elevator floors and drop into place exactly when an operator is tapped. This appendix provides validated RPN execution templates for every standard elementary formula.

<div class="admonition note">
<p class="admonition-title">Four-Register Stack Elevator Architecture</p>

| Register | Metaphor | Architectural Role |
| :--- | :--- | :--- |
| **Register T** | Penthouse | Holds top constants and duplicates on stack drop |
| **Register Z** | Second Balcony | Holds intermediate sub-expressions |
| **Register Y** | First Balcony | Holds waiting number for binary operation |
| **Register X** | Ground Lobby | Active entry and current computed result |
</div>

---

## Table 1: Elementary Geometric Formulas Directory

### Two-Dimensional Perimeter & Area Formulas

The following table summarizes 2D geometric formulas, standard metric and customary units, and their validated SC-6 RPN keystroke sequences:

| Shape | Metric / Customary Formula | SC-6 RPN Keystroke Sequence | Stack Registers Used |
|:---|:---|:---|:---:|
| **Square (Perimeter)** | $P = 4s$ | `s {{key:ENTER}} {{key:4}} {{key:×}}` | $Y, X$ |
| **Square (Area)** | $A = s^2$ | `s {{key:x²}}` | $X$ (Unary) |
| **Rectangle (Perimeter)** | $P = 2(l + w)$ | `l {{key:ENTER}} w {{key:+}} {{key:2}} {{key:×}}` | $Y, X$ |
| **Rectangle (Area)** | $A = l \times w$ | `l {{key:ENTER}} w {{key:RECT}}` | $Y, X$ |
| **Triangle (Perimeter)** | $P = a + b + c$ | `a {{key:ENTER}} b {{key:+}} [c] {{key:+}}` | $Z, Y, X$ |
| **Triangle (Area)** | $A = \frac{1}{2} b h$ | `b {{key:ENTER}} h {{key:×}} {{key:2}} {{key:÷}}` | $Y, X$ |
| **Parallelogram (Area)** | $A = b \times h$ | `b {{key:ENTER}} h {{key:×}}` | $Y, X$ |
| **Trapezoid (Area)** | $A = \frac{a + b}{2} \times h$ | `a {{key:ENTER}} b {{key:+}} {{key:2}} {{key:÷}} h {{key:×}}` | $Z, Y, X$ |
| **Circle (Circumference)** | $C = 2\pi r = \pi d$ | `d {{key:ENTER}} {{key:π}} {{key:×}}` | $Y, X$ |
| **Circle (Area)** | $A = \pi r^2$ | `r {{key:x²}} {{key:π}} {{key:×}}` | $Y, X$ |
| **Circle Sector (Area)** | $A = \frac{\theta}{360} \pi r^2$ | `r {{key:x²}} {{key:π}} {{key:×}} [θ] {{key:×}} 360 {{key:÷}}` | $Z, Y, X$ |
| **Circle Arc Length** | $s = \frac{\theta}{360} \pi d$ | `d {{key:π}} {{key:×}} [θ] {{key:×}} 360 {{key:÷}}` | $Z, Y, X$ |
| **Regular Polygon (Area)** | $A = \frac{1}{2} P \times a$ | `[P] {{key:ENTER}} `a` {{key:×}} {{key:2}} {{key:÷}}` | $Y, X$ |
| **Regular Hexagon (Area)** | $A = \frac{3\sqrt{3}}{2} s^2$ | `s {{key:x²}} {{key:3}} {{key:×}} {{key:3}} {{keycap:√x}} {{key:×}} {{key:2}} {{key:÷}}` | $Z, Y, X$ |
| **Ellipse (Area)** | $A = \pi \times a \times b$ | `a {{key:ENTER}} b {{key:×}} {{key:π}} {{key:×}}` | $Y, X$ |

---

### Deep-Dive 2D Stack Traces & Worked Numerical Examples

#### Example 2.2.1: Area of an Acute Triangle ($b = 14\text{ cm}, h = 9\text{ cm}$)
Formula: $A = \frac{1}{2} \times 14 \times 9 = 63\text{ cm}^2$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 14 | 0 | 0 | 0 | 14 |
| {{key:ENTER}} | 0 | 0 | 14 | 14 |
| {{key:9}} | 0 | 0 | 14 | 9 |
| {{key:×}} | 0 | 0 | 0 | 126 |
| {{key:2}} | 0 | 0 | 126 | 2 |
| {{key:÷}} | 0 | 0 | 0 | 63 |
*Stack Inspection:* The product $14 \times 9 = 126$ is evaluated first, then 2 enters Register $X$, pushing 126 to $Y$. Tapping `{{key:÷}}` divides $Y \div X = 126 \div 2 = 63$.

---

#### Example 2.2.2: Area of an Isosceles Trapezoid ($a = 8\text{ in}, b = 14\text{ in}, h = 6\text{ in}$)
Formula: $A = \frac{8 + 14}{2} \times 6 = \frac{22}{2} \times 6 = 11 \times 6 = 66\text{ sq in}$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:8}} | 0 | 0 | 0 | 8 |
| {{key:ENTER}} | 0 | 0 | 8 | 8 |
| 14 | 0 | 0 | 8 | 14 |
| {{key:+}} | 0 | 0 | 0 | 22 |
| {{key:2}} | 0 | 0 | 22 | 2 |
| {{key:÷}} | 0 | 0 | 0 | 11 |
| {{key:6}} | 0 | 0 | 11 | 6 |
| {{key:×}} | 0 | 0 | 0 | 66 |

---

#### Example 2.2.3: Area of a Circular Splash Pad ($r = 3.5\text{ m}$)
Formula: $A = \pi \times 3.5^2 = \pi \times 12.25 \approx 38.48451\text{ m}^2$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 3.5 | 0 | 0 | 0 | 3.5 |
| {{key:x²}} | 0 | 0 | 0 | 12.25 |
| {{key:ENTER}} | 0 | 0 | 12.25 | 12.25 |
| {{key:π}} | 0 | 0 | 12.25 | 3.1415926 |
| {{key:×}} | 0 | 0 | 0 | 38.484510 |

---

#### Example 2.2.4: Area of a Regular Hexagon ($s = 8\text{ cm}$)
Formula: $A = \frac{3\sqrt{3}}{2} s^2 = \frac{3 \times 1.7320508}{2} \times 64 = 2.598076 \times 64 \approx 166.27688\text{ cm}^2$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:8}} | 0 | 0 | 0 | 8 |
| {{key:x²}} | 0 | 0 | 0 | 64 |
| {{key:3}} | 0 | 0 | 64 | 3 |
| {{key:×}} | 0 | 0 | 0 | 192 |
| {{key:3}} | 0 | 0 | 192 | 3 |
| {{keycap:√x}} | 0 | 0 | 192 | 1.7320508 |
| {{key:×}} | 0 | 0 | 0 | 332.553759 |
| {{key:2}} | 0 | 0 | 332.553759 | 2 |
| {{key:÷}} | 0 | 0 | 0 | 166.276879 |

---

#### Example 2.2.5: Circular Sector Area and Arc Length ($r = 12\text{ cm}, \theta = 60^\circ$)
- Arc Length: $s = \frac{60}{360} \times 2 \pi (12) = \frac{1}{6} \times 24\pi = 4\pi \approx 12.56637\text{ cm}$.
- Sector Area: $A = \frac{60}{360} \times \pi (12^2) = \frac{1}{6} \times 144\pi = 24\pi \approx 75.39822\text{ cm}^2$.

Keystrokes for Sector Area:
- Key in: `12 {{key:x²}} {{key:π}} {{key:×}} 60 {{key:×}} 360 {{key:÷}}`.
- LCD Result: **$75.39822\text{ cm}^2$**.

---

### Three-Dimensional Solid Volume & Surface Area Formulas

| Solid | Volume Formula ($V$) | Total Surface Area Formula ($A$) | SC-6 Volume Keystrokes |
|:---|:---|:---|:---|
| **Cube** ($s$) | $V = s^3$ | $A = 6s^2$ | `s {{key:ENTER}} {{key:3}} {{keycap:yˣ}}` |
| **Rectangular Prism** ($l, w, h$) | $V = l \times w \times h$ | $A = 2(lw + lh + wh)$ | `l {{key:ENTER}} w {{key:×}} h {{key:×}}` |
| **Right Cylinder** ($r, h$) | $V = \pi r^2 h$ | $A = 2\pi rh + 2\pi r^2$ | `r {{key:x²}} {{key:π}} {{key:×}} h {{key:×}}` |
| **Right Cone** ($r, h$) | $V = \frac{1}{3}\pi r^2 h$ | $A = \pi r(r + \sqrt{h^2 + r^2})$ | `r {{key:x²}} {{key:π}} {{key:×}} h {{key:×}} {{key:3}} {{key:÷}}` |
| **Square Pyramid** ($b, h$) | $V = \frac{1}{3}b^2 h$ | $A = b^2 + 2b\sqrt{(b/2)^2 + h^2}$ | `b {{key:x²}} h {{key:×}} {{key:3}} {{key:÷}}` |
| **Sphere** ($r$) | $V = \frac{4}{3}\pi r^3$ | $A = 4\pi r^2$ | `{{key:4}} {{key:ENTER}} {{key:3}} {{key:÷}} {{key:π}} {{key:×}} `r` {{key:3}} {{keycap:yˣ}} {{key:×}}` |
| **Hemisphere** ($r$) | $V = \frac{2}{3}\pi r^3$ | $A = 3\pi r^2$ (solid) | `{{key:2}} {{key:ENTER}} {{key:3}} {{key:÷}} {{key:π}} {{key:×}} `r` {{key:3}} {{keycap:yˣ}} {{key:×}}` |
| **Torus** ($R, r$) | $V = 2\pi^2 R r^2$ | $A = 4\pi^2 R r$ | `{{key:2}} {{key:ENTER}} {{key:π}} {{key:x²}} {{key:×}} [R] {{key:×}} `r` {{key:x²}} {{key:×}}` |

---

### Deep-Dive 3D Stack Traces & Worked Numerical Examples

#### Example 2.4.1: Volume & Surface Area of a Storage Silo Cylinder ($r = 4\text{ m}, h = 10\text{ m}$)
- Volume: $V = \pi \times 4^2 \times 10 = 160\pi \approx 502.6548\text{ m}^3$.
- Surface Area: $A = 2\pi(4)(10) + 2\pi(4^2) = 80\pi + 32\pi = 112\pi \approx 351.8584\text{ m}^2$.

Volume Stack Trace:
| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:4}} | 0 | 0 | 0 | 4 |
| {{key:x²}} | 0 | 0 | 0 | 16 |
| {{key:π}} | 0 | 0 | 16 | 3.1415926 |
| {{key:×}} | 0 | 0 | 0 | 50.265482 |
| 10 | 0 | 0 | 50.265482 | 10 |
| {{key:×}} | 0 | 0 | 0 | 502.654824 |

Total Surface Area Stack Trace:
| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:2}} {{key:ENTER}} | 0 | 0 | 2 | 2 |
| {{key:π}} {{key:×}} | 0 | 0 | 0 | 6.2831853 |
| {{key:4}} {{key:×}} | 0 | 0 | 0 | 25.132741 |
| 10 {{key:×}} | 0 | 0 | 0 | 251.327412 |
| {{key:2}} {{key:ENTER}} | 0 | 251.327412 | 2 | 2 |
| {{key:π}} {{key:×}} | 0 | 251.327412 | 0 | 6.2831853 |
| {{key:4}} {{key:x²}} {{key:×}} | 0 | 251.327412 | 0 | 100.530964 |
| {{key:+}} | 0 | 0 | 0 | 351.858376 |

---

#### Example 2.4.2: Volume & Surface Area of a Right Cone ($r = 6\text{ cm}, h = 8\text{ cm}$)
Slant height: $s = \sqrt{r^2 + h^2} = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10\text{ cm}$.
- Volume: $V = \frac{1}{3}\pi (6^2) (8) = \frac{1}{3} \times 288\pi = 96\pi \approx 301.59289\text{ cm}^3$.
- Surface Area: $A = \pi r (r + s) = \pi (6) (6 + 10) = 96\pi \approx 301.59289\text{ cm}^2$.

Cone Volume Stack Trace:
| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:6}} {{key:x²}} | 0 | 0 | 0 | 36 |
| {{key:π}} {{key:×}} | 0 | 0 | 0 | 113.097336 |
| {{key:8}} {{key:×}} | 0 | 0 | 0 | 904.778684 |
| {{key:3}} {{key:÷}} | 0 | 0 | 0 | 301.592895 |

---

#### Example 2.4.3: Volume & Surface Area of a Sphere ($r = 9\text{ cm}$)
- Volume: $V = \frac{4}{3} \pi (9^3) = \frac{4}{3} \pi (729) = 972\pi \approx 3053.628\text{ cm}^3$.
- Surface Area: $A = 4\pi (9^2) = 4\pi (81) = 324\pi \approx 1017.876\text{ cm}^2$.

Sphere Volume Keystrokes:
- `{{key:4}} {{key:ENTER}} {{key:3}} {{key:÷}} {{key:π}} {{key:×}} {{key:9}} {{key:ENTER}} {{key:3}} {{key:yˣ}} {{key:×}}`.
- LCD Result: **$3053.628059\text{ cm}^3$**.

Sphere Surface Area Keystrokes:
- `{{key:9}} {{key:x²}} {{key:4}} {{key:×}} {{key:π}} {{key:×}}`.
- LCD Result: **$1017.876020\text{ cm}^2$**.

---

## Total Surface Area via Statistical Accumulator (`{{key:Σ+}}`)

For multi-faceted polyhedra (prisms, pyramids, and irregular engineering enclosures), calculating surface area face-by-face with scratch paper is prone to transcription errors. The SC-6 provides a zero-scratch-paper workflow using the statistical accumulator key `{{key:Σ+}}`.

<div class="admonition note">
<p class="admonition-title">Polyhedron Total Surface Area Accumulator Protocol</p>

| Step | Action | SC-6 Keystroke | Statistical State |
| :--- | :--- | :--- | :--- |
| **Step 1: Clear Memory** | Reset registers | {{key:CLΣ}} | $n = 0$ |
| **Step 2: Face Pair 1 ($L \times W$)** | Top & Bottom | `l {{key:ENTER}} w {{key:×}} 2 {{key:×}} {{key:Σ+}}` | Stored ($n = 1$) |
| **Step 3: Face Pair 2 ($L \times H$)** | Front & Back | `l {{key:ENTER}} h {{key:×}} 2 {{key:×}} {{key:Σ+}}` | Stored ($n = 2$) |
| **Step 4: Face Pair 3 ($W \times H$)** | Left & Right | `w {{key:ENTER}} h {{key:×}} 2 {{key:×}} {{key:Σ+}}` | Stored ($n = 3$) |
| **Step 5: Recall Total Area** | Sum all faces | `{{key:Σx}}` | Total Area on $X$ |
</div>

### Worked Prism Example ($l = 12\text{ cm}, w = 7\text{ cm}, h = 5\text{ cm}$)
- Face Pair 1 (Top & Bottom): $2 \times (12 \times 7) = 168\text{ cm}^2$.
- Face Pair 2 (Front & Back): $2 \times (12 \times 5) = 120\text{ cm}^2$.
- Face Pair 3 (Left & Right): $2 \times (7 \times 5) = 70\text{ cm}^2$.
- Total Surface Area: $168 + 120 + 70 = 358\text{ cm}^2$.

Keystroke Execution:
1. {{key:CLΣ}} $\to$ LCD confirms $n = 0$.
2. `12 {{key:ENTER}} {{key:7}} {{key:×}} {{key:2}} {{key:×}} {{key:Σ+}}` $\to$ LCD confirms $n = 1$.
3. `12 {{key:ENTER}} {{key:5}} {{key:×}} {{key:2}} {{key:×}} {{key:Σ+}}` $\to$ LCD confirms $n = 2$.
4. `{{key:7}} {{key:ENTER}} {{key:5}} {{key:×}} {{key:2}} {{key:×}} {{key:Σ+}}` $\to$ LCD confirms $n = 3$.
5. `{{key:Σx}}` $\to$ Result: **$358.00\text{ cm}^2$**.

---

### Worked Triangular Prism Example
A right triangular tent has triangular end faces with base $b = 6\text{ ft}$, height $h = 4\text{ ft}$, and hypotenuse legs $s = 5\text{ ft}$. The tent length is $L = 10\text{ ft}$.
- Two Triangular Ends: $2 \times \left(\frac{1}{2} \times 6 \times 4\right) = 24\text{ sq ft}$.
- Floor Face: $6 \times 10 = 60\text{ sq ft}$.
- Two Slanted Roof Faces: $2 \times (5 \times 10) = 100\text{ sq ft}$.
- Total Surface Area: $24 + 60 + 100 = 184\text{ sq ft}$.

Keystrokes:
1. {{key:CLΣ}} $\to n = 0$.
2. Ends: `{{key:6}} {{key:ENTER}} {{key:4}} {{key:×}} {{key:Σ+}}` $\to n = 1$ ($24$ stored).
3. Floor: `{{key:6}} {{key:ENTER}} 10 {{key:×}} {{key:Σ+}}` $\to n = 2$ ($60$ stored).
4. Roof: `{{key:5}} {{key:ENTER}} 10 {{key:×}} {{key:2}} {{key:×}} {{key:Σ+}}` $\to n = 3$ ($100$ stored).
5. Recall: `{{key:Σx}}` $\to$ Result: **$184.00\text{ sq ft}$**.

---

## Table 2: Complete Unit Conversions Directory

Unit conversions are expressed as exact rational ratios or internationally standardized conversion multipliers.

### Length Conversions

| From Unit | To Unit | Exact Multiplier | SC-6 Forward Keystrokes | Reverse Multiplier (To) |
|:---|:---|:---:|:---|:---:|
| **Inches (in)** | **Centimeters (cm)** | $2.54$ | `[in] {{key:ENTER}} 2.54 {{key:×}}` | $\div 2.54$ |
| **Feet (ft)** | **Inches (in)** | $12.0$ | `[ft] {{key:ENTER}} 12 {{key:×}}` | $\div 12$ |
| **Feet (ft)** | **Meters (m)** | $0.3048$ | `[ft] {{key:ENTER}} {{key:.}} 3048 {{key:×}}`| $\div 0.3048$ |
| **Yards (yd)** | **Feet (ft)** | $3.0$ | `[yd] {{key:ENTER}} {{key:3}} {{key:×}}` | $\div 3$ |
| **Yards (yd)** | **Meters (m)** | $0.9144$ | `[yd] {{key:ENTER}} {{key:.}} 9144 {{key:×}}`| $\div 0.9144$ |
| **Miles (mi)** | **Feet (ft)** | $5280.0$ | `[mi] {{key:ENTER}} 5280 {{key:×}}` | $\div 5280$ |
| **Miles (mi)** | **Kilometers (km)** | $1.609344$| `[mi] {{key:ENTER}} 1.609344 {{key:×}}`| $\div 1.609344$ |
| **Nautical Miles (NM)**| **Kilometers (km)**| $1.852$ | `[NM] {{key:ENTER}} 1.852 {{key:×}}` | $\div 1.852$ |
| **Nautical Miles (NM)**| **Statute Miles (mi)**| $\approx 1.150779$| `[NM] {{key:ENTER}} 1.1508 {{key:×}}`| $\div 1.1508$ |
| **Meters (m)** | **Centimeters (cm)** | $100.0$ | `[m] {{key:ENTER}} 100 {{key:×}}` | $\div 100$ |
| **Centimeters (cm)**| **Millimeters (mm)**| $10.0$ | `[cm] {{key:ENTER}} 10 {{key:×}}` | $\div 10$ |
| **Kilometers (km)**| **Meters (m)** | $1000.0$ | `[km] {{key:ENTER}} 1000 {{key:×}}` | $\div 1000$ |

#### Worked Length Conversion
Convert a $100\text{ yard}$ football field into meters:
- Keystrokes: `{{res:sc6_appendix_c_formulas_and_conversions_seq_01:keys}}`
- Result: **$91.44\text{ meters}$**.
- Reverse to check: `{{key:.}} 9144 {{key:÷}}`. Result: **$100.00\text{ yards}$**.

---

### Area Conversions

| From Unit | To Unit | Exact Multiplier | SC-6 Forward Keystrokes | Reverse Multiplier |
|:---|:---|:---:|:---|:---:|
| **Square Feet (sq ft)**| **Square Inches (sq in)**| $144.0$ | `[sq ft] {{key:ENTER}} 144 {{key:×}}` | $\div 144$ |
| **Square Yards (sq yd)**| **Square Feet (sq ft)**| $9.0$ | `[sq yd] {{key:ENTER}} {{key:9}} {{key:×}}` | $\div 9$ |
| **Acres (ac)** | **Square Feet (sq ft)**| $43,560.0$ | `[ac] {{key:ENTER}} 43560 {{key:×}}`| $\div 43560$ |
| **Acres (ac)** | **Hectares (ha)** | $\approx 0.4046856$| `[ac] {{key:ENTER}} {{key:.}} 4047 {{key:×}}`| $\div 0.4047$ |
| **Hectares (ha)** | **Square Meters ($m^2$)**| $10,000.0$ | `[ha] {{key:ENTER}} 10000 {{key:×}}`| $\div 10000$ |
| **Square Miles ($mi^2$)**| **Acres (ac)** | $640.0$ | `[sq mi] {{key:ENTER}} 640 {{key:×}}` | $\div 640$ |
| **Square Meters ($m^2$)**| **Square Feet (sq ft)**| $\approx 10.76391$ | `[m²] {{key:ENTER}} 10.764 {{key:×}}`| $\div 10.764$ |

#### Worked Area Conversion
How many square feet are in a $2.5\text{ acre}$ homestead parcel?
- Keystrokes: `{{res:sc6_appendix_c_formulas_and_conversions_seq_02:keys}}`
- Result: **$108,900\text{ sq ft}$**.

---

### Mass & Weight Conversions

| From Unit | To Unit | Exact Multiplier | SC-6 Forward Keystrokes | Reverse Multiplier (To) |
|:---|:---|:---:|:---|:---:|
| **Ounces (oz)** | **Grams (g)** | $28.349523$ | `[oz] {{key:ENTER}} 28.35 {{key:×}}` | $\div 28.3495$ |
| **Pounds (lb)** | **Ounces (oz)** | $16.0$ | `[lb] {{key:ENTER}} 16 {{key:×}}` | $\div 16$ |
| **Pounds (lb)** | **Kilograms (kg)** | $0.45359237$| `[lb] {{key:ENTER}} {{key:.}} 4536 {{key:×}}` | $\div 0.4536$ |
| **Kilograms (kg)** | **Pounds (lb)** | $\approx 2.2046226$| `[kg] {{key:ENTER}} 2.2046 {{key:×}}`| $\div 2.2046$ |
| **Tons (US Short)**| **Pounds (lb)** | $2000.0$ | `[ton] {{key:ENTER}} 2000 {{key:×}}` | $\div 2000$ |
| **Metric Tons (t)** | **Kilograms (kg)** | $1000.0$ | `[t] {{key:ENTER}} 1000 {{key:×}}` | $\div 1000$ |
| **Kilograms (kg)** | **Grams (g)** | $1000.0$ | `[kg] {{key:ENTER}} 1000 {{key:×}}` | $\div 1000$ |
| **Grams (g)** | **Milligrams (mg)** | $1000.0$ | `{{key:ENTER}} 1000 {{key:×}}` | $\div 1000$ |

#### Worked Weight Conversion
Convert a $65\text{ lb}$ bicycle packing crate into kilograms:
- Keystrokes: `{{res:sc6_appendix_c_formulas_and_conversions_seq_03:keys}}`
- Result: **$29.483\text{ kg}$**.

---

### Capacity & Liquid Volume Conversions

| From Unit | To Unit | Exact Multiplier | SC-6 Forward Keystrokes | Reverse Multiplier |
|:---|:---|:---:|:---|:---:|
| **Fluid Ounces (fl oz)** | **Milliliters (mL)** | $29.57352956$| `[fl oz] {{key:ENTER}} 29.57 {{key:×}}` | $\div 29.5735$ |
| **Cups (c)** | **Fluid Ounces (fl oz)**| $8.0$ | `[c] {{key:ENTER}} {{key:8}} {{key:×}}` | $\div 8$ |
| **Pints (pt)** | **Cups (c)** | $2.0$ | `[pt] {{key:ENTER}} {{key:2}} {{key:×}}` | $\div 2$ |
| **Quarts (qt)** | **Pints (pt)** | $2.0$ | `[qt] {{key:ENTER}} {{key:2}} {{key:×}}` | $\div 2$ |
| **Gallons (gal US)**| **Quarts (qt)** | $4.0$ | `[gal] {{key:ENTER}} {{key:4}} {{key:×}}` | $\div 4$ |
| **Gallons (gal US)**| **Liters (L)** | $3.785411784$ | `[gal] {{key:ENTER}} 3.7854 {{key:×}}`| $\div 3.7854$ |
| **Gallons (Imperial)**| **Liters (L)** | $4.54609$ | `[gal imp] {{key:ENTER}} 4.546 {{key:×}}`| $\div 4.5461$ |
| **Liters (L)** | **Milliliters (mL)** | $1000.0$ | `[L] {{key:ENTER}} 1000 {{key:×}}` | $\div 1000$ |
| **Cubic Meters ($m^3$)**| **Liters (L)** | $1000.0$ | `[m³] {{key:ENTER}} 1000 {{key:×}}` | $\div 1000$ |

#### Worked Liquid Volume Conversion
Convert a $15\text{ gallon}$ vehicle fuel tank into liters:
- Keystrokes: `{{res:sc6_appendix_c_formulas_and_conversions_seq_04:keys}}`
- Result: **$56.781\text{ liters}$**.

---

### Speed & Velocity Conversions

| From Unit | To Unit | Exact Multiplier | SC-6 Keystrokes |
|:---|:---|:---:|:---|
| **Miles per Hour (mph)**| **Kilometers per Hour (km/h)**| $1.609344$ | `[mph] {{key:ENTER}} 1.609 {{key:×}}` |
| **Miles per Hour (mph)**| **Feet per Second (ft/s)**| $\approx 1.466667$ | `[mph] {{key:ENTER}} 5280 {{key:×}} 3600 {{key:÷}}` |
| **Kilometers per Hour (km/h)**| **Meters per Second (m/s)**| $\approx 0.277778$| `[km/h] {{key:ENTER}} 1000 {{key:×}} 3600 {{key:÷}}` |
| **Knots (kt)** | **Miles per Hour (mph)**| $\approx 1.150779$ | `[kt] {{key:ENTER}} 1.151 {{key:×}}` |
| **Knots (kt)** | **Kilometers per Hour (km/h)**| $1.852$ | `[kt] {{key:ENTER}} 1.852 {{key:×}}` |

#### Worked Speed Conversion
A drone flies at $45\text{ mph}$. How fast is that in feet per second?
- Keystrokes: `{{res:sc6_appendix_c_formulas_and_conversions_seq_05:keys}}`
- Result: **$66.0\text{ ft/s}$**.

---

### Pressure Conversions

| From Unit | To Unit | Exact Multiplier | SC-6 Keystrokes |
|:---|:---|:---:|:---|
| **Atmospheres (atm)** | **Pounds per Sq Inch (psi)**| $14.6959488$ | `[atm] {{key:ENTER}} 14.696 {{key:×}}` |
| **Atmospheres (atm)** | **Kilopascals (kPa)** | $101.325$ | `[atm] {{key:ENTER}} 101.325 {{key:×}}` |
| **Bar (bar)** | **Kilopascals (kPa)** | $100.0$ | `[bar] {{key:ENTER}} 100 {{key:×}}` |
| **Pounds per Sq Inch (psi)**| **Kilopascals (kPa)**| $6.894757$ | `[psi] {{key:ENTER}} 6.895 {{key:×}}` |

#### Worked Pressure Conversion
Bicycle tire is inflated to $85\text{ psi}$. Convert to kilopascals:
- Keystrokes: `{{res:sc6_appendix_c_formulas_and_conversions_seq_06:keys}}`
- Result: **$586.05\text{ kPa}$**.

---

### Time Conversions

| From Unit | To Unit | Exact Multiplier | SC-6 Keystroke Sequence |
|:---|:---|:---:|:---|
| **Minutes (min)** | **Seconds (s)** | $60.0$ | `[min] {{key:ENTER}} 60 {{key:×}}` |
| **Hours (hr)** | **Minutes (min)** | $60.0$ | `[hr] {{key:ENTER}} 60 {{key:×}}` |
| **Hours (hr)** | **Seconds (s)** | $3600.0$ | `[hr] {{key:ENTER}} 3600 {{key:×}}` |
| **Days (d)** | **Hours (hr)** | $24.0$ | `d {{key:ENTER}} 24 {{key:×}}` |
| **Weeks (wk)** | **Days (d)** | $7.0$ | `[wk] {{key:ENTER}} {{key:7}} {{key:×}}` |
| **Years (yr standard)**| **Days (d)** | $365.0$ | `[yr] {{key:ENTER}} 365 {{key:×}}` |
| **Years (yr leap)**| **Days (d)** | $366.0$ | `[yr] {{key:ENTER}} 366 {{key:×}}` |

#### Worked Time Conversion
How many seconds are in one full 24-hour day?
- Keystrokes: `{{res:sc6_appendix_c_formulas_and_conversions_seq_07:keys}}`
- Result: **$86,400\text{ seconds}$**.

---

### Temperature Conversions ($F \leftrightarrow C \leftrightarrow K$)

Temperature conversions require affine transformations (scaling plus constant offsets):

$$C = (F - 32) \times \frac{5}{9} \qquad F = \left(C \times \frac{9}{5}\right) + 32 \qquad K = C + 273.15$$

<div class="admonition note">
<p class="admonition-title">Temperature Conversion RPN Protocols</p>

| Conversion | Formula | RPN Keystroke Protocol |
| :--- | :--- | :--- |
| **Fahrenheit to Celsius** | $C = (F - 32) \times \frac{5}{9}$ | `[F] {{key:ENTER}} 32 {{key:-}} {{key:5}} {{key:×}} {{key:9}} {{key:÷}}` |
| **Celsius to Fahrenheit** | $F = (C \times \frac{9}{5}) + 32$ | `{{key:C}} {{key:ENTER}} {{key:9}} {{key:×}} {{key:5}} {{key:÷}} 32 {{key:+}}` |
| **Celsius to Kelvin** | $K = C + 273.15$ | `{{key:C}} {{key:ENTER}} 273.15 {{key:+}}` |
| **Kelvin to Celsius** | $C = K - 273.15$ | `[K] {{key:ENTER}} 273.15 {{key:-}}` |
</div>

#### Worked Temperature Conversion Stack Trace: Normal Body Temp ($98.6^\circ\text{F} \to ^\circ\text{C}$)

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `98.6` | 0 | 0 | 0 | 98.6 |
| {{key:ENTER}} | 0 | 0 | 98.6 | 98.6 |
| 32 | 0 | 0 | 98.6 | 32 |
| {{key:-}} | 0 | 0 | 0 | 66.6 |
| {{key:5}} | 0 | 0 | 66.6 | 5 |
| {{key:×}} | 0 | 0 | 0 | 333.0 |
| {{key:9}} | 0 | 0 | 333.0 | 9 |
| {{key:÷}} | 0 | 0 | 0 | 37.0 |
Result: Normal human body temperature is exactly **$37.0^\circ\text{C}$** (or on the SC-6 keypad, `98.6 {{key:▸°C}}` $\to$ `37.00`).

---

### Deep-Dive Multimodal Unit Conversion Stack Traces

#### Example 4.9.1: Marathon Footrace Distance ($26.2\text{ miles} \to \text{kilometers} \to \text{meters}$)
Exact international definition: $1\text{ statute mile} = 1.609344\text{ kilometers} = 1,609.344\text{ meters}$.
$$\text{Distance in km} = 26.2 \times 1.609344 \approx 42.1648128\text{ km}$$

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:2}}{{key:6}}{{key:.}}{{key:2}} | 0 | 0 | 0 | 26.2 |
| {{key:ENTER}} | 0 | 0 | 26.2 | 26.2 |
| `1.609344` | 0 | 0 | 26.2 | 1.609344 |
| {{key:×}} | 0 | 0 | 0 | 42.164813 |
| 1000 | 0 | 0 | 42.164813 | 1000 |
| {{key:×}} | 0 | 0 | 0 | 42164.81280 |
*Stack Inspection:* Register $X$ now holds the exact Olympic marathon distance: **$42,164.81\text{ meters}$**.

---

#### Example 4.9.2: Commercial Jet Cruising Altitude ($36,000\text{ ft} \to \text{meters} \to \text{kilometers}$)
Conversion factor: $1\text{ foot} = 0.3048\text{ meters}$ exact.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `36000` | 0 | 0 | 0 | 36000 |
| {{key:ENTER}} | 0 | 0 | 36000 | 36000 |
| `.3048` | 0 | 0 | 36000 | 0.3048 |
| {{key:×}} | 0 | 0 | 0 | 10972.8 |
| 1000 | 0 | 0 | 10972.8 | 1000 |
| {{key:÷}} | 0 | 0 | 0 | 10.9728 |
Cruising altitude: **$10,972.8\text{ meters}$** or **$10.97\text{ km}$** (stratosphere).

---

#### Example 4.9.3: Automobile Fuel Economy ($35.0\text{ MPG (US)} \leftrightarrow \text{Liters per 100 km}$)
The international automotive conversion constant is:
$$\text{L/100km} = \frac{235.215}{\text{MPG}}$$

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `235.215` | 0 | 0 | 0 | 235.215 |
| {{key:ENTER}} | 0 | 0 | 235.215 | 235.215 |
| 35 | 0 | 0 | 235.215 | 35 |
| {{key:÷}} | 0 | 0 | 0 | 6.720429 |
A vehicle rated at $35\text{ MPG}$ consumes **$6.72\text{ liters of gasoline per 100 kilometers}$**.

---

#### Example 4.9.4: Absolute Zero Verification ($-459.67^\circ\text{F} \to ^\circ\text{C} \to \text{Kelvin}$)
Absolute zero in Fahrenheit is $-459.67^\circ\text{F}$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `459.67` {{key:+/-}} | 0 | 0 | 0 | -459.67 |
| {{key:ENTER}} | 0 | 0 | -459.67 | -459.67 |
| 32 | 0 | 0 | -459.67 | 32 |
| {{key:-}} | 0 | 0 | 0 | -491.67 |
| {{key:5}} | 0 | 0 | -491.67 | 5 |
| {{key:×}} | 0 | 0 | 0 | -2458.35 |
| {{key:9}} | 0 | 0 | -2458.35 | 9 |
| {{key:÷}} | 0 | 0 | 0 | -273.15 |
| `273.15` | 0 | 0 | -273.15 | 273.15 |
| {{key:+}} | 0 | 0 | 0 | 0.00 |
Result: Exactly **$-273.15^\circ\text{C}$** and **$0.00\text{ K}$** (absolute zero).

---


## Table 3: Prime Number Catalog & Factorization Directory

A prime number is an integer greater than 1 whose only positive divisors are 1 and itself. Composite numbers can be uniquely factored into products of primes (Fundamental Theorem of Arithmetic).

### Complete Catalog of All 46 Prime Numbers Under 200

There are exactly **46 prime numbers** strictly less than 200. The table below details each prime, its sequential prime index $p_n$, binary/hex representation, twin prime pairing status, and mathematical properties:

| Index ($n$) | Prime ($p_n$) | Binary ($2$) | Hex ($16$) | Twin Status | Mathematical Properties |
|:---:|:---:|:---:|:---:|:---|:---|
| $p_1$ | **2** | `10` | `0x02` | Sole Even Prime | Only even prime; smallest prime; foundational binary radix. |
| $p_2$ | **3** | `11` | `0x03` | Twin with 5 | Smallest odd prime; first Mersenne prime ($2^2 - 1$). |
| $p_3$ | **5** | `101` | `0x05` | Twin with 3, 7 | Only prime in two twin pairs ($3,5$ and $5,7$); Fermat prime ($2^2 + 1$). |
| $p_4$ | **7** | `111` | `0x07` | Twin with 5 | Second Mersenne prime ($2^3 - 1$); Mersenne exponent. |
| $p_5$ | **11** | `1011` | `0x0B` | Twin with 13 | Smallest two-digit prime; palindromic prime; Sophie Germain ($2 \times 11 + 1 = 23$). |
| $p_6$ | **13** | `1101` | `0x0D` | Twin with 11 | Wilson prime; reversal is 31 (emirp); star number. |
| $p_7$ | **17** | `10001` | `0x11` | Twin with 19 | Fermat prime ($2^4 + 1$); constructible regular 17-gon; sum of first 4 primes. |
| $p_8$ | **19** | `10011` | `0x13` | Twin with 17 | Keith number; centered triangular number; safe prime. |
| $p_9$ | **23** | `10111` | `0x17` | Isolated | Safe prime ($2 \times 11 + 1$); smallest prime requiring 9 cubes. |
| $p_{10}$ | **29** | `11101` | `0x1D` | Twin with 31 | Sum of three consecutive squares ($2^2 + 3^2 + 4^2$); Sophie Germain. |
| $p_{11}$ | **31** | `11111` | `0x1F` | Twin with 29 | Third Mersenne prime ($2^5 - 1$); repunit in base 2. |
| $p_{12}$ | **37** | `100101` | `0x25` | Isolated | Palindromic in octal ($45_8$); emirp with 73; regular prime. |
| $p_{13}$ | **41** | `101001` | `0x29` | Twin with 43 | Generates primes via Euler's polynomial $n^2 + n + 41$; Sophie Germain. |
| $p_{14}$ | **43** | `101011` | `0x2B` | Twin with 41 | Star number; centered heptagonal number. |
| $p_{15}$ | **47** | `101111` | `0x2F` | Isolated | Lucas number $L_8$; safe prime ($47 = 2 \times 23 + 1$). |
| $p_{16}$ | **53** | `110101` | `0x35` | Isolated | Sophie Germain prime ($2 \times 53 + 1 = 107$, which is prime). |
| $p_{17}$ | **59** | `111011` | `0x3B` | Twin with 61 | Regular prime; sum of three consecutive primes ($17 + 19 + 23$). |
| $p_{18}$ | **61** | `111101` | `0x3D` | Twin with 59 | Emirp with 16; cuban prime ($x=5, y=4 \to 5^3 - 4^3 = 61$). |
| $p_{19}$ | **67** | `1000011`| `0x43` | Isolated | Sum of five consecutive primes ($7 + 11 + 13 + 17 + 19$). |
| $p_{20}$ | **71** | `1000111`| `0x47` | Twin with 73 | Largest prime dividing the order of the Monster group. |
| $p_{21}$ | **73** | `1001001`| `0x49` | Twin with 71 | Sheldon prime (21st prime; reversed index 12 is prime 37; binary $1001001_2$ palindrome). |
| $p_{22}$ | **79** | `1001111`| `0x4F` | Isolated | Emirp with 97; sum of first four prime powers. |
| $p_{23}$ | **83** | `1010011`| `0x53` | Isolated | Sophie Germain prime ($2 \times 83 + 1 = 167$). |
| $p_{24}$ | **89** | `1011001`| `0x59` | Isolated | Fibonacci prime $F_{11}$; Mersenne prime exponent ($2^{89}-1$). |
| $p_{25}$ | **97** | `1100001`| `0x61` | Isolated | Largest two-digit prime; emirp with 79. |
| $p_{26}$ | **101** | `1100101`| `0x65` | Twin with 103 | Smallest three-digit prime; palindromic prime. |
| $p_{27}$ | **103** | `1100111`| `0x67` | Twin with 101 | Twin prime partner of 101. |
| $p_{28}$ | **107** | `1101011`| `0x6B` | Twin with 109 | Fourth Mersenne prime exponent ($2^{107}-1$). |
| $p_{29}$ | **109** | `1101101`| `0x6D` | Twin with 107 | Twin prime partner of 107; centered triangular number. |
| $p_{30}$ | **113** | `1110001`| `0x71` | Isolated | Permutable prime ($113, 131, 311$ are all prime); Sophie Germain ($2 \times 113 + 1 = 227$). |
| $p_{31}$ | **127** | `1111111`| `0x7F` | Isolated | Fifth Mersenne prime ($2^7 - 1 = 127$); binary repunit $1111111_2$. |
| $p_{32}$ | **131** | `10000011`| `0x83` | Isolated | Palindromic prime; permutable prime with 113; Sophie Germain. |
| $p_{33}$ | **137** | `10001001`| `0x89` | Twin with 139 | Close approximation to fine structure constant reciprocal ($\approx 137.036$). |
| $p_{34}$ | **139** | `10001011`| `0x8B` | Twin with 137 | Twin prime partner of 137. |
| $p_{35}$ | **149** | `10010101`| `0x95` | Twin with 151 | Strong prime; emirp. |
| $p_{36}$ | **151** | `10010111`| `0x97` | Twin with 149 | Palindromic prime; lucky prime. |
| $p_{37}$ | **157** | `10011101`| `0x9D` | Isolated | Balanced prime (halfway between 151 and 163). |
| $p_{38}$ | **163** | `10100011`| `0xA3` | Isolated | Heegner number; $e^{\pi\sqrt{163}}$ is an "almost integer". |
| $p_{39}$ | **167** | `10100111`| `0xA7` | Isolated | Safe prime of 83; Eisenstein prime. |
| $p_{40}$ | **173** | `10101101`| `0xAD` | Isolated | Sum of two squares ($2^2 + 13^2 = 4 + 169 = 173$). |
| $p_{41}$ | **179** | `10110011`| `0xB3` | Twin with 181 | Sophie Germain prime ($2 \times 179 + 1 = 359$). |
| $p_{42}$ | **181** | `10110101`| `0xB5` | Twin with 179 | Palindromic prime; strobogrammatic prime (reads same upside down). |
| $p_{43}$ | **191** | `10111111`| `0xBF` | Twin with 193 | Palindromic prime; Sophie Germain prime ($2 \times 191 + 1 = 383$). |
| $p_{44}$ | **193** | `11000001`| `0xC1` | Twin with 191 | Pierpont prime ($2^6 \times 3 + 1 = 193$). |
| $p_{45}$ | **197** | `11000101`| `0xC5` | Twin with 199 | Twin prime partner of 199; sum of first 12 primes. |
| $p_{46}$ | **199** | `11000111`| `0xC7` | Twin with 197 | Largest prime under 200; Lucas number $L_{11}$. |

---

### Algorithmic Divisibility Tests with RPN Verification

Before testing large integers with `{{key:PRIME}}`, mental mathletes and students use rapid divisibility rules:

| Divisor | Mental Math Criterion | SC-6 RPN Verification Procedure | Worked Example |
|:---:|:---|:---|:---|
| **2** | Last digit is even ($0, 2, 4, 6, 8$). | `{{key:N}} {{key:ENTER}} {{key:2}} {{key:÷R}} {{key:x⇄y}}` $\to 0$ | $84 \div 2 \to R = 0$ (Even) |
| **3** | Sum of digits is divisible by 3. | `[d1] {{key:ENTER}} [d2] {{key:+}} ... {{key:3}} {{key:÷R}}` | $153 \to 1+5+3=9 \div 3 \to R = 0$ |
| **4** | Last two digits form number divisible by 4. | `[last2] {{key:ENTER}} {{key:4}} {{key:÷R}} {{key:x⇄y}}` $\to 0$ | $3,728 \to 28 \div 4 \to R = 0$ |
| **5** | Last digit is 0 or 5. | Inspect last digit on LCD display. | $95 \to$ Ends in 5 (Div by 5) |
| **6** | Divisible by both 2 and 3. | Test 2 (even) and test 3 (digit sum). | $78 \to$ Even, and $7+8=15$ (Div by 6) |
| **7** | Double last digit, subtract from remaining part. | `[rem] {{key:ENTER}} [last] {{key:2}} {{key:×}} {{key:-}} {{key:7}} {{keycap:÷R}}` | $203 \to 20 - (2 \times 3) = 14$ (Div by 7) |
| **8** | Last three digits form number divisible by 8. | `[last3] {{key:ENTER}} {{key:8}} {{key:÷R}} {{key:x⇄y}}` $\to 0$ | $5,128 \to 128 \div 8 = 16, R = 0$ |
| **9** | Sum of digits is divisible by 9. | `[d1] {{key:ENTER}} [d2] {{key:+}} ... {{key:9}} {{key:÷R}}` | $423 \to 4+2+3=9 \div 9 \to R = 0$ |
| **10** | Last digit is 0. | Inspect Register $X$ display. | $340 \to$ Ends in 0 |
| **11** | Alternating sum of digits is multiple of 11. | `[d1] {{key:ENTER}} [d2] {{key:-}} [d3] {{key:+}} ...` | $913 \to 9 - 1 + 3 = 11$ (Div by 11) |
| **13** | Add 4 times last digit to remaining part. | `[rem] {{key:ENTER}} [last] {{key:4}} {{key:×}} {{key:+}} `13` {{keycap:÷R}}`| $299 \to 29 + (4 \times 9) = 65 = 5 \times 13$ |

---

### Ten Classic Canonical Prime Factorizations

The Fundamental Theorem of Arithmetic guarantees that every integer $N > 1$ decomposes uniquely into primes:

$$N = p_1^{e_1} \times p_2^{e_2} \times \dots \times p_k^{e_k}$$

The table below shows 10 foundational composite numbers, their canonical prime factorization, and their RPN reconstruction verification sequences:

| Composite Number ($N$) | Canonical Factorization | SC-6 Hardware {{key:FACT}} LCD Output | RPN Reconstruction Keystroke Sequence |
|:---:|:---:|:---|:---|
| **72** | $2^3 \times 3^2$ | `2^3 * 3^2` | `{{key:2}} {{key:ENTER}} {{key:3}} {{keycap:yˣ}} {{key:3}} {{key:x²}} {{key:×}}` $\to 72$ |
| **84** | $2^2 \times 3 \times 7$ | `2^2 * 3 * 7` | `{{key:2}} {{key:x²}} {{key:3}} {{key:×}} {{key:7}} {{key:×}}` $\to 84$ |
| **180** | $2^2 \times 3^2 \times 5$ | `2^2 * 3^2 * 5` | `{{key:2}} {{key:x²}} {{key:3}} {{key:x²}} {{key:×}} {{key:5}} {{key:×}}` $\to 180$ |
| **252** | $2^2 \times 3^2 \times 7$ | `2^2 * 3^2 * 7` | `{{key:2}} {{key:x²}} {{key:3}} {{key:x²}} {{key:×}} {{key:7}} {{key:×}}` $\to 252$ |
| **360** | $2^3 \times 3^2 \times 5$ | `2^3 * 3^2 * 5` | `{{key:2}} {{key:ENTER}} {{key:3}} {{keycap:yˣ}} {{key:3}} {{key:x²}} {{key:×}} {{key:5}} {{key:×}}` $\to 360$ |
| **504** | $2^3 \times 3^2 \times 7$ | `2^3 * 3^2 * 7` | `{{key:2}} {{key:ENTER}} {{key:3}} {{keycap:yˣ}} {{key:3}} {{key:x²}} {{key:×}} {{key:7}} {{key:×}}` $\to 504$ |
| **720** | $2^4 \times 3^2 \times 5$ | `2^4 * 3^2 * 5` | `{{key:2}} {{key:ENTER}} {{key:4}} {{keycap:yˣ}} {{key:3}} {{key:x²}} {{key:×}} {{key:5}} {{key:×}}` $\to 720$ |
| **1,000** | $2^3 \times 5^3$ | `2^3 * 5^3` | `{{key:2}} {{key:ENTER}} {{key:3}} {{keycap:yˣ}} {{key:5}} {{key:ENTER}} {{key:3}} {{keycap:yˣ}} {{key:×}}` $\to 1000$ |
| **1,024** | $2^{10}$ | `2^10` | `{{key:2}} {{key:ENTER}} 10 {{keycap:yˣ}}` $\to 1024$ |
| **1,729** | $7 \times 13 \times 19$ | `7 * 13 * 19` | `{{key:7}} {{key:ENTER}} 13 {{key:×}} 19 {{key:×}}` $\to 1729$ |

*Note on 1,729 (Hardy-Ramanujan Taxicab Number):* It is the smallest integer expressible as the sum of two positive cubes in two different ways:
$$1729 = 1^3 + 12^3 = 9^3 + 10^3$$
Verify on SC-6:
- Pair 1: `{{key:1}} {{key:ENTER}} {{key:3}} {{keycap:yˣ}} 12 {{key:ENTER}} {{key:3}} {{keycap:yˣ}} {{key:+}}` $\to 1 + 1728 = 1729$.
- Pair 2: `{{key:9}} {{key:ENTER}} {{key:3}} {{keycap:yˣ}} 10 {{key:ENTER}} {{key:3}} {{keycap:yˣ}} {{key:+}}` $\to 729 + 1000 = 1729$.

---

### Euclidean Algorithm Master Reference Table

The table below catalogs 10 number pairs, their step-by-step Euclidean quotient and remainder sequences, and their calculated $\text{GCF}$ and $\text{LCM}$:

| Number Pair ($a, b$) | Euclidean Division Steps | $\text{GCF}(a,b)$ | Product $a \times b$ | $\text{LCM} = \frac{a \times b}{\text{GCF}}$ |
|:---:|:---|:---:|:---:|:---:|
| **$(24, 18)$** | $24 = 1(18) + 6$; $18 = 3(6) + 0$ | **6** | 432 | **72** |
| **$(36, 24)$** | $36 = 1(24) + 12$; $24 = 2(12) + 0$ | **12** | 864 | **72** |
| **$(60, 42)$** | $60 = 1(42) + 18$; $42 = 2(18) + 6$; $18 = 3(6) + 0$ | **6** | 2,520 | **420** |
| **$(84, 36)$** | $84 = 2(36) + 12$; $36 = 3(12) + 0$ | **12** | 3,024 | **252** |
| **$(105, 45)$**| $105 = 2(45) + 15$; $45 = 3(15) + 0$ | **15** | 4,725 | **315** |
| **$(120, 75)$**| $120 = 1(75) + 45$; $75 = 1(45) + 30$; $45 = 1(30) + 15$; $30 = 2(15) + 0$ | **15** | 9,000 | **600** |
| **$(144, 96)$**| $144 = 1(96) + 48$; $96 = 2(48) + 0$ | **48** | 13,824 | **288** |
| **$(210, 165)$**| $210 = 1(165) + 45$; $165 = 3(45) + 30$; $45 = 1(30) + 15$; $30 = 2(15) + 0$| **15** | 34,650 | **2,310** |
| **$(252, 105)$**| $252 = 2(105) + 42$; $105 = 2(42) + 21$; $42 = 2(21) + 0$ | **21** | 26,460 | **1,260** |
---

### Goldbach's Conjecture Verification Matrix (Evens 4 to 60)

Goldbach's Conjecture (posed by Christian Goldbach to Leonhard Euler in 1742) asserts that every even integer greater than 2 can be expressed as the sum of two prime numbers:

$$2n = p_a + p_b \qquad (p_a, p_b \in \mathbb{P})$$

Elementary students can verify Goldbach partitions on the SC-6 by entering the prime pair into the stack and testing both components with {{key:PRIME}}:

| Even Number ($2n$) | Canonical Prime Pair ($p_a + p_b$) | Alternative Partitions | SC-6 RPN Verification Keystrokes |
|:---:|:---:|:---|:---|
| **4** | $2 + 2$ | Unique | `{{key:2}} {{key:ENTER}} {{key:2}} {{key:+}}` $\to 4$ |
| **6** | $3 + 3$ | Unique | `{{key:3}} {{key:ENTER}} {{key:3}} {{key:+}}` $\to 6$ |
| **8** | $3 + 5$ | Unique | `{{key:3}} {{key:ENTER}} {{key:5}} {{key:+}}` $\to 8$ |
| **10** | $3 + 7$ | $5 + 5$ | `{{key:3}} {{key:ENTER}} {{key:7}} {{key:+}}` $\to 10$ |
| **12** | $5 + 7$ | Unique | `{{key:5}} {{key:ENTER}} {{key:7}} {{key:+}}` $\to 12$ |
| **14** | $3 + 11$ | $7 + 7$ | `{{key:3}} {{key:ENTER}} 11 {{key:+}}` $\to 14$ |
| **16** | $3 + 13$ | $5 + 11$ | `{{key:3}} {{key:ENTER}} 13 {{key:+}}` $\to 16$ |
| **18** | $5 + 13$ | $7 + 11$ | `{{key:5}} {{key:ENTER}} 13 {{key:+}}` $\to 18$ |
| **20** | $3 + 17$ | $7 + 13$ | `{{key:3}} {{key:ENTER}} 17 {{key:+}}` $\to 20$ |
| **22** | $3 + 19$ | $5 + 17, 11 + 11$ | `{{key:3}} {{key:ENTER}} 19 {{key:+}}` $\to 22$ |
| **24** | $5 + 19$ | $7 + 17, 11 + 13$ | `{{key:5}} {{key:ENTER}} 19 {{key:+}}` $\to 24$ |
| **26** | $3 + 23$ | $7 + 19, 13 + 13$ | `{{key:3}} {{key:ENTER}} 23 {{key:+}}` $\to 26$ |
| **28** | $5 + 23$ | $11 + 17$ | `{{key:5}} {{key:ENTER}} 23 {{key:+}}` $\to 28$ |
| **30** | $7 + 23$ | $11 + 19, 13 + 17$ | `{{key:7}} {{key:ENTER}} 23 {{key:+}}` $\to 30$ |
| **32** | $3 + 29$ | $13 + 19$ | `{{key:3}} {{key:ENTER}} 29 {{key:+}}` $\to 32$ |
| **34** | $3 + 31$ | $5 + 29, 11 + 23, 17 + 17$ | `{{key:3}} {{key:ENTER}} 31 {{key:+}}` $\to 34$ |
| **36** | $5 + 31$ | $7 + 29, 13 + 23, 17 + 19$ | `{{key:5}} {{key:ENTER}} 31 {{key:+}}` $\to 36$ |
| **38** | $3 + 35$ (No, 35 comp); $7 + 31$ | $19 + 19$ | `{{key:7}} {{key:ENTER}} 31 {{key:+}}` $\to 38$ |
| **40** | $3 + 37$ | $11 + 29, 17 + 23$ | `{{key:3}} {{key:ENTER}} 37 {{key:+}}` $\to 40$ |
| **42** | $5 + 37$ | $11 + 31, 13 + 29, 19 + 23$ | `{{key:5}} {{key:ENTER}} 37 {{key:+}}` $\to 42$ |
| **44** | $3 + 41$ | $7 + 37, 13 + 31$ | `{{key:3}} {{key:ENTER}} 41 {{key:+}}` $\to 44$ |
| **46** | $3 + 43$ | $5 + 41, 17 + 29, 23 + 23$ | `{{key:3}} {{key:ENTER}} 43 {{key:+}}` $\to 46$ |
| **48** | $5 + 43$ | $7 + 41, 11 + 37, 17 + 31, 19 + 29$ | `{{key:5}} {{key:ENTER}} 43 {{key:+}}` $\to 48$ |
| **50** | $3 + 47$ | $7 + 43, 13 + 37, 19 + 31$ | `{{key:3}} {{key:ENTER}} 47 {{key:+}}` $\to 50$ |
| **52** | $5 + 47$ | $11 + 41, 23 + 29$ | `{{key:5}} {{key:ENTER}} 47 {{key:+}}` $\to 52$ |
| **54** | $7 + 47$ | $11 + 43, 13 + 41, 17 + 37, 23 + 31$ | `{{key:7}} {{key:ENTER}} 47 {{key:+}}` $\to 54$ |
| **56** | $3 + 53$ | $13 + 43, 19 + 37$ | `{{key:3}} {{key:ENTER}} 53 {{key:+}}` $\to 56$ |
| **58** | $5 + 53$ | $11 + 47, 17 + 41, 29 + 29$ | `{{key:5}} {{key:ENTER}} 53 {{key:+}}` $\to 58$ |
| **60** | $7 + 53$ | $13 + 47, 17 + 43, 19 + 41, 23 + 37, 29 + 31$ | `{{key:7}} {{key:ENTER}} 53 {{key:+}}` $\to 60$ |

---

### Mersenne Primes & Euclid-Euler Perfect Numbers

A **Mersenne prime** is a prime number of the form $M_p = 2^p - 1$ where the exponent $p$ is itself prime. Euclid (Book IX, Proposition 36) proved that whenever $2^p - 1$ is prime, the number:

$$N = 2^{p-1} \left(2^p - 1\right)$$

is an **even perfect number** (equal to the exact sum of its proper positive divisors). Euler later proved that *all* even perfect numbers must follow this exact formula.

The table below catalogs the first four Mersenne primes and their associated perfect numbers:

| Prime Exponent ($p$) | Mersenne Prime ($M_p = 2^p - 1$) | Perfect Number Formula | Evaluated Perfect Number ($N$) | Proper Divisors Sum Check |
|:---:|:---:|:---|:---:|:---|
| **$p = 2$** | $2^2 - 1 = \mathbf{3}$ | $2^1 \times 3$ | **6** | $1 + 2 + 3 = 6$ |
| **$p = 3$** | $2^3 - 1 = \mathbf{7}$ | $2^2 \times 7$ | **28** | $1 + 2 + 4 + 7 + 14 = 28$ |
| **$p = 5$** | $2^5 - 1 = \mathbf{31}$ | $2^4 \times 31$ | **496** | $1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 = 496$ |
| **$p = 7$** | $2^7 - 1 = \mathbf{127}$ | $2^6 \times 127$ | **8,128** | $1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + \dots = 8128$ |

#### Worked Stack Trace: Computing Third Perfect Number ($N = 496$)
Formula: $N = 2^{5-1} \times (2^5 - 1) = 16 \times 31 = 496$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:2}} {{key:ENTER}} | 0 | 0 | 2 | 2 |
| {{key:5}} {{keycap:yˣ}} | 0 | 0 | 0 | 32 |
| {{key:1}} {{key:-}} | 0 | 0 | 0 | 31 |
| {{key:PRIME}} | 0 | 0 | 0 | 31 IS PRIME |
| {{key:2}} {{key:ENTER}} | 0 | 31 | 2 | 2 |
| {{key:4}} {{keycap:yˣ}} | 0 | 31 | 0 | 16 |
| {{key:×}} | 0 | 0 | 0 | 496 |
Result: **$496$** confirmed prime-constructed perfect integer.

---

### Fermat Primes & Gauss Constructible Regular Polygons

A **Fermat number** has the form $F_n = 2^{2^n} + 1$. When $F_n$ is prime, it is called a Fermat prime. Carl Friedrich Gauss proved in 1796 (at age 19) that a regular polygon of $N$ sides can be constructed with straightedge and compass if and only if $N$ is the product of a power of 2 and any number of distinct Fermat primes:

$$N = 2^k \times F_{a} \times F_{b} \times \dots$$

There are only **five known Fermat primes** in mathematics:

| Index ($n$) | Expression ($2^{2^n} + 1$) | Fermat Prime ($F_n$) | Constructible Regular Polygons |
|:---:|:---|:---:|:---|
| **$n = 0$** | $2^{2^0} + 1 = 2^1 + 1$ | **3** | Equilateral Triangle ($N = 3$) |
| **$n = 1$** | $2^{2^1} + 1 = 2^2 + 1$ | **5** | Regular Pentagon ($N = 5$) |
| **$n = 2$** | $2^{2^2} + 1 = 2^4 + 1$ | **17** | Regular Heptadecagon ($N = 17$, Gauss's discovery) |
| **$n = 3$** | $2^{2^3} + 1 = 2^8 + 1$ | **257** | Regular 257-gon ($N = 257$) |
| **$n = 4$** | $2^{2^4} + 1 = 2^{16} + 1$| **65,537** | Regular 65,537-gon ($N = 65,537$) |

*Note on $F_5$ (Euler's Famous Counterexample):*
Pierre de Fermat conjectured that all $F_n$ are prime. In 1732, Leonhard Euler disproved this by factoring $F_5$:
$$F_5 = 2^{32} + 1 = 4,294,967,297 = 641 \times 6,700,417$$
Verify factor on SC-6:
- Keystrokes: `{{res:sc6_appendix_c_formulas_and_conversions_seq_08:keys}}`
- LCD Result: Exactly **$6,700,417.00$** (composite!).

---

## Comprehensive Formula Quick-Reference Index Matrix

### Geometric & Physical Quick Matrix


| Mathematical Problem | Known Inputs | Target Output | RPN Key Sequence Template |
|:---|:---|:---|:---|
| **Area of Circle** | Radius $r$ | Area $A$ | `r {{key:x²}} {{key:π}} {{key:×}}` |
| **Circumference of Circle** | Diameter $d$ | Circumference $C$ | `d {{key:π}} {{key:×}}` |
| **Hypotenuse of Right Triangle**| Legs $a, b$ | Hypotenuse $c$ | `a {{key:x²}} b {{key:x²}} {{key:+}} {{keycap:√x}}` |
| **Area of Triangle** | Base $b$, Height $h$ | Area $A$ | `b {{key:ENTER}} h {{key:×}} {{key:2}} {{key:÷}}` |
| **Area of Trapezoid** | Bases $a, b$, Height $h$| Area $A$ | `a {{key:ENTER}} b {{key:+}} {{key:2}} {{key:÷}} h {{key:×}}` |
| **Volume of Cylinder** | Radius $r$, Height $h$ | Volume $V$ | `r {{key:x²}} {{key:π}} {{key:×}} h {{key:×}}` |
| **Volume of Cone** | Radius $r$, Height $h$ | Volume $V$ | `r {{key:x²}} {{key:π}} {{key:×}} h {{key:×}} {{key:3}} {{key:÷}}` |
| **Volume of Sphere** | Radius $r$ | Volume $V$ | `{{key:4}} {{key:ENTER}} {{key:3}} {{key:÷}} {{key:π}} {{key:×}} `r` {{key:3}} {{keycap:yˣ}} {{key:×}}` |
| **Volume of Rectangular Box** | Length $l$, Width $w$, Height $h$| Volume $V$ | `l {{key:ENTER}} w {{key:×}} h {{key:×}}` |
| **Surface Area of Cube** | Side $s$ | Surface Area $A$| `s {{key:x²}} {{key:6}} {{key:×}}` |
| **Percent of a Number** | Whole $W$, Rate $r\%$ | Part $P$ | `[W] {{key:ENTER}} `r` {{key:%}}` |
| **Percent Increase / Decrease**| Old $O$, New $N$ | Change $\% \Delta$ | `[O] {{key:ENTER}} {{key:N}} [Δ%]` |
| **Fahrenheit to Celsius** | Temp $F$ | Temp $C$ | `[F] {{key:ENTER}} 32 {{key:-}} {{key:5}} {{key:×}} {{key:9}} {{key:÷}}` |
| **Celsius to Fahrenheit** | Temp $C$ | Temp $F$ | `{{key:C}} {{key:ENTER}} {{key:9}} {{key:×}} {{key:5}} {{key:÷}} 32 {{key:+}}` |
| **Speed / Rate** | Distance $d$, Time $t$ | Speed $s$ | `d {{key:ENTER}} [t] {{key:÷}}` |
| **Unit Price** | Cost $C$, Quantity $Q$ | Price per unit | `{{key:C}} {{key:ENTER}} [Q] {{key:÷}}` |
| **Miles to Kilometers** | Distance $mi$ | Distance $km$ | `[mi] {{key:ENTER}} 1.609344 {{key:×}}` |
| **Pounds to Kilograms** | Weight $lb$ | Mass $kg$ | `[lb] {{key:ENTER}} {{key:.}} 453592 {{key:×}}` |
| **Gallons to Liters** | Volume $gal$ | Volume $L$ | `[gal] {{key:ENTER}} 3.7854 {{key:×}}` |

---

### Elementary Financial Mathematics Protocols

Everyday consumer mathematics problems (interest, taxes, tips, unit cost comparisons) map directly onto the SC-6 stack:

| Financial Operation | Mathematical Formula | SC-6 RPN Execution Template |
|:---|:---|:---|
| **Simple Interest ($I$)** | $I = P \times r \times t$ | `[P] {{key:ENTER}} `r` {{key:%}} [t] {{key:×}}` |
| **Total Amount ($A$)** | $A = P + I = P(1 + rt)$ | `[P] {{key:ENTER}} `r` {{key:%}} [t] {{key:×}} {{key:+}}` |
| **Sales Tax ($T$)** | $T = P \times r$ | `[P] {{key:ENTER}} `r` {{key:%}}` |
| **Total with Tax** | $Total = P \times (1 + r)$ | `[P] {{key:ENTER}} `r` {{key:%}} {{key:+}}` |
| **Discount Amount ($D$)** | $D = P \times d$ | `[P] {{key:ENTER}} `d` {{key:%}}` |
| **Sale Price** | $Sale = P \times (1 - d)$ | `[P] {{key:ENTER}} `d` {{key:%}} {{key:-}}` |
| **Restaurant Tip ($18\%$)**| $Tip = Bill \times 0.18$ | `[Bill] {{key:ENTER}} 18 {{key:%}}` |
| **Compound Interest ($A$)**| $A = P(1 + r)^t$ (annual) | `{{key:1}} {{key:ENTER}} `r` {{key:+}} [t] {{keycap:yˣ}} [P] {{key:×}}` |

#### Worked Financial Stack Trace: 3-Year Certificate of Deposit ($P = 500\text{ USD}, r = 4\%, t = 3\text{ years}$)
Formula: $A = 500 \times (1 + 0.04)^3 = 500 \times (1.04)^3 = 500 \times 1.124864 = \$562.43$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 1.04 | 0 | 0 | 0 | 1.04 |
| {{key:ENTER}} | 0 | 0 | 1.04 | 1.04 |
| {{key:3}} | 0 | 0 | 1.04 | 3 |
| {{keycap:yˣ}} | 0 | 0 | 0 | 1.124864 |
| 500 | 0 | 0 | 1.124864 | 500 |
| {{key:×}} | 0 | 0 | 0 | 562.43 |
Result: **$\$562.43$** total balance (yielding $\$62.43$ compound interest).

---

---

## Alignment with Elementary & Middle School Standards

The formulas, conversion standards, and prime algorithms detailed in this appendix directly support:
- **Common Core State Standards for Mathematics (CCSS-M):**
  - `4.OA.B.4`: Find all factor pairs for a whole number in the range 1–100; recognize that a whole number is a multiple of each of its factors; determine whether a given whole number is prime or composite.
  - `4.MD.A.1`: Know relative sizes of measurement units within one system of units (km, m, cm; kg, g; lb, oz; l, ml; hr, min, sec); express measurements in a larger unit in terms of a smaller unit.
  - `5.MD.C.5`: Relate volume to the operations of multiplication and addition and solve real-world and mathematical problems involving volume.
  - `6.G.A.1, 6.G.A.2, 6.G.A.4`: Find area of right triangles, other triangles, special quadrilaterals, and polygons; represent three-dimensional figures using nets; apply techniques in context of real-world problems.
  - `6.NS.B.4`: Find the greatest common factor of two whole numbers less than or equal to 100 and the least common multiple of two whole numbers less than or equal to 12.
- **Texas Essential Knowledge and Skills (TEKS):**
  - `4.5.C, 4.5.D`: Solve problems related to perimeter and area of rectangles.
  - `5.4.A`: Identify prime and composite numbers using concrete objects, pictorial models, and patterns in factor pairs.
  - `5.6.A, 5.6.B`: Recognize volume as an attribute of three-dimensional space; determine the volume of a rectangular prism.
  - `6.4.H`: Convert units within a measurement system, including the use of proportions and unit rates.
  - `6.7.A`: Generate equivalent numerical expressions using order of operations, including whole number exponents and prime factorization.
- **Competitive STEM & Number Sense Sprints:**
  - Fast prime verification and factor decomposition under 200.
  - Rapid mental and RPN execution of geometric area and volume benchmarks.

---

## Annotated Bibliography & Primary Mathematical Sources

{{bibliography:sc6}}

---

For detailed hands-on lesson plans implementing these formulas in classroom workshop stations, see [Appendix B: Teacher Lesson Plans & Diagnostic Protocols](appendix-b-teacher-lesson-plans.md). For physical fabrication of geometric models and calibration gauges, see [Appendix A: Manipulative Blueprints & Physical Fabrication Guide](appendix-a-manipulative-blueprints.md).
