# Learn by Doing: Interactive TUI Tutorials

The StackCalc32 firmware, Apple Watch app, and iOS app include 16 built-in interactive lessons powered by the native Text User Interface (TUI). 

The TUI replaces standard nested modal dialogues with an expandable, chatbot-style scrolling terminal rendered in the bundled **Terminus** pixel font. Lessons describe physical and digital calculator operations, providing real-time verification against the deterministic `RPNCore` engine.

---

## 1. Terminal Navigation & Controls

Learn how to navigate the expandable TUI scrolling transcript buffer and switch between the standard 1-line LCD and the full-screen terminal.

<div class="lcd-screen p-4 border-2 border-charcoal font-terminus shadow-md my-4" style="max-width: 650px;">
  <div class="text-xs uppercase tracking-wider text-charcoal border-b border-charcoal border-opacity-30 pb-1 flex justify-between font-bold">
    <span>&gt; TUI: CONTROLS (LESSON 1/16)</span>
    <span>[C] EXIT</span>
  </div>
  <div class="text-sm text-charcoal leading-snug space-y-1 py-2">
    <p>&gt; Terminal navigation tutorial.</p>
    <p>&gt; Use ↰ + 8 to scroll up and ↰ + 7 to scroll down.</p>
    <p>&gt; Step 1: Press Yellow Shift (↰)</p>
    <p>&gt; Step 2: Press 8 [SCROLL UP]</p>
    <p>&gt; Step 3: Press Yellow Shift (↰)</p>
    <p>&gt; Step 4: Press 7 [SCROLL DOWN]</p>
    <p class="font-bold bg-[#CBD1DC] bg-opacity-40 px-1 inline-block">&gt; VERIFIED: Transcript buffer navigation unlocked.</p>
  </div>
  <div class="pt-2 border-t border-charcoal border-opacity-30 flex justify-between items-center text-xs font-bold">
    <span class="text-xl">0.0000_</span>
    <span class="bg-charcoal text-icyblue px-2 py-0.5">[NEXT]</span>
  </div>
</div>

- **Tap ↰ (Yellow Shift)** to engage the shift annunciator.
- **Tap 8** to scroll up into previous calculation history.
- **Tap 7** to scroll down back to the active prompt.
- **Tap C** to dismiss the TUI overlay back to the primary stack view.

---

## 2. RPN Basics: Eliminating Parentheses

Reverse Polish Notation replaces the traditional `=` button and parenthesis keys with an automatic 4-level stack ($X, Y, Z, T$).

*Mission: Calculate $5 + 3$ without parentheses.*

<div class="lcd-screen p-4 border-2 border-charcoal font-terminus shadow-md my-4" style="max-width: 650px;">
  <div class="text-xs uppercase tracking-wider text-charcoal border-b border-charcoal border-opacity-30 pb-1 flex justify-between font-bold">
    <span>&gt; TUI: RPN BASICS (LESSON 2/16)</span>
    <span>[C] EXIT</span>
  </div>
  <div class="text-sm text-charcoal leading-snug space-y-1 py-2">
    <p>&gt; Mission: Calculate 5 + 3 with no parentheses.</p>
    <p>&gt; In RPN, you enter arguments first, then specify the operator.</p>
    <p>&gt; Step 1: Tap 5</p>
    <p>&gt; Step 2: Tap ENTER [Lifts 5 into Stack Register Y]</p>
    <p>&gt; Step 3: Tap 3 [Enters 3 into Stack Register X]</p>
    <p>&gt; Step 4: Tap + [Combines Y and X into X]</p>
    <p class="font-bold bg-[#CBD1DC] bg-opacity-40 px-1 inline-block">&gt; VERIFIED: X = 8.0000 [STACK LIFT ARMED]</p>
  </div>
  <div class="pt-2 border-t border-charcoal border-opacity-30 flex justify-between items-center text-xs font-bold">
    <span class="text-xl">8.0000_</span>
    <span class="bg-charcoal text-icyblue px-2 py-0.5">[NEXT]</span>
  </div>
</div>

1. **Tap 5**: Types `5_` left-justified on the LCD display.
2. **Tap ENTER**: Commits `5` to the bottom of the stack and arms stack-lift.
3. **Tap 3**: Types `3_` in the active $X$ register while $Y$ retains `5`.
4. **Tap +**: Instantly evaluates $5 + 3 = 8.0000$.

---

## 3. Complex Numbers: Euler’s Identity

StackCalc handles full complex pairs $(a + bi)$ natively across all scientific and transcendental functions.

*Mission: Verify Euler's identity: $e^{\pi i} = -1$.*

<div class="lcd-screen p-4 border-2 border-charcoal font-terminus shadow-md my-4" style="max-width: 650px;">
  <div class="text-xs uppercase tracking-wider text-charcoal border-b border-charcoal border-opacity-30 pb-1 flex justify-between font-bold">
    <span>&gt; TUI: COMPLEX PAIRS (LESSON 3/16)</span>
    <span>[C] EXIT</span>
  </div>
  <div class="text-sm text-charcoal leading-snug space-y-1 py-2">
    <p>&gt; Mission: Verify e^(πi) = −1 with complex pairs.</p>
    <p>&gt; Step 1: Tap 0 -&gt; press ENTER [Real part in Y = 0]</p>
    <p>&gt; Step 2: Tap Blue Shift -&gt; Tap SIN (π) [Imaginary part in X = 3.1416]</p>
    <p>&gt; Step 3: Tap Yellow Shift -&gt; Tap STO (CMPLX) [Arms complex operator]</p>
    <p>&gt; Step 4: Tap eˣ [Evaluates transcendental e^(0 + πi)]</p>
    <p>&gt; Step 5: Yellow Shift -&gt; STO (CMPLX) -&gt; Blue Shift -&gt; ENTER (SHOW)</p>
    <p class="font-bold bg-[#CBD1DC] bg-opacity-40 px-1 inline-block">&gt; VERIFIED: Result = −1.0000 + 0.0000i</p>
  </div>
  <div class="pt-2 border-t border-charcoal border-opacity-30 flex justify-between items-center text-xs font-bold">
    <span class="text-xl">-1.0000_</span>
    <span class="bg-charcoal text-icyblue px-2 py-0.5">[NEXT]</span>
  </div>
</div>

---

## 4. Fraction Entry & Manual Simplification ([SIMP])

Unlike consumer calculators that automatically simplify fractions and hide the underlying math from students, StackCalc preserves exact fraction state. Students must press `[SIMP]` to actively reduce fractions step-by-step.

*Mission: Enter $\frac{2}{4}$ and reduce it to $\frac{1}{2}$.*

<div class="lcd-screen p-4 border-2 border-charcoal font-terminus shadow-md my-4" style="max-width: 650px;">
  <div class="text-xs uppercase tracking-wider text-charcoal border-b border-charcoal border-opacity-30 pb-1 flex justify-between font-bold">
    <span>&gt; TUI: FRACTION SIMPLIFICATION (LESSON 5/16)</span>
    <span>[C] EXIT</span>
  </div>
  <div class="text-sm text-charcoal leading-snug space-y-1 py-2">
    <p>&gt; Mission: Enter 2/4 and reduce step-by-step.</p>
    <p>&gt; Format: [Whole] . [Numerator] . [Denominator]</p>
    <p>&gt; Step 1: Tap . -&gt; Tap 2 -&gt; Tap . -&gt; Tap 4 [.2.4]</p>
    <p>&gt; Step 2: Tap ENTER [Displays: .2.4_ without reducing]</p>
    <p>&gt; Step 3: Tap Softkey [SIMP]</p>
    <p class="font-bold bg-[#CBD1DC] bg-opacity-40 px-1 inline-block">&gt; VERIFIED: Common divisor 2 factored out -&gt; .1.2 (.1/2)</p>
  </div>
  <div class="pt-2 border-t border-charcoal border-opacity-30 flex justify-between items-center text-xs font-bold">
    <span class="text-xl">.1.2_</span>
    <span class="bg-charcoal text-icyblue px-2 py-0.5">[NEXT]</span>
  </div>
</div>

---

## 5. Mixed Fraction Arithmetic & Decimal Toggle ([FDISP])

Add mixed numbers exactly and toggle instantly between exact fractional form and floating-point decimal.

*Mission: Add $1 \frac{1}{2} + 1 \frac{3}{4} = 3 \frac{1}{4} = 3.2500$.*

<div class="lcd-screen p-4 border-2 border-charcoal font-terminus shadow-md my-4" style="max-width: 650px;">
  <div class="text-xs uppercase tracking-wider text-charcoal border-b border-charcoal border-opacity-30 pb-1 flex justify-between font-bold">
    <span>&gt; TUI: MIXED FRACTION ARITHMETIC (LESSON 6/16)</span>
    <span>[C] EXIT</span>
  </div>
  <div class="text-sm text-charcoal leading-snug space-y-1 py-2">
    <p>&gt; Mission: Add 1 1/2 + 1 3/4 exactly.</p>
    <p>&gt; Step 1: Tap 1 . 1 . 2 -&gt; Press ENTER [1 1/2 in Y]</p>
    <p>&gt; Step 2: Tap 1 . 3 . 4 [1 3/4 in X]</p>
    <p>&gt; Step 3: Tap + [Exact sum evaluated: 3 1/4]</p>
    <p>&gt; Step 4: Tap [FDISP] to toggle to decimal representation.</p>
    <p class="font-bold bg-[#CBD1DC] bg-opacity-40 px-1 inline-block">&gt; VERIFIED: 3.2500 [PRESS FDISP AGAIN TO RETURN TO 3_1/4]</p>
  </div>
  <div class="pt-2 border-t border-charcoal border-opacity-30 flex justify-between items-center text-xs font-bold">
    <span class="text-xl">3.2500_</span>
    <span class="bg-charcoal text-icyblue px-2 py-0.5">[NEXT]</span>
  </div>
</div>

---

## 6. Time Value of Money (TVM Amortization)

The built-in financial solver handles loan payments, mortgages, savings plans, and balloon notes without requiring complex algebraic formulas.

*Mission: Calculate the monthly payment on a \$200,000 30-year fixed loan at 5.5% annual interest.*

$$\text{Monthly Payment} = \frac{PV \cdot i}{1 - (1 + i)^{-N}}$$

<div class="lcd-screen p-4 border-2 border-charcoal font-terminus shadow-md my-4" style="max-width: 650px;">
  <div class="text-xs uppercase tracking-wider text-charcoal border-b border-charcoal border-opacity-30 pb-1 flex justify-between font-bold">
    <span>&gt; TUI: TVM AMORTIZATION (LESSON 8/16)</span>
    <span>[C] EXIT</span>
  </div>
  <div class="text-sm text-charcoal leading-snug space-y-1 py-2">
    <p>&gt; Loan parameters: N=360 months, I/YR=5.5%, PV=$200,000</p>
    <p>&gt; Step 1: 360 -&gt; [N] (Number of periods)</p>
    <p>&gt; Step 2: 5.5 -&gt; [I/YR] (Annual interest rate)</p>
    <p>&gt; Step 3: 200000 -&gt; [PV] (Present loan value)</p>
    <p>&gt; Step 4: 0 -&gt; [FV] (Future loan balance)</p>
    <p>&gt; Step 5: Press [PMT] to execute solver.</p>
    <p class="font-bold bg-[#CBD1DC] bg-opacity-40 px-1 inline-block">&gt; VERIFIED: PMT = $1,126.83 / month</p>
  </div>
  <div class="pt-2 border-t border-charcoal border-opacity-30 flex justify-between items-center text-xs font-bold">
    <span class="text-xl">1,126.83_</span>
    <span class="bg-charcoal text-icyblue px-2 py-0.5">[NEXT]</span>
  </div>
</div>

---

## 7. Statistical Sums & Standard Deviation

Accumulate 2-variable data pairs $(x, y)$ into continuous memory registers using $\Sigma+$ to calculate means and sample standard deviations.

*Mission: Enter sample data points $(2, 4)$ and $(4, 6)$, then solve mean and standard deviation.*

<div class="lcd-screen p-4 border-2 border-charcoal font-terminus shadow-md my-4" style="max-width: 650px;">
  <div class="text-xs uppercase tracking-wider text-charcoal border-b border-charcoal border-opacity-30 pb-1 flex justify-between font-bold">
    <span>&gt; TUI: STATISTICS &amp; STD DEV (LESSON 14/16)</span>
    <span>[C] EXIT</span>
  </div>
  <div class="text-sm text-charcoal leading-snug space-y-1 py-2">
    <p>&gt; Step 1: Tap Yellow Shift (↰) -&gt; CLEAR -&gt; Σ (Clears stat registers)</p>
    <p>&gt; Step 2: 4 [Y] -&gt; ENTER -&gt; 2 [X] -&gt; Tap Σ+ [Accumulates n=1]</p>
    <p>&gt; Step 3: 6 [Y] -&gt; ENTER -&gt; 4 [X] -&gt; Tap Σ+ [Accumulates n=2]</p>
    <p>&gt; Step 4: Tap Blue Shift -&gt; yˣ (x̄, ȳ) -&gt; Mean X = 3.0000, Mean Y = 5.0000</p>
    <p>&gt; Step 5: Tap Blue Shift -&gt; ¹/x (s, σ) -&gt; Sample StdDev = 1.4142</p>
    <p class="font-bold bg-[#CBD1DC] bg-opacity-40 px-1 inline-block">&gt; VERIFIED: Standard deviation s = 1.4142</p>
  </div>
  <div class="pt-2 border-t border-charcoal border-opacity-30 flex justify-between items-center text-xs font-bold">
    <span class="text-xl">1.4142_</span>
    <span class="bg-charcoal text-icyblue px-2 py-0.5">[EXIT]</span>
  </div>
</div>

---

## 8. Executing Tutorials on Physical Firmware (RP2350)

StackCalc32's 16 guided lessons are not limited to touchscreens—they are implemented natively in bare-metal Embedded Swift running on the physical RP2350 microcontroller. The hardware provides an authentic, distraction-free environment to master RPN calculation.

### Hardware Launch Sequence
- **Dedicated Launcher Key**: Press **Yellow Shift (↰) + C** anywhere on the physical keypad to launch the built-in Interactive Tutorial Runner.
- **Instant Event Interception**: The firmware event loop intercepts matrix scanning, suspends the standard operational stack, and loads the active tutorial state machine directly into the display buffer.

### Physical Display & Dynamic Softkeys
- **ST7567A Transflective LCD**: The 132×65 pixel monochrome display renders a 4-line terminal transcript using the sharp 6×8 pixel Terminus font. High contrast ensures clear legibility under harsh laboratory lighting or direct sunlight.
- **Tactile Softkey Integration**: The top row of 6 tactile keys dynamically maps to contextual controls:
  - **Key 1 (`[PREV]`)**: Revisit the previous instruction step.
  - **Key 2 (`[NEXT]`)**: Advance to the next step once target preconditions are verified.
  - **Key 5 (`[SKIP]`)**: Jump ahead to the subsequent lesson in the curriculum.
  - **Key 6 (`[EXIT]`)**: Dismiss the tutorial session and immediately restore your active calculation stack.

### Real-Time Keystroke & Stack Verification
- When an instructional step prompts for an input sequence (for example, `Press 5 -> ENTER -> 3 -> +`), the firmware monitors physical switch actuations across the 43-key matrix.
- Each switch closure evaluates against the deterministic `RPNCore` math engine.
- Upon matching expected results, the LCD displays `VERIFIED: [TEST PASSED]` and enables the `[NEXT]` softkey to advance.

### Non-Volatile Flash Memory Persistence
- Progress across the 16 lessons is tracked via an internal bitmask stored in the RP2350's non-volatile QSPI flash memory (`firmwareTutorialCompletionMask`).
- Your tutorial progress and mastery state persist across deep sleep, power cycles, and battery changes.

---

## The Complete 16-Lesson Curriculum

Every lesson is available with complete bit-for-bit parity across the physical hardware instrument, iPad, and Apple Watch:

| # | Lesson Title | Target Capabilities Covered |
|---|---|---|
| **01** | **RPN Basics** | Stack lift mechanics, eliminating parentheses, 4-level register manipulation ($X, Y, Z, T$) |
| **02** | **Complex Numbers** | Cartesian $(a + bi)$ entry, complex transcendentals, Euler's identity ($e^{\pi i} = -1$) |
| **03** | **Angular Modes** | Degree, Radian, and Gradian conversions and trigonometric evaluations |
| **04** | **Register Storage** | Direct and indirect register addressing with `STO` and `RCL` |
| **05** | **Fraction Entry** | Three-part `.Whole.Numerator.Denominator` fractional format |
| **06** | **Manual Simplification** | Factoring common divisors step-by-step using the `[SIMP]` softkey |
| **07** | **Mixed Arithmetic** | Exact fractional addition, subtraction, multiplication, and division |
| **08** | **Fraction/Decimal Toggle** | Toggling instantly between exact rational fractions and floating-point decimal via `[FDISP]` |
| **09** | **TVM Amortization** | Solving loan amortization parameters ($N, I\%YR, PV, PMT, FV$) without algebraic formulas |
| **10** | **Unit Conversions** | Metric and Imperial length, mass, volume, and temperature conversions |
| **11** | **Integer Division** | Integer quotient and remainder arithmetic using modern `÷R` notation |
| **12** | **Last X Recovery** | Error correction and argument reuse via `LAST𝑥` |
| **13** | **Time Conversions** | Decimal hours to Hours:Minutes:Seconds (`▸HR`, `▸HMS`) |
| **14** | **Base Modes** | Hexadecimal, Decimal, Octal, and Binary bitwise logic and word sizes |
| **15** | **Two-Variable Statistics** | Accumulating coordinate data pairs with $\Sigma+$ and $\Sigma-$ |
| **16** | **Standard Deviation** | Sample ($s$) and population ($\sigma$) standard deviations, weighted means |

---

## Experience StackCalc Across Surfaces

Master the tutorials on dedicated tactile hardware, or practice on your iPhone and Apple Watch:

<div class="my-6" style="display: flex; flex-wrap: wrap; gap: 14px; align-items: center;">
  <a href="../#preorder" class="brutalist-button-primary px-6 py-3.5 font-mono text-xs sm:text-sm font-bold inline-flex items-center gap-2 text-decoration-none">
    PRE-ORDER PHYSICAL HARDWARE &rarr;
  </a>
  <a href="https://apps.apple.com/app/id6801788040" target="_blank" class="brutalist-button px-6 py-3.5 font-mono text-xs sm:text-sm font-bold inline-flex items-center gap-2 text-decoration-none" style="border: 2px solid #CBD1DC; color: #E2E6EE;">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: -3px; display: inline-block;"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.88c.61-.74 1.04-1.78.92-2.82-.93.04-2.02.63-2.65 1.37-.56.64-.99 1.69-.86 2.71 1.05.08 2.01-.54 2.59-1.26z"/></svg>
    DOWNLOAD COMPANION APP STORE
  </a>
</div>
