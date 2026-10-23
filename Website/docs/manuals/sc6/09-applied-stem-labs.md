---
title: "Chapter 9: Applied Elementary STEM & Maker Labs"
description: "Hands-on maker engineering on the SC-6: 12 comprehensive projects covering 3D printing dynamics, layer slicing, clock pendulums, solar ovens, catapults, botany growth, culinary scaling, gear trains, hydraulics, drone power, and solar panels."
---

# Chapter 9: Applied Elementary STEM & Maker Labs

## The Kitchen-Table Invention Studio: Turning Numbers into Moving Machines, 3D Prints, and Science Labs

Picture the kitchen table on a rainy Saturday morning. In the center sits a spool of corn-based PLA filament, a pair of digital vernier calipers, a stopwatch, a length of string, the 3D-printed math blocks you have used throughout this book, and the solid, tactile form of your StackCalc SC-6 calculator. Outside, the rain taps against the glass; inside, the table is alive with invention.

For centuries, schoolchildren were told that mathematics was something that lived exclusively in the flat, monochrome world of paper workbooks—abstract symbols marching across ruled margins under the threat of a red grading pen. But mathematics was never meant to be trapped on paper. Mathematics is the hidden operating system of physical reality. It is the invisible scaffolding that allows a 3D printer nozzle heated to $215^\circ\text{C}$ to slice models into paper-thin $0.20\text{ mm}$ layers as it fabricates your **Counting Tiles** and **Planetary Geared Clock**. It is the steady rhythm discovered by Galileo Galilei in 1638 {{cite:galilei1638}} that keeps a grandfather clock pendulum swinging back and forth in equal beats across centuries.

When you pick up the SC-6 in your workshop, you aren't just doing schoolwork—you are an engineer, a builder, and an inventor. In a hands-on maker studio, real mathematics is verified by whether your creation actually works—whether the 3D-printed planetary gears mesh smoothly, the 3D-printed layers stack to the exact millimeter, and the pendulum keeps steady time. With **Stack Math**, your numbers become as physical as the string pendulum and 3D-printed blocks on your desk: you push lengths and weights onto the stack, tap your operations, and watch your ideas turn into real machines that whir, tick, and run!

{{blocks:clock_classroom_hero|Classroom Maker Space Clock: Precision 3D-Printed Geared Engineering}}

---

{{res:sc6_led_resistor:screenshot|Slicing a 1 cm (3 cm - 2 cm) 3D-printed block top into 0.02 cm layers = 50 layers}}

**How 3D Printers Slice Models into Thin Layers:** Look at the SC-6 screen above. Suppose a 3D-printed block is $3\text{ cm}$ tall in total, and its solid base takes up the bottom $2\text{ cm}$. Subtracting `{{key:3}} {{key:ENTER}} {{key:2}} {{key:-}}` leaves $1\text{ cm}$ of height for the top section. When the 3D printer slices that $1\text{ cm}$ top section into horizontal plastic layers that are each $0.02\text{ cm}$ ($0.20\text{ mm}$) thick, dividing by `.02 {{key:÷}}` shows that the printer nozzle must lay down **`50` layers**!

## Building Real Things: From Your 3D-Printed Manipulative Studios to the Number Stack

Grounded in Jerome Bruner's hands-on learning research {{cite:bruner1966}}, every maker lab in this chapter follows a four-step engineering loop that connects your physical **StackCalc Manipulative Studios** directly to the 4-register stack:
1. **Physical Workshop (Build & Measure It):** Measure 3D printer filament with vernier calipers as you print a **Math Dominoes** or **Counting Tile** tray, turn the gears of your **Planetary Geared Clock** (`{{key:🕒}}`, `{{key:▸HR}}`, `{{key:▸HMS}}`), dial launch and solar tilt angles on your **Unit Circle Volvelle**, or stack **84 mm Fraction Towers** (`{{key:a ᵇ/c}}`, `{{key:a:b}}`) beside your measuring cups.
2. **Sketches and Data Logs (Draw It):** Record your measurements, layer sketches, and trial tables in your lab notebook.
3. **The Number Stack (Calculate It):** Push your measurements onto the SC-6 stack ($X, Y, Z, T$), chaining geometry keys (`{{key:x²}}`, `{{key:√x}}`, `{{key:π}}`), statistical accumulators (`{{key:Σ+}}`, `{{key:Σx}}`, `{{key:x̄}}`, `{{key:MAD}}`, `{{key:CLΣ}}`), percentage and currency keys (`{{key:%}}`, `{{key:%CHG}}`, `{{key:$}}`), and `{{key:LASTX}}` checks without parentheses.
4. **Maker Validation (Test It):** Snap the 3D-printed parts together, slice the 3D print, swing the pendulum, and verify that physical reality matches your stack prediction.

---

## 3D Printing Filament Mass, Infill & Spool Cost Estimation

Have you ever wondered how a 3D printer's slicing software knows—down to the gram and the penny—how much plastic your design will use before the nozzle even heats up? The secret is hidden right on the filament spool! Unwind a few centimeters of plastic filament and look closely at it: that flexible strand is really a long, thin **cylinder** (like a giant strand of plastic spaghetti). If you know the tiny circle area of its cut end and you know how many centimeters of strand the printer will unspool, multiplying $\text{Circle Area} \times \text{Length}$ tells you the exact cubic centimeters of plastic your print will use!

Standard 3D printing filament has a width (diameter) of $1.75\text{ mm}$, which means its radius from the center to the edge is half of that: $0.875\text{ mm}$, or $0.0875\text{ cm}$:
- **Circle Area of the Filament Strand:** $\text{Circle Area} = \pi \times \text{Radius} \times \text{Radius} = \pi \times (0.0875\text{ cm})^2 \approx 0.0240528\text{ cm}^2$
- **Plastic Volume:** $\text{Volume} = \text{Circle Area} \times \text{Length in cm}$
- **Part Weight (PLA):** $\text{Weight in grams} = \text{Volume} \times 1.24\text{ grams per cm}^3$
- **Part Cost:** $\text{Cost} = \text{Weight in grams} \times (\text{Spool Price} \div 1,000\text{ grams})$

{{blocks:dominoes_studio_stealth_black|Double-Six Tactile Dominoes Set in Matte Slate}}

### Estimating a 500 cm Print Model for Your Dominoes Studio Tray
Suppose your slicing software reports that printing a custom replacement lid or divider tray for your **Math Dominoes** (or a **Counting Tile** organizer) will pull $500\text{ cm}$ ($5.0\text{ meters}$) of filament off the spool. Your maker space uses a $\$20.00$ spool of Midnight Navy PLA ($1,000\text{ grams}$). Let's follow the plastic from strand to finished price tag in one continuous stack flow!

First, we find the circle area of the filament ($\pi \times \text{Radius}^2$) by entering the radius in centimeters (`{{key:.}} 0875`), squaring it with `{{key:x²}}` ($\mathbf{0.00765625\text{ cm}^2}$), and multiplying by $\pi$ via `{{key:π}} {{key:×}}` ($\approx \mathbf{0.0240528\text{ cm}^2}$). Second, while that tiny circle area sits on Register $X$, we stretch it along the $500\text{ cm}$ filament strand (`500 {{key:×}}`) to get a plastic volume of $\mathbf{12.02641\text{ cm}^3}$. Third, because every cubic centimeter of PLA weighs $1.24\text{ grams}$, multiplying by `1.24 {{key:×}}` reveals that our finished studio tray weighs **`14.91275`** ($\mathbf{14.91\text{ grams}}$). Finally, to price the part from a $\$20 / 1,000\text{ g}$ spool, keying `{{res:sc6_09_applied_stem_labs_seq_01:keys}}` places the unit cost of $\$0.02\text{ per gram}$ on Register $X$ while keeping your $14.91\text{ g}$ tray weight in Register $Y$, pressing `{{key:×}}` computes **`0.298255`**, and tapping `{{key:$}}` formats the price tag as **`$0.30`**:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `.0875` | 0 | 0 | 0 | $0.0875$ |
| `{{key:x²}}` | 0 | 0 | 0 | $0.007656$ |
| `{{key:π}} {{key:×}}` | 0 | 0 | 0 | $0.024053$ |
| `500 {{key:×}}` | 0 | 0 | 0 | $12.02641$ |
| `1.24 {{key:×}}` | 0 | 0 | 0 | $14.91275$ |
| `20 {{key:ENTER}}` | 0 | $14.91275$ | $20.00000$ | 20 |
| `1000 {{key:÷}}` | 0 | 0 | $14.91275$ | $0.02$ |
| `{{key:×}}` | 0 | 0 | 0 | $0.298255$ |
| `{{key:$}}` | 0 | 0 | 0 | $0.30$ |

---

### Infill Percentage Optimization
Why don't 3D printers make every block $100\%$ solid plastic inside? Just like honeybees build lightweight hexagonal combs inside a hive, a 3D printer builds strong outer walls and fills the inside with a $15\%$ honeycomb lattice! By setting the slicer to $15\%$ infill inside a $100\text{ cm}^3$ trophy base, how much filament weight and money do you save?
- **Solid Block Weight:** $100\text{ cm}^3 \times 1.24\text{ g/cm}^3 = 124.0\text{ g}$.
- **Outer Shell Weight:** $20\text{ cm}^3$ solid outer walls ($20 \times 1.24 = 24.8\text{ g}$).
- **Inside Infill Weight:** $80\text{ cm}^3$ inside space filled to $15\%$: $80 \times 0.15 \times 1.24 = 14.88\text{ g}$.
- **Total Hollow-Infill Weight:** $24.8 + 14.88 = 39.68\text{ g}$.
- **Weight Saved:** $124.0 - 39.68 = 84.32\text{ g}$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `124` | 0 | 0 | 0 | 124 |
| `{{key:ENTER}}` | 0 | 0 | 124 | 124 |
| `24.8` | 0 | 0 | 124 | $24.8$ |
| `{{key:ENTER}}` | 0 | 124 | $24.8$ | $24.8$ |
| `80` | 0 | $124.0$ | $24.8$ | 80 |
| `{{key:ENTER}}` | $124.0$ | $24.8$ | 80 | 80 |
| `0.15 {{key:×}}` | $124.0$ | $124.0$ | $24.8000$ | 12 |
| `1.24 {{key:×}}` | $124.0$ | $124.0$ | $24.8000$ | $14.88$ |
| `{{key:+}}` | 124 | 124 | $124.0$ | $39.68$ |
| `{{key:-}}` | 124 | 124 | 124 | $84.32$ |
| `.02 {{key:×}}` | 124 | 124 | 124 | $1.6864$ |
| `{{key:$}}` | 124 | 124 | 124 | $1.69$ |

---

## Batch Classroom Kit Production & Manufacturing Economics

What does it take to run your own miniature toy factory at home or in a classroom maker lab? When you print a complete 24-piece set of **Counting Tiles**, you aren't just using plastic from the spool—you are also paying for the electricity that keeps the printer's nozzle and build plate warm for hours! In this project, you step into the shoes of a manufacturing engineer to budget both the filament and the electricity for a full student kit.
- **How 3D Printers Slice $0.20\text{ mm}$ Layers:** A 3D printer builds objects from the bottom up by extruding thin horizontal layers of melted PLA plastic, each just $0.20\text{ mm}$ thick. To print a $14.4\text{ mm}$ tall two-tier block stack, dividing `14.4 {{key:ENTER}} 0.20 {{key:÷}}` (or clearing the decimal by multiplying both numbers by $100 \implies 1,440 \div 20$) shows that the printer nozzle must trace **$72$ horizontal layers**.

### Manufacturing a Student Kit of 24 Counting Tiles
How much does the plastic cost to 3D print a complete student kit of 24 **Counting Tiles** (6 each of Coral Red, Amber Gold, Sky Cyan, and Indigo Purple)?
- Each $19.0\text{ mm} \times 19.0\text{ mm}$ interlocking tile ($7.0\text{ mm}$ visible step height, $8.85\text{ mm}$ overall with its stacking lip) uses approximately $3.1\text{ grams}$ of PLA.
- Multiplying the 24 tiles by $3.1\text{ g}$ via `{{res:sc6_09_applied_stem_labs_seq_02:keys}}` gives a total kit weight of $\mathbf{74.4\text{ grams}}$, multiplying by `.02 {{key:×}}` finds the raw plastic cost of $1.488$, and pressing `{{key:$}}` rounds the spool cost to **`$1.49`**.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `24` | 0 | 0 | 0 | 24 |
| `{{key:ENTER}}` | 0 | 0 | 24 | 24 |
| `3.1` | 0 | 0 | 24 | $3.1$ |
| `{{key:×}}` | 0 | 0 | 0 | $74.4$ |
| `{{key:.}} 02` | 0 | 0 | $74.4$ | $0.02$ |
| `{{key:×}}` | 0 | 0 | 0 | $1.488$ |
| `{{key:$}}` | 0 | 0 | 0 | $1.49$ |

---

### Electrical Operating Costs & Machine Time
Now let's check the electric bill! A classroom 3D printer uses an average electrical power of $120\text{ Watts}$ ($0.120\text{ kilowatts}$). The 24-tile Counting Tile kit requires $4.5\text{ hours}$ to print, and the local electric rate is $\$0.15\text{ per kilowatt-hour (kWh)}$:
1. Electricity Used: $0.120\text{ kW} \times 4.5\text{ hours} = 0.54\text{ kWh}$.
2. Electricity Cost: $0.54 \times \$0.15 = \$0.081$ ($\sim \$0.08$).
3. Total Production Cost (Filament + Electricity): $\$1.49 + \$0.08 = \mathbf{\$1.57}$ for the entire 24-tile kit.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:.}} 12` | 0 | 0 | 0 | $0.12$ |
| `{{key:ENTER}}` | 0 | 0 | $0.12$ | $0.12$ |
| `4.5` | 0 | 0 | $0.12$ | $4.5$ |
| `{{key:×}}` | 0 | 0 | 0 | $0.54$ |
| `{{key:.}} 15` | 0 | 0 | $0.54$ | $0.15$ |
| `{{key:×}}` | 0 | 0 | 0 | $0.081$ |
| `1.49 {{key:+}}` | 0 | 0 | 0 | $1.571$ |
| `{{key:$}}` | 0 | 0 | 0 | $1.57$ |

---

## 3D-Printer Layer Slicing & Height Checks

Have you ever seen a 3D-printed math block with a dark slate-gray base and bright gold numbers raised on top, even though the printer only has a single nozzle? Makers do this with a clever trick called a **filament color swap**: you let the printer finish the bottom base, pause the machine, load a second color of plastic, and let it print the remaining top layers! To set the pause at the exact right height, how do you know how many paper-thin $0.02\text{ cm}$ ($0.20\text{ mm}$) layers remain in the top section?

| Slicer Measurement | Example Value | What It Means |
| :--- | :--- | :--- |
| **Total Model Height** | $3.0\text{ cm}$ (or $9.0\text{ cm}$) | Full height from the printer bed to the top of the block |
| **Base Height Printed** | $2.0\text{ cm}$ (or $3.2\text{ cm}$) | Bottom section already finished before the color swap |
| **Layer Thickness** | $0.02\text{ cm}$ ($0.20\text{ mm}$) | Height of each single plastic ribbon laid down by the nozzle |

### How Layer Slicing Works in Words
To find how many horizontal layers the printer needs for the top section of a model:
- **Step 1 (Remaining Height):** $\text{Remaining Height} = \text{Total Height} - \text{Base Height}$
- **Step 2 (Number of Layers):** $\text{Number of Layers} = \text{Remaining Height} \div \text{Layer Thickness } (0.02\text{ cm})$
- **Step 3 (Height Check with `{{key:LASTX}}`):** Press `{{key:LASTX}}` to bring back the $0.02\text{ cm}$ layer thickness without re-typing it, and press `{{key:×}}` to verify that $\text{Number of Layers} \times \text{Layer Thickness} = \text{Remaining Height}$!

---

### Slicing the Top Section of a 3 cm Block (`50` Layers)

Suppose you are printing a $3.0\text{ cm}$ tall counting block trophy. The bottom $2.0\text{ cm}$ base is already printed in slate gray, and you want to print the top section in gold using $0.02\text{ cm}$ layers.

First, find the remaining height ($\text{Total Height} - \text{Base Height}$) by entering the total block height (`{{key:3}} {{key:ENTER}}`) and subtracting the base height (`{{key:2}} {{key:-}}`), which leaves $\mathbf{1.0\text{ cm}}$ in Register $X$. Next, divide by the $0.02\text{ cm}$ layer thickness (`{{key:.}} 02 {{key:÷}}`): Register $X$ displays **`50.0`**, showing that the printer nozzle must lay down **`50` layers** of gold filament. Finally, to prove that $50$ layers of $0.02\text{ cm}$ each rebuild the exact $1.0\text{ cm}$ top section without typing `0.02` a second time, press `{{key:LASTX}}` (which recalls $0.02$ into Register $X$ and lifts $50.0$ into Register $Y$) and tap `{{key:×}}` to verify **`1.0`** ($50 \times 0.02\text{ cm} = \mathbf{1.0\text{ cm}}$):

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:3}} {{key:ENTER}}` | 0 | 0 | 3 | 3 |
| `{{key:2}} {{key:-}}` | 0 | 0 | 0 | 1 |
| `.02 {{key:÷}}` | 0 | 0 | 0 | 50 |
| `{{key:LASTX}}` | 0 | 0 | 50 | $0.02$ |
| `{{key:×}}` | 0 | 0 | 0 | 1 |

---

### Slicing a Taller 9.0 cm Tower Above a 3.2 cm Base (`290` Layers)
Suppose you print a $9.0\text{ cm}$ tall **Fraction Tower** holder whose solid base takes up the bottom $3.2\text{ cm}$, using $0.02\text{ cm}$ layers for the upper walls. Subtracting the base height via `{{res:sc6_09_applied_stem_labs_seq_03:keys}}` leaves $\mathbf{5.8\text{ cm}}$ of upper wall height, dividing by `{{key:.}} 02 {{key:÷}}` shows that the nozzle must trace **`290.0 layers`**, and tapping `{{key:LASTX}} {{key:×}}` immediately confirms that $290 \times 0.02\text{ cm}$ rebuilds the exact **`5.8 cm`** height.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:9}} {{key:ENTER}}` | 0 | 0 | 9 | 9 |
| `3.2 {{key:-}}` | 0 | 0 | 0 | $5.8$ |
| `.02 {{key:÷}}` | 0 | 0 | 0 | 290 |
| `{{key:LASTX}}` | 0 | 0 | 290 | $0.02$ |
| `{{key:×}}` | 0 | 0 | 0 | $5.8$ |

---

## Timing a Swinging Clock Pendulum (Finding the 10-Swing Average)

Why does a grandfather clock keep the exact same steady beat whether its swinging weight is heavy brass or light wood—and what happens to the beat if you shorten the string to one-fourth of its original length? Over four hundred years ago, a young Galileo Galilei watched a bronze lamp swinging from a high ceiling and timed it against his own pulse. He discovered an amazing law of nature: the time a pendulum takes to swing back and forth depends on the **length of the string**, not on how heavy the weight is!

Because a single swing goes by so fast that your thumb on the stopwatch might be a tenth of a second early or late, real scientists time **10 complete back-and-forth swings** in a row and divide by $10$ to find the razor-sharp average time for a single swing:
- **Time for 1 Swing:** $\text{One-Swing Time} = \text{Total Time for 10 Swings} \div 10$
- **Swings per Minute:** $\text{Swings per Minute} = 60\text{ seconds} \div \text{One-Swing Time}$

{{blocks:clock_quadrant_concept|Clock Quadrant Concept: Pendulum Escapements and Harmonic Oscillation}}

Look closely at the **Planetary Geared Clock** and its removable $90^\circ$ clock quadrants above: in a mechanical grandfather clock, a swinging pendulum releases one gear tooth on every tick, driving the $60\text{-minute}$ outer ring and $12:1$ planetary hour hand at a steady pace. By timing a string pendulum beside your Planetary Geared Clock dial, you can see how string length controls the beat of a clock!

### Timing 10 Swings of a 100 cm (1-Meter) Pendulum
You tie a washer to a string that is $100\text{ cm}$ ($1.00\text{ meter}$) long from the knot to the center of the washer. Using a stopwatch, you and your lab partner time 10 complete back-and-forth swings:
$$\text{Stopwatch time for 10 swings} = 20.1\text{ seconds}$$

To find the average time for 1 swing ($\text{Total Time} \div 10$), enter your stopwatch time (`20.1 {{key:ENTER}}`) and divide by 10 swings (`10 {{key:÷}}`), which lands on $\mathbf{2.01\text{ seconds per swing}}$ in Register $X$. Next, to see how many swings happen in 1 full minute ($60 \div \text{One-Swing Time}$), type `60`, swap Registers $X$ and $Y$ with `{{key:x⇄y}}` so $60$ sits in Register $Y$ above $2.01$ in Register $X$, and press `{{key:÷}}` to display **`29.8507`** ($\sim \mathbf{29.85\text{ swings per minute}}$, almost $30$ full swings every minute!):

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `20.1 {{key:ENTER}}` | 0 | 0 | $20.1$ | $20.1$ |
| `10 {{key:÷}}` | 0 | 0 | 0 | $2.01$ |
| `60` | 0 | 0 | $2.01$ | 60 |
| `{{key:x⇄y}}` | 0 | 0 | 60 | $2.01$ |
| `{{key:÷}}` | 0 | 0 | 0 | $29.8507$ |

---

### Testing a Shorter 25 cm Quarter-Length Pendulum
What happens if you shorten the string to $25\text{ cm}$ (one-fourth of a meter)? Most people guess it will swing four times as fast—let's test that guess with a stopwatch! When you time 10 full back-and-forth swings, it takes **$10.05\text{ seconds}$**:
1. Divide $10.05\text{ seconds}$ by $10$ swings: `10.05 {{key:ENTER}} 10 {{key:÷}}` $\longrightarrow \mathbf{1.005\text{ seconds per swing}}$ (about $1\text{ second}$ per round-trip swing!).
2. Compare the $100\text{ cm}$ swing time ($2.01\text{ s}$) to the $25\text{ cm}$ swing time ($1.005\text{ s}$): enter `2.01`, swap `{{key:x⇄y}}`, and press `{{key:÷}}` $\longrightarrow \mathbf{2.0}$. Shortening the string to one-fourth ($\frac{1}{4}$) of its original length made the pendulum swing **twice as fast** ($\sqrt{4} = 2$)!

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `10.05 {{key:ENTER}}` | 0 | 0 | $10.05$ | $10.05$ |
| `10 {{key:÷}}` | 0 | 0 | 0 | $1.005$ |
| `2.01` | 0 | 0 | $1.005$ | $2.01$ |
| `{{key:x⇄y}}` | 0 | 0 | $2.01$ | $1.005$ |
| `{{key:÷}}` | 0 | 0 | 0 | 2 |

---

## Solar Oven Thermal Tracking & Efficiency Rates

How can an ordinary cardboard box lined with kitchen aluminum foil and clear plastic wrap trap enough sunshine to melt chocolate and marshmallows into gooey s'mores on a sunny afternoon? The shiny foil bounces extra sunlight into the box, the black paper at the bottom soaks up that light as heat, and the clear plastic window plus newspaper insulation trap the warm air inside like a greenhouse! In this lab, you track how many degrees Celsius your solar oven gains every single minute.

| Thermal Measurement | Word Rule | What It Means |
| :--- | :--- | :--- |
| **Temperature Rise** | $\text{Ending Temp} - \text{Starting Temp}$ | Total degrees Celsius gained inside the solar box |
| **Heating Time** | $\text{Minutes in the Sun}$ | How many minutes the solar oven sits in sunlight |
| **Heating Speed** | $\text{Temperature Rise} \div \text{Minutes}$ | Degrees Celsius gained each minute ($^\circ\text{C/min}$) |

### Measuring Solar Heating Speed
Place your solar cooker in direct sunlight at noon. Your digital thermometer records:
- Starting Temperature at $0\text{ minutes}$: $22.5^\circ\text{C}$
- Ending Temperature at $25\text{ minutes}$: $78.0^\circ\text{C}$

Subtracting the starting temperature from the ending temperature with `{{res:sc6_09_applied_stem_labs_seq_05:keys}}` reveals a temperature rise of $\mathbf{55.5^\circ\text{C}}$, dividing by `25 {{key:÷}}` gives a heating speed of $\mathbf{2.22^\circ\text{C per minute}}$, and checking `{{key:%CHG}}` via `{{res:sc6_09_applied_stem_labs_seq_06:keys}}` confirms a $\mathbf{+246.67\%}$ thermal increase.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `78` | 0 | 0 | 0 | 78 |
| `{{key:ENTER}}` | 0 | 0 | 78 | 78 |
| `22.5` | 0 | 0 | 78 | $22.5$ |
| `{{key:-}}` | 0 | 0 | 0 | $55.5$ |
| `25` | 0 | 0 | $55.5$ | 25 |
| `{{key:÷}}` | 0 | 0 | 0 | $2.22$ |

---

### Thermal Insulation Retention Ratio
How well does your crumpled-newspaper insulation hold onto that heat when a cloud passes over? After reaching $78^\circ\text{C}$ (which is $78 - 22 = 56^\circ\text{C}$ warmer than the $22^\circ\text{C}$ shade), move your oven into the shade for 30 minutes. The thermometer reads $56^\circ\text{C}$ ($56 - 22 = 34^\circ\text{C}$ above the shade temperature):
- Total Heat Kept Inside: $\frac{56 - 22}{78 - 22} = \frac{34}{56} \approx \mathbf{60.71\%}$ kept inside.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `56` | 0 | 0 | 0 | 56 |
| `{{key:ENTER}}` | 0 | 0 | 56 | 56 |
| `22 {{key:-}}` | 0 | 0 | 0 | 34 |
| `78` | 0 | 0 | 34 | 78 |
| `{{key:ENTER}}` | 0 | 34 | 78 | 78 |
| `22 {{key:-}}` | 0 | 0 | 34 | 56 |
| `{{key:÷}}` | 0 | 0 | 0 | $0.6071$ |
| `100 {{key:×}}` | 0 | 0 | 0 | $60.71$ |

---

## Catapult Trajectory Math & Projectile Launch Analysis

When you pull back the arm of a tabletop rubber-band catapult and launch a foam ball toward a floor target, why doesn't the ball land on the exact same millimeter every single time? Tiny differences in how your finger releases the lever create a small scatter of landing spots! By holding your **Unit Circle Volvelle** (or a $90^\circ$ quadrant from your **Planetary Geared Clock**) beside the catapult arm to set an exact $45^\circ$ launch angle, you can use `{{key:Σ+}}`, `{{key:x̄}}`, and `{{key:MAD}}` to measure both your center bullseye distance and how tightly grouped your shots are.

| Catapult Measurement | What You Measure | Role in the Experiment |
| :--- | :--- | :--- |
| **Pullback Angle** | $30^\circ, 45^\circ, 60^\circ$ | The launch angle you choose before releasing the arm |
| **Landing Distance** | Measured in $\text{cm}$ along a floor tape | The distance you enter into the calculator with `{{key:Σ+}}` |

### Five-Trial Launch Average at $45^\circ$
Launch a foam ball 5 times at a $45^\circ$ pullback angle, measuring each landing distance in centimeters:
$$\text{Landing Distances}: 182\text{ cm},\ 195\text{ cm},\ 188\text{ cm},\ 201\text{ cm},\ 189\text{ cm}$$

Add each launch into the SC-6 statistical registers using `{{key:Σ+}}`:
1. Clear statistics: Press `{{key:CLΣ}}`.
2. Enter Launch 1: `182 {{key:Σ+}}` $\longrightarrow \text{Count} = 1$.
3. Enter Launch 2: `195 {{key:Σ+}}` $\longrightarrow \text{Count} = 2$.
4. Enter Launch 3: `188 {{key:Σ+}}` $\longrightarrow \text{Count} = 3$.
5. Enter Launch 4: `201 {{key:Σ+}}` $\longrightarrow \text{Count} = 4$.
6. Enter Launch 5: `189 {{key:Σ+}}` $\longrightarrow \text{Count} = 5$.
7. Find the Average (Mean): Press `{{key:x̄}}` $\longrightarrow X = \mathbf{191.00\text{ cm}}$.
8. Find the Mean Absolute Deviation ($\text{MAD}$): Press `{{key:MAD}}` $\longrightarrow X = \mathbf{5.60\text{ cm}}$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:CLΣ}}` | 0 | 0 | 0 | 0 |
| `182 {{key:Σ+}}` | 0 | 0 | 0 | $1.0000$ |
| `195 {{key:Σ+}}` | 0 | 0 | 0 | $2.0000$ |
| `188 {{key:Σ+}}` | 0 | 0 | 0 | $3.0000$ |
| `201 {{key:Σ+}}` | 0 | 0 | 0 | $4.0000$ |
| `189 {{key:Σ+}}` | 0 | 0 | 0 | $5.0000$ |
| `{{key:x̄}}` | 0 | 0 | 0 | $191.00$ |
| `{{key:MAD}}` | 0 | 0 | $191.00$ | $5.60$ |

---

### Target Ring Landing Consistency
Will your catapult shots land inside a circular floor target centered at $190\text{ cm}$ with a radius of $15\text{ cm}$ (stretching from $175\text{ cm}$ to $205\text{ cm}$)?
Since your average landing distance is $191.00\text{ cm}$ and double the Mean Absolute Deviation is $2 \times 5.60\text{ cm} = 11.20\text{ cm}$, your landing zone runs from $191 - 11.20 = 179.80\text{ cm}$ to $191 + 11.20 = 202.20\text{ cm}$. Notice the neat `{{key:LASTX}}` shortcut below: because subtracting $11.20$ automatically stores $11.20$ inside `{{key:LASTX}}`, tapping `191 {{key:LASTX}} {{key:+}}` finds the far edge without re-typing `11.20`. Every shot in this zone lands squarely inside the $175\text{ cm}$ to $205\text{ cm}$ target ring!

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `191 {{key:ENTER}}` | 0 | 0 | 191 | 191 |
| `5.60 {{key:ENTER}}` | 0 | 191 | $5.60$ | $5.60$ |
| `2 {{key:×}}` | 0 | 0 | 191 | $11.20$ |
| `{{key:-}}` | 0 | 0 | 0 | $179.80$ |
| `191` | 0 | 0 | $179.80$ | 191 |
| `{{key:LASTX}} {{key:+}}` | 0 | 0 | $179.80$ | $202.20$ |

---

## Plant Growth Tracking & Proportional Rate Analysis

Have you ever planted a bean seed in a clear cup by a sunny window and noticed that it seems to grow taller overnight? Plants grow too slowly for your eyes to see in real time, like the hour hand of a clock—but when you measure the stem height in millimeters every two days, the stack lets you calculate its exact **growth speed in millimeters per day**!

| **14-Day Botany Log** | **Day 2** | **Day 4** | **Day 6** | **Day 8** | **Day 10** | **Day 12** | **Day 14** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Stem Height ($\text{mm}$)** | $12$ | $28$ | $49$ | $74$ | $105$ | $138$ | $172$ |

### Daily Growth Speed
How fast was the sprout growing during its big middle growth spurt between Day 4 ($28\text{ mm}$) and Day 10 ($105\text{ mm}$)? Subtract the starting height from the ending height on top, subtract the starting day from the ending day on the bottom, and divide:
$$\text{Daily Growth Rate} = \frac{\text{Ending Height} - \text{Starting Height}}{\text{Ending Day} - \text{Starting Day}} = \frac{105 - 28}{10 - 4} = \frac{77\text{ mm}}{6\text{ days}} \approx \mathbf{12.83\text{ mm/day}}$$

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `105` | 0 | 0 | 0 | 105 |
| `{{key:ENTER}}` | 0 | 0 | 105 | 105 |
| `28 {{key:-}}` | 0 | 0 | 0 | 77 |
| `10` | 0 | 0 | 77 | 10 |
| `{{key:ENTER}}` | 0 | 77 | 10 | 10 |
| `{{key:4}} {{key:-}}` | 0 | 0 | 77 | 6 |
| `{{key:÷}}` | 0 | 0 | 0 | $12.83$ |

### Overall Growth Percentage
How much bigger is the Day 14 plant ($172\text{ mm}$) compared to when it first peeked above the soil on Day 2 ($12\text{ mm}$)? Using `{{key:%CHG}}` via `{{res:sc6_09_applied_stem_labs_seq_07:keys}}` reveals a total growth of $\mathbf{+1333.33\%}$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `12` | 0 | 0 | 0 | 12 |
| `{{key:ENTER}}` | 0 | 0 | 12 | 12 |
| `172` | 0 | 0 | 12 | 172 |
| `{{key:%CHG}}` | 0 | 0 | 12 | $1333.33$ |

---

## Culinary Chemistry & Baker's Percentage Recipe Scaling

Why do professional bread bakers weigh their ingredients in grams on a digital kitchen scale instead of scooping flour with measuring cups—and why do they call the flour weight **$100\%$** even when all the ingredients add up to $171.5\%$? If you scoop flour with a cup, packing the flour tightly can sneak $30$ extra grams into the bowl and make your bread dry and heavy. With **Baker's Percentages**, the flour is always the $100\%$ anchor, and every other ingredient (water, yeast, salt) is simply a percentage of the flour weight! That means you can scale a recipe to feed 4 people or 400 people in seconds—and on the SC-6, because `{{key:%}}` leaves your flour weight sitting untouched in Register $Y$, you never even have to re-type the flour weight!

| Ingredient | Baker's Percentage |
| :--- | :--- |
| **Bread Flour** | $100.0\%$ (Base Ingredient) |
| **Water (Hydration)** | $68.0\%$ |
| **Yeast** | $1.5\%$ |
| **Salt** | $2.0\%$ |
| **Total Formula** | **$171.5\%$** |

### Scaling Bread for a 28-Guest Banquet
The standard loaf requires $500\text{ grams}$ of flour and yields 4 generous servings. You need to bake bread for 28 guests ($28 \div 4 = 7\times$ scaling factor).

Multiplying the $500\text{ g}$ loaf base by $7$ with `{{res:sc6_09_applied_stem_labs_seq_08:keys}}` establishes $\mathbf{3,500\text{ grams}}$ ($3.5\text{ kg}$) of total flour; from there, `{{res:sc6_09_applied_stem_labs_seq_09:keys}}` computes $\mathbf{2,380\text{ grams}}$ ($2.38\text{ L}$) of water at $68\%$ hydration while keeping $3,500\text{ g}$ in Register $Y$, `{{res:sc6_09_applied_stem_labs_seq_10:keys}}` finds $\mathbf{70\text{ grams}}$ of salt ($2.0\%$), and `{{res:sc6_09_applied_stem_labs_seq_11:keys}}` finds $\mathbf{52.5\text{ grams}}$ of yeast ($1.5\%$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `500 {{key:ENTER}} 7 {{key:×}}` | 0 | 0 | 0 | 3500 | Total Flour base: $500\text{g} \times 7 = 3,500\text{g}$ |
| 02 | `68 {{key:%}}` | 0 | 0 | 3500 | 2380 | Water: $68\%$ of $3,500\text{g} = 2,380\text{g}$ ($Y$ holds base $3,500\text{g}$) |
| 03 | `{{key:C}} 2 {{key:%}}` | 0 | 0 | 3500 | 70 | Clear $X$ (`CLx`, lift disabled) then $2.0\%$ of $3,500\text{g} = 70\text{g}$ ($Y$ base preserved) |
| 04 | `{{key:C}} 1.5 {{key:%}}` | 0 | 0 | 3500 | 52.5 | Clear $X$ (`CLx`, lift disabled) then $1.5\%$ of $3,500\text{g} = 52.5\text{g}$ ($Y$ base preserved) |

### Scaling Down a Liquid Measuring Cup Recipe with Fraction Towers
What if a cookbook recipe uses fractional measuring cups and you want to make a smaller batch? Suppose a pancake recipe calls for $1\ \frac{3}{4}$ cups of milk to make 8 pancakes, and you are making breakfast for just two people ($2$ pancakes, or $\frac{2}{8} = \frac{1}{4}$ of the recipe). Before touching the keypad, picture this with your **84 mm Fraction Towers**: $1$ whole tower ($84\text{ mm}$) plus three $\frac{1}{4}$ blocks ($3 \times 21\text{ mm} = 63\text{ mm}$) equals seven $\frac{1}{4}$ blocks ($\frac{7}{4}$). Splitting each $\frac{1}{4}$ block into 4 equal pieces turns fourths into sixteenths ($\frac{7}{16}$)! Now verify on the SC-6:
- Enter milk: `1 {{key:.}} 3 {{key:.}} 4 {{key:ENTER}}` ($1\ \frac{3}{4} = 7/4 = 1.75$).
- Divide by 4: `{{key:4}} {{key:÷}}`.
- Result: **`7/16`** cup of milk ($0.4375$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `1 . 3 . 4` | 0 | 0 | 0 | $1\ \frac{3}{4}$ | Enter mixed fraction $1\ \frac{3}{4}$ cups ($1.75$) |
| 02 | `{{key:ENTER}}` | 0 | 0 | $1\ \frac{3}{4}$ | $1\ \frac{3}{4}$ | Push to operational stack |
| 03 | `{{key:4}} {{key:÷}}` | 0 | 0 | 0 | **`7/16`** | Divide by 4; yields exact $\frac{7}{16}$ cup ($0.4375$) |

---

## Compound Gear Train Ratios & Mechanical Advantage

How can a tiny electric motor that spins super fast—but is weak enough to stop with your finger—lift a heavy bridge or turn the hands of a clock when you connect it through a train of gears? Whenever a small gear with few teeth drives a big gear with many teeth, the big gear turns more slowly, **but pushes with multiplied force**! Better yet, when you connect two gear stages in a row (just like the hidden planetary gears inside your **Planetary Geared Clock** that step every turn of the minute hand down by $12:1$ to move the hour hand), the two stage ratios **multiply together**.

| Reduction Stage | Driver Gear | Driven Gear | Stage Ratio |
| :--- | :---: | :---: | :---: |
| **Stage 1 (Input Shaft)** | Gear A ($12\text{ teeth}$) | Gear B ($36\text{ teeth}$) | $36 \div 12 = 3:1$ |
| **Stage 2 (Middle Shaft)** | Gear C ($16\text{ teeth}$) | Gear D ($48\text{ teeth}$) | $48 \div 16 = 3:1$ |
| **Compound Output** | — | — | **$3 \times 3 = 9:1$** |

### The Gear Ratio Rule in Words
For a two-stage gear train, divide the driven teeth by the driver teeth for each stage, then multiply the two stage ratios together:
$$\text{Total Gear Ratio} = (\text{Stage 1 Driven Teeth} \div \text{Stage 1 Driver Teeth}) \times (\text{Stage 2 Driven Teeth} \div \text{Stage 2 Driver Teeth})$$
- **How Bicycle and Robot Gear Trains Work:** Four simple patterns show up in every gear train: **LCM tooth line-ups** (where a $14\text{-tooth}$ and $21\text{-tooth}$ gear line up their marked teeth every $\text{LCM} = 42$ teeth), **3-stage fraction multiplication** ($\frac{1}{2} \times \frac{2}{3} \times \frac{3}{4} = \frac{1}{4}$), **bicycle sprocket ratios** ($48 \div 16 = 3:1$), and **gear turn multipliers** (where a $3.5:1$ gear pair multiplies every big-gear turn by $3.5$, spinning the small gear $42$ times when you turn the big gear $12$ times).

### Computing Total Compound Gear Reduction
Stage 1: Gear A ($12\text{ teeth}$) drives Gear B ($36\text{ teeth}$).  
Stage 2: Gear C ($16\text{ teeth}$) drives Gear D ($48\text{ teeth}$).

Dividing the Stage 1 teeth with `{{res:sc6_09_applied_stem_labs_seq_12:keys}}` places $\mathbf{3.0}$ on the stack, dividing the Stage 2 teeth with `{{res:sc6_09_applied_stem_labs_seq_13:keys}}` places the second $\mathbf{3.0}$ ratio in Register $X$, and pressing `{{key:×}}` multiplies both stages into a **`9.0`** ($9:1$) compound reduction.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `36` | 0 | 0 | 0 | 36 |
| `{{key:ENTER}}` | 0 | 0 | 36 | 36 |
| `12 {{key:÷}}` | 0 | 0 | 0 | $3.0$ |
| `48` | 0 | 0 | $3.0$ | 48 |
| `{{key:ENTER}}` | 0 | $3.0$ | 48 | 48 |
| `16 {{key:÷}}` | 0 | 0 | $3.0$ | $3.0$ |
| `{{key:×}}` | 0 | 0 | 0 | $9.0$ |

### Calculating Output Shaft Speed
If the input electric motor spins at $1,800\text{ RPM}$ (revolutions per minute), how fast does the final output shaft spin after a $9:1$ gear reduction?
- `1800 {{key:ENTER}} 9 {{key:÷}}` $\longrightarrow X = \mathbf{200\text{ RPM}}$ (spinning $9\times$ slower, with $9\times$ the twisting push!).

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `1800 {{key:ENTER}}` | 0 | 0 | 1800 | 1800 |
| `9 {{key:÷}}` | 0 | 0 | 0 | 200 |

---

## Hydraulic Syringe Lift & Water Pressure Multiplication

How can a gentle push from your thumb on a small water-filled plastic syringe lift a heavy stack of dictionaries sitting on top of a wide syringe? Connect a narrow $1.0\text{ cm}$ syringe to a wide $3.0\text{ cm}$ syringe with clear vinyl tubing filled with water. When you push the small plunger, the water carries your pressure equally to every square centimeter of the big plunger! And why does making the big plunger $3\times$ wider multiply your force by **$9\times$** instead of $3\times$? Because a plunger is a circle, and just like you discovered in Chapter 06, scaling a shape's width by $3$ scales its **area** by $3 \times 3 = 9$!

| Syringe Part | Plunger Width | Circle Area Comparison | Force Multiplier |
| :--- | :---: | :---: | :--- |
| **Small Input Syringe** | $1.0\text{ cm}$ wide | $1\times$ base area | Your thumb push |
| **Large Output Syringe** | $3.0\text{ cm}$ wide | $(3 \div 1)^2 = 9\times$ area | $\text{Output Lift} = 9 \times \text{Thumb Push}$ |

### Finding the Force Multiplier
The small input syringe is $1.0\text{ cm}$ wide, and the large output syringe is $3.0\text{ cm}$ wide. Because a circle's area grows with the square of its width, we divide the widths and square the result:
1. Enter the large syringe width: `{{key:3}} {{key:ENTER}}`.
2. Divide by the small syringe width: `{{key:1}} {{key:÷}}`.
3. Square the width ratio: Press `{{key:x²}}`:
   - Register $X$ displays: **`9.0`** (The force multiplier is **$9\times$**).

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:3}}` | 0 | 0 | 0 | 3 |
| `{{key:ENTER}}` | 0 | 0 | 3 | 3 |
| `{{key:1}}` | 0 | 0 | 3 | 1 |
| `{{key:÷}}` | 0 | 0 | 0 | 3 |
| `{{key:x²}}` | 0 | 0 | 0 | 9 |

### Lifting a Heavy Stack of Books
If you push the small syringe with a force of $5.0\text{ Newtons}$ (about half a kilogram of thumb push) and the hydraulic syringe system multiplies your push by $9\times$, how much lifting force and book weight can the large syringe raise?
- `9 {{key:ENTER}} 5.0 {{key:×}}` $\longrightarrow X = \mathbf{45.0\text{ Newtons}}$, then `9.8 {{key:÷}}` $\longrightarrow X = \mathbf{4.59\text{ kg}}$ of lifting power (over $10\text{ pounds}$ of books lifted with one thumb!).

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `9 {{key:ENTER}}` | 0 | 0 | 9 | 9 |
| `5.0 {{key:×}}` | 0 | 0 | 0 | $45.0$ |
| `9.8 {{key:÷}}` | 0 | 0 | 0 | $4.59$ |

---

## Drone Flight Battery Endurance & Power Budget

Why do drone pilots always set a countdown timer to land when their rechargeable battery still has $20\%$ charge left—and how can you predict your exact hover time before spinning up the propellers? Think of a drone battery's **milliamp-hour ($\text{mAh}$) rating** like a fuel tank of electrical energy, and the four motors' **current draw ($\text{mA}$)** like how fast the motors sip from that tank. Leaving $20\%$ in reserve protects the battery chemistry from overheating and gives you a safe landing cushion!

| Drone Battery Measurement | Value / Word Rule |
| :--- | :--- |
| **Battery Capacity** | $850\text{ mAh}$ |
| **Hover Current Used** | $4,200\text{ mA}$ |
| **Safe Battery Rule** | Use $80\%$ ($0.80$) so $20\%$ stays in reserve to protect the battery |
| **Safe Flight Time (Minutes)** | $(\text{Battery Capacity} \times 0.80 \times 60\text{ minutes}) \div \text{Hover Current}$ |

### Calculating Safe Hover Duration
1. Enter battery capacity: `850 {{key:ENTER}}`.
2. Multiply by the $80\%$ safe battery rule: `{{key:.}} {{key:8}} {{key:×}}` $\longrightarrow X = \mathbf{680\text{ mAh usable}}$.
3. Multiply by $60\text{ minutes per hour}$: `60 {{key:×}}` $\longrightarrow X = \mathbf{40,800\text{ mA}\cdot\text{min}}$.
4. Divide by total hover current ($4,200\text{ mA}$): `4200 {{key:÷}}`:
   - Register $X$ displays: **$9.714\text{ minutes}$**.
5. Convert decimal minutes to minutes and seconds:
   - Safe flight timer: **9 minutes 43 seconds**.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `850` | 0 | 0 | 0 | 850 |
| `{{key:ENTER}}` | 0 | 0 | 850 | 850 |
| `{{key:.}} {{key:8}} {{key:×}}` | 0 | 0 | 0 | 680 |
| `60 {{key:×}}` | 0 | 0 | 0 | 40800 |
| `4200 {{key:÷}}` | 0 | 0 | 0 | $9.714$ |

### Carrying a Mini Action Camera
What happens to your flight time when you clip a $45\text{-gram}$ mini action camera onto the drone? Because the propellers have to spin faster to lift the extra weight, the hover current jumps from $4,200\text{ mA}$ to $5,500\text{ mA}$:
1. Calculate the new flight time with the camera:
   - Usable battery capacity: $680\text{ mAh}$ ($80\%$ of $850\text{ mAh}$).
   - Flight minutes: $(680 \times 60) \div 5,500 = 7.418\text{ minutes}$ ($7\text{ min } 25\text{ sec}$).
2. Calculate the percent change in flight time:
   - Starting flight time: $9.714\text{ min}$.
   - New flight time: $7.418\text{ min}$.
   - Percent change: enter `9.714`, swap `{{key:x⇄y}}`, then press `{{key:%CHG}}` $\longrightarrow \mathbf{-23.64\%}$ shorter flight time.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `680 {{key:ENTER}}` | 0 | 0 | 680 | 680 |
| `60 {{key:×}}` | 0 | 0 | 0 | 40800 |
| `5500 {{key:÷}}` | 0 | 0 | 0 | $7.418$ |
| `9.714` | 0 | 0 | $7.418$ | $9.714$ |
| `{{key:x⇄y}}` | 0 | 0 | $9.714$ | $7.418$ |
| `{{key:%CHG}}` | 0 | 0 | $9.714$ | $-23.64$ |

---

## Solar Panel Tilt Angle & Sunlight Shadow Factor

Why does a solar panel make maximum power when aimed straight at the noon sun ($0^\circ$ tilt), yet drop to exactly half power when tilted at $60^\circ$? Hold a flat book under a ceiling light and tilt it slowly: as the book tilts, the **shadow** it casts on the table directly underneath gets narrower! A solar panel only catches as much beam width of sunshine as its flat shadow—and you can read that exact **Sunlight Shadow Factor** right off your 3D-printed **Unit Circle Volvelle**! When you turn the pointer of the Unit Circle Volvelle to $0^\circ, 30^\circ, 45^\circ,$ or $60^\circ$, the horizontal window displays the shadow factor ($1.0000, 0.8660, 0.7071,$ and $0.5000$), showing the exact decimal fraction of direct sunlight caught by the tilted panel.

| Panel Tilt Angle | Sunlight Shadow Factor (from Volvelle) | Solar Power Produced ($\text{Peak Watts} \times \text{Shadow Factor}$) |
| :--- | :--- | :--- |
| **$0^\circ$ (Flat to the Sun)** | $1.0000$ | $100.0\%$ of Peak Watts |
| **$30^\circ$ Tilt** | $0.8660$ | $86.6\%$ of Peak Watts |
| **$45^\circ$ Tilt** | $0.7071$ | $70.7\%$ of Peak Watts |
| **$60^\circ$ Tilt** | $0.5000$ | $50.0\%$ of Peak Watts |

### Solar Power at Different Tilt Angles
A classroom solar panel produces $5.0\text{ Watts}$ when pointed straight at the sun ($0^\circ$ tilt). How many Watts does it produce at tilt angles of $30^\circ, 45^\circ,$ and $60^\circ$?

1. At a $30^\circ$ tilt (Volvelle shadow factor $0.866$), multiplying via `{{res:sc6_09_applied_stem_labs_seq_14:keys}}` yields $X = \mathbf{4.33\text{ Watts}}$ ($86.6\%$).
2. At a $45^\circ$ tilt (Volvelle shadow factor $0.7071$), multiplying via `{{res:sc6_09_applied_stem_labs_seq_15:keys}}` yields $X = \mathbf{3.54\text{ Watts}}$ ($70.7\%$).
3. At a $60^\circ$ tilt (Volvelle shadow factor $0.500$), multiplying via `{{res:sc6_09_applied_stem_labs_seq_16:keys}}` yields $X = \mathbf{2.50\text{ Watts}}$ ($50.0\%$).

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:5}} {{key:ENTER}}` | 0 | 0 | 5 | 5 |
| `.866 (30° factor)` | 0 | 0 | 5 | $0.8660$ |
| `{{key:×}}` | 0 | 0 | 0 | $4.33$ |

Repeating this stack multiplication across all four tilt angles produces the complete solar panel power table:

| Tilt Angle | Shadow Factor | Peak Watts | Output Power | Percent of Peak |
| :--- | :--- | :--- | :--- | :--- |
| 0° | 1.0000 | 5.00 W | 5.00 W | 100.0% |
| 30° | 0.8660 | 5.00 W | 4.33 W | 86.6% |
| 45° | 0.7071 | 5.00 W | 3.54 W | 70.7% |
| 60° | 0.5000 | 5.00 W | 2.50 W | 50.0% |

### Adding Up a Full School Day of Solar Energy
As the sun arcs across the sky from morning to afternoon, how much total electrical energy does your panel harvest over an 8-hour school day? Multiply the Watts by the hours for each part of the day and drop each subtotal into your statistical basket (`{{key:Σ+}}`):
- Morning (9:00 AM, $60^\circ$ tilt): $2.50\text{ Watts}$ for 3 hours $\longrightarrow 7.50\text{ Watt-hours}$.
- Noon (12:00 PM, $0^\circ$ tilt): $5.00\text{ Watts}$ for 2 hours $\longrightarrow 10.00\text{ Watt-hours}$.
- Afternoon (3:00 PM, $45^\circ$ tilt): $3.54\text{ Watts}$ for 3 hours $\longrightarrow 10.62\text{ Watt-hours}$.

Add up each energy period using the SC-6 statistical key `{{key:Σ+}}`:
1. Clear statistics: `{{key:CLΣ}}`.
2. Morning energy: `2.5 {{key:ENTER}} {{key:3}} {{key:×}} {{key:Σ+}}` $\longrightarrow \text{Count} = 1$ ($7.5\text{ Wh}$).
3. Noon energy: `{{key:5}} {{key:ENTER}} {{key:2}} {{key:×}} {{key:Σ+}}` $\longrightarrow \text{Count} = 2$ ($10.0\text{ Wh}$).
4. Afternoon energy: `3.54 {{key:ENTER}} {{key:3}} {{key:×}} {{key:Σ+}}` $\longrightarrow \text{Count} = 3$ ($10.62\text{ Wh}$).
5. Total Daily Energy: Press `{{key:Σx}}` $\longrightarrow X = \mathbf{28.12\text{ Watt-hours}}$.
6. Convert to Kilowatt-hours: `1000 {{key:÷}}` $\longrightarrow X = \mathbf{0.02812\text{ kWh}}$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:CLΣ}}` | 0 | 0 | 0 | 0 |
| `2.5 {{key:ENTER}} 3 {{key:×}}` | 0 | 0 | 0 | $7.5$ |
| `{{key:Σ+}}` | 0 | 0 | 0 | $1.0000$ |
| `5 {{key:ENTER}} 2 {{key:×}}` | 0 | 0 | 0 | $10.0$ |
| `{{key:Σ+}}` | 0 | 0 | 0 | $2.0000$ |
| `3.54 {{key:ENTER}} 3 {{key:×}}` | 0 | 0 | 0 | $10.62$ |
| `{{key:Σ+}}` | 0 | 0 | 0 | $3.0000$ |
| `{{key:Σx}}` | 0 | 0 | 0 | $28.12$ |
| `1000 {{key:÷}}` | 0 | 0 | 0 | $0.02812$ |

---

## Maker Lab Engineering Notebook & Measurement Checks

Real makers always check how close their physical measurements come to their design target. In this section, you learn to calculate **Percent Error** and **3D-Printing Snap-Fit Clearance** on the SC-6:

$$\text{Percent Error} = (\text{Difference from Target} \div \text{Target Value}) \times 100\%$$

### Checking Percent Error on a Precision Calibration Block
Suppose a precision 3D-printed calibration bar has a target weight of $9.80665\text{ grams}$, and your digital scale measures $9.7716\text{ grams}$. How close is your print in percent? Because subtracting $9.80665$ automatically saves $9.80665$ inside `{{key:LASTX}}`, tapping `{{key:LASTX}} {{key:÷}}` divides by the target value right away without making you type that six-digit number a second time!

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `9.7716` | 0 | 0 | 0 | $9.7716$ |
| `{{key:ENTER}}` | 0 | 0 | $9.7716$ | $9.7716$ |
| `9.80665` | 0 | 0 | $9.7716$ | $9.80665$ |
| `{{key:-}}` | 0 | 0 | 0 | $-0.03505$ |
| `{{key:LASTX}}` | 0 | 0 | $-0.03505$ | $9.80665$ |
| `{{key:÷}}` | 0 | 0 | 0 | $-0.003574$ |
| `{{key:|x|}}` | 0 | 0 | 0 | $0.003574$ |
| `100 {{key:×}}` | 0 | 0 | 0 | $0.357$ |

*(Your print is within $0.36\%$ of the target—and `{{key:LASTX}}` saved you from re-typing `9.80665`.)*

---

### 3D Printing Snap-Fit Clearance Gap
When 3D printing interlocking parts—like the stacking lips of your **Counting Tiles**, the dovetail slots of the **L-Frame Factoring Stage**, or the $42\text{ mm}$ **Gridfinity Studio Bins**—melted plastic expands slightly as it cools, so engineers leave a small clearance gap of $0.15\text{ mm}$ on each side.
If a round peg is $10.00\text{ mm}$ wide, what is the minimum hole width needed so the peg slides in smoothly?
$$\text{Hole Width} = \text{Peg Width} + (2 \times \text{Clearance Gap}) = 10.00\text{ mm} + (2 \times 0.15\text{ mm}) = 10.30\text{ mm}$$

Doubling the $0.15\text{ mm}$ side clearance and adding it to the $10.00\text{ mm}$ peg width on the stack via `10 {{key:ENTER}} .15 {{key:ENTER}} 2 {{key:×}} {{key:+}}` gives a smooth-sliding hole diameter of $\mathbf{10.30\text{ mm}}$.

---

### Digital Scale & Filament Density Check
In maker spaces, you can check whether a mystery spool of plastic is PLA or ABS by finding how much $1\text{ cm}^3$ of the plastic weighs ($\text{Grams per cm}^3 = \text{Weight in Grams} \div \text{Volume in cm}^3$):
1. A 3D-printed test cube measures $20.0\text{ mm} \times 20.0\text{ mm} \times 20.0\text{ mm}$ ($2.0\text{ cm}$ on each edge), so cubing its edge length via `{{res:sc6_09_applied_stem_labs_seq_17:keys}}` gives a volume of $X = \mathbf{8.00\text{ cm}^3}$.
2. Place the cube on a zeroed digital scale: it weighs $9.92\text{ grams}$.
3. Divide weight by volume with `9.92 {{key:x⇄y}} {{key:÷}}` to display **$1.24\text{ g/cm}^3$** in Register $X$—confirming that the mystery plastic is **authentic PLA** ($1.24\text{ g/cm}^3$), not lightweight ABS ($1.04\text{ g/cm}^3$).

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:2}} {{key:ENTER}}` | 0 | 0 | 2 | 2 |
| `{{key:2}} {{key:×}}` | 0 | 0 | 0 | 4 |
| `{{key:2}} {{key:×}}` | 0 | 0 | 0 | $8.0$ |
| `9.92` | 0 | 0 | $8.0$ | $9.92$ |
| `{{key:x⇄y}}` | 0 | 0 | $9.92$ | $8.0$ |
| `{{key:÷}}` | 0 | 0 | 0 | $1.24$ |

---

## Maker Space Machine Safety Protocols & Electrical Protection

Operating maker space equipment requires following classroom safety rules:

> **Workshop Safety & Electrical Power Rules**
> 1. **Heat Safety:** 3D printer nozzles reach $210^\circ\text{C} - 245^\circ\text{C}$; heated build plates reach $60^\circ\text{C}$. Never touch the nozzle or heated bed while printing.
> 2. **Battery Safety:** Never short-circuit rechargeable batteries or drain them past their $20\%$ reserve margin.
> 3. **Eye Protection:** Always wear safety glasses when launching tabletop catapults, testing water syringes, or clipping plastic support material.
> 4. **Fresh Air:** Always run the classroom air filter when 3D printing.

### Classroom Wall Outlet Load Check
A classroom maker lab has four 3D printers ($150\text{ W}$ each), two laptop computers ($65\text{ W}$ each), and an air filter ($80\text{ W}$) plugged into a single $120\text{-Volt}$, $15\text{-Amp}$ wall circuit.
Does the total electrical load stay safely below the $80\%$ continuous limit ($12\text{ Amps}$)?

1. Total Watts Used:
   - 4 printers: `{{res:sc6_09_applied_stem_labs_seq_18:keys}}` $\longrightarrow 600\text{ W}$.
   - 2 laptops: `{{res:sc6_09_applied_stem_labs_seq_19:keys}}` $\longrightarrow 730\text{ W}$.
   - 1 air filter: `80 {{key:+}}` $\longrightarrow \mathbf{810\text{ Watts total}}$.
2. Amps Used at $120\text{ Volts}$ ($\text{Total Watts} \div 120\text{ Volts}$):
   - `120 {{key:÷}}` $\longrightarrow X = \mathbf{6.75\text{ Amps}}$.
3. Safe $80\%$ Circuit Limit ($15\text{ Amps} \times 80\%$):
   - `{{res:sc6_09_applied_stem_labs_seq_20:keys}}` $\longrightarrow X = \mathbf{12.00\text{ Amps}}$.
4. Safety Room Remaining:
   - `{{res:sc6_09_applied_stem_labs_seq_21:keys}}` $\longrightarrow X = \mathbf{5.25\text{ Amps remaining}}$, confirming that all machines run safely with $5.25\text{ Amps}$ to spare.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `4 {{key:ENTER}} 150 {{key:×}}` | 0 | 0 | 0 | 600 |
| `2 {{key:ENTER}} 65 {{key:×}}` | 0 | 0 | 600 | 130 |
| `{{key:+}}` | 0 | 0 | 0 | 730 |
| `80 {{key:+}}` | 0 | 0 | 0 | 810 |
| `120 {{key:÷}}` | 0 | 0 | 0 | $6.75$ |
| `15 {{key:ENTER}} .80 {{key:×}}` | 0 | 0 | $6.75$ | $12.0$ |
| `{{key:x⇄y}} {{key:-}}` | 0 | 0 | 0 | $5.25$ |

---

### Lab Bench Mysteries: Layer Thickness & Pendulum Swings

- **Why Does Layer Thickness Change 3D-Printing Time So Much?** Suppose you slice a $1.0\text{ cm}$ top block section into $0.02\text{ cm}$ layers (`50` layers). If you switch your slicer to ultra-fine $0.01\text{ cm}$ layers, the printer nozzle has to trace $1.0 \div 0.01 = 100$ layers—twice as many horizontal trips across the build plate! You can even check how tiny a $0.020\text{ cm}$ layer is when squared (`{{res:sc6_09_applied_stem_labs_seq_22:keys}}` $\to 0.0004\text{ cm}^2$).
- **Why Doesn't a Heavier Pendulum Swing Faster?** A $50\text{-gram}$ steel bolt and a $5\text{-gram}$ wooden bead tied to the same $100\text{ cm}$ string both take $20.1\text{ seconds}$ to complete $10$ swings (an average of $2.01\text{ seconds}$ per swing). Gravity pulls ten times harder on the $50\text{-gram}$ bolt, but the heavier bolt is also ten times harder to get moving, so the two effects balance out completely. Only the length of the string changes the swing time!

Before you step into the four workshop investigations below, keep this quick troubleshooting checklist handy at your workbench:

| What Happened on Your Screen | Why It Happened | How to Fix It |
| :--- | :--- | :--- |
| **Squaring the full width (diameter) instead of the radius** | Forgetting to divide the circle's width by 2 before squaring. | *"Width (diameter) goes all the way across the circle; radius goes from the center to the edge. Always divide $1.75\text{ mm}$ by 2 to get radius $0.875\text{ mm}$."* |
| **Forgetting to subtract the base height before slicing layers** | Dividing the full block height by $0.02\text{ cm}$ instead of just the remaining top section. | *"Subtract the already-printed base height from the total height first (`3 ENTER 2 -`), then divide the remaining height by `.02`."* |
| **Assuming a heavier pendulum swings faster** | Thinking a heavier weight falls faster on a string. | *"A heavier weight gets pulled harder by gravity, but it is also harder to speed up. The two balance out: only the string length changes the swing time."* |
| **Scaling recipes by adding instead of multiplying** | Adding cups instead of multiplying by the batch size. | *"If you make 7 loaves of bread instead of 1, you must MULTIPLY every single ingredient by 7, not add 7."* |
| **Dividing gear ratios in reverse order** | Mixing up the driver gear (input) and driven gear (output). | *"Gear ratio is always Driven teeth divided by Driver teeth ($\text{Out} \div \text{In}$). A bigger driven gear spins slower with stronger push."* |
| **Ignoring the 20% battery reserve rule** | Draining a rechargeable drone battery all the way to 0%. | *"Draining a drone battery below 20% wears it out. Always multiply battery capacity by 0.80 to find safe flight time."* |

---

### Scratch-Paper Formula Juggling vs. Live Workshop Stack Modeling

Now that you have explored 3D printing, pendulums, solar ovens, catapults, recipes, gear trains, hydraulics, and drones, compare how a multi-step workshop cost calculation is entered on a standard calculator versus live unit-rate evaluation on the SC-6 stack:

| Challenge / Equation | The Algebraic Calculator Trap (Standard Entry) | The StackCalc SC-6 + Manipulative Method | Keystroke Comparison | Live Stack Visibility | Learning Breakthrough |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **3D Printing Filament Cost**: $14.91\text{g} \times (\$20.00 / 1000\text{g}) = \$0.30$ | Typing `1 4 . 9 1  2 0 / 1 0 0 0 =` (14 physical keystrokes) jumps straight to `0.2982` without ever displaying the $\$0.02/\text{g}$ unit cost—or requires parentheses `1 4 . 9 1  ( 2 0 / 1 0 0 0 ) =` (16 physical keystrokes) to group the unit rate first. | Continuous dimensional pipeline: `14.91 {{key:ENTER}} 20 {{key:ENTER}} 1000 {{key:÷}} {{key:×}} {{key:$}}` $\to \mathbf{\$0.30}$ (16 physical keystrokes, including `{{key:$}}` rounding). Both the part mass ($14.91\text{g}$) and unit cost ($\$0.02/\text{g}$) appear side by side on the stack. | **16 vs. 16 strokes (with live unit-rate check & `{{key:$}}` rounding)** | Register $Y$ holds $14.91\text{g}$ while Register $X$ displays the exact unit price $\$0.02/\text{g}$, followed by single-tap `{{key:×}}` and `{{key:$}}` currency formatting without scrap paper. | Students measure physical filament with calipers, inspect both the gram weight and per-gram unit rate simultaneously on the screen, and see the exact cost before printing. |

---

## Field & Workshop Investigations: From Pinewood Derbies to Solar Arrays

Ready to put on your maker apron and step up to the workbench? Each investigation below links several workshop calculations into a continuous project—and every sequence starts from standard numeric mode (`{{key:NUM}}`). As you work through each station, watch how the four-register stack acts like an extra pair of hands at your workbench, holding your first measurement steady on Register $Y$ while you shape the next measurement on Register $X$.

### The 3D Printing & Maker Workshop
Welcome to the Kitchen-Table 3D Printing Studio, where you are the lead builder! In this four-stop workshop investigation, you will measure a calibration test cube, see how much plastic a honeycomb interior saves, trace the volume of filament unspooled for a storage bin, and budget a batch of 50 STEM fair medals.

Every 3D-printing adventure begins with a quick "test print" to make sure the printer's belts and nozzle are tuned to perfection. Before printing a full tray of **Counting Tiles**, you print a calibration cube that measures $20\text{ mm}$ ($2.0\text{ cm}$) along its length, width, and height. Closing your vernier calipers across all three directions confirms that every edge is an exact $2\text{ cm}$. Evaluating the volume of the cube in cubic centimeters ($\text{Length} \times \text{Width} \times \text{Height}$) via `{{res:sc6_09_applied_stem_labs_p34:keys}}` produces **`{{res:sc6_09_applied_stem_labs_p34:value}}`**. Notice how the four-register stack builds the 3D cube from a flat square base up into space:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `{{key:2}}` | 0 | 0 | 0 | 2 | Enter cube length in centimeters ($2\text{ cm}$) |
| `{{key:ENTER}}` | 0 | 0 | 2 | 2 | Copy length into Register $Y$ |
| `{{key:2}}` | 0 | 0 | 2 | 2 | Enter cube width ($2\text{ cm}$) |
| `{{key:×}}` | 0 | 0 | 0 | 4 | Multiply length by width to get the bottom square area ($4\text{ cm}^2$) |
| `{{key:2}}` | 0 | 0 | 4 | 2 | Enter cube height ($2\text{ cm}$); lifts area into Register $Y$ |
| `{{key:×}}` | 0 | 0 | 0 | 8 | Multiply base area by height to find cube volume ($8.0\text{ cm}^3$) |

Register $X$ confirms a volume of $\mathbf{8.0\text{ cm}^3}$—the exact space occupied by eight $1\text{ cm}$ unit cubes stacked in a $2 \times 2 \times 2$ block.

Now that you know your test cube takes up $8.0\text{ cm}^3$ of space, let's weigh it on the workshop scale! Every cubic centimeter ($1\text{ cm}^3$) of corn-based PLA plastic weighs $1.24\text{ grams}$. If you printed that $8.0\text{ cm}^3$ cube completely solid ($100\%$ infill), how heavy would it be—and how many grams of plastic do you save when a hollow-infill **Counting Tile** weighs only $3.1\text{ grams}$? First, multiplying the $8\text{ cm}^3$ volume by $1.24\text{ grams per cm}^3$ with `{{res:sc6_09_applied_stem_labs_p35:keys}}` yields **`{{res:sc6_09_applied_stem_labs_p35:value}}`**. Next, subtracting the $3.1\text{-gram}$ hollow-infill tile weight via `{{res:sc6_09_applied_stem_labs_p36:keys}}` leaves **`{{res:sc6_09_applied_stem_labs_p36:value}}`**. Printing a honeycomb interior instead of solid plastic saves $\mathbf{6.82\text{ grams}}$ on every single block—more than two-thirds of the plastic weight—while keeping the outer walls just as stiff and sturdy in your hands!

With your printer calibrated and your honeycomb infill dialed in, you are ready to print a custom storage bin to hold your **Counting Tiles**! Before you press "Print," your slicing software previews the toolpath and reports that the bin will unspool $1,200\text{ cm}$ ($12\text{ meters}$) of filament from the reel. Closing your calipers gently across the filament strand shows a width (diameter) of $1.75\text{ mm}$, which means its radius from the center to the edge is $0.875\text{ mm} = 0.0875\text{ cm}$. First, finding the tiny circle area of the filament strand ($\pi \times \text{Radius}^2$) with `{{res:sc6_09_applied_stem_labs_p01:keys}}` produces **`{{res:sc6_09_applied_stem_labs_p01:value}}`**, and stretching that circle along the $1,200\text{ cm}$ strand via `{{res:sc6_09_applied_stem_labs_p02:keys}}` reaches **`{{res:sc6_09_applied_stem_labs_p02:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `.0875` | 0 | 0 | 0 | $0.0875$ | Enter filament radius in centimeters ($0.0875\text{ cm}$) |
| `{{key:x²}}` | 0 | 0 | 0 | $0.007656$ | Square the radius ($0.0875 \times 0.0875 = 0.00765625\text{ cm}^2$) |
| `{{key:π}}` | 0 | 0 | $0.007656$ | $3.141593$ | Enter $\pi$; stack lifts the squared radius into Register $Y$ |
| `{{key:×}}` | 0 | 0 | 0 | $0.024053$ | Multiply to find the filament circle area ($\approx 0.02405\text{ cm}^2$) |
| `1200` | 0 | 0 | $0.024053$ | 1200 | Enter the filament length ($1,200\text{ cm}$) |
| `{{key:×}}` | 0 | 0 | 0 | $28.863383$ | Multiply circle area by length to find plastic volume ($28.86\text{ cm}^3$) |

Register $X$ confirms that the storage bin uses $\mathbf{28.86\text{ cm}^3}$ of melted plastic—transforming a long, flexible cylinder of filament on the spool into a rigid geometric box on the build plate.

Finally, word spreads around school about your 3D-printing studio, and the principal asks your team to print 50 gold award medals for the Friday STEM Fair! Weighing one finished sample medal on your digital scale shows that each medal uses $14.5\text{ grams}$ of plastic. With filament priced at $\$0.02$ per gram, how much will it cost to print all 50 medals? Evaluating the three-step cost calculation on the stack via `{{res:sc6_09_applied_stem_labs_p40:keys}}` yields **`{{res:sc6_09_applied_stem_labs_p40:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `50` | 0 | 0 | 0 | 50 | Enter total medals to print ($50\text{ medals}$) |
| `{{key:ENTER}}` | 0 | 0 | 50 | 50 | Copy medal count into Register $Y$ |
| `14.5` | 0 | 0 | 50 | $14.5$ | Enter weight of one medal ($14.5\text{ g}$) |
| `{{key:×}}` | 0 | 0 | 0 | 725 | Multiply to find total plastic weight ($50 \times 14.5 = 725\text{ g}$) |
| `.02` | 0 | 0 | 725 | $0.02$ | Enter filament cost per gram ($\$0.02/\text{g}$) |
| `{{key:×}}` | 0 | 0 | 0 | $14.5$ | Multiply weight by price per gram ($725 \times 0.02 = 14.50$) |
| `{{key:$}}` | $0.00$ | $0.00$ | $0.00$ | $14.50$ | Format result in currency mode |

Register $X$ displays $\$14.50$, showing that printing all 50 STEM fair medals costs just $\mathbf{\$14.50}$ in PLA filament—less than a single store-bought trophy!

---

### Backyard Science & Botany Lab
Now let's step outside from the 3D-printing bench into the afternoon sunshine! In this investigation, you will track how fast a homemade pizza-box solar oven heats up, measure the average and consistency of tabletop catapult launches, and clock the daily growth speed of a windowsill bean sprout.

We start on the sunny patio at noon. Your science team lines a cardboard pizza box with aluminum foil and clear plastic wrap, slips a thermometer probe inside, and points the reflector at the sun. Over the next $15\text{ minutes}$, the temperature inside climbs from $20^\circ\text{C}$ to $65^\circ\text{C}$. First, find the heating speed in degrees per minute (`{{res:sc6_09_applied_stem_labs_p11:keys}}` $\to$ **`{{res:sc6_09_applied_stem_labs_p11:value}}`**): subtracting the $20^\circ\text{C}$ starting temperature gives a $45^\circ\text{C}$ rise, and dividing by $15\text{ minutes}$ gives a brisk $\mathbf{3.00^\circ\text{C/min}}$. Next, check the percentage temperature boost with `{{key:%CHG}}` (`{{res:sc6_09_applied_stem_labs_p12:keys}}` $\to$ **`{{res:sc6_09_applied_stem_labs_p12:value}}`**), confirming a $\mathbf{+225.0\%}$ jump over the starting temperature—plenty of solar warmth to melt chocolate squares onto graham crackers!

While the solar oven warms up in the sun, you unroll a measuring tape across the patio to test your rubber-band lever catapult. Firing 3 practice shots at the same pullback angle sends the foam ball landing at $150\text{ cm}$, $162\text{ cm}$, and $156\text{ cm}$. Where should you place the center of your target ring? Dropping all three launches into your statistical basket with `{{key:Σ+}}` and pressing `{{key:x̄}}` via `{{res:sc6_09_applied_stem_labs_p13:keys}}` levels the three distances out to **`{{res:sc6_09_applied_stem_labs_p13:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `{{key:CLΣ}}` | 0 | 0 | 0 | 0 | Clear the statistics registers |
| `150 {{key:Σ+}}` | 0 | 0 | 0 | 1 | Add Shot 1 ($150\text{ cm}$); screen shows count $= 1$ |
| `162 {{key:Σ+}}` | 0 | 0 | 0 | 2 | Add Shot 2 ($162\text{ cm}$); screen shows count $= 2$ |
| `156 {{key:Σ+}}` | 0 | 0 | 0 | 3 | Add Shot 3 ($156\text{ cm}$); screen shows count $= 3$ |
| `{{key:x̄}}` | 0 | 0 | 0 | 156 | Compute the average (mean) landing distance ($156.00\text{ cm}$) |

Register $X$ confirms an average launch distance of $\mathbf{156.00\text{ cm}}$.

Knowing the $156\text{ cm}$ average tells you where to center the target—but how tightly grouped were those three shots ($150\text{ cm}, 162\text{ cm}, 156\text{ cm}$) around that center? Look at how far each shot wandered from $156\text{ cm}$: Shot 1 was $6\text{ cm}$ short, Shot 2 was $6\text{ cm}$ long, and Shot 3 landed right on the nose ($0\text{ cm}$). Since all three shots are still sitting in your statistical registers from our three-shot average calculation, one tap of `{{key:MAD}}` on the SC-6 via `{{res:sc6_09_applied_stem_labs_p14:keys}}` returns **`{{res:sc6_09_applied_stem_labs_p14:value}}`**. Because $(6 + 6 + 0) \div 3 = 4$, your catapult launches stay within an average of $\mathbf{4.00\text{ cm}}$ of the bullseye!

For the final stop of our backyard science investigation, we check on the bean sprout growing on the sunny windowsill. Five days ago it stood $15\text{ mm}$ tall; today your millimeter ruler reads $75\text{ mm}$ tall! How many millimeters did it climb per day, and what was its total percentage growth? First, finding the daily growth speed with `{{res:sc6_09_applied_stem_labs_p15:keys}}` yields **`{{res:sc6_09_applied_stem_labs_p15:value}}`**, and checking the percentage growth via `{{res:sc6_09_applied_stem_labs_p16:keys}}` confirms **`{{res:sc6_09_applied_stem_labs_p16:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `75` | 0 | 0 | 0 | 75 | Enter ending sprout height ($75\text{ mm}$) |
| `{{key:ENTER}}` | 0 | 0 | 75 | 75 | Copy ending height into Register $Y$ |
| `15` | 0 | 0 | 75 | 15 | Enter starting sprout height ($15\text{ mm}$) |
| `{{key:-}}` | 0 | 0 | 0 | 60 | Subtract to find total height gained ($75 - 15 = 60\text{ mm}$) |
| `{{key:5}}` | 0 | 0 | 60 | 5 | Enter number of growing days ($5\text{ days}$) |
| `{{key:÷}}` | 0 | 0 | 0 | 12 | Divide height gained by days ($60 \div 5 = 12.0\text{ mm/day}$) |
| `15 {{key:ENTER}}` | 0 | 12 | 15 | 15 | Enter starting height ($15\text{ mm}$) into Register $Y$ |
| `75 {{key:%CHG}}` | 0 | 12 | 15 | 400 | Find percent increase from $15\text{ mm}$ to $75\text{ mm}$ ($+400.0\%$) |

Register $X$ shows that the bean sprout grew $\mathbf{12.0\text{ mm/day}}$ for a total increase of $\mathbf{+400.0\%}$—five times its starting height in less than a week!

---

### Kitchen Bakery & Recipe Scaling
Now wash your hands and tie on your baker's apron: you are the head baker for the School STEM Bake Sale! In this investigation, you will scale bread dough weights in grams using Baker's Percentages and use your **Fraction Towers** to multiply and divide measuring-cup recipes with zero kitchen-counter guesswork.

First up on the bakery counter: twelve golden loaves of artisan bread! A single loaf uses $450\text{ grams}$ of flour ($100\%$), plus $65\%$ water and $2\%$ salt. To mix the dough for all $12$ loaves at once, how many grams of flour, water, and salt should you weigh out on your kitchen scale? First calculate total flour (`{{res:sc6_09_applied_stem_labs_p17:keys}}` $\to$ **`{{res:sc6_09_applied_stem_labs_p17:value}}`**), then $65\%$ water (`{{res:sc6_09_applied_stem_labs_p18:keys}}` $\to$ **`{{res:sc6_09_applied_stem_labs_p18:value}}`**), and then $2\%$ salt (`{{res:sc6_09_applied_stem_labs_p19:keys}}` $\to$ **`{{res:sc6_09_applied_stem_labs_p19:value}}`**):

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `450 {{key:ENTER}}` | 0 | 0 | 450 | 450 | Enter flour weight for 1 loaf ($450\text{ g}$) |
| `12 {{key:×}}` | 0 | 0 | 0 | 5400 | Multiply by 12 loaves to find total flour ($5,400\text{ g}$) |
| `65 {{key:%}}` | 0 | 0 | 5400 | 3510 | Find $65\%$ of $5,400\text{ g}$ for water ($3,510\text{ g}$); $5,400$ stays in $Y$ |
| `5400 {{key:ENTER}}` | 5400 | 3510 | 5400 | 5400 | Place the $5,400\text{ g}$ flour base in Register $Y$ |
| `{{key:2}} {{key:%}}` | 5400 | 3510 | 5400 | 108 | Find $2\%$ of $5,400\text{ g}$ for salt ($108\text{ g}$) |

Your 12-loaf batch uses $\mathbf{5,400\text{ grams}}$ of flour, $\mathbf{3,510\text{ grams}}$ of water, and $\mathbf{108\text{ grams}}$ of salt—and because the flour weight stayed anchored in Register $Y$, every ingredient percentage took just a couple of taps!

While the bread dough rises in a warm bowl, let's bake trail-mix granola bars! A single batch calls for $2\ \frac{1}{4}$ cups of rolled oats, and you need $4$ batches for the bake sale table. Before touching a button, picture $2\ \frac{1}{4} \times 4$ with your **Fraction Towers**: four $2$-whole towers make $8$ wholes, and four $\frac{1}{4}$ blocks snap together into $1$ more whole tower ($8 + 1 = 9$). Verifying on the SC-6 using mixed-fraction entry via `{{res:sc6_09_applied_stem_labs_p20:keys}}` confirms **`{{res:sc6_09_applied_stem_labs_p20:value}}`**: multiplying $2\ \frac{1}{4}$ by $4$ gives an exact $\mathbf{9\text{ cups}}$ of oats.

To wash down the warm granola bars, you blend $3\ \frac{1}{2}$ cups of berry smoothie and pour it equally into $4$ tasting cups for your baking team. What fraction of a cup does each person get? Picture $3\ \frac{1}{2}$ as seven $\frac{1}{2}\text{-cup}$ blocks ($7/2$): when you slice each half-cup into 4 equal shares, halves turn into eighths ($7/8$). Dividing the mixed-number volume by 4 on the stack with `{{res:sc6_09_applied_stem_labs_p39:keys}}` yields **`{{res:sc6_09_applied_stem_labs_p39:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `3 {{key:.}} 1 {{key:.}} 2` | 0 | 0 | 0 | $3\ 1/2$ | Enter mixed number $3\ \frac{1}{2}$ cups |
| `{{key:ENTER}}` | 0 | 0 | $3\ 1/2$ | $3\ 1/2$ | Push $3\ \frac{1}{2}$ into Register $Y$ |
| `{{key:4}}` | 0 | 0 | $3\ 1/2$ | 4 | Enter 4 equal cups |
| `{{key:÷}}` | 0 | 0 | 0 | $7/8$ | Divide $3\ \frac{1}{2} \div 4 = 7/8$ cup |
| `{{key:a ᵇ/c}}` | 0 | 0 | 0 | $0.875$ | Toggle between exact fraction `7/8` and decimal `0.875` |

Each tasting cup receives $\mathbf{7/8\text{ cup}}$ ($0.875\text{ cup}$) of smoothie—just one eighth of a cup shy of a full cup!

---

### Gears, Drones & Club Budget Math
For our final adventure of the book, you step into the Robotics & Maker Club Workshop as project manager! Here you will test simple and two-stage compound gear trains, calculate safe quadcopter hover times, and split a discounted tool order evenly among 6 club members.

First, your robotics team tests a single gear pair where a small $16\text{-tooth}$ driver gear turns a large $64\text{-tooth}$ driven gear (`{{res:sc6_09_applied_stem_labs_p21:keys}}` $\to$ **`{{res:sc6_09_applied_stem_labs_p21:value}}`**). Next, to wind heavy cord onto a winch drum, you build a two-stage compound gear train: Stage 1 uses a $10\text{-tooth}$ gear driving a $40\text{-tooth}$ gear, and Stage 2 uses a $15\text{-tooth}$ gear driving a $30\text{-tooth}$ gear. Watch how the 4-register stack holds the Stage 1 ratio (`4`) on Floor $Z$ while you divide Stage 2 (`30 ÷ 15 = 2`), then multiplies both stages together (`{{res:sc6_09_applied_stem_labs_p23:keys}}` $\to$ **`{{res:sc6_09_applied_stem_labs_p23:value}}`**):

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `40 {{key:ENTER}} 10 {{key:÷}}` | 0 | 0 | 0 | 4 | Stage 1 gear ratio: $40 \div 10 = 4.0$ |
| `30 {{key:ENTER}}` | 0 | 4 | 30 | 30 | Enter Stage 2 driven gear ($30\text{ teeth}$); lifts $4$ into Register $Z$ |
| `15 {{key:÷}}` | 0 | 0 | 4 | 2 | Stage 2 gear ratio: $30 \div 15 = 2.0$; drops $4$ into Register $Y$ |
| `{{key:×}}` | 0 | 0 | 0 | 8 | Multiply Stage 1 by Stage 2: $4 \times 2 = 8.0$ |

Register $X$ displays $8.0$, proving that the two-stage gear train gives an $\mathbf{8.0 : 1}$ mechanical advantage—trading eight fast turns of the motor shaft for one slow, super-strong turn of the winch drum!

Next, your club bolts a lightweight 3D-printed frame onto an indoor quadcopter powered by a $1,200\text{ mAh}$ battery. Following the $80\%$ safe battery rule ($0.80$) so $20\%$ stays in reserve for a safe landing, how many minutes can the drone hover when its four motors draw a combined $5,000\text{ mA}$? Calculating the safe flight time in minutes on the stack via `{{res:sc6_09_applied_stem_labs_p26:keys}}` produces **`{{res:sc6_09_applied_stem_labs_p26:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `1200 {{key:ENTER}}` | 0 | 0 | 1200 | 1200 | Enter battery capacity ($1,200\text{ mAh}$) |
| `.8 {{key:×}}` | 0 | 0 | 0 | 960 | Multiply by $0.80$ safe battery rule: $960\text{ mAh}$ usable |
| `60 {{key:×}}` | 0 | 0 | 0 | 57600 | Multiply by $60\text{ minutes per hour}$ ($57,600\text{ mA}\cdot\text{min}$) |
| `5000` | 0 | 0 | 57600 | 5000 | Enter hover current draw ($5,000\text{ mA}$) |
| `{{key:÷}}` | 0 | 0 | 0 | $11.52$ | Divide usable battery by current ($57,600 \div 5,000 = 11.52\text{ min}$) |

Register $X$ displays $11.52\text{ minutes}$, showing that the quadcopter can safely hover for $\mathbf{11.52\text{ minutes}}$ before the landing timer beeps.

To wrap up the workshop day, your 6-student Maker Club orders a digital caliper and tool set listed at $\$56.00$ with a $30\%$ student discount (`{{res:sc6_09_applied_stem_labs_p31:keys}}` $\to$ **`{{res:sc6_09_applied_stem_labs_p31:value}}`**) plus $7.5\%$ sales tax (`{{res:sc6_09_applied_stem_labs_p32:keys}}` $\to$ **`{{res:sc6_09_applied_stem_labs_p32:value}}`**). Then, when the club's total 3D-printing supply bill comes to $\$124.80$, you split it equally among all $6$ members (`{{res:sc6_09_applied_stem_labs_p33:keys}}` $\to$ **`{{res:sc6_09_applied_stem_labs_p33:value}}`**):

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `56 {{key:ENTER}}` | 0 | 0 | 56 | 56 | Enter regular tool price ($\$56.00$) |
| `30 {{key:%}}` | 0 | 0 | 56 | $16.8$ | Find $30\%$ discount ($\$16.80$); base $\$56$ stays in Register $Y$ |
| `{{key:-}} {{key:$}}` | $0.00$ | $0.00$ | $0.00$ | $39.20$ | Subtract discount and format as currency ($\$39.20$ sale price) |
| `7.5 {{key:%}}` | $0.00$ | $0.00$ | $39.20$ | $2.94$ | Find $7.5\%$ sales tax ($\$2.94$); $\$39.20$ stays in Register $Y$ |
| `{{key:+}} {{key:$}}` | $0.00$ | $0.00$ | $0.00$ | $42.14$ | Add sales tax for final tool checkout price ($\$42.14$) |
| `124.80 {{key:ENTER}} {{key:6}} {{key:÷}} {{key:$}}` | $0.00$ | $0.00$ | $42.14$ | $20.80$ | Split the $\$124.80$ supply bill among 6 students ($\$20.80$ each) |

The discounted tool set costs $\mathbf{\$42.14}$ after tax, and each club member pays $\mathbf{\$20.80}$ for the supply bill—all balanced to the penny on the four-register stack!

---

## Where to Go Next: Companion Workbook Quests & Kitchen-Table Challenges

> *For 26 additional worked problems with full 4-register stack tables, see Chapter 9 of the [SC-6 Elementary Companion Problem & Activity Workbook](../../curriculum/sc6-elementary-companion-workbook.md).*

Ready to launch your own weekend invention studio? Here is how to extend the projects in this chapter using the [Big Ideas Math Middle School Supplement](../../curriculum/big-ideas-middle-school-sc6-workbook.md)—across **Unit 1: Numerical Expressions & Factors (Section 1.5)**, **Unit 2: Fractions & Decimals (Sections 2.2, 2.3 & 2.5)**, **Unit 3: Ratios, Rates & Percents (Sections 3.1 & 3.3)**, **Unit 5: Area, Surface Area & Volume (Section 5.2)**, **Unit 7: Equations & Inequalities (Section 7.5)**, **Unit 8: Geometric Figures, Scale Drawings & Circles (Section 8.4)**, and **Unit 9: Statistical Measures & Data Displays (Section 9.4)**—alongside *Timed Proficiency Trials* and the *12-Unit Curriculum Guide*:

1. **The Kitchen-Table Pendulum Timing Lab (Curriculum Guide Unit 9 & Student Workbook):** Tie a metal washer or 3D-printed bob to a $100\text{ cm}$ ($1\text{-meter}$) piece of string and time 10 full back-and-forth swings with a stopwatch. Divide by $10$ on your SC-6 to find the average time for 1 swing, then shorten the string to $25\text{ cm}$ (one-fourth as long) and time 10 swings again to see why a quarter-length pendulum swings twice as fast!
2. **The Baker's Percentage Pizza Night (Big Ideas Middle School Supplement):** Weigh out $400\text{ g}$ of flour on a kitchen scale ($100\%$), then use your SC-6's `{{key:%}}` and `{{key:C}}` keys (just like our 28-guest banquet bread scaling earlier) to compute $65\%$ warm water ($260\text{ g}$), $2\%$ salt ($8\text{ g}$), and $1.5\%$ yeast ($6\text{ g}$) without ever re-typing `400`.
3. **The 3D-Printer Slicer & `{{key:LASTX}}` Height Sprint (Timed Proficiency Trials — Maker Engineering Round):** Pick any block height in centimeters, subtract the base height, and divide by `.02` ($0.02\text{ cm}$ per layer) to find how many horizontal plastic layers the 3D printer must trace—then tap `{{key:LASTX}} {{key:×}}` to verify that the layers stack back up to the exact remaining height without typing `.02` twice!

---

## Chapter Summary & Looking Ahead

Across all nine chapters, you have paired physical manipulatives with the four-register stack to solve arithmetic, geometry, statistics, and maker problems:

1. **The RPN Mental Model & Stack Mastery:** You replaced parentheses and equals-sign confusion with a four-register stack ($X, Y, Z, T$) that tracks intermediate values like physical blocks.
2. **Tactile Fractions & Rational Arithmetic:** You explored fraction equivalence, common denominators, and mixed numerals by aligning real blocks and tapping dedicated fraction hardware keys (`{{key:a ᵇ/c}}`, `{{key:d/c}}`, `{{key:SIMP}}`).
3. **Spatial Geometry & Dimensional Scaling:** You measured perimeters, surface areas, and 3D volumes, using **Counting Tiles**, the **L-Frame Factoring Stage**, and the **Unit Circle Volvelle** shadow projection to connect 2D footprints to real 3D solids.
4. **Number Theory & Experimental Probability:** You examined the building blocks of numbers with prime factorization, GCF, and LCM, and gathered empirical data with the hardware probability engine (`{{key:🎲}}`) and statistical accumulators (`{{key:Σ+}}`).
5. **Cognitive Reflexes & Mental Math Fluency:** You trained your speed and accuracy in the Quiz Engine, applying the ends-in-5 squaring shortcut, the 11s trick, and instant verification without scratch paper.
6. **Applied STEM & Maker Design:** You connected word rules directly to physical measurements—budgeting 3D printer filament weight and spool costs, slicing $0.02\text{ cm}$ print layers, timing clock pendulums, scaling recipes, tuning gear ratios, and calculating drone flight times.

Your SC-6 is more than a calculator—it is your permanent laboratory workbench, your tactile compass, and your engineering partner. 

To fabricate your own manipulatives in CAD or on a 3D printer, check out **[Appendix A: Manipulative Blueprints & Physical Fabrication Guide](appendix-a-manipulative-blueprints.md)**, review classroom stations in **[Appendix B: Teacher Lesson Plans & Classroom Station Guide](appendix-b-teacher-lesson-plans.md)**, look up conversion factors in **[Appendix C: Formulas, Physical Constants & Unit Conversions](appendix-c-formulas-and-conversions.md)**, or inspect every button function in **[Appendix D: Complete Keycap Directory & Operational Reference](appendix-d-keycap-directory.md)**. 

Keep building, keep measuring, and keep exploring!