---
title: "Whole Number Operations & Skip-Counting Ladders"
description: "Mastering elementary multiplication, division, and RPN superpowers on the SC-6: 144-tile four-color arrays, the Four-Color Map Theorem, Superpower 1 [REP], Superpower 2 [÷R], and Superpower 4 [LASTX]."
---

# Whole Number Operations & Skip-Counting Ladders

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">WHOLE NUMBER OPERATIONS // CHAPTER 04</span>
  <span class="te-viewport-status text-emerald-400">● 144-TILE FOUR-COLOR ARRAYS &bull; FOUR-COLOR MAP THEOREM &bull; {{key:REP}} &bull; {{key:÷R}} &bull; {{key:LASTX}}</span>
</div>

## How 7-Year-Old Carl Friedrich Gauss Outsmarted His Teacher in 30 Seconds (and Why Multiplication Is a Physical Rectangle, Not a Memorized Song)

In the winter of 1784, inside a cold, dimly lit classroom in Brunswick, Germany, an exasperated schoolmaster named J.G. Büttner slammed his heavy wooden cane onto his oak podium. His classroom of boisterous boys was unruly, and Büttner desired an hour of absolute quiet.

Walking to the blackboard, he chalked an intimidating assignment: *Add every integer from 1 to 100 on your slates.*

$$\mathbf{1 + 2 + 3 + 4 + 5 + \dots + 98 + 99 + 100 = \ ?}$$

The schoolmaster settled back into his leather armchair, confident that his exhausted pupils would spend the rest of the morning bent over their slates in agonizing manual calculation.

Less than thirty seconds later, a skinny seven-year-old boy named Carl Friedrich Gauss {{cite:gauss1809}} stood up from his rough wooden bench. While his classmates were still desperately computing $1+2=3, 3+3=6, 6+4=10$, young Gauss calmly strode to the master's desk, slammed his slate face-down, and proclaimed in his native Low German dialect:

$$\text{\Large\textbf{„Ligget se!“}} \quad \text{("There it lies!")}$$

Büttner glared at the boy, certain he was bluffing. But at the end of the hour, when the slates were turned over, all the other boys had scribbled pages of error-riddled arithmetic. Only young Gauss’s slate contained the exact, perfect sum: **5,050**.

How did a seven-year-old outsmart an experienced schoolmaster in thirty seconds?

Gauss did not sing times tables in his head. He did not count on his fingers. He looked at the problem *spatially*. He noticed that the numbers could be folded in half like a piece of paper, pairing the extreme ends into identical sums:
$$1 + 100 = 101, \quad 2 + 99 = 101, \quad 3 + 98 = 101, \quad \dots \quad 50 + 51 = 101$$

There were exactly fifty pairs of $101$. And fifty groups of $101$ is not fifty tedious additions; it is a **geometric rectangle** measuring $50$ units wide by $101$ units tall:
$$50 \times 101 = 5,050$$

This is the great epiphany that conventional elementary school math so often conceals: **multiplication is not an arbitrary song you recite from memory; multiplication is a physical rectangle of space.** When you arrange tiles into equal rows and columns, the product is simply the physical area of the grid.

On the **StackCalc SC-6**, we honor Gauss's spatial insight. Using our physical **144-Tile Four-Color Array Studio**, you prove the commutative, associative, and distributive properties with your hands. And on the calculator keypad, you command three genuine computational superpowers: **Superpower 1 (`{{key:REP}}`)** for rhythmic skip-counting ladders, **Superpower 2 (`{{key:÷R}}`)** for instant simultaneous quotient and remainder display, and **Superpower 4 (`{{key:LASTX}}`)** for self-checking inverse arithmetic without scratch paper.

<div class="admonition note">
<p class="admonition-title">Chapter Baseline Mode: {{key:NUM}}</p>
<p>
Standard Base-10 Arithmetic &bull; 4-Stack XYZT &bull; Clean Transflective Display
</p>
</div>

<div class="admonition note">
<p class="admonition-title">Unlocked Keycaps Ribbon — Grades 2–4 Operations Suite</p>
<p>
• <strong>Arithmetic Operators:</strong> <code>{{key:+}}</code> Addition, <code>{{key:-}}</code> Subtraction, <code>{{key:×}}</code> Multiplication, <code>{{key:÷}}</code> Decimal Division.<br>
• <strong>RPN Superpowers:</strong> <code>{{key:REP}}</code> (Replicate Stack for Skip-Counting), <code>{{key:÷R}}</code> (Quotient &amp; Remainder), <code>{{key:LASTX}}</code> (Self-Checking Inverse Recall).<br>
• <strong>Stack Manipulation:</strong> <code>{{key:ENTER}}</code>, <code>{{key:x⇄y}}</code> (Swap Registers X and Y), <code>{{key:C}}</code> (Clear X), <code>{{key:<-}}</code> (Backspace).<br>
• <strong>Display Formatting:</strong> <code>{{key:NUM}}</code> (Whole Number Mode), <code>{{key:$}}</code> (Currency Mode).
</p>
</div>

---

{{res:sc6_bus_divr:screenshot|Field trip bus division: 145 students / 45-seat bus → Quotient 3, Remainder 10}}

## Concrete Foundation: 24-Tile Four-Color Array Studio & Map Theory

When you first learn multiplication, it might seem like a song to memorize. But multiplication is really **spatial equal groups**, **rectangular area arrays**, and **color-coded maps** you can build with your hands.

| Learning Stage | Physical Manipulative Kit | SC-6 Representational Sandbox | Abstract Operational Stack |
|---|---|---|---|
| **1. Concrete (Enactive)** | 24-Tile Four-Color Array Studio | Physical interlocking tiles and 90° array rotation | Tactile array perception |
| **2. Representational (Iconic)** | 4-Color Quadrant Partitioning & Map Theory | High-contrast LCD vector dot-matrix grid | Visual area model representation |
| **3. Abstract (Symbolic)** | Four-Register RPN Stack ($T, Z, Y, X$) | `Y {{key:ENTER}} X {{key:×}}` two-number drop | Chained parenthesis-free speed |

The StackCalc physical manipulative ecosystem replaces loose single-purpose blocks with the **24-Tile Four-Color Counting & Array Studio**:

<div class="admonition tip">
<p class="admonition-title">24-Tile Four-Color Counting &amp; Array Studio</p>
<p>
The physical manipulative studio provides 24 precision interlocking stacking tiles ($20.0 \times 20.0 \times 7.0\text{ mm}$) arranged across four distinct architectural palettes:
1. <strong>Archival White</strong> (crisp matte finish)<br>
2. <strong>Cobalt Blue</strong> (deep saturated tone)<br>
3. <strong>Radiant Gold</strong> (warm amber tone)<br>
4. <strong>Slate Gray</strong> (technical neutral tone)<br>
with exactly 6 tiles per color ($4 \times 6 = 24\text{ tiles}$). Each tile has a 1U visible height ($7.0\text{ mm}$), aligning with the 1/12th Fraction Studio tile so that 12 vertically stacked tiles match the $84.0\text{ mm}$ master datum of the 1-Whole Fraction Tower. Precision slip-fit chamfers allow smooth vertical stacking and planar docking without fatigue or sticking.
</p>
</div>

{{blocks:counting_tiles_box_3x1x13u|24-Tile Four-Color Counting & Array Studio in 3x1x13U Gridfinity Bin}}

### The Mathematical Harmony of $4 \times 6 = 24$
The number 24 divided into 4 colors creates rich mathematical properties for hands-on discovery:
1. **Highly Composite Versatility:** The 24-tile kit factors cleanly into $1 \times 24$, $2 \times 12$, $3 \times 8$, and $4 \times 6$ rectangular arrays.
2. **Four Complete $2 \times 3$ Sub-Arrays:** Each individual color contains **6 tiles**, which is both a $2 \times 3$ rectangular array and a triangular number ($1 + 2 + 3 = 6$).
3. **Model Small $\to$ Scale Big:** By modeling foundational $2 \times 3$, $3 \times 8$, and $4 \times 6$ arrays physically on the desk, you build concrete intuition before scaling up to large multi-digit arrays on the SC-6 stack!

| Array Orientation | Grid Dimensions | Row Breakdown | Total Area |
| :--- | :--- | :--- | :--- |
| **Array A** | $3\text{ Rows} \times 8\text{ Columns}$ | 3 rows of 8 tiles ($8 + 8 + 8$) | **$3 \times 8 = 24\text{ tiles}$** |
| **Array B** | $4\text{ Rows} \times 6\text{ Columns}$ | 4 rows of 6 tiles ($6 + 6 + 6 + 6$) | **$4 \times 6 = 24\text{ tiles}$** |

---

### Station Lesson 4.1: The 24-Tile Rectangular Array Studio & Multiplication Properties

<div class="admonition note">
<p class="admonition-title">Station Lesson 4.1: Tactile Setup</p>
<p>
&bull; <strong>Manipulatives:</strong> Counting &amp; Array Studio with 24 Precision Interlocking Tiles (4 colors &times; 6 tiles)<br>
&bull; <strong>Hardware:</strong> StackCalc SC-6 Elementary Calculator<br>
&bull; <strong>Core Goals:</strong> Tactile proof of Commutative, Associative, and Distributive properties with 4-register stack traces
</p>
</div>

{{blocks:counting_tiles_array_3x8|Commutative Property of Multiplication: 3x8 Array Rotated to 8x3 on Tabletop}}

#### 1. Commutative Property ($A \times B = B \times A$)
Build a solid rectangular mat of 3 rows of 8 tiles ($3 \times 8$).
Now, physically pick up the mat and rotate it by $90^\circ$ on the tabletop.
You now see 8 rows of 3 tiles ($8 \times 3$).
Did the number of tiles change? Not a single tile was added or removed!

On the SC-6 stack:
- Sequence 1: `{{res:sc6_04_operations_skip_counting_seq_53:keys}}` $\longrightarrow X = \mathbf{24}$.
- Sequence 2: `{{res:sc6_04_operations_skip_counting_seq_54:keys}}` $\longrightarrow X = \mathbf{24}$.

| Keystroke | Register T | Register Z | Register Y | Register X (Display) |
| :--- | :--- | :--- | :--- | :--- |
| {{key:3}} {{key:ENTER}} | 0 | 0 | 3 | 3 |
| {{key:8}} {{key:×}} | 0 | 0 | 0 | 24 |
| {{key:8}} {{key:ENTER}} | 0 | 24 | 8 | 8 |
| {{key:3}} {{key:×}} | 0 | 0 | 24 | 24 |

You see with your own eyes and feel with your own hands that spatial orientation does not alter the product.

#### 2. Associative Property ($(A \times B) \times C = A \times (B \times C)$)
Model small on your desk with two layers of $3 \times 4$ tiles ($12$ tiles per layer, $24$ tiles total), then scale big on your SC-6 to a three-layer block prism ($3 \times 4 \times 3 = 36$). Because each tile is $7.0\text{ mm}$ tall, 3 stacked tiles equal $21.0\text{ mm}$ (approximating 1 cubic unit):
- Method A: Multiply length by width first ($3 \times 4 = 12$), then multiply by height ($12 \times 3 = 36$).
- Method B: Multiply width by height first ($4 \times 3 = 12$), then multiply by length ($3 \times 12 = 36$).

On the SC-6:
- Keystrokes: `{{res:sc6_04_operations_skip_counting_seq_01:keys}}`$\longrightarrow X = \mathbf{36}$.

| Keystroke | Register T | Register Z | Register Y | Register X (Display) |
| :--- | :--- | :--- | :--- | :--- |
| {{key:3}} {{key:ENTER}} | 0 | 0 | 3 | 3 |
| {{key:4}} {{key:×}} | 0 | 0 | 0 | 12 |
| {{key:3}} {{key:×}} | 0 | 0 | 0 | 36 |

The operational stack handles continuous chained multiplication without requiring parentheses.

#### 3. Distributive Property & 4-Quadrant Area Models ($(a+b)(c+d)$)
Model small on your desk by arranging a $4 \times 4 = (2 + 2) \times (2 + 2) = 16$-tile square using four $2 \times 2$ color quadrants ($4 + 4 + 4 + 4 = 16$ tiles). Now scale big on your SC-6 to decompose $(10 + 2) \times (10 + 2)$ into four partial products across four quadrants:
$$(10 + 2) \times (10 + 2) = (10 \times 10) + (10 \times 2) + (2 \times 10) + (2 \times 2) = 100 + 20 + 20 + 4 = 144$$

| Partial Product Quadrant | Dimensions | Area Value |
| :--- | :--- | :--- |
| **Upper-Left ($10 \times 10$)** | $10\text{ rows} \times 10\text{ columns}$ | $100\text{ square units}$ |
| **Upper-Right ($10 \times 2$)** | $10\text{ rows} \times 2\text{ columns}$ | $20\text{ square units}$ |
| **Lower-Left ($2 \times 10$)** | $2\text{ rows} \times 10\text{ columns}$ | $20\text{ square units}$ |
| **Lower-Right ($2 \times 2$)** | $2\text{ rows} \times 2\text{ columns}$ | $4\text{ square units}$ |
| **Total Distributive Area** | $(10 + 2) \times (10 + 2) = 12 \times 12$ | **$144\text{ square units}$** |

{{blocks:counting_tiles_distributive_4color|Four-Color Distributive Area: (10 + 2) x (10 + 2) = 144 Square Units across 4 Quadrants}}

On the SC-6:
- Keystrokes: `{{res:sc6_04_operations_skip_counting_seq_02:keys}}`$\longrightarrow X = \mathbf{144}$.

| Keystroke | Register T | Register Z | Register Y | Register X (Display) |
| :--- | :--- | :--- | :--- | :--- |
| `10` {{key:ENTER}} | 0 | 0 | 10 | 10 |
| {{key:2}} {{key:+}} | 0 | 0 | 0 | 12 |
| `10` {{key:ENTER}} | 0 | 12 | 10 | 10 |
| {{key:2}} {{key:+}} | 0 | 0 | 12 | 12 |
| {{key:×}} | 0 | 0 | 0 | 144 |

The four colors turn an abstract polynomial identity into an intuitive spatial puzzle.

---

### The Four-Color Map Theorem Station Game
In 1976, Kenneth Appel and Wolfgang Haken proved that **no more than four colors are required** to color any planar map so that no two adjacent regions share a color.

**Station Game: "Planar Map Showdown"**
* **Players:** 2 to 4 players.
* **Rules:** Players take turns placing a counting tile onto the table grid to expand a contiguous "country". A placed tile may **never share a side edge** with a tile of the same color (diagonal corners are allowed).
* **The Challenge:** You discover that no matter how winding or complex the border network becomes, you **never need a 5th color**! If a player cannot legally place their color, they must skip their turn. The player with the most legal placements wins.

## Addition & Subtraction Dynamics: Regrouping Without Fear

### The Crisis of the Standard "Borrowing" Algorithm
In traditional arithmetic instruction, multi-digit subtraction ($92 - 38$) is taught through mechanical column borrowing:
1. "Look at the ones column: $2 - 8$. You can't take 8 from 2."
2. "Cross out the 9, make it an 8."
3. "Put a little 1 next to the 2 to make it 12."
4. "$12 - 8 = 4$."
5. "$8 - 3 = 5$."
6. "Answer: 54."

When you learn traditional column borrowing, it's easy to fall into two confusing habits:
- Seeing the "little 1" as an arbitrary mark rather than a physical bundle of **10 units** transferred from the tens column.
- Feeling anxious when crossing out numbers, treating it like an error rather than keeping the total quantity invariant.

### Mental Math Regrouping Strategies
With the SC-6, you can explore flexible mental math strategies that build true intermediate number awareness:

#### Strategy 1: The Compensation Method ($92 - 38$)
Instead of subtracting 38, subtract the friendly landmark number 40, and then compensate by adding 2 back:
$$92 - 38 = (92 - 40) + 2 = 52 + 2 = 54$$
On the SC-6 stack:
- `{{res:sc6_04_operations_skip_counting_seq_55:keys}}` $\longrightarrow X = \mathbf{54}$.

#### Strategy 2: Bridging Tens ($47 + 38$)
Decompose 38 into $30 + 3 + 5$:
$$47 + 30 = 77 \quad \longrightarrow \quad 77 + 3 = 80 \quad \longrightarrow \quad 80 + 5 = 85$$
On the SC-6:
- `{{res:sc6_04_operations_skip_counting_seq_56:keys}}` $\longrightarrow X = \mathbf{85}$.
Every step is evaluated in real time, giving immediate diagnostic confirmation.

---

## Superpower 1: Rhythmic Skip-Counting Ladders (`{{key:REP}}`)

In math class, times tables are mastered through **rhythmic skip-counting**. On conventional algebraic calculators, doing this requires repeatedly typing `+ 7 = = =`, which is easily disrupted if you pause, clear, or double-tap.

On classic scientific RPN calculators like the HP-32SII, loading a constant multiplier into Register $T$ required pressing `{{key:ENTER}}` three times (`{{key:7}} {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}`). That is cumbersome and easy to forget.

The SC-6 introduces **Superpower 1 (`{{key:REP}}`)** on Row 3, Col 4. In a single click, `{{key:REP}}` replicates the contents of Register $X$ across all four registers ($T, Z, Y, X$).

<div class="admonition note">
<p class="admonition-title">Superpower 1: Stack Replication {{key:REP}}</p>
<p>
• <strong>Enter Step Constant:</strong> Type <code>{{key:7}}</code>.<br>
• <strong>Press <code>{{key:REP}}</code>:</strong> Replicates the constant across every level: Register T = 7 (Top Floor Permanent Constant), Register Z = 7, Register Y = 7, Register X = 7.<br>
• <strong>The Ladder Invariant:</strong> Each time you tap <code>{{key:+}}</code>, Register T drops downward to replenish the stack, maintaining the constant step indefinitely without re-typing!
</p>
</div>

### Station Lesson 4.2: Skip-Counting Ladders with Superpower 1 (`{{key:REP}}`)

<div class="admonition note">
<p class="admonition-title">Station Lesson 4.2: Tactile Setup</p>
<p>
&bull; <strong>Manipulatives:</strong> Counting &amp; Array Studio, Batches of Stacking Tiles arranged in equal groups<br>
&bull; <strong>Hardware:</strong> StackCalc SC-6 in 4-Stack Mode with <code>{{key:REP}}</code> key<br>
&bull; <strong>Cadence:</strong> Physical group addition paired with RPN stack collapse
</p>
</div>

#### 1. Skip-Counting by Sevens: The 7s Ladder
Let us generate the multiples of 7:
1. Type `{{key:7}}`.
2. Press {{key:REP}} (Row 3, Col 4). Every register ($T, Z, Y, X$) now holds 7!
3. Now simply tap `{{key:+}}` rhythmically as you place each physical 7-tile bar onto the table:

| Keystroke | Register T (Constant) | Register Z | Register Y | Register X (Ladder) |
| :--- | :--- | :--- | :--- | :--- |
| {{key:7}} | 0 | 0 | 0 | 7 |
| {{key:REP}} | 7 | 7 | 7 | 7 |
| {{key:+}} | 7 | 7 | 7 | 14 |
| {{key:+}} | 7 | 7 | 7 | 21 |
| {{key:+}} | 7 | 7 | 7 | 28 |
| {{key:+}} | 7 | 7 | 7 | 35 |
| {{key:+}} | 7 | 7 | 7 | 42 |
| {{key:+}} | 7 | 7 | 7 | 49 |
| {{key:+}} | 7 | 7 | 7 | 56 |
| {{key:+}} | 7 | 7 | 7 | 63 |
| {{key:+}} | 7 | 7 | 7 | 70 |

Because Register $T$ constantly duplicates its value down during two-number stack drop, you can march through the entire times table ($7, 14, 21, 28 \dots 70$) in cadence with clapping drills or physical stepping.

#### 2. Skip-Counting by Twelves (Dozens Ladder)
The number 12 is fundamental to everyday life (dozens of eggs, hours on a clock, inches in a foot, months in a year).
1. Type `12`.
2. Press {{key:REP}}. All registers hold 12!
3. Tap `{{key:+}}` rhythmically to climb:
   $$\mathbf{24, 36, 48, 60, 72, 84, 96, 108, 120}$$

| Dozens ($1\text{–}4$) | Dozens ($5\text{–}8$) | Dozens ($9\text{–}12$) |
| :--- | :--- | :--- |
| $1\text{ Dozen} = 12\text{ eggs}$ | $5\text{ Dozen} = 60\text{ eggs}$ | $9\text{ Dozen} = 108\text{ eggs}$ |
| $2\text{ Dozen} = 24\text{ eggs}$ | $6\text{ Dozen} = 72\text{ eggs}$ | $10\text{ Dozen} = 120\text{ eggs}$ |
| $3\text{ Dozen} = 36\text{ eggs}$ | $7\text{ Dozen} = 84\text{ eggs}$ | $11\text{ Dozen} = 132\text{ eggs}$ |
| $4\text{ Dozen} = 48\text{ eggs}$ | $8\text{ Dozen} = 96\text{ eggs}$ | $12\text{ Dozen} = \mathbf{144}\text{ (1 Gross!)}$ |

#### 3. The Doubling Ladder: Geometric Powers
Doubling is one of the most powerful mental math strategies in Grade 2 and 3.
How do living cells divide, or how do digital computer memory chips scale?
1. Enter `{{key:2}} {{key:ENTER}}`.
2. Press `{{key:ENTER}} {{key:+}}`: $2 + 2 = \mathbf{4}$.
3. Press `{{key:ENTER}} {{key:+}}`: $4 + 4 = \mathbf{8}$.
4. Press `{{key:ENTER}} {{key:+}}`: $8 + 8 = \mathbf{16}$.
5. Press `{{key:ENTER}} {{key:+}}`: $16 + 16 = \mathbf{32}$.
6. Continue climbing: $\mathbf{64, 128, 256, 512, 1024}$!

> **YOUR STACK SUPERPOWER CHECKPOINT:**
> • Pressing {{key:ENTER}} duplicates the number in Register X into Register Y.
> • Pressing {{key:+}} immediately combines them into double their value!
> • This two-key rhythm ({{key:ENTER}} {{key:+}}) lets you double any number instantly.

---

## Superpower 2: Simultaneous Quotient & Remainder (`{{key:÷R}}`)

<div class="admonition tip">
<p class="admonition-title">Why Long Division Causes Tears vs {{key:÷R}}</p>
<p>
<strong>The Scenario:</strong> You face: <em>"Divide 43 by 6."</em><br><br>
<strong>The Traditional Homework Trap:</strong><br>
You are taught to divide, multiply, subtract, and bring down. If you type it into a standard smartphone calculator, the screen displays: <code>7.16666666667</code>.<br>
You wonder: <em>"Where did 0.1666 come from? My teacher wants a remainder!"</em> How do you convert decimals back to leftovers?<br><br>
<strong>The 10-Second RPN Superpower:</strong><br>
On your SC-6, press: <code>43 {{key:ENTER}} 6 {{key:÷R}}</code>.<br>
The transflective LCD splits instantly:
</p>
<ul>
  <li><strong>Register X displays:</strong> <code>7</code> (The whole Quotient)</li>
  <li><strong>Register Y displays:</strong> <code>1</code> (The exact Remainder!)</li>
</ul>
<p>
To inspect the remainder, simply tap <code>{{key:x⇄y}}</code>!<br>
To check your work with Superpower 4: <code>{{key:LASTX}} {{key:×}} {{key:+}}</code> &rarr; <code>43</code>! Instant self-proof! Zero decimals. Zero tears. Total mathematical confidence.
</p>
</div>

In elementary school math, long division produces a **whole quotient** and a **remainder**. Traditional calculators display unwieldy decimals ($17 \div 5 = 3.4$), completely obscuring the physical meaning of equal groups and leftovers.

The SC-6 introduces **Superpower 2: Integer Division with Remainder (`{{key:÷R}}`)** on Row 2, Col 5:

<div class="admonition note">
<p class="admonition-title">Superpower 2: Integer Division with Remainder ({{key:÷R}})</p>
<p>
Given Dividend Y and Divisor X:<br>
&bull; <strong>Register X</strong> receives the whole integer Quotient: $Q = \mathrm{trunc}(Y / X)$<br>
&bull; <strong>Register Y</strong> receives the whole integer Remainder: $R = Y \bmod X$<br>
&bull; Tapping <code>{{key:x⇄y}}</code> instantly swaps registers to inspect the Remainder!
</p>
</div>

### Algebraic Trap vs. StackCalc Superpower Showdown: Division with Remainder

| Challenge / Equation | The Algebraic Calculator Trap (TI-30X / Smartphone) | The StackCalc SC-6 + Manipulative Superpower | Keystroke Reduction | Live Stack Visibility | Pedagogical Breakthrough |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **Integer Division with Remainder:**<br>$185 \div 12$ | `1 8 5 / 1 2 =`<br>$\rightarrow 15.41666667$.<br>To extract integer remainder:<br>`- 15 = * 12 =`<br>(18 keystrokes).<br>Self-check requires retyping:<br>`15 * 12 + 5 =`<br>(28 total keystrokes).<br>*Trap: Decimals obscure discrete items; scratch paper required.* | **SC-6 + 24-Cube Array Studio &amp; Egg Cartons:**<br>`185 {{key:ENTER}} 12 {{key:÷R}}`<br>(7 keystrokes).<br>Simultaneously displays Quotient $Q = 15$ in Register $X$ and Remainder $R = 5$ in Register $Y$!<br>Tap `{{key:x⇄y}}` to swap.<br>Self-check in 3 keys:<br>`{{key:LASTX}} {{key:×}} {{key:+}}`<br>$\rightarrow 185$! | **75% fewer keystrokes**<br>(7 vs. 28) | **Dual Live Registers:**<br>Quotient $Q$ and Remainder $R$ visible simultaneously on the transflective screen; zero scratch paper. | **Discrete Math Alignment:**<br>Eliminates decimal confusion in discrete sharing problems; transforms long division into an intuitive physical packaging and self-checking workflow. |

### Station Lesson 4.3: Equal Group Packaging & Remainder Sorting with Superpower 2 (`{{key:÷R}}`)

<div class="admonition note">
<p class="admonition-title">Station Lesson 4.3: Tactile Setup</p>
<p>
&bull; <strong>Manipulatives:</strong> Counting &amp; Array Studio, 23 Stacking Tiles on desk<br>
&bull; <strong>Hardware:</strong> StackCalc SC-6 Elementary with <code>{{key:÷R}}</code> integer division<br>
&bull; <strong>Physical Goal:</strong> Deal 23 tiles into equal groups of 5; isolate remainders
</p>
</div>

> **DESK DEALING LAYOUT (23 TILES DIVIDED BY 5):**
> GROUP 1: [⬜][⬜][⬜][⬜][⬜] (5 Tiles)
> GROUP 2: [⬜][⬜][⬜][⬜][⬜] (5 Tiles)
> GROUP 3: [⬜][⬜][⬜][⬜][⬜] (5 Tiles)
> GROUP 4: [⬜][⬜][⬜][⬜][⬜] (5 Tiles)
> REMAINDER: [🟦][🟦][🟦]       (3 Loose Leftover Tiles!)
> Total: 4 Groups × 5 Tiles + 3 Remainder = 23 Tiles!

#### Step-by-Step Hands-On Protocol:
1. **Concrete Dealing:** Count out 23 tiles and divide them into piles of 5. You find you can make exactly 4 complete piles, but 3 tiles remain loose on your desk.
2. **RPN Execution:**
   - Type `23 {{key:ENTER}} {{key:5}} {{key:÷R}}`.
   - Register $X$ displays: $\mathbf{4}$ (The 4 full equal groups!).
   - Register $Y$ holds: $\mathbf{3}$ (The 3 loose leftover tiles!).
3. **Register Swap:**
   - Tap `{{key:x⇄y}}`: The active display shifts to $\mathbf{3}$, bringing the remainder directly to your eyes.
   - Tap `{{key:x⇄y}}` again: Returns to quotient $\mathbf{4}$.

| Keystroke | Register T | Register Z | Register Y | Register X (Display) |
| :--- | :--- | :--- | :--- | :--- |
| `23` {{key:ENTER}} | 0 | 0 | 23 | 23 |
| {{key:5}} | 0 | 0 | 23 | 5 |
| {{key:÷R}} | 0 | 0 | 3 | 4 |
| {{key:x⇄y}} | 0 | 0 | 4 | 3 |

---

### Real-World Problem 1: Egg Carton Packaging (12 Eggs per Carton)
A farm gathers 147 fresh eggs in the morning. Each carton holds exactly 12 eggs. How many full cartons can be packed for the farmer's market, and how many loose eggs are left over?

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `147` | 0 | 0 | 0 | 147 |
| {{key:ENTER}} | 0 | 0 | 147 | 147 |
| `12` | 0 | 0 | 147 | 12 |
| {{key:÷R}} | 0 | 0 | 3 | 12 |
| {{key:x⇄y}} | 0 | 0 | 12 | 3 |

> **DIAGNOSTIC VERIFICATION:**
> • Register X = 12 (There are 12 full cartons of eggs!).
> • Press {{key:x⇄y}} $\to$ Register X = 3 (There are 3 loose eggs left over!).
> • Mathematical proof: (12 cartons × 12 eggs) + 3 remainder = 144 + 3 = 147!

---

### Real-World Problem 2: Bakery Muffin Trays (6 Muffins per Tray)
A bakery oven bakes 86 apple cinnamon muffins. Each baking tray holds 6 muffins. How many full trays are filled, and how many extra muffins remain?

1. Type `86 {{key:ENTER}} {{key:6}} {{key:÷R}}`.
   - Register $X$ displays: $\mathbf{14}$ (14 full trays!).
   - Register $Y$ holds: $\mathbf{2}$ (2 leftover muffins).
2. Tap `{{key:x⇄y}}` to inspect the remainder: Register $X = \mathbf{2}$.

---

### Real-World Problem 3: School Field Trip Buses (54 Passengers per Bus)
An elementary school is taking 380 students and chaperones on a science museum field trip. Each chartered bus has 54 seats. How many full buses are needed, and how many people must ride on an additional bus?

1. Type `380 {{key:ENTER}} 54 {{key:÷R}}`.
   - Register $X$ displays: $\mathbf{7}$ (7 full buses carrying $7 \times 54 = 378$ people).
   - Register $Y$ holds: $\mathbf{2}$ (2 people left over).
2. **Think About It:** *"Can we order 7 buses?"*
   - No! Those 2 people cannot be left behind at school. The school must order **8 buses** in total! (Ceiling division: if remainder $> 0$, add 1 bus!).

---

### Real-World Problem 4: Dividing Classroom Chore Earnings
Four siblings earn $\$17.50$ raking autumn leaves. How much whole dollar money does each sibling receive, and what remainder must be shared in pennies?

1. Type `17.50 {{key:ENTER}} {{key:4}} {{key:÷R}}`.
   - Register $X$ displays: $\mathbf{4.00}$ (Each sibling receives $\$4.00$).
   - Register $Y$ holds: $\mathbf{1.50}$ (Remainder of $\$1.50$ left over).
2. Tap `{{key:x⇄y}}` to verify the $\$1.50$ remainder.

---

### The Euclidean Algorithm for Greatest Common Divisor via `{{key:÷R}}`
As you advance in math, you will discover Euclid's timeless algorithm for finding the Greatest Common Factor (GCF) of two large numbers:
$$\gcd(a, b) = \gcd(b, a \bmod b)$$

On the SC-6, Superpower 2 executes this algorithm with breathtaking elegance:
Find $\gcd(252, 105)$:
1. `252 {{key:ENTER}} 105 {{key:÷R}}` $\longrightarrow Q = 2, R = \mathbf{42}$ in Register $Y$.
2. Tap `{{key:x⇄y}}` to bring remainder 42 to $X$.
3. We divide prior divisor 105 by 42: `105 {{key:x⇄y}} {{key:÷R}}` $\longrightarrow Q = 2, R = \mathbf{21}$ in Register $Y$.
4. Tap `{{key:x⇄y}}` to bring remainder 21 to $X$.
5. We divide 42 by 21: `42 {{key:x⇄y}} {{key:÷R}}` $\longrightarrow Q = 2, R = \mathbf{0}$!
6. The last non-zero remainder is **21**! Therefore, $\gcd(252, 105) = \mathbf{21}$!

---

## Superpower 4: Self-Checking Inverse Arithmetic (`{{key:LASTX}}`)

A great mathematician never simply accepts an answer—they prove it using **inverse operations**.

On conventional calculators, self-checking requires clearing the screen and re-typing the entire calculation backwards. On the SC-6, **Superpower 4 (`{{key:LASTX}}`)** preserves the prior number before the operation executed:

<div class="admonition note">
<p class="admonition-title">Superpower 4: Self-Checking Inverse ({{key:LASTX}})</p>
<p>
&bull; Whenever an operation executes, Register X's prior value is saved in the hardware <code>LASTX</code> register.<br>
&bull; Tapping <code>{{key:LASTX}}</code> pushes that number back into Register X, while automatically lifting the calculated result into Register Y!<br>
&bull; You can immediately execute the inverse operation with <strong>zero re-typing</strong>!
</p>
</div>

---

### Inverse Verification 1: Checking Addition with Subtraction
Let us verify $47 + 36 = 83$:
1. Add the numbers: `{{res:sc6_04_operations_skip_counting_seq_57:keys}}` $\longrightarrow X = \mathbf{83}$.
2. Press {{key:LASTX}} (Row 2, Col 3):
   - $36$ is recalled into Register $X$.
   - $83$ is automatically lifted into Register $Y$.
3. Press `{{key:-}}` to execute the inverse check:
   - $83 - 36 = \mathbf{47}$!
   - We have restored our starting quantity with 100% mathematical certainty!

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `47` | 0 | 0 | 0 | 47 |
| {{key:ENTER}} | 0 | 0 | 47 | 47 |
| `36` | 0 | 0 | 47 | 36 |
| {{key:+}} | 0 | 0 | 0 | 83 |
| {{key:LASTX}} | 0 | 0 | 83 | 36 |
| {{key:-}} | 0 | 0 | 0 | 47 |

---

### Inverse Verification 2: Checking Multiplication with Division
Let us verify $15 \times 8 = 120$:
1. Multiply: `{{res:sc6_04_operations_skip_counting_seq_58:keys}}` $\longrightarrow X = \mathbf{120}$.
2. Press {{key:LASTX}}:
   - $8$ is recalled into Register $X$.
   - $120$ is lifted into Register $Y$.
3. Press `{{key:÷}}`:
   - $120 \div 8 = \mathbf{15}$!

---

### Inverse Verification 3: Checking Subtraction with Addition
Let us verify $95 - 38 = 57$:
1. Subtract: `{{res:sc6_04_operations_skip_counting_seq_59:keys}}` $\longrightarrow X = \mathbf{57}$.
2. Press {{key:LASTX}}:
   - $38$ is pushed into Register $X$.
   - $57$ is lifted into Register $Y$.
3. Press `{{key:+}}`:
   - $57 + 38 = \mathbf{95}$! Original starting value confirmed!

---

### Inverse Verification 4: Checking Division with Multiplication
Let us verify $84 \div 7 = 12$:
1. Divide: `{{res:sc6_04_operations_skip_counting_seq_60:keys}}` $\longrightarrow X = \mathbf{12}$.
2. Press {{key:LASTX}}:
   - $7$ is recalled into Register $X$.
   - $12$ is lifted into Register $Y$.
3. Press `{{key:×}}`:
   - $12 \times 7 = \mathbf{84}$! Original dividend restored!

---

## 5th Grader Extreme Math Challenges: Doubling to the Sky & Your Age in Seconds!

Think multiplication is just boring times tables? Try these two extreme challenges on your SC-6 and test them on your family:

### Challenge 1: What Happens If You Fold a Piece of Paper 10 Times with `{{key:REP}}`?
A sheet of notebook paper is only $1\text{ layer}$ thick. Every time you fold it in half, the number of layers **doubles** ($\times 2$). Can you fold a piece of paper 10 times with your bare hands? Almost nobody can—and Superpower 1 (`{{key:REP}}`) shows why!
* Seed the stack with `2` and tap `{{key:×}}` nine times to see 10 doublings ($2^{10}$):
  `{{res:sc6_04_paper_fold_10_rep:keys}}` $\longrightarrow$ **`{{res:sc6_04_paper_fold_10_rep:value}}` layers** (thicker than a 1,000-page dictionary!).

1. Tap `2` `{{key:REP}}` to lock constant factor 2 into every stack floor ($T = Z = Y = X = 2$), priming the physical doubling mechanism {{cite:parker2019}}.
2. Tap `{{key:×}}` for the 1st fold: 2 layers double to 4 ($X = 4$), while constant 2 drops down from Floor $T$ to wait on Floor $Y$.
3. Tap `{{key:×}}` for the 2nd fold: 4 layers double to 8 ($X = 8$), already thicker than standard cardstock.
4. Tap `{{key:×}}` for the 3rd fold: 8 layers double to 16 ($X = 16$), resisting thumb pressure.
5. Tap `{{key:×}}` for the 4th fold: 16 layers double to 32 ($X = 32$), thick like a deck of index cards.
6. Tap `{{key:×}}` for the 5th fold: 32 layers double to 64 ($X = 64$), stiff like a wooden slat.
7. Tap `{{key:×}}` for the 6th fold: 64 layers double to 128 ($X = 128$), impossible to crease with bare fingers.
8. Tap `{{key:×}}` for the 7th fold: 128 layers double to 256 ($X = 256$), thick like a textbook.
9. Tap `{{key:×}}` for the 8th fold: 256 layers double to 512 ($X = 512$), a full 500-sheet ream of copy paper.
10. Tap `{{key:×}}` for the 9th fold: 512 layers double to 1,024 ($X = 1024$), towering like a colossal phone directory!

* If you keep tapping `{{key:×}}` 10 more times ($20\text{ folds} = 1,048,576\text{ layers}$), that single sheet of paper would be taller than the Empire State Building!

### Challenge 2: How Many Seconds Old Are You Right Now?
If you are **11 years old** in 5th grade, have you lived for a million seconds yet? What about a *billion* seconds? Let's chain the multiplication right on the stack ($11\text{ years} \times 365\text{ days} \times 24\text{ hours} \times 60\text{ minutes} \times 60\text{ seconds}$):
**Keystrokes:** `{{res:sc6_04_seconds_in_11_years:keys}}` $\longrightarrow$ **`{{res:sc6_04_seconds_in_11_years:value}}` seconds**!

1. Tap `11` `{{key:ENTER}}` to set your 11-year age baseline onto the upper mezzanine shelf ($Y = 11$).
2. Tap `365` `{{key:×}}` to fold in days per year: $11 \times 365 = 4,015\text{ days}$ of sunrise and sunset resting on the active floor ($X = 4015$).
3. Tap `24` `{{key:×}}` to fold in hours per day: $4,015 \times 24 = 96,360\text{ hours}$ lived ($X = 96360$).
4. Tap `60` `{{key:×}}` to convert hours to minutes: $96,360 \times 60 = 5,781,600\text{ minutes}$ ($X = 5781600$).
5. Tap `60` `{{key:×}}` to convert minutes to seconds: $5,781,600 \times 60 = 346,896,000\text{ seconds}$ ticking past on the LCD screen!

* You blew past $1,000,000\text{ seconds}$ when you were only $11.5\text{ days}$ old—and at 11 years old, you are already more than **one-third of the way to 1 Billion seconds**!

---

<div class="admonition note">
<p class="admonition-title">For Parents &amp; Teachers: Division as Partitioning &amp; Inverse Verification</p>
<p>
<strong>Division as Partitioning vs. Decimal Abstraction:</strong> In elementary classrooms, long division often presents a severe pedagogical hurdle {{cite:ma1999}}. Traditional calculators compound this difficulty by outputting continuous decimal quotients: $17 \div 5 = 3.4$. In concrete situations involving discrete objects—such as packing egg cartons, grouping students, or cutting materials—a fractional decimal fails to match physical intuition {{cite:singapore2014}}.<br><br>
Superpower 2 (<code>{{key:÷R}}</code>) aligns calculator output directly with discrete partitioning. By placing the whole-number quotient $Q$ in Register $X$ and the integer remainder $R$ in Register $Y$, the SC-6 mirrors physical manipulation: 17 units divide into 3 complete groups of 5 with 2 loose units remaining. Tapping <code>{{key:x⇄y}}</code> swaps registers instantaneously, enabling inspection of both components without recalculation.<br><br>
<strong>Self-Checking and the Inverse Verification Strategy:</strong> Developing mathematical autonomy requires moving learners away from external answer validation toward internal verification. Superpower 4 (<code>{{key:LASTX}}</code>) provides direct support for George Pólya's classic "look back" problem-solving strategy {{cite:polya1945}}.<br><br>
By preserving the argument of the most recent operation in the non-volatile <code>LASTX</code> register, the SC-6 allows students to verify results using inverse operations without re-entering values:
after addition ($47 + 36 = 83.0$), tapping <code>{{key:LASTX}} {{key:-}}</code> immediately returns to $47.0$; after division ($120 \div 8 = 15.0$), executing <code>{{key:LASTX}} {{key:×}}</code> multiplies back to $120.0$.<br><br>
<strong>Stack Constant Seeding &amp; Fluency:</strong> Superpower 1 (<code>{{key:REP}}</code>) populates all four stack registers ($T, Z, Y, X$) with the entered step value in a single instruction {{cite:macaulay2016}}, powering rhythmic skip-counting ladders and building structural number sense.
</p>
</div>

<div class="admonition note">
<p class="admonition-title">For Parents &amp; Teachers: Classroom Dialogue Scripts &amp; Misconception Diagnostics</p>
<p>
<strong>Script 4.1: The Field Trip Bus Ceiling Trap:</strong> When dividing $145$ students across $40$-seat buses (<code>145 {{key:ENTER}} 40 {{key:÷R}}</code> &rarr; $X=3, Y=25$), remind students that $25$ people cannot be left behind. Any remainder greater than zero requires ordering an additional bus ($3 + 1 = 4$ buses!).<br><br>
<strong>Script 4.2: Array Rotation &amp; The Commutative Miracle:</strong> Rotating a $3 \times 8$ counting tile array into an $8 \times 3$ array proves that $A \times B = B \times A$ without altering the physical tile count (both evaluate to $24$).<br><br>
<strong>Script 4.3: The Magic Mirror of LASTX:</strong> If a student multiplies $18 \times 7 = 126$, pressing <code>{{key:LASTX}} {{key:÷}}</code> restores the starting $18$, proving the answer without scratch paper.<br><br>
<strong>Script 4.4: Leftovers vs. Decimals in Pizza Sharing:</strong> Four friends sharing $15$ pizza slices (<code>15 {{key:ENTER}} 4 {{key:÷R}}</code>) receive 3 slices each with 3 whole slices left in the box for tomorrow, avoiding awkward decimal cuts ($3.75$).
</p>
</div>

---

## RPN Stack Diagnostic & Remediation Playbook

The following diagnostic table addresses the ten most common beginner stumbling blocks encountered during operations, skip-counting, and remainder division:

| Common Mistake / What You See | Why It Happened | How to Fix It on the Stack |
|:---|:---|:---|
| **1. In skip-counting, `{{key:REP}}` was not pressed; `{{key:+}}` adds 0** | Forgot to seed all registers with REP. | Type step constant, press {{key:REP}}! |
| **2. In division, expected remainder but got decimal** | Pressed `{{key:÷}}` instead of integer division. | Use {{key:÷R}} for whole quotient &amp; remainder! |
| **3. Cannot see remainder after pressing `{{key:÷R}}`** | Remainder is in Register Y; Register X holds quotient. | Tap `{{key:x⇄y}}` to swap and inspect remainder! |
| **4. Self-check inverse gave wrong answer** | Pressed wrong inverse operator. | Addition pairs with `-`; multiplication pairs with `÷`! |
| **5. Doubling ladder did not double** | Did not press `{{key:ENTER}}` before `{{key:+}}`. | Press `{{key:ENTER}} {{key:+}}` to duplicate and add! |
| **6. Multiplication product was too small** | Pressed `{{key:+}}` instead of `{{key:×}}`. | `{{key:×}}` multiplies; `{{key:+}}` only adds. |
| **7. Subtraction gave negative number (e.g., -54)** | Entered second number before starting number. | Enter starting number, `{{key:ENTER}}`, then subtract. |
| **8. Pressed `{{key:C}}` after first product in chained sum** | Believed screen had to be cleared. | Do not clear! Stack lifts automatically! |
| **9. Field trip bus answer was short by one bus** | Forgot that any leftover requires an additional bus. | If remainder > 0, round up by 1 whole bus! |
| **10. `LASTX` recalled unexpected number** | Executed another operation after error. | `LASTX` updates on **every** operation! |

---

## Comprehensive Worked Reference Problems (50 Elementary Reference Problems)

<div class="admonition tip">
<p class="admonition-title">Hands-On Studio Proof: Blocks &rarr; Calculator</p>
<p>
<strong>Step 1 (Physical Concrete Intuition):</strong> Take 24 precision stacking tiles from your 24-Tile Array Studio. Build a solid rectangular array of 3 rows with 8 tiles each ($3 \times 8$). Count the rows and columns: 24 total tiles. Now physically rotate the entire tile tray $90^\circ$ on the tabletop. You now see 8 rows of 3 tiles ($8 \times 3$). Not a single tile was added or lost: the physical area is invariant.<br>
<strong>Step 2 (The Representational Bridge):</strong> Enter the calculation on your SC-6: <code>3 {{key:ENTER}} 8 {{key:×}}</code> &rarr; <code>24</code>. Now verify the rotated physical array: <code>8 {{key:ENTER}} 3 {{key:×}}</code> &rarr; <code>24</code>. Tap <code>{{key:LASTX}} {{key:÷}}</code> to execute the inverse check: <code>24 &divide; 3 = 8</code>! Every physical manipulation maps directly to a stack operation.<br>
<strong>Step 3 (Scaling on the Calculator):</strong> Now scale beyond the physical tabletop limits. You cannot easily lay out an orchard of 48 rows with 36 apple trees each on your desk—but your SC-6 evaluates <code>48 {{key:ENTER}} 36 {{key:×}}</code> &rarr; <code>1,728</code> trees in a fraction of a second, with the exact same spatial truth!
</p>
</div>

### Expedition 1: The Saturday Morning Bakehouse & Master Orchard (Problems 4.1–4.8)
*Mission Briefing:* You are the head baker and master orchardist preparing goods for the weekend market. You must calculate baking tray capacities, arrange fruit crate matrices, and rotate cookie cooling grids—verifying that commutativity and spatial area always protect your production counts.

#### Problem 4.1: Four-Color Counting Tile Array ($3 \times 8 = 24$)
At dawn in the Saturday morning bakehouse, the pastry chef prepares a rectangular baking sheet by snapping together 3 rows of 8 Archival White counting tiles on the workstation desk to model fresh sugar cookies. Rather than counting individual cookies one by one, multiplication treats the tray as a single cohesive rectangle of space ($3 \times 8 = 24$).

On your SC-6, key in `{{res:sc6_04_operations_skip_counting_seq_03:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_03:value}}`**. Keying `3 {{key:ENTER}}` lifts the row dimension into Register $Y$, and tapping `8 {{key:×}}` multiplies on the ground floor to display $24$ cookies in active Register $X$.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| {{key:3}} | 0 | 0 | 0 | 3 | Key in row count; value enters active Register $X$ |
| {{key:ENTER}} | 0 | 0 | 3 | 3 | Lift row dimension to holding Register $Y$ |
| {{key:8}} | 0 | 0 | 3 | 8 | Key in tiles per row into Register $X$ |
| {{key:×}} | 0 | 0 | 0 | 24 | Multiply dimensions; stack drops to display total area ($X = 24$) |

With Register $X$ displaying $24$, the chef verifies that all 24 cookie spaces are accounted for before sliding the tray into the brick oven.

---

#### Problem 4.2: Rotated Array Commutative Proof ($8 \times 3 = 24$)
While inspecting the cooling racks, the baker grips the assembled $3 \times 8$ cookie mat from Problem 4.1 and rotates it by $90^\circ$ on the tabletop. Where there were previously 3 rows of 8 cookies, there are now 8 rows of 3 cookies ($8 \times 3$). Without adding or discarding a single tile, the physical area remains identical at 24 cookies—demonstrating the commutative property ($A \times B = B \times A$) through direct tactile manipulation.

To verify this transformation on your SC-6, key in `{{res:sc6_04_operations_skip_counting_seq_04:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_04:value}}`**. This sequence parks 8 into Register $Y$, multiplies by 3 on the ground floor, and leaves $(T: 0, Z: 0, Y: 0, X: 24)$ glowing on the transflective screen ($X = 24\text{ cookies}$), confirming that spatial orientation never alters the underlying mathematical product.

---

#### Problem 4.3: Bakehouse Seating Grid ($4 \times 6 = 24$)
As the morning café opens for brunch, the dining room supervisor arranges 4 rows of 6 Cobalt Blue counting tiles on the desk mat to model the café table seating grid. Calculating the total guest table capacity requires finding the area of this 4-by-6 matrix.

On the SC-6 keypad, enter `{{res:sc6_04_operations_skip_counting_seq_05:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_05:value}}`**. This sequence lifts the 4 rows into Register $Y$, multiplies by 6 tables per row, and displays $(T: 0, Z: 0, Y: 0, X: 24)$ tables across the dining room ($X = 24\text{ tables}$).

---

#### Problem 4.4: Orchard Tree Matrix ($7 \times 5 = 35$)
Across the valley at the heirloom apple orchard, the arborist plants 7 parallel rows with 5 Radiant Gold Honeycrisp apple trees per row. Laying out 7 vertical strips of 5 gold tiles side-by-side models the geometric orchard grid on the planning table.

Turning to your SC-6, key in `{{res:sc6_04_operations_skip_counting_seq_06:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_06:value}}`**. This sequence holds the 7 rows in Register $Y$, multiplies by 5 trees per row, and evaluates directly to $(T: 0, Z: 0, Y: 0, X: 35)$ trees across the orchard ($X = 35\text{ trees}$).

---

#### Problem 4.5: Orchard Heirloom Apple Gift Crate ($6 \times 9 = 54$)
To prepare for the harvest festival showcase, the master orchardist packs a wooden presentation crate with 6 rows of 9 prize-winning dessert apples. Modeling small with blocks, you can build a compact $2 \times 9 = 18$ tile sample boundary ($\le 24$ tiles) on the desk mat to see how 9-compartment rows stack.

On your SC-6, scale the calculation to the full presentation crate by keying in `{{res:sc6_04_operations_skip_counting_seq_07:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_07:value}}`**. This sequence loads 6 rows into Register $Y$ and multiplies by 9 apples, yielding $(T: 0, Z: 0, Y: 0, X: 54)$ apples packaged for delivery ($X = 54\text{ apples}$).

---

#### Problem 4.6: Bakehouse Pastry Cooling Grid ($8 \times 8 = 64$)
The bakehouse pastry station features an $8 \times 8$ checkerboard cooling grid of alternating marble squares for tartlets. Model small with blocks by constructing a $4 \times 4$ checkerboard quadrant using 16 alternating white and slate tiles ($\le 24$ tiles) on your desk mat, noting how equal rows and columns form a balanced geometric square.

Scale Big on StackCalc to compute the complete commercial grid: key in `{{res:sc6_04_operations_skip_counting_seq_08:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_08:value}}`**. This sequence lifts the base dimension into Register $Y$ and multiplies by height to drop the stack to $(T: 0, Z: 0, Y: 0, X: 64)$ cooling squares ($X = 64\text{ squares}$).

---

#### Problem 4.7: Orchard Seedling Flat ($12 \times 4 = 48$)
In the greenhouse nursery, an orchard seedling propagation flat contains 12 columns with 4 apple rootstock pots in each column. Model small with blocks by snapping together 3 columns of 4 tiles ($12$ tiles $\le 24$) to observe the repeating modular structure of the planting flat.

Scale Big on StackCalc by keying in `{{res:sc6_04_operations_skip_counting_seq_09:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_09:value}}`**. This sequence parks the 12 columns in Register $Y$ and combines them with 4 pots per column, leaving $(T: 0, Z: 0, Y: 0, X: 48)$ healthy seedlings on the nursery bench ($X = 48\text{ seedlings}$).

---

#### Problem 4.8: Muffin Tin Array ($9 \times 7 = 63$)
The commercial bakery rolls out a high-capacity sheet pan featuring 9 rows of 7 blueberry muffin wells. Model small with blocks by placing 3 rows of 7 counting tiles ($21$ tiles $\le 24$) on your workstation mat to visualize the column alignment.

Scale Big on StackCalc across the entire sheet pan: key in `{{res:sc6_04_operations_skip_counting_seq_10:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_10:value}}`**. This sequence lifts 9 rows into Register $Y$ and multiplies by 7 wells per row, evaluating to $(T: 0, Z: 0, Y: 0, X: 63)$ golden blueberry muffins fresh from the oven ($X = 63\text{ muffins}$).

---

### Expedition 2: The Mountain Rescue Rhythmic Ladder (Problems 4.9–4.16)
*Mission Briefing:* You are part of an alpine search-and-rescue team ascending steep mountain ridges. Each elevation waypoint requires rhythmic stepping, skip-counting ropes, and rapid doubling ladders to track your climbing party's altitude, emergency radio beacon intervals, and supply drops.

#### Problem 4.9: Threes Ladder Alpine Trail Checkpoints ($3 \dots 27$)
As an alpine search-and-rescue team ascends a steep mountain ridge, the lead mountaineer plants an emergency trail marker every 3 vertical meters of elevation gain. Rather than performing 9 separate additions, Superpower 1 (`{{key:REP}}`) seeds the constant step across all four registers to create an effortless skip-counting ladder.

Model small with blocks by snapping together 3 rungs of 3 counting tiles ($9$ tiles $\le 24$) on your desk mat. Chant the climbing cadence: 3, 6, 9 meters! With your SC-6 ready, enter `{{res:sc6_04_operations_skip_counting_seq_11:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_11:value}}`**. Keying `3 {{key:REP}}` locks 3 into every register ($T, Z, Y, X$); each subsequent press of `{{key:+}}` pulls constant 3 downward from Register $T$ to climb smoothly up the ridge.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| {{key:3}} {{key:REP}} | 3 | 3 | 3 | 3 | Load constant 3 into all 4 registers to seed the rhythmic ladder |
| {{key:+}} | 3 | 3 | 3 | 6 | 1st step: $3 + 3 = 6\text{ m}$; Register $T$ preserves constant 3 |
| {{key:+}} | 3 | 3 | 3 | 9 | 2nd step: $6 + 3 = 9\text{ m}$; constant 3 drops from $T$ |
| {{key:+}} | 3 | 3 | 3 | 12 | 3rd step: $9 + 3 = 12\text{ m}$; rhythmically advancing up the ridge |
| {{key:+}} | 3 | 3 | 3 | 15 | 4th step: $12 + 3 = 15\text{ m}$; halfway station reached |
| {{key:+}} | 3 | 3 | 3 | 18 | 5th step: $15 + 3 = 18\text{ m}$; constant 3 preserved continuously |
| {{key:+}} | 3 | 3 | 3 | 21 | 6th step: $18 + 3 = 21\text{ m}$ elevation waypoint |
| {{key:+}} | 3 | 3 | 3 | 24 | 7th step: $21 + 3 = 24\text{ m}$ elevation waypoint |
| {{key:+}} | 3 | 3 | 3 | 27 | 8th step: $24 + 3 = 27\text{ m}$; 9th multiple reached |

With Register $X$ holding $27\text{ meters}$, the team confirms they have secured the 9th checkpoint with zero re-entry.

---

#### Problem 4.10: Fours Ladder Granite Cliff Anchor Ropes ($4 \dots 36$)
To reach a stranded hiker on a sheer granite cliff, a rescue climber drives a solid steel safety piton every 4 vertical meters. Model small with blocks by building a vertical strip of 4 four-tile rungs ($16$ tiles $\le 24$) on your workstation mat, sliding your finger upward to count by fours: 4, 8, 12, 16 meters.

Scale Big on StackCalc to determine the total rope height secured after 9 safety anchors: key in `{{res:sc6_04_operations_skip_counting_seq_12:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_12:value}}`**. Pressing `4 {{key:REP}}` loads the 4-meter interval across the entire stack; 8 rhythmic taps of `{{key:+}}` advance the climbing ladder up to $(T: 4, Z: 4, Y: 4, X: 36)$ meters ($X = 36\text{ meters}$), securing the anchor line at the 9th piton.

---

#### Problem 4.11: Sixes Ladder Alpine Shelter Rations ($6 \dots 48$)
Emergency ration packs are stocked across 8 high-altitude mountain shelters, with each shelter receiving 6 freeze-dried ration packs ($6 \times 8$). Model small with blocks on your 2-wire Number Rack: slide 6 beads across Rail 1 and 6 beads across Rail 2 ($6 \times 2 = 12$ rations $\le 24$), feeling the steady rhythm of equal groups.

Scale Big on StackCalc across all 8 shelters: key in `{{res:sc6_04_operations_skip_counting_seq_13:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_13:value}}`**. Seeding the stack with `6 {{key:REP}}` holds the 6-pack ration constant in Register $T$; 7 steady taps of `{{key:+}}` climb the supply ladder to $(T: 6, Z: 6, Y: 6, X: 48)$ packs ($X = 48\text{ ration packs}$), completely provisioning all 8 stations without scratch paper.

---

#### Problem 4.12: Eights Ladder Glacier Traverse Carabiners ($8 \dots 64$)
To cross a hazardous glacial icefield, the rescue team rigs 8 consecutive safety guide-rope spans, with each span requiring 8 heavy-duty locking carabiners ($8 \times 8$). Model small with blocks by assembling 2 rows of 8 counting tiles ($16$ tiles $\le 24$) on your desk mat to visualize the 8-carabiner span increment.

Scale Big on StackCalc using Superpower 1: key in `{{res:sc6_04_operations_skip_counting_seq_14:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_14:value}}`**. Replicating 8 with `8 {{key:REP}}` locks the span requirement in Register $T$; 7 rhythmic taps of `{{key:+}}` march through the 8s table to $(T: 8, Z: 8, Y: 8, X: 64)$ carabiners ($X = 64\text{ carabiners}$), verifying the complete rigging manifest for the crossing.

---

#### Problem 4.13: Nines Ladder Peak Radio Beacons ($9 \dots 81$)
Emergency radio transceiver beacons are positioned across 9 surrounding mountain peaks, broadcasting 9 synchronized audio pulses during each transmission cycle ($9 \times 9 = 81$). Model small with blocks using two Ten-Frames: place 9 counters on Frame 1 and 9 counters on Frame 2 ($18$ counters $\le 24$), observing how $9 + 9 = 18$.

Scale Big on StackCalc to compute the total audio pulses transmitted per cycle: key in `{{res:sc6_04_operations_skip_counting_seq_15:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_15:value}}`**. Priming all four registers with `9 {{key:REP}}` allows 8 taps of `{{key:+}}` to reach $(T: 9, Z: 9, Y: 9, X: 81)$ pulses ($X = 81$), where the digital root property ($8 + 1 = 9$) confirms the product with instant certainty.

---

#### Problem 4.14: Twelves Ladder Alpine Supply Crates (Dozens to 144)
A supply helicopter delivers an alpine emergency crate packed with 12 cartons of chemical hand-warmers, each carton containing 12 individual warming packets (1 gross). Model small with blocks by taking a single 12-tile strip ($12$ tiles $\le 24$) from your Array Studio to ground the physical unit of one dozen.

Scale Big on StackCalc through all twelve cartons: key in `{{res:sc6_04_operations_skip_counting_seq_16:keys}}` to seed all four registers $(T: 12, Z: 12, Y: 12, X: 12)$, followed by 11 rhythmic taps of `{{key:+}}`. The stack advances through each dozen ($24, 36, 48 \dots 132$) until reaching **144 warming packets** ($X = 144$), accounting for the entire gross of emergency heaters.

---

#### Problem 4.15: Geometric Doubling: Alpine Search Grid Expansion ($1 \to 64$)
At nightfall in the mountains, a search-and-rescue coordinator initiates an expanding grid search. Beginning with an initial core sector of 1 square kilometer, the search perimeter doubles each hour as additional volunteer alpine teams arrive ($1 \to 2 \to 4 \to 8 \to 16 \to 32 \to 64\text{ km}^2$).

Modeling small with blocks, place 1 counting tile on your desk mat. Double it to 2 tiles, double the pair to 4, then 8, and 16 tiles (using only 16 tiles $\le 24$ tiles). Feel how geometric doubling grows explosively on the tabletop.

Scale Big on StackCalc: Now let your SC-6 doubling cadence (`{{key:ENTER}} {{key:+}}`) scale smoothly beyond physical block limits: key in `{{res:sc6_04_operations_skip_counting_seq_17:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_17:value}}`**.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| {{key:1}} {{key:ENTER}} | 0 | 0 | 1 | 1 | Enter starting search area of $1\text{ km}^2$; duplicate into $Y$ |
| {{key:+}} | 0 | 0 | 0 | 2 | Hour 1: $1 + 1 = 2\text{ km}^2$ searched |
| {{key:ENTER}} {{key:+}} | 0 | 0 | 0 | 4 | Hour 2: Duplicate 2 and sum: $2 + 2 = 4\text{ km}^2$ |
| {{key:ENTER}} {{key:+}} | 0 | 0 | 0 | 8 | Hour 3: Duplicate 4 and sum: $4 + 4 = 8\text{ km}^2$ |
| {{key:ENTER}} {{key:+}} | 0 | 0 | 0 | 16 | Hour 4: Duplicate 8 and sum: $8 + 8 = 16\text{ km}^2$ |
| {{key:ENTER}} {{key:+}} | 0 | 0 | 0 | 32 | Hour 5: Duplicate 16 and sum: $16 + 16 = 32\text{ km}^2$ |
| {{key:ENTER}} {{key:+}} | 0 | 0 | 0 | 64 | Hour 6: Duplicate 32 and sum: $32 + 32 = 64\text{ km}^2$ |

With Register $X$ displaying $64$, the coordinator verifies that $64\text{ km}^2$ ($2^6 = 64$) have been comprehensively searched by the 6th hour.

---

#### Problem 4.16: Doubling Triples: High-Angle Hauling Rig Load ($3 \to 96$)
The alpine rescue crew rigs a heavy-duty mechanical advantage pulley system to haul a rescue stretcher up a vertical cliff. The initial pilot rope holds a 3 kN test load. As successive double-pulley stages are coupled, the system's mechanical load rating doubles through 5 consecutive stages ($3 \to 6 \to 12 \to 24 \to 48 \to 96\text{ kN}$).

Modeling small with blocks, place 3 counting tiles on your desk mat. Snap 3 more to double to 6 tiles, then double to 12 and 24 tiles (staying strictly within the 24-tile studio bound).

Scale Big on StackCalc: Let your SC-6 continue the geometric doubling ladder (`{{key:ENTER}} {{key:+}}`) to scale from 24 through 48 up to $96\text{ kN}$ without needing 96 physical tiles on your workstation mat! Key in `{{res:sc6_04_operations_skip_counting_seq_18:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_18:value}}`**. Tapping `{{key:ENTER}} {{key:+}}` five consecutive times duplicates and combines each stage ($6 \to 12 \to 24 \to 48 \to 96$), leaving $(T: 48, Z: 48, Y: 96, X: 96)\text{ kN}$ on the LCD screen ($X = 96\text{ kN}$), confirming full rated hauling capacity.

---

### Expedition 3: The Farm Stand Harvest & Egg Packaging Depot (Problems 4.17–4.26)
*Mission Briefing:* You are directing logistics at a bustling farm co-op. Baskets of fresh eggs, crates of apples, and batches of bakery muffins arrive by the truckload. Using Superpower 2 (`{{key:÷R}}`), you must determine how many standard containers can be filled completely and sort leftover units without touching scratch paper or dealing with fractions.

#### Problem 4.17: Farm Egg Cartons (185 Eggs)
The farm hen house collects 185 fresh pasture-raised eggs this morning, and the packing crew must package them into standard 12-egg dozen cartons for the farm stand market. Superpower 2 (`{{key:÷R}}`) determines both the complete carton count and the remaining loose eggs simultaneously without generating awkward decimals.

Model small with blocks using two Ten-Frames: place 14 counters into your frames, partitioning into a single dozen carton of 12 (one full frame plus 2 counters), leaving exactly 2 loose counters ($14 \div 12 = 1\text{ R }2$). Feel how remainders separate cleanly from full cartons. Scale Big on StackCalc to process all 185 eggs in one stroke: key in `{{res:sc6_04_operations_skip_counting_seq_19:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_19:value}}`**.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `185` {{key:ENTER}} | 0 | 0 | 185 | 185 | Load 185 total harvested eggs into holding Register $Y$ |
| `12` | 0 | 0 | 185 | 12 | Enter carton capacity 12 into active Register $X$ |
| {{key:÷R}} | 0 | 0 | 5 | 15 | Integer divide: $X = 15$ full cartons, $Y = 5$ leftover eggs |
| {{key:x⇄y}} | 0 | 0 | 15 | 5 | Swap registers to inspect remainder in active display ($X = 5$) |

The LCD display cleanly splits the answer: Register $X$ shows $15$ full market cartons, and tapping `{{key:x⇄y}}` reveals the remainder of $5$ loose eggs set aside for the farm kitchen ($Q = 15\text{ cartons}$, $R = 5\text{ eggs}$).

---

#### Problem 4.18: Dinner Roll Bakery Bags (75 Rolls)
The farm stand bakery pulls 75 warm honey-wheat dinner rolls fresh from the brick oven, packing them into kraft bakery bags holding 8 rolls each. Model small with blocks by taking 19 counting tiles from your studio tray ($\le 24$ tiles). Bundling them into groups of 8 yields 2 complete bags ($16$ tiles) with 3 loose rolls left over ($19 \div 8 = 2\text{ R }3$).

Scale Big on StackCalc across all 75 rolls: key in `{{res:sc6_04_operations_skip_counting_seq_20:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_20:value}}`**. Integer division with remainder simultaneously loads quotient 9 into Register $X$ and leaves remainder 3 in Register $Y$ with inline trace $(T: 0, Z: 75, Y: 3, X: 9)$, separating 9 complete market bags from 3 warm rolls for the customer tasting basket ($Q = 9\text{ bags}$, $R = 3\text{ rolls}$).

---

#### Problem 4.19: Harvest Volunteer Camp Tents (29 Volunteers)
A crew of 29 harvest volunteers stays overnight at the farm camp, with each canvas orchard tent sleeping 4 workers. Model small with blocks by placing 17 counting tiles on your desk mat ($\le 24$ tiles). Partitioning into groups of 4 yields 4 complete tents ($16$ workers) plus 1 volunteer remaining ($17 \div 4 = 4\text{ R }1$).

Scale Big on StackCalc to shelter the full team: key in `{{res:sc6_04_operations_skip_counting_seq_21:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_21:value}}`**. The stack drops into $(T: 0, Z: 0, Y: 1, X: 7)$ tents; because remainder $Y=1$ person cannot sleep outside in the orchard, ceiling division dictates that the farm must erect $7 + 1 = 8$ total tents ($Q = 7\text{ full tents}$, $R = 1\text{ volunteer}$, total $= 8\text{ tents}$).

---

#### Problem 4.20: Apple Orchard Gift Baskets (140 Apples)
The farm orchard harvests 140 crisp Honeycrisp apples, and the farm stand crew packages them into decorative woven gift baskets containing 6 apples each. Model small with blocks by taking 20 counting tiles ($\le 24$ tiles) and grouping them into bundles of 6, creating 3 full baskets ($18$ tiles) with 2 leftover apples ($20 \div 6 = 3\text{ R }2$).

Scale Big on StackCalc to package the entire harvest: key in `{{res:sc6_04_operations_skip_counting_seq_22:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_22:value}}`**. Superpower 2 evaluates $140 \div 6$ in a single stroke, leaving $(T: 0, Z: 0, Y: 2, X: 23)$ on the display: 23 full gift baskets ready for shipment and 2 dessert apples left over ($Q = 23\text{ baskets}$, $R = 2\text{ apples}$).

---

#### Problem 4.21: Farm Floral Bouquet Twine Ties (250 cm Spool)
At the farm stand floral counter, a 250 cm spool of natural jute twine is cut into 35 cm ties for bundling freshly picked wildflower bouquets. Model small with blocks by taking 20 counting tiles from your Array Studio ($\le 24$ tiles) and grouping them into bundles of 7, making 2 complete bundles ($14$ tiles) with 6 loose tiles remaining ($20 \div 7 = 2\text{ R }6$).

Scale Big on StackCalc to divide the entire spool: key in `{{res:sc6_04_operations_skip_counting_seq_23:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_23:value}}`**. Tapping `{{key:÷R}}` yields $(T: 0, Z: 0, Y: 5, X: 7)$, confirming that the florist cuts 7 full bouquet ties with an exact $5\text{ cm}$ twine remnant remaining on the wooden spool ($Q = 7\text{ ties}$, $R = 5\text{ cm leftover}$).

---

#### Problem 4.22: Farm Kitchen Chocolate Truffles (115 Truffles)
The farm confectionery kitchen dips 115 dark chocolate maple truffles, packaging them into artisan gold boxes holding 9 truffles each. Model small with blocks by counting out 24 counting tiles ($\le 24$ tiles) and grouping them into $3 \times 3$ boxes of 9 tiles, making 2 complete boxes ($18$) with 6 loose truffles left over ($24 \div 9 = 2\text{ R }6$).

Scale Big on StackCalc to package all 115 artisan delicacies: key in `{{res:sc6_04_operations_skip_counting_seq_24:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_24:value}}`**. The display resolves instantly into $(T: 0, Z: 115, Y: 7, X: 12)$, proving that 12 complete boxes can be sealed for the boutique with 7 truffles saved for the customer tasting dish ($Q = 12\text{ boxes}$, $R = 7\text{ truffles}$).

---

#### Problem 4.23: Pumpkin Patch Hayride Wagons (46 Visitors)
A farm tour group of 46 pumpkin patch visitors arrives to pick autumn pumpkins. The farm operates 7-passenger tractor hayride wagons to transport guests across the fields. Model small with blocks using two Ten-Frames: place 18 counters into your frames and group into sets of 7, filling 2 complete wagons ($14$) with 4 visitors waiting for the next wagon ($18 \div 7 = 2\text{ R }4$).

Scale Big on StackCalc to transport the entire crowd: key in `{{res:sc6_04_operations_skip_counting_seq_25:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_25:value}}`**. Integer division drops the registers to $(T: 0, Z: 0, Y: 4, X: 6)$; since 4 pumpkin patch visitors cannot be left behind, the farm dispatches $6 + 1 = 7$ total hayride wagons ($Q = 6\text{ full wagons}$, $R = 4\text{ visitors}$, total $= 7\text{ wagons}$).

---

#### Problem 4.24: Farm Harvest Garden Carts (78 Wheels)
The farm equipment shed has 78 pneumatic replacement wheels to service 4-wheeled harvesting garden carts. Model small with blocks by taking 18 counting tiles from your tray ($\le 24$ tiles) and clustering them into groups of 4: you assemble 4 complete 4-wheel sets ($16$ tiles) with 2 spare wheels remaining ($18 \div 4 = 4\text{ R }2$).

Scale Big on StackCalc to inventory all 78 replacement wheels: key in `{{res:sc6_04_operations_skip_counting_seq_26:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_26:value}}`**. The operational stack drops into $(T: 0, Z: 78, Y: 2, X: 19)$, confirming that 19 complete garden carts can be fully refitted with 2 spare wheels remaining in the maintenance bin ($Q = 19\text{ carts}$, $R = 2\text{ spare wheels}$).

---

#### Problem 4.25: Greenhouse Soil Sensor Battery Packs (42 Batteries)
The farm greenhouse operates automated irrigation soil-moisture sensors powered by 4-battery packs. The maintenance manager has 42 fresh AA batteries. Model small with blocks by taking 14 counting tiles ($\le 24$ tiles) and partitioning into clusters of 4, building 3 complete 4-battery packs ($12$ tiles) with 2 spare batteries left over ($14 \div 4 = 3\text{ R }2$).

Scale Big on StackCalc to evaluate the entire stock of 42 batteries: key in `{{res:sc6_04_operations_skip_counting_seq_27:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_27:value}}`**. Integer division leaves $(T: 0, Z: 42, Y: 2, X: 10)$ on the screen: 10 automated soil sensor packs are powered for deployment, leaving 2 reserve batteries in the charging dock ($Q = 10\text{ packs}$, $R = 2\text{ batteries}$).

---

#### Problem 4.26: Farm Stand Beeswax Candle Gift Boxes (175 Candles)
The farm apiary dips 175 handcrafted beeswax taper candles, and the farm stand packages them into gift boxes of 8 candles each. Model small with blocks by counting out 20 counting tiles ($\le 24$ tiles) and grouping by 8, assembling 2 complete 8-candle boxes ($16$ tiles) with 4 loose candles remaining ($20 \div 8 = 2\text{ R }4$).

Scale Big on StackCalc to package all 175 tapers: key in `{{res:sc6_04_operations_skip_counting_seq_28:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_28:value}}`**. The operational stack cleanly separates $175 \div 8$ into $(T: 0, Z: 175, Y: 7, X: 21)$, delivering 21 boxed gift sets ready for sale and 7 display candles for the showroom counter ($Q = 21\text{ boxes}$, $R = 7\text{ candles}$).

---

### Expedition 4: The Master Auditor's Inspection (Problems 4.27–4.34)
*Mission Briefing:* You are the chief quality inspector reviewing financial statements, warehouse balances, and shipping manifests. An auditor never assumes an arithmetic calculation is correct—they prove it through rigorous inverse operations. Using Superpower 4 (`{{key:LASTX}}`), you will verify sums, differences, products, and quotients in reverse with zero re-entry.

#### Problem 4.27: Addition Check: Silver & Copper Bullion Invoices ($68 + 27 = 95$)
As chief auditor at the precious metals mint, you inspect a shipping ledger listing 68 silver bullion bars and 27 copper bullion bars for a total consignment of 95 bars ($68 + 27 = 95$). Rather than re-entering the entire manifest from scratch, Superpower 4 (`{{key:LASTX}}`) executes an immediate inverse subtraction check ($95 - 27$) with zero scratch paper.

Modeling small with blocks, lay out 8 counting tiles on your desk mat, and place 7 tiles beside them to form 15 tiles ($8 + 7 = 15$). Pulling the 7 tiles away leaves exactly 8 tiles. Scale Big on StackCalc to audit the entire 95-bar consignment: key in `{{res:sc6_04_operations_skip_counting_seq_29:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_29:value}}`**.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `68` {{key:ENTER}} | 0 | 0 | 68 | 68 | Load 68 silver bars into $X$ and duplicate into Register $Y$ |
| `27` {{key:+}} | 0 | 0 | 0 | 95 | Add 27 copper bars; sum 95 displays in active Register $X$ |
| {{key:LASTX}} | 0 | 0 | 95 | 27 | Superpower 4: Recall last number 27 into $X$; sum lifts to $Y$ |
| {{key:-}} | 0 | 0 | 0 | 68 | Inverse subtraction: $95 - 27 = 68$; original addend restored |

When Register $X$ returns to $68$, the auditor confirms with absolute mathematical certainty that the original silver bar allocation was intact.

---

#### Problem 4.28: Multiplication Check: Precision Aerospace Valves Manifest ($18 \times 6 = 108$)
The auditor reviews a precision machining shipment of 18 crates holding 6 titanium shut-off valves each, billed as 108 valves total ($18 \times 6 = 108$). Model small with blocks by building a small $3 \times 6$ array of 18 counting tiles ($\le 24$ tiles) and dividing the array back into 6 equal rows ($18 \div 6 = 3$).

Scale Big on StackCalc to audit the bill of lading with Superpower 4: key in `{{res:sc6_04_operations_skip_counting_seq_30:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_30:value}}`**. Keying `18 {{key:ENTER}} 6 {{key:×}}` evaluates $108$ in Register $X$. Tapping `{{key:LASTX}} {{key:÷}}` instantly recalls crate multiplier 6 into Register $X$, lifts total 108 into Register $Y$, and divides to return $(T: 0, Z: 0, Y: 0, X: 18)$ crates ($X = 18$), verifying the manifest without touching scratch paper.

---

#### Problem 4.29: Subtraction Check: Central Bank Gold Vault Reserves ($92 - 35 = 57$)
A central bank vault transfer log records that from an opening vault reserve of 92 gold bricks, 35 bricks were dispatched to a regional branch, leaving an audited closing balance of 57 bricks ($92 - 35 = 57$). Model small with blocks on your 20-bead Number Rack: slide 18 beads across Rail 1, slide 5 beads away to model dispatching supplies ($18 - 5 = 13$), and then slide the same 5 beads back to restore 18 beads ($\le 24$).

Scale Big on StackCalc to validate the vault ledger: key in `{{res:sc6_04_operations_skip_counting_seq_31:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_31:value}}`**. Deducting 35 from 92 leaves 57 in Register $X$; tapping `{{key:LASTX}} {{key:+}}` immediately recalls 35 and adds it back, restoring the opening reserve $(T: 0, Z: 0, Y: 0, X: 92)$ without re-entering a single digit ($X = 92\text{ bricks}$).

---

#### Problem 4.30: Division Check: Titanium Airframe Fasteners Cargo ($156 \div 12 = 13$)
A customs inspection officer audits a shipping container of 156 high-strength aerospace bolts distributed into sealed structural kits of 12 bolts each, calculating 13 full kits ($156 \div 12 = 13$). Model small with blocks using 24 counting tiles ($\le 24$ tiles): bundle into 2 kits of 12 tiles ($24 \div 12 = 2$) and recombine them ($2 \times 12 = 24$).

Scale Big on StackCalc to verify the full shipment: key in `{{res:sc6_04_operations_skip_counting_seq_32:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_32:value}}`**. After dividing 156 by 12 to find 13 kits, tapping `{{key:LASTX}} {{key:×}}` recalls divisor 12 into Register $X$ and multiplies in place, restoring $(T: 0, Z: 0, Y: 0, X: 156)$ fasteners ($X = 156$), proving that all 156 bolts are accounted for across the 13 kits.

---

#### Problem 4.31: Large Addition Check: Treasury Capital Reserve Consolidation ($348 + 185 = 533$)
During a municipal budget audit, an auditor reviews the merger of two civic development funds: $\$348\text{k}$ in municipal bonds and $\$185\text{k}$ in utility reserves, yielding a consolidated fund of $\$533\text{k}$ ($348 + 185 = 533$). Model small with blocks using your Place Value blocks: combine 3 ten-bars and 4 unit cubes with 1 ten-bar and 8 unit cubes (16 blocks total $\le 24$), regrouping ten cubes into a ten-bar ($52$), then remove 18 to return to 34.

Scale Big on StackCalc across the multi-digit treasury accounts: key in `{{res:sc6_04_operations_skip_counting_seq_33:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_33:value}}`**. Adding 348 and 185 produces 533; executing `{{key:LASTX}} {{key:-}}` recalls 185 and subtracts it in one motion, leaving $(T: 0, Z: 0, Y: 0, X: 348)$ verified on the screen ($X = 348$).

---

#### Problem 4.32: Multi-Digit Product Check: Solar Array Photovoltaic Lot ($24 \times 16 = 384$)
A green-energy auditor inspects a commercial solar farm installation featuring 24 photovoltaic panel rows with 16 monocrystalline cells per row, reported as 384 active cells ($24 \times 16 = 384$). Model small with blocks by building a $4 \times 4$ array using 16 counting tiles ($\le 24$ tiles), and divide by 4 to return to 4.

Scale Big on StackCalc to audit the solar array: key in `{{res:sc6_04_operations_skip_counting_seq_34:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_34:value}}`**. Multiplying $24 \times 16$ gives 384 cells; tapping `{{key:LASTX}} {{key:÷}}` divides product 384 by 16 in one keystroke, returning $(T: 0, Z: 0, Y: 0, X: 24)$ rows ($X = 24$) with zero manual division steps.

---

#### Problem 4.33: Large Subtraction Check: Industrial Fuel Storage Tank ($500 - 187 = 313$)
An environmental compliance auditor inspects an industrial fuel depot with a 500-liter storage reservoir. After dispensing 187 liters of diesel fuel to a municipal service fleet, the calibrated flow meter reads 313 liters remaining ($500 - 187 = 313$). Model small with blocks using Place Value blocks: start with 1 hundred-flat, remove 3 ten-bars and 7 unit cubes ($37$, using 11 blocks $\le 24$), leaving 63, then add the 37 blocks back to reconstruct the 100-flat.

Scale Big on StackCalc to validate meter calibration: key in `{{res:sc6_04_operations_skip_counting_seq_35:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_35:value}}`**. Dispensing leaves 313 liters in Register $X$; tapping `{{key:LASTX}} {{key:+}}` recalls 187 liters and adds it back, restoring full reservoir capacity $(T: 0, Z: 0, Y: 0, X: 500)$ ($X = 500\text{ liters}$).

---

#### Problem 4.34: Long Division Check: Architectural Stone Tile Quarry ($225 \div 15 = 15$)
A quarry auditor reviews an architectural stone supply order supplying 225 square meters of honed granite pavers packed into modular pallets of 15 square meters each, billed as 15 complete pallets ($225 \div 15 = 15$). Model small with blocks by assembling a $4 \times 4$ square array using 16 counting tiles ($\le 24$ tiles) to see how equal rows and columns form a geometric square.

Scale Big on StackCalc to confirm the quarrying delivery manifest: key in `{{res:sc6_04_operations_skip_counting_seq_36:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_36:value}}`**. Dividing 225 by 15 leaves 15 pallets in Register $X$; tapping `{{key:LASTX}} {{key:×}}` multiplies quotient by pallet size to restore $(T: 0, Z: 0, Y: 0, X: 225)$ square meters ($X = 225\text{ m}^2$), matching the delivery bill to the quarry plan.

---

### Expedition 5: The Junior Engineering Workshop (Problems 4.35–4.42)
*Mission Briefing:* You are an apprentice systems engineer designing robotics assemblies, purchasing supplies, and managing material budgets. Real engineering problems never come in neat single-step packages; they require combining multiple products, sums, and differences seamlessly on the operational stack without intermediate scratch notes.

#### Problem 4.35: Robotics Frame Motor Mounts & Bearing Blocks
An apprentice systems engineer designs a robot drive chassis on the workshop bench using 3 aluminum motor brackets at $\$4$ each and 2 linear bearing blocks at $\$5$ each. Calculating the total bill $((3 \times 4) + (2 \times 5))$ demonstrates how the RPN stack automatically preserves intermediate values in higher registers without requiring parentheses.

Model small with blocks by laying out 3 rows of 4 blue counting tiles for the $\$12$ bracket cost, and 2 rows of 5 gold counting tiles for the $\$10$ bearing cost (22 tiles total $\le 24$). Pushing the two arrays together visually combines the subtotals. Step over to your SC-6 and key in `{{res:sc6_04_operations_skip_counting_seq_37:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_37:value}}`**.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| {{key:3}} {{key:ENTER}} 4 | 0 | 0 | 3 | 4 | Place 3 brackets in $Y$, key in $\$4$ unit cost in $X$ |
| {{key:×}} | 0 | 0 | 0 | 12 | Evaluate motor bracket subtotal: $3 \times 4 = \$12$ |
| {{key:2}} {{key:ENTER}} 5 | 0 | 12 | 2 | 5 | Stack lifts $\$12$ to $Z$; load 2 bearing blocks at $\$5$ |
| {{key:×}} | 0 | 0 | 12 | 10 | Evaluate bearing subtotal: $2 \times 5 = \$10$; subtotal 1 in $Y$ |
| {{key:+}} | 0 | 0 | 0 | 22 | Combine both hardware subtotals: $\$12 + \$10 = \$22$ |

With Register $X$ reading $22$, the engineer confirms that total component cost is $\mathbf{\$22}$ with zero intermediate notes scribbled on paper.

---

#### Problem 4.36: Stepper Motor Drivers & Limit Switches
An automation workcell requires 5 high-torque stepper motor drivers at $\$12$ each and 4 optical limit switches at $\$8$ each. Model small with blocks by placing 2 groups of 5 tiles ($10$) and 2 groups of 4 tiles ($8$) on your mat ($18$ tiles total $\le 24$).

Scale Big on StackCalc to compute the total electronics order: key in `{{res:sc6_04_operations_skip_counting_seq_38:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_38:value}}`**. Multiplying $5 \times 12$ stores $\$60$ in Register $Y$ while $4 \times 8 = \$32$ evaluates in Register $X$; tapping `{{key:+}}` fuses both subtotals into $(T: 0, Z: 0, Y: 0, X: 92)$, evaluating the complete workcell bill to $\mathbf{\$92}$ ($X = 92$).

---

#### Problem 4.37: Custom Servo Bracket 3D Print Batch
Your engineering team 3D prints 45 custom servo brackets valued at $\$2$ each ($45 \times 2 = \$90$), incurring raw filament and brass threaded insert expenses of $\$28$. Model small with blocks using 18 Place Value units ($\le 24$ tiles): model $9$ units, remove $3$ units to simulate expenses, leaving $6$ units.

Scale Big on StackCalc to find the net project yield: key in `{{res:sc6_04_operations_skip_counting_seq_39:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_39:value}}`**. Evaluating gross production value $45 \times 2 = \$90$ and immediately deducting $\$28$ leaves $(T: 0, Z: 0, Y: 0, X: 62)$, confirming a net project yield of $\mathbf{\$62}$ ($X = 62$).

---

#### Problem 4.38: Test Bench Frame Extrusion & Gusset Packs
A structural test frame requires 40 meters of T-slot aluminum extrusion at $\$6$ per meter ($40 \times 6 = \$240$), plus 5 heavy-duty cast corner gusset packs at $\$14$ each ($5 \times 14 = \$70$). Model small with blocks using Place Value blocks: 4 ten-bars ($40$) and 1 ten-bar plus 4 units ($14$), staying strictly within 9 blocks ($\le 24$).

Scale Big on StackCalc to determine total framing investment: key in `{{res:sc6_04_operations_skip_counting_seq_40:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_40:value}}`**. Multiplying $40 \times 6 = \$240$ lifts to Register $Z$ when loading the gussets, and the final sum drops the stack into $(T: 0, Z: 0, Y: 0, X: 310)$ framing expense ($X = 310$).

---

#### Problem 4.39: Fastener Inventory Reconciliation
A hardware workshop inventory bin starts Monday with 850 socket-head cap screws. During chassis assembly, 145 screws are driven into frame joints, and 88 unused screws from a disassembled prototype are returned to stock. Model small with blocks using Place Value blocks: represent 85 with 8 ten-bars and 5 unit cubes ($13$ blocks $\le 24$).

Scale Big on StackCalc to reconcile fastener stock: key in `{{res:sc6_04_operations_skip_counting_seq_41:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_41:value}}`**. Deducting 145 leaves 705 screws, and adding the 88 reclaimed units leaves $(T: 0, Z: 0, Y: 0, X: 793)$ screws on the active display ($X = 793$).

---

#### Problem 4.40: Robotics Wiring Harness Assembly
A production run assembles wiring harnesses: 120 sensor ribbon cables at $\$3$ each, 85 heat-shrink sleeve bundles at $\$2$ each, and 40 flexible cable-drag chains at $\$4$ each. Model small with blocks by taking 16 counting tiles ($\le 24$ tiles) and grouping them into small representative bundles of 3 and 2.

Scale Big on StackCalc through all three material lines: key in `{{res:sc6_04_operations_skip_counting_seq_42:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_42:value}}`**. The stack evaluates ribbon cables ($120 \times 3 = \$360$), lifts to add sleeves ($85 \times 2 = \$170 \to \$530$), and adds drag chains ($40 \times 4 = \$160$) to finish at $(T: 0, Z: 0, Y: 0, X: 690)$ total material cost ($X = 690$).

---

#### Problem 4.41: Hex Standoff Packaging for Sensor Modules
Four automated workstations assemble 24 sensor modules each ($4 \times 24 = 96$ modules), and each module requires 2 threaded hex standoff posts ($96 \times 2 = 192$ standoffs). Standoffs are packaged in bags of 15. Model small with blocks by taking 16 counting tiles ($\le 24$ tiles) and partitioning into clusters of 5 ($16 \div 5 = 3\text{ R }1$).

Scale Big on StackCalc to determine total bags consumed: key in `{{res:sc6_04_operations_skip_counting_seq_43:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_43:value}}`**. Chaining $4 \times 24 \times 2$ produces 192 standoffs, and tapping `15 {{key:÷R}}` drops the stack into $(T: 0, Z: 0, Y: 12, X: 12)$: 12 full bags are emptied, with 12 additional standoffs required from a 13th bag ($Q = 12\text{ bags}$, $R = 12\text{ loose}$, total bags $= 13$).

---

#### Problem 4.42: Conveyor Pallet Roller Bearings
Three automated conveyor loops have 12 carrier pallets each ($3 \times 12 = 36$ pallets), with each pallet requiring 3 precision roller bearings ($36 \times 3 = 108$ bearings). Bearings are packaged in protective tubes of 8. Model small with blocks by grouping 18 counting tiles ($\le 24$ tiles) into sets of 8: you get 2 complete tubes ($16$) with 2 loose bearings ($18 \div 8 = 2\text{ R }2$).

Scale Big on StackCalc to determine the stockroom pull: key in `{{res:sc6_04_operations_skip_counting_seq_44:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_44:value}}`**. Chaining $3 \times 12 \times 3$ yields 108 bearings, and tapping `8 {{key:÷R}}` yields $(T: 0, Z: 0, Y: 4, X: 13)$: 13 complete tubes are emptied, and 4 bearings are taken from a 14th tube ($Q = 13\text{ tubes}$, $R = 4\text{ loose}$, pull 14 tubes).

---

### Expedition 6: Mental Math & Rapid Arithmetic Shortcuts (Problems 4.43–4.50)
*Mission Briefing:* You are stepping into the High-Speed Math Discovery Studio. In rapid problem-solving sprints, speed and poise are everything: solving challenging arithmetic sequences under timed conditions without scratch paper. Use these championship-grade shortcuts, factoring tricks, and modular checks to solve high-pressure challenges in seconds.

#### Problem 4.43: Rapid Mental Multiplication by 25 ($36 \times 25$)
In the High-Speed Math Discovery Studio sprint round, the coach challenges you to calculate $36 \times 25$ mentally in under two seconds. Because $25 = \frac{100}{4}$, multiplying by 25 is mathematically identical to dividing by 4 and scaling by 100 ($36 \div 4 = 9 \rightarrow 9 \times 100 = 900$). To anchor the factoring shortcut concretely, count out a small test set of 24 counting tiles and partition them into 4 equal quarters of 6 tiles each ($24 \div 4 = 6$). Treating each quarter as 25 gives $6 \times 25 = 150$, which matches $6 \times 100 \div 4 = 150$.

Scale Big on StackCalc to execute the tournament sprint: key in `{{res:sc6_04_operations_skip_counting_seq_45:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_45:value}}`**. The stack evaluates the division and hundred-fold multiplication cleanly: `36` {{key:ENTER}} `4` {{key:÷}} sets Register $X$ to 9, and `100` {{key:×}} instantly evaluates to $(T: 0, Z: 0, Y: 0, X: 900)$—conquering the calculation in two swift keystrokes.

---

#### Problem 4.44: Mental Multiplication by 99 ($45 \times 99$)
During the rapid sprint challenge, the scoreboard flashes $45 \times 99$ without scratch paper allowed. Instead of tedious long multiplication, apply the distributive shortcut: multiplying by 99 is identical to scaling by 100 and subtracting exactly one single group of 45 ($45 \times 100 - 45 = 4,500 - 45 = 4,455$). Build a tactile model on your desk using 10 unit cubes arranged in a single row to represent a strip of tens. Removing 1 unit cube leaves 9 units ($10 - 1 = 9$); scaling each unit by 45 confirms that subtracting one group from ten groups mirrors subtracting one group from one hundred groups.

Scale Big on StackCalc to confirm the distributive trick: key in `{{res:sc6_04_operations_skip_counting_seq_46:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_46:value}}`**. Keying `45` {{key:ENTER}} `100` {{key:×}} establishes the baseline product of 4,500, and typing `45` {{key:-}} immediately yields $(T: 0, Z: 0, Y: 0, X: 4455)$.

---

#### Problem 4.45: Consecutive Integers Sum Trick ($1 + 2 + \dots + 20$)
The sprint prompt demands the sum of all consecutive integers from 1 to 20 ($1 + 2 + 3 + \dots + 20$). Rather than adding twenty numbers sequentially, apply young Carl Friedrich Gauss's pairing formula: $S = \frac{n(n+1)}{2} = \frac{20 \times 21}{2} = 210$. Prove this geometrically on your desk by assembling a 4-rung stepped staircase using 10 counting tiles ($1 + 2 + 3 + 4 = 10$). Assemble an identical 10-tile twin staircase, rotate it $180^\circ$, and interlock them into a solid $4 \times 5$ rectangle of 20 tiles ($\le 24$ tiles). Halving the rectangular area gives $\frac{20}{2} = 10$ tiles.

Scale Big on StackCalc to compute the 20-integer sum: key in `{{res:sc6_04_operations_skip_counting_seq_47:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_47:value}}`**. Entering `20` {{key:ENTER}} `21` {{key:×}} builds the paired rectangle of 420 in Register $X$, and pressing `2` {{key:÷}} halves the area to $(T: 0, Z: 0, Y: 0, X: 210)$ without a single parenthesis.

---

#### Problem 4.46: Rapid Remainder Sprint ($3,458 \div 11$)
The discovery studio timer drops to 3 seconds: extract both the whole quotient and integer remainder of $3,458 \div 11$. While a standard calculator yields an unhelpful repeating decimal ($314.3636\dots$), your SC-6 evaluates both exact integer parts simultaneously. Model the division small with 20 counters placed on two Ten-Frames: dividing 20 by 11 yields 1 full bundle of 11 counters with 9 loose remnants left over ($20 = 1 \times 11 + 9$).

Scale Big on StackCalc for the four-digit sprint: key in `{{res:sc6_04_operations_skip_counting_seq_48:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_48:value}}`**. Pressing `3458` {{key:ENTER}} `11` `{{key:÷R}}` instantly deposits the quotient 314 into Register $X$ and the integer remainder 4 into Register $Y$ ($(T: 0, Z: 0, Y: 4, X: 314)$). Tapping `{{key:x⇄y}}` swaps the display to verify the 4 loose remainder items, confirming $3,458 = 314 \times 11 + 4$.

---

#### Problem 4.47: Chained Multi-Step Arithmetic Sprint ($15 \times 12 - 18 \times 6$)
The final team sprint round challenges you to evaluate $(15 \times 12) - (18 \times 6)$ without scratch notes or parentheses. Watch how the RPN 4-register stack acts as an automatic holding buffer: it evaluates the first product ($180$), lifts it automatically into Register $Z$ when the second factor pair is loaded, holds the first product safely in Register $Y$ while computing the second product ($108$), and subtracts them with a single stroke.

Model the subtraction small on your desk using counting tiles: build a $3 \times 4$ array (12 tiles) and a $2 \times 3$ array (6 tiles). Removing the 6 tiles from the 12 tiles leaves 6 tiles ($12 - 6 = 6$).

Scale Big on StackCalc to execute the dual-product tournament sequence: key in `{{res:sc6_04_operations_skip_counting_seq_49:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_49:value}}`**.

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `15` {{key:ENTER}} 12 | 0 | 0 | 15 | 12 | Enter first factor pair: 15 into $Y$, 12 into $X$ |
| {{key:×}} | 0 | 0 | 0 | 180 | Evaluate product 1: $15 \times 12 = 180$ in Register $X$ |
| `18` {{key:ENTER}} 6 | 0 | 180 | 18 | 6 | Stack lifts 180 to $Z$; enter 18 into $Y$, 6 into $X$ |
| {{key:×}} | 0 | 0 | 180 | 108 | Evaluate product 2: $18 \times 6 = 108$; product 1 in $Y$ |
| {{key:-}} | 0 | 0 | 0 | 72 | Subtract products: $180 - 108 = 72$ in active display |

The final display reads $X = \mathbf{72}$, demonstrating how Register $Z$ buffers intermediate sub-expressions seamlessly.

---

#### Problem 4.48: Rapid Mental Square of a Number Ending in 5 ($35^2$)
In the speed squaring sprint, compute $35^2$ in under 2 seconds. Apply the mental squaring shortcut for numbers ending in 5: multiply the tens digit 3 by its consecutive successor $(3+1)=4$ to obtain 12, then append 25 to immediately produce $1,225$! Model the geometric principle small using 16 counting tiles arranged as a $4 \times 4$ square. Decomposing the square into a $3 \times 3$ core (9 tiles), two $3 \times 1$ edge strips (6 tiles), and a $1 \times 1$ corner tile (1 tile) proves how tens and units interact symmetrically ($9 + 6 + 1 = 16$).

Scale Big on StackCalc to verify the speed square: key in `{{res:sc6_04_operations_skip_counting_seq_50:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_50:value}}`**. Keying `35` {{key:ENTER}} `35` {{key:×}} yields $(T: 0, Z: 0, Y: 0, X: 1225)$, verifying the mental calculation $35^2 = 1,225$.

---

#### Problem 4.49: Sum of First 10 Odd Integers ($1 + 3 + 5 + \dots + 19$)
In the studio pattern sprint, find the sum of the first 10 odd numbers ($1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19$). The ancient Pythagorean theorem reveals that the sum of the first $n$ odd integers is always a perfect square: $S_n = n^2 = 10^2 = 100$! Build this physically on your desk using counting tiles: start with 1 tile, wrap an L-shaped border of 3 tiles around it to form a $2 \times 2$ square (4 tiles), then wrap 5 tiles around that to form a $3 \times 3$ square (9 tiles), and finally 7 tiles to make a $4 \times 4$ square (16 tiles $\le 24$ tiles). Each odd layer expands the square by exactly one unit along each axis.

Scale Big on StackCalc for the 10-odd-integer sprint: key in `{{res:sc6_04_operations_skip_counting_seq_51:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_51:value}}`**. Keying `10` {{key:ENTER}} `10` {{key:×}} squares the count $n=10$, yielding $(T: 0, Z: 0, Y: 0, X: 100)$ and confirming the geometric square sum.

---

#### Problem 4.50: Chained Divisibility & Modulo Sprint ($4,896 \div 16$)
The final tournament sprint challenge tests rapid divisibility: is 4,896 evenly divisible by 16? Tap `{{key:÷R}}` on your SC-6: if the integer remainder in Register $Y$ equals 0, the number divides cleanly with zero remainder! Model divisibility small with 16 counting tiles: arranging all 16 tiles into a single bundle of 16 leaves exactly 0 loose remnants ($16 \div 16 = 1\text{ R }0$).

Scale Big on StackCalc to test the large dividend: key in `{{res:sc6_04_operations_skip_counting_seq_52:keys}}` $\rightarrow$ **`{{res:sc6_04_operations_skip_counting_seq_52:value}}`**. Keying `4896` {{key:ENTER}} `16` `{{key:÷R}}` immediately sets Register $X$ to 306 and Register $Y$ to 0 ($(T: 0, Z: 0, Y: 0, X: 306)$). The zero remainder proves that 4,896 is evenly divisible by 16 with a clean quotient of 306.

---

## What You Mastered & Looking Ahead

In this chapter, you transformed whole number operations into spatial, joyful superpowers! With the 24-Tile Four-Color Array Studio, you proved that multiplication is a physical rectangle of space. On your SC-6 Stack Calculator, you unlocked rhythmic skip-counting ladders with **Superpower 1 (`{{key:REP}}`)**, captured whole-number quotients and real remainders with **Superpower 2 (`{{key:÷R}}`)**, and commanded the self-checking magic mirror of **Superpower 4 (`{{key:LASTX}}`)** without ever needing scratch paper.

What happens when you have a remainder that cannot be left as a whole leftover—like slicing a single remaining pizza among four friends, or measuring a piece of lumber down to the exact fraction of an inch? In **[Chapter 05: Fractions, Decimals, Percents & Proportional Towers](05-fractions-decimals-ratios.md)**, you will dive into the 84 mm Fraction Studio, master single-key two-dot fraction entry, and discover how to reduce fractions step-by-step with **Superpower 3 (`{{key:SIMP}}`)**!
