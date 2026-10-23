---
title: "From Blocks to the Stack: How Hands-On Blocks Make Numbers Click (SC-6)"
description: "An illustrated popular math guide and hands-on companion for Grades 3–6 (ages 8–12), connecting 3D-printed math blocks with parenthesis-free thinking on the StackCalc SC-6."
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

As education researchers and mathematicians including Jerome Bruner {{cite:bruner1966}}, Liping Ma {{cite:ma1999}}, and Steven Strogatz {{cite:strogatz2012}} have shown, an overuse of the `=` button trains learners to treat math as a magic trick that spits out answers rather than a physical balance of quantities you can see and touch. Worse yet, if a problem has two parts—like buying two notebooks and four pencils—an ordinary calculator forces you to wrap everything in parentheses `( ... )` or scribble halfway answers on scrap paper because its screen can only hold one number at a time.

### Meet the Four Shelves of Your Number Stack ($X, Y, Z, T$)

Now look closely at the bottom-right corner of your **StackCalc SC-6**. Notice anything missing?  
**There is no equals (`=`) button.**

Instead of an `=` button, there is a wide button labeled **`{{key:ENTER}}`**, and the screen above it acts like a **stack of four sturdy shelves** where your numbers stay in plain sight while you work:

- **Shelf $X$ (Your Workbench):** This is the bottom shelf (or the right side of the split `Y | X` screen). Every number you type appears right here on the Workbench, and every answer lands here too.
- **Shelf $Y$ (The Waiting Shelf):** This shelf sits right above the Workbench (or on the left side of the `Y | X` screen). Whenever you finish typing your first number and press **`{{key:ENTER}}`**, an invisible elevator lifts that number up onto Shelf $Y$ so your Workbench ($X$) is clear for the next number.
- **Shelves $Z$ and $T$ (The Upper Shelves):** Above Shelf $Y$ sit two more waiting shelves. Whenever a math puzzle has two or three separate parts, finished pieces ride safely upstairs to Shelves $Z$ and $T$ until you need them—so you never have to write intermediate numbers on scrap paper or juggle parentheses in your head.

{{blocks:sc6_elementary_hero|The StackCalc SC-6 Elementary RPN Hardware Calculator}}

### Your Very First Stack Move: Adding `7` and `5`

Pick up your SC-6 (or place seven and five counting tiles on your desk) and try your very first stack calculation:
1. **Put the first number on the Workbench:** Tap `7`. You see `7` sitting on Shelf $X$.
2. **Lift it to the Waiting Shelf:** Tap **`{{key:ENTER}}`**. That tells the calculator, *"My first number is finished—lift it up to Shelf $Y$ so I can type the next number."*
3. **Put the second number on the Workbench:** Tap `5`. Now look at your screen: `7` is waiting on Shelf $Y$, and `5` is sitting on Shelf $X$. Both numbers are right in front of your eyes at the same time.
4. **Combine them:** Tap **`{{key:+}}`**. Instantly, Shelf $Y$ drops down and fuses with Shelf $X$ to make **`12`**.

| Calculator Approach | Keystroke Sequence | What You See Happen |
|---|---|---|
| **Traditional Algebraic (Infix)** | `7` `+` `5` `=` $\longrightarrow 12$ | The `+` key hides `7` in invisible memory while waiting for `5`. The `=` key erases the problem structure, hiding where intermediate values live. |
| **Stack Math (RPN)** | `7` `{{key:ENTER}}` `5` `{{key:+}}` $\longrightarrow 12$ | `7` rises visibly to Shelf $Y$; `5` enters Shelf $X$; `{{key:+}}` combines them visibly into `12`. Every number stays in plain sight with zero parentheses. |

You didn't need an `=` button, because **pushing the two numbers together with `{{key:+}}` *is* the answer.** Mathematicians call this **Reverse Polish Notation (RPN)**—or as we call it throughout this book, **Stack Math**—and it is the exact way rocket engineers, scientists, and computers solve problems.

---

## Walking Through Your First Everyday Stack Stories

Once you know how to put a number on Shelf $Y$ with `{{key:ENTER}}` and put a second number on Shelf $X$, you can already solve real-world stories. Let's walk through a few gentle examples together. Beneath each story is a **4-Register Stack Table** that shows you what is sitting on each of the four shelves ($T, Z, Y,$ and $X$) after every button press.

### Taking Away: Finding Missing Spaces on a Ten-Frame Tray

Suppose Maya places **7 red counters** into her 10-space Ten-Frame tray, filling the top row of 5 and 2 more spaces on the bottom row. How many blue counters does she need to fill all 10 spaces?

In any subtraction story ($10 - 7$), we start with the whole amount (`10`) and take away the part we already have (`7`). On the stack, your starting number always goes onto the Waiting Shelf ($Y$) first via `10 {{key:ENTER}}`, the number you are taking away (`7`) goes onto the Workbench ($X$), and tapping `{{key:-}}` takes $X$ away from $Y$ to leave **`3`** empty spaces:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `{{key:C}}` | 0 | 0 | 0 | 0 | Clean baseline stack in `{{key:NUM}}` mode. |
| `10` | 0 | 0 | 0 | 10 | Key target capacity ($10$) into Ground Floor $X$. |
| `{{key:ENTER}}` | 0 | 0 | 10 | 10 | Target capacity lifts smoothly into Mezzanine Floor $Y$. |
| `7` | 0 | 0 | 10 | 7 | Enter red counters into Ground Floor $X$. |
| `{{key:-}}` | 0 | 0 | 0 | 3 | Subtraction combines $Y - X = 3$. Result in $X$. |

*What if your screen says `17` instead of `3`?* That just means your thumb tapped `{{key:+}}` instead of `{{key:-}}`! And what if you accidentally typed `7 {{key:ENTER}} 10` in the wrong order? You don't have to erase and start over: tapping the **`{{key:x⇄y}}` (Swap)** key trades the numbers on Shelf $Y$ and Shelf $X$ so `10` is back on top and `7` is on the bottom!

### Checking Your Own Work in One Tap (`{{key:LASTX}}`)

Every teacher and parent says, *"Always check your work!"* On a regular calculator, checking an addition problem by subtracting is annoying because you have to type the numbers all over again.

On the SC-6, every time an operation combines two numbers, the calculator automatically tucks a backup copy of the number from Shelf $X$ into a special memory pocket called **`LAST x`**. Suppose you are counting trading cards: you have **24 cards** in your binder and **15 cards** in a tin box. You add `24 {{key:ENTER}} 15 {{key:+}}` to get **`39`**. How can you prove that `39` is right without typing `15` again?

Just tap **`{{key:LASTX}}`**! Your `15` jumps right back onto Shelf $X$ while `39` automatically lifts up to Shelf $Y$. Now tap **`{{key:-}}`**, and `39 - 15` lands right back on your starting number, **`24`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `24 {{key:ENTER}}` | 0 | 0 | 24 | 24 | First number committed to Mezzanine Floor $Y$. |
| `15 {{key:+}}` | 0 | 0 | 0 | 39 | Addition completed; `LAST x` preserves $15$ in hardware. |
| `{{key:LASTX}}` | 0 | 0 | 39 | 15 | Prior number ($15$) recalled into $X$; sum lifts to $Y$. |
| `{{key:-}}` | 0 | 0 | 0 | 24 | Inverse check: $39 - 15 = 24$. Starting number verified. |

(And if you ever add $47 + 36$ via `47 {{key:ENTER}} 36 {{key:+}}` $\implies \mathbf{83}$, tapping `{{key:LASTX}} {{key:-}}` checks $83 - 36 = \mathbf{47}$ in two taps!)

### Sharing with Whole Groups and Leftovers (`{{key:÷R}}`)

What happens when numbers don't divide evenly? Suppose you divide $17 \div 5$ on an ordinary calculator, and the screen says `3.4`. What does `0.4` mean when you are sharing 17 counting tiles among 5 friends? In real life, you cannot hand a friend `0.4` of a tile—each friend gets **3 whole tiles**, and there are **2 tiles left over**.

On your SC-6, the **`{{key:÷R}}` (*Quotient & Remainder*)** key solves both parts of a sharing story at once. Imagine a group of **125 students and chaperones** heading to the science museum in vans that hold **8 passengers each**. When we put `125` on Shelf $Y$ (`125 {{key:ENTER}}`), put `8` on Shelf $X$, and tap **`{{key:÷R}}`**, **Shelf $X$** shows **`15`** completely full vans, and **Shelf $Y$** holds the **`5`** leftover passengers who need one more van (so the school needs $15 + 1 = 16$ vans in all!):

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `125` | 0 | 0 | 0 | 125 | Total passengers entered into Ground Floor $X$. |
| `{{key:ENTER}}` | 0 | 0 | 125 | 125 | 125 committed and copied to Mezzanine Floor $Y$. |
| `8` | 0 | 0 | 125 | 8 | Capacity per van keyed into $X$. |
| `{{key:÷R}}` | 0 | 0 | 5 | 15 | Integer division with remainder: $X = 15$ full vans, $Y = 5$ leftover passengers. |

---

## How the Upper Shelves Beat Parentheses on Two-Part Puzzles

Now that you have seen how Shelf $X$ and Shelf $Y$ work together on one-step stories, what happens when a math puzzle has **two or three steps**?

Suppose you are measuring your backyard to build a square brick patio. Your yard is **$12\text{ feet}$ wide**, and you leave a **$3\text{-foot}$ grass path** along one side ($12 - 3 = 9\text{ feet}$ on each side of the square patio). You want to find both the patio's **Area** in square bricks ($9 \times 9$) and the **Perimeter** of wooden edging around its 4 sides ($9 \times 4$).

Watch how smooth this is on the stack:
1. First subtract the grass path: `12 {{key:ENTER}} 3 {{key:-}}` puts **`9`** on Shelf $X$.
2. Tap the **`{{key:x²}}` (Square)** key to multiply $9 \times 9 = \mathbf{81\text{ sq ft}}$ of bricks on Shelf $X$.
3. Now tap **`{{key:LASTX}}`** to bring the $9\text{-foot}$ side length right back onto Shelf $X$ (which automatically lifts `81` onto Shelf $Y$!), and multiply by `4` (`4 {{key:×}}`) to see **`36` feet** of border edging on Shelf $X$ right beside **`81` square feet** of bricks on Shelf $Y$:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `12 {{key:ENTER}} 3 {{key:-}}` | 0 | 0 | 0 | 9 | Yard width minus grass path: $12 - 3 = 9\text{ ft}$ patio side. |
| `{{key:x²}}` | 0 | 0 | 0 | 81 | Square side length: $9 \times 9 = 81\text{ sq ft}$ patio area (`LAST x` saves 9). |
| `{{key:LASTX}}` | 0 | 0 | 81 | 9 | Recall side length $9\text{ ft}$ into $X$; area $81$ lifts to $Y$. |
| `4 {{key:×}}` | 0 | 0 | 81 | 36 | Multiply side by 4: $9 \times 4 = 36\text{ ft}$ border perimeter ($Y$ still shows $81\text{ sq ft}$ area). |

Notice what happened when `9` returned to Shelf $X$: you didn't have to press `{{key:ENTER}}` before typing `4`! Why? Because **whenever a finished answer is sitting on Shelf $X$, typing a new number *automatically* lifts that finished answer up to the next shelf** to wait for you.

That **automatic stack lift** is why you never need parentheses `( )` on the SC-6. Suppose someone challenges you to solve this two-group puzzle:
$$(15 - 3) \times (4 + 2) \div 6$$

On a regular phone or school calculator, you have to hunt for `(` and `)` brackets and type the entire string before seeing a single intermediate number. On your SC-6 stack, you simply build one small group at a time:
1. **Build the first group (`15 - 3`):** Tap `15` `{{key:ENTER}}` `3` `{{key:-}}`. The screen immediately shows **`12`** on Shelf $X$.
2. **Build the second group (`4 + 2`):** Now just type `4` `{{key:ENTER}}` `2` `{{key:+}}`. The moment you type `4`, automatic stack lift carries your finished `12` upstairs to wait safely on Shelf $Z$ and drop back to Shelf $Y$, while `4` and `2` add together into **`6`** on Shelf $X$.
3. **Multiply the two groups and divide by `6`:** Now `12` is waiting on Shelf $Y$ and `6` is sitting on Shelf $X$. Tap **`{{key:×}}`** to multiply them into **`72`**, and then tap `6` **`{{key:÷}}`** to divide by 6:
   `{{res:sc6_order_of_ops:keys}}` $\longrightarrow$ **`{{res:sc6_order_of_ops:value}}`**.

You can use that exact same rhythm on any two-group challenge, like $((18 + 6) \times (15 - 7)) \div 8$: build $18 + 6 = 24$, build $15 - 7 = 8$ (while `24` waits upstairs), multiply them into $192$, and divide by $8$:
`{{res:sc6_index_influencer_race:keys}}` $\longrightarrow$ **`{{res:sc6_index_influencer_race:value}}`**.

---

## More Helper Keys & Visual Sandboxes Waiting for You

As you travel through the chapters ahead, you will meet several more helper keys that turn tricky topics into hands-on discoveries:

| Signature Key | How It Helps You |
| :--- | :--- |
| **Constant Repeat (`{{key:REP}}`)** | **Skip-Counting & Times Tables:** Copies your number across all four shelves ($X = 7, Y = 7, Z = 7, T = 7$) so repeated taps of `{{key:+}}` climb times tables (`7, 14, 21, 28...`) or repeated taps of `{{key:×}}` double `2` twenty times past **one million (`1,048,576`)**! |
| **Quotient & Remainder (`{{key:÷R}}`)** | **Whole Groups & Leftovers Together:** Divides in one tap, putting the whole groups (Quotient) on Shelf $X$ and the exact leftovers (Remainder) on Shelf $Y$. |
| **Step-by-Step Simplify (`{{key:SIMP}}`)** | **Fraction Reduction You Control:** Keeps fractions like `. 12 . 18` unreduced until *you* press `{{key:SIMP}}` to divide out shared factors into `2/3`, flashing `LOWEST TERMS` when fully simplified. |
| **Add to Total (`{{key:Σ+}}`)** | **A Shopping Basket for Totals:** Lets you toss finished numbers into a running basket (`1`, `2`, `3` items) and tap `{{key:Σx}}` to see the grand total without writing anything on scrap paper. |

Look at how handy that **`{{key:Σ+}}` (*Add to Total*)** basket is when you reach geometry in Chapter 6. Imagine painting all 6 flat wooden walls of a rectangular treasure box that is **$5\text{ cm}$ long, $4\text{ cm}$ wide, and $3\text{ cm}$ high**—made of two $5 \times 4$ walls ($40\text{ cm}^2$), two $5 \times 3$ walls ($30\text{ cm}^2$), and two $4 \times 3$ walls ($24\text{ cm}^2$). Instead of jotting `40`, `30`, and `24` on paper, you clear the basket with `{{key:CLΣ}}`, toss each pair of walls into the basket with `{{key:Σ+}}`, and tap **`{{key:Σx}}`** to reveal all **`94.0` $\text{cm}^2$**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `{{key:CLΣ}}` | 0 | 0 | 0 | 0 | Clear the running total before adding face pairs. |
| `5 {{key:ENTER}} 4 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | 0 | 0 | 0 | 1 | Face Pair 1 ($40\text{ cm}^2$) added to total; Register $X$ shows `1` pair added. |
| `5 {{key:ENTER}} 3 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | 0 | 0 | 0 | 2 | Face Pair 2 ($30\text{ cm}^2$) added to total; Register $X$ shows `2` pairs added. |
| `4 {{key:ENTER}} 3 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | 0 | 0 | 0 | 3 | Face Pair 3 ($24\text{ cm}^2$) added to total; Register $X$ shows `3` pairs added. |
| `{{key:Σx}}` | 0 | 0 | 0 | $94.0$ | Recall the Grand Total of All Pairs: $94\text{ cm}^2$ without scratch paper. |

### Build with Your Hands, See on the Screen, Combine on the Stack

Inspired by the cutaway mechanical illustrations of David Macaulay {{cite:macaulay2016}} and Jerome Bruner's discovery that we understand math best when we move from **hands-on objects** to **visual pictures** to **numbers** {{cite:bruner1966}}, every chapter in this book connects three layers at your desk:

| Learning Phase | What You Use | How It Works at Your Desk |
|---|---|---|
| **1. Hands-On Blocks** | 3D-Printed Manipulative Kits | You build the problem with physical Ten-Frame Trays, $84\text{ mm}$ Fraction Towers, Four-Color Counting Tiles, Prime Factor Blocks, and a Planetary Geared Clock (which you will meet in Chapter 1). |
| **2. Visual Screen Modes** | Daylight Paper-Like Visual Modes | You see the exact same model drawn on the SC-6 screen using Ten-Frame Mode `{{key:▦}}`, the Number Rack `{{key:COUNT}}`, Number Line Jump Arcs `{{key:LINE}}`, Place Value `{{key:PV}}`, the Geared Clock Dial `{{key:🕒}}`, Polyhedral Dice `{{key:🎲}}`, or the 6-Level Math Quiz Game `{{key:?}}`. |
| **3. The Number Stack** | Four-Shelf RPN Stack ($X, Y, Z, T$) | You combine your numbers on the four visible stack shelves—solving multi-step puzzles, remainder division, and 3D surface area without parentheses or scratch paper. |

Whenever you are inside one of the visual screen modes (`{{key:▦}}`, `{{key:COUNT}}`, `{{key:LINE}}`, `{{key:🕒}}`, `{{key:🎲}}`) and want to switch back to regular numbers, just tap **`{{key:C}}` (Clear)** once when you aren't typing digits. Switching between visual pictures and regular numbers never erases your stack—it simply changes the lens through which you look at the numbers on your shelves!

{{res:sc6_hero_calculator:screenshot|StackCalc SC-6 Elementary Calculator Faceplate & 43-Key Topography}}
*Figure 0.1: The StackCalc SC-6 Elementary RPN Calculator faceplate, featuring 19 oversized tactile switches with sculpted TPU keypads, a double-wide `{{key:ENTER}}` key, and `{{key:f}}` and `{{key:g}}` shift legends.*

### Three Helpful Stack Habits as You Start

1. **`{{key:ENTER}}` Keeps Your Number; `{{key:C}}` Clears It:** The big **`{{key:ENTER}}`** button is the elevator door that locks your number in and lifts it up to Shelf $Y$. The **`{{key:C}}`** button is the eraser that clears Shelf $X$ back to `0`.
2. **Typed Two Numbers Backward for Subtraction or Division? Just Tap `{{key:x⇄y}}`:** If you ever type `8 {{key:ENTER}} 15` when you meant $15 - 8$, don't erase! Just tap **`{{key:x⇄y}}`** to swap their shelves (`15` in $Y$, `8` in $X$), and press `{{key:-}}`.
3. **Entering Clock Time (`2.30` Means 2 Hours 30 Minutes):** When you use the Geared Clock (`{{key:🕒}}`) in Chapter 6, type `2` hours and `30` minutes just like a digital wall clock as **`2.30`** (and if you have `2.5` decimal hours, tapping `{{key:▸HMS}}` converts `2.5` into `2:30:00` automatically).

| Everyday Math Problem | Standard Calculator (Infix) | StackCalc SC-6 (RPN) | Why the Stack Feels Easier |
| :--- | :--- | :--- | :--- |
| **1. Checking Addition** $(47 + 36) - 36 = 47$ | `47 + 36 = - 36 =` (9 strokes; re-types 36) | `47` `{{key:ENTER}}` `36` `{{key:+}}` `{{key:LASTX}}` `{{key:-}}` (6 strokes) | **`{{key:LASTX}}` remembers `36`** so you never re-type it. |
| **2. Two-Part Puzzle** $(15 - 3) \times (4 + 2) \div 6$ | `( 15 - 3 ) × ( 4 + 2 ) ÷ 6 =` (18 strokes) | `{{res:sc6_order_of_ops:keys}}` $\to$ **`{{res:sc6_order_of_ops:value}}`** (11 strokes) | **Zero parentheses**; you see `12` and `6` before multiplying. |
| **3. Sharing with Leftovers** $125 \div 8 = 15\text{ R }5$ | `125 ÷ 8 =` (`15.625`), then multiply & subtract on paper | `125` `{{key:ENTER}}` `8` `{{key:÷R}}` $\to$ `15` ($X$) & `5` ($Y$) (5 strokes) | **Shows `15` vans and `5` leftover riders** at the same time. |
| **4. Adding Fractions** $\frac{3}{8} + \frac{5}{12} = \frac{19}{24}$ | `( 3 ÷ 8 ) + ( 5 ÷ 12 ) =` (gives decimal `0.79167`) | `. 3 . 8` `{{key:ENTER}}` `. 5 . 12` `{{key:+}}` $\to$ **`19/24`** (8 strokes) | **Keeps exact fractions** that match your Fraction Towers. |
| **5. Box Surface Area** ($5 \times 4 \times 3$ box) | `2 × 5 × 4 + 2 × 5 × 3 + 2 × 4 × 3 =` | Toss each wall pair into `{{key:Σ+}}`, then tap `{{key:Σx}}` $\to$ **`94`** | **Zero scrap paper**; the basket counts `1, 2, 3` wall pairs. |

---

## How to Navigate This Book & Topic Finder

This book is organized into nine hands-on chapters and four reference appendices. You can read it straight through from Chapter 1 to Chapter 9 as a story of mathematical discovery, or jump directly to the topic you are exploring today (and for **25 additional Quick-Start Warm-Up Adventures**, open the companion **[SC-6 Elementary Companion Problem & Activity Workbook](../../curriculum/sc6-elementary-companion-workbook.md)**):

- **Building Your Stack & Whole-Number Foundations ([Chapters 01](01-hardware-architecture.md)–[04](04-operations-skip-counting.md)):** Set up your desk studio and meet your 3D-printed math blocks in [Chapter 01](01-hardware-architecture.md), ride the full 4-story Number Elevator in [Chapter 02](02-rpn-for-young-learners.md), explore ten-frames, number lines, and place value up to billions in [Chapter 03](03-counting-place-value.md), and build multiplication tile arrays, skip-counting ladders (`{{key:REP}}`), and remainder division (`{{key:÷R}}`) in [Chapter 04](04-operations-skip-counting.md).
- **Fractions, Geometry, Primes & Data ([Chapters 05](05-fractions-decimals-ratios.md)–[07](07-data-probability-primes.md)):** Master equivalent fractions, common denominators, decimals, and ratios with the $84\text{ mm}$ Fraction Towers in [Chapter 05](05-fractions-decimals-ratios.md); unfold 2D shapes, 3D surface area (`{{key:Σ+}}`), volumes, and planetary clock gears in [Chapter 06](06-geometry-surface-area.md); and explore prime factor towers (`{{key:FACT}}`), dice probability (`{{key:🎲}}`), fair-share statistics (`{{key:x̄}}`, `{{key:MAD}}`), and negative numbers in [Chapter 07](07-data-probability-primes.md).
- **Mental Math Sprints & Maker STEM Labs ([Chapters 08](08-math-quiz-engine.md)–[09](09-applied-stem-labs.md)):** Discover 8 mental-math shortcuts and play 6 levels of arithmetic sprints (`{{key:?}}`) in [Chapter 08](08-math-quiz-engine.md), then use your stack to weigh 3D-printed parts, slice layers, time pendulums, scale recipes, and test gear trains in [Chapter 09](09-applied-stem-labs.md).
- **3D-Printable Studios, Lesson Plans & Reference Guides ([Appendices A](appendix-a-manipulative-blueprints.md)–[D](appendix-d-keycap-directory.md)):** Find the 3D-printing guide in [Appendix A](appendix-a-manipulative-blueprints.md), 25 classroom station lesson plans in [Appendix B](appendix-b-teacher-lesson-plans.md), word rules and unit conversions in [Appendix C](appendix-c-formulas-and-conversions.md), and the 43-button directory in [Appendix D](appendix-d-keycap-directory.md).

### Chapter-by-Chapter Guide

| Chapter / Appendix | Core Mathematical Focus & Story Arc | Physical Manipulative Studio | Primary SC-6 Keycaps | Hands-On Explorations |
| :--- | :--- | :--- | :--- | :--- |
| **[Chapter 01](01-hardware-architecture.md)** | Setting up your desk studio, first block-and-stack discoveries, daylight screen & button feel | All 8 Companion Studios & Quest Scoreboard | `{{key:ENTER}}`, `{{key:+}}`, `{{key:×}}`, `{{key:C}}`, `{{key:<-}}`, `{{key:f}}`, `{{key:g}}` | Measuring screen pixels, snap-domes, Gridfinity trays & battery life |
| **[Chapter 02](02-rpn-for-young-learners.md)** | Riding the 4-shelf RPN stack ($X, Y, Z, T$) & solving multi-step order of operations without parentheses | Stack Shelves & Counting Tiles | `{{key:ENTER}}`, `{{key:+}}`, `{{key:-}}`, `{{key:x⇄y}}`, `{{key:R↓}}`, `{{key:CSTK}}` | Playground construction, sky-tower lifts, farmers' market & museum vaults |
| **[Chapter 03](03-counting-place-value.md)** | Subitizing, make-ten bridging, multi-digit place value (`1000 \| 100 \| 10 \| 1`), rounding & negative number-line hops | Ten-Frame Studio, Number Rack & Place Value Trays | `{{key:▦}}`, `{{key:COUNT}}`, `{{key:LINE}}`, `{{key:PV}}`, `{{key:$}}` | Ten-frame bridging, place-value bundling, submarine dives & book-fair budgets |
| **[Chapter 04](04-operations-skip-counting.md)** | Rectangular multiplication arrays, rhythmic skip-counting ladders, powers & fair-share division with remainders | 24-Tile Counting & Array Studio | `{{key:×}}`, `{{key:÷}}`, `{{key:REP}}`, `{{key:÷R}}`, `{{key:MOD}}`, `{{key:LASTX}}` | Tile arrays, doubling legends, bus remainders & multi-step camp logistics |
| **[Chapter 05](05-fractions-decimals-ratios.md)** | Equivalent fractions, step-by-step factor reduction, common denominators, mixed numbers, decimals, percents & ratios | 84 mm Fraction Tower Studio & Decimal Tray | `{{key:a ᵇ/c}}`, `{{key:d/c}}`, `{{key:SIMP}}`, `{{key:FDISP}}`, `{{key:%}}`, `{{key:%CHG}}` | Fraction tower alignment, carpentry cuts, recipe scaling & store discounts |
| **[Chapter 06](06-geometry-surface-area.md)** | 2D area/perimeter, Pythagorean theorem, 3D prism/cylinder/cone volume, surface area via `{{key:Σ+}}` & modulo-60 clock time | Counting Tiles, L-Frame, Volvelle & Geared Clock | `{{key:RECT}}`, `{{key:CIRC}}`, `{{key:PRISM}}`, `{{key:Σ+}}`, `{{key:🕒}}`, `{{key:▸HR}}` | Penguin huddles, garden borders, gift-box wrapping, silos & train timetables |
| **[Chapter 07](07-data-probability-primes.md)** | Prime factor trees, GCF & LCM, polyhedral dice probability, dot plots, mean/median/IQR/MAD & signed integers | Prime Factor Studio, Polyhedral Dice & Two-Color Counters | `{{key:PRIME}}`, `{{key:FACT}}`, `{{key:GCF}}`, `{{key:LCM}}`, `{{key:🎲}}`, `{{key:x̄}}`, `{{key:MED}}`, `{{key:+/-}}` | 17-year cicadas, gear teeth, dice trials, weather data & ocean trenches |
| **[Chapter 08](08-math-quiz-engine.md)** | Mental math shortcuts (Vedic squares, 11s trick, Gauss sums) & 6-level timed fluency sprints | Math Dominoes & Quest Scoreboard | `{{key:?}}` (`{{key:f}}` + `{{key:C}}`), `{{key:LASTX}}`, Classroom Seeds | Mental-math patterns & 6-level astronaut flight-simulator sprints |
| **[Chapter 09](09-applied-stem-labs.md)** | 3D-printed block weights and layer slicing, bean sprout growth, recipe scaling, gear ratios, and solar ovens | All Studios + Calipers, Scale & Stopwatches | `{{key:π}}`, `{{key:x²}}`, `{{key:√x}}`, `{{key:▸g}}`, `{{key:▸cm}}`, `{{key:▸°C}}` | 3D printer slicing, pendulum clocks, botanical growth & maker workshops |
| **[Appendices A–D](appendix-a-manipulative-blueprints.md)** | CAD/3D-print blueprints ([App. A](appendix-a-manipulative-blueprints.md)), 25 station lesson plans ([App. B](appendix-b-teacher-lesson-plans.md)), formulas & primes ([App. C](appendix-c-formulas-and-conversions.md)), and 43-key matrix ([App. D](appendix-d-keycap-directory.md)) | Full Manipulative & Curriculum Reference Suite | Complete 43-Key Hardware Matrix | Turnkey Classroom & Home Reference |

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

## Turning the Page: Let's Open Your Desk Studio

Whether you are a young builder opening your calculator and block trays for the very first time, a parent exploring evening kitchen-table puzzles, or a teacher setting up a hands-on math station, every chapter ahead begins with something you can touch, see, and build before a single button is pressed.

Turn the page to **[Chapter 1: Meet Your SC-6 Stack Calculator & Math Blocks](01-hardware-architecture.md)**, where we will snap our first base-ten blocks together, wake up the sunlit screen, and discover how the four-story number elevator turns everyday math into an adventure.
