---
title: "Appendix C: Formulas, Conversions & Prime Catalogs"
description: "Comprehensive elementary mathematical reference catalog: geometric word rules with 4-shelf RPN stack traces, unit conversion tables, divisibility rules, and complete prime number directory under 200 for the StackCalc SC-6."
---

# Appendix C: Formulas, Conversions & Prime Catalogs

## Elementary Math & Geometry Word-Rule Directory

In many school textbooks, geometry rules and unit conversions are written with lots of letter variables and parentheses:

$$\text{Triangle Area} = (\text{Base} \times \text{Height}) \div 2 \qquad \text{Trapezoid Area} = (\text{Top} + \text{Bottom}) \div 2 \times \text{Height} \qquad \text{Celsius} = (\text{Fahrenheit} - 32) \times 5 \div 9$$

When students try to type these rules into an ordinary calculator, it is easy to miss a parenthesis or lose track of a middle step.

On the **StackCalc SC-6**, the four-shelf stack ($X, Y, Z, T$) needs zero parentheses {{cite:lukasiewicz1924,hamrick1980}}. Just like looking inside a cutaway drawing of a machine {{cite:macaulay2016}}, every middle step stays visible on Waiting Shelf $Y$ and Upper Shelf $Z$ and drops into place right when you tap an operation key. This appendix gives you step-by-step RPN keystrokes, unit conversion factors, divisibility tests, and prime-number catalogs for every elementary and middle-school topic. This directory pairs core number rules, 2D flat shape rules, and 3D solid box and cylinder rules with their physical block models and SC-6 keystroke sequences.

### Foundational Number Rules & Block Models

Elementary math is built on simple, reliable patterns. The table below pairs each rule with its physical block proof, chapter link, and SC-6 stack check:

| Math Rule | Rule in Words & Numbers | Physical Block Model | Chapter Link | SC-6 Stack Check (`Example`) |
|:---|:---|:---|:---|:---|
| **Turn-Around Rule (Addition)** | $\text{First} + \text{Second} = \text{Second} + \text{First}$ ($3 + 5 = 5 + 3$) | Sliding Number Rack beads left vs. right | [Chapter 4](04-operations-skip-counting.md) | `3 {{key:ENTER}} 5 {{key:+}}` equals `5 {{key:ENTER}} 3 {{key:+}}` |
| **Turn-Around Rule (Multiplication)** | $\text{Rows} \times \text{Columns} = \text{Columns} \times \text{Rows}$ ($4 \times 6 = 6 \times 4$) | Turning a 24-tile rectangle $90^\circ$ on the desk | [Chapter 4](04-operations-skip-counting.md) | `4 {{key:ENTER}} 6 {{key:×}}` equals `6 {{key:ENTER}} 4 {{key:×}}` |
| **Grouping Rule (Addition)** | $(\text{First} + \text{Second}) + \text{Third} = \text{First} + (\text{Second} + \text{Third})$ | Joining 3 color trains of snap cubes | [Chapter 4](04-operations-skip-counting.md) | `2 {{key:ENTER}} 3 {{key:+}} 4 {{key:+}}` |
| **Grouping Rule (Multiplication)** | $(\text{Length} \times \text{Width}) \times \text{Height}$ in any order | Stacking 3D layers of unit cubes | [Chapter 4](04-operations-skip-counting.md) | `2 {{key:ENTER}} 3 {{key:×}} 4 {{key:×}}` |
| **Split-Apart Rule** | $4 \times (10 + 3) = (4 \times 10) + (4 \times 3)$ | Splitting a 4-color tile rectangle along a color seam | [Chapter 4](04-operations-skip-counting.md) | `10 {{key:ENTER}} 3 {{key:+}} 4 {{key:×}}` |
| **Zero and One Rules** | Adding $0$ or multiplying by $1$ leaves a number unchanged | Adding zero tiles; taking 1 group of tiles | [Chapter 4](04-operations-skip-counting.md) | `7 {{key:ENTER}} 0 {{key:+}}` $\to 7$; `7 {{key:ENTER}} 1 {{key:×}}` $\to 7$ |
| **Division with Remainder Check** | $\text{Total} = (\text{Divisor} \times \text{Quotient}) + \text{Remainder}$ | Sharing counters equally into cups with leftovers | [Chapter 4](04-operations-skip-counting.md) | `29 {{key:ENTER}} 4 {{key:÷R}}` $\to$ Remainder `1` in $Y$, Quotient `7` in $X$ |
| **GCF and LCM Partner Rule** | $\text{GCF} \times \text{LCM} = \text{First Number} \times \text{Second Number}$ | Comparing Prime Factor Studio towers side by side | [Chapter 7](07-data-probability-primes.md) | `12 {{key:ENTER}} 18 {{key:GCF}} 12 {{key:ENTER}} 18 {{key:LCM}} {{key:×}}` $\to 216$ |
| **Fraction-to-Decimal Bridge** | $\text{Top Number} \div \text{Bottom Number} = \text{Decimal}$ | Comparing Fraction Towers to the $1\text{-Whole}$ tower | [Chapter 5](05-fractions-decimals-ratios.md) | `3 {{key:ENTER}} 4 {{key:÷}}` $\to 0.75$ |

---

### Two-Dimensional Perimeter & Area Word Rules

The table below summarizes 2D flat shape rules in plain words alongside their chapter links and SC-6 RPN keystroke sequences:

| Flat Shape | Word Rule | Chapter Link | SC-6 RPN Keystroke Sequence | Stack Shelves Used |
|:---|:---|:---|:---|:---:|
| **Square (Perimeter)** | $\text{Perimeter} = 4 \times \text{Side}$ | [Chapter 6](06-geometry-surface-area.md) | `[Side] {{key:ENTER}} 4 {{key:×}}` | $Y, X$ |
| **Square (Area)** | $\text{Area} = \text{Side} \times \text{Side}$ | [Chapter 6](06-geometry-surface-area.md) | `[Side] {{key:x²}}` | $X$ |
| **Rectangle (Perimeter)** | $\text{Perimeter} = 2 \times (\text{Length} + \text{Width})$ | [Chapter 6](06-geometry-surface-area.md) | `[Length] {{key:ENTER}} [Width] {{key:+}} 2 {{key:×}}` | $Y, X$ |
| **Rectangle (Area)** | $\text{Area} = \text{Length} \times \text{Width}$ | [Chapter 6](06-geometry-surface-area.md) | `[Length] {{key:ENTER}} [Width] {{key:RECT}}` | $Y, X$ |
| **Triangle (Perimeter)** | $\text{Perimeter} = \text{Side 1} + \text{Side 2} + \text{Side 3}$ | [Chapter 6](06-geometry-surface-area.md) | `[Side 1] {{key:ENTER}} [Side 2] {{key:+}} [Side 3] {{key:+}}` | $Z, Y, X$ |
| **Triangle (Area)** | $\text{Area} = (\text{Base} \times \text{Height}) \div 2$ | [Chapter 6](06-geometry-surface-area.md) | `[Base] {{key:ENTER}} [Height] {{key:×}} 2 {{key:÷}}` | $Y, X$ |
| **Parallelogram (Area)** | $\text{Area} = \text{Base} \times \text{Height}$ | [Chapter 6](06-geometry-surface-area.md) | `[Base] {{key:ENTER}} [Height] {{key:×}}` | $Y, X$ |
| **Trapezoid (Area)** | $\text{Area} = (\text{Top} + \text{Bottom}) \div 2 \times \text{Height}$ | [Chapter 6](06-geometry-surface-area.md) | `[Top] {{key:ENTER}} [Bottom] {{key:+}} 2 {{key:÷}} [Height] {{key:×}}` | $Z, Y, X$ |
| **Circle (Circumference)** | $\text{Distance Around} = \pi \times \text{Width (Diameter)}$ | [Chapter 6](06-geometry-surface-area.md) | `[Diameter] {{key:π}} {{key:×}}` | $Y, X$ |
| **Circle (Area)** | $\text{Area} = \pi \times \text{Radius} \times \text{Radius}$ | [Chapter 6](06-geometry-surface-area.md) | `[Radius] {{key:x²}} {{key:π}} {{key:×}}` | $Y, X$ |

---

### Flat Shapes on the Stack

To see how Shelves $T, Z, Y,$ and $X$ update step by step when measuring flat shapes, let's trace five classic two-dimensional shapes on the stack. Suppose you start with a **triangle** whose base is $14\text{ cm}$ and height is $9\text{ cm}$. Because any triangle is half of a bounding rectangle, the triangle word rule tells us that $\text{Area} = (\text{Base} \times \text{Height}) \div 2 = (14 \times 9) \div 2 = 63\text{ cm}^2$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `14` | 0 | 0 | 0 | 14 | Enter the $14\text{ cm}$ triangle base onto Shelf $X$ |
| `{{key:ENTER}}` | 0 | 0 | 14 | 14 | Copy the $14\text{ cm}$ base up onto Shelf $Y$ |
| `9` | 0 | 0 | 14 | 9 | Enter the $9\text{ cm}$ height onto Shelf $X$ |
| `{{key:×}}` | 0 | 0 | 0 | 126 | Multiply base by height ($14 \times 9 = 126\text{ cm}^2$ rectangle) |
| `2` | 0 | 0 | 126 | 2 | Type 2 to halve the rectangle; $126$ lifts to Shelf $Y$ |
| `{{key:÷}}` | 0 | 0 | 0 | 63 | Divide by 2 for the triangle area: **63 cm²** |

Notice how you first multiply $14 \times 9 = 126$ for the full bounding rectangle, and then type `2` and tap `{{key:÷}}` to slice that rectangle in half: $126 \div 2 = 63$.

What if the top of the shape isn't a sharp point, but a flat roof—making a **trapezoid** with a top width of $8\text{ in}$, a bottom width of $14\text{ in}$, and a height of $6\text{ in}$? Averaging the top and bottom widths first gives the middle width ($(8 + 14) \div 2 = 11\text{ in}$), and multiplying by the height gives $\text{Area} = (\text{Top} + \text{Bottom}) \div 2 \times \text{Height} = 11 \times 6 = 66\text{ sq in}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `8` | 0 | 0 | 0 | 8 | Enter the $8\text{ in}$ top width onto Shelf $X$ |
| `{{key:ENTER}}` | 0 | 0 | 8 | 8 | Copy $8\text{ in}$ up onto Shelf $Y$ |
| `14` | 0 | 0 | 8 | 14 | Enter the $14\text{ in}$ bottom width onto Shelf $X$ |
| `{{key:+}}` | 0 | 0 | 0 | 22 | Add top and bottom widths ($8 + 14 = 22\text{ in}$) |
| `2` | 0 | 0 | 22 | 2 | Type 2 to average the two widths |
| `{{key:÷}}` | 0 | 0 | 0 | 11 | Divide by 2 for the middle width ($11\text{ in}$) |
| `6` | 0 | 0 | 11 | 6 | Enter the $6\text{ in}$ straight-up height |
| `{{key:×}}` | 0 | 0 | 0 | 66 | Multiply middle width by height: **66 sq in** |

Why does averaging the top and bottom widths turn any trapezoid into an equivalent rectangle? If you snip off the two slanted triangular wings on the left and right sides of the trapezoid at the halfway height mark and flip them upside down into the top corners, the slanted sides lock together into a straight-sided **$11\text{ in} \times 6\text{ in}$ rectangle** with zero leftover scraps.

When straight edges curve into a circle—such as a **circular splash pad** with a radius of $3.5\text{ m}$—imagine slicing the circle into thin pie wedges and alternating them teeth-together like a zipper. As the wedges get thinner, they form a nearly flat rectangle whose height is the radius ($r$) and whose width is half the circumference ($\pi \times r$). Squaring the radius first (`3.5 {{key:x²}}` $\to 12.25\text{ m}^2$, the area of a $3.5\text{ m} \times 3.5\text{ m}$ corner square) and scaling by `{{key:π}}` ($\approx 3.1415926$) yields $\text{Area} = \pi \times \text{Radius} \times \text{Radius} = \pi \times 3.5^2 \approx 38.48451\text{ m}^2$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `3.5` | 0 | 0 | 0 | 3.5 | Enter the $3.5\text{ m}$ radius onto Shelf $X$ |
| `{{key:x²}}` | 0 | 0 | 0 | 12.25 | Square the radius ($3.5 \times 3.5 = 12.25\text{ m}^2$) |
| `{{key:π}}` | 0 | 0 | 12.25 | 3.1415926 | Enter $\pi$; $12.25$ lifts to Shelf $Y$ |
| `{{key:×}}` | 0 | 0 | 0 | 38.484510 | Multiply by $\pi$ for circle area: **38.48 m²** |

Notice how squaring the radius first (`{{key:x²}}`) turns a 1D spoke length ($3.5\text{ m}$) into a 2D corner square ($12.25\text{ m}^2$) on Ground Shelf $X$, and tapping `{{key:π}} {{key:×}}` scales that single radius-square by slightly more than three to fill all four quadrants of the circle.

Whenever we want the distance around the outside of a shape instead of the space inside it, we walk its boundary perimeter in 1D length units. Around a **rectangular garden** of length $14\text{ m}$ and width $9\text{ m}$, walking down one long side and across one short side covers an L-shaped half-lap ($14 + 9 = 23\text{ m}$). Doubling that half-lap covers all four sides without having to type each measurement twice, giving $\text{Perimeter} = 2 \times (\text{Length} + \text{Width}) = 2 \times 23 = 46\text{ m}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `14` | 0 | 0 | 0 | 14 | Enter the $14\text{ m}$ garden length onto Shelf $X$ |
| `{{key:ENTER}}` | 0 | 0 | 14 | 14 | Copy $14\text{ m}$ up onto Shelf $Y$ |
| `9` | 0 | 0 | 14 | 9 | Enter the $9\text{ m}$ garden width onto Shelf $X$ |
| `{{key:+}}` | 0 | 0 | 0 | 23 | Add length and width for the $23\text{ m}$ half-lap |
| `2` | 0 | 0 | 23 | 2 | Type 2 to double the half-lap |
| `{{key:×}}` | 0 | 0 | 0 | 46 | Multiply by 2 for the full perimeter: **46 m** |

And to find how far a $24\text{-inch}$ **bicycle wheel** rolls along the pavement in one full turn ($\text{Circumference} = \pi \times 24$), typing `24 {{key:π}} {{key:×}}` on the stack immediately displays **$75.39822\text{ inches}$** per revolution—showing that every wheel travels a little more than three times its own diameter on every spin.

---

### Three-Dimensional Solid Volume & Surface Area Word Rules

| 3D Solid Shape | Volume Word Rule | Total Surface Area Word Rule | Chapter Link | SC-6 Volume Keystrokes |
|:---|:---|:---|:---|:---|
| **Cube** | $\text{Volume} = \text{Side} \times \text{Side} \times \text{Side}$ | $\text{Surface Area} = 6 \times (\text{Side} \times \text{Side})$ | [Chapter 6](06-geometry-surface-area.md) | `[Side] {{key:ENTER}} 3 {{key:yˣ}}` |
| **Rectangular Box (Prism)** | $\text{Volume} = \text{Length} \times \text{Width} \times \text{Height}$ | Add all $6$ rectangular faces ($2\text{ Top/Bottom} + 2\text{ Front/Back} + 2\text{ Sides}$) | [Chapter 6](06-geometry-surface-area.md) | `[Length] {{key:ENTER}} [Width] {{key:×}} [Height] {{key:×}}` |
| **Triangular Tent (Prism)** | $\text{Volume} = (\text{Base} \times \text{Height} \div 2) \times \text{Length}$ | Add the $2$ triangle ends plus the $3$ rectangular side panels | [Chapter 6](06-geometry-surface-area.md) | `[Base] {{key:ENTER}} [Height] {{key:×}} 2 {{key:÷}} [Length] {{key:×}}` |
| **Cylinder (Can)** | $\text{Volume} = (\pi \times \text{Radius}^2) \times \text{Height}$ | $\text{Curved Side} \ (2 \times \pi \times \text{Radius} \times \text{Height}) + 2\text{ Circle Ends} \ (2 \times \pi \times \text{Radius}^2)$ | [Chapter 6](06-geometry-surface-area.md) | `[Radius] {{key:x²}} {{key:π}} {{key:×}} [Height] {{key:×}}` |

---

### Solid Shapes on the Stack

When a flat base is lifted upward into three dimensions, the stack lets you find both volume and surface area without parentheses or scratch paper. Every prism or cylinder volume works like stacking identical coasters or pancakes: first calculate the flat 2D footprint on the floor, and then multiply by the height to sweep that footprint upward into 3D space. Consider a **cylindrical farm storage silo** with a radius of $4\text{ m}$ and a height of $10\text{ m}$. Its volume stacks the circular base area across the height: $(\pi \times 4^2) \times 10 = 160\pi \approx 502.6548\text{ m}^3$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `4` | 0 | 0 | 0 | 4 | Enter the $4\text{ m}$ silo radius onto Shelf $X$ |
| `{{key:x²}}` | 0 | 0 | 0 | 16 | Square the radius ($4 \times 4 = 16$) |
| `{{key:π}}` | 0 | 0 | 16 | 3.1415926 | Enter $\pi$; $16$ lifts to Shelf $Y$ |
| `{{key:×}}` | 0 | 0 | 0 | 50.265482 | Multiply for the circular floor area ($50.27\text{ m}^2$) |
| `10` | 0 | 0 | 50.265482 | 10 | Enter the $10\text{ m}$ silo height |
| `{{key:×}}` | 0 | 0 | 0 | 502.654824 | Stack the circle floor by height: **502.65 m³** |

What if we want to paint that same silo's outer shell and both circular lids? If you unroll the curved metal wall of a cylinder like a soup-can label, it flattens into a rectangle whose width is the circle's circumference ($2 \times \pi \times 4\text{ m} \approx 25.13\text{ m}$) and whose height is $10\text{ m}$. On the stack, you can calculate that unrolled side wrapper first ($251.33\text{ m}^2$) and let automatic stack lift hold it safely on Waiting Shelf $Y$ while you build the two circular end caps ($2 \times \pi \times 4^2 \approx 100.53\text{ m}^2$) on Ground Shelf $X$, then unite both parts with `{{key:+}}` for $\approx 351.8584\text{ m}^2$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `2` | 0 | 0 | 0 | 2 | Start the $2\pi r h$ curved side wall |
| `{{key:π}} {{key:×}}` | 0 | 0 | 0 | 6.2831853 | Multiply $2 \times \pi \approx 6.2832$ |
| `4 {{key:×}}` | 0 | 0 | 0 | 25.132741 | Multiply by the $4\text{ m}$ radius ($25.13\text{ m}$ rim) |
| `10 {{key:×}}` | 0 | 0 | 0 | 251.327412 | Multiply by $10\text{ m}$ height ($251.33\text{ m}^2$ side wall) |
| `2` | 0 | 0 | 251.327412 | 2 | Start the 2 circular lids; side wall lifts to Shelf $Y$ |
| `{{key:π}} {{key:×}}` | 0 | 0 | 251.327412 | 6.2831853 | Multiply $2 \times \pi$ on Shelf $X$ |
| `4 {{key:x²}} {{key:×}}` | 0 | 0 | 251.327412 | 100.530964 | Multiply by $4^2$ for both lids ($100.53\text{ m}^2$) |
| `{{key:+}}` | 0 | 0 | 0 | 351.858376 | Add side wall and lids: **351.86 m²** total surface |

The same layer-stacking idea works for rectangular boxes and cubes. Imagine filling the bottom of a **square-base storage box** ($6\text{ cm}$ by $6\text{ cm}$ base, $8\text{ cm}$ tall) with $1\text{ cm}$ unit cubes: squaring the $6\text{ cm}$ side covers the bottom floor with a single layer of $36$ unit cubes ($36\text{ cm}^2$), and multiplying by $8$ stacks eight identical layers on top of one another ($36 \times 8 = 288\text{ cm}^3$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `6 {{key:x²}}` | 0 | 0 | 0 | 36 | Square the $6\text{ cm}$ side for the $36\text{ cm}^2$ floor |
| `8` | 0 | 0 | 36 | 8 | Enter the $8\text{ cm}$ height; $36$ lifts to Shelf $Y$ |
| `{{key:×}}` | 0 | 0 | 0 | 288 | Multiply floor area by height: **288 cm³** volume |

And when all three dimensions match—such as a **$9\text{ cm}$ cube**—it holds $\text{Side}^3 = 9^3 = 729\text{ cm}^3$ of space inside (`9 {{key:ENTER}} 3 {{key:yˣ}}` $\to \mathbf{729}\text{ cm}^3$) and is wrapped by six identical $9 \times 9$ square faces (`9 {{key:x²}} 6 {{key:×}}` $\to \mathbf{486}\text{ cm}^2$).

---

## Complete Unit Conversions Directory

Why does a meter divide cleanly by $10$, $100$, and $1,000$, while an English mile contains the seemingly strange number of $5,280\text{ feet}$? Every conversion number in the tables below carries a piece of human history. In ancient Rome, soldiers measured long roads by counting $1,000$ double-paces (*mille passus*, where one left-right stride was about $5\text{ Roman feet}$), giving a Roman mile of $5,000\text{ feet}$. Centuries later in England, farmers measured plowed fields in *furlongs* ("furrow-longs" of $660\text{ feet}$, the distance an ox team could pull a plow before resting). In 1593, Queen Elizabeth I passed a law making the statute mile equal to **8 furlongs** ($8 \times 660 = \mathbf{5,280\text{ feet}}$) so land surveyors and road builders could share one common scale.

Before the French Revolution of the 1790s, almost every town in Europe used a different foot or pound. Between 1792 and 1799, French scientists decided to base a new universal unit—the **meter** (from the Greek *metron*, "measure")—on the planet Earth itself, defining $1\text{ meter}$ as one ten-millionth of the distance from the North Pole to the Equator. Two astronomers, Jean-Baptiste Delambre and Pierre Méchain, spent seven years trekking across mountains and church bell towers from Dunkirk to Barcelona with brass surveying triangles to measure the Earth's curve and cast the first platinum meter bar.

Even the numbers on a kitchen or weather thermometer tell an engineering story. In 1724, instrument maker Daniel Gabriel Fahrenheit mixed ice, water, and salt to reach the coldest laboratory temperature he could make ($0^\circ\text{F}$), and placed freezing pure water at **$32^\circ\text{F}$** and human body temperature near $96^\circ\text{F}$ so the $64\text{-degree}$ gap between them could be halved six times in a row ($64 = 2^6$) when marking glass thermometer tubes! Eighteen years later, in 1742, Swedish astronomer Anders Celsius divided the span between freezing and boiling water into **$100$ equal steps** (originally putting $0^\circ$ at boiling and $100^\circ$ at freezing, until botanist Carl Linnaeus flipped the scale upright so warmer days had higher numbers).

Every unit conversion on the SC-6 works two ways: for the most common everyday measurements (grams/ounces, kilograms/pounds, centimeters/inches, milliliters/fluid ounces, liters/gallons, and Celsius/Fahrenheit), you can use the **one-tap shifted conversion keys** on Rows 5–6 of the keypad (`{{key:f}}` for Metric, `{{key:g}}` for U.S. Customary), or you can multiply and divide directly by the exact conversion factor on the stack so you can see the rate at work.

### Length Conversions

| From Unit | To Unit | Conversion Number | SC-6 Forward Keystrokes | Reverse (Back Again) |
|:---|:---|:---:|:---|:---:|
| **Inches (in)** | **Centimeters (cm)** | $2.54$ | `[in] {{key:ENTER}} 2.54 {{key:×}}` | $\div 2.54$ |
| **Feet (ft)** | **Inches (in)** | $12.0$ | `[ft] {{key:ENTER}} 12 {{key:×}}` | $\div 12$ |
| **Feet (ft)** | **Meters (m)** | $0.3048$ | `[ft] {{key:ENTER}} {{key:.}} 3048 {{key:×}}`| $\div 0.3048$ |
| **Yards (yd)** | **Feet (ft)** | $3.0$ | `[yd] {{key:ENTER}} 3 {{key:×}}` | $\div 3$ |
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
| **Square Yards (sq yd)**| **Square Feet (sq ft)**| $9.0$ | `[sq yd] {{key:ENTER}} 9 {{key:×}}` | $\div 9$ |
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
| **Cups (c)** | **Fluid Ounces (fl oz)**| $8.0$ | `[c] {{key:ENTER}} 8 {{key:×}}` | $\div 8$ |
| **Pints (pt)** | **Cups (c)** | $2.0$ | `[pt] {{key:ENTER}} 2 {{key:×}}` | $\div 2$ |
| **Quarts (qt)** | **Pints (pt)** | $2.0$ | `[qt] {{key:ENTER}} 2 {{key:×}}` | $\div 2$ |
| **Gallons (gal US)**| **Quarts (qt)** | $4.0$ | `[gal] {{key:ENTER}} 4 {{key:×}}` | $\div 4$ |
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
| **Weeks (wk)** | **Days (d)** | $7.0$ | `[wk] {{key:ENTER}} 7 {{key:×}}` |
| **Years (yr standard)**| **Days (d)** | $365.0$ | `[yr] {{key:ENTER}} 365 {{key:×}}` |
| **Years (yr leap)**| **Days (d)** | $366.0$ | `[yr] {{key:ENTER}} 366 {{key:×}}` |

To count how many seconds tick by in a full 24-hour day, enter `{{res:sc6_appendix_c_formulas_and_conversions_seq_07:keys}}` to reach **$86,400\text{ seconds}$**.

---

### Temperature Conversions (Fahrenheit and Celsius)

Because water freezes at $32^\circ\text{F}$ ($0^\circ\text{C}$) and boils at $212^\circ\text{F}$ ($100^\circ\text{C}$), converting between Fahrenheit and Celsius uses two simple word rules:

$$\text{Celsius} = (\text{Fahrenheit} - 32) \times 5 \div 9 \qquad \text{Fahrenheit} = (\text{Celsius} \times 9 \div 5) + 32$$

| Conversion | Word Rule | SC-6 Step-by-Step Keystrokes (or One-Tap Key) |
| :--- | :--- | :--- |
| **Fahrenheit to Celsius** | $(\text{Fahrenheit} - 32) \times 5 \div 9$ | `[Temp F] {{key:ENTER}} 32 {{key:-}} 5 {{key:×}} 9 {{key:÷}}` (or `[Temp F] {{key:▸°C}}`) |
| **Celsius to Fahrenheit** | $(\text{Celsius} \times 9 \div 5) + 32$ | `[Temp C] {{key:ENTER}} 9 {{key:×}} 5 {{key:÷}} 32 {{key:+}}` (or `[Temp C] {{key:▸°F}}`) |

Here is how normal human body temperature ($98.6^\circ\text{F}$) converts to Celsius step by step on the stack:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `98.6` | 0 | 0 | 0 | 98.6 | Enter normal body temperature ($98.6^\circ\text{F}$) |
| `{{key:ENTER}}` | 0 | 0 | 98.6 | 98.6 | Copy $98.6$ up onto Shelf $Y$ |
| `32` | 0 | 0 | 98.6 | 32 | Enter freezing-point offset ($32^\circ\text{F}$) |
| `{{key:-}}` | 0 | 0 | 0 | 66.6 | Subtract 32 ($98.6 - 32 = 66.6$) |
| `5` | 0 | 0 | 66.6 | 5 | Enter numerator 5 of the $5/9$ scale factor |
| `{{key:×}}` | 0 | 0 | 0 | 333.0 | Multiply $66.6 \times 5 = 333.0$ |
| `9` | 0 | 0 | 333.0 | 9 | Enter denominator 9 of the $5/9$ scale factor |
| `{{key:÷}}` | 0 | 0 | 0 | 37.0 | Divide $333.0 \div 9 =$ **37.0°C** |

Normal human body temperature is **$37.0^\circ\text{C}$** (or in one tap on the SC-6 keypad, `98.6 {{key:▸°C}}` $\to$ `37.00`).

---

### Chaining Multi-Step Unit Conversions on the Stack

When a real-world measurement needs two conversion steps in a row, the stack lets you chain them without parentheses or scratch paper. For a **marathon footrace** ($26.2\text{ miles} \to \text{kilometers} \to \text{meters}$), since $1\text{ mile} = 1.609344\text{ kilometers}$ and $1\text{ kilometer} = 1,000\text{ meters}$, multiplying $26.2 \times 1.609344$ first gives $42.164813\text{ km}$ and multiplying by $1,000$ converts to meters:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `26.2` | 0 | 0 | 0 | 26.2 | Enter marathon distance ($26.2\text{ miles}$) |
| `{{key:ENTER}}` | 0 | 0 | 26.2 | 26.2 | Copy $26.2$ up onto Shelf $Y$ |
| `1.609344` | 0 | 0 | 26.2 | 1.609344 | Enter kilometers per mile ($1.609344$) |
| `{{key:×}}` | 0 | 0 | 0 | 42.164813 | Multiply for marathon in kilometers ($42.165\text{ km}$) |
| `1000` | 0 | 0 | 42.164813 | 1000 | Enter $1,000\text{ meters per kilometer}$ |
| `{{key:×}}` | 0 | 0 | 0 | 42164.81280 | Multiply for marathon in meters: **42,164.81 m** |

Ground Shelf $X$ shows the full Olympic marathon distance in meters: **$42,164.81\text{ meters}$**.

Next, consider an **airliner cruising at $36,000\text{ ft}$** ($36,000\text{ ft} \to \text{meters} \to \text{kilometers}$). Using $1\text{ foot} = 0.3048\text{ meters}$, we multiply $36,000 \times 0.3048$ to get meters and immediately divide by $1,000$ for kilometers:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `36000` | 0 | 0 | 0 | 36000 | Enter cruising altitude ($36,000\text{ ft}$) |
| `{{key:ENTER}}` | 0 | 0 | 36000 | 36000 | Copy $36,000$ up onto Shelf $Y$ |
| `.3048` | 0 | 0 | 36000 | 0.3048 | Enter meters per foot ($0.3048\text{ m/ft}$) |
| `{{key:×}}` | 0 | 0 | 0 | 10972.8 | Multiply to get altitude in meters ($10,972.8\text{ m}$) |
| `1000` | 0 | 0 | 10972.8 | 1000 | Enter $1,000\text{ meters per kilometer}$ |
| `{{key:÷}}` | 0 | 0 | 0 | 10.9728 | Divide by 1,000 for kilometers: **10.97 km** |

Cruising height is **$10,972.8\text{ meters}$**, or **$10.97\text{ km}$** above sea level.

What about comparing **family car fuel mileage** ($35.0\text{ Miles per Gallon} \to \text{Liters per 100 km}$)? Dividing the conversion constant $235.215$ by the Miles per Gallon ($\text{Liters per 100 km} = 235.215 \div \text{MPG}$) flips American mileage into metric fuel consumption:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `235.215` | 0 | 0 | 0 | 235.215 | Enter the fuel-economy constant ($235.215$) |
| `{{key:ENTER}}` | 0 | 0 | 235.215 | 235.215 | Copy $235.215$ up onto Shelf $Y$ |
| `35` | 0 | 0 | 235.215 | 35 | Enter fuel rating ($35\text{ MPG}$) onto Shelf $X$ |
| `{{key:÷}}` | 0 | 0 | 0 | 6.720429 | Divide $235.215 \div 35 =$ **6.72 L/100 km** |

A car rated at $35\text{ MPG}$ burns **$6.72\text{ liters of fuel per 100 kilometers}$**.

Finally, we can test a **snowy winter morning temperature** ($14^\circ\text{F} \to -10^\circ\text{C} \to 14^\circ\text{F}$) by converting $14^\circ\text{F}$ into Celsius and then running the inverse steps right on the stack to return to $14^\circ\text{F}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `14` | 0 | 0 | 0 | 14 | Enter winter morning temperature ($14^\circ\text{F}$) |
| `{{key:ENTER}}` | 0 | 0 | 14 | 14 | Copy $14$ up onto Shelf $Y$ |
| `32` | 0 | 0 | 14 | 32 | Enter freezing-point offset ($32^\circ\text{F}$) |
| `{{key:-}}` | 0 | 0 | 0 | -18 | Subtract 32 ($14 - 32 = -18^\circ\text{F}$ below freezing) |
| `5` | 0 | 0 | -18 | 5 | Enter numerator 5 |
| `{{key:×}}` | 0 | 0 | 0 | -90 | Multiply $-18 \times 5 = -90$ |
| `9` | 0 | 0 | -90 | 9 | Enter denominator 9 |
| `{{key:÷}}` | 0 | 0 | 0 | -10 | Divide $-90 \div 9 =$ **-10°C** |
| `9 {{key:×}} 5 {{key:÷}}` | 0 | 0 | 0 | -18 | Reverse the scale factor ($-10 \times 9 \div 5 = -18$) |
| `32 {{key:+}}` | 0 | 0 | 0 | 14 | Add 32 to return to **14°F** |

Here $14^\circ\text{F}$ equals **$-10^\circ\text{C}$** (ten degrees below freezing), and reversing the steps returns **$14^\circ\text{F}$**.

---

## Prime Number Catalog & Factorization Directory

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

### The $\sqrt{N}$ Sieve Stop Rule & Eratosthenes' Shadow Stick

In [Chapter 7](07-data-probability-primes.md), you used the **Sieve of Eratosthenes** to cross out multiples of $2, 3, 5,$ and $7$ on a $1\text{--}100$ grid. Notice the remarkable shortcut that happens when you extend Eratosthenes' sieve all the way to **$200$** in the 46-prime reference table above: **once you finish crossing out multiples of $2, 3, 5, 7, 11,$ and $13$, every single remaining uncrossed number up to $200$ is guaranteed to be prime!**

Why don't you have to test $17, 19, 23,$ or any larger prime? Because whenever a composite number $N$ factors into two numbers $A \times B = N$, the two factors cannot *both* be larger than $\sqrt{N}$—if both were larger than $\sqrt{N}$, their product would already exceed $N$! That means every composite number up to $200$ must have at least one prime factor less than or equal to $\sqrt{200}$. On your SC-6, tapping `200 {{key:√x}}` displays **`14.142136`**, and the largest prime below $14.142136$ is **$13$** (since the smallest composite number built purely from $17$ or larger primes is $17 \times 17 = 289$, well past $200$). That exact **$\sqrt{N}$ Stop Rule** is how the SC-6 `{{key:PRIME}}` and `{{key:FACT}}` keys test even a four-digit number like $1,999$ in a tiny fraction of a second: since `1999 {{key:√x}}` is $44.71$, the processor checks only the 14 primes up to $43$ and immediately flashes `PRIME`!

Eratosthenes of Cyrene (chief librarian of the great Library of Alexandria around 240 BCE) used that same eye for clean mathematical bounds to pull off one of the greatest measurements in science history: **measuring the distance around the entire planet Earth using nothing but a stick's shadow!** Travelers told him that at noon on the summer solstice in the southern city of Syene (modern Aswan), the sun shone straight down to the bottom of a deep water well with zero shadow ($0^\circ$). On that exact same day in Alexandria—$800\text{ kilometers}$ due north—Eratosthenes stood a vertical measuring stick in the ground and used a protractor wheel like your **$360^\circ$ Unit Circle Volvelle** to measure the sun's shadow angle at **$7.2^\circ$**.

Because a full circle around the curved Earth is $360^\circ$, Eratosthenes divided the full circle by his shadow angle (`360 {{key:ENTER}} 7.2 {{key:÷}}` $\to \mathbf{50}$) to discover that the $800\text{ km}$ road between Syene and Alexandria was exactly $\frac{1}{50}$ of the way around the world! Multiplying that fraction by $800\text{ km}$ right on the stack (`360 {{key:ENTER}} 7.2 {{key:÷}} 800 {{key:×}}`) gives **$40,000\text{ kilometers}$**—matching modern satellite measurements of Earth's circumference ($40,008\text{ km}$ around the poles) to within two-tenths of one percent!

---

### Quick Divisibility Rules with SC-6 Checks

Before testing a big number with `{{key:PRIME}}`, you can spot small factors right away using these mental math rules:

| Divide By | Quick Mental Rule | How to Check on Your SC-6 (`{{key:÷R}}`) | Example |
|:---:|:---|:---|:---|
| **2** | Last digit is even ($0, 2, 4, 6, 8$). | `[Number] {{key:ENTER}} 2 {{key:÷R}}` (Remainder in $Y$ is `0`) | $84 \div 2 = 42$ with Remainder $0$ |
| **3** | Add the digits; the sum divides evenly by 3. | Add the digits on the stack, then press `3 {{key:÷R}}` | $153 \to 1+5+3=9$, and $9 \div 3 = 3$ |
| **4** | Last two digits divide evenly by 4. | `[Last 2 Digits] {{key:ENTER}} 4 {{key:÷R}}` | $3,728 \to 28 \div 4 = 7$ (Remainder $0$) |
| **5** | Last digit is 0 or 5. | Look at the ones digit on the screen. | $95$ ends in $5$ ($95 \div 5 = 19$) |
| **6** | Passes both the 2-test (even) and the 3-test. | Check that it is even and its digits add to a multiple of 3. | $78$ is even, and $7+8=15$ ($78 \div 6 = 13$) |
| **8** | Last three digits divide evenly by 8. | `[Last 3 Digits] {{key:ENTER}} 8 {{key:÷R}}` | $5,128 \to 128 \div 8 = 16$ (Remainder $0$) |
| **9** | Add the digits; the sum divides evenly by 9. | Add the digits on the stack, then press `9 {{key:÷R}}` | $423 \to 4+2+3=9$, and $9 \div 9 = 1$ |
| **10** | Last digit is 0. | Look at the ones digit on the screen. | $340$ ends in $0$ ($340 \div 10 = 34$) |

---

### Ten Classic Prime Factorizations

Every composite whole number greater than 1 breaks down into a unique product of prime numbers—just like a tower built from your **Prime Factor Studio** blocks. The table below shows 10 classic composite numbers, their prime factor blocks, and how to multiply the prime blocks back together on your SC-6:

| Composite Number | Prime Factor Blocks | SC-6 `{{key:FACT}}` Screen Output | RPN Keystrokes to Multiply Them Back |
|:---:|:---:|:---|:---|
| **72** | $2^3 \times 3^2$ | `2³ × 3²` | `2 {{key:ENTER}} 3 {{key:yˣ}} 3 {{key:x²}} {{key:×}}` $\to 72$ |
| **84** | $2^2 \times 3 \times 7$ | `2² × 3 × 7` | `2 {{key:x²}} 3 {{key:×}} 7 {{key:×}}` $\to 84$ |
| **180** | $2^2 \times 3^2 \times 5$ | `2² × 3² × 5` | `2 {{key:x²}} 3 {{key:x²}} {{key:×}} 5 {{key:×}}` $\to 180$ |
| **252** | $2^2 \times 3^2 \times 7$ | `2² × 3² × 7` | `2 {{key:x²}} 3 {{key:x²}} {{key:×}} 7 {{key:×}}` $\to 252$ |
| **360** | $2^3 \times 3^2 \times 5$ | `2³ × 3² × 5` | `2 {{key:ENTER}} 3 {{key:yˣ}} 3 {{key:x²}} {{key:×}} 5 {{key:×}}` $\to 360$ |
| **504** | $2^3 \times 3^2 \times 7$ | `2³ × 3² × 7` | `2 {{key:ENTER}} 3 {{key:yˣ}} 3 {{key:x²}} {{key:×}} 7 {{key:×}}` $\to 504$ |
| **720** | $2^4 \times 3^2 \times 5$ | `2⁴ × 3² × 5` | `2 {{key:ENTER}} 4 {{key:yˣ}} 3 {{key:x²}} {{key:×}} 5 {{key:×}}` $\to 720$ |
| **1,000** | $2^3 \times 5^3$ | `2³ × 5³` | `2 {{key:ENTER}} 3 {{key:yˣ}} 5 {{key:ENTER}} 3 {{key:yˣ}} {{key:×}}` $\to 1000$ |
| **1,024** | $2^{10}$ | `2¹⁰` | `2 {{key:ENTER}} 10 {{key:yˣ}}` $\to 1024$ |
| **1,729** | $7 \times 13 \times 19$ | `7 × 13 × 19` | `7 {{key:ENTER}} 13 {{key:×}} 19 {{key:×}}` $\to 1729$ |

*Why Master Builders & Astronomers Love "Highly Composite" Numbers (`72`, `84`, `180`, `360`, `720`):* Look closely at the prime factor blocks of the first seven numbers in the table above. In 1915, **Srinivasa Ramanujan** (whose $1,729 = 7 \times 13 \times 19$ Taxicab Number from [Chapter 7](07-data-probability-primes.md) caps the bottom row) published a landmark study on what he named **Highly Composite Numbers**—numbers packed with small prime factors ($2, 3, 5,$ and $7$) so they can be divided evenly in more ways than any smaller number! You can actually calculate *how many* whole-number divisors any number has straight from the exponents in its `{{key:FACT}}` output: **add $1$ to each prime's exponent and multiply them together**.

For example, your **1-Whole Fraction Tower** stands **$84\text{ mm}$** tall ($2^2 \times 3^1 \times 7^1$). Adding $1$ to each exponent gives $(2+1) \times (1+1) \times (1+1) = 3 \times 2 \times 2 = \mathbf{12\text{ divisors}}$ ($1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84$), allowing halves, thirds, fourths, sixths, sevenths, and twelfths to land on exact whole-millimeter heights. A **$360^\circ$ circle** ($2^3 \times 3^2 \times 5^1$) is even richer: adding $1$ to each exponent (`3 {{key:ENTER}} 1 {{key:+}} 2 {{key:ENTER}} 1 {{key:+}} {{key:×}} 1 {{key:ENTER}} 1 {{key:+}} {{key:×}}` $\to 4 \times 3 \times 2$) reveals **$24$ exact divisors**, so a $360^\circ$ circle splits into clean whole degrees whether you divide it into $2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120,$ or $180$ equal wedges! Doubling $360$ to **$720$** ($2^4 \times 3^2 \times 5^1$) yields $(4+1) \times (2+1) \times (1+1) = 5 \times 3 \times 2 = \mathbf{30\text{ divisors}}$ (which is why two full turns of a $360^\circ$ wheel or the total interior angles of a 6-sided hexagon equal $720^\circ$). And look at **`1,000`** ($2^3 \times 5^3$) beside **`1,024`** ($2^{10}$): metric decimal blocks (`1,000`) use three $2$-blocks and three $5$-blocks ($(3+1) \times (3+1) = 16$ divisors), whereas computer memory chips (`1,024` bytes in a traditional kilobyte) stack ten pure $2$-blocks (`2 {{key:ENTER}} 10 {{key:yˣ}}` $\to 1,024$, with $10 + 1 = 11$ power-of-two divisors).

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

### Why "Goldbach's Comet" Has High Ridges and Low Valleys

In Chapter 7, you met **Christian Goldbach's** famous 1742 letter to **Leonhard Euler**—observing that every even number greater than $2$ can be written as the sum of two prime numbers ($4 = 2 + 2$, $6 = 3 + 3$, $8 = 3 + 5$, $10 = 3 + 7 = 5 + 5$). When mathematicians plot *how many different prime pairs* add up to each even number, the dots streak across the page like a glowing comet tail (**Goldbach's Comet**) split into low valleys and high ridges.

Why do powers of $2$ like **$8$** ($1$ pair: $3 + 5$), **$16$** ($2$ pairs: $3 + 13, 5 + 11$), **$32$** ($2$ pairs: $3 + 29, 13 + 19$), and **$64$** ($5$ pairs) sit in the lowest valleys? Because powers of $2$ have no odd prime factors at all (they are not divisible by $3, 5,$ or $7$), nearly half of the odd primes below them are blocked from pairing up when their partners land on multiples of $3$ or $5$! Conversely, multiples of $6$ ($2 \times 3$) and $30$ ($2 \times 3 \times 5$) like **$18$** ($2$ pairs), **$30$** ($3$ pairs), **$42$** ($4$ pairs), **$60$** ($6$ pairs), and **$90$** ($9$ pairs) ride the top ridge of the comet: because multiples of $6$ already divide evenly by both $2$ and $3$, subtracting any prime greater than $3$ from a multiple of $6$ is guaranteed *never* to land on a multiple of $2$ or $3$, giving every prime a much higher chance of meeting a prime partner!

You can test any even number on Goldbach's Comet right on your SC-6 by picking a prime candidate with `{{key:PRIME}}`, subtracting it from your even number, and tapping `{{key:PRIME}}` on the partner:

| Even Number | How Many Prime Pairs? | All Prime Pairs That Add to This Even Number | Why It Sits Low or High on Goldbach's Comet |
|:---:|:---:|:---|:---|
| **4** | **1 pair** | $2 + 2$ | Only even number that uses the even prime $2$ |
| **8** | **1 pair** | $3 + 5$ | Power of $2$ ($2^3$): only one odd prime pair works |
| **10** | **2 pairs** | $3 + 7,\; 5 + 5$ | Includes the twin-center pair $5 + 5$ |
| **16** | **2 pairs** | $3 + 13,\; 5 + 11$ | Power of $2$ ($2^4$): sits on the bottom edge of the comet |
| **24** | **3 pairs** | $5 + 19,\; 7 + 17,\; 11 + 13$ | Multiple of $6$: three symmetric prime pairs around $12$ |
| **30** | **3 pairs** | $7 + 23,\; 11 + 19,\; 13 + 17$ | Primorial ($2 \times 3 \times 5$): every non-3, non-5 prime pairs up! |
| **32** | **2 pairs** | $3 + 29,\; 13 + 19$ | Power of $2$ ($2^5$): drops back down to just $2$ pairs |
| **36** | **4 pairs** | $5 + 31,\; 7 + 29,\; 13 + 23,\; 17 + 19$ | Square multiple of $6$: four distinct prime pairs |
| **48** | **5 pairs** | $5 + 43,\; 7 + 41,\; 11 + 37,\; 17 + 31,\; 19 + 29$ | Multiple of $6$: climbs to five prime pairs |
| **60** | **6 pairs** | $7 + 53,\; 13 + 47,\; 17 + 43,\; 19 + 41,\; 23 + 37,\; 29 + 31$ | Champion under $60$ ($2^2 \times 3 \times 5$): six distinct prime pairs! |
| **64** | **5 pairs** | $3 + 61,\; 5 + 59,\; 11 + 53,\; 17 + 47,\; 23 + 41$ | Power of $2$ ($2^6$): fewer pairs than $60$ even though $64 > 60$ |
| **100** | **6 pairs** | $3 + 97,\; 11 + 89,\; 17 + 83,\; 29 + 71,\; 41 + 59,\; 47 + 53$ | Six pairs of two-digit primes add to an exact $100$ |

---

### Perfect Numbers & Giant Factor Challenges

A **Perfect Number** is a special whole number whose smaller factors add up to the number itself. Look at the first four perfect numbers:

| Perfect Number | Prime Recipe | Smaller Factors Added Together |
|:---:|:---:|:---|
| **6** | $2 \times 3$ | $1 + 2 + 3 = \mathbf{6}$ |
| **28** | $4 \times 7$ | $1 + 2 + 4 + 7 + 14 = \mathbf{28}$ |
| **496** | $16 \times 31$ | $1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 = \mathbf{496}$ |
| **8,128** | $64 \times 127$ | $1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + \dots = \mathbf{8,128}$ |

You can build the third perfect number ($496$) right on the stack by following Euclid's ancient recipe: multiply $2^4$ ($16$) by the prime number $2^5 - 1$ ($31$) to reach $16 \times 31 = 496$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `2 {{key:ENTER}}` | 0 | 0 | 2 | 2 | Enter base 2 and copy onto Shelf $Y$ |
| `5 {{key:yˣ}}` | 0 | 0 | 0 | 32 | Raise $2^5 = 32$ |
| `1 {{key:-}}` | 0 | 0 | 0 | 31 | Subtract 1 for Mersenne candidate $2^5 - 1 = 31$ |
| `{{key:PRIME}}` | 0 | 0 | 0 | 31 | Screen flashes `PRIME` to confirm that $31$ is a prime number |
| `2 {{key:ENTER}}` | 0 | 31 | 2 | 2 | Enter base 2; $31$ lifts to Shelf $Z$ |
| `4 {{key:yˣ}}` | 0 | 0 | 31 | 16 | Raise $2^4 = 16$; $31$ drops to Shelf $Y$ |
| `{{key:×}}` | 0 | 0 | 0 | 496 | Multiply $31 \times 16 =$ **496** (the third perfect number) |

The display lands on **$496$**, the third perfect number. That same curiosity about giant powers of two led to one of history's most famous division checks: in 1640, Pierre de Fermat guessed that $2^{32} + 1 = 4,294,967,297$ was a prime number, and for nearly a hundred years no one could factor it—until Leonhard Euler proved in 1732 that $641$ divides into it evenly with zero remainder:
$$4,294,967,297 = 641 \times 6,700,417$$
You can test Euler's discovery right on your SC-6 by keying in `{{res:sc6_appendix_c_formulas_and_conversions_seq_08:keys}}`, which lands cleanly on **$6,700,417.00$** with no decimal remainder.

---

## Everyday Rates, Money & Shopping Word Rules

Whether you are comparing unit prices in a grocery store aisle, computing average speed on a family road trip, or adding sales tax at a register, the SC-6 stack keeps your starting numbers visible at every step:

| Everyday Math Task | What You Know | Word Rule | SC-6 Keystroke Pattern |
|:---|:---|:---|:---|
| **Speed (Unit Rate)** | Distance, Time | $\text{Distance} \div \text{Time}$ | `[Distance] {{key:ENTER}} [Time] {{key:÷}}` |
| **Travel Distance** | Speed, Time | $\text{Speed} \times \text{Time}$ | `[Speed] {{key:ENTER}} [Time] {{key:×}}` |
| **Travel Time** | Distance, Speed | $\text{Distance} \div \text{Speed}$ | `[Distance] {{key:ENTER}} [Speed] {{key:÷}}` |
| **Unit Price (Best Buy)** | Total Cost, Count | $\text{Total Cost} \div \text{Count}$ | `[Total Cost] {{key:ENTER}} [Count] {{key:÷}} {{key:$}}` |
| **Density of an Object** | Mass (g), Volume ($\text{cm}^3$) | $\text{Mass} \div \text{Volume}$ | `[Mass] {{key:ENTER}} [Volume] {{key:÷}}` |
| **Percent of a Number** | Whole, Percent | $\text{Whole} \times (\text{Percent} \div 100)$ | `[Whole] {{key:ENTER}} [Percent] {{key:%}}` |
| **Percent Change** | Starting, Ending | $(\text{Ending} - \text{Starting}) \div \text{Starting} \times 100$ | `[Starting] {{key:ENTER}} [Ending] {{key:%CHG}}` |

### Why Distance, Unit Price & Density All Share One Rule

Look closely at the first five rows of that table and you will spot a wonderful shortcut: **Speed** ($\text{miles} \div \text{hours}$), **Unit Price** ($\text{dollars} \div \text{ounces}$), and **Density** ($\text{grams} \div \text{cm}^3$) are all the exact same mathematical idea! Every time you see the word **"per"** in everyday life—*miles per hour*, *dollars per pound*, *heartbeats per minute*, or *grams per cubic centimeter*—the word **"per"** simply means **"divide the total on Shelf $Y$ by the number of units on Shelf $X$"** (`{{key:÷}}`):

- **Finding the Best Buy in the Grocery Store Aisle:** Suppose a $12\text{-ounce}$ box of cereal costs $\$4.56$, while a giant $18\text{-ounce}$ family box of the same cereal costs $\$6.30$. Which box gives you more cereal for each dollar?
  1. Key in the first box's price and ounces (`4.56 {{key:ENTER}} 12 {{key:÷}}`): Shelf $X$ shows **`0.38`** ($38\text{ cents per ounce}$).
  2. Now key in the family box right on top (`6.30 {{key:ENTER}} 18 {{key:÷}}`): Shelf $X$ shows **`0.35`** ($35\text{ cents per ounce}$), while the first box's **`0.38`** waits right above it on Shelf $Y$ so you can compare both unit prices side by side! Subtracting `{{key:-}}` confirms that the family box saves **$3\text{ cents per ounce}$** ($\$0.54$ saved across the $18\text{-ounce}$ box).
- **Combining Road-Trip Speed and Clock Time (`{{key:→HMS}}`):** Suppose your family is driving $210\text{ miles}$ to a state park at a steady highway speed of $60\text{ miles per hour}$. Dividing `210 {{key:ENTER}} 60 {{key:÷}}` gives **`3.5` hours** in decimal time—and one tap of **`{{key:→HMS}}`** (`{{key:g}}` then `{{key:🕒}}`) translates `3.5` decimal hours directly into **`3.3000`** (**$3\text{ hours, } 30\text{ minutes}$**)!

### Adding Tax, Tips & Discounts in One Tap

Because `{{key:%}}` on the SC-6 computes the percentage on Ground Shelf $X$ while keeping your original dollar amount untouched on Shelf $Y$, you never have to retype a price to add sales tax or subtract a sale discount:

| Money Task | Word Rule | SC-6 Keystroke Pattern |
|:---|:---|:---|
| **Simple Interest Earned** | $\text{Starting Money} \times \text{Yearly Rate \%} \times \text{Years}$ | `[Money] {{key:ENTER}} [Rate] {{key:%}} [Years] {{key:×}} {{key:$}}` |
| **Sales Tax Amount** | $\text{Price} \times \text{Tax Rate \%}$ | `[Price] {{key:ENTER}} [Tax Rate] {{key:%}} {{key:$}}` |
| **Total Price with Tax** | $\text{Price} + \text{Sales Tax}$ | `[Price] {{key:ENTER}} [Tax Rate] {{key:%}} {{key:+}} {{key:$}}` |
| **Discount Saved** | $\text{Regular Price} \times \text{Discount \%}$ | `[Price] {{key:ENTER}} [Discount] {{key:%}} {{key:$}}` |
| **Sale Price After Discount** | $\text{Regular Price} - \text{Discount}$ | `[Price] {{key:ENTER}} [Discount] {{key:%}} {{key:-}} {{key:$}}` |
| **Restaurant Tip ($18\%$)**| $\text{Bill} \times 18\%$ | `[Bill] {{key:ENTER}} 18 {{key:%}} {{key:$}}` |
| **Splitting a Bill Equally** | $(\text{Bill} + \text{Tip}) \div \text{Diners}$ | `[Bill] {{key:ENTER}} 18 {{key:%}} {{key:+}} [Diners] {{key:÷}} {{key:$}}` |

Even two-step store sales—like taking a **$20\%$ coupon** off a $\$45.00$ backpack and then adding **$8\%$ sales tax** at the register—flow in one unbroken chain without writing down a single intermediate number:
1. Key in `45 {{key:ENTER}} 20 {{key:%}}` to see the **`9.00`** discount on Shelf $X$ while `45` waits on Shelf $Y$, then tap **`{{key:-}}`** to land on the **`36.00`** sale price.
2. Now type `8 {{key:%}}` (`2.88` tax on Shelf $X$, `36.00` sale price on Shelf $Y$), tap **`{{key:+}}`**, and tap **`{{key:$}}`** to round cleanly to **`38.88`** at the checkout counter!

When money stays in a savings account for several years, the interest itself starts earning interest! For example, to watch a $\$500$ savings account grow at $4\%$ interest compounded yearly for $3$ years, multiply $\$500$ by $1.04$ three times ($1.04^3 \times 500 = 562.43$ dollars):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `1.04` | 0 | 0 | 0 | 1.04 | Enter yearly growth multiplier ($1 + 0.04 = 1.04$) |
| `{{key:ENTER}}` | 0 | 0 | 1.04 | 1.04 | Copy $1.04$ up onto Shelf $Y$ |
| `3` | 0 | 0 | 1.04 | 3 | Enter 3 years of compounding |
| `{{key:yˣ}}` | 0 | 0 | 0 | 1.124864 | Raise $1.04^3 = 1.124864$ |
| `500` | 0 | 0 | 1.124864 | 500 | Enter starting savings ($\$500$); multiplier lifts to $Y$ |
| `{{key:×}}` | 0 | 0 | 0 | 562.43 | Multiply by $\$500$ for **\$562.43** total savings |

After $3$ years, the account holds **$\$562.43$** total savings ($\$62.43$ in interest earned).

---

## Annotated Bibliography & Primary Mathematical Sources

Every numbered reference across this volume links to a classic book, historical source, or mathematical study in the **Annotated Bibliography** below. If a story or puzzle in this book sparked your curiosity, several unforgettable books from our bibliography are waiting for you at your school or public library. For puzzle lovers and aspiring math magicians, **Martin Gardner's** *The Colossal Book of Short Puzzles and Problems* {{cite:gardner1959}} and **George Pólya's** *How to Solve It* {{cite:polya1945}} show how drawing a picture, testing a smaller case, or working backward can crack seemingly impossible riddles. For young engineers and machine builders, **David Macaulay's** *The Way Things Work Now* {{cite:macaulay2016}} and **Randall Munroe's** *What If?* {{cite:munroe2014}} open up gears, levers, pendulums, and wild physics questions with playful illustrations that pair naturally with Chapter 6 and Chapter 9, while **Simon Singh's** *The Code Book* {{cite:singh1997}} tells the true history of secret ciphers from ancient Rome to modern RSA prime-number internet security.

To explore the history and beauty of everyday math, look for **Steven Strogatz's** *The Joy of x* {{cite:strogatz2012}}, **Jordan Ellenberg's** *How Not to Be Wrong* {{cite:ellenberg2014}}, and **Georges Ifrah's** *The Universal History of Numbers* {{cite:ifrah2000}}, which trace how human beings use place value, fractions, geometry, and probability to understand the natural world. And for parents, teachers, and math coaches, **Jerome Bruner's** *Toward a Theory of Instruction* {{cite:bruner1966}}, **Liping Ma's** *Knowing and Teaching Elementary Mathematics* {{cite:ma1999}}, and **Zoltan Dienes's** *Building Up Mathematics* {{cite:dienes1960}} explain why building with physical blocks before moving to visual diagrams and symbols builds deep, lasting mathematical confidence.

{{bibliography:sc6}}

---

For detailed hands-on lesson plans implementing these rules in classroom workshop stations, see [Appendix B: Teacher Lesson Plans & Station Guide](appendix-b-teacher-lesson-plans.md). For 3D-printing and cardstock cutouts of the hands-on block kits, see [Appendix A: Hands-On Block Studio Guide & How We Built StackCalc](appendix-a-manipulative-blueprints.md).
