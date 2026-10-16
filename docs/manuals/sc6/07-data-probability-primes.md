---
title: "Discrete Probability, Primes & Pre-Algebra"
description: "Mastering elementary probability, number theory, descriptive statistics, and Grade 6 pre-algebra on the SC-6: dice, prime factors, GCF/LCM, and signed numbers."
---

# Discrete Probability, Primes & Pre-Algebra

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">DATA &amp; NUMBER THEORY // CHAPTER 07</span>
  <span class="te-viewport-status text-emerald-400">● POLYHEDRAL DICE &bull; PRIMES {{key:FACT}} &bull; DESCRIPTIVE STATS &bull; PRE-ALGEBRA</span>
</div>

## Why Do Primes and Probability Matter in the Real World?

You often hear that "prime numbers are numbers that can only be divided by 1 and themselves." That sounds like an arbitrary rule invented to give you boring homework.

In the physical universe, **prime numbers and probability are how living creatures survive predators, how secret codes protect spacecraft, and how games stay fair!**

### The 17-Year Cicada Mystery: How Primes Defeat Predators

Every 13 or 17 years across the deciduous forests of North America, billions of periodical cicadas (*Magicicada*) erupt from the soil on the exact same warm spring weekend, filling the forest canopy with an overwhelming roar.

Biologists wondered for centuries: **Why 13 years? Why 17 years?** Why didn't cicadas evolve a convenient 12-year or 16-year life cycle?

#### The Deadly Composite Trap
Suppose a cicada brood emerged on a 12-year cycle. The number 12 is **composite**: its factors are $1, 2, 3, 4, 6,$ and $12$.
- A predatory bird or parasitic wasp with a 2-year population surge would synchronize with them on every single emergence ($2 \times 6 = 12$).
- A predator with a 3-year boom cycle would meet them every emergence ($3 \times 4 = 12$).
- A predator with a 4-year cycle would feast on them every emergence ($4 \times 3 = 12$).

The cicada population would be devastated by specialized parasites at every generation!

#### The Prime Number Shield
Now look at 17. The number 17 is **prime**: its *only* factors are 1 and 17.
- A 2-year cyclical predator intersects with the cicadas only once every **34 years** ($\text{LCM}(2, 17) = 34$)!
- A 3-year cyclical predator intersects only once every **51 years** ($\text{LCM}(3, 17) = 51$)!
- A 5-year cyclical predator intersects only once every **85 years** ($\text{LCM}(5, 17) = 85$)!

By sleeping underground for an exact prime number of years, cicadas outsmart every predator in the forest! Primes are nature's secret code—the unbreakable atomic building blocks of all numbers.

<div class="admonition note">
<p class="admonition-title">For Parents &amp; Teachers: Number Theory &amp; Biological Optimization</p>
<p>
As Carl Friedrich Gauss proved in his <em>Disquisitiones Arithmeticae</em> {{cite:gauss1809}} and Simon Singh chronicles in the history of number theory {{cite:singh1997}}, the Fundamental Theorem of Arithmetic establishes primes as the irreducible atomic building blocks of all integers. Nature leverages prime cycles to minimize biological overlap between prey and predators.
</p>
</div>

---

### The Polyhedral Dice Maker's Secret: Why There Are Only 5 Perfect Fair Dice

Ever wonder why your favorite tabletop roleplaying games use 4, 6, 8, 12, or 20-sided dice—but nobody sells a 7-sided or 11-sided die?

Over 2,300 years ago, Greek mathematicians proved a staggering geometric fact: in our three-dimensional universe, there are **only five regular convex polyhedra** (the Platonic Solids) where every single face is an identical regular polygon and every vertex meets the exact same number of edges:
1. **Tetrahedron (d4):** 4 equilateral triangular faces
2. **Cube (d6):** 6 square faces
3. **Octahedron (d8):** 8 equilateral triangular faces
4. **Dodecahedron (d12):** 12 regular pentagonal faces
5. **Icosahedron (d20):** 20 equilateral triangular faces

If you try to make a 7-sided or 11-sided die, some sides will always be steeper or flatter than others. It is physically impossible to make them land with equal chance! True fairness in gaming isn't just about giving the dice cup a good shake—it comes from the deep spatial symmetries of the universe.

<div class="admonition note">
<p class="admonition-title">For Parents &amp; Teachers: Probability, Geometry &amp; Heuristics</p>
<p>
In Jordan Ellenberg's <em>How Not to Be Wrong</em> {{cite:ellenberg2014}} and Martin Gardner's classic studies of mathematical games {{cite:gardner1959}}, human intuition consistently misjudges randomness and symmetry. Following David Macaulay's mechanical exposition {{cite:macaulay2016}}, Jerome Bruner's learning progression {{cite:bruner1966}}, and George Pólya's problem-solving strategies {{cite:polya1945}}, students begin with physically balanced dice and concrete counters before transitioning to digital pseudo-random generation on the SC-6.
</p>
</div>

---

<div class="admonition note">
<p class="admonition-title">Chapter Baseline Mode: {{key:NUM}}</p>
<p>
Standard Base-10 Arithmetic &bull; 4-Stack XYZT &bull; Clean Transflective Display<br>
<em>(Visual Dice Sandbox <code>{{key:🎲}}</code> opens interactive probability trials)</em>
</p>
</div>

<div class="admonition note">
<p class="admonition-title">Unlocked Keycaps Ribbon — Grades 5–6 Data &amp; Pre-Algebra Suite</p>
<p>
• <strong>Probability &amp; Randomness:</strong> <code>{{key:🎲}}</code> Polyhedral Dice Sandbox, <code>{{key:1…x}}</code> (Random 1 to X), <code>{{key:t…x}}</code> (Random Y to X).<br>
• <strong>Number Theory Keys:</strong> <code>{{key:PRIME}}</code> Primality Test, <code>{{key:FACT}}</code> Prime Factor Decomposition, <code>{{key:C.FAC}}</code> Common Factors, <code>{{key:GCF}}</code> Greatest Common Factor, <code>{{key:LCM}}</code> Least Common Multiple, <code>y⟌x</code> (Quotient &amp; Remainder).<br>
• <strong>Descriptive Statistics:</strong> <code>{{key:Σ+}}</code> Accumulator, <code>{{key:Σ-}}</code> Correction, <code>{{key:N}}</code> Sample Count, <code>{{key:Σx}}</code> / <code>{{key:Σx}}</code> Sum, <code>{{key:x̄}}</code> Mean $\bar{x}$, <code>{{key:MED}}</code> Median, <code>{{key:MODE}}</code> Mode, <code>{{key:MIN}}</code> Minimum, <code>{{key:MAX}}</code> Maximum, <code>{{key:IQR}}</code> Interquartile Range, <code>{{key:MAD}}</code> Mean Absolute Deviation, <code>{{key:FRQ}}</code> Frequency of X.<br>
• <strong>Grade 6 Pre-Algebra:</strong> <code>{{key:+/-}}</code> Signed Numbers (Zero Pairs), <code>{{key:|x|}}</code> Absolute Value (Number Line Distance), Geometric <code>{{key:x²}}</code> and <code>{{key:√x}}</code> (Area-to-Side Inverses).<br>
<em>Strict Pedagogical Gatekeeping: In accordance with developmental cognitive standards, 5th graders and younger NEVER see logarithms (<code>LOG</code>, <code>LN</code>) or abstract powers (<code>yˣ</code>). Advanced functions are segregated exclusively into secondary advanced math extensions.</em>
</p>
</div>

---

## Concrete Foundations: Two-Color Counters, Polyhedral Dice & The Sieve Grid

Before we tap keys on the calculator, we roll real dice, balance counters, and build number arrays with our hands. When you understand what the numbers look like on your desk, the calculator becomes your ultimate math assistant.


<div class="admonition note">
<p class="admonition-title">Concrete Probability &amp; Number Theory Manipulatives</p>

1. **Precision Dice &amp; Spinner Studio:**
   - **Equal-Volume Pip Algorithm:** $r_n = 1.8 / \sqrt{n}$ for true mechanical balance across all 4 physical $d6$ dice.
   - **Captive Multi-Plate Spinner:** 10-sector decimal lid (`0`–`9`), plus interchangeable biased ($50\%, 25\%, 15\%, 10\%$), binary (`0`/`1`), and arithmetic operations dial plates.
   - **Digital Polyhedral Extension (`{{key:🎲}}`):** The SC-6 hardware probability engine extends physical $d6$ experiments to full polyhedral dice ($d4, d6, d8, d10, d12, d20$).
2. **Counting &amp; Array Studio:**
   - Four high-contrast color groups modeling positive/negative integer Zero Pairs and discrete frequency histograms.
3. **Prime Factor Studio:**
   - Logarithmic prime factor towers ($2, 3, 5, 7$) and bilateral comparator stage.
</div>

{{blocks:dice_spinner_probability|Probability Dice & Spinner Studio: 1x1 spinner enclosure with 10-sector lid, biased and binary dial plates, and 4 volume-equalized fair d6 dice}}

### The Equal-Volume Pip Dice & Spinner Studio
Standard commercial dice often introduce subtle physical bias because face 6 has six excavated pips while face 1 has only one, shifting the center of gravity toward the 1-face and making 6 slightly more likely to land face up. 

The StackCalc ecosystem eliminates this experimental artifact with our 3D-printable **Dice & Spinner Studio**. Pips on the four physical $d6$ dice are engineered using an Equal-Volume Excavation formula:
$$r_n = \frac{1.80\text{ mm}}{\sqrt{n}}$$
where $n$ is the number of pips on the face. On face 1, the single pip has radius $1.80\text{ mm}$; on face 6, each of the six smaller pips has radius $1.80 / \sqrt{6} \approx 0.735\text{ mm}$. The total mass excavated from every single face is mathematically identical to within $0.001\text{ grams}$, ensuring true physical uniformity for classroom probability experiments, while pressing `{{key:🎲}}` on the SC-6 simulates $d4, d6, d8, d10, d12,$ and $d20$ polyhedral rolls!

### Two-Color Integer Counters & Zero Pairs
Before you manipulate signed numbers on the SC-6 keypad, you model integers concretely using two-color tokens:
- **Yellow Token:** Represents $+1$ (a unit gain, a deposit, an upward step).
- **Crimson Token:** Represents $-1$ (a unit loss, a withdrawal, a downward step).
- **The Zero Pair:** Placing 1 Yellow token and 1 Crimson token side-by-side forms a **Zero Pair** ($+1 + (-1) = 0$).

When solving $(-5) + (+3)$, you place 5 Crimson tokens and 3 Yellow tokens on the mat. Pairing 3 Crimson tokens with the 3 Yellow tokens eliminates 3 Zero Pairs, leaving exactly 2 Crimson tokens: $-2$. 

On the SC-6, this translates directly to parenthesis-free RPN stack execution:
`{{res:sc6_07_data_probability_primes_seq_66:keys}}` $\longrightarrow X = \mathbf{-2}$.

<div class="admonition tip">
<p class="admonition-title">Parent's De-Stressing Guide: Why Negative × Negative Is Positive</p>

**The Scenario:** Your 6th grader asks: *"Why is $(-3) \times (-2)$ equal to $+6$? Why aren't two negatives even more negative?"*

**The Conventional Explanation (Confusion):**  
*"Because a negative times a negative is a positive. Just memorize it!"*  
Or: *"Two negatives make a positive in English: 'I don't not want it.'"*  
The child memorizes a grammar trick, but mathematical intuition dies.

**The Spatial $180^\circ$ Rotation Cure:**  
1. **Multiplication is walking along the number line at a steady pace:**
   - $(+3) \times (+2)$: Face Forward ($+$), take 2 steps of size 3 forward $\longrightarrow +6$.
   - $(-3) \times (+2)$: Face Backward ($-$), take 2 steps of size 3 forward $\longrightarrow -6$.
2. **Multiplying by a negative means WALKING IN REVERSE:**
   - $(+3) \times (-2)$: Face Forward ($+$), take 2 steps of size 3 in REVERSE $\longrightarrow -6$.
   - $(-3) \times (-2)$: Face Backward ($-$), take 2 steps of size 3 in REVERSE!  
     When you face backward and walk in reverse, where do you travel?  
     **YOU MOVE FORWARD TOWARD POSITIVE NUMBERS!** $(-3) \times (-2) = +6$!

On the SC-6: Key in `{{res:sc6_07_data_probability_primes_seq_67:keys}}` $\longrightarrow \mathbf{+6}$!  
You watch the sign toggle smoothly on the transflective LCD.
</div>

### The 100-Grid Sieve of Eratosthenes Tray
To discover prime numbers, you use the physical 100-Grid Sieve Tray. The Greek mathematician Eratosthenes of Cyrene (c. 276–194 BC) proved that to find all prime numbers up to $N$, one only needs to cross out composite multiples of primes up to $\sqrt{N}$.

For numbers up to $N = 100$, because $\sqrt{100} = 10$, you only need to test and filter multiples of the four prime numbers less than 10: **2, 3, 5, and 7**!

<div class="admonition note">
<p class="admonition-title">The Sieve of Eratosthenes Up to 100</p>

- **Step 1:** $1$ is a unit (neither prime nor composite) $\longrightarrow$ Filtered immediately.
- **Step 2:** Circle $2$ (Prime) $\longrightarrow$ Cross out all even multiples ($4, 6, 8, 10, \dots$).
- **Step 3:** Circle $3$ (Prime) $\longrightarrow$ Cross out all multiples of 3 ($9, 15, 21, \dots$).
- **Step 4:** Circle $5$ (Prime) $\longrightarrow$ Cross out all multiples of 5 ($25, 35, 55, \dots$).
- **Step 5:** Circle $7$ (Prime) $\longrightarrow$ Cross out all multiples of 7 ($49, 77, 91, \dots$).

**All remaining standing tiles are the 25 PRIMES UNDER 100:**  
$2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97$.
</div>

You verify each standing tile on the SC-6:
- `{{res:sc6_07_data_probability_primes_seq_68:keys}}` $\longrightarrow$ Flashes `PRIME` ($X = 1$).
- `{{res:sc6_07_data_probability_primes_seq_69:keys}}` $\longrightarrow$ Flashes `COMPOSITE` ($X = 0$, $91 = 7 \times 13$).
- The sieve makes it visually obvious why $91$ is composite while $97$ is prime!

---

## Discrete Probability & Random Trials (`{{key:🎲}}`)

Probability quantifies the likelihood of an event occurring, measured on a continuum from $0$ (impossible) to $1$ (certain):
$$P(\text{Event}) = \frac{\text{Number of Favorable Outcomes}}{\text{Total Number of Equally Likely Outcomes}}$$

| Probability $P(E)$ | Qualitative Classification | Classroom Example |
| :--- | :--- | :--- |
| **$0.0$** | Impossible | Rolling a `7` on a standard 6-sided die ($d6$) |
| **$0.5$** | Equally Likely | Flipping Heads or Tails on a fair coin |
| **$1.0$** | Certain | Rolling an integer from `1` to `6` on a standard $d6$ |

### The Classroom Dice Key (`{{key:🎲}}`)
The SC-6 features a primary key `{{key:🎲}}` on Row 0, Col 3 that serves as an interactive probability sandbox:
1. **Interactive Die Roll:** Pressing `{{key:🎲}}` triggers an on-chip uniform pseudorandom number generator, animating a 3-frame rolling shuffle before settling on an integer from $1$ to $6$.
2. **Visual Die Rendering:** The transflective graphic LCD renders a crisp $32 \times 32$ pixel die face centered on the screen with authentic pip configurations.
3. **Automatic Stack Lift:** The rolled integer ($1 \dots 6$) lands directly on the display floor ($X$), smoothly lifting prior stack contents ($X \to Y \to Z \to T$), ready for immediate arithmetic!

| Rolled Value | 32×32 LCD Pip Geometry | Visual Dot Pattern |
| :--- | :--- | :--- |
| `{{key:1}}` | Single center pip | Unit point symmetry |
| `{{key:2}}` | Top-left & bottom-right diagonal pips | Diagonal pair |
| `{{key:3}}` | Top-left, center, & bottom-right pips | Diagonal triad |
| `{{key:4}}` | Four corner pips | $2 \times 2$ square array |
| `{{key:5}}` | Four corner pips + center pip | Quincunx ($4 + 1$) |
| `{{key:6}}` | Two vertical columns of three pips | $2 \times 3$ rectangular array |

### Polyhedral Random Ranges: `{{key:1…x}}` and `{{key:t…x}}`
In science labs and tabletop math games, you often require random numbers beyond a standard 6-sided die:
- **{{key:1…x}} (Random 1 to X):** Generates a discrete uniform integer in $[1, \lfloor X \rfloor]$.
  - Roll a 20-sided die ($d20$): `20 {{key:1…x}}` $\longrightarrow X \in \{1, 2, \dots, 20\}$.
  - Flip a fair coin ($1 = \text{Heads}, 2 = \text{Tails}$): `{{key:2}} {{key:1…x}}` $\longrightarrow X \in \{1, 2\}$.
  - Select a random lab partner from a group of 28: `28 {{key:1…x}}` $\longrightarrow X \in \{1, 2, \dots, 28\}$.
- **{{key:t…x}} (Random Y to X):** Generates a discrete uniform integer in $[\lfloor Y \rfloor, \lfloor X \rfloor]$.
  - Generate a random two-digit number between 10 and 99: `10 {{key:ENTER}} 99 {{key:t…x}}`.

#### Worked Example 7.1: Theoretical vs. Experimental Die Probability
You roll a standard six-sided die 60 times.
1. What is the theoretical probability of rolling a 4 on any single roll?
2. How many times should a 4 theoretically appear in 60 rolls?
3. In an actual trial, you roll a 4 twelve times. Compute the experimental probability and compare it to the theoretical value.

$$\text{Theoretical Probability: } P(4) = \frac{1}{6} \approx 0.1667 \ (16.67\%)$$
$$\text{Expected Frequency: } 60 \times \frac{1}{6} = 10\text{ times}$$

> **RPN Evaluation of Experimental Probability:**
> 12 {{key:ENTER}} 60 {{key:÷}}  -> 0.2000 (20.0%)
>
> Percentage Difference:
> 0.20 {{key:ENTER}} {{key:1}} {{key:ENTER}} {{key:6}} {{key:÷}} {{key:-}}  -> 0.0333 (+3.33% deviation)

---

### Compound Probability: Rolling Two Dice (36 Outcomes)
When two standard dice are rolled simultaneously, the sample space consists of $6 \times 6 = 36$ equally likely ordered pairs $(D_1, D_2)$. The sum $S = D_1 + D_2$ ranges from $2$ to $12$, forming a symmetric triangular probability distribution:

> **TWO-DICE SUM DISTRIBUTION (36 OUTCOMES)**
>
> Sum (S)   Favorable Outcomes (D1, D2)                     Count   Prob P(S)
> -------------------------------------------------------------------------
> 2       (1,1)                                             1      1/36
> 3       (1,2), (2,1)                                      2      2/36
> 4       (1,3), (2,2), (3,1)                               3      3/36
> 5       (1,4), (2,3), (3,2), (4,1)                        4      4/36
> 6       (1,5), (2,4), (3,3), (4,2), (5,1)                 5      5/36
> 7       (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)         6      6/36
> 8       (2,6), (3,5), (4,4), (5,3), (6,2)                 5      5/36
> 9       (3,6), (4,5), (5,4), (6,3)                        4      4/36
> 10       (4,6), (5,5), (6,4)                               3      3/36
> 11       (5,6), (6,5)                                      2      2/36
> 12       (6,6)                                             1      1/36
> -------------------------------------------------------------------------
> Total Possible Outcomes:                                    36     36/36

#### Worked Example 7.2: Probability of Rolling a Lucky 7
Find the exact fractional and decimal probability of rolling a sum of 7 with two dice.

> **Keystrokes:**
> {{key:6}} {{key:ENTER}} 36 {{key:÷}}       -> 0.166667
> {{key:FDISP}}                       -> 1/6 (Simplified mixed/proper display)
The probability is exactly $1/6 \approx \mathbf{16.67\%}$.

### Probability Trees & Sampling Without Replacement
In hands-on probability experiments, you examine multi-stage events where the outcome of the first draw alters the sample space of subsequent draws (dependent probability).

| First Draw Outcome ($8$ Marbles) | Second Draw Outcome ($7$ Remaining) | Combined Branch Probability |
| :--- | :--- | :---: |
| **Red 1st ($5/8$)** | Red 2nd ($4/7$) | $\frac{5}{8} \times \frac{4}{7} = \frac{20}{56}$ |
| **Red 1st ($5/8$)** | Blue 2nd ($3/7$) | $\frac{5}{8} \times \frac{3}{7} = \frac{15}{56}$ |
| **Blue 1st ($3/8$)** | Red 2nd ($5/7$) | $\frac{3}{8} \times \frac{5}{7} = \frac{15}{56}$ |
| **Blue 1st ($3/8$)** | **Blue 2nd ($2/7$)** | $\frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \mathbf{\frac{3}{28}}$ |

#### Worked Example 7.3: Probability of Drawing Two Blue Marbles
You reach into a cloth bag containing 5 Red and 3 Blue marbles and draw two marbles without looking and without replacing the first marble. Find the probability that both marbles are Blue:
$$P(\text{Both Blue}) = P(\text{Blue}_1) \times P(\text{Blue}_2 \mid \text{Blue}_1) = \frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \frac{3}{28}$$

> **RPN Evaluation:**
> {{key:3}} {{key:ENTER}} {{key:8}} {{key:÷}} {{key:2}} {{key:ENTER}} {{key:7}} {{key:÷}} {{key:×}}  -> 0.107143
> {{key:FDISP}}                                       -> 3/28
The probability of drawing two consecutive blue marbles is $3/28 \approx \mathbf{10.71\%}$.

#### Worked Example 7.4: Probability of At Least One Red Marble
Using the complement rule, the probability of drawing *at least one* red marble equals 1 minus the probability of drawing *no* red marbles (both blue):
$$P(\text{At least one Red}) = 1 - P(\text{Both Blue}) = 1 - \frac{3}{28} = \frac{25}{28}$$

> **Keystrokes:**
> {{key:1}} {{key:ENTER}} {{key:3}} {{key:ENTER}} 28 {{key:÷}} {{key:-}}  -> 0.892857
> {{key:FDISP}}                                   -> 25/28
The probability is $\mathbf{25/28} \approx \mathbf{89.29\%}$.

---

## Number Theory: Primes, Factors & The Secret Partner Rule

Number theory explores the structural properties of whole numbers. Prime numbers are the fundamental "atomic elements" of arithmetic; every integer greater than 1 can be uniquely factored into a product of primes (The Fundamental Theorem of Arithmetic).

<div class="admonition note">
<p class="admonition-title">For Parents & Teachers: The CRA Continuum in Elementary Number Theory</p>

| Stage | Modality | Classroom Experience & Manipulatives | SC-6 Calculator Bridge |
| :--- | :--- | :--- | :--- |
| **Concrete** | Physical Manipulatives | • **144-Tile Array Test:** Primes form only $1 \times N$ straight lines; composites form 2D matrices.<br>• **Prime Factor Studio:** Proportional prime towers where stacking prime blocks physically multiplies their values!<br>• Height(2) + Height(3) = Height(6) on the comparator stage! | Physical verification before keystrokes |
| **Representational** | Graphic Sandboxes | • Screen Factor Tree View: exponents and prime dots ($2^3 \times 3^2 \times 5$).<br>• Dual Frame Counter `{{key:▦}}`.<br>• Interactive LCD Sieve: survivor primes highlighted on display. | Transflective LCD dot matrix |
| **Abstract** | RPN Symbolic Engines | • {{key:PRIME}} test pushes 1 (Prime) or 0 (Composite).<br>• `{{key:FACT}}` displays prime factorization string.<br>• {{key:GCF}} and {{key:LCM}} execute Euclidean and Duality engines. | Stack execution ($T, Z, Y, X$) |
</div>

### Station Lesson 7.1: The Rectangular Array Primality Test
- **Your Mission:** Physically investigate primality using the Counting & Array Studio, proving that prime numbers resist 2D rectangular factorization, and verify outcomes on the SC-6 via the dedicated primality key {{key:PRIME}}.
- **Physical Manipulatives:** 144-Tile Four-Color Counting Studio.

| Number Classification | Tile Count | Complete Rectangular Factor Arrays | Positive Divisors |
| :--- | :--- | :--- | :--- |
| **Composite ($N = 12$)** | 12 Tiles | $1 \times 12$, $2 \times 6$, and $3 \times 4$ complete rectangles | `1, 2, 3, 4, 6, 12` (6 factors) |
| **Prime ($N = 13$)** | 13 Tiles | Rows of 2, 3, or 4 always leave 1 leftover tile; only $1 \times 13$ forms a rectangle | `1, 13` (2 factors only) |

<div class="admonition note">
<p class="admonition-title">For Parents &amp; Teachers: Classroom Dialogue Script</p>
<p>
<strong>Teacher:</strong> "Take 12 counting tiles from your Counting Studio. Can you arrange them into a rectangle with at least two rows and two columns?"<br>
<strong>Student (Maya):</strong> "Yes! I built 2 rows of 6, and Marcus built 3 rows of 4!"<br>
<strong>Teacher:</strong> "Now take 13 tiles. Try to build a rectangle that is 2 tiles wide, 3 tiles wide, or 4 tiles wide without any leftover gaps."<br>
<strong>Maya:</strong> "It's impossible! Every time I try, there is an extra tile sticking out! The only way to fit all 13 is one long straight line of 13 tiles."<br>
<strong>Teacher:</strong> "That is the geometric soul of a prime number: it resists being factored into two dimensions! Now let's test both numbers on the SC-6."
</p>
</div>

#### Calculator Keystrokes & Stack Trace ($T, Z, Y, X$)
| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 12 | 0 | 0 | 0 | 12 |
| {{key:PRIME}} | 0 (Status Line: COMPOSITE -> Pushes 0 to Register X) | 0 | 0 | 0 |
| 13 | 0 | 0 | 0 | 13 |
| {{key:PRIME}} | 0 (Status Line: PRIME -> Pushes 1 to Register X) | 0 | 0 | 1 |

---

### Station Lesson 7.2: The Four-Color Sieve of Eratosthenes (144 Tiles)
- **Your Mission:** Construct the complete $12 \times 12$ matrix of 144 counting tiles, systematically eliminate composite multiples using the four distinct color palettes, and isolate all 34 primes $\le 144$.
- **Manipulatives:** 144 Stacking Tiles across four colors: Archival White (36), Cobalt Blue (36), Radiant Gold (36), Slate Gray (36).

<div class="admonition note">
<p class="admonition-title">The 144-Tile Four-Color Map Sieve of Eratosthenes</p>

- **Step 1:** Tile 1 (White) is set aside. 1 is a unit (neither prime nor composite).
- **Step 2: Prime 2 (Blue).** Replace every even multiple $\ge 4$ with Blue tiles ($4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, \dots$).
- **Step 3: Prime 3 (Gold).** Replace uncolored multiples of 3 with Gold tiles ($9, 15, 21, 27, 33, 39, 45, 51, 57, 63, \dots$).
- **Step 4: Primes 5 & 7 (White/Pattern).** Replace remaining multiples of 5 and 7 ($25, 35, 49, 55, 65, 77, 85, 91, 95, 115, 119, 121, 125, \dots$).
- **Step 5: Prime Survivors (Slate Gray).** Tiles surviving all 4 rounds are **THE PRIMES**:  
  $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139$ (Exactly 34 Primes $\le 144$!).
</div>

#### Hands-On Verification on SC-6:
You test survivor tiles and border cases on the calculator:
- Test 91: `{{res:sc6_07_data_probability_primes_seq_70:keys}}` $\longrightarrow$ Flashes `COMPOSITE`, pushes `0` ($91 = 7 \times 13$).
- Test 97: `{{res:sc6_07_data_probability_primes_seq_71:keys}}` $\longrightarrow$ Flashes `PRIME`, pushes `1`.
- Test 119: `{{res:sc6_07_data_probability_primes_seq_72:keys}}` $\longrightarrow$ Flashes `COMPOSITE`, pushes `0` ($119 = 7 \times 17$).
- Test 137: `{{res:sc6_07_data_probability_primes_seq_73:keys}}` $\longrightarrow$ Flashes `PRIME`, pushes `1`.
- **Step-by-Step RPN Reasoning & Stack Logic:**
  1. Seat the target candidate integer onto the display floor ($X$).
  2. Tap `{{key:FACT}}` to inspect its prime factor building blocks on the LCD shelves, verifying divisors without manual trial division.

---

### Station 7.3: The Magic Prime Tower Scale — Multiplying by Stacking Blocks!
- **Your Mission:** Discover a mind-blowing secret of numbers—that multiplication can be executed by physically stacking blocks of proportional heights—using the Prime Factor Studio.
- **Physical Manipulatives:** Prime Factor Studio and Proportional Prime Blocks ($2, 3, 5, 7$).

<div class="admonition note">
<p class="admonition-title">Prime Factor Studio &amp; Comparator Stage</p>
<p>
The back wall of the Prime Factor Studio holds a precision height comparator calibrated from 1 to 100.
Each prime number block has an exact proportional height:
- Prime 2 (Blue): $12.64\text{ mm}$
- Prime 3 (Amber/Green): $20.04\text{ mm}$
- Prime 5 (Yellow): $29.36\text{ mm}$
- Prime 7 (Red): $35.50\text{ mm}$

When you stack prime factor blocks together on the stage, their heights add up to match the exact composite product on the comparator wall!
</p>
</div>

{{blocks:prime_studio_comparator_stage|Prime Factor Studio: Bilateral Logarithmic Comparator Stage & Prime Factor Blocks}}

#### Try Stacking Your Prime Blocks!
1. **Multiplying $2 \times 3 = 6$:**
   Place Blue Block {{key:2}} on the desk. Stack Amber/Green Block {{key:3}} on top.
   $$h(2) + h(3) = 12.64\text{ mm} + 20.04\text{ mm} = \mathbf{32.68\text{ mm}}$$
   The top of the stack aligns **EXACTLY with the "6" tick mark on the comparator!**
2. **Multiplying $2 \times 5 = 10$:**
   Stack Blue Block {{key:2}} and Yellow Block {{key:5}}:
   $$h(2) + h(5) = 12.64\text{ mm} + 29.36\text{ mm} = \mathbf{42.00\text{ mm}}$$
   Lands precisely on the major decade line labeled **"10"**!
3. **Decomposing $60 = 2^2 \times 3 \times 5$:**
   Stack two {{key:2}}s, one {{key:3}}, and one {{key:5}}:
   $$2h(2) + h(3) + h(5) = 12.64 + 12.64 + 20.04 + 29.36 = \mathbf{74.68\text{ mm}}$$
   Points squarely at the **"60"** line on the rear wall!
4. **Why Order Doesn't Change the Height:**
   Reorder the stack: put Yellow {{key:5}} on the bottom, then {{key:3}}, then both {{key:2}}s.
   The total height remains identically **$74.68\text{ mm}$** ($5 \times 3 \times 2 \times 2 = 60$). Multiplication is commutative—no matter the order you stack them, the tower height never changes!

{{blocks:prime_studio_commutativity|Prime Studio Commutativity Proof: 2x5 = 5x2 = 10 Exact Flush Alignment}}

#### Verifying on the SC-6:
Key in `{{res:sc6_fact_60:keys}}` $\longrightarrow$ The graphic display decomposes `{{res:sc6_fact_60:value}}` into its prime factor tree (`2 × 2 × 3 × 5`):

{{res:sc6_fact_60:screenshot|SC-6 Prime Factorization Mode: 60 = 2 x 2 x 3 x 5}}

#### Stack Trace Table ($T, Z, Y, X$):
| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 60 | 0 | 0 | 0 | 60 |
| {{key:FACT}} | 0 | 0 | 0 | 2² × 3 × 5 |

---

### The Primality Testing Engine ({{key:PRIME}})
A prime number is a positive integer strictly greater than 1 whose only positive divisors are 1 and itself. On the SC-6, pressing the primary key {{key:PRIME}} (Row 2, Col 2) executes a deterministic primality test on Register $X$:
- Momentarily flashes `PRIME` or `COMPOSITE` on the graphic status line.
- Sets Register $X$ to truth flag `1` (if prime) or `0` (if composite).
- If $X \le 1$ or non-integer, flashes `INVALID DATA`.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 97 | 0 | 0 | 0 | 97 |
| {{key:PRIME}} | 0 (Status: PRIME -> 97 has exactly two factors: 1 and 97) | 0 | 0 | 1 |
| {{key:1}}{{key:1}}{{key:9}} | 0 | 0 | 1 | 119 |
| {{key:PRIME}} | 0 (Status: COMPOSITE -> 119 = 7 × 17) | 0 | 1 | 0 |
| {{key:2}} | 0 | 1 | 0 | 2 |
| {{key:PRIME}} | 0 (Status: PRIME -> 2 is the smallest and only even prime | 1 | 0 | 1 |

---

### Prime Factor Decomposition Engine (`{{key:FACT}}`)
Pressing `{{key:FACT}}` on Row 2, Col 2 decomposes any integer $\ge 2$ into its prime factor tree, formatting the output with mathematical superscripts and multiplication dots:
- Enter $12$: `12` `{{key:FACT}}` $\longrightarrow$ Displays: **`2² × 3`**
- Enter $360$: `360` `{{key:FACT}}` $\longrightarrow$ Displays: **`2³ × 3² × 5`**
- Enter $2,639$: `2639` `{{key:FACT}}` $\longrightarrow$ Displays: **`7 × 13 × 29`**

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:3}}{{key:6}}{{key:0}} | 0 | 0 | 0 | 360 |
| {{key:FACT}} | 0 | 0 | 0 | 2³ × 3² × 5 |

---

### Station Lesson 7.4: Hardware `{{key:GCF}}` and `{{key:LCM}}` Keys & Tactile Block Intersections

The SC-6 promotes Greatest Common Divisor (GCD/GCF) and Least Common Multiple (LCM) to dedicated keys on **Row 2, Col 1**:
- **Primary Key {{key:GCF}}:** Evaluates $\gcd(Y, X)$ (e.g., `{{res:sc6_gcf_12_18:keys}}` $\longrightarrow$ `{{res:sc6_gcf_12_18:value}}`).
- **Step-by-Step RPN Reasoning & Stack Logic:**
  1. `12` `{{key:ENTER}}` — Stage first integer 12 onto the upper shelf ($Y = 12$).
  2. `18` `{{key:GCF}}` — Place second integer 18 on the floor ($X = 18$) and trigger `{{key:GCF}}`: the hardware Euclidean engine extracts the greatest common factor $\gcd(12, 18) = 6$ ($X = 6$).
- **`{{key:f}}`-Shifted Key {{key:LCM}}:** Evaluates $\operatorname{lcm}(Y, X)$ (e.g., `{{res:sc6_lcm_12_18:keys}}` $\longrightarrow$ `{{res:sc6_lcm_12_18:value}}`).

#### Tactile Venn Intersection with Prime Studio Blocks:
Take $a = 48$ and $b = 72$:
- Decompose $48 = 2^4 \times 3^1$: Assemble four {{key:2}} blocks and one {{key:3}} block.
- Decompose $72 = 2^3 \times 3^2$: Assemble three {{key:2}} blocks and two {{key:3}} blocks.
- **The Intersection ($\text{GCF}$):** The shared factor blocks common to both towers are **three {{key:2}}s and one {{key:3}}**:
  $$\text{GCF} = 2^3 \times 3 = 8 \times 3 = \mathbf{24}$$
- **The Union ($\text{LCM}$):** Take the maximum power of each prime (**four {{key:2}}s and two {{key:3}}s**):
  $$\text{LCM} = 2^4 \times 3^2 = 16 \times 9 = \mathbf{144}$$

{{blocks:prime_lcm_gcd_venn|Prime Factor Studio: Prime Factorization and Venn Intersection Model}}

#### Application 1: Rectangle Tiling (GCF)
A maker lab needs to tile a tabletop measuring $24\text{ cm} \times 36\text{ cm}$ using the largest possible congruent square tiles with zero waste or cutting.
$$\text{Tile Side} = \gcd(24, 36) = \mathbf{12\text{ cm}}$$

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 24 | 0 | 0 | 0 | 24 |
| {{key:ENTER}} | 0 | 0 | 24 | 24 |
| 36 | 0 | 0 | 24 | 36 |
| {{key:GCF}} | 0 | 0 | 0 | 12.00 |

#### Application 2: Synchronized Flashing Cycle (LCM)
Two beacon lights flash at fixed intervals: Light A flashes every $6\text{ seconds}$, while Light B flashes every $8\text{ seconds}$. After how many seconds will they next flash simultaneously?
$$\text{Next Flash} = \operatorname{lcm}(6, 8) = \mathbf{24\text{ seconds}}$$

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:6}} | 0 | 0 | 0 | 6 |
| {{key:ENTER}} | 0 | 0 | 6 | 6 |
| {{key:8}} | 0 | 0 | 6 | 8 |
| {{key:LCM}} | 0 | 0 | 0 | 24.00 |

#### Application 3: Fraction Least Common Denominator (LCD)
When adding unlike fractions $\frac{3}{8} + \frac{5}{12}$, the Least Common Denominator is the LCM of the denominators:
$$\text{LCD} = \operatorname{lcm}(8, 12) = \mathbf{24}$$

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:8}} | 0 | 0 | 0 | 8 |
| {{key:ENTER}} | 0 | 0 | 8 | 8 |
| 12 | 0 | 0 | 8 | 12 |
| {{key:LCM}} | 0 | 0 | 0 | 24.00 |

---

### The Secret Partner Rule: Why GCF × LCM Always Equals a × b!
For any two positive integers $a$ and $b$, the product of their greatest common factor and least common multiple is strictly equal to the product of the original numbers:
$$\gcd(a, b) \times \operatorname{lcm}(a, b) = a \times b$$

#### Mathematical Proof & Stack Verification:
Consider $a = 24$ and $b = 36$:
- $\gcd(24, 36) = 12$
- $\operatorname{lcm}(24, 36) = 72$
- Product of GCF and LCM: $12 \times 72 = 864$
- Product of original numbers: $24 \times 36 = 864$

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 24 | 0 | 0 | 0 | 24 |
| {{key:ENTER}} | 0 | 0 | 24 | 24 |
| 36 | 0 | 0 | 24 | 36 |
| {{key:LCM}} | 0 | 0 | 0 | 72 |
| 12 | 0 | 0 | 72 | 12 |
| {{key:×}} | 0 | 0 | 0 | 864 |

Check against direct product on the stack: `{{res:sc6_07_data_probability_primes_seq_74:keys}}` $\longrightarrow X = \mathbf{864.00}$ (Secret Partner Rule confirmed!).

---

### The Euclidean Division Algorithm via Hardware `{{key:÷R}}`
Euclid of Alexandria discovered over 2,300 years ago that the greatest common divisor of two integers can be found by repeated division with remainders:
$$\gcd(a, b) = \gcd(b, a \bmod b)$$

On the SC-6, you execute the Euclidean algorithm using the shifted key {{key:÷R}} (`÷R` on `/`). Each press of {{key:÷R}} divides $Y$ by $X$, placing the quotient $Q$ in Register $X$ and the remainder $R$ in Register $Y$.

#### Worked Example 7.3: Step-by-Step Euclidean Ladder for $\gcd(105, 45)$
Find $\gcd(105, 45)$ using Euclidean division:
1. $105 \div 45 = 2$ with remainder $15 \implies \gcd(105, 45) = \gcd(45, 15)$.
2. $45 \div 15 = 3$ with remainder $0 \implies \gcd(45, 15) = 15$.
The last non-zero remainder is **15**, so $\gcd(105, 45) = \mathbf{15}$.

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:1}}{{key:0}}{{key:5}} | 0 | 0 | 0 | 105 |
| {{key:ENTER}} | 0 | 0 | 105 | 105 |
| 45 | 0 | 0 | 105 | 45 |
| {{key:÷R}} | 0 (Register Y = Remainder 15, Register X = Quotient 2) | 0 | 15 | 2 |
| {{key:x⇄y}} | 0 | 0 | 2 | 15 |

#### Euclidean Division Ladders for Large Number Pairs
For larger composite numbers, you construct an RPN division ladder, using the quotient and remainder output of {{key:÷R}} to systematically reduce the problem to zero remainder:

#### Worked Example 7.5: Euclidean Ladder for $\gcd(252, 105)$
1. $252 \div 105 = 2$ with remainder $42$ ($252 = 2 \times 105 + 42$)
2. $105 \div 42 = 2$ with remainder $21$ ($105 = 2 \times 42 + 21$)
3. $42 \div 21 = 2$ with remainder $0$ ($42 = 2 \times 21 + 0$)
The last non-zero remainder is **21**, so $\gcd(252, 105) = \mathbf{21}$.

| Step / Key | Dividend (Y) | Divisor (X) | Quotient (X) | Remainder (Y) |
| :--- | :--- | :--- | :--- | :--- |
| 252 {{keycap:E}} 105 | 252 | 105 | - | - |
| {{key:÷R}} | - | - | 2 | 42 |
| {{key:x⇄y}} | 2 | 42 | 42 | 2 |
| 105 {{key:x⇄y}} | 105 | 42 | - | - |
| {{key:÷R}} | - | - | 2 | 21 |
| 42 {{key:x⇄y}} | 42 | 21 | - | - |
| {{key:÷R}} | - | - | 2 | 0 |

You can directly verify this result in a single step using the hardware key:
`{{res:sc6_07_data_probability_primes_seq_75:keys}}` $\longrightarrow X = \mathbf{21.00}$!

---

## Elementary Descriptive Statistics & Data Analysis

<div class="admonition note">
<p class="admonition-title">For Parents &amp; Teachers: Curriculum Standards</p>
<p>Common Core Standards Alignment: CCSS 6.SP.A.2, 6.SP.B.5.</p>
</div>

In Grades 5 and 6, you transition from counting discrete numbers to analyzing datasets: describing the center (mean, median, mode) and measuring the spread or variability (range, interquartile range, mean absolute deviation).

| Metric | Key / Shift | Mathematical Definition |
| :--- | :--- | :--- |
| **Sample Size ($n$)** | `{{key:N}}` | Count of data points |
| **Sum of Data ($\Sigma x$)** | `{{key:Σx}}` / `{{key:Σx}}` | Total accumulation |
| **Mean (Average)** | `{{key:x̄}}` / `{{keycap:x̄}}` | $(\Sigma x) / n$ |
| **Median** | `{{keycap:MED}}` | Middle value of sorted set |
| **Mode** | `{{key:MODE}}` | Most frequent value |
| **Range** | `{{key:RNG}}` | $\text{Maximum} - \text{Minimum}$ |
| **Interquartile Range** | `{{key:IQR}}` | $Q_3 - Q_1$ |
| **Mean Absolute Deviation** | `{{key:MAD}}` | $\frac{1}{n} \sum |x_i - \bar{x}|$ |

### Dataset 1: The 10-Quiz Score Frequency Table & The Seed of Distributions

A 5th-grade math class records scores on a 100-point weekly quiz across 10 students:
$$70, \ 75, \ 80, \ 80, \ 85, \ 85, \ 85, \ 90, \ 90, \ 95$$

| Score ($x$) | Tally | Frequency ($f$) | Dot Plot Visual Representation |
| :---: | :---: | :---: | :--- |
| 70 | \| | 1 | ● |
| 75 | \| | 1 | ● |
| 80 | \|\| | 2 | ● ● |
| 85 | \|\|\| | 3 | ● ● ● *(Peak Mode!)* |
| 90 | \|\| | 2 | ● ● |
| 95 | \| | 1 | ● |
| **Total Count ($n = \sum f$)** | — | **10** | $10$ total observations |

#### The Intellectual Bridge to Distributions:
Notice the shape of the dot plot! The data rises smoothly from $70$ to a central peak at $85$, and then descends symmetrically down to $95$. This bell-shaped mound is your first intuitive encounter with **symmetric distributions**. In middle and high school, this exact visual symmetry develops into the continuous Gaussian Normal Distribution curve!

#### Complete SC-6 Statistical Evaluation:
> {{keycap:CLΣ}}                               -> Clears all stats registers (n = 0)
> 70 {{key:Σ+}}                        -> n = 1
> 75 {{key:Σ+}}                        -> n = 2
> 80 {{key:Σ+}} 80 {{key:Σ+}}           -> n = 4
> 85 {{key:Σ+}} 85 {{key:Σ+}} 85 {{key:Σ+}} -> n = 7
> 90 {{key:Σ+}} 90 {{key:Σ+}}           -> n = 9
> 95 {{key:Σ+}}                        -> n = 10

1. **Sample Size ($n$):** `{{key:N}}` $\longrightarrow X = \mathbf{10}$.
2. **Sum of Scores ($\Sigma x$):** `{{key:Σx}}` $\longrightarrow X = \mathbf{835.0}$.
3. **Mean Score ($\bar{x}$):** {{key:x̄}} $\longrightarrow X = \mathbf{83.5}$.
4. **Median Score ($\text{Med}$):** `{{key:MED}}` $\longrightarrow X = \mathbf{85.0}$.
5. **Mode Score ($\text{Mode}$):** `{{key:MODE}}` $\longrightarrow X = \mathbf{85.0}$.
6. **Range ($\text{Max} - \text{Min}$):** `{{key:RNG}}` $\longrightarrow X = \mathbf{25.0}$ ($95 - 70 = 25$).

Because the distribution is perfectly symmetrical around 85, the **Median** and **Mode** are identical ($85.0$), while the **Mean** ($83.5$) sits just below the peak due to the lower score of 70.

---

### Dataset 2: 5-Quiz Empirical Investigation (Measures of Spread: IQR & MAD)

A smaller study group records five scores: $85, 90, 75, 90, 100$.

#### Statistical Metrics Audit:
1. **Sorted Data:** $75, 85, 90, 90, 100$.
2. **Count:** $n = 5$.
3. **Sum:** $\Sigma x = 75 + 85 + 90 + 90 + 100 = 440.0$.
4. **Mean ($\bar{x}$):** $\frac{440}{5} = \mathbf{88.0}$.
5. **Median:** Middle ranked value = $\mathbf{90.0}$.
6. **Mode:** Most frequent value = $\mathbf{90.0}$.
7. **Minimum:** $\mathbf{75.0}$, **Maximum:** $\mathbf{100.0}$.
8. **Range:** $100 - 75 = \mathbf{25.0}$.
9. **Interquartile Range (IQR):** In RPNCore, inclusive-median quartiles yield $Q_1 = 85.0$ and $Q_3 = 90.0$:
   $$\text{IQR} = Q_3 - Q_1 = 90.0 - 85.0 = \mathbf{5.0}$$
10. **Mean Absolute Deviation (MAD):** Measures the average distance between each data point and the mean ($\bar{x} = 88.0$):
    $$|75 - 88| = 13, \quad |85 - 88| = 3, \quad |90 - 88| = 2, \quad |90 - 88| = 2, \quad |100 - 88| = 12$$
    $$\text{Sum of Deviations} = 13 + 3 + 2 + 2 + 12 = 32.0$$
    $$\text{MAD} = \frac{32.0}{5} = \mathbf{6.4}$$

> **Keystrokes:**
> {{keycap:CLΣ}}
> 85 {{key:Σ+}} 90 {{key:Σ+}} 75 {{key:Σ+}} 90 {{key:Σ+}} 100 {{key:Σ+}}
> {{key:Σx}}    -> 440.00
> {{key:x̄}}  -> 88.00
> {{keycap:MED}}       -> 90.00
> {{key:MODE}}  -> 90.00
> {{key:IQR}}   -> 5.00
> {{key:MAD}}   -> 6.40

### The Five-Number Summary, Box Plots & Outlier Analysis
In data science, you represent distributions graphically using **Box-and-Whisker Plots**. A box plot partitions any ordered dataset into four quartiles using five milestone numbers:
1. **Minimum ($Min$):** Lowest observed value (`{{key:MIN}}`).
2. **First Quartile ($Q_1$):** 25th percentile boundary.
3. **Median ($Med$):** 50th percentile center (`{{key:MED}}`).
4. **Third Quartile ($Q_3$):** 75th percentile boundary.
5. **Maximum ($Max$):** Highest observed value (`{{key:MAX}}`).

| Box Plot Milestone | Statistical Keycap | Percentile / Structural Role |
| :--- | :--- | :--- |
| **Lower Whisker Tip ($Min$)** | `{{key:MIN}}` | $0\text{th}$ percentile (minimum non-outlier observation) |
| **Left Box Edge ($Q_1$)** | `{{key:1Q}}` | $25\text{th}$ percentile (lower boundary of central $50\%$ box) |
| **Interior Vertical Line ($Med$)** | `{{key:MED}}` | $50\text{th}$ percentile (median dividing the box) |
| **Right Box Edge ($Q_3$)** | `{{key:3Q}}` | $75\text{th}$ percentile (upper boundary of central $50\%$ box) |
| **Central Box Span ($\text{IQR}$)** | `{{key:IQR}}` | Interquartile range $\text{IQR} = Q_3 - Q_1$ |
| **Upper Whisker Tip ($Max$)** | `{{key:MAX}}` | $100\text{th}$ percentile (maximum non-outlier observation) |

#### The $1.5 \times \text{IQR}$ Outlier Detection Rule
An **outlier** is an anomalous data point that lies unusually far from the central cluster. In competitive STEM challenges and introductory data science, points beyond the inner fences are classified as statistical outliers:
$$\text{Lower Fence} = Q_1 - 1.5 \times \text{IQR}$$
$$\text{Upper Fence} = Q_3 + 1.5 \times \text{IQR}$$

#### Worked Example 7.6: Detecting an Outlier in Running Times
A group of 8 runners complete a race in the following minutes: $25, 28, 30, 32, 34, 35, 38, 58$. Runner 8 took 58 minutes. Is 58 a statistical outlier?

> **Step 1: Compute Quartiles:**
> Ordered data: 25, 28, 30, 32, 34, 35, 38, 58
> Q1 = (28 + 30) / 2 = 29.0
> Median = (32 + 34) / 2 = 33.0
> Q3 = (35 + 38) / 2 = 36.5
> IQR = 36.5 - 29.0 = 7.5
>
> Step 2: Compute Upper Fence via RPN:
> 36.5 {{key:ENTER}} 7.5 {{key:ENTER}} 1.5 {{key:×}} {{key:+}}  -> 47.75 minutes
- `{{res:sc6_07_data_probability_primes_seq_76:keys}}` $\longrightarrow 11.25$ ($1.5 \times \text{IQR}$)
- `36.5 {{key:+}}` $\longrightarrow \mathbf{47.75\text{ minutes}}$ (Upper Fence).

Since $58 > 47.75$, the score of 58 minutes lies well outside the upper fence and is confirmed as a **true statistical outlier**!

---

## Grade 6 Pre-Algebra: Signed Numbers, Absolute Value & Inverses

In pre-algebra, you cross a thrilling new threshold: numbers are no longer merely static amounts—they possess **direction** along the real number line.

| Negative Direction ($x < 0$) | Origin ($0$) | Positive Direction ($x > 0$) |
| :---: | :---: | :---: |
| `-5, -4, -3, -2, -1` | **`0`** | `+1, +2, +3, +4, +5` |

### Signed Number Entry via the Negation Key `{{key:+/-}}`
A vital distinction in early algebra is the difference between:
- The **binary operation of subtraction** (`{{key:-}}`), which combines two numbers ($Y - X$).
- The **unary sign toggle** (`{{key:+/-}}`), which negates the active number in Register $X$.

On the SC-6:
- To enter $-8$: type `{{key:8}} {{key:+/-}}`. The screen displays `-8`.
- Pressing `{{key:+/-}}` again toggles back to `8`.
- **Zero Invariant:** Negating zero leaves `0` unchanged.

#### Worked Example 7.4: Winter Temperature Differential
At 6:00 AM, the outdoor temperature in Chicago is $-14^\circ\text{C}$. By 2:00 PM, the temperature rises by $+9^\circ\text{C}$. What is the afternoon temperature?

$$\text{Equation: } -14 + 9 = -5^\circ\text{C}$$

> **RPN Evaluation:**
> 14 {{key:+/-}} {{key:ENTER}} {{key:9}} {{key:+}}  -> -5.00 °C

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 14 | 0 | 0 | 0 | 14 |
| {{key:+/-}} | 0 | 0 | 0 | -14 |
| {{key:ENTER}} | 0 | 0 | -14 | -14 |
| {{key:9}} | 0 | 0 | -14 | 9 |
| {{key:+}} | 0 | 0 | 0 | -5 |

---

### Absolute Value as Number Line Distance (`{{key:|x|}}`)
The absolute value of a real number $x$, denoted $|x|$, represents its non-negative distance from zero along the number line, regardless of direction:
$$|x| = \begin{cases} x & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases}$$

On the SC-6, pressing `{{key:|x|}}` (Row 0, Col 4 `{{key:g}}` Shift) instantly strips the negative sign from Register $X$, preserving magnitude:
- `42 {{key:+/-}} {{key:|x|}}` $\longrightarrow X = \mathbf{42}$.
- `15 {{key:|x|}}` $\longrightarrow X = \mathbf{15}$.

#### Worked Example 7.5: Elevation Difference: Death Valley vs. Mountain Peak
A hiker descends to Badwater Basin in Death Valley at an elevation of $-86\text{ meters}$ (below sea level), then ascends to Telescope Peak at $+3,366\text{ meters}$. Find the total vertical elevation climbed.

$$\text{Vertical Climb: } |3366 - (-86)| = |3366 + 86| = 3,452\text{ meters}$$

> **RPN Evaluation:**
> 3366 {{key:ENTER}} 86 {{key:+/-}} {{key:-}} {{key:|x|}}  -> 3452.00 meters

---

### Geometric Inverses: Area-to-Side-Length (`{{key:x²}}` and `{{key:√x}}`)
In elementary school, the square key `{{key:x²}}` and square root key `{{key:√x}}` are taught strictly as **geometric area-to-side-length inverses**, not as abstract exponential powers:
- Squaring a number finds the **area** of a square given its side length: $A = s^2$.
- Taking the square root finds the **side length** of a square given its enclosed area: $s = \sqrt{A}$.

| Square Geometry | Forward Operation (`{{key:x²}}`) | Inverse Operation (`{{key:√x}}`) |
| :--- | :--- | :--- |
| **5 cm × 5 cm Tile Square** | Side $s = 5\text{ cm} \to \text{Area } A = s^2 = \mathbf{25\text{ cm}^2}$ | Area $A = 25\text{ cm}^2 \to \text{Side } s = \sqrt{25} = \mathbf{5\text{ cm}}$ |

#### Worked Example 7.6: Fencing a Square Pasture
A horse pasture has an exact square area of $1,225\text{ square meters}$.
1. What is the length of one side of the pasture?
2. What is the total length of fencing required to surround all four sides?

> **Step 1: Compute side length s = √A:**
> 1225 {{key:√x}}       -> 35.00 meters
>
> Step 2: Compute perimeter P = 4 * s:
> {{key:4}} {{key:×}}                         -> 140.00 meters
Each side is $\mathbf{35\text{ meters}}$, requiring $\mathbf{140\text{ meters}}$ of fence.

### Real-World Pre-Algebra Word Problems: Directed Integers in Motion
To master pre-algebra, you can solve multi-step signed integer problems reflecting real-world engineering, financial, and environmental contexts.

#### Scenario 1: Skyscraper Elevator Traversal
A high-rise tower features 3 subterranean parking levels (Floors $-3, -2, -1$), a ground lobby (Floor $0$), and 60 tower floors (Floors $1 \dots 60$).
- An elevator starts at subterranean parking Level $-3$.
- It travels up $+45$ floors to deliver office supplies.
- It then descends $-12$ floors to the cafeteria.
- Finally, it descends $-33$ floors.
Where does the elevator finish?

$$\text{Equation: } -3 + 45 - 12 - 33 = -3\text{ (Back at parking Level -3!)}$$

> **RPN Execution:**
> {{key:3}} {{key:+/-}} {{key:ENTER}} 45 {{key:+}} 12 {{key:-}} 33 {{key:-}}  -> -3.00 (Level -3)

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:3}} {{key:+/-}} | 0 | 0 | 0 | -3 |
| {{key:ENTER}} | 0 | 0 | -3 | -3 |
| 45 | 0 | 0 | -3 | 45 |
| {{key:+}} | 0 | 0 | 0 | 42 |
| 12 | 0 | 0 | 42 | 12 |
| {{key:-}} | 0 | 0 | 0 | 30 |
| 33 | 0 | 0 | 30 | 33 |
| {{key:-}} | 0 | 0 | 0 | -3 |

#### Scenario 2: Deep-Sea Oceanographic Research Submersible
A marine biology autonomous vehicle begins a mission on the deck of a research ship at $+4\text{ meters}$ above sea level. It dives to a survey trench at $-350\text{ meters}$.
1. Find the total vertical descent distance.
2. The vehicle then ascends $+125\text{ meters}$ to sample a hydrothermal vent, before descending an additional $-45\text{ meters}$. Find its final depth.

> **Step 1: Total vertical descent distance:**
> {{key:4}} {{key:ENTER}} 350 {{key:+/-}} {{key:-}} {{key:|x|}}  -> 354.00 meters
>
> Step 2: Final depth:
> 350 {{key:+/-}} {{key:ENTER}} 125 {{key:+}} 45 {{key:-}}  -> -270.00 meters
The vehicle surveyed the vent at a final depth of **$-270\text{ meters}$**.

#### Scenario 3: Bank Account Ledger with Overdraft Fees
Your student checking account starts with a positive balance of $+\$120.00$.
- You buy school books for $\$85.00$ ($-\$85.00$).
- You buy an art supply kit for $\$60.00$ ($-\$60.00$).
- The bank assesses an overdraft penalty of $\$25.00$ ($-\$25.00$).
- You deposit a lawn-mowing paycheck of $\$95.00$ ($+\$95.00$).
Calculate your net account balance using the SC-6 currency formatter `{{key:$}}`.

> **RPN Ledger Evaluation:**
> 120 {{key:ENTER}} 85 {{key:-}} 60 {{key:-}} 25 {{key:-}} 95 {{key:+}} {{key:$}}
- `{{res:sc6_07_data_probability_primes_seq_77:keys}}` $\longrightarrow 35.00$
- `60 {{key:-}}` $\longrightarrow -25.00$ (Account in overdraft!)
- `25 {{key:-}}` $\longrightarrow -50.00$ (Penalty assessed)
- `95 {{key:+}}` $\longrightarrow 45.00$ (Deposit restores positive balance!)
- `{{key:$}}` $\longrightarrow \mathbf{\$45.00}$.

---

<div class="admonition note">
<p class="admonition-title">For Parents &amp; Teachers: Empirical Probability, Number Theory &amp; Zero Pairs</p>
<p>
<strong>Empirical Probability Distributions and Statistical Accumulation:</strong> Teaching data and discrete probability in upper elementary requires guiding learners from subjective guesswork ("seven feels lucky") toward rigorous empirical evidence. The SC-6 hardware probability engine (<code>{{key:🎲}}</code>) paired with the statistical accumulator (<code>{{key:Σ+}}</code>) provides a real-time experimental laboratory directly in the learner's hands. When collecting sample datasets, learners observe empirical distributions stabilize as sample size $n$ increases. Entering successive data points into <code>{{key:Σ+}}</code> reveals how measures of center—mean, median, and mode—converge in symmetric unimodal distributions. In number theory, dedicated hardware keys for <code>{{key:GCF}}</code> and <code>{{key:LCM}}</code> allow students to verify the Fundamental Duality Theorem ($\gcd(a,b) \times \operatorname{lcm}(a,b) = a \times b$) empirically, transforming abstract identities into tangible discoveries.<br><br>
<strong>Tactile Zero-Pair Balances and Pre-Algebra Mental Models:</strong> Directed negative numbers frequently present a major cognitive hurdle in transition to pre-algebra, particularly the misconception that subtraction always results in a smaller quantity (such as $-8 - (-5) = -3$). The SC-6 grounds integer arithmetic by pairing the hardware negation toggle (<code>{{key:+/-}}</code>) with physical two-color counters. Learners model negative numbers as Crimson tokens and positive numbers as Yellow tokens. Removing five Crimson tokens from a group of eight Crimson tokens visually leaves three Crimson tokens, reinforcing that taking away debt increases net value. On the calculator, typing <code>8 {{key:+/-}} ENTER 5 {{key:+/-}} -</code> delivers $X = -3$ with zero syntax ambiguity.<br><br>
<strong>Silicon Architecture &amp; Hardware Primitives:</strong> The SC-6 statistical architecture incorporates dedicated accumulators ($\Sigma x$, $\Sigma x^2$, and sample count $n$) that update independently of the four-register working stack ($T, Z, Y, X$). Data points can be transformed or computed through intermediate formulas without overwriting running summation totals. Similarly, hardware Euclidean division via <code>{{key:÷R}}</code> executes integer division in a single cycle: dividend and divisor are processed, quotient is deposited into Register $X$, and remainder is retained in Register $Y$. Tapping <code>{{key:x⇄y}}</code> instantly prepares the remainder as the divisor for the next Euclidean iteration, illustrating the elegance and efficiency of hardware RPN architecture.
</p>
</div>

<div class="admonition note">
<p class="admonition-title">For Parents &amp; Teachers: Classroom Dialogue Scripts &amp; Misconception Diagnostics</p>
<p>
<strong>Script 7.1: The Definition of a Prime Number:</strong><br>
<strong>Teacher:</strong> "Class, who can tell me: is the number 1 a prime number?"<br>
<strong>Student (Liam):</strong> "Yes! Because 1 can only be divided by 1 and itself!"<br>
<strong>Teacher:</strong> "Let's check the formal mathematical definition. A prime number is a positive integer that has <em>exactly two distinct positive divisors</em>: 1 and itself. How many different divisors does the number 1 have?"<br>
<strong>Liam:</strong> "Just... 1."<br>
<strong>Teacher:</strong> "Right! 1 only has one factor, not two! What about composite numbers?"<br>
<strong>Liam:</strong> "Composite numbers have three or more factors."<br>
<strong>Teacher:</strong> "So where does 1 belong?"<br>
<strong>Liam:</strong> "It's not prime, and it's not composite. It's special!"<br>
<strong>Teacher:</strong> "Exactly! 1 is called a unit. Now test it on your SC-6: type <code>{{res:sc6_07_data_probability_primes_seq_79:keys}}</code>. What does the screen say?"<br>
<strong>Liam:</strong> "It flashes <code>INVALID DATA</code>! It won't let me call 1 a prime!"<br>
<strong>Teacher:</strong> "Now try the number 2: <code>{{res:sc6_07_data_probability_primes_seq_80:keys}}</code>."<br>
<strong>Liam:</strong> "It flashes <code>PRIME</code>! And pushes 1 to the stack!"<br>
<strong>Teacher:</strong> "2 is the smallest prime number, and the only even prime in the entire universe!"<br><br>
<strong>Script 7.2: Subtracting a Negative Number:</strong><br>
<strong>Student (Chloe):</strong> "Teacher, I don't understand why $7 - (-3)$ equals $10$. When you subtract, shouldn't the number get smaller?"<br>
<strong>Teacher:</strong> "Take our two-color counters, Chloe. Imagine you are running a school store. A customer owes you $\$3$, which is a debt of $-3$. If you decide to forgive the debt—meaning you <em>take away</em> the negative $\$3$—does the customer have more money or less money?"<br>
<strong>Chloe:</strong> "They have more money! Because their debt is gone!"<br>
<strong>Teacher:</strong> "Taking away a negative is the exact same as adding a positive! Now test it on your SC-6: <code>{{res:sc6_07_data_probability_primes_seq_81:keys}}</code>."<br>
<strong>Chloe:</strong> "It says 10! Because taking away 3 negatives leaves 10 positives!"
</p>

<h4>Misconception Diagnostic Table</h4>

| Observable Error | Cognitive Root Cause | Targeted Remediation Prompt |
| :--- | :--- | :--- |
| **Claiming 1 is prime** | Conflating "divisible only by 1" with "having exactly two distinct factors." | *"A prime must have exactly two distinct factors: 1 and itself. 1 only has one factor. The SC-6 classifies 1 as a unit, neither prime nor composite."* |
| **Confusing GCF and LCM** | Assuming "Greatest" must yield a larger number than "Least." | *"A factor divides INTO a number, so it must be smaller than or equal to the number. A multiple MULTIPLIES the number, so it grows larger! GCF $\le$ numbers $\le$ LCM."* |
| **Treating `$|x|$` as 'change the sign'** | Believing absolute value turns positive numbers into negative numbers. | *"Absolute value is distance on a number line. Distance is never negative! The distance from 5 to 0 is 5; the distance from -5 to 0 is also 5. `$|5| = 5$` and `$|-5| = 5$`."* |
| **Adding negatives: $-4 + (-3) = -1$** | Subtracting magnitudes instead of accumulating directed negative quantities. | *"If you take 4 steps backward ($-4$), and then take 3 more steps backward ($-3$), you are 7 steps backward ($-7$), not 1 step! Use Crimson tokens to model the sum."* |
| **Expecting Mean = Median always** | Assuming all datasets are perfectly symmetrical. | *"In skewed datasets (like home prices or quiz scores with an outlier), extreme values pull the mean away from the center. The median stays fixed in the middle."* |
| **Confusing `{{key:+/-}}` with `{{key:-}}`** | Using the binary subtraction operator to enter negative values. | *"The `{{key:-}}` key subtracts two numbers ($Y - X$). The `{{key:+/-}}` key changes the sign of the single number you are actively typing."* |

</div>

---

## Comprehensive Problem Bank: 50 Worked Reference Problems

The following problem bank provides complete, publication-grade reference solutions spanning Grade 5 and Grade 6 discrete probability, number theory, descriptive statistics, and pre-algebra. Every keystroke sequence assumes the SC-6 baseline mode `{{key:NUM}}`.

<div class="admonition note">
<p class="admonition-title">Hands-On Studio Proof: Blocks -> Calculator</p>

Before executing probability distributions, primality tests, and statistical summaries symbolically, you ground each mathematical principle in physical manipulatives:
1. **Discrete Probability & Geometry (The Dice Studio):** Roll the 3D-printed equal-volume pip dice 60 times. Record outcomes on the dot plot board. Compare empirical frequencies against theoretical fractions on the SC-6 (`{{key:FDISP}}`), proving why $P(\text{Odd}) = 3/6 = 1/2$.
2. **Primality & Rectangular Factoring (The 144-Tile Studio):** Take 83 tiles. Attempt to form rectangular grids of 2, 3, 5, or 7 rows. When every attempt leaves leftover tiles, confirm the number is prime by pressing `{{res:sc6_07_data_probability_primes_seq_82:keys}}`, watching the LCD illuminate `PRIME` ($X = 1$). Repeat with 91 tiles to discover $7 \times 13 = 91$ (`COMPOSITE`, $X = 0$).
3. **Tactile Venn Intersections (The Prime Factor Studio):** Model 48 and 72 using proportional logarithmic blocks. Physically place common factor blocks ($2^3 \times 3$) into the central comparator well to verify $\gcd(48, 72) = 24$ (`{{res:sc6_07_data_probability_primes_seq_83:keys}}`).
4. **Zero-Pair Balances (Two-Color Counters):** Pair Sun Yellow ($+1$) and Signal Crimson ($-1$) tokens to eliminate zero pairs before executing signed integer arithmetic on the stack (`{{key:+/-}}`).
</div>

### Expedition 1: The High-Rollers Tabletop & Spinner Tournament (Challenges 1–5)
*Mission Briefing: You are the chief statistician for a tabletop gaming tournament. Compute exact single-event probabilities, compound die throws, and complementary odds using RPN stack division and fraction displays.*

#### Challenge 1: Single Die Roll Probability
- **Tournament Context:** Tabletop Gaming Tournament: In the championship match, a referee rolls a precision equal-volume pip six-sided die. Calculate the theoretical probability of rolling an odd face ($1, 3, 5$).
- **Hands-On Manipulative Stage (Precision Pip Dice):** Inspect the physical equal-volume pip dice. Notice that 3 out of 6 faces are odd numbers. Rolling the die 60 times yields approximately 30 odd occurrences, validating the $3/6 = 0.5$ theoretical ratio.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_01:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_01:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3` | $0$ | $0$ | $0$ | $3$ | Key in favorable odd outcomes count ($1, 3, 5$) |
| `{{key:ENTER}}` | $0$ | $0$ | $3$ | $3$ | Stack lifts; favorable count locked into Register $Y$ |
| `6` | $0$ | $0$ | $3$ | $6$ | Key in total sample space outcomes of fair six-sided die ($6$) |
| `{{key:÷}}` | $0$ | $0$ | $0$ | $0.5$ | Divide favorable by total to compute theoretical probability ($3/6 = 0.5$) |

- **Diagnostic Checkpoint:** Register $X$ displays $0.5000$. Theoretical probability of rolling an odd face is $\mathbf{0.5000}$ ($50\%$).

#### Challenge 2: Tournament Card Deck Draw
- **Tournament Context:** Tournament Card Deck Draw: In a card tournament, a standard 52-card deck contains 4 aces. What is the probability of drawing an ace at random on the first draw?
- **Hands-On Manipulative Stage (Card Deck Partition):** Partition the deck into 4 aces and 48 non-aces. The 4 target aces represent a $1/13$ fraction of the total 52-card sample space.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_02:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_02:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4` | $0$ | $0$ | $0$ | $4$ | Key in favorable ace count (4 aces) |
| `{{key:ENTER}}` | $0$ | $0$ | $4$ | $4$ | Stack lifts; favorable count locked into Register $Y$ |
| `52` | $0$ | $0$ | $4$ | $52$ | Key in total cards in deck ($52$) |
| `{{key:÷}}` | $0$ | $0$ | $0$ | $0.0769$ | Divide to calculate single-draw ace probability ($4/52 \approx 0.0769$) |

- **Diagnostic Checkpoint:** Register $X$ displays $0.0769$. Ace drawing probability is $\mathbf{0.0769}$ ($\approx 7.69\%$).

#### Challenge 3: Compound Coin Toss: Three Consecutive Heads
- **Tournament Context:** Triple Coin Toss Tournament Tiebreaker: A match tiebreaker requires flipping three consecutive heads with a balanced coin ($P = (1/2)^3$). Determine the compound probability of three consecutive heads.
- **Hands-On Manipulative Stage (Tree Diagram Counters):** Arrange a 3-tier binary tree using two-color counters. Out of 8 possible paths ($\text{HHH}, \text{HHT}, \dots, \text{TTT}$), exactly 1 path yields three consecutive heads.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_03:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_03:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `0.5` | $0$ | $0$ | $0$ | $0.5$ | Key in single fair toss probability ($0.5$) |
| `{{key:ENTER}}` | $0$ | $0$ | $0.5$ | $0.5$ | Stack lifts; single-toss probability locked into Register $Y$ |
| `3` | $0$ | $0$ | $0.5$ | $3$ | Key in exponent 3 for three independent trials |
| `{{key:yˣ}}` | $0$ | $0$ | $0$ | $0.125$ | Raise to 3rd power to compute compound probability ($0.5^3 = 0.125$) |

- **Diagnostic Checkpoint:** Register $X$ displays $0.1250$. Probability of three consecutive heads is $\mathbf{0.1250}$ ($12.5\%$).

#### Challenge 4: Sum of Two Dice: Rolling an 11 or 12
- **Tournament Context:** High-Rollers Two-Dice Roll: Two dice are rolled simultaneously in the final round. The sum is 11 for two combinations ($(5,6), (6,5)$) and 12 for one combination ($(6,6)$). Find the probability of rolling an 11 or 12.
- **Hands-On Manipulative Stage (Two-Dice Grid Mat):** Map the $6 \times 6$ grid of 36 equally likely outcomes. Highlight the 3 winning combinations in the top-right corner.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_04:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_04:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3` | $0$ | $0$ | $0$ | $3$ | Key in favorable combinations count (sums of 11 and 12: 3 pairs) |
| `{{key:ENTER}}` | $0$ | $0$ | $3$ | $3$ | Stack lifts; favorable combinations locked into Register $Y$ |
| `36` | $0$ | $0$ | $3$ | $36$ | Key in total sample space combinations ($6 \times 6 = 36$) |
| `{{key:÷}}` | $0$ | $0$ | $0$ | $0.0833$ | Divide favorable by total combinations ($3/36 \approx 0.0833$) |

- **Diagnostic Checkpoint:** Register $X$ displays $0.0833$. Probability of rolling 11 or 12 is $\mathbf{0.0833}$ ($\approx 8.33\%$).

#### Challenge 5: Complementary Probability
- **Tournament Context:** Complementary Event Probability: The championship venue weather report indicates a $35\%$ probability of rain ($P = 0.35$). Determine the complementary probability of fair weather ($P' = 1 - P$).
- **Hands-On Manipulative Stage (Complementary Spinner):** Inspect the circular probability spinner with 100 divisions. Shading 35 sectors for rain leaves 65 unshaded sectors for fair weather, grounding $1 - P$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_05:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_05:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1` | $0$ | $0$ | $0$ | $1$ | Key in total probability sample space ($1.00 = 100\%$) |
| `{{key:ENTER}}` | $0$ | $0$ | $1$ | $1$ | Stack lifts; total certainty locked into Register $Y$ |
| `0.35` | $0$ | $0$ | $1$ | $0.35$ | Key in rain probability ($0.35$) |
| `{{key:-}}` | $0$ | $0$ | $0$ | $0.65$ | Deduct rain probability from total space to find complementary dry odds |

- **Diagnostic Checkpoint:** Register $X$ displays $0.6500$. Complementary probability of fair weather is $\mathbf{0.6500}$ ($65\%$).

---

### Expedition 2: The Prime Number Fortress & Sieve (Challenges 6–18)
*Mission Briefing: Journey into the heart of number theory. Test for prime numbers using rectangular resistance, unlock prime factor trees, find greatest common factors and least common multiples, and verify the Secret Partner Rule across the ancient Prime Number Fortress.*

#### Challenge 6: Prime Fortress Outer Gate Cipher: Primality of 83
- **Fortress Context:** The outer massive gate of the Prime Fortress opens only when presented with an indivisible prime credential. Test candidate code 83 for primality.
- **Hands-On Manipulative Stage (Counting Tiles):** Take 83 tiles. Attempt to assemble them into rectangular matrices of 2, 3, 5, or 7 rows. Every arrangement leaves uneven remainders; 83 forms only a single linear row of $1 \times 83$, proving rectangular resistance.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_06:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_06:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `83` | $0$ | $0$ | $0$ | $83$ | Key in candidate fortress key code 83 |
| `{{key:PRIME}}` | $0$ | $0$ | $0$ | $1$ | Execute primality test: status line flashes `PRIME`, pushes 1 to Register $X$ |

- **Diagnostic Checkpoint:** Status line flashes `PRIME`; Register $X = \mathbf{1}$. Outer gate cipher unlocks!

#### Challenge 7: Prime Fortress Barbican Trap Door: Primality of 91
- **Fortress Context:** The fortress barbican is guarded by a deceptive trap door set to trigger on composite impostor codes. Evaluate candidate code 91.
- **Hands-On Manipulative Stage (Rectangular Factoring):** Take 91 tiles. Arrange them into rows of 7: exactly 13 rows form a seamless $7 \times 13$ rectangular array with zero gaps, exposing 91 as composite.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_07:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_07:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `91` | $0$ | $0$ | $0$ | $91$ | Key in candidate barbican code 91 |
| `{{key:PRIME}}` | $0$ | $0$ | $0$ | $0$ | Execute primality test: status line flashes `COMPOSITE`, pushes 0 to Register $X$ |

- **Diagnostic Checkpoint:** Status line flashes `COMPOSITE`; Register $X = \mathbf{0}$ ($91 = 7 \times 13$). Barbican trap door disarmed!

#### Challenge 8: Prime Fortress Moat Portcullis: Primality of 143
- **Fortress Context:** The iron portcullis over the fortress moat evaluates candidate 143. Determine if the credential is prime or composite.
- **Hands-On Manipulative Stage (Rectangular Arrays):** Take 143 tiles. Dividing across 11 columns yields exactly 13 rows ($11 \times 13 = 143$), confirming multiple factor pairs beyond 1 and itself.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_08:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_08:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `143` | $0$ | $0$ | $0$ | $143$ | Key in moat portcullis candidate 143 |
| `{{key:PRIME}}` | $0$ | $0$ | $0$ | $0$ | Execute primality test: status line flashes `COMPOSITE`, pushes 0 to Register $X$ |

- **Diagnostic Checkpoint:** Status line flashes `COMPOSITE`; Register $X = \mathbf{0}$ ($143 = 11 \times 13$). Portcullis barrier confirmed!

#### Challenge 9: Prime Fortress Armory Key: Prime Factorization of 72
- **Fortress Context:** The fortress armory lock requires the exact prime decomposition string of tumbler code 72. Decompose 72 into prime factors.
- **Hands-On Manipulative Stage (Logarithmic Prime Blocks):** Take three Blue 2-blocks ($2^3 = 8$) and two Amber 3-blocks ($3^2 = 9$). Stack them vertically against the calibrated back-wall slide rule: the combined height aligns precisely with index 72.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_09:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_09:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `72` | $0$ | $0$ | $0$ | $72$ | Key in armory tumbler code 72 |
| `{{key:FACT}}` | $0$ | $0$ | $0$ | $2^3 \times 3^2$ | Execute prime factorization: graphic screen renders prime decomposition string |

- **Diagnostic Checkpoint:** Graphic screen renders **`2³ × 3²`**. Armory lock disengages!

#### Challenge 10: Prime Fortress Citadel Key: Prime Factorization of 210
- **Fortress Context:** The inner citadel vault is sealed with master product code 210. Find its complete prime factor decomposition.
- **Hands-On Manipulative Stage (Consecutive Prime Blocks):** Select one 2-block, one 3-block, one 5-block, and one 7-block. Stacking these four distinct prime towers models the square-free product $2 \times 3 \times 5 \times 7 = 210$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_10:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_10:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `210` | $0$ | $0$ | $0$ | $210$ | Key in citadel vault code 210 |
| `{{key:FACT}}` | $0$ | $0$ | $0$ | $2 \times 3 \times 5 \times 7$ | Execute prime factorization: graphic screen renders four-prime string |

- **Diagnostic Checkpoint:** Graphic screen renders **`2 × 3 × 5 × 7`**. Citadel vault credential accepted!

#### Challenge 11: Prime Fortress High Tower Vault Key: Prime Factorization of 504
- **Fortress Context:** The high observatory tower is protected by an astronomical key code of 504. Determine its prime factor components.
- **Hands-On Manipulative Stage (Prime Factor Tree):** Factor 504 using prime blocks: three 2-blocks ($2^3 = 8$), two 3-blocks ($3^2 = 9$), and one 7-block ($7$). Product: $8 \times 9 \times 7 = 504$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_11:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_11:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `504` | $0$ | $0$ | $0$ | $504$ | Key in high tower vault code 504 |
| `{{key:FACT}}` | $0$ | $0$ | $0$ | $2^3 \times 3^2 \times 7$ | Execute prime factorization: graphic screen displays canonical factor string |

- **Diagnostic Checkpoint:** Graphic screen renders **`2³ × 3² × 7`**. High tower observatory unsealed!

#### Challenge 12: Fortress Twin Bastions Gear Synchronization: $\gcd(48, 72)$
- **Fortress Context:** Twin drawbridge drive winches with 48 teeth and 72 teeth must mesh via a common drive gear. Find the greatest common factor $\gcd(48, 72)$.
- **Hands-On Manipulative Stage (Venn Intersection):** Model $48 = 2^4 \times 3$ and $72 = 2^3 \times 3^2$. Place shared prime blocks into the central intersection well: three 2-blocks and one 3-block $\implies 2^3 \times 3 = 24$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_12:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_12:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `48` | $0$ | $0$ | $0$ | $48$ | Key in first winch tooth count ($48$) |
| `{{key:ENTER}}` | $0$ | $0$ | $48$ | $48$ | Stack lifts; 48 locked into Register $Y$ |
| `72` | $0$ | $0$ | $48$ | $72$ | Key in second winch tooth count ($72$) |
| `{{key:GCF}}` | $0$ | $0$ | $0$ | $24$ | Execute hardware GCF engine to extract greatest common divisor |

- **Diagnostic Checkpoint:** Register $X$ displays $24.0000$. Maximum shared drive gear size is $\mathbf{24\text{ teeth}}$.

#### Challenge 13: Fortress Water Gate Sluice Synchronization: $\gcd(84, 140)$
- **Fortress Context:** Two hydraulic sluice floodgates operate on cycles of 84 seconds and 140 seconds. Find the greatest common synchronization interval $\gcd(84, 140)$.
- **Hands-On Manipulative Stage (Factor Block Overlap):** Factor $84 = 2^2 \times 3 \times 7$ and $140 = 2^2 \times 5 \times 7$. Shared intersection: two 2-blocks and one 7-block $\implies 2^2 \times 7 = 28$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_13:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_13:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `84` | $0$ | $0$ | $0$ | $84$ | Key in first sluice cycle ($84\text{ s}$) |
| `{{key:ENTER}}` | $0$ | $0$ | $84$ | $84$ | Stack lifts; 84 locked into Register $Y$ |
| `140` | $0$ | $0$ | $84$ | $140$ | Key in second sluice cycle ($140\text{ s}$) |
| `{{key:GCF}}` | $0$ | $0$ | $0$ | $28$ | Execute hardware GCF engine to find greatest common factor |

- **Diagnostic Checkpoint:** Register $X$ displays $28.0000$. Sluice synchronization step is $\mathbf{28\text{ seconds}}$.

#### Challenge 14: Fortress Sentry Patrol Synchronization: $\operatorname{lcm}(15, 20)$
- **Fortress Context:** Two rampart sentry patrols cycle every 15 minutes and 20 minutes respectively. Find the least common multiple $\operatorname{lcm}(15, 20)$ when both sentries meet at the gate.
- **Hands-On Manipulative Stage (Venn Union):** Model $15 = 3 \times 5$ and $20 = 2^2 \times 5$. The union takes maximum powers: two 2-blocks, one 3-block, and one 5-block $\implies 2^2 \times 3 \times 5 = 60$. Stacking blocks aligns with mark 60.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_14:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_14:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `15` | $0$ | $0$ | $0$ | $15$ | Key in first sentry patrol interval ($15\text{ min}$) |
| `{{key:ENTER}}` | $0$ | $0$ | $15$ | $15$ | Stack lifts; 15 locked into Register $Y$ |
| `20` | $0$ | $0$ | $15$ | $20$ | Key in second sentry patrol interval ($20\text{ min}$) |
| `{{key:LCM}}` | $0$ | $0$ | $0$ | $60$ | Execute hardware LCM engine to find least common multiple |

- **Diagnostic Checkpoint:** Register $X$ displays $60.0000$. Sentries meet at the gate every $\mathbf{60\text{ minutes}}$ ($1\text{ hour}$).

#### Challenge 15: Fortress Signal Beacon Cycle: $\operatorname{lcm}(12, 18)$
- **Fortress Context:** Two optical signal beacons on the fortress bastions flash at intervals of 12 seconds and 18 seconds. Find the least common interval $\operatorname{lcm}(12, 18)$ when both flash in unison.
- **Hands-On Manipulative Stage (Prime Union):** Decompose $12 = 2^2 \times 3$ and $18 = 2 \times 3^2$. The union of prime blocks takes two 2-blocks and two 3-blocks $\implies 4 \times 9 = 36$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_15:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_15:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `12` | $0$ | $0$ | $0$ | $12$ | Key in first beacon flash interval ($12\text{ s}$) |
| `{{key:ENTER}}` | $0$ | $0$ | $12$ | $12$ | Stack lifts; 12 locked into Register $Y$ |
| `18` | $0$ | $0$ | $12$ | $18$ | Key in second beacon flash interval ($18\text{ s}$) |
| `{{key:LCM}}` | $0$ | $0$ | $0$ | $36$ | Execute hardware LCM engine to calculate least common multiple |

- **Diagnostic Checkpoint:** Register $X$ displays $36.0000$. Beacons flash simultaneously every $\mathbf{36\text{ seconds}}$.

#### Challenge 16: Fortress Archival Seal: The Secret Partner Rule for 18 and 24
- **Fortress Context:** The grand seal of the Prime Fortress verifies that for any pair $a = 18, b = 24$, the product of their greatest common factor and least common multiple equals their arithmetic product: $\gcd(a,b) \times \operatorname{lcm}(a,b) = a \times b$.
- **Hands-On Manipulative Stage (Secret Partner Rule with Blocks):** Compute $18 \times 24 = 432$. The shared intersection ($\gcd = 6$) multiplied by the total union ($\operatorname{lcm} = 72$) yields $6 \times 72 = 432$, proving conservation of prime factors.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_16:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_16:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `18` | $0$ | $0$ | $0$ | $18$ | Key in first fortress parameter 18 |
| `{{key:ENTER}}` | $0$ | $0$ | $18$ | $18$ | Stack lifts; 18 locked into Register $Y$ |
| `24` | $0$ | $0$ | $18$ | $24$ | Key in second parameter 24 |
| `{{key:GCF}}` | $0$ | $0$ | $0$ | $6$ | Compute greatest common factor $\gcd(18, 24) = 6$ |
| `18` | $0$ | $0$ | $6$ | $18$ | Key in parameter 18; GCF lifts to Register $Y$ |
| `{{key:ENTER}}` | $0$ | $6$ | $18$ | $18$ | Stack lifts; 18 locked into Register $Y$, 6 into Register $Z$ |
| `24` | $0$ | $6$ | $18$ | $24$ | Key in parameter 24 |
| `{{key:LCM}}` | $0$ | $0$ | $6$ | $72$ | Compute least common multiple $\operatorname{lcm}(18, 24) = 72$; GCF remains in Register $Y$ |
| `{{key:×}}` | $0$ | $0$ | $0$ | $432$ | Multiply GCF by LCM ($6 \times 72 = 432$) |

- **Diagnostic Checkpoint:** Register $X$ displays $432.0000$. Secret partner rule holds identically ($18 \times 24 = 432$).

#### Challenge 17: Fortress Supply Depot Allocation: Euclidean Division $148 \div 32$
- **Fortress Context:** In the fortress provisions depot, 148 ration packs are organized into standard field cases holding 32 packs each. Find the number of full cases packed and remaining loose packs using `{{key:÷R}}`.
- **Hands-On Manipulative Stage (Tray Allocation):** Distribute 148 tokens into trays of 32. Exactly 4 trays are completely filled ($4 \times 32 = 128$), leaving 20 loose tokens on the packing bench.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_17:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_17:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `148` | $0$ | $0$ | $0$ | $148$ | Key in total ration packs dividend ($148$) |
| `{{key:ENTER}}` | $0$ | $0$ | $148$ | $148$ | Stack lifts; dividend locked into Register $Y$ |
| `32` | $0$ | $0$ | $148$ | $32$ | Key in case capacity divisor ($32$) |
| `{{key:÷R}}` | $0$ | $0$ | $20$ | $4$ | Execute Euclidean division: quotient 4 in $X$, remainder 20 in $Y$ |

- **Diagnostic Checkpoint:** Register $X$ displays $4$ (Quotient), Register $Y$ displays $20$ (Remainder). 4 full cases packed with 20 leftover packs.

#### Challenge 18: Fortress Treasury Safe Cipher Wheel: $\gcd(24, 36)$
- **Fortress Context:** The fortress treasury safe wheel requires identifying the greatest shared factor of 24 and 36 to engage the master locking tumblers.
- **Hands-On Manipulative Stage (Factor Sorting):** List all divisors: for 24: $\{1, 2, 3, 4, 6, 8, 12, 24\}$; for 36: $\{1, 2, 3, 4, 6, 9, 12, 18, 36\}$. The shared common factor set is $\{1, 2, 3, 4, 6, 12\}$, with greatest factor 12.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_18:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_18:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `24` | $0$ | $0$ | $0$ | $24$ | Key in first tumbler parameter 24 |
| `{{key:ENTER}}` | $0$ | $0$ | $24$ | $24$ | Stack lifts; 24 locked into Register $Y$ |
| `36` | $0$ | $0$ | $24$ | $36$ | Key in second tumbler parameter 36 |
| `{{key:GCF}}` | $0$ | $0$ | $0$ | $12$ | Execute hardware GCF engine to extract greatest common divisor |

- **Diagnostic Checkpoint:** Register $X$ displays $12.0000$. Treasury master tumbler code is $\mathbf{12}$.

---


### Expedition 3: The Data Detective & Bell-Curve Mystery (Challenges 19–26)
*Mission Briefing: Accumulate datasets into the statistical memory registers. Compute measures of center (mean, median, mode) and measures of spread (range, IQR, MAD) to characterize real-world measurements.*

#### Challenge 19: Mean of 4 Test Scores
- **Data Detective Context:** Science Evaluation Analysis: You score 88, 92, 79, and 95 on four consecutive science tests. Calculate your arithmetic mean $\bar{x}$.
- **Hands-On Manipulative Stage (Balance Beam Pegs):** Place pegs at marks 88, 92, 79, and 95 on the numerical balance beam. The beam balances in perfect horizontal equilibrium at the fulcrum point $88.5$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_19:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_19:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0$ | $0$ | $0$ | $0$ | Reset statistical registers ($n = 0, \Sigma x = 0$) |
| `88` | $0$ | $0$ | $0$ | $88$ | Key in first test score 88 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $1$ | Accumulate score ($n = 1, \Sigma x = 88$) |
| `92` | $0$ | $0$ | $1$ | $92$ | Key in second test score 92 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $2$ | Accumulate score ($n = 2, \Sigma x = 180$) |
| `79` | $0$ | $0$ | $2$ | $79$ | Key in third test score 79 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $3$ | Accumulate score ($n = 3, \Sigma x = 259$) |
| `95` | $0$ | $0$ | $3$ | $95$ | Key in fourth test score 95 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $4$ | Accumulate score ($n = 4, \Sigma x = 354$) |
| `{{key:x̄}}` | $0$ | $4$ | $0$ | $88.5$ | Compute sample mean $\bar{x} = 354 / 4 = 88.5$; sample size $n=4$ stored in $Z$ |

- **Diagnostic Checkpoint:** Register $X$ displays $88.5000$. Mean score is $\mathbf{88.50}$.

#### Challenge 20: Median of an Odd Dataset
- **Data Detective Context:** Sprint Velocity Analysis: Five track athletes record 100m sprint times: $12.4, 12.8, 13.1, 13.5, 14.0\text{ seconds}$. Find the median running time.
- **Hands-On Manipulative Stage (Ordered Number Ribbon):** Arrange five runner cards in ascending order along the desk. The third card sits precisely in the middle with two cards on each side, isolating the median at $13.1\text{ s}$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_20:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_20:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0$ | $0$ | $0$ | $0$ | Clear statistical memory ($n = 0$) |
| `12.4` | $0$ | $0$ | $0$ | $12.4$ | Key in sprint time 12.4 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $1$ | Deposit into statistical register ($n = 1$) |
| `12.8` | $0$ | $0$ | $1$ | $12.8$ | Key in sprint time 12.8 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $2$ | Deposit into statistical register ($n = 2$) |
| `13.1` | $0$ | $0$ | $2$ | $13.1$ | Key in sprint time 13.1 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $3$ | Deposit into statistical register ($n = 3$) |
| `13.5` | $0$ | $0$ | $3$ | $13.5$ | Key in sprint time 13.5 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $4$ | Deposit into statistical register ($n = 4$) |
| `14.0` | $0$ | $0$ | $4$ | $14.0$ | Key in sprint time 14.0 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $5$ | Deposit into statistical register ($n = 5$) |
| `{{key:MED}}` | $0$ | $0$ | $5$ | $13.1$ | Compute median value across odd dataset ($n = 5$ in $Y$) |

- **Diagnostic Checkpoint:** Register $X$ displays $13.1000$. Median sprint time is $\mathbf{13.10\text{ seconds}}$.

#### Challenge 21: Median of an Even Dataset
- **Data Detective Context:** Environmental Temperature Monitoring: Six ambient temperatures are recorded: $68, 72, 74, 76, 80, 84^\circ\text{F}$. Find the median temperature (average of two central elements 74 and 76).
- **Hands-On Manipulative Stage (Even Distribution Strip):** Arrange the six data cards in order. Because $n = 6$ is even, there is no single middle card; fold the middle pair (74 and 76) to find their midpoint: $\frac{74+76}{2} = 75^\circ\text{F}$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_21:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_21:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0$ | $0$ | $0$ | $0$ | Reset statistical registers ($n = 0$) |
| `68` | $0$ | $0$ | $0$ | $68$ | Key in temperature 68 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $1$ | Accumulate observation ($n = 1$) |
| `72` | $0$ | $0$ | $1$ | $72$ | Key in temperature 72 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $2$ | Accumulate observation ($n = 2$) |
| `74` | $0$ | $0$ | $2$ | $74$ | Key in temperature 74 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $3$ | Accumulate observation ($n = 3$) |
| `76` | $0$ | $0$ | $3$ | $76$ | Key in temperature 76 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $4$ | Accumulate observation ($n = 4$) |
| `80` | $0$ | $0$ | $4$ | $80$ | Key in temperature 80 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $5$ | Accumulate observation ($n = 5$) |
| `84` | $0$ | $0$ | $5$ | $84$ | Key in temperature 84 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $6$ | Accumulate observation ($n = 6$) |
| `{{key:MED}}` | $0$ | $0$ | $6$ | $75$ | Evaluate median of even dataset: $\frac{74+76}{2} = 75$ ($n=6$ in $Y$) |

- **Diagnostic Checkpoint:** Register $X$ displays $75.0000$. Median temperature is $\mathbf{75.00^\circ\text{F}}$.

#### Challenge 22: Mode of a Shoe Size Survey
- **Data Detective Context:** Footwear Inventory Survey: Shoe sizes collected from 8 customers: $6, 7, 7, 7, 8, 8, 9, 10$. Find the statistical mode (most frequent size).
- **Hands-On Manipulative Stage (Frequency Column Histogram):** Stack counting cubes for each size. Size 7 forms the tallest column with 3 cubes, visually standing out as the statistical mode.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_22:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_22:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0$ | $0$ | $0$ | $0$ | Clear statistical accumulator ($n = 0$) |
| `{{key:6}}` | $0$ | $0$ | $0$ | $6$ | Key in shoe size 6 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $1$ | Accumulate entry ($n = 1$) |
| `{{key:7}}` | $0$ | $0$ | $1$ | $7$ | Key in shoe size 7 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $2$ | Accumulate entry ($n = 2$) |
| `{{key:7}}` | $0$ | $0$ | $2$ | $7$ | Key in second shoe size 7 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $3$ | Accumulate entry ($n = 3$) |
| `{{key:7}}` | $0$ | $0$ | $3$ | $7$ | Key in third shoe size 7 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $4$ | Accumulate entry ($n = 4$) |
| `{{key:8}}` | $0$ | $0$ | $4$ | $8$ | Key in shoe size 8 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $5$ | Accumulate entry ($n = 5$) |
| `{{key:8}}` | $0$ | $0$ | $5$ | $8$ | Key in second shoe size 8 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $6$ | Accumulate entry ($n = 6$) |
| `{{key:9}}` | $0$ | $0$ | $6$ | $9$ | Key in shoe size 9 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $7$ | Accumulate entry ($n = 7$) |
| `10` | $0$ | $0$ | $7$ | $10$ | Key in shoe size 10 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $8$ | Accumulate entry ($n = 8$) |
| `{{key:MODE}}` | $0$ | $0$ | $8$ | $7$ | Identify statistical mode across sample ($X = 7$, $n=8$ in $Y$) |

- **Diagnostic Checkpoint:** Register $X$ displays $7.0000$. Most common shoe size (mode) is $\mathbf{7.00}$.

#### Challenge 23: Range of High Temperatures
- **Data Detective Context:** Weather Station Spread Analysis: Weekly maximum temperatures: $62, 65, 78, 81, 74, 69, 85^\circ\text{F}$. Calculate the temperature range ($\max - \min = 85 - 62$).
- **Hands-On Manipulative Stage (Range Slider):** Pin the minimum temperature ($62^\circ$) and maximum temperature ($85^\circ$) on a number line strip. The distance spanned between the extremes measures $23^\circ$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_23:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_23:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0$ | $0$ | $0$ | $0$ | Reset statistical registers ($n = 0$) |
| `62` | $0$ | $0$ | $0$ | $62$ | Key in temperature 62 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $1$ | Accumulate observation ($n = 1$) |
| `65` | $0$ | $0$ | $1$ | $65$ | Key in temperature 65 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $2$ | Accumulate observation ($n = 2$) |
| `78` | $0$ | $0$ | $2$ | $78$ | Key in temperature 78 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $3$ | Accumulate observation ($n = 3$) |
| `81` | $0$ | $0$ | $3$ | $81$ | Key in temperature 81 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $4$ | Accumulate observation ($n = 4$) |
| `74` | $0$ | $0$ | $4$ | $74$ | Key in temperature 74 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $5$ | Accumulate observation ($n = 5$) |
| `69` | $0$ | $0$ | $5$ | $69$ | Key in temperature 69 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $6$ | Accumulate observation ($n = 6$) |
| `85` | $0$ | $0$ | $6$ | $85$ | Key in temperature 85 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $7$ | Accumulate observation ($n = 7$) |
| `{{key:RNG}}` | $0$ | $0$ | $7$ | $23$ | Compute range ($\max - \min = 85 - 62 = 23$) |

- **Diagnostic Checkpoint:** Register $X$ displays $23.0000$. Weekly temperature range is $\mathbf{23.00^\circ\text{F}}$.

#### Challenge 24: Interquartile Range of Daily Rainfall
- **Data Detective Context:** Precipitation Variance: Weekly rainfall measurements: $0.1, 0.2, 0.4, 0.6, 0.9, 1.2, 1.5\text{ inches}$. Find the interquartile range ($Q_3 - Q_1$).
- **Hands-On Manipulative Stage (Box-and-Whisker Plot Mat):** Divide the sorted 7-point rainfall dataset into lower and upper quartiles. Mark $Q_1 = 0.2$ and $Q_3 = 1.2$; the width of the middle $50\%$ box spans the interquartile range.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_24:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_24:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0$ | $0$ | $0$ | $0$ | Reset statistical memory ($n = 0$) |
| `0.1` | $0$ | $0$ | $0$ | $0.1$ | Key in rainfall 0.1 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $1$ | Accumulate point ($n = 1$) |
| `0.2` | $0$ | $0$ | $1$ | $0.2$ | Key in rainfall 0.2 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $2$ | Accumulate point ($n = 2$) |
| `0.4` | $0$ | $0$ | $2$ | $0.4$ | Key in rainfall 0.4 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $3$ | Accumulate point ($n = 3$) |
| `0.6` | $0$ | $0$ | $3$ | $0.6$ | Key in rainfall 0.6 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $4$ | Accumulate point ($n = 4$) |
| `0.9` | $0$ | $0$ | $4$ | $0.9$ | Key in rainfall 0.9 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $5$ | Accumulate point ($n = 5$) |
| `1.2` | $0$ | $0$ | $5$ | $1.2$ | Key in rainfall 1.2 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $6$ | Accumulate point ($n = 6$) |
| `1.5` | $0$ | $0$ | $6$ | $1.5$ | Key in rainfall 1.5 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $7$ | Accumulate point ($n = 7$) |
| `{{key:IQR}}` | $0$ | $0$ | $7$ | $0.75$ | Compute interquartile range ($Q_3 - Q_1 = 0.75$) |

- **Diagnostic Checkpoint:** Register $X$ displays $0.7500$. Interquartile range of rainfall is $\mathbf{0.75\text{ inches}}$.

#### Challenge 25: Mean Absolute Deviation of a 5-Point Dataset
- **Data Detective Context:** Sensor Error Analysis: A 5-point dataset: $10, 15, 20, 25, 30$ has mean $\bar{x} = 20.0$. Deviations from mean are $|-10|, |-5|, |0|, |+5|, |+10|$. Sum of deviations $= 30$. Find the Mean Absolute Deviation ($\text{MAD} = 30 / 5 = 6.0$).
- **Hands-On Manipulative Stage (Distance From Mean Strip):** Lay out the points on a number line. Measure the physical distance from each point to the center mark 20: $10 + 5 + 0 + 5 + 10 = 30$. Dividing by 5 yields the average distance from center.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_25:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_25:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0$ | $0$ | $0$ | $0$ | Clear statistical accumulator ($n = 0$) |
| `10` | $0$ | $0$ | $0$ | $10$ | Key in data point 10 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $1$ | Deposit into accumulator ($n = 1$) |
| `15` | $0$ | $0$ | $1$ | $15$ | Key in data point 15 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $2$ | Deposit into accumulator ($n = 2$) |
| `20` | $0$ | $0$ | $2$ | $20$ | Key in data point 20 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $3$ | Deposit into accumulator ($n = 3$) |
| `25` | $0$ | $0$ | $3$ | $25$ | Key in data point 25 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $4$ | Deposit into accumulator ($n = 4$) |
| `30` | $0$ | $0$ | $4$ | $30$ | Key in data point 30 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $5$ | Deposit into accumulator ($n = 5$) |
| `{{key:MAD}}` | $0$ | $0$ | $5$ | $6$ | Compute Mean Absolute Deviation ($\text{MAD} = 6$) |

- **Diagnostic Checkpoint:** Register $X$ displays $6.0000$. Mean Absolute Deviation is $\mathbf{6.00}$.

#### Challenge 26: Frequency of Score 85
- **Data Detective Context:** Scorecard Frequency Binning: In survey dataset $70, 75, 80, 80, 85, 85, 85, 90, 90, 95$, accumulate observation 85 and inspect active sample counter.
- **Hands-On Manipulative Stage (Dot Plot Counter Grid):** Place a token into the score 85 column. The stack records the entry into the statistical registers.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_26:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_26:value}}`**
- **4-Register Stack Trace Table:**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `85` | $0$ | $0$ | $0$ | $85$ | Key in observed test score 85 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $1$ | Accumulate score into statistical register ($n = 1$) |

- **Diagnostic Checkpoint:** Register $X$ displays $1$. Single observation of score 85 registered in sample bin.

---

### Expedition 4: The Zero-Pair Vault & Pre-Algebra Ascent (Challenges 27–65)
*Mission Briefing: Model positive and negative integers with two-color zero pairs, master spatial sign negation, and solve pre-algebra expressions across powers, roots, and randomized ranges.*

#### Challenge 27: Adding Directed Negative Numbers
- **Problem:** Evaluate $(-15) + (-28)$.
- **Manipulative Stage:** Place 15 red debt tokens on the workspace. Add 28 more red debt tokens alongside them. Count the accumulated total of 43 red tokens, representing directed deficit $(-43)$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_27:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_27:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `15` | $0$ | $0$ | $0$ | $15$ | Key in first magnitude 15 |
| `{{key:+/-}}` | $0$ | $0$ | $0$ | $-15$ | Negate to represent directed quantity $-15$ |
| `{{key:ENTER}}` | $0$ | $0$ | $-15$ | $-15$ | Push $-15$ into Register $Y$ |
| `28` | $0$ | $0$ | $-15$ | $28$ | Key in second magnitude 28 |
| `{{key:+/-}}` | $0$ | $0$ | $-15$ | $-28$ | Negate to represent directed quantity $-28$ |
| `{{key:+}}` | $0$ | $0$ | $0$ | $-43$ | Add $-15 + (-28) = -43$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $-43$. Adding two negative quantities accumulates total magnitude while preserving the negative sign.

#### Challenge 28: Subtracting a Larger Positive Number
- **Problem:** A bank account has $\$45$. An automatic withdrawal of $\$70$ occurs. What is the balance?
- **Manipulative Stage:** Place 45 green credit tokens in a dish. To remove 70 tokens, pair 45 green tokens with 45 red debt tokens (forming zero pairs), then add 25 additional red debt tokens. Removing 70 tokens leaves 25 red debt tokens ($-25$).
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_28:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_28:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `45` | $0$ | $0$ | $0$ | $45$ | Key in starting balance $\$45$ |
| `{{key:ENTER}}` | $0$ | $0$ | $45$ | $45$ | Push $\$45$ into Register $Y$ |
| `70` | $0$ | $0$ | $45$ | $70$ | Key in withdrawal amount $\$70$ |
| `{{key:-}}` | $0$ | $0$ | $0$ | $-25$ | Subtract $45 - 70 = -25$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $-25$. Account is overdrawn by $\$25$.

#### Challenge 29: Subtracting a Negative Number
- **Problem:** Evaluate $12 - (-18)$.
- **Manipulative Stage:** Place 12 yellow positive tiles on the board. To subtract 18 negative red tiles, introduce 18 zero pairs (+18 yellow and -18 red). Physically remove the 18 red tiles. Exactly $12 + 18 = 30$ yellow tiles remain.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_29:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_29:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `12` | $0$ | $0$ | $0$ | $12$ | Key in starting number 12 |
| `{{key:ENTER}}` | $0$ | $0$ | $12$ | $12$ | Push 12 into Register $Y$ |
| `18` | $0$ | $0$ | $12$ | $18$ | Key in second number magnitude 18 |
| `{{key:+/-}}` | $0$ | $0$ | $12$ | $-18$ | Negate second number to $-18$ |
| `{{key:-}}` | $0$ | $0$ | $0$ | $30$ | Subtract $12 - (-18) = 12 + 18 = 30$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $30$. Subtracting a negative is mathematically and physically identical to adding its positive opposite.

#### Challenge 30: Multiplying Signed Numbers (Negative times Negative)
- **Problem:** Evaluate $(-7) \times (-8)$.
- **Manipulative Stage:** On a coordinate grid, establish positive orientation. Multiplying by a negative factor reverses direction $180^\circ$ into negative territory. Multiplying by a second negative factor reverses direction another $180^\circ$, returning to positive orientation $+56$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_30:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_30:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `7` | $0$ | $0$ | $0$ | $7$ | Key in first factor magnitude 7 |
| `{{key:+/-}}` | $0$ | $0$ | $0$ | $-7$ | Negate to $-7$ |
| `{{key:ENTER}}` | $0$ | $0$ | $-7$ | $-7$ | Push $-7$ into Register $Y$ |
| `8` | $0$ | $0$ | $-7$ | $8$ | Key in second factor magnitude 8 |
| `{{key:+/-}}` | $0$ | $0$ | $-7$ | $-8$ | Negate to $-8$ |
| `{{key:×}}` | $0$ | $0$ | $0$ | $56$ | Multiply $(-7) \times (-8) = 56$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $56$. The product of two negative factors evaluates to a positive result.

#### Challenge 31: Dividing Signed Numbers (Negative divided by Positive)
- **Problem:** Evaluate $(-72) \div (+9)$.
- **Manipulative Stage:** Take 72 red negative tokens representing a total deficit of $-72$. Partition them evenly into 9 cups. Each cup receives exactly 8 red negative tokens ($-8$).
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_31:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_31:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `72` | $0$ | $0$ | $0$ | $72$ | Key in dividend magnitude 72 |
| `{{key:+/-}}` | $0$ | $0$ | $0$ | $-72$ | Negate to dividend $-72$ |
| `{{key:ENTER}}` | $0$ | $0$ | $-72$ | $-72$ | Push $-72$ into Register $Y$ |
| `9` | $0$ | $0$ | $-72$ | $9$ | Enter positive divisor 9 |
| `{{key:÷}}` | $0$ | $0$ | $0$ | $-8$ | Divide $(-72) \div 9 = -8$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $-8$. Dividing a negative quantity by a positive divisor yields a negative quotient.

#### Challenge 32: Absolute Value of Negative Integer
- **Problem:** Evaluate $|-125|$.
- **Manipulative Stage:** Locate $-125$ on a real number line runner. Measure the distance from 0 to $-125$ using a meter tape. Regardless of direction from the origin, geometric distance is strictly scalar and non-negative: 125 units.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_32:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_32:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `125` | $0$ | $0$ | $0$ | $125$ | Key in integer 125 |
| `{{key:+/-}}` | $0$ | $0$ | $0$ | $-125$ | Negate to $-125$ |
| `{{key:|x|}}` | $0$ | $0$ | $0$ | $125$ | Absolute value operator strips sign; magnitude is 125 |

- **Diagnostic Checkpoint:** Register $X$ displays $125$. Absolute value computes geometric distance from zero.

#### Challenge 33: Absolute Value Expression: $|-18| + |+12|$
- **Problem:** Evaluate $|-18| + |12|$.
- **Manipulative Stage:** Measure distance from $-18$ to 0 (18 units) and distance from 0 to 12 (12 units). Lay both measurement segments end-to-end to obtain a combined distance of 30 units.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_33:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_33:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `18` | $0$ | $0$ | $0$ | $18$ | Key in first value 18 |
| `{{key:+/-}}` | $0$ | $0$ | $0$ | $-18$ | Negate to $-18$ |
| `{{key:|x|}}` | $0$ | $0$ | $0$ | $18$ | Evaluate $|-18| = 18$ |
| `12` | $0$ | $0$ | $18$ | $12$ | Key in second value 12; stack lifts 18 to $Y$ |
| `{{key:|x|}}` | $0$ | $0$ | $18$ | $12$ | Evaluate $|12| = 12$ |
| `{{key:+}}` | $0$ | $0$ | $0$ | $30$ | Sum absolute distances $18 + 12 = 30$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $30$. Sum of magnitudes evaluated without parentheses.

#### Challenge 34: Number Line Distance: Between $-12$ and $+15$
- **Problem:** Find distance between $-12$ and $+15$ on the real line: $|15 - (-12)|$.
- **Manipulative Stage:** Place a peg at $-12$ and a peg at $+15$ on a numbered track. Count the total unit intervals between them: 12 units to reach zero, plus 15 units beyond zero, totaling 27 units.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_34:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_34:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `15` | $0$ | $0$ | $0$ | $15$ | Enter endpoint 15 |
| `{{key:ENTER}}` | $0$ | $0$ | $15$ | $15$ | Push 15 to Register $Y$ |
| `12` | $0$ | $0$ | $15$ | $12$ | Key in start point magnitude 12 |
| `{{key:+/-}}` | $0$ | $0$ | $15$ | $-12$ | Negate to start point coordinate $-12$ |
| `{{key:-}}` | $0$ | $0$ | $0$ | $27$ | Subtract $15 - (-12) = 27$; stack drops |
| `{{key:|x|}}` | $0$ | $0$ | $0$ | $27$ | Confirm positive distance magnitude: $|27| = 27$ |

- **Diagnostic Checkpoint:** Register $X$ displays $27$. Euclidean distance between $-12$ and $+15$ confirmed as 27 units.

#### Challenge 35: Square of Negative Number: $(-9)^2$
- **Problem:** Evaluate $(-9)^2$.
- **Manipulative Stage:** Build a 9-by-9 grid of square tiles. Whether oriented along positive axes or rotated $180^\circ$ into opposite dimensions (negative width times negative height), the bounded physical area comprises 81 positive unit squares.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_35:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_35:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `9` | $0$ | $0$ | $0$ | $9$ | Key in side length 9 |
| `{{key:+/-}}` | $0$ | $0$ | $0$ | $-9$ | Negate to $-9$ |
| `{{key:x²}}` | $0$ | $0$ | $0$ | $81$ | Square in place: $(-9) \times (-9) = 81$ |

- **Diagnostic Checkpoint:** Register $X$ displays $81$. Even powers of negative real numbers evaluate to positive values.

#### Challenge 36: Geometric Square Root: $\sqrt{289}$
- **Problem:** A square plaza has area $289\text{ m}^2$. Find side length.
- **Manipulative Stage:** Take 289 unit square tiles. Assemble them into the largest possible solid square array. Count the number of tiles along one edge: exactly 17 tiles with zero remainder.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_36:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_36:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `289` | $0$ | $0$ | $0$ | $289$ | Enter square plaza area $289\text{ m}^2$ |
| `{{key:√x}}` | $0$ | $0$ | $0$ | $17$ | Extract principal square root: $\sqrt{289} = 17$ |

- **Diagnostic Checkpoint:** Register $X$ displays $17$. Side length of plaza is $17\text{ m}$.

#### Challenge 37: Geometric Square Root: $\sqrt{625}$
- **Problem:** A square chessboard has area $625\text{ cm}^2$. Find side length.
- **Manipulative Stage:** Model area using a 625-square grid overlay. Decompose 625 into prime squares ($25 \times 25$). Verify each dimension equals 25 units.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_37:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_37:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `625` | $0$ | $0$ | $0$ | $625$ | Enter chessboard area $625\text{ cm}^2$ |
| `{{key:√x}}` | $0$ | $0$ | $0$ | $25$ | Extract principal square root: $\sqrt{625} = 25$ |

- **Diagnostic Checkpoint:** Register $X$ displays $25$. Chessboard side length is $25\text{ cm}$.

#### Challenge 38: Random Number in Range 10 to 50
- **Problem:** Generate a random integer between 10 and 50 using `{{key:t…x}}`.
- **Manipulative Stage:** Place 41 numbered tiles (10 through 50) into an opaque urn. Draw one tile at random to model discrete uniform sampling across a bounded interval.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_38:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_38:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `10` | $0$ | $0$ | $0$ | $10$ | Enter lower range limit 10 |
| `{{key:ENTER}}` | $0$ | $0$ | $10$ | $10$ | Push lower bound into Register $Y$ |
| `50` | $0$ | $0$ | $10$ | $50$ | Enter upper range limit 50 |
| `{{key:t…x}}` | $0$ | $0$ | $10$ | $18$ | Generate uniform pseudo-random integer in $[10, 50]$ |

- **Diagnostic Checkpoint:** Register $X$ displays a random integer $r \in [10, 50]$, while Register $Y$ preserves the lower bound $10$.

#### Challenge 39: Prime Twin Pair Verification: $(29, 31)$
- **Problem:** Verify that 29 and 31 are twin primes and find their sum.
- **Manipulative Stage:** Attempt to arrange 29 unit tiles into rectangular arrays with 2 or more rows; only $1 \times 29$ forms. Repeat with 31 tiles; only $1 \times 31$ forms. Both are prime, separated by 2 units.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_39:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_39:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `29` | $0$ | $0$ | $0$ | $29$ | Key in first candidate 29 |
| `{{key:PRIME}}` | $0$ | $0$ | $0$ | $29$ | LCD flashes `PRIME`; preserves 29 in Register $X$ |
| `31` | $0$ | $0$ | $29$ | $31$ | Key in second candidate 31; stack lifts 29 to $Y$ |
| `{{key:PRIME}}` | $0$ | $0$ | $29$ | $31$ | LCD flashes `PRIME`; preserves 31 in Register $X$ |
| `{{key:+}}` | $0$ | $0$ | $0$ | $60$ | Sum twin primes $29 + 31 = 60$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $60$. Both numbers verified prime, and their sum is an even integer as predicted by number theory.

#### Challenge 40: Divisibility by 9 Check via Remainder
- **Problem:** Check if 1,557 is divisible by 9 using Euclidean division (`{{key:÷R}}`).
- **Manipulative Stage:** Group 1,557 base-ten blocks into bundles of 900, 630, and 27. Count the bundles (173 groups of 9) and verify that zero individual unit blocks remain.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_40:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_40:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1557` | $0$ | $0$ | $0$ | $1557$ | Key in dividend 1557 |
| `{{key:ENTER}}` | $0$ | $0$ | $1557$ | $1557$ | Push dividend to Register $Y$ |
| `9` | $0$ | $0$ | $1557$ | $9$ | Enter divisor 9 |
| `{{key:÷R}}` | $0$ | $0$ | $0$ | $173$ | Euclidean division: Quotient 173 in $X$, Remainder 0 in $Y$ |

- **Diagnostic Checkpoint:** Register $X$ displays $173$ and Register $Y$ displays $0$. Remainder of 0 confirms exact divisibility by 9 (also confirmed by digit sum $1+5+5+7 = 18$).

#### Challenge 41: LCD of Three Denominators: $\frac{1}{4}, \frac{1}{6}, \frac{1}{10}$
- **Problem:** Find common denominator: $\operatorname{lcm}(\operatorname{lcm}(4, 6), 10)$.
- **Manipulative Stage:** Build towers using colored interlocking cubes: length 4 (red), length 6 (blue), and length 10 (yellow). Extend each train until all three match at identical length: 60 cubes.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_41:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_41:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4` | $0$ | $0$ | $0$ | $4$ | Key in first denominator 4 |
| `{{key:ENTER}}` | $0$ | $0$ | $4$ | $4$ | Push 4 to Register $Y$ |
| `6` | $0$ | $0$ | $4$ | $6$ | Key in second denominator 6 |
| `{{key:LCM}}` | $0$ | $0$ | $0$ | $12$ | Compute $\operatorname{lcm}(4, 6) = 12$ |
| `10` | $0$ | $0$ | $12$ | $10$ | Key in third denominator 10; stack lifts 12 to $Y$ |
| `{{key:LCM}}` | $0$ | $0$ | $0$ | $60$ | Compute $\operatorname{lcm}(12, 10) = 60$ |

- **Diagnostic Checkpoint:** Register $X$ displays $60$. Common denominator for $\frac{1}{4}, \frac{1}{6}, \frac{1}{10}$ is 60.

#### Challenge 42: Temperature Range Across a Sub-Zero Week
- **Problem:** Lowest temperature was $-22^\circ\text{F}$, highest was $+14^\circ\text{F}$. Find total temperature swing.
- **Manipulative Stage:** On a vertical thermometer scale, mark $-22$ below zero and $+14$ above zero. Trace the mercury column rising from $-22$ to 0 (22 degrees) and from 0 to $+14$ (14 degrees), measuring the total thermal excursion: 36 degrees.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_42:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_42:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `14` | $0$ | $0$ | $0$ | $14$ | Enter maximum temperature $+14^\circ$ |
| `{{key:ENTER}}` | $0$ | $0$ | $14$ | $14$ | Push high temperature to Register $Y$ |
| `22` | $0$ | $0$ | $14$ | $22$ | Key in low temperature magnitude 22 |
| `{{key:+/-}}` | $0$ | $0$ | $14$ | $-22$ | Negate to low temperature $-22^\circ$ |
| `{{key:-}}` | $0$ | $0$ | $0$ | $36$ | Subtract $14 - (-22) = 14 + 22 = 36$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $36$. Total temperature variation is $36^\circ\text{F}$.

#### Challenge 43: Submarine Depth Change
- **Problem:** A submarine at depth $-180\text{ m}$ ascends $+65\text{ m}$, then dives $-40\text{ m}$. Find final depth.
- **Manipulative Stage:** Move a depth marker on a vertical bathymetric track: start at $-180\text{ m}$, slide upward $+65\text{ m}$ to $-115\text{ m}$, then slide downward $-40\text{ m}$ to settle at $-155\text{ m}$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_43:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_43:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `180` | $0$ | $0$ | $0$ | $180$ | Key in initial depth magnitude 180 |
| `{{key:+/-}}` | $0$ | $0$ | $0$ | $-180$ | Negate to depth $-180\text{ m}$ |
| `{{key:ENTER}}` | $0$ | $0$ | $-180$ | $-180$ | Push initial depth to Register $Y$ |
| `65` | $0$ | $0$ | $-180$ | $65$ | Key in ascent $+65\text{ m}$ |
| `{{key:+}}` | $0$ | $0$ | $0$ | $-115$ | Add ascent: $-180 + 65 = -115\text{ m}$; stack drops |
| `40` | $0$ | $0$ | $-115$ | $40$ | Key in dive descent $40\text{ m}$; stack lifts $-115$ to $Y$ |
| `{{key:-}}` | $0$ | $0$ | $0$ | $-155$ | Deduct descent: $-115 - 40 = -155\text{ m}$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $-155$. Final depth is $155\text{ m}$ below sea level.

#### Challenge 44: Rolling Double Sixes with Two Dice
- **Problem:** What is the probability of rolling double sixes with two fair six-sided dice ($1$ favorable outcome out of $36$)?
- **Manipulative Stage:** Examine a $6 \times 6$ grid of dice pairings (36 cells). Only one cell represents $(6,6)$. Compute the fractional area occupied by that single cell.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_44:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_44:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1` | $0$ | $0$ | $0$ | $1$ | Key in favorable outcome count 1 |
| `{{key:ENTER}}` | $0$ | $0$ | $1$ | $1$ | Push 1 to Register $Y$ |
| `36` | $0$ | $0$ | $1$ | $36$ | Key in sample space size 36 |
| `{{key:÷}}` | $0$ | $0$ | $0$ | $0.0277777778$ | Divide $1 \div 36 \approx 0.0278$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $0.0277777778$. Probability is approximately $2.78\%$ (or $1/36$).

#### Challenge 45: Probability of Not Rolling a 6 on a Die
- **Problem:** Five faces are not 6. Compute $5/6$.
- **Manipulative Stage:** Set out 6 die faces: {1, 2, 3, 4, 5, 6}. Remove the face labeled 6. The remaining 5 faces represent the complement event ($E'$). Calculate $5/6$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_45:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_45:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `5` | $0$ | $0$ | $0$ | $5$ | Key in non-six favorable outcomes 5 |
| `{{key:ENTER}}` | $0$ | $0$ | $5$ | $5$ | Push 5 to Register $Y$ |
| `6` | $0$ | $0$ | $5$ | $6$ | Key in total possible faces 6 |
| `{{key:÷}}` | $0$ | $0$ | $0$ | $0.8333333333$ | Divide $5 \div 6 \approx 0.8333$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $0.8333333333$. Complementary probability is approximately $83.33\%$.

#### Challenge 46: Prime Factor Decomposition of 1,001
- **Problem:** Decompose 1,001 into prime factors (famous number-theory product).
- **Manipulative Stage:** Build a 3D rectangular prism volume of 1,001 unit cubes. Test factor slicing: the block factors neatly into dimensions $7 \times 11 \times 13$, three distinct consecutive prime numbers.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_46:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_46:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1001` | $0$ | $0$ | $0$ | $1001$ | Key in composite integer 1001 |
| `{{key:FACT}}` | $0$ | $0$ | $0$ | $1001$ | LCD decomposes into prime factors: `7 × 11 × 13` |

- **Diagnostic Checkpoint:** Register $X$ preserves $1001$ while the display shows $7 \times 11 \times 13$.

#### Challenge 47: Prime Factor Decomposition of 1,729 (Hardy-Ramanujan Number)
- **Problem:** Decompose 1,729 into prime factors.
- **Manipulative Stage:** Inspect 1,729, known as the smallest integer expressible as the sum of two cubes in two different ways ($1^3 + 12^3 = 9^3 + 10^3$). Deconstruct it into prime factor blocks: $7 \times 13 \times 19$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_47:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_47:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1729` | $0$ | $0$ | $0$ | $1729$ | Key in integer 1729 |
| `{{key:FACT}}` | $0$ | $0$ | $0$ | $1729$ | LCD decomposes into prime factors: `7 × 13 × 19` |

- **Diagnostic Checkpoint:** Register $X$ preserves $1729$ while the display reveals $7 \times 13 \times 19$, three primes in arithmetic progression with common difference 6.

#### Challenge 48: Weighted Mean of Classroom Grades
- **Problem:** Homework (avg 90, weight 2), Quizzes (avg 82, weight 3), Exam (avg 88, weight 5). Total weight = 10.
- **Manipulative Stage:** On a balance beam, place two 90-gram weights at position 1, three 82-gram weights at position 2, and five 88-gram weights at position 3. Find the center of mass balancing the 10 weights.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_48:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_48:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `90` | $0$ | $0$ | $0$ | $90$ | Key in homework average 90 |
| `{{key:ENTER}}` | $0$ | $0$ | $90$ | $90$ | Push 90 into Register $Y$ |
| `2` | $0$ | $0$ | $90$ | $2$ | Key in homework weight 2 |
| `{{key:×}}` | $0$ | $0$ | $0$ | $180$ | Compute homework points: $90 \times 2 = 180$ |
| `82` | $0$ | $0$ | $180$ | $82$ | Key in quiz average 82; stack lifts 180 to $Y$ |
| `{{key:ENTER}}` | $0$ | $180$ | $82$ | $82$ | Push 82 to $Y$; lifts 180 to $Z$ |
| `3` | $0$ | $180$ | $82$ | $3$ | Key in quiz weight 3 |
| `{{key:×}}` | $0$ | $0$ | $180$ | $246$ | Compute quiz points: $82 \times 3 = 246$; $Z$ drops to $Y$ |
| `{{key:+}}` | $0$ | $0$ | $0$ | $426$ | Accumulate weighted points: $180 + 246 = 426$ |
| `88` | $0$ | $0$ | $426$ | $88$ | Key in exam average 88; stack lifts 426 to $Y$ |
| `{{key:ENTER}}` | $0$ | $426$ | $88$ | $88$ | Push 88 to $Y$; lifts 426 to $Z$ |
| `5` | $0$ | $426$ | $88$ | $5$ | Key in exam weight 5 |
| `{{key:×}}` | $0$ | $0$ | $426$ | $440$ | Compute exam points: $88 \times 5 = 440$; $Z$ drops to $Y$ |
| `{{key:+}}` | $0$ | $0$ | $0$ | $866$ | Total weighted points: $426 + 440 = 866$ |
| `10` | $0$ | $0$ | $866$ | $10$ | Key in total weight 10; stack lifts 866 to $Y$ |
| `{{key:÷}}` | $0$ | $0$ | $0$ | $86.6$ | Divide $866 \div 10 = 86.6$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $86.6$. Weighted mean grade is $86.6\%$.

#### Challenge 49: Goldbach Conjecture Sample Check: $28 = 11 + 17$
- **Problem:** Test if 11 and 17 are both prime and sum to 28.
- **Manipulative Stage:** Lay out 11 yellow unit tiles (prime length) and 17 yellow unit tiles (prime length). Verify neither can be factored into non-trivial rectangles. Join them end-to-end to form a single train of 28 units, demonstrating that even integer 28 decomposes into the sum of two primes.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_49:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_49:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `11` | $0$ | $0$ | $0$ | $11$ | Key in first prime candidate 11 |
| `{{key:PRIME}}` | $0$ | $0$ | $0$ | $11$ | LCD flashes `PRIME`; preserves 11 in Register $X$ |
| `17` | $0$ | $0$ | $11$ | $17$ | Key in second prime candidate 17; stack lifts 11 to $Y$ |
| `{{key:PRIME}}` | $0$ | $0$ | $11$ | $17$ | LCD flashes `PRIME`; preserves 17 in Register $X$ |
| `{{key:+}}` | $0$ | $0$ | $0$ | $28$ | Sum primes $11 + 17 = 28$; stack drops |
| `11` | $0$ | $0$ | $28$ | $11$ | Key in 11 for second partition check; stack lifts 28 to $Y$ |
| `{{key:ENTER}}` | $0$ | $28$ | $11$ | $11$ | Push 11 to $Y$; lifts 28 to $Z$ |
| `17` | $0$ | $28$ | $11$ | $17$ | Key in 17 |
| `{{key:+}}` | $0$ | $0$ | $28$ | $28$ | Sum $11 + 17 = 28$; $Z$ drops to $Y$ |

- **Diagnostic Checkpoint:** Register $X$ displays $28$ and Register $Y$ preserves $28$. Both 11 and 17 confirmed prime, summing to even integer 28.

#### Challenge 50: Net Profit Across 4 Business Quarters
- **Problem:** Q1: $+\$14,500$; Q2: $-\$3,200$; Q3: $+\$8,900$; Q4: $-\$1,400$. Find net annual profit.
- **Manipulative Stage:** On a ledger balance board, place green tokens for credits and red tokens for debits: $+14,500$ green, $-3,200$ red, $+8,900$ green, $-1,400$ red. Pair and cancel red tokens against green tokens to leave net surplus.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_50:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_50:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `14500` | $0$ | $0$ | $0$ | $14500$ | Enter Q1 profit $\$14,500$ |
| `{{key:ENTER}}` | $0$ | $0$ | $14500$ | $14500$ | Push Q1 profit into Register $Y$ |
| `3200` | $0$ | $0$ | $14500$ | $3200$ | Enter Q2 loss $\$3,200$ |
| `{{key:-}}` | $0$ | $0$ | $0$ | $11300$ | Deduct Q2 loss: $14500 - 3200 = 11300$; stack drops |
| `8900` | $0$ | $0$ | $11300$ | $8900$ | Enter Q3 profit $\$8,900$; stack lifts 11300 to $Y$ |
| `{{key:+}}` | $0$ | $0$ | $0$ | $20200$ | Add Q3 profit: $11300 + 8900 = 20200$; stack drops |
| `1400` | $0$ | $0$ | $20200$ | $1400$ | Enter Q4 loss $\$1,400$; stack lifts 20200 to $Y$ |
| `{{key:-}}` | $0$ | $0$ | $0$ | $18800$ | Deduct Q4 loss: $20200 - 1400 = 18800$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $18800$. Net annual profit is $\$18,800.00$.

#### Challenge 51: Compound Probability: Coin Flip and Die Roll
- **Problem:** What is the probability of flipping Heads on a coin AND rolling a 6 on a die? ($P = 1/2 \times 1/6$)
- **Manipulative Stage:** Set up a 2-by-6 grid: 2 coin states (Heads, Tails) times 6 die faces (1 to 6) produces 12 mutually exclusive outcomes. Exactly 1 outcome is (Heads, 6).
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_51:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_51:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1` | $0$ | $0$ | $0$ | $1$ | Key in favorable coin outcome 1 |
| `{{key:ENTER}}` | $0$ | $0$ | $1$ | $1$ | Push 1 into Register $Y$ |
| `2` | $0$ | $0$ | $1$ | $2$ | Key in coin sample space 2 |
| `{{key:÷}}` | $0$ | $0$ | $0$ | $0.5$ | Compute $P(\text{Heads}) = 1/2 = 0.5$ |
| `1` | $0$ | $0$ | $0.5$ | $1$ | Key in favorable die outcome 1; stack lifts 0.5 to $Y$ |
| `{{key:ENTER}}` | $0$ | $0.5$ | $1$ | $1$ | Push 1 to $Y$; lifts 0.5 to $Z$ |
| `6` | $0$ | $0.5$ | $1$ | $6$ | Key in die sample space 6 |
| `{{key:÷}}` | $0$ | $0$ | $0.5$ | $0.1666666667$ | Compute $P(\text{Roll 6}) = 1/6$; $Z$ drops to $Y$ |
| `{{key:×}}` | $0$ | $0$ | $0$ | $0.0833333333$ | Multiply independent probabilities: $0.5 \times 0.1667 \approx 0.0833$ |

- **Diagnostic Checkpoint:** Register $X$ displays $0.0833333333$. Joint probability is $1/12 \approx 8.33\%$.

#### Challenge 52: Drawing Two Aces Without Replacement
- **Problem:** A player draws two cards from a 52-card deck without replacement. Probability that both are aces: $\frac{4}{52} \times \frac{3}{51}$.
- **Manipulative Stage:** From a deck of 52 cards, there are 4 aces ($4/52$). After drawing one ace without replacing it, 51 cards remain, of which 3 are aces ($3/51$).
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_52:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_52:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4` | $0$ | $0$ | $0$ | $4$ | Key in initial aces 4 |
| `{{key:ENTER}}` | $0$ | $0$ | $4$ | $4$ | Push 4 into Register $Y$ |
| `52` | $0$ | $0$ | $4$ | $52$ | Key in total deck size 52 |
| `{{key:÷}}` | $0$ | $0$ | $0$ | $0.0769230769$ | Compute first draw probability: $4/52 = 1/13$ |
| `3` | $0$ | $0$ | $0.0769230769$ | $3$ | Key in remaining aces 3; stack lifts to $Y$ |
| `{{key:ENTER}}` | $0$ | $0.0769230769$ | $3$ | $3$ | Push 3 to $Y$; lifts first probability to $Z$ |
| `51` | $0$ | $0.0769230769$ | $3$ | $51$ | Key in remaining total cards 51 |
| `{{key:÷}}` | $0$ | $0$ | $0.0769230769$ | $0.0588235294$ | Compute second draw probability: $3/51 = 1/17$; $Z$ drops to $Y$ |
| `{{key:×}}` | $0$ | $0$ | $0$ | $0.0045248869$ | Multiply dependent probabilities: $1/221 \approx 0.004525$ |

- **Diagnostic Checkpoint:** Register $X$ displays $0.0045248869$. The probability of drawing two aces without replacement is approximately $0.45\%$.

#### Challenge 53: Drawing Consecutive Matching Socks
- **Problem:** A drawer has 6 black socks and 4 blue socks (10 total). Probability of drawing two matching black socks without replacement: $\frac{6}{10} \times \frac{5}{9}$.
- **Manipulative Stage:** Place 6 black tokens and 4 blue tokens in a bag (10 total). Drawing the first black token has probability $6/10$. Without replacing it, 5 black tokens remain out of 9 total ($5/9$).
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_53:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_53:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `6` | $0$ | $0$ | $0$ | $6$ | Key in initial black socks 6 |
| `{{key:ENTER}}` | $0$ | $0$ | $6$ | $6$ | Push 6 into Register $Y$ |
| `10` | $0$ | $0$ | $6$ | $10$ | Key in total socks 10 |
| `{{key:÷}}` | $0$ | $0$ | $0$ | $0.6$ | Compute first draw probability: $6/10 = 0.6$ |
| `5` | $0$ | $0$ | $0.6$ | $5$ | Key in remaining black socks 5; stack lifts 0.6 to $Y$ |
| `{{key:ENTER}}` | $0$ | $0.6$ | $5$ | $5$ | Push 5 to $Y$; lifts 0.6 to $Z$ |
| `9` | $0$ | $0.6$ | $5$ | $9$ | Key in remaining total socks 9 |
| `{{key:÷}}` | $0$ | $0$ | $0.6$ | $0.5555555556$ | Compute second draw probability: $5/9 \approx 0.5556$; $Z$ drops to $Y$ |
| `{{key:×}}` | $0$ | $0$ | $0$ | $0.3333333333$ | Multiply dependent probabilities: $0.6 \times 0.5556 = 1/3$ |

- **Diagnostic Checkpoint:** Register $X$ displays $0.3333333333$. Exactly $1/3$ ($33.33\%$) chance of drawing a matching black pair.

#### Challenge 54: Prime Factorization of 3,600
- **Problem:** Decompose 3,600 into prime factors ($3600 = 60^2$).
- **Manipulative Stage:** Construct a factor tree for 3,600: $3600 = 36 \times 100 = (4 \times 9) \times (4 \times 25) = 2^4 \times 3^2 \times 5^2$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_54:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_54:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3600` | $0$ | $0$ | $0$ | $3600$ | Key in composite integer 3600 |
| `{{key:FACT}}` | $0$ | $0$ | $0$ | $3600$ | LCD decomposes into prime factors: `2⁴ × 3² × 5²` |

- **Diagnostic Checkpoint:** Register $X$ preserves $3600$ while screen displays $2^4 \times 3^2 \times 5^2$.

#### Challenge 55: GCD and LCM of 45 and 75
- **Problem:** Find $\gcd(45, 75)$ and $\operatorname{lcm}(45, 75)$.
- **Manipulative Stage:** Factor both numbers: $45 = 3^2 \times 5$, $75 = 3 \times 5^2$. The intersection of prime factors is $3 \times 5 = 15$ ($\gcd$). The union of prime factors with highest powers is $3^2 \times 5^2 = 225$ ($\operatorname{lcm}$).
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_55:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_55:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `45` | $0$ | $0$ | $0$ | $45$ | Enter first integer 45 |
| `{{key:ENTER}}` | $0$ | $0$ | $45$ | $45$ | Push 45 into Register $Y$ |
| `75` | $0$ | $0$ | $45$ | $75$ | Key in second integer 75 |
| `{{key:GCF}}` | $0$ | $0$ | $0$ | $15$ | Compute greatest common factor: $\gcd(45, 75) = 15$ |
| `45` | $0$ | $0$ | $15$ | $45$ | Key in 45 for LCM; stack lifts 15 to $Y$ |
| `{{key:ENTER}}` | $0$ | $15$ | $45$ | $45$ | Push 45 to $Y$; lifts 15 to $Z$ |
| `75` | $0$ | $15$ | $45$ | $75$ | Key in second integer 75 |
| `{{key:LCM}}` | $0$ | $0$ | $15$ | $225$ | Compute least common multiple: $\operatorname{lcm}(45, 75) = 225$; $Z$ drops to $Y$ |

- **Diagnostic Checkpoint:** Register $X$ displays $225$ ($\text{LCM}$) and Register $Y$ preserves $15$ ($\text{GCF}$). Note that $15 \times 225 = 3375 = 45 \times 75$.

#### Challenge 56: Synchronized Municipal Traffic Signal Cycles
- **Problem:** Signal A cycles every $45\text{ seconds}$, Signal B cycles every $60\text{ seconds}$. Find the synchronized cycle time: $\operatorname{lcm}(45, 60)$.
- **Manipulative Stage:** On a timing tape, place red markers every 45 units (45, 90, 135, 180...) and blue markers every 60 units (60, 120, 180...). The first point of co-occurrence is 180 units.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_56:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_56:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `45` | $0$ | $0$ | $0$ | $45$ | Enter Signal A period 45 s |
| `{{key:ENTER}}` | $0$ | $0$ | $45$ | $45$ | Push 45 into Register $Y$ |
| `60` | $0$ | $0$ | $45$ | $60$ | Enter Signal B period 60 s |
| `{{key:LCM}}` | $0$ | $0$ | $0$ | $180$ | Compute $\operatorname{lcm}(45, 60) = 180$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $180$. Both traffic lights synchronize every 180 seconds ($3\text{ minutes}$).

#### Challenge 57: Euclidean Division Ladder for $\gcd(546, 210)$
- **Problem:** Compute Euclidean steps for $546$ and $210$: $546 \div 210 = 2\text{ R }126$; $210 \div 126 = 1\text{ R }84$; $126 \div 84 = 1\text{ R }42$; $84 \div 42 = 2\text{ R }0$.
- **Manipulative Stage:** Cut a ribbon 546 cm long and measure with a 210 cm rod: two rods fit with 126 cm remainder ($546 = 2 \times 210 + 126$). Next, measure 210 cm with 126 cm: one rod fits with 84 cm remainder. Measure 126 cm with 84 cm: one rod fits with 42 cm remainder. Finally, 84 cm divides into two 42 cm segments with 0 remainder. The last non-zero remainder is 42.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_57:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_57:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `546` | $0$ | $0$ | $0$ | $546$ | Enter first integer 546 |
| `{{key:ENTER}}` | $0$ | $0$ | $546$ | $546$ | Push 546 into Register $Y$ |
| `210` | $0$ | $0$ | $546$ | $210$ | Enter second integer 210 |
| `{{key:GCF}}` | $0$ | $0$ | $0$ | $42$ | Execute hardware Euclidean ladder: $\gcd(546, 210) = 42$ |

- **Diagnostic Checkpoint:** Register $X$ displays $42$. Greatest common divisor of 546 and 210 is 42.

#### Challenge 58: Mean Absolute Deviation of a 7-Element Dataset
- **Problem:** Dataset: $12, 14, 15, 16, 18, 20, 24$ (Mean = 17.0). Deviations: $5, 3, 2, 1, 1, 3, 7$. Sum = 22. MAD = $22/7$.
- **Manipulative Stage:** Plot the 7 points on a dot plot. Draw a fulcrum at the mean 17. Measure the physical distance from each dot to the mean (5, 3, 2, 1, 1, 3, 7). Add the lengths to get 22, and divide evenly among the 7 data points: $22/7 \approx 3.1429$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_58:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_58:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0$ | $0$ | $0$ | $0$ | Clear all statistical accumulation registers |
| `12` | $0$ | $0$ | $0$ | $12$ | Key in data point 12 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $1$ | Accumulate into statistics registers: count $n = 1$ |
| `14` | $0$ | $0$ | $1$ | $14$ | Key in data point 14 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $2$ | Accumulate: count $n = 2$ |
| `15` | $0$ | $0$ | $2$ | $15$ | Key in data point 15 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $3$ | Accumulate: count $n = 3$ |
| `16` | $0$ | $0$ | $3$ | $16$ | Key in data point 16 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $4$ | Accumulate: count $n = 4$ |
| `18` | $0$ | $0$ | $4$ | $18$ | Key in data point 18 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $5$ | Accumulate: count $n = 5$ |
| `20` | $0$ | $0$ | $5$ | $20$ | Key in data point 20 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $6$ | Accumulate: count $n = 6$ |
| `24` | $0$ | $0$ | $6$ | $24$ | Key in data point 24 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $7$ | Accumulate: count $n = 7$ |
| `{{key:MAD}}` | $0$ | $0$ | $7$ | $3.1428571429$ | Compute mean absolute deviation; $Y$ holds count $n = 7$ |

- **Diagnostic Checkpoint:** Register $X$ displays $3.1428571429$ and Register $Y$ displays $7$. Average distance from data points to mean is $\approx 3.14$.

#### Challenge 59: Interquartile Range Across Grade 6 Science Scores
- **Problem:** Scores: $65, 72, 75, 80, 84, 88, 92, 96$. Find IQR ($Q_3 - Q_1 = 90 - 73.5 = 16.5$).
- **Manipulative Stage:** Arrange 8 test score cards in ascending order. Divide into lower half ($65, 72, 75, 80$) and upper half ($84, 88, 92, 96$). Find the median of lower half ($Q_1 = 73.5$) and median of upper half ($Q_3 = 90$). Measure the spread between quartiles: $90 - 73.5 = 16.5$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_59:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_59:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CLΣ}}` | $0$ | $0$ | $0$ | $0$ | Clear statistical registers |
| `65` | $0$ | $0$ | $0$ | $65$ | Enter score 65 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $1$ | Accumulate: $n = 1$ |
| `72` | $0$ | $0$ | $1$ | $72$ | Enter score 72 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $2$ | Accumulate: $n = 2$ |
| `75` | $0$ | $0$ | $2$ | $75$ | Enter score 75 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $3$ | Accumulate: $n = 3$ |
| `80` | $0$ | $0$ | $3$ | $80$ | Enter score 80 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $4$ | Accumulate: $n = 4$ |
| `84` | $0$ | $0$ | $4$ | $84$ | Enter score 84 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $5$ | Accumulate: $n = 5$ |
| `88` | $0$ | $0$ | $5$ | $88$ | Enter score 88 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $6$ | Accumulate: $n = 6$ |
| `92` | $0$ | $0$ | $6$ | $92$ | Enter score 92 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $7$ | Accumulate: $n = 7$ |
| `96` | $0$ | $0$ | $7$ | $96$ | Enter score 96 |
| `{{key:Σ+}}` | $0$ | $0$ | $0$ | $8$ | Accumulate: $n = 8$ |
| `{{key:IQR}}` | $0$ | $0$ | $8$ | $16.5$ | Compute interquartile range $Q_3 - Q_1 = 16.5$; $Y$ holds count $n = 8$ |

- **Diagnostic Checkpoint:** Register $X$ displays $16.5$ and Register $Y$ displays $8$. Interquartile range of middle $50\%$ of class is $16.5$ points.

#### Challenge 60: Chemical Freezing Point Depression
- **Problem:** Pure water freezes at $0^\circ\text{C}$. Adding rock salt lowers the freezing point by $-7.8^\circ\text{C}$. Adding calcium chloride drops it an additional $-6.4^\circ\text{C}$. Find final freezing point.
- **Manipulative Stage:** Use a downward-pointing thermometer strip. Move down $7.8^\circ$ below zero. Move down another $6.4^\circ$ further below zero. Measure total drop from zero: $14.2^\circ$, giving final temperature of $-14.2^\circ\text{C}$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_60:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_60:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `7.8` | $0$ | $0$ | $0$ | $7.8$ | Key in first depression magnitude 7.8 |
| `{{key:+/-}}` | $0$ | $0$ | $0$ | $-7.8$ | Negate to initial depression $-7.8$ |
| `{{key:ENTER}}` | $0$ | $0$ | $-7.8$ | $-7.8$ | Push $-7.8$ into Register $Y$ |
| `6.4` | $0$ | $0$ | $-7.8$ | $6.4$ | Key in second depression magnitude 6.4 |
| `{{key:+/-}}` | $0$ | $0$ | $-7.8$ | $-6.4$ | Negate to second depression $-6.4$ |
| `{{key:+}}` | $0$ | $0$ | $0$ | $-14.2$ | Add depressions: $-7.8 + (-6.4) = -14.2$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $-14.2$. Final depressed freezing point is $-14.2^\circ\text{C}$.

#### Challenge 61: Product of Three Signed Integers
- **Problem:** Evaluate $(-4) \times (-5) \times (-6)$.
- **Manipulative Stage:** On a number ray, multiplying negative by negative flips the orientation to positive: $(-4) \times (-5) = +20$. Multiplying by a third negative flips the direction back into negative territory: $+20 \times (-6) = -120$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_61:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_61:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4` | $0$ | $0$ | $0$ | $4$ | Key in first magnitude 4 |
| `{{key:+/-}}` | $0$ | $0$ | $0$ | $-4$ | Negate to $-4$ |
| `{{key:ENTER}}` | $0$ | $0$ | $-4$ | $-4$ | Push $-4$ into Register $Y$ |
| `5` | $0$ | $0$ | $-4$ | $5$ | Key in second magnitude 5 |
| `{{key:+/-}}` | $0$ | $0$ | $-4$ | $-5$ | Negate to $-5$ |
| `{{key:×}}` | $0$ | $0$ | $0$ | $20$ | Multiply $(-4) \times (-5) = 20$; stack drops |
| `6` | $0$ | $0$ | $20$ | $6$ | Key in third magnitude 6; stack lifts 20 to $Y$ |
| `{{key:+/-}}` | $0$ | $0$ | $20$ | $-6$ | Negate to $-6$ |
| `{{key:×}}` | $0$ | $0$ | $0$ | $-120$ | Multiply $20 \times (-6) = -120$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $-120$. An odd number of negative factors produces a negative product.

#### Challenge 62: Order of Operations with Negative Numbers
- **Problem:** Evaluate $(-18) \times 4 - (-36) \div (-9) = -72 - 4 = -76$.
- **Manipulative Stage:** Model the two terms separately: Term 1 is 4 groups of $-18$ red chips ($-72$). Term 2 is $-36$ divided into $-9$ parts ($+4$). Deducting 4 positive units from 72 red debt units leaves 76 red debt units ($-76$).
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_62:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_62:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `18` | $0$ | $0$ | $0$ | $18$ | Key in first magnitude 18 |
| `{{key:+/-}}` | $0$ | $0$ | $0$ | $-18$ | Negate to $-18$ |
| `{{key:ENTER}}` | $0$ | $0$ | $-18$ | $-18$ | Push $-18$ into Register $Y$ |
| `4` | $0$ | $0$ | $-18$ | $4$ | Key in multiplier 4 |
| `{{key:×}}` | $0$ | $0$ | $0$ | $-72$ | Compute first product: $-18 \times 4 = -72$ |
| `36` | $0$ | $0$ | $-72$ | $36$ | Key in magnitude 36; stack lifts $-72$ to $Y$ |
| `{{key:+/-}}` | $0$ | $0$ | $-72$ | $-36$ | Negate to $-36$ |
| `{{key:ENTER}}` | $0$ | $-72$ | $-36$ | $-36$ | Push $-36$ to $Y$; lifts $-72$ to $Z$ |
| `9` | $0$ | $-72$ | $-36$ | $9$ | Key in magnitude 9 |
| `{{key:+/-}}` | $0$ | $-72$ | $-36$ | $-9$ | Negate to divisor $-9$ |
| `{{key:÷}}` | $0$ | $0$ | $-72$ | $4$ | Compute quotient $(-36) \div (-9) = 4$; $Z$ drops to $Y$ |
| `{{key:-}}` | $0$ | $0$ | $0$ | $-76$ | Subtract $-72 - 4 = -76$; stack drops |

- **Diagnostic Checkpoint:** Register $X$ displays $-76$. Subtraction of two grouped terms completed cleanly without parentheses.

#### Challenge 63: Geometric Square Root of a Square Ranch
- **Problem:** A square ranch has an area of $4,096\text{ m}^2$. Find side length.
- **Manipulative Stage:** On a square grid, identify that $4096 = 2^{12}$. Taking the square root halves the exponent: $\sqrt{2^{12}} = 2^6 = 64$.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_63:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_63:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4096` | $0$ | $0$ | $0$ | $4096$ | Enter ranch area $4096\text{ m}^2$ |
| `{{key:√x}}` | $0$ | $0$ | $0$ | $64$ | Extract square root: $\sqrt{4096} = 64$ |

- **Diagnostic Checkpoint:** Register $X$ displays $64$. Ranch perimeter boundary is $64\text{ m}$ per side.

#### Challenge 64: Divisibility by 11 Verification
- **Problem:** Test if 2,596 is divisible by 11 using Euclidean division (`{{key:÷R}}`).
- **Manipulative Stage:** Apply the alternating digit sum divisibility rule for 11: $(2 + 9) - (5 + 6) = 11 - 11 = 0$. Since the alternating difference is a multiple of 11, the number is divisible with zero remainder.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_64:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_64:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2596` | $0$ | $0$ | $0$ | $2596$ | Key in dividend 2596 |
| `{{key:ENTER}}` | $0$ | $0$ | $2596$ | $2596$ | Push 2596 into Register $Y$ |
| `11` | $0$ | $0$ | $2596$ | $11$ | Enter divisor 11 |
| `{{key:÷R}}` | $0$ | $0$ | $0$ | $236$ | Euclidean division: Quotient 236 in $X$, Remainder 0 in $Y$ |

- **Diagnostic Checkpoint:** Register $X$ displays $236$ and Register $Y$ displays $0$. Remainder of 0 confirms exact divisibility by 11 ($2596 = 236 \times 11$).

#### Challenge 65: Mersenne Number Primality Check: $2^5 - 1 = 31$
- **Problem:** Compute $2^5 - 1$ and check if the result is prime.
- **Manipulative Stage:** Lay out power-of-two blocks: 1, 2, 4, 8, 16. Summing these 5 blocks produces $2^5 - 1 = 31$. Attempt to arrange 31 counters into rectangular arrays: only $1 \times 31$ is possible, confirming 31 is prime.
- **RPN Keystrokes:** `{{res:sc6_07_data_probability_primes_seq_65:keys}}` $\rightarrow$ **`{{res:sc6_07_data_probability_primes_seq_65:value}}`**

| Keystroke | Register T | Register Z | Register Y | Register X | Operational Commentary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2` | $0$ | $0$ | $0$ | $2$ | Enter base 2 |
| `{{key:ENTER}}` | $0$ | $0$ | $2$ | $2$ | Push base into Register $Y$ |
| `5` | $0$ | $0$ | $2$ | $5$ | Enter exponent 5 |
| `{{key:yˣ}}` | $0$ | $0$ | $0$ | $32$ | Compute power $2^5 = 32$; stack drops |
| `1` | $0$ | $0$ | $32$ | $1$ | Key in second number 1; stack lifts 32 to $Y$ |
| `{{key:-}}` | $0$ | $0$ | $0$ | $31$ | Subtract $32 - 1 = 31$; stack drops |
| `{{key:PRIME}}` | $0$ | $0$ | $0$ | $31$ | Test primality: LCD status flashes `PRIME` |

- **Diagnostic Checkpoint:** Register $X$ preserves $31$ and LCD flashes `PRIME`. The 3rd Mersenne prime $M_5 = 2^5 - 1 = 31$ is verified.

---


<div class="admonition note">
<p class="admonition-title">For Parents &amp; Teachers: Standards Alignment Matrix</p>

| Topic / Skill | Common Core (CCSS) | Singapore Dimensions Math | Bridges in Mathematics |
| :--- | :--- | :--- | :--- |
| **Simple & Compound Probability** | 7.SP.C.5, 7.SP.C.8 | Grade 6 Chapter 14 | Unit 7 Module 1 |
| **Prime Factorization & Primes** | 6.NS.B.4 | Grade 6 Chapter 1 | Unit 1 Module 2 |
| **GCF & LCM via Hardware Keys** | 6.NS.B.4 | Grade 6 Chapter 1 | Unit 1 Module 3 |
| **Mean, Median, Mode, Range** | 6.SP.B.5.C | Grade 6 Chapter 13 | Unit 8 Module 1 |
| **IQR & Mean Absolute Deviation** | 6.SP.B.5.C | Grade 6 Chapter 13 | Unit 8 Module 3 |
| **Signed Numbers & Zero Pairs** | 6.NS.C.5, 7.NS.A.1 | Grade 6 Chapter 2 | Unit 6 Module 2 |
| **Absolute Value as Distance** | 6.NS.C.7.C | Grade 6 Chapter 2 | Unit 6 Module 3 |
| **Geometric Square & Root Inverses** | 8.EE.A.2 (Accelerated Gr 6) | Grade 6 Chapter 10 | Unit 5 Module 4 |

<p>
For detailed classroom station activities corresponding to these standards, consult <a href="../../curriculum/worksheets.md#big-ideas-math-ap-standards">Curriculum Station Worksheets: Big Ideas Math &amp; AP Standards</a>.
</p>
</div>

---

## What You Mastered & Looking Ahead

In this chapter, you unlocked the fundamental atomic architecture of numbers and real-world data:

1. **Discrete Probability & Fair Symmetries:** You investigated fair polyhedral dice (`{{key:🎲}}`), experimental frequencies, and compound probability events without tree confusion.
2. **The Prime Factor Engine:** You harnessed the Prime Factor Studio and SC-6 dedicated hardware keys (`{{key:PRIME}}`, `{{key:FACT}}`, `{{key:GCF}}`, `{{key:LCM}}`, `{{key:÷R}}`) to decompose composite numbers, calculate greatest common factors, and prove the Secret Partner Rule.
3. **Descriptive Statistics:** With the non-volatile statistical accumulator (`{{key:Σ+}}`), you evaluated real datasets, discovering how means, medians, and modes capture central tendencies while IQR and MAD reveal spread.
4. **Pre-Algebra & Directed Numbers:** You conquered negative numbers and zero pairs with the sign toggle (`{{key:+/-}}`) and distance metrics (`{{key:|x|}}`).

In **[Chapter 08: The Math Quiz Engine](08-math-quiz-engine.md)**, you will take everything you have learned and put your operational speed to the test. You will enter the interactive quiz game mode on your SC-6, solving rapid-fire arithmetic challenges, racing against the hardware timer, and tracking your accuracy streaks on the transflective LCD. Let's see how fast your mathematical reflexes really are!
