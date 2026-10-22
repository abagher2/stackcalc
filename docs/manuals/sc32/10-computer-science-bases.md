---
title: "Chapter 10: Computer Science, Bases & 36-Bit Integers | SC-32 Manual"
description: "36-bit two's complement integer architecture, base conversions (HEX, DEC, OCT, BIN), integer division & remainder bit-field extraction (÷R), CIDR IPv4 subnetting, RGB565 packing, combinatorics, and PRNG on the StackCalc SC-32."
---

# Chapter 10: Computer Science, Bases & 36-Bit Integers

## Claude Shannon's 1937 Switchboard Epiphany & Why Classic Mainframes Used 36-Bit Words

In the summer of 1936, a twenty-one-year-old graduate student named **Claude Elwood Shannon** was working in the basement of MIT's electrical engineering building. His task was operating Vannevar Bush's Differential Analyzer—a colossal mechanical analog computer composed of spinning steel discs, brass gears, and motorized lead screws that solved differential equations through physical rotation.

To reset the machine for each differential run, Shannon had to rewire complex arrays of electromechanical telephone relays.

As Shannon manipulated the clicking relays, he recalled an obscure 1854 treatise by British mathematician George Boole, *An Investigation of the Laws of Thought*, which he had studied in an undergraduate philosophy course at the University of Michigan. Boole had formulated an abstract algebraic system where variables took only two truth values: $1$ (True) or $0$ (False).

Shannon recognized a direct isomorphism: **every open or closed telephone relay implements two-state Boolean logic and binary arithmetic.**

In his 1937 MIT master's thesis—published in 1938 {{cite:shannon1938}} and subsequently hailed by computer scientist Howard Gardner as "possibly the most important, and also the most famous, master's thesis of the century"—Shannon proved that any mathematical or logical expression can be evaluated by an arrangement of physical binary switches. Every microprocessor, FPGA, and memory cell built in the past nine decades traces its intellectual lineage directly to Shannon's switchboard epiphany.

### The Architectural Drama: The 36-Bit Word vs. The 8-Bit Byte

When scientific mainframe pioneers at IBM, MIT, and Digital Equipment Corporation engineered the legendary machines of the 1950s and 1960s—the IBM 704, IBM 7094, and DEC PDP-10—they converged on a word length that seems curious to modern programmers accustomed to 32-bit and 64-bit boundaries: **the 36-bit word**.

Why 36 bits?

In that era, computers processed floating-point scientific calculations, octal and hexadecimal machine code, and alphabetic text concurrently. Thirty-six bits was a number-theoretic sweet spot because $36$ is simultaneously divisible by $2, 3, 4, 6, 9, 12,$ and $18$:
1. **Ten Decimal Digits of Scientific Precision:** $2^{36} = 68,719,476,736 \approx 6.87 \times 10^{10}$, granting ten full decimal digits of integer and mantissa precision.
2. **Clean Partitioning into Both Octal Triads and Hex Nibbles:** A 32-bit word divides cleanly into eight 4-bit hexadecimal nibbles ($32 = 8 \times 4$), but leaves an awkward 2-bit stub when grouped into 3-bit octal triads ($32 = 10 \times 3 + 2$). A 36-bit word divides with zero remainder into **twelve 3-bit octal digits** ($36 = 12 \times 3$) *and* **nine 4-bit hexadecimal nibbles** ($36 = 9 \times 4$).
3. **Six 6-Bit Characters & Dual 18-Bit Pointers:** Standard alphanumeric teleprinters encoded text in 6-bit character sets (Fieldata/ASCII-6), packing exactly six characters into a 36-bit word ($36 = 6 \times 6$), while the DEC PDP-10 split its 36-bit words into two symmetric 18-bit halves so a single instruction could hold both a left register address and a right memory pointer simultaneously.

When IBM introduced the System/360 in 1964, Gene Amdahl and Fred Brooks shifted commercial computing to 8-bit bytes and 32-bit words to streamline commercial billing and byte-stream peripherals. Yet in aerospace telemetry, radar processing, and scientific research, the 36-bit word remained legendary for its graceful handling of precision and unsigned headroom.

The StackCalc SC-32 honors this golden architectural heritage. Rather than confining programmers to signed 32-bit limits that choke on unsigned `0xFFFFFFFF` network masks, the SC-32 provides an authentic **36-bit two's complement integer architecture**.

{{blocks:prime_lcm_gcd_venn|Prime LCM and GCD Venn Diagram}}
*Figure 10.1: Prime factorization and set intersection modeling with Prime Factor Blocks. Discrete number-theoretic operations map directly to modular division, meshing gear cycles, and radix partitioning.*

{{blocks:counting_tiles_box_3x1x13u|Counting Tiles in Desktop Storage Case}}
*Figure 10.2: Concrete physical unit packaging with Counting Tiles and Place Value Cubes, representing modular grouping and discrete word-length partitioning across physical registers.*

### Positional Radix Bundling & Euclidean Remainder Extraction (`{{key:÷R}}`)

Why does the same integer division-with-remainder key (`{{key:÷R}}`) extract decimal digits, binary bit flags, octal triads, and hexadecimal nibbles? Because positional number representation in **any** radix $b \in \{2, 8, 10, 16\}$ is the exact mathematical generalization of bundling physical **Place Value Cubes** and flipping two-color counters in the **Ten-Frame Tray**:
1. **Base-10 Regrouping:** With the **Place Value Cubes**, stacking ten $7.0\text{ mm}$ ($1\text{U}$) `+1` **Regrouping Unit Miniblocks** ($10^0 = 1$) reaches $70.0\text{ mm}$ (matching the $70.0\text{ mm}$ $10\text{U}$ **10-Rod**) and trades 10-for-1 across the four sockets (`THOUSANDS | HUNDREDS | TENS | ONES`, $10^3, 10^2, 10^1, 10^0$) of the **Whole Numbers Place-Value Tray**. When you divide $255$ by $10$ via `255 {{key:ENTER}} 10 {{key:÷R}}`, Register $Y$ holds the $5$ unbundled ones ($255 \bmod 10 = 5$, the `ONES` column digit) while Register $X$ holds the $25$ bundled tens ($\lfloor 255 / 10 \rfloor = 25$) ready for the next `{{key:÷R}}` pass into the `TENS` and `HUNDREDS` columns.
2. **Base-2 Binary Bit-Counters & Base-16 Nibbles:** Replace the rule *"bundle every 10 cubes"* with *"bundle every $b = 2$ counters"* (where each slot in the Ten-Frame holds a single two-color counter flipped to **Coral Red $= 1$** or **Amber Gold $= 0$**) or *"bundle every $b = 16$ tiles into a 4-bit hexadecimal nibble"*. Repeatedly dividing a 36-bit integer $N$ by the radix $b$ (or by a bit-shift power $M = 2^k$) via `{{key:÷R}}` peels off the least-significant remainder field ($N \bmod M$) into Register $Y$ while shifting the upper quotient word ($\lfloor N / M \rfloor$) into Register $X$—performing exact bit-field unpacking and base conversion without losing a single bit.
3. **Mechanical Odometers, Meshing Gear Cycles & Planetary Clocks:** `{{key:÷R}}` is also the exact mathematical engine of **mechanical wheel odometers, meshing spur gears, and the Planetary Geared Clock**. When a 60-tooth minute wheel advances by $N$ clicks, keying `N {{key:ENTER}} 60 {{key:÷R}}` returns the completed full revolutions in Register $X$ (the carry transferred to the next gear stage) and the current tooth position in Register $Y$ (the modulo-60 remainder $N \bmod 60$). Likewise, when two meshing gears with tooth counts $A$ and $B$ rotate together, their tooth alignment repeats every $\operatorname{LCM}(A, B)$ teeth—the union of their **Prime Factor Blocks** rings (*Figure 10.1*)—while `{{key:÷R}}` tracks each wheel's instantaneous phase angle.

Sequences in this chapter begin in decimal mode (`{{key:DEC}}`) before switching dynamically among hexadecimal (`{{key:HEX}}`), octal (`{{key:OCT}}`), and binary (`{{key:BIN}}`) while preserving all four stack registers ($X, Y, Z, T$).

---

{{res:sc32_hex_255:screenshot|Decimal 255 converted to hexadecimal FFh}}

## The 36-Bit Two's Complement Integer Architecture

In digital electronics, systems programming, firmware development, and network engineering, calculations operate directly upon discrete binary registers rather than continuous floating-point approximations. How does a finite ring of 36 binary switches represent both positive and negative numbers without needing a separate subtraction circuit?

Imagine a mechanical car odometer with nine hexadecimal wheels reading `000000000h`. If you drive forward one click (`+1`), the right wheel advances to `000000001h`. What happens if you roll the odometer *backward* one click from zero (`0 - 1`)? Every wheel rolls backward past `0` to `F`, leaving the display at `FFFFFFFFFh` (all 36 bits set to `1`). Notice what happens when you add `000000001h` to `FFFFFFFFFh`: every column carries into the next until the 37th bit spills off the left edge of the 36-bit register, leaving `000000000h`! Because $X + \text{FFFFFFFFFh} \equiv X - 1 \pmod{2^{36}}$, the bit pattern `FFFFFFFFFh` behaves identically to $-1$ inside an ordinary binary adder.

This odometer wrap-around is called **two's complement arithmetic**. Rather than dedicating all $2^{36}$ states to positive integers, we split the 36-bit number wheel in half at bit position 35 (the Most Significant Bit, or `MSB`):
- **Positive Half (`Bit 35 = 0`):** Walking clockwise from `000000000h` ($0$) up to `7FFFFFFFFh` ($+2^{35} - 1 = +34,359,738,367$) covers all non-negative integers.
- **Negative Half (`Bit 35 = 1`):** Taking one more step past `7FFFFFFFFh` flips Bit 35 to `1` at `800000000h`, which represents the most negative number ($-2^{35} = -34,359,738,368$). From there, counting upward through `800000001h`, $\dots$, `FFFFFFFFEh` ($-2$), and `FFFFFFFFFh` ($-1$) climbs steadily back toward `000000000h`. To negate any integer $X$ in two's complement, the processor simply inverts all 36 bits ($\sim X = \text{FFFFFFFFFh} - X$) and adds $1$.

| Bit Position | Field Designation | Meaning in 36-Bit Two's Complement |
| :---: | :---: | :--- |
| **Bit 35** | `MSB` / Sign Bit | `0` = Positive integer ($0$ to $+2^{35}-1$); `1` = Negative integer ($-2^{35}$ to $-1$) |
| **Bits 34–32** | Upper Headroom | Provides 4 full bits of positive headroom above standard 32-bit unsigned words |
| **Bits 31–0** | Standard 32-Bit Word | Holds full 32-bit unsigned addresses, IPv4 netmasks, and GPIO bitfields |

### Why 36 Bits Solves the 32-Bit Signed Overflow Trap
On a conventional 32-bit signed calculator, Bit 31 is the sign bit. The moment you enter a 32-bit unsigned memory address or an IPv4 broadcast mask like `0xFFFFFFFF` ($4,294,967,295$), Bit 31 is `1`—so a 32-bit calculator misinterprets the address as $-1$ or throws a range error! Because the SC-32 places its sign bit four positions higher at **Bit 35**, any 32-bit unsigned value up to `0xFFFFFFFF` (`0FFFFFFFFh`) sits comfortably in Bits 31–0 with `0` in Bits 35–32. It remains strictly positive ($+4,294,967,295$) with four full bits of unsigned headroom to spare for carry flags, parity tags, and multi-word checksum accumulators. Values whose magnitude exceeds the 36-bit range ($+34,359,738,367$ or $-34,359,738,368$ in decimal entry) trigger the non-destructive `TOO BIG` annunciator rather than silently truncating digits.

---

## Dynamic Base Modes (`HEX`, `DEC`, `OCT`, `BIN`)

Following the classic HP-32SII philosophy, the SC-32 `{{key:BASE}}` menu (accessed via Left Shift `{{key:↰}}` on the multiplication key `{{key:×}}`, Row 5, Column 3) treats number bases as **live display and entry lenses** over the same underlying registers:

| Base System | Keystroke | Screen Suffix | Allowed Character Digits | Example Formatted Display |
| :--- | :--- | :---: | :--- | :--- |
| **Decimal** | `{{key:BASE}} {{key:DEC}}` | *(none)* | `0` through `9` | `1042` |
| **Hexadecimal** | `{{key:BASE}} {{key:HEX}}` | `h` | `0` through `9`, `A` through `F` | `412h` |
| **Octal** | `{{key:BASE}} {{key:OCT}}` | `o` | `0` through `7` | `2022o` |
| **Binary** | `{{key:BASE}} {{key:BIN}}` | `b` | `0` and `1` | `10000010010b` |

### The Stack Preservation Invariant
Switching between base modes **never destroys, alters, or shifts the values in the operational stack ($X, Y, Z, T$)**. If Register $X$ holds `255` in Decimal mode, pressing `{{key:BASE}} {{key:HEX}}` instantly re-renders the register as `FFh`, pressing `{{key:BASE}} {{key:OCT}}` shows `377o`, and pressing `{{key:BASE}} {{key:BIN}}` reveals all eight asserted bits as `11111111b`. The underlying 36-bit integer word in the processor's registers never changes—only the radix lens through which you view and type it.

### Direct Hexadecimal Digit Input (`A` through `F`)
When Hexadecimal mode (`{{key:HEX}}`) is active, the top row of primary scientific keys (Row 1, Columns 0 through 5) maps directly to the printed alpha legends $A$ through $F$:
* `{{key:√x}}` $\to \mathbf{A}$ ($10_{10}$), `{{key:eˣ}}` $\to \mathbf{B}$ ($11_{10}$), `{{key:LN}}` $\to \mathbf{C}$ ($12_{10}$)
* `{{key:yˣ}}` $\to \mathbf{D}$ ($13_{10}$), `{{key:1/x}}` $\to \mathbf{E}$ ($14_{10}$), `{{key:Σ+}}` $\to \mathbf{F}$ ($15_{10}$)

To enter the classic debugging magic number `0xDEADBEEF`, simply key `{{key:yˣ}} {{key:1/x}} {{key:√x}} {{key:yˣ}} {{key:eˣ}} {{key:1/x}} {{key:1/x}} {{key:Σ+}}`. Whenever you want to apply scientific functions (`{{key:√x}}`, `{{key:LN}}`, `{{key:yˣ}}`) to a hexadecimal value, switch back to Decimal mode (`{{key:BASE}} {{key:DEC}}`) first so the top-row keys resume their mathematical roles.

#### Rapid Calculation & Equation Entry: Mixing Radices Mid-Calculation
In computer science exams and embedded debugging sessions, expressions frequently mix bases—for instance, adding a hexadecimal base offset $3\text{A}7_{16}$ to an octal permission mask $452_8$ and reporting the result in decimal. Because the SC-32 preserves all four stack registers across base changes, you can switch radices right in the middle of a calculation without jotting down a single intermediate number:
1. Switch to Hex (`{{key:BASE}} {{key:HEX}}`) and enter the first operand: `3 {{key:√x}} 7 {{key:ENTER}}` ($3\text{A}7_{16} = 935_{10}$).
2. Switch to Octal (`{{key:BASE}} {{key:OCT}}`) and add the second operand directly: `452 {{key:+}}`. Register $X$ immediately sums both words in octal ($2261_8$).
3. Switch to Decimal (`{{key:BASE}} {{key:DEC}}`): Register $X$ instantly displays **$1,201_{10}$**.

---

## Bit-Field Extraction, Shifting & Masking on the RPN Stack

Why doesn't the SC-32 clutter its `BASE` menu with dedicated `AND`, `OR`, `XOR`, `SL`, and `SR` softkeys? Because in positional binary arithmetic, shifting a word left or right by $k$ bits is simply multiplying or dividing by $M = 2^k$, and splitting a hardware register at bit boundary $k$ is Euclidean division with remainder (`{{key:÷R}}`)!

When you divide a 36-bit integer $Y$ by a power of two $M = 2^k$ using `{{key:÷R}}`, the calculator cleaves the binary word cleanly at bit $k$ in a single keystroke:
* **Register `X` (Quotient $\lfloor Y / 2^k \rfloor$):** Receives the **upper bits** shifted right by $k$ positions ($Y \gg k$).
* **Register `Y` (Remainder $Y \bmod 2^k$):** Retains the **lower $k$ bits** masked off ($Y \ \& \ (2^k - 1)$).

| Bit-Field / Masking Operation | Mathematical Equivalent ($M = 2^k$) | SC-32 RPN Keystrokes (`HEX` / `DEC`) | Result Location |
| :--- | :---: | :--- | :--- |
| **Left Shift ($X \ll k$)** | $X \times 2^k$ | `X {{key:ENTER}} M {{key:×}}` | Shifted word in **`X`** |
| **Right Shift ($X \gg k$)** | $\lfloor X / 2^k \rfloor$ | `X {{key:ENTER}} M {{key:÷}}` (or `{{key:÷R}}`) | Upper bits in **`X`** |
| **Low-Bit Mask ($X \ \& \ (2^k - 1)$)** | $X \bmod 2^k$ | `X {{key:ENTER}} M {{key:÷R}} {{key:x⇄y}}` | Low $k$ bits in **`X`** |
| **High-Bit Alignment ($X \ \& \ \sim(2^k - 1)$)** | $\lfloor X / 2^k \rfloor \times 2^k$ | `X {{key:ENTER}} M {{key:÷R}} M {{key:×}}` | Aligned base in **`X`** |
| **Set Disjoint Bit $k$** | $X + 2^k$ | `X {{key:ENTER}} M {{key:+}}` | Updated word in **`X`** |
| **Clear Set Bit $k$** | $X - 2^k$ | `X {{key:ENTER}} M {{key:-}}` | Updated word in **`X`** |
| **32-Bit Unsigned Complement** | $\text{FFFFFFFF}_{16} - X$ | `FFFFFFFF {{key:ENTER}} X {{key:-}}` | Inverted mask in **`X`** |

### Mode-Locked Base Entry vs. Unified 36-Bit Word & Remainder Operations

Operating directly on 36-bit integer words across all four stack registers with simultaneous quotient-and-remainder division (`{{key:÷R}}`) eliminates the submenu radix conversions and manual remainder steps required on conventional algebraic calculators:

| Challenge / Metric | Conventional Algebraic Calculator (Infix) | Algebraic Strokes | SC-32 RPN Stack Method | SC-32 Strokes | Stack Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **IPv4 Subnet Partitioning**: Split `192.168.10.45` (`C0A80A2Dh`) into `/24` network ID & host offset | Manual integer truncation: `int(C0A80A2D / 100)` followed by subtract-and-multiply remainder `C0A80A2D - Ans * 100` (28 strokes). Stack is invisible. | 28 | **Simultaneous Division with Remainder (`{{key:÷R}}`)**: Key `C0A80A2D ENTER 100 ÷R` (11 strokes). Network prefix in $X$, host offset in $Y$ immediately. | 11 | **60% fewer strokes + single-cycle quotient/remainder split** |
| **Multi-Base Radix Inspection**: Convert decimal `3735928559` to Hex, Octal, and Binary | Navigate nested `MATH` $\to$ `Base` submenus for each radix or run manual iterative division. Stack history is discarded or obscured (26+ strokes). | 26 | **Native 36-Bit Base Engine**: Press `{{key:BASE}} {{key:HEX}}`, `{{key:OCT}}`, `{{key:BIN}}` (4 strokes). All 4 stack levels ($X, Y, Z, T$) convert losslessly in place. | 4 | **85% fewer strokes + continuous multi-register stack preservation** |
| **RGB Color Bit-Field Packing**: Pack Red ($255$), Green ($128$), Blue ($64$) into `FF8040h` | Algebraic polynomial: `255 * 256 ^ 2 + 128 * 256 + 64 =` (21 strokes). Requires repeated radix-256 entry and decimal-to-hex conversion. | 21 | **Positional RPN Pipeline (`{{key:HEX}}` mode)**: `FF {{key:ENTER}} 100 {{key:×}} 80 {{key:+}} 100 {{key:×}} 40 {{key:+}}` (12 strokes). Streamlined Horner radix-$100_{16}$ pipeline with instant byte alignment. | 12 | **43% fewer strokes + native hex byte alignment** |

---

## Bitwise Telemetry, Cryptographic Hashing, and Fixed-Point Architecture in Practice

Whether you are carving up an enterprise IPv4 address block in a data center, probing a microcontroller's peripheral control registers with a logic analyzer, or verifying a TCP packet checksum by hand, you are constantly slicing, shifting, and reassembling binary words. On a standard algebraic calculator without a remainder operator, extracting a 4-bit field from the middle of a 16-bit register requires a clumsy dance of floating-point division, manual integer truncation, and subtraction {{cite:shannon1938}}.

In the explorations that follow, we put the SC-32's 36-bit two's complement stack and `{{key:÷R}}` operator to work across real-world network routing, bare-metal GPIO control, color framebuffers, RFC 1071 packet checksums, and IEEE-754 floating-point bit unpacking {{cite:ieee754_2019}}.

---

### Network Addressing, Radix Conversions & Modular Packing

We begin by switching among `HEX`, `DEC`, `OCT`, and `BIN` to inspect IPv4 subnets, network broadcast boundaries, and bare-metal GPIO control registers.

#### Subnet Masking via Modular Division & Integer Bit-Packing
Suppose a core router in a campus data center receives an IPv4 packet addressed to final host octet `205` on a `/28` VLAN interface (`255.255.255.240`). Because a `/28` mask reserves the top 4 bits of the final octet for the subnet prefix and leaves the bottom 4 bits for hosts, it partitions the 256-address octet into blocks of $2^{32-28} = 2^4 = 16$ addresses. Rather than converting `205` and `240` into binary strings by hand to bitwise-AND them, we can divide `205` by the block stride `16` via `{{key:÷R}}` to find which 16-address block it belongs to (quotient `12` in Register $X$, host offset `13` in Register $Y$) and multiply by `16` to snap directly to the `/28` subnet boundary:

$$205_{10} = 11001101_2, \qquad 240_{10} = 11110000_2, \qquad 205 \text{ AND } 240 = 11000000_2 = 192_{10}$$

Working in `{{key:DEC}}` mode, keying `{{res:sc32_10_computer_science_bases_seq_03:keys}}` snaps the octet directly to the aligned subnet boundary **`{{res:sc32_10_computer_science_bases_seq_03:value}}`**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `205` | 0 | 0 | 0 | 205 | `205_` |
| 02 | `{{key:ENTER}}` | 0 | 0 | 205 | 205 | `205` |
| 03 | `16 {{key:÷R}}` | 0 | 0 | 13 | 12 | `12` |
| 04 | `16 {{key:×}}` | 0 | 0 | 13 | 192 | `192` |

Notice what happened in Step 03: `16 {{key:÷R}}` simultaneously placed the subnet block number (`12`) in Register $X$ and the host's relative offset within that subnet (`13`) in Register $Y$. Multiplying Register $X$ by `16` gives the aligned `/28` network ID (**`192`**), while Register $Y$ still holds the host number (`13`, since $192 + 13 = 205$)!

#### IPv4 CIDR /24 Subnet Network, Broadcast & Host Allocation
Why do network engineers love hexadecimal? Because every 8-bit octet (`0` to `255`) of an IPv4 dotted-quad address maps to a clean two-digit hexadecimal byte (`00h` to `FFh`). When you pack the workstation IPv4 address `192.168.10.45` into a single 32-bit hexadecimal integer (`C0A80A2Dh`), a `/24` subnet mask ($255.255.255.0 = \text{FFFFFF00h}$) has a block size of $2^{32-24} = 2^8 = 256_{10} = \text{100h}$. And because the SC-32 uses a 36-bit word, unsigned 32-bit masks like `FFFFFF00h` and `FFFFFFFFh` stay strictly positive without colliding with the sign bit at Bit 35:

| Field | Octet 1 (`192` / `C0h`) | Octet 2 (`168` / `A8h`) | Octet 3 (`10` / `0Ah`) | Octet 4 (`45` / `2Dh`) |
| :--- | :---: | :---: | :---: | :---: |
| **Host IP Bits** | `11000000` | `10101000` | `00001010` | `00101101` |
| **Subnet Mask (`/24`)** | `11111111` (Net) | `11111111` (Net) | `11111111` (Net) | `00000000` (Host) |
| **Aligned Network ID** | `11000000` (`192`) | `10101000` (`168`) | `00001010` (`10`) | `00000000` (`0`) |

In `{{key:HEX}}` mode, keying `{{res:sc32_10_computer_science_bases_seq_04:keys}}` extracts the `/24` network address **`{{res:sc32_10_computer_science_bases_seq_04:value}}`** (`192.168.10.0`) while leaving the host offset (`2Dh`) in Register $Y$. Subtracting the `/24` netmask from the all-ones broadcast word via `{{res:sc32_10_computer_science_bases_seq_05:keys}}` isolates the wildcard mask **`{{res:sc32_10_computer_science_bases_seq_05:value}}`** (`0.0.0.255`), and adding that wildcard mask to the aligned network address via `{{res:sc32_10_computer_science_bases_seq_06:keys}}` produces the subnet broadcast address **`{{res:sc32_10_computer_science_bases_seq_06:value}}`** (`192.168.10.255`), leaving $2^{32 - 24} - 2 = 2^8 - 2 = 256 - 2 = \mathbf{254\text{ usable hosts}}$ (`192.168.10.1` to `192.168.10.254`):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `C0A80A2D` | `0h` | `0h` | `0h` | `C0A80A2Dh` | `C0A80A2D_h` |
| 02 | `{{key:ENTER}}` | `0h` | `0h` | `C0A80A2Dh` | `C0A80A2Dh` | `C0A80A2Dh` |
| 03 | `100 {{key:÷R}}` | `0h` | `0h` | `2Dh` | `C0A80Ah` | `C0A80Ah` |
| 04 | `100 {{key:×}}` | `0h` | `0h` | `2Dh` | `C0A80A00h` | `C0A80A00h` |
| 05 | `FF {{key:+}}` | `0h` | `0h` | `2Dh` | `C0A80AFFh` | `C0A80AFFh` |

#### Embedded GPIO Pin Bit-Setting (`+`)
You are bringing up a newly assembled prototype circuit board on the lab bench and need to illuminate a green status LED connected to GPIO Pin 5. A debugger readout shows that the 32-bit GPIO direction register (`GPIO_DIR`) currently holds `0x00001804` (Pins 2, 11, and 12 already configured as outputs, while Pin 5 is currently `0` for input). Because Bit 5 is currently `0`, asserting it via bitwise OR (`GPIO_DIR | (1 << 5)`) generates zero carry into neighboring bit positions—which means it is mathematically identical to adding Bit 5's positional weight $2^5 = 32_{10} = \text{20h}$:

| Register Stage | Binary Representation (Bits 15–0) | Hexadecimal Value |
| :--- | :---: | :---: |
| **Original Register** | `0001 1000 0000 0100` | `1804h` |
| **Bit 5 Weight ($2^5$)** | `0000 0000 0010 0000` | `0020h` |
| **Updated Register (`+`)** | `0001 1000 0010 0100` | **`1824h`** |

In `{{key:HEX}}` mode, keying `{{res:sc32_10_computer_science_bases_seq_11:keys}}` sets Bit 5 cleanly to produce **`{{res:sc32_10_computer_science_bases_seq_11:value}}`**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `1804` | `0h` | `0h` | `0h` | `1804h` | `1804_h` |
| 02 | `{{key:ENTER}}` | `0h` | `0h` | `1804h` | `1804h` | `1804h` |
| 03 | `20` | `0h` | `0h` | `1804h` | `20h` | `20_h` |
| 04 | `{{key:+}}` | `0h` | `0h` | `0h` | `1824h` | `1824h` |

#### Embedded GPIO Pin Bit-Cycling (`-` / `+`)
To verify that a real-time timer interrupt is firing on schedule without halting the CPU, embedded engineers often strobe a "heartbeat" GPIO pin connected to an oscilloscope probe or external watchdog timer. Suppose the port output register currently holds `0x00000017` ($0001\,0111_2$, with Bits 0, 1, 2, and 4 asserted) and the heartbeat line is wired to Bit 2 (weight $2^2 = 4 = \text{4h}$). Let's pull Bit 2 low and then re-assert it.

Because Bit 2 is known to be asserted (`1`) in `17h`, working in `{{key:HEX}}` mode and keying `{{res:sc32_10_computer_science_bases_seq_13:keys}}` clears that single pulse bit without borrowing from neighboring columns to produce **`{{res:sc32_10_computer_science_bases_seq_13:value}}`**, and adding `4` back via `{{res:sc32_10_computer_science_bases_seq_14:keys}}` (or `{{key:LASTX}} {{key:+}}`) drives the pin back high to restore **`{{res:sc32_10_computer_science_bases_seq_14:value}}`**.

---

### Peripheral Register Bitfields, Masks & Shift Idioms

Hardware architects rarely waste an entire 32-bit register on a single setting; instead, they pack clock dividers, channel selectors, and enable flags into contiguous bit-fields inside a single control word. Here we use `{{key:÷R}}` and powers of two to slice and pack multi-bit fields.

#### Multi-Bit Field Extraction (ADC Resolution Field)
While debugging an analog sensor driver, you read `0x3C6A` from a 16-bit Analog-to-Digital Converter (ADC) configuration register. According to the datasheet, Bits [7:4] (the upper nibble of the low byte) encode the ADC's bit-resolution setting ($0 \dots 15$, where `6h` selects 12-bit conversion mode). How do we slice Bits [7:4] out of the middle of `3C6Ah` into an isolated integer in Register $X$? First, dividing by $2^8 = \text{100h}$ via `{{key:÷R}}` trims away the upper byte (`3Ch`) and drops the lower byte (`6Ah`, Bits [7:0]) into Register $Y$; swapping `6Ah` into Register $X$ and dividing by $2^4 = \text{10h}$ shifts away Bits [3:0] (`Ah`), leaving Bits [7:4] (`6h`) standing alone:

| Extraction Stage | Binary Nibbles (Bits 15–0) | Hexadecimal Value |
| :--- | :---: | :---: |
| **ADC Configuration Register** | `0011 1100 0110 1010` | `3C6Ah` |
| **Lower Byte Remainder (`÷R 100h`)** | `0000 0000 0110 1010` | `006Ah` |
| **Right-Shifted Nibble (`÷ 10h`)** | `0000 0000 0000 0110` | `0006h` ($6_{10}$) |

In `{{key:HEX}}` mode, isolating the lower byte via modulo `0x100` (`{{res:sc32_10_computer_science_bases_seq_15:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_15:value}}`) and shifting right by 4 bits ($2^4 = 16 = \text{10h}$) via `{{res:sc32_10_computer_science_bases_seq_16:keys}}` extracts **`{{res:sc32_10_computer_science_bases_seq_16:value}}`**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `3C6A {{key:ENTER}}` | `0h` | `0h` | `3C6Ah` | `3C6Ah` | `3C6Ah` |
| 02 | `100 {{key:÷R}}` | `0h` | `0h` | `6Ah` | `3Ch` | `3Ch` |
| 03 | `{{key:x⇄y}}` | `0h` | `0h` | `3Ch` | `6Ah` | `6Ah` |
| 04 | `10 {{key:÷}}` | `0h` | `0h` | `3Ch` | `6h` | `6h` |

#### RGB888 to RGB565 16-Bit Color Packing
To cut framebuffer RAM usage and SPI bus traffic by a third, embedded color LCD controllers commonly pack 24-bit TrueColor (`RGB888`, 8 bits per channel) into a 16-bit word (`RGB565`). Because the human retina's M-cones are most sensitive to green wavelengths, `RGB565` allocates 6 bits ($0\dots63$) to Green in the middle (`Bits 10–5`) and 5 bits ($0\dots31$) each to Red (`Bits 15–11`) and Blue (`Bits 4–0`). Let's pack the vibrant coral color `0xFF5733` ($R=255, G=87, B=51$) into a single 16-bit `RGB565` word:

$$\text{Red}_5 = \lfloor 255 \times 31 / 255 \rfloor = 31 = \text{1Fh}$$
$$\text{Green}_6 = \lfloor 87 \times 63 / 255 \rfloor = 21 = \text{15h}$$
$$\text{Blue}_5 = \lfloor 51 \times 31 / 255 \rfloor = 6 = \text{06h}$$

$$\text{Packed Word} = (R_5 \times 2^{11}) + (G_6 \times 2^5) + B_5$$

| Channel Allocation | Bit Positions | Binary Field | Shifted Hex Value |
| :--- | :---: | :---: | :---: |
| **Red (5-bit)** | Bits `15–11` | `11111` (`1Fh × 800h`) | `F800h` |
| **Green (6-bit)** | Bits `10–5` | `010101` (`15h × 20h`) | `02A0h` |
| **Blue (5-bit)** | Bits `4–0` | `00110` (`06h`) | `0006h` |
| **Combined RGB565 Word** | Bits `15–0` | `1111101010100110` | **`FAA6h`** |

In `{{key:HEX}}` mode, shifting the 5-bit Red channel left by 11 bits ($2^{11} = 800\text{h}$) via `{{res:sc32_10_computer_science_bases_seq_19:keys}}` yields `{{res:sc32_10_computer_science_bases_seq_19:value}}`, shifting the 6-bit Green channel left by 5 bits ($2^5 = 20\text{h}$) via `{{res:sc32_10_computer_science_bases_seq_20:keys}}` yields `{{res:sc32_10_computer_science_bases_seq_20:value}}`, pressing `{{key:+}}` merges Red and Green into `FAA0h`, and adding the 5-bit Blue channel via `{{res:sc32_10_computer_science_bases_seq_21:keys}}` completes the packed 16-bit color word **`{{res:sc32_10_computer_science_bases_seq_21:value}}`**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `1F {{key:ENTER}}` | `0h` | `0h` | `1Fh` | `1Fh` | `1Fh` |
| 02 | `800 {{key:×}}` | `0h` | `0h` | `0h` | `F800h` | `F800h` |
| 03 | `15 {{key:ENTER}}` | `0h` | `F800h` | `15h` | `15h` | `15h` |
| 04 | `20 {{key:×}}` | `0h` | `0h` | `F800h` | `2A0h` | `2A0h` |
| 05 | `{{key:+}}` | `0h` | `0h` | `0h` | `FAA0h` | `FAA0h` |
| 06 | `6 {{key:+}}` | `0h` | `0h` | `0h` | `FAA6h` | `FAA6h` |

#### Base64 Binary Chunking
When early internet mail systems (SMTP) and HTTP headers were designed around 7-bit printable ASCII text, transmitting raw binary files was a nightmare because routers interpreted byte values like `0x00` or `0x0A` as control characters. **Base64 encoding** solves this by welding every three 8-bit bytes ($3 \times 8 = 24\text{ bits}$) into a single 24-bit integer and slicing it into four 6-bit "sextets" ($4 \times 6 = 24\text{ bits}$, each ranging from $0$ to $63$), which map to the 64 safe printable characters `A–Z`, `a–z`, `0–9`, `+`, and `/`. Let's encode the classic 3-byte ASCII string `"Man"` (`0x4D`, `0x61`, `0x6E` $\implies$ 24-bit word `4D616Eh`) into its four 6-bit Base64 indices using slice divisors $2^{18} = \text{40000h}$, $2^{12} = \text{1000h}$, and $2^6 = \text{40h}$:

| Base64 Sextet | 6-Bit Binary Slice | Decimal Index | Base64 Character |
| :--- | :---: | :---: | :---: |
| **Sextet 1 (Bits 23–18)** | `010011` | `19` (`13h`) | **`T`** |
| **Sextet 2 (Bits 17–12)** | `010110` | `22` (`16h`) | **`W`** |
| **Sextet 3 (Bits 11–6)** | `000101` | `5` (`05h`) | **`F`** |
| **Sextet 4 (Bits 5–0)** | `101110` | `46` (`2Eh`) | **`u`** |

In `{{key:HEX}}` mode, slicing `4D616Eh` across the four 6-bit boundaries yields Sextet 1 via `{{res:sc32_10_computer_science_bases_seq_29:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_29:value}}`** ($19_{10} \implies \mathbf{T}$), Sextet 2 via `{{res:sc32_10_computer_science_bases_seq_30:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_30:value}}`** ($22_{10} \implies \mathbf{W}$), Sextet 3 via `{{res:sc32_10_computer_science_bases_seq_31:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_31:value}}`** ($5_{10} \implies \mathbf{F}$), and Sextet 4 via `{{res:sc32_10_computer_science_bases_seq_32:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_32:value}}`** ($46_{10} \implies \mathbf{u}$)—confirming that `"Man"` encodes to **`TWFu`**:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `4D616E {{key:ENTER}} 40000 {{key:÷}}` | `0h` | `0h` | `0h` | **`13h`** | Sextet 1: `4D616Eh >> 18 = 13h` ($19_{10} \implies \mathbf{T}$) |
| 02 | `4D616E {{key:ENTER}} 40000 {{key:÷R}} {{key:x⇄y}} 1000 {{key:÷}}` | `13h` | `13h` | `13h` | **`16h`** | Sextet 2: remainder `>> 12 = 16h` ($22_{10} \implies \mathbf{W}$) |
| 03 | `4D616E {{key:ENTER}} 1000 {{key:÷R}} {{key:x⇄y}} 40 {{key:÷}}` | `16h` | `16h` | `4D6h` | **`5h`** | Sextet 3: remainder `>> 6 = 5h` ($5_{10} \implies \mathbf{F}$) |
| 04 | `4D616E {{key:ENTER}} 40 {{key:÷R}} {{key:x⇄y}}` | `4D6h` | `5h` | `13585h` | **`2Eh`** | Sextet 4: lower 6-bit remainder = `2Eh` ($46_{10} \implies \mathbf{u}$) |

*(**Single-Entry `÷R` Cascade:** Because `{{key:÷R}}` preserves the lower remainder in $Y$ while placing the upper sextet in $X$, chaining `4D616E {{key:ENTER}} 40000 {{key:÷R}} {{key:x⇄y}} 1000 {{key:÷R}} {{key:x⇄y}} 40 {{key:÷R}}` unpacks all four Base64 indices across the four stack registers—`13h` in Register $T$, `16h` in Register $Z$, `2Eh` in Register $Y$, and `5h` in Register $X$—with `4D616E` keyed only once.)*

#### 36-Bit Two's Complement Boundary Audit
Let's test the two critical rollover seams of the 36-bit two's complement odometer in `{{key:HEX}}` mode. First, we load the largest positive signed 36-bit integer `7FFFFFFFFh` ($+2^{35} - 1 = +34,359,738,367_{10}$, where Bit 35 is `0` and Bits 34–0 are all `1`) and add `1` via `{{res:sc32_10_computer_science_bases_seq_33:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_33:value}}` ($-34,359,738,368_{10}$, the minimum negative bound). Second, we start at `0` and subtract `1` via `{{res:sc32_10_computer_science_bases_seq_34:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_34:value}}` ($-1_{10}$) to watch the odometer roll backward across zero:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `7FFFFFFFF {{key:ENTER}}` | `0h` | `0h` | `7FFFFFFFFh` | `7FFFFFFFFh` | Load maximum signed positive 36-bit bound |
| 02 | `1 {{key:+}}` | `0h` | `0h` | `0h` | **`800000000h`** | Overflow rolls over to minimum negative bound |
| 03 | `0 {{key:ENTER}} 1 {{key:-}}` | `0h` | `0h` | `800000000h` | **`FFFFFFFFFh`** | Underflow to $-1_{10}$; all 36 bits set (`FFFFFFFFFh`) |

#### Division with Remainder via `{{key:÷R}}`
In systems programming, mapping a linear memory byte offset into a fixed-size cache line or flash sector requires both the integer quotient and the remainder of Euclidean division ($N = Q \cdot D + R$). Suppose a DMA controller accesses byte offset $12,345$ inside a flash memory array organized into 16-byte rows. Working in decimal (`{{key:DEC}}`) mode, keying `{{res:sc32_10_computer_science_bases_seq_01:keys}}` computes $12,345 \div 16$ with simultaneous quotient and remainder, placing the whole quotient $Q = \mathbf{771}$ (the 16-byte row index) in Register $X$ and the remainder $R = 12345 \bmod 16 = \mathbf{{{res:sc32_10_computer_science_bases_seq_01:value}}}$ (the byte offset within row $771$) in Register $Y$:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `12345 {{key:ENTER}}` | 0 | 0 | 12345 | 12345 | Load integer dividend $12,345$ |
| 02 | `16 {{key:÷R}}` | 0 | 0 | **9** | **771** | Quotient $Q=771$ in Register X, remainder $R=9$ in Register Y |
| 03 | `{{key:x⇄y}}` | 0 | 0 | 771 | **9** | Swap registers to access remainder $9$ directly |

---

### Error Detection, Two's-Complement Arithmetic & Checksums

Digital communication links and processor buses are constantly audited by bit-difference masks, end-around carry checksums, fractional clock dividers, and IEEE-754 floating-point bit layouts.

#### Telemetry Bit-Difference Inspection
A spacecraft health-monitoring downlink transmits a 16-bit subsystem status word `0x5F5A`. During nominal flight, the baseline status mask is `0x5A50`. Which status flags have newly asserted, and what is the **Hamming distance** (the number of differing bits) between the two words?

In `{{key:HEX}}` mode, keying `{{res:sc32_10_computer_science_bases_seq_36:keys}}` isolates the bit-difference mask **`{{res:sc32_10_computer_science_bases_seq_36:value}}`** ($0000010100001010_2$ in `{{key:BIN}}`), where Bits 1, 3, 8, and 10 are set—revealing a Hamming distance of **$4\text{ bits}$**.

Why did simple subtraction work here? Whenever every asserted bit of the baseline mask `5A50h` is a subset of the active bits in `5F5Ah`, subtracting `5F5A {{key:ENTER}} 5A50 {{key:-}}` triggers zero borrows between binary columns and behaves identically to bitwise XOR (`^`), isolating the newly tripped fault flags `50Ah` in Register $X$. Switching to `{{key:BASE}} {{key:BIN}}` immediately displays the binary bit pattern $\mathbf{10100001010\text{b}}$ (bits 1, 3, 8, and 10 asserted; Hamming weight $w_H = \mathbf{4}$).

#### RFC 1071 Internet Checksum & One's Complement Fold via `{{key:÷R}}`
Why do IPv4, TCP, and UDP packet headers use a 16-bit *one's complement* checksum (RFC 1071) rather than ordinary two's complement addition {{cite:knuth1997}}? Because one's complement addition with "end-around carry" is **endian-independent**: whether a router adds 16-bit words in Big-Endian or Little-Endian byte order, wrapping overflow carries from bit 16 back into bit 0 produces the exact same sum! Suppose summing the 16-bit words of an IPv4 header in a 32-bit accumulator yields `2653Dh`. To fold the overflow carry bits ($> \text{FFFFh}$) back into the lower 16 bits and invert all bits for the wire checksum:

$$\text{Header Sum} = 2653\text{D}_{16}$$
$$\text{Carry} = \lfloor 2653\text{D}_{16} / 10000_{16} \rfloor = 2_{16}, \qquad \text{Lower 16 Bits} = 2653\text{D}_{16} \bmod 10000_{16} = 653\text{D}_{16}$$
$$\text{Folded Sum} = 653\text{D}_{16} + 2_{16} = 653\text{F}_{16}$$
$$\text{Checksum} = \text{FFFF}_{16} - 653\text{F}_{16} = \mathbf{9AC0}_{16} \ (39,616_{10})$$

In `{{key:HEX}}` mode, loading the 32-bit accumulated header sum (`2653D {{key:ENTER}}`) and dividing by $2^{16} = \text{10000h}$ via `10000 {{key:÷R}}` places the upper carry (`2h`) in Register $X$ and the lower 16 bits (`653Dh`) in Register $Y$; pressing `{{key:+}}` folds the carry into the lower sum (`653Fh`), and subtracting from `FFFFh` via `FFFF {{key:x⇄y}} {{key:-}}` yields the one's complement checksum **`9AC0h`** ($39,616_{10}$ in `{{key:DEC}}`):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `2653D {{key:ENTER}}` | `0h` | `0h` | `2653Dh` | `2653Dh` | `2653Dh` |
| 02 | `10000 {{key:÷R}}` | `0h` | `0h` | `653Dh` | `2h` | `2h` |
| 03 | `{{key:+}}` | `0h` | `0h` | `0h` | `653Fh` | `653Fh` |
| 04 | `FFFF` | `0h` | `0h` | `653Fh` | `FFFFh` | `FFFFh` |
| 05 | `{{key:x⇄y}}` | `0h` | `0h` | `FFFFh` | `653Fh` | `653Fh` |
| 06 | `{{key:-}}` | `0h` | `0h` | `0h` | `9AC0h` | `9AC0h` |

Notice how cleanly `{{key:÷R}}` executes the RFC 1071 end-around carry: dividing `2653Dh` by `10000h` ($2^{16}$) splits the upper carry (`2h`) into Register $X$ and the lower 16-bit word (`653Dh`) into Register $Y$ in one keystroke, so pressing `{{key:+}}` folds them together into `653Fh` immediately!

#### UART Fractional Baud Rate Divisor at 150 MHz
Unlike SPI or I2C buses, an asynchronous UART serial link has no shared clock wire—the transmitter and receiver sample each bit using their own internal crystal oscillators. If their baud rates drift apart by more than $\sim 2\%$, the sampling strobe slips across a bit boundary by the 10th bit (the stop bit) and garbles the frame. To achieve sub-percent accuracy from a $f_{\text{clk}} = 150.0\text{ MHz}$ peripheral clock over an $8\times$ oversampling receiver, modern UART peripherals split the clock divider into a 16-bit integer register (`IBRD`) and a 6-bit fractional register (`FBRD`, counted in sixty-fourths, $1/64$). Let's compute `IBRD`, `FBRD`, and the resulting timing error for a target rate of $115,200\text{ baud}$:

$$\text{Baud Divider} = \frac{f_{\text{clk}}}{8 \times \text{Baud}} = \frac{150,000,000}{8 \times 115,200} = \frac{150,000,000}{921,600} \approx 162.760416667$$

In `{{key:ALL}}` display mode, keying `{{res:sc32_10_computer_science_bases_seq_40:keys}}` evaluates the exact floating-point baud divider **`{{res:sc32_10_computer_science_bases_seq_40:value}}`**. Duplicating the divider and taking its integer part (`{{key:ENTER}} {{key:PARTS}} {{key:IP}}`) isolates `IBRD` = **`162`** (`0xA2`), while swapping back to the fractional part and scaling by $64$ (`{{key:x⇄y}} {{key:PARTS}} {{key:FP}} 64 {{key:×}} {{key:PARTS}} {{key:IP}}`) gives `FBRD` = **`48`** (or rounded via `{{key:RND}}`: **`49`**, `0x31`). With `IBRD = 162` and `FBRD = 49`, the actual baud rate is $150,000,000 / (8 \times (162 + 49/64)) = 150,000,000 / 1302.125 = \mathbf{115,196.3\text{ baud}}$, a timing error of just $(115196.3 - 115200) / 115200 \times 100\% = \mathbf{-0.0032\%}$:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `150000000` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $150000000.$ | `150000000._` |
| 02 | `{{key:ENTER}}` | $0.00000000$ | $0.00000000$ | $150000000.$ | $150000000.$ | `150000000._` |
| 03 | `8 {{key:÷}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $18750000.0$ | `18750000._` |
| 04 | `115200 {{key:÷}}` | $0.00000000$ | $0.00000000$ | $0.00000000$ | $162.760417$ | `162.760417_` |
| 05 | `{{key:ENTER}}` | $0.00000000$ | $0.00000000$ | $162.760417$ | $162.760417$ | `162.760417_` |
| 06 | `{{key:IP}}` | $0.00000000$ | $0.00000000$ | $162.760417$ | $162.000000$ | `162._` |
| 07 | `{{key:x⇄y}} {{key:FP}}` | $0.00000000$ | $0.00000000$ | $162.000000$ | $0.76041667$ | `0.76041667_` |
| 08 | `64 {{key:×}}` | $0.00000000$ | $0.00000000$ | $162.000000$ | $48.6666667$ | `48.6666667_` |
| 09 | `{{key:RND}}` | $0.00000000$ | $0.00000000$ | $162.000000$ | $49.0000000$ | `49._` |

#### 32-Bit Byte Swapping (Endianness Reversal)
In his classic 1980 computer-architecture essay *"On Holy Wars and a Plea for Peace"*, Danny Cohen borrowed the terms **Big-Endian** and **Little-Endian** from Jonathan Swift's *Gulliver's Travels* to describe the two rival ways computers order bytes in memory. Internet protocols transmit multi-byte integers in Big-Endian ("network byte order," most-significant byte first), whereas x86 and ARM Cortex processors store integers in Little-Endian (least-significant byte first). Let's reverse the 4-byte Big-Endian network word `0x12345678` into Little-Endian `0x78563412` on the stack using `{{key:÷R}}`, `{{key:÷}}`, `{{key:×}}`, and `{{key:+}}`:

| Byte Order | Byte 3 (MSB) | Byte 2 | Byte 1 | Byte 0 (LSB) |
| :--- | :---: | :---: | :---: | :---: |
| **Big-Endian (`12345678h`)** | `12h` | `34h` | `56h` | `78h` |
| **Shift Operation** | `>> 24` (`÷ 1000000h`) | `>> 8` (`÷ 100h`) | `<< 8` (`× 100h`) | `<< 24` (`× 1000000h`) |
| **Little-Endian (`78563412h`)** | `78h` | `56h` | `34h` | `12h` |

In `{{key:HEX}}` mode, we extract Byte 0 and shift it to Byte 3 via `{{res:sc32_10_computer_science_bases_seq_41:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_41:value}}`, extract Byte 1 and shift it to Byte 2 via `{{res:sc32_10_computer_science_bases_seq_42:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_42:value}}`, extract Byte 2 and shift it to Byte 1 via `{{res:sc32_10_computer_science_bases_seq_43:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_43:value}}`, extract Byte 3 to Byte 0 via `{{res:sc32_10_computer_science_bases_seq_44:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_44:value}}`, and merge all four non-overlapping bytes via `{{key:+}} {{key:+}} {{key:+}}` to obtain **`78563412h`**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `78 {{key:ENTER}} 1000000 {{key:×}}` | `0h` | `0h` | `0h` | `78000000h` | `78000000h` |
| 02 | `56 {{key:ENTER}} 10000 {{key:×}}` | `0h` | `0h` | `78000000h` | `560000h` | `560000h` |
| 03 | `{{key:+}}` | `0h` | `0h` | `0h` | `78560000h` | `78560000h` |
| 04 | `34 {{key:ENTER}} 100 {{key:×}}` | `0h` | `0h` | `78560000h` | `3400h` | `3400h` |
| 05 | `{{key:+}}` | `0h` | `0h` | `0h` | `78563400h` | `78563400h` |
| 06 | `12` | `0h` | `0h` | `78563400h` | `12h` | `12h` |
| 07 | `{{key:+}}` | `0h` | `0h` | `0h` | `78563412h` | `78563412h` |

#### IEEE-754 32-Bit Single Precision Float Unpacking
How does a processor pack a continuous real number like $-6.25$ into a 32-bit binary register? William Kahan's **IEEE-754 standard** writes the number in base-2 scientific notation, $(-1)^S \times 2^{E - 127} \times (1.\text{Mantissa}_2)$. Because every normalized non-zero binary number starts with a leading `1.` before the radix point, the hardware doesn't even store that leading `1`—it hides it ("the implicit leading bit") and uses all 23 low bits (`Bits 22–0`) for the fractional mantissa, 8 middle bits (`Bits 30–23`, biased by $+127$) for the exponent $E$, and 1 top bit (`Bit 31`) for the sign $S$:
1. Absolute value: $6.25_{10} = 4 + 2 + 0.25 = 110.01_2 = 1.1001_2 \times 2^2$.
2. Sign Bit: Negative $\implies S = \mathbf{1}$.
3. Biased Exponent: $E = \text{exponent} + 127 = 2 + 127 = 129_{10} = 10000001_2 = \mathbf{81h}$.
4. Fractional Mantissa (23 bits after the hidden `1.`): $M = 10010000000000000000000_2 = \mathbf{480000h}$.
5. 32-Bit Binary Hex Word: `1 10000001 10010000000000000000000` = **`0xC0C80000`**.

Watch how two chained `{{key:÷R}}` divisions in `{{key:HEX}}` mode—first by $2^{23} = \text{800000h}$ and then by $2^8 = \text{100h}$ (`C0C80000 {{key:ENTER}} 800000 {{key:÷R}} 100 {{key:÷R}}`)—unpack all three IEEE-754 fields of `C0C80000h` directly onto Registers $Z$ (`480000h`), $Y$ (`81h`, Biased Exponent $E=129_{10}$), and $X$ (`1h`, Sign $S=1$):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `C0C80000 {{key:ENTER}}` | `0h` | `0h` | `C0C80000h` | `C0C80000h` | `C0C80000h` |
| 02 | `800000 {{key:÷R}}` | `0h` | `0h` | `480000h` | `181h` | `181h` |
| 03 | `100 {{key:÷R}}` | `0h` | `480000h` | `81h` | `1h` | `1h` |
| 04 | `{{key:BASE}} {{key:DEC}}` | 0 | 4718592 | 129 | 1 | `1` |
| 05 | `{{key:x⇄y}} 127 {{key:-}}` | 4718592 | 4718592 | 1 | 2 | `2` |

From those three registers, we read off the Sign Bit $S = 1$ (negative), the Biased Exponent $E = \text{81h}$ ($129_{10} \implies e = 129 - 127 = \mathbf{2}$), and the Fractional Mantissa $M = \text{480000h}$ ($\frac{4,718,592}{2^{23}} = 0.5625 = \frac{9}{16}$), reconstructing $(-1)^1 \times 2^2 \times (1 + 0.5625) = -4 \times 1.5625 = \mathbf{-6.25}$.

---

### Floating-Point Encodings, Cryptography & Memory Architecture

We conclude with 64-bit double-precision IEEE-754 float unpacking and cryptographic circular bit rotations (`ROL`) via modular division.

#### IEEE-754 64-Bit Double Precision Float Unpacking
When scientific software upgrades from 32-bit `float` to 64-bit `double` (`binary64`), IEEE-754 widens the biased exponent from 8 bits (bias $127$) to **11 bits** (bias $1023$) and expands the fractional mantissa from 23 bits to **52 bits** (with the top 20 mantissa bits stored in the upper 32-bit word). Let's decompose the double-precision float value $-13.375$:
1. $13.375_{10} = 8 + 4 + 1 + 0.25 + 0.125 = 1101.011_2 = 1.101011_2 \times 2^3$.
2. Sign $S = 1$.
3. Biased Exponent: $3 + 1023 = 1026_{10} = 10000000010_2 = \mathbf{402h}$.
4. Fractional Mantissa (52 bits): $101011000000\dots0_2$.
5. Assembled Hex Word: **`0xC02AC00000000000`** (High 32-bit Word: `0xC02AC000`).

In William Kahan's IEEE-754 binary64 format, the upper 32-bit word packs a 1-bit sign, an 11-bit excess-1023 exponent, and the top 20 bits of the 52-bit significand. Working in `{{key:HEX}}` mode and chaining two modular divisions (`C02AC000 {{key:ENTER}} 100000 {{key:÷R}} 800 {{key:÷R}}`)—first `100000 {{key:÷R}}` ($2^{20}$) to drop the 20-bit significand fraction `AC000h` into Register $Y$, then `800 {{key:÷R}}` ($2^{11}$) on the upper 12 bits—places the unpacked fields across three adjacent stack registers in one pass: Sign $S = \mathbf{1}$ (`1h`) in $X$, Biased Exponent $E = \mathbf{\text{402h}}$ ($1026_{10} \implies e = 1026 - 1023 = \mathbf{3}$) in $Y$, and upper significand bits `AC000h` ($\frac{704,512}{2^{20}} = 0.671875 = \frac{43}{64}$) in $Z$, reconstructing $(-1)^1 \times 2^3 \times (1 + 0.671875) = -8 \times 1.671875 = \mathbf{-13.375}$.

#### Circular Left Rotation (ROL 1) on an 8-Bit Byte via `{{key:÷R}}`
In cryptographic hash functions (such as SHA-256 and ChaCha20), plain bit-shifts (`<<` or `>>`) are avoided because bits that slide off the edge of the register are lost forever, destroying information entropy. Instead, ciphers use **circular bit rotations** (`ROL` and `ROR`), where the bit pushed off the most-significant end wraps around and enters the least-significant end. Let's rotate the 8-bit byte `0x85` ($10000101_2$) left by 1 bit ($\implies 00001011_2 = \text{0Bh}$) in `{{key:HEX}}` mode using `{{key:÷R}}` at the 8-bit boundary $2^8 = \text{100h}$:
1. Shift left by 1 bit: `{{res:sc32_10_computer_science_bases_seq_50:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_50:value}}`.
2. Split 8-bit remainder (`0Ah` in $Y$) and overflow carry (`1h` in $X$) via `{{key:÷R}}`: `{{res:sc32_10_computer_science_bases_seq_51:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_51:value}}`.
3. Add carry into LSB: `{{res:sc32_10_computer_science_bases_seq_52:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_52:value}}`**.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `85 {{key:ENTER}} 2 {{key:×}}` | `0h` | `0h` | `0h` | **`10Ah`** | Shift byte left by 1 bit ($85\text{h} \times 2 = 10\text{Ah}$) |
| 02 | `100 {{key:÷R}}` | `0h` | `0h` | `Ah` | **`1h`** | Extract carry bit ($X=1\text{h}$) and rotated byte ($Y=\text{Ah}$) |
| 03 | `{{key:+}}` | `0h` | `0h` | `0h` | **`Bh`** | Add carry bit into LSB: $10\text{Ah} \bmod 100\text{h} + 1\text{h} = \text{Ah} + 1\text{h} = \text{Bh}$ |

> **Circular Bit Rotation (`ROL`) as a Meshing Gear Ring:** A circular left bit-rotation (`ROL 1`) is the binary equivalent of indexing a closed 256-state mechanical drum or **Planetary Geared Clock** ring gear by one step: multiplying by $2$ advances the state around the cylinder, `100 {{key:÷R}}` splits the wrap-around tooth carry (`1h` in Register $X$) from the in-range modulo-256 remainder (`Ah` in Register $Y$), and `{{key:+}}` feeds the wrapped bit back into Bit 0 so no information ever falls off the edge of the word.

---

## Further Exploration: Companion Workbooks & Applied Tie-Ins

> *For 24 additional worked engineering problems with full 4-register stack traces, see Chapter 10 of the [SC-32 Scientific Companion Problem & Casebook Workbook](../../curriculum/sc32-scientific-companion-workbook.md#chapter-10).*


To extend the 36-bit integer, modular bitfield (`{{key:÷R}}`), and network addressing workflows from this chapter into full embedded firmware and contest applications, consult these companion volumes:

- **StackCalc Embedded Systems & Firmware Casebook (Module 1: Peripheral Bitfields, Fixed-Point DSP & Protocol Checksums):** Covers ARM Cortex-M33 register bit-banding, Q16.16/Q8.24 fixed-point filter scaling, CAN-FD bit-timing dividers, and RFC 1071 packet checksum verification.
- **Timed Computer Science & Number Sense Competition Workbook (Section B: Radix Conversions, Modular Arithmetic & Combinatorics):** Provides high-speed drills on base-$b$ conversions, Euclidean division chains via `{{key:÷R}}`, and combinatorial code-sphere counting.

### Synthesis Challenge Problems

1. **Single-Entry RGB565 Full Unpacking Cascade:** Given the 16-bit RGB565 pixel `0xF38E` in `{{key:HEX}}` mode, unpack all three color channels ($R_5, G_6, B_5$) onto the stack in a single 9-keystroke stream by typing `F38E` only once: `F38E {{key:ENTER}} 800 {{key:÷R}} {{key:x⇄y}} 20 {{key:÷R}}`. Verify that Register $Z$ holds Red (`1Eh` $= 30_{10}$), Register $X$ holds Green (`1Ch` $= 28_{10}$), and Register $Y$ holds Blue (`Eh` $= 14_{10}$).
2. **Stirling Relative Error Audit via `{{key:LASTX}}`:** In `{{key:DEC}}` mode, compute $12!$ via `12 {{key:PROB}} {{key:x!}}`, then recover $n = 12$ from `{{key:LASTX}}` to evaluate Stirling's approximation $\sqrt{2\pi n}(n/e)^n$ and verify that the ratio $n! / \text{Stirling}(n)$ matches $e^{1/(12n)} \approx 1.00697$ without re-typing `12`.
3. **Double-Carry RFC 1071 Checksum Fold:** If a 32-bit TCP pseudo-header sum is `0x1FFFF`, a single 16-bit fold `1FFFF {{key:ENTER}} 10000 {{key:÷R}} {{key:+}}` produces `10000h`, which itself carries into Bit 16. Apply a second `10000 {{key:÷R}} {{key:+}}` fold and subtract from `FFFFh` (`FFFF {{key:x⇄y}} {{key:-}}`) to verify that the one's-complement checksum is `FFFEh`.

---

## Summary & Looking Ahead

Operating across a 36-bit two's complement integer architecture preserves multi-level stack register values intact across Hexadecimal, Decimal, Octal, and Binary modes. Modular integer division via `{{key:÷R}}`—returning the quotient in $X$ and remainder in $Y$—combines with word-length masking, modular reduction, and powers-of-two arithmetic to configure microcontroller registers, construct IPv4 CIDR subnet masks, pack and extract RGB color channels, and analyze telemetry bit disparities alongside discrete combinatorics ($nPr$, $nCr$, $n!$) and pseudorandom seeding.

From discrete bits and memory registers, the positional mathematics of radix scaling extends directly into quantitative economics and capital valuation. Notice the structural isomorphism as we cross into **Part IV (Applied STEM, Finance & Visual Modeling)**: **just as positional base-2 and base-16 arithmetic weights each column of the Place Value Cubes tray by a constant radix power $b^k$, financial time-value-of-money weights each cash flow across time by an exponential compounding or discount power $(1 + i)^{-k}$.** That means the exact same Horner polynomial nesting (`(a·b + c)·b + d`) that packed hexadecimal bytes in this chapter will discount multi-year corporate cash-flow streams in a single pass. In **[Chapter 11: Financial Mathematics & Time Value of Money (TVM)](11-financial-tvm.md)**, you will master both direct stack annuity formulas and the SC-32's dedicated five-variable compound interest solver ($N, I\%YR, PV, PMT, FV$) to calculate mortgage amortization schedules, net present value (NPV), internal rate of return (IRR), and real-world capital flows.

