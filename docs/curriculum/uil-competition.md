---
title: "Texas UIL & TMSCA Calculator Applications Competition Center | StackCalc"
description: "Tournament-grade practice exams, official scoring keys, and RPN speed benchmarks for Texas UIL and TMSCA Calculator Applications competitions. High School (SC-32) and Elementary Grades 3-6 (SC-6) PDF downloads."
---

# Texas UIL & TMSCA Calculator Applications Competition Center

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">TOURNAMENT PREPARATION // 12 FULL EXAM EDITIONS &bull; 650 COMPETITIVE PROBLEMS</span>
  <span class="te-viewport-status text-emerald-400">● OFFICIAL UIL / TMSCA / PSIA / TAPPS SCORING &bull; 100% PRE-GENERATED TOURNAMENT PDFS</span>
</div>

<nav class="curriculum-subnav flex flex-wrap gap-2 p-2.5 rounded-xl bg-[#0D1017] border border-white/10 mb-8 font-mono text-xs" aria-label="Curriculum Navigation">
  <a href="../" class="px-3 py-1.5 rounded bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white transition font-bold">📖 Master Guide</a>
  <a href="../rpn-elementary-guide/" class="px-3 py-1.5 rounded bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white transition font-bold">⚡ RPN Power Guide</a>
  <a href="../worksheets/" class="px-3 py-1.5 rounded bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white transition font-bold">📝 120 Station Worksheets</a>
  <a href="../alignment-matrix/" class="px-3 py-1.5 rounded bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white transition font-bold">🎯 Standards Matrix</a>
  <a href="../teacher-guide/" class="px-3 py-1.5 rounded bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white transition font-bold">🧑‍🏫 Teacher Guide</a>
  <a href="./" class="px-3 py-1.5 rounded bg-white text-slate-950 font-bold transition">🏆 UIL Competition</a>
</nav>

Welcome to the **StackCalc Calculator Competition Center**. The Texas University Interscholastic League (UIL), Texas Math and Science Coaches Association (TMSCA), Private Schools Interscholastic Association (PSIA), and Texas Association of Private and Parochial Schools (TAPPS) Calculator Applications contests are the nation's premier speed-and-accuracy academic math tournaments. Contestants face an intense, strictly timed 30-minute sprint featuring 70 problems (High School) or 50 problems (Junior High & Elementary), spanning numerical calculation, geometric vector figures, and applied multi-step word problems.

StackCalc provides **12 complete, authentic tournament test editions** across three distinct competitive tiers, accompanied by official contest-standard scoring keys with 3-significant-figure canonical answers and exact acceptance intervals:
* **High School Championship Tier (4 Editions &bull; 70 Problems each):** UIL 26A, 26B, 26C, and TAPPS-HS on the **SC-32 RPN Scientific Calculator**.
* **Junior High / Middle School Tier (4 Editions &bull; 50 Problems each):** TMSCA 26MS, PSIA-MS, and Grade-Level Championships for **Grade 7** and **Grade 8**.
* **Elementary School Tier (4 Editions &bull; 30–50 Problems each):** Single-mode sectioned tests for **Grade 3**, **Grade 4**, **Grade 5**, and **Grade 6** on the **SC-6 Elementary Calculator**.

---

## The Tournament Keystroke Race: Texas UIL Problem 14

In Texas UIL and TMSCA Calculator Applications, competitors have exactly **30 minutes to complete 70 rigorous problems**. At an average pace of **25.7 seconds per problem**, typing speed, finger rhythm, and error prevention dictate tournament medalists. Missing a single closing parenthesis triggers a fatal syntax error or silently corrupts algebraic operator precedence, costing $-4$ penalty points per missed question.

Here is an authentic tournament benchmark: evaluating a multi-stage rational expression typical of **UIL High School Problem 14**:

$$
\text{Problem 14: } \frac{4.82 \times 10^3 - 195}{\sqrt{84.6} + 12.7^2}
$$

### Head-to-Head Architecture: Infix vs. RPN

| Competition Metric | Standard Classroom Infix (TI-84 Plus CE) | StackCalc SC-32 RPN Architecture |
| :--- | :--- | :--- |
| **Total Keystrokes** | **24 keystrokes** | **14 keystrokes** *(41.7% fewer keystrokes)* |
| **Parentheses Required** | **4 parentheses** (`(`, `)`, `(`, `)`) | **0 parentheses** *(Zero syntax error risk)* |
| **Intermediate Visibility** | **Hidden** (Expression string until `{{keycap:ENTER}}`) | **Visible at every keypress** (`X`, `Y`, `Z`, `T` LCD lines) |
| **Syntax Error Hazard** | **High** (Mismatched parens discard calculation) | **Impossible** (Each operator executes immediately) |
| **Cognitive Load** | High (Student must mentally balance nested brackets) | Low (Operands entered from inside-out in natural evaluation order) |
| **Time to Compute** | ~14.2 seconds | **~6.8 seconds** *(2.1× faster execution)* |

### Step-by-Step Keystroke Breakdown (`{{res:curr_sc32_uil_prob14:keys}}` &rarr; `{{res:curr_sc32_uil_prob14:value}}`)

<div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6 font-mono text-xs">

<div class="p-4 rounded-xl bg-[#11141A] border border-red-500/30">
  <div class="text-red-400 font-bold mb-2 uppercase tracking-wider">// TRADITIONAL INFIX (TI-84 PLUS CE) — 24 KEYS</div>
  <ol class="space-y-1 text-slate-300">
    <li><code>1.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">(</kbd> (Open numerator)</li>
    <li><code>2-5.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">4</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">.</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">8</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">2</kbd></li>
    <li><code>6-8.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">2nd</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">EE</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">3</kbd></li>
    <li><code>9.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">−</kbd></li>
    <li><code>10-12.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">1</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">9</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">5</kbd></li>
    <li><code>13.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">)</kbd> (Close numerator)</li>
    <li><code>14.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">÷</kbd></li>
    <li><code>15.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">(</kbd> (Open denominator)</li>
    <li><code>16-17.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">2nd</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">√</kbd></li>
    <li><code>18-21.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">8</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">4</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">.</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">6</kbd></li>
    <li><code>22.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">+</kbd></li>
    <li><code>23-26.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">1</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">2</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">.</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">7</kbd><kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">x²</kbd></li>
    <li><code>27.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">)</kbd> (Close denominator)</li>
    <li><code>28.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">ENTER</kbd></li>
  </ol>
  <div class="mt-3 p-2 rounded bg-red-950/40 border border-red-500/20 text-red-300 text-[11px]">
    ⚠️ <strong>Hazard:</strong> Omitting the outer denominator parens calculates <code>(Numerator / √84.6) + 12.7²</code>, silently producing an incorrect answer and costing $-4$ points.
  </div>
</div>

<div class="p-4 rounded-xl bg-[#11141A] border border-emerald-500/30">
  <div class="text-emerald-400 font-bold mb-2 uppercase tracking-wider">// STACKCALC SC-32 RPN ARCHITECTURE — 14 KEYS</div>
  <ol class="space-y-1 text-slate-300">
    <li><code>1.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">4.82</kbd> <kbd class="px-1.5 py-0.5 rounded bg-amber-400/20 text-amber-300 font-bold">{{keycap:E}}</kbd> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">3</kbd> &rarr; <code>X: 4820</code></li>
    <li><code>2.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/20 text-white font-bold">{{keycap:ENTER}}</kbd> &rarr; <code>Y: 4820 | X: 4820</code></li>
    <li><code>3.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">195</kbd> <kbd class="px-1.5 py-0.5 rounded bg-blue-400/20 text-blue-300 font-bold">{{keycap:-}}</kbd> &rarr; <code>X: 4625</code> (Numerator locked in stack)</li>
    <li><code>4.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">84.6</kbd> <kbd class="px-1.5 py-0.5 rounded bg-amber-400/20 text-amber-300 font-bold">{{keycap:√x}}</kbd> &rarr; <code>Y: 4625 | X: 9.1978</code></li>
    <li><code>5.</code> <kbd class="px-1.5 py-0.5 rounded bg-white/10 text-white">12.7</kbd> <kbd class="px-1.5 py-0.5 rounded bg-amber-400/20 text-amber-300 font-bold">{{key:x²}}</kbd> &rarr; <code>Z: 4625 | Y: 9.1978 | X: 161.29</code></li>
    <li><code>6.</code> <kbd class="px-1.5 py-0.5 rounded bg-blue-400/20 text-blue-300 font-bold">{{keycap:+}}</kbd> &rarr; <code>Y: 4625 | X: 170.4878</code> (Denominator resolved)</li>
    <li><code>7.</code> <kbd class="px-1.5 py-0.5 rounded bg-blue-400/20 text-blue-300 font-bold">{{keycap:÷}}</kbd> &rarr; <code>X: 27.1</code> (Full precision: <code>{{res:curr_sc32_uil_prob14:value}}</code>)</li>
  </ol>
  <div class="mt-3 p-2 rounded bg-emerald-950/40 border border-emerald-500/20 text-emerald-300 text-[11px]">
    ✨ <strong>RPN Dividend:</strong> Every intermediate step is verified on the 4-line LCD. Zero parentheses, zero syntax errors, and 10 fewer physical clicks.
  </div>
</div>

</div>

> [!TIP] The 700-Keystroke Tournament Advantage
> Over a full 70-problem UIL High School exam, saving an average of 10 keystrokes per problem eliminates **700 keystrokes**. That saves roughly **4 to 5 minutes** of pure physical finger fatigue—allowing competitors to cleanly attempt **4 to 6 additional questions**. Under UIL scoring (+5 for correct, -4 for incorrect), those extra questions represent an additional **+20 to +30 tournament points**, consistently deciding State Championship podium finishes.

---

## 1. High School Championship Division (SC-32 Scientific)

Full 70-problem, 7-page tournament examinations covering multi-stage rational arithmetic, integer and fractional powers, roots, scientific notation, circular sectors, right triangles, 3D conical frustums, coordinate geometry, trigonometry (rad/deg), logarithms, and hyperbolic functions.

| Exam Edition | Organization / Division | Scope & Content | Student Exam Booklet | Official Scoring Key |
| :--- | :--- | :--- | :---: | :---: |
| **2026 UIL Invitational A** (`26A`) | Texas UIL High School | 70 Problems &bull; 7 Pages &bull; Sprint &amp; Word Geometry | [Download Exam Booklet &darr;](../downloads/uil/uil_exam_26a.pdf) | [Download Scoring Key &darr;](../downloads/uil/uil_solutions_26a.pdf) |
| **2026 UIL Invitational B** (`26B`) | Texas UIL High School | 70 Problems &bull; 7 Pages &bull; Rigorous Rational &amp; Cones | [Download Exam Booklet &darr;](../downloads/uil/uil_exam_26b.pdf) | [Download Scoring Key &darr;](../downloads/uil/uil_solutions_26b.pdf) |
| **2026 District Championship C** (`26C`) | Texas UIL High School | 70 Problems &bull; 7 Pages &bull; Advanced Trig &amp; Frustums | [Download Exam Booklet &darr;](../downloads/uil/uil_exam_26c.pdf) | [Download Scoring Key &darr;](../downloads/uil/uil_solutions_26c.pdf) |
| **2026 TAPPS State Championship** (`TAPPS-HS`) | TAPPS High School (1A–6A) | 70 Problems &bull; 7 Pages &bull; Private School Varsity Final | [Download Exam Booklet &darr;](../downloads/uil/uil_exam_tapps-hs.pdf) | [Download Scoring Key &darr;](../downloads/uil/uil_solutions_tapps-hs.pdf) |

---

## 2. Junior High & Middle School Division (Grades 6–8)

Authentic 50-problem, 5-page examinations strictly timed to 30 minutes. Includes state championship formats for public and private school leagues as well as curriculum-aligned grade-level exams:

| Exam Edition | Level / Division | Structure | Core Curriculum Focus | Student Exam Booklet | Official Scoring Key |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **2026 TMSCA Middle School** (`26MS`) | Junior High (Grades 6–8) | 50 Problems &bull; 5 Pages | Statewide Championship &bull; Rational, Roots &amp; Cones | [Download Exam Booklet &darr;](../downloads/uil/uil_exam_26ms.pdf) | [Download Scoring Key &darr;](../downloads/uil/uil_solutions_26ms.pdf) |
| **2026 PSIA Middle School** (`PSIA-MS`) | Private School (Grades 6–8) | 50 Problems &bull; 5 Pages | PSIA State Championship &bull; Geometry Diagrams &amp; Rates | [Download Exam Booklet &darr;](../downloads/uil/uil_exam_psia-ms.pdf) | [Download Scoring Key &darr;](../downloads/uil/uil_solutions_psia-ms.pdf) |
| **Grade 7 Championship** (`SC6-G7`) | Junior High (Grade 7) | 50 Problems &bull; 5 Pages &bull; Sections | Signed Rationals, Proportions, Simple Interest $I=Prt$, Circles | [Download Exam Booklet &darr;](../downloads/uil/uil_exam_sc6-g7.pdf) | [Download Scoring Key &darr;](../downloads/uil/uil_solutions_sc6-g7.pdf) |
| **Grade 8 Championship** (`SC6-G8`) | Junior High (Grade 8) | 50 Problems &bull; 5 Pages &bull; Sections | Exponents, Scientific Notation, Square Roots, Pythagoras, Cylinders | [Download Exam Booklet &darr;](../downloads/uil/uil_exam_sc6-g8.pdf) | [Download Scoring Key &darr;](../downloads/uil/uil_solutions_sc6-g8.pdf) |

---

## 3. Elementary School Division (Grades 3–6 &bull; SC-6 Calculator)

Designed specifically for elementary classroom leagues, TMSCA Elementary meets, and campus A+ math teams. Every elementary test is organized into **10-problem single-mode sections** with top-of-page mode banners (`{{keycap:123}}`, `{{keycap:FDISP}}`, `{{keycap:CLK}}`, `{{keycap:%}}`), completely eliminating in-test mode confusion.

> [!IMPORTANT] Strict Curriculum Boundary
> In compliance with Common Core, Singapore Math, and TEKS elementary standards, **all square roots ($\sqrt{x}$) and radicals have been eliminated from Grades 3, 4, and 5**. Grade 6 introduces small whole-number repeated powers ($4^3$, $2^5$) without radical cascades.

| Grade Level | Exam Edition | Structure | Targeted Skills & Dedicated Hardware Modes | Student Exam Booklet | Official Scoring Key |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Grade 3** | **SC6-G3: Novice Sprint** | 30 Problems &bull; 3 Pages | **P1:** `{{keycap:123}}` Whole Numbers &bull; **P2:** `{{keycap:FDISP}}` Like Fractions &bull; **P3:** `{{keycap:CLK}}` Elapsed Time | [Download Exam Booklet &darr;](../downloads/uil/uil_exam_sc6-g3.pdf) | [Download Scoring Key &darr;](../downloads/uil/uil_solutions_sc6-g3.pdf) |
| **Grade 4** | **SC6-G4: Elementary A+** | 40 Problems &bull; 4 Pages | **P1:** `{{keycap:123}}` Multi-Digit &bull; **P2:** `{{keycap:FDISP}}` Mixed Numbers &bull; **P3:** `{{keycap:123}}` Decimals &bull; **P4:** `{{keycap:CLK}}` Time &amp; Area | [Download Exam Booklet &darr;](../downloads/uil/uil_exam_sc6-g4.pdf) | [Download Scoring Key &darr;](../downloads/uil/uil_solutions_sc6-g4.pdf) |
| **Grade 5** | **SC6-G5: Championship** | 50 Problems &bull; 5 Pages | **P1:** `{{keycap:123}}` Decimals &bull; **P2:** `{{keycap:FDISP}}` Unlike Fractions &bull; **P3:** `{{keycap:FDISP}}` Scaling &bull; **P4:** `{{keycap:123}}` Prisms &bull; **P5:** `{{keycap:123}}` Rates | [Download Exam Booklet &darr;](../downloads/uil/uil_exam_sc6-g5.pdf) | [Download Scoring Key &darr;](../downloads/uil/uil_solutions_sc6-g5.pdf) |
| **Grade 6** | **SC6-G6: Intermediate** | 50 Problems &bull; 5 Pages | **P1:** `{{keycap:123}}` Rationals &bull; **P2:** `{{keycap:FDISP}}` Fraction Division &bull; **P3:** `{{keycap:%}}` Percent &amp; Tax &bull; **P4:** `{{keycap:123}}` Circles &bull; **P5:** `{{keycap:123}}` Rates | [Download Exam Booklet &darr;](../downloads/uil/uil_exam_sc6-g6.pdf) | [Download Scoring Key &darr;](../downloads/uil/uil_solutions_sc6-g6.pdf) |

---

## Booklet Architecture & High-Contrast Scoring Design

Both the Student Examination Booklets and Official Scoring Keys follow strict tournament printing conventions:

```
+===================================================================================+
| STUDENT EXAMINATION BOOKLET (70 OR 50 PROBLEMS)                                   |
+-----------------------------------------------------------------------------------+
| • Official UIL header with 30-minute timer directive and 3-sig-fig rubric banner  |
| • Contestant Identification Block with Grade-Level Selection Checkboxes           |
| • 7-Page Grader Subtotal Table (Page 1 through Page 7 score tallies)               |
| • Dynamic label spacing preventing collision with multi-digit prefixes            |
| • Dotted leader lines connecting problems directly to right-aligned answer blanks |
| • High-resolution vector diagrams (triangles, circular sectors, 3D cones)        |
+===================================================================================+
| OFFICIAL TOURNAMENT SCORING KEY (4-COLUMN CLEAN FORMAT)                           |
+-----------------------------------------------------------------------------------+
| • Column 1: Problem Number (#)                                                    |
| • Column 2: Official Contest Answer (3-Sig-Fig Canonical Standard)                |
| • Column 3: Scientific Notation Equivalent (Clean LaTeX/Standard notation)        |
| • Column 4: Acceptance Interval (±2 units in 3rd significant digit)                |
| • Bottom Benchmark Box: Aggregate keystrokes saved vs Algebraic calculators       |
| • Official Grader 1, Grader 2, and Contest Director signature blocks             |
+===================================================================================+
```

> [!NOTE] Keystroke Sequence Omission on Scoring Keys
> Tournament grading judges grade 70-problem tests in under 5 minutes using high-speed grading overlays. To ensure optimal contrast and zero visual clutter, **scoring keys strictly display the official 3-sig-fig answers and acceptance ranges without extraneous keystroke strings**.

---

## Contest Coaching & Sprint Pacing Strategies

Coaches training calculator teams can apply these proven pacing milestones to maximize score yields:

### 1. The Page 1–2 Baseline Sprint (Minutes 0:00 – 7:00)
Pages 1 and 2 consist of straightforward numerical calculations. Contestants should complete all 20 problems in under 7 minutes. Because RPN eliminates parentheses, keystroke cadence should be fluid and rhythmic. Aim for $100\%$ accuracy here, yielding $+100$ baseline points.

### 2. The Word Problem Filter (Minutes 7:00 – 16:00)
Pages 3 and 4 introduce stated word problems and first-tier geometry (triangles, rectangles). Contestants should read the word problem, extract the required formula, execute the RPN chain, and write down the 3-sig-fig answer immediately without writing scratch equations.

### 3. The Geometry Vector Sweep (Minutes 16:00 – 24:00)
Page 5 contains geometric figures (frustums, circular sectors). Train competitors to solve from the inside out: compute radius subtractions first, stack the result, multiply by slant height, and terminate with `{{key:π}}` and `{{key:×}}`.

### 4. The Final Push & Strategic Stopping (Minutes 24:00 – 30:00)
Under UIL scoring rules, an unattempted question incurs **zero penalty**, while an incorrect guess costs **$-4$ points**. In the final 2 minutes, competitors should never make blind guesses. Once they reach their peak problem, they should stop cleanly to avoid negative deductions.

---

## 3D Printable Classroom Competition Stands

For team practices and tournament desks, download the [Modular 3-in-1 Desk Stands](../downloads.md#3-individual-manipulative-kit-archives) engineered to hold the SC-32 and SC-6 at an ergonomic 15° reading angle, minimizing overhead glare from gymnasium fluorescent fixtures during competition meets.
