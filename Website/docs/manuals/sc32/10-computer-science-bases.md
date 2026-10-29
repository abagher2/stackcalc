---
title: "Chapter 10: Ones, Zeros, and the 36-Bit Machine: From Leibniz and Shannon to Modern Computing | Thinking in the Stack (SC-32)"
description: "36-bit two's complement integer architecture, base conversions (HEX, DEC, OCT, BIN), integer division & remainder bit-field extraction (÷R), CIDR IPv4 subnetting, RGB565 packing, combinatorics, and IEEE-754 representation on the StackCalc SC-32."
---

# Chapter 10: Ones, Zeros, and the 36-Bit Machine: From Leibniz and Shannon to Modern Computing

## Leibniz's Medallion, Boole's Logic & Claude Shannon's 1937 Master's Thesis

### From Leibniz's Binary Medallion to Shannon's Relay Basement

In the summer of 1937, a twenty-one-year-old master's student named **Claude Elwood Shannon** stood in the basement of MIT's electrical engineering building, surrounded by the clatter of brass gears and electromechanical telephone relays. His graduate assignment was maintaining Vannevar Bush's Differential Analyzer—a room-filling hundred-ton mechanical analog computer whose spinning steel shafts, torque amplifiers, and wheel-and-disc integrators solved differential equations through physical rotation.

Every time a physicist or ballistician brought a new differential equation to the basement laboratory, Shannon had to spend hours configuring two distinct worlds: the continuous mechanical shafts of the analyzer, and a maze of clicking telephone relay circuits that controlled its switches, clutches, and safety interlocks.

As Shannon wired those relays in series and in parallel, a startling memory surfaced from an undergraduate philosophy class he had taken at the University of Michigan. Eighty-three years earlier, in 1854, a self-taught English mathematician named **George Boole**—the son of a struggling Lincoln shoemaker—had published *An Investigation of the Laws of Thought*. Boole had dared to ask whether human reasoning could be written as algebra. If a statement was completely true, Boole assigned it the number $1$; if it was false, he assigned it the number $0$. Combining two statements with the word **AND** behaved like multiplication ($1 \times 1 = 1$, while $1 \times 0 = 0$); combining them with **OR** behaved like a saturating addition ($1 + 0 = 1$); and negating a statement with **NOT** flipped $1$ to $0$ and $0$ to $1$.

Boole himself had followed an even older trail. In 1703, the German polymath **Gottfried Wilhelm Leibniz** had presented a paper to the Royal Academy of Sciences in Paris titled *Explication de l'Arithmétique Binaire*. Leibniz marveled that every integer in the universe could be constructed using only two symbols—$1$ and $0$—and sketched a commemorative medallion showing light ($1$) emerging from the void ($0$) under the Latin motto *Omnibus ex nihilo ducendis sufficit unum* ("To derive everything from nothing, one suffices"). Yet for more than two centuries after Leibniz and eight decades after Boole, binary numbers and Boolean logic were regarded as philosophical curiosities—elegant parlor mathematics with no practical connection to machinery.

Staring at the racks of telephone relays in the MIT basement, young Claude Shannon saw the bridge that everyone else had missed:

- **Two switches wired in series** allow electrical current to pass only if Switch A is closed **AND** Switch B is closed ($A \cdot B$).
- **Two switches wired in parallel** allow current to pass if Switch A is closed **OR** Switch B is closed ($A + B$).
- **A normally closed relay contact** that opens when its electromagnet is energized acts as a physical **NOT** inverter ($\overline{A}$).

Every open or closed relay on a telephone switchboard was a physical embodiment of George Boole's two-valued algebra—and because Leibniz had shown that any number can be written in base-2 binary digits, circuits built from those same logical switches could add, subtract, compare, and store numbers at the speed of electricity!

In his 1937 MIT master's thesis—published in 1938 {{cite:shannon1938}} and later hailed by cognitive scientist Howard Gardner as "possibly the most important, and also the most famous, master's thesis of the century"—Shannon proved that any logical decision or arithmetic operation can be synthesized from binary switching gates. Even the fundamental unit of digital information—the **bit** (*binary digit*)—was coined by Shannon's Bell Labs colleague John Tukey and immortalized in Shannon's 1948 landmark paper *A Mathematical Theory of Communication*. Every microprocessor, memory cell, router, and spacecraft guidance computer built over the past nine decades traces its lineage back to that summer in 1937 when logic and electricity became one.

### How Three Logic Gates Build Arithmetic Out of Pure Reason

To appreciate why Shannon's discovery was so revolutionary—and why computer-science students begin by studying truth tables—examine how a silicon chip adds two binary bits $A$ and $B$ without knowing anything about arithmetic. When adding $A + B$ in base 2, the circuit produces a two-bit answer consisting of a **Carry** bit (in the twos column, $2^1$) and a **Sum** bit (in the ones column, $2^0$):

- If $A = 0$ and $B = 0$, the result is $00_2$ ($\text{Carry} = 0,\; \text{Sum} = 0$).
- If $A = 0$ and $B = 1$, or $A = 1$ and $B = 0$, the result is $01_2$ ($\text{Carry} = 0,\; \text{Sum} = 1$).
- If $A = 1$ and $B = 1$, the binary sum is $1 + 1 = 2_{10} = 10_2$ ($\text{Carry} = 1,\; \text{Sum} = 0$).

Look closely at those two output columns:

| Input Bit $A$ | Input Bit $B$ | Carry Bit ($2^1$ Column) | Sum Bit ($2^0$ Column) | Logical Meaning |
| :---: | :---: | :---: | :---: | :--- |
| `0` | `0` | `0` | `0` | Neither switch closed $\implies 0$ |
| `0` | `1` | `0` | `1` | Exactly one switch closed $\implies 1$ |
| `1` | `0` | `0` | `1` | Exactly one switch closed $\implies 1$ |
| `1` | `1` | `1` | `0` | Both closed $\implies$ Carry `1`, Sum wraps to `0` |

The **Carry** column is `1` *if and only if* both $A$ **AND** $B$ are `1`—which is a single Boolean `AND` gate. Meanwhile, the **Sum** column is `1` *if and only if* $A$ or $B$ is `1`, **but not both**—the exact truth table of the **Exclusive-OR (`XOR`, $\oplus$)** gate. Wire one `XOR` gate and one `AND` gate side by side across the same two input wires, and you have built a physical **Half-Adder**: a circuit made of pure yes/no logic switches that performs exact arithmetic. Chain thirty-six of those adders together so each column's carry feeds into the next column to its left, and a silent sliver of silicon can add ten-digit integers in a single clock cycle.

---

## Speaking in Nibbles, Octets & The Classic 36-Bit Word

### Why Humans Count in Tens, Silicon Counts in Twos & Programmers Read in Sixteens

Why does the number `255` look completely different when written as `255` in decimal, `11111111b` in binary, `377o` in octal, and `FFh` in hexadecimal—even though all four strings name the identical quantity of objects?

When humans learned to count in antiquity, we naturally bundled objects in groups of ten (**Decimal**, base $b = 10$) because we carry ten fingers on our hands. When we write the decimal number $1,042_{10}$, we are secretly writing a polynomial in powers of $10$ from the inside out:

$$1,042_{10} = 1 \times 10^3 + 0 \times 10^2 + 4 \times 10^1 + 2 \times 10^0 = ((1 \times 10 + 0) \times 10 + 4) \times 10 + 2$$

Yet the choice of $10$ is an accident of human anatomy. An electronic transistor does not have ten fingers. Trying to build a circuit that distinguishes ten different voltage levels ($0\text{ V}, 0.5\text{ V}, 1.0\text{ V}, \dots, 4.5\text{ V}$) is an engineering nightmare: a tiny thermal drift or static spark turns a $3$ into a $4$. Instead, silicon circuits use only two states—fully OFF ($0$) and fully ON ($1$). In **Binary** (base $b = 2$), each column as you move from right to left represents the next doubling power of two ($2^0 = 1,\; 2^1 = 2,\; 2^2 = 4,\; 2^3 = 8,\; 2^4 = 16,\; \dots$):

$$1042_{10} = 1024 + 16 + 2 = 1 \times 2^{10} + 1 \times 2^4 + 1 \times 2^1 = 10000010010_2$$

Binary is natural for silicon switches, but exhausting for the human eye. Stare at a 36-bit binary word like `000011000000101010000000101000101101b` for ten seconds, and your working memory blurs. Remember George Miller's discovery from Chapter 2: human working memory can comfortably hold only four to seven chunks at a time, never thirty-six individual ones and zeros.

How do computer scientists compress long strings of bits into compact human-readable chunks without doing tedious division by $10$? By choosing number bases that are **exact powers of two**:

1. **Octal (`OCT`, Base $b = 8 = 2^3$):** Because $8 = 2^3$, every single octal digit (`0` through `7`) corresponds to an exact **3-bit triad** (`000` through `111`). To convert a binary number into octal in your head, you never divide—you slice the binary string into 3-bit groups from right to left and read off each triad.
2. **Hexadecimal (`HEX`, Base $b = 16 = 2^4$):** Because $16 = 2^4$, every single hexadecimal digit corresponds to an exact **4-bit "nibble"** (`0000` through `1111`). For values from $0$ to $9$, hexadecimal uses the familiar decimal digits `0`–`9`; for the remaining six 4-bit patterns ($10$ through $15$), it borrows the first six letters of the alphabet (`A` $= 10$, `B` $= 11$, `C` $= 12$, `D` $= 13$, `E` $= 14$, and `F` $= 15$). Two hexadecimal digits side by side (`00h` through `FFh`) pack an exact **8-bit byte** (an **octet**, $2^8 = 256$ values from $0$ to $255$).

| Decimal (`DEC`) | 4-Bit Binary Nibble (`BIN`) | Octal (`OCT`) | Hexadecimal (`HEX`) | Positional Power Decomposition |
| :---: | :---: | :---: | :---: | :--- |
| `0` | `0000b` | `0o` | `0h` | $0$ |
| `5` | `0101b` | `5o` | `5h` | $4 + 1 = 2^2 + 2^0$ |
| `7` | `0111b` | `7o` | `7h` | $4 + 2 + 1 = 2^3 - 1$ |
| `8` | `1000b` | `10o` | `8h` | $2^3$ (one full octal triad carry) |
| `10` | `1010b` | `12o` | `Ah` | $8 + 2 = 2^3 + 2^1$ |
| `12` | `1100b` | `14o` | `Ch` | $8 + 4 = 2^3 + 2^2$ |
| `15` | `1111b` | `17o` | `Fh` | $8 + 4 + 2 + 1 = 2^4 - 1$ (all 4 nibble bits ON) |

Hexadecimal turns binary inspection into rapid mental sight-reading. When an engineer inspects the 16-bit hexadecimal word `3C6Ah`, you can read the four nibbles from left to right in three seconds without touching a calculator:
- `3h` $= 2 + 1 \implies \mathtt{0011}$
- `Ch` ($12_{10}$) $= 8 + 4 \implies \mathtt{1100}$
- `6h` $= 4 + 2 \implies \mathtt{0110}$
- `Ah` ($10_{10}$) $= 8 + 2 \implies \mathtt{1010}$

Putting those four nibbles side by side gives `0011 1100 0110 1010b`. What took sixteen binary digits to write on silicon takes just four hexadecimal characters to hold in your mind. On the SC-32, pressing the **`{{key:BASE}}` menu** via Left Shift `{{key:↰}}` + `{{key:×}}` brings those four radix lenses—`{{key:HEX}}`, `{{key:DEC}}`, `{{key:OCT}}`, and `{{key:BIN}}`—onto the top softkeys, re-rendering all four stack registers (`T, Z, Y, X`) on screen without altering the underlying 36-bit values. Whenever `{{key:HEX}}` is active, the top row of scientific keys from `{{key:√x}}` through `{{key:Σ+}}` acts as an `A`–`F` hexadecimal keypad.

### The Golden Age of the 36-Bit Word: From NASA's IBM 7090 to MIT's PDP-10

If you open a modern laptop or smartphone, its processor registers are organized in multiples of 8-bit bytes—32 bits or 64 bits wide. Yet when the pioneers of scientific computing and artificial intelligence designed the legendary mainframes of the 1950s, 1960s, and 1970s, they converged on a word length that seems surprising today: **the 36-bit word**.

When **Katherine Johnson**, **Dorothy Vaughan**, and NASA's Flight Research Division computed the orbital trajectories for John Glenn's *Friendship 7* Mercury mission and the early Apollo lunar rendezvous studies, celebrated in Margot Lee Shetterly's *Hidden Figures*, the electronic mainframes humming inside Langley and Goddard were **IBM 7090** and **IBM 7094** computers—each built around 36-bit registers. When **John McCarthy** and **Marvin Minsky** founded the MIT Artificial Intelligence Laboratory and invented the **LISP** programming language, giving birth to modern symbolic AI (`CAR` and `CDR` stood for *"Contents of the Address part of Register"* and *"Contents of the Decrement part of Register"* on the 36-bit IBM 704), they worked on 36-bit words. And when researchers at MIT, Stanford, CMU, and BBN built the first nodes of the **ARPANET**, the forerunner of the modern Internet, their beloved workhorse was Digital Equipment Corporation's **DEC PDP-10**, another classic 36-bit architecture.

Why did the greatest scientific and AI architects of the twentieth century fall in love with the number $36$?

Because in number theory, **$36$ is an abundant, highly composite number**—simultaneously divisible by $1, 2, 3, 4, 6, 9, 12,$ and $18$. Compare what happens when you slice a 32-bit word versus a 36-bit word across different number bases and data formats:

1. **Simultaneous Harmony of Octal and Hexadecimal:** A 32-bit word divides evenly into eight 4-bit hexadecimal nibbles ($32 = 8 \times 4$), but leaves an awkward 2-bit orphan stub when grouped into 3-bit octal triads ($32 = 10 \times 3 + 2$). A **36-bit word** is the smallest practical computer word that divides with **zero remainder** into both **twelve 3-bit octal digits** ($36 = 12 \times 3$) *and* **nine 4-bit hexadecimal nibbles** ($36 = 9 \times 4$)!
2. **Ten Full Decimal Digits of Precision:** While a signed 32-bit integer overflows at $+2,147,483,647$ (barely nine full decimal digits—not even enough to hold a 10-digit telephone number or an unsigned 32-bit IPv4 broadcast address), $2^{36} = 68,719,476,736 \approx 6.87 \times 10^{10}$, providing **ten full decimal digits** of integer headroom.
3. **Symmetric Halves & Character Packing:** Thirty-six bits split evenly into two symmetric 18-bit half-words ($36 = 2 \times 18$, allowing LISP and the PDP-10 to pack two memory pointers into a single register) or six 6-bit alphanumeric characters ($36 = 6 \times 6$).

When IBM introduced the commercial System/360 in 1964, Gene Amdahl and Fred Brooks standardized business computing around 8-bit bytes and 32-bit words to match commercial text printers. Yet anyone who has ever tried to enter an unsigned 32-bit hexadecimal address like `0xFFFFFFFF` ($4,294,967,295$) into a standard 32-bit programmer's calculator hits a hard ceiling: because Bit 31 is the sign bit on a 32-bit machine, `0xFFFFFFFF` is either rejected as an overflow or misread as $-1$.

By adopting a classic **36-bit word** across all four stack registers ($T, Z, Y, X$), the SC-32 places its sign bit four positions higher at **Bit 35**. Every 32-bit unsigned memory address, IPv4 network mask (`0xFFFFFFFF`), or microcontroller register sits comfortably in Bits 31–0 as a strictly positive number, with **four extra bits above the 32-bit ceiling—three positive magnitude headroom bits (`Bits 34–32`, expanding positive capacity $8\times$) plus the dedicated sign bit at `Bit 35`** to catch overflow carries, checksum folds, and bit-shifts without losing a single bit.

---

## How a Mechanical Odometer Explains Two's Complement Negative Numbers & Bitwise Masks

### The Backward-Rolling Odometer: Turning Subtraction into Pure Addition

Stop for a moment and ask a fundamental question of computer science: if a silicon chip contains only switches that are `1` (ON) or `0` (OFF), **where do you put a minus sign?**

Early computer designers in the 1940s tried the obvious idea first: use the leftmost bit as a "sign flag" (`0` for $+$, `1` for $-$) and leave the remaining bits as the ordinary magnitude (**Sign-Magnitude** representation). That sounds simple until you try to build the adder circuit: to add $+5$ and $-3$, the hardware first has to compare which number is larger, switch from an adder circuit to a subtractor circuit, and deal with the awkward problem that there are *two different zeros* (`+0` and `-0`).

There is a much deeper, almost magical way to represent negative numbers—one that allows an ordinary binary adder to add positive and negative numbers together **without even knowing which ones are negative**. To see how it works, forget about computers for a moment and picture an old-fashioned **4-digit mechanical bicycle odometer** showing `0000` miles.

- If you ride forward $1\text{ mile}$, the rightmost wheel clicks upward to **`0001`**.
- Now ask: what happens if you start at `0000` and roll the bicycle wheel **backward** one mile ($0 - 1 = -1$)?

All four mechanical number wheels roll backward one click from `0` to `9`, so the odometer window reads **`9999`**. Roll backward a second mile ($0 - 2 = -2$), and it reads **`9998`**. Roll backward three miles ($-3$), and it reads **`9997`**.

Watch what happens when you start with the odometer at **`9997`** (our backward representation of $-3$) and ride **forward** $5\text{ miles}$ ($+5$):
- Click 1: `9998`
- Click 2: `9999`
- Click 3: `0000` (the carry spills off the left end of the 4-digit window)
- Click 4: `0001`
- Click 5: **`0002`**.

Think about what just happened: by representing $-3$ as $10,000 - 3 = 9997$, **ordinary forward addition** ($9997 + 0005 = \cancel{1}0002 \to \mathbf{0002}$) automatically computed $(-3) + 5 = +2$ without separate subtraction circuitry!

In binary hardware, that exact odometer wrap-around is called **Two's Complement** arithmetic. On a 36-bit binary odometer (`000000000h` in nine-nibble hexadecimal):
- Rolling **forward** from `000000000h` ($0$) counts upward through all positive integers up to `7FFFFFFFFh` ($+2^{35} - 1 = +34,359,738,367$), where the leftmost bit (**Bit 35**, the Most Significant Bit or `MSB`) is `0` and all 35 lower bits are `1`.
- Rolling **backward** one click from `000000000h` ($0 - 1 = -1$) turns every single bit to `1`—displaying **`FFFFFFFFFh`** in hexadecimal (`36` consecutive `1` bits in binary).
- How do you find the Two's Complement negative ($-X$) of any integer $X$ in a single step? On our 36-bit odometer, $X$ plus its bitwise logical inverse $\overline{X}$ (where every `0` flips to `1` and every `1` flips to `0`) always equals a string of thirty-six `1`s (`FFFFFFFFFh`), which is one click below zero ($-1$):

$$X + \overline{X} = \text{FFFFFFFFFh} \equiv -1 \pmod{2^{36}} \quad \Longrightarrow \quad -X = \overline{X} + 1$$

**Flip every bit (`NOT`), and add $1$!** That single inside-out rule ($\overline{X} + 1$) is how every microprocessor on Earth—and the **`{{key:+/-}}`** change-sign key on the SC-32—negates integers on the 36-bit odometer and turns subtraction ($Y - X = Y + \overline{X} + 1$) into pure addition.

| Bit Position | Field Designation | Meaning in 36-Bit Two's Complement |
| :---: | :---: | :--- |
| **Bit 35** | `MSB` / Sign Bit | `0` = Positive integer ($0$ to $+2^{35}-1$); `1` = Negative integer ($-2^{35}$ to $-1$) |
| **Bits 34–32** | Upper Headroom | Provides 3 full bits of positive magnitude headroom ($8\times$ capacity) below Sign Bit 35 |
| **Bits 31–0** | Standard 32-Bit Word | Holds full 32-bit unsigned addresses, IPv4 netmasks, and GPIO bitfields |

### Cleaving Words at Any Bit Boundary: Why Euclidean Division (`÷R`) Is a Universal Bit-Slicer

When high-school students first learn long division in elementary school, they write "$12,345$ divided by $16$ equals a **quotient** of $771$ with a **remainder** of $9$," because:

$$12,345 = 771 \times 16 + 9$$

Number theorists call this **Euclidean Division** ($N = Q \cdot D + R$, with $0 \le R < D$). In algebra class, we often abandon remainders in favor of decimal fractions ($12,345 / 16 = 771.5625$). Yet in computer science, keeping the integer quotient $Q = \lfloor N / D \rfloor$ and the integer remainder $R = N \bmod D$ separate is one of the most versatile operations in mathematics.

Why? Because when you divide a binary integer $N$ by a power of two $D = 2^k$, Euclidean division physically **cleaves the binary word in two right at bit position $k$**:

- **The Integer Quotient ($Q = \lfloor N / 2^k \rfloor$) is a Right Bit-Shift ($N \gg k$):** Dividing by $2^k$ slides all the upper bits (from Bit $k$ upward) down by $k$ positions into the ones column, discarding the lower $k$ bits.
- **The Remainder ($R = N \bmod 2^k$) is a Bitwise `AND` Low-Bit Mask ($N \ \& \ (2^k - 1)$):** The remainder left behind is the exact, unshifted value of the lower $k$ bits (`Bits [k-1 : 0]`).

On the SC-32, the dedicated Euclidean division key **`{{key:÷R}}`** (`{{key:↱}}` + `{{key:E}}`) models this cleavage directly across the two lower shelves of the stack: placing any integer in Register $Y$ and a power-of-two divisor $2^k$ in Register $X$ and pressing `{{key:÷R}}` deposits the right-shifted upper quotient $\lfloor Y / X \rfloor$ into Register $X$ and the masked lower remainder $Y \bmod X$ into Register $Y$ in a single keystroke. Examine that $12,345 \div 16$ example in hexadecimal: $12,345_{10} = \mathtt{3039h}$ and $16_{10} = 2^4 = \mathtt{10h}$. When you divide $\mathtt{3039h}$ by $\mathtt{10h}$ ($2^4$) via `{{key:÷R}}`:
- The quotient in Register $X$ is $Q = \mathtt{303h}$ ($771_{10}$)—the upper nibbles shifted right by 4 bits.
- The remainder in Register $Y$ is $R = \mathtt{9h}$ ($9_{10}$)—the bottom 4-bit nibble masked off.

That single mathematical insight unifies six classic computer-engineering operations without needing a maze of hidden bit-shift submenus:

1. **Shifting Left by $k$ Bits ($X \ll k$):** Multiply by $M = 2^k$.
2. **Shifting Right by $k$ Bits ($X \gg k$):** Take the integer quotient on dividing by $M = 2^k$.
3. **Masking the Lowest $k$ Bits ($X \ \& \ (2^k - 1)$):** Take the remainder $X \bmod 2^k$.
4. **Snapping an Address Down to a $2^k$-Aligned Block ($X \ \& \ \overline{(2^k - 1)}$):** Take the integer quotient $\lfloor X / 2^k \rfloor$ and multiply back by $2^k$, zeroing out the bottom $k$ bits.
5. **Extracting a Middle Bit-Field (`Bits [m : k]`):** Take the remainder modulo $2^{m+1}$ to strip away everything above bit $m$, then divide by $2^k$ to shift bit $k$ down to bit $0$.
6. **Setting or Clearing an Individual Hardware Pin (Bit $k$):** Adding $+2^k$ to a register whose $k$-th bit is `0` flips Bit $k$ to `1` (bitwise `OR`), while subtracting $2^k$ from a register whose $k$-th bit is `1` clears Bit $k$ to `0` (`AND NOT`) without any carry or borrow into neighboring bits.

### Euclid's Remainder Ladder: Greatest Common Divisor (GCD) and Least Common Multiple (LCM)

Around 300 BCE in Alexandria, **Euclid** recorded in Book VII, Proposition 2 of his *Elements* what computer scientist Donald Knuth called the oldest nontrivial algorithm in human history: the **Euclidean Algorithm** for finding the **Greatest Common Divisor** $\operatorname{GCD}(a, b)$ of two integers. When a digital signal processor runs one clock domain at $a = 1,071\text{ MHz}$ and another at $b = 462\text{ MHz}$, and you want the largest common reference frequency that divides both evenly, factoring large integers into primes is unnecessary. Euclid noticed that any number dividing both $a$ and $b$ must also divide the remainder $R = a \bmod b$ left over from Euclidean division (`{{key:÷R}}`). Replacing $(a, b)$ with $(b, a \bmod b)$ and pressing `{{key:÷R}}` repeatedly marches down **Euclid's Remainder Ladder** in a handful of steps: $1071 = 2 \times 462 + 147 \longrightarrow 462 = 3 \times 147 + 21 \longrightarrow 147 = 7 \times 21 + 0$. The last non-zero remainder before `0` is the exact Greatest Common Divisor: $\operatorname{GCD}(1071, 462) = \mathbf{21}$!

On the SC-32, you can either step down Euclid's ladder manually with `{{key:÷R}}` or execute the entire ladder in a single keystroke inside the **`{{key:PARTS}}`** menu (Right Shift `{{key:↱}}` above `{{key:√x}}`), which places **`{{key:GCD}}`** (`{{key:LFU4}}`) and **`{{key:LCM}}`** (`{{key:LFU5}}`) side by side alongside `{{key:IP}}`, `{{key:FP}}`, `{{key:ABS}}`, and `{{key:SGN}}`. Once $\operatorname{GCD}(a, b)$ is known, dividing the product $|a \cdot b|$ by $\operatorname{GCD}(a, b)$ gives the **Least Common Multiple**:

$$\operatorname{LCM}(a, b) = \frac{|a \cdot b|}{\operatorname{GCD}(a, b)}$$

Together, `{{key:GCD}}` and `{{key:LCM}}` solve three everyday problems across computer engineering and mechanics: reducing gear-tooth or aspect ratios ($1920 \times 1080$ divided by $\operatorname{GCD}(1920, 1080) = 120$ gives the $16:9$ display ratio), finding the exact cycle period $\operatorname{LCM}(T_1, T_2)$ when two asynchronous timer buses realign in phase, and verifying that a public exponent $e$ is coprime to Euler's totient ($\operatorname{GCD}(e, \varphi(n)) = 1$) in **RSA public-key cryptography**.

### Real-World Bitwise Engineering: Subnet Masks, RGB Pixels, Base64, Endianness & IEEE-754 Floats

Once you can read hexadecimal nibbles and cleave binary words from the inside out at powers of two ($2^k$), five mysteries of modern technology suddenly become transparent:

1. **How Internet Routers Slice IPv4 Addresses (`CIDR` Subnetting):**
   Every IPv4 address on the Internet—such as `192.168.10.45`—is really a single 32-bit integer written for human convenience as four 8-bit decimal bytes (**octets**, each ranging from `0` to `255`, or `00h` to `FFh`). In hexadecimal, `192.168.10.45` packs into `C0A80A2Dh` (`192` $= \mathtt{C0h}$, `168` $= \mathtt{A8h}$, `10` $= \mathtt{0Ah}$, `45` $= \mathtt{2Dh}$):

| Field | Octet 1 (`192` / `C0h`) | Octet 2 (`168` / `A8h`) | Octet 3 (`10` / `0Ah`) | Octet 4 (`45` / `2Dh`) |
| :--- | :---: | :---: | :---: | :---: |
| **Host IP Bits** | `11000000` | `10101000` | `00001010` | `00101101` |
| **Subnet Mask (`/24`)** | `11111111` (Net) | `11111111` (Net) | `11111111` (Net) | `00000000` (Host) |
| **Aligned Network ID** | `11000000` (`192`) | `10101000` (`168`) | `00001010` (`10`) | `00000000` (`0`) |

   When a home or campus network uses a `/24` subnet mask (`255.255.255.0` $= \mathtt{FFFFFF00h}$), the top 24 bits identify the **Network Prefix** `192.168.10.0`, or $\mathtt{C0A80A00h}$ in hex, while the bottom $32 - 24 = 8\text{ bits}$ ($2^8 = 256_{10} = \mathtt{100h}$) identify the **Host Offset** `45`, or $\mathtt{2Dh}$. Dividing `C0A80A2Dh` by $\mathtt{100h}$ cleaves the 32-bit address right at the 8-bit host boundary. Similarly, on a smaller `/28` office subnet (`255.255.255.240`), only the bottom $32 - 28 = 4\text{ bits}$—or $2^4 = 16$ addresses per block—belong to hosts. Dividing host octet `205` by block size `16` gives integer quotient $12$ and remainder $13$ ($205 = 12 \times 16 + 13$), showing that host `205` is the $13\text{th}$ machine inside the `/28` network block starting at $12 \times 16 = \mathbf{192}$.

2. **Packing Color Channels & Base64 Characters by Horner's Method:**
   How does a smartwatch or microcontroller color display pack three separate Red, Green, and Blue brightness numbers into a single 16-bit memory word (`RGB565`)? Because the cones in the human retina are most sensitive to subtle shades of green, `RGB565` gives **5 bits** ($0\dots 31$) to Red in `Bits [15:11]`, **6 bits** ($0\dots 63$) to Green in `Bits [10:5]`, and **5 bits** ($0\dots 31$) to Blue in `Bits [4:0]`:

| Channel Allocation | Bit Positions | Binary Field | Shifted Hex Value |
| :--- | :---: | :---: | :---: |
| **Red (5-bit)** | Bits `15–11` | `11111` (`1Fh × 800h`) | `F800h` |
| **Green (6-bit)** | Bits `10–5` | `010101` (`15h × 20h`) | `02A0h` |
| **Blue (5-bit)** | Bits `4–0` | `00110` (`06h`) | `0006h` |
| **Combined RGB565 Word** | Bits `15–0` | `1111101010100110` | **`FAA6h`** |

   Packing the channels $R_5 = \mathtt{1Fh}$, $G_6 = \mathtt{15h}$, and $B_5 = \mathtt{06h}$ into a single 16-bit integer evaluates $(R_5 \times 2^{11}) + (G_6 \times 2^5) + B_5 = \mathtt{FAA6h}$. Unpacking any 16-bit pixel back into its three color channels requires only two Euclidean divisions at $2^{11} = \mathtt{800h}$ and $2^5 = \mathtt{20h}$.
   That same bit-slicing geometry powers **Base64 encoding** across the web. To transmit binary attachments over text-only email protocols, Base64 welds three 8-bit ASCII bytes—such as `"Man"` ($\mathtt{4D616Eh}$, totaling $3 \times 8 = 24\text{ bits}$)—into a 24-bit integer and slices it at $2^{18} = \mathtt{40000h}$, $2^{12} = \mathtt{1000h}$, and $2^6 = \mathtt{40h}$ into four 6-bit indices ($19, 22, 5, 46$) that map to **`TWFu`**.

3. **Big-Endian vs. Little-Endian Byte Order & Internet Checksums:**
   In 1980, computer scientist Danny Cohen borrowed the terms **Big-Endian** and **Little-Endian** from Jonathan Swift's *Gulliver's Travels* (where two empires went to war over whether to crack a soft-boiled egg at the big end or the little end) to describe how computers store multi-byte integers in memory. Network cables transmit bytes Big-Endian (`12345678h`, most-significant byte `12h` first), whereas x86 and ARM processors store bytes Little-Endian (`78563412h`, least-significant byte `78h` first). And when routers verify that a packet was not corrupted in flight, they use RFC 1071 **16-bit one's-complement addition with end-around carry** {{cite:knuth1997}}—dividing the 32-bit accumulated sum by $2^{16} = \mathtt{10000h}$ and adding the upper carry quotient right back into the lower 16-bit remainder—because end-around carry produces the identical checksum on both Big-Endian and Little-Endian machines.

4. **How IEEE-754 Packs Scientific Notation into 32 and 64 Bits:**
   Finally, how does a computer store a real floating-point number like $-6.25$ inside a 32-bit integer register? William Kahan's **IEEE-754 standard** {{cite:ieee754_2019,golub1996,parker2019}} writes the number in base-2 scientific notation:

$$-6.25_{10} = -(4 + 2 + 0.25) = -110.01_2 = (-1)^1 \times 2^2 \times 1.1001_2$$

   Because every non-zero normalized binary number begins with a leading `1.` before the binary point, IEEE-754 does not even waste a bit storing that leading `1`. Instead, a 32-bit single-precision float (`binary32`) packs **1 Sign bit $S$** in `Bit 31`, an **8-bit Biased Exponent $E = e + 127$** in `Bits [30:23]`, and the **23-bit Fractional Mantissa** after the hidden `1.` in `Bits [22:0]`. For $-6.25_{10}$, the sign bit is $S = 1$, the biased exponent is $2 + 127 = 129_{10} = \mathtt{81h}$, and the fractional mantissa `.1001000..._2` is $\mathtt{480000h}$, forming the 32-bit word **`0xC0C80000`**. Cleaving `C0C80000h` at bit 23 ($2^{23} = \mathtt{800000h}$) and bit 8 ($2^8 = \mathtt{100h}$) via `{{key:÷R}}` unpacks the mantissa, biased exponent, and sign bit onto the stack in two moves.

---

## Combinatorics (PROB), Cryptographic Keyspaces, and the Birthday Collision Paradox

How many distinct states can a digital register, a network topology, or a cryptographic cipher assume—and how quickly do two random hashes collide? In discrete mathematics and computer science, counting finite state spaces rests on the four functions inside the SC-32's **`{{key:PROB}}` menu**: **combinations `{{key:Cn,r}}`**, **permutations `{{key:Pn,r}}`**, **factorials `{{key:x!}}`**, and the uniform pseudo-random generator **`{{key:RAND}}`**.

### Ordered Permutations, Unordered Combinations & Pascal's Symmetry

Given $n$ distinct items—such as $n = 16$ hexadecimal digits (`0`–`F`) or $n = 12$ server racks—from which you draw $r$ items without replacement:
* **Ordered Permutations (`{{key:Pn,r}}`):** When the *order* of selection matters (such as assigning $r = 4$ distinct hexadecimal nibbles to a 4-stage pipeline, or ordering $r = 5$ packet routes out of $n = 12$), there are $n$ choices for the first slot, $n - 1$ for the second, down to $n - r + 1$ for the $r$-th slot:
  $$P(n, r) = n(n - 1)\cdots(n - r + 1) = \frac{n!}{(n - r)!}$$
* **Unordered Combinations (`{{key:Cn,r}}`):** When order does *not* matter (such as choosing any subset of $r = 5$ storage drives out of $n = 12$ for a RAID parity group, or wiring every pair of $r = 2$ routers among $n = 7$ ARPANET nodes), we divide $P(n, r)$ by the $r!$ ways to rearrange the chosen subset—giving Blaise Pascal's binomial coefficient:
  $$C(n, r) = \binom{n}{r} = \frac{P(n, r)}{r!} = \frac{n!}{r!\,(n - r)!}$$

### Richard von Mises's Birthday Paradox & Cryptographic Hash Collisions

That ratio between $P(n, r)$ and $n^r$ unlocks one of the most counterintuitive truths in probability and cybersecurity: **Richard von Mises's Birthday Paradox (1939)**. Ask a roomful of engineers how many people ($k$) must gather in a room before there is at least a $50\%$ chance that two people share the same birthday (out of $N = 365$ days in a year). Intuition whispers $\frac{365}{2} \approx 183\text{ people}$.

Intuition is off by nearly an order of magnitude! Why? Because we are not asking whether someone shares *your specific* birthday; we are asking whether **any** pair among the $\binom{k}{2} = \frac{k(k-1)}{2}$ possible pairs of people in the room matches. To find the exact probability of a collision, compute the complementary probability $P_{\text{unique}}$ that all $k$ people have *different* birthdays: the first person has $365$ free days, the second has $364$, the third has $363$, and the $k$-th has $(365 - k + 1)$—which is the permutation $P(365, k)$ divided by $365^k$:

$$P(\text{at least one collision}) = 1 - \frac{P(365, k)}{365^k} \approx 1 - \exp\!\left(-\frac{k(k - 1)}{2 \times 365}\right)$$

At just **$k = 23\text{ people}$**, the number of pairs reaches $\binom{23}{2} = 253\text{ pairs}$, and $1 - \frac{P(365, 23)}{365^{23}} = \mathbf{0.507297}$ (**$50.73\%$**)! In computer science, that $\sqrt{N}$ scaling is known as the **Birthday Bound**: when a $b$-bit hash function or database UUID spans $N = 2^b$ possible values, random collisions become likely after roughly **$\sqrt{2^b} = 2^{b/2}$ operations**—just $2^{16} = 65,536$ packets for a 32-bit CRC or $2^{32} \approx 4.29 \times 10^9$ blocks for a 64-bit cipher. Modern cryptographic hashes such as SHA-256 therefore use $b = 256\text{ bits}$, pushing the birthday collision threshold safely out of reach to $2^{128} \approx 3.4 \times 10^{38}$—more than a billion times the number of grains of sand on every beach on Earth.

---

## On the Stack: 36-Bit Bases, Boolean Masks & Bitwise Arithmetic

> **How `{{key:BASE}}`, Bitwise Logic (`LOGIC`), and Euclidean Division (`{{key:÷R}}`) Work Together on the Stack:**
> 1. **Four Radix Windows on One 36-Bit Word (`{{key:BASE}}`):** Switching between `{{key:DEC}}`, `{{key:HEX}}`, `{{key:OCT}}`, and `{{key:BIN}}` (via Left Shift `{{key:↰}}` + `{{key:×}}`) never alters the numbers stored in Registers `T, Z, Y, X`—it simply changes the *window* through which you view the same 36-bit integer word. Whenever `{{key:HEX}}` is active, the top row of scientific keys (`{{key:√x}}` through `{{key:Σ+}}`) automatically maps to hexadecimal digits `A` through `F`.
> 2. **Bitwise Logic & Arithmetic Masks (`LOGIC`):** On a 36-bit two's-complement register, bitwise logical gates (`AND`, `OR`, `XOR`, `NOT`) and carry-free positional additions/subtractions ($\pm 2^k$) let you set, clear, invert, or compare individual hardware pins and status flags directly across Registers `Y` and `X`.
> 3. **Universal Bit-Slicing & Wrap-Around (`{{key:÷R}}`):** Pressing `{{key:÷R}}` (`{{key:↱}}` + `{{key:E}}`) divides Register `Y` by Register `X` and deposits both halves of Euclidean division ($N = Q \cdot D + R$) onto the bottom two shelves of the stack—giving you the integer quotient $Q = \lfloor Y / X \rfloor$ and remainder $R = Y \bmod X$ in a single stroke (with a tap of `{{key:x⇄y}}` placing $Q$ in Register `Y` and $R$ in Register `X`). Whether you are extracting base-conversion remainders, wrapping cyclic clock counters, or cleaving a 32-bit word at a power-of-two boundary $D = 2^k$ into its upper bit-shifted field and lower masked bits, `{{key:÷R}}` is the universal bit-slicer.

{{res:sc32_hex_255:screenshot|Decimal 255 converted in place to hexadecimal FFh on the SC-32 transflective display while preserving all four stack registers.}}

### Live Radix Lenses (`DEC`, `HEX`, `OCT`, `BIN`) & Direct Hex Entry

Following the classic HP-32SII philosophy, the SC-32 `{{key:BASE}}` menu (accessed via Left Shift `{{key:↰}}` on the multiplication key `{{key:×}}`, Row 5, Column 3) treats number bases as **live display and entry lenses** over the same underlying 36-bit registers:

| Base System | Keystroke | Screen Suffix | Allowed Character Digits | Example Formatted Display |
| :--- | :--- | :---: | :--- | :--- |
| **Decimal** | `{{key:BASE}} {{key:DEC}}` | *(none)* | `0` through `9` | `1042` |
| **Hexadecimal** | `{{key:BASE}} {{key:HEX}}` | `h` | `0` through `9`, `A` through `F` | `412h` |
| **Octal** | `{{key:BASE}} {{key:OCT}}` | `o` | `0` through `7` | `2022o` |
| **Binary** | `{{key:BASE}} {{key:BIN}}` | `b` | `0` and `1` | `10000010010b` |

Switching between base modes **never destroys, alters, or shifts the values in the operational stack ($X, Y, Z, T$)**. If Register $X$ holds `255` in Decimal mode, pressing `{{key:BASE}} {{key:HEX}}` re-renders the register as `FFh`, pressing `{{key:BASE}} {{key:OCT}}` shows `377o`, and pressing `{{key:BASE}} {{key:BIN}}` reveals all eight asserted bits as `11111111b`.

When Hexadecimal mode (`{{key:HEX}}`) is active, the top row of primary scientific keys across Row 1 maps onto the printed alpha legends $A$ through $F$: `{{key:√x}}` enters $\mathbf{A} = 10_{10}$, `{{key:eˣ}}` enters $\mathbf{B} = 11_{10}$, `{{key:LN}}` enters $\mathbf{C} = 12_{10}$, `{{key:yˣ}}` enters $\mathbf{D} = 13_{10}$, `{{key:1/x}}` enters $\mathbf{E} = 14_{10}$, and `{{key:Σ+}}` enters $\mathbf{F} = 15_{10}$. Entering the classic debugging constant `0xDEADBEEF` thus uses the top-row sequence `yˣ 1/x √x yˣ eˣ 1/x 1/x Σ+`. In the workbench tables below, hexadecimal literals such as `C0A80A2D` or `1F` are written in compact hex notation for readability; on the physical keypad in `HEX` mode, always enter the hex digits `A`–`F` using Row 1 (`√x` through `Σ+`). Whenever you want to apply scientific functions such as square root, natural logarithm, or powers to a hexadecimal value, switch back to Decimal mode (`{{key:BASE}} {{key:DEC}}`) first so the top-row keys resume their mathematical roles.

Because the SC-32 preserves all four stack registers across base changes, you can also mix radices in the middle of a calculation without jotting down a single intermediate number. To add a hexadecimal base offset $3\text{A}7_{16}$ to an octal permission mask $452_8$ and read the sum in decimal, enter `3 {{key:√x}} 7 {{key:ENTER}}` ($935_{10}$) in `{{key:HEX}}` mode, switch to `{{key:OCT}}` mode to add `452 {{key:+}}` ($2261_8$), and switch to `{{key:DEC}}` mode to read the combined total **$1,201_{10}$** in Register $X$.

### Euclidean Division (÷R): Flash Memory Pages, IPv4 Octets & Clock Bus Alignment

Because Euclidean division **`{{key:÷R}}`** operates entirely on the bottom two stack shelves—consuming the dividend $N$ in **Register $Y$** and the divisor $D$ in **Register $X$** to split the word into an integer quotient $Q = \lfloor Y / X \rfloor$ and a non-negative remainder $R = Y \bmod X$ across **Registers $X$ and $Y$** while leaving **Registers $Z$ and $T$ untouched**—single-step address splits need no multi-register staging at all. Suppose a DMA controller accesses byte address $12,345$ inside a flash memory array:
* **16-Byte Cache-Line Row & Offset (`12345 ÷R 16`):** Working in `{{key:DEC}}` mode, keying `{{res:sc32_10_computer_science_bases_seq_01:keys}}` cleaves $12,345 = 771 \times 16 + 9$ at the $2^4 = 16$ bit boundary, placing the 16-byte row quotient $Q = \mathbf{{{res:sc32_10_computer_science_bases_seq_01:value}}}$ in Register $X$ and the intra-row byte remainder $R = \mathbf{9}$ in Register $Y$ (where a single tap of `{{key:x⇄y}}` parks the quotient `771` in **Register $Y$** and brings the remainder `9` into **Register $X$**).
* **256-Byte Flash Page & Offset (`12345 ÷R 256`):** When that same physical byte address $12,345$ (`0x3039`) is mapped onto a SPI NOR flash chip organized into $2^8 = 256\text{-byte}$ programmable pages, keying `12345 {{key:ENTER}} 256 {{key:÷R}}` (followed by `{{key:x⇄y}}` when inspecting the offset in $X$ and page in $Y$) cleaves the word right at Bit 8 into **`Page 48`** ($\lfloor 12,345 / 256 \rfloor = 48$, upper byte `0x30`) and **`Offset 57`** ($12,345 \bmod 256 = 57$, lower byte `0x39`), since $48 \times 256 + 57 = 12,345$, while Registers $Z$ and $T$ remain at zero.

That same two-register `{{key:÷R}}` cleavage decomposes IPv4 network addresses in base $256$ ($2^8$) and aligns Classless Inter-Domain Routing (`CIDR`) subnets:
* **Base-256 IPv4 Octet Unpacking (`3232235777` $\to$ `192.168.1.1`):** An unsigned 32-bit IPv4 socket address such as `3232235777` (`0xC0A80101`) is simply a four-digit integer written in base $256$. Keying `3232235777 {{key:ENTER}} 256 {{key:÷R}}` in `{{key:DEC}}` mode strips off the lowest 8-bit octet **`1`** into Register $Y$ and leaves the upper 24-bit prefix `12625921` in Register $X$. Repeating `256 {{key:÷R}}` peels off the third octet **`1`** into $Y$ (with `49320` in $X$), and a third `256 {{key:÷R}}` splits the remaining 16-bit prefix into the first octet **`192`** in Register $X$ and the second octet **`168`** in Register $Y$—reading off **`192.168.1.1`** across the four stack registers (`1, 1, 168, 192`).
* **Aligning a `/28` VLAN Interface (`205` $\to$ Block `192`, Offset `13`):** On a `/28` subnet (`255.255.255.240`), the host field occupies only the bottom $32 - 28 = 4\text{ bits}$, partitioning the final octet into 16-address blocks ($2^4 = 16$). Dividing host octet `205` by the block stride `16` via `{{key:÷R}}` places the block index `12` in Register $X$ and the host offset `13` in Register $Y$ (with $Z$ and $T$ at zero), so multiplying Register $X$ back by `16` zeroes out the low 4 host bits: keying `{{res:sc32_10_computer_science_bases_seq_03:keys}}` snaps directly to the aligned `/28` network base ID **`{{res:sc32_10_computer_science_bases_seq_03:value}}`** (`12 × 16 = 192`).

For **Partitioning a Full 32-Bit IPv4 Address on a `/24` Subnet (`192.168.10.45`)**, working directly in `{{key:HEX}}` mode turns byte-aligned routing math into two-register nibble slicing while Registers $Z$ and $T$ rest at `0h`:
* **Step 1 — Align the `/24` Network Base (`192.168.10.0`):** Cleaving the packed 32-bit workstation address `C0A80A2Dh` at the 8-bit host boundary ($2^8 = \text{100h}$) separates the 24-bit network prefix `C0A80Ah` in Register $X$ from the 8-bit host ID `2Dh` ($45_{10}$) in Register $Y$, and multiplying Register $X$ back by `100h` zeros out the host byte. Keying `{{res:sc32_10_computer_science_bases_seq_04:keys}}` produces the aligned `/24` network base **`{{res:sc32_10_computer_science_bases_seq_04:value}}`** (`192.168.10.0`).
* **Step 2 — Isolate the Inverted Host Wildcard Mask (`0.0.0.255`):** Subtracting the `/24` netmask `FFFFFF00h` from the 32-bit all-ones broadcast word `FFFFFFFFh` flips every network bit to `0` and every host bit to `1`. Keying `{{res:sc32_10_computer_science_bases_seq_05:keys}}` isolates the 8-bit host wildcard mask **`{{res:sc32_10_computer_science_bases_seq_05:value}}`**.
* **Step 3 — Populate the Directed `/24` Broadcast Address (`192.168.10.255`):** Because the aligned network base (`C0A80A00h`) and the host wildcard (`000000FFh`) occupy non-overlapping bit lanes, adding them performs an exact carry-free bitwise `OR` across the bottom 8 bits. Keying `{{res:sc32_10_computer_science_bases_seq_06:keys}}` delivers the directed `/24` broadcast address **`{{res:sc32_10_computer_science_bases_seq_06:value}}`**.

### 36-Bit Two's Complement Odometer Seams & Hardware Bit-Fields

Because a two's-complement register maps negative integers onto the upper half of a modular ring $\mathbb{Z}/2^{36}\mathbb{Z}$, we can watch both rollover seams of the 36-bit binary odometer click across the discontinuity in `{{key:HEX}}` mode on Registers $Y$ and $X$ {{cite:parker2019}}:
* **Signed Positive Overflow Seam (`+Max + 1 → -Min`):** At the highest positive 36-bit integer `7FFFFFFFFh` ($+2^{35} - 1 = +34,359,738,367_{10}$), Sign Bit 35 is `0` while all 35 magnitude bits (Bits 34–0) are `1`. Adding `1` propagates a ripple carry through all 35 magnitude bits into Sign Bit 35: keying `{{res:sc32_10_computer_science_bases_seq_33:keys}}` wraps discontinuously to the most negative 36-bit integer **`{{res:sc32_10_computer_science_bases_seq_33:value}}`** ($-2^{35} = -34,359,738,368_{10}$).
* **Zero Underflow Seam (`0 - 1 → -1`):** Rolling the odometer backward one click from `0` borrows across every bit position simultaneously, turning all thirty-six bits ON: keying `{{res:sc32_10_computer_science_bases_seq_34:keys}}` produces **`{{res:sc32_10_computer_science_bases_seq_34:value}}`** ($-1_{10}$).

Every bit-field shift and mask operation maps directly to a power of two $M = 2^k$ {{cite:shannon1938}}:

| Bit-Field / Masking Operation | Mathematical Equivalent ($M = 2^k$) | SC-32 RPN Keystrokes (`HEX` / `DEC`) | Result Location |
| :--- | :---: | :--- | :--- |
| **Left Shift ($X \ll k$)** | $X \times 2^k$ | `X {{key:ENTER}} M {{key:×}}` | Shifted word in **`X`** |
| **Right Shift ($X \gg k$)** | $\lfloor X / 2^k \rfloor$ | `X {{key:ENTER}} M {{key:÷R}}` (or `{{key:÷}}` in `HEX`/`OCT`/`BIN`) | Upper bits in **`X`** |
| **Low-Bit Mask ($X \ \& \ (2^k - 1)$)** | $X \bmod 2^k$ | `X {{key:ENTER}} M {{key:÷R}} {{key:x⇄y}}` | Low $k$ bits in **`X`** |
| **High-Bit Alignment ($X \ \& \ \sim(2^k - 1)$)** | $\lfloor X / 2^k \rfloor \times 2^k$ | `X {{key:ENTER}} M {{key:÷R}} M {{key:×}}` | Aligned base in **`X`** |
| **Set Disjoint Bit $k$** | $X + 2^k$ | `X {{key:ENTER}} M {{key:+}}` | Updated word in **`X`** |
| **Clear Set Bit $k$** | $X - 2^k$ | `X {{key:ENTER}} M {{key:-}}` | Updated word in **`X`** |
| **32-Bit Unsigned Complement** | $\text{FFFFFFFF}_{16} - X$ | `FFFFFFFF {{key:ENTER}} X {{key:-}}` | Inverted mask in **`X`** |

*(Note that for right bit-shifts in `{{key:DEC}}` mode, `{{key:÷R}}` is preferred over `{{key:÷}}` because `{{key:÷}}` retains fractional decimal digits in Decimal mode, whereas `{{key:÷R}}` always truncates to the integer quotient $\lfloor X / 2^k \rfloor$ in every base!)*

In **Toggling GPIO Pins, Telemetry Fault Masks & ADC Bit-Fields**, memory-mapped microcontroller peripherals pack independent hardware control lines into a single register word so firmware can flip or inspect individual pins via positional masks $2^k$ without disturbing neighboring lines:
* **Asserting an Unset GPIO Direction Pin (`GPIO_DIR | (1 << 5)`):** Suppose a 32-bit GPIO direction register holds `0x00001804`—meaning Pins 2 ($2^2 = \text{4h}$), 11 ($2^{11} = \text{800h}$), and 12 ($2^{12} = \text{1000h}$) are already configured as outputs while Pin 5 is currently an input (`0`). Because Bit 5 is initially unasserted, adding its positional weight $2^5 = 32_{10} = \text{20h}$ in `{{key:HEX}}` mode performs a carry-free bitwise `OR`: keying `{{res:sc32_10_computer_science_bases_seq_11:keys}}` asserts Pin 5 to produce **`{{res:sc32_10_computer_science_bases_seq_11:value}}`** (`1824h`).
* **Clearing and Re-Asserting an Active Heartbeat Pin (`PORT & ~(1 << 2)`):** If a port output register holds `0x00000017` ($0001\,0111_2$) with an active heartbeat line on Bit 2 ($2^2 = \text{4h}$), subtracting the bit weight in `{{key:HEX}}` mode performs a borrow-free `AND NOT`: keying `{{res:sc32_10_computer_science_bases_seq_13:keys}}` clears Bit 2 to **`{{res:sc32_10_computer_science_bases_seq_13:value}}`**, and adding `4h` back via `{{res:sc32_10_computer_science_bases_seq_14:keys}}` (or `{{key:LASTX}} {{key:+}}`) re-asserts the pin to **`{{res:sc32_10_computer_science_bases_seq_14:value}}`** without disturbing neighboring pins.
* **Isolating Tripped Telemetry Fault Flags (`Status ^ Baseline`):** Whenever a baseline register's asserted bits are a subset of an active status word, borrow-free subtraction acts as an exact bitwise `XOR` difference mask. Comparing a spacecraft downlink status word `0x5F5A` against its nominal baseline `0x5A50` via `{{res:sc32_10_computer_science_bases_seq_36:keys}}` strips away the nominal bits to isolate the newly tripped fault mask **`{{res:sc32_10_computer_science_bases_seq_36:value}}`**—which renders as $\mathbf{10100001010\text{b}}$ in `{{key:BIN}}`, revealing a Hamming weight of **$4\text{ fault bits}$** at positions 1, 3, 8, and 10.
* **Extracting an Interior Multi-Bit Field (`Bits [7:4]` of `0x3C6A`):** When a peripheral packs a 4-bit oversampling selector in Bits [7:4] (`6h`) inside a 16-bit ADC control register holding `0x3C6A`, extracting the interior field requires stripping off the high bits above Bit 7 ($\bmod 2^8 = \text{100h}$) and shifting the low bits below Bit 4 out of the way ($\div 2^4 = \text{10h}$):

$$\text{Bits } [7:4] = \left\lfloor \frac{\mathtt{3C6Ah} \bmod 2^8}{2^4} \right\rfloor = \left\lfloor \frac{\mathtt{6Ah}}{\mathtt{10h}} \right\rfloor = \mathtt{6h}$$

  First, cleaving at $2^8 = \text{100h}$ via `{{res:sc32_10_computer_science_bases_seq_15:keys}}` masks off the upper configuration byte (`3Ch`) and brings the lower 8-bit byte **`{{res:sc32_10_computer_science_bases_seq_15:value}}`** into Register $X$; second, right-shifting by 4 bits ($\div 2^4 = \text{10h}$) via `{{res:sc32_10_computer_science_bases_seq_16:keys}}` discards the bottom nibble (`Ah`) so Bits [7:4] land right-justified at Bit 0 as **`{{res:sc32_10_computer_science_bases_seq_16:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3C6A {{key:ENTER}}` | `0h` | `0h` | `3C6Ah` | `3C6Ah` | Stage 16-bit ADC register word `3C6Ah` |
| `100 {{key:÷R}}` | `0h` | `0h` | `6Ah` | `3Ch` | Split upper byte `3Ch` into X and lower byte `6Ah` into Y |
| `{{key:x⇄y}}` | `0h` | `0h` | `3Ch` | `6Ah` | Swap lower byte `6Ah` (Bits [7:0]) into Register X |
| `10 {{key:÷}}` | `0h` | `0h` | `3Ch` | `6h` | Shift right by 4 bits (`÷ 10h`) to isolate Bits [7:4] = `6h` |

### Packing RGB565 Pixels, Slicing Base64 Sextets & Reversing Endianness

In **Packing & Unpacking 16-Bit RGB565 Color Pixels**, embedded SPI framebuffer controllers conserve SRAM bandwidth by multiplexing three independent color intensities—5-bit Red (`1Fh` $= 31/31$ full scale), 6-bit Green (`15h` $= 21/63$), and 5-bit Blue (`06h` $= 6/31$)—into non-overlapping bit lanes of a single 16-bit word in `{{key:HEX}}` mode:
* **Shift Red into `Bits [15:11]` (`× 800h`):** Multiplying Red (`1Fh`) by $2^{11} = \text{800h}$ left-shifts those 5 bits across the Green and Blue lanes: keying `{{res:sc32_10_computer_science_bases_seq_19:keys}}` places **`{{res:sc32_10_computer_science_bases_seq_19:value}}`** in Register $X$.
* **Shift Green into `Bits [10:5]` (`× 20h`) and Merge:** Multiplying Green (`15h`) by $2^5 = \text{20h}$ via `{{res:sc32_10_computer_science_bases_seq_20:keys}}` left-shifts the 6 green bits into Bits [10:5] as **`{{res:sc32_10_computer_science_bases_seq_20:value}}`** while `F800h` waits in Register $Y$.
* **Combine All Three Lanes (`FAA6h`):** Merging Red and Green (`FAA0h`) and adding the unshifted 5-bit Blue channel (`06h`) in Bits [4:0] via `{{res:sc32_10_computer_science_bases_seq_21:keys}}` completes the packed 16-bit framebuffer pixel **`{{res:sc32_10_computer_science_bases_seq_21:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1F {{key:ENTER}}` | `0h` | `0h` | `1Fh` | `1Fh` | Stage 5-bit Red channel `1Fh` ($31_{10}$) |
| `800 {{key:×}}` | `0h` | `0h` | `0h` | `F800h` | Shift Red left 11 bits (`× 800h`) into Bits [15:11] |
| `15 {{key:ENTER}}` | `0h` | `F800h` | `15h` | `15h` | Stage 6-bit Green channel `15h` ($21_{10}$); Red lifts to Z |
| `20 {{key:×}}` | `0h` | `0h` | `F800h` | `2A0h` | Shift Green left 5 bits (`× 20h`) into Bits [10:5] |
| `{{key:+}}` | `0h` | `0h` | `0h` | `FAA0h` | Combine shifted Red and Green channels (`FAA0h`) |
| `6 {{key:+}}` | `0h` | `0h` | `0h` | `FAA6h` | Add 5-bit Blue channel `06h` for packed `RGB565` word `FAA6h` |

Conversely, given a packed 16-bit RGB565 pixel `0xF38E` in `{{key:HEX}}` mode, keying `F38E {{key:ENTER}} 800 {{key:÷R}} {{key:x⇄y}} 20 {{key:÷R}}` unpacks all three color channels onto the visible stack in one pass: Red in Register $Z$ (`1Eh` $= 30_{10}$), Green in Register $X$ (`1Ch` $= 28_{10}$), and Blue in Register $Y$ (`Eh` $= 14_{10}$).

When **Slicing 24-Bit Base64 Sextets & Swapping Endian Byte Order**, network encoders must re-partition three 8-bit ASCII bytes (`3 × 8 = 24 bits`) into four 6-bit **Base64** alphabet indices (`4 × 6 = 24 bits`) so binary payloads can traverse 7-bit text protocols without control-character corruption. Concatenating the three ASCII bytes of `"Man"` (`'M' = 4Dh`, `'a' = 61h`, `'n' = 6Eh`) forms the 24-bit integer `4D616Eh`, which we slice at the three 6-bit boundaries $2^{18} = \text{40000h}$, $2^{12} = \text{1000h}$, and $2^6 = \text{40h}$ in `{{key:HEX}}` mode:
* **Sextet 1 (`Bits [23:18]` $\to$ `'T'`):** Right-shifting by 18 bits (`÷ 40000h`) via `{{res:sc32_10_computer_science_bases_seq_29:keys}}` extracts **`{{res:sc32_10_computer_science_bases_seq_29:value}}`** ($19_{10} \implies$ Base64 `'T'`).
* **Sextet 2 (`Bits [17:12]` $\to$ `'W'`):** Masking the 18-bit remainder and right-shifting by 12 bits (`÷ 1000h`) via `{{res:sc32_10_computer_science_bases_seq_30:keys}}` isolates **`{{res:sc32_10_computer_science_bases_seq_30:value}}`** ($22_{10} \implies$ `'W'`).
* **Sextet 3 (`Bits [11:6]` $\to$ `'F'`):** Cleaving the 12-bit remainder at 6 bits (`÷ 40h`) via `{{res:sc32_10_computer_science_bases_seq_31:keys}}` extracts **`{{res:sc32_10_computer_science_bases_seq_31:value}}`** ($5_{10} \implies$ `'F'`).
* **Sextet 4 (`Bits [5:0]` $\to$ `'u'`):** Masking the final 6-bit remainder via `{{res:sc32_10_computer_science_bases_seq_32:keys}}` leaves **`{{res:sc32_10_computer_science_bases_seq_32:value}}`** ($46_{10} \implies$ `'u'`), spelling out **`TWFu`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `4D616E {{key:ENTER}} 40000 {{key:÷}}` | `0h` | `0h` | `0h` | **`13h`** | Sextet 1: `4D616Eh >> 18 = 13h` ($19_{10} \implies \mathbf{T}$) |
| `4D616E {{key:ENTER}} 40000 {{key:÷R}} {{key:x⇄y}} 1000 {{key:÷}}` | `13h` | `13h` | `13h` | **`16h`** | Sextet 2: remainder `>> 12 = 16h` ($22_{10} \implies \mathbf{W}$) |
| `4D616E {{key:ENTER}} 1000 {{key:÷R}} {{key:x⇄y}} 40 {{key:÷}}` | `16h` | `16h` | `4D6h` | **`5h`** | Sextet 3: remainder `>> 6 = 5h` ($5_{10} \implies \mathbf{F}$) |
| `4D616E {{key:ENTER}} 40 {{key:÷R}} {{key:x⇄y}}` | `4D6h` | `5h` | `13585h` | **`2Eh`** | Sextet 4: lower 6-bit remainder = `2Eh` ($46_{10} \implies \mathbf{u}$) |

*(Single-Entry `÷R` Cascade: Chaining `4D616E {{key:ENTER}} 40000 {{key:÷R}} {{key:x⇄y}} 1000 {{key:÷R}} {{key:x⇄y}} 40 {{key:÷R}}` unpacks all four Base64 indices across the four stack registers—`13h` in $T$, `16h` in $Z$, `2Eh` in $Y$, and `5h` in $X$—with `4D616E` keyed only once.)*

When an ARM or x86 processor (which stores multi-byte integers **Little-Endian**, least-significant byte at the lowest memory address) reads a 32-bit TCP/IP network header transmitted **Big-Endian** (`0x12345678`, most-significant byte first), it must execute a 32-bit byte-reversal (`BSWAP` / `REV`) to form `0x78563412` in `{{key:HEX}}` mode. Because each shifted byte is folded into a running sum on Register $X$ as soon as it is formed, the entire 4-byte reversal executes on Shelves $Y$ and $X$ while Registers $Z$ and $T$ stay at `0h`:
* **Promote Byte 0 (`78h` $\ll 24$) into Byte 3:** Multiplying `78h` by $2^{24} = \text{1000000h}$ via `{{res:sc32_10_computer_science_bases_seq_41:keys}}` yields **`{{res:sc32_10_computer_science_bases_seq_41:value}}`** (`78000000h`).
* **Promote Byte 1 (`56h` $\ll 16$) into Byte 2:** Multiplying `56h` by $2^{16} = \text{10000h}$ via `{{res:sc32_10_computer_science_bases_seq_42:keys}}` positions **`{{res:sc32_10_computer_science_bases_seq_42:value}}`** (`560000h`) and merges them into `78560000h`.
* **Promote Byte 2 (`34h` $\ll 8$) into Byte 1:** Multiplying `34h` by $2^8 = \text{100h}$ via `{{res:sc32_10_computer_science_bases_seq_43:keys}}` places **`{{res:sc32_10_computer_science_bases_seq_43:value}}`** (`3400h`) into Byte 1 (`78563400h`).
* **Demote Byte 3 (`12h` $\gg 24$) into Byte 0:** Right-shifting the original most-significant byte via `{{res:sc32_10_computer_science_bases_seq_44:keys}}` isolates **`{{res:sc32_10_computer_science_bases_seq_44:value}}`** (`12h`), so adding `12h` completes the byte-swapped Little-Endian word **`78563412h`**.

### RFC 1071 Checksums, Circular Rotations (`ROL`), UART Dividers & IEEE-754 Unpacking

Why do Internet routers compute packet header checksums using **16-bit one's-complement addition with end-around carry** (RFC 1071) rather than ordinary two's-complement modular addition? Because wrapping any overflow carry out of Bit 15 right back into Bit 0 makes the checksum associative and invariant to Big-Endian vs. Little-Endian byte order! When summing the ten 16-bit words of an IPv4 header inside a 32-bit accumulator produces `2653Dh` in `{{key:HEX}}` mode, cleaving at the 16-bit boundary $2^{16} = \text{10000h}$ via `2653D {{key:ENTER}} 10000 {{key:÷R}}` separates the upper carry quotient `2h` in Register $X$ from the lower 16-bit sum `653Dh` in Register $Y$ (with $Z = T = \text{0h}$). Pressing `{{key:+}}` folds that end-around carry directly into Bit 0 (`653Fh`), and subtracting from the all-ones 16-bit mask `FFFFh` via `FFFF {{key:x⇄y}} {{key:-}}` inverts every bit to form the one's-complement wire checksum **`9AC0h`** ($39,616_{10}$ in `{{key:DEC}}`).

In cryptographic block ciphers and cyclic redundancy checks, that same two-register end-around carry implements a **circular 1-bit left rotation (`ROL 1`)** across an 8-bit register boundary ($2^8 = \text{100h}$), where the bit shifted out of Bit 7 wraps around to enter Bit 0 (`0x85` $= 10000101_2 \implies 00001011_2 = \text{0Bh}$):
* **Step 1 — Left-Shift All 8 Bits (`× 2`):** Doubling `85h` via `{{res:sc32_10_computer_science_bases_seq_50:keys}}` shifts the byte left by one position to **`{{res:sc32_10_computer_science_bases_seq_50:value}}`** (`10Ah`), pushing the old MSB into Bit 8.
* **Step 2 — Cleave at the 8-Bit Boundary (`÷R 100h`):** Dividing by `100h` via `{{res:sc32_10_computer_science_bases_seq_51:keys}}` separates the low 8-bit remainder (`Ah` in Register $Y$) from the Bit 8 carry (**`{{res:sc32_10_computer_science_bases_seq_51:value}}`** $= \text{1h}$ in Register $X$).
* **Step 3 — Fold the Carry into Bit 0 (`+`):** Adding the carry back into the low byte via `{{res:sc32_10_computer_science_bases_seq_52:keys}}` completes the circularly rotated byte **`{{res:sc32_10_computer_science_bases_seq_52:value}}`** (`Bh`).

When configuring an asynchronous serial `UART` transceiver from a $f_{\text{clk}} = 150.0\text{ MHz}$ system bus at $115,200\text{ baud}$ with $8\times$ oversampling, hardware fractional baud-rate generators split the ideal divisor $\text{Divider} = \frac{150,000,000}{8 \times 115,200} \approx 162.760417$ into a 16-bit integer mantissa register (`IBRD`) and a 6-bit fixed-point sixty-fourths register (`FBRD` $= \lfloor 64 \times \text{FP} + 0.5 \rfloor$). Switching to `{{key:DEC}}` mode and keying `{{res:sc32_10_computer_science_bases_seq_40:keys}}` yields the exact divisor **`{{res:sc32_10_computer_science_bases_seq_40:value}}`** in Register $X$. Duplicating that divisor and extracting `{{key:IP}}` isolates `IBRD = 162` while swapping to take the fractional part `{{key:FP}}` isolates $0.76041667$; multiplying by $64$ and rounding via `{{key:RND}}` converts $48.6667$ to **`FBRD = 49`** ($49/64 = 0.765625$) in Register $X$ right beside `IBRD = 162` in Register $Y$.

Finally, to see how William Kahan's **IEEE-754 single-precision (`binary32`) format** packs a real number $(-1)^S \times 2^{E - 127} \times (1 + M / 2^{23})$ into a 32-bit word `0xC0C80000` ($-6.25_{10}$) so integer comparators can sort floats lexicographically, chain two `{{key:÷R}}` cleavages in `{{key:HEX}}` mode—first at the 23-bit mantissa boundary ($2^{23} = \text{800000h}$) and then at the 8-bit biased-exponent boundary ($2^8 = \text{100h}$). That two-step cascade unpacks all three bit-fields onto adjacent stack registers: the 23-bit fractional significand `480000h` ($4,718,592 / 2^{23} = 0.5625$, representing $1.5625$ with the hidden leading `1.`) in Register $Z$, the 8-bit biased exponent `81h` ($129_{10}$, so true exponent $e = 129 - 127 = 2$) in Register $Y$, and the sign bit `1h` (negative) in Register $X$, confirming $(-1)^1 \times 2^2 \times 1.5625 = -6.25$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `C0C80000 {{key:ENTER}}` | `0h` | `0h` | `C0C80000h` | `C0C80000h` | Stage 32-bit IEEE-754 float word `C0C80000h` |
| `800000 {{key:÷R}}` | `0h` | `0h` | `480000h` | `181h` | Cleave at Bit 23: mantissa `480000h` in Y, upper 9 bits `181h` in X |
| `100 {{key:÷R}}` | `0h` | `480000h` | `81h` | `1h` | Cleave at Bit 8: Sign `1h` in X, Exponent `81h` in Y, Mantissa in Z |
| `{{key:BASE}} {{key:DEC}}` | 0 | 4718592 | 129 | 1 | Switch to Decimal: $S = 1$, $E = 129$, $M = 4,718,592$ |
| `{{key:x⇄y}} 127 {{key:-}}` | 4718592 | 4718592 | 1 | 2 | Subtract bias $127$ to reveal true binary exponent $e = 2$ |

Similarly, for a 64-bit IEEE-754 double-precision float (`binary64`) such as $-13.375_{10}$ (`0xC02AC00000000000`), we inspect its upper 32-bit word `0xC02AC000` in `{{key:HEX}}` mode. Chaining `C02AC000 {{key:ENTER}} 100000 {{key:÷R}} 800 {{key:÷R}}` cleaves the word at $2^{20} = \text{100000h}$ and $2^{11} = \text{800h}$ to leave Sign $S = \mathbf{1}$ in $X$, Biased Exponent $E = \mathbf{\text{402h}}$ ($1026_{10}$, so $e = 1026 - 1023 = \mathbf{3}$) in $Y$, and the upper 20-bit significand `AC000h` ($704,512 / 2^{20} = 0.671875$) in $Z$, reconstructing $(-1)^1 \times 2^3 \times 1.671875 = \mathbf{-13.375}$.

### Combinatorics (PROB) & Birthday Paradox Collision Probability

Switching back to `{{key:DEC}}` mode, we can explore discrete state spaces and collision bounds through the **`{{key:PROB}}` menu** (Right Shift `{{key:↱}}` above `{{key:eˣ}}`). To see how drastically ordering expands a state space, compare a 12-drive storage array selecting $5$ drives for an unordered RAID parity group ($C(12, 5)$) against an ordered 5-drive failover chain ($P(12, 5)$): `12 {{key:ENTER}} 5 {{key:PROB}} {{key:Cn,r}}` counts **`792`** unordered subsets, whereas `12 {{key:ENTER}} 5 {{key:PROB}} {{key:Pn,r}}` spans **`95,040`** ordered sequences.

Across network and processor hardware, the same combinatorial primitives size physical topologies in a single step:
* **4-Stage Non-Repeating Hex Pipeline ($P(16, 4)$):** Assigning an ordered 4-nibble sequence without repetition from $16$ hexadecimal digits via `{{res:sc32_10_computer_science_bases_seq_47:keys}}` yields **`{{res:sc32_10_computer_science_bases_seq_47:value}}`** distinct pipeline states.
* **7-Router Full-Mesh Point-to-Point Links ($C(7, 2)$):** Wiring every unordered pair of routers across a 7-node network via `{{res:sc32_10_computer_science_bases_seq_48:keys}}` requires **`{{res:sc32_10_computer_science_bases_seq_48:value}}`** cables.
* **15-Packet Priority Queue Permutations ($15!$):** Ordering an entire 15-packet queue via `{{res:sc32_10_computer_science_bases_seq_49:keys}}` explodes to **`{{res:sc32_10_computer_science_bases_seq_49:value}}`** schedules ($12! = 479,001,600$ for $12$ items).

Finally, to verify the **23-person Birthday Collision Paradox** ($1 - P(365, 23)/365^{23}$) on the stack, `365 {{key:ENTER}} 23 {{key:PROB}} {{key:Pn,r}}` evaluates the collision-free assignments across $23$ people ($4.220082 \times 10^{58}$), dividing by `365 {{key:ENTER}} 23 {{key:yˣ}} {{key:÷}}` gives the no-collision probability $P_{\text{unique}} = \mathbf{0.492703}$, and subtracting from $1$ via `1 {{key:x⇄y}} {{key:-}}` confirms that the probability of a shared birthday or hash collision has already crossed **`0.507297`** (**$50.73\%$**)!

---

### From Binary Registers to the Mathematics of Time and Money

Every base conversion and bit-packing operation in this chapter rests on a single mathematical structure: **positional power scaling**. Writing an integer in base $b$ weights each column by $b^k$ and evaluates the resulting Horner polynomial $\sum d_k b^k$ from the inside out—whether $b = 2$ inside a silicon logic gate, $b = 16$ across a memory map, or $b = 10$ on an everyday ledger.

What happens when we replace the discrete integer radix $b = 2$ with a continuous compounding growth factor $(1 + i)$ across time? Positional power scaling across bit columns becomes **discounting and compounding across payment periods**—turning Horner's polynomial into the fundamental equation of mortgages, annuities, bonds, and capital investments. We open that eight-hundred-year-old financial engine next in **[Chapter 11: The Eight-Hundred-Year Engine of Compound Interest: Time Value of Money](11-financial-tvm.md)**.
