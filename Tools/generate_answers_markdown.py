#!/usr/bin/env python3
"""Generates the master curriculum online answer key markdown file at docs/curriculum/answers.md."""

import sys
from pathlib import Path

# Add Education/tools to sys.path
sys.path.append(str(Path("/Users/abagher/Documents/GitHub/watch-calc-32/Education/tools")))

from grade_band_curricula_data import (
    EARLY_ELEMENTARY_UNITS,
    UPPER_ELEMENTARY_UNITS,
    HIGH_SCHOOL_UNITS,
    GRADE_BAND_UNIT_WORKSHEETS,
    GRADE_BAND_CUMULATIVE_EXAMS,
)
from workbook_expansion_data import (
    get_full_year_section_tests,
)
from speed_tests_data import get_speed_test_sections

out_path = Path("/Users/abagher/Documents/GitHub/stackcalc/docs/curriculum/answers.md")

lines = [
    "# 📖 StackCalc Master Answer Key & Keystroke Verification Portal",
    "",
    "> **The Paper-First Principle:** Calculators should never replace reasoning. Students first build the problem with physical 3D blocks or write their mathematical setup, solve on paper by hand, and verify on their distraction-free StackCalc instrument. This portal provides complete worked solutions and canonical keystrokes across all volumes in *The StackCalc Library*.",
    "",
    "---",
    "",
    "## 📚 Quick Navigation by Book",
    "",
    "- [Book 2A: Early Elementary Math Lab (Grades K–2 • SC-6 • Units 01–10)](#early-elementary)",
    "- [Book 2B: Upper Elementary Math Lab (Grades 3–5 • SC-6 • Units 01–10)](#upper-elementary)",
    "- [Book 3: Middle School Math Lab (Grades 6–8 • SC-6 • Units 01–10)](#middle-school)",
    "- [Book 4: High School & STEM Lab (Grades 9–12 & AP • SC-32 • Units 01–10)](#high-school)",
    "- [Book 5: Stack Speed & Fluency (Full-Year 180-Test Edition)](#speed-fluency)",
    "",
    "---",
    "",
]


def render_grade_band_unit(u, band_key, calc_short):
    u_lines = []
    u_ws = GRADE_BAND_UNIT_WORKSHEETS[band_key][u.unit_number]
    u_lines.append(f"### Unit {u.unit_number:02d}: {u.title}")
    stds = ", ".join(u.standards)
    u_lines.append(f"**Grades:** {u.grades} | **Instrument:** StackCalc {calc_short} | **Visual / Block Model:** {u.manipulative}")
    u_lines.append(f"**Key Standards:** {stds}")
    u_lines.append("")
    u_lines.append("#### 1. Concept Labs & Warm-Up Solutions")
    lp = u.primary_lesson
    ext = u.followup_lesson
    k_lp = " ".join(lp.worksheet_expected_keys)
    k_ext = " ".join(ext.worksheet_expected_keys)
    u_lines.append(f"- **Warm-Up A (Core Lab):** {lp.worksheet_problem}")
    u_lines.append(f"  - *Verified Answer:* `{lp.worksheet_answer}`")
    u_lines.append(f"  - *Keystrokes:* `{k_lp}`")
    u_lines.append(f"- **Warm-Up B (Extension Lab):** {ext.worksheet_problem}")
    u_lines.append(f"  - *Verified Answer:* `{ext.worksheet_answer}`")
    u_lines.append(f"  - *Keystrokes:* `{k_ext}`")
    if band_key == "upper_elementary" and u.unit_number in (6, 10):
        u_lines.append("- **Hands-On Block Focus (Fraction Multiplication & Division):**")
        u_lines.append("  - *Multiplication:* Scaling one tower by another (e.g., 2/3 of 3/8 = 1/4 matching the 21 mm block).")
        u_lines.append("  - *Division (Split & Rebuild 1 Full Tower):* To divide `1/2 ÷ 3/4`, split the 1/2 block (42 mm) into 3 equal 1/6 blocks (`÷ 3 -> 14 mm` is 1/4 of the mystery tower), then stack 4 of those 1/6 blocks (`× 4 -> 56 mm = 2/3`) to prove why `÷(3/4) = ×(4/3)`!")
    u_lines.append("")
    u_lines.append("#### 2. Hands-On Lab Investigations (Investigations 1–4)")
    u_lines.append("| # | Investigation Prompt | Expected Solution | Calculator Verification Keys |")
    u_lines.append("|---|---|---|---|")
    for p_idx, p in enumerate(u.practice_problems):
        keys_str = " ".join(p["keys"])
        u_lines.append(f"| {p_idx + 1} | {p['prompt']} | **{p['ans']}** | `{keys_str}` |")
    u_lines.append("")
    u_lines.append("#### 3. Leveled Practice Worksheets (Practice A through F)")
    u_lines.append("| Problem # | Practice A (Core) | Practice B (Multi-Step) | Practice C (Real-World) | Practice D (Mental Math) | Practice E (STEM Apps) | Practice F (Mastery) |")
    u_lines.append("|:---:|:---:|:---:|:---:|:---:|:---:|:---:|")
    num_probs = min(len(u_ws["sheet_a"]["problems"]), 10)
    for i in range(num_probs):
        def _fmt_cell(p_item):
            ans = p_item[1]
            keys = " ".join(p_item[2]) if len(p_item) > 2 else ""
            return f"**{ans}**<br>`{keys}`" if keys else f"**{ans}**"

        ans_a = _fmt_cell(u_ws["sheet_a"]["problems"][i])
        ans_b = _fmt_cell(u_ws["sheet_b"]["problems"][i])
        ans_c = _fmt_cell(u_ws["sheet_c"]["problems"][i])
        ans_d = _fmt_cell(u_ws["sheet_d"]["problems"][i])
        ans_e = _fmt_cell(u_ws["sheet_e"]["problems"][i])
        ans_f = _fmt_cell(u_ws["sheet_f"]["problems"][i])
        u_lines.append(f"| **#{i + 1}** | {ans_a} | {ans_b} | {ans_c} | {ans_d} | {ans_e} | {ans_f} |")
    u_lines.append("")
    u_lines.append("#### 4. 100-Point Unit Mastery Check")
    u_lines.append("| # | Category | Assessment Prompt | Points | Expected Solution | Verification Keys |")
    u_lines.append("|:---:|---|---|:---:|---|---|")
    for q_idx, q_item in enumerate(u_ws["quiz"]):
        q_prompt = q_item[0]
        q_ans = q_item[1]
        q_keys = " ".join(q_item[2]) if len(q_item) > 2 else ""
        cat = "Core Fluency" if q_idx < 6 else ("Application" if q_idx < 9 else "Error Analysis")
        u_lines.append(f"| **{q_idx + 1}** | {cat} | {q_prompt} | 10 pts | **{q_ans}** | `{q_keys}` |")
    u_lines.append("")
    if "stem_case" in u_ws and u_ws["stem_case"]:
        sc = u_ws["stem_case"]
        sc_title = sc.get("title", "STEM Lab Case Study")
        u_lines.append(f"#### 5. STEM Lab Case Study: {sc_title}")
        if sc.get("context"):
            u_lines.append(f"> *Scenario:* {sc['context']}")
            u_lines.append("")
        for sc_idx, q_item in enumerate(sc.get("questions", [])):
            q_prompt = q_item[0]
            q_ans = q_item[1]
            q_keys = " ".join(q_item[2]) if len(q_item) > 2 else ""
            u_lines.append(f"- **Case Question {sc_idx + 1}:** {q_prompt}")
            u_lines.append(f"  - *Expected Result:* **{q_ans}**" + (f" | *Keystrokes:* `{q_keys}`" if q_keys else ""))
        u_lines.append("")
    u_lines.append("---")
    u_lines.append("")
    return u_lines


def render_cumulative_exams(band_key, calc_short):
    c_lines = []
    c_lines.append("### Appendix C: Cumulative Benchmark & Capstone Mastery Exams (Pages 117–120)")
    c_lines.append("")
    for c_exam in GRADE_BAND_CUMULATIVE_EXAMS[band_key]:
        ex_num = c_exam["exam_number"]
        ex_pg = 116 + ex_num
        c_lines.append(f"#### {c_exam['title']} (`p. {ex_pg}` • 100 Points)")
        c_lines.append(f"> *{c_exam['banner_note']}*")
        c_lines.append("")
        c_lines.append("| # | Category | Assessment Prompt | Points | Expected Solution | Verification Keys |")
        c_lines.append("|:---:|---|---|:---:|---|---|")
        for q_idx, (q_prompt, q_ans, q_keys) in enumerate(c_exam["problems"]):
            keys_str = " ".join(q_keys)
            cat = "Core Fluency" if q_idx < 6 else ("Application" if q_idx < 9 else "Error Analysis")
            c_lines.append(f"| **{q_idx + 1}** | {cat} | {q_prompt} | 10 pts | **{q_ans}** | `{keys_str}` |")
        c_lines.append("")
    c_lines.append("---")
    c_lines.append("")
    return c_lines


# Book 2A: Early Elementary
lines.append('<a id="early-elementary"></a>')
lines.append("## 📗 Book 2A: Early Elementary Math Lab (Grades K–2 • SC-6)")
lines.append("*Covers Units 01 through 10 plus 4 Cumulative Benchmark & Capstone Mastery Exams: Step Counting, Number Bonds, Make-10 Trades, Doubling, Place Value, Subtraction, Regrouping Carry, Two-Digit Operations, Equal Groups & Arrays, and Measurement/Money (840 active problems).*")
lines.append("")
for u in EARLY_ELEMENTARY_UNITS:
    lines.extend(render_grade_band_unit(u, "early_elementary", "SC-6"))
lines.extend(render_cumulative_exams("early_elementary", "SC-6"))

# Book 2B: Upper Elementary
lines.append('<a id="upper-elementary"></a>')
lines.append("## 📘 Book 2B: Upper Elementary Math Lab (Grades 3–5 • SC-6)")
lines.append("*Covers Units 01 through 10 plus 4 Cumulative Benchmark & Capstone Mastery Exams: Multiplication Arrays, Division & Remainders, Unit Fractions, Multi-Digit Operations, Long Division & Factors, Fraction Equivalence, Prime Factorization/GCF/LCM, 4-Register Stack PEMDAS, Mixed Numbers, and Fraction Multiplication & Division (840 active problems).*")
lines.append("")
for u in UPPER_ELEMENTARY_UNITS:
    lines.extend(render_grade_band_unit(u, "upper_elementary", "SC-6"))
lines.extend(render_cumulative_exams("upper_elementary", "SC-6"))

# Book 3: Middle School
lines.append('<a id="middle-school"></a>')
lines.append("## 📙 Book 3: Middle School Math Lab (Grades 6–8 • SC-6)")
lines.append("*Full 45-Section Two-Method Student Workbook (900 problems + 10 Unit Mastery Quizzes).*")
lines.append("")
lines.append("Complete section-by-section answers, calculator keystroke traces, and 100-point quiz solutions for Book 3 are published in the dedicated Middle School Portal:")
lines.append("👉 [**Middle School Math Lab Complete Solutions Directory**](big-ideas-middle-school-sc6-workbook.md)")
lines.append("")
lines.append("---")
lines.append("")

# Book 4: High School & STEM
lines.append('<a id="high-school"></a>')
lines.append("## 📕 Book 4: High School & STEM Lab (Grades 9–12 & AP • SC-32)")
lines.append("*Covers Units 01 through 10 plus 4 Cumulative Benchmark & Capstone Mastery Exams: Linear Functions & Slope, Factoring Quadratics, Quadratic Formula & [POLY], Higher-Degree Polynomials & Horner's Method, Compound Growth & Exponents, Logarithms & Base e, Right-Triangle Trig, 2D Polar Vectors, Combinatorics & Statistics, and Binary/Hex Digital Logic (840 active problems).*")
lines.append("")
for u in HIGH_SCHOOL_UNITS:
    lines.extend(render_grade_band_unit(u, "high_school", "SC-32"))
lines.extend(render_cumulative_exams("high_school", "SC-32"))

# Book 5: Speed & Fluency
lines.append('<a id="speed-fluency"></a>')
lines.append("## ⚡ Book 5: Stack Speed & Fluency (Full-Year 180-Test Edition)")
lines.append("*Complete solutions for all 15 Speed Lessons, 90 Warm-Up Drills, 180 Timed Tests (3,600 problems), Appendix B Sprint Drills, and Champion Pipelines.*")
lines.append("")
sections = get_speed_test_sections()
for sec in sections:
    full_tests = get_full_year_section_tests(sec)
    lines.append(f"### Section {sec.short_code}: {sec.title}")
    lines.append(f"**Grades:** {sec.grades_label} | **Focus:** {sec.focus_summary}")
    lines.append("")
    lines.append("#### 1. Warm-Up Drills (W1–W6)")
    lines.append("| Drill | Prompt | Shortcut Cue | Verified Answer |")
    lines.append("|:---:|---|---|---|")
    for w_idx, (w_prompt, w_cue, w_ans) in enumerate(sec.warmup_drills):
        lines.append(f"| **W{w_idx + 1}** | {w_prompt} | *{w_cue}* | **{w_ans}** |")
    lines.append("")
    lines.append("#### 2. Progressive Practice Tests (Tests A1–A3, B1–B3, C1–C3, D1–D3)")
    lines.append("| # | Test A1 | Test A2 | Test A3 | Test B1 | Test B2 | Test B3 | Test C1 | Test C2 | Test C3 | Test D1 | Test D2 | Test D3 |")
    lines.append("|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|")
    for p_i in range(20):
        row_vals = [f"**#{p_i + 1}**"]
        for tset in full_tests:
            row_vals.append(str(tset.problems[p_i][1]))
        lines.append("| " + " | ".join(row_vals) + " |")
    lines.append("")
    lines.append("#### 3. Optimal Champion Pipelines")
    for pipe_label, pipe_steps in sec.champion_pipelines:
        lines.append(f"- **{pipe_label}:** `{pipe_steps}`")
    lines.append("")
    lines.append("---")
    lines.append("")

with open(out_path, "w") as f:
    f.write("\n".join(lines))

print(f"Successfully generated {out_path} ({len(lines)} lines)!")
