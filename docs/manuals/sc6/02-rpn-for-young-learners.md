---
title: "Chapter 2: How Stack Math Works: Stacking Numbers Just Like Blocks"
description: "Master Stack Math on the SC-6: stacking numbers on a 4-level stack, leaving behind the confusing equals sign, and solving multi-step problems with zero parentheses."
---

# Chapter 2: How Stack Math Works: Stacking Numbers Just Like Blocks

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">STACK MATH FOUNDATIONS // CHAPTER 02</span>
  <span class="te-viewport-status text-emerald-400">● 4-LEVEL NUMBER STACK &bull; ZERO EQUALS SIGN &bull; 4-LVL vs 2-LVL</span>
</div>

## The Equals-Sign Trap vs. The Stack Ladder

Have you ever wondered why school worksheets always put an equals sign (`=`) at the end of a problem like $4 + 3 = \underline{\hspace{0.5cm}}$?

After a few years of filling in those blanks, it is easy to fall into the **Equals-Sign Trap**! When you see an equals sign on every worksheet, you might start believing that `=` means *"do the math right now and write the answer here!"*

Then one day, a teacher writes an open puzzle on the board with the box in the middle:
$$5 + \Box = 12 \quad \text{or} \quad 8 = 3 + 5$$
Half the class writes $17$ in the box! Why? Because their eyes dart across $5$, $+$, and $12$, and their fingers immediately calculate $5 + 12 = 17$. They didn't read the equation as a balanced seesaw where both sides must weigh the exact same amount—they treated the equals sign as an emergency "go" button!

Now think about what **you** do in the real world when you build with physical blocks:
Suppose you have **5 blue blocks** resting on your desk, and your friend hands you **3 red blocks**. How do you put them together?
You don't wave a magic wand and shout *"Equals!"* You simply slide the 3 red blocks straight into the 5 blue blocks. **Putting them together IS the answer (`8`)!**

Here is the secret of **Stack Math**: **your brain doesn't think in parentheses and equals signs—your brain naturally stacks physical objects.**
- When you pack your backpack, you place your heavy binder on the bottom shelf, then stack your lunchbox on top.
- When you bake cookies, you weigh the flour into the bowl, crack an egg on top, and stir them together.
- When you stack blocks, pancakes, or books, each new item rests on top of the stack.

That is how **Stack Math** works on your **StackCalc SC-6**:
1. Type the first number (`5`) and press `{{key:ENTER}}` to push it onto the waiting shelf (Level $Y$).
2. Type the second number (`3`) on the ground shelf (Level $X$).
3. Tap `{{key:+}}`—and *SNAP!* The upper shelf drops down, fusing the two numbers into `8` right before your eyes!

Instead of wrestling with parentheses, syntax errors, and misleading equals signs, on the SC-6 you keep a clear, visible stack of numbers that you can combine, separate, and inspect at any time.

<div class="p-4 rounded-xl bg-slate-900 border border-emerald-500/30 my-6 font-mono text-xs text-emerald-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>{{key:NUM}}</code> (Standard Base-10 Arithmetic &bull; 4-Stack XYZT &bull; Clean Display)
</div>

<div class="admonition note">
<p class="admonition-title">Unlocked Keycaps Ribbon — Grades K–1 Foundation</p>
<p>
• <strong>Numeric Entry:</strong> Digits <code>{{key:0}}</code> through <code>{{key:9}}</code>.<br>
• <strong>Stack Actions:</strong> <code>{{key:ENTER}}</code> (Stack Lift / Push Up), <code>{{key:C}}</code> (Clear), <code>{{key:&lt;-}}</code> (Backspace), <code>{{key:x⇄y}}</code> (Swap), <code>{{key:R↓}}</code> (Roll Down), <code>{{key:REP}}</code> (Repeat Operation), <code>{{key:LASTX}}</code> (Recover Last Number).<br>
• <strong>Basic Arithmetic:</strong> <code>{{key:+}}</code> (Combine / Add), <code>{{key:-}}</code> (Remove / Subtract), <code>{{key:×}}</code> (Multiply), <code>{{key:÷}}</code> (Divide).<br>
• <strong>Visual Sandboxes (Introduced in Chapter 3):</strong> <code>{{key:▦}}</code> Ten-Frame, <code>{{key:COUNT}}</code> Step Counter / Bead Rack, <code>{{key:LINE}}</code> Number Line, <code>{{key:PV}}</code> Place Value.<br>
• <strong>Stack Configuration:</strong> <code>{{key:FLAGS}}</code> (Cycle <code>2-LV</code> / <code>4-LV</code> / <code>8-LV</code>), Flag 5 (Dual Stack $Y \mid X$ vs Single Stack $X$).
</p>
</div>

---


## Stacking Numbers: The 4-Level Number Stack ($T, Z, Y, X$)

To picture how your SC-6 holds numbers inside its memory, imagine a stack of four sturdy shelves—the **4-Level Number Stack** (you can also picture it as a four-story number tower or elevator):

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
   When your first number is entered, tapping `{{key:ENTER}}` pushes it up to Level $Y$ (like an elevator rising to the second floor), leaving an identical copy ready on Level $X$ so you can type your next number!
3. **Rule 3: Pressing an Operator Key (`+`, `-`, `×`, `÷`) Drops the Stack Down.**  
   When you tap an operational key such as `{{key:+}}`, the upper shelf drops down! The number on Level $Y$ combines with the number on Level $X$, and their combined total remains on the ground shelf ($X$). Level $Y$ is now ready for future numbers.

| Stack Level | Before Pressing `{{key:+}}` | Action During `{{key:+}}` | After Pressing `{{key:+}}` |
| :--- | :---: | :--- | :---: |
| **Level 2 (`Y`)** | `3` | Drops down to combine with Level 1 | `0` |
| **Level 1 (`X`)** | `4` | Receives $3 + 4$ | **`7`** |

### Automatic Stack Lift Mechanics
One of the most elegant secrets of Stack Math is **automatic stack lift**. When an operation completes and leaves its answer in Register $X$, typing a new number does **NOT** overwrite your result. Instead, the calculator hardware automatically lifts the result up into Register $Y$ to make room for your new input!

> **AUTOMATIC STACK LIFT ON NUMBER ENTRY**
>
> State after 4 {{key:ENTER}} 5 {{key:+}} -> X = 9. Now, you type 6:
>
> BEFORE typing 6:             DURING typing 6:           AFTER typing 6:  
> T: {{key:0}}                     T: {{key:0}}                   T: {{key:0}}  
> Z: {{key:0}}                     Z: {{key:0}}                   Z: {{key:0}}  
> Y: {{key:0}}                     Y: {{key:9}}  <-- (Lifts up!)  Y: {{key:9}}  
> X: {{key:9}}  (prior answer)     X: [   ]                   X: {{key:6}}  

### Two-Number Stack Drop Mechanics & $T$-Register Replication
When any binary (two-number) operation executes (`+`, `-`, `×`, `÷`):
1. The values in $Y$ and $X$ are evaluated: $Y \text{ op } X$.
2. The result is written into $X$.
3. Register $Z$ drops down into Register $Y$.
4. Register $T$ drops down into Register $Z$.
5. **The $T$-Register Invariant:** The value in Register $T$ **duplicates itself**, remaining in Register $T$! 

This top-register replication is what allows the SC-6 to execute infinite skip-counting and constant multiplication without needing dedicated storage registers.

---

## Why Combining Numbers IS the Answer (Zero Parentheses!)

<div class="admonition tip">
<p class="admonition-title">The RPN Superpower Rule</p>
<p>
On the StackCalc SC-6, you never wait for an equals sign. The moment you press <code>{{key:+}}</code>, <code>{{key:-}}</code>, <code>{{key:×}}</code>, or <code>{{key:÷}}</code>, the numbers on Level 1 ($X$) and Level 2 ($Y$) combine immediately!
</p>
</div>

Watch how fast you can crush a 5th-grade order-of-operations monster without writing down a single scrap-paper note or pressing a single parenthesis key:

$$(15 - 3) \times (4 + 2) \div 6 = 12$$

- **Step 1 (First group):** Tap `15` `{{key:ENTER}}` `3` `{{key:-}}` $\longrightarrow$ **`12`** is ready!
- **Step 2 (Second group):** Tap `4` `{{key:ENTER}}` `2` `{{key:+}}` $\longrightarrow$ **`6`** is on Level 1 ($X$), while **`12`** waits safely upstairs on Level 2 ($Y$)!
- **Step 3 (Multiply & Divide):** Tap `{{key:×}}` (making `72`), then tap `6` `{{key:÷}}` $\longrightarrow$ **`{{res:sc6_order_of_ops:value}}`**!

Complete verified sequence: `{{res:sc6_order_of_ops:keys}}` $\longrightarrow$ **`{{res:sc6_order_of_ops:value}}`**.

| Keystroke | Register T (Roof Floor) | Register Z (Loft Floor) | Register Y (Mezzanine) | Register X (Ground Flr) |
| :--- | :--- | :--- | :--- | :--- |
| 15 | 0 | 0 | 0 | 15 |
| {{key:ENTER}} | 0 | 0 | 15 | 15 |
| 3 | 0 | 0 | 15 | 3 |
| {{key:-}} | 0 | 0 | 0 | 12 |
| 4 | 0 | 0 | 12 | 4 |
| {{key:ENTER}} | 0 | 12 | 4 | 4 |
| 2 | 0 | 12 | 4 | 2 |
| {{key:+}} | 0 | 0 | 12 | 6 |
| {{key:×}} | 0 | 0 | 0 | 72 |
| 6 | 0 | 0 | 72 | 6 |
| {{key:÷}} | 0 | 0 | 0 | 12 |

{{res:sc6_order_of_ops:screenshot|SC-6 Parenthesis-Free Order of Operations: (15 - 3) x (4 + 2) / 6 = 12}}

### Algebraic Trap vs. StackCalc Superpower Showdown: Order of Operations

| Challenge / Equation | The Algebraic Calculator Trap (TI-30X / Smartphone) | The StackCalc SC-6 + Manipulative Superpower | Keystroke Reduction | Live Stack Visibility | Pedagogical Breakthrough |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **5th Grade Order of Operations:**<br>$(15 - 3) 	imes (4 + 2) \div 6 = 12$ | `( 1 5 - 3 ) * ( 4 + 2 ) / 6 =`<br>(14 keystrokes).<br>*Trap: Missed or misplaced parenthesis computes $15 - 12 + 0.33 = 3.33$ silently! Intermediate results ($12, 6$) are invisible inside hardware buffers.* | **SC-6 Elevator Stack + Two-Number Fusion:**<br>`15 {{key:ENTER}} 3 {{key:-}} 4 {{key:ENTER}} 2 {{key:+}} {{key:×}} 6 {{key:÷}}`<br>(11 keystrokes).<br>Both intermediate quantities ($12$ in $Y$, $6$ in $X$) are visible simultaneously before multiplying! Zero parentheses. | **21% fewer keystrokes**<br>(11 vs. 14) | **Dual Live Registers:**<br>Register $Y$ holds $12$ while Register $X$ computes $6$; live display proves $(15 - 3) 	imes (4 + 2)$ without scratch paper. | **Cognitive Clarity:**<br>Eliminates parenthesis anxiety and Dijkstra shunting-yard confusion; replaces abstract rules with physical two-number stack fusion. |


### Algebraic Trap vs. StackCalc Superpower Showdown: Order of Operations

| Challenge / Equation | The Algebraic Calculator Trap (TI-30X / Smartphone) | The StackCalc SC-6 + Manipulative Superpower | Keystroke Reduction | Live Stack Visibility | Pedagogical Breakthrough |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **5th Grade Order of Operations:**<br>$(15 - 3) 	imes (4 + 2) \div 6 = 12$ | `( 1 5 - 3 ) * ( 4 + 2 ) / 6 =`<br>(14 keystrokes).<br>*Trap: Missed or misplaced parenthesis computes $15 - 12 + 0.33 = 3.33$ silently! Intermediate results ($12, 6$) are invisible inside hardware buffers.* | **SC-6 Elevator Stack + Two-Number Fusion:**<br>`15 {{key:ENTER}} 3 {{key:-}} 4 {{key:ENTER}} 2 {{key:+}} {{key:×}} 6 {{key:÷}}`<br>(11 keystrokes).<br>Both intermediate quantities ($12$ in $Y$, $6$ in $X$) are visible simultaneously before multiplying! Zero parentheses. | **21% fewer keystrokes**<br>(11 vs. 14) | **Dual Live Registers:**<br>Register $Y$ holds $12$ while Register $X$ computes $6$; live display proves $(15 - 3) 	imes (4 + 2)$ without scratch paper. | **Cognitive Clarity:**<br>Eliminates parenthesis anxiety and Dijkstra shunting-yard confusion; replaces abstract rules with physical two-number stack fusion. |


<div class="admonition note">
<p class="admonition-title">For Educators &amp; Parents: Cognitive Load Theory &amp; The Operational Equal-Sign Misconception</p>
<p>
In educational cognitive psychology, <strong>Cognitive Load Theory</strong> (pioneered by John Sweller {{cite:sweller1988}}) explains how human working memory processes novel mathematical information. In children aged 5 to 11, working memory capacity is strictly bounded: as George Miller proved {{cite:miller1956}}, young learners can reliably maintain only three to four discrete mental tokens simultaneously before experiencing cognitive overload.<br><br>
Decades of research in elementary classrooms (Steven Strogatz {{cite:strogatz2012}}, Jerome Bruner {{cite:bruner1966}}, Zoltan Dienes {{cite:dienes1960}}, and Liping Ma {{cite:ma1999}}) reveal that the equal-sign trap conditions children into treating <code>=</code> as an imperative computation trigger rather than a relational balance. When students use conventional algebraic calculators, they must juggle two competing tasks at once:<br>
1. <strong>The Intrinsic Mathematical Task:</strong> Understanding the physical quantities and relationships of the problem {{cite:bruner1966}}.<br>
2. <strong>The Extraneous Syntax Task:</strong> Managing operator precedence rules (PEMDAS), inserting nested parentheses, and waiting for an equal sign (<code>=</code>) to trigger hidden evaluation.<br><br>
By eliminating <code>=</code> and parentheses, Reverse Polish Notation (first formalized by Jan Łukasiewicz {{cite:lukasiewicz1924}} and analyzed for education by Kathy Hamrick {{cite:hamrick1980}}) aligns 100% of the child's working memory with the intrinsic mathematical structure. Every intermediate subtotal remains visible on the physical LCD stack.
</p>
</div>

---

## Five Stack Math Super-Moves

Just as a young maker learns to use a hammer, saw, and ruler, you command five foundational **Stack Math Super-Moves**. Each super-move pairs a hands-on block movement with an action on your stack {{cite:macaulay2016}}:

### Super-Move 1: The Make-a-Ten Snap
- **Physical Manipulative:** 3D-Printed Ten-Frame Studio Tray with two-color counters {{cite:singapore2014}}.
- **The Concept:** When you bridge to 10 before chaining addition (e.g., $8 + 5 = 8 + 2 + 3 = 10 + 3 = 13$), you break numbers apart so they make friendly groups of 10.
- **The Stack Action:** In `{{key:▦}}` Ten-Frame mode, you place 8 counters into Frame $Y$. Keying `5` into Frame $X$ and tapping `{{key:+}}` causes 2 counters from Frame $X$ to migrate into Frame $Y$, completing the 10-tray with a tactile snap, leaving 3 loose counters on the lower tray ($X = 13$).
- **Why It Matters:** Finger-counting disappears because your hands and eyes experience 10 as an unbreakable structural container {{cite:dienes1960}}.

### Super-Move 2: The Elevator Stack Drop
- **Physical Manipulative:** Two-Color Number Rack / Rekenrek Studio.
- **The Concept:** In traditional algebra, intermediate results must be scribbled onto scrap paper or locked behind confusing parentheses `(A - B) × (C + D) ÷ E`.
- **The Stack Action:** As binary operators (`+`, `-`, `×`, `÷`) execute, the upper stack floors drop down like an elevator descending level-by-level ($T \to Z \to Y \to X$). The intermediate value on Mezzanine Floor $Y$ combines with Ground Floor $X$, and whatever was waiting upstairs in Loft Floor $Z$ drops smoothly into $Y$.
- **Why It Matters:** You never lose an intermediate result. Parentheses are completely unnecessary because the physical levels of the stack store intermediate values in plain view.

### Super-Move 3: The Remainder-You-Can-Hold
- **Physical Manipulative:** Counting Tile Studio Trays & Egg Cartons {{cite:ma1999}}.
- **The Concept:** Dividing 17 cookies among 5 friends yields 3 whole cookies each with 2 leftover cookies. Standard calculators output `3.4`, destroying the physical reality of the leftover cookies.
- **The Stack Action:** Superpower 2 (`{{key:÷R}}`) executes integer division in one stroke: Whole Quotient $Q = 3$ appears in Register $X$, while the physical Remainder $R = 2$ rests in Register $Y$. Tapping `{{key:x⇄y}}` swaps them back and forth with zero recalculation.
- **Why It Matters:** You hold both answers at once, linking division directly to real-world sharing, packaging, and modular arithmetic.

### Super-Move 4: The Equal-Fraction Tower Alignment
- **Physical Manipulative:** 84 mm Fraction Studio proportional towers and twin comparator well {{cite:strogatz2012}}.
- **The Concept:** Fractions are equivalent when their physical heights match flush at the top rim of the comparator well.
- **The Stack Action:** Keying an unreduced fraction (e.g., `. 12 . 18`) and tapping `{{key:SIMP}}` steps through common prime factors one-by-one. The display shows each reduced stage ($12/18 \to 6/9 \to 2/3$) until flashing `LOWEST TERMS`.
- **Why It Matters:** You see fraction reduction not as an arbitrary trick, but as finding the tallest block that aligns flush in the comparator well.

### Super-Move 5: The Skip-Counting Ladder
- **Physical Manipulative:** 144-Tile Four-Color Array Studio {{cite:gauss1809}}.
- **The Concept:** Multiplication is repeated equal-group accumulation.
- **The Stack Action:** Superpower 1 (`{{key:REP}}`) seeds all four stack registers ($T, Z, Y, X$) with the step increment. Because Register $T$ automatically duplicates its value downward upon every binary drop, rhythmic taps of `{{key:+}}` climb the times-table ladder indefinitely ($7 \to 14 \to 21 \to 28 \dots$).
- **Why It Matters:** Times tables transform from rote anxiety into a rhythmic motor cadence.

---

## Horizontal $Y \mid X$ Split Screen vs. Vertical Stack

When you first learn mathematics in elementary school, you learn to read and write equations from left to right ($A \text{ op } B = C$). Traditional RPN calculators display registers vertically ($Y$ above $X$), which can feel upside-down at first.

The SC-6 graphic LCD introduces the **Horizontal $Y \mid X$ Split Screen Layout**:

**↰ ↱ FRAC                   Y                X              [BATTERY]**

| Left Column (`Y` — Waiting Number) | Center Divider | Right Column (`X` — Active Number) |
| :---: | :---: | :---: |
| **`12`** | Vertical Split Rule | **`4`** |

### The Enter-Slide Animation
1. **Typing Your First Number:** When you key `12`, it appears in the **Right ($X$)** column.
2. **Pressing `{{key:ENTER}}`:** The digits `12` visually slide smoothly across the LCD from the right column into the **Left ($Y$)** column. You see: *"My 12 has moved into position on the left, waiting for math!"*
3. **Typing Your Second Number:** When you key `4`, it enters the **Right ($X$)** column. The display clearly presents `Y = 12` and `X = 4`.
4. **Pressing an Operator (`{{key:-}}` or `{{key:÷}}`):**
   - The operator symbol briefly flashes in the center vertical divider line.
   - The calculator evaluates $Y \text{ op } X$ left-to-right ($12 - 4 = 8$ or $12 \div 4 = 3$).
   - The result appears in the right column ($X$), while the stack drops.

### System Flag 5: Dual Stack vs. Single Stack Mode
Controlled via `{{key:FLAGS}}`, Flag 5 configures the display layout to match how you like to see your numbers:
- **Flag 5 = 0 (Default — Dual Stack $Y \mid X$):** Displays both $Y$ (left) and $X$ (right) columns simultaneously. Ideal for developing spatial RPN fluency.
- **Flag 5 = 1 (Single Stack $X$ Only):** Centers a single large number across the full width of the screen. Ideal when you want absolute visual simplicity with giant bold numbers. In single-stack mode, `{{key:ENTER}}` pushes your number into $Y$ in the background stack while $X$ remains centered.

---

## Configurable Stack Depths: `2-LV`, `4-LV`, and `8-LV`

To eliminate cognitive friction across grade levels, the SC-6 features three user-selectable operational stack depths:

> **CONFIGURABLE STACK DEPTHS**
>
> 1. 2-LEVEL STACK (2-LV):
> • Registers: Y (Held/Constant) and X (Active Input).
> • Ideal for: Grades K–1 single-step addition/subtraction, step counters
> (1 {{key:ENTER}} 1 {{key:+}}), and Ten-Frame visual sandboxes.
> 2. 4-LEVEL STACK (4-LV):
> • Registers: T (Roof), Z (Loft), Y (Mezzanine), X (Ground).
> • Ideal for: Grades 2–5 standard elementary mathematics, multi-step
> word problems, long division quotient/remainder, and fraction work.
> 3. 8-LEVEL STACK (8-LV):
> • Registers: 8 full vertical registers (R7 down to R0).
> • Ideal for: Grade 6 Pre-Algebra, rapid mental math sprints,
> and multi-parenthesis equation evaluations without memory variables.

### The Step-Counter Dynamics: 2-Stack vs. 4-Stack
A classic elementary discovery exercise is building a step counter: tapping `{{res:sc6_02_rpn_for_young_learners_seq_41:keys}}` and repeatedly pressing `{{key:+}}` to count $2, 3, 4, 5 \dots$

In **4-Stack Mode (`4-LV`)**, the stack drops $Z \to Y$. Since $Z$ and $T$ start at $0$, subsequent taps of `{{key:+}}` add $0$ unless Superpower 1 (`{{key:REP}}`) was used to replicate the constant across all registers.

In **2-Stack Mode (`2-LV`)**, however, Register $Y$ acts as the top register ($T$). When `+` executes, $Y$ automatically preserves its constant ($1.0$):
`1 {{key:ENTER}} 1 {{key:+}}` $\implies \mathbf{2}$, `{{key:+}}` $\implies \mathbf{3}$, `{{key:+}}` $\implies \mathbf{4}$, `{{key:+}}` $\implies \mathbf{5}$

---

## Moving Numbers Around on Your Stack: `{{key:x⇄y}}`, `{{key:R↓}}`, `{{key:REP}}`, `{{key:LASTX}}`

The SC-6 keypad provides dedicated physical keys to move and manage numbers on your stack:

| Keystroke | Operation | Stack Register Effect |
|---|---|---|
| `{{key:x⇄y}}` | **Swap $X$ and $Y$** | Exchanges the active input and held number ($X \leftrightarrow Y$). Instantly corrects reversed subtraction or division. |
| `{{key:R↓}}` | **Roll Down** | Rotates the 4-level stack downward in a carousel: $X \to T,\; T \to Z,\; Z \to Y,\; Y \to X$. |
| `{{key:REP}}` | **Repeat Operation** | Repeats the last two-number arithmetic step for rhythmic skip-counting and constant scaling. |
| `{{key:LASTX}}` | **Recover Prior Number** | Recalls the previous $X$ value before the last operation for self-checking inverse verification. |
| `{{key:SHOW}}` | **Full Significant Digits Reveal** | Momentarily displays all internal digits of Register $X$. |

---

## Story-Driven Problem Expeditions (40 Foundational Scenarios)

Rather than facing disconnected lists of drill problems, you embark on four cohesive mathematical missions. Each expedition grounds arithmetic in a tangible, real-world narrative where intermediate calculations matter and numbers flow naturally through the stack.

<div class="admonition tip">
<p class="admonition-title">Hands-On Studio Proof: Blocks &rarr; Calculator</p>
<p>
<strong>Step 1 (Physical Concrete Intuition):</strong> Build two physical tile towers from your manipulative studio: a red tower of 5 cubes and a green tower of 3 cubes. Place them side-by-side on your desk. Slide the 3-cube tower directly on top of the 5-cube tower into a single combined tower of 8 cubes.<br>
<strong>Step 2 (The Representational Bridge):</strong> Look at the SC-6 display. When you enter <code>5 {{key:ENTER}} 3</code>, the 5 sits on Floor 2 (Register Y) and the 3 waits on Floor 1 (Register X). The screen directly mirrors your two tabletop towers!<br>
<strong>Step 3 (Scaling on the Calculator):</strong> Press <code>{{key:+}}</code>. The two numbers fuse into <code>8</code>. Now scale it up to building a skyscraper: type <code>500 {{key:ENTER}} 300 {{key:+}}</code> &rarr; <code>800</code>! The physical intuition of sliding blocks scales instantly to thousands and millions without pen or paper.
</p>
</div>

{{blocks:math_dominoes_pairing|Math Dominoes Studio Doubling and Pairing}}
*Figure 2.2: The Math Dominoes Studio. Domino pips let you see groups at a glance and build pairs that mirror RPN two-number operations.*

### Expedition 1: The School Playground Construction Crew (Problems 01–10)
*Mission Briefing:* The local elementary school is constructing a brand-new adventure playground. As the project engineers, your crew must lay border timbers, pour sandbox gravel, measure stepping stone distances, and ensure safety clearances using the SC-6 stack.

### Problem 01:
- **Playground Construction Mission:** Your playground construction crew is laying interlocking rubber safety tiles under the two-bay swing set. The crew unloads 5 blue safety tiles in the morning, and the supply truck delivers 3 more green safety tiles in the afternoon. How many total safety tiles are ready to lay down?
- **Concrete Stage:** Place 5 blue counting tiles on the left side of your desk, and 3 green tiles on the right. Slide them together into one combined row of 8 tiles.
- **Representational Stage:** The horizontal display shows `Y = 5` (left) and `X = 3` (right) before combining.
- **Abstract RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_01:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_01:value}}`**
- **Stack Flow:** Tap `5 {{key:ENTER}} 3 {{key:+}}` -> (T=0, Z=0, Y=0, X=8) to fuse both groups into 8 on the ground floor.
- **Diagnostic Checkpoint:** Did you see $Y = 5$ on the left and $X = 3$ on the right before pressing `{{key:+}}`? If your screen shows $53$, you forgot to press `{{key:ENTER}}` between the digits!
---

### Problem 02:
- **Playground Construction Mission:** Your crew needs to anchor 9 sturdy cedar fence posts along the adventure playground perimeter. Before lunch, your crew finishes concreting 4 posts firmly into the ground. How many fence posts still need to be anchored?
- **Concrete Stage:** Align 9 counting tiles in a row representing the fence line. Detach 4 tiles from the end for the completed posts. Count the 5 remaining tiles.
- **Representational Stage:** Left column holds starting number $9$; right column holds second number $4$.
- **Abstract RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_02:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_02:value}}`**
- **Stack Flow:** Tap `9 {{key:ENTER}} 4 {{key:-}}` -> (T=0, Z=0, Y=0, X=5) to leave 5 unbolted posts on the ground floor.
- **Diagnostic Checkpoint:** If your screen displays $-5$, you entered the second number first (`4 {{key:ENTER}} 9 {{key:-}}`). Do not re-type! Simply tap `{{key:x⇄y}} {{key:-}}` to reverse and correct the calculation!
---

### Problem 03:
- **Playground Construction Mission:** To fill the giant wooden sandbox, your crew wheels loads of washed pea gravel from the supply depot: 4 wheelbarrows on Monday, 5 on Tuesday, and 6 on Wednesday. How many total wheelbarrows of gravel did you pour into the sandbox?
- **Concrete Stage:** Stack 4 unit cubes on your desk, add 5 cubes, and then add 6 more cubes to form a single continuous tower of 15 cubes.
- **Abstract RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_03:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_03:value}}`**
- **Stack Flow:** Tap `4 {{key:ENTER}} 5 {{key:+}} 6 {{key:+}}` -> (T=0, Z=0, Y=0, X=15). The intermediate sum $9$ automatically lifts to $Y$ when you key $6$, delivering $15$ with zero extra `{{key:ENTER}}` strokes.
---

### Problem 04:
- **Playground Construction Mission:** Your crew is installing round sensory stepping stones along the winding garden path. You lay down 8 smooth slate stones in the morning, and the supply truck brings 7 granite stones in the afternoon. How many total stepping stones lead to the climbing tower?
- **Concrete Stage:** Place 8 counters into your first Ten-Frame tray. Take 2 counters from the group of 7 to fill the first tray to a complete 10; the remaining 5 counters spill into the second tray. Total: 1 full ten and 5 ones ($15$).
- **Abstract RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_04:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_04:value}}`**
- **Stack Flow:** Tap `8 {{key:ENTER}} 7 {{key:+}}` -> (T=0, Z=0, Y=0, X=15), bridging the decade seamlessly to leave 15 stepping stones.
---

### Problem 05:
- **Playground Construction Mission:** A heavy hardware box holds a bundle of 10 galvanized steel crossbeam bolts for the jungle gym frame. Your crew bolts 6 of them through the climbing net uprights. How many bolts remain in the box for the balance-beam brackets?
- **Concrete Stage:** Fill a complete Ten-Frame tray with 10 counters. Remove 6 counters. Exactly 4 counters remain in the tray.
- **Abstract RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_05:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_05:value}}`**
- **Stack Flow:** Tap `10 {{key:ENTER}} 6 {{key:-}}` -> (T=0, Z=0, Y=0, X=4), leaving 4 bolts ready in Register $X$.
---

### Problem 06:
- **Playground Construction Mission:** Your crew stakes 7 bright orange survey flags along the safety perimeter of the zip-line runway. The ground inspector checks the layout and confirms that zero additional flags are needed ($+0$). How many flags remain planted along the runway?
- **Concrete Stage:** Place 7 counting tiles on your desk. Add zero tiles. You still have 7 tiles.
- **Abstract RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_06:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_06:value}}`**
- **Stack Flow:** Tap `7 {{key:ENTER}} 0 {{key:+}}` -> (T=0, Z=0, Y=0, X=7), proving identity element $a + 0 = a$.
---

### Problem 07:
- **Playground Construction Mission:** The crew equipment chest has 8 safety climbing carabiners hanging from the inspection rack. During morning foundation prep, zero carabiners are taken out because the climbing tower hasn't arrived yet. How many carabiners stay clipped to the rack?
- **Concrete Stage:** Set out 8 counting tiles. Remove zero tiles. Exactly 8 tiles remain.
- **Abstract RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_07:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_07:value}}`**
- **Stack Flow:** Tap `8 {{key:ENTER}} 0 {{key:-}}` -> (T=0, Z=0, Y=0, X=8), verifying $a - 0 = a$.
---

### Problem 08:
- **Playground Construction Mission:** 6 heavy galvanized link chains are uncoiled on the grass for the three playground tire swings. Your crew bolts all 6 chains to the overhead swing hanger hooks. How many uninstalled chains remain on the grass?
- **Concrete Stage:** Place 6 counting tiles on the desk. Remove all 6 tiles. Zero tiles remain ($6 - 6 = 0$).
- **Abstract RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_08:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_08:value}}`**
- **Stack Flow:** Tap `6 {{key:ENTER}} 6 {{key:-}}` -> (T=0, Z=0, Y=0, X=0), clearing inventory to zero.
---

### Problem 09:
- **Playground Construction Mission:** Your construction crew paves the safety perimeter around the spiral slide using 23 heavy interlocking rubber pavers, and lays another 14 pavers around the low balance-beam zone. How many total border pavers did your crew install?
- **Concrete Stage:** Build 23 using 2 ten-sticks and 3 unit cubes. Build 14 using 1 ten-stick and 4 unit cubes. Combine tens ($2+1=3$) and ones ($3+4=7$) to find 37.
- **Abstract RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_09:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_09:value}}`**
- **Stack Flow:** Tap `23 {{key:ENTER}} 14 {{key:+}}` -> (T=0, Z=0, Y=0, X=37), calculating 37 installed pavers in one fluent motion.
---

### Problem 10:
- **Playground Construction Mission:** Your crew spreads soft cedar playground woodchips beneath the monkey bars to ensure a deep shock-absorbing cushion. The first wheelbarrow delivers $47\text{ kg}$ of woodchips, and the second wheelbarrow brings $36\text{ kg}$. What is the total mass of woodchips spread beneath the bars?
- **Concrete Stage:** Represent 47 with 4 tens and 7 ones. Represent 36 with 3 tens and 6 ones. Combine ones ($7 + 6 = 13$, regroup as 1 ten and 3 ones), then add tens ($4 + 3 + 1 = 8$ tens). Total: 8 tens and 3 ones ($83$).
- **Abstract RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_10:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_10:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 47 | 0 | 0 | 0 | 47 |
| {{key:ENTER}} | 0 | 0 | 47 | 47 |
| 36 | 0 | 0 | 47 | 36 |
| {{key:+}} | 0 | 0 | 0 | 83 |
| {{key:LASTX}} | 0 | 0 | 83 | 36 |
| {{key:-}} | 0 | 0 | 0 | 47 |
- **Self-Check Invariant:** Rows 5 and 6 demonstrate Superpower 4 (`{{key:LASTX}}`), verifying $83 - 36 = 47$ instantly.
---

### Expedition 2: The High-Rise Elevator Express (Problems 11–20)
*Mission Briefing:* You are the logistics controller for a bustling 20-story urban high-rise. Your mission is to track passenger loads rising between floors, monitor freight delivery weights, and calculate multi-floor transfers using the SC-6 operational stack.

### Problem 11:
- **High-Rise Elevator Mission:** A freight elevator begins at the ground floor loaded with $83\text{ kg}$ of construction fixtures. At Floor 4, the logistics crew unloads $36\text{ kg}$ of steel brackets. How many kilograms of cargo remain inside the freight cab?
- **Concrete Stage (Counting Tile Studio):** Lay out 8 ten-rods and 3 unit cubes ($83$). To subtract 36, trade 1 ten-rod for 10 units (leaving 7 tens and 13 units). Remove 3 tens and 6 units to leave 4 tens and 7 units ($47$).
- **Abstract RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_11:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_11:value}}`**
- **Stack Flow:** Tap `83 {{key:ENTER}} 36 {{key:-}}` -> (T=0, Z=0, Y=0, X=47) to leave 47 kg of remaining fixtures.
---

### Problem 12:
- **High-Rise Elevator Mission:** An express elevator cab carries 16 convention delegates from the concourse. At the mezzanine level, an equal delegation of 16 more delegates steps aboard, doubling the passenger count. How many delegates are now riding the elevator?
- **Concrete Stage:** Stack two identical 16-tile towers from your counting tile studio, showing $16 + 16 = 32$.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_12:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_12:value}}`**
- **Stack Flow:** Tap `16 {{key:ENTER}} {{key:+}}` -> (T=0, Z=0, Y=0, X=32). Pressing `{{key:ENTER}}` duplicates 16 into both shelves, and `{{key:+}}` doubles it instantly without re-typing!
---

### Problem 13:
- **High-Rise Elevator Mission:** An automated smart-lift dispatch computer doubles its active corridor scans on each floor rise. Starting with $2$ baseline sensor beams at Floor 1, determine the total active sensor scans by Floor 5.
- **Concrete Stage:** Place 2 tiles on the table. Double the pile to 4, then 8, then 16, then 32, feeling exponential growth in your hands.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_13:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_13:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 2 | 0 | 0 | 0 | 2 |
| {{key:ENTER}} {{key:+}} | 0 | 0 | 0 | 4 |
| {{key:ENTER}} {{key:+}} | 0 | 0 | 0 | 8 |
| {{key:ENTER}} {{key:+}} | 0 | 0 | 0 | 16 |
| {{key:ENTER}} {{key:+}} | 0 | 0 | 0 | 32 |
---

### Problem 14:
- **High-Rise Elevator Mission:** During morning rush hour, an express elevator boards 15 passengers on the subway concourse, 24 passengers on the ground plaza, and 31 passengers at the parking deck. How many total passengers are transported upward?
- **Concrete Stage:** Form three separate tile trains of 15, 24, and 31 tiles. Slide them end-to-end to verify a combined length of 70 tiles.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_14:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_14:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 15 | 0 | 0 | 0 | 15 |
| {{key:ENTER}} | 0 | 0 | 15 | 15 |
| 24 | 0 | 0 | 15 | 24 |
| {{key:+}} | 0 | 0 | 0 | 39 |
| 31 | 0 | 0 | 39 | 31 |
| {{key:+}} | 0 | 0 | 0 | 70 |
---

### Problem 15:
- **High-Rise Elevator Mission:** The skyscraper's observation deck elevator has a maximum permitted safety capacity of 100 people. If an incoming tour group consists of 43 visitors, how many additional visitors can board before reaching capacity?
- **Concrete Stage:** Model 100 with a ten-by-ten tile flat. Remove 4 rows of ten and 3 individual tiles to reveal 5 tens and 7 units ($57$).
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_15:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_15:value}}`**
- **Stack Flow:** Tap `100 {{key:ENTER}} 43 {{key:-}}` -> (T=0, Z=0, Y=0, X=57), confirming 57 open visitor spots.
---

### Problem 16:
- **High-Rise Elevator Mission:** The elevator safety inspector tests the floor indicator sensors by stepping upward in 10-floor intervals starting from the basement lobby (Floor 0) up to Floor 50 in 2-stack mode (`2-LV`).
- **Concrete Stage:** Line up 5 ten-rods end-to-end, counting rhythmically: 10, 20, 30, 40, 50.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_16:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_16:value}}`**
- **Stack Flow:** In 2-Stack mode, Register $Y$ acts as the constant holder. Key in `10 {{key:ENTER}} 0 {{key:+}}` -> (T=0, Z=0, Y=0, X=10); subsequent taps of `{{key:+}}` climb rhythmically through Floors 20, 30, 40, and 50.
---

### Problem 17:
- **High-Rise Elevator Mission:** The skyscraper's parking garage has 4 levels, each equipped with 6 electric vehicle elevator transfer bays. How many transfer bays are available in total?
- **Concrete Stage:** Construct a $4 \times 6$ array using 24 counting tiles from the manipulative studio.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_17:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_17:value}}`**
- **Stack Flow:** Tap `4 {{key:ENTER}} 6 {{key:×}}` -> (T=0, Z=0, Y=0, X=24), calculating 24 total transfer bays.
---

### Problem 18:
- **High-Rise Elevator Mission:** The exterior window washing elevator scaffold cleans 7 structural window bays on each of 8 executive floors. How many total window panes are washed on this run?
- **Concrete Stage:** Build a $7 \times 8$ grid using counting studio tiles, rotating the tray $90^\circ$ to see that $7 \times 8 = 8 \times 7 = 56$.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_18:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_18:value}}`**
- **Stack Flow:** Tap `7 {{key:ENTER}} 8 {{key:×}}` -> (T=0, Z=0, Y=0, X=56), evaluating 56 window panes.
---

### Problem 19:
- **High-Rise Elevator Mission:** A security supervisor delivers 24 handheld communication radios equally among 4 elevator lobby stations. How many radios are allocated to each station?
- **Concrete Stage:** Deal out 24 counting tiles into 4 equal groups, confirming 6 tiles in each group.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_19:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_19:value}}`**
- **Stack Flow:** Tap `24 {{key:ENTER}} 4 {{key:÷}}` -> (T=0, Z=0, Y=0, X=6), allocating 6 radios per station.
---

### Problem 20:
- **High-Rise Elevator Mission:** An express shuttle elevator transports 56 security staff members arriving for an international summit, distributing them equally across 7 security checkpoint floors. How many officers are stationed on each floor?
- **Concrete Stage:** Separate a group of 56 counting tiles into 7 equal rows, counting 8 tiles per row.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_20:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_20:value}}`**
- **Stack Flow:** Tap `56 {{key:ENTER}} 7 {{key:÷}}` -> (T=0, Z=0, Y=0, X=8), placing 8 officers per floor.
---

### Expedition 3: The Saturday Supermarket Shopping Spree (Problems 21–30)
*Mission Briefing:* Armed with a weekly household grocery budget, you navigate the supermarket aisles. You must calculate bulk food packaging remainders, compute multi-item basket discounts, verify sales receipts, and check coin change without scratch paper.

### Problem 21:
- **Supermarket Shopping Mission:** The bakery aisle manager packages 17 warm sourdough dinner rolls into bags of 5 rolls. How many bags are filled completely, and how many loose rolls remain?
- **Concrete Stage:** Distribute 17 counting tiles into groups of 5. Count 3 full groups and 2 loose tiles.
- **Abstract RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_21:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_21:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 17 | 0 | 0 | 0 | 17 |
| {{key:ENTER}} | 0 | 0 | 17 | 17 |
| 5 | 0 | 0 | 17 | 5 |
| {{key:÷R}} | 0 | 0 | 2 | 3 |
| {{key:x⇄y}} | 0 | 0 | 3 | 2 |
- **Diagnostic Checkpoint:** Register $X$ shows Quotient $Q = 3$ full bags. Register $Y$ holds Remainder $R = 2$ loose rolls. Press `{{key:x⇄y}}` to inspect remainder and swap back. Total bags needed to pack all rolls: $3 + 1 = 4\text{ bags}$.
---

### Problem 22:
- **Supermarket Shopping Mission:** In the dairy aisle, a wholesale crate of 125 farm-fresh eggs is sorted into specialty cartons holding 8 eggs each. How many cartons are filled completely, and how many eggs remain?
- **Concrete Stage:** Group base-10 counting blocks to represent 125 divided by 8, observing 15 full groups of 8 and 5 remaining units.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_22:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_22:value}}`**
- **Stack Flow:** Tap `125 {{key:ENTER}} 8 {{key:÷R}}` -> (T=0, Z=0, Y=5, X=15), revealing 15 full cartons in Register $X$ and 5 leftover eggs in Register $Y$.
---

### Problem 23:
- **Supermarket Shopping Mission:** The store manager orders 15 wholesale crates of Valencia oranges at $\$8.00$ per crate ($15 \times 8 = 120$). Verify the total invoice using Superpower 4 (`{{key:LASTX}}`) without re-typing.
- **Concrete Stage:** Model 15 rows of 8 tiles, then divide the total by 8 to restore the original 15 rows.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_23:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_23:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 15 | 0 | 0 | 0 | 15 |
| {{key:ENTER}} | 0 | 0 | 15 | 15 |
| 8 | 0 | 0 | 15 | 8 |
| {{key:×}} | 0 | 0 | 0 | 120 |
| {{key:LASTX}} | 0 | 0 | 120 | 8 |
| {{key:÷}} | 0 | 0 | 0 | 15 |
---

### Problem 24:
- **Supermarket Shopping Mission:** A shopper calculates unit pricing for a 24-ounce container of Greek yogurt divided into 8 snack portions ($24 \div 8 = 3$), but accidentally typed 8 first (`8 {{key:ENTER}} 24`).
- **Remediation Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_24:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_24:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 8 | 0 | 0 | 0 | 8 |
| {{key:ENTER}} | 0 | 0 | 8 | 8 |
| 24 | 0 | 0 | 8 | 24 |
| {{key:x⇄y}} | 0 | 0 | 24 | 8 |
| {{key:÷}} | 0 | 0 | 0 | 3 |
- **Diagnostic Checkpoint:** Never start over when you type numbers in the wrong order! Just tap the swap key {{key:x⇄y}} to put them in the right seats, then divide!
---

### Problem 25:
- **Supermarket Shopping Mission:** A shopper enters the checkout lane with 14 items in their cart. They add 5 items from the impulse rack, but decide to put back 3 items. How many items are scanned at checkout?
- **Concrete Stage:** Place 14 counting tiles on the desk. Add 5 more tiles, then remove 3 tiles.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_25:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_25:value}}`**
- **Stack Flow:** Tap `14 {{key:ENTER}} 5 {{key:+}} 3 {{key:-}}` -> (T=0, Z=0, Y=0, X=16). The subtotal 19 auto-lifts when you type 3, arriving at 16 scanned items seamlessly.
---

### Problem 26:
- **Supermarket Shopping Mission:** At the bakery counter, a customer buys 3 artisan baguettes at $\$4.00$ each and 2 specialty cheese rounds at $\$5.00$ each. Find the total basket cost.
- **Concrete Stage:** Build two tile groups: one $3 \times 4$ array (12) and one $2 \times 5$ array (10). Slide them together to count 22 tiles.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_26:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_26:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 3 | 0 | 0 | 0 | 3 |
| {{key:ENTER}} | 0 | 0 | 3 | 3 |
| 4 | 0 | 0 | 3 | 4 |
| {{key:×}} | 0 | 0 | 0 | 12 |
| 2 | 0 | 0 | 12 | 2 |
| {{key:ENTER}} | 0 | 12 | 2 | 2 |
| 5 | 0 | 12 | 2 | 5 |
| {{key:×}} | 0 | 0 | 12 | 10 |
| {{key:+}} | 0 | 0 | 0 | 22 |
- **Stack Elegance:** Notice in row 8: Register $Y$ held the first subtotal ($12$) while Register $X$ computed the second subtotal ($10$). Pressing `{{key:+}}` combined them cleanly without writing down anything on paper!
---

### Problem 27:
- **Supermarket Shopping Mission:** The store manager arranges a rectangular organic fruit display table that is 12 feet long and 8 feet wide. What is the total length of decorative bumper railing needed to surround the table?
- **Concrete Stage:** Construct a 12 by 8 rectangle with grid tiles, calculating $2 \times (\text{length} + \text{width})$.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_27:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_27:value}}`**
- **Stack Flow:** Tap `12 {{key:ENTER}} 8 {{key:+}} 2 {{key:×}}` -> (T=0, Z=0, Y=0, X=40), calculating 40 feet of bumper railing without writing down semi-perimeter 20.
---

### Problem 28:
- **Supermarket Shopping Mission:** A triangular promotional sign hanging over the bakery aisle has a base of 10 cm and a height of 6 cm. What is the surface area of the promotional sign?
- **Concrete Stage:** Form a $10 \times 6$ array of 60 tiles, then divide it into two equal halves of 30 tiles.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_28:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_28:value}}`**
- **Stack Flow:** Tap `10 {{key:ENTER}} 6 {{key:×}} 2 {{key:÷}}` -> (T=0, Z=0, Y=0, X=30), evaluating the $30\text{ cm}^2$ sign area cleanly.
---

### Problem 29:
- **Supermarket Shopping Mission:** A customer brings a $\$50$ cash grocery budget to the supermarket. They spend $\$18$ on fresh produce and $\$12$ on dairy items. How much grocery cash remains in their wallet?
- **Concrete Stage:** Start with 5 ten-rods ($50$). Remove 1 ten and 8 units ($18$, leaving 32), then remove 1 ten and 2 units ($12$, leaving 20).
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_29:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_29:value}}`**
- **Stack Flow:** Tap `50 {{key:ENTER}} 18 {{key:-}} 12 {{key:-}}` -> (T=0, Z=0, Y=0, X=20), leaving $\$20.00$ cash in your wallet.
---

### Problem 30:
- **Supermarket Shopping Mission:** Four family members purchase a bulk deli sandwich platter costing $\$17.50$. Using Superpower 2 (`{{key:÷R}}`), determine how many whole dollars each person contributes and the remaining loose coin change.
- **Concrete Stage:** Count 17 dollar tiles and two quarter coins. Distribute 4 dollar tiles to each of 4 people, leaving $1.50 in change.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_30:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_30:value}}`**
- **Stack Flow:** Tap `17.50 {{key:ENTER}} 4 {{key:÷R}}` -> (T=0, Z=0, Y=1.5, X=4), giving $X = \$4.00$ whole dollars per person and $Y = \$1.50$ remaining change.
---

### Expedition 4: The Junior Math Olympiad Sprint (Problems 31–40)
*Mission Briefing:* The state tournament clock is running! In this high-speed mental sprint, you solve chained order-of-operations expressions, evaluate multi-bracket terms with zero parentheses, and navigate radical equations using pure RPN stack elegance.

### Problem 31:
- **Word Problem:** Load values 10, 20, 30, 40 into the stack. Rotate them down to inspect each register.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_31:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_31:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 10 | 0 | 0 | 0 | 10 |
| {{key:ENTER}} | 0 | 0 | 10 | 10 |
| 20 | 0 | 0 | 10 | 20 |
| {{key:ENTER}} | 0 | 10 | 20 | 20 |
| 30 | 0 | 10 | 20 | 30 |
| {{key:ENTER}} | 10 | 20 | 30 | 30 |
| 40 | 10 | 20 | 30 | 40 |
| {{key:R↓}} | 40 | 10 | 20 | 30 |
| {{key:R↓}} | 30 | 40 | 10 | 20 |
| {{key:R↓}} | 20 | 30 | 40 | 10 |
| {{key:R↓}} | 10 | 20 | 30 | 40 |
- **Carousel Property:** 4 presses of `{{key:R↓}}` restore the exact original stack!
---

### Problem 32:
- **Word Problem:** Bring the top roof-garden register ($T = 10$) down into the active Ground Floor ($X$) by rotating the 4-level carousel three steps (`{{key:R↓}} {{key:R↓}} {{key:R↓}}`).
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_32:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_32:value}}`**
- **Stack Flow:** Load registers and rotate: tap `10 {{key:ENTER}} 20 {{key:ENTER}} 30 {{key:ENTER}} 40 {{key:R↓}} {{key:R↓}} {{key:R↓}}` -> (T=20, Z=30, Y=40, X=10), bringing 10 into Register $X$.
---

### Problem 33:
- **Word Problem:** 5th-grade math sprint order-of-operations challenge.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_33:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_33:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 15 | 0 | 0 | 0 | 15 |
| {{key:ENTER}} | 0 | 0 | 15 | 15 |
| 3 | 0 | 0 | 15 | 3 |
| {{key:-}} | 0 | 0 | 0 | 12 |
| 4 | 0 | 0 | 12 | 4 |
| {{key:ENTER}} | 0 | 12 | 4 | 4 |
| 2 | 0 | 12 | 4 | 2 |
| {{key:+}} | 0 | 0 | 12 | 6 |
| {{key:×}} | 0 | 0 | 0 | 72 |
| 6 | 0 | 0 | 72 | 6 |
| {{key:÷}} | 0 | 0 | 0 | 12 |
- **Result:** $12.0$. Zero parentheses!
---

### Problem 34:
- **Word Problem:** Calculate the quotient of two parenthesized differences.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_34:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_34:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 24 | 0 | 0 | 0 | 24 |
| {{key:ENTER}} | 0 | 0 | 24 | 24 |
| 8 | 0 | 0 | 24 | 8 |
| {{key:-}} | 0 | 0 | 0 | 16 |
| 6 | 0 | 0 | 16 | 6 |
| {{key:ENTER}} | 0 | 16 | 6 | 6 |
| 2 | 0 | 16 | 6 | 2 |
| {{key:-}} | 0 | 0 | 16 | 4 |
| {{key:÷}} | 0 | 0 | 0 | 4 |
- **Result:** $4.0$.
---

### Problem 35:
- **Word Problem:** Three-part chained expression.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_35:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_35:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 18 | 0 | 0 | 0 | 18 |
| {{key:ENTER}} | 0 | 0 | 18 | 18 |
| 6 | 0 | 0 | 18 | 6 |
| {{key:+}} | 0 | 0 | 0 | 24 |
| 10 | 0 | 0 | 24 | 10 |
| {{key:ENTER}} | 0 | 24 | 10 | 10 |
| 5 | 0 | 24 | 10 | 5 |
| {{key:-}} | 0 | 0 | 24 | 5 |
| {{key:×}} | 0 | 0 | 0 | 120 |
| 12 | 0 | 0 | 120 | 12 |
| {{key:÷}} | 0 | 0 | 0 | 10 |
- **Result:** $10.0$.
---

### Problem 36:
- **Word Problem:** Multi-term fraction bar challenge.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_36:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_36:value}}`**
- **Stack Flow:** Tap `48 {{key:ENTER}} 4 {{key:ENTER}} 6 {{key:×}} {{key:-}} 3 {{key:ENTER}} 2 {{key:ENTER}} 4.5 {{key:×}} {{key:+}} {{key:÷}}` -> (T=24, Z=24, Y=24, X=2), resolving the complex fraction to $2.0$ with zero parentheses!
---

### Problem 37:
- **Word Problem:** A large square patio of $15\text{ ft} \times 15\text{ ft}$ has a central fountain of $9\text{ ft} \times 9\text{ ft}$. Find the remaining paved area.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_37:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_37:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 15 | 0 | 0 | 0 | 15 |
| {{key:x²}} | 0 | 0 | 0 | 225 |
| 9 | 0 | 0 | 225 | 9 |
| {{key:x²}} | 0 | 0 | 225 | 81 |
| {{key:-}} | 0 | 0 | 0 | 144 |
- **Result:** $144.0\text{ sq ft}$.
---

### Problem 38:
- **Word Problem:** A right triangle has perpendicular legs of 6 cm and 8 cm. Find hypotenuse $c = \sqrt{a^2 + b^2}$.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_38:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_38:value}}`**
- **Stack Flow:** Tap `6 {{key:x²}} 8 {{key:x²}} {{key:+}} {{key:√x}}` -> (T=0, Z=0, Y=0, X=10), computing hypotenuse $10.0\text{ cm}$ without scratch paper.
---

### Problem 39:
- **Word Problem:** Convert $68^\circ\text{F}$ to Celsius: $C = (F - 32) \times 5 \div 9$.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_39:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_39:value}}`**
- **Stack Flow:** Tap `68 {{key:ENTER}} 32 {{key:-}} 5 {{key:×}} 9 {{key:÷}}` -> (T=0, Z=0, Y=0, X=20), converting directly to $20.0^\circ\text{C}$.
---

### Problem 40:
- **Word Problem:** Your school savings account has $\$120.00$. You make a purchase of $\$45.00$. Use Superpower 4 to restore your previous balance.
- **RPN Keystrokes:** `{{res:sc6_02_rpn_for_young_learners_seq_40:keys}}` $\rightarrow$ **`{{res:sc6_02_rpn_for_young_learners_seq_40:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 120 | 0 | 0 | 0 | 120 |
| {{key:ENTER}} | 0 | 0 | 120 | 120 |
| 45 | 0 | 0 | 120 | 45 |
| {{key:-}} | 0 | 0 | 0 | 75 |
| {{key:LASTX}} | 0 | 0 | 75 | 45 |
| {{key:+}} | 0 | 0 | 0 | 120 |
- **Result:** Initial $\$120.00$ balance completely restored.
---

## Beat Every Adult in the Room! The `1089` Mind-Reading Stack Trick

Want to amaze your parents or friends at the dinner table? Tell them you can read their mind using the SC-6 elevator stack:
1. Write the secret number **`1089`** on a folded slip of paper and hand it to an adult before you start.
2. Ask them to pick *any* 3-digit number where the first and last digits differ by at least 2 (for example, **`732`**).
3. Have them reverse the digits (**`237`**) and subtract the smaller from the larger on the stack (`732 {{key:ENTER}} 237 {{key:-}}` $\to$ `495`).
4. Now take that answer (`495`), reverse its digits (**`594`**), and add them right on the stack!
   * **Full RPN Chain:** `{{res:sc6_02_mind_reader_1089:keys}}` $\longrightarrow$ **`{{res:sc6_02_mind_reader_1089:value}}`**!
5. Tell them to open the folded paper—no matter which 3-digit number they started with, the stack lands on **`1089`** every single time! *(Why it works: subtracting a reversed 3-digit number always produces a multiple of 99 whose hundreds and ones digits add to 9, and adding its reverse gives $900 + 180 + 9 = 1,089$!)*

---

## Why Your Brain Loves Stack Math (No Parenthesis Headaches!)

Why do you learn math faster and make fewer mistakes with Stack Math? Because your brain only has to think about two numbers at a time!

On a normal calculator, solving a problem like $(15 - 3) \times (4 + 2) \div 6$ feels like juggling five spinning plates at once while worrying about tricky parentheses brackets `(` and `)`. On your SC-6, you never juggle—you just stack and combine!

| What You Are Solving | Normal Calculator (Parenthesis Headache!) | StackCalc SC-6 (Easy & Clear!) |
| :--- | :---: | :---: |
| **First Part (`15 - 3`)** | Juggling open brackets and numbers | Just 2 numbers: `15` and `3` combine right into `12`! |
| **Second Part (`× (4 + 2)`)** | Juggling brackets inside brackets | Just 2 numbers: `4` and `2` combine right into `6`! |
| **Finishing Up (`÷ 6`)** | Untangling all the leftover brackets | Just 2 numbers: `72` and `6` give you **`12`**! |

### The Headache of Parentheses on Normal Calculators
When you type a problem like $(15 - 3) \times (4 + 2) \div 6$ on a regular calculator, you cannot see what is happening until you finish the whole line:
1. You have to open a bracket `(`, type `15 - 3`, and close the bracket `)`.
2. You have to remember what that part made in your head while typing `×`.
3. You have to open another bracket `(`, type `4 + 2`, and close it `)`.
4. You have to divide by 6 at the very end.

If you forget even one bracket, or type `15 - 3 * 4 + 2 / 6` by accident, the calculator follows a confusing order and gives you `3.333` instead of `12`—with no clue where your mistake happened!

### Why Stack Math Feels Like Stacking Blocks
With Reverse Polish Notation on your SC-6, you solve one bite-sized piece at a time:
1. `{{res:sc6_02_rpn_for_young_learners_seq_42:keys}}` gives you $12.0$ right away. You can see it and check it!
2. `{{res:sc6_02_rpn_for_young_learners_seq_43:keys}}` gives you $6.0$. Now you see both building blocks ($12.0$ in $Y$, $6.0$ in $X$) side by side on your screen!
3. Tapping `{{key:×}}` multiplies them into $72.0$.
4. Tapping `6 {{key:÷}}` gives you the final answer: $12.0$!

You never have to balance tricky parentheses brackets or juggle extra numbers in your head. Your calculator's stack holds your building blocks right where you can see them!

---

<div class="admonition note">
<p class="admonition-title">For Parents &amp; Teachers: Cognitive Load, Working Memory &amp; The Diagnostic Playbook</p>
<p>
<strong>Cognitive Load &amp; Working Memory Metrics (RPN vs. Dijkstra's Shunting-Yard Burden):</strong> In algebraic infix calculators, evaluating expressions like $(15 - 3) \times (4 + 2) \div 6$ relies on Edsger Dijkstra's Shunting-Yard algorithm. This requires buffering pending operators and operands, quickly exceeding working memory token limits (typically $4 \pm 1$ items for elementary learners). If a student omits a parenthesis, operator precedence defaults to $15 - (3 \times 4) + (2 \div 6) = 3.333$, creating silent calculation errors. In RPN, evaluation is direct and postfix: working memory load never exceeds 2 active tokens, and every intermediate subtotal is immediately verified on the stack.<br><br>
<strong>The CRA Instructional Flow:</strong> In early elementary mathematics, Jerome Bruner's Concrete-Representational-Abstract (CRA) instructional progression {{cite:bruner1966}} ensures durable mastery. On the SC-6: (1) Concrete: The Elevator and Balance Scale mental models treat numbers as physical objects occupying vertical floors. (2) Representational: The horizontal $Y \mid X$ display layout aligns stack registers directly with natural left-to-right reading habits. (3) Abstract: The operator key is the evaluation event—combining quantities in real time with zero parentheses.<br><br>
<strong>The Two-Passenger Rule:</strong> Math operations combine two numbers at a time. The <code>{{key:ENTER}}</code> key is pressed once to place the first number safely into holding register $Y$. When the second number is keyed into register $X$, tapping the operator executes immediately. If a student keys numbers in reverse order ($3 - 15 = -12$), tapping <code>{{key:x⇄y}}</code> swaps registers instantly without erasing work.<br><br>
<strong>Diagnostic &amp; Remediation Table:</strong><br>
• <em>Types 5, then 3, screen shows 53:</em> Remind student that <code>{{key:ENTER}}</code> closes the elevator door.<br>
• <em>Result of $9 - 4$ shows $-5$:</em> Second number entered first; tap <code>{{key:x⇄y}}</code> then <code>{{key:-}}</code>.<br>
• <em>Taps <code>{{key:C}}</code> and loses number:</em> Explain that <code>{{key:C}}</code> clears; use <code>{{key:ENTER}}</code> to lift.<br>
• <em>Next number overwrites prior answer:</em> Do not clear; automatic stack lift preserves the prior total.<br>
• <em>Step counter adds 0:</em> Use <code>{{key:REP}}</code> or switch to 2-Stack (<code>2-LV</code>) mode.<br>
• <em>Taps <code>{{key:+}}</code> and nothing happens:</em> Only one passenger on stack; need two numbers to add.<br>
• <em>Division yields decimal 3.4 instead of quotient/remainder:</em> Use <code>{{key:÷R}}</code> for integer division with remainder.<br>
• <em>Self-Verification via <code>{{key:LASTX}}</code>:</em> Students verify calculations independently by pressing <code>{{key:LASTX}}</code> followed by the inverse operation (e.g. after $120 \div 8 = 15$, tapping <code>{{key:LASTX}} {{key:×}}</code> restores $120$).
</p>
</div>

---

## What You Mastered & Looking Ahead

Now that you've mastered pushing numbers onto the stack, swapping registers, and dropping calculations cleanly, let's travel back in time to discover how ancient pebble counters and ten human fingers created zero and the power of place value!