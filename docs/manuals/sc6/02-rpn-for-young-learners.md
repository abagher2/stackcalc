---
title: "Chapter 2: How Stack Math Works: Stacking Numbers Just Like Blocks"
description: "Master Stack Math on the SC-6: stacking numbers on a 4-level stack, leaving behind the confusing equals sign, and solving multi-step problems with zero parentheses."
---

# Chapter 2: How Stack Math Works: Stacking Numbers Just Like Blocks

## The Equals-Sign Trap vs. The 4-Story Number Elevator

In the Preface and Chapter 1, you met the bottom two shelves of your **StackCalc SC-6**—**Ground Shelf $X$** and **Waiting Shelf $Y$**—and tried your first stack additions. You saw how typing a number, pressing `{{key:ENTER}}` to slide it onto Waiting Shelf $Y$, and tapping `{{key:+}}` snaps two numbers together just like physical blocks on your desk.

Now a bigger question awaits: what happens when a real-world math puzzle has *two* or *three* parts happening at once—like buying 3 warm pretzels at $\$4$ AND 2 smoothies at $\$5$, or solving a multi-step challenge like $(15 - 3) \times (4 + 2) \div 6$?

In this chapter, you will unlock the **full 4-story Number Elevator ($X, Y, Z, T$)** tucked inside your calculator. To see why a four-shelf elevator makes multi-step math so much easier than a regular calculator, let's first look at a sneaky habit that trips up almost every student in elementary school.

Have you ever wondered why school worksheets always put an equals sign (`=`) at the end of a problem like $4 + 3 = \underline{\hspace{0.5cm}}$?

After a few years of filling in those blanks, it is easy to fall into the **Equals-Sign Trap**. When you see an equals sign at the end of every line, you might start believing that `=` means *"do the math right now and write the answer here."*

Then one day, a teacher writes an open puzzle on the board with the box in the middle—just as cognitive researchers Karen Falkner, Thomas Carpenter, and Elizabeth Fennema tested across elementary classrooms {{cite:falkner1999}}:
$$8 + 4 = \Box + 5 \quad \text{or} \quad 5 + \Box = 12$$
In the landmark study, the vast majority of students wrote $12$ or $17$ in the box. Why? Because their eyes darted across the numbers and the `+` sign, and their fingers immediately added everything in sight. They didn't read the equation as two side-by-side **Counting & Array Studio** block towers that must stand flush at the exact same height—they treated the equals sign as an emergency "compute now" button {{cite:falkner1999}}.

Now think about what **you** do in the real world when you build with physical blocks:
Suppose you have **5 blue blocks** resting on your desk, and your friend hands you **3 red blocks**. How do you put them together?
You don't wave a magic wand and shout *"Equals!"* You simply slide the 3 red blocks straight into the 5 blue blocks. **Putting them together IS the answer (`8`).**

Here is the secret of **Stack Math**: **your brain doesn't think in parentheses and equals signs—your brain naturally stacks physical objects.**
- When you pack your backpack, you place your heavy binder on the bottom shelf, then stack your lunchbox on top.
- When you bake cookies, you weigh the flour into the bowl, crack an egg on top, and stir them together.
- When you stack blocks, pancakes, or books, each new item rests on top of the stack.

That is how **Stack Math** works on your **StackCalc SC-6**:
1. Type the first number (`5`) and press `{{key:ENTER}}` to push it onto the waiting shelf (Level $Y$).
2. Type the second number (`3`) on the ground shelf (Level $X$).
3. Tap `{{key:+}}`—and *SNAP!* The upper shelf drops down, fusing the two numbers into `8` right before your eyes.

Instead of wrestling with parentheses, syntax errors, and misleading equals signs, on the SC-6 you keep a clear, visible stack of numbers that you can combine, separate, and inspect at any time.

> **Keys & Tools in This Chapter**
> - **Numeric Entry:** Digits `{{key:0}}` through `{{key:9}}`.
> - **Stack Actions:** `{{key:ENTER}}` (Stack Lift / Push Up), `{{key:C}}` (Clear), `{{key:<-}}` (Backspace), `{{key:x⇄y}}` (Swap), `{{key:R↓}}` (Roll Down), `{{key:REP}}` (Repeat Operation), `{{key:LASTX}}` (Recover Last Number).
> - **Basic Arithmetic:** `{{key:+}}` (Combine / Add), `{{key:-}}` (Remove / Subtract), `{{key:×}}` (Multiply), `{{key:÷}}` (Divide).
> - **Visual Sandboxes (Introduced in Chapter 3):** `{{key:▦}}` Ten-Frame, `{{key:COUNT}}` Step Counter / Bead Rack, `{{key:LINE}}` Number Line, `{{key:PV}}` Place Value.
> - **Stack View Options:** Choose between a simple 2-shelf view or the full 4-shelf view (for multi-step problems) using `{{key:FLAGS}}`.

---

## Unlocking the 4-Story Number Elevator ($T, Z, Y, X$)

When you only have two numbers to combine, Ground Shelf $X$ and Waiting Shelf $Y$ are all you need. But what if you finish calculating the first half of a problem—say, $15 - 3 = 12$—and you need a safe place to park that `12` while you work on the second half ($4 + 2 = 6$)?

Instead of making you copy `12` onto scrap paper or wrap everything in parentheses, your SC-6 has **two more waiting floors upstairs**—**Floor $Z$ (the Third-Floor Loft)** and **Floor $T$ (the Top-Floor Penthouse)**:

{{blocks:number_rack_subitizing|Number Rack Two-Color Bead Math Rekenrek}}
*Figure 2.1: The Number Rack (Rekenrek) model. Intermediate numbers rest on visible horizontal levels just as numbers wait on the operational shelves of the SC-6.*

| Stack Level | Stack Register | What It Does | Where You See It |
|---|---|---|---|
| **Level 4** | **Register T** | **Top Shelf** (Keeps your multiplier locked for skip-counting) | Top line on screen |
| **Level 3** | **Register Z** | **Third Shelf** (Waiting shelf for multi-step problems) | Second line from top |
| **Level 2** | **Register Y** | **Second Shelf** (Waiting partner, held for subtraction or division) | Left column in $Y \mid X$ layout |
| **Level 1** | **Register X** | **Ground Shelf** (Active shelf where you type and see results) | Right column / primary LCD line |

### The Three Golden Rules of Stack Math

1. **Rule 1: New Numbers Enter at the Ground Shelf (Level $X$).**  
   Whenever you tap digit keys (for example, `{{key:3}}`), that number appears on Level $X$. Level $X$ is the active display shelf you see right before your eyes.
2. **Rule 2: Pressing `{{key:ENTER}}` Pushes Numbers UP the Stack.**  
   When your first number is entered, tapping `{{key:ENTER}}` pushes it up to Level $Y$ (like an elevator rising to the second floor), leaving an identical copy ready on Level $X$ so you can type your next number.
3. **Rule 3: Pressing an Operator Key (`+`, `-`, `×`, `÷`) Drops the Stack Down.**  
   When you tap an operational key such as `{{key:+}}`, the upper shelf drops down. The number on Level $Y$ combines with the number on Level $X$, and their combined total remains on the ground shelf ($X$). Meanwhile, any number waiting upstairs on Floor $Z$ rides the elevator down to Floor $Y$, ready for its turn!

| Stack Level | Before Pressing `{{key:+}}` | Action During `{{key:+}}` | After Pressing `{{key:+}}` |
| :--- | :---: | :--- | :---: |
| **Level 2 (`Y`)** | `3` | Drops down to combine with Level 1 | `0` |
| **Level 1 (`X`)** | `4` | Receives $3 + 4$ | **`7`** |

### Automatic Stack Lift: Why You Never Lose a Finished Answer
One of the friendliest habits of your SC-6 is **automatic stack lift**. Suppose you just added `4 {{key:ENTER}} 5 {{key:+}}` and your answer `9` is sitting on Ground Shelf $X$. What happens when you start typing a new number, like `{{key:6}}`?

You do **NOT** need to press `{{key:ENTER}}` first, and typing `{{key:6}}` will **never** erase your `9`! Because the calculator knows `9` is a finished answer, the moment you touch `{{key:6}}`, it automatically lifts `9` up to Waiting Shelf $Y$ (and pushes anything in $Y$ up to $Z$) to make room for your `6` on the ground floor:

**Watching Automatic Stack Lift in Action** (After `4 {{key:ENTER}} 5 {{key:+}}` gives $X = 9$, then typing `{{key:6}}`):

| Register | BEFORE Typing `6` | DURING Typing `6` | AFTER Typing `6` |
| :---: | :---: | :---: | :---: |
| **Register T** | $0$ | $0$ | $0$ |
| **Register Z** | $0$ | $0$ | $0$ |
| **Register Y** | $0$ | **$9$** (Lifts up) | **$9$** |
| **Register X** | **$9$** (Prior answer) | `6_` | **$6$** |

### How the Elevator Drops (and the Top-Shelf Secret)
Whenever you press a two-number action key (`+`, `-`, `×`, `÷`), the whole four-story elevator moves together in one smooth step:
1. The waiting number on **Shelf $Y$** combines with the active number on **Shelf $X$**—for example, in subtraction or division, Shelf $Y$ always goes first: $\text{Shelf } Y - \text{Shelf } X$ ($12 - 5 = 7$) or $\text{Shelf } Y \div \text{Shelf } X$ ($12 \div 4 = 3$).
2. Their combined answer lands on **Ground Shelf $X$**.
3. Whatever was waiting on **Floor $Z$** drops down into **Shelf $Y$**.
4. Whatever was on **Top Shelf $T$** drops down into **Floor $Z$**—and **leaves a copy of itself behind on Top Shelf $T$!**

Why does Top Shelf $T$ leave a copy of itself behind every time the elevator drops? Because if you lock a step size (like `7`) into the top floor, it will keep feeding fresh `7`s down the elevator forever, letting you skip-count through your times tables ($7, 14, 21, 28 \dots$) with single taps of `{{key:+}}`!

---

## Why Combining Numbers IS the Answer (Zero Parentheses)

> **The Golden Rule of RPN:** On the StackCalc SC-6, you never wait for an equals sign. The moment you press `{{key:+}}`, `{{key:-}}`, `{{key:×}}`, or `{{key:÷}}`, the numbers on Level 1 ($X$) and Level 2 ($Y$) combine immediately.

Watch how fast you can solve a 5th-grade order-of-operations expression without writing down a single scrap-paper note or pressing a single parenthesis key:

$$(15 - 3) \times (4 + 2) \div 6 = 12$$

- **Step 1 (First group):** Tap `{{res:sc6_02_rpn_for_young_learners_seq_42:keys}}`, and **`12`** immediately appears on Ground Shelf $X$.
- **Step 2 (Second group):** Without clearing or writing anything down, tap `{{res:sc6_02_rpn_for_young_learners_seq_43:keys}}` so **`6`** forms on Level 1 ($X$) while **`12`** waits safely upstairs on Level 2 ($Y$).
- **Step 3 (Multiply & Divide):** Tap `{{key:×}}` to fuse the two waiting groups into `72`, then tap `6` `{{key:÷}}` to split `72` into **`{{res:sc6_order_of_ops:value}}`**.

When you string the entire sequence together from left to right—pressing `{{res:sc6_order_of_ops:keys}}`—the four-story elevator carries both intermediate groups and lands squarely on **`{{res:sc6_order_of_ops:value}}`**.

| Keystroke | Register T (Roof Floor) | Register Z (Loft Floor) | Register Y (Mezzanine) | Register X (Ground Flr) |
| :--- | :--- | :--- | :--- | :--- |
| `15` | 0 | 0 | 0 | 15 |
| `{{key:ENTER}}` | 0 | 0 | 15 | 15 |
| `3` | 0 | 0 | 15 | 3 |
| `{{key:-}}` | 0 | 0 | 0 | 12 |
| `4` | 0 | 0 | 12 | 4 |
| `{{key:ENTER}}` | 0 | 12 | 4 | 4 |
| `2` | 0 | 12 | 4 | 2 |
| `{{key:+}}` | 0 | 0 | 12 | 6 |
| `{{key:×}}` | 0 | 0 | 0 | 72 |
| `6` | 0 | 0 | 72 | 6 |
| `{{key:÷}}` | 0 | 0 | 0 | 12 |

{{res:sc6_order_of_ops:screenshot|SC-6 Parenthesis-Free Order of Operations: (15 - 3) x (4 + 2) / 6 = 12}}

### Parenthesis Traps vs. Inside-Out Elevator Math

Just as cognitive researcher Jerome Bruner showed that learners build lasting understanding by moving from hands-on blocks to visual models to symbols {{cite:bruner1966}}, evaluating expressions from the inside out on the stack lets your working memory focus on two numbers at a time {{cite:sweller1988,miller1956}} without juggling nested parentheses {{cite:lukasiewicz1924,hamrick1980}}. Compare how a parenthesized multi-step expression is entered on a standard calculator versus inside-out evaluation on the SC-6 stack:

| Challenge / Equation | The Algebraic Calculator Trap (Standard Entry) | The StackCalc SC-6 + Blocks Method | Keystroke Reduction | Live Stack Visibility | Learning Breakthrough |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **5th Grade Order of Operations:** $(15 - 3) \times (4 + 2) \div 6 = 12$ | `( 1 5 - 3 ) * ( 4 + 2 ) / 6 =` (14 keystrokes). *Trap: Missed or misplaced parenthesis computes $15 - 12 + 0.33 = 3.33$ silently. Intermediate results ($12, 6$) are invisible inside hardware buffers.* | **SC-6 Elevator Stack + Two-Number Fusion:** `15 {{key:ENTER}} 3 {{key:-}} 4 {{key:ENTER}} 2 {{key:+}} {{key:×}} 6 {{key:÷}}` (11 keystrokes). Both intermediate quantities ($12$ in $Y$, $6$ in $X$) are visible simultaneously before multiplying. Zero parentheses. | **21% fewer keystrokes** (11 vs. 14) | **Dual Live Registers:** Register $Y$ holds $12$ while Register $X$ computes $6$; live display proves $(15 - 3) \times (4 + 2)$ without scratch paper. | **Clarity of Structure:** Eliminates parenthesis anxiety and the Order-of-Operations & Parentheses Trap; replaces abstract rules with physical two-number stack fusion. |

---

## Five Core Stack Techniques: A Quick Preview

Throughout this book, five core techniques connect your 3D-printed math blocks (Ten-Frame Trays, Number Rack, Counting Tiles, and 84 mm Fraction Towers) directly to the 4-level stack:
- **1. The Make-a-Ten Snap (`{{key:▦}}`):** Bridging across 10 on your Ten-Frame tray before chaining addition (Chapter 3).
- **2. The Elevator Stack Drop (`{{key:ENTER}}`, `{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`):** Letting intermediate subtotals ride upstairs to Floors $Y, Z, T$ and drop down on cue with zero parentheses.
- **3. The Remainder-You-Can-Hold (`{{key:÷R}}`):** Splitting division into a whole Quotient in $X$ and a physical Remainder in $Y$ at the same time (in our Weekend Maker Fair adventure below and in Chapter 4).
- **4. The Equal-Fraction Tower Alignment (`{{key:SIMP}}`):** Aligning $84\text{ mm}$ Fraction Towers flush in the comparator well while reducing factors step by step (Chapter 5).
- **5. The Skip-Counting Ladder (`{{key:REP}}`):** Locking a constant step into Floor $T$ so rhythmic taps of `{{key:+}}` or `{{key:×}}` climb times tables automatically (Chapter 4).

Let's look inside the screen and keypad to see how the horizontal $Y \mid X$ split display and stack controls work.

---

## Horizontal $Y \mid X$ Split Screen vs. Vertical Stack

When you first learn mathematics in elementary school, you learn to read and write equations from left to right (like $12 - 4 = 8$ or $12 \div 4 = 3$). Traditional RPN calculators display registers vertically ($Y$ above $X$), which can feel upside-down at first.

The SC-6 graphic LCD introduces the **Horizontal $Y \mid X$ Split Screen Layout**:

**↰ ↱ FRAC                   Y                X              [BATTERY]**

| Left Column (`Y` — Waiting Number) | Center Divider | Right Column (`X` — Active Number) |
| :---: | :---: | :---: |
| **`12`** | Vertical Split Rule | **`4`** |

### The Enter-Slide Animation
1. **Typing Your First Number:** When you key `12`, it appears in the **Right ($X$)** column.
2. **Pressing `{{key:ENTER}}`:** The digits `12` visually slide smoothly across the LCD from the right column into the **Left ($Y$)** column. You see: *"My 12 has moved into position on the left, waiting for math."*
3. **Typing Your Second Number:** When you key `4`, it enters the **Right ($X$)** column. The display clearly presents `Y = 12` and `X = 4`.
4. **Pressing an Operator (`{{key:-}}` or `{{key:÷}}`):**
   - The operator symbol briefly flashes in the center vertical divider line.
   - The calculator combines Shelf $Y$ on the left with Shelf $X$ on the right ($12 - 4 = 8$ or $12 \div 4 = 3$).
   - The result appears in the right column ($X$), while the stack drops.

### Customizing Your Screen View: Side-by-Side ($Y \mid X$) vs. Single Number ($X$)
Everyone's eyes work a little differently when learning a new skill. Using the `{{key:FLAGS}}` menu (Flag 5), you can choose how your SC-6 displays the bottom shelves of your stack:
- **Side-by-Side View (Flag 5 = 0, Default — Dual Stack $Y \mid X$):** Shows both your waiting number on the left ($Y$) and your active number on the right ($X$) at the exact same time. Seeing both numbers side by side makes subtraction ($Y - X$) and division ($Y \div X$) feel just like reading from left to right across a page.
- **Big Single-Number View (Flag 5 = 1 — Single Stack $X$ Only):** Fills the screen with one extra-large, bold number ($X$). When you press `{{key:ENTER}}`, your first number still rides up to Shelf $Y$ in the background while your screen stays clean and simple for typing the next number.

---

## Choosing How Many Shelves You Need: `2-LV`, `4-LV`, and `8-LV`

Just as you might use a small two-pocket folder for a quick homework sheet or a big four-shelf locker for all your school projects, the `{{key:FLAGS}}` menu lets you choose how many shelves your Number Elevator uses:

- **2-Shelf Mode ($X, Y$ — `2-LV`):** Uses just two shelves—Waiting Shelf $Y$ and Ground Shelf $X$. Because Shelf $Y$ is the top shelf in this mode, whatever number sits on Shelf $Y$ stays locked there like a permanent step-counter! That makes `2-LV` wonderful for early explorers practicing single-step addition, subtraction, and Ten-Frame games.
- **4-Shelf Mode ($X, Y, Z, T$ — `4-LV` Standard):** The classic four-story Number Elevator—Ground ($X$), Mezzanine ($Y$), Loft ($Z$), and Penthouse Roof ($T$). This is your everyday mode for 3rd–6th grade adventures: multi-step word problems, whole-number division with remainders (`{{key:÷R}}`), fractions, and parenthesis-free order of operations.
- **8-Shelf Mode (8 Stories Deep — `8-LV`):** Expands the elevator to 8 full waiting shelves for long tournament mental-math relays where you want to stack half a dozen subtotals without touching scratch paper.

### A Fun Discovery: How a Step Counter Works in 2-Shelf vs. 4-Shelf Mode
One of the first experiments kids try on a calculator is building an automatic step counter: typing `{{res:sc6_02_rpn_for_young_learners_seq_41:keys}}` and tapping `{{key:+}}` over and over to watch the screen climb $2, 3, 4, 5 \dots$

Try it in **4-Shelf Mode (`4-LV`)** first: after `1 {{key:ENTER}} 1 {{key:+}}` gives `2`, what happens if you tap `{{key:+}}` again? The screen stays at `2`! Why? Because in 4-Shelf mode, the elevator dropped `0` down from Floor $Z$ into Shelf $Y$, so tapping `{{key:+}}` simply added $2 + 0 = 2$. To make a 4-shelf elevator count forever, you first press Constant Repeat (`1 {{key:REP}}`), which fills all four shelves ($T, Z, Y, X$) with `1` so the Penthouse roof keeps feeding fresh `1`s down the stack!

In **2-Shelf Mode (`2-LV`)**, however, Shelf $Y$ *is* the roof of the building. So when `+` drops the stack, Shelf $Y$ automatically keeps its `1` forever:
`1 {{key:ENTER}} 1 {{key:+}}` $\implies \mathbf{2}$, `{{key:+}}` $\implies \mathbf{3}$, `{{key:+}}` $\implies \mathbf{4}$, `{{key:+}}` $\implies \mathbf{5}$!

---

## Moving Numbers Around on Your Stack: `{{key:x⇄y}}`, `{{key:R↓}}`, `{{key:REP}}`, `{{key:LASTX}}`

The SC-6 keypad provides dedicated physical keys to move and manage numbers on your stack:

| Keystroke | Operation | Stack Register Effect |
|---|---|---|
| `{{key:x⇄y}}` | **Swap $X$ and $Y$** | Exchanges the active input and held number ($X \leftrightarrow Y$). Instantly corrects reversed subtraction or division. |
| `{{key:R↓}}` | **Roll Down** | Rotates the 4-level stack downward in a carousel: $X \to T,\; T \to Z,\; Z \to Y,\; Y \to X$. |
| `{{key:REP}}` | **Stack Replicator** | Copies Register $X$ across all four shelves ($T, Z, Y, X \leftarrow X$) so you can tap `{{key:+}}` or `{{key:×}}` repeatedly for rhythmic skip-counting and constant scaling. |
| `{{key:LASTX}}` | **Undo & Twin-Calculation Recall** | Recalls the previous $X$ value before the last operation for self-checking inverse math or reusing a number without re-typing. |
| `{{key:SHOW}}` | **Full Significant Digits Reveal** | Momentarily displays all internal digits of Register $X$. |

### Meet Your Undo & Twin-Calculation Key (`{{key:LASTX}}`)
Every time you press an operation key (`{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`), where does the number on Floor $X$ go? It doesn't disappear. Your SC-6 automatically tucks a backup copy of that number into a register called **`LAST x`**.

Pressing `{{key:LASTX}}` (`{{key:f}}` then `{{key:ENTER}}`) pulls that number right back onto Floor $X$ while lifting your answer up to Floor $Y$. That gives you three practical advantages without ever re-typing a number:
1. **Two-Tap Self-Check:** Want to prove your subtraction $83 - 36 = 47$ is right? Just tap `{{key:LASTX}} {{key:+}}`—the calculator brings back `36`, adds it to `47`, and restores `83`. Divided $56 \div 7 = 8$? Tap `{{key:LASTX}} {{key:×}}` to bring back `7` and restore `56`.
2. **Quick Undo:** Accidentally tapped `{{key:+}}` when you meant `{{key:-}}`? Don't clear and start over. Tap `{{key:LASTX}} {{key:-}}` to undo the accidental addition, then tap `{{key:LASTX}} {{key:-}}` again to perform the subtraction you wanted.
3. **Zero-Retype Twin Calculations:** Whenever a multi-step problem needs the same number twice, `{{key:LASTX}}` hands it back to you in a single click so your fingers never waste time typing the same digits twice.

---

## Beat Every Adult in the Room! The `1089` Mind-Reading Stack Trick

Want to amaze your parents or friends at the dinner table? Tell them you can read their mind using the SC-6 elevator stack:
1. Write the secret number **`1089`** on a folded slip of paper and hand it to an adult before you start.
2. Ask them to pick *any* 3-digit number where the first and last digits differ by at least 2 (for example, **`732`**).
3. Have them reverse the digits (**`237`**) and subtract the smaller number from the larger on the stack (`732 {{key:ENTER}} 237 {{key:-}}` $\to$ `495`).
4. Now take that intermediate answer (`495`), reverse its digits (**`594`**), and add them right on the stack: when you run the complete chain by pressing `{{res:sc6_02_mind_reader_1089:keys}}`, the ground shelf immediately lights up with **`{{res:sc6_02_mind_reader_1089:value}}`**!
5. Tell them to open the folded paper—no matter which 3-digit number they started with, the stack lands on **`1089`** every single time! *(Why it works: subtracting a reversed 3-digit number always produces a multiple of 99 whose hundreds and ones digits add to 9, and adding its reverse gives $900 + 180 + 9 = 1,089$.)*

---

## Why Your Brain Loves Stack Math: The PEMDAS Funnel vs. The Inside-Out Stack

Why do you learn math faster and make fewer mistakes with Stack Math? Because your brain only has to think about two numbers at a time.

Consider a classic Grade 6 order-of-operations challenge:
$$40 - 3 \times (2 + 3)^2 \div 5 = 25$$

When students try to solve this on paper or a regular calculator, the **#1 trap** is subtracting $40 - 3 = 37$ first. Why? Because reading left-to-right tempts your eyes to grab $40 - 3$ before noticing that the $3$ is bound by multiplication to $(2 + 3)^2$. Compare the two ways to evaluate this expression:

### The PEMDAS Paper Funnel (Step-by-Step Rewrite)
On paper, you shrink the expression one line at a time like a funnel (**P**arentheses $\to$ **E**xponents $\to$ **M**ultiply/**D**ivide left-to-right $\to$ **A**dd/**S**ubtract left-to-right):
1. **Parentheses First:** Compute $(2 + 3) = 5$, rewriting the line as $40 - 3 \times 5^2 \div 5$.
2. **Exponents Next:** Build a $5 \times 5$ square of Counting Tiles to see $5^2 = 25$, rewriting as $40 - 3 \times 25 \div 5$.
3. **Multiply & Divide Left-to-Right:** Multiply $3 \times 25 = 75$, then divide $75 \div 5 = 15$, rewriting as $40 - 15$. *(Never subtract $40 - 3$ first.)*
4. **Subtract Last:** $40 - 15 = \mathbf{25}$.

### Inside-Out RPN Stack Evaluation (Zero Parentheses)
On your SC-6, you can park `40` and `3` safely upstairs on the elevator while you evaluate the innermost group `(2 + 3)²` on the ground floor, or work directly from the inside out:
- **Full 4-Stack Elevator Sequence:** `40 {{key:ENTER}} 3 {{key:ENTER}} 2 {{key:ENTER}} 3 {{key:+}} {{key:x²}} {{key:×}} 5 {{key:÷}} {{key:-}}` $\longrightarrow$ **`25`**.

| What You Are Solving | PEMDAS Paper Funnel | SC-6 Elevator Stack |
| :--- | :--- | :--- |
| **1. Park Outer Numbers & Add `(2 + 3)`** | Rewrite $40 - 3 \times (5)^2 \div 5$ | `40 {{key:ENTER}} 3 {{key:ENTER}} 2 {{key:ENTER}} 3 {{key:+}}` $\to$ `5` in $X$ (`3` in $Y$, `40` in $Z$) |
| **2. Square the Group (`5²`)** | Rewrite $40 - 3 \times 25 \div 5$ | Tap `{{key:x²}}` $\to$ `25` in $X$ |
| **3. Scale & Divide (`3 × 25 ÷ 5`)** | Rewrite $40 - 75 \div 5 \to 40 - 15$ | Tap `{{key:×}} 5 {{key:÷}}` $\to$ `15` in $X$ while `40` drops to $Y$ |
| **4. Final Subtraction (`40 - 15`)** | $40 - 15 = \mathbf{25}$ | Tap `{{key:-}}` $\to$ **`25`**. |

### The Clark's Nutcracker's 30,000-Seed Memory Ledger
In the high alpine forests of the Rocky Mountains, a silver-and-black bird called **Clark's nutcracker** (*Nucifraga columbiana*) performs one of nature's most remarkable feats of spatial working memory. Every autumn, a single nutcracker harvests up to $30,000$ whitebark pine seeds, buries them in thousands of small underground caches across mountain ridges, and remembers their exact locations nine months later under deep winter snow.

How does a bird track its winter pantry? Like a living stack ledger. Suppose a nutcracker buries **9 pine seeds in each of 12 caches** along a granite ridge, finds **15 extra seeds** under a fallen pine log, and eats **28 seeds** during a January blizzard:
$$\text{Remaining Seeds} = 9 \times 12 + 15 - 28 = 95\text{ seeds}$$

Build $12$ rows of $9$ Counting Tiles ($108$), add $15$ ($123$), and remove $28$ ($95$). On your SC-6, the entire seasonal ledger flows across the ground and mezzanine shelves in 10 keystrokes with zero parentheses:
`9 {{key:ENTER}} 12 {{key:×}} 15 {{key:+}} 28 {{key:-}}` $\longrightarrow$ **`95` seeds**.

---

### Common Stack Slips & How to Fix Them

When you are getting used to the 4-level stack, keep these quick rescues in mind:
- **Typed `5`, then `3`, and the screen shows `53`:** Remember that `{{key:ENTER}}` closes the elevator door between your first and second numbers.
- **Entered numbers in reverse order (`4` then `9` instead of `9` then `4`):** Look at the stack before tapping the operator; tap `{{key:x⇄y}}` to swap registers immediately, then tap `{{key:-}}`.
- **Tapped `{{key:C}}` and lost your number:** `{{key:C}}` clears the active shelf; use `{{key:ENTER}}` to lift your number up to Floor $Y$.
- **Wondering if the next number will overwrite your answer:** Do not press Clear after an answer—automatic stack lift pushes your finished total up to Floor $Y$ as soon as you type the next digit.
- **Step counter adds `0` in 4-stack mode:** Use `{{key:REP}}` to fill all four shelves with your step size, or switch to 2-Stack (`2-LV`) mode.
- **Tapped `{{key:+}}` and nothing changed:** You need two numbers on the stack to combine (`Y` and `X`).
- **Division shows a decimal like `3.4` instead of whole groups and leftovers:** Use `{{key:÷R}}` for whole-number division with remainder.
- **Want to verify an answer without re-typing:** Press `{{key:LASTX}}` followed by the opposite operation (for example, after $120 \div 8 = 15$, tapping `{{key:LASTX}} {{key:×}}` restores $120$).

---

## Putting the Stack to Work in Everyday Adventures

Rather than marching through disconnected lists of drill problems, let's step into four connected real-world stories where every calculation builds naturally on the one before it. As you move from an elementary school playground build to a twenty-story robotics tower, a bustling weekend farmer's market, and a state math tournament, watch how numbers ride up and down the four-level stack without a single parenthesis or scrap-paper note.

{{blocks:math_dominoes_pairing|Math Dominoes Studio Doubling and Pairing}}
*Figure 2.2: The Math Dominoes Studio. Domino pips let you spot groups at a glance and build pairs that mirror RPN two-number operations.*

{{blocks:math_dominoes_bridging_12frame|Math Dominoes Studio: Bridging 10 on the 12-Frame Tray ([5|4] = 9 + [3|2] = 5 = 10 + 4 = 14)}}
*Figure 2.3: Bridging 10 on the 12-frame tray. Placing [5|4] = 9 and [3|2] = 5 across the 10-break line physically regroups 9 + 5 into 10 + 4 = 14.*

### The Adventure Playground Construction Crew
Your school is building an adventure playground complete with a two-bay swing set, a cedar perimeter fence, a giant spiral slide, and a monkey-bar climbing dome. As the project engineers, your crew walks from zone to zone laying shock-absorbing bounce tiles, setting fence posts, paving pathways, and weighing cedar woodchips—using your desk blocks and the SC-6 stack to verify every build step.

#### Swing-Bay Bounce Tiles
Your first stop is the two-bay swing set, where your crew is laying interlocking rubber bounce tiles under the swings. You unload 5 blue tiles in the morning, and the delivery truck brings 3 green tiles in the afternoon. How many bounce tiles are ready to snap into place?

Place 5 blue counting tiles on the left side of your desk, and 3 green tiles on the right. Now slide them together into one solid row of 8 tiles. Notice how your calculator's horizontal $Y \mid X$ screen mirrors your desk: pressing `{{key:ENTER}}` slides your morning count (`5`) into the left column ($Y = 5$) so the afternoon delivery (`3`) can sit right beside it ($X = 3$). When you key in `{{res:sc6_02_rpn_for_young_learners_seq_01:keys}}`, the waiting shelf and ground shelf snap together to display **`{{res:sc6_02_rpn_for_young_learners_seq_01:value}}`** bounce tiles ready for the swing bay.

*Pause & Check:* Did you see $Y = 5$ on the left and $X = 3$ on the right before pressing `{{key:+}}`? If your screen shows $53$, you forgot to press `{{key:ENTER}}` to close the elevator door between the two numbers!

#### The Perimeter Fence Post Countdown
With the swing bay cushioned, your crew walks over to the playground border to anchor 9 sturdy cedar fence posts. Before the lunch bell rings, you finish bolting 4 posts firmly into the ground. How many fence posts are still waiting for the afternoon shift?

Line up 9 counting tiles in a row for the fence line, then slide 4 tiles away for the finished posts to see 5 remaining. In Stack Math, subtraction follows a simple left-to-right rule: your **starting total ($9$)** always goes into the left column ($Y$) first, and the **amount you take away ($4$)** goes into the right column ($X$). By pressing `{{res:sc6_02_rpn_for_young_learners_seq_02:keys}}`, you subtract the 4 bolted posts from the 9 starting posts and leave **`{{res:sc6_02_rpn_for_young_learners_seq_02:value}}`** unbolted posts on the ground floor for the afternoon shift.

*Stack Rescue Tip:* What if your fingers accidentally typed `4 {{key:ENTER}} 9` in reverse order? Look at the split screen before pressing minus: $Y$ holds $4$ and $X$ holds $9$. On the SC-6, you never have to erase and re-type! Simply tap `{{key:x⇄y}}` to swap the two shelves into their proper seats ($Y = 9,\; X = 4$), then tap `{{key:-}}` to get $5$. And right after subtracting, tap `{{key:LASTX}} {{key:+}}` to bring back the $4$ finished posts and prove $5 + 4 = 9$.

#### Spiral-Slide Border Pavers
After lunch, your crew moves to the center of the playground to pave the landing zone around the giant spiral slide using 23 rubber pavers, plus another 14 pavers around the balance-beam pit. Now that we are working with two-digit numbers, how can we see the tens and ones combine before we press `{{key:+}}`?

On your **Place Value Studio Whole Numbers Tray**, dock `2` in `TENS` and `3` in `ONES` for the top row ($23$), and `1` in `TENS` and `4` in `ONES` for the bottom row ($14$). Just like Registers $Y$ and $X$, the two rows of your tray let you combine the tens column ($20 + 10 = 30$) and the ones column ($3 + 4 = 7$) to see $37$ at a glance. Now lift the spiral-slide pavers onto Shelf $Y$ and bring in the balance-beam pavers by pressing `{{res:sc6_02_rpn_for_young_learners_seq_09:keys}}`, which unites both paving zones into **`{{res:sc6_02_rpn_for_young_learners_seq_09:value}}`** on Ground Shelf $X$. *(Try tapping `{{key:LASTX}} {{key:-}}` right after—watch `14` jump back into $X$ and subtract to restore `23`!)*

#### Monkey-Bar Cushion Woodchips & The Instant Undo Check
For the final job on the playground, your crew wheels soft cedar woodchips beneath the monkey bars. The first wheelbarrow delivers $47\text{ kg}$ of woodchips, and the second brings $36\text{ kg}$. Unlike the pavers around the spiral slide, here the ones digits ($7 + 6 = 13$) overflow past 10! What is the total mass of woodchips, and how can you prove your regrouping is $100\%$ right without re-typing a single number?

Model 47 (`4` tens, `7` ones) and 36 (`3` tens, `6` ones) on your **Place Value Tray** with `+1` regrouping blocks: the $7 + 6 = 13$ ones trade 10-for-1 to add $+1$ to the `TENS` column and leave `3` in `ONES`, giving 8 tens and 3 ones ($83$). To combine both wheelbarrows on the stack and immediately verify the sum by subtracting the second load back out, press `{{res:sc6_02_rpn_for_young_learners_seq_10:keys}}`, which reaches $83\text{ kg}$ and then uses `{{key:LASTX}}` to restore the original **`{{res:sc6_02_rpn_for_young_learners_seq_10:value}}`** kg on Ground Shelf $X$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `47` | 0 | 0 | 0 | 47 |
| `{{key:ENTER}}` | 0 | 0 | 47 | 47 |
| `36` | 0 | 0 | 47 | 36 |
| `{{key:+}}` | 0 | 0 | 0 | 83 |
| `{{key:LASTX}}` | 0 | 0 | 83 | 36 |
| `{{key:-}}` | 0 | 0 | 0 | 47 |

**Why `{{key:LASTX}}` Saves Every Keystroke:** Look at row 5 of the table—you didn't have to type `3` and `6` again! Tapping `{{key:LASTX}}` pulled `36` straight out of backup memory and lifted `83` to Floor $Y$, so one tap of `{{key:-}}` proved $83 - 36 = 47$.

### The Sky-Tower Space Elevator Express
Having mastered the ground and waiting shelves on the playground, you are promoted to chief dispatch controller for a 20-story Sky-Tower & Robotics Center! Here your mission is to track heavy cargo lifts, ride a doubling cascade of laser scanners, chain three-stop passenger shuttles using automatic stack lift, and equip robot pit crews at the summit.

#### Unloading the Heavy Cargo Lift
Your shift begins at the ground-floor loading dock, where a heavy cargo lift starts upward carrying $83\text{ kg}$ of robot frame parts. At Floor 4, the build team unloads $36\text{ kg}$ of aluminum beams. How many kilograms of parts stay inside the lift?

Look closely at those numbers ($83 - 36$): they are the exact partner numbers from the woodchip challenge beneath the monkey bars! On your **Place Value Tray**, unbundle 1 ten from the `TENS` column into ten `+1` regrouping blocks in the `ONES` column (making 7 tens and 13 ones), then remove 3 tens and 6 ones to leave 4 tens and 7 ones ($47$). When you place the starting $83\text{ kg}$ load on Shelf $Y$ and subtract the $36\text{ kg}$ unloaded at Floor 4 by pressing `{{res:sc6_02_rpn_for_young_learners_seq_11:keys}}`, the ground shelf immediately shows **`{{res:sc6_02_rpn_for_young_learners_seq_11:value}}`** kg of cargo remaining inside the lift. Tap `{{key:LASTX}} {{key:+}}` right afterwards to load the $36\text{ kg}$ of aluminum beams back on and verify $47 + 36 = 83$.

#### The Laser-Grid Doubling Cascade
Next, you switch to the express turbo-lift shaft, where a laser safety scanner **doubles** its active beams on every floor rise. Starting with $2$ laser beams at Floor 1, how many beams are scanning by Floor 5?

Why would typing `2 + 2`, then `+ 4`, then `+ 8`, then `+ 16` be slow and tiring? Because on your SC-6, pressing `{{key:ENTER}}` automatically makes an identical twin copy of whatever number sits on Shelf $X$! That means tapping `{{key:ENTER}} {{key:+}}` doubles *any* number in two quick clicks. Place 2 tiles on your desk, double them to 4, then 8, then 16, and ride the two-key doubling rhythm (`{{key:ENTER}} {{key:+}}`) four times in a row on your SC-6: pressing `{{res:sc6_02_rpn_for_young_learners_seq_13:keys}}` clones and fuses each floor's beam count until Ground Shelf $X$ reaches **`{{res:sc6_02_rpn_for_young_learners_seq_13:value}}`** laser beams at Floor 5.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `2` | 0 | 0 | 0 | 2 |
| `{{key:ENTER}} {{key:+}}` | 0 | 0 | 0 | 4 |
| `{{key:ENTER}} {{key:+}}` | 0 | 0 | 0 | 8 |
| `{{key:ENTER}} {{key:+}}` | 0 | 0 | 0 | 16 |
| `{{key:ENTER}} {{key:+}}` | 0 | 0 | 0 | 32 |

#### Three-Stop Sky-Shuttle Boarding
Now the morning science fair rush begins! The passenger sky-shuttle picks up 15 passengers at the underground train station, 24 passengers at the main atrium, and 31 passengers at the botanical sky-deck. How do you add three stops in a row—and why do you only press `{{key:ENTER}}` **once** at the very beginning?

First, spot a neat mental-math pattern in the ones digits: $5 + 4 + 1 = 10$. Now watch **automatic stack lift** do the heavy lifting after the first addition: once `15 {{key:ENTER}} 24 {{key:+}}` produces `39` on Shelf $X$, typing `31` automatically lifts `39` up to Shelf $Y$ without needing another `{{key:ENTER}}`. Keying in `{{res:sc6_02_rpn_for_young_learners_seq_14:keys}}` chains all three boarding stops into a single smooth tally of **`{{res:sc6_02_rpn_for_young_learners_seq_14:value}}`** passengers.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `15` | 0 | 0 | 0 | 15 |
| `{{key:ENTER}}` | 0 | 0 | 15 | 15 |
| `24` | 0 | 0 | 15 | 24 |
| `{{key:+}}` | 0 | 0 | 0 | 39 |
| `31` | 0 | 0 | 39 | 31 |
| `{{key:+}}` | 0 | 0 | 0 | 70 |

#### Walkie-Talkie Team Distribution
When the 70-passenger shuttle reaches the top-floor robotics arena, the tournament director opens a crate of 24 walkie-talkies and splits them equally among 4 pit-crew stations. How many walkie-talkies does each pit crew get?

Deal your 24 counting tiles into 4 equal piles on your desk to see 6 tiles in each pile—proving with your hands that division is just multiplication (`4 × 6 = 24`) run in reverse. Just like subtraction, the starting total (`24`) goes into the left column ($Y$) and the number of groups (`4`) goes into the right column ($X$): pressing `{{res:sc6_02_rpn_for_young_learners_seq_19:keys}}` divides the crate evenly to show **`{{res:sc6_02_rpn_for_young_learners_seq_19:value}}`** walkie-talkies per pit crew. *(Tap `{{key:LASTX}} {{key:×}}` right after to multiply `6` by `4` and restore all `24` radios without re-typing!)*

### The Weekend Maker Fair & Farmer's Market Quest
At the top of the Sky-Tower, 24 walkie-talkies divided into 4 groups with zero leftovers. But what happens in the real world when numbers *don't* divide evenly—or when you buy two different treats at two different booths? With your weekend market pouch in hand, you stroll through the Maker Fair & Farmer's Market to master whole-number remainders (`{{key:÷R}}`), receipt checks (`{{key:LASTX}}`), backwards-entry rescues (`{{key:x⇄y}}`), and two-booth subtotals using Floor $Z$.

#### The Leftover Sourdough Roll Mystery
Your first stop at the market is the brick-oven bakery, where the baker pulls 17 warm sourdough rolls from the oven and packs them into bags of 5 rolls each. How many bags are filled completely, and how many warm rolls are left over for the baker's snack?

If you typed $17 \div 5$ on a regular calculator, it would say `3.4`—which doesn't tell you how many loose rolls are sitting on the counter! Instead, deal 17 counting tiles into piles of 5 on your desk: you get **3 full piles of 5** ($15$ tiles) and **2 loose tiles** left over. Now watch **Quotient & Remainder (`{{key:÷R}}`)** put the full bags in Register $X$ and the leftover rolls in Register $Y$ at the exact same time: when you key in `{{res:sc6_02_rpn_for_young_learners_seq_21:keys}}`, `{{key:÷R}}` splits the 17 rolls into 3 full bags and 2 leftovers before `{{key:x⇄y}}` swaps **`{{res:sc6_02_rpn_for_young_learners_seq_21:value}}`** into Ground Shelf $X$ so you can inspect the leftover rolls.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `17` | 0 | 0 | 0 | 17 |
| `{{key:ENTER}}` | 0 | 0 | 17 | 17 |
| `5` | 0 | 0 | 17 | 5 |
| `{{key:÷R}}` | 0 | 0 | 2 | 3 |
| `{{key:x⇄y}}` | 0 | 0 | 3 | 2 |

Register $X$ first shows Quotient $Q = 3$ full bags while Register $Y$ holds Remainder $R = 2$ loose rolls, and tapping `{{key:x⇄y}}` swaps them so you can inspect the 2 leftover rolls up front. *(Notice that if every single roll must go inside a bag, you need $3 + 1 = 4\text{ bags}$.)*

#### Heritage Blue-Shell Egg Cartons
Next door to the bakery is the heritage farm stand, where a basket of 125 blue-shell pasture eggs is being packed into specialty cartons holding 8 eggs each. How many 8-egg cartons are filled completely, and how many eggs remain in the basket?

Here again, a decimal like `15.625` would be completely useless—because you can't sell `0.625` of a raw egg! To split the 125 eggs into 8-egg cartons and check the remainder, press `{{res:sc6_02_rpn_for_young_learners_seq_22:keys}}`, which first places 15 full cartons in Register $X$ with 5 leftover eggs waiting on Floor $Y$, and then swaps **`{{res:sc6_02_rpn_for_young_learners_seq_22:value}}`** into Register $X$. *(Want to prove $15 \times 8 + 5 = 125$ with zero re-typing? Right after `{{key:÷R}}`, tap `{{key:LASTX}} {{key:×}} {{key:+}}` and watch `125` reappear!)*

#### Honeycrisp Cider Crate Detective Check
Walking past the egg stand, you help the orchard master check an invoice for 15 wooden crates of Honeycrisp apple cider at $\$8.00$ per crate ($15 \times \$8.00 = \$120.00$). How can you prove the $\$120.00$ receipt is $100\%$ accurate without re-typing a single digit?

Model 2 rows of 8 tiles ($16$) on your desk and divide by 8 to see that dividing by the row width always brings back the number of rows. Now multiply the 15 cider crates by $\$8$ and let `{{key:LASTX}}` reverse-check the invoice by dividing by `8`: pressing `{{res:sc6_02_rpn_for_young_learners_seq_23:keys}}` computes the $\$120$ invoice and immediately divides by the recalled $\$8$ unit price to restore **`{{res:sc6_02_rpn_for_young_learners_seq_23:value}}`** crates on Ground Shelf $X$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `15` | 0 | 0 | 0 | 15 |
| `{{key:ENTER}}` | 0 | 0 | 15 | 15 |
| `8` | 0 | 0 | 15 | 8 |
| `{{key:×}}` | 0 | 0 | 0 | 120 |
| `{{key:LASTX}}` | 0 | 0 | 120 | 8 |
| `{{key:÷}}` | 0 | 0 | 0 | 15 |

#### The Backwards-Number Rescue (`{{key:x⇄y}}`)
At the next booth, the smoothie maker wants to pour a 24-ounce tub of frozen berry mix equally into 8 tasting cups ($24 \div 8 = 3$). In your excitement, your fingers accidentally typed the `8` first (`8 {{key:ENTER}} 24`)!

On a regular calculator, typing a division problem backward means hitting Clear and starting all over. On the SC-6, look at the horizontal split screen: `8` is sitting in $Y$ and `24` is sitting in $X$. One tap of `{{key:x⇄y}}` swaps them into their proper seats before you press `{{key:÷}}`: when you run `{{res:sc6_02_rpn_for_young_learners_seq_24:keys}}`, the swap key puts `24` into the left seat ($Y$) and `8` into the right seat ($X$) so division cleanly yields **`{{res:sc6_02_rpn_for_young_learners_seq_24:value}}`** ounces per cup.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `8` | 0 | 0 | 0 | 8 |
| `{{key:ENTER}}` | 0 | 0 | 8 | 8 |
| `24` | 0 | 0 | 8 | 24 |
| `{{key:x⇄y}}` | 0 | 0 | 24 | 8 |
| `{{key:÷}}` | 0 | 0 | 0 | 3 |

Never start over when you type numbers in reverse order—just tap `{{key:x⇄y}}` and divide!

#### The Two-Booth Snack Combo (Unlocking Floor $Z$)
Hungry from your market tour, you stop at the food court to buy **3 warm pretzel twists at $\$4.00$ each** AND **2 mango smoothies at $\$5.00$ each**. On a basic calculator, typing `3 × 4 + 2 × 5` gives the wrong answer unless you write down the first subtotal or use parentheses. How does the SC-6's **third-floor loft (Register $Z$)** solve the whole bill with zero parentheses and zero scratch paper?

Build two tile arrays on your desk: a $3 \times 4$ array ($12$) and a $2 \times 5$ array ($10$). Now watch what happens in row 6 of the stack table below: as soon as you type `2 {{key:ENTER}} 5` for the smoothies, your $\$12$ pretzel subtotal rides the elevator up to **Floor $Z$**, waiting safely until the $\$10$ smoothie total finishes on Floor $X$. Pressing `{{res:sc6_02_rpn_for_young_learners_seq_26:keys}}` brings both booth subtotals together on the bottom two shelves and combines them into **`{{res:sc6_02_rpn_for_young_learners_seq_26:value}}`** dollars in all.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `3` | 0 | 0 | 0 | 3 |
| `{{key:ENTER}}` | 0 | 0 | 3 | 3 |
| `4` | 0 | 0 | 3 | 4 |
| `{{key:×}}` | 0 | 0 | 0 | 12 |
| `2` | 0 | 0 | 12 | 2 |
| `{{key:ENTER}}` | 0 | 12 | 2 | 2 |
| `5` | 0 | 12 | 2 | 5 |
| `{{key:×}}` | 0 | 0 | 12 | 10 |
| `{{key:+}}` | 0 | 0 | 0 | 22 |

**Pause & Look at Row 8:** Right before you press `{{key:+}}`, Floor $Y$ shows your $\$12$ pretzels and Floor $X$ shows your $\$10$ smoothies side by side!

### The Junior Math Olympiad Sprint
Now that you saw Floor $Z$ hold your pretzel subtotal at the market food court, you are ready for the state **Junior Math Olympiad**! The tournament clock is ticking. While other teams fumble with nested parentheses and scrap paper, you will spin the 4-story stack carousel, chain two-bracket expressions from the inside out, and solve geometric area puzzles in seconds.

#### Spinning the 4-Story Carousel (`{{key:R↓}}`)
Before the first tournament buzzer sounds, the head judge asks every competitor to prove they can inspect all four shelves of their stack without erasing a single number. Load `10`, `20`, `30`, and `40` onto the four shelves of your elevator, then spin them around the 4-level carousel using **Roll Down (`{{key:R↓}}`)**: when you key in `{{res:sc6_02_rpn_for_young_learners_seq_31:keys}}`, each tap of `{{key:R↓}}` brings the next shelf down to the ground floor until all four numbers return to their starting seats with **`{{res:sc6_02_rpn_for_young_learners_seq_31:value}}`** back on Ground Shelf $X$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `10` | 0 | 0 | 0 | 10 |
| `{{key:ENTER}}` | 0 | 0 | 10 | 10 |
| `20` | 0 | 0 | 10 | 20 |
| `{{key:ENTER}}` | 0 | 10 | 20 | 20 |
| `30` | 0 | 10 | 20 | 30 |
| `{{key:ENTER}}` | 10 | 20 | 30 | 30 |
| `40` | 10 | 20 | 30 | 40 |
| `{{key:R↓}}` | 40 | 10 | 20 | 30 |
| `{{key:R↓}}` | 30 | 40 | 10 | 20 |
| `{{key:R↓}}` | 20 | 30 | 40 | 10 |
| `{{key:R↓}}` | 10 | 20 | 30 | 40 |

**The 4-Click Carousel Secret:** Because there are 4 floors ($T, Z, Y, X$), pressing `{{key:R↓}}` 4 times brings every passenger right back to its starting floor!

#### The Zero-Parenthesis Tournament Sprint
*BZZZT!* Round 1 flashes on the scoreboard: evaluate $(15 - 3) \times (4 + 2) \div 6$. Just like the pretzel-and-smoothie combo at the market, you compute the first group ($15 - 3 = 12$), let `12` ride upstairs to Floor $Z$ while you compute the second group ($4 + 2 = 6$), and then multiply and divide with zero parentheses: pressing `{{res:sc6_02_rpn_for_young_learners_seq_33:keys}}` fuses `12` and `6` into `72` and divides by `6` to land on **`{{res:sc6_02_rpn_for_young_learners_seq_33:value}}`**.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `15` | 0 | 0 | 0 | 15 |
| `{{key:ENTER}}` | 0 | 0 | 15 | 15 |
| `3` | 0 | 0 | 15 | 3 |
| `{{key:-}}` | 0 | 0 | 0 | 12 |
| `4` | 0 | 0 | 12 | 4 |
| `{{key:ENTER}}` | 0 | 12 | 4 | 4 |
| `2` | 0 | 12 | 4 | 2 |
| `{{key:+}}` | 0 | 0 | 12 | 6 |
| `{{key:×}}` | 0 | 0 | 0 | 72 |
| `6` | 0 | 0 | 72 | 6 |
| `{{key:÷}}` | 0 | 0 | 0 | 12 |

**Look at Row 8:** The first bracket ($12$) is waiting on Floor $Y$ while the second bracket ($6$) finishes on Floor $X$. Zero parentheses needed!

#### The Twin-Difference Showdown
Round 2 tests whether you can divide one bracketed difference by another: $(24 - 8) \div (6 - 2)$. Watch how the first difference ($24 - 8 = 16$) rides upstairs to Floor $Z$, then drops right back into the left seat (Floor $Y$) the moment the second difference ($6 - 2 = 4$) finishes on Floor $X$: keying in `{{res:sc6_02_rpn_for_young_learners_seq_34:keys}}` divides `16` on Shelf $Y$ by `4` on Shelf $X$ to display **`{{res:sc6_02_rpn_for_young_learners_seq_34:value}}`**.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `24` | 0 | 0 | 0 | 24 |
| `{{key:ENTER}}` | 0 | 0 | 24 | 24 |
| `8` | 0 | 0 | 24 | 8 |
| `{{key:-}}` | 0 | 0 | 0 | 16 |
| `6` | 0 | 0 | 16 | 6 |
| `{{key:ENTER}}` | 0 | 16 | 6 | 6 |
| `2` | 0 | 16 | 6 | 2 |
| `{{key:-}}` | 0 | 0 | 16 | 4 |
| `{{key:÷}}` | 0 | 0 | 0 | 4 |

When the final `{{key:÷}}` key drops the stack, Ground Shelf $X$ shows `4`—and if you tap `{{key:LASTX}} {{key:×}}` right after, the calculator multiplies $4 \times 4$ to bring `16` right back!

#### Three-Branch Relay Race
In Round 3, the judges combine addition, subtraction, multiplication, and division into one relay expression: $(18 + 6) \times (10 - 5) \div 12$. Because your hands now know the elevator rhythm—solve the first bracket, solve the second bracket, fuse them, and divide—you can glide through all 11 keystrokes in one continuous flow by pressing `{{res:sc6_02_rpn_for_young_learners_seq_35:keys}}` to reach **`{{res:sc6_02_rpn_for_young_learners_seq_35:value}}`**.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `18` | 0 | 0 | 0 | 18 |
| `{{key:ENTER}}` | 0 | 0 | 18 | 18 |
| `6` | 0 | 0 | 18 | 6 |
| `{{key:+}}` | 0 | 0 | 0 | 24 |
| `10` | 0 | 0 | 24 | 10 |
| `{{key:ENTER}}` | 0 | 24 | 10 | 10 |
| `5` | 0 | 24 | 10 | 5 |
| `{{key:-}}` | 0 | 0 | 24 | 5 |
| `{{key:×}}` | 0 | 0 | 0 | 120 |
| `12` | 0 | 0 | 120 | 12 |
| `{{key:÷}}` | 0 | 0 | 0 | 10 |

Watching the table from top to bottom, `24` and `5` multiply into `120` on the ground shelf before dividing by `12` to finish cleanly at `10`.

#### The Castle Courtyard Moat (Difference of Squares)
Round 4 is the Geometry Lightning Puzzle: a square castle courtyard measures $15\text{ ft} \times 15\text{ ft}$ on the outside, with a central $9\text{ ft} \times 9\text{ ft}$ fountain pool inside. How many square feet of stone paving surround the fountain?

Instead of typing `15 {{key:ENTER}} 15 {{key:×}}`, use the dedicated **Square Key (`{{key:x²}}`)** (`{{key:f}}` then `{{key:x²}}`). Notice how `15 {{key:x²}}` turns `15` into `225` right on Shelf $X$, and typing `9` automatically lifts `225` to Shelf $Y$ while you square `9`: pressing `{{res:sc6_02_rpn_for_young_learners_seq_37:keys}}` subtracts the $81\text{ sq ft}$ fountain from the $225\text{ sq ft}$ courtyard to leave **`{{res:sc6_02_rpn_for_young_learners_seq_37:value}}`** square feet of stone paving.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `15` | 0 | 0 | 0 | 15 |
| `{{key:x²}}` | 0 | 0 | 0 | 225 |
| `9` | 0 | 0 | 225 | 9 |
| `{{key:x²}}` | 0 | 0 | 225 | 81 |
| `{{key:-}}` | 0 | 0 | 0 | 144 |

**Math Mystery Bonus:** Notice that $225 - 81 = 144$, which is $12^2$! You just discovered the famous $9\text{–}12\text{–}15$ right-triangle family.

#### The Treasure Vault Instant Undo (`{{key:LASTX}}`)
After winning the Olympiad trophy, your math club opens its $\$120.00$ treasure vault to buy a $\$45.00$ telescope lens (`120 {{key:ENTER}} 45 {{key:-}}` $\to \$75.00$). Just as you subtract the $\$45.00$, the school principal announces that a science grant paid for the lens! How do you undo the subtraction and restore your $\$120.00$ balance without typing `45` again?

Use `{{key:LASTX}}` to pull `45` right back out of memory and tap `{{key:+}}`: running the sequence `{{res:sc6_02_rpn_for_young_learners_seq_40:keys}}` subtracts the $\$45$ lens and then immediately reunites `$75` on Shelf $Y$ with the recalled `$45` on Shelf $X$ to restore **`{{res:sc6_02_rpn_for_young_learners_seq_40:value}}`** dollars.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `120` | 0 | 0 | 0 | 120 |
| `{{key:ENTER}}` | 0 | 0 | 120 | 120 |
| `45` | 0 | 0 | 120 | 45 |
| `{{key:-}}` | 0 | 0 | 0 | 75 |
| `{{key:LASTX}}` | 0 | 0 | 75 | 45 |
| `{{key:+}}` | 0 | 0 | 0 | 120 |

With those two final clicks (`{{key:LASTX}} {{key:+}}`), your club's initial $\$120.00$ vault balance is completely restored without re-typing a single digit.

---

## Where to Go Next: Companion Workbook Quests & Kitchen-Table Challenges

> *For 21 additional worked problems with full 4-register stack tables, see Chapter 2 of the [SC-6 Elementary Companion Problem & Activity Workbook](../../curriculum/sc6-elementary-companion-workbook.md).*

Want to turn these stack habits into rapid reflexes? Open the **[Big Ideas Math Middle School Supplement](../../curriculum/big-ideas-middle-school-sc6-workbook.md) — Unit 1: Numerical Expressions & Factors, Section 1.3 (Order of Operations)**, along with your **StackCalc Student Workbook & 12-Unit Curriculum Guide** (Unit 2: *Riding the 4-Level Number Elevator & Parenthesis-Free Chains*), or challenge your family at the dinner table tonight:

1. **PEMDAS Funnel vs. RPN Inside-Out Showdown:** Write $40 - 3 \times (2 + 3)^2 \div 5$ on a napkin. First solve it on paper using the **PEMDAS Funnel** (watching out for the $40 - 3 = 37$ trap), then race an adult using their phone calculator while you evaluate `40 {{key:ENTER}} 3 {{key:ENTER}} 2 {{key:ENTER}} 3 {{key:+}} {{key:x²}} {{key:×}} 5 {{key:÷}} {{key:-}}` $\to \mathbf{25}$.
2. **Hands-On Explorer — Clark's Nutcracker Seed-Cache Ledger & `{{key:LASTX}}` Detective:** Model the **Clark's Nutcracker Seed-Cache Ledger** (`9 {{key:ENTER}} 12 {{key:×}} 15 {{key:+}} 28 {{key:-}}` $\to \mathbf{95}$ seeds), then hand your SC-6 to a partner showing only `95` on Floor $X$. Have them tap `{{key:LASTX}} {{key:+}}` to uncover the 28 eaten seeds and restore all `123` cached seeds!
3. **Workbook & Timed Proficiency Trial:** Complete **Unit 1, Section 1.3 (Practice Sheets A & B)** in the **Big Ideas Math Middle School Supplement** and **Unit 2 Quest Sheets 2A–2D** in the Companion Student Workbook, then run **Timed Proficiency Trial #2** (Parenthesis-Free Relay & `1089` Mind-Reader Proof).

---

## Chapter Summary & Looking Ahead

The core mechanics of **Stack Math** (Reverse Polish Notation) on the SC-6 rest on five principles:
1. **The Golden Rule of Stack Math:** Always place your two numbers onto the stack first, and tap the action button (`{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`) last.
2. **The 4-Story Number Elevator ($T, Z, Y, X$):** Watching `{{key:ENTER}}` push numbers upward from Floor $X$ to Floor $Y$ while earlier subtotals wait safely on Floors $Z$ and $T$.
3. **Automatic Stack Lift & Drop:** Seeing completed results automatically lift to Floor $Y$ when you type the next number, and drop down cleanly when an operator fuses $Y$ and $X$.
4. **Mistake-Proof Stack Controls:** Fixing typing slips with `{{key:<-}}`, swapping order-sensitive subtraction or division pairs with `{{key:x⇄y}}`, rotating all four shelves with `{{key:R↓}}`, and checking or undoing work without re-typing via `{{key:LASTX}}`.
5. **Parenthesis-Free Multi-Step Expressions:** Solving multi-branch problems from the inside out without pressing a single parenthesis key or reaching for scratch paper.

Now that you've mastered pushing numbers onto the stack, swapping registers, and dropping calculations cleanly, turn the page to **[Chapter 03: Counting, Number Sense & Place Value](03-counting-place-value.md)**—where we will travel back in time to discover how ancient pebble counters and ten human fingers created zero and the power of place value.
