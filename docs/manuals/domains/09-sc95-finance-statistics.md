---
title: "SC-95 Quantitative Finance, Actuarial Science & Six Sigma Handbook"
description: "An applied guide to the William Kahan 5-key TVM system, discounted cash flows (NPV/IRR), and Six Sigma process capability on the StackCalc 95."
---

# SC-95 Quantitative Finance, Actuarial Science & Six Sigma Handbook

> **Who this is for:** Anyone who wants to understand the mathematics of capital, debt, and quality: how financial analysts value real estate and corporate acquisitions in their heads, and how industrial engineers use statistics to prevent factory defects.

---

## 1. The Cost of Tomorrow: Time, Uncertainty, and Capital

Here is a question with a seemingly obvious answer:

> *Would you rather have $\$10{,}000$ in cash handed to you today, or $\$10{,}000$ promised to you ten years from today?*

Everyone instinctively chooses the money today. But why?

Even if the future promise is $100\%$ guaranteed by a government, money today is fundamentally more valuable than money in the future for two mathematical reasons:
1. **Opportunity Cost:** If you have the $\$10{,}000$ today, you can invest it in a business or bank account earning compound interest. Over ten years at $7\%$ annual return, that $\$10{,}000$ doubles into almost $\$20{,}000$.
2. **Inflation:** Over a decade, the rising price of goods erodes purchasing power; ten years from now, $\$10{,}000$ buys substantially fewer groceries or gallons of fuel.

The mathematics of finance begins with this single realization: **cash flows occurring at different points in time cannot be added together.** A dollar in Year 10 is not the same currency as a dollar in Year 0. To compare them, you must translate future dollars backward into present dollars through **discounting**.

In corporate boardrooms, real estate acquisitions, and industrial factories, financial and quality decisions are made under severe time pressure:
- What monthly payment amortizes a $\$450{,}000$ commercial mortgage at $6.5\%$ interest?
- If a solar panel array costs $\$80{,}000$ to install and saves $\$12{,}000$ a year for a decade, what is its true Internal Rate of Return ($IRR$)?
- On an automotive stamping line producing ten thousand engine valves an hour, is the machinery capable of meeting tolerance limits without generating costly defective scrap?

In 1981, Hewlett-Packard introduced the **HP-12C**, designed with guidance from Turing Award winner Prof. William Kahan. It became the most enduring financial calculator in history, an icon carried into trading pits and boardrooms for decades.

The **StackCalc 95 (SC-95)** preserves this gold-standard financial workflow while fusing it with modern Six Sigma process capability indices ($C_p, C_{pk}$) and the complete continuous probability distribution suite of the statistical language **R** (`pnorm`, `qnorm`, `pt`, `qt`) directly within a 4-level RPN stack.

### Why Not Just Use an Excel Spreadsheet?

- **The Negotiation and Boardroom Reality:** In a high-stakes commercial lending negotiation or corporate acquisition review, pulling up a laptop and fumbling through a messy spreadsheet with thirty nested tabs and broken circular references projects hesitation. A CFO or analyst who can verify an internal rate of return, bond yield to maturity, or balloon payment in six tactile clicks commands the room with authoritative confidence.
- **Strict Proctored Professional Exams:** The Chartered Financial Analyst (CFA) Institute, Certified Financial Planner (CFP) Board, and Society of Actuaries (SOA) enforce the strictest testing security in the academic world: laptops, tablets, smartphones, and graphing tools are completely prohibited from exam halls. Candidates must master a dedicated, non-communicating financial calculator.
- **Factory Floor Mobility:** An ASQ Six Sigma Black Belt auditing a vibrating manufacturing stamping floor cannot carry a laptop through oily walkways. One touch on `[CPK]` on the SC-95 immediately reports process capability and centering offsets right at the machine.

---

## 2. Core Concepts: How Financial Analysts and Quality Engineers Think

### Concept 1: The 5-Key Time Value of Money (TVM) Engine

The foundation of all mortgages, car loans, leases, retirement accounts, and bond valuations rests on a single mathematical relationship connecting five fundamental variables:

$$PV \cdot (1 + i)^N + PMT \cdot \left[\frac{(1 + i)^N - 1}{i}\right] \cdot (1 + i \cdot S) + FV = 0$$

- **$N$:** Total number of payment periods (e.g. 360 months for a 30-year mortgage).
- **$i$:** Interest rate per compounding period (e.g. $6.0\%$ annual rate compounded monthly $\implies i = 6.0 / 12 = 0.50\%$).
- **$PV$:** Present Value (the lump-sum cash amount today).
- **$PMT$:** Periodic Payment (the recurring amount paid each period).
- **$FV$:** Future Value (the final balloon balance at the end).
- **$S$:** Timing switch ($0$ for `END` of period, $1$ for `BEGIN` of period).

This equation is a five-way balance. If you know any four of the variables, the SC-95's TVM engine solves for the fifth unknown variable using Brent's root-finding algorithm.

#### The Cash-Flow Sign Convention (Money In vs. Money Out)
Why does William Kahan's TVM system require one variable to be negative?

Because **money cannot be created out of thin air**:
- **Cash received by you is POSITIVE ($+$).**
- **Cash paid out by you is NEGATIVE ($-$).**

If a bank lends you $\$300{,}000$ to buy a home, that cash is paid to you today: **$PV = +300{,}000$**. Every month, when you write a mortgage check that leaves your bank account, that payment is an outflow: **$PMT = -1{,}896.20$**.

If you treat both as positive numbers, compound interest formulas collapse into nonsensical negative interest rates! Enforcing the sign convention reflects the true physics of accounting.

### Concept 2: Discounted Cash Flows (NPV & IRR)

In corporate finance, companies invest money today to earn unpredictable streams of cash in the future.

#### Net Present Value (NPV)
To find out if a project is worth doing, you discount every future cash flow ($CF_t$) back to the present day using the company's required cost of capital rate ($r$):

$$NPV = CF_0 + \frac{CF_1}{(1+r)^1} + \frac{CF_2}{(1+r)^2} + \dots + \frac{CF_k}{(1+r)^k}$$

- If **$NPV > 0$**, the investment generates more return than the cost of capital: **Do the project!**
- If **$NPV < 0$**, the project destroys shareholder value: **Reject it!**

#### Internal Rate of Return (IRR)
The **Internal Rate of Return ($IRR$)** is the exact annual interest rate at which $NPV$ equals zero. It tells you the exact break-even yield of the project.

### Concept 3: Taming the Bell Curve (Six Sigma $C_{pk}$)

In industrial manufacturing, parts coming off an assembly line are never 100% identical. Natural vibrations, tool wear, and temperature fluctuations cause dimensions to vary in a Gaussian "bell curve" distribution with an average ($\mu$) and standard deviation ($\sigma$).

Engineering blueprints define two boundary lines:
- **Lower Specification Limit ($LSL$)**
- **Upper Specification Limit ($USL$)**

Any part whose dimension falls outside these limits is defective scrap.

How do engineers evaluate whether a machine is capable of consistently meeting tolerances?

```
      LSL                         Target                        USL
       |                            |                            |
       |                   *--*     |                            |
       |                *        *  |                            |
       |              *            *|                            |
       |            *               |*                           |
       |          *                 |  *                         |
    ---+--------*-------------------+----*-----------------------+---
```

They use two **Process Capability Indices**:

#### 1. Process Potential ($C_p$)
Measures the pure width of the process spread ($6\sigma$) relative to the allowable tolerance band:

$$C_p = \frac{USL - LSL}{6\sigma}$$

If $C_p = 1.0$, the process width exactly equals the tolerance band. If $C_p > 1.33$, the process is capable of four-sigma or higher quality.

#### 2. Process Capability Index ($C_{pk}$)
What if the process is narrow, but its center has drifted toward one of the edges? $C_p$ cannot detect this drift, but **$C_{pk}$** measures the distance from the average to the nearest specification limit:

$$C_{pk} = \min\left(\frac{USL - \mu}{3\sigma}, \frac{\mu - LSL}{3\sigma}\right)$$

In modern manufacturing:
- **$C_{pk} < 1.0$:** The process is actively producing defects.
- **$C_{pk} = 1.33$:** Industrial standard ($4\sigma$, fewer than $63$ defects per million parts).
- **$C_{pk} \ge 2.0$:** World-Class Six Sigma ($6\sigma$, fewer than $3.4$ defects per million parts!).

---

## 3. Real-World Field Walkthroughs

### Field Case 1: 30-Year Mortgage Payment & Extra Principal (`Bogleheads`)

A homebuyer borrows $\$400{,}000$ on a 30-year fixed mortgage at an annual interest rate of $6.50\%$.
1. What is the standard monthly principal and interest payment ($PMT$)?
2. If the homeowner pays an extra $\$300\text{ per month}$ toward principal ($PMT = \$2{,}828.31$), how many years earlier will the mortgage be paid off?

#### How to Solve It on the SC-95
1. **Calculate Standard Monthly Payment:**
   - Set mode to `END` of period.
   - Number of periods: $30 \times 12 = 360 \implies$ `360` `[f] [N]`.
   - Monthly interest rate: $6.50\% / 12 = 0.54167\% \implies$ `6.5` `[ENTER]` `12` `[÷]` `[f] [I%YR]`.
   - Loan amount: `400000` `[f] [PV]`.
   - Final balance: `0` `[f] [FV]`.
   - Solve for payment: Tap `[f] [PMT]`.
   - Register $X$ displays: **`-$2,528.31`** (Monthly payment).
2. **Calculate Accelerated Payoff with $+\$300$ Extra:**
   - Enter new payment: `-2828.31` `[f] [PMT]`.
   - Solve for remaining periods: Tap `[f] [N]`.
   - Register $X$ displays: **`275.8 months`** ($23.0\text{ years}$).
   - **Result:** Paying an extra $\$300/\text{month}$ cuts **7 full years (84 payments)** off the mortgage and saves over **$\$128{,}000$ in interest**!

---

### Field Case 2: Machining Tolerance Audit ($C_{pk}$) on a Stamping Line

A quality engineer audits a CNC shaft turning operation:
- Blueprint specification: $25.000\text{ mm} \pm 0.050\text{ mm}$ ($LSL = 24.950$, $USL = 25.050$).
- A 50-part sample gives an average diameter $\mu = 25.012\text{ mm}$ and standard deviation $\sigma = 0.008\text{ mm}$.
What is the process capability $C_{pk}$?

#### Step-by-Step Mechanics
1. **Compute Distance to Upper Limit:**
   $$\frac{USL - \mu}{3\sigma} = \frac{25.050 - 25.012}{3(0.008)} = \frac{0.038}{0.024} \approx \mathbf{1.583}$$
2. **Compute Distance to Lower Limit:**
   $$\frac{\mu - LSL}{3\sigma} = \frac{25.012 - 24.950}{3(0.008)} = \frac{0.062}{0.024} \approx \mathbf{2.583}$$
3. **Determine $C_{pk}$:**
   $$C_{pk} = \min(1.583, 2.583) = \mathbf{1.58}$$
   Because $C_{pk} = 1.58 > 1.33$, the process is capable and well-centered with virtually zero defect risk!

---

## 4. Try It Yourself: Practice Problems

### Problem 1: Retirement Nest Egg (Future Value)
You invest $\$500$ at the end of every month ($PMT = -500$) into an index fund averaging $8.0\%$ annual return ($i = 8.0 / 12 = 0.6667\%$) for 35 years ($N = 35 \times 12 = 420\text{ months}$). You start with $\$0$ ($PV = 0$).
Calculate the accumulated Future Value ($FV$).
*(Solution: $FV = \mathbf{\$1,146,941.24}$. A $\$500$/month habit produces over $\$1.1$ million dollars through compound interest!)*

### Problem 2: Corporate Equipment Net Present Value (NPV)
A manufacturing plant is considering installing an automated packaging robot:
- Initial cost today: $CF_0 = -\$60{,}000$
- Cash savings Year 1: $CF_1 = +\$25{,}000$
- Cash savings Year 2: $CF_2 = +\$25{,}000$
- Cash savings Year 3: $CF_3 = +\$25{,}000$
The company's required discount rate is $10\%$ ($r = 0.10$).
Calculate the Net Present Value ($NPV$).
*(Solution: Present value of annual savings $= 25000 / 1.1 + 25000 / 1.1^2 + 25000 / 1.1^3 = 22727 + 20661 + 18783 = \$62,171$. $NPV = -60000 + 62171 = \mathbf{+\$2,171.30}$. Since $NPV > 0$, the project is financially sound and approved!)*

### Problem 3: Standard Normal Distribution Quantile ($Z$-Score)
In statistical hypothesis testing, what is the two-tailed critical $Z$-score for a $95\%$ confidence level (where $2.5\%$ sits in the upper tail, meaning cumulative probability $P = 0.975$)?
On the SC-95, enter `0.975` and tap `[g] [InvNorm]` (`qnorm` in R).
*(Solution: Register $X$ displays **`1.95996`** $\implies \mathbf{1.96}$. The iconic $1.96\sigma$ confidence interval multiplier!)*
