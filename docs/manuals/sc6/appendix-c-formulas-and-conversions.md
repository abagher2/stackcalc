---
title: "Appendix C: Formulas, Conversions & Prime Catalogs"
description: "Comprehensive elementary mathematical reference catalog: geometric word rules with 4-register RPN stack traces, unit conversion tables, divisibility rules, and complete prime number directory under 200 for the StackCalc SC-6."
---

# Appendix C: Formulas, Conversions & Prime Catalogs

## The RPN Word-Rule Advantage

In many school textbooks, geometry rules and unit conversions are written with lots of letter variables and parentheses:

$$\text{Triangle Area} = (\text{Base} \times \text{Height}) \div 2 \qquad \text{Trapezoid Area} = (\text{Top} + \text{Bottom}) \div 2 \times \text{Height} \qquad \text{Celsius} = (\text{Fahrenheit} - 32) \times 5 \div 9$$

When students try to type these rules into an ordinary calculator, it is easy to miss a parenthesis or lose track of a middle step.

On the **StackCalc SC-6**, grounded in Jan Łukasiewicz’s parenthesis-free notation {{cite:lukasiewicz1924}} and Kathy Hamrick’s history of RPN calculator architecture {{cite:hamrick1980}}, the four-register Number Elevator ($X, Y, Z, T$) needs zero parentheses. Following David Macaulay’s cutaway principles {{cite:macaulay2016}}, every middle step stays visible on the screen and drops into place right when you tap an operation key. This appendix gives you step-by-step RPN keystrokes for every elementary math rule.

| Register | Metaphor | Role on the Screen |
| :--- | :--- | :--- |
| **Register T** | Penthouse | Holds the top waiting number |
| **Register Z** | Second Balcony | Holds a middle step while you work on the bottom floors |
| **Register Y** | First Balcony | Holds the first number waiting for an operation |
| **Register X** | Ground Lobby | Shows the number you are typing or the answer you just found |

---

## Table 1: Elementary Math & Geometry Word-Rule Directory

This directory pairs core number rules, 2D flat shape rules, and 3D solid box and cylinder rules with their physical block models and SC-6 keystroke sequences.

### Foundational Number Rules & Block Models

Elementary math is built on simple, reliable patterns. The table below pairs each rule with its physical block proof, chapter link, and SC-6 stack check:

| Math Rule | Rule in Words & Numbers | Physical Block Model | Chapter Link | SC-6 Stack Check (`Example`) |
|:---|:---|:---|:---|:---|
| **Turn-Around Rule (Addition)** | $\text{First} + \text{Second} = \text{Second} + \text{First}$ ($3 + 5 = 5 + 3$) | Sliding Number Rack beads left vs. right | [Chapter 4](04-operations-skip-counting.md) | `3 {{key:ENTER}} 5 {{key:+}}` equals `5 {{key:ENTER}} 3 {{key:+}}` |
| **Turn-Around Rule (Multiplication)** | $\text{Rows} \times \text{Columns} = \text{Columns} \times \text{Rows}$ ($4 \times 6 = 6 \times 4$) | Turning a 24-tile rectangle $90^\circ$ on the desk | [Chapter 4](04-operations-skip-counting.md) | `4 {{key:ENTER}} 6 {{key:×}}` equals `6 {{key:ENTER}} 4 {{key:×}}` |
| **Grouping Rule (Addition)** | $(\text{First} + \text{Second}) + \text{Third} = \text{First} + (\text{Second} + \text{Third})$ | Joining 3 color trains of snap cubes | [Chapter 4](04-operations-skip-counting.md) | `2 {{key:ENTER}} 3 {{key:+}} 4 {{key:+}}` |
| **Grouping Rule (Multiplication)** | $(\text{Length} \times \text{Width}) \times \text{Height}$ in any order | Stacking 3D layers of unit cubes | [Chapter 4](04-operations-skip-counting.md) | `2 {{key:ENTER}} 3 {{key:×}} 4 {{key:×}}` |
| **Break-Apart Rule (Distributive)** | $4 \times (10 + 3) = (4 \times 10) + (4 \times 3)$ | Splitting a 4-color tile rectangle along a color seam | [Chapter 4](04-operations-skip-counting.md) | `10 {{key:ENTER}} 3 {{key:+}} 4 {{key:×}}` |
| **Zero and One Rules** | Adding $0$ or multiplying by $1$ leaves a number unchanged | Adding zero tiles; taking 1 group of tiles | [Chapter 4](04-operations-skip-counting.md) | `7 {{key:ENTER}} 0 {{key:+}}` $\to 7$; `7 {{key:ENTER}} 1 {{key:×}}` $\to 7$ |
| **Division with Remainder Check** | $\text{Total} = (\text{Divisor} \times \text{Quotient}) + \text{Remainder}$ | Sharing counters equally into cups with leftovers | [Chapter 4](04-operations-skip-counting.md) | `29 {{key:ENTER}} 4 {{key:÷R}}` $\to$ Remainder `1` in $Y$, Quotient `7` in $X$ |
| **GCF and LCM Partner Rule** | $\text{GCF} \times \text{LCM} = \text{First Number} \times \text{Second Number}$ | Comparing Prime Factor Studio towers side by side | [Chapter 7](07-data-probability-primes.md) | `12 {{key:ENTER}} 18 {{key:GCF}} 12 {{key:ENTER}} 18 {{key:LCM}} {{key:×}}` $\to 216$ |
| **Fraction-to-Decimal Bridge** | $\text{Top Number} \div \text{Bottom Number} = \text{Decimal}$ | Comparing Fraction Towers to the $1\text{-Whole}$ tower | [Chapter 5](05-fractions-decimals-ratios.md) | `3 {{key:ENTER}} 4 {{key:÷}}` $\to 0.75$ |

---

### Two-Dimensional Perimeter & Area Word Rules

The table below summarizes 2D flat shape rules in plain words alongside their chapter links and SC-6 RPN keystroke sequences:

| Flat Shape | Word Rule | Chapter Link | SC-6 RPN Keystroke Sequence | Stack Floors Used |
|:---|:---|:---|:---|:---:|
| **Square (Perimeter)** | $\text{Perimeter} = 4 \times \text{Side}$ | [Chapter 6](06-geometry-surface-area.md) | `[Side] {{key:ENTER}} {{key:4}} {{key:×}}` | $Y, X$ |
| **Square (Area)** | $\text{Area} = \text{Side} \times \text{Side}$ | [Chapter 6](06-geometry-surface-area.md) | `[Side] {{key:x²}}` | $X$ |
| **Rectangle (Perimeter)** | $\text{Perimeter} = 2 \times (\text{Length} + \text{Width})$ | [Chapter 6](06-geometry-surface-area.md) | `[Length] {{key:ENTER}} [Width] {{key:+}} {{key:2}} {{key:×}}` | $Y, X$ |
| **Rectangle (Area)** | $\text{Area} = \text{Length} \times \text{Width}$ | [Chapter 6](06-geometry-surface-area.md) | `[Length] {{key:ENTER}} [Width] {{key:RECT}}` | $Y, X$ |
| **Triangle (Perimeter)** | $\text{Perimeter} = \text{Side 1} + \text{Side 2} + \text{Side 3}$ | [Chapter 6](06-geometry-surface-area.md) | `[Side 1] {{key:ENTER}} [Side 2] {{key:+}} [Side 3] {{key:+}}` | $Z, Y, X$ |
| **Triangle (Area)** | $\text{Area} = (\text{Base} \times \text{Height}) \div 2$ | [Chapter 6](06-geometry-surface-area.md) | `[Base] {{key:ENTER}} [Height] {{key:×}} {{key:2}} {{key:÷}}` | $Y, X$ |
| **Parallelogram (Area)** | $\text{Area} = \text{Base} \times \text{Height}$ | [Chapter 6](06-geometry-surface-area.md) | `[Base] {{key:ENTER}} [Height] {{key:×}}` | $Y, X$ |
| **Trapezoid (Area)** | $\text{Area} = (\text{Top} + \text{Bottom}) \div 2 \times \text{Height}$ | [Chapter 6](06-geometry-surface-area.md) | `[Top] {{key:ENTER}} [Bottom] {{key:+}} {{key:2}} {{key:÷}} [Height] {{key:×}}` | $Z, Y, X$ |
| **Circle (Circumference)** | $\text{Distance Around} = \pi \times \text{Width (Diameter)}$ | [Chapter 6](06-geometry-surface-area.md) | `[Diameter] {{key:π}} {{key:×}}` | $Y, X$ |
| **Circle (Area)** | $\text{Area} = \pi \times \text{Radius} \times \text{Radius}$ | [Chapter 6](06-geometry-surface-area.md) | `[Radius] {{key:x²}} {{key:π}} {{key:×}}` | $Y, X$ |

---

### Flat Shapes in Action: 2D Stack Traces

To see how Registers $T, Z, Y,$ and $X$ update step by step when measuring flat shapes, let's trace five classic two-dimensional shapes on the stack. Suppose you start with a **triangle** whose base is $14\text{ cm}$ and height is $9\text{ cm}$. Because any triangle is half of a bounding rectangle, the triangle word rule tells us that $\text{Area} = (\text{Base} \times \text{Height}) \div 2 = (14 \times 9) \div 2 = 63\text{ cm}^2$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `14` | 0 | 0 | 0 | 14 |
| `{{key:ENTER}}` | 0 | 0 | 14 | 14 |
| `{{key:9}}` | 0 | 0 | 14 | 9 |
| `{{key:×}}` | 0 | 0 | 0 | 126 |
| `{{key:2}}` | 0 | 0 | 126 | 2 |
| `{{key:÷}}` | 0 | 0 | 0 | 63 |

Notice how you first multiply $14 \times 9 = 126$ for the full bounding rectangle, and then type `2` and tap `{{key:÷}}` to slice that rectangle in half: $126 \div 2 = 63$.

What if the top of the shape isn't a sharp point, but a flat roof—making a **trapezoid** with a top width of $8\text{ in}$, a bottom width of $14\text{ in}$, and a height of $6\text{ in}$? Averaging the top and bottom widths first gives the middle width ($(8 + 14) \div 2 = 11\text{ in}$), and multiplying by the height gives $\text{Area} = (\text{Top} + \text{Bottom}) \div 2 \times \text{Height} = 11 \times 6 = 66\text{ sq in}$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:8}}` | 0 | 0 | 0 | 8 |
| `{{key:ENTER}}` | 0 | 0 | 8 | 8 |
| `14` | 0 | 0 | 8 | 14 |
| `{{key:+}}` | 0 | 0 | 0 | 22 |
| `{{key:2}}` | 0 | 0 | 22 | 2 |
| `{{key:÷}}` | 0 | 0 | 0 | 11 |
| `{{key:6}}` | 0 | 0 | 11 | 6 |
| `{{key:×}}` | 0 | 0 | 0 | 66 |

When straight edges curve into a circle—such as a **circular splash pad** with a radius of $3.5\text{ m}$—squaring the radius first (`3.5 {{key:x²}}` $\to 12.25$) and scaling by `{{key:π}}` yields $\text{Area} = \pi \times \text{Radius} \times \text{Radius} = \pi \times 3.5^2 \approx 38.48451\text{ m}^2$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `3.5` | 0 | 0 | 0 | 3.5 |
| `{{key:x²}}` | 0 | 0 | 0 | 12.25 |
| `{{key:π}}` | 0 | 0 | 12.25 | 3.1415926 |
| `{{key:×}}` | 0 | 0 | 0 | 38.484510 |

For the distance around the outside of a shape, we walk its perimeter. Around a **rectangular garden** of length $14\text{ m}$ and width $9\text{ m}$, adding the two adjacent sides into an L-shape ($14 + 9 = 23\text{ m}$) and doubling gives $\text{Perimeter} = 2 \times (\text{Length} + \text{Width}) = 2 \times 23 = 46\text{ m}$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `14` | 0 | 0 | 0 | 14 |
| `{{key:ENTER}}` | 0 | 0 | 14 | 14 |
| `{{key:9}}` | 0 | 0 | 14 | 9 |
| `{{key:+}}` | 0 | 0 | 0 | 23 |
| `{{key:2}}` | 0 | 0 | 23 | 2 |
| `{{key:×}}` | 0 | 0 | 0 | 46 |

And to find how far a $24\text{-inch}$ **bicycle wheel** rolls in one full turn ($\text{Circumference} = \pi \times 24$), typing `24 {{key:π}} {{key:×}}` on the stack immediately displays **$75.39822\text{ inches}$** per revolution.

---

### Three-Dimensional Solid Volume & Surface Area Word Rules

| 3D Solid Shape | Volume Word Rule | Total Surface Area Word Rule | Chapter Link | SC-6 Volume Keystrokes |
|:---|:---|:---|:---|:---|
| **Cube** | $\text{Volume} = \text{Side} \times \text{Side} \times \text{Side}$ | $\text{Surface Area} = 6 \times (\text{Side} \times \text{Side})$ | [Chapter 6](06-geometry-surface-area.md) | `[Side] {{key:ENTER}} {{key:3}} {{key:yˣ}}` |
| **Rectangular Box (Prism)** | $\text{Volume} = \text{Length} \times \text{Width} \times \text{Height}$ | Add all $6$ rectangular faces ($2\text{ Top/Bottom} + 2\text{ Front/Back} + 2\text{ Sides}$) | [Chapter 6](06-geometry-surface-area.md) | `[Length] {{key:ENTER}} [Width] {{key:×}} [Height] {{key:×}}` |
| **Triangular Tent (Prism)** | $\text{Volume} = (\text{Base} \times \text{Height} \div 2) \times \text{Length}$ | Add the $2$ triangle ends plus the $3$ rectangular side panels | [Chapter 6](06-geometry-surface-area.md) | `[Base] {{key:ENTER}} [Height] {{key:×}} 2 {{key:÷}} [Length] {{key:×}}` |
| **Cylinder (Can)** | $\text{Volume} = (\pi \times \text{Radius}^2) \times \text{Height}$ | $\text{Curved Side} \ (2 \times \pi \times \text{Radius} \times \text{Height}) + 2\text{ Circle Ends} \ (2 \times \pi \times \text{Radius}^2)$ | [Chapter 6](06-geometry-surface-area.md) | `[Radius] {{key:x²}} {{key:π}} {{key:×}} [Height] {{key:×}}` |

---

### Solid Shapes in Action: 3D Stack Traces

When a flat base is lifted upward into three dimensions, the stack lets you find both volume and surface area without parentheses or scratch paper. Consider a **cylindrical farm storage silo** with a radius of $4\text{ m}$ and a height of $10\text{ m}$. Its volume stacks the circular base area across the height: $(\pi \times 4^2) \times 10 = 160\pi \approx 502.6548\text{ m}^3$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:4}}` | 0 | 0 | 0 | 4 |
| `{{key:x²}}` | 0 | 0 | 0 | 16 |
| `{{key:π}}` | 0 | 0 | 16 | 3.1415926 |
| `{{key:×}}` | 0 | 0 | 0 | 50.265482 |
| `10` | 0 | 0 | 50.265482 | 10 |
| `{{key:×}}` | 0 | 0 | 0 | 502.654824 |

To paint that same silo's outer shell and both circular lids, we add the unrolled side wrapper to the two circular ends, $(2 \times \pi \times 4 \times 10) + (2 \times \pi \times 4^2) \approx 351.8584\text{ m}^2$, letting Register $Y$ hold the curved side area ($251.33\text{ m}^2$) while we build the two circular lids ($100.53\text{ m}^2$) in $X$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:2}}` | 0 | 0 | 0 | 2 |
| `{{key:π}} {{key:×}}` | 0 | 0 | 0 | 6.2831853 |
| `{{key:4}} {{key:×}}` | 0 | 0 | 0 | 25.132741 |
| `10 {{key:×}}` | 0 | 0 | 0 | 251.327412 |
| `{{key:2}}` | 0 | 0 | 251.327412 | 2 |
| `{{key:π}} {{key:×}}` | 0 | 0 | 251.327412 | 6.2831853 |
| `{{key:4}} {{key:x²}} {{key:×}}` | 0 | 0 | 251.327412 | 100.530964 |
| `{{key:+}}` | 0 | 0 | 0 | 351.858376 |

The same layer-stacking idea works for boxes and cubes. For a **square-base storage box** with a $6\text{ cm}$ base side and an $8\text{ cm}$ height, squaring the $6\text{ cm}$ side builds a $36\text{ cm}^2$ bottom layer, and multiplying by $8$ stacks up the layers ($36 \times 8 = 288\text{ cm}^3$):

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:6}} {{key:x²}}` | 0 | 0 | 0 | 36 |
| `{{key:8}}` | 0 | 0 | 36 | 8 |
| `{{key:×}}` | 0 | 0 | 0 | 288 |

And when all three dimensions match—such as a **$9\text{ cm}$ cube**—it holds $\text{Side}^3 = 9^3 = 729\text{ cm}^3$ of space inside (`{{key:9}} {{key:ENTER}} {{key:3}} {{key:yˣ}}` $\to \mathbf{729}\text{ cm}^3$) and is wrapped by six identical $9 \times 9$ square faces (`{{key:9}} {{key:x²}} {{key:6}} {{key:×}}` $\to \mathbf{486}\text{ cm}^2$).

---

## Total Surface Area via Statistical Accumulator (`{{key:Σ+}}`)

When unfolding a 3D box or tent into its flat net of faces, adding up all the faces on scratch paper is easy to mix up. On the SC-6, you can add each pair of matching faces directly into the statistical accumulator using `{{key:Σ+}}`:

| Step | Action | SC-6 Keystroke | Screen Count |
| :--- | :--- | :--- | :--- |
| **Step 1: Clear Memory** | Reset statistics | `{{key:CLΣ}}` | $\text{Count} = 0$ |
| **Step 2: Top & Bottom Faces** | $\text{Length} \times \text{Width} \times 2$ | `[Length] {{key:ENTER}} [Width] {{key:×}} 2 {{key:×}} {{key:Σ+}}` | Stored ($\text{Count} = 1$) |
| **Step 3: Front & Back Faces** | $\text{Length} \times \text{Height} \times 2$ | `[Length] {{key:ENTER}} [Height] {{key:×}} 2 {{key:×}} {{key:Σ+}}` | Stored ($\text{Count} = 2$) |
| **Step 4: Left & Right Faces** | $\text{Width} \times \text{Height} \times 2$ | `[Width] {{key:ENTER}} [Height] {{key:×}} 2 {{key:×}} {{key:Σ+}}` | Stored ($\text{Count} = 3$) |
| **Step 5: Recall Total Area** | Sum all 6 faces | `{{key:Σx}}` | Total Surface Area on $X$ |

### Wrapping a Rectangular Box ($\text{Length} = 12\text{ cm}, \text{Width} = 7\text{ cm}, \text{Height} = 5\text{ cm}$)
Unfolding a $12 \times 7 \times 5\text{ cm}$ box reveals three matching pairs of faces: the top and bottom ($2 \times 12 \times 7 = 168\text{ cm}^2$), the front and back ($2 \times 12 \times 5 = 120\text{ cm}^2$), and the left and right ends ($2 \times 7 \times 5 = 70\text{ cm}^2$). Tap `{{key:CLΣ}}` to clear the accumulator, then feed in the three pairs one after another:
1. `12 {{key:ENTER}} {{key:7}} {{key:×}} {{key:2}} {{key:×}} {{key:Σ+}}` (Screen confirms count $1$).
2. `12 {{key:ENTER}} {{key:5}} {{key:×}} {{key:2}} {{key:×}} {{key:Σ+}}` (Screen confirms count $2$).
3. `{{key:7}} {{key:ENTER}} {{key:5}} {{key:×}} {{key:2}} {{key:×}} {{key:Σ+}}` (Screen confirms count $3$).
4. Tap `{{key:Σx}}` to recall the combined surface area: **$358.00\text{ cm}^2$**.

### Pitching a Triangular Camping Tent
A triangular camping tent has two triangle end doors with a base of $6\text{ ft}$, a height of $4\text{ ft}$, and slanted roof edges of $5\text{ ft}$, stretched along a $10\text{ ft}$ floor. The two triangle doors together equal one $6 \times 4$ rectangle ($24\text{ sq ft}$), the floor panel covers $6 \times 10 = 60\text{ sq ft}$, and the two slanted roof panels cover $2 \times (5 \times 10) = 100\text{ sq ft}$. After tapping `{{key:CLΣ}}`, store the triangle doors with `{{key:6}} {{key:ENTER}} {{key:4}} {{key:×}} {{key:Σ+}}`, the floor panel with `{{key:6}} {{key:ENTER}} 10 {{key:×}} {{key:Σ+}}`, and the roof panels with `{{key:5}} {{key:ENTER}} 10 {{key:×}} {{key:2}} {{key:×}} {{key:Σ+}}`. Pressing `{{key:Σx}}` sums all five fabric panels to **$184.00\text{ sq ft}$**.

---

## Table 2: Complete Unit Conversions Directory

Unit conversions multiply or divide by a fixed conversion number.

### Length Conversions

| From Unit | To Unit | Conversion Number | SC-6 Forward Keystrokes | Reverse (Back Again) |
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

For example, to convert a $100\text{-yard}$ football field into meters, key in `{{res:sc6_appendix_c_formulas_and_conversions_seq_01:keys}}` to obtain **$91.44\text{ meters}$**—and dividing right back with `{{key:.}} 9144 {{key:÷}}` restores the original **$100.00\text{ yards}$**.

---

### Area Conversions

| From Unit | To Unit | Conversion Number | SC-6 Forward Keystrokes | Reverse |
|:---|:---|:---:|:---|:---:|
| **Square Feet (sq ft)**| **Square Inches (sq in)**| $144.0$ | `[sq ft] {{key:ENTER}} 144 {{key:×}}` | $\div 144$ |
| **Square Yards (sq yd)**| **Square Feet (sq ft)**| $9.0$ | `[sq yd] {{key:ENTER}} {{key:9}} {{key:×}}` | $\div 9$ |
| **Acres (ac)** | **Square Feet (sq ft)**| $43,560.0$ | `[ac] {{key:ENTER}} 43560 {{key:×}}`| $\div 43560$ |
| **Acres (ac)** | **Hectares (ha)** | $\approx 0.4046856$| `[ac] {{key:ENTER}} {{key:.}} 4047 {{key:×}}`| $\div 0.4047$ |
| **Hectares (ha)** | **Square Meters ($\text{m}^2$)**| $10,000.0$ | `[ha] {{key:ENTER}} 10000 {{key:×}}`| $\div 10000$ |
| **Square Miles ($\text{mi}^2$)**| **Acres (ac)** | $640.0$ | `[sq mi] {{key:ENTER}} 640 {{key:×}}` | $\div 640$ |
| **Square Meters ($\text{m}^2$)**| **Square Feet (sq ft)**| $\approx 10.76391$ | `[m²] {{key:ENTER}} 10.764 {{key:×}}`| $\div 10.764$ |

For instance, to find how many square feet lie inside a $2.5\text{-acre}$ neighborhood park, enter `{{res:sc6_appendix_c_formulas_and_conversions_seq_02:keys}}`, which reveals **$108,900\text{ sq ft}$**.

---

### Weight & Mass Conversions

| From Unit | To Unit | Conversion Number | SC-6 Forward Keystrokes | Reverse |
|:---|:---|:---:|:---|:---:|
| **Ounces (oz)** | **Grams (g)** | $28.349523$ | `[oz] {{key:ENTER}} 28.35 {{key:×}}` | $\div 28.3495$ |
| **Pounds (lb)** | **Ounces (oz)** | $16.0$ | `[lb] {{key:ENTER}} 16 {{key:×}}` | $\div 16$ |
| **Pounds (lb)** | **Kilograms (kg)** | $0.45359237$| `[lb] {{key:ENTER}} {{key:.}} 4536 {{key:×}}` | $\div 0.4536$ |
| **Kilograms (kg)** | **Pounds (lb)** | $\approx 2.2046226$| `[kg] {{key:ENTER}} 2.2046 {{key:×}}`| $\div 2.2046$ |
| **Tons (US Short)**| **Pounds (lb)** | $2000.0$ | `[ton] {{key:ENTER}} 2000 {{key:×}}` | $\div 2000$ |
| **Metric Tons (t)** | **Kilograms (kg)** | $1000.0$ | `[t] {{key:ENTER}} 1000 {{key:×}}` | $\div 1000$ |
| **Kilograms (kg)** | **Grams (g)** | $1000.0$ | `[kg] {{key:ENTER}} 1000 {{key:×}}` | $\div 1000$ |
| **Grams (g)** | **Milligrams (mg)** | $1000.0$ | `{{key:ENTER}} 1000 {{key:×}}` | $\div 1000$ |

To convert a $65\text{ lb}$ bicycle shipping crate into kilograms, press `{{res:sc6_appendix_c_formulas_and_conversions_seq_03:keys}}` to read **$29.483\text{ kg}$** on the display.

---

### Capacity & Liquid Volume Conversions

| From Unit | To Unit | Conversion Number | SC-6 Forward Keystrokes | Reverse |
|:---|:---|:---:|:---|:---:|
| **Fluid Ounces (fl oz)** | **Milliliters (mL)** | $29.57352956$| `[fl oz] {{key:ENTER}} 29.57 {{key:×}}` | $\div 29.5735$ |
| **Cups (c)** | **Fluid Ounces (fl oz)**| $8.0$ | `[c] {{key:ENTER}} {{key:8}} {{key:×}}` | $\div 8$ |
| **Pints (pt)** | **Cups (c)** | $2.0$ | `[pt] {{key:ENTER}} {{key:2}} {{key:×}}` | $\div 2$ |
| **Quarts (qt)** | **Pints (pt)** | $2.0$ | `[qt] {{key:ENTER}} {{key:2}} {{key:×}}` | $\div 2$ |
| **Gallons (gal US)**| **Quarts (qt)** | $4.0$ | `[gal] {{key:ENTER}} {{key:4}} {{key:×}}` | $\div 4$ |
| **Gallons (gal US)**| **Liters (L)** | $3.785411784$ | `[gal] {{key:ENTER}} 3.7854 {{key:×}}`| $\div 3.7854$ |
| **Gallons (Imperial)**| **Liters (L)** | $4.54609$ | `[gal imp] {{key:ENTER}} 4.546 {{key:×}}`| $\div 4.5461$ |
| **Liters (L)** | **Milliliters (mL)** | $1000.0$ | `[L] {{key:ENTER}} 1000 {{key:×}}` | $\div 1000$ |
| **Cubic Meters ($\text{m}^3$)**| **Liters (L)** | $1000.0$ | `[m³] {{key:ENTER}} 1000 {{key:×}}` | $\div 1000$ |

To convert a $15\text{-gallon}$ camp water tank into liters, run `{{res:sc6_appendix_c_formulas_and_conversions_seq_04:keys}}` to find **$56.781\text{ liters}$**.

---

### Speed Conversions

| From Unit | To Unit | Conversion Number | SC-6 Keystrokes |
|:---|:---|:---:|:---|
| **Miles per Hour (mph)**| **Kilometers per Hour (km/h)**| $1.609344$ | `[mph] {{key:ENTER}} 1.609 {{key:×}}` |
| **Miles per Hour (mph)**| **Feet per Second (ft/s)**| $\approx 1.466667$ | `[mph] {{key:ENTER}} 5280 {{key:×}} 3600 {{key:÷}}` |
| **Kilometers per Hour (km/h)**| **Meters per Second (m/s)**| $\approx 0.277778$| `[km/h] {{key:ENTER}} 1000 {{key:×}} 3600 {{key:÷}}` |
| **Knots (kt)** | **Miles per Hour (mph)**| $\approx 1.150779$ | `[kt] {{key:ENTER}} 1.151 {{key:×}}` |
| **Knots (kt)** | **Kilometers per Hour (km/h)**| $1.852$ | `[kt] {{key:ENTER}} 1.852 {{key:×}}` |

When a quadcopter drone flies at $45\text{ mph}$, you can find how many feet it covers each second by keying in `{{res:sc6_appendix_c_formulas_and_conversions_seq_05:keys}}`, which lands on **$66.0\text{ ft/s}$**.

---

### Tire & Air Pressure Conversions

| From Unit | To Unit | Conversion Number | SC-6 Keystrokes |
|:---|:---|:---:|:---|
| **Atmospheres (atm)** | **Pounds per Sq Inch (psi)**| $14.6959488$ | `[atm] {{key:ENTER}} 14.696 {{key:×}}` |
| **Atmospheres (atm)** | **Kilopascals (kPa)** | $101.325$ | `[atm] {{key:ENTER}} 101.325 {{key:×}}` |
| **Bar (bar)** | **Kilopascals (kPa)** | $100.0$ | `[bar] {{key:ENTER}} 100 {{key:×}}` |
| **Pounds per Sq Inch (psi)**| **Kilopascals (kPa)**| $6.894757$ | `[psi] {{key:ENTER}} 6.895 {{key:×}}` |

If a road bicycle tire is inflated to $85\text{ psi}$, keying in `{{res:sc6_appendix_c_formulas_and_conversions_seq_06:keys}}` converts that pressure to **$586.05\text{ kPa}$**.

---

### Time Conversions

| From Unit | To Unit | Conversion Number | SC-6 Keystroke Sequence |
|:---|:---|:---:|:---|
| **Minutes (min)** | **Seconds (s)** | $60.0$ | `[min] {{key:ENTER}} 60 {{key:×}}` |
| **Hours (hr)** | **Minutes (min)** | $60.0$ | `[hr] {{key:ENTER}} 60 {{key:×}}` |
| **Hours (hr)** | **Seconds (s)** | $3600.0$ | `[hr] {{key:ENTER}} 3600 {{key:×}}` |
| **Days (d)** | **Hours (hr)** | $24.0$ | `[days] {{key:ENTER}} 24 {{key:×}}` |
| **Weeks (wk)** | **Days (d)** | $7.0$ | `[wk] {{key:ENTER}} {{key:7}} {{key:×}}` |
| **Years (yr standard)**| **Days (d)** | $365.0$ | `[yr] {{key:ENTER}} 365 {{key:×}}` |
| **Years (yr leap)**| **Days (d)** | $366.0$ | `[yr] {{key:ENTER}} 366 {{key:×}}` |

To count how many seconds tick by in a full 24-hour day, enter `{{res:sc6_appendix_c_formulas_and_conversions_seq_07:keys}}` to reach **$86,400\text{ seconds}$**.

---

### Temperature Conversions (Fahrenheit and Celsius)

Because water freezes at $32^\circ\text{F}$ ($0^\circ\text{C}$) and boils at $212^\circ\text{F}$ ($100^\circ\text{C}$), converting between Fahrenheit and Celsius uses two simple word rules:

$$\text{Celsius} = (\text{Fahrenheit} - 32) \times 5 \div 9 \qquad \text{Fahrenheit} = (\text{Celsius} \times 9 \div 5) + 32$$

| Conversion | Word Rule | SC-6 Step-by-Step Keystrokes (or One-Tap Key) |
| :--- | :--- | :--- |
| **Fahrenheit to Celsius** | $(\text{Fahrenheit} - 32) \times 5 \div 9$ | `[Temp F] {{key:ENTER}} 32 {{key:-}} {{key:5}} {{key:×}} {{key:9}} {{key:÷}}` (or `[Temp F] {{key:▸°C}}`) |
| **Celsius to Fahrenheit** | $(\text{Celsius} \times 9 \div 5) + 32$ | `[Temp C] {{key:ENTER}} {{key:9}} {{key:×}} {{key:5}} {{key:÷}} 32 {{key:+}}` (or `[Temp C] {{key:▸°F}}`) |

Here is how normal human body temperature ($98.6^\circ\text{F}$) converts to Celsius step by step on the stack:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `98.6` | 0 | 0 | 0 | 98.6 |
| `{{key:ENTER}}` | 0 | 0 | 98.6 | 98.6 |
| `32` | 0 | 0 | 98.6 | 32 |
| `{{key:-}}` | 0 | 0 | 0 | 66.6 |
| `{{key:5}}` | 0 | 0 | 66.6 | 5 |
| `{{key:×}}` | 0 | 0 | 0 | 333.0 |
| `{{key:9}}` | 0 | 0 | 333.0 | 9 |
| `{{key:÷}}` | 0 | 0 | 0 | 37.0 |

Normal human body temperature is **$37.0^\circ\text{C}$** (or in one tap on the SC-6 keypad, `98.6 {{key:▸°C}}` $\to$ `37.00`).

---

### Chaining Multi-Step Unit Conversions on the Stack

When a real-world measurement needs two conversion steps in a row, the stack lets you chain them without parentheses or scratch paper. For a **marathon footrace** ($26.2\text{ miles} \to \text{kilometers} \to \text{meters}$), since $1\text{ mile} = 1.609344\text{ kilometers}$ and $1\text{ kilometer} = 1,000\text{ meters}$, multiplying $26.2 \times 1.609344$ first gives $42.164813\text{ km}$ and multiplying by $1,000$ converts to meters:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:2}} {{key:6}} {{key:.}} {{key:2}}` | 0 | 0 | 0 | 26.2 |
| `{{key:ENTER}}` | 0 | 0 | 26.2 | 26.2 |
| `1.609344` | 0 | 0 | 26.2 | 1.609344 |
| `{{key:×}}` | 0 | 0 | 0 | 42.164813 |
| `1000` | 0 | 0 | 42.164813 | 1000 |
| `{{key:×}}` | 0 | 0 | 0 | 42164.81280 |

Register $X$ shows the full Olympic marathon distance in meters: **$42,164.81\text{ meters}$**.

Next, consider an **airliner cruising at $36,000\text{ ft}$** ($36,000\text{ ft} \to \text{meters} \to \text{kilometers}$). Using $1\text{ foot} = 0.3048\text{ meters}$, we multiply $36,000 \times 0.3048$ to get meters and immediately divide by $1,000$ for kilometers:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `36000` | 0 | 0 | 0 | 36000 |
| `{{key:ENTER}}` | 0 | 0 | 36000 | 36000 |
| `.3048` | 0 | 0 | 36000 | 0.3048 |
| `{{key:×}}` | 0 | 0 | 0 | 10972.8 |
| `1000` | 0 | 0 | 10972.8 | 1000 |
| `{{key:÷}}` | 0 | 0 | 0 | 10.9728 |

Cruising height is **$10,972.8\text{ meters}$**, or **$10.97\text{ km}$** above sea level.

What about comparing **family car fuel mileage** ($35.0\text{ Miles per Gallon} \to \text{Liters per 100 km}$)? Dividing the conversion constant $235.215$ by the Miles per Gallon ($\text{Liters per 100 km} = 235.215 \div \text{MPG}$) flips American mileage into metric fuel consumption:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `235.215` | 0 | 0 | 0 | 235.215 |
| `{{key:ENTER}}` | 0 | 0 | 235.215 | 235.215 |
| `35` | 0 | 0 | 235.215 | 35 |
| `{{key:÷}}` | 0 | 0 | 0 | 6.720429 |

A car rated at $35\text{ MPG}$ burns **$6.72\text{ liters of fuel per 100 kilometers}$**.

Finally, we can test a **snowy winter morning temperature** ($14^\circ\text{F} \to -10^\circ\text{C} \to 14^\circ\text{F}$) by converting $14^\circ\text{F}$ into Celsius and then running the inverse steps right on the stack to return to $14^\circ\text{F}$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `14` | 0 | 0 | 0 | 14 |
| `{{key:ENTER}}` | 0 | 0 | 14 | 14 |
| `32` | 0 | 0 | 14 | 32 |
| `{{key:-}}` | 0 | 0 | 0 | -18 |
| `{{key:5}}` | 0 | 0 | -18 | 5 |
| `{{key:×}}` | 0 | 0 | 0 | -90 |
| `{{key:9}}` | 0 | 0 | -90 | 9 |
| `{{key:÷}}` | 0 | 0 | 0 | -10 |
| `{{key:9}} {{key:×}} {{key:5}} {{key:÷}}` | 0 | 0 | 0 | -18 |
| `32 {{key:+}}` | 0 | 0 | 0 | 14 |

Here $14^\circ\text{F}$ equals **$-10^\circ\text{C}$** (ten degrees below freezing), and reversing the steps returns **$14^\circ\text{F}$**.

---

## Table 3: Prime Number Catalog & Factorization Directory

A prime number is a whole number greater than 1 that has **only two factors: 1 and itself**. Every composite number greater than 1 can be built by multiplying a unique team of prime numbers together.

### Complete Catalog of All 46 Prime Numbers Under 200

There are **46 prime numbers** less than 200. The table below lists each prime number, its Twin Prime partner (a prime just 2 steps away), and a fun number pattern:

| Prime # | Prime Number | Twin Prime Partner | Fun Number Pattern |
|:---:|:---:|:---|:---|
| #1 | **2** | Only Even Prime | Only even prime; smallest prime number ($1 + 1 = 2$). |
| #2 | **3** | Twin with 5 | Smallest odd prime ($2^2 - 1 = 3$). |
| #3 | **5** | Twin with 3 and 7 | Only prime in two twin pairs ($3,5$ and $5,7$); sum of two squares ($1^2 + 2^2 = 5$). |
| #4 | **7** | Twin with 5 | Largest one-digit prime ($2^3 - 1 = 7$). |
| #5 | **11** | Twin with 13 | Smallest two-digit prime; reads the same forward and backward. |
| #6 | **13** | Twin with 11 | Reversing its digits makes $31$ (also prime!); sum of two squares ($2^2 + 3^2 = 13$). |
| #7 | **17** | Twin with 19 | Sum of the first four primes ($2 + 3 + 5 + 7 = 17$); $4^2 + 1 = 17$. |
| #8 | **19** | Twin with 17 | Twin prime partner of $17$ ($1 + 6 + 12 = 19$). |
| #9 | **23** | Solo Prime | Sum of three consecutive primes ($5 + 7 + 11 = 23$). |
| #10 | **29** | Twin with 31 | Sum of three consecutive squares ($2^2 + 3^2 + 4^2 = 29$); also $2^2 + 5^2 = 29$. |
| #11 | **31** | Twin with 29 | One less than $32$ ($2^5 - 1 = 31$); digit-flip partner of $13$. |
| #12 | **37** | Solo Prime | Sum of two squares ($1^2 + 6^2 = 37$); digit-flip partner of $73$. |
| #13 | **41** | Twin with 43 | Sum of the first six primes ($2 + 3 + 5 + 7 + 11 + 13 = 41$); $4^2 + 5^2 = 41$. |
| #14 | **43** | Twin with 41 | Twin prime partner of $41$ ($6^2 + 7 = 43$). |
| #15 | **47** | Solo Prime | Two less than a square ($7^2 - 2 = 47$). |
| #16 | **53** | Solo Prime | Sum of two squares ($2^2 + 7^2 = 53$); sum of five primes ($5 + 7 + 11 + 13 + 17 = 53$). |
| #17 | **59** | Twin with 61 | Sum of three consecutive primes ($17 + 19 + 23 = 59$). |
| #18 | **61** | Twin with 59 | Sum of two squares ($5^2 + 6^2 = 61$); difference of two cubes ($5^3 - 4^3 = 61$). |
| #19 | **67** | Solo Prime | Sum of five consecutive primes ($7 + 11 + 13 + 17 + 19 = 67$). |
| #20 | **71** | Twin with 73 | Sum of three consecutive primes ($19 + 23 + 29 = 71$); digit-flip partner of $17$. |
| #21 | **73** | Twin with 71 | Sum of two squares ($3^2 + 8^2 = 73$); digit-flip partner of $37$. |
| #22 | **79** | Solo Prime | Digit-flip partner of $97$ ($79$ and $97$ are both prime). |
| #23 | **83** | Solo Prime | Sum of three consecutive primes ($23 + 29 + 31 = 83$); $9^2 + 2 = 83$. |
| #24 | **89** | Solo Prime | Fibonacci prime ($34 + 55 = 89$); sum of two squares ($5^2 + 8^2 = 89$). |
| #25 | **97** | Solo Prime | Largest two-digit prime; sum of two squares ($4^2 + 9^2 = 97$). |
| #26 | **101** | Twin with 103 | Smallest three-digit prime; reads the same forward and backward ($10^2 + 1 = 101$). |
| #27 | **103** | Twin with 101 | Twin prime partner of $101$. |
| #28 | **107** | Twin with 109 | Twin prime partner of $109$. |
| #29 | **109** | Twin with 107 | Sum of two squares ($3^2 + 10^2 = 109$); twin prime partner of $107$. |
| #30 | **113** | Solo Prime | Sum of two squares ($7^2 + 8^2 = 113$); every rearrangement of its digits ($113, 131, 311$) is prime! |
| #31 | **127** | Solo Prime | One less than $128$ ($2^7 - 1 = 127$). |
| #32 | **131** | Solo Prime | Reads the same forward and backward; digit partner of $113$ and $311$. |
| #33 | **137** | Twin with 139 | Sum of two squares ($4^2 + 11^2 = 137$); twin prime partner of $139$. |
| #34 | **139** | Twin with 137 | Twin prime partner of $137$; sum of five primes ($19 + 23 + 29 + 31 + 37 = 139$). |
| #35 | **149** | Twin with 151 | Sum of two squares ($7^2 + 10^2 = 149$). |
| #36 | **151** | Twin with 149 | Reads the same forward and backward; twin prime partner of $149$. |
| #37 | **157** | Solo Prime | Sum of two squares ($6^2 + 11^2 = 157$); halfway between $151$ and $163$. |
| #38 | **163** | Solo Prime | Solo prime between $157$ and $167$ ($9^2 + 9^2 + 1 = 163$). |
| #39 | **167** | Solo Prime | Two less than $169$ ($13^2 - 2 = 167$). |
| #40 | **173** | Solo Prime | Sum of two squares ($2^2 + 13^2 = 173$); sum of three primes ($53 + 59 + 61 = 173$). |
| #41 | **179** | Twin with 181 | Twin prime partner of $181$. |
| #42 | **181** | Twin with 179 | Reads the same forward and backward; sum of two squares ($9^2 + 10^2 = 181$). |
| #43 | **191** | Twin with 193 | Reads the same forward and backward; twin prime partner of $193$. |
| #44 | **193** | Twin with 191 | Sum of two squares ($7^2 + 12^2 = 193$); twin prime partner of $191$. |
| #45 | **197** | Twin with 199 | Sum of the first twelve primes ($2 + 3 + \dots + 37 = 197$); $14^2 + 1 = 197$. |
| #46 | **199** | Twin with 197 | Largest prime under $200$; sum of three consecutive primes ($61 + 67 + 71 = 199$). |

---

### Quick Divisibility Rules with SC-6 Checks

Before testing a big number with `{{key:PRIME}}`, you can spot small factors right away using these mental math rules:

| Divide By | Quick Mental Rule | How to Check on Your SC-6 (`{{key:÷R}}`) | Example |
|:---:|:---|:---|:---|
| **2** | Last digit is even ($0, 2, 4, 6, 8$). | `[Number] {{key:ENTER}} {{key:2}} {{key:÷R}}` (Remainder in $Y$ is `0`) | $84 \div 2 = 42$ with Remainder $0$ |
| **3** | Add the digits; the sum divides evenly by 3. | Add the digits on the stack, then press `{{key:3}} {{key:÷R}}` | $153 \to 1+5+3=9$, and $9 \div 3 = 3$ |
| **4** | Last two digits divide evenly by 4. | `[Last 2 Digits] {{key:ENTER}} {{key:4}} {{key:÷R}}` | $3,728 \to 28 \div 4 = 7$ (Remainder $0$) |
| **5** | Last digit is 0 or 5. | Look at the ones digit on the screen. | $95$ ends in $5$ ($95 \div 5 = 19$) |
| **6** | Passes both the 2-test (even) and the 3-test. | Check that it is even and its digits add to a multiple of 3. | $78$ is even, and $7+8=15$ ($78 \div 6 = 13$) |
| **8** | Last three digits divide evenly by 8. | `[Last 3 Digits] {{key:ENTER}} {{key:8}} {{key:÷R}}` | $5,128 \to 128 \div 8 = 16$ (Remainder $0$) |
| **9** | Add the digits; the sum divides evenly by 9. | Add the digits on the stack, then press `{{key:9}} {{key:÷R}}` | $423 \to 4+2+3=9$, and $9 \div 9 = 1$ |
| **10** | Last digit is 0. | Look at the ones digit on the screen. | $340$ ends in $0$ ($340 \div 10 = 34$) |

---

### Ten Classic Prime Factorizations

Every composite whole number greater than 1 breaks down into a unique product of prime numbers—just like a tower built from your **Prime Factor Studio** blocks! The table below shows 10 classic composite numbers, their prime factor blocks, and how to multiply the prime blocks back together on your SC-6:

| Composite Number | Prime Factor Blocks | SC-6 `{{key:FACT}}` Screen Output | RPN Keystrokes to Multiply Them Back |
|:---:|:---:|:---|:---|
| **72** | $2^3 \times 3^2$ | `2^3 * 3^2` | `{{key:2}} {{key:ENTER}} {{key:3}} {{key:yˣ}} {{key:3}} {{key:x²}} {{key:×}}` $\to 72$ |
| **84** | $2^2 \times 3 \times 7$ | `2^2 * 3 * 7` | `{{key:2}} {{key:x²}} {{key:3}} {{key:×}} {{key:7}} {{key:×}}` $\to 84$ |
| **180** | $2^2 \times 3^2 \times 5$ | `2^2 * 3^2 * 5` | `{{key:2}} {{key:x²}} {{key:3}} {{key:x²}} {{key:×}} {{key:5}} {{key:×}}` $\to 180$ |
| **252** | $2^2 \times 3^2 \times 7$ | `2^2 * 3^2 * 7` | `{{key:2}} {{key:x²}} {{key:3}} {{key:x²}} {{key:×}} {{key:7}} {{key:×}}` $\to 252$ |
| **360** | $2^3 \times 3^2 \times 5$ | `2^3 * 3^2 * 5` | `{{key:2}} {{key:ENTER}} {{key:3}} {{key:yˣ}} {{key:3}} {{key:x²}} {{key:×}} {{key:5}} {{key:×}}` $\to 360$ |
| **504** | $2^3 \times 3^2 \times 7$ | `2^3 * 3^2 * 7` | `{{key:2}} {{key:ENTER}} {{key:3}} {{key:yˣ}} {{key:3}} {{key:x²}} {{key:×}} {{key:7}} {{key:×}}` $\to 504$ |
| **720** | $2^4 \times 3^2 \times 5$ | `2^4 * 3^2 * 5` | `{{key:2}} {{key:ENTER}} {{key:4}} {{key:yˣ}} {{key:3}} {{key:x²}} {{key:×}} {{key:5}} {{key:×}}` $\to 720$ |
| **1,000** | $2^3 \times 5^3$ | `2^3 * 5^3` | `{{key:2}} {{key:ENTER}} {{key:3}} {{key:yˣ}} {{key:5}} {{key:ENTER}} {{key:3}} {{key:yˣ}} {{key:×}}` $\to 1000$ |
| **1,024** | $2^{10}$ | `2^10` | `{{key:2}} {{key:ENTER}} 10 {{key:yˣ}}` $\to 1024$ |
| **1,729** | $7 \times 13 \times 19$ | `7 * 13 * 19` | `{{key:7}} {{key:ENTER}} 13 {{key:×}} 19 {{key:×}}` $\to 1729$ |

*Fun Fact about 1,729 (The Taxicab Number):* $1,729$ is the smallest whole number that can be built by adding two cubes in two different ways:
$$1,729 = 1^3 + 12^3 = 9^3 + 10^3$$
You can verify both cube sums on your SC-6:
- **First Cube Pair ($1^3 + 12^3$):** `{{key:1}} {{key:ENTER}} {{key:3}} {{key:yˣ}} 12 {{key:ENTER}} {{key:3}} {{key:yˣ}} {{key:+}}` $\to 1 + 1728 = 1729$.
- **Second Cube Pair ($9^3 + 10^3$):** `{{key:9}} {{key:ENTER}} {{key:3}} {{key:yˣ}} 10 {{key:ENTER}} {{key:3}} {{key:yˣ}} {{key:+}}` $\to 729 + 1000 = 1729$.

---

### GCF and LCM Reference Table for Common Number Pairs

The table below shows 9 popular number pairs, the prime blocks they share (`{{key:GCF}}`), the product of the two numbers, and their Least Common Multiple (`{{key:LCM}}`):

| Number Pair | Shared Prime Blocks | Greatest Common Factor (`GCF`) | First $\times$ Second | Least Common Multiple (`LCM`) |
|:---:|:---|:---:|:---:|:---:|
| **$24\text{ and }18$** | $2 \times 3$ | **6** | 432 | **72** |
| **$36\text{ and }24$** | $2 \times 2 \times 3$ | **12** | 864 | **72** |
| **$60\text{ and }42$** | $2 \times 3$ | **6** | 2,520 | **420** |
| **$84\text{ and }36$** | $2 \times 2 \times 3$ | **12** | 3,024 | **252** |
| **$105\text{ and }45$**| $3 \times 5$ | **15** | 4,725 | **315** |
| **$120\text{ and }75$**| $3 \times 5$ | **15** | 9,000 | **600** |
| **$144\text{ and }96$**| $2^4 \times 3$ | **48** | 13,824 | **288** |
| **$210\text{ and }165$**| $3 \times 5$ | **15** | 34,650 | **2,310** |
| **$252\text{ and }105$**| $3 \times 7$ | **21** | 26,460 | **1,260** |

---

### Goldbach's Even-Number Prime Puzzle (Evens 4 to 60)

In 1742, a mathematician named Christian Goldbach noticed an amazing pattern: **every even number greater than 2 can be written by adding two prime numbers together!**

You can test Goldbach's pattern on your SC-6 by picking any even number, checking two primes with `{{key:PRIME}}`, and adding them together:

| Even Number | Prime Pair Sum | Other Prime Pairs That Work | SC-6 RPN Check Keystrokes |
|:---:|:---:|:---|:---|
| **4** | $2 + 2$ | Only way | `{{key:2}} {{key:ENTER}} {{key:2}} {{key:+}}` $\to 4$ |
| **6** | $3 + 3$ | Only way | `{{key:3}} {{key:ENTER}} {{key:3}} {{key:+}}` $\to 6$ |
| **8** | $3 + 5$ | Only way | `{{key:3}} {{key:ENTER}} {{key:5}} {{key:+}}` $\to 8$ |
| **10** | $3 + 7$ | $5 + 5$ | `{{key:3}} {{key:ENTER}} {{key:7}} {{key:+}}` $\to 10$ |
| **12** | $5 + 7$ | Only way | `{{key:5}} {{key:ENTER}} {{key:7}} {{key:+}}` $\to 12$ |
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
| **38** | $7 + 31$ | $19 + 19$ | `{{key:7}} {{key:ENTER}} 31 {{key:+}}` $\to 38$ |
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

### Perfect Numbers & Giant Factor Challenges

A **Perfect Number** is a special whole number whose smaller factors add up to the number itself! Look at the first four perfect numbers:

| Perfect Number | Prime Recipe | Smaller Factors Added Together |
|:---:|:---:|:---|
| **6** | $2 \times 3$ | $1 + 2 + 3 = \mathbf{6}$ |
| **28** | $4 \times 7$ | $1 + 2 + 4 + 7 + 14 = \mathbf{28}$ |
| **496** | $16 \times 31$ | $1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 = \mathbf{496}$ |
| **8,128** | $64 \times 127$ | $1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + \dots = \mathbf{8,128}$ |

You can build the third perfect number ($496$) right on the stack by following Euclid's ancient recipe: multiply $2^4$ ($16$) by the prime number $2^5 - 1$ ($31$) to reach $16 \times 31 = 496$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:2}} {{key:ENTER}}` | 0 | 0 | 2 | 2 |
| `{{key:5}} {{key:yˣ}}` | 0 | 0 | 0 | 32 |
| `{{key:1}} {{key:-}}` | 0 | 0 | 0 | 31 |
| `{{key:PRIME}}` | 0 | 0 | 0 | 31 (Flashes `PRIME`) |
| `{{key:2}} {{key:ENTER}}` | 0 | 31 | 2 | 2 |
| `{{key:4}} {{key:yˣ}}` | 0 | 0 | 31 | 16 |
| `{{key:×}}` | 0 | 0 | 0 | 496 |

Register $X$ lands on **$496$**, the third perfect number! That same curiosity about giant powers of two led to one of history's most famous division checks: for over a hundred years, mathematicians wondered whether $4,294,967,297$ was a prime number, until Leonhard Euler discovered that $641$ divides into it evenly with zero remainder:
$$4,294,967,297 = 641 \times 6,700,417$$
You can test Euler's discovery right on your SC-6 by keying in `{{res:sc6_appendix_c_formulas_and_conversions_seq_08:keys}}`, which lands cleanly on **$6,700,417.00$** with no decimal remainder!

---

## Quick-Reference Word-Rule Lookup Tables

Use the two lookup tables below whenever you need the fastest SC-6 keystroke pattern for a geometry, measurement, or money problem.

### Geometry & Measurement Quick Lookup

| Math Task | What You Know | Word Rule | SC-6 Keystroke Pattern |
|:---|:---|:---|:---|
| **Area of a Circle** | Radius | $\pi \times \text{Radius} \times \text{Radius}$ | `[Radius] {{key:x²}} {{key:π}} {{key:×}}` |
| **Distance Around a Circle** | Width (Diameter) | $\pi \times \text{Diameter}$ | `[Diameter] {{key:π}} {{key:×}}` |
| **Area of a Rectangle** | Length, Width | $\text{Length} \times \text{Width}$ | `[Length] {{key:ENTER}} [Width] {{key:RECT}}` |
| **Perimeter of a Rectangle**| Length, Width | $2 \times (\text{Length} + \text{Width})$ | `[Length] {{key:ENTER}} [Width] {{key:+}} {{key:2}} {{key:×}}` |
| **Area of a Triangle** | Base, Height | $(\text{Base} \times \text{Height}) \div 2$ | `[Base] {{key:ENTER}} [Height] {{key:×}} {{key:2}} {{key:÷}}` |
| **Area of a Trapezoid** | Top, Bottom, Height| $(\text{Top} + \text{Bottom}) \div 2 \times \text{Height}$ | `[Top] {{key:ENTER}} [Bottom] {{key:+}} {{key:2}} {{key:÷}} [Height] {{key:×}}` |
| **Volume of a Cylinder** | Radius, Height | $(\pi \times \text{Radius}^2) \times \text{Height}$ | `[Radius] {{key:x²}} {{key:π}} {{key:×}} [Height] {{key:×}}` |
| **Volume of a Box** | Length, Width, Height| $\text{Length} \times \text{Width} \times \text{Height}$ | `[Length] {{key:ENTER}} [Width] {{key:×}} [Height] {{key:×}}` |
| **Surface Area of a Cube** | Side Length | $6 \times (\text{Side} \times \text{Side})$ | `[Side] {{key:x²}} {{key:6}} {{key:×}}` |
| **Percent of a Number** | Whole, Percent | $\text{Whole} \times (\text{Percent} \div 100)$ | `[Whole] {{key:ENTER}} [Percent] {{key:%}}` |
| **Percent Change** | Starting, Ending | $(\text{Ending} - \text{Starting}) \div \text{Starting} \times 100$ | `[Starting] {{key:ENTER}} [Ending] {{key:%CHG}}` |
| **Fahrenheit to Celsius** | Temp in °F | $(\text{Temp F} - 32) \times 5 \div 9$ | `[Temp F] {{key:ENTER}} 32 {{key:-}} {{key:5}} {{key:×}} {{key:9}} {{key:÷}}` |
| **Celsius to Fahrenheit** | Temp in °C | $(\text{Temp C} \times 9 \div 5) + 32$ | `[Temp C] {{key:ENTER}} {{key:9}} {{key:×}} {{key:5}} {{key:÷}} 32 {{key:+}}` |
| **Speed (Unit Rate)** | Distance, Time | $\text{Distance} \div \text{Time}$ | `[Distance] {{key:ENTER}} [Time] {{key:÷}}` |
| **Unit Price** | Total Cost, Count | $\text{Total Cost} \div \text{Count}$ | `[Total Cost] {{key:ENTER}} [Count] {{key:÷}}` |
| **Miles to Kilometers** | Miles | $\text{Miles} \times 1.609344$ | `[Miles] {{key:ENTER}} 1.609344 {{key:×}}` |
| **Pounds to Kilograms** | Pounds | $\text{Pounds} \times 0.453592$ | `[Pounds] {{key:ENTER}} {{key:.}} 453592 {{key:×}}` |
| **Gallons to Liters** | Gallons | $\text{Gallons} \times 3.7854$ | `[Gallons] {{key:ENTER}} 3.7854 {{key:×}}` |

---

### Everyday Money & Shopping Word Rules

Because `{{key:%}}` on the SC-6 keeps the starting dollar amount sitting in Register $Y$, you can add sales tax or subtract a discount in one tap:

| Money Task | Word Rule | SC-6 Keystroke Pattern |
|:---|:---|:---|
| **Simple Interest Earned** | $\text{Starting Money} \times \text{Yearly Rate \%} \times \text{Years}$ | `[Money] {{key:ENTER}} [Rate] {{key:%}} [Years] {{key:×}} {{key:$}}` |
| **Sales Tax Amount** | $\text{Price} \times \text{Tax Rate \%}$ | `[Price] {{key:ENTER}} [Tax Rate] {{key:%}} {{key:$}}` |
| **Total Price with Tax** | $\text{Price} + \text{Sales Tax}$ | `[Price] {{key:ENTER}} [Tax Rate] {{key:%}} {{key:+}} {{key:$}}` |
| **Discount Saved** | $\text{Regular Price} \times \text{Discount \%}$ | `[Price] {{key:ENTER}} [Discount] {{key:%}} {{key:$}}` |
| **Sale Price After Discount** | $\text{Regular Price} - \text{Discount}$ | `[Price] {{key:ENTER}} [Discount] {{key:%}} {{key:-}} {{key:$}}` |
| **Restaurant Tip ($18\%$)**| $\text{Bill} \times 18\%$ | `[Bill] {{key:ENTER}} 18 {{key:%}} {{key:$}}` |

When money stays in a savings account for several years, the interest itself starts earning interest! For example, to watch a $\$500$ savings account grow at $4\%$ interest compounded yearly for $3$ years, multiply $\$500$ by $1.04$ three times ($1.04^3 \times \$500 = \$562.43$):

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `1.04` | 0 | 0 | 0 | 1.04 |
| `{{key:ENTER}}` | 0 | 0 | 1.04 | 1.04 |
| `{{key:3}}` | 0 | 0 | 1.04 | 3 |
| `{{key:yˣ}}` | 0 | 0 | 0 | 1.124864 |
| `500` | 0 | 0 | 1.124864 | 500 |
| `{{key:×}}` | 0 | 0 | 0 | 562.43 |

After $3$ years, the account holds **$\$562.43$** total savings ($\$62.43$ in interest earned).

---

## Alignment with Elementary & Middle School Standards

The word rules, conversion tables, and prime patterns in this appendix support:
- **Common Core State Standards for Mathematics (CCSS-M):**
  - `4.OA.B.4`: Find all factor pairs for a whole number in the range 1–100; recognize that a whole number is a multiple of each of its factors; determine whether a given whole number is prime or composite.
  - `4.MD.A.1`: Know relative sizes of measurement units within one system of units (km, m, cm; kg, g; lb, oz; l, ml; hr, min, sec); express measurements in a larger unit in terms of a smaller unit.
  - `5.MD.C.5`: Relate volume to the operations of multiplication and addition and solve real-world and mathematical problems involving volume.
  - `6.G.A.1, 6.G.A.2, 6.G.A.4`: Find area of right triangles, other triangles, special quadrilaterals, and polygons; represent three-dimensional figures using nets; apply techniques in context of real-world problems.
  - `6.NS.B.4`: Find the greatest common factor of two whole numbers less than or equal to 100 and the least common multiple of two whole numbers less than or equal to 12.
- **National & State Mathematics Standards (Grades 3–6):**
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

For detailed hands-on lesson plans implementing these rules in classroom workshop stations, see [Appendix B: Teacher Lesson Plans & Diagnostic Protocols](appendix-b-teacher-lesson-plans.md). For physical fabrication of geometric models and calibration gauges, see [Appendix A: Manipulative Blueprints & 3D Printing Fabrication Guide](appendix-a-manipulative-blueprints.md).
