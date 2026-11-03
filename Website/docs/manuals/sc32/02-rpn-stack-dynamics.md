---
title: "Chapter 2: The Architecture of Inside-Out Thinking | Thinking in the Stack (SC-32)"
description: "George Miller's working-memory limit, Dijkstra's Shunting-Yard railway, formal stack-lift state mechanics, continued fractions, nested radicals, and 4-register XYZT stack dynamics on the StackCalc SC-32."
---

# Chapter 2: The Architecture of Inside-Out Thinking

In the autumn of 1960 at the Mathematical Centre in Amsterdam, twenty-nine-year-old Dutch computer scientist Edsger W. Dijkstra confronted a fundamental mismatch between printed algebra and live computation {{cite:dijkstra1961}}. Tasked with writing one of the world's first ALGOL 60 compilers, Dijkstra had to teach a digital processor with limited memory to translate algebraic formulas like $A + B \times C$ into executable machine instructions while reading from left to right. A processor cannot add $A$ and $B$ the moment it encounters the `+` sign, because `×` carries higher operator precedence (`PEMDAS`). The compiler must shunt the `+` sign onto a temporary waiting track—much like freight cars in a railway switchyard—until $B \times C$ has been coupled together.

Why do both digital processors and human minds stall on left-to-right parenthetical formulas? Four years before Dijkstra built his railway shunting yard, Harvard cognitive psychologist George A. Miller published a landmark study on the limits of human information-processing capacity {{cite:miller1956}}, showing that *working memory*—the mental scratchpad where numbers and relationships are held during active reasoning—spans only about seven items. Subsequent experiments by Nelson Cowan and John Sweller {{cite:sweller1988}} refined Miller's bound further: a person can glance at a four-item grocery list (*milk, apples, coffee, bread*) and walk through a supermarket without writing anything down, yet stall on a four-layer algebraic fraction because biological working memory holds only about **four active chunks** at one time.

## Why Nested Parentheses Exhaust Working Memory

A two-branch rational expression worked from left to right on paper or on an ordinary infix calculator exposes this four-item bottleneck:

$$U = \frac{(a \cdot b) + (c \cdot d)}{e - f}$$

When read from left to right in the order sixteenth-century typesetters printed it, that equation consumes all four working-memory slots before arithmetic even begins. The opening bracket marks the numerator of a compound fraction in the first mental slot, while a second nested parenthesis opens to multiply $a \cdot b$ in the second slot. Next, the central `+` sign must be deferred in the third slot because the second product $(c \cdot d)$ has not yet been evaluated, and the division bar `÷ (` must likewise wait in the fourth slot until the denominator $(e - f)$ is complete. Before a single challenging operation has taken place, working memory is saturated with *suspended syntax*: open parentheses and deferred operators waiting for their right-hand operands.

Worked instead from the inside out, the same fraction leaves zero deferred operators in flight: multiplying $a \cdot b$ forms the first product $P_1$ in Register $X$; entering $c$ and $d$ lifts $P_1$ into Register $Z$ while $c \cdot d = P_2$ forms across Registers $Y$ and $X$ and sums into the completed numerator $N = P_1 + P_2$ in Register $X$; and subtracting $D = e - f$ prepares the denominator for the final division $N \div D$. At no point does the stack hold more than three numbers, and at no point is an unclosed parenthesis left in flight.

### Edsger Dijkstra's Railway Siding and Postfix Logic

To bridge printed infix algebra and Jan Łukasiewicz's parenthesis-free postfix stack {{cite:lukasiewicz1924,burks1954,hamblin1957}}, Dijkstra formulated his 1960–1961 *Shunting-Yard Algorithm* {{cite:dijkstra1961}}. As an incoming sequence of tokens (`a`, `×`, `b`, `+`, `c`, `×`, `d`) arrives from left to right along a main track, each numeric operand passes to the output queue, while each operator (`×`, `+`, `÷`) or left parenthesis `(` is diverted onto a last-in, first-out operator siding to wait until its right-hand operands have passed. Only when an operation of equal or higher precedence completes, or when a closing right parenthesis `)` arrives to clear the siding, do the waiting operators roll back onto the main output track behind their operands:

$$\text{Infix Input: } (a \times b) + (c \times d) \quad \xrightarrow{\text{Shunting Yard}} \quad \text{Postfix Output: } a \;\; b \;\; \times \;\; c \;\; d \;\; \times \;\; +$$

Along the output track emerging from Dijkstra's shunting yard on the right, every parenthesis has been discarded, producing Łukasiewicz's chronological inside-out order. Whenever an equation is entered into Python, Java, C++, JavaScript, or an algebraic pocket calculator followed by `=`, an internal shunting-yard parser translates the left-to-right infix text into postfix stack instructions before any arithmetic takes place, a mechanism that powers the Java Virtual Machine (JVM), WebAssembly (Wasm), Adobe PostScript, and spacecraft Forth navigation computers {{cite:knuth1997}}.

Together, the four-chunk working-memory bound, Łukasiewicz's postfix logic, and Dijkstra's shunting-yard architecture {{cite:hewlett1972,cochran1972}} replace hidden parenthetical buffers with four visible registers ($X, Y, Z, T$) on the instrument face, so that every intermediate subtotal appears as soon as it is formed.

### Parallel Assembly Lines and the Harmonic Trap

Four visible registers ($X, Y, Z, T$) evaluate any rational expression in algebra or engineering through the paired mechanics of stack lift and stack drop (**Figure 2.1**).

{{blocks:sc32_concept_stack_elevator|Inside-out expression tree evaluation paired with the four-register operational stack (T, Z, Y, X).}}

Across the four vertical registers, every stack lift shifts subtotals upward toward Register $T$, and every dyadic (two-operand) operation drops waiting subtotals downward toward Register $X$:

| Stack Register | Movement on Lift (`ENTER` / Armed Digit) | Movement on Dyadic Drop (`+`, `-`, `×`, `÷`, `yˣ`, `x∥y`) |
| :---: | :--- | :--- |
| **Register T (Line 4)** | Receives $Z_{\text{old}}$ ($T_{\text{old}}$ shifts out in `4-LVL`) | Copies $T_{\text{old}}$ downward into $Z$ while remaining in $T$ |
| **Register Z (Line 3)** | Receives $Y_{\text{old}}$ as a second branch starts | Drops $Z_{\text{old}}$ down into $Y$, ready to combine with $X$ |
| **Register Y (Line 2)** | Receives $X_{\text{old}}$ (`ENTER` disables lift; armed digit lifts) | Consumed with $X_{\text{old}}$; receives $Z_{\text{old}}$ from Register $Z$ |
| **Register X (Line 1)** | Holds copy on `ENTER` (overwritten by next digit) | Receives new result $f(Y_{\text{old}}, X_{\text{old}})$ and arms stack lift |

To govern how newly keyed numbers enter Register $X$, the stack-lift state machine alternates between two states: *Neutral* (`Stack Lift = FALSE`) after `ENTER` or `CLx`, and *Armed* (`Stack Lift = TRUE`) after an operator or function. Whereas pressing `ENTER` after the first number of a pair copies that number into Register $Y$ and disables stack lift so the second number overwrites Register $X$ in place, every arithmetic operator or mathematical function produces a completed result in Register $X$ and arms stack lift, so the first digit of the next number lifts that result into Register $Y$ without a second `ENTER`. Because constants ($\pi$), recalled variables, and function outputs are already completed values, `ENTER` is needed only to separate two numbers typed consecutively on the numeric keypad (or to duplicate Register $X$ before squaring or constant-filling); pressing `ENTER` after a constant, a recalled variable, or a unary function duplicates that value into Register $Z$.

This inside-out discipline clarifies a recurring problem in algebra and operations engineering. In a semiconductor fabrication plant, an engineer schedules an urgent wafer lot across two independent photolithography cells feeding the same etching bay: Cell A, the primary high-speed stepper, completes the entire lot alone in $60\text{ minutes}$, and Cell B, an auxiliary stepper, completes the same lot alone in $180\text{ minutes}$. When both Cell A and Cell B run together, the two cells work in parallel to complete the lot.

A common algebraic mistake is to average the two elapsed times ($(60 + 180)/2 = 120\text{ minutes}$) or add them ($240\text{ minutes}$). A physical bounds check rules out both answers {{cite:strogatz2012,ellenberg2014}}: if Cell A alone finishes the lot in $60\text{ minutes}$, activating a second cell alongside it cannot make the job take longer than $60\text{ minutes}$. Two cells operating together must finish in less time than the faster single cell ($T_{\text{together}} < 60\text{ minutes}$), because parallel processes add their *throughput rates*, not their elapsed times.

The completion rate per minute resolves the relationship. Because Cell A completes $1\text{ lot}$ in $60\text{ minutes}$, in a single minute it completes a fraction of the lot equal to its reciprocal, $R_A = \frac{1}{60} \approx 0.017\text{ lots per minute}$. Because Cell B completes $1\text{ lot}$ in $180\text{ minutes}$, in a single minute it contributes $R_B = \frac{1}{180} \approx 5.556 \times 10^{-3}\text{ lots per minute}$. With both cells running in parallel, the per-minute throughput rates sum to $R_{\text{total}} = R_A + R_B = \frac{1}{60} + \frac{1}{180} = \frac{4}{180} \approx 0.022\text{ lots per minute}$, and the total time $T_{\text{together}}$ required to complete $1\text{ whole lot}$ is the reciprocal of that combined rate:

$$T_{\text{together}} = \frac{1}{\frac{1}{60} + \frac{1}{180}} = \frac{60 \times 180}{60 + 180} = \frac{10,800}{240} = \mathbf{45\text{ minutes}}$$

When the cleanroom brings two additional backup steppers online—Cell C, requiring $90\text{ minutes}$ alone, and Cell D, also requiring $90\text{ minutes}$ alone—those four cycle times ($60, 180, 90,$ and $90$) obey the same harmonic reciprocal-sum law as electrical resistors wired in parallel or capacitors wired in series:

$$T_{\text{all four}} = \left(\frac{1}{60} + \frac{1}{180} + \frac{1}{90} + \frac{1}{90}\right)^{-1} = \mathbf{22.5\text{ minutes}}$$

Because the parallel-harmonic operator (`x∥y`) is associative, all four completion times never need to occupy $T, Z, Y,$ and $X$ at once: combining the first two cells yields $60 \parallel 180 = 45\text{ min}$, folding in Cell C reduces the time to $45 \parallel 90 = 30\text{ min}$, and folding in Cell D reaches $30 \parallel 90 = \mathbf{22.5\text{ min}}$ across Registers $Y$ and $X$ alone (just as two parallel transfer pumps rated at $30\text{ min}$ and $45\text{ min}$ combine in a single fold to $30 \parallel 45 = \mathbf{18\text{ min}}$).

### Continued Fractions, Rational Approximations, and Nested Radicals

When reciprocals alternate with integer addition, they generate a classical structure in number theory known as a *continued fraction*. When designing a mechanical gear train to approximate an irrational orbital-period ratio $x$—as Christiaan Huygens did in 1680 for his brass planetarium—engineers peel off the leading integer part $a_0 = \lfloor x \rfloor$, invert the remaining fractional tail, and extract a cascade of integer partial denominators $a_1, a_2, a_3, \dots$:

$$x = a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \frac{1}{a_3}}}$$

When read from the top down, a continued fraction presents a deeply nested hierarchy in which each denominator $a_k + 1/(\dots)$ contains another rational expression beneath it. Evaluating that same structure from the innermost denominator $a_3$ upward eliminates every parenthesis: in the four-level continued fraction $1 + \frac{1}{2 + \frac{1}{3 + 1/4}}$, the bottom tier $3 + 1/4$ equals $13/4 = 3.25$, its reciprocal $4/13$ added to $2$ forms $30/13 \approx 2.308$, and inverting once more to $13/30 \approx 0.433$ before adding $1$ lands on $\approx \mathbf{1.433}$ ($43/30$).

Continued fractions generate the best possible rational approximations to any irrational number for a given denominator size. Applying Euclidean reciprocal extraction to the 16-digit hardware constant $\pi$ ($\approx 3.142$) exposes each convergent in succession. Subtracting the integer part $3$ isolates the fractional remainder $\approx 0.142$, whose reciprocal ($1 / (\pi - 3)$) is $\approx 7.063$. Because $7.063$ lies close to the integer $7$, truncating the expansion at the first tier yields the classical first-order rational approximation:

$$\pi \approx 3 + \frac{1}{7} = \frac{22}{7} \approx 3.143 \quad (\text{accurate to } 2\text{ decimal places})$$

Once $7$ is subtracted from $7.063$, the next remainder $\approx 0.063$ has reciprocal $\approx 15.997$, within $0.003$ of the integer $16$ (or $15 + \frac{1}{1}$). Truncating just before the large subsequent partial denominator ($292$) produces a four-tier continued fraction:

$$\pi \approx 3 + \frac{1}{7 + \frac{1}{15 + \frac{1}{1}}} = 3 + \frac{1}{7 + \frac{1}{16}} = 3 + \frac{16}{113} = \mathbf{\frac{355}{113}} \approx \mathbf{3.142}$$

The rational approximation $\frac{355}{113}$ is easily recalled by writing the first three odd integers twice (`113355`) and dividing the second triplet by the first (`355 / 113`). Discovered in the fifth century by Chinese mathematician Zu Chongzhi, $\frac{355}{113}$ uses only three-digit integers yet matches $\pi$ to six decimal places—an absolute error of $2.67 \times 10^{-7}$ (less than nine parts in one hundred million)—and renders in mixed fraction format as `3 16/113` ($\frac{355}{113}$).

Because large partial denominators like $292$ inside a continued fraction indicate that an irrational number can be closely approximated by rationals, the irrational number that is hardest to approximate with fractions is the one whose integer partial denominators $a_0, a_1, a_2, \dots$ are as small as possible. Setting every partial denominator equal to $1$ defines the *golden ratio* $\varphi$:

$$\varphi = 1 + \frac{1}{1 + \frac{1}{1 + \frac{1}{1 + \frac{1}{1 + \dots}}}}, \qquad \varphi = 1 + \frac{1}{\varphi} \implies \varphi^2 - \varphi - 1 = 0 \implies \varphi = \frac{1 + \sqrt{5}}{2} \approx \mathbf{1.618}$$

Beneath the top fraction bar, the infinite tower $1 + \frac{1}{1 + \frac{1}{1 + \dots}}$ is an exact, self-similar copy of the entire continued fraction $\varphi$ itself. Replacing that infinite denominator with $\varphi$ folds the unending staircase into the finite balance $\varphi = 1 + 1/\varphi$; multiplying through by $\varphi$ gives $\varphi^2 - \varphi - 1 = 0$, whose positive root is $\varphi = (1+\sqrt{5})/2 \approx \mathbf{1.618}$. In Diophantine approximation, $\varphi$ is the most badly approximable of all real numbers, with rational convergents $F_{n+1}/F_n$ ($1/1, 2/1, 3/2, 5/3, 8/5, 13/8, \dots$) approaching $\varphi$ more slowly than those of any other irrational constant ($|\varphi - p/q| > \frac{1}{\sqrt{5}q^2}$ asymptotically). In celestial mechanics and nonlinear dynamics, invariant phase-space tori whose winding-frequency ratio equals $\varphi$ are the last to break up under gravitational perturbations because small-denominator harmonic resonances are maximally suppressed, and in **golden-section unimodal search**, spacing interior test evaluations by $1/\varphi = \varphi - 1 \approx 0.618$ guarantees that each function evaluation reuses one interior point from the previous bracket while shrinking the search interval by a constant factor of $\approx 0.618$ at every step.

Where Euclid's algorithm nests reciprocals, François Viète's 1593 infinite product for $\pi$ nests square roots to compare the area of a circle to an infinite sequence of inscribed regular polygons. Inscribing a square ($4$ sides) inside a unit circle of radius $r = 1$ and repeatedly doubling the number of polygon sides to an octagon ($8$ sides), a $16$-gon, a $32$-gon, and a $64$-gon bisects the central wedge angle $\theta$ at each stage, scaling the polygon area at each step by the cosine of the half-angle $\cos(\theta/2)$:

$$\cos\left(\frac{\theta}{2}\right) = \sqrt{\frac{1 + \cos\theta}{2}} = \frac{\sqrt{2 + 2\cos\theta}}{2}, \qquad \frac{2}{\pi} = \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{2 + \sqrt{2}}}{2} \cdot \frac{\sqrt{2 + \sqrt{2 + \sqrt{2}}}}{2} \cdot \frac{\sqrt{2 + \sqrt{2 + \sqrt{2 + \sqrt{2}}}}}{2} \cdots$$

Writing the half-angle cosine as $2\cos(\theta/2) = \sqrt{2 + 2\cos\theta}$ turns repeated angle bisection into an iterative recurrence: each new doubled cosine is formed simply by adding $2$ to the previous value and extracting the square root. Starting from an initial right angle $\theta_1 = 90^\circ$ ($\pi/2\text{ radians}$, where $\cos 90^\circ = 0$), successive bisections build a tower of nested radicals: the first bisection at $45^\circ$ (an octagon) gives $2\cos(45^\circ) = \sqrt{2}$; the second bisection at $22.5^\circ$ (a $16$-gon) gives $2\cos(22.5^\circ) = \sqrt{2 + \sqrt{2}} \approx 1.848$; the third bisection at $11.25^\circ$ (a $32$-gon) gives $2\cos(11.25^\circ) = \sqrt{2 + \sqrt{2 + \sqrt{2}}} \approx 1.962$; and the fourth bisection at $5.625^\circ$ (a $64$-gon) reaches $2\cos(5.625^\circ) = \sqrt{2 + \sqrt{2 + \sqrt{2 + \sqrt{2}}}} \approx 1.99$, approximating $\pi \approx 3.121$ after three tiers and $\approx \mathbf{3.137}$ after four tiers. Like continued fractions, Viète's nested radical product requires deep parenthesis nesting when written from the outside in, yet simplifies naturally from the innermost radicand outward {{cite:cochran1972}}.

---

## The Grammar of Stack Lift and Constant Memory

An RPN operational stack is a deterministic finite-state automaton. Inheriting the classical four-register state-transition architecture established on the **HP-35**, **HP-15C**, and **HP-32SII** {{cite:cochran1972,hp15c1982,hp32sii1991}}, a single seven-element state vector $\mathcal{S}$ specifies the instrument's response to every keystroke on the faceplate:

$$\mathcal{S} = \bigl(X,\; Y,\; Z,\; T,\; L,\; \mathcal{L}_{\text{lift}},\; \mathcal{B}_{\text{entry}}\bigr)$$

Alongside the four visible operational registers $X, Y, Z, T$ (ordered from Line 1 up to Line 4) and the `LASTX` shadow register $L$ (which preserves the prior value of Register $X$ before each numeric operation), two boolean flags govern how incoming digits interact with the active line: **Stack Lift Enabled** ($\mathcal{L}_{\text{lift}} \in \{\text{TRUE}, \text{FALSE}\}$) determines whether a newly started number pushes $X$ up into $Y$, while **Digit Entry Active** ($\mathcal{B}_{\text{entry}} \in \{\text{TRUE}, \text{FALSE}\}$) tracks whether subsequent digit keys append to an open string in Register $X$ or start a fresh entry.

With respect to stack lift, every key on the faceplate belongs to one of four transition classes:

| Transition Class | Representative Keys | Effect on Registers $(T, Z, Y, X)$ | Post-Op Stack Lift |
| :--- | :--- | :--- | :--- |
| **1. Neutralizing Keys** | `ENTER`, `<-` / `C` (`CLx`), `Σ+`, `Σ-` | `ENTER` copies $X \to Y$ (lifting $Y \to Z \to T$); `<-` / `C` zeroes $X$ in place | **Neutral (`FALSE`):** Next number typed overwrites $X$ in place |
| **2. Arming Keys** | `1/x`, `√x`, `LN`, `SIN`, `x⇄y`, `R↓`, `RCL`, `LASTX`, `π` | Transforms $X$ in place (saving prior $X$ in `LASTX`) or recalls/permutes registers | **Armed (`TRUE`):** Next digit typed lifts $X \to Y \to Z \to T$ |
| **3. Digit Entry** | `0`–`9`, `.`, `E` | If **Armed**, lifts $X \to Y \to Z \to T$ before starting new entry; if **Neutral**, overwrites $X$ in place | **Armed (`TRUE`)** once the entry completes |
| **4. Dyadic Drop** | `+`, `-`, `×`, `÷`, `yˣ`, `x∥y` | Combines $Y$ and $X$ into $X$, drops $Z \to Y$, and replicates $T \to Z$ (in `4-LVL` mode) | **Armed (`TRUE`):** Result lifts on next entry |

### How Register T Acts as an Automatic Constant Supply

At the top of the four-register stack, Register $T$ (Line 4) implements a retention rule that governs what happens when two operands in Registers $Y$ and $X$ combine and the upper registers drop by one level. If Register $T$ cleared to zero every time the stack dropped, three consecutive dyadic operations would leave the upper registers empty. Instead, in `4-LVL` mode, Register $T$ exhibits *$T$-Register Duplication*:

$$\begin{aligned}
X_{\text{new}} &\leftarrow Y_{\text{old}} \text{ [op] } X_{\text{old}} \\
Y_{\text{new}} &\leftarrow Z_{\text{old}} \\
Z_{\text{new}} &\leftarrow T_{\text{old}} \\
T_{\text{new}} &\leftarrow T_{\text{old}} \quad \text{(Retained in } T \text{ and replicated into } Z\text{)}
\end{aligned}$$

Whenever a dyadic operation drops the stack, Register $T$ copies its value downward into Register $Z$ while retaining its own value in $T$. That single hardware rule turns the top register into a constant supply: in compound growth, filling the upper stack with a growth factor $(1 + r) = 1.065$ and starting from an initial principal $P_0 = \$2,500$ advances the balance period by period ($P_1 = \$2,662.5 \to P_2 \approx \$2,835.563 \to P_3 \approx \$3,019.874 \to P_4 \approx \$3,216.166 \to P_5 \approx \mathbf{\$3,425.217}$), while a machinist scaling a table of inch dimensions by $k = 25.4\text{ mm/in}$ ($0.375\text{ in} \to 9.525\text{ mm}$ through $5.5\text{ in} \to \mathbf{139.7\text{ mm}}$) draws $25.4$ repeatedly from Register $T$.

To reorder operands already on the stack without re-entry, the two-register swap exchanges Registers $Y$ and $X$ ($X \leftrightarrow Y$), while the four-register cyclic permutations (Roll Down and Roll Up) rotate all four registers in a closed ring ($X \leftarrow Y \leftarrow Z \leftarrow T \leftarrow X$, so four thermocouple readings $21.5^\circ\text{C}, 24.8^\circ\text{C}, 28.2^\circ\text{C}, 31^\circ\text{C}$ can be inspected in turn and returned to their original positions):

$$\text{Roll Down: } (X, Y, Z, T) \leftarrow (Y, Z, T, X), \qquad \text{Roll Up: } (X, Y, Z, T) \leftarrow (T, X, Y, Z)$$

Two-register exchange and in-place inversion also handle non-commutative division ($Y \div X$) and subtraction ($Y - X$) whenever a formula's denominator or subtracted term is more complicated than its numerator or leading term, as in resonant frequency $f_0 = \frac{1}{2\pi\sqrt{LC}}$, impedance current $I = \frac{V_s}{\sqrt{R^2 + X^2}}$, or Carnot thermal efficiency $\eta = 1 - \frac{T_C}{T_H}$. Evaluating the multi-step denominator $D$ or subtrahend $S$ first inside Register $X$ keeps the upper stack untouched and leaves two equivalent paths to complete the calculation without re-entry: either invert or negate Register $X$ in place ($D^{-1}$ or $-S$) and multiply or add the numerator $N$ or minuend $M$ ($D^{-1} \times N$ or $-S + M$), or enter $N$ or $M$ second (which lifts $D$ or $S$ into Register $Y$) and exchange Registers $X \leftrightarrow Y$ so the operands sit in standard $(Y = N,\; X = D)$ or $(Y = M,\; X = S)$ order before dividing or subtracting.

Alongside the four visible registers, every operation that modifies Register $X$ saves its prior occupant in the last-argument shadow register (`LASTX`). In an unnormalized sinc ratio $\operatorname{sinc} x = \frac{\sin x}{x}$, evaluating $\sin(0.42) \approx 0.408$ in radians preserves the pre-sine angle $0.42$ in `LASTX`, so recalling `LASTX` and dividing yields $\frac{\sin(0.42)}{0.42} \approx \mathbf{0.971}$. In Fraunhofer single-slit diffraction, where monochromatic light of wavelength $\lambda$ passes through an aperture of slit width $a$ and spreads out at diffraction angle $\theta$, the optical path difference across the slit defines the half-aperture phase parameter $\beta = \frac{\pi a}{\lambda}\sin\theta$; for $\beta = 0.085\text{ rad}$, the same two-step sequence gives the normalized far-field diffraction amplitude $\frac{\sin\beta}{\beta} = \frac{\sin(0.085)}{0.085} \approx \mathbf{0.999}$ without re-entering $\beta$.

On the display, twelve-digit base-10 guard rounding suppresses binary representation residuals (rendering $0.1 + 0.2$ as `0.3` while retaining the 53-bit binary64 significand in memory); rounding to display precision (`RND`) replaces Register $X$'s internal 53-bit significand with its currently displayed value, quantizing a currency or tolerance figure to two decimal places under `FIX 2` so unshown fractional digits do not accumulate across downstream sums. Depending on how many independent subtotals an expression requires, four selectable stack-depth architectures generalize the operational stack:

| Mode ID | Architecture Name | Accessible Registers | Stack Drop Behavior | Recommended Application Zone |
| :---: | :--- | :--- | :--- | :--- |
| **2-LVL** | **2-Level B-Register Stack** | $X, T$ ($Y$-position) | 2-register accumulator; $T$ retains its value in $Y$ on drop while $X$ holds the result | Simple adding-machine tallies and two-operand arithmetic |
| **4-LVL** | **Classic 4-Level Stack (Default)** | $X, Y, Z, T$ | Top-of-stack $T$-duplication on drop; classic 4-register behavior | Everyday engineering, Horner recurrences, constant scaling |
| **8-LVL** | **Extended 8-Level Stack** | $R_1 \dots R_8$ (displayed as $X, Y, Z, 4, 5, 6, 7, T$) | Holds up to 8 real operands (or 4 complex pairs) before $T$ ($R_8$) replication | Multi-branch complex phasor algebra, 5-to-8-register expressions |
| **INF** | **Unbounded Infinite Stack** | Dynamic heap allocation (up to 999 levels) | True LIFO stack; dyadic drop never duplicates; pulls from history | 5+ branch parallel networks, long product-sum series |

### Named Variables and Indirect Memory Addressing

When all four stack registers ($T, Z, Y, X$) hold live subtotals and a calculation requires a constant stored in one of the 26 lettered variables `A`–`Z`, a standard recall lifts the stack by one level and pushes the occupant of Register $T$ over the cliff in `4-LVL` mode. Three non-destructive mechanisms resolve this full-stack bottleneck while preserving Registers $Y, Z,$ and $T$: first, *non-destructive variable inspection* displays the value of any stored variable on the status line (or in a read-only register catalog) without lifting the stack; second, *two-way in-place storage arithmetic* updates Register $X$ in place as $X \leftarrow X \text{ op } A$ (*Recall Arithmetic*—for example, scaling $X = 40$ by $A = 2.5$ to $\mathbf{100}$ while $10, 20, 30$ remain untouched in the upper stack) or updates Variable `A` in place as $A \leftarrow A \text{ op } X$ (*Store Arithmetic*); and third, *in-place variable exchange* swaps Register $X$ with any named variable ($X \leftrightarrow A$) to park an intermediate subtotal and bring a stored parameter onto the active line.

To step across memory without hard-wiring a fixed variable name (`A`, `B`, `C`), an *index register (`i`)* holds an integer slot number $k$ so that *indirect addressing (`(i)`)* can dynamically reference whichever memory slot resides at address $k$ across a unified 89-slot memory map:

| Pointer Range $k \in \{1, \dots, 89\}$ | Target Memory Bank | Addressed Register / Content | Access Permissions |
| :---: | :--- | :--- | :--- |
| **`1` … `26`** | **Lettered Variables (`A–Z`)** | `1` = `A`, `2` = `B`, `3` = `C`, …, `26` = `Z` | Full Read / Write (`STO (i)`, `RCL (i)`, `x⇄? (i)`) |
| **`27`** | **Index Register (`i`)** | `27` = Index register `i` itself | Full Read / Write |
| **`28` … `33`** | **Statistical Accumulators** | `28` = $\Sigma n$, `29` = $\Sigma x$, `30` = $\Sigma y$, `31` = $\Sigma x^2$, `32` = $\Sigma y^2$, `33` = $\Sigma xy$ | Read / Write via `(i)` |
| **`34` … `39`** | **`POLY` Solver Roots** | Slots `34`–`39` (Real & imaginary parts of roots $r_1, r_2, r_3$) | Read via `RCL (i)` |
| **`40` … `89`** | **Statistical Data Points** | `DATA0` (`40`) through `DATA49` (`89`) | Read via `RCL (i)` |
| **$k < 1$ or $k > 89$** | **Out of Bounds** | Displays `INVALID DATA` | N/A (Halts without stack corruption) |

Where a single-line parenthesized expression hides intermediate quantities until the final result appears, evaluating an equation across the four visible registers exposes every physical subtotal—thermal voltage, cross-sectional area, characteristic impedance, or dynamic pressure—live on the glass as it forms, making a tenfold unit or sign error visible before it propagates downstream.

---

## Five Patterns for Evaluating Any Formula

Five stack-control keys and two memory-addressing mechanisms on the physical SC-32 keypad govern how numbers move across Registers $T, Z, Y,$ and $X$:
* **Stack Entry, Non-Commutative Alignment & Rearrangement (`{{key:ENTER}}`, `{{key:x⇄y}}`, `{{key:1/x}}`, `{{key:+/-}}`, `{{key:R↓}}`, `{{key:R↑}}`, `{{key:<-}}`):** Pressing `{{key:ENTER}}` separates two consecutively typed numbers by copying Register $X$ into Register $Y$ and disabling stack lift (constants like `{{key:π}}`, recalled variables, and function outputs are already self-delimited and arm stack lift). When a multi-step denominator $D$ or subtrahend $S$ is evaluated first in Register $X$, pressing `{{key:1/x}}` or `{{key:+/-}}` before multiplying or adding the numerator or minuend—or entering the numerator/minuend second and pressing `{{key:x⇄y}}` ($X \leftrightarrow Y$) before `{{key:÷}}` or `{{key:-}}`—completes the ratio or difference without re-entry; `{{key:R↓}}` and `{{key:R↑}}` (right-shifted on `{{key:R↓}}`) rotate all four registers cyclically; and `{{key:<-}}` clears a mistyped entry in Register $X$ without disturbing $Y, Z,$ or $T$.
* **Harmonic Operator (`{{key:x∥y}}`), Shadow Register (`{{key:LASTX}}`), & Display Rounding (`{{key:RND}}`):** Pressing `{{key:x∥y}}` evaluates the parallel product-over-sum $\frac{Y \cdot X}{Y + X}$, `{{key:LASTX}}` (left-shifted on `{{key:ENTER}}`) recalls the pre-operation value of Register $X$ saved before the most recent numeric operation, and `{{key:RND}}` (left-shifted on `{{key:RCL}}`) rounds Register $X$'s internal 53-bit value to match the active `{{key:DISP}}` setting (`FIX`, `SCI`, or `ENG`).
* **Stack Depth (`{{key:FLAGS}}`), Non-Destructive Inspection (`{{key:VIEW}}`, `{{key:REGS}}`, `MEM`), & Storage Addressing (`i` and `(i)`):** Pressing `{{key:FLAGS}}` (right-shifted on `{{key:×}}`) and tapping `STACK` selects $\mathtt{[2\text{-}LVL]} \;\; \mathtt{[4\text{-}LVL]} \;\; \mathtt{[8\text{-}LVL]} \;\; \mathtt{[INF]} \;\; \mathtt{[VIEW]}$ (`4-LVL` default). To inspect memory without lifting the stack, `{{key:VIEW}}` (right-shifted on `{{key:0}}`) prompts for `A`–`Z` and displays `"A = ..."` on the status line without altering $T, Z, Y,$ or $X$, while `{{key:REGS}}` (left-shifted on `{{key:0}}`) and `MEM` (left-shifted on `{{key:x⇄y}}`) browse the stack, variables, statistical registers, and equations read-only. Pressing `{{key:STO}}` or `{{key:RCL}}` activates the `A`–`Z` Alpha layer (`.` addresses `i`; `{{key:x∥y}}` addresses `(i)`). Inserting an operator (`{{key:STO}} {{key:+}} A` or `{{key:RCL}} {{key:×}} A`, plus `{{key:-}}` and `{{key:÷}}`) performs in-place storage or recall arithmetic without stack lift, right-shifted `x⇄?` on `{{key:x⇄y}}` swaps Register $X$ with a variable in place, and `{{key:EQN}}` and `{{key:XEQ}}` store and execute symbolic postfix equations with automatic variable prompts.

Every multi-stage formula in algebra and engineering reduces to one of five patterns on these keys: evaluating a two-branch rational quotient across three registers, generating continued fractions and nested radicals from the bottom up, reusing a shared divisor across multiple branches with `LASTX`, evaluating polynomials without exponents via Horner's method, and stepping through memory slots with `(i)`.

### Evaluating Two-Branch Rational Quotients Across Three Registers

Whenever a formula adds or subtracts two products in the numerator and divides by a two-term denominator, only three registers ($X, Y, Z$) are required. In the calorimetric stream balance $\frac{(60 \times 2.5) + (35 \times 4)}{18 - 5.5}$, the first numerator product ($150$) lifts into Register $Z$ while the second product ($35 \times 4 = 140$) forms across Registers $Y$ and $X$; addition collapses both branches into the completed numerator ($290$) in Register $X$; keying `18 ENTER 5.5` shifts $290$ into Register $Z$ before subtraction forms the denominator ($12.5$) in Register $X$ and drops $290$ into Register $Y$; and division completes the quotient:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `60 {{key:ENTER}} 2.5 {{key:×}}` | $0$ | $0$ | $0$ | $150$ | First numerator product $60 \times 2.5 = 150$; stack lift armed |
| `35 {{key:ENTER}} 4` | $0$ | $150$ | $35$ | $4$ | Second branch lifts $150$ into $Z$ while $35$ and $4$ occupy $Y$ and $X$ |
| `{{key:×}} {{key:+}}` | $0$ | $0$ | $0$ | $290$ | Product $140$ drops $150$ to $Y$ and sums to completed numerator $290$ |
| `18 {{key:ENTER}} 5.5 {{key:-}}` | $0$ | $0$ | $290$ | $12.5$ | Denominator $18 - 5.5 = 12.5$ in $X$; numerator $290$ drops from $Z$ to $Y$ |
| `{{key:÷}}` | $0$ | $0$ | $0$ | **$23.2$** | Final quotient $290 \div 12.5 = 23.2$ |

This same three-register sequence governs two-branch balances across heat transfer, bridge instrumentation, and spacecraft radiative transport. In a two-pass heat exchanger, summing two heat-flux streams ($18.5 \times 4.2$ and $7.1 \times 9.6$) and dividing by the wall temperature difference ($14.3 - 5.8$) yields the overall heat-transfer conductance $U$. In a four-resistor Wheatstone bridge powered by excitation voltage $V_{\text{exc}}$, two parallel voltage-divider legs ($R_1, R_3$ on the left and $R_2, R_4$ on the right) split the supply rail, and a voltmeter wired between their midpoints measures the differential output voltage $V_{\text{diff}}$. And in vacuum radiative heat transfer between two parallel plates at absolute temperatures $T_1$ and $T_2$ with infrared surface emissivities $\varepsilon_1$ and $\varepsilon_2$ (scaled by the Stefan–Boltzmann constant $\sigma \approx 5.67 \times 10^{-8}\text{ W/(m}^2\cdot\text{K}^4)$), the net radiative heat flux $q$ (watts per square meter) balances blackbody emission against multiple surface reflections:

$$U = \frac{(18.5 \times 4.2) + (7.1 \times 9.6)}{14.3 - 5.8}, \qquad V_{\text{diff}} = V_{\text{exc}}\left(\frac{R_3}{R_1 + R_3} - \frac{R_4}{R_2 + R_4}\right), \qquad q = \frac{\sigma(T_1^4 - T_2^4)}{\frac{1}{\varepsilon_1} + \frac{1}{\varepsilon_2} - 1}$$

Although these three equations come from different laboratories, each pits a combined driving potential against a net opposing resistance or reference branch. Overall conductance $U$ divides the combined thermal power of both fluid passes by the wall temperature span. Across the Wheatstone bridge, the two midpoint divider ratios $\frac{R_3}{R_1+R_3}$ and $\frac{R_4}{R_2+R_4}$ cancel to zero whenever all four arms match, isolating any slight resistance shift in an active strain gauge $R_3$ as a clean differential signal scaled by $V_{\text{exc}}$. Between the vacuum radiation plates, the ideal fourth-power blackbody flux $\sigma(T_1^4 - T_2^4)$ is throttled by the combined gray-body surface reflection resistance $\frac{1}{\varepsilon_1} + \frac{1}{\varepsilon_2} - 1$, which equals $1$ for perfect blackbodies ($\varepsilon_1 = \varepsilon_2 = 1$) and grows larger as polished, low-emissivity foil reflects infrared photons back and forth.

In the heat-exchanger balance $U$, the first thermal product ($77.7$) waits in Register $Z$ while the second ($68.16$) forms in Registers $Y$ and $X$, and their summed numerator ($145.86$) waits in Register $Z$ while the temperature difference ($8.5$) forms, dividing to $\approx \mathbf{17.16\text{ W/(m}^2\cdot\text{K)}}$. In a Wheatstone bridge ($R_3 = 351.4\,\Omega$ active metallic strain gauge against three $350\,\Omega$ reference arms under $V_{\text{exc}} = 10\text{ V}$), subtracting the balanced reference ratio $0.5$ from the active divider ratio $351.4/(350 + 351.4) \approx 0.501$ and scaling by $10\text{ V}$ isolates a $\approx \mathbf{9.98\text{ mV}}$ strain signal. Across a two-panel spacecraft radiation shield ($T_1 = 800\text{ K}, \varepsilon_1 = 0.85$ and $T_2 = 500\text{ K}, \varepsilon_2 = 0.7$), the blackbody numerator $\sigma(T_1^4 - T_2^4) \approx 19,681.854\text{ W/m}^2$ waits in Register $Z$ while the emissivity denominator $1/\varepsilon_1 + 1/\varepsilon_2 - 1 \approx 1.605$ combines in Registers $Y$ and $X$, dividing to a net radiative flux of $q \approx \mathbf{12,262.517\text{ W/m}^2}$.

### Climbing Continued Fractions and Nested Radicals from the Bottom Up

In vertically nested expressions like the golden ratio continued fraction $\varphi = 1 + \frac{1}{1 + \frac{1}{1 + \dots}}$, bottom-up evaluation reduces each tier in place. Flooding all four stack registers with $1$ uses Register $T$'s constant replication to supply an endless stream of $1$'s into Register $Y$, so repeatedly taking the reciprocal in place and adding generates the sequence of Fibonacci rational convergents step by step ($2/1 = 2 \to 3/2 = 1.5 \to 5/3 \approx 1.667 \to 8/5 = 1.6 \to 13/8 = 1.625 \to \dots \to \varphi \approx \mathbf{1.618}$).

When evaluation begins at the deepest radical or dimensionless ratio, spacecraft orbital transfer and AC filter calculations unfold without parentheses. Consider a spacecraft orbiting in Earth's gravity well, governed by Earth's standard gravitational parameter $\mu = GM_\oplus$: to lift the craft from a circular parking orbit of inner radius $r_1$ up to an outer target radius $r_2$ along a minimum-energy Hohmann transfer ellipse of semi-major axis $a = (r_1 + r_2)/2$, the engine must fire at perigee with velocity impulse $\Delta v_1$, raising the spacecraft's orbital speed $v$ at radial distance $r$ according to the vis-viva energy integral. Similarly, when an alternating audio signal of frequency $f$ passes through a series high-pass filter built from resistance $R$ and capacitance $C$, the dimensionless frequency ratio $X = 2\pi f R C$ (comparing the signal frequency $f$ to the RC corner frequency) sets the voltage transfer magnitude $|H|$:

$$\Delta v_1 = \sqrt{\frac{\mu}{r_1}}\left(\sqrt{\frac{2r_2}{r_1+r_2}} - 1\right), \qquad v = \sqrt{\mu\left(\frac{2}{r} - \frac{1}{a}\right)}, \qquad |H| = \frac{X}{\sqrt{1 + X^2}} \quad (X = 2\pi f R C)$$

Firing a Hohmann perigee burn scales the initial circular parking speed $\sqrt{\mu/r_1}$ by the dimensionless boost factor $\sqrt{\frac{2r_2}{r_1+r_2}} - 1$ required to raise apogee from $r_1$ to $r_2$. Along the resulting transfer ellipse, the vis-viva balance trades local gravitational potential ($2/r$) against the orbit's fixed binding energy ($1/a$), slowing the spacecraft as radial distance $r$ climbs toward apogee. In the high-pass audio filter, the capacitor blocks direct current as $X \to 0$ ($|H| \to 0$) and becomes a transparent short circuit at high frequencies ($X \gg 1$, where $\sqrt{1+X^2} \approx X$ and $|H| \to 1$).

For a Hohmann transfer between a low Earth parking orbit ($r_1 = 6,678\text{ km}$) and geostationary altitude ($r_2 = 42,164\text{ km}$, with $\mu = 398,600\text{ km}^3/\text{s}^2$), computing the inner radius ratio $\frac{2r_2}{r_1+r_2} \approx 1.727$ first, taking its square root ($\approx 1.314$), and subtracting $1$ isolates the dimensionless impulse factor $\approx 0.314$ before scaling by the circular parking speed $\sqrt{\mu/r_1} \approx 7.726\text{ km/s}$ to obtain the perigee burn $\Delta v_1 \approx \mathbf{2.426\text{ km/s}}$; along that transfer ellipse of semi-major axis $a = 24,421\text{ km}$, the vis-viva integral gives the total perigee speed $v_p \approx \mathbf{10.152\text{ km/s}}$. In a first-order high-pass RC audio filter ($R = 10,000\,\Omega$, $C = 15 \times 10^{-9}\text{ F}$ at $f = 2,500\text{ Hz}$), forming the normalized frequency ratio $X = 2\pi f R C \approx 2.356$ once, duplicating it into Register $Y$, and transforming Register $X$ into $\sqrt{1 + X^2} \approx 2.56$ before dividing yields the voltage gain $|H| \approx \mathbf{0.921}$ across Registers $Y$ and $X$.

### Reusing a Shared Divisor or Argument with LASTX

When three resistors $R_{12}, R_{23}, R_{31}$ are wired in a closed triangular delta ($\Delta$) between terminal nodes $1, 2,$ and $3$ inside a bridge or a three-phase industrial motor starter, circuit analysis often requires replacing the triangle with an equivalent three-branch star ($\text{Y}$) of wye resistances $R_a, R_b, R_c$ radiating from a central neutral point. The $\Delta \to \text{Y}$ impedance transformation equates the terminal-to-terminal resistances of both networks by dividing each adjacent pair product by the shared delta perimeter sum $S = R_{12} + R_{23} + R_{31}$:

$$R_a = \frac{R_{12} R_{31}}{R_{12} + R_{23} + R_{31}}, \qquad R_b = \frac{R_{12} R_{23}}{R_{12} + R_{23} + R_{31}}, \qquad R_c = \frac{R_{23} R_{31}}{R_{12} + R_{23} + R_{31}}$$

Each equivalent star resistor $R_a, R_b, R_c$ pairs the two delta arms that meet at its terminal corner ($R_{12}R_{31}$ at node $1$, $R_{12}R_{23}$ at node $2$, and $R_{23}R_{31}$ at node $3$) and divides their product by the common loop resistance $S = R_{12} + R_{23} + R_{31}$ around the entire triangle. For $R_{12} = 30\,\Omega,\; R_{23} = 45\,\Omega,\; R_{31} = 60\,\Omega$, that shared loop sum is $S = 30 + 45 + 60 = 135\,\Omega$. Dividing the first pair product $R_{12}R_{31} = 1,800\,\Omega^2$ by $135\,\Omega$ yields the first star branch $R_a = 1,800 / 135 \approx \mathbf{13.333\,\Omega}$ and latches the divisor $135\,\Omega$ in `LASTX`. Recalling $135\,\Omega$ from `LASTX` before forming each remaining pair product ($R_{12}R_{23} = 1,350\,\Omega^2$ and $R_{23}R_{31} = 2,700\,\Omega^2$) and swapping Registers $Y$ and $X$ to divide places all three wye resistances ($\approx 13.333\,\Omega$, $10\,\Omega$, and $20\,\Omega$) on the stack without re-entering $S$.

The `LASTX` shadow register also eliminates duplicate entry in any single-variable difference like $f(x) = e^x - \ln(x)$ at $x = 2.5$: evaluating $e^{2.5} \approx 12.182$ saves $2.5$ in `LASTX`, so recalling `LASTX` to take $\ln(2.5) \approx 0.916$ and subtracting yields $\approx \mathbf{11.266}$. And if a mistyped cross-sectional area of $19\text{ mm}^2$ is keyed after computing a tensile load of $36 \times 12.5 = 450\text{ N}$, clearing Register $X$ zeroes the active line and disables stack lift so the corrected area $18\text{ mm}^2$ overwrites the zero in place ($450 \div 18 = \mathbf{25\text{ MPa}}$).

### Nested Polynomials and Horner's Evaluation Scheme

When a cubic polynomial $P(x) = 2x^3 - 5x^2 + 3x + 7$ is factored into nested linear binomials $((2x - 5)x + 3)x + 7$—Horner's evaluation scheme—every power operation disappears. Flooding all four registers with the evaluation point $x = 3.5$ lets Register $T$'s constant replication supply $x = 3.5$ at each multiplication stage, evaluating the cubic to $\mathbf{42}$ in three linear steps:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3.5 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}` | $3.5$ | $3.5$ | $3.5$ | $3.5$ | Flood all 4 registers with evaluation point $x = 3.5$ |
| `2 {{key:×}} 5 {{key:-}}` | $3.5$ | $3.5$ | $3.5$ | $2$ | Innermost Horner binomial $2x - 5 = 2(3.5) - 5 = 2$ |
| `{{key:×}} 3 {{key:+}}` | $3.5$ | $3.5$ | $3.5$ | $10$ | Second Horner stage $(2x - 5)x + 3 = 2(3.5) + 3 = 10$ |
| `{{key:×}} 7 {{key:+}}` | $3.5$ | $3.5$ | $3.5$ | **$42$** | Outer Horner stage $((2x - 5)x + 3)x + 7 = 10(3.5) + 7 = 42$ |

Pushing a fifth number ($50$) onto $10, 20, 30, 40$ and summing illustrates why `4-LVL` mode suits Horner recurrences while `8-LVL` and `INF` modes serve deep multi-branch sums: in `4-LVL` mode, pushing $50$ shifts $10$ off the top of Register $T$, and as $40 + 50 = 90$ drops the stack, Register $T$ replicates $20$ downward so three additions yield $20 + 30 + 90 = \mathbf{140}$; in `8-LVL` or `INF` mode, $10$ is preserved at level 5 and drops back into Register $T$ as the lower pairs collapse, so summing all five terms yields $\mathbf{150}$.

When a calibration routine or data-logging loop must step through sequential variables without hard-wiring `A`, `B`, `C` into each command, the index register `i` and indirect pointer `(i)` turn the 89-slot memory map into an addressable array: storing calibration offset $120$ in Variable `A` (slot $k = 1$) and $250$ in Variable `B` (slot $k = 2$), loading $k = 1$ into `i` lets an indirect recall fetch slot $1$ ($120$), while adding $1$ to pointer `i` via storage arithmetic (`1 STO+ i`) advances `i` to slot $2$ so an indirect store-addition of $35$ (`35 STO+ (i)`) updates Variable `B` to $250 + 35 = \mathbf{285}$.

### Try It on the Stack

1. **Three-Resistor Parallel Shunt Network:** Fold three current-sense shunt resistors of $R_1 = 30\,\Omega$, $R_2 = 45\,\Omega$, and $R_3 = 90\,\Omega$ in parallel using the harmonic parallel operator. *(Verified Register $X$ result: $R_{\text{eq}} = \mathbf{15\,\Omega}$.)*
2. **Delta-to-Wye ($\Delta \to \text{Y}$) Network Conversion:** For a three-terminal bridge with delta resistors $R_{ab} = 20\,\Omega$, $R_{bc} = 30\,\Omega$, and $R_{ca} = 50\,\Omega$ (perimeter sum $S = 100\,\Omega$), evaluate the three equivalent wye branch resistances $R_a = R_{ab}R_{ca}/S$, $R_b = R_{ab}R_{bc}/S$, and $R_c = R_{bc}R_{ca}/S$ using `LASTX` to restore the shared divisor $S = 100\,\Omega$ for each remaining pair product. *(Verified Register $X$ results: $R_a = \mathbf{10\,\Omega}$, $R_b = \mathbf{6\,\Omega}$, and $R_c = \mathbf{15\,\Omega}$.)*
3. **Golden Ratio Continued Fraction via $T$-Replication:** Fill all four stack registers $(T, Z, Y, X)$ with $1$ and alternate reciprocal and addition nine times to evaluate the tenth Fibonacci convergent $F_{11}/F_{10} = 89/55$ of $\varphi = 1 + \frac{1}{1 + \frac{1}{1 + \dots}}$. *(Verified Register $X$ result: $\varphi_{10} \approx \mathbf{1.618}$.)*
