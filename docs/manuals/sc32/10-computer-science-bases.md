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
| **Decimal** | `{{keycap:BASE}} {{key:DEC}}` | *(none)* | `0` through `9` | `1042` |
| **Hexadecimal** | `{{keycap:BASE}} {{key:HEX}}` | `h` | `0` through `9`, `A` through `F` | `412h` |
| **Octal** | `{{keycap:BASE}} {{key:OCT}}` | `o` | `0` through `7` | `2022o` |
| **Binary** | `{{keycap:BASE}} {{key:BIN}}` | `b` | `0` and `1` | `10000010010b` |

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
  <li>Switch to Hex: <code>{{keycap:BASE}} {{key:HEX}}</code> &rarr; Key <code>3 {{key:√x}} 7 {{key:ENTER}}</code> ($3\text{A}7_{16} = 935_{10}$).</li>
  <li>Switch to Octal: <code>{{keycap:BASE}} {{key:OCT}}</code> &rarr; Key <code>452 {{key:+}}</code>. Register $X$ instantly sums them in octal: $2261_8$.</li>
  <li>Switch to Decimal: <code>{{keycap:BASE}} {{key:DEC}}</code> &rarr; Register $X$ immediately reads <strong>$1,201_{10}$</strong> with zero intermediate scratchpad steps!</li>
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

## Engineering Design Briefing: Bare-Metal Embedded Firmware & High-Performance Network Switching (Problems 10.1 through 10.40)

<div class="admonition warning">
<p class="admonition-title">Inside-Out Stack Architecture: Algebraic Trap vs. RPN Shortcut — 36-Bit Integer Registers &amp; Subnet Boundary Partitioning via {{key:÷R}}</p>
<p><strong>The Algebraic Parenthesis Trap:</strong> In network engineering and embedded firmware development, calculating IPv4 CIDR subnet IDs or decomposing packed hardware telemetry words on standard scientific calculators is fraught with difficulty. Algebraic scientific calculators lack native quotient-remainder separation, forcing developers to alternate between floating-point division, manual integer truncation, and re-multiplication to isolate remainder bits {{cite:shannon1938}}.</p>
<p><strong>The RPN Stack Shortcut:</strong> The SC-32 provides native 36-bit two's complement integer architecture with instantaneous base conversions (<code>{{key:HEX}}</code>, <code>{{key:DEC}}</code>, <code>{{key:OCT}}</code>, <code>{{key:BIN}}</code>) across all four stack registers {{cite:ieee754_2019}}. Dividing a binary word by a power of two ($2^k$) using simultaneous division with remainder (<code>{{key:÷R}}</code>) automatically isolates the upper network prefix bits in Register $X$ while depositing the lower host field remainder directly into Register $Y$ in a single instruction cycle, completely eliminating manual bitmask scratchwork.</p>
</div>

The following 40 reference problems provide complete, publication-grade coverage across network engineering, microcontroller firmware, computer graphics, cryptography, and discrete mathematics.

---

### Problem 10.1: Subnet Masking via Modular Division & Integer Bit-Packing
A network router receives an IPv4 packet destined for host octet `205`. The interface subnet mask octet is `240` (`/28` subnet). Determine the network subnet ID octet using modular remainder division ({{key:÷R}}).

$$205_{10} = 11001101_2$$
$$240_{10} = 11110000_2$$
$$205 \text{ AND } 240 = 11000000_2 = 192_{10}$$

#### Keystrokes in `{{key:DEC}}` Mode:
`{{res:sc32_10_computer_science_bases_seq_03:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_03:value}}`**

#### Stack Trace Table:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `205` | 0 | 0 | 0 | 205 | `205_` |
| 02 | `{{key:ENTER}}` | 0 | 0 | 205 | 205 | `205` |
| 03 | `16 {{key:÷R}}` | 0 | 0 | 13 | 12 | `12` |
| 04 | `16 {{key:×}}` | 0 | 0 | 0 | 192 | `192` |

---

### Problem 10.2: IPv4 CIDR /24 Subnet Network, Broadcast & Host Allocation
Given an IPv4 host address `192.168.10.45` with a `/24` subnet mask ($255.255.255.0$):
* In Hex: IP is `C0A80A2Dh`, Mask is `FFFFFF00h`, and block size is $2^{32-24} = 2^8 = 256_{10} = \text{100h}$.

| Field | Octet 1 (`192` / `C0h`) | Octet 2 (`168` / `A8h`) | Octet 3 (`10` / `0Ah`) | Octet 4 (`45` / `2Dh`) |
| :--- | :---: | :---: | :---: | :---: |
| **Host IP Bits** | `11000000` | `10101000` | `00001010` | `00101101` |
| **Subnet Mask (`/24`)** | `11111111` (Net) | `11111111` (Net) | `11111111` (Net) | `00000000` (Host) |
| **Aligned Network ID** | `11000000` (`192`) | `10101000` (`168`) | `00001010` (`10`) | `00000000` (`0`) |

#### Keystrokes in `{{key:HEX}}` Mode:
1. Network Address: `{{res:sc32_10_computer_science_bases_seq_04:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_04:value}}`** (`192.168.10.0`)
2. Wildcard Mask: `{{res:sc32_10_computer_science_bases_seq_05:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_05:value}}`** (`0.0.0.255`)
3. Broadcast Address: `{{res:sc32_10_computer_science_bases_seq_06:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_06:value}}`** (`192.168.10.255`)
4. Usable Hosts: $2^{32 - 24} - 2 = 2^8 - 2 = 256 - 2 = \mathbf{254\text{ hosts}}$ (`192.168.10.1` to `192.168.10.254`).

#### Stack Trace Table:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `C0A80A2D` | `0h` | `0h` | `0h` | `C0A80A2Dh` | `C0A80A2D_h` |
| 02 | `{{key:ENTER}}` | `0h` | `0h` | `C0A80A2Dh` | `C0A80A2Dh` | `C0A80A2Dh` |
| 03 | `100 {{key:÷R}}` | `0h` | `0h` | `2Dh` | `C0A80Ah` | `C0A80Ah` |
| 04 | `100 {{key:×}}` | `0h` | `0h` | `0h` | `C0A80A00h` | `C0A80A00h` |
| 05 | `FF {{key:+}}` | `0h` | `0h` | `0h` | `C0A80AFFh` | `C0A80AFFh` |

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

#### Keystrokes in `{{key:HEX}}` Mode:
1. `{{res:sc32_10_computer_science_bases_seq_07:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_07:value}}`** (`10.20.30.128`)
2. Wildcard mask: $32 - 27 = 5$ bits $\implies 2^5 - 1 = 31_{10} = \text{1Fh}$.
3. Broadcast: `{{res:sc32_10_computer_science_bases_seq_08:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_08:value}}`** (`10.20.30.159`)
4. Usable host range: **`10.20.30.129` through `10.20.30.158`** ($30$ usable hosts).

#### Stack Trace Table:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `0A141E8E` | `0h` | `0h` | `0h` | `A141E8Eh` | `0A141E8E_h` |
| 02 | `{{key:ENTER}}` | `0h` | `0h` | `A141E8Eh` | `A141E8Eh` | `A141E8Eh` |
| 03 | `20 {{key:÷R}}` | `0h` | `0h` | `Eh` | `50A0F4h` | `50A0F4h` |
| 04 | `20 {{key:×}}` | `0h` | `0h` | `0h` | `A141E80h` | `A141E80h` |
| 05 | `1F {{key:+}}` | `0h` | `0h` | `0h` | `A141E9Fh` | `A141E9Fh` |

---

### Problem 10.4: IPv4 Point-to-Point /30 Subnet (WAN Link)
A WAN router serial link connects two routers using `172.16.5.9 /30`.
* $172 = \text{ACh}, 16 = \text{10h}, 5 = \text{05h}, 9 = \text{09h} \implies \text{AC100509h}$.
* Subnet Mask `/30`: $30$ ones, $2$ zeros $\implies$ block size $2^2 = 4_{10} = \text{4h}$ ($255.255.255.252$).

#### Keystrokes in `{{key:HEX}}` Mode:
1. `{{res:sc32_10_computer_science_bases_seq_09:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_09:value}}`** (`172.16.5.8`)
2. Wildcard: $2^2 - 1 = 3 = \text{03h}$.
3. Broadcast: `{{res:sc32_10_computer_science_bases_seq_10:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_10:value}}`** (`172.16.5.11`)
4. Router A interface: `172.16.5.9`, Router B interface: `172.16.5.10` ($2$ usable hosts).

#### Stack Trace Table:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `AC100509` | `0h` | `0h` | `0h` | `AC100509h` | `AC100509_h` |
| 02 | `{{key:ENTER}}` | `0h` | `0h` | `AC100509h` | `AC100509h` | `AC100509h` |
| 03 | `4 {{key:÷R}}` | `0h` | `0h` | `1h` | `2B040142h` | `2B040142h` |
| 04 | `4 {{key:×}}` | `0h` | `0h` | `0h` | `AC100508h` | `AC100508h` |
| 05 | `3 {{key:+}}` | `0h` | `0h` | `0h` | `AC10050Bh` | `AC10050Bh` |

---

### Problem 10.5: IPv4 Host Route (/32) and Loopback
A BGP loopback interface is assigned `198.51.100.1 /32`.
* In Hex: IP is `C6336401h`, Mask is `FFFFFFFFh` ($255.255.255.255$).
* Network ID = Host IP = Broadcast = `198.51.100.1` (`C6336401h`).
* Usable hosts: $2^{32-32} = 2^0 = \mathbf{1\text{ host}}$.

#### Keystrokes in `{{key:HEX}}` & `{{key:DEC}}` Modes:
1. Load Host IP: `C6336401 {{key:ENTER}}` $\rightarrow$ `C6336401h`
2. Wildcard mask: `FFFFFFFF {{key:ENTER}} FFFFFFFF {{key:-}}` $\rightarrow$ `0h` (`0.0.0.0`)
3. Broadcast Address: `{{key:+}}` $\rightarrow$ **`C6336401h`** (`198.51.100.1`)
4. Host Capacity: Switch to `{{key:DEC}}`, `2 {{key:ENTER}} 0 {{key:yˣ}}` $\rightarrow$ **`1`**.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `C6336401 {{key:ENTER}}` | `0h` | `0h` | `C6336401h` | `C6336401h` | Load /32 loopback host IP |
| 02 | `FFFFFFFF {{key:ENTER}}` | `0h` | `C6336401h` | `FFFFFFFFh` | `FFFFFFFFh` | Load 32-bit all-ones mask |
| 03 | `FFFFFFFF {{key:-}}` | `0h` | `0h` | `C6336401h` | `0h` | Wildcard mask `FFFFFFFFh - FFFFFFFFh = 0h` |
| 04 | `{{key:+}}` | `0h` | `0h` | `0h` | `C6336401h` | Broadcast `C6336401h + 0h = C6336401h` |
| 05 | `{{key:BASE}} {{key:DEC}}` | 0 | 0 | 0 | 3325256705 | Switch radix to DEC |
| 06 | `2 {{key:ENTER}} 0 {{key:yˣ}}` | 0 | 3325256705 | 2 | **1** | Usable host capacity $2^0 = 1$ |

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

#### Keystrokes in `{{key:HEX}}` Mode:
1. Base Network ID: `C0A81000 {{key:ENTER}}` $\rightarrow$ `C0A81000h` (`192.168.16.0`)
2. Supernet block span: `4 {{key:ENTER}} 100 {{key:×}}` $\rightarrow$ `400h` ($1024_{10}$ addresses)
3. Wildcard Mask: `1 {{key:-}}` $\rightarrow$ `3FFh` (`0.0.3.255`)
4. Broadcast Address: `{{key:+}}` $\rightarrow$ **`C0A813FFh`** (`192.168.19.255`)
5. Usable Hosts: `3FF {{key:ENTER}} 1 {{key:-}}` $\rightarrow$ **`3FEh`** ($1022_{10}$ hosts).

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `C0A81000 {{key:ENTER}}` | `0h` | `0h` | `C0A81000h` | `C0A81000h` | Base network address `192.168.16.0` |
| 02 | `4 {{key:ENTER}} 100 {{key:×}}` | `0h` | `C0A81000h` | `4h` | `400h` | Total 4-subnet address span $4 \times 256 = 1024$ (`400h`) |
| 03 | `1 {{key:-}}` | `0h` | `0h` | `C0A81000h` | `3FFh` | Wildcard offset `400h - 1 = 3FFh` (`0.0.3.255`) |
| 04 | `{{key:+}}` | `0h` | `0h` | `0h` | **`C0A813FFh`** | Supernet broadcast address `192.168.19.255` |
| 05 | `3FF {{key:ENTER}} 1 {{key:-}}` | `0h` | `C0A813FFh` | `3FFh` | **`3FEh`** | Usable host capacity $1023 - 1 = 1022$ (`3FEh`) |

---

### Problem 10.7: Wildcard Mask Generation via 32-Bit Complement Subtraction
In Cisco ACLs, calculate the wildcard mask for `/26` ($255.255.255.192$):
1. In `{{key:HEX}}`: Mask is `FFFFFFC0h`.
2. Subtract from the 32-bit all-ones mask `FFFFFFFFh`: key `FFFFFFFF {{key:ENTER}} FFFFFFC0 {{key:-}}` $\rightarrow$ `3Fh`.
3. In `{{key:DEC}}`: `3Fh` = **`63`**.
4. Dotted decimal wildcard: `0.0.0.63`.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `FFFFFFFF {{key:ENTER}}` | `0h` | `0h` | `FFFFFFFFh` | `FFFFFFFFh` | Load 32-bit all-ones inversion bitmask |
| 02 | `FFFFFFC0 {{key:-}}` | `0h` | `0h` | `0h` | `3Fh` | Complement subtraction yields wildcard `3Fh` |
| 03 | `{{key:BASE}} {{key:DEC}}` | 0 | 0 | 0 | **63** | Convert to decimal: `0.0.0.63` |

---

### Problem 10.8: Embedded GPIO Pin Bit-Setting (`+`)
In a 32-bit GPIO direction register (`GPIO_DIR`), set Bit 5 (Output enable for status LED, currently $0$) while preserving all other pin configurations.
Current register value: `0x00001804`. Bit 5 weight: $2^5 = 32_{10} = \text{20h}$.

| Register Stage | Binary Representation (Bits 15–0) | Hexadecimal Value |
| :--- | :---: | :---: |
| **Original Register** | `0001 1000 0000 0100` | `1804h` |
| **Bit 5 Weight ($2^5$)** | `0000 0000 0010 0000` | `0020h` |
| **Updated Register (`+`)** | `0001 1000 0010 0100` | **`1824h`** |

#### Keystrokes in `{{key:HEX}}` Mode:
`{{res:sc32_10_computer_science_bases_seq_11:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_11:value}}`**

#### Stack Trace Table:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `1804` | `0h` | `0h` | `0h` | `1804h` | `1804_h` |
| 02 | `{{key:ENTER}}` | `0h` | `0h` | `1804h` | `1804h` | `1804h` |
| 03 | `20` | `0h` | `1804h` | `1804h` | `20h` | `20_h` |
| 04 | `{{key:+}}` | `0h` | `0h` | `0h` | `1824h` | `1824h` |

---

### Problem 10.9: Embedded GPIO Pin Bit-Clearing (`-`)
Clear Bit 11 (Disable motor enable line, currently $1$) in register holding `0x00002F80`.
Bit 11 weight: $2^{11} = 2048_{10} = \text{800h}$.

#### Keystrokes in `{{key:HEX}}` Mode:
`{{res:sc32_10_computer_science_bases_seq_12:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_12:value}}`**

#### Stack Trace Table:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `2F80 {{key:ENTER}}` | `0h` | `0h` | `2F80h` | `2F80h` | `2F80h` |
| 02 | `800` | `0h` | `2F80h` | `2F80h` | `800h` | `800_h` |
| 03 | `{{key:-}}` | `0h` | `0h` | `0h` | `2780h` | `2780h` |

---

### Problem 10.10: Embedded GPIO Pin Bit-Cycling (`-` / `+`)
Cycle Bit 2 (Heartbeat pulse pin) in register holding `0x00000017`.
Bit 2 weight: $2^2 = 4 = \text{4h}$.

#### Keystrokes in `{{key:HEX}}` Mode:
1. Clear pulse bit: `{{res:sc32_10_computer_science_bases_seq_13:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_13:value}}`**
2. Set pulse bit again: `{{res:sc32_10_computer_science_bases_seq_14:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_14:value}}`** (Restores original state!).

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `17 {{key:ENTER}}` | `0h` | `0h` | `17h` | `17h` | Initial GPIO register state `0x17` |
| 02 | `4 {{key:-}}` | `0h` | `0h` | `0h` | **`13h`** | Clear Bit 2 ($2^2 = 4$): `17h - 4h = 13h` |
| 03 | `4 {{key:+}}` | `0h` | `0h` | `0h` | **`17h`** | Re-set Bit 2 ($2^2 = 4$): `13h + 4h = 17h` |

---

### Problem 10.11: Multi-Bit Field Extraction (ADC Resolution Field)
A microcontroller ADC configuration register holds `0x3C6A`. Bits [7:4] define the ADC resolution code ($0 \dots 15$, where `0x6` selects 12-bit conversion mode). Extract this 4-bit field into an isolated integer in Register $X$ using `{{key:÷R}}` and `{{key:÷}}`.

| Extraction Stage | Binary Nibbles (Bits 15–0) | Hexadecimal Value |
| :--- | :---: | :---: |
| **ADC Configuration Register** | `0011 1100 0110 1010` | `3C6Ah` |
| **Lower Byte Remainder (`÷R 100h`)** | `0000 0000 0110 1010` | `006Ah` |
| **Right-Shifted Nibble (`÷ 10h`)** | `0000 0000 0000 0110` | `0006h` ($6_{10}$) |

#### Keystrokes in `{{key:HEX}}` Mode:
1. Isolate lower byte via modulo `0x100`: `{{res:sc32_10_computer_science_bases_seq_15:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_15:value}}`
2. Shift right by 4 bits ($2^4 = 16 = \text{10h}$): `{{res:sc32_10_computer_science_bases_seq_16:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_16:value}}`**

#### Stack Trace Table:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `3C6A {{key:ENTER}}` | `0h` | `0h` | `3C6Ah` | `3C6Ah` | `3C6Ah` |
| 02 | `100 {{key:÷R}}` | `0h` | `0h` | `6Ah` | `3Ch` | `3Ch` |
| 03 | `{{key:x⇄y}}` | `0h` | `0h` | `3Ch` | `6Ah` | `6Ah` |
| 04 | `10 {{key:÷}}` | `0h` | `0h` | `0h` | `6h` | `6h` |

---

### Problem 10.12: Multi-Bit Field Insertion (Read-Modify-Write)
In a peripheral timer control register currently holding `0x4521`, update the 4-bit prescaler field at bits [11:8] (currently `5h`) with value `0xA` ($10_{10}$), without altering any of the surrounding configuration bits.

| Insertion Stage | Binary Nibbles (Bits 15–0) | Hexadecimal Value |
| :--- | :---: | :---: |
| **Original Timer Register** | `0100 0101 0010 0001` | `4521h` |
| **Subtract Old Field (`- 500h`)** | `0100 0000 0010 0001` | `4021h` |
| **Shifted New Field (`A × 100h`)** | `0000 1010 0000 0000` | `0A00h` |
| **Updated Register (`+`)** | `0100 1010 0010 0001` | `4A21h` |

#### Keystrokes in `{{key:HEX}}` Mode:
1. Clear existing field: `{{res:sc32_10_computer_science_bases_seq_17:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_17:value}}`
2. Prepare shifted new field: `{{res:sc32_10_computer_science_bases_seq_18:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_18:value}}`
3. Merge fields: `{{key:+}}` $\rightarrow$ **`4A21h`**

#### Stack Trace Table:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `4521 {{key:ENTER}}` | `0h` | `0h` | `4521h` | `4521h` | `4521h` |
| 02 | `500 {{key:-}}` | `0h` | `0h` | `0h` | `4021h` | `4021h` |
| 03 | `A {{key:ENTER}}` | `0h` | `0h` | `4021h` | `Ah` | `A_h` |
| 04 | `100 {{key:×}}` | `0h` | `0h` | `4021h` | `A00h` | `A00h` |
| 05 | `{{key:+}}` | `0h` | `0h` | `0h` | `4A21h` | `4A21h` |

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

#### Keystrokes in `{{key:HEX}}` Mode:
1. Red channel bit-shift (`<< 11`): `{{res:sc32_10_computer_science_bases_seq_19:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_19:value}}` ($2^{11} = 800\text{h}$)
2. Green channel bit-shift (`<< 5`): `{{res:sc32_10_computer_science_bases_seq_20:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_20:value}}` ($2^5 = 20\text{h}$)
3. Combine Red & Green: `{{key:+}}` $\rightarrow$ `FAA0h`
4. Combine Blue: `{{res:sc32_10_computer_science_bases_seq_21:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_21:value}}`**

#### Stack Trace Table:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `1F {{key:ENTER}}` | `0h` | `0h` | `1Fh` | `1Fh` | `1Fh` |
| 02 | `800 {{key:×}}` | `0h` | `0h` | `0h` | `F800h` | `F800h` |
| 03 | `15 {{key:ENTER}}` | `0h` | `0h` | `F800h` | `15h` | `15h` |
| 04 | `20 {{key:×}}` | `0h` | `0h` | `F800h` | `2A0h` | `2A0h` |
| 05 | `{{key:+}}` | `0h` | `0h` | `0h` | `FAA0h` | `FAA0h` |
| 06 | `6 {{key:+}}` | `0h` | `0h` | `0h` | `FAA6h` | `FAA6h` |

---

### Problem 10.14: RGB565 to RGB888 Color Unpacking & Expansion
Given packed RGB565 word `0xE5B2`, extract individual color channels using `{{key:÷}}` and `{{key:÷R}}` and expand them to standard 8-bit values ($0 \dots 255$):
* Red channel (bits 15–11): divide by $2^{11} = \text{800h}$
* Green channel (bits 10–5): take remainder modulo $\text{800h}$ via `{{key:÷R}} {{key:x⇄y}}`, then divide by $2^5 = \text{20h}$
* Blue channel (bits 4–0): take remainder modulo $\text{20h}$ via `{{key:÷R}} {{key:x⇄y}}`

#### Keystrokes in `{{key:HEX}}` & `{{key:DEC}}` Modes:
1. Extract Red: `{{res:sc32_10_computer_science_bases_seq_22:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_22:value}}`** ($28_{10}$)
   * Expand in `{{key:DEC}}`: `{{res:sc32_10_computer_science_bases_seq_23:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_23:value}}`**
2. Extract Green: `{{res:sc32_10_computer_science_bases_seq_24:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_24:value}}`** ($45_{10}$)
   * Expand in `{{key:DEC}}`: `{{res:sc32_10_computer_science_bases_seq_25:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_25:value}}`**
3. Extract Blue: `{{res:sc32_10_computer_science_bases_seq_26:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_26:value}}`** ($18_{10}$)
   * Expand in `{{key:DEC}}`: `{{res:sc32_10_computer_science_bases_seq_27:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_27:value}}`**
* Unpacked TrueColor: **`RGB(230, 182, 148)`** (`#E6B694`).

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `E5B2 {{key:ENTER}} 800 {{key:÷}}` | `0h` | `0h` | `E5B2h` | **`1Ch`** | Extract 5-bit Red channel `E5B2h >> 11 = 1Ch` ($28_{10}$) |
| 02 | `{{key:BASE}} {{key:DEC}} 255 {{key:×}} 31 {{key:÷}}` | 0 | 0 | 0 | **230.32** | Expand Red to 8-bit scale ($28 \times 255 / 31 \approx 230$) |
| 03 | `{{key:BASE}} {{key:HEX}} E5B2 {{key:ENTER}} 800 {{key:÷R}} {{key:x⇄y}} 20 {{key:÷}}` | `0h` | `0h` | `1Ch` | **`2Dh`** | Remainder mod `800h`, shift right 5 bits: Green `2Dh` ($45_{10}$) |
| 04 | `{{key:BASE}} {{key:DEC}} 255 {{key:×}} 63 {{key:÷}}` | 0 | 0 | 0 | **182.14** | Expand Green to 8-bit scale ($45 \times 255 / 63 \approx 182$) |
| 05 | `{{key:BASE}} {{key:HEX}} E5B2 {{key:ENTER}} 20 {{key:÷R}} {{key:x⇄y}}` | `0h` | `0h` | `72Dh` | **`12h`** | Remainder mod `20h`: Blue `12h` ($18_{10}$) |
| 06 | `{{key:BASE}} {{key:DEC}} 255 {{key:×}} 31 {{key:÷}}` | 0 | 0 | 0 | **148.06** | Expand Blue to 8-bit scale ($18 \times 255 / 31 \approx 148$) |

---

### Problem 10.15: RGBA4444 16-Bit Texture Color Packing
In embedded OpenGL ES graphics engines, 16-bit RGBA4444 allocates 4 bits per channel:
Pack channels $R=14$ (`Eh`), $G=9$ (`9h`), $B=3$ (`3h`), $A=15$ (`Fh`):
$$(R \times \text{1000h}) + (G \times \text{100h}) + (B \times \text{10h}) + A$$

#### Keystrokes in `{{key:HEX}}` Mode:
`{{res:sc32_10_computer_science_bases_seq_28:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_28:value}}`**

> **Named RPN Stack Idiom: *The Horner Polynomial Stream & Bitfield Packing*** — Stream 4-bit nibbles $R, G, B, A$ by progressive shifting with base-16 multipliers directly in the operational stack {{cite:knuth1997,hp15c1982}}.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `E {{key:ENTER}} 1000 {{key:×}}` | `0h` | `0h` | `0h` | `E000h` | Shift Red ($14$) left by 12 bits |
| 02 | `9 {{key:ENTER}} 100 {{key:×}} {{key:+}}` | `0h` | `0h` | `0h` | `E900h` | Shift Green ($9$) left by 8 bits and accumulate |
| 03 | `3 {{key:ENTER}} 10 {{key:×}} {{key:+}}` | `0h` | `0h` | `0h` | `E930h` | Shift Blue ($3$) left by 4 bits and accumulate |
| 04 | `F {{key:+}}` | `0h` | `0h` | `0h` | **`E93Fh`** | Add Alpha ($15$) to complete 16-bit packed RGBA4444 |

---

### Problem 10.16: Base64 Binary Stream Chunking
Convert 3 bytes of raw binary data `0x4D`, `0x61`, `0x6E` (ASCII string "Man") into four 6-bit Base64 index values:
* Assembled 24-bit word: `4D616Eh` ($010011010110000101101110_2$).
* The four 6-bit slice divisors are $2^{18} = \text{40000h}$, $2^{12} = \text{1000h}$, and $2^6 = \text{40h}$.

| Base64 Sextet | 6-Bit Binary Slice | Decimal Index | Base64 Character |
| :--- | :---: | :---: | :---: |
| **Sextet 1 (Bits 23–18)** | `010011` | `19` (`13h`) | **`T`** |
| **Sextet 2 (Bits 17–12)** | `010110` | `22` (`16h`) | **`W`** |
| **Sextet 3 (Bits 11–6)** | `000101` | `5` (`05h`) | **`F`** |
| **Sextet 4 (Bits 5–0)** | `101110` | `46` (`2Eh`) | **`u`** |

#### Keystrokes in `{{key:HEX}}` Mode:
1. Sextet 1: `{{res:sc32_10_computer_science_bases_seq_29:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_29:value}}`** ($19_{10} \implies \mathbf{T}$)
2. Sextet 2: `{{res:sc32_10_computer_science_bases_seq_30:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_30:value}}`** ($22_{10} \implies \mathbf{W}$)
3. Sextet 3: `{{res:sc32_10_computer_science_bases_seq_31:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_31:value}}`** ($5_{10} \implies \mathbf{F}$)
4. Sextet 4: `{{res:sc32_10_computer_science_bases_seq_32:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_32:value}}`** ($46_{10} \implies \mathbf{u}$)
Result: "Man" encodes to **`TWFu`**.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `4D616E {{key:ENTER}} 40000 {{key:÷}}` | `0h` | `0h` | `4D616Eh` | **`13h`** | Sextet 1: `4D616Eh >> 18 = 13h` ($19_{10} \implies \mathbf{T}$) |
| 02 | `4D616E {{key:ENTER}} 40000 {{key:÷R}} {{key:x⇄y}} 1000 {{key:÷}}` | `0h` | `0h` | `13h` | **`16h`** | Sextet 2: remainder `>> 12 = 16h` ($22_{10} \implies \mathbf{W}$) |
| 03 | `4D616E {{key:ENTER}} 1000 {{key:÷R}} {{key:x⇄y}} 40 {{key:÷}}` | `0h` | `0h` | `4D6h` | **`5h`** | Sextet 3: remainder `>> 6 = 5h` ($5_{10} \implies \mathbf{F}$) |
| 04 | `4D616E {{key:ENTER}} 40 {{key:÷R}} {{key:x⇄y}}` | `0h` | `0h` | `13585h` | **`2Eh`** | Sextet 4: lower 6-bit remainder = `2Eh` ($46_{10} \implies \mathbf{u}$) |

---

### Problem 10.17: Two's Complement Negation Proof ($(2^{36} - 1 - X) + 1$)
Verify that subtracting $X$ from all ones (`FFFFFFFFFh`) and adding $1$ produces the exact mathematical two's complement negation `{{key:+/-}}`:
* Key in $42$ in `{{key:DEC}}` mode and press `{{key:+/-}}`: produces **`-42`**.
* Switch to `{{key:BASE}} {{key:HEX}}`: displays as `FFFFFFFFD6h` ($36$-bit two's complement representation).
* Verify by one's complement subtraction: `FFFFFFFFF {{key:ENTER}} 2A {{key:-}} 1 {{key:+}}` $\rightarrow$ `FFFFFFFFD6h` (`-42` in `{{key:DEC}}`).

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `42 {{key:+/-}}` | 0 | 0 | 0 | **-42** | Negate 42 directly in DEC mode |
| 02 | `{{key:BASE}} {{key:HEX}}` | `0h` | `0h` | `0h` | **`FFFFFFFFD6h`** | Inspect 36-bit two's complement hex representation |
| 03 | `FFFFFFFFF {{key:ENTER}} 2A {{key:-}}` | `0h` | `0h` | `FFFFFFFFFh` | `FFFFFFFFD5h` | One's complement bitwise inversion ($2^{36} - 1 - 42$) |
| 04 | `1 {{key:+}}` | `0h` | `0h` | `0h` | **`FFFFFFFFD6h`** | Add 1: exact two's complement match `FFFFFFFFD6h` (`-42`) |

---

### Problem 10.18: 36-Bit Two's Complement Boundary Audit
* Maximum 36-Bit Signed Positive:
  `7FFFFFFFFh` = $+34,359,738,367_{10}$
* Add 1: `{{res:sc32_10_computer_science_bases_seq_33:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_33:value}}` ($-34,359,738,368_{10}$, Minimum Negative Bound).

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `7FFFFFFFF` `{{key:ENTER}}` — Load the maximum signed positive 36-bit boundary value ($7\text{FFFFFFFF}_{16}$) into Register $Y$.
2. `1` `{{key:+}}` — Key increment 1 and add; two's complement boundary rolls over to minimum negative bound ($800000000_{16} = -34,359,738,368_{10}$).

* Subtract 1 from 0: `{{res:sc32_10_computer_science_bases_seq_34:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_34:value}}` ($-1_{10}$).

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `7FFFFFFFF {{key:ENTER}}` | `0h` | `0h` | `7FFFFFFFFh` | `7FFFFFFFFh` | Load maximum signed positive 36-bit bound |
| 02 | `1 {{key:+}}` | `0h` | `0h` | `0h` | **`800000000h`** | Overflow rolls over to minimum negative bound |
| 03 | `0 {{key:ENTER}} 1 {{key:-}}` | `0h` | `0h` | `0h` | **`FFFFFFFFFFFFFFFFh`** | Zero minus 1 rolls under to all ones ($-1_{10}$) |

---

### Problem 10.19: Arithmetic Right Shift via Signed Integer Division
For signed negative integer $-64$:
* In `{{key:DEC}}`: `{{res:sc32_10_computer_science_bases_seq_35:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_35:value}}`** (Exact arithmetic right shift by 2 bits, sign-extended).

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `64 {{key:+/-}}` `{{key:ENTER}}` — Load the signed negative dividend ($-64$) into Register $Y$.
2. `4` `{{key:÷}}` — Key shift divisor ($2^2 = 4$) into $X$ and execute integer division; exact arithmetic right shift with sign extension ($-16$) resolves without auxiliary memory.

* In `{{key:HEX}}`: `-64` is `FFFFFFFFC0h`. Dividing by $4$ produces `FFFFFFFFF0h` ($-16_{10}$).

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `64 {{key:+/-}} {{key:ENTER}}` | 0 | 0 | -64 | -64 | Load dividend $-64$ into Y and X |
| 02 | `4 {{key:÷}}` | 0 | 0 | 0 | **-16** | Divide by $2^2 = 4$ for arithmetic right shift by 2 |
| 03 | `{{key:BASE}} {{key:HEX}}` | `0h` | `0h` | `0h` | **`FFFFFFFFF0h`** | 36-bit sign-extended hex confirms $-16$ |

---

### Problem 10.20: Division with Remainder via `{{key:÷R}}`
Compute $12345 \div 16$ with simultaneous quotient and remainder:
Keystrokes: `{{res:sc32_10_computer_science_bases_seq_01:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_01:value}}`**

> **Named RPN Stack Idiom: *The x⇄y Denominator Flip & Euclidean Remainder Pipeline*** — Execute integer division with remainder via `{{key:÷R}}`, simultaneously producing the integer quotient in $Y$ and exact remainder in $X$ without register allocation {{cite:knuth1997,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `12345` `{{key:ENTER}}` — Load the integer dividend ($12,345$) into Register $Y$.
2. `16` `{{key:÷R}}` — Enter divisor ($16$) and execute division with remainder; Register $Y$ receives remainder ($9$) and Register $X$ receives quotient ($771$) without intermediate registers.

* Register $X$: **`771`** (Whole quotient $Q$)
* Register $Y$: **`9`** (Remainder $R$, identical to $12345 \bmod 16$).

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `12345 {{key:ENTER}}` | 0 | 0 | 12345 | 12345 | Load integer dividend $12,345$ |
| 02 | `16 {{key:÷R}}` | 0 | 0 | **9** | **771** | Quotient $Q=771$ in Register X, remainder $R=9$ in Register Y |
| 03 | `{{key:x⇄y}}` | 0 | 0 | 771 | **9** | Swap registers to access remainder $9$ directly |

---

### Problem 10.21: Telemetry Bit-Difference Inspection
Determine the differing bit positions between telemetry word `0x5F5A` and baseline `0x5A50`:
Keystrokes in `{{key:HEX}}`: `{{res:sc32_10_computer_science_bases_seq_36:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_36:value}}`** ($0000010100001010_2$ in `{{key:BIN}}`).

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `5F5A` `{{key:ENTER}}` — Load telemetry word `0x5F5A` into Register $Y$.
2. `5A50` `{{key:-}}` — Enter baseline `0x5A50` and subtract ($5\text{F5A}_{16} - 5\text{A50}_{16}$); difference `50Ah` isolates bit disparities.

Bits 1, 3, 8, 10 are set, revealing a Hamming distance of **$4\text{ bits}$**.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `5F5A {{key:ENTER}}` | `0h` | `0h` | `5F5Ah` | `5F5Ah` | Load received telemetry word `0x5F5A` |
| 02 | `5A50 {{key:-}}` | `0h` | `0h` | `0h` | **`50Ah`** | Difference isolates bit discrepancies |
| 03 | `{{key:BASE}} {{key:BIN}}` | `0b` | `0b` | `0b` | **`10100001010b`** | Inspect binary bitfield: 4 differing bit positions |

---

### Problem 10.22: Parity Bit Generation
Data byte `0x3B` ($00111011_2$, five ones $\implies$ odd parity).
For even parity, the MSB parity bit (Bit 7, weight $2^7 = 128_{10} = \text{80h}$) must be set to $1$:
`{{res:sc32_10_computer_science_bases_seq_37:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_37:value}}`**.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `3B` `{{key:ENTER}}` — Load data byte `0x3B` into Register $Y$.
2. `80` `{{key:+}}` — Key MSB parity mask value $80_{16}$ and add; resulting byte `BBh` sets the parity bit.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `3B {{key:ENTER}}` | `0h` | `0h` | `3Bh` | `3Bh` | Load data byte `0x3B` ($00111011_2$) |
| 02 | `80 {{key:+}}` | `0h` | `0h` | `0h` | **`BBh`** | Set MSB Bit 7 for even parity ($10111011_2$) |

---

### Problem 10.23: Longitudinal Redundancy Check (LRC)
Calculate LRC across message bytes `0x02`, `0x41`, `0x42`:
`{{res:sc32_10_computer_science_bases_seq_38:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_38:value}}`.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `2` `{{key:ENTER}}` — Deposit the initial message byte (`0x02`) onto the stack.
2. `41` `{{key:+}}` — Key the second message byte (`0x41`) and accumulate; the partial sum (`0x43`) appears on the display.
3. `42` `{{key:+}}` — Key the third message byte (`0x42`) and accumulate; total unmasked message sum (`0x85`) occupies Register $X$.
4. `256` `{{key:÷R}}` — Execute modulo 256 division; the single-byte remainder (`0x85`) resides in Register $Y$.
5. `256` `{{key:x⇄y}}` `{{key:-}}` — Compute the two's complement additive checksum (`0x7B`) in place.

LRC = $(256 - \text{Sum}) \bmod 256$: `{{res:sc32_10_computer_science_bases_seq_39:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_39:value}}`**.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `2 {{key:ENTER}} 41 {{key:+}}` | `0h` | `0h` | `0h` | `43h` | Accumulate first two bytes `2h + 41h = 43h` |
| 02 | `42 {{key:+}}` | `0h` | `0h` | `0h` | **`85h`** | Accumulate third byte `43h + 42h = 85h` |
| 03 | `100 {{key:ENTER}} 85 {{key:-}}` | `0h` | `0h` | `100h` | **`7Bh`** | LRC checksum $(256 - \text{Sum}) \bmod 256 = \text{7Bh}$ |

---

### Problem 10.24: CRC-16-CCITT Modulo-2 Polynomial Division
Generator `0x1021`. For message byte `0xC5` padded with 16 zeros:
Modulo-2 division yields CRC remainder **`0x7B9A`**.

#### Keystrokes in `{{key:HEX}}` Mode:
1. Load zero-padded message: `C50000 {{key:ENTER}}` $\rightarrow$ `C50000h`
2. Load generator: `1021 {{key:ENTER}}` $\rightarrow$ `1021h`
3. Execute polynomial division: `{{key:÷R}}` $\rightarrow$ Remainder **`7B9Ah`**.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `C50000 {{key:ENTER}}` | `0h` | `0h` | `C50000h` | `C50000h` | Load 16-bit zero-padded message `0xC50000` |
| 02 | `1021 {{key:ENTER}}` | `0h` | `C50000h` | `1021h` | `1021h` | Load CRC-16-CCITT generator polynomial `0x1021` |
| 03 | `{{key:÷R}}` | `0h` | `0h` | `C4h` | **`7B9Ah`** | Polynomial division leaves CRC remainder `7B9Ah` |

---

### Problem 10.25: CRC-32 Frame Check Sequence
Ethernet generator polynomial `0xEDB88320`. Direct polynomial reduction verifies FCS error detection capability across 1500-byte MTU packets.

#### Keystrokes in `{{key:HEX}}` Mode:
1. Load inversion mask: `FFFFFFFF {{key:ENTER}}` $\rightarrow$ `FFFFFFFFh`
2. Subtract Ethernet polynomial: `EDB88320 {{key:-}}` $\rightarrow$ `12477CDh`
3. Switch radix: `{{key:BASE}} {{key:DEC}}` $\rightarrow$ **`19167181`**.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `FFFFFFFF {{key:ENTER}}` | `0h` | `0h` | `FFFFFFFFh` | `FFFFFFFFh` | Load 32-bit initial inversion mask |
| 02 | `EDB88320 {{key:-}}` | `0h` | `0h` | `0h` | `12477CDh` | Subtract Ethernet polynomial for inverted preset |
| 03 | `{{key:BASE}} {{key:DEC}}` | 0 | 0 | 0 | **19167181** | Inspect 32-bit check state in DEC radix |

---

### Problem 10.26: UART Fractional Baud Rate Divisor at 150 MHz
A high-performance dual-core microcontroller runs its peripheral system clock at $f_{\text{clk}} = 150.0\text{ MHz}$ ($150,000,000\text{ Hz}$). The hardware UART baud rate generator features an integer baud rate register (`IBRD`, 16-bit) and a fractional baud rate register (`FBRD`, 6-bit with divisor $64$) over an $8\times$ oversampling receiver clock.
Determine `IBRD` and `FBRD` to configure a target baud rate of $115,200\text{ baud}$, and calculate the resulting baud rate error percentage.

$$\text{Baud Divider} = \frac{f_{\text{clk}}}{8 \times \text{Baud}} = \frac{150,000,000}{8 \times 115,200} = \frac{150,000,000}{921,600} \approx 162.760416667$$

#### Keystrokes in `{{key:ALL}}` Mode:
1. `{{res:sc32_10_computer_science_bases_seq_40:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_40:value}}`**
2. Integer divider `IBRD`: `{{key:ENTER}} {{key:PARTS}} {{key:IP}}` $\rightarrow$ **`162`** (`0xA2`)
3. Fractional divider `FBRD`: `{{key:x⇄y}} {{key:PARTS}} {{key:FP}} 64 {{key:×}} {{key:PARTS}} {{key:IP}}` $\rightarrow$ **`48`** (or rounded: **`49`** `0x31`)
4. Actual baud rate: $150,000,000 / (8 \times (162 + 49/64)) = 150,000,000 / 1302.125 = \mathbf{115,196.3\text{ baud}}$
5. Baud Error: $(115196.3 - 115200) / 115200 \times 100\% = \mathbf{-0.0032\%}$ (Near zero error!).

#### Stack Trace Table:

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

#### Keystrokes:
`{{res:sc32_10_computer_science_bases_seq_53:keys}}` $\rightarrow$ $7.5$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `75.0` `{{key:ENTER}}` — Arm Register $Y$ with the master SPI peripheral clock frequency ($75.0\text{ MHz}$).
2. `10.0` `{{key:÷}}` — Enter maximum peripheral flash frequency ($10.0\text{ MHz}$) and divide; minimum required divider ratio ($7.50$) condenses in $X$.
3. `8` `{{key:ENTER}}` — Select the lowest power-of-two prescaler divider exceeding $7.5$ ($P = 8$).
4. `75.0` `{{key:x⇄y}}` `{{key:÷}}` — Divide master clock by prescaler divider; the actual operational SPI bus clock frequency ($f_{\text{SPI}} = 9.375\text{ MHz}$) is verified.

Since the divider must be a power of two $\ge 7.5$, select **`8`** (`2³`).
Actual SPI frequency: `{{res:sc32_10_computer_science_bases_seq_54:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_54:value}}`** ($9,375,000\text{ Hz}$).

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `75 {{key:ENTER}} 10 {{key:÷}}` | $0.0000$ | $0.0000$ | $75.0000$ | **$7.5000$** | Minimum prescaler ratio $75/10 = 7.5$ |
| 02 | `8 {{key:ENTER}}` | $0.0000$ | $7.5000$ | $8.0000$ | $8.0000$ | Select next power-of-two divider $P = 8$ |
| 03 | `75 {{key:x⇄y}} {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | **`{{res:sc32_10_computer_science_bases_seq_54:value}}`** | Operational SPI frequency $75/8 = 9.375\text{ MHz}$ |

---

### Problem 10.28: I2C Fast-Mode Plus SCL Timing Register Calculations
Target I2C clock frequency $f_{\text{SCL}} = 1.0\text{ MHz}$ ($1000\text{ ns}$ cycle time) derived from a $150.0\text{ MHz}$ core clock period ($T_{\text{clk}} = \frac{1}{150\times 10^6} \approx 6.6667\text{ ns}$).
Total clocks per SCL period: $150\text{ cycles}$.
In Fast-Mode Plus, asymmetric duty cycle allocates $t_{\text{LOW}} \ge 500\text{ ns}$ and $t_{\text{HIGH}} \ge 260\text{ ns}$.
Allocating $\frac{1}{3}$ high and $\frac{2}{3}$ low:
* $t_{\text{HIGH}} = 50\text{ cycles} \times 6.6667\text{ ns} = \mathbf{333.3\text{ ns}}$ ($> 260\text{ ns}$)
* $t_{\text{LOW}} = 100\text{ cycles} \times 6.6667\text{ ns} = \mathbf{666.7\text{ ns}}$ ($> 500\text{ ns}$).

#### Keystrokes:
1. Total cycles: `150 {{key:ENTER}} 1 {{key:÷}}` $\rightarrow$ $150$ cycles
2. High phase clocks: `3 {{key:÷}}` $\rightarrow$ $50$ cycles
3. Timing durations: `150 {{key:ENTER}} 6.6667 {{key:×}} 3 {{key:÷}}` $\rightarrow$ **`333.3 ns`** ($t_{\text{HIGH}}$); `2 {{key:×}}` $\rightarrow$ **`666.7 ns`** ($t_{\text{LOW}}$).

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `150 {{key:ENTER}} 1 {{key:÷}}` | $0.0000$ | $0.0000$ | $150.0000$ | $150.0000$ | Total clock cycles per SCL period at 150 MHz |
| 02 | `3 {{key:÷}}` | $0.0000$ | $0.0000$ | $0.0000$ | $50.0000$ | High-phase allocation: $150 / 3 = 50\text{ cycles}$ |
| 03 | `150 {{key:ENTER}} 6.6667 {{key:×}} 3 {{key:÷}}` | $0.0000$ | $50.0000$ | $1000.0050$ | **$333.3350$** | High time $t_{\text{HIGH}} = 333.3\text{ ns} > 260\text{ ns}$ spec |
| 04 | `2 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$666.6700$** | Low time $t_{\text{LOW}} = 666.7\text{ ns} > 500\text{ ns}$ spec |

---

### Problem 10.29: 32-Bit Byte Swapping (Endianness Reversal)
Network sockets receive data in Big-Endian format, while ARM Cortex processors operate natively in Little-Endian. Convert Big-Endian integer `0x12345678` into Little-Endian `0x78563412` using `{{key:÷R}}`, `{{key:÷}}`, `{{key:×}}`, and `{{key:+}}`.

| Byte Order | Byte 3 (MSB) | Byte 2 | Byte 1 | Byte 0 (LSB) |
| :--- | :---: | :---: | :---: | :---: |
| **Big-Endian (`12345678h`)** | `12h` | `34h` | `56h` | `78h` |
| **Shift Operation** | `>> 24` (`÷ 1000000h`) | `>> 8` (`÷ 100h`) | `<< 8` (`× 100h`) | `<< 24` (`× 1000000h`) |
| **Little-Endian (`78563412h`)** | `78h` | `56h` | `34h` | `12h` |

#### Keystrokes in `{{key:HEX}}` Mode:
1. Extract Byte 0 and shift to Byte 3: `{{res:sc32_10_computer_science_bases_seq_41:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_41:value}}`
2. Extract Byte 1 and shift to Byte 2: `{{res:sc32_10_computer_science_bases_seq_42:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_42:value}}`
3. Extract Byte 2 and shift to Byte 1: `{{res:sc32_10_computer_science_bases_seq_43:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_43:value}}`
4. Extract Byte 3 and shift to Byte 0: `{{res:sc32_10_computer_science_bases_seq_44:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_44:value}}`
5. Merge all 4 non-overlapping bytes via `{{key:+}}`: `{{key:+}} {{key:+}} {{key:+}}` $\rightarrow$ **`78563412h`**

#### Stack Trace Table:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `Byte 0 << 24` | `0h` | `0h` | `0h` | `78000000h` | `78000000h` |
| 02 | `Byte 1 << 8` | `0h` | `0h` | `78000000h` | `560000h` | `560000h` |
| 03 | `{{key:+}}` | `0h` | `0h` | `0h` | `78560000h` | `78560000h` |
| 04 | `Byte 2 >> 8` | `0h` | `0h` | `78560000h` | `3400h` | `3400h` |
| 05 | `{{key:+}}` | `0h` | `0h` | `0h` | `78563400h` | `78563400h` |
| 06 | `Byte 3 >> 24` | `0h` | `0h` | `78563400h` | `12h` | `12h` |
| 07 | `{{key:+}}` | `0h` | `0h` | `0h` | `78563412h` | `78563412h` |

---

### Problem 10.30: IEEE-754 32-Bit Single Precision Float Unpacking
Decompose the IEEE-754 single-precision float value $-6.25$ into Sign, Biased Exponent, and Fractional Mantissa:
1. Absolute value: $6.25_{10} = 4 + 2 + 0.25 = 110.01_2 = 1.1001_2 \times 2^2$.
2. Sign Bit: Negative $\implies S = \mathbf{1}$.
3. Biased Exponent: $E = \text{exponent} + 127 = 2 + 127 = 129_{10} = 10000001_2 = \mathbf{81h}$.
4. Fractional Mantissa: $M = 10010000000000000000000_2 = \mathbf{480000h}$.
5. 32-Bit Binary Hex Word: `1 10000001 10010000000000000000000` = **`0xC0C80000`**.

#### Keystrokes in `{{key:HEX}}` Mode:
`C0C80000 {{key:ENTER}} 800000 {{key:÷R}} 100 {{key:÷R}}` $\rightarrow$ Quotient: `1h` (Sign $S=1$), Remainder: `81h` (Biased Exponent $E=129_{10}$).

#### Stack Trace Table:
| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `C0C80000 {{key:ENTER}}` | `0h` | `0h` | `C0C80000h` | `C0C80000h` | `C0C80000h` |
| 02 | `800000 {{key:÷R}}` | `0h` | `0h` | `480000h` | `181h` | `181h` |
| 03 | `100 {{key:÷R}}` | `0h` | `480000h` | `81h` | `1h` | `1h` |
| 04 | `{{key:BASE}} {{key:DEC}}` | 0 | 4718592 | 129 | 1 | `1` |
| 05 | `{{key:x⇄y}} 127 {{key:-}}` | 0 | 4718592 | 1 | 2 | `2` |

**Unpacked Fields:**
* **Sign Bit ($S$):** $1$ (Negative)
* **Biased Exponent ($E$):** `81h` ($129_{10} \implies e = 129 - 127 = \mathbf{2}$)
* **Fractional Mantissa ($M$):** `480000h` ($\frac{4,718,592}{2^{23}} = 0.5625 = \frac{9}{16}$)
* **Reconstructed Value:** $(-1)^1 \times 2^2 \times (1 + 0.5625) = -4 \times 1.5625 = \mathbf{-6.25}$.

---

### Problem 10.31: IEEE-754 64-Bit Double Precision Float Unpacking
Decompose the double-precision float value $-13.375$:
1. $13.375_{10} = 8 + 4 + 1 + 0.25 + 0.125 = 1101.011_2 = 1.101011_2 \times 2^3$.
2. Sign $S = 1$.
3. Biased Exponent: $3 + 1023 = 1026_{10} = 10000000010_2 = \mathbf{402h}$.
4. Fractional Mantissa (52 bits): $101011000000\dots0_2$.
5. Assembled Hex Word: **`0xC02AC00000000000`** (High 32-bit Word: `0xC02AC000`).

#### Keystrokes in `{{key:HEX}}` Mode:
`C02AC000 {{key:ENTER}} 100000 {{key:÷R}} 800 {{key:÷R}}` $\rightarrow$ Quotient: `1h` (Sign $S=1$), Remainder: `402h` (Biased Exponent $E=1026_{10}$).

#### Stack Trace Table:
| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `C02AC000 {{key:ENTER}}` | `0h` | `0h` | `C02AC000h` | `C02AC000h` | `C02AC000h` |
| 02 | `100000 {{key:÷R}}` | `0h` | `0h` | `AC000h` | `C02h` | `C02h` |
| 03 | `800 {{key:÷R}}` | `0h` | `AC000h` | `402h` | `1h` | `1h` |
| 04 | `{{key:BASE}} {{key:DEC}}` | 0 | 704512 | 1026 | 1 | `1` |
| 05 | `{{key:x⇄y}} 1023 {{key:-}}` | 0 | 704512 | 1 | 3 | `3` |

**Unpacked Fields:**
* **Sign Bit ($S$):** $1$ (Negative)
* **Biased Exponent ($E$):** `402h` ($1026_{10} \implies e = 1026 - 1023 = \mathbf{3}$)
* **Fractional Mantissa Upper ($M_{\text{high}}$):** `AC000h` ($\frac{704,512}{2^{20}} = 0.671875 = \frac{43}{64}$)
* **Reconstructed Value:** $(-1)^1 \times 2^3 \times (1 + 0.671875) = -8 \times 1.671875 = \mathbf{-13.375}$.

---

### Problem 10.32: Fixed-Point Q16.16 Arithmetic Multiplication
In digital signal processing without FPU acceleration, numbers are formatted as signed Q16.16 (16 integer bits, 16 fractional bits, scaling factor $2^{16} = 65,536$).
Multiply $A = 3.5$ and $B = 2.25$:
* $A = 3.5 \times 65536 = 229,376 = \text{38000h}$
* $B = 2.25 \times 65536 = 147,456 = \text{24000h}$
* Product formula: $C = (A \times B) \gg 16 = (A \times B) / 65536$.

#### Keystrokes in `{{key:HEX}}` Mode:
`{{res:sc32_10_computer_science_bases_seq_45:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_45:value}}`**

> **Named RPN Stack Idiom: *The Constant-in-T Pipeline & Q16.16 Scaling*** — Multiply fixed-point integer words, then divide by radix scaling factor $2^{16} = 65,536$ in place in a single dyadic cycle {{cite:knuth1997,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `229376` `{{key:ENTER}}` — Load the fixed-point multiplicand word ($A = 3.5 \times 65536 = 229,376$) into Register $Y$.
2. `147456` `{{key:×}}` — Key multiplier fixed-point word ($B = 2.25 \times 65536 = 147,456$) and multiply; raw 32-bit product ($3.3823 \times 10^{10}$) forms in $X$.
3. `65536` `{{key:÷}}` — Divide by fixed-point base scale ($2^{16} = 65,536$); scaled Q16.16 integer product ($516,096 = \text{7E000h}$) resolves in $X$.
4. `65536` `{{key:÷}}` — Divide by base scale once more to verify real mathematical result ($7.875$) with zero parentheses.

Convert `7E000h` to decimal: `{{key:BASE}} {{key:DEC}}` $\rightarrow$ $516,096$.
Divide by scale factor: `{{res:sc32_10_computer_science_bases_seq_46:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_46:value}}`** (Exact analytical product $3.5 \times 2.25$!).

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `38000 {{key:ENTER}}` | `0h` | `0h` | `38000h` | `38000h` | Load Q16.16 multiplicand $A=3.5$ (`38000h`) |
| 02 | `24000 {{key:×}}` | `0h` | `0h` | `0h` | `7E0000000h` | Compute raw 32-bit product ($A \times B$) |
| 03 | `10000 {{key:÷}}` | `0h` | `0h` | `0h` | **`7E000h`** | Divide by radix scale factor $2^{16} = \text{10000h}$ |
| 04 | `{{key:BASE}} {{key:DEC}}` | 0 | 0 | 0 | 516096 | Switch radix to inspect decimal fixed-point word |
| 05 | `65536 {{key:÷}}` | 0 | 0 | 0 | **`7.875`** | Divide by 65536 to reveal exact product ($3.5 \times 2.25$) |

---

### Problem 10.33: Permutations ($nPr$) in Cryptography S-Box Design
Calculate the total number of ways to construct an ordered 4-element substitution key from a pool of 16 distinct nibbles:
$$P(16, 4) = \frac{16!}{(16 - 4)!} = 16 \times 15 \times 14 \times 13 = \mathbf{43,680}$$

#### Keystrokes:
`{{res:sc32_10_computer_science_bases_seq_47:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_47:value}}`**

> **Named RPN Stack Idiom: *The LASTX Dual-Branch Trick & Combinatorial Pipeline*** — Evaluate permutations $P(n, r) = n! / (n-r)!$ via `{{key:PROB}} {{key:Pn,r}}` with zero factorial overflow {{cite:knuth1997,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `16` `{{key:ENTER}}` — Arm Register $Y$ with the total element pool size ($n = 16$).
2. `4` `{{key:PROB}} {{key:Pn,r}}` — Enter permutation subset size ($r = 4$) and execute $P(n, r)$ in place; total ordered substitution keys ($P(16, 4) = 43,680$) resolve immediately.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `16 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $16.0000$ | $16.0000$ | Load total pool elements $n = 16$ |
| 02 | `4 {{key:PROB}} {{key:Pn,r}}` | $0.0000$ | $0.0000$ | $0.0000$ | **`43680.0000`** | Permutations $P(16, 4) = 43,680$ without overflow |

---

### Problem 10.34: Combinations ($nCr$) and Hamming Sphere
In a $[7, 4]$ Hamming code, calculate the number of possible 2-bit error patterns:
$$\binom{7}{2} = \frac{7!}{2! \times 5!} = \mathbf{21}$$

#### Keystrokes:
`{{res:sc32_10_computer_science_bases_seq_48:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_48:value}}`**

> **Named RPN Stack Idiom: *The Binomial Coefficient Pipeline*** — Evaluate combinations $\binom{n}{r} = \frac{n!}{r!(n-r)!}$ directly in the operational stack via `{{key:PROB}} {{key:Cn,r}}` without scratch registers {{cite:knuth1997,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `7` `{{key:ENTER}}` — Arm Register $Y$ with the Hamming codeword length ($n = 7$).
2. `2` `{{key:PROB}} {{key:Cn,r}}` — Enter error bit pattern count ($r = 2$) and execute $C(n, r)$ in place; total 2-bit Hamming sphere combinations ($\binom{7}{2} = 21$) form in Register $X$.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `7 {{key:ENTER}}` | $0.0000$ | $0.0000$ | $7.0000$ | $7.0000$ | Load Hamming codeword length $n = 7$ |
| 02 | `2 {{key:PROB}} {{key:Cn,r}}` | $0.0000$ | $0.0000$ | $0.0000$ | **`21.0000`** | Combinations $\binom{7}{2} = 21$ in Register X |

---

### Problem 10.35: Factorials and Stirling's Approximation Comparison
Calculate $15!$:
Exact: `{{res:sc32_10_computer_science_bases_seq_49:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_49:value}}`**.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `15` — Enter 15 into Register $X$ ($X = 15$).
2. `{{key:PROB}}` — Apply `PROB` on the active stack $\rightarrow \mathbf{1,307,674,368,000}$.
3. `{{key:x!}}` — Compute factorial $15!$ in place $\rightarrow$ ($X = 1.308e+12$).

Stirling's approximation: $\sqrt{2\pi n} (n/e)^n \approx 1.3004 \times 10^{12}$ (Error $< 0.6\%$).

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `15` | $0.0000$ | $0.0000$ | $0.0000$ | $15.0000$ | Enter operand $n = 15$ |
| 02 | `{{key:PROB}} {{key:x!}}` | $0.0000$ | $0.0000$ | $0.0000$ | **`1.307674E12`** | Exact factorial $15! = 1,307,674,368,000$ |

---

### Problem 10.36: Pseudo-Random Number Generation (`RAND`)
Generate 3 uniform random floats:
`{{key:PROB}} {{key:RAND}}` $\rightarrow$ $0.724194$
`{{key:PROB}} {{key:RAND}}` $\rightarrow$ $0.183022$
`{{key:PROB}} {{key:RAND}}` $\rightarrow$ $0.941581$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Load Word / Address into Register $X$:** Enter the integer operand or field width into Register $X$ and press `{{key:ENTER}}` to lift it into Register $Y$.
2. **Execute Base / Modulo Arithmetic:** Perform positional power-of-two scaling (`2 {{key:ENTER}} n {{key:yˣ}}`) or Euclidean division (`{{key:÷R}}`), then switch display radix via `{{key:BASE}}` (`{{key:HEX}}`, `{{key:DEC}}`, `{{key:OCT}}`, `{{key:BIN}}`) to inspect the exact 36-bit word representation in Register $X$.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `{{key:PROB}} {{key:RAND}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$0.724194$** | First pseudo-random draw $U_1 \in [0, 1)$ |
| 02 | `{{key:PROB}} {{key:RAND}}` | $0.0000$ | $0.0000$ | $0.724194$ | **$0.183022$** | Second draw $U_2$ lifts $U_1$ into Register Y |
| 03 | `{{key:PROB}} {{key:RAND}}` | $0.0000$ | $0.724194$ | $0.183022$ | **$0.941581$** | Third draw $U_3$ preserves stack history in Z and Y |

---

### Problem 10.37: Pseudo-Random Die Roll Simulation
Simulate a standard 6-sided die roll:
`{{key:PROB}} {{key:RAND}} 6 {{key:×}} 1 {{key:+}} {{key:PARTS}} {{key:IP}}` $\rightarrow$ Integer in $1 \dots 6$.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Load Word / Address into Register $X$:** Enter the integer operand or field width into Register $X$ and press `{{key:ENTER}}` to lift it into Register $Y$.
2. **Execute Base / Modulo Arithmetic:** Perform positional power-of-two scaling (`2 {{key:ENTER}} n {{key:yˣ}}`) or Euclidean division (`{{key:÷R}}`), then switch display radix via `{{key:BASE}}` (`{{key:HEX}}`, `{{key:DEC}}`, `{{key:OCT}}`, `{{key:BIN}}`) to inspect the exact 36-bit word representation in Register $X$.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `{{key:PROB}} {{key:RAND}}` | $0.0000$ | $0.0000$ | $0.0000$ | $0.724194$ | Generate uniform float $U \in [0, 1)$ |
| 02 | `6 {{key:×}}` | $0.0000$ | $0.0000$ | $0.0000$ | $4.345164$ | Scale to $[0, 6)$: $0.724194 \times 6 = 4.345164$ |
| 03 | `1 {{key:+}}` | $0.0000$ | $0.0000$ | $0.0000$ | $5.345164$ | Shift range to $[1, 7)$: $4.345164 + 1 = 5.345164$ |
| 04 | `{{key:PARTS}} {{key:IP}}` | $0.0000$ | $0.0000$ | $0.0000$ | **$5.0000$** | Truncate integer part: discrete die face value $5 \in \{1 \dots 6\}$ |

---

### Problem 10.38: Circular Left Rotation (ROL 1) on an 8-Bit Byte via `{{key:÷R}}`
Rotate `0x85` ($10000101_2$) left by 1 bit $\implies 00001011_2 = \text{0Bh}$.
1. Shift left by 1 bit: `{{res:sc32_10_computer_science_bases_seq_50:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_50:value}}`.
2. Split 8-bit remainder (`0Ah` in $Y$) and overflow carry (`1h` in $X$) via `{{key:÷R}}`: `{{res:sc32_10_computer_science_bases_seq_51:keys}}` $\rightarrow$ `{{res:sc32_10_computer_science_bases_seq_51:value}}`.
3. Add carry into LSB: `{{res:sc32_10_computer_science_bases_seq_52:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_52:value}}`**.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `85 {{key:ENTER}} 2 {{key:×}}` | `0h` | `0h` | `0h` | **`10Ah`** | Shift byte left by 1 bit ($85\text{h} \times 2 = 10\text{Ah}$) |
| 02 | `100 {{key:÷R}}` | `0h` | `0h` | `Ah` | **`1h`** | Extract carry bit ($X=1\text{h}$) and rotated byte ($Y=\text{Ah}$) |
| 03 | `{{key:+}}` | `0h` | `0h` | `0h` | **`Bh`** | Add carry bit into LSB: $10\text{h} \bmod 100\text{h} + 1 = \text{Bh}$ |

---

### Problem 10.39: Decimal to Binary Conversion & Bit Inspection
Convert decimal `13` into its 4-bit binary representation and verify its bit weights ($8 + 4 + 0 + 1$):
Keystrokes: `{{res:sc32_10_computer_science_bases_seq_02:keys}}` $\rightarrow$ **`{{res:sc32_10_computer_science_bases_seq_02:value}}`** ($1101_2$).

> **Named RPN Stack Idiom: *The Horner Polynomial Stream & Radix Inspection*** — Key decimal integer in `{{key:DEC}}` mode, switch to `{{key:BIN}}`, and inspect bitfields directly across display segments with zero conversion error {{cite:shannon1938,hp15c1982}}.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. `13` `{{key:ENTER}}` — Load the decimal integer ($13$) into Register $Y$.
2. `{{key:BIN}}` — Switch display radix mode to binary; exact bit sequence ($1101_2$) resolves on the transflective LCD with zero parentheses.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `13 {{key:ENTER}}` | 0 | 0 | 13 | 13 | Key decimal value 13 in DEC mode |
| 02 | `{{key:BASE}} {{key:BIN}}` | `0b` | `0b` | `1101b` | **`1101b`** | Switch to BIN mode: inspect bit weights $8 + 4 + 1$ |
| 03 | `{{key:BASE}} {{key:DEC}}` | 0 | 0 | 13 | 13 | Revert to DEC mode: stack values preserved intact |

---

### Problem 10.40: Binary to Hexadecimal & Decimal Reconstruction
Convert binary `1101b` back to decimal (`13`) and hexadecimal (`Dh`) via `{{key:BASE}} {{key:DEC}}` and `{{key:BASE}} {{key:HEX}}`, confirming lossless radix conversion across all stack registers.

**Step-by-Step RPN Reasoning & Stack Logic:**
1. **Load Word / Address into Register $X$:** Enter the integer operand or field width into Register $X$ and press `{{key:ENTER}}` to lift it into Register $Y$.
2. **Execute Base / Modulo Arithmetic:** Perform positional power-of-two scaling (`2 {{key:ENTER}} n {{key:yˣ}}`) or Euclidean division (`{{key:÷R}}`), then switch display radix via `{{key:BASE}}` (`{{key:HEX}}`, `{{key:DEC}}`, `{{key:OCT}}`, `{{key:BIN}}`) to inspect the exact 36-bit word representation in Register $X$.

#### Stack Trace Table:

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `1101 {{key:ENTER}}` | `0b` | `0b` | `1101b` | `1101b` | Enter binary word `1101b` |
| 02 | `{{key:BASE}} {{key:HEX}}` | `0h` | `0h` | `Dh` | **`Dh`** | Convert to HEX radix: $1101_2 = \text{Dh}$ |
| 03 | `{{key:BASE}} {{key:DEC}}` | 0 | 0 | 13 | **13** | Convert to DEC radix: confirms decimal 13 |

---

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

## Summary & Looking Ahead

Chapter 10 demystified the low-level binary foundation of digital computation. Operating across an authentic 36-bit two's complement integer architecture, you navigated Hexadecimal, Decimal, Octal, and Binary modes while preserving multi-level stack register values intact. Without dedicated Boolean keys, you harnessed modular integer division via `{{key:÷R}}`—returning quotient in $Y$ and remainder in $X$—alongside word length clipping, modular reduction, and powers-of-two arithmetic to configure microcontroller registers, construct IPv4 CIDR subnet masks, pack and extract RGB color channels, and analyze telemetry bit disparities. Finally, you unified discrete combinatorics ($nPr$, $nCr$, $n!$) and pseudorandom seeding into an essential mathematical toolkit for systems programming and digital electronics.

From discrete bits and memory registers, the principles of accumulation and mathematical modeling extend directly into financial decision-making and quantitative economics. In **Chapter 11: Financial Mathematics & Time Value of Money (TVM)**, you will master the SC-32's dedicated five-variable compound interest solver ($N, I\%YR, PV, PMT, FV$). You will calculate mortgage amortization schedules, evaluate net present value (NPV) and internal rate of return (IRR), and apply actuarial sign discipline to model complex real-world capital flows.

