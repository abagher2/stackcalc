---
title: "Chapter 2: The Architecture of Inside-Out Thinking | Thinking in the Stack (SC-32)"
description: "George Miller's working-memory limit, Dijkstra's Shunting-Yard railway, combined work-rate problems, continued fractions, nested radicals, and 4-register XYZT stack dynamics on the StackCalc SC-32."
---

# Chapter 2: The Architecture of Inside-Out Thinking

## George Miller's Four Chunks and Dijkstra's Railway Yard

### The Four-Chunk Limit of Human Working Memory

A human being can glance at a four-item grocery list—*milk, apples, coffee, bread*—and walk through a supermarket without writing anything down, yet stall when staring at a four-layer algebraic fraction on a mathematics examination.

In 1956, Harvard cognitive psychologist George A. Miller published a foundational study on the limits of human information-processing capacity {{cite:miller1956}} and showed that *working memory*, the mental scratchpad where numbers and intermediate relationships are held during active reasoning, spans only about seven items. Subsequent experiments by cognitive scientists Nelson Cowan and John Sweller {{cite:sweller1988}} refined Miller's bound further: when a person is actively transforming quantities rather than reciting a static digit string, biological working memory holds only about four independent chunks at one time.

Evaluating a two-branch rational expression from left to right on paper or on an ordinary infix calculator exposes this bottleneck immediately:

$$U = \frac{(a \cdot b) + (c \cdot d)}{e - f}$$

Reading that equation strictly from left to right, in the order sixteenth-century typesetters printed it, consumes all four working-memory slots before arithmetic even begins. The opening bracket marks the numerator of a compound fraction in the first mental slot, while a second nested parenthesis opens to multiply $a \cdot b$ in the second slot. Next, the central `+` sign must be deferred in the third slot because the second product $(c \cdot d)$ has not yet been evaluated, and the division bar `÷ (` must likewise wait in the fourth slot until the denominator $(e - f)$ is complete. Before a single challenging operation has taken place, working memory is saturated with *suspended syntax*: open parentheses and deferred operators waiting for their right-hand operands.

Evaluating that same fraction from the inside out eliminates the suspended syntax altogether: multiplying $a \cdot b$ forms a completed product $P_1$ in one register; multiplying $c \cdot d$ forms $P_2$ and adds the two products into the completed numerator $N = P_1 + P_2$, which immediately frees the second register; and subtracting $D = e - f$ prepares the denominator for the final division $N \div D$. At no point does the mind hold more than three numbers simultaneously, and at no point does it track an unclosed parenthesis.

### Edsger Dijkstra's 1961 Railway Siding

Humans are not the only ones impeded by left-to-right infix notation. Digital processors cannot evaluate infix equations in left-to-right order either.

In 1960 and 1961, Dutch computer scientist Edsger W. Dijkstra {{cite:dijkstra1961}} and his colleague Jaap Zonneveld were writing the first ALGOL 60 compiler on an Electrologica X1 computer at the Mathematical Centre in Amsterdam. Faced with teaching a digital machine with limited magnetic-core memory to parse formulas such as $A + B \times C$ in a single left-to-right pass, Dijkstra noted that a processor cannot add $A$ and $B$ the moment it encounters the `+` sign, because `×` carries higher operator precedence (`PEMDAS`). The compiler must shunt the `+` sign onto a temporary waiting track, much like freight cars in a railway switchyard, until $B \times C$ has been coupled together.

Dijkstra named this translation method the *Shunting-Yard Algorithm*. As an incoming sequence of tokens (`a`, `×`, `b`, `+`, `c`, `×`, `d`) arrives from left to right along a main track, each numeric operand passes directly to the output queue, whereas each operator (`×`, `+`, `÷`) or left parenthesis `(` is diverted onto a last-in, first-out operator siding to wait until its right-hand operands have passed. Only when an operation of equal or higher precedence completes, or when a closing right parenthesis `)` arrives to clear the siding, do the waiting operators roll back onto the main output track behind their operands:

$$\text{Infix Input: } (a \times b) + (c \times d) \quad \xrightarrow{\text{Shunting Yard}} \quad \text{Postfix Output: } a \;\; b \;\; \times \;\; c \;\; d \;\; \times \;\; +$$

In the postfix sequence emerging from Dijkstra's shunting yard on the right, every parenthesis has been discarded, producing the chronological postfix order developed from Łukasiewicz {{cite:lukasiewicz1924}} and Burks, Warren, and Wright {{cite:burks1954}} to Charles Hamblin's hardware push-down stack {{cite:hamblin1957}}. Whenever an equation is entered into Python, Java, C++, JavaScript, or an algebraic pocket calculator followed by `=`, an internal shunting-yard parser translates the left-to-right infix text into postfix stack instructions before any arithmetic takes place, a mechanism that powers the Java Virtual Machine (JVM), WebAssembly (Wasm), Adobe PostScript, and spacecraft Forth navigation computers {{cite:knuth1997,hp15c1982}}.

When Bill Hewlett and David Cochran designed the HP-35 in 1972 {{cite:hewlett1972,cochran1972}}, they joined George Miller's cognitive limit with Edsger Dijkstra's compiler architecture. Rather than requiring the user to hold open parentheses in working memory while an internal parser translates infix keystrokes back into a postfix stack, they exposed the four-register stack ($X, Y, Z, T$) directly on the instrument so that every intermediate subtotal appears as soon as it is formed.

---

## Unpeeling Rational Expressions and Harmonic Work Rates

Four visible registers ($X, Y, Z, T$) evaluate any rational expression in algebra or engineering through the paired mechanics of stack lift and stack drop.

{{blocks:sc32_concept_stack_elevator|Inside-out expression tree evaluation paired with the four-register operational stack (T, Z, Y, X).}}

### Stack-Lift State Transitions: Neutral After ENTER, Armed After Operators

Across the four vertical registers, every stack lift shifts subtotals upward toward Register $T$, and every dyadic (two-operand) operation drops waiting subtotals downward toward Register $X$:

| Stack Register | Architectural Role | Movement on Lift (`ENTER` / Armed Digit) | Movement on Dyadic Drop (`+`, `-`, `×`, `÷`, `yˣ`, `x∥y`) |
| :---: | :--- | :--- | :--- |
| **Register T (Line 4)** | **Top Register & Constant Source** | Receives $Z_{\text{old}}$ ($T_{\text{old}}$ shifts out in `4-LVL`) | Copies $T_{\text{old}}$ downward into $Z$ while remaining in $T$ |
| **Register Z (Line 3)** | **Upper Holding Register** | Receives $Y_{\text{old}}$ as a second branch starts | Drops $Z_{\text{old}}$ down into $Y$, ready to combine with $X$ |
| **Register Y (Line 2)** | **Pending Operand Register** | Receives $X_{\text{old}}$ (`ENTER` disables lift; armed digit lifts) | Consumed with $X_{\text{old}}$; receives $Z_{\text{old}}$ from Register $Z$ |
| **Register X (Line 1)** | **Active Register** | Holds copy on `ENTER` (overwritten by next digit) | Receives new result $f(Y_{\text{old}}, X_{\text{old}})$ and arms stack lift |

To govern how newly keyed numbers enter Register $X$, the stack-lift state machine transitions between two states: *Neutral* (`Stack Lift = FALSE`) after `ENTER`, and *Armed* (`Stack Lift = TRUE`) after any operator or function. To multiply $a$ by $b$, the user keys $a$ into Register $X$ and presses `ENTER` to terminate digit entry for the first operand. Pressing `ENTER` copies $a$ upward into Register $Y$ ($Y = a$) while $a$ remains displayed in Register $X$ ($X = a$), and sets the stack-lift state to neutral (`Stack Lift = FALSE`). Because Register $X$ still holds that duplicated copy of $a$, the next number keyed ($b$) overwrites Register $X$ in place so that $Y = a$ and $X = b$ sit ready for multiplication.

Pressing `×` then drops Register $Y$ ($a$) and combines it with Register $X$ ($b$) to form the product $P_1 = a b$ in Register $X$. Because $P_1$ is a completed result rather than a temporary duplicate from `ENTER`, every arithmetic operator or mathematical function sets the stack-lift state to armed (`Stack Lift = TRUE`). When the first digit of the next operand ($c$) is keyed, `ENTER` is not pressed: the armed stack automatically lifts $P_1$ into Register $Y$ so $c$ can occupy Register $X$. Pressing `ENTER` after $c$ and keying $d$ shifts the completed first branch ($P_1$) into Register $Z$ while $c$ and $d$ occupy Registers $Y$ and $X$. When `×` multiplies $P_2 = c d$ in Register $X$, the upper registers drop by one level and return $P_1$ from Register $Z$ into Register $Y$, where `+` sums $P_1 + P_2$ into the complete numerator $N$. Evaluating the denominator $D = e - f$ across the lower registers while $N$ waits in the upper registers then sets up the final division $N \div D$.

### Harmonic Work Rates and Parallel Reciprocals

This two-branch stack discipline clarifies a classic problem in algebra and hydraulics. Consider a civil engineer testing the emergency water supply for a town reservoir fed by two independent conduits: Pipe A, the main valley aqueduct, fills the empty reservoir alone in $100\text{ minutes}$, whereas Pipe B, an auxiliary river pump, fills the same reservoir alone in $220\text{ minutes}$. When the valves on both Pipe A and Pipe B are opened simultaneously, the two conduits work in parallel to fill the basin.

A common algebraic mistake is to average the two elapsed times ($(100 + 220)/2 = 160\text{ minutes}$) or add them ($320\text{ minutes}$). Physical reasoning rules out both results immediately {{cite:strogatz2012,ellenberg2014}}: if Pipe A alone fills the reservoir in $100\text{ minutes}$, opening a second pipe alongside it cannot make the filling take longer than $100\text{ minutes}$. Two conduits operating together must finish in less time than the faster single conduit ($T_{\text{together}} < 100\text{ minutes}$), because parallel conduits add their *volumetric flow rates* rather than their elapsed times.

Examining the flow rate per minute resolves the relationship directly. Because Pipe A fills $1\text{ reservoir}$ in $100\text{ minutes}$, in a single minute it fills a fraction of the basin equal to its reciprocal, $R_A = \frac{1}{100} = 0.0100\text{ reservoirs per minute}$. Because Pipe B fills $1\text{ reservoir}$ in $220\text{ minutes}$, in a single minute it contributes $R_B = \frac{1}{220} \approx 0.004545\text{ reservoirs per minute}$. With both valves open simultaneously, the per-minute flow rates sum directly to $R_{\text{total}} = R_A + R_B = \frac{1}{100} + \frac{1}{220} \approx 0.014545\text{ reservoirs per minute}$, and the total time $T_{\text{together}}$ required to fill $1\text{ whole reservoir}$ is the reciprocal of that combined rate:

$$T_{\text{together}} = \frac{1}{\frac{1}{100} + \frac{1}{220}} = \frac{100 \times 220}{100 + 220} = \frac{22,000}{320} = \mathbf{68.75\text{ minutes}}$$

When the town opens two additional backup conduits—Pipe C, requiring $470\text{ minutes}$ alone, and Pipe D, requiring $1,000\text{ minutes}$ alone—those four time constants ($100, 220, 470,$ and $1,000$) obey the exact same harmonic reciprocal-sum law as $100\,\Omega, 220\,\Omega,$ and $470\,\Omega$ electrical resistors wired in parallel. Each additional pipe contributes its reciprocal rate, $\frac{1}{470}$ and $\frac{1}{1000}$, which shortens the combined filling time from $100\text{ minutes}$ for Pipe A alone to $68.75\text{ minutes}$ for Pipes A and B, $59.98\text{ minutes}$ with Pipe C added, and $\mathbf{56.58\text{ minutes}}$ with all four pipes open:

$$T_{\text{all four}} = \left(\frac{1}{100} + \frac{1}{220} + \frac{1}{470} + \frac{1}{1000}\right)^{-1} = 56.5831\text{ minutes}$$

Every harmonic system follows this three-step sequence—invert into rates, sum the rates, and invert back into the net quantity—or folds each additional branch into the running total with the associative product-over-sum operator $\frac{T_A T_B}{T_A + T_B}$.

---

## Continued Fractions, Zu Chongzhi's Rational Pi, and Viète's Nested Radicals

Alternating the reciprocal operator ($1/x$) with integer addition generates a fundamental structure in number theory known as a *continued fraction*. When Christiaan Huygens designed the brass gear trains of his astronomical planetarium in 1682 to match the orbital periods of Saturn and Earth, he expressed the target ratio as a four-tier continued fraction:

$$x = a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \frac{1}{a_3}}}$$

When read from the top down, a continued fraction presents a deeply nested hierarchy in which each denominator contains another rational expression. Keying that expression from the top down into an algebraic calculator (`a0 + 1 / ( a1 + 1 / ( a2 + 1 / a3 ) )`) requires opening a new parenthesis level at every tier and closing all of them at the end.

Evaluating that same structure from the innermost denominator upward eliminates every parenthesis. The calculation begins at the deepest partial denominator $a_3$ and inverts it in place into $r_3 = 1/a_3$. Adding the next tier's integer $a_2$ forms the intermediate denominator $d_2 = a_2 + r_3$, and inverting that sum in place ($r_2 = 1/d_2$) before adding $a_1$ yields $d_1 = a_1 + r_2$. One final inversion ($r_1 = 1/d_1$) followed by addition of the leading integer $a_0$ produces the convergent $x = a_0 + r_1$. No two branches ever compete for attention simultaneously; every stage alternates between a unary reciprocal and an addition in Register $X$.

### Zu Chongzhi's Rational Approximation $\pi \approx \frac{355}{113}$

Mathematicians from ancient Greece and fifth-century China to Christiaan Huygens and Srinivasa Ramanujan prized continued fractions because they generate the best possible rational approximations to any irrational number.

Applying Euclidean reciprocal extraction to $\pi = 3.14159265358979\dots$ exposes each convergent in succession. Subtracting the integer part $3$ isolates the fractional remainder $0.14159265\dots$, whose reciprocal ($1 / 0.14159265\dots$) is $7.0625133\dots$. Because $7.0625$ lies close to the integer $7$, truncating the expansion at the first tier yields Archimedes' classical approximation:

$$\pi \approx 3 + \frac{1}{7} = \frac{22}{7} \approx 3.142857 \quad (\text{accurate to } 2\text{ decimal places})$$

Subtracting $7$ from $7.0625133\dots$ isolates the next remainder $0.0625133\dots$, and inverting it ($1 / 0.0625133\dots$) produces $15.996594\dots$, which lies within $0.0035$ of the integer $16$ (or $15 + \frac{1}{1}$). Truncating immediately before the large subsequent partial denominator ($292$) produces a four-tier continued fraction:

$$\pi \approx 3 + \frac{1}{7 + \frac{1}{15 + \frac{1}{1}}} = 3 + \frac{1}{7 + \frac{1}{16}} = 3 + \frac{16}{113} = \mathbf{\frac{355}{113}} \approx \mathbf{3.14159292}$$

The rational approximation $\frac{355}{113}$ is easily recalled by writing the first three odd integers twice (`113355`) and dividing the second triplet by the first (`355 / 113`). Using only three-digit integers, $\frac{355}{113}$ matches $\pi$ to six decimal places, corresponding to an error of less than one-millionth of an inch per foot. Discovered in AD 480 by the Chinese mathematician and astronomer Zu Chongzhi (who called it the *Milü*, or close ratio), this convergent remained the most accurate rational approximation to $\pi$ known anywhere in the world for more than a millennium.

### The Golden Ratio $\varphi$ and Fibonacci Phyllotaxis

Because large partial denominators like $292$ inside a continued fraction indicate that an irrational number can be closely approximated by rationals, the irrational number that is hardest to approximate with fractions is the one whose partial denominators are as small as possible. That extremal number is the continued fraction whose partial denominators equal `1` at every tier:

$$\varphi = 1 + \frac{1}{1 + \frac{1}{1 + \frac{1}{1 + \frac{1}{1 + \dots}}}}$$

In that infinite expansion of $1$s, the sub-fraction beneath the uppermost division bar is identical to the entire continued fraction $\varphi$ itself, satisfying the quadratic self-similarity equation:

$$\varphi = 1 + \frac{1}{\varphi} \implies \varphi^2 - \varphi - 1 = 0 \implies \varphi = \frac{1 + \sqrt{5}}{2} \approx \mathbf{1.6180339887}$$

Evaluating this expansion from the bottom up by alternating `1/x` and `+ 1` generates the sequence of rational convergents step by step: the first stage gives $1 + \frac{1}{1} = \frac{2}{1} = 2.0000$, the second gives $1 + \frac{1}{2} = \frac{3}{2} = 1.5000$, the third gives $1 + \frac{2}{3} = \frac{5}{3} \approx 1.6667$, the fourth gives $1 + \frac{3}{5} = \frac{8}{5} = 1.6000$, and subsequent iterations trace $\frac{13}{8} = 1.6250 \to \frac{21}{13} \to \frac{34}{21} \to \frac{55}{34} \to \frac{89}{55} \approx \mathbf{1.618182}$. Every convergent is the ratio of two consecutive *Fibonacci numbers* ($1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89\dots$).

This number-theoretic extremal property governs botanical phyllotaxis. Across the center of a sunflower capitulum, a daisy, or a pine cone, the florets arrange themselves into two intersecting families of parastichy spirals, typically $34$ spirals curving clockwise and $55$ curving counterclockwise (or $55$ and $89$ on larger heads). As each primordium emerges at the meristem apex, it diverges from its predecessor by the golden angle ($360^\circ / \varphi^2 \approx 137.5^\circ$). Were the divergence angle a rational fraction of a circle such as $\frac{1}{4}$ or $\frac{22}{7}$, the seeds would align along $4$ or $7$ radial spokes separated by unpopulated gaps. Because $\varphi$ has only $1$s in its continued-fraction expansion, successive primordia never align along periodic radial rays, packing the growing disk at uniform areal density.

### François Viète's 1593 Nested Square-Root Cascade

In 1593, the French mathematician and royal cryptographer François Viète published the first exact analytical formula for $\pi$ in European mathematics. Viète expressed the area of a circle through an infinite product of nested square roots. Extending Archimedes' method of exhaustion, he inscribed a square ($4$ sides) inside a unit circle of radius $r = 1$ and repeatedly doubled the number of polygon sides to an octagon ($8$ sides), a $16$-gon, a $32$-gon, and a $64$-gon.

Each bisection of a central angle $\theta$ applies the half-angle cosine identity, enclosing the previous cosine expression inside an outer radical:

$$\cos\left(\frac{\theta}{2}\right) = \sqrt{\frac{1 + \cos\theta}{2}} = \frac{\sqrt{2 + 2\cos\theta}}{2}$$

Starting at a right angle $\theta_1 = 90^\circ$ ($\pi/2\text{ radians}$, where $\cos 90^\circ = 0$), successive bisections build a tower of nested radicals: the first bisection at $45^\circ$ (an octagon) gives $2\cos(45^\circ) = \sqrt{2 + 2\cos(90^\circ)} = \sqrt{2}$; the second bisection at $22.5^\circ$ (a $16$-gon) gives $2\cos(22.5^\circ) = \sqrt{2 + \sqrt{2}}$; the third bisection at $11.25^\circ$ (a $32$-gon) gives $2\cos(11.25^\circ) = \sqrt{2 + \sqrt{2 + \sqrt{2}}}$; and the fourth bisection at $5.625^\circ$ (a $64$-gon) reaches $2\cos(5.625^\circ) = \sqrt{2 + \sqrt{2 + \sqrt{2 + \sqrt{2}}}}$.

Comparing the area of each inscribed $2^n$-gon to the area of the circumscribed circle, Viète proved that the ratio $\frac{2}{\pi}$ is the infinite product of those nested cosine factors:

$$\frac{2}{\pi} = \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{2 + \sqrt{2}}}{2} \cdot \frac{\sqrt{2 + \sqrt{2 + \sqrt{2}}}}{2} \cdot \frac{\sqrt{2 + \sqrt{2 + \sqrt{2 + \sqrt{2}}}}}{2} \cdots$$

Like continued fractions, nested radical expressions—whether Viète's polygon product, a radical quotient such as $\sqrt{\frac{128.5 + \sqrt{48.2}}{19.4 - \sqrt{7.6}}}$, or a four-tier continued radical $\sqrt{3 + \frac{5}{\sqrt{7 + \frac{11}{\sqrt{13 + 17}}}}}$—require deep parenthesis nesting when written from the outside in, yet evaluate directly in Register $X$ when executed from the innermost radicand outward {{cite:cochran1972}}.

---

## Top-of-Stack Replication in Register T and Named Memory

At the top of the four-register stack, Register $T$ (Line 4) implements a retention rule that governs what happens when two operands in Registers $Y$ and $X$ combine and the upper registers drop by one level.

### T-Register Duplication and Iterative Constants

If Register $T$ cleared to zero every time the stack dropped, three consecutive dyadic operations would leave the upper registers empty. Instead, the architecture of the classic HP-32SII and HP-15C gives Register $T$ a structural property called *$T$-Register Duplication*:

$$\begin{aligned}
X_{\text{new}} &\leftarrow Y_{\text{old}} \text{ [op] } X_{\text{old}} \\
Y_{\text{new}} &\leftarrow Z_{\text{old}} \\
Z_{\text{new}} &\leftarrow T_{\text{old}} \\
T_{\text{new}} &\leftarrow T_{\text{old}} \quad \text{(Copied downward while remaining in } T\text{)}
\end{aligned}$$

Whenever a dyadic operation drops the stack, Register $T$ copies its value downward into Register $Z$ while retaining its own value in $T$. That single hardware rule supports three standard numerical idioms. First, in one-touch compound growth, filling all four registers with a growth factor $(1 + r)$ and keying the initial principal $P_0$ into Register $X$ allows every tap of `×` to advance the balance by one period ($P_1 \to P_2 \to P_3 \to \dots$), because Register $T$ feeds an endless stream of $(1 + r)$ multipliers down into Register $Y$.

Second, in repeated blueprint scaling, loading a unit conversion factor $k$ across the upper registers makes it possible to convert an entire table of machinist dimensions by keying each measurement, multiplying, and rolling the preserved constant $k$ back into position (`{{key:R↓}}`) for the next entry. Third, in fixed-point continued-fraction iteration, filling all four registers with a constant integer $a$ turns Register $T$ into a steady source of $a$'s for continued-fraction expansions ($a + 1/(a + 1/\dots)$), including the Fibonacci convergents of the Golden Ratio $\varphi$.

### Register Permutations, LASTX Recovery, and Storage Arithmetic

To reorder operands and manage intermediate constants without re-entry, the four stack registers are paired with in-place permutation keys, an automatic `LASTX` shadow register, and 26 lettered storage registers (`A`–`Z`) with indirect addressing.

The permutation keys `{{key:x⇄y}}`, `{{key:R↓}}`, and `{{key:R↑}}` rearrange values already on the stack. Pressing `{{key:x⇄y}}` exchanges Registers $Y$ and $X$ whenever a denominator or subtrahend is evaluated before its numerator or minuend: if a complicated denominator $D$ is computed first in Register $X$ and a simple numerator $N$ is keyed next (lifting $D$ into Register $Y$), pressing `{{key:÷}}` immediately would evaluate $D \div N$ rather than $N \div D$, whereas a single tap of `{{key:x⇄y}}` places $Y = N$ and $X = D$ so `{{key:÷}}` computes $N \div D$. The same swap restores operand order when a complicated subtrahend $B$ is evaluated before $A$ in $A - B$. Meanwhile, `{{key:R↓}}` (Roll Down) and `{{key:R↑}}` (Roll Up) cycle all four registers in a closed ring ($X \leftarrow Y \leftarrow Z \leftarrow T \leftarrow X$) without losing a single digit:

$$\text{Roll Down (`R↓`): } (X, Y, Z, T) \leftarrow (Y, Z, T, X), \qquad \text{Roll Up (`R↑`): } (X, Y, Z, T) \leftarrow (T, X, Y, Z)$$

Because four consecutive rolls return every register to its original position, an engineer can load four thermocouple readings onto the stack, cycle through them with `{{key:R↓}}` to inspect each value at full precision, and then press `{{key:+}} {{key:+}} {{key:+}} 4 {{key:÷}}` to compute their four-point ensemble mean.

Alongside the four visible registers, every operation that modifies Register $X$ automatically saves the previous occupant of Register $X$ inside the shadow register `{{key:LASTX}}`. If an unintended operator or function key is pressed, `{{key:LASTX}}` recovers the input operand immediately. Whenever a formula uses the same variable $x$ or a shared divisor twice—as in the optical diffraction sinc function $\frac{\sin\theta}{\theta}$, the symmetric rational function $\frac{x^2 - 1}{x^2 + 1}$, the quadratic roots $\frac{-b \pm \sqrt{\Delta}}{2a}$, or Arthur Kennelly's 1899 three-phase Delta-to-Wye ($\Delta \to \text{Y}$) impedance transformation—`{{key:LASTX}}` acts as an automatic fifth register.

Kennelly's $\Delta \to \text{Y}$ transformation illustrates how `{{key:LASTX}}` eliminates redundant summation: when three resistors $R_{12}, R_{23}, R_{31}$ are wired in a closed delta ($\Delta$) inside a Wheatstone bridge or a three-phase industrial motor starter, neither series nor parallel rules apply in isolation. Converting the delta into an equivalent three-branch star ($\text{Y}$) requires dividing each adjacent pair product by the shared perimeter sum $S = R_{12} + R_{23} + R_{31}$:

$$R_a = \frac{R_{12} R_{31}}{R_{12} + R_{23} + R_{31}}, \qquad R_b = \frac{R_{12} R_{23}}{R_{12} + R_{23} + R_{31}}, \qquad R_c = \frac{R_{23} R_{31}}{R_{12} + R_{23} + R_{31}}$$

Because any division $N \div S$ automatically captures its divisor $S$ inside `LASTX`, evaluating the first wye branch $R_a$ latches the perimeter sum $S$ inside `LASTX` as a byproduct of the division, so $R_b$ and $R_c$ can be evaluated next by recalling `{{key:LASTX}}` instead of re-summing the three resistors.

When all four stack registers ($T, Z, Y, X$) hold live subtotals and Register $X$ must be combined with a constant stored in one of the 26 lettered variables `A`–`Z`, a standard `{{key:RCL}} A` would lift the stack by one level and push the occupant of Register $T$ off the top in `4-LVL` mode. To preserve all four stack levels, the SC-32 provides two-way in-place storage arithmetic that bypasses stack lift altogether. *Recall Arithmetic* (`{{key:RCL}}` followed by `+`, `-`, `×`, or `÷` and `A`) updates Register $X$ in place as $X \leftarrow X \text{ op } A$ while leaving Registers $Y, Z,$ and $T$ untouched. Conversely, *Store Arithmetic* (`{{key:STO}}` followed by `+`, `-`, `×`, or `÷` and `A`) updates Variable `A` in place as $A \leftarrow A \text{ op } X$.

In 1949, Tom Kilburn, Geoff Tootill, and Max Newman at the University of Manchester introduced the B-line index register on the Manchester Mark 1 and showed that instead of hard-wiring a fixed memory address (`A`, `B`, `C`) into an instruction sequence, a processor can hold an integer address $k$ inside a dedicated *index register (`i`)* and use *indirect addressing (`(i)`)* to reference whichever memory slot resides at address $k$.

On the SC-32, when `{{key:STO}}` or `{{key:RCL}}` activates the `A–Z` Alpha layer, the decimal point key `{{key:.}}` carries the Alpha label `i` (the index register itself) and the neighboring key `{{key:x∥y}}` carries the Alpha label `(i)` (the indirect pointer that dereferences $k = \lfloor \lvert i \rvert \rfloor$). Storing $2$ into `i` sets the pointer to slot $2$ (`B`), so `{{key:RCL}} (i)` recalls Variable `B`, `{{key:STO}} {{key:+}} (i)` adds Register $X$ into Variable `B`, and incrementing `i` by $1$ steps the pointer across all 89 slots of the calculator's unified memory map:

| Pointer Range $k = \lfloor \lvert i \rvert \rfloor$ | Target Memory Bank | Addressed Register / Content | Access Permissions |
| :---: | :--- | :--- | :--- |
| **`1` … `26`** | **Lettered Variables (`A–Z`)** | `1` = `A`, `2` = `B`, `3` = `C`, …, `26` = `Z` | Full Read / Write (`STO (i)`, `RCL (i)`, `x⇄? (i)`) |
| **`27`** | **Index Register (`i`)** | `27` = Index register `i` itself | Full Read / Write |
| **`28` … `33`** | **Statistical Accumulators** | `28` = $\Sigma n$, `29` = $\Sigma x$, `30` = $\Sigma y$, `31` = $\Sigma x^2$, `32` = $\Sigma y^2$, `33` = $\Sigma xy$ | Read / Write via `(i)` |
| **`34` … `39`** | **`POLY` Solver Roots** | `R34`–`R39` (Real & imaginary parts of roots $r_1, r_2, r_3$) | Read via `RCL (i)` |
| **`40` … `89`** | **Statistical Data Points** | `DATA0` (`40`) through `DATA49` (`89`) | Read via `RCL (i)` |
| **$k < 1$ or $k > 89$** | **Out of Bounds** | Displays `INVALID DATA` (Code 02) | N/A (Halts without stack corruption) |

Finally, the division key `{{key:÷}}` carries two six-operator relational test menus: left-shifted `{{key:x?y}}` compares Register $X$ against Register $Y$ (`x=y`, `x≠y`, `x>y`, `x<y`, `x≥y`, `x≤y`), while right-shifted `{{key:x?0}}` compares Register $X$ against zero (`x=0`, `x≠0`, `x>0`, `x<0`, `x≥0`, `x≤0`). On the live stack, any test flashes `YES` or `NO` non-destructively; inside the Equation Editor `{{key:EQN}}`, each test acts as Kenneth Iverson's Boolean indicator bracket $[P] \in \{1, 0\}$, returning `1.0` or `0.0` to model piecewise functions. Internally, the SC-32 computes in 64-bit IEEE-754 double precision ($53$ significand bits $\approx 15.95$ decimal digits) with a 12-digit guard-rounded display across `{{key:DISP}}` (`ALL`, `FIX`, `SCI`, `ENG`) and 15-digit inspection via `{{key:SHOW}}`.

### Selectable Stack Depth: Classic 4-LVL, Extended 8-LVL & Unbounded INF

In classic RPN calculator design, two distinct stack architectures emerged: the 1972 Corvallis four-register stack (`HP-35`, `HP-15C`, `HP-32SII`), where a fixed ceiling at Register $T$ duplicates downward on every dyadic drop to serve as an automatic constant source (`k ENTER ENTER ENTER`), and the 1987 RPL unbounded stack (`HP-28C`, `HP-48SX`), where an expandable Last-In, First-Out (`LIFO`) heap holds arbitrarily many subtotals without dropping upper values off the ceiling or duplicating the top register on drop. Through the `{{key:FLAGS}}` menu (`STACK` $\to$ `4-LVL`, `8-LVL`, or `INF`), the SC-32 supports both paradigms alongside an intermediate 8-register mode, and pressing `{{key:REGS}}` (`Left-Shift {{key:0}}`) inspects registers `R5`–`R8` or deeper `INF` stack levels above the four-line $T, Z, Y, X$ viewport:

| Mode ID | Architecture Name | Accessible Registers | Stack Drop Behavior | Recommended Application Zone |
| :---: | :--- | :--- | :--- | :--- |
| **4-LVL** | **Classic 4-Level Stack (Default)** | $X, Y, Z, T$ | Top-of-stack $T$-duplication on drop; full HP-32SII / HP-15C parity | Everyday engineering, Horner recurrences, constant scaling |
| **8-LVL** | **Extended 8-Level Stack** | $R_1 \dots R_8$ (with $R_1\text{--}R_4$ mapped to $X, Y, Z, T$) | Holds up to 8 real operands (or 4 complex pairs) before $R_8$ replication | Multi-branch complex phasor algebra, 5-to-8-register expressions |
| **INF** | **Unbounded Infinite Stack** | Dynamic heap allocation (up to 999 levels) | True LIFO stack; dyadic drop never duplicates; pulls from history | 5+ branch parallel networks, long product-sum series |

---

## Four-Register Stack Mechanics & Memory Architecture

Two transition rules govern every calculation on the stack: pressing `{{key:ENTER}}` sets stack lift to neutral so the next number keyed overwrites Register $X$, while any dyadic operator (`{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`) drops the upper registers by one level, replicates Register $T$ downward, and re-arms stack lift.

{{res:sc32_order_of_ops:screenshot|Real-time 4-register operational stack (T, Z, Y, X) displaying intermediate calculation states without deferred parentheses.}}

### Two-Branch Rational Fractions & Combined Reservoir Flow Rates

1. **Weighted Span Rational Fraction ($\frac{(45 \times 3) + (18 \times 4)}{15 - 3}$):**  
   Tracing every individual key press on its own row illustrates how `{{key:ENTER}}` disables stack lift so `3`, `4`, and `3` overwrite Register $X$ in place, how `{{key:×}}` and `{{key:-}}` drop the upper stack and re-arm stack lift, and how keying `18` and `15` automatically lifts completed subtotals into Register $Y$ by position alone:

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

2. **Two-Pass Heat Exchanger Thermal Balance ($U = \frac{(18.5 \times 4.2) + (7.1 \times 9.6)}{14.3 - 5.8}$):**  
   For a two-pass heat-exchanger balance $U = \frac{(18.5 \times 4.2) + (7.1 \times 9.6)}{14.3 - 5.8}$, grouping each logical phrase (`18.5 ENTER 4.2 ×`) onto a single row highlights the physical subtotals across Registers $Z, Y,$ and $X$. Executing `{{res:sc32_02_rpn_stack_dynamics_seq_01:keys}}` resolves the overall heat transfer coefficient to $\mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_01:value}}\text{ W/m}^2\text{K}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `18.5 {{key:ENTER}} 4.2 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $77.7000$ | First numerator term ($18.5 \times 4.2$) |
| `7.1 {{key:ENTER}} 9.6 {{key:×}}` | $0.0000$ | $0.0000$ | $77.7000$ | $68.1600$ | Second numerator term; 77.7 held in $Y$ |
| `{{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $145.8600$ | Total numerator in $X$ ($77.7 + 68.16$) |
| `14.3 {{key:ENTER}} 5.8 {{key:-}}` | $0.0000$ | $0.0000$ | $145.8600$ | $8.5000$ | Denominator ($14.3 - 5.8 = 8.5$) in $X$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$17.1600$** | Final heat transfer coefficient |

3. **Combined Reservoir Pipe Flow Rates ($T = 100 \parallel 220 \parallel 470 \parallel 1000\text{ min}$):**  
   Compare the two-branch thermal fraction, which required Register $Z$ to hold the finished numerator while the denominator formed, with the four-aqueduct town reservoir network ($100, 220, 470,$ and $1,000\text{ min}$). Because the parallel-harmonic operator `{{key:x∥y}}` is associative, all four pipe times never need to occupy $T, Z, Y,$ and $X$ simultaneously.

   Keying the initial pair `{{res:sc32_02_rpn_stack_dynamics_seq_33:keys}}` collapses $100\text{ min}$ in Register $Y$ and $220\text{ min}$ in Register $X$ directly into their two-pipe harmonic time ($68.7500\text{ min}$) in Register $X$, returning Register $Y$ to zero and arming stack lift. Opening Pipe C (`470 {{key:x∥y}}` $\to 59.9768\text{ min}$) and Pipe D (`1000 {{key:x∥y}}`) in the full sequence `{{res:sc32_02_rpn_stack_dynamics_seq_02:keys}}` then folds each additional aqueduct into that running subtotal in Register $X$ (`68.7500` $\to$ `59.9768` $\to \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_02:value}}\text{ minutes}}$) while Registers $Z$ and $T$ remain at zero from start to finish.

### Register T Constant Replication, Cyclic Roll, and LASTX Recovery

1. **Five-Year Compounding via Register $T$ Duplication ($A_n = 2500 \times 1.065^n$):**  
   Priming all four levels with the growth factor $1.065$ and tapping `{{key:×}}` five times via `{{res:sc32_02_rpn_stack_dynamics_seq_03:keys}}` compounds $\$2,500$ to $\mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_03:value}}}$ at Year 5:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1.065 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $1.0650$ | $1.0650$ | Load annual compounding factor $1 + r = 1.065$ |
| `{{key:ENTER}} {{key:ENTER}}` | $1.0650$ | $1.0650$ | $1.0650$ | $1.0650$ | Replicate multiplier across all 4 stack levels |
| `2500 {{key:×}}` | $1.0650$ | $1.0650$ | $1.0650$ | $2,662.5000$ | Enter principal $P = \$2500$; Year 1 balance in $X$ |
| `{{key:×}}` | $1.0650$ | $1.0650$ | $1.0650$ | $2,835.5625$ | $T$ duplicates down; Year 2 balance in $X$ |
| `{{key:×}}` | $1.0650$ | $1.0650$ | $1.0650$ | $3,019.8741$ | Year 3 balance compounded via $T$-replication |
| `{{key:×}}` | $1.0650$ | $1.0650$ | $1.0650$ | $3,216.1659$ | Year 4 balance compounded |
| `{{key:×}}` | $1.0650$ | $1.0650$ | $1.0650$ | **$3,425.2167$** | Year 5 portfolio balance without re-entry |

2. **Blueprint Inch-to-Millimeter Conversion Table ($x_{\text{mm}} = 25.4\,x_{\text{in}}$):**  
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
   When logging four thermocouple channels along a heat-exchanger manifold ($T_1 = 21.5^\circ\text{C},\; T_2 = 24.8^\circ\text{C},\; T_3 = 28.2^\circ\text{C},\; T_4 = 31.0^\circ\text{C}$) with all four temperatures loaded onto the stack ($T = 21.5,\; Z = 24.8,\; Y = 28.2,\; X = 31.0^\circ\text{C}$), pressing `{{key:R↓}}` four consecutive times steps through every sensor channel in Register $X$ and restores the stack to its exact starting configuration:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `21.5 {{key:ENTER}} 24.8 {{key:ENTER}}` | $0.0000$ | $21.5000$ | $24.8000$ | $24.8000$ | Load sensor channels $T_1$ and $T_2$ into stack |
| `28.2 {{key:ENTER}} 31.0` | $21.5000$ | $24.8000$ | $28.2000$ | $31.0000$ | Load channels $T_3$ and $T_4$; all 4 channels primed |
| `{{key:R↓}}` | $31.0000$ | $21.5000$ | $24.8000$ | $28.2000$ | 1st roll down: channel $T_3 = 28.2^\circ\text{C}$ in $X$ |
| `{{key:R↓}}` | $28.2000$ | $31.0000$ | $21.5000$ | $24.8000$ | 2nd roll down: channel $T_2 = 24.8^\circ\text{C}$ in $X$ |
| `{{key:R↓}}` | $24.8000$ | $28.2000$ | $31.0000$ | $21.5000$ | 3rd roll down: channel $T_1 = 21.5^\circ\text{C}$ in $X$ |
| `{{key:R↓}}` | $21.5000$ | $24.8000$ | $28.2000$ | **$31.0000$** | 4th roll down: returns full cycle to $T_4 = 31.0^\circ\text{C}$ |

4. **Optical Diffraction Sinc Function via `{{key:LASTX}}` ($\operatorname{sinc}\theta = \frac{\sin\theta}{\theta}$):**  
   An expression like $\operatorname{sinc} x = \frac{\sin x}{x}$, in which the independent variable $x$ appears in both the numerator and the denominator, never requires `{{key:ENTER}}` or the upper stack registers because `{{key:LASTX}}` acts as an automatic fifth shadow register. In radian mode (`{{key:RAD}}`), entering $0.42$ into Register $X$ and pressing `{{key:SIN}}` replaces $0.420000$ in Register $X$ with $\sin(0.42) = 0.407760$ while automatically preserving the pre-operator argument $0.420000$ inside the shadow register.

   Recalling that saved argument lifts $0.407760$ into Register $Y$ and restores $0.420000$ into Register $X$, so a single division resolves $\frac{\sin(0.42)}{0.42} = \mathbf{0.970858}$ while Registers $Z$ and $T$ stay empty. Applying that same four-stroke sequence to Fraunhofer single-slit diffraction at $\theta = 0.085\text{ radians}$ via `{{res:sc32_02_rpn_stack_dynamics_seq_04:keys}}` resolves the central diffraction lobe amplitude to $\mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_04:value}}}$ without keying the angle twice (switch back to `{{key:DEG}}` afterward).

5. **Three-Phase Delta-to-Wye ($\Delta \to \text{Y}$) Transformation ($R_a = \frac{R_{12}R_{31}}{R_{12}+R_{23}+R_{31}}$):**  
   That same shadow-register behavior applies directly to dyadic subtraction and division, where `{{key:LASTX}}` captures the *second operand* ($X_{\text{old}}$) and supports relative-change calculations $\frac{Y - X}{X}$ via subtraction followed immediately by division by `{{key:LASTX}}`, or reuse of a shared denominator across multiple branches. In Arthur Kennelly's three-phase $\Delta \to \text{Y}$ transformation for a closed $\Delta$ loop with $R_{12} = 30\,\Omega,\; R_{23} = 45\,\Omega,\; R_{31} = 60\,\Omega$, all three equivalent star branches share the identical perimeter denominator $S = R_{12} + R_{23} + R_{31} = 135\,\Omega$.

   Evaluating `{{res:sc32_02_rpn_stack_dynamics_seq_14:keys}}` computes the first star branch $R_a$ while priming `{{key:LASTX}}` for the remaining two branches: first multiplying $R_{12}R_{31} = 30 \times 60 = 1,800\,\Omega^2$ in Register $X$, then accumulating the perimeter sum $S = 30 + 45 + 60 = 135\,\Omega$ in Register $X$ while $1,800\,\Omega^2$ shifts up to Register $Z$ and drops back to Register $Y$, and finally dividing to resolve $R_a = 1,800 / 135 = \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_14:value}}\,\Omega}$ in Register $X$ while automatically latching the shared perimeter divisor $135.0000\,\Omega$ inside `{{key:LASTX}}`.

   The sum $30 + 45 + 60$ never needs to be keyed again: recalling $135\,\Omega$ from `{{key:LASTX}}` before forming each remaining pair product ($R_{12}R_{23} = 1,350\,\Omega^2$ and $R_{23}R_{31} = 2,700\,\Omega^2$) and swapping via `{{key:x⇄y}}` for division aligns all three equivalent wye impedances ($Z = 13.3333\,\Omega,\; Y = 10.0000\,\Omega,\; X = 20.0000\,\Omega$) on the stack.

   Twelve-digit base-10 guard rounding likewise suppresses repeating-binary residuals on the display: whereas raw 64-bit binary floating-point arithmetic evaluates $0.1 + 0.2$ as $0.3000000000000000444\dots$, executing `{{res:sc32_02_rpn_stack_dynamics_seq_32:keys}}` displays exact `0.3` on screen while holding `{{key:SHOW}}` exposes the full 15-digit internal significand whenever numerical precision is being audited.

### Continued Fractions, Nested Radicals & Recall Arithmetic

1. **Symmetric Rational Function ($f(x) = \frac{x^2 - 1}{x^2 + 1}$ at $x = 3.75$):**  
   Computing $x^2 = 14.0625$ once and duplicating it across $Z$ and $Y$ via `{{res:sc32_02_rpn_stack_dynamics_seq_05:keys}}` produces $\mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_05:value}}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3.75 {{key:x²}}` | $0.0000$ | $0.0000$ | $0.0000$ | $14.0625$ | Compute $x^2 = 14.0625$ |
| `{{key:ENTER}} {{key:ENTER}}` | $0.0000$ | $14.0625$ | $14.0625$ | $14.0625$ | Duplicate $x^2$ into $Y$ and $Z$ |
| `1 {{key:-}}` | $0.0000$ | $0.0000$ | $14.0625$ | $13.0625$ | Numerator $x^2 - 1$; $14.0625$ drops to $Y$ |
| `{{key:x⇄y}}` | $0.0000$ | $0.0000$ | $13.0625$ | $14.0625$ | Swap $x^2$ into $X$, numerator into $Y$ |
| `1 {{key:+}}` | $0.0000$ | $0.0000$ | $13.0625$ | $15.0625$ | Denominator $x^2 + 1 = 15.0625$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.867220$** | Final quotient $13.0625 / 15.0625$ |

2. **Evaluating a Four-Level Continued Fraction ($x = 1 + \frac{1}{2 + \frac{1}{3 + \frac{1}{4}}}$), Zu Chongzhi's $\pi \approx \frac{355}{113}$, and the Golden Ratio $\varphi$:**  
   Evaluating the four-level continued fraction $1 + \frac{1}{2 + \frac{1}{3 + 1/4}}$ confirms that Registers $Z$ and $T$ remain empty from start to finish: the unary reciprocal key `{{key:1/x}}` inverts each completed denominator in place inside Register $X$, and adding the next tier's integer immediately collapses $Y$ and $X$ back into a single number in Register $X$.

   Starting at the innermost denominator, keying `{{res:sc32_02_rpn_stack_dynamics_seq_34:keys}}` inverts $4$ into $1/4 = 0.2500$ in Register $X$ and adds $3$ to form the intermediate denominator $3.2500$ ($13/4$) with Register $Y$ cleared to zero. Continuing upward in the full sequence `{{res:sc32_02_rpn_stack_dynamics_seq_09:keys}}` alternates `{{key:1/x}}` and `{{key:+}}` directly in Register $X$—inverting $13/4$ into $4/13 \approx 0.3077$, adding $2$ to reach $30/13 \approx 2.3077$, inverting to $13/30 \approx 0.4333$, and adding $1$ to land on $\mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_09:value}}}$ ($43/30$) while Registers $Y, Z,$ and $T$ remain at zero.

   Applying this identical inside-out cadence to Archimedes' $\pi \approx 3 + 1/7 = 22/7$ or Zu Chongzhi's *Milü* $\pi \approx 3 + \frac{1}{7 + \frac{1}{15 + 1/1}}$ (starting at the deepest $1$, inverting and adding $15$, inverting and adding $7$, and inverting and adding $3$) yields `3.14159292035`, where toggling fraction display mode `{{key:FDISP}}` reveals the exact reduced rational `3 16/113` ($\frac{355}{113}$). Likewise, filling all four stack registers with $1$ via `{{key:ENTER}}` uses Register $T$'s constant replication to supply an endless stream of $1$'s, so repeating the two-keystroke sequence `{{key:1/x}} {{key:+}}` steps through the Fibonacci convergents ($2.0000 \to 1.5000 \to 1.6667 \to 1.6000 \to 1.6250 \to 1.6154 \to \dots$) to the Golden Ratio $\varphi = \mathbf{1.61803398875}$.

3. **Nested Radical Quotient ($x = \sqrt{\frac{128.5 + \sqrt{48.2}}{19.4 - \sqrt{7.6}}}$):**  
   When an expression branches into an independent radical numerator and radical denominator, Registers $Z, Y,$ and $X$ coordinate across three levels. Evaluating the numerator first via `{{res:sc32_02_rpn_stack_dynamics_seq_35:keys}}` ($\to 135.44262$) and then assembling the denominator via `{{res:sc32_02_rpn_stack_dynamics_seq_36:keys}}` ($\to 16.64319$) pushes the completed numerator up to Register $Z$ while $19.4$ and $\sqrt{7.6} \approx 2.7568$ occupy $Y$ and $X$, before `{{key:-}}` drops $135.4426$ back to Register $Y$. Chaining both branches and extracting the outer square root in `{{res:sc32_02_rpn_stack_dynamics_seq_26:keys}}` then yields $\mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_26:value}}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `48.2 {{key:√x}} 128.5 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $135.4426$ | Numerator: $\sqrt{48.2} + 128.5 \approx 135.4426$ |
| `19.4 {{key:ENTER}} 7.6 {{key:√x}}` | $0.0000$ | $135.4426$ | $19.4000$ | $2.7568$ | Start denominator: enter 19.4; compute $\sqrt{7.6}$ |
| `{{key:-}}` | $0.0000$ | $0.0000$ | $135.4426$ | $16.6432$ | Denominator: $19.4 - \sqrt{7.6} \approx 16.6432$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $8.1380$ | Divide numerator by denominator; radicand ratio |
| `{{key:√x}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$2.8527$** | Extract outer square root; final radical quotient |

4. **Four-Level Continued Radical ($x = \sqrt{3 + \frac{5}{\sqrt{7 + \frac{11}{\sqrt{13 + 17}}}}}$):**  
   Contrast that two-branch radical fraction with a four-level continued radical that mixes square roots and fraction bars at every tier. Working outward from $\sqrt{13 + 17}$ via `{{res:sc32_02_rpn_stack_dynamics_seq_31:keys}}` never touches Registers $Z$ or $T$ because each inner radical becomes the *divisor* of the tier immediately above it, and swapping via `{{key:x⇄y}}` before division collapses each tier in place.

   Specifically, summing $13 + 17$ and pressing `{{key:√x}}` extracts the deepest root $\sqrt{30} \approx 5.4772$ in Register $X$. Entering the numerator $11$ next lifts $5.4772$ into Register $Y$, where `{{key:x⇄y}}` and division place $11 / \sqrt{30} \approx 2.0083$ back in Register $X$ with Register $Y$ cleared to zero. Adding $7$ and extracting the root forms the middle radical $\sqrt{9.0083} \approx 3.0014$ in place; dividing $5$ by that root yields $1.6659$; and adding $3$ before one final square root extracts $\sqrt{4.6659} \approx \mathbf{2.1601}$ ($2.160069$) while Registers $Z$ and $T$ remain at zero.

5. **Preserving a Full 4-Register Stack with Recall Arithmetic (`{{key:RCL}} {{key:×}} A`):**  
   With `2.5` stored in variable `A` (`2.5 {{key:STO}} A`) and all four stack registers $(T, Z, Y, X)$ occupied by active subtotals (`10 {{key:ENTER}} 20 {{key:ENTER}} 30 {{key:ENTER}} 40`, placing $T = 10, Z = 20, Y = 30, X = 40$), a standard `{{key:RCL}} A {{key:×}}` would lift the stack ($T \leftarrow 20, Z \leftarrow 30, Y \leftarrow 40, X \leftarrow 2.5$), discard $10$ from the top of Register $T$ across successive operations, and leave $T = 20, Z = 20, Y = 30, X = 100$. Keying `{{key:RCL}} {{key:×}} A` instead scales Register $X$ to $40 \times 2.5 = 100$ in place while preserving $T = 10, Z = 20, Y = 30$ intact:

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

Across scientific and engineering domains, algebraic formulas fall into three recurring stack-utilization patterns determined by the depth of their expression trees:

#### Inside-Out Radical & Reactance Scaling (Two Active Registers, Z and T Free)
Whenever an equation multiplies an outer physical scale by a dimensionless inner radical, starting inside the radical resolves the entire formula across Registers $Y$ and $X$ without touching Registers $Z$ or $T$:

* **Hohmann Orbital Transfer ($\Delta v_1 = \sqrt{\frac{\mu}{r_1}}\left(\sqrt{\frac{2r_2}{r_1+r_2}} - 1\right)$):**
  To boost a spacecraft from low Earth parking orbit ($r_1 = 6,678\text{ km}$) to geostationary altitude ($r_2 = 42,164\text{ km}$, with gravitational parameter $\mu = 398,600\text{ km}^3/\text{s}^2$), start inside the dimensionless radius ratio $\frac{2r_2}{r_1+r_2} = \frac{84,328}{48,842} = 1.72655$. Extracting `{{key:√x}}` ($\to 1.31398$) and subtracting $1$ isolates the fractional velocity boost $0.31398$ in Register $X$; forming the circular orbital speed $\sqrt{\mu/r_1} = 7.72584\text{ km/s}$ in Register $X$ while $0.31398$ waits in Register $Y$ and multiplying delivers the perigee burn $\Delta v_1$:
  * **Perigee Velocity Impulse:** `{{res:sc32_02_rpn_stack_dynamics_seq_15:keys}}` $\to \Delta v_1 = \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_15:value}}\text{ km/s}}$.

* **First-Order High-Pass RC Filter Gain ($|H| = \frac{X}{\sqrt{1+X^2}}$, where $X = 2\pi f R C$):**
  For an audio network with $R = 10,000\,\Omega$ and $C = 15 \times 10^{-9}\text{ F}$ at $f = 2,500\text{ Hz}$, first form the dimensionless frequency ratio $X \approx 2.35619$ in Register $X$ and press `{{key:ENTER}}` once to copy $2.35619$ into Register $Y$. Transforming Register $X$ in place via `{{key:x²}}`, `+ 1`, and `{{key:√x}}` produces the denominator $\sqrt{1 + X^2} \approx 2.55962$ directly below the waiting numerator in $Y$:
  * **High-Pass Gain Evaluation:** `{{res:sc32_02_rpn_stack_dynamics_seq_22:keys}}` $\to |H| = \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_22:value}}}$.

#### Two-Branch Difference Over Reciprocal or Series Sum (Registers Z, Y, X in Concert)
Whenever a physical driving difference ($\Delta(T^4)$ or $\Delta T$) sits above a multi-term sum of thermal resistances, evaluate the numerator first so it shifts up to Register $Z$ while the denominator terms combine in Registers $Y$ and $X$:

* **Stefan-Boltzmann Radiative Heat Shield ($q = \frac{\sigma(T_1^4 - T_2^4)}{\frac{1}{\varepsilon_1} + \frac{1}{\varepsilon_2} - 1}$):**
  Between spacecraft shields at $T_1 = 800\text{ K}$ ($\varepsilon_1 = 0.85$) and $T_2 = 500\text{ K}$ ($\varepsilon_2 = 0.70$, $\sigma = 5.67037 \times 10^{-8}\text{ W/m}^2\text{K}^4$), scaling $800^4 - 500^4 = 3.4710 \times 10^{11}\text{ K}^4$ by $\sigma$ places radiant flux $19,681.8543\text{ W/m}^2$ in Register $X$. Next, `{{key:1/x}}` inverts $\varepsilon_1$ ($1.1765$) and $\varepsilon_2$ ($1.4286$) in place while the numerator waits in $Z$; when their sum minus $1$ collapses to $1.6050$ in $X$, the numerator drops from $Z$ to $Y$ for division:
  * **Radiative Heat Flux:** `{{res:sc32_02_rpn_stack_dynamics_seq_16:keys}}` $\to q = \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_16:value}}\text{ W/m}^2}$.

* **Composite Series Wall Conduction ($q = \frac{\Delta T}{R_1 + R_2 + R_3}$):**
  Across an envelope supporting $\Delta T = 22.0\text{ K}$ over air film ($R_1 = 0.08$), fiberglass ($R_2 = 2.20$), and sheathing ($R_3 = 0.15\text{ m}^2\text{K/W}$), hold $\Delta T = 22.0\text{ K}$ in Register $Y$ while summing $R_{\text{total}} = 2.4300\text{ m}^2\text{K/W}$ in Register $X$, then divide:
  * **Conductive Heat Flux:** `{{res:sc32_02_rpn_stack_dynamics_seq_24:keys}}` $\to q = \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_24:value}}\text{ W/m}^2}$.

#### Single-Register Multiplicative & Additive Cascades (Register X Alone)
When a formula is a chain of factors, divisors, and in-place squares—or a running sum divided by a count—each step folds into Register $X$ so $Z$ and $T$ remain at zero:

* **Darcy-Weisbach Pipe Head Loss ($h_f = f\frac{L}{D}\frac{v^2}{2g}$):**
  Pumping water at $v = 2.4\text{ m/s}$ through an $L = 250\text{ m}$ main of diameter $D = 0.30\text{ m}$ ($f = 0.022$, $g = 9.80665\text{ m/s}^2$) forms $f L / D = 18.3333$, squares $v^2 = 5.76\text{ m}^2/\text{s}^2$ in place ($\to 105.60\text{ m}^2/\text{s}^2$), and divides by $2$ and $g$:
  * **Frictional Head Loss:** `{{res:sc32_02_rpn_stack_dynamics_seq_17:keys}}` $\to h_f = \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_17:value}}\text{ m}}$.

* **Cantilever Steel Girder End Slope ($\theta = \frac{PL^2}{2EI}$):**
  Applying an end load $P = 12,000\text{ N}$ to a girder of span $L = 3.5\text{ m}$ and flexural rigidity $EI = 4.2 \times 10^6\text{ N}\cdot\text{m}^2$ squares $L^2 = 12.25\text{ m}^2$ in place, multiplies by $P$ ($147,000\text{ N}\cdot\text{m}^2$), divides by $2$ and $EI$ ($0.0175\text{ rad}$), and scales by $1,000$:
  * **Girder Tip Deflection Angle:** `{{res:sc32_02_rpn_stack_dynamics_seq_27:keys}}` $\to \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_27:value}}\text{ mrad}}$.

* **Zero-Sequence Three-Phase Fault Current ($I_0 = \frac{I_a + I_b + I_c}{3}$):**
  Across unbalanced feeder currents $I_a = 120\text{ A},\; I_b = 85\text{ A},\; I_c = 95\text{ A}$, summing $120 + 85 + 95 = 300.0\text{ A}$ in Register $X$ and dividing by $3$ isolates the neutral fault current without touching the upper stack:
  * **Neutral Fault Current:** `{{res:sc32_02_rpn_stack_dynamics_seq_20:keys}}` $\to I_0 = \mathbf{{{res:sc32_02_rpn_stack_dynamics_seq_20:value}}\text{ A}}$.

Across every algebraic structure—single-register cascades, two-register harmonic folds, three-register rational quotients, and four-register Horner recurrences—the operational stack aligns the sequence of keystrokes with the dependency order of the quantities themselves. Once operands and subtotals remain visible across $X, Y, Z,$ and $T$, parentheses disappear because every intermediate magnitude is formed and inspected in the exact order that nature combines it.
