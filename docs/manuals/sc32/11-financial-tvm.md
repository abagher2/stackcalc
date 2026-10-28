---
title: "Chapter 11: The Eight-Hundred-Year Engine of Compound Interest: Time Value of Money | Thinking in the Stack (SC-32)"
description: "Master the 5-variable Time Value of Money (TVM) solver, the Kahan base-preserving percentage invariant, mortgage amortization, corporate DCF, NPV, and IRR on the StackCalc SC-32."
---

# Chapter 11: The Eight-Hundred-Year Engine of Compound Interest: Time Value of Money

## Fibonacci's Merchants, The Percentage Asymmetry Trap & The Rule of 72

In the year 1202, a thirty-two-year-old Italian merchant's son named **Leonardo Pisano**—known to posterity as **Fibonacci**—returned to Pisa from the bustling Mediterranean ports of Bugia (in modern-day Algeria), Alexandria, and Constantinople. His father, Guglielmo Bonacci, had served as a customs official representing Pisan traders across North Africa, and young Leonardo had grown up watching Arab and North African mathematicians calculate with the nine Hindu-Arabic numerals (`1` through `9`) and the symbol `zephirum` (`0`), while European counting houses were still struggling to multiply Roman numerals (`MCCIV`) on counting boards.

When Fibonacci published his landmark treatise ***Liber Abaci*** (*The Book of Calculation*) in 1202, modern readers often assume it was a book about his famous breeding rabbits. In fact, the rabbit puzzle occupied barely half a page. Fibonacci filled the longest, most ambitious chapters of *Liber Abaci* with the real mathematical problem that kept twelfth-century Venetian, Genovese, and Pisan sea captains awake at night: **how do you compare a gold bezant in your hand today against a stream of payments arriving across different years in the future?**

Four centuries later, in 1613 London—just one year before John Napier unveiled his logarithms in Edinburgh—an English mathematician named **Richard Witt** published *Arithmeticall Questions, Touching the Buying or Exchange of Annuities*, the first comprehensive volume of compound-interest tables in the English language. Witt showed London merchants, landlords, and actuaries that **time acts like a geometric lens on money**: every year that a sum of capital $PV$ is put to work at periodic interest rate $i$, it is multiplied by the growth factor $(1 + i)$. Conversely, every year you have to wait in the future to receive a promised payment $FV$, its value today is *divided* by $(1 + i)$.

Whether you are a high-school student opening your first savings account, a college graduate comparing student loan repayment plans, a family signing a 30-year home mortgage, or a chief financial officer valuing a power plant, money is stored human time and labor. Understanding how percentages, compounding, and discounting work from the inside out is the single most practical mathematical skill of adult life.

### Why a 20% Loss Followed by a 20% Gain Leaves You Poorer: The Percentage Asymmetry Trap

Before we step into multi-year compound interest, let us expose a deceptively simple percentage illusion that fools millions of investors, shoppers, and business owners every day.

Suppose you invest $\$100.00$ in a stock index fund. During a turbulent autumn, the market **drops by $20\%$**. The next spring, the market rallies and **gains $20\%$**. Are you back to even at $\$100.00$?

Human intuition—trained since childhood on symmetric addition and subtraction ($-20 + 20 = 0$)—almost always says *yes*. Yet trace what actually happens to your money step by step:

1. **The $20\%$ Drop:** Losing $20\%$ of $\$100.00$ subtracts $\$20.00$, shrinking your investment base to $\$100.00 \times (1 - 0.20) = \mathbf{\$80.00}$.
2. **The $20\%$ Gain:** When the market rebounds by $+20\%$, that $20\%$ gain is not applied to your original $\$100.00$—it is applied to your shrunken **$\$80.00$** base. Twenty percent of $\$80.00$ is only $+\$16.00$, bringing your account to $\$80.00 \times (1 + 0.20) = \mathbf{\$96.00}$.

You are still down **$-4.0\%$**. And what if your stock drops by **$50\%$** (from $\$100$ down to $\$50$)? A $+50\%$ gain on $\$50$ only brings you back to $\$75$; to recover from a $50\%$ loss back to $\$100$, you need a **+$100\%$ gain**!

Why do equal percentage losses and gains never cancel out? Because percentages combine **multiplicatively**, not additively. Recall the high-school algebra identity for the difference of two squares when a fractional drop $-x$ is followed by an equal fractional gain $+x$:

$$(1 - x)(1 + x) = 1 - x^2 < 1$$

Whenever $x > 0$, the product $(1 - x)(1 + x)$ is strictly less than $1$ by the penalty $x^2$ (for $x = 0.20$, the penalty is $x^2 = 0.20^2 = 0.04 = 4\%$). That exact multiplicative reality also explains two everyday commercial surprises:

- **Stacked Retail Markdowns:** When a store advertises *"30% seasonal sale, plus an extra 15% VIP coupon"* on a $\$280.00$ jacket, you do not get $30\% + 15\% = 45\%$ off. Instead, the $30\%$ markdown reduces $\$280.00$ to $\$280 \times 0.70 = \$196.00$, and the $15\%$ coupon takes $15\%$ off that $\$196.00$ sale price ($\$29.40$), leaving $\$196.00 \times 0.85 = \mathbf{\$166.60}$—an effective combined discount of $1 - (0.70)(0.85) = \mathbf{40.5\%}$.
- **The Markup vs. Gross Margin Trap:** Suppose a hardware startup builds a device for a landed cost of $C = \$60.00$, and the company's financial plan requires a **$40\%$ Gross Margin** (meaning $40\%$ of the final *selling price* must be gross profit). If a manager mistakenly adds a $40\%$ **markup** onto the $\$60.00$ cost ($\text{Price} = \$60 + 0.40 \times \$60 = \$84.00$), the profit is $\$24.00$ out of an $\$84.00$ selling price—which is only $\$24 / \$84 = \mathbf{28.57\%}$ gross margin. To achieve a true $40\%$ gross margin from the inside out, if profit accounts for $40\%$ of the selling price, then the $\$60.00$ manufacturing cost must represent the remaining $1 - 0.40 = 60\%$ ($0.60$) of the selling price:

$$\text{Selling Price} = \frac{\text{Cost}}{1 - \text{Gross Margin}} = \frac{\$60.00}{1 - 0.40} = \frac{\$60.00}{0.60} = \mathbf{\$100.00}$$

### Why William Kahan Redesigned the Percentage Key—And How the Rule of 72 Works

Consider why so many people make mistakes with percentages: **every percentage only has meaning relative to its base amount**.

In 1979, UC Berkeley mathematician **William M. Kahan**—the chief architect of the IEEE-754 floating-point standard—published a celebrated analysis in the *Hewlett-Packard Journal* {{cite:kahan1979}} examining why conventional pocket calculators make percentage math so clumsy. On a typical algebraic calculator, if you want to add an $8.25\%$ sales tax to a $\$150.00$ invoice and you type `150 × 8.25 %`, the screen displays `12.38`—and **wipes out your original $\$150.00$ base amount**. To get the total invoice, you have to retype `+ 150 =` from scratch.

Kahan realized that in an inside-out stack architecture, a percentage key (`%`) should be **base-preserving**: when you have your base amount ($Y = 150.00$) on the second shelf and your percentage rate ($X = 8.25$) on the bottom shelf, pressing `%` should replace only the bottom shelf with the dollar tax ($X = 12.38$) while leaving your base amount ($Y = 150.00$) **untouched and visible right above it**. On the SC-32, the right-shifted **`{{key:%}}`** (Right Shift `{{key:↱}}` above `{{key:COS}}`) and **`{{key:%CHG}}`** (Right Shift `{{key:↱}}` above `{{key:TAN}}`) keys implement Kahan's base-preserving stack design directly: placing the base amount on Shelf $Y$ and the percentage on Shelf $X$ lets `{{key:%}}` compute the dollar adjustment on Shelf $X$ while keeping your original base intact on Shelf $Y$, ready for an immediate `{{key:+}}` (tax or markup) or `{{key:-}}` (discount).

What happens when a percentage rate $r\%$ is applied not once, but over and over again across $N$ years? Each year multiplies your balance by $(1 + r/100)$, turning addition into exponential growth:

$$FV = PV \left(1 + \frac{r}{100}\right)^N$$

How many years $N$ does it take for compound interest at an annual rate of $r\%$ to **double** your money ($FV / PV = 2$)? Taking the natural logarithm (from Chapter 3) of both sides:

$$\left(1 + \frac{r}{100}\right)^N = 2 \quad \Longrightarrow \quad N \ln\!\left(1 + \frac{r}{100}\right) = \ln 2 \approx 0.693147$$

As we saw in Chapter 3, for normal interest rates ($r \le 12\%$), the Taylor approximation $\ln(1 + r/100) \approx r/100$ gives $N \approx \frac{69.3}{r}$. And why did Franciscan friar **Luca Pacioli**—who first printed the rule in his monumental *Summa de arithmetica* (Venice, 1494)—and Renaissance merchants across Venice and Florence round $69.3$ slightly upward to **$72$** (allowing for the slight curvature of discrete annual compounding around $r \approx 8\%$)? Because **$72$ is divisible by $1, 2, 3, 4, 6, 8, 9,$ and $12$**, giving you the famous mental **Rule of 72**:

$$\text{Doubling Time (Years)} \approx \frac{72}{\text{Annual Interest Rate } r\%}$$

At $6\%$ annual return, your money doubles in about $72 / 6 = \mathbf{12\text{ years}}$; at $8\%$, in $72 / 8 = \mathbf{9\text{ years}}$; at $9\%$, in $72 / 9 = \mathbf{8\text{ years}}$. Conversely, if inflation runs at $3.2\%$ per year for $20\text{ years}$, dividing $\$100,000$ of uninvested cash by $(1.032)^{20} \approx 1.8776$ shrinks its real purchasing power nearly in half, down to **$\$53,260.60$**.

---

## The Master Equation of Time and Money—And the Mortgage Amortization Surprise

### How a Geometric Series Builds the Five-Variable TVM Balance Law

In real life, we rarely deposit a single lump sum and walk away for thirty years. Usually, three flows of money interact across $N$ compounding periods at periodic interest rate $i$:

1. **$PV$ (Present Value):** The starting lump sum at time $t = 0$ (such as a $\$350,000$ home mortgage loan or an initial retirement balance).
2. **$PMT$ (Periodic Payment):** A steady stream of equal payments made at every period $k = 1, 2, \dots, N$ (such as a monthly mortgage check, car payment, or 401(k) contribution).
3. **$FV$ (Future Value):** The final balance left at the end of period $N$ ($0$ for a fully paid-off loan, or a target nest egg for retirement).

How do all five variables—$N, i, PV, PMT,$ and $FV$—fit into a single mathematical equation?

Think of the present moment ($t = 0$) as the balance fulcrum of a scale. Every payment $PMT$ that arrives $k$ periods in the future must be discounted back to today by dividing by $(1 + i)^k$, and the final balance $FV$ at period $N$ must be discounted by $(1 + i)^N$:

$$PV + \frac{PMT}{(1+i)^1} + \frac{PMT}{(1+i)^2} + \cdots + \frac{PMT}{(1+i)^N} + \frac{FV}{(1+i)^N} = 0$$

Examine that middle sum of $N$ discounted payments: it is a classic high-school **geometric series** with common ratio $q = (1 + i)^{-1}$. Using Euclid's formula for the sum of a finite geometric series, those $N$ terms collapse into a single closed-form expression called the **Annuity Present-Value Factor ($a_{\overline{N}|i}$)**:

$$\sum_{k=1}^{N} (1 + i)^{-k} = \frac{1 - (1 + i)^{-N}}{i} = a_{\overline{N}|i}$$

Substituting that closed form gives the **Master Five-Variable Time Value of Money (`TVM`) Equation**:

$$PV + PMT \left[ \frac{1 - (1 + i)^{-N}}{i} \right] + FV (1 + i)^{-N} = 0$$

*(For an **Annuity Due**—such as an apartment lease or tuition payment where each check is paid at the **beginning** of the period rather than the end—each payment earns one extra period of compounding, multiplying the $PMT$ bracket by $(1 + i)$.)*

On the SC-32, pressing **`{{key:TVM}}`** (Left Shift `{{key:↰}}` above `{{key:x∥y}}`) maps the six top dynamic LFU softkeys (`{{key:LFU0}}`–`{{key:LFU5}}`) directly to **`N`** (`{{key:N}}`), **`I%`** (denoted `{{key:I%YR}}` in keystroke sequences as a reminder to enter the periodic interest rate per compounding interval), **`PV`** (`{{key:PV}}`), **`PMT`** (`{{key:PMT}}`), **`FV`** (`{{key:FV}}`), and **`END`/`BEG`** (`{{key:LFU5}}`, which toggles directly between Ordinary Annuity `END` and Annuity Due `BEG`). The five numerical softkeys obey a simple, deterministic **Store-vs.-Solve Rule**: *tapping a TVM softkey right after typing or calculating a number on the stack **stores** that value from Register $X$ into the TVM register; tapping a TVM softkey immediately after another TVM softkey **solves** for that unknown variable into Register $X$.*

### Why Cash-Flow Sign Discipline Works Like Conservation of Energy

Why is the right-hand side of the Master TVM Equation equal to **zero**?

Because financial mathematics treats your wallet (or a company's treasury) exactly like a physical control volume in physics:
- **Cash Inflows ($+$) are Positive:** Any money flowing **into** your pocket (the $+\$350,000$ loan wire you receive from the bank when buying a house, or the $+\$1,000$ payout you receive when a bond matures) is entered with a **positive sign ($+$)**.
- **Cash Outflows ($-$) are Negative:** Any money flowing **out** of your pocket (the monthly mortgage check you mail to the bank, or the $-\$925.00$ purchase price you pay to buy a bond) is entered with a **negative sign ($-$)**.

When all cash inflows and outflows are discounted to the same point in time at the true interest rate $i$, **the net sum must balance to zero**. That physical sign rule immediately prevents confusion: if you receive a $+\$350,000$ mortgage loan today ($PV > 0$), your monthly repayments must flow *out* of your pocket ($PMT < 0$) to pay that debt down to $FV = 0$.

### The 30-Year Mortgage Amortization Surprise: Why Month 237 Is the Turning Point

Let us walk through the most consequential calculation most families ever make: taking out a **30-year fixed-rate home mortgage**.

Suppose a family borrows **$PV = +\$350,000.00$** for 30 years (**$N = 30 \times 12 = 360\text{ months}$**, paid down to **$FV = \$0.00$**) at an annual interest rate of **$6.75\%$ APR**. Because payments occur monthly, the periodic interest rate per month is:

$$i = \frac{6.75\%}{12} = 0.5625\%\text{ per month} = 0.005625$$

Substituting $N = 360$ and $i = 0.005625$ into the Master TVM Equation fixes the required level monthly payment:

$$PMT = -PV \times \frac{i}{1 - (1 + i)^{-N}}$$

When we run this exact mortgage on the SC-32 workbench in the next section, we will see that the monthly check comes to nearly $\$2,300$—and that over thirty years, the family's $360$ payments total more than $\$817,000$, meaning they pay over $\$467,000$ in pure interest (more than $1.33$ times the original $\$350,000$ loan)!

Even more surprising is the hidden anatomy of **Month 1**. When the family mails their very first monthly check, how much of that payment actually reduces their $\$350,000$ loan balance?
- First, the bank charges one month's interest ($i = 0.5625\%$) on the entire starting principal ($I_1 = PV \times i$), which devours **$86.7\%$ of the Month 1 payment**.
- Only the tiny leftover sliver ($P_1 = |PMT| - I_1$, just **$13.3\%$ of the payment**) reduces the principal balance!

Why does it take until **Month 237**—nearly **twenty years** into a thirty-year mortgage—before at least half of your monthly check goes toward paying down your own house?

Because on any level-payment loan of $N$ periods at rate $i$, the principal portion $P_k$ of payment $k$ grows exponentially from the inside out according to $P_k = |PMT|(1 + i)^{-(N - k + 1)}$. Setting $P_k = \frac{1}{2}|PMT|$ shows that the **Amortization Crossover** occurs when $(1 + i)^{N - k + 1} = 2$—which is our exact **Rule of 72 doubling time** counted *backward from the end of the loan*. At $6.75\%$ APR ($i = 0.005625/\text{month}$), the doubling time is $\frac{\ln 2}{\ln(1.005625)} \approx 123.57\text{ months}$ ($\approx 10.3\text{ years}$) before Month $361$, landing right at Month $361 - 123.57 = \mathbf{237.43}$.

And that reveals a life-changing financial secret: **because early principal reduction is barely one-eighth of the monthly check, adding even a modest extra principal payment in the early years leaps forward along the exponential curve.** As we will verify to the exact cent on the stack below, adding just **$\$250.00\text{ per month}$** of extra principal nearly *doubles* the Month 1 principal reduction—eliminating more than **seven years of monthly payments** and saving over **$\$134,000$** in lifetime interest!

---

## Valuing Future Cash Streams: Bonds, Net Present Value & Why IRR Needs a Root Solver

### Why Bond Prices Move Opposite to Interest Rates

Step from the homeowner's kitchen table onto a bond trading desk. A **bond** is simply a tradable loan: when a corporation or government issues a 10-year, $\$1,000$ par-value bond with a $5.5\%$ annual coupon paid semi-annually ($N = 20$ six-month periods), the issuer promises to pay the bondholder **$PMT = +\$27.50$ every six months** for twenty periods, plus the **$FV = +\$1,000.00$ principal** at maturity.

Why does the market price ($PV$) of an existing bond **fall** whenever market interest rates **rise**?

Because the bond's future cash promises ($+\$27.50$ every six months and $+\$1,000$ at maturity) are printed in ink and cannot change. If new bonds in the market are suddenly paying $6.53\%$ annual yield ($3.2666\%$ per half-year), no investor will pay $\$1,000$ for your older $5.5\%$ bond unless you **discount its purchase price** down to **$PV = -\$925.00$**, so that the $\$75.00$ capital gain at maturity makes up for the lower semi-annual coupons. Because a bond is a level-coupon annuity plus a maturity redemption, the SC-32's `{{key:TVM}}` menu models bond prices (`{{key:PV}}`) and periodic yield (`I%`, denoted `{{key:I%YR}}`) in a single softkey tap.

In 1938, economist **Frederick Macaulay** asked a brilliant physical question about bonds: if a 3-year bond pays coupons at Year 1, Year 2, and Year 3 (plus principal at Year 3), what is the *effective waiting time* until you get your money back? Macaulay imagined placing weights along a horizontal beam at $t = 1, 2, 3\text{ years}$, where each weight equals the **present value** of that year's cash flow. The center-of-mass pivot point where that beam balances—identical in algebra to Archimedes' weighted centroid $\bar{x}_w = \frac{\sum t_k w_k}{\sum w_k}$ that we computed on the statistical bus in Chapter 6!—is **Macaulay Duration ($D$)**. Dividing by $(1 + y)$ gives **Modified Duration ($D^*$)**, which measures the exact percentage lever tilt in the bond's price for every $1\%$ shift in market interest rates:

$$\frac{\Delta P}{P} \approx -D^* \cdot \Delta y = -\frac{D}{1 + y} \cdot \Delta y$$

That mechanical seesaw explains why a 2-year Treasury note ($D^* \approx 1.9\text{ years}$) barely flinches when interest rates rise by $1\%$ ($\Delta P/P \approx -1.9\%$), whereas a 30-year zero-coupon bond—all of whose weight sits at the far end of a thirty-foot plank ($D = 30\text{ years}$)—plunges by nearly $30\%$ on the exact same rate hike!

### Net Present Value (`NPV`) as a Horner Polynomial—And Why `IRR` Needs Richard Brent's Solver

What if an entrepreneur or corporate board is evaluating a factory, a solar array, or a software company whose future cash flows are **uneven**—say, generating free cash flows of $C_1 = \$10\text{M}$ in Year 1, $C_2 = \$12\text{M}$ in Year 2, $C_3 = \$15\text{M}$ in Year 3, and $C_4 = \$234\text{M}$ in Year 4 (operating cash flow plus terminal sale value), discounted at a $r = 10\%$ cost of capital?

Summing the present values of each year's cash flow gives the **Net Present Value (`NPV`)**:

$$\text{PV} = \frac{10}{1.10} + \frac{12}{1.10^2} + \frac{15}{1.10^3} + \frac{234}{1.10^4} = \mathbf{\$190.11\text{M}}$$

Viewed through the lens of **Chapter 7 (Polynomials & Root-Finding)**, if we write $x = 1 + r = 1.10$, discounting a stream of uneven cash flows is a **Horner polynomial in $1/x$**, peeled from the most distant year ($t = 4$) backward to the present ($t = 0$):

$$\text{PV} = \left(\left(\left(234 \div 1.10 + 15\right) \div 1.10 + 12\right) \div 1.10 + 10\right) \div 1.10$$

And that reveals a profound mathematical connection when we ask the inverse question: suppose a project costs $C_0 = -\$100,000$ upfront today and returns $C_1 = +\$30,000$, $C_2 = +\$40,000$, and $C_3 = +\$50,000$ over the next three years. What is the project's **Internal Rate of Return (`IRR`)**—the exact interest rate $r$ where the Net Present Value equals zero?

$$\text{NPV}(r) = -100,000 + \frac{30,000}{1+r} + \frac{40,000}{(1+r)^2} + \frac{50,000}{(1+r)^3} = 0$$

That equation reveals what we are really solving: finding the `IRR` (or finding the unknown periodic interest rate `I%` / `{{key:I%YR}}` on `{{key:LFU1}}` of a 30-year mortgage) is **finding the root of a polynomial of degree $N$**. As Niels Henrik Abel and Évariste Galois proved in Chapter 7, no algebraic radical formula exists when $N \ge 5$—and by **René Descartes's 1637 Rule of Signs**, a standard investment whose cash flows change sign only once ($-$ upfront, then $+, +, +$) is guaranteed to have a **unique positive root**, whereas a strip-mine or power-plant project that requires a large negative environmental cleanup outflow at the end ($-, +, +, -$) changes sign *twice* and can possess two distinct `IRR` roots! That is why the SC-32 pairs Horner evaluation on the 4-register stack with Richard Brent's **`{{key:SOLVE}}`** root-finder (and the 240-interval scan + bisection `{{key:TVM}}` engine across `N`, `I%`, `PV`, `PMT`, `FV`, and `END`/`BEG`) to model uneven `NPV` and `IRR` cash-flow streams right under its keys.

---

## On the Stack: Percentages, Mortgages & TVM Cash-Flow Workbench

Across every financial problem we have explored—from Kahan's base-preserving percentages and markup-versus-margin pricing to 30-year mortgage amortization, bond duration, and Horner discounted cash flows—notice how naturally inside-out thinking protects you from financial illusions. In your mind, you keep your baseline principal or invoice amount on an upper shelf while evaluating the tax delta, growth ratio, or discount factor on the active shelf below. On the StackCalc SC-32, Register `Y` holds that preserved baseline while Register `X` computes `{{key:%}}` or `{{key:%CHG}}`, and the dedicated five-variable `{{key:TVM}}` menu (`{{key:N}}`, `{{key:I%YR}}`, `{{key:PV}}`, `{{key:PMT}}`, `{{key:FV}}`) links directly to the stack. Let us step onto the workbench and walk through each calculation keystroke by keystroke.

{{res:sc32_tvm_pmt:screenshot|The SC-32 transflective display executing multi-variable financial calculations with continuous stack preservation.}}

### Base-Preserving Percentages (`%`), Chain Discounts & Gross Margin Pricing

To format currency outputs rounded to cents while retaining full 64-bit internal precision, set the display mode to two decimal places (`{{key:FIX}} 2`) via `{{key:DISP}}` $\to$ `{{key:FIX}}` $\to$ `2` {{cite:hp15c1982}}. On the StackCalc SC-32, the **Percentage Function (`{{key:%}}`)** adheres strictly to William Kahan's non-destructive specification {{cite:kahan1979}}:

$$\text{Calculation: } \quad X \leftarrow \frac{Y \times X}{100}, \quad Y \leftarrow Y \text{ (Preserved)}, \quad \text{Lift} \leftarrow \text{TRUE}$$

On a $\$150.00$ consulting invoice at $8.25\%$ sales tax, keying `{{res:sc32_11_financial_tvm_seq_06:keys}}` places $\$12.38$ in Register $X$ while holding $\$150.00$ in Register $Y$, so pressing `{{key:+}}` yields $\$162.38$ in a single stroke. Similarly, keying `{{res:sc32_11_financial_tvm_seq_44:keys}}` on a $\$100.00$ baseline places the exact dollar amount ($\mathbf{{{res:sc32_11_financial_tvm_seq_44:value}}}$) in Register $X$ while freezing $100.00$ in Register $Y$.

For an enterprise server order subtotaling $\$18,450.00$ with $8.25\%$ state sales tax in `{{key:FIX}} 2` mode, keying `{{res:sc32_11_financial_tvm_seq_07:keys}}` places the tax amount $X = \mathbf{\$1,522.13}$ below the preserved base $Y = \$18,450.00$, and pressing `{{key:+}}` sums the total invoice to **`$19,972.13`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `18450 {{key:ENTER}}` | 0.00 | 0.00 | 18450.00 | 18450.00 | Stage pre-tax subtotal $\$18,450.00$ in Register Y |
| `8.25 {{key:%}}` | 0.00 | 0.00 | 18450.00 | 1522.13 | Compute $8.25\%$ tax ($\$1,522.13$) in X; base preserved in Y |
| `{{key:+}}` | 0.00 | 0.00 | 0.00 | 19972.13 | Add tax to preserved base for total invoice $\$19,972.13$ |

Base-preserving percentages streamline discounts and multi-step splits just as cleanly:
- **Single Volume Discount:** On an $\$85,000.00$ software license with a $17.5\%$ volume discount, keying `{{res:sc32_11_financial_tvm_seq_08:keys}}` displays the dollar concession ($X = \mathbf{\$14,875.00}$) alongside the $\$85,000.00$ list price in $Y$, and pressing `{{key:-}}` yields the net invoice payable (**`$70,125.00`**).
- **Stacked Chain Markdowns:** For a $30\%$ seasonal sale followed by an extra $15\%$ VIP coupon on a $\$280.00$ jacket, keying `{{res:sc32_11_financial_tvm_seq_27:keys}}` followed by `{{key:-}}` deducts the first $30\%$ markdown $(\$84.00)$ to leave $\$196.00$ in Register $X$. Chaining `15 {{key:%}} {{key:-}}` then deducts the $15\%$ coupon $(\$29.40)$ against that reduced base to yield $\mathbf{\$166.60}$.
- **Shared vs. Itemized Bill Splitting:** To split an 8-person restaurant dinner bill of $\$480.00$ where 3 guests shared $\$96.00$ of wine while all 8 shared the food equally, deducting the wine tab via `{{res:sc32_11_financial_tvm_seq_25:keys}}` isolates the shared food bill $(\$384.00)$, and `8 {{key:÷}}` establishes the per-guest food share $(\$48.00)$. Computing the per-drinker wine share via `{{res:sc32_11_financial_tvm_seq_26:keys}}` places $\$32.00$ in Register $X$ beneath $\$48.00$ in Register $Y$, so pressing `{{key:+}}` resolves the wine-drinker total ($X = \mathbf{\$80.00}$).

To compare the **Markup Trap** against true **Gross Margin Pricing** on a product with landed cost $C = \$60.00$ and target $40.0\%$ gross margin: adding a $40\%$ markup onto $\$60.00$ (`{{res:sc32_11_exec_markup_trap:keys}}` $\rightarrow$ **`\${{res:sc32_11_exec_markup_trap:value}}`**) yields only $\$24 / \$84 = 28.57\%$ margin, whereas dividing cost by the margin complement $\text{Price} = \frac{\text{Cost}}{1 - \text{Margin}}$ via `{{res:sc32_11_exec_gross_margin_price:keys}}` resolves the true retail price **`\${{res:sc32_11_exec_gross_margin_price:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `60 {{key:ENTER}} 40 {{key:%}}` | 0.00 | 0.00 | 60.00 | 24.00 | 40% markup on \$60.00 cost: \$24.00 |
| `{{key:+}}` | 0.00 | 0.00 | 0.00 | 84.00 | Flawed markup price: \$84.00 (28.57% margin) |
| `60 {{key:ENTER}} 1 {{key:ENTER}}` | 84.00 | 60.00 | 1.00 | 1.00 | True margin pricing: stage cost \$60 in $Z$ and 1.00 in $Y$ |
| `.40 {{key:-}}` | 84.00 | 84.00 | 60.00 | 0.60 | 1 - 0.40 = 0.60 margin complement; \$60.00 drops to $Y$ |
| `{{key:÷}}` | 84.00 | 84.00 | 84.00 | 100.00 | True gross margin retail price: \$100.00 |

### Percent Change (`%CHG`), Cross-Metric Elasticity, CAGR & Inflation

The **Percent Change Function (`{{key:%CHG}}`)** is executed via Right Shift `{{key:↱}}` followed by `{{key:%CHG}}` using the chronological order **Old Value `{{key:ENTER}}` New Value `{{key:%CHG}}`**, preserving the Old Value in Register $Y$ and the New Value in `LASTX`.

Suppose a software company's **Annual Recurring Revenue (ARR)** grew from $\$12.0\text{M}$ to $\$15.6\text{M}$ (`{{res:sc32_11_financial_tvm_seq_10:keys}}` $\rightarrow +30.00\%$), while **Customer Acquisition Cost (CAC)** expanded from $\$2.4\text{M}$ to $\$2.88\text{M}$ (`{{res:sc32_11_financial_tvm_seq_11:keys}}` $\rightarrow +20.00\%$). Dropping the old baseline out of the way (`{{key:x⇄y}} {{key:R↓}}`) aligns ARR growth ($Y = 30.00$) and CAC growth ($X = 20.00$) side-by-side on the stack, where pressing `{{key:-}}` yields the **`+10.00%`** growth spread and keying `{{res:sc32_11_financial_tvm_seq_12:keys}}` computes the **`{{res:sc32_11_financial_tvm_seq_12:value}}`** growth elasticity multiplier:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `12 {{key:ENTER}} 15.6 {{key:%CHG}}` | 0.00 | 0.00 | 12.00 | 30.00 | ARR growth $+30.00\%$ in X; baseline $12.00$ in Y |
| `2.4 {{key:ENTER}} 2.88 {{key:%CHG}}` | 12.00 | 30.00 | 2.40 | 20.00 | CAC growth $+20.00\%$ in X; ARR growth lifts to Z |
| `{{key:x⇄y}}` | 12.00 | 30.00 | 20.00 | 2.40 | Swap CAC baseline $2.40$ into X |
| `{{key:R↓}}` | 2.40 | 12.00 | 30.00 | 20.00 | Roll stack down to align $30.00\%$ in Y and $20.00\%$ in X |
| `{{key:-}}` | 2.40 | 2.40 | 12.00 | 10.00 | ARR vs. CAC growth spread $+10.00$ percentage points |

To compute the 5-year **Compound Annual Growth Rate (`CAGR`)** of a venture investment that grows from $\$14.0\text{M}$ to $\$88.5\text{M}$ over $n = 5\text{ years}$ ($\text{CAGR} = (88.5 / 14.0)^{1/5} - 1$), keying `{{res:sc32_11_financial_tvm_seq_13:keys}}` reveals **`{{res:sc32_11_financial_tvm_seq_13:value}}`**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `88.5 {{key:ENTER}}` | 0.00 | 0.00 | 88.50 | 88.50 | Stage exit valuation $\$88.50\text{M}$ in Register Y |
| `14.0 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 6.32 | Terminal wealth multiple $88.5 / 14.0 = 6.3214\times$ |
| `5 {{key:1/x}}` | 0.00 | 0.00 | 6.32 | 0.20 | Reciprocal exponent $1/5 = 0.20$ |
| `{{key:yˣ}}` | 0.00 | 0.00 | 0.00 | 1.45 | Annualized growth factor $(6.3214)^{0.20} = 1.4460$ |
| `1 {{key:-}}` | 0.00 | 0.00 | 0.00 | 0.45 | Deduct unity for decimal growth rate $0.4460$ |
| `100 {{key:×}}` | 0.00 | 0.00 | 0.00 | 44.60 | Scale to percentage: $\text{CAGR} = 44.60\%/\text{yr}$ |

Conversely, deflating $\$100,000$ of uninvested cash by 20 years of $3.2\%$ annual CPI inflation ($PV = 100,000 / (1.032)^{20}$) via `{{res:sc32_11_financial_tvm_seq_03:keys}}` reveals that purchasing power erodes to **`{{res:sc32_11_financial_tvm_seq_03:value}}`** ($\mathbf{\$53,260.60}$). And to convert a nominal $18.5\%$ APR compounded monthly ($m = 12$) into its true **Effective Annual Rate ($\text{EAR} = (1 + 0.185/12)^{12} - 1$)** with `12` typed only once, key `0.185 {{key:ENTER}} 12 {{key:÷}} {{key:LASTX}} {{key:x⇄y}} 1 {{key:+}} {{key:x⇄y}} {{key:yˣ}} 1 {{key:-}} 100 {{key:×}}` $\implies \mathbf{20.15\%}$.

### The Five-Variable `TVM` Engine: Mortgages, Amortization & Balloon Notes

The onboard **Five-Variable Time Value of Money (`TVM`) Engine** is accessed via Left Shift `{{key:↰}}` above `{{key:x∥y}}` (Row 7, Column 3):

| TVM Variable | LFU Softkey | Actuarial Description | Computational Units |
| :---: | :---: | :--- | :--- |
| **$N$** | `{{key:N}}` (`{{key:LFU0}}`) | Total number of compounding periods | Integer or fractional periods |
| **$I\%$** | `{{key:I%YR}}` (`{{key:LFU1}}`) | Periodic interest rate per compounding period ($i\%$) | Percent per period (e.g. `6.5` for 6.5%/yr or `6.75/12 = 0.5625` for monthly) |
| **$PV$** | `{{key:PV}}` (`{{key:LFU2}}`) | Present value (initial loan principal or investment) | Currency ($) |
| **$PMT$** | `{{key:PMT}}` (`{{key:LFU3}}`) | Periodic annuity payment amount | Currency ($ per period) |
| **$FV$** | `{{key:FV}}` (`{{key:LFU4}}`) | Future value (final balloon balance or accumulated savings) | Currency ($) |
| **Mode** | `END/BEG` (`{{key:LFU5}}`) | Payment timing within each period | `END` (Ordinary Annuity) or `BEG` (Annuity Due) |

> **Four Essential `TVM` Rules (`Store-vs.-Solve`, Periodic Rate $i\%$, `END/BEG`, and Persistent Registers):**
> 1. **Store vs. Solve:** Tapping any TVM softkey right after typing or calculating a number on the stack **stores** that value from Register $X$ into the TVM register. Tapping a TVM softkey immediately after another TVM softkey **solves** for that unknown variable into Register $X$.
> 2. **Periodic Interest Rate ($i\%$):** The second TVM softkey (`I%` on `{{key:LFU1}}`, denoted `{{key:I%YR}}` in keystroke sequences) always stores the **periodic interest rate per compounding period ($i\%$)**. For a monthly mortgage, always divide the annual APR by $12$ (`6.75 {{key:ENTER}} 12 {{key:÷}}` $\to 0.5625\%$) before tapping the softkey.
> 3. **Ordinary Annuity (`END`) vs. Annuity Due (`BEG`):** Softkey `{{key:LFU5}}` (`END/BEG`) toggles directly between **Ordinary Annuity (`END`)**, where payments occur at the *end* of each period (standard for mortgages, auto loans, and bonds), and **Annuity Due (`BEG`)**, where payments occur at the *beginning* of each period (standard for monthly apartment rent, equipment leases, and insurance premiums).
> 4. **Persistent TVM Registers:** Because the five `TVM` registers intentionally retain their stored values across calculations for rapid "what-if" sensitivity analysis, always zero any unused register (such as `0 {{key:FV}}` on a fully amortizing loan with no balloon payment, or `{{key:CLEAR}}` $\to$ `{{key:CLVARS}}` on `{{key:LFU1}}`) before starting a new financial problem!

For our 30-year fixed residential mortgage of $PV = +\$350,000.00$ ($N = 360\text{ months}$, $FV = \$0.00$) at $6.75\%$ APR (monthly periodic rate $i = 6.75 / 12 = 0.5625\%$), store the four known variables (explicitly zeroing `0 {{key:FV}}`) and press `{{key:PMT}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `360 {{key:N}}` | 0.00 | 0.00 | 0.00 | 360.00 | Store term $N = 360\text{ months}$ |
| `.5625 {{key:I%YR}}` | 0.00 | 0.00 | 360.00 | 0.56 | Store monthly periodic rate $i = 0.5625\%$ |
| `350000 {{key:PV}}` | 0.00 | 360.00 | 0.56 | 350000.00 | Store loan principal inflow $PV = +\$350,000.00$ |
| `0 {{key:FV}}` | 360.00 | 0.56 | 350000.00 | 0.00 | Zero unused balloon register $FV = \$0.00$ before solving |
| `{{key:PMT}}` | 360.00 | 0.56 | 350000.00 | -2270.09 | Solve monthly mortgage outflow $PMT = -\$2,270.09$ |
| `360 {{key:×}}` | 0.56 | 0.56 | 350000.00 | -817233.60 | Total 30-year payments $-\$817,233.60$ |
| `350000 {{key:+}}` | 0.56 | 0.56 | 350000.00 | -467233.60 | Total lifetime interest paid $-\$467,233.60$ |

To inspect the Month 1 interest/principal split ($I_1 = \$1,968.75$ vs. $P_1 = \$301.34$) and remaining balance directly on the stack:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `350000 {{key:ENTER}}` | 0.00 | 0.00 | 350000.00 | 350000.00 | Stage initial principal $\$350,000.00$ |
| `0.005625 {{key:×}}` | 0.00 | 0.00 | 0.00 | 1968.75 | Month 1 interest charge $I_1 = \$1,968.75$ ($86.7\%$) |
| `2270.09 {{key:x⇄y}} {{key:-}}` | 0.00 | 0.00 | 0.00 | 301.34 | Month 1 principal reduction $P_1 = \$301.34$ ($13.3\%$) |
| `350000 {{key:x⇄y}} {{key:-}}` | 0.00 | 0.00 | 0.00 | 349698.66 | Remaining balance after Month 1: $\$349,698.66$ |

Comparing Month 1 against the Month 237 crossover and Month 360 payoff highlights the exponential amortization trajectory across the life of the loan:

| Month | Remaining Balance | Monthly Payment | Interest ($I_k$) | Principal ($P_k$) | Equity % | Financial Milestone |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **1** | $\$349,698.66$ | $\$2,270.09$ | $\$1,968.75$ | $\$301.34$ | $0.09\%$ | $86.7\%$ of check goes straight to interest |
| **237** | $\$199,642.18$ | $\$2,270.09$ | $\$1,130.71$ | $\$1,139.38$ | $42.96\%$ | **Amortization Crossover:** $P_k$ finally overtakes $I_k$ |
| **360** | $\$0.00$ | $\$2,270.09$ | $\$12.70$ | $\$2,257.39$ | $100.00\%$ | Final payoff; $\$467,233.60$ total lifetime interest |

Now add **$\$250.00/\text{month}$** in extra principal ($PMT = -\$2,520.09/\text{mo}$) and solve for the accelerated payoff term `{{key:N}}` via `{{res:sc32_11_realtor_extra_principal_months:keys}}`, which drops the repayment horizon to **`{{res:sc32_11_realtor_extra_principal_months:value}}` months** ($22.6\text{ years}$, saving $89\text{ payments}$ and $\$134,474.66$ in interest):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `6.75 {{key:ENTER}} 12 {{key:÷}} {{key:I%YR}}` | 0.00 | 0.00 | 0.00 | 0.56 | Monthly rate i = 0.5625% |
| `350000 {{key:PV}} 0 {{key:FV}}` | 0.00 | 0.56 | 350000.00 | 0.00 | Store PV = \$350,000.00 and zero FV = \$0.00 before solving |
| `2520.09 {{key:+/-}} {{key:PMT}}` | 0.56 | 350000.00 | 0.00 | -2520.09 | Augmented payment: -\$2,520.09/mo |
| `{{key:N}}` | 0.56 | 350000.00 | 0.00 | 270.93 | Accelerated repayment: 270.93 months |

For a commercial **5-year balloon note** lending $\$500,000$ at $7.5\%$ APR ($i = 0.625\%/\text{month}$) amortized over 25 years ($N = 300\text{ months}$) with a 5-year balloon maturity ($N = 60\text{ months}$), solve for `{{key:PMT}}` at $N = 300$ via `{{res:sc32_11_financial_tvm_seq_17:keys}}` $\rightarrow$ **`{{res:sc32_11_financial_tvm_seq_17:value}}`**, and then key `60 {{key:N}} {{key:FV}}` to find the exact balloon payoff at Month 60 (**`-$458,662.75`**):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `300 {{key:N}}` | 0.00 | 0.00 | 0.00 | 300.00 | Store 25-year amortization schedule $N = 300\text{ months}$ |
| `.625 {{key:I%YR}}` | 0.00 | 0.00 | 300.00 | 0.63 | Store monthly periodic rate $7.5\% / 12 = 0.625\%$ |
| `500000 {{key:PV}}` | 0.00 | 300.00 | 0.63 | 500000.00 | Store commercial loan principal $PV = +\$500,000.00$ |
| `0 {{key:FV}}` | 300.00 | 0.63 | 500000.00 | 0.00 | Target $FV = 0$ over full 300-month amortization |
| `{{key:PMT}}` | 300.00 | 0.63 | 500000.00 | -3694.96 | Monthly payment $PMT = -\$3,694.96$ |
| `60 {{key:N}}` | 0.63 | 500000.00 | -3694.96 | 60.00 | Set horizon to 5-year maturity ($N = 60\text{ months}$) |
| `{{key:FV}}` | 0.63 | 500000.00 | -3694.96 | -458662.75 | Remaining 5-year balloon payoff $FV = -\$458,662.75$ |

Every `{{key:TVM}}` calculation can also be cross-checked directly from the closed-form annuity identities on the 4-level stack (for the full reference compendium, see **[Appendix D: Section 9](appendix-d-constants-and-equations.md)**):

| Financial Instrument | Analytical Closed-Form Formula | Native RPN Inside-Out Recipe |
| :--- | :--- | :--- |
| **Ordinary Annuity PV** | $PV = PMT \left[ \frac{1 - (1 + i)^{-N}}{i} \right]$ | `1 ENTER i + N +/- yˣ 1 x⇄y - i ÷ PMT ×` |
| **Ordinary Annuity FV** | $FV = PMT \left[ \frac{(1 + i)^N - 1}{i} \right]$ | `1 ENTER i + N yˣ 1 - i ÷ PMT ×` |
| **Amortization Payment** | $PMT = PV \left[ \frac{i}{1 - (1 + i)^{-N}} \right]$ | `1 ENTER i + N +/- yˣ 1 x⇄y - i x⇄y ÷ PV ×` |
| **Sinking Fund Payment** | $PMT = FV \left[ \frac{i}{(1 + i)^N - 1} \right]$ | `1 ENTER i + N yˣ 1 - i x⇄y ÷ FV ×` |

### Bond Yield to Maturity (`YTM`), Duration, `NPV`, `IRR` & Portfolio Risk

For a 10-year corporate bond ($N = 20$ semi-annual periods) with par value $FV = +\$1,000.00$ and a $5.5\%$ annual coupon paid semi-annually ($PMT = +\$27.50$) purchased at $PV = -\$925.00$, storing $N, PV, PMT, FV$ and pressing `{{key:I%YR}}` finds the semi-annual yield $3.2666\%$, which doubles (`2 {{key:×}}`) to the annualized **Yield to Maturity $\text{YTM} = \mathbf{6.53\%}$**:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `20 {{key:N}}` | 0.00 | 0.00 | 0.00 | 20.00 | Store $N = 20$ semi-annual coupon periods |
| `925 {{key:+/-}} {{key:PV}}` | 0.00 | 0.00 | 20.00 | -925.00 | Store bond purchase price outflow $PV = -\$925.00$ |
| `27.50 {{key:PMT}}` | 0.00 | 20.00 | -925.00 | 27.50 | Store semi-annual coupon inflow $PMT = +\$27.50$ |
| `1000 {{key:FV}}` | 20.00 | -925.00 | 27.50 | 1000.00 | Store maturity par redemption $FV = +\$1,000.00$ |
| `{{key:I%YR}}` | 20.00 | -925.00 | 27.50 | 3.27 | Solve semi-annual periodic yield $i = 3.2666\%$ |
| `2 {{key:×}}` | -925.00 | -925.00 | 27.50 | 6.53 | Annualized bond-equivalent $\text{YTM} = 6.53\%$ |

To evaluate **Macaulay Duration ($D$)** and **Modified Duration ($D^*$)** for a 3-year $8.0\%$ annual coupon bond trading at par ($\$1,000.00$, yield $y = 8.0\%$), accumulate the time-weighted present values $\sum t \cdot C_t / (1.08)^t$ and divide by price and $(1 + y)$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `80 {{key:ENTER}} 1.08 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 74.0741 | Year 1 weighted PV: $1 \times 80 / 1.08 = \$74.0741$ |
| `80 {{key:ENTER}} 1.08 {{key:ENTER}} 2 {{key:yˣ}} {{key:÷}} 2 {{key:×}} {{key:+}}` | 74.07 | 74.07 | 74.07 | 211.2483 | Add Year 2 weighted PV ($2 \times 80 / 1.08^2 = \$137.1742$) |
| `1080 {{key:ENTER}} 1.08 {{key:ENTER}} 3 {{key:yˣ}} {{key:÷}} 3 {{key:×}} {{key:+}}` | 211.25 | 211.25 | 211.25 | 2783.2648 | Add Year 3 weighted PV ($3 \times 1080 / 1.08^3 = \$2,572.02$) |
| `1000 {{key:÷}}` | 211.25 | 211.25 | 211.25 | 2.7833 | Divide by $\$1,000$ price for Macaulay Duration $D = 2.7833\text{ yr}$ |
| `1.08 {{key:÷}}` | 211.25 | 211.25 | 211.25 | 2.5771 | Divide by $1.08$ for Modified Duration $D^* = 2.5771\text{ yr}$ |

To discount a 4-year corporate free-cash-flow stream of $\$10\text{M}, \$12\text{M}, \$15\text{M},$ and $\$234\text{M}$ at a $10\%$ cost of capital ($\text{Enterprise Value} = \frac{10}{1.1} + \frac{12}{1.1^2} + \frac{15}{1.1^3} + \frac{234}{1.1^4}$), keying `{{res:sc32_11_financial_tvm_seq_18:keys}}` accumulates the four present values to **`{{res:sc32_11_financial_tvm_seq_18:value}}`** ($\mathbf{\$190.11\text{M}}$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `10 {{key:ENTER}} 1.1 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 9.09 | Year 1 discounted FCF: $10 / 1.10 = \$9.09\text{M}$ |
| `12 {{key:ENTER}} 1.1 {{key:x²}} {{key:÷}}` | 0.00 | 0.00 | 9.09 | 9.92 | Year 2 discounted FCF: $12 / 1.10^2 = \$9.92\text{M}$ |
| `{{key:+}}` | 0.00 | 0.00 | 0.00 | 19.01 | Cumulative PV through Year 2: $\$19.01\text{M}$ |
| `15 {{key:ENTER}} 1.1 {{key:ENTER}} 3 {{key:yˣ}} {{key:÷}}` | 19.01 | 19.01 | 19.01 | 11.27 | Year 3 discounted FCF: $15 / 1.10^3 = \$11.27\text{M}$ |
| `{{key:+}}` | 19.01 | 19.01 | 19.01 | 30.28 | Cumulative PV through Year 3: $\$30.28\text{M}$ |
| `234 {{key:ENTER}} 1.1 {{key:ENTER}} 4 {{key:yˣ}} {{key:÷}}` | 30.28 | 30.28 | 30.28 | 159.83 | Year 4 discounted FCF + terminal value: $\$159.83\text{M}$ |
| `{{key:+}}` | 30.28 | 30.28 | 30.28 | 190.11 | Total Enterprise Value $\text{PV} = \$190.11\text{M}$ |

*(Horner Nested Discounting via Register $T$: Keying `1.1 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}} 234 {{key:x⇄y}} {{key:÷}} 15 {{key:+}} {{key:x⇄y}} {{key:÷}} 12 {{key:+}} {{key:x⇄y}} {{key:÷}} 10 {{key:+}} {{key:x⇄y}} {{key:÷}}` evaluates $\mathbf{\$190.11\text{M}}$ with `1.1` typed only once and zero `{{key:yˣ}}` exponentiations.)*

To solve for the **Internal Rate of Return (`IRR`)** of an upfront outlay $C_0 = -\$100,000$ returning $C_1 = \$30,000$, $C_2 = \$40,000$, and $C_3 = \$50,000$, enter the Horner-nested equation `50000 X {{key:÷}} 40000 {{key:+}} X {{key:÷}} 30000 {{key:+}} X {{key:÷}} 100000 {{key:-}}` in `{{key:EQN}}` mode (where $X = 1 + r$, and each variable token `X` inside `{{key:EQN}}` is keyed via `{{key:RCL}} X`, i.e., `{{key:RCL}}` followed by `{{key:2}}`). In the stack trace below, `1.10 {{key:STO}} X` seeds both variable `X` and Register $X$ with the initial guess $1.10$ ($10\%$) before invoking `{{key:SOLVE}} X` (or you can pass a two-guess bracket directly on the stack via `1.0 {{key:ENTER}} 1.2 {{key:SOLVE}} X`, just as we did in Chapter 7):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1.10 {{key:STO}} X` | 0.00 | 0.00 | 0.00 | 1.10 | Seed initial gross discount factor guess $X = 1.10$ ($10\%$) |
| `{{key:SOLVE}}X` | 0.00 | 0.00 | 1.10 | 1.08889 | Invoke `{{key:SOLVE}} X`; Brent's solver finds $\text{NPV}(X) = 0$ at $X = 1.08889$ |
| `1 {{key:-}}` | 0.00 | 0.00 | 1.10 | 0.08889 | Deduct unity for decimal internal rate of return $r = 0.08889$ |
| `100 {{key:×}}` | 0.00 | 0.00 | 1.10 | 8.89 | Scale to percentage: $\text{IRR} = 8.89\%/\text{yr}$ |

Finally, to evaluate portfolio risk metrics on the stack: for a systematic strategy returning $R_p = 18.5\%$ against a risk-free rate $R_f = 4.5\%$ with annualized volatility $\sigma_p = 11.2\%$, keying `{{res:sc32_11_trader_sharpe_ratio:keys}}` yields **William Sharpe's Ratio** **`{{res:sc32_11_trader_sharpe_ratio:value}}`** ($\frac{18.5 - 4.5}{11.2} = \mathbf{1.25}$). And for a trade setup with win probability $p = 0.56$ ($q = 0.44$) and payoff odds $b = 1.50$, keying `{{res:sc32_11_trader_kelly_criterion:keys}}` evaluates **John Kelly's Criterion** $f^* = \frac{bp - q}{b} \times 100$ to **`{{res:sc32_11_trader_kelly_criterion:value}}`** ($\mathbf{26.67\%}$)—or with `0.56` and `1.5` each typed only once via `1 {{key:ENTER}} 0.56 {{key:-}} {{key:LASTX}} {{key:x⇄y}} 1.5 {{key:÷}} {{key:-}} 100 {{key:×}}`.

---

### From Single Numbers to the Full Picture

Step back and look at what every calculation across the first eleven chapters of this book has had in common. Whether we solved for the resonant frequency of an AC circuit in Chapter 5, the draft depth of a floating sphere in Chapter 7, a definite Romberg integral in Chapter 8, a Pearson correlation coefficient $r$ in Chapter 9, a 36-bit hexadecimal subnet mask in Chapter 10, or a monthly mortgage payment and internal rate of return in this chapter, **our answer was always a single number at a single point**.

A single high-precision number is indispensable when you already know the shape of the landscape around it. Yet a single number—even when computed to twelve decimal places—is like looking at a mountain range through a pinhole:
* In **root-finding (`SOLVE`)**, a single root $x_1 = 1.42$ cannot tell you at a glance whether the function crosses the horizontal axis a second and third time just a few units to the right, or whether the curve barely grazed the axis near a flat extremum.
* In **physics and financial modeling**, a single cash-flow yield or damping constant cannot show you the visual silhouette of an underdamped suspension ringdown envelope $e^{-\zeta\omega_n t}\cos(\omega_d t)$ or the crossover point where an exponential growth curve overtakes a linear baseline.
* And in **experimental statistics (`L.R.`)**, as Yale statistician Francis Anscombe famously demonstrated in 1973, wildly different scatter patterns can hide behind the exact same summary mean, slope, and correlation coefficient $r$ if you never look at the graph!

How do you step back from a single numerical coordinate and see the **entire behavior of a function or dataset at a single glance** on a pocket screen? And how does a discrete grid of $132 \times 65$ square monochrome pixels transform continuous algebra into smooth geometric curves? That question takes us to a French philosopher's bedroom ceiling in 1637—and to **[Chapter 12: Seeing the Invisible: From Descartes's Bedroom Ceiling to the Pixel Grid](12-function-scatter-plotting.md)**.
