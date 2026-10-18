---
title: "Chapter 11: Financial Mathematics, Executive Analytics & TVM | SC-32 Manual"
description: "Master the 5-variable Time Value of Money (TVM) solver, the Kahan base-preserving percentage invariant, cross-metric elasticity, corporate DCF, and everyday carry math on the StackCalc SC-32."
---

# Chapter 11: Financial Mathematics, Executive Analytics & TVM

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">SC-32 FINANCIAL MATH // TIME VALUE OF MONEY &amp; APPLIED BUSINESS ANALYTICS</span>
  <span class="te-viewport-status text-sky-400">● 5-VARIABLE TVM SOLVER &bull; EXECUTIVE PERCENTAGE METRICS &bull; CORPORATE DCF &amp; EVERYDAY CARRY</span>
</div>

## The Application: The Time Value of Human Labor & William Kahan's Financial Invariant

Money is not merely abstract numbers printed on green paper or glowing as digits in a bank ledger. In the physical universe, **money represents stored human time and labor**. 

When an engineer signs an employment contract, an entrepreneur secures an equipment lease, or a family signs a 30-year home mortgage, the mathematics of compound interest dictates whether that labor compounds into generational freedom or evaporates into perpetual interest debt.

### William Kahan's Crusade: The War on Destructive Percentage Keys

In the late 1970s, UC Berkeley Professor and future Turing Award laureate **William M. Kahan** inspected the commercial handheld calculators sold to consumers and business executives. What he discovered appalled him.

On almost every algebraic calculator of the era, the percentage key was **destructive**. Suppose you were billing a corporate client for $\$150.00$ of engineering consulting, plus an $8.25\%$ state sales tax:

$$\text{Algebraic keystrokes: } 150 \ [\times] \ 8.25 \ [\%] \quad \Longrightarrow \quad \text{Displays } 12.38$$

The moment you pressed `{{key:%}}`, the calculator **obliterated your $\$150.00$ base amount**! To find the invoice total ($\$162.38$), you had to either manually re-enter $\$150.00$, write it down on scratch paper, or rely on a clunky memory key (`[M+]`). If the client asked to test an alternative $9.5\%$ tax rate, you had to start completely over from scratch.

Kahan declared war on this numerical incompetence. In 1979, writing in the *Hewlett-Packard Journal* {{cite:kahan1979}}, he formulated what is now celebrated in numerical computing as the **Kahan Percentage Invariant**:

<div class="admonition note">
<p class="admonition-title">The Kahan Percentage Invariant</p>
<p>A percentage operator must be <strong>non-destructive and dyadic</strong>:</p>
$$X \longleftarrow \frac{Y \times X}{100}, \qquad Y \longleftarrow Y \quad (\text{Preserved frozen on the stack!})$$
<p>On the StackCalc SC-32, your base amount <em>never</em> disappears:</p>
<ol>
<li><strong>Key in:</strong> <code>150 {{key:ENTER}} 8.25 {{key:%}}</code><br>
&rarr; Register $X$ displays <code>12.38</code> (the tax amount).<br>
&rarr; Register $Y$ silently holds <code>150.00</code> (the base invoice).</li>
<li><strong>Total Invoice?</strong> Just tap <code>{{key:+}}</code> &rarr; <code>$162.38</code>!</li>
<li><strong>Discount Subtracted?</strong> Just tap <code>{{key:-}}</code> &rarr; <code>$137.62</code>!</li>
<li><strong>Alternative Rate?</strong> Tap <code>{{key:LASTX}} {{key:x⇄y}}</code> or test alternate taxes directly without re-entry!</li>
</ol>
</div>

{{res:sc32_tvm_pmt:screenshot|Active RPN Calculation on Transflective LCD}}

*Figure 11.1: The SC-32 transflective display executing multi-variable financial calculations with continuous stack preservation.*

{{blocks:sc32_craftsmanship_pureblack|StackCalc SC-32 Pure Black Craftsmanship Edition}}
*Figure 11.2: The SC-32 precision aluminum chassis and tactile key switches, engineered for fatigue-free boardroom and field accounting.*

Beyond simple percentages, all commercial banking, corporate bonds, and mortgages rest on the 5-variable Time Value of Money (TVM) equation:

$$PV + PMT \left[ \frac{1 - (1 + i)^{-N}}{i} \right] + FV (1 + i)^{-N} = 0$$

The SC-32's dedicated TVM register suite frees you from the tyranny of opaque amortization software. You control the five dials of capital.

<div class="admonition warning">
<p class="admonition-title">Inside-Out Stack Architecture: Algebraic Trap vs. RPN Shortcut — Compound TVM &amp; Amortization Formulas</p>
<p><strong>The Algebraic Parenthesis Trap:</strong> Consider evaluating the compound interest factor or monthly mortgage annuity payment manually from the fundamental closed-form equation:</p>
$$PMT = PV \cdot \frac{i(1 + i)^N}{(1 + i)^N - 1}$$
<p>On an algebraic textbook calculator, this formula is a minefield of nested parentheses, cognitive buffering, and operator precedence traps {{cite:sweller1988,dijkstra1961}}. An analyst must key:</p>
<pre><code>PV * ( ( I / 1200 ) * ( 1 + I / 1200 ) ^ N ) / ( ( 1 + I / 1200 ) ^ N - 1 )</code></pre>
<p>Notice the fatal vulnerabilities: <code>( I / 1200 )</code> must be recomputed or stored in scratch memory three separate times; five levels of open parentheses must remain balanced in working memory; and a single missing closing parenthesis triggers a syntax error or a silent erroneous amortization table {{cite:parker2019,ellenberg2014}}.</p>
<p><strong>The RPN Stack Shortcut:</strong> On the StackCalc SC-32, the computation proceeds from the inside out using <em>The Inside-Out Growth Factor</em> and <em>The LASTX Dual-Branch Trick</em> {{cite:hp15c1982,hp32sii1991}}. The periodic interest rate $i = I/1200$ is computed once. Adding 1 yields the base $(1 + i)$. Raising to the $N$-th power yields $G = (1 + i)^N$. Tap <code>{{key:ENTER}}</code> to duplicate $G$, subtract 1 to form the denominator $(G - 1)$ in Register $X$, and tap <code>{{key:÷}}</code> against the numerator branch or use <em>The x⇄y Denominator Flip</em>. Every intermediate subtotal is physically visible on the transflective dot-matrix LCD, requiring zero parentheses, zero scratchpad re-entry, and zero cognitive load {{cite:miller1956}}.</p>
</div>

<div class="p-4 rounded-xl bg-slate-900 border border-sky-500/30 mb-8 font-mono text-xs text-sky-300">
  <strong>CHAPTER BASELINE MODE:</strong> <code>[FIX 2]</code> (Fixed 2-decimal currency display; Standard Base-10 Arithmetic; Degrees angular mode default). TVM variables and four operational stack registers ($X, Y, Z, T$) are maintained continuously in non-volatile hardware memory.
</div>

---

## The Executive's Guide to RPN: Speed, Flow & Cognitive Friction

In high-stakes corporate boardrooms, private equity deal evaluations, commercial contract negotiations, and dynamic field estimation, computational latency imposes immediate cognitive friction. 

When an executive using an algebraic calculator (such as a smartphone app, spreadsheet formula line, or standard office desktop unit) attempts to evaluate compound financial relationships, they are forced to mentally manage parenthesis depth, worry about operator precedence, and frequently store intermediate results into disjointed memory keys (`M+`, `MR`, `STO 1`).

Reverse Polish Notation completely removes this cognitive overhead. The four-level operational stack acts as a visual, transparent ledger where operands are staged, intermediate results are automatically preserved, and dyadic operations consume inputs with zero syntax errors.

### The Algebraic Trap vs. StackCalc Superpower Showdown

| Challenge / Metric | Algebraic Trap (TI-84 / Infix) | Algebraic Strokes | StackCalc SC-32 Superpower | SC-32 Strokes | Superpower Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **Sales Tax Total**: $\$150.00$ at $8.25\%$ | `150 * 0.0825 =` $\to \$12.38$. Base $\$150.00$ destroyed; must re-enter `+ 150 =` $\to \$162.38$. Testing alternative $9.5\%$ requires starting completely over. | 18 | **Kahan Non-Destructive `%`**: `150 {{key:ENTER}} 8.25 {{key:%}}` $\to X = 12.38$, $Y = 150.00$ preserved! Tap `{{key:+}}` $\to \$162.38$. Tap `{{key:LASTX}} {{key:x⇄y}}` to test new rates. | 9 | **50% fewer strokes + 100% base preservation** |
| **YoY Growth Spread**: ARR vs CAC | Must compute and write down $(\Delta\text{ARR}\% - \Delta\text{CAC}\%)$. Requires 30+ characters with nested parentheses or 2 disjoint memory slots. | 32 | **Multi-Metric Stack Staging**: Key both metrics via `{{key:%CHG}}`; both rates staged in $Y$ ($+30\%$) and $X$ ($+20\%$). Tap `{{key:-}}` for spread ($+10\%$) or `{{key:÷}}` for elasticity ($1.5\times$). | 16 | **50% fewer strokes + zero scratchpad memory** |
| **30-Year Mortgage Payment**: $\$350\text{k}$ at $6.75\%$ | Multi-step algebraic formula with 5 levels of parentheses: `350000 * ( ( 0.0675 / 12 ) * ( 1 + 0.0675 / 12 ) ^ 360 ) / ...` | 42 | **Dedicated 5-Variable TVM**: Store terms directly into financial registers `360 {{key:N}} 6.75 {{key:ENTER}} 12 {{key:÷}} {{key:I%YR}} 350000 {{key:PV}} 0 {{key:FV}} {{key:PMT}}`. | 24 | **43% fewer strokes + zero parenthesis syntax errors** |
| **DCF Valuation**: 4-Year Free Cash Flows | `10 / 1.1 + 12 / 1.1 ^ 2 + 15 / 1.1 ^ 3 + 234 / 1.1 ^ 4 =`. Vulnerable to mistyped exponent precedence and scratchpad loss. | 36 | **Inside-Out Discounting Stream**: Chain successive cash inflows with continuous stack division; zero parenthesis syntax overhead. | 22 | **39% fewer strokes + immediate intermediate cash visibility** |

### The Concrete-Representational-Abstract (CRA) Financial Continuum
Financial comprehension on the SC-32 bridges three distinct pedagogical levels:
1. **Concrete (The Cash Ledger):** Physical dollar bills exchanged across a commercial transaction table or loan amortization ledger. Every outflow leaves the wallet (represented by negative sign `{{key:+/-}}`), and every inflow enters the wallet (positive sign).
2. **Representational (The Operational 4-Stack):** The vertical registers ($X, Y, Z, T$) represent distinct balance accounts. Register $X$ represents active liquid cash in hand; Register $Y$ preserves the pre-tax invoice baseline; Register $Z$ holds cumulative tax reserves; Register $T$ retains repeating scaling multipliers.
3. **Abstract (The Actuarial Equations):** Compound interest, annuity discount factors, and exponential discounting formulas operate behind simple single-key triggers (`{{key:%}}`, `{{key:%CHG}}`, `{{key:TVM}}`, `{{key:PMT}}`).

---

## The Base-Preserving Percentage Invariant (`{{key:%}}`)

On standard commercial calculators, pressing the percentage key is fraught with peril: some models divide the entry by 100, others multiply the previous operand, and nearly all destroy the base operand, preventing subsequent addition or subtraction without re-typing.

On the StackCalc SC-32, the **Percentage Function (`{{key:%}}`)** is an invariant dyadic operator adhering strictly to William Kahan's non-destructive specification:

$$\text{Calculation: } \quad X \leftarrow \frac{Y \times X}{100}, \quad Y \leftarrow Y \text{ (Preserved!)}, \quad \text{Lift} \leftarrow \text{TRUE}$$

| Register | State After Keying `[Base] {{key:ENTER}} [Rate] {{key:%}}` | Executive Function |
| :---: | :--- | :--- |
| **Register $Y$** | Base Amount (Preserved frozen in $Y$) | Base remains intact for subsequent total, discount, or alternative trial |
| **Register $X$** | Computed Percentage Amount: $(Y \times X) / 100$ | Tax, tip, commission, or margin dollar value |

Immediate Next Keystrokes:
* **Press `{{key:+}}`:** Instantly yields Base + Amount (Total with Tax, Markup, Tip).
* **Press `{{key:-}}`:** Instantly yields Base - Amount (Discounted Price, Net Proceeds).
* **Press `{{key:x⇄y}}`:** Restores base to $X$ for alternative tax rate trials.

### Architectural Contrast with Infix Calculators
In an algebraic calculator:
* To compute tax on $\$150.00$ at $8.25\%$, the user types `150 × 0.0825 =` to get $\$12.38$.
* To get the total, they must now type `+ 150 =` $\to \$162.38$.
* If they also needed to see what the net total would be with a $10\%$ discount instead, they must start completely over and re-enter `150`.
In RPN:
* `{{res:sc32_11_financial_tvm_seq_06:keys}}` puts $\$12.38$ in $X$ and preserves $\$150.00$ in $Y$.
* Pressing `{{key:+}}` yields $\$162.38$ in one stroke.
* Pressing `{{key:LASTX}}` recovers $\$12.38$, or rolling the stack allows immediate further analysis.

---

## Period-over-Period & Year-over-Year Performance (`{{key:%CHG}}`)

Evaluating corporate revenue growth, cost expansion, and quarterly margin velocity requires calculating the relative percentage change:

$$\%CHG = \frac{\text{New Value} - \text{Old Value}}{\text{Old Value}} \times 100$$

On the SC-32, the **Percent Change Function (`{{key:%CHG}}`)** is executed via Right Shift `{{key:↱}}` followed by `{{key:%CHG}}`:

$$\text{Protocol: } \quad \text{Old\_Value {{key:ENTER}} New\_Value {{key:%CHG}}}$$

| Register | State Before `{{key:%CHG}}` | State After `{{key:%CHG}}` | Executive Role |
| :---: | :--- | :--- | :--- |
| **Register $Y$** | Old Value (Baseline) | Old Value (Preserved in $Y$!) | Allows instant variance check: `{{key:x⇄y}} {{key:LASTX}} {{key:x⇄y}} {{key:-}}` |
| **Register $X$** | New Value (Current) | $\frac{\text{New} - \text{Old}}{\text{Old}} \times 100$ | Relative rate of expansion/contraction (%) |
| **`LASTX`** | Previous operand | New Value | Retained for delta calculations |

Because the Old Value is preserved in Register $Y$ and the New Value is saved in `LASTX`, the executive can immediately compute the absolute dollar variance ($\text{New} - \text{Old}$) by pressing `{{key:x⇄y}} {{key:LASTX}} {{key:x⇄y}} {{key:-}}` (positioning New in $Y$ and Old in $X$ before subtraction).

---

## Cross-Metric Elasticity & Spread: The Multi-Metric Stack Advantage

The true computational superiority of the RPN operational stack emerges during **comparative multi-metric corporate analytics**. 

Consider an executive evaluating a software portfolio company:
* **Metric A (Annual Recurring Revenue - ARR):** Grew from $\$12.0\text{M}$ to $\$15.6\text{M}$.
* **Metric B (Customer Acquisition Cost - CAC):** Expanded from $\$2.4\text{M}$ to $\$2.88\text{M}$.

The executive must determine:
1. **The ARR vs. CAC Growth Spread:** The percentage point difference in expansion rates ($\Delta \text{ARR}\% - \Delta \text{CAC}\%$).
2. **The Growth Elasticity Ratio:** The sensitivity of revenue growth relative to acquisition spending ($\Delta \text{ARR}\% \div \Delta \text{CAC}\%$).

| Stack Register | Value Staged | Financial Meaning | Immediate Dyadic Operation |
| :---: | :---: | :--- | :--- |
| **Register $T$** | $0.00$ | Top of stack | — |
| **Register $Z$** | $0.00$ | Holding register | — |
| **Register $Y$** | $+30.00\%$ | Metric A YoY Growth ($\Delta\text{ARR}\%$) | Base comparator |
| **Register $X$** | $+20.00\%$ | Metric B YoY Growth ($\Delta\text{CAC}\%$) | Active metric |

* **Press `{{key:-}}`:** $30.00 - 20.00 = \mathbf{+10.00\%}$ Growth Spread (ARR outgrew CAC by 10 percentage points!).
* **Press `{{key:÷}}`:** $30.00 \div 20.00 = \mathbf{1.50\times}$ Growth Elasticity Ratio (1.5x revenue leverage per CAC dollar!).

In an algebraic calculator, performing this analysis requires scribbling intermediate percentages on paper or entering a 30-character formula with nested parentheses:
$$(((15.6 - 12.0) \div 12.0) \times 100) - (((2.88 - 2.40) \div 2.40) \times 100)$$
On the SC-32, the stack natively holds both metrics side-by-side, allowing instant dyadic inspection.

---

## The 5-Variable Time Value of Money (TVM) Architecture

The SC-32 features an onboard **Five-Variable Time Value of Money (TVM) Engine** accessed via Left Shift `{{key:↰}}` followed by `{{key:TVM}}` on the multi-action `{{key:x∥y}}` key (Row 7, Column 3), as specified in the *HP32SII Deviation Rubric*.

| TVM Variable | LFU Softkey | Actuarial Description | Computational Units |
| :---: | :---: | :--- | :--- |
| **$N$** | `{{key:N}}` | Total number of compounding periods | Integer or fractional periods |
| **$I\%YR$** | `{{key:I%YR}}` | Annual nominal interest rate | Percent per year (e.g. `6.5` for 6.5%) |
| **$PV$** | `{{key:PV}}` | Present value (initial loan principal or investment) | Currency ($) |
| **$PMT$** | `{{key:PMT}}` | Periodic annuity payment amount | Currency ($ per period) |
| **$FV$** | `{{key:FV}}` | Future value (final balloon balance or accumulated savings) | Currency ($) |

### The Master Actuarial TVM Equation
The five financial variables are bound by the universal compound interest annuity formula:

$$PV + PMT \left[ \frac{1 - (1 + i)^{-N}}{i} \right] (1 + i \cdot S) + FV (1 + i)^{-N} = 0$$

where:
* $i = \frac{I\%YR}{100 \times P/\text{YR}}$ is the periodic interest rate per compounding period.
* $N$ is the total integer count of compounding periods.
* $S = 0$ for End-of-Period payments (Ordinary Annuity, default).
* $S = 1$ for Beginning-of-Period payments (Annuity Due, flagged by the `BEGIN` annunciator).

### Strict Cash Flow Sign Conventions
* **Cash Inflow ($+$):** Money received into your hands/account (e.g., bank loans, proceeds, receipts).
* **Cash Outflow ($-$, `{{key:+/-}}`):** Money paid out from your pocket (e.g., initial investment deposits, mortgage payments, maintenance costs).

### The Contest Financial Mathematics Canon: Direct Stack Solutions
While the dedicated TVM softkeys automate iterative solvers (such as finding $I\%YR$), competitive math Olympians and financial analysts frequently evaluate direct analytical closed forms inside-out on the operational stack:

| Financial Instrument | Analytical Closed-Form Formula | Native RPN Inside-Out Recipe |
| :--- | :--- | :--- |
| **Ordinary Annuity PV** | $PV = PMT \left[ \frac{1 - (1 + i)^{-N}}{i} \right]$ | `1 ENTER i + N +/- yˣ 1 x⇄y - i ÷ PMT ×` |
| **Ordinary Annuity FV** | $FV = PMT \left[ \frac{(1 + i)^N - 1}{i} \right]$ | `1 ENTER i + N yˣ 1 - i ÷ PMT ×` |
| **Amortization Payment** | $PMT = PV \left[ \frac{i}{1 - (1 + i)^{-N}} \right]$ | `1 ENTER i + N +/- yˣ 1 x⇄y - i x⇄y ÷ PV ×` |
| **Sinking Fund Payment** | $PMT = FV \left[ \frac{i}{(1 + i)^N - 1} \right]$ | `1 ENTER i + N yˣ 1 - i x⇄y ÷ FV ×` |
| **Perpetuity PV** | $PV = \frac{PMT}{i}$ | `PMT ENTER i ÷` |
| **Growing Perpetuity PV** | $PV = \frac{PMT}{i - g}$ | `PMT ENTER i ENTER g - ÷` |

> [!TIP]
> **Contest Quick-Lookup Cross-Reference:**
> For the master quick-reference tables of all financial mathematics, amortization, and TVM equations, consult **[Appendix D: Section 9 (Financial Mathematics, Amortization & TVM Equations)](file:///Users/abagher/Documents/GitHub/stackcalc/docs/manuals/sc32/appendix-d-constants-and-equations.md)**.

## Teaching & Instrument Architecture Notes

### Register Y Preservation During Percentage Operations
A classic pitfall in percentage arithmetic on algebraic calculators is keying `100 + 8% =` and receiving an unintended output like `100.08`. On the SC-32, executing `{{res:sc32_11_financial_tvm_seq_44:keys}}` places the exact percentage value ($8.00$) in Register $X$ while freezing the base ($100.00$) in Register $Y$. Both quantities remain visible simultaneously on the stack before committing to addition (`{{key:+}}` for tax or markup) or subtraction (`{{key:-}}` for discount). Similarly, economic price elasticity $\frac{\%\Delta Q}{\%\Delta P}$ is evaluated directly by stacking the two percentage changes into Registers $Y$ and $X$ and executing `{{key:÷}}`.

### Actuarial Sign Discipline & Amortization Mechanics
The five-variable TVM solver operates on strict actuarial conservation of cash flow:
$$PV + PMT \left[ \frac{1 - (1 + i)^{-N}}{i} \right] + FV (1 + i)^{-N} = 0$$
Every cash transaction is directional: cash inflows received are entered as positive values, while cash outflows disbursed (investments, down payments, periodic amortizations) are entered as negative values via `{{key:+/-}}`. If all inputs share the same sign, the solver flags an actuarial contradiction (`ERROR 5: NO SOLUTION`). Comparing a 30-year versus 15-year fixed mortgage illustrates the power of compounding: on a $\$350,000$ mortgage at $6.75\%$, the 30-year schedule accumulates over $\$467,000$ in interest, whereas a 15-year term saves over $\$277,300$ by accelerating principal amortization.

### Executive Valuation & Lineage of the HP-12C
The Hewlett-Packard HP-12C established the gold standard for financial computation in 1981. The SC-32 integrates a dedicated five-variable TVM solver into its 43-key scientific architecture while maintaining pure RPN stack mechanics. Compound Annual Growth Rate (CAGR), Net Present Value (NPV), and internal rate of return on uneven cash flows converge via Richard Brent's hybrid root-finding engine with certified 64-bit precision, providing an executive-grade analytical tool for complex deal structuring.

---

## Diagnostic Checkpoints & Singularity Handling

> [!CHECKPOINT]
> **Diagnostic Checkpoint 11.1: Cash Flow Sign Error (`ERROR 5: NO SOLUTION`)**  
> If all TVM inputs are entered with the same sign (e.g., $PV = 1000, PMT = 50, FV = 1000$), the compound interest solver halts with `ERROR 5: NO SOLUTION`. Actuarial balance requires at least one cash inflow ($+$) and one cash outflow ($-$, entered via `{{key:+/-}}`).

> [!CHECKPOINT]
> **Diagnostic Checkpoint 11.2: Periodic Rate Conversion Consistency**  
> When solving monthly mortgages ($N = 360$), the annual nominal interest rate $I\%YR$ must be divided by 12 before storing into `{{key:I%YR}}`. Storing the full annual percentage ($6.75\%$) directly would imply a crippling $6.75\%$ monthly interest rate ($81.0\%\text{ APR}$)!

> [!CHECKPOINT]
> **Diagnostic Checkpoint 11.3: Payment Mode Annunciator (`BEGIN` vs. `END`)**  
> If mortgage payment calculations differ slightly from bank quotes (e.g., $\$2,257$ vs $\$2,270$), verify whether the `BEGIN` annunciator is lit on the LCD. Mortgages pay at the `END` of each month; leases and college tuition pay at the `BEGIN`ning. Toggle via `{{key:TVM}} [BEG/END]`.

> [!CHECKPOINT]
> **Diagnostic Checkpoint 11.4: Base Preservation in Register Y**  
> Remember that after executing `[Base] {{key:ENTER}} [Rate] {{key:%}}`, Register $Y$ still contains `[Base]`. Pressing `{{key:+}}` adds the percentage to the base, while pressing `{{key:-}}` subtracts it. If you wish to retain the computed percentage in $X$ and discard the base, press `{{key:x⇄y}} {{key:R↓}}`.

---

## Engineering Design Briefing: The Wall Street Corporate Valuation Desk (Problems 11.1 through 11.42)

---

> **Thematic Arc I — Commercial Percentages, Margin Markup & Cash-Flow Foundations (Problems 11.1–11.10):** We start with `%`, `%CHG`, and basic compounding before loading the 5-register TVM solver.

### Problem 11.1: Commercial Invoice with Sales Tax
An enterprise hardware order totals $\$18,450.00$. The regional state sales tax rate is $8.25\%$. Calculate both the tax liability and the total invoice charge.

**Keystrokes in `[FIX 2]` Mode:** `{{res:sc32_11_financial_tvm_seq_07:keys}}` $\rightarrow$ $X = \mathbf{\$1,522.13}$, $Y = \$18,450.00$
Press `{{key:+}}` $\rightarrow$ **`$19,972.13`**

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `18450 {{key:ENTER}}` | 0.00 | 0.00 | 18450.00 | 18450.00 | `18450.00_` |
| 02 | `8.25 {{key:%}}` | 0.00 | 0.00 | 18450.00 | 1522.13 | `1522.13` |
| 03 | `{{key:+}}` | 0.00 | 0.00 | 0.00 | 19972.13 | `19972.13` |

---

### Problem 11.2: Enterprise Contract Volume Discount
A software contract carries a list price of $\$85,000.00$. The sales team negotiates a $17.5\%$ enterprise discount. Determine the dollar discount amount and the final net invoice payable.

**Keystrokes in `[FIX 2]` Mode:** `{{res:sc32_11_financial_tvm_seq_08:keys}}` $\rightarrow$ $X = \mathbf{\$14,875.00}$ (Discount)
Press `{{key:-}}` $\rightarrow$ **`$70,125.00`** (Net payable).

Keying `85000 {{key:ENTER}} 17.5 {{key:%}}` computes the contract discount $(\$14,875.00)$ in Register $X$ while freezing the list price in Register $Y$ $(T: 0.00, Z: 0.00, Y: 85000.00, X: 14875.00)$. Striking `{{key:-}}` subtracts the discount from the preserved base, resolving final invoice payable $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{70125.00})$ in one stroke.

---

### Problem 11.3: Annual Revenue Acceleration (%CHG)
Revenues grew from $\$42.50\text{M}$ in fiscal year 2024 to $\$51.85\text{M}$ in fiscal year 2025. Calculate the annual percentage growth rate.

$$\%CHG = \frac{51.85 - 42.50}{42.50} \times 100 = \mathbf{+22.00\%}$$

**Keystrokes:** `{{res:sc32_11_financial_tvm_seq_09:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_09:value}}`**.

Keying `42.50 {{key:ENTER}} 51.85` loads baseline revenue into $Y$ and current revenue into $X$ $(T: 0.00, Z: 0.00, Y: 42.50, X: 51.85)$. Striking `{{key:%CHG}}` executes relative rate of expansion, resolving annual growth $(T: 0.00, Z: 0.00, Y: 42.50, X: \mathbf{22.00\%})$ while retaining the baseline in Register $Y$.

---

### Problem 11.4: Multi-Metric Growth Spread and Elasticity Ratio
* Metric A (ARR): Grew from $\$12.0\text{M}$ to $\$15.6\text{M}$ ($\Delta A\% = 30.00\%$)
* Metric B (CAC): Expanded from $\$2.4\text{M}$ to $\$2.88\text{M}$ ($\Delta B\% = 20.00\%$)

**Keystrokes:**
1. `{{res:sc32_11_financial_tvm_seq_10:keys}}` $\rightarrow$ $30.00$
2. `{{res:sc32_11_financial_tvm_seq_11:keys}}` $\rightarrow$ $20.00$
3. With revenue growth ($Y = 30.00$) and headcount growth ($X = 20.00$) aligned on the stack:
4. Press `{{key:-}}` $\rightarrow$ **`+10.00%`** (Growth Spread)
5. `{{res:sc32_11_financial_tvm_seq_12:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_12:value}}`** (Elasticity Multiplier).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `12 {{key:ENTER}} 15.6 {{key:%CHG}}` | 0.00 | 0.00 | 12.00 | 30.00 | `30.00` |
| 02 | `2.4 {{key:ENTER}} 2.88 {{key:%CHG}}` | 12.00 | 30.00 | 2.40 | 20.00 | `20.00` |
| 03 | `{{key:x⇄y}}` | 12.00 | 30.00 | 20.00 | 2.40 | `2.40` |
| 04 | `{{key:R↓}}` | 2.40 | 12.00 | 30.00 | 20.00 | `20.00` |
| 05 | `{{key:-}}` | 2.40 | 2.40 | 12.00 | 10.00 | `10.00` |

---

### Problem 11.5: Compound Annual Growth Rate (CAGR)
A venture fund invests $\$14.0\text{M}$ into a startup at Series A. The company exits via acquisition for $\$88.5\text{M}$ exactly $n = 5\text{ years}$ later. Calculate the Compound Annual Growth Rate:

$$\text{CAGR} = \left(\frac{88.5}{14.0}\right)^{1/5} - 1$$

**Keystrokes:** `{{res:sc32_11_financial_tvm_seq_13:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_13:value}}`**.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `88.5 {{key:ENTER}}` | 0.00 | 0.00 | 88.50 | 88.50 | `88.50_` |
| 02 | `14.0 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 6.32 | `6.32` |
| 03 | `5 {{key:1/x}}` | 0.00 | 0.00 | 6.32 | 0.20 | `0.20` |
| 04 | `{{key:yˣ}}` | 0.00 | 0.00 | 0.00 | 1.45 | `1.45` |
| 05 | `1 {{key:-}}` | 0.00 | 0.00 | 0.00 | 0.45 | `0.45` |
| 06 | `100 {{key:×}}` | 0.00 | 0.00 | 0.00 | 44.58 | `44.58` |

---

### Problem 11.6: EBITDA Margin Expansion in Basis Points
A manufacturing firm expands revenue from $\$240.0\text{M}$ to $\$310.0\text{M}$. During the same period, EBITDA rises from $\$36.0\text{M}$ to $\$55.8\text{M}$. Determine the EBITDA margin expansion in basis points ($1\text{ bp} = 0.01\%$).
1. Baseline margin: `{{res:sc32_11_financial_tvm_seq_14:keys}}` $\rightarrow$ $15.00\%$
2. Expanded margin: `{{res:sc32_11_financial_tvm_seq_15:keys}}` $\rightarrow$ $18.00\%$
3. Spread in basis points: `{{key:-}} 100 {{key:×}}` $\rightarrow$ **`300.00 bps`**.

Keying `55.8 {{key:ENTER}} 310 {{key:÷}} 100 {{key:×}}` computes expanded operating margin ($18.00\%$) in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 18.00)$. Keying `36 {{key:ENTER}} 240 {{key:÷}} 100 {{key:×}}` computes baseline margin ($15.00\%$) in $X$, lifting expanded margin to $Y$ $(T: 0.00, Z: 0.00, Y: 18.00, X: 15.00)$. Striking `{{key:-}} 100 {{key:×}}` subtracts margins ($3.00\%$) and scales to basis points $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{300.00}\text{ bps})$.

---

### Problem 11.7: 30-Year Fixed Residential Mortgage & Lifetime Interest
* Loan Principal ($PV$): $\$350,000.00$
* Annual Rate ($I\%YR$): $6.75\%$ (Monthly periodic rate $i = 6.75\% / 12 = 0.5625\%$)
* Term ($N$): $30\text{ years} \times 12 = 360\text{ months}$
* Future Value ($FV$): $\$0.00$

**Keystrokes:**
1. Clear TVM: `{{key:CLEAR}} {{key:CLALL}}`
2. `30 {{key:ENTER}} 12 {{key:×}} {{key:N}}` (Stores $360.00$)
3. `6.75 {{key:ENTER}} 12 {{key:÷}} {{key:I%YR}}` (Stores $0.5625\%$)
4. `350000 {{key:PV}}` (Stores $350,000.00$)
5. `0 {{key:FV}}` (Stores $0.00$)
6. Solve PMT: Press `{{key:PMT}}` $\rightarrow$ **`-$2,270.09`**
7. Total Lifetime Payments: `360 {{key:×}}` $\rightarrow$ **`-$817,233.60`**
8. Total Lifetime Interest: `350000 {{key:+}}` $\rightarrow$ **`-$467,233.60`** ($\$467,233.60$ interest paid).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `360 {{key:N}}` | 0.00 | 0.00 | 0.00 | 360.00 | `360.00` |
| 02 | `.5625 {{key:I%YR}}` | 0.00 | 0.00 | 360.00 | 0.56 | `0.56` |
| 03 | `350000 {{key:PV}}` | 0.00 | 360.00 | 0.56 | 350000.00 | `350000.00` |
| 04 | `0 {{key:FV}}` | 360.00 | 0.56 | 350000.00 | 0.00 | `0.00` |
| 05 | `{{key:PMT}}` | 360.00 | 0.56 | 350000.00 | -2270.09 | `-2270.09` |
| 06 | `360 {{key:×}}` | 0.56 | 0.56 | 350000.00 | -817233.60 | `-817233.60` |
| 07 | `350000 {{key:+}}` | 0.56 | 0.56 | 350000.00 | -467233.60 | `-467233.60` |

---

### Problem 11.8: 15-Year Mortgage Acceleration Comparison
Compare the $\$350,000.00$ mortgage on a 15-year term ($N = 180$) at $6.25\%$ interest ($i = 6.25 / 12 = 0.520833\%$):
* Payment: `{{res:sc32_11_financial_tvm_seq_16:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_16:value}}`**

> ***The Periodic Rate Normalization Pipeline*** — Convert annual APR to monthly periodic rate directly in $X$, routing the quotient into financial register `{{key:I%YR}}` while staging loan parameters in hardware memory {{cite:hp15c1982,ellenberg2014}}.

Storing `180 {{key:N}}` commits the 15-year financing term ($15 \times 12 = 180\text{ months}$) into financial register $N$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 180.00)$. Keying `6.25 {{key:ENTER}} 12 {{key:÷}} {{key:I%YR}}` divides annual interest ($6.25\%$) by 12, routing monthly periodic rate $0.520833\%$ directly into register $I\%YR$ $(T: 0.00, Z: 0.00, Y: 180.00, X: 0.52)$. Storing `350000 {{key:PV}} 0 {{key:FV}}` commits the financed mortgage principal and sets zero future balloon balance $(T: 180.00, Z: 0.52, Y: 350000.00, X: 0.00)$. Striking `{{key:PMT}}` executes the closed-form TVM solver, displaying monthly payment $(T: 180.00, Z: 0.52, Y: 350000.00, X: \mathbf{-3000.98})$. Multiplying `180 {{key:×}}` yields total lifetime payments $(T: 0.52, Z: 0.52, Y: 350000.00, X: \mathbf{-540176.41})$, confirming interest savings of $\$277,057.19$ over the 30-year schedule.

---

### Problem 11.9: First-Month Amortization Split & The Crossover Point
On the 30-year mortgage ($PV = \$350,000$, monthly $i = 0.5625\%$, $PMT = -\$2,270.09$):
* Interest Month 1: $350,000 \times 0.005625 = \mathbf{\$1,968.75}$ ($86.7\%$ of payment)
* Principal Month 1: $\$2,270.09 - \$1,968.75 = \mathbf{\$301.34}$ ($13.3\%$ of payment)
* New Principal Balance: $\$350,000 - \$301.34 = \mathbf{\$349,698.66}$.

| Month | Remaining Balance | Monthly Payment | Interest ($I_k$) | Principal ($P_k$) | Equity % | Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **1** | $\$349,698.66$ | $\$2,270.09$ | $\$1,968.75$ | $\$301.34$ | $0.09\%$ | $86.7\%$ of payment goes to interest |
| **237** | $\$199,642.18$ | $\$2,270.09$ | $\$1,130.71$ | $\$1,139.38$ | $42.96\%$ | **Amortization Crossover:** $P_k > I_k$ |
| **360** | $\$0.00$ | $\$2,270.09$ | $\$12.70$ | $\$2,257.39$ | $100.00\%$ | Final payoff; $\$467,233.60$ total interest |

**Keystrokes:** `350000 {{key:ENTER}} 0.005625 {{key:×}}` $\rightarrow$ **`$1,968.75`** (Month 1 Interest $I_1$).
`2270.09 {{key:x⇄y}} {{key:-}}` $\rightarrow$ **`$301.34`** (Month 1 Principal $P_1$).  
`350000 {{key:x⇄y}} {{key:-}}` $\rightarrow$ **`$349,698.66`** (Remaining Balance).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `350000 {{key:ENTER}}` | 0.00 | 0.00 | 350000.00 | 350000.00 | `350000.00_` |
| 02 | `0.005625 {{key:×}}` | 0.00 | 0.00 | 0.00 | 1968.75 | `1968.75` |
| 03 | `2270.09 {{key:x⇄y}} {{key:-}}` | 0.00 | 0.00 | 0.00 | 301.34 | `301.34` |
| 04 | `350000 {{key:x⇄y}} {{key:-}}` | 0.00 | 0.00 | 0.00 | 349698.66 | `349698.66` |

---

### Problem 11.10: Commercial 5-Year Balloon Note
Borrow $\$500,000$ at $7.5\%$ APR, amortized over 25 years ($N=300$), balloon payoff after 5 years ($N=60$):
1. Payment: `{{res:sc32_11_financial_tvm_seq_17:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_17:value}}`**
2. Balloon at Year 5: `60 {{key:N}} {{key:FV}}` $\rightarrow$ **`-$458,662.75`**.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `300 {{key:N}}` | 0.00 | 0.00 | 0.00 | 300.00 | `300.00` |
| 02 | `.625 {{key:I%YR}}` | 0.00 | 0.00 | 300.00 | 0.63 | `0.63` |
| 03 | `500000 {{key:PV}}` | 0.00 | 300.00 | 0.63 | 500000.00 | `500000.00` |
| 04 | `0 {{key:FV}}` | 300.00 | 0.63 | 500000.00 | 0.00 | `0.00` |
| 05 | `{{key:PMT}}` | 300.00 | 0.63 | 500000.00 | -3694.96 | `-3694.96` |
| 06 | `60 {{key:N}}` | 0.63 | 500000.00 | -3694.96 | 60.00 | `60.00` |
| 07 | `{{key:FV}}` | 0.63 | 500000.00 | -3694.96 | -458662.75 | `-458662.75` |

---

> **Thematic Arc II — Fixed-Income Bonds, Mortgages & Lease Amortization (Problems 11.11–11.20):** Storing four TVM variables and solving for the fifth (`N`, `I%YR`, `PV`, `PMT`, `FV`) under strict cash-flow sign conventions.

### Problem 11.11: Corporate Bond Yield to Maturity (YTM)
Bond price $PV = -\$925.00$, semi-annual coupons $PMT = \$27.50$, face $FV = \$1000.00$, $N = 20\text{ periods}$:
Solve `{{key:I%YR}}` $\rightarrow$ $i = 3.2666\%$ per half-year $\implies \text{YTM} = 3.2666 \times 2 = \mathbf{6.53\%}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `20 {{key:N}}` | 0.00 | 0.00 | 0.00 | 20.00 | `20.00` |
| 02 | `925 {{key:+/-}} {{key:PV}}` | 0.00 | 0.00 | 20.00 | -925.00 | `-925.00` |
| 03 | `27.50 {{key:PMT}}` | 0.00 | 20.00 | -925.00 | 27.50 | `27.50` |
| 04 | `1000 {{key:FV}}` | 20.00 | -925.00 | 27.50 | 1000.00 | `1000.00` |
| 05 | `{{key:I%YR}}` | 20.00 | -925.00 | 27.50 | 3.27 | `3.27` |
| 06 | `2 {{key:×}}` | -925.00 | -925.00 | 27.50 | 6.53 | `6.53` |

---

### Problem 11.12: Discounted Cash Flow (DCF) with Terminal Multiple
Forecasted 4-year free cash flows: $\$10\text{M}, \$12\text{M}, \$15\text{M}, \$18\text{M}$. Discount rate $10\%$.
Terminal multiple: $12\times$ Year 4 FCF ($12 \times 18 = \$216\text{M}$).
Year 4 total inflow: $18 + 216 = \$234\text{M}$.
$$\text{Enterprise Value} = \frac{10}{1.10} + \frac{12}{1.10^2} + \frac{15}{1.10^3} + \frac{234}{1.10^4}$$

**Keystrokes:** `{{res:sc32_11_financial_tvm_seq_18:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_18:value}}`**.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `10 {{key:ENTER}} 1.1 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 9.09 | `9.09_` |
| 02 | `12 {{key:ENTER}} 1.1 {{key:x²}} {{key:÷}}` | 0.00 | 0.00 | 9.09 | 9.92 | `9.92_` |
| 03 | `{{key:+}}` | 0.00 | 0.00 | 0.00 | 19.01 | `19.01_` |
| 04 | `15 {{key:ENTER}} 1.1 {{key:ENTER}} 3 {{key:yˣ}} {{key:÷}}` | 19.01 | 19.01 | 19.01 | 11.27 | `11.27_` |
| 05 | `{{key:+}}` | 19.01 | 19.01 | 19.01 | 30.28 | `30.28_` |
| 06 | `234 {{key:ENTER}} 1.1 {{key:ENTER}} 4 {{key:yˣ}} {{key:÷}}` | 30.28 | 30.28 | 30.28 | 159.83 | `159.83_` |
| 07 | `{{key:+}}` | 30.28 | 30.28 | 30.28 | 190.11 | `190.11` |

---

### Problem 11.13: Weighted Average Cost of Capital (WACC)
Equity capital $\$60.0\text{M}$ ($60\%$) at required equity return $K_e = 12.0\%$; Debt capital $\$40.0\text{M}$ ($40\%$) at pre-tax interest rate $K_d = 6.0\%$; Corporate income tax rate $t = 25\%$.
$$\text{WACC} = \left(\frac{E}{V}\right) K_e + \left(\frac{D}{V}\right) K_d (1 - t)$$

**Keystrokes:**
1. After-tax debt cost: `{{res:sc32_11_financial_tvm_seq_19:keys}}` $\rightarrow$ $4.50\%$
2. Debt weight: `.40 {{key:×}}` $\rightarrow$ $1.80\%$
3. Equity contribution: `{{res:sc32_11_financial_tvm_seq_20:keys}}` $\rightarrow$ $7.20\%$
4. Combined: `{{key:+}}` $\rightarrow$ **`9.00%`**.

Keying `6 {{key:ENTER}} 1 {{key:ENTER}} .25 {{key:-}} {{key:×}}` evaluates after-tax debt cost $K_d(1-t) = 4.50\%$ in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 4.50)$. Striking `.40 {{key:×}}` weights the debt contribution to $1.80\%$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 1.80)$. Keying `.60 {{key:ENTER}} 12 {{key:×}}` calculates equity contribution $7.20\%$ in $X$ while debt waits in $Y$ $(T: 0.00, Z: 0.00, Y: 1.80, X: 7.20)$. Striking `{{key:+}}` combines both components into the corporate hurdle rate $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{9.00\%})$.

---

### Problem 11.14: Rule of 72 Doubling Time Precision
An investment yields $8.0\%$ annually. Compare the Rule of 72 mental estimate with exact compound TVM:
* Rule of 72 estimate: $72 / 8 = \mathbf{9.00\text{ years}}$.
* Exact TVM Doubling: `8 {{key:I%YR}} 1 {{key:+/-}} {{key:PV}} 0 {{key:PMT}} 2 {{key:FV}} {{key:N}}` $\rightarrow$ **`9.01 years`**.
* Error is under $0.11\%$.

Keying `72 {{key:ENTER}} 8 {{key:÷}}` computes the heuristic Rule of 72 estimate ($9.00\text{ years}$) in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 9.00)$. Storing `8 {{key:I%YR}} 1 {{key:+/-}} {{key:PV}} 0 {{key:PMT}} 2 {{key:FV}}` programs annual rate $8\%$, unit principal $-\$1.00$, and doubled future balance $\$2.00$ $(T: 8.00, Z: -1.00, Y: 0.00, X: 2.00)$. Striking `{{key:N}}` solves the exact compound growth horizon $(T: 8.00, Z: -1.00, Y: 0.00, X: \mathbf{9.01}\text{ years})$.

---

### Problem 11.15: Continuous Compounding ($A = P e^{rt}$)
Deposit $\$10,000.00$ in a treasury note yielding $5.50\%$ compounded continuously for 10 years:
$$A = 10,000 \times e^{0.055 \times 10} = 10,000 \times e^{0.55}$$

**Keystrokes:** `{{res:sc32_11_financial_tvm_seq_21:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_21:value}}`**.

Keying `.055 {{key:ENTER}} 10 {{key:×}}` evaluates continuous growth exponent $rt = 0.5500$ in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 0.55)$. Striking `{{key:eˣ}}` evaluates continuous accumulation factor $e^{0.55} \approx 1.7333$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 1.73)$. Keying `10000 {{key:×}}` scales by principal balance, resolving maturity value $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{\$17332.53})$.

---

### Problem 11.16: Effective Annual Rate (EAR) from Nominal APR
A revolving credit line charges nominal $21.99\%$ APR compounded daily ($m = 365$):
$$\text{EAR} = \left(1 + \frac{0.2199}{365}\right)^{365} - 1$$

**Keystrokes:** `{{res:sc32_11_financial_tvm_seq_22:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_22:value}}`**.

Keying `.2199 {{key:ENTER}} 365 {{key:÷}} 1 {{key:+}}` evaluates the daily compounding base $1 + i \approx 1.000602$ in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 1.000602)$. Keying `365 {{key:yˣ}}` compounds across 365 daily intervals to yield $1.245870$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 1.25)$. Striking `1 {{key:-}} 100 {{key:×}}` isolates and converts the annual rate, resolving Effective Annual Rate $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{24.59\%})$.

---

### Problem 11.17: Auto Loan Financing with Trade-In
New vehicle price $\$38,500.00$. Trade-in allowance $\$8,500.00$. Net loan principal $PV = \$30,000.00$.
Financing: 60 months ($N=60$) at $4.90\%$ APR ($i = 4.90 / 12 = 0.408333\%$):
Keystrokes: `{{res:sc32_11_financial_tvm_seq_01:keys}}`$\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_01:value}}`**.

> ***The Net Loan Amortization Pipeline*** — Compute monthly periodic vehicle financing rate on the fly and solve the net financed balance ($PV = \$30,000.00$) in one continuous flow {{cite:hp32sii1991}}.

Storing `60 {{key:N}}` sets the 5-year financing term ($60\text{ months}$) into financial register $N$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 60.00)$. Keying `4.9 {{key:ENTER}} 12 {{key:÷}} {{key:I%YR}}` stores monthly rate $0.408333\%$ into register $I\%YR$ $(T: 0.00, Z: 0.00, Y: 60.00, X: 0.41)$. Storing `30000 {{key:PV}} 0 {{key:FV}}` sets net loan principal and zero residual balance $(T: 60.00, Z: 0.41, Y: 30000.00, X: 0.00)$. Striking `{{key:PMT}}` executes TVM solver to establish exact monthly payment $(T: 60.00, Z: 0.41, Y: 30000.00, X: \mathbf{-564.76})$.

---

### Problem 11.18: Equipment Lease vs. Buy Analysis
An industrial CNC milling machine can be leased for $\$12,000.00/\text{year}$ for 5 years at an $8.00\%$ hurdle discount rate. Outright purchase price is $\$52,000.00$.
$$\text{PV of Lease} = 12,000 \times \left[\frac{1 - 1.08^{-5}}{0.08}\right] = \mathbf{\$47,912.52}$$
Leasing saves $\$4,087.48$ in present value terms compared to outright purchase.

**Keystrokes:** `5 {{key:N}} 8 {{key:I%YR}} 12000 {{key:+/-}} {{key:PMT}} 0 {{key:FV}} {{key:PV}}` $\rightarrow$ **`$47,912.52`**.
`52000 {{key:x⇄y}} {{key:-}}` $\rightarrow$ **`$4,087.48`** (Lease savings over purchase).

Storing `5 {{key:N}} 8 {{key:I%YR}} 12000 {{key:+/-}} {{key:PMT}} 0 {{key:FV}}` sets 5-year lease duration, $8.0\%$ hurdle rate, and $\$12,000$ annual payment $(T: 5.00, Z: 8.00, Y: -12000.00, X: 0.00)$. Striking `{{key:PV}}` solves present value of lease stream $(T: 5.00, Z: 8.00, Y: -12000.00, X: \mathbf{47912.52})$. Keying `52000 {{key:x⇄y}} {{key:-}}` evaluates difference against outright purchase, confirming net lease savings of $(T: 5.00, Z: 8.00, Y: 52000.00, X: \mathbf{\$4087.48})$.

---

### Problem 11.19: Dining Bill with 8.25% Tax and 20% Tip
Food and beverage subtotal: $\$164.50$. Regional tax $8.25\%$. Tip $20.0\%$ on pre-tax subtotal.
1. Tax: `{{res:sc32_11_financial_tvm_seq_23:keys}}` $\rightarrow$ $\$13.57$ (Total with tax: `{{key:+}}` $\rightarrow$ $\$178.07$).
2. Tip on pre-tax: `{{res:sc32_11_financial_tvm_seq_24:keys}}` $\rightarrow$ $\$32.90$.
3. Grand total: `{{key:+}}` $\rightarrow$ **`$210.97`**.

Keying `164.50 {{key:ENTER}} {{key:ENTER}} 8.25 {{key:%}} {{key:+}}` stages the subtotal in $Z$, calculates tax $(\$13.57)$, and adds to form taxed total $(\$178.07)$ in $X$ $(T: 0.00, Z: 0.00, Y: 164.50, X: 178.07)$. Striking `{{key:x⇄y}} 20 {{key:%}}` recalls pre-tax base to compute $20\%$ tip $(\$32.90)$ in $X$ while taxed subtotal waits in $Y$ $(T: 0.00, Z: 178.07, Y: 164.50, X: 32.90)$. Striking `{{key:+}}` sums taxed bill and tip into final grand dining total $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{\$210.97})$.

---

### Problem 11.20: 4-Way Bill Split via Stack Roll `{{key:R↓}}`
Grand total $\$210.97$ split equally among 4 dinner guests:
Keystrokes: `{{res:sc32_11_financial_tvm_seq_02:keys}}`$\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_02:value}}`**.

> ***The Table Bill Equipartition*** — Enter grand dining total into Register $Y$ and divide across party headcount in a single tactile stroke {{cite:parker2019}}.

Keying `210.97 {{key:ENTER}} 4 {{key:÷}}` divides grand dining total across party headcount $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{\$52.74})$, establishing per-person share instantly.

---

> **Thematic Arc III — Capital Budgeting, Refinancing & Sinking Funds (Problems 11.21–11.30):** Multi-stage financial workflows where intermediate TVM outputs feed directly into RPN stack comparisons.

### Problem 11.21: Banquet Check Split with Itemized Wine Separation
Table grand total is $\$480.00$. Three of the eight guests shared two reserve bottles of wine totaling $\$96.00$.
1. Shared food subtotal: `{{res:sc32_11_financial_tvm_seq_25:keys}}` $\rightarrow$ $\$384.00$. Split 8 ways: `8 {{key:÷}}` $\rightarrow$ $\$48.00$ base per person.
2. Wine drinkers' share: `{{res:sc32_11_financial_tvm_seq_26:keys}}` $\rightarrow$ $\$32.00$ wine share.
3. Total for wine drinkers: `48 {{key:+}}` $\rightarrow$ **`$80.00`** each. Non-wine drinkers pay **`$48.00`** each.

Keying `480 {{key:ENTER}} 96 {{key:-}} 8 {{key:÷}}` isolates food subtotal $(\$384.00)$ and divides across 8 guests to establish base share $(\$48.00)$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 48.00)$. Keying `96 {{key:ENTER}} 3 {{key:÷}}` evaluates wine surcharge per wine drinker $(\$32.00)$ in $X$ while base share waits in $Y$ $(T: 0.00, Z: 0.00, Y: 48.00, X: 32.00)$. Striking `{{key:+}}` combines shares into total for wine drinkers $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{\$80.00})$ each, while non-wine guests pay $\$48.00$.

---

### Problem 11.22: Retail Store Double Discount
Designer jacket list price $\$280.00$. Store offers $30\%$ seasonal sale, plus an additional $15\%$ VIP coupon:
1. First discount: `{{res:sc32_11_financial_tvm_seq_27:keys}}` $\rightarrow$ $X = 84.00$. Net: `{{key:-}}` $\rightarrow$ $\$196.00$.
2. VIP discount: `15 {{key:%}}` $\rightarrow$ $X = 29.40$. Net: `{{key:-}}` $\rightarrow$ **`$166.60`**.
(Effective total discount: $(280 - 166.60)/280 = 40.5\%$, NOT $45\%$).

Keying `280 {{key:ENTER}} 30 {{key:%}} {{key:-}}` evaluates $30\%$ discount $(\$84.00)$ and deducts from list price, leaving intermediate price $(\$196.00)$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 196.00)$. Keying `15 {{key:%}} {{key:-}}` applies $15\%$ VIP discount $(\$29.40)$ to intermediate price, resolving final payable price $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{\$166.60})$ (effective $40.5\%$ discount).

---

### Problem 11.23: Culinary Recipe Scaling with Fractions
A cake recipe yields 8 servings and calls for $2\text{-}1/2\text{ cups}$ of flour ($2.5\text{ cups}$).
Scale recipe to serve 14 guests:
1. Scaling factor: `{{res:sc32_11_financial_tvm_seq_05:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_05:value}}`**
2. Flour required: `{{res:sc32_11_financial_tvm_seq_28:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_28:value}}`** ($4\text{-}3/8\text{ cups}$).

Keying `14 {{key:ENTER}} 8 {{key:÷}}` establishes recipe scaling multiplier $1.75\times$ in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 1.75)$. Keying `2.5 {{key:×}}` scales base flour requirement, yielding scaled ingredient volume $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{4.38}\text{ cups})$ ($4\text{-}3/8\text{ cups}$).

---

### Problem 11.24: Kitchen Unit Volume Conversions
Convert $3.5\text{ fluid ounces}$ to tablespoons ($1\text{ fl oz} = 2\text{ tbsp}$), then to teaspoons ($1\text{ tbsp} = 3\text{ tsp}$):
* Tablespoons: `{{res:sc32_11_financial_tvm_seq_29:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_29:value}}`**

> ***The Kitchen Metric Cascading Pipeline*** — Scale volumetric culinary measures seamlessly across fluid ounces, tablespoons, and teaspoons without re-entering intermediate totals.

Keying `3.5 {{key:ENTER}} 2 {{key:×}}` converts fluid ounces to tablespoons $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{7.00}\text{ tbsp})$. Striking `3 {{key:×}}` scales tablespoons to teaspoons $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{21.00}\text{ tsp})$ without re-entering intermediate values.

---

### Problem 11.25: Bookshelf Bay Spacing with Dividers
Alcove width $47\text{-}5/8^{\prime\prime}$ ($47.625^{\prime\prime}$). Two $3/4^{\prime\prime}$ ($0.75^{\prime\prime}$) upright dividers create 3 equal bays:
`{{res:sc32_11_financial_tvm_seq_30:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_30:value}}`**.

> ***The Inside-Out Alcove Partition*** — Deposit total alcove span into the stack, compute cumulative divider thickness in $X$, subtract to find net clear span, and divide into equal bays without manual scratchwork {{cite:hp15c1982}}.

Keying `47.625 {{key:ENTER}} .75 {{key:ENTER}} 2 {{key:×}} {{key:-}}` subtracts two $0.75^{\prime\prime}$ uprights $(1.50^{\prime\prime})$ from total alcove span $(47.625^{\prime\prime})$, leaving clear span $46.125^{\prime\prime}$ in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 46.13)$. Striking `3 {{key:÷}}` divides net clear span into 3 equal bays, resolving clear bay width $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{15.38^{\prime\prime}})$ ($15\text{-}3/8^{\prime\prime}$).

---

### Problem 11.26: Woodworking Saw Kerf Accumulation
Cut 5 identical table legs of length $28\text{-}1/4^{\prime\prime}$ ($28.25^{\prime\prime}$) from a single board. The miter saw blade has a kerf thickness of $1/8^{\prime\prime}$ ($0.125^{\prime\prime}$). There are 4 intermediate cuts:
`{{res:sc32_11_financial_tvm_seq_31:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_31:value}}`**.

***The Lumber Kerf Dual-Branch Accumulator*** — Evaluate raw leg length and saw kerf loss in separate stack registers and sum directly into total stock required.

Keying `28.25 {{key:ENTER}} 5 {{key:×}}` computes finished leg stock $(141.25^{\prime\prime})$ in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 141.25)$. Keying `.125 {{key:ENTER}} 4 {{key:×}}` evaluates kerf waste $(0.50^{\prime\prime})$ across 4 intermediate cuts in $X$, lifting stock length to $Y$ $(T: 0.00, Z: 0.00, Y: 141.25, X: 0.50)$. Striking `{{key:+}}` sums finished lumber and kerf loss into total required board stock $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{141.75^{\prime\prime}})$ ($11\text{ ft } 9\text{-}3/4^{\prime\prime}$).

---

### Problem 11.27: Staircase Riser and Tread Layout
Total vertical rise from finished basement floor to main level is $108\text{ inches}$ ($9\text{ ft}$).
Building code requires individual riser height $h \le 7\text{-}3/4^{\prime\prime}$ ($7.75^{\prime\prime}$):
1. Target risers: `{{res:sc32_11_financial_tvm_seq_32:keys}}` $\rightarrow$ $13.935 \implies$ Round up to **`14 risers`**.
2. Exact riser height: `{{res:sc32_11_financial_tvm_seq_33:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_33:value}}`**.

Keying `108 {{key:ENTER}} 7.75 {{key:÷}}` estimates riser count ($13.94$) in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 13.94)$, rounded up to 14 risers. Keying `108 {{key:ENTER}} 14 {{key:÷}}` evaluates exact unit riser height $(T: 0.00, Z: 0.00, Y: 13.94, X: \mathbf{7.71^{\prime\prime}})$ ($7\text{-}23/32^{\prime\prime}$).

---

### Problem 11.28: Blueprint Scale Conversion ($1/4^{\prime\prime} = 1^{\prime}\text{-}0^{\prime\prime}$)
Wall on drawing measures $5\text{-}3/8^{\prime\prime}$ ($5.375^{\prime\prime}$). Real length ($4\text{ ft/in}$):
`{{res:sc32_11_financial_tvm_seq_34:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_34:value}}`**.

***The Architectural Scale Expansion*** — Transform blueprint fractional inches directly to field feet without unit conversion tables.

Keying `5.375 {{key:ENTER}} 4 {{key:×}}` scales the drawing dimension by architectural factor ($4\text{ ft/in}$), converting fractional inches directly to field length $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{21.50}\text{ ft})$.

---

### Problem 11.29: Model Railroading HO Scale (1:87.1)
Real locomotive length is $72\text{ feet}$ ($864\text{ inches}$). In HO scale:
`{{res:sc32_11_financial_tvm_seq_35:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_35:value}}`**.

***The Scale Model Ratio Pipeline*** — Load prototype dimensions and divide by scale ratio to verify miniature modeling tolerances.

Keying `864 {{key:ENTER}} 87.1 {{key:÷}}` divides prototype length ($864^{\prime\prime}$) by scale ratio, resolving model dimension $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{9.92^{\prime\prime}})$.

---

### Problem 11.30: Fuel Economy MPG to L/100km Conversion
Formula: $\text{L/100km} = \frac{235.214583}{\text{MPG}}$.
Convert $32.0\text{ MPG}$:
`{{res:sc32_11_financial_tvm_seq_36:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_36:value}}`**.

***The International Fuel Standard Inversion*** — Load the US/metric conversion invariant and divide by vehicle MPG in one reciprocal stroke.

Keying `235.215 {{key:ENTER}} 32 {{key:÷}}` divides international conversion invariant by vehicle fuel economy, resolving metric consumption $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{7.35}\text{ L/100km})$.

---

> **Thematic Arc IV — Real vs. Nominal Returns, Depreciation & SaaS Unit Economics (Problems 11.31–11.48):** The closing eighteen problems evaluate Fisher inflation adjustments, MACRS schedules, NPV/IRR hurdles, and corporate valuation multiples.

### Problem 11.31: Cumulative Inflation and Purchasing Power
Annual inflation averages $3.2\%$ over 20 years. What will $\$100,000$ in today's currency be worth?
$$PV = \frac{100,000}{(1.032)^{20}}$$
Keystrokes: `{{res:sc32_11_financial_tvm_seq_03:keys}}`$\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_03:value}}`** (Purchasing power cut nearly in half!).

***The Constant-in-Z Inflation Pipeline*** — Hold initial capital in $Z$, evaluate cumulative compound inflation $(1 + r)^N$ in $X$, and collapse via single division without losing precision {{cite:ellenberg2014}}.

Keying `100000 {{key:ENTER}} 1.032 {{key:ENTER}} 20 {{key:yˣ}}` evaluates 20-year inflation compound factor ($1.8776$) in $X$ while capital waits in $Y$ $(T: 0.00, Z: 0.00, Y: 100000.00, X: 1.88)$. Striking `{{key:÷}}` deflates nominal capital, resolving future purchasing power $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{\$53260.60})$.

---

### Problem 11.32: Foreign Currency Exchange Fee and Spread
Traveler converts $\$2,000\text{ USD}$ to Euros. Interbank rate is $1.085\text{ EUR/USD}$. Bank charges a $2.5\%$ FX spread fee:
`{{res:sc32_11_financial_tvm_seq_37:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_37:value}}`**.

***The Non-Destructive FX Margin Pipeline*** — Apply bank transaction spread via Kahan percentage invariant, deduct fee, and multiply interbank conversion rate in continuous motion {{cite:kahan1979}}.

Keying `2000 {{key:ENTER}} 2.5 {{key:%}} {{key:-}}` evaluates $2.5\%$ FX bank fee $(\$50.00)$ and deducts from budget, leaving net convertible capital $(\$1,950.00)$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 1950.00)$. Keying `1.085 {{key:×}}` multiplies by interbank rate, resolving converted currency $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{2115.75}\text{ EUR})$.

---

### Problem 11.33: Cash Conversion Cycle (CCC)
Days Inventory Outstanding $DIO = 45\text{ days}$; Days Sales Outstanding $DSO = 38\text{ days}$; Days Payables Outstanding $DPO = 52\text{ days}$.
$$\text{CCC} = DIO + DSO - DPO = 45 + 38 - 52 = \mathbf{31\text{ days}}$$

**Keystrokes:** `45 {{key:ENTER}} 38 {{key:+}} 52 {{key:-}}` $\rightarrow$ **`31 days`**.

Keying `45 {{key:ENTER}} 38 {{key:+}} 52 {{key:-}}` sums inventory and receivables days and deducts payables days, resolving net working capital cycle $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{31}\text{ days})$.

---

### Problem 11.34: Enterprise Value (EV) Calculation
Market capitalization $\$450\text{M}$, total debt $\$120\text{M}$, cash and equivalents $\$35\text{M}$.
$$\text{EV} = \text{Market Cap} + \text{Debt} - \text{Cash} = 450 + 120 - 35 = \mathbf{\$535.00M}$$

**Keystrokes:** `450 {{key:ENTER}} 120 {{key:+}} 35 {{key:-}}` $\rightarrow$ **`$535.00M`**.

Keying `450 {{key:ENTER}} 120 {{key:+}} 35 {{key:-}}` adds debt to equity market cap and subtracts cash, resolving total enterprise valuation $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{\$535.00M})$.

---

### Problem 11.35: Sinking Fund Future Savings Goal
Save $\$50,000$ in 5 years ($N=60\text{ months}$) at $6.0\%$ APR ($i = 0.5\%/\text{mo}$):
Keystrokes: `{{res:sc32_11_financial_tvm_seq_04:keys}}`$\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_04:value}}`**.

Storing `60 {{key:N}} .5 {{key:I%YR}} 0 {{key:PV}} 50000 {{key:FV}}` sets 60 monthly periods, $0.5\%$ monthly interest, zero present value, and $\$50,000$ target $(T: 60.00, Z: 0.50, Y: 0.00, X: 50000.00)$. Striking `{{key:PMT}}` computes required monthly savings contribution $(T: 60.00, Z: 0.50, Y: 0.00, X: \mathbf{-716.64})$.

---

### Problem 11.36: College Education Fund Present Value
Annual tuition $\$35,000$ for 4 years ($N=4$, beginning of year `BEGIN` mode) at $5\%$ investment return:
Toggled to `BEGIN` mode: `4 {{key:N}} 5 {{key:I%YR}} 35000 {{key:PMT}} 0 {{key:FV}} {{key:PV}}` $\rightarrow$ **`-$130,417.84`**.

In `BEGIN` mode, storing `4 {{key:N}} 5 {{key:I%YR}} 35000 {{key:PMT}} 0 {{key:FV}}` sets 4 annual tuition payments of $\$35,000$ at $5\%$ return $(T: 4.00, Z: 5.00, Y: 35000.00, X: 0.00)$. Striking `{{key:PV}}` solves required lump-sum funding balance $(T: 4.00, Z: 5.00, Y: 35000.00, X: \mathbf{-\$130417.84})$.

---

### Problem 11.37: Internal Rate of Return (IRR) on Uneven Cash Flows
An infrastructure venture requires an upfront outlay of $C_0 = -\$100,000.00$. It generates subsequent year-end inflows: $C_1 = \$30,000.00, C_2 = \$40,000.00, C_3 = \$50,000.00$. Determine the project's Internal Rate of Return ($IRR$) where $NPV = 0$:

$$NPV(r) = -100000 + \frac{30000}{1+r} + \frac{40000}{(1+r)^2} + \frac{50000}{(1+r)^3} = 0$$

Let discount factor $x = 1+r$. In `{{key:EQN}}` mode, program the polynomial in $x$:
`50000 X {{key:÷}} 40000 {{key:+}} X {{key:÷}} 30000 {{key:+}} X {{key:÷}} 100000 {{key:-}}`
Using Brent's numerical solver `{{key:SOLVE}} X` with initial guess $x = 1.10$:
The solver converges to $x = 1.08889 \implies r = x - 1 = \mathbf{8.89\%}$.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `1.10 {{key:STO}} X` | 0.00 | 0.00 | 0.00 | 1.10 | `1.10` |
| 02 | `{{key:SOLVE}}X` | 0.00 | 0.00 | 1.10 | 1.08889 | `1.08889` |
| 03 | `1 {{key:-}}` | 0.00 | 0.00 | 1.10 | 0.08889 | `0.08889` |
| 04 | `100 {{key:×}}` | 0.00 | 0.00 | 1.10 | 8.89 | `8.89` |

---

### Problem 11.38: Net Present Value (NPV) Comparison of Capital Projects
A company evaluates two mutually exclusive industrial automation projects with a $12.0\%$ hurdle rate:
**Project Alpha:** Initial Cost $\$80,000.00$; Inflows: $\$35,000/\text{yr}$ for 3 years.
**Project Beta:** Initial Cost $\$120,000.00$; Inflows: $\$52,000/\text{yr}$ for 3 years.

$$\text{PV Annuity Factor} = \frac{1 - (1.12)^{-3}}{0.12} = \frac{1 - 0.71178}{0.12} \approx 2.40183$$
* Project Alpha: $35,000 \times 2.40183 - 80,000 = \$84,064.10 - \$80,000 = \mathbf{+\$4,064.10}$.
* Project Beta: $52,000 \times 2.40183 - 120,000 = \$124,895.22 - \$120,000 = \mathbf{+\$4,895.22}$.
Project Beta delivers $\$831.12$ more net present value to shareholders.

**Keystrokes:** **Project Alpha:** `3 {{key:N}} 12 {{key:I%YR}} 35000 {{key:+/-}} {{key:PMT}} 0 {{key:FV}} {{key:PV}}` $\rightarrow$ $PV = \$84,064.10$. Then `80000 {{key:-}}` $\rightarrow$ **`+$4,064.10`**.
**Project Beta:** `52000 {{key:+/-}} {{key:PMT}} {{key:PV}}` $\rightarrow$ $PV = \$124,895.22$. Then `120000 {{key:-}}` $\rightarrow$ **`+$4,895.22`**.

For Project Alpha: Storing `3 {{key:N}} 12 {{key:I%YR}} 35000 {{key:+/-}} {{key:PMT}} 0 {{key:FV}} {{key:PV}}` computes inflow present value $(\$84,064.10)$ $(T: 3.00, Z: 12.00, Y: -35000.00, X: 84064.10)$. Subtracting `80000 {{key:-}}` yields net present value $(T: 3.00, Z: 12.00, Y: -35000.00, X: \mathbf{+\$4064.10})$. For Project Beta: Entering `52000 {{key:+/-}} {{key:PMT}} {{key:PV}}` updates inflow PV to $\$124,895.22$ $(T: 12.00, Z: -35000.00, Y: 4064.09, X: 124895.22)$. Subtracting `120000 {{key:-}}` resolves net present value $(T: 3.00, Z: 12.00, Y: -52000.00, X: \mathbf{+\$4895.22})$, delivering $\$831.12$ greater shareholder value over Project Alpha.

---

### Problem 11.39: Capital Budgeting Profitability Index (PI)
Using the present value of inflows from Problem 11.38:
$$\text{Profitability Index (PI)} = \frac{\text{PV of Future Inflows}}{\text{Initial Investment}}$$
* Project Alpha: $84,064.10 \div 80,000.00 = \mathbf{1.0508}$ ($1.05\text{x}$)
* Project Beta: $124,895.22 \div 120,000.00 = \mathbf{1.0408}$ ($1.04\text{x}$)
Although Project Beta has higher absolute NPV, Project Alpha delivers higher capital efficiency per dollar invested!

**Keystrokes:** **Project Alpha PI:** `84064.10 {{key:ENTER}} 80000 {{key:÷}}` $\rightarrow$ **`1.0508`**.
**Project Beta PI:** `124895.22 {{key:ENTER}} 120000 {{key:÷}}` $\rightarrow$ **`1.0408`**.

For Project Alpha: Keying `84064.10 {{key:ENTER}} 80000 {{key:÷}}` evaluates capital efficiency ratio $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{1.0508}\text{x})$. For Project Beta: Keying `124895.22 {{key:ENTER}} 120000 {{key:÷}}` evaluates capital efficiency ratio $(T: 0.00, Z: 0.00, Y: 1.05, X: \mathbf{1.0408}\text{x})$, demonstrating that Project Alpha extracts higher return per dollar invested.

---

### Problem 11.40: Macaulay and Modified Duration of an Investment-Grade Bond
Calculate the interest rate sensitivity (Modified Duration) of a 3-year $8.0\%$ annual coupon bond trading at par ($\$1,000.00$) with yield $y = 8.0\%$:
$$\text{Macaulay Duration } D = \frac{1 \times 80/1.08 + 2 \times 80/1.08^2 + 3 \times 1080/1.08^3}{1000} = \mathbf{2.783\text{ years}}$$
$$\text{Modified Duration } D^* = \frac{D}{1 + y} = \frac{2.783}{1.08} = \mathbf{2.577\text{ years}}$$
A $100\text{ bps}$ ($1.0\%$) rise in market interest rates causes approximately a $2.58\%$ decline in bond price.

**Keystrokes:** `80 {{key:ENTER}} 1.08 {{key:÷}} 80 {{key:ENTER}} 1.08 {{key:ENTER}} 2 {{key:yˣ}} {{key:÷}} 2 {{key:×}} {{key:+}} 1080 {{key:ENTER}} 1.08 {{key:ENTER}} 3 {{key:yˣ}} {{key:÷}} 3 {{key:×}} {{key:+}} 1000 {{key:÷}}` $\rightarrow$ **`2.7833 years`** (Macaulay Duration $D$).
`1.08 {{key:÷}}` $\rightarrow$ **`2.5771 years`** (Modified Duration $D^*$).

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `80 {{key:ENTER}} 1.08 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 74.0741 | `74.07` |
| 02 | `80 {{key:ENTER}} 1.08 {{key:ENTER}} 2 {{key:yˣ}} {{key:÷}} 2 {{key:×}} {{key:+}}` | 74.07 | 74.07 | 74.07 | 211.2483 | `211.25` |
| 03 | `1080 {{key:ENTER}} 1.08 {{key:ENTER}} 3 {{key:yˣ}} {{key:÷}} 3 {{key:×}} {{key:+}}` | 211.25 | 211.25 | 211.25 | 2783.2648 | `2783.26` |
| 04 | `1000 {{key:÷}}` | 211.25 | 211.25 | 211.25 | 2.7833 | `2.7833` |
| 05 | `1.08 {{key:÷}}` | 211.25 | 211.25 | 211.25 | 2.5771 | `2.5771` |

---

### Problem 11.41: MACRS 5-Year Depreciation Schedule
A technology enterprise purchases $\$250,000.00$ of server hardware depreciated under IRS 5-Year MACRS ($20.0\%, 32.0\%, 19.2\%, 11.52\%, 11.52\%, 5.76\%$):
* Year 1 Deduction: `{{res:sc32_11_financial_tvm_seq_38:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_38:value}}`** (Remaining basis: `{{key:-}}` $\rightarrow$ $\$200,000.00$).

***The Non-Destructive Asset Basis Stream*** — Evaluate IRS MACRS depreciation percentage while freezing asset purchase cost in Register $Y$ for sequential tax deductions {{cite:hp15c1982}}.

Keying `250000 {{key:ENTER}} 20 {{key:%}}` computes Year 1 deduction $(\$50,000.00)$ in $X$ while freezing cost basis $(\$250,000.00)$ in Register $Y$ $(T: 0.00, Z: 0.00, Y: 250000.00, X: 50000.00)$. Striking `{{key:-}}` subtracts deduction from preserved basis, resolving remaining asset book value $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{\$200000.00})$.

---

### Problem 11.42: Staircase Stringer Layout with 1/16" Carpentry Cuts
Total vertical rise is $105\text{-}1/2^{\prime\prime}$ ($105.5^{\prime\prime}$). Target riser height is $7\text{-}1/4^{\prime\prime}$ ($7.25^{\prime\prime}$):
1. Riser count: `{{res:sc32_11_financial_tvm_seq_42:keys}}` $\rightarrow$ $14.55 \implies$ Round to **`15 risers`**.
2. Exact riser height: `{{res:sc32_11_financial_tvm_seq_43:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_43:value}}`**.
3. Decompose to nearest $1/16^{\prime\prime}$:
   Fractional part: `7 {{key:-}} 16 {{key:×}}` $\rightarrow$ $0.5333 \approx 1/16^{\prime\prime} \implies$ Cut stringers at **`7-1/16"`** (exact rise $7.0625^{\prime\prime} \times 15 = 105.94^{\prime\prime}$, adjusted on bottom tread).

Keying `105.5 {{key:ENTER}} 7.25 {{key:÷}}` determines target riser count ($14.55 \to 15\text{ risers}$) in Register $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 14.55)$. Keying `105.5 {{key:ENTER}} 15 {{key:÷}}` evaluates exact unit riser height $7.0333^{\prime\prime}$ $(T: 0.00, Z: 0.00, Y: 14.55, X: 7.03)$. Keying `7 {{key:-}} 16 {{key:×}}` extracts fractional rise $0.5333/16^{\prime\prime}$ $(T: 0.00, Z: 0.00, Y: 14.55, X: 0.53)$, directing carpentry cuts at **$7\text{-}1/16^{\prime\prime}$**.

---

### Expedition 6: The Executive Boardroom, Realtor Open-House & Trading Desk Playbook (Problems 11.43–11.48)

*Executive & Desk Briefing:* Whether you are a Chief Executive Officer auditing unit economics during a board meeting, a commercial or residential realtor structuring an offer at an open house, or a quantitative trader sizing a position under market volatility, you do not have time to open a laptop spreadsheet. These six high-velocity RPN workflows turn the SC-32 into an unfair tactical advantage in any negotiation.

### Problem 11.43: The CEO's Gross Margin vs. Markup Trap
A hardware product has a landed bill-of-materials cost of $C = \$60.00$. The board mandates a **$40.0\%$ Gross Margin** on retail sales.
**The Amateur Markup Trap:** Adding $40\%$ on top of $\$60.00$ (`{{res:sc32_11_exec_markup_trap:keys}}` $\rightarrow$ **`\${{res:sc32_11_exec_markup_trap:value}}`**) yields only $\$24.00 / \$84.00 = 28.57\%$ gross margin—destroying profitability!

***The Executive Margin vs. Markup Invariant*** — Contrast naive markup addition against genuine gross margin pricing using non-destructive stack registers {{cite:parker2019,ellenberg2014}}.

**True Gross Margin Pricing:** Selling price must satisfy $\text{Price} = \frac{\text{Cost}}{1 - \text{Margin}}$:
  `{{res:sc32_11_exec_gross_margin_price:keys}}` $\rightarrow$ **`\${{res:sc32_11_exec_gross_margin_price:value}}`**.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `60 {{key:ENTER}} 40 {{key:%}}` | 0.00 | 0.00 | 60.00 | 24.00 | 40% markup on \$60.00 cost: \$24.00 |
| 02 | `{{key:+}}` | 0.00 | 0.00 | 0.00 | 84.00 | Flawed markup price: \$84.00 (28.57% margin) |
| 03 | `60 {{key:ENTER}} 1` | 0.00 | 84.00 | 60.00 | 1.00 | True margin pricing: load cost \$60 and 1.00 |
| 04 | `.40 {{key:-}}` | 84.00 | 84.00 | 60.00 | 0.60 | 1 - 0.40 = 0.60 margin complement |
| 05 | `{{key:÷}}` | 84.00 | 84.00 | 84.00 | 100.00 | True gross margin retail price: \$100.00 |

---

### Problem 11.44: SaaS Unit Economics — LTV : CAC Ratio in One Chain
A B2B software enterprise generates Average Revenue Per User $\text{ARPU} = \$250.00/\text{month}$ at an $80.0\%$ gross margin, with monthly revenue churn $c = 2.5\%$ ($0.025$) and Customer Acquisition Cost $\text{CAC} = \$1,600.00$:
$$\text{LTV} = \frac{\text{ARPU} \times \text{GM}\%}{\text{Churn}} = \frac{250 \times 0.80}{0.025} = \$8,000.00, \qquad \frac{\text{LTV}}{\text{CAC}} = \frac{8000}{1600} = \mathbf{5.00\text{x}}$$
**Boardroom RPN Keystrokes:** `{{res:sc32_11_exec_saas_ltv_cac:keys}}` $\rightarrow$ **`{{res:sc32_11_exec_saas_ltv_cac:value}}`**.

***The SaaS Unit Economics Stream*** — Cascade gross margin, churn capitalization, and customer acquisition cost in one unbroken pipeline {{cite:ellenberg2014}}.

Entering monthly ARPU `250 {{key:ENTER}}` pushes $\$250.00$ to Register $Y$ $(T: 0.00, Z: 0.00, Y: 250.00, X: 250.00)$. Striking `80 {{key:%}}` computes monthly gross profit $(\$200.00)$ while preserving base ARPU in $Y$ $(T: 0.00, Z: 0.00, Y: 250.00, X: 200.00)$. Dividing by monthly revenue churn `0.025 {{key:÷}}` evaluates customer lifetime value $(\text{LTV} = \$8,000.00)$ in Register $X$ $(T: 0.00, Z: 0.00, Y: 250.00, X: 8000.00)$. Dividing by acquisition cost `1600 {{key:÷}}` yields the boardroom unit economics ratio $(T: 0.00, Z: 0.00, Y: 250.00, X: \mathbf{5.00}\text{x})$, verifying a stellar capital payback profile.

---

### Problem 11.45: Operating Breakeven Volume ($Q_{\text{BE}}$)
A manufacturing line carries annual fixed overhead of $F = \$420,000.00$. Each unit sells for $P = \$85.00$ with variable unit cost $V = \$35.00$ (contribution margin $\$50.00/\text{unit}$):
$$Q_{\text{BE}} = \frac{F}{P - V} = \frac{420,000}{85 - 35}$$
**Keystrokes:** `{{res:sc32_11_exec_breakeven_units:keys}}` $\rightarrow$ **`{{res:sc32_11_exec_breakeven_units:value}}`**.

***The Constant-in-Z Breakeven Division*** — Position annual fixed overhead in $Z$, subtract unit variable cost from selling price in $X$, and collapse directly to volume breakeven.

Loading fixed operating overhead `420000 {{key:ENTER}}` places $\$420,000.00$ into $Y$ $(T: 0.00, Z: 0.00, Y: 420000.00, X: 420000.00)$. Keying selling price `85 {{key:ENTER}}` lifts fixed overhead into $Z$ $(T: 0.00, Z: 420000.00, Y: 85.00, X: 85.00)$. Subtracting unit variable cost `35 {{key:-}}` yields unit contribution margin $(\$50.00)$ in $X$ $(T: 0.00, Z: 0.00, Y: 420000.00, X: 50.00)$. Striking `{{key:÷}}` divides preserved overhead by unit contribution margin, resolving operating breakeven volume $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{8400}\text{ units})$.

---

### Problem 11.46: The Realtor's Open-House Extra-Principal Payoff Hack
At an open house, a buyer is hesitant about the 30-year ($360\text{-month}$) commitment on the $\$350,000.00$ mortgage at $6.75\%$ APR ($PMT = -\$2,270.09/\text{mo}$ from Problem 11.7). Show them in 4 keystrokes what happens if they add just **$\$250.00/\text{month}$** in extra principal ($PMT = -\$2,520.09/\text{mo}$):
**Keystrokes:** `{{res:sc32_11_realtor_extra_principal_months:keys}}` $\rightarrow$ **`{{res:sc32_11_realtor_extra_principal_months:value}}` months** ($22.6\text{ years}$).

***The Accelerated Amortization Horizon*** — Re-solve TVM periods with augmented payment to demonstrate accelerated equity buildup in front of clients {{cite:hp15c1982,hp32sii1991}}.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `6.75 {{key:ENTER}} 12 {{key:÷}} {{key:I%YR}}` | 0.00 | 0.00 | 0.00 | 0.56 | Monthly rate i = 0.5625% |
| 02 | `350000 {{key:PV}} 0 {{key:FV}}` | 0.00 | 0.56 | 350000.00 | 0.00 | Store PV = \$350,000.00, FV = \$0.00 |
| 03 | `2520.09 {{key:+/-}} {{key:PMT}}` | 0.56 | 350000.00 | 0.00 | -2520.09 | Augmented payment: -\$2,520.09/mo |
| 04 | `{{key:N}}` | 0.56 | 350000.00 | 0.00 | 270.93 | Accelerated repayment: 270.93 months |

**Open-House Closing Impact:** Adding $\$250/\text{month}$ eliminates **$89\text{ monthly payments}$ ($7.4\text{ years}$)** and saves **$\$134,474.66$** in lifetime interest!

---

### Problem 11.47: Commercial Real Estate Net Operating Income (NOI) & Cap Rate
An apartment building generates Gross Scheduled Rent of $\$112,500.00/\text{year}$ with a $28.0\%$ operating expense + vacancy ratio, offered at an asking price of $\$1,250,000.00$:
$$\text{NOI} = 112,500 \times (1 - 0.28) = \$81,000.00, \qquad \text{Cap Rate} = \frac{\text{NOI}}{\text{Price}} \times 100$$
**Keystrokes:** `{{res:sc32_11_realtor_cap_rate:keys}}` $\rightarrow$ **`{{res:sc32_11_realtor_cap_rate:value}}`**.

***The Commercial Capitalization Stream*** — Evaluate Net Operating Income via Kahan percentage deduction and divide by acquisition asking price in continuous flow {{cite:kahan1979,ellenberg2014}}.

Entering gross scheduled rent `112500 {{key:ENTER}}` and computing expense reserve `28 {{key:%}}` evaluates operating costs $(\$31,500.00)$ in $X$ while freezing gross rent in $Y$ $(T: 0.00, Z: 0.00, Y: 112500.00, X: 31500.00)$. Striking `{{key:-}}` deducts operating expenses, forming Net Operating Income $(\text{NOI} = \$81,000.00)$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 81000.00)$. Keying asking price and dividing `1250000 {{key:÷}}` computes capitalization ratio $0.0648$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 0.0648)$. Scaling by `100 {{key:×}}` yields the commercial cap rate $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{6.48}\%)$.

---

### Problem 11.48: Quantitative Trading Desk — Sharpe Ratio & Kelly Criterion Sizing
1. **Ex-Post Sharpe Ratio:** A systematic portfolio returns $R_p = 18.5\%$ while the risk-free Treasury bill rate is $R_f = 4.5\%$, with annualized return volatility $\sigma_p = 11.2\%$:
   $$\text{Sharpe} = \frac{R_p - R_f}{\sigma_p}$$
**Keystrokes:** `{{res:sc32_11_trader_sharpe_ratio:keys}}` $\rightarrow$ **`{{res:sc32_11_trader_sharpe_ratio:value}}`**.
2. **Kelly Criterion Optimal Position Size ($f^*$):** A trade setup has historical win rate $p = 0.56$ (loss rate $q = 0.44$) and average win-to-loss payoff ratio $b = 1.50$:
   $$f^* = \frac{b p - q}{b} \times 100$$
**Keystrokes:** `{{res:sc32_11_trader_kelly_criterion:keys}}` $\rightarrow$ **`{{res:sc32_11_trader_kelly_criterion:value}}`** of risk capital (most desk traders allocate "Half-Kelly" $= 13.33\%$ to dampen drawdown variance).

For the Sharpe Ratio: Subtracting risk-free rate `18.5 {{key:ENTER}} 4.5 {{key:-}}` yields excess portfolio return $(14.00\%)$ in $X$ $(T: 0.00, Z: 0.00, Y: 0.00, X: 14.00)$. Dividing by volatility `11.2 {{key:÷}}` resolves the ex-post Sharpe ratio $(T: 0.00, Z: 0.00, Y: 0.00, X: \mathbf{1.25})$. For Kelly Sizing: Evaluating the payoff product `1.5 {{key:ENTER}} 0.56 {{key:×}}` places $bp = 0.84$ in $X$ $(T: 0.00, Z: 0.00, Y: 1.25, X: 0.84)$. Subtracting loss rate `0.44 {{key:-}}` forms net expected advantage $0.40$ $(T: 0.00, Z: 0.00, Y: 1.25, X: 0.40)$. Dividing by payoff ratio `1.5 {{key:÷}}` and scaling `100 {{key:×}}` yields optimal full-Kelly allocation $(T: 0.00, Z: 0.00, Y: 1.25, X: \mathbf{26.67}\%)$, directing a disciplined Half-Kelly position size of $13.33\%$.
---

## Summary & Looking Ahead

Chapter 11 integrated executive-grade financial analysis into the scientific RPN workflow. By mastering the five-variable Time Value of Money solver ($N, I\%YR, PV, PMT, FV$), you navigated compound interest growth, accelerated mortgage amortization schedules, commercial real estate capitalization rates, and portfolio risk metrics such as the Sharpe ratio and Kelly criterion. Guided by strict actuarial sign discipline and Register $Y$ preservation during percentage operations, complex multi-year financial flows resolved with speed and mathematical precision.

While tabular financial schedules and discrete numerical outputs provide exact answers, engineering analysis often demands visualizing how mathematical functions behave across continuous domains. In **Chapter 12: Function Evaluation & 64-Point Vector Scatter Plotting**, you will harness the SC-32's transflective graphic vector display engine. You will sample mathematical expressions across custom intervals, render 64-point vector curve plots on the transflective screen, trace critical peaks and zero-crossings with interactive crosshairs, and overlay empirical statistical scatter points.

