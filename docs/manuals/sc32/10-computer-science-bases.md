---
title: "Chapter 10: Computer Science, Bases & 36-Bit Integers | SC-32 Manual"
description: "36-bit two's complement integer architecture, base conversions (HEX, DEC, OCT, BIN), integer division & remainder bit-field extraction (÷R), CIDR IPv4 subnetting, RGB565 packing, combinatorics, and PRNG on the StackCalc SC-32."
---

# Chapter 10: Computer Science, Bases & 36-Bit Integers

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 COMPUTER SCIENCE // 36-BIT ARCHITECTURE &amp; DISCRETE MATH</span>
  <span class="te-viewport-status text-sky-400">● 36-BIT TWO'S COMPLEMENT &bull; DYNAMIC BASE MODES &bull; CIDR SUBNETTING &bull; BIT-FIELD ARITHMETIC</span>
</div>

## Claude Shannon's 1937 Switchboard Epiphany & Why Classic Mainframes Used 36-Bit Words

In the summer of 1936, a twenty-one-year-old graduate student named **Claude Elwood Shannon** was working in the basement of MIT's electrical engineering building. His task was operating Vannevar Bush's Differential Analyzer—a colossal mechanical analog computer composed of spinning steel discs, brass gears, and motorized lead screws that solved differential equations through physical rotation.

To reset the machine for each differential run, Shannon had to rewire complex arrays of electromechanical telephone relays.

As Shannon manipulated the clicking relays, he recalled an obscure 1854 treatise by British mathematician George Boole, *An Investigation of the Laws of Thought*, which he had studied in an undergraduate philosophy course at the University of Michigan. Boole had formulated an abstract algebraic system where variables took only two truth values: $1$ (True) or $0$ (False).

In a sudden flash of insight, Shannon realized: **a telephone relay is not merely an electrical switch—it is a physical instantiation of binary arithmetic and two-state logic!**

In his 1937 MIT master's thesis—published in 1938 {{cite:shannon1938}} and subsequently hailed by computer scientist Howard Gardner as "possibly the most important, and also the most famous, master's thesis of the century"—Shannon proved that any mathematical or logical expression can be evaluated by an arrangement of physical binary switches. Every microprocessor, FPGA, and memory cell built in the past nine decades traces its intellectual lineage directly to Shannon's switchboard epiphany.

### The Architectural Drama: The 36-Bit Word vs. The 8-Bit Byte

When scientific mainframe pioneers at IBM, MIT, and Digital Equipment Corporation engineered the legendary machines of the 1950s and 1960s—the IBM 704, IBM 7094, and DEC PDP-10—they converged on a word length that seems curious to modern programmers accustomed to 32-bit and 64-bit boundaries: **the 36-bit word**.

Why 36 bits?

In that era, computers processed floating-point scientific calculations and alphabetic text concurrently. Thirty-six bits was mathematical perfection:
1. **Ten Decimal Digits of Scientific Precision:** $2^{36} \approx 6.87 \times 10^{10}$, granting ten certified decimal digits of integer and mantissa precision.
2. **Six 6-Bit Characters:** Standard alphanumeric teleprinters encoded text in 6-bit BCD (Fieldata/ASCII-6). A 36-bit word packed exactly six characters with zero wasted silicon.
3. **Dual 18-Bit Pointers:** The PDP-10 split its 36-bit words into two symmetric 18-bit halves, allowing instructions to hold both a left register address and a right memory pointer simultaneously.

When IBM introduced the System/360 in 1964, Gene Amdahl and Fred Brooks shifted commercial computing to 8-bit bytes and 32-bit words to streamline commercial billing and byte-stream peripherals. Yet in aerospace telemetry, radar processing, and scientific research, the 36-bit word remained legendary for its graceful handling of precision and unsigned headroom.

The StackCalc SC-32 honors this golden architectural heritage. Rather than confining programmers to signed 32-bit limits that choke on unsigned `0xFFFFFFFF` network masks, the SC-32 provides an authentic **36-bit two's complement integer architecture**.

{{blocks:prime_lcm_gcd_venn|Prime LCM and GCD Venn Diagram}}
*Figure 10.1: Prime factorization and set intersection modeling. Discrete number-theoretic operations map directly to modular division and radix partitioning.*

{{blocks:counting_tiles_box_3x1x13u|Counting Tiles Physical Packaging 3x1x13}}
*Figure 10.2: Concrete physical unit packaging representing modular grouping and discrete word-length partitioning across physical registers.*

<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>{{key:DEC}}</code> (Decimal integer base default; 36-Bit Two's Complement Integer Architecture; Full precision <code>{{key:ALL}}</code>). Switching dynamically between <code>{{key:HEX}}</code>, <code>{{key:DEC}}</code>, <code>{{key:OCT}}</code>, and <code>{{key:BIN}}</code> preserves all four stack registers ($X, Y, Z, T$) with zero data corruption.
</div>

---

{{res:sc32_hex_255:screenshot|Decimal 255 converted to hexadecimal FFh}}

## The 36-Bit Two's Complement Integer Architecture

In digital electronics, systems programming, firmware development, and network engineering, calculations operate directly upon discrete binary registers rather than continuous floating-point approximations.

The StackCalc SC-32 incorporates an authentic hardware-modeled **36-Bit Two's Complement Integer Architecture**:

| Bit Position | Field Designation | Meaning in 36-Bit Two's Complement |
| :---: | :---: | :--- |
| **Bit 35** | `MSB` / Sign Bit | `0` = Positive integer; `1` = Negative integer (Two's complement) |
| **Bits 34–32** | Upper Headroom | Provides 4 full bits of positive headroom above standard 32-bit unsigned words |
| **Bits 31–0** | Standard 32-Bit Word | Holds full 32-bit unsigned addresses, IPv4 netmasks, and GPIO bitfields |

* **Word Size ($W$):** Exactly 36 bits ($0$ to $35$).
* **Maximum Value ($+2^{35} - 1$):** $+34,359,738,367$ (`0x7FFFFFFFF`).
* **Minimum Value ($-2^{35}$):** $-34,359,738,368$ (`0x800000000`).
* **$-1$ Representation:** `0xFFFFFFFFF` (all 36 bits set to 1).
* **Overflow Handling:** Values exceeding 36 bits trigger the non-destructive status annunciator `TOO BIG`.

### Why 36 Bits?
The 36-bit word length honors legendary scientific mainframe computing heritage (such as the DEC PDP-10, IBM 7090, and MIT Project MAC architectures) while providing crucial engineering utility in modern embedded digital design:
1. **Full 32-Bit Unsigned Headroom:** Traditional 32-bit signed calculators overflow when representing unsigned 32-bit addresses and masks (such as IPv4 broadcast `0xFFFFFFFF` or 4 GiB memory bounds). A 36-bit architecture represents any 32-bit unsigned integer up to `0xFFFFFFFF` ($4,294,967,295$) with 4 full bits of positive headroom before the sign bit is reached.
2. **Parity & Status Bit Packing:** It provides 4 dedicated upper bits for hardware error detection, cyclic redundancy codes, and register bank tags without stealing bits from 32-bit payloads.
3. **Exact Integer Arithmetic:** Integers in `HEX`, `OCT`, and `BIN` modes are maintained as exact 36-bit two's complement words internally, guaranteeing that integer division, remainder extraction, and radix conversions never suffer floating-point roundoff errors.

---

## Dynamic Base Modes (`HEX`, `DEC`, `OCT`, `BIN`)

Following the classic HP-32SII architecture, the SC-32 `{{key:BASE}}` menu (accessed via Left Shift `{{key:↰}}` on the multiplication key `{{key:×}}`, Row 5, Column 3) provides four radix modes without cluttering the menu with separate Boolean gate keys:

| Base System | Keystroke | Screen Suffix | Allowed Character Digits | Example Formatted Display |
| :--- | :--- | :---: | :--- | :--- |
| **Decimal** | `{{key:BASE}} {{key:DEC}}` | *(none)* | `0` through `9` | `1042` |
| **Hexadecimal** | `{{key:BASE}} {{key:HEX}}` | `h` | `0` through `9`, `A` through `F` | `412h` |
| **Octal** | `{{key:BASE}} {{key:OCT}}` | `o` | `0` through `7` | `2022o` |
| **Binary** | `{{key:BASE}} {{key:BIN}}` | `b` | `0` and `1` | `10000010010b` |

### The Stack Preservation Invariant
Switching between base modes **never destroys, alters, or shifts the values in the operational stack ($X, Y, Z, T$)**.
* If Register $X$ holds `255` in Decimal mode, pressing `{{key:BASE}} {{key:HEX}}` instantly renders `FFh`.
* Pressing `{{key:BASE}} {{key:OCT}}` immediately renders `377o`.
* Pressing `{{key:BASE}} {{key:BIN}}` immediately renders `11111111b`.
* The underlying 36-bit integer representation in CPU registers remains identical.

### Direct Hexadecimal Digit Input (`A` through `F`)
When Hexadecimal mode (`{{key:HEX}}`) is active, the top row of primary scientific keys (Row 1, Columns 0 through 5) maps directly to the printed alpha legends $A$ through $F$:
* `{{key:√x}}` $\to \mathbf{A}$ ($10_{10}$)
* `{{key:eˣ}}` $\to \mathbf{B}$ ($11_{10}$)
* `{{key:LN}}` $\to \mathbf{C}$ ($12_{10}$)
* `{{key:yˣ}}` $\to \mathbf{D}$ ($13_{10}$)
* `{{key:1/x}}` $\to \mathbf{E}$ ($14_{10}$)
* `{{key:Σ+}}` $\to \mathbf{F}$ ($15_{10}$)

To type `0xDEADBEEF`: Key `{{key:yˣ}} {{key:1/x}} {{key:√x}} {{key:yˣ}} {{key:eˣ}} {{key:1/x}} {{key:1/x}} {{key:Σ+}}`!

<div class="admonition tip">
<p class="admonition-title">Rapid Calculation &amp; Equation Entry: Rapid Radix Conversion Without Stack Interruption</p>
<p>
In high-speed computer science sprints and collegiate numerical exams, base conversion problems (such as evaluating $3\text{A}7_{16} + 452_8$ in decimal) can consume precious minutes if converted on scratch paper.
</p>
<p>
On the SC-32, the entire 4-register operational stack preserves all values when cycling base modes. You can convert radices mid-expression without losing running operands:
</p>
<ol>
  <li>Switch to Hex: <code>{{key:BASE}} {{key:HEX}}</code> &rarr; Key <code>3 {{key:√x}} 7 {{key:ENTER}}</code> ($3\text{A}7_{16} = 935_{10}$).</li>
  <li>Switch to Octal: <code>{{key:BASE}} {{key:OCT}}</code> &rarr; Key <code>452 {{key:+}}</code>. Register $X$ instantly sums them in octal: $2261_8$.</li>
  <li>Switch to Decimal: <code>{{key:BASE}} {{key:DEC}}</code> &rarr; Register $X$ immediately reads <strong>$1,201_{10}$</strong> with zero intermediate scratchpad steps!</li>
</ol>
<p>
Because stack lift and numeric precision are invariant across base toggles, you never have to re-enter running totals or exit the calculation chain.
</p>
</div>

---

## Bit-Field Extraction, Shifting & Masking on the RPN Stack

Just as the original HP-32SII focused its `BASE` menu purely on radix representation (`DEC`, `HEX`, `OCT`, `BIN`), the SC-32 performs bit-shifting, bit-field masking, and register packing directly through 36-bit integer arithmetic (`{{key:+}}`, `{{key:-}}`, `{{key:×}}`, `{{key:÷}}`, `{{key:+/-}}`) and simultaneous integer division with remainder (`{{key:÷R}}`):

| Bit-Field / Masking Operation | Mathematical Equivalent ($M = 2^k$) | SC-32 RPN Keystrokes (`HEX` / `DEC`) | Result Location |
| :--- | :---: | :--- | :--- |
| **Left Shift ($X \ll k$)** | $X \times 2^k$ | `X {{key:ENTER}} M {{key:×}}` | Shifted word in **`X`** |
| **Right Shift ($X \gg k$)** | $\lfloor X / 2^k \rfloor$ | `X {{key:ENTER}} M {{key:÷}}` (or `{{key:÷R}}`) | Upper bits in **`X`** |
| **Low-Bit Mask ($X \ \& \ (2^k - 1)$)** | $X \bmod 2^k$ | `X {{key:ENTER}} M {{key:÷R}} {{key:x⇄y}}` | Low $k$ bits in **`X`** |
| **High-Bit Alignment ($X \ \& \ \sim(2^k - 1)$)** | $\lfloor X / 2^k \rfloor \times 2^k$ | `X {{key:ENTER}} M {{key:÷R}} M {{key:×}}` | Aligned base in **`X`** |
| **Set Disjoint Bit $k$** | $X + 2^k$ | `X {{key:ENTER}} M {{key:+}}` | Updated word in **`X`** |
| **Clear Set Bit $k$** | $X - 2^k$ | `X {{key:ENTER}} M {{key:-}}` | Updated word in **`X`** |
| **32-Bit Unsigned Complement** | $\text{FFFFFFFF}_{16} - X$ | `FFFFFFFF {{key:ENTER}} X {{key:-}}` | Inverted mask in **`X`** |

### Why `{{key:÷R}}` Is a Bit-Field Superpower
When you divide a binary word $Y$ by a power of two $M = 2^k$ using `{{key:÷R}}`, the SC-32 splits the binary word right at bit boundary $k$ in a single keystroke:
* **Register `X` (Quotient $\lfloor Y / 2^k \rfloor$):** Holds the **upper bits** shifted right by $k$ positions ($Y \gg k$).
* **Register `Y` (Remainder $Y \bmod 2^k$):** Holds the **lower $k$ bits** masked off ($Y \ \& \ (2^k - 1)$).

---

### The Algebraic Trap vs. StackCalc Superpower Showdown

| Challenge / Metric | Algebraic Trap (TI-84 / Infix) | Algebraic Strokes | StackCalc SC-32 Superpower | SC-32 Strokes | Superpower Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **IPv4 Subnet Partitioning**: Split `192.168.10.45` (`C0A80A2Dh`) into `/24` network ID & host offset | Manual integer truncation: `int(C0A80A2D / 100)` followed by subtract-and-multiply remainder `C0A80A2D - Ans * 100` (28 strokes). Stack is invisible. | 28 | **Simultaneous Division with Remainder (`{{key:÷R}}`)**: Key `C0A80A2D ENTER 100 ÷R` (11 strokes). Network prefix in $X$, host offset in $Y$ instantly! | 11 | **60% fewer strokes + single-cycle quotient/remainder split** |
| **Multi-Base Radix Inspection**: Convert decimal `3735928559` to Hex, Octal, and Binary | Navigate nested `MATH` $\to$ `Base` submenus for each radix or run manual iterative division. Stack history is discarded or obscured (26+ strokes). | 26 | **Native 36-Bit Base Engine**: Press `{{key:BASE}} {{key:HEX}}`, `{{key:OCT}}`, `{{key:BIN}}` (4 strokes). All 4 stack levels ($X, Y, Z, T$) convert losslessly in place. | 4 | **85% fewer strokes + continuous multi-register stack preservation** |
| **RGB Color Bit-Field Packing**: Pack Red ($255$), Green ($128$), Blue ($64$) into `FF8040h` | Algebraic nesting: `255 * 256 ^ 2 + 128 * 256 + 64` (24 strokes). Requires parenthesis and operator precedence verification. | 24 | **Positional RPN Pipeline**: `255 ENTER 100 × 128 + 100 × 64 +` (14 strokes). Streamlined linear pipeline, zero parentheses, instant nibble inspection. | 14 | **42% fewer strokes + zero parenthesis clutter** |

---

## Diagnostic Checkpoints & Singularity Handling

> [!CHECKPOINT]
> **Diagnostic Checkpoint 10.1: Integer Base Suffix Identification**  
> * `h` suffix indicates Hexadecimal (`FFh` = $255$).
> * `o` suffix indicates Octal (`377o` = $255$).
> * `b` suffix indicates Binary (`11111111b` = $255$).
> * No suffix indicates Decimal.

> [!CHECKPOINT]
> **Diagnostic Checkpoint 10.2: Two's Complement Negative Representation**  
> In `{{key:HEX}}` mode, key `1 {{key:+/-}}`. The display outputs `FFFFFFFFFh` ($36$ ones).

> [!CHECKPOINT]
> **Diagnostic Checkpoint 10.3: Unsigned 32-Bit Range Headroom**  
> Because the SC-32 uses an authentic 36-bit architecture, unsigned 32-bit values like `0xFFFFFFFF` ($4,294,967,295$) do NOT flip into negative numbers! They remain strictly positive with 4 bits of headroom.

> [!CHECKPOINT]
> **Diagnostic Checkpoint 10.4: Hexadecimal Digit Collision Safety**  
> When Hexadecimal mode is active, numeric keys `0...9` enter digits, and the top scientific row keys (`{{key:√x}}` through `{{key:Σ+}}`) enter hex letters `A...F`. To perform scientific operations on hex numbers, first switch to Decimal mode `{{key:BASE}} {{key:DEC}}`.

---

## Teaching & Instrument Architecture Notes

### Two's Complement Foundations & Modulo Odometer Intuition
Two's complement is often perceived as an arbitrary binary convention, but it is fundamentally the radix complement of base 2, mathematically isomorphic to ten's complement in decimal arithmetic. In a four-digit decimal register ($0000 \dots 9999$), subtracting $1$ from $0000$ rolls backward to $9999$, which represents $-1$. In a 36-bit binary word, subtracting $1$ from $0$ rolls over to all ones (`0xFFFFFFFFF`), which evaluates mathematically to $-1$. In RPN computer science pedagogy, students inspect bitfield transformations sequentially: partitioning nibbles via simultaneous quotient and remainder with `{{key:÷R}}`, executing bit shifts via power-of-two multiplication and division, and verifying register alignment without hidden precedence rules.

### Bitfield Manipulation via Positional Weights
Binary flags and bitmasks represent weighted combinations of powers of two ($1, 2, 4, 8, 16, 32, 64, 128 \dots$). Setting or clearing individual bits corresponds directly to adding or subtracting powers of two:
1. **Setting Bit $k$:** Adding $2^k$ sets bit $k$ without altering adjacent fields. Switching to `{{key:BIN}}` confirms that bit $k$ flips from `0` to `1`.
2. **Clearing Bit $k$:** Subtracting $2^k$ clears bit $k$ back to `0` while preserving surrounding state.
3. **Partitioning Bitfields:** Dividing by $2^k$ via `{{key:÷R}}` separates the word: the upper bits shifted right reside in Register $X$, while the lower $k$ bits remain in Register $Y$.
This confirms that digital systems manipulate composite state registers through the positional mathematics of powers of two rather than isolated logic switches.

### 36-Bit Architecture & IPv4 Headroom
The SC-32 advances classic base-conversion instruments (such as the HP-32SII) by employing a 36-bit two's complement integer word. On standard 32-bit signed architectures, the IPv4 broadcast address `0xFFFFFFFF` ($4,294,967,295$) cannot be represented as a positive integer; its leading bit forces an overflow into $-1$. On the SC-32, Bit 35 serves as the sign bit, providing 4 full bits of positive headroom above the standard 32-bit boundary. Furthermore, switching dynamically between `{{key:HEX}}`, `{{key:DEC}}`, `{{key:OCT}}`, and `{{key:BIN}}` preserves all four operational stack levels ($X, Y, Z, T$) with zero truncation or register loss.

---

## Engineering Design Briefing: Bare-Metal Embedded Firmware & High-Performance Network Switching (Problems 10.1 through 10.40)

<div class="admonition warning">
<p class="admonition-title">Inside-Out Stack Architecture: Algebraic Trap vs. RPN Shortcut — 36-Bit Integer Registers &amp; Subnet Boundary Partitioning via {{key:÷R}}</p>
<p><strong>The Algebraic Parenthesis Trap:</strong> In network engineering and embedded firmware development, calculating IPv4 CIDR subnet IDs or decomposing packed hardware telemetry words on standard scientific calculators is fraught with difficulty. Algebraic scientific calculators lack native quotient-remainder separation, forcing developers to alternate between floating-point division, manual integer truncation, and re-multiplication to isolate remainder bits {{cite:shannon1938}}.</p>
<p><strong>The RPN Stack Shortcut:</strong> The SC-32 provides native 36-bit two's complement integer architecture with instantaneous base conversions (<code>{{key:HEX}}</code>, <code>{{key:DEC}}</code>, <code>{{key:OCT}}</code>, <code>{{key:BIN}}</code>) across all four stack registers {{cite:ieee754_2019}}. Dividing a binary word by a power of two ($2^k$) using simultaneous division with remainder (<code>{{key:÷R}}</code>) automatically isolates the upper network prefix bits in Register $X$ while depositing the lower host field remainder directly into Register $Y$ in a single instruction cycle, completely eliminating manual bitmask scratchwork.</p>
</div>

The following 40 reference problems provide complete, publication-grade coverage across network engineering, microcontroller firmware, computer graphics, cryptography, and discrete mathematics.

---

> **Thematic Arc I — Network Addressing, Radix Conversions & Modular Packing (Problems 10.1–10.10):** We begin by switching effortlessly among `HEX`, `DEC`, `OCT`, and `BIN` to inspect IPv4 subnets, MAC addresses, and modular strides.

### Problem 10.1: Subnet Masking via Modular Division & Integer Bit-Packing
A network router receives an IPv4 packet destined for host octet `205`. The interface subnet mask octet is `240` (`/28` subnet). Determine the network subnet ID octet using modular remainder division ({{key:÷R}}).

$$205_{10} = 11001101_2$$
$$240_{10} = 11110000_2$$
$$205 \text{ AND } 240 = 11000000_2 = 192_{10}$$

**Keystrokes in `{{key:DEC}}` Mode:** `{{res:sc32_10_computer_science_bases_seq_03:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_03:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `205` | 0 | 0 | 0 | 205 | `205_` |
| 02 | `{{key:ENTER}}` | 0 | 0 | 205 | 205 | `205` |
| 03 | `16 {{key:÷R}}` | 0 | 0 | 13 | 12 | `12` |
| 04 | `16 {{key:×}}` | 0 | 0 | 13 | 192 | `192` |

---

### Problem 10.2: IPv4 CIDR /24 Subnet Network, Broadcast & Host Allocation
Given an IPv4 host address `192.168.10.45` with a `/24` subnet mask ($255.255.255.0$):
* In Hex: IP is `C0A80A2Dh`, Mask is `FFFFFF00h`, and block size is $2^{32-24} = 2^8 = 256_{10} = \text{100h}$.

| Field | Octet 1 (`192` / `C0h`) | Octet 2 (`168` / `A8h`) | Octet 3 (`10` / `0Ah`) | Octet 4 (`45` / `2Dh`) |
| :--- | :---: | :---: | :---: | :---: |
| **Host IP Bits** | `11000000` | `10101000` | `00001010` | `00101101` |
| **Subnet Mask (`/24`)** | `11111111` (Net) | `11111111` (Net) | `11111111` (Net) | `00000000` (Host) |
| **Aligned Network ID** | `11000000` (`192`) | `10101000` (`168`) | `00001010` (`10`) | `00000000` (`0`) |

**Keystrokes in `{{key:HEX}}` Mode:**
1. Network Address: `{{res:sc32_10_computer_science_bases_seq_04:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_04:value}}`** (`192.168.10.0`)
2. Wildcard Mask: `{{res:sc32_10_computer_science_bases_seq_05:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_05:value}}`** (`0.0.0.255`)
3. Broadcast Address: `{{res:sc32_10_computer_science_bases_seq_06:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_06:value}}`** (`192.168.10.255`)
4. Usable Hosts: $2^{32 - 24} - 2 = 2^8 - 2 = 256 - 2 = \mathbf{254\text{ hosts}}$ (`192.168.10.1` to `192.168.10.254`).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `C0A80A2D` | `0h` | `0h` | `0h` | `C0A80A2Dh` | `C0A80A2D_h` |
| 02 | `{{key:ENTER}}` | `0h` | `0h` | `C0A80A2Dh` | `C0A80A2Dh` | `C0A80A2Dh` |
| 03 | `100 {{key:÷R}}` | `0h` | `0h` | `2Dh` | `C0A80Ah` | `C0A80Ah` |
| 04 | `100 {{key:×}}` | `0h` | `0h` | `2Dh` | `C0A80A00h` | `C0A80A00h` |
| 05 | `FF {{key:+}}` | `0h` | `0h` | `2Dh` | `C0A80AFFh` | `C0A80AFFh` |

---

### Problem 10.3: IPv4 CIDR /27 Subnet (30 Usable Hosts)
A server has IP `10.20.30.142 /27`.
* $10 = \text{0Ah}, 20 = \text{14h}, 30 = \text{1Eh}, 142 = \text{8Eh} \implies \text{0A141E8Eh}$.
* Subnet Mask `/27`: $27$ ones, $5$ zeros $\implies$ block size $2^5 = 32_{10} = \text{20h}$ ($255.255.255.224$).

| Octet 4 Representation | Upper 3 Subnet Bits | Lower 5 Host Bits | Hex / Decimal Value |
| :--- | :---: | :---: | :--- |
| **Host Octet 4** | `100` | `01110` | `8Eh` ($142_{10}$) |
| **Subnet Mask (`/27`)** | `111` | `00000` | `E0h` ($224_{10}$) |
| **Network Base (`÷R 20h × 20h`)** | `100` | `00000` | `80h` ($128_{10}$) |
| **Broadcast (`+ 1Fh`)** | `100` | `11111` | `9Fh` ($159_{10}$) |

**Keystrokes in `{{key:HEX}}` Mode:**
1. `{{res:sc32_10_computer_science_bases_seq_07:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_07:value}}`** (`10.20.30.128`)
2. Wildcard mask: $32 - 27 = 5$ bits $\implies 2^5 - 1 = 31_{10} = \text{1Fh}$.
3. Broadcast: `{{res:sc32_10_computer_science_bases_seq_08:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_08:value}}`** (`10.20.30.159`)
4. Usable host range: **`10.20.30.129` through `10.20.30.158`** ($30$ usable hosts).

**Load Packed IPv4 Address:** In `{{key:HEX}}` mode, key `0A141E8E {{key:ENTER}}` to hold host IP `0A141E8Eh` (`10.20.30.142`) across Registers $Y$ and $X$ $(T: 0\text{h}, Z: 0\text{h}, Y: \text{A141E8Eh}, X: \text{A141E8Eh})$. **Partition at Subnet Boundary:** Key `20 {{key:÷R}}` to divide by block size $2^5 = 32_{10} = \text{20h}$, separating upper prefix bits in Register $X$ ($\text{50A0F4h}$) from lower host remainder $\text{Eh}$ in Register $Y$ $(T: 0\text{h}, Z: 0\text{h}, Y: \text{Eh}, X: \text{50A0F4h})$. **Align Subnet Base & Add Broadcast Offset:** Key `20 {{key:×}}` to align the network base $\text{A141E80h}$ (`10.20.30.128`), then key `1F {{key:+}}` to add wildcard offset $\text{1Fh}$ ($31_{10}$), reaching broadcast address $\mathbf{\text{A141E9Fh}}$ (`10.20.30.159`) in Register $X$.

---

### Problem 10.4: IPv4 Point-to-Point /30 Subnet (WAN Link)
A WAN router serial link connects two routers using `172.16.5.9 /30`.
* $172 = \text{ACh}, 16 = \text{10h}, 5 = \text{05h}, 9 = \text{09h} \implies \text{AC100509h}$.
* Subnet Mask `/30`: $30$ ones, $2$ zeros $\implies$ block size $2^2 = 4_{10} = \text{4h}$ ($255.255.255.252$).

**Keystrokes in `{{key:HEX}}` Mode:**
1. `{{res:sc32_10_computer_science_bases_seq_09:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_09:value}}`** (`172.16.5.8`)
2. Wildcard: $2^2 - 1 = 3 = \text{03h}$.
3. Broadcast: `{{res:sc32_10_computer_science_bases_seq_10:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_10:value}}`** (`172.16.5.11`)
4. Router A interface: `172.16.5.9`, Router B interface: `172.16.5.10` ($2$ usable hosts).

**Load Point-to-Point Host IP:** In `{{key:HEX}}` mode, key `AC100509 {{key:ENTER}}` to duplicate `AC100509h` (`172.16.5.9`) into Registers $Y$ and $X$. **Partition `/30` Subnet via `{{key:÷R}}`:** Key `4 {{key:÷R}}` to divide by /30 block size $2^2 = 4\text{h}$, extracting host index $1\text{h}$ into Register $Y$ and upper network prefix quotient $\text{2B040142h}$ into Register $X$ $(T: 0\text{h}, Z: 0\text{h}, Y: 1\text{h}, X: \text{2B040142h})$. **Reconstruct Network & Broadcast IDs:** Key `4 {{key:×}}` to recover network address $\mathbf{\text{AC100508h}}$ (`172.16.5.8`), then strike `3 {{key:+}}` to yield WAN broadcast address $\mathbf{\text{AC10050Bh}}$ (`172.16.5.11`) with zero intermediate notes.

---

### Problem 10.5: IPv4 Host Route (/32) and Loopback
A BGP loopback interface is assigned `198.51.100.1 /32`.
* In Hex: IP is `C6336401h`, Mask is `FFFFFFFFh` ($255.255.255.255$).
* Network ID = Host IP = Broadcast = `198.51.100.1` (`C6336401h`).
* Usable hosts: $2^{32-32} = 2^0 = \mathbf{1\text{ host}}$.

**Keystrokes in `{{key:HEX}}` & `{{key:DEC}}` Modes:**
1. Load Host IP: `C6336401 {{key:ENTER}}` $\rightarrow$ `C6336401h`
2. Wildcard mask: `FFFFFFFF {{key:ENTER}} FFFFFFFF {{key:-}}` $\rightarrow$ `0h` (`0.0.0.0`)
3. Broadcast Address: `{{key:+}}` $\rightarrow$ **`C6336401h`** (`198.51.100.1`)
4. Host Capacity: Switch to `{{key:DEC}}`, `2 {{key:ENTER}} 0 {{key:yˣ}}` $\rightarrow$ **`1`**.

**Load Loopback Host IP:** Key `C6336401 {{key:ENTER}}` to position `198.51.100.1` on the stack $(T: 0\text{h}, Z: 0\text{h}, Y: \text{C6336401h}, X: \text{C6336401h})$. **Complement /32 Mask:** Key `FFFFFFFF {{key:ENTER}} FFFFFFFF {{key:-}}` to subtract all-ones mask from itself, establishing wildcard mask $0\text{h}$ (`0.0.0.0`) in Register $X$. **Add Wildcard & Verify Capacity:** Press `{{key:+}}` to confirm broadcast address $\mathbf{\text{C6336401h}}$, then switch to `{{key:BASE}} {{key:DEC}}` and evaluate `2 {{key:ENTER}} 0 {{key:yˣ}}` to verify host capacity of exactly $\mathbf{1}$ in Register $X$.

---

### Problem 10.6: CIDR Route Aggregation (Supernetting)
An ISP wants to summarize four contiguous subnets into a single route:
* Subnet 1: `192.168.16.0 /24` (`C0A81000h`)
* Subnet 2: `192.168.17.0 /24` (`C0A81100h`)
* Subnet 3: `192.168.18.0 /24` (`C0A81200h`)
* Subnet 4: `192.168.19.0 /24` (`C0A81300h`)

Inspect the third octet:
$16 = 00010000_2$, $17 = 00010001_2$, $18 = 00010010_2$, $19 = 00010011_2$.
The upper 6 bits ($000100_2$) are identical across all four routes!
New network mask length: $16 + 6 = \mathbf{22\text{ bits}}$ (`/22`).
Supernet Mask: `255.255.252.0` (`FFFFFC00h`).
Summarized Route: **`192.168.16.0 /22`**.

**Keystrokes in `{{key:HEX}}` Mode:**
1. Base Network ID: `C0A81000 {{key:ENTER}}` $\rightarrow$ `C0A81000h` (`192.168.16.0`)
2. Supernet block span: `4 {{key:ENTER}} 100 {{key:×}}` $\rightarrow$ `400h` ($1024_{10}$ addresses)
3. Wildcard Mask: `1 {{key:-}}` $\rightarrow$ `3FFh` (`0.0.3.255`)
4. Broadcast Address: `{{key:+}}` $\rightarrow$ **`C0A813FFh`** (`192.168.19.255`)
5. Usable Hosts: `3FF {{key:ENTER}} 1 {{key:-}}` $\rightarrow$ **`3FEh`** ($1022_{10}$ hosts).

**Load Base Network & Compute Span:** Key `C0A81000 {{key:ENTER}}` followed by `4 {{key:ENTER}} 100 {{key:×}}` to establish the 4-subnet address span $4 \times 256 = 1024$ (`400h`) in Register $X$ $(T: 0\text{h}, Z: \text{C0A81000h}, Y: 4\text{h}, X: 400\text{h})$. **Derive Supernet Wildcard Mask:** Key `1 {{key:-}}` to compute wildcard offset $\text{3FFh}$ (`0.0.3.255`), holding base address `C0A81000h` safely in Register $Y$. **Evaluate Supernet Broadcast & Usable Hosts:** Press `{{key:+}}` to add wildcard offset to base address, producing supernet broadcast address $\mathbf{\text{C0A813FFh}}$ (`192.168.19.255`). Keying `3FF {{key:ENTER}} 1 {{key:-}}` yields $\mathbf{\text{3FEh}}$ ($1022_{10}$ usable hosts) directly.

---

### Problem 10.7: Wildcard Mask Generation via 32-Bit Complement Subtraction
In Cisco ACLs, calculate the wildcard mask for `/26` ($255.255.255.192$):
1. In `{{key:HEX}}`: Mask is `FFFFFFC0h`.
2. Subtract from the 32-bit all-ones mask `FFFFFFFFh`: key `FFFFFFFF {{key:ENTER}} FFFFFFC0 {{key:-}}` $\rightarrow$ `3Fh`.
3. In `{{key:DEC}}`: `3Fh` = **`63`**.
4. Dotted decimal wildcard: `0.0.0.63`.

**Load Inversion Mask:** In `{{key:HEX}}` mode, key `FFFFFFFF {{key:ENTER}}` to place the 32-bit all-ones mask in Registers $Y$ and $X$ $(T: 0\text{h}, Z: 0\text{h}, Y: \text{FFFFFFFFh}, X: \text{FFFFFFFFh})$. **Perform Complement Subtraction:** Key `FFFFFFC0 {{key:-}}` to subtract the /26 netmask, leaving exact wildcard offset $\text{3Fh}$ in Register $X$ $(T: 0\text{h}, Z: 0\text{h}, Y: 0\text{h}, X: \text{3Fh})$. **Convert to Decimal:** Press `{{key:BASE}} {{key:DEC}}` to convert $\text{3Fh}$ to decimal $\mathbf{63}$, establishing Cisco ACL wildcard notation `0.0.0.63`.

---

### Problem 10.8: Embedded GPIO Pin Bit-Setting (`+`)
In a 32-bit GPIO direction register (`GPIO_DIR`), set Bit 5 (Output enable for status LED, currently $0$) while preserving all other pin configurations.
Current register value: `0x00001804`. Bit 5 weight: $2^5 = 32_{10} = \text{20h}$.

| Register Stage | Binary Representation (Bits 15–0) | Hexadecimal Value |
| :--- | :---: | :---: |
| **Original Register** | `0001 1000 0000 0100` | `1804h` |
| **Bit 5 Weight ($2^5$)** | `0000 0000 0010 0000` | `0020h` |
| **Updated Register (`+`)** | `0001 1000 0010 0100` | **`1824h`** |

**Keystrokes in `{{key:HEX}}` Mode:** `{{res:sc32_10_computer_science_bases_seq_11:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_11:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `1804` | `0h` | `0h` | `0h` | `1804h` | `1804_h` |
| 02 | `{{key:ENTER}}` | `0h` | `0h` | `1804h` | `1804h` | `1804h` |
| 03 | `20` | `0h` | `0h` | `1804h` | `20h` | `20_h` |
| 04 | `{{key:+}}` | `0h` | `0h` | `0h` | `1824h` | `1824h` |

---

### Problem 10.9: Embedded GPIO Pin Bit-Clearing (`-`)
Clear Bit 11 (Disable motor enable line, currently $1$) in register holding `0x00002F80`.
Bit 11 weight: $2^{11} = 2048_{10} = \text{800h}$.

**Keystrokes in `{{key:HEX}}` Mode:** `{{res:sc32_10_computer_science_bases_seq_12:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_12:value}}`**

**Load Register State:** In `{{key:HEX}}` mode, key `2F80 {{key:ENTER}}` to position initial register value `2F80h` in Registers $Y$ and $X$. **Clear Bit 11 via Power-of-Two Subtraction:** Key `800 {{key:-}}` to subtract bit weight $2^{11} = \text{800h}$, clearing bit 11 while preserving all other bits, yielding updated register state $\mathbf{\text{2780h}}$ in Register $X$ $(T: 0\text{h}, Z: 0\text{h}, Y: 0\text{h}, X: \text{2780h})$.

---

### Problem 10.10: Embedded GPIO Pin Bit-Cycling (`-` / `+`)
Cycle Bit 2 (Heartbeat pulse pin) in register holding `0x00000017`.
Bit 2 weight: $2^2 = 4 = \text{4h}$.

**Keystrokes in `{{key:HEX}}` Mode:**
1. Clear pulse bit: `{{res:sc32_10_computer_science_bases_seq_13:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_13:value}}`**
2. Set pulse bit again: `{{res:sc32_10_computer_science_bases_seq_14:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_14:value}}`** (Restores original state!).

**Load Baseline State:** In `{{key:HEX}}` mode, key `17 {{key:ENTER}}` to place initial GPIO state `17h` on the stack $(T: 0\text{h}, Z: 0\text{h}, Y: 17\text{h}, X: 17\text{h})$. **Clear Bit 2:** Key `4 {{key:-}}` to subtract bit weight $2^2 = 4\text{h}$, driving the heartbeat pin low to $\mathbf{\text{13h}}$ in Register $X$. **Re-Set Bit 2:** Key `4 {{key:+}}` to add bit weight $2^2 = 4\text{h}$, driving the pin high and restoring the original configuration $\mathbf{\text{17h}}$ in Register $X$ with exact arithmetic repeatability.

---

> **Thematic Arc II — Peripheral Register Bitfields, Masks & Shift Idioms (Problems 10.11–10.20):** Using bitwise `AND`, `OR`, `XOR`, and `NOT` on the 36-bit integer stack to pack and unpack microcontroller control registers.

### Problem 10.11: Multi-Bit Field Extraction (ADC Resolution Field)
A microcontroller ADC configuration register holds `0x3C6A`. Bits [7:4] define the ADC resolution code ($0 \dots 15$, where `0x6` selects 12-bit conversion mode). Extract this 4-bit field into an isolated integer in Register $X$ using `{{key:÷R}}` and `{{key:÷}}`.

| Extraction Stage | Binary Nibbles (Bits 15–0) | Hexadecimal Value |
| :--- | :---: | :---: |
| **ADC Configuration Register** | `0011 1100 0110 1010` | `3C6Ah` |
| **Lower Byte Remainder (`÷R 100h`)** | `0000 0000 0110 1010` | `006Ah` |
| **Right-Shifted Nibble (`÷ 10h`)** | `0000 0000 0000 0110` | `0006h` ($6_{10}$) |

**Keystrokes in `{{key:HEX}}` Mode:**
1. Isolate lower byte via modulo `0x100`: `{{res:sc32_10_computer_science_bases_seq_15:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_15:value}}`
2. Shift right by 4 bits ($2^4 = 16 = \text{10h}$): `{{res:sc32_10_computer_science_bases_seq_16:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_16:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `3C6A {{key:ENTER}}` | `0h` | `0h` | `3C6Ah` | `3C6Ah` | `3C6Ah` |
| 02 | `100 {{key:÷R}}` | `0h` | `0h` | `6Ah` | `3Ch` | `3Ch` |
| 03 | `{{key:x⇄y}}` | `0h` | `0h` | `3Ch` | `6Ah` | `6Ah` |
| 04 | `10 {{key:÷}}` | `0h` | `0h` | `3Ch` | `6h` | `6h` |

---

### Problem 10.12: Multi-Bit Field Insertion (Read-Modify-Write)
In a peripheral timer control register currently holding `0x4521`, update the 4-bit prescaler field at bits [11:8] (currently `5h`) with value `0xA` ($10_{10}$), without altering any of the surrounding configuration bits.

| Insertion Stage | Binary Nibbles (Bits 15–0) | Hexadecimal Value |
| :--- | :---: | :---: |
| **Original Timer Register** | `0100 0101 0010 0001` | `4521h` |
| **Subtract Old Field (`- 500h`)** | `0100 0000 0010 0001` | `4021h` |
| **Shifted New Field (`A × 100h`)** | `0000 1010 0000 0000` | `0A00h` |
| **Updated Register (`+`)** | `0100 1010 0010 0001` | `4A21h` |

**Keystrokes in `{{key:HEX}}` Mode:**
1. Clear existing field: `{{res:sc32_10_computer_science_bases_seq_17:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_17:value}}`
2. Prepare shifted new field: `{{res:sc32_10_computer_science_bases_seq_18:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_18:value}}`
3. Merge fields: `{{key:+}}` $\rightarrow$ **`4A21h`**

**Clear Existing Field:** In `{{key:HEX}}` mode, key `4521 {{key:ENTER}} 500 {{key:-}}` to subtract the active field mask $\text{500h}$, zeroing bits [11:8] and holding $\text{4021h}$ in Register $X$ $(T: 0\text{h}, Z: 0\text{h}, Y: 0\text{h}, X: \text{4021h})$. **Align New Value:** Key `A {{key:ENTER}} 100 {{key:×}}` to lift $\text{4021h}$ into Register $Y$ and scale new prescaler code $\text{Ah}$ into position $\text{A00h}$ in Register $X$ $(T: 0\text{h}, Z: 0\text{h}, Y: \text{4021h}, X: \text{A00h})$. **Merge Updated Bitfield:** Press `{{key:+}}` to assemble the merged control word $\mathbf{\text{4A21h}}$ into Register $X$ in a single addition step.

---

### Problem 10.13: RGB888 to RGB565 16-Bit Color Packing
Convert 24-bit TrueColor `0xFF5733` ($R=255, G=87, B=51$) into 16-bit RGB565 format for high-speed transflective LCD frame buffers.

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

**Keystrokes in `{{key:HEX}}` Mode:**
1. Red channel bit-shift (`<< 11`): `{{res:sc32_10_computer_science_bases_seq_19:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_19:value}}` ($2^{11} = 800\text{h}$)
2. Green channel bit-shift (`<< 5`): `{{res:sc32_10_computer_science_bases_seq_20:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_20:value}}` ($2^5 = 20\text{h}$)
3. Combine Red & Green: `{{key:+}}` $\rightarrow$ `FAA0h`
4. Combine Blue: `{{res:sc32_10_computer_science_bases_seq_21:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_21:value}}`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `1F {{key:ENTER}}` | `0h` | `0h` | `1Fh` | `1Fh` | `1Fh` |
| 02 | `800 {{key:×}}` | `0h` | `0h` | `0h` | `F800h` | `F800h` |
| 03 | `15 {{key:ENTER}}` | `0h` | `F800h` | `15h` | `15h` | `15h` |
| 04 | `20 {{key:×}}` | `0h` | `0h` | `F800h` | `2A0h` | `2A0h` |
| 05 | `{{key:+}}` | `0h` | `0h` | `0h` | `FAA0h` | `FAA0h` |
| 06 | `6 {{key:+}}` | `0h` | `0h` | `0h` | `FAA6h` | `FAA6h` |

---

### Problem 10.14: RGB565 to RGB888 Color Unpacking & Expansion
Given packed RGB565 word `0xE5B2`, extract individual color channels using `{{key:÷}}` and `{{key:÷R}}` and expand them to standard 8-bit values ($0 \dots 255$):
* Red channel (bits 15–11): divide by $2^{11} = \text{800h}$
* Green channel (bits 10–5): take remainder modulo $\text{800h}$ via `{{key:÷R}} {{key:x⇄y}}`, then divide by $2^5 = \text{20h}$
* Blue channel (bits 4–0): take remainder modulo $\text{20h}$ via `{{key:÷R}} {{key:x⇄y}}`

**Keystrokes in `{{key:HEX}}` & `{{key:DEC}}` Modes:**
1. Extract Red: `{{res:sc32_10_computer_science_bases_seq_22:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_22:value}}`** ($28_{10}$)
   * Expand in `{{key:DEC}}`: `{{res:sc32_10_computer_science_bases_seq_23:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_23:value}}`**
2. Extract Green: `{{res:sc32_10_computer_science_bases_seq_24:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_24:value}}`** ($45_{10}$)
   * Expand in `{{key:DEC}}`: `{{res:sc32_10_computer_science_bases_seq_25:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_25:value}}`**
3. Extract Blue: `{{res:sc32_10_computer_science_bases_seq_26:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_26:value}}`** ($18_{10}$)
   * Expand in `{{key:DEC}}`: `{{res:sc32_10_computer_science_bases_seq_27:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_27:value}}`**
* Unpacked TrueColor: **`RGB(230, 182, 148)`** (`#E6B694`).

**Extract Red Channel:** In `{{key:HEX}}` mode, key `E5B2 {{key:ENTER}} 800 {{key:÷}}` to shift right by 11 bits ($2^{11} = \text{800h}$), extracting 5-bit Red code $\mathbf{\text{1Ch}}$ ($28_{10}$) in Register $X$. In `{{key:DEC}}`, expand via `255 {{key:×}} 31 {{key:÷}}` to establish $R = \mathbf{230}$. **Extract Green Channel:** In `{{key:HEX}}` mode, key `E5B2 {{key:ENTER}} 800 {{key:÷R}} {{key:x⇄y}} 20 {{key:÷}}` to isolate the remainder modulo $\text{800h}$ and right-shift by 5 bits ($2^5 = \text{20h}$), yielding 6-bit Green code $\mathbf{\text{2Dh}}$ ($45_{10}$) in Register $X$. In `{{key:DEC}}`, expand via `255 {{key:×}} 63 {{key:÷}}` to obtain $G = \mathbf{182}$. **Extract Blue Channel:** In `{{key:HEX}}` mode, key `E5B2 {{key:ENTER}} 20 {{key:÷R}} {{key:x⇄y}}` to isolate the remainder modulo $\text{20h}$, revealing 5-bit Blue code $\mathbf{\text{12h}}$ ($18_{10}$) in Register $X$. In `{{key:DEC}}`, expand via `255 {{key:×}} 31 {{key:÷}}` to complete TrueColor reconstruction **`RGB(230, 182, 148)`** (`#E6B694`).

---

### Problem 10.15: RGBA4444 16-Bit Texture Color Packing
In embedded OpenGL ES graphics engines, 16-bit RGBA4444 allocates 4 bits per channel:
Pack channels $R=14$ (`Eh`), $G=9$ (`9h`), $B=3$ (`3h`), $A=15$ (`Fh`):
$$(R \times \text{1000h}) + (G \times \text{100h}) + (B \times \text{10h}) + A$$

**Keystrokes in `{{key:HEX}}` Mode:** `{{res:sc32_10_computer_science_bases_seq_28:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_28:value}}`**

> ***The Horner Polynomial Stream & Bitfield Packing*** — Stream 4-bit nibbles $R, G, B, A$ by progressive shifting with base-16 multipliers directly in the operational stack {{cite:knuth1997,hp15c1982}}.

**Position Red Nibble:** In `{{key:HEX}}` mode, key `E {{key:ENTER}} 1000 {{key:×}}` to shift Red ($\text{Eh} = 14$) left by 12 bits, producing $\text{E000h}$ in Register $X$ $(T: 0\text{h}, Z: 0\text{h}, Y: 0\text{h}, X: \text{E000h})$. **Accumulate Green and Blue Nibbles:** Key `9 {{key:ENTER}} 100 {{key:×}} {{key:+}}` to pack Green ($\text{9h}$) at bits [11:8] ($\text{E900h}$), then key `3 {{key:ENTER}} 10 {{key:×}} {{key:+}}` to pack Blue ($\text{3h}$) at bits [7:4], reaching $\text{E930h}$ in Register $X$. **Merge Alpha Nibble:** Key `F {{key:+}}` to insert 4-bit Alpha ($\text{Fh} = 15$) into bits [3:0], completing 16-bit packed RGBA4444 texture word $\mathbf{\text{E93Fh}}$ in Register $X$.

---

### Problem 10.16: Base64 Binary Chunking
Convert 3 bytes of raw binary data `0x4D`, `0x61`, `0x6E` (ASCII string "Man") into four 6-bit Base64 index values:
* Assembled 24-bit word: `4D616Eh` ($010011010110000101101110_2$).
* The four 6-bit slice divisors are $2^{18} = \text{40000h}$, $2^{12} = \text{1000h}$, and $2^6 = \text{40h}$.

| Base64 Sextet | 6-Bit Binary Slice | Decimal Index | Base64 Character |
| :--- | :---: | :---: | :---: |
| **Sextet 1 (Bits 23–18)** | `010011` | `19` (`13h`) | **`T`** |
| **Sextet 2 (Bits 17–12)** | `010110` | `22` (`16h`) | **`W`** |
| **Sextet 3 (Bits 11–6)** | `000101` | `5` (`05h`) | **`F`** |
| **Sextet 4 (Bits 5–0)** | `101110` | `46` (`2Eh`) | **`u`** |

**Keystrokes in `{{key:HEX}}` Mode:**
1. Sextet 1: `{{res:sc32_10_computer_science_bases_seq_29:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_29:value}}`** ($19_{10} \implies \mathbf{T}$)
2. Sextet 2: `{{res:sc32_10_computer_science_bases_seq_30:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_30:value}}`** ($22_{10} \implies \mathbf{W}$)
3. Sextet 3: `{{res:sc32_10_computer_science_bases_seq_31:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_31:value}}`** ($5_{10} \implies \mathbf{F}$)
4. Sextet 4: `{{res:sc32_10_computer_science_bases_seq_32:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_32:value}}`** ($46_{10} \implies \mathbf{u}$) — confirming "Man" encodes to **`TWFu`**.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `4D616E {{key:ENTER}} 40000 {{key:÷}}` | `0h` | `0h` | `0h` | **`13h`** | Sextet 1: `4D616Eh >> 18 = 13h` ($19_{10} \implies \mathbf{T}$) |
| 02 | `4D616E {{key:ENTER}} 40000 {{key:÷R}} {{key:x⇄y}} 1000 {{key:÷}}` | `13h` | `13h` | `13h` | **`16h`** | Sextet 2: remainder `>> 12 = 16h` ($22_{10} \implies \mathbf{W}$) |
| 03 | `4D616E {{key:ENTER}} 1000 {{key:÷R}} {{key:x⇄y}} 40 {{key:÷}}` | `16h` | `16h` | `4D6h` | **`5h`** | Sextet 3: remainder `>> 6 = 5h` ($5_{10} \implies \mathbf{F}$) |
| 04 | `4D616E {{key:ENTER}} 40 {{key:÷R}} {{key:x⇄y}}` | `4D6h` | `5h` | `13585h` | **`2Eh`** | Sextet 4: lower 6-bit remainder = `2Eh` ($46_{10} \implies \mathbf{u}$) |

---

### Problem 10.17: Two's Complement Negation Proof ($(2^{36} - 1 - X) + 1$)
Verify that subtracting $X$ from all ones (`FFFFFFFFFh`, 9 hex digits for 36 bits) and adding $1$ produces the exact mathematical two's complement negation `{{key:+/-}}`:
* Key in $42$ in `{{key:DEC}}` mode and press `{{key:+/-}}`: produces **`-42`**.
* Switch to `{{key:BASE}} {{key:HEX}}`: displays as `FFFFFFFD6h` ($36$-bit two's complement representation, $2^{36} - 42$).
* Verify by one's complement subtraction: `FFFFFFFFF {{key:ENTER}} 2A {{key:-}} 1 {{key:+}}` $\rightarrow$ `FFFFFFFD6h` (`-42` in `{{key:DEC}}`).

**Direct Decimal Negation:** In `{{key:DEC}}` mode, key `42 {{key:+/-}}` to negate 42 directly to $\mathbf{-42}$ in Register $X$. **Inspect 36-Bit Two's Complement Hex:** Switch to `{{key:BASE}} {{key:HEX}}` to inspect the full 36-bit two's complement sign-extended representation $\mathbf{\text{FFFFFFFD6h}}$. **Mathematical Inversion & Increment Proof:** Key `FFFFFFFFF {{key:ENTER}} 2A {{key:-}}` to perform bitwise one's complement subtraction ($2^{36} - 1 - 42 = \text{FFFFFFFD5h}$), then key `1 {{key:+}}` to add 1, proving exact convergence to $\mathbf{\text{FFFFFFFD6h}}$ ($-42_{10}$).

---

### Problem 10.18: 36-Bit Two's Complement Boundary Audit
* Maximum 36-Bit Signed Positive:
  `7FFFFFFFFh` = $+34,359,738,367_{10}$
* Add 1: `{{res:sc32_10_computer_science_bases_seq_33:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_33:value}}` ($-34,359,738,368_{10}$, Minimum Negative Bound).

* Subtract 1 from 0: `{{res:sc32_10_computer_science_bases_seq_34:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_34:value}}` ($-1_{10}$).

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `7FFFFFFFF {{key:ENTER}}` | `0h` | `0h` | `7FFFFFFFFh` | `7FFFFFFFFh` | Load maximum signed positive 36-bit bound |
| 02 | `1 {{key:+}}` | `0h` | `0h` | `0h` | **`800000000h`** | Overflow rolls over to minimum negative bound |
| 03 | `0 {{key:ENTER}} 1 {{key:-}}` | `0h` | `0h` | `800000000h` | **`FFFFFFFFFh`** | Underflow to $-1_{10}$; all 36 bits set (`FFFFFFFFFh`) |

---

### Problem 10.19: Arithmetic Right Shift via Signed Integer Division
For signed negative integer $-64$:
* In `{{key:DEC}}`: `{{res:sc32_10_computer_science_bases_seq_35:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_35:value}}`** (Exact arithmetic right shift by 2 bits, sign-extended).

**Load Signed Dividend:** In `{{key:DEC}}` mode, key `64 {{key:+/-}} {{key:ENTER}}` to position $-64$ in Registers $Y$ and $X$. **Execute Arithmetic Right Shift:** Key `4 {{key:÷}}` to divide by $2^2 = 4$, performing an authentic arithmetic right shift by 2 bits with signed sign extension, yielding $\mathbf{-16}$ in Register $X$ $(T: 0, Z: 0, Y: 0, X: -16)$. **Verify Sign Extension in Hex:** Switch to `{{key:BASE}} {{key:HEX}}`. The display confirms 36-bit sign-extended two's complement form $\mathbf{\text{FFFFFFFFF0h}}$ without auxiliary storage.

---

### Problem 10.20: Division with Remainder via `{{key:÷R}}`
Compute $12345 \div 16$ with simultaneous quotient and remainder:
Keystrokes: `{{res:sc32_10_computer_science_bases_seq_01:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_01:value}}`**

> ***The x⇄y Denominator Flip & Euclidean Remainder Pipeline*** — Execute integer division with remainder via `{{key:÷R}}`, simultaneously producing the integer quotient in $X$ and exact remainder in $Y$ without register allocation {{cite:knuth1997,hp15c1982}}.

* Register $X$: **`771`** (Whole quotient $Q$)
* Register $Y$: **`9`** (Remainder $R$, identical to $12345 \bmod 16$).

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `12345 {{key:ENTER}}` | 0 | 0 | 12345 | 12345 | Load integer dividend $12,345$ |
| 02 | `16 {{key:÷R}}` | 0 | 0 | **9** | **771** | Quotient $Q=771$ in Register X, remainder $R=9$ in Register Y |
| 03 | `{{key:x⇄y}}` | 0 | 0 | 771 | **9** | Swap registers to access remainder $9$ directly |

---

> **Thematic Arc III — Error Detection, Two's-Complement Arithmetic & Checksums (Problems 10.21–10.30):** Auditing Hamming distances, sign-extension boundaries, and CRC/checksum accumulators.

### Problem 10.21: Telemetry Bit-Difference Inspection
Determine the differing bit positions between telemetry word `0x5F5A` and baseline `0x5A50`:
Keystrokes in `{{key:HEX}}`: `{{res:sc32_10_computer_science_bases_seq_36:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_36:value}}`** ($0000010100001010_2$ in `{{key:BIN}}`).

Bits 1, 3, 8, 10 are set, revealing a Hamming distance of **$4\text{ bits}$**.

**Load Telemetry Sample:** In `{{key:HEX}}` mode, key `5F5A {{key:ENTER}}` to position telemetry word `5F5Ah` in Registers $Y$ and $X$. **Isolate Bit Disparities via Subtraction:** Key `5A50 {{key:-}}` to subtract baseline `5A50h`, isolating differences into `50Ah` in Register $X$ $(T: 0\text{h}, Z: 0\text{h}, Y: 0\text{h}, X: \text{50Ah})$. **Inspect Discrepancies in Binary:** Press `{{key:BASE}} {{key:BIN}}` to view binary bitfield $\mathbf{10100001010\text{b}}$, confirming bits 1, 3, 8, 10 are flipped (Hamming distance $= 4\text{ bits}$).

---

### Problem 10.22: Parity Bit Generation
Data byte `0x3B` ($00111011_2$, five ones $\implies$ odd parity).
For even parity, the MSB parity bit (Bit 7, weight $2^7 = 128_{10} = \text{80h}$) must be set to $1$:
`{{res:sc32_10_computer_science_bases_seq_37:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_37:value}}`**.

**Load Data Byte:** In `{{key:HEX}}` mode, key `3B {{key:ENTER}}` to load byte `3Bh` ($00111011_2$, 5 ones) onto the stack. **Apply Parity Mask:** Key `80 {{key:+}}` to add MSB bit weight $2^7 = \text{80h}$, producing even-parity byte $\mathbf{\text{BBh}}$ ($10111011_2$) in Register $X$.

---

### Problem 10.23: Longitudinal Redundancy Check (LRC)
Calculate LRC across message bytes `0x02`, `0x41`, `0x42`:
`{{res:sc32_10_computer_science_bases_seq_38:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_38:value}}`.

LRC = $(256 - \text{Sum}) \bmod 256$: `{{res:sc32_10_computer_science_bases_seq_39:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_39:value}}`**.

**Accumulate Message Bytes:** In `{{key:HEX}}` mode, key `2 {{key:ENTER}} 41 {{key:+}} 42 {{key:+}}` to sum message bytes `02h`, `41h`, and `42h`, yielding unmasked sum $\text{85h}$ in Register $X$ $(T: 0\text{h}, Z: 0\text{h}, Y: 0\text{h}, X: \text{85h})$. **Compute Two's Complement Checksum:** Key `100 {{key:ENTER}} 85 {{key:-}}` to subtract the sum from $256_{10}$ (`100h`), establishing certified Longitudinal Redundancy Check byte $\mathbf{\text{7Bh}}$ in Register $X$.

---

### Problem 10.24: RFC 1071 Internet Checksum & One's Complement Fold via `{{key:÷R}}`
In IP, TCP, and UDP internet protocols, packet integrity is verified using the 16-bit one's complement sum of header words {{cite:knuth1997}}. When 16-bit header words are accumulated, the 32-bit running sum frequently generates overflow carries beyond bit 15. The RFC 1071 fold operation extracts the upper carry bits ($> \text{FFFFh}$) and adds them back into the lower 16 bits before inverting:

$$\text{Header Sum} = 2653\text{D}_{16}$$
$$\text{Carry} = \lfloor 2653\text{D}_{16} / 10000_{16} \rfloor = 2_{16}$$
$$\text{Lower 16 Bits} = 2653\text{D}_{16} \bmod 10000_{16} = 653\text{D}_{16}$$
$$\text{Folded Sum} = 653\text{D}_{16} + 2_{16} = 653\text{F}_{16}$$
$$\text{Checksum} = \text{FFFF}_{16} - 653\text{F}_{16} = \mathbf{9AC0}_{16} \ (39,616_{10})$$

**Keystrokes in `{{key:HEX}}` Mode:**
1. Load 32-bit accumulated header sum: `2653D {{key:ENTER}}` $\rightarrow$ `2653Dh`
2. Divide by $2^{16} = \text{10000h}$ via `{{key:÷R}}`: `10000 {{key:÷R}}` $\rightarrow$ Register $X$: `2h` (Carry), Register $Y$: `653Dh` (Lower 16 bits).
3. Fold carry into lower sum: `{{key:+}}` $\rightarrow$ `653Fh`
4. Compute one's complement: `FFFF {{key:x⇄y}} {{key:-}}` $\rightarrow$ **`9AC0h`** ($39,616_{10}$ in `{{key:DEC}}`).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `2653D {{key:ENTER}}` | `0h` | `0h` | `2653Dh` | `2653Dh` | `2653Dh` |
| 02 | `10000 {{key:÷R}}` | `0h` | `0h` | `653Dh` | `2h` | `2h` |
| 03 | `{{key:+}}` | `0h` | `0h` | `0h` | `653Fh` | `653Fh` |
| 04 | `FFFF` | `0h` | `0h` | `653Fh` | `FFFFh` | `FFFFh` |
| 05 | `{{key:x⇄y}}` | `0h` | `0h` | `FFFFh` | `653Fh` | `653Fh` |
| 06 | `{{key:-}}` | `0h` | `0h` | `0h` | `9AC0h` | `9AC0h` |

**Load Accumulated Header Sum:** In `{{key:HEX}}` mode, key `2653D {{key:ENTER}}` to position the un-folded 32-bit header sum `2653Dh` across Registers $Y$ and $X$. **Execute Single-Cycle 16-Bit Partitioning via `{{key:÷R}}`:** Key `10000 {{key:÷R}}` to divide by $2^{16} = \text{10000h}$. Register $X$ receives the upper carry bits ($Q = 2\text{h}$) while Register $Y$ receives the lower 16 bits ($R = 653\text{Dh}$) simultaneously. **Fold Carry in Place:** Press `{{key:+}}` to add the carry in $X$ directly to the lower half in $Y$, yielding folded sum $653\text{Fh}$ in Register $X$. **Evaluate One's Complement:** Key `FFFF {{key:x⇄y}} {{key:-}}` using the classic RPN inverted subtraction idiom to subtract the folded sum from all-ones mask $\text{FFFFh}$, producing certified IPv4 header checksum $\mathbf{\text{9AC0h}}$ ($39,616_{10}$ in `{{key:DEC}}`).

---

### Problem 10.25: Ethernet FCS 32-Bit Inversion & Frame Check Sequence Post-Conditioning
In IEEE 802.3 Ethernet frame transmission, the final 32-bit CRC remainder (Frame Check Sequence, FCS) is post-conditioned prior to transmission by inverting all 32 bits (one's complement). Given an Ethernet polynomial check state of `0xEDB88320`:
1. Invert the 32-bit word by subtracting from the all-ones mask `FFFFFFFFh`:
$$FFFFFFFF_{16} - EDB88320_{16} = \mathbf{12477CDF}_{16} \ (306,678,751_{10})$$

**Keystrokes in `{{key:HEX}}` Mode:**
1. Load 32-bit inversion mask: `FFFFFFFF {{key:ENTER}}` $\rightarrow$ `FFFFFFFFh`
2. Subtract Ethernet generator polynomial: `EDB88320 {{key:-}}` $\rightarrow$ **`12477CDFh`**
3. Switch radix to inspect in decimal: `{{key:BASE}} {{key:DEC}}` $\rightarrow$ **`306678751`**.

**Load 32-Bit Inversion Mask:** In `{{key:HEX}}` mode, key `FFFFFFFF {{key:ENTER}}` to position the 32-bit all-ones mask across Registers $Y$ and $X$. **Execute Inversion Subtraction:** Key `EDB88320 {{key:-}}` to subtract the polynomial word `EDB88320h`, producing the exact inverted FCS complement $\mathbf{\text{12477CDFh}}$ in Register $X$. **Inspect in Decimal:** Press `{{key:BASE}} {{key:DEC}}` to inspect the 32-bit check state as decimal integer $\mathbf{306,678,751}$ in Register $X$ with zero data loss across stack registers.

---

### Problem 10.26: UART Fractional Baud Rate Divisor at 150 MHz
A high-performance dual-core microcontroller runs its peripheral system clock at $f_{\text{clk}} = 150.0\text{ MHz}$ ($150,000,000\text{ Hz}$). The hardware UART baud rate generator features an integer baud rate register (`IBRD`, 16-bit) and a fractional baud rate register (`FBRD`, 6-bit with divisor $64$) over an $8\times$ oversampling receiver clock.
Determine `IBRD` and `FBRD` to configure a target baud rate of $115,200\text{ baud}$, and calculate the resulting baud rate error percentage.

$$\text{Baud Divider} = \frac{f_{\text{clk}}}{8 \times \text{Baud}} = \frac{150,000,000}{8 \times 115,200} = \frac{150,000,000}{921,600} \approx 162.760416667$$

**Keystrokes in `{{key:ALL}}` Mode:**
1. `{{res:sc32_10_computer_science_bases_seq_40:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_40:value}}`**
2. Integer divider `IBRD`: `{{key:ENTER}} {{key:PARTS}} {{key:IP}}` $\rightarrow$ **`162`** (`0xA2`)
3. Fractional divider `FBRD`: `{{key:x⇄y}} {{key:PARTS}} {{key:FP}} 64 {{key:×}} {{key:PARTS}} {{key:IP}}` $\rightarrow$ **`48`** (or rounded: **`49`** `0x31`)
4. Actual baud rate: $150,000,000 / (8 \times (162 + 49/64)) = 150,000,000 / 1302.125 = \mathbf{115,196.3\text{ baud}}$
5. Baud Error: $(115196.3 - 115200) / 115200 \times 100\% = \mathbf{-0.0032\%}$ (Near zero error!).

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

---

### Problem 10.27: SPI Clock Prescaler Selection
A SPI peripheral runs from a $75.0\text{ MHz}$ bus clock. The connected flash memory specifies a maximum operating frequency of $10.0\text{ MHz}$. The SPI prescaler offers powers of two: $2, 4, 8, 16, 32, 64, 128$.
Determine the optimal prescaler divider and actual SPI operating frequency.

**Keystrokes:** `{{res:sc32_10_computer_science_bases_seq_53:keys}}` $\rightarrow$ $7.5$.

**Compute Minimum Divider Ratio:** Running this sequence to divide the master peripheral clock ($75.0\text{ MHz}$) in Register $Y$ by the maximum flash clock ($10.0\text{ MHz}$) in Register $X$, consuming both operands and dropping the minimum required divider ratio $7.5000$ into Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 7.5000)$. **Select Power-of-Two Prescaler:** Because the hardware prescaler must be a power of two $\ge 7.5$, select **`8`** ($2^3$) via `8 {{key:ENTER}}`. **Verify Operational Clock:** Divide the master clock by the selected prescaler via `{{res:sc32_10_computer_science_bases_seq_54:keys}}` to evaluate the actual SPI bus clock frequency $f_{\text{SPI}} = \mathbf{{{res:sc32_10_computer_science_bases_seq_54:value}}\text{ Hz}}$ ($9.375\text{ MHz}$) in Register $X$.

---

### Problem 10.28: I2C Fast-Mode Plus SCL Timing Register Calculations
Target I2C clock frequency $f_{\text{SCL}} = 1.0\text{ MHz}$ ($1000\text{ ns}$ cycle time) derived from a $150.0\text{ MHz}$ core clock period ($T_{\text{clk}} = \frac{1}{150\times 10^6} \approx 6.6667\text{ ns}$).
Total clocks per SCL period: $150\text{ cycles}$.
In Fast-Mode Plus, asymmetric duty cycle allocates $t_{\text{LOW}} \ge 500\text{ ns}$ and $t_{\text{HIGH}} \ge 260\text{ ns}$.
Allocating $\frac{1}{3}$ high and $\frac{2}{3}$ low:
* $t_{\text{HIGH}} = 50\text{ cycles} \times 6.6667\text{ ns} = \mathbf{333.3\text{ ns}}$ ($> 260\text{ ns}$)
* $t_{\text{LOW}} = 100\text{ cycles} \times 6.6667\text{ ns} = \mathbf{666.7\text{ ns}}$ ($> 500\text{ ns}$).

**Keystrokes:**
1. Total cycles: `150 {{key:ENTER}} 1 {{key:÷}}` $\rightarrow$ $150$ cycles
2. High phase clocks: `3 {{key:÷}}` $\rightarrow$ $50$ cycles
3. Timing durations: `150 {{key:ENTER}} 6.6667 {{key:×}} 3 {{key:÷}}` $\rightarrow$ **`333.3 ns`** ($t_{\text{HIGH}}$); `2 {{key:×}}` $\rightarrow$ **`666.7 ns`** ($t_{\text{LOW}}$).

**Determine Core Clock Cycles per Period:** Key `150 {{key:ENTER}} 1 {{key:÷}}` to determine 150 total system clock cycles per $1.0\text{ MHz}$ SCL period at $150\text{ MHz}$. **Allocate Asymmetric Phases:** Divide by 3 via `3 {{key:÷}}` to allocate 50 clock cycles to the high phase ($t_{\text{HIGH}}$) and 100 cycles to the low phase ($t_{\text{LOW}}$). **Compute Real Nanosecond Durations:** Multiply by core clock period ($6.6667\text{ ns}$) to verify $t_{\text{HIGH}} = \mathbf{333.3\text{ ns}}$ ($> 260\text{ ns}$ specification) and $t_{\text{LOW}} = \mathbf{666.7\text{ ns}}$ ($> 500\text{ ns}$ specification), confirming full compliance with Fast-Mode Plus electrical constraints.

---

### Problem 10.29: 32-Bit Byte Swapping (Endianness Reversal)
Network sockets receive data in Big-Endian format, while ARM Cortex processors operate natively in Little-Endian. Convert Big-Endian integer `0x12345678` into Little-Endian `0x78563412` using `{{key:÷R}}`, `{{key:÷}}`, `{{key:×}}`, and `{{key:+}}`.

| Byte Order | Byte 3 (MSB) | Byte 2 | Byte 1 | Byte 0 (LSB) |
| :--- | :---: | :---: | :---: | :---: |
| **Big-Endian (`12345678h`)** | `12h` | `34h` | `56h` | `78h` |
| **Shift Operation** | `>> 24` (`÷ 1000000h`) | `>> 8` (`÷ 100h`) | `<< 8` (`× 100h`) | `<< 24` (`× 1000000h`) |
| **Little-Endian (`78563412h`)** | `78h` | `56h` | `34h` | `12h` |

**Keystrokes in `{{key:HEX}}` Mode:**
1. Extract Byte 0 and shift to Byte 3: `{{res:sc32_10_computer_science_bases_seq_41:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_41:value}}`
2. Extract Byte 1 and shift to Byte 2: `{{res:sc32_10_computer_science_bases_seq_42:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_42:value}}`
3. Extract Byte 2 and shift to Byte 1: `{{res:sc32_10_computer_science_bases_seq_43:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_43:value}}`
4. Extract Byte 3 and shift to Byte 0: `{{res:sc32_10_computer_science_bases_seq_44:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_44:value}}`
5. Merge all 4 non-overlapping bytes via `{{key:+}}`: `{{key:+}} {{key:+}} {{key:+}}` $\rightarrow$ **`78563412h`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `78 {{key:ENTER}} 1000000 {{key:×}}` | `0h` | `0h` | `0h` | `78000000h` | `78000000h` |
| 02 | `56 {{key:ENTER}} 10000 {{key:×}}` | `0h` | `0h` | `78000000h` | `560000h` | `560000h` |
| 03 | `{{key:+}}` | `0h` | `0h` | `0h` | `78560000h` | `78560000h` |
| 04 | `34 {{key:ENTER}} 100 {{key:×}}` | `0h` | `0h` | `78560000h` | `3400h` | `3400h` |
| 05 | `{{key:+}}` | `0h` | `0h` | `0h` | `78563400h` | `78563400h` |
| 06 | `12` | `0h` | `0h` | `78563400h` | `12h` | `12h` |
| 07 | `{{key:+}}` | `0h` | `0h` | `0h` | `78563412h` | `78563412h` |

---

### Problem 10.30: IEEE-754 32-Bit Single Precision Float Unpacking
Decompose the IEEE-754 single-precision float value $-6.25$ into Sign, Biased Exponent, and Fractional Mantissa:
1. Absolute value: $6.25_{10} = 4 + 2 + 0.25 = 110.01_2 = 1.1001_2 \times 2^2$.
2. Sign Bit: Negative $\implies S = \mathbf{1}$.
3. Biased Exponent: $E = \text{exponent} + 127 = 2 + 127 = 129_{10} = 10000001_2 = \mathbf{81h}$.
4. Fractional Mantissa: $M = 10010000000000000000000_2 = \mathbf{480000h}$.
5. 32-Bit Binary Hex Word: `1 10000001 10010000000000000000000` = **`0xC0C80000`**.

**Keystrokes in `{{key:HEX}}` Mode:** `C0C80000 {{key:ENTER}} 800000 {{key:÷R}} 100 {{key:÷R}}` $\rightarrow$ Quotient: `1h` (Sign $S=1$), Remainder: `81h` (Biased Exponent $E=129_{10}$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `C0C80000 {{key:ENTER}}` | `0h` | `0h` | `C0C80000h` | `C0C80000h` | `C0C80000h` |
| 02 | `800000 {{key:÷R}}` | `0h` | `0h` | `480000h` | `181h` | `181h` |
| 03 | `100 {{key:÷R}}` | `0h` | `480000h` | `81h` | `1h` | `1h` |
| 04 | `{{key:BASE}} {{key:DEC}}` | 0 | 4718592 | 129 | 1 | `1` |
| 05 | `{{key:x⇄y}} 127 {{key:-}}` | 4718592 | 4718592 | 1 | 2 | `2` |

**Unpacked Fields:**
**Sign Bit ($S$):** $1$ (Negative)
**Biased Exponent ($E$):** `81h` ($129_{10} \implies e = 129 - 127 = \mathbf{2}$)
**Fractional Mantissa ($M$):** `480000h` ($\frac{4,718,592}{2^{23}} = 0.5625 = \frac{9}{16}$)
**Reconstructed Value:** $(-1)^1 \times 2^2 \times (1 + 0.5625) = -4 \times 1.5625 = \mathbf{-6.25}$.

---

> **Thematic Arc IV — Floating-Point Encodings, Cryptography & Memory Architecture (Problems 10.31–10.40):** The final ten problems dissect IEEE-754 exponent biases, Base64 bitstreams, and cache-line address alignments.

### Problem 10.31: IEEE-754 64-Bit Double Precision Float Unpacking
Decompose the double-precision float value $-13.375$:
1. $13.375_{10} = 8 + 4 + 1 + 0.25 + 0.125 = 1101.011_2 = 1.101011_2 \times 2^3$.
2. Sign $S = 1$.
3. Biased Exponent: $3 + 1023 = 1026_{10} = 10000000010_2 = \mathbf{402h}$.
4. Fractional Mantissa (52 bits): $101011000000\dots0_2$.
5. Assembled Hex Word: **`0xC02AC00000000000`** (High 32-bit Word: `0xC02AC000`).

**Keystrokes in `{{key:HEX}}` Mode:** `C02AC000 {{key:ENTER}} 100000 {{key:÷R}} 800 {{key:÷R}}` $\rightarrow$ Quotient: `1h` (Sign $S=1$), Remainder: `402h` (Biased Exponent $E=1026_{10}$).

**Load High 32-Bit Word:** In `{{key:HEX}}` mode, key `C02AC000 {{key:ENTER}}` to position upper double-precision word `C02AC000h` in Registers $Y$ and $X$. **Separate Fractional Mantissa from Exponent:** Key `100000 {{key:÷R}}` to divide by $2^{20} = \text{100000h}$, leaving upper mantissa bits $\text{AC000h}$ in Register $Y$ and biased exponent with sign bit ($\text{C02h}$) in Register $X$. **Isolate Sign and Biased Exponent:** Key `800 {{key:÷R}}` to divide by $2^{11} = \text{800h}$, isolating Sign bit $S = \mathbf{1}$ in Register $X$ and Biased Exponent $E = \mathbf{\text{402h}}$ ($1026_{10}$) in Register $Y$. In `{{key:DEC}}`, subtracting bias ($1026 - 1023$) recovers true power $e = \mathbf{3}$.

**Unpacked Fields:**
**Sign Bit ($S$):** $1$ (Negative)
**Biased Exponent ($E$):** `402h` ($1026_{10} \implies e = 1026 - 1023 = \mathbf{3}$)
**Fractional Mantissa Upper ($M_{\text{high}}$):** `AC000h` ($\frac{704,512}{2^{20}} = 0.671875 = \frac{43}{64}$)
**Reconstructed Value:** $(-1)^1 \times 2^3 \times (1 + 0.671875) = -8 \times 1.671875 = \mathbf{-13.375}$.

---

### Problem 10.32: Fixed-Point Q16.16 Arithmetic Multiplication
In digital signal processing without FPU acceleration, numbers are formatted as signed Q16.16 (16 integer bits, 16 fractional bits, scaling factor $2^{16} = 65,536$).
Multiply $A = 3.5$ and $B = 2.25$:
* $A = 3.5 \times 65536 = 229,376 = \text{38000h}$
* $B = 2.25 \times 65536 = 147,456 = \text{24000h}$
* Product formula: $C = (A \times B) \gg 16 = (A \times B) / 65536$.

**Keystrokes in `{{key:HEX}}` Mode:** `{{res:sc32_10_computer_science_bases_seq_45:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_45:value}}`**

> ***The Constant-in-T Pipeline & Q16.16 Scaling*** — Multiply fixed-point integer words, then divide by radix scaling factor $2^{16} = 65,536$ in place in a single dyadic cycle {{cite:knuth1997,hp15c1982}}.

**Load Q16.16 Multiplicand:** In `{{key:HEX}}` mode, key `38000 {{key:ENTER}}` to place $A = 3.5 \times 65536 = \text{38000h}$ on the stack. **Compute Fixed-Point Product:** Key `24000 {{key:×}}` to multiply by $B = 2.25 \times 65536 = \text{24000h}$, producing raw 32-bit product $\text{7E0000000h}$ in Register $X$. **Rescale via Fixed-Point Divisor:** Key `10000 {{key:÷}}` to divide by radix scale factor $2^{16} = \text{10000h}$, yielding certified Q16.16 product $\mathbf{\text{7E000h}}$ ($516,096_{10}$). Dividing by $65,536$ in `{{key:DEC}}` mode verifies exact analytical product $\mathbf{{{res:sc32_10_computer_science_bases_seq_46:value}}}$.

---

### Problem 10.33: Permutations ($nPr$) in Cryptography S-Box Design
Calculate the total number of ways to construct an ordered 4-element substitution key from a pool of 16 distinct nibbles:
$$P(16, 4) = \frac{16!}{(16 - 4)!} = 16 \times 15 \times 14 \times 13 = \mathbf{43,680}$$

**Keystrokes:** `{{res:sc32_10_computer_science_bases_seq_47:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_47:value}}`**

> ***The LASTX Dual-Branch Trick & Combinatorial Pipeline*** — Evaluate permutations $P(n, r) = n! / (n-r)!$ via `{{key:PROB}} {{key:Pn,r}}` with zero factorial overflow {{cite:knuth1997,hp15c1982}}.

**Arm Total Pool Elements:** Key `16 {{key:ENTER}}` to position pool size $n = 16$ in Registers $Y$ and $X$. **Evaluate Permutations:** Key `4 {{key:PROB}} {{key:Pn,r}}` to specify subset size $r = 4$ and execute $P(16, 4)$ in place, obtaining total ordered substitution keys $P(16, 4) = \mathbf{{{res:sc32_10_computer_science_bases_seq_47:value}}}$ ($43,680$) in Register $X$ without factorial overflow.

---

### Problem 10.34: Combinations ($nCr$) and Hamming Sphere
In a $[7, 4]$ Hamming code, calculate the number of possible 2-bit error patterns:
$$\binom{7}{2} = \frac{7!}{2! \times 5!} = \mathbf{21}$$

**Keystrokes:** `{{res:sc32_10_computer_science_bases_seq_48:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_48:value}}`**

> ***The Binomial Coefficient Pipeline*** — Evaluate combinations $\binom{n}{r} = \frac{n!}{r!(n-r)!}$ directly in the operational stack via `{{key:PROB}} {{key:Cn,r}}` without scratch registers {{cite:knuth1997,hp15c1982}}.

**Load Codeword Length:** Key `7 {{key:ENTER}}` to position Hamming codeword length $n = 7$ in Registers $Y$ and $X$. **Evaluate Combinations:** Key `2 {{key:PROB}} {{key:Cn,r}}` to evaluate combinations $\binom{7}{2}$ directly on the active stack, obtaining total 2-bit error patterns $\binom{7}{2} = \mathbf{{{res:sc32_10_computer_science_bases_seq_48:value}}}$ ($21$) in Register $X$.

---

### Problem 10.35: Factorials and Stirling's Approximation Comparison
Calculate $15!$:
Exact: `{{res:sc32_10_computer_science_bases_seq_49:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_49:value}}`**.

Stirling's approximation: $\sqrt{2\pi n} (n/e)^n \approx 1.3004 \times 10^{12}$ (Error $< 0.6\%$).

**Load Factorial Argument:** Key `15` to place operand $n = 15$ into Register $X$. **Execute Full-Precision Factorial:** Press `{{key:PROB}} {{key:x!}}` to evaluate $15!$ in place, yielding exact 64-bit integer product $\mathbf{{{res:sc32_10_computer_science_bases_seq_49:value}}}$ ($1,307,674,368,000$) in Register $X$.

---

### Problem 10.36: Pseudo-Random Number Generation (`RAND`)
Generate 3 uniform random floats:
`{{key:PROB}} {{key:RAND}}` $\rightarrow$ $0.724194$
`{{key:PROB}} {{key:RAND}}` $\rightarrow$ $0.183022$
`{{key:PROB}} {{key:RAND}}` $\rightarrow$ $0.941581$.

**Clock Initial PRNG Draw ($U_1$):** Press `{{key:PROB}} {{key:RAND}}` to invoke the internal linear congruential uniform pseudo-random number generator, returning $U_1 = \mathbf{0.724194} \in [0, 1)$ into Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.724194)$. **Clock Subsequent Draw ($U_2$):** Press `{{key:PROB}} {{key:RAND}}` again. The previous draw automatically lifts into Register $Y$ while Register $X$ receives $U_2 = \mathbf{0.183022}$ $(T: 0.0000, Z: 0.0000, Y: 0.724194, X: 0.183022)$. **Preserve Stochastic History ($U_3$):** Striking `{{key:PROB}} {{key:RAND}}` a third time lifts the history upward, placing $U_1$ in $Z$, $U_2$ in $Y$, and new draw $U_3 = \mathbf{0.941581}$ in $X$ $(T: 0.0000, Z: 0.724194, Y: 0.183022, X: 0.941581)$.

---

### Problem 10.37: Pseudo-Random Die Roll Simulation
Simulate a standard 6-sided die roll:
`{{key:PROB}} {{key:RAND}} 6 {{key:×}} 1 {{key:+}} {{key:PARTS}} {{key:IP}}` $\rightarrow$ Integer in $1 \dots 6$.

**Sample Continuous Uniform Float:** Press `{{key:PROB}} {{key:RAND}}` to draw $U \in [0, 1)$ (e.g. $0.724194$) into Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 0.724194)$. **Scale by Range Width:** Key `6 {{key:×}}` to stretch the continuous interval from $[0, 1)$ to $[0, 6)$, yielding $4.345164$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 4.345164)$. **Apply Base Offset:** Key `1 {{key:+}}` to shift the interval to $[1, 7)$, giving $5.345164$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 5.345164)$. **Extract Discrete Face Value:** Press `{{key:PARTS}} {{key:IP}}` to truncate the fractional part via the integer-part function, leaving discrete die roll outcome $\mathbf{5} \in \{1, 2, 3, 4, 5, 6\}$ in Register $X$ $(T: 0.0000, Z: 0.0000, Y: 0.0000, X: 5.0000)$.

---

### Problem 10.38: Circular Left Rotation (ROL 1) on an 8-Bit Byte via `{{key:÷R}}`
Rotate `0x85` ($10000101_2$) left by 1 bit $\implies 00001011_2 = \text{0Bh}$.
1. Shift left by 1 bit: `{{res:sc32_10_computer_science_bases_seq_50:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_50:value}}`.
2. Split 8-bit remainder (`0Ah` in $Y$) and overflow carry (`1h` in $X$) via `{{key:÷R}}`: `{{res:sc32_10_computer_science_bases_seq_51:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_51:value}}`.
3. Add carry into LSB: `{{res:sc32_10_computer_science_bases_seq_52:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_52:value}}`**.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `85 {{key:ENTER}} 2 {{key:×}}` | `0h` | `0h` | `0h` | **`10Ah`** | Shift byte left by 1 bit ($85\text{h} \times 2 = 10\text{Ah}$) |
| 02 | `100 {{key:÷R}}` | `0h` | `0h` | `Ah` | **`1h`** | Extract carry bit ($X=1\text{h}$) and rotated byte ($Y=\text{Ah}$) |
| 03 | `{{key:+}}` | `0h` | `0h` | `0h` | **`Bh`** | Add carry bit into LSB: $10\text{Ah} \bmod 100\text{h} + 1\text{h} = \text{Ah} + 1\text{h} = \text{Bh}$ |

---

### Problem 10.39: Decimal to Binary Conversion & Bit Inspection
Convert decimal `13` into its 4-bit binary representation and verify its bit weights ($8 + 4 + 0 + 1$):
Keystrokes: `{{res:sc32_10_computer_science_bases_seq_02:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_02:value}}`** ($1101_2$).

***The Horner Polynomial Stream & Radix Inspection*** — Key decimal integer in `{{key:DEC}}` mode, switch to `{{key:BIN}}`, and inspect bitfields directly across display segments with zero conversion error {{cite:shannon1938,hp15c1982}}.

**Load Decimal Operand:** In `{{key:DEC}}` mode, key `13 {{key:ENTER}}` to position decimal 13 across Registers $Y$ and $X$. **Inspect Binary Radix Representation:** Press `{{key:BASE}} {{key:BIN}}`. The display immediately reflects exact 4-bit binary representation $\mathbf{{{res:sc32_10_computer_science_bases_seq_02:value}}}$ ($1101_2$), verifying bit weights $8 + 4 + 0 + 1$ directly on the transflective LCD with zero parentheses. Reverting via `{{key:BASE}} {{key:DEC}}` confirms all four stack registers remain unmodified.

---

### Problem 10.40: Binary to Hexadecimal & Decimal Reconstruction
Convert binary `1101b` back to decimal (`13`) and hexadecimal (`Dh`) via `{{key:BASE}} {{key:DEC}}` and `{{key:BASE}} {{key:HEX}}`, confirming lossless radix conversion across all stack registers.

**Enter Binary Bit Pattern:** In `{{key:BIN}}` mode, key `1101 {{key:ENTER}}` to place the 4-bit nibble $1101_2$ in Registers $Y$ and $X$ $(T: 0\text{b}, Z: 0\text{b}, Y: 1101\text{b}, X: 1101\text{b})$. **Lossless Radix Conversion to Hexadecimal:** Press `{{key:BASE}} {{key:HEX}}`. The internal 36-bit integer representation is preserved with full fidelity while the display formats the nibble as hexadecimal $(T: 0\text{h}, Z: 0\text{h}, Y: \text{Dh}, X: \mathbf{Dh})$, verifying $1101_2 = 13_{10} = \text{D}_{16}$. **Lossless Radix Conversion to Decimal:** Press `{{key:BASE}} {{key:DEC}}`. The display immediately reflects standard base-10 positional notation $(T: 0, Z: 0, Y: 13, X: \mathbf{13})$, proving that all four operational stack levels survive multi-base transitions intact without roundoff or register corruption.

---

## Summary & Looking Ahead

Chapter 10 demystified the low-level binary foundation of digital computation. Operating across an authentic 36-bit two's complement integer architecture, you navigated Hexadecimal, Decimal, Octal, and Binary modes while preserving multi-level stack register values intact. Without dedicated Boolean keys, you harnessed modular integer division via `{{key:÷R}}`—returning quotient in $X$ and remainder in $Y$—alongside word length clipping, modular reduction, and powers-of-two arithmetic to configure microcontroller registers, construct IPv4 CIDR subnet masks, pack and extract RGB color channels, and analyze telemetry bit disparities. Finally, you unified discrete combinatorics ($nPr$, $nCr$, $n!$) and pseudorandom seeding into an essential mathematical toolkit for systems programming and digital electronics.

From discrete bits and memory registers, the principles of accumulation and mathematical modeling extend directly into financial decision-making and quantitative economics. In **Chapter 11: Financial Mathematics & Time Value of Money (TVM)**, you will master the SC-32's dedicated five-variable compound interest solver ($N, I\%YR, PV, PMT, FV$). You will calculate mortgage amortization schedules, evaluate net present value (NPV) and internal rate of return (IRR), and apply actuarial sign discipline to model complex real-world capital flows.

