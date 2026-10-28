---
title: "Chapter 10: Ones, Zeros, and the 36-Bit Machine: From Leibniz and Shannon to Modern Computing | Thinking in the Stack (SC-32)"
description: "36-bit two's complement integer architecture, base conversions (HEX, DEC, OCT, BIN), integer division & remainder bit-field extraction (÷R), CIDR IPv4 subnetting, RGB565 packing, combinatorics, and IEEE-754 representation on the StackCalc SC-32."
---

# Chapter 10: Ones, Zeros, and the 36-Bit Machine: From Leibniz and Shannon to Modern Computing

## Leibniz's Medallion, Boole's Logic & Claude Shannon's 1937 Master's Thesis

### From Leibniz's Binary Medallion to Shannon's Relay Basement

In the summer of 1937, a twenty-one-year-old master's student named **Claude Elwood Shannon** stood in the basement of MIT's electrical engineering building, surrounded by the clatter of brass gears and electromechanical telephone relays. His graduate assignment was maintaining Vannevar Bush's Differential Analyzer—a room-filling hundred-ton mechanical analog computer whose spinning steel shafts, torque amplifiers, and wheel-and-disc integrators solved differential equations through physical rotation.

Every time a physicist or ballistician brought a new differential equation to the basement laboratory, Shannon had to spend hours configuring two distinct worlds: the continuous mechanical shafts of the analyzer, and a maze of clicking telephone relay circuits that controlled its switches, clutches, and safety interlocks.

As Shannon wired those relays in series and in parallel, a startling memory surfaced from an undergraduate philosophy class he had taken at the University of Michigan. Eighty-three years earlier, in 1854, a self-taught English mathematician named **George Boole**—the son of a struggling Lincoln shoemaker—had published *An Investigation of the Laws of Thought*. Boole had dared to ask whether human reasoning could be written as algebra. If a statement was completely true, Boole assigned it the number $1$; if it was false, he assigned it the number $0$. Combining two statements with the word **AND** behaved like multiplication ($1 \times 1 = 1$, while $1 \times 0 = 0$); combining them with **OR** behaved like a saturating addition ($1 + 0 = 1$); and negating a statement with **NOT** simply flipped $1$ to $0$ and $0$ to $1$.

Boole himself had followed an even older trail. In 1703, the German polymath **Gottfried Wilhelm Leibniz** had presented a paper to the Royal Academy of Sciences in Paris titled *Explication de l'Arithmétique Binaire*. Leibniz marveled that every integer in the universe could be constructed using only two symbols—$1$ and $0$—and sketched a commemorative medallion showing light ($1$) emerging from the void ($0$) under the Latin motto *Omnibus ex nihilo ducendis sufficit unum* ("To derive everything from nothing, one suffices"). Yet for more than two centuries after Leibniz and eight decades after Boole, binary numbers and Boolean logic were regarded as philosophical curiosities—elegant parlor mathematics with no practical connection to machinery.

Staring at the racks of telephone relays in the MIT basement, young Claude Shannon saw the bridge that everyone else had missed:

- **Two switches wired in series** allow electrical current to pass only if Switch A is closed **AND** Switch B is closed ($A \cdot B$).
- **Two switches wired in parallel** allow current to pass if Switch A is closed **OR** Switch B is closed ($A + B$).
- **A normally closed relay contact** that opens when its electromagnet is energized acts as a physical **NOT** inverter ($\overline{A}$).

Every open or closed relay on a telephone switchboard was a physical embodiment of George Boole's two-valued algebra—and because Leibniz had shown that any number can be written in base-2 binary digits, circuits built from those same logical switches could add, subtract, compare, and store numbers at the speed of electricity!

In his 1937 MIT master's thesis—published in 1938 {{cite:shannon1938}} and later hailed by cognitive scientist Howard Gardner as "possibly the most important, and also the most famous, master's thesis of the century"—Shannon proved that any logical decision or arithmetic operation can be synthesized from binary switching gates. Even the fundamental unit of digital information—the **bit** (*binary digit*)—was coined by Shannon's Bell Labs colleague John Tukey and immortalized in Shannon's 1948 landmark paper *A Mathematical Theory of Communication*. Every microprocessor, memory cell, router, and spacecraft guidance computer built over the past nine decades traces its lineage directly to that summer in 1937 when logic and electricity became one.

### How Three Logic Gates Build Arithmetic Out of Pure Reason

To appreciate why Shannon's discovery was so revolutionary—and why computer-science students begin by studying truth tables—consider how a silicon chip adds two binary bits $A$ and $B$ without knowing anything about arithmetic. Suppose we want to compute $A + B$ in base 2, producing a two-bit answer consisting of a **Carry** bit (in the twos column, $2^1$) and a **Sum** bit (in the ones column, $2^0$):

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

Why does the number `255` look completely different when written as `255` in decimal, `11111111b` in binary, `377o` in octal, and `FFh` in hexadecimal—even though all four strings name the exact same quantity of objects?

When humans learned to count in antiquity, we naturally bundled objects in groups of ten (**Decimal**, base $b = 10$) because we carry ten fingers on our hands. When we write the decimal number $1,042_{10}$, we are secretly writing a polynomial in powers of $10$ from the inside out:

$$1,042_{10} = 1 \times 10^3 + 0 \times 10^2 + 4 \times 10^1 + 2 \times 10^0 = ((1 \times 10 + 0) \times 10 + 4) \times 10 + 2$$

Yet the choice of $10$ is purely biological. An electronic transistor does not have ten fingers. Trying to build a circuit that distinguishes ten different voltage levels ($0\text{ V}, 0.5\text{ V}, 1.0\text{ V}, \dots, 4.5\text{ V}$) is an engineering nightmare: a tiny thermal drift or static spark turns a $3$ into a $4$. Instead, silicon circuits use only two states—fully OFF ($0$) and fully ON ($1$). In **Binary** (base $b = 2$), each column as you move from right to left represents the next doubling power of two ($2^0 = 1,\; 2^1 = 2,\; 2^2 = 4,\; 2^3 = 8,\; 2^4 = 16,\; \dots$):

$$1042_{10} = 1024 + 16 + 2 = 1 \times 2^{10} + 1 \times 2^4 + 1 \times 2^1 = 10000010010_2$$

Binary is effortless for silicon, but exhausting for the human eye. Stare at a 36-bit binary word like `000011000000101010000000101000101101b` for ten seconds, and your working memory blurs. Remember George Miller's discovery from Chapter 2: human working memory can comfortably hold only four to seven chunks at a time, never thirty-six individual ones and zeros.

How do computer scientists compress long strings of bits into compact human-readable chunks without doing tedious division by $10$? By choosing number bases that are **exact powers of two**:

1. **Octal (`OCT`, Base $b = 8 = 2^3$):** Because $8 = 2^3$, every single octal digit (`0` through `7`) corresponds to an exact **3-bit triad** (`000` through `111`). To convert a binary number into octal in your head, you never divide—you simply slice the binary string into 3-bit groups from right to left and read off each triad.
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

Consider how effortlessly hexadecimal turns binary inspection into mental sight-reading. Suppose an engineer sees the 16-bit hexadecimal word `3C6Ah`. Without touching a calculator, you can read the four nibbles from left to right in three seconds:
- `3h` $= 2 + 1 \implies \mathtt{0011}$
- `Ch` ($12_{10}$) $= 8 + 4 \implies \mathtt{1100}$
- `6h` $= 4 + 2 \implies \mathtt{0110}$
- `Ah` ($10_{10}$) $= 8 + 2 \implies \mathtt{1010}$

Putting those four nibbles side by side gives `0011 1100 0110 1010b`. What took sixteen binary digits to write on silicon takes just four hexadecimal characters to hold in your mind. On the SC-32, pressing the **`{{key:BASE}}` menu** (`{{key:↰}}` + `{{key:×}}`) brings those four radix lenses (`{{key:HEX}}`, `{{key:DEC}}`, `{{key:OCT}}`, `{{key:BIN}}`) onto the top softkeys, re-rendering all four stack registers (`T, Z, Y, X`) on screen without altering the underlying 36-bit values—and while `{{key:HEX}}` is active, the top row of scientific keys (`{{key:√x}}` through `{{key:Σ+}}`) becomes a direct `A`–`F` hexadecimal keypad.

### The Golden Age of the 36-Bit Word: From NASA's IBM 7090 to MIT's PDP-10

If you open a modern laptop or smartphone, its processor registers are organized in multiples of 8-bit bytes—32 bits or 64 bits wide. Yet when the pioneers of scientific computing and artificial intelligence designed the legendary mainframes of the 1950s, 1960s, and 1970s, they converged on a word length that seems surprising today: **the 36-bit word**.

When **Katherine Johnson**, **Dorothy Vaughan**, and NASA's Flight Research Division computed the orbital trajectories for John Glenn's *Friendship 7* Mercury mission and the early Apollo lunar rendezvous studies (celebrated in Margot Lee Shetterly's *Hidden Figures*), the electronic mainframes humming inside Langley and Goddard were **IBM 7090** and **IBM 7094** computers—each built around 36-bit registers. When **John McCarthy** and **Marvin Minsky** founded the MIT Artificial Intelligence Laboratory and invented the **LISP** programming language—giving birth to modern symbolic AI (`CAR` and `CDR` literally stood for *"Contents of the Address part of Register"* and *"Contents of the Decrement part of Register"* on the 36-bit IBM 704)—they worked on 36-bit words. And when researchers at MIT, Stanford, CMU, and BBN built the first nodes of the **ARPANET** (the direct forerunner of the modern Internet), their beloved workhorse was Digital Equipment Corporation's **DEC PDP-10**, another classic 36-bit architecture.

Why did the greatest scientific and AI architects of the twentieth century fall in love with the number $36$?

Because in number theory, **$36$ is an abundant, highly composite number**—simultaneously divisible by $1, 2, 3, 4, 6, 9, 12,$ and $18$. Compare what happens when you slice a 32-bit word versus a 36-bit word across different number bases and data formats:

1. **Simultaneous Harmony of Octal and Hexadecimal:** A 32-bit word divides cleanly into eight 4-bit hexadecimal nibbles ($32 = 8 \times 4$), but leaves an awkward 2-bit orphan stub when grouped into 3-bit octal triads ($32 = 10 \times 3 + 2$). A **36-bit word** is the smallest practical computer word that divides with **zero remainder** into both **twelve 3-bit octal digits** ($36 = 12 \times 3$) *and* **nine 4-bit hexadecimal nibbles** ($36 = 9 \times 4$)!
2. **Ten Full Decimal Digits of Precision:** While a signed 32-bit integer overflows at $+2,147,483,647$ (barely nine full decimal digits—not even enough to hold a 10-digit telephone number or an unsigned 32-bit IPv4 broadcast address), $2^{36} = 68,719,476,736 \approx 6.87 \times 10^{10}$, providing **ten full decimal digits** of integer headroom.
3. **Symmetric Halves & Character Packing:** Thirty-six bits split cleanly into two symmetric 18-bit half-words ($36 = 2 \times 18$, allowing LISP and the PDP-10 to pack two memory pointers into a single register) or six 6-bit alphanumeric characters ($36 = 6 \times 6$).

When IBM introduced the commercial System/360 in 1964, Gene Amdahl and Fred Brooks standardized business computing around 8-bit bytes and 32-bit words to match commercial text printers. Yet anyone who has ever tried to enter an unsigned 32-bit hexadecimal address like `0xFFFFFFFF` ($4,294,967,295$) into a standard 32-bit programmer's calculator immediately hits a wall: because Bit 31 is the sign bit on a 32-bit machine, `0xFFFFFFFF` is either rejected as an overflow or misread as $-1$.

By adopting a classic **36-bit word** across all four stack registers ($T, Z, Y, X$), the SC-32 places its sign bit four positions higher at **Bit 35**. Every 32-bit unsigned memory address, IPv4 network mask (`0xFFFFFFFF`), or microcontroller register sits comfortably in Bits 31–0 as a strictly positive number, with **four extra bits above the 32-bit ceiling—three positive magnitude headroom bits (`Bits 34–32`, expanding positive capacity $8\times$) plus the dedicated sign bit at `Bit 35`** to catch overflow carries, checksum folds, and bit-shifts without ever losing a bit.

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

Think about what just happened: by representing $-3$ as $10,000 - 3 = 9997$, **ordinary forward addition** ($9997 + 0005 = \cancel{1}0002 \to \mathbf{0002}$) automatically computed $(-3) + 5 = +2$ with zero subtraction circuitry!

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
6. **Setting or Clearing an Individual Hardware Pin (Bit $k$):** Adding $+2^k$ to a register whose $k$-th bit is `0` flips Bit $k$ to `1` (bitwise `OR`), while subtracting $-2^k$ from a register whose $k$-th bit is `1` clears Bit $k$ to `0` (`AND NOT`) with zero carry or borrow into neighboring bits.

### Euclid's Remainder Ladder: Greatest Common Divisor (GCD) and Least Common Multiple (LCM)

Around 300 BCE in Alexandria, **Euclid** recorded in Book VII, Proposition 2 of his *Elements* what computer scientist Donald Knuth called the oldest nontrivial algorithm in human history: the **Euclidean Algorithm** for finding the **Greatest Common Divisor** $\operatorname{GCD}(a, b)$ of two integers. Suppose a digital signal processor runs one clock domain at $a = 1,071\text{ MHz}$ and another at $b = 462\text{ MHz}$, and you want the largest common reference frequency that divides both cleanly. Instead of factoring large integers into primes, Euclid noticed that any number dividing both $a$ and $b$ must also divide the remainder $R = a \bmod b$ left over from Euclidean division (`{{key:÷R}}`). Replacing $(a, b)$ with $(b, a \bmod b)$ and pressing `{{key:÷R}}` repeatedly marches down **Euclid's Remainder Ladder** in a handful of steps: $1071 = 2 \times 462 + 147 \longrightarrow 462 = 3 \times 147 + 21 \longrightarrow 147 = 7 \times 21 + 0$. The last non-zero remainder before `0` is the exact Greatest Common Divisor: $\operatorname{GCD}(1071, 462) = \mathbf{21}$!

On the SC-32, you can either step down Euclid's ladder manually with `{{key:÷R}}` or execute the entire ladder in a single keystroke inside the **`{{key:PARTS}}`** menu (`Right Shift {{key:↱}} above {{key:√x}}`), which places **`{{key:GCD}}`** (`{{key:LFU4}}`) and **`{{key:LCM}}`** (`{{key:LFU5}}`) side by side alongside `{{key:IP}}`, `{{key:FP}}`, `{{key:ABS}}`, and `{{key:SGN}}`. Once $\operatorname{GCD}(a, b)$ is known, dividing the product $|a \cdot b|$ by $\operatorname{GCD}(a, b)$ gives the **Least Common Multiple**:

$$\operatorname{LCM}(a, b) = \frac{|a \cdot b|}{\operatorname{GCD}(a, b)}$$

Together, `{{key:GCD}}` and `{{key:LCM}}` solve three everyday problems across computer engineering and mechanics: reducing gear-tooth or aspect ratios ($1920 \times 1080$ divided by $\operatorname{GCD}(1920, 1080) = 120$ gives the $16:9$ display ratio), finding the exact cycle period $\operatorname{LCM}(T_1, T_2)$ when two asynchronous timer buses realign in phase, and verifying that a public exponent $e$ is coprime to Euler's totient ($\operatorname{GCD}(e, \varphi(n)) = 1$) in **RSA public-key cryptography**.

### Real-World Bitwise Engineering: Subnet Masks, RGB Pixels, Base64, Endianness & IEEE-754 Floats

Once you can read hexadecimal nibbles and cleave binary words from the inside out at powers of two ($2^k$), five mysteries of modern technology suddenly become transparent:

1. **How Internet Routers Slice IPv4 Addresses (`CIDR` Subnetting):**
   Every IPv4 address on the Internet—such as `192.168.10.45`—is really a single 32-bit integer written for human convenience as four 8-bit decimal bytes (**octets**, each ranging from `0` to `255`, or `00h` to `FFh`). In hexadecimal, `192.168.10.45` packs cleanly into `C0A80A2Dh` (`192` $= \mathtt{C0h}$, `168` $= \mathtt{A8h}$, `10` $= \mathtt{0Ah}$, `45` $= \mathtt{2Dh}$):

| Field | Octet 1 (`192` / `C0h`) | Octet 2 (`168` / `A8h`) | Octet 3 (`10` / `0Ah`) | Octet 4 (`45` / `2Dh`) |
| :--- | :---: | :---: | :---: | :---: |
| **Host IP Bits** | `11000000` | `10101000` | `00001010` | `00101101` |
| **Subnet Mask (`/24`)** | `11111111` (Net) | `11111111` (Net) | `11111111` (Net) | `00000000` (Host) |
| **Aligned Network ID** | `11000000` (`192`) | `10101000` (`168`) | `00001010` (`10`) | `00000000` (`0`) |

   When a home or campus network uses a `/24` subnet mask (`255.255.255.0` $= \mathtt{FFFFFF00h}$), the top 24 bits identify the **Network Prefix** (`192.168.10.0` $= \mathtt{C0A80A00h}$) and the bottom $32 - 24 = 8\text{ bits}$ ($2^8 = 256_{10} = \mathtt{100h}$) identify the **Host Offset** (`45` $= \mathtt{2Dh}$). Dividing `C0A80A2Dh` by $\mathtt{100h}$ cleaves the 32-bit address right at the 8-bit host boundary. Similarly, on a smaller `/28` office subnet (`255.255.255.240`), only the bottom $32 - 28 = 4\text{ bits}$ ($2^4 = 16$ addresses per block) belong to hosts: dividing host octet `205` by block size `16` gives integer quotient $12$ and remainder $13$ ($205 = 12 \times 16 + 13$), revealing immediately that host `205` is the $13\text{th}$ machine inside the `/28` network block starting at $12 \times 16 = \mathbf{192}$.

2. **Packing Color Channels & Base64 Characters by Horner's Method:**
   How does a smartwatch or microcontroller color display pack three separate Red, Green, and Blue brightness numbers into a single 16-bit memory word (`RGB565`)? Because the cones in the human retina are most sensitive to subtle shades of green, `RGB565` gives **5 bits** ($0\dots 31$) to Red in `Bits [15:11]`, **6 bits** ($0\dots 63$) to Green in `Bits [10:5]`, and **5 bits** ($0\dots 31$) to Blue in `Bits [4:0]`:

| Channel Allocation | Bit Positions | Binary Field | Shifted Hex Value |
| :--- | :---: | :---: | :---: |
| **Red (5-bit)** | Bits `15–11` | `11111` (`1Fh × 800h`) | `F800h` |
| **Green (6-bit)** | Bits `10–5` | `010101` (`15h × 20h`) | `02A0h` |
| **Blue (5-bit)** | Bits `4–0` | `00110` (`06h`) | `0006h` |
| **Combined RGB565 Word** | Bits `15–0` | `1111101010100110` | **`FAA6h`** |

   Packing $(R_5, G_6, B_5) = (\mathtt{1Fh}, \mathtt{15h}, \mathtt{06h})$ into a single 16-bit integer is simply $(R_5 \times 2^{11}) + (G_6 \times 2^5) + B_5 = \mathtt{FAA6h}$—and unpacking any 16-bit pixel back into its three color channels is just two Euclidean divisions at $2^{11} = \mathtt{800h}$ and $2^5 = \mathtt{20h}$.
   The exact same bit-slicing trick powers **Base64 encoding** across the web: to send binary attachments over text-only email protocols, Base64 welds three 8-bit ASCII bytes (such as `"Man"` $= \mathtt{4D616Eh}$, $3 \times 8 = 24\text{ bits}$) into a single 24-bit integer and slices it at $2^{18} = \mathtt{40000h}$, $2^{12} = \mathtt{1000h}$, and $2^6 = \mathtt{40h}$ into four 6-bit numbers ($19, 22, 5, 46$), which map to the four printable letters **`TWFu`**.

3. **Big-Endian vs. Little-Endian Byte Order & Internet Checksums:**
   In 1980, computer scientist Danny Cohen borrowed the terms **Big-Endian** and **Little-Endian** from Jonathan Swift's *Gulliver's Travels* (where two empires went to war over whether to crack a soft-boiled egg at the big end or the little end) to describe how computers store multi-byte integers in memory. Network cables transmit bytes Big-Endian (`12345678h`, most-significant byte `12h` first), whereas x86 and ARM processors store bytes Little-Endian (`78563412h`, least-significant byte `78h` first). And when routers verify that a packet was not corrupted in flight, they use RFC 1071 **16-bit one's-complement addition with end-around carry** {{cite:knuth1997}}—dividing the 32-bit accumulated sum by $2^{16} = \mathtt{10000h}$ and adding the upper carry quotient right back into the lower 16-bit remainder—because end-around carry produces the exact same checksum on both Big-Endian and Little-Endian machines.

4. **How IEEE-754 Packs Scientific Notation into 32 and 64 Bits:**
   Finally, how does a computer store a real floating-point number like $-6.25$ inside a 32-bit integer register? William Kahan's **IEEE-754 standard** {{cite:ieee754_2019}} writes the number in base-2 scientific notation:

$$-6.25_{10} = -(4 + 2 + 0.25) = -110.01_2 = (-1)^1 \times 2^2 \times 1.1001_2$$

   Because every non-zero normalized binary number begins with a leading `1.` before the binary point, IEEE-754 does not even waste a bit storing that leading `1`. Instead, a 32-bit single-precision float (`binary32`) packs **1 Sign bit $S$** in `Bit 31` (`1` for negative), an **8-bit Biased Exponent $E = e + 127$** in `Bits [30:23]` ($2 + 127 = 129_{10} = \mathtt{81h}$), and the **23-bit Fractional Mantissa** after the hidden `1.` in `Bits [22:0]` (`.1001000..._2` $= \mathtt{480000h}$), forming the 32-bit word **`0xC0C80000`**. Cleaving `C0C80000h` at bit 23 ($2^{23} = \mathtt{800000h}$) and bit 8 ($2^8 = \mathtt{100h}$) via `{{key:÷R}}` unpacks the mantissa, biased exponent, and sign bit onto the stack in two moves.

---

## Combinatorics (PROB), Cryptographic Keyspaces, and the Birthday Collision Paradox

How many distinct states can a digital register, a network topology, or a cryptographic cipher assume—and how quickly do two random hashes collide? In discrete mathematics and computer science, counting finite state spaces rests on the four functions inside the SC-32's **`{{key:PROB}}` menu** (`Right Shift {{key:↱}} above {{key:eˣ}}`): **combinations `{{key:Cn,r}}`**, **permutations `{{key:Pn,r}}`**, **factorials `{{key:x!}}`**, and the uniform pseudo-random generator **`{{key:RAND}}`**.

Suppose you have $n$ distinct items—say $n = 16$ hexadecimal digits (`0`–`F`) or $n = 12$ server racks—and you choose $r$ of them without replacement:
* **Ordered Permutations (`{{key:Pn,r}}`):** When the *order* of selection matters (such as assigning $r = 4$ distinct hexadecimal nibbles to a 4-stage pipeline, or ordering $r = 5$ packet routes out of $n = 12$), there are $n$ choices for the first slot, $n - 1$ for the second, down to $n - r + 1$ for the $r$-th slot:
  $$P(n, r) = n(n - 1)\cdots(n - r + 1) = \frac{n!}{(n - r)!}$$
* **Unordered Combinations (`{{key:Cn,r}}`):** When order does *not* matter (such as choosing any subset of $r = 5$ storage drives out of $n = 12$ for a RAID parity group, or wiring every pair of $r = 2$ routers among $n = 7$ ARPANET nodes), we divide $P(n, r)$ by the $r!$ ways to rearrange the chosen subset—giving Blaise Pascal's binomial coefficient:
  $$C(n, r) = \binom{n}{r} = \frac{P(n, r)}{r!} = \frac{n!}{r!\,(n - r)!}$$

That ratio between $P(n, r)$ and $n^r$ unlocks one of the most counterintuitive truths in probability and cybersecurity: **Richard von Mises's Birthday Paradox (1939)**. Ask a roomful of engineers how many people ($k$) must gather in a room before there is at least a $50\%$ chance that two people share the same birthday (out of $N = 365$ days in a year). Intuition whispers $\frac{365}{2} \approx 183\text{ people}$.

Intuition is off by nearly an order of magnitude! Why? Because we are not asking whether someone shares *your specific* birthday; we are asking whether **any** pair among the $\binom{k}{2} = \frac{k(k-1)}{2}$ possible pairs of people in the room matches. To find the exact probability of a collision, compute the complementary probability $P_{\text{unique}}$ that all $k$ people have *different* birthdays: the first person has $365$ free days, the second has $364$, the third has $363$, and the $k$-th has $(365 - k + 1)$—which is simply the permutation $P(365, k)$ divided by $365^k$:

$$P(\text{at least one collision}) = 1 - \frac{P(365, k)}{365^k} \approx 1 - \exp\!\left(-\frac{k(k - 1)}{2 \times 365}\right)$$

At just **$k = 23\text{ people}$**, the number of pairs reaches $\binom{23}{2} = 253\text{ pairs}$, and $1 - \frac{P(365, 23)}{365^{23}} = \mathbf{0.507297}$ (**$50.73\%$**)! In computer science, that $\sqrt{N}$ scaling is known as the **Birthday Bound**: if a $b$-bit hash function or database UUID has $N = 2^b$ possible values, random collisions do not wait until $2^b$ records are written—they become likely after roughly **$\sqrt{2^b} = 2^{b/2}$ operations** (just $2^{16} = 65,536$ packets for a 32-bit CRC, or $2^{32} \approx 4.29 \times 10^9$ blocks for a 64-bit cipher), which is why modern cryptographic hashes like SHA-256 use $b = 256\text{ bits}$ so that the birthday bound sits safely out of reach at $2^{128} \approx 3.4 \times 10^{38}$!

---

## On the Stack: 36-Bit Bases, Boolean Logic & Bitwise Workbench

Whether converting bases, rolling a 36-bit two's-complement odometer across zero, snapping an IPv4 address to its subnet boundary, packing RGB565 color channels, or cracking open an IEEE-754 floating-point word, you always start with a word in hand, cleave it at a power-of-two boundary $2^k$ into an upper quotient and a lower remainder, and recombine the pieces from the inside out. On the StackCalc SC-32, the Euclidean division key (`{{key:÷R}}`) performs that exact cleavage in a single keystroke—placing the upper quotient $\lfloor Y / X \rfloor$ in Register `X` and the lower remainder $Y \bmod X$ in Register `Y`—while `{{key:BASE}}` switches seamlessly among `{{key:DEC}}`, `{{key:HEX}}`, `{{key:OCT}}`, and `{{key:BIN}}` without ever disturbing the four stack registers (`T, Z, Y, X`). Let us step onto the workbench and put this 36-bit engine through its paces.

{{res:sc32_hex_255:screenshot|Decimal 255 converted in place to hexadecimal FFh on the SC-32 transflective display while preserving all four stack registers.}}

### Live Radix Lenses (`DEC`, `HEX`, `OCT`, `BIN`) & Direct Hex Entry

Following the classic HP-32SII philosophy, the SC-32 `{{key:BASE}}` menu (accessed via Left Shift `{{key:↰}}` on the multiplication key `{{key:×}}`, Row 5, Column 3) treats number bases as **live display and entry lenses** over the same underlying 36-bit registers:

| Base System | Keystroke | Screen Suffix | Allowed Character Digits | Example Formatted Display |
| :--- | :--- | :---: | :--- | :--- |
| **Decimal** | `{{key:BASE}} {{key:DEC}}` | *(none)* | `0` through `9` | `1042` |
| **Hexadecimal** | `{{key:BASE}} {{key:HEX}}` | `h` | `0` through `9`, `A` through `F` | `412h` |
| **Octal** | `{{key:BASE}} {{key:OCT}}` | `o` | `0` through `7` | `2022o` |
| **Binary** | `{{key:BASE}} {{key:BIN}}` | `b` | `0` and `1` | `10000010010b` |

Switching between base modes **never destroys, alters, or shifts the values in the operational stack ($X, Y, Z, T$)**. If Register $X$ holds `255` in Decimal mode, pressing `{{key:BASE}} {{key:HEX}}` instantly re-renders the register as `FFh`, pressing `{{key:BASE}} {{key:OCT}}` shows `377o`, and pressing `{{key:BASE}} {{key:BIN}}` reveals all eight asserted bits as `11111111b`.

When Hexadecimal mode (`{{key:HEX}}`) is active, the top row of primary scientific keys (Row 1, Columns 0 through 5) maps directly to the printed alpha legends $A$ through $F$: `{{key:√x}}` enters $\mathbf{A}$ ($10_{10}$), `{{key:eˣ}}` enters $\mathbf{B}$ ($11_{10}$), `{{key:LN}}` enters $\mathbf{C}$ ($12_{10}$), `{{key:yˣ}}` enters $\mathbf{D}$ ($13_{10}$), `{{key:1/x}}` enters $\mathbf{E}$ ($14_{10}$), and `{{key:Σ+}}` enters $\mathbf{F}$ ($15_{10}$). To enter the classic debugging magic number `0xDEADBEEF`, simply key `{{key:yˣ}} {{key:1/x}} {{key:√x}} {{key:yˣ}} {{key:eˣ}} {{key:1/x}} {{key:1/x}} {{key:Σ+}}`. *(In the workbench tables below, hexadecimal literals such as `C0A80A2D` or `1F` are written in compact hex notation for readability; on the physical keypad in `{{key:HEX}}` mode, always enter the hex digits `A`–`F` using that top row `{{key:√x}}`–`{{key:Σ+}}`.)* Whenever you want to apply scientific functions (`{{key:√x}}`, `{{key:LN}}`, `{{key:yˣ}}`) to a hexadecimal value, switch back to Decimal mode (`{{key:BASE}} {{key:DEC}}`) first so the top-row keys resume their mathematical roles.

Because the SC-32 preserves all four stack registers across base changes, you can also mix radices right in the middle of a calculation without jotting down a single intermediate number: to add a hexadecimal base offset $3\text{A}7_{16}$ to an octal permission mask $452_8$ and read the sum in decimal, switch to Hex (`{{key:BASE}} {{key:HEX}}`) and enter `3 {{key:√x}} 7 {{key:ENTER}}` ($3\text{A}7_{16} = 935_{10}$), switch directly to Octal (`{{key:BASE}} {{key:OCT}}`) and add `452 {{key:+}}` ($2261_8$), and then switch to Decimal (`{{key:BASE}} {{key:DEC}}`) to read the combined total **$1,201_{10}$** in Register $X$.

### Euclidean Remainder Extraction (`÷R`) & IPv4 Subnet Partitioning

Suppose a DMA controller accesses byte offset $12,345$ inside a flash memory array organized into 16-byte rows ($N = Q \cdot D + R$). Working in decimal (`{{key:DEC}}`) mode, keying `{{res:sc32_10_computer_science_bases_seq_01:keys}}` computes $12,345 \div 16$ with simultaneous quotient and remainder, placing the whole quotient $Q = \mathbf{771}$ (the 16-byte row index) in Register $X$ and the remainder $R = 12345 \bmod 16 = \mathbf{{{res:sc32_10_computer_science_bases_seq_01:value}}}$ (the byte offset within row $771$) in Register $Y$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `12345 {{key:ENTER}}` | 0 | 0 | 12345 | 12345 | Load integer dividend $12,345$ |
| `16 {{key:÷R}}` | 0 | 0 | **9** | **771** | Quotient $Q=771$ in Register X, remainder $R=9$ in Register Y |
| `{{key:x⇄y}}` | 0 | 0 | 771 | **9** | Swap registers to access remainder $9$ directly |

Now apply that exact `{{key:÷R}}` split to an IPv4 packet addressed to final host octet `205` on a `/28` VLAN interface (`255.255.255.240`, block stride $2^{32-28} = 16$). Working in `{{key:DEC}}` mode, keying `{{res:sc32_10_computer_science_bases_seq_03:keys}}` divides `205` by `16` via `{{key:÷R}}` (placing block index `12` in Register $X$ and host offset `13` in Register $Y$) and multiplies by `16` to snap directly to the aligned `/28` subnet boundary **`{{res:sc32_10_computer_science_bases_seq_03:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `205` | 0 | 0 | 0 | 205 | Enter final host octet `205` |
| `{{key:ENTER}}` | 0 | 0 | 205 | 205 | Stage `205` in Register Y |
| `16 {{key:÷R}}` | 0 | 0 | 13 | 12 | Cleave at stride $16$: block `12` in X, host offset `13` in Y |
| `16 {{key:×}}` | 0 | 0 | 13 | 192 | Multiply by $16$ for aligned `/28` network ID `192` |

To partition a full 32-bit IPv4 workstation address `192.168.10.45` (`C0A80A2Dh`) on a `/24` subnet ($2^{32-24} = 2^8 = 256_{10} = \text{100h}$), switch to `{{key:HEX}}` mode and execute three steps:
* **Extract the `/24` Network Base Address:** Keying `{{res:sc32_10_computer_science_bases_seq_04:keys}}` cleaves and aligns the `/24` network address **`{{res:sc32_10_computer_science_bases_seq_04:value}}`** (`192.168.10.0`) while leaving the host offset (`2Dh`) in Register $Y$.
* **Isolate the Host Wildcard Mask:** Subtracting the `/24` netmask from the all-ones broadcast word via `{{res:sc32_10_computer_science_bases_seq_05:keys}}` isolates the 8-bit wildcard mask **`{{res:sc32_10_computer_science_bases_seq_05:value}}`** (`0.0.0.255`).
* **Compute the Subnet Broadcast Address:** Adding that wildcard mask to the aligned network address via `{{res:sc32_10_computer_science_bases_seq_06:keys}}` produces the `/24` broadcast address **`{{res:sc32_10_computer_science_bases_seq_06:value}}`** (`192.168.10.255`):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `C0A80A2D` | `0h` | `0h` | `0h` | `C0A80A2Dh` | Enter packed 32-bit IPv4 address `192.168.10.45` |
| `{{key:ENTER}}` | `0h` | `0h` | `C0A80A2Dh` | `C0A80A2Dh` | Duplicate address into Register Y |
| `100 {{key:÷R}}` | `0h` | `0h` | `2Dh` | `C0A80Ah` | Split `/24` prefix `C0A80Ah` into X and host `2Dh` into Y |
| `100 {{key:×}}` | `0h` | `0h` | `2Dh` | `C0A80A00h` | Align `/24` network base address `192.168.10.0` |
| `FF {{key:+}}` | `0h` | `0h` | `2Dh` | `C0A80AFFh` | Add host wildcard `FFh` for broadcast `192.168.10.255` |

### 36-Bit Two's Complement Odometer Seams & Hardware Bit-Fields

We can inspect the two rollover seams of the 36-bit two's complement odometer directly on the stack in `{{key:HEX}}` mode:
* **Signed Positive Overflow Seam (`+Max + 1 → -Min`):** Load the largest positive signed 36-bit integer `7FFFFFFFFh` ($+2^{35} - 1 = +34,359,738,367_{10}$) and add `1` via `{{res:sc32_10_computer_science_bases_seq_33:keys}}` to roll across the sign boundary to **`{{res:sc32_10_computer_science_bases_seq_33:value}}`** ($-34,359,738,368_{10}$).
* **Zero Underflow Seam (`0 - 1 → -1`):** Start at `0` and subtract `1` via `{{res:sc32_10_computer_science_bases_seq_34:keys}}` to roll backward across zero to **`{{res:sc32_10_computer_science_bases_seq_34:value}}`** ($-1_{10}$, all 36 bits asserted):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `7FFFFFFFF {{key:ENTER}}` | `0h` | `0h` | `7FFFFFFFFh` | `7FFFFFFFFh` | Load maximum signed positive 36-bit bound |
| `1 {{key:+}}` | `0h` | `0h` | `0h` | **`800000000h`** | Overflow rolls over to minimum negative bound |
| `0 {{key:ENTER}} 1 {{key:-}}` | `0h` | `0h` | `800000000h` | **`FFFFFFFFFh`** | Underflow to $-1_{10}$; all 36 bits set (`FFFFFFFFFh`) |

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

*(Note that for right bit-shifts in `{{key:DEC}}` mode, `{{key:÷R}}` is preferred over `{{key:÷}}` because `{{key:÷}}` retains fractional decimal digits in Decimal mode, whereas `{{key:÷R}}` always truncates directly to the integer quotient $\lfloor X / 2^k \rfloor$ in every base!)*

Suppose a 32-bit GPIO direction register (`GPIO_DIR`) holds `0x00001804` (Pins 2, 11, and 12 configured as outputs, Pin 5 currently `0`). To set Pin 5 ($2^5 = 32_{10} = \text{20h}$) in `{{key:HEX}}` mode, keying `{{res:sc32_10_computer_science_bases_seq_11:keys}}` produces **`{{res:sc32_10_computer_science_bases_seq_11:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1804` | `0h` | `0h` | `0h` | `1804h` | Enter current `GPIO_DIR` register value `1804h` |
| `{{key:ENTER}}` | `0h` | `0h` | `1804h` | `1804h` | Stage `1804h` in Register Y |
| `20` | `0h` | `0h` | `1804h` | `20h` | Enter Bit 5 positional weight $2^5 = \text{20h}$ |
| `{{key:+}}` | `0h` | `0h` | `0h` | `1824h` | Assert Bit 5 without carry (`1824h`) |

Similarly, if a port output register holds `0x00000017` ($0001\,0111_2$) with a heartbeat line on Bit 2 ($2^2 = \text{4h}$), working in `{{key:HEX}}` mode lets us toggle and audit individual status bits without disturbing neighboring pins:
* **Clear & Restore a Heartbeat Pin:** Keying `{{res:sc32_10_computer_science_bases_seq_13:keys}}` clears Bit 2 to produce **`{{res:sc32_10_computer_science_bases_seq_13:value}}`**, and adding `4` back via `{{res:sc32_10_computer_science_bases_seq_14:keys}}` (or `{{key:LASTX}} {{key:+}}`) restores **`{{res:sc32_10_computer_science_bases_seq_14:value}}`**.
* **Spacecraft Telemetry Fault Mask (`XOR` via Borrow-Free Subtraction):** When comparing a spacecraft downlink status word `0x5F5A` against a nominal baseline mask `0x5A50` whose asserted bits are a subset of the active word (so that subtracting `5A50h` triggers zero column borrows and acts identically to bitwise `XOR`), keying `{{res:sc32_10_computer_science_bases_seq_36:keys}}` in `{{key:HEX}}` mode isolates the newly tripped fault-bit mask **`{{res:sc32_10_computer_science_bases_seq_36:value}}`** ($\mathbf{10100001010\text{b}}$ in `{{key:BIN}}`, revealing a Hamming weight of **$4\text{ bits}$** at positions 1, 3, 8, and 10).

To extract a middle bit-field—such as Bits [7:4] (`6h`) from a 16-bit ADC configuration register holding `0x3C6A`—work in `{{key:HEX}}` mode in two steps:
* **Step 1 — Strip Upper Byte (`mod 100h`):** Key `{{res:sc32_10_computer_science_bases_seq_15:keys}}` to isolate the lower 8-bit byte **`{{res:sc32_10_computer_science_bases_seq_15:value}}`**.
* **Step 2 — Shift Right by 4 Bits (`÷ 10h`):** Divide by $2^4 = \text{10h}$ via `{{res:sc32_10_computer_science_bases_seq_16:keys}}` to isolate Bits [7:4] = **`{{res:sc32_10_computer_science_bases_seq_16:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3C6A {{key:ENTER}}` | `0h` | `0h` | `3C6Ah` | `3C6Ah` | Stage 16-bit ADC register word `3C6Ah` |
| `100 {{key:÷R}}` | `0h` | `0h` | `6Ah` | `3Ch` | Split upper byte `3Ch` into X and lower byte `6Ah` into Y |
| `{{key:x⇄y}}` | `0h` | `0h` | `3Ch` | `6Ah` | Swap lower byte `6Ah` (Bits [7:0]) into Register X |
| `10 {{key:÷}}` | `0h` | `0h` | `3Ch` | `6h` | Shift right by 4 bits (`÷ 10h`) to isolate Bits [7:4] = `6h` |

### Packing RGB565 Pixels, Slicing Base64 Sextets & Reversing Endianness

Let us now pack 5-bit Red (`1Fh`), 6-bit Green (`15h`), and 5-bit Blue (`06h`) into a single 16-bit `RGB565` display word in `{{key:HEX}}` mode:
* **Shift Red into Bits [15:11]:** Multiply `1Fh` by $2^{11} = 800\text{h}$ via `{{res:sc32_10_computer_science_bases_seq_19:keys}}` to obtain **`{{res:sc32_10_computer_science_bases_seq_19:value}}`**.
* **Shift Green into Bits [10:5]:** Multiply `15h` by $2^5 = 20\text{h}$ via `{{res:sc32_10_computer_science_bases_seq_20:keys}}` to obtain **`{{res:sc32_10_computer_science_bases_seq_20:value}}`**, and press `{{key:+}}` to merge Red and Green (`FAA0h`).
* **Add Blue in Bits [4:0]:** Add `06h` via `{{res:sc32_10_computer_science_bases_seq_21:keys}}` to complete the packed 16-bit pixel word **`{{res:sc32_10_computer_science_bases_seq_21:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1F {{key:ENTER}}` | `0h` | `0h` | `1Fh` | `1Fh` | Stage 5-bit Red channel `1Fh` ($31_{10}$) |
| `800 {{key:×}}` | `0h` | `0h` | `0h` | `F800h` | Shift Red left 11 bits (`× 800h`) into Bits [15:11] |
| `15 {{key:ENTER}}` | `0h` | `F800h` | `15h` | `15h` | Stage 6-bit Green channel `15h` ($21_{10}$); Red lifts to Z |
| `20 {{key:×}}` | `0h` | `0h` | `F800h` | `2A0h` | Shift Green left 5 bits (`× 20h`) into Bits [10:5] |
| `{{key:+}}` | `0h` | `0h` | `0h` | `FAA0h` | Combine shifted Red and Green channels (`FAA0h`) |
| `6 {{key:+}}` | `0h` | `0h` | `0h` | `FAA6h` | Add 5-bit Blue channel `06h` for packed `RGB565` word `FAA6h` |

Conversely, given a packed 16-bit RGB565 pixel `0xF38E` in `{{key:HEX}}` mode, keying `F38E {{key:ENTER}} 800 {{key:÷R}} {{key:x⇄y}} 20 {{key:÷R}}` unpacks all three color channels onto the visible stack in one pass: Red in Register $Z$ (`1Eh` $= 30_{10}$), Green in Register $X$ (`1Ch` $= 28_{10}$), and Blue in Register $Y$ (`Eh` $= 14_{10}$).

In the same way, to slice the 24-bit ASCII string `"Man"` (`4D616Eh`) into four 6-bit Base64 sextet indices in `{{key:HEX}}` mode using divisors $2^{18} = \text{40000h}$, $2^{12} = \text{1000h}$, and $2^6 = \text{40h}$:
* **Sextet 1 (Bits [23:18]):** Keying `{{res:sc32_10_computer_science_bases_seq_29:keys}}` extracts **`{{res:sc32_10_computer_science_bases_seq_29:value}}`** ($19_{10} \implies$ Base64 `'T'`).
* **Sextet 2 (Bits [17:12]):** Keying `{{res:sc32_10_computer_science_bases_seq_30:keys}}` extracts **`{{res:sc32_10_computer_science_bases_seq_30:value}}`** ($22_{10} \implies$ Base64 `'W'`).
* **Sextet 3 (Bits [11:6]):** Keying `{{res:sc32_10_computer_science_bases_seq_31:keys}}` extracts **`{{res:sc32_10_computer_science_bases_seq_31:value}}`** ($5_{10} \implies$ Base64 `'F'`).
* **Sextet 4 (Bits [5:0]):** Keying `{{res:sc32_10_computer_science_bases_seq_32:keys}}` extracts **`{{res:sc32_10_computer_science_bases_seq_32:value}}`** ($46_{10} \implies$ Base64 `'u'`), confirming that `"Man"` encodes to **`TWFu`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `4D616E {{key:ENTER}} 40000 {{key:÷}}` | `0h` | `0h` | `0h` | **`13h`** | Sextet 1: `4D616Eh >> 18 = 13h` ($19_{10} \implies \mathbf{T}$) |
| `4D616E {{key:ENTER}} 40000 {{key:÷R}} {{key:x⇄y}} 1000 {{key:÷}}` | `13h` | `13h` | `13h` | **`16h`** | Sextet 2: remainder `>> 12 = 16h` ($22_{10} \implies \mathbf{W}$) |
| `4D616E {{key:ENTER}} 1000 {{key:÷R}} {{key:x⇄y}} 40 {{key:÷}}` | `16h` | `16h` | `4D6h` | **`5h`** | Sextet 3: remainder `>> 6 = 5h` ($5_{10} \implies \mathbf{F}$) |
| `4D616E {{key:ENTER}} 40 {{key:÷R}} {{key:x⇄y}}` | `4D6h` | `5h` | `13585h` | **`2Eh`** | Sextet 4: lower 6-bit remainder = `2Eh` ($46_{10} \implies \mathbf{u}$) |

*(Single-Entry `÷R` Cascade: Chaining `4D616E {{key:ENTER}} 40000 {{key:÷R}} {{key:x⇄y}} 1000 {{key:÷R}} {{key:x⇄y}} 40 {{key:÷R}}` unpacks all four Base64 indices across the four stack registers—`13h` in $T$, `16h` in $Z$, `2Eh` in $Y$, and `5h` in $X$—with `4D616E` keyed only once.)*

When converting a 4-byte Big-Endian network word `0x12345678` into Little-Endian byte order `0x78563412` in `{{key:HEX}}` mode, we isolate each byte and shift it to its mirrored lane before summing with `{{key:+}} {{key:+}} {{key:+}}`:
* **Byte 0 $\to$ Byte 3:** Shift `78h` left 24 bits via `{{res:sc32_10_computer_science_bases_seq_41:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_41:value}}`**.
* **Byte 1 $\to$ Byte 2:** Shift `56h` left 16 bits via `{{res:sc32_10_computer_science_bases_seq_42:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_42:value}}`**.
* **Byte 2 $\to$ Byte 1:** Shift `34h` left 8 bits via `{{res:sc32_10_computer_science_bases_seq_43:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_43:value}}`**.
* **Byte 3 $\to$ Byte 0:** Extract MSB `12h` via `{{res:sc32_10_computer_science_bases_seq_44:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_44:value}}`**, and sum all four lanes into **`78563412h`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `78 {{key:ENTER}} 1000000 {{key:×}}` | `0h` | `0h` | `0h` | `78000000h` | Shift LSB `78h` left 24 bits into Byte 3 (`78000000h`) |
| `56 {{key:ENTER}} 10000 {{key:×}}` | `0h` | `0h` | `78000000h` | `560000h` | Shift `56h` left 16 bits into Byte 2 (`560000h`) |
| `{{key:+}}` | `0h` | `0h` | `0h` | `78560000h` | Merge Bytes 3 and 2 (`78560000h`) |
| `34 {{key:ENTER}} 100 {{key:×}}` | `0h` | `0h` | `78560000h` | `3400h` | Shift `34h` left 8 bits into Byte 1 (`3400h`) |
| `{{key:+}}` | `0h` | `0h` | `0h` | `78563400h` | Merge Bytes 3, 2, and 1 (`78563400h`) |
| `12` | `0h` | `0h` | `78563400h` | `12h` | Enter MSB `12h` into Byte 0 position |
| `{{key:+}}` | `0h` | `0h` | `0h` | `78563412h` | Complete Little-Endian word `78563412h` |

### RFC 1071 Checksums, Circular Rotations (`ROL`), UART Dividers & IEEE-754 Unpacking

Suppose summing the 16-bit words of an IPv4 packet header in a 32-bit accumulator yields $\text{Header Sum} = 2653\text{D}_{16}$. In `{{key:HEX}}` mode, loading `2653D {{key:ENTER}}` and dividing by $2^{16} = \text{10000h}$ via `10000 {{key:÷R}}` places the upper carry (`2h`) in Register $X$ and the lower 16 bits (`653Dh`) in Register $Y$; pressing `{{key:+}}` folds the end-around carry (`653Fh`), and subtracting from `FFFFh` via `FFFF {{key:x⇄y}} {{key:-}}` yields the one's-complement wire checksum **`9AC0h`** ($39,616_{10}$ in `{{key:DEC}}`):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2653D {{key:ENTER}}` | `0h` | `0h` | `2653Dh` | `2653Dh` | Load 32-bit accumulated IPv4 header sum `2653Dh` |
| `10000 {{key:÷R}}` | `0h` | `0h` | `653Dh` | `2h` | Split upper 16-bit carry `2h` into X and low word `653Dh` into Y |
| `{{key:+}}` | `0h` | `0h` | `0h` | `653Fh` | Fold end-around carry into 16-bit sum (`653Fh`) |
| `FFFF` | `0h` | `0h` | `653Fh` | `FFFFh` | Stage all-ones 16-bit mask `FFFFh` |
| `{{key:x⇄y}}` | `0h` | `0h` | `FFFFh` | `653Fh` | Swap folded sum into X beneath `FFFFh` in Y |
| `{{key:-}}` | `0h` | `0h` | `0h` | `9AC0h` | One's-complement RFC 1071 header checksum `9AC0h` |

Similarly, to execute a circular 1-bit left rotation (`ROL 1`) on the 8-bit byte `0x85` ($10000101_2 \implies 00001011_2 = \text{0Bh}$) in `{{key:HEX}}` mode at the 8-bit boundary $2^8 = \text{100h}$:
* **Step 1 — Shift Left by 1 Bit:** Double the byte via `{{res:sc32_10_computer_science_bases_seq_50:keys}}` to obtain **`{{res:sc32_10_computer_science_bases_seq_50:value}}`**.
* **Step 2 — Split Overflow Carry at `100h`:** Cleave the 8-bit remainder (`0Ah` in $Y$) and overflow carry (`1h` in $X$) via `{{res:sc32_10_computer_science_bases_seq_51:keys}}` ($\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_51:value}}`**).
* **Step 3 — Fold Carry into LSB:** Add the carry bit back into Bit 0 via `{{res:sc32_10_computer_science_bases_seq_52:keys}}` to complete the rotated byte **`{{res:sc32_10_computer_science_bases_seq_52:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `85 {{key:ENTER}} 2 {{key:×}}` | `0h` | `0h` | `0h` | **`10Ah`** | Shift byte left by 1 bit ($85\text{h} \times 2 = 10\text{Ah}$) |
| `100 {{key:÷R}}` | `0h` | `0h` | `Ah` | **`1h`** | Extract carry bit ($X=1\text{h}$) and rotated byte ($Y=\text{Ah}$) |
| `{{key:+}}` | `0h` | `0h` | `0h` | **`Bh`** | Add carry bit into LSB: $10\text{Ah} \bmod 100\text{h} + 1\text{h} = \text{Ah} + 1\text{h} = \text{Bh}$ |

To configure a UART baud-rate divider from a $f_{\text{clk}} = 150.0\text{ MHz}$ peripheral clock at $115,200\text{ baud}$ with $8\times$ oversampling ($\text{Divider} = \frac{150,000,000}{8 \times 115,200} \approx 162.760417$), switch to `{{key:DEC}}` mode. Keying `{{res:sc32_10_computer_science_bases_seq_40:keys}}` evaluates the exact floating-point baud divider **`{{res:sc32_10_computer_science_bases_seq_40:value}}`**, and `{{key:IP}}` / `{{key:FP}}` split out the 16-bit integer register (`IBRD = 162`) and 6-bit sixty-fourths fractional register (`FBRD = 49`):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `150000000` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $150000000.$ | Enter $150\text{ MHz}$ peripheral clock frequency |
| `{{key:ENTER}}` | $0.00000000$ | $0.00000000$ | $150000000.$ | $150000000.$ | Stage clock frequency in Register Y |
| `8 {{key:÷}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $18750000.0$ | Divide by $8\times$ oversampling factor |
| `115200 {{key:÷}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $162.760417$ | Exact baud divider $162.760417$ |
| `{{key:ENTER}}` | $0.00000000$ | $0.00000000$ | $162.760417$ | $162.760417$ | Duplicate baud divider into Register Y |
| `{{key:IP}}` | $0.00000000$ | $0.00000000$ | $162.760417$ | $162.000000$ | Extract integer baud register `IBRD = 162` |
| `{{key:x⇄y}} {{key:FP}}` | $0.00000000$ | $0.00000000$ | $162.000000$ | $0.76041667$ | Swap and extract fractional remainder $0.760417$ |
| `64 {{key:×}}` | $0.00000000$ | $0.00000000$ | $162.000000$ | $48.6666667$ | Scale fraction into sixty-fourths ($48.67 / 64$) |
| `{{key:RND}}` | $0.00000000$ | $0.00000000$ | $162.000000$ | $49.0000000$ | Round to nearest integer for `FBRD = 49` |

Finally, to unpack the 32-bit IEEE-754 single-precision word `0xC0C80000` ($-6.25_{10}$) in `{{key:HEX}}` mode, chain two `{{key:÷R}}` divisions—first by $2^{23} = \text{800000h}$ and then by $2^8 = \text{100h}$—to place the 23-bit mantissa (`480000h`) in Register $Z$, the 8-bit biased exponent (`81h` $= 129_{10}$) in Register $Y$, and the 1-bit sign (`1h`) in Register $X$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `C0C80000 {{key:ENTER}}` | `0h` | `0h` | `C0C80000h` | `C0C80000h` | Stage 32-bit IEEE-754 float word `C0C80000h` |
| `800000 {{key:÷R}}` | `0h` | `0h` | `480000h` | `181h` | Cleave at Bit 23: mantissa `480000h` in Y, upper 9 bits `181h` in X |
| `100 {{key:÷R}}` | `0h` | `480000h` | `81h` | `1h` | Cleave at Bit 8: Sign `1h` in X, Exponent `81h` in Y, Mantissa in Z |
| `{{key:BASE}} {{key:DEC}}` | 0 | 4718592 | 129 | 1 | Switch to Decimal: $S = 1$, $E = 129$, $M = 4,718,592$ |
| `{{key:x⇄y}} 127 {{key:-}}` | 4718592 | 4718592 | 1 | 2 | Subtract bias $127$ to reveal true binary exponent $e = 2$ |

Similarly, for a 64-bit IEEE-754 double-precision float (`binary64`) such as $-13.375_{10}$ (`0xC02AC00000000000`, upper 32-bit word `0xC02AC000`), chaining `C02AC000 {{key:ENTER}} 100000 {{key:÷R}} 800 {{key:÷R}}` in `{{key:HEX}}` mode cleaves at $2^{20} = \text{100000h}$ and $2^{11} = \text{800h}$ to leave Sign $S = \mathbf{1}$ (`1h`) in $X$, Biased Exponent $E = \mathbf{\text{402h}}$ ($1026_{10} \implies e = 1026 - 1023 = \mathbf{3}$) in $Y$, and upper 20-bit significand `AC000h` ($\frac{704,512}{2^{20}} = 0.671875$) in $Z$, reconstructing $(-1)^1 \times 2^3 \times (1 + 0.671875) = \mathbf{-13.375}$.

### Combinatorics (PROB) & Birthday Paradox Collision Probability

Switching back to `{{key:DEC}}` mode, let us evaluate discrete state spaces and collision probabilities using the **`{{key:PROB}}` menu** (`Right Shift {{key:↱}} above {{key:eˣ}}`):
* **RAID Parity Groups vs. Failover Chains (`{{key:Cn,r}}` & `{{key:Pn,r}}`):** To count how many ways a 12-drive storage array can select $5$ drives for a RAID parity group ($C(12, 5)$) versus an ordered 5-drive failover chain ($P(12, 5)$), key `12 {{key:ENTER}} 5 {{key:PROB}} {{key:Cn,r}}` to obtain **`792`** unordered subsets, or `12 {{key:ENTER}} 5 {{key:PROB}} {{key:Pn,r}}` to obtain **`95,040`** ordered sequences.
* **Hexadecimal Pipeline Permutations ($P(16, 4)$):** Choosing an ordered 4-nibble hexadecimal sequence without repetition from $16$ hex digits via `{{res:sc32_10_computer_science_bases_seq_47:keys}}` yields **`{{res:sc32_10_computer_science_bases_seq_47:value}}`**.
* **Full-Mesh Router Topology ($C(7, 2)$):** Wiring a full mesh of point-to-point links among $7$ network routers via `{{res:sc32_10_computer_science_bases_seq_48:keys}}` requires **`{{res:sc32_10_computer_science_bases_seq_48:value}}`** cables.
* **Packet-Queue Factorial Permutations ($15!$):** Permuting $15$ packet-routing priorities via `{{res:sc32_10_computer_science_bases_seq_49:keys}}` spans **`{{res:sc32_10_computer_science_bases_seq_49:value}}`** states ($12! = 479,001,600$ for $12$ items).
* **The 23-Person Birthday Collision Paradox ($1 - P(365, 23)/365^{23}$):** Keying `365 {{key:ENTER}} 23 {{key:PROB}} {{key:Pn,r}}` computes the number of collision-free birthday assignments across $23$ people ($4.220082 \times 10^{58}$), dividing by `365 {{key:ENTER}} 23 {{key:yˣ}} {{key:÷}}` gives the no-collision probability $P_{\text{unique}} = \mathbf{0.492703}$, and subtracting from $1$ via `1 {{key:x⇄y}} {{key:-}}` confirms that the probability of a shared birthday or hash collision is already **`0.507297`** (**$50.73\%$**)!

---

### From Binary Registers to the Mathematics of Time and Money

Stepping back from Claude Shannon's relay circuits and our 36-bit two's-complement odometer, notice the quiet mathematical thread that tied every base conversion and bit-packing problem together: **positional power scaling**. Writing a number in base $b$ means weighting each column by a power $b^k$ and evaluating the resulting polynomial from the inside out—whether $b = 2$ inside a silicon logic gate, $b = 16$ inside a memory address map, or $b = 10$ on an everyday ledger. By giving you one-tap radix switching (`{{key:HEX}}`, `{{key:DEC}}`, `{{key:OCT}}`, `{{key:BIN}}`), two's-complement negation (`{{key:+/-}}`), and single-keystroke bit-field cleaving (`{{key:÷R}}`), the SC-32 lets you step inside the machine's native binary architecture without ever leaving the four-register stack.

From the silent binary hardware inside the calculator, we now return to everyday human life. Where do the exponential growth laws of Chapter 3, the Horner polynomial nesting of Chapter 7, and the root-finding engines of numerical analysis touch every household, student loan, homebuyer, and business on Earth? When we replace the discrete integer base $2$ with the compounding growth factor $(1 + i)$, positional power scaling across bit columns becomes **discounting and compounding across time**. We open that eight-hundred-year-old financial engine next in **[Chapter 11: The Eight-Hundred-Year Engine of Compound Interest: Time Value of Money](11-financial-tvm.md)**.
