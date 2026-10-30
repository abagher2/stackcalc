---
title: "Chapter 10: Boolean Logic, Two's Complement & the 36-Bit Word | Thinking in the Stack (SC-32)"
description: "36-bit two's complement integer architecture, base conversions (HEX, DEC, OCT, BIN), integer division & remainder bit-field extraction (÷R), CIDR IPv4 subnetting, RGB565 packing, combinatorics, and IEEE-754 representation on the StackCalc SC-32."
---

# Chapter 10: Boolean Logic, Two's Complement & the 36-Bit Word

## Leibniz's Medallion, Boole's Logic & Claude Shannon's 1937 Master's Thesis

### Leibniz's Binary Arithmetic and Shannon's Switching Relays

In the summer of 1937, MIT master's student Claude Elwood Shannon worked in the basement housing Vannevar Bush's Differential Analyzer alongside brass gears and electromechanical telephone relays. That hundred-ton mechanical analog computer used spinning steel shafts, torque amplifiers, and wheel-and-disc integrators to solve differential equations through physical rotation.

Every time a physicist or ballistician brought a new differential equation to the laboratory, Shannon configured two distinct subsystems: the continuous mechanical shafts of the analyzer, and a network of telephone relay circuits that controlled its switches, clutches, and safety interlocks.

Wiring those relays in series and in parallel, Shannon recognized the exact structure he had studied in an undergraduate logic course at the University of Michigan: the symbolic algebra of nineteenth-century English mathematician George Boole, published in 1854 as *An Investigation of the Laws of Thought*. Boole had formulated propositional reasoning as algebra. If a statement was true, Boole assigned it the number $1$; if it was false, he assigned it the number $0$. Combining two statements with the conjunction AND behaved like multiplication ($1 \times 1 = 1$, while $1 \times 0 = 0$); combining them with OR behaved like a saturating addition ($1 + 0 = 1$); and negating a statement with NOT inverted $1$ to $0$ and $0$ to $1$.

Boole had followed an even older trail. In 1703, the German polymath Gottfried Wilhelm Leibniz had presented a paper to the Royal Academy of Sciences in Paris titled *Explication de l'Arithmétique Binaire*. Leibniz noted that every integer could be represented using only two symbols, $1$ and $0$, and sketched a commemorative medallion showing light ($1$) emerging from the void ($0$) under the Latin motto *Omnibus ex nihilo ducendis sufficit unum* ("To derive everything from nothing, one suffices"). Yet for more than two centuries after Leibniz and eight decades after Boole, binary numbers and Boolean logic were treated as philosophical curiosities with no direct connection to machinery.

Observing the racks of telephone relays in the MIT basement, Shannon established the isomorphism between switching networks and Boolean algebra. Two switches wired in series allow electrical current to pass only if Switch A is closed AND Switch B is closed ($A \cdot B$). Two switches wired in parallel allow current to pass if Switch A is closed OR Switch B is closed ($A + B$). A normally closed relay contact that opens when its electromagnet is energized acts as a physical NOT inverter ($\overline{A}$). Every open or closed relay on a telephone switchboard was a physical realization of George Boole's two-valued algebra, and because Leibniz had shown that any number can be written in base-2 binary digits, circuits built from those logical switches could add, subtract, compare, and store numbers electronically.

In his 1937 MIT master's thesis, published in 1938 {{cite:shannon1938}}, Shannon proved that any logical decision or arithmetic operation can be synthesized from binary switching gates. Even the fundamental unit of digital information—the bit (*binary digit*)—was coined by Shannon's Bell Labs colleague John Tukey and codified in Shannon's 1948 paper *A Mathematical Theory of Communication*. Every microprocessor, memory cell, router, and spacecraft guidance computer built over the past nine decades traces its architecture to that 1937 synthesis of symbolic logic and electrical switching.

### Building Binary Addition from AND, OR, and XOR Gates

To see how Boolean switching gates perform arithmetic, consider how a silicon circuit adds two binary bits $A$ and $B$. When adding $A + B$ in base 2, the circuit produces a two-bit sum consisting of a Carry bit (in the twos column, $2^1$) and a Sum bit (in the ones column, $2^0$). When $A = 0$ and $B = 0$, the result is $00_2$ ($\text{Carry} = 0,\; \text{Sum} = 0$); when $A = 0$ and $B = 1$, or $A = 1$ and $B = 0$, the result is $01_2$ ($\text{Carry} = 0,\; \text{Sum} = 1$); and when $A = 1$ and $B = 1$, the binary sum is $1 + 1 = 2_{10} = 10_2$ ($\text{Carry} = 1,\; \text{Sum} = 0$).

Those two output columns correspond directly to elementary Boolean gates:

| Input Bit $A$ | Input Bit $B$ | Carry Bit ($2^1$ Column) | Sum Bit ($2^0$ Column) | Logical Meaning |
| :---: | :---: | :---: | :---: | :--- |
| `0` | `0` | `0` | `0` | Neither switch closed $\implies 0$ |
| `0` | `1` | `0` | `1` | Exactly one switch closed $\implies 1$ |
| `1` | `0` | `0` | `1` | Exactly one switch closed $\implies 1$ |
| `1` | `1` | `1` | `0` | Both closed $\implies$ Carry `1`, Sum wraps to `0` |

The Carry column is `1` *if and only if* both $A$ AND $B$ are `1`, which is a single Boolean `AND` gate. Meanwhile, the Sum column is `1` *if and only if* $A$ or $B$ is `1`, but not both, matching the truth table of the Exclusive-OR (`XOR`, $\oplus$) gate. Wiring one `XOR` gate and one `AND` gate side by side across the same two input wires forms a physical Half-Adder, a circuit of two-state logic switches that performs binary addition. Chaining thirty-six adders together so that each column's carry feeds into the next column to its left enables a silicon register to add ten-digit integers in a single clock cycle.

---

## Positional Radices and the 36-Bit Word Architecture

### Positional Radices: Decimal, Binary, Octal, and Hexadecimal

The integer `255` takes four distinct written forms across the standard positional bases—`255` in decimal, `11111111b` in binary, `377o` in octal, and `FFh` in hexadecimal—even though all four strings represent the identical quantity.

When humans learned to count in antiquity, they grouped objects in tens (Decimal, base $b = 10$) corresponding to the ten fingers of the hands. Writing the decimal number $1,042_{10}$ expresses a polynomial in powers of $10$ from the inside out:

$$1,042_{10} = 1 \times 10^3 + 0 \times 10^2 + 4 \times 10^1 + 2 \times 10^0 = ((1 \times 10 + 0) \times 10 + 4) \times 10 + 2$$

The choice of radix $10$ is a convention of human anatomy rather than a requirement of arithmetic. Building an electronic circuit that distinguishes ten distinct voltage levels ($0\text{ V}, 0.5\text{ V}, 1.0\text{ V}, \dots, 4.5\text{ V}$) is vulnerable to thermal drift and noise margins. Instead, digital circuits operate with two states: OFF ($0$) and ON ($1$). In Binary (base $b = 2$), each column from right to left represents the next power of two ($2^0 = 1,\; 2^1 = 2,\; 2^2 = 4,\; 2^3 = 8,\; 2^4 = 16,\; \dots$):

$$1042_{10} = 1024 + 16 + 2 = 1 \times 2^{10} + 1 \times 2^4 + 1 \times 2^1 = 10000010010_2$$

Although binary matches two-state hardware, long strings of thirty-six binary digits such as `000011000000101010000000101000101101b` exceed the four-to-seven-item span of human working memory identified by George Miller. Computer scientists compress binary words into compact human-readable notation without dividing by $10$ by using radices that are exact powers of two: octal (`OCT`, base $b = 8 = 2^3$) and hexadecimal (`HEX`, base $b = 16 = 2^4$).

Because $8 = 2^3$, each octal digit (`0` through `7`) corresponds to an exact 3-bit triad (`000` through `111`), so converting between binary and octal requires only partitioning the bit string into 3-bit groups from right to left. Similarly, because $16 = 2^4$, each hexadecimal digit corresponds to an exact 4-bit nibble (`0000` through `1111`). For values from $0$ to $9$, hexadecimal uses the standard digits `0`–`9`; for the remaining six 4-bit patterns ($10$ through $15$), it uses the letters `A` ($= 10$), `B` ($= 11$), `C` ($= 12$), `D` ($= 13$), `E` ($= 14$), and `F` ($= 15$). Two hexadecimal digits side by side (`00h` through `FFh`) pack an exact 8-bit byte (an octet, $2^8 = 256$ values from $0$ to $255$).

| Decimal (`DEC`) | 4-Bit Binary Nibble (`BIN`) | Octal (`OCT`) | Hexadecimal (`HEX`) | Positional Power Decomposition |
| :---: | :---: | :---: | :---: | :--- |
| `0` | `0000b` | `0o` | `0h` | $0$ |
| `5` | `0101b` | `5o` | `5h` | $4 + 1 = 2^2 + 2^0$ |
| `7` | `0111b` | `7o` | `7h` | $4 + 2 + 1 = 2^3 - 1$ |
| `8` | `1000b` | `10o` | `8h` | $2^3$ (one full octal triad carry) |
| `10` | `1010b` | `12o` | `Ah` | $8 + 2 = 2^3 + 2^1$ |
| `12` | `1100b` | `14o` | `Ch` | $8 + 4 = 2^3 + 2^2$ |
| `15` | `1111b` | `17o` | `Fh` | $8 + 4 + 2 + 1 = 2^4 - 1$ (all 4 nibble bits ON) |

Hexadecimal reduces binary inspection to direct nibble translation. When inspecting the 16-bit hexadecimal word `3C6Ah`, the four nibbles expand from left to right as `3h` $= 2 + 1 = \mathtt{0011}$, `Ch` ($12_{10}$) $= 8 + 4 = \mathtt{1100}$, `6h` $= 4 + 2 = \mathtt{0110}$, and `Ah` ($10_{10}$) $= 8 + 2 = \mathtt{1010}$. Concatenating those four nibbles yields `0011 1100 0110 1010b`, compressing sixteen binary digits into four hexadecimal characters. On the SC-32, pressing the `{{key:BASE}}` menu via Left Shift `{{key:↰}}` + `{{key:×}}` places those four radix modes—`{{key:HEX}}`, `{{key:DEC}}`, `{{key:OCT}}`, and `{{key:BIN}}`—onto the top softkeys and re-renders all four stack registers (`T, Z, Y, X`) on screen without altering their underlying 36-bit values. Whenever `{{key:HEX}}` is active, the top row of scientific keys from `{{key:√x}}` through `{{key:Σ+}}` operates as an `A`–`F` hexadecimal keypad.

### The 36-Bit Word Architecture of the IBM 7090 and DEC PDP-10

Modern general-purpose processors organize their registers in multiples of 8-bit bytes, typically 32 or 64 bits wide. By contrast, the scientific and artificial-intelligence mainframes of the 1950s through the 1970s standardized on the 36-bit word.

When Katherine Johnson, Dorothy Vaughan, and NASA's Flight Research Division computed the orbital trajectories for John Glenn's *Friendship 7* Mercury flight and the Apollo lunar rendezvous studies, chronicled in Margot Lee Shetterly's *Hidden Figures*, the mainframes at Langley and Goddard were IBM 7090 and IBM 7094 systems built around 36-bit registers. When John McCarthy and Marvin Minsky founded the MIT Artificial Intelligence Laboratory and created the LISP programming language (`CAR` and `CDR` stood for *"Contents of the Address part of Register"* and *"Contents of the Decrement part of Register"* on the 36-bit IBM 704), they designed around 36-bit words. Likewise, when researchers at MIT, Stanford, CMU, and BBN built the initial nodes of the ARPANET, their primary time-sharing platform was Digital Equipment Corporation's DEC PDP-10, another 36-bit architecture.

Architects of mid-twentieth-century scientific mainframes selected the 36-bit word for its divisibility and decimal range. In number theory, $36$ is an abundant, highly composite integer divisible by $1, 2, 3, 4, 6, 9, 12,$ and $18$. Whereas a 32-bit word divides evenly into eight 4-bit hexadecimal nibbles ($32 = 8 \times 4$) but leaves a 2-bit remainder when grouped into 3-bit octal triads ($32 = 10 \times 3 + 2$), a 36-bit word is the smallest practical computer word that divides with zero remainder into both twelve 3-bit octal digits ($36 = 12 \times 3$) and nine 4-bit hexadecimal nibbles ($36 = 9 \times 4$).

Furthermore, whereas a signed 32-bit integer overflows at $+2,147,483,647$ (fewer than ten full decimal digits, insufficient for a 10-digit telephone number or an unsigned 32-bit IPv4 broadcast address), $2^{36} = 68,719,476,736 \approx 6.87 \times 10^{10}$ provides ten full decimal digits of integer capacity. Thirty-six bits also partition into two symmetric 18-bit half-words ($36 = 2 \times 18$, which allowed LISP and the PDP-10 to pack two memory pointers into a single register) or six 6-bit alphanumeric characters ($36 = 6 \times 6$).

When IBM introduced the System/360 in 1964, Gene Amdahl and Fred Brooks standardized commercial computing on 8-bit bytes and 32-bit words. On a signed 32-bit calculator, however, entering an unsigned 32-bit hexadecimal value such as `0xFFFFFFFF` ($4,294,967,295$) encounters a sign-bit conflict: because Bit 31 is the sign bit on a 32-bit word, `0xFFFFFFFF` is either rejected as an overflow or interpreted as $-1$.

By adopting a 36-bit word across all four stack registers ($T, Z, Y, X$), the SC-32 places its sign bit four positions higher at Bit 35. Every 32-bit unsigned memory address, IPv4 network mask (`0xFFFFFFFF`), or microcontroller register sits in Bits 31–0 as a strictly positive integer, with four additional bits above the 32-bit boundary: three positive magnitude headroom bits (`Bits 34–32`, expanding positive range $8\times$) and the dedicated sign bit at `Bit 35` to accommodate overflow carries, checksum folds, and bit-shifts without truncation.

---

## Mechanical Odometers, Two's Complement Arithmetic & Bitwise Masks

### Two's-Complement Modular Addition

Because a silicon register contains only binary switches that are `1` (ON) or `0` (OFF), representing signed negative integers requires encoding the sign within the bit pattern itself.

Early computer designers in the 1940s tried the obvious idea first: use the leftmost bit as a "sign flag" (`0` for $+$, `1` for $-$) and leave the remaining bits as the ordinary magnitude (Sign-Magnitude representation). That sounds simple until you try to build the adder circuit: to add $+5$ and $-3$, the hardware first has to compare which number is larger, switch from an adder circuit to a subtractor circuit, and resolve two distinct representations of zero (`+0` and `-0`).

Modular arithmetic provides a direct way to represent negative numbers so that an ordinary binary adder can add positive and negative integers together without knowing which operands are negative. A 4-digit mechanical bicycle odometer set to `0000` miles illustrates how modular wrap-around encodes negative values. Riding forward $1\text{ mile}$ advances the rightmost wheel upward to `0001`, whereas starting at `0000` and rolling the wheel backward one mile ($0 - 1 = -1$) wraps all four mechanical number wheels backward one click from `0` to `9` so the odometer window reads `9999`. Rolling backward a second mile ($0 - 2 = -2$) yields `9998`, and rolling backward three miles ($-3$) yields `9997`.

Starting with the odometer at `9997` (the four-digit modular representation of $-3$) and riding forward $5\text{ miles}$ ($+5$) advances the wheels five clicks in sequence through `9998`, `9999`, `0000` (where the carry spills off the left end of the 4-digit window), `0001`, and finally `0002`. By representing $-3$ as $10,000 - 3 = 9997$, ordinary forward addition ($9997 + 0005 = \cancel{1}0002 \to \mathbf{0002}$) automatically computes $(-3) + 5 = +2$ without separate subtraction circuitry.

In binary hardware, that odometer wrap-around is called Two's Complement arithmetic. On a 36-bit binary odometer (`000000000h` in nine-nibble hexadecimal, the entry bound enforced when switching from `{{key:DEC}}` into `{{key:HEX}}`, `{{key:OCT}}`, or `{{key:BIN}}`), rolling forward from `000000000h` ($0$) counts upward through all positive 36-bit integers up to `7FFFFFFFFh` ($+2^{35} - 1 = +34,359,738,367$), where Bit 35 (the 36-bit sign boundary) is `0` and all 35 lower bits are `1`. Rolling backward one click from `000000000h` ($0 - 1 = -1$) turns every bit to `1` (`FFFFFFFFFh` across a 36-bit mask, or `FFFFFFFFFFFFFFFFh` across the SC-32's 64-bit internal two's-complement register). The Two's Complement negative ($-X$) of any integer $X$ follows directly from bitwise inversion: on a 36-bit odometer, $X$ plus its bitwise logical inverse $\overline{X}$ (where every `0` flips to `1` and every `1` flips to `0`) always equals thirty-six `1`s (`FFFFFFFFFh`), which is one click below zero ($-1$):

$$X + \overline{X} = \text{FFFFFFFFFh} \equiv -1 \pmod{2^{36}} \quad \Longrightarrow \quad -X = \overline{X} + 1$$

Flipping every bit (`NOT`) and adding $1$ produces the exact additive inverse. That single rule ($\overline{X} + 1$) is how modern microprocessors and the `{{key:+/-}}` change-sign key on the SC-32 negate integers and reduce subtraction ($Y - X = Y + \overline{X} + 1$) to pure addition.

| Bit Position | Field Designation | Meaning in 36-Bit Two's Complement |
| :---: | :---: | :--- |
| **Bit 35** | `MSB` / Sign Bit | `0` = Positive integer ($0$ to $+2^{35}-1$); `1` = Negative integer ($-2^{35}$ to $-1$) |
| **Bits 34–32** | Upper Headroom | Provides 3 full bits of positive magnitude headroom ($8\times$ capacity) below Sign Bit 35 |
| **Bits 31–0** | Standard 32-Bit Word | Holds full 32-bit unsigned addresses, IPv4 netmasks, and GPIO bitfields |

### Cleaving Words at Bit Boundaries via Euclidean Division (`÷R`)

In elementary arithmetic, dividing $12,345$ by $16$ produces a quotient of $771$ with a remainder of $9$, because:

$$12,345 = 771 \times 16 + 9$$

Number theorists call this Euclidean Division ($N = Q \cdot D + R$, with $0 \le R < D$). In algebra class, we often abandon remainders in favor of decimal fractions ($12,345 / 16 = 771.5625$). Yet in computer science, keeping the integer quotient $Q = \lfloor N / D \rfloor$ and the integer remainder $R = N \bmod D$ separate is one of the most versatile operations in mathematics.

Dividing a binary integer $N$ by a power of two $D = 2^k$ via Euclidean division cleaves the binary word in two at bit position $k$. The integer quotient $Q = \lfloor N / 2^k \rfloor$ performs a right bit-shift ($N \gg k$), sliding all upper bits from Bit $k$ upward down by $k$ positions into the ones column and discarding the lower $k$ bits. Simultaneously, the remainder $R = N \bmod 2^k$ forms a bitwise `AND` low-bit mask ($N \ \& \ (2^k - 1)$) that preserves the exact, unshifted value of the lower $k$ bits (`Bits [k-1 : 0]`).

On the SC-32, the dedicated Euclidean division key `{{key:÷R}}` (`{{key:↱}}` + `{{key:E}}`) models this cleavage directly across the two lower registers of the stack: placing any integer in Register $Y$ and a power-of-two divisor $2^k$ in Register $X$ and pressing `{{key:÷R}}` deposits the right-shifted upper quotient $\lfloor Y / X \rfloor$ into Register $X$ and the masked lower remainder $Y \bmod X$ into Register $Y$ in a single keystroke. In the $12,345 \div 16$ example expressed in hexadecimal, $12,345_{10} = \mathtt{3039h}$ and $16_{10} = 2^4 = \mathtt{10h}$. Dividing $\mathtt{3039h}$ by $\mathtt{10h}$ ($2^4$) via `{{key:÷R}}` places the quotient $Q = \mathtt{303h}$ ($771_{10}$, the upper nibbles shifted right by 4 bits) in Register $X$ and the remainder $R = \mathtt{9h}$ ($9_{10}$, the bottom 4-bit nibble masked off) in Register $Y$.

That single mathematical relationship unifies six classic computer-engineering operations without dedicated bit-shift submenus. Shifting left by $k$ bits ($X \ll k$) multiplies by $M = 2^k$, whereas shifting right by $k$ bits ($X \gg k$) takes the integer quotient on dividing by $M = 2^k$. Masking the lowest $k$ bits ($X \ \& \ (2^k - 1)$) extracts the remainder $X \bmod 2^k$, and snapping an address down to a $2^k$-aligned block ($X \ \& \ \overline{(2^k - 1)}$) takes the quotient $\lfloor X / 2^k \rfloor$ and multiplies back by $2^k$ to zero out the bottom $k$ bits. Extracting an interior bit-field (`Bits [m : k]`) takes the remainder modulo $2^{m+1}$ to strip bits above bit $m$ and divides by $2^k$ to shift bit $k$ down to bit $0$. Finally, adding $+2^k$ to a register whose $k$-th bit is `0` sets Bit $k$ to `1` (`OR`), while subtracting $2^k$ when Bit $k$ is `1` clears Bit $k$ to `0` (`AND NOT`) without affecting neighboring bits.

### Euclid's Remainder Ladder: Greatest Common Divisor (GCD) and Least Common Multiple (LCM)

Around 300 BCE in Alexandria, Euclid recorded in Book VII, Proposition 2 of his *Elements* what Donald Knuth called the oldest nontrivial algorithm in mathematics: the Euclidean Algorithm for the Greatest Common Divisor $\operatorname{GCD}(a, b)$ of two integers. When a digital signal processor runs one clock domain at $a = 1,071\text{ MHz}$ and another at $b = 462\text{ MHz}$, finding the largest common reference frequency that divides both evenly does not require prime factorization. Euclid noted that any divisor of both $a$ and $b$ must also divide the remainder $R = a \bmod b$ from Euclidean division (`{{key:÷R}}`). Replacing $(a, b)$ with $(b, a \bmod b)$ and pressing `{{key:÷R}}` repeatedly steps down Euclid's Remainder Ladder: $1071 = 2 \times 462 + 147 \longrightarrow 462 = 3 \times 147 + 21 \longrightarrow 147 = 7 \times 21 + 0$. The last non-zero remainder before `0` is $\operatorname{GCD}(1071, 462) = \mathbf{21}$.

On the SC-32, you can either step down Euclid's ladder manually with `{{key:÷R}}` or execute the entire ladder in a single keystroke inside the `{{key:PARTS}}` menu (Right Shift `{{key:↱}}` above `{{key:√x}}`), which places `{{key:GCD}}` (`{{key:LFU4}}`) and `{{key:LCM}}` (`{{key:LFU5}}`) side by side alongside `{{key:IP}}`, `{{key:FP}}`, `{{key:ABS}}`, and `{{key:SGN}}`. Once $\operatorname{GCD}(a, b)$ is known, dividing the product $|a \cdot b|$ by $\operatorname{GCD}(a, b)$ gives the Least Common Multiple:

$$\operatorname{LCM}(a, b) = \frac{|a \cdot b|}{\operatorname{GCD}(a, b)}$$

Together, `{{key:GCD}}` and `{{key:LCM}}` solve three everyday problems across computer engineering and mechanics: reducing gear-tooth or aspect ratios ($1920 \times 1080$ divided by $\operatorname{GCD}(1920, 1080) = 120$ gives the $16:9$ display ratio), finding the exact cycle period $\operatorname{LCM}(T_1, T_2)$ when two asynchronous timer buses realign in phase, and verifying that a public exponent $e$ is coprime to Euler's totient ($\operatorname{GCD}(e, \varphi(n)) = 1$) in RSA public-key cryptography.

### Real-World Bitwise Engineering: Subnet Masks, RGB Pixels, Base64, Endianness & IEEE-754 Floats

Reading hexadecimal nibbles and cleaving binary words at powers of two ($2^k$) clarifies five foundational operations in digital systems. In IPv4 address slicing and `CIDR` subnetting, every IPv4 address $A$ on the Internet is a single unsigned 32-bit integer written for human convenience in dotted-quad decimal notation $B_3.B_2.B_1.B_0$ as four 8-bit bytes (octets, each ranging from `0` to `255`, or `00h` to `FFh`), packed via Horner's radix-256 polynomial $A = ((B_3 \cdot 256 + B_2)\cdot 256 + B_1)\cdot 256 + B_0$:

| Address Component | Octet 1 (`Bits 31–24`) | Octet 2 (`Bits 23–16`) | Octet 3 (`Bits 15–8`) | Octet 4 (`Bits 7–0`) |
| :--- | :---: | :---: | :---: | :---: |
| **32-Bit Host IP ($A$)** | $B_3$ ($\times 2^{24}$) | $B_2$ ($\times 2^{16}$) | $B_1$ ($\times 2^8$) | $B_0$ ($\times 2^0$) |
| **`/24` Netmask (`FFFFFF00h`)** | `11111111` (Network) | `11111111` (Network) | `11111111` (Network) | `00000000` (Host) |
| **Aligned `/24` Network Base** | $B_3$ | $B_2$ | $B_1$ | `00000000` (`0`) |

In Classless Inter-Domain Routing (`CIDR`), a `/p` prefix notation specifies that the upper $p$ bits (`Bits [31 : 32-p]`) form the shared Network Prefix, while the remaining $k = 32 - p$ lower bits (`Bits [k-1 : 0]`, spanning $M = 2^k$ addresses per subnet block) identify the individual Host Offset. Dividing a 32-bit address $A$ (or its active boundary octet) by the block stride $M = 2^{32-p}$ via `{{key:÷R}}` cleaves the address right at the subnet boundary: the integer remainder $R = A \bmod 2^k$ isolates the host offset within the block, while multiplying the integer quotient $Q = \lfloor A / 2^k \rfloor$ back by $2^k$ zeroes out the $k$ host bits to snap directly to the aligned network base address $A_{\text{net}} = \lfloor A / 2^k \rfloor \times 2^k$. Adding the inverted host wildcard mask $W = 2^k - 1 = \mathtt{FFFFFFFFh} - \text{Netmask}$ then populates all $k$ host bits with `1`s to form the directed broadcast address $A_{\text{bcast}} = A_{\text{net}} + (2^k - 1)$.

A second application is packing color channels and Base64 characters by Horner's method. A smartwatch or microcontroller color display packs three separate Red, Green, and Blue brightness values into a single 16-bit memory word (`RGB565`). Because the cones in the human retina are most sensitive to subtle shades of green, `RGB565` allocates 5 bits ($R_5 \in [0, 31]$) to Red in `Bits [15:11]`, 6 bits ($G_6 \in [0, 63]$) to Green in `Bits [10:5]`, and 5 bits ($B_5 \in [0, 31]$) to Blue in `Bits [4:0]`:

| Channel Allocation | Bit Positions | Bit Width & Range | Positional Shift Multiplier |
| :--- | :---: | :---: | :---: |
| **Red ($R_5$)** | Bits `15–11` | 5 bits ($0\dots 31$, `00h–1Fh`) | $R_5 \times 2^{11}$ (`× 800h`) |
| **Green ($G_6$)** | Bits `10–5` | 6 bits ($0\dots 63$, `00h–3Fh`) | $G_6 \times 2^5$ (`× 20h`) |
| **Blue ($B_5$)** | Bits `4–0` | 5 bits ($0\dots 31$, `00h–1Fh`) | $B_5 \times 2^0$ (unshifted) |
| **Packed `RGB565` Word** | Bits `15–0` | 16-bit unsigned pixel (`0000h–FFFFh`) | $(R_5 \times \mathtt{800h}) + (G_6 \times \mathtt{20h}) + B_5$ |

Packing the three non-overlapping channels into a single 16-bit integer evaluates $(R_5 \times 2^{11}) + (G_6 \times 2^5) + B_5$, whereas unpacking any 16-bit pixel back into its three color channels requires only two Euclidean divisions (`{{key:÷R}}`) at $2^{11} = \mathtt{800h}$ and $2^5 = \mathtt{20h}$. That same bit-slicing geometry powers Base64 encoding across the web. To transmit binary data over text-only protocols, Base64 welds each group of three 8-bit ASCII bytes $(B_2, B_1, B_0)$ into a single 24-bit integer ($3 \times 8 = 24\text{ bits}$) and slices it at $2^{18} = \mathtt{40000h}$, $2^{12} = \mathtt{1000h}$, and $2^6 = \mathtt{40h}$ into four 6-bit sextet indices ($4 \times 6 = 24\text{ bits}$, each ranging from $0$ to $63$) that map onto the 64 printable characters `A–Z`, `a–z`, `0–9`, `+`, and `/`.

A fourth operation concerns Big-Endian versus Little-Endian byte order and Internet checksums. In 1980, computer scientist Danny Cohen borrowed the terms Big-Endian and Little-Endian from Jonathan Swift's *Gulliver's Travels* (where two empires warred over whether to crack a soft-boiled egg at the big or little end) to describe multi-byte memory ordering. Network cables transmit bytes Big-Endian (`12345678h`, most-significant byte `12h` first), whereas x86 and ARM processors store bytes Little-Endian (`78563412h`, least-significant byte `78h` first). When routers verify packet integrity in flight, they use RFC 1071 16-bit one's-complement addition with end-around carry {{cite:knuth1997}}, dividing the 32-bit accumulated sum by $2^{16} = \mathtt{10000h}$ and adding the upper carry quotient right back into the lower 16-bit remainder—turning the 16-bit register into a circular loop where high-byte carries wrap into the low byte, so Big-Endian and Little-Endian machines compute the exact same checksum without byte-swapping.

Finally, just as decimal scientific notation writes $-625$ as $-6.25 \times 10^2$, William Kahan's IEEE-754 floating-point standard {{cite:ieee754_2019,golub1996,parker2019}} writes $-6.25$ in binary scientific notation as $-1.5625 \times 2^2 = -1.1001_2 \times 2^2$, factoring every normal non-zero value into a base-2 exponent and a binary significand with an implicit leading `1.` bit before the binary point:

$$x = (-1)^S \times 2^{E - \text{bias}} \times \left(1 + \frac{M}{2^p}\right)$$

Because every non-zero normalized binary significand begins with `1.`, IEEE-754 omits that hidden bit from storage to gain one extra bit of precision. A 32-bit single-precision float (`binary32`, $p = 23$, $\text{bias} = 127$) packs 1 Sign bit $S$ in `Bit 31`, an 8-bit Biased Exponent $E = e + 127$ in `Bits [30:23]` (reserving $E = 0$ for $\pm 0$ and subnormals and $E = \mathtt{FFh}$ for $\pm\infty$ and `NaN`), and the 23-bit Fractional Mantissa $M$ in `Bits [22:0]`, so cleaving the 32-bit word at $2^{23} = \mathtt{800000h}$ and $2^8 = \mathtt{100h}$ via `{{key:÷R}}` unpacks $M$, $E$, and $S$ onto the stack in two operations (while a 64-bit `binary64` double uses $p = 52$ and an 11-bit exponent with $\text{bias} = 1023$ and $E = \mathtt{7FFh}$ reserved, cleaved in its upper 32-bit half at $2^{20} = \mathtt{100000h}$ and $2^{11} = \mathtt{800h}$).

---

## Combinatorics (PROB), Cryptographic Keyspaces, and the Birthday Collision Paradox

Sizing the state space of a digital register, a network topology, or a cryptographic cipher, and determining the collision threshold of random hashes, rests on the five functions inside the SC-32's `{{key:PROB}}` menu: combinations `{{key:Cn,r}}`, permutations `{{key:Pn,r}}`, factorials `{{key:n!}}` (`{{key:x!}}`), the uniform pseudo-random generator `{{key:RAND}}`, and the PRNG seed command `{{key:SD}}`.

### Ordered Permutations, Unordered Combinations & Pascal's Symmetry

When drawing $r$ items without replacement from $n$ distinct items (such as $n = 16$ hexadecimal digits `0`–`F` or $n = 12$ server racks), the counting law depends on whether the order of selection is significant. When the order of selection matters (such as assigning $r = 4$ distinct hexadecimal nibbles to a 4-stage shift register, or ordering $r = 5$ packet routes out of $n = 12$), there are $n$ choices for the first slot, $n - 1$ for the second, down to $n - r + 1$ for the $r$-th slot, which defines the ordered permutation `{{key:Pn,r}}`:

$$P(n, r) = n(n - 1)\cdots(n - r + 1) = \frac{n!}{(n - r)!}$$

Conversely, when order does not matter (such as choosing any subset of $r = 5$ storage drives out of $n = 12$ for a RAID parity group, or wiring every pair of $r = 2$ routers among $n = 7$ ARPANET nodes), dividing $P(n, r)$ by the $r!$ ways to rearrange the chosen subset yields Blaise Pascal's binomial coefficient `{{key:Cn,r}}`:

$$C(n, r) = \binom{n}{r} = \frac{P(n, r)}{r!} = \frac{n!}{r!\,(n - r)!}$$

### Richard von Mises's Birthday Paradox & Cryptographic Hash Collisions

That ratio between $P(N, k)$ and $N^k$ governs a classic result in probability and cybersecurity: Richard von Mises's Birthday Paradox (1939). When $k$ independent items (people in a room, or random packets in a network) are each assigned one of $N$ equally likely labels (such as $N = 365$ calendar days, or $N = 2^b$ possible values of a $b$-bit hash function), first-order intuition suggests that a collision becomes $50\%$ likely only when $k$ approaches $N/2$.

That estimate is far too large because collisions can occur across any of the $\binom{k}{2} = \frac{k(k-1)}{2}$ distinct pairs among the $k$ items. The exact probability $P_{\text{unique}}$ that all $k$ items receive *distinct* labels is the ordered permutation $P(N, k) = N(N-1)\cdots(N-k+1)$ divided by the $N^k$ total unrestricted assignments, and using the first-order Taylor bound $1 - x \approx e^{-x}$ yields the Gaussian collision law:

$$P(\text{at least one collision}) = 1 - \frac{P(N, k)}{N^k} \approx 1 - \exp\!\left(-\frac{k(k - 1)}{2N}\right)$$

Setting $\exp(-k^2 / 2N) = \frac{1}{2}$ shows that the $50\%$ collision threshold scales not with $N$, but with its square root: $k_{50\%} \approx \sqrt{(2\ln 2)\,N} \approx 1.1774\sqrt{N}$. In computer science, that $\sqrt{N}$ scaling is known as the Birthday Bound: when a $b$-bit hash function or database UUID spans $N = 2^b$ possible values, random collisions become likely after roughly $\sqrt{2^b} = 2^{b/2}$ operations, which is $2^{16} = 65,536$ packets for a 32-bit CRC or $2^{32} \approx 4.29 \times 10^9$ blocks for a 64-bit cipher. Modern cryptographic hashes such as SHA-256 therefore use $b = 256\text{ bits}$, which raises the birthday collision threshold to $2^{128} \approx 3.4 \times 10^{38}$ operations.

---

## 36-Bit Radix Representations, Boolean Masks & Bitwise Arithmetic

Because the four positional radices (`DEC`, `HEX`, `OCT`, `BIN`), modular two's-complement arithmetic ($\mathbb{Z}/2^{36}\mathbb{Z}$), and Euclidean division ($N = Q \cdot D + R$) operate on the same underlying 36-bit integer words across Registers `T, Z, Y, X`, base conversions and bit-field extractions execute directly on the lower two stack registers (`Y` and `X`) without disturbing values staged in `Z` and `T`.

Switching the active radix mode via `{{key:BASE}}` (`{{key:↰}}` + `{{key:×}}`) re-formats all four visible registers on screen without altering their binary contents, while `{{key:÷R}}` (`{{key:↱}}` + `{{key:E}}`) cleaves any word $N$ in Register `Y` at a power-of-two boundary $D = 2^k$ in Register `X` into its right-shifted upper quotient $Q = \lfloor Y / 2^k \rfloor$ in `X` and its masked lower remainder $R = Y \bmod 2^k$ in `Y` (where a single tap of `{{key:x⇄y}}` swaps `R` into `X` and `Q` into `Y`).

{{res:sc32_hex_255:screenshot|Decimal 255 converted in place to hexadecimal FFh on the SC-32 transflective display while preserving all four stack registers.}}

### Radix Modes (DEC, HEX, OCT, BIN) & Direct Hex Entry

Following the classic HP-32SII design, the `{{key:BASE}}` menu (Left Shift `{{key:↰}}` on `{{key:×}}`, Row 5, Column 3) selects the active display and entry radix across all four stack registers:

| Base System | Keystroke | Screen Suffix | Allowed Character Digits | Example Formatted Display |
| :--- | :--- | :---: | :--- | :--- |
| **Decimal** | `{{key:BASE}} {{key:DEC}}` | *(none)* | `0` through `9` | `1042` |
| **Hexadecimal** | `{{key:BASE}} {{key:HEX}}` | `h` | `0` through `9`, `A` through `F` | `412h` |
| **Octal** | `{{key:BASE}} {{key:OCT}}` | `o` | `0` through `7` | `2022o` |
| **Binary** | `{{key:BASE}} {{key:BIN}}` | `b` | `0` and `1` | `10000010010b` |

If Register $X$ holds `255` in Decimal mode, pressing `{{key:BASE}} {{key:HEX}}` re-renders the register as `FFh`, pressing `{{key:BASE}} {{key:OCT}}` shows `377o`, and pressing `{{key:BASE}} {{key:BIN}}` shows all eight asserted bits as `11111111b`.

When Hexadecimal mode (`{{key:HEX}}`) is active, the top row of primary scientific keys across Row 1 maps onto the printed alpha legends $A$ through $F$: `{{key:√x}}` enters $\mathbf{A} = 10_{10}$, `{{key:eˣ}}` enters $\mathbf{B} = 11_{10}$, `{{key:LN}}` enters $\mathbf{C} = 12_{10}$, `{{key:yˣ}}` enters $\mathbf{D} = 13_{10}$, `{{key:1/x}}` enters $\mathbf{E} = 14_{10}$, and `{{key:Σ+}}` enters $\mathbf{F} = 15_{10}$. Entering `0xDEADBEEF` thus uses the top-row sequence `yˣ 1/x √x yˣ eˣ 1/x 1/x Σ+`. In stack tables, hexadecimal literals such as `C0A80A2D` or `1F` are written in compact hex notation for readability; on the keypad in `HEX` mode, enter `A`–`F` using Row 1 (`√x` through `Σ+`). To apply scientific functions such as square root, natural logarithm, or powers to a hexadecimal value, switch back to Decimal mode (`{{key:BASE}} {{key:DEC}}`) first so the top-row keys resume their mathematical roles.

Because the SC-32 preserves all four stack registers across base changes, you can also mix radices in the middle of a calculation without jotting down a single intermediate number. To add a hexadecimal base offset $3\text{A}7_{16}$ to an octal permission mask $452_8$ and read the sum in decimal, enter `3 {{key:√x}} 7 {{key:ENTER}}` ($935_{10}$) in `{{key:HEX}}` mode, switch to `{{key:OCT}}` mode to add `452 {{key:+}}` ($2261_8$), and switch to `{{key:DEC}}` mode to read the combined total $\mathbf{1,201_{10}}$ in Register $X$.

### Euclidean Division (÷R): Flash Memory Pages, IPv4 Octets & Clock Bus Alignment

Applying Euclidean division `{{key:÷R}}` across Registers $Y$ and $X$ while Registers $Z$ and $T$ remain untouched executes byte-address and IPv4 subnet splits directly on the bottom two registers:

* **16-Byte Cache-Line Row & Offset (`12345 ÷R 16`):** For the byte address $12,345 = 771 \times 16 + 9$ (`0x3039`), keying `{{res:sc32_10_computer_science_bases_seq_01:keys}}` in `{{key:DEC}}` mode cleaves at the $2^4 = 16$ bit boundary, placing the 16-byte row quotient $Q = \mathbf{{{res:sc32_10_computer_science_bases_seq_01:value}}}$ in Register $X$ and the intra-row byte remainder $R = \mathbf{9}$ in Register $Y$ (where a single tap of `{{key:x⇄y}}` parks the quotient `771` in Register $Y$ and brings the remainder `9` into Register $X$).
* **256-Byte Flash Page & Offset (`12345 ÷R 256`):** Mapping that same byte address $12,345$ (`0x3039`) onto a SPI NOR flash chip organized into $2^8 = 256\text{-byte}$ programmable pages, keying `12345 {{key:ENTER}} 256 {{key:÷R}}` (followed by `{{key:x⇄y}}` when inspecting the offset in $X$ and page in $Y$) cleaves the word right at Bit 8 into Page $48$ ($\lfloor 12,345 / 256 \rfloor = 48$, upper byte `0x30`) and Offset $57$ ($12,345 \bmod 256 = 57$, lower byte `0x39`), since $48 \times 256 + 57 = 12,345$, while Registers $Z$ and $T$ remain at zero.

That same two-register `{{key:÷R}}` cleavage decomposes IPv4 network addresses in base $256$ ($2^8$) and aligns `/28` and `/24` Classless Inter-Domain Routing (`CIDR`) subnets:

* **Base-256 IPv4 Octet Unpacking (`3232235777` $\to$ `192.168.1.1`):** An unsigned 32-bit IPv4 socket address such as `3232235777` (`0xC0A80101`) is a four-digit integer written in base $256$. Keying `3232235777 {{key:ENTER}} 256 {{key:÷R}}` in `{{key:DEC}}` mode strips off the lowest 8-bit octet `1` into Register $Y$ and leaves the upper 24-bit prefix `12625921` in Register $X$. Repeating `256 {{key:÷R}}` peels off the third octet `1` into $Y$ (with `49320` in $X$), and a third `256 {{key:÷R}}` splits the remaining 16-bit prefix into the first octet `192` in Register $X$ and the second octet `168` in Register $Y$, which displays `192.168.1.1` across the four stack registers (`1, 1, 168, 192`).
* **Aligning a `/28` VLAN Interface (`205` $\to$ Block `192`, Offset `13`):** On a `/28` office subnet (`255.255.255.240`, where $32 - 28 = 4$ host bits give a block stride of $2^4 = 16$ addresses), dividing host octet `205` by `16` via `{{key:÷R}}` places the block index `12` in Register $X$ and the host offset `13` in Register $Y$ ($205 = 12 \times 16 + 13$, with $Z$ and $T$ at zero), and multiplying Register $X$ back by `16` zeroes out the low 4 host bits: keying `{{res:sc32_10_computer_science_bases_seq_03:keys}}` snaps directly to the aligned `/28` network base ID `{{res:sc32_10_computer_science_bases_seq_03:value}}` (`12 × 16 = 192`).

For a packed 32-bit `/24` workstation address `192.168.10.45` (`C0A80A2Dh`, where `192` $= \mathtt{C0h}$, `168` $= \mathtt{A8h}$, `10` $= \mathtt{0Ah}$, and `45` $= \mathtt{2Dh}$), working in `{{key:HEX}}` mode slices at the 8-bit host boundary ($2^8 = \text{100h}$) while Registers $Z$ and $T$ rest at `0h`:

* **Align the `/24` Network Base (`192.168.10.0`):** Cleaving `C0A80A2Dh` by `100h` separates the 24-bit network prefix `C0A80Ah` in Register $X$ from the 8-bit host ID `2Dh` ($45_{10}$) in Register $Y$, and multiplying Register $X$ back by `100h` zeros out the host byte. Keying `{{res:sc32_10_computer_science_bases_seq_04:keys}}` produces the aligned `/24` network base `{{res:sc32_10_computer_science_bases_seq_04:value}}` (`192.168.10.0`).
* **Isolate the Inverted Host Wildcard Mask (`0.0.0.255`):** Subtracting the `/24` netmask `FFFFFF00h` from the 32-bit all-ones broadcast word `FFFFFFFFh` flips every network bit to `0` and every host bit to `1`. Keying `{{res:sc32_10_computer_science_bases_seq_05:keys}}` isolates the 8-bit host wildcard mask `{{res:sc32_10_computer_science_bases_seq_05:value}}`.
* **Populate the Directed `/24` Broadcast Address (`192.168.10.255`):** Because the aligned network base (`C0A80A00h`) and the host wildcard (`000000FFh`) occupy non-overlapping bit lanes, adding them performs an exact carry-free bitwise `OR` across the bottom 8 bits. Keying `{{res:sc32_10_computer_science_bases_seq_06:keys}}` delivers the directed `/24` broadcast address `{{res:sc32_10_computer_science_bases_seq_06:value}}`.

### 36-Bit Two's Complement Odometer Seams & Hardware Bit-Fields

The two boundary seams of the 36-bit two's-complement word (`7FFFFFFFFh` and `0 - 1`) appear directly in `{{key:HEX}}` mode on Registers $Y$ and $X$ {{cite:parker2019}}:

* **Signed 36-Bit Overflow Seam (`7FFFFFFFFh + 1 → 800000000h`):** At the highest positive 36-bit integer `7FFFFFFFFh` ($+2^{35} - 1 = +34,359,738,367_{10}$), Bit 35 is `0` while all 35 lower magnitude bits (Bits 34–0) are `1`. Adding `1` propagates a ripple carry through all 35 lower bits into Bit 35 (`800000000h`), triggering signed two's-complement overflow (`V = 1`): keying `{{res:sc32_10_computer_science_bases_seq_33:keys}}` advances across the 36-bit boundary to `{{res:sc32_10_computer_science_bases_seq_33:value}}` (which represents $-2^{35} = -34,359,738,368_{10}$ in a wrapped 36-bit register, or $+34,359,738,368_{10} = \mathtt{800000000h}$ in the SC-32's unclipped 64-bit accumulator).
* **Zero Underflow Seam & Sign Extension (`0 - 1 → -1`):** Decrementing the register by one from `0` borrows across every bit position simultaneously and sets all two's-complement bits ON (`FFFFFFFFFh` masked to 36 bits, or `FFFFFFFFFFFFFFFFh` with hardware *sign extension* replicating Bit 35 across Bits 63–36 of the 64-bit register): keying `{{res:sc32_10_computer_science_bases_seq_34:keys}}` produces `{{res:sc32_10_computer_science_bases_seq_34:value}}` ($-1_{10}$).

Every bit-field shift and mask operation maps directly to a power of two $M = 2^k$ {{cite:shannon1938}}:

| Bit-Field / Masking Operation | Mathematical Equivalent ($M = 2^k$) | SC-32 RPN Keystrokes (`HEX` / `DEC`) | Result Location |
| :--- | :---: | :--- | :--- |
| **Left Shift ($X \ll k$)** | $X \times 2^k$ | `X {{key:ENTER}} M {{key:×}}` | Shifted word in **`X`** |
| **Right Shift ($X \gg k$)** | $\lfloor X / 2^k \rfloor$ | `X {{key:ENTER}} M {{key:÷R}}` | Upper bits in **`X`** |
| **Low-Bit Mask ($X \ \& \ (2^k - 1)$)** | $X \bmod 2^k$ | `X {{key:ENTER}} M {{key:÷R}} {{key:x⇄y}}` | Low $k$ bits in **`X`** |
| **High-Bit Alignment ($X \ \& \ \sim(2^k - 1)$)** | $\lfloor X / 2^k \rfloor \times 2^k$ | `X {{key:ENTER}} M {{key:÷R}} M {{key:×}}` | Aligned base in **`X`** |
| **Set Disjoint Bit $k$** | $X + 2^k$ | `X {{key:ENTER}} M {{key:+}}` | Updated word in **`X`** |
| **Clear Set Bit $k$** | $X - 2^k$ | `X {{key:ENTER}} M {{key:-}}` | Updated word in **`X`** |
| **32-Bit Unsigned Complement** | $\text{FFFFFFFF}_{16} - X$ | `FFFFFFFF {{key:ENTER}} X {{key:-}}` | Inverted mask in **`X`** |

*(For right bit-shifts in `{{key:DEC}}` mode, `{{key:÷R}}` is preferred over `{{key:÷}}` because `{{key:÷}}` retains fractional decimal digits in Decimal mode, whereas `{{key:÷R}}` always truncates to the integer quotient $\lfloor X / 2^k \rfloor$ in every base.)*

Memory-mapped microcontroller peripherals pack independent hardware control lines into a single register word so firmware can toggle GPIO pins, isolate telemetry fault masks, and extract ADC bit-fields via positional masks $2^k$ without disturbing neighboring lines:

* **Asserting an Unset GPIO Direction Pin (`GPIO_DIR | (1 << 5)`):** When a 32-bit GPIO direction register holds `0x00001804`—meaning Pins 2 ($2^2 = \text{4h}$), 11 ($2^{11} = \text{800h}$), and 12 ($2^{12} = \text{1000h}$) are already configured as outputs while Pin 5 is currently an input (`0`)—adding the unasserted Bit 5 positional weight $2^5 = 32_{10} = \text{20h}$ in `{{key:HEX}}` mode performs a carry-free bitwise `OR`: keying `{{res:sc32_10_computer_science_bases_seq_11:keys}}` asserts Pin 5 to produce `{{res:sc32_10_computer_science_bases_seq_11:value}}` (`1824h`).
* **Clearing and Re-Asserting an Active Heartbeat Pin (`PORT & ~(1 << 2)`):** If a port output register holds `0x00000017` ($0001\,0111_2$) with an active heartbeat line on Bit 2 ($2^2 = \text{4h}$), subtracting the bit weight in `{{key:HEX}}` mode performs a borrow-free `AND NOT`: keying `{{res:sc32_10_computer_science_bases_seq_13:keys}}` clears Bit 2 to `{{res:sc32_10_computer_science_bases_seq_13:value}}`, and adding `4h` back via `{{res:sc32_10_computer_science_bases_seq_14:keys}}` (or `{{key:LASTX}} {{key:+}}`) re-asserts the pin to `{{res:sc32_10_computer_science_bases_seq_14:value}}` without disturbing neighboring pins.
* **Isolating Tripped Telemetry Fault Flags (`Status ^ Baseline`):** Whenever a baseline register's asserted bits are a subset of an active status word, borrow-free subtraction acts as an exact bitwise `XOR` difference mask. Comparing a spacecraft downlink status word `0x5F5A` against its nominal baseline `0x5A50` via `{{res:sc32_10_computer_science_bases_seq_36:keys}}` strips away the nominal bits to isolate the newly tripped fault mask `{{res:sc32_10_computer_science_bases_seq_36:value}}`, which renders as $\mathbf{10100001010\text{b}}$ in `{{key:BIN}}` with a Hamming weight of $4\text{ fault bits}$ at positions 1, 3, 8, and 10.
* **Extracting an Interior Multi-Bit Field (`Bits [7:4]` of `0x3C6A`):** For the 16-bit word `0x3C6A`, when an ADC control register packs a 4-bit oversampling selector in Bits [7:4] (`6h`), extracting that interior field combines a modulo mask ($\bmod 2^8 = \text{100h}$) with an integer right-shift ($\div 2^4 = \text{10h}$):

$$\text{Bits } [7:4] = \left\lfloor \frac{\mathtt{3C6Ah} \bmod 2^8}{2^4} \right\rfloor = \left\lfloor \frac{\mathtt{6Ah}}{\mathtt{10h}} \right\rfloor = \mathtt{6h}$$

  First, cleaving at $2^8 = \text{100h}$ via `{{res:sc32_10_computer_science_bases_seq_15:keys}}` masks off the upper configuration byte (`3Ch`) and brings the lower 8-bit byte `{{res:sc32_10_computer_science_bases_seq_15:value}}` into Register $X$; second, right-shifting by 4 bits ($\div 2^4 = \text{10h}$) via `{{res:sc32_10_computer_science_bases_seq_16:keys}}` discards the bottom nibble (`Ah`) so Bits [7:4] land right-justified at Bit 0 as `{{res:sc32_10_computer_science_bases_seq_16:value}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3C6A {{key:ENTER}}` | `0h` | `0h` | `3C6Ah` | `3C6Ah` | Stage 16-bit ADC register word `3C6Ah` |
| `100 {{key:÷R}}` | `0h` | `0h` | `6Ah` | `3Ch` | Split upper byte `3Ch` into X and lower byte `6Ah` into Y |
| `{{key:x⇄y}}` | `0h` | `0h` | `3Ch` | `6Ah` | Swap lower byte `6Ah` (Bits [7:0]) into Register X |
| `10 {{key:÷}}` | `0h` | `0h` | `3Ch` | `6h` | Shift right by 4 bits (`÷ 10h`) to isolate Bits [7:4] = `6h` |

### Packing RGB565 Pixels, Slicing Base64 Sextets & Reversing Endianness

Executing `RGB565` pixel packing $(R_5 \times 2^{11}) + (G_6 \times 2^5) + B_5$ for 5-bit Red (`1Fh` $= 31/31$), 6-bit Green (`15h` $= 21/63$), and 5-bit Blue (`06h` $= 6/31$) in `{{key:HEX}}` mode shifts and merges the three non-overlapping bit lanes across Registers $Y$ and $X$:

* **Shift Red into `Bits [15:11]` (`× 800h`):** Multiplying Red (`1Fh`) by $2^{11} = \text{800h}$ left-shifts those 5 bits across the Green and Blue lanes: keying `{{res:sc32_10_computer_science_bases_seq_19:keys}}` places `{{res:sc32_10_computer_science_bases_seq_19:value}}` in Register $X$.
* **Shift Green into `Bits [10:5]` (`× 20h`) and Merge:** Multiplying Green (`15h`) by $2^5 = \text{20h}$ via `{{res:sc32_10_computer_science_bases_seq_20:keys}}` left-shifts the 6 green bits into Bits [10:5] as `{{res:sc32_10_computer_science_bases_seq_20:value}}` while `F800h` waits in Register $Y$.
* **Combine All Three Lanes (`FAA6h`):** Merging Red and Green (`FAA0h`) and adding the unshifted 5-bit Blue channel (`06h`) in Bits [4:0] via `{{res:sc32_10_computer_science_bases_seq_21:keys}}` completes the packed 16-bit framebuffer pixel `{{res:sc32_10_computer_science_bases_seq_21:value}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1F {{key:ENTER}}` | `0h` | `0h` | `1Fh` | `1Fh` | Stage 5-bit Red channel `1Fh` ($31_{10}$) |
| `800 {{key:×}}` | `0h` | `0h` | `0h` | `F800h` | Shift Red left 11 bits (`× 800h`) into Bits [15:11] |
| `15 {{key:ENTER}}` | `0h` | `F800h` | `15h` | `15h` | Stage 6-bit Green channel `15h` ($21_{10}$); Red lifts to Z |
| `20 {{key:×}}` | `0h` | `0h` | `F800h` | `2A0h` | Shift Green left 5 bits (`× 20h`) into Bits [10:5] |
| `{{key:+}}` | `0h` | `0h` | `0h` | `FAA0h` | Combine shifted Red and Green channels (`FAA0h`) |
| `6 {{key:+}}` | `0h` | `0h` | `0h` | `FAA6h` | Add 5-bit Blue channel `06h` for packed `RGB565` word `FAA6h` |

Conversely, given a packed 16-bit RGB565 pixel `0xF38E` in `{{key:HEX}}` mode, keying `F38E {{key:ENTER}} 800 {{key:÷R}} {{key:x⇄y}} 20 {{key:÷R}}` unpacks all three color channels onto the visible stack in one pass: Red in Register $Z$ (`1Eh` $= 30_{10}$), Green in Register $X$ (`1Ch` $= 28_{10}$), and Blue in Register $Y$ (`Eh` $= 14_{10}$).

Similarly, slicing the 24-bit ASCII word `"Man"` (`'M' = 4Dh`, `'a' = 61h`, `'n' = 6Eh` $\implies \mathtt{4D616Eh}$) into its four 6-bit Base64 indices cleaves at $2^{18} = \text{40000h}$, $2^{12} = \text{1000h}$, and $2^6 = \text{40h}$ in `{{key:HEX}}` mode:

* **Sextet 1 (`Bits [23:18]` $\to$ `'T'`):** Right-shifting by 18 bits (`÷ 40000h`) via `{{res:sc32_10_computer_science_bases_seq_29:keys}}` extracts `{{res:sc32_10_computer_science_bases_seq_29:value}}` ($19_{10} \implies$ Base64 `'T'`).
* **Sextet 2 (`Bits [17:12]` $\to$ `'W'`):** Masking the 18-bit remainder and right-shifting by 12 bits (`÷ 1000h`) via `{{res:sc32_10_computer_science_bases_seq_30:keys}}` isolates `{{res:sc32_10_computer_science_bases_seq_30:value}}` ($22_{10} \implies$ `'W'`).
* **Sextet 3 (`Bits [11:6]` $\to$ `'F'`):** Cleaving the 12-bit remainder at 6 bits (`÷ 40h`) via `{{res:sc32_10_computer_science_bases_seq_31:keys}}` extracts `{{res:sc32_10_computer_science_bases_seq_31:value}}` ($5_{10} \implies$ `'F'`).
* **Sextet 4 (`Bits [5:0]` $\to$ `'u'`):** Masking the final 6-bit remainder via `{{res:sc32_10_computer_science_bases_seq_32:keys}}` leaves `{{res:sc32_10_computer_science_bases_seq_32:value}}` ($46_{10} \implies$ `'u'`), spelling out `TWFu`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `4D616E {{key:ENTER}} 40000 {{key:÷}}` | `0h` | `0h` | `0h` | **`13h`** | Sextet 1: `4D616Eh >> 18 = 13h` ($19_{10} \implies \mathbf{T}$) |
| `4D616E {{key:ENTER}} 40000 {{key:÷R}} {{key:x⇄y}} 1000 {{key:÷}}` | `13h` | `13h` | `13h` | **`16h`** | Sextet 2: remainder `>> 12 = 16h` ($22_{10} \implies \mathbf{W}$) |
| `4D616E {{key:ENTER}} 1000 {{key:÷R}} {{key:x⇄y}} 40 {{key:÷}}` | `16h` | `16h` | `4D6h` | **`5h`** | Sextet 3: remainder `>> 6 = 5h` ($5_{10} \implies \mathbf{F}$) |
| `4D616E {{key:ENTER}} 40 {{key:÷R}} {{key:x⇄y}}` | `4D6h` | `5h` | `13585h` | **`2Eh`** | Sextet 4: lower 6-bit remainder = `2Eh` ($46_{10} \implies \mathbf{u}$) |

*(Single-Entry `÷R` Cascade: Chaining `4D616E {{key:ENTER}} 40000 {{key:÷R}} {{key:x⇄y}} 1000 {{key:÷R}} {{key:x⇄y}} 40 {{key:÷R}}` unpacks all four Base64 indices across the four stack registers—`13h` in $T$, `16h` in $Z$, `2Eh` in $Y$, and `5h` in $X$—with `4D616E` keyed only once.)*

Reversing the 32-bit Big-Endian network header `0x12345678` into its Little-Endian x86/ARM memory representation `0x78563412` (`BSWAP` / `REV`) in `{{key:HEX}}` mode folds each shifted byte into a running sum on Register $X$ across Registers $Y$ and $X$ while Registers $Z$ and $T$ stay at `0h`:

* **Promote Byte 0 (`78h` $\ll 24$) into Byte 3:** Multiplying `78h` by $2^{24} = \text{1000000h}$ via `{{res:sc32_10_computer_science_bases_seq_41:keys}}` yields `{{res:sc32_10_computer_science_bases_seq_41:value}}` (`78000000h`).
* **Promote Byte 1 (`56h` $\ll 16$) into Byte 2:** Multiplying `56h` by $2^{16} = \text{10000h}$ via `{{res:sc32_10_computer_science_bases_seq_42:keys}}` positions `{{res:sc32_10_computer_science_bases_seq_42:value}}` (`560000h`) and merges them into `78560000h`.
* **Promote Byte 2 (`34h` $\ll 8$) into Byte 1:** Multiplying `34h` by $2^8 = \text{100h}$ via `{{res:sc32_10_computer_science_bases_seq_43:keys}}` places `{{res:sc32_10_computer_science_bases_seq_43:value}}` (`3400h`) into Byte 1 (`78563400h`).
* **Demote Byte 3 (`12h` $\gg 24$) into Byte 0:** Right-shifting the original most-significant byte via `{{res:sc32_10_computer_science_bases_seq_44:keys}}` isolates `{{res:sc32_10_computer_science_bases_seq_44:value}}` (`12h`), so adding `12h` completes the byte-swapped Little-Endian word `78563412h`.

### RFC 1071 Checksums, Circular Rotations (`ROL`), UART Dividers & IEEE-754 Unpacking

Executing the RFC 1071 16-bit one's-complement end-around carry checksum on an IPv4 header whose ten 16-bit words sum to `2653Dh` in `{{key:HEX}}` mode cleaves at the 16-bit boundary $2^{16} = \text{10000h}$ via `2653D {{key:ENTER}} 10000 {{key:÷R}}`, separating the upper carry quotient `2h` in Register $X$ from the lower 16-bit sum `653Dh` in Register $Y$ (with $Z = T = \text{0h}$). Pressing `{{key:+}}` folds that end-around carry directly into Bit 0 (`653Fh`), and subtracting from the all-ones 16-bit mask `FFFFh` via `FFFF {{key:x⇄y}} {{key:-}}` inverts every bit to form the one's-complement wire checksum `9AC0h` ($39,616_{10}$ in `{{key:DEC}}`).

In cryptographic block ciphers and cyclic redundancy checks, that same two-register end-around carry implements a circular 1-bit left rotation (`ROL 1`) across an 8-bit register boundary ($2^8 = \text{100h}$), where the bit shifted out of Bit 7 wraps around to enter Bit 0 (`0x85` $= 10000101_2 \implies 00001011_2 = \text{0Bh}$):

* **Left-Shift All 8 Bits (`× 2`):** Doubling `85h` via `{{res:sc32_10_computer_science_bases_seq_50:keys}}` shifts the byte left by one position to `{{res:sc32_10_computer_science_bases_seq_50:value}}` (`10Ah`), pushing the old MSB into Bit 8.
* **Cleave at the 8-Bit Boundary (`÷R 100h`):** Dividing by `100h` via `{{res:sc32_10_computer_science_bases_seq_51:keys}}` separates the low 8-bit remainder (`Ah` in Register $Y$) from the Bit 8 carry (`{{res:sc32_10_computer_science_bases_seq_51:value}}` $= \text{1h}$ in Register $X$).
* **Fold the Carry into Bit 0 (`+`):** Adding the carry back into the low byte via `{{res:sc32_10_computer_science_bases_seq_52:keys}}` completes the circularly rotated byte `{{res:sc32_10_computer_science_bases_seq_52:value}}` (`Bh`).

When configuring an asynchronous serial `UART` transceiver from a $f_{\text{clk}} = 150.0\text{ MHz}$ system bus at $115,200\text{ baud}$ with $8\times$ oversampling, hardware fractional baud-rate generators split the ideal divisor $\text{Divider} = \frac{150,000,000}{8 \times 115,200} \approx 162.760417$ into a 16-bit integer mantissa register (`IBRD`) and a 6-bit fixed-point sixty-fourths register (`FBRD` $= \lfloor 64 \times \text{FP} + 0.5 \rfloor$). Switching to `{{key:DEC}}` mode and keying `{{res:sc32_10_computer_science_bases_seq_40:keys}}` yields the exact divisor `{{res:sc32_10_computer_science_bases_seq_40:value}}` in Register $X$. Duplicating that divisor and extracting `{{key:IP}}` isolates `IBRD = 162` while swapping to take the fractional part `{{key:FP}}` isolates $0.76041667$; multiplying by $64$ and rounding via `{{key:RND}}` converts $48.6667$ to `FBRD = 49` ($49/64 = 0.765625$) in Register $X$ right beside `IBRD = 162` in Register $Y$.

To unpack the 32-bit IEEE-754 single-precision (`binary32`) word `0xC0C80000`—encoding $-6.25_{10} = -110.01_2 = (-1)^1 \times 2^2 \times 1.1001_2$ as $(-1)^S \times 2^{E - 127} \times (1 + M / 2^{23})$—chain two `{{key:÷R}}` cleavages in `{{key:HEX}}` mode at the 23-bit mantissa boundary ($2^{23} = \text{800000h}$) and the 8-bit exponent boundary ($2^8 = \text{100h}$). This places the 23-bit significand `480000h` ($4,718,592 / 2^{23} = 0.5625$, or $1.5625$ with the hidden leading `1.`) in Register $Z$, the biased exponent `81h` ($129_{10}$, so $e = 129 - 127 = 2$) in Register $Y$, and the sign bit `1h` in Register $X$ to verify $(-1)^1 \times 2^2 \times 1.5625 = -6.25$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `C0C80000 {{key:ENTER}}` | `0h` | `0h` | `C0C80000h` | `C0C80000h` | Stage 32-bit IEEE-754 float word `C0C80000h` |
| `800000 {{key:÷R}}` | `0h` | `0h` | `480000h` | `181h` | Cleave at Bit 23: mantissa `480000h` in Y, upper 9 bits `181h` in X |
| `100 {{key:÷R}}` | `0h` | `480000h` | `81h` | `1h` | Cleave at Bit 8: Sign `1h` in X, Exponent `81h` in Y, Mantissa in Z |
| `{{key:BASE}} {{key:DEC}}` | 0 | 4718592 | 129 | 1 | Switch to Decimal: $S = 1$, $E = 129$, $M = 4,718,592$ |
| `{{key:x⇄y}} 127 {{key:-}}` | 4718592 | 4718592 | 1 | 2 | Subtract bias $127$ to reveal true binary exponent $e = 2$ |

Similarly, for the upper 32-bit word `0xC02AC000` of $-13.375_{10}$ (`0xC02AC00000000000`, `binary64`) in `{{key:HEX}}` mode, chaining `C02AC000 {{key:ENTER}} 100000 {{key:÷R}} 800 {{key:÷R}}` cleaves at $2^{20} = \text{100000h}$ and $2^{11} = \text{800h}$ to leave Sign $S = \mathbf{1}$ in $X$, Biased Exponent $E = \mathbf{\text{402h}}$ ($1026_{10}$, $e = 1026 - 1023 = \mathbf{3}$) in $Y$, and significand `AC000h` ($704,512 / 2^{20} = 0.671875$) in $Z$ for $(-1)^1 \times 2^3 \times 1.671875 = \mathbf{-13.375}$.

### Combinatorics (PROB) & Birthday Paradox Collision Probability

In `{{key:DEC}}` mode, the `{{key:PROB}}` menu (Right Shift `{{key:↱}}` above `{{key:eˣ}}`) evaluates discrete state spaces on the stack. For a 12-drive array selecting $5$ drives for an unordered RAID group ($C(12, 5)$) versus an ordered failover chain ($P(12, 5)$), `12 {{key:ENTER}} 5 {{key:PROB}} {{key:Cn,r}}` counts $\mathbf{792}$ subsets, while `12 {{key:ENTER}} 5 {{key:PROB}} {{key:Pn,r}}` spans $\mathbf{95,040}$ sequences:

* **4-Stage Non-Repeating Hex Shift Register ($P(16, 4)$):** Assigning an ordered 4-nibble sequence without repetition from $16$ hexadecimal digits via `{{res:sc32_10_computer_science_bases_seq_47:keys}}` yields `{{res:sc32_10_computer_science_bases_seq_47:value}}` distinct register states.
* **7-Router Full-Mesh Point-to-Point Links ($C(7, 2)$):** Wiring every unordered pair of routers across a 7-node network via `{{res:sc32_10_computer_science_bases_seq_48:keys}}` requires `{{res:sc32_10_computer_science_bases_seq_48:value}}` cables.
* **15-Packet Priority Queue Permutations ($15!$):** Ordering an entire 15-packet queue via `{{res:sc32_10_computer_science_bases_seq_49:keys}}` spans `{{res:sc32_10_computer_science_bases_seq_49:value}}` schedules ($12! = 479,001,600$ for $12$ items).

Evaluating Richard von Mises's Birthday Collision probability $1 - P(365, k)/365^k$ across $N = 365$ days for $k = 23$ people ($\binom{23}{2} = 253\text{ pairs}$) via `365 {{key:ENTER}} 23 {{key:PROB}} {{key:Pn,r}}` gives $4.220082 \times 10^{58}$ collision-free assignments; dividing by `365 {{key:ENTER}} 23 {{key:yˣ}} {{key:÷}}` yields $P_{\text{unique}} = \mathbf{0.492703}$, and `1 {{key:x⇄y}} {{key:-}}` confirms a shared-birthday probability of $\mathbf{0.507297}$ ($50.73\%$).
