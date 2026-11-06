---
title: "Chapter 7: Prime Numbers, Fair Dice & Data Detective"
description: "Exploring fair game dice, prime building blocks, GCF/LCM secret partners, data-detective averages, and negative numbers on the SC-6."
---

# Chapter 7: Prime Numbers, Fair Dice & Data Detective

## The 17-Year Cicada Mystery & Nature's Prime Shield

Deep beneath the deciduous forests of eastern North America, millions of periodical cicada nymphs (*Magicicada septendecim*) sip tree-root sap in the dark for **17 years**—until, on a single warm spring weekend, billions of them tunnel out of the soil at once and fill the forest canopy with a deafening chorus {{cite:gould1977}}. Across living ecosystems, spacecraft communications, and tabletop games, **prime numbers and probability govern how creatures outsmart predators, how secret codes stay unbreakable, and how dice roll with equal chance.**

### Why Cicadas Count in Primes

Forest scientists and bug researchers spent years puzzling over a cool nature mystery {{cite:webb2001}}: **Why 13 years? Why 17 years?** Why didn't cicadas end up with a 12-year, 14-year, or 16-year life cycle?

To see the danger of a non-prime schedule, picture the **Composite Number Trap** that would happen if a cicada brood crawled out on a 12-year schedule. Because the number 12 is **composite**—with factors of $1, 2, 3, 4, 6,$ and $12$—hungry birds or wasps that boom every 2 years would be waiting for a feast on every single cicada emergence ($2 \times 6 = 12$). Worse still, a predator with a 3-year boom would meet them every single time ($3 \times 4 = 12$), and a predator with a 4-year boom would catch them every single time ($4 \times 3 = 12$). Hungry predators would wipe out the cicadas almost every time they crawled above ground!

Now compare that trap with the **Prime Number Shield** of 17. Because 17 is **prime**, its *only* factors are 1 and 17—so a predator cycle and a 17-year cicada cycle only line up at their **Least Common Multiple (`{{key:LCM}}`)**. A **2-year predator cycle** only syncs up with the cicadas once every **34 years** ($2 \times 17 = 34$), a **3-year predator cycle** has to wait a full **51 years** between feasts ($3 \times 17 = 51$), and a **5-year predator cycle** crosses paths with the brood just once every **85 years** ($5 \times 17 = 85$, longer than a human lifetime!). By sleeping underground for an exact prime number of years, cicadas outsmart every predator in the forest!

What happens when *two different* prime cicada broods—the **13-year Brood XIX** across the southern states and the **17-year Brood XIII** across the Midwest—live in neighboring forests? Because both $13$ and $17$ are prime numbers, they share no common factors other than $1$. Key `13 {{key:ENTER}} 17 {{key:LCM}}` onto your SC-6 right now: the screen flashes **`221`**! That means the 13-year and 17-year cicada broods crawl out of the ground in the exact same spring only **once every 221 years**. When both broods emerged together in the spring of **2024**, it was the first time they had met since **1803** (when Thomas Jefferson had just signed the Louisiana Purchase!), and they will not emerge together again until the year **2245** ($2024 + 221$). Primes are nature's secret code—the unbreakable building blocks of all whole numbers {{cite:gauss1809,singh1997}}.

---

### Why Board Games Use Fair 16 mm Dice

Ever wonder why your favorite tabletop adventure games use 4, 6, 8, 12, or 20-sided dice—but nobody sells a 7-sided or 11-sided die?

Over 2,300 years ago, Greek builders and geometers proved an amazing 3D secret: in our universe, there are **only five completely symmetrical 3D shapes** (called the Platonic Solids) where every single flat face is the exact same shape and size, and every corner meets the exact same number of edges:
1. **Tetrahedron (d4):** 4 matching equilateral triangle faces
2. **Cube (d6):** 6 matching square faces
3. **Octahedron (d8):** 8 matching equilateral triangle faces
4. **Dodecahedron (d12):** 12 matching 5-sided pentagon faces
5. **Icosahedron (d20):** 20 matching equilateral triangle faces

If you try to carve a 7-sided or 11-sided die, some sides will always be wider or flatter than others—so it can never land with equal chance! True fairness in gaming isn't just about giving the dice cup a good shake—it comes from building dice whose sides and corners match in every direction {{cite:gardner1959}}.

---

### Fair-Weight Dice, Spinners & Prime Factor Blocks

Before we tap keys on the calculator, we roll real dice, balance two-color counters, and build prime-number towers with our hands. Each physical studio kit on your desk teams up directly with a family of calculator keys we will explore step by step in this chapter. Your **Precision Dice & Spinner Studio (`{{key:🎲}}`)** sets up a desktop probability lab featuring 10-slice number lids (`0`–`9`), swap-in uneven ($50\%, 25\%, 15\%, 10\%$) and coin-flip (`0`/`1`) spinner plates, and four custom-engineered 6-sided dice paired with your SC-6's digital polyhedral dice (`{{key:🎲}}`, covering $d4, d6, d8, d10, d12,$ and $d20$). Right beside it, your **Prime Factor Studio (`{{key:PRIME}}`, `{{key:FACT}}`, `{{key:GCF}}`, `{{key:LCM}}`)** provides scaled Prime Factor Blocks ($2, 3, 5, 7\dots$) and a Comparator Stage whose heights add together when you multiply numbers, while your **Counting & Array Studio (`{{key:Σ+}}`, `{{key:x̄}}`, `{{key:MED}}`, `{{key:+/-}}`)** gives you four bright color groups of interlocking tiles for stacking tabletop bar charts as you tally data into `{{key:Σ+}}` and for building positive and negative Zero Pairs when you flip signs with `{{key:+/-}}`.

{{blocks:dice_spinner_probability|Probability Dice & Spinner Studio: 1x1 spinner enclosure with 10-sector lid, biased and binary dial plates, and 4 volume-equalized fair d6 dice}}

Have you ever looked closely at an ordinary store-bought plastic die and wondered if all six sides really weigh the same? On a cheap game die, every dot (called a **pip**) is scooped out to the exact same size and depth. That means the 6-dot face has **six times as much plastic scooped out** as the 1-dot face—making the 6-dot side slightly lighter and more likely to turn face-up when the heavy 1-dot side settles to the bottom!

Professional tournament dice and your 3D-printed **Dice & Spinner Studio** fix this hidden weight bias through **volume-equalized pips**. By making the single dot on the 1-face wider and deeper—and scaling the dots on the 2, 3, 4, 5, and 6 faces progressively shallower so all six faces lose the exact same volume of plastic—every face has the exact same mass and center of balance. Whenever you roll your physical studio dice on the desk or tap `{{key:🎲}}` on the SC-6, every face has an equal mathematical chance.

---

## Fair Dice, Spinners & Game Odds

Every time you flip a coin, spin a game-board spinner, or roll a die, you are exploring **Probability**—the branch of mathematics that measures how likely something is to happen on a scale from $0$ (completely impossible) to $1$ (guaranteed to happen every time):
$$\text{Probability of an Event} = \frac{\text{Number of Winning Outcomes}}{\text{Total Number of Equally Likely Outcomes}}$$

| Probability | What It Means | Classroom Example |
| :--- | :--- | :--- |
| **$0.0$** | Impossible | Rolling a `7` on a standard 6-sided die ($d6$) |
| **$0.5$** | Equally Likely ($50/50$) | Flipping Heads or Tails on a fair coin |
| **$1.0$** | Certain | Rolling a whole number from `1` to `6` on a standard $d6$ |

### Rolling Digital Dice & Custom Random Ranges
What if you want to run a 60-roll probability experiment right at your desk without chasing runaway dice across the classroom floor? Pressing the dedicated dice key `{{key:🎲}}` on your SC-6 keypad turns the screen into an instant digital dice cup. Each press of `{{key:🎲}}` wakes up the calculator's random number roller, drawing crisp $17 \times 17$ pixel die faces right on the display (`T` and `X`) with classic dot patterns—from a single center dot for `1`, diagonal pairs and triples for `2` and `3`, four corner dots ($2 \times 2$ square) for `4`, four corners plus a center dot ($4 + 1$) for `5`, up to two columns of three dots ($2 \times 3$ rectangle) for `6`. Even better, the number you rolled ($1 \dots 6$) lands directly on Shelf $X$ with **automatic stack lift** ($X \to Y \to Z \to T$), so you can roll two dice (`2d6`) and tap `{{key:+}}` to add them, or tap `{{key:Σ+}}` to log 50 rolls in a row.

When your game or science experiment needs a 20-sided die ($d20$), a coin flip (`1` or `2`), or a random student number from `1` to `28`, two shifted random-range keys let you build any custom spinner or die you can imagine. The **`{{key:1…x}}` (Random 1 to X)** key picks a random whole number from $1$ up to whatever number is sitting on Shelf $X$: type `20 {{key:1…x}}` to roll a 20-sided die ($d20$ from $1$ to $20$), type `2 {{key:1…x}}` to flip a fair coin ($1 = \text{Heads}, 2 = \text{Tails}$), or type `28 {{key:1…x}}` to pick a random lab partner from a class of 28 students. And when you want a custom starting number other than $1$, the **`{{key:t…x}}` (Random Y to X)** key picks a random whole number between the starting number on Shelf $Y$ and the ending number on Shelf $X$—for example, keying `10 {{key:ENTER}} 99 {{key:t…x}}` generates a random two-digit number from $10$ to $99$:

| Tabletop Randomizer | Physical Studio Piece | SC-6 Keystrokes | Possible Outcomes |
| :--- | :--- | :--- | :--- |
| **Fair Coin Flip** | Binary `0`/`1` Spinner Plate | `2 {{key:1…x}}` | `1` (Heads) or `2` (Tails) |
| **Standard 6-Sided Die ($d6$)** | Volume-Equalized $16\text{ mm}$ Cube | `{{key:🎲}}` *(or `6 {{key:1…x}}`)* | Graphic die face `1` through `6` |
| **10-Slice Spinner (`1`–`10`)** | 10-Sector Probability Lid | `10 {{key:1…x}}` | Whole numbers `1` through `10` |
| **20-Sided Adventure Die ($d20$)** | 20-Triangle Icosahedron | `20 {{key:1…x}}` | Whole numbers `1` through `20` |
| **Two-Digit Mystery Draw** | Custom Range ($Y$ to $X$) | `10 {{key:ENTER}} 99 {{key:t…x}}` | Any two-digit number `10` to `99` |

Why doesn't a real die land on `4` *exactly* once every 6 rolls? Because **Expected Odds** (theoretical probability) tell you what happens over thousands of rolls, while **Real-Life Trials** (experimental probability) record what actually happened in your game today. Roll a standard six-sided die 60 times at your desk: on any single roll, the expected chance of rolling a 4 is $\frac{1}{6}$, so across 60 rolls a 4 should appear about $60 \times \frac{1}{6} = 10\text{ times}$:

$$\text{Expected Chance of Rolling a 4} = \frac{1}{6} \approx 0.1667 \ (16.67\%)$$
$$\text{Expected Count} = 60 \times \frac{1}{6} = 10\text{ times}$$

In a real 60-roll classroom trial, you might see a 4 turn up twelve times instead of ten. With Whole Number Mode (`{{key:NUM}}`) toggled off (or after tapping `{{key:FIX}} 4` / `{{key:ALL}}`), dividing your 12 wins by the 60 total rolls on the stack with `12 {{key:ENTER}} 60 {{key:÷}}` gives a real-life rate of $0.2000$ ($20.0\%$), and subtracting the expected $\frac{1}{6}$ share with `0.20 {{key:ENTER}} 1 {{key:ENTER}} 6 {{key:÷}} {{key:-}}` shows a $+0.0333$ ($+3.33\%$) difference.

Game designers use this exact ratio (`Winning Outcomes ÷ Total Outcomes`) to check the fairness of every die roll and card draw before printing a rulebook. Pick up one of your physical $d6$ dice and count the odd faces ($1, 3,$ and $5$): 3 out of the 6 faces are odd. Dividing 3 by 6 on your SC-6 with `{{res:sc6_07_data_probability_primes_seq_01:keys}}` gives **`{{res:sc6_07_data_probability_primes_seq_01:value}}`**—an exact coin-flip ($\mathbf{0.5000}$ or $50\%$), so across 60 rolls you can expect roughly 30 odd numbers.

The same ratio works for a 52-card deck when a player wants to draw an Ace on the very first card. Since each of the 4 suits (hearts, diamonds, clubs, and spades) has 1 Ace, there are 4 Aces in the 52-card deck: keying `{{res:sc6_07_data_probability_primes_seq_02:keys}}` gives **`{{res:sc6_07_data_probability_primes_seq_02:value}}`**, or $\mathbf{0.0769}$ ($\approx 7.69\%$, which simplifies to $4/52 = 1/13$).

---

### Galileo's Dice Mystery & the 36-Outcome Grid
Here is a classic board-game mystery: when you roll **two** six-sided dice and add them together, the possible totals run from $2$ all the way to $12$. Are all eleven sums equally likely? Not even close.

Imagine painting the first die **Red** and the second die **Blue**. Because each of the 6 faces on the Red die can pair up with any of the 6 faces on the Blue die, there are $6 \times 6 = \mathbf{36\text{ equally likely pairs}}$ of *(Red Die, Blue Die)*. Look at what happens when we list all 36 pairs by their sum: to roll a **$2$** ("snake eyes"), both dice *must* land on $1$ as $(1,1)$, giving **only 1 way** out of 36; and to roll a **$12$** ("boxcars"), both dice *must* land on $6$ as $(6,6)$, again giving **only 1 way** out of 36. Now look at **$7$**: if the Red die lands on *anything at all*—$1, 2, 3, 4, 5,$ or $6$—there is an exact partner on the Blue die that makes $7$: $(1,6), (2,5), (3,4), (4,3), (5,2),$ and $(6,1)$. That gives **6 different ways** to roll a $7$—making **$7$** the tallest bar in the center of the rooftop pyramid.

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

Look at the `Count` column (`1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1`): if you stack one **Counting Tile** on your studio tray for each winning pair in that column, the eleven stacks rise by 1 tile per step up to **Lucky $7$** (6 tiles tall) and step back down to $12$ (1 tile tall) like a symmetric rooftop pyramid! That rooftop shape is the exact reason strategy board games like *Catan* put the robber on **$7$** and place the highest-value resource tiles on **$6$** and **$8$** ($5/36$ each). Enter `6` ways out of `36` on your stack to simplify the exact probability of rolling a $7$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0 {{key:.}} 6 {{key:.}} 36 {{key:SIMP}}` | 0 | 0 | 0 | **1/6** | 6 ways out of 36 simplifies by their $\text{GCF} = 6$ to **$\frac{1}{6}$** |
| `{{key:FDISP}}` | 0 | 0 | 0 | **0.1667** | Toggle fraction/decimal view: $\frac{1}{6} \approx \mathbf{16.67\%}$ |

The probability of rolling a sum of $7$ is **$1/6 \approx 16.67\%$**—six times more likely than rolling a $2$ or a $12$.

Even the greatest scientists in history used this exact step-by-step table trick when dice puzzles got tricky! In 1620, the Grand Duke of Tuscany asked the Italian astronomer **Galileo Galilei** a question (*Sopra le Scoperte dei Dadi*) that had stumped every board-game player in Florence: when you roll **three** six-sided dice and add them up, why does a total of **$10$** show up slightly more often than a total of **$9$**—even though both $9$ and $10$ can be split into three die numbers in the exact same number of ways ($6$ combinations each)?

Galileo solved the mystery not with complicated formulas, but by writing out the full table of ordered outcomes ($6 \times 6 \times 6 = 216$ possibilities, just like your $6 \times 6 = 36$ table for two dice!). He showed that three different numbers like $(6,3,1)$ can land on the three dice in **$6$ different orders**, whereas a triple like $(3,3,3)$—which adds to $9$—can only land in **$1$ single way**. Counting every ordered roll gave $10$ twenty-seven winning outcomes ($27/216$) and $9$ only twenty-five ($25/216$). Whenever a probability question seems confusing, writing out the fair outcomes step by step makes the hidden pattern pop right out!

What if you pair two different random tools together—like flipping **Heads** on a fair coin ($\frac{1}{2}$) *and* rolling a **$6$** on a six-sided die ($\frac{1}{6}$) on the same turn? Because the coin and the die don't affect each other, their $2 \times 6$ outcome grid has $12$ equally likely pairs, and only $1$ of those $12$ pairs is *(Heads, 6)*. Multiplying the two chances on the stack via `{{res:sc6_07_data_probability_primes_seq_51:keys}}` yields **`{{res:sc6_07_data_probability_primes_seq_51:value}}`**, giving a combined chance of $\text{Chance of Heads} \times \text{Chance of 6} = 1/12 \approx \mathbf{8.33\%}$.

### Drawing Marbles Without Putting Them Back
What happens when you pull a marble out of a bag (or deal a card from a deck) and **keep it in your hand** instead of tossing it back in? Now the bag has *one fewer marble* inside, so the odds on your second draw change.

| First Draw Outcome ($8$ Marbles) | Second Draw Outcome ($7$ Remaining) | Combined Branch Probability |
| :--- | :--- | :---: |
| **Red 1st ($5/8$)** | Red 2nd ($4/7$) | $\frac{5}{8} \times \frac{4}{7} = \frac{20}{56}$ |
| **Red 1st ($5/8$)** | Blue 2nd ($3/7$) | $\frac{5}{8} \times \frac{3}{7} = \frac{15}{56}$ |
| **Blue 1st ($3/8$)** | Red 2nd ($5/7$) | $\frac{3}{8} \times \frac{5}{7} = \frac{15}{56}$ |
| **Blue 1st ($3/8$)** | **Blue 2nd ($2/7$)** | $\frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \mathbf{\frac{3}{28}}$ |

Reach into a cloth bag containing 5 Red and 3 Blue marbles ($8$ marbles in all) and draw two marbles without looking and without putting the first marble back. What is the chance of drawing two Blue marbles in a row? On your first reach, $3$ out of $8$ marbles are Blue ($\frac{3}{8}$). Once you hold that Blue marble in your hand, only $2$ Blue marbles remain among the $7$ marbles left in the bag ($\frac{2}{7}$). Multiply the two step chances together:
$$\text{Chance of Both Blue} = \text{Chance of 1st Blue} \times \text{Chance of 2nd Blue} = \frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \frac{3}{28}$$

On the stack (with `{{key:NUM}}` toggled off or in `{{key:ALL}}` decimal view), compute the first draw probability $\frac{3}{8}$, compute the second draw probability $\frac{2}{7}$, and multiply them with `3 {{key:ENTER}} 8 {{key:÷}} 2 {{key:ENTER}} 7 {{key:÷}} {{key:×}}` to obtain $0.107143$. Tapping `{{key:FDISP}}` switches to exact fraction view ($\mathbf{3/28}$), showing that the probability of drawing two blue marbles in a row is $3/28 \approx \mathbf{10.71\%}$.

What if someone asks for the chance of drawing **at least one Red marble** in those two picks? Instead of adding up three different branches (Red-Red, Red-Blue, and Blue-Red), use a clever shortcut: notice that the *only* way to miss Red completely is to draw **Both Blue** ($\frac{3}{28}$). Subtracting the chance of Both Blue from $1$ ($100\%$) gives the answer in one step:
$$\text{Chance of At Least One Red} = 1 - \text{Chance of Both Blue} = 1 - \frac{3}{28} = \frac{25}{28}$$

Enter `1` ($100\%$), divide `3` by `28`, and subtract with `1 {{key:ENTER}} 3 {{key:ENTER}} 28 {{key:÷}} {{key:-}}` to reach $0.892857$—and one tap of `{{key:FDISP}}` reveals the exact fraction $\mathbf{25/28}$ ($\approx \mathbf{89.29\%}$).

That same keep-it-in-your-hand rule explains why drawing **two Aces in a row** from a 52-card deck is such a rare event. On the first draw, $4$ of the $52$ cards are Aces ($4/52$). Once you hold that first Ace in your hand, only **$3$ Aces** remain among the **$51$ cards** left in the deck ($3/51$). Multiplying the two step chances on the stack with `{{res:sc6_07_data_probability_primes_seq_52:keys}}` gives **`{{res:sc6_07_data_probability_primes_seq_52:value}}`**—a combined probability of $1/221 \approx \mathbf{0.45\%}$, happening only once in every 221 two-card deals. And whenever you want to simplify a single-draw bag ratio—such as reaching into a cloth pouch holding $9$ winning gold tokens and $3$ silver tokens ($12$ tokens in all)—typing `0 {{key:.}} 9 {{key:.}} 12 {{key:SIMP}}` immediately reduces the $9/12$ chance to $\mathbf{3/4} = 75\%$.

---

## Prime Numbers, Factor Towers & The Secret Partner Rule

Now let's return to the 17-year cicada mystery from the start of our chapter. Why are prime numbers like $2, 3, 5, 7, 11, 13,$ and $17$ so special? Just as every molecule in chemistry is built out of atoms, **every whole number greater than 1 is built by multiplying a unique team of prime numbers together**. Across your desk and your SC-6 screen, you can explore prime numbers in three connected ways: testing whether **Counting Tiles** form flat rectangles, stacking scaled **Prime Factor Studio** blocks on the comparator stage so block heights multiply numbers automatically, and tapping your number-detective keys (`{{key:PRIME}}`, `{{key:FACT}}`, `{{key:GCF}}`, and `{{key:LCM}}`) on the 4-shelf stack.

### The Rectangle Test for Prime Numbers
How can you tell with your bare hands whether a number is **prime** or **composite**? Grab 12 **Counting Tiles** from your 24-Tile Studio: you can arrange them into a neat $2 \times 6$ rectangle or a $3 \times 4$ rectangle with zero leftovers. Now add one more tile to make 13 and try building a rectangle 2, 3, or 4 tiles wide. Every attempt leaves an extra tile sticking out—the only rectangle 13 tiles can form is a single skinny $1 \times 13$ line! That is the geometric meaning of a prime number: it cannot be factored into two side lengths greater than 1.

| Number Classification | Tile Count | Complete Rectangular Factor Arrays | Positive Divisors |
| :--- | :--- | :--- | :--- |
| **Composite (12 Tiles)** | 12 Tiles | $1 \times 12$, $2 \times 6$, and $3 \times 4$ complete rectangles | `1, 2, 3, 4, 6, 12` (6 factors) |
| **Prime (13 Tiles)** | 13 Tiles | Rows of 2, 3, or 4 always leave 1 leftover tile; only $1 \times 13$ forms a rectangle | `1, 13` (2 factors only) |

Comparing your 12-tile rectangle and 13-tile line on the SC-6 shows that exact difference in a single glance:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `12` | 0 | 0 | 0 | 12 | Type 12 onto Shelf $X$ |
| `{{key:PRIME}}` | 0 | 0 | 0 | 12 | Screen flashes `COMPOSITE` while keeping 12 on Shelf $X$ |
| `13` | 0 | 0 | 12 | 13 | Type 13 onto Shelf $X$; 12 lifts to Shelf $Y$ |
| `{{key:PRIME}}` | 0 | 0 | 12 | 13 | Screen flashes `PRIME` while keeping 13 on Shelf $X$ |

---

### The Four-Color Sieve of Eratosthenes
Over two thousand years ago, the Greek librarian Eratosthenes of Cyrene (c. 276–194 BC) discovered a remarkably fast way to trap every prime number on a number grid. Because $10 \times 10 = 100$ (and $12 \times 12 = 144$), any composite number up to 100 must have at least one prime factor smaller than 10. That means setting aside $1$ and crossing out the multiples of just four small primes—**2, 3, 5, and 7**—automatically leaves behind all **25 primes under 100**!

With your individual 24-tile kit, you can build a $4 \times 6$ grid to hunt down all 9 primes up to 24—or pool 6 student kits across a classroom table ($6 \times 24 = 144$ tiles: 36 each of Archival White, Cobalt Blue, Radiant Gold, and Slate Gray) to build a giant $12 \times 12$ sieve and uncover all 34 primes up to 144.

Run the four-color sweep across your tile grid in four fast moves:
1. **Set Aside Unit `1`:** Place Tile `1` (Archival White) aside at the top-left corner, since $1$ is the single unit building block rather than a prime.
2. **Cobalt Blue Sweep (Multiples of Prime `2`):** Leave Tile `2` untouched as your first prime survivor, and cover every higher even multiple ($4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, \dots$) with **Cobalt Blue** tiles—knocking out half the grid in a single pass!
3. **Radiant Gold Sweep (Multiples of Prime `3`):** Move to the next uncovered spot, **Prime 3**, keep it safe, and cover every remaining odd multiple of $3$ ($9, 15, 21, 27, 33, 39, 45, 51, 57, 63, \dots$) with **Radiant Gold** tiles.
4. **Archival White Sweep (Multiples of Primes `5` & `7`):** In the 6-kit classroom pool, cover the remaining multiples of **5 and 7** ($25, 35, 49, 55, 65, 77, 85, 91, 95, 115, 119, 121, 125, \dots$) with patterned **Archival White** tiles.

Every **Slate Gray** tile still standing untouched at the end of the sweep is a **Prime Survivor**! In a single 24-tile kit, the 9 survivor tiles are **$2, 3, 5, 7, 11, 13, 17, 19, 23$**. Across a 100-chart, 25 primes survive up to $97$, and across a 6-kit classroom pool ($144$ tiles), all 34 primes $\le 144$ survive:  
$2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139$.

Notice how the eighties end with two true prime survivors—**$83$** and **$89$**—whereas the nineties and early hundreds hide sneaky "impostor primes" that look prime at first glance because they are odd and don't end in $5$, yet are secret multiples of $7$. You can test each survivor or impostor right on your SC-6! Under 100, keying `{{res:sc6_07_data_probability_primes_seq_68:keys}}` flashes `PRIME` on the top banner while keeping `97` on the bottom line, whereas keying `{{res:sc6_07_data_probability_primes_seq_69:keys}}` (or `{{res:sc6_07_data_probability_primes_seq_70:keys}}`) flashes `COMPOSITE` while keeping `91` ($7 \times 13$, a neat $7 \times 13$ tile rectangle!) and neighbor prime $89$ (`{{res:sc6_07_data_probability_primes_seq_71:keys}}`) flashes `PRIME`. Past 100, testing $119$ (`{{res:sc6_07_data_probability_primes_seq_72:keys}}`) unmasks another multiple of $7$ ($119 = 7 \times 17$) while `{{res:sc6_07_data_probability_primes_seq_73:keys}}` confirms `PRIME`. Whenever any candidate flashes `COMPOSITE`, simply tap `{{key:FACT}}` right afterward to unmask its hidden prime factors on the LCD.

---

### Multiplying by Stacking Prime Factor Blocks
Normally, stacking two blocks *adds* their heights together. Could we design special blocks where stacking two blocks on top of each other **multiplies** their numbers instead?

That is the secret behind your **Prime Factor Studio**. The back wall of the studio has a logarithmic ruler scale numbered from $1$ to $100$ where the marks get closer together as you climb higher (every time a number doubles—$2, 4, 8, 16, 32$—it steps up by the exact same $7.00\text{ mm}$ height). Each prime block is 3D-printed to match that scale: **Prime 2 (Blue)** stands $7.00\text{ mm}$ ($1\text{U}$) tall, **Prime 3 (Amber/Green)** stands $11.09\text{ mm}$ tall, **Prime 5 (Yellow)** stands $16.25\text{ mm}$ tall, and **Prime 7 (Red)** stands $19.65\text{ mm}$ tall. Because the ruler scale is spaced by multiplication steps, **adding block heights on the stage automatically multiplies their numbers**.

{{blocks:prime_studio_comparator_stage|Prime Factor Studio: Side-by-Side Factor Tower Comparator Stage & Prime Factor Blocks}}

Try stacking your Prime Blocks right on the tower-matching stage to watch height addition turn into multiplication. If you place Blue Block `2` ($7.00\text{ mm}$) on the stage and stack Amber/Green Block `3` ($11.09\text{ mm}$) on top, their combined height ($7.00\text{ mm} + 11.09\text{ mm} = \mathbf{18.09\text{ mm}}$) lines up **right on the "6" tick mark** on the back wall, showing $2 \times 3 = 6$! Swap the `3` block for Yellow Block `5` ($16.25\text{ mm}$), and the new stack ($7.00\text{ mm} + 16.25\text{ mm} = \mathbf{23.25\text{ mm}}$) lands squarely on the line labeled **"10"** ($2 \times 5 = 10$). Even a larger number like $60 = 2 \times 2 \times 3 \times 5$ works the exact same way: when you stack two `2` blocks, one `3` block, and one `5` block, adding their heights ($7.00\text{ mm} + 7.00\text{ mm} + 11.09\text{ mm} + 16.25\text{ mm} = \mathbf{41.34\text{ mm}}$) points straight at the **"60"** line on the rear wall. Best of all, if you reorder that tower—putting Yellow `5` on the bottom, then `3`, then both `2`s—the total height stays locked at **$41.34\text{ mm}$** ($5 \times 3 \times 2 \times 2 = 60$), proving with your hands that the order in which you multiply prime factors never changes the product!

{{blocks:prime_studio_commutativity|Prime Studio Turn-Around Rule Proof: Stacking 2 × 5 and 5 × 2 to the Exact Same Height}}

Now compare your physical block tower to the screen. Keying `{{res:sc6_fact_60:keys}}` on the SC-6 breaks `{{res:sc6_fact_60:value}}` directly into its prime building blocks (`2 × 2 × 3 × 5`), matching your four stacked blocks block-for-block:

{{res:sc6_fact_60:screenshot|SC-6 Prime Factorization Mode: 60 = 2 x 2 x 3 x 5}}

How does your SC-6 uncover that exact `2² × 3 × 5` prime tower the instant you type `60` and tap `{{key:FACT}}`? Under the hood, the calculator runs a lightning-fast **prime factor peel** from the smallest prime upward, while keeping `60` safely untouched on Shelf $X$ (`T = 0, Z = 0, Y = 0, X = 60`). Because $60$ is an even number, it first peels off one Blue `2` block ($60 \div 2 = 30$) and immediately peels off a second Blue `2` block ($30 \div 2 = 15$), bundling those twin factors into `2²`. Since $15$ is odd and $2$ no longer fits evenly, the calculator steps up to the next prime number, $3$, and peels off one Amber/Green `3` block ($15 \div 3 = 5$). That leaves a quotient of $5$, which is itself a prime number—one Yellow `5` block! Every composite number has only *one* set of prime building blocks (mathematicians call this the **Fundamental Theorem of Arithmetic**), so whether you build the tower on your desk or tap `{{key:FACT}}` on your SC-6, `60` always unlocks the exact same prime signature: **`2² × 3 × 5`**.

---

### The Prime Detective Key
On the SC-6, pressing the primary key `{{key:PRIME}}` tests the whole number sitting on Shelf $X$ in a flash: it momentarily flashes `PRIME` or `COMPOSITE` on the top status banner while leaving Shelf $X$ and the rest of the 4-shelf stack completely untouched so you can immediately keep working with your number.

Why isn't the number `1` considered prime? A prime number must have *two different factors* ($1$ and itself), whereas $1$ has only *one* factor. Even deeper, remember the **Fundamental Theorem of Arithmetic**: every composite number has *one unique* prime block tower (like $12 = 2 \times 2 \times 3$). If mathematicians called $1$ a prime number, you could tack on $\times 1$ forever ($12 = 2 \times 2 \times 3 \times 1 = 2 \times 2 \times 3 \times 1 \times 1 \dots$) and no number would have a unique prime signature! That is why $1$ is a single building unit (neither prime nor composite): testing `1` with `{{res:sc6_07_data_probability_primes_seq_79:keys}}` flashes `NEITHER` because $1$ is neither prime nor composite, whereas testing `2` with `{{res:sc6_07_data_probability_primes_seq_80:keys}}` flashes `PRIME` and keeps `2` on Shelf $X$ as the smallest prime number and the only even prime.

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `97` | 0 | 0 | 0 | 97 | Type 97 onto Shelf $X$ |
| `{{key:PRIME}}` | 0 | 0 | 0 | 97 | Screen flashes `PRIME` |
| `119` | 0 | 0 | 97 | 119 | Type 119; 97 lifts to Shelf $Y$ |
| `{{key:PRIME}}` | 0 | 0 | 97 | 119 | Screen flashes `COMPOSITE` ($7 \times 17$) |
| `2` | 0 | 97 | 119 | 2 | Type 2; stack lifts 119 to Shelf $Y$ and 97 to Shelf $Z$ |
| `{{key:PRIME}}` | 0 | 97 | 119 | 2 | Screen flashes `PRIME` (the only even prime) |

Why do modern computers spend so much time testing whether numbers are prime? Every time you log into a website, send a private message, or buy something online, your computer protects your secret password using **prime-number cryptography** (such as RSA encryption, invented in 1977 by Ron Rivest, Adi Shamir, and Leonard Adleman). A computer picks two secret prime numbers and multiplies them together to create a public lock key. Multiplying two primes forward takes a fraction of a millisecond, but factoring a giant composite number backward into its two secret prime building blocks is so hard that even the world's fastest supercomputers would need years to crack it.

When building a miniature encryption lock key, you first want to test whether the candidate **`83`** (`{{res:sc6_07_data_probability_primes_seq_82:keys}}`) is a true prime number before multiplying it into a public key. Remember how 13 Counting Tiles refuse to form any rectangle of 2, 3, or 4 rows without leaving a tile sticking out? Testing candidate 83 with the prime key via `{{res:sc6_07_data_probability_primes_seq_06:keys}}` confirms **`{{res:sc6_07_data_probability_primes_seq_06:value}}`**: because $9 \times 9 = 81$ and none of the primes below 9 ($2, 3, 5,$ or $7$) divide evenly into 83, the status line flashes `PRIME` and keeps $\mathbf{83}$ ready on Shelf $X$.

Because `{{key:PRIME}}` keeps each number on the stack, you can test two primes in a row and immediately combine them. For example, two prime numbers that sit just $2$ steps apart on the number line—like $(11, 13)$ or $(17, 19)$—are called **Twin Primes** (because the even number sandwiched between them is always divisible by $2$). Let's use `{{key:PRIME}}` to verify that **$29$** and **$31$** are both prime, and then add them together on the stack via `{{res:sc6_07_data_probability_primes_seq_39:keys}}` to reach **`{{res:sc6_07_data_probability_primes_seq_39:value}}`**. Both candidates flash `PRIME` on the screen and add up to $\mathbf{60}$—a multiple of 12, which is true for every twin prime pair bigger than $(3, 5)$.

You can also use `{{key:PRIME}}` to test a famous 300-year-old mathematical puzzle from the year 1742. That year, Christian Goldbach wrote a letter to Leonhard Euler with a bold guess: *Every even whole number greater than 2 can be built by adding two prime numbers together* ($4 = 2+2$, $6 = 3+3$, $8 = 3+5$, $10 = 3+7\dots$).

Even with modern supercomputers testing numbers up into the quintillions, no one has ever found an even number that breaks Goldbach's rule. Better yet, because `{{key:PRIME}}` checks a number on Shelf $X$ without erasing or changing it, testing `11 {{key:PRIME}} 17 {{key:PRIME}} {{key:+}}` gives the exact same sum as a normal `11 {{key:ENTER}} 17 {{key:+}}` addition! Let's run both side by side with `{{res:sc6_07_data_probability_primes_seq_49:keys}}` so both sums sit together as **`{{res:sc6_07_data_probability_primes_seq_49:value}}`** on Shelves $Y$ and $X$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `11` | $0.0000$ | $0.0000$ | $0.0000$ | $11.0000$ | Type the first prime candidate 11 onto Shelf $X$ |
| `{{key:PRIME}}` | $0.0000$ | $0.0000$ | $0.0000$ | $11.0000$ | Screen flashes `PRIME`; keeps 11 on Shelf $X$ |
| `17` | $0.0000$ | $0.0000$ | $11.0000$ | $17.0000$ | Type the second candidate 17; 11 lifts to Shelf $Y$ |
| `{{key:PRIME}}` | $0.0000$ | $0.0000$ | $11.0000$ | $17.0000$ | Screen flashes `PRIME`; keeps 17 on Shelf $X$ |
| `{{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $28.0000$ | Add both primes together ($11 + 17 = 28$) |
| `11` | $0.0000$ | $0.0000$ | $28.0000$ | $11.0000$ | Type 11 for a second check; 28 lifts to Shelf $Y$ |
| `{{key:ENTER}}` | $0.0000$ | $28.0000$ | $11.0000$ | $11.0000$ | Copy 11 onto Shelf $Y$; 28 lifts to Shelf $Z$ |
| `17` | $0.0000$ | $28.0000$ | $11.0000$ | $17.0000$ | Type 17 onto Shelf $X$ |
| `{{key:+}}` | $0.0000$ | $0.0000$ | $28.0000$ | $28.0000$ | Add $11 + 17 = 28$; both Shelf $Y$ and Shelf $X$ show 28 |

Both Ground Shelf $X$ and Shelf $Y$ show $28$—proving that Goldbach's 300-year-old guess works for $28$ ($11 + 17 = 28$), and you can even find a second prime pair for $28$ by testing $5 + 23 = 28$!

---

### Prime Factor Trees & Venn Diagrams
Whenever `{{key:PRIME}}` tells you a number is `COMPOSITE`, you naturally want to know: *Which prime blocks multiply together to build it?* Pressing `{{key:FACT}}` (`{{key:g}}` + `{{key:PRIME}}`) breaks any whole number $\ge 2$ into its prime building blocks, showing exponents and multiplication dots right on the screen—so keying `12` `{{key:FACT}}` displays **`2² × 3`**, keying `140 {{key:FACT}}` displays **`2² × 5 × 7`**, keying `360` `{{key:FACT}}` displays **`2³ × 3² × 5`**, and keying `2639` `{{key:FACT}}` unmasks **`7 × 13 × 29`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `360` | 0 | 0 | 0 | 360 | Type 360 (the degrees in a full circle) onto Shelf $X$ |
| `{{key:FACT}}` | 0 | 0 | 0 | 360 | Displays `2³ × 3² × 5` while keeping 360 on Shelf $X$ |

---

### Shared Prime Blocks: Greatest Common Factor & Least Common Multiple

In Chapter 5, you met the `{{key:GCF}}` and `{{key:LCM}}` keys as fast tools for simplifying fractions and finding Least Common Denominators. Now we can look under the hood with our **Prime Factor Blocks** to see *why* GCF and LCM are secret partners. Pressing the primary key **`{{key:GCF}}`** finds the **Greatest Common Factor** of Shelf $Y$ and Shelf $X$—for example, keying `{{res:sc6_gcf_12_18:keys}}` stages $12$ on Shelf $Y$ and $18$ on Shelf $X$, then returns their largest shared factor **`{{res:sc6_gcf_12_18:value}}`**. Pressing the shifted key **`{{key:LCM}}`** finds the **Least Common Multiple** of Shelf $Y$ and Shelf $X$—for example, keying `{{res:sc6_lcm_12_18:keys}}` returns **`{{res:sc6_lcm_12_18:value}}`**, the smallest grid size that both $12$ and $18$ divide into evenly.

You can see how GCF and LCM share their prime blocks by drawing a **Two-Circle Prime Factor Venn Diagram** on your desk for the numbers **$48$** and **$72$**. First, break down $48 = 2 \times 2 \times 2 \times 2 \times 3$ (four `2` blocks and one `3` block) and $72 = 2 \times 2 \times 2 \times 3 \times 3$ (three `2` blocks and two `3` blocks). Next, slide every matching pair of prime blocks that both numbers share (**three `2`s and one `3`**) into the **Center Overlap**: multiplying those shared center blocks (or keying `{{res:sc6_07_data_probability_primes_seq_83:keys}}` on the stack) gives the Greatest Common Factor:
$$\text{GCF} = 2 \times 2 \times 2 \times 3 = 8 \times 3 = \mathbf{24}$$
Finally, place the leftover unshared blocks in the outer crescents (one extra `2` on the Left for $48$, and one extra `3` on the Right for $72$). Multiplying **all blocks across all three regions** (Left $\times$ Center $\times$ Right) gives the Least Common Multiple:
$$\text{LCM} = 2 \times 24 \times 3 = 16 \times 9 = \mathbf{144}$$

{{blocks:prime_lcm_gcd_venn|Prime Factor Studio: Prime Factorization and Venn Intersection Model}}

Why do musicians, astronomers, and harbor engineers use both `{{key:GCF}}` and `{{key:LCM}}`? Because **GCF** finds the largest shared building block that fits evenly inside two rhythms, while **LCM** finds the exact moment two different cycles line back up at the start. In an electronic music studio, suppose a drummer records a **$16\text{-beat}$ drum loop** ($16 = 2^4$) while a bassist records a **$20\text{-beat}$ synth bassline** ($20 = 2^2 \times 5$). Keying `16 {{key:ENTER}} 20 {{key:GCF}}` gives **`4`**, showing that both loops are built from **$4\text{-beat}$ measures** ($4$ measures in the drum loop, $5$ measures in the bassline), while keying `16 {{key:ENTER}} 20 {{key:LCM}}` gives **`80`**, proving that both loops hit their opening downbeat together every **$80$ beats** ($5$ drum loops $= 4$ bass loops). Out at a harbor entrance after dark, a ship's navigator uses that same cycle math to track navigation lights: when a green lighthouse beacon flashes every **$15\text{ seconds}$** ($3 \times 5$) and a red channel buoy flashes every **$25\text{ seconds}$** ($5^2$), keying `15 {{key:ENTER}} 25 {{key:LCM}}` $\to \mathbf{75}$ reveals that if both lights flash together right now, they will flash at the exact same instant every **$75\text{ seconds}$** ($1\text{ minute } 15\text{ seconds}$).

---

### Why GCF × LCM Equals First × Second
Look back at the two-circle Venn diagram you built for $48$ and $72$. When we found the **GCF** ($24$), we multiplied the shared prime blocks in the center overlap. When we found the **LCM** ($144$), we multiplied the left crescent, the center overlap, and the right crescent. Notice that if you multiply **$\text{GCF} \times \text{LCM}$**, the center overlap gets counted *twice*—which uses the exact same collection of prime blocks as multiplying the two original numbers together!
$$\text{GCF} \times \text{LCM} = \text{First Number} \times \text{Second Number}$$

Test the Secret Partner Rule on **$24$** and **$36$**: their Greatest Common Factor is $12$ (`24 {{key:ENTER}} 36 {{key:GCF}}`) and their Least Common Multiple is $72$ (`24 {{key:ENTER}} 36 {{key:LCM}}`). Multiplying $12 \times 72 = \mathbf{864}$ matches multiplying the two starting numbers directly with `{{res:sc6_07_data_probability_primes_seq_74:keys}}` $\to X = \mathbf{864.00}$!

Even better, because the SC-6 has four stack shelves, you can chain Chapter 5's **$18$-tooth and $24$-tooth** partner check in a single continuous sequence without writing down the GCF in between (and if you ever want to inspect every shared factor of two gear wheels at once, the shifted common-factors key `{{key:C.FAC}}` lists them on the screen). Chaining both keys on the stack with `{{res:sc6_07_data_probability_primes_seq_16:keys}}` holds the GCF ($6$) on Shelf $Z$ while finding the LCM ($72$), then multiplies them to land on **`{{res:sc6_07_data_probability_primes_seq_16:value}}`** ($18 \times 24 = 432$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `18` | $0.0000$ | $0.0000$ | $0.0000$ | $18.0000$ | Type the first gear tooth count (18) onto Shelf $X$ |
| `{{key:ENTER}}` | $0.0000$ | $0.0000$ | $18.0000$ | $18.0000$ | Copy 18 up onto Shelf $Y$ |
| `24` | $0.0000$ | $0.0000$ | $18.0000$ | $24.0000$ | Type the second gear tooth count (24) onto Shelf $X$ |
| `{{key:GCF}}` | $0.0000$ | $0.0000$ | $0.0000$ | $6.0000$ | Find the Greatest Common Factor of 18 and 24 ($6$) |
| `18` | $0.0000$ | $0.0000$ | $6.0000$ | $18.0000$ | Type the first number 18; the GCF ($6$) lifts to Shelf $Y$ |
| `{{key:ENTER}}` | $0.0000$ | $6.0000$ | $18.0000$ | $18.0000$ | Copy 18 onto Shelf $Y$ while 6 waits on Shelf $Z$ |
| `24` | $0.0000$ | $6.0000$ | $18.0000$ | $24.0000$ | Type the second number 24 onto Shelf $X$ |
| `{{key:LCM}}` | $0.0000$ | $0.0000$ | $6.0000$ | $72.0000$ | Find the Least Common Multiple of 18 and 24 ($72$); 6 drops to $Y$ |
| `{{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $432.0000$ | Multiply GCF by LCM ($6 \times 72 = 432$) |

The Secret Partner Rule matches on the nose ($6 \times 72 = 432$, and $18 \times 24 = 432$)! *(Pro tip: Since `{{key:GCF}}` saves `24` inside `{{key:LASTX}}`, you can make this even shorter by using `18 {{key:LASTX}} {{key:LCM}}` instead of typing `24` again.)*

---

### Tiling a Hallway with the Remainder Ladder
How does the SC-6 find the Greatest Common Factor of two huge numbers without testing hundreds of prime factors? Over 2,300 years ago, Euclid of Alexandria discovered a visual shortcut (`{{key:÷R}}`). You can see *why* it works by **tiling a rectangular hallway with the largest possible square floor tiles**:

Imagine a rectangular hallway that is **$105\text{ cm}$ long** and **$45\text{ cm}$ wide**. We want to find the largest square tile that covers the whole hallway evenly:
1. First, lay down big **$45\text{ cm} \times 45\text{ cm}$ squares** along the $105\text{ cm}$ hallway. Two of those $45\text{ cm}$ squares fit side by side ($2 \times 45 = 90\text{ cm}$), leaving an unfilled rectangular gap at the end that measures **$45\text{ cm}$ by $15\text{ cm}$** (because $105 \div 45 = 2$ with a **remainder of $15$**).
2. Any square tile that covers the whole hallway *must also* fit evenly inside that leftover **$45\text{ cm} \times 15\text{ cm}$** gap.
3. Now fill the $45\text{ cm} \times 15\text{ cm}$ gap with **$15\text{ cm} \times 15\text{ cm}$ squares**. Three $15\text{ cm}$ squares fit with **remainder $0$** ($45 \div 15 = 3$, remainder $0$). Because $15\text{ cm}$ squares tile the gap with zero leftover space, they also tile the $45\text{ cm}$ squares—and the entire $105\text{ cm} \times 45\text{ cm}$ hallway ($\text{GCF of } 105\text{ and } 45 = \mathbf{15}$).

$$\text{GCF of Big and Small} = \text{GCF of Small and Remainder}$$

On the SC-6, you can run this remainder ladder on any pair of numbers using the shifted key `{{key:÷R}}`. Each press of `{{key:÷R}}` divides $Y$ by $X$, putting the whole-number quotient in $X$, the leftover remainder in $Y$, and the divisor inside `{{key:LASTX}}`.

Watch the full remainder ladder in action on a larger stone courtyard measuring **$252\text{ cm}$ by $105\text{ cm}$**, playing the leftover game until the remainder hits zero:

First, divide $252$ by $105$ and look at the leftover: **$42$** (because two $105\text{ cm}$ squares take up $210\text{ cm}$, leaving a $42\text{ cm}$ strip). Since $42$ isn't zero yet, we divide $105$ by that $42$ leftover—which leaves a smaller strip of **$21$**. Finally, we divide $42$ by that $21$ leftover, and out pops $2$ with **$0$ leftover**. The last leftover before zero is **$21$**, so a **$21\text{ cm} \times 21\text{ cm}$** square stone tiles the whole courtyard.

| Step / Key | Dividend (Y) | Divisor (X) | Quotient (X) | Remainder (Y) |
| :--- | :--- | :--- | :--- | :--- |
| 252 `{{key:ENTER}}` 105 | 252 | 105 | - | - |
| `{{key:÷R}}` | - | - | 2 | 42 |
| `{{key:x⇄y}}` | 2 | 42 | 42 | 2 |
| `{{key:LASTX}}` `{{key:x⇄y}}` | 105 | 42 | - | - |
| `{{key:÷R}}` | - | - | 2 | 21 |
| `{{key:x⇄y}}` `{{key:LASTX}}` `{{key:x⇄y}}` | 42 | 21 | - | - |
| `{{key:÷R}}` | - | - | 2 | 0 |

> **Why the `{{key:x⇄y}} {{key:LASTX}} {{key:x⇄y}}` Dance Works Like Magic:** Why didn't we have to type `105` or `42` a second time in the table above? Every time you press `{{key:÷R}}`, the leftover remainder lands in $Y$, while the number you just divided by gets saved inside `{{key:LASTX}}`.
>
> Tapping `{{key:x⇄y}}` brings the leftover down to $X$. Next, tapping `{{key:LASTX}}` pulls the old divisor back out, and one more `{{key:x⇄y}}` puts them in the right order (`Old Divisor` in $Y$, `Leftover` in $X$) so you can press `{{key:÷R}}` again!

You can also check that entire courtyard remainder ladder in a single tap using the GCF key `{{res:sc6_07_data_probability_primes_seq_75:keys}}` to land directly on $X = \mathbf{21.00}$.

---

## Averages, Medians & Data Spread

What happens when a scientist, nurse, basketball coach, or game designer collects a whole notebook full of numbers? Looking at a jumble of 20 or 30 raw measurements can make anyone's head spin—until you organize them. In 1858, **Florence Nightingale (1820–1910)** showed the world that she wasn't just a pioneer nurse—she was also one of history's greatest **data detectives**. By carefully recording hospital numbers and turning raw tables into clear averages and colorful circular "rose diagrams," she proved to lawmakers that clean water and fresh air saved thousands of lives.

Your SC-6 gives you the exact same **Data Detective skills** with two families of tools for taming any list of numbers:
1. **Finding the Center (`{{key:x̄}}`, `{{key:MED}}`, `{{key:MODE}}`):** What single "typical" number best describes the middle of the group?
2. **Measuring the Spread (`{{key:RNG}}`, `{{key:IQR}}`, `{{key:MAD}}`):** Are all the numbers huddled tightly together, or are they scattered all over the map?

### Picturing Mean, Median & Spread
Before touching a single data key (`{{key:x̄}}`, `{{key:MED}}`, or `{{key:MAD}}`), picture what each measure looks like in the real world.

**Fair-Share Tower Leveling (`{{key:x̄}}` Mean):** In a nesting-box check, four baby bluebirds weigh $24\text{ g}, 26\text{ g}, 25\text{ g},$ and $29\text{ g}$. Build four **Counting Tile** towers of heights $4, 6, 5,$ and $9$ above a $20\text{-gram}$ baseline. Now move tiles from the tallest tower ($9$) to the shorter towers until **every tower stands at the exact same height**—all four level out at **$6$ tiles** ($26\text{ g}$). Tapping `{{key:CLΣ}} 24 {{key:Σ+}} 26 {{key:Σ+}} 25 {{key:Σ+}} 29 {{key:Σ+}} {{key:x̄}}` does that exact fair-share leveling in your running-total basket ($\text{Mean} = \mathbf{26\text{ g}}$).

**The Middle Kid in the Height Lineup (`{{key:MED}}` Median):** Imagine lining up your friends from shortest to tallest for a team photo. The **Median** (`{{key:MED}}`) is simply the person standing right in the **exact middle** of the line. Even if a 7-foot pro basketball center joins the tall end of the line, the middle person's height barely budges—which is why data detectives rely on the median whenever one extreme outlier would pull the mean off balance.

**Fencing the Middle Half (`{{key:IQR}}` Interquartile Range):** Split that shortest-to-tallest lineup into four equal quarters. The middle two quarters ($25\%$ mark to $75\%$ mark) hold the **middle half of the players**. The distance between the lower quarter mark (`{{key:1Q}}`) and the upper quarter mark (`{{key:3Q}}`) is the **Interquartile Range (`{{key:IQR}}`)**—a sturdy fence around the main group that ignores extreme stragglers at both ends.

**How Far Trials Wander from the Average (`{{key:MAD}}` Mean Absolute Deviation):** In a bird-puzzle lab, **Raven A** solves 4 puzzle boxes in **`8, 9, 9, 10` seconds**, while **Crow B** solves them in **`6, 8, 10, 12` seconds**. Both birds have the *exact same mean* ($9.0\text{ s}$). When you measure how far each try wanders from $9$, Raven A's distances are $1, 0, 0, 1$ (`{{key:MAD}}` $= \mathbf{0.5\text{ s}}$, super consistent), whereas Crow B's distances are $3, 1, 1, 3$ (`{{key:MAD}}` $= \mathbf{2.0\text{ s}}$, four times more spread out):

| Data Measure | Key / Shift | Kid-Friendly Word Rule |
| :--- | :--- | :--- |
| **Total Count (`N`)** | `{{key:N}}` | How many numbers are in your data list |
| **Total Sum (`Σx`)** | `{{key:Σx}}` | All the numbers added together |
| **Mean (Average)** | `{{key:x̄}}` | $\text{Total Sum} \div \text{How Many Numbers}$ |
| **Median** | `{{key:MED}}` | Middle number when lined up from smallest to largest |
| **Mode** | `{{key:MODE}}` | Number that shows up the most times |
| **Range** | `{{key:RNG}}` | $\text{Biggest Number} - \text{Smallest Number}$ |
| **Interquartile Range (IQR)** | `{{key:IQR}}` | $\text{Third Quartile (3Q)} - \text{First Quartile (1Q)}$ |
| **Mean Absolute Deviation (MAD)** | `{{key:MAD}}` | Average distance each number wanders from the Mean |

Let's watch the fair-share **Mean (`{{key:x̄}}`)** and middle **Median (`{{key:MED}}`)** in action on two tournament datasets. First, in a four-round free-throw basketball shootout, you score `88`, `92`, `79`, and `95` points (so the sample count is $n = 4$). What is your fair-share average (`{{key:x̄}}`)?

Mark 88, 92, 79, and 95 with four Counting Tiles on a desk number line. Notice how the two scores above $88.5$ ($+3.5$ and $+6.5$, totaling $+10$) balance the two scores below $88.5$ ($-0.5$ and $-9.5$, totaling $-10$). Tossing all four rounds into your `{{key:Σ+}}` running-total basket (where the sample count is $n = 4$) and tapping `{{key:x̄}}` via `{{res:sc6_07_data_probability_primes_seq_19:keys}}` confirms **`{{res:sc6_07_data_probability_primes_seq_19:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | Empty the running-total basket ($\text{Count} = 0, \text{Sum} = 0$) |
| `88` | $0.0000$ | $0.0000$ | $0.0000$ | $88.0000$ | Type the first shootout score (88) onto Shelf $X$ |
| `{{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $1.0000$ | Toss score 1 into the basket ($\text{Count} = 1, \text{Sum} = 88$) |
| `92` | $0.0000$ | $0.0000$ | $0.0000$ | $92.0000$ | Type the second shootout score (92) onto Shelf $X$ |
| `{{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $2.0000$ | Toss score 2 into the basket ($\text{Count} = 2, \text{Sum} = 180$) |
| `79` | $0.0000$ | $0.0000$ | $0.0000$ | $79.0000$ | Type the third shootout score (79) onto Shelf $X$ |
| `{{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $3.0000$ | Toss score 3 into the basket ($\text{Count} = 3, \text{Sum} = 259$) |
| `95` | $0.0000$ | $0.0000$ | $0.0000$ | $95.0000$ | Type the fourth shootout score (95) onto Shelf $X$ |
| `{{key:Σ+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $4.0000$ | Toss score 4 into the basket ($\text{Count} = 4, \text{Sum} = 354$) |
| `{{key:x̄}}` | $0.0000$ | $0.0000$ | $0.0000$ | $88.5$ | Find the fair-share mean ($354 \div 4 = 88.5$) |

Leveling all four shootout towers gives a fair-share mean score of $\mathbf{88.50}$—right at the balance point where the 10 points above average ($92$ and $95$) fill in the 10 points below average ($88$ and $79$).

Second, step outside to the sprint track, where five finalists finish the 100-meter dash in $12.4, 12.8, 13.1, 13.5,$ and $14.0\text{ seconds}$ (sample count is $n = 5$). What is the middle **median** (`{{key:MED}}`) time? Line up five Counting Tiles from fastest to slowest on your desk: the third tile sits right in the middle with two sprinters faster and two slower, pointing straight to $13.1\text{ s}$.

Tossing the five sprint times into your running-total basket and tapping `{{key:MED}}` via `{{res:sc6_07_data_probability_primes_seq_20:keys}}` returns **`{{res:sc6_07_data_probability_primes_seq_20:value}}`**. With $5$ runners counted on Shelf $Y$, the middle runner's time of $\mathbf{13.10\text{ seconds}}$ appears on Shelf $X$.

### The 10-Quiz Score Dot Plot & Frequency Table

Let's see how fast `{{key:Σ+}}` checks a whole classroom list of scores. Across 10 students, a math class records the following scores on a 100-point weekly quiz:
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

Look at the shape of the dot plot above. The scores climb smoothly from $70$ up to a central peak at $85$ (the **Mode**, because $85$ shows up the most times), and then step back down toward $95$.

Now toss all 10 scores into your `{{key:Σ+}}` running-total basket: start with `{{key:CLΣ}}` to empty the basket ($\text{Count} = 0$), then enter `70 {{key:Σ+}}` ($\text{Count} = 1$), `75 {{key:Σ+}}` ($\text{Count} = 2$), `80 {{key:Σ+}} 80 {{key:Σ+}}` ($\text{Count} = 4$), `85 {{key:Σ+}} 85 {{key:Σ+}} 85 {{key:Σ+}}` ($\text{Count} = 7$), `90 {{key:Σ+}} 90 {{key:Σ+}}` ($\text{Count} = 9$), and `95 {{key:Σ+}}` ($\text{Count} = 10$). (If you ever mistype a score, tapping `{{key:Σ-}}` takes it right back out of the basket, while `{{key:FRQ}}` opens the scrollable `FREQ TABLE` showing how many times each score appears in your data list.)

Once all ten quiz papers are in the basket, each data key tells a different part of the classroom story. Tapping `{{key:N}}` confirms that you logged $X = \mathbf{10}$ quizzes in all, while `{{key:Σx}}` adds every point earned across the room into a grand total of $X = \mathbf{835.0}$. When you tap `{{key:MED}}` for the middle student in the lineup and `{{key:MODE}}` for the most common score at the peak of the dot plot, both land right on $X = \mathbf{85.0}$. Meanwhile, tapping `{{key:x̄}}` levels all ten scores into a fair-share **Mean** of $X = \mathbf{83.5}$—sitting just $1.5$ points below the median and mode because that single score of $70$ at the left edge pulls the average slightly downward—and tapping `{{key:RNG}}` measures the full $X = \mathbf{25.0}$ spread from the lowest paper ($70$) to the highest ($95 - 70 = 25$).

---

### How Spread Out Are Five Quiz Scores?

Now let's zoom in on a 5-student study group with scores of $85, 90, 75, 90, 100$ (where the sample count is $n = 5$) so you can see how `{{key:IQR}}` and `{{key:MAD}}` measure spread. When you load all five scores into your running-total basket with `{{key:CLΣ}} 85 {{key:Σ+}} 90 {{key:Σ+}} 75 {{key:Σ+}} 90 {{key:Σ+}} 100 {{key:Σ+}}` and sort them from lowest to highest ($75, 85, 90, 90, 100$), they span from a minimum of $\mathbf{75.0}$ to a maximum of $\mathbf{100.0}$ (a total range of $100 - 75 = \mathbf{25.0}$). Tapping `{{key:Σx}}` adds the five papers to $\mathbf{440.00}$, so the fair-share **Mean** (`{{key:x̄}}`) is $440 \div 5 = \mathbf{88.00}$, while both the middle **Median** (`{{key:MED}}`, the 3rd score out of 5) and the most frequent **Mode** (`{{key:MODE}}`) sit at $\mathbf{90.00}$.

To see how tightly the study group is clustered without being fooled by the single $75$ or $100$ at the ends, tap `{{key:IQR}}` for the **Interquartile Range**. With $5$ sorted scores ($75, 85, \mathbf{90}, 90, 100$), the SC-6 splits the odd-sized list into two inclusive halves that both include the middle median ($90$): the lower half ($75, \mathbf{85}, 90$) and the upper half ($90, \mathbf{90}, 100$). On the SC-6, the **First Quartile (1Q)** is the median of the lower half, $\mathbf{85.0}$, and the **Third Quartile (3Q)** is the median of the upper half, $\mathbf{90.0}$, fencing off the middle half of the group inside a $5\text{-point}$ window:
$$\text{Interquartile Range (IQR)} = \text{Third Quartile (3Q)} - \text{First Quartile (1Q)} = 90.0 - 85.0 = \mathbf{5.00}$$

Next, tap `{{key:MAD}}` to find the **Mean Absolute Deviation**—the average distance each student's score wanders from the group mean of $88.0$. Measuring how far each of the five scores ($75, 85, 90, 90, 100$) sits from $88$ gives distances of $13, 3, 2, 2,$ and $12$. Adding those five distances together ($13 + 3 + 2 + 2 + 12 = 32.0$) and dividing by the $5$ students reveals that a typical score in the study group sits $\mathbf{6.40\text{ points}}$ away from the mean:
$$\text{Mean Absolute Deviation (MAD)} = \text{Total Distance from the Mean} \div \text{How Many Numbers} = 32.0 \div 5 = \mathbf{6.40}$$

### Five-Number Box Plots & Spotting Wild Outliers
When data detectives draw a **Box-and-Whisker Plot**, they line up all the numbers from smallest to largest and mark five milestones—the **Minimum (`MIN`)**, **First Quartile (`1Q`)**, **Median (`MED`)**, **Third Quartile (`3Q`)**, and **Maximum (`MAX`)**—that slice the entire sorted list into four equal quarters ($25\%$ of the data in each quarter) around a central box of width **`IQR`**:

| Box Plot Milestone | Statistical Keycap | What It Shows on the Box Plot |
| :--- | :--- | :--- |
| **Lower Whisker Tip (`MIN`)** | `{{key:MIN}}` | Smallest number ($0\%$ mark) |
| **Left Box Edge — First Quartile (`1Q`)** | `{{key:1Q}}` | Lower quarter mark ($25\%$ boundary of the center box) |
| **Center Line — Median (`MED`)** | `{{key:MED}}` | Halfway mark ($50\%$ median line inside the box) |
| **Right Box Edge — Third Quartile (`3Q`)** | `{{key:3Q}}` | Upper quarter mark ($75\%$ boundary of the center box) |
| **Center Box Width (`IQR`)** | `{{key:IQR}}` | $\text{Third Quartile (3Q)} - \text{First Quartile (1Q)}$ |
| **Upper Whisker Tip (`MAX`)** | `{{key:MAX}}` | Biggest number ($100\%$ mark) |

How do scientists decide whether an unusual number is just a little high or a true **outlier** that wandered far away from the pack? They use the **$1.5 \times \text{IQR}$ Outlier Fence Rule**: measure the width of the center box (`{{key:IQR}}`), multiply it by $1.5$, and build an invisible "fence" $1.5$ box-widths below the First Quartile and above the Third Quartile:
$$\text{Lower Fence} = \text{First Quartile (1Q)} - (1.5 \times \text{IQR})$$
$$\text{Upper Fence} = \text{Third Quartile (3Q)} + (1.5 \times \text{IQR})$$
Any number that jumps past either fence is officially flagged as an outlier.

Let's see that outlier fence in action on a real cross-country race. Eight runners finish a 5K race in the following times (in minutes): $25, 28, 30, 32, 34, 35, 38, 58$. Runner 8 stopped to tie a shoelace and took $58\text{ minutes}$. Does $58$ jump past the upper outlier fence?

When you line up those eight finish times in order ($25, 28, 30, 32, 34, 35, 38, 58$), the halfway **Median (`MED`)** sits right between the fourth and fifth runners at $(32 + 34) \div 2 = \mathbf{33.0\text{ minutes}}$. Splitting the faster four runners ($25, 28, 30, 32$) in half places the **First Quartile (`1Q`)** at $(28 + 30) \div 2 = \mathbf{29.0\text{ minutes}}$, while splitting the slower four runners ($34, 35, 38, 58$) in half places the **Third Quartile (`3Q`)** at $(35 + 38) \div 2 = \mathbf{36.5\text{ minutes}}$—giving the center box an **Interquartile Range (`IQR`)** of $36.5 - 29.0 = \mathbf{7.5\text{ minutes}}$.

Now build the upper outlier fence on the stack. Multiplying the $7.5\text{-minute}$ box width by $1.5$ via `{{res:sc6_07_data_probability_primes_seq_76:keys}}` gives a fence margin of $11.25\text{ minutes}$. Adding that margin to the Third Quartile with `36.5 {{key:+}}` places the upper fence at $\mathbf{47.75\text{ minutes}}$. Since $58$ is greater than $47.75$, the time of 58 minutes sits well past the upper fence and is a **true outlier**.

---

## Negative Numbers, Zero Pairs & Distance from Zero

Up to now, most of your math has stayed at zero or above. Now you get to cross zero into a brand-new territory. Picture a long horizontal number line with **`0`** standing right at the center origin: stepping right (or climbing up) carries you into **positive numbers ($+$)** (`+1, +2, +3, +4, +5`), while stepping left (or diving down) carries you an equal distance into **negative numbers ($-$)** (`-1, -2, -3, -4, -5`). Every number has both a **size** (how many steps from zero) and a **direction** (which side of zero it sits on).

### Hot-Air Balloons & Two-Color Zero Pairs
To make adding, subtracting, and multiplying negative numbers crystal clear with the flip-sign key (`{{key:+/-}}`), picture a **hot-air balloon** floating at height $0$ (sea level) alongside your **Two-Color Counters**. Each **Yellow Counter ($+1$)** acts like a puff of hot air that lifts the balloon **up $+1\text{ meter}$**, while each **Crimson Counter ($-1$)** acts like a heavy sandbag hooked onto the basket that pulls the balloon **down $-1\text{ meter}$**.

When one $+1$ puff of hot air and one $-1$ sandbag meet, they form a **Zero Pair ($+1 + (-1) = 0$)** and balance each other out completely, keeping the balloon at the exact same height. If you lay down **5 Crimson counters (`-5`)** and **3 Yellow counters (`+3`)** side by side, 3 Yellow-Crimson Zero Pairs cancel out, leaving **2 Crimson counters (`-2`)**—proving right on the table why `{{res:sc6_07_data_probability_primes_seq_66:keys}}` equals **`-2`**.

What happens if your balloon is floating at $+7\text{ meters}$ and you **subtract (toss overboard) $3$ heavy sandbags** ($7 - (-3) = 10$, or a friend cancels a $\$3$ debt you owed them)? With $3$ fewer sandbags pulling it down, the balloon rises **up $+3\text{ meters}$** to $+10$! Taking away a negative weight does the exact same thing as adding a positive boost—and keying `{{res:sc6_07_data_probability_primes_seq_81:keys}}` on your SC-6 confirms **`10`**. By the same token, if adding $3$ groups of $2$ Crimson sandbags ($+3 \times -2 = -6$) pulls the balloon down $6\text{ meters}$, then **removing ($-3$ groups of) $2$ Crimson sandbags** (`-3 × -2`) lifts $6$ sandbags *off* the basket, sending the balloon rising to **`+6`** (`{{res:sc6_07_data_probability_primes_seq_67:keys}}` $\longrightarrow$ **`6`**).

On the SC-6, look at the difference between the two keys that have a minus sign: the **subtraction key** (`{{key:-}}`) works between two shelves by subtracting $X$ from $Y$ ($Y - X$), whereas the **change-sign key** (`{{key:+/-}}`) flips the sign of the single number currently sitting in $X$ (turning positive `8` into negative `-8`, or `-8` back into `+8`). Because default **Whole Number Mode (`{{key:NUM}}`)** keeps stack numbers at `0` or above, toggle `{{key:NUM}}` off first (or tap `{{key:ALL}}` / `{{key:FIX}}`) whenever you want to work with negative numbers in stack view: then type `8 {{key:+/-}}` so the screen displays `-8`, and pressing `{{key:+/-}}` a second time flips `-8` right back to `8`.

Imagine checking an outdoor thermometer in Minnesota on a frosty morning: at 6:00 AM, it reads $-12^\circ\text{C}$ ($12$ degrees below freezing). By 2:00 PM, the afternoon sun warms the air up by $+15^\circ\text{C}$. What is the afternoon temperature?

$$\text{Temperature Change: } -12 + 15 = +3^\circ\text{C}$$

Picture 12 Crimson cold tokens meeting 15 Yellow warm tokens: 12 Zero Pairs cancel out to bring the thermometer right up to $0^\circ\text{C}$, and the remaining 3 Yellow tokens push it to $+3^\circ\text{C}$ so the icicles start dripping! On the stack, key `12 {{key:+/-}} {{key:ENTER}} 15 {{key:+}}` $\to \mathbf{3}$, showing $+3^\circ\text{C}$ right on the screen.

What happens when *both* numbers pull in the negative direction—for instance, if you hook $15$ sandbags ($-15$) onto a balloon basket, and then hook on $28$ *more* sandbags ($-28$)? Model a smaller version with Crimson counters first ($-3 + (-5) = -8$ Crimson tokens): because both groups pull downward, there are zero Yellow tokens to cancel them out. Combining the two negative movements on the stack with `{{res:sc6_07_data_probability_primes_seq_27:keys}}` gives **`{{res:sc6_07_data_probability_primes_seq_27:value}}`**, as the two downward pulls team up to reach **$-43$**.

Now compare that with subtracting a bigger positive number from a smaller one. When your bank account has $\$45$ (45 Yellow $+1$ tokens) and you spend $\$70$, where does your balance land? The first $\$45$ wipes out all 45 Yellow tokens down to $\$0$, and the remaining $\$25$ pulls you 25 steps below zero into Crimson debt ($-25$). Finding $45 - 70$ on the SC-6 with `{{res:sc6_07_data_probability_primes_seq_28:keys}}` gives **`{{res:sc6_07_data_probability_primes_seq_28:value}}`** (**$-\$25$**).

---

### Distance from Zero with Absolute Value
If your friend walks $5\text{ steps}$ east ($+5$) and you walk $5\text{ steps}$ west ($-5$), who walked farther from the starting line? You both walked the exact same distance: **$5\text{ steps}$** (`{{key:|x|}}`).

The **absolute value** of a number, written $|x|$, is simply its **distance from zero** on the number line—and whether you walk left or right, distance is always positive:
$$\text{Absolute Value } (|x|) = \text{Distance from } 0 \text{ on the Number Line (Always Positive!)}$$

On the SC-6, pressing the shifted absolute-value key `{{key:|x|}}` (`{{key:g}}` + `{{key:+/-}}`) strips away any negative sign from $X$, leaving its positive distance from zero—so keying `42 {{key:+/-}} {{key:|x|}}` displays **`42`**, while keying `15 {{key:|x|}}` keeps **`15`** unchanged.

To see why absolute value is so handy when crossing sea level, picture a desert hiker starting at the bottom of Badwater Basin in Death Valley at $-86\text{ meters}$ ($86\text{ m}$ below sea level) and climbing all the way to the top of Telescope Peak at $+3,366\text{ meters}$ above sea level. First the hiker climbs $86\text{ meters}$ just to reach sea level ($0\text{ m}$), and then climbs another $3,366\text{ meters}$ to the peak.

$$\text{Vertical Climb: } |3366 - (-86)| = |3366 + 86| = 3,452\text{ meters}$$

Subtract the negative starting height from the peak height and take the absolute value via `3366 {{key:ENTER}} 86 {{key:+/-}} {{key:-}} {{key:|x|}}`. The screen shows a total climb of $\mathbf{3,452.00\text{ meters}}$.

The same rule works whenever a bird dives into the ocean or a snowplow salts an icy road. When a diving Northern Gannet plunges from $+32\text{ m}$ in the sky to $-14\text{ m}$ underwater to catch a fish, its total dive distance across $0\text{ m}$ sea level is $|32| + |-14| = \mathbf{46\text{ m}}$ (`32 {{key:|x|}} {{key:ENTER}} 14 {{key:+/-}} {{key:|x|}} {{key:+}}`). And in winter, spreading rock salt lowers water's freezing point from $0^\circ\text{C}$ by $-14.5^\circ\text{C}$, while adding beet juice lowers it another $-6.75^\circ\text{C}$: keying `0 {{key:ENTER}} 14.5 {{key:-}} 6.75 {{key:-}}` shows that snowplows keep roads ice-free down to **$-21.25^\circ\text{C}$**.

---

### Unmasking Mystery Numbers by Working Backwards
Your counting tiles and four-shelf stack also make it easy to build multi-step word rules forward—and then unwind them in reverse to unmask a hidden starting number. Suppose you are playing a backyard beanbag toss where landing in the center bullseye awards $10\text{ points}$ and landing in the outer ring awards $3\text{ points}$:
$$\text{Total Points} = (10 \times \text{Bullseyes}) + (3 \times \text{Outer Rings})$$
When you land $7$ bullseyes and $4$ outer rings, the 4-shelf stack computes both groups and merges them in one smooth sequence: `10 {{key:ENTER}} 7 {{key:×}} 3 {{key:ENTER}} 4 {{key:×}} {{key:+}}` $\longrightarrow \mathbf{82\text{ points}}$.

Now flip the puzzle around: what if a friend picks a secret Mystery Number, multiplies it by $3$, and subtracts $5$ to end up at $16$? To unmask their secret number, you simply undo each step in reverse order on your stack (`16 {{key:ENTER}} 5 {{key:+}} 3 {{key:÷}}`). Adding $+5$ first undoes the $-5$ (`16 {{key:ENTER}} 5 {{key:+}}` $\to 21$), and dividing by $3$ (`3 {{key:÷}}`) undoes multiplying by $3$ to reveal **$\mathbf{7}$**. That same reverse-order detective work unlocks geometry mysteries too: in Chapter 6, you saw how squaring (`{{key:x²}}`) turns a side length into a square's area, while the square root key (`{{key:√x}}`) runs that rule backward ($\text{Side} = \sqrt{\text{Square Area}}$). Out on a ranch, if a square horse pasture covers $1,225\text{ m}^2$, taking the square root with `1225 {{key:√x}}` unmasks a side length of $35.00\text{ meters}$, and multiplying by 4 sides (`4 {{key:×}}`) shows you need $\mathbf{140.00\text{ meters}}$ of fence. Next, let's take those forward-and-backward steps below sea level to track an elevator and a deep-sea submarine in motion.

### Diving Below Sea Level with Submersible *Alvin*
You can follow negative numbers in motion across skyscrapers, deep-sea trenches, and bank accounts right on the stack.

First, picture a skyscraper with 3 underground parking levels (Floors $-3, -2, -1$), a ground lobby (Floor $0$), and 60 tower floors (Floors $1 \dots 60$). An elevator starts at underground parking Level $-3$, rides up $+45$ floors to deliver boxes, drops $-12$ floors to the cafeteria, and finally drops $-33$ floors:

$$\text{Elevator Journey: } -3 + 45 - 12 - 33 = -3\text{ (Back at parking Level -3)}$$

Keying `3 {{key:+/-}} {{key:ENTER}} 45 {{key:+}} 12 {{key:-}} 33 {{key:-}}` $\to -3$ brings the elevator right back to underground parking Level $-3$.

Next, head out into the ocean aboard the famous **deep-sea research submersible** *Alvin* **(DSV-2)**—the real three-person titanium-sphere submersible operated by the Woods Hole Oceanographic Institution since 1964, which explored the wreck of the *Titanic* on the Atlantic Ocean floor and discovered boiling volcanic hydrothermal vents and giant tube worms in the pitch-black Pacific Ocean.

To survive the crushing weight of miles of ocean water, *Alvin*'s three-person crew rides inside a hollow sphere forged from $5\text{-centimeter-thick}$ titanium, adjusting their depth by pumping seawater in and out of variable-ballast tanks. When *Alvin* is hoisted onto its support ship's A-frame crane at $+4\text{ meters}$ above sea level and lowered down to a canyon ledge at $-180\text{ meters}$ ($180\text{ m}$ below sea level), subtracting the ledge depth from the crane height via `4 {{key:ENTER}} 180 {{key:+/-}} {{key:-}}` reveals a total vertical descent of $184.00\text{ meters}$ ($4 - (-180) = +184\text{ m}$).

From that $-180\text{ m}$ canyon ledge, let's trace *Alvin*'s underwater survey across all four stack shelves: the pilot pumps seawater out of the ballast tanks to rise $+65\text{ m}$ over a deep-water coral ridge, and then vents buoyancy to descend $-40\text{ m}$ into a rocky fissure. Follow *Alvin* along a vertical depth gauge ($-180 \to -115 \to -155$) and chain the moves on your SC-6 with `{{res:sc6_07_data_probability_primes_seq_43:keys}}` to land at **`{{res:sc6_07_data_probability_primes_seq_43:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `180` | $0.0000$ | $0.0000$ | $0.0000$ | $180.0000$ | Type the starting depth number 180 onto Shelf $X$ |
| `{{key:+/-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-180.0000$ | Flip the sign to $-180\text{ m}$ ($180\text{ m}$ below sea level) |
| `{{key:ENTER}}` | $0.0000$ | $0.0000$ | $-180.0000$ | $-180.0000$ | Copy the starting depth $-180\text{ m}$ onto Shelf $Y$ |
| `65` | $0.0000$ | $0.0000$ | $-180.0000$ | $65.0000$ | Type the upward climb ($+65\text{ m}$) onto Shelf $X$ |
| `{{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-115.0000$ | Add the climb ($-180 + 65 = -115\text{ m}$) |
| `40` | $0.0000$ | $0.0000$ | $-115.0000$ | $40.0000$ | Type the canyon dive ($40\text{ m}$); $-115$ lifts to Shelf $Y$ |
| `{{key:-}}` | $0.0000$ | $0.0000$ | $0.0000$ | $-155.0000$ | Subtract the dive ($-115 - 40 = -155\text{ m}$) |

After rising $+65\text{ m}$ over the coral ridge and descending $-40\text{ m}$ into the rocky fissure, *Alvin* hovers at $\mathbf{155\text{ m}}$ below sea level ($-155.00$)—$25\text{ m}$ higher than where its canyon survey began.

Negative numbers also show up whenever you track money. Follow four transactions in a student checking account that starts with $+\$120.00$, using the SC-6 dollar key `{{key:$}}`: suppose you buy school books for $\$85.00$ ($-\$85.00$), buy an art supply kit for $\$60.00$ ($-\$60.00$), get charged a bank overdraft fee of $\$25.00$ ($-\$25.00$), and then deposit a lawn-mowing paycheck of $\$95.00$ ($+\$95.00$). Keying `{{res:sc6_07_data_probability_primes_seq_77:keys}}` subtracts the $\$85.00$ book purchase to leave $35.00$. Next, subtracting `60 {{key:-}}` drops the account below zero to $-25.00$, and subtracting the `25 {{key:-}}` fee reaches $-50.00$. Finally, adding the `95 {{key:+}}` paycheck brings you back up to $+45.00$, and pressing `{{key:$}}` displays your closing balance as **$\$45.00$**. Now let's meet a self-taught mathematician who saw hidden beauty in every whole number he met.

---

### Srinivasa Ramanujan & Taxicab Number 1729

To a true number detective, whole numbers aren't just cold labels on a page—each one has its own personality, prime building blocks, and hidden symmetries. No one in history felt that friendship with numbers more deeply than the self-taught Indian mathematician **Srinivasa Ramanujan** (1887–1920). Growing up in the temple town of Kumbakonam in southern India, young Ramanujan became fascinated by prime numbers, infinite series, and number partitions when he borrowed a single battered library book of math formulas at age 15. Because writing paper was expensive in his family's small home, Ramanujan worked out thousands of original mathematical discoveries on a handheld stone slate rested against his knee, wiping the slate clean with his elbow and copying only his favorite finished gems into frayed notebooks.

When Ramanujan mailed a letter filled with his strange, breathtaking formulas to **G. H. Hardy** at the University of Cambridge in 1913, Hardy took one look and realized these theorems could only have been written by a mathematician of the highest class—inviting the young clerk to sail to England so they could work side by side. A few years later, when Ramanujan fell ill in a London nursing home at Putney, Hardy rode a taxicab across town to visit him. Hoping to start a cheerful conversation, Hardy walked into the room and remarked: *"I rode in taxicab number **1729** today. It seemed to me rather a dull number, and I hope it is not an unfavorable omen."*

Without a second's hesitation, Ramanujan smiled from his bed and replied: *"No, Hardy! It is a very interesting number; it is the smallest number expressible as the sum of two cubes in two different ways!"* Years earlier, while exploring number patterns on his slate in India, Ramanujan had noticed that **`1729`** sits at the exact crossroads of two completely different pairs of 3D cubes—which is why mathematicians ever since have called `1729` the **Hardy–Ramanujan Taxicab Number**.

Grab your SC-6 right now and test Ramanujan's Taxicab Number on your stack in seconds. First, build a $12 \times 12 \times 12$ cube and add a tiny $1 \times 1 \times 1$ unit cube by keying `12 {{key:x³}} 1 {{key:x³}} {{key:+}}`: Shelf $Y$ ($1,728$) and Ground Shelf $X$ ($1$) fuse into **`1729`**. Now test the second way by building a $10 \times 10 \times 10$ thousand-cube and adding a $9 \times 9 \times 9$ cube with `10 {{key:x³}} 9 {{key:x³}} {{key:+}}`: Shelf $Y$ ($1,000$) and Shelf $X$ ($729$) fuse into the exact same number, **`1729`**, while your first `1729` waits right above on Shelf $Y$ so you can see both sums side by side!

While `1729` is still resting on the bottom shelf, tap `{{key:PRIME}}` (`COMPOSITE`) and then press `{{key:FACT}}` to peek inside its prime building blocks. The screen reveals **`7 × 13 × 19`**—three prime numbers spaced in a neat step-by-6 pattern ($7$, plus $6$ is $13$, plus $6$ is $19$) multiplying together to build Ramanujan's favorite taxicab number! Even wilder, try adding the four digits of $1,729$ together on your stack (`1 {{key:ENTER}} 7 {{key:+}} 2 {{key:+}} 9 {{key:+}}`): their sum is **`19`**. Now reverse the digits of `19` to make **`91`**, and multiply them together with `91 {{key:×}}`—and out pops **`1729`** all over again ($19 \times 91 = 1,729$)! Whenever you spot an ordinary-looking number on a license plate, a street sign, or a locker door, tapping `{{key:PRIME}}` and `{{key:FACT}}` lets you explore its hidden personality just like Ramanujan did on his slate.

---

## Dice, Prime & Data Detective Challenges & Looking Ahead

Grab your Polyhedral Dice, Prime Factor Blocks, Counting Tiles, and SC-6 to test these four challenges tonight, and then see how Chapter 8 puts all of your number sense on a 4-second speedrun clock.

### Four Dice, Prime & Data Detective Challenges to Try

1. **The 36-Roll Lucky 7 Tower Race:** Grab two 6-sided dice from your Dice & Spinner Studio and roll them 36 times. After each roll, toss the sum ($2$ through $12$) into `{{key:Σ+}}` on your SC-6 and stack a Counting Tile onto your tabletop bar chart. When all 36 rolls are done, tap `{{key:x̄}}`, `{{key:MED}}`, and `{{key:MODE}}`—did **Lucky 7** build the tallest tower, and how close did your average get to $7.00$?
2. **The Sneaky Impostor Prime Hunt:** Odd numbers like **$91$**, **$119$**, **$133$**, and **$143$** love to disguise themselves as prime numbers because $2, 3,$ and $5$ don't divide into them! Race someone in your family to unmask all four impostors using `{{key:PRIME}}` and `{{key:FACT}}` on your SC-6, then build their secret prime towers on your Prime Factor Studio stage!
3. **The Unbreakable Secret Partner Bet:** Ask a parent or friend to pick *any* two two-digit numbers—say, $36$ and $48$ (`36 {{key:ENTER}} 48 {{key:GCF}}`). Find their `{{key:GCF}}` (`12`), then use `36 {{key:LASTX}} {{key:LCM}}` to find their `{{key:LCM}}` (`144`) without re-typing `48`, and multiply them together (`{{key:×}}` $\to 1,728$). Bet them that $\text{GCF} \times \text{LCM}$ will match the two starting numbers multiplied together ($36 \times 48 = 1,728$) every single time!
4. **The Outlier vs. Median Balance Test:** Measure the length of five pencils or shoes in centimeters and log all five into your running-total basket (`{{key:CLΣ}}` followed by five `{{key:Σ+}}` entries). Check `{{key:x̄}}` and `{{key:MED}}` and write both numbers down. Now add one "giant" imaginary measurement (like `250 {{key:Σ+}}`) and check `{{key:x̄}}` and `{{key:MED}}` again: watch how the fair-share mean jumps upward toward the giant outlier while the middle median hardly moves at all!

---

### Looking Ahead to Chapter 8

Across more than two thousand years of discovery, the greatest breakthroughs in number theory, probability, and statistics all began when curious thinkers looked for the hidden structure inside everyday puzzles. When Eratosthenes of Cyrene sifted prime numbers on a parchment grid in Alexandria, and when Euclid tiled rectangular floors with smaller and smaller squares until the leftover gap disappeared (`105 {{key:ENTER}} 45 {{key:÷R}}` $\to$ Quotient `2` on Shelf $X$ and Remainder `15` on Shelf $Y$), they proved that whole numbers are built from unbreakable prime blocks—turning a mystery number like `2,639` into **`7 × 13 × 29`** with a single tap of `{{key:FACT}}`. And when you stack your physical **Prime Factor Blocks** on the comparator stage and run `24 {{key:ENTER}} 36 {{key:GCF}} 24 {{key:LASTX}} {{key:LCM}} {{key:×}}` on your SC-6, you can see with your own eyes why the Greatest Common Factor ($12$) and the Least Common Multiple ($72$) are secret partners whose product ($12 \times 72 = 864$) always matches the two starting numbers multiplied together ($24 \times 36 = 864$).

That same search for hidden balance connects Galileo Galilei's 1620 dice tables, Blaise Pascal's games of chance, and Florence Nightingale's pioneering hospital charts. A single roll of a volume-equalized six-sided die (`{{key:🎲}}`) is unpredictable on its own, yet across 36 pairs of two dice, six different number pairs converge on the center peak of **Lucky 7**. Better still, your calculator's running-total basket (`{{key:Σ+}}`) lets you level out uneven towers into a fair-share average (`{{key:x̄}}`), line up data from smallest to largest to spot the middle value (`{{key:MED}}`) and most frequent score (`{{key:MODE}}`), fence off wild outliers, and dive below sea level with the submersible *Alvin* using signed numbers (`{{key:+/-}}`) and absolute distance from zero (`{{key:|x|}}`):

| Number & Data Detective Tool | Hands-On Studio Model | Key Stack Move on Your SC-6 |
| :--- | :--- | :--- |
| **Fair Dice & Random Trials (`{{key:🎲}}`)** | Volume-equalized $d6$ dice & 10-slice spinner | Roll `{{key:🎲}}` or custom ranges `{{key:1…x}}` and `{{key:t…x}}` |
| **Prime & Factor Towers (`{{key:PRIME}}`, `{{key:FACT}}`)** | Scaled Prime Factor blocks ($2, 3, 5, 7$) on the stage | Test primality with `{{key:PRIME}}` and peel prime factors with `{{key:FACT}}` |
| **Secret Partner Rule (`{{key:GCF}}`, `{{key:LCM}}`)** | Shared prime blocks vs. tallest prime towers | `24 {{key:ENTER}} 36 {{key:GCF}} 24 {{key:LASTX}} {{key:LCM}} {{key:×}}` $\to \mathbf{864}$ |
| **Center & Spread (`{{key:x̄}}`, `{{key:MED}}`, `{{key:IQR}}`, `{{key:MAD}}`)** | Leveling Counting Tile towers & 5-number box plots | Load data with `{{key:CLΣ}}` $\dots$ `{{key:Σ+}}`, then inspect `{{key:x̄}}`, `{{key:MED}}`, `{{key:IQR}}`, `{{key:MAD}}` |
| **Zero Pairs & Sea-Level Dives (`{{key:+/-}}`, `{{key:|x|}}`)** | Yellow ($+1$) and Crimson ($-1$) two-color counters | Flip signs in place with `{{key:+/-}}` and find distance from $0$ with `{{key:|x|}}` |

In **[Chapter 8: Mental Math Tricks & The Quiz Game](08-math-quiz-engine.md)**, you will take all of that number sense and put your reflexes to the test. You will learn eight lightning-fast mental-math shortcuts—from multiplying two-digit numbers by $11$ in your head to spotting prime and divisibility clues at a glance—and then step into the built-in 4-second Quiz Challenge (`{{key:?}}`) on your SC-6 to light up your five-dot streak meter and race the clock!
