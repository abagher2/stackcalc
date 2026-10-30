---
title: "Chapter 11: Compound Interest, Amortization & the Time Value of Money | Thinking in the Stack (SC-32)"
description: "The 5-variable Time Value of Money (TVM) solver, William Kahan's base-preserving percentage invariant, mortgage amortization, corporate DCF, NPV, and IRR on the StackCalc SC-32."
---

# Chapter 11: Compound Interest, Amortization & the Time Value of Money

## Fibonacci's Merchants, Percentage Asymmetry & The Rule of 72

In 1202, Leonardo Pisano, known to posterity as Fibonacci, returned to Pisa from the commercial ports of Bugia (in modern-day Algeria), Alexandria, and Constantinople. His father, Guglielmo Bonacci, had served as a customs official representing Pisan traders across North Africa, and young Leonardo had grown up watching Arab and North African mathematicians calculate with the nine Hindu-Arabic numerals (`1` through `9`) and the symbol `zephirum` (`0`), while European counting houses were still struggling to multiply Roman numerals (`MCCIV`) on counting boards.

When Fibonacci completed his treatise *Liber Abaci* (*The Book of Calculation*) in 1202, popular history remembered the work chiefly for its exercise on breeding rabbits. In fact, that rabbit problem occupied barely half a page. Fibonacci filled the longest, most ambitious chapters of *Liber Abaci* with the real mathematical problem that kept twelfth-century Venetian, Genovese, and Pisan sea captains awake at night: comparing the worth of a gold bezant in hand today against a stream of payments arriving across different years in the future.

Four centuries later, after Simon Stevin printed the first public compound-interest tables in Leiden (*Tafelen van Interest*, 1582), English mathematician Richard Witt published *Arithmeticall Questions, Touching the Buying or Exchange of Annuities* in 1613 London, just one year before John Napier unveiled his logarithms in Edinburgh. Witt demonstrated to London merchants, landlords, and actuaries that time acts as a geometric operator on capital: every period that a principal $PV$ is invested at periodic rate $i$, it scales by the growth factor $(1 + i)$. Conversely, every period one must wait to receive a promised future sum $FV$, its present value is discounted through division by $(1 + i)$.

Across personal savings, amortizing residential mortgages, fixed-income securities, and corporate capital budgeting, compound growth and present-value discounting translate cash flows occurring at different dates into a single common measure of value.

### Multiplicative Asymmetry in Percentage Gains and Losses

Even over a two-period horizon, percentage changes exhibit a fundamental asymmetry between gains and losses. When a portfolio of initial value $V_0$ suffers a fractional drawdown of $\delta$ during an autumn sell-off, and then rallies by an equal fractional gain of $+\delta$ the following spring, linear intuition—trained on symmetric addition and subtraction ($-\delta + \delta = 0$)—expects the portfolio to return to its starting balance $V_0$.

Tracing the capital across the two periods reveals the multiplicative asymmetry. Losing a fraction $\delta$ first reduces the initial capital $V_0$ to a diminished base of $V_1 = V_0(1 - \delta)$; for a $20\%$ drop on $\$100.00$, the capital shrinks to $\$80.00$. When the market subsequently rebounds by $+\delta$, that percentage gain acts on the shrunken base $V_1$ rather than on $V_0$, bringing the terminal value to $V_2 = V_1(1 + \delta) = V_0(1 - \delta)(1 + \delta)$. On the $\$80.00$ base, a $+20\%$ gain adds only $+\$16.00$ and ends at $\$96.00$, so the portfolio remains down by $-4.0\%$. More dramatically, when an asset loses half its value ($\delta = 50\%$), a subsequent $+50\%$ gain restores only three-quarters of the initial principal; full recovery to $V_0$ requires solving $V_0(1 - \delta)(1 + g) = V_0$, which demands a hyperbolic recovery gain of $g = \frac{\delta}{1 - \delta}$ (or $+100\%$ after a $50\%$ loss, and $+25\%$ after a $20\%$ loss).

Equal percentage losses and gains never cancel out because percentages compose multiplicatively rather than additively. By the algebraic identity for the difference of two squares, a fractional drop $-\delta$ followed by an equal fractional gain $+\delta$ produces:

$$(1 - \delta)(1 + \delta) = 1 - \delta^2 < 1$$

Whenever $\delta > 0$, the product $(1 - \delta)(1 + \delta)$ falls short of unity by the quadratic volatility drag $\delta^2$ (for $\delta = 0.20$, the drag is $\delta^2 = 0.04 = 4\%$).

That same multiplicative structure governs successive chain markdowns and commercial gross-margin pricing. When a merchant applies a primary fractional markdown $d_1$ followed by an additional promotional discount $d_2$ at checkout, the two concessions do not sum to $d_1 + d_2$. Instead, the net retention factor is the product $(1 - d_1)(1 - d_2)$, so the effective combined discount is $d_{\text{eff}} = 1 - (1 - d_1)(1 - d_2) = d_1 + d_2 - d_1 d_2$. A $50\%$ clearance markdown followed by an extra $40\%$ off retains $0.50 \times 0.60 = 0.30$ of list price, an effective discount of $70\%$ rather than $90\%$.

Similarly, in commercial accounting, a markup rate $r$ is measured as a fraction of unit landed cost $C$ to produce a selling price of $P_{\text{markup}} = C(1 + r)$, whereas a gross margin requirement $m$ specifies the fraction of the final selling price $P$ retained as gross profit, $(P - C)/P = m$. Applying a cost markup of $r = m$ realizes a gross margin of only $\frac{m}{1 + m}$. To achieve a true target gross margin $m$, the unit cost $C$ must represent the complement $(1 - m)$ of the selling price:

$$P_{\text{margin}} = \frac{C}{1 - m}$$

### Base-Preserving Percentages and the Logarithmic Rule of 72

Everyday percentage calculations frequently go astray because every percentage only has meaning relative to its reference base.

In the 1970s, Hewlett-Packard's RPN calculator architects and UC Berkeley numerical analyst William M. Kahan, the chief architect of the IEEE-754 floating-point standard and financial solver algorithms {{cite:kahan1979}}, examined why conventional pocket calculators make percentage math so error-prone. On an algebraic calculator, computing a tax or discount rate $r\%$ on an invoice base $B$ via `B × r %` overwrites the display with the adjustment $B \cdot r / 100$ and destroys the original base $B$, so the operator must re-enter the base from scratch to obtain the net total.

Hewlett-Packard's architects and Kahan recognized that in an inside-out stack architecture, the percentage operator must be a two-register state transformation $(Y, X) \mapsto (Y, Y \cdot X / 100)$ that preserves the reference base in Register $Y$. On the SC-32, `{{key:%}}` (Right Shift `{{key:↱}}` above `{{key:COS}}`) and `{{key:%CHG}}` (Right Shift `{{key:↱}}` above `{{key:TAN}}`) enforce this base-preserving invariant. Staging the base amount in Register $Y$ and the percentage rate in Register $X$ lets `{{key:%}}` place the exact currency adjustment in Register $X$ while holding the original base untouched in Register $Y$, ready for `{{key:+}}` to add a tax or `{{key:-}}` to deduct a markdown in a single keystroke.

When a periodic growth rate $r\%$ compounds across $N$ consecutive periods, each period multiplies the balance by $(1 + r/100)$ and compounds additive rates into exponential growth:

$$FV = PV \left(1 + \frac{r}{100}\right)^N$$

To find the number of periods $N$ required for compound growth at rate $r\%$ to double an initial principal ($FV / PV = 2$), take the natural logarithm of both sides:

$$\left(1 + \frac{r}{100}\right)^N = 2 \quad \Longrightarrow \quad N \ln\!\left(1 + \frac{r}{100}\right) = \ln 2 \approx 0.693147$$

For moderate rates ($r \le 12\%$), the Mercator-Taylor expansion $\ln(1 + u) = u - \frac{1}{2}u^2 + \cdots$ with $u = r/100$ gives $N \approx \frac{69.31}{r}\left(1 + \frac{r}{200}\right)$. Franciscan friar Luca Pacioli, who first printed the rule in his monumental *Summa de arithmetica* (Venice, 1494), and Renaissance merchants across Venice and Florence adjusted the numerator from $69.3$ to $72$ (matching the exact discrete-compounding curvature around $r \approx 8\%$) because $72$ is evenly divisible by $1, 2, 3, 4, 6, 8, 9,$ and $12$ to establish the Rule of 72:

$$\text{Doubling Time (Years)} \approx \frac{72}{\text{Annual Interest Rate } r\%}$$

At $6\%$ annual return, capital doubles in approximately $72 / 6 = 12\text{ years}$; at $8\%$, in $72 / 8 = 9\text{ years}$; at $9\%$, in $72 / 9 = 8\text{ years}$. Conversely, when price inflation runs at an annual rate $\pi$ over $N$ years, the real purchasing power of uninvested cash decays exponentially according to $PV_{\text{real}} = FV \cdot (1 + \pi)^{-N}$ and cuts purchasing power in half every $72 / (100\pi)$ years.

---

## The Five-Variable Balance Law and Mortgage Amortization

### Deriving the Five-Variable TVM Balance Equation

In practice, financial contracts rarely involve a single lump sum left untouched for decades. Instead, three distinct cash components interact across $N$ compounding periods at periodic interest rate $i$: the present value $PV$ exchanged at time $t = 0$ (such as loan principal disbursed at closing or an opening investment balance), the uniform periodic payment stream $PMT$ transferred at each period $k = 1, 2, \dots, N$ (such as a periodic loan installment, lease payment, or sinking-fund contribution), and the terminal future value $FV$ remaining at the end of period $N$ ($0$ for a fully amortizing loan, a contractual balloon payoff, or an accumulated savings target). All five variables—$N, i, PV, PMT,$ and $FV$—are unified by Francis Baily's (1808) and Augustus De Morgan's (1838) principle of actuarial equivalence, which discounts every cash flow to a common reference epoch.

Taking the present epoch ($t = 0$) as the valuation fulcrum, each periodic payment $PMT$ occurring at period $k$ is discounted to $t = 0$ through multiplication by $(1 + i)^{-k}$, and the terminal balance $FV$ at period $N$ is discounted by $(1 + i)^{-N}$:

$$PV + \frac{PMT}{(1+i)^1} + \frac{PMT}{(1+i)^2} + \cdots + \frac{PMT}{(1+i)^N} + \frac{FV}{(1+i)^N} = 0$$

The central summation of $N$ discounted payments is a finite geometric series with common ratio $q = (1 + i)^{-1}$. Applying Euclid's closed-form summation identity collapses those $N$ terms into the standard actuarial Annuity Present-Value Factor ($a_{\overline{N}|i}$):

$$\sum_{k=1}^{N} (1 + i)^{-k} = \frac{1 - (1 + i)^{-N}}{i} = a_{\overline{N}|i}$$

Substituting $a_{\overline{N}|i}$ yields the Master Five-Variable Time Value of Money (`TVM`) Equation:

$$PV + PMT \left[ \frac{1 - (1 + i)^{-N}}{i} \right] + FV (1 + i)^{-N} = 0$$

Payment timing within each period modifies the annuity factor. In an Ordinary Annuity (`END` mode), standard for residential mortgages, term loans, and coupon bonds, each payment $PMT$ occurs at the end of its compounding period after one interval of interest has accrued. In an Annuity Due (`BEG` mode), standard for real-estate leases, equipment rentals, and insurance premiums, each payment occurs at the beginning of the period, so it compounds for one extra interval and multiplies the $PMT$ bracket by $(1 + i)$.

### Cash-Flow Conservation and the Sign Convention

The right-hand side of the Master TVM Equation equals zero because every financial contract conserves discounted value across time. Financial mathematics models an individual wallet or corporate treasury as a thermodynamic control volume across time, governed by a strict directional sign convention. Cash inflows entering the operator's hands, such as loan proceeds received at closing, coupon checks collected, or maturity redemptions paid out, carry a positive sign ($+$). Cash outflows leaving the operator's hands, such as periodic loan repayments, savings deposits transferred into an external account, or the purchase price paid to acquire a security, carry a negative sign ($-$).

When all inflows and outflows along the timeline are discounted to $t = 0$ at periodic rate $i$, their algebraic sum vanishes. This sign discipline makes the direction of every transaction unambiguous: when a borrower receives loan proceeds $PV > 0$ at $t = 0$, the $N$ periodic repayments must carry the opposite sign ($PMT < 0$) to reduce the remaining debt to $FV = 0$.

{{blocks:sc32_concept_tvm_cashflow|Time Value of Money (TVM) cash-flow sign conservation timeline and 30-year mortgage principal-versus-interest amortization crossover.}}

### Principal-Interest Decomposition and Amortization Crossover

For a fully amortizing level-payment loan of principal $PV > 0$ repaid across $N$ periods (`FV = 0`) at periodic interest rate $i$, solving the Master TVM Equation fixes the constant periodic payment magnitude $|PMT|$:

$$|PMT| = PV \left[ \frac{i}{1 - (1 + i)^{-N}} \right]$$

Although the total check $|PMT|$ remains constant at every period $k = 1, 2, \dots, N$, its internal allocation between interest charge $I_k$ and principal reduction $P_k$ shifts exponentially over the life of the contract. At the end of period $k - 1$, the remaining loan balance $B_{k-1}$ equals the present value of the $N - k + 1$ payments still remaining:

$$B_{k-1} = |PMT| \left[ \frac{1 - (1 + i)^{-(N - k + 1)}}{i} \right]$$

During period $k$, the lender first assesses periodic interest $I_k = i \cdot B_{k-1}$ on that outstanding balance, and only the residual portion $P_k = |PMT| - I_k$ reduces the principal:

$$I_k = |PMT| \left[ 1 - (1 + i)^{-(N - k + 1)} \right], \qquad P_k = |PMT| (1 + i)^{-(N - k + 1)}$$

These two identities govern the structural dynamics of every amortizing loan. Because $P_{k+1} / P_k = 1 + i$, the principal portion of each payment follows a geometric progression that grows exponentially at rate $i$ from the first period to the last. On long-duration loans where $N \cdot i \gg 1$, the factor $(1 + i)^{-N}$ is small, so $I_1$ consumes the overwhelming majority of the opening payments while $P_1$ retires only a small fraction of principal. The amortization crossover period $k_{\text{cross}}$ at which principal reduction $P_k$ finally overtakes interest $I_k$ occurs when $P_k = \frac{1}{2}|PMT|$, which simplifies directly to $(1 + i)^{N - k + 1} = 2$. Taking logarithms reveals that the crossover point depends only on $N$ and $i$, completely independent of the loan size $PV$:

$$k_{\text{cross}} = N + 1 - \frac{\ln 2}{\ln(1 + i)}$$

Thus, the amortization crossover always occurs exactly one Rule-of-72 doubling time prior to maturity. Furthermore, because early principal reduction $P_k$ is small, sending an unscheduled periodic principal curtailment $\Delta P$ on top of $|PMT|$ accelerates the payoff horizon from $N$ down to $N^*$, derived in closed form by inverting the annuity factor:

$$N^* = -\frac{\ln\!\left(1 - \frac{i \cdot PV}{|PMT| + \Delta P}\right)}{\ln(1 + i)}$$

Each extra dollar directed to principal in early periods bypasses all compound interest that would otherwise accrue on that dollar across the remaining $N - k$ periods of the schedule.

---

## Valuing Future Cash Streams: Bond Pricing, Net Present Value & Internal Rate of Return

### Coupon Discounting, Inverse Yield Dynamics, and Macaulay Duration

A fixed-rate bond is a standardized loan contract in which an issuer promises to pay a sequence of periodic coupon inflows $PMT = +C$ across $N$ compounding periods together with a par redemption inflow $FV = +M$ at maturity. When the market requires a periodic yield to maturity $y$ on securities of comparable credit risk, the fair purchase price $P$ on a coupon date (entered as an acquisition outflow $PV = -P$; between coupon dates, the settlement "dirty" invoice price adds accrued interest to the quoted "clean" price) is the sum of the discounted coupons and discounted par redemption:

$$P(y) = C \left[ \frac{1 - (1 + y)^{-N}}{y} \right] + M (1 + y)^{-N}$$

Because the contractual cash promises $C$ and $M$ are fixed at issuance, the market price $P(y)$ moves inversely to the prevailing yield $y$. When the market yield $y$ equals the coupon rate $c = C / M$, the bond trades at par ($P = M$); when prevailing yields rise above the coupon rate ($y > c$), the bond must trade at a discount ($P < M$) so that the capital gain $M - P$ at maturity compensates the buyer for the below-market coupons; when yields fall below the coupon rate ($y < c$), the bond trades at a premium ($P > M$).

In 1938, economist Frederick Macaulay introduced a closed-form measure of a bond's effective maturity and interest-rate sensitivity by treating the discounted cash flows $w_t = C_t (1 + y)^{-t}$ at epochs $t = 1, 2, \dots, N$ as point masses distributed along a timeline. The center-of-mass fulcrum where that timeline balances—identical in form to Archimedes' weighted centroid $\bar{t} = \frac{\sum t w_t}{\sum w_t}$—is Macaulay Duration ($D$, measured in periods, or $D_{\text{yr}} = D/m$ in years for $m$ coupons per year). Differentiating $P(y)$ with respect to $y$ and dividing $D_{\text{yr}}$ by $(1 + y/m)$ yields Modified Duration ($D^*$), the first-order elasticity linking percentage price changes to annual yield shifts $\Delta y$:

$$D = \frac{1}{P} \sum_{t=1}^{N} \frac{t \cdot C_t}{(1 + y)^t}, \qquad \frac{\Delta P}{P} \approx -D^* \cdot \Delta y = -\frac{D}{1 + y} \cdot \Delta y$$

This duration lever explains why short-dated notes with small $D^*$ exhibit minimal price volatility when central-bank rates move, whereas long-dated bonds—whose cash-flow centroid sits far out along the time axis—experience large percentage price swings for every $1\%$ shift in yield (if a bond fund has $D^* = 7.0\text{ yr}$ and market interest rates rise by $1\%$, the fund's price drops by roughly $7\%$, before second-order convexity curvature $\frac{1}{2}C(\Delta y)^2$).

### Net Present Value (`NPV`) as a Horner Polynomial and `IRR` Root-Finding

Unlike level-coupon bonds, capital projects, industrial plants, and operating businesses generate uneven cash flows $C_1, C_2, \dots, C_N$ across successive years. Discounting each cash flow at the firm's periodic cost of capital $r$ defines the present value of the stream (and, after subtracting the initial outlay $|C_0|$, the Net Present Value):

$$\text{PV}(r) = \sum_{t=1}^{N} \frac{C_t}{(1 + r)^t}, \qquad \text{NPV}(r) = C_0 + \sum_{t=1}^{N} \frac{C_t}{(1 + r)^t}$$

Letting $x = 1 + r$ represent the gross periodic discount factor, the discounted sum is a degree-$N$ polynomial in the reciprocal factor $u = 1/x$, which folds from the terminal horizon $t = N$ backward to $t = 0$ via Horner's nested recurrence:

$$\text{NPV}(x) = C_0 + \left(\cdots\left(\left(C_N \div x + C_{N-1}\right) \div x + C_{N-2}\right) \div x + \cdots + C_1\right) \div x$$

This nested polynomial representation directly governs the inverse valuation problem: given an initial investment outlay $C_0 < 0$ followed by future cash flows $C_1, \dots, C_N$, the Internal Rate of Return (`IRR`) is the critical discount rate $r^*$ at which the Net Present Value vanishes, $\text{NPV}(r^*) = 0$.

Determining `IRR`—or solving the Master TVM Equation for an unknown periodic rate `I%` (`{{key:I%}}` on `{{key:LFU1}}`)—requires finding the root of a degree-$N$ polynomial. As Niels Henrik Abel and Évariste Galois proved in the nineteenth century, no closed-form radical formula exists for general polynomial equations of degree $N \ge 5$. Moreover, as William Kahan demonstrated in his 1979 analysis of financial calculators, direct evaluation of $\frac{1 - (1 + i)^{-N}}{i}$ suffers catastrophic cancellation when $i \to 0$, requiring evaluation through $\ln(1 + i)$ and $\exp(x) - 1$ primitives during iterative root-finding:

$$a_{\overline{N}|i} = \frac{1 - \exp\!\left(-N \ln(1 + i)\right)}{i}$$

Two structural properties govern numerical root-finding on discounted cash-flow polynomials. First, `NPV` and `IRR` can rank mutually exclusive projects differently when their scales or cash-flow timings diverge: `IRR` measures the constant compounding rate earned on capital while it remains invested inside the project (whereas Modified `MIRR` explicitly compounds intermediate inflows to the horizon at the firm's external reinvestment rate before taking the $N$-th root), while `NPV` discounts every cash flow at the external opportunity cost of capital $r$.

Second, by René Descartes's 1637 Rule of Signs, a conventional investment whose cash-flow sequence changes sign only once ($C_0 < 0$ followed by $C_t \ge 0$) possesses a unique positive root $x^* = 1 + r^*$. By contrast, a project with a large terminal decommissioning or reclamation outflow ($-, +, +, -$) changes sign twice and can exhibit two distinct internal rates of return. To handle both regimes cleanly, the SC-32 combines Horner stack evaluation with Richard Brent's `{{key:SOLVE}}` root-finder and William Kahan's financial convergence safeguards {{cite:kahan1979,brent1973}} across `N`, `I%`, `PV`, `PMT`, `FV`, and `END`/`BEG`.

---

## Percentages, Mortgage Amortization & Discounted Cash Flows

Because a unit of capital today compounds at periodic rate $i$ into $(1 + i)^N$ units $N$ periods hence, every commercial invoice, amortizing loan, bond, or capital budget is governed by discounted cash-flow conservation. On the StackCalc SC-32, financial computation relies on a two-register discipline: Register `Y` holds the baseline principal or subtotal untouched while Register `X` evaluates `{{key:%}}` or `{{key:%CHG}}`, and the five-variable `{{key:TVM}}` softkey bar (`{{key:N}}`, `{{key:I%}}`, `{{key:PV}}`, `{{key:PMT}}`, `{{key:FV}}`) reads known inputs from and writes solved roots directly to Register `X` without disturbing the upper stack.

Pressing `{{key:TVM}}` (Left Shift `{{key:↰}}` above `{{key:x∥y}}`) maps the five financial variables plus `END/BEG` across the six top softkeys (`{{key:LFU0}}`–`{{key:LFU5}}`), where two operational invariants govern every entry. Under the wallet reference frame, cash flowing into your pocket is entered as positive (`+`), whereas cash flowing out of your pocket is negated with `{{key:+/-}}` (`-`). To solve for an unknown quantity from four known parameters, keying a number and tapping a softkey stores that parameter from Register `X`, while tapping a fifth softkey without prior numeric entry solves for that unknown variable.

{{res:sc32_tvm_pmt:screenshot|The SC-32 transflective display executing multi-variable financial calculations with continuous stack preservation.}}

### Base-Preserving Percentages (`%`), Chain Discounts & Gross Margin Pricing

To format currency outputs rounded to cents while retaining full 64-bit internal precision, set the display mode to two decimal places (`{{key:FIX}} 2`) via `{{key:DISP}}` $\to$ `{{key:FIX}}` $\to$ `2` {{cite:hp15c1982}}. On the StackCalc SC-32, the Percentage Function (`{{key:%}}`) adheres strictly to William Kahan's non-destructive specification {{cite:kahan1979}}:

$$\text{Calculation: } \quad X \leftarrow \frac{Y \times X}{100}, \quad Y \leftarrow Y \text{ (Preserved)}, \quad \text{Lift} \leftarrow \text{TRUE}$$

Because `{{key:%}}` leaves your original base amount intact in Register $Y$ while placing the computed dollar adjustment directly beneath it in Register $X$ (with Registers $Z$ and $T$ at zero), everyday commercial calculations flow in two natural moves:
* **Consulting Invoice Tax (`$150.00 + 8.25%`):** To add $8.25\%$ sales tax to a $\$150.00$ invoice, keying `{{res:sc32_11_financial_tvm_seq_06:keys}}` places the $\$12.38$ tax in Register $X$ while holding $\$150.00$ in Register $Y$, so pressing `{{key:+}}` completes the $\$162.38$ total in one stroke. Likewise, running `{{res:sc32_11_financial_tvm_seq_44:keys}}` on a $\$100.00$ baseline leaves the exact dollar adjustment (`{{res:sc32_11_financial_tvm_seq_44:value}}`) in Register $X$ while freezing $100.00$ in Register $Y$.
* **Enterprise Server Purchase Order (`$18,450.00 + 8.25%`):** On an enterprise server order subtotaling $\$18,450.00$ with $8.25\%$ state sales tax (`{{key:FIX}} 2`), keying `{{res:sc32_11_financial_tvm_seq_07:keys}}` stages $\$18,450.00$ in Register $Y$, computes the $\$1,522.13$ sales tax in Register $X$, and sums the two registers to `$19,972.13` without retyping the base.
* **Single Volume Discount (`$85,000.00 - 17.5%`):** On an $\$85,000.00$ software license carrying a $17.5\%$ volume discount, `{{res:sc32_11_financial_tvm_seq_08:keys}}` places the $\$14,875.00$ concession in Register $X$ directly beneath the $\$85,000.00$ list price in Register $Y$, so subtracting settles the net invoice payable at `$70,125.00`.
* **Stacked Chain Markdowns (`$280.00 - 30% - 15%`):** When a $30\%$ seasonal sale is followed by an extra $15\%$ VIP coupon on a $\$280.00$ field jacket, evaluating `{{res:sc32_11_financial_tvm_seq_27:keys}}` and subtracting the initial $\$84.00$ markdown leaves the intermediate $\$196.00$ sale price in Register $X$; applying the second $15\%$ discount ($\$29.40$) via `15 {{key:%}} {{key:-}}` then lands at $\$166.60$, an effective $40.5\%$ reduction rather than $45\%$.
* **Shared vs. Itemized Bill Splitting:** When $8$ diners split a $\$480.00$ restaurant tab where $3$ guests shared $\$96.00$ of wine while all $8$ split the food equally, deducting the wine tab via `{{res:sc32_11_financial_tvm_seq_25:keys}}` isolates the $\$384.00$ food subtotal and divides by $8$ to establish the $\$48.00$ per-person food share in Register $X$; chaining `{{res:sc32_11_financial_tvm_seq_26:keys}}` then stages the $\$32.00$ per-drinker wine share in Register $X$ beneath $\$48.00$ in $Y$ and adds them to finish the wine-drinker total ($\$80.00$).

By contrast, comparing the Markup Trap against true Gross Margin Pricing on a product with landed cost $C = \$60.00$ and target $40.0\%$ gross margin activates all four stack registers so you can hold the flawed markup price in the upper registers while computing the true margin price below: adding a $40\%$ markup onto $\$60.00$ (`{{res:sc32_11_exec_markup_trap:keys}}` $\rightarrow$ `${{res:sc32_11_exec_markup_trap:value}}`) yields only $\$24 / \$84 = 28.57\%$ margin, whereas dividing cost by the margin complement $\text{Price} = \frac{\text{Cost}}{1 - \text{Margin}}$ via `{{res:sc32_11_exec_gross_margin_price:keys}}` resolves the true retail price `${{res:sc32_11_exec_gross_margin_price:value}}`:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `60 {{key:ENTER}} 40 {{key:%}}` | 0.00 | 0.00 | 60.00 | 24.00 | 40% markup on \$60.00 cost: \$24.00 |
| `{{key:+}}` | 0.00 | 0.00 | 0.00 | 84.00 | Flawed markup price: \$84.00 (28.57% margin) |
| `60 {{key:ENTER}} 1 {{key:ENTER}}` | 84.00 | 60.00 | 1.00 | 1.00 | True margin pricing: stage cost \$60 in $Z$ and 1.00 in $Y$ |
| `.40 {{key:-}}` | 84.00 | 84.00 | 60.00 | 0.60 | 1 - 0.40 = 0.60 margin complement; \$60.00 drops to $Y$ |
| `{{key:÷}}` | 84.00 | 84.00 | 84.00 | 100.00 | True gross margin retail price: \$100.00 |

### Percent Change (`%CHG`), Cross-Metric Elasticity, CAGR & Inflation

The Percent Change Function (`{{key:%CHG}}`) is executed via Right Shift `{{key:↱}}` followed by `{{key:%CHG}}` using the chronological order Old Value `{{key:ENTER}}` New Value `{{key:%CHG}}`, preserving the Old Value in Register $Y$ and the New Value in `LASTX`.

In a quarterly SaaS operating review where Annual Recurring Revenue (`ARR`) grew from $\$12.0\text{M}$ to $\$15.6\text{M}$, `{{res:sc32_11_financial_tvm_seq_10:keys}}` returns $+30.00\%$. Over the same period, Customer Acquisition Cost (`CAC`) expanded from $\$2.4\text{M}$ to $\$2.88\text{M}$, where `{{res:sc32_11_financial_tvm_seq_11:keys}}` returns $+20.00\%$. Dropping the old baseline out of the way via `{{key:x⇄y}} {{key:R↓}}` aligns `ARR` growth in Register $Y$ ($30.00$) and `CAC` growth in Register $X$ ($20.00$) side-by-side on the stack. Pressing `{{key:-}}` then gives the `+10.00%` growth spread, while `{{res:sc32_11_financial_tvm_seq_12:keys}}` delivers the `{{res:sc32_11_financial_tvm_seq_12:value}}` bang-for-the-buck growth elasticity multiplier ($1.50\times$ revenue growth per $1\times$ marketing spend growth):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `12 {{key:ENTER}} 15.6 {{key:%CHG}}` | 0.00 | 0.00 | 12.00 | 30.00 | ARR growth $+30.00\%$ in X; baseline $12.00$ in Y |
| `2.4 {{key:ENTER}} 2.88 {{key:%CHG}}` | 12.00 | 30.00 | 2.40 | 20.00 | CAC growth $+20.00\%$ in X; ARR growth lifts to Z |
| `{{key:x⇄y}}` | 12.00 | 30.00 | 20.00 | 2.40 | Swap CAC baseline $2.40$ into X |
| `{{key:R↓}}` | 2.40 | 12.00 | 30.00 | 20.00 | Roll stack down to align $30.00\%$ in Y and $20.00\%$ in X |
| `{{key:-}}` | 2.40 | 2.40 | 12.00 | 10.00 | ARR vs. CAC growth spread $+10.00$ percentage points |

To compute the $n$-year Compound Annual Growth Rate (`CAGR`), $\text{CAGR} = (FV / PV)^{1/n} - 1$, the entire inside-out chain executes across Registers $X$ and $Y$ alone while Registers $Z$ and $T$ remain at zero. For a venture investment that expands from $PV = \$14.0\text{M}$ to $FV = \$88.5\text{M}$ over $n = 5\text{ years}$, keying `{{res:sc32_11_financial_tvm_seq_13:keys}}` forms the terminal wealth multiple $88.5 / 14.0 = 6.3214\times$ in Register $X$, raises it to the reciprocal power $1/5 = 0.20$ via `{{key:1/x}}` and `{{key:yˣ}}` to obtain the annualized growth factor $1.4460$, and subtracts unity before scaling by $100$ to reveal `{{res:sc32_11_financial_tvm_seq_13:value}}` ($44.60\%\text{/yr}$; by the same five-year root, an equity share rising from $\$4.20$ to $\$11.45$ compounds at $(11.45 / 4.20)^{1/5} - 1 = 22.21\%\text{/yr}$).

Conversely, deflating $\$100,000$ of uninvested cash by 20 years of $3.2\%$ annual CPI inflation ($PV = 100,000 / (1.032)^{20}$) via `{{res:sc32_11_financial_tvm_seq_03:keys}}` reveals that real purchasing power erodes to `{{res:sc32_11_financial_tvm_seq_03:value}}` ($\$53,260.60$). By the same exponential logic, translating a nominal $18.5\%$ APR compounded monthly ($m = 12$) into its true Effective Annual Rate, $\text{EAR} = (1 + 0.185/12)^{12} - 1$, needs `12` typed only once when you recover the compounding frequency from `{{key:LASTX}}` right after dividing $0.185 / 12$, which compounds the monthly factor $1.015417^{12} - 1$ to an effective annual yield of $20.15\%$.

### The Five-Variable `TVM` Engine: Mortgages, Amortization & Balloon Notes

The onboard Five-Variable Time Value of Money (`{{key:TVM}}`) Engine is accessed via Left Shift `{{key:↰}}` above `{{key:x∥y}}` (Row 7, Column 3):

| TVM Variable | LFU Softkey | Actuarial Description | Computational Units |
| :---: | :---: | :--- | :--- |
| **$N$** | `{{key:N}}` (`{{key:LFU0}}`) | Total number of compounding periods | Integer or fractional periods |
| **$I\%$** | `{{key:I%}}` (`{{key:LFU1}}`) | Periodic interest rate per compounding period ($i\%$) | Percent per period (e.g. `6.5` for 6.5%/yr or `6.75/12 = 0.5625` for monthly) |
| **$PV$** | `{{key:PV}}` (`{{key:LFU2}}`) | Present value (initial loan principal or investment) | Currency ($) |
| **$PMT$** | `{{key:PMT}}` (`{{key:LFU3}}`) | Periodic annuity payment amount | Currency ($ per period) |
| **$FV$** | `{{key:FV}}` (`{{key:LFU4}}`) | Future value (final balloon balance or accumulated savings) | Currency ($) |
| **Mode** | `END/BEG` (`{{key:LFU5}}`) | Payment timing within each period | `END` (Ordinary Annuity) or `BEG` (Annuity Due) |

Four hardware state conventions govern the `{{key:TVM}}` softkey interface:
1. **Store versus Solve Dispatch:** Tapping any `{{key:TVM}}` softkey immediately after numeric entry or an arithmetic operation stores Register $X$ into that financial register; tapping a softkey immediately after another `{{key:TVM}}` softkey solves for that unknown variable into Register $X$.
2. **Periodic Interest Rate Scaling:** Softkey `{{key:I%}}` (`{{key:LFU1}}`) stores the periodic interest rate $i\%$ per compounding interval. For a monthly contract quoted at nominal annual rate $\text{APR}$, divide by $12$ (`6.75 {{key:ENTER}} 12 {{key:÷}}` $\to 0.5625\%$) before storing.
3. **Payment Timing Mode (`END/BEG`):** Softkey `{{key:LFU5}}` toggles between Ordinary Annuity (`END`, end-of-period cash flows) and Annuity Due (`BEG`, beginning-of-period cash flows).
4. **Register Persistence Across Scenarios:** All five `{{key:TVM}}` registers retain their stored parameters across calculations for sensitivity analysis; explicitly zero any unused variable (such as `0 {{key:FV}}` or `{{key:CLEAR}}` $\to$ `{{key:CLVARS}}` on `{{key:LFU1}}`) before starting an unrelated contract.

Applying this five-variable sequence to a 30-year fixed residential mortgage of $PV = +\$350,000.00$ at $6.75\%$ APR establishes the monthly payment and lifetime interest burden:
1. **Total Periods (`N = 360`):** Thirty years of monthly payments span $30 \times 12 = 360$ compounding periods $\to$ `360 {{key:N}}`.
2. **Monthly Periodic Rate (`I% = 6.75 / 12 = 0.5625`):** Divide the $6.75\%$ annual rate by $12$ months to get $0.5625\%$ per month $\to$ `.5625 {{key:I%}}`.
3. **Present Value Loan Inflow (`PV = +350000`):** At closing, the lender wires $+\$350,000.00$ into your transaction $\to$ `350000 {{key:PV}}`.
4. **Target Future Payoff Balance (`FV = 0`):** A fully amortizing mortgage pays the balance down to zero at Month 360 $\to$ `0 {{key:FV}}`.
5. **Solve for the Unknown Monthly Outflow (`PMT`):** With four variables stored, tap `{{key:PMT}}` without typing a number to solve for the monthly check ($-\$2,270.09$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `360 {{key:N}}` | 0.00 | 0.00 | 0.00 | 360.00 | Store term $N = 360\text{ months}$ |
| `.5625 {{key:I%}}` | 0.00 | 0.00 | 360.00 | 0.56 | Store monthly periodic rate $i = 0.5625\%$ |
| `350000 {{key:PV}}` | 0.00 | 360.00 | 0.56 | 350000.00 | Store loan principal inflow $PV = +\$350,000.00$ |
| `0 {{key:FV}}` | 360.00 | 0.56 | 350000.00 | 0.00 | Zero unused balloon register $FV = \$0.00$ before solving |
| `{{key:PMT}}` | 360.00 | 0.56 | 350000.00 | -2270.09 | Solve monthly mortgage outflow $PMT = -\$2,270.09$ |
| `360 {{key:×}}` | 0.56 | 0.56 | 350000.00 | -817233.60 | Total 30-year payments $-\$817,233.60$ |
| `350000 {{key:+}}` | 0.56 | 0.56 | 350000.00 | -467233.60 | Total lifetime interest paid $-\$467,233.60$ |

Dissecting the Month 1 interest/principal split requires only Registers $X$ and $Y$ while Registers $Z$ and $T$ stay at zero (noting that Truth-in-Lending cent-rounding from $-\$2,270.0934$ adjusts the Month 360 payoff by a few cents): in Month 1, the bank assesses one periodic rate ($i = 0.0675 / 12 = 0.005625$) against the $\$350,000.00$ balance. Keying `350000 {{key:ENTER}} 0.005625 {{key:×}}` computes Month 1 interest $I_1 = \$1,968.75$ in Register $X$—consuming $86.7\%$ of the $\$2,270.09$ check before a single cent touches the debt. Deducting that interest via `2270.09 {{key:x⇄y}} {{key:-}}` isolates the Month 1 principal reduction $P_1 = \$301.34$ ($13.3\%$), and subtracting $P_1$ via `350000 {{key:x⇄y}} {{key:-}}` leaves $\$349,698.66$ owed after Month 1. By the crossover formula $k_{\text{cross}} = 361 - \frac{\ln 2}{\ln(1.005625)} = 237.43$, Month 238 is the first integer month where principal overtakes interest:

| Month | Remaining Balance | Monthly Payment | Interest ($I_k$) | Principal ($P_k$) | Equity % | Financial Milestone |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **1** | $\$349,698.66$ | $\$2,270.09$ | $\$1,968.75$ | $\$301.34$ | $0.09\%$ | $86.7\%$ of check goes straight to interest |
| **Month 238** *(Principal Crossover)* | $\$199,998.44$ | $\$2,270.09$ | $\$1,131.40$ | $\$1,138.70$ | $42.86\%$ | **Amortization Crossover:** $P_k$ finally overtakes $I_k$ |
| **360** | $\$0.00$ | $\$2,270.09$ | $\$12.70$ | $\$2,257.39$ | $100.00\%$ | Final payoff; $\$467,233.60$ total lifetime interest |

Because the `TVM` registers retain your loan parameters, testing an extra $\$250.00/\text{month}$ principal curtailment means storing the augmented outflow $PMT = -\$2,520.09/\text{mo}$ and tapping `{{key:N}}` (`{{res:sc32_11_realtor_extra_principal_months:keys}}`), which compresses the repayment horizon to `{{res:sc32_11_realtor_extra_principal_months:value}}` months ($22.6\text{ years}$, saving $89\text{ payments}$ and $\$134,474.66$ in interest):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
|:---|:---|:---|:---|:---|:---|
| `6.75 {{key:ENTER}} 12 {{key:÷}} {{key:I%}}` | 0.00 | 0.00 | 0.00 | 0.56 | Monthly rate i = 0.5625% |
| `350000 {{key:PV}} 0 {{key:FV}}` | 0.00 | 0.56 | 350000.00 | 0.00 | Store PV = \$350,000.00 and zero FV = \$0.00 before solving |
| `2520.09 {{key:+/-}} {{key:PMT}}` | 0.56 | 350000.00 | 0.00 | -2520.09 | Augmented payment: -\$2,520.09/mo |
| `{{key:N}}` | 0.56 | 350000.00 | 0.00 | 270.93 | Accelerated repayment: 270.93 months |

Next, take a commercial 5-year balloon note lending $\$500,000$ at $7.5\%$ APR ($i = 0.625\%/\text{month}$), amortized on a 25-year schedule ($N = 300\text{ months}$) with a balloon maturity at Month $60$. Because the monthly check is sized as if the loan ran for 300 months to $FV = 0$, first solve for `{{key:PMT}}` at $N = 300$ via `{{res:sc32_11_financial_tvm_seq_17:keys}}` $\rightarrow$ `{{res:sc32_11_financial_tvm_seq_17:value}}`, and then shorten the horizon to `60 {{key:N}}` and tap `{{key:FV}}` to read off the remaining principal payoff due at Month 60 (`-$458,662.75`):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `300 {{key:N}}` | 0.00 | 0.00 | 0.00 | 300.00 | Store 25-year amortization schedule $N = 300\text{ months}$ |
| `.625 {{key:I%}}` | 0.00 | 0.00 | 300.00 | 0.63 | Store monthly periodic rate $7.5\% / 12 = 0.625\%$ |
| `500000 {{key:PV}}` | 0.00 | 300.00 | 0.63 | 500000.00 | Store commercial loan principal $PV = +\$500,000.00$ |
| `0 {{key:FV}}` | 300.00 | 0.63 | 500000.00 | 0.00 | Target $FV = 0$ over full 300-month amortization |
| `{{key:PMT}}` | 300.00 | 0.63 | 500000.00 | -3694.96 | Monthly payment $PMT = -\$3,694.96$ |
| `60 {{key:N}}` | 0.63 | 500000.00 | -3694.96 | 60.00 | Set horizon to 5-year maturity ($N = 60\text{ months}$) |
| `{{key:FV}}` | 0.63 | 500000.00 | -3694.96 | -458662.75 | Remaining 5-year balloon payoff $FV = -\$458,662.75$ |

Every `{{key:TVM}}` calculation can also be cross-checked from the closed-form annuity identities on the 4-level stack:

| Financial Instrument | Analytical Closed-Form Formula | Native RPN Inside-Out Recipe |
| :--- | :--- | :--- |
| **Ordinary Annuity PV** | $PV = PMT \left[ \frac{1 - (1 + i)^{-N}}{i} \right]$ | `1 ENTER i + N +/- yˣ 1 x⇄y - i ÷ PMT ×` |
| **Ordinary Annuity FV** | $FV = PMT \left[ \frac{(1 + i)^N - 1}{i} \right]$ | `1 ENTER i + N yˣ 1 - i ÷ PMT ×` |
| **Amortization Payment** | $PMT = PV \left[ \frac{i}{1 - (1 + i)^{-N}} \right]$ | `1 ENTER i + N +/- yˣ 1 x⇄y - i x⇄y ÷ PV ×` |
| **Sinking Fund Payment** | $PMT = FV \left[ \frac{i}{(1 + i)^N - 1} \right]$ | `1 ENTER i + N yˣ 1 - i x⇄y ÷ FV ×` |

### Bond Yield to Maturity (`YTM`), Duration, `NPV`, `IRR` & Portfolio Risk

For a 10-year corporate bond ($N = 20$ semi-annual periods) with par value $FV = +\$1,000.00$ and a $5.5\%$ annual coupon paid semi-annually ($PMT = +\$27.50$) purchased at $PV = -\$925.00$, storing $N, PV, PMT, FV$ and pressing `{{key:I%}}` finds the semi-annual yield $3.2666\%$, which doubles (`2 {{key:×}}`) to the Wall Street Bond-Equivalent Yield $\text{BEY} = 2i = 6.53\%$ (or compounds via $(1 + i)^2 - 1 = 6.64\%$ as an Effective Annual Yield $\text{EAY}$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `20 {{key:N}}` | 0.00 | 0.00 | 0.00 | 20.00 | Store $N = 20$ semi-annual coupon periods |
| `925 {{key:+/-}} {{key:PV}}` | 0.00 | 0.00 | 20.00 | -925.00 | Store bond purchase price outflow $PV = -\$925.00$ |
| `27.50 {{key:PMT}}` | 0.00 | 20.00 | -925.00 | 27.50 | Store semi-annual coupon inflow $PMT = +\$27.50$ |
| `1000 {{key:FV}}` | 20.00 | -925.00 | 27.50 | 1000.00 | Store maturity par redemption $FV = +\$1,000.00$ |
| `{{key:I%}}` | 20.00 | -925.00 | 27.50 | 3.27 | Solve semi-annual periodic yield $i = 3.2666\%$ |
| `2 {{key:×}}` | -925.00 | -925.00 | 27.50 | 6.53 | Annualized bond-equivalent $\text{YTM} = 6.53\%$ |

To evaluate Macaulay Duration $D$ and Modified Duration $D^*$ for a 3-year $8.0\%$ annual coupon bond trading at par of $\$1,000.00$ with yield $y = 8.0\%$, accumulate the time-weighted present values $\sum t \cdot C_t / (1.08)^t$ and divide by price and $(1 + y)$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `80 {{key:ENTER}} 1.08 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 74.0741 | Year 1 weighted PV: $1 \times 80 / 1.08 = \$74.0741$ |
| `80 {{key:ENTER}} 1.08 {{key:ENTER}} 2 {{key:yˣ}} {{key:÷}} 2 {{key:×}} {{key:+}}` | 74.07 | 74.07 | 74.07 | 211.2483 | Add Year 2 weighted PV ($2 \times 80 / 1.08^2 = \$137.1742$) |
| `1080 {{key:ENTER}} 1.08 {{key:ENTER}} 3 {{key:yˣ}} {{key:÷}} 3 {{key:×}} {{key:+}}` | 211.25 | 211.25 | 211.25 | 2783.2648 | Add Year 3 weighted PV ($3 \times 1080 / 1.08^3 = \$2,572.02$) |
| `1000 {{key:÷}}` | 211.25 | 211.25 | 211.25 | 2.7833 | Divide by $\$1,000$ price for Macaulay Duration $D = 2.7833\text{ yr}$ |
| `1.08 {{key:÷}}` | 211.25 | 211.25 | 211.25 | 2.5771 | Divide by $1.08$ for Modified Duration $D^* = 2.5771\text{ yr}$ |

To discount a 4-year corporate free-cash-flow stream of $\$10\text{M}, \$12\text{M}, \$15\text{M},$ and $\$234\text{M}$ at a $10\%$ cost of capital ($\text{Enterprise Value} = \frac{10}{1.1} + \frac{12}{1.1^2} + \frac{15}{1.1^3} + \frac{234}{1.1^4}$), running `{{res:sc32_11_financial_tvm_seq_18:keys}}` accumulates the four present values to `{{res:sc32_11_financial_tvm_seq_18:value}}` ($\$190.10\text{M}$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `10 {{key:ENTER}} 1.1 {{key:÷}}` | 0.00 | 0.00 | 0.00 | 9.09 | Year 1 discounted FCF: $10 / 1.10 = \$9.09\text{M}$ |
| `12 {{key:ENTER}} 1.1 {{key:x²}} {{key:÷}}` | 0.00 | 0.00 | 9.09 | 9.92 | Year 2 discounted FCF: $12 / 1.10^2 = \$9.92\text{M}$ |
| `{{key:+}}` | 0.00 | 0.00 | 0.00 | 19.01 | Cumulative PV through Year 2: $\$19.01\text{M}$ |
| `15 {{key:ENTER}} 1.1 {{key:ENTER}} 3 {{key:yˣ}} {{key:÷}}` | 19.01 | 19.01 | 19.01 | 11.27 | Year 3 discounted FCF: $15 / 1.10^3 = \$11.27\text{M}$ |
| `{{key:+}}` | 19.01 | 19.01 | 19.01 | 30.28 | Cumulative PV through Year 3: $\$30.28\text{M}$ |
| `234 {{key:ENTER}} 1.1 {{key:ENTER}} 4 {{key:yˣ}} {{key:÷}}` | 30.28 | 30.28 | 30.28 | 159.83 | Year 4 discounted FCF + terminal value: $\$159.83\text{M}$ |
| `{{key:+}}` | 30.28 | 30.28 | 30.28 | 190.10 | Total Enterprise Value $\text{PV} = \$190.10\text{M}$ |

*(Horner Nested Discounting via Register $T$: Pre-filling the stack with `1.1 {{key:ENTER}} {{key:ENTER}} {{key:ENTER}}` and alternating `{{key:x⇄y}} {{key:÷}}` with each cash-flow addition from Year 4 ($234$) down to Year 1 ($10$) evaluates $\$190.10\text{M}$ with `1.1` typed only once and zero `{{key:yˣ}}` exponentiations.)*

To solve for the Internal Rate of Return (`IRR`) of an upfront outlay $C_0 = -\$100,000$ returning $C_1 = \$30,000$, $C_2 = \$40,000$, and $C_3 = \$50,000$, store the Net Present Value polynomial $((50000 / X + 40000) / X + 30000) / X - 100000$ in `{{key:EQN}}` mode using Horner RPN tokens `50000 X ÷ 40000 + X ÷ 30000 + X ÷ 100000 -`, where $X = 1 + r$ is the gross annual discount factor. Because Richard Brent's root-finder evaluates the stored equation internally, passing a two-guess bracket `1.0 {{key:ENTER}} 1.2` (or seeding `1.1 {{key:STO}} X`) and invoking `{{key:SOLVE}}` pushes the converged zero-NPV root $X = 1.088963$ into Register $X$ (lifting the prior contents of Register $X$ into $Y$ and preserving the upper stack in $Z$ and $T$). Subtracting unity and multiplying by $100$ then extracts the project's exact internal rate of return, $\text{IRR} = 8.90\%/\text{yr}$ ($8.8963\%$).

Finally, two classic metrics quantify risk-adjusted return and position sizing on the stack. William Sharpe's Ratio $(R_p - R_f)/\sigma_p$ measures the excess return earned above a risk-free Treasury bill per unit of volatility: for $R_p = 18.5\%$ against $R_f = 4.5\%$ with volatility $\sigma_p = 11.2\%$, `{{res:sc32_11_trader_sharpe_ratio:keys}}` yields `{{res:sc32_11_trader_sharpe_ratio:value}}` ($\frac{18.5 - 4.5}{11.2} = 1.25$). John Kelly's 1956 Criterion $f^* = \frac{bp - q}{b} = p - \frac{1-p}{b}$ determines the fraction of capital to wager on a favorable repeat bet to maximize long-run logarithmic growth without risking ruin: for win probability $p = 0.56$ ($q = 0.44$) and odds $b = 1.50$, `{{res:sc32_11_trader_kelly_criterion:keys}}` yields `{{res:sc32_11_trader_kelly_criterion:value}}` ($26.67\%$, with `{{key:LASTX}}` recalling $0.56$; in practice, portfolio managers often deploy "Half-Kelly" $\frac{1}{2}f^* \approx 13.3\%$ to halve drawdown volatility while retaining three-quarters of the compound growth rate).
