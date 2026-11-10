---
title: "Unit III: Digital Systems, Bitwise Logic & Embedded Timing"
description: "Multi-base conversions, signed two's complement arithmetic, bitwise masking and shifts, IEEE-754 floating point, CRC-32 checksums, UART baud divisors, and timer prescalers on the SC-16."
---

# Unit III: Digital Systems, Bitwise Logic & Embedded Timing

At a clock speed of one hundred megahertz, light travels barely three meters in a single instruction cycle. On a microchip, time is not an abstract dimension; it is physical distance etched in copper and silicon. In the winter of 1937, George Stibitz assembled two dry-cell batteries, two flashlight bulbs, a pair of telephone relays, and strips of tin cut from a tobacco can on the kitchen table of his Manhattan apartment. When he completed the circuit with a tin strip, the bulb glowed: the "Model K" adder was born, proving that Boolean algebra could execute in physical electronic circuits. In high-level software, computation is presented as an unconstrained world of infinite integers, frictionless floating-point types, and automatic garbage collection. But at the hardware boundary of embedded firmware, digital signal processing, and low-level kernel architecture, raw physical constraints govern every register: fixed word widths, finite propagation delays, and discrete voltage thresholds. Through George Boole's 1854 *An Investigation of the Laws of Thought*, Claude Shannon's 1937 master's thesis *A Symbolic Analysis of Relay and Switching Circuits*, and John von Neumann's 1945 EDVAC architecture, computing hardware established **binary logic**—the physical presence or absence of a voltage potential ($0\text{ V}$ vs. $3.3\text{ V}$)—as the fundamental currency of modern civilization.

Because microprocessors store numbers in fixed-width physical registers of 8, 16, 32, or 64 flip-flops, arithmetic is fundamentally **modular**. Numbers do not stretch endlessly to infinity; they wrap around a finite mathematical ring ($\mathbb{Z} / 2^n \mathbb{Z}$). In signed arithmetic, the **Two's Complement** system maps the upper half of the unsigned integer range into negative values, permitting digital adders to execute subtraction using the exact same silicon logic gates as addition ($A - B = A + (\sim B + 1)$) with zero execution time penalty and zero ambiguity between $+0$ and $-0$. Meanwhile, peripheral control registers expose bare hardware pins directly into memory address space, demanding atomic **bitwise masking** (`&= ~MASK`, `|= MASK`) to toggle safety flags without overwriting neighboring bits.

The catastrophic vulnerability of digital systems when binary word boundaries, endian byte ordering, and clock drift are miscalculated was etched into military history on February 25, 1991, during Operation Desert Storm in Dhahran, Saudi Arabia. An American Patriot missile air-defense battery failed to track and intercept an incoming Iraqi Scud missile, which struck an army barracks, killing twenty-eight soldiers and injuring ninety-eight. The official Government Accountability Office (GAO) investigation revealed that the Patriot's radar tracking computer calculated time by multiplying an integer counter by $0.1$ seconds. But in binary arithmetic, one-tenth ($1/10$) has an infinite repeating expansion:

$$0.1_{10} = 0.0001100110011001100110011..._2$$

The Patriot's 24-bit fixed-point register chopped this fraction at 24 bits, introducing an imperceptible timing error of $0.000000095$ seconds per tick. Over one hundred hours of continuous operation without a system reboot, that tiny fractional truncation accumulated into an absolute clock drift of $\mathbf{0.3433\text{ seconds}}$. At Mach 5 ($1{,}676\text{ m/s}$), the incoming Scud traveled more than **$575\text{ meters}$** during that fractional second. When the Patriot's radar opened its range gate to track the missile, the Scud was over half a kilometer outside the calculation window. The computer discarded the radar return as false clutter, failed to launch an interceptor, and the Scud hit the barracks. The Dhahran disaster stands as the ultimate cautionary monument in computer systems engineering: fixed-width binary arithmetic, floating-point truncation, and timer prescalers are matters of life and death.

Around those silicon microcontrollers, embedded engineers and cyber operators solve coupled low-level hardware, networking, and signal-processing problems across the industrial plant. Firmware engineers reverse endian byte ordering between big-endian network packet streams and little-endian ARM processors using single-cycle `BSWAP` primitives. Systems programmers unpack IEEE-754 floating-point bitfields, evaluate Galois-field cyclic redundancy checks (CRC-32) across noisy serial links, and synthesize ultrasonic pulse-width-modulated (PWM) motor frequencies using 16-bit hardware timer prescalers. Simultaneously, network architects partition Classless Inter-Domain Routing (CIDR) subnets and align direct memory access (DMA) buffers to natural cache-line boundaries.

At the interface between physical power and automated control, digital systems govern modern machinery through discrete logic, serialized telemetry, and network communication. The **SC-16 Digital Systems, Bitwise Logic & Cyber Operations** calculator brings multi-base hexadecimal arithmetic, signed modular rings, bitfield manipulation, and network subnetting directly to the engineer's fingertips. Three diagnostic case studies trace the boundary between embedded software and physical silicon:

In **Chapter 7**, we step into the cleanroom of a precision robotics laboratory to debug a stalled linear actuator, isolating stuck interrupt flags in memory-mapped timer registers, calculating signed two's complement velocities, and executing atomic bitmasking on the RPN stack.

In **Chapter 8**, we connect a protocol analyzer across an RS-485 serial telemetry bus to unpack corrupted sensor frames, reversing network byte order via `BSWAP`, decoding IEEE-754 floating-point temperatures, verifying reflected CRC-32 checksums, and calculating 16-times oversampled UART baud divisors.

In **Chapter 9**, we partition a factory floor industrial Ethernet network and configure mixed-signal sensor nodes, sizing CIDR subnet masks, calculating hardware timer PWM prescalers, determining 12-bit ADC quantization noise, and sizing passive RC anti-aliasing filters.

---

# Chapter 7: The Stuck Interrupt Flag in the Motor Controller

Inside the cleanroom of a precision semiconductor equipment manufacturing facility, laminar airflow hoods hum softly at 0.3 microns. On Test Station 3, an automated wafer-handling robotic arm driven by a high-torque linear actuator freezes midway through a transfer sweep. The robot arm—responsible for moving eight-inch silicon wafers between chemical-vapor deposition chambers—is locked stationary in mid-air. An oscilloscope probe clipped to the gate drive of the pulse-width modulated (PWM) H-bridge inverter shows a constant, unmodulated high voltage; the motor windings are rapidly warming up, and the diagnostic status LED on the ARM Cortex-M4 microcontroller board is latched solid red.

Senior embedded firmware architect Maya Lin and junior firmware developer Alex connect a JTAG in-circuit debugger probe to the controller's debug port. The microcontroller is trapped inside an infinite loop in the default interrupt handler (`HardFault_Handler`). When Alex halts the processor and dumps the hardware peripheral registers, the core register dump reveals a cascade of low-level digital anomalies:
1. The hardware timer status register (`TIM2->SR`) has its interrupt flag locked high at bit 0 (`UIF = 1`), repeatedly re-triggering the timer interrupt service routine (ISR) before the processor can return to user-space code.
2. In the timer control register (`TIM2->CR1`), an engineer attempted to enable center-aligned PWM mode by assigning a raw decimal constant, inadvertently overwriting and clearing the critical auto-reload preload (`ARPE`) and clock division bits.
3. In the motor velocity loop, a signed negative shaft velocity read from the quadrature encoder interface was shifted right using a **logical shift** (`LSR`) instead of an **arithmetic shift** (`ASR`), stripping the sign bit and corrupting a backward velocity of $-3{,}840\text{ counts/s}$ (`0xF100`) into a massive forward runaway command of $+15{,}424\text{ counts/s}$ (`0x3C40`).

To resuscitate the robotic arm and prevent wafer contamination, Maya and Alex turn to the **SC-16 Digital Systems, Bitwise Logic & Cyber Operations** calculator:
1. Unpack positional radix notation across Hexadecimal (`HEX`), Decimal (`DEC`), Octal (`OCT`), and Binary (`BIN`) modes.
2. Master signed modular arithmetic and two's complement additive inversion ($A - B = A + (\sim B + 1)$) across 8-bit, 16-bit, 32-bit, and 64-bit word boundaries.
3. Construct contiguous bitmasks to execute atomic read-modify-write peripheral updates (`&= ~MASK`, `|= MASK`).
4. Correct the signed velocity shift using sign-preserving arithmetic shifts (`ASR`) and fixed-point Q-format scaling.

---

## Silicon Transistor Switches, Two's Complement, and the Dhahran Clock Trap

When moving from the 480-volt electrical switchgear of Unit II into embedded silicon, the governing scale shifts from macro-power to transistor states. A field-effect transistor has no intrinsic knowledge of mathematical signs or fractions; it is a physical switch saturated at $3.3\text{ volts}$ (Boolean `1`) or pulled down to ground at $0.0\text{ volts}$ (Boolean `0`). Every higher-level construct—from two's complement signed arithmetic to cryptographic checksums—is a mathematical abstraction mapped onto arrays of physical switches.

### From Heavy AC Power to 3.3V Silicon Transistor Switches

In Unit II, we explored polyphase alternating current: magnetic induction, rotating phasors, power triangles, and high-voltage feeder cables.

In Unit III, we cross the threshold into **digital electronics**. The physical principles do not vanish; they scale down into microscopic sub-micron silicon geometries:
- A $480\text{-volt}$ motor feeder carrying $145\text{ A}$ through rigid steel conduit becomes a $3.3\text{-volt}$ metal trace carrying microamperes on a printed circuit board.
- The 60-hertz grid frequency gives way to high-frequency quartz crystal oscillators vibrating at $168\text{ MHz}$ ($168{,}000{,}000\text{ cycles per second}$).
- The continuous sinusoidal voltages of Steinmetz are replaced by discrete square pulses switching in hundreds of picoseconds.

Inside the ARM Cortex-M4 microcontroller, over ten million complementary metal-oxide-semiconductor (CMOS) field-effect transistors switch on and off. Each transistor stores or transfers a single bit of information: charge trapped on a capacitive gate oxide. In modern 3.3V CMOS logic, these logic levels are defined by strict physical voltage thresholds:
- $V_{\text{IL}}$ (Input Low Maximum): Typically $0.3 \times V_{\text{DD}} \approx 0.99\text{ V}$. Any input voltage below this threshold is reliably detected as Boolean `0`.
- $V_{\text{IH}}$ (Input High Minimum): Typically $0.7 \times V_{\text{DD}} \approx 2.31\text{ V}$. Any input voltage above this threshold is reliably detected as Boolean `1`.
- $V_{\text{OL}}$ (Output Low Maximum): Typically $0.4\text{ V}$. Guaranteed maximum output voltage when asserting logic `0`.
- $V_{\text{OH}}$ (Output High Minimum): Typically $V_{\text{DD}} - 0.4\text{ V} \approx 2.9\text{ V}$. Guaranteed minimum output voltage when asserting logic `1`.

The difference between $V_{\text{IL}}$ and $V_{\text{OL}}$ ($0.99\text{ V} - 0.40\text{ V} = 0.59\text{ V}$) represents the low-state noise margin ($NM_{\text{L}}$), while the difference between $V_{\text{OH}}$ and $V_{\text{IH}}$ ($2.90\text{ V} - 2.31\text{ V} = 0.59\text{ V}$) represents the high-state noise margin ($NM_{\text{H}}$). Within these noise margins, physical transistors operate deterministically despite thermal fluctuations and power rail ripple.

Because physical registers are built from finite arrays of silicon flip-flops (8 bits in a `uint8_t`, 16 bits in a half-word, 32 bits in a standard ARM word, 64 bits in a quad-word), arithmetic in digital hardware is fundamentally **modular**. Numbers do not stretch endlessly to infinity; they wrap around a finite integer ring ($\mathbb{Z} / 2^N \mathbb{Z}$).

### Why Two's Complement Won: Zero Logic Gate Overhead and the Elimination of Minus Zero

In the dawn of modern digital computing during the 1940s and 1950s, computer architects experimented with multiple methods to represent signed negative numbers in binary:

1. **Sign-and-Magnitude**: The most significant bit (MSB) serves as a sign flag ($0 = \text{positive}, 1 = \text{negative}$), while the remaining $N-1$ bits store the absolute magnitude of the number.
   - For an 8-bit byte:
     $$+5_{10} = \text{00000101}_2 = \text{0x05}$$
     $$-5_{10} = \text{10000101}_2 = \text{0x85}$$
2. **One's Complement (Diminished Radix Complement)**: Negative numbers are generated by flipping every bit in the positive binary representation (bitwise NOT):
   - For an 8-bit byte:
     $$+5_{10} = \text{00000101}_2 = \text{0x05}$$
     $$-5_{10} = \sim(\text{00000101}_2) = \text{11111010}_2 = \text{0xFA}$$

Why did both Sign-and-Magnitude and One's Complement fail, disappearing from modern microprocessor architectures?

Because both systems contain two catastrophic hardware and software flaws:

First, **The Dual-Zero Ambiguity Bug ($+0$ vs. $-0$)**:
In Sign-and-Magnitude, there are two distinct physical bit patterns for zero:
- Positive Zero: $\text{00000000}_2 = \text{0x00} = +0$
- Negative Zero: $\text{10000000}_2 = \text{0x80} = -0$

In One's Complement, there are likewise two zeros:
- Positive Zero: $\text{00000000}_2 = \text{0x00} = +0$
- Negative Zero: $\text{11111111}_2 = \text{0xFF} = -0$

Having two representations of zero creates severe hazards in real-time control. A conditional branch like `if (velocity == 0)` fails if the compiler tests only for `0x00` while an arithmetic operation produces `0x80` or `0xFF`. Testing for zero requires multiple logic gates and extra clock cycles, introducing race conditions in interrupt service routines.

Second, **The Requirement for Dual Silicon Adders and Subtractors**:
In Sign-and-Magnitude, you cannot add a positive number and a negative number using a standard binary adder. The CPU must first compare the magnitudes of both numbers, determine which one is larger, subtract the smaller magnitude from the larger magnitude using a dedicated subtractor circuit, and conditionally assign the sign bit. This required massive amounts of redundant silicon circuitry and introduced severe propagation delays.

The solution that triumphed across all modern computer architectures was **Two's Complement**, formalized by John von Neumann and early computer pioneers.

In Two's Complement, the negative of an integer $X$ is defined as its **additive inverse** in the modular ring $\mathbb{Z} / 2^N \mathbb{Z}$:

$$X^* = 2^N - X = \left((2^N - 1) - X\right) + 1 = \sim X + 1$$

To negate a number in two's complement, you simply:
1. Invert all bits (bitwise NOT, $\sim X$).
2. Add one ($+1$).

Analyze the practical consequences of this definition:

1. **Zero Silicon Overhead Between Addition and Subtraction**:
   Subtracting $B$ from $A$ is mathematically identical to adding the two's complement of $B$:
   $$A - B = A + (\sim B + 1)$$
   The central processing unit requires no dedicated subtraction hardware. The exact same binary adder circuit (ripple-carry or carry-lookahead adder) that adds two positive numbers executes subtraction with zero silicon overhead. The CPU simply inverts the $B$ input bits through XOR gates and asserts the adder's carry-in bit ($C_{\text{in}} = 1$).
2. **Exactly One Zero**:
   In two's complement, negating zero yields:
   $$\sim(\text{00000000}_2) + 1 = \text{11111111}_2 + 1 = \text{100000000}_2$$
   The 9th bit overflows and is discarded by the 8-bit register, leaving only $\text{00000000}_2$. There is no negative zero; zero is unique, unambiguous, and testable with a single NOR gate.
3. **Asymmetric Range**:
   Because zero uses one of the positive bit patterns (starting with MSB = $0$), an $N$-bit two's complement integer has an asymmetric range:
   $$\left[-2^{N-1}, \; 2^{N-1} - 1\right]$$
   - 8-bit (`BYTE`): $[-128, \; +127]$
   - 16-bit (`WORD`): $[-32{,}768, \; +32{,}767]$
   - 32-bit (`DWORD`): $[-2{,}147{,}483{,}648, \; +2{,}147{,}483{,}647]$
   - 64-bit (`QWORD`): $[-9{,}223{,}372{,}036{,}854{,}775{,}808, \; +9{,}223{,}372{,}036{,}854{,}775{,}807]$

The most negative number (such as $-128$ in 8-bit mode, `0x80`) has no positive counterpart. Attempting to negate $-128$ produces:
$$\sim(\text{10000000}_2) + 1 = \text{01111111}_2 + 1 = \text{10000000}_2 = -128$$
It overflows back to itself. This asymmetry is a mathematical property of modular rings that every systems programmer must account for.

### The Dhahran Patriot Missile Failure: Binary Truncation in Real-Time Systems

Consider the decimal number $0.1$ ($1/10$) represented in base 2. In base 10, $0.1$ is a single-digit terminating fraction. But converting $1/10$ to base 2 reveals an infinite repeating expansion:
- $0.1 \times 2 = 0.2 \to 0$
- $0.2 \times 2 = 0.4 \to 0$
- $0.4 \times 2 = 0.8 \to 0$
- $0.8 \times 2 = 1.6 \to 1$
- $0.6 \times 2 = 1.2 \to 1$
- $0.2 \times 2 = 0.4 \to 0$ (the sequence repeats indefinitely).

In binary, $0.1_{10}$ is an **infinite repeating fraction**:

$$0.1_{10} = 0.00011001100110011001100110011..._2$$

Just as $1/3 = 0.333333...$ cannot be represented with a terminating decimal fraction, $1/10$ cannot be represented with a terminating binary fraction.

This mathematical reality triggered a well-documented military software failure on February 25, 1991, during Operation Desert Storm in Dhahran, Saudi Arabia. An American Patriot missile air-defense battery failed to track and intercept an incoming Iraqi Scud missile, which struck an army barracks.

The Patriot radar tracking computer measured system time by incrementing an integer counter by one every tenth of a second ($0.1\text{ s}$). To calculate time in seconds for radar velocity tracking, the software multiplied this integer count by a fixed-point binary representation of $1/10$.

The Patriot used a 24-bit fixed-point register. Truncating the infinite binary expansion of $1/10$ at 24 bits resulted in:

$$0.1_{10} \approx 0.00011001100110011001100_2 = \frac{1{,}677{,}721}{16{,}777{,}216} \approx 0.099999904632568359375\text{ s}$$

The error per tick was small:

$$\Delta t_{\text{tick}} = 0.1 - 0.099999904632568359375 \approx 0.000000095367\text{ seconds}$$

This error is less than one ten-millionth of a second per tick. In a system intended to run for a few hours before rebooting, this drift was negligible. But at Dhahran, the battery had been running continuously for **100 hours**:

$$\text{Total Ticks} = 100\text{ hours} \times 3{,}600\text{ s/hr} \times 10\text{ ticks/s} = 3{,}600{,}000\text{ ticks}$$

Multiplying the total ticks by the tiny 24-bit truncation error:

$$\Delta t_{\text{total}} = 3{,}600{,}000 \times 0.000000095367\text{ s} \approx \mathbf{0.3433\text{ seconds}}$$

This accumulated into a timing drift of over a third of a second. When an incoming Al-Hussein Scud missile approached at Mach 5 ($v \approx 1{,}676\text{ m/s}$), the Patriot radar predicted where the missile should be by searching a spatial range gate. Due to the $0.3433\text{ s}$ clock drift, the radar searched a volume of sky displaced by:

$$\Delta x = v \times \Delta t_{\text{total}} = 1{,}676\text{ m/s} \times 0.3433\text{ s} \approx \mathbf{575.43\text{ meters}}$$

The Scud was more than half a kilometer away from the predicted range gate. The radar declared the target a false track, dropped lock, and never launched an interceptor. The Dhahran failure stands as an enduring lesson in computer systems engineering: fixed-width binary arithmetic, floating-point truncation, and timer prescalers are matters of life and death.

### Memory-Mapped I/O and Peripheral Register Assignment

In ARM Cortex-M microcontrollers, peripherals (timers, UARTs, SPI, GPIO) do not use dedicated I/O instructions; they use **Memory-Mapped Input/Output (MMIO)**. Every hardware control register is mapped to a physical 32-bit address on the peripheral bus:
- `TIM2->CR1` (Timer 2 Control Register 1) resides at address `0x40000000`.
- `TIM2->SR` (Timer 2 Status Register) resides at address `0x40000010`.

Consider an attempt to configure center-aligned PWM mode via raw assignment:
```c
TIM2->CR1 = 0x0020; // Attempting to set CMS bits [6:5]
```

Raw assignment (`=`) overwrites every bit in the 32-bit register. By writing `0x0020`, software sets bit 5, but simultaneously clears bits 0, 7, 8, and 9 to zero. Clearing bit 0 halts the timer counter; clearing bit 7 disables the preload buffer, causing motor PWM duty cycles to glitch; and clearing bits 8-9 alters the dead-time clock prescaler, causing both the high-side and low-side MOSFETs in the H-bridge inverter to turn on simultaneously—a dead short across the DC bus known as **shoot-through**.

Furthermore, on high-performance microcontrollers equipped with an Advanced High-Performance Bus (AHB) and Advanced Peripheral Bus (APB), peripheral writes are buffered. If software writes to a register and immediately proceeds without verifying bus completion, pipeline latency can cause subsequent instructions to execute before the hardware state has settled. In critical sections, systems programmers insert memory barriers (`__DSB()`, Data Synchronization Barrier) and declare register pointers as `volatile` to prevent the C compiler from optimizing out repeated register reads or reordering bus transactions.

To safely manipulate peripheral registers, an embedded engineer must use **Bitwise Boolean Masking**:
1. **Setting Bits (Atomic OR)**:
   ```c
   TIM2->CR1 |= (1 << 0); // Sets CEN (bit 0) without modifying any other bit
   ```
2. **Clearing Bits (Atomic Inverted AND)**:
   ```c
   TIM2->CR1 &= ~(1 << 0); // Clears CEN (bit 0) while leaving all other bits intact
   ```
3. **Modifying Multi-Bit Fields (Read-Modify-Write)**:
   To update a multi-bit field (such as bits 6:5), you must first clear the field using the inverted mask, and then OR in the new value:
   ```c
   #define CMS_MASK (0x3 << 5) // Bits [6:5] mask = 0x0060
   TIM2->CR1 = (TIM2->CR1 & ~CMS_MASK) | (0x1 << 5); // Clears [6:5] then sets to 01
   ```
4. **Write-1-to-Clear (W1C) Status Registers**:
   In many peripherals, status flags (like `UIF`, bit 0 of `TIM2->SR`) are cleared by writing a `0` or a `1` depending on the silicon architecture. In standard STM32/ARM timers, writing `0` to a status bit clears it, while writing `1` has no effect:
   ```c
   TIM2->SR = ~(1 << 0); // Writes 0 to bit 0, preserving other pending hardware flags
   ```
   Executing `TIM2->SR = 0;` clears capture-compare interrupt flags that occurred simultaneously, dropping encoder counts.

### Hardware Memory-Mapped Bit-Banding in ARM Cortex-M Architectures

Even a standard read-modify-write operation (`TIM2->CR1 |= MASK`) has a subtle flaw in preemptive real-time systems: it is **not atomic** at the machine-code level.

When the CPU executes `TIM2->CR1 |= (1 << 0);`, the compiler generates three distinct assembly instructions:
```assembly
LDR  R0, =0x40000000   ; Load register address
LDR  R1, [R0]          ; Read: fetch current 32-bit register value into R1
ORR  R1, R1, #0x01     ; Modify: set bit 0
STR  R1, [R0]          ; Write: store updated 32-bit value back to peripheral
```

Suppose a high-priority hardware interrupt fires between the `LDR` and the `STR`. The interrupt service routine modifies bit 4 of `TIM2->CR1` and returns. When the interrupted main thread resumes, its stale value in `R1` is written back via `STR`, overwriting the change made by the ISR. This is the classic read-modify-write race condition in multi-threaded firmware.

To solve this without the severe execution penalty of disabling global interrupts (`__disable_irq()`), ARM Cortex-M3 and Cortex-M4 processors implement an ingenious hardware feature: **Bit-Banding**.

Bit-banding maps individual bits within memory-mapped peripheral and SRAM regions into an entirely separate, expanded 32-megabyte address space known as the **bit-band alias region**:
1. **Peripheral Bit-Band Region**: Physical addresses `0x40000000` through `0x400FFFFF` ($1\text{ MB}$) map to alias addresses `0x42000000` through `0x43FFFFFF` ($32\text{ MB}$).
2. **SRAM Bit-Band Region**: Physical addresses `0x20000000` through `0x200FFFFF` ($1\text{ MB}$) map to alias addresses `0x22000000` through `0x23FFFFFF` ($32\text{ MB}$).

In this alias region, every single bit of the original memory space is assigned its own dedicated 32-bit word address. When the CPU writes a `1` or `0` to an alias word address, the internal bus matrix hardware automatically performs an atomic read-modify-write transaction directly on the target peripheral register in a single cycle.

The mathematical formula to compute the 32-bit alias word address from a byte address and bit number is:

$$\text{Bit\_Band\_Address} = \text{Alias\_Base} + (\text{Byte\_Offset} \times 32) + (\text{Bit\_Number} \times 4)$$

Where:
- $\text{Alias\_Base}$ is `0x42000000` for peripherals or `0x22000000` for SRAM.
- $\text{Byte\_Offset}$ is the byte distance from the start of the bit-band region ($\text{Target\_Address} - \text{Base\_Address}$).
- $\text{Bit\_Number}$ is the target bit position ($0 \le \text{Bit\_Number} \le 7$ within that byte, or $0 \le \text{Bit\_Number} \le 31$ within a 32-bit word).

Consider clearing bit 0 of the Timer 2 Status Register (`TIM2->SR`) located at physical address `0x40000010`.
1. Peripheral base is `0x40000000`, so $\text{Byte\_Offset} = \text{0x40000010} - \text{0x40000000} = \text{0x10} = 16_{10}$.
2. Bit number is $0$.
3. Evaluating the alias formula:
   $$\text{Bit\_Band\_Address} = \text{0x42000000} + (16 \times 32) + (0 \times 4) = \text{0x42000000} + 512 + 0 = \text{0x42000200}$$

By simply executing a single store instruction:
```c
*((volatile uint32_t *)0x42000200) = 0;
```
The processor clears bit 0 of `TIM2->SR` with hardware atomicity. No interrupts can preempt it, no temporary registers are corrupted, and zero race conditions can occur.

---

## Positional Radix Compression and Fixed-Width Two's Complement Rings

The SC-16 provides dedicated hardware modes for four positional number bases: Hexadecimal (base 16), Decimal (base 10), Octal (base 8), and Binary (base 2).

### Binary Nibbles, Octal Triads, and Hexadecimal Register Notation

In any positional number system of radix $b$, a number is represented by a sequence of digits $(d_{n-1} d_{n-2} \dots d_1 d_0)_b$ whose magnitude evaluates the polynomial expansion:

**Eq. 7.1 — Positional Number Base Radix Expansion**
$$V = \sum_{i=0}^{n-1} d_i \cdot b^i = d_{n-1} b^{n-1} + d_{n-2} b^{n-2} + \dots + d_1 b^1 + d_0 b^0$$

Where each digit is bounded by $0 \le d_i < b$.

Why do engineers switch between bases?
1. **Binary ($b = 2$, digits $0, 1$)**: Direct reflection of physical CMOS voltage levels. Every digit is one bit. However, a 32-bit register requires 32 digits, making human visual inspection exhausting and error-prone.
2. **Octal ($b = 8$, digits $0\text{–}7$)**: Groups bits into groups of 3 ($2^3 = 8$), known as triads. Historically dominant in 12-bit, 18-bit, and 36-bit minicomputer architectures such as the PDP-8 and PDP-11, where instruction opcodes were partitioned into 3-bit fields. Octal is still used in Unix file system permissions (`chmod 755`). However, because 8 bits, 16 bits, and 32 bits do not divide evenly by 3, octal produces awkward split boundaries in modern byte-oriented architectures.
3. **Hexadecimal ($b = 16$, digits $0\text{–}9, \text{A–F}$)**: The universal language of embedded systems. Because $2^4 = 16$, exactly four binary bits compress into a single hexadecimal digit (a **nibble**).
   - An 8-bit byte is exactly 2 hex digits (`0x00` to `0xFF`).
   - A 16-bit word is exactly 4 hex digits (`0x0000` to `0xFFFF`).
   - A 32-bit double-word is exactly 8 hex digits (`0x00000000` to `0xFFFFFFFF`).
   - A 64-bit quad-word is exactly 16 hex digits.

Hexadecimal aligns perfectly with byte boundaries. Converting between binary and hexadecimal requires zero arithmetic calculation; it is pure visual pattern matching:
- `0x42964000`:
- `4` = `0100`
- `2` = `0010`
- `9` = `1001`
- `6` = `0110`
- `4` = `0100`
- `0` = `0000`
- `0` = `0000`
- `0` = `0000`

Summing powers of two evaluates the decimal equivalent: $V = 1{,}117{,}143{,}040_{10}$.

### Modular Integer Rings, Two's Complement Negation, and Signed Overflow

In an $N$-bit processor register, arithmetic operations occur within the finite ring of integers modulo $2^N$ ($\mathbb{Z} / 2^N \mathbb{Z}$).

When a positive number exceeds the maximum representable integer, it does not stop; it wraps around to zero (in unsigned arithmetic) or wraps into negative values (in signed two's complement arithmetic).

The two's complement additive inverse equation is:

**Eq. 7.2 — Two's Complement Additive Inversion**
$$X^* = 2^N - X = \sim X + 1$$

Where $\sim X$ is the bitwise NOT operation (inverting all $N$ bits), and $+1$ completes the additive inverse in modulo $2^N$.

```
       Unsigned Byte (0 to 255)                  Signed Byte (-128 to +127)
               0x00 (0)                                  0x00 (0)
        0xFF              0x01                    0xFF              0x01
        (255)              (1)                    (-1)              (+1)
    0xFE                      0x02            0xFE                      0x02
    (254)                      (2)            (-2)                      (+2)
   0x80                        0x7F          0x80                        0x7F
   (128)                      (127)         (-128)                      (+127)
```

Look at the boundary at `0x7F` ($+127$) transitioning to `0x80`:
- In unsigned arithmetic, `0x7F + 1 = 0x80` ($127 + 1 = 128$).
- In signed arithmetic, `0x7F + 1 = 0x80` ($+127 + 1 = \mathbf{-128}$).

This sudden sign inversion is **Signed Integer Overflow**.

### The Silicon Arithmetic Logic Unit: Carry ($C$), Overflow ($V$), and Condition Codes

To detect arithmetic boundaries, every microprocessor ALU sets condition flags inside the status register (e.g., `APSR` in ARM, `EFLAGS` in x86):
1. **Zero Flag ($Z$)**: Set to $1$ if the result of an operation is exactly zero; $0$ otherwise.
2. **Negative Flag ($N$ or $S$)**: Matches the most significant bit (MSB) of the result ($1$ if negative, $0$ if positive).
3. **Carry Flag ($C$)**: Set when an **unsigned** addition produces a carry out of the MSB ($> 2^N - 1$), or when an unsigned subtraction requires a borrow. (Note: in ARM processors, $C=1$ on subtraction indicates "no borrow", whereas in x86 $C=1$ indicates "borrow").
4. **Overflow Flag ($V$)**: Set when a **signed** operation produces a result that exceeds the representable signed range $\left[-2^{N-1}, 2^{N-1}-1\right]$.

In physical silicon, the Overflow Flag is generated by a simple, elegant logic gate: the exclusive-OR of the carry into the MSB ($C_{\text{in}}$) and the carry out of the MSB ($C_{\text{out}}$):

$$V = C_{\text{in}} \oplus C_{\text{out}}$$

Equivalently, signed overflow occurs if and only if two positive numbers yield a negative sum, or two negative numbers yield a positive sum:

$$V = (A_{\text{MSB}} \land B_{\text{MSB}} \land \overline{R_{\text{MSB}}}) \lor (\overline{A_{\text{MSB}}} \land \overline{B_{\text{MSB}}} \land R_{\text{MSB}})$$

For an 8-bit signed byte, adding $+120$ (`0x78`) and $+15$ (`0x0F`) yields $+135$, which exceeds $+127$. The bit result is `0x87`, which interprets in two's complement as **$-121$**. The positive sum overflowed into a negative representation, asserting the processor's Overflow Flag ($V = 1$).

This distinction between $C$ and $V$ dictates how processors evaluate conditional branch instructions:

| Comparison Instruction | Evaluated Flags | Condition Name | Arithmetic Domain |
| :--- | :--- | :--- | :--- |
| **`BEQ`** (Branch Equal) | $Z = 1$ | Equal | Both Signed and Unsigned |
| **`BNE`** (Branch Not Equal) | $Z = 0$ | Not Equal | Both Signed and Unsigned |
| **`BHI`** (Branch Higher) | $C = 1 \land Z = 0$ | Greater Than | Unsigned |
| **`BLS`** (Branch Lower or Same) | $C = 0 \lor Z = 1$ | Less Than or Equal | Unsigned |
| **`BGT`** (Branch Greater Than) | $Z = 0 \land (N = V)$ | Greater Than | Signed |
| **`BLT`** (Branch Less Than) | $N \ne V$ | Less Than | Signed |
| **`BGE`** (Branch Greater or Equal) | $N = V$ | Greater Than or Equal | Signed |
| **`BLE`** (Branch Less or Equal) | $Z = 1 \lor (N \ne V)$ | Less Than or Equal | Signed |

If a developer compiles a boundary check with unsigned types (`unsigned int len`), the compiler emits unsigned comparisons (`BHI`/`BLS`). If the developer compares signed variables with unsigned bounds, catastrophic cyber vulnerabilities occur (such as the classic negative-index heap overwrite, where $-1$ treated as unsigned evaluates to $4{,}294{,}967{,}295$, bypassing length limits).

### Sign Extension Across Register Boundaries: CBW, SXTB, and MOVSX

When a microprocessor loads an 8-bit or 16-bit signed integer into a 32-bit or 64-bit general-purpose register, how does it preserve its mathematical value?

Suppose an 8-bit temperature reading is $-5_{10}$, stored in memory as byte `0xFB` (`11111011_2`).
If the CPU loads this byte into a 32-bit register without sign extension (zero-extension, `MOVZX` in x86):
$$\text{Register} = \text{0x000000FB} = +251_{10}$$
The temperature reading wraps from $-5^\circ\text{C}$ to $+251^\circ\text{C}$, corrupting downstream process control.

To preserve the negative signed value, the processor must perform **Sign Extension**: it replicates the most significant bit of the smaller type across all upper bit positions of the larger register:
- Positive number (`0x05`, MSB = 0) $\to$ `0x00000005` (+5).
- Negative number (`0xFB`, MSB = 1) $\to$ `0xFFFFFFFB` (-5).

Modern assembly architectures provide dedicated instructions for this operation:
- x86: `CBW` (Convert Byte to Word), `CWDE` (Convert Word to Doubleword Extended), `CDQ` (Convert Doubleword to Quadword), and `MOVSX` (Move with Sign Extension).
- ARM: `SXTB` (Signed Extend Byte), `SXTH` (Signed Extend Halfword), and `SBFX` (Signed Bit Field Extract).

On the SC-16 calculator, changing the active word size with `{{key:WSZ}}` while in signed mode automatically enforces correct sign extension and truncation rules, allowing engineers to audit register widening bugs directly on the stack.

---

## Bitwise Boolean Masking, Shifts, and Fixed/Floating-Point Encoding

### Boolean Logic Gates and Peripheral Control Register Masking

Silicon microcontrollers do not modify physical pins directly; they modify bits inside peripheral registers. The fundamental Boolean logic operations are:

1. **Bitwise AND (`&`, `{{key:&}}`)**: Output is $1$ if and only if both inputs are $1$. Used to **mask** and isolate specific bits, clearing all others to $0$.
   - $X \ \& \ 1 = X$ (preserves bit)
   - $X \ \& \ 0 = 0$ (forces bit to zero)
2. **Bitwise OR (`|`, `{{key:|}}`)**: Output is $1$ if either input is $1$. Used to **set** specific bits without disturbing adjacent bits.
   - $X \mid 0 = X$ (preserves bit)
   - $X \mid 1 = 1$ (forces bit to one)
3. **Bitwise XOR (`^`, `{{key:⊕}}`)**: Output is $1$ if inputs are different; $0$ if identical. Used to **toggle/invert** bits and calculate parity.
   - $X \oplus 0 = X$ (preserves bit)
   - $X \oplus 1 = \sim X$ (toggles bit)
   - $X \oplus X = 0$ (clears register to zero in a single cycle)
4. **Bitwise NOT (`~`, `{{key:~}}`)**: Inverts every bit (one's complement).

To manipulate a specific bitfield of width $W$ starting at bit position $P$, we generate a contiguous bitmask:

**Eq. 7.3 — Contiguous Bitfield Mask Generation**
$$\text{Mask} = (2^W - 1) \ll P$$

Where $W$ is the field bit-width, $P$ is the starting bit position (offset), and $\ll$ is the logical shift-left operator.

For example, to isolate or update a 4-bit configuration field ($W = 4$) at bit position $P = 8$ (bits [11:8]):
$$\text{Mask} = (2^4 - 1) \ll 8 = (16 - 1) \ll 8 = 15 \ll 8 = \text{0x0F} \ll 8 = \mathbf{\text{0x0F00}}$$

To update bits [11:8] in register `REG` containing `0xA528` to new value `0x5` (`0x0500`):
1. Clear the field: `REG & ~0x0F00 = 0xA528 & 0xF0FF = 0xA028`.
2. OR in the new value: `0xA028 | 0x0500 = 0xA528`.

In modern ARM Cortex microcontrollers, dedicated bitfield instructions accelerate these operations:
- `UBFX Rd, Rn, #lsb, #width` (Unsigned Bit Field Extract): Extracts $W$ bits starting at position $P$ into register `Rd`, zero-extending the result.
- `SBFX Rd, Rn, #lsb, #width` (Signed Bit Field Extract): Extracts $W$ bits and sign-extends the highest extracted bit across the destination register.
- `BFI Rd, Rn, #lsb, #width` (Bit Field Insert): Copies $W$ bits from the low-order bits of `Rn` into `Rd` starting at position $P$, leaving all other bits of `Rd` intact.

### Logical Shifts, Sign-Preserving Arithmetic Shifts, Rotations, and Fixed-Point Scaling

Bit shifts move all bits inside a register to the left or right by $k$ positions:

1. **Logical Shift Left (`LSL`, `<<`, `{{key:≪}}`)**:
   Shifts bits left, discarding bits that fall off the MSB, and shifting in zeros (`0`) at the LSB.
   - Mathematically equivalent to multiplying by $2^k$:
     $$X \ll k = X \cdot 2^k \pmod{2^N}$$
2. **Logical Shift Right (`LSR`, `>>`, `{{key:≫}}`)**:
   Shifts bits right, discarding bits that fall off the LSB, and shifting in zeros (`0`) at the MSB.
   - Correct for **unsigned** integer division by $2^k$:
     $$X \gg_{\text{logical}} k = \lfloor X / 2^k \rfloor$$
3. **Arithmetic Shift Right (`ASR`, `>>`, `{{key:ASR}}`)**:
   Shifts bits right, discarding bits that fall off the LSB, but **replicates the sign bit (MSB)** into the vacated high-order bit positions.
   - Mandatory for **signed** two's complement division by $2^k$:
     $$X \gg_{\text{arithmetic}} k = \lfloor X / 2^k \rfloor$$
4. **Rotate Right (`ROR`, `{{key:ROR}}`) and Rotate Left (`ROL`, `{{key:ROR}}`)**:
   Circular shifts where bits shifted out of one end wrap around and enter the opposite end. Zero bits are lost. Essential in cryptographic hashing algorithms (MD5, SHA-256) to achieve the avalanche effect.

### Fixed-Point Q-Format Arithmetic Architectures

In resource-constrained microcontrollers lacking a floating-point unit (FPU), or in ultra-low-latency motor control loops where FPU cycles are too slow, engineers use **Fixed-Point Arithmetic**.

In Q-format notation, a signed $N$-bit integer is partitioned into:
- $1$ sign bit (implicitly part of the integer bits).
- $M$ integer bits.
- $F$ fractional bits, where $M + F = N - 1$ (or $N$ total bits).
- Notation: **$\text{Q}M.F$** or simply **$\text{Q}F$** when total word size $N$ is known.

Common industrial Q formats:
- **Q16.16** (32-bit word): 1 sign bit, 15 integer bits, 16 fractional bits.
  - Range: $[-32{,}768.0, \; +32{,}767.9999847]$
  - Resolution: $\epsilon = 2^{-16} = \frac{1}{65{,}536} \approx 0.0000152588$
- **Q8.8** (16-bit word): 1 sign bit, 7 integer bits, 8 fractional bits.
  - Range: $[-128.0, \; +127.99609375]$
  - Resolution: $\epsilon = 2^{-8} = \frac{1}{256} \approx 0.00390625$
- **Q1.15** or **Q15** (16-bit DSP format): 1 sign bit, 0 integer bits, 15 fractional bits. Widely used for normalized audio waveforms in $[-1.0, +0.999969]$.

To convert a real number $V_{\text{real}}$ into fixed-point integer representation $X_{\text{fixed}}$:
$$X_{\text{fixed}} = \text{round}(V_{\text{real}} \times 2^F)$$

To convert back to real floating-point:
$$V_{\text{real}} = \frac{X_{\text{fixed}}}{2^F}$$

Fixed-point arithmetic rules:
1. **Addition and Subtraction**: Direct integer operations, provided both operands share the exact same Q format:
   $$Z_{\text{fixed}} = X_{\text{fixed}} \pm Y_{\text{fixed}}$$
2. **Multiplication**: Multiplying two Q$M.F$ numbers produces an intermediate product with $2F$ fractional bits:
   $$P_{\text{raw}} = X_{\text{fixed}} \times Y_{\text{fixed}} \implies Z_{\text{fixed}} = (X_{\text{fixed}} \times Y_{\text{fixed}}) \gg F$$
   To prevent intermediate overflow, 32-bit Q16.16 multiplication must store the product in a 64-bit integer before shifting right by 16 bits.
3. **Division**: Dividing two Q$M.F$ numbers drops the fractional scaling:
   $$Z_{\text{fixed}} = \frac{X_{\text{fixed}} \ll F}{Y_{\text{fixed}}}$$
   The dividend must be pre-shifted left by $F$ bits (using a wider 64-bit integer) prior to division to retain precision.

---

## Debugging the Motor Controller Register and Velocity Shift on the Stack

On the SC-16 calculator, multi-base logic, word-size boundaries, and signed arithmetic are first-class primitives.

| Button | Operation | Register Z | Register Y | Register X | Governing Expression |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`{{key:HEX}}`** / **`{{key:DEC}}`** / **`{{key:BIN}}`** / **`{{key:OCT}}`** | Radix Base Selection | — | — | Active Number | Sets active entry/display radix; updates LCD banner |
| **`{{key:WSZ}}`** | Register Word Size Toggle | — | — | Active Word | Cycles 8-bit (`B`), 16-bit (`W`), 32-bit (`DW`), 64-bit (`QW`) |
| **`{{key:~}}`** / **`{{key:NEG}}`** | One's / Two's Complement Negation | — | — | Word $X$ | `NOT`: $\sim X$; `NEG`: $\sim X + 1$ (two's complement) |
| **`{{key:&}}`** / **`{{key:|}}`** / **`{{key:⊕}}`** | Bitwise Boolean Logic | — | Word $Y$ | Word $X$ | $Y \ \& \ X,\; Y \mid X,\; Y \oplus X$ |
| **`{{key:≪}}`** / **`{{key:≫}}`** | Logical Shift Left / Right | — | Word $Y$ | Shift count $k$ | $Y \ll k,\; Y \gg k$ (zero-fill) |
| **`{{key:ASR}}`** | Arithmetic Shift Right | — | Word $Y$ | Shift count $k$ | $Y \gg k$ (sign-extended) |
| **`{{key:MSK}}`** | Contiguous Bitmask Generator | — | Field width $W$ | Start bit $P$ | $(2^W - 1) \ll P$ (evaluates Eq. 7.3) |

### Masking and Merging the Timer Control Field in Hexadecimal

To configure the 4-bit clock divider at bits `[11:8]` ($s = 8, w = 4$) with `0xA` ($10_{10}$, entered via softkey {{keycap:A}}) on a control register holding `0x0005`, the engineer switches to {{key:HEX}}, generates `8` {{key:ENTER}} `4` {{key:MSK}} ($\mathbf{\text{0xF00}}$), shifts {{keycap:A}} left by $8$ bits via {{keycap:A}} {{key:ENTER}} `8` {{key:≪}} ($\mathbf{\text{0xA00}}$), and merges with `5` via {{key:&#124;}} to obtain $\mathbf{\text{0xA05}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| {{key:HEX}} `8` {{key:ENTER}} `4` {{key:MSK}} | $0$ | $0$ | $0$ | $\text{0xF00}$ | Generate 4-bit mask at bit offset $8$ ($\text{MSK}(8,4) = \text{0x0F00}$) |
| `5` {{key:ENTER}} | $0$ | $\text{0xF00}$ | $\text{0x5}$ | $\text{0x5}$ | Stage initial control register value `0x0005` |
| {{keycap:A}} {{key:ENTER}} `8` {{key:≪}} | $\text{0xF00}$ | $\text{0xF00}$ | $\text{0x5}$ | $\text{0xA00}$ | Shift hex digit {{keycap:A}} left by $8$ bits to `0x0A00` |
| {{key:&#124;}} | $\text{0xF00}$ | $\text{0xF00}$ | $\text{0xF00}$ | **$\text{0xA05}$** | Merge shifted field into register ($\text{0x0005} \lor \text{0x0A00} = \text{0x0A05}$) |

### Fixing the Signed Velocity Right Shift in Sixteen-Bit Mode

Next, setting the word width to 16 bits ({{key:HEX}} `10` {{key:WSZ}}, since `0x10` $= 16_{10}$) and negating `+16` (`0x10`) with {{key:NEG}} produces `0xFFF0` ($-16$). Executing `2` {{key:ASR}} preserves the sign bit to give $\mathbf{\text{0xFFFC}}$ ($-4$), whereas `2` {{key:≫}} reproduces the runaway positive value $\mathbf{\text{0x3FFC}}$ ($+16{,}380$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| {{key:HEX}} `10` {{key:WSZ}} | $0$ | $0$ | $0$ | $\text{0x10}$ | Set active word width to $16$ bits (`0x10` $= 16_{10}$) |
| `10` {{key:NEG}} | $0$ | $0$ | $\text{0x10}$ | $\text{0xFFF0}$ | Negate `0x0010` ($+16$) to 16-bit two's complement `0xFFF0` ($-16$) |
| {{key:ENTER}} `2` {{key:ASR}} | $0$ | $0$ | $\text{0x10}$ | $\text{0xFFFC}$ | Arithmetic right shift by $2$ bits preserves sign (`0xFFFC` $= -4$) |
| {{keycap:F}} {{keycap:F}} {{keycap:F}} `0` {{key:ENTER}} `2` {{key:≫}} | $\text{0x10}$ | $\text{0x10}$ | $\text{0xFFFC}$ | **$\text{0x3FFC}$** | Logical right shift by $2$ bits zero-fills high bits (`0x3FFC` $= +16{,}380$) |

### Decoding Fixed-Point Q16.16 Motor Velocity and Simulating Dhahran Clock Truncation on the Stack

In high-precision motion control, angular velocity is represented in signed Q16.16 fixed-point format (16 integer bits, 16 fractional bits). The motor tachometer outputs a negative angular velocity of $-3.75\text{ rad/s}$. Maya wants Alex to:
1. Encode $-3.75\text{ rad/s}$ into 32-bit Q16.16 hexadecimal representation on the stack.
2. Divide the velocity by 4 using an arithmetic shift right (`ASR 2`), verifying the sign extension and resulting fixed-point value.
3. Simulate the 1991 Dhahran Patriot clock drift on the stack, computing the accumulated timing error and radar range-gate displacement.

```
Step 1: Compute Q16.16 representation of +3.75 rad/s:
        3.75 * 65536 = 245,760 = 0x0003C000
Step 2: Additive inverse (two's complement) for -3.75 rad/s:
        ~0x0003C000 + 1 = 0xFFFC3FFF + 1 = 0xFFFC4000
Step 3: Arithmetic shift right by 2 (ASR 2):
        0xFFFC4000 >> 2 = 0xFFFF1000
        In decimal: 0xFFFF1000 = -61,440. Dividing by 65536 = -0.9375 rad/s (-3.75 / 4).
Step 4: Dhahran truncation error per tick (24-bit representation of 0.1 s):
        0.1 - (1,677,721 / 16,777,216) = 0.000000095367 s
Step 5: Accumulation over 100 hours (3,600,000 ticks):
        3,600,000 * 0.000000095367 s = 0.3433 seconds
Step 6: Scud range gate error at Mach 5 (1,676 m/s):
        1,676 m/s * 0.3433 s = 575.43 meters
```

| Keystroke Sequence | Reg T | Reg Z | Reg Y | Reg X | Engineering Explanation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:HEX}} 32 {{key:WSZ}}` | $0$ | $0$ | $0$ | $0$ | Set 32-bit Hexadecimal mode |
| `3C000 {{key:NEG}}` | $0$ | $0$ | $0$ | **`0xFFFC4000`** | Negate Q16.16 $+3.75\text{ rad/s}$: two's complement $-3.75\text{ rad/s}$ is `0xFFFC4000` |
| `2 {{key:ASR}}` | $0$ | $0$ | $0$ | **`0xFFFF1000`** | Divide by 4 via `ASR 2`: sign-extended result is `0xFFFF1000` ($-0.9375\text{ rad/s}$) |
| `{{key:DEC}} 0.1 {{key:ENTER}}` | $0$ | $0$ | $0$ | $0.1$ | Switch to Decimal mode; stage exact decimal tenth of a second ($0.1\text{ s}$) |
| `1677721 {{key:ENTER}} 2 {{key:ENTER}} 24 {{key:yˣ}} {{key:÷}} {{key:-}}` | $0$ | $0$ | $0.1$ | $9.5367 \times 10^{-8}$ | Evaluate Patriot 24-bit truncation error per tick: $\Delta t_{\text{tick}} \approx 9.5367 \times 10^{-8}\text{ s}$ |
| `3600000 {{key:×}}` | $0$ | $0$ | $0.1$ | **$0.3433$** | Multiply by $3{,}600{,}000\text{ ticks}$ ($100\text{ hours}$): clock drift is $\mathbf{0.3433\text{ seconds}}$ |
| `1676 {{key:×}}` | $0$ | $0$ | $0.1$ | **$575.43$** | Multiply by Scud speed ($1{,}676\text{ m/s}$): radar range-gate error is $\mathbf{575.43\text{ meters}}$ |

Alex stares at the number: *575.43 meters.*

*"That is the distance of nearly six football fields,"* Maya says quietly. *"A missile traveling at Mach 5 covers that distance in an eyeblink. In software, rounding $0.1$ looks innocent. In the physical world, it was fatal."*

---

### Try It on the Stack

Work through these five field problems on your calculator. Step-by-step keystroke solutions and register walkthroughs are provided in [Appendix C](appendix-c-solutions-to-practice-problems.md).

1. **Two's Complement Additive Inversion:** An 8-bit sensor register reports a raw signed temperature offset of $-42_{10}$. Convert this number to its 8-bit two's complement hexadecimal representation, and verify its additive inverse by adding $+42_{10}$.
2. **Contiguous Bitmask Generation:** A telecommunications framing chip requires isolating bits [14:9] (a 6-bit channel identifier) within a 16-bit header. Calculate the exact hexadecimal bitmask required.
3. **Logical vs. Arithmetic Right Shift:** A signed 16-bit audio sample has a value of $-16{,}384_{10}$ (`0xC000`). Divide this sample by 8 ($2^3$) using both logical right shift and arithmetic right shift. Compare the decimal results.
4. **Cortex-M Bit-Band Alias Address Calculation:** Determine the exact 32-bit bit-band alias memory address required to atomically toggle bit 3 of GPIO Port A Output Data Register (`GPIOA->ODR`), located at peripheral byte address `0x40020014`.
5. **Q8.8 Fixed-Point Voltage Threshold Encoding:** A battery monitoring IC measures an undervoltage threshold of $3.625\text{ V}$. Encode this voltage into unsigned Q8.8 fixed-point format, and determine the raw 16-bit register constant.

With the bit-serial ring oscillator, shift register, and SPI timing verified at the bench, Noah Chen and Sarah Pryce turn from raw register logic to the high-throughput communication corridors of modern instrumentation—where serialized data frames must survive electromagnetic transit across factory backplanes.

---

# Chapter 8: The Corrupt Sensor Packet Across the Serial Bus

High on the deck of an offshore oil production platform in the North Sea, icy gale-force winds whip spray against the steel bulkhead of the separation manifold module. Inside the pressurized explosion-proof telemetry junction enclosure, a master supervisory terminal continuously monitors crude oil separation temperatures via a multidrop RS-485 serial fieldbus. The fieldbus connects twenty-four remote RTD temperature transmitters daisy-chained across eight hundred meters of shielded twisted-pair industrial cable.

Suddenly, the central human-machine interface (HMI) screen flashes yellow warning banners across the control room. The crude oil inlet temperature on Wellhead 4—normally stable at $+75.125^\circ\text{C}$—is jumping erratically. For three seconds the HMI displays $-1.08 \times 10^9$, then `NaN` (Not a Number), then drops connection entirely with a continuous flood of `CRC_ERROR` and `UART_FRAME_ERR` status flags.

Senior automation systems architect Noah Chen and field instrumentation engineer Sarah Pryce arrive at the junction cabinet with their test equipment. Noah clips a digital storage oscilloscope across the differential RS-485 bus lines ($A$ and $B$). The differential eye diagram reveals significant high-frequency ringing and waveform distortion at the signal transitions. Sarah hooks a serial bus protocol analyzer to the receiver lines. The analyzer captures the raw 32-bit hexadecimal data words arriving from the Wellhead 4 transmitter:
1. The 32-bit temperature telemetry word arrives as `0x00409642`. When Noah examines the byte stream, he recognizes that the remote sensor microcontroller (a Little-Endian ARM Cortex) transmitted its native byte sequence across an industrial network protocol (Modbus RTU) that mandates Big-Endian network byte order. The bytes are arriving inverted.
2. The 32-bit frame check sequence trailing the packet fails verification against the standard IEEE 802.3 CRC-32 polynomial, rejecting every incoming packet even when the raw sensor readings are valid.
3. The sensor node's asynchronous serial UART baud rate is configured for $115{,}200\text{ bps}$ using an unverified hardware baud divisor register. Under severe sub-zero North Sea operating temperatures, the local crystal oscillator has drifted by $-3.2\%$, pushing the cumulative bit-sampling skew across the 10-bit serial frame past the maximum allowable timing margin.
4. Downstream SCADA routers are failing to forward telemetry packets because the plant subnet mask was entered as a `/22` instead of a `/24`, creating broadcast domain collisions across the industrial automation network.

To diagnose the communication failure, restore serial packet integrity, and stabilize the offshore production platform, Noah and Sarah turn to the **SC-16 Digital Systems, Bitwise Logic & Cyber Operations** calculator:
1. Reverse network byte order using 32-bit byte-swapping (`BSWAP`) to align Little-Endian sensor data with Big-Endian wire formats.
2. Unpack the IEEE-754 single-precision floating-point bitfields (sign bit, biased exponent, and fractional mantissa) to decode physical temperatures directly on the stack.
3. Step through Galois Field $GF(2)$ polynomial division and verify reflected CRC-32 linear feedback shift register (LFSR) checksums.
4. Partition industrial IP subnets using Classless Inter-Domain Routing (CIDR) netmask and host capacity calculations.
5. Audit 16-times oversampled UART hardware baud divisors and quantify thermal clock drift tolerances.

---

## Endian Architectures, IEEE-754 Packing, and Galois Noise Shields

Data corruption across industrial communications rarely stems from broken physical transceivers; it arises when interacting subsystems make conflicting assumptions about bit endianness, word boundaries, and polynomial representations.

### Big-Endian vs. Little-Endian Byte Ordering

In 1726, Jonathan Swift published *Gulliver's Travels*, satirizing the absurd political wars between the empires of Lilliput and Blefuscu. The conflict erupted over a royal decree compelling citizens to break their boiled eggs at the small end (the *Little-Endians*), prompting a violent rebellion by the *Big-Endians*, who insisted on breaking their eggs at the big end.

In 1980, legendary computer scientist Danny Cohen published the famous Internet Engineering Note 137, titled *"On Holy Wars and a Plea for Peace"*. Cohen adopted Swift's satire to describe the most contentious battle in computer architecture: **how multi-byte binary numbers are stored in physical computer memory**.

Consider a 32-bit unsigned hexadecimal integer:
$$V = \text{0x42964000}$$

This double-word consists of four distinct 8-bit bytes:
- Byte 0 (Least Significant Byte, LSB): `0x00`
- Byte 1: `0x40`
- Byte 2: `0x96`
- Byte 3 (Most Significant Byte, MSB): `0x42`

Suppose this 32-bit word is stored in memory starting at byte address `0x20000000`. In what order should the four physical memory bytes be arranged?

```
Address:        0x20000000    0x20000001    0x20000002    0x20000003
-----------------------------------------------------------------------
Big-Endian:        0x42          0x96          0x40          0x00
                  (MSB)                                     (LSB)

Little-Endian:     0x00          0x40          0x96          0x42
                  (LSB)                                     (MSB)
```

1. **Big-Endian Architecture** (Motorola 68000, SPARC, IBM System/360, PowerPC):
   - The **Most Significant Byte** is stored at the **lowest memory address**.
   - Natural human reading order: reading left-to-right from lowest address to highest address presents the number in conventional high-order notation.
   - Adopted by RFC 791 as **Network Byte Order**: all multi-byte fields in standard Internet protocols (IPv4 addresses, TCP port numbers) are transmitted Big-Endian (MSB first).
2. **Little-Endian Architecture** (x86, x86-64, DEC VAX, modern ARM Cortex by default, RISC-V):
   - The **Least Significant Byte** is stored at the **lowest memory address**.
   - Silicon hardware design: If an engineer casts a pointer to a 32-bit integer (`uint32_t *p32`) down to a 16-bit integer (`uint16_t *p16`) or an 8-bit byte (`uint8_t *p8`) at address `p`, the pointer references the numerical value without offset adjustment. The low-order bits do not move when the variable is widened or narrowed. Furthermore, in hardware ripple-carry adders, addition begins at the lowest address (LSB) and propagates carries upward, matching the natural sequential flow of memory access.

The conflict arises when Little-Endian microcontrollers communicate with Big-Endian networks. If a Little-Endian ARM microcontroller transmits the 32-bit float `0x42964000` over a Big-Endian serial bus without swapping bytes, the remote receiver reads the memory bytes in reverse:
$$\text{Received Word} = \text{0x00409642}$$
A reading of $+75.125^\circ\text{C}$ is corrupted into an invalid floating-point representation.

To bridge this divide, microprocessors provide hardware byte-swap instructions (`BSWAP` in x86, `REV` in ARM). On the SC-16 calculator, pressing `{{key:SWP}}` reverses the byte order of the active word in Register X across the selected word width (16, 32, or 64 bits).

In the industrial world, this endian confusion is further compounded by **Modbus Register Swapping**. The Modbus RTU protocol transmits 16-bit registers in Big-Endian order. However, when manufacturers transmit 32-bit IEEE-754 floats or 32-bit integers across two consecutive 16-bit registers (e.g., registers 40001 and 40002), the Modbus standard does not specify the register order. This results in four conflicting industrial formats:
- **Big-Endian (ABCD)**: Register 1 holds MSW (MSB first), Register 2 holds LSW (MSB first). Standard network byte order.
- **Little-Endian Inverted (DCBA)**: True little-endian byte stream.
- **Mid-Little / Word Swap (CDAB)**: 16-bit words are swapped, but bytes within each word are Big-Endian. Most common in Schneider and Siemens PLCs.
- **Mid-Big / Byte Swap (BADC)**: Bytes within each 16-bit word are swapped, but words are in Big-Endian order.

Without a stack calculator capable of multi-base byte swapping and bitfield extraction, debugging these four permutations in the field requires tedious trial and error.

### IEEE-754 Floating-Point Encoding: Packing Real Numbers into 32 Bits

Text-based protocols like JSON or NMEA-0183 are human-readable, but they incur substantial serial overhead: transmitting `'75.1250'` requires seven ASCII bytes rather than four binary bytes, consuming $75\%$ more channel bandwidth. Fixed-point integers are compact, but they enforce a rigid dynamic range. To represent scientific quantities across orders of magnitude with constant relative precision, William Kahan and the IEEE committee created the **IEEE-754 Floating-Point Standard**.

In IEEE-754 single-precision (`binary32`), an arbitrary real number is packed into exactly 32 bits:
- **Bit 31 (Sign, $S$)**: 1 bit. $S = 0$ for positive numbers, $S = 1$ for negative numbers.
- **Bits [30:23] (Biased Exponent, $E$)**: 8 bits. Unsigned integer ranging from $0$ to $255$. An offset bias of $+127$ is added to the true power-of-two exponent $e$, so $E = e + 127$. This bias allows exponents from $-126$ to $+127$ to be compared as unsigned integers without sign logic.
- **Bits [22:0] (Fractional Mantissa/Significand, $M$)**: 23 bits. Represents the fractional part of the significand. In normalized numbers, there is an **implicit leading 1** before the binary point ($1.M$), giving 24 bits of effective precision ($\approx 7.22$ decimal digits).

```
 31 30                  23 22                                       0
+--+----------------------+------------------------------------------+
|S |   Biased Exponent E  |          Fractional Mantissa M           |
|1b|        8 bits        |                 23 bits                  |
+--+----------------------+------------------------------------------+
```

The mathematical decoding equation for normalized numbers is:

**Eq. 8.1 — IEEE 754 Floating-Point Real Decoding**
$$V_{\text{float}} = (-1)^S \times \left(1 + \frac{M}{2^{23}}\right) \times 2^{E - 127}$$

Where:
- $S \in \{0, 1\}$ is the sign bit.
- $E \in [1, 254]$ is the biased exponent ($e = E - 127$).
- $M \in [0, 2^{23}-1]$ is the 23-bit fractional mantissa.

IEEE-754 defines critical special boundary cases:
1. **Zero ($E = 0, M = 0$)**: Evaluates to $\pm 0.0$ depending on $S$. Because there is an explicit sign bit, IEEE-754 has both $+0$ and $-0$, though they compare as equal ($+0.0 == -0.0$).
2. **Subnormal / Denormal Numbers ($E = 0, M \ne 0$)**:
   When the exponent drops below the minimum normalized threshold ($e = -126$), the implicit leading bit switches from $1$ to **$0$**:
   $$V_{\text{subnormal}} = (-1)^S \times \left(0 + \frac{M}{2^{23}}\right) \times 2^{-126}$$
   This feature—known as **Gradual Underflow**—prevents precision cliffs, ensuring that subtracting two close floating-point numbers never flushes abruptly to zero.
3. **Infinity ($E = 255, M = 0$)**: Evaluates to $+\infty$ or $-\infty$. Arithmetic operations that overflow the representable dynamic range saturate at infinity rather than corrupting memory.
4. **Not-a-Number (NaN) ($E = 255, M \ne 0$)**: Represents invalid operations (such as $0/0$ or $\sqrt{-1}$).
   - **Quiet NaN (QNaN)**: MSB of mantissa is $1$ ($M_{22} = 1$). Propagates through arithmetic operations without raising hardware exceptions.
   - **Signaling NaN (SNaN)**: MSB of mantissa is $0$ ($M_{22} = 0, M \ne 0$). Triggers an immediate hardware floating-point trap.

Furthermore, single-precision floating point exhibits a physical finite resolution limit known as **Machine Epsilon** ($\epsilon_{\text{mach}} = 2^{-23} \approx 1.192 \times 10^{-7}$). This represents the relative spacing between consecutive representable numbers. When subtracting two nearly identical floating-point numbers, higher-order mantissa bits cancel out, leaving only low-order rounding noise—a phenomenon known as **Catastrophic Cancellation**. In industrial software, testing floating-point numbers for exact equality (`a == b`) is an anti-pattern; developers must always test within a scaled tolerance band ($|a - b| \le \epsilon \cdot \max(|a|, |b|)$).

To decode the Wellhead 4 temperature reading `0x42964000`:
- Sign bit: $S = 0$ (positive).
- Biased exponent: $E = \text{0x85} = 133_{10}$. True exponent $e = 133 - 127 = +6$.
- Mantissa: Bits [22:0] = `0x164000` = $\text{00101100100000000000000}_2$.
  $$\frac{M}{2^{23}} = 2^{-3} + 2^{-5} + 2^{-6} + 2^{-9} = 0.125 + 0.03125 + 0.015625 + 0.001953125 = 0.173828125$$
- Evaluating Eq. 8.1:
  $$V_{\text{float}} = (+1) \times (1 + 0.173828125) \times 2^6 = 1.173828125 \times 64 = \mathbf{+75.1250^\circ\text{C}}$$

### Cyclic Redundancy Checks Across Industrial Noise: Galois Field Modulo-2 Arithmetic

In simple serial protocols, engineers historically used **parity bits** (checking whether the number of `1` bits is even or odd) or **additive checksums** (summing all packet bytes modulo 256). Both methods are inadequate in industrial environments:
- A parity bit fails completely if an industrial electromagnetic transient flips an even number of bits ($2, 4, 6$).
- An additive checksum detects single-bit errors, but if an electrical transient increments one byte while decrementing another byte, or if bytes arrive transposed in time, the sum remains unchanged.

To detect burst errors caused by motor contactor arcs and variable-frequency drives, modern telecommunications relies on **Cyclic Redundancy Checks (CRC)**.

A CRC treats a digital data stream not as a sequence of numbers, but as the coefficients of a polynomial over the **Galois Field of two elements**, denoted $\mathbf{GF(2)}$.

In $GF(2)$:
- Addition and subtraction are identical and correspond to the **bitwise XOR operation ($\oplus$)**:
  $$0 \oplus 0 = 0, \quad 0 \oplus 1 = 1, \quad 1 \oplus 0 = 1, \quad 1 \oplus 1 = 0$$
  Arithmetic proceeds with no carries and no borrows.
- Multiplication corresponds to Boolean AND.
- Division is polynomial long division executed using successive shifts and XOR operations.

To see $GF(2)$ polynomial long division clearly, consider dividing a 4-bit message $M = 1101_2$ ($x^3 + x^2 + 1$) by a 3-bit generator polynomial $G = 1011_2$ ($x^3 + x + 1$).
First, we append 3 zero bits to $M$: $1101000_2$.
Then we perform long division using XOR:
```
           1111 (Quotient)
     ------------------
1011 | 1101000
       1011
       ----
        1100
        1011
        ----
         1110
         1011
         ----
          1010
          1011
          ----
           001  (Remainder R = CRC = 001_2)
```
Transmitting $1101_2$ followed by remainder $001_2$ gives the protected frame $1101001_2$. Dividing $1101001_2$ by $1011_2$ at the receiver yields an exact remainder of zero.

Mathematically, to generate an $N$-bit CRC checksum, the transmitter and receiver agree on a fixed **generator polynomial** $G(x)$ of degree $N$. The transmitter appends $N$ zero bits to the message polynomial $M(x)$ and divides by $G(x)$ using $GF(2)$ arithmetic. The remainder $R(x)$ of this division is the CRC checksum:

$$M(x) \cdot x^N = Q(x) \cdot G(x) \oplus R(x)$$

Because subtraction is identical to addition in $GF(2)$, appending the remainder $R(x)$ to the transmitted message ensures that the entire transmitted frame is **exactly divisible by $G(x)$ with zero remainder**:

$$\left(M(x) \cdot x^N \oplus R(x)\right) \div G(x) = Q(x) \quad \text{Remainder} = 0$$

A well-designed CRC polynomial $G(x)$ provides ironclad mathematical guarantees:
1. It detects **all single-bit errors** anywhere in the message.
2. It detects **all double-bit errors**, provided the message length is less than the cycle length of the polynomial.
3. If $G(x)$ contains $(x + 1)$ as a factor (as in CRC-16-CCITT and CRC-32), it detects **all odd numbers of bit errors** (1, 3, 5, 7, ...).
4. It detects **all burst errors** of length up to and including $N$ bits (the degree of the polynomial).
5. For burst errors longer than $N$ bits, the probability of an undetected error is at most $2^{-N}$. For CRC-32, that is a failure rate of less than $1$ in $4.29 \times 10^9$ frames.

In the **IEEE 802.3 Ethernet CRC-32** standard, the generator polynomial is:
$$G(x) = x^{32} + x^{26} + x^{23} + x^{22} + x^{16} + x^{12} + x^{11} + x^{10} + x^8 + x^7 + x^5 + x^4 + x^2 + x + 1$$

In standard hexadecimal notation, this polynomial is represented by the 32-bit constant `0x04C11DB7`.

However, serial UARTs and Ethernet controllers transmit data **Least Significant Bit first (LSB-first)**. If hardware had to shift bits MSB-first, it would require reversing every byte in memory. To optimize silicon performance, IEEE 802.3 uses a **Reflected CRC-32**:
1. The generator polynomial is bit-reversed (reflected): `0x04C11DB7` reflected becomes **`0xEDB88320`**.
2. The initial CRC register is seeded with `0xFFFFFFFF` to protect against leading zero errors.
3. For each bit, the linear feedback shift register (LFSR) shifts right. If the bit shifted out of the LSB is `1`, the register is XORed with `0xEDB88320`.
4. After all bits are processed, the result is XORed with `0xFFFFFFFF` (final inversion).

The mathematical recurrence relation for a reflected LFSR step is:

**Eq. 8.2 — Reflected CRC-32 LFSR Step**
$$C_{i+1} = \begin{cases} (C_i \gg 1) \oplus G_{\text{poly}} & \text{if } (C_i \ \& \ 1) = 1 \\ C_i \gg 1 & \text{if } (C_i \ \& \ 1) = 0 \end{cases}$$

Where:
- $C_i$ is the current 32-bit LFSR accumulator state.
- $G_{\text{poly}} = \text{0xEDB88320}$ is the reflected IEEE-802.3 CRC-32 divisor polynomial.
- $\gg$ is the logical shift right operator.

### Asynchronous Serial UART Timing and Clock Drift Accumulation

Finally, Noah examines the oscilloscope trace of the serial waveform. The pulse widths of the incoming bits are slightly narrower than they should be.

In an **asynchronous** serial link (such as RS-232, RS-422, or RS-485), there is **no shared clock wire**. The transmitter and receiver operate from independent local quartz crystal or RC oscillators.

How does the receiver know when to read the data bits?

1. **The Start Bit**: When the line is idle, it rests in the Mark state (logic `1`). The transmission begins with a **Start Bit** (a transition to logic `0`). This falling edge resets the receiver's internal timing generator.
2. **Sixteen-Times (16x) Oversampling**: To ensure reliable synchronization, the UART receiver peripheral does not sample at the symbol baud rate. Instead, it oversamples the incoming signal at **16 times the baud frequency** ($16 \times B$).
3. **Majority Voting**: When the falling edge is detected, the UART counts 8 oversample clock ticks to reach the exact physical center of the Start Bit. It then verifies the start bit. For each subsequent bit (8 data bits, optional parity bit, and 1 or 2 stop bits), the UART counts 16 ticks, landing squarely in the middle of each bit cell. At ticks 7, 8, and 9, the receiver takes three high-speed samples and performs a **2-out-of-3 majority vote** to reject high-frequency noise spikes.

```
       Start Bit          Data Bit 0          Data Bit 1
    +---+               +---------------+   +---------------+
    |   |               |               |   |               |
----+   +---------------+               +---+               +---
    ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^
    |   |   |   |   |   |   |   |   |   |   |
  Edge  0   4   8  12  16   4   8  12  16   4   8  12  16
                ^               ^               ^
             Sample          Sample          Sample
```

However, because the transmitter and receiver clocks are generated by independent physical crystals, their frequencies are never identical. The difference in clock frequency causes the sampling point to **accumulate drift across the frame**.

In a standard 10-bit asynchronous frame (1 start bit, 8 data bits, 1 stop bit), the final bit sampled is the Stop Bit, located $9.5$ bit periods after the initial start edge.

For the stop bit to be read correctly, the sampling point must not drift past the boundary of the bit cell ($\pm 0.5$ bit period):
$$\text{Max Allowable Clock Error} = \frac{\pm 0.5 \text{ bit}}{9.5 \text{ bits}} \approx \pm 5.26\%$$

However, this theoretical limit assumes perfect square pulses with zero rise time. On real-world industrial cables with line capacitance, slew-rate limited transceivers, and electrical noise, the reliable sampling window is restricted to the middle $50\%$ of the bit cell ($\pm 0.25$ bit period). Therefore, industrial standards mandate that total cumulative clock mismatch between transmitter and receiver must **never exceed $\pm 2.0\%$ to $\pm 2.5\%$**.

---

## Network Byte Order, Floating-Point Bitfields, and Galois-Field Checksums

### Endian Byte Swapping and Single-Precision Floating-Point Encoding

On the SC-16 calculator, multi-byte endianness conversion and IEEE-754 floating-point translation are executed directly with dedicated hardware functions:
- `{{key:SWP}}`: Swaps the byte ordering of the active register according to the selected word width (`WSIZE`). In 32-bit mode, byte sequence $[B_3, B_2, B_1, B_0]$ transforms into $[B_0, B_1, B_2, B_3]$.
- `{{key:FLT}}`: Reinterprets a 32-bit hexadecimal bit pattern as an IEEE-754 single-precision float (or converts a decimal float into its raw 32-bit hexadecimal bitfield representation).

To see this in action:
The Wellhead 4 telemetry word arrived as `0x00409642`.
1. Keying `00409642` into Register X in 32-bit Hexadecimal mode and pressing `{{key:SWP}}` produces `0x42964000`.
2. Pressing `{{key:FLT}}` immediately decodes the bitfield via Eq. 8.1 into **`+75.1250`** ($^\circ\text{C}$).

### Polynomial Division over Galois Field Two and Cyclic Redundancy Checks

The SC-16 integrates a hardware Galois Field arithmetic engine:
- `{{key:CRC}}`: Computes standard cyclic redundancy checks over byte buffers or multi-word frames.
- Polynomial presets include:
  - `CRC-8-ATM` ($G(x) = x^8 + x^2 + x + 1$, polynomial `0x07`)
  - `CRC-16-CCITT` ($G(x) = x^{16} + x^{12} + x^5 + 1$, polynomial `0x1021`)
  - `CRC-16-MODBUS` ($G(x) = x^{16} + x^{15} + x^2 + 1$, reflected polynomial `0xA001`)
  - `CRC-32-IEEE` ($G_{\text{ref}} = \text{0xEDB88320}$)

For the sensor payload word `0x42964000`, the reflected CRC-32 LFSR steps evaluate bit-by-bit:
Starting from initial seed $C_0 = \text{0xFFFFFFFF}$, each byte of the payload shifts through the reflected feedback taps. If bit 0 of the accumulator is `1`, the register shifts right by 1 bit and XORs with `0xEDB88320`. After all four bytes (`0x00`, `0x40`, `0x96`, `0x42`) are processed, final inversion ($\sim C$) evaluates the expected 32-bit frame check sequence:
$$\text{FCS} = \text{0xCBF43926}$$

When Sarah inspects the corrupted sensor packet, the received CRC field was `0x2639F4CB`—the CRC bytes were transmitted in Little-Endian byte order without being swapped to network order.

---

## CIDR Subnet Mask Synthesis and Asynchronous Serial Baud Divisors

### CIDR Prefix Netmasks and Usable Host Counts

In industrial automation networks, operational technology (OT) sensors and programmable logic controllers (PLCs) are isolated into dedicated IP subnets to prevent broadcast storms and cyber intrusion.

Under **Classless Inter-Domain Routing (CIDR)**, a subnet is specified by its base IP address followed by a prefix length $P \in [0, 32]$, representing the number of contiguous leading `1` bits in the 32-bit network mask.

The governing equations for netmask synthesis and usable host capacity are:

**Eq. 8.3 — CIDR Netmask and Usable Host Capacity**
$$\text{Netmask}(P) = \left(2^{32} - 2^{32 - P}\right) = \text{0xFFFFFFFF} \ll (32 - P)$$
$$N_{\text{hosts}} = 2^{32 - P} - 2$$

Where:
- $P$ is the CIDR prefix length ($0 \le P \le 32$).
- $\ll$ is the logical shift-left operator.
- The term $-2$ in host capacity accounts for the two reserved addresses in every IPv4 subnet:
  - **Network Address** (all host bits `0`): Identifies the subnet itself.
  - **Directed Broadcast Address** (all host bits `1`): Sends packets to all hosts on the subnet simultaneously.

Common Industrial Subnet Allocations:
- `/24` Subnet ($P = 24$):
  - Netmask: $\text{0xFFFFFFFF} \ll 8 = \text{0xFFFFFF00} = \mathbf{255.255.255.0}$
  - Host Capacity: $2^{32-24} - 2 = 2^8 - 2 = 256 - 2 = \mathbf{254\text{ hosts}}$
- `/22` Subnet ($P = 22$):
  - Netmask: $\text{0xFFFFFFFF} \ll 10 = \text{0xFFFFFC00} = \mathbf{255.255.252.0}$
  - Host Capacity: $2^{32-22} - 2 = 2^{10} - 2 = 1024 - 2 = \mathbf{1{,}022\text{ hosts}}$
- `/30` Point-to-Point Link ($P = 30$):
  - Netmask: $\text{0xFFFFFFFC} = \mathbf{255.255.255.252}$
  - Host Capacity: $2^2 - 2 = \mathbf{2\text{ hosts}}$ (strictly for two router interfaces).

When Noah reviews the plant network configuration, he discovers that the telemetry gateway router was configured as `/22` (`255.255.252.0`), causing it to treat four adjacent `/24` subnets (spanning IP addresses `192.168.0.0` through `192.168.3.255`) as a single broadcast domain. Routers refused to route between the SCADA server and sensor gateways because they treated the nodes as members of the same physical link.

### Sixteen-Times Oversampled Asynchronous Serial Divisors and Clock Drift

To generate standard baud rates from a fixed peripheral bus clock $f_{\text{clk}}$, microcontroller UART peripherals use an internal integer and fractional clock prescaler.

Dividing the peripheral clock $f_{\text{clk}}$ by 16 times the desired baud rate $B$ yields the hardware baud divisor $D$:

**Eq. 8.4 — Sixteen-Times Oversampled UART Baud Divisor**
$$D = \operatorname{round}\!\left(\frac{f_{\text{clk}}}{16 \cdot B}\right)$$
$$\text{Err\%} = \left(\frac{B_{\text{actual}} - B}{B}\right) \times 100\%$$

Where:
- $f_{\text{clk}}$ is the peripheral clock frequency (in $\text{Hz}$).
- $B$ is the nominal target baud rate (in $\text{bits/s}$).
- $D$ is the integer divisor loaded into the UART Baud Rate Register (`USART_BRR`).
- $B_{\text{actual}} = \frac{f_{\text{clk}}}{16 \cdot D}$ is the exact baud rate synthesized by the hardware divider.
- $\text{Err\%}$ is the percentage baud rate error (must satisfy $|\text{Err\%}| \le 2.0\%$).

Let us analyze the Wellhead 4 transmitter's timing:
The peripheral bus clock is $f_{\text{clk}} = 48\text{ MHz}$ ($48{,}000{,}000\text{ Hz}$). The target baud rate is $B = 115{,}200\text{ bps}$.

Evaluating Eq. 8.4:
$$D_{\text{ideal}} = \frac{48{,}000{,}000}{16 \times 115{,}200} = \frac{48{,}000{,}000}{1{,}843{,}200} \approx 26.041667$$

Rounding to the nearest integer yields $D = 26$.
The actual synthesized baud rate is:
$$B_{\text{actual}} = \frac{48{,}000{,}000}{16 \times 26} = \frac{48{,}000{,}000}{416} \approx 115{,}384.62\text{ bps}$$

The nominal clock error is:
$$\text{Err\%} = \left(\frac{115{,}384.62 - 115{,}200}{115{,}200}\right) \times 100\% = +0.160\%$$

Under laboratory conditions at $+20^\circ\text{C}$, a $+0.16\%$ error is pristine.
However, out on the North Sea rig at $-25^\circ\text{C}$, the uncompensated local crystal oscillator frequency dropped by $-3.2\%$, shifting the effective clock frequency down to:
$$f_{\text{clk, cold}} = 48\text{ MHz} \times (1 - 0.032) = 46.464\text{ MHz}$$

With divisor $D = 26$, the cold synthesized baud rate became:
$$B_{\text{cold}} = \frac{46{,}464{,}000}{16 \times 26} = 111{,}692.3\text{ bps}$$

Comparing this cold baud rate against the receiver's nominal $115{,}200\text{ bps}$:
$$\text{Err\%}_{\text{cold}} = \left(\frac{111{,}692.3 - 115{,}200}{115{,}200}\right) \times 100\% = \mathbf{-3.045\%}$$

The clock error exceeds the standard $\pm 2.0\%$ asynchronous UART threshold. Over the 10-bit frame, the receiver's sampling point drifted by $0.3045$ bit periods, landing outside the safe sampling window and triggering recurring `UART_FRAME_ERR` flags.

### RS-485 Transceiver Bus Loading, Ground Potentials, and Physical Layer Integrity

Sarah examines the physical RS-485 wiring inside the junction box. Even if the baud rate is corrected, an RS-485 bus must satisfy four physical layer laws to ensure signal integrity across industrial environments:

1. **Transmission Line Characteristic Impedance and Termination**:
   RS-485 uses a balanced differential pair ($A$ and $B$, or $D+$ and $D-$). Standard industrial shielded twisted pair cable (such as Belden 3105A) has a characteristic impedance of $Z_0 = 120\ \Omega$.
   When electrical signals travel along a transmission line, any impedance discontinuity causes reflections. If the cable ends are left open-circuit (unterminated), the traveling edge reflects back with identical polarity, creating ringing that creates false zero-crossings and corrupts UART start bits.
   To eliminate reflections, **both extreme physical ends of the cable trunk must be terminated with a $120\ \Omega$ resistor** placed across line $A$ and line $B$:
   $$R_{\text{term}} = Z_0 = 120\ \Omega$$
   Termination resistors must never be placed at intermediate stub nodes, as multiple parallel terminations overload the transmitter driver.
2. **Unit Loading (UL) and Maximum Transceiver Count**:
   The EIA/TIA-485 standard mandates that an RS-485 driver must be capable of driving a minimum differential voltage of $|V_{OD}| \ge 1.5\text{ V}$ into a 54-ohm load (representing two $120\ \Omega$ termination resistors in parallel, $60\ \Omega$, plus parallel receiver leakage).
   A standard RS-485 receiver presents an input impedance of $12\ \text{k}\Omega$, defined as **One Unit Load ($1\text{ UL}$)**. Standard drivers are rated to drive up to **32 Unit Loads**. Modern low-power transceivers feature high input impedance ($96\ \text{k}\Omega$, or $1/8\text{ UL}$), allowing up to $256$ transceivers on a single bus trunk without repeater amplifiers.
3. **Fail-Safe Bus Biasing Networks**:
   When no transmitter is actively driving the bus (during the idle time between packets, or if a cable breaks), the differential lines float in a high-impedance state ($V_A \approx V_B$, so $V_{AB} \approx 0\text{ V}$).
   Standard RS-485 receiver thresholds are defined between $-200\text{ mV}$ and $+200\text{ mV}$. If $V_{AB}$ is near zero, ambient industrial electromagnetic noise easily bounces the receiver above and below zero, causing the UART to detect ghost start bits and flood the processor with framing errors.
   To prevent this, engineers install a **Fail-Safe Biasing Network**:
   - Pull-up resistor $R_{\text{pullup}}$ from line $A$ to $+5\text{ V}$.
   - Pull-down resistor $R_{\text{pulldown}}$ from line $B$ to Ground.
   - These resistors force $V_{AB} \ge +200\text{ mV}$ (logic `1`, Mark/Idle state) whenever the bus is undriven:
     $$V_{AB} = V_{\text{CC}} \times \frac{R_{\text{term, eq}}}{2 \cdot R_{\text{bias}} + R_{\text{term, eq}}} \ge 200\text{ mV}$$
   Where $R_{\text{term, eq}} = 120\ \Omega \parallel 120\ \Omega = 60\ \Omega$. Sizing $R_{\text{bias}} \le 680\ \Omega$ guarantees robust fail-safe idle voltage.
4. **Ground Potential Differences (GPD) and Galvanic Isolation**:
   Across eight hundred meters of offshore steel structure, the local earth ground potential at Wellhead 4 often differs from the control room ground by tens of volts. This **Ground Potential Difference (GPD)** is driven by massive motor return currents, cathodic corrosion protection systems, and switching transients.
   The absolute common-mode voltage rating ($V_{\text{CM}}$) of standard RS-485 transceivers is strictly restricted to **$-7\text{ V}$ to $+12\text{ V}$**. If the ground offset between two nodes exceeds this window, the transceiver input ESD diodes conduct, leading to latch-up, thermal runaway, and transceiver destruction.
   To survive harsh industrial field conditions, nodes must incorporate **Galvanic Isolation**:
   - High-speed digital isolators (capacitive or magnetic barriers providing $2.5\text{ kV}_{\text{RMS}}$ to $5\text{ kV}_{\text{RMS}}$ isolation).
   - Isolated DC-DC power converters to float the transceiver ground relative to local earth.
   - Cable shield grounding rules: The cable drain wire and braided shield must be grounded at **exactly one physical point** (typically at the master telemetry panel). Connecting the shield to ground at both ends creates a closed ground loop, turning the cable shield into an unintended conductor that carries circulating ground currents and injects high-frequency common-mode noise directly into the signal pairs.

---

## Unpacking the Telemetry Frame and Auditing Subnets and Clocks on the Stack

On the SC-16, industrial communications engineering is executed through dedicated stack keys.

| Button | Operation | Register Z | Register Y | Register X | Governing Expression |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`{{key:SWP}}`** | Word Byte-Swap (Endian Reversal) | — | — | Word $X$ | Inverts byte order across active `WSIZE` |
| **`{{key:FLT}}`** | IEEE-754 Float Encode / Decode | — | — | Float / Hex | Converts hex bitfield to float, or float to hex (Eq. 8.1) |
| **`{{key:CRC}}`** | Polynomial CRC Remainder | — | Data Word | Poly Preset | Evaluates $GF(2)$ polynomial division (Eq. 8.2) |
| **`{{key:NET}}`** | CIDR Netmask and Host Sizing | — | Prefix $P$ | Usable Hosts | Pushes Netmask to $Y$, host capacity to $X$ (Eq. 8.3) |
| **`{{key:BPS}}`** | 16x Oversampled Baud Divisor | — | Clock $f_{\text{clk}}$ | Baud Rate $B$ | Pushes Divisor $D$ to $Y$, error $\%$ to $X$ (Eq. 8.4) |

### Byte-Swapping the Telemetry Word, Decoding IEEE-754, and Checking CIDR and CRC

In 32-bit {{key:HEX}} mode ({{key:DEC}} `32` {{key:WSZ}} {{key:HEX}}), loading the mis-ordered Little-Endian capture `0x00004441` and pressing {{key:SWP}} restores the Big-Endian word `0x41440000`. Pressing {{key:FLT}} decodes the true heatsink temperature $\mathbf{+12.25^\circ\text{C}}$, keying `12.5` {{key:FLT}} encodes $+12.5^\circ\text{C}$ to `1095237632` ($\mathbf{\text{0x41480000}}$), and keying `24` {{key:NET}} pushes netmask `4294967040` (`0xFFFFFF00`) to Register $Y$ and $\mathbf{254}$ usable hosts to Register $X$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| {{key:DEC}} `32` {{key:WSZ}} {{key:HEX}} `4441` {{key:SWP}} | $0$ | $0$ | $\text{0x20}$ | $\text{0x41440000}$ | Byte-swap Little-Endian `0x00004441` into Big-Endian `0x41440000` |
| {{key:FLT}} | $0$ | $0$ | $32$ | $12.25$ | Decode IEEE 754 `binary32` pattern `0x41440000` to $+12.25$ |
| {{key:DEC}} `12.5` {{key:FLT}} | $0$ | $32$ | $12.25$ | $1095237632$ | Encode float `12.5` into IEEE 754 bit pattern `1095237632` (`0x41480000`) |
| `24` {{key:NET}} | $12.25$ | $1095237632$ | $4294967040$ | **$254$** | Compute `/24` netmask in $Y$ (`0xFFFFFF00`) and $254$ usable hosts in $X$ |

### Auditing the Sixteen-Times Oversampled UART Baud Divisor on the Stack

Switching to {{key:DEC}} mode, the engineer verifies the $115{,}200\text{ bps}$ UART divisor on the $48\text{ MHz}$ peripheral bus via `48000000` {{key:ENTER}} `115200` {{key:BPS}} ($\to D = \mathbf{26}$) and computes the resulting $+0.1603\%$ baud-rate drift:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| {{key:DEC}} `48000000` {{key:ENTER}} `115200` {{key:BPS}} | $0$ | $0$ | $0$ | $26$ | Compute $16\times$ oversampled UART integer divisor $D = 26$ |
| `16` {{key:×}} `48000000` {{key:x⇄y}} {{key:÷}} | $0$ | $0$ | $0$ | $115384.6154$ | Compute actual synthesized baud rate $B_{\text{actual}} = 48{,}000{,}000 / (16 \times 26)$ |
| `115200` {{key:-}} `115200` {{key:÷}} `100` {{key:×}} | $0$ | $0$ | $0$ | **$0.1603$** | Confirm $+0.1603\%$ UART clock drift (well within $\pm 2.0\%$ limit) |

### Diagnosing UART Clock Drift and Sizing an RS-485 Telemetry Baud Divisor on the Stack

Under the $-25^\circ\text{C}$ North Sea gale, the transmitter's crystal oscillator has slowed down by $-3.2\%$. Noah and Sarah must:
1. Calculate the exact cold clock frequency and evaluate the cold baud rate with divisor $D = 26$.
2. Determine the exact timing error percentage and compare it against the $\pm 2.0\%$ framing threshold.
3. Reprogram the UART to run at $57{,}600\text{ bps}$ and compute the new optimal divisor $D_{\text{new}}$ and cold error percentage to restore robust communication.

```
Step 1: Compute cold clock frequency:
        48,000,000 * (1 - 0.032) = 46,464,000 Hz
Step 2: Evaluate cold baud rate with D = 26:
        46,464,000 / (16 * 26) = 111,692.3 bps
Step 3: Evaluate percentage timing error:
        (111,692.3 - 115,200) / 115,200 = -3.045% (Violates +/-2.0% threshold)
Step 4: Sizing new divisor for 57,600 bps on cold clock:
        46,464,000 / (16 * 57,600) = 50.4167 -> D = 50
Step 5: Synthesized baud rate with D = 50:
        46,464,000 / (16 * 50) = 58,080.0 bps
Step 6: Evaluate new timing error:
        (58,080.0 - 57,600) / 57,600 = +0.833% (Safely inside +/-2.0% window)
```

| Keystroke Sequence | Reg T | Reg Z | Reg Y | Reg X | Engineering Explanation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:DEC}} 48000000 {{key:ENTER}}` | $0$ | $0$ | $0$ | $48{,}000{,}000$ | Enter nominal $48\text{ MHz}$ bus clock frequency |
| `0.032 {{key:ENTER}} 1 {{key:x⇄y}} {{key:-}} {{key:×}}` | $0$ | $0$ | $0$ | **`46464000`** | Scale by $(1 - 0.032)$: cold clock frequency is $46.464\text{ MHz}$ |
| `16 {{key:ENTER}} 26 {{key:×}} {{key:÷}}` | $0$ | $0$ | $46{,}464{,}000$ | **`111692.31`** | Compute actual cold baud rate with $D = 26$: $111{,}692.3\text{ bps}$ |
| `115200 {{key:-}} 115200 {{key:÷}} 100 {{key:×}}` | $0$ | $0$ | $0$ | **`-3.045`** | Evaluate cold timing error: $\mathbf{-3.045\%}$ (fails $\pm 2.0\%$ threshold) |
| `46464000 {{key:ENTER}} 57600 {{key:BPS}}` | $0$ | $-3.045$ | **`50`** | **`0.833`** | Sizing at $57.6\text{ kbps}$: Divisor $D = \mathbf{50}$, cold error is only $\mathbf{+0.833\%}$ |

Dropping the baud rate from $115.2\text{ kbps}$ to $57.6\text{ kbps}$ increases the divisor from $26$ to $50$, providing finer quantization and keeping error safely below one percent.

Noah terminates the un-terminated cable end with a $120\ \Omega$ metal film resistor, programs divisor $50$ into the sensor node, and re-enables the interface. The `CRC_ERROR` flags clear, the eye diagram opens cleanly, and the HMI temperature display locks at $+75.1250^\circ\text{C}$.

---

### Try It on the Stack

Work through these five field problems on your calculator. Step-by-step keystroke solutions and register walkthroughs are provided in [Appendix C](appendix-c-solutions-to-practice-problems.md).

1. **IEEE-754 Single-Precision Float Encoding:** An industrial chilled-water temperature probe reads $-12.50^\circ\text{C}$. Encode this temperature into its 32-bit hexadecimal IEEE-754 representation on the stack.
2. **32-Bit Endianness Reversal:** A Modbus RTU telemetry register arrives over the wire in Big-Endian order as `0x00409642`. Swap byte order to decode the Little-Endian ARM floating-point representation.
3. **CIDR /28 Subnet Sizing:** An automation field engineer is assigned subnet `192.168.10.64/28`. Calculate the subnet mask in hexadecimal, the total number of IP addresses, and the count of usable host addresses.
4. **16x Oversampled UART Baud Divisor on an 80 MHz Clock:** A microcontroller with an $80.0\text{ MHz}$ peripheral bus clock generates a high-speed UART baud rate of $921{,}600\text{ bps}$ using 16-times oversampling. Calculate the ideal floating-point divisor, find the integer rounding error, and compute the percentage baud rate error.
5. **Reflected CRC-32 Verification of a 4-Byte Payload:** Compute the 32-bit reflected CRC-32 checksum for a 4-byte telemetry payload containing `0x12345678`.

Having engineered robust frame synchronization, CRC verification, and oversampled baud generators, the systems team advances to the physical boundary where embedded silicon meets analog transducers: factory-floor sensor networks, high-resolution ADC front ends, and synchronous bus architecture.

---

# Chapter 9: Partitioning the Factory Floor Subnet and ADC Front End

On the floor of an advanced automotive battery gigafactory, an automated robotic assembly cell welds aluminum prismatic cell tabs at high velocity. Six-axis industrial robots maneuver fiber laser welding heads across battery trays with sub-millimeter precision. Each robot arm is actuated by high-torque permanent magnet synchronous motors (PMSM) driven by high-voltage pulse-width modulated (PWM) silicon carbide (SiC) inverter stages.

Suddenly, an automated weld cell shuts down with a catastrophic Emergency Stop fault. The primary spindle motor on Robot Arm 3 reports an intermittent over-temperature alarm, while the piezoelectric vibration monitoring node mounted directly to the spindle bearing registers extreme, unexplained 2.0 kHz vibration spikes. Simultaneously, the factory floor Ethernet switch logs continuous packet drops from the cell's vibration gateway, and high-speed telemetry packets delivered to the supervisory control server arrive corrupted or truncated in memory.

Senior automation systems architect Dev Patel and lead mixed-signal systems engineer Maya Lin hook their portable diagnostic instrumentation to the robot's control cabinet. A quick examination reveals a confluence of hardware and digital design flaws:
1. The motor drive's hardware PWM carrier frequency was set to an audible $4.0\text{ kHz}$. At this frequency, magnetostrictive forces inside the motor stator laminations generate an ear-splitting acoustic whine that resonates throughout the plant floor, while switching harmonics are coupling directly into the adjacent sensor cabling.
2. The analog front end of the piezoelectric vibration sensor uses a 12-bit Successive Approximation Register (SAR) Analog-to-Digital Converter (ADC) sampling at $25.0\text{ kSPS}$. However, the front-end anti-aliasing RC filter was sized improperly: high-frequency inverter switching spikes at $23.0\text{ kHz}$ fold across the Nyquist boundary and appear as phantom $2.0\text{ kHz}$ bearing vibrations. Furthermore, the sampling capacitor does not have enough time to settle within half a Least Significant Bit ($\frac{1}{2}\text{ LSB}$) during the microsecond acquisition window.
3. The robotic cell's IP network was assigned an ad-hoc subnet mask that overlaps with the central factory backbone, causing routing loops and packet drops whenever fifty-four vibration nodes broadcast high-rate telemetry simultaneously.
4. In the microcontroller's Direct Memory Access (DMA) engine, circular sample buffers were allocated with arbitrary, non-power-of-two byte lengths, causing DMA transfer addresses to cross 16-byte burst boundaries and trigger memory bus wait-state stalls.

To resolve the vibration aliasing, silence the acoustic inverter noise, partition the industrial subnet, and align the DMA ring buffers, Dev and Maya pull out the **SC-16 Digital Systems, Bitwise Logic & Cyber Operations** calculator:
1. Sizing the hardware timer prescaler and auto-reload period to synthesize an ultrasonic $20.0\text{ kHz}$ center-aligned PWM carrier frequency.
2. Calculating SAR ADC quantization step resolution ($V_{\text{LSB}}$), theoretical signal-to-noise ratio (SNR), and Effective Number of Bits (ENOB).
3. Designing a passive RC anti-aliasing filter to enforce exponential settling within half an LSB across the ADC sampling acquisition window.
4. Partitioning the factory subnet using Classless Inter-Domain Routing (CIDR) netmask and host capacity calculations.
5. Aligning DMA packet descriptors to natural power-of-two memory bus boundaries and evaluating high-speed synchronous bus timing margins.

---

## Ultrasonic Motor Inverters, Nyquist Aliasing, and Cache-Line Alignment

Before touching the motor drive firmware, Maya gestures toward the welding robot's inverter drive cabinet.

*"Dev,"* Maya says, *"when an inverter switches high-voltage DC into three-phase motor windings, or when an analog voltage becomes a digital sample inside a microcontroller, we are translating between the continuous physical universe and discrete digital time. If your discrete time steps do not respect the physical time constants of the hardware, the physics will bite back: motors whine, high frequencies fold into phantom vibrations, and memory buses stall."*

### Hardware Timer Prescaler Division for Human-Scale PWM

In high-power motion control, electric motors are not driven by continuous linear power amplifiers; linear amplifiers would dissipate enormous amounts of heat across their power transistors ($P = (V_{\text{supply}} - V_{\text{motor}}) \cdot I$), instantly destroying the electronics.

Instead, motors are driven by **Pulse-Width Modulation (PWM)** using power MOSFETs or Silicon Carbide (SiC) switches. The switches operate exclusively in two low-loss states: fully on (near-zero resistance, near-zero voltage drop) or fully off (zero current). By varying the ratio of on-time to total switching period—the **duty cycle**—the motor windings receive an effective average DC or sinusoidal voltage.

However, the choice of PWM carrier frequency involves a severe engineering trade-off:
1. **The Acoustic Nightmare of Low Frequencies ($1\text{ kHz}$ to $8\text{ kHz}$)**:
   In alternating magnetic fields, ferromagnetic core laminations inside motors expand and contract due to **magnetostriction**. When driven by a $4\text{ kHz}$ PWM carrier, the stator teeth vibrate like microscopic speaker diaphragms, emitting a piercing, deafening whistle that causes severe auditory fatigue for plant operators and technicians.
2. **The Thermal Penalty of Ultrasonic Frequencies ($> 20\text{ kHz}$)**:
   Increasing the PWM carrier above $20\text{ kHz}$ pushes the acoustic noise beyond the range of human hearing ($20\text{ Hz}$ to $20\text{ kHz}$), silencing the drive. However, every time a power transistor switches, it passes through a brief linear transition region where both voltage and current are simultaneously high. The average switching power loss is directly proportional to switching frequency:
   $$P_{\text{sw}} = \frac{1}{2} V_{\text{bus}} I_{\text{load}} (t_{\text{rise}} + t_{\text{fall}}) f_{\text{PWM}}$$
   Doubling the PWM frequency doubles the switching heat generated in the power stage, requiring larger heatsinks and forced-air cooling.

To balance acoustic silence against switching losses, modern servo drives standardize on an ultrasonic carrier of exactly $20.0\text{ kHz}$. To synthesize this carrier from a high-speed peripheral bus clock ($f_{\text{clk}} = 168\text{ MHz}$), the embedded engineer must divide the master clock through two hardware stages: an integer **Prescaler ($P$)** and an **Auto-Reload Register ($\text{ARR}$)**. Sizing these registers requires precise integer division on the stack.

### Mixed-Signal ADC Quantization Noise Floor and the 6.02N Rule

Dev points to the vibration sensor on the robot spindle. *"Maya, the sensor output is an analog voltage between $0\text{ V}$ and $3.3\text{ V}$. When the ADC converts this voltage into a 12-bit number, how much information are we losing?"*

An Analog-to-Digital Converter (ADC) maps an infinite continuum of analog voltages into a finite set of discrete digital codes:
- An $N$-bit converter has exactly $2^N$ code bins.
- For a 12-bit converter: $2^{12} = 4{,}096\text{ discrete levels}$.
- Across a full-scale reference voltage of $V_{\text{ref}} = 3.30\text{ V}$, each digital code represents a voltage interval known as the **Least Significant Bit ($V_{\text{LSB}}$)**:
  $$V_{\text{LSB}} = \frac{V_{\text{ref}}}{2^N} = \frac{3.30\text{ V}}{4{,}096} \approx 0.00080566\text{ V} = 805.66\ \mu\text{V}$$

Because any analog voltage falling within a given $V_{\text{LSB}}$ interval is assigned the exact same digital code, quantization introduces an unavoidable deterministic error bounded by $\pm \frac{1}{2} V_{\text{LSB}}$.

Assuming an input signal that spans many quantization levels with uniform probability, this quantization error behaves like an uncorrelated white noise source with a uniform probability distribution over $[-V_{\text{LSB}}/2, +V_{\text{LSB}}/2]$.

The root-mean-square (RMS) quantization noise voltage is:
$$V_{q,\text{rms}} = \sqrt{\frac{1}{V_{\text{LSB}}} \int_{-V_{\text{LSB}}/2}^{+V_{\text{LSB}}/2} x^2 \, dx} = \frac{V_{\text{LSB}}}{\sqrt{12}}$$

For a full-scale sinusoidal input of peak amplitude $V_{\text{ref}} / 2$, the signal's RMS voltage is:
$$V_{\text{signal,rms}} = \frac{V_{\text{ref}}}{2\sqrt{2}} = \frac{2^N \cdot V_{\text{LSB}}}{2\sqrt{2}}$$

Computing the ratio of signal power to noise power and converting to decibels yields the legendary **6.02N Rule** of mixed-signal engineering:
$$\text{SNR}_{\text{ideal}} = 20 \log_{10}\!\left(\frac{V_{\text{signal,rms}}}{V_{q,\text{rms}}}\right) = 20 \log_{10}\!\left(\frac{2^N \cdot \sqrt{12}}{2\sqrt{2}}\right) = 20 \log_{10}(2^N) + 20 \log_{10}(\sqrt{1.5})$$
$$\text{SNR}_{\text{ideal}} = 6.0206 N + 1.7609\text{ dB}$$

For an ideal 12-bit converter:
$$\text{SNR}_{\text{ideal}} = 6.0206(12) + 1.7609 \approx \mathbf{74.007\text{ dB}}$$

In real-world silicon, thermal noise, clock jitter, and integral non-linearity (INL) degrade this performance. Manufacturers characterize actual converter performance using the **Effective Number of Bits (ENOB)**, computed from measured Signal-to-Noise-and-Distortion ($\text{SINAD}$):
$$\text{ENOB} = \frac{\text{SINAD}_{\text{dB}} - 1.7609}{6.0206}$$
If an electrical transient or noisy ground plane reduces $\text{SINAD}$ to $62.0\text{ dB}$, the 12-bit ADC delivers only $10.0$ effective bits of resolution—wasting the bottom two bits on noise.

### The Nyquist-Shannon Theorem, Frequency Folding, and Anti-Aliasing Settling

Maya points to the protocol analyzer showing the $2.0\text{ kHz}$ vibration fault. *"Why is the vibration node reporting a $2.0\text{ kHz}$ bearing spike when physical mechanical inspection shows the spindle is rotating smoothly?"*

The answer lies in the **Nyquist-Shannon Sampling Theorem**.

The theorem states that a continuous analog signal can be completely and unambiguously reconstructed from its discrete samples if and only if the sampling frequency $f_s$ is strictly greater than twice the highest frequency component $f_{\max}$ present in the signal:
$$f_s > 2 f_{\max} \iff f_{\text{Nyquist}} = \frac{f_s}{2}$$

The critical frequency $f_{\text{Nyquist}} = f_s / 2$ is the **Nyquist folding boundary**.

What happens if the analog input contains high-frequency signals above $f_{\text{Nyquist}}$?

Those high frequencies do **not** disappear. Instead, they are reflected (folded) across the Nyquist boundary back into the audible baseband. The apparent frequency $f_{\text{alias}}$ observed by the digital processor is:
$$f_{\text{alias}} = |k \cdot f_s - f_{\text{signal}}|$$
Where $k$ is an integer chosen such that $0 \le f_{\text{alias}} \le f_s / 2$.

In our robot arm:
- The vibration sensor is sampled at $f_s = 25.0\text{ kSPS}$ ($25{,}000\text{ samples/s}$).
- The Nyquist frequency is $f_{\text{Nyquist}} = 25.0 / 2 = 12.5\text{ kHz}$.
- The motor inverter's fast switching edges emit electromagnetic radiation with a strong switching harmonic at $f_{\text{harmonic}} = 23.0\text{ kHz}$.
- Because $23.0\text{ kHz} > 12.5\text{ kHz}$, the inverter noise folds across the Nyquist boundary:
  $$f_{\text{alias}} = |25.0\text{ kHz} - 23.0\text{ kHz}| = \mathbf{2.0\text{ kHz}}$$

The digital processor reads an apparent, high-amplitude $2.0\text{ kHz}$ sine wave. The software reports spindle bearing vibration at $2.0\text{ kHz}$, triggering a false Emergency Stop. In reality, the mechanical spindle was stable—the apparent vibration was an artifact of mathematical aliasing.

Once an analog signal is sampled, **aliasing cannot be removed by digital filtering or software**. Both the true $2.0\text{ kHz}$ signal and the aliased $2.0\text{ kHz}$ component occupy the exact same discrete-time frequency. Anti-aliasing filtering must occur **in the physical analog domain before the ADC sampling switch**.

Furthermore, the external RC filter must satisfy a demanding physical settling constraint:
Inside a Successive Approximation Register (SAR) ADC, the input stage consists of an analog sampling switch ($R_{\text{sw}} \approx 1\text{ k}\Omega$) and an internal capacitive DAC ($C_{\text{adc}} \approx 8\text{ pF}$). When the sampling switch closes during the acquisition window ($t_{\text{acq}}$), the external circuit must charge the internal capacitor from whatever voltage was left by the previous conversion.

To achieve 12-bit accuracy, the voltage across $C_{\text{adc}}$ must settle to within **half a Least Significant Bit ($\frac{1}{2}\text{ LSB}$)** of the true input voltage. The fractional error following an exponential step response is $e^{-t / \tau}$. Setting this error less than $\frac{1}{2^{N+1}}$:
$$e^{-t_{\text{acq}} / \tau} \le \frac{1}{2^{N+1}} \iff t_{\text{acq}} \ge (N + 1) \ln(2) \cdot \tau$$

For a 12-bit ADC ($N = 12$):
$$(12 + 1) \ln(2) = 13 \times 0.693147 \approx \mathbf{9.011 \tau}$$

The acquisition window must last at least **9.01 time constants**. If the external filter resistance $R$ is too large, the time constant $\tau = R C$ stretches out, the capacitor fails to settle within $t_{\text{acq}}$, and the ADC readings suffer severe gain error and crosstalk between channels.

### Memory-Bus Alignment and Cache-Line Bounding

Finally, Maya examines the software memory layout. The DMA engine is dropping packets because circular ring buffers cross memory bus alignment boundaries.

In modern 32-bit and 64-bit microprocessors, memory is not accessed as individual isolated bytes. The physical silicon bus consists of 32 or 64 parallel copper traces that read and write data in aligned **words** (4 bytes) or **double-words** (8 bytes):
- A 32-bit word access must begin at an address divisible by 4 (address ending in `00` binary).
- A 64-bit access must begin at an address divisible by 8 (address ending in `000` binary).
- High-performance DMA burst transactions and processor cache lines operate on 16-byte, 32-byte, or 64-byte boundaries.

When an unaligned access occurs (for example, attempting to read a 32-bit integer from address `0x20000003`):
1. On architectures with strict alignment enforcement (such as ARM Cortex-M0 or Cortex-M4 when the `UNALIGN_TRP` bit in the Configuration and Control Register `CCR` is set), the CPU immediately generates a hardware **UsageFault exception**, halting execution.
2. On architectures that support unaligned access in hardware (such as x86 or ARM Cortex-M4 by default), the internal bus interconnect must execute **two separate bus read cycles**, fetch two adjacent 32-bit words, shift the bytes, and merge them in a temporary register. This doubles bus traffic, wastes memory bandwidth, and destroys atomic multi-threaded operations.

Furthermore, high-speed Direct Memory Access (DMA) controllers require circular ring buffers to be sized to an exact **power of two** ($2^K$). Why?
Because when a circular buffer size is an exact power of two, wrapping the buffer pointer from the end back to the beginning requires only a single, single-cycle bitwise AND operation:
$$\text{next\_ptr} = (\text{ptr} + 1) \ \& \ (2^K - 1)$$
If the buffer size is an arbitrary integer (such as $300\text{ bytes}$), wrapping the pointer requires an integer division or modulo instruction (`%`), which consumes multiple clock cycles and introduces execution jitter in high-speed interrupt service routines.

---

## Hardware Timer Prescalers, Mixed-Signal ADC Quantization, and RC Settling

### Hardware Timer Prescalers and Pulse-Width Modulation Carrier Synthesis

A hardware timer divides the peripheral bus clock $f_{\text{clk}}$ through an integer **Prescaler ($P$)** to generate the counter tick rate $f_{\text{tick}} = f_{\text{clk}} / P$. The timer counter then counts up to an integer **Auto-Reload Period ($\text{ARR}$)**, synthesizing a PWM carrier frequency $f_{\text{PWM}}$:

**Eq. 9.1 — Pulse-Width Modulation Carrier Frequency**
$$f_{\text{PWM}} = \frac{f_{\text{clk}}}{P \cdot \text{ARR}} \iff \text{ARR} = \frac{f_{\text{clk}}}{P \cdot f_{\text{PWM}}}$$

Where:
- $f_{\text{clk}}$ is the peripheral bus clock frequency (in $\text{Hz}$).
- $P$ is the integer timer prescaler ($P \ge 1$; in ARM timer registers, the register value is loaded with $P - 1$).
- $\text{ARR}$ is the timer auto-reload register value ($\text{ARR} \ge 1$).
- $f_{\text{PWM}}$ is the synthesized PWM carrier frequency (in $\text{Hz}$).

In motor drives, center-aligned (up-down) counting is used to eliminate odd harmonics and reduce electromagnetic interference. In center-aligned mode, the counter counts up to $\text{ARR}$ and then counts down to $0$, doubling the effective period:
$$f_{\text{PWM, center}} = \frac{f_{\text{clk}}}{2 \cdot P \cdot \text{ARR}}$$

The duty cycle is controlled by the Capture/Compare Register ($\text{CCR}$):
$$\text{Duty\%} = \left(\frac{\text{CCR}}{\text{ARR}}\right) \times 100\%$$

On a $f_{\text{clk}} = 168\text{ MHz}$ bus, targeting an ultrasonic $f_{\text{PWM}} = 20.0\text{ kHz}$ carrier with prescaler $P = 4$ in edge-aligned mode:
$$\text{ARR} = \frac{168{,}000{,}000}{4 \times 20{,}000} = \frac{168{,}000{,}000}{80{,}000} = \mathbf{2{,}100\text{ counts}}$$

The timer period register is programmed with $2{,}100$, providing an outstanding duty cycle resolution of $1$ part in $2{,}100$ ($\approx 0.0476\%$).

### Successive-Approximation Quantization, ENOB, and Half-LSB RC Settling

An $N$-bit Analog-to-Digital Converter partitions full-scale reference voltage $V_{\text{ref}}$ into $2^N$ uniform quantization intervals of width $V_{\text{LSB}}$, mapping analog voltage $V_{\text{in}} \in [0, V_{\text{ref}})$ to digital integer code $D \in [0, 2^N - 1]$:

**Eq. 9.2 — Successive-Approximation ADC Quantization**
$$V_{\text{LSB}} = \frac{V_{\text{ref}}}{2^N}$$
$$D = \left\lfloor \frac{V_{\text{in}}}{V_{\text{LSB}}} \right\rfloor = \left\lfloor \frac{V_{\text{in}}}{V_{\text{ref}}} \cdot 2^N \right\rfloor$$

To prevent aliasing and satisfy sample-and-hold acquisition requirements, the analog front end incorporates a low-pass resistor-capacitor filter:

**Eq. 9.3 — Resistor-Capacitor Filter Cutoff and Exponential Settling**
$$\tau = R \cdot C$$
$$f_c = \frac{1}{2\pi R C}$$
$$v(t) = V_0 e^{-t/\tau}$$

Where:
- $\tau$ is the RC time constant (in seconds).
- $f_c$ is the $-3\text{ dB}$ filter cutoff frequency (in $\text{Hz}$).
- $v(t)$ governs exponential settling during capacitor charging and discharging.

To guarantee that tracking error drops below $\frac{1}{2}\text{ LSB}$ during ADC acquisition time $t_{\text{acq}}$, the maximum allowable time constant is bounded by:
$$t_{\text{acq}} \ge (N + 1) \ln(2) \cdot \tau \implies \tau \le \frac{t_{\text{acq}}}{(N + 1) \ln(2)}$$

Given a 12-bit ADC ($N = 12$) with an acquisition window of $t_{\text{acq}} = 1.0\ \mu\text{s}$ and sampling capacitance $C_{\text{adc}} = 10\text{ pF}$ ($10^{-11}\text{ F}$):
$$\tau_{\max} = \frac{1.0 \times 10^{-6}}{13 \times \ln(2)} \approx \frac{1.0 \times 10^{-6}}{9.011} \approx 1.1097 \times 10^{-7}\text{ s} \approx 111\text{ ns}$$

The maximum allowable source resistance driving the ADC is:
$$R_{\max} = \frac{\tau_{\max}}{C_{\text{adc}}} = \frac{1.1097 \times 10^{-7}}{10 \times 10^{-12}} \approx \mathbf{11{,}097\ \Omega} \approx 11.1\text{ k}\Omega$$

If the sensor's output impedance exceeds $11.1\text{ k}\Omega$, an operational amplifier buffer or a smaller series resistor must be used to prevent conversion errors.

### Population Count, Hamming Distance, and Count Leading Zeros

The SC-16 provides dedicated hardware bit-manipulation primitives essential for digital signal processing, cryptography, and network subnetting:
1. **Population Count (`POPCNT`, `{{key:#B}}`)**:
   Counts the total number of set `1` bits within an active register word.
   - Used to verify bitmask densities, evaluate error-correcting codes, and compute **Hamming Distance**:
     $$\text{Hamming\_Distance}(A, B) = \text{POPCNT}(A \oplus B)$$
2. **Count Leading Zeros (`CLZ`, `{{key:CLZ}}`)**:
   Counts the number of consecutive zero bits starting from the Most Significant Bit (MSB).
   - In floating-point normalization and fixed-point math, `CLZ` identifies the exact shift count required to normalize an integer significand in a single cycle.
   - Computes integer base-2 logarithm:
     $$\lfloor \log_2 X \rfloor = (W - 1) - \text{CLZ}(X)$$
     Where $W$ is the register word width (32 for a double-word).
3. **Count Trailing Zeros (`CTZ`)**:
   Counts the number of consecutive zero bits starting from the Least Significant Bit (LSB).
   - Identifies the lowest set bit in real-time operating system (RTOS) priority schedulers.

---

## Classless Inter-Domain Routing Subnets and Memory Bus Alignment

### Prefix Bitmasks, Usable Host Capacity, and Broadcast Boundaries

In industrial automation networks, operational technology (OT) sensors and programmable logic controllers (PLCs) are isolated into dedicated IP subnets to prevent broadcast storms and cyber intrusion.

Under **Classless Inter-Domain Routing (CIDR)**, a subnet is specified by its base IP address followed by a prefix length $P \in [0, 32]$, representing the number of contiguous leading `1` bits in the 32-bit network mask.

The governing equations for netmask synthesis and usable host capacity are:

**Eq. 9.4 — Classless Inter-Domain Routing Host Capacity**
$$\text{Block Size} = 2^{32 - P}$$
$$N_{\text{hosts}} = 2^{32 - P} - 2 \quad (0 \le P \le 30)$$

Where:
- $P$ is the CIDR prefix length ($0 \le P \le 32$).
- $\text{Block Size}$ is the total number of IPv4 addresses in the CIDR block.
- $N_{\text{hosts}}$ is the number of usable host addresses.
- The two reserved addresses are:
  - **Subnet Network ID** (all host bits `0`): Identifies the subnet itself.
  - **Subnet Broadcast Address** (all host bits `1`): Broadcasts to all nodes on the subnet.

For the factory floor vibration cluster requiring 54 sensor nodes plus gateway:
- Sizing a `/26` subnet ($P = 26$):
  - Host bits: $H = 32 - 26 = 6\text{ bits}$.
  - Block size: $2^6 = 64\text{ addresses}$.
  - Usable hosts: $N_{\text{hosts}} = 64 - 2 = \mathbf{62\text{ hosts}}$.
  - Netmask: `0xFFFFFFC0` ($255.255.255.192$).
- The 62 usable addresses easily accommodate the 54 vibration nodes and the gateway router with 7 spare IP addresses.

### Power-of-Two DMA Ring Buffers and Natural Structure Alignment

Inside microcontroller SRAM, high-speed DMA controllers and CPU cache lines require memory buffers and data structures to align to natural power-of-two address boundaries:

**Eq. 9.5 — Natural Power-of-Two Memory Bus Alignment**
$$A_{\text{aligned}} = \left\lceil \frac{A}{B} \right\rceil \times B = (A + B - 1) \ \& \ \sim(B - 1)$$
$$S_{\text{pow2}} = 2^{\lceil \log_2 S \rceil}$$

Where:
- $A$ is the raw byte address or structure length.
- $B$ is the power-of-two alignment boundary ($B \in \{2, 4, 8, 16, 32, 64, 4096\}$).
- $A_{\text{aligned}}$ is the aligned byte address rounded up to the nearest multiple of $B$.
- $S_{\text{pow2}}$ is the buffer capacity rounded up to the next power of two.
- $\&$ is bitwise AND, and $\sim$ is bitwise NOT.

For example, a raw vibration telemetry packet descriptor is 53 bytes long ($A = 53$). To align this descriptor to a 16-byte DMA burst boundary ($B = 16$):
$$A_{\text{aligned}} = (53 + 16 - 1) \ \& \ \sim(16 - 1) = 68 \ \& \ \sim(15) = 68 \ \& \ \text{0xFFFFFFF0} = \mathbf{64\text{ bytes}}$$

The compiler inserts $11\text{ bytes}$ of padding, ensuring that every packet descriptor begins cleanly on a 16-byte burst boundary.

Furthermore, a circular sample queue requiring at least $300\text{ bytes}$ ($S = 300$) rounds up to the next power of two via Eq. 9.5:
$$\lceil \log_2(300) \rceil = \lceil 8.2288 \rceil = 9 \implies S_{\text{pow2}} = 2^9 = \mathbf{512\text{ bytes}}$$

Allocating $512\text{ bytes}$ ($0.5\text{ KiB}$) ensures pointer wrapping via `next_ptr = (ptr + 1) & 511`, eliminating integer division entirely.

### High-Speed Synchronous Bus Timing and Hold-Time Violations

When interfacing microcontrollers with external high-speed peripherals (such as Quad-SPI Flash memory or external ADC ICs), signals must satisfy strict synchronous timing requirements:
1. **Setup Time ($t_{\text{su}}$)**: The minimum time the data signal must remain stable before the active clock latching edge arrives.
2. **Hold Time ($t_{\text{h}}$)**: The minimum time the data signal must remain stable after the active clock edge has passed.

The operational margins for a synchronous digital interface are:

**Eq. 9.6 — High-Speed Synchronous Bus Timing Margins**
$$t_{\text{margin,setup}} = T_{\text{clk}} - t_{\text{co,\max}} - t_{\text{prop,\max}} - t_{\text{su}} \ge 0$$
$$t_{\text{margin,hold}} = t_{\text{co,\min}} + t_{\text{prop,\min}} - t_{\text{h}} - \Delta t_{\text{skew}} \ge 0$$

Where:
- $T_{\text{clk}} = 1 / f_{\text{clk}}$ is the clock period.
- $t_{\text{co}}$ is the transmitter's clock-to-output propagation delay.
- $t_{\text{prop}}$ is the electromagnetic flight time along the PCB trace ($\approx 160\text{ ps/in}$ on FR-4 substrate).
- $\Delta t_{\text{skew}}$ is the clock skew between transmitter and receiver.

Look carefully at the hold margin equation:
$$t_{\text{margin,hold}} = t_{\text{co,\min}} + t_{\text{prop,\min}} - t_{\text{h}} - \Delta t_{\text{skew}}$$

Crucially, **clock period $T_{\text{clk}}$ does not appear in the hold margin equation**.
If a high-speed bus suffers from a hold-time violation ($t_{\text{margin,hold}} < 0$), **slowing down the clock will not fix it**. A hold violation means new data is arriving at the receiver before the previous data has been latched. The only fixes are physical PCB trace redesign, adding trace length to delay the data line, or adding series buffer delay gates.

### Metastability and Clock Domain Crossing (CDC)

When an asynchronous external signal violates either setup time or hold time, the internal bistable latch inside the receiving flip-flop enters a state of **Metastability**.

In a metastable state, the flip-flop's internal output does not settle cleanly to logic `0` or logic `1`; instead, it hovers at an intermediate, indeterminate voltage ($V_{\text{DD}} / 2$) for an unpredictable duration before thermal noise eventually tips it into one state or the other.

If downstream combinational logic reads this indeterminate voltage, different logic gates can interpret the same signal as different Boolean values simultaneously, causing processor faults.

The reliability of a synchronizer is quantified by its **Mean Time Between Failures (MTBF)**:
$$\text{MTBF} = \frac{e^{t_{\text{resolve}} / \tau_m}}{T_0 \cdot f_{\text{clk}} \cdot f_{\text{data}}}$$
Where:
- $t_{\text{resolve}}$ is the available settling time.
- $\tau_m$ and $T_0$ are empirical silicon process parameters.
- $f_{\text{clk}}$ is the receiving clock frequency.
- $f_{\text{data}}$ is the asynchronous data transition rate.

To protect against metastability on single-bit asynchronous inputs (such as pushbuttons or external interrupts), engineers use a **Dual-Rank (Two-Flop) Synchronizer**:
```
Asynchronous       +-------+     Q1     +-------+     Synchronized
Input ------------>| D   Q |----------->| D   Q |----> Output
                   |  FF1  |            |  FF2  |
Clock ------------>|>      |        +-->|>      |
                   +-------+        |   +-------+
                       |            |
                       +------------+
```
The first flip-flop (FF1) captures the asynchronous signal and may go metastable. However, it has an entire clock cycle ($T_{\text{clk}}$) for its internal nodes to resolve before the second flip-flop (FF2) samples its output, increasing MTBF from microseconds to centuries.

On multi-bit buses (such as a 16-bit ADC data bus or FIFO pointers), dual-rank synchronizers cannot be applied bit-by-bit. Because slight trace length differences cause bits to transition with slight skew, FF1 would sample some bits before the transition and some bits after, generating an illegal intermediate binary word.

To safely transfer multi-bit counters across asynchronous clock domains, systems architects use **Gray Code Counters**. In a Gray code sequence, **exactly one bit changes state per count increment**:

```
Binary:    0000 -> 0001 -> 0010 -> 0011 -> 0100
Gray Code: 0000 -> 0001 -> 0011 -> 0010 -> 0110
```

Because only a single bit changes on each clock tick, a clock domain crossing cannot produce an illegal multi-bit state. If the receiver samples during the transition, it either captures the old value or the new value—both of which are valid.

---

## Configuring Timer PWM, the Vibration Node, and Subnet Block on the Stack

On the SC-16, embedded digital engineering is supported by dedicated hardware stack operations and multi-variable equation solvers.

| Button | Operation | Register Z | Register Y | Register X | Governing Expression |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`{{key:PWM}}`** | PWM Carrier Frequency Solver | Bus Clock $f_{\text{clk}}$ | Prescaler $P$ | Auto-Reload $\text{ARR}$ | $f_{\text{PWM}} = f_{\text{clk}} / (P \cdot \text{ARR})$ (Eq. 9.1) |
| **`{{key:ADC}}`** | SAR ADC Quantization Solver | Ref Voltage $V_{\text{ref}}$ | Bits $N$ | Analog Voltage $V_{\text{in}}$ | $D = \lfloor (V_{\text{in}} / V_{\text{ref}}) \cdot 2^N \rfloor$ (Eq. 9.2) |
| **`{{key:τ}}`** | RC Time Constant Solver | Resistance $R$ | Capacitance $C$ | Cutoff $f_c$ / Time $t$ | $\tau = RC,\; f_c = 1/(2\pi RC)$ (Eq. 9.3) |
| **`{{key:NET}}`** | CIDR Netmask and Host Sizing | — | Prefix $P$ | Usable Hosts | Pushes Netmask to $Y$, host capacity to $X$ (Eq. 9.4) |
| **`{{key:ALN}}`** | Memory Bus Alignment & Rounding | — | Base Address $A$ | Boundary $B$ | $(A + B - 1) \ \& \ \sim(B - 1)$ (Eq. 9.5) |
| **`{{key:CLZ}}`** / **`{{key:#B}}`** | Count Leading Zeros / Popcount | — | — | Word $X$ | Bitfield analysis primitives |

### Synthesizing PWM Carrier Frequencies and Quantizing the Vibration Sensor on the Stack

To verify the $1{,}000.0\text{ Hz}$ PWM carrier (`48000000` {{key:ENTER}} `48` {{key:ENTER}} `1000` {{key:PWM}}), compute the 12-bit vibration sensor {{key:ADC}} step size at $V_{\text{ref}} = 3.30\text{ V}$ (`3.3` {{key:ENTER}} `12` {{key:ADC}} `1000` {{key:×}} $\to \mathbf{0.8057\text{ mV/LSB}}$), and inspect the set bits ({{key:#B}}) and leading zeros ({{key:CLZ}}) of the 32-bit word `0x41440000`, the architect executes:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| {{key:DEC}} `48000000` {{key:ENTER}} `48` {{key:ENTER}} `1000` {{key:PWM}} {{key:C}} | $0$ | $0$ | $0$ | $1000$ | 3-arg stack shortcut: $f_{\text{PWM}} = 48{,}000{,}000 / (48 \times 1000) = 1{,}000\text{ Hz}$ |
| `3.3` {{key:ENTER}} `12` {{key:ADC}} {{key:C}} `1000` {{key:×}} | $0$ | $0$ | $1000$ | $0.8057$ | Compute 12-bit step size $V_{\text{LSB}} = (3.3 / 4096) \times 1000 \approx 0.8057\text{ mV}$ |
| `1650` {{key:x⇄y}} {{key:÷}} | $0$ | $0$ | $1000$ | $2048$ | Divide $1{,}650\text{ mV}$ input by $V_{\text{LSB}}$ to obtain mid-scale code $D = 2{,}048$ |
| `32` {{key:WSZ}} {{key:HEX}} `41440000` {{key:ENTER}} {{key:#B}} | $2048$ | $32$ | $\text{0x41440000}$ | $\text{0x4}$ | Count set `1` bits in `0x41440000` ({{key:#B}} $= 4$) |
| {{key:x⇄y}} {{key:CLZ}} | $2048$ | $32$ | $\text{0x4}$ | **$\text{0x1}$** | Count leading zeros of `0x41440000` in 32-bit register ({{key:CLZ}} $= 1$) |

### Solving Backward in the {{key:PWM}}, {{key:ADC}}, and {{key:τ}} Workspaces

When configuring the $20\text{ kHz}$ ultrasonic servo timer on a $168\text{ MHz}$ bus ({{key:PWM}} workspace `F = C / (P × A)`), inverting a raw 12-bit DMA accelerometer code $D = 2{,}894$ ({{key:ADC}} workspace `D = V / R × 2^N`, pre-populated with $R = 3.3\text{ V}$ and $N = 12$), or sizing the anti-aliasing series resistor $R$ driving a $C = 1.0\text{ nF}$ ($10^{-9}\text{ F}$) capacitor for $\tau = 1.0\ \mu\text{s}$ ({{key:τ}} workspace `T = R × C`), the architect solves directly for the unknown parameter:

| Keystroke | Solver Display / Register X | What Happens in the {{key:PWM}}, {{key:ADC}}, & {{key:τ}} Workspaces |
| :--- | :---: | :--- |
| {{key:DEC}} `0` {{key:ENTER}} `0` {{key:PWM}} | `F = C / (P × A)` | Open the {{key:PWM}} Solver Workspace (`PWM: TIMER FREQ`) |
| `168000000` {{keycap:C}} `4` {{keycap:P}} `20000` {{keycap:F}} | $20{,}000.0000$ | Bind $C = 168\text{ MHz}$, $P = 4$, and $F = 20\text{ kHz}$ |
| {{key:SOLVE}} {{keycap:A}} | **$2{,}100.0000$** | Solve backward for 16-bit auto-reload period $A = 168{,}000{,}000 / (4 \times 20{,}000) = \mathbf{2{,}100}$ |
| `0` {{key:ENTER}} `0` {{key:ADC}} | `D = V / R × 2^N` | Open the {{key:ADC}} Solver Workspace (pre-populated with $R = 3.3\text{ V}$, $N = 12$) |
| `2894` {{keycap:D}} | $2{,}894.0000$ | Store the captured DMA sample register code $D = 2{,}894$ into softkey {{keycap:D}} |
| {{key:SOLVE}} {{keycap:V}} | **$2.3316$** | Solve backward for analog input voltage $V = 2894 \times 3.3 / 2^{12} = \mathbf{2.3316\text{ V}}$ |
| `0` {{key:ENTER}} `0` {{key:τ}} | `T = R × C` | Open the RC Time Constant ({{key:τ}}) Solver Workspace with softkeys {{keycap:T}}, {{keycap:R}}, {{keycap:C}} |
| `1` {{key:E}} `6` {{key:+/-}} {{keycap:T}} `1` {{key:E}} `9` {{key:+/-}} {{keycap:C}} | $1.0000 \times 10^{-9}$ | Store target time constant $T = 1.0\ \mu\text{s}$ into {{keycap:T}} and $C = 1.0\text{ nF}$ into {{keycap:C}} |
| {{key:SOLVE}} {{keycap:R}} | **$1{,}000.0000$** | Solve backward for anti-aliasing series resistance $R = T / C = \mathbf{1{,}000\ \Omega}$ ($1.0\text{ k}\Omega$) |

### Partitioning the Factory Subnet and Aligning DMA Packet Descriptors

In {{key:DEC}} mode, keying `26` {{key:NET}} (or `32` {{key:ENTER}} `26` {{key:-}} {{key:2ˣ}} `2` {{key:-}}) confirms that the `/26` factory floor subnet provides $\mathbf{62}$ usable IPv4 host addresses (with netmask `4294967232` $= \text{0xFFFFFFC0}$ in Register $Y$), keying `53` {{key:ENTER}} `16` {{key:ALN}} aligns the 53-byte telemetry header up to a $\mathbf{64\text{-byte}}$ DMA boundary, and keying `0` {{key:ENTER}} `300` {{key:ALN}} rounds the 300-byte sample queue up to the next power of two at $\mathbf{512\text{ bytes}}$ ($\mathbf{0.5\text{ KiB}}$ via {{key:▸KiB}}):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| {{key:DEC}} `26` {{key:NET}} | $0$ | $0$ | $4294967232$ | $62$ | Evaluate `/26` netmask in $Y$ (`0xFFFFFFC0`) and $62$ usable IPv4 hosts in $X$ |
| `22` {{key:NET}} | $4294967232$ | $62$ | $4294966272$ | $1022$ | Evaluate plant-wide `/22` supernet netmask in $Y$ and $1{,}022$ usable hosts in $X$ |
| `53` {{key:ENTER}} `16` {{key:ALN}} | $4294967232$ | $4294966272$ | $1022$ | $64$ | Align 53-byte packet descriptor up to 16-byte boundary ($64\text{ bytes}$) |
| `0` {{key:ENTER}} `300` {{key:ALN}} | $1022$ | $64$ | $0$ | **$512$** | Round 300-byte DMA ring request up to next power of two ($512\text{ bytes}$) |

### Designing a 12-Bit ADC Vibration Filter and Aligning DMA Ring Descriptors on the Stack

On Robot Arm 3, the vibration sensor's analog input must be filtered to reject the $23.0\text{ kHz}$ inverter switching harmonic while settling to within $\frac{1}{2}\text{ LSB}$ during the $t_{\text{acq}} = 1.0\ \mu\text{s}$ acquisition window. The sampling capacitance is $C_{\text{adc}} = 10\text{ pF}$. Furthermore, the DMA engine needs a circular buffer to hold 1,200 samples of 16-bit vibration data, aligned to a 64-byte processor cache line. Maya guides Dev through the complete stack verification:

```
Step 1: Calculate maximum allowable settling time constant:
        tau_max = t_acq / ((N + 1) * ln(2)) = 1.0 us / (13 * 0.693147) = 110.97 ns
Step 2: Sizing maximum series resistance for C_adc = 10 pF:
        R_max = tau_max / C_adc = 110.97 ns / 10 pF = 11,097 ohms
Step 3: Anti-aliasing filter cutoff with R = 1.0 k-ohm and C_ext = 10 nF:
        f_c = 1 / (2 * pi * 1000 * 10e-9) = 15,915 Hz (15.92 kHz)
        Attenuates 23 kHz harmonic by -6.2 dB prior to sampling.
Step 4: Sizing circular DMA buffer: 1,200 samples * 2 bytes/sample = 2,400 bytes.
Step 5: Round buffer up to next power of two:
        ceil(log2(2400)) = 12 -> 2^12 = 4,096 bytes (4.0 KiB).
Step 6: Align buffer base address to 64-byte cache line:
        Aligning address 0x20000042 up to 64-byte boundary yields 0x20000080.
```

| Keystroke Sequence | Reg T | Reg Z | Reg Y | Reg X | Engineering Explanation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:DEC}} 1 {{key:E}} 6 {{key:+/-}} {{key:ENTER}}` | $0$ | $0$ | $0$ | $1.0 \times 10^{-6}$ | Enter acquisition window $t_{\text{acq}} = 1.0\ \mu\text{s}$ |
| `13 {{key:ENTER}} 2 {{key:sc32:LN}} {{key:×}} {{key:÷}}` | $0$ | $0$ | $1.0 \times 10^{-6}$ | **`1.1097e-7`** | Divide by $13 \ln(2)$: maximum settling $\tau_{\max} \approx 110.97\text{ ns}$ |
| `10 {{key:E}} 12 {{key:+/-}} {{key:÷}}` | $0$ | $0$ | $1.1097 \times 10^{-7}$ | **`11097.3`** | Divide by $C_{\text{adc}} = 10\text{ pF}$: maximum $R_{\max} \approx \mathbf{11{,}097\ \Omega}$ |
| `1000 {{key:ENTER}} 10 {{key:E}} 9 {{key:+/-}} {{key:×}} 2 {{key:×}} {{key:sc32:π}} {{key:×}} {{key:sc32:𝑥⁻¹}}` | $0$ | $11{,}097.3$ | $0$ | **`15915.5`** | Cutoff of $1\text{ k}\Omega$ + $10\text{ nF}$ filter: $f_c \approx \mathbf{15.92\text{ kHz}}$ |
| `1200 {{key:ENTER}} 2 {{key:×}}` | $0$ | $0$ | $15{,}915.5$ | `2400` | Sizing raw buffer: $1{,}200\text{ samples} \times 2\text{ B} = 2{,}400\text{ bytes}$ |
| `0 {{key:ENTER}} 2400 {{key:ALN}}` | $0$ | $15{,}915.5$ | $0$ | **`4096`** | Round up to power of two: buffer size is $\mathbf{4{,}096\text{ bytes}}$ ($4.0\text{ KiB}$) |
| `{{key:HEX}} 20000042 {{key:ENTER}} 40 {{key:ALN}}` | $0$ | $0$ | `0x20000042` | **`0x20000080`** | Align address `0x20000042` up to 64-byte (`0x40`) boundary: `0x20000080` |

Sizing the buffer to 4,096 bytes allows the DMA circular pointer to wrap with mask `0x0FFF`. Aligning the base address to `0x20000080` ensures that burst transactions remain within a single 64-byte cache line.

Maya programs the new $20.0\text{ kHz}$ PWM timer period, solders the $1\text{ k}\Omega$ series resistor into the vibration front end, and activates the `/26` subnet gateway. The robot arm's high-pitched acoustic whine vanishes instantly, replaced by a smooth, imperceptible hum. The false $2.0\text{ kHz}$ vibration alarms disappear from the SCADA terminal, and telemetry packets flow across the industrial network without a single dropped frame.

---

### Try It on the Stack

Work through these five field problems on your calculator. Step-by-step keystroke solutions and register walkthroughs are provided in [Appendix C](appendix-c-solutions-to-practice-problems.md).

1. **Precision Sixteen-Bit ADC Step Resolution and Code Inversion:** A precision strain-gauge bridge uses a 16-bit ADC ($2^{16} = 65{,}536$) with a full-scale reference voltage of $V_{\text{ref}} = 2.50\text{ V}$. Calculate the step size $V_{\text{LSB}}$ in microvolts, and determine the physical voltage represented by raw digital output code `0x8C40` ($35{,}904_{10}$).
2. **CIDR Subnet Capacity and Broadcast Address Calculation:** A factory automation network is assigned IP block `10.240.16.0/22`. Calculate the total address capacity, count of usable host IPs, and the exact broadcast IP address.
3. **Cache-Line Descriptor Alignment and Power-of-Two Ring Sizing:** An Ethernet DMA ring buffer contains 128 packet descriptors, each $48\text{ bytes}$ wide. Calculate total buffer size, and determine the address alignment padding needed to align the buffer to a $64\text{-byte}$ processor cache line.
4. **High-Speed Synchronous SPI Bus Setup Timing Margin:** A high-speed SPI bus runs at $f_{\text{SCK}} = 25.0\text{ MHz}$ ($T_{\text{clk}} = 40.0\text{ ns}$). The master controller specifies maximum clock-to-output propagation delay $t_{\text{prop,max}} = 12.0\text{ ns}$, trace propagation delay $t_{\text{flight}} = 2.5\text{ ns}$, and sensor setup time $t_{\text{setup}} = 6.0\text{ ns}$. Calculate the remaining data setup timing margin across a half-clock period ($20.0\text{ ns}$).
5. **PWM Ultrasonic Auto-Reload Period Sizing:** An advanced motor drive timer clocked at $f_{\text{TIM}} = 120.0\text{ MHz}$ synthesizes a center-aligned PWM carrier frequency of $f_{\text{PWM}} = 20.0\text{ kHz}$. Calculate the required 16-bit Auto-Reload Register (ARR) value assuming zero prescaler division.

---

## Operational Baton: Handing Off from Embedded Silicon to Cinema Optics and Broadcast Media

With the vibration sensor's analog front end filtered and calibrated, timer PWM synthesis humming silently at ultrasonic frequencies, and DMA packet buffers aligned cleanly across the factory subnet, the digital embedded foundation is rock-solid.

Yet physical control, mixed-signal quantization, and data serialization represent only half the modern industrial mission. When autonomous robotic workcells, industrial inspections, and aerospace vehicles operate in the physical world, their operations must be captured, synchronized, and documented with absolute photographic precision.

In **Unit IV (Chapters 10–12)**, these discrete timing principles transition from microcontroller buses to optical glass and broadcast media:
- In **Chapter 10**, we evaluate image capture geometry: calculating circles of confusion, hyperfocal distances, depths of field, and sensor format crop factors.
- In **Chapter 11**, we synchronize high-speed motion capture against pulsed illumination, solving shutter angles, flicker-free exposure windows, photometric lux-to-footcandle conversions, and inverse-square lighting falloff.
- In **Chapter 12**, we synchronize multi-camera streams, audio recorders, and broadcast video infrastructure using SMPTE timecode arithmetic, drop-frame compensation, and audio sample-rate phase alignment.

From the register buses of embedded silicon, we turn next to the optics, exposure timing, and acoustic fields of cinema and broadcast engineering.

