---
title: "Chapter 3: Ten-Frames, Number Lines & Place Value"
description: "Concrete manipulative integration on the SC-6: Ten-Frame Studio, Step Counter dynamics, Number Line jump arcs, Rekenrek bead racks, Place Value decomposition, and Big Numbers in Nature."
---

# Chapter 3: Ten-Frames, Number Lines & Place Value

## The Greatest Invention in Human History: How Ten Fingers and an Empty Shell Created Zero and Place Value

Five thousand years ago, across the fertile river valleys of the Tigris and Euphrates, an ancient shepherd stood before his flock at dawn. To keep account of his sheep, he dropped small clay pebbles into a woven pouch—one pebble for every sheep that passed through the wooden gate. If thirty sheep walked by, thirty pebbles weighed down his hip. But what happened when a city merchant wished to tally three thousand bushels of barley or thirty thousand bricks for a temple wall? Pockets tore; stone piles grew unmanageable; human memory buckled.

Ancient Egyptian scribes invented symbols for larger numbers: a coiled rope for one hundred, a lotus plant for one thousand, a pointing finger for ten thousand. Yet even with these hieroglyphic shortcuts, writing the number $9,999$ required thirty-six separate symbols carved into stone!

Then came what historians of mathematics document as the single greatest intellectual leap in human numbering {{cite:ifrah2000}}: **Place Value and the Invention of Zero.**

In ancient India and among the classic Maya of Mesoamerica {{cite:ifrah2000}}, thinkers made a startling realization. You do not need thousands of distinct symbols to write every number in the cosmos. You need only ten fingers, ten counting digits ($0$ through $9$), and a spatial rule: **where a symbol sits changes what it means.** An empty shell glyph drawn in the sand—or an empty groove on a counting board—told the reader: *nothing is in this column, but hold this place open!* Because an empty groove held space, a single digit $1$ could represent one sheep, ten sheep, one hundred sheep, or ten million stars simply by sliding across columns.

The decimal system was born of our anatomy: ten fleshy fingers resting on a tabletop.

On the **StackCalc SC-6**, this five-thousand-year evolution is not an abstract lecture; it is a living tactile laboratory. When you touch the precision-milled **Ten-Frame Studio** or slide the vivid dual-color beads of the **Number Rack**, you recreate the ancient counting table with your own fingers. Throughout this chapter, you will open four visual picture windows right on your keypad—`{{key:▦}}` (Ten-Frame Studio), `{{key:COUNT}}` (Number Rack), `{{key:LINE}}` (Open Number Line), and `{{key:PV}}` (Place Value X-Ray)—using `{{key:.}}` to drop single counters, combining and separating numbers on the stack, and returning to standard numbers anytime with `{{key:NUM}}`.

---

## Building Numbers: From Hands-On Blocks to the Screen Stack

Before numbers become symbols on a screen, they start as real objects in your hands {{cite:dienes1960,singapore2014}}. When you learn math on the StackCalc SC-6, you move through three steps:
1. **Hands-On Blocks (Touch It):** You build with real physical blocks, flip counters, and slide beads across rails on your desk.
2. **Picture Screen (See It):** You tap sandbox keys like `{{key:▦}}` or `{{key:LINE}}` to see your blocks mirrored as clear pictures on the daylight screen.
3. **The Number Stack (Solve It):** You combine numbers on the 4-level stack with speed and clarity.

{{blocks:ten_frames_hero|Ten-Frame Studio Physical Manipulative Kit}}
*Figure 3.1: The Ten-Frame Studio with dual-color counters. Tactile grounding for five-anchors, decade bridging, and place value.*

| Learning Phase | Physical Manipulative | SC-6 Visual Sandbox | Operational Number Stack |
|---|---|---|---|
| **1. Hands-On Blocks** | Ten-Frame Trays & Dual-Color Disks | Hands-on physical token placement | Sensory tactile certainty |
| **2. Visual Screen** | 20-Bead Rekenrek Number Rack | High-contrast `{{key:▦}}` and `{{key:COUNT}}` LCD vector grids | Visual subgroup perception |
| **3. Number Stack** | Place Value Studio | `{{key:LINE}}` jump arcs and `{{key:PV}}` Place Value mode | 4-Register RPN stack arithmetic |

When learners skip hands-on blocks and visual models and jump straight into symbolic calculation on conventional calculators, math can feel like a set of arbitrary rules without conceptual grounding. When faced with an expression such as $8 + 5$, numerals can seem like disconnected symbols and the equal sign (`=`) like a magic black box.

The **StackCalc SC-6** was engineered specifically to give you direct physical grounding. By pairing physical, open-source 3D-printed math manipulatives with dedicated hardware visual sandbox keys (`{{key:▦}}`, `{{key:COUNT}}`, `{{key:LINE}}`, `{{key:PV}}`), the SC-6 bridges the tactile world of physical objects directly into the spatial logic of the RPN operational stack.

{{res:sc6_ten_frame_8_plus_5:screenshot|SC-6 Ten-Frame Studio Mode: Bridging Ten with 8 + 5 = 13}}
*Figure 3.2: SC-6 Ten-Frame Studio mode (`{{key:▦}}`) bridging across 10 with $8 + 5 = 10 + 3 = 13$.*

### The Ten-Step Triangle Staircase (A Preview of Chapter 4's Multiplication Shortcut)

Have you ever tried adding all the counting numbers from $1$ to $10$ ($1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10$) without losing track halfway through? Long before you meet the famous story that opens Chapter 4, you can discover the secret right on your desk by pairing Friends of Ten with your $7.0\text{ mm}$ ($1\text{U}$) **Unit Miniblocks**, the $70.0\text{ mm}$ ($10\text{U}$) **10-Rod**, and your **Number Rack**:
1. **Build the Staircase:** Line up towers of $1, 2, 3, 4, 5, 6, 7, 8, 9$ Unit Miniblocks ($7.0\text{ mm}$ visible height per block) beside your $70.0\text{ mm}$ 10-Rod ($10$). It forms a 10-step triangle staircase climbing in $7.0\text{ mm}$ steps up to $70.0\text{ mm}$.
2. **Fold the Staircase into $70.0\text{ mm}$ Ten-Towers:** Pick up the smallest step ($1\text{ block}$, $7.0\text{ mm}$) and dock it on top of the $9\text{-block}$ step ($63.0\text{ mm}$)—together they stand exactly $70.0\text{ mm}$ tall, flush with the **10-Rod ($1 + 9 = 10$)**. Next, dock the $2\text{-block}$ step on the $8\text{-block}$ step ($2 + 8 = 10$), the $3\text{-block}$ step on the $7\text{-block}$ step ($3 + 7 = 10$), and the $4\text{-block}$ step on the $6\text{-block}$ step ($4 + 6 = 10$).
3. **Count Your Ten-Towers at a Glance:** You now have **five full $70.0\text{ mm}$ Ten-Towers** ($10$, $9+1$, $8+2$, $7+3$, and $6+4$, worth $5 \times 10 = 50$) plus the single middle tower of **$5$ Unit Miniblocks** ($35.0\text{ mm}$) standing by itself: $50 + 5 = \mathbf{55}$!

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `10 {{key:ENTER}} 11 {{key:×}}` | 0 | 0 | 0 | 110 | Double staircase forms a $10 \times 11 = 110$ rectangle |
| 2 | `2 {{key:÷}}` | 0 | 0 | 0 | **55** | Half the rectangle gives the staircase sum $1 + \dots + 10 = 55$ |

---

### Seeing Groups Instantly Without Counting One-by-One

Have you ever rolled a dot die and known right away it was a 5, without having to point your finger and count $1, 2, 3, 4, 5$? That skill is called **seeing groups at a glance** (or **subitizing**). 

When you look at small groups of dots, blocks, or counters, your brain recognizes the total in a split second. By organizing numbers around friendly landmarks of **5** and **10**, the SC-6 and your Ten-Frame Studio let you see big numbers just as easily as small numbers—without counting on your fingers.

**Subitizing** is your brain's ability to see how many items are in a small group right away without counting them one by one. It works in two helpful ways:
- **Small Groups ($1$ to $4$):** When you look at $1, 2, 3,$ or $4$ counters on your desk, you recognize the total right away without counting.
- **Combining Friendly Groups ($5$ to $10+$):** For larger numbers, your eyes spot smaller groups and snap them together. When you see $7$ dots arranged in a ten-frame, you don't count $1, 2, 3, 4, 5, 6, 7$—you immediately see a full top row of $5$ plus $2$ more on the bottom ($5 + 2 = 7$).

The SC-6 visual screens are built around friendly landmarks of **5** and **10** so your eyes can always spot the pattern at a glance.

---

### How Your Trays and Counters Are Built for Your Hands

The physical manipulative studios accompanying the SC-6 are engineered as modular tactile companions, standardized on the Gridfinity organization grid. Where the calculator provides a dark, glare-free slate upon which numbers are evaluated, the manipulative blocks supply immediate physical mass and vibrant color:

- **Ten-Frame Studio & Dual-Color Counters:** Dual ten-frame wells separated by a raised divider rib. The physical tactile ridge provides an unmistakable boundary at five, allowing fingers to spot group sizes at a glance (subitizing) without counting one by one. Chamfered counter disks in contrasting coral and amber seat firmly into each pocket.
- **Number Rack (Rekenrek):** Dual horizontal stainless guide rails holding smoothly sliding beads arranged in five-and-five color clusters, mirroring the two-register display of the calculator.
- **Place Value Studio:** Dual $4 \times 2$ desktop Place Value Activity Trays—the **Whole Numbers Tray** (`THOUSANDS | HUNDREDS | TENS | ONES`) and **Decimal Numbers Tray** (`ONES • TENTHS | HUNDREDTHS | THOUSANDTHS`)—paired with 44 digit miniblocks (`0`–`9`) and 9 stackable `+1` regrouping unit miniblocks ($19.0 \times 19.0 \times 7.0\text{ mm}$ visible $1\text{U}$ height, where 10 stacked unit blocks match the $70.0\text{ mm}$ Ten-Frame 10-Rod).
- **Counting & Array Tiles:** Interlocking tactile tiles engineered with smooth slip-fit tabs that assemble into flat 2D arrays and vertical counting towers.
- **Prime Factor Studio:** Color-coded blocks for the prime numbers ($2$, $3$, $5$, and $7$) whose heights stack together so you can see and feel how prime factors multiply to build composite numbers.

---

## Inside the Ten-Frame Studio (`{{key:▦}}`): A Picture Window Into Your Stack

Think of the four visual sandbox keys (`{{key:▦}}`, `{{key:COUNT}}`, `{{key:LINE}}`, and `{{key:PV}}`) as special camera lenses that let you peek inside your calculator's shelves and *see* your numbers as real blocks, beads, and number trails.

The first lens is the **Ten-Frame Studio (`{{key:▦}}`)**. It arranges numbers in neat groups of five and ten so your eyes can spot how many counters you have at a glance—and how many empty pockets are left to reach the next ten!

> **Why Your Physical Ten-Frame Tray Has a Center Ridge:**  
> Run your finger across your physical Ten-Frame Studio tray and you will feel a raised central divider rib splitting the two $2 \times 5$ ten-frame wells. That ridge separates the first five pockets from the second five pockets, so your eyes and fingertips can recognize a full row of five immediately without counting one by one.

### Opening the Ten-Frame Window
Suppose you type `{{key:7}}` onto Ground Shelf $X$ and press `{{key:▦}}`. Right away, the screen opens a split picture window: the top half draws two ten-frame trays with **7 round counters** tucked inside, while the bottom half keeps your live $Y$ and $X$ shelves in plain view:

| Display Region | Visual & Numeric Representation (`X = 7`) |
| :--- | :--- |
| **Upper Screen (Ten-Frame Grid)** | Top row: `[●][●][●][●][●]` ($5$ filled); Bottom row: `[●][●][ ][ ][ ]` ($2$ filled, $3$ empty) |
| **Lower Screen (Active Stack)** | `Y: 0` $\mid$ **`X: 7`** ($5 + 2 = 7$ seen at a glance) |

Look at how those 7 counters sit inside the first frame: the top row is completely full with 5 counters, the bottom row holds 2 counters, and 3 empty pockets are waiting at the end of the row (while the second ten-frame sits empty). You don't need to count $1, 2, 3, 4, 5, 6, 7$. Your eyes immediately see a full row of 5 plus 2 more on the bottom ($5 + 2 = 7$)—and you can see at a glance that **3 empty pockets** are waiting to make a full 10!

### Dropping Counters One by One with the Decimal Key (`{{key:.}}`)
While you are inside the Ten-Frame Studio, the decimal key `{{key:.}}` acts like your own hand dropping counters into the tray one at a time. Starting from $X = 7$, watch what happens each time you tap `{{key:.}}`:
- Tap `{{key:.}}` once and an 8th counter drops into the bottom row ($X = 8$).
- Tap `{{key:.}}` again and a 9th counter lands next to it ($X = 9$), leaving just **1 empty pocket** in the first frame.
- Tap `{{key:.}}` a third time and the 10th counter snaps that last pocket shut ($X = 10$)! The border of the first ten-frame flashes briefly to celebrate that you have built one complete group of ten.
- Tap `{{key:.}}` one more time ($X = 11$) and the 11th counter hops across the center divider ridge into the first pocket of Frame 2, showing $10 + 1 = 11$ right before your eyes.

> **Spotting the Partner to Ten:** Whenever a number under 10 is sitting in the Ten-Frame Studio, just count the empty pockets in Frame 1 to find its "Friend of Ten." With 7 counters in the tray, you see 3 empty pockets—so pressing `{{key:3}}` `{{key:+}}` fills the frame completely and lands on $X = \mathbf{10}$.

---

## Making Ten & The "Bridging Ten" Strategy

When you first add across a ten boundary (like $8 + 5$), counting on your fingers (*"eight... nine, ten, eleven, twelve, thirteen"*) can feel slow and tricky. The Ten-Frame Studio shows you a much faster way called **Bridging Ten**: instead of counting by ones, you borrow just enough counters from the second number to finish filling the first tray of 10, and drop the leftovers into the second tray!
$$\mathbf{8 + 5 = 8 + (2 + 3) = (8 + 2) + 3 = 10 + 3 = 13}$$

### How Your Eyes Bridge Across Ten
Picture starting with **8 counters** in Frame 1 (`[●][●][●][●][●] | [●][●][●][ ][ ]`), which leaves **2 empty pockets**. You are holding **5 counters** in your hand to add. Instead of adding all 5 at once, split your 5 into **`2 + 3`**:
1. Drop **2 counters** into the two empty pockets of Frame 1 (`[●][●][●][●][●] | [●][●][●][●][●]`) to lock in a **Full 10**.
2. Drop the remaining **3 counters** into the fresh second frame (`[●][●][●][ ][ ] | [ ][ ][ ][ ][ ]`).
3. Now read the two trays together: **1 full tray of 10 + 3 extras = 13!** On your SC-6, key in `{{res:sc6_ten_frame_8_plus_5:keys}}` to see **`{{res:sc6_ten_frame_8_plus_5:value}}`**.

### Try Bridging Ten with Your Dual-Color Counters and Screen

{{blocks:ten_frame_bridging_ten|Ten-Frame Studio: Bridging Ten Strategy (8 + 5 = 13)}}

First, build the bridge on your desk: place 8 coral-red counters into Frame 1 of your physical tray (filling the top row of 5 and 3 pockets on the bottom row), and hold 5 amber-gold counters in your hand. Because Frame 1 has 2 empty pockets waiting, drop 2 gold counters in to complete the ten ($8 + 2 = 10$), then place the remaining 3 gold counters into Frame 2 ($10 + 3 = 13$).

Now watch the exact same bridge happen on your Ten-Frame screen: press `{{key:8}} {{key:▦}}` to see 8 dots in Frame 1, tap `{{key:2}} {{key:+}}` to fill Frame 1 and flash the completed ten ($X = \mathbf{10}$), and tap `{{key:3}} {{key:+}}` to land the remaining 3 counters in Frame 2 ($X = \mathbf{13}$):

| Keystroke | Register T | Register Z | Register Y | Register X (Display) |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:8}} {{key:▦}}` | 0 | 0 | 0 | 8 |
| `{{key:2}} {{key:+}}` | 0 | 0 | 0 | 10 |
| `{{key:3}} {{key:+}}` | 0 | 0 | 0 | 13 |

### The Bioluminescent Nature Lab: Ten-Frames & Bridging Ten in Action
To see how Ten-Frames and Bridging Ten help real scientists in the field, step into the shoes of a junior field biologist inside a glowing rainforest nature dome! Researchers bring in firefly terrariums, meteorite fragments, crystal geodes, weather sensors, and glowing algae tubes. Using your Ten-Frame trays (`{{key:▦}}`) and the SC-6 stack, you will spot groups at a glance, bridge across 10 without counting on your fingers, and step back across 10 with ease.

Your first stop in the rainforest dome is a glass terrarium where 5 glowing lantern fireflies rest on the top branch. Just after dusk, 3 more fireflies land on the lower fern branch, and your lab partner asks how many fireflies are glowing in the terrarium altogether. On your Ten-Frame tray, fill the top row of Frame 1 with 5 counters and place 3 counters on the bottom row. Because the top row of a ten-frame always holds 5, your eyes immediately see *"5 on top and 3 on the bottom makes 8"*—zero finger-counting needed! When you lift the 5 upper fireflies onto Shelf $Y$ and add the 3 lower fireflies by pressing `{{res:sc6_03_counting_place_value_seq_02:keys}}`, the stack combines both branches to show **`{{res:sc6_03_counting_place_value_seq_02:value}}`** glowing fireflies on Ground Shelf $X$.

Right beside the firefly habitat, a planetary geologist is sorting magnetic iron meteorite pebbles into 10-slot specimen trays. The first tray already holds 9 pebbles, and a rover scoop delivers 4 more pebbles from a crater rim. What happens when we add $9 + 4$ across the 10-boundary? Look at your Ten-Frame tray: with 9 counters in Frame 1, there is only **1 empty pocket** left. Instead of counting upward by ones, split your 4 new pebbles into **$1 + 3$** so 1 pebble snaps the first tray shut at 10, and the other 3 pebbles land in Frame 2: pressing `{{res:sc6_03_counting_place_value_seq_03:keys}}` bridges cleanly through $10$ and lands on **`{{res:sc6_03_counting_place_value_seq_03:value}}`** pebbles.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `9 {{key:ENTER}}` | 0 | 0 | 9 | 9 | Load 9 meteorite pebbles into $X$ and duplicate to Mezzanine $Y$ |
| `1 {{key:+}}` | 0 | 0 | 0 | 10 | Bridge to ten; Frame 1 completely fills and flashes ($X = 10$) |
| `3 {{key:+}}` | 0 | 0 | 0 | 13 | Combine ten and three; Frame 2 holds 3 dots, giving total $X = 13$ pebbles |

Once Frame 1 locks in at 10, adding the remaining 3 pebbles is an instant visual snap ($10 + 3 = 13$).

Walking deeper into the geology alcove, a cave explorer cracks open a limestone boulder and finds 7 purple amethyst crystals in the first pocket and 6 sparkling quartz crystals in the second pocket. How does that same Bridging Ten trick work when we start at 7 instead of 9? On your Ten-Frame tray, 7 counters fill the top row of 5 plus 2 on the bottom row, leaving **3 empty pockets** in Frame 1—which invites you to split the 6 quartz crystals into twin halves ($3 + 3$). Watch how the shelves and the Ten-Frame screen move in lockstep as you key in `{{res:sc6_03_counting_place_value_seq_05:keys}}` to reach **`{{res:sc6_03_counting_place_value_seq_05:value}}`**: first, `7 {{key:ENTER}}` loads the 7 amethyst crystals into Ground Shelf $X$ and duplicates them onto Waiting Shelf $Y$. Next, typing `3 {{key:+}}` drops the first 3 quartz crystals into those 3 empty pockets—snapping Frame 1 completely full so the display flashes the clean benchmark `10` ($X = 10$). Then a second `3 {{key:+}}` places the remaining 3 quartz crystals into the top row of Frame 2, uniting 1 full ten-frame with 3 loose crystals to display `13` ($X = 13$). Even better, notice that right after the first `3 {{key:+}}` reaches 10, the number `3` is already sitting in your `LASTX` backup memory—so you can also tap `{{key:LASTX}} {{key:+}}` to add the second 3 without even typing the digit again!

From the crystal alcove, you step out onto the dome's canopy deck carrying a foam launch case that holds a full set of 10 micro-weather sensors. Your team clips 4 sensors onto kite strings and launches them into the rainforest wind, leaving the rest in the case. Fill Frame 1 with all 10 counters and pop 4 counters out to see the full top row of 5 plus 1 counter on the bottom row ($6$). When you load the full crate onto Shelf $Y$ and subtract the 4 launched sensors by pressing `{{res:sc6_03_counting_place_value_seq_07:keys}}`, Ground Shelf $X$ immediately shows **`{{res:sc6_03_counting_place_value_seq_07:value}}`** sensors still nestled in the foam case. *(Want to prove none were lost when you reel the kites back in? Tap `{{key:LASTX}} {{key:+}}` and watch the 4 launched sensors reunite with the 6 in the crate to restore `10`!)*

Back inside the wet lab, a bioluminescence rack holds 14 glowing algae test tubes—1 full rack of 10 plus 4 extra tubes in the second rack—and a student scientist takes 6 tubes to the microscope station. Just as we bridged *forward* across 10 with the meteorite pebbles and geode crystals, we can bridge *backward* across 10 when subtracting $14 - 6$! Instead of counting backward one by one, hop back to the landmark 10 first by splitting the 6 tubes you are removing into **$4 + 2$**: first remove all 4 tubes from Frame 2 (leaving a clean 10 in Frame 1), then take 2 more tubes from Frame 1. Pressing `{{res:sc6_03_counting_place_value_seq_08:keys}}` steps back to `10` and then down to **`{{res:sc6_03_counting_place_value_seq_08:value}}`** glowing tubes.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `14 {{key:ENTER}}` | 0 | 0 | 14 | 14 | Load 14 glow-tubes into $X$ and duplicate to Mezzanine $Y$ |
| `4 {{key:-}}` | 0 | 0 | 0 | 10 | First subtraction empties Frame 2, leaving clean benchmark ten ($X = 10$) |
| `2 {{key:-}}` | 0 | 0 | 0 | 8 | Second subtraction takes 2 from Frame 1, leaving 8 glow-tubes ($X = 8$) |

Splitting $-6$ into $-4$ and $-2$ turns a tricky teen subtraction into two effortless mental hops ($14 \to 10 \to 8$).

---

## Step-Counter Towers & Stacking Tile Heights

Have you ever noticed that counting forward ($1, 2, 3, 4 \dots$) is really just adding $1$ over and over again? On a regular calculator, pressing `+ 1 = = =` hides the `+ 1` inside a secret memory box. On your SC-6, you can watch the `1` sit right on your waiting shelf while you stack real $7.0\text{ mm}$ counting tiles into a rising tower on your desk!

### Building a 12-Story Tower up to 84 Millimeters

{{blocks:counting_tiles_fraction_datum_84mm|Master Datum Alignment: 12 Counting Tiles (12 x 7.0 mm = 84.0 mm) Flush with 1-Whole Fraction Tower}}

Every interlocking Counting Tile adds exactly $7.0\text{ mm}$ of visible height. As you snap them together one by one, watch how your growing tower matches the heights of your **84 mm Fraction Studio** blocks:

| Stacked Tile Count (`X`) | Cumulative Physical Height | Geometric & Fraction Studio Datum |
| :---: | :---: | :--- |
| **Tile 1 (`X = 1`)** | $7.0\text{ mm}$ | $1\text{U}$ visible increment $= 1/12$ Fraction Tower |
| **Tile 2 (`X = 2`)** | $14.0\text{ mm}$ | $1/6$ Fraction Tower datum |
| **Tile 3 (`X = 3`)** | $21.0\text{ mm}$ | $1$ Unit Cube equivalent $= 1/4$ Fraction Tower |
| **Tile 4 (`X = 4`)** | $28.0\text{ mm}$ | $1/3$ Fraction Tower datum |
| **Tile 6 (`X = 6`)** | $42.0\text{ mm}$ | Halfway datum $= 1/2$ Fraction Tower |
| **Tile 12 (`X = 12`)** | $84.0\text{ mm}$ | Full $1\text{-Whole}$ Master Fraction Tower |

You can climb—and count down—that 12-story tile tower on your calculator in three different ways, depending on how many shelves your elevator is using. First, try climbing in **2-Shelf Mode (`{{key:FLAGS}}` $\to$ `2-LV`)**: place 1 white tile on your desk ($7.0\text{ mm}$) and press `{{res:sc6_03_counting_place_value_seq_39:keys}}` to reach $X = 2$ as you snap a second tile on top ($14.0\text{ mm}$). Because Shelf $Y$ is the top shelf in `2-LV` mode, it keeps `1` locked in place—so every time you snap another tile onto your tower and tap `{{key:+}}`, the screen climbs in lockstep ($3, 4, 5 \dots 12$). When you snap the 12th tile on top, stand your 12-tile stack next to the white **1-Whole Fraction Tower**: both stand at the exact same **$84.0\text{ mm}$** height!

| Keystroke | Register Y (Constant) | Register X (Display) | Physical Tile Height on Desk (7.0 mm per Tile) |
| :--- | :--- | :--- | :--- |
| `{{key:1}} {{key:ENTER}}` | 1 | 1 | 1 Tile  =  7.0 mm |
| `{{key:1}}` | 1 | 1 | 1 Tile  =  7.0 mm |
| `{{key:+}}` | 1 | 2 | 2 Tiles = 14.0 mm |
| `{{key:+}}` | 1 | 3 | 3 Tiles = 21.0 mm (1 Unit Cube) |
| `{{key:+}}` | 1 | 4 | 4 Tiles = 28.0 mm |
| `{{key:+}}` | 1 | 5 | 5 Tiles = 35.0 mm |
| `{{key:+}}` | 1 | 6 | 6 Tiles = 42.0 mm (1/2 Whole Tower) |
| `{{key:+}}` | 1 | 7 | 7 Tiles = 49.0 mm |
| `{{key:+}}` | 1 | 8 | 8 Tiles = 56.0 mm |
| `{{key:+}}` | 1 | 9 | 9 Tiles = 63.0 mm |
| `{{key:+}}` | 1 | 10 | 10 Tiles = 70.0 mm |
| `{{key:+}}` | 1 | 11 | 11 Tiles = 77.0 mm |
| `{{key:+}}` | 1 | 12 | 12 Tiles = 84.0 mm (1 Whole Tower!) |

Second, what if you are in standard **4-Shelf Mode (`4-LV`)**? Press `{{key:1}} {{key:REP}}` first! Constant Repeat copies `1` onto all four shelves ($T, Z, Y, X$), so every tap of `{{key:+}}` feeds a fresh `1` down from the Penthouse roof ($2, 3, 4, 5, 6 \dots$):

| Keystroke | Register T (Constant) | Register Z | Register Y | Register X (Display) |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:1}}` | 0 | 0 | 0 | 1 |
| `{{key:REP}}` | 1 | 1 | 1 | 1 |
| `{{key:+}}` | 1 | 1 | 1 | 2 |
| `{{key:+}}` | 1 | 1 | 1 | 3 |
| `{{key:+}}` | 1 | 1 | 1 | 4 |
| `{{key:+}}` | 1 | 1 | 1 | 5 |
| `{{key:+}}` | 1 | 1 | 1 | 6 |

Third, you can run a **Rocket Launch Countdown** by unstacking a 10-tile tower ($70.0\text{ mm}$) one block at a time: key in `{{key:1}} {{key:0}} {{key:ENTER}} {{key:1}}`, pop 1 tile off the top of your tower as you tap `{{key:-}}` ($X = \mathbf{9}$), and keep unstacking down to $X = \mathbf{0}$—Blast off!

| Keystroke | Register Y | Register X |
| :--- | :--- | :--- |
| `10 {{key:ENTER}}` | 10 | 10 |
| `{{key:1}} {{key:-}}` | 10 | 9 |
| `{{key:-}}` | 10 | 8 |
| `{{key:-}}` | 10 | 7 |
| `{{key:-}}` | 10 | 6 |
| `{{key:-}}` | 10 | 5 |
| `{{key:-}}` | 10 | 4 |
| `{{key:-}}` | 10 | 3 |
| `{{key:-}}` | 10 | 2 |
| `{{key:-}}` | 10 | 1 |
| `{{key:-}}` | 10 | 0 |

### Observatory Step Ladders & Rhythmic Countdowns
Now let's take those step-counting ladders up to a mountaintop astronomical observatory! Inside the optics and planetary motion labs, technicians calibrate paired sensors, launch weather balloons, and track orbiting moons using rhythmic step-counting ladders in 2-Shelf (`2-LV`) and 4-Shelf (`4-LV`) modes.

In the observatory optics lab, technicians calibrate paired star sensors by counting by 2s up to 20. Remember our step-counter discovery from Chapter 2: in **2-Shelf mode (`2-LV`)**, Shelf $Y$ is the roof of the stack, so it holds onto your step size (`2`) across every single tap of `{{key:+}}`! Switch to `{{key:FLAGS}} 2-LV` and climb the twos ladder by pressing `{{res:sc6_03_counting_place_value_seq_44:keys}}`, which steps evenly by twos all the way to **`{{res:sc6_03_counting_place_value_seq_44:value}}`**. After `2 {{key:ENTER}} 2 {{key:+}}` shows $Y = 2,\; X = 4$, each rhythmic tap of `{{key:+}}` advances through $6, 8, 10, 12, 14, 16, 18,$ up to $20$ while Shelf $Y$ keeps the constant `2` locked in place.

Once the star sensors are calibrated, you step out onto the observatory roof deck, where the flight director prepares to launch a high-altitude weather balloon by counting down from 50 to 0 by 5s. Each `5 {{key:-}}` step drops the countdown by 5 in a steady rhythm until liftoff at zero: keying in `{{res:sc6_03_counting_place_value_seq_47:keys}}` steps down five meters of cable at a time until Ground Shelf $X$ reaches **`{{res:sc6_03_counting_place_value_seq_47:value}}`**. Starting with `50 {{key:ENTER}} 5 {{key:-}}` $\to$ $45$, nine more steps count down through $40, 35, 30, \dots, 0$ to reach liftoff at $X = 0$! *(Tip: You can also press `{{key:LASTX}} {{key:-}}` to reuse the `5` from `LASTX`.)*

What if you want a one-tap skip-counting ladder with `{{key:REP}}` while staying in standard **4-Shelf mode (`4-LV`)**? Back inside the planetary motion lab, astronomers track Jupiter's three locked Galilean moons (Io, Europa, and Ganymede) by generating multiples of 3. Pressing Constant Repeat (`{{key:REP}}`) fills all four floors ($T, Z, Y, X$) with `3`, so every tap of `{{key:+}}` automatically feeds a fresh `3` down from the Penthouse roof: `3 {{key:REP}} {{key:+}} {{key:+}} {{key:+}}`.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `3 {{key:REP}}` | 3 | 3 | 3 | 3 | The `{{key:REP}}` repeat key replicates 3 across all registers ($T, Z, Y, X$) |
| `{{key:+}}` | 3 | 3 | 3 | 6 | First addition yields 6; register $T$ preserves constant 3 |
| `{{key:+}}` | 3 | 3 | 3 | 9 | Stack drop supplies 3 automatically; total reaches 9 |
| `{{key:+}}` | 3 | 3 | 3 | 12 | Constant replicates from top of stack ($X = 12$) |

Because Penthouse $T$ copies itself every time the stack drops, you never run out of 3s!

---

### Why Adding Odd Numbers Always Builds a Square (The L-Shape Pattern)

Here is one of the coolest number mysteries in all of mathematics. Look at what happens when you add consecutive **odd numbers** starting from $1$:
$$1 = 1 = 1^2$$
$$1 + 3 = 4 = 2^2$$
$$1 + 3 + 5 = 9 = 3^2$$
$$1 + 3 + 5 + 7 = 16 = 4^2$$
$$1 + 3 + 5 + 7 + 9 = 25 = 5^2$$

Wait—why does adding odd numbers ($1, 3, 5, 7, 9 \dots$) *always* produce a perfect square number ($1, 4, 9, 16, 25 \dots$) without a single exception?

You can solve this mystery with your own hands in thirty seconds! Grab 16 Counting Tiles from your **Counting & Array Studio**—**1 White**, **3 Cobalt Blue**, **5 Radiant Gold**, and **7 Slate Gray**—and build the pattern right on your desk:

1. **Stage 1 ($1\text{ Tile} = 1 \times 1$):** Place **1 White tile** in the bottom-left corner of your desk mat. That single tile is a tiny $1 \times 1$ square ($1$).
2. **Stage 2 ($1 + 3 = 4\text{ Tiles} = 2 \times 2$):** Now ask yourself: *what do I need to add to make this $1 \times 1$ square grow into a $2 \times 2$ square?* You need **1 tile on top**, **1 tile on the right side**, and **1 corner tile** where they meet ($1 + 1 + 1 = 3$). Wrap those **3 Blue tiles** around the White tile like an L-shaped collar—and look down: you have a solid **$2 \times 2 = 4$ square**!
3. **Stage 3 ($1 + 3 + 5 = 9\text{ Tiles} = 3 \times 3$):** To grow your $2 \times 2$ square into a $3 \times 3$ square, you must cover its **2 top edges**, its **2 right edges**, plus **1 new corner tile** ($2 + 2 + 1 = 5$). Wrap **5 Gold tiles** around the corner to complete a **$3 \times 3 = 9$ square**!
4. **Stage 4 ($1 + 3 + 5 + 7 = 16\text{ Tiles} = 4 \times 4$):** To grow from $3 \times 3$ to $4 \times 4$, you need **3 tiles on top**, **3 tiles on the right**, and **1 corner tile** ($3 + 3 + 1 = 7$). Wrap **7 Gray tiles** around the outside to lock in a **$4 \times 4 = 16$ square**!

Now you see the secret: **every odd number is really two matching side arms plus one corner tile!** Whenever you wrap that L-shaped border around a square, it grows the width by 1 and the height by 1 at the exact same time.

You can watch those growing squares form right on the SC-6 stack—and even go beyond the 16 tiles on your desk to build $5 \times 5$ and $6 \times 6$ squares before checking the final side length with the square-root key (`{{key:√x}}`). Start by pressing `{{res:sc6_03_counting_place_value_seq_40:keys}}` to reach $\mathbf{4}$ ($2^2$), matching your 1 white center tile ($Y = 1$) wrapped by a 3-tile blue L-border ($X = 4$). Next, tap `{{key:5}} {{key:+}}` to wrap the 5-tile gold border around the corner and reach $\mathbf{9}$ ($3 \times 3$ square), then tap `{{key:7}} {{key:+}}` to wrap the 7-tile gray border and lock in $\mathbf{16}$ ($4 \times 4$ square). Keep the pattern rolling by tapping `{{key:9}} {{key:+}}` to wrap a 9-tile border into $\mathbf{25}$ ($5 \times 5$ square), and finally tap `{{res:sc6_03_counting_place_value_seq_41:keys}}` to wrap an 11-tile border into $\mathbf{36}$ ($6 \times 6$ square) before pressing `{{key:√x}}` to reveal $\mathbf{6}$—the exact side length of your $6 \times 6$ square!

---

### How Triangular Step Ladders Build Rectangular Arrays

Earlier in this chapter, we folded a 10-step staircase of blocks into Friends of Ten ($1 + 2 + \dots + 10 = 55$). Now let's discover an even more powerful geometric trick that works for *any* staircase of counting numbers—like $1 + 2 + 3 + 4 + 5 + 6 = 21$.

Using your **24-Tile Four-Color Counting & Array Studio**, build six rising columns of tiles on your desk: $1\text{ tile}$, then $2\text{ tiles}$, then $3, 4, 5,$ and $6\text{ tiles}$. Notice how your 21 tiles form a right triangle whose top edge climbs in a jagged 6-step staircase.

How can you find the area of a jagged triangle without adding every column one by one? Imagine a friend builds an identical 21-tile staircase ($1 + 2 + 3 + 4 + 5 + 6$) and flips theirs **upside-down** right on top of yours:
- Their tallest column of **$6$** lands on top of your shortest step of **$1$**, making a column **$7$ tiles tall** ($1 + 6 = 7$).
- Their step of **$5$** lands on your step of **$2$**, also making **$7$ tiles tall** ($2 + 5 = 7$).
- Every single column locks together at **$7$ tiles tall** across all **$6$ columns**—forming a solid **$6 \times 7 = 42$ rectangle**! (And even with a single 24-tile kit, you can fold your 6-step staircase in half—snapping $1$ onto $6$, $2$ onto $5$, and $3$ onto $4$—to form a $3 \times 7 = 21$ rectangle.)

Because two identical staircases make a $6 \times 7 = 42$ rectangle, **one** staircase is simply half of that rectangle ($42 \div 2 = 21$):

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `6 {{key:ENTER}}` | 0 | 0 | 6 | 6 | Place 6 staircase columns onto Mezzanine $Y$ |
| `7 {{key:×}}` | 0 | 0 | 0 | 42 | Two interlocked staircases form a $6 \times 7 = 42$ rectangle ($X = 42$) |
| `2 {{key:÷}}` | 0 | 0 | 0 | 21 | Half the rectangle gives one triangular staircase ($42 \div 2 = 21$) |

Remember this *"put two staircases together into a rectangle and cut it in half"* secret—at the start of Chapter 4, you will see how a 9-year-old boy used this exact trick to add $1$ through $100$ in seconds!

---

## Number Line Navigation & Visual Jump Arcs (`{{key:LINE}}`)

If the Ten-Frame Studio lets you see numbers as trays of counters, the **Open Number Line (`{{key:LINE}}`)** turns addition and subtraction into a hiking trail across your screen.

### Watching Your Numbers Leap Across the Trail
Whenever you press `{{key:LINE}}`, the top half of your screen draws a crisp ruler trail that automatically scales its tick marks ($1, 2, 5,$ or $10$) to fit your journey. Then, as soon as you add or subtract, a curved **jump arc** leaps from your starting milepost to your landing spot:

| Display Zone | Visual Representation (`2 + 5 = 7`) |
| :--- | :--- |
| **Jump Arc Layer** | Curved forward jump arc labeled `+5` spanning from tick `2` to tick `7` |
| **Number Line Axis** | High-contrast tick ruler spanning `0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11` |
| **Register `Y:`** | `2` (Starting coordinate) |
| **Register `X:`** | `7` (Landing coordinate after `+5` jump) |

### Forward Hops, Backward Hops & The `{{key:LASTX}}` Return Trip
Watching the arc leap across the screen connects three ideas at once—where you started ($Y$), how far and which way you hopped, and where you landed ($X$):
- **Forward Jump (Addition):** When you key in `2 {{key:ENTER}} 5 {{key:+}}` (or `14 {{key:ENTER}} 8 {{key:+}}` $\to 22$), an arc sweeps **to the right**, labeled `+5` (or `+8`), showing your number growing along the trail.
- **Backward Jump (Subtraction):** When you key in `9 {{key:ENTER}} 4 {{key:-}}` (or `22 {{key:ENTER}} 5 {{key:-}}` $\to 17$), an arc leaps **to the left**, labeled `-4` (or `-5`), showing you walking back down the trail.
- **The `{{key:LASTX}}` Return-Trip Trick:** Want to hop right back to your starting milepost without re-typing your jump size? Right after `14 {{key:ENTER}} 8 {{key:+}}` lands on `22`, tap `{{key:LASTX}} {{key:-}}`—`LASTX` remembers your `8`-step jump and arcs straight back to `14`!

### The Kangaroo Trailblazer: Tracking Hops Across the Outback
To see how the Open Number Line (`{{key:LINE}}`) turns real-world distances and elevations into visual jump arcs, join a wildlife tracking team mapping the Australian Outback trail!

At the start of the trail, an Australian red kangaroo rests at kilometer marker 14 near a dry creek bed, then bounds forward 8 kilometers across the red sand plains to reach fresh desert grass. Which trail marker does the kangaroo reach? On your Open Number Line (`{{key:LINE}}`), start at tick 14 and launch a forward arc of `+8`. Just like bridging across 10 on a ten-frame, your mind can hop $+6$ to land on milestone 20 and $+2$ more to reach marker 22: when you press `{{res:sc6_03_counting_place_value_seq_18:keys}}`, the jump arc sweeps across the twenty mark and lands squarely on kilometer **`{{res:sc6_03_counting_place_value_seq_18:value}}`**.

A little farther along the trail, an outback scout stands atop a towering red sand dune at elevation 23 meters, then hikes down 7 meters into a shaded eucalyptus grove. To find the grove's elevation on the number line, pin tick 23 on your Open Number Line and launch a backward arc of `-7` across benchmark 20—stepping back 3 meters to hit 20, and 4 more meters to land on 16: pressing `{{res:sc6_03_counting_place_value_seq_19:keys}}` traces the downward hike to **`{{res:sc6_03_counting_place_value_seq_19:value}}`** meters. *(Now try the **Instant Reverse-Hop Check**: press `{{key:LASTX}} {{key:+}}` and watch the `-7` hike sitting in `LASTX` reverse into a `+7` climb right back to `23`!)*

From that shaded eucalyptus grove, your survey team maps a three-part trek across the bush: 18 kilometers from base camp to Spinifex Ridge, 5 kilometers to the Giant Boab Tree, and 7 kilometers to the Emerald Billabong. Watch how automatic stack lift chains the two forward jump arcs (`+5` then `+7`, which together add $+12$ onto $18$) to land right on a round decade milestone: keying in `{{res:sc6_03_counting_place_value_seq_20:keys}}` advances from marker `18` to `23` and then lands on **`{{res:sc6_03_counting_place_value_seq_20:value}}`** kilometers.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `18 {{key:ENTER}}` | 0 | 0 | 18 | 18 | Pin Spinifex Ridge distance 18 into $X$ and duplicate to Mezzanine $Y$ |
| `5 {{key:+}}` | 0 | 0 | 0 | 23 | First hop completes; first arc lands on Boab Tree marker 23 ($X = 23$) |
| `7 {{key:+}}` | 0 | 0 | 0 | 30 | Final hop completes; second arc lands cleanly on milestone 30 ($X = 30$) |

Those two consecutive arcs trace $18 \to 23 \to 30$, confirming a total trail length of $30\text{ km}$.

At the end of the outback hike, the team cartographer measures the span between Escarpment Overlook (kilometer 63) and Riverbed Base Camp (kilometer 27) to see how far apart the two camps sit. On the Open Number Line, jump backward from 63 by splitting $-27$ into friendly mental hops ($-20$ to 43, $-3$ to 40, and $-4$ to 36), then verify on the stack by pressing `{{res:sc6_03_counting_place_value_seq_25:keys}}` to find a camp separation of **`{{res:sc6_03_counting_place_value_seq_25:value}}`** kilometers.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `63 {{key:ENTER}}` | 0 | 0 | 63 | 63 | Pin Escarpment marker 63 into Register $X$ and duplicate to Mezzanine $Y$ |
| `27 {{key:-}}` | 0 | 0 | 0 | 36 | Leap backward by 27 units; arc lands squarely on tick 36 ($X = 36$) |

Want to verify that starting at camp $36$ and hiking $+27\text{ km}$ brings you right back to marker $63$? Don't re-type `27`—just press `{{key:LASTX}} {{key:+}}` and watch `63` reappear on the ground floor!

### What Happens When You Hop Left Past Zero? (`{{key:LINE}}` & Zero-Pair Counters Preview)

What happens on the Open Number Line (`{{key:LINE}}`) if you start at **$+3$** and subtract **$5$** (`3 {{key:ENTER}} 5 {{key:-}}`)? Does the number line stop at a brick wall at $0$?

Not at all! The mark $0$ is simply the mirror line (like sea level at the beach or freezing point on a thermometer) between positive numbers to the right and negative numbers to the left:

{{blocks:diagram_submarine_elevation|Positive and Negative Numbers Above and Below 0 m Sea Level: Seabird Dive, Submarine Depth & Hot-Air Balloon Sandbags}}

- **Two-Stage Hop Past Zero on `{{key:LINE}}`:** Tap `{{key:LINE}}`, then key in `3 {{key:ENTER}} 5 {{key:-}}`. Watch the jump arc hop **3 steps left to reach $0$**, and then continue **2 more steps left of zero** to land on **`-2`**!
- **Andean Hummingbird Nighttime Torpor:** High in the Andes mountains, a hummingbird conserving energy in nighttime *torpor* watches the mountain air drop from $+3^\circ\text{C}$ at dusk by $5^\circ\text{C}$ overnight: $3 - 5 = \mathbf{-2^\circ\text{C}}$ ($2^\circ\text{C}$ below freezing).
- **Zero-Pair Flip Counters:** On your Ten-Frame tray, 1 gold/yellow counter ($+1$) and 1 coral/red counter ($-1$) form a **Zero Pair** ($+1 + (-1) = 0$) that cancels out to zero—a core concept you will master alongside the `{{key:+/-}}` key, balance equations, and the 4-Quadrant Coordinate Plane in **[Chapter 7: Prime Numbers, Fair Dice & Data Detective](07-data-probability-primes.md)**.

---

## The European Rekenrek / Number Rack (`{{key:COUNT}}`)

Our third visual lens is the **Number Rack (`{{key:COUNT}}`)**, modeled on the classic 20-bead *Rekenrek* invented by Adrian Treffers at the Freudenthal Institute in the Netherlands. Look at your physical Number Rack: it has two parallel stainless-steel rods, and each rod carries 10 sliding beads split into **5 Red** and **5 White** ($5 + 5 = 10$ on the top wire, and $5 + 5 = 10$ on the bottom wire, for 20 beads in all).

### The Five-and-Ten Anchor: How $8 + 6$ Becomes $(5 + 5) + (3 + 1) = 14$ at a Glance
Why did Adrian Treffers split every 10-bead wire into **5 Red** and **5 White** beads instead of painting all 10 beads the same color? Because human eyes can instantly spot up to 5 objects without counting one-by-one—and if 8 beads in a row were all the same color, your eyes would blur!

Watch how the 5-red / 5-white grouping turns $8 + 6$ into an instant visual snap on your physical Number Rack:
1. **Top Wire ($8$):** Slide **8 beads** to the left in a single push—all **5 Red beads** plus **3 White beads** ($5 + 3 = 8$).
2. **Bottom Wire ($6$):** Slide **6 beads** to the left—all **5 Red beads** plus **1 White bead** ($5 + 1 = 6$).
3. **Read the Colors Vertically:** Look at the left column of Red beads: **5 Red on top + 5 Red on the bottom = 10!** Now look at the White beads right next to them: **3 White + 1 White = 4.**

$$8 + 6 = (5 + 3) + (5 + 1) = (5 + 5) + (3 + 1) = 10 + 4 = 14$$

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `5 {{key:ENTER}} 5 {{key:+}}` | 0 | 0 | 0 | 10 | Combine the two 5-Red bead clusters into a full ten ($X = 10$) |
| `3 {{key:ENTER}} 1 {{key:+}}` | 0 | 0 | 10 | 4 | Combine the 3 White and 1 White beads ($X = 4$) while 10 waits in $Y$ |
| `{{key:+}}` | 0 | 0 | 0 | 14 | Unite the Red ten and White ones: $10 + 4 = 14$ |

### Seeing Teen Numbers Clearly on the Number Rack (`{{key:COUNT}}`)
Teen numbers ($11$ through $19$) play a sneaky trick in the English language. In languages like Chinese or Japanese, $14$ is spoken directly as *"ten-four"*, which tells you right away to write a `1` (one ten) followed by a `4` (four ones). In English, however, we say *"fourteen"*—hearing the word *"four"* first, which tempts many young learners to write $41$ instead of $14$!

Whenever you type `{{key:1}} {{key:4}}` and press `{{key:COUNT}}`, that confusion vanishes at a glance:
- **Top Wire (Wire 1):** Shows all **10 beads** (5 red, 5 white) slid to the active left side—that is the **`1` ten** in `14`.
- **Bottom Wire (Wire 2):** Shows **4 red beads** slid to the left—that is the **`4` ones** in `14`.
- And just like in Ten-Frame mode, tapping `{{key:.}}` slides beads across the wire one by one so you can watch numbers grow up to 20 on the dual-wire rack (and up to 100 in extended counting mode).

### The Coral Reef & Deep-Sea Research Station: Teen Numbers & Doubles on the Rack
Now board a research submarine bound for an underwater coral reef habitat! Here your crew pairs the two-rail **Rekenrek Number Rack (`{{key:COUNT}}`)** with the SC-6 stack, sliding 5-red and 5-white bead clusters across the top and bottom wires to spot teen numbers, doubles, and near-doubles in a single glance.

As your submarine descends past the reef wall, the sonar operator spots a pod of 17 spinner dolphins swimming past the observation window. How do you show 17 on the two-rail Number Rack in just two pushes—without counting 17 beads one by one? Slide all 10 beads on Rail 1 (5 red, 5 white) in one sweep to lock in one full ten, then slide 7 beads on Rail 2 (all 5 red plus 2 white). To build that exact $10 + 7$ structure on the stack, press `{{res:sc6_03_counting_place_value_seq_10:keys}}` so Ground Shelf $X$ shows **`{{res:sc6_03_counting_place_value_seq_10:value}}`**, and then tap `{{key:COUNT}}` to see 1 full wire of 10 on top and $5 + 2 = 7$ beads on the bottom wire ($X = 17$).

Once the submarine docks inside the underwater hangar, an engineer balances a mini-submersible's left and right thruster pods by bolting 6 battery cells onto the port side and 6 matching battery cells onto the starboard side. Why does the Number Rack make doubles like $6 + 6$ pop out immediately? Slide 6 beads on Rail 1 (5 red, 1 white) and 6 beads on Rail 2 (5 red, 1 white). Now look *vertically* at the red beads: the two 5-red clusters stack up to make a hidden **10**, and the two white beads make **2** ($10 + 2 = 12$)! Combine both battery pods on the stack by pressing `{{res:sc6_03_counting_place_value_seq_14:keys}}`, and the bottom shelf immediately displays **`{{res:sc6_03_counting_place_value_seq_14:value}}`** cells.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `6 {{key:ENTER}}` | 0 | 0 | 6 | 6 | Enter 6 port-side battery cells into $X$ and duplicate to Mezzanine $Y$ |
| `6 {{key:+}}` | 0 | 0 | 0 | 12 | Add double quantities; $6 + 6 = 12$ battery cells forms in Register $X$ |

Because `6 {{key:ENTER}}` already duplicated `6` into both $Y$ and $X$, you don't even have to type the second `6` in your own calculations—pressing `6 {{key:ENTER}} {{key:+}}` doubles any number on the spot!

Once you know your doubles (like $6 + 6 = 12$ and $7 + 7 = 14$), what happens when two numbers are right next door to each other, like $7 + 8$? On the reef's live video feed, night cameras monitor two sea-turtle nesting beaches: North Cove has 7 nests, and South Cove has 8 nests. Slide 7 beads on Rail 1 and 8 beads on Rail 2 of your Number Rack. You can clearly see a matching pair of sevens ($7 + 7 = 14$) plus **1 extra white bead** on the bottom rail! That is the **Doubles-Plus-One** strategy in action: keying in `{{res:sc6_03_counting_place_value_seq_15:keys}}` doubles the 7 nests to `14` and adds the 1 extra nest to reach **`{{res:sc6_03_counting_place_value_seq_15:value}}`**.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `7 {{key:ENTER}}` | 0 | 0 | 7 | 7 | Load North Cove's 7 turtle nests into $X$ and duplicate to Mezzanine $Y$ |
| `7 {{key:+}}` | 0 | 0 | 0 | 14 | Add the known double; $7 + 7 = 14$ nests forms in Register $X$ |
| `1 {{key:+}}` | 0 | 0 | 0 | 15 | Add the 1 extra nest; total reaches 15 turtle nests ($X = 15$) |

Any two neighbor numbers (like $6 + 7$, $7 + 8$, or $8 + 9$) are simply a double plus 1!

---

## Place Value Decomposition Studio (`{{key:PV}}`): Archimedes & The 10-for-1 Regrouping Exchange

In the third century BC, the Greek mathematician Archimedes wrote a daring treatise called *The Sand Reckoner*. At the time, people believed the grains of sand on the Sicilian coast were "infinite" because Greek numerals had no clean way to name giant numbers. Archimedes proved them wrong by inventing a system of bundling powers of ten—a breakthrough that Hindu-Arabic mathematicians perfected into the **10-for-1 Regrouping Exchange** we use today {{cite:ifrah2000}}.

When you look at a big number like $4,725$, it isn't just four separate digits sitting next to each other ("4", "7", "2", "5"). It is actually four distinct bundled packages working together:
$$4,725 = 4,000 + 700 + 20 + 5$$

To let you touch and test those bundles directly, your **Place Value Studio** pairs physical desktop trays with the calculator's **Place Value Engine (`{{key:PV}}`)**:
- **$4 \times 2$ Whole Numbers Activity Tray (`1000 | 100 | 10 | 1`):** A precision $77.8 \times 38.6\text{ mm}$ desktop mat with four recessed place-value columns labeled `THOUSANDS`, `HUNDREDS`, `TENS`, and `ONES` across two working rows (so you can set up two multi-digit numbers side-by-side just like Registers $Y$ and $X$).
- **$4 \times 2$ Decimal Numbers Activity Tray (`1 • 0.1 | 0.01 | 0.001`):** A matching desktop mat with a raised tactile decimal point (`•`) separating `ONES` from `TENTHS`, `HUNDREDTHS`, and `THOUSANDTHS`.
- **44 Place Value Digit Miniblocks (`0`–`9`) & 9 Stackable `+1` Regrouping Blocks ($19.0 \times 19.0 \times 7.0\text{ mm}$ visible $1\text{U}$ height):** Whenever a column accumulates ten `+1` unit miniblocks (reaching $10 \times 7.0\text{ mm} = 70.0\text{ mm}$, the exact height of the $70.0\text{ mm}$ 10-Rod in your Ten-Frame Studio), you trade all 10 unit blocks for a single `+1` regrouping block in the next column to the left (`ONES` $\to$ `TENS` $\to$ `HUNDREDS` $\to$ `THOUSANDS`).

{{blocks:place_value_regrouping|Place Value Studio Base-10 Decomposition and Regrouping}}
*Figure 3.3: The Place Value Studio. The $4 \times 2$ Whole and Decimal Place Value Trays, digit miniblocks (`0`–`9`), and stackable `+1` regrouping blocks make 10-for-1 place value physical, pairing directly with the SC-6 `{{key:PV}}` mode.*

### Peeking Inside Any Number with `{{key:PV}}`
Think of the `{{key:PV}}` key as an X-ray lens that lets you look inside a big number and ask: *"How many bundles are sitting in this exact column?"*
1. First, park your **Starting Number** on Waiting Shelf $Y$ (for example, `{{key:4}} {{key:7}} {{key:2}} {{key:5}} {{key:ENTER}}`).
2. Next, type the **Place Value Column** you want to inspect onto Ground Shelf $X$—type `1` for ones, `10` for tens, `100` for hundreds, or `1000` for thousands.
3. Press `{{key:PV}}`, and Ground Shelf $X$ immediately reveals the single digit sitting in that column!

For example, when you check the Tens place of $4,725$ by pressing `{{key:1}} {{key:0}} {{key:PV}}`, Register $X$ shows **`2`** (telling you there are 2 tens, or $20$, inside $4,725$):

| Keystroke | Display T | Display Z | Display Y (Target Number) | Display X (Query / Result) |
| :--- | :--- | :--- | :--- | :--- |
| `4725` | 0 | 0 | 0 | 4725 |
| `{{key:ENTER}}` | 0 | 0 | 4725 | 4725 |
| `10` | 0 | 0 | 4725 | 10 |
| `{{key:PV}}` | 0 | 0 | 4725 | 2 |

---

### Why `{{key:PV}}` Keeps Your Number Parked on Shelf $Y$
Look closely at the `Display Y` column in the table above: even after you pressed `{{key:PV}}`, **your starting number (`4725`) stayed parked on Shelf $Y$!** Even better, `{{key:PV}}` turns off automatic stack lift for your next entry so that typing another column size (`100`, `1000`, or `1`) simply replaces the query in $X$ while keeping `4725` right in $Y$.

That means you can X-ray every single column of $4,725$ in rapid-fire succession without ever re-typing `4725`. Right after checking the tens column, type `{{key:1}} {{key:0}} {{key:0}} {{key:PV}}` and Ground Shelf $X$ reveals $\mathbf{7}$ (telling you there are 7 hundreds, worth $700$). Next, type `{{key:1}} {{key:0}} {{key:0}} {{key:0}} {{key:PV}}` to see $X = \mathbf{4}$ (4 thousands, worth $4,000$), and finally type `{{key:1}} {{key:PV}}` to see $X = \mathbf{5}$ (5 ones, worth $5$).

### Building Numbers from Expanded Notation in the Navigation Archive
Just as `{{key:PV}}` pulls a number apart into its place-value columns, you can also build three-, four-, and five-digit numbers from the ground up by adding their expanded powers of ten ($100\text{s}, 10\text{s}, 1\text{s}$ and beyond). Step into the observatory's historical navigation archive with your physical **Place Value Studio Whole Numbers Tray** to see how!

Your first stop in the archive is a celestial globe showing Earth's solar orbit. How many days does Earth take to complete one full orbit around the Sun? Dock the digit miniblocks `3`, `6`, and `5` into the `HUNDREDS`, `TENS`, and `ONES` sockets of your **Place Value Studio Whole Numbers Tray**: `3` hundreds ($300$), `6` tens ($60$), and `5` ones ($5$). Now watch those three bundled packages snap together into one whole number on the stack: pressing `{{res:sc6_03_counting_place_value_seq_26:keys}}` fuses $300 + 60 + 5$ into **`{{res:sc6_03_counting_place_value_seq_26:value}}`** solar days.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `300 {{key:ENTER}}` | 0 | 0 | 300 | 300 | Enter `3` hundreds ($300$) into stack |
| `60 {{key:+}}` | 0 | 0 | 0 | 360 | Add `6` tens ($60$); subtotal accumulates to 360 |
| `5 {{key:+}}` | 0 | 0 | 0 | 365 | Add `5` ones ($5$); full expanded sum reaches 365 |

Each column contributes its exact place-value weight—$3$ hundreds, $6$ tens, and $5$ ones—to form $300 + 60 + 5 = 365$ days in a year.

Next to the celestial globe sits a brass star astrolabe used by early ocean navigators who steered by the stars long before GPS satellites. Dock the four digit miniblocks `1`, `4`, `9`, and `2` into the `THOUSANDS`, `HUNDREDS`, `TENS`, and `ONES` sockets of your **Whole Numbers Place Value Tray**, then reconstruct that four-digit exploration year on the stack by adding its four place-value columns ($1,000 + 400 + 90 + 2$): keying in `{{res:sc6_03_counting_place_value_seq_27:keys}}` stacks each power of ten in turn to display **`{{res:sc6_03_counting_place_value_seq_27:value}}`**. Watch how the open zeros act like empty seats waiting for each smaller bundle to slide into place: starting with `1000 {{key:ENTER}}` parks `1000` on Waiting Shelf $Y$, and tapping `400 {{key:+}}` slides the 4 hundreds into the hundreds seat so Ground Shelf $X$ updates to `1400`. Next, `90 {{key:+}}` lifts `1400` to Shelf $Y$ and drops the 9 tens into the tens seat to form `1490`, and finally `2 {{key:+}}` snaps the 2 ones into the rightmost seat to complete `1492`—showing step by step how $1$ thousand, $4$ hundreds, $9$ tens, and $2$ ones lock together without ever interfering with one another's columns.

What happens when a number grows past four digits? In the back of the observatory library, a vault archives a countdown-patterned collection of photographic glass star plates: 9 ten-thousands, 8 thousands, 7 hundreds, 6 tens, and 5 ones. Even though your desktop Place Value Tray has four physical sockets (`1000 | 100 | 10 | 1`), every new column to the left simply bundles 10 of the column before it! Build the five-digit archive total on the stack by pressing `{{res:sc6_03_counting_place_value_seq_29:keys}}`, which layers each place-value bundle from left to right to reach **`{{res:sc6_03_counting_place_value_seq_29:value}}`**.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `90000 {{key:ENTER}}` | 0 | 0 | 90000 | 90000 | Enter 9 ten-thousands tier into stack |
| `8000 {{key:+}}` | 0 | 0 | 0 | 98000 | Add 8 thousands tier ($X = 98000$) |
| `700 {{key:+}}` | 0 | 0 | 0 | 98700 | Add 7 hundreds column ($X = 98700$) |
| `60 {{key:+}}` | 0 | 0 | 0 | 98760 | Add 6 tens column ($X = 98760$) |
| `5 {{key:+}}` | 0 | 0 | 0 | 98765 | Add 5 ones column; completes 98,765 |

Each addition fills the next open zero column—uniting $9$ ten-thousands, $8$ thousands, $7$ hundreds, $6$ tens, and $5$ ones into $98,765$.

### Exploring Tenths and Hundredths with Place Value
In Grades 4–6, the exact same 10-for-1 pattern continues to the right of the raised tactile decimal point (`•`) on your **Decimal Place Value Tray (`1 • 0.1 | 0.01 | 0.001`)**. If you cut 1 whole into 10 equal strips, each strip is one **Tenth ($0.1$)**; if you cut 1 tenth into 10 tiny squares, each square is one **Hundredth ($0.01$)**. Suppose you park $345.67$ on Shelf $Y$: you can inspect its Tenths column ($0.1$) by typing `{{key:.}} {{key:1}} {{key:PV}}` to reveal $X = \mathbf{6}$ (6 tenths), and then inspect its Hundredths column ($0.01$) by typing `{{key:.}} {{key:0}} {{key:1}} {{key:PV}}` to reveal $X = \mathbf{7}$ (7 hundredths).

Your Decimal Place Value Tray also makes it obvious *why* you must line up the decimal points—not the rightmost digits—when adding or subtracting decimals like $14.6 + 3.85$:
- **Lining Up the Decimal Points on Paper:** Write $14.6$ above $3.85$ so their decimal points (`•`) sit in a straight vertical line, and add a placeholder zero on the end so $14.6$ becomes **$14.60$**. Now Tenths add to Tenths ($.60 + .80$) and Hundredths add to Hundredths ($.00 + .05$): $14.60 + 3.85 = \mathbf{18.45}$.
- **On Your Decimal Tray & SC-6 Stack:** Dock `14.60` in the top row of the Decimal Tray and `3.85` in the bottom row—the raised decimal point physically keeps the Tenths (`6` and `8`) and Hundredths (`0` and `5`) in matching columns! Verify on your SC-6 (`14.6 {{key:ENTER}} 3.85 {{key:+}}` $\to \mathbf{18.45}$, then `0.1 {{key:PV}}` $\to 4$ Tenths and `0.01 {{key:PV}}` $\to 5$ Hundredths).
- **Real Workshop Drawer Clearance:** Suppose you slide **4 modular Gridfinity storage bins** ($42.0\text{ mm}$ wide each) side-by-side into a workshop desk drawer whose inside width is **$170.5\text{ mm}$**. How many millimeters of sliding clearance remain? On your SC-6, subtract the width of the 4 bins from the inside width of the drawer (`170.5 {{key:ENTER}} 4 {{key:ENTER}} 42 {{key:×}} {{key:-}}`) to see **`2.5` mm** of smooth drawer clearance ($170.5 - 168.0 = 2.5\text{ mm}$).

---

## Big Numbers in Nature: Expanding Horizons

Once you master the 10-for-1 regrouping exchange with your blocks, `{{key:PV}}` acts like a mathematical X-ray machine that lets you look inside any giant number in nature—from prehistoric dinosaur eras to the icy rings of Saturn.

### The Earth-Moon Distance ($384,400\text{ km}$)
Look up at the night sky: the average distance from the Earth to the Moon is $384,400\text{ kilometers}$. To see how that colossal distance is built out of base-ten bundles, park $384,400$ on Waiting Shelf $Y$ by typing `{{key:3}} {{key:8}} {{key:4}} {{key:4}} {{key:0}} {{key:0}} {{key:ENTER}}`, and then X-ray each column from largest to smallest. Querying the hundred-thousands place with `{{key:1}} {{key:0}} {{key:0}} {{key:0}} {{key:0}} {{key:0}} {{key:PV}}` reveals $X = \mathbf{3}$ ($3$ hundred-thousands $= 300,000\text{ km}$); querying the ten-thousands place with `{{key:1}} {{key:0}} {{key:0}} {{key:0}} {{key:0}} {{key:PV}}` shows $X = \mathbf{8}$ ($8$ ten-thousands $= 80,000\text{ km}$); querying the thousands place with `{{key:1}} {{key:0}} {{key:0}} {{key:0}} {{key:PV}}` extracts $X = \mathbf{4}$ ($4$ thousands $= 4,000\text{ km}$); and querying the hundreds place with `{{key:1}} {{key:0}} {{key:0}} {{key:PV}}` finishes with $X = \mathbf{4}$ ($4$ hundreds $= 400\text{ km}$).

> **Lunar Transit Time:** If an Apollo spacecraft cruises toward the Moon at $4,000\text{ km/hour}$, how many hours does it take to complete the journey? By placing the lunar distance on Shelf $Y$ and dividing by the spacecraft's speed—pressing `{{res:sc6_03_counting_place_value_seq_01:keys}}`—Ground Shelf $X$ immediately displays **`{{res:sc6_03_counting_place_value_seq_01:value}}`** hours, which works out to about $4\text{ days}$ of continuous spaceflight.

### Human Heartbeats in a Year ($42,048,000$)
You don't even have to leave Earth to find numbers in the tens of millions—one is beating inside your chest right now! Your heart beats approximately $80\text{ times per minute}$ when you are resting. How many times does it beat in an entire year? With 60 minutes in an hour, your heart beats $80 \times 60 = 4,800\text{ times per hour}$; across 24 hours in a day, that climbs to $4,800 \times 24 = 115,200\text{ beats per day}$; and across all 365 days in a year, it reaches $115,200 \times 365 = \mathbf{42,048,000\text{ beats per year}}$!

Watch how cleanly you can chain that entire year of heartbeats on the SC-6 stack without writing down a single intermediate subtotal:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `80 {{key:ENTER}}` | 0 | 0 | 80 | 80 |
| `60 {{key:×}}` | 0 | 0 | 0 | 4800 |
| `24 {{key:×}}` | 0 | 0 | 0 | 115200 |
| `365 {{key:×}}` | 0 | 0 | 0 | 42048000 |

With $42,048,000$ sitting on Ground Shelf $X$, lift it onto Shelf $Y$ and X-ray the top two columns: typing `{{key:ENTER}} {{key:1}} {{key:0}} {{key:0}} {{key:0}} {{key:0}} {{key:0}} {{key:0}} {{key:0}} {{key:PV}}` reveals $X = \mathbf{4}$ ($4$ ten-millions, or $40,000,000$ beats), and typing `{{key:1}} {{key:0}} {{key:0}} {{key:0}} {{key:0}} {{key:0}} {{key:0}} {{key:PV}}` reveals $X = \mathbf{2}$ ($2$ millions, or $2,000,000$ beats).

### Distance to Mars ($225,000,000\text{ km}$) & The Age of *Tyrannosaurus rex* ($66,000,000\text{ Years}$)
Now let's step up to eight- and nine-digit numbers. At its average orbital distance, the red planet Mars is approximately $225,000,000\text{ kilometers}$ from Earth—and on Earth's geological timeline, the mighty *Tyrannosaurus rex* walked through Cretaceous fern forests $66,000,000\text{ years ago}$. When you X-ray Mars's distance on the Place Value Engine by pressing `225000000 {{key:ENTER}} 100000000 {{key:PV}}`, Ground Shelf $X$ shows $\mathbf{2}$ (hundred-millions), followed by `10000000 {{key:PV}}` $\longrightarrow X = \mathbf{2}$ (ten-millions) and `1000000 {{key:PV}}` $\longrightarrow X = \mathbf{5}$ (millions). Doing the same X-ray on the *T. rex* extinction boundary (`66000000 {{key:ENTER}} 10000000 {{key:PV}}`) reveals $X = \mathbf{6}$ ($6$ ten-million-year bundles), and `1000000 {{key:PV}}` reveals $X = \mathbf{6}$ ($6$ one-million-year bundles). And if a robotic spacecraft travels toward Mars at $25,000\text{ km/h}$, how many days will the voyage take? Divide the orbital distance by the hourly speed and then by $24$ hours per day—pressing `225000000 {{key:ENTER}} 25000 {{key:÷}} 24 {{key:÷}}`—to see Ground Shelf $X$ land on **`375` days**, or just over 1 full year in space!

### Saturn's Ring Orbit ($1,427,000,000\text{ km}$) & Stars in a Dwarf Galaxy ($2,500,000,000$)
Venturing even deeper into the solar system, the ringed planet Saturn orbits the Sun at an average distance of **1 billion, 427 million kilometers** ($1,427,000,000\text{ km}$), while a nearby dwarf galaxy cluster holds $2,500,000,000$ stars:
$$1,427,000,000 = 1,000,000,000 + 400,000,000 + 20,000,000 + 7,000,000$$

Using `{{key:PV}}`, you can X-ray Saturn's orbit from the Billions column down to the Millions column without re-typing the number once: `1427000000 {{key:ENTER}} 1000000000 {{key:PV}}` extracts $X = \mathbf{1}$ (1 billion km), `100000000 {{key:PV}}` extracts $X = \mathbf{4}$ (4 hundred-million km), `10000000 {{key:PV}}` extracts $X = \mathbf{2}$ (2 ten-million km), and `1000000 {{key:PV}}` extracts $X = \mathbf{7}$ (7 million km). In the exact same way, X-raying the dwarf galaxy (`2500000000 {{key:ENTER}} 1000000000 {{key:PV}}`) shows $X = \mathbf{2}$ (2 billions) and `100000000 {{key:PV}}` shows $X = \mathbf{5}$ (5 hundred-millions).

### Deep-Space Mission Control & Seven-Digit X-Rays
Now take a seat at the Deep-Space Mission Control console to see how `{{key:PV}}`, `{{key:LASTX}}`, and the four-level stack verify our lunar flight from the start of this section and scale up to seven-digit numbers across million-carton school totals and Voyager 1's daily race through interstellar space!

Start by pulling the $384,400\text{ km}$ Earth-Moon transit we X-rayed a moment ago up onto the main flight-director console. Remember how dividing $384,400\text{ km}$ by the Apollo spacecraft's $4,000\text{ km/h}$ cruising speed gave a lunar voyage of $96.1\text{ hours}$? At Mission Control, every flight calculation must be verified in reverse before launch: when you run that transit division on the stack by pressing `{{res:sc6_03_counting_place_value_seq_48:keys}}` to display **`{{res:sc6_03_counting_place_value_seq_48:value}}`** hours ($X = 96.1$), the spacecraft's $4,000\text{ km/h}$ speed is automatically saved inside `{{key:LASTX}}`. That means you can prove your transit time is $100\%$ accurate without re-typing a single digit—just tap `{{key:LASTX}} {{key:×}}` and watch $96.1\text{ hours} \times 4,000\text{ km/h}$ snap right back to the exact `384400` kilometer Earth-Moon distance on Ground Shelf $X$!

Before launching into interstellar space, mission nutritionists ask a down-to-earth question to help the crew picture seven-digit numbers: how big is **one million** in everyday life? Suppose 14 school districts each serve 450 cartons of milk per day across a 180-day school year. Do they cross the one-million-carton mark by summer vacation? To chain all three factors on the stack (`14 × 450 × 180`) without writing down intermediate subtotals, press `{{res:sc6_03_counting_place_value_seq_37:keys}}`, and Ground Shelf $X$ immediately climbs to **`{{res:sc6_03_counting_place_value_seq_37:value}}`** cartons.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `14 {{key:ENTER}}` | 0 | 0 | 14 | 14 | Enter number of school districts |
| `450 {{key:×}}` | 0 | 0 | 0 | 6300 | Daily consumption across all districts ($6,300\text{ cartons/day}$) |
| `180 {{key:×}}` | 0 | 0 | 0 | 1134000 | Scale by 180 school days: $1,134,000\text{ cartons/year}$ |

With $1,134,000$ on the screen, you can X-ray every column in place: keying `{{key:ENTER}} 1000000 {{key:PV}}` extracts $X = \mathbf{1}$ (1 million cartons); `100000 {{key:PV}}` extracts $X = \mathbf{1}$ (1 hundred-thousand cartons); `10000 {{key:PV}}` extracts $X = \mathbf{3}$ (3 ten-thousand cartons); and `1000 {{key:PV}}` extracts $X = \mathbf{4}$ (4 thousand cartons).

Now look out beyond the planets for your final telemetry check: NASA's Voyager 1 spacecraft hurtles through interstellar space at $17\text{ kilometers every second}$. How many kilometers does Voyager 1 travel in one full 24-hour day ($86,400\text{ seconds}$)? Multiply the seconds per day by Voyager's speed on the stack by pressing `{{res:sc6_03_counting_place_value_seq_38:keys}}`, and the bottom shelf immediately reveals **`{{res:sc6_03_counting_place_value_seq_38:value}}`** kilometers!

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `86400 {{key:ENTER}}` | 0 | 0 | 86400 | 86400 | Enter seconds per solar day into Register $Y$ |
| `17 {{key:×}}` | 0 | 0 | 0 | 1468800 | Daily distance covered: $1,468,800\text{ km/day}$ |

Voyager 1 covers $1,468,800\text{ kilometers}$—nearly $1.5\text{ million kilometers}$—every single day! You can then X-ray every column in place: keying `{{key:ENTER}} 1000000 {{key:PV}}` extracts $X = \mathbf{1}$ (1 million km); `100000 {{key:PV}}` extracts $X = \mathbf{4}$ (4 hundred-thousand km); `10000 {{key:PV}}` extracts $X = \mathbf{6}$ (6 ten-thousand km); `1000 {{key:PV}}` extracts $X = \mathbf{8}$ (8 thousand km); and `100 {{key:PV}}` extracts $X = \mathbf{8}$ (8 hundred km).

---

### Place Value & Counting Tips

- **Bridging Ten with Two Logs (`{{key:▦}}`):** Imagine two logs on a pond, each with room for 10 frogs. If Log 1 already has 9 green frogs and 6 brown frogs arrive, 1 brown frog hops onto Log 1 to fill it ($9 + 1 = 10$), and the remaining 5 hop onto Log 2 ($10 + 5 = 15$). Try it on your Ten-Frame screen (`{{res:sc6_03_counting_place_value_seq_42:keys}}`): Frame 1 shows 10 dots, Frame 2 shows 5 dots, and Register $X = 15$.
- **Why Zero Matters in 4,005 (`{{key:PV}}`):** When writing "four thousand five," leaving out the zeros gives $45$. Test both on the Place Value Engine: `45 {{key:ENTER}} 1000 {{key:PV}}` returns $X = 0$ (zero thousands), whereas `4005 {{key:ENTER}} 1000 {{key:PV}}` returns $X = 4$. The zeros hold the hundreds and tens columns open so the 4 stays in the thousands place. Because `{{key:PV}}` keeps your number parked in Register $Y$ and suppresses stack lift, you can check `10`, `100`, and `1000` one after another without re-entering the number.
- **Avoiding Teen Number Reversals (`14` vs. `41`):** Because we hear the word "four" first in "fourteen," it is tempting to write `4` first ($41$). Enter `14 {{key:COUNT}}` on the Number Rack: Wire 1 holds a full group of 10 beads and Wire 2 holds 4 loose beads. The `1` stands for that full ten, so it always leads on the left.
- **Why a Step Counter Stops Without `{{key:REP}}`:** In 4-stack mode, if you press `{{res:sc6_03_counting_place_value_seq_43:keys}}`, the screen shows `2`, but pressing `{{key:+}}` again leaves it at `2` because Register $Z$ held `0` ($2 + 0 = 2$). To fill all four floors ($T, Z, Y, X$) with your step size so it never runs out, press `1 {{key:REP}} {{key:+}} {{key:+}} {{key:+}}` and watch it climb: `2, 3, 4, 5, 6`.

---

### Common Stack Slips & How to Fix Them

If your screen shows something unexpected while counting or checking place value, use this quick table to spot what happened and fix it:

| What Happened on Your Screen | Why It Happened | How to Fix It |
| :--- | :--- | :--- |
| 1. In Ten-Frame mode, typing `{{key:▦}}` shows empty frame | Forgot to enter initial quantity. | Load the number FIRST, then press `{{key:▦}}`. |
| 2. Step counter in 4-stack adds `0` instead of constant | Stack dropped `0` from empty $Z$ to $Y$. | Switch to 2-Stack (`2-LV`) or use `{{key:REP}}`. |
| 3. Place Value `{{key:PV}}` query returns error | Entered query place before subject number. | Enter number, press `{{key:ENTER}}`, then query place value. |
| 4. Ten-frame step key `{{key:.}}` adds decimal point to number | Pressed digit key while typing digits. | Tap `{{key:.}}` alone to step the counter by 1. |
| 5. Child writes `41` for teen number fourteen | Auditory reversal of "four" in 14. | Use the Rekenrek screen to show 1 ten + 4 ones. |
| 6. Number line arc jumps backward on addition | Typed second number before starting number. | Enter start coordinate first, then `{{key:ENTER}}`, then jump. |
| 7. Big number heartbeats overwritten during multiply | Pressed `{{key:C}}` between multi-step factors. | Let the stack lift; do not press Clear between `{{key:×}}` steps. |
| 8. Querying tens place of `405` gives `0` | Confused digit with total magnitude. | Query `10` $\to$ shows `0`: explain that zero is a placeholder. |
| 9. Worried returning from sandbox to `{{key:NUM}}` lost data | Assumed mode switch clears the stack. | Press `{{key:NUM}}`: the operational stack is preserved. |
| 10. Querying hundredths shows `0` on $\$345.67$ | Used `100` instead of `.01` for decimal place value. | Use `.01` for hundredths ($1/100$); `100` queries hundreds. |

### Blind Digit Typing vs. Visible Place-Value Bundling

Now that you have explored all four visual sandboxes (`{{key:▦}}`, `{{key:COUNT}}`, `{{key:LINE}}`, and `{{key:PV}}`), compare how a standard single-line calculator handles counting, ten-bridging, and place-value inspection versus the SC-6's visual studios:

| Challenge / Real-World Task | The Algebraic Calculator Trap (Infix) | Algebraic Keystrokes & Clutter | The StackCalc + Blocks Method (RPN Stack + Visual Studio) | StackCalc Keystrokes | The Stack Advantage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Stadium Light Wattage:** Chained multi-bank load sum: $(30 \times 1500) + (10 \times 2000)$ | A basic four-function calculator evaluates strictly left-to-right ($30 \times 1500 + 10 = 45,010 \times 2000 = 90,020,000\text{ W}$!), while on a scientific infix screen, typing the full line hides both light-bank subtotals ($45,000$ and $20,000$) until you press `=`. Students wrap each product in defensive parentheses just to keep the two groups visually separate. | `( 3 0 × 1 5 0 0 ) + ( 1 0 × 2 0 0 0 ) =` (23 keystrokes with defensive brackets; intermediate subtotals hidden) | **RPN Parallel Accumulation:** Evaluates bank A ($45,000$) and bank B ($20,000$) into visible registers $Y$ and $X$, then combines them in a single keystroke with zero parentheses. | `30 {{key:ENTER}} 1500 {{key:×}} 10 {{key:ENTER}} 2000 {{key:×}} {{key:+}}` (16 keystrokes) | **Both Subtotals Visible:** Both power bank subtotals remain in plain sight on the stack before combining. |
| **Ten-Frame Bridging:** Mental addition across ten boundary: $8 + 5 = (8 + 2) + 3 = 10 + 3$ | Single-line algebraic screens hide the intermediate landmark of 10. Pressing equals triggers a black-box answer without showing the ten-frame filling up. | `8 + 2 + 3 =` (Single-line display; intermediate ten lost) | **Ten-Frame Studio Bridge (`{{key:▦}}`):** Interactive grid drops 2 counters into Frame 1, flashing the completed ten at 10, then cascades remaining 3 counters into Frame 2. | `8 {{key:ENTER}} 2 {{key:+}} 3 {{key:+}}` (Visual ten-frame flash at $X = 10$) | **Visual Ten Landmark:** Concrete spatial grouping eliminates finger-counting and reveals why bridging ten works. |
| **Place Value Explorer:** Extracting tens and hundreds from $4,725$ without scratch paper | Infix calculators have no positional extraction keys. Students must manually divide by 10, subtract the integer part, and multiply back—destroying the original number. | `4 7 2 5 / 1 0 =` $\to 472.5$, `- 4 7 0 =` $\to 2.5$ (Destructive multi-step division) | **Preserved Target Engine (`{{key:PV}}`):** Dedicated hardware instruction preserves target $4,725$ in Register $Y$, suppressing stack lift so subsequent checks execute instantly. | `4725 {{key:ENTER}} 10 {{key:PV}} 100 {{key:PV}} 1000 {{key:PV}}` (Chained single-stroke checks) | **Zero Value Destruction:** Target number remains permanently parked in Register $Y$; checks tens ($2$), hundreds ($7$), thousands ($4$) in rapid cadence. |
| **Rhythmic Cadence Counting:** Even number ladder up to 20 | Infix constant equals-key mode (`2 + 2 = = =`) relies on hidden register state that fails if any non-equals key is accidentally touched. | `2 + 2 = = = = =` (Flaky state; hidden accumulator easily cleared) | **Stack Constant Duplication:** In 2-LV mode, Register $Y$ preserves constant $2.0$. Each tap of `{{key:+}}` advances count by 2 with deterministic mechanical precision. | `2 {{key:ENTER}} 2 {{key:+}} {{key:+}} {{key:+}} ...` (100% reliable stack retention) | **Visual Stepping Ladder:** Learners see constant waiting on Level $Y$ while Level $X$ climbs in cadence with physical block towers. |

---

## Where to Go Next: Companion Workbook Quests & Kitchen-Table Challenges

> *For 24 additional worked problems with full 4-register stack tables, see Chapter 3 of the [SC-6 Elementary Companion Problem & Activity Workbook](../../curriculum/sc6-elementary-companion-workbook.md).*

Ready to put your Ten-Frame, Rekenrek, Number Line, and Place Value tools to the test? Pair this chapter with the **[Big Ideas Math Middle School Supplement](../../curriculum/big-ideas-middle-school-sc6-workbook.md) — Unit 2, Section 2.4 (Adding, Subtracting & Multiplying Decimals)** and **Unit 6, Section 6.1 (Positive & Negative Integers, Opposites & Zero Pairs)**, along with **Unit 3 of the 12-Unit Curriculum Guide** and the **StackCalc Student Workbook**—or try these three challenges right now:

1. **Hands-On Explorer (The Coin-Jar & Workshop Drawer Decimal Challenge):** First, grab a handful of dimes ($0.10$) and pennies ($0.01$), enter the total into Register $Y$, and extract the Tenths (`0.1 {{key:PV}}`) and Hundredths (`0.01 {{key:PV}}`) digits on your SC-6. Then test the **Gridfinity Workshop Drawer Clearance** (`170.5 {{key:ENTER}} 4 {{key:ENTER}} 42 {{key:×}} {{key:-}}` $\to \mathbf{2.5\text{ mm}}$).
2. **"Bet Your Family!" (The Secret Digit X-Ray & Sub-Zero Hop):** Ask a family member to type any secret 6-digit number onto your SC-6 and press `{{key:ENTER}}`, then cover the $Y$ register with a sticky note and type `0`. Reveal their secret number one digit at a time using `100000 {{key:PV}}` down to `1 {{key:PV}}`—and then switch to `{{key:LINE}}` (`3 {{key:ENTER}} 5 {{key:-}}` $\to \mathbf{-2^\circ\text{C}}$) to show how the Andean hummingbird's nighttime torpor hops left past zero.
3. **Rapid-Fire Sprint (The 30-Second Bridging Race):** Open the Ten-Frame Sandbox (`{{key:▦}}`) and see how many "9-plus" and "8-plus" teen bridging problems ($9 + 6$, $8 + 7$, $9 + 8$) you can decompose across 10 in 30 seconds before logging your score in your *Timed Proficiency Trials* passport.

---

## Chapter Summary & Looking Ahead

The tools and models in this chapter link physical counting directly to the base-10 number system:

1. **From Trays to Numbers:** Physical Ten-Frame trays and Rekenrek racks translate directly into the high-contrast vector sandboxes of the SC-6 (`{{key:▦}}`, `{{key:COUNT}}`).
2. **Spotting Groups at a Glance (Subitizing):** Anchors of 5 and 10 eliminate finger counting, allowing you to recognize quantities at a glance.
3. **Bridging Ten:** Decomposing additions across the decade ($8 + 5 = 8 + 2 + 3 = 10 + 3 = 13$) provides a reliable foundation for mental math.
4. **Step Counter Mechanics:** Constant step addition is verified through 2-stack register retention and 4-stack `{{key:REP}}` replication.
5. **Spatial Travel & `{{key:LASTX}}` Reversals:** The Open Number Line (`{{key:LINE}}`) visualizes arithmetic as forward and backward jump arcs that you can reverse in one tap with `{{key:LASTX}}`.
6. **Structural Decomposition:** The Place Value Engine (`{{key:PV}}`) slices numbers into their constituent powers of ten, preserving Register $Y$ across chained queries.
7. **Cosmic Horizons:** Place value structures scale directly from single unit cubes to solar system distances.

Once you can bundle single units into tens, hundreds, and thousands, what happens when we arrange equal groups into rectangular arrays? In **[Chapter 4: Tile Arrays, Skip-Counting & Remainders](04-operations-skip-counting.md)**, young Carl Friedrich Gauss shows us how multiplication and skip-counting reveal patterns across the universe.
