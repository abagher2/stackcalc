---
title: "Chapter 2: The Architecture of Inside-Out Thinking | Thinking in the Stack (SC-32)"
description: "George Miller's working-memory limit, Dijkstra's Shunting-Yard railway, combined work-rate problems, continued fractions, nested radicals, and 4-register XYZT stack dynamics on the StackCalc SC-32."
---

# Chapter 2: The Architecture of Inside-Out Thinking

## George Miller's Four Chunks and Dijkstra's Railway Yard

### The Four-Chunk Limit of Human Working Memory

Why can a human being glance at a four-item grocery list—*milk, apples, coffee, bread*—and walk through a supermarket without writing anything down, yet freeze in frustration when staring at a four-layer algebraic fraction on a high-school math test?

In 1956, as we glimpsed in the Prologue, Harvard cognitive psychologist **George A. Miller** published one of the most cited papers in the history of science, *"The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information"* {{cite:miller1956}}. Miller discovered that human **working memory**—the mental scratchpad where you hold numbers and ideas while reasoning—is surprisingly small. Subsequent experiments by cognitive scientists Nelson Cowan and **John Sweller** {{cite:sweller1988}} refined Miller's limit even further: when you are actively transforming information rather than reciting a phone number, **the human brain can hold only about four independent chunks at one time**.

Now think about what happens when you try to evaluate a multi-story rational expression from left to right on paper or on an ordinary infix calculator:

$$U = \frac{(18.5 \times 4.2) + (7.1 \times 9.6)}{14.3 - 5.8}$$

If you force yourself to read that equation strictly from left to right—the way 16th-century typesetters printed it—look at the tax imposed on your four mental slots:
1. First you have to remember that you are inside the **numerator** of a giant fraction (Slot 1).
2. Next you open a second parenthesis to multiply $18.5 \times 4.2$ (Slot 2).
3. Then you encounter a `+` sign that *cannot be executed yet* because the second product $(7.1 \times 9.6)$ has not been calculated (Slot 3).
4. Then you encounter a division bar `÷ (` that *also* cannot be executed until the denominator $(14.3 - 5.8)$ is finished (Slot 4).

Before you have done a single difficult piece of mathematics, all four slots of your working memory are jammed with **suspended grammar**—open parentheses and deferred operators waiting for their future partners!

Compare that mental gridlock with how you naturally solve the same fraction in your head when nobody forces you to write a single giant line of symbols: you multiply $18.5 \times 4.2 = 77.70$ and hold that single finished number on one mental shelf; you multiply $7.1 \times 9.6 = 68.16$ and add the two products into $145.86$, freeing your second shelf at once; and you subtract $14.3 - 5.8 = 8.5$ before dividing $145.86 \div 8.5 = 17.16$. At no moment did your brain hold more than three numbers at once, and at no moment did it hold a dangling parenthesis!

### Edsger Dijkstra's 1961 Railway Siding

Humans are not the only ones who choke on left-to-right infix notation. Digital processors cannot evaluate infix equations in left-to-right order either!

In 1960 and 1961, the thirty-one-year-old Dutch computer scientist **Edsger W. Dijkstra** {{cite:dijkstra1961}} and his colleague Jaap Zonneveld were writing the world's first **ALGOL 60** compiler on an Electrologica X1 computer at the Mathematical Centre in Amsterdam. Faced with the problem of teaching a digital machine with tiny magnetic-core memory how to read human formulas like $A + B \times C$ in a single left-to-right pass, Dijkstra realized that a processor cannot add $A$ and $B$ the moment it sees the `+` sign, because `×` has higher precedence (`PEMDAS`). The computer has to shunt the `+` sign onto a temporary waiting track—just like a freight locomotive shunting boxcars in a railway switchyard—until $B \times C$ has been coupled together!

Dijkstra called his invention the **Shunting-Yard Algorithm**:
- Imagine an incoming train of symbols arriving from left to right along a main railway track: `18.5`, `×`, `4.2`, `+`, `7.1`, `×`, `9.6`.
- Whenever a **number** boxcar arrives, it rolls straight through to the departure yard.
- Whenever an **operator** boxcar (`×`, `+`, `÷`) or a **left parenthesis** `(` arrives, it is diverted onto a dead-end **operator siding** to wait until its right-hand numbers have passed by.
- Only when a higher-precedence operation finishes—or when a **right parenthesis** `)` arrives to clear the siding—do the waiting operator cars roll back out onto the main track behind their numbers:

$$\text{Infix Input: } (18.5 \times 4.2) + (7.1 \times 9.6) \quad \xrightarrow{\text{Shunting Yard}} \quad \text{Postfix Output: } 18.5 \;\; 4.2 \;\; \times \;\; 7.1 \;\; 9.6 \;\; \times \;\; +$$

Look closely at the train leaving Dijkstra's railway yard on the right: every single parenthesis has been uncoupled and thrown away, leaving the pure chronological postfix sequence that we traced in the Prologue from Łukasiewicz {{cite:lukasiewicz1924}} and Burks, Warren, and Wright {{cite:burks1954}} to Charles Hamblin's hardware push-down stack {{cite:hamblin1957}}. Today, whenever you type an equation into **Python**, **Java**, **C++**, **JavaScript**, or even an ordinary algebraic calculator and press `=`, an internal shunting-yard parser secretly translates your left-to-right infix text into postfix stack instructions before a single multiplication takes place—powering the **Java Virtual Machine (JVM)**, **WebAssembly (Wasm)**, **Adobe PostScript**, and deep-space **Forth** navigation computers {{cite:knuth1997,hp15c1982}}.

When **Bill Hewlett** and **David Cochran** designed the HP-35 in 1972 {{cite:hewlett1972,cochran1972}}, they united George Miller's psychology with Edsger Dijkstra's computer science. Why force a human being to act like a 16th-century typesetter—holding open parentheses in fragile working memory—only for the silicon chip to translate those keystrokes back into a postfix stack anyway? By placing the **four-shelf stack ($X, Y, Z, T$)** on the screen to match the **four chunks** of human working memory, human and machine speak the same language, and every intermediate subtotal appears in plain sight the moment it is formed.

---

## Unpeeling Rational Expressions and the Two-Pipe Reservoir Puzzle

How do four shelves ($X, Y, Z, T$) untangle any rational expression in high-school Algebra II or collegiate engineering? Picture the physical choreography of those four shelves in motion.

{{blocks:sc32_concept_stack_elevator|Inside-out expression tree evaluation paired with the four-register operational stack elevator (T, Z, Y, X).}}

### The Elevator Shaft: Why `ENTER` Parks the Car While Operators Arm It

In Chapter 1, we saw what each of the four shelves holds at rest. Now picture those four registers in motion as a vertical glass elevator shaft with four floors, where every lift pushes subtotals upward and every two-number (dyadic) operation drops waiting subtotals back down into position:

| Stack Shelf | Role on Workbench | Movement on Lift (`ENTER` / Armed Digit) | Movement on Dyadic Drop (`+`, `-`, `×`, `÷`, `yˣ`, `x∥y`) |
| :---: | :--- | :--- | :--- |
| **Line T (4th Floor)** | **Top Shelf & Constant Conveyor** | Receives $Z_{\text{old}}$ ($T_{\text{old}}$ exits the roof in `4-LVL`) | Copies $T_{\text{old}}$ downward into $Z$ while remaining in $T$ |
| **Line Z (3rd Floor)** | **Upper Waiting Shelf** | Receives $Y_{\text{old}}$ as a second branch starts | Drops $Z_{\text{old}}$ down into $Y$, ready to meet $X$ |
| **Line Y (2nd Floor)** | **Staging Shelf** | Receives $X_{\text{old}}$ (`ENTER` parks lift; armed digit lifts) | Consumed with $X_{\text{old}}$; receives $Z_{\text{old}}$ from upstairs |
| **Line X (Ground Floor)** | **Active Workbench** | Holds copy on `ENTER` (overwritten by next digit) | Receives new result $f(Y_{\text{old}}, X_{\text{old}})$ and arms stack lift |

To keep numbers moving smoothly through this four-floor shaft, the elevator has only two states—**Parked** (`Stack Lift = FALSE`) and **Primed** (`Stack Lift = TRUE`):

1. **Why `ENTER` Parks the Elevator (`Lift = FALSE`):**  
   To multiply $18.5$ by $4.2$, you type `18.5` into the ground-floor lobby (Shelf $X$) and press **`ENTER`** to tell the instrument that your first number is complete. Pressing **`ENTER`** copies $18.5$ up to the second floor ($Y = 18.5$), while $18.5$ also remains visible on the ground floor ($X = 18.5$). Because the ground floor still holds a temporary copy of $18.5$, pressing **`ENTER` parks the elevator**: the next number you type (`4.2`) writes over that temporary copy on Shelf $X$, leaving $Y = 18.5$ and $X = 4.2$ face to face.
2. **Why Every Operator Arms the Elevator (`Lift = TRUE`):**  
   Now you tap **`×`**. The second floor ($18.5$) drops down and fuses with the ground floor ($4.2$) into **`77.70`** on Shelf $X$. That `77.70` is not a temporary copy—it is a finished mathematical result. Every operator or function therefore **arms the elevator** (`Stack Lift = TRUE`). The instant you begin typing the next number in your problem (`7.1`), you do **not** press `ENTER`: the armed elevator lifts `77.70` up to Shelf $Y$ so `7.1` can take its place on Shelf $X$.
3. **How Two-Branch Fractions Meet Without Parentheses (Dyadic Stack Drop):**  
   Watch what happens when you press `ENTER` after `7.1` and type `9.6`: your finished first branch (`77.70`) rides safely up to the **3rd Floor (Shelf $Z$)** while `7.1` and `9.6` occupy Shelves $Y$ and $X$. When you tap **`×`** to multiply $7.1 \times 9.6 = 68.16$ on Shelf $X$, the upper floors drop down one story—bringing `77.70` from Shelf $Z$ right back down into Shelf $Y$. One tap of **`+`** fuses $77.70 + 68.16 = 145.86$ for the entire numerator. Then you compute the denominator $14.3 - 5.8 = 8.50$ on the lower shelves while $145.86$ waits upstairs, and one final tap of **`÷`** divides them ($145.86 \div 8.50 = 17.16$)!

### The Classic High-School Work-Rate Puzzle: Two Pipes Filling a Reservoir

This same two-branch rhythm illuminates one of the classic word problems of high-school Algebra II.

Picture a civil engineer testing the emergency water supply for a town reservoir:
- **Pipe A** (the main valley aqueduct), running alone, can fill the empty reservoir to the brim in **$100\text{ minutes}$**.
- **Pipe B** (the auxiliary river pump), running alone, can fill the same reservoir in **$220\text{ minutes}$**.

If the water superintendent opens the valves on **both Pipe A and Pipe B at the same time**, how many minutes will it take them to fill the reservoir together?

Every autumn in Algebra II classrooms, a tempting trap claims its victims: students try to average the two times ($(100 + 220)/2 = 160\text{ minutes}$) or add them ($320\text{ minutes}$). Pause for one second and test that against common sense {{cite:strogatz2012,ellenberg2014}}: if Pipe A *alone* fills the reservoir in $100\text{ minutes}$, opening a second pipe to help it cannot possibly make the job take *longer* than $100\text{ minutes}$! Two pipes working together must finish in **less time than the fastest single pipe** ($T_{\text{together}} < 100\text{ minutes}$).

Why can't we add the times $T_A$ and $T_B$ together? Because **times do not add when two helpers work side by side—rates of flow add!**

Look at the problem from the **inside out**, one minute at a time:
1. If Pipe A fills $1\text{ reservoir}$ in $100\text{ minutes}$, then in **one single minute** Pipe A fills a fraction of the reservoir equal to its **reciprocal**:
   $$R_A = \frac{1}{100} = 0.0100\text{ reservoirs per minute}$$
2. If Pipe B fills $1\text{ reservoir}$ in $220\text{ minutes}$, then in **one single minute** Pipe B fills:
   $$R_B = \frac{1}{220} \approx 0.004545\text{ reservoirs per minute}$$
3. Because both pipes pour water into the same basin at the same time, their **per-minute flow rates add together**:
   $$R_{\text{total}} = R_A + R_B = \frac{1}{100} + \frac{1}{220} \approx 0.014545\text{ reservoirs per minute}$$
4. Finally, if $0.014545$ of the reservoir fills each minute, the total time $T_{\text{together}}$ required to fill $1\text{ whole reservoir}$ is the **reciprocal** of the combined rate:
   $$T_{\text{together}} = \frac{1}{\frac{1}{100} + \frac{1}{220}} = \frac{100 \times 220}{100 + 220} = \frac{22,000}{320} = \mathbf{68.75\text{ minutes}}$$

What if the town also opens two smaller backup pipes: **Pipe C**, which takes $470\text{ minutes}$ alone, and **Pipe D**, which takes $1,000\text{ minutes}$ alone? Those numbers—$100, 220,$ and $470$—are familiar for a reason: parallel water pipes filling a reservoir obey the **same harmonic reciprocal-sum law as the $100\,\Omega, 220\,\Omega,$ and $470\,\Omega$ parallel resistors we met in the Prologue**! Each additional pipe contributes its own reciprocal rate, $\frac{1}{470}$ and $\frac{1}{1000}$, pulling the combined filling time down step by step: from $100\text{ minutes}$ for Pipe A alone, to $68.75\text{ minutes}$ for Pipes A and B, to $59.98\text{ minutes}$ with Pipe C added, and finally to $\mathbf{56.58\text{ minutes}}$ with all four pipes open:

$$T_{\text{all four}} = \left(\frac{1}{100} + \frac{1}{220} + \frac{1}{470} + \frac{1}{1000}\right)^{-1} = 56.5831\text{ minutes}$$

Every harmonic problem follows this three-beat cadence: *flip into rates, add the rates, flip back into time*—or fold each new branch into the running total with the harmonic product-over-sum operator $\frac{T_A T_B}{T_A + T_B}$.

---

## Continued Fractions, Zu Chongzhi's Miracle Pi, and Viète's Nested Radicals

Once you discover the power of flipping a number upside down ($1/x$) and adding a whole number, a hidden staircase opens up inside mathematics—a staircase called a **Continued Fraction**.

Look at an equation like this on paper:

$$x = 1 + \frac{1}{2 + \frac{1}{3 + \frac{1}{4}}}$$

To an eye trained to read from the top down, a continued fraction looks like a hall of mirrors: a fraction whose denominator contains a fraction, whose denominator contains yet another fraction. If you try to type that expression from the top down into an algebraic calculator—`1 + 1 / ( 2 + 1 / ( 3 + 1 / 4 ) )`—you have to open parentheses at every floor and pray they match at the bottom.

Yet watch what happens when you read that same staircase from the **basement up**:
1. Start at the bottom floor with $4$, and flip it upside down into $\frac{1}{4} = 0.25$.
2. Step up to the third floor and add $3$: now you have $3.25$ ($13/4$).
3. Flip that entire sum upside down ($1 / 3.25 = 4/13 \approx 0.3077$) and add $2$: now you have $2.3077$ ($30/13$).
4. Flip that upside down ($13/30 \approx 0.4333$) and add the roof integer $1$: you land on **$1.4333$** ($43/30$)!

You never had to hold two branches in your head at once! Every step was just *flip, add, flip, add*.

### How Zu Chongzhi Found $\pi \approx \frac{355}{113}$ a Thousand Years Before Europe

Why have mathematicians from ancient Greece and fifth-century China to Christiaan Huygens and Srinivasa Ramanujan been so enchanted by continued fractions? Because continued fractions are nature's X-ray machine: they reveal the **best possible rational approximations** to any irrational number in the universe!

Put this X-ray machine to work on the most famous number in geometry: **$\pi = 3.14159265358979\dots$**
1. Peel off the whole-number part **$3$**, leaving the decimal tail $0.14159265\dots$
2. Flip that decimal tail upside down ($1 / 0.14159265\dots$): you get **$7.0625133\dots$**! Because $7.0625$ is so close to the integer **$7$**, stopping right there gives Archimedes's classic schoolhouse approximation:
   $$\pi \approx 3 + \frac{1}{7} = \frac{22}{7} \approx 3.142857 \quad (\text{accurate to } 2\text{ decimal places})$$
3. Now peel off that **$7$**, leaving $0.0625133\dots$, and flip it upside down again ($1 / 0.0625133\dots$): you get **$15.996594\dots$**—which is astonishingly close to **$16$** (or $15 + \frac{1}{1}$)!

If you stop right before the giant jump that comes next (the next denominator is $292$!), you get a four-story continued fraction:

$$\pi \approx 3 + \frac{1}{7 + \frac{1}{15 + \frac{1}{1}}} = 3 + \frac{1}{7 + \frac{1}{16}} = 3 + \frac{16}{113} = \mathbf{\frac{355}{113}} \approx \mathbf{3.14159292}$$

Look at that fraction: **$\frac{355}{113}$** (easy to remember by writing the first three odd numbers twice: `113355`, and splitting them in the middle as `355 / 113`). Using only three-digit numbers, $\frac{355}{113}$ matches $\pi$ to **six decimal places**—an error of less than one-millionth of an inch per foot! It was discovered in **AD 480** by the Chinese mathematician and astronomer **Zu Chongzhi** (who called it the *Milü*, or "close ratio"), and no mathematician in Europe found a better fraction for $\pi$ for more than a thousand years.

### The Golden Ratio $\varphi$ and Why Sunflowers Count in Fibonacci Numbers

If large denominators like $292$ inside a continued fraction mean a number is *easy* to approximate with fractions, what irrational number is the *hardest* in the universe to approximate with fractions—the "most irrational" of all numbers?

It must be the continued fraction whose denominators are as *small* as possible at every single floor—all **`1`s**:

$$\varphi = 1 + \frac{1}{1 + \frac{1}{1 + \frac{1}{1 + \frac{1}{1 + \dots}}}}$$

Look at that infinite tower of $1$s. Because the endless staircase tucked under the top fraction bar is an exact miniature copy of the whole staircase $\varphi$ itself, we can write:

$$\varphi = 1 + \frac{1}{\varphi} \implies \varphi^2 - \varphi - 1 = 0 \implies \varphi = \frac{1 + \sqrt{5}}{2} \approx \mathbf{1.6180339887}$$

It is the **Golden Ratio**! Even better, look at what happens when you climb that ladder of $1$s from the basement up, one floor at a time (*flip and add $1$, flip and add $1$*):
- Floor 1: $1 + \frac{1}{1} = \frac{2}{1} = 2.0000$
- Floor 2: $1 + \frac{1}{2} = \frac{3}{2} = 1.5000$
- Floor 3: $1 + \frac{2}{3} = \frac{5}{3} \approx 1.6667$
- Floor 4: $1 + \frac{3}{5} = \frac{8}{5} = 1.6000$
- Floor 5: $1 + \frac{5}{8} = \frac{13}{8} = 1.6250 \;\to\; \frac{21}{13} \;\to\; \frac{34}{21} \;\to\; \frac{55}{34} \;\to\; \frac{89}{55} \approx \mathbf{1.618182}$

Every single step produces the ratio of two consecutive **Fibonacci numbers** ($1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89\dots$)!

That mathematical property explains one of nature's most breathtaking sights: if you look at the center of a **sunflower head**, a **daisy**, or a **pine cone**, the seeds form two families of interlocking spirals—typically $34$ spirals curving clockwise and $55$ spirals curving counterclockwise (or $55$ and $89$ on a large sunflower). Why? Because as each new seed bud emerges at the center of the growing flower tip, it turns by the Golden Angle ($360^\circ / \varphi^2 \approx 137.5^\circ$). If the flower turned by a simple fraction of a circle like $\frac{1}{4}$ or $\frac{22}{7}$, the seeds would line up along $4$ or $7$ straight spokes with wasted empty gaps between them. Because $\varphi$ has only $1$s in its continued fraction, it refuses to lock into spokes—packing every seed at maximum geometric efficiency!

### François Viète's 1593 Nested Square-Root Cascade

In 1593, the French mathematician and royal cryptographer **François Viète** discovered the first exact analytical formula for $\pi$ in European history.

How did Viète trap a curved circle inside a staircase of square roots? Like Archimedes before him, Viète started by inscribing a regular square ($4$ sides) inside a unit circle of radius $r = 1$, and then repeatedly doubled the number of sides: from a square ($4$ sides) to a regular octagon ($8$ sides), a $16$-gon, a $32$-gon, a $64$-gon, and so on toward infinity.

Watch what happens to the trigonometry each time you slice a central angle $\theta$ in half. By the half-angle cosine identity:

$$\cos\left(\frac{\theta}{2}\right) = \sqrt{\frac{1 + \cos\theta}{2}} = \frac{\sqrt{2 + 2\cos\theta}}{2}$$

Starting at a right angle $\theta_1 = 90^\circ$ ($\pi/2\text{ radians}$, where $\cos 90^\circ = 0$), bisect the angle step by step:
- **First Bisection ($45^\circ$, Octagon):**
  $$2\cos(45^\circ) = \sqrt{2 + 2\cos(90^\circ)} = \sqrt{2}$$
- **Second Bisection ($22.5^\circ$, $16$-gon):**
  $$2\cos(22.5^\circ) = \sqrt{2 + 2\cos(45^\circ)} = \sqrt{2 + \sqrt{2}}$$
- **Third Bisection ($11.25^\circ$, $32$-gon):**
  $$2\cos(11.25^\circ) = \sqrt{2 + 2\cos(22.5^\circ)} = \sqrt{2 + \sqrt{2 + \sqrt{2}}}$$
- **Fourth Bisection ($5.625^\circ$, $64$-gon):**
  $$2\cos(5.625^\circ) = \sqrt{2 + \sqrt{2 + \sqrt{2 + \sqrt{2}}}}$$

Comparing the area of each inscribed $2^n$-gon to the area of the circumscribed circle, Viète proved that the ratio $\frac{2}{\pi}$ is the infinite product of those nested cosine factors:

$$\frac{2}{\pi} = \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{2 + \sqrt{2}}}{2} \cdot \frac{\sqrt{2 + \sqrt{2 + \sqrt{2}}}}{2} \cdot \frac{\sqrt{2 + \sqrt{2 + \sqrt{2 + \sqrt{2}}}}}{2} \cdots$$

Just like continued fractions, nested square-root pyramids—whether Viète's polygon cascade, a radical quotient like $\sqrt{\frac{128.5 + \sqrt{48.2}}{19.4 - \sqrt{7.6}}}$, or a four-story continued radical $\sqrt{3 + \frac{5}{\sqrt{7 + \frac{11}{\sqrt{13 + 17}}}}}$—look like parenthesis obstacle courses when read from the outside in, yet collapse into a calm two-beat rhythm when you start at the deepest inner root and step outward {{cite:cochran1972}}.

---

## The Conveyor Belt at the Top of the Stack and Named Memory

What happens at the top of our four-floor elevator shaft—on **Floor 4 (Register $T$)**—when two numbers on the bottom floors ($Y$ and $X$) fuse together and the upper floors drop down?

### Why Register $T$ Duplicates Itself Downward

If Floor 4 ($T$) emptied out to zero every time the stack dropped, then after three operations your upper shelves would be blank. Instead, the architects of the classic HP-32SII and HP-15C gave Register $T$ a wonderfully clever property called **$T$-Register Duplication**:

$$\begin{aligned}
X_{\text{new}} &\leftarrow Y_{\text{old}} \text{ [op] } X_{\text{old}} \\
Y_{\text{new}} &\leftarrow Z_{\text{old}} \\
Z_{\text{new}} &\leftarrow T_{\text{old}} \\
T_{\text{new}} &\leftarrow T_{\text{old}} \quad \text{(Copied downward while remaining in } T\text{!)}
\end{aligned}$$

Think of Register $T$ as a **gravity-fed hopper** or a permanently meshed drive gear at the top of the shaft. Whenever the stack drops, Register $T$ hands a copy of its number down to Register $Z$ while keeping its own value in $T$! That single architectural detail unlocks three everyday techniques:
1. **One-Touch Compound Growth:** If you fill all four shelves with a growth factor like $1.065$ (for $6.5\%$ annual growth) and type your starting principal $\$2,500$ into Shelf $X$, every tap of `×` advances the balance by one year ($\text{Year 1} \to \text{Year 2} \to \text{Year 3} \to \text{Year 4} \to \text{Year 5}$) because Register $T$ feeds an endless stream of $1.065$ multipliers down into Shelf $Y$!
2. **Blueprint Unit-Conversion Pipelines:** If you load a conversion constant like $25.4\text{ mm/in}$ across the upper shelves, you can convert an entire table of machinist inch dimensions into millimeters with one multiplication and a single roll-down (`{{key:R↓}}`) per line.
3. **Fixed-Point Continued-Fraction Iteration:** Filling all four shelves with a constant integer $a$ turns Register $T$ into a steady source of $a$'s for continued-fraction staircases ($a + 1/(a + 1/\dots)$), as we will put to the test on the Golden Ratio $\varphi$ in our workbench trace.

### Rearranging Shelves, Recovering `LASTX`, and Two-Way Register Arithmetic

To give you complete command over numbers in flight, the four operational shelves are paired with four sets of architectural tools:
- **In-Place Shelf Permutations (`{{key:x⇄y}}`, `{{key:R↓}}`, `{{key:R↑}}`):**  
  Tapping **`{{key:x⇄y}}`** trades Shelves $Y$ and $X$ whenever you compute a denominator or subtracted term *before* the outer number:
  * If you evaluated a complicated denominator $D$ first on Shelf $X$ and then typed the simple numerator $N$ onto Shelf $X$ (lifting $D$ to Shelf $Y$), pressing `{{key:÷}}` right away would compute $D \div N$ instead of $N \div D$. A single tap of **`{{key:x⇄y}}`** swaps them into $Y = N, X = D$ so `{{key:÷}}` delivers $N \div D$.
  * Similarly, if you evaluated a complicated subtrahend $B$ first and then typed $A$, tapping **`{{key:x⇄y}}`** followed by `{{key:-}}` evaluates $A - B$ in the proper order.
  * Tapping **`{{key:R↓}}`** (Roll Down) or **`{{key:R↑}}`** (Roll Up) rotates all four shelves in a closed four-car Ferris wheel ($X \leftarrow Y \leftarrow Z \leftarrow T \leftarrow X$) without losing a single digit:

  $$\text{Roll Down (`R↓`): } (X, Y, Z, T) \leftarrow (Y, Z, T, X), \qquad \text{Roll Up (`R↑`): } (X, Y, Z, T) \leftarrow (T, X, Y, Z)$$

  Because four rolls bring every shelf right back to its starting floor, you can load four thermocouple readings onto the stack, cycle through them with `{{key:R↓}}` to inspect each reading in full precision, and then tap `{{key:+}} {{key:+}} {{key:+}} 4 {{key:÷}}` to compute their four-point ensemble mean.
- **The Automatic Shadow Register (`{{key:LASTX}}`):**  
  Every time an operation changes Shelf $X$, the previous occupant of Shelf $X$ is saved automatically inside **`LASTX`**. If you press the wrong operator or function key, `{{key:LASTX}}` lets you undo the mistake in seconds. Even better, whenever a formula uses the same variable $x$ or a shared divisor twice—as in the optical diffraction sinc function $\frac{\sin\theta}{\theta}$, the symmetric rational fraction $\frac{x^2 - 1}{x^2 + 1}$, the quadratic roots $\frac{-b \pm \sqrt{\Delta}}{2a}$, or Arthur Kennelly's 1899 three-phase Delta-to-Wye ($\Delta \to \text{Y}$) resistor transformation—`{{key:LASTX}}` acts as an automatic **fifth shadow shelf**!

  Kennelly's $\Delta \to \text{Y}$ transformation is a classic test of stack fluency: when three resistors $R_{12}, R_{23}, R_{31}$ are wired in a closed triangle ($\Delta$) inside a Wheatstone bridge or a three-phase industrial motor starter, neither series nor parallel rules apply on their own. Converting the triangle into an equivalent three-branch star ($\text{Y}$) requires dividing each adjacent pair product by the shared perimeter sum $S = R_{12} + R_{23} + R_{31}$:

  $$R_a = \frac{R_{12} R_{31}}{R_{12} + R_{23} + R_{31}}, \qquad R_b = \frac{R_{12} R_{23}}{R_{12} + R_{23} + R_{31}}, \qquad R_c = \frac{R_{23} R_{31}}{R_{12} + R_{23} + R_{31}}$$

  Because any division $N \div S$ automatically captures its divisor $S$ inside **`LASTX`**, evaluating the first star branch $R_a$ latches the perimeter sum $S$ inside `LASTX` for free—allowing you to compute $R_b$ and $R_c$ next by recalling `{{key:LASTX}}` rather than re-summing the three resistors!
- **26 Named Variables (`A`–`Z`), Two-Way Register Arithmetic, and Indirect Pointers (`i`, `(i)`):**  
  What happens when all four stack shelves ($T, Z, Y, X$) are occupied by live subtotals and you need to combine Shelf $X$ with a constant stored in one of the 26 named variables `A`–`Z`? Because a standard `{{key:RCL}} A` lifts the stack by one floor—pushing the 4th-floor occupant ($T$) off the roof in `4-LVL` mode—the SC-32 provides two-way in-place register arithmetic that bypasses stack lift altogether. **Recall Arithmetic** (`{{key:RCL}}` followed by `+`, `-`, `×`, or `÷` and `A`) updates Register $X$ in place as $X \leftarrow X \text{ op } A$ while leaving Shelves $Y, Z,$ and $T$ untouched. Conversely, **Store Arithmetic** (`{{key:STO}}` followed by `+`, `-`, `×`, or `÷` and `A`) updates Variable `A` in place as $A \leftarrow A \text{ op } X$.

  Even more powerfully, in 1949 **Tom Kilburn, Geoff Tootill, and Max Newman** at the University of Manchester introduced the **"B-line" index register** on the Manchester Mark 1—showing that instead of hard-wiring a fixed memory letter (`A`, `B`, `C`) into a calculation, a machine can hold an integer address $k$ inside a dedicated **index register (`i`)** and use **indirect addressing (`(i)`)** to point to whichever memory slot sits at address $k$. On the SC-32, when `{{key:STO}}` or `{{key:RCL}}` activates the `A–Z` Alpha layer, the decimal point key `{{key:.}}` carries the Alpha label **`i`** (the index register itself) and the neighboring key `{{key:x∥y}}` carries the Alpha label **`(i)`** (the indirect pointer that dereferences $k = \lfloor \lvert i \rvert \rfloor$). Storing $2$ into `i` sets the pointer to slot $2$ (`B`), so `{{key:RCL}} (i)` recalls Variable `B`, `{{key:STO}} {{key:+}} (i)` adds Register $X$ into Variable `B`, and incrementing `i` by $1$ slides your window across all 89 slots of the calculator's unified memory map:

| Pointer Range $k = \lfloor \lvert i \rvert \rfloor$ | Target Memory Bank | Addressed Register / Content | Access Permissions |
| :---: | :--- | :--- | :--- |
| **`1` … `26`** | **Lettered Variables (`A–Z`)** | `1` = `A`, `2` = `B`, `3` = `C`, …, `26` = `Z` | Full Read / Write (`STO (i)`, `RCL (i)`, `x⇄? (i)`) |
| **`27`** | **Index Register (`i`)** | `27` = Index register `i` itself | Full Read / Write |
| **`28` … `33`** | **Statistical Accumulators** | `28` = $\Sigma n$, `29` = $\Sigma x$, `30` = $\Sigma y$, `31` = $\Sigma x^2$, `32` = $\Sigma y^2$, `33` = $\Sigma xy$ | Read / Write via `(i)` |
| **`34` … `39`** | **`POLY` Solver Roots** | `R34`–`R39` (Real & imaginary parts of roots $r_1, r_2, r_3$) | Read via `RCL (i)` |
| **`40` … `89`** | **Statistical Data Points** | `DATA0` (`40`) through `DATA49` (`89`) | Read via `RCL (i)` |
| **$k < 1$ or $k > 89$** | **Out of Bounds** | Displays `INVALID DATA` (Code 02) | N/A (Halts without stack corruption) |

  Finally, the division key `{{key:÷}}` carries two six-operator relational test menus: left-shifted **`{{key:x?y}}`** compares Register $X$ against Register $Y$ (`x=y`, `x≠y`, `x>y`, `x<y`, `x≥y`, `x≤y`), while right-shifted **`{{key:x?0}}`** compares Register $X$ against zero (`x=0`, `x≠0`, `x>0`, `x<0`, `x≥0`, `x≤0`). On the live stack, any test flashes **`YES`** or **`NO`** non-destructively; inside the Equation Editor `{{key:EQN}}`, each test acts as **Kenneth Iverson's Boolean indicator bracket $[P] \in \{1, 0\}$**, returning `1.0` or `0.0` to model piecewise functions in Chapters 7, 8, and 12. Internally, the SC-32 computes in 64-bit IEEE-754 double precision ($53$ significand bits $\approx 15.95$ decimal digits) with a 12-digit guard-rounded display across `{{key:DISP}}` (`ALL`, `FIX`, `SCI`, `ENG`) and 15-digit inspection via `{{key:SHOW}}`. Through the `{{key:FLAGS}}` menu—which also houses user flags and proctored `EXAM` mode in **Chapter 14**—you can switch the stack depth between `4-LVL`, `8-LVL`, and unbounded `INF` mode:

| Mode ID | Architecture Name | Accessible Registers | Stack Drop Behavior | Recommended Application Zone |
| :---: | :--- | :--- | :--- | :--- |
| **4-LVL** | **Classic 4-Level Stack (Default)** | $X, Y, Z, T$ | Top-of-stack $T$-duplication on drop; full HP-32SII / HP-15C parity | Everyday engineering, iterative series, high-speed calculation sprints |
| **8-LVL** | **Extended 8-Level Stack** | $R_1 \dots R_8$ (with $R_1\text{--}R_4$ mapped to $X, Y, Z, T$) | Holds up to 8 nested operands before top-register replication | High-order polynomial factoring, multi-stage audio filters |
| **INF** | **Unbounded Infinite Stack** | Dynamic heap allocation (up to 999 levels) | True LIFO stack; dyadic drop never duplicates; pulls from history | Deep recursive algorithms, large matrix operations |

---

## On the Stack: 4-Register Dynamics & Memory Architecture

Two physical habits govern every trace in this workbench: pressing `{{key:ENTER}}` parks stack lift so the next number you type overwrites Register $X$, while any dyadic operator (`{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`) drops the upper shelves by one floor, replicates Register $T$ downward, and re-arms stack lift.

{{res:sc32_order_of_ops:screenshot|Real-time 4-register operational stack (T, Z, Y, X) displaying intermediate calculation states without deferred parentheses.}}

### Two-Branch Rational Fractions & Combined Reservoir Flow Rates

1. **Weighted Span Rational Fraction ($\frac{(45 \times 3) + (18 \times 4)}{15 - 3} = 17.25$ — Slow-Motion Keystroke Trace):**  
   In this first table, we give **every individual key press its own separate row** so you can watch in slow motion how `{{key:ENTER}}` disables stack lift (allowing `3`, `4`, and `3` to overwrite Register $X$ in place), how `{{key:×}}` and `{{key:-}}` drop the upper stack and re-arm stack lift, and how typing `18` and `15` automatically lifts your finished subtotals into Register $Y$ by position alone:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `45` | $0.0000$ | $0.0000$ | $0.0000$ | $45.0000$ | Enter numerator term 1 |
| `{{key:ENTER}}` | $0.0000$ | $0.0000$ | $45.0000$ | $45.0000$ | Stack lift disabled; $X$ copied to $Y$ |
| `3` | $0.0000$ | $0.0000$ | $45.0000$ | $3.0000$ | Overwrites $X$ directly |
| `{{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $135.0000$ | $45 \times 3 = 135$; Stack lift armed |
| `18` | $0.0000$ | $0.0000$ | $135.0000$ | $18.0000$ | Stack lifts; 135 preserved in $Y$ |
| `{{key:ENTER}}` | $0.0000$ | $135.0000$ | $18.0000$ | $18.0000$ | Stack lift disabled; 135 pushed to $Z$ |
| `4` | $0.0000$ | $135.0000$ | $18.0000$ | $4.0000$ | Overwrites $X$ directly |
| `{{key:×}}` | $0.0000$ | $0.0000$ | $135.0000$ | $72.0000$ | $18 \times 4 = 72$; $Z$ drops to $Y$ |
| `{{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $207.0000$ | $135 + 72 = 207$ (Numerator complete) |
| `15` | $0.0000$ | $0.0000$ | $207.0000$ | $15.0000$ | Stack lifts; 207 preserved in $Y$ |
| `{{key:ENTER}}` | $0.0000$ | $207.0000$ | $15.0000$ | $15.0000$ | Stack lift disabled; 207 pushed to $Z$ |
| `3` | $0.0000$ | $207.0000$ | $15.0000$ | $3.0000$ | Overwrites $X$ directly |
| `{{key:-}}` | $0.0000$ | $0.0000$ | $207.0000$ | $12.0000$ | $15 - 3 = 12$; $Z$ drops to $Y$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$17.2500$** | $207 \div 12 = 17.25$ (Final result) |

2. **Two-Pass Heat Exchanger Thermal Balance ($U = \frac{(18.5 \times 4.2) + (7.1 \times 9.6)}{14.3 - 5.8}$ — Phrase-by-Phrase Workbench Format):**  
   Once that elevator rhythm is in your fingers, you naturally think in complete mathematical phrases (`18.5 ENTER 4.2 ×`) rather than isolated keystrokes. In the table below—and throughout the rest of this book—each logical phrase is grouped onto a single compact row so you can track the physical subtotals at a glance. Executing `{{res:sc32_02_rpn_stack_dynamics_seq_01:keys}}` resolves the overall heat transfer coefficient to **`{{res:sc32_02_rpn_stack_dynamics_seq_01:value}}`** $\text{W/m}^2\text{K}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `18.5 {{key:ENTER}} 4.2 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $77.7000$ | First numerator term ($18.5 \times 4.2$) |
| `7.1 {{key:ENTER}} 9.6 {{key:×}}` | $0.0000$ | $0.0000$ | $77.7000$ | $68.1600$ | Second numerator term; 77.7 held in $Y$ |
| `{{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $145.8600$ | Total numerator in $X$ ($77.7 + 68.16$) |
| `14.3 {{key:ENTER}} 5.8 {{key:-}}` | $0.0000$ | $0.0000$ | $145.8600$ | $8.5000$ | Denominator ($14.3 - 5.8 = 8.5$) in $X$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$17.1600$** | Final heat transfer coefficient |

3. **Combined Reservoir Pipe Flow Rates ($T = 100 \parallel 220 \parallel 470 \parallel 1000\text{ min}$):**  
   Compare the two-branch fraction above—which needed Shelf $Z$ to hold the finished numerator while the denominator formed—with a four-pipe harmonic network where Pipe A ($100\text{ min}$), Pipe B ($220\text{ min}$), Pipe C ($470\text{ min}$), and Pipe D ($1,000\text{ min}$) fill a town reservoir together. Because the parallel-harmonic operator `{{key:x∥y}}` is associative, you never have to stack all four pipe times onto $T, Z, Y,$ and $X$ at once! Instead, keying the initial pair `{{res:sc32_02_rpn_stack_dynamics_seq_33:keys}}` collapses $100\text{ min}$ on Shelf $Y$ and $220\text{ min}$ on Shelf $X$ straight into their two-pipe harmonic time ($68.7500\text{ min}$) on Shelf $X$, returning Shelf $Y$ to zero and arming stack lift. Opening Pipe C (`470 {{key:x∥y}}` $\to 59.9768\text{ min}$) and Pipe D (`1000 {{key:x∥y}}`) in the full sequence `{{res:sc32_02_rpn_stack_dynamics_seq_02:keys}}` then folds each additional aqueduct into that running subtotal on Register $X$ (`68.7500` $\to$ `59.9768` $\to$ **`{{res:sc32_02_rpn_stack_dynamics_seq_02:value}}`** $\text{minutes}$), leaving Registers $Z$ and $T$ completely untouched from start to finish.

### Register T Constant Replication, Cyclic Roll, and LASTX Recovery

1. **Five-Year Compounding via Register $T$ Duplication ($A_n = 2500 \times 1.065^n$):**  
   Priming all four levels with the growth factor $1.065$ and tapping `{{key:×}}` five times via `{{res:sc32_02_rpn_stack_dynamics_seq_03:keys}}` compounds $\$2,500$ to **`{{res:sc32_02_rpn_stack_dynamics_seq_03:value}}`** at Year 5:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1.065 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $1.0650$ | $1.0650$ | Load annual compounding factor $1 + r = 1.065$ |
| `{{key:ENTER}} {{key:ENTER}}` | $1.0650$ | $1.0650$ | $1.0650$ | $1.0650$ | Replicate multiplier across all 4 stack levels |
| `2500 {{key:×}}` | $1.0650$ | $1.0650$ | $1.0650$ | $2,662.5000$ | Enter principal $P = \$2500$; Year 1 balance in $X$ |
| `{{key:×}}` | $1.0650$ | $1.0650$ | $1.0650$ | $2,835.5625$ | $T$ duplicates down; Year 2 balance in $X$ |
| `{{key:×}}` | $1.0650$ | $1.0650$ | $1.0650$ | $3,019.8741$ | Year 3 balance compounded via $T$-replication |
| `{{key:×}}` | $1.0650$ | $1.0650$ | $1.0650$ | $3,216.1659$ | Year 4 balance compounded |
| `{{key:×}}` | $1.0650$ | $1.0650$ | $1.0650$ | **$3,425.2167$** | Year 5 portfolio balance without re-entry |

2. **Blueprint Inch-to-Millimeter Pipeline ($x_{\text{mm}} = 25.4\,x_{\text{in}}$):**  
   Flooding the stack with `25.4` locks the conversion factor in Register $T$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `25.4 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $25.4000$ | $25.4000$ | Enter conversion constant $25.4\text{ mm/in}$ |
| `{{key:ENTER}} {{key:ENTER}}` | $25.4000$ | $25.4000$ | $25.4000$ | $25.4000$ | Flood entire stack with $25.4$ conversion factor |
| `0.375 {{key:×}}` | $25.4000$ | $25.4000$ | $25.4000$ | $9.5250$ | Convert $0.375\text{ in} \to 9.5250\text{ mm}$; $T$ replicates |
| `{{key:R↓}} 1.125 {{key:×}}` | $25.4000$ | $25.4000$ | $25.4000$ | $28.5750$ | Roll down $25.4$ into place; convert $1.125\text{ in} \to 28.5750\text{ mm}$ |
| `{{key:R↓}} 2.875 {{key:×}}` | $25.4000$ | $25.4000$ | $25.4000$ | $73.0250$ | Roll down $25.4$ into place; convert $2.875\text{ in} \to 73.0250\text{ mm}$ |
| `{{key:R↓}} 5.500 {{key:×}}` | $25.4000$ | $25.4000$ | $25.4000$ | **$139.7000$** | Roll down $25.4$ into place; convert $5.500\text{ in} \to 139.7000\text{ mm}$ |

3. **Cyclic 4-Register Carousel (`{{key:R↓}}`):**  
   Imagine you are logging four thermocouple channels along a heat-exchanger manifold ($T_1 = 21.5^\circ\text{C},\; T_2 = 24.8^\circ\text{C},\; T_3 = 28.2^\circ\text{C},\; T_4 = 31.0^\circ\text{C}$) and have loaded all four temperatures onto the stack ($T = 21.5,\; Z = 24.8,\; Y = 28.2,\; X = 31.0^\circ\text{C}$). Pressing `{{key:R↓}}` four consecutive times steps through every sensor channel in Register $X$ and restores the stack to its exact starting configuration:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `21.5 {{key:ENTER}} 24.8 {{key:ENTER}}` | $0.0000$ | $21.5000$ | $24.8000$ | $24.8000$ | Load sensor channels $T_1$ and $T_2$ into stack |
| `28.2 {{key:ENTER}} 31.0` | $21.5000$ | $24.8000$ | $28.2000$ | $31.0000$ | Load channels $T_3$ and $T_4$; all 4 channels primed |
| `{{key:R↓}}` | $31.0000$ | $21.5000$ | $24.8000$ | $28.2000$ | 1st roll down: channel $T_3 = 28.2^\circ\text{C}$ in $X$ |
| `{{key:R↓}}` | $28.2000$ | $31.0000$ | $21.5000$ | $24.8000$ | 2nd roll down: channel $T_2 = 24.8^\circ\text{C}$ in $X$ |
| `{{key:R↓}}` | $24.8000$ | $28.2000$ | $31.0000$ | $21.5000$ | 3rd roll down: channel $T_1 = 21.5^\circ\text{C}$ in $X$ |
| `{{key:R↓}}` | $21.5000$ | $24.8000$ | $28.2000$ | **$31.0000$** | 4th roll down: returns full cycle to $T_4 = 31.0^\circ\text{C}$ |

4. **Optical Diffraction Sinc Function via `{{key:LASTX}}` ($\operatorname{sinc}\theta = \frac{\sin\theta}{\theta}$):**  
   Why does an expression like $\operatorname{sinc} x = \frac{\sin x}{x}$—where the independent variable $x$ appears in both the numerator and the denominator—never require `{{key:ENTER}}` or upper stack shelves? Because `{{key:LASTX}}` acts as an automatic fifth shadow register! In radian mode (`{{key:RAD}}`), entering $0.42$ into Register $X$ and pressing `{{key:SIN}}` replaces $0.420000$ in Register $X$ with $\sin(0.42) = 0.407760$ while automatically preserving the pre-operator argument $0.420000$ inside the shadow register. Recalling that saved argument lifts $0.407760$ onto Shelf $Y$ and restores $0.420000$ onto Shelf $X$, so a single division resolves $\frac{\sin(0.42)}{0.42} = \mathbf{0.970858}$ while Registers $Z$ and $T$ stay completely empty. Applying that same four-stroke rhythm to Fraunhofer single-slit diffraction at $\theta = 0.085\text{ radians}$ via `{{res:sc32_02_rpn_stack_dynamics_seq_04:keys}}` resolves the central diffraction lobe amplitude to $\mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_04:value}}}$ without typing the angle twice (switch back to `{{key:DEG}}` afterward).

5. **Three-Phase Delta-to-Wye ($\Delta \to \text{Y}$) Transformation ($R_a = \frac{R_{12}R_{31}}{R_{12}+R_{23}+R_{31}}$):**  
   That same shadow-register behavior becomes even more powerful in dyadic subtraction and division, where `{{key:LASTX}}` captures the **second operand** ($X_{\text{old}}$)—letting you evaluate relative change $\frac{Y - X}{X}$ by subtracting $Y - X$ and immediately dividing by `{{key:LASTX}}`, or reuse a shared denominator across multiple branches. In Arthur Kennelly's three-phase $\Delta \to \text{Y}$ transformation for a closed $\Delta$ loop with $R_{12} = 30\,\Omega,\; R_{23} = 45\,\Omega,\; R_{31} = 60\,\Omega$, all three equivalent star branches share the identical perimeter denominator $S = R_{12} + R_{23} + R_{31} = 135\,\Omega$.

   Watch how `{{res:sc32_02_rpn_stack_dynamics_seq_14:keys}}` computes the first star branch $R_a$ while priming `{{key:LASTX}}` for the remaining two branches: first multiplying $R_{12}R_{31} = 30 \times 60 = 1,800\,\Omega^2$ on Shelf $X$, then accumulating the perimeter sum $S = 30 + 45 + 60 = 135\,\Omega$ on Shelf $X$ while $1,800\,\Omega^2$ rides up to Shelf $Z$ and drops back to Shelf $Y$, and finally dividing to resolve $R_a = 1,800 / 135 = \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_14:value}}\,\Omega}$ in Register $X$ **while automatically latching the shared perimeter divisor $135.0000\,\Omega$ inside `{{key:LASTX}}`**. You never have to add $30 + 45 + 60$ again: recalling $135\,\Omega$ from `{{key:LASTX}}` before forming each remaining pair product ($R_{12}R_{23} = 1,350\,\Omega^2$ and $R_{23}R_{31} = 2,700\,\Omega^2$) and swapping via `{{key:x⇄y}}` for division leaves all three equivalent wye impedances ($Z = 13.3333\,\Omega,\; Y = 10.0000\,\Omega,\; X = 20.0000\,\Omega$) aligned on the stack!

> **IEEE-754 Guard Rounding & 15-Digit Inspection (`{{key:SHOW}}`):** In raw 64-bit binary floating-point arithmetic, $0.1 + 0.2$ produces a tiny repeating-binary residual ($0.3000000000000000444\dots$). On the SC-32, 12-digit base-10 guard rounding ensures that `{{res:sc32_02_rpn_stack_dynamics_seq_32:keys}}` displays exact `0.3` on screen, while holding `{{key:SHOW}}` lets you inspect the full 15-digit internal mantissa whenever you are auditing numerical precision.

### Continued Fractions, Nested Radicals & Recall Arithmetic

1. **Symmetric Rational Function ($f(x) = \frac{x^2 - 1}{x^2 + 1}$ at $x = 3.75$):**  
   Computing $x^2 = 14.0625$ once and duplicating it across $Z$ and $Y$ via `{{res:sc32_02_rpn_stack_dynamics_seq_05:keys}}` produces **`{{res:sc32_02_rpn_stack_dynamics_seq_05:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3.75 {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $14.0625$ | Compute $x^2 = 14.0625$ |
| `{{key:ENTER}} {{key:ENTER}}` | $0.0000$ | $14.0625$ | $14.0625$ | $14.0625$ | Duplicate $x^2$ into $Y$ and $Z$ |
| `1 {{key:-}}` | $0.0000$ | $0.0000$ | $14.0625$ | $13.0625$ | Numerator $x^2 - 1$; $14.0625$ drops to $Y$ |
| `{{key:x⇄y}}` | $0.0000$ | $0.0000$ | $13.0625$ | $14.0625$ | Swap $x^2$ into $X$, numerator into $Y$ |
| `1 {{key:+}}` | $0.0000$ | $0.0000$ | $13.0625$ | $15.0625$ | Denominator $x^2 + 1 = 15.0625$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.867220$** | Final quotient $13.0625 / 15.0625$ |

2. **Climbing a Four-Story Continued Fraction ($x = 1 + \frac{1}{2 + \frac{1}{3 + \frac{1}{4}}}$), Zu Chongzhi's $\pi \approx \frac{355}{113}$, and the Golden Ratio $\varphi$:**  
   Why does a towering continued fraction—which looks on paper like four nested floors of division bars—leave Registers $Z$ and $T$ completely empty when evaluated from the bottom up? Because the unary reciprocal key `{{key:1/x}}` inverts each completed denominator **in place inside Register $X$**, and adding the next floor's integer immediately collapses $Y$ and $X$ back into a single number on Shelf $X$! Starting at the basement floor, keying `{{res:sc32_02_rpn_stack_dynamics_seq_34:keys}}` flips $4$ into $1/4 = 0.2500$ in Register $X$ and adds $3$ to form the third-floor denominator $3.2500$ ($13/4$) without leaving anything in Register $Y$. Continuing upward in the full sequence `{{res:sc32_02_rpn_stack_dynamics_seq_09:keys}}` alternates `{{key:1/x}}` and `{{key:+}}` right on the ground floor—flipping $13/4$ into $4/13 \approx 0.3077$, adding $2$ to reach $30/13 \approx 2.3077$, inverting to $13/30 \approx 0.4333$, and adding $1$ to land on **`{{res:sc32_02_rpn_stack_dynamics_seq_09:value}}`** ($43/30$) while Registers $Y, Z,$ and $T$ rest at zero.

   Applying this identical basement-up cadence to Archimedes's $\pi \approx 3 + 1/7 = 22/7$ or **Zu Chongzhi's $\pi \approx 3 + \frac{1}{7 + \frac{1}{15 + 1/1}}$** (starting at the deepest $1$, inverting and adding $15$, inverting and adding $7$, and inverting and adding $3$) lands on **`3.14159292035`**, where toggling fraction display mode `{{key:FDISP}}` reveals the exact reduced rational `3 16/113` ($\frac{355}{113}$). Likewise, flooding all four stack shelves with $1$ via `{{key:ENTER}}` turns Register $T$'s constant replication into an endless source of $1$'s, so repeating the two-keystroke rhythm `{{key:1/x}} {{key:+}}` steps through the Fibonacci convergents ($2.0000 \to 1.5000 \to 1.6667 \to 1.6000 \to 1.6250 \to 1.6154 \to \dots$) to the **Golden Ratio $\varphi = \mathbf{1.61803398875}$**.

3. **Nested Radical Quotient ($x = \sqrt{\frac{128.5 + \sqrt{48.2}}{19.4 - \sqrt{7.6}}}$):**  
   When an expression branches into an independent radical numerator and radical denominator, Registers $Z, Y,$ and $X$ work together as a three-level staging elevator. Evaluating the numerator first via `{{res:sc32_02_rpn_stack_dynamics_seq_35:keys}}` ($\to 135.44262$) and then assembling the denominator via `{{res:sc32_02_rpn_stack_dynamics_seq_36:keys}}` ($\to 16.64319$) pushes the completed numerator safely up to Shelf $Z$ while $19.4$ and $\sqrt{7.6} \approx 2.7568$ occupy $Y$ and $X$, before `{{key:-}}` drops $135.4426$ back to Shelf $Y$. Chaining both branches and extracting the outer square root in `{{res:sc32_02_rpn_stack_dynamics_seq_26:keys}}` then yields **`{{res:sc32_02_rpn_stack_dynamics_seq_26:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `48.2 {{key:√x}} 128.5 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $135.4426$ | Numerator: $\sqrt{48.2} + 128.5 \approx 135.4426$ |
| `19.4 {{key:ENTER}} 7.6 {{key:√x}}` | $0.0000$ | $135.4426$ | $19.4000$ | $2.7568$ | Start denominator: enter 19.4; compute $\sqrt{7.6}$ |
| `{{key:-}}` | $0.0000$ | $0.0000$ | $135.4426$ | $16.6432$ | Denominator: $19.4 - \sqrt{7.6} \approx 16.6432$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $8.1380$ | Divide numerator by denominator; radicand ratio |
| `{{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$2.8527$** | Extract outer square root; final radical quotient |

4. **Four-Story Continued Radical ($x = \sqrt{3 + \frac{5}{\sqrt{7 + \frac{11}{\sqrt{13 + 17}}}}}$):**  
   Contrast the two-branch fraction above with a four-story continued radical that mixes square roots and fraction bars at every level. Why does climbing outward from $\sqrt{13 + 17}$ via `{{res:sc32_02_rpn_stack_dynamics_seq_31:keys}}` never touch Registers $Z$ or $T$ at all? Because each inner radical becomes the *divisor* of the floor immediately above it, and swapping via `{{key:x⇄y}}` before division collapses each floor in place! Specifically, summing $13 + 17$ and pressing `{{key:√x}}` extracts the deepest root $\sqrt{30} \approx 5.4772$ in Register $X$. Entering the numerator $11$ next lifts $5.4772$ to Shelf $Y$, where `{{key:x⇄y}}` and division place $11 / \sqrt{30} \approx 2.0083$ back on Shelf $X$ with Shelf $Y$ cleared to zero. Adding $7$ and extracting the root forms the middle radical $\sqrt{9.0083} \approx 3.0014$ in place; dividing $5$ by that root yields $1.6659$; and adding $3$ before one final square root extracts $\sqrt{4.6659} \approx \mathbf{2.1601}$ ($2.160069$), leaving Registers $Z$ and $T$ completely free!

5. **Preserving a Full 4-Register Stack with Recall Arithmetic (`{{key:RCL}} {{key:×}} A`):**  
   With `2.5` stored in variable `A` (`2.5 {{key:STO}} A`) and all four stack registers $(T, Z, Y, X)$ occupied by active subtotals (`10 {{key:ENTER}} 20 {{key:ENTER}} 30 {{key:ENTER}} 40`, placing $T = 10, Z = 20, Y = 30, X = 40$), a standard `{{key:RCL}} A {{key:×}}` would lift the stack ($T \leftarrow 20, Z \leftarrow 30, Y \leftarrow 40, X \leftarrow 2.5$), **push $10$ off the top of Register $T$ forever**, and leave $T = 20, Z = 20, Y = 30, X = 100$. Keying `{{key:RCL}} {{key:×}} A` instead scales Register $X$ to $40 \times 2.5 = 100$ in place while preserving $T = 10, Z = 20, Y = 30$ intact:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2.5 {{key:STO}} A` | $0.0000$ | $0.0000$ | $0.0000$ | $2.5000$ | Store scale factor $2.5$ in variable `A`; lift armed |
| `10 {{key:ENTER}} 20 {{key:ENTER}}` | $2.5000$ | $10.0000$ | $20.0000$ | $20.0000$ | Load first two subtotals ($10$ and $20$) onto stack |
| `30 {{key:ENTER}} 40` | $10.0000$ | $20.0000$ | $30.0000$ | $40.0000$ | All 4 registers $(T, Z, Y, X)$ are now completely full |
| `{{key:RCL}} {{key:×}} A` | **$10.0000$** | **$20.0000$** | **$30.0000$** | **$100.0000$** | In-place $X \leftarrow 40 \times 2.5$ (`LASTX` = $40.0000$, `A` = $2.5000$); **$T = 10$ is preserved** |

6. **Indirect Register Addressing & Pointer Arithmetic via `i` and `(i)` (`{{key:STO}} i`, `{{key:RCL}} (i)`, `{{key:STO}} {{key:+}} (i)`):**  
   Store calibration offset $120.0$ in Variable `A` at slot $k = 1$ and $250.0$ in Variable `B` at slot $k = 2$. Loading $k = 1$ into index register `i` via `1 {{key:STO}} i`—tapping `{{key:.}}` for Alpha `i`—lets `{{key:RCL}} (i)` on `{{key:x∥y}}` dereference slot $1$ to return $120.0$. Incrementing the pointer in place with `1 {{key:STO}} {{key:+}} i` advances `i` to slot $2$, where `35 {{key:STO}} {{key:+}} (i)` and `{{key:RCL}} (i)` update and recall Variable `B` as $250 + 35 = 285.0$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `120 {{key:STO}} A` | $0.0000$ | $0.0000$ | $0.0000$ | $120.0000$ | Store $120.0$ in slot $1$ (`A`) |
| `250 {{key:STO}} B` | $0.0000$ | $0.0000$ | $120.0000$ | $250.0000$ | Store $250.0$ in slot $2$ (`B`) |
| `1 {{key:STO}} i` | $0.0000$ | $120.0000$ | $250.0000$ | $1.0000$ | Point index register `i` (`{{key:.}}`) to slot $k = 1$ (`A`) |
| `{{key:RCL}} (i)` | $120.0000$ | $250.0000$ | $1.0000$ | $120.0000$ | Indirect recall `RCL (i)` (`{{key:x∥y}}`) fetches `A` $= 120.0$ |
| `1 {{key:STO}} {{key:+}} i` | $250.0000$ | $1.0000$ | $120.0000$ | $1.0000$ | Increment pointer `i` in place to $k = 2$ (`B`) |
| `35 {{key:STO}} {{key:+}} (i)` | $1.0000$ | $120.0000$ | $1.0000$ | $35.0000$ | Indirect store-add updates `B` $\leftarrow 250 + 35 = 285$ |
| `{{key:RCL}} (i)` | $120.0000$ | $1.0000$ | $35.0000$ | **$285.0000$** | Indirect recall fetches updated slot $2$ (`B` $= \mathbf{285.0}$) |

### Multi-Register Engineering Synthesis

Once these stack movements become second nature, you stop seeing textbook formulas as isolated domain equations and start recognizing **three structural stack archetypes**. In each example below, notice how the inside-out plan determines which shelves of the stack come into play before a single key is pressed:

#### Archetype I — Inside-Out Radical & Reactance Scaling (Two Active Shelves, $Z$ and $T$ Free)
Whenever an equation multiplies an outer physical scale by a dimensionless inner radical, starting inside the radical resolves the entire formula across Registers $Y$ and $X$ without touching Registers $Z$ or $T$:

* **Hohmann Orbital Transfer ($\Delta v_1 = \sqrt{\frac{\mu}{r_1}}\left(\sqrt{\frac{2r_2}{r_1+r_2}} - 1\right)$):**
  To boost a spacecraft from low Earth parking orbit ($r_1 = 6,678\text{ km}$) to geostationary altitude ($r_2 = 42,164\text{ km}$, with gravitational parameter $\mu = 398,600\text{ km}^3/\text{s}^2$), start inside the dimensionless radius ratio $\frac{2r_2}{r_1+r_2} = \frac{84,328}{48,842} = 1.72655$. Extracting `{{key:√x}}` ($\to 1.31398$) and subtracting $1$ isolates the fractional velocity boost $0.31398$ on Shelf $X$; forming the circular orbital speed $\sqrt{\mu/r_1} = 7.72584\text{ km/s}$ on Shelf $X$ while $0.31398$ waits on Shelf $Y$ and multiplying delivers the perigee burn $\Delta v_1$ (a classic orbital sprint we revisit in **Chapter 14**):
  * **Perigee Boost Trace:** `{{res:sc32_02_rpn_stack_dynamics_seq_15:keys}}` $\to \Delta v_1 = \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_15:value}}\text{ km/s}}$.

* **First-Order High-Pass RC Filter Gain ($|H| = \frac{X}{\sqrt{1+X^2}}$, where $X = 2\pi f R C$):**
  For an audio network with $R = 10,000\,\Omega$ and $C = 15 \times 10^{-9}\text{ F}$ at $f = 2,500\text{ Hz}$, first form the dimensionless frequency ratio $X \approx 2.35619$ in Register $X$ and press `{{key:ENTER}}` once to copy $2.35619$ onto Shelf $Y$. Transforming Shelf $X$ in place via `{{key:x²}}`, `+ 1`, and `{{key:√x}}` produces the denominator $\sqrt{1 + X^2} \approx 2.55962$ right below the waiting numerator in $Y$:
  * **Filter Gain Trace:** `{{res:sc32_02_rpn_stack_dynamics_seq_22:keys}}` $\to |H| = \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_22:value}}}$.

#### Archetype II — Two-Branch Difference Over Reciprocal or Series Sum (Shelves $Z, Y, X$ in Concert)
Whenever a physical driving difference ($\Delta(T^4)$ or $\Delta T$) sits above a multi-term sum of thermal resistances, evaluate the numerator first so it rides up to Shelf $Z$ while the denominator terms meet on Shelves $Y$ and $X$:

* **Stefan-Boltzmann Radiative Heat Shield ($q = \frac{\sigma(T_1^4 - T_2^4)}{\frac{1}{\varepsilon_1} + \frac{1}{\varepsilon_2} - 1}$):**
  Between parallel spacecraft thermal shields at $T_1 = 800\text{ K}$ ($\varepsilon_1 = 0.85$) and $T_2 = 500\text{ K}$ ($\varepsilon_2 = 0.70$, $\sigma = 5.67037 \times 10^{-8}\text{ W/m}^2\text{K}^4$), subtracting $800^4 - 500^4 = 3.4710 \times 10^{11}\text{ K}^4$ and scaling by $\sigma$ places the driving radiant flux $19,681.8543\text{ W/m}^2$ on Shelf $X$. Next, the unary `{{key:1/x}}` key inverts $\varepsilon_1$ ($\to 1.1765$) and $\varepsilon_2$ ($\to 1.4286$) in place while the numerator rides safely up to Shelf $Z$; when their sum minus $1$ collapses to $1.6050$ on Shelf $X$, the numerator drops from $Z$ to $Y$ for division:
  * **Radiative Heat Flux Trace:** `{{res:sc32_02_rpn_stack_dynamics_seq_16:keys}}` $\to q = \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_16:value}}\text{ W/m}^2}$.

* **Composite Series Wall Conduction ($q = \frac{\Delta T}{R_1 + R_2 + R_3}$):**
  Across an insulated building envelope supporting a temperature drop $\Delta T = 22.0\text{ K}$ across interior air film ($R_1 = 0.08$), fiberglass batt ($R_2 = 2.20$), and exterior sheathing ($R_3 = 0.15\text{ m}^2\text{K/W}$), park $\Delta T = 22.0\text{ K}$ on Shelf $Y$ while accumulating the three series thermal resistances into $R_{\text{total}} = 2.4300\text{ m}^2\text{K/W}$ on Shelf $X$, then divide $Y$ by $X$:
  * **Conductive Heat Flux Trace:** `{{res:sc32_02_rpn_stack_dynamics_seq_24:keys}}` $\to q = \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_24:value}}\text{ W/m}^2}$.

#### Archetype III — Single-Shelf Multiplicative & Additive Cascades (Register $X$ Alone)
Finally, when a formula is a pure chain of factors, divisors, and in-place squares—or a running sum divided by a count—each step folds immediately into Register $X$ so Registers $Z$ and $T$ never leave zero:

* **Darcy-Weisbach Pipe Head Loss ($h_f = f\frac{L}{D}\frac{v^2}{2g}$):**
  Pumping water at $v = 2.4\text{ m/s}$ through an $L = 250\text{ m}$ cast-iron main of diameter $D = 0.30\text{ m}$ ($f = 0.022$, $g = 9.80665\text{ m/s}^2$) flows straight through Register $X$ in a single pass: form the dimensionless friction-length ratio $f L / D = 18.3333$, square the flow speed in place with `{{key:x²}}` ($\to 5.76\text{ m}^2/\text{s}^2$) to reach $105.60\text{ m}^2/\text{s}^2$, and divide by $2$ and $g$ step by step:
  * **Frictional Head Loss Trace:** `{{res:sc32_02_rpn_stack_dynamics_seq_17:keys}}` $\to h_f = \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_17:value}}\text{ m}}$.

* **Cantilever Steel Girder End Slope ($\theta = \frac{PL^2}{2EI}$):**
  Applying an end load $P = 12,000\text{ N}$ to a girder of span $L = 3.5\text{ m}$ and flexural rigidity $EI = 4.2 \times 10^6\text{ N}\cdot\text{m}^2$ follows the same single-register rhythm: square $L^2 = 12.25\text{ m}^2$ in place, multiply by $P$ to $147,000\text{ N}\cdot\text{m}^2$, divide by $2$ and $EI$ into $0.0175\text{ rad}$, and scale by $1,000$ for milliradians:
  * **Girder Tip Deflection Angle:** `{{res:sc32_02_rpn_stack_dynamics_seq_27:keys}}` $\to \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_27:value}}\text{ mrad}}$.

* **Zero-Sequence Three-Phase Fault Current ($I_0 = \frac{I_a + I_b + I_c}{3}$):**
  Across unbalanced feeder currents $I_a = 120\text{ A},\; I_b = 85\text{ A},\; I_c = 95\text{ A}$, fold $120 + 85 = 205.0\text{ A}$ and $+ 95 = 300.0\text{ A}$ directly on Shelf $X$ before dividing by $3$, isolating the neutral fault current without ever touching the upper half of the stack:
  * **Neutral Fault Current Trace:** `{{res:sc32_02_rpn_stack_dynamics_seq_20:keys}}` $\to I_0 = \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_20:value}}\text{ A}}$.

---

### Beyond Rational Fractions: When Nature Multiplies Repeatedly

Addition, subtraction, multiplication, and division—even when aided by `{{key:1/x}}`, `{{key:√x}}`, `{{key:LASTX}}`, two-way register arithmetic (`{{key:STO}} {{key:+}}`, `{{key:RCL}} {{key:×}}`), and the 89-slot indirect pointer `i` and `(i)`—eventually hit a physical wall. What happens when nature stops adding and starts **multiplying repeatedly** across twenty or a hundred orders of magnitude?

When planets sweep around the Sun, radioactive carbon-14 decays inside ancient parchment, sound waves roar across a stadium, or a deck of playing cards is shuffled into $52!$ arrangements, pressing `{{key:×}}` a thousand times in a row is out of the question. In **[Chapter 3: The Shortcut That Doubled the Lifespan of Astronomers](03-algebra-transcendentals.md)**, we travel to 1614 Scotland to meet a baron who discovered a hidden tunnel in mathematics—turning the hardest multiplications and fractional powers in the universe into simple addition.
