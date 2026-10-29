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
        "kit_summary": "Place Value Studio (PLACE-01) + Prime Factor Studio (PRIME-01)",
        "hero_png": "prime_lcm_gcd_venn.png",
        "coach_misconception": "Students interpret remainders as meaningless decimal tails (e.g., .875 of a person), read 2^3 as 2×3=6, lose track of PEMDAS parentheses, and confuse GCF (overlap) with LCM (union).",
        "coach_remediation": "Have students model division remainders on the Place Value Tray, stack Prime Factor Blocks ([2][2][2] = 2³) for exponents, use the 4-line elevator (Y holds Room 1 while X solves Room 2) instead of rewriting PEMDAS lines, and stand logarithmic Prime Factor Towers side-by-side on the 12-socket lid.",
        "sections": [
            {
                "day_num": 1,
                "sec_num": "1.1",
                "title": "Whole Number Operations & Division with Remainders",
                "big_ideas_ref": "Big Ideas Grade 6, Section 1.1 (Whole Number Operations)",
                "ccss": "CCSS.MATH.6.NS.B.2",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "array_rem",
                "diagram_data": {"total": 23, "divisor": 4, "quotient": 5, "rem": 3, "caption": "23 split into groups of 4 = 5 full groups (20) + 3 leftover units"},
                "concept": "In Big Ideas Math, whole-number division splits a dividend into equal groups of the divisor: Dividend = (Quotient × Divisor) + Remainder, where the remainder is always less than the divisor. Modeling the dividend on the Place Value Tray (PLACE-01) physically separates the equal groups (Quotient) from the leftover ones (Remainder).",
                "examples": [
                    {
                        "title": "Example 1: Long Division & Remainder Check",
                        "problem": "Divide 23 ÷ 4 and check your answer using the Division Algorithm.",
                        "block_step": "Partition 23 into equal groups of 4: you build 5 full groups (20) with 3 leftover units.",
                        "keys": ["23", "ENTER", "4", "g", "÷R"],
                        "stack_y": "3 (Rem)",
                        "stack_x": "5 (Quot)",
                        "ans": "5 R 3",
                        "note": "Check: (5 × 4) + 3 = 20 + 3 = 23!"
                    },
                    {
                        "title": "Example 2: Interpreting the Remainder",
                        "problem": "135 students ride in 8-passenger vans. How many vans are completely full, and how many vans are needed so no student is left behind?",
                        "block_step": "135 ÷ 8 = 16 R 7. That means 16 vans are completely full (128 students), and 1 extra van is needed for the 7 remaining students.",
                        "keys": ["135", "ENTER", "8", "g", "÷R", "f", "LASTX", "×", "+"],
                        "stack_y": "7 -> 0",
                        "stack_x": "16 -> 135",
                        "ans": "16 full vans; 17 vans needed",
                        "note": "Check: 16 × 8 + 7 = 135!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Divide 31 ÷ 6.", "keys": "31 [ENTER] 6 [g][÷R]", "yx": "Y:1 | X:5", "ans": "5 R 1"},
                    {"num": 2, "part": "A", "prompt": "Divide 47 ÷ 5.", "keys": "47 [ENTER] 5 [g][÷R]", "yx": "Y:2 | X:9", "ans": "9 R 2"},
                    {"num": 3, "part": "A", "prompt": "Divide 58 ÷ 7 and check your answer by multiplying.", "keys": "58 [ENTER] 7 [g][÷R]", "yx": "Y:2 | X:8", "ans": "8 R 2"},
                    {"num": 4, "part": "A", "prompt": "Divide 85 ÷ 9. How many full groups of 9 can be made, and how many are left over?", "keys": "85 [ENTER] 9 [g][÷R]", "yx": "Y:4 | X:9", "ans": "9 R 4"},
                    {"num": 5, "part": "B", "prompt": "Divide 146 ÷ 12.", "keys": "146 [ENTER] 12 [g][÷R]", "yx": "Y:2 | X:12", "ans": "12 R 2"},
                    {"num": 6, "part": "B", "prompt": "Parachute Cord Rigging: A rigger cuts 35 cm suspension lines from a 250 cm spool of cord. How many full lines can be cut, and how many centimeters of cord remain?", "keys": "250 [ENTER] 35 [g][÷R]", "yx": "Y:5 | X:7", "ans": "7 full lines, 5 cm left"},
                    {"num": 7, "part": "B", "prompt": "When a number is divided by 8, the quotient is 14 and the remainder is 5. What is the number?", "keys": "14 [ENTER] 8 [×] 5 [+]", "yx": "Y:112 | X:5", "ans": "117"},
                    {"num": 8, "part": "B", "prompt": "Error Analysis: Sam says 75 ÷ 8 = 8 R 11. Explain why a remainder of 11 is impossible and find the correct answer.", "keys": "75 [ENTER] 8 [g][÷R]", "yx": "Y:3 | X:9", "ans": "9 R 3 (Rem < 8)"},
                    {"num": 9, "part": "C", "prompt": "All-Terrain Rover Assembly: A robotics depot has 78 rover tires. Each rover requires 4 tires. How many complete 4-wheel rovers can be built, and how many tires are left in spares?", "keys": "78 [ENTER] 4 [g][÷R]", "yx": "Y:2 | X:19", "ans": "19 rovers, 2 tires left"},
                    {"num": 10, "part": "C", "prompt": "Wilderness Tent Expedition: 29 explorers are setting up 4-person tents for a storm. How many tents must they pitch so every explorer has shelter?", "keys": "29 [ENTER] 4 [g][÷R]", "yx": "Y:1 | X:7", "ans": "8 tents (7 full + 1 for the 29th explorer)"}
                ]
            },
            {
                "day_num": 2,
                "sec_num": "1.2",
                "title": "Powers and Exponents",
                "big_ideas_ref": "Big Ideas Grade 6, Section 1.2 (Powers and Exponents)",
                "ccss": "CCSS.MATH.6.EE.A.1",
                "kit_id": "PRIME-01",
                "kit_name": "Prime Factor Studio",
                "asset_png": "prime_studio_comparator_stage.png",
                "diagram_type": "power_array",
                "diagram_data": {"base": 4, "sq": 16, "trap": 8, "caption": "4² = 4×4 square model (16), NEVER 4×2 (8)!"},
                "concept": "A power represents repeated multiplication of the same factor. In bⁿ, the base b is the repeated factor and the exponent n tells how many times the base is used as a factor. In the Prime Factor Studio (PRIME-01), stacking n identical prime blocks models bⁿ directly (for example, three [2] blocks build 2³ = 8, and four [2] blocks build 4² = 2⁴ = 16).",
                "examples": [
                    {
                        "title": "Example 1: Writing & Evaluating Squares and Cubes",
                        "problem": "Write 4² and 4³ as repeated multiplication and find their values. Compare 4² to 4 × 2.",
                        "block_step": "Multiply 4 × 4 = 16 for 4² (four [2] prime blocks = 2⁴ = 16), and 4 × 4 × 4 = 64 for 4³ (six [2] prime blocks = 2⁶ = 64). Notice 4 × 2 is only 8!",
                        "keys": ["4", "x²", "4", "x³"],
                        "stack_y": "16 (4²)",
                        "stack_x": "64 (4³)",
                        "ans": "4² = 16, 4³ = 64",
                        "note": "4² = 4 × 4 = 16; 4³ = 4 × 4 × 4 = 64!"
                    },
                    {
                        "title": "Example 2: Evaluating Higher Powers",
                        "problem": "Evaluate 3⁴.",
                        "block_step": "Stack four [3] Prime Factor blocks: 3 × 3 × 3 × 3. Multiply in pairs (9 × 9 = 81) or step-by-step (3 -> 9 -> 27 -> 81).",
                        "keys": ["3", "ENTER", "4", "g", "yˣ"],
                        "stack_y": "3 (Base)",
                        "stack_x": "4 (Exp)",
                        "ans": "81",
                        "note": "3⁴ = 3 × 3 × 3 × 3 = 81!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Write 5² as repeated multiplication and find its value.", "keys": "5 [x²]", "yx": "Y:0 | X:25", "ans": "5 × 5 = 25"},
                    {"num": 2, "part": "A", "prompt": "Evaluate 7² and compare its value to 7 × 2.", "keys": "7 [x²]", "yx": "Y:0 | X:49", "ans": "49 (vs. 14)"},
                    {"num": 3, "part": "A", "prompt": "Write 3³ as repeated multiplication and find its value.", "keys": "3 [x³]", "yx": "Y:0 | X:27", "ans": "3 × 3 × 3 = 27"},
                    {"num": 4, "part": "A", "prompt": "Evaluate 5³.", "keys": "5 [x³]", "yx": "Y:0 | X:125", "ans": "125"},
                    {"num": 5, "part": "B", "prompt": "Write 2⁵ as repeated multiplication and find its value.", "keys": "2 [ENTER] 5 [g][yˣ]", "yx": "Y:2 | X:5", "ans": "32"},
                    {"num": 6, "part": "B", "prompt": "Evaluate 6⁴.", "keys": "6 [ENTER] 4 [g][yˣ]", "yx": "Y:6 | X:4", "ans": "1,296"},
                    {"num": 7, "part": "B", "prompt": "Evaluate 10⁴ and 1⁴. How does the exponent relate to the number of zeros in a power of 10?", "keys": "10 [ENTER] 4 [g][yˣ]", "yx": "Y:10 | X:4", "ans": "10,000 (4 zeros) and 1"},
                    {"num": 8, "part": "B", "prompt": "Error Analysis: Mia wrote 2⁴ = 8 because 2 × 4 = 8. Describe and correct her error.", "keys": "2 [ENTER] 4 [g][yˣ]", "yx": "Y:2 | X:4", "ans": "16 (2×2×2×2 = 16)"},
                    {"num": 9, "part": "C", "prompt": "Five-Stage Compound Pulley: Each stage of a rescue pulley doubles a crew's pulling force. With 5 stages, the multiplier is 2⁵. If a crew pulls with 3 kN of force, what total force (3 × 2⁵) does the hoist lift?", "keys": "2 [ENTER] 5 [g][yˣ] 3 [×]", "yx": "Y:32 | X:3", "ans": "96 kN (3 × 32)"},
                    {"num": 10, "part": "C", "prompt": "Polar Research Station Habitat: A modular Arctic station is assembled from cubic rooms measuring 2 m on each edge (2³ m³ each). What is the volume of 1 cubic room, and of 8 rooms?", "keys": "2 [x³] 8 [×]", "yx": "Y:8 | X:8", "ans": "8 m³ per room; 64 m³ total"}
                ]
            },
            {
                "day_num": 3,
                "sec_num": "1.3",
                "title": "Order of Operations",
                "big_ideas_ref": "Big Ideas Grade 6, Section 1.3 (Order of Operations)",
                "ccss": "CCSS.MATH.6.EE.A.1",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "two_room",
                "diagram_data": {"room1": "8 + 4 = 12", "room2": "9 - 3 = 6", "op": "×", "res": "72", "caption": "Group 1 (8 + 4 = 12) × Group 2 (9 - 3 = 6) = 12 × 6 = 72!"},
                "concept": "Big Ideas Order of Operations (PEMDAS): (1) Evaluate expressions inside grouping symbols (), [], or fraction bars first; (2) Evaluate powers; (3) Multiply and divide from left to right; (4) Add and subtract from left to right.",
                "examples": [
                    {
                        "title": "Example 1: Grouping Symbols & Order of Operations",
                        "problem": "Evaluate (8 + 4) × (9 - 3).",
                        "block_step": "First evaluate inside each set of parentheses: 8 + 4 = 12 and 9 - 3 = 6. Then multiply: 12 × 6 = 72.",
                        "keys": ["8", "ENTER", "4", "+", "9", "ENTER", "3", "-", "×"],
                        "stack_y": "12 (Group 1)",
                        "stack_x": "6 (Group 2)",
                        "ans": "72",
                        "note": "(8 + 4) × (9 - 3) = 12 × 6 = 72!"
                    },
                    {
                        "title": "Example 2: Exponents & Multi-Step Order of Operations",
                        "problem": "Evaluate 40 - 3 × (2 + 3)² ÷ 5.",
                        "block_step": "Parentheses: (2+3)=5. Exponent: 5²=25. Multiply/Divide left-to-right: 3×25=75, 75÷5=15. Subtract: 40-15=25.",
                        "keys": ["40", "ENTER", "3", "ENTER", "2", "ENTER", "3", "+", "x²", "×", "5", "÷", "-"],
                        "stack_y": "40",
                        "stack_x": "15",
                        "ans": "25",
                        "note": "40 - 3(25) ÷ 5 = 40 - 75 ÷ 5 = 40 - 15 = 25!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Evaluate 5 + 2 × 3.", "keys": "5 [ENTER] 2 [ENTER] 3 [×] [+]", "yx": "Y:5 | X:6", "ans": "11"},
                    {"num": 2, "part": "A", "prompt": "Evaluate (14 + 6) ÷ (7 - 2).", "keys": "14 [ENTER] 6 [+] 7 [ENTER] 2 [-] [÷]", "yx": "Y:20 | X:5", "ans": "4"},
                    {"num": 3, "part": "A", "prompt": "Evaluate 30 - 4 × 6.", "keys": "30 [ENTER] 4 [ENTER] 6 [×] [-]", "yx": "Y:30 | X:24", "ans": "6"},
                    {"num": 4, "part": "A", "prompt": "Evaluate (9 + 3) × (15 - 8).", "keys": "9 [ENTER] 3 [+] 15 [ENTER] 8 [-] [×]", "yx": "Y:12 | X:7", "ans": "84"},
                    {"num": 5, "part": "B", "prompt": "Evaluate 50 - (3 + 4)².", "keys": "50 [ENTER] 3 [ENTER] 4 [+] [x²] [-]", "yx": "Y:50 | X:49", "ans": "1"},
                    {"num": 6, "part": "B", "prompt": "Evaluate 120 - 4 × (3 + 2)².", "keys": "120 [ENTER] 4 [ENTER] 3 [ENTER] 2 [+] [x²] [×] [-]", "yx": "Y:120 | X:100", "ans": "20"},
                    {"num": 7, "part": "B", "prompt": "Evaluate the fraction-bar expression (48 - 4 × 6) / (3 + 2 × 4.5).", "keys": "48 [ENTER] 4 [ENTER] 6 [×] [-] 3 [ENTER] 2 [ENTER] 4.5 [×] [+] [÷]", "yx": "Y:24 | X:12", "ans": "2 (24 ÷ 12)"},
                    {"num": 8, "part": "B", "prompt": "Evaluate 3³ + 15 ÷ 3 - 2 × 4.", "keys": "3 [x³] 15 [ENTER] 3 [÷] [+] 2 [ENTER] 4 [×] [-]", "yx": "Y:32 | X:8", "ans": "24"},
                    {"num": 9, "part": "C", "prompt": "Claw-Bot Robotics Kit: A team orders 5 high-torque servos at $12 each and 4 bumper sensors at $8 each. What is the total cost of the parts?", "keys": "5 [ENTER] 12 [×] 4 [ENTER] 8 [×] [+]", "yx": "Y:60 | X:32", "ans": "$92 (60 + 32)"},
                    {"num": 10, "part": "C", "prompt": "3D-Printed Mini-Drone Fundraiser: A maker club sells 45 mini-drone frames at $2 each and subtracts $28 for PLA filament spools. What is the club's net profit?", "keys": "45 [ENTER] 2 [×] 28 [-]", "yx": "Y:90 | X:28", "ans": "$62 (90 - 28)"}
                ]
            },
            {
                "day_num": 4,
                "sec_num": "1.4",
                "title": "Prime Factorization",
                "big_ideas_ref": "Big Ideas Grade 6, Section 1.4 (Prime Factorization)",
                "ccss": "CCSS.MATH.6.NS.B.4",
                "kit_id": "PRIME-01",
                "kit_name": "Prime Factor Studio",
                "asset_png": "prime_studio_comparator_stage.png",
                "diagram_type": "prime_tower",
                "diagram_data": {"num": 60, "blocks": [2, 2, 3, 5], "caption": "Tower 60 = [2] + [2] + [3] + [5]. Rearranging order never changes tower height!"},
                "concept": "In Big Ideas Math, a Factor Tree or Division Ladder splits a composite number until every branch ends at a prime number. In the Prime Factor Studio (PRIME-01), block heights are logarithmic, so stacking [2]+[2]+[3]+[5] always reaches the exact 60 mark whether you split 60 as 6 × 10 or 4 × 15.",
                "examples": [
                    {
                        "title": "Example 1: Factor Tree & Division Ladder for 60",
                        "problem": "Write the prime factorization of 60 using exponents.",
                        "block_step": "Split 60 into 6 × 10 (or 4 × 15): both factor trees end at two 2s, one 3, and one 5, matching the [2]+[2]+[3]+[5] Prime Tower!",
                        "keys": ["60", "g", "FACT"],
                        "stack_y": "60 = 6×10",
                        "stack_x": "2² × 3 × 5",
                        "ans": "60 = 2² × 3 × 5",
                        "note": "Write prime factors in increasing order using exponents!"
                    },
                    {
                        "title": "Example 2: Finding a Number from Its Prime Factorization",
                        "problem": "Which whole number has the prime factorization 2³ × 3 × 5?",
                        "block_step": "Evaluate the prime power 2³ = 8, then multiply 8 × 3 × 5 = 120 (or pair 2 × 5 = 10 first: 12 × 10 = 120).",
                        "keys": ["2", "x³", "3", "×", "5", "×"],
                        "stack_y": "24",
                        "stack_x": "5 -> 120",
                        "ans": "120",
                        "note": "Pairing 2 × 5 = 10 makes mental multiplication super fast!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Write the prime factorization of 12 using exponents.", "keys": "12 [g][FACT]", "yx": "Y:0 | X:12", "ans": "2² × 3"},
                    {"num": 2, "part": "A", "prompt": "Write the prime factorization of 36 using exponents.", "keys": "36 [g][FACT]", "yx": "Y:0 | X:36", "ans": "2² × 3²"},
                    {"num": 3, "part": "A", "prompt": "Determine whether 29 and 91 are prime or composite. If composite, write the prime factorization.", "keys": "29 [PRIME], 91 [g][FACT]", "yx": "91 = 7×13", "ans": "29 is prime; 91 is composite (7 × 13)"},
                    {"num": 4, "part": "A", "prompt": "Write the prime factorization of 45.", "keys": "45 [g][FACT]", "yx": "Y:0 | X:45", "ans": "3² × 5"},
                    {"num": 5, "part": "B", "prompt": "Armory Master Key: Write the prime factorization of 72 using two different factor trees (starting with 8 × 9 and 6 × 12).", "keys": "72 [g][FACT]", "yx": "Y:0 | X:72", "ans": "2³ × 3²"},
                    {"num": 6, "part": "B", "prompt": "Write the prime factorization of 84.", "keys": "84 [g][FACT]", "yx": "Y:0 | X:84", "ans": "2² × 3 × 7"},
                    {"num": 7, "part": "B", "prompt": "Citadel Gate Key: Write the prime factorization of 210.", "keys": "210 [g][FACT]", "yx": "Y:0 | X:210", "ans": "2 × 3 × 5 × 7"},
                    {"num": 8, "part": "B", "prompt": "High Tower Vault: Write the prime factorization of 504 using exponents.", "keys": "504 [g][FACT]", "yx": "Y:0 | X:504", "ans": "2³ × 3² × 7"},
                    {"num": 9, "part": "C", "prompt": "Arabian Nights Mystery Number: Factor 1,001 into its three prime factors.", "keys": "1001 [g][FACT]", "yx": "Y:0 | X:1001", "ans": "7 × 11 × 13"},
                    {"num": 10, "part": "C", "prompt": "Base-60 Ancient Astronomer Number: There are 3,600 seconds in 1 hour. Write the prime factorization of 3,600 using exponents.", "keys": "3600 [g][FACT]", "yx": "Y:0 | X:3600", "ans": "2⁴ × 3² × 5²"}
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
                "diagram_data": {"a": 20, "b": 50, "gcf": 10, "lcm": 100, "caption": "Venn Diagram & Prime Blocks for 20 ([2][2][5]) & 50 ([2][5][5]): Overlap = GCF 10; All Regions = LCM 100"},
                "concept": "In Big Ideas Math, a Prime Factor Venn Diagram places shared prime factors in the center overlap and remaining primes in the outer circles: multiplying the center overlap gives the GCF, and multiplying all regions together gives the LCM! Placing Prime Factor Blocks (PRIME-01) into the Venn circles makes the shared overlap and union visible.",
                "examples": [
                    {
                        "title": "Example 1: GCF & LCM of 20 and 50 with a Prime Venn Diagram",
                        "problem": "Find the greatest common factor (GCF) and least common multiple (LCM) of 20 and 50.",
                        "block_step": "20 = 2 · 2 · 5 and 50 = 2 · 5 · 5. Place shared [2] and [5] in the Venn overlap (GCF = 2 × 5 = 10). Multiply all regions: 2 × 10 × 5 = 100 (LCM)!",
                        "keys": ["20", "ENTER", "50", "GCF", "20", "ENTER", "50", "f", "LCM"],
                        "stack_y": "10 (GCF)",
                        "stack_x": "100 (LCM)",
                        "ans": "GCF = 10, LCM = 100",
                        "note": "Check: GCF × LCM = 10 × 100 = 1,000 = 20 × 50!"
                    },
                    {
                        "title": "Example 2: Real-Life GCF Grouping vs. LCM Cycles",
                        "problem": "You have 18 pretzels and 24 granola bars to make identical snack packs with none left over. What is the greatest number of packs you can make?",
                        "block_step": "18 = 2 · 3² and 24 = 2³ · 3. The shared prime factors are 2 × 3 = 6 packs (each with 3 pretzels and 4 granola bars).",
                        "keys": ["18", "ENTER", "24", "GCF"],
                        "stack_y": "18 | 24",
                        "stack_x": "6 (GCF)",
                        "ans": "6 snack packs",
                        "note": "Check: 6(3 + 4) = 18 pretzels + 24 granola bars!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the GCF and LCM of 12 and 18.", "keys": "12 [ENTER] 18 [GCF] / [f][LCM]", "yx": "Y:6 | X:36", "ans": "GCF = 6, LCM = 36"},
                    {"num": 2, "part": "A", "prompt": "Find the GCF and LCM of 8 and 12.", "keys": "8 [ENTER] 12 [GCF] / [f][LCM]", "yx": "Y:4 | X:24", "ans": "GCF = 4, LCM = 24"},
                    {"num": 3, "part": "A", "prompt": "Find the GCF and LCM of 15 and 25.", "keys": "15 [ENTER] 25 [GCF] / [f][LCM]", "yx": "Y:5 | X:75", "ans": "GCF = 5, LCM = 75"},
                    {"num": 4, "part": "A", "prompt": "Find the GCF and LCM of 14 and 35.", "keys": "14 [ENTER] 35 [GCF] / [f][LCM]", "yx": "Y:7 | X:70", "ans": "GCF = 7, LCM = 70"},
                    {"num": 5, "part": "B", "prompt": "Twin Bastions Gear Sync: Two bronze clockwork gears have 48 teeth and 72 teeth. What is the greatest common factor of their tooth counts?", "keys": "48 [ENTER] 72 [GCF]", "yx": "Y:48 | X:72", "ans": "24"},
                    {"num": 6, "part": "B", "prompt": "Water Gate Sluice Sync: Two canal lock wheels have 84 teeth and 140 teeth. Find the GCF of 84 and 140.", "keys": "84 [ENTER] 140 [GCF]", "yx": "Y:84 | X:140", "ans": "28"},
                    {"num": 7, "part": "B", "prompt": "Find the GCF and LCM of 45 and 75.", "keys": "45 [ENTER] 75 [GCF] / [f][LCM]", "yx": "Y:15 | X:225", "ans": "GCF = 15, LCM = 225"},
                    {"num": 8, "part": "B", "prompt": "Sentry Patrol Cycle: North Watch completes a patrol every 15 minutes and South Watch every 20 minutes. If they meet at the gate at midnight, in how many minutes will they meet at the gate again?", "keys": "15 [ENTER] 20 [f][LCM]", "yx": "Y:15 | X:20", "ans": "60 minutes"},
                    {"num": 9, "part": "C", "prompt": "Municipal Traffic Signals: Along an avenue, the North-South green light cycles every 45 seconds and the pedestrian walk signal cycles every 60 seconds. If both trigger together now, how many seconds pass before they trigger together again?", "keys": "45 [ENTER] 60 [f][LCM]", "yx": "Y:45 | X:60", "ans": "180 seconds (3 minutes)"},
                    {"num": 10, "part": "C", "prompt": "Workshop Kit Bags: You have 36 red gears and 48 blue gears to pack into identical kit bags with none left over. What is the greatest number of kit bags you can make, and how many gears of each color go into each bag?", "keys": "36 [ENTER] 48 [GCF]", "yx": "Y:36 | X:48", "ans": "12 bags (3 red, 4 blue per bag)"}
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
                "title": "Equivalent Fractions, Mixed Numbers & Adding/Subtracting Fractions",
                "big_ideas_ref": "Big Ideas Grade 6, Section 2.1 Prep (Equivalence, Mixed Numbers & Like/Unlike Fractions)",
                "ccss": "CCSS.MATH.6.NS.A.1",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_common_denominator.png",
                "diagram_type": "fraction_towers",
                "diagram_data": {"towers": [("1 Whole", [84], "84mm"), ("2/3", [28, 28], "56mm"), ("4/6", [14, 14, 14, 14], "56mm"), ("1/3+1/4", [28, 21], "49mm = 7/12")], "caption": "Fraction Strips (FRAC-01): 2/3 and 4/6 have equal length; 1/3 (4/12) + 1/4 (3/12) = 7/12"},
                "concept": "In Big Ideas Math, divide the numerator and denominator by their GCF to write a fraction in simplest form, and rewrite unlike fractions using their Least Common Denominator (LCD) to add or subtract. With Fraction Strips (FRAC-01, 1 Whole = 84 mm), equivalent fractions match in length, and trading 1/3 + 1/4 for twelfths shows 4/12 + 3/12 = 7/12.",
                "examples": [
                    {
                        "title": "Example 1: Simplifying Fractions",
                        "problem": "Write 12/18 in simplest form.",
                        "block_step": "Divide by GCF(12, 18) = 6: (12 ÷ 6)/(18 ÷ 6) = 2/3. Six 1/6 strips (4/6) and two 1/3 strips have the exact same 56 mm length!",
                        "keys": [".", "12", ".", "18", "ENTER", "g", "SIMP", "g", "SIMP"],
                        "stack_y": "6/9 (Step 1)",
                        "stack_x": "2/3 (Final)",
                        "ans": "2/3",
                        "note": "Dividing numerator and denominator by GCF = 6 gives 2/3 in 1 step!"
                    },
                    {
                        "title": "Example 2: Adding Unlike Fractions with the LCD",
                        "problem": "You plant 1/3 of a garden with tomatoes and 1/4 with peppers. What fraction of the garden is planted?",
                        "block_step": "LCD(3, 4) = 12. Trade 1/3 for four 1/12 strips (4/12) and 1/4 for three 1/12 strips (3/12): 4/12 + 3/12 = 7/12.",
                        "keys": [".", "1", ".", "3", "ENTER", ".", "1", ".", "4", "+"],
                        "stack_y": "4/12",
                        "stack_x": "3/12 -> 7/12",
                        "ans": "7/12 of the garden",
                        "note": "Check by subtracting: 7/12 - 3/12 = 4/12 = 1/3!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Write 8/12 in simplest form.", "keys": "[.] 8 [.] 12 [ENTER] [g][SIMP]×2", "yx": "4/6 -> 2/3", "ans": "2/3"},
                    {"num": 2, "part": "A", "prompt": "Championship Pizza Party: A team eats 48 slices from trays cut into 18ths (48/18). Write 48/18 in simplest form and as a mixed number.", "keys": "[.] 48 [.] 18 [ENTER] [g][SIMP]", "yx": "8/3 -> 2 2/3", "ans": "8/3 = 2 2/3 trays"},
                    {"num": 3, "part": "A", "prompt": "Write the mixed number 2 3/5 as an improper fraction and as a decimal.", "keys": "2 [.] 3 [.] 5 [ENTER] [f][d/c]", "yx": "13/5 | 2.6", "ans": "13/5 and 2.6"},
                    {"num": 4, "part": "A", "prompt": "Pizza Slice Inventory: After a festival, 23 sixth-slices (23/6) remain. How many whole pizzas and leftover sixth-slices can be boxed?", "keys": "[.] 23 [.] 6 [ENTER]", "yx": "3 5/6", "ans": "3 5/6 pizzas (3 whole, 5 sixths)"},
                    {"num": 5, "part": "B", "prompt": "Add 1/2 + 1/3. Write the sum in simplest form.", "keys": "[.] 1 [.] 2 [ENTER] [.] 1 [.] 3 [+]", "yx": "Y:1/2 | X:1/3", "ans": "5/6"},
                    {"num": 6, "part": "B", "prompt": "Woodshop Sealant Blend: A boatbuilder mixes 3/4 gallon of pine resin with 2/5 gallon of linseed oil. How many gallons of sealant are in the bucket?", "keys": "[.] 3 [.] 4 [ENTER] [.] 2 [.] 5 [+]", "yx": "Y:3/4 | X:2/5", "ans": "1 3/20 gallons (23/20)"},
                    {"num": 7, "part": "B", "prompt": "Lookout Balcony Rail: A carpenter welds a 1 1/2-foot bracket to a 2 1/3-foot rail. What is the combined length?", "keys": "1 [.] 1 [.] 2 [ENTER] 2 [.] 1 [.] 3 [+]", "yx": "Y:1 1/2 | X:2 1/3", "ans": "3 5/6 feet"},
                    {"num": 8, "part": "B", "prompt": "Sawing a Diagonal Cross-Brace: A timber frame carpenter trims 2 3/4 feet from a 5 1/3-foot cedar beam. How long is the remaining beam?", "keys": "5 [.] 1 [.] 3 [ENTER] 2 [.] 3 [.] 4 [-]", "yx": "Y:5 1/3 | X:2 3/4", "ans": "2 7/12 feet"},
                    {"num": 9, "part": "C", "prompt": "Zeno's Rope Ladder: A climber scales 1/2 of a cliff in Hour 1, 1/4 in Hour 2, and 1/8 in Hour 3. What total fraction of the cliff has she climbed, and what fraction remains?", "keys": "[.] 1 [.] 2 [ENTER] [.] 1 [.] 4 [+] [.] 1 [.] 8 [+]", "yx": "Y:3/4 | X:1/8", "ans": "7/8 climbed; 1/8 remains"},
                    {"num": 10, "part": "C", "prompt": "Gallery Stucco Mix: An artisan blends 3 1/2 pints of lime putty with 1 3/4 pints of marble dust. How many pints of plaster does this make?", "keys": "3 [.] 1 [.] 2 [ENTER] 1 [.] 3 [.] 4 [+]", "yx": "Y:3.5 | X:1.75", "ans": "5 1/4 pints"}
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
                "diagram_data": {"towers": [("3/4 Tower", [21, 21, 21], "63.0mm"), ("1/2 of 3/4", [10.5, 10.5, 10.5], "31.5mm = 3/8")], "caption": "2D Area Model & Fraction Strips: 1/2 of 3/4 = 3/8!"},
                "concept": "In Big Ideas Math, multiply fractions by multiplying the numerators and multiplying the denominators: (a/b) × (c/d) = (ac)/(bd). For mixed numbers, write each mixed number as an improper fraction first, and divide out common factors before multiplying. Partitioning a 3/4 Fraction Strip (FRAC-01) in half visually shows why 1/2 of 3/4 is 3/8.",
                "examples": [
                    {
                        "title": "Example 1: Multiplying Proper Fractions (1/2 × 3/4)",
                        "problem": "Find 1/2 × 3/4.",
                        "block_step": "Multiply numerators (1 × 3 = 3) and denominators (2 × 4 = 8) -> 3/8. On an area grid or fraction strip, half of 3 fourths is 3 eighths!",
                        "keys": [".", "1", ".", "2", "ENTER", ".", "3", ".", "4", "×"],
                        "stack_y": "1/2",
                        "stack_x": "3/4",
                        "ans": "3/8",
                        "note": "(1 × 3) / (2 × 4) = 3/8!"
                    },
                    {
                        "title": "Example 2: Multiplying Mixed Numbers (2 2/3 × 1 1/2)",
                        "problem": "Multiply 2 2/3 × 1 1/2.",
                        "block_step": "Rewrite as improper fractions: 8/3 × 3/2. Divide out the common factors of 3 and 2 to get 4/1 × 1/1 = 4!",
                        "keys": ["2", ".", "2", ".", "3", "ENTER", "1", ".", "1", ".", "2", "×"],
                        "stack_y": "2 2/3 (8/3)",
                        "stack_x": "1 1/2 (3/2)",
                        "ans": "4",
                        "note": "Cross-canceling 8/3 × 3/2 simplifies before you multiply!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find 1/2 × 2/3. Write the product in simplest form.", "keys": "[.] 1 [.] 2 [ENTER] [.] 2 [.] 3 [×]", "yx": "Y:1/2 | X:2/3", "ans": "1/3"},
                    {"num": 2, "part": "A", "prompt": "Multiply 2/3 × 3/4. Divide out common factors before multiplying.", "keys": "[.] 2 [.] 3 [ENTER] [.] 3 [.] 4 [×]", "yx": "Y:2/3 | X:3/4", "ans": "1/2"},
                    {"num": 3, "part": "A", "prompt": "Multiply 3/5 × 5/9.", "keys": "[.] 3 [.] 5 [ENTER] [.] 5 [.] 9 [×]", "yx": "Y:3/5 | X:5/9", "ans": "1/3"},
                    {"num": 4, "part": "A", "prompt": "Cranberry Trail Mix: A recipe for 16 cups of trail mix is 3/8 dried cranberries. How many cups of cranberries are in the batch?", "keys": "16 [ENTER] [.] 3 [.] 8 [×]", "yx": "Y:16 | X:3/8", "ans": "6 cups"},
                    {"num": 5, "part": "B", "prompt": "Multiply 1 3/4 × 2 2/7.", "keys": "1 [.] 3 [.] 4 [ENTER] 2 [.] 2 [.] 7 [×]", "yx": "Y:7/4 | X:16/7", "ans": "4"},
                    {"num": 6, "part": "B", "prompt": "Multiply 2 1/4 × 1 1/3.", "keys": "2 [.] 1 [.] 4 [ENTER] 1 [.] 1 [.] 3 [×]", "yx": "Y:9/4 | X:4/3", "ans": "3"},
                    {"num": 7, "part": "B", "prompt": "High-Energy Trail Cookies: One batch of trail cookies uses 2 1/4 cups of rolled oats. How many cups of oats are needed to bake 4 batches?", "keys": "2 [.] 1 [.] 4 [ENTER] 4 [×]", "yx": "Y:2 1/4 | X:4", "ans": "9 cups"},
                    {"num": 8, "part": "B", "prompt": "Without calculating, is 5 × 2/3 greater than 5 or less than 5? Explain why, then find the product.", "keys": "5 [ENTER] [.] 2 [.] 3 [×]", "yx": "Y:5 | X:2/3", "ans": "3 1/3 (Less than 5 because 2/3 < 1)"},
                    {"num": 9, "part": "C", "prompt": "Light-Rail Blueprint Scale: On an transit map, 1 inch represents 3 1/2 miles. If a proposed rail line measures 4 1/4 inches on the map, how many miles long is the actual line?", "keys": "3 [.] 1 [.] 2 [ENTER] 4 [.] 1 [.] 4 [×]", "yx": "Y:7/2 | X:17/4", "ans": "14 7/8 miles (119/8)"},
                    {"num": 10, "part": "C", "prompt": "Three-Stage Planetary Gear Hub: Three reduction gears step down rotational speed by factors of 1/2, 2/3, and 3/4. What fraction of the input speed comes out of the final stage?", "keys": "[.] 1 [.] 2 [ENTER] [.] 2 [.] 3 [×] [.] 3 [.] 4 [×]", "yx": "Y:1/3 | X:3/4", "ans": "1/4 of the input speed"}
                ]
            },
            {
                "day_num": 8,
                "sec_num": "2.3",
                "title": "Dividing Fractions & Mixed Numbers",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 2.2 & 2.3 (Dividing Fractions and Mixed Numbers)",
                "ccss": "CCSS.MATH.6.NS.A.1",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_common_denominator.png",
                "diagram_type": "fraction_towers",
                "diagram_data": {"towers": [("3/4 Tower", [21, 21, 21], "63.0mm"), ("Six 1/8s", [10.5]*6, "6 × 10.5mm = 63mm")], "caption": "3/4 ÷ 1/8: Six 1/8 strips fit inside a 3/4 strip (6/8 ÷ 1/8 = 6)!"},
                "concept": "In Big Ideas Math, you can divide fractions in two ways: (1) Multiply by the Reciprocal of the divisor: (a/b) ÷ (c/d) = (a/b) × (d/c), or (2) Rewrite both fractions with a Common Denominator and divide their numerators! Placing 1/8 Fraction Strips (FRAC-01) alongside a 3/4 strip shows why six 1/8s fit inside 3/4.",
                "examples": [
                    {
                        "title": "Example 1: Dividing Fractions (3/4 ÷ 1/8)",
                        "problem": "Find 3/4 ÷ 1/8.",
                        "block_step": "Multiply by the reciprocal of 1/8 (which is 8/1): (3/4) × (8/1) = 24/4 = 6. Or use common denominators: 6/8 ÷ 1/8 = 6 ÷ 1 = 6!",
                        "keys": [".", "3", ".", "4", "ENTER", ".", "1", ".", "8", "f", "1/x", "×"],
                        "stack_y": "3/4 (Kept)",
                        "stack_x": "8 (Reciprocal)",
                        "ans": "6",
                        "note": "Six 1/8 strips have the exact same length as three 1/4 strips!"
                    },
                    {
                        "title": "Example 2: Dividing Mixed Numbers (4 1/2 ÷ 3/4)",
                        "problem": "A 4 1/2-foot braided cable is snipped into 3/4-foot loops. How many loops can be cut?",
                        "block_step": "Rewrite 4 1/2 as 9/2. Multiply by the reciprocal of 3/4 (4/3): (9/2) × (4/3) = 36/6 = 6 loops!",
                        "keys": ["4", ".", "1", ".", "2", "ENTER", ".", "3", ".", "4", "÷"],
                        "stack_y": "4 1/2 (9/2)",
                        "stack_x": "3/4",
                        "ans": "6 loops",
                        "note": "Check: 6 × 3/4 = 18/4 = 4 1/2 feet!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Divide 1/2 ÷ 1/4.", "keys": "[.] 1 [.] 2 [ENTER] [.] 1 [.] 4 [÷]", "yx": "Y:1/2 | X:1/4", "ans": "2"},
                    {"num": 2, "part": "A", "prompt": "Divide 2/3 ÷ 1/6.", "keys": "[.] 2 [.] 3 [ENTER] [.] 1 [.] 6 [÷]", "yx": "Y:2/3 | X:1/6", "ans": "4"},
                    {"num": 3, "part": "A", "prompt": "Divide 5/6 ÷ 5/12. Write the quotient in simplest form.", "keys": "[.] 5 [.] 6 [ENTER] [.] 5 [.] 12 [f][1/x] [×]", "yx": "Y:5/6 | X:12/5", "ans": "2"},
                    {"num": 4, "part": "A", "prompt": "Divide 6 ÷ 3/4.", "keys": "6 [ENTER] [.] 3 [.] 4 [÷]", "yx": "Y:6 | X:3/4", "ans": "8"},
                    {"num": 5, "part": "B", "prompt": "Divide 3/4 ÷ 2/5. Write the answer as a mixed number.", "keys": "[.] 3 [.] 4 [ENTER] [.] 2 [.] 5 [÷]", "yx": "Y:3/4 | X:2/5", "ans": "1 7/8 (15/8)"},
                    {"num": 6, "part": "B", "prompt": "Quarter-Batch Polymer Clay: A sculpture recipe uses 3 1/2 cups of base clay. If you divide the recipe equally into 4 mini-batches, how much clay is in each mini-batch?", "keys": "3 [.] 1 [.] 2 [ENTER] 4 [÷]", "yx": "Y:3 1/2 | X:4", "ans": "7/8 cup"},
                    {"num": 7, "part": "B", "prompt": "Ceramic Bike Frame Polish: A mechanic has 2/3 liter of polish. Each bike frame requires 1/4 liter. How many frames (including fraction of a frame) can be coated?", "keys": "[.] 2 [.] 3 [ENTER] [.] 1 [.] 4 [÷]", "yx": "Y:2/3 | X:1/4", "ans": "2 2/3 bike frames"},
                    {"num": 8, "part": "B", "prompt": "Divide 5 1/4 ÷ 1 3/4 and check your answer by multiplying.", "keys": "5 [.] 1 [.] 4 [ENTER] 1 [.] 3 [.] 4 [÷]", "yx": "Y:5 1/4 | X:1 3/4", "ans": "3"},
                    {"num": 9, "part": "C", "prompt": "Oak Crate Slats: A carpenter saws an 8-foot (96-inch) oak board into crate slats that are each 18 1/2 inches long. How many full slats can be sawed from the board?", "keys": "96 [ENTER] 18 [.] 1 [.] 2 [÷]", "yx": "Y:96 | X:18.5", "ans": "5 full slats (5 7/37 -> 3 1/2 in left)"},
                    {"num": 10, "part": "C", "prompt": "Smoothie Pitcher Servings: A 3 3/4-cup pitcher of berry smoothie is poured into 5/8-cup glasses. How many glasses does it fill?", "keys": "3 [.] 3 [.] 4 [ENTER] [.] 5 [.] 8 [÷]", "yx": "Y:15/4 | X:5/8", "ans": "6 glasses"}
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
                "asset_png": "place_value_ortho_steps.png",
                "diagram_type": "place_value",
                "diagram_data": {"num": "14.85", "ip": "14", "fp": "0.85", "caption": "Line up decimal points vertically for + and -; count total decimal places for ×!"},
                "concept": "To add or subtract decimals, line up the decimal points vertically so ones, tenths, and hundredths align, and annex trailing zeros as needed. To multiply decimals, multiply as whole numbers and count the total number of decimal places in the factors—always checking with a whole-number front-end estimate.",
                "examples": [
                    {
                        "title": "Example 1: Adding & Subtracting Decimals Vertically",
                        "problem": "Find 14.6 + 3.85 and check by subtracting.",
                        "block_step": "Line up the decimal points and annex a zero (14.60 + 3.85). Add hundredths, tenths, and wholes to get 18.45.",
                        "keys": ["14.6", "ENTER", "3.85", "+", "f", "LASTX", "-"],
                        "stack_y": "14.6",
                        "stack_x": "3.85 -> 18.45",
                        "ans": "18.45",
                        "note": "Check: 18.45 - 3.85 = 14.60!"
                    },
                    {
                        "title": "Example 2: Multiplying Decimals + Estimate Check",
                        "problem": "A melon weighs 4.5 pounds and costs $1.80 per pound. Find the total cost.",
                        "block_step": "Estimate first: 5 × $2 = $10. Multiply 45 × 18 = 810, then place 2 decimal places -> $8.10.",
                        "keys": ["4.5", "ENTER", "1.80", "×"],
                        "stack_y": "4.5",
                        "stack_x": "1.80 -> 8.10",
                        "ans": "$8.10",
                        "note": "Distributive check: 4($1.80) + 0.5($1.80) = $7.20 + $0.90 = $8.10!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Telescope Mirror Calibration: An optical grinding machine adds shims of 345 mm, 0.6 mm, and 0.07 mm. What is the combined thickness?", "keys": "345 [ENTER] 0.6 [+] 0.07 [+]", "yx": "345.67", "ans": "345.67 mm"},
                    {"num": 2, "part": "A", "prompt": "Find 12.8 + 4.75 and check by subtracting.", "keys": "12.8 [ENTER] 4.75 [+]", "yx": "Y:12.8 | X:4.75", "ans": "17.55"},
                    {"num": 3, "part": "A", "prompt": "Find 20 - 8.65.", "keys": "20 [ENTER] 8.65 [-]", "yx": "Y:20 | X:8.65", "ans": "11.35"},
                    {"num": 4, "part": "A", "prompt": "Multiply 4.5 × 0.6.", "keys": "4.5 [ENTER] 0.6 [×]", "yx": "Y:4.5 | X:0.6", "ans": "2.7"},
                    {"num": 5, "part": "B", "prompt": "Evaluate 25.4 - 9.86 + 3.2.", "keys": "25.4 [ENTER] 9.86 [-] 3.2 [+]", "yx": "Y:15.54 | X:3.2", "ans": "18.74"},
                    {"num": 6, "part": "B", "prompt": "Multiply 3.6 × 2.25 and check that your answer is reasonable using a whole-number estimate.", "keys": "3.6 [ENTER] 2.25 [×]", "yx": "Y:3.6 | X:2.25", "ans": "8.1 (Estimate: 4 × 2 = 8)"},
                    {"num": 7, "part": "B", "prompt": "Multiply 0.15 × 0.4. Write the product as a decimal and as a simplified fraction.", "keys": "0.15 [ENTER] 0.4 [×] [FDISP]", "yx": "Y:0.15 | X:0.4", "ans": "0.06 (3/50)"},
                    {"num": 8, "part": "B", "prompt": "Bioplastic Funnel Mass: A 3D-printed bioplastic funnel has a volume of 28.86 cm³ and a density of 1.24 g/cm³. What is its mass in grams (rounded to the nearest hundredth)?", "keys": "28.86 [ENTER] 1.24 [×]", "yx": "Y:28.86 | X:1.24", "ans": "35.79 g (35.7864)"},
                    {"num": 9, "part": "C", "prompt": "You pay with a $20 bill for an $8.75 burger and a $4.60 smoothie. How much change should you receive?", "keys": "20 [ENTER] 8.75 [ENTER] 4.60 [+] [-]", "yx": "Y:20 | X:13.35", "ans": "$6.65"},
                    {"num": 10, "part": "C", "prompt": "Geodesic Radome Strut Tubing: A dome requires 30 struts of 1.20 m, 40 struts of 1.35 m, and 50 struts of 1.42 m. How many meters of aluminum tubing are required in all?", "keys": "30 [ENTER] 1.20 [×] 40 [ENTER] 1.35 [×] [+] 50 [ENTER] 1.42 [×] [+]", "yx": "36 + 54 + 71", "ans": "161 meters"}
                ]
            },
            {
                "day_num": 10,
                "sec_num": "2.5",
                "title": "Dividing Whole Numbers and Decimals",
                "big_ideas_ref": "Big Ideas Grade 6, Section 2.6 (Dividing Decimals)",
                "ccss": "CCSS.MATH.6.NS.B.3",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "place_value_ortho_steps.png",
                "diagram_type": "place_value",
                "diagram_data": {"num": "15 ÷ 4", "ip": "3 R 3", "fp": "3.75 = 3 3/4", "caption": "Shift the decimal point in both divisor and dividend by the same power of 10!"},
                "concept": "When dividing by a decimal (such as 6.75 ÷ 0.25), multiply both the divisor and the dividend by the same power of 10 (shift both decimal points the same number of places to the right) so the divisor becomes a whole number (675 ÷ 25 = 27).",
                "examples": [
                    {
                        "title": "Example 1: Expressing Quotients as Decimals & Mixed Numbers",
                        "problem": "Divide 23 ÷ 4. Write the quotient as a remainder, a mixed number, and an exact decimal.",
                        "block_step": "23 ÷ 4 gives 5 with 3 left over (5 R 3). Dividing the leftover 3 by 4 gives 3/4 = 0.75, so 23 ÷ 4 = 5 3/4 = 5.75.",
                        "keys": ["23", "ENTER", "4", "÷", "FDISP", "f", "d/c"],
                        "stack_y": "23 | 4",
                        "stack_x": "5.75 <-> 5 3/4",
                        "ans": "5 R 3 = 5 3/4 = 5.75",
                        "note": "Annexing .00 (23.00 ÷ 4) continues long division to 5.75!"
                    },
                    {
                        "title": "Example 2: Dividing by a Decimal (6.75 ÷ 0.25)",
                        "problem": "Evaluate 6.75 ÷ 0.25 and explain why the quotient is greater than 6.75.",
                        "block_step": "Multiply both numbers by 100 (shift 2 places right): 675 ÷ 25 = 27. Since 0.25 is less than 1, 27 quarters fit in $6.75!",
                        "keys": ["6.75", "ENTER", "0.25", "÷", "f", "LASTX", "×"],
                        "stack_y": "6.75",
                        "stack_x": "0.25 -> 27",
                        "ans": "27",
                        "note": "Check: 27 × 0.25 = 6.75!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Write 39 ÷ 8 as (a) a quotient with remainder, (b) a mixed number, and (c) a decimal.", "keys": "39 [ENTER] 8 [÷] [FDISP]", "yx": "Y:39 | X:8", "ans": "4 R 7, 4 7/8, and 4.875"},
                    {"num": 2, "part": "A", "prompt": "Divide 18.4 ÷ 8.", "keys": "18.4 [ENTER] 8 [÷]", "yx": "Y:18.4 | X:8", "ans": "2.3"},
                    {"num": 3, "part": "A", "prompt": "How many quarters ($0.25) are in $11.25?", "keys": "11.25 [ENTER] 0.25 [÷]", "yx": "Y:11.25 | X:0.25", "ans": "45 quarters"},
                    {"num": 4, "part": "A", "prompt": "Divide 7.2 ÷ 0.9 and check by multiplying.", "keys": "7.2 [ENTER] 0.9 [÷]", "yx": "Y:7.2 | X:0.9", "ans": "8"},
                    {"num": 5, "part": "B", "prompt": "Divide 15.6 ÷ 0.12.", "keys": "15.6 [ENTER] 0.12 [÷]", "yx": "Y:15.6 | X:0.12", "ans": "130"},
                    {"num": 6, "part": "B", "prompt": "Divide 9.45 ÷ 1.5. Write the answer as a decimal and as a mixed number in simplest form.", "keys": "9.45 [ENTER] 1.5 [÷] [FDISP]", "yx": "Y:9.45 | X:1.5", "ans": "6.3 (6 3/10)"},
                    {"num": 7, "part": "B", "prompt": "Team Material Budget Split: Six engineering students split a $124.80 hardware store bill equally. How much does each student pay?", "keys": "124.80 [ENTER] 6 [÷]", "yx": "Y:124.80 | X:6", "ans": "$20.80"},
                    {"num": 8, "part": "B", "prompt": "Error Analysis: Leo says 4.8 ÷ 0.2 = 0.24. Use estimation or multiplication to explain and correct his error.", "keys": "4.8 [ENTER] 0.2 [÷]", "yx": "Y:4.8 | X:0.2", "ans": "24 (24 × 0.2 = 4.8)"},
                    {"num": 9, "part": "C", "prompt": "Track Race Laps: A runner completes a 4.5-mile race on a track where each lap is 0.75 mile. How many laps is the race?", "keys": "4.5 [ENTER] 0.75 [÷]", "yx": "Y:4.5 | X:0.75", "ans": "6 laps"},
                    {"num": 10, "part": "C", "prompt": "Sports Drink Case: A 6-pack of sports drinks costs $7.50. What is the price of 1 bottle, and how many bottles can you buy with $20.00?", "keys": "7.50 [ENTER] 6 [÷] -> 1.25; 20 [ENTER] 1.25 [÷]", "yx": "Y:20 | X:1.25", "ans": "$1.25 per bottle; 16 bottles"}
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
        "kit_summary": "Fraction Studio (FRAC-01) + Place Value Studio (PLACE-01)",
        "hero_png": "fraction_studio_twin_comparator.png",
        "coach_misconception": "Students confuse Part-to-Part (3:2) with Part-to-Whole (3/5), add instead of multiply in ratio tables, divide unit rates upside-down, and memorize 6 disconnected rules for moving decimal points in percents.",
        "coach_remediation": "Use equal Fraction Studio blocks as physical Tape Diagram units, step through ratio tables rhythmically with [g] [REP], use [x⇄y] when unit-rate division is entered upside-down, and use [f] [%] + [FDISP] to show Fraction/Decimal/Percent are three costumes of one number.",
        "sections": [
            {
                "day_num": 11,
                "sec_num": "3.1",
                "title": "Ratios and Tape Diagrams",
                "big_ideas_ref": "Big Ideas Grade 6, Section 3.1 & 3.2 (Ratios and Tape Diagrams)",
                "ccss": "CCSS.MATH.6.RP.A.1",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_twin_comparator.png",
                "diagram_type": "ratio_tape",
                "diagram_data": {"a": 3, "b": 2, "unit_val": 4, "label_a": "Part A (3×4=12)", "label_b": "Part B (2×4=8)", "caption": "Tape Diagram with Equal Fraction Strips: 3 boxes : 2 boxes (5 boxes total). If total = 20, each box = 4!"},
                "concept": "A ratio compares two quantities (a to b, a:b, or a/b). In a Tape Diagram, each equal box (or equal-length Fraction Strip in FRAC-01) represents the same unit amount. For a 3:2 ratio, 3 equal strips + 2 equal strips = 5 total strips, making the Part-to-Whole ratios 3:5 and 2:5.",
                "examples": [
                    {
                        "title": "Example 1: Part-to-Part vs. Part-to-Whole Ratios",
                        "problem": "A robotics team has 12 builders and 8 programmers. Write the simplified Part-to-Part and Part-to-Whole ratios.",
                        "block_step": "Divide 12 and 8 by GCF = 4 to get 3 builders : 2 programmers. Since 3 + 2 = 5 parts total, builders to total is 3 : 5.",
                        "keys": ["12", "ENTER", "8", "g", "a:b"],
                        "stack_y": "3 (Part 1)",
                        "stack_x": "2 (Part 2)",
                        "ans": "Part-to-Part = 3:2; Part-to-Whole = 3:5",
                        "note": "Always check whether the question asks for Part-to-Part or Part-to-Whole!"
                    },
                    {
                        "title": "Example 2: Solving a Tape Diagram",
                        "problem": "The ratio of wins to losses is 5:3. If a team played 32 games in all, how many games did they win?",
                        "block_step": "5 win boxes + 3 loss boxes = 8 total boxes. Divide 32 ÷ 8 = 4 games per box. Wins = 5 × 4 = 20!",
                        "keys": ["32", "ENTER", "5", "ENTER", "3", "+", "÷", "5", "×"],
                        "stack_y": "4 (Per Box)",
                        "stack_x": "5 -> 20",
                        "ans": "20 wins (and 12 losses)",
                        "note": "Check: 20 + 12 = 32 games, and 20:12 simplifies to 5:3!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Write the ratio 12 : 18 in simplest form.", "keys": "12 [ENTER] 18 [g][a:b]", "yx": "Y:2 | X:3", "ans": "2 : 3"},
                    {"num": 2, "part": "A", "prompt": "Write the ratio 24 : 16 in simplest form.", "keys": "24 [ENTER] 16 [g][a:b]", "yx": "Y:3 | X:2", "ans": "3 : 2"},
                    {"num": 3, "part": "A", "prompt": "A pouch holds 4 red marbles and 6 blue marbles. Find the simplified ratio of red marbles to total marbles.", "keys": "4 [ENTER] 10 [g][a:b]", "yx": "Y:2 | X:5", "ans": "2 : 5"},
                    {"num": 4, "part": "A", "prompt": "In a 3:4 tape diagram, each box represents 6 items. Find the two parts and the total.", "keys": "3 [ENTER] 6 [×], 4 [ENTER] 6 [×]", "yx": "18 and 24", "ans": "18 and 24 (Total = 42)"},
                    {"num": 5, "part": "B", "prompt": "Living-Wall Hydroponic Reservoir: Nutrient solution mixes 2 parts plant concentrate with 15 parts water. How many liters of concentrate and water are in a 34-liter tank?", "keys": "34 [ENTER] 17 [÷] -> 2/part", "yx": "Y:2 | X:2,15", "ans": "4 L concentrate, 30 L water"},
                    {"num": 6, "part": "B", "prompt": "The ratio of cats to dogs at an animal shelter is 4:5. If there are 36 animals in all, how many are dogs?", "keys": "36 [ENTER] 9 [÷] 5 [×]", "yx": "Y:4 | X:5", "ans": "20 dogs"},
                    {"num": 7, "part": "B", "prompt": "The ratio of sixth graders to seventh graders in a chess club is 3:5. If there are 15 sixth graders, how many seventh graders are in the club?", "keys": "15 [ENTER] 3 [÷] 5 [×]", "yx": "Y:5 | X:5", "ans": "25 seventh graders"},
                    {"num": 8, "part": "B", "prompt": "The ratio of acoustic guitars to electric guitars in a music shop is 2:5. There are 18 more electric guitars than acoustic guitars. How many electric guitars are there?", "keys": "18 [ENTER] 3 [÷] 5 [×]", "yx": "Y:6 | X:5", "ans": "30 electric guitars (12 acoustic)"},
                    {"num": 9, "part": "C", "prompt": "Two robotics squads split 84 gears in a 4:3 ratio. How many gears does each squad receive?", "keys": "84 [ENTER] 7 [÷] -> 12/box", "yx": "Y:12 | X:4,3", "ans": "48 gears and 36 gears"},
                    {"num": 10, "part": "C", "prompt": "The ratio of gold coins to silver coins in a chest is 7:4. If there are 21 more gold coins than silver coins, how many coins are in the chest in all?", "keys": "21 [ENTER] 3 [÷] 11 [×]", "yx": "Y:7 | X:11", "ans": "77 coins total (49 gold, 28 silver)"}
                ]
            },
            {
                "day_num": 12,
                "sec_num": "3.2",
                "title": "Ratio Tables and Double Number Lines",
                "big_ideas_ref": "Big Ideas Grade 6, Section 3.3 (Ratio Tables & Double Number Lines)",
                "ccss": "CCSS.MATH.6.RP.A.3a",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "ratio_tape",
                "diagram_data": {"a": 3, "b": 7, "unit_val": 1, "label_a": "Top Row: 3 -> 6 -> 9 -> 12 -> 15", "label_b": "Bot Row: 7 -> 14 -> 21 -> 28 -> 35", "caption": "Ratio Table & Double Number Line: Multiply or add equal groups of both quantities!"},
                "concept": "In Big Ideas Math, you can find equivalent ratios in a Ratio Table or on a Double Number Line by (1) adding the base ratio quantities repeatedly, (2) multiplying or dividing both quantities by the same scale factor, or (3) scaling down to a smaller equivalent ratio and then scaling up.",
                "examples": [
                    {
                        "title": "Example 1: Ratio Table & Double Number Line",
                        "problem": "A drone flies 8 meters every 3 seconds. How far does it fly in 15 seconds?",
                        "block_step": "Since 3 × 5 = 15 seconds, multiply 8 meters × 5 = 40 meters (or jump 5 times on a double number line: 8, 16, 24, 32, 40).",
                        "keys": ["8", "g", "REP", "+", "+", "+", "+"],
                        "stack_y": "8 (Step)",
                        "stack_x": "40 (5 jumps)",
                        "ans": "40 meters",
                        "note": "Scaling both parts of 3 : 8 by ×5 gives 15 seconds : 40 meters!"
                    },
                    {
                        "title": "Example 2: Scaling Down Then Scaling Up",
                        "problem": "6 skate park tickets cost $45. At this rate, how much do 10 tickets cost?",
                        "block_step": "Divide both 6 and 45 by 3 to find 2 tickets = $15. Then multiply both by 5 to find 10 tickets = $75!",
                        "keys": ["45", "ENTER", "3", "÷", "5", "×"],
                        "stack_y": "15 (2 tix)",
                        "stack_x": "5 -> 75",
                        "ans": "$75",
                        "note": "Or find the unit price ($45 ÷ 6 = $7.50) and multiply by 10 -> $75!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Write the first 4 equivalent ratios of 4 : 9.", "keys": "4 [g][REP] [+], 9 [g][REP] [+]", "yx": "×1, ×2, ×3, ×4", "ans": "4:9, 8:18, 12:27, 16:36"},
                    {"num": 2, "part": "A", "prompt": "In a ratio table where A : B = 4 : 9, find B when A = 28.", "keys": "28 [ENTER] 4 [÷] 9 [×]", "yx": "Y:7 | X:9", "ans": "63"},
                    {"num": 3, "part": "A", "prompt": "In a ratio table where X : Y = 5 : 12, find X when Y = 60.", "keys": "60 [ENTER] 12 [÷] 5 [×]", "yx": "Y:5 | X:5", "ans": "25"},
                    {"num": 4, "part": "A", "prompt": "A laser printer prints 15 pages every 2 minutes. How many pages does it print in 8 minutes?", "keys": "8 [ENTER] 2 [÷] 15 [×]", "yx": "Y:4 | X:15", "ans": "60 pages"},
                    {"num": 5, "part": "B", "prompt": "Hot cocoa uses 3 tablespoons of cocoa for every 8 ounces of milk. How many ounces of milk are needed for 18 tablespoons of cocoa?", "keys": "18 [ENTER] 3 [÷] 8 [×]", "yx": "Y:6 | X:8", "ans": "48 ounces"},
                    {"num": 6, "part": "B", "prompt": "8 studio markers cost $12. Find the cost of 10 markers.", "keys": "12 [ENTER] 4 [÷] 5 [×]", "yx": "Y:3 | X:5", "ans": "$15"},
                    {"num": 7, "part": "B", "prompt": "A runner's heart beats 21 times in 15 seconds. At this rate, how many times does it beat in 1 minute (60 seconds)?", "keys": "60 [ENTER] 15 [÷] 21 [×]", "yx": "Y:4 | X:21", "ans": "84 beats"},
                    {"num": 8, "part": "B", "prompt": "Error Analysis: To find a ratio equivalent to 3:5, Sam added 4 to both terms and wrote 7:9. Explain why 3:5 and 7:9 are not equivalent.", "keys": "7 [ENTER] 9 [g][a:b]", "yx": "3:5 != 7:9", "ans": "Ratios scale by multiplication (e.g., ×3 gives 9:15), not addition"},
                    {"num": 9, "part": "C", "prompt": "Smoothie Bar: 9 berry smoothies require 12 cups of berries. How many cups of berries are needed to blend 15 smoothies?", "keys": "12 [ENTER] 3 [÷] 5 [×]", "yx": "Y:4 | X:5", "ans": "20 cups"},
                    {"num": 10, "part": "C", "prompt": "Electric Scooter Range: An e-scooter travels 14 miles on 35% of its battery. At this rate, how many miles can it travel on a 100% full charge?", "keys": "14 [ENTER] 7 [÷] 20 [×]", "yx": "Y:2 | X:20", "ans": "40 miles"}
                ]
            },
            {
                "day_num": 13,
                "sec_num": "3.3",
                "title": "Rates, Unit Rates & Best-Buy Comparisons",
                "big_ideas_ref": "Big Ideas Grade 6, Section 3.4 & 3.5 (Rates and Unit Rates)",
                "ccss": "CCSS.MATH.6.RP.A.2",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_ortho_steps.png",
                "diagram_type": "two_room",
                "diagram_data": {"room1": "Bag A: $4.20 ÷ 12 = $0.35/oz", "room2": "Bag B: $5.12 ÷ 16 = $0.32/oz", "op": "vs", "res": "Bag B Wins!", "caption": "Divide both quantities by the denominator to find the Unit Rate (per 1 unit)!"},
                "concept": "A rate compares two quantities measured in different units (such as miles and hours). A unit rate gives the amount per 1 unit of the second quantity (divide numerator ÷ denominator). Comparing unit prices shows which package is the better buy.",
                "examples": [
                    {
                        "title": "Example 1: Finding a Unit Rate",
                        "problem": "You type 315 words in 5 minutes. Find your unit rate in words per minute.",
                        "block_step": "Divide 315 words by 5 minutes: 315 ÷ 5 = 63 words per 1 minute.",
                        "keys": ["315", "ENTER", "5", "÷"],
                        "stack_y": "315 (Words)",
                        "stack_x": "5 (Min) -> 63",
                        "ans": "63 words per minute",
                        "note": "Check: 63 words/min × 5 min = 315 words!"
                    },
                    {
                        "title": "Example 2: Comparing Unit Prices (Best Buy)",
                        "problem": "Pack A has 4 batteries for $5.80. Pack B has 6 batteries for $8.40. Which pack is the better buy?",
                        "block_step": "Pack A: $5.80 ÷ 4 = $1.45 per battery. Pack B: $8.40 ÷ 6 = $1.40 per battery. Pack B costs less per battery!",
                        "keys": ["5.80", "ENTER", "4", "÷", "8.40", "ENTER", "6", "÷"],
                        "stack_y": "1.45 (Pack A)",
                        "stack_x": "1.40 (Pack B)",
                        "ans": "Pack B ($1.40/battery vs. $1.45/battery)",
                        "note": "Or compare 12 batteries: 3 Pack As = $17.40 vs. 2 Pack Bs = $16.80!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "A car travels 195 miles in 3 hours. Find the average speed in miles per hour.", "keys": "195 [ENTER] 3 [÷]", "yx": "Y:195 | X:3", "ans": "65 mph"},
                    {"num": 2, "part": "A", "prompt": "You earn $36 for 4 hours of tutoring. What is your hourly pay rate?", "keys": "36 [ENTER] 4 [÷]", "yx": "Y:36 | X:4", "ans": "$9 per hour"},
                    {"num": 3, "part": "A", "prompt": "A 6-pound bag of apples costs $7.80. What is the price per pound?", "keys": "7.80 [ENTER] 6 [÷]", "yx": "Y:7.80 | X:6", "ans": "$1.30 per pound"},
                    {"num": 4, "part": "A", "prompt": "A 3D printer extrudes 90 grams of filament in 6 hours. How many grams does it extrude per hour?", "keys": "90 [ENTER] 6 [÷]", "yx": "Y:90 | X:6", "ans": "15 grams per hour"},
                    {"num": 5, "part": "B", "prompt": "Dueling Copper-Foil Suppliers: Supplier A sells an 18-oz roll of copper foil for $3.24. Supplier B sells a 24-oz roll for $4.08. Find both unit prices—which supplier is cheaper per ounce?", "keys": "3.24 [ENTER] 18 [÷]; 4.08 [ENTER] 24 [÷]", "yx": "Y:0.18 | X:0.17", "ans": "Supplier B ($0.17/oz vs. $0.18/oz)"},
                    {"num": 6, "part": "B", "prompt": "A 6-pack of gel pens costs $5.10, and a 10-pack costs $8.20. Which pack has the lower cost per pen?", "keys": "5.10 [ENTER] 6 [÷]; 8.20 [ENTER] 10 [÷]", "yx": "Y:0.85 | X:0.82", "ans": "10-pack ($0.82/pen vs. $0.85/pen)"},
                    {"num": 7, "part": "B", "prompt": "A train travels 210 miles in 3.5 hours. At this constant speed, how far will it travel in 5 hours?", "keys": "210 [ENTER] 3.5 [÷] 5 [×]", "yx": "Y:60 | X:5", "ans": "300 miles"},
                    {"num": 8, "part": "B", "prompt": "Pump A fills 45 gallons in 5 minutes. Pump B fills 64 gallons in 8 minutes. Which pump has the faster flow rate?", "keys": "45 [ENTER] 5 [÷]; 64 [ENTER] 8 [÷]", "yx": "Y:9 | X:8", "ans": "Pump A (9 gal/min vs. 8 gal/min)"},
                    {"num": 9, "part": "C", "prompt": "An extruder pushes 45 mm of filament in 15 seconds. At this rate, how many millimeters of filament does it push in 1 minute (60 seconds)?", "keys": "45 [ENTER] 15 [÷] 60 [×]", "yx": "Y:3 | X:60", "ans": "180 mm"},
                    {"num": 10, "part": "C", "prompt": "Car A drives 168 miles on 6 gallons of gas. Car B drives 232 miles on 8 gallons. Which car gets better fuel mileage, and by how many miles per gallon?", "keys": "168 [ENTER] 6 [÷]; 232 [ENTER] 8 [÷]", "yx": "Y:28 | X:29", "ans": "Car B by 1 mpg (29 mpg vs. 28 mpg)"}
                ]
            },
            {
                "day_num": 14,
                "sec_num": "3.4",
                "title": "Percents, Fractions, and Decimals",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 4.1–4.3 / 5.5 (Percents, Fractions, and Decimals)",
                "ccss": "CCSS.MATH.6.RP.A.3c",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_twin_comparator.png",
                "diagram_type": "percent_bar",
                "diagram_data": {"pct": 75, "frac": "3/4", "dec": "0.75", "caption": "75% = 75/100 = 3/4 = 0.75!"},
                "concept": "'Percent' (%) means 'per hundred' or 'out of 100.' Any fraction, decimal, or percent can be converted into the other two forms: scale the denominator to 100 (or divide numerator ÷ denominator and multiply by 100%). To find p% of a whole w, multiply (p/100) × w.",
                "examples": [
                    {
                        "title": "Example 1: Converting Fractions, Decimals & Percents",
                        "problem": "Write 7/20 as a decimal and as a percent.",
                        "block_step": "Scale the denominator to 100: (7 × 5)/(20 × 5) = 35/100 = 0.35 = 35%. Or divide 7 ÷ 20 = 0.35.",
                        "keys": [".", "7", ".", "20", "ENTER", "FDISP", "100", "×"],
                        "stack_y": "7/20",
                        "stack_x": "0.35 -> 35%",
                        "ans": "0.35 and 35%",
                        "note": "7/20 = 35/100 = 0.35 = 35%!"
                    },
                    {
                        "title": "Example 2: Finding a Percent from a Part and Whole",
                        "problem": "You make 18 out of 24 free throws. What percent of your free throws did you make?",
                        "block_step": "Simplify 18/24 by dividing by 6 to get 3/4. Since 3/4 = 75/100 = 0.75, you made 75% of your shots!",
                        "keys": ["18", "ENTER", "24", "÷", "FDISP"],
                        "stack_y": "18 | 24",
                        "stack_x": "0.75 (3/4 = 75%)",
                        "ans": "75%",
                        "note": "Simplifying 18/24 -> 3/4 makes the benchmark percent 75% instant!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Write 3/5 as a decimal and as a percent.", "keys": "[.] 3 [.] 5 [ENTER] [FDISP]", "yx": "Y:3/5 | X:0.6", "ans": "0.6 and 60%"},
                    {"num": 2, "part": "A", "prompt": "Write 9/25 as a decimal and as a percent.", "keys": "[.] 9 [.] 25 [ENTER] [FDISP]", "yx": "Y:9/25 | X:0.36", "ans": "0.36 and 36%"},
                    {"num": 3, "part": "A", "prompt": "Write 45% as a decimal and as a fraction in simplest form.", "keys": "45 [ENTER] 100 [÷] [FDISP]", "yx": "0.45 -> 9/20", "ans": "0.45 and 9/20"},
                    {"num": 4, "part": "A", "prompt": "Write 0.125 as a percent and as a fraction in simplest form.", "keys": "0.125 [ENTER] [FDISP]", "yx": "12.5% | 1/8", "ans": "12.5% and 1/8"},
                    {"num": 5, "part": "B", "prompt": "Harvest Co-Op Banquet: A community hall seats 450 guests. If 60% of the seats are reserved for farm families, how many seats are reserved?", "keys": "450 [ENTER] 60 [%]", "yx": "Y:450 | X:270", "ans": "270 seats"},
                    {"num": 6, "part": "B", "prompt": "Artisan Sourdough Hydration: A baker uses a 65% hydration ratio (water weight is 65% of flour weight). For 5,400 grams of flour, how many grams of water are needed?", "keys": "5400 [ENTER] 65 [%]", "yx": "Y:5400 | X:3510", "ans": "3,510 grams"},
                    {"num": 7, "part": "B", "prompt": "Grading Golden Honey Jars: An inspector grades 42 out of 50 jars of wildflower honey as Grade A Amber. What percent of the jars earned Grade A?", "keys": "42 [ENTER] 50 [÷]", "yx": "0.84 -> 84%", "ans": "84%"},
                    {"num": 8, "part": "B", "prompt": "Write 150% as a decimal and as a mixed number in simplest form.", "keys": "150 [ENTER] 100 [÷] [FDISP]", "yx": "1.5 -> 1 1/2", "ans": "1.5 and 1 1/2"},
                    {"num": 9, "part": "C", "prompt": "Order 5/8, 60%, and 0.61 from least to greatest.", "keys": "[.] 5 [.] 8 [FDISP] -> 0.625", "yx": "0.60, 0.61, 0.625", "ans": "60%, 0.61, 5/8"},
                    {"num": 10, "part": "C", "prompt": "A phone battery is at 35% of its 4,000 mAh capacity. How many mAh of charge remain?", "keys": "4000 [ENTER] 35 [%]", "yx": "Y:4000 | X:1400", "ans": "1,400 mAh"}
                ]
            },
            {
                "day_num": 15,
                "sec_num": "3.5",
                "title": "Discounts, Percent Change & Converting Measures",
                "big_ideas_ref": "Big Ideas Grade 6, Section 5.6 & 5.7 (Percent Problems & Converting Measures)",
                "ccss": "CCSS.MATH.6.RP.A.3d",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_ortho_steps.png",
                "diagram_type": "percent_bar",
                "diagram_data": {"pct": 75, "frac": "Pay 75% ($45)", "dec": "Save 25% ($15)", "caption": "$60 Game at 25% Off: Subtract $15 discount ($60 - $15 = $45) OR find 75% of $60 ($45)!"},
                "concept": "In Big Ideas Math, you can find a discounted sale price in two ways: (1) find the discount amount and subtract it from the original price, or (2) subtract the discount percent from 100% first and multiply! For percent change, divide (Change ÷ Original Amount) × 100%. For unit conversions, multiply by a conversion factor so the old units cancel.",
                "examples": [
                    {
                        "title": "Example 1: Finding a Sale Price in Two Ways",
                        "problem": "A $60 video game is on sale for 25% off. Find the discount and the sale price.",
                        "block_step": "Way 1: 25% of $60 = $15 discount; $60 - $15 = $45. Way 2: 100% - 25% = 75% paid; 0.75 × $60 = $45!",
                        "keys": ["60", "ENTER", "25", "%", "-"],
                        "stack_y": "60 (Orig)",
                        "stack_x": "15 (Disc) -> 45",
                        "ans": "Discount = $15; Sale Price = $45",
                        "note": "Both ways give the exact same $45 sale price!"
                    },
                    {
                        "title": "Example 2: Percent Change & Unit Conversions",
                        "problem": "A club's membership grows from 20 to 26 students. Find the percent of increase, and convert 32 inches to centimeters (1 in = 2.54 cm).",
                        "block_step": "Change = 26 - 20 = 6; 6 ÷ 20 = 0.30 = +30%. For 32 inches: 32 in × (2.54 cm / 1 in) = 81.28 cm.",
                        "keys": ["20", "ENTER", "26", "g", "%CHG", "32", "f", "▸cm"],
                        "stack_y": "+30%",
                        "stack_x": "81.28 cm",
                        "ans": "+30% increase; 32 in = 81.28 cm",
                        "note": "Always divide the change by the ORIGINAL amount (20)!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Wool Work Coat: An $85 wool coat is on sale for 20% off. Find the discount amount and the sale price.", "keys": "85 [ENTER] 20 [%] [-]", "yx": "Y:85 | X:17", "ans": "Discount $17; Sale price $68"},
                    {"num": 2, "part": "A", "prompt": "Garden Cart Checkout: A steel garden cart costs $120.00 before an 8.5% sales tax. Find the sales tax and the final price.", "keys": "120 [ENTER] 8.5 [%] [+]", "yx": "Y:120 | X:10.20", "ans": "Tax $10.20; Total $130.20"},
                    {"num": 3, "part": "A", "prompt": "Seedling Height Surge: A pine seedling grows from 15 mm to 75 mm. What is the percent of increase in its height?", "keys": "15 [ENTER] 75 [g][%CHG]", "yx": "Y:15 | X:75", "ans": "+400% ((75-15)÷15 = 400%)"},
                    {"num": 4, "part": "A", "prompt": "Find the percent of decrease from 80 down to 60.", "keys": "80 [ENTER] 60 [g][%CHG]", "yx": "Y:80 | X:60", "ans": "25% decrease"},
                    {"num": 5, "part": "B", "prompt": "Use the conversion factor 1 in = 2.54 cm to convert 10 inches to centimeters.", "keys": "10 [f][▸cm]", "yx": "10 in -> cm", "ans": "25.4 cm"},
                    {"num": 6, "part": "B", "prompt": "Use the conversion factor 1 in = 2.54 cm to convert 50.8 centimeters to inches.", "keys": "50.8 [g][▸in]", "yx": "50.8 cm -> in", "ans": "20 in"},
                    {"num": 7, "part": "B", "prompt": "Workshop Tool Backpack: A $56 canvas tool backpack is on sale for 30% off. What is the sale price?", "keys": "56 [ENTER] 30 [%] [-]", "yx": "Y:56 | X:16.80", "ans": "$39.20"},
                    {"num": 8, "part": "B", "prompt": "18 is 25% of what whole number?", "keys": "18 [ENTER] 0.25 [÷]", "yx": "Y:18 | X:0.25", "ans": "72"},
                    {"num": 9, "part": "C", "prompt": "Stacking Two Discounts on a Solar Battery: A $200 solar battery is marked 20% off, and an extra 10% clearance coupon is applied to the reduced sale price. What is the final price?", "keys": "200 [ENTER] 20 [%] [-] 10 [%] [-]", "yx": "160 -> 144", "ans": "$144 ($200 -> $160 -> $144)"},
                    {"num": 10, "part": "C", "prompt": "A 32-inch skateboard deck weighs 5 pounds. Convert its length to centimeters (1 in = 2.54 cm) and its mass to kilograms (1 lb ≈ 0.4536 kg, rounded to the nearest hundredth).", "keys": "32 [f][▸cm]; 5 [f][▸kg]", "yx": "81.28cm | 2.27kg", "ans": "81.28 cm and 2.27 kg"}
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
        "kit_summary": "Place Value Studio (PLACE-01) + Prime Factor Studio (PRIME-01)",
        "hero_png": "place_value_regrouping.png",
        "coach_misconception": "Students panic when letters appear, erroneously combine 3x + 2 into 5x or x² + x into x³, and don't see why 3(x + 4) = 3x + 12.",
        "coach_remediation": "Show that a variable x is simply an empty Place Value tray socket waiting for a Digit Block to be substituted in, and that different place-value columns (x², x, and 1s) cannot be combined into one column! Use Prime Factor Studio (PRIME-01) to find the GCF when factoring expressions.",
        "sections": [
            {
                "day_num": 16,
                "sec_num": "4.1",
                "title": "Algebraic Expressions — Writing & Evaluating Expressions",
                "big_ideas_ref": "Big Ideas Grade 6, Section 3.1 / 5.1 (Algebraic Expressions)",
                "ccss": "CCSS.MATH.6.EE.A.2",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "algebra_tiles",
                "diagram_data": {"mode": "eval", "x_rods": 4, "units": 7, "x_val": 5, "caption": "4x + 7 when x = 5: Substitute 5 into each x-box (4 × 5 = 20) and add 7 unit blocks = 27."},
                "concept": "An algebraic expression contains numbers, variables (letters representing unknown quantities), and operations. In an expression like 4x + 7, 4x and 7 are terms, 4 is the coefficient of x, and 7 is a constant. To evaluate an algebraic expression, substitute the given number for each variable and follow the Order of Operations (PEMDAS).",
                "examples": [
                    {
                        "title": "Example 1: Evaluating a Single-Variable Expression (4x + 7 when x = 5)",
                        "problem": "Evaluate 4x + 7 when x = 5.",
                        "block_step": "Substitute 5 for x: 4(5) + 7 = 20 + 7 = 27.",
                        "keys": ["4", "ENTER", "5", "×", "7", "+"],
                        "stack_y": "20 (4x)",
                        "stack_x": "7 -> 27",
                        "ans": "27",
                        "note": "Multiply the coefficient 4 by 5 before adding the constant 7."
                    },
                    {
                        "title": "Example 2: Exponents & Two Variables (3a² + 4b for a=5, b=6)",
                        "problem": "Evaluate 3a² + 4b when a = 5 and b = 6.",
                        "block_step": "In 3a², evaluate the exponent first (5² = 25), then multiply by 3 (= 75), and add 4(6) = 24 to get 99.",
                        "keys": ["5", "x²", "3", "×", "4", "ENTER", "6", "×", "+"],
                        "stack_y": "75 (3a²)",
                        "stack_x": "24 (4b) -> 99",
                        "ans": "99",
                        "note": "In 3a², only a is squared—never multiply 3 × a before squaring!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Evaluate 6x - 9 when x = 7.", "keys": "6 [ENTER] 7 [×] 9 [-]", "yx": "Y:42 | X:9", "ans": "33"},
                    {"num": 2, "part": "A", "prompt": "Evaluate 5n + 14 when n = 8.", "keys": "5 [ENTER] 8 [×] 14 [+]", "yx": "Y:40 | X:14", "ans": "54"},
                    {"num": 3, "part": "A", "prompt": "Evaluate 40 - 3m when m = 9.", "keys": "40 [ENTER] 3 [ENTER] 9 [×] [-]", "yx": "Y:40 | X:27", "ans": "13"},
                    {"num": 4, "part": "A", "prompt": "Evaluate x² + 11 when x = 6.", "keys": "6 [x²] 11 [+]", "yx": "Y:36 | X:11", "ans": "47"},
                    {"num": 5, "part": "B", "prompt": "Evaluate 2y² - 5 when y = 4.", "keys": "4 [x²] 2 [×] 5 [-]", "yx": "Y:32 | X:5", "ans": "27"},
                    {"num": 6, "part": "B", "prompt": "Evaluate 7a + 3b when a = 4 and b = 9.", "keys": "7 [ENTER] 4 [×] 3 [ENTER] 9 [×] [+]", "yx": "Y:28 | X:27", "ans": "55"},
                    {"num": 7, "part": "B", "prompt": "Evaluate (x + y) ÷ 4 when x = 19 and y = 13.", "keys": "19 [ENTER] 13 [+] 4 [÷]", "yx": "Y:32 | X:4", "ans": "8"},
                    {"num": 8, "part": "B", "prompt": "Evaluate 5k - 2.4 when k = 3.5.", "keys": "5 [ENTER] 3.5 [×] 2.4 [-]", "yx": "Y:17.5 | X:2.4", "ans": "15.1"},
                    {"num": 9, "part": "C", "prompt": "Skate Park Rental: A skate park charges an $8 helmet fee plus $4.50 per hour. Write an algebraic expression for the total cost of h hours, and find the total cost for 4 hours.", "keys": "4.50 [ENTER] 4 [×] 8 [+]", "yx": "Y:18 | X:8", "ans": "8 + 4.50h; $26"},
                    {"num": 10, "part": "C", "prompt": "Cube Display Case: The surface area of a cube with edge length s is given by the expression 6s². What is the surface area of a cube with edge length s = 5 cm?", "keys": "5 [x²] 6 [×]", "yx": "Y:25 | X:6", "ans": "150 cm²"}
                ]
            },
            {
                "day_num": 17,
                "sec_num": "4.2",
                "title": "Simplifying Expressions — Combining Like Terms",
                "big_ideas_ref": "Big Ideas Grade 6, Section 3.2 & 3.3 / 5.2 (Simplifying Algebraic Expressions)",
                "ccss": "CCSS.MATH.6.EE.A.3",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "algebra_tiles",
                "diagram_data": {"mode": "like_terms", "x2_flats": 2, "x_rods": 5, "units": 4, "caption": "Three distinct term columns: x²-Terms, x-Terms, and 1-Units. Only terms with the exact same variable and exponent combine!"},
                "concept": "Terms that have the exact same variable raised to the exact same exponent are called Like Terms (such as 4x and 2x, or 3x² and 2x²). Constant terms (such as 5 and 3) are also like terms. To simplify an expression, use the Commutative and Associative Properties to group like terms together and add or subtract their coefficients.",
                "examples": [
                    {
                        "title": "Example 1: Combining Linear and Constant Terms (4x + 5 + 2x + 3)",
                        "problem": "Simplify the expression 4x + 5 + 2x + 3.",
                        "block_step": "Group the x-terms together (4x + 2x = 6x) and group the constant terms together (5 + 3 = 8) to get 6x + 8.",
                        "keys": ["4", "ENTER", "2", "+", "5", "ENTER", "3", "+"],
                        "stack_y": "6 (x-terms)",
                        "stack_x": "8 (units)",
                        "ans": "6x + 8",
                        "note": "Check with x=10: 4(10)+5+2(10)+3 = 68, and 6(10)+8 = 68."
                    },
                    {
                        "title": "Example 2: Combining x², x, and Constant Terms (3x² + 5x + 2x² - x + 6)",
                        "problem": "Simplify 3x² + 5x + 2x² - x + 6.",
                        "block_step": "Group by variable and exponent: (3x² + 2x²) + (5x - 1x) + 6 = 5x² + 4x + 6.",
                        "keys": ["3", "ENTER", "2", "+", "5", "ENTER", "1", "-"],
                        "stack_y": "5 (x²-terms)",
                        "stack_x": "4 (x-terms)",
                        "ans": "5x² + 4x + 6",
                        "note": "Remember: a variable x with no written coefficient has a coefficient of 1 (1x)."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Simplify the expression: 7x + 4 + 2x + 9.", "keys": "7 [ENTER] 2 [+]; 4 [ENTER] 9 [+]", "yx": "Y:9 (x) | X:13 (1)", "ans": "9x + 13"},
                    {"num": 2, "part": "A", "prompt": "Simplify the expression: 8x + 11 - 3x - 4.", "keys": "8 [ENTER] 3 [-]; 11 [ENTER] 4 [-]", "yx": "Y:5 (x) | X:7 (1)", "ans": "5x + 7"},
                    {"num": 3, "part": "A", "prompt": "Simplify the expression: 9y - y + 6.", "keys": "9 [ENTER] 1 [-]", "yx": "Y:8 (y) | X:6 (1)", "ans": "8y + 6"},
                    {"num": 4, "part": "A", "prompt": "Simplify the expression: 12a + 5 - 4a + 8.", "keys": "12 [ENTER] 4 [-]; 5 [ENTER] 8 [+]", "yx": "Y:8 (a) | X:13 (1)", "ans": "8a + 13"},
                    {"num": 5, "part": "B", "prompt": "Simplify the expression: 4x² + 3x + 2x² + 5x + 7.", "keys": "4+2=6; 3+5=8", "yx": "6(x²) | 8(x) | 7", "ans": "6x² + 8x + 7"},
                    {"num": 6, "part": "B", "prompt": "Simplify the expression: 6n² + 9n - 2n² - 4n + 10.", "keys": "6-2=4; 9-4=5", "yx": "4(n²) | 5(n) | 10", "ans": "4n² + 5n + 10"},
                    {"num": 7, "part": "B", "prompt": "Simplify the expression: 3.5x + 4.2 + 1.8x - 1.5.", "keys": "3.5 [ENTER] 1.8 [+]; 4.2 [ENTER] 1.5 [-]", "yx": "Y:5.3 | X:2.7", "ans": "5.3x + 2.7"},
                    {"num": 8, "part": "B", "prompt": "Error Analysis: Leo simplified 5x + 3 to 8x. Explain why 5x and 3 cannot be combined, and prove they are not equivalent by substituting x = 10 into both expressions.", "keys": "5(10)+3=53 vs 8(10)=80", "yx": "Y:53 | X:80", "ans": "53 != 80; 5x + 3 is already in simplest form"},
                    {"num": 9, "part": "C", "prompt": "Garden Border: A rectangular garden has two sides of length (2x + 3) meters and two sides of length (x + 5) meters. Write a simplified algebraic expression for its perimeter, and find the perimeter when x = 10.", "keys": "2+2+1+1=6x; 3+3+5+5=16", "yx": "Y:6 (x) | X:16", "ans": "6x + 16; 76 meters"},
                    {"num": 10, "part": "C", "prompt": "Pennant Frame: A triangular frame has side lengths of (3x + 2) cm, (2x + 7) cm, and (4x - 1) cm. Write a simplified expression for its perimeter, and find the perimeter when x = 5.", "keys": "3+2+4=9x; 2+7-1=8", "yx": "Y:9 (x) | X:8", "ans": "9x + 8; 53 cm"}
                ]
            },
            {
                "day_num": 18,
                "sec_num": "4.3",
                "title": "The Distributive Property — Area Models & Expanding Expressions",
                "big_ideas_ref": "Big Ideas Grade 6, Section 3.4 / 5.3 (The Distributive Property)",
                "ccss": "CCSS.MATH.6.EE.A.3",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "algebra_tiles",
                "diagram_data": {"mode": "distrib", "rows": 3, "x_per_row": 1, "u_per_row": 4, "caption": "Area Model for 3(x + 4): 3 rows of (x + 4) equals 3x + 12."},
                "concept": "To multiply a sum or difference by a number, multiply each term inside the parentheses by the number outside the parentheses: a(b + c) = ab + ac and a(b - c) = ab - ac. Geometrically, a rectangle of height 3 and split width (x + 4) has two partial areas: 3(x) + 3(4) = 3x + 12.",
                "examples": [
                    {
                        "title": "Example 1: Numerical Area Model 6(10 + 4)",
                        "problem": "Evaluate 6(10 + 4) using the Order of Operations and using the Distributive Property.",
                        "block_step": "Order of Operations: 6(14) = 84. Distributive Property: 6(10) + 6(4) = 60 + 24 = 84.",
                        "keys": ["6", "ENTER", "10", "×", "6", "ENTER", "4", "×", "+"],
                        "stack_y": "60 (6×10)",
                        "stack_x": "24 (6×4) -> 84",
                        "ans": "84",
                        "note": "Both methods give the exact same area: 60 + 24 = 84."
                    },
                    {
                        "title": "Example 2: Distributing & Combining Like Terms 5(2x + 3) + 4x",
                        "problem": "Simplify the expression 5(2x + 3) + 4x.",
                        "block_step": "Distribute 5 to both terms inside the parentheses (10x + 15), then combine like terms: (10x + 4x) + 15 = 14x + 15.",
                        "keys": ["5", "ENTER", "2", "×", "4", "+", "5", "ENTER", "3", "×"],
                        "stack_y": "14 (x-terms)",
                        "stack_x": "15 (units)",
                        "ans": "14x + 15",
                        "note": "Check with x=2: 5(4+3) + 8 = 43, and 14(2) + 15 = 43."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Use the Distributive Property to find the two partial products and total of 7(20 + 3).", "keys": "7 [ENTER] 20 [×] 7 [ENTER] 3 [×] [+]", "yx": "Y:140 | X:21", "ans": "140 + 21 = 161"},
                    {"num": 2, "part": "A", "prompt": "Use the Distributive Property to simplify 4(x + 5).", "keys": "4 [ENTER] 5 [×]", "yx": "4(x) | 20(1)", "ans": "4x + 20"},
                    {"num": 3, "part": "A", "prompt": "Use the Distributive Property to simplify 6(3x + 4).", "keys": "6×3=18; 6×4=24", "yx": "Y:18 | X:24", "ans": "18x + 24"},
                    {"num": 4, "part": "A", "prompt": "Use the Distributive Property to simplify 8(2y - 5).", "keys": "8×2=16; 8×5=40", "yx": "Y:16 | X:-40", "ans": "16y - 40"},
                    {"num": 5, "part": "B", "prompt": "Evaluate 9 × 43 mentally using the Distributive Property by splitting 43 into (40 + 3).", "keys": "9 [ENTER] 40 [×] 9 [ENTER] 3 [×] [+]", "yx": "Y:360 | X:27", "ans": "387"},
                    {"num": 6, "part": "B", "prompt": "Simplify the expression: 3(4x + 2) + 5x.", "keys": "3×4+5=17; 3×2=6", "yx": "Y:17 | X:6", "ans": "17x + 6"},
                    {"num": 7, "part": "B", "prompt": "Simplify the expression: 4(3n + 5) - 7.", "keys": "4×3=12; 20-7=13", "yx": "Y:12 | X:13", "ans": "12n + 13"},
                    {"num": 8, "part": "B", "prompt": "Error Analysis: Mia wrote 5(x + 6) = 5x + 6. Explain her error and write the correct simplified expression.", "keys": "5 [ENTER] 6 [×]", "yx": "5 × 6 = 30", "ans": "5x + 30 (She forgot to multiply 6 by 5)"},
                    {"num": 9, "part": "C", "prompt": "Simplify 5(2x + 3) + 4x, and verify your simplified expression by evaluating both expressions when x = 2.", "keys": "5×2+4=14; 5×3=15", "yx": "Y:14 | X:15", "ans": "14x + 15 (Both equal 43 when x = 2)"},
                    {"num": 10, "part": "C", "prompt": "Team Lunch Order: Six teammates each order a sandwich costing x dollars and a smoothie costing $3.50. Write a factored expression and an expanded expression for the total cost, then find the total if each sandwich costs $6.50.", "keys": "6 [ENTER] 3.50 [×] -> 6x+21", "yx": "Y:39 | X:21", "ans": "6(x + 3.50) = 6x + 21; $60 total"}
                ]
            },
            {
                "day_num": 19,
                "sec_num": "4.4",
                "title": "Factoring Expressions — Factoring Out the GCF",
                "big_ideas_ref": "Big Ideas Grade 6, Section 3.4 Ext / 5.4 (Factoring Expressions)",
                "ccss": "CCSS.MATH.6.EE.A.3",
                "kit_id": "PRIME-01",
                "kit_name": "Prime Factor Studio",
                "asset_png": "prime_lcm_gcd_venn.png",
                "diagram_type": "algebra_tiles",
                "diagram_data": {"mode": "distrib", "rows": 6, "x_per_row": 3, "u_per_row": 4, "caption": "Factoring 18x + 24: GCF(18, 24) = 6 equal rows of (3x + 4) -> 6(3x + 4)."},
                "concept": "Factoring an expression means writing a sum or difference as a product—the exact reverse of the Distributive Property! To factor an expression completely, find the Greatest Common Factor (GCF) of its terms, write the GCF outside the parentheses, and divide each term by the GCF to find the terms inside.",
                "examples": [
                    {
                        "title": "Example 1: Factoring an Algebraic Expression Using the GCF",
                        "problem": "Factor 18x + 24 completely using the GCF.",
                        "block_step": "The GCF of 18 and 24 is 6. Divide each term by 6 (18x ÷ 6 = 3x and 24 ÷ 6 = 4) to get 6(3x + 4).",
                        "keys": ["18", "ENTER", "24", "GCF"],
                        "stack_y": "18 | 24",
                        "stack_x": "6 (GCF rows)",
                        "ans": "6(3x + 4)",
                        "note": "Check by distributing: 6(3x) + 6(4) = 18x + 24."
                    },
                    {
                        "title": "Example 2: Factoring Subtraction Expressions (45x - 30)",
                        "problem": "Factor 45x - 30 completely using the GCF.",
                        "block_step": "The GCF of 45 and 30 is 15. Divide each term by 15 (45x ÷ 15 = 3x and 30 ÷ 15 = 2) to get 15(3x - 2).",
                        "keys": ["45", "ENTER", "30", "GCF", "45", "x⇄y", "÷"],
                        "stack_y": "15 (GCF)",
                        "stack_x": "3 (45÷15)",
                        "ans": "15(3x - 2)",
                        "note": "Check by distributing: 15(3x) - 15(2) = 45x - 30."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Factor the numerical expression 12 + 20 using the GCF.", "keys": "12 [ENTER] 20 [GCF] -> 4", "yx": "GCF = 4", "ans": "4(3 + 5)"},
                    {"num": 2, "part": "A", "prompt": "Factor 8x + 12 completely using the GCF.", "keys": "8 [ENTER] 12 [GCF] -> 4", "yx": "GCF = 4", "ans": "4(2x + 3)"},
                    {"num": 3, "part": "A", "prompt": "Factor 15y - 25 completely using the GCF.", "keys": "15 [ENTER] 25 [GCF] -> 5", "yx": "GCF = 5", "ans": "5(3y - 5)"},
                    {"num": 4, "part": "A", "prompt": "Factor 24x + 36 completely using the GCF.", "keys": "24 [ENTER] 36 [GCF] -> 12", "yx": "GCF = 12", "ans": "12(2x + 3)"},
                    {"num": 5, "part": "B", "prompt": "Factor 32n - 48 completely using the GCF.", "keys": "32 [ENTER] 48 [GCF] -> 16", "yx": "GCF = 16", "ans": "16(2n - 3)"},
                    {"num": 6, "part": "B", "prompt": "Factor 42a + 14 completely using the GCF.", "keys": "42 [ENTER] 14 [GCF] -> 14", "yx": "GCF = 14", "ans": "14(3a + 1)"},
                    {"num": 7, "part": "B", "prompt": "Factor 36m - 60 completely using the GCF.", "keys": "36 [ENTER] 60 [GCF] -> 12", "yx": "GCF = 12", "ans": "12(3m - 5)"},
                    {"num": 8, "part": "B", "prompt": "Error Analysis: Sam factored 24x + 36 as 6(4x + 6). Explain why his expression is not factored completely, and write the completely factored form.", "keys": "4 [ENTER] 6 [GCF] -> 2 left!", "yx": "GCF(24,36)=12", "ans": "12(2x + 3) (4 and 6 still share a factor of 2)"},
                    {"num": 9, "part": "C", "prompt": "Banner Width: A rectangular banner has an area of (28x + 42) square inches and a height equal to the GCF of 28 and 42. What are the height and width of the banner?", "keys": "28 [ENTER] 42 [GCF] -> 14", "yx": "GCF = 14", "ans": "Height = 14 in.; Width = (2x + 3) in."},
                    {"num": 10, "part": "C", "prompt": "Square Garden Perimeter: A square garden has a total perimeter of (36x + 48) feet. What is the length of one side of the garden?", "keys": "36 [ENTER] 4 [÷]; 48 [ENTER] 4 [÷]", "yx": "Y:9 | X:12", "ans": "(9x + 12) feet"}
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
        "kit_summary": "Fraction Studio (FRAC-01) + Place Value Studio (PLACE-01)",
        "hero_png": "fraction_studio_common_denominator.png",
        "coach_misconception": "Students multiply the slanted side of a parallelogram instead of the vertical height, forget to divide by 2 for triangles, lose track of multi-piece composite areas, and subtract clock times in base-10 instead of base-60.",
        "coach_remediation": "Slide the corner triangle of a parallelogram to form a straight [f] [RECT] rectangle, use the dedicated [g] [TRI] key ([g][7]) which divides by 2 automatically, accumulate composite chunks with [Σ+], and use the Place Value Studio (PLACE-01) + [CLK] key for base-60 time.",
        "sections": [
            {
                "day_num": 20,
                "sec_num": "5.1",
                "title": "Areas of Parallelograms — Base Times Perpendicular Height",
                "big_ideas_ref": "Big Ideas Grade 6, Section 4.1 (Areas of Parallelograms)",
                "ccss": "CCSS.MATH.6.G.A.1",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "polygon_area",
                "diagram_data": {"shape": "parallelogram", "b": 12, "h": 8, "slant": 10, "caption": "Cut the right triangle off one end and slide it to the other: every parallelogram has the same area as a b × h rectangle (A = bh)."},
                "concept": "If you cut a right triangle from one end of a parallelogram and translate (slide) it to the other end, the parallelogram forms a rectangle with the exact same base b and perpendicular height h! Therefore, the area of any parallelogram is A = bh, where h is the perpendicular vertical height (never the slanted side length).",
                "examples": [
                    {
                        "title": "Example 1: Finding the Area of a Parallelogram",
                        "problem": "Find the area of a parallelogram with base b = 12 cm, perpendicular height h = 8 cm, and slanted side 10 cm.",
                        "block_step": "Use the base b = 12 cm and perpendicular height h = 8 cm (ignore the 10 cm slanted side): A = 12 × 8 = 96 cm².",
                        "keys": ["12", "ENTER", "8", "f", "RECT"],
                        "stack_y": "12 (Base)",
                        "stack_x": "8 (Height)",
                        "ans": "96 cm²",
                        "note": "Always use the perpendicular height (marked with a right-angle box), never the slanted side."
                    },
                    {
                        "title": "Example 2: Finding a Missing Dimension from Area",
                        "problem": "A parallelogram banner has an area of 168 in.² and a base of 14 in. What is its perpendicular height h?",
                        "block_step": "Substitute into A = bh: 168 = 14h. Divide both sides by 14: h = 168 ÷ 14 = 12 in.",
                        "keys": ["168", "ENTER", "14", "÷", "f", "LASTX", "f", "RECT"],
                        "stack_y": "168",
                        "stack_x": "14 -> 12",
                        "ans": "h = 12 in.",
                        "note": "Check: 14 in. × 12 in. = 168 in.²."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the area of a parallelogram with base b = 15 m, perpendicular height h = 9 m, and slanted side 11 m.", "keys": "15 [ENTER] 9 [f][RECT]", "yx": "Y:15 | X:9", "ans": "135 m²"},
                    {"num": 2, "part": "A", "prompt": "Parallelogram Flower Bed: A botanical garden bed is shaped like a parallelogram with a base of 8 meters and a perpendicular height of 4.5 meters. What is the area of the flower bed?", "keys": "8 [ENTER] 4.5 [f][RECT]", "yx": "Y:8 | X:4.5", "ans": "36 m²"},
                    {"num": 3, "part": "A", "prompt": "Find the area of a parallelogram with base b = 8.5 m and perpendicular height h = 6.4 m.", "keys": "8.5 [ENTER] 6.4 [f][RECT]", "yx": "Y:8.5 | X:6.4", "ans": "54.4 m²"},
                    {"num": 4, "part": "A", "prompt": "Find the area of a square courtyard tile with side length 13 cm.", "keys": "13 [x²]", "yx": "Y:0 | X:169", "ans": "169 cm²"},
                    {"num": 5, "part": "B", "prompt": "A parallelogram has a base of 6 1/2 inches and a perpendicular height of 4 inches. What is its area?", "keys": "6 [.] 1 [.] 2 [ENTER] 4 [f][RECT]", "yx": "Y:6 1/2 | X:4", "ans": "26 in.²"},
                    {"num": 6, "part": "B", "prompt": "A parallelogram has an area of 108 cm² and a base of 12 cm. What is its perpendicular height?", "keys": "108 [ENTER] 12 [÷]", "yx": "Y:108 | X:12", "ans": "9 cm"},
                    {"num": 7, "part": "B", "prompt": "A parallelogram has an area of 135 ft² and a perpendicular height of 7.5 ft. What is its base?", "keys": "135 [ENTER] 7.5 [÷]", "yx": "Y:135 | X:7.5", "ans": "18 ft"},
                    {"num": 8, "part": "B", "prompt": "Error Analysis: A parallelogram has base b = 10 cm, perpendicular height h = 6 cm, and slanted side s = 7.5 cm. Sam calculated the area as 75 cm². Explain his error and find the correct area.", "keys": "10 [ENTER] 6 [f][RECT]", "yx": "Y:10 | X:6", "ans": "60 cm² (He multiplied by the slanted side 7.5)"},
                    {"num": 9, "part": "C", "prompt": "Angled Parking Spaces: Each angled parking space is a parallelogram with a base of 9 feet and a perpendicular length of 18.5 feet. How many square feet of asphalt are needed to pave 4 adjacent spaces?", "keys": "9 [ENTER] 18.5 [f][RECT] 4 [×]", "yx": "Y:166.5 | X:4", "ans": "666 ft²"},
                    {"num": 10, "part": "C", "prompt": "Patio Planter Cutout: A rectangular stone patio measuring 15 feet by 12 feet has a parallelogram-shaped herb planter (base 4 feet, perpendicular height 3 feet) built in the center. How many square feet of stone paving surround the planter?", "keys": "15 [ENTER] 12 [f][RECT] 4 [ENTER] 3 [f][RECT] [-]", "yx": "Y:180 | X:12", "ans": "168 ft²"}
                ]
            },
            {
                "day_num": 21,
                "sec_num": "5.2",
                "title": "Areas of Triangles — Half of a Parallelogram",
                "big_ideas_ref": "Big Ideas Grade 6, Section 4.2 (Areas of Triangles)",
                "ccss": "CCSS.MATH.6.G.A.1",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_twin_comparator.png",
                "diagram_type": "polygon_area",
                "diagram_data": {"shape": "triangle", "b": 10, "h": 6, "area": 30, "caption": "Two congruent triangles always form a parallelogram of area b × h (60), so one triangle has area A = ½bh = 30."},
                "concept": "Any triangle can be duplicated and rotated to form a parallelogram with the same base b and height h. Because the two congruent triangles make up one bh parallelogram, the area of a single triangle is exactly half the area of the parallelogram: A = ½bh = (b × h) ÷ 2.",
                "examples": [
                    {
                        "title": "Example 1: Finding the Area of a Triangle",
                        "problem": "Find the area of a triangle with base b = 10 cm and perpendicular height h = 6 cm.",
                        "block_step": "A 10 cm by 6 cm rectangle has area 60 cm², so the triangle's area is half of 60: A = ½(10)(6) = 30 cm².",
                        "keys": ["10", "ENTER", "6", "g", "TRI"],
                        "stack_y": "10 (Base)",
                        "stack_x": "6 (Height)",
                        "ans": "30 cm²",
                        "note": "Always remember to divide the product of base and height by 2."
                    },
                    {
                        "title": "Example 2: Finding a Missing Height from Triangle Area",
                        "problem": "A triangular pennant has an area of 60 in.² and a base of 15 in. What is its height h?",
                        "block_step": "Since A = ½bh, double the triangle's area first to get the full rectangle area (2 × 60 = 120), then divide by the base 15: h = 120 ÷ 15 = 8 in.",
                        "keys": ["60", "ENTER", "2", "×", "15", "÷"],
                        "stack_y": "120 (2×Area)",
                        "stack_x": "15 -> 8",
                        "ans": "h = 8 in.",
                        "note": "Check: ½ × 15 × 8 = 60 in.²."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Triangular Park Pavilion Pennant: A nylon celebration pennant for the park pavilion has a base of 25 cm and a height of 60 cm. What is the area of the pennant?", "keys": "25 [ENTER] 60 [g][TRI]", "yx": "Y:25 | X:60", "ans": "750 cm²"},
                    {"num": 2, "part": "A", "prompt": "A right triangle has legs of 9 feet and 4 feet, and a slanted hypotenuse of 9.85 feet. What is its area?", "keys": "9 [ENTER] 4 [g][TRI]", "yx": "Y:9 | X:4", "ans": "18 ft²"},
                    {"num": 3, "part": "A", "prompt": "Find the area of a triangle with base b = 16 cm and height h = 11 cm.", "keys": "16 [ENTER] 11 [g][TRI]", "yx": "Y:16 | X:11", "ans": "88 cm²"},
                    {"num": 4, "part": "A", "prompt": "Find the area of a triangle with base b = 12.5 m and height h = 8.4 m.", "keys": "12.5 [ENTER] 8.4 [g][TRI]", "yx": "Y:12.5 | X:8.4", "ans": "52.5 m²"},
                    {"num": 5, "part": "B", "prompt": "Find the area of a triangle with base b = 4 1/2 inches and height h = 6 inches.", "keys": "4 [.] 1 [.] 2 [ENTER] 6 [g][TRI]", "yx": "Y:4 1/2 | X:6", "ans": "13 1/2 in.² (13.5)"},
                    {"num": 6, "part": "B", "prompt": "A triangle has an area of 54 cm² and a base of 12 cm. What is its perpendicular height?", "keys": "54 [ENTER] 2 [×] 12 [÷]", "yx": "Y:108 | X:12", "ans": "9 cm"},
                    {"num": 7, "part": "B", "prompt": "A triangle has an area of 84 m² and a perpendicular height of 14 m. What is its base?", "keys": "84 [ENTER] 2 [×] 14 [÷]", "yx": "Y:168 | X:14", "ans": "12 m"},
                    {"num": 8, "part": "B", "prompt": "Error Analysis: Leo found the area of a triangle with base 8 cm and height 5 cm as 40 cm². What did he forget to do, and what is the correct area?", "keys": "8 [ENTER] 5 [g][TRI]", "yx": "Y:8 | X:5", "ans": "20 cm² (He forgot to divide by 2)"},
                    {"num": 9, "part": "C", "prompt": "Sailboat Rigging: A sailboat has a triangular mainsail (base 12 ft, height 25 ft) and a triangular jib sail (base 8 ft, height 15 ft). What is the combined area of both sails?", "keys": "12 [ENTER] 25 [g][TRI] 8 [ENTER] 15 [g][TRI] [+]", "yx": "Y:150 | X:60", "ans": "210 ft²"},
                    {"num": 10, "part": "C", "prompt": "Rhombus Pathway Pavers: A decorative rhombus paver is formed by two identical triangles joined along a 40 cm diagonal, with a total perpendicular length of 70 cm across the second diagonal (A = ½ × d₁ × d₂). What is the area of one rhombus paver?", "keys": "40 [ENTER] 70 [g][TRI]", "yx": "Y:40 | X:70", "ans": "1,400 cm²"}
                ]
            },
            {
                "day_num": 22,
                "sec_num": "5.3",
                "title": "Areas of Trapezoids & Composite Figures",
                "big_ideas_ref": "Big Ideas Grade 6, Section 4.3 & 4.3 Ext (Trapezoids and Composite Figures)",
                "ccss": "CCSS.MATH.6.G.A.1",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_common_denominator.png",
                "diagram_type": "polygon_area",
                "diagram_data": {"shape": "composite", "rect_b": 12, "rect_h": 8, "tri_b": 12, "tri_h": 5, "caption": "Decomposing a Composite Shed Wall: Rectangle (12×8 = 96 ft²) + Roof Triangle (½×12×5 = 30 ft²) = 126 ft²."},
                "concept": "A trapezoid has two parallel bases, b₁ and b₂, and a perpendicular height h. Its area is half the product of the height and the sum of the bases: A = ½h(b₁ + b₂). To find the area of a composite figure, decompose it into non-overlapping rectangles, triangles, and trapezoids (or subtract cutout areas from an enclosing rectangle).",
                "examples": [
                    {
                        "title": "Example 1: Area of a Composite Figure (Rectangle + Triangle)",
                        "problem": "Find the total area of a 12 ft by 8 ft rectangular shed wall topped by a roof gable triangle (base 12 ft, height 5 ft).",
                        "block_step": "Rectangle area = 12 × 8 = 96 ft². Roof triangle area = ½ × 12 × 5 = 30 ft². Total area = 96 + 30 = 126 ft².",
                        "keys": ["g", "CLΣ", "12", "ENTER", "8", "f", "RECT", "Σ+", "12", "ENTER", "5", "g", "TRI", "Σ+", "f", "Σx"],
                        "stack_y": "96 + 30",
                        "stack_x": "126 (Total)",
                        "ans": "126 ft²",
                        "note": "Decompose the figure into familiar shapes and sum their areas."
                    },
                    {
                        "title": "Example 2: Area of a Trapezoid",
                        "problem": "Find the area of a trapezoid desk with parallel bases b₁ = 48 in. and b₂ = 36 in., and perpendicular depth h = 24 in.",
                        "block_step": "Add the two parallel bases (48 + 36 = 84), multiply by the height 24, and divide by 2: A = ½(24)(84) = 1,008 in.².",
                        "keys": ["48", "ENTER", "36", "+", "24", "g", "TRI"],
                        "stack_y": "84 (b₁+b₂)",
                        "stack_x": "24 -> 1008",
                        "ans": "1,008 in.²",
                        "note": "Equivalently, the average of the bases is (48+36)÷2 = 42 in., and 42 × 24 = 1,008 in.²."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the area of a trapezoid with parallel bases b₁ = 10 cm and b₂ = 14 cm, and height h = 6 cm.", "keys": "10 [ENTER] 14 [+] 6 [g][TRI]", "yx": "Y:24 | X:6", "ans": "72 cm²"},
                    {"num": 2, "part": "A", "prompt": "Find the area of a trapezoid with parallel bases b₁ = 18 ft and b₂ = 12 ft, and height h = 9 ft.", "keys": "18 [ENTER] 12 [+] 9 [g][TRI]", "yx": "Y:30 | X:9", "ans": "135 ft²"},
                    {"num": 3, "part": "A", "prompt": "An L-shaped floor plan consists of a 10 ft by 6 ft section and an 8 ft by 4 ft section. What is the total floor area?", "keys": "10 [ENTER] 6 [f][RECT] [Σ+] 8 [ENTER] 4 [f][RECT] [Σ+] [f][Σx]", "yx": "60 + 32", "ans": "92 ft²"},
                    {"num": 4, "part": "A", "prompt": "A directional sign is made of a 15 in. by 6 in. rectangle attached to a triangular arrowhead with base 10 in. and height 6 in. What is the total area of the sign?", "keys": "15 [ENTER] 6 [f][RECT] [Σ+] 10 [ENTER] 6 [g][TRI] [Σ+] [f][Σx]", "yx": "90 + 30", "ans": "120 in.²"},
                    {"num": 5, "part": "B", "prompt": "Find the area of a trapezoid with parallel bases b₁ = 8.5 m and b₂ = 5.5 m, and height h = 4.2 m.", "keys": "8.5 [ENTER] 5.5 [+] 4.2 [g][TRI]", "yx": "Y:14 | X:4.2", "ans": "29.4 m²"},
                    {"num": 6, "part": "B", "prompt": "Picture Frame Mat: A 10 in. by 8 in. rectangular mat board has a 6 in. by 4 in. rectangular photo window cut out of the center. What is the remaining area of the mat border?", "keys": "10 [ENTER] 8 [f][RECT] [Σ+] 6 [ENTER] 4 [f][RECT] [f][Σ-] [f][Σx]", "yx": "80 - 24", "ans": "56 in.²"},
                    {"num": 7, "part": "B", "prompt": "A trapezoid has an area of 90 cm² and parallel bases of 11 cm and 7 cm. What is its perpendicular height h?", "keys": "90 [ENTER] 2 [×] 11 [ENTER] 7 [+] [÷]", "yx": "Y:180 | X:18", "ans": "10 cm"},
                    {"num": 8, "part": "B", "prompt": "Mini-Golf Fairway: A mini-golf hole is made of a 12 ft by 5 ft rectangular fairway connected to a trapezoid green (bases 5 ft and 9 ft, height 4 ft). How much turf is needed to cover the hole?", "keys": "60 [Σ+] 5 [ENTER] 9 [+] 4 [g][TRI] [Σ+] [f][Σx]", "yx": "60 + 28", "ans": "88 ft²"},
                    {"num": 9, "part": "C", "prompt": "Two Ways to Measure a Trapezoid: Find the area of a right trapezoid with bases 10 cm and 16 cm and height 8 cm both by using the trapezoid formula and by splitting it into a 10×8 rectangle and a 6×8 right triangle.", "keys": "10 [ENTER] 16 [+] 8 [g][TRI]", "yx": "Y:26 | X:8", "ans": "104 cm² (80 + 24 = 104)"},
                    {"num": 10, "part": "C", "prompt": "Backyard Landscaping: A 20 ft by 15 ft rectangular yard contains a triangular flowerbed (base 8 ft, height 6 ft) and a 5 ft by 5 ft square storage shed. How many square feet of grass lawn remain?", "keys": "300 [Σ+] 24 [f][Σ-] 25 [f][Σ-] [f][Σx]", "yx": "300 - 24 - 25", "ans": "251 ft²"}
                ]
            },
            {
                "day_num": 23,
                "sec_num": "5.4",
                "title": "Polygons in the Coordinate Plane & Base-60 Elapsed Time",
                "big_ideas_ref": "Big Ideas Grade 6, Section 4.4 (Polygons in the Coordinate Plane) & Time Lab",
                "ccss": "CCSS.MATH.6.G.A.3",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "clock_dial",
                "diagram_data": {"start": "1:45", "add": "+1h 35m", "end": "3:20", "caption": "Base-60 Elapsed Time: 1:45 + 1 hr 35 min regroups 60 minutes into +1 hour -> 3:20."},
                "concept": "To find the length of a horizontal segment in Quadrant I, subtract the x-coordinates; for a vertical segment, subtract the y-coordinates. When calculating elapsed time, remember that hours and minutes use Base-60 (60 minutes = 1 hour), so regroup 60 minutes whenever minutes exceed 59 or when borrowing 1 hour.",
                "examples": [
                    {
                        "title": "Example 1: Coordinate Rectangle Perimeter & Area",
                        "problem": "A rectangle has vertices (2, 3), (9, 3), (9, 8), and (2, 8). Find its width, height, perimeter, and area.",
                        "block_step": "Horizontal width = 9 - 2 = 7 units. Vertical height = 8 - 3 = 5 units. Perimeter = 2(7 + 5) = 24 units; Area = 7 × 5 = 35 square units.",
                        "keys": ["9", "ENTER", "2", "-", "8", "ENTER", "3", "-", "f", "RECT"],
                        "stack_y": "7 (Width)",
                        "stack_x": "5 (Height) -> 35",
                        "ans": "Width = 7, Height = 5, Perimeter = 24, Area = 35",
                        "note": "Subtract x-coordinates for horizontal length and y-coordinates for vertical length."
                    },
                    {
                        "title": "Example 2: Base-60 Elapsed Time & Decimal Hours",
                        "problem": "A 3D print starts at 9:40 AM and runs for 2 hours 50 minutes. When does it finish, and what is 3 hours 15 minutes written as a decimal number of hours?",
                        "block_step": "9 hr 40 min + 2 hr 50 min = 11 hr 90 min = 12 hr 30 min (12:30 PM). Since 15 min = 15/60 = 0.25 hr, 3 hr 15 min = 3.25 hours.",
                        "keys": ["CLK", "9.40", "ENTER", "2.50", "+", "3.15", "f", "▸HR"],
                        "stack_y": "12.30 (12:30)",
                        "stack_x": "3.25 hr",
                        "ans": "Finishes at 12:30 PM; 3.25 hours",
                        "note": "Divide minutes by 60 to convert minutes into decimal hours."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the length of the horizontal segment connecting (3, 4) and (11, 4) in the coordinate plane.", "keys": "11 [ENTER] 3 [-]", "yx": "Y:11 | X:3", "ans": "8 units"},
                    {"num": 2, "part": "A", "prompt": "A rectangle has vertices at (1, 2), (10, 2), (10, 8), and (1, 8). What is its area?", "keys": "10 [ENTER] 1 [-] 8 [ENTER] 2 [-] [f][RECT]", "yx": "Y:9 | X:6", "ans": "54 square units"},
                    {"num": 3, "part": "A", "prompt": "Aquarium Filter Cycle: The main bio-filter pump starts its morning cycle at 7:10 AM and runs for 3 hours and 48 minutes. At what time does the cycle finish?", "keys": "[CLK] 7.10 [ENTER] 3.48 [+]", "yx": "Y:7.10 | X:3.48", "ans": "10:58 AM"},
                    {"num": 4, "part": "A", "prompt": "Convert 2 hours 30 minutes into decimal hours, and convert 4 hours 45 minutes into decimal hours.", "keys": "2.30 [f][▸HR]; 4.45 [f][▸HR]", "yx": "2.5 and 4.75", "ans": "2.5 hours; 4.75 hours"},
                    {"num": 5, "part": "B", "prompt": "Science Museum Fountain Shift: The courtyard water fountain turns on at 8:15 AM and shuts down for maintenance at 3:05 PM. For how many hours and minutes did the fountain run?", "keys": "[CLK] 15.05 [ENTER] 8.15 [-]", "yx": "Y:15.05 | X:8.15", "ans": "6 hours 50 minutes"},
                    {"num": 6, "part": "B", "prompt": "Convert 1.75 hours into hours and minutes.", "keys": "1.75 [g][▸HMS]", "yx": "1.75 -> H.MM", "ans": "1 hour 45 minutes"},
                    {"num": 7, "part": "B", "prompt": "A train departs at 8:50 AM and arrives at 11:25 AM. How long was the train ride in hours and minutes?", "keys": "[CLK] 11.25 [ENTER] 8.50 [-]", "yx": "Y:11.25 | X:8.50", "ans": "2 hours 35 minutes"},
                    {"num": 8, "part": "B", "prompt": "A right triangle in the coordinate plane has vertices at (2, 1), (10, 1), and (2, 7). What is the area of the triangle?", "keys": "8 [ENTER] 6 [g][TRI]", "yx": "Y:8 | X:6", "ans": "24 square units"},
                    {"num": 9, "part": "C", "prompt": "Saturday Pet-Sitting: You pet-sit a neighbor's dogs from 9:15 AM until 2:45 PM on Saturday at a rate of $18.50 per hour. How many hours did you work, and how much did you earn?", "keys": "5.5 [ENTER] 18.50 [×]", "yx": "Y:5.5 | X:18.50", "ans": "5.5 hours (5 hr 30 min); $101.75"},
                    {"num": 10, "part": "C", "prompt": "Coordinate Park Blueprint: A rectangular park has vertices (2, 2), (14, 2), (14, 11), and (2, 11), where each grid unit represents 10 yards. What are the perimeter (in yards) and area (in square yards) of the park?", "keys": "12 [ENTER] 9 [f][RECT]", "yx": "Y:12 | X:9", "ans": "Perimeter = 420 yd; Area = 10,800 yd²"}
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
        "kit_summary": "Place Value Studio (PLACE-01) + Fraction Studio (FRAC-01)",
        "hero_png": "place_value_regrouping.png",
        "coach_misconception": "Students confuse the subtraction operator [-] with the negative sign [+/-], think -18 > -5 because 18 > 5, confuse Opposite ([+/-]) with Absolute Value ([g] [|x|]), and reverse (x, y) coordinates.",
        "coach_remediation": "Use Place Value Studio (PLACE-01) tokens and the SC-6 Number Line ([f] [LINE]) to model opposites and zero pairs, test inequalities with [f] [>] and [g] [<], contrast [+/-] (flip sign) with [g] [|x|] (always positive distance from 0), and use the Elevator Rule (walk across x first, ride up/down y second).",
        "sections": [
            {
                "day_num": 24,
                "sec_num": "6.1",
                "title": "Integers — Positive & Negative Numbers and Opposites",
                "big_ideas_ref": "Big Ideas Grade 6, Section 6.1 (Integers)",
                "ccss": "CCSS.MATH.6.NS.C.5",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "zero_pairs",
                "diagram_data": {"pos": 3, "neg": 5, "net": -2, "caption": "3 Positive (+1) units + 5 Negative (-1) units: 3 Zero Pairs cancel to 0, leaving 2 Negative (-2)."},
                "concept": "Integers are the set of whole numbers and their opposites (... -3, -2, -1, 0, 1, 2, 3 ...). Positive numbers are greater than 0 and represent gains, deposits, or elevations above sea level; negative numbers are less than 0 and represent losses, withdrawals, or depths below sea level. Two numbers that are the same distance from 0 on opposite sides are called opposites, and their sum is always 0 (a Zero Pair).",
                "examples": [
                    {
                        "title": "Example 1: Writing Integers and Finding Opposites",
                        "problem": "Find the opposite of -15 and the value of -(-15).",
                        "block_step": "-15 is 15 units left of 0, so its opposite is +15 (15 units right of 0). Combining 15 negative units and 15 positive units forms 15 Zero Pairs (= 0).",
                        "keys": ["f", "LINE", "15", "+/-", "ENTER", "15", "+"],
                        "stack_y": "-15",
                        "stack_x": "15 -> 0",
                        "ans": "Opposite of -15 is +15; -15 + 15 = 0",
                        "note": "Zero (0) is neither positive nor negative, and its opposite is 0."
                    },
                    {
                        "title": "Example 2: Real-World Elevation & Bank Ledger",
                        "problem": "An account starts at $0, receives a $35 deposit, pays a $50 bill, and receives a $20 deposit. What is the final balance?",
                        "block_step": "Total deposits are +35 + 20 = +55. Combining +55 with the -50 withdrawal cancels 50 Zero Pairs, leaving +$5.",
                        "keys": ["35", "ENTER", "50", "+/-", "+", "20", "+"],
                        "stack_y": "-15 (Step 1)",
                        "stack_x": "20 -> +5",
                        "ans": "+$5",
                        "note": "Deposits are represented by positive integers and withdrawals by negative integers."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Write the integer that represents '25 feet below sea level' and state its opposite.", "keys": "25 [+/-] -> -25; [+/-] -> 25", "yx": "-25 <-> +25", "ans": "-25; Opposite = +25"},
                    {"num": 2, "part": "A", "prompt": "Find the opposite of -42, and then evaluate -(-42).", "keys": "42 [+/-] [+/-]", "yx": "-42 -> +42", "ans": "+42; and +42"},
                    {"num": 3, "part": "A", "prompt": "A research submarine is at an elevation of -18 meters and rises 18 meters. What is its new elevation?", "keys": "18 [+/-] [ENTER] 18 [+]", "yx": "Y:-18 | X:18", "ans": "0 m (Sea level)"},
                    {"num": 4, "part": "A", "prompt": "You combine 6 positive (+1) units and 6 negative (-1) units. What is the net value?", "keys": "6 [ENTER] 6 [+/-] [+]", "yx": "Y:6 | X:-6", "ans": "0"},
                    {"num": 5, "part": "B", "prompt": "A desert canyon hiker starts at -120 feet relative to sea level and climbs 120 feet up the canyon wall. What is her elevation now?", "keys": "120 [+/-] [ENTER] 120 [+]", "yx": "Y:-120 | X:120", "ans": "0 ft"},
                    {"num": 6, "part": "B", "prompt": "Which integer is its own opposite? Explain why using a number line.", "keys": "0 [+/-]", "yx": "X: 0", "ans": "0 (0 is 0 units from itself)"},
                    {"num": 7, "part": "B", "prompt": "A freezer thermometer starts at 0°F, drops 12°F, and then rises 19°F. What is the new temperature?", "keys": "12 [+/-] [ENTER] 19 [+]", "yx": "Y:-12 | X:19", "ans": "+7°F"},
                    {"num": 8, "part": "B", "prompt": "In golf, -3 means 3 strokes under par. If a golfer shoots -3 on Saturday and +3 on Sunday, what is her combined score relative to par?", "keys": "3 [+/-] [ENTER] 3 [+]", "yx": "Y:-3 | X:3", "ans": "0 (Even par)"},
                    {"num": 9, "part": "C", "prompt": "An elevator starts at the Ground Lobby (Floor 0), goes up 14 floors, goes down 20 floors to the underground garage, and then goes up 9 floors. On which floor does it stop?", "keys": "14 [ENTER] 20 [+/-] [+] 9 [+]", "yx": "Y:-6 | X:9", "ans": "Floor 3"},
                    {"num": 10, "part": "C", "prompt": "Four-Season Robotics Club Treasury: Over four seasons, the robotics club treasury records +$14,500 in fall grants, -$3,200 in winter parts, +$8,900 in spring sponsorships, and -$1,400 in travel fees. What is the club's net treasury balance?", "keys": "14500 [ENTER] 3200 [-] 8900 [+] 1400 [-]", "yx": "Y:20200 | X:1400", "ans": "+$18,800"}
                ]
            },
            {
                "day_num": 25,
                "sec_num": "6.2",
                "title": "Comparing & Ordering Integers and Rational Numbers",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 6.2 & 6.3 (Comparing & Ordering Integers and Rational Numbers)",
                "ccss": "CCSS.MATH.6.NS.C.7",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_twin_comparator.png",
                "diagram_type": "zero_pairs",
                "diagram_data": {"pos": 2, "neg": 5, "net": -3, "caption": "Number Line Rule: Numbers further to the RIGHT are always greater (-5 is to the right of -18, so -5 > -18)."},
                "concept": "On a horizontal number line, numbers increase from left to right and decrease from right to left. For negative numbers, a number closer to 0 is further to the right and therefore GREATER (so -5 > -18 because -5°F is warmer than -18°F). To compare negative fractions and decimals, convert them to the same form or common denominator first.",
                "examples": [
                    {
                        "title": "Example 1: Comparing Negative Integers on a Number Line",
                        "problem": "Compare -5 and -18 using > or <.",
                        "block_step": "On a horizontal number line, -5 is 5 units left of 0, while -18 is 18 units left of 0. Because -5 is to the right of -18, -5 > -18.",
                        "keys": ["18", "+/-", "ENTER", "5", "+/-", "f", ">"],
                        "stack_y": "-18 (Y)",
                        "stack_x": "-5 (X) -> YES",
                        "ans": "-5 > -18",
                        "note": "Further right on the number line is always greater ([f][>] flashes YES!)."
                    },
                    {
                        "title": "Example 2: Comparing Negative Fractions & Decimals",
                        "problem": "Compare -4/5 and -0.75 using > or <.",
                        "block_step": "Convert -4/5 to a decimal: -4/5 = -0.80. On the number line, -0.75 is closer to 0 (further right) than -0.80, so -0.80 < -0.75 (meaning -0.75 > -4/5).",
                        "keys": ["0.75", "+/-", "ENTER", ".", "4", ".", "5", "+/-", "FDISP", "g", "<"],
                        "stack_y": "-0.75 (Y)",
                        "stack_x": "-0.80 (X) -> YES",
                        "ans": "-4/5 < -0.75 (-0.75 is greater)",
                        "note": "In common denominator form: -4/5 = -16/20 and -3/4 = -15/20, and -16/20 < -15/20."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Which temperature is warmer (greater): -12°C or -5°C? Write an inequality comparing them.", "keys": "5 [+/-] [ENTER] 12 [+/-] [g][<]", "yx": "Y:-5 | X:-12", "ans": "-5°C (-12 < -5)"},
                    {"num": 2, "part": "A", "prompt": "Compare -9 and -2 using > or <.", "keys": "2 [+/-] [ENTER] 9 [+/-] [g][<]", "yx": "Y:-2 | X:-9", "ans": "-9 < -2"},
                    {"num": 3, "part": "A", "prompt": "Compare -15 and 0 using > or <.", "keys": "0 [ENTER] 15 [+/-] [g][<]", "yx": "Y:0 | X:-15", "ans": "-15 < 0"},
                    {"num": 4, "part": "A", "prompt": "Order the integers from least to greatest: 4, -7, 0, -2, -10.", "keys": "Left-to-right on [f][LINE]", "yx": "Coldest to warmest", "ans": "-10, -7, -2, 0, 4"},
                    {"num": 5, "part": "B", "prompt": "Compare -3/4 and -0.6 using > or <.", "keys": "0.6 [+/-] [ENTER] 0.75 [+/-] [g][<]", "yx": "Y:-0.6 | X:-0.75", "ans": "-3/4 < -0.6 (-0.6 is greater)"},
                    {"num": 6, "part": "B", "prompt": "Compare -2 1/2 and -2.3 using > or <.", "keys": "2.3 [+/-] [ENTER] 2.5 [+/-] [g][<]", "yx": "Y:-2.3 | X:-2.5", "ans": "-2 1/2 < -2.3"},
                    {"num": 7, "part": "B", "prompt": "Compare -5/8 and -7/8 using > or <.", "keys": "[.] 7 [.] 8 [+/-] [ENTER] [.] 5 [.] 8 [+/-] [f][>]", "yx": "-0.625 > -0.875", "ans": "-5/8 > -7/8"},
                    {"num": 8, "part": "B", "prompt": "Error Analysis: Leo says -4.5 > -4.1 because 4.5 > 4.1. Explain why -4.1 is actually greater using a number line.", "keys": "4.5 [+/-] [ENTER] 4.1 [+/-] [g][<]", "yx": "-4.5 < -4.1", "ans": "-4.1 is closer to 0 (further to the right) than -4.5"},
                    {"num": 9, "part": "C", "prompt": "Order the rational numbers -1.5, 1 1/4, -1 3/4, and -0.5 from least to greatest.", "keys": "-1.75, -1.5, -0.5, 1.25", "yx": "All pairwise [g][<]=1", "ans": "-1 3/4, -1.5, -0.5, 1 1/4"},
                    {"num": 10, "part": "C", "prompt": "Three marine biologists are diving at elevations of -14.8 m, -14 1/2 m, and -15.2 m. Which diver is the deepest (least elevation), and which is the shallowest (greatest elevation)?", "keys": "-15.2 < -14.8 < -14.5", "yx": "-14 1/2 = -14.5", "ans": "Deepest: -15.2 m; Shallowest: -14 1/2 m"}
                ]
            },
            {
                "day_num": 26,
                "sec_num": "6.3",
                "title": "Absolute Value — Distance from Zero on the Number Line",
                "big_ideas_ref": "Big Ideas Grade 6, Section 6.4 (Absolute Value)",
                "ccss": "CCSS.MATH.6.NS.C.7c",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "zero_pairs",
                "diagram_data": {"pos": 6, "neg": 6, "net": 0, "caption": "Both -6 and +6 are 6 units from 0 on the number line: |-6| = 6 and |+6| = 6. Distance is never negative."},
                "concept": "The absolute value of a number is its distance from 0 on a number line, written as |x|. Because distance is never negative, the absolute value of any non-zero number is always positive: |-6| = 6 and |6| = 6. Be careful not to confuse Opposite (which flips + and -) with Absolute Value (which measures positive distance from 0).",
                "examples": [
                    {
                        "title": "Example 1: Evaluating Absolute Value vs. Opposite",
                        "problem": "Evaluate |-14|, |14|, and -|-14|.",
                        "block_step": "-14 is 14 units from 0, so |-14| = 14 and |14| = 14. In -|-14|, evaluate the absolute value bars first (|-14| = 14), then apply the outside negative sign to get -14.",
                        "keys": ["14", "+/-", "g", "|x|"],
                        "stack_y": "|-14|",
                        "stack_x": "+14",
                        "ans": "|-14| = 14, |14| = 14, -|-14| = -14",
                        "note": "Treat absolute value bars | | like grouping symbols: evaluate inside them first!"
                    },
                    {
                        "title": "Example 2: Multi-Step Absolute Value Expression 50 - |-18|",
                        "problem": "Evaluate 50 - |-18|.",
                        "block_step": "First find |-18| = 18, then subtract from 50: 50 - 18 = 32.",
                        "keys": ["50", "ENTER", "18", "+/-", "g", "|x|", "-"],
                        "stack_y": "50",
                        "stack_x": "18 -> 32",
                        "ans": "32",
                        "note": "Evaluate |-18| = +18 first before subtracting from 50."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Evaluate |-125|.", "keys": "125 [+/-] [g][|x|]", "yx": "X: 125", "ans": "125"},
                    {"num": 2, "part": "A", "prompt": "Evaluate |-18| + |12|.", "keys": "18 [+/-] [g][|x|] [ENTER] 12 [+]", "yx": "Y:18 | X:12", "ans": "30"},
                    {"num": 3, "part": "A", "prompt": "Evaluate |-4.8| + |-3.2|.", "keys": "4.8 [+/-] [g][|x|] [ENTER] 3.2 [+/-] [g][|x|] [+]", "yx": "Y:4.8 | X:3.2", "ans": "8.0"},
                    {"num": 4, "part": "A", "prompt": "Evaluate |-35| - |-19|.", "keys": "35 [+/-] [g][|x|] [ENTER] 19 [+/-] [g][|x|] [-]", "yx": "Y:35 | X:19", "ans": "16"},
                    {"num": 5, "part": "B", "prompt": "Compare |-12| and |9| using > or <.", "keys": "12 > 9", "yx": "Y:12 | X:9", "ans": "|-12| > |9| (12 > 9)"},
                    {"num": 6, "part": "B", "prompt": "Evaluate -|-24|.", "keys": "24 [+/-] [g][|x|] [+/-]", "yx": "24 -> -24", "ans": "-24"},
                    {"num": 7, "part": "B", "prompt": "Evaluate 50 - |-18|.", "keys": "50 [ENTER] 18 [+/-] [g][|x|] [-]", "yx": "Y:50 | X:18", "ans": "32"},
                    {"num": 8, "part": "B", "prompt": "Order the values from least to greatest: |-8|, -6, |-3|, 0, -|-9|.", "keys": "Values: 8, -6, 3, 0, -9", "yx": "-9, -6, 0, 3, 8", "ans": "-|-9|, -6, 0, |-3|, |-8|"},
                    {"num": 9, "part": "C", "prompt": "A scuba diver is at -32 feet and a seagull is flying at +25 feet relative to sea level (0 ft). Which is closer to sea level, and by how many feet?", "keys": "32 [+/-] [g][|x|] [ENTER] 25 [-]", "yx": "Y:32 | X:25", "ans": "Seagull is closer by 7 feet (25 < 32)"},
                    {"num": 10, "part": "C", "prompt": "Two bank accounts have balances of -$45 and -$28. Which account has the greater debt (magnitude), and which account has the greater balance?", "keys": "|-45|=45 > |-28|=28", "yx": "-45 < -28", "ans": "Greater debt: -$45 ($45); Greater balance: -$28"}
                ]
            },
            {
                "day_num": 27,
                "sec_num": "6.4",
                "title": "The Coordinate Plane — Four Quadrants & Axis Reflections",
                "big_ideas_ref": "Big Ideas Grade 6, Section 6.5 (The Coordinate Plane)",
                "ccss": "CCSS.MATH.6.NS.C.6",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "coord_plane",
                "diagram_data": {"pts": [("(4,3) QI", 4, 3), ("(-4,3) QII", -4, 3), ("(-4,-3) QIII", -4, -3), ("(4,-3) QIV", 4, -3)], "caption": "Four Quadrants & Reflections: Reflecting across the y-axis flips the x-sign; reflecting across the x-axis flips the y-sign."},
                "concept": "The horizontal x-axis and vertical y-axis intersect at the origin (0, 0) and divide the coordinate plane into four quadrants: QI (+, +), QII (-, +), QIII (-, -), and QIV (+, -). To plot an ordered pair (x, y), move horizontally along the x-axis first, then vertically along the y-axis. Reflecting a point across the x-axis changes the sign of y; reflecting across the y-axis changes the sign of x.",
                "examples": [
                    {
                        "title": "Example 1: Identifying Quadrants I, II, III, and IV",
                        "problem": "Identify the quadrant for A(-6, 5), B(4, -7), and C(-3, -8).",
                        "block_step": "A(-, +) goes left 6, up 5 -> Quadrant II. B(+, -) goes right 4, down 7 -> Quadrant IV. C(-, -) goes left 3, down 8 -> Quadrant III.",
                        "keys": ["6", "+/-", "ENTER", "5"],
                        "stack_y": "-6 (x: Left)",
                        "stack_x": "+5 (y: Up)",
                        "ans": "A: Quadrant II, B: Quadrant IV, C: Quadrant III",
                        "note": "QI: (+,+), QII: (-,+), QIII: (-,-), QIV: (+,-)."
                    },
                    {
                        "title": "Example 2: Reflecting Points Across the Axes",
                        "problem": "Reflect P(-5, 8) across the x-axis, and then reflect the resulting point across the y-axis.",
                        "block_step": "Across the x-axis: keep x = -5 and flip y to -8 -> (-5, -8). Across the y-axis: flip x to +5 and keep y = -8 -> (5, -8).",
                        "keys": ["5", "+/-", "ENTER", "8", "+/-", "x⇄y", "+/-", "x⇄y"],
                        "stack_y": "+5 (New x)",
                        "stack_x": "-8 (New y)",
                        "ans": "Step 1: (-5, -8); Final: (5, -8) in Quadrant IV",
                        "note": "Reflecting across both axes flips the signs of both coordinates."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Name the Quadrant (I, II, III, or IV) that contains the point (7, -4).", "keys": "(+, -) -> Right, Down", "yx": "Y:7 | X:-4", "ans": "Quadrant IV"},
                    {"num": 2, "part": "A", "prompt": "Name the Quadrant that contains the point (-9, -2).", "keys": "(-, -) -> Left, Down", "yx": "Y:-9 | X:-2", "ans": "Quadrant III"},
                    {"num": 3, "part": "A", "prompt": "Name the Quadrant that contains the point (-5, 11).", "keys": "(-, +) -> Left, Up", "yx": "Y:-5 | X:11", "ans": "Quadrant II"},
                    {"num": 4, "part": "A", "prompt": "Reflect the point (6, 9) across the y-axis. What are the coordinates of the reflected point?", "keys": "6 [+/-] -> -6", "yx": "Y:-6 | X:9", "ans": "(-6, 9)"},
                    {"num": 5, "part": "B", "prompt": "Reflect the point (6, 9) across the x-axis. What are the coordinates of the reflected point?", "keys": "9 [+/-] -> -9", "yx": "Y:6 | X:-9", "ans": "(6, -9)"},
                    {"num": 6, "part": "B", "prompt": "Reflect the point (-3, -7) across the x-axis.", "keys": "7 [+/-] [+/-] -> +7", "yx": "Y:-3 | X:7", "ans": "(-3, 7)"},
                    {"num": 7, "part": "B", "prompt": "Reflect the point (-8, 4) across the y-axis, and then reflect the new point across the x-axis.", "keys": "Flip x -> (8,4); flip y -> (8,-4)", "yx": "Y:8 | X:-4", "ans": "(8, -4)"},
                    {"num": 8, "part": "B", "prompt": "Which axis does the point (0, -9) lie on, and which axis does the point (-7, 0) lie on?", "keys": "0 sideways vs 0 up/down", "yx": "(0,-9) & (-7,0)", "ans": "(0, -9) on y-axis; (-7, 0) on x-axis"},
                    {"num": 9, "part": "C", "prompt": "Starting at (4, -5), you move 7 units left and 8 units up. What are your final coordinates, and which quadrant are you in?", "keys": "4 [ENTER] 7 [-]; 5 [+/-] [ENTER] 8 [+]", "yx": "Y:-3 | X:3", "ans": "(-3, 3) in Quadrant II"},
                    {"num": 10, "part": "C", "prompt": "Points A(-4, 2), B(4, 2), and C(4, -5) are three vertices of a rectangle. What are the coordinates of the fourth vertex D, and which quadrant is it in?", "keys": "Match x of A (-4) & y of C (-5)", "yx": "Y:-4 | X:-5", "ans": "D(-4, -5) in Quadrant III"}
                ]
            },
            {
                "day_num": 28,
                "sec_num": "6.5",
                "title": "Distances in the Coordinate Plane — Absolute Value & Quadrants",
                "big_ideas_ref": "Big Ideas Grade 6, Section 6.5 Ext (Distances on the Coordinate Plane)",
                "ccss": "CCSS.MATH.6.NS.C.8",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "coord_plane",
                "diagram_data": {"pts": [("(-6,4)", -6, 4), ("(9,4)", 9, 4)], "caption": "Distance from (-6, 4) to (9, 4): |-6| + |9| = 6 + 9 = 15 units across the y-axis."},
                "concept": "To find the distance between two points that share the same x-coordinate or the same y-coordinate: if the points lie in DIFFERENT quadrants (across an axis), add the absolute values of their differing coordinates; if they lie in the SAME quadrant, subtract the absolute values of their differing coordinates. Equivalently, distance is always |a - b|.",
                "examples": [
                    {
                        "title": "Example 1: Cross-Axis Distance vs. Same-Quadrant Distance",
                        "problem": "Find the distance between (-6, 4) and (9, 4), and between (-12, -3) and (-4, -3).",
                        "block_step": "Across the y-axis: |-6| + |9| = 6 + 9 = 15 units. Same quadrant: |-12| - |-4| = 12 - 4 = 8 units.",
                        "keys": ["6", "+/-", "ENTER", "9", "-", "g", "|x|"],
                        "stack_y": "-15 (Diff)",
                        "stack_x": "15 (Dist)",
                        "ans": "15 units; and 8 units",
                        "note": "In both cases, the absolute difference |x₁ - x₂| gives the exact positive distance."
                    },
                    {
                        "title": "Example 2: 4-Quadrant Rectangle Perimeter & Area",
                        "problem": "A rectangle has vertices (-4, 6), (5, 6), (5, -2), and (-4, -2). Find its perimeter and area.",
                        "block_step": "Width from -4 to 5 is |-4| + |5| = 9 units. Height from 6 to -2 is |6| + |-2| = 8 units. Perimeter = 2(9 + 8) = 34 units; Area = 9 × 8 = 72 square units.",
                        "keys": ["4", "+/-", "ENTER", "5", "-", "g", "|x|", "6", "ENTER", "2", "+/-", "-", "f", "RECT"],
                        "stack_y": "9 (Width)",
                        "stack_x": "8 (Height) -> 72",
                        "ans": "Width = 9, Height = 8, Perimeter = 34, Area = 72",
                        "note": "Add distances to the axis whenever a side crosses the x-axis or y-axis."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the distance between (-12, 5) and (15, 5).", "keys": "12 [+/-] [ENTER] 15 [-] [g][|x|]", "yx": "|-27| = 27", "ans": "27 units"},
                    {"num": 2, "part": "A", "prompt": "Find the vertical distance between (-3, -4) and (-3, -15).", "keys": "4 [+/-] [ENTER] 15 [+/-] [-] [g][|x|]", "yx": "|+11| = 11", "ans": "11 units"},
                    {"num": 3, "part": "A", "prompt": "Find the vertical distance between (7, 9) and (7, -6).", "keys": "9 [ENTER] 6 [+/-] [-] [g][|x|]", "yx": "|15| = 15", "ans": "15 units"},
                    {"num": 4, "part": "A", "prompt": "Find the horizontal distance between (-14, 2) and (-5, 2).", "keys": "14 [+/-] [ENTER] 5 [+/-] [-] [g][|x|]", "yx": "|-9| = 9", "ans": "9 units"},
                    {"num": 5, "part": "B", "prompt": "Find the distance between (-3.5, 4) and (6.5, 4).", "keys": "3.5 [+/-] [ENTER] 6.5 [-] [g][|x|]", "yx": "|-10| = 10", "ans": "10 units"},
                    {"num": 6, "part": "B", "prompt": "Find the distance between (2, -4 1/2) and (2, 3 1/2).", "keys": "4.5 [+/-] [ENTER] 3.5 [-] [g][|x|]", "yx": "|-8| = 8", "ans": "8 units"},
                    {"num": 7, "part": "B", "prompt": "A horizontal segment starts at (-6, 3) and extends 10 units to the right. What are the coordinates of its right endpoint?", "keys": "6 [+/-] [ENTER] 10 [+]", "yx": "Y:-6 | X:10", "ans": "(4, 3)"},
                    {"num": 8, "part": "B", "prompt": "Error Analysis: To find the distance from (-5, 2) to (8, 2), Sam subtracted 8 - 5 = 3. Explain why the distance is 13 units, not 3 units.", "keys": "5 [+/-] [ENTER] 8 [-] [g][|x|]", "yx": "5 to 0 + 8 past 0", "ans": "13 units (They lie on opposite sides of the y-axis: |-5| + |8| = 13)"},
                    {"num": 9, "part": "C", "prompt": "Archaeological Survey Grid: A rectangular excavation zone has corners at (-4, 6), (5, 6), (5, -2), and (-4, -2). What are the perimeter and area of the zone?", "keys": "Width 9, Height 8", "yx": "Y:9 | X:8", "ans": "Perimeter = 34 units, Area = 72 sq units"},
                    {"num": 10, "part": "C", "prompt": "City Grid Walk: On a map where 1 grid unit equals 0.5 mile, you walk from (-6, -2) north to (-6, 8), and then east to (4, 8). How many total miles did you walk?", "keys": "10 + 10 = 20 units × 0.5", "yx": "Y:20 | X:0.5", "ans": "20 grid units = 10 miles"}
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
        "kit_summary": "Place Value Studio (PLACE-01) + Fraction Studio (FRAC-01)",
        "hero_png": "place_value_regrouping.png",
        "coach_misconception": "Students treat '=' as 'write the answer', translate '8 less than n' backwards as 8 - n, resent writing -14 under both sides of x + 14 = 39, and confuse open vs. solid inequality circles.",
        "coach_remediation": "Model '=' as a Balance Scale using Place Value Studio (PLACE-01) and Fraction Studio (FRAC-01). Solve 1-step equations with inverse operations on both sides, verify your solution with the SC-6 Equality Test [≠] (which flashes NO when Left = Right!), and test inequalities on [f] [LINE] with [f] [≥] and [g] [≤] (which flash YES or NO).",
        "sections": [
            {
                "day_num": 29,
                "sec_num": "7.1",
                "title": "Writing Equations in One Variable — The Balance Scale",
                "big_ideas_ref": "Big Ideas Grade 6, Section 7.1 (Writing Equations in One Variable)",
                "ccss": "CCSS.MATH.6.EE.B.5",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "balance_scale",
                "diagram_data": {"left": "3x - 5", "right": "19", "sol": "x = 8", "caption": "Balance Scale: Left Side (3x - 5) must equal Right Side (19). When x = 8, 3(8) - 5 = 19."},
                "concept": "An equation is a mathematical sentence that uses an equal sign (=) to state that two expressions have the exact same value—just like the two pans of a balanced scale. A value of the variable that makes the equation true is called a solution of the equation.",
                "examples": [
                    {
                        "title": "Example 1: Testing Whether a Number is a Solution",
                        "problem": "Tell whether x = 7 or x = 9 is a solution of 4x + 5 = 41.",
                        "block_step": "Substitute x = 7: 4(7) + 5 = 33 != 41 (Not a solution). Substitute x = 9: 4(9) + 5 = 41 = 41 (Solution!).",
                        "keys": ["41", "ENTER", "4", "ENTER", "9", "×", "5", "+", "≠"],
                        "stack_y": "41 (Right)",
                        "stack_x": "41 (Left) -> NO",
                        "ans": "x = 9 is the solution (41 = 41)",
                        "note": "Pressing [≠] flashes NO (not unequal), proving Left = Right = 41!"
                    },
                    {
                        "title": "Example 2: Translating Word Sentences into Equations",
                        "problem": "Write the word sentence '8 less than a number n is 25' as an equation and find n.",
                        "block_step": "'8 less than n' means start with n and subtract 8: n - 8 = 25 (never 8 - n = 25). Since 33 - 8 = 25, n = 33.",
                        "keys": ["25", "ENTER", "8", "+", "25", "x⇄y", "8", "-", "≠"],
                        "stack_y": "25 (Right)",
                        "stack_x": "25 (33-8) -> NO",
                        "ans": "n - 8 = 25; n = 33",
                        "note": "Phrases like 'less than' and 'subtracted from' reverse the order of the terms."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Tell whether x = 6 or x = 8 is a solution of 5x - 7 = 33.", "keys": "33 [ENTER] 5 [ENTER] 8 [×] 7 [-] [≠]", "yx": "Y:33 | X:33 (NO)", "ans": "x = 8 (5(8)-7 = 33)"},
                    {"num": 2, "part": "A", "prompt": "Tell whether y = 12 or y = 15 is a solution of y ÷ 3 + 4 = 9.", "keys": "9 [ENTER] 15 [ENTER] 3 [÷] 4 [+] [≠]", "yx": "Y:9 | X:9 (NO)", "ans": "y = 15 (15÷3 + 4 = 9)"},
                    {"num": 3, "part": "A", "prompt": "Write the word sentence as an equation and solve: 'The sum of a number x and 14 is 52.'", "keys": "x + 14 = 52", "yx": "52 - 14 = 38", "ans": "x + 14 = 52; x = 38"},
                    {"num": 4, "part": "A", "prompt": "Write the word sentence as an equation and solve: '6 times a number k equals 84.'", "keys": "6k = 84", "yx": "84 ÷ 6 = 14", "ans": "6k = 84; k = 14"},
                    {"num": 5, "part": "B", "prompt": "Write the word sentence as an equation and solve: '9 less than a number w is 17.'", "keys": "w - 9 = 17", "yx": "17 + 9 = 26", "ans": "w - 9 = 17; w = 26"},
                    {"num": 6, "part": "B", "prompt": "Write the word sentence as an equation and solve: 'The quotient of a number m and 5 is 13.'", "keys": "m / 5 = 13", "yx": "13 × 5 = 65", "ans": "m / 5 = 13; m = 65"},
                    {"num": 7, "part": "B", "prompt": "Four identical pizzas (costing p dollars each) plus a $6 delivery fee total $54. Write an equation to represent the order, and test whether p = 12 is the solution.", "keys": "54 [ENTER] 4 [ENTER] 12 [×] 6 [+] [≠]", "yx": "Y:54 | X:54 (NO)", "ans": "4p + 6 = 54; p = $12"},
                    {"num": 8, "part": "B", "prompt": "Error Analysis: For the sentence '12 less than x is 20', Sam wrote 12 - x = 20. Explain his error, write the correct equation, and find x.", "keys": "x - 12 = 20", "yx": "20 + 12 = 32", "ans": "x - 12 = 20; x = 32"},
                    {"num": 9, "part": "C", "prompt": "Movie Streaming Pass: A streaming service charges a $10 monthly membership plus $3 per movie rental. This month your bill is $28. Write an equation and find how many movies m you rented.", "keys": "28 [ENTER] 10 [-] 3 [÷]", "yx": "Y:18 | X:3", "ans": "10 + 3m = 28; m = 6 movies"},
                    {"num": 10, "part": "C", "prompt": "Restaurant Bill Split: Three friends split a restaurant bill b equally, and each friend pays $14.50. Write an equation and find the total bill b.", "keys": "14.50 [ENTER] 3 [×]", "yx": "b/3 = 14.50", "ans": "b / 3 = 14.50; b = $43.50"}
                ]
            },
            {
                "day_num": 30,
                "sec_num": "7.2",
                "title": "Solving Equations Using Addition or Subtraction",
                "big_ideas_ref": "Big Ideas Grade 6, Section 7.2 (Solving Equations Using Addition or Subtraction)",
                "ccss": "CCSS.MATH.6.EE.B.7",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "balance_scale",
                "diagram_data": {"left": "x + 14", "right": "39", "sol": "Subtract 14 -> x = 25", "caption": "Subtraction Property of Equality: Remove 14 from both sides of x + 14 = 39 to isolate x = 25."},
                "concept": "Addition and subtraction are inverse operations—they undo each other. To solve an addition equation like x + 14 = 39, use the Subtraction Property of Equality to subtract 14 from BOTH sides so x is isolated on one pan of the balance scale. To solve a subtraction equation like x - 18 = 45, use the Addition Property of Equality to add 18 to both sides.",
                "examples": [
                    {
                        "title": "Example 1: Solving an Addition Equation (x + 28 = 73)",
                        "problem": "Solve x + 28 = 73 and check your solution.",
                        "block_step": "Subtract 28 from both sides: x = 73 - 28 = 45. Check by substituting 45 back into the original equation: 45 + 28 = 73.",
                        "keys": ["73", "ENTER", "28", "-", "73", "x⇄y", "28", "+", "≠"],
                        "stack_y": "73 (Right)",
                        "stack_x": "45+28=73 -> NO",
                        "ans": "x = 45",
                        "note": "Subtract 28 to get x = 45, then test 45 + 28 against 73 with [≠] (flashes NO!)."
                    },
                    {
                        "title": "Example 2: Solving Equations with Decimals & Fractions",
                        "problem": "Solve w - 19.6 = 34.8 and m + 3/8 = 5/6.",
                        "block_step": "For w - 19.6 = 34.8, add 19.6 to both sides: w = 34.8 + 19.6 = 54.4. For m + 3/8 = 5/6, subtract 3/8 from both sides: m = 20/24 - 9/24 = 11/24.",
                        "keys": ["34.8", "ENTER", "19.6", "+", ".", "5", ".", "6", "ENTER", ".", "3", ".", "8", "-"],
                        "stack_y": "w = 54.4",
                        "stack_x": "m = 11/24",
                        "ans": "w = 54.4; m = 11/24",
                        "note": "Check: 11/24 + 9/24 = 20/24 = 5/6."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Solve x + 28 = 73 and check your solution.", "keys": "73 [ENTER] 28 [-]", "yx": "Y:73 | X:28", "ans": "x = 45"},
                    {"num": 2, "part": "A", "prompt": "Solve y - 34 = 58 and check your solution.", "keys": "58 [ENTER] 34 [+]", "yx": "Y:58 | X:34", "ans": "y = 92"},
                    {"num": 3, "part": "A", "prompt": "Solve 19 + n = 64.", "keys": "64 [ENTER] 19 [-]", "yx": "Y:64 | X:19", "ans": "n = 45"},
                    {"num": 4, "part": "A", "prompt": "Solve k - 47 = 29.", "keys": "29 [ENTER] 47 [+]", "yx": "Y:29 | X:47", "ans": "k = 76"},
                    {"num": 5, "part": "B", "prompt": "Solve w - 19.6 = 34.8.", "keys": "34.8 [ENTER] 19.6 [+]", "yx": "Y:34.8 | X:19.6", "ans": "w = 54.4"},
                    {"num": 6, "part": "B", "prompt": "Solve p + 8.75 = 25.4.", "keys": "25.4 [ENTER] 8.75 [-]", "yx": "Y:25.4 | X:8.75", "ans": "p = 16.65"},
                    {"num": 7, "part": "B", "prompt": "Solve m + 3/8 = 5/6.", "keys": "[.] 5 [.] 6 [ENTER] [.] 3 [.] 8 [-]", "yx": "Y:5/6 | X:3/8", "ans": "m = 11/24"},
                    {"num": 8, "part": "B", "prompt": "Solve a - 1 1/4 = 3 1/2.", "keys": "3 [.] 1 [.] 2 [ENTER] 1 [.] 1 [.] 4 [+]", "yx": "Y:3 1/2 | X:1 1/4", "ans": "a = 4 3/4"},
                    {"num": 9, "part": "C", "prompt": "Game Controller Purchase: After spending $18.50 on a custom controller skin, you have $26.75 left in your wallet. Write and solve an equation to find how much money m you had before the purchase.", "keys": "26.75 [ENTER] 18.50 [+]", "yx": "Y:26.75 | X:18.50", "ans": "m - 18.50 = 26.75; m = $45.25"},
                    {"num": 10, "part": "C", "prompt": "Drone Altitude Climb: A quadcopter climbs 42.5 feet to reach a hovering altitude of 110 feet. Write and solve an equation to find its starting altitude h.", "keys": "110 [ENTER] 42.5 [-]", "yx": "Y:110 | X:42.5", "ans": "h + 42.5 = 110; h = 67.5 ft"}
                ]
            },
            {
                "day_num": 31,
                "sec_num": "7.3",
                "title": "Solving Equations Using Multiplication or Division",
                "big_ideas_ref": "Big Ideas Grade 6, Section 7.3 (Solving Equations Using Multiplication or Division)",
                "ccss": "CCSS.MATH.6.EE.B.7",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_common_denominator.png",
                "diagram_type": "balance_scale",
                "diagram_data": {"left": "6x (6 boxes)", "right": "84 units", "sol": "84 ÷ 6 -> x = 14", "caption": "Division Property of Equality: 6 identical x-boxes balance 84 units, so 1 x-box balances 84 ÷ 6 = 14 units."},
                "concept": "Multiplication and division are inverse operations. To solve a multiplication equation like 6x = 84, use the Division Property of Equality to divide both sides by 6. To solve a division equation like k ÷ 7 = 14.5, use the Multiplication Property of Equality to multiply both sides by 7. When the coefficient is a fraction (such as 2/5 n = 16), multiply both sides by the reciprocal (5/2).",
                "examples": [
                    {
                        "title": "Example 1: Solving Multiplication & Division Equations",
                        "problem": "Solve 8x = 136 and k ÷ 7 = 14.5, and check each solution.",
                        "block_step": "For 8x = 136, divide both sides by 8: x = 136 ÷ 8 = 17. For k ÷ 7 = 14.5, multiply both sides by 7: k = 14.5 × 7 = 101.5.",
                        "keys": ["136", "ENTER", "8", "÷", "136", "x⇄y", "8", "×", "≠"],
                        "stack_y": "x = 17",
                        "stack_x": "8(17)=136 -> NO",
                        "ans": "x = 17; k = 101.5",
                        "note": "Check with [≠] (flashes NO!): 8(17) = 136 and 101.5 ÷ 7 = 14.5."
                    },
                    {
                        "title": "Example 2: Solving Equations with Fraction Coefficients (2/5 n = 16)",
                        "problem": "Solve 2/5 n = 16 using reciprocal multiplication.",
                        "block_step": "Multiply both sides by the reciprocal 5/2: n = 16 × (5/2) = 80 ÷ 2 = 40.",
                        "keys": ["16", "ENTER", ".", "2", ".", "5", "f", "1/x", "×"],
                        "stack_y": "16",
                        "stack_x": "5/2 -> 40",
                        "ans": "n = 40",
                        "note": "Check: 2/5 of 40 is (2 × 40) ÷ 5 = 16."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Solve 8x = 136 and check your solution.", "keys": "136 [ENTER] 8 [÷]", "yx": "Y:136 | X:8", "ans": "x = 17"},
                    {"num": 2, "part": "A", "prompt": "Solve 12y = 180 and check your solution.", "keys": "180 [ENTER] 12 [÷]", "yx": "Y:180 | X:12", "ans": "y = 15"},
                    {"num": 3, "part": "A", "prompt": "Solve m ÷ 6 = 19 and check your solution.", "keys": "19 [ENTER] 6 [×]", "yx": "Y:19 | X:6", "ans": "m = 114"},
                    {"num": 4, "part": "A", "prompt": "Solve k ÷ 7 = 14.5.", "keys": "14.5 [ENTER] 7 [×]", "yx": "Y:14.5 | X:7", "ans": "k = 101.5"},
                    {"num": 5, "part": "B", "prompt": "Solve 4.5w = 63.", "keys": "63 [ENTER] 4.5 [÷]", "yx": "Y:63 | X:4.5", "ans": "w = 14"},
                    {"num": 6, "part": "B", "prompt": "Solve 3/4 x = 18.", "keys": "18 [ENTER] [.] 3 [.] 4 [÷]", "yx": "Y:18 | X:3/4", "ans": "x = 24"},
                    {"num": 7, "part": "B", "prompt": "Solve 2/5 n = 16.", "keys": "16 [ENTER] [.] 2 [.] 5 [÷]", "yx": "Y:16 | X:2/5", "ans": "n = 40"},
                    {"num": 8, "part": "B", "prompt": "Solve 5/6 p = 2/3.", "keys": "[.] 2 [.] 3 [ENTER] [.] 5 [.] 6 [÷]", "yx": "Y:2/3 | X:5/6", "ans": "p = 4/5 (0.8)"},
                    {"num": 9, "part": "C", "prompt": "3D Tower Print Time: A 3D printer builds a vertical tower at a steady rate of 1.5 cm per minute. Write and solve an equation to find how many minutes t it takes to print a 27 cm tower.", "keys": "27 [ENTER] 1.5 [÷]", "yx": "Y:27 | X:1.5", "ans": "1.5t = 27; t = 18 minutes"},
                    {"num": 10, "part": "C", "prompt": "Robotics Club Roster: Exactly 3/5 of the students in the STEM club are 6th graders. If there are 27 sixth graders in the club, write and solve an equation to find the total number of students s in the club.", "keys": "27 [ENTER] [.] 3 [.] 5 [÷]", "yx": "Y:27 | X:3/5", "ans": "3/5 s = 27; s = 45 students"}
                ]
            },
            {
                "day_num": 32,
                "sec_num": "7.4",
                "title": "Writing, Graphing & Solving One-Step Inequalities",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 7.5–7.7 (Writing, Graphing, and Solving Inequalities)",
                "ccss": "CCSS.MATH.6.EE.B.8",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "zero_pairs",
                "diagram_data": {"pos": 7, "neg": 0, "net": 7, "caption": "Graphing Inequalities: '>' or '<' uses an Open Circle (o); '≥' or '≤' uses a Solid Dot (•)."},
                "concept": "An inequality compares two expressions using <, >, ≤ (at most / no more than), or ≥ (at least / no less than) and has infinitely many solutions. On a number line graph, use an OPEN circle (o) for < or > (boundary not included) and a SOLID dot (•) for ≤ or ≥ (boundary included), then shade the arrow in the direction of the true solutions.",
                "examples": [
                    {
                        "title": "Example 1: Solving & Graphing x - 7 ≥ 12",
                        "problem": "Solve x - 7 ≥ 12 and describe its graph on a number line.",
                        "block_step": "Add 7 to both sides: x ≥ 19. Because the symbol is '≥', place a solid dot (•) at 19 and shade the arrow to the right.",
                        "keys": ["12", "ENTER", "7", "+", "20", "f", "≥"],
                        "stack_y": "19 (Boundary)",
                        "stack_x": "20 (Test) -> YES",
                        "ans": "x ≥ 19 (Solid dot at 19, arrow right)",
                        "note": "Testing x = 20 against 19 with [f][≥] flashes YES (20 ≥ 19 is true)!"
                    },
                    {
                        "title": "Example 2: Real-World Weight Limit Inequality",
                        "problem": "A cargo drone can carry at most 60 pounds. It already carries a 15-pound camera rig plus supply boxes weighing 3 pounds each (3b + 15 ≤ 60). What is the maximum number of boxes b it can carry?",
                        "block_step": "Subtract the 15-pound rig (60 - 15 = 45), then divide by 3 pounds per box (45 ÷ 3 = 15) -> b ≤ 15 boxes.",
                        "keys": ["60", "ENTER", "15", "-", "3", "÷"],
                        "stack_y": "45 (Left)",
                        "stack_x": "3 -> 15",
                        "ans": "b ≤ 15 (At most 15 boxes)",
                        "note": "Check b = 15 with [g][≤]: 60 [ENTER] 3 [ENTER] 15 [×] 15 [+] [g][≤] flashes YES!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Solve x + 8 > 21. Then state whether the boundary point uses an open circle or solid dot, and which way the arrow points.", "keys": "21 [ENTER] 8 [-]", "yx": "Y:21 | X:8", "ans": "x > 13 (Open circle at 13, arrow right)"},
                    {"num": 2, "part": "A", "prompt": "Solve y - 9 ≤ 15. Then state whether the boundary point uses an open circle or solid dot, and which way the arrow points.", "keys": "15 [ENTER] 9 [+]", "yx": "Y:15 | X:9", "ans": "y ≤ 24 (Solid dot at 24, arrow left)"},
                    {"num": 3, "part": "A", "prompt": "Solve 6n ≥ 78. Then state whether the boundary point uses an open circle or solid dot, and which way the arrow points.", "keys": "78 [ENTER] 6 [÷]", "yx": "Y:78 | X:6", "ans": "n ≥ 13 (Solid dot at 13, arrow right)"},
                    {"num": 4, "part": "A", "prompt": "Solve m ÷ 4 < 9. Then state whether the boundary point uses an open circle or solid dot, and which way the arrow points.", "keys": "9 [ENTER] 4 [×]", "yx": "Y:9 | X:4", "ans": "m < 36 (Open circle at 36, arrow left)"},
                    {"num": 5, "part": "B", "prompt": "Write an inequality for the statement: 'You must be at least 48 inches tall (h) to ride the roller coaster.'", "keys": "'At least' = ≥", "yx": "Solid dot at 48", "ans": "h ≥ 48"},
                    {"num": 6, "part": "B", "prompt": "Write an inequality for the statement: 'A freight elevator holds at most 2,000 pounds (w).'", "keys": "'At most' = ≤", "yx": "Solid dot at 2000", "ans": "w ≤ 2,000"},
                    {"num": 7, "part": "B", "prompt": "Which values from the set {4, 5, 6} are solutions of the inequality 4n + 3 > 23?", "keys": "23 [ENTER] 4 [ENTER] 6 [×] 3 [+] [f][>]", "yx": "27 > 23 (YES)", "ans": "Only 6 (At n = 5, 23 > 23 is false)"},
                    {"num": 8, "part": "B", "prompt": "Which values from the set {4, 5, 6} are solutions of the inequality 4x - 3 ≥ 17?", "keys": "17 [ENTER] 4 [ENTER] 5 [×] 3 [-] [f][≥]", "yx": "17 ≥ 17 (YES)", "ans": "5 and 6"},
                    {"num": 9, "part": "C", "prompt": "Book Fair Budget: You have $50 to spend on paperback books that cost $8 each. Write and solve an inequality to find the maximum number of whole books b you can buy, and state how much money is left over.", "keys": "50 [ENTER] 8 [g][÷R]", "yx": "Y:2 | X:6", "ans": "8b ≤ 50; at most 6 books ($2 left over)"},
                    {"num": 10, "part": "C", "prompt": "Next-Level Score Target: A player needs at least 500 total points to advance to the next level and currently has 340 points. Write and solve an inequality to find how many more points p the player needs.", "keys": "500 [ENTER] 340 [-]", "yx": "Y:500 | X:340", "ans": "p + 340 ≥ 500; p ≥ 160 points"}
                ]
            },
            {
                "day_num": 33,
                "sec_num": "7.5",
                "title": "Writing Equations in Two Variables — Independent & Dependent Variables",
                "big_ideas_ref": "Big Ideas Grade 6, Section 7.4 (Writing Equations in Two Variables)",
                "ccss": "CCSS.MATH.6.EE.C.9",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "coord_plane",
                "diagram_data": {"pts": [("(1,6)", 1, 6), ("(2,12)", 2, 12), ("(3,18)", 3, 18)], "caption": "Multiplicative Rule y = 6x passes through (0, 0); Additive Rule y = x + 6 starts at (0, 6)."},
                "concept": "In a two-variable equation such as y = 6x or y = x + 6, the input variable x is the independent variable (you choose its value freely) and the output variable y is the dependent variable (its value depends on x). In a table of values, if y - x is constant, the rule is additive (y = x + b); if y ÷ x is constant, the rule is multiplicative (y = kx).",
                "examples": [
                    {
                        "title": "Example 1: Identifying Multiplicative (y = kx) vs. Additive (y = x + b) Rules",
                        "problem": "Table A contains (2, 14), (5, 35), (8, 56). Table B contains (10, 6), (15, 11), (22, 18). Write the equation for each table.",
                        "block_step": "Table A: 14÷2 = 7, 35÷5 = 7, 56÷8 = 7 -> y = 7x. Table B: 10 - 4 = 6, 15 - 4 = 11, 22 - 4 = 18 -> y = x - 4.",
                        "keys": ["14", "ENTER", "2", "÷", "35", "ENTER", "5", "÷", "≠"],
                        "stack_y": "7 (14÷2)",
                        "stack_x": "7 (35÷5) -> NO",
                        "ans": "Table A: y = 7x; Table B: y = x - 4",
                        "note": "Check the ratio y ÷ x and the difference y - x across all columns of the table."
                    },
                    {
                        "title": "Example 2: Independent vs. Dependent Variables in Real Life",
                        "problem": "You earn $12.50 per hour (h) mowing lawns, for a total pay of p = 12.50h. Identify the independent and dependent variables and find p for 6.5 hours.",
                        "block_step": "Hours worked h is the independent variable; total pay p is the dependent variable. For h = 6.5: p = 12.50 × 6.5 = $81.25.",
                        "keys": ["12.50", "ENTER", "6.5", "×"],
                        "stack_y": "12.50 (Rate)",
                        "stack_x": "6.5 (Hours)",
                        "ans": "Independent: h, Dependent: p; p = $81.25",
                        "note": "Total pay p depends on the number of hours h worked."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "A table contains the ordered pairs (1, 8), (2, 16), and (3, 24). Write the equation relating x and y, and find y when x = 10.", "keys": "16 [ENTER] 2 [÷] -> 8; 8×10", "yx": "y = 8x", "ans": "y = 8x; y = 80"},
                    {"num": 2, "part": "A", "prompt": "A table contains the ordered pairs (1, 9), (2, 10), and (5, 13). Write the equation relating x and y, and find y when x = 20.", "keys": "9 [ENTER] 1 [-] -> +8; 20+8", "yx": "y = x + 8", "ans": "y = x + 8; y = 28"},
                    {"num": 3, "part": "A", "prompt": "A table contains the ordered pairs (2, 14), (5, 35), and (8, 56). Write the equation relating x and y, and find y when x = 12.", "keys": "14 [ENTER] 2 [÷] -> 7; 7×12", "yx": "y = 7x", "ans": "y = 7x; y = 84"},
                    {"num": 4, "part": "A", "prompt": "A table contains the ordered pairs (10, 6), (15, 11), and (22, 18). Write the equation relating x and y, and find y when x = 30.", "keys": "30 [ENTER] 4 [-]", "yx": "y = x - 4", "ans": "y = x - 4; y = 26"},
                    {"num": 5, "part": "B", "prompt": "Complete a table of ordered pairs (x, y) for the equation y = 6x using x = 1, 2, 3, and 4.", "keys": "6 [g][REP] [+] [+] [+]", "yx": "6, 12, 18, 24", "ans": "(1, 6), (2, 12), (3, 18), (4, 24)"},
                    {"num": 6, "part": "B", "prompt": "In the formula d = 65t (representing the distance d in miles a train travels in t hours), which variable is independent and which variable is dependent?", "keys": "d depends on t", "yx": "Input t -> Output d", "ans": "Independent: t; Dependent: d"},
                    {"num": 7, "part": "B", "prompt": "Using the train formula d = 65t, how far does the train travel in 4.5 hours?", "keys": "65 [ENTER] 4.5 [×]", "yx": "Y:65 | X:4.5", "ans": "292.5 miles"},
                    {"num": 8, "part": "B", "prompt": "Does the graph of the multiplicative equation y = 4x pass through the origin (0, 0)? Where does the additive equation y = x + 4 cross the y-axis?", "keys": "Test x = 0 in both", "yx": "4(0)=0 vs 0+4=4", "ans": "y = 4x passes through (0, 0); y = x + 4 crosses at (0, 4)"},
                    {"num": 9, "part": "C", "prompt": "Summer Lawn Care: You earn $12.50 per hour according to p = 12.50h. How many hours h must you work to earn $100?", "keys": "100 [ENTER] 12.50 [÷]", "yx": "Y:100 | X:12.50", "ans": "8 hours"},
                    {"num": 10, "part": "C", "prompt": "Climbing Gym Membership: A climbing gym charges a one-time $25 registration fee plus $15 per month m. Write a two-variable equation for the total cost c, and find the total cost for 12 months.", "keys": "15 [ENTER] 12 [×] 25 [+]", "yx": "Y:180 | X:25", "ans": "c = 15m + 25; $205"}
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
        "kit_summary": "Place Value Studio (PLACE-01) + Fraction Studio (FRAC-01)",
        "hero_png": "place_value_regrouping.png",
        "coach_misconception": "Students drop one of the 6 faces when finding rectangular prism surface area, tangle prism and pyramid formulas, and confuse 2D Surface Area (cardboard outside) with 3D Volume (cubes inside).",
        "coach_remediation": "Have students count the 3 pairs of opposite faces on a rectangular prism while logging each pair into [Σ+] (n=1, 2, 3), pack unit blocks or use [f] [PRISM] ([f][9]) to multiply 3 stack floors (l, w, h) at once for volume, and verify [f] [CIRC], [g] [CONE], and [g] [HYP].",
        "sections": [
            {
                "day_num": 34,
                "sec_num": "8.1",
                "title": "Three-Dimensional Figures, Nets & Surface Area of Rectangular Prisms",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 8.1 & 8.2 (Three-Dimensional Figures and Surface Area of Prisms)",
                "ccss": "CCSS.MATH.6.G.A.4",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_ortho_steps.png",
                "diagram_type": "solid_3d",
                "diagram_data": {"mode": "net", "l": 8, "w": 5, "h": 3, "caption": "Unfolded 6-Face Rectangular Prism Net: Top/Bottom (2×8×5 = 80) + Front/Back (2×8×3 = 48) + Left/Right (2×5×3 = 30) = 158."},
                "concept": "The surface area of a polyhedron is the sum of the areas of all its flat faces, which can be visualized by unfolding the solid into a two-dimensional net. A rectangular prism of length l, width w, and height h has 6 rectangular faces arranged in 3 congruent opposite pairs: SA = 2lw + 2lh + 2wh.",
                "examples": [
                    {
                        "title": "Example 1: Surface Area of a Rectangular Prism Using Face Pairs",
                        "problem": "Find the surface area of a rectangular prism measuring 8 cm long, 5 cm wide, and 3 cm high.",
                        "block_step": "Top & bottom: 2(8 × 5) = 80 cm². Front & back: 2(8 × 3) = 48 cm². Left & right: 2(5 × 3) = 30 cm². Total SA = 80 + 48 + 30 = 158 cm².",
                        "keys": ["g", "CLΣ", "8", "ENTER", "5", "f", "RECT", "2", "×", "Σ+", "8", "ENTER", "3", "f", "RECT", "2", "×", "Σ+", "5", "ENTER", "3", "f", "RECT", "2", "×", "Σ+", "f", "Σx"],
                        "stack_y": "80 + 48 + 30",
                        "stack_x": "158 cm²",
                        "ans": "158 cm²",
                        "note": "Always check that all 3 pairs of opposite faces (6 faces total) are included."
                    },
                    {
                        "title": "Example 2: Surface Area of a Cube & an Open-Top Bin",
                        "problem": "Find the surface area of a cube with edge length s = 7 in., and the outer surface area of an open-top bin measuring 10 cm by 8 cm by 5 cm.",
                        "block_step": "A cube has 6 congruent square faces: SA = 6(7²) = 6 × 49 = 294 in.². An open-top bin has only 1 bottom (10×8 = 80) plus 4 vertical walls (2×10×5 + 2×8×5 = 180) = 260 cm².",
                        "keys": ["7", "x²", "6", "×"],
                        "stack_y": "49 (1 face)",
                        "stack_x": "6 -> 294 in²",
                        "ans": "Cube = 294 in.²; Open-Top Bin = 260 cm²",
                        "note": "An open-top bin has 5 faces (no top lid)."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the surface area of a cube with edge length s = 4 cm.", "keys": "4 [x²] 6 [×]", "yx": "Y:16 | X:6", "ans": "96 cm²"},
                    {"num": 2, "part": "A", "prompt": "Find the surface area of a cube with edge length s = 9 in.", "keys": "9 [x²] 6 [×]", "yx": "Y:81 | X:6", "ans": "486 in.²"},
                    {"num": 3, "part": "A", "prompt": "Find the surface area of a rectangular prism measuring 6 cm long, 4 cm wide, and 3 cm high.", "keys": "2(24)+2(18)+2(12)", "yx": "48 + 36 + 24", "ans": "108 cm²"},
                    {"num": 4, "part": "A", "prompt": "Find the surface area of a rectangular box measuring 10 in. long, 5 in. wide, and 2 in. high.", "keys": "2(50)+2(20)+2(10)", "yx": "100 + 40 + 20", "ans": "160 in.²"},
                    {"num": 5, "part": "B", "prompt": "Find the surface area of a rectangular prism with length l = 12 ft, width w = 8 ft, and height h = 5 ft.", "keys": "2(96)+2(60)+2(40)", "yx": "192 + 120 + 80", "ans": "392 ft²"},
                    {"num": 6, "part": "B", "prompt": "Find the surface area of a rectangular prism measuring 5 m long, 4 m wide, and 2.5 m high.", "keys": "2(20)+2(12.5)+2(10)", "yx": "40 + 25 + 20", "ans": "85 m²"},
                    {"num": 7, "part": "B", "prompt": "A cube has a total surface area of 150 cm². What is the area of one square face, and what is the edge length s of the cube?", "keys": "150 [ENTER] 6 [÷] [f][√x]", "yx": "25 -> s = 5", "ans": "One face = 25 cm²; s = 5 cm"},
                    {"num": 8, "part": "B", "prompt": "Error Analysis: For a 5 cm by 4 cm by 3 cm box, Leo added 20 + 15 + 12 = 47 cm². What did he forget to do, and what is the correct surface area?", "keys": "47 [ENTER] 2 [×]", "yx": "Y:47 | X:2", "ans": "94 cm² (He only summed 3 faces instead of doubling for all 6 faces)"},
                    {"num": 9, "part": "C", "prompt": "Open-Top Cold-Storage Battery Cargo Pod: An open-top rectangular battery cargo pod (5 faces, no top lid) is 30 cm long, 20 cm wide, and 15 cm tall. How many square centimeters of insulation paneling are needed to line the bottom and four sides?", "keys": "600 + 2(450) + 2(300)", "yx": "600 + 900 + 600", "ans": "2,100 cm²"},
                    {"num": 10, "part": "C", "prompt": "Gift Box Wrapping Paper: You are wrapping a gift box that is 15 inches long, 10 inches wide, and 4 inches tall. If you have a sheet of wrapping paper with an area of 550 in.², do you have enough paper to cover the box?", "keys": "2(150)+2(60)+2(40)", "yx": "300 + 120 + 80", "ans": "500 in.² needed; Yes, with 50 in.² to spare"}
                ]
            },
            {
                "day_num": 35,
                "sec_num": "8.2",
                "title": "Surface Area of Triangular Prisms & Pyramids",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 8.2 & 8.3 (Surface Area of Triangular Prisms and Pyramids)",
                "ccss": "CCSS.MATH.6.G.A.4",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "polygon_area",
                "diagram_data": {"shape": "composite", "rect_b": 10, "rect_h": 10, "tri_b": 10, "tri_h": 12, "caption": "Square Pyramid Net: 1 Square Base (10² = 100) + 4 Congruent Lateral Triangles (4 × ½×10×12 = 240) = 340."},
                "concept": "To find the surface area of a triangular prism, unfold its net into 2 congruent triangular bases and 3 rectangular lateral faces, and sum their areas. To find the surface area of a pyramid, add the area of its single polygon base to the areas of its triangular lateral faces (using the slant height of each triangle).",
                "examples": [
                    {
                        "title": "Example 1: Surface Area of a Square Pyramid",
                        "problem": "Find the surface area of a square pyramid with a 10 m by 10 m square base and 4 congruent triangular faces each having base 10 m and slant height 12 m.",
                        "block_step": "Square base area = 10 × 10 = 100 m². Each triangular face has area ½ × 10 × 12 = 60 m², so 4 triangles = 4 × 60 = 240 m². Total SA = 100 + 240 = 340 m².",
                        "keys": ["g", "CLΣ", "10", "x²", "Σ+", "10", "ENTER", "12", "g", "TRI", "4", "×", "Σ+", "f", "Σx"],
                        "stack_y": "100 (Base)",
                        "stack_x": "240 (4 Tris) -> 340",
                        "ans": "340 m²",
                        "note": "1 Square Base (100) + 4 Congruent Lateral Triangles (240) = 340 m²."
                    },
                    {
                        "title": "Example 2: Surface Area of a Triangular Prism",
                        "problem": "A ramp is a triangular prism with 2 right-triangle bases (b = 6 ft, h = 8 ft) and 3 rectangular faces of length 10 ft (with widths 6 ft, 8 ft, and 10 ft). Find its surface area.",
                        "block_step": "Two triangle bases: 2 × (½ × 6 × 8) = 48 ft². Three rectangular faces: (6×10) + (8×10) + (10×10) = 240 ft². Total SA = 48 + 240 = 288 ft².",
                        "keys": ["6", "ENTER", "8", "g", "TRI", "2", "×", "6", "ENTER", "8", "+", "10", "+", "10", "f", "RECT", "+"],
                        "stack_y": "48 (2 Ends)",
                        "stack_x": "240 (3 Sides) -> 288",
                        "ans": "288 ft²",
                        "note": "Notice that the 3 rectangles together form a large rectangle of width (6+8+10) = 24 ft and length 10 ft."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the surface area of a square pyramid with a 6 cm by 6 cm base and 4 triangular faces each having base 6 cm and slant height 5 cm.", "keys": "6 [x²] 6 [ENTER] 5 [g][TRI] 4 [×] [+]", "yx": "Y:36 | X:60", "ans": "96 cm²"},
                    {"num": 2, "part": "A", "prompt": "Find the surface area of a square pyramid with an 8 in. by 8 in. base and 4 triangular faces each having base 8 in. and slant height 10 in.", "keys": "8 [x²] 8 [ENTER] 10 [g][TRI] 4 [×] [+]", "yx": "Y:64 | X:160", "ans": "224 in.²"},
                    {"num": 3, "part": "A", "prompt": "Find the surface area of a square pyramid with a 12 ft by 12 ft base and 4 triangular faces each having base 12 ft and slant height 9 ft.", "keys": "12 [x²] 12 [ENTER] 9 [g][TRI] 4 [×] [+]", "yx": "Y:144 | X:216", "ans": "360 ft²"},
                    {"num": 4, "part": "A", "prompt": "A regular triangular pyramid (tetrahedron) is made of 4 congruent equilateral triangles, each with base 6 cm and slant height 5.2 cm. What is its total surface area?", "keys": "6 [ENTER] 5.2 [g][TRI] 4 [×]", "yx": "Y:15.6 | X:4", "ans": "62.4 cm²"},
                    {"num": 5, "part": "B", "prompt": "A triangular prism has 2 right-triangle bases (b = 4 cm, h = 3 cm) and 3 rectangular faces of length 10 cm (widths 3 cm, 4 cm, and 5 cm). What is its surface area?", "keys": "4 [ENTER] 3 [g][TRI] 2 [×] (12) + 12×10 (120)", "yx": "Y:12 | X:120", "ans": "132 cm²"},
                    {"num": 6, "part": "B", "prompt": "A triangular prism tent has 2 triangular ends (base 8 ft, height 3 ft) and 3 rectangular panels of length 7 ft (widths 5 ft, 5 ft, and 8 ft). What is its total surface area?", "keys": "8 [ENTER] 3 [g][TRI] 2 [×] (24) + 18×7 (126)", "yx": "Y:24 | X:126", "ans": "150 ft²"},
                    {"num": 7, "part": "B", "prompt": "A regular tetrahedron has 4 congruent triangular faces each with base 8 cm and slant height 6.93 cm. What is its surface area?", "keys": "8 [ENTER] 6.93 [g][TRI] 4 [×]", "yx": "Y:27.72 | X:4", "ans": "110.88 cm²"},
                    {"num": 8, "part": "B", "prompt": "Compare the nets of a triangular prism and a square pyramid: how many triangular faces and how many rectangular/square faces does each solid have?", "keys": "Count net faces", "yx": "Prism:5 | Pyr:5", "ans": "Triangular prism: 2 triangles + 3 rectangles; Square pyramid: 1 square + 4 triangles"},
                    {"num": 9, "part": "C", "prompt": "A-Frame Camping Tent: An A-frame tent is a triangular prism with 2 triangular doors (base 6 ft, height 4 ft), a 6 ft by 8 ft floor, and 2 sloped roof panels (5 ft by 8 ft each). How many square feet of nylon fabric are in the tent?", "keys": "24 + 48 + 80", "yx": "24 + 128", "ans": "152 ft²"},
                    {"num": 10, "part": "C", "prompt": "Glass Pyramid Skylight: A rooftop skylight is shaped like a square pyramid with an open bottom (no floor)—only 4 congruent triangular glass panes, each with base 9 ft and slant height 6 ft. What is the total area of the glass panes?", "keys": "9 [ENTER] 6 [g][TRI] 4 [×]", "yx": "Y:27 | X:4", "ans": "108 ft²"}
                ]
            },
            {
                "day_num": 36,
                "sec_num": "8.3",
                "title": "Volume of Rectangular Prisms with Whole & Fractional Edge Lengths",
                "big_ideas_ref": "Big Ideas Grade 6, Section 8.4 (Volume of Rectangular Prisms)",
                "ccss": "CCSS.MATH.6.G.A.2",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_twin_comparator.png",
                "diagram_type": "solid_3d",
                "diagram_data": {"mode": "prism", "l": 12, "w": 8, "h": 5, "caption": "Volume of a Rectangular Prism: V = l × w × h = 12 × 8 × 5 = 480 cubic inches."},
                "concept": "While Surface Area measures the 2D flat area covering the outside of a solid (in square units), Volume measures the 3D space inside the solid—the number of unit cubes needed to fill it completely (in cubic units). For any rectangular prism, Volume equals the base area B times the height h: V = Bh = l × w × h.",
                "examples": [
                    {
                        "title": "Example 1: Volume with Whole & Fractional Edge Lengths",
                        "problem": "Find the volume of a crate measuring 12 in. by 8 in. by 5 in., and an aquarium measuring 3 1/2 ft by 1 1/2 ft by 2 ft.",
                        "block_step": "Crate: V = 12 × 8 × 5 = 480 in.³. Aquarium: V = (7/2) × (3/2) × 2 = 21/2 = 10 1/2 ft³.",
                        "keys": ["12", "ENTER", "8", "ENTER", "5", "f", "PRISM"],
                        "stack_y": "Z:12 | Y:8",
                        "stack_x": "X:5 -> 480",
                        "ans": "Crate = 480 in.³; Aquarium = 10 1/2 ft³",
                        "note": "The formula V = l × w × h works for both whole numbers and fractional edge lengths."
                    },
                    {
                        "title": "Example 2: Finding a Missing Dimension from Volume (V = Bh)",
                        "problem": "A rectangular planter has a base area of B = 45 in.² (9 in. by 5 in.) and holds 360 in.³ of soil. How deep (h) is the soil?",
                        "block_step": "Substitute into V = Bh: 360 = 45h. Divide both sides by 45: h = 360 ÷ 45 = 8 in.",
                        "keys": ["360", "ENTER", "45", "÷"],
                        "stack_y": "360 (Vol)",
                        "stack_x": "45 (Base) -> 8",
                        "ans": "h = 8 in.",
                        "note": "Check: 9 × 5 × 8 = 360 in.³."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Deep-Freeze Survival Rations Container: A rectangular insulated rations container measures 18 cm long, 6 cm wide, and 28 cm tall. What is its interior volume in cubic centimeters?", "keys": "18 [ENTER] 6 [ENTER] 28 [f][PRISM]", "yx": "Z:18|Y:6|X:28", "ans": "3,024 cm³"},
                    {"num": 2, "part": "A", "prompt": "Find the volume of a cube with edge length s = 5 inches.", "keys": "5 [x³]", "yx": "5×5×5", "ans": "125 in.³"},
                    {"num": 3, "part": "A", "prompt": "Water Ballast Flume: A rectangular water testing flume is 25 meters long, 10 meters wide, and filled to a depth of 2 meters. How many cubic meters of water does it hold?", "keys": "25 [ENTER] 10 [ENTER] 2 [f][PRISM]", "yx": "Z:25|Y:10|X:2", "ans": "500 m³"},
                    {"num": 4, "part": "A", "prompt": "A rectangular prism has a base area of B = 32 m² and a height of h = 7 m. What is its volume?", "keys": "32 [ENTER] 7 [×]", "yx": "Y:32 | X:7", "ans": "224 m³"},
                    {"num": 5, "part": "B", "prompt": "Find the volume of a fish tank that is 3 1/2 feet long, 1 1/2 feet wide, and 2 feet tall.", "keys": "3.5 [ENTER] 1.5 [ENTER] 2 [f][PRISM]", "yx": "Z:3.5|Y:1.5|X:2", "ans": "10 1/2 ft³ (10.5)"},
                    {"num": 6, "part": "B", "prompt": "Find the volume of a wooden block measuring 4 1/2 inches long, 3 inches wide, and 2 inches high.", "keys": "4.5 [ENTER] 3 [ENTER] 2 [f][PRISM]", "yx": "Z:4.5|Y:3|X:2", "ans": "27 in.³"},
                    {"num": 7, "part": "B", "prompt": "A rectangular storage box has a volume of 270 in.³, a length of 9 in., and a width of 5 in. What is its height h?", "keys": "270 [ENTER] 9 [ENTER] 5 [×] [÷]", "yx": "Y:270 | X:45", "ans": "6 in."},
                    {"num": 8, "part": "B", "prompt": "How many 1/2-inch cubes are needed to completely fill a 1-inch cube (measuring 1 in. by 1 in. by 1 in.)?", "keys": "2 [x³]", "yx": "2 × 2 × 2", "ans": "8 half-inch cubes"},
                    {"num": 9, "part": "C", "prompt": "Garden Planter Depth: A raised cedar planter has a base measuring 9 inches by 5 inches and holds 360 cubic inches of potting soil. What is the depth h of the soil?", "keys": "360 [ENTER] 45 [÷]", "yx": "Y:360 | X:45", "ans": "8 inches"},
                    {"num": 10, "part": "C", "prompt": "Packing Half-Inch Cubes: A wooden box has a volume of 27 cubic inches. How many 1/2-inch unit cubes can be packed inside the box?", "keys": "27 [ENTER] 2 [x³] [×]", "yx": "Y:27 | X:8", "ans": "216 half-inch cubes"}
                ]
            },
            {
                "day_num": 37,
                "sec_num": "8.4",
                "title": "Circles, Cones & Right-Triangle Hypotenuse (Geometry Bridge)",
                "big_ideas_ref": "Big Ideas Grade 6/7 Geometry Bridge (Circles, Cones & Right Triangles)",
                "ccss": "CCSS.MATH.7.G.B.4",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_ortho_steps.png",
                "diagram_type": "polygon_area",
                "diagram_data": {"shape": "triangle", "b": 4, "h": 3, "area": 6, "caption": "3-4-5 Right Triangle (3² + 4² = 5² -> c = 5), Circle Area (A = πr²), and Cone Volume (V = ⅓πr²h)."},
                "concept": "In this Grade 7/8 Geometry Bridge: (1) The area of a circle with radius r is A = πr² (where r is half the diameter d). (2) In a right triangle with legs a and b and hypotenuse c, the Pythagorean Theorem states a² + b² = c², so c = √(a² + b²). (3) The volume of a cone is one-third the volume of a cylinder with the same base and height: V = ⅓πr²h.",
                "examples": [
                    {
                        "title": "Example 1: Circle Area (A = πr²) & Right-Triangle Hypotenuse",
                        "problem": "Find the area of a circular pizza with radius r = 6 in. (round to 2 decimal places), and find the diagonal length of a ramp with legs 12 ft and 5 ft.",
                        "block_step": "Circle area: A = π(6²) = 36π ≈ 113.10 in.². Ramp hypotenuse: c = √(12² + 5²) = √(144 + 25) = √169 = 13 ft.",
                        "keys": ["6", "f", "CIRC", "12", "ENTER", "5", "g", "HYP"],
                        "stack_y": "113.10 (Area)",
                        "stack_x": "13 (Hypot)",
                        "ans": "Pizza = 113.10 in.²; Ramp diagonal = 13 ft",
                        "note": "Square the radius first before multiplying by π."
                    },
                    {
                        "title": "Example 2: Volume of a Cone (V = ⅓πr²h)",
                        "problem": "A waffle cone has radius r = 3 cm and height h = 10 cm. Find its volume rounded to the nearest hundredth.",
                        "block_step": "Base circle area B = π(3²) ≈ 28.274 cm². Multiply by height 10 and divide by 3: V = (28.274 × 10) ÷ 3 ≈ 94.25 cm³.",
                        "keys": ["3", "ENTER", "10", "g", "CONE"],
                        "stack_y": "3 (Radius)",
                        "stack_x": "10 (Height) -> 94.25",
                        "ans": "94.25 cm³",
                        "note": "A cone holds exactly 1/3 the volume of a cylinder with the same radius and height."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the area of a circle with radius r = 5 cm (round to the nearest hundredth).", "keys": "5 [f][CIRC]", "yx": "π × 5²", "ans": "78.54 cm²"},
                    {"num": 2, "part": "A", "prompt": "Circular Sundial Clockface: A bronze garden sundial has a diameter of 30 cm (so its radius is r = 15 cm). What is the area of the circular sundial face, rounded to the nearest hundredth?", "keys": "15 [f][CIRC]", "yx": "π × 15²", "ans": "706.86 cm²"},
                    {"num": 3, "part": "A", "prompt": "Find the hypotenuse c of a right triangle with legs a = 3 cm and b = 4 cm.", "keys": "3 [ENTER] 4 [g][HYP]", "yx": "Y:3 | X:4", "ans": "5 cm"},
                    {"num": 4, "part": "A", "prompt": "Treehouse Zip-Line Shortcut: A backyard treehouse platform is 6 meters high, and the anchor post is 8 meters away across flat ground. How long is the straight diagonal zip-line cable connecting them?", "keys": "6 [ENTER] 8 [g][HYP]", "yx": "Y:6 | X:8", "ans": "10 meters"},
                    {"num": 5, "part": "B", "prompt": "A skateboard ramp has a horizontal base of 12 feet and a vertical back height of 5 feet. How long is the sloped riding surface?", "keys": "12 [ENTER] 5 [g][HYP]", "yx": "Y:12 | X:5", "ans": "13 ft"},
                    {"num": 6, "part": "B", "prompt": "A circular landing pad has a diameter of d = 16 meters. What is its radius r, and what is its area rounded to the nearest hundredth?", "keys": "16 [ENTER] 2 [÷] [f][CIRC]", "yx": "r = 8 m", "ans": "r = 8 m; Area = 201.06 m²"},
                    {"num": 7, "part": "B", "prompt": "Conical Sand Filtration Pile: A conical pile of water-filtration sand at the treatment plant has a base radius of r = 3 meters and a height of h = 2 meters. What is the volume of the sand pile, rounded to the nearest hundredth?", "keys": "3 [ENTER] 2 [g][CONE]", "yx": "Y:3 | X:2", "ans": "18.85 m³"},
                    {"num": 8, "part": "B", "prompt": "Find the volume of a cone with radius r = 6 inches and height h = 5 inches, rounded to the nearest hundredth.", "keys": "6 [ENTER] 5 [g][CONE]", "yx": "Y:6 | X:5", "ans": "188.50 in.³"},
                    {"num": 9, "part": "C", "prompt": "Cylinder vs. Cone Volume: A cylinder and a cone both have radius r = 3 cm and height h = 10 cm. Find the volume of the cylinder and the volume of the cone, rounded to the nearest hundredth.", "keys": "3 [ENTER] 10 [g][CONE]", "yx": "Y:3 | X:10", "ans": "Cylinder = 282.74 cm³; Cone = 94.25 cm³"},
                    {"num": 10, "part": "C", "prompt": "Widescreen Monitor Diagonal: Computer monitors are advertised by their diagonal screen length. If a monitor screen is 32 inches wide and 24 inches tall, what is its diagonal measurement?", "keys": "32 [ENTER] 24 [g][HYP]", "yx": "Y:32 | X:24", "ans": "40 inches"}
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
        "kit_summary": "Place Value Studio (PLACE-01) + Fraction Studio (FRAC-01)",
        "hero_png": "place_value_regrouping.png",
        "coach_misconception": "Students forget to sort data before finding Median/Quartiles, lose their place adding long lists for Mean, and dread Mean Absolute Deviation (MAD) because doing it by hand takes 20 minutes of subtraction.",
        "coach_remediation": "Show that Mean is physically leveling unequal Place Value digit stacks to the same height. Then show that entering a list ONCE with [Σ+] unlocks Mean ([g] [x̄]), Median ([f] [MED]), Mode ([g] [MODE]), Range ([RNG]), Quartiles ([f] [1Q], [g] [3Q], [IQR]), and MAD ([g] [MAD]) in 1 click each!",
        "sections": [
            {
                "day_num": 38,
                "sec_num": "9.1",
                "title": "Statistical Questions, Dot Plots & The Mean (Fair Share)",
                "big_ideas_ref": "Big Ideas Grade 6, Sections 9.1 & 9.2 (Statistical Questions, Dot Plots, and The Mean)",
                "ccss": "CCSS.MATH.6.SP.B.5c",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "stat_plot",
                "diagram_data": {"mode": "mean_towers", "towers": [3, 7, 5, 9, 6], "mean": 6, "caption": "Fair-Share Leveling: Towers of height 3, 7, 5, 9, 6 (total = 30 cubes) level out to 5 equal towers of height 6 (Mean x̄ = 6)."},
                "concept": "The mean (or average, x̄) of a numerical data set is the sum of the data values divided by the number of data values: x̄ = (Σx) ÷ n. Physically, the mean represents a 'fair share'—if you build cube towers for each data value and move cubes from taller towers to shorter towers until all towers have the exact same height, that common height is the mean!",
                "examples": [
                    {
                        "title": "Example 1: Finding the Mean of a Data Set",
                        "problem": "Find the sum, the number of values, and the mean of 18, 24, 15, 27, 21.",
                        "block_step": "Sum of the 5 values: 18 + 24 + 15 + 27 + 21 = 105. Divide by the count (n = 5): Mean = 105 ÷ 5 = 21.",
                        "keys": ["g", "CLΣ", "18", "Σ+", "24", "Σ+", "15", "Σ+", "27", "Σ+", "21", "Σ+", "g", "x̄"],
                        "stack_y": "Σx = 105 (n=5)",
                        "stack_x": "x̄ = 21",
                        "ans": "Sum = 105, Count = 5, Mean = 21",
                        "note": "Check by balancing deviations from 21: (-3) + (+3) + (-6) + (+6) + 0 = 0."
                    },
                    {
                        "title": "Example 2: Finding a Missing Score for a Target Mean",
                        "problem": "You want a mean score of 90 across 4 math quizzes. Your first 3 quiz scores are 86, 92, and 88. What score do you need on Quiz 4?",
                        "block_step": "Four quizzes with a mean of 90 require 4 × 90 = 360 total points. The first 3 quizzes total 86 + 92 + 88 = 266, so Quiz 4 must be 360 - 266 = 94.",
                        "keys": ["4", "ENTER", "90", "×", "86", "ENTER", "92", "+", "88", "+", "-"],
                        "stack_y": "360 (Target)",
                        "stack_x": "266 -> 94",
                        "ans": "94 on Quiz 4",
                        "note": "Deviation check: (-4) + (+2) + (-2) = -4 deficit, so Quiz 4 needs 90 + 4 = 94."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Find the sum and the mean of the data set: 2, 4, 6, 8.", "keys": "[g][CLΣ] 2 [Σ+] 4 [Σ+] 6 [Σ+] 8 [Σ+] [g][x̄]", "yx": "Σx:20 | n:4", "ans": "Sum = 20, Mean = 5"},
                    {"num": 2, "part": "A", "prompt": "Find the sum and the mean of the data set: 12, 15, 18, 11, 14.", "keys": "Load 5 nums into [Σ+] -> [g][x̄]", "yx": "Σx:70 | n:5", "ans": "Sum = 70, Mean = 14"},
                    {"num": 3, "part": "A", "prompt": "Seed-Bomber Catapult Mean: In three test launches, a seed-bomber catapult flings clay seed pods distances of 150 cm, 162 cm, and 156 cm. What is the mean launch distance?", "keys": "150 [Σ+] 162 [Σ+] 156 [Σ+] [g][x̄]", "yx": "Σx:468 | n:3", "ans": "156 cm"},
                    {"num": 4, "part": "A", "prompt": "Find the mean of these four mineral sample masses (in grams): 4.2, 3.8, 4.5, 3.5.", "keys": "Load into [Σ+] -> [g][x̄]", "yx": "Σx:16.0 | n:4", "ans": "Mean = 4.0 g"},
                    {"num": 5, "part": "B", "prompt": "Three measurements are 10, 20, and 25. Find the sum and the mean (rounded to the nearest hundredth).", "keys": "... 35 [f][Σ-] 25 [Σ+] [g][x̄]", "yx": "Σx:55 | n:3", "ans": "Sum = 55, Mean = 18.33"},
                    {"num": 6, "part": "B", "prompt": "In a dot plot of 6 quiz scores, the score 10 appears 4 times and the score 20 appears 2 times. What is the mean of all 6 scores (rounded to the nearest hundredth)?", "keys": "10 [ENTER] 4 [FRQ] 20 [ENTER] 2 [FRQ] [g][x̄]", "yx": "Σx:80 | n:6", "ans": "13.33 (80 ÷ 6)"},
                    {"num": 7, "part": "B", "prompt": "Find the mean daily high temperature (°F) for the 6-day period: 68, 72, 75, 71, 64, 70.", "keys": "Load 6 temps into [Σ+] -> [g][x̄]", "yx": "Σx:420 | n:6", "ans": "70°F"},
                    {"num": 8, "part": "B", "prompt": "If 5 stacks of blocks have a mean height of 12 blocks, how many total blocks are in all 5 stacks combined?", "keys": "5 [ENTER] 12 [×]", "yx": "Y:5 | X:12", "ans": "60 total blocks"},
                    {"num": 9, "part": "C", "prompt": "Target Test Average: You want a mean of 90 across 4 unit tests. Your first three scores are 85, 92, and 88. What score do you need on the fourth test?", "keys": "360 [ENTER] 265 [-]", "yx": "Y:360 | X:265", "ans": "95"},
                    {"num": 10, "part": "C", "prompt": "Joining the Roster: Six basketball players have a mean score of 15 points per game. A seventh player joins the team and scores 29 points. What is the new mean score for all 7 players?", "keys": "90 [ENTER] 29 [+] 7 [÷]", "yx": "Y:119 | X:7", "ans": "17 points"}
                ]
            },
            {
                "day_num": 39,
                "sec_num": "9.2",
                "title": "Measures of Center & Variation — Median, Mode, Range & Outliers",
                "big_ideas_ref": "Big Ideas Grade 6, Section 9.3 (Measures of Center: Median, Mode, and Range)",
                "ccss": "CCSS.MATH.6.SP.B.5c",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_ortho_steps.png",
                "diagram_type": "stat_plot",
                "diagram_data": {"mode": "mean_towers", "towers": [6, 7, 7, 7, 8, 9, 9, 10], "mean": 7.5, "caption": "Ordered Data (6, 7, 7, 7, 8, 9, 9, 10): Mode = 7 (most frequent), Median = 7.5 (middle average), Range = 10 - 6 = 4."},
                "concept": "When data values are ordered from least to greatest: the Median is the middle value (or the mean of the two middle values when the count n is even); the Mode is the value(s) that occur most often; and the Range is the difference between the greatest and least values (Max - Min). When an extreme outlier is present, the median is usually the best measure of center.",
                "examples": [
                    {
                        "title": "Example 1: Finding Mean, Median, Mode, and Range",
                        "problem": "Find the mean, median, mode, and range of the shoe sizes: 7, 9, 6, 7, 10, 8, 9, 7.",
                        "block_step": "Order from least to greatest: 6, 7, 7, 7, 8, 9, 9, 10. Mean = 63 ÷ 8 = 7.875. Median = (7 + 8) ÷ 2 = 7.5. Mode = 7. Range = 10 - 6 = 4.",
                        "keys": ["g", "CLΣ", "7", "Σ+", "9", "Σ+", "6", "Σ+", "7", "Σ+", "10", "Σ+", "8", "Σ+", "9", "Σ+", "7", "Σ+", "f", "MED", "g", "MODE", "RNG"],
                        "stack_y": "MED = 7.5",
                        "stack_x": "MODE = 7 | RNG = 4",
                        "ans": "Mean = 7.875, Median = 7.5, Mode = 7, Range = 4",
                        "note": "Always order data from least to greatest before finding the median by hand."
                    },
                    {
                        "title": "Example 2: Identifying an Outlier (Mean vs. Median)",
                        "problem": "Daily pet-sitting earnings are $15, $18, $15, $20, $17, and $90. Compare the mean and the median, and state which better represents a typical day.",
                        "block_step": "Ordered: 15, 15, 17, 18, 20, 90. The outlier $90 pulls the mean up to $29.17 (higher than 5 of the 6 days), while the median is $17.50.",
                        "keys": ["g", "x̄", "f", "MED"],
                        "stack_y": "x̄ = 29.17",
                        "stack_x": "MED = 17.50",
                        "ans": "Mean = $29.17, Median = $17.50 (Median better represents the data)",
                        "note": "When a data set has an extreme outlier, the median is the more reliable measure of center."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Shoe Size Survey Mode: A sneaker store records the shoe sizes of 8 customers: 6, 7, 7, 7, 8, 8, 9, 10. What is the mode of the shoe sizes?", "keys": "Load 8 nums -> [g][MODE]", "yx": "7 occurs 3 times", "ans": "Mode = 7"},
                    {"num": 2, "part": "A", "prompt": "Find the median, mode, and range of the data set: 12, 15, 12, 18, 20, 13.", "keys": "Load 6 nums -> [f][MED], [g][MODE], [RNG]", "yx": "Sorted: 12,12,13,15,18,20", "ans": "Median = 14, Mode = 12, Range = 8"},
                    {"num": 3, "part": "A", "prompt": "Find the mean, median, mode, and range of the data set: 5, 8, 8, 10, 14.", "keys": "Load 5 nums into [Σ+]", "yx": "Σx = 45 (n=5)", "ans": "Mean = 9, Median = 8, Mode = 8, Range = 9"},
                    {"num": 4, "part": "A", "prompt": "High Temperature Range: Over 7 days, the high temperatures (°F) were 62, 65, 78, 81, 74, 69, and 85. What are the minimum, maximum, and range of the temperatures?", "keys": "Load 7 nums -> [f][MIN], [g][MAX], [RNG]", "yx": "Min:62 | Max:85", "ans": "Min = 62°F, Max = 85°F, Range = 23°F"},
                    {"num": 5, "part": "B", "prompt": "Even-Dataset Median: Six daily high temperatures (°F) are ordered from least to greatest: 68, 72, 74, 76, 80, 84. What is the median temperature?", "keys": "Load 6 nums -> [f][MED]", "yx": "Avg of 74 & 76", "ans": "75°F"},
                    {"num": 6, "part": "B", "prompt": "Daily earnings are $15, $18, $15, $20, $17, and $90. Find the mean and median, and state which measure better represents a typical day.", "keys": "Load 6 nums -> [g][x̄], [f][MED]", "yx": "x̄:29.17 | MED:17.5", "ans": "Mean = $29.17, Median = $17.50 (Median is best)"},
                    {"num": 7, "part": "B", "prompt": "How do the mean and the median of {10, 12, 14, 16, 18} change if the value 18 is replaced by the outlier 100?", "keys": "Compare both sets", "yx": "Med stays 14", "ans": "Mean increases from 14 to 30.8; Median stays 14"},
                    {"num": 8, "part": "B", "prompt": "The minimum score on a science test is 64 and the range of the scores is 31. What was the maximum score on the test?", "keys": "64 [ENTER] 31 [+]", "yx": "Y:64 | X:31", "ans": "95"},
                    {"num": 9, "part": "C", "prompt": "Find the median and range of the data set {14, 8, 21, 11, 16}.", "keys": "Sorted: 8, 11, 14, 16, 21", "yx": "Med:14 | Rng:13", "ans": "Median = 14, Range = 13"},
                    {"num": 10, "part": "C", "prompt": "Neighborhood Home Prices: Five homes on a street sold for (in thousands of dollars): 210, 220, 215, 225, and 980. Find the mean and median sale prices, and explain which measure a home buyer should use.", "keys": "Load 5 nums -> [g][x̄], [f][MED]", "yx": "x̄:370 | MED:220", "ans": "Mean = $370k, Median = $220k (Use Median due to the $980k outlier)"}
                ]
            },
            {
                "day_num": 40,
                "sec_num": "9.3",
                "title": "Quartiles, Interquartile Range (IQR) & Box-and-Whisker Plots",
                "big_ideas_ref": "Big Ideas Grade 6, Section 9.4 & 10.4 (Measures of Variation and Box-and-Whisker Plots)",
                "ccss": "CCSS.MATH.6.SP.B.4",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_twin_comparator.png",
                "diagram_type": "stat_plot",
                "diagram_data": {"mode": "boxplot", "min": 68, "q1": 73.5, "med": 82, "q3": 90, "max": 96, "caption": "5-Number Box Plot: Min = 68, Q1 = 73.5, Median = 82, Q3 = 90, Max = 96. Interquartile Range (IQR) = 90 - 73.5 = 16.5."},
                "concept": "Quartiles divide an ordered data set into four equal parts (each containing 25% of the data). The median (Q2) divides the data into a lower half and an upper half; the first quartile (Q1) is the median of the lower half, and the third quartile (Q3) is the median of the upper half. The Interquartile Range (IQR = Q3 - Q1) measures the spread of the middle 50% of the data.",
                "examples": [
                    {
                        "title": "Example 1: Finding the 5-Number Summary & Interquartile Range (IQR)",
                        "problem": "Find the 5-Number Summary (Min, Q1, Median, Q3, Max) and IQR of: 68, 72, 75, 78, 82, 85, 88, 92, 96.",
                        "block_step": "The middle (5th) value is Median = 82. Lower half {68, 72, 75, 78} has median Q1 = 73.5. Upper half {85, 88, 92, 96} has median Q3 = 90. IQR = 90 - 73.5 = 16.5.",
                        "keys": ["f", "MIN", "f", "1Q", "f", "MED", "g", "3Q", "g", "MAX", "IQR"],
                        "stack_y": "1Q: 73.5 | 3Q: 90",
                        "stack_x": "IQR: 16.5",
                        "ans": "Min = 68, Q1 = 73.5, Med = 82, Q3 = 90, Max = 96; IQR = 16.5",
                        "note": "When n is odd, exclude the overall median before finding the medians of the lower and upper halves."
                    },
                    {
                        "title": "Example 2: Interpreting Quarters (25% / 50% / 75%) on a Box Plot",
                        "problem": "In any Box-and-Whisker Plot, what percent of the data lies inside the central box (between Q1 and Q3), and what percent lies above Q1?",
                        "block_step": "Each of the 4 sections (left whisker, left box half, right box half, right whisker) holds 25% of the data. Thus the box (Q1 to Q3) holds 50%, and 75% lies above Q1.",
                        "keys": ["25", "ENTER", "2", "×"],
                        "stack_y": "25% (×2)",
                        "stack_x": "50% (Middle Box)",
                        "ans": "50% inside the box; 75% above Q1",
                        "note": "A narrower box (smaller IQR) means the middle 50% of the data is more tightly clustered."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "For the ordered data set 10, 20, 30, 40, 50, find the 5-Number Summary (Min, Q1, Median, Q3, Max) and the IQR.", "keys": "Load 5 nums -> [f][1Q], [g][3Q], [IQR]", "yx": "1Q:15 | 3Q:45", "ans": "Min = 10, Q1 = 15, Med = 30, Q3 = 45, Max = 50, IQR = 30"},
                    {"num": 2, "part": "A", "prompt": "For the ordered data set 4, 6, 8, 10, 12, 14, 16, find Q1, Median, Q3, and the IQR.", "keys": "Load 7 nums -> [f][1Q], [g][3Q], [IQR]", "yx": "1Q:6 | 3Q:14", "ans": "Q1 = 6, Med = 10, Q3 = 14, IQR = 8"},
                    {"num": 3, "part": "A", "prompt": "If a box-and-whisker plot has Q1 = 24 and Q3 = 58, what is the Interquartile Range (IQR)?", "keys": "58 [ENTER] 24 [-]", "yx": "Y:58 | X:24", "ans": "34"},
                    {"num": 4, "part": "A", "prompt": "What percent of the data in a box-and-whisker plot falls above the first quartile (Q1)?", "keys": "3 quarters = 3 × 25%", "yx": "75% above Q1", "ans": "75%"},
                    {"num": 5, "part": "B", "prompt": "Grade 6 Science Scores IQR: Eight ordered science test scores are 65, 72, 75, 80, 84, 88, 92, 96. Find Q1, Median, Q3, and the Interquartile Range (IQR).", "keys": "Load 8 nums into [Σ+]", "yx": "1Q:73.5 | 3Q:90", "ans": "Q1 = 73.5, Med = 82, Q3 = 90, IQR = 16.5"},
                    {"num": 6, "part": "B", "prompt": "Find Q1, Median, Q3, and the IQR for the 8 ordered wind speeds (mph): 42, 45, 48, 50, 52, 55, 58, 60.", "keys": "Load 8 nums into [Σ+]", "yx": "1Q:46.5 | 3Q:56.5", "ans": "Q1 = 46.5, Med = 51, Q3 = 56.5, IQR = 10"},
                    {"num": 7, "part": "B", "prompt": "Player A's game scores have an IQR of 4 points, while Player B's scores have an IQR of 19 points. Which player is more consistent? Explain.", "keys": "Compare box widths", "yx": "4 < 19", "ans": "Player A (smaller IQR means the middle 50% of scores are closer together)"},
                    {"num": 8, "part": "B", "prompt": "Outlier Boundary (1.5 × IQR Rule): A data set has Q1 = 40 and Q3 = 60 (so IQR = 20). Any value greater than Q3 + 1.5(IQR) is considered an upper outlier. What is that upper outlier cutoff?", "keys": "60 [ENTER] 1.5 [ENTER] 20 [×] [+]", "yx": "Y:60 | X:30", "ans": "90 (Any score > 90 is an outlier)"},
                    {"num": 9, "part": "C", "prompt": "Find Q1, Median, Q3, and the Interquartile Range (IQR) for the data set {12, 15, 18, 22, 25, 28, 34}.", "keys": "Load 7 nums -> [IQR]", "yx": "1Q:15 | 3Q:28", "ans": "Q1 = 15, Med = 22, Q3 = 28, IQR = 13"},
                    {"num": 10, "part": "C", "prompt": "Grade-Level Benchmark Exam: Exactly 200 sixth graders take a benchmark exam whose box plot has Min = 50, Q1 = 70, Median = 80, Q3 = 90, and Max = 100. About how many students scored between 70 and 90?", "keys": "200 [ENTER] 50 [%]", "yx": "Middle 50% of 200", "ans": "About 100 students (50% of 200)"}
                ]
            },
            {
                "day_num": 41,
                "sec_num": "9.4",
                "title": "Mean Absolute Deviation (MAD) — Average Distance from the Mean",
                "big_ideas_ref": "Big Ideas Grade 6, Section 9.5 (Mean Absolute Deviation)",
                "ccss": "CCSS.MATH.6.SP.B.5c",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "stat_plot",
                "diagram_data": {"mode": "mean_towers", "towers": [10, 12, 14, 16, 18], "mean": 14, "caption": "Data 10, 12, 14, 16, 18 has Mean = 14. Absolute distances |x - 14| are 4, 2, 0, 2, 4 -> MAD = 12 ÷ 5 = 2.4."},
                "concept": "The Mean Absolute Deviation (MAD) is a measure of variation that tells the average distance between each data value and the mean. To find the MAD in 3 steps: (1) Find the mean x̄ of the data. (2) Find the absolute distance |x - x̄| of each data value from the mean. (3) Find the mean of those absolute distances!",
                "examples": [
                    {
                        "title": "Example 1: Calculating Mean Absolute Deviation (MAD)",
                        "problem": "Find the mean and the Mean Absolute Deviation (MAD) of 10, 12, 14, 16, 18.",
                        "block_step": "Step 1: Mean = 70 ÷ 5 = 14. Step 2: Distances |x - 14| are 4, 2, 0, 2, 4. Step 3: Average the distances: (4 + 2 + 0 + 2 + 4) ÷ 5 = 12 ÷ 5 = 2.4.",
                        "keys": ["g", "CLΣ", "10", "Σ+", "12", "Σ+", "14", "Σ+", "16", "Σ+", "18", "Σ+", "g", "x̄", "g", "MAD"],
                        "stack_y": "x̄ = 14",
                        "stack_x": "MAD = 2.4",
                        "ans": "Mean = 14, MAD = 2.4",
                        "note": "Distances from the mean are always positive (absolute values)."
                    },
                    {
                        "title": "Example 2: MAD of Decimal Sprint Times",
                        "problem": "Find the mean and MAD of the 6 sprint times (in seconds): 12.4, 13.0, 12.6, 13.2, 12.8, 14.0.",
                        "block_step": "Mean = 78.0 ÷ 6 = 13.0 s. Distances from 13.0 are 0.6, 0.0, 0.4, 0.2, 0.2, 1.0 (sum = 2.4). MAD = 2.4 ÷ 6 = 0.40 s.",
                        "keys": ["g", "x̄", "g", "MAD"],
                        "stack_y": "x̄ = 13.0 s",
                        "stack_x": "MAD = 0.40 s",
                        "ans": "Mean = 13.0 s, MAD = 0.40 s",
                        "note": "A MAD of 0.40 s means the sprint times vary from the 13.0 s mean by an average of 0.40 s."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Seed-Bomber Catapult MAD: For the three catapult launch distances 150 cm, 162 cm, and 156 cm, find the mean and the Mean Absolute Deviation (MAD).", "keys": "150 [Σ+] 162 [Σ+] 156 [Σ+] [g][MAD]", "yx": "x̄:156 | dists:6,6,0", "ans": "Mean = 156 cm, MAD = 4.0 cm"},
                    {"num": 2, "part": "A", "prompt": "Find the mean and the MAD of the data set: 10, 12, 14, 16, 18.", "keys": "Load 5 nums -> [g][x̄], [g][MAD]", "yx": "x̄:14 | dists:4,2,0,2,4", "ans": "Mean = 14, MAD = 2.4"},
                    {"num": 3, "part": "A", "prompt": "5-Point Sensor Calibration MAD: Five calibration readings from a pressure sensor are 10, 15, 20, 25, and 30. Find the mean and the Mean Absolute Deviation (MAD).", "keys": "Load 5 nums -> [g][x̄], [g][MAD]", "yx": "x̄:20 | dists:10,5,0,5,10", "ans": "Mean = 20, MAD = 6.0"},
                    {"num": 4, "part": "A", "prompt": "What is the Mean Absolute Deviation (MAD) of five identical values: 7, 7, 7, 7, 7? Explain.", "keys": "All distances from 7 are 0", "yx": "x̄:7 | MAD:0", "ans": "Mean = 7, MAD = 0 (Zero spread)"},
                    {"num": 5, "part": "B", "prompt": "Find the mean and the MAD of the data set: 20, 24, 28, 32, 36.", "keys": "Load 5 nums -> [g][x̄], [g][MAD]", "yx": "x̄:28 | dists:8,4,0,4,8", "ans": "Mean = 28, MAD = 4.8"},
                    {"num": 6, "part": "B", "prompt": "Find the mean and the MAD of the 6 sprint times (seconds): 12.4, 13.0, 12.6, 13.2, 12.8, 14.0.", "keys": "Load 6 decimals -> [g][x̄], [g][MAD]", "yx": "x̄:13.0 | MAD:0.40", "ans": "Mean = 13.0 s, MAD = 0.40 s"},
                    {"num": 7, "part": "B", "prompt": "Find the mean and the MAD of the quiz scores: 82, 85, 88, 90, 95.", "keys": "Load 5 nums -> [g][x̄], [g][MAD]", "yx": "x̄:88 | dists:6,3,0,2,7", "ans": "Mean = 88, MAD = 3.6"},
                    {"num": 8, "part": "B", "prompt": "Team A has a mean score of 50 and a MAD of 2.1. Team B has a mean score of 50 and a MAD of 8.4. Which team's scores are more spread out?", "keys": "Compare MADs", "yx": "8.4 > 2.1", "ans": "Team B (a larger MAD indicates greater variation from the mean)"},
                    {"num": 9, "part": "C", "prompt": "For the data set {6, 10, 11, 13}, find the mean, list the four absolute deviations |x - x̄|, and compute the MAD.", "keys": "Mean=10; dists 4+0+1+3=8 ÷ 4", "yx": "x̄:10 | MAD:2", "ans": "Mean = 10; deviations: 4, 0, 1, 3; MAD = 2.0"},
                    {"num": 10, "part": "C", "prompt": "Complete Statistical Profile: For the data set {5, 8, 8, 10, 14}, find the Mean, Median, Mode, Range, IQR, and MAD.", "keys": "1 entry -> 6 stats!", "yx": "x̄:9, Med:8, Mode:8", "ans": "Mean = 9, Med = 8, Mode = 8, Range = 9, IQR = 5.5, MAD = 2.4"}
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
        "kit_summary": "Place Value Studio (PLACE-01) + Fraction Studio (FRAC-01) + Prime Factor Studio (PRIME-01)",
        "hero_png": "fraction_studio_common_denominator.png",
        "coach_misconception": "Students guess signs when adding/subtracting negatives, get -25 instead of +25 for (-5)² on algebraic calculators, undo ×3 before +7 in 3x + 7 = 28, and confuse Permutations (order matters) with Combinations (order doesn't).",
        "coach_remediation": "Use Place Value blocks and the SC-6 Number Line ([f] [LINE]) to show that removing a negative debt (10 - (-4)) equals +14. Notice how RPN 5 [+/-] [x²] squares the entire register (-5)² = +25 without parentheses! Unwrap 2-step equations in reverse (undo ±b first, then ÷a second), and finish with [DICE], [f] [nCr], [g] [nPr], and [f] [?].",
        "sections": [
            {
                "day_num": 42,
                "sec_num": "10.1",
                "title": "Adding & Subtracting Signed Rational Numbers",
                "big_ideas_ref": "Big Ideas Grade 7, Sections 1.2, 1.3, 2.2 & 2.3 (Adding and Subtracting Integers & Rational Numbers)",
                "ccss": "CCSS.MATH.7.NS.A.1",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_regrouping.png",
                "diagram_type": "zero_pairs",
                "diagram_data": {"pos": 5, "neg": 8, "net": -3, "caption": "-8 + 5: 8 Negative (-1) + 5 Positive (+1) counters cancel 5 Zero Pairs, leaving -3. And 10 - (-4) = 10 + 4 = +14."},
                "concept": "To add two numbers with the SAME sign, add their absolute values and keep the common sign (-6 + (-4) = -10). To add two numbers with DIFFERENT signs, subtract the lesser absolute value from the greater absolute value and keep the sign of the number with the greater absolute value (-8 + 5 = -3). To subtract any signed number, add its opposite: a - b = a + (-b), so 10 - (-4) = 10 + 4 = 14.",
                "examples": [
                    {
                        "title": "Example 1: Adding Integers with Different Signs vs. Same Signs",
                        "problem": "Evaluate -8 + 5 and -6 + (-4).",
                        "block_step": "In -8 + 5, 5 Zero Pairs cancel, leaving -3. In -6 + (-4), both numbers are negative so their magnitudes add: -(6 + 4) = -10.",
                        "keys": ["f", "LINE", "8", "+/-", "ENTER", "5", "+", "6", "+/-", "ENTER", "4", "+/-", "+"],
                        "stack_y": "-3 (-8 + 5)",
                        "stack_x": "-10 (-6 + -4)",
                        "ans": "-8 + 5 = -3; -6 + (-4) = -10",
                        "note": "Same signs: add magnitudes and keep the sign. Different signs: subtract magnitudes."
                    },
                    {
                        "title": "Example 2: Subtracting a Negative by Adding the Opposite",
                        "problem": "Evaluate 10 - (-4) and -3/4 - (-5/8).",
                        "block_step": "Rewrite subtraction as adding the opposite: 10 - (-4) = 10 + 4 = 14. For -3/4 - (-5/8): -6/8 + 5/8 = -1/8.",
                        "keys": ["10", "ENTER", "4", "+/-", "-", ".", "3", ".", "4", "+/-", "ENTER", ".", "5", ".", "8", "+/-", "-"],
                        "stack_y": "14 (10 - -4)",
                        "stack_x": "-1/8",
                        "ans": "10 - (-4) = 14; -3/4 - (-5/8) = -1/8",
                        "note": "Subtracting a negative number is always equivalent to adding a positive number."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Evaluate: (a) -15 + 9 and (b) -15 + (-9).", "keys": "15 [+/-] [ENTER] 9 [+] / 9 [+/-] [+]", "yx": "Fight vs Team up", "ans": "(a) -6; (b) -24"},
                    {"num": 2, "part": "A", "prompt": "Evaluate: 14 + (-23).", "keys": "14 [ENTER] 23 [+/-] [+]", "yx": "Y:14 | X:-23", "ans": "-9"},
                    {"num": 3, "part": "A", "prompt": "Evaluate: (a) 12 - (-18) and (b) -12 - (-8).", "keys": "12 [ENTER] 18 [+/-] [-] / 12 [+/-]...", "yx": "12+18 vs -12+8", "ans": "(a) 30; (b) -4"},
                    {"num": 4, "part": "A", "prompt": "Evaluate: -9 - 16.", "keys": "9 [+/-] [ENTER] 16 [-]", "yx": "Y:-9 | X:16", "ans": "-25"},
                    {"num": 5, "part": "B", "prompt": "Chemical Freezing Point Depression: Pure water freezes at 0°C. Adding a salt solute lowers the freezing point by 7.8°C, and adding an alcohol co-solvent lowers it by another 6.4°C. What is the new freezing point of the mixture?", "keys": "0 [ENTER] 7.8 [-] 6.4 [-]", "yx": "Y:-7.8 | X:6.4", "ans": "-14.2°C"},
                    {"num": 6, "part": "B", "prompt": "Evaluate: 6.4 - 11.2.", "keys": "6.4 [ENTER] 11.2 [-]", "yx": "Y:6.4 | X:11.2", "ans": "-4.8"},
                    {"num": 7, "part": "B", "prompt": "Evaluate: -7.5 - (-10.2).", "keys": "7.5 [+/-] [ENTER] 10.2 [+/-] [-]", "yx": "Y:-7.5 | X:-10.2", "ans": "+2.7"},
                    {"num": 8, "part": "B", "prompt": "Evaluate: -3/4 - (-5/8).", "keys": "[.] 3 [.] 4 [+/-] [ENTER] [.] 5 [.] 8 [+/-] [-]", "yx": "-6/8 - (-5/8)", "ans": "-1/8"},
                    {"num": 9, "part": "C", "prompt": "Sub-Zero Week Temperature Swing: During a polar vortex week, the lowest recorded temperature was -22°F and the highest recorded temperature was +14°F. How many degrees warmer was the high temperature than the low temperature?", "keys": "14 [ENTER] 22 [+/-] [-]", "yx": "Y:14 | X:-22", "ans": "36°F"},
                    {"num": 10, "part": "C", "prompt": "Evaluate the rational expression: -2 1/2 + 4 1/4 - (-1 1/8).", "keys": "2.5 [+/-] [ENTER] 4.25 [+] 1.125 [+]", "yx": "1.75 + 1.125", "ans": "2 7/8 (2.875)"}
                ]
            },
            {
                "day_num": 43,
                "sec_num": "10.2",
                "title": "Multiplying & Dividing Signed Rational Numbers",
                "big_ideas_ref": "Big Ideas Grade 7, Sections 1.4, 1.5 & 2.4 (Multiplying and Dividing Rational Numbers)",
                "ccss": "CCSS.MATH.7.NS.A.2",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_common_denominator.png",
                "diagram_type": "zero_pairs",
                "diagram_data": {"pos": 4, "neg": 4, "net": 0, "caption": "Sign Rules for Multiplication & Division: Same Signs -> Positive (+); Different Signs -> Negative (-). So (-6)(-4) = +24 and (-5)² = +25."},
                "concept": "When multiplying or dividing two non-zero numbers: if the signs are the SAME (both positive or both negative), the product or quotient is POSITIVE (+); if the signs are DIFFERENT, the product or quotient is NEGATIVE (-). In a product of multiple factors, an EVEN number of negative factors produces a positive result, and an ODD number of negative factors produces a negative result.",
                "examples": [
                    {
                        "title": "Example 1: Multiplying Signed Numbers & Evaluating (-5)²",
                        "problem": "Evaluate 6 × (-4), (-6) × (-4), and (-5)².",
                        "block_step": "Different signs: 6 × (-4) = -24. Same signs: (-6) × (-4) = +24. Similarly, (-5)² means (-5) × (-5) = +25.",
                        "keys": ["6", "ENTER", "4", "+/-", "×", "5", "+/-", "x²"],
                        "stack_y": "-24 (6 × -4)",
                        "stack_x": "+25 ((-5)²)",
                        "ans": "6×(-4) = -24, (-6)×(-4) = +24, (-5)² = +25",
                        "note": "In (-5)², the negative sign is inside the base being squared, so (-5)(-5) = +25."
                    },
                    {
                        "title": "Example 2: Dividing Signed Fractions (-5/6 ÷ -5/12)",
                        "problem": "Evaluate -5/6 ÷ (-5/12).",
                        "block_step": "Negative ÷ Negative = Positive (+). Multiply by the reciprocal: (-5/6) × (-12/5) = +60/30 = +2.",
                        "keys": [".", "5", ".", "6", "+/-", "ENTER", ".", "5", ".", "12", "+/-", "÷"],
                        "stack_y": "-5/6",
                        "stack_x": "-5/12 -> +2",
                        "ans": "+2",
                        "note": "Determine the sign of the answer first, then divide the magnitudes."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Evaluate: (a) 7 × (-8) and (b) (-7) × (-8).", "keys": "7 [ENTER] 8 [+/-] [×] / 7 [+/-]...", "yx": "1 neg vs 2 negs", "ans": "(a) -56; (b) +56"},
                    {"num": 2, "part": "A", "prompt": "Evaluate: (a) -45 ÷ 9 and (b) -45 ÷ (-9).", "keys": "45 [+/-] [ENTER] 9 [÷] / 9 [+/-] [÷]", "yx": "1 neg vs 2 negs", "ans": "(a) -5; (b) +5"},
                    {"num": 3, "part": "A", "prompt": "Evaluate (-5)². Explain why the result is positive.", "keys": "5 [+/-] [x²]", "yx": "(-5) × (-5)", "ans": "+25 (2 negative factors = positive)"},
                    {"num": 4, "part": "A", "prompt": "Evaluate (-2)³. Explain why the cube of a negative number is negative.", "keys": "2 [+/-] [x³]", "yx": "(-2)×(-2)×(-2)", "ans": "-8 (3 negative factors = odd count = negative)"},
                    {"num": 5, "part": "B", "prompt": "Evaluate: (-3.5) × (-2.4).", "keys": "3.5 [+/-] [ENTER] 2.4 [+/-] [×]", "yx": "Y:-3.5 | X:-2.4", "ans": "+8.4"},
                    {"num": 6, "part": "B", "prompt": "Evaluate: -14.4 ÷ 1.2.", "keys": "14.4 [+/-] [ENTER] 1.2 [÷]", "yx": "Y:-14.4 | X:1.2", "ans": "-12"},
                    {"num": 7, "part": "B", "prompt": "Evaluate: (-2/3) × (9/10).", "keys": "[.] 2 [.] 3 [+/-] [ENTER] [.] 9 [.] 10 [×]", "yx": "Y:-2/3 | X:9/10", "ans": "-3/5 (-0.6)"},
                    {"num": 8, "part": "B", "prompt": "Evaluate: -5/6 ÷ (-5/12).", "keys": "[.] 5 [.] 6 [+/-] [ENTER] [.] 5 [.] 12 [+/-] [÷]", "yx": "Y:-5/6 | X:-5/12", "ans": "+2"},
                    {"num": 9, "part": "C", "prompt": "Evaluate the triple product: (-4) × (-5) × (-6).", "keys": "4 [+/-] [ENTER] 5 [+/-] [×] 6 [+/-] [×]", "yx": "Y:20 | X:-6", "ans": "-120"},
                    {"num": 10, "part": "C", "prompt": "Evaluate using the Order of Operations: (-18) × 4 - (-36) ÷ (-9).", "keys": "18 [+/-] [ENTER] 4 [×] 36 [+/-] [ENTER] 9 [+/-] [÷] [-]", "yx": "Y:-72 | X:4", "ans": "-76"}
                ]
            },
            {
                "day_num": 44,
                "sec_num": "10.3",
                "title": "Solving Two-Step Equations (ax + b = c)",
                "big_ideas_ref": "Big Ideas Grade 7, Sections 3.3–3.5 (Solving Two-Step Equations)",
                "ccss": "CCSS.MATH.7.EE.B.4a",
                "kit_id": "PLACE-01",
                "kit_name": "Place Value Studio",
                "asset_png": "place_value_ortho_steps.png",
                "diagram_type": "balance_scale",
                "diagram_data": {"left": "3x + 7", "right": "28", "sol": "Step 1: 28 - 7 = 21 -> Step 2: 21 ÷ 3 = 7", "caption": "Solving 3x + 7 = 28: Step 1 undo addition (28 - 7 = 21 -> 3x = 21); Step 2 undo multiplication (21 ÷ 3 = 7 -> x = 7)."},
                "concept": "A two-step equation contains two operations. To isolate the variable, undo the operations in the REVERSE order of operations: Step 1 undo addition or subtraction first to isolate the variable term (ax), and Step 2 undo multiplication or division second to isolate the variable x.",
                "examples": [
                    {
                        "title": "Example 1: Solving a Two-Step Equation (3x + 7 = 28)",
                        "problem": "Solve 3x + 7 = 28 and check your solution.",
                        "block_step": "Step 1: Subtract 7 from both sides: 3x = 28 - 7 = 21. Step 2: Divide both sides by 3: x = 21 ÷ 3 = 7. Check: 3(7) + 7 = 28.",
                        "keys": ["28", "ENTER", "7", "-", "3", "÷", "28", "x⇄y", "3", "×", "7", "+", "≠"],
                        "stack_y": "28 (Right)",
                        "stack_x": "3(7)+7=28 -> NO",
                        "ans": "x = 7 (Step 1: 3x = 21)",
                        "note": "Undo ±b first and ×a second, then test with [≠] (flashes NO when balanced!)."
                    },
                    {
                        "title": "Example 2: Two-Step Equation with a Negative Coefficient (-3x + 14 = 2)",
                        "problem": "Solve -3x + 14 = 2 and check your solution.",
                        "block_step": "Step 1: Subtract 14 from both sides: -3x = 2 - 14 = -12. Step 2: Divide both sides by -3: x = -12 ÷ (-3) = +4.",
                        "keys": ["2", "ENTER", "14", "-", "3", "+/-", "÷"],
                        "stack_y": "-12 (-3x)",
                        "stack_x": "-3 -> x = 4",
                        "ans": "x = 4",
                        "note": "Check with [≠]: 2 [ENTER] 3 [+/-] [ENTER] 4 [×] 14 [+] [≠] flashes NO!"
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Solve 4x + 9 = 45. Show the result of Step 1 (4x = ?) and the final value of x.", "keys": "45 [ENTER] 9 [-] 4 [÷]", "yx": "Y:36 | X:4", "ans": "4x = 36; x = 9"},
                    {"num": 2, "part": "A", "prompt": "Solve 5x - 12 = 38.", "keys": "38 [ENTER] 12 [+] 5 [÷]", "yx": "Y:50 | X:5", "ans": "5x = 50; x = 10"},
                    {"num": 3, "part": "A", "prompt": "Solve 6y + 11 = 59.", "keys": "59 [ENTER] 11 [-] 6 [÷]", "yx": "Y:48 | X:6", "ans": "6y = 48; y = 8"},
                    {"num": 4, "part": "A", "prompt": "Solve 8n - 15 = 49.", "keys": "49 [ENTER] 15 [+] 8 [÷]", "yx": "Y:64 | X:8", "ans": "8n = 64; n = 8"},
                    {"num": 5, "part": "B", "prompt": "Solve m ÷ 4 + 6 = 15.", "keys": "15 [ENTER] 6 [-] 4 [×]", "yx": "Y:9 | X:4", "ans": "m / 4 = 9; m = 36"},
                    {"num": 6, "part": "B", "prompt": "Solve k ÷ 3 - 5 = 7.", "keys": "7 [ENTER] 5 [+] 3 [×]", "yx": "Y:12 | X:3", "ans": "k / 3 = 12; k = 36"},
                    {"num": 7, "part": "B", "prompt": "Solve -3x + 14 = 2.", "keys": "2 [ENTER] 14 [-] 3 [+/-] [÷]", "yx": "Y:-12 | X:-3", "ans": "-3x = -12; x = 4"},
                    {"num": 8, "part": "B", "prompt": "Solve 2.5w + 8 = 23.", "keys": "23 [ENTER] 8 [-] 2.5 [÷]", "yx": "Y:15 | X:2.5", "ans": "2.5w = 15; w = 6"},
                    {"num": 9, "part": "C", "prompt": "Appliance Repair Call: A repair technician charges a $35 service visit fee plus $25 per hour of labor. If the total bill is $160, write and solve a two-step equation to find how many hours h the technician worked.", "keys": "160 [ENTER] 35 [-] 25 [÷]", "yx": "Y:125 | X:25", "ans": "25h + 35 = 160; h = 5 hours"},
                    {"num": 10, "part": "C", "prompt": "Skateboard Savings Plan: You already have $45 saved toward a $120 custom skateboard and save $15 each week. Write and solve a two-step equation to find how many weeks w it will take to reach $120.", "keys": "120 [ENTER] 45 [-] 15 [÷]", "yx": "Y:75 | X:15", "ans": "15w + 45 = 120; w = 5 weeks"}
                ]
            },
            {
                "day_num": 45,
                "sec_num": "10.4",
                "title": "Probability, Compound Events & Counting Methods (n!, nPr, nCr)",
                "big_ideas_ref": "Big Ideas Grade 7, Chapter 7 (Probability) & SC-6 Graduation Finale",
                "ccss": "CCSS.MATH.7.SP.C.5",
                "kit_id": "FRAC-01",
                "kit_name": "84mm Fraction Studio",
                "asset_png": "fraction_studio_twin_comparator.png",
                "diagram_type": "prob_spinner",
                "diagram_data": {"blue": 4, "gold": 3, "red": 3, "caption": "10-Sector Spinner Ratio: P(Blue) = 4/10 = 2/5 = 0.40 = 40%. Plus Factorials (n!), Permutations (nPr), and Combinations (nCr)."},
                "concept": "Theoretical probability is the ratio of favorable outcomes to total equally likely outcomes: P(event) = Favorable ÷ Total, written as a simplified fraction, decimal, or percent. The probability of an event NOT occurring is the complement: P(not E) = 1 - P(E). For counting arrangements: n! counts ways to order all n items; nPr counts ordered permutations; and nCr counts unordered combinations.",
                "examples": [
                    {
                        "title": "Example 1: Theoretical Probability & Factorial Arrangements (n!)",
                        "problem": "A 10-sector spinner has 4 Blue, 3 Gold, and 3 Red sectors. Find P(Blue) as a fraction, decimal, and percent, and find how many ways 5 trophies can be arranged in a row (5!).",
                        "block_step": "P(Blue) = 4/10 = 2/5 = 0.40 = 40%. The number of ways to arrange 5 trophies is 5! = 5 × 4 × 3 × 2 × 1 = 120 ways.",
                        "keys": [".", "4", ".", "10", "g", "SIMP", "5", "x!"],
                        "stack_y": "2/5 (0.4 = 40%)",
                        "stack_x": "120 (5!)",
                        "ans": "P(Blue) = 2/5 = 0.4 = 40%; 5! = 120 ways",
                        "note": "Every probability lies between 0 (impossible) and 1 (certain)."
                    },
                    {
                        "title": "Example 2: Combinations (nCr) vs. Permutations (nPr)",
                        "problem": "Compare choosing 3 pizza toppings from 10 options (order does not matter) versus awarding 1st, 2nd, and 3rd place among 10 runners (order matters).",
                        "block_step": "Unordered combinations: 10C3 = (10 × 9 × 8) ÷ (3 × 2 × 1) = 120. Ordered permutations: 10P3 = 10 × 9 × 8 = 720.",
                        "keys": ["10", "ENTER", "3", "f", "nCr", "10", "ENTER", "3", "g", "nPr"],
                        "stack_y": "120 (nCr)",
                        "stack_x": "720 (nPr)",
                        "ans": "120 combinations vs. 720 permutations",
                        "note": "720 is 6 times 120 because there are 3! = 6 ways to order each group of 3."
                    }
                ],
                "problems": [
                    {"num": 1, "part": "A", "prompt": "Not Rolling a Six: You roll a fair 6-sided die once. What is the probability of rolling a 5, and what is the probability of NOT rolling a 6?", "keys": "1/6; and 1 - 1/6 = 5/6", "yx": "1/6 and 5/6", "ans": "P(5) = 1/6; P(not 6) = 5/6"},
                    {"num": 2, "part": "A", "prompt": "Complementary Weather Probability: A weather forecast states there is a 0.35 (35%) probability of rain today. What is the probability that it will NOT rain today?", "keys": "1 [ENTER] 0.35 [-]", "yx": "1 - 0.35", "ans": "0.65 (65% or 13/20)"},
                    {"num": 3, "part": "A", "prompt": "Double Sixes & High Sums: You roll two fair 6-sided dice (36 equally likely outcomes). What is the probability of rolling double sixes (6, 6), and what is the probability of rolling a sum of 11 or 12?", "keys": "1/36; and 3/36 = 1/12", "yx": "1/36 and 1/12", "ans": "P(double 6s) = 1/36; P(sum 11 or 12) = 3/36 = 1/12"},
                    {"num": 4, "part": "A", "prompt": "In how many different ways can 4 students line up at the classroom door (4!)?", "keys": "4 [x!]", "yx": "4×3×2×1", "ans": "24 ways"},
                    {"num": 5, "part": "B", "prompt": "In how many different ways can 6 books be arranged left-to-right on a shelf (6!)?", "keys": "6 [x!]", "yx": "6×5×4×3×2×1", "ans": "720 ways"},
                    {"num": 6, "part": "B", "prompt": "How many different 3-person project teams can be chosen from 8 students when order does NOT matter?", "keys": "8 [ENTER] 3 [f][nCr]", "yx": "Y:8 | X:3", "ans": "56 teams"},
                    {"num": 7, "part": "B", "prompt": "How many different ways can 1st, 2nd, and 3rd place ribbons be awarded among 8 science fair finalists when order DOES matter?", "keys": "8 [ENTER] 3 [g][nPr]", "yx": "Y:8 | X:3", "ans": "336 podium arrangements"},
                    {"num": 8, "part": "B", "prompt": "Triple Coin Toss: You flip a fair coin 3 times in a row. What is the probability of getting Heads on all 3 flips, written as a fraction and as a percent?", "keys": "1/2 × 1/2 × 1/2 = 1/8", "yx": "1/8 = 0.125", "ans": "1/8 (12.5%)"},
                    {"num": 9, "part": "C", "prompt": "Consecutive Matching Socks: A drawer contains 6 blue socks and 4 gray socks (10 socks total). If you pull out 2 socks in a row without replacement, what is the probability that both socks are blue?", "keys": "6/10 × 5/9 = 30/90", "yx": "30/90 = 1/3", "ans": "1/3 (6/10 × 5/9 = 30/90)"},
                    {"num": 10, "part": "C", "prompt": "Toppings vs. Medals Finale: From 10 choices, compare the number of ways to choose 3 unordered pizza toppings (10C3) with the number of ways to award 1st, 2nd, and 3rd place medals (10P3). By what factor do they differ?", "keys": "10 [ENTER] 3 [f][nCr] / [g][nPr]", "yx": "Y:120 | X:720", "ans": "120 combinations vs. 720 permutations (differ by 3! = 6)"}
                ]
            }
        ]
    }
])

