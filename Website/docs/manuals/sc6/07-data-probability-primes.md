---
title: "Chapter 7: Discrete Probability, Primes & Pre-Algebra"
description: "Mastering elementary probability, number theory, descriptive statistics, and Grade 6 pre-algebra on the SC-6: dice, prime factors, GCF/LCM, and signed numbers."
---

# Chapter 7: Discrete Probability, Primes & Pre-Algebra

## The 17-Year Cicada Mystery: How Prime Numbers Outsmart Predators and Fair Dice Balance Chance

Deep beneath the deciduous forests of eastern North America, millions of periodical cicada nymphs (*Magicicada septendecim*) sip tree-root sap in the dark for **17 years**—until, on a single warm spring weekend, billions of them tunnel out of the soil at once and fill the forest canopy with a deafening chorus {{cite:gould1977}}. Across living ecosystems, spacecraft communications, and tabletop games, **prime numbers and probability govern how creatures outsmart predators, how secret codes stay unbreakable, and how dice roll with equal chance.**

### Why Cicadas Count in Primes

Naturalists and mathematical biologists long investigated a fascinating evolutionary question {{cite:gould1977,webb2001}}: **Why 13 years? Why 17 years?** Why didn't cicadas evolve a 12-year, 14-year, or 16-year life cycle?

To see the danger of a non-prime schedule, picture the **Deadly Composite Trap** that would happen if a cicada brood emerged on a 12-year cycle. The number 12 is **composite**, meaning its factors are $1, 2, 3, 4, 6,$ and $12$:
- A predatory bird or parasitic wasp with a 2-year population surge would synchronize with them on every single emergence ($2 \times 6 = 12$).
- A predator with a 3-year boom cycle would meet them every emergence ($3 \times 4 = 12$).
- A predator with a 4-year cycle would feast on them every emergence ($4 \times 3 = 12$).

The cicada population would be devastated by specialized parasites at every generation!

Now compare that trap with the **Prime Number Shield** of 17. The number 17 is **prime**, so its *only* factors are 1 and 17:
- A 2-year cyclical predator intersects with the cicadas only once every **34 years** ($\text{Least Common Multiple of } 2\text{ and } 17 = 34$).
- A 3-year cyclical predator intersects only once every **51 years** ($\text{Least Common Multiple of } 3\text{ and } 17 = 51$).
- A 5-year cyclical predator intersects only once every **85 years** ($\text{Least Common Multiple of } 5\text{ and } 17 = 85$).

By sleeping underground for an exact prime number of years, cicadas outsmart every predator in the forest! Primes are nature's secret code—the unbreakable atomic building blocks of all numbers {{cite:gauss1809,singh1997}}.

---

### The Polyhedral Dice Maker's Secret: Why There Are Only 5 Perfect Fair Dice

Ever wonder why your favorite tabletop roleplaying games use 4, 6, 8, 12, or 20-sided dice—but nobody sells a 7-sided or 11-sided die?

Over 2,300 years ago, Greek mathematicians proved a staggering geometric fact: in our three-dimensional universe, there are **only five regular convex polyhedra** (the Platonic Solids) where every single face is an identical regular polygon and every vertex meets the exact same number of edges:
1. **Tetrahedron (d4):** 4 equilateral triangular faces
2. **Cube (d6):** 6 square faces
3. **Octahedron (d8):** 8 equilateral triangular faces
4. **Dodecahedron (d12):** 12 regular pentagonal faces
5. **Icosahedron (d20):** 20 equilateral triangular faces

If you try to make a 7-sided or 11-sided die, some sides will always be steeper or flatter than others. It is physically impossible to make them land with equal chance! True fairness in gaming isn't just about giving the dice cup a good shake—it comes from the deep spatial symmetries of the universe {{cite:gardner1959,bruner1966}}.

---

## Hands-On Studio: Two-Color Counters, Polyhedral Dice & The Sieve Grid

Before we tap keys on the calculator, we roll real dice, balance counters, and build number arrays with our hands. When you understand what the numbers look like on your desk, the calculator's probability keys (`{{key:🎲}}`, `{{key:1…x}}`, `{{key:t…x}}`), number-theory engines (`{{key:PRIME}}`, `{{key:FACT}}`, `{{key:C.FAC}}`, `{{key:GCF}}`, `{{key:LCM}}`, `{{key:÷R}}`), statistical accumulators (`{{key:Σ+}}`, `{{key:Σ-}}`, `{{key:N}}`, `{{key:Σx}}`, `{{key:Σx²}}`, `{{key:x̄}}`, `{{key:MED}}`, `{{key:MODE}}`, `{{key:MIN}}`, `{{key:MAX}}`, `{{key:IQR}}`, `{{key:MAD}}`, `{{key:FRQ}}`), and pre-algebra keys (`{{key:+/-}}`, `{{key:|x|}}`, `{{key:x²}}`, `{{key:√x}}`) become your ultimate math assistants.

### Concrete Probability & Number Theory Manipulatives

1. **Precision Dice & Spinner Studio:**
   - **Equal-Volume Pip Design:** Carefully sized dots for true mechanical balance across all 4 physical $d6$ dice so every face has the exact same weight.
   - **Captive Multi-Plate Spinner:** 10-sector decimal lid (`0`–`9`), plus interchangeable biased ($50\%, 25\%, 15\%, 10\%$), binary (`0`/`1`), and arithmetic operations dial plates.
   - **Digital Polyhedral Extension (`{{key:🎲}}`):** The SC-6 hardware probability engine extends physical $d6$ experiments to full polyhedral dice ($d4, d6, d8, d10, d12, d20$).
2. **Counting & Array Studio:**
   - Four high-contrast color groups modeling positive/negative integer Zero Pairs and discrete frequency histograms.
3. **Prime Factor Studio:**
   - Proportional prime factor towers ($2, 3, 5, 7$) and bilateral comparator stage.

{{blocks:dice_spinner_probability|Probability Dice & Spinner Studio: 1x1 spinner enclosure with 10-sector lid, biased and binary dial plates, and 4 volume-equalized fair d6 dice}}

### The Equal-Volume Pip Dice & Spinner Studio
Standard store-bought dice often have a tiny physical imbalance because the 6-dot side has six scooped-out dots while the 1-dot side has only one!

The StackCalc kit eliminates this lopsided imbalance with our 3D-printable **Dice & Spinner Studio**. If all the dots were the same size, the 6-dot side would have 6 times as much plastic scooped out as the 1-dot side, making the 1-dot side heavier! By making the 6 dots smaller than the 1 dot, every side of the die loses the exact same tiny weight of plastic so every roll is completely fair. Meanwhile, pressing `{{key:🎲}}` on the SC-6 simulates fair $d4, d6, d8, d10, d12,$ and $d20$ polyhedral rolls.

### Two-Color Integer Counters & Zero Pairs
Before you manipulate signed numbers on the SC-6 keypad, you model integers concretely using two-color tokens:
- **Yellow Token:** Represents $+1$ (a unit gain, a deposit, an upward step).
- **Crimson Token:** Represents $-1$ (a unit loss, a withdrawal, a downward step).
- **The Zero Pair:** Placing 1 Yellow token and 1 Crimson token side-by-side forms a **Zero Pair** ($+1 + (-1) = 0$).

When solving $(-5) + (+3)$, you place 5 Crimson tokens and 3 Yellow tokens on the mat. Pairing 3 Crimson tokens with the 3 Yellow tokens eliminates 3 Zero Pairs, leaving 2 Crimson tokens: $-2$. On the SC-6, you model that exact zero-pair cancellation on the stack by entering `5`, toggling its sign to `-5` on Register $Y$, and adding `3` on Register $X$ with `{{res:sc6_07_data_probability_primes_seq_66:keys}}` to land directly on $X = \mathbf{-2}$.

That physical number-line walk also explains a puzzle that mystifies many students: *"Why is $(-3) \times (-2)$ equal to $+6$? Why aren't two negatives even more negative?"* Instead of memorizing a grammar rule ("two negatives make a positive"), picture yourself walking along your Number Line:

1. **Multiplication is walking along the number line at a steady pace:**
   - $(+3) \times (+2)$: Face Forward ($+$), take 2 steps of size 3 forward $\longrightarrow +6$.
   - $(-3) \times (+2)$: Face Backward ($-$), take 2 steps of size 3 forward $\longrightarrow -6$.
2. **Multiplying by a negative means WALKING IN REVERSE:**
   - $(+3) \times (-2)$: Face Forward ($+$), take 2 steps of size 3 in REVERSE $\longrightarrow -6$.
   - $(-3) \times (-2)$: Face Backward ($-$), take 2 steps of size 3 in REVERSE. When you face backward and walk in reverse, **you move forward toward positive numbers!** $(-3) \times (-2) = +6$.

On the SC-6, staging `-3` on Register $Y$ and multiplying by `-2` on Register $X$ with `{{res:sc6_07_data_probability_primes_seq_67:keys}}` produces $\mathbf{+6}$, letting you watch the sign toggle smoothly on the daylight LCD.

### The 100-Grid Sieve of Eratosthenes
To discover prime numbers, the Greek mathematician Eratosthenes of Cyrene (c. 276–194 BC) showed a clever shortcut for finding every prime number up to 100. Because $10 \times 10 = 100$, any composite number up to 100 must have at least one factor smaller than 10! That means crossing out $1$ and the multiples of just four small primes—**2, 3, 5, and 7**—automatically uncovers all **25 primes under 100**: $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97$.

You can test each survivor candidate right on the SC-6: keying `{{res:sc6_07_data_probability_primes_seq_68:keys}}` flashes `PRIME` on the status banner while preserving `97` on the ground shelf, whereas keying `{{res:sc6_07_data_probability_primes_seq_69:keys}}` flashes `COMPOSITE` while preserving `91` (since $91 = 7 \times 13$). Pairing your physical sieve with the keypad makes it visually obvious why $91$ breaks into a $7 \times 13$ rectangle while $97$ stands alone as a prime.

---

## Discrete Probability & Random Trials (`{{key:🎲}}`)

Every time you flip a coin, spin a game-board spinner, or roll a die, you are exploring **Probability**—the branch of mathematics that measures how likely something is to happen on a scale from $0$ (completely impossible) to $1$ (guaranteed to happen every time):
$$\text{Probability of an Event} = \frac{\text{Number of Winning Outcomes}}{\text{Total Number of Equally Likely Outcomes}}$$

| Probability | What It Means | Classroom Example |
| :--- | :--- | :--- |
| **$0.0$** | Impossible | Rolling a `7` on a standard 6-sided die ($d6$) |
| **$0.5$** | Equally Likely ($50/50$) | Flipping Heads or Tails on a fair coin |
| **$1.0$** | Certain | Rolling a whole number from `1` to `6` on a standard $d6$ |

### The Classroom Dice Key (`{{key:🎲}}`)
What if you want to run a 60-roll probability experiment right at your desk without chasing runaway dice across the classroom floor? Pressing the dedicated dice key `{{key:🎲}}` on your SC-6 keypad turns the screen into an instant digital dice cup:
1. **Interactive Die Roll:** Each press of `{{key:🎲}}` wakes up the calculator's random number generator, animating a 3-frame rolling tumble before landing on a fair whole number from $1$ to $6$.
2. **Visual Die Rendering:** The daylight graphic LCD draws a crisp $32 \times 32$ pixel die face right in the middle of the screen with classic dot patterns.
3. **Automatic Stack Lift:** Even better, the number you rolled ($1 \dots 6$) lands directly on Register $X$ and lifts your previous numbers up the stack ($X \to Y \to Z \to T$)—so you can roll two dice and tap `{{key:+}}` to add them, or tap `{{key:Σ+}}` to log 50 rolls in a row!

| Rolled Value | 32×32 LCD Pip Geometry | Visual Dot Pattern |
| :--- | :--- | :--- |
| `{{key:1}}` | Single center pip | Unit point symmetry |
| `{{key:2}}` | Top-left & bottom-right diagonal pips | Diagonal pair |
| `{{key:3}}` | Top-left, center, & bottom-right pips | Diagonal triad |
| `{{key:4}}` | Four corner pips | $2 \times 2$ square array |
| `{{key:5}}` | Four corner pips + center pip | Quincunx ($4 + 1$) |
| `{{key:6}}` | Two vertical columns of three pips | $2 \times 3$ rectangular array |

### Polyhedral Random Ranges: `{{key:1…x}}` and `{{key:t…x}}`
What if your game or science experiment needs a 20-sided dragon die ($d20$), a coin flip (`1` or `2`), or a random student number from `1` to `28`? Two shifted random-range keys let you build any custom spinner or die you can imagine:
- **`{{key:1…x}}` (Random 1 to X):** Picks a random whole number from 1 up to whatever number is sitting on Shelf X.
  - Roll a 20-sided die ($d20$): `20 {{key:1…x}}` $\longrightarrow$ picks a random whole number from 1 to 20.
  - Flip a fair coin ($1 = \text{Heads}, 2 = \text{Tails}$): `{{key:2}} {{key:1…x}}` $\longrightarrow$ picks 1 or 2 with equal chance.
  - Select a random lab partner from a class of 28: `28 {{key:1…x}}` $\longrightarrow$ picks a random student number from 1 to 28.
- **`{{key:t…x}}` (Random Y to X):** Picks a random whole number between the starting number on Shelf Y and the ending number on Shelf X.
  - Generate a random two-digit number from 10 to 99: `10 {{key:ENTER}} 99 {{key:t…x}}`.

Why doesn't a real die land on `4` *exact* once every 6 rolls? Because **Theoretical Probability** tells you what happens over thousands of rolls, while **Experimental Probability** records what actually happened in your real-life trial! Suppose you roll a standard six-sided die 60 times. On any single roll, the theoretical probability of rolling a 4 is $\frac{1}{6}$, so across 60 rolls a 4 should theoretically appear $60 \times \frac{1}{6} = 10\text{ times}$:

$$\text{Theoretical Probability of Rolling a 4} = \frac{1}{6} \approx 0.1667 \ (16.67\%)$$
$$\text{Expected Count} = 60 \times \frac{1}{6} = 10\text{ times}$$

Suppose that in your actual 60-roll experiment, you roll a 4 twelve times. Dividing your 12 wins by the 60 total rolls on the stack with `12 {{key:ENTER}} 60 {{key:÷}}` gives an experimental probability of $0.2000$ ($20.0\%$), and subtracting the theoretical $\frac{1}{6}$ share with `0.20 {{key:ENTER}} {{key:1}} {{key:ENTER}} {{key:6}} {{key:÷}} {{key:-}}` shows a $+0.0333$ ($+3.33\%$) experimental difference.

---

### Compound Probability: Rolling Two Dice (36 Outcomes)
Here is a classic board-game mystery: when you roll **two** six-sided dice and add them together, the possible totals run from $2$ all the way to $12$. Are all eleven sums equally likely? Not even close!

Imagine painting the first die **Red** and the second die **Blue**. Because each of the 6 faces on the Red die can pair up with any of the 6 faces on the Blue die, there are $6 \times 6 = \mathbf{36\text{ equally likely pairs}}$ of *(Red Die, Blue Die)*. Look at what happens when we list all 36 pairs by their sum:
- To roll a **$2$** ("snake eyes"), both dice *must* land on $1$: $(1,1)$. There is **only 1 way** out of 36!
- To roll a **$12$** ("boxcars"), both dice *must* land on $6$: $(6,6)$. Again, **only 1 way** out of 36!
- Now look at **$7$**: if the Red die lands on *anything at all*—$1, 2, 3, 4, 5,$ or $6$—there is an exact partner on the Blue die that makes $7$: $(1,6), (2,5), (3,4), (4,3), (5,2),$ and $(6,1)$. There are **6 different ways** to roll a $7$—making **$7$** the tallest bar in the center of the rooftop pyramid!

{{blocks:dice_spinner_d20_and_polyhedra|Probability Dice & Spinner Studio: Independent 2d6 Pairs (36-Outcome Sample Space) with 10-Sector Hub and Operations Dial}}

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
| 1 | `. 6 . 36 {{key:SIMP}}` | 0 | 0 | 0 | **1/6** | 6 ways out of 36 simplifies by their $\text{GCF} = 6$ to **$\frac{1}{6}$** |
| 2 | `{{key:FDISP}}` | 0 | 0 | 0 | **0.1667** | Toggle fraction/decimal view: $\frac{1}{6} \approx \mathbf{16.67\%}$ |

The probability of rolling a sum of $7$ is **$1/6 \approx 16.67\%$**—six times more likely than rolling a $2$ or a $12$.

### Probability Trees & Sampling Without Replacement
What happens when you pull a marble out of a bag and **keep it in your hand** instead of tossing it back in? Now the bag has *one fewer marble* inside, so the odds on your second draw change!

| First Draw Outcome ($8$ Marbles) | Second Draw Outcome ($7$ Remaining) | Combined Branch Probability |
| :--- | :--- | :---: |
| **Red 1st ($5/8$)** | Red 2nd ($4/7$) | $\frac{5}{8} \times \frac{4}{7} = \frac{20}{56}$ |
| **Red 1st ($5/8$)** | Blue 2nd ($3/7$) | $\frac{5}{8} \times \frac{3}{7} = \frac{15}{56}$ |
| **Blue 1st ($3/8$)** | Red 2nd ($5/7$) | $\frac{3}{8} \times \frac{5}{7} = \frac{15}{56}$ |
| **Blue 1st ($3/8$)** | **Blue 2nd ($2/7$)** | $\frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \mathbf{\frac{3}{28}}$ |

Suppose you reach into a cloth bag containing 5 Red and 3 Blue marbles ($8$ marbles in all) and draw two marbles without looking and without putting the first marble back. What is the chance of drawing two Blue marbles in a row? On your first reach, $3$ out of $8$ marbles are Blue ($\frac{3}{8}$). Once you hold that Blue marble in your hand, only $2$ Blue marbles remain among the $7$ marbles left in the bag ($\frac{2}{7}$)! Multiply the two step chances together:
$$\text{Chance of Both Blue} = \text{Chance of 1st Blue} \times \text{Chance of 2nd Blue} = \frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \frac{3}{28}$$

On the stack, compute the first draw probability $\frac{3}{8}$ on Register $Y$, compute the second draw probability $\frac{2}{7}$ on Register $X$, and multiply them with `{{key:3}} {{key:ENTER}} {{key:8}} {{key:÷}} {{key:2}} {{key:ENTER}} {{key:7}} {{key:÷}} {{key:×}}` to obtain $0.107143$. Tapping `{{key:FDISP}}` switches to exact fraction view ($\mathbf{3/28}$), showing that the probability of drawing two blue marbles in a row is $3/28 \approx \mathbf{10.71\%}$.

What if someone asks for the chance of drawing **at least one Red marble** in those two picks? Instead of adding up three different branches (Red-Red, Red-Blue, and Blue-Red), use the **Complement Shortcut**: notice that the *only* way to fail is to draw **Both Blue** ($\frac{3}{28}$)! Subtracting the chance of Both Blue from $1$ ($100\%$) gives the answer in one step:
$$\text{Chance of At Least One Red} = 1 - \text{Chance of Both Blue} = 1 - \frac{3}{28} = \frac{25}{28}$$

Place `1` ($100\%$) onto Register $Y$, divide `3` by `28` on Register $X$, and subtract with `{{key:1}} {{key:ENTER}} {{key:3}} {{key:ENTER}} 28 {{key:÷}} {{key:-}}` to reach $0.892857$—and one tap of `{{key:FDISP}}` reveals the exact fraction $\mathbf{25/28}$ ($\approx \mathbf{89.29\%}$).

---

## Number Theory: Primes, Factors & The Secret Partner Rule

Now let's return to the 17-year cicada mystery from the start of our chapter. Why are prime numbers like $2, 3, 5, 7, 11, 13,$ and $17$ so special? Just as every molecule in chemistry is built out of atoms, **every whole number greater than 1 is built by multiplying a unique team of prime numbers together**!

| Tool | Format | What You Build & See | How It Connects to Your SC-6 |
| :--- | :--- | :--- | :--- |
| **Hands-On Blocks** | Physical Manipulatives | • **24-Tile Array Test:** Primes form only $1 \times \text{Number}$ straight lines; composites form 2D matrices. • **Prime Factor Studio:** Proportional prime towers where stacking prime blocks physically multiplies their values. • Height(2) + Height(3) = Height(6) on the comparator stage. | Physical verification before keystrokes |
| **Visual Screen** | Graphic Sandboxes | • Screen Factor Tree View: exponents and prime dots ($2^3 \times 3^2 \times 5$). • Dual Frame Counter `{{key:▦}}`. • Interactive LCD Sieve: survivor primes highlighted on display. | Daylight LCD dot matrix |
| **Number Stack** | RPN Symbolic Engines | • `{{key:PRIME}}` test flashes `PRIME` or `COMPOSITE` on the graphic status line, preserving the number on $X$. • `{{key:FACT}}` displays prime factorization string. • `{{key:GCF}}` and `{{key:LCM}}` execute Euclidean and Duality engines. | Stack execution ($T, Z, Y, X$) |

### The Rectangular Array Primality Test
How can you tell with your bare hands whether a number is **prime** or **composite**? Grab a handful of **Counting Tiles** from your 24-Tile Studio and try to arrange them into a neat rectangle with at least 2 rows!

| Number Classification | Tile Count | Complete Rectangular Factor Arrays | Positive Divisors |
| :--- | :--- | :--- | :--- |
| **Composite (12 Tiles)** | 12 Tiles | $1 \times 12$, $2 \times 6$, and $3 \times 4$ complete rectangles | `1, 2, 3, 4, 6, 12` (6 factors) |
| **Prime (13 Tiles)** | 13 Tiles | Rows of 2, 3, or 4 always leave 1 leftover tile; only $1 \times 13$ forms a rectangle | `1, 13` (2 factors only) |

> **Why Prime Numbers Cannot Form Rectangles:** Take 12 counting tiles from your kit: you can arrange them into a neat $2 \times 6$ rectangle or a $3 \times 4$ rectangle with zero leftovers. Now add one more tile to make 13 and try building a rectangle 2, 3, or 4 tiles wide. Every attempt leaves an extra tile sticking out! The only rectangle 13 tiles can form is a single skinny $1 \times 13$ line. That is the geometric meaning of a prime number: it cannot be factored into two dimensions greater than 1.

Walking through $12$ and $13$ on the keypad shows how `{{key:PRIME}}` tests each number in place without disturbing the rest of the stack:

| Keystroke | Register T | Register Z | Register Y | Register X | Status / Screen |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `12` | 0 | 0 | 0 | 12 | Number entered |
| `{{key:PRIME}}` | 0 | 0 | 0 | 12 | Flashes `COMPOSITE` |
| `13` | 0 | 0 | 12 | 13 | Stack lifts; 13 entered |
| `{{key:PRIME}}` | 0 | 0 | 12 | 13 | Flashes `PRIME` |

---

### The Four-Color Sieve of Eratosthenes (24-Tile Kit & 144-Tile Classroom Pool)
With your individual 24-tile kit, you can build a $4 \times 6$ grid to hunt down all 9 primes up to 24—or pool 6 student kits across a classroom table ($6 \times 24 = 144$ tiles: 36 each of Archival White, Cobalt Blue, Radiant Gold, and Slate Gray) to build a giant $12 \times 12$ sieve and uncover all 34 primes up to 144!

- **Step 1:** Tile 1 (White) is set aside. 1 is a unit (neither prime nor composite).
- **Step 2: Prime 2 (Blue).** Replace every even multiple $\ge 4$ with Blue tiles ($4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, \dots$).
- **Step 3: Prime 3 (Gold).** Replace uncolored multiples of 3 with Gold tiles ($9, 15, 21, 27, 33, 39, 45, 51, 57, 63, \dots$).
- **Step 4: Primes 5 & 7 (White/Pattern).** In the 6-kit classroom pool, replace remaining multiples of 5 and 7 ($25, 35, 49, 55, 65, 77, 85, 91, 95, 115, 119, 121, 125, \dots$).
- **Step 5: Prime Survivors (Slate Gray).** In a single 24-tile kit, the 9 survivor tiles are **$2, 3, 5, 7, 11, 13, 17, 19, 23$**. Across a 6-kit classroom pool ($144$ tiles), all 34 primes $\le 144$ survive:  
  $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139$.

Watch out for "impostor primes" like $91$ and $119$—they look prime at first glance because they are odd and don't end in $5$, but both are secret multiples of $7$! When you test $91$ with `{{res:sc6_07_data_probability_primes_seq_70:keys}}`, the screen flashes `COMPOSITE` while leaving `91` on the display ($91 = 7 \times 13$), whereas testing $97$ with `{{res:sc6_07_data_probability_primes_seq_71:keys}}` flashes `PRIME` and keeps `97` on Register $X$. Likewise, testing $119$ with `{{res:sc6_07_data_probability_primes_seq_72:keys}}` flashes `COMPOSITE` ($119 = 7 \times 17$), while testing $137$ with `{{res:sc6_07_data_probability_primes_seq_73:keys}}` flashes `PRIME`. Whenever a number flashes `COMPOSITE`, simply tap `{{key:FACT}}` right afterward to unmask its hidden prime factors on the LCD!

---

### The Prime Tower Scale: Multiplying by Stacking Blocks
Normally, stacking two blocks *adds* their heights together. Could we design special blocks where stacking two blocks on top of each other **multiplies** their numbers instead?

That is the magic of your **Prime Factor Studio**! The back wall of the studio has a special ruler scale numbered from $1$ to $100$ where the marks get closer together as you climb higher (every time a number doubles—$2, 4, 8, 16, 32$—it steps up by the exact same $7.00\text{ mm}$ height!). Each prime block is 3D-printed to match that scale:
- **Prime 2 (Blue):** $7.00\text{ mm}$ ($1\text{U}$)
- **Prime 3 (Amber/Green):** $11.09\text{ mm}$
- **Prime 5 (Yellow):** $16.25\text{ mm}$
- **Prime 7 (Red):** $19.65\text{ mm}$

Because the ruler scale is spaced by multiplication steps, **adding block heights on the stage automatically multiplies their numbers**!

{{blocks:prime_studio_comparator_stage|Prime Factor Studio: Bilateral Comparator Stage & Prime Factor Blocks}}

Try stacking your Prime Blocks right on the comparator stage to watch height addition turn into multiplication:
1. **Multiplying $2 \times 3 = 6$:**
   Place Blue Block `{{key:2}}` on the desk. Stack Amber/Green Block `{{key:3}}` on top:
   $$\text{Height of 2-Block} + \text{Height of 3-Block} = 7.00\text{ mm} + 11.09\text{ mm} = \mathbf{18.09\text{ mm}}$$
   The top of the stack aligns **EXACTLY with the "6" tick mark on the comparator!**
2. **Multiplying $2 \times 5 = 10$:**
   Stack Blue Block `{{key:2}}` and Yellow Block `{{key:5}}`:
   $$\text{Height of 2-Block} + \text{Height of 5-Block} = 7.00\text{ mm} + 16.25\text{ mm} = \mathbf{23.25\text{ mm}}$$
   Lands precisely on the major line labeled **"10"**.
3. **Decomposing $60 = 2 \times 2 \times 3 \times 5$:**
   Stack two `{{key:2}}` blocks, one `{{key:3}}` block, and one `{{key:5}}` block so that stacking the blocks adds their heights ($7.00 + 7.00 + 11.09 + 16.25 = 41.34\text{ mm}$) to match multiplying their numbers ($2 \times 2 \times 3 \times 5 = 60$):
   $$7.00\text{ mm} + 7.00\text{ mm} + 11.09\text{ mm} + 16.25\text{ mm} = \mathbf{41.34\text{ mm}}$$
   Points squarely at the **"60"** line on the rear wall!
4. **Why Order Doesn't Change the Height:**
   Reorder the stack: put Yellow `{{key:5}}` on the bottom, then `{{key:3}}`, then both `{{key:2}}`s.
   The total height stays the exact same (**$41.34\text{ mm}$**, matching $5 \times 3 \times 2 \times 2 = 60$). Multiplication is commutative—no matter what order you stack the blocks, the tower height never changes.

{{blocks:prime_studio_commutativity|Prime Studio Commutativity Proof: 2x5 = 5x2 = 10 Exact Flush Alignment}}

Now compare your physical block tower to the screen! Keying `{{res:sc6_fact_60:keys}}` on the SC-6 decomposes `{{res:sc6_fact_60:value}}` directly into its prime factor tree (`2 × 2 × 3 × 5`), matching your four stacked blocks block-for-block:

{{res:sc6_fact_60:screenshot|SC-6 Prime Factorization Mode: 60 = 2 x 2 x 3 x 5}}

| Keystroke | Register T | Register Z | Register Y | Register X | Status / Screen |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `60` | 0 | 0 | 0 | 60 | Number entered |
| `{{key:FACT}}` | 0 | 0 | 0 | 60 | Displays `2² × 3 × 5` |

---

### The Primality Testing Engine (`{{key:PRIME}}`)
A prime number is a whole number greater than 1 whose only factors are 1 and itself. On the SC-6, pressing the primary key `{{key:PRIME}}` tests the number sitting on Register $X$ in a flash:
- Momentarily flashes `PRIME` or `COMPOSITE` on the graphic status line.
- Preserves Register $X$ intact so you can immediately continue calculations with your candidate number.
- If the number is $1$ or less (or has a decimal part), flashes `INVALID DATA` (or `NEITHER` for 0 and 1).

| Keystroke | Register T | Register Z | Register Y | Register X | Status / Screen |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `97` | 0 | 0 | 0 | 97 | Number entered |
| `{{key:PRIME}}` | 0 | 0 | 0 | 97 | Flashes `PRIME` |
| `119` | 0 | 0 | 97 | 119 | Stack lifts; 119 entered |
| `{{key:PRIME}}` | 0 | 0 | 97 | 119 | Flashes `COMPOSITE` |
| `2` | 0 | 97 | 119 | 2 | Stack lifts; 2 entered |
| `{{key:PRIME}}` | 0 | 97 | 119 | 2 | Flashes `PRIME` |

---

### Prime Factor Decomposition Engine (`{{key:FACT}}`)
Whenever `{{key:PRIME}}` tells you a number is `COMPOSITE`, you naturally want to know: *Which prime blocks multiply together to build it?* Pressing `{{key:FACT}}` (`{{key:g}}` + `{{key:PRIME}}`) breaks any whole number $\ge 2$ into its prime factor tree, showing exponents and multiplication dots:
- Enter $12$: `12` `{{key:FACT}}` $\longrightarrow$ Displays: **`2² × 3`**
- Enter $360$: `360` `{{key:FACT}}` $\longrightarrow$ Displays: **`2³ × 3² × 5`**
- Enter $2,639$: `2639` `{{key:FACT}}` $\longrightarrow$ Displays: **`7 × 13 × 29`**

| Keystroke | Register T | Register Z | Register Y | Register X | Status / Screen |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `360` | 0 | 0 | 0 | 360 | Number entered |
| `{{key:FACT}}` | 0 | 0 | 0 | 360 | Displays `2³ × 3² × 5` |

---

### Hardware `{{key:GCF}}` and `{{key:LCM}}` Keys & Tactile Block Intersections

In Chapter 05, you met the `{{key:GCF}}` and `{{key:LCM}}` keys as fast tools for simplifying fractions and finding Least Common Denominators. Now we can look under the hood with our **Prime Factor Blocks** to see *why* GCF and LCM are secret partners:
- **Primary Key `{{key:GCF}}`:** Finds the **Greatest Common Factor** of Shelf $Y$ and Shelf $X$ (e.g., `{{res:sc6_gcf_12_18:keys}}` $\longrightarrow$ `{{res:sc6_gcf_12_18:value}}`).
- Keying `12` `{{key:ENTER}}` stages the first number $12$ onto Floor $Y$ ($Y = 12$), and keying `18` `{{key:GCF}}` places $18$ on Floor $X$ ($X = 18$) and finds the Greatest Common Factor of $12$ and $18$, which is $6$ ($X = 6$).
- **Shifted Key `{{key:LCM}}`:** Finds the **Least Common Multiple** of Shelf $Y$ and Shelf $X$ (e.g., `{{res:sc6_lcm_12_18:keys}}` $\longrightarrow$ `{{res:sc6_lcm_12_18:value}}`).
- **Why Songbird Brains Pack More Neurons per Gram:** Why can a tiny songbird learn hundreds of complex melodies? Because songbird brains pack $140\text{ million}$ neurons into a single gram of tissue. Tapping `140 {{key:FACT}}` breaks $140$ into its prime building blocks: **`2² × 5 × 7`**.

You can see how GCF and LCM share their prime blocks by drawing a **Two-Circle Prime Factor Venn Diagram** on your desk for the numbers **$48$** and **$72$**:
- Break down $48 = 2 \times 2 \times 2 \times 2 \times 3$: Assemble four `{{key:2}}` blocks and one `{{key:3}}` block.
- Break down $72 = 2 \times 2 \times 2 \times 3 \times 3$: Assemble three `{{key:2}}` blocks and two `{{key:3}}` blocks.
- **Center Overlap ($\text{GCF}$):** Slide every matching pair of prime blocks that both numbers share (**three `{{key:2}}`s and one `{{key:3}}`**) into the **Center Overlap**. Multiplying the center blocks gives the Greatest Common Factor:
  $$\text{GCF} = 2 \times 2 \times 2 \times 3 = 8 \times 3 = \mathbf{24}$$
- **All Three Regions Combined ($\text{LCM}$):** Place the leftover unshared blocks in the outer crescents (one extra `{{key:2}}` on the Left for $48$; one extra `{{key:3}}` on the Right for $72$). Multiplying **all blocks across all three regions** (Left $\times$ Center $\times$ Right) gives the Least Common Multiple:
  $$\text{LCM} = 2 \times 24 \times 3 = 16 \times 9 = \mathbf{144}$$

{{blocks:prime_lcm_gcd_venn|Prime Factor Studio: Prime Factorization and Venn Intersection Model}}

Why do mechanical engineers care about both GCF and LCM when two gears mesh together? Imagine a **$14\text{-tooth}$ driver gear** ($14 = 2 \times 7$) clicking tooth-for-tooth against a **$21\text{-tooth}$ driven gear** ($21 = 3 \times 7$), with two chalk-marked teeth touching at the start:
- **GCF is the Largest Equal Tooth Group:** Keying `14 {{key:ENTER}} 21 {{key:GCF}}` gives **`7`**—meaning you can paint both gears in equal color-coded groups of **$7$ teeth** ($2$ groups on the small gear, $3$ groups on the big gear).
- **LCM is When the Marked Teeth Meet Again:** Keying `14 {{key:ENTER}} 21 {{key:LCM}}` gives **`42`**—meaning exactly **$42$ teeth** must click past the mesh point ($42 \div 14 = 3$ spins of the small gear and $42 \div 21 = 2$ spins of the big gear) before the two chalk-marked teeth touch again!

Once you see how `{{key:GCF}}` finds the largest shared building block and `{{key:LCM}}` finds the first shared meeting point, three everyday puzzles snap into focus:
- **Rectangle Tiling (`{{key:GCF}}`):** Suppose a maker lab needs to tile a tabletop measuring $24\text{ cm} \times 36\text{ cm}$ using the largest possible square tiles with zero waste or cutting. Keying `24 {{key:ENTER}} 36 {{key:GCF}}` $\to 12$ immediately reveals that the largest square tile side is the $\text{GCF of } 24\text{ and } 36 = \mathbf{12\text{ cm}}$.
- **Synchronized Flashing Cycles (`{{key:LCM}}`):** Suppose two signal lights flash at steady intervals—Light A every $6\text{ seconds}$ and Light B every $8\text{ seconds}$. Keying `6 {{key:ENTER}} 8 {{key:LCM}}` $\to 24$ confirms that the signal lights flash together every $\text{LCM of } 6\text{ and } 8 = \mathbf{24\text{ seconds}}$.
- **Fraction Least Common Denominator (`{{key:LCM}}`):** When adding unlike fractions $\frac{3}{8} + \frac{5}{12}$, the Least Common Denominator is simply the LCM of the denominators. Keying `8 {{key:ENTER}} 12 {{key:LCM}}` $\to 24$ gives the exact common denominator $\text{LCM of } 8\text{ and } 12 = \mathbf{24}$ in a single keystroke.

---

### The Secret Partner Rule: Why GCF × LCM Always Equals First Number × Second Number
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
| `{{key:ENTER}}` | 0 | 0 | 24 | 24 |
| `36` | 0 | 0 | 24 | 36 |
| `{{key:LCM}}` | 0 | 0 | 0 | 72 |
| `12` | 0 | 0 | 72 | 12 |
| `{{key:×}}` | 0 | 0 | 0 | 864 |

Check against direct multiplication on the stack by keying `{{res:sc6_07_data_probability_primes_seq_74:keys}}` to reach $X = \mathbf{864.00}$, confirming the Secret Partner Rule!

---

### The Remainder-Step Ladder (Euclidean Division) via Hardware `{{key:÷R}}`
How does the SC-6 find the Greatest Common Factor of two huge numbers without testing hundreds of prime factors? Over 2,300 years ago, Euclid of Alexandria discovered a brilliant visual shortcut—and you can see *why* it works by **tiling a rectangular hallway with the largest possible square floor tiles**:

Imagine a rectangular hallway that is **$105\text{ cm}$ long** and **$45\text{ cm}$ wide**. We want to find the largest square tile that tiles the whole hallway evenly:
1. First, lay down big **$45\text{ cm} \times 45\text{ cm}$ squares** along the $105\text{ cm}$ hallway. Two of those $45\text{ cm}$ squares fit side by side ($2 \times 45 = 90\text{ cm}$), leaving an unfilled rectangular gap at the end that measures **$45\text{ cm}$ by $15\text{ cm}$** (because $105 \div 45 = 2$ with a **remainder of $15$**)!
2. Any square tile that tiles the whole hallway *must also* tile that leftover **$45\text{ cm} \times 15\text{ cm}$** gap!
3. Now tile the $45\text{ cm} \times 15\text{ cm}$ gap with **$15\text{ cm} \times 15\text{ cm}$ squares**: exactly three $15\text{ cm}$ squares fit with **remainder $0$** ($45 \div 15 = 3$, remainder $0$)! Because $15\text{ cm}$ squares tile the gap with zero leftover space, they also tile the $45\text{ cm}$ squares—and the entire $105\text{ cm} \times 45\text{ cm}$ hallway!

$$\text{GCF of Big and Small} = \text{GCF of Small and Remainder}$$

On the SC-6, you can climb this remainder ladder using the shifted key `{{key:÷R}}`. Each press of `{{key:÷R}}` divides $Y$ by $X$, placing the whole-number quotient in Register $X$ and the remainder in Register $Y$—while automatically saving the divisor you just used inside `{{key:LASTX}}`.

Let's run our $105\text{ cm} \times 45\text{ cm}$ hallway tiling puzzle on the stack using `{{key:÷R}}`:
1. $105 \div 45 = 2$ with remainder $15$, so the **GCF of 105 and 45** is the same as the **GCF of 45 and 15**.
2. $45 \div 15 = 3$ with remainder $0$, which means $15\text{ cm}$ square tiles fit evenly with zero waste!
The last non-zero remainder is **15**, so the **GCF of 105 and 45** is $\mathbf{15}$.

| Keystroke | Register T | Register Z | Register Y | Register X | Status / Commentary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `105` | 0 | 0 | 0 | 105 | Dividend entered |
| `{{key:ENTER}}` | 0 | 0 | 105 | 105 | Stack lifts; 105 staged to $Y$ |
| `45` | 0 | 0 | 105 | 45 | Divisor 45 entered on floor $X$ |
| `{{key:÷R}}` | 0 | 0 | 15 | 2 | Integer quotient $Q = 2$ in $X$, remainder $R = 15$ in $Y$ (`LASTX` saves 45) |
| `{{key:x⇄y}}` | 0 | 0 | 2 | 15 | Swap: remainder 15 now in $X$ |

For even larger hallways or courtyards—like a $252\text{ cm}$ by $105\text{ cm}$ stone courtyard—you can keep stepping from the old width to the new remainder using `{{key:LASTX}}` and `{{key:÷R}}` until the remainder hits zero, without ever re-typing a divisor. What is the largest square paver that tiles a $252\text{ cm} \times 105\text{ cm}$ courtyard with zero cutting?
1. Two $105 \times 105$ squares fit inside $252$, leaving a remainder strip of $42$ ($252 \div 105 = 2$, remainder $42$).
2. Two $42 \times 42$ squares fit inside $105$, leaving a remainder strip of $21$ ($105 \div 42 = 2$, remainder $21$).
3. Two $21 \times 21$ squares fit inside $42$ with **zero remainder** ($42 \div 21 = 2$, remainder $0$)!
The last non-zero remainder is **21**, so the **GCF of 252 and 105** is $\mathbf{21}$.

| Step / Key | Dividend (Y) | Divisor (X) | Quotient (X) | Remainder (Y) |
| :--- | :--- | :--- | :--- | :--- |
| 252 `{{key:ENTER}}` 105 | 252 | 105 | - | - |
| `{{key:÷R}}` | - | - | 2 | 42 |
| `{{key:x⇄y}}` | 2 | 42 | 42 | 2 |
| `{{key:LASTX}}` `{{key:x⇄y}}` | 105 | 42 | - | - |
| `{{key:÷R}}` | - | - | 2 | 21 |
| `{{key:x⇄y}}` `{{key:LASTX}}` `{{key:x⇄y}}` | 42 | 21 | - | - |
| `{{key:÷R}}` | - | - | 2 | 0 |

> **The `{{key:LASTX}}` Conveyor Belt in Remainder Ladders & Secret Partner Checks:** Why didn't we have to type `105` or `42` a second time in the table above? Because every time you press `{{key:÷R}}`, `{{key:GCF}}`, or `{{key:LCM}}`, the SC-6 automatically tucks the divisor from Register $X$ into `{{key:LASTX}}`. In a remainder ladder, the previous step's divisor becomes the next step's starting number—so tapping `{{key:x⇄y}} {{key:LASTX}} {{key:x⇄y}} {{key:÷R}}` pulls the old divisor straight out of `LASTX` and divides it by the new remainder. And when you test the Secret Partner Rule on two numbers like 24 and 36, computing `24 {{key:ENTER}} 36 {{key:GCF}}` leaves `36` waiting in `LASTX`, so you only need `24 {{key:LASTX}} {{key:LCM}} {{key:×}}` to finish the proof!

You can also confirm that three-step remainder ladder in a single stroke using the dedicated hardware key `{{res:sc6_07_data_probability_primes_seq_75:keys}}` to land directly on $X = \mathbf{21.00}$.

---

## Elementary Descriptive Statistics & Data Analysis

What happens when a scientist, sports coach, or game designer collects a whole notebook full of numbers? Looking at a jumble of 20 or 30 raw numbers can make your head spin! **Statistics** gives you two superpowers for taming any list of numbers:
1. **Finding the Center (`{{key:x̄}}`, `{{key:MED}}`, `{{key:MODE}}`):** What single "typical" number best represents the whole group?
2. **Measuring the Spread (`{{key:RNG}}`, `{{key:IQR}}`, `{{key:MAD}}`):** Are all the numbers huddled tightly together, or are they scattered all over the map?

### Four Physical Stories Behind Your Statistical Keys
Before touching a single statistical key, picture what each measure looks like in the real world:
- **The Mean (`{{key:x̄}}`) Is Fair-Share Tower Leveling:** Suppose four eastern bluebird nestlings weigh $24\text{ g}, 26\text{ g}, 25\text{ g},$ and $29\text{ g}$. If you build four **Counting Tile** towers of heights $4, 6, 5,$ and $9$ above a $20\text{-gram}$ baseline and move tiles from the tallest tower ($9$) to the shorter towers until **every tower stands at the exact same height**, all four towers level out at **$6$ tiles** ($26\text{ g}$). Tapping `{{key:CLΣ}} 24 {{key:Σ+}} 26 {{key:Σ+}} 25 {{key:Σ+}} 29 {{key:Σ+}} {{key:x̄}}` performs that exact fair-share leveling on the stack ($\text{Mean} = \mathbf{26\text{ g}}$).
- **The Median (`{{key:MED}}`) Is the Middle Kid in the Height Lineup:** Imagine lining up your friends from shortest to tallest for a class photo. The **Median** (`{{key:MED}}`) is simply the person standing right in the **exact middle** of the line! Even if a 7-foot basketball player joins the tall end of the line, the middle person's height barely budges—which is why data detectives love the median when one extreme number would pull the mean off balance.
- **The Interquartile Range (`{{key:IQR}}`) Fences the Middle Half of the Class:** If you split that shortest-to-tallest lineup into four equal quarters, the middle two quarters ($25\%$ mark to $75\%$ mark) contain the **middle half of the class**. The distance between the lower quarter mark (`{{key:1Q}}`) and the upper quarter mark (`{{key:3Q}}`) is the **Interquartile Range (`{{key:IQR}}`)**—a sturdy fence around the core group that ignores extreme stragglers at both ends!
- **Mean Absolute Deviation (`{{key:MAD}}`) Measures How Far Trials Wander from the Average:** Why do scientists need `{{key:MAD}}` when they already have the mean (`{{key:x̄}}`)? In a behavioral lab, **Raven A** solves 4 puzzle boxes in **`8, 9, 9, 10` seconds**, while **Crow B** solves them in **`6, 8, 10, 12` seconds**. Both birds have the *exact same mean* ($9.0\text{ s}$). But when you measure how far each trial wanders from $9$, Raven A's distances are $1, 0, 0, 1$ (`{{key:MAD}}` $= \mathbf{0.5\text{ s}}$, super steady!), whereas Crow B's distances are $3, 1, 1, 3$ (`{{key:MAD}}` $= \mathbf{2.0\text{ s}}$, four times more spread out).

| Data Measure | Key / Shift | Kid-Friendly Word Rule |
| :--- | :--- | :--- |
| **Total Count (`N`)** | `{{key:N}}` | How many numbers are in your data list |
| **Total Sum (`Σx`)** | `{{key:Σx}}` | All the numbers added together |
| **Mean (Average)** | `{{key:x̄}}` | $\text{Total Sum} \div \text{How Many Numbers}$ |
| **Median** | `{{key:MED}}` | Middle number when lined up from smallest to largest |
| **Mode** | `{{key:MODE}}` | Number that shows up the most times |
| **Range** | `{{key:RNG}}` | $\text{Biggest Number} - \text{Smallest Number}$ |
| **Interquartile Range (IQR)** | `{{key:IQR}}` | $\text{Third Quartile (3Q)} - \text{First Quartile (1Q)}$ |
| **Mean Absolute Deviation (MAD)** | `{{key:MAD}}` | $\text{Mean Absolute Deviation (MAD)} = \text{Total Distance from the Mean} \div \text{How Many Numbers}$ |

### The 10-Quiz Score Frequency Table & The Seed of Distributions

Let's see how fast `{{key:Σ+}}` analyzes a whole classroom dataset. Suppose a 5th-grade math class records scores on a 100-point weekly quiz across 10 students:
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

Let's audit all ten scores on the SC-6! Toss all 10 scores into your `{{key:Σ+}}` statistical basket (and remember that if you ever mistype a score, tapping `{{key:Σ-}}` immediately removes it from the basket, while `{{key:FRQ}}` checks how many times a given score appears and `{{key:Σx²}}` tracks the sum of squared scores), then tap any statistical key to inspect the class results:
- `{{key:CLΣ}}` $\to$ Clears all stats registers ($\text{Count} = 0$)
- `70 {{key:Σ+}}` $\to \text{Count} = 1$
- `75 {{key:Σ+}}` $\to \text{Count} = 2$
- `80 {{key:Σ+}} 80 {{key:Σ+}}` $\to \text{Count} = 4$
- `85 {{key:Σ+}} 85 {{key:Σ+}} 85 {{key:Σ+}}` $\to \text{Count} = 7$
- `90 {{key:Σ+}} 90 {{key:Σ+}}` $\to \text{Count} = 9$
- `95 {{key:Σ+}}` $\to \text{Count} = 10$

1. **Total Count:** `{{key:N}}` $\longrightarrow X = \mathbf{10}$.
2. **Sum of Scores:** `{{key:Σx}}` $\longrightarrow X = \mathbf{835.0}$.
3. **Mean Score (Average):** `{{key:x̄}}` $\longrightarrow X = \mathbf{83.5}$.
4. **Median Score (Middle):** `{{key:MED}}` $\longrightarrow X = \mathbf{85.0}$.
5. **Mode Score (Most Common):** `{{key:MODE}}` $\longrightarrow X = \mathbf{85.0}$.
6. **Range ($\text{Biggest} - \text{Smallest}$):** `{{key:RNG}}` $\longrightarrow X = \mathbf{25.0}$ ($95 - 70 = 25$).

Because the scores are balanced around 85, the **Median** and **Mode** are identical ($85.0$), while the **Mean** ($83.5$) sits just slightly below the peak because the single score of $70$ pulls the fair-share average down by $1.5$ points.

---

### Measuring Spread in a Five-Quiz Study Group: IQR & MAD

Now let's zoom in on a 5-student study group with scores of $85, 90, 75, 90, 100$ so you can see how `{{key:IQR}}` and `{{key:MAD}}` measure spread:

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

Once you load all five scores into the statistical basket with `{{key:CLΣ}} 85 {{key:Σ+}} 90 {{key:Σ+}} 75 {{key:Σ+}} 90 {{key:Σ+}} 100 {{key:Σ+}}`, you can inspect every center and spread measure with a single tap:
- `{{key:Σx}}` $\to 440.00$
- `{{key:x̄}}` $\to 88.00$
- `{{key:MED}}` $\to 90.00$
- `{{key:MODE}}` $\to 90.00$
- `{{key:IQR}}` $\to 5.00$
- `{{key:MAD}}` $\to 6.40$

### The Five-Number Summary, Box Plots & Outlier Analysis
When data detectives draw a **Box-and-Whisker Plot**, they line up all the numbers from smallest to largest and mark five milestones that slice the list into four equal quarters ($25\%$ in each quarter):
1. **Minimum (`MIN`):** Smallest number at the left whisker tip (`{{key:MIN}}`).
2. **First Quartile (`1Q`):** Left edge of the center box ($25\%$ mark, `{{key:1Q}}`).
3. **Median (`MED`):** Center line inside the box ($50\%$ mark, `{{key:MED}}`).
4. **Third Quartile (`3Q`):** Right edge of the center box ($75\%$ mark, `{{key:3Q}}`).
5. **Maximum (`MAX`):** Biggest number at the right whisker tip (`{{key:MAX}}`).

| Box Plot Milestone | Statistical Keycap | What It Shows on the Box Plot |
| :--- | :--- | :--- |
| **Lower Whisker Tip (`MIN`)** | `{{key:MIN}}` | Smallest number ($0\%$ mark) |
| **Left Box Edge — First Quartile (`1Q`)** | `{{key:1Q}}` | Lower quarter mark ($25\%$ boundary of the center box) |
| **Center Line — Median (`MED`)** | `{{key:MED}}` | Halfway mark ($50\%$ median line inside the box) |
| **Right Box Edge — Third Quartile (`3Q`)** | `{{key:3Q}}` | Upper quarter mark ($75\%$ boundary of the center box) |
| **Center Box Width (`IQR`)** | `{{key:IQR}}` | $\text{Third Quartile (3Q)} - \text{First Quartile (1Q)}$ |
| **Upper Whisker Tip (`MAX`)** | `{{key:MAX}}` | Biggest number ($100\%$ mark) |

How do scientists decide whether an unusual number is just a little high or a true **outlier** that wandered far away from the pack? They use the **$1.5 \times \text{IQR}$ Outlier Detection Rule**: measure the width of the center box (`{{key:IQR}}`), multiply it by $1.5$, and build an invisible "fence" $1.5$ box-widths below the First Quartile and above the Third Quartile:
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

Now build the upper outlier fence on the stack: multiplying the $7.5\text{-minute}$ box width by $1.5$ via `{{res:sc6_07_data_probability_primes_seq_76:keys}}` yields a fence margin of $11.25\text{ minutes}$, and adding that margin to the Third Quartile with `36.5 {{key:+}}` places the upper fence at $\mathbf{47.75\text{ minutes}}$. Since $58$ is greater than $47.75$, the time of 58 minutes sits well past the upper fence and is a **true outlier**.

---

## Grade 6 Pre-Algebra: Signed Numbers, Absolute Value & Inverses

In pre-algebra, you cross an exciting threshold: numbers no longer stop at zero! Every number now has both a **size** and a **direction**—stepping right (or up) into **positive numbers ($+$)**, or stepping left (or down) into **negative numbers ($-$)**.

| Negative Direction (Left of $0$) | Origin ($0$) | Positive Direction (Right of $0$) |
| :---: | :---: | :---: |
| `-5, -4, -3, -2, -1` | **`0`** | `+1, +2, +3, +4, +5` |

### Hot-Air Balloons, Sandbags & Two-Color Zero Pairs
To make adding and subtracting negative numbers crystal clear, picture a **hot-air balloon** floating at altitude $0$ (sea level) alongside your **Two-Color Counters**:
- **Yellow Counters ($+1$) Are Hot-Air Puffs:** Adding a Yellow counter puffs warm air into the balloon, lifting it **up $+1\text{ meter}$**.
- **Crimson Counters ($-1$) Are Heavy Sandbags:** Adding a Crimson counter hooks a sandbag onto the basket, pulling the balloon **down $-1\text{ meter}$**.
- **Zero Pairs ($+1 + (-1) = 0$):** One $+1$ puff of hot air and one $-1$ sandbag balance each other out completely, keeping the balloon at the exact same height!
- **Why Subtracting a Negative Moves You UP ($7 - (-3) = 10$):** What happens if your balloon is floating at $+7\text{ meters}$ and you **subtract (throw overboard) $3$ heavy sandbags** ($-(-3)$)? With $3$ fewer sandbags pulling it down, the balloon shoots **up $+3\text{ meters}$** to $+10$! Taking away a negative weight has the exact same effect as adding a positive boost!

### Signed Number Entry via the Negation Key `{{key:+/-}}`
On the SC-6 keypad, notice the difference between two keys that use a minus sign:
- The **subtraction key** (`{{key:-}}`) is an operation between two shelves: it subtracts Register $X$ from Register $Y$ ($Y - X$).
- The **change-sign key** (`{{key:+/-}}`) flips the sign of the single number currently sitting in Register $X$ (turning positive `8` into negative `-8`, or `-8` back into `+8`).

To enter $-8$ on your SC-6:
- Type `{{key:8}} {{key:+/-}}`. The screen immediately displays `-8`.
- Pressing `{{key:+/-}}` a second time flips `-8` right back to `8`.

Imagine checking the outdoor thermometer in Chicago on a frosty winter morning: at 6:00 AM, it reads $-14^\circ\text{C}$ ($14$ degrees below zero). By 2:00 PM, the winter sun warms the air up by $+9^\circ\text{C}$. What is the afternoon temperature?

$$\text{Temperature Change: } -14 + 9 = -5^\circ\text{C}$$

Think of 14 Crimson cold tokens meeting 9 Yellow warm tokens: 9 Zero Pairs cancel out, leaving 5 Crimson tokens ($-5^\circ\text{C}$). On the stack, key `14 {{key:+/-}} {{key:ENTER}} 9 {{key:+}}` $\to -5$, confirming an afternoon temperature of $-5^\circ\text{C}$ directly on the LCD.

---

### Absolute Value as Number Line Distance (`{{key:|x|}}`)
Suppose your friend walks $5\text{ steps}$ east ($+5$) and you walk $5\text{ steps}$ west ($-5$). Who walked farther from the starting line? You both walked the exact same distance: **$5\text{ steps}$**!

The **absolute value** of a number, written $|x|$, is simply its **distance from zero** on the number line—and whether you walk left or right, distance is always positive:
$$\text{Absolute Value } (|x|) = \text{Distance from } 0 \text{ on the Number Line (Always Positive!)}$$

On the SC-6, pressing the shifted absolute-value key `{{key:|x|}}` (`{{key:g}}` + `{{key:+/-}}`) removes any negative sign from Register $X$, leaving its positive distance from zero:
- `42 {{key:+/-}} {{key:|x|}}` $\longrightarrow X = \mathbf{42}$.
- `15 {{key:|x|}}` $\longrightarrow X = \mathbf{15}$.

To see why absolute value shines when crossing sea level, picture a desert hiker starting at the bottom of Badwater Basin in Death Valley at an elevation of $-86\text{ meters}$ ($86\text{ m}$ below sea level) and climbing all the way to the summit of Telescope Peak at $+3,366\text{ meters}$ above sea level. First the hiker climbs $86\text{ meters}$ just to reach sea level ($0\text{ m}$), and then climbs another $3,366\text{ meters}$ to the peak!

$$\text{Vertical Climb: } |3366 - (-86)| = |3366 + 86| = 3,452\text{ meters}$$

When you subtract the negative starting elevation from the summit height and take the absolute value via `3366 {{key:ENTER}} 86 {{key:+/-}} {{key:-}} {{key:|x|}}`, the display confirms a total vertical climb of $\mathbf{3,452.00\text{ meters}}$.

- **Northern Gannet Plunge Across Sea Level & Road-Salt Freezing Science:** A diving Northern Gannet plummets from $+32\text{ m}$ in the sky to $-14\text{ m}$ underwater to catch a herring; its total plunge distance across $0\text{ m}$ sea level is $|32| + |-14| = \mathbf{46\text{ m}}$ (`32 {{key:|x|}} {{key:ENTER}} 14 {{key:+/-}} {{key:|x|}} {{key:+}}`). In winter chemistry, spreading rock salt lowers water's freezing point from $0^\circ\text{C}$ by $-14.5^\circ\text{C}$, while adding sugar-beet juice lowers it another $-6.75^\circ\text{C}$: keying `0 {{key:ENTER}} 14.5 {{key:-}} 6.75 {{key:-}}` shows that snowplows keep roads ice-free down to **$-21.25^\circ\text{C}$**.

---

### Word Rules, Mystery Number Backwards Puzzles & Token Probability
Your counting tiles and Dice & Spinner Studio connect everyday word rules directly to the RPN stack:
- **Kea Parrot Puzzle Locks:** In a sanctuary puzzle challenge, an alpine kea parrot earns $10\text{ points}$ for each wire latch it unfastens and $3\text{ points}$ for each door it slides open:
  $$\text{Total Points} = (10 \times \text{Wire Latches}) + (3 \times \text{Doors})$$
  For $7$ wire latches and $4$ doors, the 4-register stack finds both parts and adds them with zero parentheses: `10 {{key:ENTER}} 7 {{key:×}} 3 {{key:ENTER}} 4 {{key:×}} {{key:+}}` $\longrightarrow \mathbf{82\text{ points}}$.
- **Mystery Number Backwards Puzzles & Inverse Operations:** Start with a Mystery Number, multiply by 3, and subtract 5 to get 16—work backwards on your stack `16 {{key:ENTER}} 5 {{key:+}} 3 {{key:÷}}` to uncover `7`! Adding $+5$ first undoes the $-5$ (`16 {{key:ENTER}} 5 {{key:+}}` $\to 21$), and dividing by $3$ (`3 {{key:÷}}`) undoes multiplying by 3 to reveal the Mystery Number **$\mathbf{7}$**.
- **Kea Token Jars:** When a kea parrot peers into a clear jar holding $9$ black tokens (worth a peanut) and $3$ orange tokens (worth nothing), its theoretical chance of drawing a black token is `{{key:.}} 9 {{key:.}} 12 {{key:SIMP}}` $\longrightarrow \mathbf{3/4} = 75\%$—which you can test experimentally on your SC-6 by pressing `{{key:🎲}}` across 20 trials.

---

### Geometric Inverses: Area-to-Side-Length (`{{key:x²}}` and `{{key:√x}}`)
In elementary school, the square key `{{key:x²}}` and square root key `{{key:√x}}` are taught as **square area-to-side-length opposites**:
- Squaring a number finds the **area** of a square from its side length: $\text{Square Area} = \text{Side} \times \text{Side}$.
- Taking the square root finds the **side length** of a square from its area: $\text{Side} = \sqrt{\text{Square Area}}$.

| Square Geometry | Forward Operation (`{{key:x²}}`) | Inverse Operation (`{{key:√x}}`) |
| :--- | :--- | :--- |
| **5 cm × 5 cm Tile Square** | $\text{Side} = 5\text{ cm} \to \text{Square Area} = 5 \times 5 = \mathbf{25\text{ cm}^2}$ | $\text{Square Area} = 25\text{ cm}^2 \to \text{Side} = \sqrt{25} = \mathbf{5\text{ cm}}$ |

Suppose a horse pasture has an exact square area of $1,225\text{ square meters}$. How long is one side of the pasture, and how much fencing is needed to surround all four sides? Taking the square root of the area with `1225 {{key:√x}}` immediately reveals a side length of $35.00\text{ meters}$ ($\text{Side} = \sqrt{\text{Square Area}}$), and multiplying that live result by four equal sides via `{{key:4}} {{key:×}}` gives a total perimeter of $\mathbf{140.00\text{ meters}}$ of fence.

### Directed Integers in Motion: Elevators, Submersibles & Ledgers
To master pre-algebra, you can follow multi-step signed integers in motion across skyscrapers, deep-sea trenches, and student bank accounts!

First, imagine a high-rise tower with 3 subterranean parking levels (Floors $-3, -2, -1$), a ground lobby (Floor $0$), and 60 tower floors (Floors $1 \dots 60$). An elevator starts at subterranean parking Level $-3$, travels up $+45$ floors to deliver office supplies, descends $-12$ floors to the cafeteria, and finally descends $-33$ floors:

$$\text{Elevator Journey: } -3 + 45 - 12 - 33 = -3\text{ (Back at parking Level -3!)}$$

Keying `3 {{key:+/-}} {{key:ENTER}} 45 {{key:+}} 12 {{key:-}} 33 {{key:-}}` $\to -3$ returns the elevator precisely to subterranean parking Level $-3$ with zero register overflow.

Next, let's head out to sea! A marine biology autonomous submersible begins a mission on the deck of a research ship at $+4\text{ meters}$ above sea level and dives to a survey trench at $-350\text{ meters}$. After measuring the total vertical descent distance, the vehicle ascends $+125\text{ meters}$ to sample a hydrothermal vent before descending an additional $-45\text{ meters}$. Subtracting the trench elevation from the ship-deck height via `{{key:4}} {{key:ENTER}} 350 {{key:+/-}} {{key:-}}` reveals a total vertical descent of $354.00\text{ meters}$ ($4 - (-350) = +354\text{ m}$) while automatically tucking $-350$ into `{{key:LASTX}}`. To find the vehicle's final depth from that trench floor without typing `350 {{key:+/-}}` a second time, simply recall it with `{{key:LASTX}} 125 {{key:+}} 45 {{key:-}}` to land at **$-270.00\text{ meters}$**.

Signed numbers also govern your personal finances! Suppose your student checking account starts with a positive balance of $+\$120.00$, and you track four transactions using the SC-6 currency formatter `{{key:$}}`:
- You buy school books for $\$85.00$ ($-\$85.00$).
- You buy an art supply kit for $\$60.00$ ($-\$60.00$).
- The bank assesses an overdraft penalty of $\$25.00$ ($-\$25.00$).
- You deposit a lawn-mowing paycheck of $\$95.00$ ($+\$95.00$).

Keying `{{res:sc6_07_data_probability_primes_seq_77:keys}}` deducts the $\$85.00$ book purchase to leave $35.00$, subtracting `60 {{key:-}}` drops the ledger into overdraft at $-25.00$, subtracting the `25 {{key:-}}` fee reaches $-50.00$, adding the `95 {{key:+}}` paycheck restores a positive balance of $45.00$, and pressing `{{key:$}}` formats the closing balance as **$\$45.00$**.

---

### Common Questions: Why 1 Is Not Prime & Subtracting Negatives

- **Why Is the Number 1 Not a Prime Number?** A prime number has *exactly two distinct positive factors* (1 and itself), while a composite number has three or more factors. The number $1$ has only *one* factor (just $1$), so it is neither prime nor composite—mathematicians call $1$ a **unit**. Test it on your SC-6 with `{{res:sc6_07_data_probability_primes_seq_79:keys}}` and the screen alerts `INVALID DATA`. Now test `2` (`{{res:sc6_07_data_probability_primes_seq_80:keys}}`): it flashes `PRIME` and keeps `2` on the display—the smallest prime number and the only even prime.
- **Why Does Subtracting a Negative Make a Number Bigger ($7 - (-3) = 10$)?** Imagine running a school store where a friend owes you $\$3$ (a debt of $-3$), or a hot-air balloon at $+7\text{ m}$ tossing $3$ sandbags ($-3$) overboard. If you cancel—or *subtract*—that $-3$ debt, your friend is $\$3$ richer and the balloon rises $+3\text{ m}$ higher! Taking away a negative is the exact same as adding a positive. Try it on your SC-6: `{{res:sc6_07_data_probability_primes_seq_81:keys}}` gives **`10`**.

If you ever see an unexpected result while exploring primes, statistics, or signed numbers, check this quick reference table:

| What Happened on Your Screen | Why It Happened | How to Fix It |
| :--- | :--- | :--- |
| **Claiming 1 is prime** | Conflating "divisible only by 1" with "having exactly two distinct factors." | *"A prime must have exactly two distinct factors: 1 and itself. 1 only has one factor. The SC-6 classifies 1 as a unit, neither prime nor composite."* |
| **Confusing GCF and LCM** | Assuming "Greatest" must yield a larger number than "Least." | *"A factor divides INTO a number, so it must be smaller than or equal to the number. A multiple MULTIPLIES the number, so it grows larger. GCF $\le$ numbers $\le$ LCM."* |
| **Treating $\lvert x\rvert$ as 'change the sign'** | Believing absolute value turns positive numbers into negative numbers. | *"Absolute value is distance on a number line. Distance is never negative. The distance from 5 to 0 is 5; the distance from -5 to 0 is also 5. $\lvert 5\rvert = 5$ and $\lvert -5\rvert = 5$."* |
| **Adding negatives: $-4 + (-3) = -1$** | Subtracting magnitudes instead of accumulating directed negative quantities. | *"If you take 4 steps backward ($-4$), and then take 3 more steps backward ($-3$), you are 7 steps backward ($-7$), not 1 step. Use Crimson tokens to model the sum."* |
| **Expecting Mean = Median always** | Assuming all datasets are perfectly symmetrical. | *"In skewed datasets (like home prices or quiz scores with an outlier), extreme values pull the mean away from the center. The median stays fixed in the middle."* |
| **Confusing `{{key:+/-}}` with `{{key:-}}`** | Using the binary subtraction operator to enter negative values. | *"The `{{key:-}}` key subtracts two numbers ($Y - X$). The `{{key:+/-}}` key changes the sign of the single number you are actively typing."* |

---

### Black-Box Statistics vs. Prime Towers, Fair-Share Blocks & Dice Trials

Now that you have explored probability trials, prime factor towers, statistical accumulators, and signed numbers, look at how the SC-6's dedicated number-theory and statistical keys compare against manual trial division and parenthesized averaging on an algebraic calculator:

| Challenge / Real-World Task | The Algebraic Calculator Trap (Infix) | Algebraic Keystrokes & Clutter | The StackCalc + Blocks Method (RPN Stack + Visual Studio) | StackCalc Keystrokes | The Stack Advantage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GCF & LCM Secret Partner Rule:** Checking that $\text{GCF} \times \text{LCM} = 24 \times 36 = 864$ | No hardware GCF or LCM keys: students must sketch manual factor trees on scratch paper, find prime powers, and re-enter multi-step arithmetic from scratch. Intermediate products vanish. | `2 4 * 3 6 =` Manual scratch work factor trees (28+ keystrokes, zero live factors) | **Hardware `{{key:GCF}}` & `{{key:LCM}}` Stack Duality:** Single-tap prime engines extract GCF (12) and LCM (72). Because `{{key:GCF}}` saves 36 in `LASTX`, tapping `24 {{key:LASTX}} {{key:LCM}} {{key:×}}` proves $12 \times 72 = 864$ without re-typing 36. | `24 {{key:ENTER}} 36 {{key:GCF}} 24 {{key:LASTX}} {{key:LCM}} {{key:×}}` (11 keystrokes) | **60% fewer keystrokes** Zero scratch paper; `{{key:LASTX}}` and the stack prove the Secret Partner Rule live on screen. |
| **Euclidean Division:** Hydraulic gate synchronization: $105 \div 45 \implies \text{Quotient} = 2, \text{Remainder} = 15$ | Infix division yields decimal $2.3333333$. Finding integer quotient and remainder requires rounding down, re-multiplying $2 \times 45 = 90$, and subtracting $105 - 90 = 15$ across multiple steps. | `1 0 5 / 4 5 =` $\to 2.333$, `1 0 5 - ( 2 * 4 5 ) =` (18 keystrokes, modal confusion) | **Single-Tap Euclidean `{{key:÷R}}`:** Hardware integer division deposits integer quotient $2$ in Register $X$ and exact remainder $15$ in Register $Y$ simultaneously in one step. | `105 {{key:ENTER}} 45 {{key:÷R}}` (8 keystrokes) | **56% fewer keystrokes** Simultaneous quotient and remainder display matches physical token distribution. |
| **Prime Factorization:** Cryptographic vault key factoring: $2,639 = 7 \times 13 \times 29$ | Standard algebraic calculators provide no hardware factoring. Students must manually test trial divisors on scratch paper ($2,639 \div 3, \div 7, \dots$) through tedious, error-prone trial division. | `2 6 3 9 / 3 =`, `2 6 3 9 / 7 =` $\to 377$, `3 7 7 / 1 1 =` $\dots$ (35+ keystrokes, manual logging) | **Hardware Prime Engine `{{key:FACT}}`:** Dedicated factoring co-processor parses composite numbers instantly into prime components, rendering $7 \times 13 \times 29$ across the daylight dot-matrix display. | `2639 {{key:FACT}}` (5 keystrokes) | **85% fewer keystrokes** Instant canonical decomposition; flashes `PRIME` or renders prime tower strings without guesswork. |
| **Statistical Mean:** Four test scores averaging: $88, 92, 79, 95 \implies \text{Mean} = 88.5$ | Must enter chained addition with parentheses `( 88 + 92 + 79 + 95 ) / 4 =`. Forgetting outer brackets divides only 95 by 4, creating an undetected order-of-operations error ($283.75$). | `( 8 8 + 9 2 + 7 9 + 9 5 ) / 4 =` (23 keystrokes, bracket risk) | **Hardware Statistical Accumulator (`{{key:Σ+}}`):** Each data point accumulates into dedicated $\Sigma$ registers with running sample count. Pressing `{{key:x̄}}` extracts the exact mean with zero syntax parentheses. | `{{key:CLΣ}} 88 {{key:Σ+}} 92 {{key:Σ+}} 79 {{key:Σ+}} 95 {{key:Σ+}} {{key:x̄}}` (16 keystrokes) | **Zero Parentheses Clutter** Running sample count protects data entry; enables instant spread and total sum queries. |

---

## Cicada Cycles, Fair Dice, and Wildlife Field Data in Action

Every keystroke sequence below starts from standard numeric mode (`{{key:NUM}}`). Whether you are testing a large candidate like `83` for primality (`{{res:sc6_07_data_probability_primes_seq_82:keys}}`, flashing `PRIME`) or finding the greatest common factor of `48` and `72` (`{{res:sc6_07_data_probability_primes_seq_83:keys}}` $\to 24$), these six connected story adventures bring your physical studios and your 4-register stack together!

### The High-Rollers Tabletop & Spinner Tournament
Welcome to the annual Tabletop Game Designers' Convention! As the chief tournament referee, your job is to check the fairness and exact odds of every die roll and card draw before the championship round begins. Game designers never guess whether a game mechanic feels fair—they calculate the exact fraction of winning outcomes on the stack before printing a single rulebook!

In the opening match at the dice table, a player needs to roll an odd number ($1, 3,$ or $5$) on a single six-sided equal-volume pip die from your Dice & Spinner Studio to unlock a treasure chest. Pick up one of your physical $d6$ dice and count the odd faces: 3 out of the 6 faces are odd. If you roll the die 60 times, you expect roughly 30 odd rolls. Comparing the 3 winning odd faces against all 6 faces of the cube on your SC-6 via `{{res:sc6_07_data_probability_primes_seq_01:keys}}` yields **`{{res:sc6_07_data_probability_primes_seq_01:value}}`**. Because half the faces of a standard cube are odd, the player's theoretical chance is an exact coin-flip ($\mathbf{0.5000}$ or $50\%$).

Moving from the dice table over to the championship card arena, a finalist needs to draw an Ace on the very first card pulled from a freshly shuffled 52-card deck. Since there are 4 suits (hearts, diamonds, clubs, and spades), there are 4 Aces hiding among the 52 cards. Dividing the 4 Aces by the 52-card deck on the stack with `{{res:sc6_07_data_probability_primes_seq_02:keys}}` produces **`{{res:sc6_07_data_probability_primes_seq_02:value}}`**. Because every suit holds 1 Ace out of 13 ranks ($4/52 = 1/13$), the opening-draw probability is $\mathbf{0.0769}$ ($\approx 7.69\%$)—rare enough to make the whole crowd gasp when an Ace turns over on the first draw!

---

### The Prime Number Fortress & Sieve
Next, you step into the convention's most popular tabletop adventure quest: the **Prime Number Fortress**, whose ancient stone doors only unlock when explorers solve prime and factor riddles!

The massive outer gate of the Prime Fortress opens only if the code carved into the bronze key—**`83`**—is an unbreakable prime number! Remember how 13 Counting Tiles refuse to form any rectangle of 2, 3, or 4 rows without leaving a tile sticking out? Let's test whether `83` has that same rectangular resistance without counting out 83 loose tiles across the game mat. Testing candidate 83 with the hardware primality key via `{{res:sc6_07_data_probability_primes_seq_06:keys}}` confirms **`{{res:sc6_07_data_probability_primes_seq_06:value}}`**. Because $9 \times 9 = 81$ and none of the primes below 9 ($2, 3, 5,$ or $7$) divide evenly into 83, the status line flashes `PRIME` and preserves $\mathbf{83}$ in Register $X$—swinging the outer gate wide open!

Inside the torchlit fortress courtyard, the inner archival vault is locked by two interlocking stone gears with **$18$ teeth** and **$24$ teeth** (and if you ever want to inspect every shared divisor of two gear wheels at once, the shifted common-factors key `{{key:C.FAC}}` lists them on the screen). To open the vault, you must prove the **Secret Partner Rule**: multiplying their Greatest Common Factor ($\text{GCF} = 6$) by their Least Common Multiple ($\text{LCM} = 72$) must equal $18 \times 24 = 432$! Chaining both keys on the stack with `{{res:sc6_07_data_probability_primes_seq_16:keys}}` lands on **`{{res:sc6_07_data_probability_primes_seq_16:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `18` | $0.0000$ | $0.0000$ | $0.0000$ | $18.0000$ | Key in first fortress number 18 |
| `{{key:ENTER}}` | $0.0000$ | $0.0000$ | $18.0000$ | $18.0000$ | Stack lifts; 18 locked into Register $Y$ |
| `24` | $0.0000$ | $0.0000$ | $18.0000$ | $24.0000$ | Key in second number 24 |
| `{{key:GCF}}` | $0.0000$ | $0.0000$ | $0.0000$ | $6.0000$ | Compute Greatest Common Factor of 18 and 24 ($6$) |
| `18` | $0.0000$ | $0.0000$ | $6.0000$ | $18.0000$ | Key in first number 18; GCF lifts to Register $Y$ |
| `{{key:ENTER}}` | $0.0000$ | $6.0000$ | $18.0000$ | $18.0000$ | Stack lifts; 18 locked into Register $Y$, 6 into Register $Z$ |
| `24` | $0.0000$ | $6.0000$ | $18.0000$ | $24.0000$ | Key in second number 24 |
| `{{key:LCM}}` | $0.0000$ | $0.0000$ | $6.0000$ | $72.0000$ | Compute Least Common Multiple of 18 and 24 ($72$); GCF stays in Register $Y$ |
| `{{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $432.0000$ | Multiply GCF by LCM ($6 \times 72 = 432$) |

The Secret Partner Rule holds identically ($18 \times 24 = 432$), and the stone vault door rumbles open! *(Pro tip: Since `{{key:GCF}}` saves `24` in `{{key:LASTX}}`, you can also replace `18 {{key:ENTER}} 24 {{key:LCM}}` with `18 {{key:LASTX}} {{key:LCM}}`.)*

---

### The Data Detective & Bell-Curve Mystery
Now put on your Data Detective badge! At the school science and track-and-field day, you use your `{{key:Σ+}}` statistical basket to find the fair-share **Mean (`{{key:x̄}}`)** in the classroom and the middle **Median (`{{key:MED}}`)** out on the running track.

First, inside the science lab, you score `88`, `92`, `79`, and `95` on four lab quizzes. What is your fair-share average (`{{key:x̄}}`)? Mark 88, 92, 79, and 95 with four Counting Tiles on a desk number line: notice how the two scores above $88.5$ ($+3.5$ and $+6.5$, totaling $+10$) balance the two scores below $88.5$ ($-0.5$ and $-9.5$, totaling $-10$). Tossing all four scores into `{{key:Σ+}}` and tapping `{{key:x̄}}` via `{{res:sc6_07_data_probability_primes_seq_19:keys}}` confirms **`{{res:sc6_07_data_probability_primes_seq_19:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Reset statistical registers ($\text{Count} = 0, \text{Sum} = 0$) |
| `88` | $0.0000$ | $0.0000$ | $0.0000$ | $88.0000$ | Key in first test score 88 |
| `{{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Accumulate score ($\text{Count} = 1, \text{Sum} = 88$) |
| `92` | $0.0000$ | $0.0000$ | $0.0000$ | $92.0000$ | Key in second test score 92 |
| `{{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Accumulate score ($\text{Count} = 2, \text{Sum} = 180$) |
| `79` | $0.0000$ | $0.0000$ | $0.0000$ | $79.0000$ | Key in third test score 79 |
| `{{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.0000$ | Accumulate score ($\text{Count} = 3, \text{Sum} = 259$) |
| `95` | $0.0000$ | $0.0000$ | $0.0000$ | $95.0000$ | Key in fourth test score 95 |
| `{{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | Accumulate score ($\text{Count} = 4, \text{Sum} = 354$) |
| `{{key:x̄}}` | $0.0000$ | $0.0000$ | $0.0000$ | $88.5$ | Compute mean ($354 \div 4 = 88.5$) |

Your fair-share mean lab score is $\mathbf{88.50}$.

Stepping outside from the science lab to the running track, five sprinters finish the 100-meter dash in $12.4, 12.8, 13.1, 13.5,$ and $14.0\text{ seconds}$. What is the middle **median** (`{{key:MED}}`) time? Line up five Counting Tiles from fastest to slowest on your desk: the third tile sits right in the middle with two sprinters faster and two sprinters slower, pointing straight to $13.1\text{ s}$. Entering the five sprint times into the statistical accumulator and tapping `{{key:MED}}` via `{{res:sc6_07_data_probability_primes_seq_20:keys}}` returns **`{{res:sc6_07_data_probability_primes_seq_20:value}}`**. With $5$ runners stored in Register $Y$, the middle runner's time of $\mathbf{13.10\text{ seconds}}$ appears in Register $X$.

---

### The Zero-Pair Vault & Pre-Algebra Ascent
Next, let's practice our two-color counter and sandbag/balloon intuition on two signed-number puzzles using `{{key:+/-}}`!

First, what happens when you hook $15$ sandbags ($-15$) onto a balloon basket, and then hook on $28$ *more* sandbags ($-28$)? Model a smaller version with Crimson counters first ($-3 + (-5) = -8$ Crimson tokens): because both groups pull in the exact same negative direction, there are zero Yellow tokens to cancel them out! Combining the two negative movements on the stack with `{{res:sc6_07_data_probability_primes_seq_27:keys}}` produces **`{{res:sc6_07_data_probability_primes_seq_27:value}}`**, as the two downward pulls add their sizes together to reach **$-43$**.

Now compare that with subtracting a larger positive number from a smaller one: suppose your student bank account has $\$45$ (45 Yellow $+1$ tokens), and an automatic purchase withdraws $\$70$. Where does your balance land? The first $\$45$ of the withdrawal cancels all 45 Yellow tokens down to $\$0$, and the remaining $\$25$ pulls you 25 steps below zero into Crimson debt ($-25$)! Evaluating $45 - 70$ on the SC-6 with `{{res:sc6_07_data_probability_primes_seq_28:keys}}` yields **`{{res:sc6_07_data_probability_primes_seq_28:value}}`**, wiping out your positive $\$45$ balance to $\$0$ and crossing zero into negative territory (**$-\$25$**).

---

### Number Theory Challenges & Directed Integer Navigation
Next, we combine our prime-hunting keys (`{{key:PRIME}}`) and signed-number navigation (`{{key:+/-}}`) to explore twin primes, guide a deep-sea submarine, and test a famous 300-year-old prime mystery!

Two prime numbers that sit just $2$ steps apart on the number line—like $(11, 13)$ or $(17, 19)$—are called **Twin Primes** (because the even number sandwiched between them is always divisible by $2$!). Let's use `{{key:PRIME}}` to verify that **$29$** and **$31$** are both prime, and then add them together on the stack via `{{res:sc6_07_data_probability_primes_seq_39:keys}}` to reach **`{{res:sc6_07_data_probability_primes_seq_39:value}}`**. Both candidates flash `PRIME` on the daylight LCD and sum to $\mathbf{60}$—a multiple of 12, which is true for every twin prime pair greater than $(3, 5)$!

From the number line, we dive into the deep ocean! A research submarine hovering at a depth of $-180\text{ m}$ ($180\text{ m}$ below sea level) puffs compressed air into its ballast tanks to rise $+65\text{ m}$, and then dives $-40\text{ m}$ into a trench canyon. Trace the submarine along a vertical number line ($-180 \to -115 \to -155$) and chain the moves on your SC-6 with `{{res:sc6_07_data_probability_primes_seq_43:keys}}` to land at **`{{res:sc6_07_data_probability_primes_seq_43:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `180` | $0.0000$ | $0.0000$ | $0.0000$ | $180.0000$ | Key in initial depth magnitude 180 |
| `{{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-180.0000$ | Negate to depth $-180\text{ m}$ |
| `{{key:ENTER}}` | $0.0000$ | $0.0000$ | $-180.0000$ | $-180.0000$ | Push initial depth to Register $Y$ |
| `65` | $0.0000$ | $0.0000$ | $-180.0000$ | $65.0000$ | Key in ascent $+65\text{ m}$ |
| `{{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-115.0000$ | Add ascent: $-180 + 65 = -115\text{ m}$; stack drops |
| `40` | $0.0000$ | $0.0000$ | $-115.0000$ | $40.0000$ | Key in dive descent $40\text{ m}$; stack lifts $-115$ to $Y$ |
| `{{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-155.0000$ | Deduct descent: $-115 - 40 = -155\text{ m}$; stack drops |

The submarine settles at a final depth of $\mathbf{155\text{ m}}$ below sea level ($-155.00$).

While the submarine crew rests on the canyon floor, they test a famous mathematical puzzle from the year 1742! That year, Christian Goldbach wrote a letter to Leonhard Euler with a bold guess: *Every even whole number greater than 2 can be built by adding two prime numbers together!* ($4 = 2+2$, $6 = 3+3$, $8 = 3+5$, $10 = 3+7\dots$). Even with modern supercomputers, no one has ever found an even number that breaks Goldbach's rule! Let's test the even number **$28$** by checking whether **$11$** and **$17$** are both prime and add up to $28$ using `{{res:sc6_07_data_probability_primes_seq_49:keys}}`, which confirms **`{{res:sc6_07_data_probability_primes_seq_49:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `11` | $0.0000$ | $0.0000$ | $0.0000$ | $11.0000$ | Key in first prime candidate 11 |
| `{{key:PRIME}}` | $0.0000$ | $0.0000$ | $0.0000$ | $11.0000$ | LCD flashes `PRIME`; preserves 11 in Register $X$ |
| `17` | $0.0000$ | $0.0000$ | $11.0000$ | $17.0000$ | Key in second candidate 17; stack lifts 11 to $Y$ |
| `{{key:PRIME}}` | $0.0000$ | $0.0000$ | $11.0000$ | $17.0000$ | LCD flashes `PRIME`; preserves 17 in Register $X$ |
| `{{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $28.0000$ | Sum primes $11 + 17 = 28$; stack drops |
| `11` | $0.0000$ | $0.0000$ | $28.0000$ | $11.0000$ | Key in 11 for second partition check; stack lifts 28 to $Y$ |
| `{{key:ENTER}}` | $0.0000$ | $28.0000$ | $11.0000$ | $11.0000$ | Push 11 to $Y$; lifts 28 to $Z$ (stack lift disabled) |
| `17` | $0.0000$ | $28.0000$ | $11.0000$ | $17.0000$ | Key in 17; overwrites $X$ since `ENTER` disabled lift |
| `{{key:+}}` | $0.0000$ | $0.0000$ | $28.0000$ | $28.0000$ | Sum $11 + 17 = 28$; stack drops, preserving first sum in $Y$ |

Register $X$ displays $28$ and Register $Y$ preserves $28$—Goldbach's Conjecture holds true for $28$!

---

### Compound Probability & Pre-Algebra Mastery Sprints
For our final adventure of Chapter 7, we return to the championship gaming table to compare two kinds of two-step probability: an **independent** event (where the first step has no effect on the second) and a **dependent** event (where keeping a card changes the deck for the second draw!).

First, suppose a board game bonus requires you to flip **Heads** on a fair coin ($\frac{1}{2}$) *and* roll a **$6$** on a six-sided die ($\frac{1}{6}$) on the same turn. Because the coin and the die don't affect each other, their $2 \times 6$ outcome grid has $12$ equally likely pairs, and only $1$ of those $12$ pairs is *(Heads, 6)*. Multiplying the two independent chances on the stack via `{{res:sc6_07_data_probability_primes_seq_51:keys}}` yields **`{{res:sc6_07_data_probability_primes_seq_51:value}}`**, giving a combined chance of $\text{Chance of Heads} \times \text{Chance of 6} = 1/12 \approx \mathbf{8.33\%}$.

Now compare that to drawing **two Aces in a row** from a 52-card deck *without putting the first card back*! On the first draw, $4$ of the $52$ cards are Aces ($4/52$). Once you hold that first Ace in your hand, only **$3$ Aces** remain among the **$51$ cards** left in the deck ($3/51$). Multiplying the two dependent step chances on the stack with `{{res:sc6_07_data_probability_primes_seq_52:keys}}` gives **`{{res:sc6_07_data_probability_primes_seq_52:value}}`**—a combined probability of $1/221 \approx \mathbf{0.45\%}$, happening only once in every 221 two-card deals!

---

## Where to Go Next: Companion Workbook Quests & Kitchen-Table Challenges

> *For 52 additional worked problems with full 4-register stack tables, see Chapter 7 of the [SC-6 Elementary Companion Problem & Activity Workbook](../../curriculum/sc6-elementary-companion-workbook.md).*

Ready to test your data-detective instincts and number-theory skills away from this chapter? Here is how to connect your Polyhedral Dice, Prime Factor Blocks, Counting Tiles, and SC-6 with the [Big Ideas Math Middle School Supplement](../../curriculum/big-ideas-middle-school-sc6-workbook.md) across **Unit 1: Numerical Expressions & Factors (Sections 1.4–1.5)**, **Unit 4: Algebraic Expressions & Properties (Sections 4.1–4.4)**, **Unit 6: Integers, Number Lines & The Coordinate Plane (Sections 6.1–6.5)**, **Unit 7: Equations & Inequalities (Sections 7.1–7.5)**, **Unit 9: Statistical Measures & Data Displays (Sections 9.1–9.4)**, and **Unit 10: Rational Numbers, Two-Step Equations & Probability (Sections 10.1–10.4)**:

1. **The 100-Roll Casino Boss Challenge (Curriculum Guide Unit 7 & Student Workbook):** Grab the 4 equal-volume pip dice from your Dice & Spinner Studio and roll two dice 36 times, logging each sum ($2$ through $12$) into `{{key:Σ+}}` on your SC-6 and stacking Counting Tiles into a live tabletop histogram. Tap `{{key:x̄}}`, `{{key:MED}}`, and `{{key:MODE}}`—did Lucky 7 win the tallest tower, and how close did your experimental mean get to $7.00$?
2. **The Impostor Prime Hunt (Timed Proficiency Trials — Prime Sieve Sprint):** Numbers like $91$, $119$, $133$, and $143$ love to disguise themselves as primes because they are odd and aren't divisible by $2, 3,$ or $5$. Race a partner to unmask all four impostors using `{{key:PRIME}}` and `{{key:FACT}}` on your SC-6, then build their secret prime towers on your Prime Factor Studio comparator stage!
3. **The Secret Partner Speed Proof (Big Ideas Middle School Supplement):** Pick any two mystery two-digit numbers—say, $36$ and $48$. Compute their `{{key:GCF}}`, then use `{{key:LASTX}}` so you don't have to re-type the second number when computing their `{{key:LCM}}`, and multiply the two results together. Can your family find *any* pair of whole numbers that breaks the Secret Partner Rule $\text{GCF} \times \text{LCM} = \text{First Number} \times \text{Second Number}$?

---

## Chapter Summary & Looking Ahead

With the probability generator, prime engine, statistical registers, and signed-number keys, you can analyze both discrete numbers and experimental data on the stack:

1. **Discrete Probability & Fair Symmetries:** You investigated fair polyhedral dice (`{{key:🎲}}`), experimental frequencies, and compound probability events without tree confusion.
2. **The Prime Factor Engine:** You used the Prime Factor Studio and SC-6 dedicated hardware keys (`{{key:PRIME}}`, `{{key:FACT}}`, `{{key:GCF}}`, `{{key:LCM}}`, `{{key:÷R}}`)—plus `{{key:LASTX}}`—to decompose composite numbers, calculate greatest common factors, and prove the Secret Partner Rule.
3. **Descriptive Statistics:** With the non-volatile statistical accumulator (`{{key:Σ+}}`), you evaluated real datasets, discovering how means, medians, and modes capture central tendencies while IQR and MAD reveal spread.
4. **Pre-Algebra & Directed Numbers:** You conquered negative numbers and zero pairs with the sign toggle (`{{key:+/-}}`) and distance metrics (`{{key:|x|}}`).

In **[Chapter 08: The Math Quiz Engine](08-math-quiz-engine.md)**, you will take everything you have learned and put your operational speed to the test. You will enter the interactive quiz game mode on your SC-6, solving rapid-fire arithmetic challenges, racing against the hardware timer, and tracking your accuracy streaks on the daylight LCD. Let's see how fast your mathematical reflexes really are!
