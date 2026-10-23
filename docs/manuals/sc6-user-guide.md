---
title: "From Blocks to the Stack: Hands-On Math & the SC-6 Stack Calculator (Complete Edition)"
description: "Complete single-page edition of From Blocks to the Stack: Hands-On Math & the SC-6 Stack Calculator."
---

# Preface: Why Your Brain Already Thinks in a Stack

## Welcome, Explorer! How Hands-On Building Connects to Numbers

If an adult handed you this book and said, *"Here, read this math manual,"* you probably wanted to groan and hide it under your bed. Most school math books feel like an obstacle course: pages of repetitive drills, mysterious rules like *"borrow from the neighbor,"* and giant tangles of parentheses where one tiny slip ruins your whole page.

**Here is the good news: this is not a normal school math book, and the calculator in your hands is not a normal calculator.**

Before you press a single button, think about how you build things with your hands in everyday life. Suppose you have **7 red LEGO bricks** on your desk, and your friend hands you **5 gold bricks**. How do you find out how many bricks you have altogether?

You don't wave a magic wand in the air and shout, *"Plus! Seven! Five! Equals!"*  
Instead, you do three simple things with your hands:
1. You place the **first pile (`7`)** on your desk.
2. You place the **second pile (`5`)** right beside it.
3. You **push the two piles together** into **`12`**.

Every time you stack pancakes on a plate, pack books into your backpack, or build a tower out of blocks, your hands follow that exact rhythm: **first put the pieces on the table, then do something with them.**

In mathematics and computer science, that everyday workspace has a special name: **a Stack**.

### Why Do Ordinary Calculators Hide Your Numbers?

Think about what happens when you type `7 + 5 =` on an ordinary pocket calculator or a tablet app. You type `7`, and then the moment you press `+` and `5`, your `7` disappears from the screen! Then you press `=`, and the `5` disappears too, replaced by `12`. Both of the numbers you started with have vanished into a hidden black box.

As education researchers and mathematicians including Jerome Bruner *([Bruner, 1966](sc6/appendix-c-formulas-and-conversions.md#cite-bruner1966))*, Liping Ma *([Ma, 1999](sc6/appendix-c-formulas-and-conversions.md#cite-ma1999))*, and Steven Strogatz *([Strogatz, 2012](sc6/appendix-c-formulas-and-conversions.md#cite-strogatz2012))* have shown, an overuse of the `=` button trains learners to treat math as a magic trick that spits out answers rather than a physical balance of quantities you can see and touch. Worse yet, if a problem has two parts—like buying two notebooks and four pencils—an ordinary calculator forces you to wrap everything in parentheses `( ... )` or scribble halfway answers on scrap paper because its screen can only hold one number at a time.

### Meet the Four Shelves of Your Number Stack ($X, Y, Z, T$)

Now look closely at the bottom-right corner of your **StackCalc SC-6**. Notice anything missing?  
**There is no equals (`=`) button.**

Instead of an `=` button, there is a wide button labeled **`[ENTER]`**, and the screen above it acts like a **stack of four sturdy shelves** where your numbers stay in plain sight while you work:

- **Shelf $X$ (Your Workbench):** This is the bottom shelf (or the right side of the split `Y | X` screen). Every number you type appears right here on the Workbench, and every answer lands here too.
- **Shelf $Y$ (The Waiting Shelf):** This shelf sits right above the Workbench (or on the left side of the `Y | X` screen). Whenever you finish typing your first number and press **`[ENTER]`**, an invisible elevator lifts that number up onto Shelf $Y$ so your Workbench ($X$) is clear for the next number.
- **Shelves $Z$ and $T$ (The Upper Shelves):** Above Shelf $Y$ sit two more waiting shelves. Whenever a math puzzle has two or three separate parts, finished pieces ride safely upstairs to Shelves $Z$ and $T$ until you need them—so you never have to write intermediate numbers on scrap paper or juggle parentheses in your head.

![The StackCalc SC-6 Elementary RPN Hardware Calculator](../assets/renders/sc6-elementary-hero.png)

### Your Very First Stack Move: Adding `7` and `5`

Pick up your SC-6 (or place seven and five counting tiles on your desk) and try your very first stack calculation:
1. **Put the first number on the Workbench:** Tap `7`. You see `7` sitting on Shelf $X$.
2. **Lift it to the Waiting Shelf:** Tap **`[ENTER]`**. That tells the calculator, *"My first number is finished—lift it up to Shelf $Y$ so I can type the next number."*
3. **Put the second number on the Workbench:** Tap `5`. Now look at your screen: `7` is waiting on Shelf $Y$, and `5` is sitting on Shelf $X$. Both numbers are right in front of your eyes at the same time.
4. **Combine them:** Tap **`[+]`**. Instantly, Shelf $Y$ drops down and fuses with Shelf $X$ to make **`12`**.

| Calculator Approach | Keystroke Sequence | What You See Happen |
|---|---|---|
| **Traditional Algebraic (Infix)** | `7` `+` `5` `=` $\longrightarrow 12$ | The `+` key hides `7` in invisible memory while waiting for `5`. The `=` key erases the problem structure, hiding where intermediate values live. |
| **Stack Math (RPN)** | `7` `[ENTER]` `5` `[+]` $\longrightarrow 12$ | `7` rises visibly to Shelf $Y$; `5` enters Shelf $X$; `[+]` combines them visibly into `12`. Every number stays in plain sight with zero parentheses. |

You didn't need an `=` button, because **pushing the two numbers together with `[+]` *is* the answer.** Mathematicians call this **Reverse Polish Notation (RPN)**—or as we call it throughout this book, **Stack Math**—and it is the exact way rocket engineers, scientists, and computers solve problems.

---

## Walking Through Your First Everyday Stack Stories

Once you know how to put a number on Shelf $Y$ with `[ENTER]` and put a second number on Shelf $X$, you can already solve real-world stories. Let's walk through a few gentle examples together. Beneath each story is a **4-Register Stack Table** that shows you what is sitting on each of the four shelves ($T, Z, Y,$ and $X$) after every button press.

### Taking Away: Finding Missing Spaces on a Ten-Frame Tray

Suppose Maya places **7 red counters** into her 10-space Ten-Frame tray, filling the top row of 5 and 2 more spaces on the bottom row. How many blue counters does she need to fill all 10 spaces?

In any subtraction story ($10 - 7$), we start with the whole amount (`10`) and take away the part we already have (`7`). On the stack, your starting number always goes onto the Waiting Shelf ($Y$) first via `10 [ENTER]`, the number you are taking away (`7`) goes onto the Workbench ($X$), and tapping `[-]` takes $X$ away from $Y$ to leave **`3`** empty spaces:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `[C]` | 0 | 0 | 0 | 0 | Clean baseline stack in `[NUM]` mode. |
| `10` | 0 | 0 | 0 | 10 | Key target capacity ($10$) into Ground Floor $X$. |
| `[ENTER]` | 0 | 0 | 10 | 10 | Target capacity lifts smoothly into Mezzanine Floor $Y$. |
| `7` | 0 | 0 | 10 | 7 | Enter red counters into Ground Floor $X$. |
| `[-]` | 0 | 0 | 0 | 3 | Subtraction combines $Y - X = 3$. Result in $X$. |

*What if your screen says `17` instead of `3`?* That just means your thumb tapped `[+]` instead of `[-]`! And what if you accidentally typed `7 [ENTER] 10` in the wrong order? You don't have to erase and start over: tapping the **`[x⇄y]` (Swap)** key trades the numbers on Shelf $Y$ and Shelf $X$ so `10` is back on top and `7` is on the bottom!

### Checking Your Own Work in One Tap (`[f] [LASTX]`)

Every teacher and parent says, *"Always check your work!"* On a regular calculator, checking an addition problem by subtracting is annoying because you have to type the numbers all over again.

On the SC-6, every time an operation combines two numbers, the calculator automatically tucks a backup copy of the number from Shelf $X$ into a special memory pocket called **`LAST x`**. Suppose you are counting trading cards: you have **24 cards** in your binder and **15 cards** in a tin box. You add `24 [ENTER] 15 [+]` to get **`39`**. How can you prove that `39` is right without typing `15` again?

Just tap **`[f] [LASTX]`**! Your `15` jumps right back onto Shelf $X$ while `39` automatically lifts up to Shelf $Y$. Now tap **`[-]`**, and `39 - 15` lands right back on your starting number, **`24`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `24 [ENTER]` | 0 | 0 | 24 | 24 | First number committed to Mezzanine Floor $Y$. |
| `15 [+]` | 0 | 0 | 0 | 39 | Addition completed; `LAST x` preserves $15$ in hardware. |
| `[f] [LASTX]` | 0 | 0 | 39 | 15 | Prior number ($15$) recalled into $X$; sum lifts to $Y$. |
| `[-]` | 0 | 0 | 0 | 24 | Inverse check: $39 - 15 = 24$. Starting number verified. |

(And if you ever add $47 + 36$ via `47 [ENTER] 36 [+]` $\implies \mathbf{83}$, tapping `[f] [LASTX] [-]` checks $83 - 36 = \mathbf{47}$ in two taps!)

### Sharing with Whole Groups and Leftovers (`[g] [÷R]`)

What happens when numbers don't divide evenly? Suppose you divide $17 \div 5$ on an ordinary calculator, and the screen says `3.4`. What does `0.4` mean when you are sharing 17 counting tiles among 5 friends? In real life, you cannot hand a friend `0.4` of a tile—each friend gets **3 whole tiles**, and there are **2 tiles left over**.

On your SC-6, the **`[g] [÷R]` (*Quotient & Remainder*)** key solves both parts of a sharing story at once. Imagine a group of **125 students and chaperones** heading to the science museum in vans that hold **8 passengers each**. When we put `125` on Shelf $Y$ (`125 [ENTER]`), put `8` on Shelf $X$, and tap **`[g] [÷R]`**, **Shelf $X$** shows **`15`** completely full vans, and **Shelf $Y$** holds the **`5`** leftover passengers who need one more van (so the school needs $15 + 1 = 16$ vans in all!):

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `125` | 0 | 0 | 0 | 125 | Total passengers entered into Ground Floor $X$. |
| `[ENTER]` | 0 | 0 | 125 | 125 | 125 committed and copied to Mezzanine Floor $Y$. |
| `8` | 0 | 0 | 125 | 8 | Capacity per van keyed into $X$. |
| `[g] [÷R]` | 0 | 0 | 5 | 15 | Integer division with remainder: $X = 15$ full vans, $Y = 5$ leftover passengers. |

---

## How the Upper Shelves Beat Parentheses on Two-Part Puzzles

Now that you have seen how Shelf $X$ and Shelf $Y$ work together on one-step stories, what happens when a math puzzle has **two or three steps**?

Suppose you are measuring your backyard to build a square brick patio. Your yard is **$12\text{ feet}$ wide**, and you leave a **$3\text{-foot}$ grass path** along one side ($12 - 3 = 9\text{ feet}$ on each side of the square patio). You want to find both the patio's **Area** in square bricks ($9 \times 9$) and the **Perimeter** of wooden edging around its 4 sides ($9 \times 4$).

Watch how smooth this is on the stack:
1. First subtract the grass path: `12 [ENTER] 3 [-]` puts **`9`** on Shelf $X$.
2. Tap the **`[x²]` (Square)** key to multiply $9 \times 9 = \mathbf{81\text{ sq ft}}$ of bricks on Shelf $X$.
3. Now tap **`[f] [LASTX]`** to bring the $9\text{-foot}$ side length right back onto Shelf $X$ (which automatically lifts `81` onto Shelf $Y$!), and multiply by `4` (`4 [×]`) to see **`36` feet** of border edging on Shelf $X$ right beside **`81` square feet** of bricks on Shelf $Y$:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `12 [ENTER] 3 [-]` | 0 | 0 | 0 | 9 | Yard width minus grass path: $12 - 3 = 9\text{ ft}$ patio side. |
| `[x²]` | 0 | 0 | 0 | 81 | Square side length: $9 \times 9 = 81\text{ sq ft}$ patio area (`LAST x` saves 9). |
| `[f] [LASTX]` | 0 | 0 | 81 | 9 | Recall side length $9\text{ ft}$ into $X$; area $81$ lifts to $Y$. |
| `4 [×]` | 0 | 0 | 81 | 36 | Multiply side by 4: $9 \times 4 = 36\text{ ft}$ border perimeter ($Y$ still shows $81\text{ sq ft}$ area). |

Notice what happened when `9` returned to Shelf $X$: you didn't have to press `[ENTER]` before typing `4`! Why? Because **whenever a finished answer is sitting on Shelf $X$, typing a new number *automatically* lifts that finished answer up to the next shelf** to wait for you.

That **automatic stack lift** is why you never need parentheses `( )` on the SC-6. Suppose someone challenges you to solve this two-group puzzle:
$$(15 - 3) \times (4 + 2) \div 6$$

On a regular phone or school calculator, you have to hunt for `(` and `)` brackets and type the entire string before seeing a single intermediate number. On your SC-6 stack, you simply build one small group at a time:
1. **Build the first group (`15 - 3`):** Tap `15` `[ENTER]` `3` `[-]`. The screen immediately shows **`12`** on Shelf $X$.
2. **Build the second group (`4 + 2`):** Now just type `4` `[ENTER]` `2` `[+]`. The moment you type `4`, automatic stack lift carries your finished `12` upstairs to wait safely on Shelf $Z$ and drop back to Shelf $Y$, while `4` and `2` add together into **`6`** on Shelf $X$.
3. **Multiply the two groups and divide by `6`:** Now `12` is waiting on Shelf $Y$ and `6` is sitting on Shelf $X$. Tap **`[×]`** to multiply them into **`72`**, and then tap `6` **`[÷]`** to divide by 6:
   `15 [ENTER] 3 [-] 4 [ENTER] 2 [+] [×] 6 [÷]` $\longrightarrow$ **`12`**.

You can use that exact same rhythm on any two-group challenge, like $((18 + 6) \times (15 - 7)) \div 8$: build $18 + 6 = 24$, build $15 - 7 = 8$ (while `24` waits upstairs), multiply them into $192$, and divide by $8$:
`18 [ENTER] 6 [+] 15 [ENTER] 7 [-] [×] 8 [÷]` $\longrightarrow$ **`24`**.

---

## More Helper Keys & Visual Sandboxes Waiting for You

As you travel through the chapters ahead, you will meet several more helper keys that turn tricky topics into hands-on discoveries:

| Signature Key | How It Helps You |
| :--- | :--- |
| **Constant Repeat (`[g] [REP]`)** | **Skip-Counting & Times Tables:** Copies your number across all four shelves ($X = 7, Y = 7, Z = 7, T = 7$) so repeated taps of `[+]` climb times tables (`7, 14, 21, 28...`) or repeated taps of `[×]` double `2` twenty times past **one million (`1,048,576`)**! |
| **Quotient & Remainder (`[g] [÷R]`)** | **Whole Groups & Leftovers Together:** Divides in one tap, putting the whole groups (Quotient) on Shelf $X$ and the exact leftovers (Remainder) on Shelf $Y$. |
| **Step-by-Step Simplify (`[g] [SIMP]`)** | **Fraction Reduction You Control:** Keeps fractions like `. 12 . 18` unreduced until *you* press `[g] [SIMP]` to divide out shared factors into `2/3`, flashing `LOWEST TERMS` when fully simplified. |
| **Add to Total (`[Σ+]`)** | **A Shopping Basket for Totals:** Lets you toss finished numbers into a running basket (`1`, `2`, `3` items) and tap `[f] [Σx]` to see the grand total without writing anything on scrap paper. |

Look at how handy that **`[Σ+]` (*Add to Total*)** basket is when you reach geometry in Chapter 6. Imagine painting all 6 flat wooden walls of a rectangular treasure box that is **$5\text{ cm}$ long, $4\text{ cm}$ wide, and $3\text{ cm}$ high**—made of two $5 \times 4$ walls ($40\text{ cm}^2$), two $5 \times 3$ walls ($30\text{ cm}^2$), and two $4 \times 3$ walls ($24\text{ cm}^2$). Instead of jotting `40`, `30`, and `24` on paper, you clear the basket with `[g] [CLΣ]`, toss each pair of walls into the basket with `[Σ+]`, and tap **`[f] [Σx]`** to reveal all **`94.0` $\text{cm}^2$**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `[g] [CLΣ]` | 0 | 0 | 0 | 0 | Clear the running total before adding face pairs. |
| `5 [ENTER] 4 [×] 2 [×] [Σ+]` | 0 | 0 | 0 | 1 | Face Pair 1 ($40\text{ cm}^2$) added to total; Register $X$ shows `1` pair added. |
| `5 [ENTER] 3 [×] 2 [×] [Σ+]` | 0 | 0 | 0 | 2 | Face Pair 2 ($30\text{ cm}^2$) added to total; Register $X$ shows `2` pairs added. |
| `4 [ENTER] 3 [×] 2 [×] [Σ+]` | 0 | 0 | 0 | 3 | Face Pair 3 ($24\text{ cm}^2$) added to total; Register $X$ shows `3` pairs added. |
| `[f] [Σx]` | 0 | 0 | 0 | $94.0$ | Recall the Grand Total of All Pairs: $94\text{ cm}^2$ without scratch paper. |

### Build with Your Hands, See on the Screen, Combine on the Stack

Inspired by the cutaway mechanical illustrations of David Macaulay *([Macaulay, 2016](sc6/appendix-c-formulas-and-conversions.md#cite-macaulay2016))* and Jerome Bruner's discovery that we understand math best when we move from **hands-on objects** to **visual pictures** to **numbers** *([Bruner, 1966](sc6/appendix-c-formulas-and-conversions.md#cite-bruner1966))*, every chapter in this book connects three layers at your desk:

| Learning Phase | What You Use | How It Works at Your Desk |
|---|---|---|
| **1. Hands-On Blocks** | 3D-Printed Manipulative Kits | You build the problem with physical Ten-Frame Trays, $84\text{ mm}$ Fraction Towers, Four-Color Counting Tiles, Prime Factor Blocks, and a Planetary Geared Clock (which you will meet in Chapter 1). |
| **2. Visual Screen Modes** | Daylight Paper-Like Visual Modes | You see the exact same model drawn on the SC-6 screen using Ten-Frame Mode `[▦]`, the Number Rack `[g] [COUNT]`, Number Line Jump Arcs `[f] [LINE]`, Place Value `[PV]`, the Geared Clock Dial `[🕒]`, Polyhedral Dice `[🎲]`, or the 6-Level Math Quiz Game `[f] [?]`. |
| **3. The Number Stack** | Four-Shelf RPN Stack ($X, Y, Z, T$) | You combine your numbers on the four visible stack shelves—solving multi-step puzzles, remainder division, and 3D surface area without parentheses or scratch paper. |

Whenever you are inside one of the visual screen modes (`[▦]`, `[g] [COUNT]`, `[f] [LINE]`, `[🕒]`, `[🎲]`) and want to switch back to regular numbers, just tap **`[C]` (Clear)** once when you aren't typing digits. Switching between visual pictures and regular numbers never erases your stack—it simply changes the lens through which you look at the numbers on your shelves!

![StackCalc SC-6 Elementary Calculator Faceplate & 43-Key Topography](../assets/manuals/screenshots/sc6_hero_calculator.png)
*Figure 0.1: The StackCalc SC-6 Elementary RPN Calculator faceplate, featuring 19 oversized tactile switches with sculpted TPU keypads, a double-wide `[ENTER]` key, and `[f]` and `[g]` shift legends.*

### Three Helpful Stack Habits as You Start

1. **`[ENTER]` Keeps Your Number; `[C]` Clears It:** The big **`[ENTER]`** button is the elevator door that locks your number in and lifts it up to Shelf $Y$. The **`[C]`** button is the eraser that clears Shelf $X$ back to `0`.
2. **Typed Two Numbers Backward for Subtraction or Division? Just Tap `[x⇄y]`:** If you ever type `8 [ENTER] 15` when you meant $15 - 8$, don't erase! Just tap **`[x⇄y]`** to swap their shelves (`15` in $Y$, `8` in $X$), and press `[-]`.
3. **Entering Clock Time (`2.30` Means 2 Hours 30 Minutes):** When you use the Geared Clock (`[🕒]`) in Chapter 6, type `2` hours and `30` minutes just like a digital wall clock as **`2.30`** (and if you have `2.5` decimal hours, tapping `[g] [▸HMS]` converts `2.5` into `2:30:00` automatically).

| Everyday Math Problem | Standard Calculator (Infix) | StackCalc SC-6 (RPN) | Why the Stack Feels Easier |
| :--- | :--- | :--- | :--- |
| **1. Checking Addition** $(47 + 36) - 36 = 47$ | `47 + 36 = - 36 =` (9 strokes; re-types 36) | `47` `[ENTER]` `36` `[+]` `[f] [LASTX]` `[-]` (6 strokes) | **`[f] [LASTX]` remembers `36`** so you never re-type it. |
| **2. Two-Part Puzzle** $(15 - 3) \times (4 + 2) \div 6$ | `( 15 - 3 ) × ( 4 + 2 ) ÷ 6 =` (18 strokes) | `15 [ENTER] 3 [-] 4 [ENTER] 2 [+] [×] 6 [÷]` $\to$ **`12`** (11 strokes) | **Zero parentheses**; you see `12` and `6` before multiplying. |
| **3. Sharing with Leftovers** $125 \div 8 = 15\text{ R }5$ | `125 ÷ 8 =` (`15.625`), then multiply & subtract on paper | `125` `[ENTER]` `8` `[g] [÷R]` $\to$ `15` ($X$) & `5` ($Y$) (5 strokes) | **Shows `15` vans and `5` leftover riders** at the same time. |
| **4. Adding Fractions** $\frac{3}{8} + \frac{5}{12} = \frac{19}{24}$ | `( 3 ÷ 8 ) + ( 5 ÷ 12 ) =` (gives decimal `0.79167`) | `. 3 . 8` `[ENTER]` `. 5 . 12` `[+]` $\to$ **`19/24`** (8 strokes) | **Keeps exact fractions** that match your Fraction Towers. |
| **5. Box Surface Area** ($5 \times 4 \times 3$ box) | `2 × 5 × 4 + 2 × 5 × 3 + 2 × 4 × 3 =` | Toss each wall pair into `[Σ+]`, then tap `[f] [Σx]` $\to$ **`94`** | **Zero scrap paper**; the basket counts `1, 2, 3` wall pairs. |

---

## How to Navigate This Book & Topic Finder

This book is organized into nine hands-on chapters and four reference appendices. You can read it straight through from Chapter 1 to Chapter 9 as a story of mathematical discovery, or jump directly to the topic you are exploring today (and for **25 additional Quick-Start Warm-Up Adventures**, open the companion **[SC-6 Elementary Companion Problem & Activity Workbook](../curriculum/sc6-elementary-companion-workbook.md)**):

- **Building Your Stack & Whole-Number Foundations ([Chapters 01](sc6/01-hardware-architecture.md)–[04](sc6/04-operations-skip-counting.md)):** Set up your desk studio and meet your 3D-printed math blocks in [Chapter 01](sc6/01-hardware-architecture.md), ride the full 4-story Number Elevator in [Chapter 02](sc6/02-rpn-for-young-learners.md), explore ten-frames, number lines, and place value up to billions in [Chapter 03](sc6/03-counting-place-value.md), and build multiplication tile arrays, skip-counting ladders (`[g] [REP]`), and remainder division (`[g] [÷R]`) in [Chapter 04](sc6/04-operations-skip-counting.md).
- **Fractions, Geometry, Primes & Data ([Chapters 05](sc6/05-fractions-decimals-ratios.md)–[07](sc6/07-data-probability-primes.md)):** Master equivalent fractions, common denominators, decimals, and ratios with the $84\text{ mm}$ Fraction Towers in [Chapter 05](sc6/05-fractions-decimals-ratios.md); unfold 2D shapes, 3D surface area (`[Σ+]`), volumes, and planetary clock gears in [Chapter 06](sc6/06-geometry-surface-area.md); and explore prime factor towers (`[g] [FACT]`), dice probability (`[🎲]`), fair-share statistics (`[g] [x̄]`, `[g] [MAD]`), and negative numbers in [Chapter 07](sc6/07-data-probability-primes.md).
- **Mental Math Sprints & Maker STEM Labs ([Chapters 08](sc6/08-math-quiz-engine.md)–[09](sc6/09-applied-stem-labs.md)):** Discover 8 mental-math shortcuts and play 6 levels of arithmetic sprints (`[f] [?]`) in [Chapter 08](sc6/08-math-quiz-engine.md), then use your stack to weigh 3D-printed parts, slice layers, time pendulums, scale recipes, and test gear trains in [Chapter 09](sc6/09-applied-stem-labs.md).
- **3D-Printable Studios, Lesson Plans & Reference Guides ([Appendices A](sc6/appendix-a-manipulative-blueprints.md)–[D](sc6/appendix-d-keycap-directory.md)):** Find the 3D-printing guide in [Appendix A](sc6/appendix-a-manipulative-blueprints.md), 25 classroom station lesson plans in [Appendix B](sc6/appendix-b-teacher-lesson-plans.md), word rules and unit conversions in [Appendix C](sc6/appendix-c-formulas-and-conversions.md), and the 43-button directory in [Appendix D](sc6/appendix-d-keycap-directory.md).

### Chapter-by-Chapter Guide

| Chapter / Appendix | Core Mathematical Focus & Story Arc | Physical Manipulative Studio | Primary SC-6 Keycaps | Hands-On Explorations |
| :--- | :--- | :--- | :--- | :--- |
| **[Chapter 01](sc6/01-hardware-architecture.md)** | Setting up your desk studio, first block-and-stack discoveries, daylight screen & button feel | All 8 Companion Studios & Quest Scoreboard | `[ENTER]`, `[+]`, `[×]`, `[C]`, `[<-]`, `[f]`, `[g]` | Measuring screen pixels, snap-domes, Gridfinity trays & battery life |
| **[Chapter 02](sc6/02-rpn-for-young-learners.md)** | Riding the 4-shelf RPN stack ($X, Y, Z, T$) & solving multi-step order of operations without parentheses | Stack Shelves & Counting Tiles | `[ENTER]`, `[+]`, `[-]`, `[x⇄y]`, `[f] [R↓]`, `[f] [CSTK]` | Playground construction, sky-tower lifts, farmers' market & museum vaults |
| **[Chapter 03](sc6/03-counting-place-value.md)** | Subitizing, make-ten bridging, multi-digit place value (`1000 \| 100 \| 10 \| 1`), rounding & negative number-line hops | Ten-Frame Studio, Number Rack & Place Value Trays | `[▦]`, `[g] [COUNT]`, `[f] [LINE]`, `[PV]`, `[$]` | Ten-frame bridging, place-value bundling, submarine dives & book-fair budgets |
| **[Chapter 04](sc6/04-operations-skip-counting.md)** | Rectangular multiplication arrays, rhythmic skip-counting ladders, powers & fair-share division with remainders | 24-Tile Counting & Array Studio | `[×]`, `[÷]`, `[g] [REP]`, `[g] [÷R]`, `[f] [MOD]`, `[f] [LASTX]` | Tile arrays, doubling legends, bus remainders & multi-step camp logistics |
| **[Chapter 05](sc6/05-fractions-decimals-ratios.md)** | Equivalent fractions, step-by-step factor reduction, common denominators, mixed numbers, decimals, percents & ratios | 84 mm Fraction Tower Studio & Decimal Tray | `[a ᵇ/c]`, `[f] [d/c]`, `[g] [SIMP]`, `[FDISP]`, `[%]`, `[g] [%CHG]` | Fraction tower alignment, carpentry cuts, recipe scaling & store discounts |
| **[Chapter 06](sc6/06-geometry-surface-area.md)** | 2D area/perimeter, Pythagorean theorem, 3D prism/cylinder/cone volume, surface area via `[Σ+]` & modulo-60 clock time | Counting Tiles, L-Frame, Volvelle & Geared Clock | `[f] [RECT]`, `[f] [CIRC]`, `[f] [PRISM]`, `[Σ+]`, `[🕒]`, `[f] [▸HR]` | Penguin huddles, garden borders, gift-box wrapping, silos & train timetables |
| **[Chapter 07](sc6/07-data-probability-primes.md)** | Prime factor trees, GCF & LCM, polyhedral dice probability, dot plots, mean/median/IQR/MAD & signed integers | Prime Factor Studio, Polyhedral Dice & Two-Color Counters | `[PRIME]`, `[g] [FACT]`, `[GCF]`, `[f] [LCM]`, `[🎲]`, `[g] [x̄]`, `[f] [MED]`, `[+/-]` | 17-year cicadas, gear teeth, dice trials, weather data & ocean trenches |
| **[Chapter 08](sc6/08-math-quiz-engine.md)** | Mental math shortcuts (Vedic squares, 11s trick, Gauss sums) & 6-level timed fluency sprints | Math Dominoes & Quest Scoreboard | `[f] [?]` (`[f]` + `[C]`), `[f] [LASTX]`, Classroom Seeds | Mental-math patterns & 6-level astronaut flight-simulator sprints |
| **[Chapter 09](sc6/09-applied-stem-labs.md)** | 3D-printed block weights and layer slicing, bean sprout growth, recipe scaling, gear ratios, and solar ovens | All Studios + Calipers, Scale & Stopwatches | `[π]`, `[x²]`, `[f] [√x]`, `[f] [▸g]`, `[f] [▸cm]`, `[f] [▸°C]` | 3D printer slicing, pendulum clocks, botanical growth & maker workshops |
| **[Appendices A–D](sc6/appendix-a-manipulative-blueprints.md)** | CAD/3D-print blueprints ([App. A](sc6/appendix-a-manipulative-blueprints.md)), 25 station lesson plans ([App. B](sc6/appendix-b-teacher-lesson-plans.md)), formulas & primes ([App. C](sc6/appendix-c-formulas-and-conversions.md)), and 43-key matrix ([App. D](sc6/appendix-d-keycap-directory.md)) | Full Manipulative & Curriculum Reference Suite | Complete 43-Key Hardware Matrix | Turnkey Classroom & Home Reference |

---

## Safety, Regulatory, Trademark & Parent/Educator Notices

> **CHOKING HAZARD — SMALL PARTS (16 CFR § 1501 / ASTM F963):**  
> The physical StackCalc manipulative kits (Counting & Array Tiles, Ten-Frame Flip Counters, Fraction Studio 1/12 Blocks, Prime Factor Studio Blocks, Math Dominoes, and Polyhedral Dice) contain small modular parts ($7.0\,\text{mm}$ minimum thickness). **Not for children under 3 years of age.** Use only under adult or educator supervision.
> - **3D-Printed Part Inspection:** When fabricating manipulative kits on classroom or home Fused Deposition Modeling (FDM) 3D printers, adults must use non-toxic PLA or PETG filament and inspect every finished piece prior to student handling—removing any loose filament strings, sharp seam burrs, or delaminated layers.

> **INGESTION HAZARD — COIN CELL BATTERY SAFETY (REESE'S LAW / 16 CFR PART 1263):**  
> The physical StackCalc SC-6 handheld calculator operates on an internal **CR2032 lithium coin cell battery ($3.0\,\text{V}$)**.
> - **DEATH or serious injury can occur if ingested.** A swallowed button or coin cell battery can cause **Internal Chemical Burns in as little as 2 hours**.
> - **KEEP new and used batteries OUT OF REACH of children.** Adults must verify that the tool-secured battery compartment screw and dovetail latch are fully fastened before handing the instrument to a child.
> - **Seek immediate medical attention** if a battery is suspected to be swallowed or inserted inside any part of the body. In the United States, call the **National Battery Ingestion Hotline at 1-800-498-8666** immediately.

### Trademark Attribution & Non-Affiliation Notice
StackCalc™, StackCalc SC-6™, and StackCalc SC-32™ are independent products of StackCalc (stackcalc.io).
* **HP®**, **Hewlett-Packard®**, and **HP-32SII™** are registered trademarks or trademarks of **HP Inc.**, which does not sponsor, endorse, or affiliate with this textbook.
* **Unifix®** is a registered trademark of Didax, Inc.; **Cuisenaire®** is a registered trademark of Hand2Mind, Inc.; **Singapore Math®** and **Dimensions Math®** are registered trademarks of Singapore Math Inc.; **Big Ideas Math®** is a registered trademark of Larson Texts, Inc. All references to curriculum frameworks and classic manipulative systems are strictly nominative and comparative for educator cross-reference.
* **Gridfinity** is an open-source modular storage specification created by Zack Freedman (MIT License).

---

# Chapter 1: Meet Your SC-6 Stack Calculator & Math Blocks

## 1.1 Why Real Buttons, a Daylight Screen & a Number Stack Help You Think

Picture sitting at your kitchen table on a rainy Tuesday afternoon. Your math book is open on the desk, and right beside it rests a glowing tablet. Within ninety seconds of starting your work, a notification banner slides across the glass: a message chime, a game update, a video alert. Even when locked in "study mode," the tablet's bright electric backlight shines straight into your eyes like a flashlight, and its flat glass screen gives your fingers nothing to feel.

Now look at the other side of your desk: the **StackCalc SC-6**. Molded from tough, dark Midnight Navy plastic, it has no Wi-Fi, no pop-up alerts, and no noisy distractions. Its screen doesn't beam harsh light into your face—it reflects the natural daylight in your room just like a page of paper. And when you press a key, your finger doesn't slide across flat, silent glass. Beneath every keycap sits a tiny stainless-steel spring dome that clicks down with a crisp, satisfying *snap!*

![StackCalc SC-6 Elementary Handheld Portrait](../assets/manuals/screenshots/sc6_hero_calculator.png)
*Figure 1.1: The StackCalc SC-6 Elementary Handheld in Midnight Navy with sliding 15° easel desk cowl. A dedicated tactile tool for deep mathematical focus.*

Educational researchers John Sweller *([Sweller, 1988](sc6/appendix-c-formulas-and-conversions.md#cite-sweller1988))* and George A. Miller *([Miller, 1956](sc6/appendix-c-formulas-and-conversions.md#cite-miller1956))* discovered that human working memory can only hold about four to seven pieces of new information at once. When you try to solve a math puzzle on a glowing tablet—or on an ordinary calculator that hides your numbers and forces you to juggle parentheses—those distractions crowd out your working memory. Inspired by David Macaulay's cutaway illustrations of how machines work *([Macaulay, 2016](sc6/appendix-c-formulas-and-conversions.md#cite-macaulay2016))*, the SC-6 pairs **physical math blocks on your desk** with **four visible number shelves on the screen**, freeing your mind to focus completely on the math in your hands.

### 1.1.1 What Is a Stack, and Why Is It Such a Useful Idea?

If you look at the bottom-right corner of your SC-6 keypad, you will notice something surprising right away: **there is no equals (`=`) button.**

Why would a calculator leave off the `=` button? Think about how you build things with your hands in real life. Suppose you want to add **5 blue counting tiles** and **3 gold counting tiles** on your desk:
1. First, you place the **5 blue tiles** on the table.
2. Next, you place the **3 gold tiles** right beside them.
3. Finally, you **slide the two piles together** to make **`8`**.

Notice that in the real world, you always **put the pieces on the table first**, and **do the action last**. You don't put `5` down, wave a `+` sign in the air, make the `5` vanish while you look for `3`, and then shout *"Equals!"* Yet that is what an ordinary calculator does: the moment you type `5 + 3 =`, the `5` and the `3` disappear one after another, hiding your steps inside a black box.

Your SC-6 works the way your hands naturally build. Instead of hiding numbers, its screen is organized like a **stack of four sturdy shelves**—called **Registers $X, Y, Z,$ and $T$**—where your numbers stay in plain sight while you work:

- **Shelf $X$ (The Ground Shelf / Your Workbench):** The bottom shelf of the screen (or the right side of the split `Y | X` view). Every number you type appears right here on the Workbench, and every answer lands here too.
- **Shelf $Y$ (The Second Shelf / Your Waiting Shelf):** The shelf directly above $X$ (or the left side of the `Y | X` view). When you finish typing your first number (`5`) and press the wide **`[ENTER]`** button, an invisible elevator lifts `5` up onto Waiting Shelf $Y$ so your Workbench ($X$) is clear for the second number (`3`).
- **Shelves $Z$ and $T$ (The Upper Waiting Shelves):** Above Shelf $Y$ sit two more shelves. Whenever a puzzle has two or three parts, your finished subtotals ride safely upstairs to Shelves $Z$ and $T$ to wait for you—and automatically drop back down when you are ready to combine them!

### 1.1.2 Try Your First Block-and-Stack Move (`5 + 3 = 8`)

Let's try that four-step rhythm right now using your Counting Tiles and your keypad:
1. Press **`[C]`** once to wake the daylight screen and start with a clean stack (`0`).
2. **Build Group 1:** Place **5 blue counting tiles** in the top row of your tray, type `5` on the keypad, and press **`[ENTER]`**. Look at the screen: `5` just rode the elevator up onto Waiting Shelf $Y$!
3. **Build Group 2:** Place **3 gold counting tiles** in the bottom row of your tray, and type `3` on the keypad. (Do *not* press `[ENTER]` after the second number!) Now look at your screen: `5` is waiting on Shelf $Y$ and `3` is sitting on Shelf $X$, matching the two rows of tiles on your desk.
4. **Combine Them:** Slide the 3 gold tiles up beside the 5 blue tiles to count **8 tiles**, and tap **`[+]`** on your keypad. Instantly, Shelf $Y$ drops down and fuses with Shelf $X$ to show **`8`**.

### 1.1.3 Direct Keys, Shift Keys (`[f]` and `[g]`) & Your $15^\circ$ Desk Stand

Instead of hiding math tools inside confusing computer menus, every sculpted button on the SC-6 can perform up to **three actions**:
- **Direct Press:** Tapping any key directly uses the main white label on the keycap face—digits `0`–`9`, `[ENTER]`, `[+]`, `[-]`, `[×]`, `[÷]`, clear `[C]`, and backspace `[<-]` (which erases the last digit if you make a typing slip).
- **`[f]` Shift Key:** Pressing `[f]` first activates the feature printed directly above the keycap, such as finding common multiples with `[f] [LCM]`, simplifying fractions step-by-step with `[g] [SIMP]`, recalling your last number with `[f] [LASTX]`, and inspecting memory `[f] [REGS]`.
- **`[g]` Shift Key:** Pressing `[g]` first activates the feature printed on or below the keycap, such as prime factor trees with `[g] [FACT]`, skip-counting ladders with `[g] [REP]`, whole-number division with remainder `[g] [÷R]`, low-power sleep `[g] [OFF]`, and settings `[g] [FLAGS]`.

> **Faceplate Themes & Shift Legend Conventions**
>
> Because the StackCalc SC-6 hardware faceplates and companion app support multiple visual themes (`Pure Black`, `Retro Futurism`, `Pioneer`, `Stealth`, `Supernova`, `Voyager`, and `Arcade`), keycap and shift accent colors vary by faceplate. Throughout this textbook, shifted operations are always referenced by their shift symbols rather than color: **`[f]` Shift** and **`[g]` Shift**.

Before we open your math block kits, slide the protective cover downward off the front of your calculator, flip the calculator over, and slide the cover onto the rear rails until it clicks into place. Your SC-6 now rests at a hands-free **$15^\circ$ reading angle**, leaving your left hand free to build with blocks while your right hand taps keys onto the stack.

---

## 1.2 Meet Your Nine 3D-Printed Math Block Studios

Why is your SC-6 calculator molded in dark Midnight Navy or Slate Gray, while your math blocks are bright white, radiant gold, and electric blue?

Think about how an astronomer uses a telescope: the tube of the telescope is dark matte black so stray light doesn't bounce into your eyes, letting you focus clearly on the bright stars. Your dark calculator frame gives your eyes a quiet, glare-free place to read numbers, while the bright math blocks invite your hands to reach out, sort, stack, and build.

![Companion Manipulative Color Palette: Matte Slate Enclosure and Color-Coded Math Blocks](../assets/renders/materials_swatch_grid.png)

> **Color Design: Dark Calculator vs. Bright Math Blocks:** To make sure your eyes can tell the calculator and the blocks apart at a glance, the SC-6 case, bezel, and sliding cover are molded from dark matte plastics (Midnight Navy, Space Gray, or Matte Black), while bright white, gold, red, and blue colors are reserved for your physical math blocks (84 mm Fraction Towers, Ten-Frame counters, Counting Tiles, and Planetary Clock gears).

Whenever you start an activity in this book, place your **3D-printed block tray on the left side of your desk** and your **SC-6 in its $15^\circ$ stand on the right**. Every activity follows the same four hands-on steps:

| Desk Step | What Your Left Hand Does (The Blocks) | What Your Right Hand Does (The SC-6) | What You See & Feel |
| :---: | :--- | :--- | :--- |
| **Step 1: Build Group 1** | Place your first group of counters, tiles, or fraction towers into the **top/back row** (or Well A) of your tray. | Type that first number on the keypad and press `[ENTER]`. | Your first number rides up to **Shelf $Y$** on the screen, matching your top/back tray row. |
| **Step 2: Build Group 2** | Place your second group of blocks into the **bottom/front row** (or Well B) of your tray. | Type that second number into **Shelf $X$** (do not press `[ENTER]` after the second number). | Now **Shelf $Y$** and **Shelf $X$** on the screen mirror the two physical groups sitting on your desk. |
| **Step 3: Combine by Hand** | Slide the counters across the **5-anchor rib** to fill a ten-frame, rotate the tile array, or stack the fraction blocks in the **84 mm comparator well**. | Feel with your fingertips whether the ten-frame is full or the fraction towers sit flush at the top edge. | Your hands discover the physical answer *before* the calculator computes it. |
| **Step 4: Fuse on the Stack** | Point to your combined physical blocks on the tray. | Press the operation key (`[+]`, `[-]`, `[×]`, `[÷]`, or `[g] [SIMP]`). | Shelf $Y$ and Shelf $X$ fuse into a single answer on **Shelf $X$**, confirming your physical block model. |

Here are the nine companion block studios that you will explore across this book:

### 1.2.1 The Ten-Frame Trays & Flip Counters (`[▦]`)
Two 5-pocket trays hold ten two-color disc counters (coral red on one side, radiant gold on the other). Built-in finger scoops make it easy to slide and flip counters, and a raised **5-anchor divider rib** splits each row of ten into two visual groups of 5 so your eyes can spot numbers at a glance (*subitizing*). Tap `[▦]` to see your trays drawn right on the calculator screen: Shelf $Y$ shows the top tray, Shelf $X$ shows the bottom tray, and tapping `[+]` slides counters across to fill a complete ten (`7 + 5 = 12`).

![Ten-Frame Studio: 5-Anchor Spotting at a Glance (5 Red + 3 Green = 8, 2 Empty to 10) and 70.0 mm 10-Rod Height Parity](../assets/manuals/ten_frame_subitizing_5anchor.png)

### 1.2.2 The Four-Color Counting & Array Studio (`[NUM]`)
Each kit holds 24 smooth-docking counting tiles in four colors (6 white, 6 blue, 6 gold, and 6 slate gray—or 144 tiles when 6 kits are shared at a table). Arrange tiles into rows and columns to build rectangular arrays for multiplication ($4 \times 6 = 24$), with rows on Shelf $Y$ and columns on Shelf $X$. Spin the tray sideways: 6 rows of 4 tiles still make 24—proving with your hands that changing the multiplication order never changes the total!

### 1.2.3 The 84 mm Fraction Towers & Comparator Tray (`[FDISP]` & `[g] [SIMP]`)
A $84.0\text{ mm}$ master tower represents $1\text{ Whole}$, paired with proportional fraction blocks ($1/2, 1/3, 1/4, 1/6, 1/8, 1/12$) and a side-by-side comparison tray. Why is the whole tower exactly **$84\text{ mm}$** tall? Because 84 divides evenly by $1, 2, 3, 4, 6, 7, 12, 14, 21, 28,$ and $42$—giving every fraction block an exact whole-millimeter height ($1/2 = 42\text{ mm}$, $1/3 = 28\text{ mm}$, $1/4 = 21\text{ mm}$, $1/6 = 14\text{ mm}$, $1/12 = 7\text{ mm}$)! Stack **twelve $7\text{ mm}$ Counting Tiles** right next to your **$84\text{ mm}$ 1-Whole Fraction Tower**, run your finger across their tops, and tap `12 [ENTER] 7 [×]` to see **`84`** millimeters on Shelf $X$. When you snap two $1/4$ towers together in the tray and type `. 2 . 4 [g] [SIMP]`, the screen simplifies `2/4` to `1/2` while your fingers feel their matching $42\text{ mm}$ height.

![Fraction Studio: Common Denominator Discovery on 12-Socket Lid Tray Proving 1/3 (28.0 mm) + 1/4 (21.0 mm) = 7/12 (49.0 mm)](../assets/manuals/fraction_studio_common_denominator.png)

### 1.2.4 The Prime Factor Studio (`[PRIME]` & `[g] [FACT]`) and Planetary Geared Clock (`[🕒]`)
In the **Prime Factor Studio**, prime-number blocks ($2, 3, 5, 7, \dots$) are scaled so that stacking block 2 on block 3 reaches the exact height of $2 \times 3 = 6$ on the back-wall scale, while typing `60 [g] [FACT]` on the keypad reveals $2^2 \times 3 \times 5$. In the **Planetary Geared Clock**, real interlocking 12-to-1 planetary gears link the minute hand and hour hand so turning the minute hand automatically glides the hour hand, matching the `[🕒]` Clock mode when you add hours and minutes across 60-minute boundaries.

### 1.2.5 The Polyhedral Dice (`[🎲]`), Place Value Trays (`[PV]`), Number Rack (`[g] [COUNT]`) & Quest Scoreboard (`[f] [?]`)
Rounding out your desk studio are precision **Polyhedral Dice** ($d4, d6, d8, d10, d12, d20$) that pair with `[🎲]` digital dice rolls; the **Whole & Decimal Place Value Trays** with digit miniblocks and `+1` regrouping cubes that pair with `[PV]` (`347 = 300 + 40 + 7`); the two-rail **Number Rack** (5 red and 5 white beads per row) that pairs with `[g] [COUNT]`; and the **Quest Scoreboard** pegboard where you place a `+10` token for solving with blocks and stack a second `+10` token (`10 [ENTER] 10 [+]` $\to \mathbf{20}$) for verifying on the SC-6.

### 1.2.6 Watching the Upper Shelves Work: Adding Up Your Desktop Math Station

Now let's see why having **four shelves ($T, Z, Y, X$)** on your screen is so helpful when a puzzle has more than one step!

Look at the undersides of your 3D-printed manipulative trays. To keep counters and fraction towers neatly organized on your desk, every tray snaps into a baseplate made of $42\text{ mm}$ squares called **Gridfinity squares**. Suppose you set up a desktop math station with three trays side by side:
- **1 Ten-Frame Tray:** $2\text{ squares long} \times 1\text{ square wide}$
- **1 Fraction Studio Well:** $3\text{ squares long} \times 1\text{ square wide}$
- **1 Counting & Array Box:** $3\text{ squares long} \times 2\text{ squares wide}$

How many Gridfinity squares does your whole station cover?

$$\text{Total Tray Squares} = (2 \times 1) + (3 \times 1) + (3 \times 2) = 2 + 3 + 6 = 11\text{ squares}$$

On an ordinary calculator, you would have to wrap each tray in parentheses `(2 × 1) + (3 × 1) + (3 × 2)` or write `2`, `3`, and `6` on scrap paper. On your SC-6, watch how the upper shelves hold each finished tray automatically (`2 [ENTER] 1 [×] 3 [ENTER] 1 [×] [+] 3 [ENTER] 2 [×] [+]` $\rightarrow$ **`11`**):
1. First multiply the **Ten-Frame Tray**: `2 [ENTER] 1 [×]` puts **`2`** on Shelf $X$.
2. Next multiply the **Fraction Well**: the moment you type `3 [ENTER] 1`, your finished `2` automatically rides the elevator up to **Shelf $Z$** to wait for you! When you tap `[×]`, the Fraction Well becomes `3` on Shelf $X$ while `2` drops back down to Shelf $Y$, and tapping `[+]` adds them into **`5`** squares.
3. Finally multiply the **Counting Box**: type `3 [ENTER] 2 [×]` (while `5` waits upstairs and drops back to Shelf $Y$) and tap `[+]` to land on **`11` Gridfinity squares**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2 [ENTER]` | 0 | 0 | 2 | 2 | Enter ten-frame tray length (2 units) into Register $Y$ |
| `1 [×]` | 0 | 0 | 0 | 2 | Ten-frame footprint: $2 \times 1 = 2\text{ units}$ in Register $X$ |
| `3 [ENTER]` | 0 | 2 | 3 | 3 | Footprint 2 lifts to $Z$; enter fraction well length (3 units) into $Y, X$ |
| `1 [×]` | 0 | 0 | 2 | 3 | Fraction well footprint: $3 \times 1 = 3\text{ units}$ in $X$ ($2$ drops to $Y$) |
| `[+]` | 0 | 0 | 0 | 5 | Combine footprints: $2 + 3 = 5\text{ units}$ in Register $X$ |
| `3 [ENTER]` | 0 | 5 | 3 | 3 | Subtotal 5 lifts to $Z$; enter counting box length (3 units) into $Y, X$ |
| `2 [×]` | 0 | 0 | 5 | 6 | Counting box footprint: $3 \times 2 = 6\text{ units}$ in $X$ ($5$ drops to $Y$) |
| `[+]` | 0 | 0 | 0 | 11 | Sum all footprints: $5 + 6 = 11\text{ Gridfinity units}$ ($462\text{ mm}$) |

Compare how an ordinary algebraic calculator handles everyday multi-step tasks against the visible shelves of your SC-6:

| Challenge / Real-World Task | The Algebraic Calculator Trap (Infix) | Algebraic Keystrokes & Clutter | The StackCalc + Blocks Method (RPN Stack + Visual Studio) | StackCalc Keystrokes | The Stack Advantage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **School Store Shopping:** Buying 2 Notebooks at $\$3.50$ and 4 Pencils at $\$0.75$: $(3.50 \times 2) + (0.75 \times 4)$ | A basic four-function calculator evaluates strictly left-to-right ($3.50 \times 2 + 0.75 = 7.75 \times 4 = \$31.00$), and on a scientific infix calculator, typing the full expression hides both individual subtotals ($\$7.00$ and $\$3.00$) until you press `=`. | `( 3 . 5 0 × 2 ) + ( 0 . 7 5 × 4 ) =` (21 keystrokes with brackets; subtotals hidden) | **RPN Elevator Stack:** Computes the notebook subtotal ($\$7.00$) and pencil subtotal ($\$3.00$) into visible shelves $Y$ and $X$, then combines them into $\$10.00$ with `[+]`. | `3.50 [ENTER] 2 [×] 0.75 [ENTER] 4 [×] [+]` (13 keystrokes) | **Both Subtotals Visible:** Zero parentheses; the $\$7.00$ notebook subtotal and $\$3.00$ pencil subtotal sit side-by-side on shelves $Y$ and $X$ before adding. |
| **Craft Ribbon Bookmarks:** Cutting $142\text{ cm}$ of Ribbon into $9.35\text{ cm}$ Strips ($142 \div 9.35$) | On a glowing tablet app, typing $142 \div 9.35 =$ erases both starting measurements the moment you press `=`, leaving only a decimal on a bright screen. | `1 4 2 . 0 / 9 . 3 5 =` (12 keystrokes; starting numbers disappear) | **Daylight Stack Division:** Places the $142\text{ cm}$ ribbon length on Shelf $Y$ and the $9.35\text{ cm}$ strip length on Shelf $X$ before dividing on a paper-like screen. | `142 [ENTER] 9.35 [÷]` (9 keystrokes) | **Clear Step-by-Step View:** Both the total ribbon length and strip size are visible on screen before dividing, with zero glare. |
| **Desktop Tray Footprint:** Total Gridfinity squares: $(2 \times 1) + (3 \times 1) + (3 \times 2)$ | Typing a chain of three products on an infix screen hides each individual tray area ($2$, $3$, and $6$) until the final `=`. | `( 2 * 1 ) + ( 3 * 1 ) + ( 3 * 2 ) =` (21 keystrokes with brackets) | **Progressive Stack Accumulation:** Each tray area ($2, 3, 6$) collapses cleanly on the stack, maintaining running totals without parentheses. | `2 [ENTER] 1 [×] 3 [ENTER] 1 [×] [+] 3 [ENTER] 2 [×] [+]` (16 keystrokes) | **Step-by-Step Verification:** Each tray footprint is verified on the live stack as physical trays dock into the baseplate. |

---

## 1.3 Behind the Scenes: How Engineers Used the Stack to Design Your Calculator

Now that you know how to put numbers on Shelf $Y$ and Shelf $X$ and let finished subtotals wait upstairs, let's peek behind the scenes! When the engineers designed the StackCalc SC-6, they had to solve five real-world math puzzles about its screen, its buttons, its stand, and its battery. You can solve all five of those engineering puzzles right now using the exact stack moves you just learned:

### 1.3.1 Counting the Tiny Pixel Dots on Your Screen
Lean in close and look at a digit on your calculator screen. Every number, ten-frame counter, and clock hand is drawn on a rectangular grid of tiny square dots called **pixels**—arranged just like a giant array of Counting Tiles with **$132$ columns across** and **$65$ rows high**. In computer memory, each pixel dot takes $1\text{ bit}$ (`1` for a dark dot, `0` for a silver-white dot), and **$8$ bits** pack neatly into **$1$ byte** of memory. How many pixel dots are on your screen altogether, and how many bytes of memory does it take to hold one full screen picture?

First multiply the $132$ columns by the $65$ rows (`132 [ENTER] 65 [×]`) to see all **`8,580` pixels** on Shelf $X$. Then type `8` (which automatically lifts `8,580` up to Shelf $Y$!) and tap `[÷]` (`132 [ENTER] 65 [×] 8 [÷]` $\rightarrow$ **`1072.5`**) to see that the whole screen fits into **`1072.5` bytes** ($1,073$ whole bytes). *(Try tapping `[f] [LASTX] [×]` right after—it brings back `8` and multiplies to show all $8,580$ pixels again!)*

### 1.3.2 Why the Daylight Screen Looks Like Real Paper
Why doesn't your SC-6 need a glowing electric backlight? Because tucked behind the pixel grid is a silvery mirror that bounces natural room light back to your eyes. Under classroom lights, a light sensor measures **$142.0$ units** of light bouncing off the silver background and only **$9.35$ units** bouncing off the dark numbers. Put `142` on Shelf $Y$ (`142 [ENTER]`), put `9.35` on Shelf $X$, and tap `[÷]` (`142 [ENTER] 9.35 [÷]` $\rightarrow$ **`15.187165775`**): the silver background is **`15.19` times brighter** than the dark numbers, making it as crisp and restful to read as ink on paper.

### 1.3.3 Why Every Button Clicks with a Crisp Snap
When you press a button on the keypad, the tiny stainless-steel spring dome underneath pushes back until your thumb presses with **$400.0\text{ grams}$** of weight over a **$1.6\text{ millimeter}$** downward travel—and then snaps down cleanly so you never press a key by accident. To find how many grams of push it takes for each millimeter the button travels downward:

$$\text{Grams per Millimeter} = \text{Push Weight} \div \text{Distance Pushed} = 400.0\text{ grams} \div 1.6\text{ millimeters} = 250.0\text{ grams per millimeter}$$

Put `400` on Shelf $Y$ (`400 [ENTER]`), put `1.6` on Shelf $X$, and tap `[÷]` (`400 [ENTER] 1.6 [÷]` $\rightarrow$ **`250`**) to see **`250.0` grams per millimeter**.

### 1.3.4 Measuring Your $15^\circ$ Desk Stand with 3 Counting Tiles
Look at the side of your SC-6 while it sits in its $15^\circ$ reading stand. For every $1\text{ mm}$ the calculator reaches back across your desk, the $15^\circ$ ramp lifts it **$0.2679\text{ mm}$** upward. Since the stand reaches **$80.0\text{ mm}$** from front to back, how many millimeters high is the top edge lifted above your desk? Put `80` on Shelf $Y$ (`80 [ENTER]`), put `0.2679` on Shelf $X$, and tap `[×]` (`80 [ENTER] 0.2679 [×]` $\rightarrow$ **`21.432`**) to see that the top edge lifts **`21.43` mm**—which you can check with your hands right now by stacking **3 Counting Tiles** ($3 \times 7\text{ mm} = 21\text{ mm}$) right behind the top edge of your calculator!

*(Curious how we 3D-printed the snap-together calculator case, tested the screen in a virtual simulator, and built an automated verification harness to test every math problem in this book? Check out **[Appendix A: Manipulative Studio Guide & How We Built StackCalc](sc6/appendix-a-manipulative-blueprints.md)**, **[stackcalc.io/hardware](https://stackcalc.io/hardware)**, and our open-source **[Hackaday Build Logs](https://hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator)**.)*

### 1.3.5 How One Coin Battery Lasts Nearly a Whole School Year
Whenever you turn your calculator off (`[g] [OFF]`) or let it fall asleep in your backpack after 3 minutes of quiet time, it automatically saves all four stack shelves ($X, Y, Z, T$), your `[f] [LASTX]` number, and your quiz streaks so you can pick up right where you left off.

How can a single battery the size of a nickel power your calculator for nearly a whole school year? Inside the rear safety-locked hatch sits a CR2032 coin-cell battery that holds **$225$ drops of battery energy**. During a school day, your calculator uses **$0.65$ energy drops per hour** for **$2$ hours** of math class, and sips just **$0.0025$ energy drops per hour** for the other **$22$ hours** while sleeping:

$$\text{School Days} = \text{Total Energy Drops} \div (\text{Awake Drops} + \text{Sleeping Drops}) = 225 \div ((0.65 \times 2) + (0.0025 \times 22)) \approx 166.05\text{ days}$$

Watch how we solve this two-team battery story on the stack without any parentheses:
1. First multiply the **Awake Team**: `0.65 [ENTER] 2 [×]` puts **`1.30`** awake drops on Shelf $X$.
2. Next multiply the **Sleeping Team**: `0.0025 [ENTER] 22 [×]` puts **`0.055`** sleeping drops on Shelf $X$ while `1.30` waits safely on Shelf $Y$, and tapping **`[+]`** adds them into **`1.355`** energy drops per day.
3. Finally, type `225` onto Shelf $X$ (lifting `1.355` onto Shelf $Y$), tap the **`[x⇄y]` (Swap)** key so `225` trades places into Shelf $Y$ and `1.355` sits in Shelf $X$, and tap **`[÷]`** (`0.65 [ENTER] 2 [×] 0.0025 [ENTER] 22 [×] [+] 225 [x⇄y] [÷]` $\rightarrow$ **`166.051660517`**) to discover that one tiny battery lasts **`166.05` school days**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0.65 [ENTER]` | 0 | 0 | $0.6500$ | $0.6500$ | Awake energy rate ($0.65\text{ energy drops/hr}$) placed into Register $Y$ |
| `2 [×]` | 0 | 0 | 0 | $1.3000$ | Awake energy drops: $0.65 \times 2 = 1.30\text{ energy drops}$ in Register $X$ |
| `0.0025 [ENTER]` | 0 | $1.3000$ | $0.0025$ | $0.0025$ | Sleeping energy rate ($0.0025\text{ energy drops/hr}$) entered; awake drops lift to $Z$ |
| `22 [×]` | 0 | 0 | $1.3000$ | $0.0550$ | Sleeping energy drops: $0.0025 \times 22 = 0.055\text{ energy drops}$ in $X$; awake drops drop to $Y$ |
| `[+]` | 0 | 0 | 0 | $1.3550$ | Total daily energy drops: $1.30 + 0.055 = 1.355\text{ energy drops/day}$ |
| `225 [x⇄y]` | 0 | 0 | $225.0000$ | $1.3550$ | Enter $225\text{ total energy drops}$ and swap: 225 in $Y$, daily drops in $X$ |
| `[÷]` | 0 | 0 | 0 | $166.0517$ | Divide total energy drops by daily drops: $\approx 166.05\text{ school days}$ of power |

### 1.3.6 Quick Care & Everyday Rescues

- **Waking a Sleeping Screen:** Tap **`[C]`** once in a well-lit room and the screen wakes up in an instant with all your stack numbers still in place.
- **Returning to Normal Numbers from a Visual Mode:** If your screen is showing ten-frames (`[▦]`), clock hands (`[🕒]`), or a number line (`[f] [LINE]`), tap **`[C]`** once (or tap the active mode button again) to switch right back to regular numbers.
- **Adjusting Screen Contrast:** If you want the numbers darker or lighter for your room lighting, press `[g] [FLAGS]`, press `[7]`, tap `[+]` (darker) or `[-]` (lighter), and press `[ENTER]`.
- **Starting Fresh Before a Quiz (Factory Clean Reset):** If a teacher wants to clear all saved registers and quiz scores before a class challenge, hold `[C]` down firmly, tap `[g] [OFF]`, and release to reset the memory.
- **Adult Battery Replacement:** When the tiny battery icon appears in the top-right corner of the screen, an adult should use a coin and small screwdriver to open the child-safe rear battery door and put in a fresh CR2032 coin cell (`+` side facing up).

> **COIN CELL BATTERY INGESTION HAZARD (REESE'S LAW / 16 CFR PART 1263):** This instrument operates on a **CR2032 3.0V lithium coin cell battery**. **DEATH or serious injury can occur if ingested.** A swallowed button or coin cell battery can cause **Internal Chemical Burns in as little as 2 hours**. **KEEP new and used batteries OUT OF REACH of children.** Battery replacement must be performed exclusively by an adult, ensuring the retention fastener is securely tightened. Seek immediate medical attention if a battery is suspected to be swallowed or inserted inside any part of the body (U.S. National Battery Ingestion Hotline: **1-800-498-8666**).

---

## 1.4 Where to Go Next: Companion Workbook Quests & Kitchen-Table Challenges

Ready to put your hardware and blocks to the test? Flip open the **[Big Ideas Math Middle School Supplement](../curriculum/big-ideas-middle-school-sc6-workbook.md) — Front Matter (How to Use Your SC-6 & Math Blocks) & Unit 1, Sections 1.1–1.3**, along with your **StackCalc Student Workbook & 12-Unit Curriculum Guide** (Unit 1: *Tactile Foundations & The 4-Level Stack*), or try these three five-minute challenges at your kitchen table tonight:

1. **Hands-On Explorer — The 84 mm Height Parity & 3-Tile Ramp Test:** First, stack **12 Counting Tiles** ($12 \times 7.0\text{ mm} = 84.0\text{ mm}$) beside your **1-Whole Fraction Tower** ($84.0\text{ mm}$) and verify on your SC-6 (`12 [ENTER] 7 [×]` $\to \mathbf{84}$) that their tops sit flush. Then stack **3 Counting Tiles** ($3 \times 7.0\text{ mm} = 21.0\text{ mm}$) right behind the top edge of your SC-6 while it rests in its $15^\circ$ easel stand to feel the **`21.43` mm** lift you calculated for the reading stand above.
2. **Bet Your Family! — The "No-Look" Snap-Dome Count:** Close your eyes, tap `1` `[g] [REP]`, and click `[+]` rhythmically while counting only by the feel and sound of the $400\text{g}$ stainless-steel snap-domes under your thumb. Stop when you think you've reached `15`, open your eyes, and see if your thumb's click-counter matched the stack!
3. **Big Ideas Supplement & Quest Scoreboard Challenge:** Open the **[Big Ideas Math Middle School Supplement](../curriculum/big-ideas-middle-school-sc6-workbook.md) (Front Matter & Unit 1, Sections 1.1–1.3)** and set up your **Quest Scoreboard** pegboard. Place your first `+10` token by building the physical block model, stack a second `+10` token by verifying on the SC-6 stack, and then tap `[f] [?]` to run a 60-second **Level 1 Warm-Up Sprint**.

---

## 1.5 Chapter Summary & Looking Ahead

The physical design of the StackCalc SC-6 and its companion blocks rests on five core elements:
1. **The 4-Level Number Stack ($T, Z, Y, X$) & Big `[ENTER]` Key:** Placing numbers onto visible shelves first and combining them immediately without needing an `=` key or parentheses.
2. **The Daylight Screen & 400g Tactile Keys:** Reading numbers comfortably under natural room light while feeling each button click crisply under your thumb.
3. **Shift Key Operations (`[f]` and `[g]`):** Accessing up to three operations per button while keeping the keypad clean and uncluttered.
4. **The Nine 3D-Printed Manipulative Studios:** Pairing physical Ten-Frames (`[▦]`), the Number Rack (`[g] [COUNT]`), Place Value blocks (`[PV]`), 84 mm Fraction Towers, Prime Factor blocks (`[g] [FACT]`), the Geared Clock (`[🕒]`), and Polyhedral Dice (`[🎲]`) with the live stack.
5. **The $15^\circ$ Sliding Desk Stand & Instant-On Memory:** Docking the protective cover into a hands-free reading stand while preserving every stack shelf and quiz streak in continuous memory.

Now that your desk studio is set up and you have tried your first moves on the stack, turn the page to **[Chapter 02: How Stack Math Works](sc6/02-rpn-for-young-learners.md)**—where you will unlock the full 4-story Number Elevator and see why stacking numbers beats parenthetical confusion every time.

---

# Chapter 2: How Stack Math Works: Stacking Numbers Just Like Blocks

## 2.1 The Equals-Sign Trap vs. The 4-Story Number Elevator

In the Preface and Chapter 1, you met the bottom two shelves of your **StackCalc SC-6**—**Ground Shelf $X$** and **Waiting Shelf $Y$**—and tried your first stack additions. You saw how typing a number, pressing `[ENTER]` to slide it onto Waiting Shelf $Y$, and tapping `[+]` snaps two numbers together just like physical blocks on your desk.

Now a bigger question awaits: what happens when a real-world math puzzle has *two* or *three* parts happening at once—like buying 3 warm pretzels at $\$4$ AND 2 smoothies at $\$5$, or solving a multi-step challenge like $(15 - 3) \times (4 + 2) \div 6$?

In this chapter, you will unlock the **full 4-story Number Elevator ($X, Y, Z, T$)** tucked inside your calculator. To see why a four-shelf elevator makes multi-step math so much easier than a regular calculator, let's first look at a sneaky habit that trips up almost every student in elementary school.

Have you ever wondered why school worksheets always put an equals sign (`=`) at the end of a problem like $4 + 3 = \underline{\hspace{0.5cm}}$?

After a few years of filling in those blanks, it is easy to fall into the **Equals-Sign Trap**. When you see an equals sign at the end of every line, you might start believing that `=` means *"do the math right now and write the answer here."*

Then one day, a teacher writes an open puzzle on the board with the box in the middle—just as cognitive researchers Karen Falkner, Thomas Carpenter, and Elizabeth Fennema tested across elementary classrooms *([Falkner et al., 1999](sc6/appendix-c-formulas-and-conversions.md#cite-falkner1999))*:
$$8 + 4 = \Box + 5 \quad \text{or} \quad 5 + \Box = 12$$
In the landmark study, the vast majority of students wrote $12$ or $17$ in the box. Why? Because their eyes darted across the numbers and the `+` sign, and their fingers immediately added everything in sight. They didn't read the equation as two side-by-side **Counting & Array Studio** block towers that must stand flush at the exact same height—they treated the equals sign as an emergency "compute now" button *([Falkner et al., 1999](sc6/appendix-c-formulas-and-conversions.md#cite-falkner1999))*.

Now think about what **you** do in the real world when you build with physical blocks:
Suppose you have **5 blue blocks** resting on your desk, and your friend hands you **3 red blocks**. How do you put them together?
You don't wave a magic wand and shout *"Equals!"* You simply slide the 3 red blocks straight into the 5 blue blocks. **Putting them together IS the answer (`8`).**

Here is the secret of **Stack Math**: **your brain doesn't think in parentheses and equals signs—your brain naturally stacks physical objects.**
- When you pack your backpack, you place your heavy binder on the bottom shelf, then stack your lunchbox on top.
- When you bake cookies, you weigh the flour into the bowl, crack an egg on top, and stir them together.
- When you stack blocks, pancakes, or books, each new item rests on top of the stack.

That is how **Stack Math** works on your **StackCalc SC-6**:
1. Type the first number (`5`) and press `[ENTER]` to push it onto the waiting shelf (Level $Y$).
2. Type the second number (`3`) on the ground shelf (Level $X$).
3. Tap `[+]`—and *SNAP!* The upper shelf drops down, fusing the two numbers into `8` right before your eyes.

Instead of wrestling with parentheses, syntax errors, and misleading equals signs, on the SC-6 you keep a clear, visible stack of numbers that you can combine, separate, and inspect at any time. Over the next few pages, you will meet the everyday controls that drive this number elevator: the digit keys `[0]` through `[9]` for building numbers on the ground floor, `[ENTER]` to lift a finished number upstairs, the four arithmetic action keys (`[+]` to combine, `[-]` to remove, `[×]` to scale equal groups, and `[÷]` to share equally), and a set of friendly rescue and navigation keys—`[C]` (Clear), `[<-]` (Backspace), `[x⇄y]` (Swap), `[f] [R↓]` (Roll Down), `[g] [REP]` (Repeat Operation), `[f] [LASTX]` (Recover Last Number), and `[g] [FLAGS]` (for switching between a simple 2-shelf view and the full 4-shelf view)—before we open the visual sandboxes (`[▦]` Ten-Frame, `[g] [COUNT]` Bead Rack, `[f] [LINE]` Number Line, and `[PV]` Place Value) in Chapter 3.

---

## 2.2 Unlocking the 4-Story Number Elevator ($T, Z, Y, X$)

When you only have two numbers to combine, Ground Shelf $X$ and Waiting Shelf $Y$ are all you need. But what if you finish calculating the first half of a problem—say, $15 - 3 = 12$—and you need a safe place to park that `12` while you work on the second half ($4 + 2 = 6$)?

Instead of making you copy `12` onto scrap paper or wrap everything in parentheses, your SC-6 has **two more waiting floors upstairs**—**Floor $Z$ (the Third-Floor Loft)** and **Floor $T$ (the Top-Floor Penthouse)**:

![Number Rack Two-Color Bead Math Rekenrek](../assets/manuals/number_rack_subitizing.png)
*Figure 2.1: The Number Rack (Rekenrek) model. Intermediate numbers rest on visible horizontal levels just as numbers wait on the operational shelves of the SC-6.*

| Stack Level | Stack Register | What It Does | Where You See It |
|---|---|---|---|
| **Level 4** | **Register T** | **Top Shelf** (Keeps your multiplier locked for skip-counting) | Top line on screen |
| **Level 3** | **Register Z** | **Third Shelf** (Waiting shelf for multi-step problems) | Second line from top |
| **Level 2** | **Register Y** | **Second Shelf** (Waiting partner, held for subtraction or division) | Left column in $Y \mid X$ layout |
| **Level 1** | **Register X** | **Ground Shelf** (Active shelf where you type and see results) | Right column / primary LCD line |

### 2.2.1 The Three Golden Rules of Stack Math

1. **Rule 1: New Numbers Enter at the Ground Shelf (Level $X$).**  
   Whenever you tap digit keys (for example, `[3]`), that number appears on Level $X$. Level $X$ is the active display shelf you see right before your eyes.
2. **Rule 2: Pressing `[ENTER]` Pushes Numbers UP the Stack.**  
   When your first number is entered, tapping `[ENTER]` pushes it up to Level $Y$ (like an elevator rising to the second floor), leaving an identical copy ready on Level $X$ so you can type your next number.
3. **Rule 3: Pressing an Operator Key (`+`, `-`, `×`, `÷`) Drops the Stack Down.**  
   When you tap an operational key such as `[+]`, the upper shelf drops down. The number on Level $Y$ combines with the number on Level $X$, and their combined total remains on the ground shelf ($X$). Meanwhile, any number waiting upstairs on Floor $Z$ rides the elevator down to Floor $Y$, ready for its turn!

| Stack Level | Before Pressing `[+]` | Action During `[+]` | After Pressing `[+]` |
| :--- | :---: | :--- | :---: |
| **Level 2 (`Y`)** | `3` | Drops down to combine with Level 1 | `0` |
| **Level 1 (`X`)** | `4` | Receives $3 + 4$ | **`7`** |

### 2.2.2 Automatic Stack Lift: Why You Never Lose a Finished Answer
One of the friendliest habits of your SC-6 is **automatic stack lift**. Suppose you just added `4 [ENTER] 5 [+]` and your answer `9` is sitting on Ground Shelf $X$. What happens when you start typing a new number, like `[6]`?

You do **NOT** need to press `[ENTER]` first, and typing `[6]` will **never** erase your `9`! Because the calculator knows `9` is a finished answer, the moment you touch `[6]`, it automatically lifts `9` up to Waiting Shelf $Y$ (and pushes anything in $Y$ up to $Z$) to make room for your `6` on the ground floor:

**Watching Automatic Stack Lift in Action** (After `4 [ENTER] 5 [+]` gives $X = 9$, then typing `[6]`):

| Register | BEFORE Typing `6` | DURING Typing `6` | AFTER Typing `6` |
| :---: | :---: | :---: | :---: |
| **Register T** | $0$ | $0$ | $0$ |
| **Register Z** | $0$ | $0$ | $0$ |
| **Register Y** | $0$ | **$9$** (Lifts up) | **$9$** |
| **Register X** | **$9$** (Prior answer) | `6_` | **$6$** |

### 2.2.3 How the Elevator Drops (and the Top-Shelf Secret)
Whenever you press a two-number action key (`+`, `-`, `×`, `÷`), the whole four-story elevator moves together in one smooth step:
1. The waiting number on **Shelf $Y$** combines with the active number on **Shelf $X$**—for example, in subtraction or division, Shelf $Y$ always goes first: $\text{Shelf } Y - \text{Shelf } X$ ($12 - 5 = 7$) or $\text{Shelf } Y \div \text{Shelf } X$ ($12 \div 4 = 3$).
2. Their combined answer lands on **Ground Shelf $X$**.
3. Whatever was waiting on **Floor $Z$** drops down into **Shelf $Y$**.
4. Whatever was on **Top Shelf $T$** drops down into **Floor $Z$**—and **leaves a copy of itself behind on Top Shelf $T$!**

Why does Top Shelf $T$ leave a copy of itself behind every time the elevator drops? Because if you lock a step size (like `7`) into the top floor, it will keep feeding fresh `7`s down the elevator forever, letting you skip-count through your times tables ($7, 14, 21, 28 \dots$) with single taps of `[+]`!

### 2.2.4 Riding the Sky-Tower Space Elevator Express
To see how automatic stack lift and the four elevator shelves work together in real life, imagine you are the chief dispatch controller for a 20-story Sky-Tower & Robotics Center! On your morning shift, you track heavy cargo lifts, ride a doubling cascade of laser scanners, chain three-stop passenger shuttles using automatic stack lift, and equip robot pit crews at the summit.

Your shift begins at the ground-floor loading dock, where a heavy cargo lift starts upward carrying $83\text{ kg}$ of robot frame parts. At Floor 4, the build team unloads $36\text{ kg}$ of aluminum beams, and the control console asks how many kilograms of parts stay inside the lift as it continues upward. On your **Place Value Tray**, unbundle 1 ten from the `TENS` column into ten `+1` regrouping blocks in the `ONES` column (making 7 tens and 13 ones), then remove 3 tens and 6 ones to leave 4 tens and 7 ones ($47$). When you place the starting $83\text{ kg}$ load on Shelf $Y$ and subtract the $36\text{ kg}$ unloaded at Floor 4 by pressing `83 [ENTER] 36 [-]`, the ground shelf immediately shows **`47`** kg of cargo remaining inside the lift—and tapping `[f] [LASTX] [+]` right afterwards loads the $36\text{ kg}$ of aluminum beams back on to verify $47 + 36 = 83$.

While the cargo lift climbs slowly with its $47\text{ kg}$ load, you switch your monitor to the express turbo-lift shaft next door, where a laser safety scanner **doubles** its active beams on every floor rise. Starting with $2$ laser beams at Floor 1, how many beams are scanning by Floor 5? Typing `2 + 2`, then `+ 4`, then `+ 8`, then `+ 16` on a regular calculator would be slow and tiring—but on your SC-6, pressing `[ENTER]` automatically makes an identical twin copy of whatever number sits on Shelf $X$! That means tapping `[ENTER] [+]` doubles *any* number in two quick clicks. Place 2 tiles on your desk, double them to 4, then 8, then 16, and ride the two-key doubling rhythm (`[ENTER] [+]`) four times in a row on your SC-6: pressing `2 [ENTER] [+] [ENTER] [+] [ENTER] [+] [ENTER] [+]` clones and fuses each floor's beam count until Ground Shelf $X$ reaches **`32`** laser beams at Floor 5.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `2` | 0 | 0 | 0 | 2 |
| `[ENTER] [+]` | 0 | 0 | 0 | 4 |
| `[ENTER] [+]` | 0 | 0 | 0 | 8 |
| `[ENTER] [+]` | 0 | 0 | 0 | 16 |
| `[ENTER] [+]` | 0 | 0 | 0 | 32 |

With the laser grid verified up to 32 beams, the morning science-fair rush begins! The passenger sky-shuttle picks up 15 passengers at the underground train station, 24 passengers at the main atrium, and 31 passengers at the botanical sky-deck. How do you add three stops in a row—and why do you only press `[ENTER]` **once** at the very beginning? First, spot a neat mental-math pattern in the ones digits: $5 + 4 + 1 = 10$. Now watch **automatic stack lift** do the heavy lifting after the first addition: once `15 [ENTER] 24 [+]` produces `39` on Shelf $X$, typing `31` automatically lifts `39` up to Shelf $Y$ without needing another `[ENTER]`. Keying in `15 [ENTER] 24 [+] 31 [+]` chains all three boarding stops into a single smooth tally of **`70`** passengers.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `15` | 0 | 0 | 0 | 15 |
| `[ENTER]` | 0 | 0 | 15 | 15 |
| `24` | 0 | 0 | 15 | 24 |
| `[+]` | 0 | 0 | 0 | 39 |
| `31` | 0 | 0 | 39 | 31 |
| `[+]` | 0 | 0 | 0 | 70 |

When that 70-passenger shuttle reaches the top-floor robotics arena, the tournament director opens a crate of 24 walkie-talkies and splits them equally among 4 pit-crew stations. To see how many walkie-talkies each pit crew gets, deal your 24 counting tiles into 4 equal piles on your desk: you see 6 tiles in each pile, proving with your hands that division is just multiplication (`4 × 6 = 24`) run in reverse. Just like subtraction, the starting total (`24`) goes into the left column ($Y$) and the number of groups (`4`) goes into the right column ($X$), so pressing `24 [ENTER] 4 [÷]` divides the crate evenly to show **`6`** walkie-talkies per pit crew. *(Tap `[f] [LASTX] [×]` right after to multiply `6` by `4` and restore all `24` radios without re-typing!)*

---

## 2.3 Why Combining Numbers IS the Answer (Zero Parentheses)

> **The Golden Rule of RPN:** On the StackCalc SC-6, you never wait for an equals sign. The moment you press `[+]`, `[-]`, `[×]`, or `[÷]`, the numbers on Level 1 ($X$) and Level 2 ($Y$) combine immediately.

To see how the four-story elevator rescues you from parentheses, imagine you are helping organize snacks for a 5th-grade field day and encounter a multi-step puzzle with two separate groups that need to be multiplied and then shared equally:

$$(15 - 3) \times (4 + 2) \div 6 = 12$$

On a regular calculator, you would have to type opening and closing parentheses around $(15 - 3)$ and $(4 + 2)$—or stop halfway through to scribble $12$ on a scrap of paper so you don't forget it while adding $4 + 2$. On your SC-6, the elevator shelves hold your place automatically. First, you find the size of the first group ($15 - 3$) by tapping `15 [ENTER] 3 [-]`, and **`12`** immediately appears on Ground Shelf $X$. Next, without clearing the screen or reaching for a pencil, you start typing the second group ($4 + 2$): as soon as you tap `4 [ENTER] 2 [+]`, automatic stack lift carries your finished **`12`** upstairs to the third-floor loft ($Z$) while `4` and `2` sit on the lower shelves, and tapping `[+]` fuses $4 + 2$ into **`6`** on Level 1 ($X$) as **`12`** rides back down to Level 2 ($Y$) right beside it! Now both finished groups (`12` and `6`) are sitting side by side on your screen, ready to combine: one tap of `[×]` multiplies those two groups into `72`, and tapping `6` `[÷]` splits `72` into 6 equal shares to reveal **`12`**.

When you string the entire sequence together from left to right—pressing `15 [ENTER] 3 [-] 4 [ENTER] 2 [+] [×] 6 [÷]`—the four-story elevator carries both intermediate groups and lands squarely on **`12`**.

| Keystroke | Register T (Roof Floor) | Register Z (Loft Floor) | Register Y (Mezzanine) | Register X (Ground Flr) |
| :--- | :--- | :--- | :--- | :--- |
| `15` | 0 | 0 | 0 | 15 |
| `[ENTER]` | 0 | 0 | 15 | 15 |
| `3` | 0 | 0 | 15 | 3 |
| `[-]` | 0 | 0 | 0 | 12 |
| `4` | 0 | 0 | 12 | 4 |
| `[ENTER]` | 0 | 12 | 4 | 4 |
| `2` | 0 | 12 | 4 | 2 |
| `[+]` | 0 | 0 | 12 | 6 |
| `[×]` | 0 | 0 | 0 | 72 |
| `6` | 0 | 0 | 72 | 6 |
| `[÷]` | 0 | 0 | 0 | 12 |

![SC-6 Parenthesis-Free Order of Operations: (15 - 3) x (4 + 2) / 6 = 12](../assets/manuals/screenshots/sc6_order_of_operations.png)

---

## 2.4 Five Core Stack Techniques: A Quick Preview

Throughout this book, five core techniques connect your 3D-printed math blocks (Ten-Frame Trays, Number Rack, Counting Tiles, and 84 mm Fraction Towers) directly to the 4-level stack:
- **1. The Make-a-Ten Snap (`[▦]`):** Bridging across 10 on your Ten-Frame tray before chaining addition (Chapter 3).
- **2. The Elevator Stack Drop (`[ENTER]`, `[+]`, `[-]`, `[×]`, `[÷]`):** Letting intermediate subtotals ride upstairs to Floors $Y, Z, T$ and drop down on cue with zero parentheses.
- **3. The Remainder-You-Can-Hold (`[g] [÷R]`):** Splitting division into a whole Quotient in $X$ and a physical Remainder in $Y$ at the same time (in our Weekend Maker Fair adventure below and in Chapter 4).
- **4. The Equal-Fraction Tower Alignment (`[g] [SIMP]`):** Aligning $84\text{ mm}$ Fraction Towers flush in the comparator well while reducing factors step by step (Chapter 5).
- **5. The Skip-Counting Ladder (`[g] [REP]`):** Locking a constant step into Floor $T$ so rhythmic taps of `[+]` or `[×]` climb times tables automatically (Chapter 4).

Let's look inside the screen and keypad to see how the horizontal $Y \mid X$ split display and stack controls work.

---

## 2.5 Horizontal $Y \mid X$ Split Screen vs. Vertical Stack

When you first learn mathematics in elementary school, you learn to read and write equations from left to right (like $12 - 4 = 8$ or $12 \div 4 = 3$). Traditional RPN calculators display registers vertically ($Y$ above $X$), which can feel upside-down at first.

The SC-6 graphic LCD introduces the **Horizontal $Y \mid X$ Split Screen Layout**:

**↰ ↱ FRAC                   Y                X              [BATTERY]**

| Left Column (`Y` — Waiting Number) | Center Divider | Right Column (`X` — Active Number) |
| :---: | :---: | :---: |
| **`12`** | Vertical Split Rule | **`4`** |

### 2.5.1 The Enter-Slide Animation
1. **Typing Your First Number:** When you key `12`, it appears in the **Right ($X$)** column.
2. **Pressing `[ENTER]`:** The digits `12` visually slide smoothly across the LCD from the right column into the **Left ($Y$)** column. You see: *"My 12 has moved into position on the left, waiting for math."*
3. **Typing Your Second Number:** When you key `4`, it enters the **Right ($X$)** column. The display clearly presents `Y = 12` and `X = 4`.
4. **Pressing an Operator (`[-]` or `[÷]`):**
   - The operator symbol briefly flashes in the center vertical divider line.
   - The calculator combines Shelf $Y$ on the left with Shelf $X$ on the right ($12 - 4 = 8$ or $12 \div 4 = 3$).
   - The result appears in the right column ($X$), while the stack drops.

### 2.5.2 Customizing Your Screen View: Side-by-Side ($Y \mid X$) vs. Single Number ($X$)
Everyone's eyes work a little differently when learning a new skill. Using the `[g] [FLAGS]` menu (Flag 5), you can choose how your SC-6 displays the bottom shelves of your stack:
- **Side-by-Side View (Flag 5 = 0, Default — Dual Stack $Y \mid X$):** Shows both your waiting number on the left ($Y$) and your active number on the right ($X$) at the exact same time. Seeing both numbers side by side makes subtraction ($Y - X$) and division ($Y \div X$) feel just like reading from left to right across a page.
- **Big Single-Number View (Flag 5 = 1 — Single Stack $X$ Only):** Fills the screen with one extra-large, bold number ($X$). When you press `[ENTER]`, your first number still rides up to Shelf $Y$ in the background while your screen stays clean and simple for typing the next number.

![Math Dominoes Studio Doubling and Pairing](../assets/manuals/math_dominoes_pairing.png)
*Figure 2.2: The Math Dominoes Studio. Domino pips let you spot groups at a glance and build pairs that mirror RPN two-number operations.*

![Math Dominoes Studio: Bridging 10 on the 12-Frame Tray ([5|4] = 9 + [3|2] = 5 = 10 + 4 = 14)](../assets/manuals/math_dominoes_bridging_12frame.png)
*Figure 2.3: Bridging 10 on the 12-frame tray. Placing [5|4] = 9 and [3|2] = 5 across the 10-break line physically regroups 9 + 5 into 10 + 4 = 14.*

### 2.5.3 The Adventure Playground Construction Crew: Seeing $Y \mid X$ Side by Side
To feel how natural that left-to-right $Y \mid X$ split screen is in action, step into the boots of the **Adventure Playground Construction Crew**! Your school is building an adventure playground complete with a two-bay swing set, a cedar perimeter fence, a giant spiral slide, and a monkey-bar climbing dome. As the project engineers, your crew walks from zone to zone laying shock-absorbing bounce tiles, setting fence posts, paving pathways, and weighing cedar woodchips—using your desk blocks and the horizontal $Y \mid X$ screen to verify every build step.

Your first stop is the two-bay swing set, where your crew is laying interlocking rubber bounce tiles under the swings. You unload 5 blue tiles in the morning, and the delivery truck brings 3 green tiles in the afternoon. How many bounce tiles are ready to snap into place? Place 5 blue counting tiles on the left side of your desk, and 3 green tiles on the right, then slide them together into one solid row of 8 tiles. Notice how your calculator's horizontal $Y \mid X$ screen mirrors your desk: pressing `[ENTER]` slides your morning count (`5`) into the left column ($Y = 5$) so the afternoon delivery (`3`) can sit right beside it ($X = 3$). When you key in `5 [ENTER] 3 [+]`, the waiting shelf and ground shelf snap together to display **`8`** bounce tiles ready for the swing bay. Pause for a moment and glance at the screen: did you see $Y = 5$ on the left and $X = 3$ on the right before pressing `[+]`? If your screen showed $53$ instead, your fingers simply forgot to press `[ENTER]` to close the elevator door between the two numbers!

Once the swing bay is cushioned with all 8 rubber tiles, your crew walks over to the playground border to anchor 9 sturdy cedar fence posts along the property line. Before the lunch bell rings, you finish bolting 4 posts firmly into the ground, and your foreman asks how many fence posts are still waiting for the afternoon shift. To see the answer with your hands, line up 9 counting tiles in a row for the fence line, then slide 4 tiles away for the finished posts to leave 5 remaining. In Stack Math, subtraction follows that exact same left-to-right story: your **starting total ($9$)** always goes into the left column ($Y$) first, and the **amount you take away ($4$)** goes into the right column ($X$). By pressing `9 [ENTER] 4 [-]`, you subtract the 4 bolted posts from the 9 starting posts and leave **`5`** unbolted posts on the ground floor for the afternoon shift.

What if your fingers accidentally typed `4 [ENTER] 9` in reverse order while setting up that fence-post subtraction? Look at the split screen before pressing minus: $Y$ holds $4$ and $X$ holds $9$. On the SC-6, you never have to erase and re-type! Simply tap `[x⇄y]` to swap the two shelves into their proper seats ($Y = 9,\; X = 4$), then tap `[-]` to get $5$. Better yet, right after subtracting, tap `[f] [LASTX] [+]` to bring back the $4$ finished posts and prove that $5 + 4 = 9$.

After lunch, your crew moves from the perimeter fence to the center of the playground to pave the landing zone around the giant spiral slide using 23 rubber pavers, plus another 14 pavers around the balance-beam pit. Now that the numbers have grown into the twenties and teens, you can watch the tens and ones combine on your **Place Value Studio Whole Numbers Tray** before you even press `[+]`. Dock `2` in `TENS` and `3` in `ONES` for the top row ($23$), and `1` in `TENS` and `4` in `ONES` for the bottom row ($14$). Just like Registers $Y$ and $X$, the two rows of your tray let you combine the tens column ($20 + 10 = 30$) and the ones column ($3 + 4 = 7$) to see $37$ at a glance. Now lift the 23 spiral-slide pavers onto Shelf $Y$ and bring in the 14 balance-beam pavers by pressing `23 [ENTER] 14 [+]`, which unites both paving zones into **`37`** on Ground Shelf $X$. *(Try tapping `[f] [LASTX] [-]` right after—watch `14` jump back into $X$ and subtract to restore `23`!)*

With the spiral-slide pathway paved, your crew tackles the final job on the playground: wheeling soft cedar woodchips beneath the monkey-bar dome. The first wheelbarrow delivers $47\text{ kg}$ of woodchips, and the second brings $36\text{ kg}$. Unlike the pavers around the spiral slide, here the ones digits ($7 + 6 = 13$) overflow past 10! When you model 47 (`4` tens, `7` ones) and 36 (`3` tens, `6` ones) on your **Place Value Tray** with `+1` regrouping blocks, the $7 + 6 = 13$ ones trade 10-for-1 to add $+1$ to the `TENS` column and leave `3` in `ONES`, giving 8 tens and 3 ones ($83$). To combine both wheelbarrows on the stack and immediately verify the sum by subtracting the second load back out without re-typing a single digit, press `47 [ENTER] 36 [+]`, which reaches $83\text{ kg}$ and then uses `[f] [LASTX]` to restore the original **`83`** kg on Ground Shelf $X$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `47` | 0 | 0 | 0 | 47 |
| `[ENTER]` | 0 | 0 | 47 | 47 |
| `36` | 0 | 0 | 47 | 36 |
| `[+]` | 0 | 0 | 0 | 83 |
| `[f] [LASTX]` | 0 | 0 | 83 | 36 |
| `[-]` | 0 | 0 | 0 | 47 |

Look at row 5 of that table to see why `[f] [LASTX]` saves every keystroke: you didn't have to type `3` and `6` a second time! Tapping `[f] [LASTX]` pulled `36` straight out of backup memory and lifted `83` to Floor $Y$, so one tap of `[-]` proved $83 - 36 = 47$.

---

## 2.6 Choosing How Many Shelves You Need: `2-LV`, `4-LV`, and `8-LV`

Just as you might use a small two-pocket folder for a quick homework sheet or a big four-shelf locker for all your school projects, the `[g] [FLAGS]` menu lets you choose how many shelves your Number Elevator uses:

- **2-Shelf Mode ($X, Y$ — `2-LV`):** Uses just two shelves—Waiting Shelf $Y$ and Ground Shelf $X$. Because Shelf $Y$ is the top shelf in this mode, whatever number sits on Shelf $Y$ stays locked there like a permanent step-counter! That makes `2-LV` wonderful for early explorers practicing single-step addition, subtraction, and Ten-Frame games.
- **4-Shelf Mode ($X, Y, Z, T$ — `4-LV` Standard):** The classic four-story Number Elevator—Ground ($X$), Mezzanine ($Y$), Loft ($Z$), and Penthouse Roof ($T$). This is your everyday mode for 3rd–6th grade adventures: multi-step word problems, whole-number division with remainders (`[g] [÷R]`), fractions, and parenthesis-free order of operations.
- **8-Shelf Mode (8 Stories Deep — `8-LV`):** Expands the elevator to 8 full waiting shelves for long tournament mental-math relays where you want to stack half a dozen subtotals without touching scratch paper.

### 2.6.1 A Fun Discovery: How a Step Counter Works in 2-Shelf vs. 4-Shelf Mode
One of the first experiments kids try on a calculator is building an automatic step counter: typing `1 [ENTER] 1 [+]` and tapping `[+]` over and over to watch the screen climb $2, 3, 4, 5 \dots$

Try it in **4-Shelf Mode (`4-LV`)** first: after `1 [ENTER] 1 [+]` gives `2`, what happens if you tap `[+]` again? The screen stays at `2`! Why? Because in 4-Shelf mode, the elevator dropped `0` down from Floor $Z$ into Shelf $Y$, so tapping `[+]` simply added $2 + 0 = 2$. To make a 4-shelf elevator count forever, you first press Constant Repeat (`1 [g] [REP]`), which fills all four shelves ($T, Z, Y, X$) with `1` so the Penthouse roof keeps feeding fresh `1`s down the stack!

In **2-Shelf Mode (`2-LV`)**, however, Shelf $Y$ *is* the roof of the building. So when `+` drops the stack, Shelf $Y$ automatically keeps its `1` forever:
`1 [ENTER] 1 [+]` $\implies \mathbf{2}$, `[+]` $\implies \mathbf{3}$, `[+]` $\implies \mathbf{4}$, `[+]` $\implies \mathbf{5}$!

---

## 2.7 Moving Numbers Around on Your Stack: `[x⇄y]`, `[f] [R↓]`, `[g] [REP]`, `[f] [LASTX]`

The SC-6 keypad provides dedicated physical keys to move and manage numbers on your stack:

| Keystroke | Operation | Stack Register Effect |
|---|---|---|
| `[x⇄y]` | **Swap $X$ and $Y$** | Exchanges the active input and held number ($X \leftrightarrow Y$). Instantly corrects reversed subtraction or division. |
| `[f] [R↓]` | **Roll Down** | Rotates the 4-level stack downward in a carousel: $X \to T,\; T \to Z,\; Z \to Y,\; Y \to X$. |
| `[g] [REP]` | **Stack Replicator** | Copies Register $X$ across all four shelves ($T, Z, Y, X \leftarrow X$) so you can tap `[+]` or `[×]` repeatedly for rhythmic skip-counting and constant scaling. |
| `[f] [LASTX]` | **Undo & Twin-Calculation Recall** | Recalls the previous $X$ value before the last operation for self-checking inverse math or reusing a number without re-typing. |
| `[g] [SHOW]` | **Full Significant Digits Reveal** | Momentarily displays all internal digits of Register $X$. |

### 2.7.1 Fixing Reversed Entries with Swap (`[x⇄y]`) and Spinning the Stack Carousel (`[f] [R↓]`)
What happens if you type two numbers onto the stack in reverse order during a subtraction or division problem? Suppose you are at the Weekend Maker Fair & Farmer's Market, where the smoothie maker wants to pour a 24-ounce tub of frozen berry mix equally into 8 tasting cups ($24 \div 8 = 3$), and asks you to verify the ounces per cup. In your excitement, your fingers accidentally type the `8` first (`8 [ENTER] 24`)! On a regular calculator, typing a division problem backward means hitting Clear and starting all over. On the SC-6, look at the horizontal split screen: `8` is sitting in $Y$ and `24` is sitting in $X$. One tap of `[x⇄y]` swaps them into their proper seats before you press `[÷]`: when you run `8 [ENTER] 24 [x⇄y] [÷]`, the swap key puts `24` into the left seat ($Y$) and `8` into the right seat ($X$) so division cleanly yields **`3`** ounces per cup.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `8` | 0 | 0 | 0 | 8 |
| `[ENTER]` | 0 | 0 | 8 | 8 |
| `24` | 0 | 0 | 8 | 24 |
| `[x⇄y]` | 0 | 0 | 24 | 8 |
| `[÷]` | 0 | 0 | 0 | 3 |

Never start over when you type numbers in reverse order—just tap `[x⇄y]` and divide!

And what if you have numbers parked on all four floors ($T, Z, Y, X$) and want to inspect every shelf without erasing a single number? Before the first buzzer sounds at the state **Junior Math Olympiad**, the head judge asks every competitor to prove they can inspect all four shelves of their stack. You load `10`, `20`, `30`, and `40` onto the four shelves of your elevator, then spin them around the 4-level carousel using **Roll Down (`[f] [R↓]`)**: when you key in `10 [ENTER] 20 [ENTER] 30 [ENTER] 40 [f] [R↓]`, each tap of `[f] [R↓]` brings the next shelf down to the ground floor until all four numbers return to their starting seats with **`30`** back on Ground Shelf $X$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `10` | 0 | 0 | 0 | 10 |
| `[ENTER]` | 0 | 0 | 10 | 10 |
| `20` | 0 | 0 | 10 | 20 |
| `[ENTER]` | 0 | 10 | 20 | 20 |
| `30` | 0 | 10 | 20 | 30 |
| `[ENTER]` | 10 | 20 | 30 | 30 |
| `40` | 10 | 20 | 30 | 40 |
| `[f] [R↓]` | 40 | 10 | 20 | 30 |
| `[f] [R↓]` | 30 | 40 | 10 | 20 |
| `[f] [R↓]` | 20 | 30 | 40 | 10 |
| `[f] [R↓]` | 10 | 20 | 30 | 40 |

Because there are 4 floors ($T, Z, Y, X$), pressing `[f] [R↓]` 4 times brings every passenger right back to its starting floor!

### 2.7.2 Meet Your Undo & Twin-Calculation Key (`[f] [LASTX]`)
Every time you press an operation key (`[+]`, `[-]`, `[×]`, `[÷]`), where does the number on Floor $X$ go? It doesn't disappear. Your SC-6 automatically tucks a backup copy of that number into a register called **`LAST x`**.

Pressing `[f] [LASTX]` (`[f]` then `[ENTER]`) pulls that number right back onto Floor $X$ while lifting your answer up to Floor $Y$. That gives you three practical advantages without ever re-typing a number:
1. **Two-Tap Self-Check:** Want to prove your subtraction $83 - 36 = 47$ is right? Just tap `[f] [LASTX] [+]`—the calculator brings back `36`, adds it to `47`, and restores `83`. Divided $56 \div 7 = 8$? Tap `[f] [LASTX] [×]` to bring back `7` and restore `56`.
2. **Quick Undo:** Accidentally tapped `[+]` when you meant `[-]`? Don't clear and start over. Tap `[f] [LASTX] [-]` to undo the accidental addition, then tap `[f] [LASTX] [-]` again to perform the subtraction you wanted.
3. **Zero-Retype Twin Calculations:** Whenever a multi-step problem needs the same number twice, `[f] [LASTX]` hands it back to you in a single click so your fingers never waste time typing the same digits twice.

To see `[f] [LASTX]` in action, suppose you stop at the Farmer's Market orchard booth to help the orchard master check an invoice for 15 wooden crates of Honeycrisp apple cider at $\$8.00$ per crate ($15 \times \$8.00 = \$120.00$). How can you prove the $\$120.00$ receipt is $100\%$ accurate without re-typing a single digit? If you model 2 rows of 8 tiles ($16$) on your desk and divide by 8, you see that dividing by the row width always brings back the number of rows. Now multiply the 15 cider crates by $\$8$ and let `[f] [LASTX]` reverse-check the invoice by dividing by `8`: pressing `15 [ENTER] 8 [×] [f] [LASTX] [÷]` computes the $\$120$ invoice and immediately divides by the recalled $\$8$ unit price to restore **`15`** crates on Ground Shelf $X$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `15` | 0 | 0 | 0 | 15 |
| `[ENTER]` | 0 | 0 | 15 | 15 |
| `8` | 0 | 0 | 15 | 8 |
| `[×]` | 0 | 0 | 0 | 120 |
| `[f] [LASTX]` | 0 | 0 | 120 | 8 |
| `[÷]` | 0 | 0 | 0 | 15 |

That same `[f] [LASTX]` rescue also lets you undo a subtraction when plans change! Suppose your school math club opens its $\$120.00$ treasure vault to buy a $\$45.00$ telescope lens (`120 [ENTER] 45 [-]` $\to \$75.00$). Just as you subtract the $\$45.00$, the school principal walks in and announces that a science grant paid for the lens! How do you undo the subtraction and restore your $\$120.00$ balance without typing `45` again? You use `[f] [LASTX]` to pull `45` right back out of memory and tap `[+]`: running the sequence `120 [ENTER] 45 [-] [f] [LASTX] [+]` subtracts the $\$45$ lens and then immediately reunites `$75` on Shelf $Y$ with the recalled `$45` on Shelf $X$ to restore **`120`** dollars.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `120` | 0 | 0 | 0 | 120 |
| `[ENTER]` | 0 | 0 | 120 | 120 |
| `45` | 0 | 0 | 120 | 45 |
| `[-]` | 0 | 0 | 0 | 75 |
| `[f] [LASTX]` | 0 | 0 | 75 | 45 |
| `[+]` | 0 | 0 | 0 | 120 |

With those two final clicks (`[f] [LASTX] [+]`), your club's initial $\$120.00$ vault balance is completely restored without re-typing a single digit.

### 2.7.3 Sharing with Whole Groups and Leftovers (`[g] [÷R]`)
Earlier at the top of the Sky-Tower, 24 walkie-talkies divided into 4 groups with zero leftovers. But what happens at the Weekend Maker Fair & Farmer's Market when numbers *don't* divide evenly?

Your first stop at the market is the brick-oven bakery, where the baker pulls 17 warm sourdough rolls from the oven and packs them into bags of 5 rolls each. How many bags are filled completely, and how many warm rolls are left over for the baker's snack? If you typed $17 \div 5$ on a regular calculator, it would say `3.4`—which doesn't tell you how many loose rolls are sitting on the counter! Instead, deal 17 counting tiles into piles of 5 on your desk: you get **3 full piles of 5** ($15$ tiles) and **2 loose tiles** left over. Now watch **Quotient & Remainder (`[g] [÷R]`)** put the full bags in Register $X$ and the leftover rolls in Register $Y$ at the exact same time: when you key in `17 [ENTER] 5 [g] [÷R]`, `[g] [÷R]` splits the 17 rolls into 3 full bags and 2 leftovers before `[x⇄y]` swaps **`3`** into Ground Shelf $X$ so you can inspect the leftover rolls.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `17` | 0 | 0 | 0 | 17 |
| `[ENTER]` | 0 | 0 | 17 | 17 |
| `5` | 0 | 0 | 17 | 5 |
| `[g] [÷R]` | 0 | 0 | 2 | 3 |
| `[x⇄y]` | 0 | 0 | 3 | 2 |

Notice how Register $X$ first shows Quotient $Q = 3$ full bags while Register $Y$ holds Remainder $R = 2$ loose rolls, and tapping `[x⇄y]` swaps them so you can inspect the 2 leftover rolls up front. *(And if every single roll must go inside a bag, you need $3 + 1 = 4\text{ bags}$.)*

That same whole-number remainder power comes to the rescue right next door at the heritage farm stand, where a basket of 125 blue-shell pasture eggs is being packed into specialty cartons holding 8 eggs each. How many 8-egg cartons are filled completely, and how many eggs remain in the basket? Here again, a decimal like `15.625` would be completely useless—because nobody can pack `0.625` of a raw egg! To split the 125 eggs into 8-egg cartons and check the remainder, press `125 [ENTER] 8 [g] [÷R]`, which first places 15 full cartons in Register $X$ with 5 leftover eggs waiting on Floor $Y$, and then swaps **`15`** into Register $X$. *(Want to prove $15 \times 8 + 5 = 125$ with zero re-typing? Right after `[g] [÷R]`, tap `[f] [LASTX] [×] [+]` and watch `125` reappear!)*

---

## 2.8 Beat Every Adult in the Room! The `1089` Mind-Reading Stack Trick

Want to amaze your parents or friends at the dinner table? Tell them you can read their mind using the SC-6 elevator stack:
1. Write the secret number **`1089`** on a folded slip of paper and hand it to an adult before you start.
2. Ask them to pick *any* 3-digit number where the first and last digits differ by at least 2 (for example, **`732`**).
3. Have them reverse the digits (**`237`**) and subtract the smaller number from the larger on the stack (`732 [ENTER] 237 [-]` $\to$ `495`).
4. Now take that intermediate answer (`495`), reverse its digits (**`594`**), and add them right on the stack: when you run the complete chain by pressing `732 [ENTER] 237 [-] 594 [+]`, the ground shelf immediately lights up with **`1089`**!
5. Tell them to open the folded paper—no matter which 3-digit number they started with, the stack lands on **`1089`** every single time! *(Why it works: subtracting a reversed 3-digit number always produces a multiple of 99 whose hundreds and ones digits add to 9, and adding its reverse gives $900 + 180 + 9 = 1,089$.)*

---

## 2.9 Why Your Brain Loves Stack Math: The PEMDAS Funnel vs. The Inside-Out Stack

Why do you learn math faster and make fewer mistakes with Stack Math? Because your brain only has to think about two numbers at a time.

Consider a classic Grade 6 order-of-operations challenge:
$$40 - 3 \times (2 + 3)^2 \div 5 = 25$$

When students try to solve this on paper or a regular calculator, the **#1 trap** is subtracting $40 - 3 = 37$ first. Why? Because reading left-to-right tempts your eyes to grab $40 - 3$ before noticing that the $3$ is bound by multiplication to $(2 + 3)^2$. Compare the two ways to evaluate this expression:

### 2.9.1 The PEMDAS Paper Funnel (Step-by-Step Rewrite)
On paper, you shrink the expression one line at a time like a funnel (**P**arentheses $\to$ **E**xponents $\to$ **M**ultiply/**D**ivide left-to-right $\to$ **A**dd/**S**ubtract left-to-right):
1. **Parentheses First:** Compute $(2 + 3) = 5$, rewriting the line as $40 - 3 \times 5^2 \div 5$.
2. **Exponents Next:** Build a $5 \times 5$ square of Counting Tiles to see $5^2 = 25$, rewriting as $40 - 3 \times 25 \div 5$.
3. **Multiply & Divide Left-to-Right:** Multiply $3 \times 25 = 75$, then divide $75 \div 5 = 15$, rewriting as $40 - 15$. *(Never subtract $40 - 3$ first.)*
4. **Subtract Last:** $40 - 15 = \mathbf{25}$.

### 2.9.2 Inside-Out RPN Stack Evaluation (Zero Parentheses)
On your SC-6, you never have to rewrite four lines of paper or worry about subtracting $40 - 3$ too early. Because the elevator has four waiting shelves, you can park the outer `40` and `3` safely upstairs on Floors $Z$ and $Y$ while you solve the innermost group $(2 + 3)^2$ right on the ground floor! First you type `40 [ENTER] 3 [ENTER]` to send `40` and `3` upstairs, then you add `2 [ENTER] 3 [+]` to form `5` on Shelf $X$, and tap the square key `[x²]` to turn `5` into `25`. Now the waiting `3` on Shelf $Y$ is ready to multiply (`[×]` $\to 75$), dividing by `5` (`5 [÷]` $\to 15$) brings your parked `40` down into Shelf $Y$, and one final tap of `[-]` subtracts $40 - 15$ to land on **`25`**—all in one continuous chain (`40 [ENTER] 3 [ENTER] 2 [ENTER] 3 [+] [x²] [×] 5 [÷] [-]` $\longrightarrow$ **`25`**):

| What You Are Solving | PEMDAS Paper Funnel | SC-6 Elevator Stack |
| :--- | :--- | :--- |
| **1. Park Outer Numbers & Add `(2 + 3)`** | Rewrite $40 - 3 \times (5)^2 \div 5$ | `40 [ENTER] 3 [ENTER] 2 [ENTER] 3 [+]` $\to$ `5` in $X$ (`3` in $Y$, `40` in $Z$) |
| **2. Square the Group (`5²`)** | Rewrite $40 - 3 \times 25 \div 5$ | Tap `[x²]` $\to$ `25` in $X$ |
| **3. Scale & Divide (`3 × 25 ÷ 5`)** | Rewrite $40 - 75 \div 5 \to 40 - 15$ | Tap `[×] 5 [÷]` $\to$ `15` in $X$ while `40` drops to $Y$ |
| **4. Final Subtraction (`40 - 15`)** | $40 - 15 = \mathbf{25}$ | Tap `[-]` $\to$ **`25`**. |

### 2.9.3 The Clark's Nutcracker's 30,000-Seed Memory Ledger
That same ability to hold a running total in working memory while new quantities arrive shows up in nature, too. High in the alpine forests of the Rocky Mountains, a silver-and-black bird called **Clark's nutcracker** (*Nucifraga columbiana*) performs one of the animal kingdom's most astonishing feats of spatial memory. Every autumn, a single nutcracker harvests up to $30,000$ whitebark pine seeds, buries them in thousands of small underground caches across mountain ridges, and remembers their exact locations nine months later under deep winter snow.

How does a bird track its winter pantry? Like a living stack ledger. Suppose a nutcracker buries **9 pine seeds in each of 12 caches** along a granite ridge, finds **15 extra seeds** under a fallen pine log, and eats **28 seeds** during a January blizzard:
$$\text{Remaining Seeds} = 9 \times 12 + 15 - 28 = 95\text{ seeds}$$

If you build $12$ rows of $9$ Counting Tiles on your desk to represent the $108$ cached seeds, slide in $15$ loose tiles for the bonus find under the log ($123$ seeds in all), and then sweep away $28$ tiles for the January blizzard, you are left with $95$ seeds. On your SC-6, the entire seasonal ledger flows across the ground and mezzanine shelves in 10 keystrokes with zero parentheses—multiplying the 12 caches of 9 seeds first (`9 [ENTER] 12 [×]`), adding the 15 extra seeds (`15 [+]`), and subtracting the 28 eaten seeds (`28 [-]`) to land directly on **`95` seeds**.

### 2.9.4 Beating Parentheses with Floor $Z$: From Market Food Courts to the Math Olympiad
Even in everyday shopping, multi-step math pops up whenever you buy two different items at once. Suppose you stop at the Farmer's Market food court to buy **3 warm pretzel twists at $\$4.00$ each** AND **2 mango smoothies at $\$5.00$ each**. On a basic calculator, typing `3 × 4 + 2 × 5` gives the wrong answer unless you write down the first subtotal or use parentheses. How does the SC-6's **third-floor loft (Register $Z$)** solve the whole bill with zero parentheses and zero scratch paper? Build two tile arrays on your desk: a $3 \times 4$ array ($12$) and a $2 \times 5$ array ($10$). Now watch what happens in row 6 of the stack table below: as soon as you type `2 [ENTER] 5` for the smoothies, your $\$12$ pretzel subtotal rides the elevator up to **Floor $Z$**, waiting safely until the $\$10$ smoothie total finishes on Floor $X$. Pressing `3 [ENTER] 4 [×] 2 [ENTER] 5 [×] [+]` brings both booth subtotals together on the bottom two shelves and combines them into **`22`** dollars in all.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `3` | 0 | 0 | 0 | 3 |
| `[ENTER]` | 0 | 0 | 3 | 3 |
| `4` | 0 | 0 | 3 | 4 |
| `[×]` | 0 | 0 | 0 | 12 |
| `2` | 0 | 0 | 12 | 2 |
| `[ENTER]` | 0 | 12 | 2 | 2 |
| `5` | 0 | 12 | 2 | 5 |
| `[×]` | 0 | 0 | 12 | 10 |
| `[+]` | 0 | 0 | 0 | 22 |

Pause and look at Row 8 of that table: right before you press `[+]`, Floor $Y$ shows your $\$12$ pretzels and Floor $X$ shows your $\$10$ smoothies side by side!

Now that you saw Floor $Z$ hold your pretzel subtotal at the market food court, watch how that exact same Floor $Z$ superpower conquers all four rounds of the state **Junior Math Olympiad** while other teams fumble with nested parentheses!

*BZZZT!* Round 1 flashes on the scoreboard—and our Olympiad warm-up begins with a familiar friend from earlier in the chapter: the two-group expression $(15 - 3) \times (4 + 2) \div 6$. Remember how we walked through all 11 elevator floors of this puzzle when you first met Floor $Z$? Now that your fingers know the pretzel-and-smoothie rhythm from the market food court, you don't even have to pause between steps! You solve the first bracketed group on the ground floor (`15 [ENTER] 3 [-]` $\to 12$), let `12` ride automatically upstairs to Floor $Z$ while you build and add the second group (`4 [ENTER] 2 [+]` $\to 6$), and watch `12` drop right back down to Waiting Shelf $Y$ beside `6` on Ground Shelf $X$. With both bracket answers sitting side by side in plain sight, pressing `15 [ENTER] 3 [-] 4 [ENTER] 2 [+] [×] 6 [÷]` fuses `12` and `6` into `72` on the ground shelf and divides by `6` to lock in **`12`**—all with zero parentheses and zero scratch paper while the other teams are still hunting for their bracket keys!

Hardly has the applause from Round 1 settled when Round 2 lights up the board, testing whether you can divide one bracketed difference by another: $(24 - 8) \div (6 - 2)$. Watch how the first difference ($24 - 8 = 16$) rides upstairs to Floor $Z$, then drops right back into the left seat (Floor $Y$) the moment the second difference ($6 - 2 = 4$) finishes on Floor $X$: keying in `24 [ENTER] 8 [-] 6 [ENTER] 2 [-] [÷]` divides `16` on Shelf $Y$ by `4` on Shelf $X$ to display **`4`**.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `24` | 0 | 0 | 0 | 24 |
| `[ENTER]` | 0 | 0 | 24 | 24 |
| `8` | 0 | 0 | 24 | 8 |
| `[-]` | 0 | 0 | 0 | 16 |
| `6` | 0 | 0 | 16 | 6 |
| `[ENTER]` | 0 | 16 | 6 | 6 |
| `2` | 0 | 16 | 6 | 2 |
| `[-]` | 0 | 0 | 16 | 4 |
| `[÷]` | 0 | 0 | 0 | 4 |

When the final `[÷]` key drops the stack, Ground Shelf $X$ shows `4`—and if you tap `[f] [LASTX] [×]` right after, the calculator multiplies $4 \times 4$ to bring `16` right back!

In Round 3, the judges raise the stakes by combining addition, subtraction, multiplication, and division into one three-branch relay expression: $(18 + 6) \times (10 - 5) \div 12$. Because your hands now know the elevator rhythm—solve the first bracket, solve the second bracket, fuse them, and divide—you can glide through all 11 keystrokes in one continuous flow by pressing `18 [ENTER] 6 [+] 10 [ENTER] 5 [-] [×] 12 [÷]` to reach **`10`**. Trace the three-story choreography in your mind's eye as each parenthesized pair resolves on the shelves: first, `18 [ENTER] 6 [+]` fuses the opening bracket into `24` on Ground Shelf $X$. Next, typing `10` automatically lifts `24` to Shelf $Y$, and pressing `[ENTER]` pushes `24` safely up to the Second Balcony (Floor $Z$) while `10` and `5` settle into $Y$ and $X$. The moment you tap `[-]`, two things happen at once: $10 - 5$ becomes `5` on Ground Shelf $X$, and your waiting `24` rides the elevator back down from Floor $Z$ into Shelf $Y$! Now `24` and `5` sit side by side on $Y$ and $X$, so one tap of `[×]` multiplies them into `120` on the ground shelf, and `12 [÷]` divides `120` by `12` to finish cleanly at `10`.

That brings you to Round 4, the Geometry Lightning Puzzle: a square castle courtyard measures $15\text{ ft} \times 15\text{ ft}$ on the outside, with a central $9\text{ ft} \times 9\text{ ft}$ fountain pool inside. How many square feet of stone paving surround the fountain? Instead of typing `15 [ENTER] 15 [×]`, you reach for the dedicated **Square Key (`[x²]`)** (`[f]` then `[x²]`). Notice how `15 [x²]` turns `15` into `225` right on Shelf $X$, and typing `9` automatically lifts `225` to Shelf $Y$ while you square `9`: pressing `15 [x²] 9 [x²] [-]` subtracts the $81\text{ sq ft}$ fountain from the $225\text{ sq ft}$ courtyard to leave **`144`** square feet of stone paving.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `15` | 0 | 0 | 0 | 15 |
| `[x²]` | 0 | 0 | 0 | 225 |
| `9` | 0 | 0 | 225 | 9 |
| `[x²]` | 0 | 0 | 225 | 81 |
| `[-]` | 0 | 0 | 0 | 144 |

Look at that difference of squares: $225 - 81 = 144$, which is $12^2$! You just discovered the famous $9\text{–}12\text{–}15$ right-triangle family.

### 2.9.5 Parenthesis Traps vs. Inside-Out Elevator Math

Just as cognitive researcher Jerome Bruner showed that learners build lasting understanding by moving from hands-on blocks to visual models to symbols *([Bruner, 1966](sc6/appendix-c-formulas-and-conversions.md#cite-bruner1966))*, evaluating expressions from the inside out on the stack lets your working memory focus on two numbers at a time *([Sweller, 1988](sc6/appendix-c-formulas-and-conversions.md#cite-sweller1988); [Miller, 1956](sc6/appendix-c-formulas-and-conversions.md#cite-miller1956))* without juggling nested parentheses *([Łukasiewicz, 1924](sc6/appendix-c-formulas-and-conversions.md#cite-lukasiewicz1924); [Hamrick, 1980](sc6/appendix-c-formulas-and-conversions.md#cite-hamrick1980))*. Now that you have seen every shelf and control key of the SC-6 in action, compare how a parenthesized multi-step expression is entered on a standard calculator versus inside-out evaluation on the SC-6 stack:

| Challenge / Equation | The Algebraic Calculator Trap (Standard Entry) | The StackCalc SC-6 + Blocks Method | Keystroke Reduction | Live Stack Visibility | Learning Breakthrough |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **5th Grade Order of Operations:** $(15 - 3) \times (4 + 2) \div 6 = 12$ | `( 1 5 - 3 ) * ( 4 + 2 ) / 6 =` (14 keystrokes). *Trap: Missed or misplaced parenthesis computes $15 - 12 + 0.33 = 3.33$ silently. Intermediate results ($12, 6$) are invisible inside hardware buffers.* | **SC-6 Elevator Stack + Two-Number Fusion:** `15 [ENTER] 3 [-] 4 [ENTER] 2 [+] [×] 6 [÷]` (11 keystrokes). Both intermediate quantities ($12$ in $Y$, $6$ in $X$) are visible simultaneously before multiplying. Zero parentheses. | **21% fewer keystrokes** (11 vs. 14) | **Dual Live Registers:** Register $Y$ holds $12$ while Register $X$ computes $6$; live display proves $(15 - 3) \times (4 + 2)$ without scratch paper. | **Clarity of Structure:** Eliminates parenthesis anxiety and the Order-of-Operations & Parentheses Trap; replaces abstract rules with physical two-number stack fusion. |

---

### 2.9.6 Common Stack Slips & How to Fix Them

When you are getting used to the 4-level stack, keep these quick rescues in mind:
- **Typed `5`, then `3`, and the screen shows `53`:** Remember that `[ENTER]` closes the elevator door between your first and second numbers.
- **Entered numbers in reverse order (`4` then `9` instead of `9` then `4`):** Look at the stack before tapping the operator; tap `[x⇄y]` to swap registers immediately, then tap `[-]`.
- **Tapped `[C]` and lost your number:** `[C]` clears the active shelf; use `[ENTER]` to lift your number up to Floor $Y$.
- **Wondering if the next number will overwrite your answer:** Do not press Clear after an answer—automatic stack lift pushes your finished total up to Floor $Y$ as soon as you type the next digit.
- **Step counter adds `0` in 4-stack mode:** Use `[g] [REP]` to fill all four shelves with your step size, or switch to 2-Stack (`2-LV`) mode.
- **Tapped `[+]` and nothing changed:** You need two numbers on the stack to combine (`Y` and `X`).
- **Division shows a decimal like `3.4` instead of whole groups and leftovers:** Use `[g] [÷R]` for whole-number division with remainder.
- **Want to verify an answer without re-typing:** Press `[f] [LASTX]` followed by the opposite operation (for example, after $120 \div 8 = 15$, tapping `[f] [LASTX] [×]` restores $120$).

---

## 2.10 Where to Go Next: Companion Workbook Quests & Kitchen-Table Challenges

> *For 21 additional worked problems with full 4-register stack tables, see Chapter 2 of the [SC-6 Elementary Companion Problem & Activity Workbook](../curriculum/sc6-elementary-companion-workbook.md).*

Want to turn these stack habits into rapid reflexes? Open the **[Big Ideas Math Middle School Supplement](../curriculum/big-ideas-middle-school-sc6-workbook.md) — Unit 1: Numerical Expressions & Factors, Section 1.3 (Order of Operations)**, along with your **StackCalc Student Workbook & 12-Unit Curriculum Guide** (Unit 2: *Riding the 4-Level Number Elevator & Parenthesis-Free Chains*), or challenge your family at the dinner table tonight:

1. **PEMDAS Funnel vs. RPN Inside-Out Showdown:** Write $40 - 3 \times (2 + 3)^2 \div 5$ on a napkin. First solve it on paper using the **PEMDAS Funnel** (watching out for the $40 - 3 = 37$ trap), then race an adult using their phone calculator while you evaluate `40 [ENTER] 3 [ENTER] 2 [ENTER] 3 [+] [x²] [×] 5 [÷] [-]` $\to \mathbf{25}$.
2. **Hands-On Explorer — Clark's Nutcracker Seed-Cache Ledger & `[f] [LASTX]` Detective:** Model the **Clark's Nutcracker Seed-Cache Ledger** (`9 [ENTER] 12 [×] 15 [+] 28 [-]` $\to \mathbf{95}$ seeds), then hand your SC-6 to a partner showing only `95` on Floor $X$. Have them tap `[f] [LASTX] [+]` to uncover the 28 eaten seeds and restore all `123` cached seeds!
3. **Workbook & Timed Proficiency Trial:** Complete **Unit 1, Section 1.3 (Practice Sheets A & B)** in the **Big Ideas Math Middle School Supplement** and **Unit 2 Quest Sheets 2A–2D** in the Companion Student Workbook, then run **Timed Proficiency Trial #2** (Parenthesis-Free Relay & `1089` Mind-Reader Proof).

---

## 2.11 Chapter Summary & Looking Ahead

The core mechanics of **Stack Math** (Reverse Polish Notation) on the SC-6 rest on five principles:
1. **The Golden Rule of Stack Math:** Always place your two numbers onto the stack first, and tap the action button (`[+]`, `[-]`, `[×]`, `[÷]`) last.
2. **The 4-Story Number Elevator ($T, Z, Y, X$):** Watching `[ENTER]` push numbers upward from Floor $X$ to Floor $Y$ while earlier subtotals wait safely on Floors $Z$ and $T$.
3. **Automatic Stack Lift & Drop:** Seeing completed results automatically lift to Floor $Y$ when you type the next number, and drop down cleanly when an operator fuses $Y$ and $X$.
4. **Mistake-Proof Stack Controls:** Fixing typing slips with `[<-]`, swapping order-sensitive subtraction or division pairs with `[x⇄y]`, rotating all four shelves with `[f] [R↓]`, and checking or undoing work without re-typing via `[f] [LASTX]`.
5. **Parenthesis-Free Multi-Step Expressions:** Solving multi-branch problems from the inside out without pressing a single parenthesis key or reaching for scratch paper.

Now that you've mastered pushing numbers onto the stack, swapping registers, and dropping calculations cleanly, turn the page to **[Chapter 03: Counting, Number Lines & Place Value Studio](sc6/03-counting-place-value.md)**—where we will travel back in time to discover how ancient pebble counters and ten human fingers created zero and the power of place value.

---

# Chapter 3: Counting, Number Lines & Place Value Studio

## 3.1 The Greatest Invention in Human History: How Ten Fingers and an Empty Shell Created Zero and Place Value

Five thousand years ago, across the fertile river valleys of the Tigris and Euphrates, an ancient shepherd stood before his flock at dawn. To keep account of his sheep, he dropped small clay pebbles into a woven pouch—one pebble for every sheep that passed through the wooden gate. If thirty sheep walked by, thirty pebbles weighed down his hip. But what happened when a city merchant wished to tally three thousand bushels of barley or thirty thousand bricks for a temple wall? Pockets tore; stone piles grew unmanageable; human memory buckled.

Ancient Egyptian scribes invented symbols for larger numbers: a coiled rope for one hundred, a lotus plant for one thousand, a pointing finger for ten thousand. Yet even with these hieroglyphic shortcuts, writing the number $9,999$ required thirty-six separate symbols carved into stone!

Then came what historians of mathematics document as the single greatest intellectual leap in human numbering *([Ifrah, 2000](sc6/appendix-c-formulas-and-conversions.md#cite-ifrah2000))*: **Place Value and the Invention of Zero.**

In ancient India and among the classic Maya of Mesoamerica *([Ifrah, 2000](sc6/appendix-c-formulas-and-conversions.md#cite-ifrah2000))*, thinkers made a startling realization. You do not need thousands of distinct symbols to write every number in the cosmos. You need only ten fingers, ten counting digits ($0$ through $9$), and a spatial rule: **where a symbol sits changes what it means.** An empty shell glyph drawn in the sand—or an empty groove on a counting board—told the reader: *nothing is in this column, but hold this place open!* Because an empty groove held space, a single digit $1$ could represent one sheep, ten sheep, one hundred sheep, or ten million stars simply by sliding across columns.

The decimal system was born of our anatomy: ten fleshy fingers resting on a tabletop.

On the **StackCalc SC-6**, this five-thousand-year evolution is not an abstract lecture; it is a living tactile laboratory. When you touch the precision-milled **Ten-Frame Studio** or slide the vivid dual-color beads of the **Number Rack**, you recreate the ancient counting table with your own fingers. And as you explore this chapter, you will open four visual sandbox windows right on your keypad—`[▦]` (Ten-Frame Studio), `[g] [COUNT]` (Step Counter / Number Rack), `[f] [LINE]` (Open Number Line), and `[PV]` (Place Value Mode)—using the dot key `[.]` to drop single counters, combining and separating numbers with `[0]`–`[9]`, `[ENTER]`, `[+]`, `[-]`, `[C]`, and `[<-]`, climbing step-counting ladders with `[g] [FLAGS]` and `[g] [REP]`, and returning to standard numbers anytime with `[NUM]` or `[C]`.

---

## 3.2 Building Numbers: From Hands-On Blocks to the Screen Stack

Before numbers become symbols on a screen, they start as real objects in your hands *([Dienes, 1960](sc6/appendix-c-formulas-and-conversions.md#cite-dienes1960); [Singapore MOE, 2014](sc6/appendix-c-formulas-and-conversions.md#cite-singapore2014))*. When you learn math on the StackCalc SC-6, you move through three steps:
1. **Hands-On Blocks (Touch It):** You build with real physical blocks, flip counters, and slide beads across rails on your desk.
2. **Picture Screen (See It):** You tap sandbox keys like `[▦]` or `[f] [LINE]` to see your blocks mirrored as clear pictures on the daylight screen.
3. **The Number Stack (Solve It):** You combine numbers on the 4-level stack with speed and clarity.

![Ten-Frame Studio Physical Manipulative Kit](../assets/renders/ten-frames-hero.png)
*Figure 3.1: The Ten-Frame Studio with dual-color counters. Tactile grounding for five-anchors, decade bridging, and place value.*

| Learning Phase | Physical Manipulative | SC-6 Visual Sandbox | Operational Number Stack |
|---|---|---|---|
| **1. Hands-On Blocks** | Ten-Frame Trays & Dual-Color Disks | Hands-on physical token placement | Sensory tactile certainty |
| **2. Visual Screen** | 20-Bead Rekenrek Number Rack | High-contrast `[▦]` and `[g] [COUNT]` LCD vector grids | Visual subgroup perception |
| **3. Number Stack** | Place Value Studio | `[f] [LINE]` jump arcs and `[PV]` Place Value mode | 4-Register RPN stack arithmetic |

When learners skip hands-on blocks and visual models and jump straight into symbolic calculation on conventional calculators, math can feel like a set of arbitrary rules without conceptual grounding. When faced with an expression such as $8 + 5$, numerals can seem like disconnected symbols and the equal sign (`=`) like a magic black box.

The **StackCalc SC-6** was engineered specifically to give you direct physical grounding. By pairing physical, open-source 3D-printed math manipulatives with dedicated hardware visual sandbox keys (`[▦]`, `[g] [COUNT]`, `[f] [LINE]`, `[PV]`), the SC-6 bridges the tactile world of physical objects directly into the spatial logic of the RPN operational stack.

![SC-6 Ten-Frame Studio Mode: Bridging Ten with 8 + 5 = 13](../assets/manuals/screenshots/sc6_ten_frame_mode.png)
*Figure 3.2: SC-6 Ten-Frame Studio mode (`[▦]`) bridging across 10 with $8 + 5 = 10 + 3 = 13$.*

### 3.2.1 The Ten-Step Triangle Staircase (A Preview of Chapter 4's Multiplication Shortcut)

Have you ever tried adding all the counting numbers from $1$ to $10$ ($1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10$) without losing track halfway through? Long before you meet the famous story that opens Chapter 4, you can discover the secret right on your desk by pairing Friends of Ten with your $7.0\text{ mm}$ ($1\text{U}$) **Unit Miniblocks**, the $70.0\text{ mm}$ ($10\text{U}$) **10-Rod**, and your **Number Rack**:
1. **Build the Staircase:** Line up towers of $1, 2, 3, 4, 5, 6, 7, 8, 9$ Unit Miniblocks ($7.0\text{ mm}$ visible height per block) beside your $70.0\text{ mm}$ 10-Rod ($10$). It forms a 10-step triangle staircase climbing in $7.0\text{ mm}$ steps up to $70.0\text{ mm}$.
2. **Fold the Staircase into $70.0\text{ mm}$ Ten-Towers:** Pick up the smallest step ($1\text{ block}$, $7.0\text{ mm}$) and dock it on top of the $9\text{-block}$ step ($63.0\text{ mm}$)—together they stand exactly $70.0\text{ mm}$ tall, flush with the **10-Rod ($1 + 9 = 10$)**. Next, dock the $2\text{-block}$ step on the $8\text{-block}$ step ($2 + 8 = 10$), the $3\text{-block}$ step on the $7\text{-block}$ step ($3 + 7 = 10$), and the $4\text{-block}$ step on the $6\text{-block}$ step ($4 + 6 = 10$).
3. **Count Your Ten-Towers at a Glance:** You now have **five full $70.0\text{ mm}$ Ten-Towers** ($10$, $9+1$, $8+2$, $7+3$, and $6+4$, worth $5 \times 10 = 50$) plus the single middle tower of **$5$ Unit Miniblocks** ($35.0\text{ mm}$) standing by itself: $50 + 5 = \mathbf{55}$!

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `10 [ENTER] 11 [×]` | 0 | 0 | 0 | 110 | Double staircase forms a $10 \times 11 = 110$ rectangle |
| 2 | `2 [÷]` | 0 | 0 | 0 | **55** | Half the rectangle gives the staircase sum $1 + \dots + 10 = 55$ |

---

### 3.2.2 Seeing Groups Instantly Without Counting One-by-One

Have you ever rolled a dot die and known right away it was a 5, without having to point your finger and count $1, 2, 3, 4, 5$? That skill is called **seeing groups at a glance** (or **subitizing**). 

When you look at small groups of dots, blocks, or counters, your brain recognizes the total in a split second. By organizing numbers around friendly landmarks of **5** and **10**, the SC-6 and your Ten-Frame Studio let you see big numbers just as easily as small numbers—without counting on your fingers.

**Subitizing** is your brain's ability to see how many items are in a small group right away without counting them one by one. It works in two helpful ways:
- **Small Groups ($1$ to $4$):** When you look at $1, 2, 3,$ or $4$ counters on your desk, you recognize the total right away without counting.
- **Combining Friendly Groups ($5$ to $10+$):** For larger numbers, your eyes spot smaller groups and snap them together. When you see $7$ dots arranged in a ten-frame, you don't count $1, 2, 3, 4, 5, 6, 7$—you immediately see a full top row of $5$ plus $2$ more on the bottom ($5 + 2 = 7$).

The SC-6 visual screens are built around friendly landmarks of **5** and **10** so your eyes can always spot the pattern at a glance.

---

### 3.2.3 How Your Trays and Counters Are Built for Your Hands

The physical manipulative studios accompanying the SC-6 are engineered as modular tactile companions, standardized on the Gridfinity organization grid. Where the calculator provides a dark, glare-free slate upon which numbers are evaluated, the manipulative blocks supply immediate physical mass and vibrant color:

- **Ten-Frame Studio & Dual-Color Counters:** Dual ten-frame wells separated by a raised divider rib. The physical tactile ridge provides an unmistakable boundary at five, allowing fingers to spot group sizes at a glance (subitizing) without counting one by one. Chamfered counter disks in contrasting coral and amber seat firmly into each pocket.
- **Number Rack (Rekenrek):** Dual horizontal stainless guide rails holding smoothly sliding beads arranged in five-and-five color clusters, mirroring the two-register display of the calculator.
- **Place Value Studio:** Dual $4 \times 2$ desktop Place Value Activity Trays—the **Whole Numbers Tray** (`THOUSANDS | HUNDREDS | TENS | ONES`) and **Decimal Numbers Tray** (`ONES • TENTHS | HUNDREDTHS | THOUSANDTHS`)—paired with 44 digit miniblocks (`0`–`9`) and 9 stackable `+1` regrouping unit miniblocks ($19.0 \times 19.0 \times 7.0\text{ mm}$ visible $1\text{U}$ height, where 10 stacked unit blocks match the $70.0\text{ mm}$ Ten-Frame 10-Rod).
- **Counting & Array Tiles:** Interlocking tactile tiles engineered with smooth slip-fit tabs that assemble into flat 2D arrays and vertical counting towers.
- **Prime Factor Studio:** Color-coded blocks for the prime numbers ($2$, $3$, $5$, and $7$) whose heights stack together so you can see and feel how prime factors multiply to build composite numbers.

---

## 3.3 Inside the Ten-Frame Studio (`[▦]`): A Picture Window Into Your Stack

Think of the four visual sandbox keys (`[▦]`, `[g] [COUNT]`, `[f] [LINE]`, and `[PV]`) as special camera lenses that let you peek inside your calculator's shelves and *see* your numbers as real blocks, beads, and number trails.

The first lens is the **Ten-Frame Studio (`[▦]`)**. It arranges numbers in neat groups of five and ten so your eyes can spot how many counters you have at a glance—and how many empty pockets are left to reach the next ten!

> **Why Your Physical Ten-Frame Tray Has a Center Ridge:**  
> Run your finger across your physical Ten-Frame Studio tray and you will feel a raised central divider rib splitting the two $2 \times 5$ ten-frame wells. That ridge separates the first five pockets from the second five pockets, so your eyes and fingertips can recognize a full row of five immediately without counting one by one.

### 3.3.1 Opening the Ten-Frame Window
Suppose you type `[7]` onto Ground Shelf $X$ and press `[▦]`. Right away, the screen opens a split picture window: the top half draws two ten-frame trays with **7 round counters** tucked inside, while the bottom half keeps your live $Y$ and $X$ shelves in plain view:

| Display Region | Visual & Numeric Representation (`X = 7`) |
| :--- | :--- |
| **Upper Screen (Ten-Frame Grid)** | Top row: `[●][●][●][●][●]` ($5$ filled); Bottom row: `[●][●][ ][ ][ ]` ($2$ filled, $3$ empty) |
| **Lower Screen (Active Stack)** | `Y: 0` $\mid$ **`X: 7`** ($5 + 2 = 7$ seen at a glance) |

Look at how those 7 counters sit inside the first frame: the top row is completely full with 5 counters, the bottom row holds 2 counters, and 3 empty pockets are waiting at the end of the row (while the second ten-frame sits empty). You don't need to count $1, 2, 3, 4, 5, 6, 7$. Your eyes immediately see a full row of 5 plus 2 more on the bottom ($5 + 2 = 7$)—and you can see at a glance that **3 empty pockets** are waiting to make a full 10!

### 3.3.2 Dropping Counters One by One with the Decimal Key (`[.]`)
While you are inside the Ten-Frame Studio, the decimal key `[.]` acts like your own hand dropping counters into the tray one at a time. Starting from $X = 7$, watch what happens each time you tap `[.]`:
- Tap `[.]` once and an 8th counter drops into the bottom row ($X = 8$).
- Tap `[.]` again and a 9th counter lands next to it ($X = 9$), leaving just **1 empty pocket** in the first frame.
- Tap `[.]` a third time and the 10th counter snaps that last pocket shut ($X = 10$)! The border of the first ten-frame flashes briefly to celebrate that you have built one complete group of ten.
- Tap `[.]` one more time ($X = 11$) and the 11th counter hops across the center divider ridge into the first pocket of Frame 2, showing $10 + 1 = 11$ right before your eyes.

> **Spotting the Partner to Ten:** Whenever a number under 10 is sitting in the Ten-Frame Studio, just count the empty pockets in Frame 1 to find its "Friend of Ten." With 7 counters in the tray, you see 3 empty pockets—so pressing `[3]` `[+]` fills the frame completely and lands on $X = \mathbf{10}$.

---

## 3.4 Making Ten & The "Bridging Ten" Strategy

When you first add across a ten boundary (like $8 + 5$), counting on your fingers (*"eight... nine, ten, eleven, twelve, thirteen"*) can feel slow and tricky. The Ten-Frame Studio shows you a much faster way called **Bridging Ten**: instead of counting by ones, you borrow just enough counters from the second number to finish filling the first tray of 10, and drop the leftovers into the second tray!
$$\mathbf{8 + 5 = 8 + (2 + 3) = (8 + 2) + 3 = 10 + 3 = 13}$$

### 3.4.1 How Your Eyes Bridge Across Ten
Picture starting with **8 counters** in Frame 1 (`[●][●][●][●][●] | [●][●][●][ ][ ]`), which leaves **2 empty pockets**. You are holding **5 counters** in your hand to add. Instead of adding all 5 at once, split your 5 into **`2 + 3`**:
1. Drop **2 counters** into the two empty pockets of Frame 1 (`[●][●][●][●][●] | [●][●][●][●][●]`) to lock in a **Full 10**.
2. Drop the remaining **3 counters** into the fresh second frame (`[●][●][●][ ][ ] | [ ][ ][ ][ ][ ]`).
3. Now read the two trays together: **1 full tray of 10 + 3 extras = 13!** On your SC-6, key in `[▦] 8 [ENTER] 5 [+]` to see **`13`**.

### 3.4.2 Try Bridging Ten with Your Dual-Color Counters and Screen

![Ten-Frame Studio: Bridging Ten Strategy (8 + 5 = 13)](../assets/manuals/ten_frame_bridging_ten.png)

First, build the bridge on your desk: place 8 coral-red counters into Frame 1 of your physical tray (filling the top row of 5 and 3 pockets on the bottom row), and hold 5 amber-gold counters in your hand. Because Frame 1 has 2 empty pockets waiting, drop 2 gold counters in to complete the ten ($8 + 2 = 10$), then place the remaining 3 gold counters into Frame 2 ($10 + 3 = 13$).

Now watch the exact same bridge happen on your Ten-Frame screen: press `[8] [▦]` to see 8 dots in Frame 1, tap `[2] [+]` to fill Frame 1 and flash the completed ten ($X = \mathbf{10}$), and tap `[3] [+]` to land the remaining 3 counters in Frame 2 ($X = \mathbf{13}$):

| Keystroke | Register T | Register Z | Register Y | Register X (Display) |
| :--- | :--- | :--- | :--- | :--- |
| `[8] [▦]` | 0 | 0 | 0 | 8 |
| `[2] [+]` | 0 | 0 | 0 | 10 |
| `[3] [+]` | 0 | 0 | 0 | 13 |

### 3.4.3 The Bioluminescent Nature Lab: Ten-Frames & Bridging Ten in Action
To see how Ten-Frames and Bridging Ten help real scientists in the field, step into the shoes of a junior field biologist inside a glowing rainforest nature dome! Researchers bring in firefly terrariums, meteorite fragments, crystal geodes, weather sensors, and glowing algae tubes. Using your Ten-Frame trays (`[▦]`) and the SC-6 stack, you will spot groups at a glance, bridge across 10 without counting on your fingers, and step back across 10 with ease.

Your first stop in the rainforest dome is a glass terrarium where 5 glowing lantern fireflies rest on the top branch. Just after dusk, 3 more fireflies land on the lower fern branch, and your lab partner asks how many fireflies are glowing in the terrarium altogether. On your Ten-Frame tray, fill the top row of Frame 1 with 5 counters and place 3 counters on the bottom row. Because the top row of a ten-frame always holds 5, your eyes immediately see *"5 on top and 3 on the bottom makes 8"*—zero finger-counting needed! When you lift the 5 upper fireflies onto Shelf $Y$ and add the 3 lower fireflies by pressing `5 [ENTER] 3 [+]`, the stack combines both branches to show **`8`** glowing fireflies on Ground Shelf $X$.

Right beside the firefly habitat, a planetary geologist is sorting magnetic iron meteorite pebbles into 10-slot specimen trays. The first tray already holds 9 pebbles, and a rover scoop delivers 4 more pebbles from a crater rim. What happens when we add $9 + 4$ across the 10-boundary? Look at your Ten-Frame tray: with 9 counters in Frame 1, there is only **1 empty pocket** left. Instead of counting upward by ones, split your 4 new pebbles into **$1 + 3$** so 1 pebble snaps the first tray shut at 10, and the other 3 pebbles land in Frame 2: pressing `9 [ENTER] 1 [+] 3 [+]` bridges cleanly through $10$ and lands on **`13`** pebbles.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `9 [ENTER]` | 0 | 0 | 9 | 9 | Load 9 meteorite pebbles into $X$ and duplicate to Mezzanine $Y$ |
| `1 [+]` | 0 | 0 | 0 | 10 | Bridge to ten; Frame 1 completely fills and flashes ($X = 10$) |
| `3 [+]` | 0 | 0 | 0 | 13 | Combine ten and three; Frame 2 holds 3 dots, giving total $X = 13$ pebbles |

Once Frame 1 locks in at 10, adding the remaining 3 pebbles is an instant visual snap ($10 + 3 = 13$).

Walking deeper into the geology alcove, a cave explorer cracks open a limestone boulder and finds 7 purple amethyst crystals in the first pocket and 6 sparkling quartz crystals in the second pocket. How does that same Bridging Ten trick work when we start at 7 instead of 9? On your Ten-Frame tray, 7 counters fill the top row of 5 plus 2 on the bottom row, leaving **3 empty pockets** in Frame 1—which invites you to split the 6 quartz crystals into twin halves ($3 + 3$). Watch how the shelves and the Ten-Frame screen move in lockstep as you key in `7 [ENTER] 3 [+] 3 [+]` to reach **`13`**: first, `7 [ENTER]` loads the 7 amethyst crystals into Ground Shelf $X$ and duplicates them onto Waiting Shelf $Y$. Next, typing `3 [+]` drops the first 3 quartz crystals into those 3 empty pockets—snapping Frame 1 completely full so the display flashes the clean benchmark `10` ($X = 10$). Then a second `3 [+]` places the remaining 3 quartz crystals into the top row of Frame 2, uniting 1 full ten-frame with 3 loose crystals to display `13` ($X = 13$). Even better, notice that right after the first `3 [+]` reaches 10, the number `3` is already sitting in your `LASTX` backup memory—so you can also tap `[f] [LASTX] [+]` to add the second 3 without even typing the digit again!

From the crystal alcove, you step out onto the dome's canopy deck carrying a foam launch case that holds a full set of 10 micro-weather sensors. Your team clips 4 sensors onto kite strings and launches them into the rainforest wind, leaving the rest in the case. Fill Frame 1 with all 10 counters and pop 4 counters out to see the full top row of 5 plus 1 counter on the bottom row ($6$). When you load the full crate onto Shelf $Y$ and subtract the 4 launched sensors by pressing `10 [ENTER] 4 [-]`, Ground Shelf $X$ immediately shows **`6`** sensors still nestled in the foam case. *(Want to prove none were lost when you reel the kites back in? Tap `[f] [LASTX] [+]` and watch the 4 launched sensors reunite with the 6 in the crate to restore `10`!)*

Back inside the wet lab, a bioluminescence rack holds 14 glowing algae test tubes—1 full rack of 10 plus 4 extra tubes in the second rack—and a student scientist takes 6 tubes to the microscope station. Just as we bridged *forward* across 10 with the meteorite pebbles and geode crystals, we can bridge *backward* across 10 when subtracting $14 - 6$! Instead of counting backward one by one, hop back to the landmark 10 first by splitting the 6 tubes you are removing into **$4 + 2$**: first remove all 4 tubes from Frame 2 (leaving a clean 10 in Frame 1), then take 2 more tubes from Frame 1. Pressing `14 [ENTER] 4 [-] 2 [-]` steps back to `10` and then down to **`8`** glowing tubes.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `14 [ENTER]` | 0 | 0 | 14 | 14 | Load 14 glow-tubes into $X$ and duplicate to Mezzanine $Y$ |
| `4 [-]` | 0 | 0 | 0 | 10 | First subtraction empties Frame 2, leaving clean benchmark ten ($X = 10$) |
| `2 [-]` | 0 | 0 | 0 | 8 | Second subtraction takes 2 from Frame 1, leaving 8 glow-tubes ($X = 8$) |

Splitting $-6$ into $-4$ and $-2$ turns a tricky teen subtraction into two effortless mental hops ($14 \to 10 \to 8$).

---

## 3.5 Step-Counter Towers & Stacking Tile Heights

Have you ever noticed that counting forward ($1, 2, 3, 4 \dots$) is really just adding $1$ over and over again? On a regular calculator, pressing `+ 1 = = =` hides the `+ 1` inside a secret memory box. On your SC-6, you can watch the `1` sit right on your waiting shelf while you stack real $7.0\text{ mm}$ counting tiles into a rising tower on your desk!

### 3.5.1 Building a 12-Story Tower up to 84 Millimeters

![Master Datum Alignment: 12 Counting Tiles (12 x 7.0 mm = 84.0 mm) Flush with 1-Whole Fraction Tower](../assets/manuals/counting_tiles_fraction_datum_84mm.png)

Every interlocking Counting Tile adds exactly $7.0\text{ mm}$ of visible height. As you snap them together one by one, watch how your growing tower matches the heights of your **84 mm Fraction Studio** blocks:

| Stacked Tile Count (`X`) | Cumulative Physical Height | Geometric & Fraction Studio Datum |
| :---: | :---: | :--- |
| **Tile 1 (`X = 1`)** | $7.0\text{ mm}$ | $1\text{U}$ visible increment $= 1/12$ Fraction Tower |
| **Tile 2 (`X = 2`)** | $14.0\text{ mm}$ | $1/6$ Fraction Tower datum |
| **Tile 3 (`X = 3`)** | $21.0\text{ mm}$ | $1$ Unit Cube equivalent $= 1/4$ Fraction Tower |
| **Tile 4 (`X = 4`)** | $28.0\text{ mm}$ | $1/3$ Fraction Tower datum |
| **Tile 6 (`X = 6`)** | $42.0\text{ mm}$ | Halfway datum $= 1/2$ Fraction Tower |
| **Tile 12 (`X = 12`)** | $84.0\text{ mm}$ | Full $1\text{-Whole}$ Master Fraction Tower |

You can climb—and count down—that 12-story tile tower on your calculator in three different ways, depending on how many shelves your elevator is using. First, try climbing in **2-Shelf Mode (`[g] [FLAGS]` $\to$ `2-LV`)**: place 1 white tile on your desk ($7.0\text{ mm}$) and press `[1] [ENTER] [1] [+]` to reach $X = 2$ as you snap a second tile on top ($14.0\text{ mm}$). Because Shelf $Y$ is the top shelf in `2-LV` mode, it keeps `1` locked in place—so every time you snap another tile onto your tower and tap `[+]`, the screen climbs in lockstep ($3, 4, 5 \dots 12$). When you snap the 12th tile on top, stand your 12-tile stack next to the white **1-Whole Fraction Tower**: both stand at the exact same **$84.0\text{ mm}$** height!

| Keystroke | Register Y (Constant) | Register X (Display) | Physical Tile Height on Desk (7.0 mm per Tile) |
| :--- | :--- | :--- | :--- |
| `[1] [ENTER]` | 1 | 1 | 1 Tile  =  7.0 mm |
| `[1]` | 1 | 1 | 1 Tile  =  7.0 mm |
| `[+]` | 1 | 2 | 2 Tiles = 14.0 mm |
| `[+]` | 1 | 3 | 3 Tiles = 21.0 mm (1 Unit Cube) |
| `[+]` | 1 | 4 | 4 Tiles = 28.0 mm |
| `[+]` | 1 | 5 | 5 Tiles = 35.0 mm |
| `[+]` | 1 | 6 | 6 Tiles = 42.0 mm (1/2 Whole Tower) |
| `[+]` | 1 | 7 | 7 Tiles = 49.0 mm |
| `[+]` | 1 | 8 | 8 Tiles = 56.0 mm |
| `[+]` | 1 | 9 | 9 Tiles = 63.0 mm |
| `[+]` | 1 | 10 | 10 Tiles = 70.0 mm |
| `[+]` | 1 | 11 | 11 Tiles = 77.0 mm |
| `[+]` | 1 | 12 | 12 Tiles = 84.0 mm (1 Whole Tower!) |

Second, what if you are in standard **4-Shelf Mode (`4-LV`)**? Press `[1] [g] [REP]` first! Constant Repeat copies `1` onto all four shelves ($T, Z, Y, X$), so every tap of `[+]` feeds a fresh `1` down from the Penthouse roof ($2, 3, 4, 5, 6 \dots$):

| Keystroke | Register T (Constant) | Register Z | Register Y | Register X (Display) |
| :--- | :--- | :--- | :--- | :--- |
| `[1]` | 0 | 0 | 0 | 1 |
| `[g] [REP]` | 1 | 1 | 1 | 1 |
| `[+]` | 1 | 1 | 1 | 2 |
| `[+]` | 1 | 1 | 1 | 3 |
| `[+]` | 1 | 1 | 1 | 4 |
| `[+]` | 1 | 1 | 1 | 5 |
| `[+]` | 1 | 1 | 1 | 6 |

Third, you can run a **Rocket Launch Countdown** by unstacking a 10-tile tower ($70.0\text{ mm}$) one block at a time: key in `[1] [0] [ENTER] [1]`, pop 1 tile off the top of your tower as you tap `[-]` ($X = \mathbf{9}$), and keep unstacking down to $X = \mathbf{0}$—Blast off!

| Keystroke | Register Y | Register X |
| :--- | :--- | :--- |
| `10 [ENTER]` | 10 | 10 |
| `[1] [-]` | 10 | 9 |
| `[-]` | 10 | 8 |
| `[-]` | 10 | 7 |
| `[-]` | 10 | 6 |
| `[-]` | 10 | 5 |
| `[-]` | 10 | 4 |
| `[-]` | 10 | 3 |
| `[-]` | 10 | 2 |
| `[-]` | 10 | 1 |
| `[-]` | 10 | 0 |

### 3.5.2 Observatory Step Ladders & Rhythmic Countdowns
Now let's take those step-counting ladders up to a mountaintop astronomical observatory! Inside the optics and planetary motion labs, technicians calibrate paired sensors, launch weather balloons, and track orbiting moons using rhythmic step-counting ladders in 2-Shelf (`2-LV`) and 4-Shelf (`4-LV`) modes.

In the observatory optics lab, technicians calibrate paired star sensors by counting by 2s up to 20. Remember our step-counter discovery from Chapter 2: in **2-Shelf mode (`2-LV`)**, Shelf $Y$ is the roof of the stack, so it holds onto your step size (`2`) across every single tap of `[+]`! Switch to `[g] [FLAGS] 2-LV` and climb the twos ladder by pressing `2 [ENTER] 2 [+]`, which steps evenly by twos all the way to **`4`**. After `2 [ENTER] 2 [+]` shows $Y = 2,\; X = 4$, each rhythmic tap of `[+]` advances through $6, 8, 10, 12, 14, 16, 18,$ up to $20$ while Shelf $Y$ keeps the constant `2` locked in place.

Once the star sensors are calibrated, you step out onto the observatory roof deck, where the flight director prepares to launch a high-altitude weather balloon by counting down from 50 to 0 by 5s. Each `5 [-]` step drops the countdown by 5 in a steady rhythm until liftoff at zero: keying in `50 [ENTER] 5 [-] 5 [-] 5 [-] 5 [-] 5 [-] 5 [-] 5 [-] 5 [-] 5 [-] 5 [-]` steps down five meters of cable at a time until Ground Shelf $X$ reaches **`0`**. Starting with `50 [ENTER] 5 [-]` $\to$ $45$, nine more steps count down through $40, 35, 30, \dots, 0$ to reach liftoff at $X = 0$! *(Tip: You can also press `[f] [LASTX] [-]` to reuse the `5` from `LASTX`.)*

What if you want a one-tap skip-counting ladder with `[g] [REP]` while staying in standard **4-Shelf mode (`4-LV`)**? Back inside the planetary motion lab, astronomers track Jupiter's three locked Galilean moons (Io, Europa, and Ganymede) by generating multiples of 3. Pressing Constant Repeat (`[g] [REP]`) fills all four floors ($T, Z, Y, X$) with `3`, so every tap of `[+]` automatically feeds a fresh `3` down from the Penthouse roof: `3 [g] [REP] [+] [+] [+]`.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `3 [g] [REP]` | 3 | 3 | 3 | 3 | The `[g] [REP]` repeat key replicates 3 across all registers ($T, Z, Y, X$) |
| `[+]` | 3 | 3 | 3 | 6 | First addition yields 6; register $T$ preserves constant 3 |
| `[+]` | 3 | 3 | 3 | 9 | Stack drop supplies 3 automatically; total reaches 9 |
| `[+]` | 3 | 3 | 3 | 12 | Constant replicates from top of stack ($X = 12$) |

Because Penthouse $T$ copies itself every time the stack drops, you never run out of 3s!

---

### 3.5.3 Why Adding Odd Numbers Always Builds a Square (The L-Shape Pattern)

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

You can watch those growing squares form right on the SC-6 stack—and even go beyond the 16 tiles on your desk to build $5 \times 5$ and $6 \times 6$ squares before checking the final side length with the square-root key (`[f] [√x]`). Start by pressing `[1] [ENTER] [3] [+]` to reach $\mathbf{4}$ ($2^2$), matching your 1 white center tile ($Y = 1$) wrapped by a 3-tile blue L-border ($X = 4$). Next, tap `[5] [+]` to wrap the 5-tile gold border around the corner and reach $\mathbf{9}$ ($3 \times 3$ square), then tap `[7] [+]` to wrap the 7-tile gray border and lock in $\mathbf{16}$ ($4 \times 4$ square). Keep the pattern rolling by tapping `[9] [+]` to wrap a 9-tile border into $\mathbf{25}$ ($5 \times 5$ square), and finally tap `[1] [1] [+]` to wrap an 11-tile border into $\mathbf{36}$ ($6 \times 6$ square) before pressing `[f] [√x]` to reveal $\mathbf{6}$—the exact side length of your $6 \times 6$ square!

---

### 3.5.4 How Triangular Step Ladders Build Rectangular Arrays

Earlier in this chapter, we folded a 10-step staircase of blocks into Friends of Ten ($1 + 2 + \dots + 10 = 55$). Now let's discover an even more powerful geometric trick that works for *any* staircase of counting numbers—like $1 + 2 + 3 + 4 + 5 + 6 = 21$.

Using your **24-Tile Four-Color Counting & Array Studio**, build six rising columns of tiles on your desk: $1\text{ tile}$, then $2\text{ tiles}$, then $3, 4, 5,$ and $6\text{ tiles}$. Notice how your 21 tiles form a right triangle whose top edge climbs in a jagged 6-step staircase.

How can you find the area of a jagged triangle without adding every column one by one? Imagine a friend builds an identical 21-tile staircase ($1 + 2 + 3 + 4 + 5 + 6$) and flips theirs **upside-down** right on top of yours:
- Their tallest column of **$6$** lands on top of your shortest step of **$1$**, making a column **$7$ tiles tall** ($1 + 6 = 7$).
- Their step of **$5$** lands on your step of **$2$**, also making **$7$ tiles tall** ($2 + 5 = 7$).
- Every single column locks together at **$7$ tiles tall** across all **$6$ columns**—forming a solid **$6 \times 7 = 42$ rectangle**! (And even with a single 24-tile kit, you can fold your 6-step staircase in half—snapping $1$ onto $6$, $2$ onto $5$, and $3$ onto $4$—to form a $3 \times 7 = 21$ rectangle.)

Because two identical staircases make a $6 \times 7 = 42$ rectangle, **one** staircase is simply half of that rectangle ($42 \div 2 = 21$):

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `6 [ENTER]` | 0 | 0 | 6 | 6 | Place 6 staircase columns onto Mezzanine $Y$ |
| `7 [×]` | 0 | 0 | 0 | 42 | Two interlocked staircases form a $6 \times 7 = 42$ rectangle ($X = 42$) |
| `2 [÷]` | 0 | 0 | 0 | 21 | Half the rectangle gives one triangular staircase ($42 \div 2 = 21$) |

Remember this *"put two staircases together into a rectangle and cut it in half"* secret—at the start of Chapter 4, you will see how a 9-year-old boy used this exact trick to add $1$ through $100$ in seconds!

---

## 3.6 Number Line Navigation & Visual Jump Arcs (`[f] [LINE]`)

If the Ten-Frame Studio lets you see numbers as trays of counters, the **Open Number Line (`[f] [LINE]`)** turns addition and subtraction into a hiking trail across your screen.

### 3.6.1 Watching Your Numbers Leap Across the Trail
Whenever you press `[f] [LINE]`, the top half of your screen draws a crisp ruler trail that automatically scales its tick marks ($1, 2, 5,$ or $10$) to fit your journey. Then, as soon as you add or subtract, a curved **jump arc** leaps from your starting milepost to your landing spot:

| Display Zone | Visual Representation (`2 + 5 = 7`) |
| :--- | :--- |
| **Jump Arc Layer** | Curved forward jump arc labeled `+5` spanning from tick `2` to tick `7` |
| **Number Line Axis** | High-contrast tick ruler spanning `0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11` |
| **Register `Y:`** | `2` (Starting coordinate) |
| **Register `X:`** | `7` (Landing coordinate after `+5` jump) |

### 3.6.2 Forward Hops, Backward Hops & The `[f] [LASTX]` Return Trip
Watching the arc leap across the screen connects three ideas at once—where you started ($Y$), how far and which way you hopped, and where you landed ($X$):
- **Forward Jump (Addition):** When you key in `2 [ENTER] 5 [+]` (or `14 [ENTER] 8 [+]` $\to 22$), an arc sweeps **to the right**, labeled `+5` (or `+8`), showing your number growing along the trail.
- **Backward Jump (Subtraction):** When you key in `9 [ENTER] 4 [-]` (or `22 [ENTER] 5 [-]` $\to 17$), an arc leaps **to the left**, labeled `-4` (or `-5`), showing you walking back down the trail.
- **The `[f] [LASTX]` Return-Trip Trick:** Want to hop right back to your starting milepost without re-typing your jump size? Right after `14 [ENTER] 8 [+]` lands on `22`, tap `[f] [LASTX] [-]`—`LASTX` remembers your `8`-step jump and arcs straight back to `14`!

### 3.6.3 The Kangaroo Trailblazer: Tracking Hops Across the Outback
To see how the Open Number Line (`[f] [LINE]`) turns real-world distances and elevations into visual jump arcs, join a wildlife tracking team mapping the Australian Outback trail!

At the start of the trail, an Australian red kangaroo rests at kilometer marker 14 near a dry creek bed, then bounds forward 8 kilometers across the red sand plains to reach fresh desert grass. Which trail marker does the kangaroo reach? On your Open Number Line (`[f] [LINE]`), start at tick 14 and launch a forward arc of `+8`. Just like bridging across 10 on a ten-frame, your mind can hop $+6$ to land on milestone 20 and $+2$ more to reach marker 22: when you press `14 [ENTER] 8 [+]`, the jump arc sweeps across the twenty mark and lands squarely on kilometer **`22`**.

A little farther along the trail, an outback scout stands atop a towering red sand dune at elevation 23 meters, then hikes down 7 meters into a shaded eucalyptus grove. To find the grove's elevation on the number line, pin tick 23 on your Open Number Line and launch a backward arc of `-7` across benchmark 20—stepping back 3 meters to hit 20, and 4 more meters to land on 16: pressing `23 [ENTER] 7 [-]` traces the downward hike to **`16`** meters. *(Now try the **Instant Reverse-Hop Check**: press `[f] [LASTX] [+]` and watch the `-7` hike sitting in `LASTX` reverse into a `+7` climb right back to `23`!)*

From that shaded eucalyptus grove, your survey team maps a three-part trek across the bush: 18 kilometers from base camp to Spinifex Ridge, 5 kilometers to the Giant Boab Tree, and 7 kilometers to the Emerald Billabong. Watch how automatic stack lift chains the two forward jump arcs (`+5` then `+7`, which together add $+12$ onto $18$) to land right on a round decade milestone: keying in `18 [ENTER] 5 [+] 7 [+]` advances from marker `18` to `23` and then lands on **`30`** kilometers.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `18 [ENTER]` | 0 | 0 | 18 | 18 | Pin Spinifex Ridge distance 18 into $X$ and duplicate to Mezzanine $Y$ |
| `5 [+]` | 0 | 0 | 0 | 23 | First hop completes; first arc lands on Boab Tree marker 23 ($X = 23$) |
| `7 [+]` | 0 | 0 | 0 | 30 | Final hop completes; second arc lands cleanly on milestone 30 ($X = 30$) |

Those two consecutive arcs trace $18 \to 23 \to 30$, confirming a total trail length of $30\text{ km}$.

At the end of the outback hike, the team cartographer measures the span between Escarpment Overlook (kilometer 63) and Riverbed Base Camp (kilometer 27) to see how far apart the two camps sit. On the Open Number Line, jump backward from 63 by splitting $-27$ into friendly mental hops ($-20$ to 43, $-3$ to 40, and $-4$ to 36), then verify on the stack by pressing `63 [ENTER] 27 [-]` to find a camp separation of **`36`** kilometers.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `63 [ENTER]` | 0 | 0 | 63 | 63 | Pin Escarpment marker 63 into Register $X$ and duplicate to Mezzanine $Y$ |
| `27 [-]` | 0 | 0 | 0 | 36 | Leap backward by 27 units; arc lands squarely on tick 36 ($X = 36$) |

Want to verify that starting at camp $36$ and hiking $+27\text{ km}$ brings you right back to marker $63$? Don't re-type `27`—just press `[f] [LASTX] [+]` and watch `63` reappear on the ground floor!

### 3.6.4 What Happens When You Hop Left Past Zero? (`[f] [LINE]` & Zero-Pair Counters Preview)

What happens on the Open Number Line (`[f] [LINE]`) if you start at **$+3$** and subtract **$5$** (`3 [ENTER] 5 [-]`)? Does the number line stop at a brick wall at $0$?

Not at all! The mark $0$ is simply the mirror line (like sea level at the beach or freezing point on a thermometer) between positive numbers to the right and negative numbers to the left:
- **Two-Stage Hop Past Zero on `[f] [LINE]`:** Tap `[f] [LINE]`, then key in `3 [ENTER] 5 [-]`. Watch the jump arc hop **3 steps left to reach $0$**, and then continue **2 more steps left of zero** to land on **`-2`**!
- **Andean Hummingbird Nighttime Torpor:** High in the Andes mountains, a hummingbird conserving energy in nighttime *torpor* watches the mountain air drop from $+3^\circ\text{C}$ at dusk by $5^\circ\text{C}$ overnight: $3 - 5 = \mathbf{-2^\circ\text{C}}$ ($2^\circ\text{C}$ below freezing).
- **Zero-Pair Flip Counters:** On your Ten-Frame tray, 1 gold/yellow counter ($+1$) and 1 coral/red counter ($-1$) form a **Zero Pair** ($+1 + (-1) = 0$) that cancels out to zero—a core concept you will master alongside the `[+/-]` key, balance equations, and the 4-Quadrant Coordinate Plane in **[Chapter 07: Discrete Probability, Primes & Pre-Algebra](sc6/07-data-probability-primes.md)**.

---

## 3.7 The European Rekenrek / Number Rack (`[g] [COUNT]`)

Our third visual lens is the **Number Rack (`[g] [COUNT]`)**, modeled on the classic 20-bead *Rekenrek* invented by Adrian Treffers at the Freudenthal Institute in the Netherlands. Look at your physical Number Rack: it has two parallel stainless-steel rods, and each rod carries 10 sliding beads split into **5 Red** and **5 White** ($5 + 5 = 10$ on the top wire, and $5 + 5 = 10$ on the bottom wire, for 20 beads in all).

### 3.7.1 The Five-and-Ten Anchor: How $8 + 6$ Becomes $(5 + 5) + (3 + 1) = 14$ at a Glance
Why did Adrian Treffers split every 10-bead wire into **5 Red** and **5 White** beads instead of painting all 10 beads the same color? Because human eyes can instantly spot up to 5 objects without counting one-by-one—and if 8 beads in a row were all the same color, your eyes would blur!

Watch how the 5-red / 5-white grouping turns $8 + 6$ into an instant visual snap on your physical Number Rack:
1. **Top Wire ($8$):** Slide **8 beads** to the left in a single push—all **5 Red beads** plus **3 White beads** ($5 + 3 = 8$).
2. **Bottom Wire ($6$):** Slide **6 beads** to the left—all **5 Red beads** plus **1 White bead** ($5 + 1 = 6$).
3. **Read the Colors Vertically:** Look at the left column of Red beads: **5 Red on top + 5 Red on the bottom = 10!** Now look at the White beads right next to them: **3 White + 1 White = 4.**

$$8 + 6 = (5 + 3) + (5 + 1) = (5 + 5) + (3 + 1) = 10 + 4 = 14$$

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `5 [ENTER] 5 [+]` | 0 | 0 | 0 | 10 | Combine the two 5-Red bead clusters into a full ten ($X = 10$) |
| `3 [ENTER] 1 [+]` | 0 | 0 | 10 | 4 | Combine the 3 White and 1 White beads ($X = 4$) while 10 waits in $Y$ |
| `[+]` | 0 | 0 | 0 | 14 | Unite the Red ten and White ones: $10 + 4 = 14$ |

### 3.7.2 Seeing Teen Numbers Clearly on the Number Rack (`[g] [COUNT]`)
Teen numbers ($11$ through $19$) play a sneaky trick in the English language. In languages like Chinese or Japanese, $14$ is spoken directly as *"ten-four"*, which tells you right away to write a `1` (one ten) followed by a `4` (four ones). In English, however, we say *"fourteen"*—hearing the word *"four"* first, which tempts many young learners to write $41$ instead of $14$!

Whenever you type `[1] [4]` and press `[g] [COUNT]`, that confusion vanishes at a glance:
- **Top Wire (Wire 1):** Shows all **10 beads** (5 red, 5 white) slid to the active left side—that is the **`1` ten** in `14`.
- **Bottom Wire (Wire 2):** Shows **4 red beads** slid to the left—that is the **`4` ones** in `14`.
- And just like in Ten-Frame mode, tapping `[.]` slides beads across the wire one by one so you can watch numbers grow up to 20 on the dual-wire rack (and up to 100 in extended counting mode).

### 3.7.3 The Coral Reef & Deep-Sea Research Station: Teen Numbers & Doubles on the Rack
Now board a research submarine bound for an underwater coral reef habitat! Here your crew pairs the two-rail **Rekenrek Number Rack (`[g] [COUNT]`)** with the SC-6 stack, sliding 5-red and 5-white bead clusters across the top and bottom wires to spot teen numbers, doubles, and near-doubles in a single glance.

As your submarine descends past the reef wall, the sonar operator spots a pod of 17 spinner dolphins swimming past the observation window. How do you show 17 on the two-rail Number Rack in just two pushes—without counting 17 beads one by one? Slide all 10 beads on Rail 1 (5 red, 5 white) in one sweep to lock in one full ten, then slide 7 beads on Rail 2 (all 5 red plus 2 white). To build that exact $10 + 7$ structure on the stack, press `10 [ENTER] 7 [+]` so Ground Shelf $X$ shows **`17`**, and then tap `[g] [COUNT]` to see 1 full wire of 10 on top and $5 + 2 = 7$ beads on the bottom wire ($X = 17$).

Once the submarine docks inside the underwater hangar, an engineer balances a mini-submersible's left and right thruster pods by bolting 6 battery cells onto the port side and 6 matching battery cells onto the starboard side. Why does the Number Rack make doubles like $6 + 6$ pop out immediately? Slide 6 beads on Rail 1 (5 red, 1 white) and 6 beads on Rail 2 (5 red, 1 white). Now look *vertically* at the red beads: the two 5-red clusters stack up to make a hidden **10**, and the two white beads make **2** ($10 + 2 = 12$)! Combine both battery pods on the stack by pressing `6 [ENTER] 6 [+]`, and the bottom shelf immediately displays **`12`** cells.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `6 [ENTER]` | 0 | 0 | 6 | 6 | Enter 6 port-side battery cells into $X$ and duplicate to Mezzanine $Y$ |
| `6 [+]` | 0 | 0 | 0 | 12 | Add double quantities; $6 + 6 = 12$ battery cells forms in Register $X$ |

Because `6 [ENTER]` already duplicated `6` into both $Y$ and $X$, you don't even have to type the second `6` in your own calculations—pressing `6 [ENTER] [+]` doubles any number on the spot!

Once you know your doubles (like $6 + 6 = 12$ and $7 + 7 = 14$), what happens when two numbers are right next door to each other, like $7 + 8$? On the reef's live video feed, night cameras monitor two sea-turtle nesting beaches: North Cove has 7 nests, and South Cove has 8 nests. Slide 7 beads on Rail 1 and 8 beads on Rail 2 of your Number Rack. You can clearly see a matching pair of sevens ($7 + 7 = 14$) plus **1 extra white bead** on the bottom rail! That is the **Doubles-Plus-One** strategy in action: keying in `7 [ENTER] 7 [+] 1 [+]` doubles the 7 nests to `14` and adds the 1 extra nest to reach **`15`**.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `7 [ENTER]` | 0 | 0 | 7 | 7 | Load North Cove's 7 turtle nests into $X$ and duplicate to Mezzanine $Y$ |
| `7 [+]` | 0 | 0 | 0 | 14 | Add the known double; $7 + 7 = 14$ nests forms in Register $X$ |
| `1 [+]` | 0 | 0 | 0 | 15 | Add the 1 extra nest; total reaches 15 turtle nests ($X = 15$) |

Any two neighbor numbers (like $6 + 7$, $7 + 8$, or $8 + 9$) are simply a double plus 1!

---

## 3.8 Place Value Decomposition Studio (`[PV]`): Archimedes & The 10-for-1 Regrouping Exchange

In the third century BC, the Greek mathematician Archimedes wrote a daring treatise called *The Sand Reckoner*. At the time, people believed the grains of sand on the Sicilian coast were "infinite" because Greek numerals had no clean way to name giant numbers. Archimedes proved them wrong by inventing a system of bundling powers of ten—a breakthrough that Hindu-Arabic mathematicians perfected into the **10-for-1 Regrouping Exchange** we use today *([Ifrah, 2000](sc6/appendix-c-formulas-and-conversions.md#cite-ifrah2000))*.

When you look at a big number like $4,725$, it isn't just four separate digits sitting next to each other ("4", "7", "2", "5"). It is actually four distinct bundled packages working together:
$$4,725 = 4,000 + 700 + 20 + 5$$

To let you touch and test those bundles directly, your **Place Value Studio** pairs physical desktop trays with the calculator's **Place Value Engine (`[PV]`)**:
- **$4 \times 2$ Whole Numbers Activity Tray (`1000 | 100 | 10 | 1`):** A precision $77.8 \times 38.6\text{ mm}$ desktop mat with four recessed place-value columns labeled `THOUSANDS`, `HUNDREDS`, `TENS`, and `ONES` across two working rows (so you can set up two multi-digit numbers side-by-side just like Registers $Y$ and $X$).
- **$4 \times 2$ Decimal Numbers Activity Tray (`1 • 0.1 | 0.01 | 0.001`):** A matching desktop mat with a raised tactile decimal point (`•`) separating `ONES` from `TENTHS`, `HUNDREDTHS`, and `THOUSANDTHS`.
- **44 Place Value Digit Miniblocks (`0`–`9`) & 9 Stackable `+1` Regrouping Blocks ($19.0 \times 19.0 \times 7.0\text{ mm}$ visible $1\text{U}$ height):** Whenever a column accumulates ten `+1` unit miniblocks (reaching $10 \times 7.0\text{ mm} = 70.0\text{ mm}$, the exact height of the $70.0\text{ mm}$ 10-Rod in your Ten-Frame Studio), you trade all 10 unit blocks for a single `+1` regrouping block in the next column to the left (`ONES` $\to$ `TENS` $\to$ `HUNDREDS` $\to$ `THOUSANDS`).

![Place Value Studio Base-10 Decomposition and Regrouping](../assets/manuals/place_value_regrouping.png)
*Figure 3.3: The Place Value Studio. The $4 \times 2$ Whole and Decimal Place Value Trays, digit miniblocks (`0`–`9`), and stackable `+1` regrouping blocks make 10-for-1 place value physical, pairing directly with the SC-6 `[PV]` mode.*

### 3.8.1 Peeking Inside Any Number with `[PV]`
Think of the `[PV]` key as an X-ray lens that lets you look inside a big number and ask: *"How many bundles are sitting in this exact column?"*
1. First, park your **Starting Number** on Waiting Shelf $Y$ (for example, `[4] [7] [2] [5] [ENTER]`).
2. Next, type the **Place Value Column** you want to inspect onto Ground Shelf $X$—type `1` for ones, `10` for tens, `100` for hundreds, or `1000` for thousands.
3. Press `[PV]`, and Ground Shelf $X$ immediately reveals the single digit sitting in that column!

For example, when you check the Tens place of $4,725$ by pressing `[1] [0] [PV]`, Register $X$ shows **`2`** (telling you there are 2 tens, or $20$, inside $4,725$):

| Keystroke | Display T | Display Z | Display Y (Target Number) | Display X (Query / Result) |
| :--- | :--- | :--- | :--- | :--- |
| `4725` | 0 | 0 | 0 | 4725 |
| `[ENTER]` | 0 | 0 | 4725 | 4725 |
| `10` | 0 | 0 | 4725 | 10 |
| `[PV]` | 0 | 0 | 4725 | 2 |

---

### 3.8.2 Why `[PV]` Keeps Your Number Parked on Shelf $Y$
Look closely at the `Display Y` column in the table above: even after you pressed `[PV]`, **your starting number (`4725`) stayed parked on Shelf $Y$!** Even better, `[PV]` turns off automatic stack lift for your next entry so that typing another column size (`100`, `1000`, or `1`) simply replaces the query in $X$ while keeping `4725` right in $Y$.

That means you can X-ray every single column of $4,725$ in rapid-fire succession without ever re-typing `4725`. Right after checking the tens column, type `[1] [0] [0] [PV]` and Ground Shelf $X$ reveals $\mathbf{7}$ (telling you there are 7 hundreds, worth $700$). Next, type `[1] [0] [0] [0] [PV]` to see $X = \mathbf{4}$ (4 thousands, worth $4,000$), and finally type `[1] [PV]` to see $X = \mathbf{5}$ (5 ones, worth $5$).

### 3.8.3 Building Numbers from Expanded Notation in the Navigation Archive
Just as `[PV]` pulls a number apart into its place-value columns, you can also build three-, four-, and five-digit numbers from the ground up by adding their expanded powers of ten ($100\text{s}, 10\text{s}, 1\text{s}$ and beyond). Step into the observatory's historical navigation archive with your physical **Place Value Studio Whole Numbers Tray** to see how!

Your first stop in the archive is a celestial globe showing Earth's solar orbit. How many days does Earth take to complete one full orbit around the Sun? Dock the digit miniblocks `3`, `6`, and `5` into the `HUNDREDS`, `TENS`, and `ONES` sockets of your **Place Value Studio Whole Numbers Tray**: `3` hundreds ($300$), `6` tens ($60$), and `5` ones ($5$). Now watch those three bundled packages snap together into one whole number on the stack: pressing `300 [ENTER] 60 [+] 5 [+]` fuses $300 + 60 + 5$ into **`365`** solar days.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `300 [ENTER]` | 0 | 0 | 300 | 300 | Enter `3` hundreds ($300$) into stack |
| `60 [+]` | 0 | 0 | 0 | 360 | Add `6` tens ($60$); subtotal accumulates to 360 |
| `5 [+]` | 0 | 0 | 0 | 365 | Add `5` ones ($5$); full expanded sum reaches 365 |

Each column contributes its exact place-value weight—$3$ hundreds, $6$ tens, and $5$ ones—to form $300 + 60 + 5 = 365$ days in a year.

Next to the celestial globe sits a brass star astrolabe used by early ocean navigators who steered by the stars long before GPS satellites. Dock the four digit miniblocks `1`, `4`, `9`, and `2` into the `THOUSANDS`, `HUNDREDS`, `TENS`, and `ONES` sockets of your **Whole Numbers Place Value Tray**, then reconstruct that four-digit exploration year on the stack by adding its four place-value columns ($1,000 + 400 + 90 + 2$): keying in `1000 [ENTER] 400 [+] 90 [+] 2 [+]` stacks each power of ten in turn to display **`1492`**. Watch how the open zeros act like empty seats waiting for each smaller bundle to slide into place: starting with `1000 [ENTER]` parks `1000` on Waiting Shelf $Y$, and tapping `400 [+]` slides the 4 hundreds into the hundreds seat so Ground Shelf $X$ updates to `1400`. Next, `90 [+]` lifts `1400` to Shelf $Y$ and drops the 9 tens into the tens seat to form `1490`, and finally `2 [+]` snaps the 2 ones into the rightmost seat to complete `1492`—showing step by step how $1$ thousand, $4$ hundreds, $9$ tens, and $2$ ones lock together without ever interfering with one another's columns.

What happens when a number grows past four digits? In the back of the observatory library, a vault archives a countdown-patterned collection of photographic glass star plates: 9 ten-thousands, 8 thousands, 7 hundreds, 6 tens, and 5 ones. Even though your desktop Place Value Tray has four physical sockets (`1000 | 100 | 10 | 1`), every new column to the left simply bundles 10 of the column before it! Build the five-digit archive total on the stack by pressing `90000 [ENTER] 8000 [+] 700 [+] 60 [+] 5 [+]`, which layers each place-value bundle from left to right to reach **`98765`**.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `90000 [ENTER]` | 0 | 0 | 90000 | 90000 | Enter 9 ten-thousands tier into stack |
| `8000 [+]` | 0 | 0 | 0 | 98000 | Add 8 thousands tier ($X = 98000$) |
| `700 [+]` | 0 | 0 | 0 | 98700 | Add 7 hundreds column ($X = 98700$) |
| `60 [+]` | 0 | 0 | 0 | 98760 | Add 6 tens column ($X = 98760$) |
| `5 [+]` | 0 | 0 | 0 | 98765 | Add 5 ones column; completes 98,765 |

Each addition fills the next open zero column—uniting $9$ ten-thousands, $8$ thousands, $7$ hundreds, $6$ tens, and $5$ ones into $98,765$.

### 3.8.4 Exploring Tenths and Hundredths with Place Value
In Grades 4–6, the exact same 10-for-1 pattern continues to the right of the raised tactile decimal point (`•`) on your **Decimal Place Value Tray (`1 • 0.1 | 0.01 | 0.001`)**. If you cut 1 whole into 10 equal strips, each strip is one **Tenth ($0.1$)**; if you cut 1 tenth into 10 tiny squares, each square is one **Hundredth ($0.01$)**. Suppose you park $345.67$ on Shelf $Y$: you can inspect its Tenths column ($0.1$) by typing `[.] [1] [PV]` to reveal $X = \mathbf{6}$ (6 tenths), and then inspect its Hundredths column ($0.01$) by typing `[.] [0] [1] [PV]` to reveal $X = \mathbf{7}$ (7 hundredths).

Your Decimal Place Value Tray also makes it obvious *why* you must line up the decimal points—not the rightmost digits—when adding or subtracting decimals like $14.6 + 3.85$:
- **Lining Up the Decimal Points on Paper:** Write $14.6$ above $3.85$ so their decimal points (`•`) sit in a straight vertical line, and add a placeholder zero on the end so $14.6$ becomes **$14.60$**. Now Tenths add to Tenths ($.60 + .80$) and Hundredths add to Hundredths ($.00 + .05$): $14.60 + 3.85 = \mathbf{18.45}$.
- **On Your Decimal Tray & SC-6 Stack:** Dock `14.60` in the top row of the Decimal Tray and `3.85` in the bottom row—the raised decimal point physically keeps the Tenths (`6` and `8`) and Hundredths (`0` and `5`) in matching columns! Verify on your SC-6 (`14.6 [ENTER] 3.85 [+]` $\to \mathbf{18.45}$, then `0.1 [PV]` $\to 4$ Tenths and `0.01 [PV]` $\to 5$ Hundredths).
- **Real Workshop Drawer Clearance:** Suppose you slide **4 modular Gridfinity storage bins** ($42.0\text{ mm}$ wide each) side-by-side into a workshop desk drawer whose inside width is **$170.5\text{ mm}$**. How many millimeters of sliding clearance remain? On your SC-6, subtract the width of the 4 bins from the inside width of the drawer (`170.5 [ENTER] 4 [ENTER] 42 [×] [-]`) to see **`2.5` mm** of smooth drawer clearance ($170.5 - 168.0 = 2.5\text{ mm}$).

---

## 3.9 Big Numbers in Nature: Expanding Horizons

Once you master the 10-for-1 regrouping exchange with your blocks, `[PV]` acts like a mathematical X-ray machine that lets you look inside any giant number in nature—from prehistoric dinosaur eras to the icy rings of Saturn.

### 3.9.1 The Earth-Moon Distance ($384,400\text{ km}$)
Look up at the night sky: the average distance from the Earth to the Moon is $384,400\text{ kilometers}$. To see how that colossal distance is built out of base-ten bundles, park $384,400$ on Waiting Shelf $Y$ by typing `[3] [8] [4] [4] [0] [0] [ENTER]`, and then X-ray each column from largest to smallest. Querying the hundred-thousands place with `[1] [0] [0] [0] [0] [0] [PV]` reveals $X = \mathbf{3}$ ($3$ hundred-thousands $= 300,000\text{ km}$); querying the ten-thousands place with `[1] [0] [0] [0] [0] [PV]` shows $X = \mathbf{8}$ ($8$ ten-thousands $= 80,000\text{ km}$); querying the thousands place with `[1] [0] [0] [0] [PV]` extracts $X = \mathbf{4}$ ($4$ thousands $= 4,000\text{ km}$); and querying the hundreds place with `[1] [0] [0] [PV]` finishes with $X = \mathbf{4}$ ($4$ hundreds $= 400\text{ km}$).

> **Lunar Transit Time:** If an Apollo spacecraft cruises toward the Moon at $4,000\text{ km/hour}$, how many hours does it take to complete the journey? By placing the lunar distance on Shelf $Y$ and dividing by the spacecraft's speed—pressing `[3] [8] [4] [4] [0] [0] [ENTER] [4] [0] [0] [0] [÷]`—Ground Shelf $X$ immediately displays **`96`** hours, which works out to about $4\text{ days}$ of continuous spaceflight.

### 3.9.2 Human Heartbeats in a Year ($42,048,000$)
You don't even have to leave Earth to find numbers in the tens of millions—one is beating inside your chest right now! Your heart beats approximately $80\text{ times per minute}$ when you are resting. How many times does it beat in an entire year? With 60 minutes in an hour, your heart beats $80 \times 60 = 4,800\text{ times per hour}$; across 24 hours in a day, that climbs to $4,800 \times 24 = 115,200\text{ beats per day}$; and across all 365 days in a year, it reaches $115,200 \times 365 = \mathbf{42,048,000\text{ beats per year}}$!

Watch how cleanly you can chain that entire year of heartbeats on the SC-6 stack without writing down a single intermediate subtotal:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `80 [ENTER]` | 0 | 0 | 80 | 80 |
| `60 [×]` | 0 | 0 | 0 | 4800 |
| `24 [×]` | 0 | 0 | 0 | 115200 |
| `365 [×]` | 0 | 0 | 0 | 42048000 |

With $42,048,000$ sitting on Ground Shelf $X$, lift it onto Shelf $Y$ and X-ray the top two columns: typing `[ENTER] [1] [0] [0] [0] [0] [0] [0] [0] [PV]` reveals $X = \mathbf{4}$ ($4$ ten-millions, or $40,000,000$ beats), and typing `[1] [0] [0] [0] [0] [0] [0] [PV]` reveals $X = \mathbf{2}$ ($2$ millions, or $2,000,000$ beats).

### 3.9.3 Distance to Mars ($225,000,000\text{ km}$) & The Age of *Tyrannosaurus rex* ($66,000,000\text{ Years}$)
Now let's step up to eight- and nine-digit numbers. At its average orbital distance, the red planet Mars is approximately $225,000,000\text{ kilometers}$ from Earth—and on Earth's geological timeline, the mighty *Tyrannosaurus rex* walked through Cretaceous fern forests $66,000,000\text{ years ago}$. When you X-ray Mars's distance on the Place Value Engine by pressing `225000000 [ENTER] 100000000 [PV]`, Ground Shelf $X$ shows $\mathbf{2}$ (hundred-millions), followed by `10000000 [PV]` $\longrightarrow X = \mathbf{2}$ (ten-millions) and `1000000 [PV]` $\longrightarrow X = \mathbf{5}$ (millions). Doing the same X-ray on the *T. rex* extinction boundary (`66000000 [ENTER] 10000000 [PV]`) reveals $X = \mathbf{6}$ ($6$ ten-million-year bundles), and `1000000 [PV]` reveals $X = \mathbf{6}$ ($6$ one-million-year bundles). And if a robotic spacecraft travels toward Mars at $25,000\text{ km/h}$, how many days will the voyage take? Divide the orbital distance by the hourly speed and then by $24$ hours per day—pressing `225000000 [ENTER] 25000 [÷] 24 [÷]`—to see Ground Shelf $X$ land on **`375` days**, or just over 1 full year in space!

### 3.9.4 Saturn's Ring Orbit ($1,427,000,000\text{ km}$) & Stars in a Dwarf Galaxy ($2,500,000,000$)
Venturing even deeper into the solar system, the ringed planet Saturn orbits the Sun at an average distance of **1 billion, 427 million kilometers** ($1,427,000,000\text{ km}$), while a nearby dwarf galaxy cluster holds $2,500,000,000$ stars:
$$1,427,000,000 = 1,000,000,000 + 400,000,000 + 20,000,000 + 7,000,000$$

Using `[PV]`, you can X-ray Saturn's orbit from the Billions column down to the Millions column without re-typing the number once: `1427000000 [ENTER] 1000000000 [PV]` extracts $X = \mathbf{1}$ (1 billion km), `100000000 [PV]` extracts $X = \mathbf{4}$ (4 hundred-million km), `10000000 [PV]` extracts $X = \mathbf{2}$ (2 ten-million km), and `1000000 [PV]` extracts $X = \mathbf{7}$ (7 million km). In the exact same way, X-raying the dwarf galaxy (`2500000000 [ENTER] 1000000000 [PV]`) shows $X = \mathbf{2}$ (2 billions) and `100000000 [PV]` shows $X = \mathbf{5}$ (5 hundred-millions).

### 3.9.5 Deep-Space Mission Control & Seven-Digit X-Rays
Now take a seat at the Deep-Space Mission Control console to see how `[PV]`, `[f] [LASTX]`, and the four-level stack verify our lunar flight from the start of this section and scale up to seven-digit numbers across million-carton school totals and Voyager 1's daily race through interstellar space!

Start by pulling the $384,400\text{ km}$ Earth-Moon transit we X-rayed a moment ago up onto the main flight-director console. Remember how dividing $384,400\text{ km}$ by the Apollo spacecraft's $4,000\text{ km/h}$ cruising speed gave a lunar voyage of $96.1\text{ hours}$? At Mission Control, every flight calculation must be verified in reverse before launch: when you run that transit division on the stack by pressing `384400 [ENTER] 4000 [÷]` to display **`96.1`** hours ($X = 96.1$), the spacecraft's $4,000\text{ km/h}$ speed is automatically saved inside `[f] [LASTX]`. That means you can prove your transit time is $100\%$ accurate without re-typing a single digit—just tap `[f] [LASTX] [×]` and watch $96.1\text{ hours} \times 4,000\text{ km/h}$ snap right back to the exact `384400` kilometer Earth-Moon distance on Ground Shelf $X$!

Before launching into interstellar space, mission nutritionists ask a down-to-earth question to help the crew picture seven-digit numbers: how big is **one million** in everyday life? Suppose 14 school districts each serve 450 cartons of milk per day across a 180-day school year. Do they cross the one-million-carton mark by summer vacation? To chain all three factors on the stack (`14 × 450 × 180`) without writing down intermediate subtotals, press `14 [ENTER] 450 [×] 180 [×]`, and Ground Shelf $X$ immediately climbs to **`1134000`** cartons.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `14 [ENTER]` | 0 | 0 | 14 | 14 | Enter number of school districts |
| `450 [×]` | 0 | 0 | 0 | 6300 | Daily consumption across all districts ($6,300\text{ cartons/day}$) |
| `180 [×]` | 0 | 0 | 0 | 1134000 | Scale by 180 school days: $1,134,000\text{ cartons/year}$ |

With $1,134,000$ on the screen, you can X-ray every column in place: keying `[ENTER] 1000000 [PV]` extracts $X = \mathbf{1}$ (1 million cartons); `100000 [PV]` extracts $X = \mathbf{1}$ (1 hundred-thousand cartons); `10000 [PV]` extracts $X = \mathbf{3}$ (3 ten-thousand cartons); and `1000 [PV]` extracts $X = \mathbf{4}$ (4 thousand cartons).

Now look out beyond the planets for your final telemetry check: NASA's Voyager 1 spacecraft hurtles through interstellar space at $17\text{ kilometers every second}$. How many kilometers does Voyager 1 travel in one full 24-hour day ($86,400\text{ seconds}$)? Multiply the seconds per day by Voyager's speed on the stack by pressing `86400 [ENTER] 17 [×]`, and the bottom shelf immediately reveals **`1468800`** kilometers!

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `86400 [ENTER]` | 0 | 0 | 86400 | 86400 | Enter seconds per solar day into Register $Y$ |
| `17 [×]` | 0 | 0 | 0 | 1468800 | Daily distance covered: $1,468,800\text{ km/day}$ |

Voyager 1 covers $1,468,800\text{ kilometers}$—nearly $1.5\text{ million kilometers}$—every single day! You can then X-ray every column in place: keying `[ENTER] 1000000 [PV]` extracts $X = \mathbf{1}$ (1 million km); `100000 [PV]` extracts $X = \mathbf{4}$ (4 hundred-thousand km); `10000 [PV]` extracts $X = \mathbf{6}$ (6 ten-thousand km); `1000 [PV]` extracts $X = \mathbf{8}$ (8 thousand km); and `100 [PV]` extracts $X = \mathbf{8}$ (8 hundred km).

---

### 3.9.6 Place Value & Counting Tips

- **Bridging Ten with Two Logs (`[▦]`):** Imagine two logs on a pond, each with room for 10 frogs. If Log 1 already has 9 green frogs and 6 brown frogs arrive, 1 brown frog hops onto Log 1 to fill it ($9 + 1 = 10$), and the remaining 5 hop onto Log 2 ($10 + 5 = 15$). Try it on your Ten-Frame screen (`9 [▦] 1 [+] 5 [+]`): Frame 1 shows 10 dots, Frame 2 shows 5 dots, and Register $X = 15$.
- **Why Zero Matters in 4,005 (`[PV]`):** When writing "four thousand five," leaving out the zeros gives $45$. Test both on the Place Value Engine: `45 [ENTER] 1000 [PV]` returns $X = 0$ (zero thousands), whereas `4005 [ENTER] 1000 [PV]` returns $X = 4$. The zeros hold the hundreds and tens columns open so the 4 stays in the thousands place. Because `[PV]` keeps your number parked in Register $Y$ and suppresses stack lift, you can check `10`, `100`, and `1000` one after another without re-entering the number.
- **Avoiding Teen Number Reversals (`14` vs. `41`):** Because we hear the word "four" first in "fourteen," it is tempting to write `4` first ($41$). Enter `14 [g] [COUNT]` on the Number Rack: Wire 1 holds a full group of 10 beads and Wire 2 holds 4 loose beads. The `1` stands for that full ten, so it always leads on the left.
- **Why a Step Counter Stops Without `[g] [REP]`:** In 4-stack mode, if you press `1 [ENTER] 1 [+]`, the screen shows `2`, but pressing `[+]` again leaves it at `2` because Register $Z$ held `0` ($2 + 0 = 2$). To fill all four floors ($T, Z, Y, X$) with your step size so it never runs out, press `1 [g] [REP] [+] [+] [+]` and watch it climb: `2, 3, 4, 5, 6`.

---

### 3.9.7 Common Stack Slips & How to Fix Them

If your screen shows something unexpected while counting or checking place value, use this quick table to spot what happened and fix it:

| What Happened on Your Screen | Why It Happened | How to Fix It |
| :--- | :--- | :--- |
| 1. In Ten-Frame mode, typing `[▦]` shows empty frame | Forgot to enter initial quantity. | Load the number FIRST, then press `[▦]`. |
| 2. Step counter in 4-stack adds `0` instead of constant | Stack dropped `0` from empty $Z$ to $Y$. | Switch to 2-Stack (`2-LV`) or use `[g] [REP]`. |
| 3. Place Value `[PV]` query returns error | Entered query place before subject number. | Enter number, press `[ENTER]`, then query place value. |
| 4. Ten-frame step key `[.]` adds decimal point to number | Pressed digit key while typing digits. | Tap `[.]` alone to step the counter by 1. |
| 5. Child writes `41` for teen number fourteen | Auditory reversal of "four" in 14. | Use the Rekenrek screen to show 1 ten + 4 ones. |
| 6. Number line arc jumps backward on addition | Typed second number before starting number. | Enter start coordinate first, then `[ENTER]`, then jump. |
| 7. Big number heartbeats overwritten during multiply | Pressed `[C]` between multi-step factors. | Let the stack lift; do not press Clear between `[×]` steps. |
| 8. Querying tens place of `405` gives `0` | Confused digit with total magnitude. | Query `10` $\to$ shows `0`: explain that zero is a placeholder. |
| 9. Worried returning from sandbox to `[NUM]` lost data | Assumed mode switch clears the stack. | Press `[NUM]`: the operational stack is preserved. |
| 10. Querying hundredths shows `0` on $\$345.67$ | Used `100` instead of `.01` for decimal place value. | Use `.01` for hundredths ($1/100$); `100` queries hundreds. |

### 3.9.8 Blind Digit Typing vs. Visible Place-Value Bundling

Now that you have explored all four visual sandboxes (`[▦]`, `[g] [COUNT]`, `[f] [LINE]`, and `[PV]`), compare how a standard single-line calculator handles counting, ten-bridging, and place-value inspection versus the SC-6's visual studios:

| Challenge / Real-World Task | The Algebraic Calculator Trap (Infix) | Algebraic Keystrokes & Clutter | The StackCalc + Blocks Method (RPN Stack + Visual Studio) | StackCalc Keystrokes | The Stack Advantage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Stadium Light Wattage:** Chained multi-bank load sum: $(30 \times 1500) + (10 \times 2000)$ | A basic four-function calculator evaluates strictly left-to-right ($30 \times 1500 + 10 = 45,010 \times 2000 = 90,020,000\text{ W}$!), while on a scientific infix screen, typing the full line hides both light-bank subtotals ($45,000$ and $20,000$) until you press `=`. Students wrap each product in defensive parentheses just to keep the two groups visually separate. | `( 3 0 × 1 5 0 0 ) + ( 1 0 × 2 0 0 0 ) =` (23 keystrokes with defensive brackets; intermediate subtotals hidden) | **RPN Parallel Accumulation:** Evaluates bank A ($45,000$) and bank B ($20,000$) into visible registers $Y$ and $X$, then combines them in a single keystroke with zero parentheses. | `30 [ENTER] 1500 [×] 10 [ENTER] 2000 [×] [+]` (16 keystrokes) | **Both Subtotals Visible:** Both power bank subtotals remain in plain sight on the stack before combining. |
| **Ten-Frame Bridging:** Mental addition across ten boundary: $8 + 5 = (8 + 2) + 3 = 10 + 3$ | Single-line algebraic screens hide the intermediate landmark of 10. Pressing equals triggers a black-box answer without showing the ten-frame filling up. | `8 + 2 + 3 =` (Single-line display; intermediate ten lost) | **Ten-Frame Studio Bridge (`[▦]`):** Interactive grid drops 2 counters into Frame 1, flashing the completed ten at 10, then cascades remaining 3 counters into Frame 2. | `8 [ENTER] 2 [+] 3 [+]` (Visual ten-frame flash at $X = 10$) | **Visual Ten Landmark:** Concrete spatial grouping eliminates finger-counting and reveals why bridging ten works. |
| **Place Value Explorer:** Extracting tens and hundreds from $4,725$ without scratch paper | Infix calculators have no positional extraction keys. Students must manually divide by 10, subtract the integer part, and multiply back—destroying the original number. | `4 7 2 5 / 1 0 =` $\to 472.5$, `- 4 7 0 =` $\to 2.5$ (Destructive multi-step division) | **Preserved Target Engine (`[PV]`):** Dedicated hardware instruction preserves target $4,725$ in Register $Y$, suppressing stack lift so subsequent checks execute instantly. | `4725 [ENTER] 10 [PV] 100 [PV] 1000 [PV]` (Chained single-stroke checks) | **Zero Value Destruction:** Target number remains permanently parked in Register $Y$; checks tens ($2$), hundreds ($7$), thousands ($4$) in rapid cadence. |
| **Rhythmic Cadence Counting:** Even number ladder up to 20 | Infix constant equals-key mode (`2 + 2 = = =`) relies on hidden register state that fails if any non-equals key is accidentally touched. | `2 + 2 = = = = =` (Flaky state; hidden accumulator easily cleared) | **Stack Constant Duplication:** In 2-LV mode, Register $Y$ preserves constant $2.0$. Each tap of `[+]` advances count by 2 with deterministic mechanical precision. | `2 [ENTER] 2 [+] [+] [+] ...` (100% reliable stack retention) | **Visual Stepping Ladder:** Learners see constant waiting on Level $Y$ while Level $X$ climbs in cadence with physical block towers. |

---

## 3.10 Where to Go Next: Companion Workbook Quests & Kitchen-Table Challenges

> *For 24 additional worked problems with full 4-register stack tables, see Chapter 3 of the [SC-6 Elementary Companion Problem & Activity Workbook](../curriculum/sc6-elementary-companion-workbook.md).*

Ready to put your Ten-Frame, Rekenrek, Number Line, and Place Value tools to the test? Pair this chapter with the **[Big Ideas Math Middle School Supplement](../curriculum/big-ideas-middle-school-sc6-workbook.md) — Unit 2, Section 2.4 (Adding, Subtracting & Multiplying Decimals)** and **Unit 6, Section 6.1 (Positive & Negative Integers, Opposites & Zero Pairs)**, along with **Unit 3 of the 12-Unit Curriculum Guide** and the **StackCalc Student Workbook**—or try these three challenges right now:

1. **Hands-On Explorer (The Coin-Jar & Workshop Drawer Decimal Challenge):** First, grab a handful of dimes ($0.10$) and pennies ($0.01$), enter the total into Register $Y$, and extract the Tenths (`0.1 [PV]`) and Hundredths (`0.01 [PV]`) digits on your SC-6. Then test the **Gridfinity Workshop Drawer Clearance** (`170.5 [ENTER] 4 [ENTER] 42 [×] [-]` $\to \mathbf{2.5\text{ mm}}$).
2. **"Bet Your Family!" (The Secret Digit X-Ray & Sub-Zero Hop):** Ask a family member to type any secret 6-digit number onto your SC-6 and press `[ENTER]`, then cover the $Y$ register with a sticky note and type `0`. Reveal their secret number one digit at a time using `100000 [PV]` down to `1 [PV]`—and then switch to `[f] [LINE]` (`3 [ENTER] 5 [-]` $\to \mathbf{-2^\circ\text{C}}$) to show how the Andean hummingbird's nighttime torpor hops left past zero.
3. **Rapid-Fire Sprint (The 30-Second Bridging Race):** Open the Ten-Frame Sandbox (`[▦]`) and see how many "9-plus" and "8-plus" teen bridging problems ($9 + 6$, $8 + 7$, $9 + 8$) you can decompose across 10 in 30 seconds before logging your score in your *Timed Proficiency Trials* passport.

---

## 3.11 Chapter Summary & Looking Ahead

The tools and models in this chapter link physical counting directly to the base-10 number system:

1. **From Trays to Numbers:** Physical Ten-Frame trays and Rekenrek racks translate directly into the high-contrast vector sandboxes of the SC-6 (`[▦]`, `[g] [COUNT]`).
2. **Spotting Groups at a Glance (Subitizing):** Anchors of 5 and 10 eliminate finger counting, allowing you to recognize quantities at a glance.
3. **Bridging Ten:** Decomposing additions across the decade ($8 + 5 = 8 + 2 + 3 = 10 + 3 = 13$) provides a reliable foundation for mental math.
4. **Step Counter Mechanics:** Constant step addition is verified through 2-stack register retention and 4-stack `[g] [REP]` replication.
5. **Spatial Travel & `[f] [LASTX]` Reversals:** The Open Number Line (`[f] [LINE]`) visualizes arithmetic as forward and backward jump arcs that you can reverse in one tap with `[f] [LASTX]`.
6. **Structural Decomposition:** The Place Value Engine (`[PV]`) slices numbers into their constituent powers of ten, preserving Register $Y$ across chained queries.
7. **Cosmic Horizons:** Place value structures scale directly from single unit cubes to solar system distances.

Once you can bundle single units into tens, hundreds, and thousands, what happens when we arrange equal groups into rectangular arrays? In **[Chapter 04: Whole Number Operations & Skip-Counting Ladders](sc6/04-operations-skip-counting.md)**, young Carl Friedrich Gauss shows us how multiplication and skip-counting reveal patterns across the universe.

---

# Chapter 4: Whole Number Operations & Skip-Counting Ladders

## 4.1 How 9-Year-Old Carl Friedrich Gauss Outsmarted His Teacher in Seconds (and Why Multiplication Is a Physical Rectangle, Not a Memorized Song)

In 1786, inside a crowded elementary classroom at the St. Katharinen-Volksschule in Brunswick, Germany, schoolmaster J.G. Büttner and his young assistant Martin Bartels presided over roughly a hundred pupils *([Sartorius von Waltershausen, 1856](sc6/appendix-c-formulas-and-conversions.md#cite-sartorius1856))*. Whenever Büttner wanted an hour of quiet, he assigned his arithmetic class a long summation problem to compute on their handheld slates.

Walking to the front of the room, he assigned the class a daunting series: *Add every integer from 1 to 100 on your slates.*

$$\mathbf{1 + 2 + 3 + 4 + 5 + \dots + 98 + 99 + 100 = \ ?}$$

The schoolmaster expected his pupils to spend the rest of the hour bent over their slates in laborious step-by-step addition.

As Gauss's friend and biographer Wolfgang Sartorius von Waltershausen recorded in *Gauss zum Gedächtniss* (1856) *([Sartorius von Waltershausen, 1856](sc6/appendix-c-formulas-and-conversions.md#cite-sartorius1856))*, the problem had barely been stated when nine-year-old Carl Friedrich Gauss *([Gauss, 1809](sc6/appendix-c-formulas-and-conversions.md#cite-gauss1809))* walked to the master's table, laid his slate down on top of the empty pile, and spoke the famous words in his native Low German dialect:

$$\text{\Large\textbf{„Ligget se!“}} \quad \text{("There it lies!")}$$

While the other boys scribbled rows of intermediate sums for the remainder of the hour, Gauss sat quietly with his arms folded. When the slates were finally turned over and inspected, almost all the longer calculations contained errors—yet young Gauss’s slate held a single number, written without a scratch of intermediate work: **5,050** *([Sartorius von Waltershausen, 1856](sc6/appendix-c-formulas-and-conversions.md#cite-sartorius1856))*.

How did a nine-year-old solve the series almost instantly?

Gauss did not sing times tables in his head. He did not count on his fingers. He looked at the problem *spatially*. He noticed that the numbers could be folded in half like a piece of paper, pairing the extreme ends into identical sums:
$$1 + 100 = 101, \quad 2 + 99 = 101, \quad 3 + 98 = 101, \quad \dots \quad 50 + 51 = 101$$

There were exactly fifty pairs of $101$. And fifty groups of $101$ is not fifty tedious additions; it is a **geometric rectangle** measuring $50$ units wide by $101$ units tall:
$$50 \times 101 = 5,050$$

This is the key insight that conventional elementary school math so often conceals: **multiplication is not an arbitrary song you recite from memory; multiplication is a physical rectangle of space.** When you arrange tiles into equal rows and columns, the product is simply the physical area of the grid.

On the **StackCalc SC-6**, we honor Gauss's spatial insight. Using our physical **24-Tile Four-Color Array Studio** (or pooling six desk kits into a 144-tile classroom set), you prove the commutative, associative, and distributive properties with your hands. And on the calculator keypad—working in standard whole-number (`[NUM]`) or currency (`[$]`) view alongside the core operators (`[+]`, `[-]`, `[×]`, `[÷]`) and stack controls (`[ENTER]`, `[x⇄y]`, `[C]`, `[<-]`)—you command three computational signature keys: **Constant Repeat (`[g] [REP]`)** for rhythmic skip-counting ladders, **Quotient & Remainder (`[g] [÷R]`)** for instant simultaneous quotient and remainder display, and **Last Number Recall (`[f] [LASTX]`)** for self-checking inverse arithmetic without scratch paper. As you work through this chapter, you will see how `[g] [REP]`, `[g] [÷R]`, and `[f] [LASTX]` turn your four-level stack into a hands-on multiplication and division studio.

---

![Field trip bus division: 145 students / 45-seat bus → Quotient 3, Remainder 10](../assets/manuals/screenshots/sc6_divr_quotient_remainder.png)

## 4.2 Hands-On Studio: 24-Tile Four-Color Array Studio & Map Theory

When you first learn multiplication, it might seem like a song to memorize. But multiplication is really **spatial equal groups**, **rectangular area arrays**, and **color-coded maps** you can build with your hands.

| Topic | Physical Manipulative Kit | Visual Screen Mode | RPN Operational Stack |
|---|---|---|---|
| **1. Hands-On Blocks** | 24-Tile Four-Color Array Studio | Physical interlocking tiles and 90° array rotation | Tactile array perception |
| **2. Visual Screen** | 4-Color Quadrant Partitioning & Map Theory | High-contrast LCD vector dot-matrix grid | Visual area model representation |
| **3. Number Stack** | Four-Register RPN Stack ($T, Z, Y, X$) | `Y [ENTER] X [×]` two-number drop | Chained parenthesis-free speed |

The StackCalc physical block kit replaces loose single-purpose blocks with the **24-Tile Four-Color Counting & Array Studio**:

Each student desk kit provides 24 precision interlocking stacking tiles ($19.0 \times 19.0 \times 7.0\text{ mm}$ visible height, $8.85\text{ mm}$ overall with the top stacking lip) arranged across four distinct color palettes:
1. **Archival White** (crisp matte finish)
2. **Cobalt Blue** (deep saturated tone)
3. **Radiant Gold** (warm amber tone)
4. **Slate Gray** (technical neutral tone)

With 6 tiles per color ($4 \times 6 = 24\text{ tiles}$ per student kit, or 6 kits pooled together for a 144-tile $12 \times 12$ classroom set), each tile has a $1\text{U}$ visible height ($7.0\text{ mm}$), aligning with the $1/12\text{th}$ Fraction Studio tile so that 12 vertically stacked tiles match the $84.0\text{ mm}$ master datum of the 1-Whole Fraction Tower. Smooth beveled edges let you snap tiles into flat arrays or stack them into 3D towers without sticking.

![24-Tile Four-Color Counting & Array Studio in Desktop Storage Case](../assets/manuals/counting_tiles_box_3x1x13u.png)

### 4.2.1 The Mathematical Harmony of $4 \times 6 = 24$
The number 24 divided into 4 colors creates rich mathematical properties for hands-on discovery:
1. **Super-Factorable Versatility:** The 24-tile kit factors cleanly into $1 \times 24$, $2 \times 12$, $3 \times 8$, and $4 \times 6$ rectangular arrays.
2. **Four Complete $2 \times 3$ Sub-Arrays:** Each individual color contains **6 tiles**, which is both a $2 \times 3$ rectangular array and a staircase triangular number ($1 + 2 + 3 = 6$).
3. **From Desk Blocks to Giant Numbers:** By modeling foundational $2 \times 3$, $3 \times 8$, and $4 \times 6$ arrays physically on the desk, you build concrete intuition before scaling up to large multi-digit arrays on the SC-6 stack.

| Array Orientation | Grid Dimensions | Row Breakdown | Total Area |
| :--- | :--- | :--- | :--- |
| **Array A** | $3\text{ Rows} \times 8\text{ Columns}$ | 3 rows of 8 tiles ($8 + 8 + 8$) | **$3 \times 8 = 24\text{ tiles}$** |
| **Array B** | $4\text{ Rows} \times 6\text{ Columns}$ | 4 rows of 6 tiles ($6 + 6 + 6 + 6$) | **$4 \times 6 = 24\text{ tiles}$** |

### 4.2.2 Pythagoras's Secret: Why Odd Numbers Build Perfect Squares
Remember the L-shaped odd-number collars we built on our desk in Chapter 3 ($1 + 3 + 5 + 7 = 16$)? Over 2,500 years ago, Pythagoras and his students connected those exact L-shaped borders—which the Greeks called *gnomons*, after the L-shaped shadow arm on a sundial—directly to **multiplication arrays** inside your **24-Tile Four-Color Counting & Array Studio** and the $90^\circ$ **L-Frame Stage**! When you dock your tiles into the $90^\circ$ corner of the L-Frame Stage, adding consecutive odd numbers ($1 + 3 + 5 + 7$) doesn't just count upward—it grows a square multiplication array by $+1$ row and $+1$ column at the same time:
1. **Start with $1$ ($1 \times 1$):** Dock **1 White tile** snugly into the $90^\circ$ corner of the L-Frame Stage (or the bottom-left socket of your $6 \times 2$ Snapfinity lid). It is a tiny $1 \times 1 = \mathbf{1}$ square array.
2. **Add $3$ ($1 + 3 = 4$):** Take **3 Cobalt Blue tiles** and wrap them around the top and right edges of the White tile like an L-shaped corner border. Look down: your $1 \times 1$ array just grew into a **$2 \times 2 = \mathbf{4}$ square array**.
3. **Add $5$ ($1 + 3 + 5 = 9$):** Wrap an L-border of **5 Radiant Gold tiles** around the outer corner of the blue square. It locks into a **$3 \times 3 = \mathbf{9}$ square array**.
4. **Add $7$ ($1 + 3 + 5 + 7 = 16$):** Wrap **7 Slate Gray tiles** (your 6 Slate Gray tiles plus 1 spare White tile, using $16$ of your $24$ student kit tiles) around the gold square: it forms a **$4 \times 4 = \mathbf{16}$ square array**! Notice how the $3 \times 3$ square grows into a $4 \times 4$ square by wrapping an L-border of $7$ tiles ($3$ on top, $3$ down the side, and $1$ in the corner) around its outer edge—bridging addition of odd numbers directly to multiplication of equal side lengths.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `1 [ENTER] 3 [+]` | 0 | 0 | 0 | 4 | $1 + 3 = 4 = 2^2$ ($2 \times 2$ White + Blue square) |
| 2 | `5 [+]` | 0 | 0 | 0 | 9 | $+ 5 = 9 = 3^2$ ($3 \times 3$ Gold L-border added) |
| 3 | `7 [+]` | 0 | 0 | 0 | 16 | $+ 7 = 16 = 4^2$ ($4 \times 4$ Slate L-border added) |
| 4 | `[f] [√x]` | 0 | 0 | 0 | **4** | Square root confirms the $4 \times 4$ side length |

---

### 4.2.3 The 24-Tile Rectangular Array Studio & Multiplication Properties

![Commutative Property of Multiplication: 3x8 Array Rotated to 8x3 on Tabletop](../assets/manuals/counting_tiles_array_3x8.png)

Once you see that any multiplication problem is a physical rectangle of tiles, the three great laws of multiplication—the **Commutative**, **Associative**, and **Distributive** properties—stop sounding like vocabulary words and become things you can prove with your hands in seconds.

First, test the **Commutative Property ($\text{Rows} \times \text{Columns} = \text{Columns} \times \text{Rows}$)** right on your desk: snap together a solid rectangular mat of 3 rows of 8 tiles ($3 \times 8 = 24$), then physically pick up the mat and rotate it by $90^\circ$ on the tabletop so you see 8 rows of 3 tiles ($8 \times 3 = 24$). Did the number of tiles change? Not a single tile was added or removed! On the SC-6 stack, you can place both orientations side by side: first multiply 3 rows of 8 by pressing `3 [ENTER] 8 [×]` to put $\mathbf{24}$ on Shelf $X$, and then multiply 8 rows of 3 by pressing `8 [ENTER] 3 [×]` so the rotated $\mathbf{24}$ lands on Shelf $X$ while the original $\mathbf{24}$ waits right next to it on Shelf $Y$.

| Keystroke | Register T | Register Z | Register Y | Register X (Display) |
| :--- | :--- | :--- | :--- | :--- |
| `[3] [ENTER]` | 0 | 0 | 3 | 3 |
| `[8] [×]` | 0 | 0 | 0 | 24 |
| `[8] [ENTER]` | 0 | 24 | 8 | 8 |
| `[3] [×]` | 0 | 0 | 24 | 24 |

Look at `Register Y` and `Register X` at the bottom of that table: both hold `24`! You see with your own eyes and feel with your own hands that spinning a rectangle never changes its area.

Next, what happens when you stack flat rectangles on top of each other into a 3D box? That brings us to the **Associative Property (grouping 3 factors in any order: $(3 \times 4) \times 3 = 3 \times (4 \times 3)$)**. On your desk, start with two layers of $3 \times 4$ tiles ($12$ tiles per layer, $24$ tiles total), and then scale up on your SC-6 to a three-layer block box ($\text{Length} = 3,\; \text{Width} = 4,\; \text{Height} = 3 \implies 36\text{ blocks}$). Because each tile has $7.0\text{ mm}$ of visible height, 3 stacked tiles equal $21.0\text{ mm}$:

$$\text{Box Volume} = \text{Length} \times \text{Width} \times \text{Height} = (3 \times 4) \times 3 = 3 \times (4 \times 3) = 36\text{ blocks}$$

Why do we practice two different ways of building and multiplying the exact same 3D block prism?
- **Horizontal Floor-Layer First ($(3 \times 4) \times 3$):** First lay a flat $3 \times 4$ floor mat on your desk ($12$ tiles per horizontal floor), then stack $3$ identical floors upward ($12 \times 3 = 36$). Architects use this floor-layer approach when calculating total building size from one floor's footprint multiplied by the number of stories: pressing `[3] [ENTER] [4] [×] [3] [×]` multiplies the $3 \times 4$ floor footprint into `12` and then scales by `3` stories to reach $X = \mathbf{36}$.
- **Vertical Wall-Slice First ($3 \times (4 \times 3)$):** First stand up a vertical $4 \times 3$ wall slice ($12$ tiles per vertical slice), then line up $3$ identical wall slices side-by-side ($12 \times 3 = 36$). Cargo spacecraft planners use this wall-slice approach when counting how many vertical supply walls fit down the length of a module (`4 [ENTER] 3 [×] [f] [LASTX] [×]` $\longrightarrow X = \mathbf{36}$—notice how `[f] [LASTX]` pulls the second `3` right back onto the ground floor without re-typing it).

| Keystroke | Register T | Register Z | Register Y | Register X (Display) |
| :--- | :--- | :--- | :--- | :--- |
| `[3] [ENTER]` | 0 | 0 | 3 | 3 |
| `[4] [×]` | 0 | 0 | 0 | 12 |
| `[3] [×]` | 0 | 0 | 0 | 36 |

Both physical constructions use the exact same blocks and land on $X = 36$ with zero parentheses.

Finally, what do you do when a multiplication rectangle is too big to multiply in your head all at once—like $12 \times 12$? You use the **Distributive Property & Four-Part Area Models**, slicing the big rectangle along the **10-lines** into smaller rectangles whose areas you already know! Start on your desk by arranging a $4 \times 4 = 16$-tile square using four $2 \times 2$ color quadrants (4 white, 4 blue, 4 gold, and 4 gray tiles: $4 + 4 + 4 + 4 = 16$). Now imagine doing the exact same thing with a $12 \times 12$ square by splitting each side of $12$ into **$10 + 2$**. Slicing between the $10$ and the $2$ divides the big $12 \times 12$ square into four friendly color zones:
$$(10 + 2) \times (10 + 2) = (10 \times 10) + (10 \times 2) + (2 \times 10) + (2 \times 2) = 100 + 20 + 20 + 4 = 144$$

| Partial Product Quadrant | Dimensions | Area Value |
| :--- | :--- | :--- |
| **Upper-Left ($10 \times 10$)** | $10\text{ rows} \times 10\text{ columns}$ | $100\text{ square units}$ |
| **Upper-Right ($10 \times 2$)** | $10\text{ rows} \times 2\text{ columns}$ | $20\text{ square units}$ |
| **Lower-Left ($2 \times 10$)** | $2\text{ rows} \times 10\text{ columns}$ | $20\text{ square units}$ |
| **Lower-Right ($2 \times 2$)** | $2\text{ rows} \times 2\text{ columns}$ | $4\text{ square units}$ |
| **Total Distributive Area** | $(10 + 2) \times (10 + 2) = 12 \times 12$ | **$144\text{ square units}$** |

![Four-Color Distributive Area: (10 + 2) x (10 + 2) = 144 Square Units across 4 Quadrants](../assets/manuals/counting_tiles_distributive_4color.png)

On the SC-6, you can build both $(10 + 2)$ sides and multiply them with zero parentheses by pressing `[1][0] [ENTER] [2] [+] [1][0] [ENTER] [2] [+] [×]`, which forms `12` on Shelf $Y$ and `12` on Shelf $X$ before multiplying them into $X = \mathbf{144}$.

| Keystroke | Register T | Register Z | Register Y | Register X (Display) |
| :--- | :--- | :--- | :--- | :--- |
| `10 [ENTER]` | 0 | 0 | 10 | 10 |
| `[2] [+]` | 0 | 0 | 0 | 12 |
| `10 [ENTER]` | 0 | 12 | 10 | 10 |
| `[2] [+]` | 0 | 0 | 12 | 12 |
| `[×]` | 0 | 0 | 0 | 144 |

Those four color zones turn a big $12 \times 12$ multiplication problem into four bite-sized pieces ($100 + 20 + 20 + 4 = 144$) you can add in your head! (And once you build the first `12` in Register $X$, you can also duplicate and square it in two clicks: `[ENTER] [×]` $\to$ `144`.)

Once you see that you can slice any rectangle into two smaller rectangles, you unlock two everyday kitchen-table shortcuts for multiplying two-digit numbers and store prices in your head:
- **Splitting Tens and Ones ($8 \times 53$):** Suppose 8 buses each carry 53 campers. Instead of reaching for a pencil, picture a rectangle 8 rows tall and 53 columns wide, and slice the width into **$50 + 3$**. Now you have an $8 \times 50$ rectangle ($400$) next to an $8 \times 3$ rectangle ($24$):
  $$8 \times 53 = 8(50 + 3) = (8 \times 50) + (8 \times 3) = 400 + 24 = \mathbf{424}$$
  On your SC-6 stack, compute both rectangles and fuse them with zero parentheses: `8 [ENTER] 50 [×] 8 [ENTER] 3 [×] [+]` $\longrightarrow$ **`424`**.
- **The Store Price-Tag Trick ($6 \times \$9.90$):** Why do stores price items at $\$9.90$ instead of $\$10.00$? Because `.90` looks smaller—and it looks annoying to multiply! To outsmart the price tag when buying 6 maker kits at $\$9.90$ each, pretend each kit costs a clean **$\$10.00$**, and then subtract the **$\$0.10$** overcharge on each of the 6 kits:
  $$6 \times \$9.90 = 6(\$10.00 - \$0.10) = (6 \times \$10.00) - (6 \times \$0.10) = \$60.00 - \$0.60 = \mathbf{\$59.40}$$
  On your SC-6 stack: `6 [ENTER] 10 [×] 6 [ENTER] 0.10 [×] [-]` $\longrightarrow$ **`59.40`**.

### 4.2.4 The Voxel Game Studio & Solar Rover Array Lab
To see how rectangular arrays power real engineering and game design, step into the shoes of the lead level designer in a pixel-art game studio and solar-rover lab! Instead of counting power cells and LEDs one by one, you build rectangular arrays, rotate solar wings on your tabletop, wire up arcade scoreboards, and subtract doorway cutouts from studio walls.

To power an autonomous Mars rover, your first task at the lab workbench brings back the 24-tile rotation we tested at the start of this section—except now each tile represents a high-efficiency photovoltaic cell on a rectangular solar wing! First, snap together 3 horizontal rows of 8 counting tiles on your desk mat to model the wide wing deployment. Instead of pointing your finger to count all 24 cells one by one, multiplication measures the whole rectangle in a single snap (`3 × 8`): when you key `[3]` into active Register $X$, lift the 3 rows onto Holding Shelf $Y$ with `[ENTER]`, and multiply by the 8 columns per row via `3 [ENTER] 8 [×]`, the stack drops to show **`24`** solar cells on Ground Shelf $X$ ($X = 24$). Next, to fit that solar wing inside a narrow vertical rocket nose cone for launch, grip your $3 \times 8$ tile array on the rover workbench and rotate it by $90^\circ$ so it stands tall as **8 rows of 3 tiles**. Without adding or removing a single solar cell, does rotating the wing change its power output? You check the rotated $8 \times 3$ array on the stack by pressing `8 [ENTER] 3 [×]`, which parks 8 into Register $Y$, multiplies by 3 on the ground floor, and leaves **`24`** on the daylight screen ($X = 24\text{ cells}$)—confirming once again that spinning a rectangular array $90^\circ$ swaps its rows and columns ($3 \times 8 = 8 \times 3 = 24$) while keeping every single cell intact!

Now that the rover wing is packed into the nose cone, you walk over to the voxel game studio to wire up a custom LED scoreboard made of 9 rows with 7 RGB light tiles in each row. Place 3 rows of 7 counting tiles ($21$ tiles) on your desk mat to see one-third of the scoreboard, then scale up to all 9 rows on the stack: pressing `9 [ENTER] 7 [×]` lifts the 9 rows into Register $Y$ and multiplies by 7 LEDs per row, lighting up **`63`** glowing pixels ($X = 63$). *(Want to prove $63 \div 7 = 9$ without re-typing `7`? Tap `[f] [LASTX] [÷]`!)*

What if you need to multiply $36 \times 25$ in your head in under two seconds while sizing a pixel texture grid? Picture quarters in your pocket: **4 quarters make 1 dollar ($100\text{ cents}$)**, which means $25$ is simply $100 \div 4$. So instead of multiplying $36 \times 25$ the long way, just divide $36$ by $4$ (to find how many 4-quarter dollars you have) and multiply by $100$! Divide 36 by 4 and scale by 100 on the stack by pressing `36 [ENTER] 4 [÷] 100 [×]`: `36 [ENTER] 4 [÷]` splits 36 quarters into 9 whole dollars, and `100 [×]` turns 9 dollars into **`900`** cents ($X = 900$).

And what if you are painting a rectangular game-studio wall measuring $15\text{ ft} \times 12\text{ ft}$, and that wall has a large rectangular sliding doorway measuring $18\text{ ft} \times 6\text{ ft}$ that doesn't need paint? How do you find the painted area—written $(15 \times 12) - (18 \times 6)$—without touching a parenthesis key? Watch Floor $Z$ act as your automatic upper balcony, holding the $180\text{ sq ft}$ wall area while you multiply the $108\text{ sq ft}$ doorway area on the ground floor: pressing `15 [ENTER] 12 [×] 18 [ENTER] 6 [×] [-]` subtracts the doorway from the wall to display **`72`** square feet.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `15 [ENTER] 12` | 0 | 0 | 15 | 12 | Enter first factor pair: 15 into $Y$, 12 into $X$ |
| `[×]` | 0 | 0 | 0 | 180 | Evaluate wall area: $15 \times 12 = 180$ in Register $X$ |
| `18 [ENTER] 6` | 0 | 180 | 18 | 6 | Stack lifts 180 to $Z$; enter 18 into $Y$, 6 into $X$ |
| `[×]` | 0 | 0 | 180 | 108 | Evaluate doorway area: $18 \times 6 = 108$; 180 drops to $Y$ |
| `[-]` | 0 | 0 | 0 | 72 | Subtract areas: $180 - 108 = 72$ in active display |

The final display reads $X = \mathbf{72}$ square feet of wall to paint!

---

### 4.2.5 The Four-Color Map Theorem Station Game
In 1976, mathematicians Kenneth Appel and Wolfgang Haken proved a famous puzzle that had stumped mapmakers for over a century: **no more than four colors are ever needed** to color any flat map so that no two bordering countries share the same color!

**Station Game: "Four-Color Map Showdown"**
* **Players:** 2 to 4 players.
* **Rules:** Players take turns snapping a counting tile onto the table grid to expand a connected "country". A placed tile may **never share a flat side edge** with a tile of the same color (touching at diagonal corners is legal).
* **The Challenge:** Try to trap your opponent so they think they need a 5th color—and discover why 4 colors can always solve the map.

## 4.3 Addition & Subtraction Dynamics: Regrouping Without Fear

Before diving into skip-counting ladders and remainder division, let's see how the SC-6 stack and your place-value blocks turn tricky multi-digit addition and subtraction into smooth, visual steps.

### 4.3.1 Why Traditional "Column Borrowing" Feels Like a Trap
In traditional arithmetic worksheets, multi-digit subtraction ($92 - 38$) is often taught as a mechanical rule:
1. "Look at the ones column: $2 - 8$. You can't take 8 from 2."
2. "Cross out the 9, make it an 8."
3. "Put a little 1 next to the 2 to make it 12."
4. "$12 - 8 = 4$, and $8 - 3 = 5$. Answer: 54."

When you just cross out digits on paper, it is easy to forget *why* it works: that "little 1" isn't just a mark—it is a physical **10-rod** unbundled into 10 unit cubes. Even better, on your SC-6 you can use two mental-math shortcuts that skip column borrowing altogether!

First is the **Round-Landmark Compensation Trick ($92 - 38$)**: imagine paying for a $38\text{-cent}$ sticker when you have $92\text{ cents}$ in your pocket. Instead of counting out 38 pennies, you hand the cashier **4 dimes ($40\text{ cents}$)**—leaving $92 - 40 = 52\text{ cents}$ in your pocket—and the cashier hands you **$2\text{ cents}$ change** ($52 + 2 = 54$)! Because $38$ is just $2$ steps shy of the round landmark $40$, subtracting $40$ and adding $2$ back skips borrowing completely:
$$92 - 38 = (92 - 40) + 2 = 52 + 2 = 54$$
Try that exact two-step rhythm on the SC-6 stack by pressing `92 [ENTER] 40 [-] 2 [+]`, which subtracts `40` to reach `52` and adds the `2` cents of change to display $X = \mathbf{54}$.

Second is **Hop-by-Hop Bridging ($47 + 38$)**: when adding $47 + 38$ in your head, split $38$ into three friendly hops ($30 + 3 + 5$). First add the 3 tens ($47 + 30 = 77$), next hop $+3$ to lock into the round decade $80$, and finally add the remaining $5$:
$$47 + 30 = 77 \quad \longrightarrow \quad 77 + 3 = 80 \quad \longrightarrow \quad 80 + 5 = 85$$
Watch the stack trace your mental hops as you key in `47 [ENTER] 30 [+] 3 [+] 5 [+]` to land on $X = \mathbf{85}$.

---

## 4.4 Constant Repeat: Rhythmic Skip-Counting Ladders (`[g] [REP]`)

How do you build rock-solid fluency with your times tables? Not by staring at a wall chart, but by climbing **rhythmic skip-counting ladders** ($7, 14, 21, 28 \dots$) while laying down rows of tiles on your desk!

On an ordinary calculator, trying to skip-count with `+ 7 = = =` is fragile—if you bump any other key, the hidden constant vanishes. And on older scientific RPN calculators, locking a constant into the top shelf required pressing `[ENTER]` three times in a row (`7 ENTER ENTER ENTER`).

Your SC-6 makes skip-counting effortless with **Constant Repeat (`[g] [REP]`)** (`[g]` then `[x⇄y]`). When you type a step size like `[7]` and press `[g] [REP]`, the calculator copies `7` onto **all four floors of the elevator ($T, Z, Y, X$) at once**!

Why does filling all four shelves turn `[+]` into an unstoppable skip-counting ladder? Remember the Top-Shelf Secret from Chapter 2: whenever an operation drops the stack, **Penthouse Floor $T$ leaves a copy of itself behind**. So every single time you tap `[+]`, a fresh `7` rides down from the roof to Shelf $Y$, ready for your next tap!

### 4.4.1 Climbing Skip-Counting Ladders with `[g] [REP]`

Let's start by climbing the **Sevens Ladder**—the same rhythm that counts the days in 1, 2, 3, or 10 weeks. First type `[7]` and press `[g] [REP]` (`[g]` then `[x⇄y]`) so every shelf ($T, Z, Y, X$) holds `7`, and then tap `[+]` in a steady rhythm as you place 7-tile rows onto your desk:

| Keystroke | Register T (Constant) | Register Z | Register Y | Register X (Ladder) |
| :--- | :--- | :--- | :--- | :--- |
| `[7]` | 0 | 0 | 0 | 7 |
| `[g] [REP]` | 7 | 7 | 7 | 7 |
| `[+]` | 7 | 7 | 7 | 14 |
| `[+]` | 7 | 7 | 7 | 21 |
| `[+]` | 7 | 7 | 7 | 28 |
| `[+]` | 7 | 7 | 7 | 35 |
| `[+]` | 7 | 7 | 7 | 42 |
| `[+]` | 7 | 7 | 7 | 49 |
| `[+]` | 7 | 7 | 7 | 56 |
| `[+]` | 7 | 7 | 7 | 63 |
| `[+]` | 7 | 7 | 7 | 70 |

Look at the `Register T (Constant)` column: `7` never leaves the Penthouse! You can march through the entire 7s table ($7, 14, 21, 28 \dots 70$) with single taps of `[+]`.

Once you have climbed the sevens, try the **Twelves (Dozens) Ladder**. The number 12 is everywhere in daily life—dozens of eggs, hours on a clock face, inches in a foot, and months in a year. Type `12`, press `[g] [REP]`, and tap `[+]` to climb the Dozens Ladder all the way to a gross ($144$):
$$\mathbf{24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144}$$

| Dozens ($1\text{–}4$) | Dozens ($5\text{–}8$) | Dozens ($9\text{–}12$) |
| :--- | :--- | :--- |
| $1\text{ Dozen} = 12\text{ eggs}$ | $5\text{ Dozen} = 60\text{ eggs}$ | $9\text{ Dozen} = 108\text{ eggs}$ |
| $2\text{ Dozen} = 24\text{ eggs}$ | $6\text{ Dozen} = 72\text{ eggs}$ | $10\text{ Dozen} = 120\text{ eggs}$ |
| $3\text{ Dozen} = 36\text{ eggs}$ | $7\text{ Dozen} = 84\text{ eggs}$ | $11\text{ Dozen} = 132\text{ eggs}$ |
| $4\text{ Dozen} = 48\text{ eggs}$ | $8\text{ Dozen} = 96\text{ eggs}$ | $12\text{ Dozen} = \mathbf{144}\text{ (1 Gross!)}$ |

What if you want to **double** a number over and over on a **Powers-of-Two Doubling Ladder**—the way dividing cells, computer memory chips, or laser grids grow? Because pressing `[ENTER]` duplicates whatever sits on Shelf $X$ up into Shelf $Y$, the two-key rhythm **`[ENTER] [+]`** doubles any number on the spot: start with `[2]`, then tap `[ENTER] [+]` to get **`4`**, `[ENTER] [+]` to get **`8`**, `[ENTER] [+]` to get **`16`**, `[ENTER] [+]` to get **`32`**, and keep climbing through **`64, 128, 256, 512, 1024`**! (Or use `2 [g] [REP] [×] [×] [×]...` to multiply by 2 on every single tap!)

### 4.4.2 The Mountain Rescue Rhythmic Ladder: Additive Steps vs. Doubling Grids
Now helicopter up to an alpine search-and-rescue base camp to see how those two ladders work side by side! Climbing steep mountain ridges and expanding aerial drone searches require two different kinds of ladders: an **additive skip-counting ladder** (`[g] [REP]` with `[+]`) that climbs by the same vertical step every time, and a **geometric doubling ladder** (`[ENTER] [+]`) that doubles the search grid every hour.

As your search-and-rescue team climbs a snowy ridge, the lead mountaineer plants a neon trail flag every 3 vertical meters. Instead of typing `+ 3` over and over, Constant Repeat (`[g] [REP]`) copies `3` into all four registers ($T, Z, Y, X$) so every single tap of `[+]` climbs another 3-meter rung! Snap together 3 rungs of 3 counting tiles ($9$ tiles) on your desk mat and chant: *3, 6, 9 meters!* Now climb all 9 checkpoints on the stack by pressing `3 [g] [REP] [+] [+] [+] [+] [+] [+] [+] [+]`, which feeds a fresh `3` down from the Penthouse roof on every tap to reach **`27`** meters.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[3] [g] [REP]` | 3 | 3 | 3 | 3 | Load constant 3 into all 4 registers to seed the rhythmic ladder |
| `[+]` | 3 | 3 | 3 | 6 | 1st step: $3 + 3 = 6\text{ m}$; Register $T$ preserves constant 3 |
| `[+]` | 3 | 3 | 3 | 9 | 2nd step: $6 + 3 = 9\text{ m}$; constant 3 drops from $T$ |
| `[+]` | 3 | 3 | 3 | 12 | 3rd step: $9 + 3 = 12\text{ m}$; rhythmically advancing up the ridge |
| `[+]` | 3 | 3 | 3 | 15 | 4th step: $12 + 3 = 15\text{ m}$; halfway station reached |
| `[+]` | 3 | 3 | 3 | 18 | 5th step: $15 + 3 = 18\text{ m}$; constant 3 preserved continuously |
| `[+]` | 3 | 3 | 3 | 21 | 6th step: $18 + 3 = 21\text{ m}$ elevation waypoint |
| `[+]` | 3 | 3 | 3 | 24 | 7th step: $21 + 3 = 24\text{ m}$ elevation waypoint |
| `[+]` | 3 | 3 | 3 | 27 | 8th step: $24 + 3 = 27\text{ m}$; 9th multiple reached |

If you play pattern detective and add the digits of every two-digit number in Register $X$ ($1+2=3$, $1+5=6$, $1+8=9$, $2+1=3$, $2+4=6$, $2+7=9$), you discover that the digit sums of the 3s ladder always cycle through **3, 6, 9**!

Once your climbers reach that $27\text{-meter}$ ridge outlook, dusk begins to fall, and the team launches aerial rescue drones! In Hour 0, a single scout drone scans a $1\text{ km}^2$ mountain sector. Every hour after that, backup drones join the formation and **double** the scanned area ($1 \to 2 \to 4 \to 8 \dots$). Place 1 counting tile on your desk, double it to 2, then 4, then 8, then 16 tiles to feel how much faster doubling grows than adding 3. Then ride the two-key doubling rhythm (`[ENTER] [+]`) across 6 hours on your SC-6: keying in `1 [ENTER] [+] [ENTER] [+] [ENTER] [+] [ENTER] [+] [ENTER] [+] [ENTER] [+]` duplicates and adds each hour's coverage until Ground Shelf $X$ reaches **`64`** square kilometers.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[1] [ENTER]` | 0 | 0 | 1 | 1 | Enter starting search area of $1\text{ km}^2$; duplicate into $Y$ |
| `[+]` | 0 | 0 | 0 | 2 | Hour 1: $1 + 1 = 2\text{ km}^2$ searched |
| `[ENTER] [+]` | 0 | 0 | 0 | 4 | Hour 2: Duplicate 2 and sum: $2 + 2 = 4\text{ km}^2$ |
| `[ENTER] [+]` | 0 | 0 | 0 | 8 | Hour 3: Duplicate 4 and sum: $4 + 4 = 8\text{ km}^2$ |
| `[ENTER] [+]` | 0 | 0 | 0 | 16 | Hour 4: Duplicate 8 and sum: $8 + 8 = 16\text{ km}^2$ |
| `[ENTER] [+]` | 0 | 0 | 0 | 32 | Hour 5: Duplicate 16 and sum: $16 + 16 = 32\text{ km}^2$ |
| `[ENTER] [+]` | 0 | 0 | 0 | 64 | Hour 6: Duplicate 32 and sum: $32 + 32 = 64\text{ km}^2$ |

By Hour 6, the fleet covers $64\text{ km}^2$ ($2^6 = 64$)!

---

## 4.5 Quotient & Remainder: Remainders You Can Hold (`[g] [÷R]`)

### 4.5.1 Why Decimals Hide the Story in Whole-Number Division

Suppose 6 friends are sharing 43 strawberries equally, and you want to know: *"How many strawberries does each friend get, and how many are left over on the plate?"*
- **The Regular Calculator Trap:** If you type `43 ÷ 6 =` on a phone or basic calculator, the screen spits out `7.16666666667`. What on earth is `0.16666666667` of a strawberry? That decimal hides the leftover strawberry!
- **The SC-6 Remainder-You-Can-Hold Solution (`[g] [÷R]`):** On your SC-6, press `43 [ENTER] 6 [g] [÷R]` (`[g]` then `[÷]`). Because your screen has **two side-by-side shelves ($Y$ and $X$)**, the calculator shows you *both* whole-number answers at the exact same time:
  - **Ground Shelf $X$ shows `7`:** the **Whole Quotient** (7 strawberries for each friend).
  - **Waiting Shelf $Y$ holds `1`:** the **Exact Remainder** (1 leftover strawberry sitting on the plate!).
- Want to bring the remainder to the front shelf? Tap `[x⇄y]`. Want to prove that $7 \times 6 + 1 = 43$ without re-typing a single digit? Tap `[f] [LASTX] [×] [+]` and watch `43` snap right back!

> **How `[g] [÷R]` Splits Division Across Your Two Shelves:**
> Put your starting Total on Shelf $Y$ and your Group Size on Shelf $X$, then press `[g] [÷R]`:
> - **Shelf $X$** shows **Whole Groups (Quotient $Q$)**—how many complete groups you can build.
> - **Shelf $Y$** holds **Leftovers (Remainder $R$)**—how many loose items remain.

### 4.5.2 Hands-On Discovery: Dealing 23 Tiles into Groups of 5 (`[g] [÷R]`)

Count out **23 Counting Tiles** onto your desk and deal them into stacks of **5 tiles each**. You can build **4 complete stacks of 5** ($4 \times 5 = 20$ tiles), and you will have **3 loose tiles** left over in your hand that aren't enough to make a 5th stack.

Now watch your SC-6 mirror the exact piles on your desk:
1. Type `23 [ENTER] [5] [g] [÷R]`. Right away, Ground Shelf $X$ displays **`4`** (your 4 complete stacks of 5), while Waiting Shelf $Y$ holds **`3`** (your 3 loose leftover tiles)!
2. Tap `[x⇄y]` to swap the shelves and bring the **`3`** leftover tiles into $X$ (and tap `[x⇄y]` again if you want to put Quotient `4` back in $X$ and Remainder `3` back in $Y$).
3. **The 3-Key Remainder Proof:** With Quotient `4` in $X$ and Remainder `3` in $Y$, tap `[f] [LASTX] [×] [+]`—`LASTX` recalls your group size (`5`), `[×]` multiplies $4 \times 5 = 20$, and `[+]` adds the `3` waiting on Shelf $Y$ to restore all **`23`** tiles!

| Keystroke | Register T | Register Z | Register Y | Register X (Display) |
| :--- | :--- | :--- | :--- | :--- |
| `23 [ENTER]` | 0 | 0 | 23 | 23 |
| `[5]` | 0 | 0 | 23 | 5 |
| `[g] [÷R]` | 0 | 0 | 3 | 4 |
| `[x⇄y]` | 0 | 0 | 4 | 3 |

---

### 4.5.3 Four Real-Life Remainder Puzzles

Once you see how `[g] [÷R]` separates full containers in Register $X$ from leftover items in Register $Y$, everyday sharing and packaging puzzles click into place across four classic scenarios.

First, imagine a family farm that gathers **147 fresh eggs** in the morning and packs them into **12-egg cartons** for the farmer's market. How many full cartons can they pack, and how many loose eggs are left over for the farm family's breakfast? Instead of dealing with a messy decimal, type `147` into Register $X$, press `[ENTER]` to lift the 147 eggs onto Waiting Shelf $Y$, type the carton size `12` onto Ground Shelf $X$, and tap `[g] [÷R]`. In a single stroke, the two shelves split the harvest cleanly in two: Ground Shelf $X$ displays **`12` full cartons** ($12 \times 12 = 144$ packed eggs), while Waiting Shelf $Y$ holds the **`3` loose eggs** left over! A quick tap of `[x⇄y]` swaps the two shelves so you can inspect the `3` leftover breakfast eggs right in the active display ($Y = 12,\; X = 3$), and tapping `[x⇄y] [f] [LASTX] [×] [+]` proves that $(12 \times 12) + 3 = 144 + 3 = 147$ eggs without re-typing a single digit.

Second, step from the farm into a robotics lab where the team has **86 rechargeable lithium cells**, and each **rover battery pack requires 6 cells**. Keying in `86 [ENTER] [6] [g] [÷R]` immediately shows **`14` full battery packs** in Register $X$ and **`2` spare cells** waiting in Register $Y$ (and a single tap of `[x⇄y]` brings `2` to the front).

Third, what happens when the items being divided are people who cannot be left behind? Suppose an elementary school is taking **380 students and chaperones** to the science museum in chartered buses that hold **54 passengers each**. When you key in `380 [ENTER] 54 [g] [÷R]`, Register $X$ shows **`7` full buses** ($7 \times 54 = 378$ people) and Register $Y$ shows **`2` people left over**. Pause and think: *can the school order just 7 buses?* No way—you can't leave 2 students waving from the school parking lot! Whenever a bus or van problem has a remainder greater than zero, you must round up by 1 and order **`8` buses** in total.

Fourth, `[g] [÷R]` even works when four siblings earn **$\$17.50$** raking autumn leaves and want to take whole-dollar bills first before splitting the coins! Keying in `17.50 [ENTER] [4] [g] [÷R]` shows **`4.00`** in Register $X$ (each sibling gets four $\$1$ bills) and **`1.50`** in Register $Y$ (the remaining $\$1.50$ in quarters and dimes still to be shared!).

### 4.5.4 The Space Station Cargo & Wildlife Expedition Depot
Now report for duty as logistics quartermaster at the Space Station & Field Science Depot! Whenever a harvest of eggs or a basket of crystal geodes arrives at the loading dock, you have to pack them into fixed-size crates—and use **Quotient & Remainder (`[g] [÷R]`)** to separate full containers (in Register $X$) from leftover items (in Register $Y$) in a single click.

In the depot's hydroponic farm module, crew members collect 185 fresh eggs to pack into 12-egg cartons. Why would a regular calculator's decimal answer (`15.41666...`) slow you down at the packing table? Because you need to know how many *whole* 12-egg cartons are full and how many *whole* eggs are left over! To divide all 185 eggs by 12 and inspect the leftover eggs, press `185 [ENTER] 12 [g] [÷R]`, which first places 15 full cartons in Register $X$ with 5 leftover eggs in Register $Y$, and then swaps **`15`** into the active display.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `185 [ENTER]` | 0 | 0 | 185 | 185 | Load 185 total harvested eggs into holding Register $Y$ |
| `12` | 0 | 0 | 185 | 12 | Enter carton capacity 12 into active Register $X$ |
| `[g] [÷R]` | 0 | 0 | 5 | 15 | Integer divide: $X = 15$ full cartons, $Y = 5$ leftover eggs |
| `[x⇄y]` | 0 | 0 | 15 | 5 | Swap registers to inspect remainder in active display ($X = 5$) |

Register $X$ shows $15$ full cartons right after `[g] [÷R]`, and tapping `[x⇄y]` reveals the $5$ leftover eggs ($Q = 15\text{ cartons}$, $R = 5\text{ eggs}$).

Right next to the farm pod, a planetary geology team unloads 140 sparkling quartz geodes to pack into padded 6-slot carrying cases. How many 6-slot cases are completely filled, how many geodes remain loose, and how can you prove not a single geode rolled under the table? When you divide the 140 geodes into 6-slot cases and swap shelves by pressing `140 [ENTER] 6 [g] [÷R]`, `[g] [÷R]` evaluates $140 \div 6$ in a single stroke to put **23 full cases** in $X$ and **2 extra geodes** in $Y$ before `[x⇄y]` brings **`23`** to the front ($Q = 23\text{ cases}$, $R = 2\text{ geodes}$). Now run the **3-Key `[f] [LASTX]` Proof:** right after `[g] [÷R]`, tap `[f] [LASTX] [×] [+]` and watch $(23 \times 6) + 2 = 140$ reappear on the ground floor!

What if a cargo manifest has a four-digit count like $3,458$ items packed into crates of $11$? On a regular calculator, $3,458 \div 11$ fills the screen with a repeating decimal tail ($314.363636\dots$) that hides the remainder. On your SC-6, pressing `3458 [ENTER] 11 [g] [÷R]` divides by `11` with `[g] [÷R]` to put Quotient **`314`** in Register $X$ and Remainder **`4`** in Register $Y$, and then swaps **`314`** into Register $X$. *(Tap `[f] [LASTX] [×] [+]` right after `[g] [÷R]` to see $(314 \times 11) + 4 = 3,458$ snap right back!)*

---

### 4.5.5 Three-Way Division & Interpreting Remainders in Real Life

You can verify and interpret division three ways—and see why the most important step in any real-world division problem is knowing **what the remainder means**:

1. **Long Division & The Division Algorithm Check:** Every whole-number division obeys the exact identity:
   $$\text{Quotient} \times \text{Divisor} + \text{Remainder} = \text{Dividend}$$
   After any `[g] [÷R]` calculation on the SC-6, Quotient $Q$ sits in Register $X$, Remainder $R$ waits in Register $Y$, and the Divisor sits in `LASTX`—so tapping `[f] [LASTX] [×] [+]` verifies the Division Algorithm in 3 clicks.
2. **Partial Quotients & Equal-Groups Tile Array:** Deal your Counting Tiles into equal rows on the tabletop. The completed rows show the **Whole Quotient ($Q$)**, and the loose tiles that cannot fill a complete row are the **Remainder ($R$)**.
3. **Interpreting the Remainder in Real Life (Round Up vs. Keep Whole Quotient):**
   - **When You MUST Round Up ($Q + 1$): Robotics Tournament Vans:** Suppose **135 robotics students** are riding to a tournament in **8-seat vans**. Tap `135 [ENTER] 8 [g] [÷R]` $\longrightarrow$ Quotient **`16`** full vans in $X$, Remainder **`7`** students in $Y$ (check: `[f] [LASTX] [×] [+]` $\to 135$). Can you leave 7 teammates standing in the parking lot? Never! You must round up to **$16 + 1 = \mathbf{17\text{ vans}}$**.
   - **When Leftovers Need One Extra Cache — The Clark's Nutcracker:** A Clark's nutcracker collects **165 whitebark pine seeds** and buries **9 seeds** in each underground cache (`165 [ENTER] 9 [g] [÷R]` $\longrightarrow$ Quotient **`18`** full caches in $X$, Remainder **`3`** seeds in $Y$). To hide every single seed before winter snow falls, the bird digs **18 full caches** plus **1 final partial cache** holding the last 3 seeds—**`19` caches in all**.
   - **When Only Full Groups Count — 3D Printer Spool Budgeting:** A maker-lab spool holds **$450\text{ meters}$** of PLA filament, and each 3D-printed chess knight requires **$16\text{ meters}$** (`450 [ENTER] 16 [g] [÷R]` $\longrightarrow$ Quotient **`28`** in $X$, Remainder **`2`** meters in $Y$). Because $2\text{ m}$ of leftover filament cannot print a 29th knight, you can print **`28` complete chess knights** with **$2\text{ m}$ of PLA left over**. *(See Chapter 7 for how `[g] [÷R]` also powers Euclid's GCF algorithm.)*

---

## 4.6 Last Number Recall: Self-Checking Without Re-Typing (`[f] [LASTX]`)

A true math detective never just hopes an answer is right—they **prove** it by running the operation in reverse. Every arithmetic operation has an opposite partner that undoes its work: **subtraction undoes addition**, **addition undoes subtraction**, **division undoes multiplication**, and **multiplication undoes division**.

On a regular calculator, checking your answer means clearing the screen and typing the whole problem backward from memory. On the SC-6, **Last Number Recall (`[f] [LASTX]`)** (`[f]` then `[ENTER]`) automatically saves a backup copy of whatever number was sitting on Shelf $X$ right before your last operation! That gives you three everyday superpowers:
1. **Two-Tap Detective Check:** Tap `[f] [LASTX]` to pull your last number back onto Shelf $X$ (while your answer lifts to Shelf $Y$), then tap the opposite operator (`[-]` after `[+]`, or `[÷]` after `[×]`) to restore your starting number with **zero re-typing**.
2. **The Instant "Oops!" Undo:** Accidentally tapped `[+]` when you meant to tap `[×]`? Just tap `[f] [LASTX] [-]` to undo the addition, then tap `[f] [LASTX] [×]`!
3. **Zero-Retype Factor Re-Use:** Whenever the next step of a problem needs the exact same number again (like multiplying by `60` minutes and then by `60` seconds), `[f] [LASTX]` hands it back to you in a single click.

### 4.6.1 Seeing All Four Inverse Checks in Two Taps

Watch how `[f] [LASTX]` pairs each of the four operations with its opposite partner across the two shelves of your screen. First, to check **addition with subtraction** ($47 + 36 = 83 \longrightarrow 83 - 36 = 47$), enter `47`, press `[ENTER]` to lift `47` onto Shelf $Y$, and type `36 [+]` via `47 [ENTER] 36 [+]`: the stack drops to show the sum $X = \mathbf{83}$ on the ground floor while silently tucking a backup copy of `36` into `LASTX`. Now tap `[f] [LASTX]`: the calculator pulls `36` right back onto Ground Shelf $X$ while automatic stack lift pushes `83` up to Waiting Shelf $Y$ ($Y = 83,\; X = 36$), so one tap of `[-]` computes $83 - 36 = \mathbf{47}$ on Ground Shelf $X$ and confirms your starting number with zero re-typing!

That exact same two-tap rhythm works for the other three operations as well. To check **multiplication with division** ($15 \times 8 = 120 \longrightarrow 120 \div 8 = 15$), multiply `15 [ENTER] 8 [×]` to reach $X = \mathbf{120}$, then tap `[f] [LASTX]` to pull `8` back into Shelf $X$ (lifting `120` to Shelf $Y$) and tap `[÷]` to see $120 \div 8 = \mathbf{15}$. To check **subtraction with addition** ($95 - 38 = 57 \longrightarrow 57 + 38 = 95$), subtract `95 [ENTER] 38 [-]` to get $X = \mathbf{57}$, then tap `[f] [LASTX]` to recall the `38` you took away and tap `[+]` to put it back ($57 + 38 = \mathbf{95}$). And to check **division with multiplication** ($84 \div 7 = 12 \longrightarrow 12 \times 7 = 84$), divide `84 [ENTER] 7 [÷]` to get $X = \mathbf{12}$, then tap `[f] [LASTX]` to recall divisor `7` and tap `[×]` to multiply $12 \times 7 = \mathbf{84}$ and restore the whole group!

### 4.6.2 The Science Museum Night-Watch Detective Club
Seeing how `[f] [LASTX]` proves every calculation in two clicks earns you a badge in the **Science Museum & Space Camp Night-Watch Detective Club**! Every Saturday evening after the museum doors close, your junior detective squad walks through eight exhibit halls to audit priceless artifacts—sunken pirate coins, rocket motors, megalodon shark teeth, astronaut ice cream, trading-card vaults, LEGO mosaic walls, coral reef tanks, and robotics bins. By tapping `[f] [LASTX]` followed by the opposite operation at every exhibit stop, you prove every single tally is $100\%$ accurate without re-typing a single number!

Your night-watch rounds begin in the Maritime Hall in front of a sunken pirate ship's sea chest holding **68 silver doubloon coins** and **27 copper coins**. Once you add them together ($68 + 27 = 95$ coins in all), how do you prove your total is right without dumping the chest out and recounting? If $68$ silver plus $27$ copper really equals $95$, then taking away the $27$ copper coins (`[f] [LASTX] [-]`) must leave the exact $68$ silver coins you started with! Add the coins and run your two-tap subtraction check by pressing `68 [ENTER] 27 [+] [f] [LASTX] [-]`, which reaches `95` and then subtracts the recalled `27` copper coins to restore **`68`** silver coins on Ground Shelf $X$.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `68 [ENTER]` | 0 | 0 | 68 | 68 | Load 68 silver coins into $X$ and duplicate into Register $Y$ |
| `27 [+]` | 0 | 0 | 0 | 95 | Add 27 copper coins; sum 95 displays in active Register $X$ |
| `[f] [LASTX]` | 0 | 0 | 95 | 27 | Last Number Recall: Recall last number 27 into $X$; sum lifts to $Y$ |
| `[-]` | 0 | 0 | 0 | 68 | Inverse subtraction: $95 - 27 = 68$; original silver count restored |

When Register $X$ returns to $68$ in two taps, your 95-coin treasure count is locked in.

From the pirate ship, your squad walks through the next three exhibit halls on the ground floor:
- **Space Camp Launch Bay (Checking Multiplication with Division):** Here **18 launch boxes** each hold **6 solid-fuel model rocket motors** ($18 \times 6 = 108$). Packing those 108 motors back into groups of 6 (`[f] [LASTX] [÷]`) must give back all 18 boxes: pressing `18 [ENTER] 6 [×] [f] [LASTX] [÷]` evaluates $108$ motors in Register $X$, and then recalls box size `6` to divide and restore **`18`** boxes ($X = 18$).
- **Paleontology Lab (Checking Subtraction with Addition):** A velvet specimen drawer starts the week with **92 fossilized megalodon and mako shark teeth**, and the curator moves **35 teeth** into a glass display case (`92 - 35 = 57` left in the drawer). Since subtraction took 35 teeth out, addition puts them back: pressing `92 [ENTER] 35 [-] [f] [LASTX] [+]` leaves 57 teeth in Register $X$ and then recalls `35` via `[f] [LASTX] [+]` to restore all **`92`** fossils ($X = 92$).
- **Space Camp Commissary (Checking Division with Multiplication):** A shipping carton of **156 freeze-dried astronaut ice cream pouches** is divided into mission bags of **12 pouches each** (`156 ÷ 12 = 13` mission bags). Recombining those 13 bags of 12 by pressing `156 [ENTER] 12 [÷] [f] [LASTX] [×]` recalls bag size `12` via `[f] [LASTX] [×]` and multiplies $13 \times 12$ in place to restore **`156`** pouches ($X = 156$).

Now your detective squad heads upstairs to the **Grand Hobby, Ocean & Robotics Galleries**, where the numbers grow into the hundreds:
- **Collector Vault:** Two friends combine **348 Pokémon and sports cards** plus **185 superhero cards** (`348 + 185 = 533`), then separate the 185 superhero cards back out: keying in `348 [ENTER] 185 [+] [f] [LASTX] [-]` produces 533 cards on Shelf $X$ and recalls `185` with `[f] [LASTX] [-]` to verify **`348`** ($X = 348$).
- **Maker Studio LEGO Mosaic Wall:** A giant pixel-art wall has **24 rows** with **16 baseplates in each row**. Instead of scribbling long division to check $24 \times 16 = 384$, pressing `24 [ENTER] 16 [×] [f] [LASTX] [÷]` multiplies $24 \times 16$ into 384 baseplates and uses `[f] [LASTX] [÷]` to divide 384 by 16 in a single click, returning **`24`** rows ($X = 24$).
- **Living Ocean Gallery:** The coral reef tank holds **500 liters** of saltwater, and the aquarist pumps **187 liters** into a filter tub (`500 - 187 = 313` liters left). Simulating pumping those 187 filtered liters right back in via `500 [ENTER] 187 [-] [f] [LASTX] [+]` recalls `187` and adds it back to restore all **`500`** liters ($X = 500$).
- **Robotics Testing Arena:** A bulk tub of **225 rubber omni-wheels** is sorted into team bins of **15 wheels each** ($225 \div 15 = 15$ bins, a perfect square!). Pressing `225 [ENTER] 15 [÷] [f] [LASTX] [×]` divides 225 into 15 bins and then multiplies by the recalled `15` via `[f] [LASTX] [×]` to restore **`225`** omni-wheels ($X = 225$). Your eight-stop museum audit is complete!

---

## 4.7 Extreme Math Challenges: Doubling to the Sky & Your Age in Seconds

Think multiplication is just memorizing times tables? Try these three challenges on your SC-6 and test them on your family:

### Challenge 1: What Happens If You Fold a Piece of Paper 10 Times with `[g] [REP]`?
A sheet of notebook paper is only $1\text{ layer}$ thick. Every time you fold it in half, the number of layers **doubles** ($\times 2$). Can you fold a piece of paper 10 times with your bare hands? Almost nobody can—and Constant Repeat (`[g] [REP]`) shows why! When you seed the stack with `2` and tap `[×]` nine times in a row—running `2 [g] [REP] [×] [×] [×] [×] [×] [×] [×] [×] [×]`—you watch a 10-step **Doubling Chain ($2 \times 2 \times 2\dots$)** climb to **`1024` layers** (thicker than a 1,000-page dictionary).

Watch what happens to that single sheet of paper on each fold: first tap `2` `[g] [REP]` to lock constant factor 2 into every stack floor ($T = Z = Y = X = 2$), priming the doubling ladder after the first fold. Tap `[×]` for the 2nd fold and the 2 layers double to 4 ($X = 4$) while constant 2 drops down from Floor $T$ to wait on Floor $Y$; tap `[×]` for the 3rd fold and 4 layers double to 8 ($X = 8$), already thicker than cardstock; tap `[×]` for the 4th fold to reach 16 layers ($X = 16$), resisting thumb pressure; tap `[×]` for the 5th fold to reach 32 layers ($X = 32$), thick like a deck of index cards; tap `[×]` for the 6th fold to reach 64 layers ($X = 64$), stiff like a wooden slat; tap `[×]` for the 7th fold to reach 128 layers ($X = 128$), impossible to crease with bare fingers; tap `[×]` for the 8th fold to reach 256 layers ($X = 256$), thick like a textbook; tap `[×]` for the 9th fold to reach 512 layers ($X = 512$), a full 500-sheet ream of copy paper; and tap `[×]` for the 10th fold to reach 1,024 layers ($X = 1024$), towering like a colossal phone directory! If you kept tapping `[×]` 10 more times ($20\text{ folds} = 1,048,576\text{ layers}$), that single sheet of paper would stand taller than the Empire State Building!

### Challenge 2: How Many Seconds Old Are You Right Now?
If you are **11 years old** in 5th grade, have you lived for a million seconds yet? What about a *billion* seconds? Let's chain the multiplication right on the stack ($11\text{ years} \times 365\text{ days} \times 24\text{ hours} \times 60\text{ minutes} \times 60\text{ seconds}$) without writing down a single intermediate subtotal: pressing `11 [ENTER] 365 [×] 24 [×] 60 [×] 60 [×]` scales your age through days, hours, minutes, and seconds to reveal **`346,896,000` seconds** on Ground Shelf $X$!

Follow the journey across the stack: first tap `11` `[ENTER]` to set your 11-year age baseline onto the upper mezzanine shelf ($Y = 11$), then tap `365` `[×]` to fold in the days per year ($11 \times 365 = 4,015\text{ days}$ of sunrise and sunset resting on $X = 4015$). Next, tap `24` `[×]` to convert those days into hours ($4,015 \times 24 = 96,360\text{ hours}$ lived at $X = 96360$), tap `60` `[×]` to convert hours into minutes ($96,360 \times 60 = 5,781,600\text{ minutes}$ at $X = 5781600$), and finally tap `60` `[×]`—or even faster, `[f] [LASTX] [×]` since `60` is already sitting in `LASTX`—to convert minutes into seconds ($5,781,600 \times 60 = 346,896,000\text{ seconds}$)! You actually passed $1,000,000\text{ seconds}$ when you were only $11.5\text{ days}$ old—and at 11 years old, you are already more than **one-third of the way to 1 Billion seconds**.

### Challenge 3: Doubling Chains ($2 \times 2 \times 2\dots$) & Multiplying by 5s ($5 \times 5 \times 5\dots$)
With exponents (`[x²]` and `[g] [yˣ]`), repeated multiplication models both treehouse rope pulleys and bird flock waves:

- **The #1 Exponent Watch-Out with Counting Tiles ($4^2 \neq 4 \times 2$):** Before pressing an exponent key, build a **$4 \times 4$ square** on your desk with 16 Counting Tiles. Notice that $4^2$ means **4 multiplied by itself** ($4 \times 4 = \mathbf{16}$ tiles in a square), **never** $4 \times 2 = 8$! On your SC-6, tap `4 [x²]` $\longrightarrow$ **`16`**.
- **Compound Treehouse Rope Pulleys (Doubling Chains $2 \times 2 \times 2\dots$):** How can you hoist a heavy **$96\text{-pound}$ tool crate** up into a backyard treehouse using only **$3\text{ pounds}$** of pulling force? By rigging a compound **block-and-tackle pulley hoist** where each movable pulley loop shares the load between two ropes, **doubling your lifting power ($\times 2$)** with every stage. With **5 movable pulleys**, your pulling force doubles 5 times ($2 \times 2 \times 2 \times 2 \times 2 = 2^5 = 32$):
  $$\text{Total Lifting Force} = 3\text{ pounds} \times (2 \times 2 \times 2 \times 2 \times 2) = 3 \times 32 = \mathbf{96\text{ pounds}}$$
  Verify on your SC-6 stack: `2 [ENTER] 5 [g] [yˣ] 3 [×]` $\longrightarrow$ **`96` pounds**.
- **Starling Murmuration Waves (Multiplying by 5s $5 \times 5 \times 5\dots$):** When European starlings wheel across the sunset sky in a swirling *murmuration*, each bird coordinates its turns with its nearest neighbors. If 1 startled scout signals **5 neighbors**, who each signal **5 more** ($5 \times 5 = 25$), across **4 signaling waves** ($5 \times 5 \times 5 \times 5 = 5^4$), how many starlings turn together in a fraction of a second? Tap `5 [ENTER] 4 [g] [yˣ]` $\longrightarrow$ **`625` starlings**!

### 4.7.1 Putting It All Together: The Battle-Bot & Maker-Lab Workshop
To bring rectangular arrays, Floor $Z$, and `[g] [÷R]` together in one place, join the morning build crew in the **Battle-Bot & Maker-Lab Workshop**! Real engineering builds never happen in isolated single steps: you have to combine two separate hardware subtotals using Floor $Z$, and chain multi-part multiplication directly into a `[g] [÷R]` packaging check.

At the main assembly bench, you first bolt together a robot chassis using **3 drive-motor brackets at $\$4$ each** AND **2 titanium armor plates at $\$5$ each**. Just like we discovered in Chapter 2, the 4-level stack solves $(3 \times 4) + (2 \times 5)$ with zero parentheses because your first subtotal ($\$12$) rides the elevator up to Floor $Z$ while you multiply the second subtotal ($\$10$) on the ground floor! Lay out 3 rows of 4 blue counting tiles ($\$12$) and 2 rows of 5 gold counting tiles ($\$10$), then chain both products on the stack by pressing `3 [ENTER] 4 [×] 2 [ENTER] 5 [×] [+]`, which brings the $\$12$ bracket subtotal and $\$10$ armor subtotal together into **`22`** dollars.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[3] [ENTER] 4` | 0 | 0 | 3 | 4 | Place 3 brackets in $Y$, key in $\$4$ unit cost in $X$ |
| `[×]` | 0 | 0 | 0 | 12 | Evaluate motor bracket subtotal: $3 \times 4 = \$12$ |
| `[2] [ENTER] 5` | 0 | 12 | 2 | 5 | Stack lifts $\$12$ to $Z$; load 2 armor plates at $\$5$ |
| `[×]` | 0 | 0 | 12 | 10 | Evaluate armor subtotal: $2 \times 5 = \$10$; subtotal 1 in $Y$ |
| `[+]` | 0 | 0 | 0 | 22 | Combine both hardware subtotals: $\$12 + \$10 = \$22$ |

With Register $X$ reading $22$, the total chassis cost is $\mathbf{\$22}$ with zero parentheses.

Once the battle-bot chassis is bolted together, your crew steps out into the maker-lab courtyard to build **3 gravity-coaster cars**. Each car rolls on **12 wheel bogies**, and every bogie spins on **3 steel skate bearings** ($3 \times 12 \times 3$ bearings in all). If bearings are sold in tubes of **8**, how many full tubes are emptied, and how many tubes must you buy so every wheel can spin? When you chain the three multiplications right into `8 [g] [÷R]` and swap registers by pressing `3 [ENTER] 12 [×] 3 [×] 8 [g] [÷R]`, multiplying $3 \times 12 \times 3$ gives 108 bearings in all, `8 [g] [÷R]` splits 108 into **13 full tubes** ($X = 13$) with **4 extra bearings** needed ($Y = 4$), and `[x⇄y]` brings **`13`** to the front—meaning your team must buy **14 tubes** in total!

---

### 4.7.2 Key Insights & Common Pitfalls

- **The Field Trip Bus Ceiling Trap:** When dividing $145$ students across $40$-seat buses (`145 [ENTER] 40 [g] [÷R]` $\to X=3,\; Y=25$), remember that $25$ people cannot be left behind *([Singapore MOE, 2014](sc6/appendix-c-formulas-and-conversions.md#cite-singapore2014))*. Any remainder greater than zero requires ordering an extra bus ($3 + 1 = 4\text{ buses}$).
- **Array Rotation & The Commutative Law:** Rotating a $3 \times 8$ counting tile array into an $8 \times 3$ array proves that $\text{Rows} \times \text{Columns} = \text{Columns} \times \text{Rows}$ ($3 \times 8 = 8 \times 3 = 24$) without altering the physical tile count.
- **The 3-Key Remainder Proof:** Following George Pólya's "look back" strategy *([Pólya, 1945](sc6/appendix-c-formulas-and-conversions.md#cite-polya1945))*, after any `[g] [÷R]` division, pressing `[f] [LASTX] [×] [+]` multiplies the quotient by the divisor and adds the remainder from Register $Y$ to restore your exact starting dividend.
- **Leftovers vs. Decimals in Pizza Sharing:** Four friends sharing $15$ pizza slices (`15 [ENTER] 4 [g] [÷R]`) receive 3 slices each with 3 whole slices left in the box for tomorrow, avoiding awkward decimal cuts ($3.75$).

---

## 4.8 Quick Troubleshooting Guide

The following diagnostic table addresses the ten most common beginner stumbling blocks encountered during operations, skip-counting, and remainder division:

| Common Mistake / What You See | Why It Happened | How to Fix It on the Stack |
|:---|:---|:---|
| **1. In skip-counting, `[g] [REP]` was not pressed; `[+]` adds 0** | Forgot to seed all registers with `[g] [REP]`. | Type step constant, press `[g] [REP]`. |
| **2. In division, expected remainder but got decimal** | Pressed `[÷]` instead of integer division. | Use `[g] [÷R]` for whole quotient & remainder. |
| **3. Cannot see remainder after pressing `[g] [÷R]`** | Remainder is in Register Y; Register X holds quotient. | Tap `[x⇄y]` to swap and inspect remainder. |
| **4. Self-check inverse gave wrong answer** | Pressed wrong inverse operator. | Addition pairs with `-`; multiplication pairs with `÷`. |
| **5. Doubling ladder did not double** | Did not press `[ENTER]` before `[+]`. | Press `[ENTER] [+]` to duplicate and add. |
| **6. Multiplication product was too small** | Pressed `[+]` instead of `[×]`. | `[×]` multiplies; `[+]` only adds. |
| **7. Subtraction gave negative number (e.g., -54)** | Entered second number before starting number. | Enter starting number, `[ENTER]`, then subtract. |
| **8. Pressed `[C]` after first product in chained sum** | Believed screen had to be cleared. | Do not clear; the stack lifts automatically. |
| **9. Field trip bus answer was short by one bus** | Forgot that any leftover requires an additional bus. | If remainder > 0, round up by 1 whole bus. |
| **10. `LASTX` recalled unexpected number** | Executed another operation after error. | `LASTX` updates on **every** operation. |

### 4.8.1 Standard Decimal Division vs. `[g] [÷R]` Remainder Division

Now that you have mastered `[g] [÷R]`, `[x⇄y]`, and the 3-key `[f] [LASTX]` remainder proof, compare how much work it takes to find and verify a whole-number remainder on a standard calculator versus the SC-6:

| Challenge / Equation | The Algebraic Calculator Trap (Standard Entry) | The StackCalc SC-6 + Manipulative Method | Keystroke Reduction | Live Stack Visibility | Learning Breakthrough |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **Integer Division with Remainder:** $185 \div 12$ | `1 8 5 / 1 2 =` $\rightarrow 15.41666667$. To extract integer remainder: `- 15 = * 12 =` (18 keystrokes). Self-check requires retyping: `15 * 12 + 5 =` (28 total keystrokes). *Trap: Decimals obscure discrete items; scratch paper required.* | **SC-6 + 24-Tile Array Studio & Egg Cartons:** `185 [ENTER] 12 [g] [÷R]` (7 keystrokes). Simultaneously displays Quotient $Q = 15$ in Register $X$ and Remainder $R = 5$ in Register $Y$. Tap `[x⇄y]` to swap. Self-check in 3 keys: `[f] [LASTX] [×] [+]` $\rightarrow 185$. | **75% fewer keystrokes** (7 vs. 28) | **Dual Live Registers:** Quotient $Q$ and Remainder $R$ visible simultaneously on the daylight screen; zero scratch paper. | **Discrete Math Alignment:** Eliminates decimal confusion in discrete sharing problems; transforms long division into an intuitive physical packaging and self-checking workflow. |

---

## 4.9 Where to Go Next: Companion Workbook Quests & Kitchen-Table Challenges

> *For 30 additional worked problems with full 4-register stack tables, see Chapter 4 of the [SC-6 Elementary Companion Problem & Activity Workbook](../curriculum/sc6-elementary-companion-workbook.md).*

With all four whole-number operations and the SC-6's dedicated keys (`[g] [REP]`, `[g] [÷R]`, `[x²]`, `[g] [yˣ]`, and `[f] [LASTX]`) in hand, pair this chapter with the **[Big Ideas Math Middle School Supplement](../curriculum/big-ideas-middle-school-sc6-workbook.md) — Unit 1, Sections 1.1–1.2 (Whole Number Operations, Remainders & Exponents)** and **Unit 4, Section 4.3 (The Distributive Property)**, along with **Unit 4 of the 12-Unit Curriculum Guide** and the **StackCalc Student Workbook**—or try these three family challenges right now:

1. **Remainder Detective — Robotics Vans & Clark's Nutcracker Caches:** Test both real-world remainder rules on your SC-6: first run the **Robotics Van Challenge** (`135 [ENTER] 8 [g] [÷R]` $\to$ Quotient `16`, Remainder `7` $\implies$ **17 vans needed**), then run **Clark's Nutcracker Seed Caches** (`165 [ENTER] 9 [g] [÷R]` $\to$ `18` full caches + `1` partial cache of `3` seeds = **19 caches dug**), and prove each one in 3 clicks with `[f] [LASTX] [×] [+]`.
2. **Hands-On Explorer — The Odd-Number L-Border & Treehouse Pulley Hoist:** First, use your 24-Tile Array Studio to wrap odd L-borders ($1 + 3 + 5 + 7 = 4^2 = 16$) and split $8 \times 53 = 8(50 + 3) = 424$ via the Distributive Property. Then calculate the **5-Pulley Treehouse Hoist** (`2 [ENTER] 5 [g] [yˣ] 3 [×]` $\to \mathbf{96\text{ lb}}$) and **Starling Murmuration Wave** (`5 [ENTER] 4 [g] [yˣ]` $\to \mathbf{625}$).
3. **"Bet Your Family!" (The Ending-in-Five Squaring Showdown):** Challenge a parent or older sibling to race you on $45^2$, $75^2$, and $85^2$. While they reach for scratch paper, multiply the tens digit by its next neighbor ($4 \times 5 = 20 \to 2,025$; $7 \times 8 = 56 \to 5,625$; $8 \times 9 = 72 \to 7,225$), announce the answer out loud, and prove it on your SC-6 with `85 [x²]` (or `85 [ENTER] [×]`)!

---

## 4.10 Chapter Summary & Looking Ahead

Whole-number operations on the SC-6 rest on five spatial and mechanical principles:
1. **The Four-Color Array Studio & Commutative Symmetry:** Building rectangular tile arrays ($3 \times 8 = 24$) and rotating the tray $90^\circ$ ($8 \times 3 = 24$) to see why multiplication order never changes the total area.
2. **The Distributive Property (Break-Apart Arrays):** Splitting wide arrays into friendly four-color quadrants ($(10 + 2) \times (10 + 2) = 100 + 20 + 20 + 4 = 144$) across Registers $Y$ and $X$.
3. **Skip-Counting & Constant Replication (`[g] [REP]`):** Filling Register $T$ with a constant step size and tapping `[+]` or `[×]` to climb arithmetic and geometric ladders step by step.
4. **Integer Division with Remainder (`[g] [÷R]`):** Separating full containers (quotient in Register $X$) from leftover items (remainder in Register $Y$) in a single keystroke without confusing decimal tails.
5. **Self-Checking Without Re-Typing (`[f] [LASTX]`):** Recalling the last operand from `LASTX` to verify every sum, difference, product, and quotient in reverse—or reuse factors—with zero re-typing.

What happens when you have a remainder that cannot be left as a whole leftover—like slicing a single remaining pizza among four friends, or measuring a piece of craft wood down to the exact quarter-inch? Turn the page to **[Chapter 05: Fractions, Decimals, Percents & Proportional Towers](sc6/05-fractions-decimals-ratios.md)**, where you will step into the 84 mm Fraction Tower Studio, master two-dot fraction entry, and reduce fractions step-by-step with **Step-by-Step Simplify (`[g] [SIMP]`)**.

---

# Chapter 5: Fractions, Decimals, Percents & Proportional Towers

## 5.1 The Music of Halves, Quarters, and Gear Teeth: How Fractions and Ratios Run the Physical World

Pluck a guitar string, flip a bicycle upside down to spin its rear wheel, or slice a warm flatbread across a kitchen cutting board, and you are watching fractions and ratios in motion. Long before John Napier popularized the decimal point in 1614 *([Napier, 1614](sc6/appendix-c-formulas-and-conversions.md#cite-napier1614))* to help astronomers and engineers compute without tangles of ink, builders and musicians measured the physical world by dividing whole lengths into equal parts. As David Macaulay shows in his cutaway illustrations of machines *([Macaulay, 2016](sc6/appendix-c-formulas-and-conversions.md#cite-macaulay2016))*, every meshing pair of clock gears, every pulley block, and every musical harmony is a living fraction ratio that turns numbers into physical force and sound.

### 5.1.1 Why Fractions & Equivalent Fractions (`[g] [SIMP]`) Matter to You
Have you ever tried sharing a giant flatbread, pizza, or chocolate bar fairly among your friends? Or have you ever built a backyard treehouse where you measured a board with a tape measure and wondered why $\frac{4}{8}\text{ inch}$ is the exact same length as a $\frac{1}{2}\text{ inch}$ bolt?

When you lay four $\frac{1}{8}$ blocks alongside one $\frac{1}{2}$ block inside your **84 mm Fraction Studio Twin Comparator Well**, your fingers and eyes feel why $\frac{4}{8} = \frac{1}{2}$ before you ever touch a pencil. On your SC-6, **Step-by-Step Simplify (`[g] [SIMP]`)** does the exact same thing: it peels away common factors one step at a time until your fraction reaches simplest terms.

### 5.1.2 The Pharaoh's Bakery & Pythagoras's Musical Strings

Why does your **84 mm Fraction Studio** include every unit-fraction block from $\frac{1}{2}$ ($42.0\text{ mm}$) and $\frac{1}{3}$ ($28.0\text{ mm}$) down to $\frac{1}{12}$ ($7.0\text{ mm}$)? Because it models two of the most famous discoveries in ancient history:
1. **The Pharaoh's Fair-Share Bakery (1550 BCE):** In Ancient Egypt (recorded in the Rhind Mathematical Papyrus), if **4 temple bakers** needed to share **3 round loaves of bread** equally ($\frac{3}{4}$ of a loaf per person), they never cut every loaf into four small slices. Instead, they sliced the first two loaves cleanly in **half**—handing every baker one big $\frac{1}{2}$ loaf—and cut only the third loaf into **quarters** ($\frac{1}{4}$). Dock one $\frac{1}{2}$ block ($42.0\text{ mm}$) plus one $\frac{1}{4}$ block ($21.0\text{ mm}$) in the left channel of your Twin Comparator Well, and dock three $\frac{1}{4}$ blocks ($3 \times 21.0 = 63.0\text{ mm}$) in the right channel: both towers stand completely flush at **$63.0\text{ mm}$** ($\frac{1}{2} + \frac{1}{4} = \frac{3}{4}$), and the Pharaoh's bakers made only 5 knife cuts instead of 9!
2. **Pythagoras's Musical Guitar Strings:** Line up the **1 Whole** block ($84.0\text{ mm}$), two $\frac{1}{3}$ blocks ($\frac{2}{3} = 56.0\text{ mm}$), three $\frac{1}{4}$ blocks ($\frac{3}{4} = 63.0\text{ mm}$), and one $\frac{1}{2}$ block ($42.0\text{ mm}$) on your Fraction Studio lid tray. Pythagoras discovered that pinching a plucked string at $\frac{1}{2}$ its length ($42.0\text{ mm}$) sounds a pure **Octave**, pinching at $\frac{2}{3}$ ($56.0\text{ mm}$) sounds a **Perfect Fifth**, and pinching at $\frac{3}{4}$ ($63.0\text{ mm}$) sounds a **Perfect Fourth**.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `. 1 . 2 [ENTER]` | 0 | 0 | 1/2 | 1/2 | Load Egyptian half-loaf $\frac{1}{2}$ ($42.0\text{ mm}$ block) |
| 2 | `. 1 . 4 [+]` | 0 | 0 | 0 | **3/4** | Add quarter-loaf $\frac{1}{4}$ ($21.0\text{ mm}$ block) $\to \frac{3}{4}$ ($63.0\text{ mm}$) |

---

### 5.1.3 The Backyard Barbecue Mystery: Why Hot Dogs and Buns Never Match (LCM)

Every kid who has ever helped plan a picnic or family birthday barbecue has faced the greatest commercial conspiracy in the grocery store: **hot dogs** come in packs of **10**, while **hot dog buns** come in packs of **8**. If you buy 1 pack of each, you have 2 extra wieners and zero buns. If you buy 2 packs of buns (16) and 2 packs of hot dogs (20), you now have 4 extra dogs. It feels like an endless trap. How many packages must you buy so that **every single hot dog gets a bun with zero waste**?

To rescue the picnic mathematically, you are searching for the **Least Common Multiple (LCM)**—the smallest positive integer that is a simultaneous multiple of both 10 and 8:

$$\text{Multiples of } 10: 10, 20, 30, \mathbf{40}, 50, \dots$$
$$\text{Multiples of } 8: 8, 16, 24, 32, \mathbf{40}, 48, \dots$$

The magic number is **40**, because $40 \div 10 = \mathbf{4}\text{ packs of hot dogs}$ and $40 \div 8 = \mathbf{5}\text{ packs of buns}$. Four packs of dogs plus five packs of buns yields 40 hot dogs tucked neatly into 40 buns. Even better, on your SC-6 you don't need to guess multiples on scratch paper: press `10 [ENTER] 8 [f] [LCM]` and the screen immediately flashes **`40`**!

Least Common Multiple isn't just for hot dogs—it is your key to adding different-sized fraction slices. Suppose you are building a treehouse railing and need to join a $\frac{3}{8}\text{-foot}$ piece of oak trim and a $\frac{5}{12}\text{-foot}$ piece of pine trim. You can't just add $3 + 5$, because an eighth-block and a twelfth-block are completely different sizes. You need the **smallest block size that fits evenly under both**: $\text{LCM}(8, 12) = 24$ (twenty-fourths). Once both pieces are measured in twenty-fourths, adding them is straightforward.

---

### 5.1.4 The Drummer's Secret: Polyrhythms & Why Music Is Living Math

Ever listen to an Afro-Cuban groove, a jazz drum solo, or a modern hip-hop beat where the rhythm seems to float, dance, and pull against itself? That rhythmic tension is powered directly by number theory.

Imagine a drummer playing a **"3-against-4" polyrhythm**:
- The right hand taps a steady pulse every 4 clock ticks: $[4, 8, \mathbf{12}, 16, 20, \mathbf{24}, \dots]$
- The left hand plays a cross-pulse every 3 clock ticks: $[3, 6, 9, \mathbf{12}, 15, 18, 21, \mathbf{24}, \dots]$

As the music plays, the two hands wander apart, creating musical tension. The listener's ear holds its breath. But then—**CRASH!** Both hands strike the cymbals at the exact same microsecond.

When does the pattern resolve? At tick **12**—the Least Common Multiple of 3 and 4 ($\text{LCM}(3, 4) = 12$). The entire universe of musical syncopation and harmonic acoustics is governed by common denominators.

---

### 5.1.5 The Bicycle Mechanic's Secret: The "Hunting Tooth" & Why Gears Survive (GCF)

Look closely at the steel chain and sprockets on a professional racing bicycle. Suppose the chainring at the crank has 34 teeth and the rear cog has 17 teeth.

Notice something dangerous? $34 = 2 \times 17$. Their **Greatest Common Factor is 17** (because 17 divides evenly into both 34 and 17).

If a bicycle were built with that ratio, the exact same chain link would slam into the exact same cog tooth on every second pedal revolution. If that one link picks up a microscopic speck of diamond-hard road grit, it will hammer into that identical tooth thousands of times an hour, gouging a groove and destroying the drivetrain.

Master bicycle engineers avoid this disaster by choosing gear tooth counts that **share no common factor greater than 1** (their Greatest Common Factor is $1$, a pattern we explore in depth in Chapter 7). When the two gear tooth numbers share no common factor greater than 1, each chain link **"hunts"** around every single tooth on the entire sprocket before ever repeating. Wear is distributed uniformly across all teeth, allowing the chain to last for thousands of miles. GCF is mechanical engineering.

Throughout this chapter, you will pair your $84\text{ mm}$ Fraction Towers with two-dot fraction entry (`[.]` for `. n . d` and `w . n . d`) and Fraction/Decimal Display Mode (`[FDISP]`), flipping effortlessly between Mixed Number Display (`[a ᵇ/c]`), Improper Fraction Display (`[f] [d/c]`), and Repeating Decimal Display (`[f] [0.3̄]`). You will watch common factors peel away with Step-by-Step Simplify (`[g] [SIMP]`), uncover common denominators and shared factors with `[f] [LCM]` and `[GCF]`, scale recipes and blueprints in Ratio Mode (`[g] [a:b]`), and compute tips, discounts, and exact rational chains with `[%]`, `[+]`, `[-]`, `[×]`, `[÷]`, `[ENTER]`, `[x⇄y]`, and `[C]`.

![Least Common Multiple of 12 and 18 → 36](../assets/manuals/screenshots/sc6_fractions_lcm.png)

## 5.2 Hands-On Studio: Why Your Fraction Towers Stand 84 Millimeters Tall

Think back to the Pharaoh's bread loaves, the hot dog packs, and the bicycle gears we just met. Whether you are sharing bread into halves and quarters, lining up 3-against-4 drumbeats at tick $12$, or comparing different-sized slices, the hardest part of fractions on paper is that the numbers $\frac{3}{4}$ and $\frac{2}{3}$ look like flat symbols trapped on a page—you can't *feel* how big $\frac{3}{4}$ is compared to $\frac{2}{3}$!

That is why your **StackCalc Fraction Studio** turns fractions into real physical towers you can hold in your hands. And why did our engineers choose **$84.0\text{ millimeters}$** as the height of the **1-Whole Tower** instead of $100\text{ mm}$?

Because $84$ is a super-divisible number! You can divide $84\text{ mm}$ cleanly into **halves** ($42\text{ mm}$), **thirds** ($28\text{ mm}$), **fourths** ($21\text{ mm}$), **sixths** ($14\text{ mm}$), **eighths** ($10.5\text{ mm}$), and **twelfths** ($7.0\text{ mm}$—the exact visible height of a single Counting Tile!).

### 5.2.1 Seeing $\frac{3}{4} + \frac{2}{3} = 1\frac{5}{12}$ Before You Touch a Pencil

Watch how your $84\text{ mm}$ Fraction Towers take the mystery out of adding fractions with different denominators, like $\frac{3}{4} + \frac{2}{3}$:
- **Why Paper Alone Can Feel Tricky:** On paper, adding $\frac{3}{4} + \frac{2}{3}$ requires finding the Least Common Multiple of 4 and 3 ($12$), rewriting $\frac{3}{4} = \frac{9}{12}$ and $\frac{2}{3} = \frac{8}{12}$, adding $9 + 8 = \frac{17}{12}$, and converting to $1\frac{5}{12}$.
- **How Your Hands See It in Seconds:** Drop the $\frac{3}{4}$ tower ($63.0\text{ mm}$) and the $\frac{2}{3}$ tower ($56.0\text{ mm}$) into the left channel of your **Twin Comparator Well** ($63.0 + 56.0 = 119.0\text{ mm}$). Now drop the white **1-Whole** tower ($84.0\text{ mm}$) into the right channel beside them. Your $\frac{3}{4} + \frac{2}{3}$ stack sticks up above 1 Whole by $35.0\text{ mm}$—and when you stack **five $\frac{1}{12}$ lilac blocks** ($5 \times 7.0\text{ mm} = 35.0\text{ mm}$) on top of the 1-Whole tower, both channels stand completely flush! You can see and feel the answer right in your tray: **$1\frac{5}{12}$**.
- **On Your SC-6 Stack:** Key in `. 3 . 4 [ENTER] . 2 . 3 [+]`. The screen immediately shows `1_5/12` (or `17/12` if you tap `[f] [d/c]`, and `1.41666667` if you tap `[FDISP]`).

| Physical Fraction Towers | Dot-Matrix LCD View | RPN Operational Stack |
|:---|:---|:---|
| **84.0 mm Proportional Towers** with zero-loss lap joints | **Daylight Dot-Matrix Grid** with $Y \mid X$ split | **Hardware Stack Lift & Drop** without parenthesis clutter |
| **Twin Comparator Well** for immediate flush alignment checks | **3-Tier Linear Scaling Fonts** preventing digit truncation | **Intuitive Two-Dot Entry Syntax** (`. n . d` and `w . n . d`) |
| **Calibrated Tri-Face Markings** (Fraction / Decimal / Percent) | **Unreduced Default Mode** preserving your fractions | **Step-by-Step Simplify (`[g] [SIMP]`)** step-by-step reduction & LCM |

![StackCalc Fraction Studio: 84mm Proportional Towers and Twin Comparator Well](../assets/renders/fraction-studio-hero.png)

### 5.2.2 Meet Every Tower in Your $84.0\text{ mm}$ Fraction Family
Every color-coded block in your kit is a precise fraction of the $84.0\text{ mm}$ master tower:
- **1 WHOLE Tower:** $84.0\text{ mm}$ master architectural datum in matte technical white
- **1/2 Halves:** $42.0\text{ mm}$ each (vibrant scarlet red)
- **1/3 Thirds:** $28.0\text{ mm}$ each (bright solar yellow)
- **1/4 Fourths:** $21.0\text{ mm}$ each (cobalt blue)
- **1/6 Sixths:** $14.0\text{ mm}$ each (emerald green)
- **1/8 Eighths:** $10.5\text{ mm}$ each (cyan blue)
- **1/12 Twelfths:** $7.0\text{ mm}$ each (lilac purple)

Even better, rotate any block in your hand and look at its **three laser-marked faces**: the **Front Face** shows the common fraction ($\frac{1}{4}$), the **Right Face** shows its decimal twin ($0.25$), and the **Back Face** shows its percentage twin ($25\%$). Holding a single blue block lets your eyes see that $\frac{1}{4}$, $0.25$, and $25\%$ are three names for the exact same size!

### 5.2.3 Proving Equivalence in the Twin Comparator Well

The storage case for your Fraction Studio includes a side-by-side channel called the **Twin Comparator Well**. Whenever you want to know whether two fractions are equal—or which one is bigger—you simply stand them side by side in Well A and Well B and slide your fingertip across the top edge!

![Fraction Studio: Twin Comparator Well Equivalence Proof and Counting Tile Bridge](../assets/manuals/fraction_studio_twin_comparator.png)

Try two hands-on experiments right now:
1. **Two Halves Make One Whole ($\frac{2}{2} = 1$):** Place the white **1-Whole** tower ($84.0\text{ mm}$) into Well A, and stack two scarlet **$\frac{1}{2}$** towers ($42.0\text{ mm} + 42.0\text{ mm} = 84.0\text{ mm}$) into Well B. Slide your finger across the top: there is zero step between them, proving $\frac{2}{2} = 1$.
2. **Which Is Bigger: $\frac{3}{4}$ or $\frac{4}{6}$? (And How Much Bigger?):** Stack three blue **$\frac{1}{4}$** blocks in Well A ($3 \times 21.0\text{ mm} = 63.0\text{ mm}$) and four green **$\frac{1}{6}$** blocks in Well B ($4 \times 14.0\text{ mm} = 56.0\text{ mm}$). Slide your finger across the top: Well A stands taller than Well B by $7.0\text{ mm}$, proving $\frac{3}{4} > \frac{4}{6}$! Now grab **1 Counting Tile** ($7.0\text{ mm}$ visible height, which is $\frac{1}{12}$ of $84\text{ mm}$) from your Counting Studio and drop it on top of the $\frac{4}{6}$ stack in Well B ($56.0 + 7.0 = 63.0\text{ mm}$). Run your finger across again—*completely flush!* Your fingertips just discovered that $\frac{4}{6} + \frac{1}{12} = \frac{3}{4}$.

Now watch the SC-6 stack confirm what your hands just felt—enter $\frac{4}{6}$ (`[.] 4 [.] 6 [ENTER]`), add $\frac{1}{12}$ (`[.] 1 [.] 12 [+]`) to see the unreduced twelfths sum **`9/12`**, and tap `[g] [SIMP]` to reduce it to **`3/4`**:

| Keystroke | Register T | Register Z | Register Y | Register X (Display) |
| :--- | :--- | :--- | :--- | :--- |
| `[.] 4 [.] 6` | 0 | 0 | 0 | 4/6 |
| `[ENTER]` | 0 | 0 | 4/6 | 4/6 |
| `[.] 1 [.] 12` | 0 | 0 | 4/6 | 1/12 |
| `[+]` | 0 | 0 | 0 | 9/12 |
| `[g] [SIMP]` | 0 | 0 | 0 | 3/4 |

---

## 5.3 Two-Dot Entry Syntax (`. n . d` and `w . n . d`): Building a Fraction from Top to Bottom

Did you notice how fast we entered `4/6` and `1/12` in the table above using the decimal point key `[.]`?

On most calculators, typing a fraction is a chore: you have to hunt for a special fraction-template button, arrow up and down between little boxes, or wrap division problems inside parentheses like `( 3 / 8 )`.

On the SC-6, you build a fraction from top to bottom using the single button your fingers already know best—the **dot key (`[.]`)**! Here is how the **Two-Dot Rule** works:
- Think of the **first dot (`[.]`)** as saying *"Get ready for a fraction!"* and the **second dot (`[.]`)** as drawing the **fraction bar (`/`)** between the top number (numerator) and bottom number (denominator).
- **Proper Fraction ($\frac{3}{8}$):** Tap `[.] 3 [.] 8` $\longrightarrow$ Display shows **`3/8`**.
- **Mixed Number ($2\frac{3}{4}$):** If your fraction has a whole number in front, just type the whole number *before* the first dot! Tap `[2] [.] 3 [.] 4` $\longrightarrow$ Display shows **`2 3/4`**.
- **Improper Fraction ($\frac{11}{4}$):** Tap `[.] 11 [.] 4` $\longrightarrow$ Display shows **`11/4`**.

The moment your finger taps that second dot `[.]`, the calculator knows you are building a fraction and displays it clearly in your horizontal $Y \mid X$ split screen, automatically sizing the digits so nothing ever gets cut off.

### 5.3.1 Flipping Between Mixed Numbers, Improper Fractions, and Decimals
Just as your physical Fraction Towers show fraction, decimal, and percent faces when you turn them in your hand, three keys let you flip how any number looks on screen at any time:
- **Mixed Number View (`[a ᵇ/c]`):** Shows whole units plus the leftover fraction (turning `11/4` into **`2 3/4`**).
- **Improper Fraction View (`[f] [d/c]`):** Packs the whole units inside the numerator so you can count total slices (turning `2 3/4` into **`11/4`**).
- **Fraction / Decimal Toggle (`[FDISP]`):** Flips back and forth between exact fraction view and decimal view (`3/4` $\longleftrightarrow$ **`0.75`**).

### 5.3.2 Rock Band Beats & Post-Scrimmage Chocolate Bars
Step into the music and robotics studio, where fractions power everything from electric guitar solos and drum fills to sharing giant chocolate bars after a scrimmage! Let's put your $84\text{ mm}$ Fraction Towers and two-dot entry syntax (`. n . d` and `w . n . d`) to work locking proper fractions onto the stack and flipping mixed numbers into improper fractions in a single tap.

In a rock song's 8-beat measure, your drummer plays a syncopated fill covering $\frac{5}{8}$ of the bar—and if you press a guitar string down so $\frac{5}{8}$ of its length vibrates, it rings with a bright musical sixth! Stack five cyan $\frac{1}{8}$ Fraction Studio blocks ($5 \times 10.5\text{ mm} = 52.5\text{ mm}$) in the Comparator Well to feel that exact proportion against the $84\text{ mm}$ Whole tower, then build the fraction from top to bottom with two dots by pressing `[.] 5 [.] 8 [ENTER]` so the stack displays **`5/8`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[.] 5 [.] 8` | 0 | 0 | 0 | 5/8 | Two-dot syntax parses numerator 5 and denominator 8 into active $X$ |
| `[ENTER]` | 0 | 0 | 5/8 | 5/8 | Lift fraction to holding Register $Y$; verified as exact rational quantity |

The daylight display confirms $X = 5/8$ as an exact fraction without any decimal rounding, matching the five cyan eighth-blocks in your Twin Comparator Well down to the half-millimeter. After recording the drum track and winning the afternoon robotics scrimmage, your team gathers around the studio snack table, where $3\ \frac{2}{5}$ giant scored chocolate bars are waiting—each bar scored into 5 equal strips so every musician and robot pilot can grab an identical share. How many individual $\frac{1}{5}\text{-bar}$ strips can you hand out to the team in all?

Place 3 full 1-Whole towers ($84\text{ mm}$ each) beside two $\frac{1}{5}$ fractional blocks to see both the whole bars and the extra strips side by side on your tray, then enter `3 . 2 . 5` (putting the whole number `3` before the first dot!) and tap `[f] [d/c]` to unpack all the whole bars into fifths: pressing `[3] [.] 2 [.] 5 [ENTER] [f] [d/c]` converts the mixed number on Ground Shelf $X$ into **`17/5`**. Loading `3 . 2 . 5` ($X = 3\ 2/5$) and `[ENTER]` ($X = 3\ 2/5$), then flipping to improper fraction mode with `[f] [d/c]` ($Y = 3\ 2/5,\; X = 17/5$) proves that $3$ whole bars ($3 \times 5 = 15$ strips) plus $2$ extra strips give **$\frac{17}{5}$ strips** in all, with your original mixed number still resting on Shelf $Y$ for comparison!

---

## 5.4 Why Your Calculator Keeps Fractions Unreduced Until You Press `[g] [SIMP]`

Suppose you multiply $\frac{1}{2} \times \frac{2}{3}$ on a standard school calculator. As soon as you press equals, the screen jumps straight to `1/3`.

Why is that actually a problem when you are learning fractions? Because if the calculator jumps straight from $\frac{1}{2} \times \frac{2}{3}$ to $\frac{1}{3}$, it hides the most important rule of fraction multiplication: **multiplying the numerators ($1 \times 2 = 2$) and multiplying the denominators ($2 \times 3 = 6$) to get $\frac{2}{6}$!**

On the SC-6, **arithmetic never hides your intermediate steps**:
1. When you multiply $\frac{1}{2} \times \frac{2}{3}$, the screen shows your true unreduced product: **`2/6`**.
2. When you are ready to simplify, **you** press **Step-by-Step Simplify (`[g] [SIMP]`)** and watch the shared factor divide out to reveal **`1/3`**!

| Operation | Unreduced Output | Next Step with `[g] [SIMP]` |
|:---|:---|:---|
| **Like Addition:** $2/4 + 1/4$ | $3/4$ | `LOWEST TERMS` alert |
| **Like Addition:** $2/4 + 2/4$ | $4/4$ (retains $4/4$) | `[g] [SIMP]` $\to 1$ |
| **Like Subtraction:** $3/4 - 1/4$ | $2/4$ (retains $2/4$) | `[g] [SIMP]` $\to 1/2$ |
| **Unlike Addition:** $1/2 + 1/4$ | $3/4$ (common denom $4$) | `LOWEST TERMS` alert |
| **Multiply:** $2/3 \times 3/4$ | $6/12$ | `[g] [SIMP]` $\to 1/2$ |
| **Divide:** $2/3 \div 1/4$ | $8/3$ ($2/3 \times 4/1$) | `[a ᵇ/c]` $\to 2\frac{2}{3}$ |

### 5.4.1 How Robot Speed Gears Work: Multiplying Across vs. Cross-Canceling

Seeing the unreduced fraction first also helps you understand a famous shortcut your teacher will show you on paper called **cross-canceling**.

Imagine building a 3-stage robot gear train where each gear slows the spin down for extra climbing power. Suppose Gear 1 spins at $\frac{1}{2}$ the motor's speed, Gear 2 spins at $\frac{2}{3}$ of Gear 1's speed, and Gear 3 spins at $\frac{3}{4}$ of Gear 2's speed. How fast does Gear 3 spin compared to the motor?
- **Pathway 1 — Multiply Straight Across, Then Press `[g] [SIMP]`:** Multiply all the numerators ($1 \times 2 \times 3 = 6$) and all the denominators ($2 \times 3 \times 4 = 24$) to get $\frac{6}{24}$ on the SC-6 (`[.] 1 [.] 2 [ENTER] [.] 2 [.] 3 [×] [.] 3 [.] 4 [×]`), then tap `[g] [SIMP]` to shrink $\frac{6}{24} \longrightarrow \mathbf{\frac{1}{4}}$.
- **Pathway 2 — Cross-Cancel Shared Factors Before You Multiply:** Look at the numerators and denominators before multiplying: there is a $2$ on the bottom and a $2$ on top, plus a $3$ on the bottom and a $3$ on top! Canceling those matching pairs ($\frac{2}{2} = 1$ and $\frac{3}{3} = 1$) leaves the answer right away:
  $$\frac{1}{\cancel{2}} \times \frac{\cancel{2}}{\cancel{3}} \times \frac{\cancel{3}}{4} = \mathbf{\frac{1}{4}}$$
  The middle gears act like bridges—only the first numerator ($1$) and last denominator ($4$) survive!
- **Nature Connection — Migrating Frigatebird Half-Brain Flight Sleep:** Great frigatebirds fly non-stop over the ocean for weeks by resting half their brain at a time. If a frigatebird spends $\frac{1}{3}$ of a $24\text{-hour}$ day in flight-sleep postures, and $\frac{1}{4}$ of *that* time in deep two-hemisphere sleep, multiplying $\frac{1}{3} \times \frac{1}{4} = \frac{1}{12}$ of a day (`24 [×]` $\longrightarrow \mathbf{2\text{ hours}}$) shows how "a fraction of a fraction" works in nature.

### 5.4.2 The Custom Bicycle Gear Shop
Roll your mountain bike into the **Custom Bicycle Gear Shop** to test fraction multiplication in action—first multiplying proper fractions to see the unreduced grid before pressing `[g] [SIMP]`, and then scaling a mixed-number suspension fluid recipe for a downhill race!

To protect the bike's rear shock from mud, you cut a rectangular carbon-fiber mudguard patch measuring $\frac{2}{3}\text{ meter}$ wide by $\frac{3}{4}\text{ meter}$ long. What is its area in square meters? Picture folding a $1\text{-meter}$ square into $3$ columns (taking $2$) and $4$ rows (taking $3$): the overlapping patch covers $2 \times 3 = 6$ out of $3 \times 4 = 12$ mini-rectangles ($\frac{6}{12}$). Multiply on the stack so you can see the unreduced $\frac{6}{12}$ grid first, and then tap `[g] [SIMP]` to peel away the shared factor of $6$: keying in `[.] 2 [.] 3 [ENTER] [.] 3 [.] 4 [×] [g] [SIMP]` shows `6/12` and then reduces it to **`1/2`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[.] 2 [.] 3 [ENTER]` | 0 | 0 | 2/3 | 2/3 | Enter width $\frac{2}{3}\text{ m}$ into Register $Y$ |
| `[.] 3 [.] 4 [×]` | 0 | 0 | 0 | 6/12 | Multiply by length $\frac{3}{4}\text{ m}$; stack yields unreduced $\frac{6}{12}$ |
| `[g] [SIMP]` | 0 | 0 | 0 | 1/2 | Tap `[g] [SIMP]` to reduce $\frac{6}{12}$ to $\frac{1}{2}\text{ m}^2$ |

The SC-6 preserves the unreduced product `6/12` so you can verify the $3 \times 4$ grid of twelve mini-rectangles before simplifying to $X = \mathbf{1/2\text{ m}^2}$ with `[g] [SIMP]`. With the carbon-fiber mudguard mounted above the rear wheel, you turn to the front of the bike to tune the suspension fork for a steep, rocky downhill trail! That trail upgrade requires scaling the standard cross-country damper oil volume of $2\ \frac{1}{4}\text{ ounces}$ by $1\ \frac{1}{2}$ times so the fork absorbs heavy landings smoothly. Thinking in improper fractions, $2\ \frac{1}{4}$ is $\frac{9}{4}$ and $1\ \frac{1}{2}$ is $\frac{3}{2}$, so their product is $\frac{27}{8}$ ounces. Watch the SC-6 multiply the mixed numbers directly and convert back to whole ounces and eighths with `[a ᵇ/c]` when you press `[2] [.] 1 [.] 4 [ENTER] [1] [.] 1 [.] 2 [×] [a ᵇ/c]` to reach **`3 3/8`**. Loading the base volume `2 . 1 . 4` with `[ENTER]` ($X = 2\ 1/4$), scaling by `1 . 1 . 2 [×]` ($X = 27/8$), and unpacking the whole ounces with `[a ᵇ/c]` ($X = 3\ 3/8$) gives **$3\ \frac{3}{8}\text{ ounces}$** of damper oil ready to pour into the fork!

### 5.4.3 Three Ways to Understand Fraction Division (Why $\frac{3}{4} \div \frac{1}{8} = 6$)

When students first see a fraction division problem like $\frac{3}{4} \div \frac{1}{8} = 6$, they often ask a great question: *"Wait—how can dividing make the answer BIGGER ($6$)?"*

Think about what $12 \div 3 = 4$ means with whole numbers: it asks, *"How many groups of $3$ fit inside $12$?"* Now ask the exact same question for $\frac{3}{4} \div \frac{1}{8}$: **"How many $\frac{1}{8}\text{-size}$ blocks fit inside a $\frac{3}{4}\text{-size}$ tower?"** Because $\frac{1}{8}$ blocks are small, you can fit **6 of them** inside $\frac{3}{4}$! You can see and prove this three ways:

1. **Physical Fraction Tower Alignment:** Stack three blue $\frac{1}{4}$ blocks ($3 \times 21.0\text{ mm} = 63.0\text{ mm}$) in Well A of your **84 mm Fraction Studio**, and stack cyan $\frac{1}{8}$ blocks ($10.5\text{ mm}$ each) in Well B until both towers stand flush. It takes exactly **6 cyan $\frac{1}{8}$ blocks** ($6 \times 10.5\text{ mm} = 63.0\text{ mm}$) to match $\frac{3}{4}$!
2. **Common-Denominator Measurement Division:** Rewrite both fractions using the same block size (eighths, since $\frac{3}{4} = \frac{6}{8}$). Now the question is simply *"How many $1\text{-eighths}$ fit inside $6\text{-eighths}$?"*
   $$\frac{3}{4} \div \frac{1}{8} = \frac{6}{8} \div \frac{1}{8} = 6\text{ eighths} \div 1\text{-eighth} = 6 \div 1 = \mathbf{6}$$
3. **Multiplying by the Reciprocal (`[f] [1/x]`):** Because eight $\frac{1}{8}$ blocks fit inside $1$ Whole, dividing by $\frac{1}{8}$ is the same as multiplying by its flipped partner (the **reciprocal** $\frac{8}{1}$, which you can see anytime with the `[f] [1/x]` key):
   $$\frac{3}{4} \times \frac{8}{1} = \frac{24}{4} = \mathbf{6}$$

Once you picture fraction division as *"how many small steps fit inside a total distance?"*, real-world puzzles click into place:
- **Aesop's Crow Water-Displacement Puzzle:** In biology labs, a clever New Caledonian crow drops pebbles into a tube to raise the water level by $4\frac{1}{2}\text{ cm}$ and reach a floating treat. If each pebble raises the water by $\frac{3}{8}\text{ cm}$, how many pebbles must the crow drop? Keying `4 [.] 1 [.] 2 [ENTER] [.] 3 [.] 8 [÷]` ($\frac{9}{2} \div \frac{3}{8} = \frac{36}{8} \div \frac{3}{8} = 36 \div 3$) reveals that the crow needs **$12$ pebbles**.
- **3D Print Nozzle Layer Slicing:** When a 3D printer slices a $6\text{ mm}$ tall bracket into thin $\frac{3}{20}\text{ mm}$ layers of melted plastic, keying `6 [ENTER] [.] 3 [.] 20 [÷]` shows the printer must lay down **$40$ layers**.

### 5.4.4 Chained Mixed-Number Sprints: Zero Parentheses on the Stack
What happens when a Science Olympiad challenge combines mixed-number multiplication *and* fraction division in a single expression, like $(3\ \frac{1}{2} \times 2\ \frac{2}{3}) \div 1\ \frac{1}{6}$? On an ordinary infix calculator, typing that expression takes 33 keystrokes and 6 nested parentheses—where a single missed bracket ruins the entire answer! Under the hood, $\frac{7}{2} \times \frac{8}{3} = \frac{28}{3}$, and dividing by $\frac{7}{6}$ flips and multiplies ($\frac{28}{3} \times \frac{6}{7} = 4 \times 2 = 8$). Watch two-dot RPN glide straight to **`8`** in 17 keystrokes with zero parentheses when you key in `3 [.] 1 [.] 2 [ENTER] 2 [.] 2 [.] 3 [×] 1 [.] 1 [.] 6 [÷] [a ᵇ/c]` to land on **`8`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `3 [.] 1 [.] 2 [ENTER]` | 0 | 0 | 3 1/2 | 3 1/2 | Enter first mixed factor $3\ \frac{1}{2}$ |
| `2 [.] 2 [.] 3 [×]` | 0 | 0 | 0 | 28/3 | Multiply by $2\ \frac{2}{3}$; unreduced product is $\frac{28}{3}$ |
| `1 [.] 1 [.] 6 [÷]` | 0 | 0 | 0 | 8 | Divide by $1\ \frac{1}{6}$; stack resolves directly to exact integer 8. |

Chained mixed operations resolve to exact integer **`8`** with zero parentheses and zero scratch paper!

---

## 5.5 Step-by-Step Simplify (`[g] [SIMP]`): Watching Common Factors Peel Away

In 4th and 5th grade, simplifying a fraction to lowest terms is one of the most important skills you learn. When you drop two $\frac{1}{4}$ blocks ($42.0\text{ mm}$) and one $\frac{1}{2}$ block ($42.0\text{ mm}$) into your Twin Comparator Well, their top edges stand completely flush *([Dienes, 1960](sc6/appendix-c-formulas-and-conversions.md#cite-dienes1960); [Singapore MOE, 2014](sc6/appendix-c-formulas-and-conversions.md#cite-singapore2014))*—showing your fingers that $\frac{2}{4}$ and $\frac{1}{2}$ are the exact same height, just built with fewer blocks!

![Fraction Studio Gauge Comparison: Visual and Tactile Height Verification](../assets/renders/fraction-studio-gauge-comparison.png)

On your SC-6, **Step-by-Step Simplify (`[g] [SIMP]`)** does the exact same thing on screen:
- If your fraction shares a common factor between top and bottom, pressing `[g] [SIMP]` divides out the factor and shows the simpler fraction.
- If your fraction is already as simple as it can get (the top and bottom share no factor greater than $1$), pressing `[g] [SIMP]` flashes **`"LOWEST TERMS"`** across the status bar!

### 5.5.1 Try Simplifying $\frac{12}{18}$ Step by Step
Suppose you stack twelve $\frac{1}{18}$ unit slices ($12 \times 4.67\text{ mm} = 56.0\text{ mm}$) in Well A and two yellow $\frac{1}{3}$ blocks ($2 \times 28.0\text{ mm} = 56.0\text{ mm}$) in Well B. Their tops match at $56.0\text{ mm}$, proving $\frac{12}{18} = \frac{2}{3}$. Now watch `[g] [SIMP]` prove it on the stack:
1. Enter $\frac{12}{18}$ using two-dot syntax: `[.] 12 [.] 18 [ENTER]`.
2. Press `[g] [SIMP]`: the calculator divides both $12$ and $18$ by their Greatest Common Factor ($6$), updating Register $X$ to **`2/3`** while keeping your original `12/18` visible in Register $Y$ for comparison!
3. Press `[g] [SIMP]` a second time: because $2$ and $3$ share no common factor greater than $1$, the screen flashes **`LOWEST TERMS`**!

| Keystroke | Register T | Register Z | Register Y | Register X (Display) |
| :--- | :--- | :--- | :--- | :--- |
| `[.] 12 [.] 18` | 0 | 0 | 0 | 12/18 |
| `[ENTER]` | 0 | 0 | 12/18 | 12/18 |
| `[g] [SIMP]` | 0 | 0 | 12/18 | 2/3 |
| `[g] [SIMP]` | 0 | 0 | 12/18 [STATUS: LOWEST TERMS] | 2/3 |

---

## 5.6 Adding & Subtracting Unlike Denominators with `[f] [LCM]` and `[GCF]`

![Fraction Studio: Common Denominator Discovery on 12-Socket Lid Tray Proving 1/3 (28.0 mm) + 1/4 (21.0 mm) = 7/12 (49.0 mm)](../assets/manuals/fraction_studio_common_denominator.png)

Remember our treehouse trim problem from the beginning of the chapter: how do you add $\frac{3}{8} + \frac{5}{12}$ when eighths and twelfths are different sizes? You need the **Least Common Denominator (LCD)**—which is simply the **Least Common Multiple (`[f] [LCM]`)** of the two denominators $8$ and $12$!

### 5.6.1 Finding the Least Common Denominator with `[f] [LCM]`
Instead of listing multiples on scrap paper, ask your SC-6 for the Least Common Multiple of $8$ and $12$ first, and then add the fractions right underneath it. Pressing `8 [ENTER] 12 [f] [LCM]` reveals $X = \mathbf{24}$, telling you at a glance that both fractions can be measured in **twenty-fourths** ($\frac{3}{8} = \frac{9}{24}$ and $\frac{5}{12} = \frac{10}{24}$, so $\frac{9}{24} + \frac{10}{24} = \frac{19}{24}$). Now add $\frac{3}{8} + \frac{5}{12}$ directly on the stack while `24` waits upstairs by pressing `[.] 3 [.] 8 [ENTER] [.] 5 [.] 12 [+]` to reach $X = \mathbf{19/24}$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[8] [ENTER]` | 0 | 0 | 8 | 8 |
| `12` | 0 | 0 | 8 | 12 |
| `[f] [LCM]` | 0 | 0 | 0 | 24 |
| `[.] 3 [.] 8` | 0 | 0 | 24 | 3/8 |
| `[ENTER]` | 0 | 24 | 3/8 | 3/8 |
| `[.] 5 [.] 12` | 0 | 24 | 3/8 | 5/12 |
| `[+]` | 0 | 0 | 24 | 19/24 |

Look at the bottom row of that table: Register $Y$ still holds the common denominator `24` right beside the exact fraction sum `19/24` in Register $X$!

### 5.6.2 The Backyard Treehouse Workshop: Like Fifths, Steel Gusset Plates & the Pharaoh's Unit-Fraction Trio
Climb up into the **Backyard Treehouse Workshop**, where construction lumber and steel brackets are measured in fractional yards and inches! First you will join two cedar deck planks that share the *same* denominator, then bolt together two steel corner plates with *different* denominators, and finally test Ancient Egypt's favorite three-fraction sum.

You begin by laying cedar deck planks across the elevated treehouse floor frame, fastening a plank covering $\frac{2}{5}\text{ yard}$ of the deck opening in the morning, and another plank covering $\frac{1}{5}\text{ yard}$ after lunch. Because both planks are measured in fifths, their denominators already match! Stack two $\frac{1}{5}$ blocks with one $\frac{1}{5}$ block in the Comparator Well to see why you only add the numerators ($2 + 1 = 3$), then fuse them on the stack by pressing `[.] 2 [.] 5 [ENTER] [.] 1 [.] 5 [+]` to obtain **`3/5`**. Sliding the morning plank `. 2 . 5` into $Y$ with `[ENTER]` ($X = 2/5$) and joining the afternoon plank `. 1 . 5 [+]` ($X = 3/5$) unites the fifths into **$\frac{3}{5}\text{ yard}$**.

Once the cedar deck planks are down, you turn back to the $\frac{3}{8}\text{-foot}$ oak trim and $\frac{5}{12}\text{-foot}$ pine trim we previewed at the beginning of the chapter—now paired with two custom steel gusset plates measuring $\frac{3}{8}\text{ inch}$ and $\frac{5}{12}\text{ inch}$ thick on the corner post! Unlike the fifths in the cedar deck planks, eighths and twelfths are different sizes: in the Comparator Well, three $\frac{1}{8}$ blocks ($31.5\text{ mm}$) and five $\frac{1}{12}$ blocks ($35.0\text{ mm}$) stack to $66.5\text{ mm}$ ($19 \times 3.5\text{ mm}$ twenty-fourth increments). Because we already saw how the Least Common Denominator of $24$ aligns both pieces ($\frac{9}{24} + \frac{10}{24}$), you can fuse them directly on the stack without touching `[f] [LCM]` first: pressing `[.] 3 [.] 8 [ENTER] [.] 5 [.] 12 [+]` loads `[.] 3 [.] 8` onto Shelf $Y$, adds `[.] 5 [.] 12` on Shelf $X$, and displays **`19/24`** ($\mathbf{19/24\text{ inch}}$) in a single step—and if you then trim a $\frac{5}{12}\text{-foot}$ rail off a $\frac{7}{8}\text{-foot}$ cedar board (`. 7 . 8 [ENTER] . 5 . 12 [-]`), that same 24ths common denominator ($\frac{21}{24} - \frac{10}{24}$) leaves $\mathbf{\frac{11}{24}\text{ foot}}$ of board with zero scratch-paper conversions! What if you chain *three* different denominators together? Remember the Pharaoh's bakers from the start of this chapter: Ancient Egyptian scribes loved writing fractions as sums of *unit fractions* (fractions with a $1$ on top), and their favorite puzzle trio was $\frac{1}{2} + \frac{1}{3} + \frac{1}{6}$ (where $\text{LCM}(2, 3, 6) = 6$, so $\frac{3}{6} + \frac{2}{6} + \frac{1}{6} = \frac{6}{6}$). Drop a scarlet $\frac{1}{2}$ block ($42\text{ mm}$), a yellow $\frac{1}{3}$ block ($28\text{ mm}$), and a green $\frac{1}{6}$ block ($14\text{ mm}$) into the Twin Comparator Well: $42 + 28 + 14 = 84.0\text{ mm}$, standing completely flush with the 1-Whole tower! Now watch them snap together into `1` on the stack when you press `[.] 1 [.] 2 [ENTER] [.] 1 [.] 3 [+] [.] 1 [.] 6 [+]` to reach **`6/6`**. Stacking the half `. 1 . 2` with `[ENTER]` ($X = 1/2$), adding the third `. 1 . 3 [+]` ($X = 5/6$), and dropping in the final sixth `. 1 . 6 [+]` ($X = 1$) makes the screen snap cleanly to **`1` Whole**!

### 5.6.3 Finding the Biggest Shared Factor with `[GCF]`
What if your worksheet asks: *"What is the Greatest Common Factor you should divide out of $\frac{24}{36}$ to reduce it in a single step?"* Tap the **`[GCF]`** key by keying in `24 [ENTER] 36 [GCF]` to see $X = \mathbf{12}$ on the display. Dividing both $24$ and $36$ by that shared factor of $12$ gives the lowest-terms fraction right away: $\frac{24 \div 12}{36 \div 12} = \mathbf{\frac{2}{3}}$.

### 5.6.4 The Secret Partner Rule: $\text{GCF} \times \text{LCM}$
Here is a neat number-theory secret you can test on your family: pick *any* two whole numbers, find their **Greatest Common Factor (`[GCF]`)** and their **Least Common Multiple (`[f] [LCM]`)**, and multiply those two answers together. You will get the **exact same product** as multiplying the two original numbers!
$$\text{Greatest Common Factor} \times \text{Least Common Multiple} = \text{First Number} \times \text{Second Number}$$

Try it on the stack with $18$ and $24$: finding their Greatest Common Factor with `18 [ENTER] 24 [GCF]` gives $X = \mathbf{6}$, and finding their Least Common Multiple with `18 [ENTER] 24 [f] [LCM]` gives $X = \mathbf{72}$. When you multiply $\text{GCF} \times \text{LCM}$ ($6 \times 72$) with `6 [ENTER] 72 [×]` to get $X = \mathbf{432}$, and then multiply the original numbers ($18 \times 24$) with `18 [ENTER] 24 [×]`, the stack lands on the exact same product: $X = \mathbf{432}$!

---

## 5.7 Bridging Fractions, Decimals, and Percents

Every fraction on your stack can be viewed as a decimal or a percentage—just like turning one of your physical Fraction Studio blocks in your hand to inspect its three laser-marked faces.

### 5.7.1 Terminating vs. Repeating Decimals (`[FDISP]` and `[f] [0.3̄]`)
When you convert a fraction to a decimal with `[FDISP]`, one of two things happens:
- **Terminating Decimals Stop Cleanly:** Fractions whose denominators divide evenly into powers of $10$ (like $2, 4, 5, 8, 10, 20, 25$) come to a clean stop: $\frac{1}{4} = 0.25$ and $\frac{3}{8} = 0.375$.
- **Repeating Decimals Loop in a Pattern Forever:** Fractions like thirds, sixths, and ninths repeat a pattern without end: $\frac{1}{3} = 0.3333\dots$, $\frac{2}{3} = 0.6666\dots$, and $\frac{1}{6} = 0.1666\dots$. Using the **Repeating Bar (`[f] [0.3̄]`)** mode, your SC-6 draws a crisp vinculum bar directly over the repeating digits (like $0.\overline{3}$) just like you write it in math class!

### 5.7.2 Why the Stack Makes Percent Tips and Discounts So Easy (`[%]`)
The word *percent* comes from the Latin *per centum*, meaning **"out of 100."** So $25\%$ simply means $\frac{25}{100} = 0.25$, and $15\%$ means $\frac{15}{100} = 0.15$.

On a regular calculator, finding a $15\%$ tip or discount on an $\$80.00$ bill and then adding or subtracting it from $\$80.00$ can be clumsy if the starting $\$80.00$ disappears. On your SC-6, watch what happens when you put `80` on Shelf $Y$, type `15` on Shelf $X$, and press `[%]`: keying in `80 [ENTER] 15 [%]` produces $X = \mathbf{12.00}$ (the $\$12.00$ tip appears on Shelf $X$, **while your base $\$80.00$ bill stays waiting on Shelf $Y$!**). Want the total bill with tip? Just tap `[+]` to unite them into $X = \mathbf{92.00}$. And what if that $15\%$ was a store discount instead of a tip? Just tap `[-]` ($80 - 12 = \$68.00$)! Because Shelf $Y$ keeps your starting price alive, adding a tax or tip or subtracting a sale discount takes just one extra tap.

### 5.7.3 The Farmer's Market & Nursery Percent Counter
Ride your bike over to the regional **Farmer's Market & Plant Nursery**, where you can test how Shelf $Y$ holds your base bill when calculating a cafe tip, and how **`[f] [LASTX]`** rescues the starting height when measuring a giant sunflower's percent growth spurt!

At the market cafe counter, you want to leave a $15\%$ tip on a $\$48.00$ lunch order for the farm crew. Mentally, $10\%$ of $\$48.00$ is $\$4.80$, and half of that ($5\%$) is $\$2.40$, which add up to $\$7.20$. On the SC-6, pressing `[%]` computes $\$7.20$ on Shelf $X$ while **keeping $\$48.00$ waiting on Shelf $Y$**—so a single tap of `[+]` finishes the whole bill: `48 [ENTER] 15 [%]` $\longrightarrow X = \$7.20$ tip, then press `[+]` $\longrightarrow X = \$55.20$ total!

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `48 [ENTER]` | 0 | 0 | 48 | 48 | Enter base restaurant bill into holding Register $Y$ |
| `15 [%]` | 0 | 0 | 48 | 7.20 | Calculate 15% tip ($0.15 \times 48 = 7.20$); base \$48 preserved in $Y$ |
| `[+]` | 0 | 0 | 0 | 55.20 | Add tip directly to base bill in $Y$ without re-entering numbers |

Holding the base bill in Register $Y$ lets a single `[+]` stroke yield the total bill of **$\$55.20$**. Right outside the cafe at the plant nursery stall, a prize sunflower stood $80\text{ cm}$ tall last Saturday and towers at $100\text{ cm}$ today! To find the percent increase, you first subtract the $80\text{ cm}$ starting height ($100 - 80 = 20\text{ cm}$ of new growth) and then divide by that *exact same* $80\text{ cm}$ starting height. Instead of typing `80` a second time, press **`[f] [LASTX]`** to rescue `80` straight from backup memory: `100 [ENTER] 80 [-] [f] [LASTX] [÷] 100 [×]`. Finding the growth spurt with `100 [ENTER] 80 [-]` ($X = 20$), rescuing the $80\text{ cm}$ baseline via `[f] [LASTX] [÷]` ($X = 0.25$), and scaling by `100 [×]` ($X = 25$) confirms a **$25\%$ growth spurt** with zero re-typing!

---

## 5.8 Ratio Mode & Ratio Table Studio (`[g] [a:b]`)

What is the difference between a **fraction** and a **ratio**? Suppose you mix **2 cups of lemon juice** with **6 cups of water** to make a pitcher of lemonade:
- The **part-to-part ratio** compares lemon juice to water: **`2:6`** (which simplifies to **`1:3`**—1 cup of lemon juice for every 3 cups of water).
- The **part-to-whole fraction** compares lemon juice to the *entire pitcher* ($2 + 6 = 8$ total cups): $\frac{2}{8} = \mathbf{\frac{1}{4}}$ of the pitcher is lemon juice.

On an ordinary calculator, if you try to enter the ratio $15:25$ using division (`15 ÷ 25 =`), it turns your ratio into the decimal `0.6`, destroying the two parts! On your SC-6, **Ratio Mode (`[g] [a:b]`)** (`[g]` then `[GCF]`) keeps both sides of the ratio together so you can simplify ratios with `[g] [SIMP]` or scale recipes and blueprints up and down with `[×]`:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[.] 15 [.] 25` | 0 | 0 | 0 | 15/25 |
| `[g] [a:b]` | 0 | 0 | 0 | 15:25 |
| `[g] [SIMP]` | 0 | 0 | 0 | 3:5 |
| `[2] [×]` | 0 | 0 | 0 | 6:10 |
| `[g] [SIMP]` | 0 | 0 | 0 | 3:5 |

And if you already have a part-to-whole fraction like $\frac{15}{25}$ committed on the stack (15 selected items out of 25 total items), pressing `[g] [a:b]` converts it into the **part-to-part ratio** comparing the 15 selected items to the remaining $25 - 15 = 10$ items (**`15:10`**, which simplifies with `[g] [SIMP]` to **`3:2`**)!

### 5.8.1 Tape Diagrams, Unit Rates & Percents in Action

Watch how your Counting Tiles and Ratio Mode (`[g] [a:b]`) solve three classic middle-grades proportional puzzles:

1. **Tape Diagrams & Bicycle Gear Ratios:**
   - **Western Scrub-Jay Anti-Theft Seed Caching (Tape Diagram):** When a rival bird is watching, a clever western scrub-jay re-hides $60$ pine seeds in a $7:5$ ratio of **secret trays** to **open trays** to fool the thief. Build a physical **Tape Diagram** on your desk by lining up **7 Red Counting Tiles** next to **5 Blue Counting Tiles**: together they form $7 + 5 = 12$ equal boxes sharing $60$ seeds, so each box holds $60 \div 12 = \mathbf{5\text{ seeds}}$ (`60 [ENTER] 7 [ENTER] 5 [+] [÷]` $\longrightarrow \mathbf{5}$). Multiplying $5\text{ seeds}$ by $7$ boxes and $5$ boxes reveals **$35$ secret seeds** and **$25$ open seeds**!
   - **Bicycle Gear Ratios (`3:1`):** A bicycle chain links every tooth of the front pedal chainring to one tooth of the rear wheel sprocket. If a $48\text{-tooth}$ front gear pulls a $16\text{-tooth}$ rear sprocket, keying `[.] 48 [.] 16 [g] [a:b] [g] [SIMP]` (or `48 [ENTER] 16 [GCF]` to see the shared factor of $16$) simplifies the ratio to **`3:1`**—meaning the back wheel spins **$3$ full turns** for every **$1$ turn of your pedals**!
2. **Unit Rates (Finding the "Per-One" Speed):**
   - **3D Printer Filament Feed Speed:** A 3D printer extruder pulls $45\text{ cm}$ of plastic filament in $18\text{ seconds}$. Dividing `45 [ENTER] 18 [÷]` finds the **unit rate** for $1\text{ second}$ (**$2.5\text{ cm/s}$**), and tapping `50 [×]` immediately predicts it will feed **$125\text{ cm}$** of filament in $50\text{ seconds}$.
   - **Woodpecker Foraging Speed:** Which bird taps faster—Woodpecker A drumming $220\text{ taps}$ in $4\text{ minutes}$ (`220 [ENTER] 4 [÷]` $\longrightarrow \mathbf{55\text{ taps/min}}$) or Woodpecker B drumming $285\text{ taps}$ in $5\text{ minutes}$ (`285 [ENTER] 5 [÷]` $\longrightarrow \mathbf{57\text{ taps/min}}$)? Finding the 1-minute unit rate makes the comparison fair and instant!
3. **Turning a Fraction Score into a Percent:**
   - **Alex the African Grey Parrot's Number Trials:** In Dr. Irene Pepperberg's cognition lab, Alex the African Grey parrot answered $21$ out of $24$ spoken counting and tray-addition questions accurately. Keying `[.] 21 [.] 24 [g] [SIMP]` reduces Alex's score to **`7/8`**; tapping `[FDISP]` flips it to **`0.875`**, and multiplying by `100 [×]` reveals **`87.5%`** accuracy!

### 5.8.2 The Architectural Scale Model Lab
Now step into an **Architectural Scale Model Lab**, where model makers build miniature working drawbridges and civic plazas. Let's use **Ratio Mode (`[g] [a:b]`)** to simplify a drawbridge gear pair without turning it into a decimal, and build a 3-part Tape Diagram on the stack to mix mortar for miniature stone pavers.

In an architectural scale model, a motorized drawbridge operates using a $12\text{-tooth}$ motor pinion meshed with a $36\text{-tooth}$ sector gear. Laying a $12\text{-unit}$ block stack beside three $12\text{-unit}$ stacks shows that the big gear has $3$ times as many teeth as the small gear. Enter the tooth counts into Ratio Mode (`[g] [a:b]`) and simplify directly with `[g] [SIMP]` by pressing `[.] 12 [.] 36 [g] [a:b] [g] [SIMP]` to display **`1:3`**. Keying in the tooth pair `. 12 . 36` ($X = 12/36$), flipping into Ratio Mode with `[g] [a:b]` ($X = 12:36$), and tapping `[g] [SIMP]` ($X = 1:3$) factors out $12$ to reveal the clean **`1:3` gear ratio**!

Next to the drawbridge, casting miniature stone pavers for the civic plaza model blends **cement, sand, and fine gravel** in a **$1:2:3$ ratio** to produce $12\text{ cubic feet}$ of mortar. How many cubic feet sit in each single part? Stack $1$ gray tile (cement), $2$ gold tiles (sand), and $3$ white tiles (gravel) on your desk to build a $6\text{-tile}$ column ($1 + 2 + 3 = 6$ total parts). Because $6$ equal parts share $12\text{ cubic feet}$, add the parts on the stack, type `12`, and use `[x⇄y]` to put `12` in the left seat ($Y$) before dividing by `6`: pressing `1 [ENTER] 2 [+] 3 [+] 12 [x⇄y] [÷]` divides the $12\text{ cu ft}$ batch by $6$ parts to show **`2`** cubic feet per part:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `1 [ENTER] 2 [+]` | 0 | 0 | 0 | 3 | Add cement and sand parts ($1 + 2 = 3$) |
| `3 [+]` | 0 | 0 | 0 | 6 | Add gravel parts: $3 + 3 = 6\text{ total parts}$ |
| `12 [x⇄y] [÷]` | 0 | 0 | 0 | 2 | Divide 12 cu ft batch by 6 parts to find $2\text{ cu ft per part}$ |

Each single part equals **$2\text{ cu ft}$**—giving $2\text{ cu ft}$ cement ($1 \times 2$), $4\text{ cu ft}$ sand ($2 \times 2$), and $6\text{ cu ft}$ gravel ($3 \times 2$), which add right back up to the full $12\text{ cu ft}$ mortar batch!

---

### 5.8.3 Key Insights & Common Pitfalls

- **The Unreduced Fraction Revelation:** When multiplying $\frac{1}{2} \times \frac{2}{3}$, the SC-6 shows `2/6`, verifying $1 \times 2 = 2$ and $2 \times 3 = 6$. Pressing `[g] [SIMP]` reduces it to `1/3` and flashes `LOWEST TERMS`.
- **Why We Don't Add Denominators:** Stacking a $\frac{1}{2}$ tower ($42\text{ mm}$) and $\frac{1}{4}$ tower ($21\text{ mm}$) in Well A ($63\text{ mm}$) vs. two $\frac{1}{6}$ towers ($28\text{ mm}$) in Well B physically proves why $\frac{1}{2} + \frac{1}{4} \ne \frac{2}{6}$. Well B is far too short! Three $\frac{1}{4}$ towers ($63\text{ mm}$) align flush.
- **Lemonade Ratios (Parts vs. Whole):** Mixing 2 cups lemon juice with 6 cups water gives a part-to-part ratio of $2:6$ ($1:3$). But the total volume is $1 + 3 = 4$ cups, meaning lemon juice represents $\frac{1}{4}$ of the total pitcher.

---

## 5.9 Quick Troubleshooting Guide

If a fraction or ratio result looks unexpected, check this quick reference table:

| What Happened on Your Screen | Why It Happened | How to Fix It |
|:---|:---|:---|
| **1. Entered `3.4` for `3/4`** | Used single dot (decimal syntax). | Use two dots: `[.] 3 [.] 4` is $3/4$. |
| **2. Result of `1/2 × 2/3` shows `2/6` instead of `1/3`** | Confused unreduced default with error. | Calculator preserves your steps; tap `[g] [SIMP]`. |
| **3. `[g] [SIMP]` flashes `LOWEST TERMS` without changing digits** | Fraction is already irreducible. | $3/7$ has no common factors; it is already in lowest terms. |
| **4. Screen displays decimal `0.75` when fraction was wanted** | In decimal display mode. | Tap `[FDISP]` to toggle display to fraction. |
| **5. Added numerators & denoms: `1/2 + 1/4 = 2/6`** | Treating fractions as disconnected numbers. | Use Fraction Towers in the Twin Comparator Well. |
| **6. Confused ratio `3:5` with fraction `3/5`** | Part-to-part vs. part-to-whole confusion. | $3:5$ has 8 total parts; the fraction of the whole is $3/8$. |
| **7. Wanted mixed number `2 3/4` but saw `11/4`** | Screen in improper fraction mode. | Tap `[a ᵇ/c]` to toggle to mixed number display. |
| **8. Percent tip calculated but total bill missing** | Base in Register Y was lost by clearing screen. | Base stays in Register Y; tap `[+]` to add tip to bill. |
| **9. Cannot find LCD of 8 and 12 on scratch paper** | Manually guessing multiples. | Use hardware key: `8 [ENTER] 12 [f] [LCM]` $\to$ 24. |
| **10. Saw `0.3333333333` without knowing if it repeats** | Converting $1/3$ to decimal display. | Notice the `[f] [0.3̄]` repeating bar on the LCD showing repeating decimals. |

---

### 5.9.1 Decimal Approximations vs. Exact Fraction Towers & Ratios

Now that you have explored two-dot fraction entry, `[g] [SIMP]`, `[f] [LCM]`, `[%]`, and Ratio Mode (`[g] [a:b]`), compare how standard infix calculators handle fraction entry and ratio scaling against your SC-6 and $84\text{ mm}$ Fraction Studio towers:

| Challenge / Real-World Task | The Algebraic Calculator Trap (Infix) | Algebraic Keystrokes & Clutter | The StackCalc + Blocks Method (RPN Stack + Visual Studio) | StackCalc Keystrokes | The Stack Advantage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Unlike Denominators Sum:** Rafter bolt spacing: $\frac{3}{8} + \frac{5}{12} = \frac{19}{24}$ | Infix fraction entry requires opening fraction templates or nested parentheses. Forgetting a parenthesis divides 8 by 5 prematurely, producing a misleading decimal. Common denominator (24) is hidden. | `( 3 / 8 ) + ( 5 / 12 ) =` (15 keystrokes, syntax brackets, invisible LCD) | **Hardware LCD via `[f] [LCM]` + Two-Dot Entry:** Single-tap `[f] [LCM]` extracts LCD ($24$). Two-dot syntax `. 3 . 8 [ENTER] . 5 . 12 [+]` computes $19/24$ directly with unreduced transparency. | `. 3 . 8 [ENTER] . 5 . 12 [+]` (10 keystrokes) | **33% fewer keystrokes:** Zero parentheses, zero mode shifting; students see the exact common denominator and rational sum simultaneously. |
| **Step-by-Step Simplification:** Bulk syrup reduction: $\frac{12}{18} \longrightarrow \frac{2}{3}$ | Modern algebraic calculators automatically reduce fractions immediately, hiding numerator and denominator multiplication ($1 \times 2 = 2, 2 \times 3 = 6$). Students cannot see which common factor was divided out. | `1 2 / 1 8 =` $\to 2/3$ (Skips educational factoring; black-box reduction) | **Deliberate Unreduced Default + `[g] [SIMP]`:** Preserves $12/18$ on the stack. Pressing `[g] [SIMP]` factors out 6 to show $2/3$, flashing `LOWEST TERMS` only when irreducible. | `. 12 . 18 [g] [SIMP]` (7 keystrokes) | **Step-by-Step Transparency:** Honors student work; common factors are peeled away step-by-step matching physical Fraction Studio towers. |
| **Chained Mixed-Number Evaluation:** Scale model ratio batching: $(3\ \frac{1}{2} \times 2\ \frac{2}{3}) \div 1\ \frac{1}{6}$ | Chained mixed numbers require massive nested parentheses `( 3 + 1 / 2 ) × ( 2 + 2 / 3 ) / ( 1 + 1 / 6 ) =`. Forgetting an outer bracket divides prematurely, corrupting the calculation by orders of magnitude. | `( 3 + 1 / 2 ) × ( 2 + 2 / 3 ) / ( 1 + 1 / 6 ) =` (33 keystrokes, 6 parentheses) | **Natural Two-Dot RPN Stack Fusion:** Two-dot syntax enters whole and fractional parts directly. The 4-register stack holds intermediate rational products with zero parentheses or scratch paper. | `3 . 1 . 2 [ENTER] 2 . 2 . 3 [×] 1 . 1 . 6 [÷]` (17 keystrokes) | **48% fewer keystrokes:** Zero parentheses; stack resolves directly to exact integer 8 with intermediate rational verification on screen. |
| **Part-to-Part Ratio Scaling:** Drawbridge gear ratio reduction & scale: $15:25 \longrightarrow 3:5 \longrightarrow 6:10$ | Algebraic calculators treat ratios as division, converting $15:25$ into decimal $0.6$. The proportional relationship between parts is permanently lost. | `1 5 / 2 5 =` $\to 0.6$ (Ratios destroyed into decimal quotient; cannot scale terms) | **Dedicated Ratio Mode (`[g] [a:b]`):** Keeps the first and second numbers of the simplified ratio together. Pressing `[g] [SIMP]` reduces to $3:5$; multiplying by 2 scales both parts simultaneously to $6:10$. | `. 15 . 25 [g] [a:b] [g] [SIMP] 2 [×]` (11 keystrokes) | **True Ratio Arithmetic:** Scales recipes, gear teeth, and blueprints without converting to decimals or losing component parts. |

---

## 5.10 Where to Go Next: Companion Workbook Quests & Kitchen-Table Challenges

> *For 38 additional worked problems with full 4-register stack tables, see Chapter 5 of the [SC-6 Elementary Companion Problem & Activity Workbook](../curriculum/sc6-elementary-companion-workbook.md).*

Ready to take your Fraction Studio towers and two-dot stack skills beyond this chapter? Open your companion resources and try these three hands-on challenges at home or in the classroom:

- **[Big Ideas Math Middle School Supplement](../curriculum/big-ideas-middle-school-sc6-workbook.md):** Dive into **Unit 2: Fractions & Decimals (Sections 2.1–2.5)** and **Unit 3: Ratios, Rates & Percents (Sections 3.1–3.5)** for practice sheets featuring **Robot Speed Gears**, **Aesop's Crow Water-Displacement Puzzle**, **Bicycle Gear Ratios**, **Western Scrub-Jay Tape Diagrams**, and **Alex the African Grey Parrot's Percent Accuracy**.
- **Timed Proficiency Trials & 12-Unit Curriculum Guide:** Challenge a classmate or parent to the **60-Second Lowest-Terms & LCD Relay** in **Unit 5 of the Curriculum Guide**, racing to simplify unruly fractions with `[g] [SIMP]` and predict common denominators before tapping `[f] [LCM]`.

### 5.10.1 Three Hands-On Kitchen-Table Quests
1. **The Water-Glass Musical Scale (`1/2`, `2/3`, `3/4`, `5/8`):** Line up four identical drinking glasses on the kitchen table. Leave the first glass empty, fill the second to $\frac{1}{2}$, the third to $\frac{2}{3}$, and the fourth to $\frac{3}{4}$ (use your $84\text{ mm}$ Fraction Towers next to the glasses as a height gauge). Gently tap each glass with a spoon to hear the musical intervals, then use two-dot syntax and `[-]` on your SC-6 to find the exact fractional difference in water height between each pair of notes.
2. **The Double-Batch Cookie & Pancake Scaler (`[g] [a:b]` and `[f] [LASTX]`):** Grab a favorite family recipe card that uses fractional cups and teaspoons (like $1\ \frac{3}{4}$ cups flour and $\frac{3}{8}$ teaspoon cinnamon). Use your SC-6 to scale every ingredient by $1\ \frac{1}{2}$ for a crowd—and use `[f] [LASTX]` to keep the scale factor ready at your fingertips without re-typing it.
3. **The Infinite Zeno Paper-Folding Challenge:** Take a strip of paper $1$ unit long. Fold it in half ($\frac{1}{2}$), fold the remaining half in half ($\frac{1}{4}$), then $\frac{1}{8}$, $\frac{1}{16}$, and $\frac{1}{32}$. Keep a running sum on your SC-6 (`[+]`) after every fold and tap `[FDISP]` to watch the decimal march closer and closer to $1.0000000$!

---

## 5.11 Chapter Summary & Looking Ahead

Rational numbers on the SC-6 connect physical height comparison to exact symbolic arithmetic:

1. **Proportional Heights:** Your 84 mm Fraction Studio blocks give rational numbers physical geometry and tactile mass, proving equivalence in the Comparator Well.
2. **Two-Dot Syntax:** Entering proper, improper, and mixed numbers requires only natural decimal point presses (`. n . d`).
3. **Unreduced Arithmetic:** The SC-6 preserves your mathematical work by displaying unreduced fractions by default.
4. **Step-by-Step Simplify (`[g] [SIMP]`):** Step-by-step reduction reveals factor cancellation with lowest-terms feedback.
5. **Number Theory Power:** Hardware `[GCF]` and `[f] [LCM]` verify the secret partner rule ($\text{Greatest Common Factor} \times \text{Least Common Multiple} = \text{First Number} \times \text{Second Number}$).
6. **Proportional Reasoning:** Ratio Mode (`[g] [a:b]`), percentage calculations (`[%]`), and `[f] [LASTX]` support music, carpentry, and financial calculations.

In **[Chapter 06: Geometry, Surface Area & Planetary Geared Time](sc6/06-geometry-surface-area.md)**, you will transition into spatial and geometric dimensions. You will build 3D stacked block prisms and area models, master the **Master Surface Area Technique via Stats Mode (`[Σ+]`)**, calculate 3D prism and pyramid volumes, and explore continuous modulo-60 elapsed time on the Planetary Geared Clock (`[🕒]`).

---

# Chapter 6: Geometry, Surface Area & Planetary Geared Time

## 6.1 The Antarctic Penguin Huddle & Galileo's Square-Cube Secret: How Geometry Saves Lives at -40°C

Out on the Antarctic ice shelf in the middle of winter, the air temperature plummets to $-40^\circ\text{C}$ as howling gale-force blizzards blast across the frozen tundra at $100\text{ km/h}$. Standing directly in that polar gale are thousands of Emperor penguins and their newborn chicks—surviving without shelter, fire, or blankets by relying on one of the deepest geometric laws in the physical universe.

An adult Emperor penguin weighs $35\text{ kg}$, but a baby chick weighs under $1\text{ kg}$. Why does an isolated chick freeze in under 10 minutes, while an adult stands calmly against the polar gale?

### 6.1.1 The Secret Ratio: Volume vs. Surface Area
First discovered by Galileo Galilei in 1638 as the **Square-Cube Law** *([Galilei, 1638](sc6/appendix-c-formulas-and-conversions.md#cite-galilei1638))*, every living creature's survival depends on the balance between two geometric measurements:
- **Volume** is where an animal stores and produces internal body heat (proportional to its biological mass).
- **Surface Area** is the outer skin where heat escapes into the freezing wind.

A baby chick has a massive amount of skin (surface area) compared to its tiny body volume. Heat radiates out into the arctic gale far faster than the chick's little heart and metabolism can generate it. Alone on the ice, the chick cannot survive.

### 6.1.2 Why Huddling Works: Shared Walls, Less Exposed Skin
What do the penguins do? As physiological field studies in Antarctica have documented *([Gilbert et al., 2006](sc6/appendix-c-formulas-and-conversions.md#cite-gilbert2006))*, hundreds of Emperor penguins press tightly together shoulder-to-shoulder into a slowly circulating hexagonal huddle.

Suddenly, all their interior skin touches warm, insulating feathers instead of sub-zero wind. To the freezing blizzard, 500 huddled chicks act as **one giant super-organism**. Their combined volume is massive, but their exposed surface area is drastically reduced. Inside the center of the rotating huddle, the ambient temperature climbs to a toasty $+20^\circ\text{C}$ while the blizzard rages at $-40^\circ\text{C}$ outside. Geometry literally keeps them alive.

### 6.1.3 Prove the Penguin Huddle Yourself with 8 Unit Miniblocks
Grab **8 Unit Miniblocks** ($19.0 \times 19.0 \times 7.0\text{ mm}$ visible $1\text{U}$ blocks) from your **Counting & Array Studio** or **Place Value Studio**:
- **Standing Alone in the Wind:** Spread the 8 blocks apart on your desk like 8 lone penguin chicks. Every block has **6 exposed faces** touching the cold air, so all 8 blocks expose $8 \times 6 = \mathbf{48\text{ outer block faces}}$ of skin.
- **Pressed Together in a $2 \times 2 \times 2$ Huddle:** Now dock all 8 blocks tightly together into a single $2 \times 2 \times 2$ block prism (four $2\text{-block}$ towers docked side-by-side in a $2 \times 2$ square). The total volume is still 8 blocks, but each of the 6 outer sides is now just a $2 \times 2 = 4\text{-face}$ wall—only $6 \times 4 = \mathbf{24\text{ exposed faces}}$. Half of their cold surface area ($\mathbf{-50\%}$) disappeared inside the warm huddle!

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `8 [ENTER] 6 [×]` | 0 | 0 | 0 | 48 | 8 lone cubes $\times 6$ faces $= 48$ cold exposed faces |
| 2 | `6 [ENTER] 4 [×]` | 0 | 0 | 48 | 24 | $2 \times 2 \times 2$ huddle has $6 \times 4 = 24$ exposed faces |
| 3 | `[g] [%CHG]` | 0 | 0 | 48 | **-50** | Huddling cuts exposed heat-loss area by **$-50\%$**. |

### 6.1.4 The Kitchen-Table Proof: French Fries vs. Baked Potatoes

You observe this exact same surface-area-to-volume geometry every day in your kitchen:
- **The Whole Potato:** A whole baked potato takes 45 to 60 minutes to cook through in a $400^\circ\text{F}$ oven because heat must conduct slowly through its large volume.
- **The French Fry:** Slice that identical potato into thin batons, and it cooks crisp in boiling oil in just 3 minutes. Slicing didn't change the potato's volume—it multiplied its exposed surface area by over **600%**.
- **The Ice Cube:** A single large ice sphere melts slowly in a drink; crushed ice chills your juice in 10 seconds because surface area is everywhere.

When you calculate surface area on your SC-6, you are not wrapping theoretical gift boxes. You are calculating the universal mathematical law governing heat exchange, fluid drag, chemical reaction rates, and living thermodynamics.

![SC-6 Clock Mode displaying 3:30 on the geared dial](../assets/manuals/screenshots/sc6_planetary_clock_mode.png)

---

## 6.2 Hands-On Studio: 3D Block Prisms, L-Frame Area Tiles & Planetary Gear Trains

Geometry is inherently spatial, yet many school textbooks reduce three-dimensional shapes to flat drawings on a page. When you calculate the surface area of a box or the volume of a cylinder, you don't need to struggle with confusing letter formulas. Throughout this chapter, your SC-6 grounds every flat shape, 3D solid, and moving clock hand in physical 3D-printed blocks, L-Frame area tiles, polyhedral solids, and planetary gear trains you can hold and turn in your hands.

![2-Digit Multiplication Rectangles & Area Studio: Concrete 2D Grids and Partial-Product Tiles](../assets/manuals/algebra_factoring_area.png)

![L-Frame Area Studio: Splitting 2-Digit Multiplication Rectangles and Comparing Square Borders](../assets/manuals/algebra_difference_of_squares.png)

### 6.2.1 Hands-On Geometry & Time Studio Kit

1. **19 mm Stacking Unit Tiles & 3D Block Prisms + Polyhedral Solids:**
   - $19.0 \times 19.0\text{ mm}$ precision gravity-docking base & socket ($7.0\text{ mm}$ visible $1\text{U}$ height; stack of 3 tiles $= 21.0\text{ mm}$; stack of 12 tiles $= 84.0\text{ mm}$ tower).
   - Build 3D rectangular prisms on the Snapfinity lid grid and inspect all 6 outer walls (top/bottom, front/back, left/right), or inspect the faces, edges, and vertices of the 5 Platonic polyhedra ($d4, d6, d8, d12, d20$) from your Polyhedral Dice set.
   - Printable cardstock cutout nets in **Appendix A** let you score, fold, and tape full-scale 3D paper boxes and fraction towers.
2. **2-Digit Multiplication Rectangles & $90^\circ$ L-Frame Stage:**
   - Interlocking horizontal and vertical guide rails frame 2-digit multiplication rectangles (area models, like splitting $12 \times 13$ into a $10 \times 10 = 100$ flat, five $10 \times 1$ ten-rods $= 50$, and six $1 \times 1$ unit tiles $= 6$, totaling $100 + 50 + 6 = 156$).
3. **Planetary Geared Clock & $360^\circ$ Unit Circle Volvelle:**
   - Exact $12.0000:1$ compound planetary reduction gear train with 4 removable $90^\circ$ quadrant sectors.
   - Continuous, non-stepping hour hand moves in lockstep with minutes alongside the $120\text{ mm}$ dual-ring rotary Volvelle protractor, matching your SC-6's Planetary Clock mode (`[🕒]`) and time-conversion keys (`[f] [▸HR]` and `[g] [▸HMS]`).

### 6.2.2 The Six-Wall Prism Inspection Experience
When you build a 3D rectangular prism out of **Counting Tiles** on your Snapfinity lid (or unfold a printable cardstock net from Appendix A), the concept of surface area ceases to be an equation to memorize. All six outer walls of a $5 \times 4 \times 3$ rectangular prism lie open to direct tactile inspection:
- Two identical horizontal faces (the top lid and bottom floor): $5\text{ units} \times 4\text{ units} = 20\text{ square units}$ each.
- Two identical long vertical walls (the front and back panels): $5\text{ units} \times 3\text{ units} = 15\text{ square units}$ each.
- Two identical side walls (the left and right end caps): $4\text{ units} \times 3\text{ units} = 12\text{ square units}$ each.

You don't need to write down intermediate numbers on scratch paper. Using your SC-6, you first clear the statistical memory with `[g] [CLΣ]`, then enter each opposing face pair directly into the calculator's hardware statistical accumulator using the `[Σ+]` key (and if a wall ever has a window or door cutout, you can even subtract that opening from your basket with `[f] [Σ-]`). As you accumulate each pair, the LCD displays your face-pair count: `n = 1`, `n = 2`, `n = 3`. Finally, tapping `[f] [Σx]` reveals your total surface area: $94\text{ cm}^2$. Rotate your 3D block prism in your hands (or fold the three pairs of cardstock panels together): *total surface area is simply the sum of all flat 2D faces wrapping the 3D solid*.

| Prism Face Pair | Opposing Faces | Dimensions | Face Area | Pair Area ($2 \times \text{Face Area}$) |
| :--- | :--- | :--- | :--- | :--- |
| **Pair 1** | Top Face & Bottom Face | $5\text{ cm} \times 4\text{ cm}$ | $20\text{ cm}^2$ | $40\text{ cm}^2$ |
| **Pair 2** | Front Panel & Back Panel | $5\text{ cm} \times 3\text{ cm}$ | $15\text{ cm}^2$ | $30\text{ cm}^2$ |
| **Pair 3** | Left End & Right End | $4\text{ cm} \times 3\text{ cm}$ | $12\text{ cm}^2$ | $24\text{ cm}^2$ |
| **Total Surface Area** | All 6 Unfolded Faces | $5 \times 4 \times 3\text{ cm}$ | — | **$94\text{ cm}^2$** |

### 6.2.3 Interlocking Unit Cubes and Counting Tile Volumes
Volume measures internal capacity—how many cubic units fill a solid without gaps or overlaps. By assembling 24 unit cubes from your Base-10 Place Value Studio (or 24 Counting Tiles, each $19.0 \times 19.0\text{ mm}$ with a $7.0\text{ mm}$ visible $1\text{U}$ body height) into arrays of $2 \times 3 \times 4$, $1 \times 2 \times 12$, and $2 \times 2 \times 6$, you physically discover that while the footprint and height change, the total volume remains constant at 24 cubic units.

### 6.2.4 How Stack Drops Build 3D Volumes Step by Step
On the SC-6, Stack Math works just like stacking blocks to build a room, whether you use the step-by-step multiplication keys or dedicated 3D volume solvers like `[f] [PRISM]` and `[g] [CONE]`:

1. **Laying Down the Floor:** When you type $\text{Length} \ \mathtt{ENTER} \ \text{Width}$, you set the floor dimensions on the two active shelves (Length on Level $Y$, Width on Level $X$).
2. **Floor Area:** Tapping `[×]` multiplies length by width. The two numbers fuse together onto Level $X$ to give the floor area ($\text{Floor Area} = \text{Length} \times \text{Width}$).
3. **Raising the Walls:** Now type $\text{Height}$ and tap `[×]`. The floor area multiplies by the height, turning the flat floor into a solid 3D box ($\text{Box Volume} = \text{Floor Area} \times \text{Height}$).

You never have to memorize a long, confusing formula all at once—you build your math step-by-step from the floor up *([Bruner, 1966](sc6/appendix-c-formulas-and-conversions.md#cite-bruner1966); [Pólya, 1945](sc6/appendix-c-formulas-and-conversions.md#cite-polya1945))*.

---

Before we can unfold and measure the complete outer skin of a 3D penguin huddle, a triangular A-frame camping tent, or a multi-panel spacecraft fairing, we first need to master the flat 2D building blocks that stitch every 3D solid together. Think about a cardboard cereal box or a sewn camping tent: before it was folded or stitched into three dimensions, every single wall started out as a flat 2D shape on a tabletop. Let's start on that flat tabletop with the rectangles, triangles, circles, parallelograms, trapezoids, and hexagons that form every 3D net.

## 6.3 2D Plane Geometry & Direct Area Solvers

Every flat shape has two different stories to tell: how far it is to walk all the way around its outside border (the **Perimeter**), and how many unit squares it takes to cover the space inside (the **Area**). Instead of memorizing disconnected letter formulas, let's see *why* each shape's rule works physically.

### 6.3.1 Rectangles and Squares (`[f] [RECT]`)
Picture walking around a rectangular school garden with four square corners. If you walk along one **Length** and turn the corner to walk along one **Width**, you have traced an L-shaped half-lap around the garden. Since the opposite two sides are identical twins, doubling that L-shaped half-lap wraps all the way around the **Perimeter**! Meanwhile, to cover the ground inside with square carpet tiles, you lay down $\text{Length}$ tiles in each row and repeat for $\text{Width}$ rows, multiplying them to find the **Area**:
$$\text{Perimeter} = (\text{Length} + \text{Width}) \times 2, \qquad \text{Rectangle Area} = \text{Length} \times \text{Width}$$

To see how both measurements work together in a real project, suppose your class is building a rectangular vegetable garden measuring $14\text{ meters}$ long and $8.5\text{ meters}$ wide. Before heading to the garden center, you need to know both the length of wooden fencing required to enclose all four sides of the garden and the total square meterage of weed-barrier fabric needed to carpet the soil inside.

To walk the perimeter on the stack, push the $14\text{-meter}$ length onto Register $Y$ and add the $8.5\text{-meter}$ width on Register $X$ to trace the L-shaped half-lap ($22.5\text{ m}$), then double that sum with `14 [ENTER] 8.5 [+] [2] [×]` to wrap all four sides in $\mathbf{45.00\text{ meters}}$ of wooden fencing. Next, to carpet the interior soil, multiply the length by the width with `14 [ENTER] 8.5 [×]` to uncover $\mathbf{119.00\text{ square meters}}$ of garden bed. Better yet, right after pressing `14 [ENTER] 8.5 [+]` for the half-perimeter $22.5$, the width `8.5` is still resting inside `LASTX`—so you can tap `14 [f] [LASTX] [×]` to compute the $119.00\text{ m}^2$ area while $22.5$ waits safely in Register $Y$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `14` | 0 | 0 | 0 | 14 |
| `[ENTER]` | 0 | 0 | 14 | 14 |
| `8.5` | 0 | 0 | 14 | $8.5$ |
| `[+]` | 0 | 0 | 0 | $22.5$ |
| `[2]` | 0 | 0 | $22.5$ | 2 |
| `[×]` | 0 | 0 | 0 | 45 |

When you want to find a rectangle's area in a single stroke, the SC-6 also provides the dedicated `[f] [RECT]` solver, which multiplies $\text{Length} \times \text{Width}$ directly: keying `14 [ENTER] 8.5 [f] [RECT]` lands straight on $X = \mathbf{119.00\text{ m}^2}$.

That same L-shaped half-lap rule works whenever you frame a sign, a picture, or a park kiosk! Suppose you are designing a community adventure park, and right at the entrance plaza sits a rectangular welcome bulletin board measuring $2.4\text{ meters}$ wide and $1.2\text{ meters}$ high that needs a weatherproof aluminum edging ribbon around all four sides. Model the kiosk proportions using a small $2 \times 4$ tile array on your desk and touch the top and right edges to see the L-shaped half-perimeter ($6$). Scaling up to the real $2.4\text{ m} \times 1.2\text{ m}$ dimensions, we walk the top edge `2.4` onto Register $Y$ with `[ENTER]`, turn the corner down the side `1.2` with `[+]` to form the $3.6\text{ m}$ half-perimeter, and double that L-shape across all four sides with `2.4 [ENTER] 1.2 [+] [2] [×]` to reach **`7.2`**—requiring $\mathbf{7.20\text{ meters}}$ of weatherproof framing ribbon.

What if a rectangle's length and width are the exact same size—a **square**, like a modular classroom carpet tile or a square playground sandpit? Instead of typing the side length twice, you can use the square key `[x²]` to multiply the side by itself in one tap. Suppose a square classroom carpet tile has a side length of $0.5\text{ meters}$. Entering `0.5` places the tile's side length ($0.5\text{ m}$) into Register $X$, and tapping `0.5 [x²]` squares Register $X$ in place ($\text{Square Area} = \text{Side} \times \text{Side} = 0.5 \times 0.5$), revealing an area of $X = \mathbf{0.25\text{ m}^2}$ without touching a single extra register.

Now step over to the toddler adventure zone right past the park welcome kiosk, which features a square sandpit with a side length of $3.5\text{ meters}$ that needs a heavy-duty waterproof canvas tarp to protect the sand from overnight rain. Lay out a square array of counting tiles ($3 \times 3$ or $4 \times 4$) to see how squaring a side length tiles the two-dimensional interior plane directly, turning a linear measure ($3.5\text{ m}$) into square meters ($\text{m}^2$). Keying `3.5 [x²]` on the SC-6 squares the $3.5\text{ m}$ side length in place on Register $X$ to land on **`12.25`**, sweeping the $3.5\text{ m}$ edge across itself into a $\mathbf{12.25\text{ m}^2}$ square tarp.

---

### 6.3.2 Triangles (`[g] [TRI]`) & Two-Triangle Parallelogram Proofs
Why does the area rule for *every* triangle divide by $2$? Imagine slicing a rectangular sandwich straight from one corner to the opposite corner: you get two identical right triangles, each holding exactly half of the sandwich! Even better, take *any* two identical triangles—whether right-angled, acute, or obtuse—flip one upside-down, and slide their matching slanted edges together: **two matching triangles always lock together into a rectangle or parallelogram** with the same Base and straight-up Height. Because the combined shape has area $\text{Base} \times \text{Height}$, each single triangle covers exactly half:
$$\text{Triangle Area} = (\text{Base} \times \text{Height}) \div 2$$
where the Height is always measured straight up (`90°`) from the Base to the top tip—like measuring your own height standing straight up against a wall, never leaning along a slanted edge!

Once you spot triangles hiding inside everyday gear, you can measure almost anything. A traditional diamond kite with a $20\text{-inch}$ horizontal crossbar and a $30\text{-inch}$ vertical spine is simply two wide triangles sharing the crossbar (or two tall triangles sharing the spine): keying `20 [ENTER] 30 [g] [TRI]` ($20 \times 30 \div 2$) reveals **$300\text{ in}^2$** of ripstop nylon. Similarly, a skateboard launch ramp is supported by two identical right-triangle plywood side panels, each with a base of $48\text{ in}$ and a vertical height of $18\text{ in}$: one side panel has area `48 [ENTER] 18 [g] [TRI]` $= 432\text{ in}^2$, and doubling for both sides (`2 [×]`) returns you to the full $48 \times 18 = \mathbf{864\text{ in}^2}$ sheet of plywood!

| Triangle Classification | Straight-Up Height Location | Area Rule |
| :--- | :--- | :--- |
| **Right Triangle** | Upright side serves directly as the straight-up Height | $\text{Triangle Area} = (\text{Base} \times \text{Height}) \div 2$ |
| **Obtuse Triangle** | Straight-up Height drops outside the base line | $\text{Triangle Area} = (\text{Base} \times \text{Height}) \div 2$ |
| **Acute Triangle** | Straight-up Height drops inside the triangle | $\text{Triangle Area} = (\text{Base} \times \text{Height}) \div 2$ |

Let's put `[g] [TRI]` to work on a model pond-yacht build. Suppose your scale model yacht features a triangular mainsail with a bottom boom (base) of $18\text{ cm}$ and a vertical mast height of $32\text{ cm}$, and you want to know how much sailcloth it takes to stitch the mainsail:

$$\text{Triangle Area} = (\text{Base} \times \text{Height}) \div 2 = (18 \times 32) \div 2 = 288\text{ cm}^2$$

If you build the full bounding rectangle on the stack first and slice it in half with `18 [ENTER] 32 [×] [2] [÷]`, the $576\text{ cm}^2$ rectangle divides cleanly into $\mathbf{288.00\text{ cm}^2}$. Or, using the dedicated `[g] [TRI]` shortcut, you simply stage the $18\text{ cm}$ boom on Register $Y$, enter the $32\text{ cm}$ mast height on Register $X$, and let `[g] [TRI]` multiply and halve them in a single stroke:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `18` | 0 | 0 | 0 | 18 |
| `[ENTER]` | 0 | 0 | 18 | 18 |
| `32` | 0 | 0 | 18 | 32 |
| `[g] [TRI]` | 0 | 0 | 0 | 288 |

What if you are carpeting an L-shaped backyard clubhouse floor that isn't a single rectangle or triangle? Here is a builder's favorite trick: draw one straight line to split the L-shape into **two friendly rectangles**! Suppose the main room measures $8\text{ feet}$ by $6\text{ feet}$ ($8 \times 6 = 48\text{ sq ft}$) and the attached reading nook measures $4\text{ feet}$ by $3\text{ feet}$ ($4 \times 3 = 12\text{ sq ft}$):
$$\text{Total Floor Area} = (\text{Main Room Length} \times \text{Width}) + (\text{Nook Length} \times \text{Width}) = (8 \times 6) + (4 \times 3) = 48 + 12 = 60\text{ sq ft}$$

On your SC-6 stack, you can multiply the main room's $8\text{-foot}$ and $6\text{-foot}$ edges first, let that $48\text{ sq ft}$ floor wait safely on the upper shelf while you multiply the $4 \times 3$ reading nook on the lower shelves, and then fuse both rooms together with `8 [ENTER] 6 [×] 4 [ENTER] 3 [×] [+]` to reach $\mathbf{60\text{ sq ft}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `8 [ENTER] 6 [×]` | 0 | 0 | 0 | 48 | Main room area: $8 \times 6 = 48\text{ sq ft}$ in Register $X$ |
| `4 [ENTER]` | 0 | 48 | 4 | 4 | Main room ($48$) lifts to $Z$; nook length ($4$) enters $Y$ and $X$ |
| `3 [×]` | 0 | 0 | 48 | 12 | Nook area: $4 \times 3 = 12\text{ sq ft}$ in $X$; $48$ drops to $Y$ |
| `[+]` | 0 | 0 | 0 | 60 | Add both rooms together: $48 + 12 = \mathbf{60\text{ sq ft}}$ |

---

### 6.3.3 Circles, Disks & Rings (`[f] [CIRC]`)
What happens when a shape has no straight sides at all? Pin one end of a piece of string to the center of your paper and sweep a pencil all the way around: every point on the **Circle** sits at the exact same distance (the **Radius**) from the center. The distance straight across through the center is the **Diameter** ($\text{Diameter} = 2 \times \text{Radius}$).

Over two thousand years ago, builders noticed something magical: no matter how tiny or gigantic a circle is—whether it is a shirt button or a Ferris wheel—if you wrap a string around its outside rim (the **Circumference**) and compare it to the **Diameter** straight across, the circumference is always just over $3.14$ times as long! Mathematicians call that universal circle ratio **$\pi$ (pi)**, approximately $3.1415926535\dots$, accessed on your SC-6 via the shifted key `[π]`.

Wait—why does that same number $\pi$ also find the flat **Area** inside a circle ($\text{Circle Area} = \text{Radius} \times \text{Radius} \times \pi$)? Picture slicing a round pizza into 16 thin triangular wedges. If you line up the slices alternating point-up, point-down, point-up, point-down like teeth on a zipper, the slices lock together into an almost-rectangular parallelogram! The straight-up height of that rectangle is one pizza slice long ($\text{Radius}$), and its bottom width is half of the crust ($\frac{1}{2} \times 2 \times \pi \times \text{Radius} = \pi \times \text{Radius}$). Multiply the width by the height, and out pops the circle area rule:
$$\text{Circumference} = 2 \times \pi \times \text{Radius} = \pi \times \text{Diameter}, \qquad \text{Circle Area} = \text{Radius} \times \text{Radius} \times \pi$$

| Circle Part | Meaning & Word Rule |
| :--- | :--- |
| **Radius** | Distance from the center point to the outer edge |
| **Diameter** | Full distance straight across through the center: $\text{Diameter} = 2 \times \text{Radius}$ |
| **Circumference** | Distance around one full lap of the circle: $\text{Circumference} = 2 \times \pi \times \text{Radius}$ |
| **Circle Area** | Total flat space inside the circle: $\text{Circle Area} = \text{Radius} \times \text{Radius} \times \pi$ (`[f] [CIRC]`) |

Using the SC-6's built-in hardware $\pi$ (`[π]`) and circle-area solver (`[f] [CIRC]`) gives you full decimal precision automatically, avoiding the rounding drift of rough $3.14$ paper estimates. For example, suppose the semicircular turnaround loop at the end of a school sprint track is laid out around a circle with a radius of $15\text{ meters}$. We can find both the grass seeding area enclosed by a full $15\text{-meter}$ radius circle and the running distance around one full circular lap—using `[f] [LASTX]` so we only type the radius once! First, tap `[f] [CIRC]` to find the enclosed grass area:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `15` | 0 | 0 | 0 | 15 |
| `[f] [CIRC]` | 0 | 0 | 0 | $706.8583$ |

Because `[f] [CIRC]` just consumed the radius `15`, that `15` is automatically waiting inside `LASTX`. Pull it right back onto the ground shelf and scale by $2\pi$ with `[f] [LASTX] [2] [×] [π] [×]` to reveal the **94.2478-meter** lap circumference while the grass area $706.8583\text{ m}^2$ rests right above it in Register $Y$.

Let's trace that full circumference step by step on a park landscaping build. In the botanical plaza of our community park sits a circular water fountain with a radius of $4.2\text{ meters}$ that needs a ring of granite stone curbing laid around its outer rim. Unroll the Cylindrical Wrapper Net on your desk: the width of the unrolled rectangular wall matches one complete turn around the circular disk, traveling $\pi$ times the diameter ($\text{Circumference} = 2 \times \text{Radius} \times \pi$). On the stack, doubling the $4.2\text{ m}$ radius into the $8.4\text{ m}$ diameter and scaling by $\pi$ with `4.2 [ENTER] [2] [×] [π] [×]` produces **`26.38937829`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4.2` | $0.0000$ | $0.0000$ | $0.0000$ | $4.2$ | Key fountain radius ($4.2\text{ m}$) |
| `[ENTER]` | $0.0000$ | $0.0000$ | $4.2$ | $4.2$ | Stack lifts; radius locked into Register $Y$ |
| `2` | $0.0000$ | $0.0000$ | $4.2$ | $2.0000$ | Key diameter doubling factor 2 |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $8.4$ | Multiply to obtain full diameter ($8.4\text{ m}$) in Register $X$ |
| `[π]` | $0.0000$ | $0.0000$ | $8.4$ | $3.1416$ | Push circle constant $\pi \approx 3.141593$ onto stack |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $26.3894$ | Multiply diameter by $\pi$ to wrap curb perimeter |

Wrapping the circular fountain rim takes $\mathbf{26.39\text{ meters}}$ of granite curbing—a smooth stone ring where park visitors can sit and dip their fingers in the cool water.

Once you can stamp out a solid circle, what happens when a circle has a hole punched out of the middle—like a glazed doughnut, a roll of tape, or a metal washer? Just imagine stamping out the big outer circle and subtracting the smaller inner circle that was punched out! Suppose a 3D-printed spacer washer has an outer radius of $12\text{ mm}$ and an inside hole with a radius of $5\text{ mm}$. Subtract the inside hole's radius squared from the outer circle's radius squared, then multiply by $\pi$:
$$\text{Ring Area} = (\text{Outer Radius}^2 - \text{Inner Radius}^2) \times \pi$$

Start by keying `12 [x²]` to enter the outer radius $12$ into Register $X$ and square it in place to $144$. Next, type `5 [x²]`, which automatically lifts $144$ up to Register $Y$ while squaring the inner hole radius $5$ to $25$ on Register $X$. Tapping `[-]` punches out the center hole ($144 - 25 = 119$), and finishing with `[π] [×]` scales that ring factor by $\pi$ to give $\mathbf{373.85\text{ mm}^2}$ of solid plastic.

---

### 6.3.4 Parallelograms & Trapezoids

Slanted four-sided figures like parallelograms and trapezoids look tricky at first glance, but they become effortless to measure once you snip and slide their angled corners back into familiar rectangles and triangles.

A **parallelogram** looks like a rectangle that has been nudged sideways so its left and right walls lean at the same angle. Why do we multiply its **Base** by the straight-up **Height** instead of the leaning side? Picture taking a pair of scissors, slicing a right triangle straight down (`90°`) from one slanted end of a parallelogram, and sliding that triangle across to the opposite end: the two pieces click together into a neat $\text{Base} \times \text{Height}$ rectangle (`[f] [RECT]`)! Because no paper was added or thrown away during the slide, its area rule is the exact same as a rectangle's:
$$\text{Parallelogram Area} = \text{Base} \times \text{Height} \quad \text{(Never multiply by the leaning side!)}$$

A **trapezoid**, meanwhile, has one pair of parallel bases—a shorter **Top Base** and a wider **Bottom Base**—separated by a straight-up **Height**. Think of a trapezoid as a rectangle whose top and bottom couldn't agree on how wide to be! You can solve any trapezoid (such as one with a $6\text{ cm}$ top base, a $10\text{ cm}$ bottom base, and a $4\text{ cm}$ height) in three fun ways:
1. **Splitting into a Central Rectangle and Side Triangles:** Slice straight down from the shorter top base ($6\text{ cm}$) to the bottom base ($10\text{ cm}$), creating a central $6 \times 4 = 24\text{ cm}^2$ rectangle plus two side triangles whose bases add up to $10 - 6 = 4\text{ cm}$ ($\text{Area} = (4 \times 4) \div 2 = 8\text{ cm}^2$), totaling $24 + 8 = \mathbf{32\text{ cm}^2}$.
2. **Enclosing Box Minus Cutouts:** Surround the trapezoid with a full $10 \times 4 = 40\text{ cm}^2$ bounding rectangle (`10 [ENTER] 4 [f] [RECT]`), then subtract the two empty corner triangles ($40 - 8 = \mathbf{32\text{ cm}^2}$).
3. **Averaging the Two Parallel Bases Times Height (The Middle-Width Shortcut):** What is halfway between a $6\text{ cm}$ top and a $10\text{ cm}$ bottom? Add the Top Base and Bottom Base and divide by $2$ to find the **average middle width** ($(6 + 10) \div 2 = 8\text{ cm}$), then multiply by the straight-up Height:
$$\text{Trapezoid Area} = (\text{Top Base} + \text{Bottom Base}) \div 2 \times \text{Height}$$

| Trapezoid Dimension | Measurement | Role in Area Rule |
| :--- | :--- | :--- |
| **Top Base** | $6\text{ cm}$ | Averaged with Bottom Base: $(\text{Top Base} + \text{Bottom Base}) \div 2$ |
| **Bottom Base** | $10\text{ cm}$ | Average width $= (6 + 10) \div 2 = 8\text{ cm}$ |
| **Straight-Up Height** | $4\text{ cm}$ | $\text{Trapezoid Area} = 8 \times 4 = \mathbf{32\text{ cm}^2}$ |

That middle-width shortcut is a favorite tool of civil engineers, who dig storm-water drainage canals in the shape of a trapezoid—narrow at the bottom and wide at the top—so the dirt banks don't cave in during heavy rain. Suppose a runoff culvert has a bottom width of $60\text{ cm}$, a top opening width of $110\text{ cm}$, and a straight-up depth of $40\text{ cm}$. You can average the top and bottom widths right on the stack without touching a parenthesis key: first enter `60`, press `[ENTER]` to lift `60` onto Shelf $Y$, and type `110 [+]` so the combined parallel widths ($170\text{ cm}$) appear on Ground Shelf $X$. Next, type `2 [÷]` to slice that sum in half and reveal the exact average middle width of $85\text{ cm}$ ($Y = 0,\; X = 85$). Finally, type the $40\text{ cm}$ vertical depth and tap `[×]` to multiply the $85\text{ cm}$ middle width by $40\text{ cm}$, landing on a water flow area of $\mathbf{3,400\text{ cm}^2}$ ($0.34\text{ m}^2$).

Landscape architects use that exact same middle-width rhythm whenever a sloped grass embankment rises beside a wheelchair and bicycle access ramp: because the ramp starts flush with the ground on one end and rises to meet an elevated terrace on the other, the side embankment has two parallel edges of different lengths. Suppose the park's ramp embankment is shaped like a trapezoid with a top width of $14\text{ m}$, a wider bottom width of $22\text{ m}$, and a straight-up height of $6\text{ m}$. How much grass sod is needed to carpet the slope? Remember our middle-width shortcut: joining two identical trapezoids with one flipped upside down forms a parallelogram whose base is $\text{Top Width} + \text{Bottom Width}$; halving that combined base gives the average middle width ($18\text{ m}$). Combining both parallel widths on Registers $Y$ and $X$, halving them, and multiplying by the $6\text{ m}$ vertical height with `14 [ENTER] 22 [+] [2] [÷] [6] [×]` yields **`108`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `14` | $0.0000$ | $0.0000$ | $0.0000$ | $14.0000$ | Key top crest base ($14\text{ m}$) |
| `[ENTER]` | $0.0000$ | $0.0000$ | $14.0000$ | $14.0000$ | Stack lifts; top base locked into Register $Y$ |
| `22` | $0.0000$ | $0.0000$ | $14.0000$ | $22.0000$ | Key ground base ($22\text{ m}$) into floor $X$ |
| `[+]` | $0.0000$ | $0.0000$ | $0.0000$ | $36.0000$ | Sum parallel bases ($14 + 22 = 36\text{ m}$) |
| `2` | $0.0000$ | $0.0000$ | $36.0000$ | $2.0000$ | Key divisor 2 on floor $X$ |
| `[÷]` | $0.0000$ | $0.0000$ | $0.0000$ | $18.0000$ | Divide sum by 2 to compute average midline width ($18\text{ m}$) |
| `6` | $0.0000$ | $0.0000$ | $18.0000$ | $6.0000$ | Key embankment vertical height ($6\text{ m}$) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $108.0000$ | Multiply average width by height for total area |

Carpeting the bicycle ramp embankment takes $\mathbf{108.00\text{ m}^2}$ of grass sod.

---

### 6.3.5 Regular Polygons: Honeycomb Hexagons & Floor Tiles
Why do honeybees build their wax honeycombs out of 6-sided **regular hexagons** instead of circles or squares? If you pack circles together (like pennies on a table), curved gaps are wasted between them; and among all polygons that tile a flat wall with zero gaps, a regular hexagon encloses the most honey using the least wax! Even better, if you draw straight lines from the center of a regular hexagon to all 6 corners, the hexagon splits into **6 matching equilateral triangles**—just like a round pizza cut into 6 equal slices:
$$\text{Hexagon Area} = \text{Side}^2 \times 3 \times \sqrt{3} \div 2$$

Suppose your school courtyard is being paved with regular 6-sided hexagonal stone pavers, each having a side length of $10\text{ cm}$. Because the 6 equilateral triangles lock together around the center, we can find the surface area of one hexagonal paver on the stack using `[x²]` and `[f] [√x]` without writing down or rounding any intermediate decimals. First, key `10 [x²]` to enter the $10\text{ cm}$ side length into Register $X$ and square it in place to $100$, then tap `[3] [×]` to scale up to $300$. Next, key `3 [f] [√x]`—which lifts $300$ onto Register $Y$ while extracting $\sqrt{3} \approx 1.73205$ in Register $X$—and tap `[×]` to merge them into $519.6152$ before halving with `[2] [÷]` to land on $\mathbf{259.81\text{ cm}^2}$.

To see every register shift in detail, suppose carpenters at our park's hilltop overlook are building a 6-sided honeycomb-shaped picnic gazebo. On our $1{:}10$ scale tabletop blueprint, each side of the regular hexagon measures $12\text{ cm}$. Following the word rule $\text{Hexagon Area} = \text{Side}^2 \times 3 \times \sqrt{3} \div 2$ on the stack by squaring $12$ and scaling by $3\sqrt{3} \div 2$ with `12 [x²] [3] [×] [3] [f] [√x] [×] [2] [÷]` obtains **`374.12297443`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `12` | $0.0000$ | $0.0000$ | $0.0000$ | $12.0000$ | Key hexagon side length ($12\text{ cm}$) |
| `[x²]` | $0.0000$ | $0.0000$ | $0.0000$ | $144.0000$ | Square side length ($12^2 = 144$) |
| `3` | $0.0000$ | $0.0000$ | $144.0000$ | $3.0000$ | Key multiplier 3 for the 6 matching triangles |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $432.0000$ | Multiply ($144 \times 3 = 432$) |
| `3` | $0.0000$ | $0.0000$ | $432.0000$ | $3.0000$ | Key number 3 on floor $X$ |
| `[f] [√x]` | $0.0000$ | $0.0000$ | $432.0000$ | $1.7321$ | Extract square root in place ($\sqrt{3} \approx 1.732051$) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $748.2459$ | Multiply by $\sqrt{3}$ ($432 \times 1.732051 = 748.2459$) |
| `2` | $0.0000$ | $0.0000$ | $748.2459$ | $2.0000$ | Key divisor 2 |
| `[÷]` | $0.0000$ | $0.0000$ | $0.0000$ | $374.1230$ | Divide by 2 to finalize the hexagon floor area |

The scale blueprint of the hexagonal gazebo floor covers $\mathbf{374.12\text{ cm}^2}$, giving the park carpenters the exact tabletop template they need before cutting the full-size cedar decking planks.

---

## 6.4 The Master Surface Area Technique via Stats Mode (`[Σ+]`)

Now that you can find the area of any flat 2D shape on your tabletop, let's fold those flat panels up into three-dimensional boxes, tents, and tanks!

### 6.4.1 The "Shopping Basket for Walls": Why `[Σ+]` Makes Wrapping 3D Boxes Effortless
Imagine you are wrapping a rectangular birthday present or building a cardboard treasure chest, and you want to know the total **Surface Area** of all 6 outer walls:
$$\text{Total Box Surface Area} = 2 \times (\text{Length} \times \text{Width}) + 2 \times (\text{Length} \times \text{Height}) + 2 \times (\text{Width} \times \text{Height})$$

If you try to type all 6 walls as one giant line on an ordinary calculator—`2*(5*4) + 2*(5*3) + 2*(4*3)`—you run into three big headaches:
1. **Parenthesis Overload:** You have to juggle six brackets in a row. Forget a single parenthesis or hit `+` instead of `*` near the end, and the whole line is ruined!
2. **Scrap-Paper Scribbles:** Many students give up on brackets and write each wall's area on scrap paper ("40", "30", "24"), then type them all back in. Copying numbers back and forth invites silly copying mistakes.
3. **Working Blind:** On a regular calculator, you can't see whether each wall pair makes sense before it gets swallowed into a giant formula.

On your SC-6, there is a much smarter way: **think of the `[Σ+]` key as a shopping basket for walls!**
- First, you tap `[g] [CLΣ]` to start with an empty basket.
- Next, you measure the **Top and Bottom walls** ($2 \times 5 \times 4 = 40$) and tap `[Σ+]` to toss them into your basket. The screen says **`n = 1`**, confirming 1 wall pair is safely inside!
- Then you measure the **Front and Back walls** ($2 \times 5 \times 3 = 30$) and tap `[Σ+]` to toss them into the basket. Now the screen says **`n = 2`**!
- Finally, you measure the **Left and Right walls** ($2 \times 4 \times 3 = 24$) and tap `[Σ+]` (`n = 3`).
- When every wall is in the basket, you walk up to the checkout counter and tap **`[f] [Σx]`**—and out pops the grand total surface area (**`94`**)!

> **The Master Surface Area Technique (`[Σ+]`)**
> - **Rule 1 (Empty the Basket):** Always reset statistical memory before starting: `[g] [CLΣ]`.
> - **Rule 2 (Toss Each Wall Pair In):** Compute each face (or opposing face pair) and press `[Σ+]` immediately.
> - **Rule 3 (Check Your Wall Count):** The screen displays `n = 1, 2, 3...`, counting how many face groups are in your basket.
> - **Rule 4 (Ring Up the Total):** Press `[f] [Σx]` to reveal the grand total surface area.
>
> *Zero scratch paper • Zero parentheses • 100% hardware stack verified.*

### 6.4.2 3D Block Prisms & The Master Surface Area Technique (`[Σ+]`)

Let's walk through that $5\text{ cm}$ long by $4\text{ cm}$ wide by $3\text{ cm}$ tall instrument case step by step in narrative slow-motion so you can picture the shopping basket (`Stat n, Σx`) filling up on your screen before we head to Antarctica for our full 23-step register trace!
1. **Empty the Basket (`[g] [CLΣ]`):** Press `[g] [CLΣ]` first so your statistical memory resets cleanly to `n = 0, Σx = 0` and all four stack registers ($T, Z, Y, X$) start at `0`.
2. **Pair 1 — Top & Bottom Walls ($2 \times 5 \times 4 = 40\text{ cm}^2$):** Key `[5] [ENTER] [4] [×]` to multiply the $5\text{ cm}$ length by the $4\text{ cm}$ width into a single $20\text{ cm}^2$ face on Ground Shelf $X$, then tap `[2] [×]` to double it for both the top and bottom walls ($X = 40$). Now press `[Σ+]`: the calculator tosses `40` into your statistical basket and displays `1` on Ground Shelf $X$ (`n = 1, Σx = 40`), confirming that your first wall pair is safely stored!
3. **Pair 2 — Front & Back Walls ($2 \times 5 \times 3 = 30\text{ cm}^2$):** Key `[5] [ENTER] [3] [×]` to build one $15\text{ cm}^2$ front wall, double it with `[2] [×]` to cover both front and back ($X = 30$), and tap `[Σ+]`. Ground Shelf $X$ increments to `2` (`n = 2, Σx = 70`), showing that two wall pairs are now in the basket!
4. **Pair 3 — Left & Right End Walls ($2 \times 4 \times 3 = 24\text{ cm}^2$) & Checkout (`[f] [Σx]`):** Key `[4] [ENTER] [3] [×]` for one $12\text{ cm}^2$ side end, double it with `[2] [×]` ($X = 24$), and tap `[Σ+]` (`n = 3, Σx = 94`). With all three wall pairs in the basket, tap `[f] [Σx]` at the checkout counter: out pops the grand total surface area of **`94`** ($40 + 30 + 24 = \mathbf{94\text{ cm}^2}$) while keeping your 4-register stack completely uncluttered!

Now let's take this `[Σ+]` wall-basket method south to McMurdo Station, Antarctica, where the Emperor penguins from the start of our chapter huddle against $-40^\circ\text{C}$ gales—and watch every single register across the full 23-row table! As the station's cold-weather engineering officer, you know that precious warmth escapes through every square centimeter of exposed **surface area**. Your first polar mission is wrapping a rectangular weather-sensor pod measuring $6\text{ cm} \times 4\text{ cm} \times 2\text{ cm}$ in aluminized mylar so its battery doesn't freeze in the $-40^\circ\text{C}$ wind. Unfold the Rectangular Prism Net on your desk: the 6 rectangular walls pair up into top/bottom ($6 \times 4$), front/back ($6 \times 2$), and left/right ($4 \times 2$). Tossing all three opposing wall pairs into your `[Σ+]` basket and ringing up the total with `[f] [Σx]` via `[g] [CLΣ] [6] [ENTER] [4] [×] [2] [×] [Σ+] [6] [ENTER] [2] [×] [2] [×] [Σ+] [4] [ENTER] [2] [×] [2] [×] [Σ+] [f] [Σx]` reveals **`88`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `[g] [CLΣ]` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Clear statistical memory accumulators ($n = 0, \Sigma x = 0$) |
| `6` | $0.0000$ | $0.0000$ | $0.0000$ | $6.0000$ | Key in pod length ($6\text{ cm}$) |
| `[ENTER]` | $0.0000$ | $0.0000$ | $6.0000$ | $6.0000$ | Stack lifts; length locked into Register $Y$ |
| `4` | $0.0000$ | $0.0000$ | $6.0000$ | $4.0000$ | Key in pod width ($4\text{ cm}$) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $24.0000$ | Multiply length by width for single top face ($24\text{ cm}^2$) |
| `2` | $0.0000$ | $0.0000$ | $24.0000$ | $2.0000$ | Key in face-pair factor 2 |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $48.0000$ | Double for top and bottom face pair ($48\text{ cm}^2$) |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Accumulate pair 1 into $\Sigma x$ ($n = 1, \Sigma x = 48$) |
| `6` | $0.0000$ | $0.0000$ | $0.0000$ | $6.0000$ | Key in pod length ($6\text{ cm}$) |
| `[ENTER]` | $0.0000$ | $0.0000$ | $6.0000$ | $6.0000$ | Stack lifts; length locked into Register $Y$ |
| `2` | $0.0000$ | $0.0000$ | $6.0000$ | $2.0000$ | Key in pod height ($2\text{ cm}$) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $12.0000$ | Multiply length by height for single front face ($12\text{ cm}^2$) |
| `2` | $0.0000$ | $0.0000$ | $12.0000$ | $2.0000$ | Key in face-pair factor 2 |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $24.0000$ | Double for front and back face pair ($24\text{ cm}^2$) |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Accumulate pair 2 into $\Sigma x$ ($n = 2, \Sigma x = 72$) |
| `4` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | Key in pod width ($4\text{ cm}$) |
| `[ENTER]` | $0.0000$ | $0.0000$ | $4.0000$ | $4.0000$ | Stack lifts; width locked into Register $Y$ |
| `2` | $0.0000$ | $0.0000$ | $4.0000$ | $2.0000$ | Key in pod height ($2\text{ cm}$) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $8.0000$ | Multiply width by height for single side face ($8\text{ cm}^2$) |
| `2` | $0.0000$ | $0.0000$ | $8.0000$ | $2.0000$ | Key in face-pair factor 2 |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $16.0000$ | Double for left and right end pair ($16\text{ cm}^2$) |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $3.0000$ | Accumulate pair 3 into $\Sigma x$ ($n = 3, \Sigma x = 88$) |
| `[f] [Σx]` | $0.0000$ | $0.0000$ | $0.0000$ | $88.0000$ | Recall total accumulated surface area across all 6 faces |

The sensor pod requires $\mathbf{88.00\text{ cm}^2}$ of thermal foil.

---

### 6.4.3 The Cube Manipulative
What if all three dimensions of a box—Length, Width, and Height—are equal? Then you have a **cube**, like a 6-sided game die (`d6`) where all 6 walls are identical squares! For a solid cube manipulative with a side length of $4\text{ cm}$:
$$\text{Area of 1 face} = 4\text{ cm} \times 4\text{ cm} = 16\text{ cm}^2$$
$$\text{Total Surface Area} = 6 \times 16\text{ cm}^2 = 96\text{ cm}^2$$

If you want to physically confirm the 6-face count in your shopping basket, you can start with `[g] [CLΣ]`, repeat `[4] [ENTER] [4] [×] [Σ+]` six times until the display shows `n = 6`, and tap `[f] [Σx]` to reach $\mathbf{96.00\text{ cm}^2}$. Or, since all 6 square faces are identical twins, you can square one side and multiply by 6 in three quick taps via `4 [x²] 6 [×]` to land directly on $\mathbf{96.00\text{ cm}^2}$.

---

### 6.4.4 Triangular Prism

Now picture a camping tent, a wheelchair ramp, or a triangular prism manipulative with **5 flat faces**: two triangular end caps (front and back) connected by three rectangular panels (a flat floor, a vertical back wall, and a slanted roof). Suppose our prism has two right-triangular end bases with straight-angle legs of $3\text{ cm}$ and $4\text{ cm}$ (and a slanted roof edge of $5\text{ cm}$), stretched along a prism length of $6\text{ cm}$:

| Triangular Prism Face | Geometry & Dimensions | Area Calculation |
| :--- | :--- | :--- |
| **2 Triangular Ends** | Right triangle legs of $3\text{ cm}$ and $4\text{ cm}$ | $2 \times (\frac{1}{2} \times 3 \times 4) = 12\text{ cm}^2$ |
| **1 Bottom Rectangular Base** | Base $3\text{ cm}$, prism length $6\text{ cm}$ | $1 \times (3 \times 6) = 18\text{ cm}^2$ |
| **1 Vertical Rectangular Back** | Height $4\text{ cm}$, prism length $6\text{ cm}$ | $1 \times (4 \times 6) = 24\text{ cm}^2$ |
| **1 Slanted Rectangular Roof** | Slanted edge $5\text{ cm}$, prism length $6\text{ cm}$ | $1 \times (5 \times 6) = 30\text{ cm}^2$ |
| **Total Surface Area** | Accumulated via `[Σ+]` ($n = 4$) | **$84\text{ cm}^2$** |

Let's take a step-by-step inventory of those four face groups before tossing them into our `[Σ+]` basket:
1. **Two Triangular Ends:** Remember how two matching triangles always lock together into a rectangle? Since each end is $\frac{1}{2} \times 3 \times 4 = 6\text{ cm}^2$, the two ends together equal $3 \times 4 = 12\text{ cm}^2$!
2. **Bottom Rectangular Face:** $3\text{ cm} \times 6\text{ cm} = 18\text{ cm}^2$.
3. **Vertical Rectangular Back:** $4\text{ cm} \times 6\text{ cm} = 24\text{ cm}^2$.
4. **Slanted Rectangular Roof:** $5\text{ cm} \times 6\text{ cm} = 30\text{ cm}^2$.
$$\text{Total Surface Area} = 12 + 18 + 24 + 30 = 84\text{ cm}^2$$

Watch how `[f] [LASTX]` lets you reuse the $6\text{ cm}$ prism length across all three rectangular panels without typing `6` three times: start with `[g] [CLΣ]`, then accumulate the $12\text{ cm}^2$ triangular ends with `[3] [ENTER] [4] [×] [Σ+]` ($n = 1$) and the $18\text{ cm}^2$ bottom panel with `[3] [ENTER] [6] [×] [Σ+]` ($n = 2$). Because `6` is now tucked inside `LASTX`, you can accumulate the $24\text{ cm}^2$ back wall with `[4] [f] [LASTX] [×] [Σ+]` ($n = 3$) and the $30\text{ cm}^2$ slanted roof with `[5] [f] [LASTX] [×] [Σ+]` ($n = 4$), then tap `[f] [Σx]` to reveal $\mathbf{84.00\text{ cm}^2}$.

What if all three sides of the triangular ends are equal—an **equilateral triangular prism**? Back at McMurdo Station, the Antarctic glaciology team brings in a long triangular prism case used to carry ancient ice cores without rolling off their sleds. Its equilateral triangular ends have a base of $4\text{ cm}$ and a height of $3.464\text{ cm}$, and the carrier is $20\text{ cm}$ long. Unfold the Triangular Prism Net from your kit: the two triangular ends lock together into one $\text{Base} \times \text{Height}$ rectangle ($4 \times 3.464$), while the three matching rectangular side walls form $3 \times (4 \times 20)$. Depositing both face groups into `[Σ+]` with `[g] [CLΣ] [4] [ENTER] 3.464 [×] [Σ+] [4] [ENTER] 20 [×] [3] [×] [Σ+] [f] [Σx]` brings the total to **`253.856`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `[g] [CLΣ]` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Reset statistical accumulator ($n = 0, \Sigma x = 0$) |
| `4` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | Key in triangular end base ($4\text{ cm}$) |
| `[ENTER]` | $0.0000$ | $0.0000$ | $4.0000$ | $4.0000$ | Stack lifts; base locked into Register $Y$ |
| `3.464` | $0.0000$ | $0.0000$ | $4.0000$ | $3.464$ | Key in triangle height ($3.464\text{ cm}$) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $13.856$ | Multiply: two triangular ends combine into $4 \times 3.464 = 13.856\text{ cm}^2$ |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Deposit both end caps into accumulator ($n = 1, \Sigma x = 13.856$) |
| `4` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | Key in prism side width ($4\text{ cm}$) |
| `[ENTER]` | $0.0000$ | $0.0000$ | $4.0000$ | $4.0000$ | Stack lifts; width locked into Register $Y$ |
| `20` | $0.0000$ | $0.0000$ | $4.0000$ | $20.0000$ | Key in container length ($20\text{ cm}$) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $80.0000$ | Multiply for single rectangular wall area ($80\text{ cm}^2$) |
| `3` | $0.0000$ | $0.0000$ | $80.0000$ | $3.0000$ | Key in 3 congruent wrapping side walls |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $240.0000$ | Multiply to obtain total lateral area ($240\text{ cm}^2$) |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Deposit lateral walls into accumulator ($n = 2, \Sigma x = 253.856$) |
| `[f] [Σx]` | $0.0000$ | $0.0000$ | $0.0000$ | $253.856$ | Recall total accumulated prism surface area |

Wrapping the ice-core carrier takes $\mathbf{253.86\text{ cm}^2}$ of insulation.

---

### 6.4.5 Right Circular Cylinder
How do you measure the curved wall of a round **cylinder**, like a soup can or a water tank? Imagine peeling the paper label off a soup can and laying it flat on your desk! The top and bottom lids are two matching circular disks (`[f] [CIRC]`), and the unrolled paper label is simply a **flat rectangle** whose width wrapped all the way around the circle's rim ($\text{Circumference} = 2 \times \pi \times \text{Radius}$) and whose height is the cylinder's Height:
$$\text{Cylinder Surface Area} = (2 \times \text{Circle Area}) + (\text{Circumference} \times \text{Height})$$

To see this unrolled label in action on a real engineering structure, first picture a cylindrical steel farm water tank with a radius of $3\text{ meters}$ and a height of $8\text{ meters}$: after clearing the statistical registers with `[g] [CLΣ]`, you stamp out and double the $3\text{-meter}$ circular end disks using `[3] [f] [CIRC] [2] [×] [Σ+]` ($2 \times \pi \times 3^2 \approx 56.5487\text{ m}^2$, $n = 1$), unroll the tank's rim circumference and stretch it up the $8\text{-meter}$ wall with `[3] [ENTER] [2] [×] [π] [×] [8] [×] [Σ+]` ($18.8496 \times 8 \approx 150.7964\text{ m}^2$, $n = 2$), and tap `[f] [Σx]` to ring up $\mathbf{207.35\text{ m}^2}$ of steel sheeting. Now let's trace that exact two-part `[Σ+]` rhythm across all four stack registers at McMurdo Station as the Antarctic drill team melts a sample of sub-glacial lake water into a cylindrical titanium flask with a radius of $3.3\text{ cm}$ and a height of $12.2\text{ cm}$! Unroll the Cylindrical Wrapper Net from your kit: the top and bottom form circular disks (`[f] [CIRC]`), while the curved wall unrolls into a rectangle of width $2 \times \text{Radius} \times \pi$ and height $12.2\text{ cm}$. Accumulating the twin circular end caps ($n = 1$) and the unrolled lateral jacket ($n = 2$) in your `[Σ+]` basket with `[g] [CLΣ] 3.3 [f] [CIRC] [2] [×] [Σ+] 3.3 [ENTER] [2] [×] [π] [×] 12.2 [×] [Σ+] [f] [Σx]` gives **`321.38492846`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `[g] [CLΣ]` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Reset statistical memory bin ($n = 0, \Sigma x = 0$) |
| `3.3` | $0.0000$ | $0.0000$ | $0.0000$ | $3.3$ | Key in flask radius ($3.3\text{ cm}$) |
| `[f] [CIRC]` | $0.0000$ | $0.0000$ | $0.0000$ | $34.2119$ | Dedicated circle solver evaluates single disc area ($\pi \times \text{Radius}^2$) |
| `2` | $0.0000$ | $0.0000$ | $34.2119$ | $2.0000$ | Key in multiplier 2 for circular ends |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $68.4239$ | Double for top and bottom lids ($68.4239\text{ cm}^2$) |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Deposit both end discs into accumulator ($n = 1, \Sigma x = 68.4239$) |
| `3.3` | $0.0000$ | $0.0000$ | $0.0000$ | $3.3$ | Key in radius ($3.3\text{ cm}$) |
| `[ENTER]` | $0.0000$ | $0.0000$ | $3.3$ | $3.3$ | Stack lifts; radius locked into Register $Y$ |
| `2` | $0.0000$ | $0.0000$ | $3.3$ | $2.0000$ | Key doubling factor 2 for diameter |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $6.6$ | Multiply to obtain diameter ($6.6\text{ cm}$) |
| `[π]` | $0.0000$ | $0.0000$ | $6.6$ | $3.1416$ | Push circle constant $\pi \approx 3.141593$ |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $20.7345$ | Multiply diameter by $\pi$ for circumference ($20.7345\text{ cm}$) |
| `12.2` | $0.0000$ | $0.0000$ | $20.7345$ | $12.2$ | Key in cylinder height ($12.2\text{ cm}$) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $252.9610$ | Multiply circumference by height for lateral wall ($252.961\text{ cm}^2$) |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Deposit lateral jacket into accumulator ($n = 2, \Sigma x = 321.385$) |
| `[f] [Σx]` | $0.0000$ | $0.0000$ | $0.0000$ | $321.3849$ | Recall total accumulated cylindrical surface area |

The cylindrical titanium flask has a total outer surface area of $\mathbf{321.38\text{ cm}^2}$.

---

### 6.4.6 Right Circular Cone
A right **cone**—like an ice-cream sugar cone or an orange traffic pylon—has a flat circular floor and a sloped side wall that tapers up to a single point at the top. The distance from the top tip straight down the outside slope is called the **Slant Height** ($\text{Slant Height} = \sqrt{\text{Radius}^2 + \text{Height}^2}$):
$$\text{Circle Base Area} = \text{Radius} \times \text{Radius} \times \pi, \qquad \text{Cone Side Area} = \pi \times \text{Radius} \times \text{Slant Height}$$
$$\text{Total Cone Surface Area} = \text{Circle Base Area} + (\pi \times \text{Radius} \times \text{Slant Height})$$

Suppose a road-safety workshop is wrapping reflective orange vinyl around a highway safety cone that has a base radius of $15\text{ cm}$ and a vertical height of $36\text{ cm}$. Because a traffic pylon sits over a rubber base ring with an open bottom, we only need to wrap its sloped side wall! (*Note for Grades 3–5: Students may use the given slant height of $39\text{ cm}$ directly; Grade 6 explorers can compute the slant height $\sqrt{15^2 + 36^2} = 39\text{ cm}$ using `[f] [√x]`.*)

First, square both the $15\text{ cm}$ radius and $36\text{ cm}$ height on the stack, add them together, and take the square root with `15 [x²] 36 [x²] [+] [f] [√x]` to uncover the exact slant height of $\mathbf{39.00\text{ cm}}$ in Register $X$. With $39$ waiting right on the ground shelf, multiply by $\pi$ and the $15\text{ cm}$ base radius using `[π] [×] 15 [×]` ($\pi \times \text{Radius} \times \text{Slant Height}$) to find that the cone requires $\mathbf{1,837.83\text{ cm}^2}$ of reflective vinyl sheeting.

---

### 6.4.7 Regular Square-Based Pyramid
If you unfold a **square pyramid** flat on your desk, it looks like a 4-pointed star: one **square floor** in the middle surrounded by **four matching triangular walls** that fold up to meet at the top peak! The **Slant Height** runs from the top peak straight down the middle of each triangular wall:
$$\text{Square Floor Area} = \text{Side} \times \text{Side}, \qquad \text{Four Triangle Walls Area} = 4 \times (\text{Side} \times \text{Slant Height} \div 2)$$
$$\text{Total Pyramid Surface Area} = \text{Square Floor Area} + \text{Four Triangle Walls Area}$$

For a full-size expedition tent with a $3\text{-meter}$ square floor and $2.5\text{-meter}$ wall slant height, tossing the squared floor (`[g] [CLΣ] [3] [x²] [Σ+]` $\to 9.00\text{ m}^2$, $n = 1$) and the four triangular walls (`[3] [ENTER] 2.5 [×] [2] [÷] [4] [×] [Σ+]` $\to 15.00\text{ m}^2$, $n = 2$) into your `[Σ+]` basket and tapping `[f] [Σx]` rings up $\mathbf{24.00\text{ m}^2}$ of waterproof canvas. Even better, notice a neat shortcut when adding all four triangular walls at once: because $4 \times \frac{1}{2} = 2$, the four triangular walls together always equal $2 \times \text{Base} \times \text{Slant Height}$! Let's use that shortcut as the Antarctic scientists test a $1{:}10$ scale wind-tunnel model of their polar survival pyramid tent whose square floor has a side of $20\text{ cm}$ and whose four triangular walls each have a slant height of $16\text{ cm}$. Tossing the square floor ($n = 1$) and the four triangular canopy walls ($n = 2$) into `[Σ+]` with `[g] [CLΣ] 20 [x²] [Σ+] 20 [ENTER] 16 [×] [2] [×] [Σ+] [f] [Σx]` yields **`1040`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `[g] [CLΣ]` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Clear statistical accumulator ($n = 0, \Sigma x = 0$) |
| `20` | $0.0000$ | $0.0000$ | $0.0000$ | $20.0000$ | Key in square floor base side ($20\text{ cm}$) |
| `[x²]` | $0.0000$ | $0.0000$ | $0.0000$ | $400.0000$ | Square side length ($20^2 = 400\text{ cm}^2$) for floor area |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Deposit floor square into accumulator ($n = 1, \Sigma x = 400$) |
| `20` | $0.0000$ | $0.0000$ | $0.0000$ | $20.0000$ | Key in tent base edge ($20\text{ cm}$) |
| `[ENTER]` | $0.0000$ | $0.0000$ | $20.0000$ | $20.0000$ | Stack lifts; edge locked into Register $Y$ |
| `16` | $0.0000$ | $0.0000$ | $20.0000$ | $16.0000$ | Key in wall slant height ($16\text{ cm}$) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $320.0000$ | Multiply base by slant height ($20 \times 16 = 320$) |
| `2` | $0.0000$ | $0.0000$ | $320.0000$ | $2.0000$ | Scale by 2 ($4 \times \frac{1}{2} = 2$) for all 4 triangular faces |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $640.0000$ | Multiply to evaluate total canopy wall area ($640\text{ cm}^2$) |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Deposit 4 canopy walls into accumulator ($n = 2, \Sigma x = 1040$) |
| `[f] [Σx]` | $0.0000$ | $0.0000$ | $0.0000$ | $1040.0000$ | Recall total tent model surface area |

The scale pyramid tent model has a total surface area of $\mathbf{1040.00\text{ cm}^2}$—a streamlined four-sided shelter whose sloped triangular walls shed fierce Antarctic blizzard gusts without buckling.

---

### 6.4.8 Open-Top Solids & Custom Maker Enclosures
Why is the `[Σ+]` wall-basket method so much safer than a rigid textbook formula? Because real-world objects often leave one side open, or combine two different shapes into a custom structure! If you build a glass fish tank, a domed silo sitting on the ground, or an open concrete drainage canal, you only want to count the walls that actually get painted or lined.

Suppose you are building an open-top aquarium measuring $10\text{ inches}$ long, $8\text{ inches}$ wide, and $6\text{ inches}$ high. Because fish need an open top for air and feeding, this box has only **5 glass panels** (1 bottom floor + 2 left/right walls + 2 front/back walls). Notice how after computing the bottom floor ($10 \times 8$), the width `8` stays inside `LASTX`—so you can recall it with `[f] [LASTX]` for the side walls without typing `8` again!

Start with `[g] [CLΣ]` and toss the single $80.00\text{ in}^2$ bottom glass sheet into the basket using `10 [ENTER] [8] [×] [Σ+]` ($n = 1$, with $8$ saved in `LASTX`). Pull `8` back from `LASTX` to build both left and right end walls ($8 \times 6 \times 2 = 96.00\text{ in}^2$) with `[f] [LASTX] [6] [×] [2] [×] [Σ+]` ($n = 2$), then add the front and back glass panels ($10 \times 6 \times 2 = 120.00\text{ in}^2$) with `10 [ENTER] [6] [×] [2] [×] [Σ+]` ($n = 3$). A single press of `[f] [Σx]` confirms that all `n = 3` panel groups require $\mathbf{296.00\text{ in}^2}$ of acrylic glass.

Now let's try two real-world engineering structures at a regional airport where one side sits open or rests on the ground. First, inspect the airport's gleaming aviation fuel silo: a cylindrical tank body (radius $4\text{ m}$, height $10\text{ m}$) topped by a hemispherical half-dome roof (radius $4\text{ m}$). Because the flat bottom sits on a concrete pad, painters only coat the curved cylinder wall plus the half-dome roof! Unroll the Cylindrical Wrapper Net into a rectangle of $\text{Circumference} \times \text{Height}$ ($25.13\text{ m} \times 10\text{ m}$), and pair it with the hemispherical half-dome surface ($2 \times \pi \times \text{Radius}^2$, which Archimedes proved equals the area of two flat circular disks!). Accumulating the cylinder wall ($n = 1$) and dome surface ($n = 2$) in `[Σ+]` with `[g] [CLΣ] [4] [ENTER] [2] [×] [π] [×] 10 [×] [Σ+] [4] [f] [CIRC] [2] [×] [Σ+] [f] [Σx]` gives **`351.8583772`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `[g] [CLΣ]` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Clear statistical accumulator registers ($n = 0, \Sigma x = 0$) |
| `4` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | Key in cylinder radius ($4\text{ m}$) |
| `[ENTER]` | $0.0000$ | $0.0000$ | $4.0000$ | $4.0000$ | Stack lifts; radius locked into Register $Y$ |
| `2` | $0.0000$ | $0.0000$ | $4.0000$ | $2.0000$ | Key in factor 2 |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $8.0000$ | Multiply to find cylinder diameter ($2 \times 4 = 8\text{ m}$) |
| `[π]` | $0.0000$ | $0.0000$ | $8.0000$ | $3.1416$ | Push circle constant $\pi$; diameter lifts to Register $Y$ |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $25.1327$ | Multiply to compute cylinder perimeter ($8 \times \pi \approx 25.1327\text{ m}$) |
| `10` | $0.0000$ | $0.0000$ | $25.1327$ | $10.0000$ | Key in cylinder height ($10\text{ m}$); perimeter lifts to Register $Y$ |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $251.3274$ | Multiply perimeter by height to compute cylinder wall area ($251.3274\text{ m}^2$) |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Accumulate cylinder wall into statistical bin ($n = 1, \Sigma x = 251.3274$) |
| `4` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | Key in hemispherical dome radius ($4\text{ m}$) |
| `[f] [CIRC]` | $0.0000$ | $0.0000$ | $0.0000$ | $50.2655$ | Compute circular disk area via circle key ($\pi \times 4^2 = 50.2655\text{ m}^2$) |
| `2` | $0.0000$ | $0.0000$ | $50.2655$ | $2.0000$ | Key in dome factor 2 (half-dome area $= 2 \times \text{Circle Area}$); base area lifts to Register $Y$ |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $100.5310$ | Multiply by 2 to compute dome external surface ($100.5310\text{ m}^2$) |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Accumulate dome surface into statistical bin ($n = 2, \Sigma x = 351.8584$) |
| `[f] [Σx]` | $0.0000$ | $0.0000$ | $0.0000$ | $351.8584$ | Recall total accumulated exterior surface area ($\Sigma x$) |

Painting the fuel silo's cylinder wall and half-dome roof covers $\mathbf{351.86\text{ m}^2}$ of weather-resistant silver primer—all added up on your SC-6 without writing a single number on a clipboard!

Second, beside the main runway, civil engineering crews are lining an open $15\text{-meter-long}$ storm-water drainage canal with poured concrete so heavy rainstorms drain safely off the tarmac. Its cross-section is an open-top trapezoid: bottom width $1.2\text{ m}$, top opening width $2.4\text{ m}$, straight-up depth $0.8\text{ m}$, and slanted side walls $1.0\text{ m}$ wide each. How much concrete lining covers all 5 wet surfaces (1 flat bottom floor + 2 slanted side walls + 2 trapezoidal end gates)? Tossing each of the three surface groups into your `[Σ+]` basket and tapping `[f] [Σx]` via `[g] [CLΣ] 1.2 [ENTER] 15 [×] [Σ+] 1.0 [ENTER] 15 [×] [2] [×] [Σ+] 1.2 [ENTER] 2.4 [+] [2] [÷] 0.8 [×] [2] [×] [Σ+] [f] [Σx]` rings up **`50.88`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `[g] [CLΣ]` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Clear statistical registers ($n = 0, \Sigma x = 0$) |
| `1.2` | $0.0000$ | $0.0000$ | $0.0000$ | $1.2$ | Key in culvert channel bottom width ($1.2\text{ m}$) |
| `[ENTER]` | $0.0000$ | $0.0000$ | $1.2$ | $1.2$ | Stack lifts; bottom width locked into Register $Y$ |
| `15` | $0.0000$ | $0.0000$ | $1.2$ | $15.0000$ | Key in channel length ($15\text{ m}$) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $18.0000$ | Multiply to compute bottom slab area ($1.2 \times 15 = 18\text{ m}^2$) |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Deposit bottom slab area into bin ($n = 1, \Sigma x = 18$) |
| `1.0` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0$ | Key in slant side wall width ($1.0\text{ m}$) |
| `[ENTER]` | $0.0000$ | $0.0000$ | $1.0$ | $1.0$ | Stack lifts; slant width copied into Register $Y$ |
| `15` | $0.0000$ | $0.0000$ | $1.0$ | $15.0000$ | Key in channel length ($15\text{ m}$) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $15.0000$ | Multiply to compute single slant wall area ($15\text{ m}^2$) |
| `2` | $0.0000$ | $0.0000$ | $15.0000$ | $2.0000$ | Key in count of symmetric slant walls (2) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $30.0000$ | Multiply to compute twin slant walls ($2 \times 15 = 30\text{ m}^2$) |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Deposit slant walls into bin ($n = 2, \Sigma x = 48$) |
| `1.2` | $0.0000$ | $0.0000$ | $0.0000$ | $1.2$ | Key in trapezoid bottom width ($1.2\text{ m}$) |
| `[ENTER]` | $0.0000$ | $0.0000$ | $1.2$ | $1.2$ | Stack lifts; bottom width copied to Register $Y$ |
| `2.4` | $0.0000$ | $0.0000$ | $1.2$ | $2.4$ | Key in trapezoid top width ($2.4\text{ m}$) |
| `[+]` | $0.0000$ | $0.0000$ | $0.0000$ | $3.6$ | Add parallel bases ($1.2 + 2.4 = 3.6\text{ m}$) |
| `2` | $0.0000$ | $0.0000$ | $3.6$ | $2.0000$ | Key in averaging divisor 2 |
| `[÷]` | $0.0000$ | $0.0000$ | $0.0000$ | $1.8$ | Divide to compute average width ($1.8\text{ m}$) |
| `0.8` | $0.0000$ | $0.0000$ | $1.8$ | $0.8$ | Key in vertical channel depth ($0.8\text{ m}$) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $1.44$ | Multiply to compute single trapezoid end area ($1.44\text{ m}^2$) |
| `2` | $0.0000$ | $0.0000$ | $1.44$ | $2.0000$ | Key in count of end plates (2) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $2.88$ | Multiply to compute twin end plates ($2 \times 1.44 = 2.88\text{ m}^2$) |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $3.00$ | Deposit end plates into bin ($n = 3, \Sigma x = 50.88$) |
| `[f] [Σx]` | $0.0000$ | $0.0000$ | $0.0000$ | $50.88$ | Recall total accumulated concrete lining surface area |

Lining all five wet surfaces of the runway drainage canal takes $\mathbf{50.88\text{ m}^2}$ of poured concrete—protecting the airfield tarmac from the heaviest summer downpours while keeping every single face pair organized inside your `[Σ+]` statistical basket.

---

## 6.5 3D Solid Volume Dynamics

If **Surface Area** is the wrapping paper on the outside of a box, **Volume** is how many unit cubes, marbles, or liters of water fit *inside* the box!

Why do almost all 3D volume rules look so similar? Imagine stacking a deck of flat playing cards or a stack of identical round pancakes on a plate. A single card at the bottom covers a flat 2D **Floor Base Area**. As you stack more and more identical layers straight up to a **Height**, that flat footprint sweeps out a solid 3D **prism** or **cylinder**! That is why every flat-topped box, prism, or cylinder shares one master volume rule:
$$\text{Prism or Cylinder Volume} = \text{Floor Base Area} \times \text{Height}$$

What if the walls taper inward to a single point at the top, like a **cone** or a **pyramid**? Then the tapered top holds less than a straight-sided cylinder or box—in fact, it always holds **exact one-third**:
$$\text{Cone or Pyramid Volume} = (\text{Floor Base Area} \times \text{Height}) \div 3$$

| 3D Solid Shape | Floor Base Area | Word Rule for Volume |
|:---|:---|:---|
| **Rectangular Box (Prism)** | $\text{Length} \times \text{Width}$ | $\text{Box Volume} = \text{Length} \times \text{Width} \times \text{Height}$ |
| **Cube** | $\text{Side} \times \text{Side}$ | $\text{Cube Volume} = \text{Side} \times \text{Side} \times \text{Side}$ |
| **Cylinder** | $\text{Radius} \times \text{Radius} \times \pi$ | $\text{Cylinder Volume} = \text{Circle Floor Area} \times \text{Height}$ |
| **Square Pyramid** | $\text{Side} \times \text{Side}$ | $\text{Pyramid Volume} = (\text{Square Floor Area} \times \text{Height}) \div 3$ |
| **Cone** | $\text{Radius} \times \text{Radius} \times \pi$ | $\text{Cone Volume} = (\text{Circle Floor Area} \times \text{Height}) \div 3$ |
| **Sphere (Ball)** | *(Round Ball)* | $\text{Sphere Volume} = 4 \div 3 \times \pi \times \text{Radius}^3$ |

### 6.5.1 Rectangular Prisms & Cubes
To find the volume of any box-shaped prism or cube, first multiply $\text{Length} \times \text{Width}$ to build the bottom layer of unit cubes, and then multiply by the vertical $\text{Height}$ to stack that layer all the way to the ceiling. Suppose a steel cargo container on a freight ship measures $12\text{ meters}$ long, $2.4\text{ meters}$ wide, and $2.6\text{ meters}$ tall. Let's lay down the floor ($12 \times 2.4 = 28.8\text{ m}^2$) and raise it by the $2.6\text{ m}$ height to see how many cubic meters of cargo fit inside:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `12` | 0 | 0 | 0 | 12 |
| `[ENTER]` | 0 | 0 | 12 | 12 |
| `2.4` | 0 | 0 | 12 | $2.4$ |
| `[×]` | 0 | 0 | 0 | $28.8$ |
| `2.6` | 0 | 0 | $28.8$ | $2.6$ |
| `[×]` | 0 | 0 | 0 | $74.88$ |

The cargo volume is $\mathbf{74.88\text{ m}^3}$.

What happens when we pack a box with smaller fractional cubes—for instance, why does a $1\text{-inch}$ unit cube hold **eight** $\frac{1}{2}\text{-inch}$ mini-cubes instead of just two? Because you pack along all three spatial dimensions—$2$ cubes across the length, $2$ cubes back along the width, and $2$ cubes high ($2 \times 2 \times 2 = 8$). On your SC-6, entering `[.] 1 [.] 2 [x³]` ($\frac{1}{2} \times \frac{1}{2} \times \frac{1}{2}$) shows that each half-inch cube has a volume of $\mathbf{\frac{1}{8}\text{ in}^3}$. Thus, if a $3\frac{1}{2}\text{ in} \times 2\text{ in} \times 1\frac{1}{2}\text{ in}$ wooden block case holds $10\frac{1}{2}\text{ in}^3$ (`3 [.] 1 [.] 2 [ENTER] 2 [×] 1 [.] 1 [.] 2 [×]`), multiplying by `8 [×]` reveals it packs **$84$ half-inch cubes**.
- **Kea Parrot Puzzle-Box Height:** When animal cognition researchers build a rectangular acrylic puzzle box for an alpine kea parrot with a $9\text{ in} \times 5\text{ in}$ floor ($\text{Floor Area} = 45\text{ in}^2$) and a target internal volume of $360\text{ in}^3$, working the Stack Drop backward (`360 [ENTER] 9 [ENTER] 5 [×] [÷]`) finds the required height: $\text{Height} = 360 \div 45 = \mathbf{8\text{ inches}}$.
- **How Bicycle Tire Circumference Works:** Every time a bicycle wheel with a radius of $14\text{ inches}$ completes $1$ full spin, the tire unrolls its entire circumference along the pavement: keying `14 [ENTER] 2 [×] [π] [×]` ($\text{Circumference} = 2 \times \pi \times \text{Radius}$) shows the bike rolls forward **$87.96\text{ inches}$** ($\approx 7.33\text{ feet}$) per wheel revolution.

---

### 6.5.2 Cylinders & Storage Tanks
A right circular cylinder works just like stacking a tower of round coins or pancakes: you stamp out one flat circular floor disk of area $\text{Radius} \times \text{Radius} \times \pi$ (`[f] [CIRC]`) and multiply by the cylinder's $\text{Height}$.

Suppose a stainless-steel dairy storage tank has an inside diameter of $2.4\text{ meters}$ (so its radius from the center to the wall is half of that: $1.2\text{ m}$) and a vertical height of $4.5\text{ meters}$. Let's find the tank's volume in cubic meters, and then—since $1\text{ cubic meter}$ holds $1,000\text{ liters}$—convert that volume into liters of milk. Stamp out the $1.2\text{-meter}$ circular floor and raise it through the $4.5\text{-meter}$ height with `1.2 [f] [CIRC] 4.5 [×]` to obtain $20.3575\text{ m}^3$ on Register $X$, then scale directly by `1000 [×]` to see that the dairy silo holds $\mathbf{20,357.52\text{ Liters}}$ ($\mathbf{20.36\text{ m}^3}$ or $\mathbf{20,358\text{ liters}}$ of milk).

That same stack-extrusion pattern scales all the way up to city water infrastructure. Suppose a city science center has a cylindrical rooftop water storage tower with an interior radius of $4\text{ m}$ and a vertical height of $16\text{ m}$ to feed the museum's interactive hydro-exhibits. Fold up the Cylindrical Wrapper Net from your kit to picture the circular floor disk ($\pi \times \text{Radius}^2$) stacking upward through $16\text{ meters}$ of height like a column of coins. Stamping out the circular floor on Register $X$ ($50.2655\text{ m}^2$) and extruding that disk up the $16\text{-meter}$ tower height with `[4] [f] [CIRC] 16 [×]` reaches **`804`**, holding $\mathbf{804.25\text{ m}^3}$ ($\approx 804,248\text{ liters}$) of city water.

What happens when you combine rectangular prism volume and cylinder volume in the same part—by boring a round cylindrical hole straight through a solid square block? To keep pencils and calipers organized on a workbench, suppose you 3D-print a custom desk block that starts as a solid square prism ($10 \times 10 \times 5\text{ cm}$) with a round cylindrical cup hole of radius $2\text{ cm}$ bored straight through its $5\text{ cm}$ height. Just like punching the hole out of our flat 3D-printed spacer washer earlier—except now in three dimensions!—the net plastic volume equals the solid rectangular block minus the cylinder's volume. Holding the $500\text{ cm}^3$ outer prism on Register $Y$ while computing the $62.8319\text{ cm}^3$ cylindrical hole on Register $X$ and subtracting with `10 [x²] [5] [×] [2] [f] [CIRC] [5] [×] [-]` yields **`437.16814693`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `10` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | Key in square block side length ($10\text{ cm}$) |
| `[x²]` | $0.0000$ | $0.0000$ | $0.0000$ | $100.0000$ | Square side length to find block top area ($10^2 = 100\text{ cm}^2$) |
| `5` | $0.0000$ | $0.0000$ | $100.0000$ | $5.0000$ | Key in block height ($5\text{ cm}$); top area lifts to Register $Y$ |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $500.0000$ | Multiply to compute gross solid prism volume ($500\text{ cm}^3$) |
| `2` | $0.0000$ | $0.0000$ | $500.0000$ | $2.0000$ | Key in cylindrical hole radius ($2\text{ cm}$); prism volume lifts to Register $Y$ |
| `[f] [CIRC]` | $0.0000$ | $0.0000$ | $500.0000$ | $12.5664$ | Compute hole circular area via circle key ($\pi \times 2^2$) |
| `5` | $0.0000$ | $500.0000$ | $12.5664$ | $5.0000$ | Key in hole depth ($5\text{ cm}$); circle area lifts to Register $Y$ |
| `[×]` | $0.0000$ | $0.0000$ | $500.0000$ | $62.8319$ | Multiply area by depth to compute cylindrical void volume ($62.8319\text{ cm}^3$) |
| `[-]` | $0.0000$ | $0.0000$ | $0.0000$ | $437.1681$ | Subtract cylindrical void from solid block to find net plastic volume |

The finished 3D-printed desk caddy uses $\mathbf{437.17\text{ cm}^3}$ of plastic.

---

### 6.5.3 Cones & Pyramids: The $3:1$ Pouring Proof
Why do cones and pyramids divide by $3$? Try this kitchen-table experiment: roll a stiff paper cone that has the exact same circular opening and height as a drinking glass. If you fill the cone to the brim with dry rice or water and pour it into the glass, one cone fills the glass one-third of the way; a second cone fills it two-thirds; and the **third cone fills the cylinder right to the rim**! Whether the base is a circle (a cone) or a square (a pyramid), three pointed solids always fill one straight-sided prism or cylinder of the same base and height:
$$\text{Cylinder Volume} = 3 \times \text{Cone Volume}, \qquad \text{Cone Volume} = (\text{Circle Floor Area} \times \text{Height}) \div 3$$

To test this $3:1$ rule in the science lab, picture a conical glass funnel with a top opening radius of $6\text{ cm}$ and an internal depth of $10\text{ cm}$. If you plug the bottom stem, how many cubic centimeters of liquid can the cone hold? First, tap `[6] [f] [CIRC]` to find the circular opening area ($113.0973\text{ cm}^2 = \text{Radius}^2 \times \pi$), and multiply by the depth with `10 [×]` to get the volume of a full cylinder of the same base and height ($1,130.9734\text{ cm}^3$). Dividing by three with `[3] [÷]` takes exact one-third of that cylinder, revealing a funnel capacity of $\mathbf{376.99\text{ cm}^3}$.

What if a beach sandcastle bucket is shaped like a cone that had its pointy tip sliced flat (a shape architects call a *frustum*)? Suppose sculptors in the science center courtyard are packing wet sand into a colossal festival sandcastle mold with a wide bottom radius of $10\text{ m}$, a flat top radius of $6\text{ m}$, and a vertical height of $12\text{ m}$. Because the bucket tapers smoothly from a $10\text{ m}$ bottom radius to a $6\text{ m}$ top radius, you find its volume in clear steps: first add the three radius products ($\text{Bottom} \times \text{Bottom} = 10 \times 10 = 100$, $\text{Top} \times \text{Top} = 6 \times 6 = 36$, and $\text{Bottom} \times \text{Top} = 10 \times 6 = 60$, totaling $100 + 36 + 60 = 196$), then multiply by $\pi$ and the $12\text{ m}$ height, and divide by $3$ with `10 [x²] [6] [x²] [+] 10 [ENTER] [6] [×] [+] [π] [×] 12 [×] [3] [÷]` to land on **`2,463.00864`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `10` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | Key in wide bottom radius ($10\text{ m}$) |
| `[x²]` | $0.0000$ | $0.0000$ | $0.0000$ | $100.0000$ | Bottom $\times$ Bottom ($10 \times 10 = 100$) |
| `6` | $0.0000$ | $0.0000$ | $100.0000$ | $6.0000$ | Key in flat top radius ($6\text{ m}$); $100$ lifts to Register $Y$ |
| `[x²]` | $0.0000$ | $0.0000$ | $100.0000$ | $36.0000$ | Top $\times$ Top ($6 \times 6 = 36$) |
| `[+]` | $0.0000$ | $0.0000$ | $0.0000$ | $136.0000$ | Add the first two products ($100 + 36 = 136$) |
| `10` | $0.0000$ | $0.0000$ | $136.0000$ | $10.0000$ | Key in bottom radius 10; sum $136$ lifts to Register $Y$ |
| `[ENTER]` | $0.0000$ | $136.0000$ | $10.0000$ | $10.0000$ | Stack lifts; radius 10 copied to Register $Y$ |
| `6` | $0.0000$ | $136.0000$ | $10.0000$ | $6.0000$ | Key in top radius 6 |
| `[×]` | $0.0000$ | $0.0000$ | $136.0000$ | $60.0000$ | Bottom $\times$ Top ($10 \times 6 = 60$) |
| `[+]` | $0.0000$ | $0.0000$ | $0.0000$ | $196.0000$ | Add all three radius products ($136 + 60 = 196$) |
| `[π]` | $0.0000$ | $0.0000$ | $196.0000$ | $3.1416$ | Push circle constant $\pi$; $196$ lifts to Register $Y$ |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $615.7522$ | Multiply by $\pi$ ($196 \times \pi \approx 615.7522$) |
| `12` | $0.0000$ | $0.0000$ | $615.7522$ | $12.0000$ | Key in bucket height ($12\text{ m}$) |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $7389.0259$ | Multiply by height ($7389.0259$) |
| `3` | $0.0000$ | $0.0000$ | $7389.0259$ | $3.0000$ | Key in cone divisor 3 |
| `[÷]` | $0.0000$ | $0.0000$ | $0.0000$ | $2463.0086$ | Divide by 3 to find the sandcastle bucket volume |

The giant sandcastle bucket holds $\mathbf{2463.01\text{ m}^3}$ of sand.

---

### 6.5.4 Spheres & Hemispheres
What about a completely round ball, or **sphere**, like a basketball, a weather balloon, or Planet Earth? Around 225 BC, the Greek inventor Archimedes imagined placing a sphere snugly inside a cylinder of the exact same radius and twice the radius in height. He proved that the sphere takes up **exact two-thirds** of that cylinder's volume, which simplifies to:
$$\text{Sphere Volume} = 4 \div 3 \times \pi \times \text{Radius}^3$$

As Steven Strogatz notes *([Strogatz, 2012](sc6/appendix-c-formulas-and-conversions.md#cite-strogatz2012))*, Archimedes loved this sphere discovery so much that he asked for a carving of a sphere inside a cylinder to be placed on his tombstone! Today, meteorologists use Archimedes' rule every morning: before launching a high-altitude weather balloon into the stratosphere, they inflate the latex sphere to a radius of $1.5\text{ meters}$. How many cubic meters of helium gas does it take to fill the balloon?

Begin by keying `4 [ENTER] 3 [÷]` to stage $4$ onto Floor $Y$ and divide by $3$, forming Archimedes' sphere ratio $4 \div 3 \approx 1.33333$ on Floor $X$, and tap `[π] [×]` to scale by the circle constant $\pi \longrightarrow 4.18879$. Next, key `1.5 [ENTER] 3 [g] [yˣ]`—which lifts $4.18879$ safely onto Floor $Y$ while cubing the balloon's radius ($1.5 \times 1.5 \times 1.5 = 1.5^3 = 3.375\text{ m}^3$) on Floor $X$—and tap `[×]` to merge both shelves into $\mathbf{14.14\text{ m}^3}$ of helium gas.

---

### 6.5.5 Fluid Displacement & Irregular Objects
How do you measure the volume of a bumpy, lumpy object—like a quartz crystal, a metal bolt, or a toy dinosaur—that doesn't have a neat length, width, or radius? Legend says Archimedes solved this mystery while stepping into a full bathtub and watching the water overflow! When you lower an underwater object into a cylindrical beaker of water, the object pushes water out of the way, making the water level rise into a **new cylindrical slice**. The volume of that rising cylinder of water equals the exact volume of the rock!

Suppose you pour water into a cylindrical glass beaker with an inside radius of $4\text{ cm}$, and when you gently lower a bumpy mineral rock beneath the surface, the water level rises by $1.8\text{ cm}$. To measure the rock's volume on the stack, stamp out the circular cross-section of the beaker first and multiply by the $1.8\text{ cm}$ water rise with `[4] [f] [CIRC] 1.8 [×]` $\to \mathbf{90.4779\text{ cm}^3}$, proving that the bumpy mineral specimen occupies $\mathbf{90.48\text{ cm}^3}$.

---

## 6.6 Planetary Geared Clock & Continuous Modulo-60 Elapsed Time

Circle geometry doesn't stop with pizzas, fountains, and water tanks—it also governs how we measure **time**! Every time you look at an analog wall clock, you are watching two pointers sweep around a $360^\circ$ circle, linked together inside the clock by a $12:1$ train of gears.

### 6.6.1 How the Gears Inside Your Planetary Clock Work Together
Have you ever played with a cheap plastic classroom teaching clock where the hour hand and minute hand spin loosely on their own? On those disconnected dials, it is easy to accidentally point the hour hand straight at the $4$ while the minute hand points down at $30$ minutes—a position that can never happen on a real clock!

Why? Because inside a real clock, the minute hand and the hour hand are locked together by **planetary gears**. Your StackCalc studio kit pairs the SC-6 with a 3D-printed **Planetary Geared Clock** built around an exact $12.0000:1$ gear reduction train:
- Every time you turn the **minute hand** through one full $360^\circ$ lap ($60\text{ minutes}$), the internal planet gears smoothly carry the **hour hand** forward by $\frac{1}{12}\text{th}$ of a circle ($360^\circ \div 12 = 30^\circ$, or 1 hour).
- That means at **3:30**—when the minute hand has traveled halfway around the circle ($180^\circ$)—the hour hand does **not** sit still on the $3$. The gears have already pushed it halfway between the $3$ and the $4$ ($3.5\text{ hours} \times 30^\circ/\text{hr} = 105^\circ$)!

As Matt Parker observes in *Humble Pi* *([Parker, 2019](sc6/appendix-c-formulas-and-conversions.md#cite-parker2019))*, real-world engineering mistakes often happen when people forget how linked gears or base-60 time cycles move together. With your Planetary Geared Clock in your hands and `[🕒]` on your SC-6, you can see and feel every minute pulling the hour hand along in smooth lockstep.

| Clock Hand at $3:30$ | Dial Position | Continuous Mechanical Angle |
| :--- | :--- | :--- |
| **Minute Hand** | Points directly at **$6$** ($30\text{ min}$) | $30 \times 6^\circ = \mathbf{180.0^\circ}$ (half turn) |
| **Hour Hand** | Halfway between **$3$** and **$4$** ($3.5\text{ hr}$) | $(3 + 30/60) \times 30^\circ = 3.5 \times 30^\circ = \mathbf{105.0^\circ}$ |

### 6.6.2 Continuous Hand Angle Verification

Because one complete lap around a clock face measures $360^\circ$:
- The **minute hand** sweeps $360^\circ$ in 60 minutes, moving **$6^\circ$ per minute** ($360^\circ \div 60 = 6^\circ$):
  $$\text{Minute Angle} = \text{minutes} \times 6^\circ$$
- The **hour hand** sweeps $360^\circ$ in 12 hours, moving **$30^\circ$ per hour** (or half a degree every single minute!):
  $$\text{Hour Angle} = \left(\text{hours} + \frac{\text{minutes}}{60}\right) \times 30^\circ$$

For $3:30$ ($3.30\text{ HMS}$):
- **Minute Hand:** $30 \times 6^\circ = \mathbf{180.0^\circ}$.
- **Hour Hand:** $\left(3 + \frac{30}{60}\right) \times 30^\circ = 3.5 \times 30^\circ = \mathbf{105.0^\circ}$.

You can use that exact same rule to verify any analog cockpit heading indicator! Inside an airport flight dispatch tower, suppose a clock-style heading indicator reads 4:20 ($4.20\text{ HMS}$), and the pilot asks for the exact continuous angle of the hour hand using $(4 + 20/60) \times 30^\circ$. Turn your Planetary Geared Clock to 4:20: notice that the hour hand does not stay pinned on the 4, but advances smoothly one-third of the way toward 5, reaching $130^\circ$. Park the base hour `4` in Register $Y$ with `[ENTER]`, convert the 20 minutes into $\frac{1}{3}$ of an hour (`20`, `[ENTER]`, `60`, `[÷]`), merge them into $4.3333$ decimal hours, and scale by $30^\circ$ per hour via `[4] [ENTER] 20 [ENTER] 60 [÷] [+] 30 [×]` to land on **`130`**, proving why the hour hand rests at $130^\circ$ ($10^\circ$ past the 4).

---

### 6.6.3 Clock Time (`H.MMSS`) Entry and `[f] [▸HR]` / `[g] [▸HMS]` Conversion
Why can't you add clock times like ordinary decimals on a regular calculator? Because ordinary decimals count to $100$ before carrying over, whereas clock minutes count to **$60$**! If you type $9.45 + 2.35 = 11.80$, a regular calculator treats $45\text{ minutes} + 35\text{ minutes}$ as $.80$, when in reality $80\text{ minutes}$ is **1 hour and 20 minutes** ($12{:}20$)!

On the SC-6, two shifted keys (`[f] [▸HR]` and `[g] [▸HMS]`) translate between base-60 clock time and base-10 decimal hours automatically:
- **Step 1 (Enter Clock Time as `H.MMSS`):** Type `9.45` for 9 hours 45 minutes (or `9.4530` for 9 hours, 45 minutes, 30 seconds).
- **Step 2 (Convert to Decimal Hours with `[f] [▸HR]`):** Tapping `[f] [▸HR]` turns $9\text{ hr } 45\text{ min}$ into `9.7500` hours (because $45\text{ minutes}$ is $\frac{45}{60} = \frac{3}{4} = 0.75$ of an hour!).
- **Step 3 (Do Your Math, Then Tap `[g] [▸HMS]`):** Once your times are in decimal hours, you can add, subtract, or multiply them normally—and tap `[g] [▸HMS]` at the end to turn the decimal answer right back into `Hours.MinutesSeconds`!

Better yet, because `[f] [▸HR]` gives you a clean decimal number like `9.7500` on Register $X$, you can also multiply a flight's decimal hours directly by its speed in miles per hour to find distance, or multiply a babysitter's decimal hours by their hourly pay rate!

---

### 6.6.4 Continuous Geared Clock Elapsed Time (`[🕒]`)

![Planetary Clock Planetary Gear Stages: 12:1 Compound Reduction](../assets/renders/clock-gear-stages-macro.png)

![Planetary Geared Clock: 12.0000:1 Planetary Reduction Gear Train at 3:30 (105.0° Continuous Hour Hand)](../assets/manuals/planetary_geared_clock_330.png)

Let's test both your physical Planetary Geared Clock and your SC-6 on a real flight schedule. Suppose a plane departs New York at 9:45 AM ($9.45\text{ HMS}$) and flies for 2 hours and 35 minutes ($2.35\text{ HMS}$). What time does it touch down?

First, try it with your hands on the physical Planetary Geared Clock: turn the dial until the hands show 9:45, noticing how the hour hand is physically locked three-quarters of the way between 9 and 10 ($9.75\text{ hours} \times 30^\circ/\text{hr} = 292.5^\circ$). Now rotate the minute ring through 2 full turns ($120\text{ minutes} = 2\text{ hours}$) plus 35 more minutes, and watch the hour hand glide smoothly past 12 to land at **12:20**. Now let's verify that exact arrival time on the 4-register stack:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `9.45 [f] [▸HR]` | 0 | 0 | 0 | 9.7500 | Enter 9:45 AM and convert to decimal hours ($9.7500\text{ hr}$; stack lift armed) |
| `2.35 [f] [▸HR]` | 0 | 0 | 9.7500 | 2.5833 | Enter 2 hr 35 min flight duration (automatically lifting $9.7500$ to $Y$) and convert ($2.5833\text{ hr}$) |
| `[+]` | 0 | 0 | 0 | 12.3333 | Add decimal hours: $9.75 + 2.5833 = 12.3333\text{ hr}$ |
| `[g] [▸HMS]` | 0 | 0 | 0 | 12.2000 | Convert back to clock time: 12:20 PM arrival |

The flight lands at **12:20 PM**, matching your physical geared clock to the second!

> **Why Base-10 Decimals Fail on Base-60 Clock Time:** You cannot simply type `9.45 + 2.35` on a standard calculator to add clock times, because $45 + 35 = 80$ and there are $60$ minutes in an hour, not $100$. On the SC-6, pressing `[f] [▸HR]` converts hours and minutes into true decimal hours so you can add or subtract normally, and `[g] [▸HMS]` converts the decimal total right back into hours, minutes, and seconds.

What if a cross-country cargo flight has multiple legs and a refueling layover in the middle? Suppose a cargo plane departs at 10:00 AM, flies Leg 1 for 2h 15m ($2.15\text{ HMS}$), stops for a refueling layover of 1h 30m ($1.30\text{ HMS}$), and flies Leg 2 for 3h 20m ($3.20\text{ HMS}$). What time does it touch down at its final destination? Trace all three segments on your Planetary Geared Clock ($10{:}00 \to 12{:}15 \to 13{:}45 \to 17{:}05$) and chain them in decimal hours on the stack using `10 [f] [▸HR] 2.15 [f] [▸HR] [+] 1.30 [f] [▸HR] [+] 3.20 [f] [▸HR] [+] [g] [▸HMS]` to reach **`17.05`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `10` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | Key in initial departure time 10:00 AM (`HH.MM`) |
| `[f] [▸HR]` | $0.0000$ | $0.0000$ | $0.0000$ | $10.0000$ | Convert departure to decimal hours ($10.0\text{ hr}$) |
| `2.15` | $0.0000$ | $0.0000$ | $10.0000$ | $2.1500$ | Key in Leg 1 flight duration (2h 15m); departure lifts to Register $Y$ |
| `[f] [▸HR]` | $0.0000$ | $0.0000$ | $10.0000$ | $2.2500$ | Convert Leg 1 time to decimal hours ($2 + 15/60 = 2.25$) |
| `[+]` | $0.0000$ | $0.0000$ | $0.0000$ | $12.2500$ | Add Leg 1 to departure time ($12.25\text{ hr}$) |
| `1.30` | $0.0000$ | $0.0000$ | $12.2500$ | $1.3000$ | Key in airport layover duration (1h 30m) |
| `[f] [▸HR]` | $0.0000$ | $0.0000$ | $12.2500$ | $1.5000$ | Convert layover to decimal hours ($1 + 30/60 = 1.5$) |
| `[+]` | $0.0000$ | $0.0000$ | $0.0000$ | $13.7500$ | Add layover to accumulated itinerary ($13.75\text{ hr}$) |
| `3.20` | $0.0000$ | $0.0000$ | $13.7500$ | $3.2000$ | Key in Leg 2 flight duration (3h 20m) |
| `[f] [▸HR]` | $0.0000$ | $0.0000$ | $13.7500$ | $3.3333$ | Convert Leg 2 to decimal hours ($3 + 20/60 = 3.3333$) |
| `[+]` | $0.0000$ | $0.0000$ | $0.0000$ | $17.0833$ | Add Leg 2 to find landing time in decimal hours |
| `[g] [▸HMS]` | $0.0000$ | $0.0000$ | $0.0000$ | $17.0500$ | Convert decimal hours back to clock time (`17:05` or `5:05 PM`) |

The cargo flight touches down at $\mathbf{17:05\text{ HMS}}$ ($5:05\text{ PM}$), right on schedule for the evening ground crew!

---

### 6.6.5 Midnight Boundary Crossings
What happens when an astronomy stargazing session or an overnight scientific instrument run starts late in the evening and continues past midnight (`24:00`) into the next morning? Whenever your accumulated decimal hours (`[f] [▸HR]`) climb past `24`, the clock has wrapped into a new day—so you simply subtract `24` (one full 24-hour daily cycle) on the stack before pressing `[g] [▸HMS]` to read the morning clock time!

Let's watch every register during a midnight crossing up in the science center's planetarium observatory dome! An automated telescope camera begins a deep-sky exposure at 21:30 ($9{:}30\text{ PM}$, which converts via `21.30 [f] [▸HR]` to $21.5000\text{ decimal hours}$) and tracks a glowing nebula across the night sky for 4 hours and 45 minutes ($4.45\text{ HMS}$, or $4.7500\text{ decimal hours}$). When you press `[+]` to combine the start time and runtime, the total reaches $26.2500\text{ hours}$—exceeding 24 hours because the telescope tracked right across the midnight boundary! Rotating your Planetary Geared Clock past midnight wraps the hour hand smoothly into the new morning, matching modulo-24 subtraction (`24 [-]` $\to 2.2500\text{ hr}$) and `[g] [▸HMS]` conversion on the stack when you run `21.30 [f] [▸HR] 4.45 [f] [▸HR] [+] 24 [-] [g] [▸HMS]` to reach **`2.15`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `21.30` | $0.0000$ | $0.0000$ | $0.0000$ | $21.3000$ | Key in start time 21:30 (`HH.MM` format) |
| `[f] [▸HR]` | $0.0000$ | $0.0000$ | $0.0000$ | $21.5000$ | Convert start time to decimal hours ($21 + 30/60 = 21.5$) |
| `4.45` | $0.0000$ | $0.0000$ | $21.5000$ | $4.4500$ | Key in tracking runtime 4h 45m; start time lifts to Register $Y$ |
| `[f] [▸HR]` | $0.0000$ | $0.0000$ | $21.5000$ | $4.7500$ | Convert runtime to decimal hours ($4 + 45/60 = 4.75$) |
| `[+]` | $0.0000$ | $0.0000$ | $0.0000$ | $26.2500$ | Add runtime to start time, exceeding 24 hours ($26.25\text{ hr}$ total) |
| `24` | $0.0000$ | $0.0000$ | $26.2500$ | $24.0000$ | Key in 24-hour daily cycle; accumulated hours lift to Register $Y$ |
| `[-]` | $0.0000$ | $0.0000$ | $0.0000$ | $2.2500$ | Deduct 24 hours to cross midnight into the next morning ($2.25\text{ hr}$) |
| `[g] [▸HMS]` | $0.0000$ | $0.0000$ | $0.0000$ | $2.1500$ | Convert decimal hours back to clock format (`02:15 AM`) |

The telescope time-lapse finishes at $\mathbf{02:15\text{ AM}}$ ($2.15\text{ HMS}$).

---

### 6.6.6 Planetary Clock Gear Ratio Derivation
If you flip your Planetary Geared Clock over and peek at the gears inside, how do those three spinning planet gears create an exact $12:1$ reduction? Count the teeth on each gear:
- **Center Sun Gear:** $12\text{ teeth}$
- **Three Planet Gears:** $60\text{ teeth}$ each
- **Outer Ring Gear:** $132\text{ teeth}$

The gear ratio between the minute hand and the hour hand comes straight from comparing the big outer ring gear to the small center sun gear:
$$\text{Clock Gear Ratio} = 1 + (\text{Outer Ring Teeth} \div \text{Center Sun Teeth}) = 1 + (132 \div 12) = 1 + 11 = 12$$
Every 12 full turns of the minute hand turn the hour hand 1 full circle ($12:1$), keeping both hands smoothly synchronized.

### 6.6.7 How Gear Teeth Fit Together Without Jamming
In STEM maker labs, you can 3D-print functional clock gears using open-source blueprints (see Appendix A). In our classroom gear set, each gear tooth adds $1.0\text{ mm}$ to the gear's width (diameter):
$$\text{Gear Width in mm} = 1.0\text{ mm per tooth} \times \text{Number of Teeth}$$
- **Center Sun Gear ($12\text{ teeth}$):** $1.0 \times 12 = 12.0\text{ mm}$ wide
- **Planet Gears ($60\text{ teeth}$ each):** $1.0 \times 60 = 60.0\text{ mm}$ wide
- **Outer Ring Gear ($132\text{ teeth}$):** $1.0 \times 132 = 132.0\text{ mm}$ wide

You can verify the simple tooth-count rule that makes all your clock gears sit flat and fit together inside the ring: the number of teeth on the big **Outer Ring Gear** must equal the **Center Sun Gear** plus **two Planet Gears** sitting side-by-side:
$$\text{Outer Ring Teeth} = \text{Center Sun Teeth} + (2 \times \text{Planet Gear Teeth}) \longrightarrow 132 = 12 + (2 \times 60) = 12 + 120 = 132$$
Because $12 + 120 = 132$, all three planet gears mesh smoothly around the center sun gear without jamming!

---

### 6.6.8 Watch Out for These Two Geometry & Clock Traps

- **The Open-Top Aquarium Dilemma:** Suppose you are building an open-top glass aquarium measuring $10\text{ in.}$ long, $8\text{ in.}$ wide, and $6\text{ in.}$ tall. If you blindly add all 6 faces of a closed box, you will buy glass for a sealed top lid. An open aquarium has only **five** glass faces: one bottom ($10 \times 8$), two front/back walls ($2 \times 10 \times 6$), and two left/right ends ($2 \times 8 \times 6$). With `[Σ+]`, you simply add each real face (`10 [ENTER] 8 [×] [Σ+]`, then `10 [ENTER] 6 [×] 2 [×] [Σ+]`, then `8 [ENTER] 6 [×] 2 [×] [Σ+]`) and tap `[f] [Σx]` to get **$296\text{ in.}^2$**.
- **The 3:30 Clock-Hand Angle Trap:** What is the angle between the hour and minute hands at $3{:}30$? It is tempting to say $90^\circ$ because $3$ and $6$ are a quarter-circle apart. Turn the minute hand on your Planetary Geared Clock from $3{:}00$ to $3{:}30$: because the internal gears are linked ($12:1$), the hour hand does not sit frozen on the $3$—it advances halfway toward the $4$ (moving $15^\circ$ from $90^\circ$ to $105^\circ$). With the minute hand at $180^\circ$, the true angle between them is $180^\circ - 105^\circ = \mathbf{75^\circ}$.

---

### 6.6.9 Common Stack Slips & How to Fix Them

| What Happened on Your Screen | Why It Happened | How to Fix It |
| :--- | :--- | :--- |
| **Adding $9.45 + 2.35 = 11.80$** | Confusing base-60 clock minutes with base-10 decimal fractions. | *"There are 60 minutes in an hour, not 100. 45 minutes + 35 minutes = 80 minutes, which is 1 hour and 20 minutes. Always convert using `[f] [▸HR]` before adding, then convert back with `[g] [▸HMS]`."* |
| **Forgetting to multiply faces by 2** | Omitting the matching opposite face in a rectangular box. | *"Hold the 3D wooden box. Does it have only one top, or both a top AND a bottom? Every rectangular box has 3 pairs of matching faces. Always multiply each face product by 2 before tapping `[Σ+]`."* |
| **Calculating 6 faces for an open container** | Adding all 6 faces of a closed box without checking whether the top is open. | *"Look at the real object. Is the tank sealed shut like a shipping crate, or open like a bucket? Only multiply by 2 if both opposing faces actually exist."* |
| **Static hour-hand misconception ($3:30 \to 90^\circ$)** | Assuming the hour hand jumps instantaneously on the hour. | *"Look at the planetary gears in our clock manipulative. The hour hand moves continuously in lockstep with the minutes. At 30 minutes past, the hour hand is exactly halfway to the next number."* |
| **Treating volume as surface area** | Confusing boundary area (units of $\text{cm}^2$) with interior capacity (units of $\text{cm}^3$). | *"Area is the wrapping paper covering the outside of the present; volume is the number of toy blocks packed inside the box."* |
| **Omitting the $\frac{1}{3}$ factor in cone volume** | Assuming a cone holds the same volume as a cylinder of equal height. | *"Remember our water pouring experiment: it took 3 full cones of water to fill the cylinder. A cone is always one-third of the cylinder: divide by 3."* |

### 6.6.10 Blind Formula Plugging vs. Geoboards, Folding Nets & Stack Accumulation

Now that you have explored 2D shapes, 3D volumes, and the `[Σ+]` wall-basket method, compare how a parenthesized surface-area formula is entered on a standard calculator versus face-by-face accumulation on the SC-6:

| Challenge / Equation | The Algebraic Calculator Trap (Standard Entry) | The StackCalc SC-6 + Manipulative Method | Keystroke Reduction | Live Stack Visibility | Learning Breakthrough |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **Rectangular Prism Surface Area:** $2(8 \times 5 + 8 \times 3 + 5 \times 3)$ | `2 * ( 8 * 5 + 8 * 3 + 5 * 3 ) =` (19 keystrokes). One missed bracket or operator typo ruins the entire expression. No individual face audit is possible. *Trap: Decimals or typos force complete re-entry; zero visual verification of intermediate face pairs.* | **SC-6 + Stats Mode (`[Σ+]`):** `[g] [CLΣ] 8 [ENTER] 5 [×] [Σ+] 3 [×] [Σ+] 5 [ENTER] 3 [×] [Σ+] [f] [Σx] 2 [×]` $\rightarrow \mathbf{158.0\text{ cm}^2}$ (17 keystrokes). Every face pair verified on screen before accumulating; zero scratch paper. | **11% fewer keystrokes** (17 vs. 19) | **100% Face Visibility:** Tracks item count $n = 1, 2, 3$ and lets you inspect intermediate face areas ($40, 24, 15$) before multiplying by 2. | **Modular Face Decomposition:** Transforms abstract bracket clutter into an intuitive physical inventory of 2D nets; mistakes can be corrected face-by-face without starting over. |

---

## 6.7 Where to Go Next: Companion Workbook Quests & Kitchen-Table Challenges

> *For 33 additional worked problems with full 4-register stack tables, see Chapter 6 of the [SC-6 Elementary Companion Problem & Activity Workbook](../curriculum/sc6-elementary-companion-workbook.md).*


Ready to put your 3D stacked block prisms, `[Σ+]` surface area accumulator, and Planetary Geared Clock to the test? Grab your companion workbooks and try these three hands-on builds:

- **[Big Ideas Math Middle School Supplement](../curriculum/big-ideas-middle-school-sc6-workbook.md):** Open **Unit 5: Areas of Polygons & Elapsed Time (Sections 5.1–5.4)** and **Unit 8: Surface Area & Volume of 3D Solids (Sections 8.1–8.4)** for cut-and-slide parallelogram proofs, diamond kite and skateboard ramp triangles, cardstock net blueprints (`[Σ+]`), $\frac{1}{2}\text{-inch}$ fractional cube packing, kea parrot puzzle-box volumes, and Planetary Geared Clock investigations.
- **Timed Proficiency Trials & 12-Unit Curriculum Guide:** Run the **Scratch-Paper-Free `[Σ+]` Surface Area Sprint** in **Unit 7 of the Curriculum Guide**, racing to accumulate 3D prism and pyramid faces with zero parentheses and zero written intermediate numbers.

### 6.7.1 Three Hands-On Kitchen-Table Quests
1. **The Cereal-Box Unfolding Audit (`[g] [CLΣ]`, `[Σ+]`, `[f] [Σx]`):** Take an empty cardboard cereal or cracker box and carefully slit along three vertical edges so all six rectangular walls unfold flat on the kitchen table. Measure the length, width, and height in centimeters, accumulate all three opposing face pairs on your SC-6 using `[Σ+]`, and then use `[f] [LASTX]` to compute the internal volume ($\text{Length} \times \text{Width} \times \text{Height}$)—how many square centimeters of cardboard does it take to hold each cubic centimeter of cereal?
2. **The Three-Cone Rice Pouring Proof (`[f] [CIRC]` and `[g] [CONE]`):** Roll a sheet of stiff paper into a cone that has the exact same circular opening and height as a kitchen drinking glass, and tape the seam. Fill the paper cone to the brim with dry rice or popcorn kernels and pour it into the glass—count how many cones it takes to fill the cylinder to the top, then verify both volumes on your SC-6.
3. **The Live Clock-Hand Angle Hunt (`[f] [▸HR]` and `[g] [▸HMS]`):** Look at a wall clock right now (or set your Planetary Geared Clock to your favorite time of day). Use your SC-6 to compute the exact continuous angle of the hour hand ($\text{decimal hours} \times 30^\circ$) and minute hand ($\text{minutes} \times 6^\circ$), and find the exact degree wedge between them.

---

## 6.8 Chapter Summary & Looking Ahead

This chapter covered four core areas of spatial measurement and continuous time:

1. **2D Plane Geometry:** Perimeter and area across rectangles, triangles, parallelograms, trapezoids, and circles using dedicated geometry keys (`[f] [RECT]`, `[g] [TRI]`, `[f] [CIRC]`, `[π]`) and `[f] [LASTX]`.
2. **The Master Surface Area Technique:** Accumulating opposing face pairs into statistical registers with `[Σ+]` to find the total outer surface area of 3D solids without intermediate scratch-paper notes.
3. **3D Volume & Capacity:** Using the Stack Drop method to turn flat base areas into three-dimensional volumes (`[f] [PRISM]`, `[g] [CONE]`) and fluid capacities.
4. **Planetary Geared Time:** Continuous modulo-60 elapsed time on the 12:1 planetary gear train (`[🕒]`), converting between decimal hours and clock format (`[f] [▸HR]`, `[g] [▸HMS]`).

In **[Chapter 07: Discrete Probability, Primes & Pre-Algebra](sc6/07-data-probability-primes.md)**, you will examine the structure of whole numbers and empirical data—organizing observations into frequency tables, computing means and medians with statistical accumulators, and building prime factorizations with Prime Factor Blocks and the SC-6 number-theory keys (`[PRIME]`, `[g] [FACT]`, `[g] [÷R]`).

---

# Chapter 7: Discrete Probability, Primes & Pre-Algebra

## 7.1 The 17-Year Cicada Mystery: How Prime Numbers Outsmart Predators and Fair Dice Balance Chance

Deep beneath the deciduous forests of eastern North America, millions of periodical cicada nymphs (*Magicicada septendecim*) sip tree-root sap in the dark for **17 years**—until, on a single warm spring weekend, billions of them tunnel out of the soil at once and fill the forest canopy with a deafening chorus *([Gould, 1977](sc6/appendix-c-formulas-and-conversions.md#cite-gould1977))*. Across living ecosystems, spacecraft communications, and tabletop games, **prime numbers and probability govern how creatures outsmart predators, how secret codes stay unbreakable, and how dice roll with equal chance.**

### 7.1.1 Why Cicadas Count in Primes

Naturalists and mathematical biologists long investigated a fascinating evolutionary question *([Gould, 1977](sc6/appendix-c-formulas-and-conversions.md#cite-gould1977); [Webb, 2001](sc6/appendix-c-formulas-and-conversions.md#cite-webb2001))*: **Why 13 years? Why 17 years?** Why didn't cicadas evolve a 12-year, 14-year, or 16-year life cycle?

To see the danger of a non-prime schedule, picture the **Deadly Composite Trap** that would happen if a cicada brood emerged on a 12-year cycle. The number 12 is **composite**, meaning its factors are $1, 2, 3, 4, 6,$ and $12$:
- A predatory bird or parasitic wasp with a 2-year population surge would synchronize with them on every single emergence ($2 \times 6 = 12$).
- A predator with a 3-year boom cycle would meet them every emergence ($3 \times 4 = 12$).
- A predator with a 4-year cycle would feast on them every emergence ($4 \times 3 = 12$).

The cicada population would be devastated by specialized parasites at every generation!

Now compare that trap with the **Prime Number Shield** of 17. The number 17 is **prime**, so its *only* factors are 1 and 17:
- A 2-year cyclical predator intersects with the cicadas only once every **34 years** ($\text{Least Common Multiple of } 2\text{ and } 17 = 34$).
- A 3-year cyclical predator intersects only once every **51 years** ($\text{Least Common Multiple of } 3\text{ and } 17 = 51$).
- A 5-year cyclical predator intersects only once every **85 years** ($\text{Least Common Multiple of } 5\text{ and } 17 = 85$).

By sleeping underground for an exact prime number of years, cicadas outsmart every predator in the forest! Primes are nature's secret code—the unbreakable atomic building blocks of all numbers *([Gauss, 1809](sc6/appendix-c-formulas-and-conversions.md#cite-gauss1809); [Singh, 1997](sc6/appendix-c-formulas-and-conversions.md#cite-singh1997))*.

---

### 7.1.2 The Polyhedral Dice Maker's Secret: Why There Are Only 5 Perfect Fair Dice

Ever wonder why your favorite tabletop roleplaying games use 4, 6, 8, 12, or 20-sided dice—but nobody sells a 7-sided or 11-sided die?

Over 2,300 years ago, Greek mathematicians proved a staggering geometric fact: in our three-dimensional universe, there are **only five regular convex polyhedra** (the Platonic Solids) where every single face is an identical regular polygon and every vertex meets the exact same number of edges:
1. **Tetrahedron (d4):** 4 equilateral triangular faces
2. **Cube (d6):** 6 square faces
3. **Octahedron (d8):** 8 equilateral triangular faces
4. **Dodecahedron (d12):** 12 regular pentagonal faces
5. **Icosahedron (d20):** 20 equilateral triangular faces

If you try to make a 7-sided or 11-sided die, some sides will always be steeper or flatter than others. It is physically impossible to make them land with equal chance! True fairness in gaming isn't just about giving the dice cup a good shake—it comes from the deep spatial symmetries of the universe *([Gardner, 1959](sc6/appendix-c-formulas-and-conversions.md#cite-gardner1959); [Bruner, 1966](sc6/appendix-c-formulas-and-conversions.md#cite-bruner1966))*.

---

## 7.2 Hands-On Studio: Two-Color Counters, Polyhedral Dice & The Sieve Grid

Before we tap keys on the calculator, we roll real dice, balance counters, and build number arrays with our hands. When you understand what the numbers look like on your desk, the calculator's probability keys (`[🎲]`, `[f] [1…x]`, `[g] [t…x]`), number-theory engines (`[PRIME]`, `[g] [FACT]`, `[f] [C.FAC]`, `[GCF]`, `[f] [LCM]`, `[g] [÷R]`), statistical accumulators (`[Σ+]`, `[f] [Σ-]`, `[N]`, `[f] [Σx]`, `[Σx²]`, `[g] [x̄]`, `[f] [MED]`, `[g] [MODE]`, `[f] [MIN]`, `[g] [MAX]`, `[IQR]`, `[g] [MAD]`, `[FRQ]`), and pre-algebra keys (`[+/-]`, `[g] [|x|]`, `[x²]`, `[f] [√x]`) become your ultimate math assistants.

### 7.2.1 Concrete Probability & Number Theory Manipulatives

1. **Precision Dice & Spinner Studio:**
   - **Equal-Volume Pip Design:** Carefully sized dots for true mechanical balance across all 4 physical $d6$ dice so every face has the exact same weight.
   - **Captive Multi-Plate Spinner:** 10-sector decimal lid (`0`–`9`), plus interchangeable biased ($50\%, 25\%, 15\%, 10\%$), binary (`0`/`1`), and arithmetic operations dial plates.
   - **Digital Polyhedral Extension (`[🎲]`):** The SC-6 hardware probability engine extends physical $d6$ experiments to full polyhedral dice ($d4, d6, d8, d10, d12, d20$).
2. **Counting & Array Studio:**
   - Four high-contrast color groups modeling positive/negative integer Zero Pairs and discrete frequency histograms.
3. **Prime Factor Studio:**
   - Proportional prime factor towers ($2, 3, 5, 7$) and bilateral comparator stage.

![Probability Dice & Spinner Studio: 1x1 spinner enclosure with 10-sector lid, biased and binary dial plates, and 4 volume-equalized fair d6 dice](../assets/manuals/dice_spinner_probability.png)

### 7.2.2 The Equal-Volume Pip Dice & Spinner Studio
Standard store-bought dice often have a tiny physical imbalance because the 6-dot side has six scooped-out dots while the 1-dot side has only one!

The StackCalc kit eliminates this lopsided imbalance with our 3D-printable **Dice & Spinner Studio**. If all the dots were the same size, the 6-dot side would have 6 times as much plastic scooped out as the 1-dot side, making the 1-dot side heavier! By making the 6 dots smaller than the 1 dot, every side of the die loses the exact same tiny weight of plastic so every roll is completely fair. Meanwhile, pressing `[🎲]` on the SC-6 simulates fair $d4, d6, d8, d10, d12,$ and $d20$ polyhedral rolls.

### 7.2.3 Two-Color Integer Counters & Zero Pairs
Before you manipulate signed numbers on the SC-6 keypad, you model integers concretely using two-color tokens:
- **Yellow Token:** Represents $+1$ (a unit gain, a deposit, an upward step).
- **Crimson Token:** Represents $-1$ (a unit loss, a withdrawal, a downward step).
- **The Zero Pair:** Placing 1 Yellow token and 1 Crimson token side-by-side forms a **Zero Pair** ($+1 + (-1) = 0$).

When solving $(-5) + (+3)$, you place 5 Crimson tokens and 3 Yellow tokens on the mat. Pairing 3 Crimson tokens with the 3 Yellow tokens eliminates 3 Zero Pairs, leaving 2 Crimson tokens: $-2$. On the SC-6, you model that exact zero-pair cancellation on the stack by entering `5`, toggling its sign to `-5` on Register $Y$, and adding `3` on Register $X$ with `5 [+/-] [ENTER] 3 [+]` to land directly on $X = \mathbf{-2}$.

That physical number-line walk also explains a puzzle that mystifies many students: *"Why is $(-3) \times (-2)$ equal to $+6$? Why aren't two negatives even more negative?"* Instead of memorizing a grammar rule ("two negatives make a positive"), picture yourself walking along your Number Line:

1. **Multiplication is walking along the number line at a steady pace:**
   - $(+3) \times (+2)$: Face Forward ($+$), take 2 steps of size 3 forward $\longrightarrow +6$.
   - $(-3) \times (+2)$: Face Backward ($-$), take 2 steps of size 3 forward $\longrightarrow -6$.
2. **Multiplying by a negative means WALKING IN REVERSE:**
   - $(+3) \times (-2)$: Face Forward ($+$), take 2 steps of size 3 in REVERSE $\longrightarrow -6$.
   - $(-3) \times (-2)$: Face Backward ($-$), take 2 steps of size 3 in REVERSE. When you face backward and walk in reverse, **you move forward toward positive numbers!** $(-3) \times (-2) = +6$.

On the SC-6, staging `-3` on Register $Y$ and multiplying by `-2` on Register $X$ with `3 [+/-] [ENTER] 2 [+/-] [×]` produces $\mathbf{+6}$, letting you watch the sign toggle smoothly on the daylight LCD.

### 7.2.4 The 100-Grid Sieve of Eratosthenes
To discover prime numbers, the Greek mathematician Eratosthenes of Cyrene (c. 276–194 BC) showed a clever shortcut for finding every prime number up to 100. Because $10 \times 10 = 100$, any composite number up to 100 must have at least one factor smaller than 10! That means crossing out $1$ and the multiples of just four small primes—**2, 3, 5, and 7**—automatically uncovers all **25 primes under 100**: $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97$.

You can test each survivor candidate right on the SC-6: keying `97 [PRIME]` flashes `PRIME` on the status banner while preserving `97` on the ground shelf, whereas keying `91 [PRIME]` flashes `COMPOSITE` while preserving `91` (since $91 = 7 \times 13$). Pairing your physical sieve with the keypad makes it visually obvious why $91$ breaks into a $7 \times 13$ rectangle while $97$ stands alone as a prime.

---

## 7.3 Discrete Probability & Random Trials (`[🎲]`)

Every time you flip a coin, spin a game-board spinner, or roll a die, you are exploring **Probability**—the branch of mathematics that measures how likely something is to happen on a scale from $0$ (completely impossible) to $1$ (guaranteed to happen every time):
$$\text{Probability of an Event} = \frac{\text{Number of Winning Outcomes}}{\text{Total Number of Equally Likely Outcomes}}$$

| Probability | What It Means | Classroom Example |
| :--- | :--- | :--- |
| **$0.0$** | Impossible | Rolling a `7` on a standard 6-sided die ($d6$) |
| **$0.5$** | Equally Likely ($50/50$) | Flipping Heads or Tails on a fair coin |
| **$1.0$** | Certain | Rolling a whole number from `1` to `6` on a standard $d6$ |

### 7.3.1 The Classroom Dice Key (`[🎲]`)
What if you want to run a 60-roll probability experiment right at your desk without chasing runaway dice across the classroom floor? Pressing the dedicated dice key `[🎲]` on your SC-6 keypad turns the screen into an instant digital dice cup:
1. **Interactive Die Roll:** Each press of `[🎲]` wakes up the calculator's random number generator, animating a 3-frame rolling tumble before landing on a fair whole number from $1$ to $6$.
2. **Visual Die Rendering:** The daylight graphic LCD draws a crisp $32 \times 32$ pixel die face right in the middle of the screen with classic dot patterns.
3. **Automatic Stack Lift:** Even better, the number you rolled ($1 \dots 6$) lands directly on Register $X$ and lifts your previous numbers up the stack ($X \to Y \to Z \to T$)—so you can roll two dice and tap `[+]` to add them, or tap `[Σ+]` to log 50 rolls in a row!

| Rolled Value | 32×32 LCD Pip Geometry | Visual Dot Pattern |
| :--- | :--- | :--- |
| `[1]` | Single center pip | Unit point symmetry |
| `[2]` | Top-left & bottom-right diagonal pips | Diagonal pair |
| `[3]` | Top-left, center, & bottom-right pips | Diagonal triad |
| `[4]` | Four corner pips | $2 \times 2$ square array |
| `[5]` | Four corner pips + center pip | Quincunx ($4 + 1$) |
| `[6]` | Two vertical columns of three pips | $2 \times 3$ rectangular array |

### 7.3.2 Polyhedral Random Ranges: `[f] [1…x]` and `[g] [t…x]`
What if your game or science experiment needs a 20-sided dragon die ($d20$), a coin flip (`1` or `2`), or a random student number from `1` to `28`? Two shifted random-range keys let you build any custom spinner or die you can imagine:
- **`[f] [1…x]` (Random 1 to X):** Picks a random whole number from 1 up to whatever number is sitting on Shelf X.
  - Roll a 20-sided die ($d20$): `20 [f] [1…x]` $\longrightarrow$ picks a random whole number from 1 to 20.
  - Flip a fair coin ($1 = \text{Heads}, 2 = \text{Tails}$): `[2] [f] [1…x]` $\longrightarrow$ picks 1 or 2 with equal chance.
  - Select a random lab partner from a class of 28: `28 [f] [1…x]` $\longrightarrow$ picks a random student number from 1 to 28.
- **`[g] [t…x]` (Random Y to X):** Picks a random whole number between the starting number on Shelf Y and the ending number on Shelf X.
  - Generate a random two-digit number from 10 to 99: `10 [ENTER] 99 [g] [t…x]`.

Why doesn't a real die land on `4` *exact* once every 6 rolls? Because **Theoretical Probability** tells you what happens over thousands of rolls, while **Experimental Probability** records what actually happened in your real-life trial! Suppose you roll a standard six-sided die 60 times. On any single roll, the theoretical probability of rolling a 4 is $\frac{1}{6}$, so across 60 rolls a 4 should theoretically appear $60 \times \frac{1}{6} = 10\text{ times}$:

$$\text{Theoretical Probability of Rolling a 4} = \frac{1}{6} \approx 0.1667 \ (16.67\%)$$
$$\text{Expected Count} = 60 \times \frac{1}{6} = 10\text{ times}$$

Suppose that in your actual 60-roll experiment, you roll a 4 twelve times. Dividing your 12 wins by the 60 total rolls on the stack with `12 [ENTER] 60 [÷]` gives an experimental probability of $0.2000$ ($20.0\%$), and subtracting the theoretical $\frac{1}{6}$ share with `0.20 [ENTER] [1] [ENTER] [6] [÷] [-]` shows a $+0.0333$ ($+3.33\%$) experimental difference.

Game designers use this exact probability ratio (`Winning Outcomes ÷ Total Outcomes`) to check the fairness of every die roll and card draw before printing a rulebook. Suppose in the opening match of a tabletop tournament, a player needs to roll an odd number ($1, 3,$ or $5$) on a single six-sided equal-volume pip die from your Dice & Spinner Studio to unlock a treasure chest. Pick up one of your physical $d6$ dice and count the odd faces: 3 out of the 6 faces are odd. If you roll the die 60 times, you expect roughly 30 odd rolls. Comparing the 3 winning odd faces against all 6 faces of the cube on your SC-6 via `[3] [ENTER] [6] [÷]` yields **`0.5`**. Because half the faces of a standard cube are odd, the player's theoretical chance is an exact coin-flip ($\mathbf{0.5000}$ or $50\%$).

Now move from the dice table over to the championship card arena, where a finalist needs to draw an Ace on the very first card pulled from a freshly shuffled 52-card deck. Since there are 4 suits (hearts, diamonds, clubs, and spades), there are 4 Aces hiding among the 52 cards. Dividing the 4 Aces by the 52-card deck on the stack with `[4] [ENTER] 52 [÷]` produces **`0.0769230769`**. Because every suit holds 1 Ace out of 13 ranks ($4/52 = 1/13$), the opening-draw probability is $\mathbf{0.0769}$ ($\approx 7.69\%$)—rare enough to make the whole crowd gasp when an Ace turns over on the first draw!

---

### 7.3.3 Compound Probability: Rolling Two Dice (36 Outcomes)
Here is a classic board-game mystery: when you roll **two** six-sided dice and add them together, the possible totals run from $2$ all the way to $12$. Are all eleven sums equally likely? Not even close!

Imagine painting the first die **Red** and the second die **Blue**. Because each of the 6 faces on the Red die can pair up with any of the 6 faces on the Blue die, there are $6 \times 6 = \mathbf{36\text{ equally likely pairs}}$ of *(Red Die, Blue Die)*. Look at what happens when we list all 36 pairs by their sum:
- To roll a **$2$** ("snake eyes"), both dice *must* land on $1$: $(1,1)$. There is **only 1 way** out of 36!
- To roll a **$12$** ("boxcars"), both dice *must* land on $6$: $(6,6)$. Again, **only 1 way** out of 36!
- Now look at **$7$**: if the Red die lands on *anything at all*—$1, 2, 3, 4, 5,$ or $6$—there is an exact partner on the Blue die that makes $7$: $(1,6), (2,5), (3,4), (4,3), (5,2),$ and $(6,1)$. There are **6 different ways** to roll a $7$—making **$7$** the tallest bar in the center of the rooftop pyramid!

![Probability Dice & Spinner Studio: Independent 2d6 Pairs (36-Outcome Sample Space) with 10-Sector Hub and Operations Dial](../assets/manuals/dice_spinner_d20_and_polyhedra.png)

| Dice Sum | Winning Pairs *(First Die, Second Die)* | Count | Probability of Sum |
| :---: | :--- | :---: | :---: |
| **$2$** | $(1,1)$ | $1$ | $1/36$ |
| **$3$** | $(1,2), (2,1)$ | $2$ | $2/36 = 1/18$ |
| **$4$** | $(1,3), (2,2), (3,1)$ | $3$ | $3/36 = 1/12$ |
| **$5$** | $(1,4), (2,3), (3,2), (4,1)$ | $4$ | $4/36 = 1/9$ |
| **$6$** | $(1,5), (2,4), (3,3), (4,2), (5,1)$ | $5$ | $5/36$ |
| **$7$** | $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$ | **$6$** | **$6/36 = 1/6$** |
| **$8$** | $(2,6), (3,5), (4,4), (5,3), (6,2)$ | $5$ | $5/36$ |
| **$9$** | $(3,6), (4,5), (5,4), (6,3)$ | $4$ | $4/36 = 1/9$ |
| **$10$** | $(4,6), (5,5), (6,4)$ | $3$ | $3/36 = 1/12$ |
| **$11$** | $(5,6), (6,5)$ | $2$ | $2/36 = 1/18$ |
| **$12$** | $(6,6)$ | $1$ | $1/36$ |
| **Total** | **All $6 \times 6$ Outcomes** | **$36$** | **$36/36 = 1.00$** |

Why do board-game designers put the robber or the most frequent resource on **$7$** when you throw two $d6$ dice from your **Polyhedral Dice** kit? You can build a physical 2-dice rooftop pyramid by docking **Counting Tiles** along your Snapfinity lid—one tile ($7.0\text{ mm}$) for each *(First Die, Second Die)* pair in the table above:
- Sums **$2$** and **$12$** get only **1 tile** ($7.0\text{ mm}$ tall), because there is only one way to roll snake-eyes $(1,1)$ or boxcars $(6,6)$.
- Sums **$3$** and **$11$** stand **2 tiles** ($14.0\text{ mm}$) tall; **$4$** and **$10$** stand **3 tiles** ($21.0\text{ mm}$) tall; **$5$** and **$9$** stand **4 tiles** ($28.0\text{ mm}$) tall; **$6$** and **$8$** stand **5 tiles** ($35.0\text{ mm}$) tall.
- Right in the center, **Lucky $7$** towers **6 tiles ($42.0\text{ mm}$) tall** because every possible number on the first die ($1$ through $6$) has an exact partner on the second die ($(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$) that adds to $7$.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | `. 6 . 36 [g] [SIMP]` | 0 | 0 | 0 | **1/6** | 6 ways out of 36 simplifies by their $\text{GCF} = 6$ to **$\frac{1}{6}$** |
| 2 | `[FDISP]` | 0 | 0 | 0 | **0.1667** | Toggle fraction/decimal view: $\frac{1}{6} \approx \mathbf{16.67\%}$ |

The probability of rolling a sum of $7$ is **$1/6 \approx 16.67\%$**—six times more likely than rolling a $2$ or a $12$.

What if you pair two different random tools together—like flipping **Heads** on a fair coin ($\frac{1}{2}$) *and* rolling a **$6$** on a six-sided die ($\frac{1}{6}$) on the same turn? Because the coin and the die don't affect each other (mathematicians call them **independent events**), their $2 \times 6$ outcome grid has $12$ equally likely pairs, and only $1$ of those $12$ pairs is *(Heads, 6)*. Multiplying the two independent chances on the stack via `[1] [ENTER] [2] [÷] [1] [ENTER] [6] [÷] [×]` yields **`0.0833333333`**, giving a combined chance of $\text{Chance of Heads} \times \text{Chance of 6} = 1/12 \approx \mathbf{8.33\%}$.

### 7.3.4 Probability Trees & Sampling Without Replacement
What happens when you pull a marble out of a bag (or deal a card from a deck) and **keep it in your hand** instead of tossing it back in? Now the bag has *one fewer marble* inside, so the odds on your second draw change!

| First Draw Outcome ($8$ Marbles) | Second Draw Outcome ($7$ Remaining) | Combined Branch Probability |
| :--- | :--- | :---: |
| **Red 1st ($5/8$)** | Red 2nd ($4/7$) | $\frac{5}{8} \times \frac{4}{7} = \frac{20}{56}$ |
| **Red 1st ($5/8$)** | Blue 2nd ($3/7$) | $\frac{5}{8} \times \frac{3}{7} = \frac{15}{56}$ |
| **Blue 1st ($3/8$)** | Red 2nd ($5/7$) | $\frac{3}{8} \times \frac{5}{7} = \frac{15}{56}$ |
| **Blue 1st ($3/8$)** | **Blue 2nd ($2/7$)** | $\frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \mathbf{\frac{3}{28}}$ |

Suppose you reach into a cloth bag containing 5 Red and 3 Blue marbles ($8$ marbles in all) and draw two marbles without looking and without putting the first marble back. What is the chance of drawing two Blue marbles in a row? On your first reach, $3$ out of $8$ marbles are Blue ($\frac{3}{8}$). Once you hold that Blue marble in your hand, only $2$ Blue marbles remain among the $7$ marbles left in the bag ($\frac{2}{7}$)! Multiply the two step chances together:
$$\text{Chance of Both Blue} = \text{Chance of 1st Blue} \times \text{Chance of 2nd Blue} = \frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \frac{3}{28}$$

On the stack, compute the first draw probability $\frac{3}{8}$ on Register $Y$, compute the second draw probability $\frac{2}{7}$ on Register $X$, and multiply them with `[3] [ENTER] [8] [÷] [2] [ENTER] [7] [÷] [×]` to obtain $0.107143$. Tapping `[FDISP]` switches to exact fraction view ($\mathbf{3/28}$), showing that the probability of drawing two blue marbles in a row is $3/28 \approx \mathbf{10.71\%}$.

What if someone asks for the chance of drawing **at least one Red marble** in those two picks? Instead of adding up three different branches (Red-Red, Red-Blue, and Blue-Red), use the **Complement Shortcut**: notice that the *only* way to fail is to draw **Both Blue** ($\frac{3}{28}$)! Subtracting the chance of Both Blue from $1$ ($100\%$) gives the answer in one step:
$$\text{Chance of At Least One Red} = 1 - \text{Chance of Both Blue} = 1 - \frac{3}{28} = \frac{25}{28}$$

Place `1` ($100\%$) onto Register $Y$, divide `3` by `28` on Register $X$, and subtract with `[1] [ENTER] [3] [ENTER] 28 [÷] [-]` to reach $0.892857$—and one tap of `[FDISP]` reveals the exact fraction $\mathbf{25/28}$ ($\approx \mathbf{89.29\%}$).

That same without-replacement rule explains why drawing **two Aces in a row** from a 52-card deck is such a rare thrill! On the first draw, $4$ of the $52$ cards are Aces ($4/52$). Once you hold that first Ace in your hand, only **$3$ Aces** remain among the **$51$ cards** left in the deck ($3/51$). Multiplying the two dependent step chances on the stack with `[4] [ENTER] 52 [÷] [3] [ENTER] 51 [÷] [×]` gives **`0.0045248869`**—a combined probability of $1/221 \approx \mathbf{0.45\%}$, happening only once in every 221 two-card deals!

---

## 7.4 Number Theory: Primes, Factors & The Secret Partner Rule

Now let's return to the 17-year cicada mystery from the start of our chapter. Why are prime numbers like $2, 3, 5, 7, 11, 13,$ and $17$ so special? Just as every molecule in chemistry is built out of atoms, **every whole number greater than 1 is built by multiplying a unique team of prime numbers together**!

| Tool | Format | What You Build & See | How It Connects to Your SC-6 |
| :--- | :--- | :--- | :--- |
| **Hands-On Blocks** | Physical Manipulatives | • **24-Tile Array Test:** Primes form only $1 \times \text{Number}$ straight lines; composites form 2D matrices. • **Prime Factor Studio:** Proportional prime towers where stacking prime blocks physically multiplies their values. • Height(2) + Height(3) = Height(6) on the comparator stage. | Physical verification before keystrokes |
| **Visual Screen** | Graphic Sandboxes | • Screen Factor Tree View: exponents and prime dots ($2^3 \times 3^2 \times 5$). • Dual Frame Counter `[▦]`. • Interactive LCD Sieve: survivor primes highlighted on display. | Daylight LCD dot matrix |
| **Number Stack** | RPN Symbolic Engines | • `[PRIME]` test flashes `PRIME` or `COMPOSITE` on the graphic status line, preserving the number on $X$. • `[g] [FACT]` displays prime factorization string. • `[GCF]` and `[f] [LCM]` execute Euclidean and Duality engines. | Stack execution ($T, Z, Y, X$) |

### 7.4.1 The Rectangular Array Primality Test
How can you tell with your bare hands whether a number is **prime** or **composite**? Grab a handful of **Counting Tiles** from your 24-Tile Studio and try to arrange them into a neat rectangle with at least 2 rows!

| Number Classification | Tile Count | Complete Rectangular Factor Arrays | Positive Divisors |
| :--- | :--- | :--- | :--- |
| **Composite (12 Tiles)** | 12 Tiles | $1 \times 12$, $2 \times 6$, and $3 \times 4$ complete rectangles | `1, 2, 3, 4, 6, 12` (6 factors) |
| **Prime (13 Tiles)** | 13 Tiles | Rows of 2, 3, or 4 always leave 1 leftover tile; only $1 \times 13$ forms a rectangle | `1, 13` (2 factors only) |

> **Why Prime Numbers Cannot Form Rectangles:** Take 12 counting tiles from your kit: you can arrange them into a neat $2 \times 6$ rectangle or a $3 \times 4$ rectangle with zero leftovers. Now add one more tile to make 13 and try building a rectangle 2, 3, or 4 tiles wide. Every attempt leaves an extra tile sticking out! The only rectangle 13 tiles can form is a single skinny $1 \times 13$ line. That is the geometric meaning of a prime number: it cannot be factored into two dimensions greater than 1.

Walking through $12$ and $13$ on the keypad shows how `[PRIME]` tests each number in place without disturbing the rest of the stack:

| Keystroke | Register T | Register Z | Register Y | Register X | Status / Screen |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `12` | 0 | 0 | 0 | 12 | Number entered |
| `[PRIME]` | 0 | 0 | 0 | 12 | Flashes `COMPOSITE` |
| `13` | 0 | 0 | 12 | 13 | Stack lifts; 13 entered |
| `[PRIME]` | 0 | 0 | 12 | 13 | Flashes `PRIME` |

---

### 7.4.2 The Four-Color Sieve of Eratosthenes (24-Tile Kit & 144-Tile Classroom Pool)
With your individual 24-tile kit, you can build a $4 \times 6$ grid to hunt down all 9 primes up to 24—or pool 6 student kits across a classroom table ($6 \times 24 = 144$ tiles: 36 each of Archival White, Cobalt Blue, Radiant Gold, and Slate Gray) to build a giant $12 \times 12$ sieve and uncover all 34 primes up to 144!

- **Step 1:** Tile 1 (White) is set aside. 1 is a unit (neither prime nor composite).
- **Step 2: Prime 2 (Blue).** Replace every even multiple $\ge 4$ with Blue tiles ($4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, \dots$).
- **Step 3: Prime 3 (Gold).** Replace uncolored multiples of 3 with Gold tiles ($9, 15, 21, 27, 33, 39, 45, 51, 57, 63, \dots$).
- **Step 4: Primes 5 & 7 (White/Pattern).** In the 6-kit classroom pool, replace remaining multiples of 5 and 7 ($25, 35, 49, 55, 65, 77, 85, 91, 95, 115, 119, 121, 125, \dots$).
- **Step 5: Prime Survivors (Slate Gray).** In a single 24-tile kit, the 9 survivor tiles are **$2, 3, 5, 7, 11, 13, 17, 19, 23$**. Across a 6-kit classroom pool ($144$ tiles), all 34 primes $\le 144$ survive:  
  $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139$.

Notice how the eighties end with two true prime survivors—**$83$** and **$89$**—whereas the nineties and early hundreds hide sneaky "impostor primes" that look prime at first glance because they are odd and don't end in $5$, yet are secret multiples of $7$! For example, testing $91$ (`91 [PRIME]`) flashes `COMPOSITE` ($91 = 7 \times 13$) while neighbor prime $89$ (or `97 [PRIME]`) flashes `PRIME`, and beyond 100, testing $119$ (`119 [PRIME]`) unmasks another multiple of $7$ ($119 = 7 \times 17$) while `137 [PRIME]` confirms `PRIME`. Whenever any candidate flashes `COMPOSITE`, simply tap `[g] [FACT]` right afterward to unmask its hidden prime factors on the LCD!

---

### 7.4.3 The Prime Tower Scale: Multiplying by Stacking Blocks
Normally, stacking two blocks *adds* their heights together. Could we design special blocks where stacking two blocks on top of each other **multiplies** their numbers instead?

That is the magic of your **Prime Factor Studio**! The back wall of the studio has a special ruler scale numbered from $1$ to $100$ where the marks get closer together as you climb higher (every time a number doubles—$2, 4, 8, 16, 32$—it steps up by the exact same $7.00\text{ mm}$ height!). Each prime block is 3D-printed to match that scale:
- **Prime 2 (Blue):** $7.00\text{ mm}$ ($1\text{U}$)
- **Prime 3 (Amber/Green):** $11.09\text{ mm}$
- **Prime 5 (Yellow):** $16.25\text{ mm}$
- **Prime 7 (Red):** $19.65\text{ mm}$

Because the ruler scale is spaced by multiplication steps, **adding block heights on the stage automatically multiplies their numbers**!

![Prime Factor Studio: Bilateral Comparator Stage & Prime Factor Blocks](../assets/manuals/prime_studio_comparator_stage.png)

Try stacking your Prime Blocks right on the comparator stage to watch height addition turn into multiplication:
1. **Multiplying $2 \times 3 = 6$:**
   Place Blue Block `[2]` on the desk. Stack Amber/Green Block `[3]` on top:
   $$\text{Height of 2-Block} + \text{Height of 3-Block} = 7.00\text{ mm} + 11.09\text{ mm} = \mathbf{18.09\text{ mm}}$$
   The top of the stack aligns **EXACTLY with the "6" tick mark on the comparator!**
2. **Multiplying $2 \times 5 = 10$:**
   Stack Blue Block `[2]` and Yellow Block `[5]`:
   $$\text{Height of 2-Block} + \text{Height of 5-Block} = 7.00\text{ mm} + 16.25\text{ mm} = \mathbf{23.25\text{ mm}}$$
   Lands precisely on the major line labeled **"10"**.
3. **Decomposing $60 = 2 \times 2 \times 3 \times 5$:**
   Stack two `[2]` blocks, one `[3]` block, and one `[5]` block so that stacking the blocks adds their heights ($7.00 + 7.00 + 11.09 + 16.25 = 41.34\text{ mm}$) to match multiplying their numbers ($2 \times 2 \times 3 \times 5 = 60$):
   $$7.00\text{ mm} + 7.00\text{ mm} + 11.09\text{ mm} + 16.25\text{ mm} = \mathbf{41.34\text{ mm}}$$
   Points squarely at the **"60"** line on the rear wall!
4. **Why Order Doesn't Change the Height:**
   Reorder the stack: put Yellow `[5]` on the bottom, then `[3]`, then both `[2]`s.
   The total height stays the exact same (**$41.34\text{ mm}$**, matching $5 \times 3 \times 2 \times 2 = 60$). Multiplication is commutative—no matter what order you stack the blocks, the tower height never changes.

![Prime Studio Commutativity Proof: 2x5 = 5x2 = 10 Exact Flush Alignment](../assets/manuals/prime_studio_commutativity.png)

Now compare your physical block tower to the screen! Keying `60 [g] [FACT]` on the SC-6 decomposes `60` directly into its prime factor tree (`2 × 2 × 3 × 5`), matching your four stacked blocks block-for-block:

![SC-6 Prime Factorization Mode: 60 = 2 x 2 x 3 x 5](../assets/manuals/screenshots/sc6_prime_factors_mode.png)

| Keystroke | Register T | Register Z | Register Y | Register X | Status / Screen |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `60` | 0 | 0 | 0 | 60 | Number entered |
| `[g] [FACT]` | 0 | 0 | 0 | 60 | Displays `2² × 3 × 5` |

---

### 7.4.4 The Primality Testing Engine (`[PRIME]`)
A prime number is a whole number greater than 1 whose only factors are 1 and itself. On the SC-6, pressing the primary key `[PRIME]` tests the number sitting on Register $X$ in a flash:
- Momentarily flashes `PRIME` or `COMPOSITE` on the graphic status line.
- Preserves Register $X$ intact so you can immediately continue calculations with your candidate number.
- If the number is $1$ or less (or has a decimal part), flashes `INVALID DATA` (or `NEITHER` for 0 and 1).

| Keystroke | Register T | Register Z | Register Y | Register X | Status / Screen |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `97` | 0 | 0 | 0 | 97 | Number entered |
| `[PRIME]` | 0 | 0 | 0 | 97 | Flashes `PRIME` |
| `119` | 0 | 0 | 97 | 119 | Stack lifts; 119 entered |
| `[PRIME]` | 0 | 0 | 97 | 119 | Flashes `COMPOSITE` |
| `2` | 0 | 97 | 119 | 2 | Stack lifts; 2 entered |
| `[PRIME]` | 0 | 97 | 119 | 2 | Flashes `PRIME` |

Because `[PRIME]` leaves the number sitting untouched on Register $X$, you can test large candidates and immediately use them in multi-step number puzzles! Suppose an adventure quest's stone gate opens only if the code carved into the bronze key—**`83`** (`83 [PRIME]`)—is an unbreakable prime number. Remember how 13 Counting Tiles refuse to form any rectangle of 2, 3, or 4 rows without leaving a tile sticking out? Testing candidate 83 with the hardware primality key via `83 [PRIME]` confirms **`83`**: because $9 \times 9 = 81$ and none of the primes below 9 ($2, 3, 5,$ or $7$) divide evenly into 83, the status line flashes `PRIME` and preserves $\mathbf{83}$ in Register $X$.

Better yet, because `[PRIME]` preserves each number on the stack, you can test two primes in a row and immediately add them together! For example, two prime numbers that sit just $2$ steps apart on the number line—like $(11, 13)$ or $(17, 19)$—are called **Twin Primes** (because the even number sandwiched between them is always divisible by $2$!). Let's use `[PRIME]` to verify that **$29$** and **$31$** are both prime, and then add them together on the stack via `29 [PRIME] 31 [PRIME] [+]` to reach **`60`**. Both candidates flash `PRIME` on the daylight LCD and sum to $\mathbf{60}$—a multiple of 12, which is true for every twin prime pair greater than $(3, 5)$!

You can also use `[PRIME]` to test a famous 300-year-old mathematical puzzle from the year 1742! That year, Christian Goldbach wrote a letter to Leonhard Euler with a bold guess: *Every even whole number greater than 2 can be built by adding two prime numbers together!* ($4 = 2+2$, $6 = 3+3$, $8 = 3+5$, $10 = 3+7\dots$). Even with modern supercomputers, no one has ever found an even number that breaks Goldbach's rule! Let's test the even number **$28$** by checking whether **$11$** and **$17$** are both prime and add up to $28$ using `11 [PRIME] 17 [PRIME] [+] 11 [ENTER] 17 [+]`, which confirms **`28`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `11` | $0.0000$ | $0.0000$ | $0.0000$ | $11.0000$ | Key in first prime candidate 11 |
| `[PRIME]` | $0.0000$ | $0.0000$ | $0.0000$ | $11.0000$ | LCD flashes `PRIME`; preserves 11 in Register $X$ |
| `17` | $0.0000$ | $0.0000$ | $11.0000$ | $17.0000$ | Key in second candidate 17; stack lifts 11 to $Y$ |
| `[PRIME]` | $0.0000$ | $0.0000$ | $11.0000$ | $17.0000$ | LCD flashes `PRIME`; preserves 17 in Register $X$ |
| `[+]` | $0.0000$ | $0.0000$ | $0.0000$ | $28.0000$ | Sum primes $11 + 17 = 28$; stack drops |
| `11` | $0.0000$ | $0.0000$ | $28.0000$ | $11.0000$ | Key in 11 for second partition check; stack lifts 28 to $Y$ |
| `[ENTER]` | $0.0000$ | $28.0000$ | $11.0000$ | $11.0000$ | Push 11 to $Y$; lifts 28 to $Z$ (stack lift disabled) |
| `17` | $0.0000$ | $28.0000$ | $11.0000$ | $17.0000$ | Key in 17; overwrites $X$ since `ENTER` disabled lift |
| `[+]` | $0.0000$ | $0.0000$ | $28.0000$ | $28.0000$ | Sum $11 + 17 = 28$; stack drops, preserving first sum in $Y$ |

Register $X$ displays $28$ and Register $Y$ preserves $28$—Goldbach's Conjecture holds true for $28$!

---

### 7.4.5 Prime Factor Decomposition Engine (`[g] [FACT]`)
Whenever `[PRIME]` tells you a number is `COMPOSITE`, you naturally want to know: *Which prime blocks multiply together to build it?* Pressing `[g] [FACT]` (`[g]` + `[PRIME]`) breaks any whole number $\ge 2$ into its prime factor tree, showing exponents and multiplication dots:
- Enter $12$: `12` `[g] [FACT]` $\longrightarrow$ Displays: **`2² × 3`**
- Enter $360$: `360` `[g] [FACT]` $\longrightarrow$ Displays: **`2³ × 3² × 5`**
- Enter $2,639$: `2639` `[g] [FACT]` $\longrightarrow$ Displays: **`7 × 13 × 29`**

| Keystroke | Register T | Register Z | Register Y | Register X | Status / Screen |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `360` | 0 | 0 | 0 | 360 | Number entered |
| `[g] [FACT]` | 0 | 0 | 0 | 360 | Displays `2³ × 3² × 5` |

---

### 7.4.6 Hardware `[GCF]` and `[f] [LCM]` Keys & Tactile Block Intersections

In Chapter 05, you met the `[GCF]` and `[f] [LCM]` keys as fast tools for simplifying fractions and finding Least Common Denominators. Now we can look under the hood with our **Prime Factor Blocks** to see *why* GCF and LCM are secret partners:
- **Primary Key `[GCF]`:** Finds the **Greatest Common Factor** of Shelf $Y$ and Shelf $X$ (e.g., `12 [ENTER] 18 [GCF]` $\longrightarrow$ `6`).
- Keying `12` `[ENTER]` stages the first number $12$ onto Floor $Y$ ($Y = 12$), and keying `18` `[GCF]` places $18$ on Floor $X$ ($X = 18$) and finds the Greatest Common Factor of $12$ and $18$, which is $6$ ($X = 6$).
- **Shifted Key `[f] [LCM]`:** Finds the **Least Common Multiple** of Shelf $Y$ and Shelf $X$ (e.g., `12 [ENTER] 18 [f] [LCM]` $\longrightarrow$ `36`).
- **Why Songbird Brains Pack More Neurons per Gram:** Why can a tiny songbird learn hundreds of complex melodies? Because songbird brains pack $140\text{ million}$ neurons into a single gram of tissue. Tapping `140 [g] [FACT]` breaks $140$ into its prime building blocks: **`2² × 5 × 7`**.

You can see how GCF and LCM share their prime blocks by drawing a **Two-Circle Prime Factor Venn Diagram** on your desk for the numbers **$48$** and **$72$**:
- Break down $48 = 2 \times 2 \times 2 \times 2 \times 3$: Assemble four `[2]` blocks and one `[3]` block.
- Break down $72 = 2 \times 2 \times 2 \times 3 \times 3$: Assemble three `[2]` blocks and two `[3]` blocks.
- **Center Overlap ($\text{GCF}$):** Slide every matching pair of prime blocks that both numbers share (**three `[2]`s and one `[3]`**) into the **Center Overlap**. Multiplying the center blocks (or keying `48 [ENTER] 72 [GCF]` on the stack) gives the Greatest Common Factor:
  $$\text{GCF} = 2 \times 2 \times 2 \times 3 = 8 \times 3 = \mathbf{24}$$
- **All Three Regions Combined ($\text{LCM}$):** Place the leftover unshared blocks in the outer crescents (one extra `[2]` on the Left for $48$; one extra `[3]` on the Right for $72$). Multiplying **all blocks across all three regions** (Left $\times$ Center $\times$ Right) gives the Least Common Multiple:
  $$\text{LCM} = 2 \times 24 \times 3 = 16 \times 9 = \mathbf{144}$$

![Prime Factor Studio: Prime Factorization and Venn Intersection Model](../assets/manuals/prime_lcm_gcd_venn.png)

Why do mechanical engineers care about both GCF and LCM when two gears mesh together? Imagine a **$14\text{-tooth}$ driver gear** ($14 = 2 \times 7$) clicking tooth-for-tooth against a **$21\text{-tooth}$ driven gear** ($21 = 3 \times 7$), with two chalk-marked teeth touching at the start:
- **GCF is the Largest Equal Tooth Group:** Keying `14 [ENTER] 21 [GCF]` gives **`7`**—meaning you can paint both gears in equal color-coded groups of **$7$ teeth** ($2$ groups on the small gear, $3$ groups on the big gear).
- **LCM is When the Marked Teeth Meet Again:** Keying `14 [ENTER] 21 [f] [LCM]` gives **`42`**—meaning exactly **$42$ teeth** must click past the mesh point ($42 \div 14 = 3$ spins of the small gear and $42 \div 21 = 2$ spins of the big gear) before the two chalk-marked teeth touch again!

Once you see how `[GCF]` finds the largest shared building block and `[f] [LCM]` finds the first shared meeting point, three everyday puzzles snap into focus:
- **Rectangle Tiling (`[GCF]`):** Suppose a maker lab needs to tile a tabletop measuring $24\text{ cm} \times 36\text{ cm}$ using the largest possible square tiles with zero waste or cutting. Keying `24 [ENTER] 36 [GCF]` $\to 12$ immediately reveals that the largest square tile side is the $\text{GCF of } 24\text{ and } 36 = \mathbf{12\text{ cm}}$.
- **Synchronized Flashing Cycles (`[f] [LCM]`):** Suppose two signal lights flash at steady intervals—Light A every $6\text{ seconds}$ and Light B every $8\text{ seconds}$. Keying `6 [ENTER] 8 [f] [LCM]` $\to 24$ confirms that the signal lights flash together every $\text{LCM of } 6\text{ and } 8 = \mathbf{24\text{ seconds}}$.
- **Fraction Least Common Denominator (`[f] [LCM]`):** When adding unlike fractions $\frac{3}{8} + \frac{5}{12}$, the Least Common Denominator is simply the LCM of the denominators. Keying `8 [ENTER] 12 [f] [LCM]` $\to 24$ gives the exact common denominator $\text{LCM of } 8\text{ and } 12 = \mathbf{24}$ in a single keystroke.

---

### 7.4.7 The Secret Partner Rule: Why GCF × LCM Always Equals First Number × Second Number
Look back at the two-circle Venn diagram you built for $48$ and $72$. When we found the **GCF** ($24$), we multiplied the shared prime blocks in the center overlap. When we found the **LCM** ($144$), we multiplied the left crescent, the center overlap, and the right crescent. Notice that if you multiply **$\text{GCF} \times \text{LCM}$**, the center overlap gets counted *twice*—which uses the exact same collection of prime blocks as multiplying the two original numbers together!
$$\text{GCF} \times \text{LCM} = \text{First Number} \times \text{Second Number}$$

Let's check the Secret Partner Rule on the stack using the numbers **$24$** and **$36$**:
- **$\text{GCF of } 24\text{ and } 36$** $= 12$
- **$\text{LCM of } 24\text{ and } 36$** $= 72$
- **$\text{GCF} \times \text{LCM}$:** $12 \times 72 = 864$
- **$\text{First Number} \times \text{Second Number}$:** $24 \times 36 = 864$

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `24` | 0 | 0 | 0 | 24 |
| `[ENTER]` | 0 | 0 | 24 | 24 |
| `36` | 0 | 0 | 24 | 36 |
| `[f] [LCM]` | 0 | 0 | 0 | 72 |
| `12` | 0 | 0 | 72 | 12 |
| `[×]` | 0 | 0 | 0 | 864 |

Check against direct multiplication on the stack by keying `24 [ENTER] 36 [×]` to reach $X = \mathbf{864.00}$, confirming the Secret Partner Rule!

Let's also watch how `[GCF]` and `[f] [LCM]` chain together in a single continuous stack sequence when two interlocking stone gears with **$18$ teeth** and **$24$ teeth** mesh inside a clockwork mechanism (and if you ever want to inspect every shared divisor of two gear wheels at once, the shifted common-factors key `[f] [C.FAC]` lists them on the screen). Multiplying their Greatest Common Factor ($\text{GCF} = 6$) by their Least Common Multiple ($\text{LCM} = 72$) must equal $18 \times 24 = 432$! Chaining both keys on the stack with `18 [ENTER] 24 [GCF] 18 [ENTER] 24 [f] [LCM] [×]` lands on **`432`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `18` | $0.0000$ | $0.0000$ | $0.0000$ | $18.0000$ | Key in first fortress number 18 |
| `[ENTER]` | $0.0000$ | $0.0000$ | $18.0000$ | $18.0000$ | Stack lifts; 18 locked into Register $Y$ |
| `24` | $0.0000$ | $0.0000$ | $18.0000$ | $24.0000$ | Key in second number 24 |
| `[GCF]` | $0.0000$ | $0.0000$ | $0.0000$ | $6.0000$ | Compute Greatest Common Factor of 18 and 24 ($6$) |
| `18` | $0.0000$ | $0.0000$ | $6.0000$ | $18.0000$ | Key in first number 18; GCF lifts to Register $Y$ |
| `[ENTER]` | $0.0000$ | $6.0000$ | $18.0000$ | $18.0000$ | Stack lifts; 18 locked into Register $Y$, 6 into Register $Z$ |
| `24` | $0.0000$ | $6.0000$ | $18.0000$ | $24.0000$ | Key in second number 24 |
| `[f] [LCM]` | $0.0000$ | $0.0000$ | $6.0000$ | $72.0000$ | Compute Least Common Multiple of 18 and 24 ($72$); GCF stays in Register $Y$ |
| `[×]` | $0.0000$ | $0.0000$ | $0.0000$ | $432.0000$ | Multiply GCF by LCM ($6 \times 72 = 432$) |

The Secret Partner Rule holds identically ($18 \times 24 = 432$)! *(Pro tip: Since `[GCF]` saves `24` in `[f] [LASTX]`, you can also replace `18 [ENTER] 24 [f] [LCM]` with `18 [f] [LASTX] [f] [LCM]`.)*

---

### 7.4.8 The Remainder-Step Ladder (Euclidean Division) via Hardware `[g] [÷R]`
How does the SC-6 find the Greatest Common Factor of two huge numbers without testing hundreds of prime factors? Over 2,300 years ago, Euclid of Alexandria discovered a brilliant visual shortcut—and you can see *why* it works by **tiling a rectangular hallway with the largest possible square floor tiles**:

Imagine a rectangular hallway that is **$105\text{ cm}$ long** and **$45\text{ cm}$ wide**. We want to find the largest square tile that tiles the whole hallway evenly:
1. First, lay down big **$45\text{ cm} \times 45\text{ cm}$ squares** along the $105\text{ cm}$ hallway. Two of those $45\text{ cm}$ squares fit side by side ($2 \times 45 = 90\text{ cm}$), leaving an unfilled rectangular gap at the end that measures **$45\text{ cm}$ by $15\text{ cm}$** (because $105 \div 45 = 2$ with a **remainder of $15$**)!
2. Any square tile that tiles the whole hallway *must also* tile that leftover **$45\text{ cm} \times 15\text{ cm}$** gap!
3. Now tile the $45\text{ cm} \times 15\text{ cm}$ gap with **$15\text{ cm} \times 15\text{ cm}$ squares**: exactly three $15\text{ cm}$ squares fit with **remainder $0$** ($45 \div 15 = 3$, remainder $0$)! Because $15\text{ cm}$ squares tile the gap with zero leftover space, they also tile the $45\text{ cm}$ squares—and the entire $105\text{ cm} \times 45\text{ cm}$ hallway!

$$\text{GCF of Big and Small} = \text{GCF of Small and Remainder}$$

On the SC-6, you can climb this remainder ladder using the shifted key `[g] [÷R]`. Each press of `[g] [÷R]` divides $Y$ by $X$, placing the whole-number quotient in Register $X$ and the remainder in Register $Y$—while automatically saving the divisor you just used inside `[f] [LASTX]`.

Let's run our $105\text{ cm} \times 45\text{ cm}$ hallway tiling puzzle on the stack using `[g] [÷R]`:
1. $105 \div 45 = 2$ with remainder $15$, so the **GCF of 105 and 45** is the same as the **GCF of 45 and 15**.
2. $45 \div 15 = 3$ with remainder $0$, which means $15\text{ cm}$ square tiles fit evenly with zero waste!
The last non-zero remainder is **15**, so the **GCF of 105 and 45** is $\mathbf{15}$.

| Keystroke | Register T | Register Z | Register Y | Register X | Status / Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `105` | 0 | 0 | 0 | 105 | Dividend entered |
| `[ENTER]` | 0 | 0 | 105 | 105 | Stack lifts; 105 staged to $Y$ |
| `45` | 0 | 0 | 105 | 45 | Divisor 45 entered on floor $X$ |
| `[g] [÷R]` | 0 | 0 | 15 | 2 | Integer quotient $Q = 2$ in $X$, remainder $R = 15$ in $Y$ (`LASTX` saves 45) |
| `[x⇄y]` | 0 | 0 | 2 | 15 | Swap: remainder 15 now in $X$ |

For even larger hallways or courtyards—like a $252\text{ cm}$ by $105\text{ cm}$ stone courtyard—you can keep stepping from the old width to the new remainder using `[f] [LASTX]` and `[g] [÷R]` until the remainder hits zero, without ever re-typing a divisor. What is the largest square paver that tiles a $252\text{ cm} \times 105\text{ cm}$ courtyard with zero cutting?
1. Two $105 \times 105$ squares fit inside $252$, leaving a remainder strip of $42$ ($252 \div 105 = 2$, remainder $42$).
2. Two $42 \times 42$ squares fit inside $105$, leaving a remainder strip of $21$ ($105 \div 42 = 2$, remainder $21$).
3. Two $21 \times 21$ squares fit inside $42$ with **zero remainder** ($42 \div 21 = 2$, remainder $0$)!
The last non-zero remainder is **21**, so the **GCF of 252 and 105** is $\mathbf{21}$.

| Step / Key | Dividend (Y) | Divisor (X) | Quotient (X) | Remainder (Y) |
| :--- | :--- | :--- | :--- | :--- |
| 252 `[ENTER]` 105 | 252 | 105 | - | - |
| `[g] [÷R]` | - | - | 2 | 42 |
| `[x⇄y]` | 2 | 42 | 42 | 2 |
| `[f] [LASTX]` `[x⇄y]` | 105 | 42 | - | - |
| `[g] [÷R]` | - | - | 2 | 21 |
| `[x⇄y]` `[f] [LASTX]` `[x⇄y]` | 42 | 21 | - | - |
| `[g] [÷R]` | - | - | 2 | 0 |

> **The `[f] [LASTX]` Conveyor Belt in Remainder Ladders & Secret Partner Checks:** Why didn't we have to type `105` or `42` a second time in the table above? Because every time you press `[g] [÷R]`, `[GCF]`, or `[f] [LCM]`, the SC-6 automatically tucks the divisor from Register $X$ into `[f] [LASTX]`. In a remainder ladder, the previous step's divisor becomes the next step's starting number—so tapping `[x⇄y] [f] [LASTX] [x⇄y] [g] [÷R]` pulls the old divisor straight out of `LASTX` and divides it by the new remainder. And when you test the Secret Partner Rule on two numbers like 24 and 36, computing `24 [ENTER] 36 [GCF]` leaves `36` waiting in `LASTX`, so you only need `24 [f] [LASTX] [f] [LCM] [×]` to finish the proof!

You can also confirm that three-step remainder ladder in a single stroke using the dedicated hardware key `252 [ENTER] 105 [GCF]` to land directly on $X = \mathbf{21.00}$.

---

## 7.5 Elementary Descriptive Statistics & Data Analysis

What happens when a scientist, sports coach, or game designer collects a whole notebook full of numbers? Looking at a jumble of 20 or 30 raw numbers can make your head spin! **Statistics** gives you two superpowers for taming any list of numbers:
1. **Finding the Center (`[g] [x̄]`, `[f] [MED]`, `[g] [MODE]`):** What single "typical" number best represents the whole group?
2. **Measuring the Spread (`[RNG]`, `[IQR]`, `[g] [MAD]`):** Are all the numbers huddled tightly together, or are they scattered all over the map?

### 7.5.1 Four Physical Stories Behind Your Statistical Keys
Before touching a single statistical key, picture what each measure looks like in the real world:
- **The Mean (`[g] [x̄]`) Is Fair-Share Tower Leveling:** Suppose four eastern bluebird nestlings weigh $24\text{ g}, 26\text{ g}, 25\text{ g},$ and $29\text{ g}$. If you build four **Counting Tile** towers of heights $4, 6, 5,$ and $9$ above a $20\text{-gram}$ baseline and move tiles from the tallest tower ($9$) to the shorter towers until **every tower stands at the exact same height**, all four towers level out at **$6$ tiles** ($26\text{ g}$). Tapping `[g] [CLΣ] 24 [Σ+] 26 [Σ+] 25 [Σ+] 29 [Σ+] [g] [x̄]` performs that exact fair-share leveling on the stack ($\text{Mean} = \mathbf{26\text{ g}}$).
- **The Median (`[f] [MED]`) Is the Middle Kid in the Height Lineup:** Imagine lining up your friends from shortest to tallest for a class photo. The **Median** (`[f] [MED]`) is simply the person standing right in the **exact middle** of the line! Even if a 7-foot basketball player joins the tall end of the line, the middle person's height barely budges—which is why data detectives love the median when one extreme number would pull the mean off balance.
- **The Interquartile Range (`[IQR]`) Fences the Middle Half of the Class:** If you split that shortest-to-tallest lineup into four equal quarters, the middle two quarters ($25\%$ mark to $75\%$ mark) contain the **middle half of the class**. The distance between the lower quarter mark (`[f] [1Q]`) and the upper quarter mark (`[g] [3Q]`) is the **Interquartile Range (`[IQR]`)**—a sturdy fence around the core group that ignores extreme stragglers at both ends!
- **Mean Absolute Deviation (`[g] [MAD]`) Measures How Far Trials Wander from the Average:** Why do scientists need `[g] [MAD]` when they already have the mean (`[g] [x̄]`)? In a behavioral lab, **Raven A** solves 4 puzzle boxes in **`8, 9, 9, 10` seconds**, while **Crow B** solves them in **`6, 8, 10, 12` seconds**. Both birds have the *exact same mean* ($9.0\text{ s}$). But when you measure how far each trial wanders from $9$, Raven A's distances are $1, 0, 0, 1$ (`[g] [MAD]` $= \mathbf{0.5\text{ s}}$, super steady!), whereas Crow B's distances are $3, 1, 1, 3$ (`[g] [MAD]` $= \mathbf{2.0\text{ s}}$, four times more spread out).

| Data Measure | Key / Shift | Kid-Friendly Word Rule |
| :--- | :--- | :--- |
| **Total Count (`N`)** | `[N]` | How many numbers are in your data list |
| **Total Sum (`Σx`)** | `[f] [Σx]` | All the numbers added together |
| **Mean (Average)** | `[g] [x̄]` | $\text{Total Sum} \div \text{How Many Numbers}$ |
| **Median** | `[f] [MED]` | Middle number when lined up from smallest to largest |
| **Mode** | `[g] [MODE]` | Number that shows up the most times |
| **Range** | `[RNG]` | $\text{Biggest Number} - \text{Smallest Number}$ |
| **Interquartile Range (IQR)** | `[IQR]` | $\text{Third Quartile (3Q)} - \text{First Quartile (1Q)}$ |
| **Mean Absolute Deviation (MAD)** | `[g] [MAD]` | $\text{Mean Absolute Deviation (MAD)} = \text{Total Distance from the Mean} \div \text{How Many Numbers}$ |

Let's watch the fair-share **Mean (`[g] [x̄]`)** and middle **Median (`[f] [MED]`)** in action on two quick school datasets before we tackle a full 10-student frequency table. First, suppose you score `88`, `92`, `79`, and `95` on four science lab quizzes. What is your fair-share average (`[g] [x̄]`)? Mark 88, 92, 79, and 95 with four Counting Tiles on a desk number line: notice how the two scores above $88.5$ ($+3.5$ and $+6.5$, totaling $+10$) balance the two scores below $88.5$ ($-0.5$ and $-9.5$, totaling $-10$). Tossing all four scores into `[Σ+]` and tapping `[g] [x̄]` via `[g] [CLΣ] 88 [Σ+] 92 [Σ+] 79 [Σ+] 95 [Σ+] [g] [x̄]` confirms **`88.5`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `[g] [CLΣ]` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Reset statistical registers ($\text{Count} = 0, \text{Sum} = 0$) |
| `88` | $0.0000$ | $0.0000$ | $0.0000$ | $88.0000$ | Key in first test score 88 |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Accumulate score ($\text{Count} = 1, \text{Sum} = 88$) |
| `92` | $0.0000$ | $0.0000$ | $0.0000$ | $92.0000$ | Key in second test score 92 |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Accumulate score ($\text{Count} = 2, \text{Sum} = 180$) |
| `79` | $0.0000$ | $0.0000$ | $0.0000$ | $79.0000$ | Key in third test score 79 |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $3.0000$ | Accumulate score ($\text{Count} = 3, \text{Sum} = 259$) |
| `95` | $0.0000$ | $0.0000$ | $0.0000$ | $95.0000$ | Key in fourth test score 95 |
| `[Σ+]` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | Accumulate score ($\text{Count} = 4, \text{Sum} = 354$) |
| `[g] [x̄]` | $0.0000$ | $0.0000$ | $0.0000$ | $88.5$ | Compute mean ($354 \div 4 = 88.5$) |

Your fair-share mean lab score is $\mathbf{88.50}$.

Second, step outside from the science lab to the running track, where five sprinters finish the 100-meter dash in $12.4, 12.8, 13.1, 13.5,$ and $14.0\text{ seconds}$. What is the middle **median** (`[f] [MED]`) time? Line up five Counting Tiles from fastest to slowest on your desk: the third tile sits right in the middle with two sprinters faster and two sprinters slower, pointing straight to $13.1\text{ s}$. Entering the five sprint times into the statistical accumulator and tapping `[f] [MED]` via `[g] [CLΣ] 12.4 [Σ+] 12.8 [Σ+] 13.1 [Σ+] 13.5 [Σ+] 14.0 [Σ+] [f] [MED]` returns **`13.1`**. With $5$ runners stored in Register $Y$, the middle runner's time of $\mathbf{13.10\text{ seconds}}$ appears in Register $X$.

### 7.5.2 The 10-Quiz Score Frequency Table & The Seed of Distributions

Let's see how fast `[Σ+]` analyzes a whole classroom dataset. Suppose a 5th-grade math class records scores on a 100-point weekly quiz across 10 students:
$$70, \ 75, \ 80, \ 80, \ 85, \ 85, \ 85, \ 90, \ 90, \ 95$$

| Quiz Score | Tally | Frequency (How Many Times) | Dot Plot Visual Representation |
| :---: | :---: | :---: | :--- |
| 70 | I | 1 | ● |
| 75 | I | 1 | ● |
| 80 | II | 2 | ● ● |
| 85 | III | 3 | ● ● ● *(Peak Mode)* |
| 90 | II | 2 | ● ● |
| 95 | I | 1 | ● |
| **Total Count = Sum of All Frequencies** | — | **10** | $10$ total quiz scores |

Look at the shape of the dot plot above. The scores climb smoothly from $70$ up to a central peak at $85$ (the **Mode**, because $85$ appears the most times!), and then step down toward $95$. This bell-shaped hill is your first look at a **symmetric distribution**.

Let's audit all ten scores on the SC-6! Toss all 10 scores into your `[Σ+]` statistical basket (and remember that if you ever mistype a score, tapping `[f] [Σ-]` immediately removes it from the basket, while `[FRQ]` checks how many times a given score appears and `[Σx²]` tracks the sum of squared scores), then tap any statistical key to inspect the class results:
- `[g] [CLΣ]` $\to$ Clears all stats registers ($\text{Count} = 0$)
- `70 [Σ+]` $\to \text{Count} = 1$
- `75 [Σ+]` $\to \text{Count} = 2$
- `80 [Σ+] 80 [Σ+]` $\to \text{Count} = 4$
- `85 [Σ+] 85 [Σ+] 85 [Σ+]` $\to \text{Count} = 7$
- `90 [Σ+] 90 [Σ+]` $\to \text{Count} = 9$
- `95 [Σ+]` $\to \text{Count} = 10$

1. **Total Count:** `[N]` $\longrightarrow X = \mathbf{10}$.
2. **Sum of Scores:** `[f] [Σx]` $\longrightarrow X = \mathbf{835.0}$.
3. **Mean Score (Average):** `[g] [x̄]` $\longrightarrow X = \mathbf{83.5}$.
4. **Median Score (Middle):** `[f] [MED]` $\longrightarrow X = \mathbf{85.0}$.
5. **Mode Score (Most Common):** `[g] [MODE]` $\longrightarrow X = \mathbf{85.0}$.
6. **Range ($\text{Biggest} - \text{Smallest}$):** `[RNG]` $\longrightarrow X = \mathbf{25.0}$ ($95 - 70 = 25$).

Because the scores are balanced around 85, the **Median** and **Mode** are identical ($85.0$), while the **Mean** ($83.5$) sits just slightly below the peak because the single score of $70$ pulls the fair-share average down by $1.5$ points.

---

### 7.5.3 Measuring Spread in a Five-Quiz Study Group: IQR & MAD

Now let's zoom in on a 5-student study group with scores of $85, 90, 75, 90, 100$ so you can see how `[IQR]` and `[g] [MAD]` measure spread:

1. **Sorted Data (Shortest to Tallest):** $75, 85, 90, 90, 100$.
2. **Total Count:** $5$ scores.
3. **Total Sum:** $75 + 85 + 90 + 90 + 100 = 440.0$.
4. **Mean (Average):** $440 \div 5 = \mathbf{88.0}$.
5. **Median:** Middle number (3rd out of 5) = $\mathbf{90.0}$.
6. **Mode:** Most frequent number = $\mathbf{90.0}$.
7. **Minimum:** $\mathbf{75.0}$, **Maximum:** $\mathbf{100.0}$.
8. **Range:** $100 - 75 = \mathbf{25.0}$.
9. **Interquartile Range (IQR):** On the SC-6, the **First Quartile (1Q)** is $85.0$ and the **Third Quartile (3Q)** is $90.0$:
   $$\text{Interquartile Range (IQR)} = \text{Third Quartile (3Q)} - \text{First Quartile (1Q)} = 90.0 - 85.0 = \mathbf{5.0}$$
10. **Mean Absolute Deviation (MAD):** Measures the average distance between each score and the mean ($88.0$):
    - Distance of $75$ from $88$ is $13$; distance of $85$ from $88$ is $3$; distance of $90$ from $88$ is $2$ (twice); distance of $100$ from $88$ is $12$.
    $$\text{Total Distance from the Mean} = 13 + 3 + 2 + 2 + 12 = 32.0$$
    $$\text{Mean Absolute Deviation (MAD)} = \text{Total Distance from the Mean} \div \text{How Many Numbers} = 32.0 \div 5 = \mathbf{6.4}$$

Once you load all five scores into the statistical basket with `[g] [CLΣ] 85 [Σ+] 90 [Σ+] 75 [Σ+] 90 [Σ+] 100 [Σ+]`, you can inspect every center and spread measure with a single tap:
- `[f] [Σx]` $\to 440.00$
- `[g] [x̄]` $\to 88.00$
- `[f] [MED]` $\to 90.00$
- `[g] [MODE]` $\to 90.00$
- `[IQR]` $\to 5.00$
- `[g] [MAD]` $\to 6.40$

### 7.5.4 The Five-Number Summary, Box Plots & Outlier Analysis
When data detectives draw a **Box-and-Whisker Plot**, they line up all the numbers from smallest to largest and mark five milestones that slice the list into four equal quarters ($25\%$ in each quarter):
1. **Minimum (`MIN`):** Smallest number at the left whisker tip (`[f] [MIN]`).
2. **First Quartile (`1Q`):** Left edge of the center box ($25\%$ mark, `[f] [1Q]`).
3. **Median (`MED`):** Center line inside the box ($50\%$ mark, `[f] [MED]`).
4. **Third Quartile (`3Q`):** Right edge of the center box ($75\%$ mark, `[g] [3Q]`).
5. **Maximum (`MAX`):** Biggest number at the right whisker tip (`[g] [MAX]`).

| Box Plot Milestone | Statistical Keycap | What It Shows on the Box Plot |
| :--- | :--- | :--- |
| **Lower Whisker Tip (`MIN`)** | `[f] [MIN]` | Smallest number ($0\%$ mark) |
| **Left Box Edge — First Quartile (`1Q`)** | `[f] [1Q]` | Lower quarter mark ($25\%$ boundary of the center box) |
| **Center Line — Median (`MED`)** | `[f] [MED]` | Halfway mark ($50\%$ median line inside the box) |
| **Right Box Edge — Third Quartile (`3Q`)** | `[g] [3Q]` | Upper quarter mark ($75\%$ boundary of the center box) |
| **Center Box Width (`IQR`)** | `[IQR]` | $\text{Third Quartile (3Q)} - \text{First Quartile (1Q)}$ |
| **Upper Whisker Tip (`MAX`)** | `[g] [MAX]` | Biggest number ($100\%$ mark) |

How do scientists decide whether an unusual number is just a little high or a true **outlier** that wandered far away from the pack? They use the **$1.5 \times \text{IQR}$ Outlier Detection Rule**: measure the width of the center box (`[IQR]`), multiply it by $1.5$, and build an invisible "fence" $1.5$ box-widths below the First Quartile and above the Third Quartile:
$$\text{Lower Fence} = \text{First Quartile (1Q)} - (1.5 \times \text{IQR})$$
$$\text{Upper Fence} = \text{Third Quartile (3Q)} + (1.5 \times \text{IQR})$$
Any number that jumps past either fence is officially flagged as an outlier!

Let's see that outlier fence in action on a real cross-country race. Suppose 8 runners finish a 5K race in the following times (in minutes): $25, 28, 30, 32, 34, 35, 38, 58$. Runner 8 stopped to tie a shoelace and took $58\text{ minutes}$. Does $58$ jump past the upper outlier fence?

First, line up the eight finish times to locate the quartiles:
- **Ordered data:** $25, 28, 30, 32, 34, 35, 38, 58$
- **First Quartile (`1Q`):** $(28 + 30) \div 2 = 29.0$
- **Median (`MED`):** $(32 + 34) \div 2 = 33.0$
- **Third Quartile (`3Q`):** $(35 + 38) \div 2 = 36.5$
- **Interquartile Range (`IQR`):** $36.5 - 29.0 = 7.5$

Now build the upper outlier fence on the stack: multiplying the $7.5\text{-minute}$ box width by $1.5$ via `7.5 [ENTER] 1.5 [×]` yields a fence margin of $11.25\text{ minutes}$, and adding that margin to the Third Quartile with `36.5 [+]` places the upper fence at $\mathbf{47.75\text{ minutes}}$. Since $58$ is greater than $47.75$, the time of 58 minutes sits well past the upper fence and is a **true outlier**.

---

## 7.6 Grade 6 Pre-Algebra: Signed Numbers, Absolute Value & Inverses

In pre-algebra, you cross an exciting threshold: numbers no longer stop at zero! Every number now has both a **size** and a **direction**—stepping right (or up) into **positive numbers ($+$)**, or stepping left (or down) into **negative numbers ($-$)**.

| Negative Direction (Left of $0$) | Origin ($0$) | Positive Direction (Right of $0$) |
| :---: | :---: | :---: |
| `-5, -4, -3, -2, -1` | **`0`** | `+1, +2, +3, +4, +5` |

### 7.6.1 Hot-Air Balloons, Sandbags & Two-Color Zero Pairs
To make adding and subtracting negative numbers crystal clear, picture a **hot-air balloon** floating at altitude $0$ (sea level) alongside your **Two-Color Counters**:
- **Yellow Counters ($+1$) Are Hot-Air Puffs:** Adding a Yellow counter puffs warm air into the balloon, lifting it **up $+1\text{ meter}$**.
- **Crimson Counters ($-1$) Are Heavy Sandbags:** Adding a Crimson counter hooks a sandbag onto the basket, pulling the balloon **down $-1\text{ meter}$**.
- **Zero Pairs ($+1 + (-1) = 0$):** One $+1$ puff of hot air and one $-1$ sandbag balance each other out completely, keeping the balloon at the exact same height!
- **Why Subtracting a Negative Moves You UP ($7 - (-3) = 10$):** What happens if your balloon is floating at $+7\text{ meters}$ and you **subtract (throw overboard) $3$ heavy sandbags** ($-(-3)$)? With $3$ fewer sandbags pulling it down, the balloon shoots **up $+3\text{ meters}$** to $+10$! Taking away a negative weight has the exact same effect as adding a positive boost!

### 7.6.2 Signed Number Entry via the Negation Key `[+/-]`
On the SC-6 keypad, notice the difference between two keys that use a minus sign:
- The **subtraction key** (`[-]`) is an operation between two shelves: it subtracts Register $X$ from Register $Y$ ($Y - X$).
- The **change-sign key** (`[+/-]`) flips the sign of the single number currently sitting in Register $X$ (turning positive `8` into negative `-8`, or `-8` back into `+8`).

To enter $-8$ on your SC-6:
- Type `[8] [+/-]`. The screen immediately displays `-8`.
- Pressing `[+/-]` a second time flips `-8` right back to `8`.

Imagine checking the outdoor thermometer in Chicago on a frosty winter morning: at 6:00 AM, it reads $-14^\circ\text{C}$ ($14$ degrees below zero). By 2:00 PM, the winter sun warms the air up by $+9^\circ\text{C}$. What is the afternoon temperature?

$$\text{Temperature Change: } -14 + 9 = -5^\circ\text{C}$$

Think of 14 Crimson cold tokens meeting 9 Yellow warm tokens: 9 Zero Pairs cancel out, leaving 5 Crimson tokens ($-5^\circ\text{C}$). On the stack, key `14 [+/-] [ENTER] 9 [+]` $\to -5$, confirming an afternoon temperature of $-5^\circ\text{C}$ directly on the LCD.

What happens when *both* numbers pull in the negative direction—for instance, if you hook $15$ sandbags ($-15$) onto a balloon basket, and then hook on $28$ *more* sandbags ($-28$)? Model a smaller version with Crimson counters first ($-3 + (-5) = -8$ Crimson tokens): because both groups pull in the exact same negative direction, there are zero Yellow tokens to cancel them out! Combining the two negative movements on the stack with `15 [+/-] [ENTER] 28 [+/-] [+]` produces **`-43`**, as the two downward pulls add their sizes together to reach **$-43$**.

Now compare that with subtracting a larger positive number from a smaller one: suppose your student bank account has $\$45$ (45 Yellow $+1$ tokens), and an automatic purchase withdraws $\$70$. Where does your balance land? The first $\$45$ of the withdrawal cancels all 45 Yellow tokens down to $\$0$, and the remaining $\$25$ pulls you 25 steps below zero into Crimson debt ($-25$)! Evaluating $45 - 70$ on the SC-6 with `45 [ENTER] 70 [-]` yields **`-25`**, wiping out your positive $\$45$ balance to $\$0$ and crossing zero into negative territory (**$-\$25$**).

---

### 7.6.3 Absolute Value as Number Line Distance (`[g] [|x|]`)
Suppose your friend walks $5\text{ steps}$ east ($+5$) and you walk $5\text{ steps}$ west ($-5$). Who walked farther from the starting line? You both walked the exact same distance: **$5\text{ steps}$**!

The **absolute value** of a number, written $|x|$, is simply its **distance from zero** on the number line—and whether you walk left or right, distance is always positive:
$$\text{Absolute Value } (|x|) = \text{Distance from } 0 \text{ on the Number Line (Always Positive!)}$$

On the SC-6, pressing the shifted absolute-value key `[g] [|x|]` (`[g]` + `[+/-]`) removes any negative sign from Register $X$, leaving its positive distance from zero:
- `42 [+/-] [g] [|x|]` $\longrightarrow X = \mathbf{42}$.
- `15 [g] [|x|]` $\longrightarrow X = \mathbf{15}$.

To see why absolute value shines when crossing sea level, picture a desert hiker starting at the bottom of Badwater Basin in Death Valley at an elevation of $-86\text{ meters}$ ($86\text{ m}$ below sea level) and climbing all the way to the summit of Telescope Peak at $+3,366\text{ meters}$ above sea level. First the hiker climbs $86\text{ meters}$ just to reach sea level ($0\text{ m}$), and then climbs another $3,366\text{ meters}$ to the peak!

$$\text{Vertical Climb: } |3366 - (-86)| = |3366 + 86| = 3,452\text{ meters}$$

When you subtract the negative starting elevation from the summit height and take the absolute value via `3366 [ENTER] 86 [+/-] [-] [g] [|x|]`, the display confirms a total vertical climb of $\mathbf{3,452.00\text{ meters}}$.

- **Northern Gannet Plunge Across Sea Level & Road-Salt Freezing Science:** A diving Northern Gannet plummets from $+32\text{ m}$ in the sky to $-14\text{ m}$ underwater to catch a herring; its total plunge distance across $0\text{ m}$ sea level is $|32| + |-14| = \mathbf{46\text{ m}}$ (`32 [g] [|x|] [ENTER] 14 [+/-] [g] [|x|] [+]`). In winter chemistry, spreading rock salt lowers water's freezing point from $0^\circ\text{C}$ by $-14.5^\circ\text{C}$, while adding sugar-beet juice lowers it another $-6.75^\circ\text{C}$: keying `0 [ENTER] 14.5 [-] 6.75 [-]` shows that snowplows keep roads ice-free down to **$-21.25^\circ\text{C}$**.

---

### 7.6.4 Word Rules, Mystery Number Backwards Puzzles & Token Probability
Your counting tiles and Dice & Spinner Studio connect everyday word rules directly to the RPN stack:
- **Kea Parrot Puzzle Locks:** In a sanctuary puzzle challenge, an alpine kea parrot earns $10\text{ points}$ for each wire latch it unfastens and $3\text{ points}$ for each door it slides open:
  $$\text{Total Points} = (10 \times \text{Wire Latches}) + (3 \times \text{Doors})$$
  For $7$ wire latches and $4$ doors, the 4-register stack finds both parts and adds them with zero parentheses: `10 [ENTER] 7 [×] 3 [ENTER] 4 [×] [+]` $\longrightarrow \mathbf{82\text{ points}}$.
- **Mystery Number Backwards Puzzles & Inverse Operations:** Start with a Mystery Number, multiply by 3, and subtract 5 to get 16—work backwards on your stack `16 [ENTER] 5 [+] 3 [÷]` to uncover `7`! Adding $+5$ first undoes the $-5$ (`16 [ENTER] 5 [+]` $\to 21$), and dividing by $3$ (`3 [÷]`) undoes multiplying by 3 to reveal the Mystery Number **$\mathbf{7}$**.
- **Kea Token Jars:** When a kea parrot peers into a clear jar holding $9$ black tokens (worth a peanut) and $3$ orange tokens (worth nothing), its theoretical chance of drawing a black token is `[.] 9 [.] 12 [g] [SIMP]` $\longrightarrow \mathbf{3/4} = 75\%$—which you can test experimentally on your SC-6 by pressing `[🎲]` across 20 trials.

---

### 7.6.5 Geometric Inverses: Area-to-Side-Length (`[x²]` and `[f] [√x]`)
In elementary school, the square key `[x²]` and square root key `[f] [√x]` are taught as **square area-to-side-length opposites**:
- Squaring a number finds the **area** of a square from its side length: $\text{Square Area} = \text{Side} \times \text{Side}$.
- Taking the square root finds the **side length** of a square from its area: $\text{Side} = \sqrt{\text{Square Area}}$.

| Square Geometry | Forward Operation (`[x²]`) | Inverse Operation (`[f] [√x]`) |
| :--- | :--- | :--- |
| **5 cm × 5 cm Tile Square** | $\text{Side} = 5\text{ cm} \to \text{Square Area} = 5 \times 5 = \mathbf{25\text{ cm}^2}$ | $\text{Square Area} = 25\text{ cm}^2 \to \text{Side} = \sqrt{25} = \mathbf{5\text{ cm}}$ |

Suppose a horse pasture has an exact square area of $1,225\text{ square meters}$. How long is one side of the pasture, and how much fencing is needed to surround all four sides? Taking the square root of the area with `1225 [f] [√x]` immediately reveals a side length of $35.00\text{ meters}$ ($\text{Side} = \sqrt{\text{Square Area}}$), and multiplying that live result by four equal sides via `[4] [×]` gives a total perimeter of $\mathbf{140.00\text{ meters}}$ of fence.

### 7.6.6 Directed Integers in Motion: Elevators, Submersibles & Ledgers
To master pre-algebra, you can follow multi-step signed integers in motion across skyscrapers, deep-sea trenches, and student bank accounts!

First, imagine a high-rise tower with 3 subterranean parking levels (Floors $-3, -2, -1$), a ground lobby (Floor $0$), and 60 tower floors (Floors $1 \dots 60$). An elevator starts at subterranean parking Level $-3$, travels up $+45$ floors to deliver office supplies, descends $-12$ floors to the cafeteria, and finally descends $-33$ floors:

$$\text{Elevator Journey: } -3 + 45 - 12 - 33 = -3\text{ (Back at parking Level -3!)}$$

Keying `3 [+/-] [ENTER] 45 [+] 12 [-] 33 [-]` $\to -3$ returns the elevator precisely to subterranean parking Level $-3$ with zero register overflow.

Next, let's head out to sea aboard the marine biology research ship and launch the autonomous deep-sea submersible *Nautilus Jr.*! First, as *Nautilus Jr.* is lowered from the ship's A-frame crane at $+4\text{ meters}$ above sea level down to a deep survey trench at $-350\text{ meters}$ (before rising $+125\text{ meters}$ to a hydrothermal vent and descending $-45\text{ meters}$), subtracting the trench elevation from the deck height via `[4] [ENTER] 350 [+/-] [-]` reveals a total vertical descent span of $354.00\text{ meters}$ ($4 - (-350) = +354\text{ m}$) while automatically tucking $-350$ into `[f] [LASTX]`—so tapping `[f] [LASTX] 125 [+] 45 [-]` tracks the vent excursion to **$-270.00\text{ meters}$** without typing `350 [+/-]` twice. Now let's trace the second *Nautilus Jr.* canyon dive step by step across all four stack registers: hovering at a mid-water depth of $-180\text{ m}$ ($180\text{ m}$ below sea level), the submersible puffs compressed air into its ballast tanks to rise $+65\text{ m}$ over a coral ridge, and then dives $-40\text{ m}$ into a trench canyon. Trace *Nautilus Jr.* along a vertical number line ($-180 \to -115 \to -155$) and chain the moves on your SC-6 with `180 [+/-] [ENTER] 65 [+] 40 [-]` to land at **`-155`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `180` | $0.0000$ | $0.0000$ | $0.0000$ | $180.0000$ | Key in initial depth magnitude 180 |
| `[+/-]` | $0.0000$ | $0.0000$ | $0.0000$ | $-180.0000$ | Negate to depth $-180\text{ m}$ |
| `[ENTER]` | $0.0000$ | $0.0000$ | $-180.0000$ | $-180.0000$ | Push initial depth to Register $Y$ |
| `65` | $0.0000$ | $0.0000$ | $-180.0000$ | $65.0000$ | Key in ascent $+65\text{ m}$ |
| `[+]` | $0.0000$ | $0.0000$ | $0.0000$ | $-115.0000$ | Add ascent: $-180 + 65 = -115\text{ m}$; stack drops |
| `40` | $0.0000$ | $0.0000$ | $-115.0000$ | $40.0000$ | Key in dive descent $40\text{ m}$; stack lifts $-115$ to $Y$ |
| `[-]` | $0.0000$ | $0.0000$ | $0.0000$ | $-155.0000$ | Deduct descent: $-115 - 40 = -155\text{ m}$; stack drops |

The submarine settles at a final depth of $\mathbf{155\text{ m}}$ below sea level ($-155.00$).

Signed numbers also govern your personal finances! Suppose your student checking account starts with a positive balance of $+\$120.00$, and you track four transactions using the SC-6 currency formatter `[$]`:
- You buy school books for $\$85.00$ ($-\$85.00$).
- You buy an art supply kit for $\$60.00$ ($-\$60.00$).
- The bank assesses an overdraft penalty of $\$25.00$ ($-\$25.00$).
- You deposit a lawn-mowing paycheck of $\$95.00$ ($+\$95.00$).

Keying `120 [ENTER] 85 [-]` deducts the $\$85.00$ book purchase to leave $35.00$, subtracting `60 [-]` drops the ledger into overdraft at $-25.00$, subtracting the `25 [-]` fee reaches $-50.00$, adding the `95 [+]` paycheck restores a positive balance of $45.00$, and pressing `[$]` formats the closing balance as **$\$45.00$**.

---

### 7.6.7 Common Questions: Why 1 Is Not Prime & Subtracting Negatives

- **Why Is the Number 1 Not a Prime Number?** A prime number has *exactly two distinct positive factors* (1 and itself), while a composite number has three or more factors. The number $1$ has only *one* factor (just $1$), so it is neither prime nor composite—mathematicians call $1$ a **unit**. Test it on your SC-6 with `1 [PRIME]` and the screen alerts `INVALID DATA`. Now test `2` (`2 [PRIME]`): it flashes `PRIME` and keeps `2` on the display—the smallest prime number and the only even prime.
- **Why Does Subtracting a Negative Make a Number Bigger ($7 - (-3) = 10$)?** Imagine running a school store where a friend owes you $\$3$ (a debt of $-3$), or a hot-air balloon at $+7\text{ m}$ tossing $3$ sandbags ($-3$) overboard. If you cancel—or *subtract*—that $-3$ debt, your friend is $\$3$ richer and the balloon rises $+3\text{ m}$ higher! Taking away a negative is the exact same as adding a positive. Try it on your SC-6: `7 [ENTER] 3 [+/-] [-]` gives **`10`**.

If you ever see an unexpected result while exploring primes, statistics, or signed numbers, check this quick reference table:

| What Happened on Your Screen | Why It Happened | How to Fix It |
| :--- | :--- | :--- |
| **Claiming 1 is prime** | Conflating "divisible only by 1" with "having exactly two distinct factors." | *"A prime must have exactly two distinct factors: 1 and itself. 1 only has one factor. The SC-6 classifies 1 as a unit, neither prime nor composite."* |
| **Confusing GCF and LCM** | Assuming "Greatest" must yield a larger number than "Least." | *"A factor divides INTO a number, so it must be smaller than or equal to the number. A multiple MULTIPLIES the number, so it grows larger. GCF $\le$ numbers $\le$ LCM."* |
| **Treating $\lvert x\rvert$ as 'change the sign'** | Believing absolute value turns positive numbers into negative numbers. | *"Absolute value is distance on a number line. Distance is never negative. The distance from 5 to 0 is 5; the distance from -5 to 0 is also 5. $\lvert 5\rvert = 5$ and $\lvert -5\rvert = 5$."* |
| **Adding negatives: $-4 + (-3) = -1$** | Subtracting magnitudes instead of accumulating directed negative quantities. | *"If you take 4 steps backward ($-4$), and then take 3 more steps backward ($-3$), you are 7 steps backward ($-7$), not 1 step. Use Crimson tokens to model the sum."* |
| **Expecting Mean = Median always** | Assuming all datasets are perfectly symmetrical. | *"In skewed datasets (like home prices or quiz scores with an outlier), extreme values pull the mean away from the center. The median stays fixed in the middle."* |
| **Confusing `[+/-]` with `[-]`** | Using the binary subtraction operator to enter negative values. | *"The `[-]` key subtracts two numbers ($Y - X$). The `[+/-]` key changes the sign of the single number you are actively typing."* |

---

### 7.6.8 Black-Box Statistics vs. Prime Towers, Fair-Share Blocks & Dice Trials

Now that you have explored probability trials, prime factor towers, statistical accumulators, and signed numbers, look at how the SC-6's dedicated number-theory and statistical keys compare against manual trial division and parenthesized averaging on an algebraic calculator:

| Challenge / Real-World Task | The Algebraic Calculator Trap (Infix) | Algebraic Keystrokes & Clutter | The StackCalc + Blocks Method (RPN Stack + Visual Studio) | StackCalc Keystrokes | The Stack Advantage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GCF & LCM Secret Partner Rule:** Checking that $\text{GCF} \times \text{LCM} = 24 \times 36 = 864$ | No hardware GCF or LCM keys: students must sketch manual factor trees on scratch paper, find prime powers, and re-enter multi-step arithmetic from scratch. Intermediate products vanish. | `2 4 * 3 6 =` Manual scratch work factor trees (28+ keystrokes, zero live factors) | **Hardware `[GCF]` & `[f] [LCM]` Stack Duality:** Single-tap prime engines extract GCF (12) and LCM (72). Because `[GCF]` saves 36 in `LASTX`, tapping `24 [f] [LASTX] [f] [LCM] [×]` proves $12 \times 72 = 864$ without re-typing 36. | `24 [ENTER] 36 [GCF] 24 [f] [LASTX] [f] [LCM] [×]` (11 keystrokes) | **60% fewer keystrokes** Zero scratch paper; `[f] [LASTX]` and the stack prove the Secret Partner Rule live on screen. |
| **Euclidean Division:** Hydraulic gate synchronization: $105 \div 45 \implies \text{Quotient} = 2, \text{Remainder} = 15$ | Infix division yields decimal $2.3333333$. Finding integer quotient and remainder requires rounding down, re-multiplying $2 \times 45 = 90$, and subtracting $105 - 90 = 15$ across multiple steps. | `1 0 5 / 4 5 =` $\to 2.333$, `1 0 5 - ( 2 * 4 5 ) =` (18 keystrokes, modal confusion) | **Single-Tap Euclidean `[g] [÷R]`:** Hardware integer division deposits integer quotient $2$ in Register $X$ and exact remainder $15$ in Register $Y$ simultaneously in one step. | `105 [ENTER] 45 [g] [÷R]` (8 keystrokes) | **56% fewer keystrokes** Simultaneous quotient and remainder display matches physical token distribution. |
| **Prime Factorization:** Cryptographic vault key factoring: $2,639 = 7 \times 13 \times 29$ | Standard algebraic calculators provide no hardware factoring. Students must manually test trial divisors on scratch paper ($2,639 \div 3, \div 7, \dots$) through tedious, error-prone trial division. | `2 6 3 9 / 3 =`, `2 6 3 9 / 7 =` $\to 377$, `3 7 7 / 1 1 =` $\dots$ (35+ keystrokes, manual logging) | **Hardware Prime Engine `[g] [FACT]`:** Dedicated factoring co-processor parses composite numbers instantly into prime components, rendering $7 \times 13 \times 29$ across the daylight dot-matrix display. | `2639 [g] [FACT]` (5 keystrokes) | **85% fewer keystrokes** Instant canonical decomposition; flashes `PRIME` or renders prime tower strings without guesswork. |
| **Statistical Mean:** Four test scores averaging: $88, 92, 79, 95 \implies \text{Mean} = 88.5$ | Must enter chained addition with parentheses `( 88 + 92 + 79 + 95 ) / 4 =`. Forgetting outer brackets divides only 95 by 4, creating an undetected order-of-operations error ($283.75$). | `( 8 8 + 9 2 + 7 9 + 9 5 ) / 4 =` (23 keystrokes, bracket risk) | **Hardware Statistical Accumulator (`[Σ+]`):** Each data point accumulates into dedicated $\Sigma$ registers with running sample count. Pressing `[g] [x̄]` extracts the exact mean with zero syntax parentheses. | `[g] [CLΣ] 88 [Σ+] 92 [Σ+] 79 [Σ+] 95 [Σ+] [g] [x̄]` (16 keystrokes) | **Zero Parentheses Clutter** Running sample count protects data entry; enables instant spread and total sum queries. |

---

## 7.7 Where to Go Next: Companion Workbook Quests & Kitchen-Table Challenges

> *For 52 additional worked problems with full 4-register stack tables, see Chapter 7 of the [SC-6 Elementary Companion Problem & Activity Workbook](../curriculum/sc6-elementary-companion-workbook.md).*

Ready to test your data-detective instincts and number-theory skills away from this chapter? Here is how to connect your Polyhedral Dice, Prime Factor Blocks, Counting Tiles, and SC-6 with the [Big Ideas Math Middle School Supplement](../curriculum/big-ideas-middle-school-sc6-workbook.md) across **Unit 1: Numerical Expressions & Factors (Sections 1.4–1.5)**, **Unit 4: Algebraic Expressions & Properties (Sections 4.1–4.4)**, **Unit 6: Integers, Number Lines & The Coordinate Plane (Sections 6.1–6.5)**, **Unit 7: Equations & Inequalities (Sections 7.1–7.5)**, **Unit 9: Statistical Measures & Data Displays (Sections 9.1–9.4)**, and **Unit 10: Rational Numbers, Two-Step Equations & Probability (Sections 10.1–10.4)**:

1. **The 100-Roll Casino Boss Challenge (Curriculum Guide Unit 7 & Student Workbook):** Grab the 4 equal-volume pip dice from your Dice & Spinner Studio and roll two dice 36 times, logging each sum ($2$ through $12$) into `[Σ+]` on your SC-6 and stacking Counting Tiles into a live tabletop histogram. Tap `[g] [x̄]`, `[f] [MED]`, and `[g] [MODE]`—did Lucky 7 win the tallest tower, and how close did your experimental mean get to $7.00$?
2. **The Impostor Prime Hunt (Timed Proficiency Trials — Prime Sieve Sprint):** Numbers like $91$, $119$, $133$, and $143$ love to disguise themselves as primes because they are odd and aren't divisible by $2, 3,$ or $5$. Race a partner to unmask all four impostors using `[PRIME]` and `[g] [FACT]` on your SC-6, then build their secret prime towers on your Prime Factor Studio comparator stage!
3. **The Secret Partner Speed Proof (Big Ideas Middle School Supplement):** Pick any two mystery two-digit numbers—say, $36$ and $48$. Compute their `[GCF]`, then use `[f] [LASTX]` so you don't have to re-type the second number when computing their `[f] [LCM]`, and multiply the two results together. Can your family find *any* pair of whole numbers that breaks the Secret Partner Rule $\text{GCF} \times \text{LCM} = \text{First Number} \times \text{Second Number}$?

---

## 7.8 Chapter Summary & Looking Ahead

With the probability generator, prime engine, statistical registers, and signed-number keys, you can analyze both discrete numbers and experimental data on the stack:

1. **Discrete Probability & Fair Symmetries:** You investigated fair polyhedral dice (`[🎲]`), experimental frequencies, and compound probability events without tree confusion.
2. **The Prime Factor Engine:** You used the Prime Factor Studio and SC-6 dedicated hardware keys (`[PRIME]`, `[g] [FACT]`, `[GCF]`, `[f] [LCM]`, `[g] [÷R]`)—plus `[f] [LASTX]`—to decompose composite numbers, calculate greatest common factors, and prove the Secret Partner Rule.
3. **Descriptive Statistics:** With the non-volatile statistical accumulator (`[Σ+]`), you evaluated real datasets, discovering how means, medians, and modes capture central tendencies while IQR and MAD reveal spread.
4. **Pre-Algebra & Directed Numbers:** You conquered negative numbers and zero pairs with the sign toggle (`[+/-]`) and distance metrics (`[g] [|x|]`).

In **[Chapter 08: The Gamified Math Quiz Engine](sc6/08-math-quiz-engine.md)**, you will take everything you have learned and put your operational speed to the test. You will enter the interactive quiz game mode on your SC-6, solving rapid-fire arithmetic challenges, racing against the hardware timer, and tracking your accuracy streaks on the daylight LCD. Let's see how fast your mathematical reflexes really are!

---

# Chapter 8: The Gamified Math Quiz Engine

## 8.1 The Musician's Scales & The Astronaut's Simulator: Why Instant Math Reflexes Set Your Creative Brain Free

Watch a master concert pianist sit before a Steinway grand piano to perform a Rachmaninoff concerto. Their fingers fly across eighty-eight ebony and ivory keys with dizzying speed, striking chords of astonishing harmonic complexity. If that pianist had to pause for even a quarter of a second to consciously calculate which fingers belong on middle C, E-flat, and G, the music would instantly collapse into dissonant stuttering. The pianist can pour their soul into emotional nuance, rubato tempo, and melodic phrasing *only because their fingers mastered scales, arpeggios, and Hanon drills years ago*. The mechanical technique was drilled into smooth muscle memory so thoroughly that it became invisible.

Now journey to Cape Canaveral during the golden age of Apollo spaceflight. Inside the mission flight simulators, astronauts like Neil Armstrong and Jim Lovell spent hundreds of grueling hours strapped into mock command modules while flight instructors deliberately triggered catastrophic thruster failures, computer alarms, and guidance malfunctions. In an emergency traveling at 25,000 miles per hour, there is no time to consult a flight manual or ponder first principles from scratch. The astronauts drilled until their physical reactions were instantaneous, cool-headed reflexes. Because survival instincts were completely automated, their mental energy was liberated to make life-or-death decisions when the unexpected occurred.

In mathematics, **elementary fact fluency is your musical scale and your flight simulator**.

When you look at $7 \times 8$ and have to count by sevens on your fingers ($7, 14, 21, 28, 35, 42, 49, 56$), your brain gets tired before you even start the rest of the problem. When basic math facts become second nature—because you can picture your **Math Dominoes**, **Counting Tile Arrays**, and **Fraction Towers** in your mind's eye—your brain stays fresh for multi-step puzzles and creative solutions *([Ma, 1999](sc6/appendix-c-formulas-and-conversions.md#cite-ma1999))*.

The StackCalc SC-6 does not replace your human brain—it coaches it. By integrating an authentic, hardware-timed mental sprint engine directly into the calculator's silicon (`[f] [?]`), the SC-6 transforms math practice into a focused, rhythmic, distraction-free flow state.

![The SC-6 Elementary Hardware Calculator](../assets/renders/sc6-elementary-hero.png)

---

![Launch SC-6 Gamified Arithmetic Sprint Quiz Engine](../assets/manuals/screenshots/sc6_quiz_engine_mode.png)

---

## 8.2 Stepping into the Rhythm Game: How the Quiz Engine Works (`[f] [?]` & `[ENTER]`)

Have you ever played a musical rhythm game where notes glide down the screen and you tap the beat right on time, or climbed into an arcade flight simulator where each checkpoint unlocks a faster, higher-altitude course? Tapping `[f] [?]` (`[f]` + `[C]`) transforms the SC-6 screen into an interactive mental-math flight deck where you key in answers using digits `[0]` through `[9]`, the two-dot fraction separator `[.]`, the negative toggle `[+/-]`, or the backspace key `[<-]`, and submit every puzzle with a single rhythmic press of `[ENTER]`. At any point during a flight, pressing `[g] [SHOW]` lets you inspect your active score, streak, and average response time, while pressing `[C]` twice—or tapping any base display mode key (`[NUM]`, `[g] [FIX]`, `[f] [ALL]`, or `[FDISP]`)—exits the quiz sandbox and restores your stack registers so you can verify answers with `[+]`, `[-]`, `[×]`, `[÷]`, `[g] [÷R]`, `[g] [SIMP]`, and `[f] [LASTX]`.

### 8.2.1 Two Ways to Play: RPN Mystery Puzzles & Classic Mental Sprints
Most quiz apps lock you into multiple-choice guessing games—where you can often spot the right answer just by looking at the last digit without actually doing the math. On the SC-6, there are no multiple-choice buttons to guess from. Instead, the Quiz Engine challenges your brain with two complementary prompt styles on the daylight LCD:

1. **RPN Missing-Value Puzzles (`3 ? + = 10` or `8 ? × = 56`):** Shows how two numbers sit on Floor $Y$ and Floor $X$ before an operation combines them, with a mystery question mark `?` hiding one of the floors:
   $$\mathtt{3 \ ? \ + \ = \ 10}$$
2. **Direct Mental-Math Prompts (`4 + 5 = ?`, `1/2 + 1/4 = ?`, or `35² = ?`):** Shows a classic arithmetic or number-sense challenge where you picture the blocks in your head, type the exact answer into Register $X$, and tap `[ENTER]`.

| Quiz Header (`[f] [?] LVL 1`) | Active Puzzle Prompt | Stack Display (`Y` / `X`) |
| :--- | :---: | :--- |
| **`SCORE: 40`** • **`STREAK: 3 ●●●○○`** | **`3  ?  +  =  10`** | **`Y: 3`**, **`X: _`** *(awaiting entry)* |

*Figure 8.1: Graphic LCD Layout in Quiz Mode: Solving for Missing Value `?`*

Look at the puzzle `3  ?  +  =  10` in Figure 8.1 as a four-step story on the flight instruments:
- *"Start with `3` resting on Floor $Y$."*
- *"Place the missing mystery number `?` on the Ground Floor ($X$)."*
- *"Press `+` to combine them."*
- *"Your total must land on `10`."*

In a heartbeat, your brain translates that stack story into a familiar number bond: *"What number added to 3 makes 10?"* Better yet, after any quiz sprint, you can test every single puzzle right in `[NUM]` mode using the exact RPN stack sequences shown in each level below.

---

### 8.2.2 One-Tap Submission with `[ENTER]`
Answering a puzzle in Quiz Mode is designed to keep your fingers in a smooth, uninterrupted rhythm:
1. Read the puzzle on the screen and picture the blocks in your mind.
2. Type your answer using the number keys (for example, `[7]`).
3. Tap **`[ENTER]`** to lock it in!

The moment you press `[ENTER]`, the calculator checks your work and measures how fast you solved it against the 4-second speed target:
1. **Smart Fraction & Decimal Check:** The engine reads your whole number, decimal, or fraction from Register $X$—and automatically simplifies fractions so equivalent answers like `2/4` or `0.5` match `1/2`.
2. **Speed & Streak Scoring:** Just like hitting a "Perfect!" beat in a rhythm game, the engine checks how many seconds you took from the moment the puzzle appeared:
   - **Fast Match (Under 4 seconds):** Flashes `★ FAST!  <ans> (<time>s)`, awards **`+20` mastery points**, adds points to your session score, and lights up one more dot on your fast streak (`+1`).
   - **Good Match (4 to 8 seconds):** Flashes `✓ GOOD  <ans> (<time>s)`, awards **`+10` mastery points**, adds to your session score, and protects your current streak so you don't lose your progress.
   - **Steady Match (Over 8 seconds):** Flashes `OK  <ans> (<time>s)`, awards **`+5` mastery points**, adds to your session score, and resets your fast streak to `0` so you can start a fresh speed run.
   - **Missed Attempt:** Flashes `WRONG: <expected>` so you immediately see the right fact, subtracts **`-10` mastery points** (never dropping below `0%`), resets your fast streak to `0`, and gently steps down to a friendlier question band if your mastery bar dips below $25\%$.

---

## 8.3 The 6-Level Adaptive Curriculum Ladder & Classroom Seed Codes

Have you ever wondered how a great coach knows the exact moment to make a drill slightly harder—not so easy that you get bored, and not so hard that you get frustrated? During solo practice, the SC-6 shuffles each level's question deck automatically so you never memorize a fixed list of answers. And when you want to race a friend or run a classroom relay, two players can type the exact same **Classroom Seed Number** (such as `42` followed by `[f] [?]`) so both calculators deal the exact same shuffled puzzles in the exact same order!

Every level is organized into **three smooth difficulty bands (`Band 1: Warm-Up`, `Band 2: Cruising`, `Band 3: Challenge`)**, displaying either **RPN Stack Prompts** (`3 4 + = ?`) or **Algebraic Prompts** (`3 + 4 = ?`):

| Level (`Menu Label`) | Focus Tier | Question Pool & 3-Band Fluency Progression | Fast Target | Mastery Advance |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1** (`L1: +/- to 10`) | Warm-Up Tier (Number Bonds) | **Single-Digit Number Bonds (Sums & Differences to 10):** • **Band 1:** Sums $\le 5$ and differences within 5 ($3 + 2 = {?}$, $4 - 1 = {?}$). • **Band 2:** Sums 6 to 10 and complements to 10 ($7 + 3 = {?}$, $8 - 5 = {?}$). • **Band 3:** Missing-addend and missing-subtrahend puzzles (`3 + ? = 10`, `? - 4 = 5`). | Under 4 seconds (`★ FAST!`) | $100\%$ Mastery or $5$ Fast Streak |
| **Level 2** (`L2: +/- to 100`) | Two-Digit Mental Fluency | **Whole Number Addition & Subtraction to 100:** • **Band 1:** Two-digit + single-digit without regrouping ($23 + 5 = {?}$, $48 - 6 = {?}$). • **Band 2:** Full two-digit mental addition & subtraction ($34 + 25 = {?}$, $67 - 24 = {?}$). • **Band 3:** Two-digit regrouping across tens and missing operands (`47 + ? = 85`, `? - 28 = 44`). | Under 4 seconds (`★ FAST!`) | $100\%$ Mastery or $5$ Fast Streak |
| **Level 3** (`L3: x/÷ to 12`) | Grades 3–4 Core | **Times Tables & Exact Division Facts to $12 \times 12$:** • **Band 1:** Foundational tables $1\text{--}5$ ($5 \times 4 = {?}$, $20 \div 5 = {?}$). • **Band 2:** Full multiplication & division tables $2\text{--}9$ ($7 \times 8 = {?}$, $56 \div 7 = {?}$). • **Band 3:** Extended tables $6\text{--}12$ and missing-factor equations (`8 × ? = 96`, `? ÷ 9 = 11`). | Under 4 seconds (`★ FAST!`) | $100\%$ Mastery or $5$ Fast Streak |
| **Level 4** (`L4: Fractions`) | Grades 4–5 Core | **Proper Fractions & Mixed Operations (200-Card Shuffled Deck):** • **Band 1:** Like-denominator addition & subtraction with GCF reduction ($1/4 + 1/4 = 1/2$). • **Band 2:** Unlike denominators $\le 6$ ($1/2 + 1/3 = 5/6$, $3/4 - 1/6 = 7/12$). • **Band 3:** All four operations ($+, -, \times, \div$) with denominators up to 10 ($2/3 \div 4/5 = 5/6$). | Under 4 seconds (`★ FAST!`) | $100\%$ Mastery or $5$ Fast Streak |
| **Level 5** (`L5: Mixed Mastery`) | Grades 5–6 Bridge | **Mixed Mastery (Interleaved Arithmetic, Fractions & Warm-Ups):** • **RPN Mode:** $40\%$ proper fraction card deck interleaved with $60\%$ Level 2/3 whole-number operations. • **Band 3 Bridge:** Blends in 20 pre-competition mental math warm-ups ($15^2$, $23 \times 11$, $16 \times 25$, $\text{GCF of } 12\text{ and } 18$, $\text{LCM of } 4\text{ and } 6$, $1+2+\dots+10$). | Under 4 seconds (`★ FAST!`) | $100\%$ Mastery or $5$ Fast Streak |
| **Level 6** (`L6: Math Champ`) | Grades 6–7+ Olympiad | **Number Sense Championship Deck (60 Curated Olympiad Problems):** • **Band 1 (20 cards):** Squares ending in 5 ($35^2, 65^2$), $\times 11$ ($43 \times 11$), $\times 25/\times 50$, $\text{GCF}/\text{LCM}$, triangular series. • **Band 2 (20 cards):** $\times 101$, $\times 125$, near-100 products ($98 \times 97$), difference of squares ($54^2 - 46^2$), cubes, benchmarks. • **Band 3 (20 cards):** Remainder puzzles, $\times 37$, $\times 3367$, sum of odds/evens, unit-fraction sums ($\frac{1}{6} + \frac{1}{12} + \frac{1}{20}$), powers of 2. | Under 4 seconds (`★ FAST!`) | $100\%$ Mastery or $5$ Fast Streak |

Every level is directly paired with your physical **StackCalc Manipulative Studios** so that mental speed grows naturally out of hands-on discovery. In Levels 1 and 2, for instance, you build instant number-bond recognition using the **Math Dominoes**—whose 28 double-six domino tiles train your eyes to spot $4 + 5 = 9$ and turn-around twins like $[3 \mid 5]$ and $[5 \mid 3]$ without counting dots one by one—and the **Quest Scoreboard**, whose physical **`?` Mystery Block** slots right into an equation rail to model missing-value puzzles like `3 ? + = 10` before you tap `[f] [?]` on the keypad.

![Math Dominoes Pairing: Concrete Number Bonds and Commutative Pairs](../assets/manuals/math_dominoes_pairing.png)

![Dominoes Studio: Modular Enclosure and Tactile Training Tiles](../assets/renders/dominoes-studio-hero.png)

Let's step into the simulator cockpit and fly through all six levels of the curriculum ladder to see how each physical manipulative studio powers your mental reflexes and how every quiz prompt can be verified on the 4-register stack in `[NUM]` mode.

### 8.3.1 Level 1: Single-Digit Number Bonds (Sums & Differences to 10)
Strap into the simulator cockpit and check your instrument panel! Level 1 is your runway warm-up: instead of counting on your fingers, your goal is to train your eyes to recognize number bonds up to 10 in a single glance using your **Math Dominoes** and **Ten-Frame Tray**.

Our first runway prompt flashes a classic near-double: $4 + 5 = {?}$. Draw the $[4 \mid 5]$ tile from your **Math Dominoes**: you don't need to count nine dots one by one because the twin $4$-dot patterns leap right out at your eyes ($4 + 4 = 8$), with $1$ extra center dot making $8 + 1 = 9$. When the quiz prompt `4 [ENTER] 5 [+] ?` flashes on screen, tap `9 [ENTER]` (aim for under $< 2.0\text{ seconds}$ to light your first streak pip `●○○○○`). In `[NUM]` mode, keying `4 [ENTER] 5 [+]` produces **`9`**, as pushing `4` onto Floor $Y$ and adding `5` on Floor $X$ merges both domino halves into `9`.

Right on the heels of that near-double, the flight deck flips addition around into a ten-frame complement puzzle: $10 - 7 = {?}$. Your **Ten-Frame Tray** holds 10 counters in two rows of 5. When you lift away 7 counters (one full row of 5 plus 2 more), your eyes immediately see 3 empty sockets waiting to be filled ($10 - 7 = 3$, because $7$ and $3$ are ten-partners). On the quiz puzzle `10 [ENTER] 7 [-] ?` (or Missing-Value Puzzle `10 ? - = 3`), enter `3 [ENTER]` within $< 2.0\text{ seconds}$. Checking on the stack with `10 [ENTER] 7 [-]` confirms **`3`**: starting with a full `10` in Register $Y$ and taking away `7` in Register $X$ leaves its ten-partner `3`.

---

### 8.3.2 Level 2: Two-Digit Mental Addition & Subtraction (To 100)
With five fast answers in Level 1, the screen flashes `★ NEXT LEVEL UNLOCKED! ★` and promotes your flight simulator to Level 2! Notice how every number bond you just mastered in Level 1 now scales up tenfold to let you leap across tens and ones up to 100.

First, watch how single-digit bonds turn into tens bonds when the cockpit displays $40 + 30 = {?}$. Place 4 counters and 3 counters in your **Ten-Frame Tray** to see $4 + 3 = 7$. Now imagine each counter is a 10-rod: $4\text{ tens} + 3\text{ tens} = 7\text{ tens} = 70$. When `40 [ENTER] 30 [+] ?` appears, tap `70 [ENTER]` (aim for under $< 2.5\text{ seconds}$). You can verify the sum on the stack via `40 [ENTER] 30 [+]` to reach **`70`**—adding tens works just like adding ones, with a zero holding the ones place.

What if the second number has both tens and ones, like our next checkpoint prompt $80 - 25 = {?}$? Instead of trying to borrow on imaginary paper in the air, jump in two clean steps: start with 8 tens ($80$) in your **Ten-Frame Tray**, hop back 2 tens to land on $60$ ($80 - 20 = 60$), and then hop back 5 more to land on $55$ ($60 - 5 = 55$). For `80 [ENTER] 25 [-] ?` (or Missing-Value Puzzle `80 ? - = 55`), enter `55 [ENTER]` within $< 3.0\text{ seconds}$. Evaluating `80 [ENTER] 25 [-]` on the stack yields **`55`**, showing how subtracting in two mental jumps ($80 \to 60 \to 55$) matches the stack result `55` with zero paper borrowing.

---

### 8.3.3 Level 3: Multiplication & Division Mastery (Up to $12 \times 12$)
Now you lift off into orbital flight! Level 3 turns the rectangular tile grids you built in Chapter 02 into lightning-fast multiplication and missing-factor reflexes up to $12 \times 12$.

Many kids find our first orbital prompt—$7 \times 8 = {?}$—the trickiest fact in the times table, until they slice the rectangle in two! Split 7 rows of 8 into $(5 \times 8) + (2 \times 8)$. Build the $2 \times 8 = 16$ rectangle using 16 of your **24 Array Tiles**, then add the friendly five-times fact $5 \times 8 = 40$ in your head: $40 + 16 = 56$. For `7 [ENTER] 8 [×] ?` (or Missing-Value Puzzle `7 ? × = 56`), tap `56 [ENTER]` (aim for under $< 1.5\text{ seconds}$). Multiplying on the stack with `7 [ENTER] 8 [×]` lands on **`56`**. Bonus memory hook: count four digits in a row—$5, 6, 7, 8 \implies 56 = 7 \times 8$!

Division puzzles in Level 3 ask you to spot the missing side of a rectangle, like $72 \div 9 = {?}$. Test the 9s pattern with 18 of your **24 Array Tiles** ($2 \times 9 = 18$—notice how the digits $1 + 8 = 9$ always add up to $9$, and the tens digit $1$ is always $1$ less than the multiplier $2$). So when you see $72 \div 9$, look at the tens digit $7$ and add $1$: $7 + 1 = 8$ rows of 9 ($8 \times 9 = 72 \implies 72 \div 9 = 8$)! When `72 [ENTER] 9 [÷] ?` appears, enter `8 [ENTER]` within $< 1.8\text{ seconds}$. Confirming in `[NUM]` mode via `72 [ENTER] 9 [÷]` returns **`8`**, as dividing `72` in Register $Y$ by `9` in Register $X$ reveals the missing side length `8`.

---

### 8.3.4 Level 4: Remainder Division & Fraction Benchmarks
Welcome to Level 4! Here the Quiz Engine shifts from whole-number rectangles into leftover tiles (`[g] [÷R]`) and your 84 mm **Fraction Towers** (`[g] [SIMP]`), training you to combine and simplify fractions in your head as smoothly as whole numbers.

Let's start with a division puzzle that doesn't come out even: $17 \div 5$. Take 17 tiles from your **24-Tile Counting & Array Studio** and stack them into columns of 5. You build 3 complete 5-towers ($15$ tiles), with 2 leftover tiles resting in your hand ($\text{Quotient} = 3, \text{Remainder} = 2$). For `17 [ENTER] 5 [g] [÷R] ?`, tap `3 [ENTER]` (aim for under $< 3.5\text{ seconds}$). Running `17 [ENTER] 5 [g] [÷R]` on the stack produces **`3`**:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `17` | 0 | 0 | 0 | 17 |
| `[ENTER]` | 0 | 0 | 17 | 17 |
| `[5]` | 0 | 0 | 17 | 5 |
| `[g] [÷R]` | 0 | 0 | 2 | 3 |

*(Register $X$ holds quotient 3, Register $Y$ holds remainder 2; tap `[x⇄y]` to inspect the remainder).*

Next, the flight deck switches to fraction towers with $1/2 + 1/4 = {?}$. Bring out your **Fraction Towers** and slide them into the twin comparator well: a single $1/2$ tower stands at the exact same height as two $1/4$ pieces ($2/4$). Stacking one more $1/4$ piece on top builds a $3/4$ tower ($2/4 + 1/4 = 3/4$). When `1/2 [ENTER] 1/4 [+] ?` is shown, enter `[.] 3 [.] 4 [ENTER]` within $< 3.0\text{ seconds}$. You can verify that fraction tower height in `[NUM]` mode on the stack with `. 1 . 2 [ENTER] . 1 . 4 [+]`, which yields **`3/4`**: keying `[.] 1 [.] 2` places `1/2` into Ground Shelf $X$, pressing `[ENTER]` lifts `1/2` onto Waiting Shelf $Y$, typing `[.] 1 [.] 4` loads `1/4` onto Ground Shelf $X$ ($Y = 1/2,\; X = 1/4$), and tapping `[+]` fuses the half and quarter into `3/4` on Ground Shelf $X$.

What happens when you subtract two fractions and the leftover tower can be traded for a simpler block, as in $5/6 - 1/3 = {?}$? Stand five $1/6$ pieces ($5/6$) next to a $1/3$ piece in your **Fraction Towers** studio. Because the $1/3$ piece matches two $1/6$ blocks ($2/6$), taking away two sixths from five sixths leaves three $1/6$ blocks ($3/6$)—which stands the exact same height as a single $1/2$ tower! For `5/6 [ENTER] 1/3 [-] ?`, key in `[.] 1 [.] 2 [ENTER]` in under $< 3.5\text{ seconds}$. Evaluating `. 5 . 6 [ENTER] . 1 . 3 [-] [g] [SIMP]` on the stack reduces the difference to **`1/2`**:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[.] 5 [.] 6` | 0 | 0 | 0 | 5/6 |
| `[ENTER]` | 0 | 0 | 5/6 | 5/6 |
| `[.] 1 [.] 3` | 0 | 0 | 5/6 | 1/3 |
| `[-]` | 0 | 0 | 0 | 3/6 |
| `[g] [SIMP]` | 0 | 0 | 0 | 1/2 |

With two fast answers in Band 1, the simulator promotes you to Band 2 of Level 4, where neither denominator divides evenly into the other: $2/3 + 1/4 = {?}$. Reach for the twelfths pieces in your **Fraction Towers** kit: two $1/3$ pieces match eight $1/12$ pieces ($8/12$), and one $1/4$ piece matches three $1/12$ pieces ($3/12$). Stacking them together gives $8 + 3 = 11$ twelfths ($11/12$). On `2/3 [ENTER] 1/4 [+] ?`, press `[.] 11 [.] 12 [ENTER]` (target time: $< 4.0\text{ seconds}$). Checking on the stack with `. 2 . 3 [ENTER] . 1 . 4 [+]` confirms **`11/12`** as `[.] 2 [.] 3 [ENTER]` parks `2/3` on Shelf $Y$, `[.] 1 [.] 4` loads `1/4` onto Shelf $X$, and `[+]` aligns both fractions over their common denominator of 12 to display `11/12` on Ground Shelf $X$.

Sometimes the fastest move in Level 4 is shrinking a big fraction down to its simplest building blocks, like $\text{Simplify } 18/24 \to {?}$. Build two **Prime Factor Block** towers or group your **24 Array Tiles**: 18 is three groups of 6 ($3 \times 6$), and 24 is four groups of 6 ($4 \times 6$). Dividing both top and bottom by their Greatest Common Factor ($\text{GCF} = 6$) simplifies $18/24$ right down to $3/4$. For `18/24 [g] [SIMP] ?`, enter `[.] 3 [.] 4 [ENTER]` within $< 3.0\text{ seconds}$. Pressing `. 18 . 24 [ENTER] [g] [SIMP]` on the stack simplifies the ratio directly to **`3/4`**—keying `[.] 18 [.] 24 [ENTER]` copies `18/24` into both $Y$ and $X$, and tapping `[g] [SIMP]` divides out the shared factor of 6 so Ground Shelf $X$ shows `3/4` right alongside the original `18/24` on Waiting Shelf $Y$.

For our final Level 4 challenge before level-up, watch what happens when two fraction towers grow taller than $1$ whole in $5/8 + 1/2 = {?}$! In your **Fraction Towers** comparator well, a $1/2$ tower matches four $1/8$ pieces ($4/8$). Adding five $1/8$ pieces makes nine $1/8$ pieces ($9/8$), which stands 1 full whole tower tall plus 1 extra eighth ($1\ 1/8$). On `5/8 [ENTER] 1/2 [+] ?`, press `1 [.] 1 [.] 8 [ENTER]` (target time: $< 4.0\text{ seconds}$). Verifying on the stack with `. 5 . 8 [ENTER] . 1 . 2 [+]` yields **`1 1/8`**:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[.] 5 [.] 8` | 0 | 0 | 0 | 5/8 |
| `[ENTER]` | 0 | 0 | 5/8 | 5/8 |
| `[.] 1 [.] 2` | 0 | 0 | 5/8 | 1/2 |
| `[+]` | 0 | 0 | 0 | 1 1/8 |

---

### 8.3.5 Level 5: Multi-Step Order of Operations, Decimals & Percents
You have reached Level 5! Now the Quiz Engine mixes two-step expressions with mixed numbers so your brain learns to spot which operation must happen *first* before combining the pieces.

Look at our first Level 5 prompt, $24 \div 6 + 7 = {?}$: if you added $6 + 7 = 13$ first, you wouldn't even be able to divide $24$ evenly! Use all **24 Array Tiles** from your kit: because division happens before addition, first split the 24 tiles into 6 equal rows of 4 tiles ($24 \div 6 = 4$), and then bring in 7 counters from your **Ten-Frame Tray** to finish with 11 ($4 + 7 = 11$). When `24 ÷ 6 + 7 = ?` appears, tap `11 [ENTER]` (aim for under $< 2.5\text{ seconds}$). Evaluating `24 [ENTER] 6 [÷] 7 [+]` on the stack confirms **`11`**:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `24` | 0 | 0 | 0 | 24 |
| `[ENTER]` | 0 | 0 | 24 | 24 |
| `[6]` | 0 | 0 | 24 | 6 |
| `[÷]` | 0 | 0 | 0 | 4 |
| `[7]` | 0 | 0 | 4 | 7 |
| `[+]` | 0 | 0 | 0 | 11 |

Next comes the classic trap that catches anyone who reads strictly left-to-right: $15 - 3 \times 4 = {?}$ (where reading left-to-right gives $15 - 3 = 12$, times $4 = 48$—wrong!). Set out 15 tiles from your **24 Array Tiles**: because multiplication is a package deal, you must first group $3 \times 4 = 12$ of those tiles into a rectangle and lift that whole rectangle away from the 15 tiles, leaving $15 - 12 = 3$ tiles! Notice how the RPN stack handles this naturally without parentheses: for `15 - 3 × 4 = ?`, key in `3 [ENTER]` in under $< 2.5\text{ seconds}$, and verify in `[NUM]` mode by running `15 [ENTER] 3 [ENTER] 4 [×] [-]` on the stack to land on **`3`**. As you type `15 [ENTER] 3 [ENTER] 4`, your starting `15` rides safely up to Floor $Z$ while `3` and `4` sit on Floors $Y$ and $X$; tapping `[×]` fuses $3 \times 4$ into `12` on Floor $X$ and drops `15` back down into Floor $Y$, so one final tap of `[-]` subtracts $15 - 12$ to leave `3` on Ground Shelf $X$.

What happens when parentheses wrap around the subtraction, like $(18 - 6) \div 3 = {?}$? Parentheses mean *"handle this box of tiles first!"* From 18 of your **24 Array Tiles**, remove 6 tiles to leave 12 tiles ($18 - 6 = 12$), and then share those 12 tiles equally into 3 rows of 4 ($12 \div 3 = 4$). On `(18 - 6) ÷ 3 = ?`, press `4 [ENTER]` (target time: $< 2.5\text{ seconds}$). In `[NUM]` mode, keying `18 [ENTER] 6 [-] 3 [÷]` produces **`4`**:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `18` | 0 | 0 | 0 | 18 |
| `[ENTER]` | 0 | 0 | 18 | 18 |
| `[6]` | 0 | 0 | 18 | 6 |
| `[-]` | 0 | 0 | 0 | 12 |
| `[3]` | 0 | 0 | 12 | 3 |
| `[÷]` | 0 | 0 | 0 | 4 |

Level 5 also mixes whole numbers and fractions together, like $1\ 1/2 + 2\ 1/4 = {?}$. When you see mixed numbers on the flight display, stack your **Fraction Towers** in two quick steps: first combine the whole towers ($1 + 2 = 3$), then combine the fractional pieces ($1/2 = 2/4$, plus $1/4$ gives $3/4$) to reach $3\ 3/4$. When `1 1/2 [ENTER] 2 1/4 [+] ?` is shown, tap `3 [.] 3 [.] 4 [ENTER]` (aim for under $< 3.5\text{ seconds}$). Verifying on the stack with `1 . 1 . 2 [ENTER] 2 . 1 . 4 [+]` yields **`3 3/4`**: keying `[1] [.] 1 [.] 2 [ENTER]` lifts `1 1/2` onto Waiting Shelf $Y$, typing `[2] [.] 1 [.] 4` loads `2 1/4` onto Ground Shelf $X$, and pressing `[+]` unites the whole units and fourths into `3 3/4` on Ground Shelf $X$.

One more order-of-operations check locks in your Level 5 promotion: $8 + 4 \times 5 = {?}$! Resist the urge to add $8 + 4$ first: build the $4 \times 5 = 20$ rectangle using 20 of your **24 Array Tiles** (or fill both **Ten-Frame Trays**), then add 8 more counters to get $20 + 8 = 28$. For `8 + 4 × 5 = ?`, press `28 [ENTER]` (target time: $< 2.5\text{ seconds}$). Evaluating `8 [ENTER] 4 [ENTER] 5 [×] [+]` on the stack confirms **`28`**:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[8]` | 0 | 0 | 0 | 8 |
| `[ENTER]` | 0 | 0 | 8 | 8 |
| `[4]` | 0 | 0 | 8 | 4 |
| `[ENTER]` | 0 | 8 | 4 | 4 |
| `[5]` | 0 | 8 | 4 | 5 |
| `[×]` | 0 | 0 | 8 | 20 |
| `[+]` | 0 | 0 | 0 | 28 |

---

### 8.3.6 Level 6: Pre-Algebra & Competitive Speed Sprints
Congratulations—you have unlocked **Level 6 (`L6: Math Champ`)**, the highest tier on the SC-6! Here signed integer zero-pairs (`[+/-]`), prime factor intersections (`[GCF]` and `[f] [LCM]`), and mental math number-sense shortcuts come together for championship-speed sprints.

First, the championship deck tests your signed-number reflexes with $-14 + 9 = {?}$. Picture the hot-air balloon and sandbags (or two-color counters) from Chapter 07! Place 14 red negative counters (`-1` sandbags) and 9 yellow positive counters (`+1` flame puffs) in your two **Ten-Frame Trays**. Nine positive counters cancel 9 negative counters into zero-pairs, leaving 5 red negative counters ($-5$). On `-14 [ENTER] 9 [+] ?`, key in `5 [+/-] [ENTER]` in under $< 1.8\text{ seconds}$. Running `14 [+/-] [ENTER] 9 [+]` on the stack lands on **`-5`**:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `14` | 0 | 0 | 0 | 14 |
| `[+/-]` | 0 | 0 | 0 | $-14.0000$ |
| `[ENTER]` | 0 | 0 | $-14.0000$ | $-14.0000$ |
| `[9]` | 0 | 0 | $-14.0000$ | 9 |
| `[+]` | 0 | 0 | 0 | $-5.0000$ |

For our final championship sprint challenge, find the largest shared building block between $24$ and $36$ when the screen prompts for the GCF of $24$ and $36$. Stand up two prime factor towers using your **Prime Factor Blocks**: $24 = 2 \times 2 \times 2 \times 3$ and $36 = 2 \times 2 \times 3 \times 3$. Pull out the blocks both towers share—two $2$-blocks and one $3$-block—and multiply them in your head: $2 \times 2 \times 3 = 12$. For `24 [ENTER] 36 [GCF] ?`, press `12 [ENTER]` (target time: $< 1.8\text{ seconds}$). Verifying on the stack with `24 [ENTER] 36 [GCF]` confirms **`12`**:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `24` | 0 | 0 | 0 | 24 |
| `[ENTER]` | 0 | 0 | 24 | 24 |
| `36` | 0 | 0 | 24 | 36 |
| `[GCF]` | 0 | 0 | 0 | 12 |

*(Bonus `[f] [LASTX]` move: Because `[GCF]` saved `36` inside `LASTX`, tapping `24 [f] [LASTX] [f] [LCM]` right afterward checks the matching Least Common Multiple `72` without re-typing `36`—completing your six-level simulator flight with every streak dot glowing across the cockpit display!)*

---

## 8.4 How Streaks, Mastery Bars & Automatic Level-Ups Work

How does the SC-6 know when you are ready to graduate from warm-up questions to tougher puzzles, or unlock the next level altogether? It watches two things at once—your **steady mastery bar** and your **5-dot speed streak** (`●●●○○`):

| Quiz Event & Response Time | LCD Feedback Banner | Mastery Point Delta | Fast Streak Effect |
| :--- | :--- | :--- | :--- |
| **Fast Correct (Under 4 seconds)** | `★ FAST!  <ans> (<time>s)` | **`+20%` Mastery** | Increments Fast Streak (`+1`, fills pip `●`) |
| **Good Correct (4 to 8 seconds)** | `✓ GOOD  <ans> (<time>s)` | **`+10%` Mastery** | Preserves current Fast Streak |
| **Steady Correct (Over 8 seconds)** | `OK  <ans> (<time>s)` | **`+5%` Mastery** | Resets Fast Streak to `0` |
| **Incorrect Submission** | `WRONG: <expected>` | **`-10%` Mastery** (min `0%`) | Resets Fast Streak to `0` (demotes band if Mastery $< 25\%$) |

### 8.4.1 Two Roads to the Next Level: Steady Climber or Speed Sprinter
Notice something wonderful about the table above: you don't have to be the fastest kid in the room on your very first try to level up! The SC-6 gives you two ways to advance—either by filling your **Mastery Bar to `100%`** at a steady pace, or by lighting up **all five streak dots (`●●●●●`)** in a row under 4 seconds each:
- **Band 1 $\to$ Band 2 Promotion:** Unlocks automatically when your `Mastery` reaches `35%` **or** you hit a `Fast Streak` of `2` (`●●○○○`).
- **Band 2 $\to$ Band 3 Promotion:** Unlocks automatically when your `Mastery` reaches `70%` **or** you hit a `Fast Streak` of `4` (`●●●●○`).
- **Next Level Advance (`★ NEXT LEVEL UNLOCKED! ★`):** Triggers the moment your `Mastery` hits `100%` **or** you complete a **5-Fast-Streak (`●●●●●`)**—five consecutive answers under $4.0\text{ seconds}$! On the very next prompt, the screen celebrates your promotion and lifts you to `Level + 1` (all the way up to `L6: Math Champ`).
- **Classroom Tournament Badges:** In team relays, players also earn streak badges across rounds—**Bronze Streak (3 fast)**, **Silver Streak (5 fast — automatic level advance)**, **Golden Master (10 fast)**, and the legendary **20-Streak Flawless Sprint**.

| Quiz Header (`[f] [?] LVL 3`) | Level Advance Banner & Solved Prompt | Stack Display (`Y` / `X`) |
| :--- | :---: | :--- |
| **`SCORE: 180`** • **`STREAK: 5 ●●●●●`** | **`★ NEXT LEVEL UNLOCKED! ★`** — **`8  ?  ×  =  56`** | **`Y: 8`**, **`X: 7`** *(Silver Streak achieved)* |

*Figure 8.2: Daylight LCD Frame: 5 Fast Streak Level Promotion in Level 3*

---

## 8.5 Walkthrough: Riding a 5-Streak Wave in Level 6

What does it feel like when your mental-math shortcuts and your fingers lock into a rhythm? Step into the cockpit for a real 5-problem sprint in **Level 6 (`L6: Math Champ`)** and watch how five tough-looking problems fall in under 8 seconds total:

| Sprint Prompt | Mental Math Strategy | Your Keystrokes | Elapsed Time & Score |
| :--- | :--- | :--- | :--- |
| **Prompt 1:** `35² = ?` | Multiply tens digit by $(\text{tens} + 1)$: $3 \times 4 = 12$; attach $25 \to 1225$ | `1225` `[ENTER]` | $1.8\text{ s}$ (`+20 pts`, `●○○○○`) |
| **Prompt 2:** `48 × 5 = ?` | Cut $48$ in half $\to 24$, then multiply by $10 \to 240$ | `240` `[ENTER]` | $1.4\text{ s}$ (`+20 pts`, `●●○○○`) |
| **Prompt 3:** `1000 - 647 = ?` | Complement from $999$: $(9-6)(9-4)(10-7) = 353$ | `353` `[ENTER]` | $1.7\text{ s}$ (`+20 pts`, `●●●○○`) |
| **Prompt 4:** `144 ÷ 12 = ?` | Picture the $12 \times 12 = 144$ square array $\to 12$ | `12` `[ENTER]` | $1.1\text{ s}$ (`+20 pts`, `●●●●○`) |
| **Prompt 5:** `25 × 16 = ?` | Four quarters make $100$: $16 \div 4 = 4$ hundreds $\to 400$ | `400` `[ENTER]` | $1.5\text{ s}$ (`+20 pts`, `●●●●●` **5-Streak Bonus `+25 pts`**) |

Not a single piece of scratch paper was needed—and the whole 5-problem wave took just $7.5\text{ seconds}$ of active thinking!

---

## 8.6 Classroom Sprint Stations, Relays & Tournament Games

You can play the SC-6 Quiz Engine solo on the bus, at the kitchen table, or with friends in a classroom math station. Here are three favorite ways to play:

### 8.6.1 Protocol 1: The 2-Minute Daily Personal-Best Sprint
Before starting your daily math lesson, set your SC-6 to your current level and run a focused 2-minute warmup sprint:
- **Duration:** Exactly 120 seconds on a kitchen timer or classroom clock.
- **Goal:** Beat *your own* personal best from yesterday—not anyone else's score.
- **Tracking:** Jot down your score, accuracy, and longest fast streak in your math logbook.
- **Why It Works:** Just like a musician playing two minutes of scales before rehearsal, it wakes up your number sense in 120 seconds flat.

| Date | Target Level | Final Score | Fast Streak | Personal Best? |
| :--- | :--- | :--- | :--- | :--- |
| **Oct 14** | Level 3 ($\times/\div$) | `140` | `4` | No |
| **Oct 15** | Level 3 ($\times/\div$) | `180` | `6` | **Yes** |
| **Oct 16** | Level 3 ($\times/\div$) | `210` | `8` | **Yes** |
| **Oct 17** | Level 4 (Fractions) | `90` | `2` | New Level |

---

### 8.6.2 Protocol 2: The 4-Player Baton Relay
Turn mental math into a team sport with four players and a single SC-6 as the relay baton:
1. Four teammates sit in a row with one SC-6 calculator in the middle of the table.
2. Player 1 launches Quiz Mode and aims for a **3-Fast-Streak (`●●●○○`)** before passing the calculator to Player 2.
3. If a player enters a wrong answer, their streak resets to zero—and their teammates can coach them using the physical blocks on the table until they hit their 3-streak!
4. Player 2 earns 3 more streak dots and passes to Player 3, who passes to Player 4.
5. The team clock stops the instant Player 4 locks in the final 3-streak (12 fast answers across the team).

---

### 8.6.3 Protocol 3: Starting Fresh with a Clean Scoreboard
Before a head-to-head race or team relay, you can clear out old scores and registers so every player starts from a brand-new baseline:
1. Hold down the clear key `[C]`.
2. Momentarily tap `[g] [OFF]`.
3. Release `[C]`.
4. The screen briefly announces: `"MEMORY CLEARED - ALL REGISTERS PURGED"`.
5. All four stack floors ($X, Y, Z, T$) and your quiz scoreboard reset cleanly to zero.

---

### 8.6.4 Why the SC-6 Quiz Mode Builds Real Confidence

- **Private, Low-Stress Practice:** Timed paper tests on a classroom wall chart can make anyone feel nervous. On the SC-6, your practice is private and encouraging. When you miss a problem, the screen simply invites you to try again and brings that fact back a few questions later so you can conquer it. Even when you turn the calculator off (`[g] [OFF]`), it remembers your completed levels, high scores, and review questions.
- **Accuracy Beats Guessing:** The scoring rules reward steady thinking over wild guessing: answering correctly within $4.0\text{ seconds}$ (`★ FAST!`) earns $+20\%$ mastery and builds your streak toward advancing to the next level, while answering in $4.0\text{--}8.0\text{ seconds}$ (`✓ GOOD`) earns $+10\%$ mastery. Because a wrong guess costs $-10\%$ mastery and resets your streak, taking an extra second to think through the blocks in your head always wins.
- **Mental Math & Number Sense Fluency:** Level 6 (`L6: Math Champ`) trains mental math shortcuts—multiplying by 11, 25, 37, 101, and 125, squaring numbers ending in 5 ($35^2 = 3 \times 4\text{ hundred} + 25 = 1,225$), summing number patterns, and combining unit fractions.

### 8.6.5 Three Secrets for High-Score Quiz Sprints

1. **Why Guessing Hurts Your Score:** Each wrong guess deducts $-10$ points and resets your fast streak to zero, whereas taking an extra second to think through $7 \times 8 = 56$ within $4.0\text{ seconds}$ earns $+20$ points and builds your streak toward automatic level promotion. Ten accurate answers ($200\text{ points}$) beat forty wild guesses every time.
2. **The One-Second $\times 11$ Shortcut:** To multiply any two-digit number like $53 \times 11$ in your head, split the digits apart (`5 _ 3`) and put their sum ($5 + 3 = 8$) right in the middle: **$583$**. For $42 \times 11$, $4 + 2 = 6$ gives **$462$**. If the middle sum is $10$ or more—like $75 \times 11$ where $7 + 5 = 12$—place the `2` in the middle and carry the `1` to the left digit ($7 + 1 = 8$) to get **$825$** (verify with `10 [ENTER] 7 [-]`).
3. **Adding Fractions in Level 4 ($\frac{1}{3} + \frac{1}{4}$):** Never add denominators straight across ($\frac{1}{3} + \frac{1}{4} \ne \frac{2}{7}$). Stack a $\frac{1}{3}$ tower and a $\frac{1}{4}$ tower in your Fraction Studio: both convert cleanly into twelfths ($\frac{4}{12} + \frac{3}{12} = \frac{7}{12}$). Enter `[.] 7 [.] 1 2 [ENTER]` to score the full $+20$ points.

If a tricky quiz prompt ever catches you by surprise, this quick reference table shows the physical block picture behind each common pitfall:

| What Happened on Your Screen | Why It Happened | How to Fix It |
| :--- | :--- | :--- |
| **Adding denominators in Level 4: $\frac{2}{5} + \frac{1}{5} = \frac{3}{10}$** | Treating fractions as two disconnected whole numbers rather than equal fractional parts. | *"Look at the fraction tower manipulative. If you have 2 fifths and add 1 fifth, you have 3 fifths ($\frac{3}{5}$). The denominator tells you the size of the pieces; it never changes when adding like slices."* |
| **Forgetting to carry in the 11s shortcut: $68 \times 11 = 6148$** | Inserting the full sum $6 + 8 = 14$ into the center without regrouping the tens digit. | *"The center slot can only hold a single digit. Put the 4 in the middle, and carry the 1 over to the 6: $6 + 1 = 7$, yielding 748."* |
| **Squaring numbers ending in 5: $35^2 = 3025$** | Multiplying the tens digit by itself ($3 \times 3 = 9$) instead of the next integer ($3 \times 4 = 12$). | *"Remember the rule: multiply the tens digit by the NEXT whole number ($3 \times 4 = 12$), then append 25 to get 1,225."* |
| **Order of operations violation: $24 \div 6 + 7 = 24 \div 13$** | Reading left-to-right and adding before dividing. | *"Division and multiplication always happen before addition and subtraction. First compute $24 \div 6 = 4$. Then add $4 + 7 = 11$."* |
| **Sign confusion: $-15 + 8 = -23$** | Adding absolute values instead of moving toward zero on the number line. | *"You are at $-15$ in the basement. Going up $+8$ floors moves you CLOSER to ground level: you end at Floor $-7$."* |
| **Remainder as decimal: $17 \div 5 \to 3.2$ instead of $\text{Quotient} = 3, \text{Remainder} = 2$** | Confusing base-10 tenths with fractional parts ($2/5 = 0.4$, not $0.2$). | *"In whole number division with remainder, $17 \div 5$ gives 3 groups of 5 with 2 left over. On the SC-6, use `[g] [÷R]` to see quotient $3$ and remainder $2$ separated."* |
| **Doubles error: $7 + 8 \to 16$** | Misapplying double of the upper addend ($8 + 8 = 16$) instead of double plus one ($7 + 7 + 1 = 15$). | *"Think of 8 as $7 + 1$. Double 7 is 14, plus 1 is 15. Double plus one always gives an odd sum."* |
| **Percentage of number: $10\%\text{ of } 250 = 2500$** | Multiplying by 10 instead of dividing by 10 (or moving decimal wrong way). | *"Ten percent means ten out of one hundred—one tenth. To take one tenth of 250, shift the decimal point ONE space to the LEFT: $25.0$."* |

---

## 8.7 Mental Math & Number Sense Fluency: 8 Mental Math Shortcuts for Fast Calculation

Have you ever watched someone multiply two two-digit numbers in their head in two seconds and wondered if they had a secret superpower? Real mathematicians don't memorize giant multiplication tables up to $100 \times 100$—instead, they rearrange rectangles and place-value blocks in their heads! Here are eight favorite mental math shortcuts, along with the physical "why" behind each one so you can see the pattern for yourself:

### 8.7.1 Multiplying Two Numbers with the Same Tens Digit and Ones That Add to 10
When two numbers start with the **same tens digit** (like the $4$ in $43$ and $47$) and their **ones digits add up to 10** ($3 + 7 = 10$):
- **How Does This Trick Work?** Picture a $43 \times 47$ rectangle of tiles split at $40$. Inside, you have a big $40 \times 40$ square, two side strips ($40 \times 3$ and $40 \times 7$), and a tiny $3 \times 7$ corner. Because both side strips are $40$ tiles long and their widths add up to $3 + 7 = 10$, those two strips snap together into one full $40 \times 10$ bar! Adding that $40 \times 10$ bar onto the $40 \times 40$ square gives a clean $40 \times 50 = 2,000$ rectangle ($4 \times 5 = 20\text{ hundreds}$), plus the tiny $3 \times 7 = 21$ corner!
- **Word Rule:** $\text{First Two Digits} = \text{Tens Digit} \times (\text{Next Whole Number})$, and $\text{Last Two Digits} = \text{First Ones Digit} \times \text{Second Ones Digit}$.
- *Example ($43 \times 47$):*
  - Multiply the tens digit $4$ by the next whole number $5$: $4 \times 5 = 20$ ($20\text{ hundreds} = 2,000$).
  - Multiply the ones digits together: $3 \times 7 = 21$.
  - Put them side by side: **2,021**, which you can verify in an instant on the stack with `43 [ENTER] 47 [×]` $\to \mathbf{2021.00}$.
  - *Special Case — Squaring Any Number Ending in 5 (like $35^2$):* Because $35 \times 35$ has the same tens digit ($3$) and its ones digits add up to $5 + 5 = 10$, the exact same rule applies! Multiply $3$ by the next whole number $4$ ($3 \times 4 = 12\text{ hundreds} = 1,200$) and attach $5 \times 5 = 25$ to get **1,225**—which you can verify on the stack via `6 [ENTER] 3 [+]`.

### 8.7.2 Fast Multiplication by 25 (The Four-Quarters Trick)
Because $4$ quarters make $100$ cents ($25 = 100 \div 4$), multiplying any number by $25$ is the same as **dividing by 4 and multiplying by 100**:
- **How Does This Trick Work?** Imagine dumping $36$ quarters onto the kitchen table. Counting by $25$s thirty-six times would take forever! Instead, stack the coins into little piles of $4$ quarters each, because every stack of $4$ quarters equals $1$ whole dollar ($100\text{ cents}$). Since $36 \div 4 = 9$ stacks, you immediately see $9$ dollars, or $900\text{ cents}$!
- **Word Rule:** $\text{Number} \times 25 = (\text{Number} \div 4) \times 100$.
- *Example ($36 \times 25$):*
  - Divide $36$ into $4$ equal quarters: $36 \div 4 = 9$.
  - Multiply by $100$: **900**, matching `36 [ENTER] 25 [×]` $\to \mathbf{900.00}$ on your SC-6.

### 8.7.3 Squaring Numbers Just Above 50
To square a number in the fifties (like $54 \times 54$), ask how many steps it sits above $50$ ($54$ is $4$ steps above $50$):
- **How Does This Trick Work?** Picture a $54 \times 54$ square split into four sections at $50$: a big $50 \times 50 = 2,500$ square ($25\text{ hundreds}$), two matching side strips of $50 \times 4$, and a small $4 \times 4 = 16$ corner square. When you lay the two $50 \times 4$ strips end-to-end, two $50$s always join into $100$—making a $100 \times 4 = 400$ bar ($4\text{ hundreds}$)! That is why every step above $50$ simply adds $1\text{ hundred}$ onto $25\text{ hundreds}$, while the corner square supplies the last two digits!
- **Word Rule:** $\text{First Two Digits} = 25 + \text{Steps Above 50}$, and $\text{Last Two Digits} = \text{Steps Above 50} \times \text{Steps Above 50}$.
- *Example ($54^2$, which is $4$ steps above $50$):*
  - First two digits: $25 + 4 = 29$ ($2,900$).
  - Last two digits: $4 \times 4 = 16$.
  - Put them side by side: **2,916**, which you can check in a single keystroke with `54 [x²]` $\to \mathbf{2916.00}$.

### 8.7.4 Multiplying Neighbours Around a Round Number
When two numbers sit the exact same distance below and above a round tens number—like $28 \times 32$, which sit $2$ steps below and $2$ steps above $30$:
- **How Does This Trick Work?** On your **L-Frame Factoring Stage**, start with a $30 \times 30$ square of tiles ($900$) and remove a tiny $2 \times 2$ square ($4$) from one corner, leaving $900 - 4 = 896$ tiles. Now slice the remaining strip of width $2$ off the top edge and slide it onto the right edge: it fits flush to form a $28 \times 32$ rectangle!
- **Word Rule:** $\text{Product} = (\text{Center Number} \times \text{Center Number}) - (\text{Step Distance} \times \text{Step Distance})$.
- *Example ($28 \times 32$, centered at $30$ with step distance $2$):*
  - Square the center number: $30 \times 30 = 900$.
  - Subtract the squared step distance ($2 \times 2 = 4$): $900 - 4 = \mathbf{896}$, confirmed on the stack via `28 [ENTER] 32 [×]` $\to \mathbf{896.00}$.

### 8.7.5 Adding a Staircase of Whole Numbers Starting at 1
To add all the whole numbers from $1$ up to any ending number (like $1 + 2 + 3 + \dots + 20$):
- **How Does This Trick Work?** Build a staircase of $1 + 2 + 3 + 4 = 10$ **Counting Tiles** in Coral Red, and a second identical staircase of 10 tiles in Sky Cyan. Flip the Cyan staircase upside-down and snap it against the Red staircase: the two staircases lock together into a $4 \times 5 = 20$ rectangle! Because two staircases make a $\text{Last Number} \times \text{Next Whole Number}$ rectangle, a single staircase is always half of that rectangle ($20 \div 2 = 10$).
- **Word Rule:** $\text{Staircase Sum} = (\text{Last Number} \times \text{Next Whole Number}) \div 2$.
- *Example (Sum of numbers from 1 to 20):*
  - Multiply the last number ($20$) by the next whole number ($21$), then divide by $2$: $(20 \times 21) \div 2 = 10 \times 21 = \mathbf{210}$, which you can verify on the stack with `20 [ENTER] 21 [×] [2] [÷]` $\to \mathbf{210.00}$.

### 8.7.6 Adding a Staircase of Odd Numbers Starting at 1
Whenever you add the first several odd numbers starting at $1$ ($1 + 3 + 5 + 7 + \dots$), the sum is always a perfect square:
- **How Does This Trick Work?** Remember the L-shaped **Gnomon Square** you built in Chapters 03 and 04! Start with $1$ corner tile ($1 \times 1 = 1$). Wrap an L-shaped border of $3$ tiles around it and you get a $2 \times 2 = 4$ square. Wrap the next odd border of $5$ tiles around that and you get a $3 \times 3 = 9$ square! Every odd number adds one new row and one new column, plus $1$ corner tile, growing the square's side length by $1$ each time. So the sum of the first $12$ odd numbers ($1 + 3 + 5 + \dots + 23$) is simply a $12 \times 12 = \mathbf{144}$ square!
- **Word Rule:** $\text{Sum of Odd Numbers} = \text{How Many Odd Numbers} \times \text{How Many Odd Numbers}$, which `12 [x²]` $\to \mathbf{144.00}$ confirms in a single tap.

### 8.7.7 Turning Repeating Decimals into Fractions (The 9s and 99s Rule)
A decimal that repeats a single digit forever (like $0.777\dots$) is that digit over $9$ ($\frac{7}{9}$). A decimal that repeats a two-digit pattern forever (like $0.363636\dots$) is that two-digit number over $99$:
- **How Does This Trick Work?** Why do $9$s and $99$s make decimals echo forever? Imagine sharing $1$ whole block among $9$ friends on a decimal place-value mat ($1 \div 9$). First you trade $1$ whole for $10$ tenths: each friend gets $1$ tenth ($0.1$), leaving **$1$ tenth left over**. Trade that $1$ leftover tenth for $10$ hundredths: each friend gets $1$ hundredth ($0.01$), leaving **$1$ hundredth left over**! Because $9$ is exactly $1$ shy of $10$, every decimal place leaves the exact same remainder of $1$ forever ($\frac{1}{9} = 0.111\dots$, so $\frac{7}{9} = 0.777\dots$). And because $99$ is $1$ shy of $100$, dividing by $99$ leaves the same remainder every *two* decimal places ($\frac{1}{99} = 0.010101\dots$, so $\frac{36}{99} = 0.363636\dots$)!
- **Word Rule:** $\text{One Repeating Digit} = \frac{\text{Digit}}{9}$, and $\text{Two Repeating Digits} = \frac{\text{Two-Digit Pattern}}{99}$.
- *Example (Convert $0.363636\dots$ to simplest fraction):*
  - Write the repeating pattern over $99$: $\frac{36}{99}$.
  - Simplify by dividing top and bottom by $9$: $\frac{36 \div 9}{99 \div 9} = \mathbf{\frac{4}{11}}$, which you can verify directly in fraction mode with `[.] 36 [.] 99 [g] [SIMP]` $\to \mathbf{4/11}$.

### 8.7.8 The Alternating-Digit Test for Divisibility by 11
To check whether a big number divides evenly by $11$, add every other digit in two teams and subtract the two sums:
- **How Does This Trick Work?** Why do alternating digits play tug-of-war when you divide by $11$? Look at how close each place-value block sits to a multiple of $11$:
  - Each **ten** ($10$) is $1$ *short* of $11$ ($11 - 1$).
  - Each **hundred** ($100$) is $1$ *more* than $99$ ($9 \times 11 + 1$).
  - Each **thousand** ($1,000$) is $1$ *short* of $1,001$ ($91 \times 11 - 1$).
  Every time you step one column to the left, the leftover flips between $+1$ and $-1$! Grouping the $+1$ places into one team and the $-1$ places into the other team tells you immediately whether all the leftovers cancel out to $0$ (or a multiple of $11$).
- **Word Rule:** $(\text{Sum of 1st, 3rd, 5th Digits}) - (\text{Sum of 2nd, 4th Digits}) = 0 \text{ or a multiple of } 11$.
- *Example (Test $8,426$):*
  - First team of alternating digits (ones + hundreds): $6 + 4 = 10$.
  - Second team of alternating digits (tens + thousands): $2 + 8 = 10$.
  - Subtract the two teams: $10 - 10 = 0$. Because $0$ divides evenly by $11$, $8,426$ is a multiple of $11$, which `8426 [ENTER] 11 [g] [÷R]` confirms with quotient $X = \mathbf{766}$ and remainder $Y = \mathbf{0}$.

### 8.7.9 Why Typing Less Means Thinking More (`[f] [?]`)

Now that you have seen how mental math shortcuts rearrange blocks in your head, watch what happens when you solve a big subtraction puzzle like $1,000 - 647$ on an ordinary calculator versus solving it with a mental complement in `[f] [?]` Quiz Mode:

| Challenge / Equation | The Algebraic Calculator Trap (Standard Entry) | The StackCalc SC-6 + Manipulative Method | Keystroke Reduction | Live Stack Visibility | Learning Breakthrough |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Rapid Subtraction Complement**: $1000 - 647 = 353$ | Keying the full subtraction `1 0 0 0 - 6 4 7 =` takes **8 physical keystrokes**—and on paper, crossing out three zeros requires three separate column borrows. | **9s Complement Mental Shortcut:** subtract the hundreds and tens digits from 9, and the ones digit from 10: $(9-6)(9-4)(10-7) = \mathbf{353}$. In Quiz Mode, you type `3 5 3 [ENTER]` (**4 physical keystrokes**)—and in `[NUM]` mode, `1 0 0 0 [ENTER] 6 4 7 [-]` (8 physical keystrokes) verifies both numbers side by side. | **50% fewer strokes in Quiz Mode (4 vs. 8)** | In `[NUM]` verification, Register $Y$ holds `1000` while Register $X$ holds `647` before `[-]` confirms `353`. | Learners discover the base-10 complement rule ($999 + 1 = 1000$) using Place Value blocks, eliminating multi-column borrowing across zeros completely. |

---

## 8.8 Where to Go Next: Companion Workbook Quests & Kitchen-Table Challenges

> *For 29 additional worked problems with full 4-register stack tables, see Chapter 8 of the [SC-6 Elementary Companion Problem & Activity Workbook](../curriculum/sc6-elementary-companion-workbook.md).*

Ready to take your mental-math flight simulator skills into friendly competition? Here is how to pair the SC-6 Quiz Engine (`[f] [?]`) and your **Quest Scoreboard** with the [Big Ideas Math Middle School Supplement](../curriculum/big-ideas-middle-school-sc6-workbook.md) (**Units 1–10**), *Timed Proficiency Trials*, and *12-Unit Curriculum Guide*:
- **Workbook-to-Quiz Level Alignment:** Every worksheet in the [Big Ideas Math Middle School Supplement](../curriculum/big-ideas-middle-school-sc6-workbook.md) pairs physical block proofs with RPN stack verification. Warm up with **Quiz Levels 1–3** for Whole-Number Operations & Factoring (**Unit 1**), **Level 4** for Remainder Division & Fraction Towers (**Unit 2**), **Level 5** for Order of Operations, Decimals, Ratios & Percents (**Units 1, 2 & 3**), and **Level 6** for Signed Integers, GCF/LCM, Algebraic Expressions, Geometry, and Statistics (**Units 4–10**).

1. **The Synchronized Seed-Code Duel (Timed Proficiency Trials — Head-to-Head Sprint):** Grab a partner or family member with a second SC-6 (or take turns on one calculator after a reset). Both players enter the same Classroom Seed Code—try `42 [f] [?]`—so the Quiz Engine deals the exact same sequence of shuffled puzzles. Who can hit a 5-Fast-Streak (`●●●●●`) and advance to the next level first without a single `-10` penalty?
2. **The Ends-in-5 Beat-the-Calculator Trick (Big Ideas Middle School Supplement):** Challenge an adult at the dinner table: let them use a smartphone calculator while you solve $25^2, 35^2, 45^2, 65^2, 75^2,$ and $85^2$ purely in your head using the tens-partner rule: multiply the tens digit by the next higher whole number and attach $25$ at the end ($6 \times 7 = 42 \to 4,225$). Verify each win in one tap on your SC-6 with `[x²]`!
3. **The 4-Player Kitchen-Table Relay (Curriculum Guide Unit 8 & Student Workbook):** Set up your Math Dominoes, Ten-Frame Trays, and Fraction Towers on the table alongside one SC-6 in Quiz Mode. Each player must score a 3-Fast-Streak (`●●●○○`) before passing the calculator to the next teammate—and if someone gets stuck on a fraction or remainder puzzle, the team can model it with the blocks on the table before entering the answer!

---

## 8.9 Chapter Summary & Looking Ahead

Combining the hardware quiz mode (`[f] [?]`) with mental math strategies builds rapid arithmetic fluency across all six levels:

1. **Pure RPN Mental Representation:** You deciphered arithmetic questions presented as RPN stack puzzles on the daylight LCD.
2. **Instant Sprint Evaluation:** You mastered instant submission via the hardware test key (`[ENTER]`), getting immediate tactile and visual feedback on every attempt.
3. **The 6-Level Adaptive Ladder:** You advanced across number bonds, multi-digit operations, times tables, fraction remainders, and rapid pre-algebra shortcuts.
4. **Mental Math Signature Keys:** You applied the eight mental math shortcuts—from the 11s trick to squaring numbers that end in 5—reducing response times without scratch paper.

In **[Chapter 09: Applied Elementary STEM & Maker Labs](sc6/09-applied-stem-labs.md)**, you will take all your computational speed, geometric visualization, and fractional precision out into the real world. You will weigh 3D-printed blocks and slice $0.20\text{ mm}$ nozzle layers, time a swinging clock pendulum to find its 10-swing average, track solar-oven heating rates and bean sprout growth, scale kitchen recipes, launch tabletop catapults, compound bicycle and clock gear trains, and lift loads with hydraulic syringes. Grab your safety goggles—it's time to build!

---

# Chapter 9: Applied Elementary STEM & Maker Labs

## 9.1 The Kitchen-Table Invention Studio: Turning Numbers into Moving Machines, 3D Prints, and Science Labs

Picture the kitchen table on a rainy Saturday morning. In the center sits a spool of corn-based PLA filament, a pair of digital vernier calipers, a stopwatch, a length of string, the 3D-printed math blocks you have used throughout this book, and the solid, tactile form of your StackCalc SC-6 calculator. Outside, the rain taps against the glass; inside, the table is alive with invention.

For centuries, schoolchildren were told that mathematics was something that lived exclusively in the flat, monochrome world of paper workbooks—abstract symbols marching across ruled margins under the threat of a red grading pen. But mathematics was never meant to be trapped on paper. Mathematics is the hidden operating system of physical reality. It is the invisible scaffolding that allows a 3D printer nozzle heated to $215^\circ\text{C}$ to slice models into paper-thin $0.20\text{ mm}$ layers as it fabricates your **Counting Tiles** and **Planetary Geared Clock**. It is the steady rhythm discovered by Galileo Galilei in 1638 *([Galilei, 1638](sc6/appendix-c-formulas-and-conversions.md#cite-galilei1638))* that keeps a grandfather clock pendulum swinging back and forth in equal beats across centuries.

When you pick up the SC-6 in your workshop, you aren't just doing schoolwork—you are an engineer, a builder, and an inventor. In a hands-on maker studio, real mathematics is verified by whether your creation actually works—whether the 3D-printed planetary gears mesh smoothly, the 3D-printed layers stack to the exact millimeter, and the pendulum keeps steady time. With **Stack Math**, your numbers become as physical as the string pendulum and 3D-printed blocks on your desk: you push lengths and weights onto the stack, tap your operations, and watch your ideas turn into real machines that whir, tick, and run!

![Classroom Maker Space Clock: Precision 3D-Printed Geared Engineering](../assets/renders/clock-classroom-hero.png)

---

![Slicing a 1 cm (3 cm - 2 cm) 3D-printed block top into 0.02 cm layers = 50 layers](../assets/manuals/screenshots/sc6_stem_led_resistor.png)

**How 3D Printers Slice Models into Thin Layers:** Look at the SC-6 screen above. Suppose a 3D-printed block is $3\text{ cm}$ tall in total, and its solid base takes up the bottom $2\text{ cm}$. Subtracting `[3] [ENTER] [2] [-]` leaves $1\text{ cm}$ of height for the top section. When the 3D printer slices that $1\text{ cm}$ top section into horizontal plastic layers that are each $0.02\text{ cm}$ ($0.20\text{ mm}$) thick, dividing by `.02 [÷]` shows that the printer nozzle must lay down **`50` layers**!

## 9.2 Building Real Things: From Your 3D-Printed Manipulative Studios to the Number Stack

Grounded in Jerome Bruner's hands-on learning research *([Bruner, 1966](sc6/appendix-c-formulas-and-conversions.md#cite-bruner1966))*, every maker lab in this chapter follows a four-step engineering loop that connects your physical **StackCalc Manipulative Studios** directly to the 4-register stack:
1. **Physical Workshop (Build & Measure It):** Measure 3D printer filament with vernier calipers as you print a **Math Dominoes** or **Counting Tile** tray, turn the gears of your **Planetary Geared Clock** (`[🕒]`, `[f] [▸HR]`, `[g] [▸HMS]`), dial launch and solar tilt angles on your **Unit Circle Volvelle**, or stack **84 mm Fraction Towers** (`[a ᵇ/c]`, `[g] [a:b]`) beside your measuring cups.
2. **Sketches and Data Logs (Draw It):** Record your measurements, layer sketches, and trial tables in your lab notebook.
3. **The Number Stack (Calculate It):** Push your measurements onto the SC-6 stack ($X, Y, Z, T$), chaining geometry keys (`[x²]`, `[f] [√x]`, `[π]`), statistical accumulators (`[Σ+]`, `[f] [Σx]`, `[g] [x̄]`, `[g] [MAD]`, `[g] [CLΣ]`), percentage and currency keys (`[%]`, `[g] [%CHG]`, `[$]`), and `[f] [LASTX]` checks without parentheses.
4. **Maker Validation (Test It):** Snap the 3D-printed parts together, slice the 3D print, swing the pendulum, and verify that physical reality matches your stack prediction.

---

## 9.3 3D Printing Filament Mass, Infill & Spool Cost Estimation

Have you ever wondered how a 3D printer's slicing software knows—down to the gram and the penny—how much plastic your design will use before the nozzle even heats up? The secret is hidden right on the filament spool! Unwind a few centimeters of plastic filament and look closely at it: that flexible strand is really a long, thin **cylinder** (like a giant strand of plastic spaghetti). If you know the tiny circle area of its cut end and you know how many centimeters of strand the printer will unspool, multiplying $\text{Circle Area} \times \text{Length}$ tells you the exact cubic centimeters of plastic your print will use!

Standard 3D printing filament has a width (diameter) of $1.75\text{ mm}$, which means its radius from the center to the edge is half of that: $0.875\text{ mm}$, or $0.0875\text{ cm}$:
- **Circle Area of the Filament Strand:** $\text{Circle Area} = \pi \times \text{Radius} \times \text{Radius} = \pi \times (0.0875\text{ cm})^2 \approx 0.0240528\text{ cm}^2$
- **Plastic Volume:** $\text{Volume} = \text{Circle Area} \times \text{Length in cm}$
- **Part Weight (PLA):** $\text{Weight in grams} = \text{Volume} \times 1.24\text{ grams per cm}^3$
- **Part Cost:** $\text{Cost} = \text{Weight in grams} \times (\text{Spool Price} \div 1,000\text{ grams})$

![Double-Six Tactile Dominoes Set in Matte Slate](../assets/renders/dominoes-studio-stealth_black.png)

### 9.3.1 Estimating a 500 cm Print Model for Your Dominoes Studio Tray
Suppose your slicing software reports that printing a custom replacement lid or divider tray for your **Math Dominoes** (or a **Counting Tile** organizer) will pull $500\text{ cm}$ ($5.0\text{ meters}$) of filament off the spool. Your maker space uses a $\$20.00$ spool of Midnight Navy PLA ($1,000\text{ grams}$). Let's follow the plastic from strand to finished price tag in one continuous stack flow!

First, we find the circle area of the filament ($\pi \times \text{Radius}^2$) by entering the radius in centimeters (`[.] 0875`), squaring it with `[x²]` ($\mathbf{0.00765625\text{ cm}^2}$), and multiplying by $\pi$ via `[π] [×]` ($\approx \mathbf{0.0240528\text{ cm}^2}$). Second, while that tiny circle area sits on Register $X$, we stretch it along the $500\text{ cm}$ filament strand (`500 [×]`) to get a plastic volume of $\mathbf{12.02641\text{ cm}^3}$. Third, because every cubic centimeter of PLA weighs $1.24\text{ grams}$, multiplying by `1.24 [×]` reveals that our finished studio tray weighs **`14.91275`** ($\mathbf{14.91\text{ grams}}$). Finally, to price the part from a $\$20 / 1,000\text{ g}$ spool, keying `20 [ENTER] 1000 [÷]` places the unit cost of $\$0.02\text{ per gram}$ on Register $X$ while keeping your $14.91\text{ g}$ tray weight in Register $Y$, pressing `[×]` computes **`0.298255`**, and tapping `[$]` formats the price tag as **`$0.30`**:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `.0875` | 0 | 0 | 0 | $0.0875$ |
| `[x²]` | 0 | 0 | 0 | $0.007656$ |
| `[π] [×]` | 0 | 0 | 0 | $0.024053$ |
| `500 [×]` | 0 | 0 | 0 | $12.02641$ |
| `1.24 [×]` | 0 | 0 | 0 | $14.91275$ |
| `20 [ENTER]` | 0 | $14.91275$ | $20.00000$ | 20 |
| `1000 [÷]` | 0 | 0 | $14.91275$ | $0.02$ |
| `[×]` | 0 | 0 | 0 | $0.298255$ |
| `[$]` | 0 | 0 | 0 | $0.30$ |

What if your next print is a deeper storage bin to hold all your **Counting Tiles**, and the slicing software previews that the nozzle will unspool $1,200\text{ cm}$ ($12\text{ meters}$) of $1.75\text{ mm}$ filament (radius $= 0.875\text{ mm} = 0.0875\text{ cm}$)? First, finding the tiny circle area of the filament strand ($\pi \times \text{Radius}^2$) with `.0875 [x²] [π] [×]` produces **`0.02405 cm²`**, and stretching that circle along the $1,200\text{ cm}$ strand via `.02405 [ENTER] 1200 [×]` reaches **`28.86 cm³`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `.0875` | 0 | 0 | 0 | $0.0875$ | Enter filament radius in centimeters ($0.0875\text{ cm}$) |
| `[x²]` | 0 | 0 | 0 | $0.007656$ | Square the radius ($0.0875 \times 0.0875 = 0.00765625\text{ cm}^2$) |
| `[π]` | 0 | 0 | $0.007656$ | $3.141593$ | Enter $\pi$; stack lifts the squared radius into Register $Y$ |
| `[×]` | 0 | 0 | 0 | $0.024053$ | Multiply to find the filament circle area ($\approx 0.02405\text{ cm}^2$) |
| `1200` | 0 | 0 | $0.024053$ | 1200 | Enter the filament length ($1,200\text{ cm}$) |
| `[×]` | 0 | 0 | 0 | $28.863383$ | Multiply circle area by length to find plastic volume ($28.86\text{ cm}^3$) |

Register $X$ confirms that the storage bin uses $\mathbf{28.86\text{ cm}^3}$ of melted plastic—transforming a long, flexible cylinder of filament on the spool into a rigid geometric box on the build plate.

---

### 9.3.2 Infill Percentage Optimization
Why don't 3D printers make every block $100\%$ solid plastic inside? Just like honeybees build lightweight hexagonal combs inside a hive, a 3D printer builds strong outer walls and fills the inside with a $15\%$ honeycomb lattice!

You can feel this difference right in your hand by comparing a $20\text{ mm}$ ($2.0\text{ cm}$) calibration test cube against a hollow-infill block. Closing your vernier calipers across all three directions of the test cube confirms that its length, width, and height are each an exact $2\text{ cm}$. Evaluating the volume of the cube in cubic centimeters ($\text{Length} \times \text{Width} \times \text{Height}$) via `[2] [ENTER] [2] [×] [2] [×]` produces **`8.0 cm³`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[2]` | 0 | 0 | 0 | 2 | Enter cube length in centimeters ($2\text{ cm}$) |
| `[ENTER]` | 0 | 0 | 2 | 2 | Copy length into Register $Y$ |
| `[2]` | 0 | 0 | 2 | 2 | Enter cube width ($2\text{ cm}$) |
| `[×]` | 0 | 0 | 0 | 4 | Multiply length by width to get the bottom square area ($4\text{ cm}^2$) |
| `[2]` | 0 | 0 | 4 | 2 | Enter cube height ($2\text{ cm}$); lifts area into Register $Y$ |
| `[×]` | 0 | 0 | 0 | 8 | Multiply base area by height to find cube volume ($8.0\text{ cm}^3$) |

Register $X$ confirms a volume of $\mathbf{8.0\text{ cm}^3}$—the exact space occupied by eight $1\text{ cm}$ unit cubes stacked in a $2 \times 2 \times 2$ block. Because every cubic centimeter ($1\text{ cm}^3$) of corn-based PLA plastic weighs $1.24\text{ grams}$, printing that $8.0\text{ cm}^3$ block completely solid ($100\%$ infill) via `[8] [ENTER] 1.24 [×]` would weigh **`9.92 grams`** ($9.92\text{ grams}$). Subtracting the $3.1\text{-gram}$ weight of a hollow-infill **Counting Tile** via `9.92 [ENTER] 3.1 [-]` leaves **`6.82 g saved`**—saving $\mathbf{6.82\text{ grams}}$ on every single block while keeping the outer walls just as stiff and sturdy!

Now scale that honeycomb savings up to a larger $100\text{ cm}^3$ trophy base with $15\%$ infill:
- **Solid Block Weight:** $100\text{ cm}^3 \times 1.24\text{ g/cm}^3 = 124.0\text{ g}$.
- **Outer Shell Weight:** $20\text{ cm}^3$ solid outer walls ($20 \times 1.24 = 24.8\text{ g}$).
- **Inside Infill Weight:** $80\text{ cm}^3$ inside space filled to $15\%$: $80 \times 0.15 \times 1.24 = 14.88\text{ g}$.
- **Total Hollow-Infill Weight:** $24.8 + 14.88 = 39.68\text{ g}$.
- **Weight Saved:** $124.0 - 39.68 = 84.32\text{ g}$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `124` | 0 | 0 | 0 | 124 |
| `[ENTER]` | 0 | 0 | 124 | 124 |
| `24.8` | 0 | 0 | 124 | $24.8$ |
| `[ENTER]` | 0 | 124 | $24.8$ | $24.8$ |
| `80` | 0 | $124.0$ | $24.8$ | 80 |
| `[ENTER]` | $124.0$ | $24.8$ | 80 | 80 |
| `0.15 [×]` | $124.0$ | $124.0$ | $24.8000$ | 12 |
| `1.24 [×]` | $124.0$ | $124.0$ | $24.8000$ | $14.88$ |
| `[+]` | 124 | 124 | $124.0$ | $39.68$ |
| `[-]` | 124 | 124 | 124 | $84.32$ |
| `.02 [×]` | 124 | 124 | 124 | $1.6864$ |
| `[$]` | 124 | 124 | 124 | $1.69$ |

---

## 9.4 Batch Classroom Kit Production & Manufacturing Economics

What does it take to run your own miniature toy factory at home or in a classroom maker lab? When you print a complete 24-piece set of **Counting Tiles**, you aren't just using plastic from the spool—you are also paying for the electricity that keeps the printer's nozzle and build plate warm for hours! In this project, you step into the shoes of a manufacturing engineer to budget both the filament and the electricity for a full student kit.
- **How 3D Printers Slice $0.20\text{ mm}$ Layers:** A 3D printer builds objects from the bottom up by extruding thin horizontal layers of melted PLA plastic, each just $0.20\text{ mm}$ thick. To print a $14.4\text{ mm}$ tall two-tier block stack, dividing `14.4 [ENTER] 0.20 [÷]` (or clearing the decimal by multiplying both numbers by $100 \implies 1,440 \div 20$) shows that the printer nozzle must trace **$72$ horizontal layers**.

### 9.4.1 Manufacturing a Student Kit of 24 Counting Tiles
How much does the plastic cost to 3D print a complete student kit of 24 **Counting Tiles** (6 each of Coral Red, Amber Gold, Sky Cyan, and Indigo Purple)?
- Each $19.0\text{ mm} \times 19.0\text{ mm}$ interlocking tile ($7.0\text{ mm}$ visible step height, $8.85\text{ mm}$ overall with its stacking lip) uses approximately $3.1\text{ grams}$ of PLA.
- Multiplying the 24 tiles by $3.1\text{ g}$ via `24 [ENTER] 3.1 [×]` gives a total kit weight of $\mathbf{74.4\text{ grams}}$, multiplying by `.02 [×]` finds the raw plastic cost of $1.488$, and pressing `[$]` rounds the spool cost to **`$1.49`**.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `24` | 0 | 0 | 0 | 24 |
| `[ENTER]` | 0 | 0 | 24 | 24 |
| `3.1` | 0 | 0 | 24 | $3.1$ |
| `[×]` | 0 | 0 | 0 | $74.4$ |
| `[.] 02` | 0 | 0 | $74.4$ | $0.02$ |
| `[×]` | 0 | 0 | 0 | $1.488$ |
| `[$]` | 0 | 0 | 0 | $1.49$ |

---

### 9.4.2 Electrical Operating Costs & Machine Time
Now let's check the electric bill! A classroom 3D printer uses an average electrical power of $120\text{ Watts}$ ($0.120\text{ kilowatts}$). The 24-tile Counting Tile kit requires $4.5\text{ hours}$ to print, and the local electric rate is $\$0.15\text{ per kilowatt-hour (kWh)}$:
1. Electricity Used: $0.120\text{ kW} \times 4.5\text{ hours} = 0.54\text{ kWh}$.
2. Electricity Cost: $0.54 \times \$0.15 = \$0.081$ ($\sim \$0.08$).
3. Total Production Cost (Filament + Electricity): $\$1.49 + \$0.08 = \mathbf{\$1.57}$ for the entire 24-tile kit.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[.] 12` | 0 | 0 | 0 | $0.12$ |
| `[ENTER]` | 0 | 0 | $0.12$ | $0.12$ |
| `4.5` | 0 | 0 | $0.12$ | $4.5$ |
| `[×]` | 0 | 0 | 0 | $0.54$ |
| `[.] 15` | 0 | 0 | $0.54$ | $0.15$ |
| `[×]` | 0 | 0 | 0 | $0.081$ |
| `1.49 [+]` | 0 | 0 | 0 | $1.571$ |
| `[$]` | 0 | 0 | 0 | $1.57$ |

Once word spreads around school about your 3D-printing studio, the principal asks your team to print 50 gold award medals for the Friday STEM Fair! Weighing one finished sample medal on your digital scale shows that each medal uses $14.5\text{ grams}$ of plastic. With filament priced at $\$0.02$ per gram, how much will it cost to print all 50 medals? Evaluating the three-step cost calculation on the stack via `50 [ENTER] 14.5 [×] .02 [×] [$]` yields **`$14.50`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `50` | 0 | 0 | 0 | 50 | Enter total medals to print ($50\text{ medals}$) |
| `[ENTER]` | 0 | 0 | 50 | 50 | Copy medal count into Register $Y$ |
| `14.5` | 0 | 0 | 50 | $14.5$ | Enter weight of one medal ($14.5\text{ g}$) |
| `[×]` | 0 | 0 | 0 | 725 | Multiply to find total plastic weight ($50 \times 14.5 = 725\text{ g}$) |
| `.02` | 0 | 0 | 725 | $0.02$ | Enter filament cost per gram ($\$0.02/\text{g}$) |
| `[×]` | 0 | 0 | 0 | $14.5$ | Multiply weight by price per gram ($725 \times 0.02 = 14.50$) |
| `[$]` | $0.00$ | $0.00$ | $0.00$ | $14.50$ | Format result in currency mode |

Register $X$ displays $\$14.50$, showing that printing all 50 STEM fair medals costs just $\mathbf{\$14.50}$ in PLA filament—less than a single store-bought trophy!

To equip the rest of your 6-student Maker Club workbench, suppose your team orders a digital caliper and tool set listed at $\$56.00$ with a $30\%$ student discount (`56 [ENTER] 30 [%] [-] [$]` $\to$ **`$39.20`**) plus $7.5\%$ sales tax (`39.20 [ENTER] 7.5 [%] [+] [$]` $\to$ **`$42.14`**). Then, when the club's total 3D-printing supply bill comes to $\$124.80$, you split it equally among all $6$ members (`124.80 [ENTER] [6] [÷] [$]` $\to$ **`$20.80`**):

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `56 [ENTER]` | 0 | 0 | 56 | 56 | Enter regular tool price ($\$56.00$) |
| `30 [%]` | 0 | 0 | 56 | $16.8$ | Find $30\%$ discount ($\$16.80$); base $\$56$ stays in Register $Y$ |
| `[-] [$]` | $0.00$ | $0.00$ | $0.00$ | $39.20$ | Subtract discount and format as currency ($\$39.20$ sale price) |
| `7.5 [%]` | $0.00$ | $0.00$ | $39.20$ | $2.94$ | Find $7.5\%$ sales tax ($\$2.94$); $\$39.20$ stays in Register $Y$ |
| `[+] [$]` | $0.00$ | $0.00$ | $0.00$ | $42.14$ | Add sales tax for final tool checkout price ($\$42.14$) |
| `124.80 [ENTER] [6] [÷] [$]` | $0.00$ | $0.00$ | $42.14$ | $20.80$ | Split the $\$124.80$ supply bill among 6 students ($\$20.80$ each) |

The discounted tool set costs $\mathbf{\$42.14}$ after tax, and each club member pays $\mathbf{\$20.80}$ for the supply bill—all balanced to the penny on the four-register stack!

---

## 9.5 3D-Printer Layer Slicing & Height Checks

Have you ever seen a 3D-printed math block with a dark slate-gray base and bright gold numbers raised on top, even though the printer only has a single nozzle? Makers do this with a clever trick called a **filament color swap**: you let the printer finish the bottom base, pause the machine, load a second color of plastic, and let it print the remaining top layers! To set the pause at the exact right height, how do you know how many paper-thin $0.02\text{ cm}$ ($0.20\text{ mm}$) layers remain in the top section?

| Slicer Measurement | Example Value | What It Means |
| :--- | :--- | :--- |
| **Total Model Height** | $3.0\text{ cm}$ (or $9.0\text{ cm}$) | Full height from the printer bed to the top of the block |
| **Base Height Printed** | $2.0\text{ cm}$ (or $3.2\text{ cm}$) | Bottom section already finished before the color swap |
| **Layer Thickness** | $0.02\text{ cm}$ ($0.20\text{ mm}$) | Height of each single plastic ribbon laid down by the nozzle |

### 9.5.1 How Layer Slicing Works in Words
To find how many horizontal layers the printer needs for the top section of a model:
- **Step 1 (Remaining Height):** $\text{Remaining Height} = \text{Total Height} - \text{Base Height}$
- **Step 2 (Number of Layers):** $\text{Number of Layers} = \text{Remaining Height} \div \text{Layer Thickness } (0.02\text{ cm})$
- **Step 3 (Height Check with `[f] [LASTX]`):** Press `[f] [LASTX]` to bring back the $0.02\text{ cm}$ layer thickness without re-typing it, and press `[×]` to verify that $\text{Number of Layers} \times \text{Layer Thickness} = \text{Remaining Height}$!

---

### 9.5.2 Slicing the Top Section of a 3 cm Block (`50` Layers)

Remember the $3.0\text{ cm}$ block slicer screenshot we previewed at the opening of this chapter? Let's trace every shelf of that filament color swap in detail—and add a two-tap `[f] [LASTX]` height proof at the end! Suppose you are printing a $3.0\text{ cm}$ tall counting block trophy where the bottom $2.0\text{ cm}$ base is already printed in slate gray, and you want to print the remaining top section in radiant gold using $0.02\text{ cm}$ layers.

First, find the remaining height ($\text{Total Height} - \text{Base Height}$) by entering the total block height (`[3] [ENTER]`) and subtracting the base height (`[2] [-]`), which leaves $\mathbf{1.0\text{ cm}}$ in Register $X$. Next, divide by the $0.02\text{ cm}$ layer thickness (`[.] 02 [÷]`): Register $X$ displays **`50.0`**, showing that the printer nozzle must lay down **`50` layers** of gold filament. Finally, to prove that $50$ layers of $0.02\text{ cm}$ each rebuild the exact $1.0\text{ cm}$ top section without typing `0.02` a second time, press `[f] [LASTX]` (which recalls $0.02$ into Register $X$ and lifts $50.0$ into Register $Y$) and tap `[×]` to verify **`1.0`** ($50 \times 0.02\text{ cm} = \mathbf{1.0\text{ cm}}$):

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[3] [ENTER]` | 0 | 0 | 3 | 3 |
| `[2] [-]` | 0 | 0 | 0 | 1 |
| `.02 [÷]` | 0 | 0 | 0 | 50 |
| `[f] [LASTX]` | 0 | 0 | 50 | $0.02$ |
| `[×]` | 0 | 0 | 0 | 1 |

---

### 9.5.3 Slicing a Taller 9.0 cm Tower Above a 3.2 cm Base (`290` Layers)
Suppose you print a $9.0\text{ cm}$ tall **Fraction Tower** holder whose solid base takes up the bottom $3.2\text{ cm}$, using $0.02\text{ cm}$ layers for the upper walls. Subtracting the base height via `9 [ENTER] 3.2 [-]` leaves $\mathbf{5.8\text{ cm}}$ of upper wall height, dividing by `[.] 02 [÷]` shows that the nozzle must trace **`290.0 layers`**, and tapping `[f] [LASTX] [×]` immediately confirms that $290 \times 0.02\text{ cm}$ rebuilds the exact **`5.8 cm`** height.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[9] [ENTER]` | 0 | 0 | 9 | 9 |
| `3.2 [-]` | 0 | 0 | 0 | $5.8$ |
| `.02 [÷]` | 0 | 0 | 0 | 290 |
| `[f] [LASTX]` | 0 | 0 | 290 | $0.02$ |
| `[×]` | 0 | 0 | 0 | $5.8$ |

---

## 9.6 Timing a Swinging Clock Pendulum (Finding the 10-Swing Average)

Why does a grandfather clock keep the exact same steady beat whether its swinging weight is heavy brass or light wood—and what happens to the beat if you shorten the string to one-fourth of its original length? Over four hundred years ago, a young Galileo Galilei watched a bronze lamp swinging from a high ceiling and timed it against his own pulse. He discovered an amazing law of nature: the time a pendulum takes to swing back and forth depends on the **length of the string**, not on how heavy the weight is!

Because a single swing goes by so fast that your thumb on the stopwatch might be a tenth of a second early or late, real scientists time **10 complete back-and-forth swings** in a row and divide by $10$ to find the razor-sharp average time for a single swing:
- **Time for 1 Swing:** $\text{One-Swing Time} = \text{Total Time for 10 Swings} \div 10$
- **Swings per Minute:** $\text{Swings per Minute} = 60\text{ seconds} \div \text{One-Swing Time}$

![Clock Quadrant Concept: Pendulum Escapements and Harmonic Oscillation](../assets/renders/clock-quadrant-concept.png)

Look closely at the **Planetary Geared Clock** and its removable $90^\circ$ clock quadrants above: in a mechanical grandfather clock, a swinging pendulum releases one gear tooth on every tick, driving the $60\text{-minute}$ outer ring and $12:1$ planetary hour hand at a steady pace. By timing a string pendulum beside your Planetary Geared Clock dial, you can see how string length controls the beat of a clock!

### 9.6.1 Timing 10 Swings of a 100 cm (1-Meter) Pendulum
You tie a washer to a string that is $100\text{ cm}$ ($1.00\text{ meter}$) long from the knot to the center of the washer. Using a stopwatch, you and your lab partner time 10 complete back-and-forth swings:
$$\text{Stopwatch time for 10 swings} = 20.1\text{ seconds}$$

To find the average time for 1 swing ($\text{Total Time} \div 10$), enter your stopwatch time (`20.1 [ENTER]`) and divide by 10 swings (`10 [÷]`), which lands on $\mathbf{2.01\text{ seconds per swing}}$ in Register $X$. Next, to see how many swings happen in 1 full minute ($60 \div \text{One-Swing Time}$), type `60`, swap Registers $X$ and $Y$ with `[x⇄y]` so $60$ sits in Register $Y$ above $2.01$ in Register $X$, and press `[÷]` to display **`29.8507`** ($\sim \mathbf{29.85\text{ swings per minute}}$, almost $30$ full swings every minute!):

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `20.1 [ENTER]` | 0 | 0 | $20.1$ | $20.1$ |
| `10 [÷]` | 0 | 0 | 0 | $2.01$ |
| `60` | 0 | 0 | $2.01$ | 60 |
| `[x⇄y]` | 0 | 0 | 60 | $2.01$ |
| `[÷]` | 0 | 0 | 0 | $29.8507$ |

---

### 9.6.2 Testing a Shorter 25 cm Quarter-Length Pendulum
What happens if you shorten the string to $25\text{ cm}$ (one-fourth of a meter)? Most people guess it will swing four times as fast—let's test that guess with a stopwatch! When you time 10 full back-and-forth swings, it takes **$10.05\text{ seconds}$**:
1. Divide $10.05\text{ seconds}$ by $10$ swings: `10.05 [ENTER] 10 [÷]` $\longrightarrow \mathbf{1.005\text{ seconds per swing}}$ (about $1\text{ second}$ per round-trip swing!).
2. Compare the $100\text{ cm}$ swing time ($2.01\text{ s}$) to the $25\text{ cm}$ swing time ($1.005\text{ s}$): enter `2.01`, swap `[x⇄y]`, and press `[÷]` $\longrightarrow \mathbf{2.0}$. Shortening the string to one-fourth ($\frac{1}{4}$) of its original length made the pendulum swing **twice as fast** ($\sqrt{4} = 2$)!

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `10.05 [ENTER]` | 0 | 0 | $10.05$ | $10.05$ |
| `10 [÷]` | 0 | 0 | 0 | $1.005$ |
| `2.01` | 0 | 0 | $1.005$ | $2.01$ |
| `[x⇄y]` | 0 | 0 | $2.01$ | $1.005$ |
| `[÷]` | 0 | 0 | 0 | 2 |

---

## 9.7 Solar Oven Thermal Tracking & Efficiency Rates

How can an ordinary cardboard box lined with kitchen aluminum foil and clear plastic wrap trap enough sunshine to melt chocolate and marshmallows into gooey s'mores on a sunny afternoon? The shiny foil bounces extra sunlight into the box, the black paper at the bottom soaks up that light as heat, and the clear plastic window plus newspaper insulation trap the warm air inside like a greenhouse! In this lab, you track how many degrees Celsius your solar oven gains every single minute.

| Thermal Measurement | Word Rule | What It Means |
| :--- | :--- | :--- |
| **Temperature Rise** | $\text{Ending Temp} - \text{Starting Temp}$ | Total degrees Celsius gained inside the solar box |
| **Heating Time** | $\text{Minutes in the Sun}$ | How many minutes the solar oven sits in sunlight |
| **Heating Speed** | $\text{Temperature Rise} \div \text{Minutes}$ | Degrees Celsius gained each minute ($^\circ\text{C/min}$) |

### 9.7.1 Measuring Solar Heating Speed
Place your solar cooker in direct sunlight at noon. Your digital thermometer records:
- Starting Temperature at $0\text{ minutes}$: $22.5^\circ\text{C}$
- Ending Temperature at $25\text{ minutes}$: $78.0^\circ\text{C}$

Subtracting the starting temperature from the ending temperature with `78 [ENTER] 22.5 [-]` reveals a temperature rise of $\mathbf{55.5^\circ\text{C}}$, dividing by `25 [÷]` gives a heating speed of $\mathbf{2.22^\circ\text{C per minute}}$, and checking `[g] [%CHG]` via `22.5 [ENTER] 78 [g] [%CHG]` confirms a $\mathbf{+246.67\%}$ thermal increase.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `78` | 0 | 0 | 0 | 78 |
| `[ENTER]` | 0 | 0 | 78 | 78 |
| `22.5` | 0 | 0 | 78 | $22.5$ |
| `[-]` | 0 | 0 | 0 | $55.5$ |
| `25` | 0 | 0 | $55.5$ | 25 |
| `[÷]` | 0 | 0 | 0 | $2.22$ |

What if you angle the foil reflector flap on a smaller pizza-box solar oven so it catches even more direct noon rays? Suppose over a $15\text{-minute}$ sprint, the temperature inside your pizza-box solar oven climbs from $20^\circ\text{C}$ to $65^\circ\text{C}$. First, find the heating speed in degrees per minute (`65 [ENTER] 20 [-] 15 [÷]` $\to$ **`3.00 °C/min`**): subtracting the $20^\circ\text{C}$ starting temperature gives a $45^\circ\text{C}$ rise, and dividing by $15\text{ minutes}$ gives a brisk $\mathbf{3.00^\circ\text{C/min}}$. Next, check the percentage temperature boost with `[g] [%CHG]` (`20 [ENTER] 65 [g] [%CHG]` $\to$ **`+225.0%`**), confirming a $\mathbf{+225.0\%}$ jump over the starting temperature—plenty of solar warmth to melt chocolate squares onto graham crackers!

---

### 9.7.2 Thermal Insulation Retention Ratio
How well does your crumpled-newspaper insulation hold onto that heat when a cloud passes over? After reaching $78^\circ\text{C}$ (which is $78 - 22 = 56^\circ\text{C}$ warmer than the $22^\circ\text{C}$ shade), move your oven into the shade for 30 minutes. The thermometer reads $56^\circ\text{C}$ ($56 - 22 = 34^\circ\text{C}$ above the shade temperature):
- Total Heat Kept Inside: $\frac{56 - 22}{78 - 22} = \frac{34}{56} \approx \mathbf{60.71\%}$ kept inside.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `56` | 0 | 0 | 0 | 56 |
| `[ENTER]` | 0 | 0 | 56 | 56 |
| `22 [-]` | 0 | 0 | 0 | 34 |
| `78` | 0 | 0 | 34 | 78 |
| `[ENTER]` | 0 | 34 | 78 | 78 |
| `22 [-]` | 0 | 0 | 34 | 56 |
| `[÷]` | 0 | 0 | 0 | $0.6071$ |
| `100 [×]` | 0 | 0 | 0 | $60.71$ |

---

## 9.8 Catapult Trajectory Math & Projectile Launch Analysis

When you pull back the arm of a tabletop rubber-band catapult and launch a foam ball toward a floor target, why doesn't the ball land on the exact same millimeter every single time? Tiny differences in how your finger releases the lever create a small scatter of landing spots! By holding your **Unit Circle Volvelle** (or a $90^\circ$ quadrant from your **Planetary Geared Clock**) beside the catapult arm to set an exact $45^\circ$ launch angle, you can use `[Σ+]`, `[g] [x̄]`, and `[g] [MAD]` to measure both your center bullseye distance and how tightly grouped your shots are.

| Catapult Measurement | What You Measure | Role in the Experiment |
| :--- | :--- | :--- |
| **Pullback Angle** | $30^\circ, 45^\circ, 60^\circ$ | The launch angle you choose before releasing the arm |
| **Landing Distance** | Measured in $\text{cm}$ along a floor tape | The distance you enter into the calculator with `[Σ+]` |

### 9.8.1 Five-Trial Launch Average at $45^\circ$
Launch a foam ball 5 times at a $45^\circ$ pullback angle, measuring each landing distance in centimeters:
$$\text{Landing Distances}: 182\text{ cm},\ 195\text{ cm},\ 188\text{ cm},\ 201\text{ cm},\ 189\text{ cm}$$

Add each launch into the SC-6 statistical registers using `[Σ+]`:
1. Clear statistics: Press `[g] [CLΣ]`.
2. Enter Launch 1: `182 [Σ+]` $\longrightarrow \text{Count} = 1$.
3. Enter Launch 2: `195 [Σ+]` $\longrightarrow \text{Count} = 2$.
4. Enter Launch 3: `188 [Σ+]` $\longrightarrow \text{Count} = 3$.
5. Enter Launch 4: `201 [Σ+]` $\longrightarrow \text{Count} = 4$.
6. Enter Launch 5: `189 [Σ+]` $\longrightarrow \text{Count} = 5$.
7. Find the Average (Mean): Press `[g] [x̄]` $\longrightarrow X = \mathbf{191.00\text{ cm}}$.
8. Find the Mean Absolute Deviation ($\text{MAD}$): Press `[g] [MAD]` $\longrightarrow X = \mathbf{5.60\text{ cm}}$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[g] [CLΣ]` | 0 | 0 | 0 | 0 |
| `182 [Σ+]` | 0 | 0 | 0 | $1.0000$ |
| `195 [Σ+]` | 0 | 0 | 0 | $2.0000$ |
| `188 [Σ+]` | 0 | 0 | 0 | $3.0000$ |
| `201 [Σ+]` | 0 | 0 | 0 | $4.0000$ |
| `189 [Σ+]` | 0 | 0 | 0 | $5.0000$ |
| `[g] [x̄]` | 0 | 0 | 0 | $191.00$ |
| `[g] [MAD]` | 0 | 0 | $191.00$ | $5.60$ |

You can also run a quick 3-shot calibration check whenever you move your catapult to a new patio surface! Suppose firing 3 practice shots at the same pullback angle sends the foam ball landing at $150\text{ cm}$, $162\text{ cm}$, and $156\text{ cm}$. Dropping all three launches into your statistical basket with `[Σ+]` and pressing `[g] [x̄]` via `[g] [CLΣ] 150 [Σ+] 162 [Σ+] 156 [Σ+] [g] [x̄]` levels the three distances out to **`156.00 cm`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[g] [CLΣ]` | 0 | 0 | 0 | 0 | Clear the statistics registers |
| `150 [Σ+]` | 0 | 0 | 0 | 1 | Add Shot 1 ($150\text{ cm}$); screen shows count $= 1$ |
| `162 [Σ+]` | 0 | 0 | 0 | 2 | Add Shot 2 ($162\text{ cm}$); screen shows count $= 2$ |
| `156 [Σ+]` | 0 | 0 | 0 | 3 | Add Shot 3 ($156\text{ cm}$); screen shows count $= 3$ |
| `[g] [x̄]` | 0 | 0 | 0 | 156 | Compute the average (mean) landing distance ($156.00\text{ cm}$) |

How tightly grouped were those three practice shots ($150\text{ cm}, 162\text{ cm}, 156\text{ cm}$) around the $156.00\text{ cm}$ center? Shot 1 was $6\text{ cm}$ short, Shot 2 was $6\text{ cm}$ long, and Shot 3 landed right on the nose ($0\text{ cm}$). Since all three shots are still sitting in your statistical registers, one tap of `[g] [MAD]` via `[g] [CLΣ] 150 [Σ+] 162 [Σ+] 156 [Σ+] [g] [MAD]` returns **`4.00 cm`**—confirming that $(6 + 6 + 0) \div 3 = \mathbf{4.00\text{ cm}}$ of average spread from the bullseye!

---

### 9.8.2 Target Ring Landing Consistency
Will your catapult shots land inside a circular floor target centered at $190\text{ cm}$ with a radius of $15\text{ cm}$ (stretching from $175\text{ cm}$ to $205\text{ cm}$)?
Since your average landing distance is $191.00\text{ cm}$ and double the Mean Absolute Deviation is $2 \times 5.60\text{ cm} = 11.20\text{ cm}$, your landing zone runs from $191 - 11.20 = 179.80\text{ cm}$ to $191 + 11.20 = 202.20\text{ cm}$. Notice the neat `[f] [LASTX]` shortcut below: because subtracting $11.20$ automatically stores $11.20$ inside `[f] [LASTX]`, tapping `191 [f] [LASTX] [+]` finds the far edge without re-typing `11.20`. Every shot in this zone lands squarely inside the $175\text{ cm}$ to $205\text{ cm}$ target ring!

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `191 [ENTER]` | 0 | 0 | 191 | 191 |
| `5.60 [ENTER]` | 0 | 191 | $5.60$ | $5.60$ |
| `2 [×]` | 0 | 0 | 191 | $11.20$ |
| `[-]` | 0 | 0 | 0 | $179.80$ |
| `191` | 0 | 0 | $179.80$ | 191 |
| `[f] [LASTX] [+]` | 0 | 0 | $179.80$ | $202.20$ |

---

## 9.9 Plant Growth Tracking & Proportional Rate Analysis

Have you ever planted a bean seed in a clear cup by a sunny window and noticed that it seems to grow taller overnight? Plants grow too slowly for your eyes to see in real time, like the hour hand of a clock—but when you measure the stem height in millimeters every two days, the stack lets you calculate its exact **growth speed in millimeters per day**!

| **14-Day Botany Log** | **Day 2** | **Day 4** | **Day 6** | **Day 8** | **Day 10** | **Day 12** | **Day 14** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Stem Height ($\text{mm}$)** | $12$ | $28$ | $49$ | $74$ | $105$ | $138$ | $172$ |

### 9.9.1 Daily Growth Speed
How fast was the sprout growing during its big middle growth spurt between Day 4 ($28\text{ mm}$) and Day 10 ($105\text{ mm}$)? Subtract the starting height from the ending height on top, subtract the starting day from the ending day on the bottom, and divide:
$$\text{Daily Growth Rate} = \frac{\text{Ending Height} - \text{Starting Height}}{\text{Ending Day} - \text{Starting Day}} = \frac{105 - 28}{10 - 4} = \frac{77\text{ mm}}{6\text{ days}} \approx \mathbf{12.83\text{ mm/day}}$$

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `105` | 0 | 0 | 0 | 105 |
| `[ENTER]` | 0 | 0 | 105 | 105 |
| `28 [-]` | 0 | 0 | 0 | 77 |
| `10` | 0 | 0 | 77 | 10 |
| `[ENTER]` | 0 | 77 | 10 | 10 |
| `[4] [-]` | 0 | 0 | 77 | 6 |
| `[÷]` | 0 | 0 | 0 | $12.83$ |

### 9.9.2 Overall Growth Percentage
How much bigger is the Day 14 plant ($172\text{ mm}$) compared to when it first peeked above the soil on Day 2 ($12\text{ mm}$)? Using `[g] [%CHG]` via `12 [ENTER] 172 [g] [%CHG]` reveals a total growth of $\mathbf{+1333.33\%}$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `12` | 0 | 0 | 0 | 12 |
| `[ENTER]` | 0 | 0 | 12 | 12 |
| `172` | 0 | 0 | 12 | 172 |
| `[g] [%CHG]` | 0 | 0 | 12 | $1333.33$ |

You can combine both measurements—daily growth speed *and* percentage growth—into a single 8-step stack check on your windowsill bean sprout! Suppose five days ago your sprout stood $15\text{ mm}$ tall, and today your millimeter ruler reads $75\text{ mm}$ tall. First, finding the daily growth speed with `75 [ENTER] 15 [-] [5] [÷]` yields **`12.0 mm/day`**, and checking the percentage growth via `15 [ENTER] 75 [g] [%CHG]` confirms **`+400.0%`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `75` | 0 | 0 | 0 | 75 | Enter ending sprout height ($75\text{ mm}$) |
| `[ENTER]` | 0 | 0 | 75 | 75 | Copy ending height into Register $Y$ |
| `15` | 0 | 0 | 75 | 15 | Enter starting sprout height ($15\text{ mm}$) |
| `[-]` | 0 | 0 | 0 | 60 | Subtract to find total height gained ($75 - 15 = 60\text{ mm}$) |
| `[5]` | 0 | 0 | 60 | 5 | Enter number of growing days ($5\text{ days}$) |
| `[÷]` | 0 | 0 | 0 | 12 | Divide height gained by days ($60 \div 5 = 12.0\text{ mm/day}$) |
| `15 [ENTER]` | 0 | 12 | 15 | 15 | Enter starting height ($15\text{ mm}$) into Register $Y$ |
| `75 [g] [%CHG]` | 0 | 12 | 15 | 400 | Find percent increase from $15\text{ mm}$ to $75\text{ mm}$ ($+400.0\%$) |

Register $X$ shows that the bean sprout grew $\mathbf{12.0\text{ mm/day}}$ for a total increase of $\mathbf{+400.0\%}$—five times its starting height in less than a week!

---

## 9.10 Culinary Chemistry & Baker's Percentage Recipe Scaling

Why do professional bread bakers weigh their ingredients in grams on a digital kitchen scale instead of scooping flour with measuring cups—and why do they call the flour weight **$100\%$** even when all the ingredients add up to $171.5\%$? If you scoop flour with a cup, packing the flour tightly can sneak $30$ extra grams into the bowl and make your bread dry and heavy. With **Baker's Percentages**, the flour is always the $100\%$ anchor, and every other ingredient (water, yeast, salt) is simply a percentage of the flour weight! That means you can scale a recipe to feed 4 people or 400 people in seconds—and on the SC-6, because `[%]` leaves your flour weight sitting untouched in Register $Y$, you never even have to re-type the flour weight!

| Ingredient | Baker's Percentage |
| :--- | :--- |
| **Bread Flour** | $100.0\%$ (Base Ingredient) |
| **Water (Hydration)** | $68.0\%$ |
| **Yeast** | $1.5\%$ |
| **Salt** | $2.0\%$ |
| **Total Formula** | **$171.5\%$** |

### 9.10.1 Scaling Bread for a 28-Guest Banquet
The standard loaf requires $500\text{ grams}$ of flour and yields 4 generous servings. You need to bake bread for 28 guests ($28 \div 4 = 7\times$ scaling factor).

Multiplying the $500\text{ g}$ loaf base by $7$ with `500 [ENTER] 7 [×]` establishes $\mathbf{3,500\text{ grams}}$ ($3.5\text{ kg}$) of total flour; from there, `3500 [ENTER] 68 [%]` computes $\mathbf{2,380\text{ grams}}$ ($2.38\text{ L}$) of water at $68\%$ hydration while keeping $3,500\text{ g}$ in Register $Y$, `3500 [ENTER] 2 [%]` finds $\mathbf{70\text{ grams}}$ of salt ($2.0\%$), and `3500 [ENTER] 1.5 [%]` finds $\mathbf{52.5\text{ grams}}$ of yeast ($1.5\%$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `500 [ENTER] 7 [×]` | 0 | 0 | 0 | 3500 | Total Flour base: $500\text{g} \times 7 = 3,500\text{g}$ |
| 02 | `68 [%]` | 0 | 0 | 3500 | 2380 | Water: $68\%$ of $3,500\text{g} = 2,380\text{g}$ ($Y$ holds base $3,500\text{g}$) |
| 03 | `[C] 2 [%]` | 0 | 0 | 3500 | 70 | Clear $X$ (`CLx`, lift disabled) then $2.0\%$ of $3,500\text{g} = 70\text{g}$ ($Y$ base preserved) |
| 04 | `[C] 1.5 [%]` | 0 | 0 | 3500 | 52.5 | Clear $X$ (`CLx`, lift disabled) then $1.5\%$ of $3,500\text{g} = 52.5\text{g}$ ($Y$ base preserved) |

Let's scale a second bakery recipe for the School STEM Bake Sale: twelve golden loaves of country sourdough! A single loaf uses $450\text{ grams}$ of flour ($100\%$), plus $65\%$ water and $2\%$ salt. To mix the dough for all $12$ loaves at once, first calculate total flour (`450 [ENTER] 12 [×]` $\to$ **`5,400 grams`**), then $65\%$ water (`5400 [ENTER] 65 [%]` $\to$ **`3,510 grams`**), and then $2\%$ salt (`5400 [ENTER] [2] [%]` $\to$ **`108 grams`**):

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `450 [ENTER]` | 0 | 0 | 450 | 450 | Enter flour weight for 1 loaf ($450\text{ g}$) |
| `12 [×]` | 0 | 0 | 0 | 5400 | Multiply by 12 loaves to find total flour ($5,400\text{ g}$) |
| `65 [%]` | 0 | 0 | 5400 | 3510 | Find $65\%$ of $5,400\text{ g}$ for water ($3,510\text{ g}$); $5,400$ stays in $Y$ |
| `5400 [ENTER]` | 5400 | 3510 | 5400 | 5400 | Place the $5,400\text{ g}$ flour base in Register $Y$ |
| `[2] [%]` | 5400 | 3510 | 5400 | 108 | Find $2\%$ of $5,400\text{ g}$ for salt ($108\text{ g}$) |

Your 12-loaf batch uses $\mathbf{5,400\text{ grams}}$ of flour, $\mathbf{3,510\text{ grams}}$ of water, and $\mathbf{108\text{ grams}}$ of salt!

### 9.10.2 Scaling Down a Liquid Measuring Cup Recipe with Fraction Towers
What if a cookbook recipe uses fractional measuring cups and you want to make a smaller or larger batch? Suppose a pancake recipe calls for $1\ \frac{3}{4}$ cups of milk to make 8 pancakes, and you are making breakfast for just two people ($2$ pancakes, or $\frac{2}{8} = \frac{1}{4}$ of the recipe). Before touching the keypad, picture this with your **84 mm Fraction Towers**: $1$ whole tower ($84\text{ mm}$) plus three $\frac{1}{4}$ blocks ($3 \times 21\text{ mm} = 63\text{ mm}$) equals seven $\frac{1}{4}$ blocks ($\frac{7}{4}$). Splitting each $\frac{1}{4}$ block into 4 equal pieces turns fourths into sixteenths ($\frac{7}{16}$)! Now verify on the SC-6:
- Enter milk: `1 [.] 3 [.] 4 [ENTER]` ($1\ \frac{3}{4} = 7/4 = 1.75$).
- Divide by 4: `[4] [÷]`.
- Result: **`7/16`** cup of milk ($0.4375$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `1 . 3 . 4` | 0 | 0 | 0 | $1\ \frac{3}{4}$ | Enter mixed fraction $1\ \frac{3}{4}$ cups ($1.75$) |
| 02 | `[ENTER]` | 0 | 0 | $1\ \frac{3}{4}$ | $1\ \frac{3}{4}$ | Push to operational stack |
| 03 | `[4] [÷]` | 0 | 0 | 0 | **`7/16`** | Divide by 4; yields exact $\frac{7}{16}$ cup ($0.4375$) |

Now try scaling up and down for two STEM Bake Sale treats! First, a single batch of trail-mix granola bars calls for $2\ \frac{1}{4}$ cups of rolled oats, and you need $4$ batches for the bake sale table. Picture $2\ \frac{1}{4} \times 4$ with your **Fraction Towers**: four $2$-whole towers make $8$ wholes, and four $\frac{1}{4}$ blocks snap together into $1$ more whole tower ($8 + 1 = 9$). Verifying on the SC-6 using mixed-fraction entry via `2 [.] 1 [.] 4 [ENTER] [4] [×] [a ᵇ/c]` confirms **`9 cups`**: multiplying $2\ \frac{1}{4}$ by $4$ gives an exact $\mathbf{9\text{ cups}}$ of oats.

Second, to wash down the warm granola bars, you blend $3\ \frac{1}{2}$ cups of berry smoothie and pour it equally into $4$ tasting cups for your baking team. Picture $3\ \frac{1}{2}$ as seven $\frac{1}{2}\text{-cup}$ blocks ($7/2$): when you slice each half-cup into 4 equal shares, halves turn into eighths ($7/8$). Dividing the mixed-number volume by 4 on the stack with `3 [.] 1 [.] 2 [ENTER] [4] [÷] [a ᵇ/c]` yields **`7/8 cup`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `3 [.] 1 [.] 2` | 0 | 0 | 0 | $3\ 1/2$ | Enter mixed number $3\ \frac{1}{2}$ cups |
| `[ENTER]` | 0 | 0 | $3\ 1/2$ | $3\ 1/2$ | Push $3\ \frac{1}{2}$ into Register $Y$ |
| `[4]` | 0 | 0 | $3\ 1/2$ | 4 | Enter 4 equal cups |
| `[÷]` | 0 | 0 | 0 | $7/8$ | Divide $3\ \frac{1}{2} \div 4 = 7/8$ cup |
| `[a ᵇ/c]` | 0 | 0 | 0 | $0.875$ | Toggle between exact fraction `7/8` and decimal `0.875` |

Each tasting cup receives $\mathbf{7/8\text{ cup}}$ ($0.875\text{ cup}$) of smoothie—just one eighth of a cup shy of a full cup!

---

## 9.11 Compound Gear Train Ratios & Mechanical Advantage

How can a tiny electric motor that spins super fast—but is weak enough to stop with your finger—lift a heavy bridge or turn the hands of a clock when you connect it through a train of gears? Whenever a small gear with few teeth drives a big gear with many teeth, the big gear turns more slowly, **but pushes with multiplied force**! Better yet, when you connect two gear stages in a row (just like the hidden planetary gears inside your **Planetary Geared Clock** that step every turn of the minute hand down by $12:1$ to move the hour hand), the two stage ratios **multiply together**.

| Reduction Stage | Driver Gear | Driven Gear | Stage Ratio |
| :--- | :---: | :---: | :---: |
| **Stage 1 (Input Shaft)** | Gear A ($12\text{ teeth}$) | Gear B ($36\text{ teeth}$) | $36 \div 12 = 3:1$ |
| **Stage 2 (Middle Shaft)** | Gear C ($16\text{ teeth}$) | Gear D ($48\text{ teeth}$) | $48 \div 16 = 3:1$ |
| **Compound Output** | — | — | **$3 \times 3 = 9:1$** |

### 9.11.1 The Gear Ratio Rule in Words
For a two-stage gear train, divide the driven teeth by the driver teeth for each stage, then multiply the two stage ratios together:
$$\text{Total Gear Ratio} = (\text{Stage 1 Driven Teeth} \div \text{Stage 1 Driver Teeth}) \times (\text{Stage 2 Driven Teeth} \div \text{Stage 2 Driver Teeth})$$
- **How Bicycle and Robot Gear Trains Work:** Four simple patterns show up in every gear train: **LCM tooth line-ups** (where a $14\text{-tooth}$ and $21\text{-tooth}$ gear line up their marked teeth every $\text{LCM} = 42$ teeth), **3-stage fraction multiplication** ($\frac{1}{2} \times \frac{2}{3} \times \frac{3}{4} = \frac{1}{4}$), **bicycle sprocket ratios** ($48 \div 16 = 3:1$), and **gear turn multipliers** (where a $3.5:1$ gear pair multiplies every big-gear turn by $3.5$, spinning the small gear $42$ times when you turn the big gear $12$ times).

### 9.11.2 Computing Total Compound Gear Reduction
Stage 1: Gear A ($12\text{ teeth}$) drives Gear B ($36\text{ teeth}$).  
Stage 2: Gear C ($16\text{ teeth}$) drives Gear D ($48\text{ teeth}$).

Dividing the Stage 1 teeth with `36 [ENTER] 12 [÷]` places $\mathbf{3.0}$ on the stack, dividing the Stage 2 teeth with `48 [ENTER] 16 [÷]` places the second $\mathbf{3.0}$ ratio in Register $X$, and pressing `[×]` multiplies both stages into a **`9.0`** ($9:1$) compound reduction.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `36` | 0 | 0 | 0 | 36 |
| `[ENTER]` | 0 | 0 | 36 | 36 |
| `12 [÷]` | 0 | 0 | 0 | $3.0$ |
| `48` | 0 | 0 | $3.0$ | 48 |
| `[ENTER]` | 0 | $3.0$ | 48 | 48 |
| `16 [÷]` | 0 | 0 | $3.0$ | $3.0$ |
| `[×]` | 0 | 0 | 0 | $9.0$ |

### 9.11.3 Calculating Output Shaft Speed
If the input electric motor spins at $1,800\text{ RPM}$ (revolutions per minute), how fast does the final output shaft spin after a $9:1$ gear reduction?
- `1800 [ENTER] 9 [÷]` $\longrightarrow X = \mathbf{200\text{ RPM}}$ (spinning $9\times$ slower, with $9\times$ the twisting push!).

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `1800 [ENTER]` | 0 | 0 | 1800 | 1800 |
| `9 [÷]` | 0 | 0 | 0 | 200 |

What if your robotics team wants to test a single $4:1$ gear pair where a small $16\text{-tooth}$ driver gear turns a large $64\text{-tooth}$ driven gear (`64 [ENTER] 16 [÷]` $\to$ **`4.0 : 1`**), and then build a two-stage compound winch where Stage 1 has a $10\text{-tooth}$ gear driving a $40\text{-tooth}$ gear and Stage 2 has a $15\text{-tooth}$ gear driving a $30\text{-tooth}$ gear? Watch how the 4-register stack holds the Stage 1 ratio (`4`) on Floor $Z$ while you divide Stage 2 (`30 ÷ 15 = 2`), then multiplies both stages together (`40 [ENTER] 10 [÷] 30 [ENTER] 15 [÷] [×]` $\to$ **`8.0 : 1`**):

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `40 [ENTER] 10 [÷]` | 0 | 0 | 0 | 4 | Stage 1 gear ratio: $40 \div 10 = 4.0$ |
| `30 [ENTER]` | 0 | 4 | 30 | 30 | Enter Stage 2 driven gear ($30\text{ teeth}$); lifts $4$ into Register $Z$ |
| `15 [÷]` | 0 | 0 | 4 | 2 | Stage 2 gear ratio: $30 \div 15 = 2.0$; drops $4$ into Register $Y$ |
| `[×]` | 0 | 0 | 0 | 8 | Multiply Stage 1 by Stage 2: $4 \times 2 = 8.0$ |

Register $X$ displays $8.0$, proving that the two-stage gear train gives an $\mathbf{8.0 : 1}$ mechanical advantage—trading eight fast turns of the motor shaft for one slow, super-strong turn of the winch drum!

---

## 9.12 Hydraulic Syringe Lift & Water Pressure Multiplication

How can a gentle push from your thumb on a small water-filled plastic syringe lift a heavy stack of dictionaries sitting on top of a wide syringe? Connect a narrow $1.0\text{ cm}$ syringe to a wide $3.0\text{ cm}$ syringe with clear vinyl tubing filled with water. When you push the small plunger, the water carries your pressure equally to every square centimeter of the big plunger! And why does making the big plunger $3\times$ wider multiply your force by **$9\times$** instead of $3\times$? Because a plunger is a circle, and just like you discovered in Chapter 06, scaling a shape's width by $3$ scales its **area** by $3 \times 3 = 9$!

| Syringe Part | Plunger Width | Circle Area Comparison | Force Multiplier |
| :--- | :---: | :---: | :--- |
| **Small Input Syringe** | $1.0\text{ cm}$ wide | $1\times$ base area | Your thumb push |
| **Large Output Syringe** | $3.0\text{ cm}$ wide | $(3 \div 1)^2 = 9\times$ area | $\text{Output Lift} = 9 \times \text{Thumb Push}$ |

### 9.12.1 Finding the Force Multiplier
The small input syringe is $1.0\text{ cm}$ wide, and the large output syringe is $3.0\text{ cm}$ wide. Because a circle's area grows with the square of its width, we divide the widths and square the result:
1. Enter the large syringe width: `[3] [ENTER]`.
2. Divide by the small syringe width: `[1] [÷]`.
3. Square the width ratio: Press `[x²]`:
   - Register $X$ displays: **`9.0`** (The force multiplier is **$9\times$**).

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[3]` | 0 | 0 | 0 | 3 |
| `[ENTER]` | 0 | 0 | 3 | 3 |
| `[1]` | 0 | 0 | 3 | 1 |
| `[÷]` | 0 | 0 | 0 | 3 |
| `[x²]` | 0 | 0 | 0 | 9 |

### 9.12.2 Lifting a Heavy Stack of Books
If you push the small syringe with a force of $5.0\text{ Newtons}$ (about half a kilogram of thumb push) and the hydraulic syringe system multiplies your push by $9\times$, how much lifting force and book weight can the large syringe raise?
- `9 [ENTER] 5.0 [×]` $\longrightarrow X = \mathbf{45.0\text{ Newtons}}$, then `9.8 [÷]` $\longrightarrow X = \mathbf{4.59\text{ kg}}$ of lifting power (over $10\text{ pounds}$ of books lifted with one thumb!).

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `9 [ENTER]` | 0 | 0 | 9 | 9 |
| `5.0 [×]` | 0 | 0 | 0 | $45.0$ |
| `9.8 [÷]` | 0 | 0 | 0 | $4.59$ |

---

## 9.13 Drone Flight Battery Endurance & Power Budget

Why do drone pilots always set a countdown timer to land when their rechargeable battery still has $20\%$ charge left—and how can you predict your exact hover time before spinning up the propellers? Think of a drone battery's **milliamp-hour ($\text{mAh}$) rating** like a fuel tank of electrical energy, and the four motors' **current draw ($\text{mA}$)** like how fast the motors sip from that tank. Leaving $20\%$ in reserve protects the battery chemistry from overheating and gives you a safe landing cushion!

| Drone Battery Measurement | Value / Word Rule |
| :--- | :--- |
| **Battery Capacity** | $850\text{ mAh}$ |
| **Hover Current Used** | $4,200\text{ mA}$ |
| **Safe Battery Rule** | Use $80\%$ ($0.80$) so $20\%$ stays in reserve to protect the battery |
| **Safe Flight Time (Minutes)** | $(\text{Battery Capacity} \times 0.80 \times 60\text{ minutes}) \div \text{Hover Current}$ |

### 9.13.1 Calculating Safe Hover Duration
1. Enter battery capacity: `850 [ENTER]`.
2. Multiply by the $80\%$ safe battery rule: `[.] [8] [×]` $\longrightarrow X = \mathbf{680\text{ mAh usable}}$.
3. Multiply by $60\text{ minutes per hour}$: `60 [×]` $\longrightarrow X = \mathbf{40,800\text{ mA}\cdot\text{min}}$.
4. Divide by total hover current ($4,200\text{ mA}$): `4200 [÷]`:
   - Register $X$ displays: **$9.714\text{ minutes}$**.
5. Convert decimal minutes to minutes and seconds:
   - Safe flight timer: **9 minutes 43 seconds**.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `850` | 0 | 0 | 0 | 850 |
| `[ENTER]` | 0 | 0 | 850 | 850 |
| `[.] [8] [×]` | 0 | 0 | 0 | 680 |
| `60 [×]` | 0 | 0 | 0 | 40800 |
| `4200 [÷]` | 0 | 0 | 0 | $9.714$ |

### 9.13.2 Carrying a Mini Action Camera
What happens to your flight time when you clip a $45\text{-gram}$ mini action camera onto the drone? Because the propellers have to spin faster to lift the extra weight, the hover current jumps from $4,200\text{ mA}$ to $5,500\text{ mA}$:
1. Calculate the new flight time with the camera:
   - Usable battery capacity: $680\text{ mAh}$ ($80\%$ of $850\text{ mAh}$).
   - Flight minutes: $(680 \times 60) \div 5,500 = 7.418\text{ minutes}$ ($7\text{ min } 25\text{ sec}$).
2. Calculate the percent change in flight time:
   - Starting flight time: $9.714\text{ min}$.
   - New flight time: $7.418\text{ min}$.
   - Percent change: enter `9.714`, swap `[x⇄y]`, then press `[g] [%CHG]` $\longrightarrow \mathbf{-23.64\%}$ shorter flight time.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `680 [ENTER]` | 0 | 0 | 680 | 680 |
| `60 [×]` | 0 | 0 | 0 | 40800 |
| `5500 [÷]` | 0 | 0 | 0 | $7.418$ |
| `9.714` | 0 | 0 | $7.418$ | $9.714$ |
| `[x⇄y]` | 0 | 0 | $9.714$ | $7.418$ |
| `[g] [%CHG]` | 0 | 0 | $9.714$ | $-23.64$ |

How can you get more flight time back when carrying a heavier frame or camera? Upgrade to a higher-capacity battery! Suppose your club bolts a lightweight 3D-printed frame onto an indoor quadcopter powered by a larger $1,200\text{ mAh}$ battery. Following the $80\%$ safe battery rule ($0.80$) so $20\%$ stays in reserve for a safe landing, how many minutes can the drone hover when its four motors draw a combined $5,000\text{ mA}$? Calculating the safe flight time in minutes on the stack via `1200 [ENTER] .8 [×] 60 [×] 5000 [÷]` produces **`11.52 min`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `1200 [ENTER]` | 0 | 0 | 1200 | 1200 | Enter battery capacity ($1,200\text{ mAh}$) |
| `.8 [×]` | 0 | 0 | 0 | 960 | Multiply by $0.80$ safe battery rule: $960\text{ mAh}$ usable |
| `60 [×]` | 0 | 0 | 0 | 57600 | Multiply by $60\text{ minutes per hour}$ ($57,600\text{ mA}\cdot\text{min}$) |
| `5000` | 0 | 0 | 57600 | 5000 | Enter hover current draw ($5,000\text{ mA}$) |
| `[÷]` | 0 | 0 | 0 | $11.52$ | Divide usable battery by current ($57,600 \div 5,000 = 11.52\text{ min}$) |

Register $X$ displays $11.52\text{ minutes}$, showing that the upgraded $1,200\text{ mAh}$ battery lets the quadcopter safely hover for $\mathbf{11.52\text{ minutes}}$ before the landing timer beeps!

---

## 9.14 Solar Panel Tilt Angle & Sunlight Shadow Factor

Why does a solar panel make maximum power when aimed straight at the noon sun ($0^\circ$ tilt), yet drop to exactly half power when tilted at $60^\circ$? Hold a flat book under a ceiling light and tilt it slowly: as the book tilts, the **shadow** it casts on the table directly underneath gets narrower! A solar panel only catches as much beam width of sunshine as its flat shadow—and you can read that exact **Sunlight Shadow Factor** right off your 3D-printed **Unit Circle Volvelle**! When you turn the pointer of the Unit Circle Volvelle to $0^\circ, 30^\circ, 45^\circ,$ or $60^\circ$, the horizontal window displays the shadow factor ($1.0000, 0.8660, 0.7071,$ and $0.5000$), showing the exact decimal fraction of direct sunlight caught by the tilted panel.

| Panel Tilt Angle | Sunlight Shadow Factor (from Volvelle) | Solar Power Produced ($\text{Peak Watts} \times \text{Shadow Factor}$) |
| :--- | :--- | :--- |
| **$0^\circ$ (Flat to the Sun)** | $1.0000$ | $100.0\%$ of Peak Watts |
| **$30^\circ$ Tilt** | $0.8660$ | $86.6\%$ of Peak Watts |
| **$45^\circ$ Tilt** | $0.7071$ | $70.7\%$ of Peak Watts |
| **$60^\circ$ Tilt** | $0.5000$ | $50.0\%$ of Peak Watts |

### 9.14.1 Solar Power at Different Tilt Angles
A classroom solar panel produces $5.0\text{ Watts}$ when pointed straight at the sun ($0^\circ$ tilt). How many Watts does it produce at tilt angles of $30^\circ, 45^\circ,$ and $60^\circ$?

1. At a $30^\circ$ tilt (Volvelle shadow factor $0.866$), multiplying via `5 [ENTER] 0.866 [×]` yields $X = \mathbf{4.33\text{ Watts}}$ ($86.6\%$).
2. At a $45^\circ$ tilt (Volvelle shadow factor $0.7071$), multiplying via `5 [ENTER] 0.7071 [×]` yields $X = \mathbf{3.54\text{ Watts}}$ ($70.7\%$).
3. At a $60^\circ$ tilt (Volvelle shadow factor $0.500$), multiplying via `5 [ENTER] .5 [×]` yields $X = \mathbf{2.50\text{ Watts}}$ ($50.0\%$).

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[5] [ENTER]` | 0 | 0 | 5 | 5 |
| `.866 (30° factor)` | 0 | 0 | 5 | $0.8660$ |
| `[×]` | 0 | 0 | 0 | $4.33$ |

Repeating this stack multiplication across all four tilt angles produces the complete solar panel power table:

| Tilt Angle | Shadow Factor | Peak Watts | Output Power | Percent of Peak |
| :--- | :--- | :--- | :--- | :--- |
| 0° | 1.0000 | 5.00 W | 5.00 W | 100.0% |
| 30° | 0.8660 | 5.00 W | 4.33 W | 86.6% |
| 45° | 0.7071 | 5.00 W | 3.54 W | 70.7% |
| 60° | 0.5000 | 5.00 W | 2.50 W | 50.0% |

### 9.14.2 Adding Up a Full School Day of Solar Energy
As the sun arcs across the sky from morning to afternoon, how much total electrical energy does your panel harvest over an 8-hour school day? Multiply the Watts by the hours for each part of the day and drop each subtotal into your statistical basket (`[Σ+]`):
- Morning (9:00 AM, $60^\circ$ tilt): $2.50\text{ Watts}$ for 3 hours $\longrightarrow 7.50\text{ Watt-hours}$.
- Noon (12:00 PM, $0^\circ$ tilt): $5.00\text{ Watts}$ for 2 hours $\longrightarrow 10.00\text{ Watt-hours}$.
- Afternoon (3:00 PM, $45^\circ$ tilt): $3.54\text{ Watts}$ for 3 hours $\longrightarrow 10.62\text{ Watt-hours}$.

Add up each energy period using the SC-6 statistical key `[Σ+]`:
1. Clear statistics: `[g] [CLΣ]`.
2. Morning energy: `2.5 [ENTER] [3] [×] [Σ+]` $\longrightarrow \text{Count} = 1$ ($7.5\text{ Wh}$).
3. Noon energy: `[5] [ENTER] [2] [×] [Σ+]` $\longrightarrow \text{Count} = 2$ ($10.0\text{ Wh}$).
4. Afternoon energy: `3.54 [ENTER] [3] [×] [Σ+]` $\longrightarrow \text{Count} = 3$ ($10.62\text{ Wh}$).
5. Total Daily Energy: Press `[f] [Σx]` $\longrightarrow X = \mathbf{28.12\text{ Watt-hours}}$.
6. Convert to Kilowatt-hours: `1000 [÷]` $\longrightarrow X = \mathbf{0.02812\text{ kWh}}$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[g] [CLΣ]` | 0 | 0 | 0 | 0 |
| `2.5 [ENTER] 3 [×]` | 0 | 0 | 0 | $7.5$ |
| `[Σ+]` | 0 | 0 | 0 | $1.0000$ |
| `5 [ENTER] 2 [×]` | 0 | 0 | 0 | $10.0$ |
| `[Σ+]` | 0 | 0 | 0 | $2.0000$ |
| `3.54 [ENTER] 3 [×]` | 0 | 0 | 0 | $10.62$ |
| `[Σ+]` | 0 | 0 | 0 | $3.0000$ |
| `[f] [Σx]` | 0 | 0 | 0 | $28.12$ |
| `1000 [÷]` | 0 | 0 | 0 | $0.02812$ |

---

## 9.15 Maker Lab Engineering Notebook & Measurement Checks

Real makers always check how close their physical measurements come to their design target. In this section, you learn to calculate **Percent Error** and **3D-Printing Snap-Fit Clearance** on the SC-6:

$$\text{Percent Error} = (\text{Difference from Target} \div \text{Target Value}) \times 100\%$$

### 9.15.1 Checking Percent Error on a Precision Calibration Block
Suppose a precision 3D-printed calibration bar has a target weight of $9.80665\text{ grams}$, and your digital scale measures $9.7716\text{ grams}$. How close is your print in percent? Because subtracting $9.80665$ automatically saves $9.80665$ inside `[f] [LASTX]`, tapping `[f] [LASTX] [÷]` divides by the target value right away without making you type that six-digit number a second time!

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `9.7716` | 0 | 0 | 0 | $9.7716$ |
| `[ENTER]` | 0 | 0 | $9.7716$ | $9.7716$ |
| `9.80665` | 0 | 0 | $9.7716$ | $9.80665$ |
| `[-]` | 0 | 0 | 0 | $-0.03505$ |
| `[f] [LASTX]` | 0 | 0 | $-0.03505$ | $9.80665$ |
| `[÷]` | 0 | 0 | 0 | $-0.003574$ |
| `[g] [|x|]` | 0 | 0 | 0 | $0.003574$ |
| `100 [×]` | 0 | 0 | 0 | $0.357$ |

*(Your print is within $0.36\%$ of the target—and `[f] [LASTX]` saved you from re-typing `9.80665`.)*

---

### 9.15.2 3D Printing Snap-Fit Clearance Gap
When 3D printing interlocking parts—like the stacking lips of your **Counting Tiles**, the dovetail slots of the **L-Frame Factoring Stage**, or the $42\text{ mm}$ **Gridfinity Studio Bins**—melted plastic expands slightly as it cools, so engineers leave a small clearance gap of $0.15\text{ mm}$ on each side.
If a round peg is $10.00\text{ mm}$ wide, what is the minimum hole width needed so the peg slides in smoothly?
$$\text{Hole Width} = \text{Peg Width} + (2 \times \text{Clearance Gap}) = 10.00\text{ mm} + (2 \times 0.15\text{ mm}) = 10.30\text{ mm}$$

Doubling the $0.15\text{ mm}$ side clearance and adding it to the $10.00\text{ mm}$ peg width on the stack via `10 [ENTER] .15 [ENTER] 2 [×] [+]` gives a smooth-sliding hole diameter of $\mathbf{10.30\text{ mm}}$.

---

### 9.15.3 Digital Scale & Filament Density Check
In maker spaces, you can also run our earlier $20.0\text{ mm} \times 20.0\text{ mm} \times 20.0\text{ mm}$ ($2.0\text{ cm}$ on each edge) calibration test cube in reverse to check whether an unlabeled mystery spool of plastic is corn-based PLA ($1.24\text{ g/cm}^3$) or lightweight ABS ($1.04\text{ g/cm}^3$) by finding how much $1\text{ cm}^3$ of the plastic weighs ($\text{Grams per cm}^3 = \text{Weight in Grams} \div \text{Volume in cm}^3$). Just as we saw when comparing solid and hollow infill earlier in the chapter, cubing the $2.0\text{ cm}$ edge length on the stack via `2 [ENTER] 2 [×] 2 [×]` (`[2] [ENTER] [2] [×]` $\to 4\text{ cm}^2$ base area, followed by `[2] [×]`) places the exact cube volume **`8`** ($X = \mathbf{8.00\text{ cm}^3}$) on Ground Shelf $X$. Next, place the solid mystery cube on a zeroed digital scale, where it reads $9.92\text{ grams}$, and type `9.92` into Register $X$ (which automatically lifts the $8.0\text{ cm}^3$ volume onto Waiting Shelf $Y$). Because density is weight divided by volume ($\text{Grams} \div \text{cm}^3$), tap `[x⇄y]` once to swap `9.92` into the left seat (Register $Y$) and `8.0` into the right seat (Register $X$), then press `[÷]`: Ground Shelf $X$ immediately displays **`1.24`** ($\mathbf{1.24\text{ g/cm}^3}$)—confirming that the mystery spool is **authentic PLA** ($1.24\text{ g/cm}^3$) rather than ABS ($1.04\text{ g/cm}^3$)!

---

## 9.16 Maker Space Machine Safety Protocols & Electrical Protection

Operating maker space equipment requires following classroom safety rules:

> **Workshop Safety & Electrical Power Rules**
> 1. **Heat Safety:** 3D printer nozzles reach $210^\circ\text{C} - 245^\circ\text{C}$; heated build plates reach $60^\circ\text{C}$. Never touch the nozzle or heated bed while printing.
> 2. **Battery Safety:** Never short-circuit rechargeable batteries or drain them past their $20\%$ reserve margin.
> 3. **Eye Protection:** Always wear safety glasses when launching tabletop catapults, testing water syringes, or clipping plastic support material.
> 4. **Fresh Air:** Always run the classroom air filter when 3D printing.

### 9.16.1 Classroom Wall Outlet Load Check
A classroom maker lab has four 3D printers ($150\text{ W}$ each), two laptop computers ($65\text{ W}$ each), and an air filter ($80\text{ W}$) plugged into a single $120\text{-Volt}$, $15\text{-Amp}$ wall circuit.
Does the total electrical load stay safely below the $80\%$ continuous limit ($12\text{ Amps}$)?

1. Total Watts Used:
   - 4 printers: `4 [ENTER] 150 [×]` $\longrightarrow 600\text{ W}$.
   - 2 laptops: `2 [ENTER] 65 [×] [+]` $\longrightarrow 730\text{ W}$.
   - 1 air filter: `80 [+]` $\longrightarrow \mathbf{810\text{ Watts total}}$.
2. Amps Used at $120\text{ Volts}$ ($\text{Total Watts} \div 120\text{ Volts}$):
   - `120 [÷]` $\longrightarrow X = \mathbf{6.75\text{ Amps}}$.
3. Safe $80\%$ Circuit Limit ($15\text{ Amps} \times 80\%$):
   - `15 [ENTER] 80 [%]` $\longrightarrow X = \mathbf{12.00\text{ Amps}}$.
4. Safety Room Remaining:
   - `12 [ENTER] 6.75 [-]` $\longrightarrow X = \mathbf{5.25\text{ Amps remaining}}$, confirming that all machines run safely with $5.25\text{ Amps}$ to spare.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `4 [ENTER] 150 [×]` | 0 | 0 | 0 | 600 |
| `2 [ENTER] 65 [×]` | 0 | 0 | 600 | 130 |
| `[+]` | 0 | 0 | 0 | 730 |
| `80 [+]` | 0 | 0 | 0 | 810 |
| `120 [÷]` | 0 | 0 | 0 | $6.75$ |
| `15 [ENTER] .80 [×]` | 0 | 0 | $6.75$ | $12.0$ |
| `[x⇄y] [-]` | 0 | 0 | 0 | $5.25$ |

---

### 9.16.2 Lab Bench Mysteries: Layer Thickness & Pendulum Swings

- **Why Does Layer Thickness Change 3D-Printing Time So Much?** Suppose you slice a $1.0\text{ cm}$ top block section into $0.02\text{ cm}$ layers (`50` layers). If you switch your slicer to ultra-fine $0.01\text{ cm}$ layers, the printer nozzle has to trace $1.0 \div 0.01 = 100$ layers—twice as many horizontal trips across the build plate! You can even check how tiny a $0.020\text{ cm}$ layer is when squared (`0.020 [x²]` $\to 0.0004\text{ cm}^2$).
- **Why Doesn't a Heavier Pendulum Swing Faster?** A $50\text{-gram}$ steel bolt and a $5\text{-gram}$ wooden bead tied to the same $100\text{ cm}$ string both take $20.1\text{ seconds}$ to complete $10$ swings (an average of $2.01\text{ seconds}$ per swing). Gravity pulls ten times harder on the $50\text{-gram}$ bolt, but the heavier bolt is also ten times harder to get moving, so the two effects balance out completely. Only the length of the string changes the swing time!

Keep this quick troubleshooting checklist handy at your workbench whenever a measurement or calculation looks surprising:

| What Happened on Your Screen | Why It Happened | How to Fix It |
| :--- | :--- | :--- |
| **Squaring the full width (diameter) instead of the radius** | Forgetting to divide the circle's width by 2 before squaring. | *"Width (diameter) goes all the way across the circle; radius goes from the center to the edge. Always divide $1.75\text{ mm}$ by 2 to get radius $0.875\text{ mm}$."* |
| **Forgetting to subtract the base height before slicing layers** | Dividing the full block height by $0.02\text{ cm}$ instead of just the remaining top section. | *"Subtract the already-printed base height from the total height first (`3 ENTER 2 -`), then divide the remaining height by `.02`."* |
| **Assuming a heavier pendulum swings faster** | Thinking a heavier weight falls faster on a string. | *"A heavier weight gets pulled harder by gravity, but it is also harder to speed up. The two balance out: only the string length changes the swing time."* |
| **Scaling recipes by adding instead of multiplying** | Adding cups instead of multiplying by the batch size. | *"If you make 7 loaves of bread instead of 1, you must MULTIPLY every single ingredient by 7, not add 7."* |
| **Dividing gear ratios in reverse order** | Mixing up the driver gear (input) and driven gear (output). | *"Gear ratio is always Driven teeth divided by Driver teeth ($\text{Out} \div \text{In}$). A bigger driven gear spins slower with stronger push."* |
| **Ignoring the 20% battery reserve rule** | Draining a rechargeable drone battery all the way to 0%. | *"Draining a drone battery below 20% wears it out. Always multiply battery capacity by 0.80 to find safe flight time."* |

---

### 9.16.3 Scratch-Paper Formula Juggling vs. Live Workshop Stack Modeling

Now that you have explored 3D printing, pendulums, solar ovens, catapults, recipes, gear trains, hydraulics, and drones, compare how a multi-step workshop cost calculation is entered on a standard calculator versus live unit-rate evaluation on the SC-6 stack:

| Challenge / Equation | The Algebraic Calculator Trap (Standard Entry) | The StackCalc SC-6 + Manipulative Method | Keystroke Comparison | Live Stack Visibility | Learning Breakthrough |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **3D Printing Filament Cost**: $14.91\text{g} \times (\$20.00 / 1000\text{g}) = \$0.30$ | Typing `1 4 . 9 1  2 0 / 1 0 0 0 =` (14 physical keystrokes) jumps straight to `0.2982` without ever displaying the $\$0.02/\text{g}$ unit cost—or requires parentheses `1 4 . 9 1  ( 2 0 / 1 0 0 0 ) =` (16 physical keystrokes) to group the unit rate first. | Continuous dimensional pipeline: `14.91 [ENTER] 20 [ENTER] 1000 [÷] [×] [$]` $\to \mathbf{\$0.30}$ (16 physical keystrokes, including `[$]` rounding). Both the part mass ($14.91\text{g}$) and unit cost ($\$0.02/\text{g}$) appear side by side on the stack. | **16 vs. 16 strokes (with live unit-rate check & `[$]` rounding)** | Register $Y$ holds $14.91\text{g}$ while Register $X$ displays the exact unit price $\$0.02/\text{g}$, followed by single-tap `[×]` and `[$]` currency formatting without scrap paper. | Students measure physical filament with calipers, inspect both the gram weight and per-gram unit rate simultaneously on the screen, and see the exact cost before printing. |

---

## 9.17 Where to Go Next: Companion Workbook Quests & Kitchen-Table Challenges

> *For 26 additional worked problems with full 4-register stack tables, see Chapter 9 of the [SC-6 Elementary Companion Problem & Activity Workbook](../curriculum/sc6-elementary-companion-workbook.md).*

Ready to launch your own weekend invention studio? Here is how to extend the projects in this chapter using the [Big Ideas Math Middle School Supplement](../curriculum/big-ideas-middle-school-sc6-workbook.md)—across **Unit 1: Numerical Expressions & Factors (Section 1.5)**, **Unit 2: Fractions & Decimals (Sections 2.2, 2.3 & 2.5)**, **Unit 3: Ratios, Rates & Percents (Sections 3.1 & 3.3)**, **Unit 5: Area, Surface Area & Volume (Section 5.2)**, **Unit 7: Equations & Inequalities (Section 7.5)**, **Unit 8: Geometric Figures, Scale Drawings & Circles (Section 8.4)**, and **Unit 9: Statistical Measures & Data Displays (Section 9.4)**—alongside *Timed Proficiency Trials* and the *12-Unit Curriculum Guide*:

1. **The Kitchen-Table Pendulum Timing Lab (Curriculum Guide Unit 9 & Student Workbook):** Tie a metal washer or 3D-printed bob to a $100\text{ cm}$ ($1\text{-meter}$) piece of string and time 10 full back-and-forth swings with a stopwatch. Divide by $10$ on your SC-6 to find the average time for 1 swing, then shorten the string to $25\text{ cm}$ (one-fourth as long) and time 10 swings again to see why a quarter-length pendulum swings twice as fast!
2. **The Baker's Percentage Pizza Night (Big Ideas Middle School Supplement):** Weigh out $400\text{ g}$ of flour on a kitchen scale ($100\%$), then use your SC-6's `[%]` and `[C]` keys (just like our 28-guest banquet bread scaling earlier) to compute $65\%$ warm water ($260\text{ g}$), $2\%$ salt ($8\text{ g}$), and $1.5\%$ yeast ($6\text{ g}$) without ever re-typing `400`.
3. **The 3D-Printer Slicer & `[f] [LASTX]` Height Sprint (Timed Proficiency Trials — Maker Engineering Round):** Pick any block height in centimeters, subtract the base height, and divide by `.02` ($0.02\text{ cm}$ per layer) to find how many horizontal plastic layers the 3D printer must trace—then tap `[f] [LASTX] [×]` to verify that the layers stack back up to the exact remaining height without typing `.02` twice!

---

## 9.18 Chapter Summary & Looking Ahead

Across all nine chapters, you have paired physical manipulatives with the four-register stack to solve arithmetic, geometry, statistics, and maker problems:

1. **The RPN Mental Model & Stack Mastery:** You replaced parentheses and equals-sign confusion with a four-register stack ($X, Y, Z, T$) that tracks intermediate values like physical blocks.
2. **Tactile Fractions & Rational Arithmetic:** You explored fraction equivalence, common denominators, and mixed numerals by aligning real blocks and tapping dedicated fraction hardware keys (`[a ᵇ/c]`, `[f] [d/c]`, `[g] [SIMP]`).
3. **Spatial Geometry & Dimensional Scaling:** You measured perimeters, surface areas, and 3D volumes, using **Counting Tiles**, the **L-Frame Factoring Stage**, and the **Unit Circle Volvelle** shadow projection to connect 2D footprints to real 3D solids.
4. **Number Theory & Experimental Probability:** You examined the building blocks of numbers with prime factorization, GCF, and LCM, and gathered empirical data with the hardware probability engine (`[🎲]`) and statistical accumulators (`[Σ+]`).
5. **Cognitive Reflexes & Mental Math Fluency:** You trained your speed and accuracy in the Quiz Engine, applying the ends-in-5 squaring shortcut, the 11s trick, and instant verification without scratch paper.
6. **Applied STEM & Maker Design:** You connected word rules directly to physical measurements—budgeting 3D printer filament weight and spool costs, slicing $0.02\text{ cm}$ print layers, timing clock pendulums, scaling recipes, tuning gear ratios, and calculating drone flight times.

Your SC-6 is more than a calculator—it is your permanent laboratory workbench, your tactile compass, and your engineering partner. 

To fabricate your own manipulatives in CAD or on a 3D printer, check out **[Appendix A: Manipulative Studio Guide & How We Built StackCalc](sc6/appendix-a-manipulative-blueprints.md)**, review classroom stations in **[Appendix B: Teacher Lesson Plans & Diagnostic Protocols](sc6/appendix-b-teacher-lesson-plans.md)**, look up conversion factors in **[Appendix C: Formulas, Conversions & Prime Catalogs](sc6/appendix-c-formulas-and-conversions.md)**, or inspect every button function in **[Appendix D: Keycap Matrix & Layout Directory](sc6/appendix-d-keycap-directory.md)**. 

Keep building, keep measuring, and keep exploring!

---

# Appendix A: Manipulative Studio Guide & How We Built StackCalc

> **Where to Download 3D Print Files, Laser Templates & Full Hardware Specs**
> To keep this book focused on hands-on math discovery rather than long lists of 3D-printer temperatures, slicer settings, and mechanical tolerances, all downloadable `.stl` and `.3mf` 3D print files, laser-cutter templates, and detailed hardware specifications are hosted online:
> - **3D Print Files & Printable PDF Cutouts:** [stackcalc.io/downloads](https://stackcalc.io/downloads/) (including the complete [Learning Lab Master STL Pack](https://stackcalc.io/downloads/stackcalc-learning-lab-0.2.0-stl-pack.zip))
> - **Hardware & Enclosure Documentation:** [stackcalc.io/hardware](https://stackcalc.io/hardware)
> - **Open Engineering Logs & Build Story:** [Hackaday.io — StackCalc Tactile RPN Calculator Project](https://hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator)

> **CHOKING HAZARD — SMALL PARTS & 3D PRINTING SAFETY (16 CFR § 1501 / ASTM F963):**  
> The physical manipulative studios documented in this appendix (including the $19.0 \times 19.0 \times 7.0\,\text{mm}$ visible $1\text{U}$ Counting Tiles [$8.85\,\text{mm}$ overall height with stacking lip], Ten-Frame Counters, $\frac{1}{12}$ Fraction Studio blocks, Prime Factor blocks, and Polyhedral Dice) contain small parts that fit within the CPSC small-parts test cylinder ($31.7\,\text{mm}$ diameter). **Not for children under 3 years of age.** Recommended for supervised educational use in Grades 3–6 (ages 8–12).  
> **Classroom Print Check:** Always print classroom manipulatives using certified non-toxic PLA or PETG filament. Before handing newly printed parts to students, an adult should inspect each piece and remove any loose filament wisps or brims.

---

## A.1 Why Hands-On Blocks Make Math Click

Why build physical math blocks when digital screens are everywhere? Because your hands and eyes learn together! When you pick up a physical 10-rod, stack an $84\text{ mm}$ fraction tower, or balance a lever beam, your fingers can *feel* why an idea is true before you even press a key on the calculator.

Grounded in Jerome Bruner's hands-on learning research *([Bruner, 1966](sc6/appendix-c-formulas-and-conversions.md#cite-bruner1966))*, Zoltan Dienes' multi-embodiment principle *([Dienes, 1960](sc6/appendix-c-formulas-and-conversions.md#cite-dienes1960))*, and David Macaulay's clear visual explanations of how things work *([Macaulay, 2016](sc6/appendix-c-formulas-and-conversions.md#cite-macaulay2016))*, every StackCalc manipulative kit follows three simple rules:
1. **True Mathematical Scale:** A 10-rod equals exactly 10 unit cubes in length and volume. Two $\frac{1}{4}$ fraction blocks stacked together match a $\frac{1}{2}$ block right to the top edge with zero gap.
2. **Three Ways to Build:** Every classroom and family can make these tools using a desktop 3D printer (with zero support material needed), a school laser cutter, or ordinary cardstock paper, scissors, and a glue stick.
3. **Tidy Modular Trays:** All eight manipulative kits store neatly inside standard **Gridfinity** modular trays ($42.0\text{ mm}$ grid squares) so pieces stay organized on your desk.

---

## A.2 How the Eight Manipulative Studios Work

All 3D-printable `.stl` and `.3mf` files for these eight studios can be downloaded free of charge at **[stackcalc.io/downloads](https://stackcalc.io/downloads/)**:

### A.2.1 The Ten-Frame Studio
- **What It Teaches:** Early counting, spotting groups of 5 and 10 at a glance (subitizing), and make-ten addition (CCSS 3.OA.C.7).
- **How the Math Is Built In:** Each tray holds two $2 \times 5$ rows of two-color flip counters ($16.5\text{ mm} \times 3.5\text{ mm}$, red on one side and yellow on the other). A raised **5-anchor divider rib** right down the middle splits each row of 10 into two clear groups of 5, matching `[▦]` Ten-Frame Mode on your SC-6 screen.
- **Download:** **[stackcalc.io/downloads/ten-frames-open-source-stls.zip](https://stackcalc.io/downloads/ten-frames-open-source-stls.zip)**

### A.2.2 Place Value Studio
- **What It Teaches:** Multi-digit place value, 10-for-1 carrying and borrowing (regrouping), and decimal place value (CCSS 3.NBT.A.2, 5.NBT.A.1).
- **How the Math Is Built In:** Stored in a $3 \times 1 \times 7\text{U}$ Gridfinity box (`"PLACE VALUE"` plaque, `[PV]` lid badge), every component is engineered around the unified $19.0 \times 19.0 \times 7.0\text{ mm}$ visible $1\text{U}$ Miniblock standard:
  - **$4 \times 2$ Whole Numbers Activity Tray (`77.8 × 38.6 × 8.85 mm`):** Four recessed column sockets labeled `THOUSANDS | HUNDREDS | TENS | ONES` (`1000 | 100 | 10 | 1`) across two rows (matching Registers $Y$ and $X$).
  - **$4 \times 2$ Decimal Numbers Activity Tray (`77.8 × 38.6 × 8.85 mm`):** Four recessed column sockets labeled `ONES • TENTHS | HUNDREDTHS | THOUSANDTHS` (`1 • 0.1 | 0.01 | 0.001`) with a raised tactile decimal point (`•`).
  - **44 Place Value Digit Miniblocks (`0`–`9`):** Four complete sets of digits `0–9` plus four extra `0` placeholders ($19.0 \times 19.0 \times 7.0\text{ mm}$ visible $1\text{U}$ height).
  - **9 Stackable `+1` Regrouping Unit Miniblocks:** $19.0 \times 19.0 \times 7.0\text{ mm}$ visible $1\text{U}$ height; stacking 10 unit blocks reaches $70.0\text{ mm}$ (matching the $70.0\text{ mm}$ Ten-Frame 10-Rod) and trades 10-for-1 into the next place-value column to the left.
- **Download:** **[stackcalc.io/downloads/place-value-open-source-stls.zip](https://stackcalc.io/downloads/place-value-open-source-stls.zip)**

### A.2.3 The 84 mm Fraction Studio
- **What It Teaches:** Equivalent fractions, common denominators, and step-by-step simplification with `[g] [SIMP]` (CCSS 3.NF.A.1, 4.NF.A.1).
- **Why Exactly 84 Millimeters?** Because $84$ divides evenly by $1, 2, 3, 4, 6, 7, 12, 14, 21, 28,$ and $42$. That gives every fraction tower an exact, whole-millimeter height ($1 = 84\text{ mm}$, $\frac{1}{2} = 42\text{ mm}$, $\frac{1}{3} = 28\text{ mm}$, $\frac{1}{4} = 21\text{ mm}$, $\frac{1}{6} = 14\text{ mm}$, $\frac{1}{8} = 10.5\text{ mm}$, $\frac{1}{12} = 7\text{ mm}$). A recessed lap joint lets towers stack without adding extra height, so $\frac{1}{2} + \frac{1}{3} + \frac{1}{6}$ stands at $42 + 28 + 14 = 84.0\text{ mm}$ alongside the $1\text{ WHOLE}$ tower.
- **Download:** **[stackcalc.io/downloads/fraction-studio-open-source-stls.zip](https://stackcalc.io/downloads/fraction-studio-open-source-stls.zip)**

### A.2.4 Algebra Factoring Studio & L-Frame Stage
- **What It Teaches:** Area models, distributive multiplication, breaking rectangles into friendlier parts, and solving puzzles with positive and negative zero-pairs (CCSS 6.EE.A.3, 6.EE.B.7).
- **How the Math Is Built In:** Two interlocking rails snap together at a $90^\circ$ corner to form the **L-Frame Factoring Stage** (horizontal rail for the top width, vertical rail for the side height). Inside the grid sit 40 stackable Miniblock tiles—four large square flats ($38.6 \times 38.6\text{ mm}$), twelve rectangular rods ($38.6 \times 19.0\text{ mm}$), and twenty-four unit tiles ($19.0 \times 19.0\text{ mm}$, twelve $+1$ and twelve $-1$, $7.0\text{ mm}$ visible height)—so learners can build area-model rectangles like $(10 + 2) \times (10 + 3) = 100 + 50 + 6 = 156$ and cancel $+1$ and $-1$ zero-pairs by hand.
- **Download:** **[stackcalc.io/downloads/algebra-boxes-open-source-stls.zip](https://stackcalc.io/downloads/algebra-boxes-open-source-stls.zip)**

### A.2.5 Planetary Geared Clock & $360^\circ$ Unit Circle Volvelle
- **What It Teaches:** Telling time across the 60-minute boundary (`[🕒]`), fractions of an hour using 4 removable $90^\circ$ dial quadrants, and measuring angles around a $360^\circ$ circle (CCSS 3.MD.A.1, 4.MD.C.5).
- **How the Math Is Built In:** Inside the clock sits a planetary gear train with a **12-tooth center sun gear, three 60-tooth planet gears, and a 132-tooth outer ring gear** ($12 + 2 \times 60 = 132$):
  $$\text{Clock Gear Ratio} = 1 + (132 \div 12) = 1 + 11 = \mathbf{12 : 1\text{ Exact Reduction}}$$
  Every full $360^\circ$ turn of the minute hand advances the hour hand by $\frac{1}{12}$ of a circle ($30^\circ$, or 1 hour).
- **Download:** **[stackcalc.io/downloads/classroom-clock-open-source-stls.zip](https://stackcalc.io/downloads/classroom-clock-open-source-stls.zip)** and **[stackcalc.io/downloads/unit-circle-volvelle-open-source-stls.zip](https://stackcalc.io/downloads/unit-circle-volvelle-open-source-stls.zip)**

### A.2.6 Number Rack, Math Dominoes & Quest Scoreboard
- **What It Teaches:** Subitizing 5-and-5 bead groups (`[g] [COUNT]`), pairing domino dot patterns across a 12-frame, and tracking two-way problem mastery (`[f] [?]` Quiz Mode).
- **How the Math Is Built In:**
  - **Number Rack & Math Dominoes:** Color-grouped 5-and-5 sliding blocks and tactile domino tiles let young learners spot combinations of 5, 10, and 12 without counting one-by-one.
  - **Quest Scoreboard:** Holds 60 identical `+10` $1\text{U}$ tokens ($19.0 \times 19.0 \times 7.0\text{ mm}$ visible height) and a $3 \times 1$ Snapfinity desktop scoreboard lid numbered `1`–`10` with a `100` Mastery Tower socket—place 1 token ($+10\text{ pts}$) when you solve a problem with blocks, and stack a 2nd token ($+20\text{ pts}$) when you verify it on the SC-6.
- **Download:** **[stackcalc.io/downloads](https://stackcalc.io/downloads/)**

### A.2.7 Probability Dice, Modular Spinner & Counting Array Studio
- **What It Teaches:** Multiplication arrays, area and perimeter on the Miniblock socket grid (`[f] [RECT]`, `[g] [TRI]`), commutative and distributive properties, and fair probability trials (`[🎲]`).
- **How the Math Is Built In:**
  - **Fair-Weight Dice & Modular Spinners:** Includes four $18\text{ mm}$ volume-equalized $d6$ dice (where pip depths are adjusted so all six faces remove the exact same volume of plastic), polyhedral dice ($d4, d6, d8, d10, d12, d20$), and a $1 \times 1$ spinner box with a 10-sector (`0–9`) lid plus drop-in Biased ($\frac{1}{2}\text{–}\frac{1}{4}\text{–}\frac{1}{4}$), Binary ($50/50$), and Operations ($+, -, \times, \div$) dials.
  - **Four-Color Counting Tiles:** Each student kit holds 24 gravity-docking tiles ($19.0 \times 19.0 \times 8.85\text{ mm}$ overall, with a $7.0\text{ mm}$ visible $1\text{U}$ step—so 12 stacked tiles equal the exact $84.0\text{ mm}$ Fraction Studio whole) across four colors (6 white, 6 blue, 6 gold, 6 slate; 144 tiles in a drop-front classroom Desktop Storage Case).

![Counting & Array Studio: Desktop Storage Case with COUNTING Plaque and [NUM] Badge](../assets/manuals/counting_tiles_box_3x1x13u.png)

![Counting & Array Studio: 4-Color Distributive 144-Tile Array (12x12)](../assets/manuals/counting_tiles_distributive_4color.png)

- **Download:** **[stackcalc.io/downloads/dice-and-spinner-open-source-stls.zip](https://stackcalc.io/downloads/dice-and-spinner-open-source-stls.zip)** and **[stackcalc.io/downloads/counting-tiles-open-source-stls.zip](https://stackcalc.io/downloads/counting-tiles-open-source-stls.zip)**

### A.2.8 Prime Factor Studio
- **What It Teaches:** Prime numbers (`[PRIME]`), prime factor trees (`[g] [FACT]`), Greatest Common Factor (`[GCF]`), and Least Common Multiple (`[f] [LCM]`).
- **How the Math Is Built In:** The drop-front Desktop Storage Case comparator box holds stackable $19.0 \times 19.0\text{ mm}$ prime factor blocks ($[2], [3], [5], [7], [11], [13], [17], [19], [23], [29]$ plus fused powers $2^2, 2^3, 3^2, 5^2$) harmonized to the $7.00\text{ mm}$ ($1\text{U}$) datum so the $[2]$ block has exact visible height $7.00\text{ mm}$ and **stacking blocks adds their heights to multiply their prime numbers**. Whether you build $12$ as $2 \times 2 \times 3$ or $3 \times 2 \times 2$, your factor tower reaches the exact same $25.09\text{ mm}$ `12` mark on the comparator scale—and comparing $20 = 2^2 \times 5$ ($30.25\text{ mm}$) beside $50 = 2 \times 5^2$ ($39.51\text{ mm}$) physically proves that $\text{GCF}(20,50) = 2 \times 5 = 10$ ($23.25\text{ mm}$) and $\text{LCM}(20,50) = 2^2 \times 5^2 = 100$ ($46.51\text{ mm}$) use the exact same prime blocks!

![Prime Factor Studio: Desktop Storage Case with Bilateral Factor Tower Comparator](../assets/manuals/prime_studio_comparator_stage.png)

| Target Number | Prime Building Blocks | Visible Block Heights Added Together (in $\text{mm}$) | Mark on Comparator Scale |
|:---:|:---|:---|:---:|
| **2** | $[2]$ | $7.00\text{ mm}$ ($1\text{U}$ base unit) | **Target 2** |
| **3** | $[3]$ | $11.09\text{ mm}$ | **Target 3** |
| **4** | $[2] \times [2]$ ($2^2$) | $7.00 + 7.00 = 14.00\text{ mm}$ | **Target 4** |
| **6** | $[2] \times [3]$ | $7.00 + 11.09 = 18.09\text{ mm}$ | **Target 6** |
| **10** | $[2] \times [5]$ | $7.00 + 16.25 = 23.25\text{ mm}$ | **Target 10** |
| **12** | $[2]^2 \times [3]$ | $14.00 + 11.09 = 25.09\text{ mm}$ | **Target 12** |
| **20** | $[2]^2 \times [5]$ | $14.00 + 16.25 = 30.25\text{ mm}$ | **Target 20** |
| **30** | $[2] \times [3] \times [5]$ | $7.00 + 11.09 + 16.25 = 34.35\text{ mm}$ | **Target 30** |
| **50** | $[2] \times [5]^2$ | $7.00 + 32.51 = 39.51\text{ mm}$ | **Target 50** |
| **60** | $[2]^2 \times [3] \times [5]$ | $14.00 + 11.09 + 16.25 = 41.35\text{ mm}$ | **Target 60** |
| **100** | $[2]^2 \times [5]^2$ | $14.00 + 32.51 = 46.51\text{ mm}$ | **Target 100** |

- **Download:** **[stackcalc.io/downloads/prime-factor-studio-open-source-stls.zip](https://stackcalc.io/downloads/prime-factor-studio-open-source-stls.zip)**

---

## A.3 Printable Cardstock Cutout Workshop (Scissors & Glue Nets)

If you don't have a 3D printer handy, you can print the full-scale paper nets from **[stackcalc.io/downloads](https://stackcalc.io/downloads/)** at $100\%$ scale on heavy cardstock ($110\text{ lb}$ index paper), score the dashed lines with an empty ballpoint pen, cut along the solid outer edges, and glue the tabs:

### A.3.1 Cardstock Net: Ten-Frame Tray ($125 \times 42\text{ mm}$ Base)

Score and fold the side flaps upward along the $125 \times 42\text{ mm}$ base to form a rigid two-row desktop ten-frame tray:

| Left Flap ($12 \times 42\text{ mm}$) | Ten-Frame Base ($125 \times 42\text{ mm}$) | Right Flap ($12 \times 42\text{ mm}$) |
| :---: | :---: | :---: |
| Fold & Glue Tab | Row 1: Cells `(1) (2) (3) (4) (5)` | Fold & Glue Tab |
| Fold & Glue Tab | Row 2: Cells `(6) (7) (8) (9) (10)` | Fold & Glue Tab |

### A.3.2 Cardstock Net: 84 mm Whole & 42 mm Half Fraction Towers

Fold the four vertical faces at $90^\circ$ angles and glue the side and bottom tabs to assemble hollow square fraction towers calibrated to the $84.0\text{ mm}$ datum:

| Face Left | Front Label Face | Face Right | Back Percent Face |
| :--- | :--- | :--- | :--- |
| **Whole ($1$):** $20 \times 84\text{ mm}$ | `"1 WHOLE"` ($20 \times 84\text{ mm}$) | $20 \times 84\text{ mm}$ | `"100%"` ($20 \times 84\text{ mm}$) |
| **Half ($1/2$):** $20 \times 42\text{ mm}$ | `"1/2"` ($20 \times 42\text{ mm}$) | $20 \times 42\text{ mm}$ | `"50%"` ($20 \times 42\text{ mm}$) |
| Bottom Cap ($20 \times 20\text{ mm}$) | Fold Glue Tab | Fold Glue Tab | Fold Glue Tab |

---

## A.4 System Configuration Flags (`[g] [FLAGS]`) & Studio Catalog

Teachers and parents can customize classroom settings anytime via the `[g] [FLAGS]` menu:

| Flag # | Default State | Classroom Purpose |
| :--- | :--- | :--- |
| **Flag 0** | `0` (Normal) | Math Exception Trap: `1` = Flash gentle hint & keep stack intact |
| **Flag 1** | `0` (Normal) | Battery Health: `1` = Low battery icon active |
| **Flag 2** | `0` (4-Stack) | Stack Depth Mode: `0` = 4-Stack XYZT, `1` = Simple 2-Stack |
| **Flag 3** | `0` (Degrees) | Angle Mode: `0` = Degrees ($360^\circ$), `1` = Pre-Algebra Turn Units |
| **Flag 4** | `0` (12-Hour) | Clock Format: `0` = 12-Hour Clock, `1` = 24-Hour Time |
| **Flag 5** | `0` (Dual Stack) | Screen Layout: `0` = Side-by-Side `Y \| X`, `1` = Large Single `X` |
| **Flag 6** | `0` (Silent) | Sound Chime: `0` = Classroom Silent, `1` = Click & Streak Beeps |
| **Flag 7** | `0` (Decimal) | Fraction Display: `0` = Decimal, `1` = Fraction (`a b/c`) |
| **Flag 8** | `0` (Manual) | Fraction Reduction: `0` = Step-by-Step `[g] [SIMP]`, `1` = Auto-Simplify |
| **Flag 9** | `0` (General) | Quiz Mode State: `1` = Active `[f] [?]` Math Sprint |

### A.4.1 Complete Manipulative Studio Quick-Reference

| Manipulative Kit Name | Tray Size | What's Inside the Box | Target Grades |
| :--- | :---: | :--- | :--- |
| **Ten-Frame Studio** | $3 \times 1 \times 7\text{U}$ | Dual $2 \times 5$ tray with 5-anchor rib & two-color counters | Foundational & Grades 3–6 |
| **Number Rack Studio** | $3 \times 1 \times 7\text{U}$ | Two horizontal rows of sliding subitizing blocks grouped $5+5$ by color | Foundational & Grades 3–6 |
| **Math Dominoes Studio** | $3 \times 1 \times 7\text{U}$ | Tactile math dominoes with 12-frame subitizing divider tray | Foundational & Grades 3–6 |
| **Place Value Studio** | $3 \times 1 \times 7\text{U}$ | $4 \times 2$ Whole & Decimal Place Value Trays, 44 digit miniblocks (`0`–`9`), and 9 `+1` regrouping blocks | Grades 3–6 |
| **Counting & Array Studio** | Desktop Case ($3 \times 1$) | 24 four-color $1\text{U}$ stacking tiles per student kit (144 per drop-front classroom box) | Grades 3–6 |
| **Planetary Geared Clock** | $3 \times 2 \times 7\text{U}$ | $12:1$ geared hands, 4 removable $90^\circ$ dial quadrants, and time blocks | Grades 3–6 |
| **84 mm Fraction Studio** | Desktop Case ($3 \times 1$) | 78 proportional fraction blocks ($1$ down to $1/12$, $84\text{ mm}$ datum) & lid comparator | Grades 3–6 |
| **Probability Dice & Spinner** | $1 \times 1 \times 7\text{U}$ | 4 fair $d6$ dice, polyhedral dice ($d4 \dots d20$), and 10-sector + 3 drop-in spinner dials | Grades 3–6 |
| **Unit Circle Volvelle** | $120\text{ mm}$ | Dual-ring rotary protractor and shadow-factor sight-window wheel | Grades 3–6 |
| **Prime Factor Studio** | Desktop Case ($3 \times 1$) | Stackable prime factor blocks ($[2] \dots [29]$) & comparator scale box | Grades 3–6 |
| **Algebra Factoring Studio** | $3 \times 1 \times 7\text{U}$ | 40 area-model tiles (squares, rods, and $\pm 1$ unit tiles) and interlocking $90^\circ$ L-Frame Stage | Grades 3–6 |
| **Quest Scoreboard** | $3 \times 1 \times 7\text{U}$ | 60 universal `+10` $1\text{U}$ tokens and 10-problem + 100-Point Mastery scoreboard lid | Grades 3–6 |

> **Companion Workbook Studio Mapping:** Every one of the **10 Units (45 Sections, 90 Two-Way Worksheets)** in the [Big Ideas Math Middle School Supplement](../curriculum/big-ideas-middle-school-sc6-workbook.md) pairs directly with these 3D-printed kits and the **Quest Scoreboard**—from **Counting Tiles** and **Prime Factor Blocks** in Unit 1 (Exponents, Factor Trees & GCF/LCM Venn Diagrams), **84 mm Fraction Towers** and **Place Value Trays** in Units 2–3 (Fractions, Decimals, Tape Diagrams & Percents), **Algebra Tiles** in Units 4, 7 & 10 (Algebraic Expressions & Balance-Scale Equations), the **Planetary Geared Clock** and **Unit Circle Volvelle** in Units 5 & 8 (2D Polygons, 3D Nets, Fractional Cube Packing & Elapsed Time), **Ten-Frame** two-color zero-pairs in Unit 6 (Signed Integers & Coordinate Plane), to **Polyhedral Dice & Spinners** in Units 9 & 10 (Fair-Share Mean, MAD & Experimental Probability).

---

## A.5 How We Built the StackCalc Learning Lab: Open-Source Hardware & Hackaday Build Logs

Curious how a calculator, nine 3D-printed block kits, and this math book were invented together? We documented every step of our journey on our open-source **[Hackaday Engineering Blog](https://hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator)** and at **[stackcalc.io](https://stackcalc.io)**. Here is the behind-the-scenes story of how open-source hardware engineering, physical block design, and screen simulation came together to build StackCalc:

### A.5.1 Starting on a Tiny Apple Watch Screen—and Sharing One Math Brain
StackCalc began on a wristwatch. When you try to do math on an Apple Watch screen that is barely $40\text{ millimeters}$ wide, there is no room for tiny `( )` parenthesis buttons or long scrolling formulas. Reverse Polish Notation (RPN)—the 4-story Number Elevator you use in this book—made watch math direct and practical: you type your two numbers, see them sitting right on Shelf $Y$ and Shelf $X$, and tap the operation key.

As we expanded from the watch to the iPhone, the web browser, and our physical handheld calculators (`SC-6` and `SC-32`), we made a strict rule: **every device would share the exact same mathematical brain.** Whether you tap `[g] [SIMP]` on a handheld SC-6 at your desk or click it in the web simulator at **[stackcalc.io](https://stackcalc.io)**, every shelf of the stack behaves the exact same way.

### A.5.2 Calibrating Physical Blocks to Match the Screen
Why are the Counting Tiles $7.0\text{ mm}$ tall and the Whole Fraction Tower $84.0\text{ mm}$ tall? Because $84 = 12 \times 7$! By choosing a height that divides evenly by $1, 2, 3, 4, 6,$ and $12$, every fraction block—halves ($42\text{ mm}$), thirds ($28\text{ mm}$), fourths ($21\text{ mm}$), sixths ($14\text{ mm}$), and twelfths ($7\text{ mm}$)—can be printed to an exact whole-millimeter height without messy decimal fractions of a millimeter. When you stack three $\frac{1}{4}$ blocks ($63\text{ mm}$) beside two $\frac{1}{3}$ blocks ($56\text{ mm}$), your fingertips feel the $1\frac{5}{12}$ tower height before you even type `. 3 . 4 [ENTER] . 2 . 3 [+]` on the keypad.

### A.5.3 Testing a Virtual Calculator Before Building the Real One
Before we ever ordered a physical circuit board or soldered a single button, we built a **virtual hardware simulator** that runs right on a computer screen. It draws the exact $132 \times 65$ pixel display—including the live Ten-Frame dots (`[▦]`), Number Line jump arcs (`[f] [LINE]`), and Geared Clock hands (`[🕒]`)—so teachers and students could test every button and Math Quiz sprint (`[f] [?]`) while the physical parts were still being 3D-printed.

### A.5.4 3D Printing Directly from the Circuit Board & Snap-Together Assembly
Have you ever opened a toy or calculator and found tiny metal screws that strip out the plastic or roll off the table and get lost? In our Hackaday build logs (*"How the Circuit Board Design Shapes the Printed Calculator"* and *"Tool-Free Sliding Assembly"*), we showed how we eliminated external case screws:
- **Circuit-Board-Driven 3D Models:** Instead of measuring the circuit board with a ruler and guessing where the buttons and screen holes should go, our 3D-printing program reads the exact button coordinates directly from the circuit board design file. Every keycap hole lines up automatically.
- **4-Piece Sliding Lock:** The calculator case prints in four interlocking pieces (bottom shell, button frame, top faceplate, and a side-locking rail) that slide together like a puzzle box and lock tight with a single click, which locks the internal circuit board and battery contacts securely in place—and all of your desktop math block trays print on any classroom 3D printer with zero support plastic to peel off.

For complete classroom lesson scripts and station activities that use these manipulatives, turn to **[Appendix B: Teacher Lesson Plans & Diagnostic Protocols](sc6/appendix-b-teacher-lesson-plans.md)**.

---

# Appendix B: Teacher Lesson Plans & Diagnostic Protocols

## B.1 Station Facilitation Model & Workshop Architecture

The StackCalc SC-6 curriculum follows the **Math Workshop Rotation Model**, where every mathematical concept moves naturally from physical blocks to visual sketches to the four-register number stack:

| Time Window | Phase | Activity & Student Experience |
| :---: | :--- | :--- |
| **00:00 – 05:00** | Whole-Class Warm-Up | Pose the real-world narrative challenge and frame the question. |
| **05:00 – 20:00** | Station Investigation | Hands-on physical manipulative build at studio stations. |
| **20:00 – 35:00** | Stack Verification & Practice | SC-6 four-register stack verification and keystroke logging. |
| **35:00 – 45:00** | Discourse & Exit Ticket | Mathematical reflection, diagnostic check, and notebook log. |

### B.1.1 Four-Register Stack Elevator Mental Model
For elementary students, the four-register RPN stack ($X, Y, Z, T$) is taught as a four-story glass elevator:
- **Floor 1 (Register $X$):** The Lobby / Ground Floor where current typing happens.
- **Floor 2 (Register $Y$):** The First Balcony where numbers wait for two-number operations.
- **Floor 3 (Register $Z$):** The Second Balcony for intermediate storage.
- **Floor 4 (Register $T$):** The Penthouse / Constant Dispenser that duplicates downward during continuous operations.

> **Middle School Supplement Station Alignment:** For Grades 5–7 classrooms, the station rotation model in this appendix scales directly into the **10 Units (45 Sections, 90 Worksheets)** of the [Big Ideas Math Middle School Supplement](../curriculum/big-ideas-middle-school-sc6-workbook.md): **Unit 1** (Exponents, Order of Operations & Prime Factor Studio GCF/LCM Venn Diagrams), **Unit 2** (Fraction Tower Multiplication/Division & Place Value Studio Decimals), **Unit 3** (Tape Diagrams, Unit Rates & Percents), **Unit 4** (Expressions, Distributive L-Frames & Factoring), **Unit 5** (2D Polygon Areas & Planetary Geared Clock Elapsed Time), **Unit 6** (Signed Integers, `[g] [|x|]` & Coordinate Plane), **Unit 7** (Balance-Scale Equations & Inequalities), **Unit 8** (`[Σ+]` 3D Surface Area Nets, Fractional Cube Volume & Circles), **Unit 9** (Counting Tile Fair-Share Mean, `[g] [MAD]`, Box Plots & Histograms), and **Unit 10** (Signed Rational Numbers, Two-Step Equations & Polyhedral Dice Probability). Each worksheet includes two-way verification and **Quest Scoreboard** tracking.

---

## B.2 Foundational Fluency & Grade 3 Readiness Warm-Up Stations

Foundational fluency stations build one-to-one correspondence, five-and-ten subitizing, tower comparisons, place-value bundling, and skip-counting fluency as warm-up and intervention stations for Grades 3–6 classrooms using physical Ten-Frame trays, Place Value Trays, and Counting Tiles alongside `[▦]` Ten-Frame Mode.

### Station F.1: One-to-One Correspondence & Counting to 10
- **Standards:** CCSS.MATH.CONTENT.3.NBT.A.2 (Foundational Readiness); TEKS 3.2.A.
- **Learning Objective:** Students will place up to 10 physical counters onto a Ten-Frame Studio tray while stepping through counts on the SC-6 LCD display using Ten-Frame Mode (`[▦]`).
- **Manipulatives:** Ten-Frame Studio tray, 10 two-color flip counters (yellow/red).
- **Warm-Up Activity (5 min):** "Place 4 yellow counters in the top row. Count them with your finger: one, two, three, four. Now tap one red counter into the next space. How many now?"

![Ten-Frame Studio: 5-Anchor Subitizing (5 Red + 3 Green = 8, 2 Empty to 10) and 70.0 mm 10-Rod Height Parity](../assets/manuals/ten_frame_subitizing_5anchor.png)

**Guided Facilitation Walkthrough:**
1. **Prompt:** "Hold up your SC-6 calculator. Tap the Ten-Frame key `[▦]`. Look at the glass screen. Do you see the two empty rows of five boxes, just like your wooden tray?" *(Expected response: Yes, it looks like our tray.)*
2. **Prompt:** "Now, let us drop one counter into both trays at the same time. Place one yellow counter on your tray. At the same time, tap `1 [+]` on your calculator. What popped onto your screen?" *(Expected response: A little dot filled the first box.)*
3. **Prompt:** "Tap `1 [+]` again. And again. Stop when your top row is full. How many counters are in the top row?" *(Expected response: Five.)*
4. **Prompt:** "What number shows in the corner?" *(Expected response: 5.)*

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[▦]` | 0 | 0 | 0 | 0 (10F) |
| `1 [+]` | 0 | 0 | 0 | 1 (10F) |
| `1 [+]` | 0 | 0 | 0 | 2 (10F) |
| `1 [+]` | 0 | 0 | 0 | 3 (10F) |
| `1 [+]` | 0 | 0 | 0 | 4 (10F) |
| `1 [+]` | 0 | 0 | 0 | 5 (10F) |

**Student Practice Problems:**
1. Count out 7 counters on the tray and match with 7 dots on the SC-6 (`[▦] 7`).
2. Show 10 full dots on the screen. How many rows are filled? (Both rows, answer: 10).
3. Clear the frame (`[C] [▦]`). Enter 3 dots. How many empty boxes remain? (7 boxes).

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student taps keys rapidly, overshooting the physical counter count. | Motor impulsivity without one-to-one correspondence pairing. | "One touch on the block, one tap on the key. Say 'click' for each." |
| Student starts filling the bottom row first. | Lacks left-to-right, top-to-bottom reading orientation. | "The top row is the attic. Fill the attic from left to right first." |

---

### Station F.2: Composing & Decomposing 5 (Number Bonds)
- **Standards:** CCSS.MATH.CONTENT.3.OA.C.7 (Foundational Readiness); TEKS 3.4.A.
- **Learning Objective:** Students decompose 5 into pairs ($4+1, 3+2, 2+3, 1+4$) using two-color counters and verify that the sum remains invariant.
- **Manipulatives:** 5 two-color counters, 1 Ten-Frame Studio tray.
- **Warm-Up Activity:** Shake 5 counters in a cup and spill them onto the desk. Count yellow vs. red.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "Spill your counters. Maya, how many yellow and how many red did you get?" *(Expected response: I got 3 yellow and 2 red.)*
2. **Prompt:** "Let us enter Maya's spill into our SC-6 elevator. Type `[3] [ENTER]`. The 3 rides up to the first balcony. Now type `[2]`. Look at Floor 1 and Floor 2. Press `[+]`. What is the total?" *(Expected response: 5.)*
3. **Prompt:** "Now spill again. David, what did you get?" *(Expected response: 4 yellow and 1 red.)*
4. **Prompt:** "Type `[4] [ENTER] [1] [+]`. What do you get?" *(Expected response: Still 5.)*

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[3]` | 0 | 0 | 0 | 3 |
| `[ENTER]` | 0 | 0 | 3 | 3 |
| `[2]` | 0 | 0 | 3 | 2 |
| `[+]` | 0 | 0 | 0 | 5 |

**Student Practice Problems:**
1. Enter $1 + 4$: `[1] [ENTER] [4] [+]`. Display shows `5`.
2. Enter $2 + 3$: `[2] [ENTER] [3] [+]`. Display shows `5`.
3. Enter $5 + 0$: `[5] [ENTER] [0] [+]`. Display shows `5`.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student types `32 [+]` without `[ENTER]`, getting 32. | Forgets stack lift separator. | "Press `[ENTER]` so the 3 can climb into the balcony before 2 enters the lobby." |
| Student thinks $3+2$ and $2+3$ have different totals. | Has not internalized commutativity. | "Turn your tray around $180^\circ$. Did any counters disappear?" |

---

### Station F.3: Comparing Quantities (More, Fewer, Same)
- **Standards:** CCSS.MATH.CONTENT.3.NBT.A.2 (Foundational Readiness); TEKS 3.2.D.
- **Learning Objective:** Students compare two side-by-side towers of counting tiles docked on the Counting & Array Studio lid, determine the height difference in tiles, and verify on SC-6 via subtraction.
- **Manipulatives:** Counting & Array Studio with $6 \times 2$ Snapfinity docking lid and 20 counting tiles (10 Cobalt Blue, 10 Amber Gold).
- **Warm-Up Activity:** Dock a tower of 7 blue tiles on the left lid socket and a tower of 4 gold tiles on the adjacent right socket. Run a finger across the tops of both towers to feel the step difference.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "Which tower stands taller on the docking lid?" *(Expected response: The blue tower with 7 tiles.)*
2. **Prompt:** "How many more tiles are in the blue tower? Let us ask the calculator to find the difference. Put the bigger number in first: `[7] [ENTER]`. Now put the smaller number in: `[4]`. Press `[-]`. What is the difference?" *(Expected response: 3.)*
3. **Prompt:** "Stack 3 more gold tiles onto the shorter gold tower. Run your finger across the tops of the two towers now—what happened?" *(Expected response: Their tops are completely flush. Both towers are 7 tiles tall, or $49.0\text{ mm}$.)*

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[7]` | 0 | 0 | 0 | 7 |
| `[ENTER]` | 0 | 0 | 7 | 7 |
| `[4]` | 0 | 0 | 7 | 4 |
| `[-]` | 0 | 0 | 0 | 3 |

**Student Practice Problems:**
1. Compare 9 and 5: `[9] [ENTER] [5] [-]`. Difference is `4`.
2. Compare 8 and 8: `[8] [ENTER] [8] [-]`. Difference is `0` (balanced).
3. Compare 6 and 2: `[6] [ENTER] [2] [-]`. Difference is `4`.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student enters `[4] [ENTER] [7] [-]` and gets `-3`. | Operates with smaller number first. | "In subtraction, the heavy tower enters the elevator first." |
| Student equates physical height with numerical quantity when using mismatched objects. | Perceptual salience over unit count. | "Count the cubes one-by-one; do not just look with your eyes." |

---

### Station F.4: Bridging Through 10 with the Ten-Frame
- **Standards:** CCSS.MATH.CONTENT.3.NBT.A.2 (Foundational Readiness); TEKS 3.4.A.
- **Learning Objective:** Students solve $8 + 5$ by decomposing 5 into $2 + 3$, filling the first ten-frame, and recognizing that $8 + 5 = 10 + 3 = 13$.
- **Manipulatives:** 2 Ten-Frame Studio trays side-by-side, 20 two-color counters.
- **Warm-Up Activity:** Place 8 counters in the first frame. Place 5 in hand. How many are needed to fill the first frame?

**Guided Facilitation Walkthrough:**
1. **Prompt:** "We have 8 yellow counters in Tray 1. We want to add 5 red counters. Where must the first 2 red counters go?" *(Expected response: They must go in the empty spots of Tray 1 to make 10.)*
2. **Prompt:** "Good. That makes 10. How many red counters are still in your hand?" *(Expected response: 3 counters.)*
3. **Prompt:** "Put them in Tray 2. So 8 plus 5 is the same as 10 plus 3. Let us see this on the SC-6. Type `[8] [ENTER] [5] [+]`. What do you get?" *(Expected response: 13.)*
4. **Prompt:** "Now press `[▦]`. See the two frames on screen: one completely full (10), and the second has 3 dots."

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[8]` | 0 | 0 | 0 | 8 |
| `[ENTER]` | 0 | 0 | 8 | 8 |
| `[5]` | 0 | 0 | 8 | 5 |
| `[+]` | 0 | 0 | 0 | 13 |
| `[▦]` | 0 | 0 | 0 | 13(10F) |

**Student Practice Problems:**
1. Solve $9 + 6$: `[9] [ENTER] [6] [+] [▦]`. Display shows 10 + 5 = 15.
2. Solve $7 + 5$: `[7] [ENTER] [5] [+] [▦]`. Display shows 10 + 2 = 12.
3. Solve $8 + 7$: `[8] [ENTER] [7] [+] [▦]`. Display shows 10 + 5 = 15.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student counts on fingers starting from 1 ($1, 2, 3 \dots 13$). | Lacks ten-structuring automaticity. | "Lock the 8 in your mind. How many to 10? Two. Now add the rest." |
| Student places all 5 in the second frame, leaving first incomplete. | Does not recognize benchmark 10 constraint. | "A ten-frame must be full before you open a new one." |

---

### Station F.5: Commutative Property of Addition (The Turn-Around Rule: $3 + 7 = 7 + 3$)
- **Standards:** CCSS.MATH.CONTENT.3.NBT.A.2 (Foundational Readiness); TEKS 3.4.A.
- **Learning Objective:** Students construct two towers ($3+7$ and $7+3$) and use the exchange key `[x⇄y]` on the SC-6 to prove sum invariance.
- **Manipulatives:** Four-color counting tiles (blue and gold).
- **Warm-Up Activity:** Build a tower of 3 blue tiles stacked onto 7 gold tiles. Turn the tower over.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "Enter `[3] [ENTER] [7]`. Register $Y$ has 3, Register $X$ has 7. Press `[x⇄y]`. What happened?" *(Expected response: They swapped places. 7 is on top, 3 is on bottom.)*
2. **Prompt:** "Press `[+]`. What is the sum?" *(Expected response: 10.)*
3. **Prompt:** "Press `[f] [LASTX] [3] [+]`. It is still 10. Flipping the order never changes the sum."

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[3]` | 0 | 0 | 0 | 3 |
| `[ENTER]` | 0 | 0 | 3 | 3 |
| `[7]` | 0 | 0 | 3 | 7 |
| `[x⇄y]` | 0 | 0 | 7 | 3 |
| `[+]` | 0 | 0 | 0 | 10 |

**Student Practice Problems:**
1. Test $4 + 8$ vs. $8 + 4$: `[4] [ENTER] [8] [+]` = 12; `[8] [ENTER] [4] [+]` = 12.
2. Test $2 + 9$ vs. $9 + 2$: both equal 11.
3. Test $6 + 5$ vs. $5 + 6$: both equal 11.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student assumes subtraction is also commutative ($7-3 = 3-7$). | Overgeneralizes additive symmetry to non-symmetric operations. | "Try `[3] [ENTER] [7] [-]` on your calculator. Do you get 4 or -4?" |

---

### Station F.6: Number Bonds & Part-Whole Missing Addends
- **Standards:** CCSS.MATH.CONTENT.3.OA.D.8 (Foundational Readiness); TEKS 3.5.A.
- **Learning Objective:** Students solve missing addend problems ($? + 6 = 14$) by modeling whole-part subtraction on the SC-6.
- **Manipulatives:** 14 counting tiles from the Counting Studio; cup hiding an unknown number.
- **Warm-Up Activity:** Place 14 tiles on desk. Teacher hides 6 under a cup. How many are visible? (8 tiles).

**Guided Facilitation Walkthrough:**
1. **Prompt:** "We started with a set of 14 tiles. I put some under this cup, and 6 are left on the desk. How do we find what is under the cup?" *(Expected response: Take away the 6 from the 14.)*
2. **Prompt:** "Key it into the SC-6: Whole set first: `14 [ENTER]`. Visible part second: `[6]`. Take it away: `[-]`. What is in the lobby?" *(Expected response: 8.)*
3. **Prompt:** "Lift the cup and count the tiles: 8."

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `14` | 0 | 0 | 0 | 14 |
| `[ENTER]` | 0 | 0 | 14 | 14 |
| `[6]` | 0 | 0 | 14 | 6 |
| `[-]` | 0 | 0 | 0 | 8 |

**Student Practice Problems:**
1. $? + 5 = 12$: `12 [ENTER] [5] [-]` = 7.
2. $? + 9 = 16$: `16 [ENTER] [9] [-]` = 7.
3. $? + 8 = 15$: `15 [ENTER] [8] [-]` = 7.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student adds $14 + 6$ to get 20. | Keywords trigger addition without spatial whole-part analysis. | "Can the hidden part be bigger than the whole train?" |

---

### Station F.7: Place Value: Bundling 10 Ones into 1 Ten
- **Standards:** CCSS.MATH.CONTENT.3.NBT.A.1 (Foundational Readiness); TEKS 3.2.A.
- **Learning Objective:** Students stack ten $7.0\text{ mm}$ ($1\text{U}$) unit miniblocks to match a $70.0\text{ mm}$ ($10\text{U}$) 10-Rod and trade 10 ones for 1 ten on the Place Value Tray.
- **Manipulatives:** Place Value Studio (Whole Numbers Tray, digit miniblocks, and `+1` regrouping unit blocks) plus the $70.0\text{ mm}$ 10-Rod from the Ten-Frame Studio.
- **Warm-Up Activity:** Count out 13 single $1\text{U}$ miniblocks. Stack 10 of them beside the $70.0\text{ mm}$ 10-Rod, then trade 10 ones into the `TENS` column of the Place Value Tray.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "Stack 10 unit miniblocks into a tower and stand it beside the 10-Rod. Do they have the exact same $70.0\text{ mm}$ height?" *(Expected response: Yes, the exact same height.)*
2. **Prompt:** "Trade those 10 ones for a `1` in the `TENS` socket and dock `3` in the `ONES` socket of your Place Value Tray. Now what do you have on your tray?" *(Expected response: One ten and three ones.)*
3. **Prompt:** "Type `13` on the SC-6. The digit 1 means 1 full bundle of ten. The digit 3 means 3 loose ones."

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `10` | 0 | 0 | 0 | 10 |
| `[ENTER]` | 0 | 0 | 10 | 10 |
| `[3]` | 0 | 0 | 10 | 3 |
| `[+]` | 0 | 0 | 0 | 13 |

**Student Practice Problems:**
1. Model 2 tens and 5 ones: `20 [ENTER] [5] [+]` = 25.
2. Model 3 tens and 8 ones: `30 [ENTER] [8] [+]` = 38.
3. Model 4 tens and 0 ones: `40 [ENTER] [0] [+]` = 40.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student writes '103' for thirteen. | Writes numbers concatenating 10 and 3. | "The 1 ten already carries the 0 inside it until the 3 sits in its seat." |

---

### Station F.8: Skip-Counting Ladders with Constant Repeat (`[g] [REP]`)
- **Standards:** CCSS.MATH.CONTENT.3.OA.A.1 (Foundational Readiness); TEKS 3.4.E.
- **Learning Objective:** Students generate skip-counting sequences (twos, fives, tens) using continuous stack replication (`[g] [REP]`).
- **Manipulatives:** Counting tiles from Counting Studio stacked in towers of 5.
- **Warm-Up Activity:** Line up six towers of 5 tiles. Skip-count aloud: 5, 10, 15, 20, 25, 30.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "Today we teach our calculator to skip-count automatically using Constant Repeat: `[g] [REP]`. Type `[5]`. Now press `[g] [REP]`. What did `[g] [REP]` do?" *(Expected response: It copied 5 into all four elevator floors: T, Z, Y, and X.)*
2. **Prompt:** "Now press `[+]` once. What is on Floor 1?" *(Expected response: 10.)*
3. **Prompt:** "Tap `[+]` again, and again." *(Expected response: 15, 20, 25, 30.)*
4. **Prompt:** "Floor $T$ at the top of the elevator keeps dispensing a fresh 5 every time you add."

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[5]` | 0 | 0 | 0 | 5 |
| `[g] [REP]` | 5 | 5 | 5 | 5 |
| `[+]` | 5 | 5 | 5 | 10 |
| `[+]` | 5 | 5 | 5 | 15 |
| `[+]` | 5 | 5 | 5 | 20 |

**Student Practice Problems:**
1. Skip-count by 2 up to 16: `[2] [g] [REP] [+] ...`
2. Skip-count by 10 up to 70: `10 [g] [REP] [+] ...`
3. Skip-count by 3 up to 21: `[3] [g] [REP] [+] ...`

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student taps `[ENTER]` instead of `[+]`. | Confuses stack replication with arithmetic operation. | "`[ENTER]` lifts passengers up; `[+]` brings the top passenger down to combine." |

---

### Station F.9: Two-Digit Addition with Regrouping
- **Standards:** CCSS.MATH.CONTENT.3.NBT.A.2 (Foundational Readiness); TEKS 3.4.A.
- **Learning Objective:** Students solve $38 + 27$ by modeling tens and ones on the Place Value Studio Whole Numbers Tray and confirming the regrouped sum on the SC-6.
- **Manipulatives:** Place Value Studio: Whole Numbers Tray (`1000 | 100 | 10 | 1`), digit miniblocks (`0`–`9`), and stackable `+1` regrouping unit blocks (plus Counting Tiles).
- **Warm-Up Activity:** Dock `3` tens and `8` ones in the top row ($38$) and `2` tens and `7` ones in the bottom row ($27$). Combine the ones ($8 + 7 = 15$) and trade 10 unit blocks for $+1$ in the `TENS` column.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "When we combined 8 ones and 7 ones, we got 15 ones. What do we do when we have 10 or more ones in the `ONES` column?" *(Expected response: Trade 10 ones for 1 ten in the `TENS` column.)*
2. **Prompt:** "Now check your `TENS` column: 3 tens + 2 tens + 1 traded ten = 6 tens, and 5 ones remain in `ONES`. That is 65. Let us confirm on SC-6: `38 [ENTER] 27 [+]`." *(Expected response: 65.)*

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `38` | 0 | 0 | 0 | 38 |
| `[ENTER]` | 0 | 0 | 38 | 38 |
| `27` | 0 | 0 | 38 | 27 |
| `[+]` | 0 | 0 | 0 | 65 |

**Student Practice Problems:**
1. $46 + 28$: `46 [ENTER] 28 [+]` = 74.
2. $57 + 35$: `57 [ENTER] 35 [+]` = 92.
3. $19 + 64$: `19 [ENTER] 64 [+]` = 83.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student adds tens and ones separately on paper and writes '515' ($3+2=5, 8+7=15$). | Fails to carry regrouped ten into the tens column. | "15 ones has a full ten inside it. Trade 10 ones into the `TENS` column first." |

---

### Station F.10: Two-Digit Subtraction with Decomposition
- **Standards:** CCSS.MATH.CONTENT.3.NBT.A.2 (Foundational Readiness); TEKS 3.4.A.
- **Learning Objective:** Students solve $52 - 26$ by unbundling 1 ten from the `TENS` column into ten `+1` unit blocks in the `ONES` column.
- **Manipulatives:** Place Value Studio (Whole Numbers Tray, digit miniblocks, and `+1` regrouping blocks).
- **Warm-Up Activity:** Dock `5` in `TENS` and `2` unit blocks in `ONES` ($52$). Try to take away 6 ones and observe that only 2 ones sit in the `ONES` column.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "We have 5 tens and 2 ones on our Place Value Tray. We need to take away 26, which means 2 tens and 6 ones. Can we take 6 ones from 2 ones?" *(Expected response: No, not enough ones.)*
2. **Prompt:** "How can we get 10 more ones into the `ONES` column?" *(Expected response: Trade 1 ten from the `TENS` column for 10 `+1` unit blocks.)*
3. **Prompt:** "Do that now. You have `4` in `TENS` and 12 unit blocks in `ONES`. Take away 6 ones: 6 remain. Take away 2 tens: 2 remain. Answer: 26. Key it in: `52 [ENTER] 26 [-]`." *(Expected response: 26.)*

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `52` | 0 | 0 | 0 | 52 |
| `[ENTER]` | 0 | 0 | 52 | 52 |
| `26` | 0 | 0 | 52 | 26 |
| `[-]` | 0 | 0 | 0 | 26 |

**Student Practice Problems:**
1. $63 - 27$: `63 [ENTER] 27 [-]` = 36.
2. $71 - 38$: `71 [ENTER] 38 [-]` = 33.
3. $80 - 45$: `80 [ENTER] 45 [-]` = 35.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student subtracts smaller from larger digit on paper ($6-2=4$, writing 34). | Avoidance of regrouping by inverting digit roles. | "The top number is what you have in the bank. You cannot steal from the bottom number." |

---

### Station F.11: Even and Odd Numbers via Equal Pairing & `[g] [÷R]`
- **Standards:** CCSS.MATH.CONTENT.3.OA.D.9 (Foundational Readiness); TEKS 3.4.I.
- **Learning Objective:** Students determine if a number is even or odd by pairing counters and checking for remainder 0 vs. 1 using `[g] [÷R]`.
- **Manipulatives:** 15 counters per student pair.
- **Warm-Up Activity:** Pair up 11 counters in two parallel rows. Does one counter stick out alone?

**Guided Facilitation Walkthrough:**
1. **Prompt:** "Line up 11 counters in pairs of two. Is there a leftover counter without a partner?" *(Expected response: Yes, one counter is left over.)*
2. **Prompt:** "That means 11 is an *odd* number. Let us test with Quotient & Remainder: `[g] [÷R]`. Type `11 [ENTER] [2] [g] [÷R]`."
3. **Prompt:** "Register $X$ shows 5 pairs. Now press `[x⇄y]`. What is in Register $Y$?" *(Expected response: 1. The remainder is 1.)*
4. **Prompt:** "Any number with a remainder of 1 when divided by 2 is ODD. If the remainder is 0, it is EVEN."

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `11` | 0 | 0 | 0 | 11 |
| `[ENTER]` | 0 | 0 | 11 | 11 |
| `[2]` | 0 | 0 | 11 | 2 |
| `[g] [÷R]` | 0 | 0 | 1 (Rem) | 5 (Quot) |
| `[x⇄y]` | 0 | 0 | 5 (Quot) | 1 (Rem) |

**Student Practice Problems:**
1. Test 14: `14 [ENTER] [2] [g] [÷R] [x⇄y]` $\to$ Remainder 0 (EVEN).
2. Test 17: `17 [ENTER] [2] [g] [÷R] [x⇄y]` $\to$ Remainder 1 (ODD).
3. Test 20: `20 [ENTER] [2] [g] [÷R] [x⇄y]` $\to$ Remainder 0 (EVEN).

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student looks only at first digit of two-digit number (e.g. thinking 16 is odd because 1 is odd). | Ignores place value significance of ones digit. | "Look only at the ones place. Can 6 ones be shared equally?" |

---

## B.3 Grade 3 Lesson Plans (Ages 8–9)

Grade 3 stations transition from additive counting to 2D rectangular arrays (`[f] [RECT]`), fair-share division with remainders (`[g] [÷R]`), unit fraction towers, and polygon perimeters (`[Σ+]`).

### B.3.1 Lesson 3.1: Arrays, Equal Groups & Area with `[f] [RECT]`
- **Standards:** CCSS.MATH.CONTENT.3.OA.A.1, 3.MD.C.7; TEKS 3.4.D, 3.6.C.
- **Learning Objective:** Students construct a $6 \times 4$ array, compute area using `[f] [RECT]`, and rotate it $90^\circ$ to demonstrate commutativity ($6 \times 4 = 4 \times 6 = 24$).
- **Manipulatives:** Four-Color Counting Studio (24-tile student kit in a Desktop Storage Case, or shared 144-tile 6-kit classroom pack), Gridfinity $4 \times 4$ coordinate baseplate.
- **Warm-Up Activity:** Build a rectangle 6 tiles long and 4 tiles wide using 24 counting tiles on the baseplate.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "How many columns of 4 tiles did you make?" *(Expected response: 6 columns.)*
2. **Prompt:** "Count all the tiles covering the rectangle. How many?" *(Expected response: 24 tiles.)*
3. **Prompt:** "In geometry, the surface covered by tiles is called *area*. On the SC-6, we have a dedicated geometry key: `[f] [RECT]`. Type `[6] [ENTER] [4]`."
4. **Prompt:** "Now press `[f] [RECT]`. What is the area?" *(Expected response: 24.)*
5. **Prompt:** "Turn the tray sideways. Now it is 4 columns of 6. Test: `[4] [ENTER] [6] [f] [RECT]`. Still 24."

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[6]` | 0 | 0 | 0 | 6 |
| `[ENTER]` | 0 | 0 | 6 | 6 |
| `[4]` | 0 | 0 | 6 | 4 |
| `[f] [RECT]` | 0 | 0 | 0 | 24 |

**Student Practice Problems:**
1. $7 \times 5$ rug: `[7] [ENTER] [5] [f] [RECT]` = 35 square units.
2. $8 \times 3$ garden bed: `[8] [ENTER] [3] [f] [RECT]` = 24 square units.
3. $9 \times 4$ patio: `[9] [ENTER] [4] [f] [RECT]` = 36 square units (built by combining two 24-tile partner kits).

**Classroom Station Partner Game: "Capture the Rectangle":**
* **Materials:** Four-Color Counting Tiles (shared 144-tile classroom pack across 4 players: Player 1 in Archival White, Player 2 in Cobalt Blue Silk, Player 3 in Radiant Gold Silk, and Player 4 in Slate Blue-Gray PLA), SC-6 Calculator, 2 Polyhedral Dice (or roll via `[🎲]`).
* **Gameplay:** Player 1 rolls two factors (e.g., 5 and 4). Player 1 calculates area on the SC-6 (`5 [ENTER] 4 [×] = 20`), assembles a $5 \times 4$ rectangle in their color, and claims their territory on the table. Player 2 rolls, computes, assembles, and places their rectangle adjacent to Player 1.
* **The Four-Color Challenge Rule:** Placed rectangles of the same color cannot touch along a side. The SC-6 calculator serves as the referee: if a challenged player computes an area incorrectly, they forfeit their turn.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student confuses perimeter with area. | Conflates boundary fence with surface tiles. | "Trace the fence with your finger—that is perimeter. Lay your hand over the blocks—that is area." |

---

### B.3.2 Lesson 3.2: Division as Fair Sharing vs. Grouping (`[g] [÷R]`)
- **Standards:** CCSS.MATH.CONTENT.3.OA.A.2; TEKS 3.4.H.
- **Learning Objective:** Students model dividing 23 tiles among 4 Gridfinity holding bays, finding quotient 5 and remainder 3 using `[g] [÷R]`.
- **Manipulatives:** 23 Four-Color Counting Tiles (from a single 24-tile student kit), 4 Gridfinity sorting trays/bays.
- **Warm-Up Activity:** Deal 23 counting tiles one by one into the 4 trays until no more equal rounds can be dealt.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "How many cookies ended up in each cup?" *(Expected response: 5 cookies.)*
2. **Prompt:** "How many cookies are left on the table that cannot be shared equally?" *(Expected response: 3 cookies.)*
3. **Prompt:** "Let us verify with the SC-6 quotient and remainder engine. Dividend first: `23 [ENTER]`. Divisor second: `[4]`. Quotient & Remainder: `[g] [÷R]`. What is in Register $X$?" *(Expected response: 5, the quotient.)*
4. **Prompt:** "Press `[x⇄y]`. What is in Register $Y$?" *(Expected response: 3, the remainder.)*

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `23` | 0 | 0 | 0 | 23 |
| `[ENTER]` | 0 | 0 | 23 | 23 |
| `[4]` | 0 | 0 | 23 | 4 |
| `[g] [÷R]` | 0 | 0 | 3 (Rem) | 5 (Quot) |
| `[x⇄y]` | 0 | 0 | 5 (Quot) | 3 (Rem) |

**Student Practice Problems:**
1. 19 markers shared among 3 pencil cases: `19 [ENTER] [3] [g] [÷R]` $\to$ Quotient = 6, Remainder = 1.
2. 31 apples packed into bags of 6: `31 [ENTER] [6] [g] [÷R]` $\to$ Quotient = 5, Remainder = 1.
3. 35 tiles partitioned into teams of 4: `35 [ENTER] [4] [g] [÷R]` $\to$ Quotient = 8, Remainder = 3.

**Classroom Station Partner Game: "Remainder Race to Bank":**
* **Materials:** 36 Counting Tiles (combining two partner 24-tile kits), 1 Die, SC-6 Calculator.
* **Gameplay:** Players start with a shared pool of 36 tiles. Player 1 rolls a die (e.g., 5) and keys `36 [ENTER] 5 [g] [÷R]`. Line $X$ displays quotient 7 (which returns to the supply depot), and line $Y$ (`[x⇄y]`) displays remainder 1. Player 1 takes the 1 remainder tile into their personal bank.
* **Winning:** Players alternate turns with the remaining tiles. The player who banks the most remainder tiles wins the round.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student writes $23 \div 4 = 5.75$ and doesn't know what to do with the leftover cookies. | Standard decimal division obscures integer remainder context. | "Can you hand a guest $0.75$ of an unwrapped cookie at a party? Give them 5 cookies and keep 3 in the box." |

---

### B.3.3 Lesson 3.3: Introduction to Unit Fractions with Fraction Studio
- **Standards:** CCSS.MATH.CONTENT.3.NF.A.1; TEKS 3.3.A.
- **Learning Objective:** Students compare physical fraction towers ($\frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \frac{1}{6}, \frac{1}{8}$) against the $84.0\text{ mm}$ whole tower and understand that larger denominators produce smaller unit pieces.
- **Manipulatives:** Fraction Studio tower set.
- **Warm-Up Activity:** Place the 1-Whole tower ($84\text{ mm}$) on desk. Stack two $\frac{1}{2}$ blocks next to it. Observe equal heights.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "Hold up a $\frac{1}{2}$ block and a $\frac{1}{8}$ block. Which block is taller?" *(Expected response: The $\frac{1}{2}$ block is much taller.)*
2. **Prompt:** "Why is $\frac{1}{8}$ smaller if 8 is a bigger number than 2?" *(Expected response: Because you had to cut the same candy bar into 8 pieces instead of 2 pieces, so each slice is smaller.)*
3. **Prompt:** "Right. The denominator tells us how many equal pieces the whole was cut into. Enter $\frac{1}{2}$ on the SC-6: `[.] 1 [.] 2 [ENTER]`. Enter $\frac{1}{8}$: `[.] 1 [.] 8`. Now press `[-]`. The difference is positive: $\frac{1}{2}$ is $\frac{3}{8}$ larger."

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[.] 1 [.] 2` | 0 | 0 | 0 | 1/2 |
| `[ENTER]` | 0 | 0 | 1/2 | 1/2 |
| `[.] 1 [.] 8` | 0 | 0 | 1/2 | 1/8 |
| `[-]` | 0 | 0 | 0 | 3/8 |

**Student Practice Problems:**
1. Show that three $\frac{1}{3}$ blocks equal 1 whole: `[.] 1 [.] 3 [ENTER] [3] [×]` = 1.
2. Compare $\frac{1}{4}$ and $\frac{1}{2}$: `[.] 1 [.] 2 [ENTER] [.] 1 [.] 4 [-]` = $\frac{1}{4}$.
3. Show that four $\frac{1}{8}$ blocks equal $\frac{1}{2}$: `[.] 1 [.] 8 [ENTER] [4] [×]` = $\frac{1}{2}$.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student believes $\frac{1}{8} > \frac{1}{4}$ because $8 > 4$. | Whole-number bias applied to denominators. | "Place the physical $\frac{1}{8}$ tower next to the $\frac{1}{4}$ tower. Which one touches the ceiling first?" |

---

### B.3.4 Lesson 3.4: Perimeter of Polygons vs. Area using `[Σ+]`
- **Standards:** CCSS.MATH.CONTENT.3.MD.D.8; TEKS 3.7.B.
- **Learning Objective:** Students find the perimeter of a stepped or 5-sided polygon by accumulating side lengths with `[Σ+]`, distinguishing boundary distance from internal tile area.
- **Manipulatives:** Counting & Array Studio tiles, Algebra Factoring L-Frame Stage, and millimeter ruler.
- **Warm-Up Activity:** Arrange Counting & Array Studio tiles inside the $90^\circ$ L-Frame Stage to form a stepped pentagon outline with side lengths $6\text{ cm}, 4\text{ cm}, 4.2\text{ cm}, 4.2\text{ cm},$ and $4\text{ cm}$.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "To find the perimeter, we walk all the way around the outer boundary fence. Let us add the sides using our SC-6 statistical accumulator key `[Σ+]`. First, clear memory: `[g] [CLΣ]`."
2. **Prompt:** "Side 1 is 6 cm: `[6] [Σ+]`. Side 2 is 4 cm: `[4] [Σ+]`. Side 3 is 4.2 cm: `4.2 [Σ+]`. Side 4 is 4.2 cm: `4.2 [Σ+]`. Side 5 is 4 cm: `[4] [Σ+]`."
3. **Prompt:** "How many sides did we measure? $\text{Count} = 5$. Now press `[f] [Σx]`. What is the total perimeter?" *(Expected response: 22.4 centimeters.)*

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[g] [CLΣ]` | 0 | 0 | 0 | 0 |
| `[6] [Σ+]` | 0 | 0 | 0 | Count = 1 |
| `[4] [Σ+]` | 0 | 0 | 0 | Count = 2 |
| `4.2 [Σ+]` | 0 | 0 | 0 | Count = 3 |
| `4.2 [Σ+]` | 0 | 0 | 0 | Count = 4 |
| `[4] [Σ+]` | 0 | 0 | 0 | Count = 5 |
| `[f] [Σx]` | 0 | 0 | 0 | 22.4 |

**Student Practice Problems:**
1. Triangle with sides 5, 7, 8: `[g] [CLΣ] [5] [Σ+] [7] [Σ+] [8] [Σ+] [f] [Σx]` = 20.
2. Rectangle perimeter ($8 + 5 + 8 + 5$): `[f] [Σx]` = 26.
3. Hexagon with sides 3, 3, 4, 4, 5, 5: `[f] [Σx]` = 24.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student forgets to clear statistical memory before starting problem 2. | Persistent accumulator contamination. | "Always check the count on the screen. If the count is not zero, press `[g] [CLΣ]` before walking your fence." |

---

## B.4 Grade 4 Lesson Plans (Ages 9–10)

Grade 4 stations extend division to multi-digit remainders (`[g] [÷R]`), build equivalent fractions and step-by-step reductions (`[g] [SIMP]`), add and subtract unlike fractions, and measure angles with the $360^\circ$ Volvelle.

### B.4.1 Lesson 4.1: Long Division with Remainders (`[g] [÷R]`)
- **Standards:** CCSS.MATH.CONTENT.4.OA.A.3; TEKS 4.4.F.
- **Learning Objective:** Students solve a multi-step hiking trail provisioning problem ($89\text{ oz}$ water distributed into $16\text{ oz}$ flasks) using `[g] [÷R]`.
- **Manipulatives:** Place Value Studio (`8` in `TENS` and `9` in `ONES` to represent 89) or shared 144-tile classroom Counting Studio bin.
- **Warm-Up Activity:** Model a smaller proportional sample first with your 24-tile student kit (such as $20 \div 6 = 3\text{ R }2$), or count out 89 counting tiles from the shared 144-tile classroom station bin and group into 16-unit flasks to count full flasks and leftover ounces.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "We have 89 fluid ounces of water. Each water bottle holds 16 fluid ounces. How many full bottles can we pack, and how many ounces are left over?" *(Expected response: Type `89 [ENTER] 16 [g] [÷R]`.)*
2. **Prompt:** "What is on your screen?" *(Expected response: 5.)*
3. **Prompt:** "That is 5 full flasks. Now swap registers: press `[x⇄y]`. What is in Register $Y$?" *(Expected response: 9. 9 ounces left over.)*
4. **Prompt:** "Check your answer: 5 bottles times 16 oz is 80 oz, plus 9 oz equals 89 oz."

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `89` | 0 | 0 | 0 | 89 |
| `[ENTER]` | 0 | 0 | 89 | 89 |
| `16` | 0 | 0 | 89 | 16 |
| `[g] [÷R]` | 0 | 0 | 9 (Rem) | 5 (Quot) |
| `[x⇄y]` | 0 | 0 | 5 (Quot) | 9 (Rem) |

**Student Practice Problems:**
1. 145 campers into cabins of 12: `145 [ENTER] 12 [g] [÷R]` $\to$ Quotient = 12 cabins, Remainder = 1 camper.
2. 250 eggs packed in cartons of 12: `250 [ENTER] 12 [g] [÷R]` $\to$ Quotient = 20 cartons, Remainder = 10 eggs.
3. 500 pencils in packs of 24: `500 [ENTER] 24 [g] [÷R]` $\to$ Quotient = 20 packs, Remainder = 20 pencils.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student interprets remainder 9 as $0.9$ bottles. | Confuses integer discrete leftovers with decimal fraction. | "Is that 9 tenths of a bottle, or 9 whole ounces in the bottom of the pot? Remember the units." |

---

### B.4.2 Lesson 4.2: Equivalent Fractions & Simplification (`[g] [SIMP]`)
- **Standards:** CCSS.MATH.CONTENT.4.NF.A.1; TEKS 4.3.C.
- **Learning Objective:** Students build equivalent fraction models ($\frac{6}{8} = \frac{3}{4}$) and reduce them on the SC-6 using Step-by-Step Simplify (`[g] [SIMP]`).
- **Manipulatives:** Fraction Studio towers ($\frac{1}{8}$ and $\frac{1}{4}$ blocks).
- **Warm-Up Activity:** Line up six $\frac{1}{8}$ blocks in the channel. Find which group of $\frac{1}{4}$ blocks matches the exact length.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "How many $\frac{1}{4}$ blocks match six $\frac{1}{8}$ blocks?" *(Expected response: Three $\frac{1}{4}$ blocks.)*
2. **Prompt:** "So $\frac{6}{8}$ is equivalent to $\frac{3}{4}$. Now let us watch the SC-6 simplify it step-by-step. Enter six-eighths: `[.] 6 [.] 8 [ENTER]`. Press `[g] [SIMP]`. What does the screen show?" *(Expected response: `3/4`.)*
3. **Prompt:** "What factor did the calculator divide out from top and bottom?" *(Expected response: It divided both numbers by 2.)*
4. **Prompt:** "Now press `[g] [SIMP]` again. What does it say?" *(Expected response: `LOWEST TERMS`. It cannot be simplified any further because 3 is prime.)*

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[.] 6 [.] 8` | 0 | 0 | 0 | 6/8 |
| `[ENTER]` | 0 | 0 | 6/8 | 6/8 |
| `[g] [SIMP]` | 0 | 0 | 6/8 | 3/4 |
| `[g] [SIMP]` | 0 | 0 | 6/8 | 3/4 (LOWEST) |

**Student Practice Problems:**
1. Simplify $\frac{8}{12}$: `[.] 8 [.] 12 [ENTER] [g] [SIMP]` = $\frac{2}{3}$.
2. Simplify $\frac{10}{25}$: `[.] 10 [.] 25 [ENTER] [g] [SIMP]` = $\frac{2}{5}$.
3. Simplify $\frac{18}{24}$: `[.] 18 [.] 24 [ENTER] [g] [SIMP]` = $\frac{3}{4}$.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student divides numerator by 2 and denominator by 3 ($\frac{6 \div 2}{8 \div 4}$). | Fails to recognize that scaling requires multiplying or dividing by a whole fraction like $\frac{2}{2} = 1$. | "You must treat the top and bottom with equal justice. Divide both by the exact same number." |

---

### B.4.3 Lesson 4.3: Adding & Subtracting Fractions with Unlike Denominators
- **Standards:** CCSS.MATH.CONTENT.4.NF.B.3; TEKS 4.3.E.
- **Learning Objective:** Students solve $\frac{1}{2} + \frac{1}{4}$ and $\frac{2}{3} - \frac{1}{6}$ using Fraction Studio blocks and SC-6 fraction arithmetic.
- **Manipulatives:** Fraction Studio towers.
- **Warm-Up Activity:** Put one $\frac{1}{2}$ block and one $\frac{1}{4}$ block end-to-end. Measure total length with $\frac{1}{4}$ blocks.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "How many fourths fit across $\frac{1}{2} + \frac{1}{4}$?" *(Expected response: Three fourths.)*
2. **Prompt:** "Enter it on the SC-6: `[.] 1 [.] 2 [ENTER] [.] 1 [.] 4 [+]`. What is the result?" *(Expected response: `3/4`.)*
3. **Prompt:** "Now try a subtraction: $\frac{5}{6} - \frac{1}{3}$. Key: `[.] 5 [.] 6 [ENTER] [.] 1 [.] 3 [-]`. What do you get?" *(Expected response: `1/2`.)*

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[.] 1 [.] 2` | 0 | 0 | 0 | 1/2 |
| `[ENTER]` | 0 | 0 | 1/2 | 1/2 |
| `[.] 1 [.] 4` | 0 | 0 | 1/2 | 1/4 |
| `[+]` | 0 | 0 | 0 | 3/4 |

**Student Practice Problems:**
1. $\frac{1}{3} + \frac{1}{6}$: `[.] 1 [.] 3 [ENTER] [.] 1 [.] 6 [+]` = $\frac{1}{2}$.
2. $\frac{3}{4} - \frac{1}{8}$: `[.] 3 [.] 4 [ENTER] [.] 1 [.] 8 [-]` = $\frac{5}{8}$.
3. $\frac{2}{5} + \frac{3}{10}$: `[.] 2 [.] 5 [ENTER] [.] 3 [.] 10 [+]` = $\frac{7}{10}$.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student adds across numerators and denominators ($\frac{1}{2} + \frac{1}{4} = \frac{2}{6}$). | Treats numerator and denominator as independent whole numbers. | "Look at your blocks. Is $\frac{2}{6}$ bigger than $\frac{1}{2}$? No. You cannot add pieces of different sizes until they share a common name." |

---

### B.4.4 Lesson 4.4: Angles & Rotations with the $360^\circ$ Volvelle Protractor
- **Standards:** CCSS.MATH.CONTENT.4.MD.C.6; TEKS 4.7.C.
- **Learning Objective:** Students measure acute, right, and obtuse angles using the $360^\circ$ Volvelle and calculate supplementary and complementary angles.
- **Manipulatives:** Two-disc rotating Unit Circle Volvelle protractor, removable $90^\circ$ clock quadrant sectors, and $d4$/$d6$ polyhedral faces.
- **Warm-Up Activity:** Align the Volvelle pointer to $0^\circ$. Rotate the top disc to match the $90^\circ$ corner of a clock quadrant sector (or a square counting tile).

**Guided Facilitation Walkthrough:**
1. **Prompt:** "Rotate your Volvelle to the $120^\circ$ mark (4 hour marks on your Planetary Clock). What degree reading does the cursor line up with?" *(Expected response: 120 degrees.)*
2. **Prompt:** "If two angles sit on a straight line, their sum is $180^\circ$ (supplementary). How many degrees are left to make a straight line? Calculate on SC-6: `180 [ENTER] 120 [-]`." *(Expected response: 60 degrees.)*
3. **Prompt:** "Check with the $60^\circ$ equilateral triangle face of your $d4$ or $d8$ polyhedron: it fits the $60^\circ$ gap on your Volvelle."

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `180` | 0 | 0 | 0 | 180 |
| `[ENTER]` | 0 | 0 | 180 | 180 |
| `120` | 0 | 0 | 180 | 120 |
| `[-]` | 0 | 0 | 0 | 60 |

**Student Practice Problems:**
1. Complement of $35^\circ$ ($90 - 35$): `[9] [0] [ENTER] [3] [5] [-]` = $55^\circ$.
2. Supplement of $45^\circ$ ($180 - 45$): `[1] [8] [0] [ENTER] [4] [5] [-]` = $135^\circ$.
3. Sum of four angles meeting at a point ($90 + 120 + 80 + ?$): `[3] [6] [0] [ENTER] ...` = $70^\circ$.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student reads outer scale instead of inner scale on standard protractor, reporting $60^\circ$ for an obtuse angle. | Dual-scale confusion on semi-circular protractors. | "Look at the corner: is it sharper than a book corner or wider than a book corner? Obtuse must be $> 90^\circ$." |

---

## B.5 Grade 5 Lesson Plans (Ages 10–11)

Grade 5 stations explore 3D prism volume and `[Σ+]` surface area accumulation, fraction multiplication and reciprocal division (`[f] [1/x]`), and parenthesis-free order of operations on the 4-register stack.

### B.5.1 Lesson 5.1: Volume & Total Surface Area of Prisms via `[Σ+]`
- **Standards:** CCSS.MATH.CONTENT.5.MD.C.5, 6.G.A.4; TEKS 5.6.B.
- **Learning Objective:** Students calculate the volume and total surface area of a $5 \times 4 \times 3\text{ cm}$ wooden prism using the statistical accumulator `[Σ+]` without scratch paper.
- **Manipulatives:** Wooden prism ($5 \times 4 \times 3\text{ cm}$), digital caliper.
- **Warm-Up Activity:** Count the faces on the prism. Notice that opposite faces are identical twins (3 pairs: top/bottom, front/back, left/right).

**Guided Facilitation Walkthrough:**
1. **Prompt:** "First, let us calculate volume: Length $\times$ Width $\times$ Height. Key: `[5] [ENTER] [4] [×] [3] [×]`. Volume is $60\text{ cm}^3$."
2. **Prompt:** "Now, total surface area. We must add the areas of all 6 faces. We will use the SC-6 statistical accumulator memory: `[Σ+]`. Clear memory first: `[g] [CLΣ]`."
3. **Prompt:** "Pair 1 (Top/Bottom, $5 \times 4$, two faces): `[5] [ENTER] [4] [×] [2] [×]` $\to$ 40. Press `[Σ+]`."
4. **Prompt:** "Pair 2 (Front/Back, $5 \times 3$, two faces): `[5] [ENTER] [3] [×] [2] [×]` $\to$ 30. Press `[Σ+]`."
5. **Prompt:** "Pair 3 (Left/Right, $4 \times 3$, two faces): `[4] [ENTER] [3] [×] [2] [×]` $\to$ 24. Press `[Σ+]`."
6. **Prompt:** "Screen shows $\text{Count} = 3$. Now press `[f] [Σx]`. What is the total surface area?" *(Expected response: 94 square centimeters.)*

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[g] [CLΣ]` | 0 | 0 | 0 | 0 |
| `[5] [ENTER] [4] [×] [2] [×]` | 0 | 0 | 0 | 40 |
| `[Σ+]` | 0 | 0 | 0 | Count = 1 |
| `[5] [ENTER] [3] [×] [2] [×]` | 0 | 0 | 0 | 30 |
| `[Σ+]` | 0 | 0 | 0 | Count = 2 |
| `[4] [ENTER] [3] [×] [2] [×]` | 0 | 0 | 0 | 24 |
| `[Σ+]` | 0 | 0 | 0 | Count = 3 |
| `[f] [Σx]` | 0 | 0 | 0 | 94 |

**Student Practice Problems:**
1. Box measuring $6 \times 3 \times 2\text{ cm}$: Volume = $36\text{ cm}^3$, Surface Area = $72\text{ cm}^2$.
2. Cube measuring $4 \times 4 \times 4\text{ cm}$: Volume = $64\text{ cm}^3$, Surface Area = $96\text{ cm}^2$.
3. Storage crate $10 \times 8 \times 5\text{ cm}$: Volume = $400\text{ cm}^3$, Surface Area = $340\text{ cm}^2$.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student calculates only 3 faces and forgets to multiply by 2. | Confuses the three unique face orientations with total face count. | "Every room has a ceiling AND a floor. Multiply each face pair by 2." |

---

### B.5.2 Lesson 5.2: Fraction Multiplication & Division via Reciprocal (`[f] [1/x]`)
- **Standards:** CCSS.MATH.CONTENT.5.NF.B.4, 5.NF.B.7; TEKS 5.3.I, 5.3.L.
- **Learning Objective:** Students model multiplying $\frac{2}{3} \times \frac{3}{4}$ using area grid overlays, and divide fractions by multiplying by the reciprocal using `[f] [1/x]`.
- **Manipulatives:** Transparent grid overlay sheets, dry-erase markers.
- **Warm-Up Activity:** Shade $\frac{3}{4}$ of a square vertically. Shade $\frac{2}{3}$ horizontally. Count overlapping squares: $\frac{6}{12} = \frac{1}{2}$.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "Enter $\frac{2}{3} \times \frac{3}{4}$ on SC-6: `[.] 2 [.] 3 [ENTER] [.] 3 [.] 4 [×]`. What is the result?" *(Expected response: `1/2`.)*
2. **Prompt:** "Now let us divide: $\frac{3}{4} \div \frac{2}{5}$. Dividing by a fraction is the same as multiplying by its flipped upside-down twin—the reciprocal. Enter $\frac{3}{4}$: `[.] 3 [.] 4 [ENTER]`. Enter $\frac{2}{5}$: `[.] 2 [.] 5`. Now tap reciprocal `[f] [1/x]`. What did $\frac{2}{5}$ turn into?" *(Expected response: `5/2`.)*
3. **Prompt:** "Now press `[×]`. What is the final quotient?" *(Expected response: `15/8` or $1\frac{7}{8}$.)*

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[.] 3 [.] 4` | 0 | 0 | 0 | 3/4 |
| `[ENTER]` | 0 | 0 | 3/4 | 3/4 |
| `[.] 2 [.] 5` | 0 | 0 | 3/4 | 2/5 |
| `[f] [1/x]` | 0 | 0 | 3/4 | 5/2 |
| `[×]` | 0 | 0 | 0 | 15/8 |

**Student Practice Problems:**
1. $\frac{4}{5} \times \frac{5}{8}$: `[.] 4 [.] 5 [ENTER] [.] 5 [.] 8 [×]` = $\frac{1}{2}$.
2. $\frac{1}{2} \div \frac{1}{6}$: `[.] 1 [.] 2 [ENTER] [.] 1 [.] 6 [f] [1/x] [×]` = 3.
3. $\frac{2}{3} \div \frac{4}{9}$: `[.] 2 [.] 3 [ENTER] [.] 4 [.] 9 [f] [1/x] [×]` = $\frac{3}{2} = 1\frac{1}{2}$.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student reciprocates the first fraction instead of the second fraction ($\frac{4}{3} \times \frac{2}{5}$). | Rote mnemonic "keep-change-flip" memorized without structural meaning. | "The divisor (the second passenger) is the one doing the dividing. That is the one that flips." |

---

### B.5.3 Lesson 5.3: Order of Operations without Parentheses (Stack Architecture)
- **Standards:** CCSS.MATH.CONTENT.5.OA.A.1; TEKS 5.4.F.
- **Learning Objective:** Students evaluate complex multi-step expressions like $(8 + 4) \times (9 - 3)$ and $15 + 4 \times (12 - 7)$ using the 4-register RPN stack with zero parentheses keys.
- **Manipulatives:** Expression cards, 4-story physical elevator cardboard model.
- **Warm-Up Activity:** Analyze $(8 + 4) \times (9 - 3)$. What must be solved first? The two parenthetical groups.

**Guided Facilitation Walkthrough:**
1. **Prompt:** "On ordinary calculators, students get lost in tangled parentheses like `( ( 8 + 4 ) * ( 9 - 3 ) )`. If you forget one parenthesis, you get a syntax error. On the SC-6 RPN elevator, we solve inside-out naturally. Evaluate group 1: `[8] [ENTER] [4] [+]` $\to$ 12. Keep it in the elevator. Now evaluate group 2: `[9] [ENTER] [3] [-]` $\to$ 6. Look at your screen: Register $Y$ holds 12, Register $X$ holds 6. What operation combines them?" *(Expected response: Multiplication. Press `[×]`.)*
2. **Prompt:** "Tap `[×]`. What is the answer?" *(Expected response: 72.)*
3. **Prompt:** "Zero parentheses keys used. The stack holds intermediate answers automatically."

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[8] [ENTER] [4]` | 0 | 0 | 8 | 4 |
| `[+]` | 0 | 0 | 0 | 12 |
| `[9]` | 0 | 0 | 12 | 9 |
| `[ENTER]` | 0 | 12 | 9 | 9 |
| `[3]` | 0 | 12 | 9 | 3 |
| `[-]` | 0 | 0 | 12 | 6 |
| `[×]` | 0 | 0 | 0 | 72 |

**Student Practice Problems:**
1. $(14 + 6) \div (7 - 2)$: `14 [ENTER] [6] [+] [7] [ENTER] [2] [-] [÷]` = 4.
2. $50 - (4 \times 8) + 6$: `50 [ENTER] [4] [ENTER] [8] [×] [-] [6] [+]` = 24.
3. $(3 + 5)^2 - 10$: `[3] [ENTER] [5] [+] [x²] 10 [-]` = 54.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student keys in numbers sequentially from left to right without respecting operator precedence. | Linear reading habit overriding algebraic hierarchy. | "RPN processes operators from the inside out. Build your building blocks first, then combine them." |

---

## B.6 Grade 6 Lesson Plans (Ages 11–12)

Grade 6 stations bridge into pre-algebra with two-color integer zero-pairs (`[+/-]`), prime factor towers and GCF/LCM intersections (`[PRIME]`, `[g] [FACT]`), and unit rates with `[f] [LASTX]`.

### B.6.1 Lesson 6.1: Negative Numbers, Zero Pairs & `[+/-]`
- **Standards:** CCSS.MATH.CONTENT.6.NS.C.5, 6.NS.C.6; TEKS 6.2.B.
- **Learning Objective:** Students model integer addition and subtraction using two-color counters (yellow $= +1$, red $= -1$), cancel zero pairs, and verify signed arithmetic on SC-6 using `[+/-]`.
- **Manipulatives:** 30 two-color counters (15 yellow, 15 red).
- **Warm-Up Activity:** Place 7 yellow counters ($+7$) and 4 red counters ($-4$) on desk. Pair them up. What is left? (+3).

**Guided Facilitation Walkthrough:**
1. **Prompt:** "What happens when $+1$ meets $-1$?" *(Expected response: They make a zero pair and cancel out.)*
2. **Prompt:** "Now let us model $-8 + 5$. Lay out 8 red counters and 5 yellow counters. Pair up 5 zero pairs. How many counters remain?" *(Expected response: 3 red counters, so the answer is $-3$.)*
3. **Prompt:** "Now key it into the SC-6. Type `[8]`. To make it negative, press the sign toggle key `[+/-]`. Look at the screen—a minus sign appears before the 8. Press `[ENTER]`. Now type `[5]` and press `[+]`. What is the result?" *(Expected response: $-3$.)*

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[8]` | 0 | 0 | 0 | 8 |
| `[+/-]` | 0 | 0 | 0 | -8 |
| `[ENTER]` | 0 | 0 | -8 | -8 |
| `[5]` | 0 | 0 | -8 | 5 |
| `[+]` | 0 | 0 | 0 | -3 |

**Student Practice Problems:**
1. Solve $-12 + (-7)$: `[1] [2] [+/-] [ENTER] [7] [+/-] [+]` = $-19$.
2. Solve $15 - (-6)$: `[1] [5] [ENTER] [6] [+/-] [-]` = 21.
3. Solve $(-4) \times (-8)$: `[4] [+/-] [ENTER] [8] [+/-] [×]` = 32.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student presses the operation key `[-]` instead of sign toggle key `[+/-]`. | Conflates binary subtraction operator with unary negative sign. | "`[-]` is an action combining two numbers. `[+/-]` is a label stuck onto one number." |

---

### B.6.2 Lesson 6.2: Prime Factorization, GCF & LCM (`[PRIME]`, `[g] [FACT]`)
- **Standards:** CCSS.MATH.CONTENT.6.NS.B.4; TEKS 6.7.A.
- **Learning Objective:** Students test numbers for primality using `[PRIME]`, decompose composite numbers into prime factor trees using `[g] [FACT]`, and physically verify factor products using the Prime Factor Studio factor towers and Counting Studio rectangular arrays.
- **Manipulatives:** StackCalc Prime Factor Studio (Desktop Storage Case with Prime Power Lid Sockets and 29 Proportional Blocks) and Counting & Array Studio (24-tile student kit or 144-tile classroom pack).
- **Warm-Up Activity:** 
  1. *Counting Tile Array Test:* Take 24 counting tiles. Can they form a rectangular array with row and column dimensions $\ge 2$? (Yes: $2 \times 12, 3 \times 8, 4 \times 6$). Now take 23 tiles. Try every width: 2 leaves 1 leftover; 3 leaves 2 leftover; 4 leaves 3 leftover. 23 tiles can ONLY form a straight line $1 \times 23$. A prime number cannot be arranged into a multi-row rectangle.
  2. *Prime Factor Stacking:* Place a Blue Block `[2]` ($7.00\text{ mm}$) and a Green Block `[3]` ($11.09\text{ mm}$) from the Prime Studio onto the desk next to the comparator box. Stack Block `[3]` on top of Block `[2]`. Look at the composite factor mark `6` on the side of the box: the top edge of your tower lines up flush with `6` ($7.00\text{ mm} + 11.09\text{ mm} = 18.09\text{ mm}$).

**Guided Facilitation Walkthrough:**
1. **Prompt:** "Take 23 counting tiles from your Counting Studio. Try to build a rectangle that is 2 tiles wide, or 3 tiles wide. Can anyone do it without leftovers?" *(Expected response: No, 23 only forms a single straight line of 23 tiles.)*
2. **Prompt:** "Enter 23 on the SC-6. Press `[PRIME]`. What does the display show?" *(Expected response: It flashes `PRIME` while keeping `23` on the screen.)*
3. **Prompt:** "Now let's examine 60. Can 60 tiles form rectangles? Yes, many. Enter 60 and press `[PRIME]`. What does it say?" *(Expected response: It flashes `COMPOSITE`.)*
4. **Prompt:** "To break 60 down into its fundamental prime building blocks, press `[g] [FACT]`. What is the prime factorization?" *(Expected response: `2^2 * 3 * 5`.)*
5. **Prompt:** "Now open your Prime Factor Studio. Take two Blue `[2]` blocks, one Green `[3]` block, and one Yellow `[5]` block. Stack them next to the scale on the comparator box. Where does the top of your tower land?" *(Expected response: It lines up right at the `60` mark on the comparator rail.)*
6. **Prompt:** "Now swap the order of the blocks: put the `[5]` block at the bottom, then `[3]`, then the two `[2]` blocks on top. Does the total height change?" *(Expected response: No, it still reaches the `60` mark. Multiplying factors in any order gives the same product.)*
7. **Prompt:** "Now multiply them back on the SC-6: `[2] [x²] [3] [×] [5] [×]`. You get 60."

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `60` | 0 | 0 | 0 | 60 |
| `[PRIME]` | 0 | 0 | 0 | 60 (Flashes `COMPOSITE`) |
| `[g] [FACT]` | 0 | 0 | 0 | 60 (2² × 3 × 5) |

**Student Practice Problems:**
1. Prime factorize 84: `[8] [4] [g] [FACT]` $\to$ $2^2 \times 3 \times 7$.
2. Prime factorize 180: `[1] [8] [0] [g] [FACT]` $\to$ $2^2 \times 3^2 \times 5$.
3. Find GCF of 84 and 180: Shared prime factors $= 2^2 \times 3 = 12$.

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student claims 1 is a prime number. | Misunderstands definition of prime (must have exactly two distinct factors). | "A prime number must have *exactly two* factors: 1 and itself. How many factors does 1 have? Only one." |

---

### B.6.3 Lesson 6.3: Ratios, Unit Rates & Nature's Spiral Ratio
- **Standards:** CCSS.MATH.CONTENT.6.RP.A.2, 6.RP.A.3; TEKS 6.4.B.
- **Learning Objective:** Students calculate unit rates ($240\text{ miles}$ on $8\text{ gallons} = 30\text{ mpg}$) and compute consecutive Fibonacci ratios approaching Nature's Spiral Ratio ($1.618$).
- **Manipulatives:** Double number lines, tape measures.
- **Warm-Up Activity:** If 3 packs of gum cost \$4.50, how much does 1 pack cost? ($4.50 \div 3 = 1.50$).

**Guided Facilitation Walkthrough:**
1. **Prompt:** "A car drives 372 miles on 12 gallons of fuel. What is the unit rate in miles per gallon? Enter miles: `372 [ENTER]`. Enter gallons: `12`. Divide: `[÷]`. What is the rate?" *(Expected response: 31 miles per gallon.)*
2. **Prompt:** "Now let us investigate the Fibonacci sequence ($1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89$). Divide consecutive terms: $55 \div 34$: `55 [ENTER] 34 [÷]`. What do you get?" *(Expected response: 1.6176...)*
3. **Prompt:** "Now see how `[f] [LASTX]` works here: add $34 + 55$ to get the next Fibonacci number (`34 [ENTER] 55 [+]` $\to 89$). Because `55` was just saved inside `[f] [LASTX]`, you don't even have to re-type `55`—just tap `[f] [LASTX] [÷]` to divide $89 \div 55$." *(Expected response: 1.61818...)*
4. **Prompt:** "That is Nature's Spiral Ratio ($1.618$), the Golden Ratio found in sunflower spirals, pinecones, seashells, and classical architecture."

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `372` | 0 | 0 | 0 | 372 |
| `[ENTER]` | 0 | 0 | 372 | 372 |
| `12` | 0 | 0 | 372 | 12 |
| `[÷]` | 0 | 0 | 0 | 31 |

**Student Practice Problems:**
1. Unit price: $\$18.60$ for 6 pairs of socks: `18.60 [ENTER] [6] [÷]` = $\$3.10$ per pair.
2. Typing rate: 385 words in 7 minutes: `385 [ENTER] [7] [÷]` = 55 wpm.
3. Fibonacci ratio $144 \div 89$: `55 [ENTER] 89 [+] [f] [LASTX] [÷]` (or `144 [ENTER] 89 [÷]`) = $1.61797...$

**Common Stumbling Blocks:**

| What You Might See | Why It Happens | How to Guide |
|:---|:---|:---|
| Student divides gallons by miles ($12 \div 372 = 0.032$) when asked for miles per gallon. | Ignores unit dimensional grammar. | "Say the units out loud: *miles* PER *gallon*. Miles goes in first, gallons goes in second." |

---

## B.7 Classroom Observation Guide & Common Student Stumbling Blocks

Every student interaction across the 25 lesson plans is evaluated along four observable performance criteria:

| Performance Band | Score | Hands-On Block Building | Visual Sketching | Calculator Stack Execution |
|:---|:---:|:---|:---|:---|
| **Exemplary** | **4 pts** | Fluidly constructs physical model with zero prompting. Explains spatial relationships and invariances clearly to peers. | Accurately sketches bar models, area arrays, or number lines with correct proportional scaling. | Keys problem into SC-6 fluently; explains register states ($X, Y, Z, T$); uses `[f] [LASTX]` or inverse operations to self-check. |
| **Proficient** | **3 pts** | Correctly builds model after initial launch. Self-corrects minor manipulative errors without teacher intervention. | Draws recognizable visual models matching the problem context. | Enters correct keystrokes on SC-6; successfully identifies solution on Register $X$. |
| **Developing** | **2 pts** | Requires teacher prompting to begin building or select correct manipulative blocks. | Sketches disorganized diagrams that fail to preserve mathematical proportionality. | Frequently omits `[ENTER]` separator or confuses `[+/-]` with `[-]`; needs step-by-step keystroke guidance. |
| **Intervention** | **1 pt** | Unable to model problem with concrete blocks; counts by ones; exhibits persistent off-task or frustrated behavior. | Does not produce pictorial representations; writes isolated digits disconnected from meaning. | Unable to operate calculator interface; relies on wild guessing without checking screen feedback. |

---

## B.8 Student Intervention Decision Tree & Cognitive Misconceptions

When a student struggles at a workshop station, follow this structured diagnostic decision protocol:

| What You Might See | Why It Happens | How to Guide |
| :--- | :--- | :--- |
| **Concatenated Digits** (e.g., `64` instead of `6` `[ENTER]` `4`) | Omitted `[ENTER]` separator before second operand | Re-anchor the **Elevator Mental Model** (*"Lift `6` to the balcony first."*) |
| **Nonsensical Numerical Answer** (e.g., negative area) | Reversed operand order or misapplied operation | Point to physical blocks: *"Can $4$ tiles have negative area?"* |
| **Counting One-by-One from $1$** | Subitizing benchmark not yet internalized | Revert to **Ten-Frame Subitizing Drill** (`[▦]`); focus on $5$ and $10$ benchmarks |
| **Blind Guessing in Quiz Mode** | Frustration from pace or difficulty tier | Drop down two difficulty levels; re-engage tactile blocks before restarting timer |

---

## B.9 Cognitive Science of Fluency & Classroom Quiz Practice

Short, low-stakes retrieval sessions in the SC-6 Quiz Engine (`[f] [?]`) help students consolidate hands-on block discoveries into effortless long-term fact fluency.

### B.9.1 Spaced Retrieval Practice & Memory Retention
Why does passive flashcard reading fail so often in elementary classrooms? Cognitive scientists studying the **Forgetting Curve** and active recall have shown that actively *retrieving* a math fact from memory strengthens its neural pathway far more effectively than passively re-reading a multiplication chart:

| Review Milestone | Scheduled Interval | Typical Memory Retention Floor |
| :--- | :--- | :--- |
| **Initial Acquisition** | Day 1 | $100\% \to 40\%$ without review |
| **1st Spaced Retrieval** | Day 2 | Restores to $100\%$; floor rises to $60\%$ |
| **2nd Spaced Retrieval** | Day 4 | Restores to $100\%$; floor rises to $80\%$ |
| **3rd Spaced Retrieval** | Day 8 | Restores to $100\%$; floor rises to $90\%$ |
| **Long-Term Automaticity** | Day 16+ | Consolidated in permanent long-term memory |

### B.9.2 Smart Review Queue in the SC-6 Quiz Engine (`[f] [?]`)
The SC-6 Quiz Engine (`[f] [?]`) uses a built-in smart review queue to help students master tricky facts without frustration:
- When a student answers a challenge quickly and accurately, the question is marked as mastered and rests for at least $30$ problem turns.
- When a student misses a question, the calculator quietly brings that fact back 3 turns and 7 turns later so the student can practice it again while the strategy is still fresh.

| Student Evaluation (`[ENTER]`) | Queue Transition | Scoring & Review Policy |
| :--- | :--- | :--- |
| **Accurate & Steady** | Promoted to **Mastered** | Rests for $30$ problem turns; streak increases |
| **Missed Fact** | Scheduled for **Quick Review** | Brought back in $+3$ and $+7$ turns for a second chance |

### B.9.3 Synchronized Classroom Seed Codes & Continuous Memory
During solo practice, the SC-6 shuffles questions automatically so no two practice sessions feel repetitive. For partner relays or whole-class fluency games, a teacher can announce a shared **Classroom Seed Number** (such as `42` followed by `[f] [?]`) so every student's calculator generates the exact same sequence of 10 questions in the exact same order for a fair race. Even when powered off (`[g] [OFF]`), the calculator remembers completed levels, high scores, and any tricky facts waiting for review.

---

## B.10 Companion Curriculum Suite Cross-Reference

To extend these 25 turnkey station lessons across a full academic year, pair this playbook with the three companion StackCalc classroom volumes:
- **[The 12-Unit Curriculum Guide](../curriculum/teacher-guide.md):** Multi-week unit pacing calendars, CCSS-M/TEKS standards matrices, and station rotation schedules spanning Chapters 01–09.
- **[The StackCalc Student Workbook](../curriculum/sc6-elementary-companion-workbook.md) & [Big Ideas Math Middle School Supplement](../curriculum/big-ideas-middle-school-sc6-workbook.md):** Printable student lab sheets, grid sketch pads, and middle-school extension quests for ratios, proportions, surface area nets, and pre-algebra zero pairs.
- **[Timed Proficiency Trials](../curriculum/worksheets.md):** Seed-synchronized classroom sprint scorecards, 4-player relay sheets, and fluency growth trackers for the SC-6 Quiz Engine (`[f] [?]`).

For foundational formula references and prime catalogs, see [Appendix C: Formulas, Conversions & Prime Catalogs](sc6/appendix-c-formulas-and-conversions.md).

---

# Appendix C: Formulas, Conversions & Prime Catalogs

## C.1 The RPN Word-Rule Advantage

In many school textbooks, geometry rules and unit conversions are written with lots of letter variables and parentheses:

$$\text{Triangle Area} = (\text{Base} \times \text{Height}) \div 2 \qquad \text{Trapezoid Area} = (\text{Top} + \text{Bottom}) \div 2 \times \text{Height} \qquad \text{Celsius} = (\text{Fahrenheit} - 32) \times 5 \div 9$$

When students try to type these rules into an ordinary calculator, it is easy to miss a parenthesis or lose track of a middle step.

On the **StackCalc SC-6**, grounded in Jan Łukasiewicz’s parenthesis-free notation *([Łukasiewicz, 1924](#cite-lukasiewicz1924))* and Kathy Hamrick’s history of RPN calculator architecture *([Hamrick, 1980](#cite-hamrick1980))*, the four-register Number Elevator ($X, Y, Z, T$) needs zero parentheses. Following David Macaulay’s cutaway principles *([Macaulay, 2016](#cite-macaulay2016))*, every middle step stays visible on the screen and drops into place right when you tap an operation key. This appendix gives you step-by-step RPN keystrokes for every elementary math rule.

| Register | Metaphor | Role on the Screen |
| :--- | :--- | :--- |
| **Register T** | Penthouse | Holds the top waiting number |
| **Register Z** | Second Balcony | Holds a middle step while you work on the bottom floors |
| **Register Y** | First Balcony | Holds the first number waiting for an operation |
| **Register X** | Ground Lobby | Shows the number you are typing or the answer you just found |

---

## C.2 Table 1: Elementary Math & Geometry Word-Rule Directory

This directory pairs core number rules, 2D flat shape rules, and 3D solid box and cylinder rules with their physical block models and SC-6 keystroke sequences.

### C.2.1 Foundational Number Rules & Block Models

Elementary math is built on simple, reliable patterns. The table below pairs each rule with its physical block proof, chapter link, and SC-6 stack check:

| Math Rule | Rule in Words & Numbers | Physical Block Model | Chapter Link | SC-6 Stack Check (`Example`) |
|:---|:---|:---|:---|:---|
| **Turn-Around Rule (Addition)** | $\text{First} + \text{Second} = \text{Second} + \text{First}$ ($3 + 5 = 5 + 3$) | Sliding Number Rack beads left vs. right | [Chapter 4](sc6/04-operations-skip-counting.md) | `3 [ENTER] 5 [+]` equals `5 [ENTER] 3 [+]` |
| **Turn-Around Rule (Multiplication)** | $\text{Rows} \times \text{Columns} = \text{Columns} \times \text{Rows}$ ($4 \times 6 = 6 \times 4$) | Turning a 24-tile rectangle $90^\circ$ on the desk | [Chapter 4](sc6/04-operations-skip-counting.md) | `4 [ENTER] 6 [×]` equals `6 [ENTER] 4 [×]` |
| **Grouping Rule (Addition)** | $(\text{First} + \text{Second}) + \text{Third} = \text{First} + (\text{Second} + \text{Third})$ | Joining 3 color trains of snap cubes | [Chapter 4](sc6/04-operations-skip-counting.md) | `2 [ENTER] 3 [+] 4 [+]` |
| **Grouping Rule (Multiplication)** | $(\text{Length} \times \text{Width}) \times \text{Height}$ in any order | Stacking 3D layers of unit cubes | [Chapter 4](sc6/04-operations-skip-counting.md) | `2 [ENTER] 3 [×] 4 [×]` |
| **Break-Apart Rule (Distributive)** | $4 \times (10 + 3) = (4 \times 10) + (4 \times 3)$ | Splitting a 4-color tile rectangle along a color seam | [Chapter 4](sc6/04-operations-skip-counting.md) | `10 [ENTER] 3 [+] 4 [×]` |
| **Zero and One Rules** | Adding $0$ or multiplying by $1$ leaves a number unchanged | Adding zero tiles; taking 1 group of tiles | [Chapter 4](sc6/04-operations-skip-counting.md) | `7 [ENTER] 0 [+]` $\to 7$; `7 [ENTER] 1 [×]` $\to 7$ |
| **Division with Remainder Check** | $\text{Total} = (\text{Divisor} \times \text{Quotient}) + \text{Remainder}$ | Sharing counters equally into cups with leftovers | [Chapter 4](sc6/04-operations-skip-counting.md) | `29 [ENTER] 4 [g] [÷R]` $\to$ Remainder `1` in $Y$, Quotient `7` in $X$ |
| **GCF and LCM Partner Rule** | $\text{GCF} \times \text{LCM} = \text{First Number} \times \text{Second Number}$ | Comparing Prime Factor Studio towers side by side | [Chapter 7](sc6/07-data-probability-primes.md) | `12 [ENTER] 18 [GCF] 12 [ENTER] 18 [f] [LCM] [×]` $\to 216$ |
| **Fraction-to-Decimal Bridge** | $\text{Top Number} \div \text{Bottom Number} = \text{Decimal}$ | Comparing Fraction Towers to the $1\text{-Whole}$ tower | [Chapter 5](sc6/05-fractions-decimals-ratios.md) | `3 [ENTER] 4 [÷]` $\to 0.75$ |

---

### C.2.2 Two-Dimensional Perimeter & Area Word Rules

The table below summarizes 2D flat shape rules in plain words alongside their chapter links and SC-6 RPN keystroke sequences:

| Flat Shape | Word Rule | Chapter Link | SC-6 RPN Keystroke Sequence | Stack Floors Used |
|:---|:---|:---|:---|:---:|
| **Square (Perimeter)** | $\text{Perimeter} = 4 \times \text{Side}$ | [Chapter 6](sc6/06-geometry-surface-area.md) | `[Side] [ENTER] [4] [×]` | $Y, X$ |
| **Square (Area)** | $\text{Area} = \text{Side} \times \text{Side}$ | [Chapter 6](sc6/06-geometry-surface-area.md) | `[Side] [x²]` | $X$ |
| **Rectangle (Perimeter)** | $\text{Perimeter} = 2 \times (\text{Length} + \text{Width})$ | [Chapter 6](sc6/06-geometry-surface-area.md) | `[Length] [ENTER] [Width] [+] [2] [×]` | $Y, X$ |
| **Rectangle (Area)** | $\text{Area} = \text{Length} \times \text{Width}$ | [Chapter 6](sc6/06-geometry-surface-area.md) | `[Length] [ENTER] [Width] [f] [RECT]` | $Y, X$ |
| **Triangle (Perimeter)** | $\text{Perimeter} = \text{Side 1} + \text{Side 2} + \text{Side 3}$ | [Chapter 6](sc6/06-geometry-surface-area.md) | `[Side 1] [ENTER] [Side 2] [+] [Side 3] [+]` | $Z, Y, X$ |
| **Triangle (Area)** | $\text{Area} = (\text{Base} \times \text{Height}) \div 2$ | [Chapter 6](sc6/06-geometry-surface-area.md) | `[Base] [ENTER] [Height] [×] [2] [÷]` | $Y, X$ |
| **Parallelogram (Area)** | $\text{Area} = \text{Base} \times \text{Height}$ | [Chapter 6](sc6/06-geometry-surface-area.md) | `[Base] [ENTER] [Height] [×]` | $Y, X$ |
| **Trapezoid (Area)** | $\text{Area} = (\text{Top} + \text{Bottom}) \div 2 \times \text{Height}$ | [Chapter 6](sc6/06-geometry-surface-area.md) | `[Top] [ENTER] [Bottom] [+] [2] [÷] [Height] [×]` | $Z, Y, X$ |
| **Circle (Circumference)** | $\text{Distance Around} = \pi \times \text{Width (Diameter)}$ | [Chapter 6](sc6/06-geometry-surface-area.md) | `[Diameter] [π] [×]` | $Y, X$ |
| **Circle (Area)** | $\text{Area} = \pi \times \text{Radius} \times \text{Radius}$ | [Chapter 6](sc6/06-geometry-surface-area.md) | `[Radius] [x²] [π] [×]` | $Y, X$ |

---

### C.2.3 Flat Shapes in Action: 2D Stack Traces

To see how Registers $T, Z, Y,$ and $X$ update step by step when measuring flat shapes, let's trace five classic two-dimensional shapes on the stack. Suppose you start with a **triangle** whose base is $14\text{ cm}$ and height is $9\text{ cm}$. Because any triangle is half of a bounding rectangle, the triangle word rule tells us that $\text{Area} = (\text{Base} \times \text{Height}) \div 2 = (14 \times 9) \div 2 = 63\text{ cm}^2$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `14` | 0 | 0 | 0 | 14 |
| `[ENTER]` | 0 | 0 | 14 | 14 |
| `[9]` | 0 | 0 | 14 | 9 |
| `[×]` | 0 | 0 | 0 | 126 |
| `[2]` | 0 | 0 | 126 | 2 |
| `[÷]` | 0 | 0 | 0 | 63 |

Notice how you first multiply $14 \times 9 = 126$ for the full bounding rectangle, and then type `2` and tap `[÷]` to slice that rectangle in half: $126 \div 2 = 63$.

What if the top of the shape isn't a sharp point, but a flat roof—making a **trapezoid** with a top width of $8\text{ in}$, a bottom width of $14\text{ in}$, and a height of $6\text{ in}$? Averaging the top and bottom widths first gives the middle width ($(8 + 14) \div 2 = 11\text{ in}$), and multiplying by the height gives $\text{Area} = (\text{Top} + \text{Bottom}) \div 2 \times \text{Height} = 11 \times 6 = 66\text{ sq in}$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[8]` | 0 | 0 | 0 | 8 |
| `[ENTER]` | 0 | 0 | 8 | 8 |
| `14` | 0 | 0 | 8 | 14 |
| `[+]` | 0 | 0 | 0 | 22 |
| `[2]` | 0 | 0 | 22 | 2 |
| `[÷]` | 0 | 0 | 0 | 11 |
| `[6]` | 0 | 0 | 11 | 6 |
| `[×]` | 0 | 0 | 0 | 66 |

When straight edges curve into a circle—such as a **circular splash pad** with a radius of $3.5\text{ m}$—squaring the radius first (`3.5 [x²]` $\to 12.25$) and scaling by `[π]` yields $\text{Area} = \pi \times \text{Radius} \times \text{Radius} = \pi \times 3.5^2 \approx 38.48451\text{ m}^2$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `3.5` | 0 | 0 | 0 | 3.5 |
| `[x²]` | 0 | 0 | 0 | 12.25 |
| `[π]` | 0 | 0 | 12.25 | 3.1415926 |
| `[×]` | 0 | 0 | 0 | 38.484510 |

For the distance around the outside of a shape, we walk its perimeter. Around a **rectangular garden** of length $14\text{ m}$ and width $9\text{ m}$, adding the two adjacent sides into an L-shape ($14 + 9 = 23\text{ m}$) and doubling gives $\text{Perimeter} = 2 \times (\text{Length} + \text{Width}) = 2 \times 23 = 46\text{ m}$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `14` | 0 | 0 | 0 | 14 |
| `[ENTER]` | 0 | 0 | 14 | 14 |
| `[9]` | 0 | 0 | 14 | 9 |
| `[+]` | 0 | 0 | 0 | 23 |
| `[2]` | 0 | 0 | 23 | 2 |
| `[×]` | 0 | 0 | 0 | 46 |

And to find how far a $24\text{-inch}$ **bicycle wheel** rolls in one full turn ($\text{Circumference} = \pi \times 24$), typing `24 [π] [×]` on the stack immediately displays **$75.39822\text{ inches}$** per revolution.

---

### C.2.4 Three-Dimensional Solid Volume & Surface Area Word Rules

| 3D Solid Shape | Volume Word Rule | Total Surface Area Word Rule | Chapter Link | SC-6 Volume Keystrokes |
|:---|:---|:---|:---|:---|
| **Cube** | $\text{Volume} = \text{Side} \times \text{Side} \times \text{Side}$ | $\text{Surface Area} = 6 \times (\text{Side} \times \text{Side})$ | [Chapter 6](sc6/06-geometry-surface-area.md) | `[Side] [ENTER] [3] [g] [yˣ]` |
| **Rectangular Box (Prism)** | $\text{Volume} = \text{Length} \times \text{Width} \times \text{Height}$ | Add all $6$ rectangular faces ($2\text{ Top/Bottom} + 2\text{ Front/Back} + 2\text{ Sides}$) | [Chapter 6](sc6/06-geometry-surface-area.md) | `[Length] [ENTER] [Width] [×] [Height] [×]` |
| **Triangular Tent (Prism)** | $\text{Volume} = (\text{Base} \times \text{Height} \div 2) \times \text{Length}$ | Add the $2$ triangle ends plus the $3$ rectangular side panels | [Chapter 6](sc6/06-geometry-surface-area.md) | `[Base] [ENTER] [Height] [×] 2 [÷] [Length] [×]` |
| **Cylinder (Can)** | $\text{Volume} = (\pi \times \text{Radius}^2) \times \text{Height}$ | $\text{Curved Side} \ (2 \times \pi \times \text{Radius} \times \text{Height}) + 2\text{ Circle Ends} \ (2 \times \pi \times \text{Radius}^2)$ | [Chapter 6](sc6/06-geometry-surface-area.md) | `[Radius] [x²] [π] [×] [Height] [×]` |

---

### C.2.5 Solid Shapes in Action: 3D Stack Traces

When a flat base is lifted upward into three dimensions, the stack lets you find both volume and surface area without parentheses or scratch paper. Consider a **cylindrical farm storage silo** with a radius of $4\text{ m}$ and a height of $10\text{ m}$. Its volume stacks the circular base area across the height: $(\pi \times 4^2) \times 10 = 160\pi \approx 502.6548\text{ m}^3$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[4]` | 0 | 0 | 0 | 4 |
| `[x²]` | 0 | 0 | 0 | 16 |
| `[π]` | 0 | 0 | 16 | 3.1415926 |
| `[×]` | 0 | 0 | 0 | 50.265482 |
| `10` | 0 | 0 | 50.265482 | 10 |
| `[×]` | 0 | 0 | 0 | 502.654824 |

To paint that same silo's outer shell and both circular lids, we add the unrolled side wrapper to the two circular ends, $(2 \times \pi \times 4 \times 10) + (2 \times \pi \times 4^2) \approx 351.8584\text{ m}^2$, letting Register $Y$ hold the curved side area ($251.33\text{ m}^2$) while we build the two circular lids ($100.53\text{ m}^2$) in $X$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[2]` | 0 | 0 | 0 | 2 |
| `[π] [×]` | 0 | 0 | 0 | 6.2831853 |
| `[4] [×]` | 0 | 0 | 0 | 25.132741 |
| `10 [×]` | 0 | 0 | 0 | 251.327412 |
| `[2]` | 0 | 0 | 251.327412 | 2 |
| `[π] [×]` | 0 | 0 | 251.327412 | 6.2831853 |
| `[4] [x²] [×]` | 0 | 0 | 251.327412 | 100.530964 |
| `[+]` | 0 | 0 | 0 | 351.858376 |

The same layer-stacking idea works for boxes and cubes. For a **square-base storage box** with a $6\text{ cm}$ base side and an $8\text{ cm}$ height, squaring the $6\text{ cm}$ side builds a $36\text{ cm}^2$ bottom layer, and multiplying by $8$ stacks up the layers ($36 \times 8 = 288\text{ cm}^3$):

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[6] [x²]` | 0 | 0 | 0 | 36 |
| `[8]` | 0 | 0 | 36 | 8 |
| `[×]` | 0 | 0 | 0 | 288 |

And when all three dimensions match—such as a **$9\text{ cm}$ cube**—it holds $\text{Side}^3 = 9^3 = 729\text{ cm}^3$ of space inside (`[9] [ENTER] [3] [g] [yˣ]` $\to \mathbf{729}\text{ cm}^3$) and is wrapped by six identical $9 \times 9$ square faces (`[9] [x²] [6] [×]` $\to \mathbf{486}\text{ cm}^2$).

---

## C.3 Total Surface Area via Statistical Accumulator (`[Σ+]`)

When unfolding a 3D box or tent into its flat net of faces, adding up all the faces on scratch paper is easy to mix up. On the SC-6, you can add each pair of matching faces directly into the statistical accumulator using `[Σ+]`:

| Step | Action | SC-6 Keystroke | Screen Count |
| :--- | :--- | :--- | :--- |
| **Step 1: Clear Memory** | Reset statistics | `[g] [CLΣ]` | $\text{Count} = 0$ |
| **Step 2: Top & Bottom Faces** | $\text{Length} \times \text{Width} \times 2$ | `[Length] [ENTER] [Width] [×] 2 [×] [Σ+]` | Stored ($\text{Count} = 1$) |
| **Step 3: Front & Back Faces** | $\text{Length} \times \text{Height} \times 2$ | `[Length] [ENTER] [Height] [×] 2 [×] [Σ+]` | Stored ($\text{Count} = 2$) |
| **Step 4: Left & Right Faces** | $\text{Width} \times \text{Height} \times 2$ | `[Width] [ENTER] [Height] [×] 2 [×] [Σ+]` | Stored ($\text{Count} = 3$) |
| **Step 5: Recall Total Area** | Sum all 6 faces | `[f] [Σx]` | Total Surface Area on $X$ |

### C.3.1 Wrapping a Rectangular Box ($\text{Length} = 12\text{ cm}, \text{Width} = 7\text{ cm}, \text{Height} = 5\text{ cm}$)
Unfolding a $12 \times 7 \times 5\text{ cm}$ box reveals three matching pairs of faces: the top and bottom ($2 \times 12 \times 7 = 168\text{ cm}^2$), the front and back ($2 \times 12 \times 5 = 120\text{ cm}^2$), and the left and right ends ($2 \times 7 \times 5 = 70\text{ cm}^2$). Tap `[g] [CLΣ]` to clear the accumulator, then feed in the three pairs one after another:
1. `12 [ENTER] [7] [×] [2] [×] [Σ+]` (Screen confirms count $1$).
2. `12 [ENTER] [5] [×] [2] [×] [Σ+]` (Screen confirms count $2$).
3. `[7] [ENTER] [5] [×] [2] [×] [Σ+]` (Screen confirms count $3$).
4. Tap `[f] [Σx]` to recall the combined surface area: **$358.00\text{ cm}^2$**.

### C.3.2 Pitching a Triangular Camping Tent
A triangular camping tent has two triangle end doors with a base of $6\text{ ft}$, a height of $4\text{ ft}$, and slanted roof edges of $5\text{ ft}$, stretched along a $10\text{ ft}$ floor. The two triangle doors together equal one $6 \times 4$ rectangle ($24\text{ sq ft}$), the floor panel covers $6 \times 10 = 60\text{ sq ft}$, and the two slanted roof panels cover $2 \times (5 \times 10) = 100\text{ sq ft}$. After tapping `[g] [CLΣ]`, store the triangle doors with `[6] [ENTER] [4] [×] [Σ+]`, the floor panel with `[6] [ENTER] 10 [×] [Σ+]`, and the roof panels with `[5] [ENTER] 10 [×] [2] [×] [Σ+]`. Pressing `[f] [Σx]` sums all five fabric panels to **$184.00\text{ sq ft}$**.

---

## C.4 Table 2: Complete Unit Conversions Directory

Unit conversions multiply or divide by a fixed conversion number.

### C.4.1 Length Conversions

| From Unit | To Unit | Conversion Number | SC-6 Forward Keystrokes | Reverse (Back Again) |
|:---|:---|:---:|:---|:---:|
| **Inches (in)** | **Centimeters (cm)** | $2.54$ | `[in] [ENTER] 2.54 [×]` | $\div 2.54$ |
| **Feet (ft)** | **Inches (in)** | $12.0$ | `[ft] [ENTER] 12 [×]` | $\div 12$ |
| **Feet (ft)** | **Meters (m)** | $0.3048$ | `[ft] [ENTER] [.] 3048 [×]`| $\div 0.3048$ |
| **Yards (yd)** | **Feet (ft)** | $3.0$ | `[yd] [ENTER] [3] [×]` | $\div 3$ |
| **Yards (yd)** | **Meters (m)** | $0.9144$ | `[yd] [ENTER] [.] 9144 [×]`| $\div 0.9144$ |
| **Miles (mi)** | **Feet (ft)** | $5280.0$ | `[mi] [ENTER] 5280 [×]` | $\div 5280$ |
| **Miles (mi)** | **Kilometers (km)** | $1.609344$| `[mi] [ENTER] 1.609344 [×]`| $\div 1.609344$ |
| **Nautical Miles (NM)**| **Kilometers (km)**| $1.852$ | `[NM] [ENTER] 1.852 [×]` | $\div 1.852$ |
| **Nautical Miles (NM)**| **Statute Miles (mi)**| $\approx 1.150779$| `[NM] [ENTER] 1.1508 [×]`| $\div 1.1508$ |
| **Meters (m)** | **Centimeters (cm)** | $100.0$ | `[m] [ENTER] 100 [×]` | $\div 100$ |
| **Centimeters (cm)**| **Millimeters (mm)**| $10.0$ | `[cm] [ENTER] 10 [×]` | $\div 10$ |
| **Kilometers (km)**| **Meters (m)** | $1000.0$ | `[km] [ENTER] 1000 [×]` | $\div 1000$ |

For example, to convert a $100\text{-yard}$ football field into meters, key in `100 [ENTER] 0.9144 [×]` to obtain **$91.44\text{ meters}$**—and dividing right back with `[.] 9144 [÷]` restores the original **$100.00\text{ yards}$**.

---

### C.4.2 Area Conversions

| From Unit | To Unit | Conversion Number | SC-6 Forward Keystrokes | Reverse |
|:---|:---|:---:|:---|:---:|
| **Square Feet (sq ft)**| **Square Inches (sq in)**| $144.0$ | `[sq ft] [ENTER] 144 [×]` | $\div 144$ |
| **Square Yards (sq yd)**| **Square Feet (sq ft)**| $9.0$ | `[sq yd] [ENTER] [9] [×]` | $\div 9$ |
| **Acres (ac)** | **Square Feet (sq ft)**| $43,560.0$ | `[ac] [ENTER] 43560 [×]`| $\div 43560$ |
| **Acres (ac)** | **Hectares (ha)** | $\approx 0.4046856$| `[ac] [ENTER] [.] 4047 [×]`| $\div 0.4047$ |
| **Hectares (ha)** | **Square Meters ($\text{m}^2$)**| $10,000.0$ | `[ha] [ENTER] 10000 [×]`| $\div 10000$ |
| **Square Miles ($\text{mi}^2$)**| **Acres (ac)** | $640.0$ | `[sq mi] [ENTER] 640 [×]` | $\div 640$ |
| **Square Meters ($\text{m}^2$)**| **Square Feet (sq ft)**| $\approx 10.76391$ | `[m²] [ENTER] 10.764 [×]`| $\div 10.764$ |

For instance, to find how many square feet lie inside a $2.5\text{-acre}$ neighborhood park, enter `2.5 [ENTER] 43560 [×]`, which reveals **$108,900\text{ sq ft}$**.

---

### C.4.3 Weight & Mass Conversions

| From Unit | To Unit | Conversion Number | SC-6 Forward Keystrokes | Reverse |
|:---|:---|:---:|:---|:---:|
| **Ounces (oz)** | **Grams (g)** | $28.349523$ | `[oz] [ENTER] 28.35 [×]` | $\div 28.3495$ |
| **Pounds (lb)** | **Ounces (oz)** | $16.0$ | `[lb] [ENTER] 16 [×]` | $\div 16$ |
| **Pounds (lb)** | **Kilograms (kg)** | $0.45359237$| `[lb] [ENTER] [.] 4536 [×]` | $\div 0.4536$ |
| **Kilograms (kg)** | **Pounds (lb)** | $\approx 2.2046226$| `[kg] [ENTER] 2.2046 [×]`| $\div 2.2046$ |
| **Tons (US Short)**| **Pounds (lb)** | $2000.0$ | `[ton] [ENTER] 2000 [×]` | $\div 2000$ |
| **Metric Tons (t)** | **Kilograms (kg)** | $1000.0$ | `[t] [ENTER] 1000 [×]` | $\div 1000$ |
| **Kilograms (kg)** | **Grams (g)** | $1000.0$ | `[kg] [ENTER] 1000 [×]` | $\div 1000$ |
| **Grams (g)** | **Milligrams (mg)** | $1000.0$ | `[ENTER] 1000 [×]` | $\div 1000$ |

To convert a $65\text{ lb}$ bicycle shipping crate into kilograms, press `65 [ENTER] 0.453592 [×]` to read **$29.483\text{ kg}$** on the display.

---

### C.4.4 Capacity & Liquid Volume Conversions

| From Unit | To Unit | Conversion Number | SC-6 Forward Keystrokes | Reverse |
|:---|:---|:---:|:---|:---:|
| **Fluid Ounces (fl oz)** | **Milliliters (mL)** | $29.57352956$| `[fl oz] [ENTER] 29.57 [×]` | $\div 29.5735$ |
| **Cups (c)** | **Fluid Ounces (fl oz)**| $8.0$ | `[c] [ENTER] [8] [×]` | $\div 8$ |
| **Pints (pt)** | **Cups (c)** | $2.0$ | `[pt] [ENTER] [2] [×]` | $\div 2$ |
| **Quarts (qt)** | **Pints (pt)** | $2.0$ | `[qt] [ENTER] [2] [×]` | $\div 2$ |
| **Gallons (gal US)**| **Quarts (qt)** | $4.0$ | `[gal] [ENTER] [4] [×]` | $\div 4$ |
| **Gallons (gal US)**| **Liters (L)** | $3.785411784$ | `[gal] [ENTER] 3.7854 [×]`| $\div 3.7854$ |
| **Gallons (Imperial)**| **Liters (L)** | $4.54609$ | `[gal imp] [ENTER] 4.546 [×]`| $\div 4.5461$ |
| **Liters (L)** | **Milliliters (mL)** | $1000.0$ | `[L] [ENTER] 1000 [×]` | $\div 1000$ |
| **Cubic Meters ($\text{m}^3$)**| **Liters (L)** | $1000.0$ | `[m³] [ENTER] 1000 [×]` | $\div 1000$ |

To convert a $15\text{-gallon}$ camp water tank into liters, run `15 [ENTER] 3.7854 [×]` to find **$56.781\text{ liters}$**.

---

### C.4.5 Speed Conversions

| From Unit | To Unit | Conversion Number | SC-6 Keystrokes |
|:---|:---|:---:|:---|
| **Miles per Hour (mph)**| **Kilometers per Hour (km/h)**| $1.609344$ | `[mph] [ENTER] 1.609 [×]` |
| **Miles per Hour (mph)**| **Feet per Second (ft/s)**| $\approx 1.466667$ | `[mph] [ENTER] 5280 [×] 3600 [÷]` |
| **Kilometers per Hour (km/h)**| **Meters per Second (m/s)**| $\approx 0.277778$| `[km/h] [ENTER] 1000 [×] 3600 [÷]` |
| **Knots (kt)** | **Miles per Hour (mph)**| $\approx 1.150779$ | `[kt] [ENTER] 1.151 [×]` |
| **Knots (kt)** | **Kilometers per Hour (km/h)**| $1.852$ | `[kt] [ENTER] 1.852 [×]` |

When a quadcopter drone flies at $45\text{ mph}$, you can find how many feet it covers each second by keying in `45 [ENTER] 5280 [×] 3600 [÷]`, which lands on **$66.0\text{ ft/s}$**.

---

### C.4.6 Tire & Air Pressure Conversions

| From Unit | To Unit | Conversion Number | SC-6 Keystrokes |
|:---|:---|:---:|:---|
| **Atmospheres (atm)** | **Pounds per Sq Inch (psi)**| $14.6959488$ | `[atm] [ENTER] 14.696 [×]` |
| **Atmospheres (atm)** | **Kilopascals (kPa)** | $101.325$ | `[atm] [ENTER] 101.325 [×]` |
| **Bar (bar)** | **Kilopascals (kPa)** | $100.0$ | `[bar] [ENTER] 100 [×]` |
| **Pounds per Sq Inch (psi)**| **Kilopascals (kPa)**| $6.894757$ | `[psi] [ENTER] 6.895 [×]` |

If a road bicycle tire is inflated to $85\text{ psi}$, keying in `85 [ENTER] 6.89476 [×]` converts that pressure to **$586.05\text{ kPa}$**.

---

### C.4.7 Time Conversions

| From Unit | To Unit | Conversion Number | SC-6 Keystroke Sequence |
|:---|:---|:---:|:---|
| **Minutes (min)** | **Seconds (s)** | $60.0$ | `[min] [ENTER] 60 [×]` |
| **Hours (hr)** | **Minutes (min)** | $60.0$ | `[hr] [ENTER] 60 [×]` |
| **Hours (hr)** | **Seconds (s)** | $3600.0$ | `[hr] [ENTER] 3600 [×]` |
| **Days (d)** | **Hours (hr)** | $24.0$ | `[days] [ENTER] 24 [×]` |
| **Weeks (wk)** | **Days (d)** | $7.0$ | `[wk] [ENTER] [7] [×]` |
| **Years (yr standard)**| **Days (d)** | $365.0$ | `[yr] [ENTER] 365 [×]` |
| **Years (yr leap)**| **Days (d)** | $366.0$ | `[yr] [ENTER] 366 [×]` |

To count how many seconds tick by in a full 24-hour day, enter `24 [ENTER] 3600 [×]` to reach **$86,400\text{ seconds}$**.

---

### C.4.8 Temperature Conversions (Fahrenheit and Celsius)

Because water freezes at $32^\circ\text{F}$ ($0^\circ\text{C}$) and boils at $212^\circ\text{F}$ ($100^\circ\text{C}$), converting between Fahrenheit and Celsius uses two simple word rules:

$$\text{Celsius} = (\text{Fahrenheit} - 32) \times 5 \div 9 \qquad \text{Fahrenheit} = (\text{Celsius} \times 9 \div 5) + 32$$

| Conversion | Word Rule | SC-6 Step-by-Step Keystrokes (or One-Tap Key) |
| :--- | :--- | :--- |
| **Fahrenheit to Celsius** | $(\text{Fahrenheit} - 32) \times 5 \div 9$ | `[Temp F] [ENTER] 32 [-] [5] [×] [9] [÷]` (or `[Temp F] [f] [▸°C]`) |
| **Celsius to Fahrenheit** | $(\text{Celsius} \times 9 \div 5) + 32$ | `[Temp C] [ENTER] [9] [×] [5] [÷] 32 [+]` (or `[Temp C] [g] [▸°F]`) |

Here is how normal human body temperature ($98.6^\circ\text{F}$) converts to Celsius step by step on the stack:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `98.6` | 0 | 0 | 0 | 98.6 |
| `[ENTER]` | 0 | 0 | 98.6 | 98.6 |
| `32` | 0 | 0 | 98.6 | 32 |
| `[-]` | 0 | 0 | 0 | 66.6 |
| `[5]` | 0 | 0 | 66.6 | 5 |
| `[×]` | 0 | 0 | 0 | 333.0 |
| `[9]` | 0 | 0 | 333.0 | 9 |
| `[÷]` | 0 | 0 | 0 | 37.0 |

Normal human body temperature is **$37.0^\circ\text{C}$** (or in one tap on the SC-6 keypad, `98.6 [f] [▸°C]` $\to$ `37.00`).

---

### C.4.9 Chaining Multi-Step Unit Conversions on the Stack

When a real-world measurement needs two conversion steps in a row, the stack lets you chain them without parentheses or scratch paper. For a **marathon footrace** ($26.2\text{ miles} \to \text{kilometers} \to \text{meters}$), since $1\text{ mile} = 1.609344\text{ kilometers}$ and $1\text{ kilometer} = 1,000\text{ meters}$, multiplying $26.2 \times 1.609344$ first gives $42.164813\text{ km}$ and multiplying by $1,000$ converts to meters:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `[2] [6] [.] [2]` | 0 | 0 | 0 | 26.2 |
| `[ENTER]` | 0 | 0 | 26.2 | 26.2 |
| `1.609344` | 0 | 0 | 26.2 | 1.609344 |
| `[×]` | 0 | 0 | 0 | 42.164813 |
| `1000` | 0 | 0 | 42.164813 | 1000 |
| `[×]` | 0 | 0 | 0 | 42164.81280 |

Register $X$ shows the full Olympic marathon distance in meters: **$42,164.81\text{ meters}$**.

Next, consider an **airliner cruising at $36,000\text{ ft}$** ($36,000\text{ ft} \to \text{meters} \to \text{kilometers}$). Using $1\text{ foot} = 0.3048\text{ meters}$, we multiply $36,000 \times 0.3048$ to get meters and immediately divide by $1,000$ for kilometers:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `36000` | 0 | 0 | 0 | 36000 |
| `[ENTER]` | 0 | 0 | 36000 | 36000 |
| `.3048` | 0 | 0 | 36000 | 0.3048 |
| `[×]` | 0 | 0 | 0 | 10972.8 |
| `1000` | 0 | 0 | 10972.8 | 1000 |
| `[÷]` | 0 | 0 | 0 | 10.9728 |

Cruising height is **$10,972.8\text{ meters}$**, or **$10.97\text{ km}$** above sea level.

What about comparing **family car fuel mileage** ($35.0\text{ Miles per Gallon} \to \text{Liters per 100 km}$)? Dividing the conversion constant $235.215$ by the Miles per Gallon ($\text{Liters per 100 km} = 235.215 \div \text{MPG}$) flips American mileage into metric fuel consumption:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `235.215` | 0 | 0 | 0 | 235.215 |
| `[ENTER]` | 0 | 0 | 235.215 | 235.215 |
| `35` | 0 | 0 | 235.215 | 35 |
| `[÷]` | 0 | 0 | 0 | 6.720429 |

A car rated at $35\text{ MPG}$ burns **$6.72\text{ liters of fuel per 100 kilometers}$**.

Finally, we can test a **snowy winter morning temperature** ($14^\circ\text{F} \to -10^\circ\text{C} \to 14^\circ\text{F}$) by converting $14^\circ\text{F}$ into Celsius and then running the inverse steps right on the stack to return to $14^\circ\text{F}$:

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `14` | 0 | 0 | 0 | 14 |
| `[ENTER]` | 0 | 0 | 14 | 14 |
| `32` | 0 | 0 | 14 | 32 |
| `[-]` | 0 | 0 | 0 | -18 |
| `[5]` | 0 | 0 | -18 | 5 |
| `[×]` | 0 | 0 | 0 | -90 |
| `[9]` | 0 | 0 | -90 | 9 |
| `[÷]` | 0 | 0 | 0 | -10 |
| `[9] [×] [5] [÷]` | 0 | 0 | 0 | -18 |
| `32 [+]` | 0 | 0 | 0 | 14 |

Here $14^\circ\text{F}$ equals **$-10^\circ\text{C}$** (ten degrees below freezing), and reversing the steps returns **$14^\circ\text{F}$**.

---

## C.5 Table 3: Prime Number Catalog & Factorization Directory

A prime number is a whole number greater than 1 that has **only two factors: 1 and itself**. Every composite number greater than 1 can be built by multiplying a unique team of prime numbers together.

### C.5.1 Complete Catalog of All 46 Prime Numbers Under 200

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

### C.5.2 Quick Divisibility Rules with SC-6 Checks

Before testing a big number with `[PRIME]`, you can spot small factors right away using these mental math rules:

| Divide By | Quick Mental Rule | How to Check on Your SC-6 (`[g] [÷R]`) | Example |
|:---:|:---|:---|:---|
| **2** | Last digit is even ($0, 2, 4, 6, 8$). | `[Number] [ENTER] [2] [g] [÷R]` (Remainder in $Y$ is `0`) | $84 \div 2 = 42$ with Remainder $0$ |
| **3** | Add the digits; the sum divides evenly by 3. | Add the digits on the stack, then press `[3] [g] [÷R]` | $153 \to 1+5+3=9$, and $9 \div 3 = 3$ |
| **4** | Last two digits divide evenly by 4. | `[Last 2 Digits] [ENTER] [4] [g] [÷R]` | $3,728 \to 28 \div 4 = 7$ (Remainder $0$) |
| **5** | Last digit is 0 or 5. | Look at the ones digit on the screen. | $95$ ends in $5$ ($95 \div 5 = 19$) |
| **6** | Passes both the 2-test (even) and the 3-test. | Check that it is even and its digits add to a multiple of 3. | $78$ is even, and $7+8=15$ ($78 \div 6 = 13$) |
| **8** | Last three digits divide evenly by 8. | `[Last 3 Digits] [ENTER] [8] [g] [÷R]` | $5,128 \to 128 \div 8 = 16$ (Remainder $0$) |
| **9** | Add the digits; the sum divides evenly by 9. | Add the digits on the stack, then press `[9] [g] [÷R]` | $423 \to 4+2+3=9$, and $9 \div 9 = 1$ |
| **10** | Last digit is 0. | Look at the ones digit on the screen. | $340$ ends in $0$ ($340 \div 10 = 34$) |

---

### C.5.3 Ten Classic Prime Factorizations

Every composite whole number greater than 1 breaks down into a unique product of prime numbers—just like a tower built from your **Prime Factor Studio** blocks! The table below shows 10 classic composite numbers, their prime factor blocks, and how to multiply the prime blocks back together on your SC-6:

| Composite Number | Prime Factor Blocks | SC-6 `[g] [FACT]` Screen Output | RPN Keystrokes to Multiply Them Back |
|:---:|:---:|:---|:---|
| **72** | $2^3 \times 3^2$ | `2^3 * 3^2` | `[2] [ENTER] [3] [g] [yˣ] [3] [x²] [×]` $\to 72$ |
| **84** | $2^2 \times 3 \times 7$ | `2^2 * 3 * 7` | `[2] [x²] [3] [×] [7] [×]` $\to 84$ |
| **180** | $2^2 \times 3^2 \times 5$ | `2^2 * 3^2 * 5` | `[2] [x²] [3] [x²] [×] [5] [×]` $\to 180$ |
| **252** | $2^2 \times 3^2 \times 7$ | `2^2 * 3^2 * 7` | `[2] [x²] [3] [x²] [×] [7] [×]` $\to 252$ |
| **360** | $2^3 \times 3^2 \times 5$ | `2^3 * 3^2 * 5` | `[2] [ENTER] [3] [g] [yˣ] [3] [x²] [×] [5] [×]` $\to 360$ |
| **504** | $2^3 \times 3^2 \times 7$ | `2^3 * 3^2 * 7` | `[2] [ENTER] [3] [g] [yˣ] [3] [x²] [×] [7] [×]` $\to 504$ |
| **720** | $2^4 \times 3^2 \times 5$ | `2^4 * 3^2 * 5` | `[2] [ENTER] [4] [g] [yˣ] [3] [x²] [×] [5] [×]` $\to 720$ |
| **1,000** | $2^3 \times 5^3$ | `2^3 * 5^3` | `[2] [ENTER] [3] [g] [yˣ] [5] [ENTER] [3] [g] [yˣ] [×]` $\to 1000$ |
| **1,024** | $2^{10}$ | `2^10` | `[2] [ENTER] 10 [g] [yˣ]` $\to 1024$ |
| **1,729** | $7 \times 13 \times 19$ | `7 * 13 * 19` | `[7] [ENTER] 13 [×] 19 [×]` $\to 1729$ |

*Fun Fact about 1,729 (The Taxicab Number):* $1,729$ is the smallest whole number that can be built by adding two cubes in two different ways:
$$1,729 = 1^3 + 12^3 = 9^3 + 10^3$$
You can verify both cube sums on your SC-6:
- **First Cube Pair ($1^3 + 12^3$):** `[1] [ENTER] [3] [g] [yˣ] 12 [ENTER] [3] [g] [yˣ] [+]` $\to 1 + 1728 = 1729$.
- **Second Cube Pair ($9^3 + 10^3$):** `[9] [ENTER] [3] [g] [yˣ] 10 [ENTER] [3] [g] [yˣ] [+]` $\to 729 + 1000 = 1729$.

---

### C.5.4 GCF and LCM Reference Table for Common Number Pairs

The table below shows 9 popular number pairs, the prime blocks they share (`[GCF]`), the product of the two numbers, and their Least Common Multiple (`[f] [LCM]`):

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

### C.5.5 Goldbach's Even-Number Prime Puzzle (Evens 4 to 60)

In 1742, a mathematician named Christian Goldbach noticed an amazing pattern: **every even number greater than 2 can be written by adding two prime numbers together!**

You can test Goldbach's pattern on your SC-6 by picking any even number, checking two primes with `[PRIME]`, and adding them together:

| Even Number | Prime Pair Sum | Other Prime Pairs That Work | SC-6 RPN Check Keystrokes |
|:---:|:---:|:---|:---|
| **4** | $2 + 2$ | Only way | `[2] [ENTER] [2] [+]` $\to 4$ |
| **6** | $3 + 3$ | Only way | `[3] [ENTER] [3] [+]` $\to 6$ |
| **8** | $3 + 5$ | Only way | `[3] [ENTER] [5] [+]` $\to 8$ |
| **10** | $3 + 7$ | $5 + 5$ | `[3] [ENTER] [7] [+]` $\to 10$ |
| **12** | $5 + 7$ | Only way | `[5] [ENTER] [7] [+]` $\to 12$ |
| **14** | $3 + 11$ | $7 + 7$ | `[3] [ENTER] 11 [+]` $\to 14$ |
| **16** | $3 + 13$ | $5 + 11$ | `[3] [ENTER] 13 [+]` $\to 16$ |
| **18** | $5 + 13$ | $7 + 11$ | `[5] [ENTER] 13 [+]` $\to 18$ |
| **20** | $3 + 17$ | $7 + 13$ | `[3] [ENTER] 17 [+]` $\to 20$ |
| **22** | $3 + 19$ | $5 + 17, 11 + 11$ | `[3] [ENTER] 19 [+]` $\to 22$ |
| **24** | $5 + 19$ | $7 + 17, 11 + 13$ | `[5] [ENTER] 19 [+]` $\to 24$ |
| **26** | $3 + 23$ | $7 + 19, 13 + 13$ | `[3] [ENTER] 23 [+]` $\to 26$ |
| **28** | $5 + 23$ | $11 + 17$ | `[5] [ENTER] 23 [+]` $\to 28$ |
| **30** | $7 + 23$ | $11 + 19, 13 + 17$ | `[7] [ENTER] 23 [+]` $\to 30$ |
| **32** | $3 + 29$ | $13 + 19$ | `[3] [ENTER] 29 [+]` $\to 32$ |
| **34** | $3 + 31$ | $5 + 29, 11 + 23, 17 + 17$ | `[3] [ENTER] 31 [+]` $\to 34$ |
| **36** | $5 + 31$ | $7 + 29, 13 + 23, 17 + 19$ | `[5] [ENTER] 31 [+]` $\to 36$ |
| **38** | $7 + 31$ | $19 + 19$ | `[7] [ENTER] 31 [+]` $\to 38$ |
| **40** | $3 + 37$ | $11 + 29, 17 + 23$ | `[3] [ENTER] 37 [+]` $\to 40$ |
| **42** | $5 + 37$ | $11 + 31, 13 + 29, 19 + 23$ | `[5] [ENTER] 37 [+]` $\to 42$ |
| **44** | $3 + 41$ | $7 + 37, 13 + 31$ | `[3] [ENTER] 41 [+]` $\to 44$ |
| **46** | $3 + 43$ | $5 + 41, 17 + 29, 23 + 23$ | `[3] [ENTER] 43 [+]` $\to 46$ |
| **48** | $5 + 43$ | $7 + 41, 11 + 37, 17 + 31, 19 + 29$ | `[5] [ENTER] 43 [+]` $\to 48$ |
| **50** | $3 + 47$ | $7 + 43, 13 + 37, 19 + 31$ | `[3] [ENTER] 47 [+]` $\to 50$ |
| **52** | $5 + 47$ | $11 + 41, 23 + 29$ | `[5] [ENTER] 47 [+]` $\to 52$ |
| **54** | $7 + 47$ | $11 + 43, 13 + 41, 17 + 37, 23 + 31$ | `[7] [ENTER] 47 [+]` $\to 54$ |
| **56** | $3 + 53$ | $13 + 43, 19 + 37$ | `[3] [ENTER] 53 [+]` $\to 56$ |
| **58** | $5 + 53$ | $11 + 47, 17 + 41, 29 + 29$ | `[5] [ENTER] 53 [+]` $\to 58$ |
| **60** | $7 + 53$ | $13 + 47, 17 + 43, 19 + 41, 23 + 37, 29 + 31$ | `[7] [ENTER] 53 [+]` $\to 60$ |

---

### C.5.6 Perfect Numbers & Giant Factor Challenges

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
| `[2] [ENTER]` | 0 | 0 | 2 | 2 |
| `[5] [g] [yˣ]` | 0 | 0 | 0 | 32 |
| `[1] [-]` | 0 | 0 | 0 | 31 |
| `[PRIME]` | 0 | 0 | 0 | 31 (Flashes `PRIME`) |
| `[2] [ENTER]` | 0 | 31 | 2 | 2 |
| `[4] [g] [yˣ]` | 0 | 0 | 31 | 16 |
| `[×]` | 0 | 0 | 0 | 496 |

Register $X$ lands on **$496$**, the third perfect number! That same curiosity about giant powers of two led to one of history's most famous division checks: for over a hundred years, mathematicians wondered whether $4,294,967,297$ was a prime number, until Leonhard Euler discovered that $641$ divides into it evenly with zero remainder:
$$4,294,967,297 = 641 \times 6,700,417$$
You can test Euler's discovery right on your SC-6 by keying in `4294967297 [ENTER] 641 [÷]`, which lands cleanly on **$6,700,417.00$** with no decimal remainder!

---

## C.6 Quick-Reference Word-Rule Lookup Tables

Use the two lookup tables below whenever you need the fastest SC-6 keystroke pattern for a geometry, measurement, or money problem.

### C.6.1 Geometry & Measurement Quick Lookup

| Math Task | What You Know | Word Rule | SC-6 Keystroke Pattern |
|:---|:---|:---|:---|
| **Area of a Circle** | Radius | $\pi \times \text{Radius} \times \text{Radius}$ | `[Radius] [x²] [π] [×]` |
| **Distance Around a Circle** | Width (Diameter) | $\pi \times \text{Diameter}$ | `[Diameter] [π] [×]` |
| **Area of a Rectangle** | Length, Width | $\text{Length} \times \text{Width}$ | `[Length] [ENTER] [Width] [f] [RECT]` |
| **Perimeter of a Rectangle**| Length, Width | $2 \times (\text{Length} + \text{Width})$ | `[Length] [ENTER] [Width] [+] [2] [×]` |
| **Area of a Triangle** | Base, Height | $(\text{Base} \times \text{Height}) \div 2$ | `[Base] [ENTER] [Height] [×] [2] [÷]` |
| **Area of a Trapezoid** | Top, Bottom, Height| $(\text{Top} + \text{Bottom}) \div 2 \times \text{Height}$ | `[Top] [ENTER] [Bottom] [+] [2] [÷] [Height] [×]` |
| **Volume of a Cylinder** | Radius, Height | $(\pi \times \text{Radius}^2) \times \text{Height}$ | `[Radius] [x²] [π] [×] [Height] [×]` |
| **Volume of a Box** | Length, Width, Height| $\text{Length} \times \text{Width} \times \text{Height}$ | `[Length] [ENTER] [Width] [×] [Height] [×]` |
| **Surface Area of a Cube** | Side Length | $6 \times (\text{Side} \times \text{Side})$ | `[Side] [x²] [6] [×]` |
| **Percent of a Number** | Whole, Percent | $\text{Whole} \times (\text{Percent} \div 100)$ | `[Whole] [ENTER] [Percent] [%]` |
| **Percent Change** | Starting, Ending | $(\text{Ending} - \text{Starting}) \div \text{Starting} \times 100$ | `[Starting] [ENTER] [Ending] [g] [%CHG]` |
| **Fahrenheit to Celsius** | Temp in °F | $(\text{Temp F} - 32) \times 5 \div 9$ | `[Temp F] [ENTER] 32 [-] [5] [×] [9] [÷]` |
| **Celsius to Fahrenheit** | Temp in °C | $(\text{Temp C} \times 9 \div 5) + 32$ | `[Temp C] [ENTER] [9] [×] [5] [÷] 32 [+]` |
| **Speed (Unit Rate)** | Distance, Time | $\text{Distance} \div \text{Time}$ | `[Distance] [ENTER] [Time] [÷]` |
| **Unit Price** | Total Cost, Count | $\text{Total Cost} \div \text{Count}$ | `[Total Cost] [ENTER] [Count] [÷]` |
| **Miles to Kilometers** | Miles | $\text{Miles} \times 1.609344$ | `[Miles] [ENTER] 1.609344 [×]` |
| **Pounds to Kilograms** | Pounds | $\text{Pounds} \times 0.453592$ | `[Pounds] [ENTER] [.] 453592 [×]` |
| **Gallons to Liters** | Gallons | $\text{Gallons} \times 3.7854$ | `[Gallons] [ENTER] 3.7854 [×]` |

---

### C.6.2 Everyday Money & Shopping Word Rules

Because `[%]` on the SC-6 keeps the starting dollar amount sitting in Register $Y$, you can add sales tax or subtract a discount in one tap:

| Money Task | Word Rule | SC-6 Keystroke Pattern |
|:---|:---|:---|
| **Simple Interest Earned** | $\text{Starting Money} \times \text{Yearly Rate \%} \times \text{Years}$ | `[Money] [ENTER] [Rate] [%] [Years] [×] [$]` |
| **Sales Tax Amount** | $\text{Price} \times \text{Tax Rate \%}$ | `[Price] [ENTER] [Tax Rate] [%] [$]` |
| **Total Price with Tax** | $\text{Price} + \text{Sales Tax}$ | `[Price] [ENTER] [Tax Rate] [%] [+] [$]` |
| **Discount Saved** | $\text{Regular Price} \times \text{Discount \%}$ | `[Price] [ENTER] [Discount] [%] [$]` |
| **Sale Price After Discount** | $\text{Regular Price} - \text{Discount}$ | `[Price] [ENTER] [Discount] [%] [-] [$]` |
| **Restaurant Tip ($18\%$)**| $\text{Bill} \times 18\%$ | `[Bill] [ENTER] 18 [%] [$]` |

When money stays in a savings account for several years, the interest itself starts earning interest! For example, to watch a $\$500$ savings account grow at $4\%$ interest compounded yearly for $3$ years, multiply $\$500$ by $1.04$ three times ($1.04^3 \times \$500 = \$562.43$):

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `1.04` | 0 | 0 | 0 | 1.04 |
| `[ENTER]` | 0 | 0 | 1.04 | 1.04 |
| `[3]` | 0 | 0 | 1.04 | 3 |
| `[g] [yˣ]` | 0 | 0 | 0 | 1.124864 |
| `500` | 0 | 0 | 1.124864 | 500 |
| `[×]` | 0 | 0 | 0 | 562.43 |

After $3$ years, the account holds **$\$562.43$** total savings ($\$62.43$ in interest earned).

---

## C.7 Alignment with Elementary & Middle School Standards

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

## C.8 Annotated Bibliography & Primary Mathematical Sources

### C.8.1 Foundations of Logic & Computer Architecture

<a id="cite-lukasiewicz1924"></a>
**[lukasiewicz1924] Jan Łukasiewicz (1924)** — *Oznaczenie bez nawiasów (Parenthesis-Free Notation)*. *Komunikaty Polskiego Towarzystwa Matematycznego, Vol. 1, pp. 1–6*.
> **Annotation:** Introduces parenthesis-free prefix and postfix notation, demonstrating that operator position alone uniquely determines evaluation order without grouping symbols.  
> **Cited in Chapters:** [Ch 02](sc6/02-rpn-for-young-learners.md)

<a id="cite-burks1954"></a>
**[burks1954] Arthur W. Burks, Don W. Warren & Jesse B. Wright (1954)** — *An Analysis of a Logical Machine Using Parenthesis-Free Notation*. *Mathematical Tables and Other Aids to Computation, Vol. 8, No. 46, pp. 53–57*.
> **Annotation:** Formalizes Polish parenthesis-free postfix notation for electronic digital computers, laying the theoretical foundation for hardware-evaluated operational stacks.  
> **Cited in Chapters:** *Foundational reference & curriculum background*

### C.8.2 Corvallis Silicon & Handheld Architecture

<a id="cite-hamrick1980"></a>
**[hamrick1980] Kathy B. Hamrick (1980)** — *The History of Reverse Polish Notation*. *The Two-Year College Mathematics Journal, Vol. 11, No. 5, pp. 317–326*.
> **Annotation:** Traces the historical evolution of Polish notation from abstract Warsaw mathematical logic to Corvallis handheld scientific computing.  
> **Cited in Chapters:** [Ch 02](sc6/02-rpn-for-young-learners.md)

### C.8.3 Numerical Stability & Scientific Algorithms

<a id="cite-napier1614"></a>
**[napier1614] John Napier (1614)** — *Mirifici Logarithmorum Canonis Descriptio*. *Andrew Hart, Edinburgh*.
> **Annotation:** The invention of logarithms, transforming laborious multi-digit multiplication into addition and doubling the working lifespan of astronomers.  
> **Cited in Chapters:** [Ch 05](sc6/05-fractions-decimals-ratios.md)

<a id="cite-galilei1638"></a>
**[galilei1638] Galileo Galilei (1638)** — *Discorsi e Dimostrazioni Matematiche, intorno à due nuoue scienze (Dialogues Concerning Two New Sciences)*. *Louis Elsevier, Leiden*.
> **Annotation:** Establishes the geometric Square-Cube Law governing surface-area-to-volume scaling in structural mechanics and biological thermoregulation, as well as the isochronous law of the pendulum.  
> **Cited in Chapters:** [Ch 06](sc6/06-geometry-surface-area.md), [Ch 09](sc6/09-applied-stem-labs.md)

<a id="cite-gauss1809"></a>
**[gauss1809] Carl Friedrich Gauss (1809)** — *Theoria Motus Corporum Coelestium in Sectionibus Conicis Solem Ambientium*. *Perthes and Besser, Hamburg*.
> **Annotation:** Introduces the Method of Least Squares and the Gaussian Normal error distribution, recovering the lost celestial orbit of Ceres.  
> **Cited in Chapters:** [Ch 04](sc6/04-operations-skip-counting.md), [Ch 07](sc6/07-data-probability-primes.md)

<a id="cite-kahan1979"></a>
**[kahan1979] William M. Kahan (1979)** — *Personal Calculator Has Key to Solve Any Equation f(x) = 0*. *Hewlett-Packard Journal, Vol. 30, No. 12, pp. 20–26*.
> **Annotation:** Establishes the non-destructive base-preserving percentage invariant and foundational floating-point error bounds for handheld solvers.  
> **Cited in Chapters:** *Foundational reference & curriculum background*

### C.8.4 Breakout Mathematics & Scientific Nonfiction

<a id="cite-sartorius1856"></a>
**[sartorius1856] Wolfgang Sartorius von Waltershausen (1856)** — *Gauss zum Gedächtniss*. *S. Hirzel, pp. 12–13, Leipzig*.
> **Annotation:** Primary biographical source recording young Carl Friedrich Gauss's arithmetic series solution in J.G. Büttner's Brunswick classroom and his Low German exclamation 'Ligget se!' ('There it lies!').  
> **Cited in Chapters:** [Ch 04](sc6/04-operations-skip-counting.md)

<a id="cite-gardner1959"></a>
**[gardner1959] Martin Gardner (1959)** — *The Scientific American Book of Mathematical Puzzles and Diversions*. *Simon & Schuster, New York*.
> **Annotation:** Pioneered popular mathematical recreations, flexagons, hexaflexagons, and spatial puzzles that celebrate mathematical play.  
> **Cited in Chapters:** [Ch 07](sc6/07-data-probability-primes.md)

<a id="cite-gould1977"></a>
**[gould1977] Stephen Jay Gould (1977)** — *Ever Since Darwin: Reflections in Natural History*. *W. W. Norton & Company, New York*.
> **Annotation:** Analyzes the evolutionary biology of 13-year and 17-year periodical cicadas (*Magicicada*) and prime-number predator avoidance cycles.  
> **Cited in Chapters:** [Ch 07](sc6/07-data-probability-primes.md)

<a id="cite-singh1997"></a>
**[singh1997] Simon Singh (1997)** — *Fermat's Enigma: The Epic Quest to Solve the World's Greatest Mathematical Problem*. *Walker & Company, New York*.
> **Annotation:** Captures the three-century human quest to prove Fermat's Last Theorem, conveying the passion and stakes of mathematical discovery.  
> **Cited in Chapters:** [Ch 07](sc6/07-data-probability-primes.md)

<a id="cite-ifrah2000"></a>
**[ifrah2000] Georges Ifrah (2000)** — *The Universal History of Numbers: From Prehistory to the Invention of the Computer*. *John Wiley & Sons, New York*.
> **Annotation:** Comprehensive historical account of tally stones, Mesopotamian sexagesimal accounting, Egyptian hieroglyphic numerals, and the independent invention of zero and positional place value in India and Mesoamerica.  
> **Cited in Chapters:** [Ch 03](sc6/03-counting-place-value.md)

<a id="cite-webb2001"></a>
**[webb2001] Glenn F. Webb (2001)** — *The Prime Number Periodical Cicada Problem*. *Discrete and Continuous Dynamical Systems - Series B, Vol. 1, No. 3, pp. 387–399*.
> **Annotation:** Mathematical population model proving that 13-year and 17-year prime emergence periods minimize resonance with multi-year predator-prey cycles.  
> **Cited in Chapters:** [Ch 07](sc6/07-data-probability-primes.md)

<a id="cite-gilbert2006"></a>
**[gilbert2006] Caroline Gilbert, Graham Robertson, Yvon Le Maho, Yasuhiko Naito & André Ancel (2006)** — *Huddling behavior in emperor penguins: Dynamics of huddling*. *Physiology & Behavior, Vol. 88, No. 4-5, pp. 479–488*.
> **Annotation:** Quantifies how Emperor penguins (*Aptenodytes forsteri*) reduce exposed windward surface area per bird to survive Antarctic winter blizzards.  
> **Cited in Chapters:** [Ch 06](sc6/06-geometry-surface-area.md)

<a id="cite-strogatz2012"></a>
**[strogatz2012] Steven Strogatz (2012)** — *The Joy of x: A Guided Tour of Math, from One to Infinity*. *Eamon Dolan / Houghton Mifflin Harcourt, Boston*.
> **Annotation:** Opens every mathematical section with everyday curiosity and intuitive aha-moments, showing how mathematical beauty connects to human experience.  
> **Cited in Chapters:** [Ch 06](sc6/06-geometry-surface-area.md), [Foreword](sc6/index.md)

<a id="cite-ellenberg2014"></a>
**[ellenberg2014] Jordan Ellenberg (2014)** — *How Not to Be Wrong: The Power of Mathematical Thinking*. *Penguin Press, New York*.
> **Annotation:** Exposes common cognitive biases, non-linear scaling traps, and statistical survivorship fallacies with conversational wit.  
> **Cited in Chapters:** *Foundational reference & curriculum background*

<a id="cite-munroe2014"></a>
**[munroe2014] Randall Munroe (2014)** — *What If?: Serious Scientific Answers to Absurd Hypothetical Questions*. *Houghton Mifflin Harcourt, Boston*.
> **Annotation:** Applies order-of-magnitude dimensional analysis, physics Fermi approximations, and creative mathematical modeling to wild scenarios.  
> **Cited in Chapters:** *Foundational reference & curriculum background*

<a id="cite-macaulay2016"></a>
**[macaulay2016] David Macaulay (2016)** — *The Way Things Work Now*. *HMH Books for Young Readers, Boston*.
> **Annotation:** Visualizes mechanical physical mechanisms and gear systems through step-by-step illustrations, inspiring the SC-6 tactile manipulative studio design.  
> **Cited in Chapters:** [App A](sc6/appendix-a-manipulative-blueprints.md), [Ch 01](sc6/01-hardware-architecture.md), [Ch 05](sc6/05-fractions-decimals-ratios.md), [Foreword](sc6/index.md)

<a id="cite-parker2019"></a>
**[parker2019] Matt Parker (2019)** — *Humble Pi: A Comedy of Maths Errors*. *Riverhead Books, New York*.
> **Annotation:** Explores famous engineering catastrophes and numerical bugs caused by round-off errors, integer overflows, and unit conversion failures.  
> **Cited in Chapters:** [Ch 06](sc6/06-geometry-surface-area.md)

### C.8.5 Pedagogy, Cognitive Science & Manipulatives

<a id="cite-polya1945"></a>
**[polya1945] George Pólya (1945)** — *How to Solve It: A New Aspect of Mathematical Method*. *Princeton University Press, Princeton, NJ*.
> **Annotation:** Defines the heuristic problem-solving framework (Understand, Plan, Carry Out, Look Back), aligned with step-by-step RPN stack inspection.  
> **Cited in Chapters:** [Ch 04](sc6/04-operations-skip-counting.md), [Ch 06](sc6/06-geometry-surface-area.md)

<a id="cite-miller1956"></a>
**[miller1956] George A. Miller (1956)** — *The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information*. *Psychological Review, Vol. 63, No. 2, pp. 81–97*.
> **Annotation:** Identifies the 7 ± 2 item capacity limit of human short-term working memory, validating the 4-register stack as the optimal cognitive span.  
> **Cited in Chapters:** [Ch 01](sc6/01-hardware-architecture.md), [Ch 02](sc6/02-rpn-for-young-learners.md)

<a id="cite-dienes1960"></a>
**[dienes1960] Zoltan P. Dienes (1960)** — *Building Up Mathematics*. *Hutchinson Educational, London*.
> **Annotation:** Introduces Multibase Arithmetic Blocks and the Dynamic Principle of mathematical learning, grounding the SC-6 Place Value Studio.  
> **Cited in Chapters:** [App A](sc6/appendix-a-manipulative-blueprints.md), [Ch 03](sc6/03-counting-place-value.md), [Ch 05](sc6/05-fractions-decimals-ratios.md)

<a id="cite-bruner1966"></a>
**[bruner1966] Jerome S. Bruner (1966)** — *Toward a Theory of Instruction*. *Harvard University Press, Cambridge, MA*.
> **Annotation:** Establishes the developmental progression from physical action to visual imagery and symbolic notation underpinning the StackCalc manipulative studios and display modes.  
> **Cited in Chapters:** [App A](sc6/appendix-a-manipulative-blueprints.md), [Ch 02](sc6/02-rpn-for-young-learners.md), [Ch 06](sc6/06-geometry-surface-area.md), [Ch 07](sc6/07-data-probability-primes.md), [Ch 09](sc6/09-applied-stem-labs.md), [Foreword](sc6/index.md)

<a id="cite-sweller1988"></a>
**[sweller1988] John Sweller (1988)** — *Cognitive Load During Problem Solving: Effects on Learning*. *Cognitive Science, Vol. 12, No. 2, pp. 257–285*.
> **Annotation:** Establishes Cognitive Load Theory, demonstrating that parentheses and operator precedence buffering in algebraic calculators impose extraneous cognitive load.  
> **Cited in Chapters:** [Ch 01](sc6/01-hardware-architecture.md), [Ch 02](sc6/02-rpn-for-young-learners.md)

<a id="cite-falkner1999"></a>
**[falkner1999] Karen P. Falkner, Thomas P. Carpenter & Elizabeth Fennema (1999)** — *Children's Understanding of Equality: A Foundation for Algebra*. *Teaching Children Mathematics, Vol. 6, No. 4, pp. 232–236*.
> **Annotation:** Landmark empirical study demonstrating that elementary students misinterpret the equals sign (=) as a command to execute an operation rather than relational equivalence.  
> **Cited in Chapters:** [Ch 02](sc6/02-rpn-for-young-learners.md)

<a id="cite-ma1999"></a>
**[ma1999] Liping Ma (1999)** — *Knowing and Teaching Elementary Mathematics: Teachers' Understanding of Fundamental Mathematics in China and the United States*. *Lawrence Erlbaum Associates, Mahwah, NJ*.
> **Annotation:** Demonstrates Profound Understanding of Fundamental Mathematics (PUFM) through transparent conceptual operations and division with remainders.  
> **Cited in Chapters:** [Ch 08](sc6/08-math-quiz-engine.md), [Foreword](sc6/index.md)

<a id="cite-singapore2014"></a>
**[singapore2014] Ministry of Education Singapore (2014)** — *Primary Mathematics Teaching and Learning Syllabus*. *Curriculum Planning and Development Division, Singapore*.
> **Annotation:** The Singapore Math framework emphasizing bar modeling, hands-on block-to-symbol transitions, and relational understanding in fractions and ratios.  
> **Cited in Chapters:** [Ch 03](sc6/03-counting-place-value.md), [Ch 04](sc6/04-operations-skip-counting.md), [Ch 05](sc6/05-fractions-decimals-ratios.md)

### C.8.6 Standards & Hardware Handbooks

<a id="cite-ccssm2010"></a>
**[ccssm2010] National Governors Association Center for Best Practices & Council of Chief State School Officers (2010)** — *Common Core State Standards for Mathematics*. *National Governors Association & CCSSO, Washington, DC*.
> **Annotation:** The foundational curriculum standards framework governing K-12 operations, algebraic thinking, number sense, and geometry in US classrooms.  
> **Cited in Chapters:** *Foundational reference & curriculum background*

### C.8.7 Complete BibTeX Catalog (StackCalc SC-6 Elementary)

```bibtex
@article{lukasiewicz1924,
  author    = {Łukasiewicz, Jan},
  title     = {Oznaczenie bez nawiasów (Parenthesis-Free Notation)},
  journal   = {Komunikaty Polskiego Towarzystwa Matematycznego},
  volume    = {1},
  pages     = {1--6},
  year      = {1924},
  note      = {Introduces parenthesis-free prefix and postfix notation, demonstrating that operator position alone uniquely determines evaluation order without grouping symbols.}
}

@article{burks1954,
  author    = {Burks, Arthur W. and Warren, Don W. and Wright, Jesse B.},
  title     = {An Analysis of a Logical Machine Using Parenthesis-Free Notation},
  journal   = {Mathematical Tables and Other Aids to Computation},
  volume    = {8},
  number    = {46},
  pages     = {53--57},
  year      = {1954},
  note      = {Formalizes Polish parenthesis-free postfix notation for electronic digital computers, laying the theoretical foundation for hardware-evaluated operational stacks.}
}

@article{hamrick1980,
  author    = {Hamrick, Kathy B.},
  title     = {The History of Reverse Polish Notation},
  journal   = {The Two-Year College Mathematics Journal},
  volume    = {11},
  number    = {5},
  pages     = {317--326},
  year      = {1980},
  note      = {Traces the historical evolution of Polish notation from abstract Warsaw mathematical logic to Corvallis handheld scientific computing.}
}

@book{napier1614,
  author    = {Napier, John},
  title     = {Mirifici Logarithmorum Canonis Descriptio},
  publisher = {Andrew Hart},
  address   = {Edinburgh},
  year      = {1614},
  note      = {The invention of logarithms, transforming laborious multi-digit multiplication into addition and doubling the working lifespan of astronomers.}
}

@book{gauss1809,
  author    = {Gauss, Carl Friedrich},
  title     = {Theoria Motus Corporum Coelestium in Sectionibus Conicis Solem Ambientium},
  publisher = {Perthes and Besser},
  address   = {Hamburg},
  year      = {1809},
  note      = {Introduces the Method of Least Squares and the Gaussian Normal error distribution, recovering the lost celestial orbit of Ceres.}
}

@article{kahan1979,
  author    = {Kahan, William M.},
  title     = {Personal Calculator Has Key to Solve Any Equation f(x) = 0},
  journal   = {Hewlett-Packard Journal},
  volume    = {30},
  number    = {12},
  pages     = {20--26},
  year      = {1979},
  note      = {Establishes the non-destructive base-preserving percentage invariant and foundational floating-point error bounds for handheld solvers.}
}

@book{strogatz2012,
  author    = {Strogatz, Steven},
  title     = {The Joy of x: A Guided Tour of Math, from One to Infinity},
  publisher = {Eamon Dolan / Houghton Mifflin Harcourt},
  address   = {Boston},
  year      = {2012},
  isbn      = {978-0547517650},
  note      = {Opens every mathematical section with everyday curiosity and intuitive aha-moments, showing how mathematical beauty connects to human experience.}
}

@book{ellenberg2014,
  author    = {Ellenberg, Jordan},
  title     = {How Not to Be Wrong: The Power of Mathematical Thinking},
  publisher = {Penguin Press},
  address   = {New York},
  year      = {2014},
  isbn      = {978-1594205224},
  note      = {Exposes common cognitive biases, non-linear scaling traps, and statistical survivorship fallacies with conversational wit.}
}

@book{parker2019,
  author    = {Parker, Matt},
  title     = {Humble Pi: A Comedy of Maths Errors},
  publisher = {Riverhead Books},
  address   = {New York},
  year      = {2019},
  isbn      = {978-0593084694},
  note      = {Explores famous engineering catastrophes and numerical bugs caused by round-off errors, integer overflows, and unit conversion failures.}
}

@book{munroe2014,
  author    = {Munroe, Randall},
  title     = {What If?: Serious Scientific Answers to Absurd Hypothetical Questions},
  publisher = {Houghton Mifflin Harcourt},
  address   = {Boston},
  year      = {2014},
  isbn      = {978-0544272996},
  note      = {Applies order-of-magnitude dimensional analysis, physics Fermi approximations, and creative mathematical modeling to wild scenarios.}
}

@book{macaulay2016,
  author    = {Macaulay, David},
  title     = {The Way Things Work Now},
  publisher = {HMH Books for Young Readers},
  address   = {Boston},
  year      = {2016},
  isbn      = {978-0544824386},
  note      = {Visualizes mechanical physical mechanisms and gear systems through step-by-step illustrations, inspiring the SC-6 tactile manipulative studio design.}
}

@book{singh1997,
  author    = {Singh, Simon},
  title     = {Fermat's Enigma: The Epic Quest to Solve the World's Greatest Mathematical Problem},
  publisher = {Walker & Company},
  address   = {New York},
  year      = {1997},
  isbn      = {978-0385493628},
  note      = {Captures the three-century human quest to prove Fermat's Last Theorem, conveying the passion and stakes of mathematical discovery.}
}

@book{gardner1959,
  author    = {Gardner, Martin},
  title     = {The Scientific American Book of Mathematical Puzzles and Diversions},
  publisher = {Simon & Schuster},
  address   = {New York},
  year      = {1959},
  note      = {Pioneered popular mathematical recreations, flexagons, hexaflexagons, and spatial puzzles that celebrate mathematical play.}
}

@article{miller1956,
  author    = {Miller, George A.},
  title     = {The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information},
  journal   = {Psychological Review},
  volume    = {63},
  number    = {2},
  pages     = {81--97},
  year      = {1956},
  note      = {Identifies the 7 ± 2 item capacity limit of human short-term working memory, validating the 4-register stack as the optimal cognitive span.}
}

@book{bruner1966,
  author    = {Bruner, Jerome S.},
  title     = {Toward a Theory of Instruction},
  publisher = {Harvard University Press},
  address   = {Cambridge, MA},
  year      = {1966},
  note      = {Establishes the developmental progression from physical action to visual imagery and symbolic notation underpinning the StackCalc manipulative studios and display modes.}
}

@book{dienes1960,
  author    = {Dienes, Zoltan P.},
  title     = {Building Up Mathematics},
  publisher = {Hutchinson Educational},
  address   = {London},
  year      = {1960},
  note      = {Introduces Multibase Arithmetic Blocks and the Dynamic Principle of mathematical learning, grounding the SC-6 Place Value Studio.}
}

@book{polya1945,
  author    = {Pólya, George},
  title     = {How to Solve It: A New Aspect of Mathematical Method},
  publisher = {Princeton University Press},
  address   = {Princeton, NJ},
  year      = {1945},
  note      = {Defines the heuristic problem-solving framework (Understand, Plan, Carry Out, Look Back), aligned with step-by-step RPN stack inspection.}
}

@article{sweller1988,
  author    = {Sweller, John},
  title     = {Cognitive Load During Problem Solving: Effects on Learning},
  journal   = {Cognitive Science},
  volume    = {12},
  number    = {2},
  pages     = {257--285},
  year      = {1988},
  note      = {Establishes Cognitive Load Theory, demonstrating that parentheses and operator precedence buffering in algebraic calculators impose extraneous cognitive load.}
}

@book{ma1999,
  author    = {Ma, Liping},
  title     = {Knowing and Teaching Elementary Mathematics: Teachers' Understanding of Fundamental Mathematics in China and the United States},
  publisher = {Lawrence Erlbaum Associates},
  address   = {Mahwah, NJ},
  year      = {1999},
  note      = {Demonstrates Profound Understanding of Fundamental Mathematics (PUFM) through transparent conceptual operations and division with remainders.}
}

@techreport{singapore2014,
  author      = {{Ministry of Education Singapore}},
  title       = {Primary Mathematics Teaching and Learning Syllabus},
  institution = {Curriculum Planning and Development Division},
  address     = {Singapore},
  year        = {2014},
  note        = {The Singapore Math framework emphasizing bar modeling, Concrete-Pictorial-Abstract transitions, and relational understanding in fractions and ratios.}
}

@techreport{ccssm2010,
  author      = {{National Governors Association Center for Best Practices and Council of Chief State School Officers}},
  title       = {Common Core State Standards for Mathematics},
  institution = {NGA Center for Best Practices and CCSSO},
  address     = {Washington, DC},
  year        = {2010},
  note        = {The foundational curriculum standards framework governing K-12 operations, algebraic thinking, number sense, and geometry in US classrooms.}
}

@article{falkner1999,
  author = {Karen P. Falkner, Thomas P. Carpenter & Elizabeth Fennema},
  title = {Children's Understanding of Equality: A Foundation for Algebra},
  year = {1999},
  journal = {Teaching Children Mathematics},
  volume = {6},
  number = {4},
  pages = {232--236},
}

@book{ifrah2000,
  author = {Georges Ifrah},
  title = {The Universal History of Numbers: From Prehistory to the Invention of the Computer},
  year = {2000},
  publisher = {John Wiley & Sons},
  address = {New York},
  isbn = {978-0471393405},
}

@book{sartorius1856,
  author = {Wolfgang Sartorius von Waltershausen},
  title = {Gauss zum Gedächtniss},
  year = {1856},
  pages = {12--13},
  publisher = {S. Hirzel},
  address = {Leipzig},
}

@book{galilei1638,
  author = {Galileo Galilei},
  title = {Discorsi e Dimostrazioni Matematiche, intorno à due nuoue scienze (Dialogues Concerning Two New Sciences)},
  year = {1638},
  publisher = {Louis Elsevier},
  address = {Leiden},
}

@article{gilbert2006,
  author = {Caroline Gilbert, Graham Robertson, Yvon Le Maho, Yasuhiko Naito & André Ancel},
  title = {Huddling behavior in emperor penguins: Dynamics of huddling},
  year = {2006},
  journal = {Physiology & Behavior},
  volume = {88},
  number = {4-5},
  pages = {479--488},
}

@book{gould1977,
  author = {Stephen Jay Gould},
  title = {Ever Since Darwin: Reflections in Natural History},
  year = {1977},
  publisher = {W. W. Norton & Company},
  address = {New York},
  isbn = {978-0393308181},
}

@article{webb2001,
  author = {Glenn F. Webb},
  title = {The Prime Number Periodical Cicada Problem},
  year = {2001},
  journal = {Discrete and Continuous Dynamical Systems - Series B},
  volume = {1},
  number = {3},
  pages = {387--399},
}
```


---

For detailed hands-on lesson plans implementing these rules in classroom workshop stations, see [Appendix B: Teacher Lesson Plans & Diagnostic Protocols](sc6/appendix-b-teacher-lesson-plans.md). For physical fabrication of geometric models and calibration gauges, see [Appendix A: Manipulative Blueprints & 3D Printing Fabrication Guide](sc6/appendix-a-manipulative-blueprints.md).

---

# Appendix D: Keycap Matrix & Layout Directory

## D.1 Keypad Physical Geometry & Tactile Matrix

The StackCalc SC-6 elementary keypad is designed specifically for young hands, everyday classroom durability, and clear physical feedback on every math operation.

The physical keypad comprises 43 mechanical switch positions organized into three kid-proof, ergonomic functional zones:

![StackCalc SC-6 Elementary Calculator Faceplate & 43-Key Topography](../assets/manuals/screenshots/sc6_hero_calculator.png)
*Figure D.1: StackCalc SC-6 Elementary RPN Calculator physical hardware faceplate render, showing the 43-key layout, double-wide `[ENTER]`, concrete manipulative mode keys (`[▦]` Ten-Frame, `[🕒]` Planetary Clock), and high-contrast `[f]` and `[g]` shift legends.*

### D.1.1 Upper Math & Number Sense Zone (Rows 0–2, 6 Columns)
- **Purpose:** Powers, place value (`[PV]`), fractions (`[a ᵇ/c]`, `[g] [SIMP]`), number theory (`[GCF]`, `[PRIME]`), and classroom data tools (`[Σ+]`, `[IQR]`).

| Row | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 0** | `[x²]` | `[x!]` | `[π]` | `[x³]` | `[PV]` | `[$]` |
| **Row 1** | `[FDISP]` | `[a ᵇ/c]` | `[GCF]` | `[PRIME]` | `[x⇄y]` | `[+/-]` |
| **Row 2** | `[FRQ]` | `[RNG]` | `[IQR]` | `[Σ+]` | `[N]` | `[%]` |

### D.1.2 Concrete Manipulative & Stack Transition Zone (Row 3)
- **ENTER Key:** Double-wide key spanning Columns 0 and 1 (primary RPN stack elevator button positioned right beneath your left thumb), alongside visual mode buttons (`[🕒]`, `[▦]`, `[NUM]`).

| Row | Col 0 & 1 (Double-Wide) | Col 2 | Col 3 | Col 4 | Col 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 3** | `[ENTER]` | `[🕒]` | `[▦]` | `[NUM]` | `[<-]` |

### D.1.3 Lower Arithmetic & Geometry Zone (Rows 4–7, 5 Columns)
- **Purpose:** High-visibility digit entry (`0`–`9`), core arithmetic (`÷, ×, -, +`), polyhedral dice (`[🎲]`), color-coded shift keys (`[f]`, `[g]`), and `[C]` (Clear / Wake / `[f] [?]` Quiz).

| Row | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 4** | `[🎲]` | `[7]` | `[8]` | `[9]` | `[÷]` |
| **Row 5** | `[f]` (f-Shift) | `[4]` | `[5]` | `[6]` | `[×]` |
| **Row 6** | `[g]` (g-Shift) | `[1]` | `[2]` | `[3]` | `[-]` |
| **Row 7** | `[C]` (ON) | `[0]` | `[.]` | `[≠]` | `[+]` |

### D.1.4 Tactile Keys, No-Bounce Typing & Classroom Battery Life
* **Crisp Tactile Click:** Each key uses a responsive tactile switch under a sculpted Shore 90A TPU keycap that gives a clear physical click. Students know right away that a number or operation has been entered without having to guess or press a key twice. (Full mechanical CAD drawings and enclosure files are available at **[stackcalc.io/hardware](https://stackcalc.io/hardware)**.)
* **No-Bounce Typing Protection:** Built-in key filtering registers each press cleanly and blocks accidental double-taps, even when excited students type rapidly during timed math sprints.
* **Instant Wake & Multi-Year Battery Life:** When stored in a backpack or classroom bin, the SC-6 automatically enters a deep power-saving sleep mode after 3 minutes of inactivity while keeping all four stack shelves ($X, Y, Z, T$), memory registers, statistics, and quiz levels safely saved. Tapping `[C]` (Row 7, Col 0) wakes the calculator instantaneously for months and years of classroom use on a single coin-cell battery.

---

## D.2 The Complete 43-Key Directory & Chapter Guide

The table below catalogs every keycap position, primary legend, `[f]` and `[g]` shift combinations, grade band, and direct links to the chapters where each key is introduced and practiced:

| Key # | Row & Col | Primary Legend | `[f]` Shift | `[g]` Shift | Grade Band | Chapter Guide & Key Topics |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- |
| **1** | R0, C0 | `[x²]` | `[f] [√x]` Root | `[g] [yˣ]` Power | Gr 5–6+ | [Chapter 6: Square Area & Roots](sc6/06-geometry-surface-area.md) • [Chapter 4: Powers](sc6/04-operations-skip-counting.md) |
| **2** | R0, C1 | `[x!]` | `[f] [nCr]` Comb | `[g] [nPr]` Perm | Gr 6+ | [Chapter 7: Counting Choices & Arrangements](sc6/07-data-probability-primes.md) |
| **3** | R0, C2 | `[π]` | `[f] [e]` Euler | `[g] [ˣ√y]` Radic | Gr 5–6+ | [Chapter 6: Circle Geometry & 3D Volumes](sc6/06-geometry-surface-area.md) |
| **4** | R0, C3 | `[x³]` | `[f] [10ˣ]` Exp | `[g] [LOG]` Base-10 | Gr 5–6+ | [Chapter 6: 3D Cube Volumes](sc6/06-geometry-surface-area.md) • [Chapter 3: Place Value Powers](sc6/03-counting-place-value.md) |
| **5** | R0, C4 | `[PV]` | `[f] [IP]` Int Part | `[g] [FP]` Frac Part | Gr 3–4 | [Chapter 3: Place Value Decomposition](sc6/03-counting-place-value.md) • [Chapter 5: Whole & Fractional Parts](sc6/05-fractions-decimals-ratios.md) |
| **6** | R0, C5 | `[$]` | `[f] [ALL]` Full | `[g] [RND]` Round | Gr 3–5 | [Chapter 3: Currency & Place Value](sc6/03-counting-place-value.md) • [Chapter 4: Rounding](sc6/04-operations-skip-counting.md) |
| **7** | R1, C0 | `[FDISP]` | `[f] [1/x]` Recip | `[g] [/c]` Denom | Gr 3–5 | [Chapter 5: Fraction Entry, Reciprocals & Fixed Denominators](sc6/05-fractions-decimals-ratios.md) |
| **8** | R1, C1 | `[a ᵇ/c]` | `[f] [d/c]` Improper | `[g] [SIMP]` Step | Gr 3–5 | [Chapter 5: Mixed Numbers, Improper Fractions & Step-by-Step Simplify](sc6/05-fractions-decimals-ratios.md) |
| **9** | R1, C2 | `[GCF]` | `[f] [LCM]` Multiple | `[g] [a:b]` Ratio | Gr 5–6 | [Chapter 7: Number Theory GCF & LCM](sc6/07-data-probability-primes.md) • [Chapter 5: Ratios & Rates](sc6/05-fractions-decimals-ratios.md) |
| **10**| R1, C3 | `[PRIME]` | `[f] [C.FAC]` ComFac | `[g] [FACT]` Tree | Gr 5–6 | [Chapter 7: Prime Studio & Factorization](sc6/07-data-probability-primes.md) |
| **11**| R1, C4 | `[x⇄y]` | `[f] [R↓]` Roll Down | `[g] [REP]` Replicate | Gr 3–4 | [Chapter 2: Stack Swapping & Rolling](sc6/02-rpn-for-young-learners.md) • [Chapter 4: Constant Repeat Skip-Counting](sc6/04-operations-skip-counting.md) |
| **12**| R1, C5 | `[+/-]` | `[f] [E]` Exponent | `[ABS]` Abs | Gr 5–6 | [Chapter 7: Signed Numbers & Absolute Value](sc6/07-data-probability-primes.md) • [Chapter 3: Big Numbers](sc6/03-counting-place-value.md) |
| **13**| R2, C0 | `[FRQ]` | `[f] [MED]` Median | `[g] [MODE]` Mode | Gr 5–6 | [Chapter 7: Frequency Tables, Median & Mode](sc6/07-data-probability-primes.md) |
| **14**| R2, C1 | `[RNG]` | `[f] [MIN]` Minimum | `[g] [MAX]` Maximum | Gr 5–6 | [Chapter 7: Data Spread & Extremes](sc6/07-data-probability-primes.md) |
| **15**| R2, C2 | `[IQR]` | `[f] [1Q]` Quartile 1| `[g] [3Q]` Quartile 3| Gr 6+ | [Chapter 7: Quartiles & Box Plots](sc6/07-data-probability-primes.md) |
| **16**| R2, C3 | `[Σ+]` | `[f] [Σ-]` Remove | `[g] [MAD]` MeanDev | Gr 4–6 | [Chapter 6: Master Surface Area via Stats](sc6/06-geometry-surface-area.md) • [Chapter 7: Mean Absolute Deviation](sc6/07-data-probability-primes.md) |
| **17**| R2, C4 | `[N]` | `[f] [Σx]` Total Sum | `[g] [x̄]` Mean Avg | Gr 5–6 | [Chapter 7: Sample Count & Fair-Share Mean](sc6/07-data-probability-primes.md) |
| **18**| R2, C5 | `[%]` | `[f] [▸%]` Dec to Pct | `[g] [%CHG]` Change | Gr 5–6 | [Chapter 5: Percentages, Tips & Discounts](sc6/05-fractions-decimals-ratios.md) |
| **19**| R3, C0-1| `[ENTER]` | `[f] [LASTX]` Check | `[g] [SHOW]` 15-Dig | Gr 3–6 | [Chapter 2: The Elevator Push](sc6/02-rpn-for-young-learners.md) • [Chapter 4: Last Number Self-Check](sc6/04-operations-skip-counting.md) • [Chapter 8: Quiz Submit](sc6/08-math-quiz-engine.md) |
| **20**| R3, C2 | `[🕒]` | `[f] [▸HR]` Decimal | `[g] [▸HMS]` Clock | Gr 3–5 | [Chapter 6: Planetary Geared Clock & Elapsed Time](sc6/06-geometry-surface-area.md) |
| **21**| R3, C3 | `[▦]` | `[f] [LINE]` Line | `[g] [COUNT]` Step | Gr 3–5 | [Chapter 3: Ten-Frame, Number Line & Number Rack](sc6/03-counting-place-value.md) |
| **22**| R3, C4 | `[NUM]` | `[f] [SCI]` Sci Not | `[g] [FIX]` Fixed Dec | Gr 3–6 | [Chapter 2: Numerical 4-Stack Mode](sc6/02-rpn-for-young-learners.md) • [Chapter 3: Display Formats](sc6/03-counting-place-value.md) |
| **23**| R3, C5 | `[<-]` | `[f] [CSTK]` Clr Stk | `[g] [CLΣ]` Clr Stat| Gr 3–6 | [Chapter 2: Backspace & Clear Stack](sc6/02-rpn-for-young-learners.md) • [Chapter 6: Clear Stats Basket](sc6/06-geometry-surface-area.md) |
| **24**| R4, C0 | `[🎲]` | `[f] [1…x]` Random | `[g] [t…x]` Range | Gr 3–6 | [Chapter 7: Polyhedral Dice & Probability Trials](sc6/07-data-probability-primes.md) |
| **25**| R4, C1 | `[7]` | `[f] [RECT]` Area | `[g] [TRI]` Area | Gr 3–6 | [Chapter 3: Digit Entry](sc6/03-counting-place-value.md) • [Chapter 6: Rectangle & Triangle Area](sc6/06-geometry-surface-area.md) |
| **26**| R4, C2 | `[8]` | `[f] [CIRC]` Area | `[g] [HYP]` Hypoten | Gr 3–6 | [Chapter 3: Digit Entry](sc6/03-counting-place-value.md) • [Chapter 6: Circle Area & Hypotenuse](sc6/06-geometry-surface-area.md) |
| **27**| R4, C3 | `[9]` | `[f] [PRISM]` Volume | `[g] [CONE]` Volume | Gr 3–6 | [Chapter 3: Digit Entry](sc6/03-counting-place-value.md) • [Chapter 6: Prism & Cone Volume](sc6/06-geometry-surface-area.md) |
| **28**| R4, C4 | `[÷]` | `[f] [MOD]` Rem | `[g] [÷R]` Quotient | Gr 3–5 | [Chapter 4: Division, Quotient & Remainder](sc6/04-operations-skip-counting.md) |
| **29**| R5, C0 | `[f]` (f-Shift)| *(f-Shift Latch)* | *(f-Shift Latch)* | Gr 3–6 | [Chapter 1: Primary `[f]` Shift Key](sc6/01-hardware-architecture.md) |
| **30**| R5, C1 | `[4]` | `[f] [▸g]` Grams | `[g] [▸oz]` Ounces | Gr 3–6 | [Chapter 3: Digit Entry](sc6/03-counting-place-value.md) • [Chapter 9: 3D Print Weight in Grams](sc6/09-applied-stem-labs.md) |
| **31**| R5, C2 | `[5]` | `[f] [▸ft]` Feet | `[g] [▸mi]` Miles | Gr 3–6 | [Chapter 3: Digit Entry](sc6/03-counting-place-value.md) • [Chapter 9: Distance Scaling](sc6/09-applied-stem-labs.md) |
| **32**| R5, C3 | `[6]` | `[f] [▸mL]` Millilit | `[g] [▸fl]` Fluid Oz| Gr 3–6 | [Chapter 3: Digit Entry](sc6/03-counting-place-value.md) • [Chapter 9: Kitchen Recipe Volumes](sc6/09-applied-stem-labs.md) |
| **33**| R5, C4 | `[×]` | *(Unassigned)* | `[g] [FLAGS]` Stack | Gr 3–5 | [Chapter 4: Array Multiplication](sc6/04-operations-skip-counting.md) • [Chapter 2: Stack Depth Modes](sc6/02-rpn-for-young-learners.md) |
| **34**| R6, C0 | `[g]` (g-Shift)| *(g-Shift Latch)* | *(g-Shift Latch)* | Gr 3–6 | [Chapter 1: Secondary `[g]` Shift Key](sc6/01-hardware-architecture.md) |
| **35**| R6, C1 | `[1]` | `[f] [▸kg]` Kilograms| `[g] [▸lb]` Pounds | Gr 3–6 | [Chapter 3: Digit Entry](sc6/03-counting-place-value.md) • [Chapter 9: Mass Conversions](sc6/09-applied-stem-labs.md) |
| **36**| R6, C2 | `[2]` | `[f] [▸°C]` Celsius | `[g] [▸°F]` Fahren | Gr 3–6 | [Chapter 3: Digit Entry](sc6/03-counting-place-value.md) • [Chapter 9: Solar Oven Temperatures](sc6/09-applied-stem-labs.md) |
| **37**| R6, C3 | `[3]` | `[f] [▸cm]` Centimet | `[g] [▸in]` Inches | Gr 3–6 | [Chapter 3: Digit Entry](sc6/03-counting-place-value.md) • [Chapter 9: 3D Print Measurements](sc6/09-applied-stem-labs.md) |
| **38**| R6, C4 | `[-]` | `[f] [▸L]` Liters | `[g] [▸gal]` Gallons | Gr 3–6 | [Chapter 4: Subtraction](sc6/04-operations-skip-counting.md) • [Chapter 9: Water & Tank Volumes](sc6/09-applied-stem-labs.md) |
| **39**| R7, C0 | `[C]` (ON) | `[f] [?]` Quiz Sprint| `[g] [OFF]` Sleep | Gr 3–6 | [Chapter 1: Wake & Sleep](sc6/01-hardware-architecture.md) • [Chapter 8: Math Quiz Game](sc6/08-math-quiz-engine.md) |
| **40**| R7, C1 | `[0]` | `[f] [REGS]` Viewer | *(Unassigned)* | Gr 3–6 | [Chapter 3: Zero & Place Value](sc6/03-counting-place-value.md) • [Chapter 2: Stack Viewer](sc6/02-rpn-for-young-learners.md) |
| **41**| R7, C2 | `[.]` | `[f] [0.3̄]` Repeat | *(Unassigned)* | Gr 3–5 | [Chapter 5: Two-Dot Fractions & Repeating Decimals](sc6/05-fractions-decimals-ratios.md) |
| **42**| R7, C3 | `[≠]` | `[f] [>]` Greater | `[g] [<]` Less | Gr 3–5 | [Chapter 4: Comparing Numbers](sc6/04-operations-skip-counting.md) |
| **43**| R7, C4 | `[+]` | `[f] [≥]` Greater/Eq | `[g] [≤]` Less/Eq | Gr 3–5 | [Chapter 4: Addition & Comparisons](sc6/04-operations-skip-counting.md) |

---

## D.3 Developmental Keycap Ribbon Architecture

The SC-6 physical keyboard supports the full elementary-to-middle school progression through progressive grade-band introduction:

| Curriculum Stage | Core Mathematical Focus | Keycaps Introduced |
| :--- | :--- | :--- |
| **Foundational Fluency** | Concrete counting, make-ten pairing, and tactile arithmetic | `[▦]` Ten-Frame, `[g] [COUNT]`, `[f] [LINE]`, `[+]`, `[-]`, `[ENTER]`, `[C]`, `[<-]` |
| **Place Value & Skip-Counting** | Multi-digit decomposition, doubles, and rhythmic counting | `[PV]` Place Value, `[g] [REP]` Stack Replicator, `[$]` Currency, `[x⇄y]` |
| **Grade 3: Arrays, Area & Fractions** | Grid arrays, time arithmetic, and unit fraction exploration | `[×]`, `[÷]`, `[f] [RECT]`, `[🕒]` Planetary Clock, `[FDISP]`, `[.]` |
| **Grade 4: Division & Fraction Mastery** | Division with remainders and step-by-step fraction reduction | `[g] [÷R]` Quotient & Remainder, `[a ᵇ/c]`, `[f] [d/c]`, `[g] [SIMP]`, `[f] [LASTX]` |
| **Grade 5: Unlike Fractions & Surface Area** | Common denominators, 3D volume, and ledger accumulation | `[GCF]`, `[f] [LCM]`, `[f] [PRISM]`, `[Σ+]` Surface Area Ledger, `[FRQ]` Tables |
| **Grade 6 & Beyond: Primes, Data & Sprints** | Negatives, primes, descriptive statistics, and rapid mental math sprints | `[+/-]`, `[ABS]`, `[PRIME]`, `[g] [FACT]`, `[g] [a:b]`, `[x²]`, `[f] [√x]`, `[IQR]`, `[g] [MAD]` |

---

## D.4 Continuing Your Mathematical Journey

Every time you place a number on Shelf $Y$ with `[ENTER]`, watch a finished answer lift automatically to Shelf $Z$, or unfold a 3D box into `[Σ+]`, you are practicing the exact way scientists, architects, and engineers think: breaking big puzzles into small, honest pieces you can see and touch. Keep your math blocks and your SC-6 within reach on your desk—and whenever you are ready for trigonometric waves, orbital mechanics, and numerical calculus, *Thinking in the Stack* (**Volume II: StackCalc SC-32**) is waiting for you.
