---
title: "Chapter 1: Meet Your SC-6 Stack Calculator & Math Blocks"
description: "Discover the daylight screen, the 4-level number stack, tactile clicky buttons, and 3D-printed math blocks of the StackCalc SC-6."
---

# Chapter 1: Meet Your SC-6 Stack Calculator & Math Blocks

## Why Real Buttons and Blocks Beat a Glowing Tablet Screen

Picture sitting at your kitchen table on a rainy Tuesday afternoon. Your math book is open to multi-digit subtraction, and right beside it rests a school tablet. Within ninety seconds of starting homework, a red notification badge slides across the glass: a message chime, a game update, a colorful video banner. Even when locked in "study mode," the tablet's bright electric backlight shines straight into your eyes like a tiny flashlight. Before long, your eyes feel tired and your focus is pulled in twenty directions at once. A glowing tablet feels like an arcade pretending to be a desk.

Now look at the other side of your desk: the **StackCalc SC-6**. Molded from tough, dark Midnight Navy plastic, it has no Wi-Fi, no pop-up alerts, and no noisy distractions. Its screen doesn't beam harsh light into your face—it reads just like a paper book using the natural daylight in your room. And when you press a key, your finger doesn't slide across flat, silent glass. Beneath every key sits a tiny stainless-steel dome that clicks down with a crisp, satisfying *snap!* Your fingers feel the click and your ears hear the snap: *your number is on the stack, and you are ready for the next step.*

{{res:sc6_hero_calculator:screenshot|StackCalc SC-6 Elementary Handheld Portrait}}
*Figure 1.1: The StackCalc SC-6 Elementary Handheld in Midnight Navy with sliding 15° easel desk cowl. A dedicated tactile tool for deep mathematical focus.*

The SC-6 is built like an astronaut's pocket instrument. Nothing on it is flimsy or disposable. Every button, shelf, and angle helps you focus on what math really is: building, discovering, and exploring with your hands.

Educational research by John Sweller {{cite:sweller1988}} and George A. Miller {{cite:miller1956}} shows that human working memory can only hold about four to seven pieces of new information at once. When a learner tries to do math on a glowing tablet filled with notifications, menus, and nested parentheses, those distractions crowd out working memory. Inspired by David Macaulay’s clear cutaways of how machines work {{cite:macaulay2016}}, the SC-6 keeps four visible stack shelves right on the screen and pairs them with physical blocks on the desk—freeing up your mind to focus completely on the math in your hands.

> **Faceplate Themes & Shift Legend Conventions**
>
> Because the StackCalc SC-6 hardware faceplates and companion app support multiple visual themes (`Pure Black`, `Retro Futurism`, `Pioneer`, `Stealth`, `Supernova`, `Voyager`, and `Arcade`), keycap and shift accent colors vary by faceplate. Throughout this textbook, shifted operations are always referenced by their shift symbols rather than color: **`{{key:f}}` Shift** and **`{{key:g}}` Shift**.

---

## Inside Your Stack Calculator: The Screen, The Buttons & The Desk Stand

Before we open your math block trays, let's explore the physical parts of your calculator—and use the stack itself to measure how each piece works!

### The Daylight Screen & Its Tiny Pixel Grid

Unlike phones or tablets that shine bright electric light straight into your eyes, the SC-6 features a **Daylight Screen**. Have you ever noticed that a tablet screen washes out when you take it outside into bright sunlight, while your SC-6 screen actually looks *sharper* by a sunny window? That is because tucked right behind the liquid-crystal layer is a silvery reflector that bounces natural room light back to your eyes just like a page of white paper.

Under bright classroom lighting, a light meter measures **$142.0$ units** of light bouncing off the silver background and **$9.35$ units** bouncing off the dark ink-black numbers. We can use our stack right now to see how many times brighter the silver background is than the dark numbers: put `142` onto Waiting Shelf $Y$ (`142 {{key:ENTER}}`), put `9.35` onto Workbench Shelf $X$, and tap `{{key:÷}}` (`{{res:sc6_01_hardware_architecture_seq_03:keys}}` $\rightarrow$ **`{{res:sc6_01_hardware_architecture_seq_03:value}}`**). The silver background is **`15.19` times brighter** than the dark numbers—which is why your eyes never feel tired even after an hour of math!

Now lean in close and look at the numbers on the screen. Every digit, ten-frame counter, and clock hand is drawn on a grid of tiny square dots called **pixels**—just like a giant rectangle of Counting Tiles arranged in **$132$ columns across** and **$65$ rows high**. In computer memory, each pixel dot takes 1 bit (`1` for a dark dot, `0` for a silver-white dot), and **$8$ bits** pack neatly into **$1$ byte** of memory. How many total pixels are on your screen, and how many bytes of memory does it take to hold one full screen picture?

First, multiply the columns by the rows (`132 {{key:ENTER}} 65 {{key:×}}`) to see all **`8,580` pixels** on Shelf $X$. Because `8,580` is now a finished answer sitting on Shelf $X$, you don't even need to press `{{key:ENTER}}` before the next step: just type `8` (which automatically lifts `8,580` up to Shelf $Y$!) and tap `{{key:÷}}` (`{{res:sc6_01_hardware_architecture_seq_02:keys}}` $\rightarrow$ **`{{res:sc6_01_hardware_architecture_seq_02:value}}`**) to pack those pixels into **`1072.5` bytes** ($1,073$ whole bytes). *(Try tapping `{{key:LASTX}} {{key:×}}` right after—it brings back `8` and multiplies to show all $8,580$ pixels again!)*

### How the Four Stack Shelves ($T, Z, Y, X$) & `{{key:ENTER}}` Work Together

On that pixel screen, your numbers don't vanish into hidden memory when you press `+` or `×`. Instead, they stack up on four visible shelves—the **4-Level Number Stack** ($T, Z, Y, X$), just like stacking physical blocks or books on your desk:
- **Level $X$ (The Ground Shelf / Active Workbench):** The bottom shelf of the screen where numbers appear as you type them, and where the immediate answer to every calculation lands.
- **Level $Y$ (The Second Shelf / Waiting Partner):** When you finish typing your first number and tap the big black **`{{key:ENTER}}`** button, your number pushes smoothly up to Level $Y$. Level $Y$ holds the first number waiting for math to happen (like the $142$ waiting in $142 \div 9.35$).
- **Levels $Z$ and $T$ (The Upper Shelves):** Above $Y$ sit two more shelves. When a problem has two or three parts, your finished subtotals ride up into $Z$ and $T$ to wait for you—and automatically drop back down when you combine numbers on $Y$ and $X$.

### Clicking Buttons You Can Feel & The `{{key:f}}` and `{{key:g}}` Shift Keys

Now press any button on your keypad slowly and feel the crisp *snap!* Underneath that sculpted keycap sits a tiny stainless-steel spring dome that pushes back against your thumb until your finger presses with **$400.0\text{ grams}$** of weight over a **$1.6\text{ millimeter}$** downward travel—and then clicks down to enter your number. How many grams of push does it take for each millimeter the button travels downward?

$$\text{Grams per Millimeter} = \text{Push Weight} \div \text{Distance Pushed} = 400.0\text{ grams} \div 1.6\text{ millimeters} = 250.0\text{ grams per millimeter}$$

Put the `400` grams of push weight on Shelf $Y$ (`400 {{key:ENTER}}`), put the `1.6` millimeters of travel on Shelf $X$, and tap `{{key:÷}}` (`{{res:sc6_01_hardware_architecture_seq_04:keys}}` $\rightarrow$ **`{{res:sc6_01_hardware_architecture_seq_04:value}}`**) to find **`250.0` grams per millimeter**. Every button label is molded directly into the keycap plastic so it never wears off, and instead of hiding math tools inside computer menus, each button gives you up to **three actions**:
- **Direct Press:** Tapping any key directly uses the main white label on the keycap face (digits `0`–`9`, `{{key:ENTER}}`, `{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`, clear `{{key:C}}`, and backspace `{{key:<-}}`).
- **`{{key:f}}` Shift Key:** Pressing `{{key:f}}` first activates the feature printed directly above the keycap, such as finding common multiples with `{{key:LCM}}`, simplifying fractions step-by-step with `{{key:SIMP}}`, unit conversions, and memory recall `{{key:REGS}}`.
- **`{{key:g}}` Shift Key:** Pressing `{{key:g}}` first activates the feature printed on or below the keycap, such as prime factor trees with `{{key:FACT}}`, skip-counting with `{{key:REP}}`, integer division with remainder `{{key:÷R}}`, low-power sleep `{{key:OFF}}`, and settings `{{key:FLAGS}}`.

### Setting Up Your $15^\circ$ Classroom Desk Stand

Your SC-6 includes a rugged **sliding protective cover** that doubles as a hands-free desk stand:
1. Slide the protective cover downward off the front of the calculator.
2. Flip the calculator over and slide the cover onto the rear rails until a gentle snap locks it in place.
3. Set the SC-6 on your desk—it now rests at a stable **$15^\circ$ reading angle**, keeping both hands free so your left hand can build with math blocks while your right hand taps keys into the stack.

Look at the side of your SC-6 while it rests in its $15^\circ$ stand. For every $1\text{ mm}$ the calculator reaches back across your desk, the $15^\circ$ ramp lifts it **$0.2679\text{ mm}$** upward. Since the stand reaches **$80.0\text{ mm}$** from front to back, how many millimeters high is the top edge lifted above your desk? Put `80` on Shelf $Y$ (`80 {{key:ENTER}}`), put `0.2679` on Shelf $X$, and tap `{{key:×}}` (`{{res:sc6_01_hardware_architecture_seq_06:keys}}` $\rightarrow$ **`{{res:sc6_01_hardware_architecture_seq_06:value}}`**) to see that the top edge lifts **`21.43` mm**—which you can feel right now by stacking **3 Counting Tiles** ($3 \times 7\text{ mm} = 21\text{ mm}$) behind the top edge of your calculator!

---

## Why the Calculator Is Dark and the Blocks Are Bright

Why is your calculator molded in dark Midnight Navy or Slate Gray, while your math blocks are bright white, radiant gold, and electric blue?

Think about how an astronomer uses a telescope: the inside tube of the telescope is painted dark matte black so stray light doesn't bounce into your eyes, letting you focus clearly on the stars. The dark shell of your SC-6 creates a quiet, restful frame of deep focus around the display with zero glare.

Your math blocks, on the other hand, are the stars. They are molded in bright white, warm amber, and vivid cobalt blue because blocks are meant to be touched, sorted, and counted. Your hands instinctively reach for the bright physical objects to build arrays, trains, and towers, while your eyes rest comfortably on the dark, glare-free calculator that records the results.

{{blocks:materials_swatch_grid|Companion Manipulative Color Palette: Matte Slate Enclosure and Color-Coded Math Blocks}}

> **Color Design: Dark Calculator vs. Bright Math Blocks:** To make sure your eyes can tell the calculator and the blocks apart at a glance, the SC-6 follows a simple color rule: the calculator case, bezel, and sliding cover are always molded from tough, dark matte plastics (Midnight Navy, Space Gray, or Matte Black), while bright white, gold, red, and blue colors are reserved for your physical math blocks (84 mm Fraction Towers, Ten-Frame counters, Counting Tiles, and Planetary Clock gears).

*(Curious how we 3D-printed the snap-together calculator case, tested the screen in a virtual simulator, and built an automated verification harness to test every math problem in this book? Check out **[Appendix A: Manipulative Studio Guide & How We Built StackCalc](appendix-a-manipulative-blueprints.md)**, **[stackcalc.io/hardware](https://stackcalc.io/hardware)**, and our open-source **[Hackaday Build Logs](https://hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator)**.)*

---

## Meet Your Math Blocks: Building Numbers with Your Hands

To make sure every number on the screen connects directly to something you can hold and explore, your StackCalc SC-6 pairs with physical 3D-printed math block sets. Whenever you start a math activity, place your **3D-printed block tray on the left side of your desk** and your **SC-6 on its $15^\circ$ easel stand on the right**. Every activity follows the same four hands-on steps:

| Desk Step | What Your Left Hand Does (The Blocks) | What Your Right Hand Does (The SC-6) | What You See & Feel |
| :---: | :--- | :--- | :--- |
| **Step 1: Build Group 1** | Place your first group of counters, tiles, or fraction towers into the **top/back row** (or Well A) of your tray. | Type that first number on the keypad and press `{{key:ENTER}}`. | Your first number rides up to **Floor $Y$** on the screen, matching your top/back tray row. |
| **Step 2: Build Group 2** | Place your second group of blocks into the **bottom/front row** (or Well B) of your tray. | Type that second number into **Floor $X$** (do not press `{{key:ENTER}}` after the second number). | Now **Floor $Y$** and **Floor $X$** on the screen mirror the two physical groups sitting on your desk. |
| **Step 3: Combine by Hand** | Slide the counters across the **5-anchor rib** to fill a ten-frame, rotate the tile array, or stack the fraction blocks in the **84 mm comparator well**. | Feel with your fingertips whether the ten-frame is full or the fraction towers sit flush at the top edge. | Your hands discover the physical answer *before* the calculator computes it. |
| **Step 4: Fuse on the Stack** | Point to your combined physical blocks on the tray. | Press the operation key (`{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`, or `{{key:SIMP}}`). | Floor $Y$ and Floor $X$ fuse into a single answer on **Floor $X$**, confirming your physical block model. |

Let's try that 4-step routine right now with your Counting Tiles:
1. Press `{{key:C}}` to wake the daylight screen.
2. **Step 1 (Group 1):** Place **5 blue counting tiles** into the top row of your tray, and tap `5` `{{key:ENTER}}` so `5` rides up to Shelf $Y$.
3. **Step 2 (Group 2):** Place **3 gold counting tiles** into the bottom row of your tray, and tap `3` so `3` sits on Shelf $X$. Look at how your screen (`Y = 5`, `X = 3`) matches the two rows on your desk!
4. **Steps 3 & 4 (Combine by Hand & Fuse on the Stack):** Slide the 3 gold tiles up beside the 5 blue tiles to count **8 tiles**, then tap **`{{key:+}}`** on your keypad to watch `5` and `3` fuse into **`8`** on Shelf $X$.

Now let's tour the nine companion studios that work with your SC-6:

### The Ten-Frame Trays & Flip Counters (`{{key:▦}}`)
Two 5-pocket trays hold ten two-color disc counters (coral red on one side, radiant gold on the other). Built-in finger scoops make it easy to slide and flip counters, and a raised **5-anchor divider rib** divides each row of ten into two visual groups of 5 so your eyes can spot numbers at a glance (*subitizing*). Tap `{{key:▦}}` to mirror your trays right on the screen: Shelf $Y$ shows the top tray, Shelf $X$ shows the bottom tray, and tapping `{{key:+}}` moves counters across to fill a complete ten (`7 + 5 = 12`).

{{blocks:ten_frame_subitizing_5anchor|Ten-Frame Studio: 5-Anchor Spotting at a Glance (5 Red + 3 Green = 8, 2 Empty to 10) and 70.0 mm 10-Rod Height Parity}}

### The Four-Color Counting & Array Studio (`{{key:NUM}}`)
Each kit holds 24 smooth-docking counting tiles in four colors (6 white, 6 blue, 6 gold, and 6 slate gray—or 144 tiles when 6 kits are shared at a table). Arrange tiles into rows and columns to build rectangular arrays for multiplication ($4 \times 6 = 24$), with rows on Shelf $Y$ and columns on Shelf $X$. Spin the tray sideways: 6 rows of 4 tiles still make 24—proving visually that changing the multiplication order never changes the total!

### The 84 mm Fraction Towers & Comparator Tray (`{{key:FDISP}}` & `{{key:SIMP}}`)
A precision $84.0\text{ mm}$ master tower represents $1\text{ Whole}$, paired with proportional fraction blocks ($1/2, 1/3, 1/4, 1/6, 1/8, 1/12$) and a side-by-side comparison tray. Why is the whole tower exactly **$84\text{ mm}$** tall? Because 84 divides evenly by $1, 2, 3, 4, 6, 7, 12, 14, 21, 28,$ and $42$—giving every fraction block an exact whole-millimeter height ($1/2 = 42\text{ mm}$, $1/3 = 28\text{ mm}$, $1/4 = 21\text{ mm}$, $1/6 = 14\text{ mm}$, $1/12 = 7\text{ mm}$)! Stack **twelve $7\text{ mm}$ Counting Tiles** right next to your **$84\text{ mm}$ 1-Whole Fraction Tower**, run your finger across their tops, and tap `12 {{key:ENTER}} 7 {{key:×}}` to see **`84`** millimeters on Shelf $X$. When you snap two $1/4$ towers together in the tray and type `. 2 . 4 {{key:SIMP}}`, the screen simplifies `2/4` to `1/2` while your fingers feel their matching $42\text{ mm}$ height.

{{blocks:fraction_studio_common_denominator|Fraction Studio: Common Denominator Discovery on 12-Socket Lid Tray Proving 1/3 (28.0 mm) + 1/4 (21.0 mm) = 7/12 (49.0 mm)}}

### The Prime Factor Studio (`{{key:PRIME}}` & `{{key:FACT}}`) and Planetary Geared Clock (`{{key:🕒}}`)
In the **Prime Factor Studio**, prime-number blocks ($2, 3, 5, 7, \dots$) are scaled so that stacking block 2 on block 3 reaches the exact height of $2 \times 3 = 6$ on the back-wall scale, while typing `60 {{key:FACT}}` on the keypad reveals $2^2 \times 3 \times 5$. In the **Planetary Geared Clock**, real interlocking 12-to-1 planetary gears link the minute hand and hour hand so turning the minute hand automatically glides the hour hand, matching the `{{key:🕒}}` Clock mode when you add hours and minutes across 60-minute boundaries.

### The Polyhedral Dice (`{{key:🎲}}`), Place Value Trays (`{{key:PV}}`), Number Rack (`{{key:COUNT}}`) & Quest Scoreboard (`{{key:?}}`)
Rounding out your desk studio are precision **Polyhedral Dice** ($d4, d6, d8, d10, d12, d20$) that pair with `{{key:🎲}}` digital dice rolls; the **Whole & Decimal Place Value Trays** with digit miniblocks and `+1` regrouping cubes that pair with `{{key:PV}}` (`347 = 300 + 40 + 7`); the two-rail **Number Rack** (5 red and 5 white beads per row) that pairs with `{{key:COUNT}}`; and the **Quest Scoreboard** pegboard where you place a `+10` token for solving with blocks and stack a second `+10` token (`10 {{key:ENTER}} 10 {{key:+}}` $\to \mathbf{20}$) for verifying on the SC-6.

### Adding Up Your Desktop Gridfinity Math Station on the Stack

Look at the undersides of your 3D-printed manipulative trays. To keep counters and fraction towers neatly organized on your desk, every tray snaps into a baseplate made of $42\text{ mm}$ squares called **Gridfinity squares**. Suppose you set up a desktop math station with three trays side by side:
- **1 Ten-Frame Tray:** $2\text{ squares long} \times 1\text{ square wide}$
- **1 Fraction Studio Well:** $3\text{ squares long} \times 1\text{ square wide}$
- **1 Counting & Array Box:** $3\text{ squares long} \times 2\text{ squares wide}$

How many Gridfinity squares does your whole station cover?

$$\text{Total Tray Squares} = (2 \times 1) + (3 \times 1) + (3 \times 2) = 2 + 3 + 6 = 11\text{ squares}$$

Watch how your stack shelves hold each finished tray while you multiply the next one (`{{res:sc6_01_hardware_architecture_seq_05:keys}}` $\rightarrow$ **`{{res:sc6_01_hardware_architecture_seq_05:value}}`**): first multiply the Ten-Frame Tray (`2 {{key:ENTER}} 1 {{key:×}}` $\to 2$), then multiply the Fraction Well (`3 {{key:ENTER}} 1 {{key:×}}` $\to 3$, while `2` automatically rides up to Shelf $Z$ and drops back to Shelf $Y$) and tap `{{key:+}}` to get `5` squares, and finally multiply the Counting Box (`3 {{key:ENTER}} 2 {{key:×}}` $\to 6$) and tap `{{key:+}}` to land on **`11` Gridfinity squares** with zero parentheses:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2 {{key:ENTER}}` | 0 | 0 | 2 | 2 | Enter ten-frame tray length (2 units) into Register $Y$ |
| `1 {{key:×}}` | 0 | 0 | 0 | 2 | Ten-frame footprint: $2 \times 1 = 2\text{ units}$ in Register $X$ |
| `3 {{key:ENTER}}` | 0 | 2 | 3 | 3 | Footprint 2 lifts to $Z$; enter fraction well length (3 units) into $Y, X$ |
| `1 {{key:×}}` | 0 | 0 | 2 | 3 | Fraction well footprint: $3 \times 1 = 3\text{ units}$ in $X$ ($2$ drops to $Y$) |
| `{{key:+}}` | 0 | 0 | 0 | 5 | Combine footprints: $2 + 3 = 5\text{ units}$ in Register $X$ |
| `3 {{key:ENTER}}` | 0 | 5 | 3 | 3 | Subtotal 5 lifts to $Z$; enter counting box length (3 units) into $Y, X$ |
| `2 {{key:×}}` | 0 | 0 | 5 | 6 | Counting box footprint: $3 \times 2 = 6\text{ units}$ in $X$ ($5$ drops to $Y$) |
| `{{key:+}}` | 0 | 0 | 0 | 11 | Sum all footprints: $5 + 6 = 11\text{ Gridfinity units}$ ($462\text{ mm}$) |

### Mystery-Button Calculators vs. Tactile Blocks & Stack Keys

Compare how an ordinary algebraic calculator handles these multi-step desk tasks against the visible shelves of your SC-6:

| Challenge / Real-World Task | The Algebraic Calculator Trap (Infix) | Algebraic Keystrokes & Clutter | The StackCalc + Blocks Method (RPN Stack + Visual Studio) | StackCalc Keystrokes | The Stack Advantage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **School Store Shopping:** Buying 2 Notebooks at $\$3.50$ and 4 Pencils at $\$0.75$: $(3.50 \times 2) + (0.75 \times 4)$ | A basic four-function calculator evaluates strictly left-to-right ($3.50 \times 2 + 0.75 = 7.75 \times 4 = \$31.00$), and on a scientific infix calculator, typing the full expression hides both individual subtotals ($\$7.00$ and $\$3.00$) until you press `=`. | `( 3 . 5 0 × 2 ) + ( 0 . 7 5 × 4 ) =` (21 keystrokes with brackets; subtotals hidden) | **RPN Elevator Stack:** Computes the notebook subtotal ($\$7.00$) and pencil subtotal ($\$3.00$) into visible shelves $Y$ and $X$, then combines them into $\$10.00$ with `{{key:+}}`. | `3.50 {{key:ENTER}} 2 {{key:×}} 0.75 {{key:ENTER}} 4 {{key:×}} {{key:+}}` (13 keystrokes) | **Both Subtotals Visible:** Zero parentheses; the $\$7.00$ notebook subtotal and $\$3.00$ pencil subtotal sit side-by-side on shelves $Y$ and $X$ before adding. |
| **Craft Ribbon Bookmarks:** Cutting $142\text{ cm}$ of Ribbon into $9.35\text{ cm}$ Strips ($142 \div 9.35$) | On a glowing tablet app, typing $142 \div 9.35 =$ erases both starting measurements the moment you press `=`, leaving only a decimal on a bright screen. | `1 4 2 . 0 / 9 . 3 5 =` (12 keystrokes; starting numbers disappear) | **Daylight Stack Division:** Places the $142\text{ cm}$ ribbon length on Shelf $Y$ and the $9.35\text{ cm}$ strip length on Shelf $X$ before dividing on a paper-like screen. | `142 {{key:ENTER}} 9.35 {{key:÷}}` (9 keystrokes) | **Clear Step-by-Step View:** Both the total ribbon length and strip size are visible on screen before dividing, with zero glare. |
| **Desktop Tray Footprint:** Total Gridfinity squares: $(2 \times 1) + (3 \times 1) + (3 \times 2)$ | Typing a chain of three products on an infix screen hides each individual tray area ($2$, $3$, and $6$) until the final `=`. | `( 2 * 1 ) + ( 3 * 1 ) + ( 3 * 2 ) =` (21 keystrokes with brackets) | **Progressive Stack Accumulation:** Each tray area ($2, 3, 6$) collapses cleanly on the stack, maintaining running totals without parentheses. | `2 {{key:ENTER}} 1 {{key:×}} 3 {{key:ENTER}} 1 {{key:×}} {{key:+}} 3 {{key:ENTER}} 2 {{key:×}} {{key:+}}` (16 keystrokes) | **Step-by-Step Verification:** Each tray footprint is verified on the live stack as physical trays dock into the baseplate. |

---

## Instant-On Memory, Battery Life & Taking Care of Your SC-6

Whenever you turn your calculator off (`{{key:OFF}}`) or let it fall asleep in your backpack after 3 minutes of quiet time, it automatically saves all four stack shelves ($X, Y, Z, T$), your `{{key:LASTX}}` number, and your quiz streaks so you can pick up right where you left off.

How can a single battery the size of a nickel power your calculator for nearly a whole school year? Because the daylight screen doesn't need an electric backlight, and the calculator goes into a deep sleep whenever you aren't pressing buttons! Inside the rear safety-locked hatch sits a CR2032 coin-cell battery that holds **$225$ drops of battery energy**. During a school day, your calculator uses **$0.65$ energy drops per hour** for **$2$ hours** of math class, and sips just **$0.0025$ energy drops per hour** for the other **$22$ hours** while sleeping.

$$\text{School Days} = \text{Total Energy Drops} \div (\text{Awake Drops} + \text{Sleeping Drops}) = 225 \div ((0.65 \times 2) + (0.0025 \times 22)) \approx 166.05\text{ days}$$

Look at how we can solve this two-team battery story right on the stack without any parentheses:
1. First multiply the **Awake Team**: `0.65 {{key:ENTER}} 2 {{key:×}}` puts **`1.30`** awake drops on Shelf $X$.
2. Next multiply the **Sleeping Team**: `0.0025 {{key:ENTER}} 22 {{key:×}}` puts **`0.055`** sleeping drops on Shelf $X$ while `1.30` waits safely on Shelf $Y$, and tapping **`{{key:+}}`** adds them into **`1.355`** energy drops per day.
3. Finally, type `225` onto Shelf $X$ (lifting `1.355` onto Shelf $Y$), tap the **`{{key:x⇄y}}` (Swap)** key so `225` trades places into Shelf $Y$ and `1.355` sits in Shelf $X$, and tap **`{{key:÷}}`** (`{{res:sc6_01_hardware_architecture_seq_01:keys}}` $\rightarrow$ **`{{res:sc6_01_hardware_architecture_seq_01:value}}`**) to discover that one tiny battery lasts **`166.05` school days**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0.65 {{key:ENTER}}` | 0 | 0 | $0.6500$ | $0.6500$ | Awake energy rate ($0.65\text{ energy drops/hr}$) placed into Register $Y$ |
| `2 {{key:×}}` | 0 | 0 | 0 | $1.3000$ | Awake energy drops: $0.65 \times 2 = 1.30\text{ energy drops}$ in Register $X$ |
| `0.0025 {{key:ENTER}}` | 0 | $1.3000$ | $0.0025$ | $0.0025$ | Sleeping energy rate ($0.0025\text{ energy drops/hr}$) entered; awake drops lift to $Z$ |
| `22 {{key:×}}` | 0 | 0 | $1.3000$ | $0.0550$ | Sleeping energy drops: $0.0025 \times 22 = 0.055\text{ energy drops}$ in $X$; awake drops drop to $Y$ |
| `{{key:+}}` | 0 | 0 | 0 | $1.3550$ | Total daily energy drops: $1.30 + 0.055 = 1.355\text{ energy drops/day}$ |
| `225 {{key:x⇄y}}` | 0 | 0 | $225.0000$ | $1.3550$ | Enter $225\text{ total energy drops}$ and swap: 225 in $Y$, daily drops in $X$ |
| `{{key:÷}}` | 0 | 0 | 0 | $166.0517$ | Divide total energy drops by daily drops: $\approx 166.05\text{ school days}$ of power |

### Quick Care & Everyday Rescues

- **Waking a Sleeping Screen:** Tap **`{{key:C}}`** once in a well-lit room and the screen wakes up in an instant with all your stack numbers still in place.
- **Returning to Normal Numbers from a Visual Mode:** If your screen is showing ten-frames (`{{key:▦}}`), clock hands (`{{key:🕒}}`), or a number line (`{{key:LINE}}`), tap **`{{key:C}}`** once (or tap the active mode button again) to switch right back to regular numbers.
- **Adjusting Screen Contrast:** If you want the numbers darker or lighter for your room lighting, press `{{key:FLAGS}}`, press `{{key:7}}`, tap `{{key:+}}` (darker) or `{{key:-}}` (lighter), and press `{{key:ENTER}}`.
- **Starting Fresh Before a Quiz (Factory Clean Reset):** If a teacher wants to clear all saved registers and quiz scores before a class challenge, hold `{{key:C}}` down firmly, tap `{{key:OFF}}`, and release to reset the memory.
- **Adult Battery Replacement:** When the tiny battery icon appears in the top-right corner of the screen, an adult should use a coin and small screwdriver to open the child-safe rear battery door and put in a fresh CR2032 coin cell (`+` side facing up).

> **COIN CELL BATTERY INGESTION HAZARD (REESE'S LAW / 16 CFR PART 1263):** This instrument operates on a **CR2032 3.0V lithium coin cell battery**. **DEATH or serious injury can occur if ingested.** A swallowed button or coin cell battery can cause **Internal Chemical Burns in as little as 2 hours**. **KEEP new and used batteries OUT OF REACH of children.** Battery replacement must be performed exclusively by an adult, ensuring the retention fastener is securely tightened. Seek immediate medical attention if a battery is suspected to be swallowed or inserted inside any part of the body (U.S. National Battery Ingestion Hotline: **1-800-498-8666**).

---

## Where to Go Next: Companion Workbook Quests & Kitchen-Table Challenges

Ready to put your hardware and blocks to the test? Flip open the **[Big Ideas Math Middle School Supplement](../../curriculum/big-ideas-middle-school-sc6-workbook.md) — Front Matter (How to Use Your SC-6 & Math Blocks) & Unit 1, Sections 1.1–1.3**, along with your **StackCalc Student Workbook & 12-Unit Curriculum Guide** (Unit 1: *Tactile Foundations & The 4-Level Stack*), or try these three five-minute challenges at your kitchen table tonight:

1. **Hands-On Explorer — The 84 mm Height Parity & 3-Tile Ramp Test:** First, stack **12 Counting Tiles** ($12 \times 7.0\text{ mm} = 84.0\text{ mm}$) beside your **1-Whole Fraction Tower** ($84.0\text{ mm}$) and verify on your SC-6 (`12 {{key:ENTER}} 7 {{key:×}}` $\to \mathbf{84}$) that their tops sit flush. Then stack **3 Counting Tiles** ($3 \times 7.0\text{ mm} = 21.0\text{ mm}$) right behind the top edge of your SC-6 while it rests in its $15^\circ$ easel stand to feel the **`21.43` mm** lift you calculated for the reading easel ramp above.
2. **Bet Your Family! — The "No-Look" Snap-Dome Count:** Close your eyes, tap `1` `{{key:REP}}`, and click `{{key:+}}` rhythmically while counting only by the feel and sound of the $400\text{g}$ stainless-steel snap-domes under your thumb. Stop when you think you've reached `15`, open your eyes, and see if your thumb's click-counter matched the stack!
3. **Big Ideas Supplement & Quest Scoreboard Challenge:** Open the **[Big Ideas Math Middle School Supplement](../../curriculum/big-ideas-middle-school-sc6-workbook.md) (Front Matter & Unit 1, Sections 1.1–1.3)** and set up your **Quest Scoreboard** pegboard. Place your first `+10` token by building the physical block model, stack a second `+10` token by verifying on the SC-6 stack, and then tap `{{key:?}}` to run a 60-second **Level 1 Warm-Up Sprint**.

---

## Chapter Summary & Looking Ahead

The physical design of the StackCalc SC-6 and its companion blocks rests on five core elements:
1. **The Daylight Screen & 4-Level Stack ($T, Z, Y, X$):** Reading numbers comfortably under natural room light across four visible stack shelves with zero blue-light fatigue.
2. **The Big `{{key:ENTER}}` Button & 400g Tactile Keys:** Feeling each number click into Level $X$ and push smoothly upward onto Level $Y$ without needing an `=` key.
3. **Shift Key Operations (`{{key:f}}` and `{{key:g}}`):** Accessing up to three operations per button while keeping the keypad clean and uncluttered.
4. **The 3D-Printed Manipulative Studios:** Pairing physical Ten-Frames (`{{key:▦}}`), the Number Rack (`{{key:COUNT}}`), Place Value blocks (`{{key:PV}}`), 84 mm Fraction Towers, Prime Factor blocks (`{{key:FACT}}`), the Geared Clock (`{{key:🕒}}`), and Polyhedral Dice (`{{key:🎲}}`) with the live stack.
5. **The $15^\circ$ Sliding Desk Easel & Instant-On Memory:** Docking the protective cover into a hands-free reading stand while preserving every stack shelf and quiz streak in continuous memory.

Now that your desk studio is set up and your blocks are arranged in their trays, turn the page to **[Chapter 02: How Stack Math Works](02-rpn-for-young-learners.md)**—where you will ride the 4-story Number Elevator and see why stacking numbers beats parenthetical confusion every time.
