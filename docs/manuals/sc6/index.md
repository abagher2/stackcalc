---
title: "StackCalc SC-6 Elementary Calculator Manual & Classroom Companion"
description: "The complete student handbook, user guide, and classroom companion for the StackCalc SC-6 Elementary RPN Calculator."
---

# From Blocks to the Stack: Hands-On Math & the SC-6 Stack Calculator

## Welcome, Explorer! Why Your Brain Already Thinks in a Stack

If an adult handed you this book and said, *"Here, read this math manual,"* you probably wanted to groan and hide it under your bed. Most school math books feel like an obstacle course: pages of repetitive drills, mysterious rules like *"borrow from the neighbor,"* and giant tangles of parentheses like `((15 - 3) × (4 + 2)) ÷ 6 = ?` where one tiny slip ruins your whole page.

**Here is the good news: this is not a normal school math book, and the calculator in your hands is not a normal calculator.**

Before you press a single button, think about how you build things with your hands in everyday life. Suppose you have **7 red LEGO bricks** on your desk, and your friend hands you **5 gold bricks**. How do you find out how many bricks you have altogether?

You don't wave a magic wand in the air and shout, *"Open parenthesis! Seven! Plus! Five! Close parenthesis! Equals!"*  
Instead, you do three simple things with your hands:
1. You place the **first pile (`7`)** on your desk.
2. You place the **second pile (`5`)** right beside it.
3. You **push the two piles together** into **`12`**.

Every time you stack pancakes on a plate, pack books into your backpack, or build a tower out of blocks, your hands follow that exact rhythm: **first put the pieces on the table, then do something with them.**

In mathematics and computer science, that everyday workspace has a special name: **a Stack**.

### Meet the Four Shelves of Your Number Stack ($X, Y, Z, T$)

Look closely at the bottom-right corner of your **StackCalc SC-6**. Notice anything missing?  
**There is no equals (`=`) button.**

Instead of an `=` button, there is a wide button labeled **`{{key:ENTER}}`**, and the screen above it acts like a **stack of four sturdy shelves** where your numbers live in plain sight:

- **Shelf $X$ (Your Workbench):** This is the bottom shelf (or the right side of the split `Y | X` screen). Every number you type appears right here on the Workbench, and every answer lands here too.
- **Shelf $Y$ (The Waiting Shelf):** This shelf sits right above the Workbench (or on the left side of the `Y | X` screen). Whenever you finish typing your first number and press **`{{key:ENTER}}`**, an invisible elevator lifts that number up onto Shelf $Y$ so your Workbench ($X$) is clear for the next number.
- **Shelves $Z$ and $T$ (The Upper Shelves):** Above Shelf $Y$ sit two more waiting shelves. Whenever a math puzzle has two or three separate parts, finished pieces ride safely upstairs to Shelves $Z$ and $T$ until you need them—so you never have to write intermediate numbers on scrap paper or juggle parentheses in your head.

### Your Very First Stack Move: Adding `7` and `5`

Pick up your SC-6 (or place seven and five counting tiles on your desk) and try your very first stack calculation:
1. **Put the first number on the Workbench:** Tap `7`. You see `7` sitting on Shelf $X$.
2. **Lift it to the Waiting Shelf:** Tap **`{{key:ENTER}}`**. That tells the calculator, *"My first number is finished—lift it up to Shelf $Y$ so I can type the next number."*
3. **Put the second number on the Workbench:** Tap `5`. Now look at your screen: `7` is waiting on Shelf $Y$, and `5` is sitting on Shelf $X$. Both numbers are right in front of your eyes at the same time.
4. **Combine them:** Tap **`{{key:+}}`**. Instantly, Shelf $Y$ drops down and fuses with Shelf $X$ to make **`12`**.

You didn't need an `=` button, because **pushing the two numbers together with `{{key:+}}` *is* the answer.** Mathematicians call this **Reverse Polish Notation (RPN)**—or as we call it throughout this book, **Stack Math**—and it is the exact way rocket engineers, scientists, and computers solve problems.

{{blocks:sc6_elementary_hero|The StackCalc SC-6 Elementary RPN Hardware Calculator}}

### Why the Stack Beats Parentheses Every Time

Now watch what happens when a problem has more than one step. Suppose someone challenges you to solve this 5th-grade puzzle:
$$(15 - 3) \times (4 + 2) \div 6$$

On a regular phone or school calculator, you have to hunt for `(` and `)` brackets and type the entire string before you are allowed to see a single intermediate number. On your SC-6 stack, you simply solve one small piece at a time—just like building two small block towers and then combining them:

1. **Build the first group (`15 - 3`):** Tap `15` `{{key:ENTER}}` `3` `{{key:-}}`. The screen immediately shows **`12`** on Shelf $X$. You already know the first group is `12`!
2. **Build the second group (`4 + 2`):** Now just type `4` `{{key:ENTER}}` `2` `{{key:+}}`. The moment you type `4`, the calculator *automatically* lifts your `12` upstairs to wait for you while `4` and `2` add together into **`6`** on Shelf $X$.
3. **Multiply the two groups and divide by `6`:** Now `12` is sitting on Shelf $Y$ and `6` is sitting on Shelf $X$. Tap **`{{key:×}}`** to multiply them into **`72`**, and then tap `6` **`{{key:÷}}`** to divide by 6:
   `{{res:sc6_order_of_ops:keys}}` $\longrightarrow$ **`{{res:sc6_order_of_ops:value}}`**.

Zero parentheses. Zero `SYNTAX ERROR` alarms. Every single step happened right before your eyes. Look at the same idea on another multi-step puzzle, $((18 + 6) \times (15 - 7)) \div 8$: you build $18 + 6 = 24$, then $15 - 7 = 8$, multiply them into $192$, and divide by $8$ in one smooth flow:
`{{res:sc6_index_influencer_race:keys}}` $\longrightarrow$ **`{{res:sc6_index_influencer_race:value}}`**.

---

## Why Hands-On Blocks and a Visible Stack Belong Together

When you type `7 + 5 =` on an ordinary pocket calculator or tablet app, the input numbers vanish and `12` appears in their place. As education researchers and mathematicians including Jerome Bruner {{cite:bruner1966}}, Liping Ma {{cite:ma1999}}, and Steven Strogatz {{cite:strogatz2012}} have shown, an overuse of the `=` button trains learners to treat math as a black box that spits out answers rather than a physical balance of quantities you can see and touch.

Inspired by the cutaway mechanical illustrations of David Macaulay {{cite:macaulay2016}}, the **StackCalc SC-6** pairs its visible four-shelf number stack ($X, Y, Z, T$) with physical, 3D-printed math blocks on your desk:

| Calculator Approach | Keystroke Sequence | What You See Happen |
|---|---|---|
| **Traditional Algebraic (Infix)** | `7` `+` `5` `=` $\longrightarrow 12$ | The `+` key hides `7` in invisible memory while waiting for `5`. The `=` key erases the problem structure, hiding where intermediate values live. |
| **Stack Math (RPN)** | `7` `{{key:ENTER}}` `5` `{{key:+}}` $\longrightarrow 12$ | `7` rises visibly to Shelf $Y$; `5` enters Shelf $X$; `{{key:+}}` combines them visibly into `12`. Every number stays in plain sight with zero parentheses. |

### Build with Your Hands, See on the Screen, Combine on the Stack

Following Jerome Bruner's insight that we understand math best when we move from **hands-on objects** to **visual pictures** to **numbers** {{cite:bruner1966}}, every chapter in this book connects three layers at your desk:

| Learning Phase | What You Use | How It Works at Your Desk |
|---|---|---|
| **1. Hands-On Blocks** | 3D-Printed Manipulative Kits | You build the problem with physical Ten-Frame Trays, $84\text{ mm}$ Fraction Towers, Four-Color Counting Tiles, Prime Factor Blocks, and a Planetary Geared Clock. |
| **2. Visual Screen Modes** | Daylight Paper-Like Visual Modes | You see the exact same model on the SC-6 screen using Ten-Frame Mode `{{key:▦}}`, the Number Rack `{{key:COUNT}}`, Number Line Jump Arcs `{{key:LINE}}`, Place Value `{{key:PV}}`, or the Geared Clock Dial `{{key:🕒}}`. |
| **3. The Number Stack** | Four-Shelf RPN Stack ($X, Y, Z, T$) | You combine your numbers on the four visible stack shelves—solving multi-step puzzles, remainder division, and 3D surface area without parentheses or scratch paper. |

Here are three five-minute lightbulb moments you will experience as you work with the blocks and the stack together:
- **The "Make-a-Ten" Snap:** Place 8 red counters and 2 gold counters into the Ten-Frame tray to fill a complete `10`, leave 3 gold counters beside it (`13`), and see the exact same ten-frame on the SC-6 screen via `{{key:▦}}`—turning $8 + 5$ into $10 + 3 = 13$ at a glance.
- **The Bus Remainder Insight:** When 145 campers board 45-seat buses, a regular calculator says `3.2222222` buses—which doesn't tell you how many campers are standing at the curb! On the SC-6, tapping `145 {{key:ENTER}} 45 {{key:÷R}}` shows **`3` full buses** on Shelf $X$ and **`10` leftover campers** waiting on Shelf $Y$.
- **The Fraction Tower Match:** Drop a $\frac{1}{2}$ block and a $\frac{1}{3}$ block into the Fraction Studio comparator well, slide five $\frac{1}{6}$ blocks beside them until their tops sit completely flush with your fingertip, and see why $\frac{1}{2} + \frac{1}{3} = \frac{5}{6}$ before checking it on the stack.

---

## Meet Your Math Blocks: Building Numbers with Your Hands

Your physical 3D-printed math block sets are molded in bright, durable colors that map directly onto the calculator's screen modes and stack shelves:

| Studio Kit | Physical Manipulative Object | SC-6 Visual Mode / Key | How the Blocks Connect to the Stack |
| :--- | :--- | :---: | :--- |
| **1. The Ten-Frame Tray** | Dual $2 \times 5$ compartmentalized trays with 20 two-color (coral/gold) counters | `{{key:▦}}` Ten-Frame Mode | Shelf $Y$ shows the upper ten-frame; Shelf $X$ shows the lower ten-frame. Tapping `{{key:+}}` combines counters, grouping them into one full ten and extras ($7 + 5 = 12$) right on the stack. |
| **2. The Four-Color Tile Studio** | 24 smooth-docking counting & array tiles in four colors (white, blue, gold, slate) | `{{key:NUM}}` Standard Mode | Build rectangular tile arrays up to $4 \times 6 = 24$ (and scale larger arrays on the stack). Row count sits on Shelf $Y$, column count sits on Shelf $X$; tapping `{{key:×}}` calculates total tiles in $X$. Spin the tray sideways: it is still 24—proving that switching the order doesn't change the answer. |
| **3. The 84 mm Fraction Towers** | $84.0\text{ mm}$ master tower ($1\text{ Whole}$) with proportional sub-towers ($1/2, 1/3, 1/4, 1/6, 1/12$) & comparator well | `{{key:FDISP}}` & `{{key:SIMP}}` | Snap two $1/4$ towers together and feel with your finger how their top edge matches the $1/2$ tower. On the SC-6, enter `. 2 . 4`, tap `{{key:SIMP}}`, and watch the numbers reduce to $1/2$ while the towers stay locked flush in the tray. |
| **4. The Prime Factor Studio** | 29 proportional prime factor blocks ($2, 3, 5, 7, \dots$) with proportional heights & number scale | `{{key:PRIME}}` & `{{key:FACT}}` | Puzzle blocks for prime numbers ($2, 3, 5, 7, \dots$). Stacking block 2 on block 3 reaches the exact height of 6. On the SC-6, type `60` and tap `{{key:FACT}}` to reveal its prime building blocks: $2^2 \times 3 \times 5$. |
| **5. The Planetary Geared Clock** | Functional 3D-printed clock with 12:1 compound planetary reduction gears and linked hands | `{{key:🕒}}` Clock Sandbox | Turn the minute hand and watch the hour hand glide automatically. On the SC-6, enter start time in $Y$ (`9.30`) and minutes in $X$ (`2.45`), then tap `{{key:+}}` to calculate arrival time across 60-minute boundaries. |
| **6. The Polyhedral Dice & Spinner Studio** | Precision polyhedral dice ($d4, d6, d8, d10, d12, d20$) with equal-volume excavated pips & balanced spinner | `{{key:🎲}}` Dice Sandbox | Roll physical dice on your desk, then tap `{{key:🎲}}` to roll digital dice into Shelf $X$, saving prior rolls in $Y, Z, T$ to build live dot plots and frequency tables. |
| **7. The Place Value Studio** | $4 \times 2$ Whole (`1000 \| 100 \| 10 \| 1`) & Decimal (`1 • 0.1 \| 0.01 \| 0.001`) trays with 44 digit miniblocks (`0`–`9`) & 9 `+1` regrouping blocks | `{{key:PV}}` Place Value Mode | Dock digit miniblocks and stack `+1` regrouping blocks across columns. Type `347` and tap `{{key:PV}}` to split the number across the stack shelves: $300 + 40 + 7$ with matching place-value column counts. |
| **8. The Number Rack (Rekenrek)** | Dual horizontal stainless rails with 10 beads each ($5\text{ red} + 5\text{ white}$) | `{{key:COUNT}}` Number Rack Mode | Top rail links to Shelf $Y$, bottom rail links to Shelf $X$. Slide beads with your fingers to see friend numbers that make 5 and 10 at a glance before doing arithmetic on the keys. |
| **9. The Quest Scoreboard** | Two-piece desktop pegboard with stackable `+10` and `+100` tokens | `{{key:?}}` & `{{key:NUM}}` | Tracks two-way problem solving across the companion workbooks: place one `+10` token when you solve a problem with blocks or paper, and stack a second `+10` token when you verify the calculation on the SC-6. |

---

## Four Helper Keys That Make Tricky Math Topics Click

Once you understand how numbers sit on Shelf $X$ and Shelf $Y$, four special keys on the SC-6 turn the trickiest topics in elementary and middle-school math—times tables, remainders, simplifying fractions, and checking your work—into physical steps you can see right on the screen:

| Signature Key | How It Helps You |
| :--- | :--- |
| **Constant Repeat (`{{key:REP}}`)** | **Skip-Counting & Times Tables:** Copies your number across all four shelves so repeated taps of `{{key:+}}` climb times tables (`7, 14, 21, 28...`) or repeated taps of `{{key:×}}` double a number into the millions. |
| **Quotient & Remainder (`{{key:÷R}}`)** | **Whole Groups & Leftovers Together:** Divides in one tap, putting the whole groups (Quotient) on Shelf $X$ and the exact leftovers (Remainder) on Shelf $Y$. |
| **Step-by-Step Simplify (`{{key:SIMP}}`)** | **Fraction Reduction You Control:** Keeps fractions unreduced until *you* press `{{key:SIMP}}` to divide out shared factors; flashes `LOWEST TERMS` when fully simplified. |
| **Last Number Recall (`{{key:LASTX}}`)** | **One-Tap Undo & Work Checker:** Brings back the number you just used so you can check addition with subtraction (or reuse a measurement) without re-typing a single digit. |

### Climbing Times Tables with Constant Repeat (`{{key:REP}}`)
Memorizing multiplication tables from flashcards can feel hard when you don't see equal groups building up step by step. On the SC-6, when you type a number like `7` and tap **`{{key:REP}}`**, the calculator fills all four shelves of the stack with `7`:
$$X = 7, \quad Y = 7, \quad Z = 7, \quad T = 7$$
Now, every tap of **`{{key:+}}`** drops another `7` onto your total. As you tap `{{key:+}}` in a steady rhythm, watch the screen climb the 7s ladder:
$$7 \xrightarrow{[+]} 14 \xrightarrow{[+]} 21 \xrightarrow{[+]} 28 \xrightarrow{[+]} 35 \xrightarrow{[+]} 42 \xrightarrow{[+]} 49 \xrightarrow{[+]} 56 \dots$$
Because the top shelf ($T$) automatically makes a fresh copy of `7` every time the stack drops, your skip-counting ladder never runs out! (Try tapping `2` `{{key:REP}}` and then clicking `{{key:×}}` twenty times in a row—you will watch `2` double to `4, 8, 16, 32...` all the way past **one million (`1,048,576`)** in seconds.)

### Real-World Sharing with Quotient & Remainder (`{{key:÷R}}`)
When you divide $17 \div 5$ on an ordinary calculator, the screen says `3.4`. What does `0.4` mean when you are packing 17 eggs into 5-egg cartons, or sharing 17 counting tiles among 5 friends? In real life, you cannot hand a friend `0.4` of a tile—each friend gets **3 whole tiles**, and there are **2 tiles left over**.

On your SC-6, typing `17 {{key:ENTER}} 5 {{key:÷R}}` solves both parts of the sharing story at once:
- **Shelf $X$** shows the whole groups: **`3`** (each friend gets 3 tiles).
- **Shelf $Y$** holds the exact leftovers: **`2`** (2 tiles left over on the table).
- Tapping **`{{key:x⇄y}}`** swaps the two shelves whenever you want to trade places between the whole groups and the remainder.

### Simplifying Fractions at Your Own Pace (`{{key:SIMP}}`)
When you place a $\frac{1}{2}$ block ($42\text{ mm}$ tall) beside three $\frac{1}{6}$ blocks ($3 \times 14\text{ mm} = 42\text{ mm}$ tall) in your Fraction Studio tray, you can see and feel why $\frac{3}{6}$ and $\frac{1}{2}$ are the exact same height. On most calculators, typing a fraction like `12/18` immediately erases your numbers and replaces them with `2/3` or `0.66667` before you even get a chance to think about what factor they share!

The SC-6 **keeps your fractions unreduced until you decide to simplify them**. When you enter twelfths or eighteenths (using the two-dot fraction key, `. 12 . 18 {{key:ENTER}}`), the screen keeps `12/18` intact. When you are ready to simplify, tap **`{{key:SIMP}}`** to divide out the shared factor and reveal `2/3`. Tap `{{key:SIMP}}` one more time when no shared factors remain, and the screen proudly flashes **`LOWEST TERMS`**.

### Checking Your Own Work Without Re-Typing (`{{key:LASTX}}`)
Every teacher and parent says, *"Always check your work!"* Usually, checking an addition problem by subtracting (or checking division by multiplying) is annoying because you have to type the numbers all over again.

On the SC-6, every time an operation combines two numbers, the calculator automatically tucks a backup copy of the number from Shelf $X$ into a special memory pocket called **`LAST x`**. Suppose you add $47 + 36$:
`47 {{key:ENTER}} 36 {{key:+}}` $\implies \mathbf{83}$
To prove that $83$ is right—or to undo a button you pressed by mistake—just tap **`{{key:LASTX}}`**:
- Your `36` jumps right back onto Shelf $X$, automatically lifting `83` up to Shelf $Y$.
- Now tap **`{{key:-}}`**, and `83 - 36` lands right back on your starting number, **`47`**!

---

## Seeing Math Inside the Screen: Your Visual Sandboxes

On top of regular numbers, your SC-6 has five built-in **Visual Sandboxes** that draw your math blocks directly inside Shelf $Y$ and Shelf $X$:
1. **Ten-Frame Studio (`{{key:▦}}`):** Draws two $2 \times 5$ ten-frame trays right on the screen, showing filled dots (`●`), empty spaces (`○`), and how many more dots are needed to make 10.
2. **Number Line Jumping Tool (`{{key:LINE}}`):** Draws a number line where `{{key:+}}` hops forward with curved jump arcs and `{{key:-}}` hops backward (even left of zero into negative numbers!).
3. **Number Rack / Rekenrek (`{{key:COUNT}}`):** Displays two rows of 10 sliding beads (5 dark and 5 light) so your eyes can spot groups of 5 and 10 without counting one by one.
4. **Planetary Clock & Elapsed Time (`{{key:🕒}}`):** Draws twin 12-hour clock faces with linked hands so you can add and subtract hours and minutes across the 60-minute mark.
5. **Polyhedral Dice (`{{key:🎲}}`) & Math Quiz Game (`{{key:?}}`):** Rolls fair digital dice right onto the stack (`{{key:🎲}}`) or launches a 6-level mental-math sprint game (`{{key:?}}`) that tracks your winning streak.

Whenever you are inside one of these visual modes and want to switch back to regular numbers, just tap the **`{{key:C}}` (Clear)** button once when you aren't typing digits (or tap the same mode button a second time). Switching between visual pictures and regular numbers never erases your stack—it simply changes the lens through which you look at the numbers on your shelves!

{{res:sc6_hero_calculator:screenshot|StackCalc SC-6 Elementary Calculator Faceplate & 43-Key Topography}}
*Figure 0.1: The StackCalc SC-6 Elementary RPN Calculator faceplate, featuring 19 oversized tactile switches with sculpted TPU keypads, a double-wide `{{key:ENTER}}` key, and `{{key:f}}` and `{{key:g}}` shift legends.*

---

## Five Everyday Stories Where the Stack Shines

Before we begin Chapter 1, let's walk through **five short, everyday math stories** to see how your shelves ($T, Z, Y,$ and $X$) work in practice. Beneath each story is a **4-Register Stack Table** showing what is sitting on each shelf after every button press. (For **25 additional Quick-Start Warm-Up Adventures**, open the companion **[SC-6 Elementary Companion Problem & Activity Workbook](../../curriculum/sc6-elementary-companion-workbook.md)**.)

### Finding Missing Spaces on a Ten-Frame Tray
*Previewing [Chapter 03: Counting, Number Lines & Place Value Studio](03-counting-place-value.md)*

Maya places **7 red counters** into her 10-space Ten-Frame tray, filling the top row of 5 and 2 more spaces on the bottom row. How many blue counters does she need to fill all 10 spaces?

On the stack, we start with the full tray capacity (`10`) and take away the `7` spaces that are already filled. That means `10` goes onto the Waiting Shelf ($Y$) first via `10 {{key:ENTER}}`, `7` goes onto the Workbench ($X$), and tapping `{{key:-}}` finds the **`3`** empty spaces:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `{{key:C}}` | 0 | 0 | 0 | 0 | Clean baseline stack in `{{key:NUM}}` mode. |
| `10` | 0 | 0 | 0 | 10 | Key target capacity ($10$) into Ground Floor $X$. |
| `{{key:ENTER}}` | 0 | 0 | 10 | 10 | Target capacity lifts smoothly into Mezzanine Floor $Y$. |
| `7` | 0 | 0 | 10 | 7 | Enter red counters into Ground Floor $X$. |
| `{{key:-}}` | 0 | 0 | 0 | 3 | Subtraction combines $Y - X = 3$. Result in $X$. |

*What if your screen says `17` instead of `3`?* That just means your thumb tapped `{{key:+}}` instead of `{{key:-}}`! You don't have to clear and start over: tap `{{key:LASTX}} {{key:-}}` to undo the accidental addition (bringing back `10`), and then tap `{{key:LASTX}} {{key:-}}` again to subtract `7` and land on **`3`**.

### Checking Your Trading Cards in Reverse (`{{key:LASTX}}`)
*Previewing [Chapter 02: How Stack Math Works](02-rpn-for-young-learners.md) & [Chapter 04: Whole Number Operations](04-operations-skip-counting.md)*

Suppose you are counting trading cards: you have **24 cards** in your binder and **15 cards** in a tin box ($24 + 15 = 39$). How can you prove that `39` is right without typing `39` or `15` again?

First we add `24` and `15` on the stack (`24 {{key:ENTER}} 15 {{key:+}}` to get `39`). Because the calculator automatically saved `15` inside `LAST x`, tapping `{{key:LASTX}}` brings `15` right back to Shelf $X$ while lifting `39` to Shelf $Y$—so a single tap of `{{key:-}}` proves that $39 - 15 = 24$:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `24 {{key:ENTER}}` | 0 | 0 | 24 | 24 | First number committed to Mezzanine Floor $Y$. |
| `15 {{key:+}}` | 0 | 0 | 0 | 39 | Addition completed; `LAST x` preserves $15$ in hardware. |
| `{{key:LASTX}}` | 0 | 0 | 39 | 15 | Prior number ($15$) recalled into $X$; sum lifts to $Y$. |
| `{{key:-}}` | 0 | 0 | 0 | 24 | Inverse check: $39 - 15 = 24$. Starting number verified. |

### Packing Science Museum Vans with Whole Groups and Leftovers (`{{key:÷R}}`)
*Previewing [Chapter 04: Whole Number Operations & Skip-Counting Ladders](04-operations-skip-counting.md)*

A group of **125 students and chaperones** is heading to the science museum in vans that hold **8 passengers each**. How many vans will be completely full, and how many passengers will ride in the last van?

When we put all `125` passengers on Shelf $Y$ (`125 {{key:ENTER}}`), put the van capacity `8` on Shelf $X$, and tap **`{{key:÷R}}`** (*Quotient & Remainder*), the SC-6 answers both questions at once: **Shelf $X$** shows **`15`** completely full vans, and **Shelf $Y$** shows **`5`** leftover passengers who need one more van (so the school needs $15 + 1 = 16$ vans in all so nobody gets left behind!):

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `125` | 0 | 0 | 0 | 125 | Total passengers entered into Ground Floor $X$. |
| `{{key:ENTER}}` | 0 | 0 | 125 | 125 | 125 committed and copied to Mezzanine Floor $Y$. |
| `8` | 0 | 0 | 125 | 8 | Capacity per van keyed into $X$. |
| `{{key:÷R}}` | 0 | 0 | 5 | 15 | Integer division with remainder: $X = 15$ full vans, $Y = 5$ leftover passengers. |

### Painting Six Walls of a Wooden Treasure Box Without Scrap Paper (`{{key:Σ+}}`)
*Previewing [Chapter 06: Geometry, Surface Area & Planetary Time](06-geometry-surface-area.md)*

Imagine painting all 6 flat wooden walls of a rectangular treasure box that is **$5\text{ cm}$ long, $4\text{ cm}$ wide, and $3\text{ cm}$ high**. Every box has **three matching pairs of walls**:
- **Top & Bottom Walls:** $2 \times (5 \times 4) = 40\text{ cm}^2$
- **Front & Back Walls:** $2 \times (5 \times 3) = 30\text{ cm}^2$
- **Left & Right Walls:** $2 \times (4 \times 3) = 24\text{ cm}^2$

Instead of writing `40`, `30`, and `24` on scrap paper, you can use the **`{{key:Σ+}}` (*Add to Total*)** button like a **shopping basket for walls**! First clear the basket with `{{key:CLΣ}}`, toss each pair of walls into the basket with `{{key:Σ+}}` (watching the screen count `1`, `2`, `3` pairs in the basket), and then tap **`{{key:Σx}}` (*Grand Total*)** to add all three pairs into **`94.0` $\text{cm}^2$**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `{{key:CLΣ}}` | 0 | 0 | 0 | 0 | Clear the running total before adding face pairs. |
| `5 {{key:ENTER}} 4 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | 0 | 0 | 0 | 1 | Face Pair 1 ($40\text{ cm}^2$) added to total; Register $X$ shows `1` pair added. |
| `5 {{key:ENTER}} 3 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | 0 | 0 | 0 | 2 | Face Pair 2 ($30\text{ cm}^2$) added to total; Register $X$ shows `2` pairs added. |
| `4 {{key:ENTER}} 3 {{key:×}} 2 {{key:×}} {{key:Σ+}}` | 0 | 0 | 0 | 3 | Face Pair 3 ($24\text{ cm}^2$) added to total; Register $X$ shows `3` pairs added. |
| `{{key:Σx}}` | 0 | 0 | 0 | $94.0$ | Recall the Grand Total of All Pairs: $94\text{ cm}^2$ without scratch paper. |

### Measuring a Backyard Brick Patio and Its Border (`{{key:x²}}` and `{{key:LASTX}}`)
*Previewing [Chapter 06: Geometry, Surface Area & Planetary Time](06-geometry-surface-area.md)*

Your backyard is **$12\text{ feet}$ wide**, and you leave a **$3\text{-foot}$ grass path** along one side to build a square brick patio ($12 - 3 = 9\text{ feet}$ on each side). How many $1\text{-foot}$ square bricks do you need to fill the patio's **Area** ($9 \times 9$), and how many feet of wooden edging do you need for its 4-sided **Perimeter** ($9 \times 4$)?

After we subtract `12 {{key:ENTER}} 3 {{key:-}}` to get the $9\text{-foot}$ side length, tapping **`{{key:x²}}`** multiplies $9 \times 9 = \mathbf{81\text{ sq ft}}$ of bricks. Then, instead of typing `9` again, tapping **`{{key:LASTX}}`** pulls the $9\text{-foot}$ side length right back onto Shelf $X$ (lifting `81` onto Shelf $Y$!) so multiplying by `4` (`4 {{key:×}}`) shows **`36` feet** of border edging on Shelf $X$ right beside **`81` square feet** of bricks on Shelf $Y$:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
|:---|:---:|:---:|:---:|:---:|:---|
| `12 {{key:ENTER}} 3 {{key:-}}` | 0 | 0 | 0 | 9 | Yard width minus grass path: $12 - 3 = 9\text{ ft}$ patio side. |
| `{{key:x²}}` | 0 | 0 | 0 | 81 | Square side length: $9 \times 9 = 81\text{ sq ft}$ patio area (`LAST x` saves 9). |
| `{{key:LASTX}}` | 0 | 0 | 81 | 9 | Recall side length $9\text{ ft}$ into $X$; area $81$ lifts to $Y$. |
| `4 {{key:×}}` | 0 | 0 | 81 | 36 | Multiply side by 4: $9 \times 4 = 36\text{ ft}$ border perimeter ($Y$ still shows $81\text{ sq ft}$ area). |

---

## Three Helpful Stack Tips Before You Begin

As you and your family start exploring the SC-6, keep these three simple tips in mind:

1. **`{{key:ENTER}}` Keeps Your Number; `{{key:C}}` Clears It:**  
   On some phone apps, people confuse `C` with "Confirm." On the SC-6, the big **`{{key:ENTER}}`** button is the elevator door that locks your number in and lifts it up to Shelf $Y$. The **`{{key:C}}`** button is the eraser that clears Shelf $X$ back to `0`.
2. **Typed Two Numbers Backward for Subtraction or Division? Just Tap `{{key:x⇄y}}`:**  
   When subtracting $15 - 8$, your starting pile (`15`) goes onto Shelf $Y$ first (`15 {{key:ENTER}} 8 {{key:-}}`). If you ever type them backward (`8 {{key:ENTER}} 15`), don't erase! Just tap **`{{key:x⇄y}}`** to swap their shelves (`15` in $Y$, `8` in $X$), and then press `{{key:-}}`.
3. **Entering Clock Time (`2.30` Means 2 Hours 30 Minutes):**  
   When you use the Geared Clock (`{{key:🕒}}`) in Chapter 6, type hours and minutes just like a digital wall clock: `2` hours and `30` minutes is typed as **`2.30`** (and if you ever have `2.5` decimal hours and want clock minutes, tapping `{{key:▸HMS}}` converts `2.5` into `2:30:00` automatically).

### At a Glance: Why Stack Math Keeps Your Head Clear

| Everyday Math Problem | Standard Calculator (Infix) | StackCalc SC-6 (RPN) | Why the Stack Feels Easier |
| :--- | :--- | :--- | :--- |
| **1. Checking Addition** $(47 + 36) - 36 = 47$ | `47 + 36 = - 36 =` (9 strokes; re-types 36) | `47` `{{key:ENTER}}` `36` `{{key:+}}` `{{key:LASTX}}` `{{key:-}}` (6 strokes) | **`{{key:LASTX}}` remembers `36`** so you never re-type it. |
| **2. Two-Part Puzzle** $(15 - 3) \times (4 + 2) \div 6$ | `( 15 - 3 ) × ( 4 + 2 ) ÷ 6 =` (18 strokes) | `{{res:sc6_order_of_ops:keys}}` $\to$ **`{{res:sc6_order_of_ops:value}}`** (11 strokes) | **Zero parentheses**; you see `12` and `6` before multiplying. |
| **3. Sharing with Leftovers** $125 \div 8 = 15\text{ R }5$ | `125 ÷ 8 =` (`15.625`), then multiply & subtract on paper | `125` `{{key:ENTER}}` `8` `{{key:÷R}}` $\to$ `15` ($X$) & `5` ($Y$) (5 strokes) | **Shows `15` vans and `5` leftover riders** at the same time. |
| **4. Adding Fractions** $\frac{3}{8} + \frac{5}{12} = \frac{19}{24}$ | `( 3 ÷ 8 ) + ( 5 ÷ 12 ) =` (gives decimal `0.79167`) | `. 3 . 8` `{{key:ENTER}}` `. 5 . 12` `{{key:+}}` $\to$ **`19/24`** (8 strokes) | **Keeps exact fractions** that match your Fraction Towers. |
| **5. Box Surface Area** ($5 \times 4 \times 3$ box) | `2 × 5 × 4 + 2 × 5 × 3 + 2 × 4 × 3 =` | Toss each wall pair into `{{key:Σ+}}`, then tap `{{key:Σx}}` $\to$ **`94`** | **Zero scrap paper**; the basket counts `1, 2, 3` wall pairs. |

## How to Navigate This Book & Topic Finder

This book is organized into nine hands-on chapters and four reference appendices. You can read it straight through from Chapter 1 to Chapter 9 as a story of mathematical discovery, or jump directly to the topic you are exploring today:

- **Building Your Stack & Whole-Number Foundations ([Chapters 01](01-hardware-architecture.md)–[04](04-operations-skip-counting.md)):** Set up your desk studio and try your first block-and-stack discoveries in [Chapter 01](01-hardware-architecture.md), ride the full 4-story Number Elevator in [Chapter 02](02-rpn-for-young-learners.md), explore ten-frames, number lines, and place value up to billions in [Chapter 03](03-counting-place-value.md), and build multiplication tile arrays, skip-counting ladders (`{{key:REP}}`), and remainder division (`{{key:÷R}}`) in [Chapter 04](04-operations-skip-counting.md).
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
