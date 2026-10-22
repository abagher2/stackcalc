---
title: "Chapter 11: Financial Mathematics, Executive Analytics & TVM | SC-32 Manual"
description: "Master the 5-variable Time Value of Money (TVM) solver, the Kahan base-preserving percentage invariant, cross-metric elasticity, corporate DCF, and everyday carry math on the StackCalc SC-32."
---

# Chapter 11: Financial Mathematics, Executive Analytics & TVM

## The Time Value of Money & William Kahan's Financial Invariant

Beyond digits in a bank ledger, **money represents stored human time and labor**. 

When an engineer signs an employment contract, an entrepreneur secures an equipment lease, or a family signs a 30-year home mortgage, the mathematics of compound interest dictates whether that labor compounds into generational freedom or evaporates into perpetual interest debt.

### William Kahan and the Base-Preserving Percentage Invariant

In the late 1970s, UC Berkeley Professor and future Turing Award laureate **William M. Kahan** examined how commercial handheld calculators implemented financial percentage keys.

On almost every algebraic calculator of the era, the percentage key was **destructive**. Suppose you were billing a corporate client for $\$150.00$ of engineering consulting, plus an $8.25\%$ state sales tax:

$$\text{Algebraic keystrokes: } 150 \ [\times] \ 8.25 \ [\%] \quad \Longrightarrow \quad \text{Displays } 12.38$$

The moment you pressed `{{key:%}}`, the calculator **overwrote your $\$150.00$ base amount**. To find the invoice total ($\$162.38$), you had to either manually re-enter $\$150.00$, write it down on scratch paper, or rely on a separate memory key (`M+`). If the client asked to test an alternative $9.5\%$ tax rate, you had to start over from scratch.

In 1979, writing in the *Hewlett-Packard Journal* {{cite:kahan1979}}, Kahan formalized what is now known in numerical computing as the **Kahan Percentage Invariant**:

#### The Kahan Percentage Invariant

A percentage operator must be **non-destructive and dyadic**:
$$X \longleftarrow \frac{Y \times X}{100}, \qquad Y \longleftarrow Y \quad (\text{Preserved frozen on the stack})$$

On the StackCalc SC-32, your base amount *never* disappears:
1. **Key in:** `150 {{key:ENTER}} 8.25 {{key:%}}`
   * Register $X$ displays `12.38` (the tax amount).
   * Register $Y$ silently holds `150.00` (the base invoice).
2. **Total Invoice?** Just tap `{{key:+}}` $\to$ `$162.38`.
3. **Discount Subtracted?** Just tap `{{key:-}}` $\to$ `$137.62`.
4. **Alternative Rate?** Tap `{{key:LASTX}} {{key:x⇄y}}` or test alternate taxes directly without re-entry.

{{res:sc32_tvm_pmt:screenshot|Active RPN Calculation on Transflective LCD}}
*Figure 11.1: The SC-32 transflective display executing multi-variable financial calculations with continuous stack preservation.*

{{blocks:sc32_craftsmanship_pureblack|StackCalc SC-32 Pure Black Craftsmanship Edition}}
*Figure 11.2: The SC-32 precision aluminum chassis and tactile key switches, engineered for fatigue-free boardroom and field accounting.*

Beyond simple percentages, all commercial banking, corporate bonds, and mortgages rest on the 5-variable Time Value of Money (TVM) equation:

$$PV + PMT \left[ \frac{1 - (1 + i)^{-N}}{i} \right] + FV (1 + i)^{-N} = 0$$

The SC-32's dedicated TVM register suite frees you from the tyranny of opaque amortization software. You control the five dials of capital.

Consider evaluating the compound interest factor or monthly mortgage annuity payment manually from the fundamental closed-form equation:

$$PMT = PV \cdot \frac{i(1 + i)^N}{(1 + i)^N - 1}$$
On an algebraic textbook calculator, this formula is a minefield of nested parentheses, manual intermediate storage, and operator precedence traps. An analyst must key:

$$\mathrm{PV} \times ((I / 1200) \times (1 + I / 1200)^N) / ((1 + I / 1200)^N - 1)$$
Notice the fatal vulnerabilities: $(I / 1200)$ must be recomputed or stored in scratch memory three separate times; five levels of open parentheses must remain balanced in working memory; and a single missing closing parenthesis triggers a syntax error or a silent erroneous amortization table.

On the StackCalc SC-32, the computation proceeds from the inside out using *The Inside-Out Growth Factor* and *The LASTX Dual-Branch Trick* {{cite:hp15c1982}}. The periodic interest rate $i = I/1200$ is computed once. Adding 1 yields the base $(1 + i)$. Raising to the $N$-th power yields $G = (1 + i)^N$. Tap `{{key:ENTER}}` to duplicate $G$, subtract 1 to form the denominator $(G - 1)$ in Register $X$, and tap `{{key:÷}}` against the numerator branch or use *The x⇄y Denominator Flip*. Every intermediate subtotal is physically visible on the transflective dot-matrix LCD, requiring zero parentheses and zero scratchpad re-entry. To format currency outputs rounded to cents while retaining full 64-bit internal precision, set the display mode to two decimal places (`{{key:FIX}} 2`) via `{{key:DISP}}` $\to$ `{{key:FIX}}` $\to$ `2`.

---

## Financial RPN Workflows: Speed, Clarity & Stack Ledger Discipline

In high-stakes corporate boardrooms, private equity deal evaluations, commercial contract negotiations, and dynamic field estimation, computational latency disrupts quantitative decision-making. 

When an executive using an algebraic calculator (such as a smartphone app, spreadsheet formula line, or standard office desktop unit) attempts to evaluate compound financial relationships, they are forced to mentally manage parenthesis depth, worry about operator precedence, and frequently store intermediate results into disjointed memory keys (`M+`, `MR`, `STO 1`).

Reverse Polish Notation eliminates this parenthetical bookkeeping. The four-level operational stack acts as a visual, transparent ledger where operands are staged, intermediate results are automatically preserved, and dyadic operations consume inputs with zero syntax errors.

### Algebraic Annuity Formulas vs. Cash-Flow Sign Discipline (`{{key:TVM}}` & `{{key:%CHG}}`)

Comparing closed-form infix annuity entry against the SC-32's non-destructive percentage invariant and dedicated 5-variable `{{key:TVM}}` registers illustrates why RPN eliminates parenthetical bookkeeping in financial analysis:

| Challenge / Metric | Conventional Algebraic Calculator (Infix) | Algebraic Strokes | SC-32 RPN Stack Method | SC-32 Strokes | Stack Advantage |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **Sales Tax Total**: $\$150.00$ at $8.25\%$ | `150 * 0.0825 =` $\to \$12.38$. Base $\$150.00$ destroyed; must re-enter `+ 150 =` $\to \$162.38$. Testing alternative $9.5\%$ requires starting completely over. | 18 | **Kahan Non-Destructive `%`**: `150 {{key:ENTER}} 8.25 {{key:%}}` $\to X = 12.38$, $Y = 150.00$ preserved. Tap `{{key:+}}` $\to \$162.38$. Tap `{{key:LASTX}} {{key:x⇄y}}` to test new rates. | 9 | **50% fewer strokes + 100% base preservation** |
| **YoY Growth Spread**: ARR vs CAC | Must compute and write down $(\Delta\text{ARR}\% - \Delta\text{CAC}\%)$. Requires 30+ characters with nested parentheses or 2 disjoint memory slots. | 32 | **Multi-Metric Stack Staging**: Key both metrics via `{{key:%CHG}}`; both rates staged in $Y$ ($+30\%$) and $X$ ($+20\%$). Tap `{{key:-}}` for spread ($+10\%$) or `{{key:÷}}` for elasticity ($1.5\times$). | 16 | **50% fewer strokes + zero scratchpad memory** |
| **30-Year Mortgage Payment**: $\$350\text{k}$ at $6.75\%$ | Multi-step algebraic formula with 5 levels of parentheses: `350000 * ( ( 0.0675 / 12 ) * ( 1 + 0.0675 / 12 ) ^ 360 ) / ...` | 42 | **Dedicated 5-Variable TVM**: Store terms directly into financial registers `360 {{key:N}} 6.75 {{key:ENTER}} 12 {{key:÷}} {{key:I%YR}} 350000 {{key:PV}} 0 {{key:FV}} {{key:PMT}}`. | 24 | **43% fewer strokes + zero parenthesis syntax errors** |
| **DCF Valuation**: 4-Year Free Cash Flows | `10 / 1.1 + 12 / 1.1 ^ 2 + 15 / 1.1 ^ 3 + 234 / 1.1 ^ 4 =`. Vulnerable to mistyped exponent precedence and scratchpad loss. | 36 | **Inside-Out Discounting Stream**: Chain successive cash inflows with continuous stack division; zero parenthesis syntax overhead. | 22 | **39% fewer strokes + immediate intermediate cash visibility** |

### Cash-Flow Sign Conventions, Register Allocation & Tactile Financial Models
Every financial calculation on the SC-32 models a physical cash ledger: money leaving your pocket (investments, loan principal outlays, savings deposits) carries a negative sign (`{{key:+/-}}`), while money entering your pocket (loan proceeds, coupon inflows, maturity payouts) carries a positive sign. On the 4-level stack, each register serves as an explicit working account—Register $X$ holds the active adjustment or tax delta, Register $Y$ preserves the pre-tax invoice or principal baseline intact, Register $Z$ accumulates multi-tier reserves, and the dedicated five-variable `{{key:TVM}}` solver links those cash flows directly to compound discounting and amortization equations.

Three physical manipulative models turn the core concepts of quantitative finance into tangible geometry on your desk:
1. **Simple vs. Compound Growth (Counting Tiles & Prime Factor Blocks):** Simple interest ($FV = PV(1 + N i)$) merely docks a constant number of new $19.0 \times 19.0\text{ mm}$ **Counting Tiles** onto the end of a row each period. Compound interest ($FV = PV(1 + i)^N$), by contrast, scales the entire rectangular array in two dimensions so that *prior interest tiles generate new interest tiles of their own*—and with the **Prime Factor Blocks**, each doubling of capital adds one full $7.00\text{ mm}$ Blue $[2]$ block to your wealth tower.
2. **Percentages & Basis Points (Place Value Cubes Decimal Tray):** Switching the **Place Value Cubes** tray to its engraved decimal face (`1 • 0.1 | 0.01 | 0.001`) makes financial rate scaling transparent: moving two slots right of the unit post (`•`) into the hundredths socket (`0.01`) represents $1\% = 0.01$, while a single institutional **basis point** ($1\text{ bp} = 0.01\% = 0.0001$) is one hundredth of the `0.01` percent slot.
3. **Present-Value Discounting & Bond Duration (84 mm Fraction Towers):** Why is a dollar promised 10 or 20 years in the future worth less than a dollar in your hand today? Line up the **84 mm Fraction Towers** in decreasing height order ($1 = 84.0\text{ mm}$ today at $t=0$, down through $\frac{1}{2} = 42.0\text{ mm}$, $\frac{1}{3} = 28.0\text{ mm}$, and $\frac{1}{4} = 21.0\text{ mm}$ at distant horizons). Dividing a future cash flow $FV$ by $(1 + i)^N$ physically compresses its present-value tower height according to how far in the future it arrives—and **Macaulay Duration** (analyzed in the investment-grade bond duration section below) is literally the horizontal center-of-mass fulcrum where those discounted cash-flow towers balance along the timeline.

---

## The Base-Preserving Percentage Invariant (`{{key:%}}`)

On standard commercial calculators, pressing the percentage key is fraught with peril: some models merely divide the active entry by 100, others multiply by the previous operand, and nearly all overwrite the base operand in the process. Worse still, keying `100 + 8% =` on many algebraic pocket calculators literally computes $100 + 0.08 = 100.08$!

On the StackCalc SC-32, the **Percentage Function (`{{key:%}}`)** is an invariant dyadic operator adhering strictly to William Kahan's non-destructive specification:

$$\text{Calculation: } \quad X \leftarrow \frac{Y \times X}{100}, \quad Y \leftarrow Y \text{ (Preserved)}, \quad \text{Lift} \leftarrow \text{TRUE}$$

| Register | State After Keying `[Base] {{key:ENTER}} [Rate] {{key:%}}` | Executive Function |
| :---: | :--- | :--- |
| **Register $Y$** | Base Amount (Preserved frozen in $Y$) | Base remains intact for subsequent total, discount, or alternative trial |
| **Register $X$** | Computed Percentage Amount: $(Y \times X) / 100$ | Tax, tip, commission, or margin dollar value |

Because the base amount remains frozen in Register $Y$ while the dollar percentage appears in Register $X$, you see *both* numbers on the screen before deciding what to do with them. If you are adding sales tax, markup, or a gratuity, press `{{key:+}}` to sum $Y + X$. If you are deducting a trade discount or withholding tax, press `{{key:-}}` to compute $Y - X$. And if you want to discard the base and keep only the percentage amount in $X$, a quick `{{key:x⇄y}} {{key:R↓}}` drops it off the stack.

Compare how this plays out on the invoice from the beginning of the chapter ($\$150.00$ at $8.25\%$ tax): on an algebraic calculator, typing `150 × 0.0825 =` displays $\$12.38$ and destroys the $\$150.00$ base, forcing you to re-type `+ 150 =` to reach $\$162.38$—and if the client asks to check a $10\%$ discount instead, you have to start over from scratch. On the SC-32, keying `{{res:sc32_11_financial_tvm_seq_06:keys}}` places $\$12.38$ in Register $X$ while holding $\$150.00$ in Register $Y$; pressing `{{key:+}}` yields $\$162.38$ in a single stroke, and keying `{{res:sc32_11_financial_tvm_seq_44:keys}}` on a $\$100.00$ baseline places the exact dollar amount ($\mathbf{{{res:sc32_11_financial_tvm_seq_44:value}}}$) in $X$ while freezing $100.00$ in $Y$.

---

## Period-over-Period & Year-over-Year Performance (`{{key:%CHG}}`)

Corporate revenue growth, cost expansion, and quarterly margin velocity are measured by relative percentage change:

$$\%CHG = \frac{\text{New Value} - \text{Old Value}}{\text{Old Value}} \times 100$$

On the SC-32, the **Percent Change Function (`{{key:%CHG}}`)** is executed via Right Shift `{{key:↱}}` followed by `{{key:%CHG}}` using the natural chronological order **Old Value `{{key:ENTER}}` New Value `{{key:%CHG}}`**:

| Register | State Before `{{key:%CHG}}` | State After `{{key:%CHG}}` | Executive Role |
| :---: | :--- | :--- | :--- |
| **Register $Y$** | Old Value (Baseline) | Old Value (Preserved in $Y$) | Allows instant variance check: `{{key:x⇄y}} {{key:LASTX}} {{key:x⇄y}} {{key:-}}` |
| **Register $X$** | New Value (Current) | $\frac{\text{New} - \text{Old}}{\text{Old}} \times 100$ | Relative rate of expansion/contraction (%) |
| **`LASTX`** | Previous operand | New Value | Retained for delta calculations |

Just like `{{key:%}}`, `{{key:%CHG}}` is non-destructive: the Old Value stays anchored in Register $Y$ and the New Value is saved in `LASTX`, so you can immediately recover the absolute dollar variance ($\text{New} - \text{Old}$) by pressing `{{key:x⇄y}} {{key:LASTX}} {{key:x⇄y}} {{key:-}}`.

---

## Cross-Metric Elasticity & Spread: The Multi-Metric Stack Advantage

The true computational superiority of the RPN operational stack emerges during **comparative multi-metric corporate analytics**. Suppose an executive is evaluating a software portfolio company whose **Annual Recurring Revenue (ARR)** grew from $\$12.0\text{M}$ to $\$15.6\text{M}$ ($+30.00\%$), while **Customer Acquisition Cost (CAC)** expanded from $\$2.4\text{M}$ to $\$2.88\text{M}$ ($+20.00\%$). Two questions immediately arise at the board table:
1. **The ARR vs. CAC Growth Spread ($\Delta \text{ARR}\% - \Delta \text{CAC}\%$):** By how many percentage points did revenue growth outpace acquisition cost growth?
2. **The Growth Elasticity Ratio ($\Delta \text{ARR}\% \div \Delta \text{CAC}\%$):** How many percentage points of top-line revenue growth did each percentage point of acquisition spending buy?

| Stack Register | Value Staged | Financial Meaning | Immediate Dyadic Operation |
| :---: | :---: | :--- | :--- |
| **Register $T$** | $0.00$ | Top of stack | — |
| **Register $Z$** | $0.00$ | Holding register | — |
| **Register $Y$** | $+30.00\%$ | Metric A YoY Growth ($\Delta\text{ARR}\%$) | Base comparator |
| **Register $X$** | $+20.00\%$ | Metric B YoY Growth ($\Delta\text{CAC}\%$) | Active metric |

With both growth rates staged side-by-side in Registers $Y$ and $X$, pressing `{{key:-}}` immediately yields the **$+10.00\%$ Growth Spread**, and pressing `{{key:÷}}` yields the **$1.50\times$ Growth Elasticity Ratio**. On an algebraic calculator, answering the same question requires either jotting intermediate percentages on a notepad or typing a 30-character nested-parenthesis formula `(((15.6 - 12.0) / 12.0) * 100) - (((2.88 - 2.40) / 2.40) * 100)`.

---

## The 5-Variable Time Value of Money (TVM) Architecture

The SC-32 features an onboard **Five-Variable Time Value of Money (TVM) Engine** accessed via Left Shift `{{key:↰}}` followed by `{{key:TVM}}` on the multi-action `{{key:x∥y}}` key (Row 7, Column 3).

| TVM Variable | LFU Softkey | Actuarial Description | Computational Units |
| :---: | :---: | :--- | :--- |
| **$N$** | `{{key:N}}` | Total number of compounding periods | Integer or fractional periods |
| **$I\%YR$** | `{{key:I%YR}}` | Periodic interest rate per compounding period | Percent per period (e.g. `6.5` for 6.5%/yr or `6.75/12` for monthly) |
| **$PV$** | `{{key:PV}}` | Present value (initial loan principal or investment) | Currency ($) |
| **$PMT$** | `{{key:PMT}}` | Periodic annuity payment amount | Currency ($ per period) |
| **$FV$** | `{{key:FV}}` | Future value (final balloon balance or accumulated savings) | Currency ($) |

### The Master Actuarial TVM Equation & Hybrid Analytical-Bisection Engine
All five financial variables are bound together by a single conservation law—the universal compound interest annuity equation:

$$PV + PMT \left[ \frac{1 - (1 + i)^{-N}}{i} \right] (1 + i \cdot S) + FV (1 + i)^{-N} = 0$$

where $i = \frac{I\%YR}{100}$ is the periodic interest rate per compounding period stored in `{{key:I%YR}}`, $N$ is the total number of compounding periods stored in `{{key:N}}`, and $S = 0$ for End-of-Period payments (Ordinary Annuity, the default for loans and mortgages) or $S = 1$ for Beginning-of-Period payments (Annuity Due, the standard for equipment leases and tuition, flagged by the `BEGIN` annunciator and toggled via `{{key:TVM}} [BEG/END]`).

When you store any four of the five TVM variables and press the fifth softkey, the SC-32 solves for the unknown variable automatically. Four of the five variables have exact $\mathcal{O}(1)$ analytical closed-form solutions, with a smooth zero-interest limit ($a_{\overline{N}|i} = \frac{1 - (1+i)^{-N}}{i} \to N$ whenever $|i| < 10^{-14}$):
* **Solving for `FV`:** $FV = -\frac{PV + PMT \cdot (1 + i \cdot S) \cdot a_{\overline{N}|i}}{(1+i)^{-N}}$
* **Solving for `PV`:** $PV = -PMT \cdot (1 + i \cdot S) \cdot a_{\overline{N}|i} - FV(1+i)^{-N}$
* **Solving for `PMT`:** $PMT = -\frac{PV + FV(1+i)^{-N}}{(1 + i \cdot S) \cdot a_{\overline{N}|i}}$
* **Solving for `N`:** Inverted analytically via natural logarithms:
  $$N = -\frac{\ln\!\left(\frac{\text{PMT}_{\text{adj}} - i \cdot FV}{\text{PMT}_{\text{adj}} + i \cdot PV}\right)}{\ln(1 + i)}, \qquad \text{PMT}_{\text{adj}} = PMT(1 + i \cdot S)$$
  (which simplifies cleanly to $N = -(PV + FV)/PMT$ when $|i| < 10^{-14}$).
* **Solving for `I%YR` (240-Interval Scan + 100-Iteration Bisection):** Because the polynomial $f(i) = PV + PMT(1 + i \cdot S)a_{\overline{N}|i}(i) + FV(1+i)^{-N} = 0$ has no closed-form algebraic inverse for $i$ when $N > 4$ (by the Abel-Ruffini theorem!), the SC-32 runs a two-stage numerical root finder: first, it sweeps **240 uniform subintervals** across $i \in [-0.9999, +10.0]$ ($-99.99\%$ to $+1000\%$ per period) to bracket the sign change $f(a) \cdot f(b) \le 0$; second, it refines that bracket across up to **100 bisection steps** until $|f(\text{mid})| < 10^{-12}$ or $(b - a)/2 < 10^{-13}$, returning $I\%YR = 100 \cdot i$ to full 64-bit precision.

### Why Cash-Flow Sign Discipline Works Like Conservation of Energy
Notice that the right-hand side of the master TVM equation is **zero**. Think of your wallet—or a corporate treasury account—as a physical control volume in thermodynamics or a circuit node in Kirchhoff's Current Law:
- **Cash Inflows ($+$) are Positive:** Any cash flowing *into* your hands (the $\$350,000$ loan wire you receive at mortgage closing, the $\$27.50$ semi-annual coupon check from a bond, or the final maturity payout at the end of a CD) is entered as a **positive** number.
- **Cash Outflows ($-$) are Negative (`{{key:+/-}}`):** Any cash flowing *out* of your pocket (the $\$925.00$ purchase price you pay to buy a bond, the monthly $\$2,270.09$ mortgage check you mail to the bank, or a balloon payoff at the end of a commercial note) is entered as a **negative** number using `{{key:+/-}}`.

When every future payment and final balance is discounted back to the present moment ($t = 0$), the inflows and outflows must balance to zero. That immediately explains why entering all positive numbers ($PV = +1000, PMT = +50, FV = +1000$) triggers `ERROR 5: NO SOLUTION`: physically, a transaction where you only receive money and never pay anything out cannot balance to zero at any real interest rate! Likewise, always make sure your time period $N$ and periodic rate $I\%YR$ share the same time unit: for a 30-year monthly mortgage ($N = 360\text{ months}$), divide the annual nominal rate ($6.75\%$) by $12$ (`6.75 {{key:ENTER}} 12 {{key:÷}} {{key:I%YR}}` $\to 0.5625\%/\text{month}$) before storing it—otherwise `6.75 {{key:I%YR}}` would model a loan charging $6.75\%$ interest *every single month* ($81\%\text{ APR}$)!

### Financial Verification: Dedicated `{{key:TVM}}` Registers vs. Direct Stack Closed Forms
While the dedicated 5-variable `{{key:TVM}}` softkeys automate iterative and multi-register calculations, seasoned financial analysts often cross-check valuations by pairing the **5-Variable `{{key:TVM}}` Register Solver** with **Direct Inside-Out Closed-Form Evaluation on the 4-Level Stack**:

| Financial Instrument | Analytical Closed-Form Formula | Native RPN Inside-Out Recipe |
| :--- | :--- | :--- |
| **Ordinary Annuity PV** | $PV = PMT \left[ \frac{1 - (1 + i)^{-N}}{i} \right]$ | `1 ENTER i + N +/- yˣ 1 x⇄y - i ÷ PMT ×` |
| **Ordinary Annuity FV** | $FV = PMT \left[ \frac{(1 + i)^N - 1}{i} \right]$ | `1 ENTER i + N yˣ 1 - i ÷ PMT ×` |
| **Amortization Payment** | $PMT = PV \left[ \frac{i}{1 - (1 + i)^{-N}} \right]$ | `1 ENTER i + N +/- yˣ 1 x⇄y - i x⇄y ÷ PV ×` |
| **Sinking Fund Payment** | $PMT = FV \left[ \frac{i}{(1 + i)^N - 1} \right]$ | `1 ENTER i + N yˣ 1 - i x⇄y ÷ FV ×` |
| **Perpetuity PV** | $PV = \frac{PMT}{i}$ | `PMT ENTER i ÷` |
| **Growing Perpetuity PV** | $PV = \frac{PMT}{i - g}$ | `PMT ENTER i ENTER g - ÷` |

For the master quick-reference tables of all financial mathematics, amortization, and TVM equations, consult **[Appendix D: Section 9 (Financial Mathematics, Amortization & TVM Equations)](appendix-d-constants-and-equations.md)**.

---

## Capital Allocation, Bond Pricing, and Cash-Flow Modeling on the Stack

The following explorations progress from commercial invoice percentages and SaaS growth elasticity through residential and commercial mortgage amortization, bond duration, discounted cash-flow (DCF) valuation, and quantitative trading risk metrics.

### Commercial Percentages, Margin Markup & Cash-Flow Foundations

We start with William Kahan's non-destructive `%` and `%CHG` operators and geometric compounding before moving into the 5-variable TVM solver.

#### Commercial Invoice with Sales Tax
Suppose a procurement officer is signing off on an enterprise server hardware order subtotaling $\$18,450.00$ in a jurisdiction with an $8.25\%$ state sales tax. Rather than multiplying by $0.0825$ and losing the subtotal, let's use `{{key:%}}` in `{{key:FIX}} 2` display mode so that both the tax liability and the pre-tax base remain visible on the stack: keying `{{res:sc32_11_financial_tvm_seq_07:keys}}` places the tax amount $X = \mathbf{\$1,522.13}$ below the preserved base $Y = \$18,450.00$, and pressing `{{key:+}}` immediately sums the total invoice to **`$19,972.13`**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `18450 {{key:ENTER}}` | 0.00 | 0.00 | 18450.00 | 18450.00 | `18450.00_` |
| 02 | `8.25 {{key:%}}` | 0.00 | 0.00 | 18450.00 | 1522.13 | `1522.13` |
| 03 | `{{key:+}}` | 0.00 | 0.00 | 0.00 | 19972.13 | `19972.13` |

#### Enterprise Contract Volume Discount
Now flip the scenario to the other side of the negotiating table: an enterprise software license carries a list price of $\$85,000.00$, and the procurement team negotiates a $17.5\%$ volume discount. We need both the dollar concession for the discount line item and the net invoice payable.

Because `{{key:%}}` on an RPN stack replaces Register $X$ with $(Y \times X)/100$ while leaving the base contract amount untouched in Register $Y$, keying `{{res:sc32_11_financial_tvm_seq_08:keys}}` in `{{key:FIX}} 2` mode displays the negotiated dollar concession ($X = \mathbf{\$14,875.00}$) alongside the $\$85,000.00$ list price in $Y$, and pressing `{{key:-}}` immediately yields the net invoice payable (**`$70,125.00`**, $X = \mathbf{70125.00}$).

#### Multi-Metric Growth Spread and Elasticity Ratio
During a quarterly board review, a SaaS company reports that Annual Recurring Revenue (Metric A, ARR) grew from $\$12.0\text{M}$ to $\$15.6\text{M}$ ($\Delta A\% = 30.00\%$), while Customer Acquisition Cost (Metric B, CAC) expanded from $\$2.4\text{M}$ to $\$2.88\text{M}$ ($\Delta B\% = 20.00\%$). Watch how the 4-level stack lets us compute the ARR percentage change via `{{res:sc32_11_financial_tvm_seq_10:keys}}` ($\rightarrow 30.00$) followed by the CAC percentage change via `{{res:sc32_11_financial_tvm_seq_11:keys}}` ($\rightarrow 20.00$). Dropping the old baseline out of the way (`{{key:x⇄y}} {{key:R↓}}`) aligns revenue growth ($Y = 30.00$) and acquisition cost growth ($X = 20.00$) side-by-side on the stack, where pressing `{{key:-}}` yields the **`+10.00%`** growth spread and keying `{{res:sc32_11_financial_tvm_seq_12:keys}}` computes the **`{{res:sc32_11_financial_tvm_seq_12:value}}`** growth elasticity multiplier:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `12 {{key:ENTER}} 15.6 {{key:%CHG}}` | 0.00 | 0.00 | 12.00 | 30.00 | `30.00` |
| 02 | `2.4 {{key:ENTER}} 2.88 {{key:%CHG}}` | 12.00 | 30.00 | 2.40 | 20.00 | `20.00` |
| 03 | `{{key:x⇄y}}` | 12.00 | 30.00 | 20.00 | 2.40 | `2.40` |
| 04 | `{{key:R↓}}` | 2.40 | 12.00 | 30.00 | 20.00 | `20.00` |
| 05 | `{{key:-}}` | 2.40 | 2.40 | 12.00 | 10.00 | `10.00` |

#### Compound Annual Growth Rate (CAGR)
A venture capital fund invests $\$14.0\text{M}$ into an industrial robotics startup at Series A, and the company exits via acquisition for $\$88.5\text{M}$ exactly $n = 5\text{ years}$ later. Total multiple on invested capital is $88.5 / 14.0 = 6.32\times$, but what steady annual compounding rate—the **Compound Annual Growth Rate (CAGR)**—produces a $6.32\times$ expansion over five years? Taking the fifth root (`5 {{key:1/x}} {{key:yˣ}}`) of the terminal wealth ratio and subtracting $1$ gives the exact geometric mean annual return:

$$\text{CAGR} = \left(\frac{88.5}{14.0}\right)^{1/5} - 1$$

Keying `{{res:sc32_11_financial_tvm_seq_13:keys}}` evaluates the terminal multiple, raises it to the $1/5$ power, subtracts $1$, and scales by $100$ to reveal a compound annual growth rate of **`{{res:sc32_11_financial_tvm_seq_13:value}}`**:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `88.5 {{key:ENTER}}` | 0.00 | 0.00 | 88.50 | 88.50 | `88.50_` |
| 02 | `14.0 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 6.32 | `6.32` |
| 03 | `5 {{key:1/x}}` | 0.00 | 0.00 | 6.32 | 0.20 | `0.20` |
| 04 | `{{key:yˣ}}` | 0.00 | 0.00 | 0.00 | 1.45 | `1.45` |
| 05 | `1 {{key:-}}` | 0.00 | 0.00 | 0.00 | 0.45 | `0.45` |
| 06 | `100 {{key:×}}` | 0.00 | 0.00 | 0.00 | 44.60 | `44.60` |

#### 30-Year Fixed Residential Mortgage & Lifetime Interest
Few financial calculations are more eye-opening than computing the true 30-year cost of a home mortgage. Suppose a family borrows $PV = +\$350,000.00$ (cash inflow received at closing) on a 30-year fixed mortgage ($N = 30 \times 12 = 360\text{ months}$, $FV = \$0.00$) at an annual nominal rate of $6.75\%$ APR (monthly periodic rate $i = 6.75\% / 12 = 0.5625\%$).

After clearing TVM registers (`{{key:CLEAR}} {{key:CLALL}}`), store $N = 360$ (`30 {{key:ENTER}} 12 {{key:×}} {{key:N}}`), monthly periodic rate $I\%YR = 0.5625\%$ (`6.75 {{key:ENTER}} 12 {{key:÷}} {{key:I%YR}}`), principal $PV = \$350,000$, and $FV = \$0$. Pressing `{{key:PMT}}` solves the monthly payment (**`-$2,270.09`**), multiplying by `360 {{key:×}}` yields total lifetime payments (**`-$817,233.60`**), and adding the original principal `350000 {{key:+}}` isolates total lifetime interest (**`-$467,233.60`**—more than $1.33\times$ the price of the house itself!):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `360 {{key:N}}` | 0.00 | 0.00 | 0.00 | 360.00 | `360.00` |
| 02 | `.5625 {{key:I%YR}}` | 0.00 | 0.00 | 360.00 | 0.56 | `0.56` |
| 03 | `350000 {{key:PV}}` | 0.00 | 360.00 | 0.56 | 350000.00 | `350000.00` |
| 04 | `0 {{key:FV}}` | 360.00 | 0.56 | 350000.00 | 0.00 | `0.00` |
| 05 | `{{key:PMT}}` | 360.00 | 0.56 | 350000.00 | -2270.09 | `-2270.09` |
| 06 | `360 {{key:×}}` | 0.56 | 0.56 | 350000.00 | -817233.60 | `-817233.60` |
| 07 | `350000 {{key:+}}` | 0.56 | 0.56 | 350000.00 | -467233.60 | `-467233.60` |

> **5-Variable `{{key:TVM}}` Solver vs. Closed-Form Stack Annuity with `{{key:LASTX}}`:**
> Every mortgage payment can be verified via the dedicated 5-variable `{{key:TVM}}` registers or directly from the closed-form compound-factor equation $PMT = PV \cdot \frac{i}{1 - (1+i)^{-N}}$ on the stack:
>
> * **At $6.75\%$ APR ($i = 0.005625$/month):** **Dedicated `{{key:TVM}}` Registers:** key `360 {{key:N}} .5625 {{key:I%YR}} 350000 {{key:PV}} 0 {{key:FV}} {{key:PMT}}` $\implies \mathbf{-\$2,270.09}$. **Direct Stack Closed Form:** key `1 {{key:ENTER}} .005625 {{key:+}} 360 {{key:+/-}} {{key:yˣ}} 1 {{key:x⇄y}} {{key:-}} .005625 {{key:x⇄y}} {{key:÷}} 350000 {{key:×}}` $\implies \mathbf{\$2,270.09}$.
> * **Rate-Comparison Check at $6.50\%$ APR ($i = 0.065/12$/month):** **Dedicated `{{key:TVM}}` Registers:** key `360 {{key:N}} 6.5 {{key:ENTER}} 12 {{key:÷}} {{key:I%YR}} 350000 {{key:PV}} 0 {{key:FV}} {{key:PMT}}` $\implies \mathbf{-\$2,212.24}$. **Direct Stack Closed Form with `{{key:LASTX}}`:** compute $1 + i$ and $(1+i)^{360}$ once via `.065 {{key:ENTER}} 12 {{key:÷}} {{key:ENTER}} 1 {{key:+}} 360 {{key:yˣ}} {{key:ENTER}} 1 {{key:-}} {{key:÷}} {{key:×}} 350000 {{key:×}}` $\implies \mathbf{\$2,212.24}$—immediately confirming that a $25\text{ bp}$ ($0.25\%$) rate reduction saves $\$57.85/\text{month}$ ($\$20,826$ over 30 years).

#### First-Month Amortization Split & The Crossover Point
Why does your loan balance barely budge during the early years of a 30-year mortgage? Because each month, the bank first charges rent on the entire remaining debt ($I_1 = PV \times i$) and only applies whatever is left over of your monthly check ($P_1 = |PMT| - I_1$) toward reducing principal. On our $\$350,000$ mortgage at $0.5625\%/\text{month}$ ($PMT = -\$2,270.09$):
* Interest Month 1: $350,000 \times 0.005625 = \mathbf{\$1,968.75}$ ($86.7\%$ of payment)
* Principal Month 1: $\$2,270.09 - \$1,968.75 = \mathbf{\$301.34}$ ($13.3\%$ of payment)
* New Principal Balance: $\$350,000 - \$301.34 = \mathbf{\$349,698.66}$.

In fact, as the table below shows, the monthly principal reduction $P_k$ does not overtake the monthly interest charge $I_k$ until **Month 237**—nearly twenty years into the loan!

| Month | Remaining Balance | Monthly Payment | Interest ($I_k$) | Principal ($P_k$) | Equity % | Notes |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **1** | $\$349,698.66$ | $\$2,270.09$ | $\$1,968.75$ | $\$301.34$ | $0.09\%$ | $86.7\%$ of payment goes to interest |
| **237** | $\$199,642.18$ | $\$2,270.09$ | $\$1,130.71$ | $\$1,139.38$ | $42.96\%$ | **Amortization Crossover:** $P_k > I_k$ |
| **360** | $\$0.00$ | $\$2,270.09$ | $\$12.70$ | $\$2,257.39$ | $100.00\%$ | Final payoff; $\$467,233.60$ total interest |

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `350000 {{key:ENTER}}` | 0.00 | 0.00 | 350000.00 | 350000.00 | `350000.00_` |
| 02 | `0.005625 {{key:×}}` | 0.00 | 0.00 | 0.00 | 1968.75 | `1968.75` |
| 03 | `2270.09 {{key:x⇄y}} {{key:-}}` | 0.00 | 0.00 | 0.00 | 301.34 | `301.34` |
| 04 | `350000 {{key:x⇄y}} {{key:-}}` | 0.00 | 0.00 | 0.00 | 349698.66 | `349698.66` |

#### Commercial 5-Year Balloon Note
Commercial real estate loans rarely lock in a fixed rate for 25 or 30 years. Instead, a bank might lend $\$500,000$ at $7.5\%$ APR ($i = 7.5\% / 12 = 0.625\%/\text{month}$) with monthly payments **amortized over 25 years** ($N = 300\text{ months}$), but with a **5-year balloon maturity** ($N = 60\text{ months}$) where the entire remaining principal comes due at once. On the SC-32, we first solve for `{{key:PMT}}` at $N = 300$ via `{{res:sc32_11_financial_tvm_seq_17:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_17:value}}`**, and then simply key `60 {{key:N}} {{key:FV}}`—without re-entering `I%YR`, `PV`, or `PMT`—to find the exact balloon payoff at Month 60 (**`-$458,662.75`**):

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

### Fixed-Income Bonds, Mortgages & Lease Amortization

Storing four TVM variables and solving for the fifth (`N`, `I%YR`, `PV`, `PMT`, `FV`) under strict cash-flow sign conventions also prices corporate bonds and multi-year acquisition targets.

#### Corporate Bond Yield to Maturity (YTM)
Suppose an investor buys a 10-year corporate bond ($N = 20$ semi-annual periods) with a $\$1,000.00$ par value ($FV = +\$1,000.00$) and a $5.5\%$ annual coupon paid semi-annually ($PMT = +\$27.50$ every six months) at a discounted market price of $\$925.00$ ($PV = -\$925.00$ cash outflow today). What is the bond's annualized **Yield to Maturity (YTM)**? Storing $N, PV, PMT,$ and $FV$ and pressing `{{key:I%YR}}` invokes the 240-interval bisection solver to find the semi-annual yield $i = 3.2666\%$, which we double (`2 {{key:×}}`) to obtain the bond-equivalent annual yield $\text{YTM} = \mathbf{6.53\%}$:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `20 {{key:N}}` | 0.00 | 0.00 | 0.00 | 20.00 | `20.00` |
| 02 | `925 {{key:+/-}} {{key:PV}}` | 0.00 | 0.00 | 20.00 | -925.00 | `-925.00` |
| 03 | `27.50 {{key:PMT}}` | 0.00 | 20.00 | -925.00 | 27.50 | `27.50` |
| 04 | `1000 {{key:FV}}` | 20.00 | -925.00 | 27.50 | 1000.00 | `1000.00` |
| 05 | `{{key:I%YR}}` | 20.00 | -925.00 | 27.50 | 3.27 | `3.27` |
| 06 | `2 {{key:×}}` | -925.00 | -925.00 | 27.50 | 6.53 | `6.53` |

#### Discounted Cash Flow (DCF) with Terminal Multiple
An investment banking analyst is valuing a precision manufacturing firm projected to generate free cash flows (FCF) of $\$10\text{M}, \$12\text{M}, \$15\text{M},$ and $\$18\text{M}$ over the next 4 years, discounted at a weighted average cost of capital (WACC) of $10\%$. At the end of Year 4, the business is valued at a terminal exit multiple of $12\times$ Year 4 FCF ($12 \times 18 = \$216\text{M}$), bringing the total Year 4 cash flow to $18 + 216 = \$234\text{M}$:
$$\text{Enterprise Value} = \frac{10}{1.10} + \frac{12}{1.10^2} + \frac{15}{1.10^3} + \frac{234}{1.10^4}$$

Discounting and accumulating the four annual inflows term-by-term via `{{res:sc32_11_financial_tvm_seq_18:keys}}` yields an enterprise valuation of **`{{res:sc32_11_financial_tvm_seq_18:value}}`** ($\mathbf{\$190.11\text{M}}$):

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `10 {{key:ENTER}} 1.1 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 9.09 | `9.09_` |
| 02 | `12 {{key:ENTER}} 1.1 {{key:x²}} {{key:÷}}` | 0.00 | 0.00 | 9.09 | 9.92 | `9.92_` |
| 03 | `{{key:+}}` | 0.00 | 0.00 | 0.00 | 19.01 | `19.01_` |
| 04 | `15 {{key:ENTER}} 1.1 {{key:ENTER}} 3 {{key:yˣ}} {{key:÷}}` | 19.01 | 19.01 | 19.01 | 11.27 | `11.27_` |
| 05 | `{{key:+}}` | 19.01 | 19.01 | 19.01 | 30.28 | `30.28_` |
| 06 | `234 {{key:ENTER}} 1.1 {{key:ENTER}} 4 {{key:yˣ}} {{key:÷}}` | 30.28 | 30.28 | 30.28 | 159.83 | `159.83_` |
| 07 | `{{key:+}}` | 30.28 | 30.28 | 30.28 | 190.11 | `190.11` |

**Horner Nested Discounting Stream via Register $T$:** Just as Chapter 7 nested polynomials and Chapter 10 nested positional radix powers ($b^{-k}$), writing the 4-year DCF sum in nested Horner form as $\left(\left(\left(\frac{234}{1.1} + 15\right)\frac{1}{1.1} + 12\right)\frac{1}{1.1} + 10\right)\frac{1}{1.1}$ and parking the gross return factor $1.10$ across the upper stack via `1.1 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}} 234 {{key:x⇄y}} {{key:÷}} 15 {{key:+}} {{key:x⇄y}} {{key:÷}} 12 {{key:+}} {{key:x⇄y}} {{key:÷}} 10 {{key:+}} {{key:x⇄y}} {{key:÷}}` evaluates $\mathbf{\$190.11\text{M}}$ with `1.1` typed only once and zero `{{key:yˣ}}` exponentiations.

---

### Everyday Carry Math & Compound Markdowns

Even outside the boardroom, keeping intermediate subtotals live on the four-level stack turns multi-way dinner splits and stacked retail markdowns into effortless one-pass calculations.

#### Banquet Check Split with Itemized Wine Separation
Eight colleagues dine out together and receive a grand total bill of $\$480.00$. Three of the eight guests shared two reserve bottles of wine totaling $\$96.00$, while everyone shared the food equally. How much should the wine drinkers and non-drinkers each pay? Deducting the wine tab via `{{res:sc32_11_financial_tvm_seq_25:keys}}` isolates the shared food bill $(\$384.00)$, and `8 {{key:÷}}` establishes the per-guest food share $(\$48.00)$ in Register $X$. Computing the per-drinker wine allocation via `{{res:sc32_11_financial_tvm_seq_26:keys}}` places $\$32.00$ in $X$ while the $\$48.00$ food share waits in $Y$, so `{{key:+}}` resolves the wine-drinker total ($X = \mathbf{\$80.00}$) alongside **`$48.00`** for non-wine guests.

#### Retail Store Double Discount
A retail store advertises a "$30\%$ seasonal sale plus an extra $15\%$ VIP coupon" on a $\$280.00$ designer jacket. A casual shopper might add $30\% + 15\% = 45\%$ off, expecting to pay $\$154.00$—but successive percentage markdowns compound multiplicatively against the reduced subtotal rather than additively! Keying `{{res:sc32_11_financial_tvm_seq_27:keys}}` followed by `{{key:-}}` deducts the initial $30\%$ markdown $(\$84.00)$ to leave the sale price $(\$196.00)$ in Register $X$, and chaining `15 {{key:%}} {{key:-}}` applies the $15\%$ VIP coupon $(\$29.40)$ against that reduced base to yield $\mathbf{\$166.60}$—an effective combined discount of $1 - (0.70)(0.85) = 40.5\%$.

---

### Real vs. Nominal Returns, Uneven IRR & Bond Duration

We next evaluate cumulative inflation erosion, uneven cash-flow internal rates of return (IRR) via `{{key:SOLVE}}`, and fixed-income Macaulay and modified duration.

#### Cumulative Inflation and Purchasing Power
A creeping inflation rate of $3.2\%$ per year sounds gentle in any single twelve-month window, but over two decades its exponential compounding quietly erodes uninvested cash. What will $\$100,000$ of uninvested cash buy in today's constant dollars after 20 years of $3.2\%$ average annual inflation?

$$PV = \frac{100,000}{(1.032)^{20}}$$

Deflating nominal currency by the cumulative CPI price-level factor $(1 + \pi)^{20}$ via `{{res:sc32_11_financial_tvm_seq_03:keys}}` ($1.87756$ in the denominator) reveals that $3.2\%$ annual inflation erodes $\$100,000$ to **`{{res:sc32_11_financial_tvm_seq_03:value}}`** ($\mathbf{\$53260.60}$) in constant-dollar purchasing power—cutting purchasing power nearly in half and shrinking an $84.0\text{ mm}$ 1-Whole purchasing-power column in the **84 mm Fraction Towers** down to nearly the $42.0\text{ mm}$ ($\frac{1}{2}$) block.

#### Internal Rate of Return (IRR) on Uneven Cash Flows
When a project produces *equal* periodic payments, `{{key:TVM}}` solves its yield in one keystroke. What if the annual cash flows are *uneven*? Suppose an infrastructure venture requires an upfront capital outlay of $C_0 = -\$100,000.00$ and generates rising year-end inflows of $C_1 = \$30,000.00, C_2 = \$40,000.00,$ and $C_3 = \$50,000.00$. To find the project's **Internal Rate of Return ($\text{IRR}$)**—the discount rate $r$ where Net Present Value ($\text{NPV}$) equals zero—we write $\text{NPV}(r) = 0$ in Horner nested form using the gross discount factor $x = 1 + r$ and hand it to Brent's root finder `{{key:SOLVE}}`:

$$NPV(r) = -100000 + \frac{30000}{1+r} + \frac{40000}{(1+r)^2} + \frac{50000}{(1+r)^3} = 0$$

Let discount factor $x = 1+r$. In `{{key:EQN}}` mode, enter the Horner-nested polynomial in $x$:
`50000 X {{key:÷}} 40000 {{key:+}} X {{key:÷}} 30000 {{key:+}} X {{key:÷}} 100000 {{key:-}}`
Using `{{key:SOLVE}} X` with initial guess $x = 1.10$, the solver converges to $x = 1.08889 \implies r = x - 1 = \mathbf{8.89\%}$:

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `1.10 {{key:STO}} X` | 0.00 | 0.00 | 0.00 | 1.10 | `1.10` |
| 02 | `{{key:SOLVE}}X` | 0.00 | 0.00 | 1.10 | 1.08889 | `1.08889` |
| 03 | `1 {{key:-}}` | 0.00 | 0.00 | 1.10 | 0.08889 | `0.08889` |
| 04 | `100 {{key:×}}` | 0.00 | 0.00 | 1.10 | 8.89 | `8.89` |

#### Macaulay and Modified Duration of an Investment-Grade Bond
Why does a 3-year coupon bond behave like a slightly shorter-than-3-year zero-coupon bond when interest rates move? Because you receive part of your cash back early in Years 1 and 2 via the coupon payments! In 1938, economist Frederick Macaulay defined **Macaulay Duration ($D$)** as the present-value-weighted average time until a bond's cash flows arrive, and dividing by $(1 + y)$ gives **Modified Duration ($D^*$)**, which measures the percentage change in bond price per $1\%$ change in yield. Let's compute both for a 3-year $8.0\%$ annual coupon bond trading at par ($\$1,000.00$) with yield $y = 8.0\%$:

$$\text{Macaulay Duration } D = \frac{1 \times 80/1.08 + 2 \times 80/1.08^2 + 3 \times 1080/1.08^3}{1000} = \mathbf{2.783\text{ years}}$$
$$\text{Modified Duration } D^* = \frac{D}{1 + y} = \frac{2.783}{1.08} = \mathbf{2.577\text{ years}}$$
Physically, if you dock three present-value **84 mm Fraction Towers** at $t = 1, 2, 3\text{ years}$ proportional to the discounted cash flows ($\$74.07$, $\$68.59$, and $\$857.34$), Macaulay Duration $D = 2.783\text{ years}$ is the exact center-of-mass pivot point where the timeline balances, and a $100\text{ bps}$ ($1.0\%$ on the `0.01` hundredths socket of the **Place Value Cubes** tray) rise in market interest rates causes approximately a $2.58\%$ decline in bond price.

| Step | Keystroke | Register T | Register Z | Register Y | Register X | Display |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | `80 {{key:ENTER}} 1.08 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 74.0741 | `74.07` |
| 02 | `80 {{key:ENTER}} 1.08 {{key:ENTER}} 2 {{key:yˣ}} {{key:÷}} 2 {{key:×}} {{key:+}}` | 74.07 | 74.07 | 74.07 | 211.2483 | `211.25` |
| 03 | `1080 {{key:ENTER}} 1.08 {{key:ENTER}} 3 {{key:yˣ}} {{key:÷}} 3 {{key:×}} {{key:+}}` | 211.25 | 211.25 | 211.25 | 2783.2648 | `2783.26` |
| 04 | `1000 {{key:÷}}` | 211.25 | 211.25 | 211.25 | 2.7833 | `2.7833` |
| 05 | `1.08 {{key:÷}}` | 211.25 | 211.25 | 211.25 | 2.5771 | `2.5771` |

---

### The Executive Boardroom, Realtor Open-House & Trading Desk Playbook

Whether you are a Chief Executive Officer auditing unit economics during a board meeting, a commercial or residential realtor structuring an offer at an open house, or a quantitative trader sizing a position under market volatility, you do not have time to open a laptop spreadsheet. These high-velocity RPN workflows turn the SC-32 into an instant tactical advantage in any negotiation.

#### The CEO's Gross Margin vs. Markup Trap
One of the most expensive mistakes in retail and hardware manufacturing is confusing **Markup** (profit divided by *cost*) with **Gross Margin** (profit divided by *selling price*). Suppose a hardware product has a landed bill-of-materials cost of $C = \$60.00$, and the board mandates a **$40.0\%$ Gross Margin** on retail sales.
* **The Amateur Markup Trap:** Adding $40\%$ on top of $\$60.00$ (`{{res:sc32_11_exec_markup_trap:keys}}` $\rightarrow$ **`\${{res:sc32_11_exec_markup_trap:value}}`**) yields $\$24.00$ of profit on an $\$84.00$ price tag—which is only $\$24.00 / \$84.00 = 28.57\%$ gross margin!
* **True Gross Margin Pricing:** If gross profit takes $40\%$ of the selling price, then the $\$60.00$ cost must represent the remaining $1 - 0.40 = 60\%$ of the selling price ($\text{Price} = \frac{\text{Cost}}{1 - \text{Margin}}$):
  `{{res:sc32_11_exec_gross_margin_price:keys}}` $\rightarrow$ **`\${{res:sc32_11_exec_gross_margin_price:value}}`**.

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `60 {{key:ENTER}} 40 {{key:%}}` | 0.00 | 0.00 | 60.00 | 24.00 | 40% markup on \$60.00 cost: \$24.00 |
| 02 | `{{key:+}}` | 0.00 | 0.00 | 0.00 | 84.00 | Flawed markup price: \$84.00 (28.57% margin) |
| 03 | `60 {{key:ENTER}} 1 {{key:ENTER}}` | 84.00 | 60.00 | 1.00 | 1.00 | True margin pricing: stage cost \$60 in $Z$ and 1.00 in $Y$ |
| 04 | `.40 {{key:-}}` | 84.00 | 84.00 | 60.00 | 0.60 | 1 - 0.40 = 0.60 margin complement; \$60.00 drops to $Y$ |
| 05 | `{{key:÷}}` | 84.00 | 84.00 | 84.00 | 100.00 | True gross margin retail price: \$100.00 |

#### The Realtor's Open-House Extra-Principal Payoff Hack
At an open house, a prospective buyer is hesitant about the 30-year ($360\text{-month}$) commitment on the $\$350,000.00$ mortgage at $6.75\%$ APR ($PMT = -\$2,270.09/\text{mo}$ from the 30-year residential mortgage analysis above). Because 86.7% of early payments go to interest, any extra principal added each month attacks the loan balance directly! Let's show the buyer what happens if they add just **$\$250.00/\text{month}$** in extra principal ($PMT = -\$2,520.09/\text{mo}$) and solve for the new payoff term `{{key:N}}` via `{{res:sc32_11_realtor_extra_principal_months:keys}}`, which drops the repayment horizon to **`{{res:sc32_11_realtor_extra_principal_months:value}}` months** ($22.6\text{ years}$):

| Step | Keystrokes | Register T | Register Z | Register Y | Register X | Notes |
|:---|:---|:---|:---|:---|:---|:---|
| 01 | `6.75 {{key:ENTER}} 12 {{key:÷}} {{key:I%YR}}` | 0.00 | 0.00 | 0.00 | 0.56 | Monthly rate i = 0.5625% |
| 02 | `350000 {{key:PV}} 0 {{key:FV}}` | 0.00 | 0.56 | 350000.00 | 0.00 | Store PV = \$350,000.00, FV = \$0.00 |
| 03 | `2520.09 {{key:+/-}} {{key:PMT}}` | 0.56 | 350000.00 | 0.00 | -2520.09 | Augmented payment: -\$2,520.09/mo |
| 04 | `{{key:N}}` | 0.56 | 350000.00 | 0.00 | 270.93 | Accelerated repayment: 270.93 months |

Adding $\$250/\text{month}$ eliminates **$89\text{ monthly payments}$ ($7.4\text{ years}$)** and saves **$\$134,474.66$** in lifetime interest.

#### Quantitative Trading Desk — Sharpe Ratio & Kelly Criterion Sizing
On a quantitative trading desk, raw return means nothing without knowing how much volatility risk was taken to earn it, and a winning edge can still bankrupt a fund if positions are oversized. Two classic metrics govern portfolio risk: Nobel laureate William Sharpe's **Sharpe Ratio** (excess return over the risk-free rate per unit of volatility) and Bell Labs physicist John Kelly's **Kelly Criterion** (the exact fraction of capital $f^*$ that maximizes long-run logarithmic wealth growth):
1. **Ex-Post Sharpe Ratio:** A systematic portfolio returns $R_p = 18.5\%$ while the risk-free Treasury bill rate is $R_f = 4.5\%$, with annualized return volatility $\sigma_p = 11.2\%$:
   $$\text{Sharpe} = \frac{R_p - R_f}{\sigma_p}$$
   Normalizing the excess return via `{{res:sc32_11_trader_sharpe_ratio:keys}}` yields a Sharpe Ratio of **`{{res:sc32_11_trader_sharpe_ratio:value}}`**.
2. **Kelly Criterion Optimal Position Size ($f^*$):** A trade setup has historical win rate $p = 0.56$ (loss rate $q = 0.44$) and average win-to-loss payoff ratio $b = 1.50$:
   $$f^* = \frac{b p - q}{b} \times 100$$
   Evaluating the expected edge via `{{res:sc32_11_trader_kelly_criterion:keys}}` yields an optimal full-Kelly allocation of **`{{res:sc32_11_trader_kelly_criterion:value}}`** of risk capital (most desk traders allocate "Half-Kelly" $= 13.33\%$ to dampen drawdown variance).

Normalizing excess portfolio return `18.5 {{key:ENTER}} 4.5 {{key:-}}` ($14.00\%$) by annualized return standard deviation `11.2 {{key:÷}}` yields William Sharpe's reward-to-variability ratio ($X = \mathbf{1.25}$). To maximize expected logarithmic capital growth $E[\ln(1 + f R)]$, John Kelly's information-theoretic sizing formula `1.5 {{key:ENTER}} 0.56 {{key:×}}` ($bp = 0.84$) less `0.44 {{key:-}}` ($0.40$) divided by `1.5 {{key:÷}} 100 {{key:×}}` yields the full-Kelly allocation ($Y = 1.25,\; X = \mathbf{26.67}\%$).
*(**`LASTX` Single-Entry Kelly Identity:** Rewriting Kelly's formula as $f^* = p - \frac{1 - p}{b}$ eliminates re-entering both $b = 1.5$ and $q = 1 - p$: keying `1 {{key:ENTER}} 0.56 {{key:-}} {{key:LASTX}} {{key:x⇄y}} 1.5 {{key:÷}} {{key:-}} 100 {{key:×}}` computes $1 - 0.56 = 0.44$ in $X$ while saving $p = 0.56$ in `LASTX`, recalls $0.56$ and swaps it into $Y$, divides $0.44 / 1.5$, and subtracts from $0.56$ to produce $\mathbf{26.67\%}$ with `0.56` and `1.5` each typed only once.)*
---

## Further Exploration: Companion Workbooks & Applied Tie-Ins

> *For 31 additional worked engineering problems with full 4-register stack traces, see Chapter 11 of the [SC-32 Scientific Companion Problem & Casebook Workbook](../../curriculum/sc32-scientific-companion-workbook.md#chapter-11).*


To extend the TVM solver, actuarial discounting, and unit-economics pipelines from this chapter into full corporate finance models and contest speed drills, consult these companion volumes:

- **StackCalc Quantitative Finance & Actuarial Casebook (Module 3: Fixed-Income Duration, Convexity & Option-Adjusted Spreads):** Combines the 5-variable TVM registers (`{{key:N}}`, `{{key:I%YR}}`, `{{key:PV}}`, `{{key:PMT}}`, `{{key:FV}}`) with `{{key:SOLVE}}` and `{{key:∫}}` to price callable corporate bonds, construct spot-rate yield curves via bootstrapping, and evaluate Black-Scholes-Merton d1/d2 normal tail integrals.
- **Timed STEM Competition & Business Math Workbook (Section F: Compound Interest, Annuities & Percentage Chains):** Features timed drills on continuous vs. discrete compounding, nominal-to-effective rate conversions, and multi-tier discount/markup chains exploiting Register $Y$ base preservation.

### Synthesis Challenge Problems

1. **Single-Entry Kelly Criterion via `{{key:LASTX}}`:** Using the identity $f^* = p - \frac{1 - p}{b}$, verify that for win probability $p = 0.62$ and payoff odds $b = 1.90$, keying `1 {{key:ENTER}} 0.62 {{key:-}} {{key:LASTX}} {{key:x⇄y}} 1.90 {{key:÷}} {{key:-}} 100 {{key:×}}` computes the exact full-Kelly fraction $f^* = \mathbf{42.00\%}$ while typing `0.62` and `1.90` only once each.
2. **Single-Entry Effective Annual Rate (EAR) Evaluation:** For a nominal rate of $18.5\%$ APR compounded monthly ($m = 12$), compute $\text{EAR} = (1 + 0.185/12)^{12} - 1$ by typing `12` only once: key `0.185 {{key:ENTER}} 12 {{key:÷}} {{key:LASTX}} {{key:x⇄y}} 1 {{key:+}} {{key:x⇄y}} {{key:yˣ}} 1 {{key:-}} 100 {{key:×}}` to obtain $\mathbf{20.15\%}$.
3. **Amortization Crossover Month via Closed-Form Logarithm:** On a 30-year ($N = 360$) mortgage at monthly rate $i = 0.005625$ ($6.75\%$ APR), the principal portion $P_k$ first exceeds the interest portion $I_k$ when $(1 + i)^{N - k + 1} = 2$, or $N - k + 1 = \frac{\ln 2}{\ln(1 + i)}$. Evaluate `2 {{key:LN}} 1.005625 {{key:LN}} {{key:÷}} 361 {{key:x⇄y}} {{key:-}}` on the stack to confirm that the crossover occurs at month $k = \mathbf{237.43}$ (Month **238**).

---

## Summary & Looking Ahead

The five-variable Time Value of Money solver ($N, I\%YR, PV, PMT, FV$) and William Kahan's base-preserving percentage operators (`{{key:%}}` and `{{key:%CHG}}`) bring compound interest growth, mortgage amortization schedules, discounted cash-flow valuation, fixed-income duration, and portfolio risk metrics directly onto the four-level stack. Strict cash-flow sign conventions and Register $Y$ base preservation allow multi-period financial analyses to be verified against closed-form annuity identities without intermediate scratch storage.

While tabular financial schedules and discrete numerical outputs provide exact answers, engineering analysis often demands visualizing how mathematical functions behave across continuous domains. In **[Chapter 12: Function Evaluation & 64-Point Vector Scatter Plotting](12-function-scatter-plotting.md)**, you will use the SC-32's transflective graphic display to plot and inspect functions. You will sample mathematical expressions across custom intervals, render 64-point vector curve plots on the transflective screen, trace critical peaks and zero-crossings with interactive crosshairs, and overlay empirical statistical scatter points.

