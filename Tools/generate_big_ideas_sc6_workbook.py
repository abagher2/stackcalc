#!/usr/bin/env python3
"""
Generate Printable PDF Workbooks for the Big Ideas Math Middle School SC-6 Catch-Up Program
and keep the Markdown curriculum synchronized with the 45-Day Confidence Ramp, 30-Second
Zero-Fail Starters, 5 Rotating Variety Game Modes, and 3-Visit Spiral Reward System.

Reads and synchronizes the single-source-of-truth curriculum markdown:
  - docs/curriculum/big-ideas-middle-school-sc6-workbook.md

Produces two publication-grade ReportLab PDFs:
  1. docs/downloads/worksheets/bigideas_middle_school_sc6_daily_student_workbook.pdf
  2. docs/downloads/worksheets/bigideas_middle_school_sc6_teacher_coach_guide.pdf
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT / "Tools") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "Tools"))

from book_engine import expand_key_macros

DOCS_DIR = REPO_ROOT / "docs"
WATCH_CALC_ROOT = REPO_ROOT.parent / "watch-calc-32"
FONT_DIR = (
    DOCS_DIR / "assets" / "fonts"
    if (DOCS_DIR / "assets" / "fonts" / "SpaceMono-Regular.ttf").exists()
    else (WATCH_CALC_ROOT / "documentation")
)

SOURCE_MD = DOCS_DIR / "curriculum" / "big-ideas-middle-school-sc6-workbook.md"
OUT_DIR = DOCS_DIR / "downloads" / "worksheets"
STUDENT_PDF = OUT_DIR / "bigideas_middle_school_sc6_daily_student_workbook.pdf"
TEACHER_PDF = OUT_DIR / "bigideas_middle_school_sc6_teacher_coach_guide.pdf"

FONT_BODY = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_ITALIC = "Helvetica-Oblique"
FONT_MONO = "Courier"
FONT_MONO_BOLD = "Courier-Bold"

try:
    if (FONT_DIR / "SpaceMono-Regular.ttf").exists():
        pdfmetrics.registerFont(TTFont("SpaceMono", str(FONT_DIR / "SpaceMono-Regular.ttf")))
        pdfmetrics.registerFont(TTFont("SpaceMono-Bold", str(FONT_DIR / "SpaceMono-Bold.ttf")))
        FONT_MONO = "SpaceMono"
        FONT_MONO_BOLD = "SpaceMono-Bold"
    arial_dir = Path("/System/Library/Fonts/Supplemental")
    if (arial_dir / "Arial.ttf").exists() and (arial_dir / "Arial Bold.ttf").exists():
        pdfmetrics.registerFont(TTFont("BookSans", str(arial_dir / "Arial.ttf")))
        pdfmetrics.registerFont(TTFont("BookSans-Bold", str(arial_dir / "Arial Bold.ttf")))
        italic_ttf = arial_dir / ("Arial Italic.ttf" if (arial_dir / "Arial Italic.ttf").exists() else "Arial.ttf")
        pdfmetrics.registerFont(TTFont("BookSans-Italic", str(italic_ttf)))
        FONT_BODY = "BookSans"
        FONT_BOLD = "BookSans-Bold"
        FONT_ITALIC = "BookSans-Italic"
except Exception as exc:
    print(f"[WARN] Font registration fallback: {exc}")


# Canonical 45-Day Spiral Revisit Path, 30-Sec Zero-Fail Starter, Rotating Game Mode, and Twin-Way Bonus Map
SPIRAL_REVISIT_MAP: Dict[int, Dict[str, str]] = {
    1: {
        "spiral": "Thread A (Factor & Split) • [🔨 VISIT 1: BUILDER WAY — Launch of Thread A]",
        "game_mode": "⚡ Mode C: Human vs. Screen Prediction",
        "starter": "Grab **7 Counting Tiles** and make groups of **2**. You see **3 pairs** and **1 leftover**! Now press `7 {{key:ENTER}} 2 {{key:÷R}}` on your SC-6—watch `X: 3` and `Y: 1` pop up together! (`[ ] +5 Spark XP!`)",
        "why_new": "Phone calculators spit out ugly decimals like `16.875` that hide the real leftover items. Building tile rows (`🔨`) shows what a remainder actually is, and `{{key:÷R}}` (`🚀`) handles huge numbers in 1 click!",
        "twin": "**Way A (`🚀` `{{key:÷R}}` Key):** `115 {{key:ENTER}} 14 {{key:÷R}}` -> `8 R 3` (so **9 vans**). **Way B (`⚡` Multiply-Up Table):** `14 {{key:ENTER}} 8 {{key:×}}` = `112` (3 kids left!) vs `14 {{key:ENTER}} 9 {{key:×}}` = `126` (all 115 fit -> **9 vans**)!",
    },
    2: {
        "spiral": "Thread C (Scale & Growth) • [🔨 VISIT 1: BUILDER WAY — 2D/3D Tile Arrays -> REP Ladder]",
        "game_mode": "🕵️ Mode A: Spot the Glitch ('2^3 = 6 or 8?')",
        "starter": "Leo says $2^3 = 6$. Snap a $2 \\times 2 \\times 2$ cube of blocks (8 blocks!) and press `2 {{key:x³}}` (`[g][x²]`). Screen says **`8`**! You just busted the #1 6th-grade math myth in 15 seconds! (`[ ] +5 Spark XP!`)",
        "why_new": "Building a 2D square ($4^2=16$) or 3D cube ($4^3=64$) with physical tiles (`🔨`) cures the '$4^3=12$' trap forever, while the `{{key:REP}}` ladder (`⚡`) and `{{key:yˣ}}` (`🚀`) take over when powers grow too huge for your desk!",
        "twin": "**Way A (`⚡` `{{key:REP}}` Cube Ladder):** `6 {{key:REP}} {{key:×}} {{key:×}}` = `216` (edge = **6**). **Way B (`🚀` Cube Root `{{key:ˣ√y}}`):** `216 {{key:ENTER}} 3 {{key:ˣ√y}}` = **6**!",
    },
    3: {
        "spiral": "Thread D (Inside-Out Chunking) • [🔨 VISIT 1: BUILDER WAY — Launch of Thread D]",
        "game_mode": "🎯 Mode B: Mystery Target (2-Room Elevator)",
        "starter": "Put **5 tiles** on the left of your desk and **2 rows of 3 tiles** ($6$) on the right. Total is **11**! Now type `5 {{key:ENTER}} 2 {{key:ENTER}} 3 {{key:×}}`—see `Y: 5` waiting while `X: 6` finishes! Press `{{key:+}}` -> **`11`**! (`[ ] +5 Spark XP!`)",
        "why_new": "Rewriting 5 lines of PEMDAS by hand causes copying mistakes. Grouping tiles into separate 'rooms' (`🔨`) and solving inside-out on the 4-line elevator (`🚀`) lets Floor 2 (`Y`) hold Room 1 while you solve Room 2 on Floor 1 (`X`)!",
        "twin": "**Way A (`🚀` Inside-Out 4-Stack):** `10 {{key:ENTER}} 15 {{key:ENTER}} 3 {{key:-}} {{key:x²}} 9 {{key:÷}} {{key:+}}` = **26**. **Way B (`🔨` 2-Room Chunking):** Room 1 = `10`, Room 2 = `144 ÷ 9 = 16` -> `10 + 16` = **26**!",
    },
    4: {
        "spiral": "Thread A (Factor & Split) • [⚡ VISIT 2: PATTERN WAY — Revisits Day 1 Tile Splitting]",
        "game_mode": "🔄 Mode D: 2-Second Shortcut Race (`{{key:FACT}}`)",
        "starter": "Stack a red **`2` block** (`12.6mm`), another **`2` block**, and a green **`3` block** (`20.0mm`). Their height matches the **`12` tower** ($2 \\times 2 \\times 3 = 12$)! Now type `12 {{key:ENTER}} {{key:FACT}}` -> screen says **`2^2 × 3`**! (`[ ] +5 Spark XP!`)",
        "why_new": "On Day 1 we split numbers into equal rows one divisor at a time. When you want the deepest 'DNA building blocks' of a number without drawing lopsided paper factor trees, snap Prime Towers (`🔨`) or press `{{key:FACT}}` (`🚀`)!",
        "twin": "**Way A (`⚡` Split-in-Chunks Tree):** $180 = 18 \\times 10 = (2 \\cdot 3^2) \\times (2 \\cdot 5) = 2^2 \\cdot 3^2 \\cdot 5$. **Way B (`🚀` SC-6 `{{key:FACT}}` Key):** `180 {{key:ENTER}} {{key:FACT}}` -> **`2^2 × 3^2 × 5`**!",
    },
    5: {
        "spiral": "Thread A (Factor & Split) • [🚀 VISIT 3: STACK HACKER WAY — Boss Revisit of Days 1 & 4]",
        "game_mode": "🎲 Mode E: Speed Pack Challenge (`{{key:GCF}}` & `{{key:LCM}}`)",
        "starter": "Stand the Prime Towers for **`12`** ($2,2,3$) and **`18`** ($2,3,3$) next to each other. Both share one `2` and one `3` ($2 \\times 3 = 6$)! Now press `12 {{key:ENTER}} 18 {{key:GCF}}` -> **`6`** in 1 second! (`[ ] +5 Spark XP!`)",
        "why_new": "Listing every factor by hand works for `6` and `8`, but for `36` and `48` you'll miss factors and waste 10 minutes! Laying Day 4's Prime Towers side-by-side (`🔨`) shows *why* GCF is the shared overlap, and `{{key:GCF}}`/`{{key:LCM}}` (`🚀`) solves it in 2 clicks!",
        "twin": "**Way A (`⚡` `{{key:REP}}` Skip-Count Race):** Step `12 {{key:REP}} {{key:+}}...` (`12, 24, 36, 48, 60`) vs `15 {{key:REP}} {{key:+}}...` (`15, 30, 45, 60`). **Way B (`🚀` `{{key:LCM}}` Key):** `12 {{key:ENTER}} 15 {{key:LCM}}` = **60**!",
    },
    6: {
        "spiral": "Thread B (Flip & Inverse) + Thread A Boomerang • [🔨 VISIT 1: BUILDER WAY — Revisits Day 5 GCF]",
        "game_mode": "⚡ Mode C: Same-Height Tower Match (`{{key:SIMP}}`)",
        "starter": "Hold one **`1/2` tower** (`42mm`) next to three **`1/6` blocks** (`3 × 14mm = 42mm`). Exact same height! Now type `{{key:.}} 3 {{key:.}} 6 {{key:ENTER}} {{key:SIMP}}`—watch `3/6` snap into **`1/2`**! (`[ ] +5 Spark XP!`)",
        "why_new": "In Chapter 1 (`Day 5`), you learned `{{key:GCF}}`. Today that exact skill boomerangs back! Simplifying a fraction is just dividing top and bottom by their GCF—or matching 84mm Fraction Towers (`🔨`) side-by-side and pressing `{{key:SIMP}}` (`🚀`)!",
        "twin": "**Way A (`🔨` 84mm Tower Swap):** Swap $1/3$ (`28mm`) for four $1/12$ blocks and $1/4$ (`21mm`) for three $1/12$ blocks -> **`7/12`**. **Way B (`🚀` SC-6 Fraction Stack):** `{{key:.}} 1 {{key:.}} 3 {{key:ENTER}} {{key:.}} 1 {{key:.}} 4 {{key:+}}` = **`7/12`**!",
    },
    7: {
        "spiral": "Thread B (Flip & Inverse) • [⚡ VISIT 2: PATTERN WAY — Revisits Day 6 Fraction Towers]",
        "game_mode": "🕵️ Mode A: Prediction Bet ('Does × Make It Bigger or Smaller?')",
        "starter": "Take two **`1/3` blocks** ($2/3$). Hand **half** of them ($1/2$ of $2/3$) to a friend—you're holding just **one `1/3` block**! Key `{{key:.}} 1 {{key:.}} 2 {{key:ENTER}} {{key:.}} 2 {{key:.}} 3 {{key:×}}` -> **`1/3`**! (`[ ] +5 Spark XP!`)",
        "why_new": "Adding fractions (`Day 6`) required common denominators. Multiplying fractions is way faster once you see with 84mm blocks (`🔨`) that '$1/2$ of $2/3$' just means taking 1 of the 2 thirds—and cross-canceling (`⚡`) shrinks big numbers before you even multiply!",
        "twin": "**Way A (`⚡` Cross-Cancel Pattern):** In $\\frac{4}{5} \\times \\frac{5}{6} \\times \\frac{3}{4}$, cancel the `5`s and `4`s first -> $3/6 =$ **`1/2`**. **Way B (`🚀` Direct Stack Multiply):** Multiply all three on the SC-6 -> **`1/2`**!",
    },
    8: {
        "spiral": "Thread B (Flip & Inverse) • [🚀 VISIT 3: STACK HACKER WAY — Boss Revisit of Days 1, 6 & 7]",
        "game_mode": "🔄 Mode D: 2-Second Shortcut Race (`{{key:1/x}}` Flip)",
        "starter": "How many **`1/4` blocks** fit next to one **`1/2` block**? Lay them down: **2 fit**! Now type `{{key:.}} 1 {{key:.}} 2 {{key:ENTER}} {{key:.}} 1 {{key:.}} 4 {{key:÷}}` -> **`2`**! Dividing by $1/4$ is the same as multiplying by $4$! (`[ ] +5 Spark XP!`)",
        "why_new": "On small problems like $\\frac{3}{4} \\div \\frac{1}{8}$, laying $\\frac{1}{8}$ blocks (`🔨`) along a $\\frac{3}{4}$ bar is super clear (6 fit!). But for $6\\frac{3}{4} \\div \\frac{3}{4}$, you don't want to count 27 plastic fourths—flipping the divisor with `{{key:1/x}}` (`🚀`) turns division into Day 7's fast multiplication!",
        "twin": "**Way A (`⚡` Common-Denominator Fourths):** $6\\frac{3}{4} = \\frac{27}{4}$, and $27 \\text{ fourths} \\div 3 \\text{ fourths} =$ **9**. **Way B (`🚀` Reciprocal Flip `{{key:1/x}}`):** `6 {{key:.}} 3 {{key:.}} 4 {{key:ENTER}} {{key:.}} 3 {{key:.}} 4 {{key:1/x}} {{key:×}}` = **9 shelves**!",
    },
    9: {
        "spiral": "Thread B (Flip & Inverse) • [⚡ VISIT 2: PATTERN WAY — Revisits Day 6 Mixed Numbers]",
        "game_mode": "🎯 Mode B: Split the Whole & Decimal (`{{key:IP}}` & `{{key:FP}}`)",
        "starter": "Type `14.75 {{key:ENTER}}` and press `{{key:IP}}` (`[f][PV]`)—it grabs the whole **`14`**! Press `{{key:LASTX}} {{key:FP}}` (`[g][PV]`)—it grabs the decimal **`.75`**! Zero crooked paper columns! (`[ ] +5 Spark XP!`)",
        "why_new": "Lining up decimal points by hand on lined paper is frustrating when columns drift. Splitting wholes and tenths with `{{key:IP}}` and `{{key:FP}}` (`🔨`) or entering decimals directly on the stack (`🚀`) keeps place value locked automatically!",
        "twin": "**Way A (`🚀` Decimal Stack):** `4.75 {{key:ENTER}} 1.2 {{key:×}}` = **`5.7`**. **Way B (`⚡` Fraction Costume via `{{key:FDISP}}`):** $4\\frac{3}{4} \\times 1\\frac{1}{5} = \\frac{19}{4} \\times \\frac{6}{5} = \\frac{57}{10} =$ **`5 7/10`**!",
    },
    10: {
        "spiral": "Thread A & B Boomerang • [🔄 VISIT 4: CROSS-CHAPTER BOOMERANG — Revisits Days 1, 6, 8 & 9]",
        "game_mode": "🔄 Mode D: 1-Thumb Costume Change (`{{key:FDISP}}`)",
        "starter": "Type `15 {{key:ENTER}} 4 {{key:÷}}` (`3.75`). Now tap `{{key:FDISP}}` three times: watch **`3.75`** morph into **`3 3/4`**, then **`15/4`**, then **`3 R 3`**! Four textbook answers with 1 thumb! (`[ ] +5 Spark XP!`)",
        "why_new": "Moving the decimal scoop in long division is easy to mess up. Today connects **4 earlier days at once**: decimal division (`Day 10`), fraction division (`Day 8`), mixed numbers (`Day 6`), and remainders (`Day 1`)—using `{{key:FDISP}}` to switch between them in 1 click!",
        "twin": "**Way A (`🚀` Decimal Division):** `4.5 {{key:ENTER}} 0.75 {{key:÷}}` = **6 laps**. **Way B (`🔨` Fraction Tower Equivalent from Day 8):** $4\\frac{1}{2} \\div \\frac{3}{4} = \\frac{9}{2} \\times \\frac{4}{3} =$ **6 laps**!",
    },
    11: {
        "spiral": "Thread C (Scale & Ratio) • [🔨 VISIT 1: BUILDER WAY — Revisits Day 6 Fraction Bars]",
        "game_mode": "🎯 Mode B: Mystery Box Weight (Tape Diagram)",
        "starter": "Put **2 Blue tiles** and **3 Gold tiles** on your desk ($5$ tiles total). If all $5$ tiles weigh $20\\text{g}$, each tile is **$4\\text{g}$**! Now type `12 {{key:ENTER}} 18 {{key:a:b}}` -> watch it simplify to **`2:3`**! (`[ ] +5 Spark XP!`)",
        "why_new": "Students often confuse Part-to-Part ($3:2$) with Part-to-Whole ($3/5$). Building 2 rows of colored Counting Tiles (`🔨`) lets you physically see both the two parts AND the combined total bar before pressing `{{key:a:b}}` (`🚀`)!",
        "twin": "**Way A (`🔨` Tile Gap Model):** $7 \\text{ parts} - 4 \\text{ parts} = 3 \\text{ extra parts} = 18 \\to 1 \\text{ part} = 6 \\to 11 \\text{ parts} =$ **66**. **Way B (`🚀` Stack Ratio):** `18 {{key:ENTER}} 3 {{key:÷}} 11 {{key:×}}` = **66 guitars**!",
    },
    12: {
        "spiral": "Thread C (Scale & Ratio) • [⚡ VISIT 2: PATTERN WAY — Revisits Day 2 REP & Day 11 Tape Diagrams]",
        "game_mode": "🔄 Mode D: 5-Second Ratio Table Sprint (`{{key:REP}}`)",
        "starter": "Type `4 {{key:REP}}` (`[g][ENTER]`) and tap `{{key:+}}` four times: watch **`8 -> 12 -> 16 -> 20`** march across the screen! You just built a 5-column ratio row in 3 seconds! (`[ ] +5 Spark XP!`)",
        "why_new": "On Day 11, laying out tiles (`🔨`) worked great for small numbers. But if a ratio table jumps to 10 or 15 batches, you don't want to count 90 plastic tiles! Using Day 2's `{{key:REP}}` constant key (`⚡`) lets you skip-count an entire ratio table in 5 seconds!",
        "twin": "**Way A (`⚡` Scale Down to 2 Tickets):** $6 \\text{ tickets} = \\$45 \\to 2 \\text{ tickets} = \\$15 \\to 10 \\text{ tickets} (5 \\times 2) =$ **$75**. **Way B (`🚀` Unit Rate Stack):** `45 {{key:ENTER}} 6 {{key:÷}} 10 {{key:×}}` = **$75**!",
    },
    13: {
        "spiral": "Thread C & B Boomerang • [🚀 VISIT 3: STACK HACKER WAY — Revisits Days 8, 11 & 12]",
        "game_mode": "🕵️ Mode A: Best-Buy Store Showdown (`{{key:x⇄y}}` Rescue)",
        "starter": "Oops—you typed `5 {{key:ENTER}} 15` instead of `15 {{key:ENTER}} 5`! Don't clear it—just press `{{key:x⇄y}}` (`[f][R↓]`) to swap Floors 1 & 2, then press `{{key:÷}}` -> **`3`**! (`[ ] +5 Spark XP!`)",
        "why_new": "Tape diagrams (`Day 11`) and skip-counting tables (`Day 12`) get stuck when comparing weird pack sizes like `8 oz for $3.60` vs `12 oz for $5.04`. Dividing down to **1 single unit** (`🚀` Unit Rate) works on *any* two numbers—and `{{key:x⇄y}}` rescues you if you enter them upside-down!",
        "twin": "**Way A (`🚀` Unit Rate `mm/s`):** `45 {{key:ENTER}} 15 {{key:÷}}` = $3\\text{ mm/s} \\times 60\\text{ s} =$ **180 mm**. **Way B (`⚡` Ratio Table Scaling from Day 12):** $60\\text{ s}$ is $4 \\times 15\\text{ s}$, so $4 \\times 45\\text{ mm} =$ **180 mm**!",
    },
    14: {
        "spiral": "Thread C (Scale & Ratio) • [🔄 VISIT 4: CROSS-CHAPTER BOOMERANG — Revisits Day 10 FDISP & Day 11 Ratios]",
        "game_mode": "⚡ Mode C: 3-Costume Instant Reveal (`{{key:▸%}}`)",
        "starter": "Hold up the **`1/4` Fraction Tower**. You know 1 quarter is **25 cents** ($25\\%$). Now type `{{key:.}} 1 {{key:.}} 4 {{key:ENTER}} {{key:▸%}}` (`[f][%]`)—screen says **`25%`**! (`[ ] +5 Spark XP!`)",
        "why_new": "Percents aren't a brand-new topic—they are just Day 11 ratios locked to a denominator of `100`! Instead of memorizing 6 rules for moving decimal points left or right, use `{{key:▸%}}` and `{{key:FDISP}}` (`🚀`) to see all 3 costumes of the same number!",
        "twin": "**Way A (`⚡` All-Decimals Lineup):** $60\\% = 0.60$, $0.61$, $\\frac{5}{8} = 0.625$. **Way B (`🚀` All-Percents via `{{key:▸%}}`):** $60\\% < 61\\% < 62.5\\%$. Both prove **`60%, 0.61, 5/8`**!",
    },
    15: {
        "spiral": "Thread C (Scale & Ratio) • [🚀 VISIT 5: BOSS BOOMERANG — Revisits Days 11–14]",
        "game_mode": "🔄 Mode D: 2-Key Sale Price Hack (`{{key:%}}` & `{{key:%CHG}}`)",
        "starter": "A $\\$50$ hoodie is **$20\\%$ off**. Type `50 {{key:ENTER}} 20 {{key:%}}`—Floor 1 shows the **`$10`** discount while **`$50`** waits on Floor 2! Press `{{key:-}}` -> **`$40`** sale price! (`[ ] +5 Spark XP!`)",
        "why_new": "Finding a sale price usually takes two separate steps (find discount, then subtract). Today you compare two pro ways: subtracting the `{{key:%}}` discount on `Y | X` (`🚀`) vs multiplying by the remaining percent (`⚡`), plus 1-click unit conversions (`{{key:▸cm}}`, `{{key:▸kg}}`)!",
        "twin": "**Way A (`🚀` 1-Click Converter Keys):** `32 {{key:▸cm}}` = **`81.28 cm`** and `5 {{key:▸kg}}` = **`2.27 kg`**. **Way B (`⚡` Unit-Rate Multiply from Day 13):** `32 {{key:ENTER}} 2.54 {{key:×}}` = **`81.28 cm`**!",
    },
    16: {
        "spiral": "Thread D (Inside-Out Chunking) • [⚡ VISIT 2: PATTERN WAY — Revisits Day 3 4-Stack Order of Operations]",
        "game_mode": "🎲 Mode E: Secret Variable Box Drop (`ALGB-01`)",
        "starter": "Drop **4 unit cubes** into the green **`x` box**. Now 'read' $2x + 3$: two boxes ($8$) plus $3$ = **`11`**! Key `2 {{key:ENTER}} 4 {{key:×}} 3 {{key:+}}` -> **`11`**! Algebra is just a box with a number inside! (`[ ] +5 Spark XP!`)",
        "why_new": "Algebra letters (`x`, `y`) look scary until you realize a variable is just an empty green box (`ALGB-01`) waiting for a number! Once you drop the number into the box (`🔨`), evaluating $3x^2 - 5$ is literally just Day 3's elevator math (`🚀`)!",
        "twin": "**Way A (`🚀` Inside-Out Formula Stack):** `4.5 {{key:ENTER}} 4 {{key:×}} 8 {{key:+}}` = **$26**. **Way B (`🔨` Repeat Addition Table from Day 12):** $\\$8 + \\$4.50 + \\$4.50 + \\$4.50 + \\$4.50 = \\$8 + \\$18 =$ **$26**!",
    },
    17: {
        "spiral": "Thread D (Inside-Out Chunking) • [🔨 VISIT 1: BUILDER WAY — Tactile Like-Term Sorting]",
        "game_mode": "🕵️ Mode A: Spot the Glitch ('Does 3x + 2 = 5x?')",
        "starter": "Put **3 green $x$-rods** and **2 yellow unit cubes** on your desk. Are there 5 green rods? **NO!** Now test $x=10$ on your SC-6: $3(10)+2 = 32$, while $5(10) = 50$! Different shapes never merge! (`[ ] +5 Spark XP!`)",
        "why_new": "On paper, kids constantly add $3x + 5$ and write $8x$. Once you hold a green $x$-rod ($42\\text{ mm}$) and a small yellow $1$-cube ($14\\text{ mm}$) (`🔨`), your hands see why they can't merge—and plugging a test number into the SC-6 (`🚀`) proves your simplified expression matches!",
        "twin": "**Way A (`🔨` Sort All 4 Sides by Tile Shape):** $(2x+2x+x+x) + (3+3+5+5) =$ **`6x + 16`**. **Way B (`🚀` Numerical Twin Proof at $x=10$):** Original $2(23) + 2(15) = 76$ == Simplified $6(10) + 16 =$ **76**!",
    },
    18: {
        "spiral": "Thread D (Inside-Out Chunking) • [⚡ VISIT 2: PATTERN WAY — Revisits Day 3 Grouping & Day 17 Tiles]",
        "game_mode": "⚡ Mode C: Split-Rectangle Twin Match ($a(b+c)$)",
        "starter": "Build **2 rows** of **(1 green $x$-rod + 3 yellow cubes)**. Count by rows: $2(x+3)$. Count by color piles: **`2x + 6`**! Same blocks on your desk, two ways to name them! (`[ ] +5 Spark XP!`)",
        "why_new": "Why does $3(x + 4) = 3x + 12$? Because whether you measure the whole rectangle at once (`Way A`) or split it into two rooms (`Way B`), the total tile count never changes! This is the #1 place in middle school where two approaches prove each other.",
        "twin": "**Way A (`🔨` Distribute & Sort Tiles):** $5(2x+3) + 4x = 10x + 15 + 4x =$ **`14x + 15`**. **Way B (`🚀` Numerical Twin Proof at $x=2$):** Original $5(7) + 8 =$ **43** == Simplified $14(2) + 15 =$ **43**!",
    },
    19: {
        "spiral": "Thread A & D Boomerang • [🔄 VISIT 4: CROSS-CHAPTER BOOMERANG — Revisits Day 5 GCF & Day 18 Distributive]",
        "game_mode": "🎯 Mode B: Reverse the Rectangle (`{{key:GCF}}` Unlock)",
        "starter": "Take **4 green $x$-rods** and **6 yellow cubes** ($4x + 6$). Arrange them into **2 identical rows**—each row has **`2x + 3`**! Now press `4 {{key:ENTER}} 6 {{key:GCF}}` -> **`2`** (the number of rows)! (`[ ] +5 Spark XP!`)",
        "why_new": "Remember `{{key:GCF}}` from Chapter 1 (`Day 5`)? Today it boomerangs back to unlock Algebra! Factoring $45x - 30$ isn't a brand-new process—it's just running Day 18's Distributive Property in reverse using Day 5's `{{key:GCF}}` key (`🚀`)!",
        "twin": "**Way A (`🚀` SC-6 `{{key:GCF}}` Pull-Out):** `45 {{key:ENTER}} 30 {{key:GCF}}` = `15` -> **`15(3x - 2)`**. **Way B (`⚡` Multiply Back Out from Day 18):** $15 \\times 3x = 45x$ and $15 \\times 2 = 30 \\to$ **`45x - 30`**!",
    },
    20: {
        "spiral": "Thread D (Inside-Out Chunking) • [🔨 VISIT 1: BUILDER WAY — Geometric Area Arrays]",
        "game_mode": "🕵️ Mode A: Slant-Side Trap Detector (`{{key:RECT}}`)",
        "starter": "Snap a **5 by 3 rectangle** of tiles (15 tiles). Press `5 {{key:ENTER}} 3 {{key:RECT}}` (`[f][1]`) -> **`15`**! Even if you slant the stack sideways into a parallelogram, did the number of plastic tiles change? **Never!** (`[ ] +5 Spark XP!`)",
        "why_new": "Kids accidentally multiply the slanted side of a parallelogram instead of the straight height. Sliding the corner triangle on the grid (`🔨`) proves every parallelogram is a disguised rectangle—so `{{key:RECT}}` (`🚀`) solves both!",
        "twin": "**Way A (`🚀` Inverse Division):** `168 {{key:ENTER}} 12 {{key:÷}}` = **`14 in`**. **Way B (`⚡` Forward `{{key:RECT}}` Proof):** `14 {{key:ENTER}} 12 {{key:RECT}}` = **`168 in²`**!",
    },
    21: {
        "spiral": "Thread D (Inside-Out Chunking) • [⚡ VISIT 2: PATTERN WAY — Revisits Day 20 Parallelogram/Rectangle]",
        "game_mode": "🔄 Mode D: Half-a-Rectangle Shortcut (`{{key:TRI}}`)",
        "starter": "A **6 by 4 rectangle** has area **`24`** (`6 {{key:ENTER}} 4 {{key:RECT}}`). Cut it corner-to-corner into two identical triangles—each triangle is half of 24 = **`12`**! Now press `6 {{key:ENTER}} 4 {{key:TRI}}` (`[g][1]`) -> **`12`**! (`[ ] +5 Spark XP!`)",
        "why_new": "Why does a triangle have a $\\div 2$ in its formula when a rectangle (`Day 20`) doesn't? Putting two identical triangles together on the tray (`🔨`) always forms a Day 20 parallelogram! You can use `{{key:RECT}} 2 {{key:÷}}` (`⚡`) OR the 1-click `{{key:TRI}}` key (`🚀`)!",
        "twin": "**Way A (`🚀` Double-Area Then Divide):** `60 {{key:ENTER}} 2 {{key:×}} 15 {{key:÷}}` = **`8 in`**. **Way B (`⚡` `{{key:TRI}}` Key Verification):** `15 {{key:ENTER}} 8 {{key:TRI}}` = **`60 in²`**!",
    },
    22: {
        "spiral": "Thread D (Inside-Out Chunking) • [🚀 VISIT 3: STACK HACKER WAY — Boss Revisit of Days 3, 20 & 21]",
        "game_mode": "🎯 Mode B: Multi-Room Memory Vault (`{{key:Σ+}}` & `{{key:Σx}}`)",
        "starter": "Press `{{key:CLΣ}}` (`[g][÷]`). Toss a rectangle `4 {{key:ENTER}} 5 {{key:RECT}} {{key:Σ+}}` (`20`) and a triangle `4 {{key:ENTER}} 3 {{key:TRI}} {{key:Σ+}}` (`6`) into memory. Press `{{key:Σx}}` (`[f][7]`) -> **`26`** total area! (`[ ] +5 Spark XP!`)",
        "why_new": "Memorizing the trapezoid formula is annoying—and what if an L-shape has 4 rooms? Instead of writing a giant equation, chop any weird shape into simple rectangles (`Day 20`) and triangles (`Day 21`) and toss each piece into `{{key:Σ+}}` (`🚀`)!",
        "twin": "**Way A (`🚀` Outer Minus Cutout Hole):** `10 {{key:ENTER}} 8 {{key:RECT}}` (`80`) minus `6 {{key:ENTER}} 4 {{key:RECT}}` (`24`) = **`56 in²`**. **Way B (`🔨` 4 Border Strips Sum via `{{key:Σ+}}`):** $20 + 20 + 8 + 8 =$ **`56 in²`**!",
    },
    23: {
        "spiral": "Thread A & C Boomerang • [🔄 VISIT 4: CROSS-CHAPTER BOOMERANG — Revisits Day 1 Modulo-60 & Day 10 Decimals]",
        "game_mode": "⚡ Mode C: Planetary Clock Gear Spin (`{{key:🕒}}`)",
        "starter": "Spin the minute hand on your **Planetary Clock (`TIME-01`)** by **30 minutes** ($1/2$ turn). Type `1.30 {{key:▸HR}}` (`[g][9]`) on the SC-6—watch `1 hr 30 min` turn into **`1.5 hours`**! (`[ ] +5 Spark XP!`)",
        "why_new": "Subtracting time on paper (`1:20 PM - 11:45 AM`) fails if you borrow `100` instead of `60`. Spinning the Planetary Geared Clock (`🔨`) shows the 60-minute gear ratio physically, while `{{key:🕒}}` and `{{key:▸HR}}` (`🚀`) convert `3 hr 15 min` into `3.25 hr` automatically!",
        "twin": "**Way A (`🚀` `{{key:▸HR}}` Paycheck Shortcut):** `3.15 {{key:▸HR}}` = `3.25 hr` $\\times \\$16 =$ **$52.00**. **Way B (`🔨` Split Hours + Quarter-Hour from Day 6):** $3(\\$$16) = \\$48$ plus $\\frac{1}{4}(\\$$16) = \\$4 \\to$ **$52.00**!",
    },
    24: {
        "spiral": "Thread E (Zero-Pair & Distance) • [🔨 VISIT 1: BUILDER WAY — Launch of Thread E]",
        "game_mode": "🎲 Mode E: Zero-Pair Battle Royale (`{{key:+/-}}`)",
        "starter": "Put **3 Yellow ($+1$)** and **3 Red ($-1$)** counters on your tray—each Yellow+Red pair cancels to **0**! Now type `3 {{key:ENTER}} 3 {{key:+/-}} {{key:+}}` -> **`0`**! (`[ ] +5 Spark XP!`)",
        "why_new": "Negative numbers feel abstract until you hold Yellow ($+1$) and Red ($-1$) counters (`🔨`) that physically cancel in **Zero Pairs**, paired with the SC-6's dedicated `{{key:+/-}}` sign-flipper key (`🚀`)!",
        "twin": "**Way A (`🚀` Running Stack Ledger):** `35 {{key:ENTER}} 50 {{key:+/-}} {{key:+}} 20 {{key:+}}` = **`+$5`**. **Way B (`⚡` Group Positives vs Negatives):** Deposits ($\\$35+\\$20=\\$55$) minus Spend ($\\$50$) = **`+$5`**!",
    },
    25: {
        "spiral": "Thread E (Zero-Pair & Distance) • [⚡ VISIT 2: PATTERN WAY — Revisits Day 14 Ordering & Day 24 Integers]",
        "game_mode": "🕵️ Mode A: Spot the Glitch ('Is -18 Bigger Than -5?')",
        "starter": "Which is warmer: **$-5^\\circ$** or **$-18^\\circ$**? Type `5 {{key:+/-}} {{key:ENTER}} 18 {{key:+/-}} {{key:>}}` (`[f][+]`)—the SC-6 outputs **`1` (TRUE)**! $-5$ is to the right of $-18$, so $-5 > -18$! (`[ ] +5 Spark XP!`)",
        "why_new": "On the negative side of zero, bigger digits mean *colder/smaller* numbers ($-18 < -5$), which tricks your brain! Sliding beads on the Number Rack (`🔨`), checking `{{key:LINE}}` (`⚡`), and testing with `{{key:<}}`/`{{key:>}}` (`🚀`) gives you 3 ways to never get tricked!",
        "twin": "**Way A (`🔨` Number Line Position `{{key:LINE}}`):** Left-to-right order is **`-1 3/4, -1.5, -0.5, 1 1/4`**. **Way B (`🚀` Pairwise `{{key:<}}` Truth Check):** `1.75 {{key:+/-}} {{key:ENTER}} 1.5 {{key:+/-}} {{key:<}}` -> `1` (True)!",
    },
    26: {
        "spiral": "Thread E (Zero-Pair & Distance) • [🚀 VISIT 3: STACK HACKER WAY — Boss Revisit of Days 24 & 25]",
        "game_mode": "⚡ Mode C: Positive Mirror Test (`[|x|]` vs `{{key:+/-}}`)",
        "starter": "Walk **6 steps backward** ($-6$). How many steps did your feet take? **6 steps** (you can't walk negative steps!). Type `6 {{key:+/-}}` and press `[|x|]` (`[f][+/-]`) -> **`6`**! (`[ ] +5 Spark XP!`)",
        "why_new": "Counting steps to zero on a number line (`Day 25`) is easy for $|-4|$, but in multi-step expressions like $50 - |-18|$, kids confuse 'opposite' (`{{key:+/-}}`) with 'distance from zero' (`[|x|]`). Using `[|x|]` on Floor 1 (`X`) while `50` waits on Floor 2 (`Y`) keeps them crystal clear!",
        "twin": "**Way A (`🚀` Elevator Stack):** `50 {{key:ENTER}} 18 {{key:+/-}}` `[|x|]` (`Y: 50 | X: 18`) `{{key:-}}` = **32**. **Way B (`🔨` Distance-First Rewrite):** Distance from $-18$ to $0$ is $+18$, so $50 - 18 =$ **32**!",
    },
    27: {
        "spiral": "Thread E (Zero-Pair & Distance) • [⚡ VISIT 2: PATTERN WAY — Revisits Day 24 Sign Flipping in 2D]",
        "game_mode": "🎯 Mode B: 4-Quadrant Mirror Treasure Hunt",
        "starter": "Start at $(3, 4)$ in Quadrant I. Flip the $x$-sign with `{{key:+/-}}` to $(-3, 4)$—you just jumped across the $y$-axis into Quadrant II! (`[ ] +5 Spark XP!`)",
        "why_new": "Plotting 4 quadrants on paper gets messy when you mix up $(x,y)$ order or reflection signs. Snapping pegs on the Coordinate Baseplate (`🔨`) shows that reflecting across an axis is just pressing `{{key:+/-}}` (`🚀`) on one coordinate!",
        "twin": "**Way A (`🔨` Baseplate Peg Walk):** $(0,-9)$ goes $0$ sideways, $9$ down (**y-axis**); $(-7,0)$ goes $7$ left, $0$ up/down (**x-axis**). **Way B (`⚡` Zero-Coordinate Rule):** $x=0 \\to$ **y-axis**; $y=0 \\to$ **x-axis**!",
    },
    28: {
        "spiral": "Thread E & D Boomerang • [🔄 VISIT 4: CROSS-CHAPTER BOOMERANG — Revisits Day 20 Perimeter & Day 26 |x|]",
        "game_mode": "🔄 Mode D: Bridge Builder Distance Race (`[|x|]`)",
        "starter": "How far is $-3$ from $+4$? It's **3 steps** to zero plus **4 steps** past zero = **`7`**! Now type `3 {{key:+/-}} {{key:ENTER}} 4 {{key:-}}` `[|x|]` -> **`7`** in 2 clicks! (`[ ] +5 Spark XP!`)",
        "why_new": "Counting grid squares one by one works when points are 4 units apart, but what if a bridge spans from $(-45, 12)$ to $(80, 12)$? Using Day 26's absolute value distance (`[|x|]`) finds the span across *any* two coordinates in 2 clicks!",
        "twin": "**Way A (`🔨` Add Distances to Axis):** Width $= |-4| + |5| = 9$; Height $= |6| + |-2| = 8 \\to P = 2(9+8) =$ **34**. **Way B (`🚀` Coordinate Subtraction + `[|x|]`):** `|-4 - 5| = 9` and `|6 - (-2)| = 8` -> Perimeter = **34**!",
    },
    29: {
        "spiral": "Thread F (Balance & Fair Share) • [🔨 VISIT 1: BUILDER WAY — Launch of Thread F]",
        "game_mode": "🕵️ Mode A: Balance Scale Lie Detector (`{{key:≠}}`)",
        "starter": "Does $x = 5$ solve $x + 4 = 9$? Type `5 {{key:ENTER}} 4 {{key:+}}` (`9`), then `9 {{key:≠}}` (`[g][-]`). The screen says **`0`** (Zero difference = Perfectly Balanced)! (`[ ] +5 Spark XP!`)",
        "why_new": "Before learning formal equation-solving steps, you can test whether a number is the solution just by dropping it onto the Algebra Stage (`🔨`) or checking `{{key:≠}}` (`🚀`) to see if both sides weigh the exact same!",
        "twin": "**Way A (`🚀` Inverse Undo):** Equation is $n - 8 = 25 \\to$ `25 {{key:ENTER}} 8 {{key:+}}` = **33**. **Way B (`🔨` Plug-In Balance Proof from Day 16):** Test $n=33 \\to 33 - 8 = 25$ (Balanced!)!",
    },
    30: {
        "spiral": "Thread F & B Boomerang • [⚡ VISIT 2: PATTERN WAY — Revisits Day 8 Inverse & Day 29 Balance]",
        "game_mode": "🎯 Mode B: Mystery Box Unwrap + `{{key:LASTX}}` Bounce-Back",
        "starter": "A mystery box plus **5 cubes** weighs **12 cubes** ($x + 5 = 12$). Take **5 cubes off both sides**: `12 {{key:ENTER}} 5 {{key:-}}` -> **`x = 7`**! Now press `{{key:LASTX}} {{key:+}}`—watch **`12`** bounce right back! (`[ ] +5 Spark XP!`)",
        "why_new": "Guessing-and-checking (`Day 29`) works for easy whole numbers, but good luck guessing $m + \\frac{3}{8} = \\frac{5}{6}$! Sweeping blocks off both pans (`🔨`) shows *why* the inverse operation (`{{key:-}}` or `{{key:+}}`) isolates the variable in 1 step, and `{{key:LASTX}}` (`🚀`) proves it!",
        "twin": "**Way A (`🚀` Fraction Stack Undo):** `{{key:.}} 5 {{key:.}} 6 {{key:ENTER}} {{key:.}} 3 {{key:.}} 8 {{key:-}}` = **`11/24`**. **Way B (`⚡` Common-Denominator 24ths from Day 6):** $\\frac{20}{24} - \\frac{9}{24} =$ **`11/24`**!",
    },
    31: {
        "spiral": "Thread F, A & B Boomerang • [🚀 VISIT 3: STACK HACKER WAY — Boss Revisit of Days 8, 29 & 30]",
        "game_mode": "🔄 Mode D: Twin-Method Showdown (`{{key:÷}}` vs `{{key:1/x}}`)",
        "starter": "**3 identical $x$-rods** weigh **15 cubes** ($3x = 15$). Split 15 into 3 equal piles: `15 {{key:ENTER}} 3 {{key:÷}}` -> **`x = 5`**! Press `{{key:LASTX}} {{key:×}}` -> **`15`**! (`[ ] +5 Spark XP!`)",
        "why_new": "When an equation has a fraction coefficient like $\\frac{2}{5}n = 16$, kids freeze up. Today you discover two awesome ways that give the exact same answer: dividing by $\\frac{2}{5}$ (`Way A`) OR using Day 8's Reciprocal Flip `{{key:1/x}}` (`Way B`)!",
        "twin": "**Way A (`🚀` Direct Fraction Divide):** `16 {{key:ENTER}} {{key:.}} 2 {{key:.}} 5 {{key:÷}}` = **40**. **Way B (`⚡` Reciprocal Flip `{{key:1/x}}` from Day 8):** `16 {{key:ENTER}} {{key:.}} 2 {{key:.}} 5 {{key:1/x}} {{key:×}}` ($16 \\times \\frac{5}{2}$) = **40**!",
    },
    32: {
        "spiral": "Thread F & E Boomerang • [🔄 VISIT 4: CROSS-CHAPTER BOOMERANG — Revisits Day 25 Number Line & Day 29 Balance]",
        "game_mode": "⚡ Mode C: Coaster Height Truth Detector (`{{key:≥}}` & `{{key:≤}}`)",
        "starter": "You need **at least 54 inches** ($h \\ge 54$) to ride. Are 54 inches enough? Type `54 {{key:ENTER}} 54 {{key:≥}}` (`[f][×]`) -> **`1` (TRUE, Ride On!)** (`[ ] +5 Spark XP!`)",
        "why_new": "Inequalities ($>, <, \\ge, \\le$) have infinitely many solutions! Combining Day 30–31's Balance Undo (`⚡`) with Day 25's SC-6 Truth Detector keys (`{{key:≥}}`, `{{key:≤}}` `🚀`) lets you solve AND test boundary numbers in seconds!",
        "twin": "**Way A (`🚀` Truth-Detector Plug-In):** Test $x=4,5,6$ in $4x - 3 \\ge 17$: at $x=5$, `17 >= 17` (`1 = True`). **Way B (`⚡` Balance Solve First):** $4x \\ge 20 \\to x \\ge 5$, so **`{5, 6}`** work!",
    },
    33: {
        "spiral": "Thread C & F Boomerang • [🔄 VISIT 5: CROSS-CHAPTER BOOMERANG — Revisits Day 12 REP, Day 16 Formulas & Day 27 Graphs]",
        "game_mode": "🎲 Mode E: Function Machine Table Builder (`{{key:REP}}`)",
        "starter": "Each level gives **6 gold coins** ($y = 6x$). Type `6 {{key:REP}}` and tap `{{key:+}}` three times: **`6 -> 12 -> 18 -> 24`**! You just generated 4 $(x,y)$ graph points in 3 seconds! (`[ ] +5 Spark XP!`)",
        "why_new": "Today ties together three whole chapters: a two-variable equation like $y = 12.5x$ is simultaneously a Day 12 Ratio Table (`⚡`), a Day 16 Formula (`🚀`), and a Day 27 Coordinate Line (`🔨`)!",
        "twin": "**Way A (`🚀` Inverse Equation Undo for $p=\\$100$):** `100 {{key:ENTER}} 12.5 {{key:÷}}` = **8 hours**. **Way B (`⚡` Double-Up Ratio Table from Day 12):** $1\\text{ hr}=\\$12.50 \\to 2\\text{ hr}=\\$25 \\to 4\\text{ hr}=\\$50 \\to 8\\text{ hr}=$ **$100**!",
    },
    34: {
        "spiral": "Thread D (Inside-Out Chunking) • [🔄 VISIT 4: CROSS-CHAPTER BOOMERANG — Revisits Day 20 RECT & Day 22 Σ+]",
        "game_mode": "🎯 Mode B: Unfold the 6-Wall Box (`{{key:RECT}}` + `{{key:Σ+}}`)",
        "starter": "Look at a **2 by 2 by 2 cube** of blocks. Each square wall has area $2 \\times 2 = 4$, and a cube has **6 walls** ($6 \\times 4 = 24$)! Key `4 {{key:ENTER}} 6 {{key:×}}` -> **`24`**! (`[ ] +5 Spark XP!`)",
        "why_new": "Finding the surface area of a 3D box by writing $2(lw + lh + wh)$ on paper is a magnet for arithmetic mistakes. Unfolding the 6 faces (`🔨`) and feeding the 3 pairs into Day 22's `{{key:RECT}}` + `{{key:Σ+}}` ledger (`🚀`) never drops a face!",
        "twin": "**Way A (`🚀` Add 5 Faces via `{{key:Σ+}}`):** Bottom ($80$) + 2 F/B ($100$) + 2 L/R ($80$) -> `{{key:Σx}}` = **`260 cm²`**. **Way B (`⚡` Full 6-Face Box Minus Missing Top):** $340 - 80 =$ **`260 cm²`**!",
    },
    35: {
        "spiral": "Thread D (Inside-Out Chunking) • [🔄 VISIT 5: CROSS-CHAPTER BOOMERANG — Revisits Day 21 TRI & Day 34 Nets]",
        "game_mode": "⚡ Mode C: Pyramid Tent Builder (`{{key:TRI}}` + `{{key:Σ+}}`)",
        "starter": "A square pyramid has **1 square floor** (`4 by 4 = 16`) and **4 triangle roofs** (`each area 6 -> 24`). Total is $16 + 24 =$ **`40`**! (`[ ] +5 Spark XP!`)",
        "why_new": "Pyramids and triangular prisms mix rectangles and triangles. Instead of tangling two formulas together, use `{{key:RECT}}` for flat walls and `{{key:TRI}}` for sloped roofs, tossing each into `{{key:Σ+}}` (`🚀`)!",
        "twin": "**Way A (`🚀` One Triangle $\\times 4$):** `6 {{key:ENTER}} 5.2 {{key:TRI}}` (`15.6`) `4 {{key:×}}` = **`62.4 cm²`**. **Way B (`⚡` Repeat `{{key:Σ+}}` 4 Times):** Add `15.6` four times into `{{key:Σ+}}` -> `{{key:Σx}}` = **`62.4 cm²`**!",
    },
    36: {
        "spiral": "Thread D & B Boomerang • [🚀 VISIT 3: STACK HACKER WAY — Revisits Day 2 Cubes, Day 7 Fractions & Day 20 Area]",
        "game_mode": "🔄 Mode D: 1-Click 3D Volume (`{{key:PRISM}}`)",
        "starter": "Build a **3 by 2 layer** of cubes ($6$ cubes) and stack **4 layers** high ($24$ cubes). Now type `3 {{key:ENTER}} 2 {{key:ENTER}} 4 {{key:PRISM}}` (`[f][2]`) -> **`24`** in 1 click! (`[ ] +5 Spark XP!`)",
        "why_new": "Packing physical unit cubes (`🔨`) shows why Volume is 3D space ($l \\times w \\times h$), while `{{key:PRISM}}` (`🚀`) computes volume even when the edge lengths are fractions or decimals!",
        "twin": "**Way A (`🚀` Base-Area Division):** Since $V = B \\times h$, key `270 {{key:ENTER}} 45 {{key:÷}}` = **`6 in`**. **Way B (`⚡` Forward `{{key:PRISM}}` Proof with $9 \\times 5 \\times 6$):** `9 {{key:ENTER}} 5 {{key:ENTER}} 6 {{key:PRISM}}` = **`270 in³`**!",
    },
    37: {
        "spiral": "Thread C & D Boomerang • [🚀 VISIT 4: CROSS-CHAPTER BOOMERANG — Revisits Day 2 Squares & Day 36 Volume]",
        "game_mode": "🕵️ Mode A: 3-4-5 Right Triangle Magic (`{{key:HYP}}` & `{{key:CONE}}`)",
        "starter": "Lay a **3-tile row** and a **4-tile column** at a right angle. Measure the diagonal: it's **5 tiles** ($3^2+4^2=5^2$)! Now press `3 {{key:ENTER}} 4 {{key:HYP}}` (`[g][3]`) -> **`5`**! (`[ ] +5 Spark XP!`)",
        "why_new": "Typing `3.14` by hand causes rounding drift, and cones/right triangles take 4 steps on a basic calculator. Today you compare manual formula steps (`⚡`) against the SC-6's 1-click `{{key:CIRC}}`, `{{key:CONE}}`, and `{{key:HYP}}` keys (`🚀`)!",
        "twin": "**Way A (`🚀` 1-Click `{{key:CONE}}`):** `3 {{key:ENTER}} 10 {{key:CONE}}` = **`94.25 cm³`**. **Way B (`⚡` Cylinder $\\div 3$ Formula):** `{{key:π}} 3 {{key:x²}} {{key:×}} 10 {{key:×}} 3 {{key:÷}}` = **`94.25 cm³`**!",
    },
    38: {
        "spiral": "Thread F (Balance & Fair Share) • [⚡ VISIT 2: PATTERN WAY — Revisits Day 1 Division & Day 22 Σ+]",
        "game_mode": "⚡ Mode C: Level the Cube Towers (`{{key:Σ+}}` & `{{key:x̄}}`)",
        "starter": "Build 3 cube towers of heights **`2`**, **`4`**, and **`6`**. Move **2 cubes** from the `6`-tower to the `2`-tower—now all three towers are height **`4`**! Press `{{key:CLΣ}} 2 {{key:Σ+}} 4 {{key:Σ+}} 6 {{key:Σ+}} {{key:x̄}}` -> **`4`**! (`[ ] +5 Spark XP!`)",
        "why_new": "What *is* an average (Mean)? If you build unequal towers of cubes (`🔨`) and move cubes from tall towers to short ones until every tower is the **same height**, that leveled height is the Mean! And for big lists, `{{key:Σ+}}` + `{{key:x̄}}` (`🚀`) levels them in 1 click!",
        "twin": "**Way A (`🚀` Target Total Minus `{{key:Σx}}`):** Need $4 \\times 90 = 360$ pts; current `{{key:Σx}}` $= 265 \\to 360 - 265 =$ **95**. **Way B (`🔨` Fair-Share Points Above/Below 90):** $(-6) + (-2) + (+3) = -5$ deficit, so Quiz 4 needs $90 + 5 =$ **95**!",
    },
    39: {
        "spiral": "Thread F (Balance & Fair Share) • [🚀 VISIT 3: STACK HACKER WAY — Revisits Day 38 Mean]",
        "game_mode": "🎲 Mode E: Live Dice Roll Stats Lab (`{{key:MED}}`, `{{key:MODE}}`, `{{key:RNG}}`)",
        "starter": "With `2, 4, 6` still in memory from yesterday, press `{{key:MED}}` (`[g][7]`) -> **`4`** (middle number) and `{{key:RNG}}` (`[g][8]`) -> **`4`** ($6 - 2$)! Zero re-typing! (`[ ] +5 Spark XP!`)",
        "why_new": "On Day 38 we leveled towers to find the Mean (`{{key:x̄}}`). Why do we also need the **Median (`{{key:MED}}`)**? Because one crazy outlier (like a $\\$450$ console in a list of $\\$20$ games) drags the Mean way up, while the middle number (`{{key:MED}}`) stays rock-solid!",
        "twin": "**Way A (`🔨` Line Up Physical Tiles in Order):** Sort your 5 rolls from least to greatest to spot the middle tile (`Median`) and `Max - Min` (`Range`). **Way B (`🚀` SC-6 `{{key:MED}}` & `{{key:RNG}}` Keys):** Load into `{{key:Σ+}}` and press `{{key:MED}}` and `{{key:RNG}}`—100% match!",
    },
    40: {
        "spiral": "Thread F (Balance & Fair Share) • [🚀 VISIT 4: BOSS REVISIT — Revisits Day 6 Quarters & Day 39 Median]",
        "game_mode": "🔄 Mode D: 3-Second Box-Plot Builder (`{{key:1Q}}`, `{{key:3Q}}`, `{{key:IQR}}`)",
        "starter": "Load `10, 20, 30, 40, 50` into `{{key:Σ+}}`. Tap `{{key:MIN}}` (`10`), `{{key:1Q}}` (`15`), `{{key:MED}}` (`30`), `{{key:3Q}}` (`45`), `{{key:MAX}}` (`50`), and `{{key:IQR}}` (`30`)! Whole Box Plot in 5 seconds! (`[ ] +5 Spark XP!`)",
        "why_new": "Finding $Q_1$, $Q_3$, and $\\text{IQR}$ by hand requires splitting a sorted list in half and finding medians of each half. Once your data is in `{{key:Σ+}}` from Day 39, pressing `{{key:1Q}}`, `{{key:3Q}}`, and `{{key:IQR}}` (`🚀`) builds your entire Box Plot in 3 seconds!",
        "twin": "**Way A (`🔨` Box-Plot Width Visual):** A narrower middle box (`IQR = 4` vs `18`) means the middle $50\\%$ of scores are tightly clustered (**Player A**). **Way B (`🚀` `3Q - 1Q` Stack Check):** Verify `{{key:3Q}}` minus `{{key:1Q}}` equals `{{key:IQR}}`!",
    },
    41: {
        "spiral": "Thread E & F Boomerang • [🔄 VISIT 5: CROSS-CHAPTER BOOMERANG — Revisits Day 26 |x| & Day 38 Mean]",
        "game_mode": "🔄 Mode D: Beat the 20-Minute Homework Monster (`{{key:MAD}}`)",
        "starter": "Towers `2, 4, 6` have Mean `4`. Their distances from `4` are `2, 0, 2` (average distance = $4 \\div 3 = 1.33$). Now press `{{key:MAD}}` (`[g][5]`) on your SC-6 -> **`1.33`** in 1 click! (`[ ] +5 Spark XP!`)",
        "why_new": "Mean Absolute Deviation (`MAD`) is the most dreaded calculation in 6th grade because doing it by hand takes 15 steps (find mean, subtract every number, take `[|x|]` from Day 26, and average again). Today you see *how* Day 26's `[|x|]` + Day 38's `{{key:x̄}}` build `MAD`—and unlock the 1-click `{{key:MAD}}` key (`🚀`)!",
        "twin": "**Way A (`🚀` 1-Click `{{key:MAD}}` Key):** Load `5, 8, 8, 10, 14` into `{{key:Σ+}}` and press `{{key:MAD}}` = **`2.4`**. **Way B (`⚡` Distance-from-Mean Check using Day 26 `[|x|]`):** Mean $= 9$; distances $4+1+1+1+5 = 12 \\to 12 \\div 5 =$ **`2.4`**!",
    },
    42: {
        "spiral": "Thread E (Zero-Pair & Distance) • [🔄 VISIT 5: GRADE 7 BRIDGE BOOMERANG — Revisits Days 7, 24 & 26]",
        "game_mode": "🕵️ Mode A: Penalty Cancellation Trick ($10 - (-4) = 14$)",
        "starter": "Your game score is **`10`**, and the ref **erases a $-4$ penalty** ($10 - (-4)$). Erasing a penalty makes your score go **UP to `14`**! Key `10 {{key:ENTER}} 4 {{key:+/-}} {{key:-}}` -> **`14`**! (`[ ] +5 Spark XP!`)",
        "why_new": "In Chapter 6 (`Day 24`), you met Yellow ($+1$) and Red ($-1$) counters. Today they boomerang back for 7th-grade signed arithmetic: removing red debt counters (`🔨`) proves *why* subtracting a negative ($10 - (-4)$) is the exact same as adding a positive ($10 + 4 = 14$)!",
        "twin": "**Way A (`🚀` Signed Fraction Stack):** `{{key:.}} 3 {{key:.}} 4 {{key:+/-}} {{key:ENTER}} {{key:.}} 5 {{key:.}} 8 {{key:+/-}} {{key:-}}` = **`-1/8`**. **Way B (`⚡` Add-the-Opposite + Common 8ths):** $-\\frac{6}{8} + (+\\frac{5}{8}) =$ **`-1/8`**!",
    },
    43: {
        "spiral": "Thread E & B Boomerang • [🔄 VISIT 6: GRADE 7 BRIDGE BOOMERANG — Revisits Days 8, 24 & 42]",
        "game_mode": "⚡ Mode C: Light-Switch Double-Flip (`{{key:+/-}}` × `{{key:+/-}}`)",
        "starter": "Type `5` on your SC-6. Tap `{{key:+/-}}` **twice**: `5 -> -5 -> +5`! Two negative flips always bring you back to **POSITIVE**! Now key `3 {{key:+/-}} {{key:ENTER}} 4 {{key:+/-}} {{key:×}}` -> **`+12`**! (`[ ] +5 Spark XP!`)",
        "why_new": "Why does $(-)\\times(-) = (+)$? Pressing `{{key:+/-}}` twice (`🔨`) flips a negative right back to positive! Combining Day 8's Reciprocal Flip (`{{key:1/x}}`) with today's Even/Odd Sign-Flip rule (`⚡`) lets you predict the sign of any product or quotient before touching a key!",
        "twin": "**Way A (`🚀` Signed Fraction Stack):** `{{key:.}} 5 {{key:.}} 6 {{key:+/-}} {{key:ENTER}} {{key:.}} 5 {{key:.}} 12 {{key:+/-}} {{key:÷}}` = **`+2`**. **Way B (`⚡` Sign-Flip Rule + Day 8 Reciprocal):** 2 negatives = $(+)$, and $\\frac{5}{6} \\times \\frac{12}{5} =$ **`+2`**!",
    },
    44: {
        "spiral": "Thread F, B & D Boomerang • [🚀 VISIT 6: GRADE 7 BOSS BOOMERANG — Revisits Days 3, 30, 31 & 42]",
        "game_mode": "🎯 Mode B: Unwrap the Present in Reverse ($ax + b = c$)",
        "starter": "To Solve $2x + 3 = 11$: first untie the loose ribbon (`11 {{key:ENTER}} 3 {{key:-}}` -> `8`), then open the 2 boxes (`2 {{key:÷}}` -> **`x = 4`**)! Two clicks, zero algebra rewrites! (`[ ] +5 Spark XP!`)",
        "why_new": "Two-step equations ($ax + b = c$) combine Day 30 (Addition/Subtraction Undo), Day 31 (Multiplication/Division Undo), and Day 42 (Signed Numbers) into one reverse unwrap! Solve by sweeping blocks off the Algebra Stage (`🔨`) OR running the 2-step reverse stack (`🚀`)!",
        "twin": "**Way A (`🚀` 2-Step Reverse Stack):** `2 {{key:ENTER}} 14 {{key:-}}` (`-12`) `3 {{key:+/-}} {{key:÷}}` = **`x = 4`**. **Way B (`🔨` Plug-In Forward Check from Day 16):** Substitute $x=4$ into $-3(4) + 14 = -12 + 14 =$ **`2`**!",
    },
    45: {
        "spiral": "All 6 Threads Finale • [🏆 GRADUATION BOSS SPRINT — Revisits Fractions (Ch. 2), Percents (Ch. 3) & Stats (Ch. 9)]",
        "game_mode": "🎲 Mode E: Graduation Live Dice & `{{key:?}}` Quiz Sprint",
        "starter": "Press `6 {{key:1…x}}` (`[f][🎲]`) three times to roll a digital 6-sided die, then press `3 {{key:x!}}` (`[g][🎲]`) -> **`6`** ways to arrange 3 trophies! (`[ ] +5 Spark XP!`)",
        "why_new": "On Graduation Day, you combine physical dice/spinner trials (`🔨`), 3-way fraction/decimal/percent probability (`⚡`), and the SC-6's combinatorics (`{{key:x!}}`, `{{key:nCr}}`, `{{key:nPr}}`) and Quiz Engine (`{{key:?}}` `🚀`)!",
        "twin": "**Way A (`🚀` Factorial Key `{{key:x!}}`):** `5 {{key:x!}}` = **120 ways**. **Way B (`⚡` Permutation Key `{{key:nPr}}`):** Choosing all 5 badges in order is `5 {{key:ENTER}} 5 {{key:nPr}}` = **120 ways** ($5\\times 4\\times 3\\times 2\\times 1$)!",
    },
}


def sync_markdown_with_spiral_map(md_path: Path) -> None:
    """Idempotently inject Spiral Revisit Path, Variety Game Mode, 30-Sec Zero-Fail Starter, Why Try a New Way Today, and Problem 3 Twin-Way Bonus into the Markdown curriculum."""
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    out_lines: List[str] = []
    cur_day: Optional[int] = None

    i = 0
    while i < len(lines):
        line = lines[i]
        # Skip previously injected lines so running is 100% idempotent
        if (
            line.startswith("- **Spiral Revisit Path:**")
            or line.startswith("- **🎮 Today's Variety Game Mode:**")
            or line.startswith("- **⚡ 30-Second Zero-Fail Starter (Instant Win #1):**")
            or line.startswith("- **Why Try a New Way Today?")
            or line.strip().startswith("- **★★ Twin-Way Bonus")
        ):
            i += 1
            continue

        day_m = re.match(r"^###\s+Day\s+(\d+)\s+\(Lesson\s+([\d.]+)\):", line)
        if day_m:
            cur_day = int(day_m.group(1))

        if cur_day in SPIRAL_REVISIT_MAP and line.startswith("- **Why Should I Care? (2-Min Hook):**"):
            info = SPIRAL_REVISIT_MAP[cur_day]
            out_lines.append(f"- **Spiral Revisit Path:** {info['spiral']}")
            out_lines.append(f"- **🎮 Today's Variety Game Mode:** {info['game_mode']}")
            out_lines.append(f"- **⚡ 30-Second Zero-Fail Starter (Instant Win #1):** {info['starter']}")
            out_lines.append(line)
            while i + 1 < len(lines) and lines[i + 1].startswith("  "):
                i += 1
                out_lines.append(lines[i])
            out_lines.append(f"- **Why Try a New Way Today? (When the Old Way Gets Annoying):** {info['why_new']}")
            i += 1
            continue

        if cur_day in SPIRAL_REVISIT_MAP and re.match(r"^3\.\s+\*\*Problem\s+3\s*\(", line):
            out_lines.append(line)
            while i + 1 < len(lines) and lines[i + 1].startswith("   - ") and not lines[i + 1].strip().startswith("- **★★ Twin-Way Bonus"):
                i += 1
                out_lines.append(lines[i])
            info = SPIRAL_REVISIT_MAP[cur_day]
            out_lines.append(f"   - **★★ Twin-Way Bonus (+25 XP toward 🛡️ Skip Shield):** {info['twin']}")
            i += 1
            continue

        out_lines.append(line)
        i += 1

    updated = "\n".join(out_lines) + "\n"
    if updated != text:
        md_path.write_text(updated, encoding="utf-8")
        print(f"[SYNC] Updated {md_path} with 45-Day Zero-Fail Starters, Variety Game Modes, Spiral Paths & Twin-Way Bonuses.")


def clean_inline_md(text: str) -> str:
    """Convert inline markdown/LaTeX into clean ReportLab XML markup."""
    s = text.strip()
    emoji_map = {
        "🧱": "[BLOCKS]",
        "📟": "[STACK]",
        "✅": "[PROVE]",
        "🏆": "[BADGE]",
        "🔨": "[BUILDER]",
        "⚡": "[SPARK]",
        "🚀": "[STACK-HACK]",
        "🔄": "[BOOMERANG]",
        "🕵️": "[DETECTIVE]",
        "🎯": "[TARGET]",
        "🎮": "[GAME]",
        "🟢": "[EASY-WIN]",
        "🟡": "[PUZZLE]",
        "🔴": "[BOSS]",
        "😎": "",
        "🔥": "",
        "🛠️": "",
        "🛡️": "[SKIP-SHIELD]",
        "🪪": "[DEALERS-CHOICE]",
        "★★": "[2x-STAR]",
        "★": "[1x-STAR]",
        "📖": "",
        "📝": "",
        "🎯": "[TARGET]",
        "🧑‍🏫": "",
        "🕒": "CLK",
        "▦": "10F",
        "🎲": "DICE",
        "●": "*",
        "○": "o",
        "&bull;": "•",
        "&amp;": "&",
        "&rarr;": "->",
        "&darr;": "v",
        "&le;": "<=",
        "&ge;": ">=",
        "&#124;": "|",
    }
    for k, v in emoji_map.items():
        s = s.replace(k, v)

    s = re.sub(r"\\frac\{([^{}]+)\}\{([^{}]+)\}", r"\1/\2", s)
    s = re.sub(r"\\text\{([^{}]+)\}", r"\1", s)
    s = re.sub(r"\\sqrt\{([^{}]+)\}", r"√(\1)", s)
    latex_repls = {
        r"\times": "×",
        r"\div": "÷",
        r"\cdot": "·",
        r"\to": "->",
        r"\leftrightarrow": "<->",
        r"\ge": ">=",
        r"\le": "<=",
        r"\pi": "π",
        r"\bar{x}": "x̄",
        r"\sum": "Σ",
        r"\approx": "≈",
        r"^\circ": "°",
        r"\_": "_",
        r"\{": "{",
        r"\}": "}",
        r"\$": "$",
    }
    for k, v in latex_repls.items():
        s = s.replace(k, v)
    s = re.sub(r"\$([^$]+)\$", r"\1", s)

    code_tokens: List[str] = []

    def _stash_code(m: re.Match) -> str:
        idx = len(code_tokens)
        escaped_code = html.escape(m.group(1))
        code_tokens.append(f'<font name="{FONT_MONO_BOLD}" color="#0F172A">{escaped_code}</font>')
        return f"@@CODE{idx}@@"

    s = re.sub(r"`([^`]+)`", _stash_code, s)
    s = s.replace("<br>", "@@BR@@").replace("<br/>", "@@BR@@")
    s = html.escape(s)
    s = s.replace("@@BR@@", "<br/>")

    s = re.sub(r"\*\*([^*]+)\*\*", lambda m: f"<b>{m.group(1)}</b>", s)
    s = re.sub(r"\*([^*]+)\*", lambda m: f"<i>{m.group(1)}</i>", s)

    for idx, tok in enumerate(code_tokens):
        s = s.replace(f"@@CODE{idx}@@", tok)
    return s


def split_md_row(line: str) -> List[str]:
    """Split a markdown table row on | outside backticks."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    cells: List[str] = []
    cur: List[str] = []
    in_code = False
    for ch in s:
        if ch == "`":
            in_code = not in_code
            cur.append(ch)
        elif ch == "|" and not in_code:
            cells.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    cells.append("".join(cur).strip())
    return cells


def parse_workbook_markdown(md_path: Path) -> List[Dict]:
    """Parse chapters and daily lessons from the markdown source."""
    raw = md_path.read_text(encoding="utf-8")
    expanded = expand_key_macros(raw, is_sc32=False, file_path=md_path, target_format="pdf")

    chapters: List[Dict] = []
    current_chapter: Optional[Dict] = None
    current_day: Optional[Dict] = None
    mode: Optional[str] = None

    for line in expanded.splitlines():
        ch_match = re.match(r"^#\s+CHAPTER\s+(\d+):\s+(.+)$", line)
        if ch_match:
            current_chapter = {
                "num": int(ch_match.group(1)),
                "title": ch_match.group(2).strip(),
                "subtitle": "",
                "days": [],
            }
            chapters.append(current_chapter)
            current_day = None
            mode = "chapter_intro"
            continue

        day_match = re.match(r"^###\s+Day\s+(\d+)\s+\(Lesson\s+([\d.]+)\):\s+(.+)$", line)
        if day_match and current_chapter is not None:
            d_num = int(day_match.group(1))
            spiral_info = SPIRAL_REVISIT_MAP.get(d_num, {})
            current_day = {
                "day_num": d_num,
                "lesson_num": day_match.group(2).strip(),
                "title": day_match.group(3).strip(),
                "alignment": "",
                "spiral": spiral_info.get("spiral", ""),
                "game_mode": spiral_info.get("game_mode", ""),
                "starter": expand_key_macros(spiral_info.get("starter", ""), is_sc32=False, file_path=md_path, target_format="pdf"),
                "why_new": expand_key_macros(spiral_info.get("why_new", ""), is_sc32=False, file_path=md_path, target_format="pdf"),
                "twin": expand_key_macros(spiral_info.get("twin", ""), is_sc32=False, file_path=md_path, target_format="pdf"),
                "question": "",
                "hook": "",
                "decoder_lines": [],
                "problems": [],
            }
            current_chapter["days"].append(current_day)
            mode = "day_meta"
            continue

        if re.match(r"^##\s+4\.\s+The 45-Day Student Streak", line):
            current_day = None
            mode = "end"
            break

        if current_day is None:
            if mode == "chapter_intro" and current_chapter and line.startswith("*") and line.endswith("*"):
                current_chapter["subtitle"] = line.strip("*")
            continue

        if line.startswith("#### ") and ("Decoder" in line or "Elevator Trace" in line):
            mode = "decoder"
            continue
        if line.startswith("#### Daily 3-Problem Workout"):
            mode = "problems"
            continue

        if mode == "day_meta":
            if line.startswith("- **Big Ideas"):
                current_day["alignment"] = re.sub(r"^-\s*\*\*[^*]+\*\*\s*", "", line).strip()
            elif line.startswith("- **The Real Question:**"):
                current_day["question"] = line.replace("- **The Real Question:**", "").strip()
            elif line.startswith("- **Why Should I Care? (2-Min Hook):**"):
                current_day["hook"] = line.replace("- **Why Should I Care? (2-Min Hook):**", "").strip()
        elif mode == "decoder":
            if line.strip() and not line.strip().startswith("{{blocks:") and not line.strip().startswith("```"):
                current_day["decoder_lines"].append(line)
        elif mode == "problems":
            prob_match = re.match(r"^(\d+)\.\s+\*\*Problem\s+\d+\s*\(([^)]+)\):\*\*\s*(.+)$", line)
            if prob_match:
                p_num = int(prob_match.group(1))
                current_day["problems"].append({
                    "num": p_num,
                    "tag": prob_match.group(2).strip(),
                    "prompt": prob_match.group(3).strip(),
                    "game_mode": current_day["game_mode"] if p_num == 2 else "",
                    "touch": "",
                    "stack": "",
                    "prove": "",
                    "twin": current_day["twin"] if p_num == 3 else "",
                })
            elif current_day["problems"]:
                last_p = current_day["problems"][-1]
                stripped = line.strip()
                if stripped.startswith("- **") and "Touch It" in stripped:
                    last_p["touch"] = re.sub(r"^-\s*\*\*[^*]+\*\*\s*", "", stripped)
                elif stripped.startswith("- **") and ("Stack It" in stripped or "Way A" in stripped or "Way B" in stripped):
                    val = re.sub(r"^-\s*\*\*([^*]+)\*\*\s*", r"**\1** ", stripped)
                    last_p["stack"] = (last_p["stack"] + " • " + val) if last_p["stack"] else val
                elif stripped.startswith("- **") and ("Prove It" in stripped or "Answer" in stripped):
                    last_p["prove"] = re.sub(r"^-\s*\*\*[^*]+\*\*\s*", "", stripped)

    return chapters


def build_styles() -> Dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "CoverKicker": ParagraphStyle(
            "CoverKicker",
            parent=base["Normal"],
            fontName=FONT_MONO_BOLD,
            fontSize=9,
            leading=12,
            textColor=HexColor("#059669"),
            spaceAfter=4,
        ),
        "CoverTitle": ParagraphStyle(
            "CoverTitle",
            parent=base["Title"],
            fontName=FONT_BOLD,
            fontSize=21,
            leading=25,
            textColor=HexColor("#0F172A"),
            alignment=0,
            spaceAfter=5,
        ),
        "CoverSub": ParagraphStyle(
            "CoverSub",
            parent=base["Normal"],
            fontName=FONT_BODY,
            fontSize=9.6,
            leading=13.2,
            textColor=HexColor("#334155"),
            spaceAfter=8,
        ),
        "ChapterHeader": ParagraphStyle(
            "ChapterHeader",
            parent=base["Heading1"],
            fontName=FONT_BOLD,
            fontSize=15,
            leading=19,
            textColor=HexColor("#FFFFFF"),
            spaceBefore=0,
            spaceAfter=2,
        ),
        "ChapterSub": ParagraphStyle(
            "ChapterSub",
            parent=base["Normal"],
            fontName=FONT_ITALIC,
            fontSize=8.5,
            leading=11.5,
            textColor=HexColor("#E2E8F0"),
        ),
        "DayHeader": ParagraphStyle(
            "DayHeader",
            parent=base["Heading2"],
            fontName=FONT_BOLD,
            fontSize=11.5,
            leading=14.5,
            textColor=HexColor("#064E3B"),
            spaceBefore=6,
            spaceAfter=2,
        ),
        "SpiralBadge": ParagraphStyle(
            "SpiralBadge",
            parent=base["Normal"],
            fontName=FONT_MONO_BOLD,
            fontSize=7.4,
            leading=10.0,
            textColor=HexColor("#1E3A8A"),
            spaceAfter=2,
        ),
        "BodySmall": ParagraphStyle(
            "BodySmall",
            parent=base["Normal"],
            fontName=FONT_BODY,
            fontSize=8.3,
            leading=11.0,
            textColor=HexColor("#1E293B"),
            spaceAfter=3,
        ),
        "HookBox": ParagraphStyle(
            "HookBox",
            parent=base["Normal"],
            fontName=FONT_BODY,
            fontSize=7.9,
            leading=10.6,
            textColor=HexColor("#0F172A"),
        ),
        "TableCell": ParagraphStyle(
            "TableCell",
            parent=base["Normal"],
            fontName=FONT_BODY,
            fontSize=7.5,
            leading=9.8,
            textColor=HexColor("#0F172A"),
        ),
        "TableHeader": ParagraphStyle(
            "TableHeader",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=7.5,
            leading=9.8,
            textColor=HexColor("#FFFFFF"),
        ),
        "TicketTitle": ParagraphStyle(
            "TicketTitle",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=8.4,
            leading=10.8,
            textColor=HexColor("#0F172A"),
        ),
    }


def render_markdown_table(lines: List[str], styles: Dict[str, ParagraphStyle], usable_w: float) -> Optional[Table]:
    """Extract and render the first markdown table in decoder_lines."""
    table_lines = [ln.strip() for ln in lines if ln.strip().startswith("|") and ln.strip().endswith("|")]
    if len(table_lines) < 3:
        return None
    rows_raw = []
    for idx, ln in enumerate(table_lines):
        cells = split_md_row(ln)
        if idx == 1 and all(re.match(r"^[:\-]+$", c.replace(" ", "")) for c in cells if c):
            continue
        rows_raw.append(cells)
    if len(rows_raw) < 2:
        return None
    ncols = max(len(r) for r in rows_raw)
    data = []
    for r_idx, r in enumerate(rows_raw):
        padded = (r + [""] * ncols)[:ncols]
        st = styles["TableHeader"] if r_idx == 0 else styles["TableCell"]
        data.append([Paragraph(clean_inline_md(c), st) for c in padded])

    col_w = usable_w / ncols
    t = Table(data, colWidths=[col_w] * ncols, repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), HexColor("#1E293B")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#F8FAFC"), HexColor("#FFFFFF")]),
                ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#CBD5E1")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 3.0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3.0),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return t


def build_student_ticket(prob: Dict, styles: Dict[str, ParagraphStyle], usable_w: float) -> Table:
    """Create the fillable 3-Box 'Touch • Stack • Prove' student work ticket with 3-Speed Confidence Ramp badges."""
    p_num = prob["num"]
    if p_num == 1:
        ramp_badge = "[STEP 1: 60-SEC QUICK WIN (+10 XP)] "
        hdr_bg = HexColor("#ECFDF5")
        border_col = HexColor("#10B981")
    elif p_num == 2:
        gm = prob.get("game_mode") or "VARIETY PUZZLE"
        ramp_badge = f"[STEP 2: {gm.upper()} (+10 XP)] "
        hdr_bg = HexColor("#EFF6FF")
        border_col = HexColor("#3B82F6")
    else:
        ramp_badge = "[STEP 3: SECRET-GENIUS BOSS + 2x-STAR BONUS (+25 XP)] "
        hdr_bg = HexColor("#FEF3C7")
        border_col = HexColor("#D97706")

    header_p = Paragraph(
        clean_inline_md(f"**{ramp_badge}Problem {p_num} ({prob['tag']}):** {prob['prompt']}"),
        styles["TicketTitle"],
    )
    touch_hint = prob["touch"].replace("[ ]", "").strip() if prob["touch"] else "Build with blocks on your desk first!"
    col1 = Paragraph(
        clean_inline_md(f"<b>1. [BLOCKS] TOUCH IT</b><br/>[  ] {touch_hint}<br/><i>(Only 1 method needed!)</i>"),
        styles["TableCell"],
    )
    col2 = Paragraph(
        f'<b>2. [STACK] ELEVATOR SNAPSHOT</b><br/>'
        f'<font name="{FONT_MONO}" size="7.3">Floor 2 (Y): ___________<br/>Floor 1 (X): ___________</font>',
        styles["TableCell"],
    )
    col3 = Paragraph(
        f'<b>3. [PROVE] GREEN-LIGHT CHECK</b><br/>'
        f'<font name="{FONT_MONO}" size="7.3">FINAL ANSWER: __________</font><br/>'
        f'[  ] Proven with [f][LASTX]!',
        styles["TableCell"],
    )

    data = [
        [header_p, "", ""],
        [col1, col2, col3],
    ]
    if p_num == 3 and prob.get("twin"):
        twin_p = Paragraph(
            clean_inline_md(
                f"<b>[2x-STAR] TWIN-WAY REVISIT BONUS (Try 2 Ways -> Earn [SKIP-SHIELD]):</b> {prob['twin']}<br/>"
                f"<b>Check 2 Ways Matched:</b>  [  ] [BUILDER] Blocks   [  ] [SPARK] Pattern/Table   [  ] [STACK-HACK] SC-6 Key   "
                f"•   <b>Confidence Check:</b>  [  ] Easy Win!   [  ] Just Right!   [  ] Blocks Helped!"
            ),
            styles["TableCell"],
        )
        data.append([twin_p, "", ""])

    w1 = usable_w * 0.36
    w2 = usable_w * 0.32
    w3 = usable_w * 0.32
    t = Table(data, colWidths=[w1, w2, w3])
    style_cmds = [
        ("SPAN", (0, 0), (2, 0)),
        ("BACKGROUND", (0, 0), (2, 0), hdr_bg),
        ("BACKGROUND", (0, 1), (0, 1), HexColor("#FFFFFF")),
        ("BACKGROUND", (1, 1), (1, 1), HexColor("#F8FAFC")),
        ("BACKGROUND", (2, 1), (2, 1), HexColor("#FFFFFF")),
        ("BOX", (0, 0), (-1, -1), 0.9, border_col),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, HexColor("#CBD5E1")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]
    if p_num == 3 and prob.get("twin"):
        style_cmds.extend([
            ("SPAN", (0, 2), (2, 2)),
            ("BACKGROUND", (0, 2), (2, 2), HexColor("#FFFBEB")),
        ])
    t.setStyle(TableStyle(style_cmds))
    return t


def build_teacher_ticket(prob: Dict, styles: Dict[str, ParagraphStyle], usable_w: float) -> Table:
    """Create the filled Teacher/Coach Solution & Stack Trace ticket."""
    p_num = prob["num"]
    is_boss = p_num == 3
    header_p = Paragraph(
        clean_inline_md(f"**Problem {p_num} ({prob['tag']}):** {prob['prompt']}"),
        styles["TicketTitle"],
    )
    touch_txt = prob["touch"] or "Hands-on manipulative build verified."
    stack_txt = prob["stack"] or "Verified on 4-line XYZT stack."
    prove_txt = prob["prove"] or "Verified via [f][LASTX] inverse operation."

    col1 = Paragraph(clean_inline_md(f"<b>1. [BLOCKS] TOUCH IT:</b><br/>{touch_txt}"), styles["TableCell"])
    col2 = Paragraph(clean_inline_md(f"<b>2. [STACK] KEYSTROKES &amp; Y|X:</b><br/>{stack_txt}"), styles["TableCell"])
    col3 = Paragraph(clean_inline_md(f"<b>3. [PROVE] VERIFIED SOLUTION:</b><br/>{prove_txt}"), styles["TableCell"])

    data = [
        [header_p, "", ""],
        [col1, col2, col3],
    ]
    if is_boss and prob.get("twin"):
        twin_p = Paragraph(
            clean_inline_md(f"<b>[2x-STAR] TWIN-WAY REVISIT KEY (Way A == Way B):</b> {prob['twin']}"),
            styles["TableCell"],
        )
        data.append([twin_p, "", ""])

    w1 = usable_w * 0.28
    w2 = usable_w * 0.42
    w3 = usable_w * 0.30
    t = Table(data, colWidths=[w1, w2, w3])
    style_cmds = [
        ("SPAN", (0, 0), (2, 0)),
        ("BACKGROUND", (0, 0), (2, 0), HexColor("#FEF3C7") if is_boss else HexColor("#EFF6FF")),
        ("BACKGROUND", (0, 1), (2, 1), HexColor("#FFFFFF")),
        ("BOX", (0, 0), (-1, -1), 0.8, HexColor("#D97706") if is_boss else HexColor("#3B82F6")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, HexColor("#CBD5E1")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]
    if is_boss and prob.get("twin"):
        style_cmds.extend([
            ("SPAN", (0, 2), (2, 2)),
            ("BACKGROUND", (0, 2), (2, 2), HexColor("#FFFBEB")),
        ])
    t.setStyle(TableStyle(style_cmds))
    return t


def add_footer(canvas_obj, doc, title_str: str):
    canvas_obj.saveState()
    canvas_obj.setFont(FONT_MONO, 7.5)
    canvas_obj.setFillColor(HexColor("#64748B"))
    canvas_obj.drawString(36, 22, title_str)
    canvas_obj.drawRightString(letter[0] - 36, 22, f"Page {doc.page}")
    canvas_obj.restoreState()


def generate_pdf(chapters: List[Dict], output_path: Path, is_teacher: bool) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    styles = build_styles()
    usable_w = letter[0] - 72.0

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=34,
        bottomMargin=36,
        title=(
            "StackCalc SC-6 Big Ideas Middle School Coach & Answer Key"
            if is_teacher
            else "StackCalc SC-6 Big Ideas Middle School Daily Catch-Up Student Workbook"
        ),
        author="StackCalc Learning Lab",
    )

    story = []

    kicker = (
        "STACKCALC LEARNING LAB // OFFICIAL TEACHER & PARENT COACHING KEY"
        if is_teacher
        else "STACKCALC LEARNING LAB // 45-DAY MIDDLE SCHOOL CONFIDENCE & CATCH-UP WORKBOOK"
    )
    main_title = (
        "Big Ideas Math Middle School: Coach Guide & 3-Visit Spiral Solutions"
        if is_teacher
        else "Big Ideas Math Middle School: Daily 'Touch • Stack • Prove' Workbook"
    )
    subtitle = (
        "Complete 10-Chapter, 45-Day Facilitation Playbook, 30-Second Zero-Fail Starters, 5 Variety Game Modes, and Verified SC-6 RPN Stack Snapshots (Grades 6–7 Bridge)."
        if is_teacher
        else "45 Daily 15-Minute Hands-On Missions with 30-Second Zero-Fail Starters, 5 Rotating Variety Game Modes & Skip-Shield Rewards for Reluctant Math Learners."
    )

    story.append(Paragraph(kicker, styles["CoverKicker"]))
    story.append(Paragraph(main_title, styles["CoverTitle"]))
    story.append(Paragraph(subtitle, styles["CoverSub"]))
    story.append(HRFlowable(width="100%", thickness=1.5, color=HexColor("#0F172A"), spaceAfter=6))

    # Explain the 3-Speed Confidence Ramp, 3-Visit Spiral, and Reward Economy on Page 1
    rules_data = [
        [
            Paragraph("<b>1. 30-SEC ZERO-FAIL + 3-SPEED RAMP</b>", styles["TableHeader"]),
            Paragraph("<b>2. 2-NUMBER SNAPSHOT = YOUR WORK</b>", styles["TableHeader"]),
            Paragraph("<b>3. 3-VISIT SPIRAL &amp; SKIP SHIELDS</b>", styles["TableHeader"]),
        ],
        [
            Paragraph(
                "Every day starts with a <b>30-Second Zero-Fail Starter (+5 XP)</b> you can't get wrong, followed by <b>Problem 1 (60-Sec Quick Win)</b>, <b>Problem 2 (Rotating Variety Game)</b>, and <b>Problem 3 (Secret-Genius Boss)</b>!",
                styles["TableCell"],
            ),
            Paragraph(
                "Never copy 6 lines of algebra steps! Your SC-6 4-line elevator holds intermediate numbers on <b>Floor 2 (Y)</b> and <b>Floor 1 (X)</b>. Writing down the 2 numbers on <b>Y</b> and <b>X</b> before your final keypress IS your work!",
                styles["TableCell"],
            ),
            Paragraph(
                "Problems 1 &amp; 2 require <b>ONLY 1 way</b>. On <b>Problem 3</b>, prove 2 different ways match to earn a <b>[2x-STAR]</b>! Every 3 [2x-STAR]s unlocks a <b>[SKIP-SHIELD]</b> (skip any 1 future problem!), and trying all 3 ways unlocks <b>[DEALERS-CHOICE]</b>!",
                styles["TableCell"],
            ),
        ],
    ]
    rules_tbl = Table(rules_data, colWidths=[usable_w / 3.0] * 3)
    rules_tbl.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), HexColor("#064E3B") if not is_teacher else HexColor("#1E3A8A")),
                ("BACKGROUND", (0, 1), (-1, 1), HexColor("#F0FDF4") if not is_teacher else HexColor("#EFF6FF")),
                ("GRID", (0, 0), (-1, -1), 0.6, HexColor("#94A3B8")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(rules_tbl)
    story.append(Spacer(1, 8))

    # 45-Day Pacing, 3-Way Method Passport & Skip-Shield Tracker Table on Page 1
    streak_rows = [
        [
            Paragraph("<b>Chapter &amp; Big Ideas Topic</b>", styles["TableHeader"]),
            Paragraph("<b>Daily 15-Minute Missions</b>", styles["TableHeader"]),
            Paragraph("<b>3-Way Passport</b>", styles["TableHeader"]),
            Paragraph("<b>Twin-Way Stars &amp; Rewards</b>", styles["TableHeader"]),
        ]
    ]
    badge_names = [
        "1. Prime Architect",
        "2. Tower Master",
        "3. Ratio Navigator",
        "4. Tile Alchemist",
        "5. Polygon Engineer",
        "6. Zero-Pair Cmdr",
        "7. Balance Breaker",
        "8. 3D Solid Builder",
        "9. Data Scientist",
        "10. Stack Champion",
    ]
    for idx, ch in enumerate(chapters):
        day_checks = " ".join(f"[ ]D{d['day_num']}" for d in ch["days"])
        b_name = badge_names[idx] if idx < len(badge_names) else f"Badge {idx+1}"
        streak_rows.append(
            [
                Paragraph(clean_inline_md(f"<b>Ch.{ch['num']}:</b> {ch['title'].split('(')[0].strip()}"), styles["TableCell"]),
                Paragraph(clean_inline_md(day_checks), styles["TableCell"]),
                Paragraph(clean_inline_md("[ ]Build [ ]Pat [ ]Stack"), styles["TableCell"]),
                Paragraph(clean_inline_md(f"[ ]** [ ]** [ ]** -> [ ]Shield | [ ]{b_name}"), styles["TableCell"]),
            ]
        )
    streak_tbl = Table(streak_rows, colWidths=[usable_w * 0.27, usable_w * 0.25, usable_w * 0.20, usable_w * 0.28])
    streak_tbl.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), HexColor("#0F172A")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#FFFFFF"), HexColor("#F8FAFC")]),
                ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#CBD5E1")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(streak_tbl)
    story.append(PageBreak())

    # Render each Chapter & its Daily Missions
    for ch in chapters:
        ch_banner = Table(
            [
                [
                    Paragraph(clean_inline_md(f"CHAPTER {ch['num']}: {ch['title']}"), styles["ChapterHeader"]),
                ],
                [
                    Paragraph(clean_inline_md(ch["subtitle"]), styles["ChapterSub"]),
                ],
            ],
            colWidths=[usable_w],
        )
        ch_banner.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), HexColor("#0F172A")),
                    ("TOPPADDING", (0, 0), (-1, 0), 7),
                    ("BOTTOMPADDING", (0, -1), (-1, -1), 7),
                    ("LEFTPADDING", (0, 0), (-1, -1), 10),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ]
            )
        )
        story.append(ch_banner)
        story.append(Spacer(1, 6))

        for day in ch["days"]:
            day_flow = []
            day_flow.append(
                Paragraph(
                    clean_inline_md(f"Day {day['day_num']} (Lesson {day['lesson_num']}): {day['title']}"),
                    styles["DayHeader"],
                )
            )
            if day.get("spiral") or day.get("game_mode"):
                badge_line = f"SPIRAL PATH: {day.get('spiral', '')}   //   VARIETY MODE: {day.get('game_mode', '')}"
                day_flow.append(
                    Paragraph(
                        clean_inline_md(badge_line),
                        styles["SpiralBadge"],
                    )
                )
            if day.get("starter"):
                starter_box = Table(
                    [
                        [
                            Paragraph(
                                clean_inline_md(f"<b>[SPARK] 30-SECOND ZERO-FAIL STARTER (Instant Win #1):</b> {day['starter']}"),
                                styles["HookBox"],
                            )
                        ]
                    ],
                    colWidths=[usable_w],
                )
                starter_box.setStyle(
                    TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, -1), HexColor("#ECFDF5")),
                            ("BOX", (0, 0), (-1, -1), 0.7, HexColor("#10B981")),
                            ("TOPPADDING", (0, 0), (-1, -1), 3.5),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                        ]
                    )
                )
                day_flow.append(starter_box)
                day_flow.append(Spacer(1, 3))

            if day["question"]:
                day_flow.append(
                    Paragraph(clean_inline_md(f"<b>The Real Question:</b> {day['question']}"), styles["BodySmall"])
                )
            if day["hook"] or day.get("why_new"):
                hook_parts = []
                if day["hook"]:
                    hook_parts.append(f"<b>Why Should I Care? (2-Min Hook):</b> {day['hook']}")
                if day.get("why_new"):
                    hook_parts.append(f"<b>Why Try a New Way Today? (When the Old Way Gets Annoying):</b> {day['why_new']}")
                hook_box = Table(
                    [[Paragraph(clean_inline_md("<br/>".join(hook_parts)), styles["HookBox"])]],
                    colWidths=[usable_w],
                )
                hook_box.setStyle(
                    TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, -1), HexColor("#FEF3C7")),
                            ("BOX", (0, 0), (-1, -1), 0.6, HexColor("#F59E0B")),
                            ("TOPPADDING", (0, 0), (-1, -1), 3.5),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                        ]
                    )
                )
                day_flow.append(hook_box)
                day_flow.append(Spacer(1, 3.5))

            dec_tbl = render_markdown_table(day["decoder_lines"], styles, usable_w)
            if dec_tbl is not None:
                day_flow.append(dec_tbl)
                day_flow.append(Spacer(1, 3.5))

            story.append(KeepTogether(day_flow))

            for prob in day["problems"]:
                if is_teacher:
                    t_box = build_teacher_ticket(prob, styles, usable_w)
                else:
                    t_box = build_student_ticket(prob, styles, usable_w)
                story.append(KeepTogether([t_box, Spacer(1, 3.5)]))

            story.append(HRFlowable(width="100%", thickness=0.6, color=HexColor("#CBD5E1"), spaceBefore=3, spaceAfter=5))

        story.append(PageBreak())

    footer_label = (
        "StackCalc SC-6 // Big Ideas Middle School Coach Guide & 3-Visit Spiral Key"
        if is_teacher
        else "StackCalc SC-6 // Big Ideas Middle School Daily Student Workbook (30-Sec Quick Wins & Skip Shields)"
    )
    doc.build(
        story,
        onFirstPage=lambda c, d: add_footer(c, d, footer_label),
        onLaterPages=lambda c, d: add_footer(c, d, footer_label),
    )
    print(f"[OK] Built {output_path} ({output_path.stat().st_size / 1024:.1f} KB)")


def main() -> None:
    sync_markdown_with_spiral_map(SOURCE_MD)
    chapters = parse_workbook_markdown(SOURCE_MD)
    total_days = sum(len(c["days"]) for c in chapters)
    total_probs = sum(len(d["problems"]) for c in chapters for d in c["days"])
    print(f"Parsed {len(chapters)} chapters, {total_days} daily lessons, {total_probs} workout problems.")
    generate_pdf(chapters, STUDENT_PDF, is_teacher=False)
    generate_pdf(chapters, TEACHER_PDF, is_teacher=True)


if __name__ == "__main__":
    main()
