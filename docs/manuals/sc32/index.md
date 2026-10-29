---
title: "Thinking in the Stack: Why We Write Mathematics for Paper, Yet Solve It in Time (SC-32)"
description: "Jan Łukasiewicz's 1924 parenthesis-free logic, sixteenth-century printing history, the Corvallis four-register lineage, and inside-out equation evaluation on the StackCalc SC-32."
---

# Prologue: Writing Equations for Space, Solving Them in Time

## The Typesetter's Bargain and the Inside-Out Mind

In the autumn of 1924, in a quiet lecture hall at the University of Warsaw, the Polish logician and philosopher Jan Łukasiewicz stood before a blackboard covered in logic formulas and examined a foundational anomaly of mathematical notation {{cite:lukasiewicz1924}}: the ubiquity of parentheses.

Every high-school student who has ever stared at a page of Algebra II or Precalculus knows the feeling of parenthesis vertigo. You look at an equation on a printed page:

$$x = \sqrt{7 + \sqrt{13 + \sqrt{29 + \sqrt{41}}}}$$

or a compound rational fraction from physics or chemistry:

$$Q = \frac{12.4 \times 8.6}{3.2 + 4.9}$$

On paper, your eyes naturally read from left to right and from the outside in. In this radical pyramid, the first symbol you encounter on the left is the outer square-root radical $\sqrt{\dots}$, followed by $7 +$, followed by a second radical, a third radical, and finally, at the far right end of the line, the number $41$.

The moment you sit down to *solve* that equation, the outer square root cannot be evaluated first because you cannot take the square root of a sum that has not been added yet. To find $x$, evaluation must ignore the left-to-right order of the ink and travel straight to the innermost number, $41$, extracting its square root first, adding $29$, taking the next square root, adding $13$, extracting that root, and finally adding $7$ before one last square root completes the chain from right to left.

Writing mathematics from the outside in while every human mind and every computer processor on Earth can only evaluate it from the inside out is a historical artifact of the printing press.

### Space Versus Time: Sixteenth-Century Typography and Infix Notation

For thousands of years, from Babylonian clay scribes and Greek geometers to medieval Arab algebraists, mathematics was written out in spoken sentences: *"Take forty-one, extract its root, add twenty-nine to what results..."* Spoken language unfolds in *time*. Physical measurement and construction follow the same chronological order, gathering materials first and applying the tool second: a carpenter aligns two boards on a bench before joining them, a chemist weighs two reagents on a balance before combining them in a beaker, and an action in speech or calculation cannot occur until its objects exist.

In the sixteenth and early seventeenth centuries, however, Renaissance mathematicians—including Robert Recorde (who introduced the equals sign `=` in 1557 in *The Whetstone of Witte*), François Viète, and Thomas Harriot—working with European printers and typesetters faced an economic problem. Movable lead type was expensive, and rag paper was costly. Printers wanted to pack an entire finished mathematical thought onto a single static horizontal line of type. To fit a multi-step timeline onto a flat two-dimensional line, they wedged action symbols (`+`, `-`, `×`, `÷`) *between* numbers in a convention called *infix notation*, and invented parentheses `( )`, brackets `[ ]`, and horizontal fraction bars as punctuation fences to warn the eye: *"Do not read this line from left to right; jump inside the deepest fence first."*

That 16th-century typesetter's bargain was well suited to static paper, where the eye can scan back and forth across a page. It became a cognitive obstacle the moment 20th-century engineers copied paper notation onto electronic calculator keyboards.

When you type an infix string like `( ( 12.4 × 8.6 ) ÷ ( 3.2 + 4.9 ) ) =` into an algebraic pocket or smartphone calculator, you are forced to feed the machine in the exact order of the printed ink rather than the order of evaluation. Halfway through the formula, when you press `÷ (`, the calculation stalls because the denominator `(3.2 + 4.9)` does not yet exist. As cognitive psychologist George A. Miller demonstrated in his 1956 study of human working memory {{cite:miller1956,sweller1988}}, the mind holds only four to seven active items at once. Hiding intermediate numbers behind a single-line display while counting nested parentheses `( ( ... ) / ( ... ) )` diverts working memory from the physical structure of the problem to clerical punctuation {{cite:strogatz2012,strogatz2019,ellenberg2014}}.

### Jan Łukasiewicz's Breakthrough and the Four Visible Registers

In 1924, Jan Łukasiewicz proved a foundational theorem {{cite:lukasiewicz1924}}: if operators are placed consistently before or after their operands, parentheses disappear from mathematical notation. No matter how deeply an equation is nested, the order in which numbers combine is unambiguous without a single bracket or precedence rule.

Three decades later, Australian philosopher and computer pioneer Charles Hamblin (1957) {{cite:hamblin1957}} paired the postfix (*Reverse Polish*) form of Łukasiewicz's parenthesis-free notation, in which operands precede their operator, with a last-in, first-out hardware memory structure: an operational *stack*.

On a four-register operational stack, four horizontal display lines are arranged from bottom to top as Registers $X, Y, Z,$ and $T$. Register $X$ at the bottom of the screen serves as the active register where keyed digits appear and where every unary or binary operation writes its immediate result. When a first operand is completed in Register $X$ and the central `ENTER` bar is pressed, that value copies upward into Register $Y$, preparing Register $X$ to receive the second operand. Whenever a calculation spans two or three separate branches, such as the numerator and denominator of a rational expression, the completed subtotal from the first branch lifts into Register $Z$ (and Register $T$) to remain visible while the second branch is evaluated across Registers $Y$ and $X$. As soon as that second branch reduces to a single value in Register $X$, the waiting subtotal in Register $Z$ drops back into Register $Y$ so the two operands align for the final binary operation.

When equations are read from their innermost operands outward, expressions from disparate branches of science reveal shared algebraic skeletons {{cite:hp15c1982}}. Wiring electrical resistors in parallel, focusing light through a thin optical lens, and averaging a round-trip velocity all reduce to the same binary harmonic operation $x \parallel y = (x^{-1} + y^{-1})^{-1}$ {{cite:horowitz2015}}, and multi-layer formulas resolve into a direct sequence of two-register reductions from the innermost core outward.

---

## From Warsaw to Palo Alto: The Four-Register Lineage

Łukasiewicz's 1924 logic notation and Hamblin's 1957 hardware stack, formalized for digital computer evaluation by Arthur Burks, Don Warren, and Jesse Wright in 1954 {{cite:burks1954}}, became the native operating language of scientific handhelds in 1972, when William Hewlett, David Cochran, and the Palo Alto engineering team {{cite:hewlett1972,cochran1972}} introduced the HP-35, the world's first pocket scientific calculator, supplanting the slide rule with a 4-register operational stack ($X, Y, Z, T$). Over the next two decades, Hewlett-Packard's Corvallis division steadily expanded that four-register architecture: in 1979–1982, William M. Kahan and the HP-34C / HP-15C Voyager team {{cite:hp15c1982,kahan1979}} brought Richard Brent's hybrid root-finding algorithm (`SOLVE`), adaptive Romberg quadrature (`∫f(x)`), and complex-number arithmetic into a shirt-pocket instrument.

In 1991, the HP-32SII Pioneer (succeeding the 1988 HP-32S) {{cite:hp32sii1991}} paired those same Brent `SOLVE` and Romberg `∫` engines with 26 named `A`–`Z` variables, a symbolic Equation Bank (`EQN`), exact fraction reduction, and eight SI/Imperial unit conversions. The StackCalc SC-32 continues that four-register architecture on a 4-line transflective LCD ($T, Z, Y, X$ visible simultaneously) with a 6-key softkey bar, RPN equation storage, closed-form quadratic/cubic `{{key:POLY}}`, five-variable `{{key:TVM}}` finance, parallel-harmonic (`{{key:x∥y}}`) and quotient-remainder (`{{key:÷R}}`) operators, and a $128 \times 52\text{-pixel}$ `{{key:PLOT}}` canvas.

While the SC-32 defaults to the classic 4-register stack (`4-LVL`) for direct keystroke parity with the HP-35, HP-15C, and HP-32SII, its `{{key:FLAGS}}` menu also allows expanding the operational stack to 8 registers (`8-LVL`, providing a full 4-level complex stack when each complex number occupies two registers) or an unbounded 999-level LIFO stack (`INF`) for deep multi-branch networks. Because the operational rules of Registers $X, Y, Z,$ and $T$ remain constant across this lineage, every four-register postfix recurrence and keystroke sequence applies directly across any four-register RPN instrument as well as the free, open-source browser simulator at [stackcalc.io](https://stackcalc.io):

| Architectural Feature | HP-35 (1972) | HP-15C Voyager (1982) | HP-32SII Pioneer (1991) | StackCalc SC-32 (Present) |
| :--- | :--- | :--- | :--- | :--- |
| **Processor Architecture** | 56-bit serial PMOS (10-digit BCD) | 56-bit Nut CMOS (10-digit BCD) | 64-bit Saturn CMOS (12-digit BCD) | 64-bit IEEE-754 double-precision math engine |
| **Display & Stack View** | 1-line 15-char red LED (`X` only) | 1-line 10-digit 7-seg LCD (`X` only) | 1-line 12-char dot-matrix LCD (`X` only) | 4-line 132×65 transflective LCD ($T, Z, Y, X$ visible) |
| **Operational Stack** | 4-level ($X, Y, Z, T$) | 4-level ($X, Y, Z, T$) | 4-level ($X, Y, Z, T$) | Selectable `4-LVL`, `8-LVL`, or `INF` (999-level) |
| **Dynamic Softkeys** | None | None | Remaps top row (`√x`..`Σ+`) in menus | Dedicated 6-key LFU softkey strip |
| **Variables & Equations** | 1 storage register | Numbered `R0`–`R9` / `LBL 0..9` | Named `A`–`Z` & Infix `EQN` (`(`, `)`, `=`) | Named `A`–`Z` (89 slots) & RPN `{{key:EQN}}` Bank |
| **Numerical Solver** | None | Brent–Kahan hybrid (via `LBL`) | Brent–Kahan hybrid (via `EQN` / `LBL`) | Brent–Kahan `{{key:SOLVE}}` ($10^{-12}$) + Closed-Form `{{key:POLY}}` |
| **Quadrature Engine** | None | Adaptive Romberg (via `LBL`) | Adaptive Romberg (via `EQN` / `LBL`) | Adaptive Romberg Richardson extrapolation ($10^{-12}$) |
| **Complex Numbers** | None | Parallel imaginary stack (`I` / `Re⇄Im`) | 4-register $(Y,X)$ & $(T,Z)$ via `CMPLX` | 4-line visible $(T,Z,Y,X)$ `{{key:CMPLX}}` + complex `{{key:x∥y}}` & `{{key:POLY}}` |
| **Financial (`TVM`)** | None | None (HP-12C required) | None (HP-12C required) | Built-in 5-variable `{{key:TVM}}` (`N`, `I%`, `PV`, `PMT`, `FV`) |
| **Parallel & Integer Math** | Manual reciprocal $(1/x)$ | Manual reciprocal $(1/x)$ | Fractions `a b/c`; `PARTS` softkeys | Direct `{{key:x∥y}}`, `{{key:ABS}}` & `{{key:÷R}}` keys (`GCD`/`LCM` in `PARTS` menu) |
| **Graphical Plotting** | None | None | None | $128 \times 52\text{ px}$ `{{key:PLOT}}` function & scatter canvas |
| **Non-Volatile Memory** | None (volatile RAM) | CMOS continuous memory | CMOS continuous memory | Continuous non-volatile flash memory |

| Chapter | Title & Scope | Mathematical & Engineering Landmarks |
| :--- | :--- | :--- |
| **[Chapter 1](01-craftsmanship-hardware.md)** | **Slide Rules, Quartz Oscillators & Pocket Instrument Design** | Bill Hewlett's 1971 shirt-pocket specification; scientific notation ($m \times 10^n$); $32,768\text{ Hz}$ ($2^{15}\text{ Hz}$) quartz oscillators; daylight optics & Ohm's/Joule's laws |
| **[Chapter 2](02-rpn-stack-dynamics.md)** | **The Architecture of Inside-Out Thinking** | George Miller's working-memory capacity; Dijkstra's Shunting-Yard algorithm; reciprocal rate combination; continued fractions ($\pi \approx 355/113$, Golden Ratio $\varphi$) & Viète's nested radicals |
| **[Chapter 3](03-algebra-transcendentals.md)** | **Logarithms, Power Laws & Exponential Scaling** | John Napier (1614) & Leonhard Euler ($e$); Weber-Fechner logarithmic scales (decibels, Richter, pH); Kleiber's $M^{3/4}$ metabolic law; the 5-domain harmonic operator `{{key:x∥y}}`; Carbon-14 decay & Lanczos Gamma ($70!$) |
| **[Chapter 4](04-trig-vectors-polar.md)** | **Circular Trigonometry, Vector Projections & Hyperbolic Functions** | Eratosthenes's 240 BC meridian arc; circular projections & the Law of Cosines; aircraft crosswind triangles & surveying traverses (`{{key:▸y,x}}`, `{{key:▸θ,r}}`); Bernoulli's 1691 catenary ($\cosh x$) & relativistic rapidities ($\tanh\phi$) |
| **[Chapter 5](05-complex-numbers-phasors.md)** | **Complex Numbers, Euler's Identity & Alternating-Current Phasors** | Orthogonal $90^\circ$ rotation by $i = \sqrt{-1}$; Euler's identity ($e^{i\pi} + 1 = 0$); Charles Proteus Steinmetz's AC impedance phasors; polyphase networks & loudspeaker crossovers |
| **[Chapter 6](06-geometry-surface-area.md)** | **The Square-Cube Law, Solid Geometry & Three-Dimensional Space** | Galileo's 1638 Square-Cube Law; Archimedes's sphere-and-cylinder ratio; Heron's formula; Cavalieri's principle; 3D print slicing, Center of Mass & Moment of Inertia ($I$) |
| **[Chapter 7](07-polynomials-brent-solver.md)** | **Polynomial Evaluation, Cardano's Cubic & Brent's Root-Finder** | Al-Khwarizmi's completing the square (AD 820); the 1535 Tartaglia–Cardano cubic solution; Horner's nested evaluation; Newton-Raphson divergence & Richard Brent's hybrid `{{key:SOLVE}}` algorithm |
| **[Chapter 8](08-calculus-romberg-quadrature.md)** | **Archimedes' Balance Beam, Central Differences & Romberg Quadrature** | Symmetric central-difference derivatives; definite integrals by recursive trapezoidal refinement; Werner Romberg's $\frac{4}{3}T_{\text{fine}} - \frac{1}{3}T_{\text{coarse}}$ Richardson extrapolation; Tsiolkovsky rocket staging & hydrostatic load |
| **[Chapter 9](09-statistics-curve-fitting.md)** | **Least Squares, Small Samples & the Geometry of Uncertainty** | Gauss's 1801 orbit determination of Ceres via Least Squares; sample standard deviation & Bessel's $n - 1$ degree-of-freedom correction; Galton's regression to the mean; Gosset's small-sample $t$-distribution |
| **[Chapter 10](10-computer-science-bases.md)** | **Boolean Logic, Two's Complement & the 36-Bit Word** | Leibniz's 1703 binary arithmetic; Claude Shannon's 1937 switching algebra; modular ring arithmetic & Two's Complement signed integers; 36-bit words, IPv4 subnet masks & RGB bitfield packing |
| **[Chapter 11](11-financial-tvm.md)** | **Compound Interest, Amortization & the Time Value of Money** | Fibonacci's 1202 *Liber Abaci*; geometric return asymmetry; the cash-flow sign convention; 30-year mortgage amortization dynamics; bond pricing, `NPV` & `IRR` |
| **[Chapter 12](12-function-scatter-plotting.md)** | **Cartesian Coordinates, Pixel Rasterization & Visual Analysis** | Descartes's 1637 coordinate geometry; Jack Bresenham's 1962 integer line rasterization; Francis Anscombe's 1973 Quartet; visual root bracketing (`{{key:PLOT}}` $\to$ `{{key:SOLVE}}`) |
| **[Chapter 13](13-applied-stem-case-studies.md)** | **Coupled Laws of Classical and Modern Engineering** | Compound microscope optics; Root-Sum-Square (RSS) mechanical tolerance stacking; Reynolds pipe flow; Euler column buckling; Carnot heat exchangers; Sabine acoustics & geostationary orbits |
| **[Chapter 14](14-uil-contest-playbook.md)** | **Fermi Estimation, Algebraic Symmetry & High-Speed Calculation** | Enrico Fermi's 1945 order-of-magnitude estimation; dimensional bounds checking; algebraic difference of squares ($48 \times 52$); half-integer squaring; single-entry `{{key:LASTX}}` Horner evaluation |
| **[Appendices A–E](appendix-a-stack-lift-state-machine.md)** | **Formal Reference Compendium** | **App. A:** Stack-Lift State Machine • **App. B:** 12 Error Codes • **App. C:** 43-Key Directory & Instrument Architecture • **App. D:** Constants & 100 STEM Equations • **App. E:** Annotated Bibliography |

---

## Evaluating Nested Equations Across the Four Registers

{{blocks:sc32_hero_keynote|The StackCalc SC-32 handheld RPN scientific computer: monolithic chassis, tactile TPU keypad, and daylight-reflective vector display.}}

On the StackCalc SC-32 display glass, four live registers sit stacked vertically from Register $T$ at the top down to Register $X$ at the bottom, without a single `(`, `)`, or `=` key on the bezel. At power-on, the instrument initializes in decimal floating-point format (`{{key:DEC}}`, `{{key:ALL}}`) and degree angle mode (`{{key:DEG}}`).

### Chaining Measurements and Eliminating Parentheses

Three foundational operations—`{{key:ENTER}}`, *automatic stack lift*, and *two-branch drops*—govern how operands move across the four visible registers:

1. **Adding Two Numbers (`14` and `6`):**
   Keying `14` enters the first value into Register $X$. Pressing `{{key:ENTER}}` marks that first number complete and lifts `14` into Register $Y$. Keying `6` then places the second value into Register $X$ so that `14` (in $Y$) and `6` (in $X$) are visible simultaneously. Pressing `{{key:+}}` drops Register $Y$ and combines it with Register $X$ to yield `20`.
2. **Automatic Stack Lift (Chaining Without Pressing `{{key:ENTER}}` Again):**
   To multiply three physical dimensions in sequence, such as the volumetric melt flow rate $\dot{Q} = w \times h \times v$ of a 3D printer hotend extruding a $w = 0.45\text{ mm}$ bead width at a $h = 0.20\text{ mm}$ layer height and $v = 180\text{ mm/s}$ printhead speed, keying `0.45 {{key:ENTER}} 0.20 {{key:×}}` computes the cross-sectional area of the bead, `0.09` $\text{mm}^2$, in Register $X$. Multiplying that `0.09` by `180` requires no second `{{key:ENTER}}`. Because `0.09` is a completed result, touching `1` to begin typing `180` triggers *automatic stack lift*, which moves `0.09` into Register $Y$. Keying `180` and pressing `{{key:×}}` yields `16.2` $\text{mm}^3/\text{s}$ in Register $X$.

{{res:sc32_hero_stack:screenshot|Chaining three measurements on the live 4-register stack: evaluating the volumetric melt flow rate Q = w × h × v = 0.45 mm × 0.20 mm × 180 mm/s = 16.2 mm³/s of a 3D printer hotend.}}

3. **Untangling a Two-Branch Fraction Across Registers $Z$ and $Y$:**
   A two-branch rational expression such as dividing a hydraulic pump's output capacity by the combined cross-sectional area of two parallel intake manifolds ($3.2\text{ cm}^2$ and $4.9\text{ cm}^2$),
   $$Q = \frac{12.4 \times 8.6}{3.2 + 4.9} \quad \text{[L/min]}$$
   requires no parentheses on the SC-32 because Registers $Y$ and $Z$ stage intermediate subtotals above the active register. Once the numerator $12.4 \times 8.6 = 106.64$ is evaluated in Register $X$, that completed subtotal is armed for stack lift. Typing the first denominator term (`3.2`) lifts $106.64$ into Register $Y$, and pressing `{{key:ENTER}}` to separate `3.2` from `4.9` shifts $106.64$ into Register $Z$ while the two intake areas occupy Registers $Y$ and $X$. When `{{key:+}}` collapses $3.2 + 4.9$ into $8.1000\text{ cm}^2$ in Register $X$, the waiting numerator drops from Register $Z$ back into Register $Y$ so the two completed branches align for `{{key:÷}}` (`{{res:sc32_index_seq_01:keys}}` $\to \mathbf{{{res:sc32_index_seq_01:value}}\text{ L/min}}$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `12.4` | $0.0000$ | $0.0000$ | $0.0000$ | $12.4000$ | Keying first numerator factor |
| `{{key:ENTER}}` | $0.0000$ | $0.0000$ | $12.4000$ | $12.4000$ | Stack lift: pushes $12.4$ into $Y$ |
| `8.6` | $0.0000$ | $0.0000$ | $12.4000$ | $8.6000$ | Entering second factor into $X$ |
| `{{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $106.6400$ | Numerator product: $12.4 \times 8.6$ |
| `3.2` | $0.0000$ | $0.0000$ | $106.6400$ | $3.2000$ | Automatic stack lift: numerator preserved in $Y$ |
| `{{key:ENTER}}` | $0.0000$ | $106.6400$ | $3.2000$ | $3.2000$ | Numerator elevated to $Z$; $3.2$ in $Y$ |
| `4.9` | $0.0000$ | $106.6400$ | $3.2000$ | $4.9000$ | Loading second denominator term |
| `{{key:+}}` | $0.0000$ | $0.0000$ | $106.6400$ | $8.1000$ | Denominator summed in $X$; numerator drops to $Y$ |
| `{{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$13.1654$** | Final quotient $106.64 / 8.1$ |

### Parallel Harmonics, Nernst Potentials, and Nested Radicals

Three electrical pathways wired in parallel ($R_1 = 100\,\Omega$, $R_2 = 220\,\Omega$, $R_3 = 470\,\Omega$) obey the reciprocal conductance relation:
$$\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$$
Parallel resistors combine by reciprocals because all three branches share the same voltage while their electrical conductances ($G_i = 1/R_i$, in Siemens) add directly. On a traditional RPN keypad, you invert each resistance into a conductance in place with the unary `{{key:1/x}}` key, accumulate the running sum across Register $Y$ and Register $X$, and invert the total conductance back into Ohms (`{{res:sc32_index_seq_03:keys}}` $\to \mathbf{{{res:sc32_index_seq_03:value}}\,\Omega}$).

More directly, the SC-32's dedicated parallel-harmonic key `{{key:x∥y}}` ($x \parallel y = \frac{yx}{y+x}$) reduces that reciprocal sum-and-invert sequence to an associative fold across the lower two registers: pressing `{{key:x∥y}}` collapses the first two branches in $Y$ and $X$ into their combined equivalent resistance and arms stack lift, so typing the third resistor pushes the two-branch subtotal into Register $Y$ for a second parallel fold (`{{res:sc32_index_seq_04:keys}}` $\to \mathbf{{{res:sc32_index_seq_04:value}}\,\Omega}$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `100 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $100.0000$ | $100.0000$ | Load $R_1 = 100\,\Omega$ into $Y$ and $X$; stack lift disabled |
| `220` | $0.0000$ | $0.0000$ | $100.0000$ | $220.0000$ | Overwrite Register $X$ with second branch $R_2 = 220\,\Omega$ |
| `{{key:x∥y}}` | $0.0000$ | $0.0000$ | $0.0000$ | $68.7500$ | Collapse $Y$ and $X$ into $100 \parallel 220 = 68.75\,\Omega$; stack lift armed |
| `470` | $0.0000$ | $0.0000$ | $68.7500$ | $470.0000$ | Auto-lift $68.75\,\Omega$ to $Y$ and load third branch $R_3 = 470\,\Omega$ in $X$ |
| `{{key:x∥y}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$59.9768$** | Collapse $Y$ and $X$ into 3-branch equivalent $R_{\text{eq}} \approx 59.9768\,\Omega$ |

Across that entire three-branch reduction, Registers $Z$ and $T$ remain at zero because each harmonic fold immediately collapses $Y$ and $X$ back into a single number in Register $X$. That same two-register economy carries straight over to geometrical optics. In Carl Friedrich Gauss's thin-lens equation ($\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i} \implies f = d_o \parallel d_i$), a converging glass lens bends diverging wavefronts from an object distance $d_o = 45\text{ cm}$ into converging wavefronts focused at an image distance $d_i = 90\text{ cm}$ by adding their optical vergences ($1/45\text{ cm}^{-1}$ and $1/90\text{ cm}^{-1}$). Loading $d_o = 45\text{ cm}$ into Register $Y$ and $d_i = 90\text{ cm}$ into Register $X$ and pressing `{{key:x∥y}}` (`{{res:sc32_index_seq_13:keys}}`) collapses the two distances directly into the lens's focal length $f = \mathbf{{{res:sc32_index_seq_13:value}}\text{ cm}}$ in Register $X$, while Registers $Z$ and $T$ remain at zero.

Inside-out evaluation also flattens multi-layer transcendental formulas so they barely need upper stack registers at all. In Walther Nernst's 1889 electrochemical cell equation for a Daniell copper-zinc battery at $298.15\text{ K}$ ($n = 2\text{ moles}$ of electrons transferred per reaction, thermal voltage factor $RT/F = 0.025693\text{ V}$, and standard potential $E^\circ = 1.100\text{ V}$), a diluted zinc-ion anode activity ($0.015\text{ M}$) and concentrated copper-ion cathode activity ($0.850\text{ M}$) raise the cell voltage above its standard baseline:

$$E = E^\circ - \frac{R T}{n F} \ln Q = 1.100 - \frac{0.025693}{2} \ln\left(\frac{0.015}{0.850}\right)$$

Rather than typing from left to right and stalling after $1.100 -$, inside-out evaluation begins with the reaction quotient $Q = 0.015 / 0.850 = 0.017647$. Once that ratio sits in Register $X$, the next three physical transformations happen entirely inside Register $X$ without lifting the stack: `{{key:LN}}` converts the concentration ratio in place into $\ln Q = -4.0372$, multiplying by $0.025693\text{ V}$ scales it into single-electron Volts, and dividing by $2$ leaves the Nernst overpotential $-0.05186\text{ V}$ in Register $X$ while $Y, Z,$ and $T$ remain at zero. Entering the standard potential $1.100\text{ V}$ then lifts $-0.05186\text{ V}$ into Register $Y$, where `{{key:x⇄y}}` (the Register Swap key) orders the two terms for subtraction (`{{res:sc32_index_seq_25:keys}}` $\to \mathbf{{{res:sc32_index_seq_25:value}}\text{ V}}$).

The clearest demonstration of this single-register collapse is the four-level nested radical pyramid from the opening equation:
$$x = \sqrt{7 + \sqrt{13 + \sqrt{29 + \sqrt{41}}}}$$
On an algebraic keypad, typing that expression from the outside in requires opening four nested levels of parentheses while three unfinished additions hang suspended in memory. On the SC-32, walking from the innermost radicand outward via `{{res:sc32_index_seq_34:keys}}` extracts $\sqrt{41} = \mathbf{{{res:sc32_index_seq_34:value}}}$ in place in Register $X$. Typing $29$ lifts $6.4031$ into Register $Y$ for an instant before addition and `{{key:√x}}` collapse $29 + 6.4031 = 35.4031$ into $\sqrt{35.4031} \approx 5.9501$ in Register $X$. Adding $13$ and extracting the root collapses $\sqrt{18.9501}$ into $4.3532$, and adding $7$ before one final square root (`{{res:sc32_index_seq_26:keys}}`) resolves the four-level radical to $\mathbf{{{res:sc32_index_seq_26:value}}}$ with Registers $Y, Z,$ and $T$ resting at zero at the close of every layer.
