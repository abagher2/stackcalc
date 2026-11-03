---
title: "From Blocks to the Stack: How Hands-On Blocks Make Numbers Click (SC-6)"
description: "An illustrated popular math guide and hands-on companion for Grades 3–6 (ages 8–12), connecting 3D-printed math blocks with parenthesis-free thinking on the StackCalc SC-6."
---

# Preface: Welcome to Your Hands-On Math Studio

## Welcome, Explorer!

Open the lid of a LEGO set, dump a handful of colorful gears onto your desk, or lay out fresh ingredients on a kitchen counter, and your hands know right away what to do: you group matching pieces together, build one small section at a time, and see your creation take shape right in front of your eyes. What if mathematics worked the exact same way—not as a silent page of mystery rules, but as a hands-on workshop where you can touch, stack, and see every number you build?

**Welcome to your Desktop Math Studio.** Beside this book sit two partners designed to work together in your hands: a set of **3D-printed math blocks** that let you feel how numbers fit together on your desk, and the **StackCalc SC-6**, a calculator whose sunlit screen holds your numbers on **four visible shelves** just like trays on a workbench. When you can hold math in your left hand with real blocks and watch your numbers ride up and down four sturdy shelves under your right hand, math becomes an adventure you can see and touch.

Before you press a single button, think about how you build things with your hands in everyday life. Suppose you have **7 red LEGO bricks** on your desk, and your friend hands you **5 gold bricks**. How do you find out how many bricks you have altogether?

1. You place the **first pile (`7`)** on your desk.
2. You place the **second pile (`5`)** right beside it.
3. You **push the two piles together** into **`12`**.

Every time you stack pancakes on a plate, pack books into your backpack, or build a tower out of blocks, your hands follow that exact rhythm: **first put the pieces on the table, then do something with them.**

In mathematics and computer science, that everyday workspace has a special name: **a Stack**.

### Meet the Four Shelves of Your Number Stack ($X, Y, Z, T$)

When you work with numbers that have two or three parts—like measuring boards for a treehouse, sharing snacks among friends, or adding up three pairs of walls on a wooden treasure chest—your eyes want to see both numbers at the same time {{cite:strogatz2012}}. Keeping your numbers visible on a workbench lets your brain focus on the story instead of trying to juggle hidden numbers in your head.

Now look at the bottom-right corner of your **StackCalc SC-6**. Instead of an equals key, there is a wide button labeled **`{{key:ENTER}}`**, and the screen above it acts like a **stack of four sturdy shelves** where your numbers stay in plain sight while you work:

- **Shelf $X$ (Your Ground Shelf & Workbench):** This is the bottom shelf, shown in large bold digits along the lower edge of the screen. Every number you type appears right here on Shelf $X$, and every finished answer lands here too.
- **Shelf $Y$ (Your Waiting Shelf):** This shelf sits stacked right above Ground Shelf $X$. Whenever you finish typing your first number and press **`{{key:ENTER}}`**, an invisible elevator lifts that number up onto Shelf $Y$ so the bottom shelf is clear for your next number.
- **Shelf $Z$ and Top Shelf $T$ (Your Upper Shelves):** Above Shelf $Y$ sit two more waiting shelves. Whenever a math puzzle has two or three separate parts, finished pieces ride safely upstairs to Shelf $Z$ and Top Shelf $T$ until you need them, then drop right back down when it is time to combine them.

{{blocks:sc6_elementary_hero|The StackCalc SC-6 Calculator and Four-Shelf Number Stack}}

### Your Very First Stack Move: Adding `7` and `5`

Pick up your SC-6 (or place seven and five counting tiles on your desk) and try your very first stack calculation:
1. **Put the first number on Ground Shelf $X$:** Tap `7`. You see `7` sitting on Shelf $X$.
2. **Lift it to Waiting Shelf $Y$:** Tap **`{{key:ENTER}}`**. That tells the calculator, *"My first number is finished—lift it up to Shelf $Y$ so I can type the next number."*
3. **Put the second number on Shelf $X$:** Tap `5`. Now look at your screen: `7` is waiting on Shelf $Y$, and `5` is sitting on Shelf $X$. Both numbers are right in front of your eyes at the same time.
4. **Combine them:** Tap **`{{key:+}}`**. Instantly, Shelf $Y$ drops down and fuses with Shelf $X$ to make **`12`**.

Mathematicians and engineers call this step-by-step workspace **Reverse Polish Notation (RPN)**—or as we call it throughout this book, **Stack Math**—because you build one small piece at a time and watch every step unfold in plain view. In Chapter 2, you will discover how engineers first built this four-shelf stack into a pocket calculator for astronauts and scientists so no one would ever lose their place halfway through a problem.

---

## Taking the Stack for a Test Drive

Once you know how to send your first number up to Shelf $Y$ with `{{key:ENTER}}` and place a second number on Shelf $X$, you can already solve real-world stories. Let's walk through a few everyday adventures together to see what you will build and discover in the chapters ahead.

Throughout this book, whenever we introduce a new stack move, you will see a **4-Register Stack Table** like the one below. Think of each row in the table as a snapshot of your calculator's four shelves (**Top Shelf $T$**, **Shelf $Z$**, **Shelf $Y$**, and **Ground Shelf $X$**, shown as `Register T` through `Register X` in the column headers) right after your finger presses a key, so you can follow every step at your own pace.

### Taking Away: Finding Missing Spaces on a Ten-Frame Tray

Picture placing **7 red counters** into your 10-space Ten-Frame tray, filling the top row of 5 and 2 more spaces on the bottom row. How many blue counters do you need to fill all 10 spaces?

When you look at the Ten-Frame tray on your desk, your eyes don't even have to count the 7 red counters one by one: the raised center divider ridge shows a full top row of 5 plus 2 on the bottom, leaving 3 empty pockets waiting at the end of the tray.

In any subtraction story ($10 - 7$), we start with the whole amount (`10`) and take away the part we already have (`7`). On the stack, your starting number always goes onto Waiting Shelf $Y$ first via `10 {{key:ENTER}}`, the number you are taking away (`7`) goes onto Ground Shelf $X$, and tapping `{{key:-}}` takes Shelf $X$ away from Shelf $Y$ to leave **`3`** empty spaces:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---:|:---:|:---:|:---:|:---|
| `{{key:C}}` | 0 | 0 | 0 | 0 | Start with a clean stack of four empty shelves in `{{key:NUM}}` mode. |
| `10` | 0 | 0 | 0 | 10 | Put the 10 total spaces of the tray onto Workbench Shelf $X$. |
| `{{key:ENTER}}` | 0 | 0 | 10 | 10 | Lift 10 up onto Shelf $Y$ so your Workbench is ready. |
| `7` | 0 | 0 | 10 | 7 | Put the 7 red counters you already have onto Workbench Shelf $X$. |
| `{{key:-}}` | 0 | 0 | 0 | 3 | Take 7 away from 10 ($10 - 7 = 3$), leaving 3 empty spaces on Shelf $X$. |

*What if your screen says `17` instead of `3`?* That just means your thumb tapped `{{key:+}}` instead of `{{key:-}}`. And what if you accidentally typed `7 {{key:ENTER}} 10` in the wrong order? You don't have to erase and start over: tapping the **`{{key:x⇄y}}` (Swap)** key trades the numbers on Shelf $Y$ and Shelf $X$ so `10` is back on Shelf $Y$ and `7` is on Shelf $X$.

### Checking Your Own Work in One Tap

Every builder and explorer loves to know for sure that a measurement is right. On the SC-6, every time an operation combines two numbers, the calculator automatically tucks a backup copy of the number from Shelf $X$ into a special memory pocket called **`LAST x`** (`{{key:LASTX}}`).

Say you are counting trading cards at your desk: you have **24 cards** neatly sorted in your binder and **15 cards** stacked in a tin box. You add `24 {{key:ENTER}} 15 {{key:+}}` to get **`39`** cards in all. How can you prove that `39` is right in two quick clicks?

Just tap **`{{key:LASTX}}`**. Right away, your `15` jumps out of its memory pocket back onto Shelf $X$, while your `39` sum automatically lifts up to Shelf $Y$ to make room. Now tap **`{{key:-}}`**, and `39 - 15` lands right back on your starting number, **`24`**, proving your addition was spot-on!

Throughout Chapters 2, 3, and 4, you will use this two-tap detective check across every operation. After adding two beach-bucket collections of seashells ($38 + 25$) via `38 {{key:ENTER}} 25 {{key:+}}` $\implies \mathbf{63}$, tapping `{{key:LASTX}} {{key:-}}` checks $63 - 25 = \mathbf{38}$ in two clicks; after multiplying a rectangular array of tiles or dividing supplies among friends, tapping `{{key:LASTX}}` followed by the opposite operation restores your starting pile right on Shelf $X$. Even better, if your thumb ever taps `{{key:+}}` when you meant to tap `{{key:-}}`, `{{key:LASTX}}` acts as an instant undo button so you can recover in seconds—and as you are about to see, it can even help you verify division problems that leave extra items behind.

### Sharing with Whole Groups and Leftovers

What happens when numbers don't divide evenly? Imagine you have **26 favorite comic books** on your desk and you are sliding them into protective display sleeves that hold **4 comics each**. If a screen only showed a decimal like `6.5`, what would `0.5` of a sleeve mean? In real life, you fill **6 whole sleeves** ($6 \times 4 = 24$ comics), and you have **2 loose comics left over** on your desk.

On your SC-6, the **`{{key:÷R}}` (Quotient & Remainder)** key solves both parts of a sharing story at the exact same time because your screen has two visible shelves waiting to catch both whole numbers. Imagine a summer camp group of **94 campers and counselors** strapping on life jackets for a whitewater river trip in inflatable rafts that hold **8 paddlers each**. How many rafts will be completely full, and how many campers still need a seat?

When you put `94` on Shelf $Y$ (`94 {{key:ENTER}}`), put `8` on Shelf $X$, and tap **`{{key:÷R}}`**, the calculator splits the division cleanly across your two shelves:
- **Ground Shelf $X$** immediately shows **`11`** completely full rafts ($11 \times 8 = 88$ paddlers).
- **Waiting Shelf $Y$** holds the **`6`** leftover campers who still need a seat on the river!

Because you can see both the **`11` full rafts** and the **`6` remaining campers** side by side on your screen, you immediately spot the real-world answer: the camp cannot leave 6 kids standing on the riverbank, so the guides need to launch $11 + 1 = \mathbf{12\text{ rafts}}$ in all! And when you reach Chapter 4, you will discover a three-tap proof (`{{key:LASTX}} {{key:×}} {{key:+}}`) that multiplies the 11 full rafts by 8 and adds the 6 leftover campers right back to `94`.

---

### Building Two-Step Projects on the Stack

Now that you have seen how Shelf $X$ and Shelf $Y$ work together on one-step stories, what happens when a real-world project has **two or three steps**?

Imagine you are helping design a square brick patio or a wooden skateboard launch pad in a backyard that is **$12\text{ feet}$ wide**, leaving a **$3\text{-foot}$ grass path** along one edge so people can walk by. First, you take away the grass path ($12 - 3 = 9\text{ feet}$) to find the side length of your square patio. Next, you want to know two different things about that $9\text{-foot}$ square:
1. How many **square feet of bricks** it takes to fill the inside of the patio ($9 \times 9 = 81\text{ sq ft}$).
2. How many **feet of wooden border edging** it takes to frame all 4 outside edges ($9 \times 4 = 36\text{ ft}$).

Watch how naturally that whole design unfolds on your SC-6 workbench:
1. **Find the side length ($12 - 3$):** Tap `12 {{key:ENTER}} 3 {{key:-}}` to put **`9`** feet on Shelf $X$.
2. **Find the brick area ($9^2$):** Tap the **`{{key:x²}}` (Square)** key to multiply $9 \times 9 = \mathbf{81\text{ sq ft}}$ of bricks right on Shelf $X$. Because `{{key:x²}}` just used your `9`, it automatically tucks a copy of `9` into your `LAST x` pocket!
3. **Bring back the side length for the border ($9 \times 4$):** Tap **`{{key:LASTX}}`** to bring the $9\text{-foot}$ side length right back onto Shelf $X$ (which automatically lifts your `81` square feet up onto Waiting Shelf $Y$!).
4. **Finish both measurements side by side:** Type `4` and tap **`{{key:×}}`**. Now look at your screen: **`36` feet** of wooden border sits on Shelf $X$, right beside **`81` square feet** of bricks waiting on Shelf $Y$!

Notice something magical that happened in Step 4 when `9` was sitting on Shelf $X$: you didn't have to press `{{key:ENTER}}` before typing `4`! Why? Because **whenever a finished answer is sitting on Shelf $X$, typing a new number automatically lifts that finished answer up to the next shelf** to wait for you.

That **automatic stack lift** lets you build multi-part projects one small group at a time, just like snapping two LEGO sub-assemblies together on your desk. Picture your neighborhood maker club weaving a rope suspension bridge for a backyard treehouse: you combine **18 long oak slats and 6 cedar slats** ($18 + 6 = 24$ slats per bundle), you prepare **15 bundles minus 7 spare bundles** kept in the shed ($15 - 7 = 8$ active bundles), and you divide all those slats equally across **8 bridge sections**:
$$((18 + 6) \times (15 - 7)) \div 8$$

Watch how **Shelf $Z$** holds your first finished group upstairs while you build the second group on the bottom shelves:
1. **Build the first group (`18 + 6`):** Tap `18` `{{key:ENTER}}` `6` `{{key:+}}`. The screen immediately shows **`24`** slats on Shelf $X$.
2. **Build the second group (`15 - 7`):** Right away, type `15` `{{key:ENTER}}` `7` `{{key:-}}`. The moment you touch `15`, automatic stack lift carries your finished `24` upstairs to wait safely on **Shelf $Z$**, and when `{{key:-}}` combines `15` and `7` into **`8`** on Shelf $X$, your waiting `24` drops right back down to **Shelf $Y$** beside it!
3. **Multiply the two groups and divide by `8`:** Now `24` is waiting on Shelf $Y$ and `8` is sitting on Shelf $X$. Tap **`{{key:×}}`** to multiply them into **`192`**, and then tap `8` **`{{key:÷}}`** to divide by 8:
   `{{res:sc6_index_influencer_race:keys}}` $\longrightarrow$ **`{{res:sc6_index_influencer_race:value}}`**.

In Chapter 2, you will see how **Shelf $Z$** and **Top Shelf $T$** unlock the full four-story elevator so you can solve multi-group stories from the inside out (`{{res:sc6_order_of_ops:keys}}` $\longrightarrow$ **`{{res:sc6_order_of_ops:value}}`**) while watching every intermediate piece wait safely on its shelf.

---

### Four Helper Keys & Your Visual Screen Modes

As you travel through the chapters ahead, you will meet several more helper keys that turn tricky math topics into hands-on discoveries:

| Signature Key | How It Helps You |
| :--- | :--- |
| **Constant Repeat (`{{key:REP}}`)** | **Skip-Counting & Times Tables:** Copies your number across all four shelves ($X = 7, Y = 7, Z = 7, T = 7$) so repeated taps of `{{key:+}}` climb times tables (`7, 14, 21, 28...`) or repeated taps of `{{key:×}}` double `2` twenty times past **one million (`1,048,576`)**! |
| **Quotient & Remainder (`{{key:÷R}}`)** | **Whole Groups & Leftovers Together:** Divides in one tap, putting the whole groups (Quotient) on Shelf $X$ and the exact leftovers (Remainder) on Shelf $Y$. |
| **One-Tap GCF Simplify (`{{key:SIMP}}`)** | **Fraction Reduction You Control:** Keeps fractions like `0 {{key:.}} 12 {{key:.}} 18` unreduced until *you* press `{{key:SIMP}}` to divide top and bottom by their Greatest Common Factor in one tap into `2/3`, displaying `LOWEST TERMS` when already simplified. |
| **Add to Total (`{{key:Σ+}}`)** | **A Shopping Basket for Totals:** Lets you toss finished numbers into a running basket (`1`, `2`, `3` items) and tap `{{key:Σx}}` to see the grand total in one click. |

Look at how handy that **`{{key:Σ+}}` (Add to Total)** basket is whenever a project has several separate pieces to add up. Imagine painting three plywood walls for a backyard treehouse: a **North Wall** measuring $4\text{ ft} \times 3\text{ ft}$ ($12\text{ sq ft}$), an **East Wall** measuring $5\text{ ft} \times 3\text{ ft}$ ($15\text{ sq ft}$), and a **South Wall** measuring $6\text{ ft} \times 3\text{ ft}$ ($18\text{ sq ft}$). Instead of writing those three wall sizes down on scrap paper, you simply empty your calculator's running-total basket with **`{{key:CLΣ}}`** and toss each finished wall straight in. First, multiply the North Wall (`4 {{key:ENTER}} 3 {{key:×}}`) and tap **`{{key:Σ+}}`**—Shelf $X$ displays **`1`** to confirm *"1 wall is safely inside the basket."* Next, multiply and add the East Wall (`5 {{key:ENTER}} 3 {{key:×}} {{key:Σ+}}` $\to$ **`2`** walls) and the South Wall (`6 {{key:ENTER}} 3 {{key:×}} {{key:Σ+}}` $\to$ **`3`** walls). Finally, one tap of **`{{key:Σx}}`** adds the entire basket together to reveal **`45.0` $\text{sq ft}$** of total wall area—and tapping **`{{key:x̄}}`** divides that $45\text{ sq ft}$ total equally across all $3$ walls to show an average wall size of **`15.0` $\text{sq ft}$**!

### How Your Blocks, Screen Modes, and Stack Team Up

Just like cutaway drawings that peel back the cover of a machine so you can see every gear working inside {{cite:macaulay2016}}, math clicks fastest when you build with **hands-on objects** first, see **visual pictures** second, and combine **numbers** third. Every chapter in this book connects those three layers right at your desk:

| Learning Phase | What You Use | How It Works at Your Desk |
|---|---|---|
| **1. Hands-On Blocks** | 3D-Printed Math Block Kits | You build the problem with physical Ten-Frame Trays, $84\text{ mm}$ Fraction Towers, Four-Color Counting Tiles, Prime Factor Blocks, and a Planetary Geared Clock. |
| **2. Visual Screen Modes** | Daylight Paper-Like Visual Modes | You see the exact same model drawn on the SC-6 screen using Ten-Frame Mode `{{key:▦}}`, the Number Rack `{{key:COUNT}}`, Number Line Jump Arcs `{{key:LINE}}`, Place Value `{{key:PV}}`, the Geared Clock Dial `{{key:🕒}}`, Polyhedral Dice `{{key:🎲}}`, or the 6-Level Math Quiz Game `{{key:?}}`. |
| **3. The Number Stack** | Four-Shelf RPN Stack ($X, Y, Z, T$) | You combine your numbers on the four visible stack shelves—solving multi-step puzzles, remainder division, and 3D surface area step by step. |

Switching between any visual picture mode (`{{key:▦}}`, `{{key:COUNT}}`, `{{key:LINE}}`, `{{key:🕒}}`, `{{key:🎲}}`) and regular numbers (`{{key:NUM}}` or `{{key:C}}`) never erases your stack—it simply changes the lens through which you view the numbers on your shelves. As you begin exploring, three simple buttons do 90% of the work: **`{{key:ENTER}}`** locks your number in and lifts it up to Shelf $Y$, **`{{key:C}}`** clears Shelf $X$ back to `0`, and **`{{key:x⇄y}}`** swaps Shelf $Y$ and Shelf $X$ in one tap if you ever type two numbers in reverse order for subtraction or division!

### Why Master Builders Always Use a Workbench

Walk into a violin maker's workshop, a neighborhood bakery at dawn, or a robotics garage where students are bolting aluminum frames together, and you will notice one shared habit: great builders never try to hold twenty measurements in their heads at once. A carpenter planes one cedar board on the lower bench, sets it safely on the upper rack, planes the matching board below, and checks their fit side by side before gluing them together.

Long before electronic calculators existed, merchants and architects across Europe, Asia, and the Americas worked the exact same way on carved wooden **counting tables** and **bead frames**. Each horizontal line carved into a merchant's wooden table acted as a visible shelf where bronze or ivory counters waited in plain sight while the next part of a trade was counted out below.

As you flip through the chapters ahead, you will use your blocks and four-shelf workbench to crack real-world mysteries that surprise even adults. In **Chapter 4**, you will test **The Unfoldable Paper Bet**—discovering why it is physically impossible to fold an ordinary sheet of notebook paper in half 10 times with your bare hands, and how locking `2` into your stack with `{{key:REP}}` proves that 20 folds would tower higher than the Empire State Building. In **Chapter 6**, you will uncover **The $-40^\circ\text{C}$ Penguin Huddle Secret**, seeing how Emperor penguins in Antarctica use the geometry difference between *outside wall area* and *inside volume* to stay warm in howling blizzards—and why that exact same rule makes French fries crispy on the outside and fluffy on the inside. And in **Chapter 8**, you will master **Beating a Smartphone in Two Seconds Flat**, multiplying $65 \times 65$ or $43 \times 47$ out loud in your head faster than an adult can even unlock their phone and open the calculator app!

Whether you love building LEGO machines, baking in the kitchen, sketching 3D shapes, or racing the 4-second clock in Quiz Mode (`{{key:?}}`), every page ahead gives your hands something real to build and test.

---

## How Every Chapter Builds Your Skills

This book is organized into nine hands-on chapters and four reference appendices, and you don't have to read it like a school textbook where every page must be finished in strict order. If you are just unboxing your SC-6 for the first time, start with **Chapters 01 and 02** to set up your desk trays, test the snap-action keys, and learn the smooth rhythm of `{{key:ENTER}}`, `{{key:x⇄y}}`, and the four stack shelves.

If you are curious about a specific math puzzle today—whether it's why cicadas emerge every 17 years, how bakers scale sourdough recipes, or how deep-sea submersibles dive below sea level—you can jump straight to that chapter in the guide below, because every chapter pairs a 3D-printed block studio with matching visual screen modes and real-world stories. And whenever you are 3D-printing blocks, teaching a class, or looking up a button, flip to the **Appendices** at the back of the book for 3D-printing blueprints ([Appendix A](appendix-a-manipulative-blueprints.md)), 25 classroom station guides ([Appendix B](appendix-b-teacher-lesson-plans.md)), plain-English geometry and data formulas ([Appendix C](appendix-c-formulas-and-conversions.md)), and the complete 43-button directory ([Appendix D](appendix-d-keycap-directory.md)):

| Chapter / Appendix | What You Will Discover | 3D-Printed Math Block Studio | Primary SC-6 Keycaps | Hands-On Explorations |
| :--- | :--- | :--- | :--- | :--- |
| **[Chapter 01](01-hardware-architecture.md)** | Setting up your desk studio, first block-and-stack discoveries, daylight screen & button feel | All 8 Companion Studios & Quest Scoreboard | `{{key:ENTER}}`, `{{key:+}}`, `{{key:×}}`, `{{key:C}}`, `{{key:<-}}`, `{{key:f}}`, `{{key:g}}` | Measuring screen pixels, snap-domes, Gridfinity trays & battery life |
| **[Chapter 02](02-rpn-for-young-learners.md)** | Riding the 4-shelf RPN stack ($X, Y, Z, T$) & solving multi-step order of operations step by step | Stack Shelves & Counting Tiles | `{{key:ENTER}}`, `{{key:+}}`, `{{key:-}}`, `{{key:x⇄y}}`, `{{key:R↓}}`, `{{key:CSTK}}` | Weighing a dog on a bathroom scale, cell division, smoothie pitchers & backyard patios |
| **[Chapter 03](03-counting-place-value.md)** | Spotting groups at a glance, make-ten bridging, multi-digit place value (`1000 \| 100 \| 10 \| 1`), rounding & negative number-line hops | Ten-Frame Studio, Number Rack & Place Value Trays | `{{key:▦}}`, `{{key:COUNT}}`, `{{key:LINE}}`, `{{key:PV}}`, `{{key:$}}` | Fireflies & ten-pin bowling, Jupiter's moons, red kangaroo leaps & Voyager 1 |
| **[Chapter 04](04-operations-skip-counting.md)** | Rectangular multiplication arrays, rhythmic skip-counting ladders, powers & fair-share division with remainders | 24-Tile Counting & Array Studio | `{{key:×}}`, `{{key:÷}}`, `{{key:REP}}`, `{{key:÷R}}`, `{{key:MOD}}`, `{{key:LASTX}}` | Spacecraft solar panels, the chessboard wheat legend, farm egg cartons & garage skateboards |
| **[Chapter 05](05-fractions-decimals-ratios.md)** | Equivalent fractions, one-tap GCF reduction, common denominators, mixed numbers, decimals, percents & ratios | 84 mm Fraction Tower Studio & Decimal Tray | `{{key:a ᵇ/c}}`, `{{key:d/c}}`, `{{key:SIMP}}`, `{{key:FDISP}}`, `{{key:%}}`, `{{key:%CHG}}` | Musical guitar strings, bicycle sprockets, woodworking boards & the 1-2-3 concrete rule |
| **[Chapter 06](06-geometry-surface-area.md)** | 2D area/perimeter, Pythagorean theorem, 3D prism/cylinder/cone volume, surface area via `{{key:Σ+}}` & modulo-60 clock time | Counting Tiles, L-Frame, Volvelle & Geared Clock | `{{key:RECT}}`, `{{key:CIRC}}`, `{{key:PRISM}}`, `{{key:Σ+}}`, `{{key:🕒}}`, `{{key:▸HR}}` | Penguin huddles, Antarctic Scott tents, gift-box wrapping & Palomar dome |
| **[Chapter 07](07-data-probability-primes.md)** | Prime factor trees, GCF & LCM, polyhedral dice probability, dot plots, mean/median/IQR/MAD & signed integers | Prime Factor Studio, Polyhedral Dice & Two-Color Counters | `{{key:PRIME}}`, `{{key:FACT}}`, `{{key:GCF}}`, `{{key:LCM}}`, `{{key:🎲}}`, `{{key:x̄}}`, `{{key:MED}}`, `{{key:+/-}}` | 17-year cicadas, RSA secret codes, dice trials & submersible Alvin |
| **[Chapter 08](08-math-quiz-engine.md)** | Left-to-right mental math tricks (matching tens, 11s split, staircase sums) & 6-level 4-second speedruns | Math Dominoes & Quest Scoreboard | `{{key:?}}` (`{{key:f}}` + `{{key:C}}`), `{{key:≠}}`, `{{key:LASTX}}` | Mental-math speed shortcuts & 6-level 4-second speedrun sprints |
| **[Chapter 09](09-applied-stem-labs.md)** | 3D-printed block weights and layer slicing, bean sprout growth, recipe scaling, gear ratios, and solar ovens | All Studios + Calipers, Scale & Stopwatches | `{{key:π}}`, `{{key:x²}}`, `{{key:√x}}`, `{{key:▸g}}`, `{{key:▸cm}}`, `{{key:▸°C}}` | 3D printer slicing, pendulum clocks, botanical growth & maker workshops |
| **[Appendices A–D](appendix-a-manipulative-blueprints.md)** | CAD/3D-print blueprints ([App. A](appendix-a-manipulative-blueprints.md)), 25 station lesson plans ([App. B](appendix-b-teacher-lesson-plans.md)), formulas & primes ([App. C](appendix-c-formulas-and-conversions.md)), and 43-key matrix ([App. D](appendix-d-keycap-directory.md)) | Full 3D-Printed Math Block & Reference Suite | Complete 43-Key Hardware Matrix | Turnkey Classroom & Home Reference |

---

## Safety, Regulatory, Trademark & Parent/Educator Notices

> **CHOKING HAZARD — SMALL PARTS (16 CFR § 1501 / ASTM F963):**  
> The physical StackCalc 3D-printed math block kits (Counting & Array Tiles, Ten-Frame Flip Counters, Fraction Studio 1/12 Blocks, Prime Factor Studio Blocks, Math Dominoes, and Polyhedral Dice) contain small modular parts ($7.0\,\text{mm}$ minimum thickness). **Not for children under 3 years of age.** Use only under adult or educator supervision.
> - **3D-Printed Part Inspection:** When printing math block kits on classroom or home Fused Deposition Modeling (FDM) 3D printers, adults must use non-toxic PLA or PETG filament and inspect every finished piece prior to student handling—removing any loose filament strings, sharp seam burrs, or delaminated layers.

> **INGESTION HAZARD — COIN CELL BATTERY SAFETY (REESE'S LAW / 16 CFR PART 1263):**  
> The physical StackCalc SC-6 handheld calculator operates on an internal **CR2032 lithium coin cell battery ($3.0\,\text{V}$)**.
> - **DEATH or serious injury can occur if ingested.** A swallowed button or coin cell battery can cause **Internal Chemical Burns in as little as 2 hours**.
> - **KEEP new and used batteries OUT OF REACH of children.** Adults must verify that the tool-secured battery compartment screw and dovetail latch are fully fastened before handing the instrument to a child.
> - **Seek immediate medical attention** if a battery is suspected to be swallowed or inserted inside any part of the body. In the United States, call the **National Battery Ingestion Hotline at 1-800-498-8666** immediately.

**Trademark Attribution & Non-Affiliation Notice:** StackCalc™, StackCalc SC-6™, and StackCalc SC-32™ are independent products of StackCalc (stackcalc.io).
* **HP®**, **Hewlett-Packard®**, and **HP-32SII™** are registered trademarks or trademarks of **HP Inc.**, which does not sponsor, endorse, or affiliate with this textbook.
* **Unifix®** is a registered trademark of Didax, Inc.; **Cuisenaire®** is a registered trademark of Hand2Mind, Inc.; **Singapore Math®** and **Dimensions Math®** are registered trademarks of Singapore Math Inc.; **Big Ideas Math®** is a registered trademark of Larson Texts, Inc. All references to curriculum frameworks and classic classroom block systems are strictly nominative and comparative for educator cross-reference.
* **Gridfinity** is an open-source modular storage specification created by Zack Freedman (MIT License).

---

### Ready to Open Your Desk Studio?

Whether you are a young builder opening your calculator and block trays for the very first time, a parent exploring evening kitchen-table puzzles, or a teacher setting up a hands-on math station, every chapter ahead begins with something you can touch, see, and build before a single button is pressed.

As you work through the puzzles and maker labs in this book, notice how quickly your confidence grows when you can *see* every step of your thinking. If an answer ever looks unexpected, you never have to erase a whole page and start over from scratch: a single tap of `{{key:LASTX}}` brings your last number right back onto Ground Shelf $X$, and switching to a visual mode like `{{key:▦}}`, `{{key:LINE}}`, or `{{key:PV}}` lets you inspect the picture behind the digits immediately.

Whenever a math question looks big or unfamiliar, you never have to guess at a formula in the dark: you can reach into your tray, snap together a physical model you can rotate and measure with your fingers, and watch the exact same numbers ride up and down the shelves of your screen. Turn the page to **[Chapter 1: Meet Your SC-6 Stack Calculator & Math Blocks](01-hardware-architecture.md)**, where we will set up your desk studio, wake up the daylight screen, and discover the clever engineering hidden inside your calculator and blocks!
