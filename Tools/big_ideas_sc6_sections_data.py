#!/usr/bin/env python3
"""
Authoritative Section-by-Section Textbook Supplement Dataset for Big Ideas Math Middle School (SC-6).

Covers 10 Chapters / 45 Textbook Sections (Grade 6 Complete + Grade 7 Bridge):
- Each section includes:
  * Exact Big Ideas Math textbook section alignment & CCSS standard
  * Manipulative Kit ID & 3D render asset from docs/assets/manuals/
  * Vector Block Schematic specification (diagram_type + diagram_data)
  * 2 Step-by-Step Worked Examples (with physical block steps, SC-6 keycap sequences, and Y|X stack snapshots)
  * 10 Graded Practice Problems (#1-#4 Quick Wins, #5-#8 Guided Section Practice, #9-#10 Real-World & Twin-Way Bonus)
    with full solutions, SC-6 keystrokes, and Y|X snapshots for the 10-page Chapter Coach Guide.
"""

from __future__ import annotations
from typing import Dict, List, Any

CHAPTERS_DATA: List[Dict[str, Any]] = [
    # =========================================================================
    # CHAPTER 1: NUMERICAL EXPRESSIONS & FACTORS (Sections 1.1 - 1.5)
    # =========================================================================
    {
        "num": 1,
        "title": "Numerical Expressions & Factors",
        "big_ideas_book": "Big Ideas Math Grade 6 — Chapter 1",
        "subtitle": "Whole Number Operations, Powers & Exponents, Order of Operations, Prime Factorization, GCF & LCM",
        "kit_summary": "Counting & Array Studio (COUNT-01) + Prime Factor Studio (PRIME-01)",
        "hero_png": "prime_lcm_gcd_venn.png",
        "coach_misconception": "Students interpret remainders as meaningless decimal tails (e.g., .875 of a person), read 2^3 as 2×3=6, lose track of PEMDAS parentheses, and confuse GCF (overlap) with LCM (union).",
        "coach_remediation": "Have students build physical tile rows for division remainders, stack 2D/3D arrays for exponents, use the 4-line elevator (Y holds Room 1 while X solves Room 2) instead of rewriting PEMDAS lines, and stand logarithmic Prime Factor Towers side-by-side on the 12-socket lid.",
        "sections": [
            {
                "day_num": 1,
                "sec_num": "1.1",
                "title": "Whole Number Operations & Division with Remainders",
                "big_ideas_ref": "Big Ideas Grade 6, Section 1.1 (Whole Number Operations)",
                "ccss": "CCSS.MATH.6.NS.B.2",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Array Tiles",
                "asset_png": "counting_tiles_array_3x8.png",
                "diagram_type": "array_rem",
                "diagram_data": {"total": 23, "divisor": 4, "quotient": 5, "rem": 3, "caption": "23 tiles in rows of 4 = 5 full rows (20) + 3 leftover tiles"},
                "concept": "When you divide real items (like 23 tiles into groups of 4), a decimal like 5.75 hides the actual leftover pieces. Grouping physical Counting Tiles shows the full rows (Quotient) and loose tiles (Remainder), while [g] [÷R] puts Quotient on Floor 1 (X) and Remainder on Floor 2 (Y) at the same time!",
                "examples": [
                    {
                        "title": "Example 1: Quotient & Remainder with Blocks + [g] [÷R]",
                        "problem": "Divide 23 ÷ 4 and find the quotient and remainder.",
                        "block_step": "Snap 23 Counting Tiles into rows of 4. You build 5 full rows (20 tiles) with 3 leftover tiles.",
                        "keys": ["23", "ENTER", "4", "g", "÷R"],
                        "stack_y": "3 (Rem)",
                        "stack_x": "5 (Quot)",
                        "ans": "5 R 3",
                        "note": "Floor 1 (X) shows 5 full rows; Floor 2 (Y) shows 3 leftovers!"
                    },
                    {
                        "title": "Example 2: 3-Click Division Proof with [f] [LASTX]",
                        "problem": "Divide 135 ÷ 8 and prove your answer without re-dividing.",
                        "block_step": "After 135 [ENTER] 8 [g] [÷R] gives Y: 7 | X: 16, bring back divisor 8 with [f] [LASTX], multiply, and add the remainder!",
                        "keys": ["135", "ENTER", "8", "g", "÷R", "f", "LASTX", "×", "+"],
                        "stack_y": "7 -> 0",
                        "stack_x": "16 -> 135",
                        "ans": "16 R 7 (Proven: 16×8+7 = 135)",
                        "note": "[f] [LASTX] pulls 8 back; [×] gives 128; [+] adds Y=7 -> 135!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Arrange 31 tiles into rows of 6. Find Quotient & Remainder.", "keys": "31 [ENTER] 6 [g][÷R]", "yx": "Y:1 | X:5", "ans": "5 R 1"},
                    {"num": 2, "part": "A", "prompt": "Divide 47 ÷ 5 using tiles or [g] [÷R].", "keys": "47 [ENTER] 5 [g][÷R]", "yx": "Y:2 | X:9", "ans": "9 R 2"},
                    {"num": 3, "part": "A", "prompt": "Divide 58 ÷ 7 and check with [f] [LASTX] [×] [+].", "keys": "58 [ENTER] 7 [g][÷R]", "yx": "Y:2 | X:8", "ans": "8 R 2"},
                    {"num": 4, "part": "A", "prompt": "Divide 85 ÷ 9. How many full groups of 9 and how many left?", "keys": "85 [ENTER] 9 [g][÷R]", "yx": "Y:4 | X:9", "ans": "9 R 4"},
                    {"num": 5, "part": "B", "prompt": "Divide 146 ÷ 12. Find the Quotient and Remainder.", "keys": "146 [ENTER] 12 [g][÷R]", "yx": "Y:2 | X:12", "ans": "12 R 2"},
                    {"num": 6, "part": "B", "prompt": "Divide 250 ÷ 36 and prove with [f] [LASTX] [×] [+].", "keys": "250 [ENTER] 36 [g][÷R]", "yx": "Y:34 | X:6", "ans": "6 R 34"},
                    {"num": 7, "part": "B", "prompt": "Find the missing dividend: Quotient = 14, Divisor = 8, Remainder = 5.", "keys": "14 [ENTER] 8 [×] 5 [+]", "yx": "Y:112 | X:5", "ans": "117"},
                    {"num": 8, "part": "B", "prompt": "Spot the Glitch: Sam says 75 ÷ 8 = 8 R 11. Why is R=11 impossible? Fix it!", "keys": "75 [ENTER] 8 [g][÷R]", "yx": "Y:3 | X:9", "ans": "9 R 3 (Rem < 8)"},
                    {"num": 9, "part": "C", "prompt": "A 3D spool has 300g of PLA. Each box takes 42g. How many full boxes can you print, and how much PLA is left?", "keys": "300 [ENTER] 42 [g][÷R]", "yx": "Y:6 | X:7", "ans": "7 boxes, 6g left (Way 2: 7×42=294)"},
                    {"num": 10, "part": "C", "prompt": "115 students ride vans that hold 14 kids each. How many vans must be booked so nobody is left behind?", "keys": "115 [ENTER] 14 [g][÷R]", "yx": "Y:3 | X:8", "ans": "9 vans (8 full + 1 for 3 kids; Way 2: 9×14=126)"}
                ]
            },
            {
                "day_num": 2,
                "sec_num": "1.2",
                "title": "Powers & Exponents — Squares, Cubes & Growth",
                "big_ideas_ref": "Big Ideas Grade 6, Section 1.2 (Powers and Exponents)",
                "ccss": "CCSS.MATH.6.EE.A.1",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Array Tiles",
                "asset_png": "counting_tiles_box_3x1x13u.png",
                "diagram_type": "power_array",
                "diagram_data": {"base": 4, "sq": 16, "trap": 8, "caption": "4² = 4×4 square array (16 tiles), NEVER 4×2 (8 tiles)!"},
                "concept": "An exponent tells how many times to use the base as a factor in repeated multiplication. A 2nd power (4²) builds a 2D square array (4×4 = 16 tiles), and a 3rd power (4³) stacks 4 square layers into a 3D cube (64 tiles). Evaluate powers using repeated multiplication or [x²], [g] [x³], and [g] [yˣ]!",
                "examples": [
                    {
                        "title": "Example 1: Squares & Cubes with Tiles and [x²] / [g] [x³]",
                        "problem": "Write 4² and 4³ as repeated multiplication and find their values. Compare 4² to 4 × 2.",
                        "block_step": "Build a 4×4 square of tiles (16 tiles). Stack 4 layers high for 4³ (64 tiles). Notice 4×2 is only 2 rows of 4 (8 tiles)!",
                        "keys": ["4", "x²", "4", "g", "x³"],
                        "stack_y": "16 (4²)",
                        "stack_x": "64 (4³)",
                        "ans": "4² = 16, 4³ = 64",
                        "note": "[x²] squares the base; [g] [x³] cubes the base!"
                    },
                    {
                        "title": "Example 2: Higher Powers via [g] [REP] vs. [g] [yˣ]",
                        "problem": "Evaluate 3⁴ in two different ways on your SC-6.",
                        "block_step": "Way A (Constant Ladder): Press 3 [g] [REP], then tap [×] three times (9 -> 27 -> 81). Way B (Power Key): 3 [ENTER] 4 [g] [yˣ].",
                        "keys": ["3", "ENTER", "4", "g", "yˣ"],
                        "stack_y": "3 (Base)",
                        "stack_x": "4 (Exp)",
                        "ans": "81",
                        "note": "3⁴ = 3 × 3 × 3 × 3 = 81!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Write 5² as repeated multiplication and find how many tiles are in a 5 × 5 square.", "keys": "5 [x²]", "yx": "Y:0 | X:25", "ans": "25"},
                    {"num": 2, "part": "A", "prompt": "Evaluate 7² and compare it to 7 × 2.", "keys": "7 [x²]", "yx": "Y:0 | X:49", "ans": "49 (vs 14)"},
                    {"num": 3, "part": "A", "prompt": "Evaluate 3³ (a 3 × 3 × 3 cube of blocks).", "keys": "3 [g][x³]", "yx": "Y:0 | X:27", "ans": "27"},
                    {"num": 4, "part": "A", "prompt": "Evaluate 5³ using repeated multiplication or [g] [x³].", "keys": "5 [g][x³]", "yx": "Y:0 | X:125", "ans": "125"},
                    {"num": 5, "part": "B", "prompt": "Evaluate 2⁵ by writing the repeated factors and checking with 2 [ENTER] 5 [g] [yˣ].", "keys": "2 [ENTER] 5 [g][yˣ]", "yx": "Y:2 | X:5", "ans": "32"},
                    {"num": 6, "part": "B", "prompt": "Evaluate 6⁴ using repeated multiplication or [g] [yˣ].", "keys": "6 [ENTER] 4 [g][yˣ]", "yx": "Y:6 | X:4", "ans": "1,296"},
                    {"num": 7, "part": "B", "prompt": "Evaluate 10⁴ and 1⁴. How many zeros are in 10⁴?", "keys": "10 [ENTER] 4 [g][yˣ]", "yx": "Y:10 | X:4", "ans": "10,000 and 1"},
                    {"num": 8, "part": "B", "prompt": "Spot the Glitch: Mia wrote 2⁴ = 8 because 2 × 4 = 8. Find the true value of 2⁴.", "keys": "2 [ENTER] 4 [g][yˣ]", "yx": "Y:2 | X:4", "ans": "16 (2×2×2×2)"},
                    {"num": 9, "part": "C", "prompt": "A cell doubles every hour (2ⁿ). How many cells are there after 6 hours (2⁶)? Solve 2 ways!", "keys": "2 [ENTER] 6 [g][yˣ]", "yx": "Y:2 | X:6", "ans": "64 cells (Way 2: 2 [g][REP] [×]×5)"},
                    {"num": 10, "part": "C", "prompt": "Mystery Cube: A giant cube uses 216 unit blocks. How many blocks wide is 1 edge? (Try [g] [ˣ√y]!)", "keys": "216 [ENTER] 3 [g][ˣ√y]", "yx": "Y:216 | X:3", "ans": "6 blocks wide (Way 2: 6 [g][x³]=216)"}
                ]
            },
            {
                "day_num": 3,
                "sec_num": "1.3",
                "title": "Order of Operations — Grouping Symbols, Exponents & PEMDAS",
                "big_ideas_ref": "Big Ideas Grade 6, Section 1.3 (Order of Operations)",
                "ccss": "CCSS.MATH.6.EE.A.1",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Array Tiles",
                "asset_png": "counting_tiles_distributive_4color.png",
                "diagram_type": "two_room",
                "diagram_data": {"room1": "8 + 4 = 12", "room2": "9 - 3 = 6", "op": "×", "res": "72", "caption": "Group 1 (8 + 4 = 12) × Group 2 (9 - 3 = 6) = 12 × 6 = 72!"},
                "concept": "Big Ideas Order of Operations (PEMDAS): (1) Evaluate expressions inside grouping symbols (), [], or fraction bars first; (2) Evaluate powers; (3) Multiply and divide from left to right; (4) Add and subtract from left to right. Grouping tiles on your desk lets you solve each part step by step!",
                "examples": [
                    {
                        "title": "Example 1: Grouping Symbols & Order of Operations",
                        "problem": "Evaluate (8 + 4) × (9 - 3) using the Big Ideas Order of Operations.",
                        "block_step": "Group 1 has 8 + 4 = 12 tiles. Group 2 has 9 - 3 = 6 tiles. Multiply the two groups: 12 × 6 = 72!",
                        "keys": ["8", "ENTER", "4", "+", "9", "ENTER", "3", "-", "×"],
                        "stack_y": "12 (Group 1)",
                        "stack_x": "6 (Group 2)",
                        "ans": "72",
                        "note": "(8 + 4) × (9 - 3) = 12 × 6 = 72!"
                    },
                    {
                        "title": "Example 2: Exponents & Multi-Step PEMDAS",
                        "problem": "Evaluate 40 - 3 × (2 + 3)² ÷ 5 step by step.",
                        "block_step": "Parentheses: (2+3)=5. Exponent: 5²=25. Multiply/Divide left-to-right: 3×25=75, 75÷5=15. Subtract: 40-15=25!",
                        "keys": ["40", "ENTER", "3", "ENTER", "2", "ENTER", "3", "+", "x²", "×", "5", "÷", "-"],
                        "stack_y": "40",
                        "stack_x": "15",
                        "ans": "25",
                        "note": "40 - 3(25) ÷ 5 = 40 - 75 ÷ 5 = 40 - 15 = 25!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Evaluate 5 + 2 × 3. Multiply before adding!", "keys": "5 [ENTER] 2 [ENTER] 3 [×] [+]", "yx": "Y:5 | X:6", "ans": "11"},
                    {"num": 2, "part": "A", "prompt": "Evaluate (14 + 6) ÷ (7 - 2). Solve both parentheses first!", "keys": "14 [ENTER] 6 [+] 7 [ENTER] 2 [-] [÷]", "yx": "Y:20 | X:5", "ans": "4"},
                    {"num": 3, "part": "A", "prompt": "Evaluate 30 - 4 × 6.", "keys": "30 [ENTER] 4 [ENTER] 6 [×] [-]", "yx": "Y:30 | X:24", "ans": "6"},
                    {"num": 4, "part": "A", "prompt": "Evaluate (9 + 3) × (15 - 8).", "keys": "9 [ENTER] 3 [+] 15 [ENTER] 8 [-] [×]", "yx": "Y:12 | X:7", "ans": "84"},
                    {"num": 5, "part": "B", "prompt": "Evaluate 50 - (3 + 4)². Square the sum before subtracting from 50!", "keys": "50 [ENTER] 3 [ENTER] 4 [+] [x²] [-]", "yx": "Y:50 | X:49", "ans": "1"},
                    {"num": 6, "part": "B", "prompt": "Evaluate 120 - 4 × (3 + 2)².", "keys": "120 [ENTER] 4 [ENTER] 3 [ENTER] 2 [+] [x²] [×] [-]", "yx": "Y:120 | X:100", "ans": "20"},
                    {"num": 7, "part": "B", "prompt": "Fraction Bar Grouping: Evaluate (24 + 12) / (9 - 3).", "keys": "24 [ENTER] 12 [+] 9 [ENTER] 3 [-] [÷]", "yx": "Y:36 | X:6", "ans": "6"},
                    {"num": 8, "part": "B", "prompt": "Evaluate 3³ + 15 ÷ 3 - 2 × 4.", "keys": "3 [g][x³] 15 [ENTER] 3 [÷] [+] 2 [ENTER] 4 [×] [-]", "yx": "Y:32 | X:8", "ans": "24"},
                    {"num": 9, "part": "C", "prompt": "Evaluate 10 + (15 - 3)² ÷ 9 using PEMDAS step-by-step AND check on your SC-6.", "keys": "10 [ENTER] 15 [ENTER] 3 [-] [x²] 9 [÷] [+]", "yx": "Y:10 | X:16", "ans": "26 (Way 2: 10 + 144÷9 = 26)"},
                    {"num": 10, "part": "C", "prompt": "Movie tickets: 2 adults at $12 each and 4 kids at $8 each, minus a $10 coupon. Write an expression and find total cost.", "keys": "2 [ENTER] 12 [×] 4 [ENTER] 8 [×] [+] 10 [-]", "yx": "Y:56 | X:10", "ans": "$46 (Way 2: 24 + 32 - 10 = 46)"}
                ]
            },
            {
                "day_num": 4,
                "sec_num": "1.4",
                "title": "Prime Factorization — Factor Trees & Logarithmic Prime Towers",
                "big_ideas_ref": "Big Ideas Grade 6, Section 1.4 (Prime Factorization)",
                "ccss": "CCSS.MATH.6.NS.B.4",
                "kit_id": "PRIME-01",
                "kit_name": "Prime Factor Studio",
                "asset_png": "prime_studio_comparator_stage.png",
                "diagram_type": "prime_tower",
                "diagram_data": {"num": 60, "blocks": [2, 2, 3, 5], "caption": "Tower 60 = [2] + [2] + [3] + [5]. Rearranging order never changes tower height!"},
                "concept": "In Big Ideas Math, a Factor Tree splits a composite number until every branch ends at a prime number. In the Prime Factor Studio (PRIME-01), block heights are logarithmic (h = 7·log₂(p) mm), so [2]+[2]+[3]+[5] always reaches the exact 60 mark whether you split 60 as 6×10 or 4×15!",
                "examples": [
                    {
                        "title": "Example 1: Factor Tree & Prime Tower for 60",
                        "problem": "Write the prime factorization of 60 using a factor tree, Prime Blocks, and [g] [FACT].",
                        "block_step": "Stack two [2] blocks, one [3] block, and one [5] block on the lid—their combined height aligns with 60 on the box wall!",
                        "keys": ["60", "g", "FACT"],
                        "stack_y": "60 = 6×10",
                        "stack_x": "2² × 3 × 5",
                        "ans": "60 = 2² × 3 × 5",
                        "note": "[PRIME] tests primality; [g] [FACT] ([g][PRIME]) shows prime powers!"
                    },
                    {
                        "title": "Example 2: Rebuilding a Mystery Prime Tower",
                        "problem": "Which number has the prime factorization 2³ × 3 × 5?",
                        "block_step": "Multiply 2³ (8) × 3 (24) × 5 (120), then press [g] [FACT] to verify!",
                        "keys": ["2", "g", "x³", "3", "×", "5", "×"],
                        "stack_y": "24",
                        "stack_x": "5 -> 120",
                        "ans": "120",
                        "note": "Check: 120 [g] [FACT] immediately displays 2³ × 3 × 5!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Draw a factor tree or stack [2] + [2] + [3]. Write the prime factorization of 12.", "keys": "12 [g][FACT]", "yx": "Y:0 | X:12", "ans": "2² × 3"},
                    {"num": 2, "part": "A", "prompt": "Find the prime factorization of 36 using blocks and [g] [FACT].", "keys": "36 [g][FACT]", "yx": "Y:0 | X:36", "ans": "2² × 3²"},
                    {"num": 3, "part": "A", "prompt": "Test 29 and 57 with [PRIME]. Which one is prime and which is composite?", "keys": "29 [PRIME], 57 [g][FACT]", "yx": "57 = 3×19", "ans": "29 Prime; 57 Composite (3×19)"},
                    {"num": 4, "part": "A", "prompt": "Find the prime factorization of 45.", "keys": "45 [g][FACT]", "yx": "Y:0 | X:45", "ans": "3² × 5"},
                    {"num": 5, "part": "B", "prompt": "Build the Prime Tower for 72. Show how 8 × 9 and 6 × 12 use the exact same blocks.", "keys": "72 [g][FACT]", "yx": "Y:0 | X:72", "ans": "2³ × 3²"},
                    {"num": 6, "part": "B", "prompt": "Find the prime factorization of 84.", "keys": "84 [g][FACT]", "yx": "Y:0 | X:84", "ans": "2² × 3 × 7"},
                    {"num": 7, "part": "B", "prompt": "Find the prime factorization of 100.", "keys": "100 [g][FACT]", "yx": "Y:0 | X:100", "ans": "2² × 5²"},
                    {"num": 8, "part": "B", "prompt": "What number has the prime tower [2] + [2] + [3] + [7] (2² × 3 × 7)?", "keys": "2 [x²] 3 [×] 7 [×]", "yx": "Y:12 | X:7", "ans": "84"},
                    {"num": 9, "part": "C", "prompt": "Find the prime factorization of 180 both by splitting 18 × 10 AND with [g] [FACT].", "keys": "180 [g][FACT]", "yx": "Y:0 | X:180", "ans": "2² × 3² × 5 (Way 2: (2·3²)(2·5))"},
                    {"num": 10, "part": "C", "prompt": "Mystery Vault Code: A 3-digit number equals 2³ × 3² × 5. Find the number and verify with [g] [FACT].", "keys": "2 [g][x³] 3 [x²] [×] 5 [×]", "yx": "Y:72 | X:5", "ans": "360 (Way 2: 8 × 9 × 5 = 360)"}
                ]
            },
            {
                "day_num": 5,
                "sec_num": "1.5",
                "title": "Greatest Common Factor (GCF) & Least Common Multiple (LCM)",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 1.5 & 1.6 (GCF and LCM)",
                "ccss": "CCSS.MATH.6.NS.B.4",
                "kit_id": "PRIME-01",
                "kit_name": "Prime Factor Studio",
                "asset_png": "prime_lcm_gcd_venn.png",
                "diagram_type": "gcf_lcm_towers",
                "diagram_data": {"a": 20, "b": 50, "gcf": 10, "lcm": 100, "caption": "Towers 20 ([2][2][5]) & 50 ([2][5][5]): Shared overlap = GCF 10; Tallest union = LCM 100"},
                "concept": "When you stand two Prime Factor Towers next to each other on the 12-socket lid, you see GCF and LCM at the same time: GCF is the shared blocks both towers have in common (overlap), and LCM is the tallest tower needed to cover both (union)! Verify in 1 click with [GCF] and [f] [LCM].",
                "examples": [
                    {
                        "title": "Example 1: Simultaneous GCF & LCM of 20 and 50",
                        "problem": "Find both the GCF and LCM of 20 and 50 using Prime Towers and the SC-6.",
                        "block_step": "Tower 20 is [2][2][5] and Tower 50 is [2][5][5]. Both share [2][5] = 10 (GCF). Taking the max of each color gives [2][2][5][5] = 100 (LCM)!",
                        "keys": ["20", "ENTER", "50", "GCF", "20", "ENTER", "50", "f", "LCM"],
                        "stack_y": "10 (GCF)",
                        "stack_x": "100 (LCM)",
                        "ans": "GCF = 10, LCM = 100",
                        "note": "Check: GCF × LCM = 10 × 100 = 1,000, matching 20 × 50 = 1,000!"
                    },
                    {
                        "title": "Example 2: Listing All Common Factors with [f] [C.FAC]",
                        "problem": "Find the GCF and all common factors of 18 and 24.",
                        "block_step": "Tower 18 ([2][3][3]) and Tower 24 ([2][2][2][3]) share [2][3] = 6. Press [f] [C.FAC] ([f][PRIME]) to see every shared factor!",
                        "keys": ["18", "ENTER", "24", "GCF"],
                        "stack_y": "18 | 24",
                        "stack_x": "6 (GCF)",
                        "ans": "GCF = 6, LCM = 72",
                        "note": "18 [ENTER] 24 [f] [LCM] gives 72 ([2][2][2][3][3])!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the GCF and LCM of 12 and 18 using Prime Towers and [GCF] / [f] [LCM].", "keys": "12 [ENTER] 18 [GCF] / [f][LCM]", "yx": "Y:6 | X:36", "ans": "GCF = 6, LCM = 36"},
                    {"num": 2, "part": "A", "prompt": "Find the GCF and LCM of 8 and 12.", "keys": "8 [ENTER] 12 [GCF] / [f][LCM]", "yx": "Y:4 | X:24", "ans": "GCF = 4, LCM = 24"},
                    {"num": 3, "part": "A", "prompt": "Find the GCF and LCM of 15 and 25.", "keys": "15 [ENTER] 25 [GCF] / [f][LCM]", "yx": "Y:5 | X:75", "ans": "GCF = 5, LCM = 75"},
                    {"num": 4, "part": "A", "prompt": "Find the GCF and LCM of 14 and 35.", "keys": "14 [ENTER] 35 [GCF] / [f][LCM]", "yx": "Y:7 | X:70", "ans": "GCF = 7, LCM = 70"},
                    {"num": 5, "part": "B", "prompt": "Find the GCF and LCM of 16 and 24.", "keys": "16 [ENTER] 24 [GCF] / [f][LCM]", "yx": "Y:8 | X:48", "ans": "GCF = 8, LCM = 48"},
                    {"num": 6, "part": "B", "prompt": "Find the GCF and LCM of 28 and 42.", "keys": "28 [ENTER] 42 [GCF] / [f][LCM]", "yx": "Y:14 | X:84", "ans": "GCF = 14, LCM = 84"},
                    {"num": 7, "part": "B", "prompt": "Two prime numbers are 5 and 7. What is their GCF and what is their LCM?", "keys": "5 [ENTER] 7 [GCF] / [f][LCM]", "yx": "Y:1 | X:35", "ans": "GCF = 1, LCM = 35"},
                    {"num": 8, "part": "B", "prompt": "Verify that GCF(15, 20) × LCM(15, 20) equals 15 × 20.", "keys": "15 [ENTER] 20 [GCF] ... [×]", "yx": "Y:5 | X:60", "ans": "5 × 60 = 300 (Matches 15×20!)"},
                    {"num": 9, "part": "C", "prompt": "Hot dogs come in packs of 12 and buns in packs of 15. What is the smallest number of each to buy with 0 leftovers?", "keys": "12 [ENTER] 15 [f][LCM]", "yx": "Y:12 | X:15", "ans": "60 (5 packs dogs, 4 packs buns; Way 2: [g][REP] skip-count)"},
                    {"num": 10, "part": "C", "prompt": "You have 36 red tiles and 48 blue tiles to pack into identical kit bags with none left over. What is the max number of bags?", "keys": "36 [ENTER] 48 [GCF]", "yx": "Y:36 | X:48", "ans": "12 bags (3 red, 4 blue per bag; Way 2: Prime overlap 2²×3=12)"}
                ]
            }
        ]
    },

    # =========================================================================
    # CHAPTER 2: FRACTIONS & DECIMALS (Sections 2.1 - 2.5)
    # =========================================================================
    {
        "num": 2,
        "title": "Fractions & Decimals",
        "big_ideas_book": "Big Ideas Math Grade 6 — Chapter 2",
        "subtitle": "Equivalent Fractions, Multiplying & Dividing Fractions, and All Four Decimal Operations",
        "kit_summary": "Fraction Studio (FRAC-01) + Place Value Studio (PLACE-01)",
        "hero_png": "fraction_studio_common_denominator.png",
        "coach_misconception": "Students treat fractions, mixed numbers, and decimals as unrelated rules, expect multiplication to always make numbers bigger, forget which fraction to flip in division, and misalign decimal columns.",
        "coach_remediation": "Use the 84.0 mm Fraction Studio towers so equivalence and common denominators are physical millimeter height matches. Use [f] [1/x] on Floor 1 (X) so students see only the divisor flip, and use [f] [IP] / [g] [FP] to split whole dollars from decimal cents.",
        "sections": [
            {
                "day_num": 6,
                "sec_num": "2.1",
                "title": "Equivalent Fractions, Mixed Numbers & Adding Towers",
                "big_ideas_ref": "Big Ideas Grade 6, Section 2.1 Prep (Equivalence, Mixed Numbers & Like/Unlike Fractions)",
                "ccss": "CCSS.MATH.6.NS.A.1",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_common_denominator.png",
                "diagram_type": "fraction_towers",
                "diagram_data": {"towers": [("1 Whole", [84], "84mm"), ("2/3", [28, 28], "56mm"), ("4/6", [14, 14, 14, 14], "56mm"), ("1/3+1/4", [28, 21], "49mm = 7/12")], "caption": "84.0 mm Whole Datum: 2/3 and 4/6 are both 56.0 mm tall; 1/3 (28mm) + 1/4 (21mm) = 49mm (7/12)"},
                "concept": "In the Fraction Studio (FRAC-01), 1 Whole is exactly 84.0 mm tall. Whenever two fraction towers stand at the exact same millimeter height, they are equivalent! Use [.] to enter fractions (e.g., [.] 4 [.] 6), [g] [SIMP] to simplify step-by-step, [f] [d/c] for improper fractions, and [FDISP] to toggle decimal view!",
                "examples": [
                    {
                        "title": "Example 1: Step-by-Step Simplification with [g] [SIMP]",
                        "problem": "Simplify 12/18 step-by-step and compare tower heights.",
                        "block_step": "Four 1/6 blocks (4 × 14mm = 56mm) stand at the exact same height as two 1/3 blocks (2 × 28mm = 56mm).",
                        "keys": [".", "12", ".", "18", "ENTER", "g", "SIMP", "g", "SIMP"],
                        "stack_y": "6/9 (Step 1)",
                        "stack_x": "2/3 (Final)",
                        "ans": "12/18 -> 6/9 -> 2/3",
                        "note": "Each press of [g] [SIMP] ([g][a b/c]) divides out one common factor!"
                    },
                    {
                        "title": "Example 2: Mixed Numbers <-> Improper <-> Decimal",
                        "problem": "Convert 1 3/4 to an improper fraction and a decimal, then add 1/3 + 1/4.",
                        "block_step": "1 Whole (84mm) + three 1/4s (63mm) = seven 1/4s (147mm). For 1/3 + 1/4, 28mm + 21mm = 49mm = seven 1/12 blocks (7/12)!",
                        "keys": ["1", ".", "3", ".", "4", "ENTER", "f", "d/c", "FDISP"],
                        "stack_y": "7/4",
                        "stack_x": "1.75",
                        "ans": "7/4 = 1.75; and 1/3 + 1/4 = 7/12",
                        "note": "[f] [d/c] shows 7/4; [FDISP] toggles between 1 3/4 and 1.75!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Simplify 8/12 using [g] [SIMP]. What intermediate fraction appears first?", "keys": "[.] 8 [.] 12 [ENTER] [g][SIMP]×2", "yx": "4/6 -> 2/3", "ans": "4/6 -> 2/3"},
                    {"num": 2, "part": "A", "prompt": "Simplify 24/36 completely and check its decimal with [FDISP].", "keys": "[.] 24 [.] 36 [ENTER] [g][SIMP]...", "yx": "12/18->6/9->2/3", "ans": "2/3 (0.667)"},
                    {"num": 3, "part": "A", "prompt": "Convert 2 3/5 into an improper fraction ([f] [d/c]) and a decimal ([FDISP]).", "keys": "2 [.] 3 [.] 5 [ENTER] [f][d/c]", "yx": "13/5 | 2.6", "ans": "13/5 and 2.6"},
                    {"num": 4, "part": "A", "prompt": "Convert 19/8 into a mixed number ([a b/c]) and a decimal ([FDISP]).", "keys": "[.] 19 [.] 8 [ENTER] [FDISP]", "yx": "2 3/8 | 2.375", "ans": "2 3/8 and 2.375"},
                    {"num": 5, "part": "B", "prompt": "Add 1/2 + 1/3 using a common denominator (sixths) and check with 84mm Fraction Blocks.", "keys": "[.] 1 [.] 2 [ENTER] [.] 1 [.] 3 [+]", "yx": "Y:1/2 | X:1/3", "ans": "5/6 (42mm+28mm=70mm)"},
                    {"num": 6, "part": "B", "prompt": "Add 3/4 + 5/6 using the LCD (12). Write both the mixed number and improper fraction.", "keys": "[.] 3 [.] 4 [ENTER] [.] 5 [.] 6 [+]", "yx": "Y:3/4 | X:5/6", "ans": "1 7/12 (or 19/12)"},
                    {"num": 7, "part": "B", "prompt": "Subtract 7/8 - 1/4 and verify with [f] [LASTX] [+].", "keys": "[.] 7 [.] 8 [ENTER] [.] 1 [.] 4 [-]", "yx": "Y:7/8 | X:1/4", "ans": "5/8"},
                    {"num": 8, "part": "B", "prompt": "Subtract mixed numbers: 4 1/3 - 1 5/6.", "keys": "4 [.] 1 [.] 3 [ENTER] 1 [.] 5 [.] 6 [-]", "yx": "Y:4 1/3 | X:1 5/6", "ans": "2 1/2 (or 5/2)"},
                    {"num": 9, "part": "C", "prompt": "Build 1/3 + 1/4 with 84mm towers (28mm + 21mm) AND solve using the LCD (twelfths).", "keys": "[.] 1 [.] 3 [ENTER] [.] 1 [.] 4 [+]", "yx": "Y:1/3 | X:1/4", "ans": "7/12 (49mm = seven 7mm twelfths)"},
                    {"num": 10, "part": "C", "prompt": "A trail is 3 3/4 miles long. You hiked 1 7/8 miles. How much trail is left? Solve 2 ways!", "keys": "3 [.] 3 [.] 4 [ENTER] 1 [.] 7 [.] 8 [-]", "yx": "Y:3.75 | X:1.875", "ans": "1 7/8 miles (Way 2: 30/8 - 15/8 = 15/8)"}
                ]
            },
            {
                "day_num": 7,
                "sec_num": "2.2",
                "title": "Multiplying Fractions & Mixed Numbers",
                "big_ideas_ref": "Big Ideas Grade 6, Section 2.1 (Multiplying Fractions)",
                "ccss": "CCSS.MATH.6.NS.A.1",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_twin_comparator.png",
                "diagram_type": "fraction_towers",
                "diagram_data": {"towers": [("3/4 Tower", [21, 21, 21], "63.0mm"), ("1/2 of 3/4", [10.5, 10.5, 10.5], "31.5mm = 3/8")], "caption": "Taking 1/2 OF a 3/4 tower (63mm) gives a 31.5mm tower = three 1/8 blocks (3/8)!"},
                "concept": "Why does multiplying two proper fractions make a SMALLER answer? Because '×' means 'OF'! Taking 1/2 OF a 3/4 tower (63 mm) gives half its height (31.5 mm = 3/8). For mixed numbers, rewrite as improper fractions first (or use [f] [d/c]) and simplify common factors before multiplying!",
                "examples": [
                    {
                        "title": "Example 1: Fraction OF a Fraction (1/2 × 3/4)",
                        "problem": "Find 1/2 × 3/4 using 84mm Fraction Towers and the SC-6.",
                        "block_step": "Stand three 1/4 blocks (63 mm). Half of 63 mm is 31.5 mm, which matches three 1/8 blocks (3 × 10.5 mm = 3/8)!",
                        "keys": [".", "1", ".", "2", "ENTER", ".", "3", ".", "4", "×"],
                        "stack_y": "1/2",
                        "stack_x": "3/4",
                        "ans": "3/8",
                        "note": "Check with [f] [LASTX] [÷] -> restores 1/2 immediately!"
                    },
                    {
                        "title": "Example 2: Multiplying Mixed Numbers (1 1/2 × 2 2/3)",
                        "problem": "Multiply 1 1/2 × 2 2/3 by converting to improper fractions.",
                        "block_step": "Rewrite 1 1/2 = 3/2 and 2 2/3 = 8/3. Cross-cancel the 3s and simplify 8/2 = 4!",
                        "keys": ["1", ".", "1", ".", "2", "ENTER", "2", ".", "2", ".", "3", "×"],
                        "stack_y": "1 1/2 (3/2)",
                        "stack_x": "2 2/3 (8/3)",
                        "ans": "4",
                        "note": "Cross-canceling 3/2 × 8/3 cancels the 3s and gives 8/2 = 4!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find 1/2 × 2/3. (Hold two 1/3 blocks and take half of them!)", "keys": "[.] 1 [.] 2 [ENTER] [.] 2 [.] 3 [×]", "yx": "Y:1/2 | X:2/3", "ans": "1/3"},
                    {"num": 2, "part": "A", "prompt": "Find 2/3 × 3/4 and check with [f] [LASTX] [÷].", "keys": "[.] 2 [.] 3 [ENTER] [.] 3 [.] 4 [×]", "yx": "Y:2/3 | X:3/4", "ans": "1/2"},
                    {"num": 3, "part": "A", "prompt": "Multiply 3/5 × 5/9.", "keys": "[.] 3 [.] 5 [ENTER] [.] 5 [.] 9 [×]", "yx": "Y:3/5 | X:5/9", "ans": "1/3"},
                    {"num": 4, "part": "A", "prompt": "Multiply a whole number by a fraction: 12 × 3/4.", "keys": "12 [ENTER] [.] 3 [.] 4 [×]", "yx": "Y:12 | X:3/4", "ans": "9"},
                    {"num": 5, "part": "B", "prompt": "Multiply mixed numbers: 1 3/4 × 2 2/7.", "keys": "1 [.] 3 [.] 4 [ENTER] 2 [.] 2 [.] 7 [×]", "yx": "Y:7/4 | X:16/7", "ans": "4"},
                    {"num": 6, "part": "B", "prompt": "Multiply 2 1/4 × 1 1/3.", "keys": "2 [.] 1 [.] 4 [ENTER] 1 [.] 1 [.] 3 [×]", "yx": "Y:9/4 | X:4/3", "ans": "3"},
                    {"num": 7, "part": "B", "prompt": "Multiply 3 1/2 × 2 1/2. Write the answer as a mixed number and decimal.", "keys": "3 [.] 1 [.] 2 [ENTER] 2 [.] 1 [.] 2 [×]", "yx": "Y:3 1/2 | X:2 1/2", "ans": "8 3/4 (8.75)"},
                    {"num": 8, "part": "B", "prompt": "Prediction Check: Without calculating, is 5 × 2/3 greater than 5 or less than 5? Now compute it!", "keys": "5 [ENTER] [.] 2 [.] 3 [×]", "yx": "Y:5 | X:2/3", "ans": "3 1/3 (Less than 5!)"},
                    {"num": 9, "part": "C", "prompt": "A slime recipe uses 1 3/4 cups of glue per batch. How much glue is needed for 2 1/2 batches?", "keys": "1 [.] 3 [.] 4 [ENTER] 2 [.] 1 [.] 2 [×]", "yx": "Y:7/4 | X:5/2", "ans": "4 3/8 cups (Way 2: 1.75 × 2.5 = 4.375)"},
                    {"num": 10, "part": "C", "prompt": "Triple Chain: Evaluate 4/5 × 5/6 × 3/4 both by cross-canceling common factors AND on your SC-6!", "keys": "[.] 4 [.] 5 [ENTER] [.] 5 [.] 6 [×] [.] 3 [.] 4 [×]", "yx": "Y:2/3 | X:3/4", "ans": "1/2 (Way 2: cancel 4s & 5s -> 3/6 = 1/2)"}
                ]
            },
            {
                "day_num": 8,
                "sec_num": "2.3",
                "title": "Dividing Fractions & Mixed Numbers — Why Reciprocal Flip Works",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 2.2 & 2.3 (Dividing Fractions and Mixed Numbers)",
                "ccss": "CCSS.MATH.6.NS.A.1",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "counting_tiles_fraction_datum_84mm.png",
                "diagram_type": "fraction_towers",
                "diagram_data": {"towers": [("3/4 Tower", [21, 21, 21], "63.0mm"), ("Six 1/8s", [10.5]*6, "6 × 10.5mm = 63mm")], "caption": "3/4 ÷ 1/8 asks: 'How many 1/8 blocks (10.5mm) fit inside a 3/4 tower (63mm)?' -> 6 blocks!"},
                "concept": "Kids memorize 'Keep-Change-Flip' and then forget which fraction to flip! Physically, 3/4 ÷ 1/8 asks how many 1/8 blocks fit alongside a 3/4 tower (6 fit!). In Big Ideas Math, dividing by a fraction equals multiplying by its reciprocal—and [f] [1/x] flips ONLY the divisor into its reciprocal before you press [×]!",
                "examples": [
                    {
                        "title": "Example 1: Physical Tower Fit vs. [f] [1/x] Reciprocal Flip",
                        "problem": "Divide 3/4 ÷ 1/8 by comparing tower heights and by multiplying by the reciprocal with [f] [1/x].",
                        "block_step": "One 1/4 block (21mm) holds two 1/8 blocks (10.5mm). So three 1/4 blocks hold 3 × 2 = 6 eighths!",
                        "keys": [".", "3", ".", "4", "ENTER", ".", "1", ".", "8", "f", "1/x", "×"],
                        "stack_y": "3/4 (Kept)",
                        "stack_x": "8 (Flipped!)",
                        "ans": "6",
                        "note": "[f] [1/x] ([f][FDISP]) flips 1/8 into its reciprocal 8/1, then [×] gives 6!"
                    },
                    {
                        "title": "Example 2: Dividing Mixed Numbers (6 3/4 ÷ 1 1/8)",
                        "problem": "Solve 6 3/4 ÷ 1 1/8 and check with [f] [LASTX] [×].",
                        "block_step": "Rewrite 6 3/4 = 27/4 and 1 1/8 = 9/8. Multiply by the reciprocal: 27/4 × 8/9 = 6!",
                        "keys": ["6", ".", "3", ".", "4", "ENTER", "1", ".", "1", ".", "8", "÷"],
                        "stack_y": "6 3/4 (27/4)",
                        "stack_x": "1 1/8 (9/8)",
                        "ans": "6",
                        "note": "Check: 6 [f] [LASTX] [×] multiplies 6 × 1 1/8 = 6 3/4!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "How many 1/4 blocks fit in a 1/2 tower? Compute 1/2 ÷ 1/4.", "keys": "[.] 1 [.] 2 [ENTER] [.] 1 [.] 4 [÷]", "yx": "Y:1/2 | X:1/4", "ans": "2"},
                    {"num": 2, "part": "A", "prompt": "How many 1/6 blocks (14mm) fit in a 2/3 tower (56mm)? Compute 2/3 ÷ 1/6.", "keys": "[.] 2 [.] 3 [ENTER] [.] 1 [.] 6 [÷]", "yx": "Y:2/3 | X:1/6", "ans": "4"},
                    {"num": 3, "part": "A", "prompt": "Divide 5/6 ÷ 5/12 by multiplying by the reciprocal ([f] [1/x] [×]).", "keys": "[.] 5 [.] 6 [ENTER] [.] 5 [.] 12 [f][1/x] [×]", "yx": "Y:5/6 | X:12/5", "ans": "2"},
                    {"num": 4, "part": "A", "prompt": "Divide a whole number by a fraction: 6 ÷ 3/4.", "keys": "6 [ENTER] [.] 3 [.] 4 [÷]", "yx": "Y:6 | X:3/4", "ans": "8"},
                    {"num": 5, "part": "B", "prompt": "Divide 3/4 ÷ 2/5. Write the answer as a mixed number.", "keys": "[.] 3 [.] 4 [ENTER] [.] 2 [.] 5 [÷]", "yx": "Y:3/4 | X:2/5", "ans": "1 7/8 (15/8)"},
                    {"num": 6, "part": "B", "prompt": "Divide a fraction by a whole number: 4/5 ÷ 2.", "keys": "[.] 4 [.] 5 [ENTER] 2 [÷]", "yx": "Y:4/5 | X:2", "ans": "2/5"},
                    {"num": 7, "part": "B", "prompt": "Divide mixed numbers: 4 1/2 ÷ 3/4.", "keys": "4 [.] 1 [.] 2 [ENTER] [.] 3 [.] 4 [÷]", "yx": "Y:4 1/2 | X:3/4", "ans": "6"},
                    {"num": 8, "part": "B", "prompt": "Divide 5 1/4 ÷ 1 3/4 and prove with [f] [LASTX] [×].", "keys": "5 [.] 1 [.] 4 [ENTER] 1 [.] 3 [.] 4 [÷]", "yx": "Y:5 1/4 | X:1 3/4", "ans": "3"},
                    {"num": 9, "part": "C", "prompt": "A board is 6 3/4 ft long. You cut it into 3/4-ft shelves. How many shelves can you cut? Solve 2 ways!", "keys": "6 [.] 3 [.] 4 [ENTER] [.] 3 [.] 4 [÷]", "yx": "Y:27/4 | X:3/4", "ans": "9 shelves (Way 2: 27 fourths ÷ 3 fourths = 9)"},
                    {"num": 10, "part": "C", "prompt": "A 3 3/4-cup pitcher of smoothie is poured into 5/8-cup glasses. How many glasses does it fill?", "keys": "3 [.] 3 [.] 4 [ENTER] [.] 5 [.] 8 [÷]", "yx": "Y:15/4 | X:5/8", "ans": "6 glasses (Way 2: 30/8 ÷ 5/8 = 6)"}
                ]
            },
            {
                "day_num": 9,
                "sec_num": "2.4",
                "title": "Adding, Subtracting & Multiplying Decimals",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 2.4 & 2.5 (Adding, Subtracting, and Multiplying Decimals)",
                "ccss": "CCSS.MATH.6.NS.B.3",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "place_value",
                "diagram_data": {"num": "14.85", "ip": "14", "fp": "0.85", "caption": "Place Value Studio: [f] [IP] isolates Whole Dollars (14); [g] [FP] isolates Decimal Cents (0.85)"},
                "concept": "Paper decimal errors happen when place-value columns drift or decimal places are miscounted in multiplication. Use the Place Value Studio (PLACE-01) and the [f] [IP] (Integer Part) and [g] [FP] (Fractional Part) keys to align Tenths and Hundredths and estimate whole-number products first!",
                "examples": [
                    {
                        "title": "Example 1: Aligning Decimal Place Values ([f] [IP] & [g] [FP])",
                        "problem": "Split 14.85 into its whole and decimal parts, then compute 14.60 + 3.85.",
                        "block_step": "On the Place Value tray, 14 sits in the Tens/Ones bays ([f] [IP] -> 14) and .85 sits in Tenths/Hundredths ([g] [FP] -> 0.85).",
                        "keys": ["14.6", "ENTER", "3.85", "+", "f", "LASTX", "-"],
                        "stack_y": "14.6",
                        "stack_x": "3.85 -> 18.45",
                        "ans": "18.45 (Checked: 18.45 - 3.85 = 14.6)",
                        "note": "[f] [IP] ([f][PV]) shows whole part; [g] [FP] ([g][PV]) shows decimal part!"
                    },
                    {
                        "title": "Example 2: Multiplying Decimals + Whole-Number Estimate",
                        "problem": "Evaluate 3.6 × 2.25 and check with [FDISP] fraction costume.",
                        "block_step": "First check whole parts: 4 × 2 = 8, so the answer must be near 8 (never 81 or 0.81!). Multiply and tap [FDISP].",
                        "keys": ["3.6", "ENTER", "2.25", "×", "FDISP"],
                        "stack_y": "3.6",
                        "stack_x": "2.25 -> 8.1",
                        "ans": "8.1 (or 8 1/10)",
                        "note": "[FDISP] confirms 8.1 = 8 1/10 = 81/10!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Enter 27.64. Use [f] [IP] and [g] [FP] to write its Whole part and Decimal part.", "keys": "27.64 [f][IP] / [g][FP]", "yx": "IP:27 | FP:0.64", "ans": "Whole = 27, Decimal = 0.64"},
                    {"num": 2, "part": "A", "prompt": "Line up the decimal points to add 12.8 + 4.75, and check with [f] [LASTX] [-].", "keys": "12.8 [ENTER] 4.75 [+]", "yx": "Y:12.8 | X:4.75", "ans": "17.55"},
                    {"num": 3, "part": "A", "prompt": "Annex zeros to subtract 20.00 - 8.65.", "keys": "20 [ENTER] 8.65 [-]", "yx": "Y:20 | X:8.65", "ans": "11.35"},
                    {"num": 4, "part": "A", "prompt": "Multiply 4.5 × 0.6.", "keys": "4.5 [ENTER] 0.6 [×]", "yx": "Y:4.5 | X:0.6", "ans": "2.7"},
                    {"num": 5, "part": "B", "prompt": "Evaluate 25.4 - 9.86 + 3.2.", "keys": "25.4 [ENTER] 9.86 [-] 3.2 [+]", "yx": "Y:15.54 | X:3.2", "ans": "18.74"},
                    {"num": 6, "part": "B", "prompt": "Multiply 3.6 × 2.25 and check the whole-number ballpark.", "keys": "3.6 [ENTER] 2.25 [×]", "yx": "Y:3.6 | X:2.25", "ans": "8.1"},
                    {"num": 7, "part": "B", "prompt": "Multiply 0.15 × 0.4 and tap [FDISP] to see its simplified fraction.", "keys": "0.15 [ENTER] 0.4 [×] [FDISP]", "yx": "Y:0.15 | X:0.4", "ans": "0.06 (3/50)"},
                    {"num": 8, "part": "B", "prompt": "Find the area of a rectangular desk top measuring 1.8 m by 0.75 m.", "keys": "1.8 [ENTER] 0.75 [×]", "yx": "Y:1.8 | X:0.75", "ans": "1.35 m²"},
                    {"num": 9, "part": "C", "prompt": "You pay with a $20 bill for a $8.75 burger and $4.60 smoothie. How much change do you get?", "keys": "20 [ENTER] 8.75 [ENTER] 4.60 [+] [-]", "yx": "Y:20 | X:13.35", "ans": "$6.65 (Way 2: 20 - 8.75 - 4.60 = 6.65)"},
                    {"num": 10, "part": "C", "prompt": "Multiply 4.75 × 1.2 both as decimals AND as fractions (4 3/4 × 1 1/5) using [FDISP]!", "keys": "4.75 [ENTER] 1.2 [×]", "yx": "Y:4.75 | X:1.2", "ans": "5.7 or 5 7/10 (Way 2: 19/4 × 6/5 = 57/10)"}
                ]
            },
            {
                "day_num": 10,
                "sec_num": "2.5",
                "title": "Dividing Decimals & The 3-Way Fraction-Decimal-Remainder Translator",
                "big_ideas_ref": "Big Ideas Grade 6, Section 2.6 (Dividing Decimals)",
                "ccss": "CCSS.MATH.6.NS.B.3",
                "kit_id": "FRAC-01",
                "kit_name": "Fraction & Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "place_value",
                "diagram_data": {"num": "15 ÷ 4", "ip": "3 R 3", "fp": "3.75 = 3 3/4", "caption": "One division (15 ÷ 4), three outfits via [FDISP]: 3.75 (Decimal) <-> 3 3/4 (Mixed) <-> 15/4 <-> 3 R 3!"},
                "concept": "Why are 15 ÷ 4 = 3 R 3, 3 3/4, and 3.75 all the same answer? Because 3 leftover pieces divided by 4 is 3/4 = 0.75! On the SC-6, tapping [FDISP] after any division cycles through Decimal, Mixed Fraction, Improper Fraction, and Quotient+Remainder with one thumb!",
                "examples": [
                    {
                        "title": "Example 1: The 4-Outfit [FDISP] Translator (23 ÷ 4)",
                        "problem": "Write 23 ÷ 4 as a decimal, mixed number, improper fraction, and quotient with remainder.",
                        "block_step": "23 quarter-blocks make 5 whole stacks of 4 (20) plus 3 fourths (3/4 = 0.75).",
                        "keys": ["23", "ENTER", "4", "÷", "FDISP", "f", "d/c"],
                        "stack_y": "23 | 4",
                        "stack_x": "5.75 <-> 5 3/4",
                        "ans": "5.75 = 5 3/4 = 23/4 = 5 R 3",
                        "note": "Tap [FDISP] repeatedly to see every textbook format on Floor 1!"
                    },
                    {
                        "title": "Example 2: Dividing by a Decimal (6.75 ÷ 0.25)",
                        "problem": "Evaluate 6.75 ÷ 0.25 and explain why the answer is larger than 6.75.",
                        "block_step": "0.25 is 1 quarter (1/4). Asking '6.75 ÷ 0.25' asks 'How many quarters are in $6.75?' (4 per dollar -> 27 quarters!).",
                        "keys": ["6.75", "ENTER", "0.25", "÷", "f", "LASTX", "×"],
                        "stack_y": "6.75",
                        "stack_x": "0.25 -> 27",
                        "ans": "27 quarters",
                        "note": "[f] [LASTX] [×] proves 27 × 0.25 = 6.75!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Write 39 ÷ 8 as (a) Quotient + Remainder, (b) Decimal, and (c) Mixed Number.", "keys": "39 [ENTER] 8 [÷] [FDISP]", "yx": "Y:39 | X:8", "ans": "4 R 7, 4.875, 4 7/8"},
                    {"num": 2, "part": "A", "prompt": "Divide a decimal by a whole number: 18.4 ÷ 8.", "keys": "18.4 [ENTER] 8 [÷]", "yx": "Y:18.4 | X:8", "ans": "2.3"},
                    {"num": 3, "part": "A", "prompt": "How many quarters ($0.25) are in $11.25? Compute 11.25 ÷ 0.25.", "keys": "11.25 [ENTER] 0.25 [÷]", "yx": "Y:11.25 | X:0.25", "ans": "45"},
                    {"num": 4, "part": "A", "prompt": "Divide 7.2 ÷ 0.9 and check with [f] [LASTX] [×].", "keys": "7.2 [ENTER] 0.9 [÷]", "yx": "Y:7.2 | X:0.9", "ans": "8"},
                    {"num": 5, "part": "B", "prompt": "Divide 15.6 ÷ 0.12.", "keys": "15.6 [ENTER] 0.12 [÷]", "yx": "Y:15.6 | X:0.12", "ans": "130"},
                    {"num": 6, "part": "B", "prompt": "Divide 9.45 ÷ 1.5 and tap [FDISP] to write its mixed fraction form.", "keys": "9.45 [ENTER] 1.5 [÷] [FDISP]", "yx": "Y:9.45 | X:1.5", "ans": "6.3 (6 3/10)"},
                    {"num": 7, "part": "B", "prompt": "Divide 0.84 ÷ 0.07.", "keys": "0.84 [ENTER] 0.07 [÷]", "yx": "Y:0.84 | X:0.07", "ans": "12"},
                    {"num": 8, "part": "B", "prompt": "Spot the Glitch: Leo says 4.8 ÷ 0.2 = 0.24. Use [f] [LASTX] or estimation to fix it!", "keys": "4.8 [ENTER] 0.2 [÷]", "yx": "Y:4.8 | X:0.2", "ans": "24 (0.2 fits 5 times per 1)"},
                    {"num": 9, "part": "C", "prompt": "A runner completes a 4.5-mile race in 0.75-mile laps. How many laps is the race? Solve 2 ways!", "keys": "4.5 [ENTER] 0.75 [÷]", "yx": "Y:4.5 | X:0.75", "ans": "6 laps (Way 2: 4 1/2 ÷ 3/4 = 6)"},
                    {"num": 10, "part": "C", "prompt": "A 6-pack of sports drinks costs $7.50. What is the cost of 1 bottle, and how many bottles can $20 buy?", "keys": "7.50 [ENTER] 6 [÷] -> 1.25; 20 [ENTER] 1.25 [÷]", "yx": "Y:20 | X:1.25", "ans": "$1.25/bottle; 16 bottles"}
                ]
            }
        ]
    },

    # =========================================================================
    # CHAPTER 3: RATIOS, RATES & PERCENTS (Sections 3.1 - 3.5)
    # =========================================================================
    {
        "num": 3,
        "title": "Ratios, Rates & Percents",
        "big_ideas_book": "Big Ideas Math Grade 6 — Chapters 3, 4 & 5 (Ratios, Rates & Percents)",
        "subtitle": "Ratios & Tape Diagrams, Ratio Tables, Unit Rates, Percents, Discounts & Unit Conversions",
        "kit_summary": "Counting & Array Tiles (COUNT-01) + Fraction Studio (FRAC-01)",
        "hero_png": "counting_tiles_array_3x8.png",
        "coach_misconception": "Students confuse Part-to-Part (3:2) with Part-to-Whole (3/5), add instead of multiply in ratio tables, divide unit rates upside-down, and memorize 6 disconnected rules for moving decimal points in percents.",
        "coach_remediation": "Use Blue and Gold Counting Tiles as physical Tape Diagram boxes, step through ratio tables rhythmically with [g] [REP], use [x⇄y] when unit-rate division is entered upside-down, and use [f] [%] + [FDISP] to show Fraction/Decimal/Percent are three costumes of one number.",
        "sections": [
            {
                "day_num": 11,
                "sec_num": "3.1",
                "title": "Ratios & Tape Diagrams — Part-to-Part vs. Part-to-Whole",
                "big_ideas_ref": "Big Ideas Grade 6, Section 3.1 & 3.2 (Ratios and Tape Diagrams)",
                "ccss": "CCSS.MATH.6.RP.A.1",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Array Tiles",
                "asset_png": "counting_tiles_array_3x8.png",
                "diagram_type": "ratio_tape",
                "diagram_data": {"a": 3, "b": 2, "unit_val": 4, "label_a": "Blue (3×4=12)", "label_b": "Gold (2×4=8)", "caption": "3 Blue tiles : 2 Gold tiles (5 tiles total). If total = 20, each tile = 20 ÷ 5 = 4!"},
                "concept": "Instead of drawing uneven paper boxes for a Tape Diagram, snap Blue and Gold Counting Tiles onto your desk! Each tile is 1 equal unit box. For a 3:2 ratio, 3 Blue + 2 Gold = 5 total tiles (Part-to-Whole = 3/5). Use [g] [a:b] ([g][GCF]) to reduce any ratio to simplest form!",
                "examples": [
                    {
                        "title": "Example 1: Simplifying Ratios with [g] [a:b]",
                        "problem": "A gaming clan has 18 builders and 12 speedrunners. Simplify the Part-to-Part and Part-to-Whole ratios.",
                        "block_step": "Group 18 and 12 by their GCF (6): you get 3 builders for every 2 speedrunners (and 3 + 2 = 5 players per group).",
                        "keys": ["18", "ENTER", "12", "g", "a:b"],
                        "stack_y": "3 (Part 1)",
                        "stack_x": "2 (Part 2)",
                        "ans": "Part-to-Part = 3:2; Part-to-Whole = 3:5",
                        "note": "[g] [a:b] divides both Y and X by their GCF in 1 click!"
                    },
                    {
                        "title": "Example 2: Solving a Tape Diagram with Tiles",
                        "problem": "The ratio of wins to losses is 5:3. If a team played 32 games total, how many did they win?",
                        "block_step": "Lay 5 Blue tiles + 3 Gold tiles = 8 total tiles. Share 32 games across 8 tiles: 32 ÷ 8 = 4 games per tile. Wins = 5 × 4 = 20!",
                        "keys": ["32", "ENTER", "5", "ENTER", "3", "+", "÷", "5", "×"],
                        "stack_y": "4 (Per Tile)",
                        "stack_x": "5 -> 20",
                        "ans": "20 wins (and 12 losses)",
                        "note": "Check: 20 + 12 = 32 total games, and 20:12 reduces to 5:3!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Simplify the ratio 12 : 18 using [g] [a:b].", "keys": "12 [ENTER] 18 [g][a:b]", "yx": "Y:2 | X:3", "ans": "2 : 3"},
                    {"num": 2, "part": "A", "prompt": "Simplify the ratio 24 : 16 using [g] [a:b].", "keys": "24 [ENTER] 16 [g][a:b]", "yx": "Y:3 | X:2", "ans": "3 : 2"},
                    {"num": 3, "part": "A", "prompt": "A bag has 4 red marbles and 6 blue marbles. Find the simplified ratio of red to TOTAL marbles.", "keys": "4 [ENTER] 10 [g][a:b]", "yx": "Y:2 | X:5", "ans": "2 : 5"},
                    {"num": 4, "part": "A", "prompt": "In a 3:4 tape diagram, each tile is worth 6. Find the two parts and the total.", "keys": "3 [ENTER] 6 [×], 4 [ENTER] 6 [×]", "yx": "18 and 24", "ans": "18, 24 (Total = 42)"},
                    {"num": 5, "part": "B", "prompt": "Green paint mixes blue and yellow in a 2:3 ratio. If you use 25 cups total, how many cups of each?", "keys": "25 [ENTER] 5 [÷] -> 5/tile", "yx": "Y:5 | X:2,3", "ans": "10 blue, 15 yellow"},
                    {"num": 6, "part": "B", "prompt": "The ratio of cats to dogs at a shelter is 4:5. There are 36 animals total. How many are dogs?", "keys": "36 [ENTER] 9 [÷] 5 [×]", "yx": "Y:4 | X:5", "ans": "20 dogs"},
                    {"num": 7, "part": "B", "prompt": "The ratio of boys to girls in a club is 3:5. If there are 15 boys, how many girls are there?", "keys": "15 [ENTER] 3 [÷] 5 [×]", "yx": "Y:5 | X:5", "ans": "25 girls"},
                    {"num": 8, "part": "B", "prompt": "Difference Tape Model: The ratio of acoustic to electric guitars is 2:5. There are 18 MORE electric guitars. Find how many electric guitars!", "keys": "18 [ENTER] 3 [÷] 5 [×]", "yx": "Y:6 | X:5", "ans": "30 electric (12 acoustic)"},
                    {"num": 9, "part": "C", "prompt": "Two robot teams split 84 gears in a 4:3 ratio. How many gears does each team get? Solve 2 ways!", "keys": "84 [ENTER] 7 [÷] -> 12/tile", "yx": "Y:12 | X:4,3", "ans": "48 and 36 gears (Way 2: 4/7 of 84 = 48)"},
                    {"num": 10, "part": "C", "prompt": "Ratio of gold to silver coins is 7:4. There are 21 more gold coins than silver. How many coins in all?", "keys": "21 [ENTER] 3 [÷] 11 [×]", "yx": "Y:7 | X:11", "ans": "77 coins total (Way 2: 49 gold + 28 silver)"}
                ]
            },
            {
                "day_num": 12,
                "sec_num": "3.2",
                "title": "Ratio Tables & Double Number Lines via [g] [REP]",
                "big_ideas_ref": "Big Ideas Grade 6, Section 3.3 (Ratio Tables & Double Number Lines)",
                "ccss": "CCSS.MATH.6.RP.A.3a",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Array Tiles",
                "asset_png": "number_rack_subitizing.png",
                "diagram_type": "ratio_tape",
                "diagram_data": {"a": 3, "b": 7, "unit_val": 1, "label_a": "Top Row: 3 -> 6 -> 9 -> 12 -> 15", "label_b": "Bot Row: 7 -> 14 -> 21 -> 28 -> 35", "caption": "Dual Skip-Count Ladder via [g] [REP]: Top steps by +3 while Bottom steps by +7!"},
                "concept": "A Ratio Table and a Double Number Line are the exact same thing: two skip-counting ladders running side-by-side! Press 3 [g] [REP] and tap [+] to march across the top row (3, 6, 9, 12, 15), then 7 [g] [REP] and tap [+] to march across the bottom row (7, 14, 21, 28, 35)!",
                "examples": [
                    {
                        "title": "Example 1: Generating a Ratio Table with [g] [REP]",
                        "problem": "A drone flies 8 meters every 3 seconds. Build a 5-step table to find how far it flies in 15 seconds.",
                        "block_step": "Seconds ladder: 3 [g] [REP] [+] [+] [+] [+] -> 3, 6, 9, 12, 15 (5 jumps). Meters ladder: 8 [g] [REP] [+] [+] [+] [+] -> 8, 16, 24, 32, 40!",
                        "keys": ["8", "g", "REP", "+", "+", "+", "+"],
                        "stack_y": "8 (Step)",
                        "stack_x": "40 (5 jumps)",
                        "ans": "40 meters in 15 seconds",
                        "note": "[g] [REP] ([g][x⇄y]) locks the step size so each [+] adds another batch!"
                    },
                    {
                        "title": "Example 2: Scaling Down Then Up in a Ratio Table",
                        "problem": "6 skate park tickets cost $45. How much do 10 tickets cost?",
                        "block_step": "Divide both 6 and 45 by 3 to find 2 tickets = $15. Now multiply by 5 (since 2 × 5 = 10 tickets): 15 × 5 = $75!",
                        "keys": ["45", "ENTER", "3", "÷", "5", "×"],
                        "stack_y": "15 (2 tix)",
                        "stack_x": "5 -> 75",
                        "ans": "$75 for 10 tickets",
                        "note": "Or find 1 ticket ($45 ÷ 6 = $7.50) and multiply by 10 -> $75!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Use 4 [g] [REP] and 9 [g] [REP] to write the first 4 equivalent ratios of 4 : 9.", "keys": "4 [g][REP] [+], 9 [g][REP] [+]", "yx": "×1, ×2, ×3, ×4", "ans": "4:9, 8:18, 12:27, 16:36"},
                    {"num": 2, "part": "A", "prompt": "In a ratio table where A : B = 4 : 9, find B when A = 28.", "keys": "28 [ENTER] 4 [÷] 9 [×]", "yx": "Y:7 | X:9", "ans": "63"},
                    {"num": 3, "part": "A", "prompt": "In a ratio table where X : Y = 5 : 12, find X when Y = 60.", "keys": "60 [ENTER] 12 [÷] 5 [×]", "yx": "Y:5 | X:5", "ans": "25"},
                    {"num": 4, "part": "A", "prompt": "A printer prints 15 pages every 2 minutes. How many pages in 8 minutes?", "keys": "8 [ENTER] 2 [÷] 15 [×]", "yx": "Y:4 | X:15", "ans": "60 pages"},
                    {"num": 5, "part": "B", "prompt": "Hot cocoa uses 3 tbsp cocoa for every 8 oz milk. How much milk for 18 tbsp cocoa?", "keys": "18 [ENTER] 3 [÷] 8 [×]", "yx": "Y:6 | X:8", "ans": "48 oz milk"},
                    {"num": 6, "part": "B", "prompt": "8 markers cost $12. Scale down to 2 markers, then scale up to find the cost of 10 markers.", "keys": "12 [ENTER] 4 [÷] 5 [×]", "yx": "Y:3 | X:5", "ans": "$15"},
                    {"num": 7, "part": "B", "prompt": "A heart beats 21 times in 15 seconds. How many beats in 60 seconds (1 minute)?", "keys": "60 [ENTER] 15 [÷] 21 [×]", "yx": "Y:4 | X:21", "ans": "84 beats"},
                    {"num": 8, "part": "B", "prompt": "Spot the Glitch: For 3:5, Sam added 4 to both sides and wrote 7:9. Test with [g] [a:b]—are they equal?", "keys": "7 [ENTER] 9 [g][a:b]", "yx": "3:5 != 7:9", "ans": "No! Multiply by 3 -> 9:15"},
                    {"num": 9, "part": "C", "prompt": "9 smoothies take 12 cups of berries. How many cups of berries for 15 smoothies? Solve 2 ways!", "keys": "12 [ENTER] 3 [÷] 5 [×]", "yx": "Y:4 | X:5", "ans": "20 cups (Way 2: 12÷9 × 15 = 20)"},
                    {"num": 10, "part": "C", "prompt": "An e-bike travels 14 miles on 35% battery. How far can it travel on 100% battery?", "keys": "14 [ENTER] 7 [÷] 20 [×]", "yx": "Y:2 | X:20", "ans": "40 miles (Way 2: 2 mi per 5% × 20)"}
                ]
            },
            {
                "day_num": 13,
                "sec_num": "3.3",
                "title": "Unit Rates & Best-Buy Showdowns (Plus [x⇄y] Swap Rescue)",
                "big_ideas_ref": "Big Ideas Grade 6, Section 3.4 & 3.5 (Rates and Unit Rates)",
                "ccss": "CCSS.MATH.6.RP.A.2",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Array Tiles",
                "asset_png": "counting_tiles_box_3x1x13u.png",
                "diagram_type": "two_room",
                "diagram_data": {"room1": "Bag A: $4.20 ÷ 12 = $0.35/oz", "room2": "Bag B: $5.12 ÷ 16 = $0.32/oz", "op": "vs", "res": "Bag B Wins!", "caption": "Keep Bag A's unit price ($0.35) on Floor 2 (Y) while computing Bag B ($0.32) on Floor 1 (X)!"},
                "concept": "'Dollars PER Ounce' means Dollars ÷ Ounces (enter Dollars on Y, Ounces on X, press [÷]). What if you accidentally typed Ounces first and Dollars second? Don't clear! Just press [x⇄y] ([f][R↓]) to swap Floor 1 and Floor 2, then press [÷]!",
                "examples": [
                    {
                        "title": "Example 1: The [x⇄y] Upside-Down Rescue",
                        "problem": "Find the unit rate in words per minute for 315 words in 5 minutes (even if you typed 5 first!).",
                        "block_step": "If you typed 5 [ENTER] 315, tap [x⇄y] so Y=315 and X=5, then press [÷]!",
                        "keys": ["5", "ENTER", "315", "x⇄y", "÷"],
                        "stack_y": "315 (Words)",
                        "stack_x": "5 (Min) -> 63",
                        "ans": "63 words per minute",
                        "note": "[x⇄y] swaps Floor 1 (X) and Floor 2 (Y) instantly!"
                    },
                    {
                        "title": "Example 2: Side-by-Side Best-Buy Comparison on Y and X",
                        "problem": "Compare Pack A (8 batteries for $11.60) vs. Pack B (12 batteries for $16.80).",
                        "block_step": "Compute Pack A first (11.60 [ENTER] 8 [÷] -> $1.45). Now compute Pack B (16.80 [ENTER] 12 [÷] -> $1.40) while $1.45 sits right above it on Y!",
                        "keys": ["11.60", "ENTER", "8", "÷", "16.80", "ENTER", "12", "÷"],
                        "stack_y": "1.45 (Pack A)",
                        "stack_x": "1.40 (Pack B)",
                        "ans": "Pack B is better ($1.40 vs $1.45 per battery)",
                        "note": "Both unit prices sit on the screen at once for instant comparison!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the unit speed in miles per hour: 195 miles in 3 hours.", "keys": "195 [ENTER] 3 [÷]", "yx": "Y:195 | X:3", "ans": "65 mph"},
                    {"num": 2, "part": "A", "prompt": "You typed 4 [ENTER] 36 for $36 in 4 hours. Press [x⇄y] [÷] to find the hourly pay!", "keys": "4 [ENTER] 36 [x⇄y] [÷]", "yx": "Y:36 | X:4", "ans": "$9 / hour"},
                    {"num": 3, "part": "A", "prompt": "Find the unit price per pound: $7.80 for 6 pounds of apples.", "keys": "7.80 [ENTER] 6 [÷]", "yx": "Y:7.80 | X:6", "ans": "$1.30 / lb"},
                    {"num": 4, "part": "A", "prompt": "A 3D printer uses 90 grams of filament in 6 hours. How many grams per hour?", "keys": "90 [ENTER] 6 [÷]", "yx": "Y:90 | X:6", "ans": "15 g / hr"},
                    {"num": 5, "part": "B", "prompt": "Best Buy: Cereal A is $4.50 for 15 oz. Cereal B is $5.04 for 18 oz. Find both unit prices!", "keys": "4.50 [ENTER] 15 [÷]; 5.04 [ENTER] 18 [÷]", "yx": "Y:0.30 | X:0.28", "ans": "Cereal B ($0.28/oz vs $0.30/oz)"},
                    {"num": 6, "part": "B", "prompt": "Best Buy: 6-pack of pens for $5.10 vs. 10-pack of pens for $8.20.", "keys": "5.10 [ENTER] 6 [÷]; 8.20 [ENTER] 10 [÷]", "yx": "Y:0.85 | X:0.82", "ans": "10-pack ($0.82 vs $0.85)"},
                    {"num": 7, "part": "B", "prompt": "A train travels 210 miles in 3.5 hours. At this rate, how far does it travel in 5 hours?", "keys": "210 [ENTER] 3.5 [÷] 5 [×]", "yx": "Y:60 | X:5", "ans": "300 miles"},
                    {"num": 8, "part": "B", "prompt": "Pump A fills 45 gallons in 5 min. Pump B fills 64 gallons in 8 min. Which pump is faster?", "keys": "45 [ENTER] 5 [÷]; 64 [ENTER] 8 [÷]", "yx": "Y:9 | X:8", "ans": "Pump A (9 gal/min vs 8 gal/min)"},
                    {"num": 9, "part": "C", "prompt": "An extruder pushes 45 mm of filament in 15 seconds. How much in 60 seconds (1 min)? Solve 2 ways!", "keys": "45 [ENTER] 15 [÷] 60 [×]", "yx": "Y:3 | X:60", "ans": "180 mm (Way 2: 60s is 4×15s -> 4×45=180)"},
                    {"num": 10, "part": "C", "prompt": "Car A drives 168 miles on 6 gallons. Car B drives 232 miles on 8 gallons. Which car gets more mpg?", "keys": "168 [ENTER] 6 [÷]; 232 [ENTER] 8 [÷]", "yx": "Y:28 | X:29", "ans": "Car B (29 mpg vs 28 mpg)"}
                ]
            },
            {
                "day_num": 14,
                "sec_num": "3.4",
                "title": "Percents, Fractions & Decimals — The 3-Costume Switcher",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 4.1–4.3 / 5.5 (Percents, Fractions, and Decimals)",
                "ccss": "CCSS.MATH.6.RP.A.3c",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_twin_comparator.png",
                "diagram_type": "percent_bar",
                "diagram_data": {"pct": 75, "frac": "3/4", "dec": "0.75", "caption": "75% Battery = 0.75 Decimal = three 1/4 Fraction Blocks (63mm / 84mm). One amount, three costumes!"},
                "concept": "'Per-cent' literally means 'out of 100' (like 100 cents in $1.00). Instead of memorizing rules for moving decimal points left or right, enter any fraction or decimal on the SC-6 and press [f] [%] ([f][÷]) to see its percent, or [FDISP] to switch between fraction and decimal!",
                "examples": [
                    {
                        "title": "Example 1: Fraction <-> Decimal <-> Percent in 1 Click",
                        "problem": "Convert 7/20 into a decimal and a percent using [FDISP] and [f] [%].",
                        "block_step": "Since 20 × 5 = 100, 7/20 is 35/100 = 0.35 = 35%. Verify with [FDISP] and [f] [%].",
                        "keys": [".", "7", ".", "20", "ENTER", "FDISP", "100", "×"],
                        "stack_y": "7/20",
                        "stack_x": "0.35 -> 35%",
                        "ans": "0.35 and 35%",
                        "note": "To turn any percent p% into a fraction: key p [ENTER] 100 [÷] [FDISP]!"
                    },
                    {
                        "title": "Example 2: Finding Shooting Percentage (18 out of 24)",
                        "problem": "You make 18 out of 24 free throws. Find your simplified fraction, decimal, and shooting percentage.",
                        "block_step": "18/24 reduces to three 1/4 blocks (3/4 = 0.75 = 75%).",
                        "keys": ["18", "ENTER", "24", "÷", "FDISP"],
                        "stack_y": "18 | 24",
                        "stack_x": "0.75 (3/4 = 75%)",
                        "ans": "3/4 = 0.75 = 75%",
                        "note": "Three quarters of a dollar is 75 cents -> 75%!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Write 3/5 as a decimal and as a percent.", "keys": "[.] 3 [.] 5 [ENTER] [FDISP]", "yx": "Y:3/5 | X:0.6", "ans": "0.6 and 60%"},
                    {"num": 2, "part": "A", "prompt": "Write 9/25 as a decimal and as a percent.", "keys": "[.] 9 [.] 25 [ENTER] [FDISP]", "yx": "Y:9/25 | X:0.36", "ans": "0.36 and 36%"},
                    {"num": 3, "part": "A", "prompt": "Write 45% as a decimal and as a simplified fraction ([FDISP]).", "keys": "45 [ENTER] 100 [÷] [FDISP]", "yx": "0.45 -> 9/20", "ans": "0.45 and 9/20"},
                    {"num": 4, "part": "A", "prompt": "Write 0.125 as a percent and as a simplified fraction ([FDISP]).", "keys": "0.125 [ENTER] [FDISP]", "yx": "12.5% | 1/8", "ans": "12.5% and 1/8"},
                    {"num": 5, "part": "B", "prompt": "Find 30% of 80 using the [f] [%] key: 80 [ENTER] 30 [f] [%].", "keys": "80 [ENTER] 30 [f][%]", "yx": "Y:80 | X:24", "ans": "24"},
                    {"num": 6, "part": "B", "prompt": "Find 15% of 60.", "keys": "60 [ENTER] 15 [f][%]", "yx": "Y:60 | X:9", "ans": "9"},
                    {"num": 7, "part": "B", "prompt": "You answered 21 out of 25 questions right. What is your score as a percent?", "keys": "21 [ENTER] 25 [÷]", "yx": "0.84 -> 84%", "ans": "84%"},
                    {"num": 8, "part": "B", "prompt": "Convert 150% into a decimal and a mixed fraction.", "keys": "150 [ENTER] 100 [÷] [FDISP]", "yx": "1.5 -> 1 1/2", "ans": "1.5 and 1 1/2"},
                    {"num": 9, "part": "C", "prompt": "Order 5/8, 60%, and 0.61 from least to greatest by converting all 3 to decimals (and percents!).", "keys": "[.] 5 [.] 8 [FDISP] -> 0.625", "yx": "0.60, 0.61, 0.625", "ans": "60%, 0.61, 5/8 (Way 2: 60% < 61% < 62.5%)"},
                    {"num": 10, "part": "C", "prompt": "A phone battery is at 35% of its 4,000 mAh capacity. How many mAh remain? Solve 2 ways!", "keys": "4000 [ENTER] 35 [f][%]", "yx": "Y:4000 | X:1400", "ans": "1,400 mAh (Way 2: 7/20 × 4000 = 1400)"}
                ]
            },
            {
                "day_num": 15,
                "sec_num": "3.5",
                "title": "Discounts, Percent Change ([g] [%CHG]) & Unit Conversions",
                "big_ideas_ref": "Big Ideas Grade 6, Section 5.6 & 5.7 (Percent Problems & Converting Measures)",
                "ccss": "CCSS.MATH.6.RP.A.3d",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value & Fraction Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "percent_bar",
                "diagram_data": {"pct": 75, "frac": "Pay 75% ($45)", "dec": "Save 25% ($15)", "caption": "$60 Game at 25% Off: 60 [ENTER] 25 [f][%] puts $15 discount on X while $60 stays on Y. Press [-] -> $45!"},
                "concept": "On a normal calculator, finding a sale price takes two separate calculations because computing the discount erases the original price! On the SC-6, typing 60 [ENTER] 25 [f] [%] puts the $15 discount on Floor 1 (X) while keeping $60 on Floor 2 (Y)—so pressing [-] gives the $45 sale price in 1 click!",
                "examples": [
                    {
                        "title": "Example 1: 2-Key Sale Price ([f] [%] then [-])",
                        "problem": "A $60 video game is 25% off. Find the discount and the sale price.",
                        "block_step": "25% is 1/4 of $60 = $15 off. The remaining 75% (3/4) is $45!",
                        "keys": ["60", "ENTER", "25", "f", "%", "-"],
                        "stack_y": "60 (Orig)",
                        "stack_x": "15 (Disc) -> 45",
                        "ans": "Discount = $15; Sale Price = $45",
                        "note": "For tax or tip, press [+] instead of [-] at the end!"
                    },
                    {
                        "title": "Example 2: Percent Change ([g] [%CHG]) & Unit Conversions ([f] [▸cm])",
                        "problem": "Find the percent increase from 250 to 325 subscribers, and convert 32 inches to cm.",
                        "block_step": "Enter Old (250) on Y, New (325) on X, and press [g] [%CHG]. For 32 inches, press 32 [f] [▸cm] ([f][1])!",
                        "keys": ["250", "ENTER", "325", "g", "%CHG", "32", "f", "▸cm"],
                        "stack_y": "+30%",
                        "stack_x": "81.28 cm",
                        "ans": "+30% increase; 32 in = 81.28 cm",
                        "note": "[f] [▸cm] ([f][1]) and [f] [▸kg] ([f][3]) convert units in 1 click!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "An $80 pair of shoes is 30% off. Find the discount (X) and sale price ([-]).", "keys": "80 [ENTER] 30 [f][%] [-]", "yx": "Y:80 | X:24", "ans": "Discount $24; Sale $56"},
                    {"num": 2, "part": "A", "prompt": "A $40 restaurant meal has a 15% tip. Find the tip and total bill ([+]).", "keys": "40 [ENTER] 15 [f][%] [+]", "yx": "Y:40 | X:6", "ans": "Tip $6; Total $46"},
                    {"num": 3, "part": "A", "prompt": "Find the percent change from 50 to 65 using [g] [%CHG].", "keys": "50 [ENTER] 65 [g][%CHG]", "yx": "Y:50 | X:65", "ans": "+30%"},
                    {"num": 4, "part": "A", "prompt": "Find the percent change from 80 down to 60 using [g] [%CHG].", "keys": "80 [ENTER] 60 [g][%CHG]", "yx": "Y:80 | X:60", "ans": "-25%"},
                    {"num": 5, "part": "B", "prompt": "Convert 10 inches to centimeters using [f] [▸cm] (2.54 cm = 1 in).", "keys": "10 [f][▸cm]", "yx": "10 in -> cm", "ans": "25.4 cm"},
                    {"num": 6, "part": "B", "prompt": "Convert 50.8 centimeters back to inches using [g] [▸in] ([g][1]).", "keys": "50.8 [g][▸in]", "yx": "50.8 cm -> in", "ans": "20 in"},
                    {"num": 7, "part": "B", "prompt": "Convert 11 pounds to kilograms using [f] [▸kg] ([f][3]).", "keys": "11 [f][▸kg]", "yx": "11 lb -> kg", "ans": "4.99 kg"},
                    {"num": 8, "part": "B", "prompt": "Reverse Percent: 18 is 25% of what number? (Divide 18 by 0.25!)", "keys": "18 [ENTER] 0.25 [÷]", "yx": "Y:18 | X:0.25", "ans": "72"},
                    {"num": 9, "part": "C", "prompt": "A $120 skateboard is 20% off. Find the sale price both by subtracting [f][%] AND by multiplying by 80%!", "keys": "120 [ENTER] 20 [f][%] [-]", "yx": "Y:120 | X:24", "ans": "$96 (Way 2: 120 × 0.80 = 96)"},
                    {"num": 10, "part": "C", "prompt": "A 32-inch deck weighs 5 lbs. Convert length to cm ([f][▸cm]) and weight to kg ([f][▸kg]). Verify with ×2.54!", "keys": "32 [f][▸cm]; 5 [f][▸kg]", "yx": "81.28cm | 2.27kg", "ans": "81.28 cm, 2.27 kg (Way 2: 32×2.54=81.28)"}
                ]
            }
        ]
    },

    # =========================================================================
    # CHAPTER 4: ALGEBRAIC EXPRESSIONS & PROPERTIES (Sections 4.1 - 4.4)
    # =========================================================================
    {
        "num": 4,
        "title": "Algebraic Expressions & Properties",
        "big_ideas_book": "Big Ideas Math Grade 6 — Chapter 3 / Chapter 5 (Algebraic Expressions)",
        "subtitle": "Evaluating Algebraic Expressions, Combining Like Terms, Distributive Property & Factoring with GCF",
        "kit_summary": "Algebra Boxes & Factoring Stage (ALGB-01) + Counting Tiles (COUNT-01)",
        "hero_png": "algebra_factoring_area.png",
        "coach_misconception": "Students panic when letters appear, erroneously combine 3x + 2 into 5x or x² + x into x³, and don't see why 3(x + 4) = 3x + 12.",
        "coach_remediation": "Show that a variable x is literally a physical green x-rod (42×14mm) whereas 1 is a small yellow unit cube (14×14mm) and x² is a large blue flat (42×42mm)—different physical shapes cannot be counted as one pile! Build rectangles on the L-frame stage for the Distributive Property.",
        "sections": [
            {
                "day_num": 16,
                "sec_num": "4.1",
                "title": "Evaluating Algebraic Expressions — Variable Boxes on the Stack",
                "big_ideas_ref": "Big Ideas Grade 6, Section 3.1 / 5.1 (Algebraic Expressions)",
                "ccss": "CCSS.MATH.6.EE.A.2",
                "kit_id": "ALGB-01",
                "kit_name": "Algebra Boxes & Tiles",
                "asset_png": "algebra_factoring_area.png",
                "diagram_type": "algebra_tiles",
                "diagram_data": {"mode": "eval", "x_rods": 4, "units": 7, "x_val": 5, "caption": "4x + 7 with x = 5: Four x-rods (each worth 5 units = 20) + 7 unit cubes = 27!"},
                "concept": "A letter like x is not scary—it is just an empty green box (ALGB-01) waiting for you to drop a number inside! When you see 4x + 7 and x = 5, replace each x-rod with 5 units (4 × 5 = 20) and add 7 -> 27. On the SC-6, evaluating an expression is just Section 1.3's elevator math!",
                "examples": [
                    {
                        "title": "Example 1: Single-Variable Plug-In (4x + 7 when x = 5)",
                        "problem": "Evaluate 4x + 7 when x = 5 using Algebra Tiles and the SC-6.",
                        "block_step": "Lay out 4 green x-rods and 7 unit cubes. Replace each x-rod with 5 units (4 × 5 = 20), then add 7 units -> 27!",
                        "keys": ["4", "ENTER", "5", "×", "7", "+"],
                        "stack_y": "20 (4x)",
                        "stack_x": "7 -> 27",
                        "ans": "27",
                        "note": "Write Snapshot Y: 20 | X: 7 before pressing [+]!"
                    },
                    {
                        "title": "Example 2: Exponents & Two Variables (3a² + 4b for a=5, b=6)",
                        "problem": "Evaluate 3a² + 4b when a = 5 and b = 6.",
                        "block_step": "In 3a², square a FIRST (5² = 25), then multiply by 3 (= 75). Leave 75 on Floor 2 (Y) while computing 4 × 6 = 24 on Floor 1 (X)!",
                        "keys": ["5", "x²", "3", "×", "4", "ENTER", "6", "×", "+"],
                        "stack_y": "75 (3a²)",
                        "stack_x": "24 (4b) -> 99",
                        "ans": "99",
                        "note": "Floor 2 holds 75 while Floor 1 computes 24, then [+] gives 99!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Evaluate 6x - 9 when x = 7.", "keys": "6 [ENTER] 7 [×] 9 [-]", "yx": "Y:42 | X:9", "ans": "33"},
                    {"num": 2, "part": "A", "prompt": "Evaluate 5n + 14 when n = 8.", "keys": "5 [ENTER] 8 [×] 14 [+]", "yx": "Y:40 | X:14", "ans": "54"},
                    {"num": 3, "part": "A", "prompt": "Evaluate 40 - 3m when m = 9. (Park 40 on Y first!)", "keys": "40 [ENTER] 3 [ENTER] 9 [×] [-]", "yx": "Y:40 | X:27", "ans": "13"},
                    {"num": 4, "part": "A", "prompt": "Evaluate x² + 11 when x = 6.", "keys": "6 [x²] 11 [+]", "yx": "Y:36 | X:11", "ans": "47"},
                    {"num": 5, "part": "B", "prompt": "Evaluate 2y² - 5 when y = 4. (Square 4 before multiplying by 2!)", "keys": "4 [x²] 2 [×] 5 [-]", "yx": "Y:32 | X:5", "ans": "27"},
                    {"num": 6, "part": "B", "prompt": "Evaluate 7a + 3b when a = 4 and b = 9.", "keys": "7 [ENTER] 4 [×] 3 [ENTER] 9 [×] [+]", "yx": "Y:28 | X:27", "ans": "55"},
                    {"num": 7, "part": "B", "prompt": "Evaluate (x + y) ÷ 4 when x = 19 and y = 13.", "keys": "19 [ENTER] 13 [+] 4 [÷]", "yx": "Y:32 | X:4", "ans": "8"},
                    {"num": 8, "part": "B", "prompt": "Evaluate 5k - 2.4 when k = 3.5.", "keys": "5 [ENTER] 3.5 [×] 2.4 [-]", "yx": "Y:17.5 | X:2.4", "ans": "15.1"},
                    {"num": 9, "part": "C", "prompt": "Skate park rental costs $8 flat plus $4.50 per hour (8 + 4.50h). Find the cost for 4 hours 2 ways!", "keys": "4.50 [ENTER] 4 [×] 8 [+]", "yx": "Y:18 | X:8", "ans": "$26 (Way 2: 8+4.5+4.5+4.5+4.5 = 26)"},
                    {"num": 10, "part": "C", "prompt": "Surface area of a cube is 6s². Find the surface area when edge s = 5 cm.", "keys": "5 [x²] 6 [×]", "yx": "Y:25 | X:6", "ans": "150 cm² (Way 2: 6 faces × 25 cm² = 150)"}
                ]
            },
            {
                "day_num": 17,
                "sec_num": "4.2",
                "title": "Combining Like Terms — Why x² Flats, x Rods & 1 Cubes Never Mix",
                "big_ideas_ref": "Big Ideas Grade 6, Section 3.2 & 3.3 / 5.2 (Simplifying Algebraic Expressions)",
                "ccss": "CCSS.MATH.6.EE.A.3",
                "kit_id": "ALGB-01",
                "kit_name": "Algebra Boxes & Tiles",
                "asset_png": "algebra_factoring_area.png",
                "diagram_type": "algebra_tiles",
                "diagram_data": {"mode": "like_terms", "x2_flats": 2, "x_rods": 5, "units": 4, "caption": "3 different physical shapes: Blue x²-Flats (42×42), Green x-Rods (42×14), Yellow 1-Cubes (14×14). Sort by shape!"},
                "concept": "Why can't you add 3x + 2 and write 5x? Hold a green x-rod (42 mm long) next to a small yellow 1-cube (14 mm)—they are completely different shapes! 'Combining Like Terms' simply means sorting your tiles into separate piles by shape (x²-flats, x-rods, and 1-cubes) and counting each pile!",
                "examples": [
                    {
                        "title": "Example 1: Sorting x-Rods and Unit Cubes (4x + 5 + 2x + 3)",
                        "problem": "Simplify 4x + 5 + 2x + 3 and prove it by testing x = 10 on your SC-6.",
                        "block_step": "Slide the x-rods together (4x + 2x = 6x) and slide the unit cubes together (5 + 3 = 8) -> 6x + 8.",
                        "keys": ["4", "ENTER", "2", "+", "5", "ENTER", "3", "+"],
                        "stack_y": "6 (x-rods)",
                        "stack_x": "8 (units)",
                        "ans": "6x + 8",
                        "note": "Test x=10: Original 4(10)+5+2(10)+3 = 68; Simplified 6(10)+8 = 68!"
                    },
                    {
                        "title": "Example 2: Three Tile Shapes (3x² + 5x + 2x² - x + 6)",
                        "problem": "Simplify 3x² + 5x + 2x² - x + 6.",
                        "block_step": "Sort into 3 piles: x²-flats (3 + 2 = 5x²), x-rods (5 - 1 = 4x), and unit cubes (6).",
                        "keys": ["3", "ENTER", "2", "+", "5", "ENTER", "1", "-"],
                        "stack_y": "5 (x²-flats)",
                        "stack_x": "4 (x-rods)",
                        "ans": "5x² + 4x + 6",
                        "note": "Remember: a single 'x' with no number in front is 1x!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Sort and simplify: 7x + 4 + 2x + 9.", "keys": "7 [ENTER] 2 [+]; 4 [ENTER] 9 [+]", "yx": "Y:9 (x) | X:13 (1)", "ans": "9x + 13"},
                    {"num": 2, "part": "A", "prompt": "Simplify: 8x + 11 - 3x - 4.", "keys": "8 [ENTER] 3 [-]; 11 [ENTER] 4 [-]", "yx": "Y:5 (x) | X:7 (1)", "ans": "5x + 7"},
                    {"num": 3, "part": "A", "prompt": "Simplify: 9y - y + 6. (Remember: -y means -1y!)", "keys": "9 [ENTER] 1 [-]", "yx": "Y:8 (y) | X:6 (1)", "ans": "8y + 6"},
                    {"num": 4, "part": "A", "prompt": "Simplify: 12a + 5 - 4a + 8.", "keys": "12 [ENTER] 4 [-]; 5 [ENTER] 8 [+]", "yx": "Y:8 (a) | X:13 (1)", "ans": "8a + 13"},
                    {"num": 5, "part": "B", "prompt": "Sort all 3 tile shapes: 4x² + 3x + 2x² + 5x + 7.", "keys": "4+2=6; 3+5=8", "yx": "6(x²) | 8(x) | 7", "ans": "6x² + 8x + 7"},
                    {"num": 6, "part": "B", "prompt": "Simplify: 6n² + 9n - 2n² - 4n + 10.", "keys": "6-2=4; 9-4=5", "yx": "4(n²) | 5(n) | 10", "ans": "4n² + 5n + 10"},
                    {"num": 7, "part": "B", "prompt": "Simplify with decimals: 3.5x + 4.2 + 1.8x - 1.5.", "keys": "3.5 [ENTER] 1.8 [+]; 4.2 [ENTER] 1.5 [-]", "yx": "Y:5.3 | X:2.7", "ans": "5.3x + 2.7"},
                    {"num": 8, "part": "B", "prompt": "Spot the Glitch: Leo simplified 5x + 3 to 8x. Test x = 10 on your SC-6 to prove 5x + 3 != 8x!", "keys": "5(10)+3=53 vs 8(10)=80", "yx": "Y:53 | X:80", "ans": "53 != 80; 5x + 3 is already simplified!"},
                    {"num": 9, "part": "C", "prompt": "A rectangle has two sides of (2x + 3) and two sides of (x + 5). Write its simplified perimeter & test x=10!", "keys": "2+2+1+1=6x; 3+3+5+5=16", "yx": "Y:6 (x) | X:16", "ans": "6x + 16 (At x=10: both give 76!)"},
                    {"num": 10, "part": "C", "prompt": "A triangle has sides (3x + 2), (2x + 7), and (4x - 1). Write the simplified perimeter & test x=5!", "keys": "3+2+4=9x; 2+7-1=8", "yx": "Y:9 (x) | X:8", "ans": "9x + 8 (At x=5: 17+17+19 = 53)"}
                ]
            },
            {
                "day_num": 18,
                "sec_num": "4.3",
                "title": "The Distributive Property — One Split Rectangle, Two Ways",
                "big_ideas_ref": "Big Ideas Grade 6, Section 3.4 / 5.3 (The Distributive Property)",
                "ccss": "CCSS.MATH.6.EE.A.3",
                "kit_id": "ALGB-01",
                "kit_name": "Algebra Boxes & Tiles",
                "asset_png": "counting_tiles_distributive_4color.png",
                "diagram_type": "algebra_tiles",
                "diagram_data": {"mode": "distrib", "rows": 3, "x_per_row": 1, "u_per_row": 4, "caption": "3 rows of (x + 4) on the L-frame stage = 3 green x-rods (3x) + 12 yellow cubes (+12)!"},
                "concept": "Why does 3(x + 4) = 3x + 12? Build 3 identical rows of (1 green x-rod + 4 yellow cubes) on the Algebra Stage. Count by rows: 3(x + 4). Count by shape columns: 3 x-rods + 12 cubes = 3x + 12! Same tiles on your desk, two ways to name the area!",
                "examples": [
                    {
                        "title": "Example 1: Numerical Split Rectangle 6(10 + 4)",
                        "problem": "Compute 6 × (10 + 4) both ways on your SC-6 to see why distribution works.",
                        "block_step": "Way A (Add inside first): 6 × 14 = 84. Way B (Split into 2 rooms): 6×10 (60) + 6×4 (24) = 84!",
                        "keys": ["6", "ENTER", "10", "×", "6", "ENTER", "4", "×", "+"],
                        "stack_y": "60 (6×10)",
                        "stack_x": "24 (6×4) -> 84",
                        "ans": "84 (Matches 6 × 14 = 84)",
                        "note": "Floor 2 holds Room 1 (60) while Floor 1 holds Room 2 (24)!"
                    },
                    {
                        "title": "Example 2: Distributing & Combining 5(2x + 3) + 4x",
                        "problem": "Simplify 5(2x + 3) + 4x and verify by testing x = 2 on the SC-6.",
                        "block_step": "5 rows of (2x + 3) gives 10x + 15. Adding 4 more x-rods gives 14x + 15!",
                        "keys": ["5", "ENTER", "2", "×", "4", "+", "5", "ENTER", "3", "×"],
                        "stack_y": "14 (x-rods)",
                        "stack_x": "15 (units)",
                        "ans": "14x + 15",
                        "note": "Test x=2: 5(2(2)+3) + 4(2) = 35 + 8 = 43; and 14(2) + 15 = 43!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Compute 7 × (20 + 3) both ways on your SC-6. Write the two partial products.", "keys": "7 [ENTER] 20 [×] 7 [ENTER] 3 [×] [+]", "yx": "Y:140 | X:21", "ans": "140 + 21 = 161"},
                    {"num": 2, "part": "A", "prompt": "Build 4 rows of (x + 5) and write the distributed expression for 4(x + 5).", "keys": "4 [ENTER] 5 [×]", "yx": "4(x) | 20(1)", "ans": "4x + 20"},
                    {"num": 3, "part": "A", "prompt": "Use the Distributive Property to expand 6(3x + 4).", "keys": "6×3=18; 6×4=24", "yx": "Y:18 | X:24", "ans": "18x + 24"},
                    {"num": 4, "part": "A", "prompt": "Expand 8(2y - 5). Watch the subtraction sign!", "keys": "8×2=16; 8×5=40", "yx": "Y:16 | X:-40", "ans": "16y - 40"},
                    {"num": 5, "part": "B", "prompt": "Mental Math Split: Compute 9 × 43 by splitting 43 into (40 + 3).", "keys": "9 [ENTER] 40 [×] 9 [ENTER] 3 [×] [+]", "yx": "Y:360 | X:27", "ans": "387"},
                    {"num": 6, "part": "B", "prompt": "Distribute and combine like terms: 3(4x + 2) + 5x.", "keys": "3×4+5=17; 3×2=6", "yx": "Y:17 | X:6", "ans": "17x + 6"},
                    {"num": 7, "part": "B", "prompt": "Distribute and combine: 4(3n + 5) - 7.", "keys": "4×3=12; 20-7=13", "yx": "Y:12 | X:13", "ans": "12n + 13"},
                    {"num": 8, "part": "B", "prompt": "Spot the Glitch: Mia wrote 5(x + 6) = 5x + 6. What did she forget to multiply by 5?", "keys": "5 [ENTER] 6 [×]", "yx": "5 × 6 = 30", "ans": "5x + 30 (Must multiply 6 by 5 too!)"},
                    {"num": 9, "part": "C", "prompt": "Simplify 5(2x + 3) + 4x AND prove your answer matches the original when x = 2!", "keys": "5×2+4=14; 5×3=15", "yx": "Y:14 | X:15", "ans": "14x + 15 (At x=2: both equal 43!)"},
                    {"num": 10, "part": "C", "prompt": "6 friends each buy a burger ($x) and $3.50 fries: 6(x + 3.50). Expand it and evaluate for x = $6.50!", "keys": "6 [ENTER] 3.50 [×] -> 6x+21", "yx": "Y:39 | X:21", "ans": "6x + 21; $60 total"}
                ]
            },
            {
                "day_num": 19,
                "sec_num": "4.4",
                "title": "Factoring Expressions with GCF — Reverse the Rectangle",
                "big_ideas_ref": "Big Ideas Grade 6, Section 3.4 Ext / 5.4 (Factoring Expressions)",
                "ccss": "CCSS.MATH.6.EE.A.3",
                "kit_id": "ALGB-01",
                "kit_name": "Algebra & Prime Studio",
                "asset_png": "algebra_factoring_area.png",
                "diagram_type": "algebra_tiles",
                "diagram_data": {"mode": "distrib", "rows": 6, "x_per_row": 3, "u_per_row": 4, "caption": "Factoring 18x + 24: GCF(18, 24) = 6 equal rows! Each row holds (3x + 4) -> 6(3x + 4)!"},
                "concept": "'Factoring' sounds hard, but it is just running Section 4.3's Distributive Property in reverse using Section 1.5's [GCF] key! To factor 18x + 24, press 18 [ENTER] 24 [GCF] -> 6 (that's the number of equal rows!). Divide 18x and 24 by 6 to get 6(3x + 4)!",
                "examples": [
                    {
                        "title": "Example 1: Factoring Numbers & Algebra with [GCF]",
                        "problem": "Factor 18x + 24 completely using the [GCF] key.",
                        "block_step": "Find the largest number of equal rows: 18 [ENTER] 24 [GCF] -> 6 rows! Each of the 6 rows has 18÷6 = 3 x-rods and 24÷6 = 4 cubes.",
                        "keys": ["18", "ENTER", "24", "GCF"],
                        "stack_y": "18 | 24",
                        "stack_x": "6 (GCF rows)",
                        "ans": "6(3x + 4)",
                        "note": "Check by distributing back: 6 × 3x = 18x and 6 × 4 = 24!"
                    },
                    {
                        "title": "Example 2: Factoring Subtraction Expressions (45x - 30)",
                        "problem": "Factor 45x - 30 completely using [GCF].",
                        "block_step": "Press 45 [ENTER] 30 [GCF] -> 15. Pull 15 outside the parentheses: 45÷15 = 3x and 30÷15 = 2.",
                        "keys": ["45", "ENTER", "30", "GCF", "45", "x⇄y", "÷"],
                        "stack_y": "15 (GCF)",
                        "stack_x": "3 (45÷15)",
                        "ans": "15(3x - 2)",
                        "note": "Check: 15 × 3x - 15 × 2 = 45x - 30!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Factor 12 + 20 into the form a(b + c) using [GCF].", "keys": "12 [ENTER] 20 [GCF] -> 4", "yx": "GCF = 4", "ans": "4(3 + 5)"},
                    {"num": 2, "part": "A", "prompt": "Factor 8x + 12 using [GCF].", "keys": "8 [ENTER] 12 [GCF] -> 4", "yx": "GCF = 4", "ans": "4(2x + 3)"},
                    {"num": 3, "part": "A", "prompt": "Factor 15y - 25 using [GCF].", "keys": "15 [ENTER] 25 [GCF] -> 5", "yx": "GCF = 5", "ans": "5(3y - 5)"},
                    {"num": 4, "part": "A", "prompt": "Factor 24x + 36 completely using [GCF].", "keys": "24 [ENTER] 36 [GCF] -> 12", "yx": "GCF = 12", "ans": "12(2x + 3)"},
                    {"num": 5, "part": "B", "prompt": "Factor 32n - 48 completely using [GCF].", "keys": "32 [ENTER] 48 [GCF] -> 16", "yx": "GCF = 16", "ans": "16(2n - 3)"},
                    {"num": 6, "part": "B", "prompt": "Factor 42a + 14 completely. (Careful: what is 14 ÷ 14?)", "keys": "42 [ENTER] 14 [GCF] -> 14", "yx": "GCF = 14", "ans": "14(3a + 1)"},
                    {"num": 7, "part": "B", "prompt": "Factor 36m - 60 completely using [GCF].", "keys": "36 [ENTER] 60 [GCF] -> 12", "yx": "GCF = 12", "ans": "12(3m - 5)"},
                    {"num": 8, "part": "B", "prompt": "Spot the Glitch: Sam factored 24x + 36 as 6(4x + 6). Why isn't it factored completely?", "keys": "4 [ENTER] 6 [GCF] -> 2 left!", "yx": "GCF(24,36)=12", "ans": "12(2x + 3) (4 and 6 still share factor 2)"},
                    {"num": 9, "part": "C", "prompt": "A rectangular banner has area (28x + 42) sq in and height 14 in. Factor with [GCF] to find its width!", "keys": "28 [ENTER] 42 [GCF] -> 14", "yx": "GCF = 14", "ans": "Width = 2x + 3 (Way 2: 14(2x+3)=28x+42)"},
                    {"num": 10, "part": "C", "prompt": "A square garden has perimeter (36x + 48) ft. Factor out 4 to find the length of 1 side!", "keys": "36 [ENTER] 4 [÷]; 48 [ENTER] 4 [÷]", "yx": "Y:9 | X:12", "ans": "Side = 9x + 12 (4(9x + 12))"}
                ]
            }
        ]
    },

    # =========================================================================
    # CHAPTER 5: AREAS OF POLYGONS & ELAPSED TIME (Sections 5.1 - 5.4)
    # =========================================================================
    {
        "num": 5,
        "title": "Areas of Polygons & Elapsed Time",
        "big_ideas_book": "Big Ideas Math Grade 6 — Chapter 4 (Areas of Polygons)",
        "subtitle": "Areas of Parallelograms, Triangles, Trapezoids, Composite Figures, Coordinate Polygons & Base-60 Time",
        "kit_summary": "Counting & Array Tiles (COUNT-01) + Planetary Geared Clock (TIME-01)",
        "hero_png": "planetary_geared_clock_330.png",
        "coach_misconception": "Students multiply the slanted side of a parallelogram instead of the vertical height, forget to divide by 2 for triangles, lose track of multi-piece composite areas, and subtract clock times in base-10 instead of base-60.",
        "coach_remediation": "Slide the corner triangle of a parallelogram to form a straight [f] [RECT] rectangle, use the dedicated [g] [TRI] key ([g][7]) which divides by 2 automatically, accumulate composite chunks with [Σ+], and use the Planetary Clock (TIME-01) + [CLK] key for base-60 time.",
        "sections": [
            {
                "day_num": 20,
                "sec_num": "5.1",
                "title": "Areas of Parallelograms & Rectangles ([f] [RECT])",
                "big_ideas_ref": "Big Ideas Grade 6, Section 4.1 (Areas of Parallelograms)",
                "ccss": "CCSS.MATH.6.G.A.1",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Array Tiles",
                "asset_png": "counting_tiles_array_3x8.png",
                "diagram_type": "polygon_area",
                "diagram_data": {"shape": "parallelogram", "b": 12, "h": 8, "slant": 10, "caption": "Chop the right triangle off one end and slide it to the other: every parallelogram is a b × h Rectangle ([f] [RECT])! Ignore the slanted 10!"},
                "concept": "Textbooks always label a trap number on parallelograms: Base b, straight vertical Height h, AND the slanted side s. If you chop the corner triangle off one end and slide it to the other, every parallelogram turns into a straight b × h Rectangle! Cross out the slanted side and press b [ENTER] h [f] [RECT] ([f][7])!",
                "examples": [
                    {
                        "title": "Example 1: Dodge the Slanted Trap with [f] [RECT]",
                        "problem": "Find the area of a parallelogram with base b = 12 cm, vertical height h = 8 cm, and slanted side 10 cm.",
                        "block_step": "Cross out the slanted 10 cm trap! Push Base 12 onto Y, vertical Height 8 onto X, and press [f] [RECT] ([f][7]).",
                        "keys": ["12", "ENTER", "8", "f", "RECT"],
                        "stack_y": "12 (Base)",
                        "stack_x": "8 (Height)",
                        "ans": "96 cm²",
                        "note": "[f] [RECT] multiplies Base (Y) × Height (X) -> 96 cm²!"
                    },
                    {
                        "title": "Example 2: Finding a Missing Height from Area",
                        "problem": "A parallelogram banner has Area = 168 in² and Base = 14 in. Find its vertical height h.",
                        "block_step": "Since Area = b × h, undo multiplication with division: 168 ÷ 14!",
                        "keys": ["168", "ENTER", "14", "÷", "f", "LASTX", "f", "RECT"],
                        "stack_y": "168",
                        "stack_x": "14 -> 12",
                        "ans": "h = 12 in",
                        "note": "Check: 12 [f] [LASTX] [f] [RECT] gives 12 × 14 = 168 in²!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the area of a parallelogram with base b = 15 m, vertical height h = 9 m, and slanted side 11 m.", "keys": "15 [ENTER] 9 [f][RECT]", "yx": "Y:15 | X:9", "ans": "135 m² (Ignore 11m!)"},
                    {"num": 2, "part": "A", "prompt": "Find the area of a rectangle measuring 18 ft by 12 ft using [f] [RECT].", "keys": "18 [ENTER] 12 [f][RECT]", "yx": "Y:18 | X:12", "ans": "216 ft²"},
                    {"num": 3, "part": "A", "prompt": "Find the area of a parallelogram with b = 8.5 m and vertical height h = 6.4 m.", "keys": "8.5 [ENTER] 6.4 [f][RECT]", "yx": "Y:8.5 | X:6.4", "ans": "54.4 m²"},
                    {"num": 4, "part": "A", "prompt": "Find the area of a square tile with side 13 cm.", "keys": "13 [x²]", "yx": "Y:0 | X:169", "ans": "169 cm²"},
                    {"num": 5, "part": "B", "prompt": "A parallelogram has base b = 6 1/2 in and height h = 4 in. Find its area.", "keys": "6 [.] 1 [.] 2 [ENTER] 4 [f][RECT]", "yx": "Y:6 1/2 | X:4", "ans": "26 in²"},
                    {"num": 6, "part": "B", "prompt": "Missing Height: A parallelogram has Area = 108 cm² and base b = 12 cm. Find h.", "keys": "108 [ENTER] 12 [÷]", "yx": "Y:108 | X:12", "ans": "9 cm"},
                    {"num": 7, "part": "B", "prompt": "Missing Base: A parallelogram has Area = 135 ft² and vertical height h = 7.5 ft. Find b.", "keys": "135 [ENTER] 7.5 [÷]", "yx": "Y:135 | X:7.5", "ans": "18 ft"},
                    {"num": 8, "part": "B", "prompt": "Spot the Glitch: A parallelogram has b = 10, vertical h = 6, slanted side = 7.5. Sam got 75. Fix it!", "keys": "10 [ENTER] 6 [f][RECT]", "yx": "Y:10 | X:6", "ans": "60 (Sam multiplied slanted 7.5!)"},
                    {"num": 9, "part": "C", "prompt": "A slanted parking space has base 9 ft and straight length 18.5 ft. How much asphalt covers 4 spaces?", "keys": "9 [ENTER] 18.5 [f][RECT] 4 [×]", "yx": "Y:166.5 | X:4", "ans": "666 ft² (Way 2: base 36 × 18.5 = 666)"},
                    {"num": 10, "part": "C", "prompt": "A rectangular patio (15 ft × 12 ft) has a parallelogram planter (b=4 ft, h=3 ft) inside. Find the remaining patio area!", "keys": "15 [ENTER] 12 [f][RECT] 4 [ENTER] 3 [f][RECT] [-]", "yx": "Y:180 | X:12", "ans": "168 ft² (Way 2: 180 - 12 = 168)"}
                ]
            },
            {
                "day_num": 21,
                "sec_num": "5.2",
                "title": "Areas of Triangles — Half a Rectangle ([g] [TRI])",
                "big_ideas_ref": "Big Ideas Grade 6, Section 4.2 (Areas of Triangles)",
                "ccss": "CCSS.MATH.6.G.A.1",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Array Tiles",
                "asset_png": "counting_tiles_array_3x8.png",
                "diagram_type": "polygon_area",
                "diagram_data": {"shape": "triangle", "b": 10, "h": 6, "area": 30, "caption": "Two identical triangles always form a b × h rectangle (60). So 1 triangle is HALF a rectangle: [g] [TRI] = 30!"},
                "concept": "The #1 geometry test mistake is multiplying b × h for a triangle and forgetting to divide by 2! Look at key 7 on your SC-6: [f] [RECT] is b × h, and right next to it, [g] [TRI] ([g][7]) computes ½ × b × h in a single click so you never forget the ½!",
                "examples": [
                    {
                        "title": "Example 1: One-Click Triangle Area with [g] [TRI]",
                        "problem": "Find the area of a triangle with base b = 10 cm and height h = 6 cm.",
                        "block_step": "A 10 × 6 rectangle has area 60 cm². Cutting it diagonally in half gives two identical triangles of 30 cm² each!",
                        "keys": ["10", "ENTER", "6", "g", "TRI"],
                        "stack_y": "10 (Base)",
                        "stack_x": "6 (Height)",
                        "ans": "30 cm²",
                        "note": "[g] [TRI] ([g][7]) multiplies Y × X and divides by 2 automatically!"
                    },
                    {
                        "title": "Example 2: Finding a Missing Triangle Height (Double First!)",
                        "problem": "A triangular pennant has Area = 60 in² and base b = 15 in. Find its height h.",
                        "block_step": "First double the triangle's area (60 × 2 = 120) to rebuild the full rectangle, then divide by base 15!",
                        "keys": ["60", "ENTER", "2", "×", "15", "÷"],
                        "stack_y": "120 (2×Area)",
                        "stack_x": "15 -> 8",
                        "ans": "h = 8 in",
                        "note": "Check: 15 [ENTER] 8 [g] [TRI] -> 60 in²!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the area of a triangle with base b = 14 ft and height h = 18 ft using [g] [TRI].", "keys": "14 [ENTER] 18 [g][TRI]", "yx": "Y:14 | X:18", "ans": "126 ft²"},
                    {"num": 2, "part": "A", "prompt": "Find the area of a right triangle with base 9 ft, vertical height 4 ft, and slanted hypotenuse 9.85 ft.", "keys": "9 [ENTER] 4 [g][TRI]", "yx": "Y:9 | X:4", "ans": "18 ft² (Ignore 9.85!)"},
                    {"num": 3, "part": "A", "prompt": "Find the area of a triangle with b = 16 cm and h = 11 cm.", "keys": "16 [ENTER] 11 [g][TRI]", "yx": "Y:16 | X:11", "ans": "88 cm²"},
                    {"num": 4, "part": "A", "prompt": "Find the area of a triangle with decimal dimensions: b = 12.5 m, h = 8.4 m.", "keys": "12.5 [ENTER] 8.4 [g][TRI]", "yx": "Y:12.5 | X:8.4", "ans": "52.5 m²"},
                    {"num": 5, "part": "B", "prompt": "Find the area of a triangle with fractional dimensions: b = 4 1/2 in, h = 6 in.", "keys": "4 [.] 1 [.] 2 [ENTER] 6 [g][TRI]", "yx": "Y:4 1/2 | X:6", "ans": "13 1/2 in² (13.5)"},
                    {"num": 6, "part": "B", "prompt": "Missing Height: A triangle has Area = 54 cm² and base b = 12 cm. (Double 54 first, then ÷ 12!)", "keys": "54 [ENTER] 2 [×] 12 [÷]", "yx": "Y:108 | X:12", "ans": "9 cm"},
                    {"num": 7, "part": "B", "prompt": "Missing Base: A triangle has Area = 84 m² and height h = 14 m. Find base b.", "keys": "84 [ENTER] 2 [×] 14 [÷]", "yx": "Y:168 | X:14", "ans": "12 m"},
                    {"num": 8, "part": "B", "prompt": "Spot the Glitch: Leo found the area of a b=8, h=5 triangle as 40. What did he calculate instead?", "keys": "8 [ENTER] 5 [g][TRI]", "yx": "Y:8 | X:5", "ans": "20 (40 is the full rectangle!)"},
                    {"num": 9, "part": "C", "prompt": "A sailboat has a main sail (b=12 ft, h=25 ft) and jib sail (b=8 ft, h=15 ft). Find total sail area 2 ways!", "keys": "12 [ENTER] 25 [g][TRI] 8 [ENTER] 15 [g][TRI] [+]", "yx": "Y:150 | X:60", "ans": "210 ft² (Way 2: (300+120)÷2 = 210)"},
                    {"num": 10, "part": "C", "prompt": "A triangular gable window has Area = 36 ft² and base 9 ft. Find its height and check with [g] [TRI]!", "keys": "36 [ENTER] 2 [×] 9 [÷]", "yx": "Y:72 | X:9", "ans": "8 ft (Way 2: 9 [ENTER] 8 [g][TRI] = 36)"}
                ]
            },
            {
                "day_num": 22,
                "sec_num": "5.3",
                "title": "Trapezoids & Composite Figures with the [Σ+] Running Ledger",
                "big_ideas_ref": "Big Ideas Grade 6, Section 4.3 & 4.3 Ext (Trapezoids and Composite Figures)",
                "ccss": "CCSS.MATH.6.G.A.1",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Array Tiles",
                "asset_png": "counting_tiles_distributive_4color.png",
                "diagram_type": "polygon_area",
                "diagram_data": {"shape": "composite", "rect_b": 12, "rect_h": 8, "tri_b": 12, "tri_h": 5, "caption": "Shed Wall = Rectangle (12×8 = 96, tap [Σ+]) + Roof Triangle (½×12×5 = 30, tap [Σ+]). Read [f] [Σx] = 126 ft²!"},
                "concept": "Composite figures (weird shapes made of rectangles and triangles) are easy when you use the SC-6 [Σ+] running accumulator! Clear memory with [g] [CLΣ] ([g][÷]). Compute each simple piece ([f] [RECT] or [g] [TRI]) and tap [Σ+] to toss it in the bucket (use [f] [Σ-] to subtract a cutout hole), then read the grand total with [f] [Σx] ([f][N])!",
                "examples": [
                    {
                        "title": "Example 1: House Wall Composite (Rectangle + Triangle via [Σ+])",
                        "problem": "Find the total area of a 12 ft × 8 ft rectangular wall topped by a roof triangle (b = 12 ft, h = 5 ft).",
                        "block_step": "Clear stats ([g] [CLΣ]). Piece 1: 12 [ENTER] 8 [f] [RECT] [Σ+] (96, n=1). Piece 2: 12 [ENTER] 5 [g] [TRI] [Σ+] (30, n=2). Read [f] [Σx]!",
                        "keys": ["g", "CLΣ", "12", "ENTER", "8", "f", "RECT", "Σ+", "12", "ENTER", "5", "g", "TRI", "Σ+", "f", "Σx"],
                        "stack_y": "96 + 30",
                        "stack_x": "126 (Total)",
                        "ans": "126 ft²",
                        "note": "The screen counts n = 1, n = 2 so you never forget a piece!"
                    },
                    {
                        "title": "Example 2: Area of a Trapezoid (Average Base × Height)",
                        "problem": "Find the area of a trapezoid desk with parallel bases b₁ = 48 in, b₂ = 36 in, and depth h = 24 in.",
                        "block_step": "Add the two bases (48 + 36 = 84), multiply by height 24, and divide by 2 (or use [g] [TRI] on (b₁+b₂) and h!).",
                        "keys": ["48", "ENTER", "36", "+", "24", "g", "TRI"],
                        "stack_y": "84 (b₁+b₂)",
                        "stack_x": "24 -> 1008",
                        "ans": "1,008 in²",
                        "note": "Shortcut: (b₁ + b₂) [ENTER] h [g] [TRI] computes ½(b₁+b₂)h in 1 step!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the area of a trapezoid with b₁ = 10 cm, b₂ = 14 cm, and h = 6 cm using (b₁+b₂) [ENTER] h [g] [TRI].", "keys": "10 [ENTER] 14 [+] 6 [g][TRI]", "yx": "Y:24 | X:6", "ans": "72 cm²"},
                    {"num": 2, "part": "A", "prompt": "Find the area of a trapezoid with b₁ = 18 ft, b₂ = 12 ft, and h = 9 ft.", "keys": "18 [ENTER] 12 [+] 9 [g][TRI]", "yx": "Y:30 | X:9", "ans": "135 ft²"},
                    {"num": 3, "part": "A", "prompt": "L-Shape Room: Split into Room A (10 × 6) and Room B (8 × 4). Sum with [Σ+] and [f] [Σx].", "keys": "10 [ENTER] 6 [f][RECT] [Σ+] 8 [ENTER] 4 [f][RECT] [Σ+] [f][Σx]", "yx": "60 + 32", "ans": "92"},
                    {"num": 4, "part": "A", "prompt": "Banner Arrow: A 15 × 6 rectangle attached to a triangle (b = 10, h = 6). Find total area.", "keys": "15 [ENTER] 6 [f][RECT] [Σ+] 10 [ENTER] 6 [g][TRI] [Σ+] [f][Σx]", "yx": "90 + 30", "ans": "120"},
                    {"num": 5, "part": "B", "prompt": "Find the area of a trapezoid with decimal bases b₁ = 8.5 m, b₂ = 5.5 m, and h = 4.2 m.", "keys": "8.5 [ENTER] 5.5 [+] 4.2 [g][TRI]", "yx": "Y:14 | X:4.2", "ans": "29.4 m²"},
                    {"num": 6, "part": "B", "prompt": "Cutout Frame: A 10 in × 8 in frame has a 6 in × 4 in hole cut out. Use [Σ+] and [f] [Σ-] to find the border area!", "keys": "10 [ENTER] 8 [f][RECT] [Σ+] 6 [ENTER] 4 [f][RECT] [f][Σ-] [f][Σx]", "yx": "80 - 24", "ans": "56 in²"},
                    {"num": 7, "part": "B", "prompt": "Missing Trapezoid Height: A trapezoid has Area = 90 cm² and bases b₁ = 11 cm, b₂ = 7 cm. Find h.", "keys": "90 [ENTER] 2 [×] 11 [ENTER] 7 [+] [÷]", "yx": "Y:180 | X:18", "ans": "10 cm"},
                    {"num": 8, "part": "B", "prompt": "A mini-golf hole is a 12 × 5 ft rectangle plus a trapezoid (b₁=5, b₂=9, h=4). Find total area.", "keys": "60 [Σ+] 5 [ENTER] 9 [+] 4 [g][TRI] [Σ+] [f][Σx]", "yx": "60 + 28", "ans": "88 ft²"},
                    {"num": 9, "part": "C", "prompt": "Find the area of a trapezoid (b₁=10, b₂=16, h=8) both with the trapezoid formula AND by splitting into a 10×8 rect + 6×8 triangle!", "keys": "10 [ENTER] 16 [+] 8 [g][TRI]", "yx": "Y:26 | X:8", "ans": "104 (Way 2: 80 + 24 = 104)"},
                    {"num": 10, "part": "C", "prompt": "A 20 ft × 15 ft lawn has a triangular flowerbed (b=8 ft, h=6 ft) and square shed (5 ft × 5 ft). Find grass area!", "keys": "300 [Σ+] 24 [f][Σ-] 25 [f][Σ-] [f][Σx]", "yx": "300 - 24 - 25", "ans": "251 ft²"}
                ]
            },
            {
                "day_num": 23,
                "sec_num": "5.4",
                "title": "Coordinate Polygons & Planetary Clock Base-60 Time ([CLK])",
                "big_ideas_ref": "Big Ideas Grade 6, Section 4.4 (Polygons in the Coordinate Plane) & Time Lab",
                "ccss": "CCSS.MATH.6.G.A.3",
                "kit_id": "TIME-01",
                "kit_name": "Planetary Geared Clock",
                "asset_png": "planetary_geared_clock_330.png",
                "diagram_type": "clock_dial",
                "diagram_data": {"start": "1:45", "add": "+1h 35m", "end": "3:20", "caption": "Planetary Clock (TIME-01) & [CLK]: 1.45 + 1.35 bundles 60 minutes into +1 hour -> 3:20 (NEVER 2.80)!"},
                "concept": "On a coordinate grid, find rectangle side lengths by subtracting the x-coordinates and y-coordinates. And when adding/subtracting hours and minutes, remember time is Base-60! Press [CLK] on the SC-6 to enter H.MM mode (1.45 [ENTER] 1.35 [+] -> 3.20), or use [f] [▸HR] ([f][CLK]) to turn 3 hr 15 min (3.15) into 3.25 decimal hours!",
                "examples": [
                    {
                        "title": "Example 1: Coordinate Rectangle Perimeter & Area",
                        "problem": "A rectangle has vertices (2, 3), (9, 3), (9, 8), and (2, 8). Find its width, height, perimeter, and area.",
                        "block_step": "Width = 9 - 2 = 7 units. Height = 8 - 3 = 5 units. Area = 7 × 5 = 35 sq units; Perimeter = 2(7 + 5) = 24 units.",
                        "keys": ["9", "ENTER", "2", "-", "8", "ENTER", "3", "-", "f", "RECT"],
                        "stack_y": "7 (Width)",
                        "stack_x": "5 (Height) -> 35",
                        "ans": "Width = 7, Height = 5, Perimeter = 24, Area = 35",
                        "note": "Subtract x-coords for horizontal width; subtract y-coords for vertical height!"
                    },
                    {
                        "title": "Example 2: Modulo-60 Clock Addition & [f] [▸HR] Paycheck",
                        "problem": "A print job starts at 9:40 and takes 2 hr 50 min. Find finish time ([CLK]), and convert 3 hr 15 min to decimal hours.",
                        "block_step": "In [CLK] mode: 9.40 [ENTER] 2.50 [+] -> 12.30 (12:30 PM). For 3 hr 15 min: 3.15 [f] [▸HR] -> 3.25 hours!",
                        "keys": ["CLK", "9.40", "ENTER", "2.50", "+", "3.15", "f", "▸HR"],
                        "stack_y": "12.30 (12:30)",
                        "stack_x": "3.25 hr",
                        "ans": "Finishes at 12:30; 3 hr 15 min = 3.25 hr",
                        "note": "[f] [▸HR] converts H.MM -> decimal hours; [g] [▸HMS] converts back!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the distance between (3, 4) and (11, 4) on a coordinate grid.", "keys": "11 [ENTER] 3 [-]", "yx": "Y:11 | X:3", "ans": "8 units"},
                    {"num": 2, "part": "A", "prompt": "A rectangle has corners (1, 2), (10, 2), (10, 8), (1, 8). Find its area.", "keys": "10 [ENTER] 1 [-] 8 [ENTER] 2 [-] [f][RECT]", "yx": "Y:9 | X:6", "ans": "54 sq units"},
                    {"num": 3, "part": "A", "prompt": "In [CLK] mode, add 1 hr 45 min + 1 hr 35 min (1.45 [ENTER] 1.35 [+]).", "keys": "[CLK] 1.45 [ENTER] 1.35 [+]", "yx": "Y:1.45 | X:1.35", "ans": "3 hr 20 min (3.20)"},
                    {"num": 4, "part": "A", "prompt": "Convert 2 hr 30 min (2.30) to decimal hours using [f] [▸HR].", "keys": "2.30 [f][▸HR]", "yx": "2h 30m -> dec", "ans": "2.5 hours"},
                    {"num": 5, "part": "B", "prompt": "Convert 4 hr 45 min (4.45) to decimal hours using [f] [▸HR].", "keys": "4.45 [f][▸HR]", "yx": "4h 45m -> dec", "ans": "4.75 hours"},
                    {"num": 6, "part": "B", "prompt": "Convert 1.75 decimal hours back into Hours & Minutes using [g] [▸HMS].", "keys": "1.75 [g][▸HMS]", "yx": "1.75 -> H.MM", "ans": "1 hr 45 min (1.45)"},
                    {"num": 7, "part": "B", "prompt": "In [CLK] mode, find elapsed time from 8:50 AM to 11:25 AM (11.25 [ENTER] 8.50 [-]).", "keys": "[CLK] 11.25 [ENTER] 8.50 [-]", "yx": "Y:11.25 | X:8.50", "ans": "2 hr 35 min (2.35)"},
                    {"num": 8, "part": "B", "prompt": "A right triangle on a grid has vertices (2, 1), (10, 1), and (2, 7). Find its area!", "keys": "8 [ENTER] 6 [g][TRI]", "yx": "Y:8 | X:6", "ans": "24 sq units"},
                    {"num": 9, "part": "C", "prompt": "You tutor for 3 hr 15 min (3.15) at $16/hr. Convert to decimal hours with [f] [▸HR] and find your pay 2 ways!", "keys": "3.15 [f][▸HR] 16 [×]", "yx": "Y:3.25 | X:16", "ans": "$52.00 (Way 2: 3×16 + ¼×16 = 48+4 = 52)"},
                    {"num": 10, "part": "C", "prompt": "Coordinate Park: Vertices (2, 2), (14, 2), (14, 11), (2, 11) where 1 unit = 10 yd. Find perimeter and area!", "keys": "12 [ENTER] 9 [f][RECT]", "yx": "Y:12 | X:9", "ans": "P = 42 units (420 yd); A = 108 sq units (10,800 yd²)"}
                ]
            }
        ]
    }
]

CHAPTERS_DATA.extend([
    # =========================================================================
    # CHAPTER 6: INTEGERS, RATIONAL NUMBERS & THE COORDINATE PLANE (Sections 6.1 - 6.5)
    # =========================================================================
    {
        "num": 6,
        "title": "Integers, Rational Numbers & The Coordinate Plane",
        "big_ideas_book": "Big Ideas Math Grade 6 — Chapter 6",
        "subtitle": "Positive & Negative Integers, Comparing Rational Numbers, Absolute Value, and the 4-Quadrant Coordinate Plane",
        "kit_summary": "Ten-Frame Bicolor Counters (BASE-10) + Number Rack (RACK-01)",
        "hero_png": "ten_frame_subitizing_5anchor.png",
        "coach_misconception": "Students confuse the subtraction operator [-] with the negative sign [+/-], think -18 > -5 because 18 > 5, confuse Opposite ([+/-]) with Absolute Value ([g] [|x|]), and reverse (x, y) coordinates.",
        "coach_remediation": "Use Yellow (+1) and Red (-1) Zero-Pair counters, test inequalities with [f] [>] and [g] [<], contrast [+/-] (flip sign) with [g] [|x|] (always positive distance from 0), and use the Elevator Rule (walk across x first, ride up/down y second).",
        "sections": [
            {
                "day_num": 24,
                "sec_num": "6.1",
                "title": "Positive & Negative Integers — Zero Pairs & The [+/-] Sign Flipper",
                "big_ideas_ref": "Big Ideas Grade 6, Section 6.1 (Integers)",
                "ccss": "CCSS.MATH.6.NS.C.5",
                "kit_id": "BASE-10",
                "kit_name": "Ten-Frame Zero-Pair Counters",
                "asset_png": "ten_frame_subitizing_5anchor.png",
                "diagram_type": "zero_pairs",
                "diagram_data": {"pos": 3, "neg": 5, "net": -2, "caption": "3 Yellow (+1) counters + 5 Red (-1) counters -> 3 Zero Pairs cancel to 0, leaving 2 Red (-2)!"},
                "concept": "On regular calculators, mixing up the minus key and negative key causes SYNTAX ERROR. On the SC-6, [-] is the two-number subtraction action, while [+/-] flips the sign of the number on Floor 1 (X) between Positive (+) and Negative (-)—just like flipping a counter from Yellow (+) to Red (-)!",
                "examples": [
                    {
                        "title": "Example 1: Opposites & Zero-Pair Cancellation with [+/-]",
                        "problem": "Enter -15 on the SC-6, find its opposite, and verify that -15 + 15 = 0.",
                        "block_step": "15 Red (-1) counters and 15 Yellow (+1) counters pair up 1-for-1 into 15 Zero Pairs (= 0).",
                        "keys": ["15", "+/-", "ENTER", "15", "+"],
                        "stack_y": "-15",
                        "stack_x": "15 -> 0",
                        "ans": "Opposite of -15 is +15; -15 + 15 = 0",
                        "note": "Type the digits 15 first, THEN tap [+/-] to make it -15!"
                    },
                    {
                        "title": "Example 2: Real-World Elevation & Bank Ledger",
                        "problem": "You start at $0, deposit $35, spend $50 (50 [+/-]), and deposit $20. Find your final balance.",
                        "block_step": "Deposits are positive (+35, +20 = +55); spending is negative (-50). 55 and -50 leave +$5!",
                        "keys": ["35", "ENTER", "50", "+/-", "+", "20", "+"],
                        "stack_y": "-15 (Step 1)",
                        "stack_x": "20 -> +5",
                        "ans": "+$5",
                        "note": "Wait! Notice how 50 [+/-] [+] adds a negative (-50) cleanly!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Write the integer for '25 feet below sea level' and find its opposite using [+/-].", "keys": "25 [+/-] -> -25; [+/-] -> 25", "yx": "-25 <-> +25", "ans": "-25; Opposite = +25"},
                    {"num": 2, "part": "A", "prompt": "Find the opposite of -42, and then the opposite of the opposite (-[ -(-42) ]).", "keys": "42 [+/-] [+/-] [+/-]", "yx": "-42 -> +42 -> -42", "ans": "+42; and -42"},
                    {"num": 3, "part": "A", "prompt": "Zero-Pair Cancellation: A submarine is at -18 m and rises +18 m. Where is it now?", "keys": "18 [+/-] [ENTER] 18 [+]", "yx": "Y:-18 | X:18", "ans": "0 m (Sea level)"},
                    {"num": 4, "part": "A", "prompt": "Combine 6 Yellow (+1) counters and 6 Red (-1) counters. What is the value?", "keys": "6 [ENTER] 6 [+/-] [+]", "yx": "Y:6 | X:-6", "ans": "0"},
                    {"num": 5, "part": "B", "prompt": "A hiker starts at -120 ft in a canyon and climbs +120 ft. What is her elevation?", "keys": "120 [+/-] [ENTER] 120 [+]", "yx": "Y:-120 | X:120", "ans": "0 ft"},
                    {"num": 6, "part": "B", "prompt": "What integer is its own opposite? Test 0 [+/-] on your SC-6!", "keys": "0 [+/-]", "yx": "X: 0", "ans": "0"},
                    {"num": 7, "part": "B", "prompt": "Temperature starts at 0°F, drops 12°F (12 [+/-]), and rises 19°F. Find the temperature.", "keys": "12 [+/-] [ENTER] 19 [+]", "yx": "Y:-12 | X:19", "ans": "+7°F"},
                    {"num": 8, "part": "B", "prompt": "Golf Par: -3 means 3 strokes under par. If you shoot -3 on Saturday and +3 on Sunday, what is your total?", "keys": "3 [+/-] [ENTER] 3 [+]", "yx": "Y:-3 | X:3", "ans": "0 (Even par)"},
                    {"num": 9, "part": "C", "prompt": "Elevator starts at Floor 0, goes up 14, down 20 (20 [+/-]), and up 9. Find the floor 2 ways!", "keys": "14 [ENTER] 20 [+/-] [+] 9 [+]", "yx": "Y:-6 | X:9", "ans": "Floor 3 (Way 2: (14+9) - 20 = 3)"},
                    {"num": 10, "part": "C", "prompt": "Game XP: You gain 40 XP, lose 65 XP, and gain 25 XP. Did you break even? Prove 2 ways!", "keys": "40 [ENTER] 65 [+/-] [+] 25 [+]", "yx": "Y:-25 | X:25", "ans": "0 XP (Break even! 40+25 = 65)"}
                ]
            },
            {
                "day_num": 25,
                "sec_num": "6.2",
                "title": "Comparing & Ordering Integers and Rational Numbers",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 6.2 & 6.3 (Comparing & Ordering Integers and Rational Numbers)",
                "ccss": "CCSS.MATH.6.NS.C.7",
                "kit_id": "RACK-01",
                "kit_name": "Number Rack & Number Line",
                "asset_png": "number_rack_subitizing.png",
                "diagram_type": "zero_pairs",
                "diagram_data": {"pos": 2, "neg": 5, "net": -3, "caption": "Number Line Rule: Further to the RIGHT is ALWAYS greater (-5 is to the right of -18, so -5 > -18)!"},
                "concept": "When kids see -18 and -5, their instinct says -18 is bigger because 18 > 5. Think of temperature: -5°F is WARMER than -18°F! On a horizontal number line ([f] [LINE]), further to the RIGHT is always greater. Test any inequality on the SC-6 with [f] [>] ([f][≠]) and [g] [<] ([g][≠]): 1 = TRUE, 0 = FALSE!",
                "examples": [
                    {
                        "title": "Example 1: Testing Negative Inequalities with [f] [>] & [g] [<]",
                        "problem": "Compare -5 and -18. Which one is greater?",
                        "block_step": "On the number line, -5 is 5 steps left of 0, while -18 is 18 steps left of 0. Since -5 is to the right of -18, -5 > -18!",
                        "keys": ["5", "+/-", "ENTER", "18", "+/-", "f", ">"],
                        "stack_y": "-5",
                        "stack_x": "-18 -> 1 (True)",
                        "ans": "-5 > -18 (SC-6 outputs 1 = TRUE)",
                        "note": "If you test [g] [<], the SC-6 outputs 0 (FALSE)!"
                    },
                    {
                        "title": "Example 2: Comparing Negative Fractions & Decimals",
                        "problem": "Compare -4/5 and -0.75. Which one is greater?",
                        "block_step": "Convert -4/5 to a decimal with [FDISP]: -4/5 = -0.80. Since -0.75 is closer to 0 (further right) than -0.80, -0.75 > -4/5!",
                        "keys": [".", "4", ".", "5", "+/-", "FDISP", "0.75", "+/-", "g", "<"],
                        "stack_y": "-0.80 (-4/5)",
                        "stack_x": "-0.75 -> 1",
                        "ans": "-0.80 < -0.75 (so -0.75 is greater!)",
                        "note": "Convert fractions to decimals with [FDISP] to compare in seconds!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Which temperature is warmer (greater): -12°C or -5°C? Test with [g] [<].", "keys": "12 [+/-] [ENTER] 5 [+/-] [g][<]", "yx": "Y:-12 | X:-5", "ans": "-5°C (-12 < -5)"},
                    {"num": 2, "part": "A", "prompt": "Compare -9 and -2 using > or <.", "keys": "9 [+/-] [ENTER] 2 [+/-] [g][<]", "yx": "Y:-9 | X:-2", "ans": "-9 < -2"},
                    {"num": 3, "part": "A", "prompt": "Compare -15 and 0 using > or <.", "keys": "15 [+/-] [ENTER] 0 [g][<]", "yx": "Y:-15 | X:0", "ans": "-15 < 0"},
                    {"num": 4, "part": "A", "prompt": "Order the integers from least to greatest: 4, -7, 0, -2, -10.", "keys": "Left-to-right on number line", "yx": "Coldest to warmest", "ans": "-10, -7, -2, 0, 4"},
                    {"num": 5, "part": "B", "prompt": "Compare -3/4 and -0.6. (Hint: -3/4 = -0.75. Which is further right?)", "keys": "0.75 [+/-] [ENTER] 0.6 [+/-] [g][<]", "yx": "Y:-0.75 | X:-0.6", "ans": "-3/4 < -0.6 (-0.6 is greater)"},
                    {"num": 6, "part": "B", "prompt": "Compare -2 1/2 and -2.3 using > or <.", "keys": "2.5 [+/-] [ENTER] 2.3 [+/-] [g][<]", "yx": "Y:-2.5 | X:-2.3", "ans": "-2 1/2 < -2.3"},
                    {"num": 7, "part": "B", "prompt": "Compare -5/8 and -7/8.", "keys": "[.] 5 [.] 8 [+/-] [ENTER] [.] 7 [.] 8 [+/-] [f][>]", "yx": "-0.625 > -0.875", "ans": "-5/8 > -7/8"},
                    {"num": 8, "part": "B", "prompt": "Spot the Glitch: Leo says -4.5 > -4.1 because 4.5 > 4.1. Explain why -4.1 is actually greater!", "keys": "4.5 [+/-] [ENTER] 4.1 [+/-] [g][<]", "yx": "-4.5 < -4.1", "ans": "-4.1 is closer to 0 (further right)"},
                    {"num": 9, "part": "C", "prompt": "Order -1.5, 1 1/4, -1 3/4, and -0.5 from least to greatest. Verify both as decimals AND with [g] [<]!", "keys": "-1.75, -1.5, -0.5, 1.25", "yx": "All pairwise [g][<]=1", "ans": "-1 3/4, -1.5, -0.5, 1 1/4"},
                    {"num": 10, "part": "C", "prompt": "Three divers are at -14.8 m, -14 1/2 m, and -15.2 m. Who is deepest (least) and who is shallowest (greatest)?", "keys": "-15.2 < -14.8 < -14.5", "yx": "-14 1/2 = -14.5", "ans": "Deepest: -15.2 m; Shallowest: -14 1/2 m"}
                ]
            },
            {
                "day_num": 26,
                "sec_num": "6.3",
                "title": "Absolute Value — Distance From Zero Is Always Positive ([g] [|x|])",
                "big_ideas_ref": "Big Ideas Grade 6, Section 6.4 (Absolute Value)",
                "ccss": "CCSS.MATH.6.NS.C.7c",
                "kit_id": "RACK-01",
                "kit_name": "Number Rack & Zero-Pair Studio",
                "asset_png": "number_rack_subitizing.png",
                "diagram_type": "zero_pairs",
                "diagram_data": {"pos": 6, "neg": 6, "net": 0, "caption": "Both -6 and +6 are exactly 6 steps from 0: |-6| = 6 and |+6| = 6! Distance is never negative."},
                "concept": "Students often confuse Opposite ([+/-]) with Absolute Value ([g] [|x|], [g][+/-]). Opposite flips the sign (+9 -> -9, -9 -> +9). Absolute Value asks 'How many steps from 0?' Since you can't walk a negative number of steps, [g] [|x|] is ALWAYS positive (or 0)!",
                "examples": [
                    {
                        "title": "Example 1: Opposite ([+/-]) vs. Absolute Value ([g] [|x|])",
                        "problem": "Find |-14|, |14|, and -|-14| on your SC-6.",
                        "block_step": "-14 is 14 steps from 0, so |-14| = 14. In -|-14|, find |-14| = 14 first, then apply the outside negative sign -> -14!",
                        "keys": ["14", "+/-", "g", "|x|"],
                        "stack_y": "|-14|",
                        "stack_x": "+14",
                        "ans": "|-14| = 14, |14| = 14, -|-14| = -14",
                        "note": "[g] [|x|] ([g][+/-]) makes any number on Floor 1 positive!"
                    },
                    {
                        "title": "Example 2: Multi-Step Absolute Value 50 - |-18|",
                        "problem": "Evaluate 50 - |-18|. (Watch out: does -|-18| turn into +18?)",
                        "block_step": "Park 50 on Floor 2 (Y). Enter 18 [+/-] on Floor 1 (X) and press [g] [|x|] -> X becomes +18. Now press [-] -> 50 - 18 = 32!",
                        "keys": ["50", "ENTER", "18", "+/-", "g", "|x|", "-"],
                        "stack_y": "50",
                        "stack_x": "18 -> 32",
                        "ans": "32 (NOT 68!)",
                        "note": "|-18| becomes +18 BEFORE you subtract it from 50!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find |-27| using [g] [|x|].", "keys": "27 [+/-] [g][|x|]", "yx": "X: 27", "ans": "27"},
                    {"num": 2, "part": "A", "prompt": "Evaluate |-27| + |13|.", "keys": "27 [+/-] [g][|x|] [ENTER] 13 [+]", "yx": "Y:27 | X:13", "ans": "40"},
                    {"num": 3, "part": "A", "prompt": "Evaluate |-4.8| + |-3.2|.", "keys": "4.8 [+/-] [g][|x|] [ENTER] 3.2 [+/-] [g][|x|] [+]", "yx": "Y:4.8 | X:3.2", "ans": "8.0"},
                    {"num": 4, "part": "A", "prompt": "Evaluate |-35| - |-19|.", "keys": "35 [+/-] [g][|x|] [ENTER] 19 [+/-] [g][|x|] [-]", "yx": "Y:35 | X:19", "ans": "16"},
                    {"num": 5, "part": "B", "prompt": "Compare |-12| and |9| using > or <. (Which is further from 0?)", "keys": "12 > 9", "yx": "Y:12 | X:9", "ans": "|-12| > |9| (12 > 9)"},
                    {"num": 6, "part": "B", "prompt": "Evaluate -|-24|. (Find |-24| first, then press [+/-] for the outside minus!)", "keys": "24 [+/-] [g][|x|] [+/-]", "yx": "24 -> -24", "ans": "-24"},
                    {"num": 7, "part": "B", "prompt": "Evaluate 50 - |-18|. Find |-18| first, then subtract from 50.", "keys": "50 [ENTER] 18 [+/-] [g][|x|] [-]", "yx": "Y:50 | X:18", "ans": "32"},
                    {"num": 8, "part": "B", "prompt": "Order from least to greatest: |-8|, -6, |-3|, 0, -|-9|.", "keys": "Values: 8, -6, 3, 0, -9", "yx": "-9, -6, 0, 3, 8", "ans": "-|-9|, -6, 0, |-3|, |-8|"},
                    {"num": 9, "part": "C", "prompt": "A diver is at -32 ft and a seagull is at +25 ft. Which is closer to sea level (0), and by how many feet?", "keys": "32 [+/-] [g][|x|] [ENTER] 25 [-]", "yx": "Y:32 | X:25", "ans": "Seagull is closer by 7 ft (25 < 32)"},
                    {"num": 10, "part": "C", "prompt": "Two accounts have balances of -$45 and -$28. Which account has the greater debt (|-45| vs |-28|), and which has the greater balance?", "keys": "|-45|=45 > |-28|=28", "yx": "-45 < -28", "ans": "Greater debt: -$45 ($45); Greater balance: -$28"}
                ]
            },
            {
                "day_num": 27,
                "sec_num": "6.4",
                "title": "The 4-Quadrant Coordinate Plane & Axis Reflections",
                "big_ideas_ref": "Big Ideas Grade 6, Section 6.5 (The Coordinate Plane)",
                "ccss": "CCSS.MATH.6.NS.C.6",
                "kit_id": "COUNT-01",
                "kit_name": "4x4 Gridfinity Baseplate & Tiles",
                "asset_png": "counting_tiles_array_3x8.png",
                "diagram_type": "coord_plane",
                "diagram_data": {"pts": [("(4,3) QI", 4, 3), ("(-4,3) QII", -4, 3), ("(-4,-3) QIII", -4, -3), ("(4,-3) QIV", 4, -3)], "caption": "Reflections flip signs with [+/-]: Across y-axis flips x -> (-4,3); across x-axis flips y -> (4,-3)!"},
                "concept": "To never mix up (x, y), use the Elevator Rule: walk ACROSS the lobby first (x: right +, left -), then ride UP/DOWN the elevator (y: up +, down -)! Reflecting across the y-axis flips the x-sign ([+/-]); reflecting across the x-axis flips the y-sign ([+/-])!",
                "examples": [
                    {
                        "title": "Example 1: Naming Quadrants I, II, III, and IV",
                        "problem": "Identify the quadrant for A(-6, 5), B(4, -7), and C(-3, -8).",
                        "block_step": "A(-, +) goes left 6, up 5 -> Quad II. B(+, -) goes right 4, down 7 -> Quad IV. C(-, -) goes left 3, down 8 -> Quad III.",
                        "keys": ["6", "+/-", "ENTER", "5"],
                        "stack_y": "-6 (x: Left)",
                        "stack_x": "+5 (y: Up)",
                        "ans": "A: Quad II, B: Quad IV, C: Quad III",
                        "note": "QI: (+,+), QII: (-,+), QIII: (-,-), QIV: (+,-)!"
                    },
                    {
                        "title": "Example 2: Axis Reflections Using [+/-]",
                        "problem": "Start at P(-5, 8). Reflect across the x-axis, then reflect that new point across the y-axis.",
                        "block_step": "Across x-axis (horizontal mirror): x stays -5, y flips to -8 -> (-5, -8). Across y-axis: x flips to +5, y stays -8 -> (5, -8)!",
                        "keys": ["5", "+/-", "ENTER", "8", "+/-", "x⇄y", "+/-", "x⇄y"],
                        "stack_y": "+5 (New x)",
                        "stack_x": "-8 (New y)",
                        "ans": "Step 1: (-5, -8); Final: (5, -8) in Quad IV",
                        "note": "Reflecting across BOTH axes flips both signs with [+/-]!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Name the Quadrant (I, II, III, or IV) for point (7, -4).", "keys": "(+, -) -> Right, Down", "yx": "Y:7 | X:-4", "ans": "Quadrant IV"},
                    {"num": 2, "part": "A", "prompt": "Name the Quadrant for point (-9, -2).", "keys": "(-, -) -> Left, Down", "yx": "Y:-9 | X:-2", "ans": "Quadrant III"},
                    {"num": 3, "part": "A", "prompt": "Name the Quadrant for point (-5, 11).", "keys": "(-, +) -> Left, Up", "yx": "Y:-5 | X:11", "ans": "Quadrant II"},
                    {"num": 4, "part": "A", "prompt": "Reflect (6, 9) across the y-axis. (Flip the x-coordinate with [+/-]!)", "keys": "6 [+/-] -> -6", "yx": "Y:-6 | X:9", "ans": "(-6, 9)"},
                    {"num": 5, "part": "B", "prompt": "Reflect (6, 9) across the x-axis. (Flip the y-coordinate with [+/-]!)", "keys": "9 [+/-] -> -9", "yx": "Y:6 | X:-9", "ans": "(6, -9)"},
                    {"num": 6, "part": "B", "prompt": "Reflect (-3, -7) across the x-axis.", "keys": "7 [+/-] [+/-] -> +7", "yx": "Y:-3 | X:7", "ans": "(-3, 7)"},
                    {"num": 7, "part": "B", "prompt": "Reflect (-8, 4) across the y-axis, and then across the x-axis.", "keys": "Flip x -> (8,4); flip y -> (8,-4)", "yx": "Y:8 | X:-4", "ans": "(8, -4)"},
                    {"num": 8, "part": "B", "prompt": "On the Fence: Which axis does (0, -9) sit on, and which axis does (-7, 0) sit on?", "keys": "0 sideways vs 0 up/down", "yx": "(0,-9) & (-7,0)", "ans": "(0,-9) on y-axis; (-7,0) on x-axis"},
                    {"num": 9, "part": "C", "prompt": "Start at (4, -5). Walk 7 units left and 8 units up. Where do you land, and in which quadrant?", "keys": "4 [ENTER] 7 [-]; 5 [+/-] [ENTER] 8 [+]", "yx": "Y:-3 | X:3", "ans": "(-3, 3) in Quadrant II"},
                    {"num": 10, "part": "C", "prompt": "Points A(-4, 2), B(4, 2), and C(4, -5) are 3 corners of a rectangle. Find the 4th corner D!", "keys": "Match x of A (-4) & y of C (-5)", "yx": "Y:-4 | X:-5", "ans": "D(-4, -5) in Quadrant III"}
                ]
            },
            {
                "day_num": 28,
                "sec_num": "6.5",
                "title": "Distance Between Points on the Coordinate Plane ([g] [|x|])",
                "big_ideas_ref": "Big Ideas Grade 6, Section 6.5 Ext (Distances on the Coordinate Plane)",
                "ccss": "CCSS.MATH.6.NS.C.8",
                "kit_id": "COUNT-01",
                "kit_name": "Baseplate & Zero-Pair Studio",
                "asset_png": "number_rack_subitizing.png",
                "diagram_type": "coord_plane",
                "diagram_data": {"pts": [("(-6,4)", -6, 4), ("(9,4)", 9, 4)], "caption": "Bridge from (-6, 4) to (9, 4): 6 steps to y-axis + 9 steps past axis = 15 units! Or |-6 - 9| = 15!"},
                "concept": "When two points share a coordinate like (-6, 4) and (9, 4), how far apart are they? If they are in different quadrants (cross an axis), add their distances to the axis (|-6| + |9| = 15). Even faster: on the SC-6, subtract ANY two coordinates and press [g] [|x|] (-6 - 9 = -15 -> |-15| = 15)!",
                "examples": [
                    {
                        "title": "Example 1: Cross-Axis Distance vs. Same-Quadrant Distance",
                        "problem": "Find the distance between (-6, 4) and (9, 4), and between (-12, -3) and (-4, -3).",
                        "block_step": "Cross-axis: 6 + 9 = 15 units. Same quadrant: 12 - 4 = 8 units. On SC-6, [subtract] then [g] [|x|] works for BOTH!",
                        "keys": ["6", "+/-", "ENTER", "9", "-", "g", "|x|"],
                        "stack_y": "-15 (Diff)",
                        "stack_x": "15 (Dist)",
                        "ans": "15 units; and 8 units",
                        "note": "Subtracting and pressing [g] [|x|] works whether points cross an axis or not!"
                    },
                    {
                        "title": "Example 2: 4-Quadrant Rectangle Perimeter & Area",
                        "problem": "A rectangle has vertices (-4, 6), (5, 6), (5, -2), and (-4, -2). Find its perimeter and area.",
                        "block_step": "Width from -4 to 5 is |-4 - 5| = 9 units. Height from 6 to -2 is |6 - (-2)| = 8 units.",
                        "keys": ["4", "+/-", "ENTER", "5", "-", "g", "|x|", "6", "ENTER", "2", "+/-", "-", "f", "RECT"],
                        "stack_y": "9 (Width)",
                        "stack_x": "8 (Height) -> 72",
                        "ans": "Width = 9, Height = 8, Perimeter = 34, Area = 72",
                        "note": "Perimeter = 2(9 + 8) = 34 units; Area = 9 × 8 = 72 sq units!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the horizontal distance between (-8, 5) and (11, 5).", "keys": "8 [+/-] [ENTER] 11 [-] [g][|x|]", "yx": "|-19| = 19", "ans": "19 units"},
                    {"num": 2, "part": "A", "prompt": "Find the vertical distance between (-3, -4) and (-3, -15).", "keys": "4 [+/-] [ENTER] 15 [+/-] [-] [g][|x|]", "yx": "|+11| = 11", "ans": "11 units"},
                    {"num": 3, "part": "A", "prompt": "Find the vertical distance between (7, 9) and (7, -6).", "keys": "9 [ENTER] 6 [+/-] [-] [g][|x|]", "yx": "|15| = 15", "ans": "15 units"},
                    {"num": 4, "part": "A", "prompt": "Find the horizontal distance between (-14, 2) and (-5, 2).", "keys": "14 [+/-] [ENTER] 5 [+/-] [-] [g][|x|]", "yx": "|-9| = 9", "ans": "9 units"},
                    {"num": 5, "part": "B", "prompt": "Find the distance between (-3.5, 4) and (6.5, 4).", "keys": "3.5 [+/-] [ENTER] 6.5 [-] [g][|x|]", "yx": "|-10| = 10", "ans": "10 units"},
                    {"num": 6, "part": "B", "prompt": "Find the distance between (2, -4 1/2) and (2, 3 1/2).", "keys": "4.5 [+/-] [ENTER] 3.5 [-] [g][|x|]", "yx": "|-8| = 8", "ans": "8 units"},
                    {"num": 7, "part": "B", "prompt": "A line segment starts at (-6, 3) and goes 10 units right. What are the coordinates of the right endpoint?", "keys": "6 [+/-] [ENTER] 10 [+]", "yx": "Y:-6 | X:10", "ans": "(4, 3)"},
                    {"num": 8, "part": "B", "prompt": "Spot the Glitch: For (-5, 2) to (8, 2), Sam subtracted 8 - 5 = 3. Why is the distance 13, not 3?", "keys": "5 [+/-] [ENTER] 8 [-] [g][|x|]", "yx": "5 to 0 + 8 past 0", "ans": "13 units (They are on opposite sides of the y-axis!)"},
                    {"num": 9, "part": "C", "prompt": "A treasure map rectangle has corners (-4, 6), (5, 6), (5, -2), (-4, -2). Find its perimeter & area 2 ways!", "keys": "Width 9, Height 8", "yx": "Y:9 | X:8", "ans": "Perimeter = 34, Area = 72"},
                    {"num": 10, "part": "C", "prompt": "On a city grid (1 unit = 0.5 mile), you walk from (-6, -2) to (-6, 8) to (4, 8). How many miles did you walk?", "keys": "10 + 10 = 20 units × 0.5", "yx": "Y:20 | X:0.5", "ans": "20 units = 10 miles"}
                ]
            }
        ]
    },

    # =========================================================================
    # CHAPTER 7: EQUATIONS & INEQUALITIES (Sections 7.1 - 7.5)
    # =========================================================================
    {
        "num": 7,
        "title": "Equations & Inequalities",
        "big_ideas_book": "Big Ideas Math Grade 6 — Chapter 7",
        "subtitle": "Writing Equations, Solving One-Step Equations, Writing & Graphing Inequalities, and Two-Variable Relationships",
        "kit_summary": "Algebra Boxes & Stage (ALGB-01) + Number Rack (RACK-01)",
        "hero_png": "algebra_factoring_area.png",
        "coach_misconception": "Students treat '=' as 'write the answer', translate '8 less than n' backwards as 8 - n, resent writing -14 under both sides of x + 14 = 39, and confuse open vs. solid inequality circles.",
        "coach_remediation": "Model '=' as a Balance Scale using Algebra Boxes & Stage (ALGB-01). Solve 1-step equations with inverse operations on both sides and check the answer with [f] [LASTX], and test inequalities with [f] [≥] and [g] [≤].",
        "sections": [
            {
                "day_num": 29,
                "sec_num": "7.1",
                "title": "Writing Equations & Testing Solutions — The Balance Scale Rule",
                "big_ideas_ref": "Big Ideas Grade 6, Section 7.1 (Writing Equations in One Variable)",
                "ccss": "CCSS.MATH.6.EE.B.5",
                "kit_id": "ALGB-01",
                "kit_name": "Algebra Boxes & Stage",
                "asset_png": "algebra_factoring_area.png",
                "diagram_type": "balance_scale",
                "diagram_data": {"left": "3x - 5", "right": "19", "sol": "x = 8", "caption": "Balance Scale: Left Pan (Floor 2 Y) must equal Right Pan (Floor 1 X). At x=8, 3(8)-5 = 19 == 19!"},
                "concept": "In algebra, '=' is the center pivot of a Balance Scale! On your SC-6, Floor 2 (Y) is the Left Pan and Floor 1 (X) is the Right Pan. To test if x = 8 solves 3x - 5 = 19, put 19 on Y, compute 3(8) - 5 on X, and see Y: 19 | X: 19 (or press [g] [≠] -> 0 difference)!",
                "examples": [
                    {
                        "title": "Example 1: Balance Scale Solution Tester",
                        "problem": "Test whether x = 7 or x = 9 is the solution to 4x + 5 = 41.",
                        "block_step": "Park 41 on Y. Test x = 7: 4(7)+5 = 33 (Not 41!). Test x = 9: 4(9)+5 = 41 (Matches Y = 41—Balanced!).",
                        "keys": ["41", "ENTER", "4", "ENTER", "9", "×", "5", "+"],
                        "stack_y": "41 (Right)",
                        "stack_x": "41 (Left at x=9)",
                        "ans": "x = 9 is the solution (41 == 41)",
                        "note": "When Floor 2 (Y) and Floor 1 (X) match, the equation is balanced!"
                    },
                    {
                        "title": "Example 2: Dodging the 'Less Than' Flip Trap",
                        "problem": "Translate '8 less than a number n is 25' into an equation and find n.",
                        "block_step": "'8 less than n' means start with n and take 8 away: n - 8 = 25 (NEVER 8 - n = 25!). Since 33 - 8 = 25, n = 33!",
                        "keys": ["25", "ENTER", "8", "+", "8", "-"],
                        "stack_y": "n = 33",
                        "stack_x": "33 - 8 = 25",
                        "ans": "n - 8 = 25; n = 33",
                        "note": "Always watch out for 'less than' and 'subtracted from'—they reverse the order!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Test whether x = 6 or x = 8 solves 5x - 7 = 33.", "keys": "5 [ENTER] 8 [×] 7 [-]", "yx": "Y:33 | X:33", "ans": "x = 8 (5(8)-7 = 33)"},
                    {"num": 2, "part": "A", "prompt": "Test whether y = 12 or y = 15 solves y / 3 + 4 = 9.", "keys": "15 [ENTER] 3 [÷] 4 [+]", "yx": "Y:9 | X:9", "ans": "y = 15 (15/3 + 4 = 9)"},
                    {"num": 3, "part": "A", "prompt": "Translate into an equation: 'The sum of a number x and 14 is 52.'", "keys": "x + 14 = 52", "yx": "52 - 14 = 38", "ans": "x + 14 = 52 (x = 38)"},
                    {"num": 4, "part": "A", "prompt": "Translate into an equation: '6 times a number k equals 84.'", "keys": "6k = 84", "yx": "84 ÷ 6 = 14", "ans": "6k = 84 (k = 14)"},
                    {"num": 5, "part": "B", "prompt": "Translate: '9 less than a number w is 17.' (Watch the order!)", "keys": "w - 9 = 17", "yx": "17 + 9 = 26", "ans": "w - 9 = 17 (w = 26)"},
                    {"num": 6, "part": "B", "prompt": "Translate: 'The quotient of a number m and 5 is 13.'", "keys": "m / 5 = 13", "yx": "13 × 5 = 65", "ans": "m/5 = 13 (m = 65)"},
                    {"num": 7, "part": "B", "prompt": "4 pizza pies (p) plus a $6 delivery fee total $54. Write the equation and test p = 12!", "keys": "4 [ENTER] 12 [×] 6 [+]", "yx": "Y:54 | X:54", "ans": "4p + 6 = 54; p = $12"},
                    {"num": 8, "part": "B", "prompt": "Spot the Glitch: For '12 less than x is 20', Sam wrote 12 - x = 20. Fix the equation and solve!", "keys": "x - 12 = 20", "yx": "20 + 12 = 32", "ans": "x - 12 = 20 (x = 32)"},
                    {"num": 9, "part": "C", "prompt": "A streaming pass costs $10 plus $3 per movie (10 + 3m = 28). Find m by testing AND by undoing!", "keys": "28 [ENTER] 10 [-] 3 [÷]", "yx": "Y:18 | X:3", "ans": "m = 6 movies (10 + 3(6) = 28)"},
                    {"num": 10, "part": "C", "prompt": "Three friends split a restaurant bill b equally and each pays $14.50. Write the equation and find b!", "keys": "14.50 [ENTER] 3 [×]", "yx": "b/3 = 14.50", "ans": "b/3 = 14.50; b = $43.50"}
                ]
            },
            {
                "day_num": 30,
                "sec_num": "7.2",
                "title": "Solving One-Step Addition & Subtraction Equations ([f] [LASTX])",
                "big_ideas_ref": "Big Ideas Grade 6, Section 7.2 (Solving Equations Using Addition or Subtraction)",
                "ccss": "CCSS.MATH.6.EE.B.7",
                "kit_id": "ALGB-01",
                "kit_name": "Algebra Boxes & Stage",
                "asset_png": "algebra_factoring_area.png",
                "diagram_type": "balance_scale",
                "diagram_data": {"left": "x + 14", "right": "39", "sol": "Remove 14 -> x = 25", "caption": "Sweep 14 cubes off both pans: 39 [ENTER] 14 [-] -> x = 25. Prove with [f] [LASTX] [+] -> 39!"},
                "concept": "Why does x + 14 = 39 become 39 - 14? Because the Subtraction Property of Equality removes 14 cubes from both pans of the balance scale so the x-rod stands alone! And why does x - 18 = 45 become 45 + 18? Because the Addition Property of Equality adds 18 back to both sides! Use [f] [LASTX] and the inverse operation to check!",
                "examples": [
                    {
                        "title": "Example 1: Undoing Addition (x + 28 = 73) + [f] [LASTX] Proof",
                        "problem": "Solve x + 28 = 73 using the Subtraction Property of Equality and check your solution.",
                        "block_step": "Remove 28 from both sides: 73 [ENTER] 28 [-] -> x = 45. Now tap [f] [LASTX] [+] -> 45 + 28 = 73!",
                        "keys": ["73", "ENTER", "28", "-", "f", "LASTX", "+"],
                        "stack_y": "73 (Total)",
                        "stack_x": "28 -> x = 45",
                        "ans": "x = 45 (Proven: 45 + 28 = 73)",
                        "note": "Subtracting 28 from both sides isolates x = 45!"
                    },
                    {
                        "title": "Example 2: Undoing Subtraction with Decimals & Fractions",
                        "problem": "Solve w - 19.6 = 34.8 and m + 3/8 = 5/6.",
                        "block_step": "For w - 19.6 = 34.8, add 19.6 back (34.8 + 19.6 = 54.4). For m + 3/8 = 5/6, subtract 3/8 from 5/6!",
                        "keys": ["34.8", "ENTER", "19.6", "+", ".", "5", ".", "6", "ENTER", ".", "3", ".", "8", "-"],
                        "stack_y": "w = 54.4",
                        "stack_x": "m = 11/24",
                        "ans": "w = 54.4; m = 11/24",
                        "note": "Check m: 11/24 [f] [LASTX] [+] -> 11/24 + 3/8 = 5/6!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Solve x + 28 = 73 and prove with [f] [LASTX] [+].", "keys": "73 [ENTER] 28 [-]", "yx": "Y:73 | X:28", "ans": "x = 45"},
                    {"num": 2, "part": "A", "prompt": "Solve y - 34 = 58 and prove with [f] [LASTX] [-].", "keys": "58 [ENTER] 34 [+]", "yx": "Y:58 | X:34", "ans": "y = 92"},
                    {"num": 3, "part": "A", "prompt": "Solve 19 + n = 64.", "keys": "64 [ENTER] 19 [-]", "yx": "Y:64 | X:19", "ans": "n = 45"},
                    {"num": 4, "part": "A", "prompt": "Solve k - 47 = 29.", "keys": "29 [ENTER] 47 [+]", "yx": "Y:29 | X:47", "ans": "k = 76"},
                    {"num": 5, "part": "B", "prompt": "Solve w - 19.6 = 34.8.", "keys": "34.8 [ENTER] 19.6 [+]", "yx": "Y:34.8 | X:19.6", "ans": "w = 54.4"},
                    {"num": 6, "part": "B", "prompt": "Solve p + 8.75 = 25.4.", "keys": "25.4 [ENTER] 8.75 [-]", "yx": "Y:25.4 | X:8.75", "ans": "p = 16.65"},
                    {"num": 7, "part": "B", "prompt": "Solve m + 3/8 = 5/6 on your SC-6 and check with [f] [LASTX] [+].", "keys": "[.] 5 [.] 6 [ENTER] [.] 3 [.] 8 [-]", "yx": "Y:5/6 | X:3/8", "ans": "m = 11/24"},
                    {"num": 8, "part": "B", "prompt": "Solve a - 1 1/4 = 3 1/2.", "keys": "3 [.] 1 [.] 2 [ENTER] 1 [.] 1 [.] 4 [+]", "yx": "Y:3 1/2 | X:1 1/4", "ans": "a = 4 3/4"},
                    {"num": 9, "part": "C", "prompt": "After spending $18.50 on a controller skin, you have $26.75 left (m - 18.50 = 26.75). Find starting money m!", "keys": "26.75 [ENTER] 18.50 [+]", "yx": "Y:26.75 | X:18.50", "ans": "$45.25 (Check: 45.25 - 18.50 = 26.75)"},
                    {"num": 10, "part": "C", "prompt": "A drone climbs 42.5 ft to reach 110 ft (h + 42.5 = 110). Find its starting height h and prove with [f][LASTX]!", "keys": "110 [ENTER] 42.5 [-]", "yx": "Y:110 | X:42.5", "ans": "67.5 ft (Check: 67.5 + 42.5 = 110)"}
                ]
            },
            {
                "day_num": 31,
                "sec_num": "7.3",
                "title": "Solving One-Step Multiplication & Division Equations",
                "big_ideas_ref": "Big Ideas Grade 6, Section 7.3 (Solving Equations Using Multiplication or Division)",
                "ccss": "CCSS.MATH.6.EE.B.7",
                "kit_id": "ALGB-01",
                "kit_name": "Algebra & Fraction Studio",
                "asset_png": "algebra_factoring_area.png",
                "diagram_type": "balance_scale",
                "diagram_data": {"left": "6x (6 rods)", "right": "84 cubes", "sol": "84 ÷ 6 -> x = 14", "caption": "6 identical x-rods weigh 84 cubes: split 84 into 6 equal piles (84 ÷ 6 = 14 cubes per rod)!"},
                "concept": "When 6 identical x-rods balance 84 cubes (6x = 84), divide 84 into 6 equal piles (84 [ENTER] 6 [÷] -> 14)! When a variable is divided (k/7 = 14.5), multiply by 7 to put the 7 parts back together! And for a fraction coefficient like 2/5n = 16, either divide by 2/5 OR flip with [f] [1/x] and multiply!",
                "examples": [
                    {
                        "title": "Example 1: Undoing Multiplication & Division",
                        "problem": "Solve 8x = 136 and k / 7 = 14.5, and prove each with [f] [LASTX].",
                        "block_step": "For 8x = 136: 136 [ENTER] 8 [÷] -> 17 (Check: [f] [LASTX] [×] -> 136). For k/7 = 14.5: 14.5 [ENTER] 7 [×] -> 101.5.",
                        "keys": ["136", "ENTER", "8", "÷", "14.5", "ENTER", "7", "×"],
                        "stack_y": "x = 17",
                        "stack_x": "k = 101.5",
                        "ans": "x = 17; k = 101.5",
                        "note": "Division undoes multiplication; multiplication undoes division!"
                    },
                    {
                        "title": "Example 2: Fraction Coefficient Both Ways (2/5 n = 16)",
                        "problem": "Solve 2/5 n = 16 using BOTH division ([÷]) and reciprocal multiplication ([f] [1/x] [×]).",
                        "block_step": "Way A: 16 [ENTER] [.] 2 [.] 5 [÷] -> 40. Way B: 16 [ENTER] [.] 2 [.] 5 [f] [1/x] (flips to 5/2) [×] -> 40!",
                        "keys": ["16", "ENTER", ".", "2", ".", "5", "f", "1/x", "×"],
                        "stack_y": "16",
                        "stack_x": "5/2 -> 40",
                        "ans": "n = 40",
                        "note": "Both ways prove 2/5 of 40 is 16!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Solve 8x = 136 and prove with [f] [LASTX] [×].", "keys": "136 [ENTER] 8 [÷]", "yx": "Y:136 | X:8", "ans": "x = 17"},
                    {"num": 2, "part": "A", "prompt": "Solve 12y = 180 and prove with [f] [LASTX] [×].", "keys": "180 [ENTER] 12 [÷]", "yx": "Y:180 | X:12", "ans": "y = 15"},
                    {"num": 3, "part": "A", "prompt": "Solve m / 6 = 19 and prove with [f] [LASTX] [÷].", "keys": "19 [ENTER] 6 [×]", "yx": "Y:19 | X:6", "ans": "m = 114"},
                    {"num": 4, "part": "A", "prompt": "Solve k / 7 = 14.5.", "keys": "14.5 [ENTER] 7 [×]", "yx": "Y:14.5 | X:7", "ans": "k = 101.5"},
                    {"num": 5, "part": "B", "prompt": "Solve 4.5w = 63.", "keys": "63 [ENTER] 4.5 [÷]", "yx": "Y:63 | X:4.5", "ans": "w = 14"},
                    {"num": 6, "part": "B", "prompt": "Solve 3/4 x = 18.", "keys": "18 [ENTER] [.] 3 [.] 4 [÷]", "yx": "Y:18 | X:3/4", "ans": "x = 24"},
                    {"num": 7, "part": "B", "prompt": "Solve 2/5 n = 16 using BOTH [÷] and [f] [1/x] [×].", "keys": "16 [ENTER] [.] 2 [.] 5 [÷]", "yx": "Y:16 | X:2/5", "ans": "n = 40"},
                    {"num": 8, "part": "B", "prompt": "Solve 5/6 p = 2/3.", "keys": "[.] 2 [.] 3 [ENTER] [.] 5 [.] 6 [÷]", "yx": "Y:2/3 | X:5/6", "ans": "p = 4/5 (0.8)"},
                    {"num": 9, "part": "C", "prompt": "A 3D printer prints at 1.5 cm/min. How long (t) to print a 27 cm tower (1.5t = 27)? Solve & prove!", "keys": "27 [ENTER] 1.5 [÷]", "yx": "Y:27 | X:1.5", "ans": "18 minutes (Check: 18 × 1.5 = 27)"},
                    {"num": 10, "part": "C", "prompt": "3/5 of the students in a club (3/5 s = 27) are 6th graders. How many total students s are in the club?", "keys": "27 [ENTER] [.] 3 [.] 5 [÷]", "yx": "Y:27 | X:3/5", "ans": "45 students (Way 2: 27 ÷ 3 × 5 = 45)"}
                ]
            },
            {
                "day_num": 32,
                "sec_num": "7.4",
                "title": "Writing, Graphing & Solving Inequalities ([f] [>], [g] [<], [f] [≥], [g] [≤])",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 7.5–7.7 (Writing, Graphing, and Solving Inequalities)",
                "ccss": "CCSS.MATH.6.EE.B.8",
                "kit_id": "RACK-01",
                "kit_name": "Number Rack & Number Line",
                "asset_png": "number_rack_subitizing.png",
                "diagram_type": "zero_pairs",
                "diagram_data": {"pos": 7, "neg": 0, "net": 7, "caption": "Inequality Graph: '>' or '<' = Open Circle (o); '≥' or '≤' = Solid Dot (•). Test with [f][≥] & [g][≤] (1=True, 0=False)!"},
                "concept": "Inequalities have infinitely many solutions! On a number line: '>' and '<' use an OPEN circle (o) because the boundary number is not included; '≥' (at least) and '≤' (at most) use a SOLID dot (•) because the boundary IS included! Solve just like one-step equations, then test boundary numbers with [f] [≥] ([f][+]) and [g] [≤] ([g][+])!",
                "examples": [
                    {
                        "title": "Example 1: Solving & Graphing x - 7 ≥ 12",
                        "problem": "Solve x - 7 ≥ 12, state whether the circle at 19 is Open or Solid, and test x = 20.",
                        "block_step": "Add 7 to both sides: 12 [ENTER] 7 [+] -> x ≥ 19. Because it is '≥', put a SOLID dot (•) at 19 and shade RIGHT!",
                        "keys": ["12", "ENTER", "7", "+", "20", "x⇄y", "f", "≥"],
                        "stack_y": "20 (Test)",
                        "stack_x": "19 -> 1 (True)",
                        "ans": "x ≥ 19 (Solid dot at 19, arrow Right)",
                        "note": "Testing 20 ≥ 19 with [f] [≥] outputs 1 (TRUE)!"
                    },
                    {
                        "title": "Example 2: Backpack Weight Limit (3g + 15 ≤ 60)",
                        "problem": "You carry a 15-lb shield plus gold bars weighing 3 lb each (3g + 15 ≤ 60). Find the max bars g.",
                        "block_step": "Subtract the 15-lb shield first (60 - 15 = 45), then divide by 3 lb per bar (45 ÷ 3 = 15) -> g ≤ 15!",
                        "keys": ["60", "ENTER", "15", "-", "3", "÷"],
                        "stack_y": "45 (Left)",
                        "stack_x": "3 -> 15",
                        "ans": "g ≤ 15 (At most 15 gold bars)",
                        "note": "Test g=15: 3(15)+15 = 60 ≤ 60 (1 = TRUE)!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Solve x + 8 > 21. Tell whether the circle at 13 is Open or Solid, and arrow direction.", "keys": "21 [ENTER] 8 [-]", "yx": "Y:21 | X:8", "ans": "x > 13 (Open circle, arrow Right)"},
                    {"num": 2, "part": "A", "prompt": "Solve y - 9 ≤ 15. Tell whether the circle at 24 is Open or Solid, and arrow direction.", "keys": "15 [ENTER] 9 [+]", "yx": "Y:15 | X:9", "ans": "y ≤ 24 (Solid dot, arrow Left)"},
                    {"num": 3, "part": "A", "prompt": "Solve 6n ≥ 78. Tell whether the circle at 13 is Open or Solid, and arrow direction.", "keys": "78 [ENTER] 6 [÷]", "yx": "Y:78 | X:6", "ans": "n ≥ 13 (Solid dot, arrow Right)"},
                    {"num": 4, "part": "A", "prompt": "Solve m / 4 < 9. Tell whether the circle at 36 is Open or Solid, and arrow direction.", "keys": "9 [ENTER] 4 [×]", "yx": "Y:9 | X:4", "ans": "m < 36 (Open circle, arrow Left)"},
                    {"num": 5, "part": "B", "prompt": "Translate: 'You must be at least 48 inches tall (h) to ride.' Write the inequality!", "keys": "'At least' = ≥", "yx": "Solid dot at 48", "ans": "h ≥ 48"},
                    {"num": 6, "part": "B", "prompt": "Translate: 'An elevator holds at most 2,000 pounds (w).' Write the inequality!", "keys": "'At most' = ≤", "yx": "Solid dot at 2000", "ans": "w ≤ 2000"},
                    {"num": 7, "part": "B", "prompt": "Which numbers from {4, 5, 6} are solutions to 4n + 3 > 23? Test on your SC-6!", "keys": "4(5)+3=23 (False); 4(6)+3=27 (True)", "yx": "n > 5", "ans": "Only 6 (At n=5, 23 > 23 is False!)"},
                    {"num": 8, "part": "B", "prompt": "Which numbers from {4, 5, 6} are solutions to 4x - 3 ≥ 17?", "keys": "4(5)-3=17 ≥ 17 (1=True)", "yx": "x ≥ 5", "ans": "5 and 6"},
                    {"num": 9, "part": "C", "prompt": "You have $50 to buy $8 books (8b ≤ 50). Solve with [g] [÷R] to find the max whole books b you can buy!", "keys": "50 [ENTER] 8 [g][÷R]", "yx": "Y:2 | X:6", "ans": "At most 6 books ($2 left over)"},
                    {"num": 10, "part": "C", "prompt": "A gamer needs at least 500 points (p + 340 ≥ 500). Solve for p AND test p = 160 with [f] [≥]!", "keys": "500 [ENTER] 340 [-]", "yx": "Y:500 | X:340", "ans": "p ≥ 160 (340+160=500 ≥ 500 -> True!)"}
                ]
            },
            {
                "day_num": 33,
                "sec_num": "7.5",
                "title": "Two-Variable Relationships (y = kx and y = x + b) — Tables & Graphs",
                "big_ideas_ref": "Big Ideas Grade 6, Section 7.4 (Writing Equations in Two Variables)",
                "ccss": "CCSS.MATH.6.EE.C.9",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Array Tiles",
                "asset_png": "counting_tiles_array_3x8.png",
                "diagram_type": "coord_plane",
                "diagram_data": {"pts": [("(1,6)", 1, 6), ("(2,12)", 2, 12), ("(3,18)", 3, 18)], "caption": "Multiplicative Rule y = 6x passes through (0,0); Additive Rule y = x + 6 starts at (0,6)!"},
                "concept": "How do you tell if a table of (x, y) points is an ADDITION rule (y = x + b) or a MULTIPLICATION rule (y = kx)? Check y - x (if constant, it's y = x + b) and check y ÷ x (if constant, it's y = kx)! Remember: x is the Independent variable (input you choose) and y is the Dependent variable (output that depends on x).",
                "examples": [
                    {
                        "title": "Example 1: The 2-Second Rule Detector (y = kx vs. y = x + b)",
                        "problem": "Table A has (2, 14), (5, 35), (8, 56). Table B has (10, 6), (15, 11), (22, 18). Find both equations.",
                        "block_step": "Table A: 14÷2 = 7, 35÷5 = 7, 56÷8 = 7 -> Multiplicative y = 7x! Table B: 10 - 4 = 6, 15 - 4 = 11 -> Additive y = x - 4!",
                        "keys": ["14", "ENTER", "2", "÷", "35", "ENTER", "5", "÷"],
                        "stack_y": "7 (14÷2)",
                        "stack_x": "7 (35÷5)",
                        "ans": "Table A: y = 7x; Table B: y = x - 4",
                        "note": "Once you know y = 7x, find y at x = 12 with 7 [ENTER] 12 [×] = 84!"
                    },
                    {
                        "title": "Example 2: Independent vs. Dependent Variables (p = 12.50h)",
                        "problem": "You earn $12.50 per hour (h) mowing lawns, for total pay p = 12.50h. Find p for 6.5 hours.",
                        "block_step": "Hours h is Independent (input); Pay p is Dependent (depends on h). Multiply 12.50 × 6.5!",
                        "keys": ["12.50", "ENTER", "6.5", "×"],
                        "stack_y": "12.50 (Rate)",
                        "stack_x": "6.5 (Hours)",
                        "ans": "p = $81.25 (h = Independent, p = Dependent)",
                        "note": "To find hours h for $100 pay, divide: 100 [ENTER] 12.50 [÷] = 8 hours!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Table has (1, 8), (2, 16), (3, 24). Write the equation and find y when x = 10.", "keys": "16 [ENTER] 2 [÷] -> 8; 8×10", "yx": "y = 8x", "ans": "y = 8x; y = 80"},
                    {"num": 2, "part": "A", "prompt": "Table has (1, 9), (2, 10), (5, 13). Write the equation and find y when x = 20.", "keys": "9 [ENTER] 1 [-] -> +8; 20+8", "yx": "y = x + 8", "ans": "y = x + 8; y = 28"},
                    {"num": 3, "part": "A", "prompt": "Table has (2, 14), (5, 35), (8, 56). Write the equation and find y when x = 12.", "keys": "14 [ENTER] 2 [÷] -> 7; 7×12", "yx": "y = 7x", "ans": "y = 7x; y = 84"},
                    {"num": 4, "part": "A", "prompt": "Table has (10, 6), (15, 11), (22, 18). Write the equation and find y when x = 30.", "keys": "30 [ENTER] 4 [-]", "yx": "y = x - 4", "ans": "y = x - 4; y = 26"},
                    {"num": 5, "part": "B", "prompt": "Use 6 [g] [REP] [+] to generate the y-values of y = 6x for x = 1, 2, 3, 4.", "keys": "6 [g][REP] [+] [+] [+]", "yx": "6, 12, 18, 24", "ans": "(1,6), (2,12), (3,18), (4,24)"},
                    {"num": 6, "part": "B", "prompt": "In d = 65t (distance d in miles after t hours), which variable is Independent and which is Dependent?", "keys": "d depends on t", "yx": "Input t -> Output d", "ans": "Independent: t; Dependent: d"},
                    {"num": 7, "part": "B", "prompt": "Using d = 65t, how far does the car travel in 4.5 hours?", "keys": "65 [ENTER] 4.5 [×]", "yx": "Y:65 | X:4.5", "ans": "292.5 miles"},
                    {"num": 8, "part": "B", "prompt": "Does the graph of y = 4x pass through the origin (0, 0)? What about y = x + 4?", "keys": "Test x = 0 in both!", "yx": "4(0)=0 vs 0+4=4", "ans": "y = 4x hits (0,0); y = x + 4 hits (0,4)"},
                    {"num": 9, "part": "C", "prompt": "You earn p = 12.50h. How many hours h must you work to earn $100? Solve by division AND ratio doubling!", "keys": "100 [ENTER] 12.50 [÷]", "yx": "Y:100 | X:12.50", "ans": "8 hours (Way 2: 1h=12.5 -> 2h=25 -> 4h=50 -> 8h=100)"},
                    {"num": 10, "part": "C", "prompt": "A gym charges a $25 signup fee plus $15 per month (m). Write the equation for total cost c and find c for 12 months!", "keys": "15 [ENTER] 12 [×] 25 [+]", "yx": "Y:180 | X:25", "ans": "c = 15m + 25; $205 for 12 months"}
                ]
            }
        ]
    },

    # =========================================================================
    # CHAPTER 8: SURFACE AREA & VOLUME OF 3D SOLIDS (Sections 8.1 - 8.4)
    # =========================================================================
    {
        "num": 8,
        "title": "Surface Area & Volume of 3D Solids",
        "big_ideas_book": "Big Ideas Math Grade 6 — Chapter 8",
        "subtitle": "Surface Area of Rectangular & Triangular Prisms, Pyramids, Volume of Prisms, and Circles/Cones/Hypotenuse",
        "kit_summary": "Counting & Array Tiles (COUNT-01) + Gridfinity 3x1 Storage Boxes",
        "hero_png": "counting_tiles_box_3x1x13u.png",
        "coach_misconception": "Students drop one of the 6 faces when finding rectangular prism surface area, tangle prism and pyramid formulas, and confuse 2D Surface Area (cardboard outside) with 3D Volume (cubes inside).",
        "coach_remediation": "Have students touch the 3 pairs of faces on their physical Gridfinity box while logging each pair into [Σ+] (n=1, 2, 3), use [f] [PRISM] ([f][9]) to multiply 3 stack floors (l, w, h) at once for volume, and unlock [f] [CIRC], [g] [CONE], and [g] [HYP].",
        "sections": [
            {
                "day_num": 34,
                "sec_num": "8.1",
                "title": "3D Solids, Nets & Surface Area of Rectangular Prisms ([f] [RECT] + [Σ+])",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 8.1 & 8.2 (Three-Dimensional Figures and Surface Area of Prisms)",
                "ccss": "CCSS.MATH.6.G.A.4",
                "kit_id": "COUNT-01",
                "kit_name": "3x1 Gridfinity Box & Tiles",
                "asset_png": "counting_tiles_box_3x1x13u.png",
                "diagram_type": "solid_3d",
                "diagram_data": {"mode": "net", "l": 8, "w": 5, "h": 3, "caption": "Unfolded 6-Face Box Net: Pair 1 Top/Bot (2×8×5=80) + Pair 2 Front/Back (2×8×3=48) + Pair 3 Left/Right (2×5×3=30) = 158!"},
                "concept": "Finding the surface area of a 6-sided box on paper is a magnet for mistakes because kids forget to double one of the 3 face pairs! Touch your physical Gridfinity box: clear memory ([g] [CLΣ]), compute each pair of opposite walls with l [ENTER] w [f] [RECT] 2 [×] [Σ+] (watch n=1, n=2, n=3!), and read the total with [f] [Σx]!",
                "examples": [
                    {
                        "title": "Example 1: The 3-Pair Box Ledger ([f] [RECT] 2 [×] [Σ+])",
                        "problem": "Find the surface area of a rectangular prism measuring 8 cm by 5 cm by 3 cm.",
                        "block_step": "Clear ([g] [CLΣ]). Top/Bot: 8×5×2 = 80 [Σ+] (n=1). Front/Back: 8×3×2 = 48 [Σ+] (n=2). Left/Right: 5×3×2 = 30 [Σ+] (n=3). Tap [f] [Σx]!",
                        "keys": ["g", "CLΣ", "8", "ENTER", "5", "f", "RECT", "2", "×", "Σ+", "8", "ENTER", "3", "f", "RECT", "2", "×", "Σ+", "5", "ENTER", "3", "f", "RECT", "2", "×", "Σ+", "f", "Σx"],
                        "stack_y": "80 + 48 + 30",
                        "stack_x": "158 cm²",
                        "ans": "158 cm²",
                        "note": "Seeing n = 3 guarantees you logged all 3 pairs of faces (6 faces total)!"
                    },
                    {
                        "title": "Example 2: Cube Shortcut (SA = 6s²) & Open-Top Bin",
                        "problem": "Find the surface area of a cube with side s = 7 in, and an open-top 10×8×5 cm bin.",
                        "block_step": "For a 7-in cube, all 6 faces are 7² = 49 -> 6 × 49 = 294 in². For an open-top 10×8×5 bin, subtract the missing 10×8 lid (80) from the 6-wall total (340) -> 260 cm²!",
                        "keys": ["7", "x²", "6", "×"],
                        "stack_y": "49 (1 face)",
                        "stack_x": "6 -> 294 in²",
                        "ans": "Cube = 294 in²; Open-Top Bin = 260 cm²",
                        "note": "An open-top bin has only 1 bottom (10×8=80) + 4 side walls (180) = 260!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the surface area of a cube with edge length s = 4 cm (6s²).", "keys": "4 [x²] 6 [×]", "yx": "Y:16 | X:6", "ans": "96 cm²"},
                    {"num": 2, "part": "A", "prompt": "Find the surface area of a cube with edge length s = 9 in.", "keys": "9 [x²] 6 [×]", "yx": "Y:81 | X:6", "ans": "486 in²"},
                    {"num": 3, "part": "A", "prompt": "Find the surface area of a 6 cm by 4 cm by 3 cm rectangular prism using the 3-pair [Σ+] ledger.", "keys": "2(24)+2(18)+2(12)", "yx": "48 + 36 + 24", "ans": "108 cm²"},
                    {"num": 4, "part": "A", "prompt": "Find the surface area of a 10 in by 5 in by 2 in rectangular box.", "keys": "2(50)+2(20)+2(10)", "yx": "100 + 40 + 20", "ans": "160 in²"},
                    {"num": 5, "part": "B", "prompt": "Find the surface area of a prism with l = 12 ft, w = 8 ft, and h = 5 ft.", "keys": "2(96)+2(60)+2(40)", "yx": "192 + 120 + 80", "ans": "392 ft²"},
                    {"num": 6, "part": "B", "prompt": "Find the surface area of a prism with decimal edges: 5 m by 4 m by 2.5 m.", "keys": "2(20)+2(12.5)+2(10)", "yx": "40 + 25 + 20", "ans": "85 m²"},
                    {"num": 7, "part": "B", "prompt": "A cube has a total surface area of 150 cm². What is the area of 1 face, and what is the edge length s?", "keys": "150 [ENTER] 6 [÷] [f][√x]", "yx": "25 -> s = 5", "ans": "1 face = 25 cm²; s = 5 cm"},
                    {"num": 8, "part": "B", "prompt": "Spot the Glitch: For a 5×4×3 box, Leo added 20 + 15 + 12 = 47. What did he forget to do?", "keys": "47 [ENTER] 2 [×]", "yx": "Y:47 | X:2", "ans": "94 (He only found 3 faces; must double for 6 faces!)"},
                    {"num": 9, "part": "C", "prompt": "An open-top 3D-printed bin is 10 cm long, 8 cm wide, and 5 cm tall (NO lid!). Find its outer surface area 2 ways!", "keys": "80 + 2(50) + 2(40)", "yx": "80 + 100 + 80", "ans": "260 cm² (Way 2: Full box 340 - 80 lid = 260)"},
                    {"num": 10, "part": "C", "prompt": "You wrap a gift box (15 in × 10 in × 4 in). If you have 550 in² of wrapping paper, is it enough?", "keys": "2(150)+2(60)+2(40)", "yx": "300 + 120 + 80", "ans": "500 in² needed -> Yes, 50 in² to spare!"}
                ]
            },
            {
                "day_num": 35,
                "sec_num": "8.2",
                "title": "Surface Area of Triangular Prisms & Pyramids ([f] [RECT] + [g] [TRI] + [Σ+])",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 8.2 & 8.3 (Surface Area of Triangular Prisms and Pyramids)",
                "ccss": "CCSS.MATH.6.G.A.4",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Array Tiles",
                "asset_png": "counting_tiles_distributive_4color.png",
                "diagram_type": "polygon_area",
                "diagram_data": {"shape": "composite", "rect_b": 10, "rect_h": 10, "tri_b": 10, "tri_h": 12, "caption": "Square Pyramid Net = 1 Square Base (10² = 100, [Σ+]) + 4 Triangle Sides (4 × ½×10×12 = 240, [Σ+]) = 340!"},
                "concept": "Never memorize complicated formulas for triangular prisms or pyramids! Just look at the flat shapes in the unfolded net: use [f] [RECT] for rectangular walls and [g] [TRI] for triangular faces, tossing each piece into [Σ+] and reading the sum with [f] [Σx]!",
                "examples": [
                    {
                        "title": "Example 1: Square Pyramid Tent (1 Square + 4 Triangles)",
                        "problem": "Find the surface area of a square pyramid with a 10 m × 10 m base and 4 triangles (b = 10 m, slant height = 12 m).",
                        "block_step": "Clear ([g] [CLΣ]). Square Base: 10 [x²] [Σ+] (100). 4 Triangles: 10 [ENTER] 12 [g] [TRI] 4 [×] [Σ+] (240). Read [f] [Σx] -> 340 m²!",
                        "keys": ["g", "CLΣ", "10", "x²", "Σ+", "10", "ENTER", "12", "g", "TRI", "4", "×", "Σ+", "f", "Σx"],
                        "stack_y": "100 (Base)",
                        "stack_x": "240 (4 Tris) -> 340",
                        "ans": "340 m²",
                        "note": "1 Square Base (100) + 4 Identical Triangles (4 × 60 = 240) = 340 m²!"
                    },
                    {
                        "title": "Example 2: Triangular Prism Ramp (2 Triangle Ends + 3 Rectangles)",
                        "problem": "A ramp has 2 right-triangle ends (b=6 ft, h=8 ft) and 3 rectangular sides of length 10 ft (widths 6, 8, 10 ft).",
                        "block_step": "2 Triangle Ends: 6 [ENTER] 8 [g] [TRI] 2 [×] [Σ+] (48). 3 Rectangular Sides: (6+8+10)×10 = 240 [Σ+]. Total = 288 ft²!",
                        "keys": ["6", "ENTER", "8", "g", "TRI", "2", "×", "6", "ENTER", "8", "+", "10", "+", "10", "f", "RECT", "+"],
                        "stack_y": "48 (2 Ends)",
                        "stack_x": "240 (3 Sides) -> 288",
                        "ans": "288 ft²",
                        "note": "Pro Shortcut: The 3 rectangles wrap around the perimeter (6+8+10 = 24) × length 10 = 240!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Square Pyramid: Base is 6 cm × 6 cm; 4 triangles each have b = 6 cm, slant height = 5 cm. Find SA.", "keys": "6 [x²] 6 [ENTER] 5 [g][TRI] 4 [×] [+]", "yx": "Y:36 | X:60", "ans": "96 cm²"},
                    {"num": 2, "part": "A", "prompt": "Square Pyramid: Base is 8 in × 8 in; 4 triangles each have b = 8 in, slant height = 10 in. Find SA.", "keys": "8 [x²] 8 [ENTER] 10 [g][TRI] 4 [×] [+]", "yx": "Y:64 | X:160", "ans": "224 in²"},
                    {"num": 3, "part": "A", "prompt": "Square Pyramid: Base is 12 ft × 12 ft; 4 triangles each have b = 12 ft, slant height = 9 ft. Find SA.", "keys": "12 [x²] 12 [ENTER] 9 [g][TRI] 4 [×] [+]", "yx": "Y:144 | X:216", "ans": "360 ft²"},
                    {"num": 4, "part": "A", "prompt": "Regular Tetrahedron: Made of 4 identical equilateral triangles (b = 6 cm, h = 5.2 cm). Find total SA.", "keys": "6 [ENTER] 5.2 [g][TRI] 4 [×]", "yx": "Y:15.6 | X:4", "ans": "62.4 cm²"},
                    {"num": 5, "part": "B", "prompt": "Triangular Prism: 2 triangle ends (b=4, h=3) + 3 rectangles of length 10 (widths 3, 4, 5). Find SA.", "keys": "4 [ENTER] 3 [g][TRI] 2 [×] (12) + 12×10 (120)", "yx": "Y:12 | X:120", "ans": "132"},
                    {"num": 6, "part": "B", "prompt": "Triangular Prism Tent: 2 triangle ends (b=8 ft, h=3 ft) + 3 rectangles of length 7 ft (widths 5, 5, 8 ft).", "keys": "8 [ENTER] 3 [g][TRI] 2 [×] (24) + 18×7 (126)", "yx": "Y:24 | X:126", "ans": "150 ft²"},
                    {"num": 7, "part": "B", "prompt": "A regular tetrahedron has 4 identical triangles with b = 8 cm and h = 6.93 cm. Find its surface area.", "keys": "8 [ENTER] 6.93 [g][TRI] 4 [×]", "yx": "Y:27.72 | X:4", "ans": "110.88 cm²"},
                    {"num": 8, "part": "B", "prompt": "How many faces (triangles and rectangles) does a Triangular Prism have vs. a Square Pyramid?", "keys": "Count net faces", "yx": "Prism:5 | Pyr:5", "ans": "Prism: 2 tris + 3 rects; Pyramid: 1 sq + 4 tris"},
                    {"num": 9, "part": "C", "prompt": "Camping Tent (Triangular Prism): 2 ends (b=6 ft, h=4 ft), floor (6×8 ft), and 2 roof sides (5×8 ft each). Find total fabric 2 ways!", "keys": "24 + 48 + 80", "yx": "24 + 128", "ans": "152 ft² (Way 2: 24 + (6+5+5)×8 = 152)"},
                    {"num": 10, "part": "C", "prompt": "A glass pyramid skylight has NO bottom floor—only 4 triangular glass panes (b = 9 ft, slant h = 6 ft). Find glass area!", "keys": "9 [ENTER] 6 [g][TRI] 4 [×]", "yx": "Y:27 | X:4", "ans": "108 ft² (Way 2: 27 + 27 + 27 + 27 = 108)"}
                ]
            },
            {
                "day_num": 36,
                "sec_num": "8.3",
                "title": "Volume of Rectangular Prisms with Whole & Fractional Edges ([f] [PRISM])",
                "big_ideas_ref": "Big Ideas Grade 6, Section 8.4 (Volume of Rectangular Prisms)",
                "ccss": "CCSS.MATH.6.G.A.2",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Fraction Studio",
                "asset_png": "counting_tiles_box_3x1x13u.png",
                "diagram_type": "solid_3d",
                "diagram_data": {"mode": "prism", "l": 12, "w": 8, "h": 5, "caption": "3D Volume via [f] [PRISM]: Push Length (Z: 12), Width (Y: 8), Height (X: 5) and press [f] [PRISM] -> 480 in³!"},
                "concept": "Surface Area is the flat cardboard on the outside; Volume is how many 3D unit cubes fit inside! On key 9 of your SC-6, [f] [PRISM] ([f][9]) takes Length (l) on Floor 3 (Z), Width (w) on Floor 2 (Y), and Height (h) on Floor 1 (X) and multiplies all three dimensions in a single click!",
                "examples": [
                    {
                        "title": "Example 1: 1-Click 3-Floor Volume with [f] [PRISM]",
                        "problem": "Find the volume of a shipping crate measuring 12 in × 8 in × 5 in, and an aquarium 3 1/2 ft × 1 1/2 ft × 2 ft.",
                        "block_step": "Push l [ENTER] w [ENTER] h onto Z, Y, X and press [f] [PRISM] ([f][9])!",
                        "keys": ["12", "ENTER", "8", "ENTER", "5", "f", "PRISM"],
                        "stack_y": "Z:12 | Y:8",
                        "stack_x": "X:5 -> 480",
                        "ans": "Crate = 480 in³; Aquarium = 10 1/2 ft³",
                        "note": "For the aquarium: 3.5 [ENTER] 1.5 [ENTER] 2 [f] [PRISM] = 10.5 ft³!"
                    },
                    {
                        "title": "Example 2: Finding Missing Depth from Volume (V = B × h)",
                        "problem": "A planter has Base Area B = 45 in² (9 in × 5 in) and holds 360 in³ of soil. How deep (h) is the soil?",
                        "block_step": "Since Volume = Base Area × Height (V = B × h), divide Volume by Base Area: 360 ÷ 45 = 8 in!",
                        "keys": ["360", "ENTER", "45", "÷"],
                        "stack_y": "360 (Vol)",
                        "stack_x": "45 (Base) -> 8",
                        "ans": "h = 8 in",
                        "note": "Verify: 9 [ENTER] 5 [ENTER] 8 [f] [PRISM] -> 360 in³!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Use [f] [PRISM] to find the volume of a box measuring 10 cm by 6 cm by 4 cm.", "keys": "10 [ENTER] 6 [ENTER] 4 [f][PRISM]", "yx": "Z:10|Y:6|X:4", "ans": "240 cm³"},
                    {"num": 2, "part": "A", "prompt": "Find the volume of a cube with edge length 5 in using [g] [x³] or [f] [PRISM].", "keys": "5 [g][x³]", "yx": "5×5×5", "ans": "125 in³"},
                    {"num": 3, "part": "A", "prompt": "Find the volume of a crate measuring 15 ft by 8 ft by 6 ft.", "keys": "15 [ENTER] 8 [ENTER] 6 [f][PRISM]", "yx": "Z:15|Y:8|X:6", "ans": "720 ft³"},
                    {"num": 4, "part": "A", "prompt": "A prism has Base Area B = 32 m² and height h = 7 m. Find its volume.", "keys": "32 [ENTER] 7 [×]", "yx": "Y:32 | X:7", "ans": "224 m³"},
                    {"num": 5, "part": "B", "prompt": "Fractional Edges: Find the volume of a fish tank 3 1/2 ft long, 1 1/2 ft wide, and 2 ft tall.", "keys": "3.5 [ENTER] 1.5 [ENTER] 2 [f][PRISM]", "yx": "Z:3.5|Y:1.5|X:2", "ans": "10 1/2 ft³ (10.5)"},
                    {"num": 6, "part": "B", "prompt": "Fractional Edges: Find the volume of a block 4 1/2 in by 3 in by 2 in.", "keys": "4.5 [ENTER] 3 [ENTER] 2 [f][PRISM]", "yx": "Z:4.5|Y:3|X:2", "ans": "27 in³"},
                    {"num": 7, "part": "B", "prompt": "Missing Height: A box has Volume = 270 in³, length = 9 in, and width = 5 in. Find height h.", "keys": "270 [ENTER] 9 [ENTER] 5 [×] [÷]", "yx": "Y:270 | X:45", "ans": "6 in"},
                    {"num": 8, "part": "B", "prompt": "How many 1/2-inch mini-cubes fit inside 1 cubic inch? (Compute 2³!)", "keys": "2 [g][x³]", "yx": "2 × 2 × 2", "ans": "8 mini-cubes per 1 in³"},
                    {"num": 9, "part": "C", "prompt": "A planter has Base Area 45 in² (9×5) and Volume 360 in³. Find depth h by division AND verify with [f] [PRISM]!", "keys": "360 [ENTER] 45 [÷]", "yx": "Y:360 | X:45", "ans": "8 in (Check: 9 [ENTER] 5 [ENTER] 8 [f][PRISM]=360)"},
                    {"num": 10, "part": "C", "prompt": "How many 1/2-inch cubes fit inside a box with volume 27 in³? (Multiply 27 by 2³ = 8!)", "keys": "27 [ENTER] 2 [g][x³] [×]", "yx": "Y:27 | X:8", "ans": "216 half-inch cubes"}
                ]
            },
            {
                "day_num": 37,
                "sec_num": "8.4",
                "title": "Circles, Cones & Right-Triangle Hypotenuse ([π], [f] [CIRC], [g] [CONE], [g] [HYP])",
                "big_ideas_ref": "Big Ideas Grade 6/7 Geometry Bridge (Circles, Cones & Right Triangles)",
                "ccss": "CCSS.MATH.7.G.B.4",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Array Tiles",
                "asset_png": "unit_circle_volvelle_30deg.png",
                "diagram_type": "polygon_area",
                "diagram_data": {"shape": "triangle", "b": 4, "h": 3, "area": 6, "caption": "3-4-5 Right Triangle (3²+4²=5² -> [g][HYP]=5) + 1-Click Circle Area ([f][CIRC]=πr²) & Cone Volume ([g][CONE])!"},
                "concept": "Look at keys 8 and 9 on your SC-6: they hold 1-click geometry superpowers! For a circle of radius r, press r [f] [CIRC] ([f][8]) to compute πr² instantly. For a right triangle with legs a and b, press a [ENTER] b [g] [HYP] ([g][8]) for √(a²+b²). For a cone with radius r and height h, press r [ENTER] h [g] [CONE] ([g][9]) for ⅓πr²h!",
                "examples": [
                    {
                        "title": "Example 1: Circle Area ([f] [CIRC]) & 3-4-5 Hypotenuse ([g] [HYP])",
                        "problem": "Find the area of a pizza with radius r = 6 in, and the diagonal of a 12 ft by 5 ft ramp.",
                        "block_step": "For r = 6: press 6 [f] [CIRC] -> 113.10 in². For legs 12 and 5: press 12 [ENTER] 5 [g] [HYP] -> 13 ft!",
                        "keys": ["6", "f", "CIRC", "12", "ENTER", "5", "g", "HYP"],
                        "stack_y": "113.10 (Area)",
                        "stack_x": "13 (Hypot)",
                        "ans": "Pizza = 113.10 in²; Ramp diagonal = 13 ft",
                        "note": "Check 6 [f] [CIRC] against 6 [x²] [π] [×] -> identical 113.097!"
                    },
                    {
                        "title": "Example 2: Cone Volume ([g] [CONE] vs. Cylinder ÷ 3)",
                        "problem": "An ice cream cone has radius r = 3 cm and height h = 10 cm. Find its volume two ways.",
                        "block_step": "Way A: 3 [ENTER] 10 [g] [CONE] -> 94.25 cm³. Way B: Base circle 3 [f] [CIRC] × 10 ÷ 3 -> 94.25 cm³!",
                        "keys": ["3", "ENTER", "10", "g", "CONE"],
                        "stack_y": "3 (Radius)",
                        "stack_x": "10 (Height) -> 94.25",
                        "ans": "94.25 cm³",
                        "note": "A cone holds exactly 1/3 the volume of a cylinder with the same base and height!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the area of a circle with radius r = 5 cm using [f] [CIRC].", "keys": "5 [f][CIRC]", "yx": "π × 5²", "ans": "78.54 cm²"},
                    {"num": 2, "part": "A", "prompt": "Find the area of a circle with radius r = 10 in using [f] [CIRC].", "keys": "10 [f][CIRC]", "yx": "π × 10²", "ans": "314.16 in²"},
                    {"num": 3, "part": "A", "prompt": "Find the hypotenuse of a right triangle with legs a = 3 and b = 4 using [g] [HYP].", "keys": "3 [ENTER] 4 [g][HYP]", "yx": "Y:3 | X:4", "ans": "5"},
                    {"num": 4, "part": "A", "prompt": "Find the hypotenuse of a right triangle with legs a = 6 ft and b = 8 ft using [g] [HYP].", "keys": "6 [ENTER] 8 [g][HYP]", "yx": "Y:6 | X:8", "ans": "10 ft"},
                    {"num": 5, "part": "B", "prompt": "Find the hypotenuse of a skate ramp with base 12 ft and back height 5 ft using [g] [HYP].", "keys": "12 [ENTER] 5 [g][HYP]", "yx": "Y:12 | X:5", "ans": "13 ft"},
                    {"num": 6, "part": "B", "prompt": "A circle has diameter d = 16 m. Divide by 2 to find radius r, then press [f] [CIRC]!", "keys": "16 [ENTER] 2 [÷] [f][CIRC]", "yx": "r = 8 m", "ans": "201.06 m²"},
                    {"num": 7, "part": "B", "prompt": "Find the volume of a cone with radius r = 3 cm and height h = 12 cm using [g] [CONE].", "keys": "3 [ENTER] 12 [g][CONE]", "yx": "Y:3 | X:12", "ans": "113.10 cm³"},
                    {"num": 8, "part": "B", "prompt": "Find the volume of a cone with radius r = 6 in and height h = 5 in using [g] [CONE].", "keys": "6 [ENTER] 5 [g][CONE]", "yx": "Y:6 | X:5", "ans": "188.50 in³"},
                    {"num": 9, "part": "C", "prompt": "Find the volume of a cone (r = 3 cm, h = 10 cm) both with [g] [CONE] AND via 3 [f] [CIRC] 10 [×] 3 [÷]!", "keys": "3 [ENTER] 10 [g][CONE]", "yx": "Y:3 | X:10", "ans": "94.25 cm³ (Both ways match 100%!)"},
                    {"num": 10, "part": "C", "prompt": "TV screens are measured along the diagonal. A screen is 32 in wide and 24 in tall. Find its diagonal size 2 ways!", "keys": "32 [ENTER] 24 [g][HYP]", "yx": "Y:32 | X:24", "ans": "40-inch screen (Way 2: √(1024+576) = 40)"}
                ]
            }
        ]
    },

    # =========================================================================
    # CHAPTER 9: STATISTICAL MEASURES & DATA DISPLAYS (Sections 9.1 - 9.4)
    # =========================================================================
    {
        "num": 9,
        "title": "Statistical Measures & Data Displays",
        "big_ideas_book": "Big Ideas Math Grade 6 — Chapters 9 & 10 (Statistical Measures and Data Displays)",
        "subtitle": "Mean as Fair Share, Median, Mode, Range, Quartiles, Interquartile Range (IQR), Box Plots & MAD",
        "kit_summary": "Counting & Array Tiles (COUNT-01) + Probability Dice Studio (PROB-01)",
        "hero_png": "dice_spinner_probability.png",
        "coach_misconception": "Students forget to sort data before finding Median/Quartiles, lose their place adding long lists for Mean, and dread Mean Absolute Deviation (MAD) because doing it by hand takes 20 minutes of subtraction.",
        "coach_remediation": "Show that Mean is physically leveling unequal cube towers to the same height. Then show that entering a list ONCE with [Σ+] unlocks Mean ([g] [x̄]), Median ([f] [MED]), Mode ([g] [MODE]), Range ([RNG]), Quartiles ([f] [1Q], [g] [3Q], [IQR]), and MAD ([g] [MAD]) in 1 click each!",
        "sections": [
            {
                "day_num": 38,
                "sec_num": "9.1",
                "title": "Dot Plots, Frequency & Mean as 'Fair Share Leveling' ([Σ+], [g] [x̄])",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 9.1 & 9.2 (Statistical Questions, Dot Plots, and The Mean)",
                "ccss": "CCSS.MATH.6.SP.B.5c",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Array Tiles",
                "asset_png": "counting_tiles_box_3x1x13u.png",
                "diagram_type": "stat_plot",
                "diagram_data": {"mode": "mean_towers", "towers": [3, 7, 5, 9, 6], "mean": 6, "caption": "Fair-Share Leveling: Towers 3, 7, 5, 9, 6 (Total = 30 tiles) level out to 5 equal towers of height 6 ([g][x̄] = 6)!"},
                "concept": "What is the Mean (average) physically? If you build 5 unequal cube towers (3, 7, 5, 9, 6) and move cubes from the tallest towers onto the shortest ones until all 5 are the exact same height, every tower stands 6 cubes tall! On the SC-6, clear stats ([g] [CLΣ]), enter each number with [Σ+], and press [g] [x̄] ([g][N])!",
                "examples": [
                    {
                        "title": "Example 1: Fair-Share Mean with [Σ+] & [g] [x̄]",
                        "problem": "Find the sum ([f] [Σx]), count ([N]), and Mean ([g] [x̄]) of 18, 24, 15, 27, 21.",
                        "block_step": "Press [g] [CLΣ], then enter each score followed by [Σ+]. Tap [f] [Σx] for total (105), [N] for count (5), and [g] [x̄] for Mean (21)!",
                        "keys": ["g", "CLΣ", "18", "Σ+", "24", "Σ+", "15", "Σ+", "27", "Σ+", "21", "Σ+", "g", "x̄"],
                        "stack_y": "Σx = 105 (n=5)",
                        "stack_x": "x̄ = 21",
                        "ans": "Sum = 105, Count = 5, Mean = 21",
                        "note": "If you make a typo (e.g. 35 instead of 25), type 35 [f] [Σ-] to remove it!"
                    },
                    {
                        "title": "Example 2: Finding a Missing Quiz Score for a Target Mean",
                        "problem": "You want a Mean of 90 across 4 quizzes. Your first 3 quizzes are 86, 92, and 88. What do you need on Quiz 4?",
                        "block_step": "4 quizzes averaging 90 require 4 × 90 = 360 total points. Your first 3 sum to 266, so you need 360 - 266 = 94!",
                        "keys": ["4", "ENTER", "90", "×", "86", "ENTER", "92", "+", "88", "+", "-"],
                        "stack_y": "360 (Target)",
                        "stack_x": "266 -> 94",
                        "ans": "94 on Quiz 4",
                        "note": "Balance check: (-4) + (+2) + (-2) = -4 deficit, so Quiz 4 needs 90 + 4 = 94!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Level the towers 2, 4, 6, 8. Find the sum ([f] [Σx]) and Mean ([g] [x̄]).", "keys": "[g][CLΣ] 2 [Σ+] 4 [Σ+] 6 [Σ+] 8 [Σ+] [g][x̄]", "yx": "Σx:20 | n:4", "ans": "Sum = 20, Mean = 5"},
                    {"num": 2, "part": "A", "prompt": "Find the sum and Mean of: 12, 15, 18, 11, 14.", "keys": "Load 5 nums into [Σ+] -> [g][x̄]", "yx": "Σx:70 | n:5", "ans": "Sum = 70, Mean = 14"},
                    {"num": 3, "part": "A", "prompt": "Find the Mean of your 5 gaming scores: 18, 24, 15, 27, 21.", "keys": "Load into [Σ+] -> [g][x̄]", "yx": "Σx:105 | n:5", "ans": "Mean = 21"},
                    {"num": 4, "part": "A", "prompt": "Find the Mean of these 4 decimal weights (g): 4.2, 3.8, 4.5, 3.5.", "keys": "Load into [Σ+] -> [g][x̄]", "yx": "Σx:16.0 | n:4", "ans": "Mean = 4.0 g"},
                    {"num": 5, "part": "B", "prompt": "Typo Rescue: Enter 10 [Σ+] 20 [Σ+] 35 [Σ+], then remove 35 with 35 [f] [Σ-] and add 25 [Σ+]. Find [g] [x̄]!", "keys": "... 35 [f][Σ-] 25 [Σ+] [g][x̄]", "yx": "Σx:55 | n:3", "ans": "Sum = 55, Mean = 18.33"},
                    {"num": 6, "part": "B", "prompt": "Frequency Shortcut ([FRQ]): If 10 appears 4 times and 20 appears 2 times, find the Mean of all 6 numbers!", "keys": "10 [ENTER] 4 [FRQ] 20 [ENTER] 2 [FRQ] [g][x̄]", "yx": "Σx:80 | n:6", "ans": "13.33 (80 ÷ 6)"},
                    {"num": 7, "part": "B", "prompt": "Find the Mean daily high temperature (°F): 68, 72, 75, 71, 64, 70.", "keys": "Load 6 temps into [Σ+] -> [g][x̄]", "yx": "Σx:420 | n:6", "ans": "70°F"},
                    {"num": 8, "part": "B", "prompt": "If 5 towers have a Mean height of 12 blocks, how many total blocks are in all 5 towers combined?", "keys": "5 [ENTER] 12 [×]", "yx": "Y:5 | X:12", "ans": "60 total blocks"},
                    {"num": 9, "part": "C", "prompt": "You need a Mean of 90 across 4 quizzes (360 pts). Your first 3 are 85, 92, 88. Find Quiz 4 score 2 ways!", "keys": "360 [ENTER] 265 [-]", "yx": "Y:360 | X:265", "ans": "95 (Way 2: (-5)+(+2)+(-2)=-5 -> 90+5=95)"},
                    {"num": 10, "part": "C", "prompt": "6 players have a Mean score of 15 pts (90 pts). A 7th player scores 29 pts. What is the new Mean of all 7?", "keys": "90 [ENTER] 29 [+] 7 [÷]", "yx": "Y:119 | X:7", "ans": "17 points"}
                ]
            },
            {
                "day_num": 39,
                "sec_num": "9.2",
                "title": "Median, Mode & Range — One Data Entry, Five Instant Answers!",
                "big_ideas_ref": "Big Ideas Grade 6, Section 9.3 (Measures of Center: Median, Mode, and Range)",
                "ccss": "CCSS.MATH.6.SP.B.5c",
                "kit_id": "PROB-01",
                "kit_name": "Probability & Stats Studio",
                "asset_png": "dice_spinner_probability.png",
                "diagram_type": "stat_plot",
                "diagram_data": {"mode": "mean_towers", "towers": [6, 7, 7, 7, 8, 9, 9, 10], "mean": 7.5, "caption": "Sorted Shoe Sizes (6, 7, 7, 7, 8, 9, 9, 10): Mode = 7 (most frequent), Median = 7.5 (middle), Range = 10 - 6 = 4!"},
                "concept": "Normally, finding Median and Range requires sorting the list by hand first—and missing one number ruins the answer! On the SC-6, enter your numbers with [Σ+] in ANY order: the chip sorts them automatically and gives you Mean ([g] [x̄]), Median ([f] [MED]), Mode ([g] [MODE]), and Range ([RNG]) in 1 click each!",
                "examples": [
                    {
                        "title": "Example 1: One Entry, Five Instant Stats",
                        "problem": "For shoe sizes 7, 9, 6, 7, 10, 8, 9, 7, find Mean, Median, Mode, Min, Max, and Range.",
                        "block_step": "Clear ([g] [CLΣ]), enter all 8 numbers with [Σ+], then tap [g] [x̄], [f] [MED], [g] [MODE], and [RNG]!",
                        "keys": ["g", "CLΣ", "7", "Σ+", "9", "Σ+", "6", "Σ+", "7", "Σ+", "10", "Σ+", "8", "Σ+", "9", "Σ+", "7", "Σ+", "f", "MED", "g", "MODE", "RNG"],
                        "stack_y": "MED = 7.5",
                        "stack_x": "MODE = 7 | RNG = 4",
                        "ans": "Mean = 7.875, Median = 7.5, Mode = 7, Range = 4 (10 - 6)",
                        "note": "You don't even have to sort the numbers before typing them into [Σ+]!"
                    },
                    {
                        "title": "Example 2: Outlier Detective (Why Median Beats Mean)",
                        "problem": "Daily dog-walking earnings are $15, $18, $15, $20, $17, and $90 (bonus day!). Compare Mean vs. Median.",
                        "block_step": "The $90 outlier drags the Mean way up to $29.17 (higher than 5 of the 6 days!), while the Median stays rock-solid at $17.50!",
                        "keys": ["g", "x̄", "f", "MED"],
                        "stack_y": "x̄ = 29.17",
                        "stack_x": "MED = 17.50",
                        "ans": "Mean = $29.17, Median = $17.50 (Median is much better when there is an outlier!)",
                        "note": "Whenever one extreme outlier skews the list, choose Median as the best measure of center!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Load 4, 9, 2, 7, 8 into [Σ+]. Find the Median ([f] [MED]) and Range ([RNG]).", "keys": "Load 5 nums -> [f][MED], [RNG]", "yx": "Sorted: 2,4,7,8,9", "ans": "Median = 7, Range = 7 (9 - 2)"},
                    {"num": 2, "part": "A", "prompt": "Load 12, 15, 12, 18, 20, 13 into [Σ+]. Find the Median, Mode ([g] [MODE]), and Range.", "keys": "Load 6 nums -> [f][MED], [g][MODE], [RNG]", "yx": "Sorted: 12,12,13,15,18,20", "ans": "Median = 14, Mode = 12, Range = 8"},
                    {"num": 3, "part": "A", "prompt": "Find the Mean, Median, Mode, and Range of: 5, 8, 8, 10, 14.", "keys": "Load 5 nums into [Σ+]", "yx": "Σx = 45 (n=5)", "ans": "Mean = 9, Med = 8, Mode = 8, Range = 9"},
                    {"num": 4, "part": "A", "prompt": "Find the Minimum ([f] [MIN]), Maximum ([g] [MAX]), and Range ([RNG]) of: 23, 45, 19, 38, 51.", "keys": "Load 5 nums -> [f][MIN], [g][MAX], [RNG]", "yx": "Min:19 | Max:51", "ans": "Min = 19, Max = 51, Range = 32"},
                    {"num": 5, "part": "B", "prompt": "Even Count Median: Find the Median of the 6 test scores 70, 80, 84, 90, 92, 98.", "keys": "Load 6 nums -> [f][MED]", "yx": "Avg of 84 & 90", "ans": "87 ((84+90)÷2)"},
                    {"num": 6, "part": "B", "prompt": "Outlier Check: Earnings are $15, $18, $15, $20, $17, $90. Find Mean and Median. Which represents a typical day?", "keys": "Load 6 nums -> [g][x̄], [f][MED]", "yx": "x̄:29.17 | MED:17.5", "ans": "Mean=$29.17, Med=$17.50 (Median is best!)"},
                    {"num": 7, "part": "B", "prompt": "What happens to the Mean and Median of {10, 12, 14, 16, 18} if 18 changes to 100?", "keys": "Test both on [Σ+]!", "yx": "Med stays 14!", "ans": "Mean jumps 14 -> 30.8; Median stays 14!"},
                    {"num": 8, "part": "B", "prompt": "Mystery Range: The minimum score on a quiz is 64 and the Range is 31. What was the maximum score?", "keys": "64 [ENTER] 31 [+]", "yx": "Y:64 | X:31", "ans": "95"},
                    {"num": 9, "part": "C", "prompt": "Find Median and Range of {14, 8, 21, 11, 16} both by sorting tiles by hand AND with [f] [MED] & [RNG]!", "keys": "Sorted: 8, 11, 14, 16, 21", "yx": "Med:14 | Rng:13", "ans": "Median = 14, Range = 13 (21 - 8)"},
                    {"num": 10, "part": "C", "prompt": "Home prices on a block (in $1,000s): 210, 220, 215, 225, 980. Find Mean and Median—which should a buyer trust?", "keys": "Load 5 nums -> [g][x̄], [f][MED]", "yx": "x̄:370 | MED:220", "ans": "Mean=$370k, Med=$220k (Trust Median!)"}
                ]
            },
            {
                "day_num": 40,
                "sec_num": "9.3",
                "title": "Quartiles, Interquartile Range ([IQR]) & Box-and-Whisker Plots",
                "big_ideas_ref": "Big Ideas Grade 6, Section 9.4 & 10.4 (Measures of Variation and Box-and-Whisker Plots)",
                "ccss": "CCSS.MATH.6.SP.B.4",
                "kit_id": "FRAC-01",
                "kit_name": "Fraction & Stats Studio",
                "asset_png": "fraction_studio_twin_comparator.png",
                "diagram_type": "stat_plot",
                "diagram_data": {"mode": "boxplot", "min": 68, "q1": 73.5, "med": 82, "q3": 90, "max": 96, "caption": "5-Number Box Plot: [f][MIN]=68, [f][1Q]=73.5, [f][MED]=82, [g][3Q]=90, [g][MAX]=96. Box width [IQR] = 90 - 73.5 = 16.5!"},
                "concept": "A Box-and-Whisker Plot splits your sorted data into 4 equal quarters (25% in each section, just like four 1/4 Fraction Studio blocks!). Once your data is in [Σ+], tap [f] [MIN], [f] [1Q], [f] [MED], [g] [3Q], [g] [MAX], and [IQR] (= 3Q - 1Q) to get the entire Box Plot in 5 seconds!",
                "examples": [
                    {
                        "title": "Example 1: Instant 5-Number Summary & [IQR]",
                        "problem": "Find the 5-Number Summary and IQR of: 68, 72, 75, 78, 82, 85, 88, 92, 96.",
                        "block_step": "Load all 9 scores with [Σ+]. Read off [f] [MIN] (68), [f] [1Q] (73.5), [f] [MED] (82), [g] [3Q] (90), [g] [MAX] (96), and [IQR] (16.5)!",
                        "keys": ["f", "MIN", "f", "1Q", "f", "MED", "g", "3Q", "g", "MAX", "IQR"],
                        "stack_y": "1Q: 73.5 | 3Q: 90",
                        "stack_x": "IQR: 16.5",
                        "ans": "Min=68, Q1=73.5, Med=82, Q3=90, Max=96; IQR = 16.5",
                        "note": "Check: [g] [3Q] (90) minus [f] [1Q] (73.5) = 16.5 ([IQR])!"
                    },
                    {
                        "title": "Example 2: Reading Quarters (25% / 50% / 75%) on a Box Plot",
                        "problem": "In any Box-and-Whisker Plot, what percent of the data lives inside the central box (between Q1 and Q3)?",
                        "block_step": "Left whisker = 25% (1/4), Left box half = 25% (1/4), Right box half = 25% (1/4), Right whisker = 25% (1/4). The middle box holds 25% + 25% = 50%!",
                        "keys": ["25", "ENTER", "2", "×"],
                        "stack_y": "25% (×2)",
                        "stack_x": "50% (Middle Box)",
                        "ans": "50% of the data lives inside the box (from Q1 to Q3)!",
                        "note": "A narrower box (smaller IQR) means the middle 50% of data is more consistent!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Load 10, 20, 30, 40, 50 into [Σ+]. Record Min, Q1, Med, Q3, Max, and [IQR].", "keys": "Load 5 nums -> [f][1Q], [g][3Q], [IQR]", "yx": "1Q:15 | 3Q:45", "ans": "Min=10, Q1=15, Med=30, Q3=45, Max=50, IQR=30"},
                    {"num": 2, "part": "A", "prompt": "Load 4, 6, 8, 10, 12, 14, 16 into [Σ+]. Find Q1, Median, Q3, and [IQR].", "keys": "Load 7 nums -> [f][1Q], [g][3Q], [IQR]", "yx": "1Q:6 | 3Q:14", "ans": "Q1=6, Med=10, Q3=14, IQR=8"},
                    {"num": 3, "part": "A", "prompt": "If a box plot has Q1 = 24 and Q3 = 58, what is the Interquartile Range (IQR)?", "keys": "58 [ENTER] 24 [-]", "yx": "Y:58 | X:24", "ans": "34"},
                    {"num": 4, "part": "A", "prompt": "What percent of data in a Box Plot falls above Q1 (the 25th percentile)?", "keys": "3 quarters = 3 × 25%", "yx": "75% above Q1", "ans": "75%"},
                    {"num": 5, "part": "B", "prompt": "Find the 5-Number Summary and [IQR] of the 9 scores: 68, 72, 75, 78, 82, 85, 88, 92, 96.", "keys": "Load 9 nums into [Σ+]", "yx": "1Q:73.5 | 3Q:90", "ans": "68, 73.5, 82, 90, 96; IQR = 16.5"},
                    {"num": 6, "part": "B", "prompt": "Find Q1, Median, Q3, and [IQR] for the 8 speeds: 42, 45, 48, 50, 52, 55, 58, 60.", "keys": "Load 8 nums into [Σ+]", "yx": "1Q:46.5 | 3Q:56.5", "ans": "Q1=46.5, Med=51, Q3=56.5, IQR=10"},
                    {"num": 7, "part": "B", "prompt": "Consistency Check: Player A has IQR = 4 pts and Player B has IQR = 19 pts. Who is more consistent?", "keys": "Compare box widths", "yx": "4 < 19", "ans": "Player A (smaller IQR = tighter cluster)"},
                    {"num": 8, "part": "B", "prompt": "Outlier Rule (1.5 × IQR): If Q1 = 40, Q3 = 60 (IQR = 20), any score above Q3 + 1.5(IQR) is an outlier. Find that cutoff!", "keys": "60 [ENTER] 1.5 [ENTER] 20 [×] [+]", "yx": "Y:60 | X:30", "ans": "90 (Any score > 90 is an outlier)"},
                    {"num": 9, "part": "C", "prompt": "For {12, 15, 18, 22, 25, 28, 34}, find [IQR] both with the [IQR] key AND by subtracting [g] [3Q] - [f] [1Q]!", "keys": "Load 7 nums -> [IQR]", "yx": "1Q:15 | 3Q:28", "ans": "IQR = 13 (28 - 15 = 13)"},
                    {"num": 10, "part": "C", "prompt": "200 students take a test. The box plot has Min=50, Q1=70, Med=80, Q3=90, Max=100. How many students scored between 70 and 90?", "keys": "200 [ENTER] 50 [f][%]", "yx": "Middle 50% of 200", "ans": "100 students (50% of 200)"}
                ]
            },
            {
                "day_num": 41,
                "sec_num": "9.4",
                "title": "Mean Absolute Deviation ([g] [MAD]) Without the 20-Minute Nightmare",
                "big_ideas_ref": "Big Ideas Grade 6, Section 9.5 (Mean Absolute Deviation)",
                "ccss": "CCSS.MATH.6.SP.B.5c",
                "kit_id": "COUNT-01",
                "kit_name": "Counting & Stats Studio",
                "asset_png": "counting_tiles_box_3x1x13u.png",
                "diagram_type": "stat_plot",
                "diagram_data": {"mode": "mean_towers", "towers": [10, 12, 14, 16, 18], "mean": 14, "caption": "Data 10, 12, 14, 16, 18 has Mean = 14. Distances from 14 are 4, 2, 0, 2, 4 -> Average distance [g][MAD] = 12 ÷ 5 = 2.4!"},
                "concept": "Every 6th grader dreads Mean Absolute Deviation (MAD) because doing it by hand takes 15 steps: find the Mean, subtract the Mean from every number, take the absolute value (|x|), and average all the distances! On the SC-6, once your data is in [Σ+], pressing [g] [MAD] ([g][Σ+]) computes the exact MAD in 1 click!",
                "examples": [
                    {
                        "title": "Example 1: Understanding & Checking MAD with [g] [MAD]",
                        "problem": "Find the Mean and Mean Absolute Deviation (MAD) of 10, 12, 14, 16, 18.",
                        "block_step": "Mean is 14. The distances |x - 14| from the Mean are 4, 2, 0, 2, 4 (sum = 12). Average distance = 12 ÷ 5 = 2.4! Confirm with [g] [MAD]!",
                        "keys": ["g", "CLΣ", "10", "Σ+", "12", "Σ+", "14", "Σ+", "16", "Σ+", "18", "Σ+", "g", "x̄", "g", "MAD"],
                        "stack_y": "x̄ = 14",
                        "stack_x": "MAD = 2.4",
                        "ans": "Mean = 14, MAD = 2.4",
                        "note": "[g] [MAD] ([g][Σ+]) turns a 15-minute hand calculation into a 1-second check!"
                    },
                    {
                        "title": "Example 2: Decimal Sprint Times MAD",
                        "problem": "Find the Mean and MAD of the 6 sprint times (sec): 12.4, 13.0, 12.6, 13.2, 12.8, 14.0.",
                        "block_step": "Load all 6 decimals into [Σ+]. Tap [g] [x̄] (13.0 sec) and [g] [MAD] (0.40 sec)!",
                        "keys": ["g", "x̄", "g", "MAD"],
                        "stack_y": "x̄ = 13.0 s",
                        "stack_x": "MAD = 0.40 s",
                        "ans": "Mean = 13.0 s, MAD = 0.40 s",
                        "note": "On average, each sprint was within 0.40 seconds of the 13.0 s mean!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Load 2, 4, 6 into [Σ+]. Find the Mean ([g] [x̄]) and MAD ([g] [MAD]).", "keys": "2 [Σ+] 4 [Σ+] 6 [Σ+] [g][MAD]", "yx": "x̄:4 | dists:2,0,2", "ans": "Mean = 4, MAD = 1.33 (4/3)"},
                    {"num": 2, "part": "A", "prompt": "Load 10, 12, 14, 16, 18 into [Σ+]. Find the Mean and MAD.", "keys": "Load 5 nums -> [g][x̄], [g][MAD]", "yx": "x̄:14 | dists:4,2,0,2,4", "ans": "Mean = 14, MAD = 2.4"},
                    {"num": 3, "part": "A", "prompt": "Load 5, 8, 8, 10, 14 into [Σ+]. Find the Mean and MAD.", "keys": "Load 5 nums -> [g][x̄], [g][MAD]", "yx": "x̄:9 | dists:4,1,1,1,5", "ans": "Mean = 9, MAD = 2.4"},
                    {"num": 4, "part": "A", "prompt": "What is the MAD of 7, 7, 7, 7, 7 (5 identical towers)?", "keys": "All distances from 7 are 0!", "yx": "x̄:7 | MAD:0", "ans": "Mean = 7, MAD = 0"},
                    {"num": 5, "part": "B", "prompt": "Find the Mean and MAD of: 20, 24, 28, 32, 36.", "keys": "Load 5 nums -> [g][x̄], [g][MAD]", "yx": "x̄:28 | dists:8,4,0,4,8", "ans": "Mean = 28, MAD = 4.8"},
                    {"num": 6, "part": "B", "prompt": "Find the Mean and MAD of the 6 sprint times: 12.4, 13.0, 12.6, 13.2, 12.8, 14.0.", "keys": "Load 6 decimals -> [g][x̄], [g][MAD]", "yx": "x̄:13.0 | MAD:0.40", "ans": "Mean = 13.0, MAD = 0.40"},
                    {"num": 7, "part": "B", "prompt": "Find the Mean and MAD of quiz scores: 82, 85, 88, 90, 95.", "keys": "Load 5 nums -> [g][x̄], [g][MAD]", "yx": "x̄:88 | dists:6,3,0,2,7", "ans": "Mean = 88, MAD = 3.6"},
                    {"num": 8, "part": "B", "prompt": "Team A has Mean = 50, MAD = 2.1. Team B has Mean = 50, MAD = 8.4. Which team's scores are more spread out?", "keys": "Compare MADs", "yx": "8.4 > 2.1", "ans": "Team B (larger MAD = more spread out)"},
                    {"num": 9, "part": "C", "prompt": "For {6, 10, 11, 13}, find MAD both by averaging |x - 10| distances AND with 1 click of [g] [MAD]!", "keys": "Mean=10; dists 4+0+1+3=8 ÷ 4", "yx": "x̄:10 | MAD:2", "ans": "Mean = 10, MAD = 2.0"},
                    {"num": 10, "part": "C", "prompt": "Full Chapter 9 Boss Sweep: For {5, 8, 8, 10, 14}, record [g][x̄], [f][MED], [g][MODE], [RNG], [IQR], and [g][MAD]!", "keys": "1 entry -> 6 stats!", "yx": "x̄:9, Med:8, Mode:8", "ans": "x̄=9, Med=8, Mode=8, Rng=9, IQR=5.5, MAD=2.4"}
                ]
            }
        ]
    },

    # =========================================================================
    # CHAPTER 10: GRADE 7 BRIDGE — SIGNED RATIONALS, 2-STEP EQUATIONS & PROBABILITY (Sections 10.1 - 10.4)
    # =========================================================================
    {
        "num": 10,
        "title": "Grade 7 Bridge — Signed Rationals, 2-Step Equations & Probability",
        "big_ideas_book": "Big Ideas Math Grade 7 Bridge — Chapters 1–3 & Chapter 7",
        "subtitle": "Adding, Subtracting, Multiplying & Dividing Signed Rationals, Two-Step Equations, and Probability/Combinatorics",
        "kit_summary": "Ten-Frame Zero-Pair Counters (BASE-10) + Algebra Stage (ALGB-01) + Probability Studio (PROB-01)",
        "hero_png": "dice_spinner_d20_and_polyhedra.png",
        "coach_misconception": "Students guess signs when adding/subtracting negatives, get -25 instead of +25 for (-5)² on algebraic calculators, undo ×3 before +7 in 3x + 7 = 28, and confuse Permutations (order matters) with Combinations (order doesn't).",
        "coach_remediation": "Use Yellow/Red counters to show removing 4 red debt tokens (10 - (-4)) equals +14. Notice how RPN 5 [+/-] [x²] squares the entire register (-5)² = +25 without parentheses! Unwrap 2-step equations in reverse (untie ribbon ±b first, open box ×a second), and finish with [DICE], [f] [nCr], [g] [nPr], and [f] [?].",
        "sections": [
            {
                "day_num": 42,
                "sec_num": "10.1",
                "title": "Adding & Subtracting Signed Numbers — Why 'Minus a Negative' Adds!",
                "big_ideas_ref": "Big Ideas Grade 7, Sections 1.2, 1.3, 2.2 & 2.3 (Adding and Subtracting Integers & Rational Numbers)",
                "ccss": "CCSS.MATH.7.NS.A.1",
                "kit_id": "BASE-10",
                "kit_name": "Ten-Frame Zero-Pair Counters",
                "asset_png": "ten_frame_subitizing_5anchor.png",
                "diagram_type": "zero_pairs",
                "diagram_data": {"pos": 5, "neg": 8, "net": -3, "caption": "-8 + 5: 8 Red (-1) + 5 Yellow (+1) -> 5 Zero Pairs cancel, leaving 3 Red (-3)! And 10 - (-4) removes 4 debts = +14!"},
                "concept": "When adding with Yellow (+1) and Red (-1) counters: if signs are the SAME, they team up (-6 + (-4) = -10); if signs are OPPOSITE, they fight in Zero Pairs (-8 + 5 = -3)! And why does subtracting a negative like 10 - (-4) equal +14? Because erasing a -4 penalty makes your score go UP by 4!",
                "examples": [
                    {
                        "title": "Example 1: Zero-Pair Battle (-8 + 5) vs. Same-Sign Team-Up (-6 + (-4))",
                        "problem": "Evaluate -8 + 5 and -6 + (-4) using counters and the SC-6 [+/-] key.",
                        "block_step": "-8 + 5 cancels 5 Zero Pairs, leaving 3 Red (-3). -6 + (-4) combines 6 Red and 4 Red into 10 Red (-10)!",
                        "keys": ["8", "+/-", "ENTER", "5", "+", "6", "+/-", "ENTER", "4", "+/-", "+"],
                        "stack_y": "-3 (-8 + 5)",
                        "stack_x": "-10 (-6 + -4)",
                        "ans": "-8 + 5 = -3; -6 + (-4) = -10",
                        "note": "Always enter the number first, then tap [+/-] to make it negative!"
                    },
                    {
                        "title": "Example 2: Taking Away a Debt 10 - (-4) & Signed Fractions",
                        "problem": "Evaluate 10 - (-4) and -3/4 - (-5/8).",
                        "block_step": "Subtracting -4 is the same as adding +4: 10 - (-4) = 14. For -3/4 - (-5/8): -6/8 + 5/8 = -1/8!",
                        "keys": ["10", "ENTER", "4", "+/-", "-", ".", "3", ".", "4", "+/-", "ENTER", ".", "5", ".", "8", "+/-", "-"],
                        "stack_y": "14 (10 - -4)",
                        "stack_x": "-1/8",
                        "ans": "10 - (-4) = 14; -3/4 - (-5/8) = -1/8",
                        "note": "Check with [f] [LASTX] [+]: -1/8 + (-5/8) = -6/8 = -3/4!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Solve side-by-side: (a) -15 + 9 and (b) -15 + (-9).", "keys": "15 [+/-] [ENTER] 9 [+] / 9 [+/-] [+]", "yx": "Fight vs Team up", "ans": "(a) -6; (b) -24"},
                    {"num": 2, "part": "A", "prompt": "Solve: 14 + (-23).", "keys": "14 [ENTER] 23 [+/-] [+]", "yx": "Y:14 | X:-23", "ans": "-9"},
                    {"num": 3, "part": "A", "prompt": "Taking Away a Penalty: Solve (a) 12 - (-8) and (b) -12 - (-8).", "keys": "12 [ENTER] 8 [+/-] [-] / 12 [+/-]...", "yx": "12+8 vs -12+8", "ans": "(a) 20; (b) -4"},
                    {"num": 4, "part": "A", "prompt": "Solve: -9 - 16. (Start at -9 and go 16 steps further negative!)", "keys": "9 [+/-] [ENTER] 16 [-]", "yx": "Y:-9 | X:16", "ans": "-25"},
                    {"num": 5, "part": "B", "prompt": "Solve with decimals: -4.8 + (-3.5).", "keys": "4.8 [+/-] [ENTER] 3.5 [+/-] [+]", "yx": "Y:-4.8 | X:-3.5", "ans": "-8.3"},
                    {"num": 6, "part": "B", "prompt": "Solve with decimals: 6.4 - 11.2.", "keys": "6.4 [ENTER] 11.2 [-]", "yx": "Y:6.4 | X:11.2", "ans": "-4.8"},
                    {"num": 7, "part": "B", "prompt": "Solve with decimals: -7.5 - (-10.2).", "keys": "7.5 [+/-] [ENTER] 10.2 [+/-] [-]", "yx": "Y:-7.5 | X:-10.2", "ans": "+2.7"},
                    {"num": 8, "part": "B", "prompt": "Solve with signed fractions: -3/4 - (-5/8).", "keys": "[.] 3 [.] 4 [+/-] [ENTER] [.] 5 [.] 8 [+/-] [-]", "yx": "-6/8 - (-5/8)", "ans": "-1/8"},
                    {"num": 9, "part": "C", "prompt": "Temperature in Fairbanks is -18°F at dawn and rises to +7°F by noon. Find the change (7 - (-18)) 2 ways!", "keys": "7 [ENTER] 18 [+/-] [-]", "yx": "Y:7 | X:-18", "ans": "+25°F (Way 2: 18 steps to 0 + 7 steps = 25)"},
                    {"num": 10, "part": "C", "prompt": "Evaluate -2 1/2 + 4 1/4 - (-1 1/8) on the SC-6 and check by converting to eighths!", "keys": "2.5 [+/-] [ENTER] 4.25 [+] 1.125 [+]", "yx": "1.75 + 1.125", "ans": "2 7/8 (2.875)"}
                ]
            },
            {
                "day_num": 43,
                "sec_num": "10.2",
                "title": "Multiplying & Dividing Signed Rationals — The Light-Switch Flip Rule",
                "big_ideas_ref": "Big Ideas Grade 7, Sections 1.4, 1.5 & 2.4 (Multiplying and Dividing Rational Numbers)",
                "ccss": "CCSS.MATH.7.NS.A.2",
                "kit_id": "BASE-10",
                "kit_name": "Zero-Pair & Fraction Studio",
                "asset_png": "fraction_studio_common_denominator.png",
                "diagram_type": "zero_pairs",
                "diagram_data": {"pos": 4, "neg": 4, "net": 0, "caption": "Light-Switch Rule: 1 Negative flips to (-); 2 Negatives flip back to (+)! So (-6) × (-4) = +24 and (-5)² = +25!"},
                "concept": "Think of a negative sign as flipping a light switch (just like tapping [+/-]!): 1 negative flip leaves you in the dark (-), but 2 negative flips bring you right back to POSITIVE (+)! And on the SC-6, 5 [+/-] [x²] squares the entire number (-5) × (-5) = +25 without needing parentheses!",
                "examples": [
                    {
                        "title": "Example 1: The 4 Sign Combinations & (-5)²",
                        "problem": "Compute 6 × (-4), (-6) × (-4), and (-5)² on your SC-6.",
                        "block_step": "1 negative gives -24; 2 negatives flip back to +24! For (-5)², type 5 [+/-] [x²] -> +25!",
                        "keys": ["6", "ENTER", "4", "+/-", "×", "5", "+/-", "x²"],
                        "stack_y": "-24 (6 × -4)",
                        "stack_x": "+25 ((-5)²)",
                        "ans": "6×(-4) = -24, (-6)×(-4) = +24, (-5)² = +25",
                        "note": "On algebraic calculators, typing -5² gives -25! On RPN, 5 [+/-] [x²] squares -5 to +25!"
                    },
                    {
                        "title": "Example 2: Signed Fraction Division (-5/6 ÷ -5/12)",
                        "problem": "Evaluate -5/6 ÷ (-5/12) and check the sign rule.",
                        "block_step": "Negative ÷ Negative = Positive (+). Flipping -5/12 gives -12/5, and (-5/6) × (-12/5) = +2!",
                        "keys": [".", "5", ".", "6", "+/-", "ENTER", ".", "5", ".", "12", "+/-", "÷"],
                        "stack_y": "-5/6",
                        "stack_x": "-5/12 -> +2",
                        "ans": "+2",
                        "note": "Count the negative signs first: Even count = Positive (+); Odd count = Negative (-)!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Compute: (a) 7 × (-8) and (b) (-7) × (-8).", "keys": "7 [ENTER] 8 [+/-] [×] / 7 [+/-]...", "yx": "1 neg vs 2 negs", "ans": "(a) -56; (b) +56"},
                    {"num": 2, "part": "A", "prompt": "Compute: (a) -45 ÷ 9 and (b) -45 ÷ (-9).", "keys": "45 [+/-] [ENTER] 9 [÷] / 9 [+/-] [÷]", "yx": "1 neg vs 2 negs", "ans": "(a) -5; (b) +5"},
                    {"num": 3, "part": "A", "prompt": "Compute (-5)² using 5 [+/-] [x²]. Why is it +25?", "keys": "5 [+/-] [x²]", "yx": "(-5) × (-5)", "ans": "+25 (2 negatives = +)"},
                    {"num": 4, "part": "A", "prompt": "Compute (-2)³ using 2 [+/-] [g] [x³]. Why is a negative cubed still negative?", "keys": "2 [+/-] [g][x³]", "yx": "(-2)×(-2)×(-2)", "ans": "-8 (3 negatives = odd = -)"},
                    {"num": 5, "part": "B", "prompt": "Multiply signed decimals: (-3.5) × (-2.4).", "keys": "3.5 [+/-] [ENTER] 2.4 [+/-] [×]", "yx": "Y:-3.5 | X:-2.4", "ans": "+8.4"},
                    {"num": 6, "part": "B", "prompt": "Divide signed decimals: -14.4 ÷ 1.2.", "keys": "14.4 [+/-] [ENTER] 1.2 [÷]", "yx": "Y:-14.4 | X:1.2", "ans": "-12"},
                    {"num": 7, "part": "B", "prompt": "Multiply signed fractions: (-2/3) × (9/10).", "keys": "[.] 2 [.] 3 [+/-] [ENTER] [.] 9 [.] 10 [×]", "yx": "Y:-2/3 | X:9/10", "ans": "-3/5 (-0.6)"},
                    {"num": 8, "part": "B", "prompt": "Divide signed fractions: -5/6 ÷ (-5/12).", "keys": "[.] 5 [.] 6 [+/-] [ENTER] [.] 5 [.] 12 [+/-] [÷]", "yx": "Y:-5/6 | X:-5/12", "ans": "+2"},
                    {"num": 9, "part": "C", "prompt": "Triple Product: Evaluate (-4) × (-5) × (-3) both by counting negative signs AND on your SC-6!", "keys": "4 [+/-] [ENTER] 5 [+/-] [×] 3 [+/-] [×]", "yx": "Y:20 | X:-3", "ans": "-60 (3 negatives = odd -> negative!)"},
                    {"num": 10, "part": "C", "prompt": "A submarine dives 360 ft in 8 minutes (-45 ft/min). Confirm the total change in 8 min and the change per minute!", "keys": "360 [+/-] [ENTER] 8 [÷]", "yx": "Y:-360 | X:8", "ans": "-45 ft/min (Check: -45 × 8 = -360 ft)"}
                ]
            },
            {
                "day_num": 44,
                "sec_num": "10.3",
                "title": "Solving Two-Step Equations (ax + b = c) — Unwrapping in Reverse!",
                "big_ideas_ref": "Big Ideas Grade 7, Sections 3.3–3.5 (Solving Two-Step Equations)",
                "ccss": "CCSS.MATH.7.EE.B.4a",
                "kit_id": "ALGB-01",
                "kit_name": "Algebra Boxes & Stage",
                "asset_png": "algebra_factoring_area.png",
                "diagram_type": "balance_scale",
                "diagram_data": {"left": "3x + 7", "right": "28", "sol": "Step 1: 28-7=21 -> Step 2: 21÷3 = 7!", "caption": "Unwrap in Reverse: First remove the 7 loose cubes (28 - 7 = 21), THEN split 21 across the 3 x-rods (21 ÷ 3 = 7)!"},
                "concept": "Think of 3x + 7 = 28 like wrapping a present: first x was put into 3 boxes (× 3), then 7 loose cubes were tied on outside (+ 7). When you unwrap the present, go in REVERSE: untie the loose cubes FIRST (28 [ENTER] 7 [-] -> 21), and divide by the 3 boxes SECOND (3 [÷] -> x = 7)!",
                "examples": [
                    {
                        "title": "Example 1: Solving 3x + 7 = 28 with Inverse Operations",
                        "problem": "Solve 3x + 7 = 28 using inverse operations and check your solution.",
                        "block_step": "Step 1 (Clear loose cubes): 28 - 7 = 21 (so 3x = 21). Step 2 (Split across rods): 21 ÷ 3 = 7! Check: 3(7) + 7 = 28!",
                        "keys": ["28", "ENTER", "7", "-", "3", "÷"],
                        "stack_y": "21 (3x = 21)",
                        "stack_x": "3 -> x = 7",
                        "ans": "x = 7 (Step 1: 3x = 21)",
                        "note": "Step 1: Subtract 7 (3x = 21). Step 2: Divide by 3 (x = 7)!"
                    },
                    {
                        "title": "Example 2: Negative Coefficient Two-Step (-3x + 14 = 2)",
                        "problem": "Solve -3x + 14 = 2 on the SC-6 and verify by plugging x back in.",
                        "block_step": "Step 1 (Subtract 14): 2 [ENTER] 14 [-] -> -12 (so -3x = -12). Step 2 (Divide by -3): 3 [+/-] [÷] -> x = +4!",
                        "keys": ["2", "ENTER", "14", "-", "3", "+/-", "÷"],
                        "stack_y": "-12 (-3x)",
                        "stack_x": "-3 -> x = 4",
                        "ans": "x = 4",
                        "note": "Check: -3(4) + 14 = -12 + 14 = 2 (100% Proven)!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Solve 4x + 9 = 45. Write the Step 1 value (4x = ?) and final x.", "keys": "45 [ENTER] 9 [-] 4 [÷]", "yx": "Y:36 | X:4", "ans": "4x = 36 -> x = 9"},
                    {"num": 2, "part": "A", "prompt": "Solve 5x - 12 = 38. (Undo -12 with [+] first, then ÷ 5!)", "keys": "38 [ENTER] 12 [+] 5 [÷]", "yx": "Y:50 | X:5", "ans": "5x = 50 -> x = 10"},
                    {"num": 3, "part": "A", "prompt": "Solve 6y + 11 = 59.", "keys": "59 [ENTER] 11 [-] 6 [÷]", "yx": "Y:48 | X:6", "ans": "6y = 48 -> y = 8"},
                    {"num": 4, "part": "A", "prompt": "Solve 8n - 15 = 49.", "keys": "49 [ENTER] 15 [+] 8 [÷]", "yx": "Y:64 | X:8", "ans": "8n = 64 -> n = 8"},
                    {"num": 5, "part": "B", "prompt": "Solve m / 4 + 6 = 15. (Subtract 6 first, then multiply by 4!)", "keys": "15 [ENTER] 6 [-] 4 [×]", "yx": "Y:9 | X:4", "ans": "m/4 = 9 -> m = 36"},
                    {"num": 6, "part": "B", "prompt": "Solve k / 3 - 5 = 7.", "keys": "7 [ENTER] 5 [+] 3 [×]", "yx": "Y:12 | X:3", "ans": "k/3 = 12 -> k = 36"},
                    {"num": 7, "part": "B", "prompt": "Solve -3x + 14 = 2.", "keys": "2 [ENTER] 14 [-] 3 [+/-] [÷]", "yx": "Y:-12 | X:-3", "ans": "-3x = -12 -> x = 4"},
                    {"num": 8, "part": "B", "prompt": "Solve 2.5w + 8 = 23.", "keys": "23 [ENTER] 8 [-] 2.5 [÷]", "yx": "Y:15 | X:2.5", "ans": "2.5w = 15 -> w = 6"},
                    {"num": 9, "part": "C", "prompt": "A repair tech charges $35 flat plus $25/hr (25h + 35 = 160). Find hours h by unwrapping AND plug-in check!", "keys": "160 [ENTER] 35 [-] 25 [÷]", "yx": "Y:125 | X:25", "ans": "h = 5 hours (Check: 25(5)+35 = 160)"},
                    {"num": 10, "part": "C", "prompt": "You save $15/week toward a $120 skateboard and already have $45 (15w + 45 = 120). How many weeks w?", "keys": "120 [ENTER] 45 [-] 15 [÷]", "yx": "Y:75 | X:15", "ans": "w = 5 weeks (Check: 15(5)+45 = 120)"}
                ]
            },
            {
                "day_num": 45,
                "sec_num": "10.4",
                "title": "Probability, Combinatorics & Graduation Quiz Sprint ([DICE], [x!], [f] [nCr], [f] [?])",
                "big_ideas_ref": "Big Ideas Grade 7, Chapter 7 (Probability) & SC-6 Graduation Finale",
                "ccss": "CCSS.MATH.7.SP.C.5",
                "kit_id": "PROB-01",
                "kit_name": "Probability Dice & Spinner Studio",
                "asset_png": "dice_spinner_d20_and_polyhedra.png",
                "diagram_type": "prob_spinner",
                "diagram_data": {"blue": 4, "gold": 3, "red": 3, "caption": "10-Sector Spinner (PROB-01): P(Blue) = 4/10 = 2/5 = 0.40 = 40%! Plus [x!], [f][nCr], [g][nPr] & [f][?] Quiz Engine!"},
                "concept": "Probability is Favorable Outcomes ÷ Total Outcomes—and you can express it as a Fraction, Decimal, or Percent! Plus, the top-left keys of your SC-6 unlock Combinatorics: [x!] ([g][DICE]) for arrangements of all n items, [g] [nPr] when order matters (1st/2nd/3rd podium), [f] [nCr] when order does NOT matter (pizza toppings), and [f] [?] ([f][C]) for the built-in Math Quiz Engine!",
                "examples": [
                    {
                        "title": "Example 1: 3-Way Probability & Factorial ([x!])",
                        "problem": "A 10-sector spinner has 4 Blue, 3 Gold, and 3 Red sectors. Find P(Blue) in 3 forms, and find how many ways to line up 5 trophies (5!).",
                        "block_step": "P(Blue) = 4/10 = 2/5 = 0.40 = 40%. For 5 trophies: press 5 [g] [x!] ([g][DICE]) -> 120 ways!",
                        "keys": [".", "4", ".", "10", "g", "SIMP", "5", "g", "x!"],
                        "stack_y": "2/5 (0.4 = 40%)",
                        "stack_x": "120 (5!)",
                        "ans": "P(Blue) = 2/5 = 0.4 = 40%; 5! = 120 ways",
                        "note": "5! means 5 × 4 × 3 × 2 × 1 = 120!"
                    },
                    {
                        "title": "Example 2: Combinations ([f] [nCr]) vs. Permutations ([g] [nPr])",
                        "problem": "Compare choosing 3 pizza toppings from 10 ([f] [nCr]) vs. awarding 1st, 2nd, 3rd place to 10 runners ([g] [nPr]).",
                        "block_step": "Pizza toppings don't care about order: 10 [ENTER] 3 [f] [nCr] = 120. Podium medals DO care about order: 10 [ENTER] 3 [g] [nPr] = 720!",
                        "keys": ["10", "ENTER", "3", "f", "nCr", "10", "ENTER", "3", "g", "nPr"],
                        "stack_y": "120 (nCr)",
                        "stack_x": "720 (nPr)",
                        "ans": "120 pizza combinations vs. 720 podium permutations",
                        "note": "Notice 720 is 6 times 120 because 3! = 6 ways to order the 3 winners!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Roll a fair 6-sided die. Find P(rolling a 5) as a fraction, and P(rolling an even number) in simplest form.", "keys": "1/6; and 3/6 -> [g][SIMP]", "yx": "1/6 and 1/2", "ans": "1/6; and 1/2 (50%)"},
                    {"num": 2, "part": "A", "prompt": "A 10-sector spinner has 4 Blue, 3 Gold, 3 Red. Find P(Blue) as a simplified fraction, decimal, and percent.", "keys": "[.] 4 [.] 10 [g][SIMP] [FDISP]", "yx": "2/5 = 0.4 = 40%", "ans": "2/5, 0.4, 40%"},
                    {"num": 3, "part": "A", "prompt": "Using the same 10-sector spinner, find P(NOT Red) as a fraction and percent.", "keys": "(10 - 3) / 10 = 7/10", "yx": "7/10 = 0.7", "ans": "7/10 (70%)"},
                    {"num": 4, "part": "A", "prompt": "In how many ways can 4 students line up at the door? Compute 4! using [g] [x!].", "keys": "4 [g][x!]", "yx": "4×3×2×1", "ans": "24 ways"},
                    {"num": 5, "part": "B", "prompt": "In how many ways can you arrange 6 books on a shelf? Compute 6! using [g] [x!].", "keys": "6 [g][x!]", "yx": "6×5×4×3×2×1", "ans": "720 ways"},
                    {"num": 6, "part": "B", "prompt": "How many ways can you choose a 3-person team from 8 players (order does NOT matter: [f] [nCr])?", "keys": "8 [ENTER] 3 [f][nCr]", "yx": "Y:8 | X:3", "ans": "56 teams"},
                    {"num": 7, "part": "B", "prompt": "How many ways can 1st, 2nd, and 3rd place be awarded among 8 finalists (order DOES matter: [g] [nPr])?", "keys": "8 [ENTER] 3 [g][nPr]", "yx": "Y:8 | X:3", "ans": "336 podiums"},
                    {"num": 8, "part": "B", "prompt": "Two Independent Events: You flip a coin (1/2) AND roll a 6-sided die (P(>4) = 2/6 = 1/3). Multiply to find P(Heads and >4)!", "keys": "[.] 1 [.] 2 [ENTER] [.] 1 [.] 3 [×]", "yx": "Y:1/2 | X:1/3", "ans": "1/6"},
                    {"num": 9, "part": "C", "prompt": "From 10 toppings, compare choosing 3 toppings ([f] [nCr]) vs. 3 ordered medals ([g] [nPr]). How are they related by 3!?", "keys": "10 [ENTER] 3 [f][nCr] / [g][nPr]", "yx": "Y:120 | X:720", "ans": "120 vs 720 (120 × 3! = 720)"},
                    {"num": 10, "part": "C", "prompt": "GRADUATION BOSS: Compute 5! both with [g] [x!] AND 5 [ENTER] 5 [g] [nPr], then complete a 5-streak on [f] [?]!", "keys": "5 [g][x!]; then [f][?]", "yx": "X: 120", "ans": "120 ways (Course Complete!)"}
                ]
            }
        ]
    }
])
