#!/usr/bin/env python3
"""
Section-by-Section Big Ideas Math Middle School Pedagogy, Unit Tracking,
Textbook Methods, and Step-by-Step Manipulative Block Instructions
for all 45 Sections (Units 1–10 in big_ideas_sc6_sections_data.py).
"""

from typing import Any, Dict

SECTION_PEDAGOGY: Dict[str, Dict[str, Any]] = {
    # =========================================================================
    # UNIT 1: NUMERICAL EXPRESSIONS & FACTORS (Sections 1.1 - 1.5)
    # =========================================================================
    "1.1": {
        "unit_name": "Unit 1: Numerical Expressions & Factors",
        "big_ideas_method": "Rectangular Array Model & Division Check (Dividend = Divisor × Quotient + Remainder)",
        "block_steps": [
            "Open Kit COUNT-01 (Counting & Array Tiles) and count out 23 unit tiles onto the Gridfinity baseplate.",
            "Arrange the tiles into equal rows of 4. Count 5 complete rows of 4 tiles (5 × 4 = 20 tiles).",
            "Place the 3 leftover tiles beside the array as Remainder R = 3, proving 23 = 4 × 5 + 3.",
        ],
        "textbook_steps": "1. Divide 23 ÷ 4 to find the greatest whole number of groups of 4: 5 groups (5 × 4 = 20).\n2. Subtract 23 - 20 = 3 to find the remainder (R = 3, which is less than the divisor 4).\n3. Check with the Division Algorithm: Quotient × Divisor + Remainder = 5 × 4 + 3 = 23.",
        "problem_methods": ("Equal-Rows Array", "Quotient & Remainder", "Division Check (q × d + r)"),
    },
    "1.2": {
        "unit_name": "Unit 1: Numerical Expressions & Factors",
        "big_ideas_method": "Repeated Multiplication Factors, Perfect Squares (2D Array) & Cubes (3D Stack)",
        "block_steps": [
            "Open Kit COUNT-01 (Counting & Array Tiles) and lay down a row of 4 tiles for the base (4).",
            "For 4², build a 4 × 4 square array (4 rows of 4 = 16 tiles)—compare to 2 rows of 4 (4 × 2 = 8 tiles).",
            "For 4³, stack 4 identical 4 × 4 square layers high to build a 3D cube of 16 × 4 = 64 tiles.",
        ],
        "textbook_steps": "1. Identify the base (4) and the exponent (2 or 3).\n2. Write the power as repeated multiplication of the base: 4² = 4 × 4 = 16.\n3. For 4³, multiply the base 3 times: 4³ = 4 × 4 × 4 = 16 × 4 = 64 (never multiply base × exponent!).",
        "problem_methods": ("Repeated Factors (b × b)", "Square & Cube Evaluation", "Exponential Growth Model"),
    },
    "1.3": {
        "unit_name": "Unit 1: Numerical Expressions & Factors",
        "big_ideas_method": "Order of Operations (PEMDAS: Grouping Symbols -> Powers -> Multiply/Divide L-to-R -> Add/Subtract L-to-R)",
        "block_steps": [
            "Open Kit COUNT-01 (Counting & Array Tiles) and use two zones of the lid for the two parentheses groups.",
            "In Zone 1, combine 8 tiles and 4 tiles to model (8 + 4) = 12 tiles.",
            "In Zone 2, start with 9 tiles and remove 3 tiles to model (9 - 3) = 6, then multiply 12 groups of 6 = 72.",
        ],
        "textbook_steps": "1. Grouping Symbols First: Evaluate inside both sets of parentheses: (8 + 4) = 12 and (9 - 3) = 6.\n2. Substitute the simplified values back into the expression: 12 × 6.\n3. Multiply to find the final value: 12 × 6 = 72.",
        "problem_methods": ("Grouping Symbols First", "PEMDAS Step-by-Step", "Multi-Step Expression"),
    },
    "1.4": {
        "unit_name": "Unit 1: Numerical Expressions & Factors",
        "big_ideas_method": "Factor Trees, Prime vs. Composite Testing & Prime-Power Factorization",
        "block_steps": [
            "Open Kit PRIME-01 (Prime Factor Studio) and set the logarithmic slide-rule scale on the box wall.",
            "Select the prime blocks that multiply to 60: two blue [2] blocks, one green [3] block, and one gold [5] block.",
            "Stack [2] + [2] + [3] + [5] in any order—the tower height always aligns with 60 on the logarithmic scale!",
        ],
        "textbook_steps": "1. Branch 60 into any factor pair (such as 6 × 10 or 4 × 15) on a Factor Tree.\n2. Continue splitting composite branches until only prime leaves remain: 6 = 2 × 3 and 10 = 2 × 5.\n3. Group identical prime factors using exponents from least to greatest: 60 = 2² × 3 × 5.",
        "problem_methods": ("Factor Tree Branches", "Prime-Power Form", "Prime Factorization Check"),
    },
    "1.5": {
        "unit_name": "Unit 1: Numerical Expressions & Factors",
        "big_ideas_method": "Venn Diagram of Prime Factors — Shared Overlap for GCF & Tallest Prime Powers for LCM",
        "block_steps": [
            "Open Kit PRIME-01 (Prime Factor Studio) and build Tower 20 ([2][2][5]) and Tower 50 ([2][5][5]) side by side.",
            "For GCF, pull out the prime blocks shared by BOTH towers: one [2] and one [5] -> [2][5] = 10.",
            "For LCM, build the tallest union covering both towers: two [2]s and two [5]s -> [2][2][5][5] = 100.",
        ],
        "textbook_steps": "1. Write the prime factorization of each number: 20 = 2² × 5 and 50 = 2 × 5².\n2. GCF (Shared Factors): Multiply the common prime factors with lesser exponents: 2¹ × 5¹ = 10.\n3. LCM (All Factors): Multiply all prime factors using the greatest exponent of each: 2² × 5² = 4 × 25 = 100.",
        "problem_methods": ("Prime Factor GCF & LCM", "Shared Factors vs. Multiples", "GCF & LCM Word Problem"),
    },

    # =========================================================================
    # UNIT 2: FRACTIONS & DECIMALS (Sections 2.1 - 2.5)
    # =========================================================================
    "2.1": {
        "unit_name": "Unit 2: Fractions & Decimals",
        "big_ideas_method": "Equivalent Fractions via GCF Simplification & Adding/Subtracting with Least Common Denominator (LCD)",
        "block_steps": [
            "Open Kit FRAC-01 (84mm Fraction Studio) and place the 84mm Whole (1) datum block on the comparator lid.",
            "Stack four 1/6 blocks (4 × 14mm = 56mm) next to two 1/3 blocks (2 × 28mm = 56mm) to see 12/18 = 6/9 = 2/3.",
            "To add 1/3 + 1/4, stack one 1/3 block (28mm) and one 1/4 block (21mm) = 49mm, matching seven 1/12 blocks (7/12).",
        ],
        "textbook_steps": "1. Divide numerator and denominator of 12/18 by common factors: (12 ÷ 2)/(18 ÷ 2) = 6/9, then (6 ÷ 3)/(9 ÷ 3) = 2/3.\n2. To add unlike fractions (1/3 + 1/4), find the LCD of 3 and 4, which is 12.\n3. Rewrite as equivalent twelfths and add numerators: 4/12 + 3/12 = 7/12.",
        "problem_methods": ("Simplest Form / Mixed-Improper", "LCD Addition & Subtraction", "Mixed Number Regrouping"),
    },
    "2.2": {
        "unit_name": "Unit 2: Fractions & Decimals",
        "big_ideas_method": "Area/Tower Model for Fraction × Fraction & Cross-Canceling Common Factors",
        "block_steps": [
            "Open Kit FRAC-01 (84mm Fraction Studio) and stand three 1/4 blocks to build a 3/4 tower (63.0 mm tall).",
            "To find 1/2 OF 3/4, measure half the height of the 63.0 mm tower: 63.0 mm ÷ 2 = 31.5 mm.",
            "Place three 1/8 blocks (3 × 10.5 mm = 31.5 mm) alongside to prove 1/2 × 3/4 = 3/8.",
        ],
        "textbook_steps": "1. Multiply the numerators and multiply the denominators: (1 × 3) / (2 × 4) = 3/8.\n2. For mixed numbers (1 1/2 × 2 2/3), convert to improper fractions first: 3/2 × 8/3.\n3. Divide out common factors on the diagonal (cancel the 3s and divide 8 by 2) to get 4.",
        "problem_methods": ("Numerator × Numerator / Cross-Cancel", "Improper Fraction Conversion", "Scaling & Multi-Step Product"),
    },
    "2.3": {
        "unit_name": "Unit 2: Fractions & Decimals",
        "big_ideas_method": "Measurement Division ('How Many Fit?') & Multiplying by the Reciprocal (Keep-Change-Flip)",
        "block_steps": [
            "Open Kit FRAC-01 (84mm Fraction Studio) and build a 3/4 dividend tower (three 21mm blocks = 63.0 mm).",
            "Stack 1/8 divisor blocks (10.5 mm each) right beside the 3/4 tower until the heights match.",
            "Count the 1/8 blocks: every 1/4 block matches two 1/8 blocks, so 3 × 2 = 6 blocks fit (3/4 ÷ 1/8 = 6).",
        ],
        "textbook_steps": "1. Write the division problem: 3/4 ÷ 1/8.\n2. Find the reciprocal of the divisor (flip 1/8 to 8/1) and rewrite division as multiplication: 3/4 × 8/1.\n3. Simplify common factors (8 ÷ 4 = 2) and multiply: 3 × 2 = 6.",
        "problem_methods": ("Multiply by Reciprocal", "Mixed-Number Reciprocal Division", "Equal-Size Measurement Cuts"),
    },
    "2.4": {
        "unit_name": "Unit 2: Fractions & Decimals",
        "big_ideas_method": "Vertical Decimal Point Alignment (+/-) & Counting Decimal Places / Estimation (×)",
        "block_steps": [
            "Open Kit PLACE-01 (Place Value Studio) and separate 14.85 into Whole Tens/Ones (14) and Tenths/Hundredths (0.85).",
            "To add 14.60 + 3.85, place 6 tenths + 8 tenths (regroup 10 tenths -> 1 one + 4 tenths) and 5 hundredths.",
            "Combine the whole ones (14 + 3 + 1 = 18) with the decimal part (0.45) to read 18.45.",
        ],
        "textbook_steps": "1. Line up the decimal points vertically and annex a trailing zero so both numbers have hundredths: 14.60 + 3.85.\n2. Add column by column from right to left (hundredths, tenths, ones, tens): 14.60 + 3.85 = 18.45.\n3. Check by subtracting 18.45 - 3.85 = 14.60.",
        "problem_methods": ("Vertical Decimal Alignment", "Decimal Place Count & Estimate", "Multi-Step Money & Area"),
    },
    "2.5": {
        "unit_name": "Unit 2: Fractions & Decimals",
        "big_ideas_method": "Power-of-10 Divisor Shift & 3-Way Translation (Decimal <-> Mixed Number <-> Quotient + Remainder)",
        "block_steps": [
            "Open Kit FRAC-01 / PLACE-01 and model 23 ÷ 4 using 5 whole blocks and 3 fourths (5 3/4 = 23/4).",
            "Trade the 3 leftover fourths into 0.75 (7 tenths + 5 hundredths) to read the exact decimal 5.75.",
            "For decimal divisors like 15.6 ÷ 0.12, shift both decimals 2 places right (× 100) to divide 1,560 ÷ 12 = 130.",
        ],
        "textbook_steps": "1. Quotient & Remainder Form: 23 ÷ 4 = 5 R 3 (5 full groups of 4 with 3 left over).\n2. Mixed Number & Improper Fraction Form: Write the remainder over the divisor -> 5 3/4 = 23/4.\n3. Decimal Form: Divide 3.00 ÷ 4 = 0.75 -> 5.75 (for decimal divisors, multiply both by 10 or 100 first).",
        "problem_methods": ("3-Way Form Translation", "Power-of-10 Divisor Shift", "Decimal Division Application"),
    },

    # =========================================================================
    # UNIT 3: RATIOS, RATES & PERCENTS (Sections 3.1 - 3.5)
    # =========================================================================
    "3.1": {
        "unit_name": "Unit 3: Ratios, Rates & Percents",
        "big_ideas_method": "Part-to-Part vs. Part-to-Whole Tape Diagrams & GCF Ratio Simplification",
        "block_steps": [
            "Open Kit COUNT-01 (Counting & Array Tiles) and place 3 blue tiles (Row A) above 2 gold tiles (Row B) for 3:2.",
            "To model 18 builders and 12 speedrunners, group by GCF(18, 12) = 6 per tile -> 3 blue tiles : 2 gold tiles.",
            "Count all 3 + 2 = 5 tiles to read the Part-to-Whole ratio: 3:5 (18 out of 30 total).",
        ],
        "textbook_steps": "1. Part-to-Part Ratio: Compare 18 builders to 12 speedrunners -> 18:12. Divide both by GCF(18, 12) = 6 -> 3:2.\n2. Total (Whole): Add the parts: 18 + 12 = 30 total members.\n3. Part-to-Whole Ratio: Compare 18 builders to 30 total -> 18:30, which simplifies by GCF = 6 to 3:5.",
        "problem_methods": ("Part-to-Part & Part-to-Whole", "Tape Diagram Box Value", "Total-Share Tape Problem"),
    },
    "3.2": {
        "unit_name": "Unit 3: Ratios, Rates & Percents",
        "big_ideas_method": "Equivalent Ratio Tables & Double Number Lines via Repeated Addition or Scale Factors",
        "block_steps": [
            "Open Kit COUNT-01 (Counting & Array Tiles) and lay down Step 1 of the ratio table: 8 distance tiles and 3 time tiles.",
            "Add identical groups of (8 m, 3 s) to build the Double Number Line: (8, 3), (16, 6), (24, 9), (32, 12), (40, 15).",
            "Notice that 5 jumps of 3 seconds reach 15 seconds, and 5 jumps of 8 meters reach 40 meters!",
        ],
        "textbook_steps": "1. Set up a Ratio Table (or Double Number Line) starting with Distance = 8 m and Time = 3 s.\n2. Find the scale factor from 3 seconds to 15 seconds: 15 ÷ 3 = 5 (5 equal steps).\n3. Multiply the distance by the same scale factor: 8 m × 5 = 40 meters.",
        "problem_methods": ("Ratio Table / Double Number Line", "Scale Factor Multiplication", "Multi-Step Ratio Scaling"),
    },
    "3.3": {
        "unit_name": "Unit 3: Ratios, Rates & Percents",
        "big_ideas_method": "Unit Rate Method (Dividing to Find Amount per 1 Unit) & Best-Buy Unit Price Comparison",
        "block_steps": [
            "Open Kit COUNT-01 (Counting & Array Tiles) and represent 5 minutes with 5 equal 1-minute trays.",
            "Divide 315 words equally across the 5 trays: 315 ÷ 5 = 63 words per 1-minute tray.",
            "To compare two store deals, find the price of 1 single unit (dollars ÷ items) for each deal!",
        ],
        "textbook_steps": "1. Write the rate as a fraction with the 'per' unit in the denominator: 315 words / 5 minutes.\n2. Divide both numerator and denominator by 5 to get 1 minute in the denominator: 63 words / 1 minute.\n3. Always check units: 'Dollars per ounce' means Dollars ÷ Ounces!",
        "problem_methods": ("Unit Rate (Amount per 1)", "Unit Rate Scaling", "Best-Buy Unit Price Showdown"),
    },
    "3.4": {
        "unit_name": "Unit 3: Ratios, Rates & Percents",
        "big_ideas_method": "10×10 Hundredths Grid ('Per 100') & 3-Way Fraction-Decimal-Percent Translation",
        "block_steps": [
            "Open Kit FRAC-01 (84mm Fraction Studio) and compare the fraction tower to the 100% Whole datum.",
            "Scale 7/20 so the denominator is 100 (multiply top and bottom by 5): 7/20 = 35/100.",
            "Read all 3 equivalent forms from 35 hundredths: Fraction = 7/20, Decimal = 0.35, Percent = 35%.",
        ],
        "textbook_steps": "1. Fraction to Decimal: Divide numerator by denominator: 7 ÷ 20 = 0.35.\n2. Decimal to Percent: Multiply by 100 (shift decimal 2 places right): 0.35 = 35%.\n3. Finding a Percent of a Number (35% of 80): Multiply 0.35 × 80 = 28.",
        "problem_methods": ("Fraction <-> Decimal <-> Percent", "Percent of a Number (p% × Whole)", "Find the Whole (Part ÷ p%)"),
    },
    "3.5": {
        "unit_name": "Unit 3: Ratios, Rates & Percents",
        "big_ideas_method": "Discounts, Markup/Tax, Percent Change (Change / Original) & Unit Factor Conversions",
        "block_steps": [
            "Open Kit PLACE-01 (Place Value Studio) and model $60 across four 25% quarters ($15 per quarter).",
            "Remove one 25% quarter ($15 discount) to leave three quarters (75% of $60 = $45 sale price).",
            "For Percent Change, always divide the Change (New - Old) by the ORIGINAL starting value!",
        ],
        "textbook_steps": "1. Discount & Sale Price: Discount = 25% of $60 = 0.25 × 60 = $15; Sale Price = $60 - $15 = $45 (or 0.75 × $60 = $45).\n2. Percent Change: (New - Original) ÷ Original × 100%.\n3. Unit Conversion: Multiply by the conversion factor that cancels the starting unit.",
        "problem_methods": ("Discount, Tax & Tip", "Percent Change & Unit Conversion", "2-Way Sale Price & Rate Proof"),
    },

    # =========================================================================
    # UNIT 4: ALGEBRAIC EXPRESSIONS & PROPERTIES (Sections 4.1 - 4.4)
    # =========================================================================
    "4.1": {
        "unit_name": "Unit 4: Algebraic Expressions & Properties",
        "big_ideas_method": "Variable Substitution, Evaluating Algebraic Expressions & Translating Verbal Phrases",
        "block_steps": [
            "Open Kit ALGB-01 (Algebra Boxes & Stage) and place 4 green x-rods and 7 yellow unit cubes on the stage for 4x + 7.",
            "To evaluate at x = 5, replace each green x-rod with 5 unit cubes (4 groups of 5 = 20 unit cubes).",
            "Combine the 20 cubes from the x-rods with the 7 constant cubes: 20 + 7 = 27!",
        ],
        "textbook_steps": "1. Write the algebraic expression: 4x + 7.\n2. Substitute x = 5 in parentheses: 4(5) + 7.\n3. Follow the Order of Operations (multiply before adding): 20 + 7 = 27.",
        "problem_methods": ("Variable Substitution", "Two-Variable & Power Evaluation", "Translating & Modeling Phrases"),
    },
    "4.2": {
        "unit_name": "Unit 4: Algebraic Expressions & Properties",
        "big_ideas_method": "Identifying Terms/Coefficients/Constants & Sorting and Combining Like Terms",
        "block_steps": [
            "Open Kit ALGB-01 (Algebra Boxes & Stage) and lay out 4x + 5 + 2x + 3 using green x-rods and yellow 1-cubes.",
            "Sort matching shapes together: group the 4 x-rods and 2 x-rods into 6 x-rods (6x), and 5 cubes + 3 cubes into 8 cubes (+ 8).",
            "Notice that blue x²-flats (18×18mm), green x-rods (18×7mm), and yellow 1-cubes (7×7mm) have different dimensions and never mix!",
        ],
        "textbook_steps": "1. Use Commutative and Associative Properties to group like terms: (4x + 2x) + (5 + 3).\n2. Add the coefficients of the x-terms and add the constants: (4 + 2)x + 8 = 6x + 8.\n3. Verify by substituting x = 10 into both: 4(10)+5+2(10)+3 = 68 and 6(10)+8 = 68.",
        "problem_methods": ("Combining Like Terms", "x²-Flats vs. x-Rods vs. Constants", "Perimeter & Equivalence Check"),
    },
    "4.3": {
        "unit_name": "Unit 4: Algebraic Expressions & Properties",
        "big_ideas_method": "The Distributive Property Area Model — Splitting Rectangles as a(b + c) = ab + ac",
        "block_steps": [
            "Open Kit ALGB-01 / COUNT-01 and build a rectangle 6 rows tall by (10 + 4) columns wide.",
            "Way 1 (Total Width): Add 10 + 4 = 14 columns first, then multiply 6 × 14 = 84 tiles.",
            "Way 2 (Split Rectangle): Multiply Left Room (6 × 10 = 60) + Right Room (6 × 4 = 24) = 84 tiles!",
        ],
        "textbook_steps": "1. Numeric Distribution: 6(10 + 4) = 6(10) + 6(4) = 60 + 24 = 84.\n2. Algebraic Distribution: Multiply the outside factor by EVERY term inside the parentheses: 4(3x + 5) = 4(3x) + 4(5) = 12x + 20.\n3. If like terms remain outside, combine them after distributing.",
        "problem_methods": ("Area Model & Mental Math Split", "Distributing Over Addition/Subtraction", "Distribute Then Combine Terms"),
    },
    "4.4": {
        "unit_name": "Unit 4: Algebraic Expressions & Properties",
        "big_ideas_method": "Factoring Numerical & Algebraic Expressions by Dividing Out the Greatest Common Factor (GCF)",
        "block_steps": [
            "Open Kit ALGB-01 (Algebra Boxes & Stage) and place 18 green x-rods and 24 yellow unit cubes on the stage for 18x + 24.",
            "Find the greatest number of identical rows you can arrange: GCF(18, 24) = 6 equal rows.",
            "Place 18x ÷ 6 = 3 x-rods and 24 ÷ 6 = 4 unit cubes in each of the 6 rows to read 6(3x + 4)!",
        ],
        "textbook_steps": "1. Find the GCF of the terms in 18x + 24: GCF(18, 24) = 6.\n2. Divide each term by the GCF: 18x ÷ 6 = 3x and 24 ÷ 6 = 4.\n3. Write the expression as a product of the GCF and the remaining sum: 6(3x + 4).",
        "problem_methods": ("Factoring Out Numerical GCF", "Factoring Algebraic Expressions", "Reverse Area Model (Width × Length)"),
    },

    # =========================================================================
    # UNIT 5: AREAS OF POLYGONS & ELAPSED TIME (Sections 5.1 - 5.4)
    # =========================================================================
    "5.1": {
        "unit_name": "Unit 5: Areas of Polygons & Elapsed Time",
        "big_ideas_method": "Parallelogram Cut-and-Slide Area Formula (A = b · h) Using Perpendicular Height",
        "block_steps": [
            "Open Kit COUNT-01 (Counting & Array Tiles) and build a parallelogram with base b = 12 and vertical height h = 8.",
            "Slice the right-triangle overhang off the left side and slide it to the right side—it forms a 12 × 8 rectangle!",
            "Multiply Base × Perpendicular Height: 12 × 8 = 96 cm² (ignore the 10 cm slanted side for area!).",
        ],
        "textbook_steps": "1. Identify the base b = 12 cm and the perpendicular height h = 8 cm (do NOT use the 10 cm slant side for area).\n2. Apply the Parallelogram Area Formula: A = b × h = 12 × 8 = 96 cm².\n3. Use the slanted side ONLY when finding Perimeter: P = 2(12 + 10) = 44 cm.",
        "problem_methods": ("Parallelogram Area (A = bh)", "Missing Base/Height (b = A ÷ h)", "Area vs. Perimeter & Frame Cutouts"),
    },
    "5.2": {
        "unit_name": "Unit 5: Areas of Polygons & Elapsed Time",
        "big_ideas_method": "Triangle Area as Half of a Parallelogram/Rectangle (A = ½ · b · h) & Double-Area Inverse",
        "block_steps": [
            "Open Kit COUNT-01 (Counting & Array Tiles) and build a 10 × 6 rectangle (Area = 60 unit squares).",
            "Cut the 10 × 6 rectangle diagonally from corner to corner into 2 congruent triangles.",
            "Each triangle has half the area of the rectangle: A = ½ × 10 × 6 = 30 cm².",
        ],
        "textbook_steps": "1. Identify the perpendicular base b = 10 cm and height h = 6 cm.\n2. Multiply base × height and divide by 2: A = ½ × 10 × 6 = 60 ÷ 2 = 30 cm².\n3. To find a missing base or height from Area, DOUBLE the area first (2A), then divide by the known dimension!",
        "problem_methods": ("Triangle Area (A = ½bh)", "Missing Base/Height (2A ÷ b)", "Right Triangle & Pennant Area"),
    },
    "5.3": {
        "unit_name": "Unit 5: Areas of Polygons & Elapsed Time",
        "big_ideas_method": "Trapezoid Area Formula A = ½h(b₁ + b₂) & Decomposing Composite Figures into Simple Chunks",
        "block_steps": [
            "Open Kit COUNT-01 (Counting & Array Tiles) and split the house wall into Chunk 1 (12 × 8 rectangle) and Chunk 2 (12 × 5 roof triangle).",
            "Compute Chunk 1 = 12 × 8 = 96 ft² and Chunk 2 = ½ × 12 × 5 = 30 ft².",
            "Add the non-overlapping chunks together (or accumulate with [Σ+]): 96 + 30 = 126 ft²!",
        ],
        "textbook_steps": "1. Composite Figures: Split the figure into rectangles and triangles, find each area (96 and 30), and add: 96 + 30 = 126 ft².\n2. Trapezoid Formula: Add the two parallel bases (b₁ + b₂), multiply by height h, and divide by 2: A = ½h(b₁ + b₂).\n3. Cutout Figures: Subtract the inner hole area from the outer rectangle area.",
        "problem_methods": ("Trapezoid Formula A = ½h(b₁+b₂)", "Composite Figure Decomposition", "Shaded Cutout & Multi-Chunk Area"),
    },
    "5.4": {
        "unit_name": "Unit 5: Areas of Polygons & Elapsed Time",
        "big_ideas_method": "Polygons in the Coordinate Plane (Side Lengths via Coordinates) & Base-60 Elapsed Time",
        "block_steps": [
            "Open Kit TIME-01 (Planetary Geared Clock) and COUNT-01 (Gridfinity Baseplate).",
            "On the grid, plot (2, 3), (9, 3), (9, 8), and (2, 8): count horizontal width 9 - 2 = 7 and vertical height 8 - 3 = 5 (Area = 35).",
            "On the Planetary Clock, dial 1 hr 45 min and advance 50 min—the 12:1 planetary gears carry 60 min into +1 hr automatically (2 hr 35 min)!",
        ],
        "textbook_steps": "1. Coordinate Polygon: Subtract x-coordinates for horizontal width (9 - 2 = 7) and y-coordinates for vertical height (8 - 3 = 5).\n2. Compute Perimeter = 2(7 + 5) = 24 units and Area = 7 × 5 = 35 sq units.\n3. Base-60 Time: Regroup every 60 minutes into 1 hour (45 min + 50 min = 95 min = 1 hr 35 min).",
        "problem_methods": ("Coordinate Polygon Side Lengths", "Base-60 Elapsed Time Regrouping", "Grid Area & Time Addition/Subtraction"),
    },

    # =========================================================================
    # UNIT 6: INTEGERS, RATIONAL NUMBERS & THE COORDINATE PLANE (Sections 6.1 - 6.5)
    # =========================================================================
    "6.1": {
        "unit_name": "Unit 6: Integers, Rational Numbers & Coordinate Plane",
        "big_ideas_method": "Positive & Negative Integers on a Number Line, Zero Pairs & Opposites Across 0",
        "block_steps": [
            "Open Kit BASE-10 / RACK-01 and set the center line as Zero (0 / Sea Level).",
            "Place 15 negative counters (-15) on the left side and 15 positive counters (+15) on the right side.",
            "Combine -15 and +15 into 15 Zero Pairs—every (+1, -1) pair cancels to 0, proving -15 and +15 are opposites!",
        ],
        "textbook_steps": "1. Positive (+) integers represent gains/above 0; negative (-) integers represent losses/below 0; 0 is neither positive nor negative.\n2. Two numbers the same distance from 0 on opposite sides are Opposites (-15 and +15), and their sum is 0.\n3. The opposite of the opposite of a number returns to the original number: -(-15) = +15.",
        "problem_methods": ("Real-World Integer Sign", "Opposites & -(-x) Double Flip", "Zero-Reference Modeling"),
    },
    "6.2": {
        "unit_name": "Unit 6: Integers, Rational Numbers & Coordinate Plane",
        "big_ideas_method": "Comparing & Ordering Integers, Decimals, and Fractions on a Number Line",
        "block_steps": [
            "Open Kit RACK-01 (Number Rack) and mark 0 at the center, with negative numbers going left and positive going right.",
            "Locate -5 (5 steps left of 0) and -18 (18 steps left of 0).",
            "Apply the Number Line Rule: further RIGHT (closer to 0 for negatives) is ALWAYS greater, so -5 > -18!",
        ],
        "textbook_steps": "1. Plot -5 and -18 on a horizontal number line.\n2. Because -5 is to the right of -18 (warmer / closer to 0), -5 is greater than -18 (-5 > -18).\n3. For negative fractions/decimals (e.g., -3/4 = -0.75 vs. -1/2 = -0.50), -0.50 is further right, so -1/2 > -3/4.",
        "problem_methods": ("Number Line Inequality (< or >)", "Comparing Negative Fractions/Decimals", "Ordering Least to Greatest"),
    },
    "6.3": {
        "unit_name": "Unit 6: Integers, Rational Numbers & Coordinate Plane",
        "big_ideas_method": "Absolute Value |x| as Distance from Zero (Always Non-Negative) & Evaluating |x| Expressions",
        "block_steps": [
            "Open Kit RACK-01 (Number Rack) and place a marker at -14 (14 beads left of 0) and +14 (14 beads right of 0).",
            "Count the physical distance from 0 to each marker: both are 14 steps from 0, so |-14| = 14 and |14| = 14.",
            "For -|-14|, first find the distance |-14| = 14, then apply the outside negative sign to get -14.",
        ],
        "textbook_steps": "1. Absolute value |x| is the distance between x and 0 on a number line, so |x| ≥ 0 always: |-14| = 14 and |14| = 14.\n2. Evaluate inside absolute value bars first (like parentheses): |-27| + |13| = 27 + 13 = 40.\n3. An outside negative sign applies after taking the absolute value: -|-14| = -14.",
        "problem_methods": ("Distance from Zero |x|", "Absolute Value Expressions", "Magnitude (Debt/Depth) vs. Value"),
    },
    "6.4": {
        "unit_name": "Unit 6: Integers, Rational Numbers & Coordinate Plane",
        "big_ideas_method": "Plotting (x, y) in All Four Quadrants (I, II, III, IV) & Reflecting Across the x- and y-Axes",
        "block_steps": [
            "Open Kit COUNT-01 (4x4 Gridfinity Baseplate) and divide the grid into 4 quadrants around the center origin (0, 0).",
            "Use the Elevator Rule for (x, y): walk ACROSS the x-axis first (+ right, - left), then ride UP/DOWN the y-axis (+ up, - down).",
            "Reflect across the x-axis by flipping the y-sign (x, -y); reflect across the y-axis by flipping the x-sign (-x, y).",
        ],
        "textbook_steps": "1. Check coordinate signs: A(-6, 5) is (-, +) -> Quadrant II; B(4, -7) is (+, -) -> Quadrant IV; C(-3, -8) is (-, -) -> Quadrant III.\n2. Reflection across x-axis: keep x, flip y.\n3. Reflection across y-axis: flip x, keep y.",
        "problem_methods": ("Quadrant Identification (I–IV)", "x-Axis & y-Axis Reflections", "Coordinate Grid Navigation"),
    },
    "6.5": {
        "unit_name": "Unit 6: Integers, Rational Numbers & Coordinate Plane",
        "big_ideas_method": "Finding Horizontal & Vertical Distances on the Coordinate Plane Using Absolute Value",
        "block_steps": [
            "Open Kit COUNT-01 / RACK-01 and snap tiles at (-6, 4) in Quadrant II and (9, 4) in Quadrant I.",
            "Count the steps from (-6, 4) to the y-axis (|-6| = 6 steps) plus the steps from the y-axis to (9, 4) (|9| = 9 steps).",
            "Add the distances across the axis: 6 + 9 = 15 units (or subtract coordinates and take absolute value: |-6 - 9| = 15).",
        ],
        "textbook_steps": "1. Different Quadrants (points cross an axis, like -6 and 9): Add absolute values: |-6| + |9| = 6 + 9 = 15 units.\n2. Same Quadrant (points on same side of axis, like -12 and -4): Subtract absolute values: |-12| - |-4| = 12 - 4 = 8 units.\n3. Universal Formula: Distance = |x₁ - x₂| (or |y₁ - y₂|).",
        "problem_methods": ("Cross-Axis / Same-Quadrant Distance", "Decimal & Fraction Coordinates", "Coordinate Rectangle Perimeter/Area"),
    },

    # =========================================================================
    # UNIT 7: EQUATIONS & INEQUALITIES (Sections 7.1 - 7.5)
    # =========================================================================
    "7.1": {
        "unit_name": "Unit 7: Equations & Inequalities",
        "big_ideas_method": "Writing Equations in One Variable & Testing Solutions by Substitution (Balance Scale Rule)",
        "block_steps": [
            "Open Kit ALGB-01 (Algebra Boxes & Stage) and set the Balance Scale pivot (=) between the Left Pan and Right Pan.",
            "Place 4 x-rods and 5 unit cubes on the Left Pan (4x + 5) and 41 unit cubes on the Right Pan.",
            "Substitute x = 9 into each x-rod: 4(9) + 5 = 36 + 5 = 41, matching the Right Pan (41 = 41, Balanced!).",
        ],
        "textbook_steps": "1. Test x = 7 in 4x + 5 = 41: 4(7) + 5 = 28 + 5 = 33 ≠ 41 (Not a solution).\n2. Test x = 9 in 4x + 5 = 41: 4(9) + 5 = 36 + 5 = 41 = 41 (True! x = 9 is the solution).\n3. When translating phrases, watch turnaround words: '8 less than n is 25' is n - 8 = 25.",
        "problem_methods": ("Substitution Solution Test", "Translating Verbal Equations", "Real-World Equation Modeling"),
    },
    "7.2": {
        "unit_name": "Unit 7: Equations & Inequalities",
        "big_ideas_method": "Subtraction & Addition Properties of Equality (Inverse Operations on Both Sides)",
        "block_steps": [
            "Open Kit ALGB-01 (Algebra Boxes & Stage) and place 1 x-rod + 28 unit cubes on the Left Pan and 73 cubes on the Right Pan.",
            "Remove 28 unit cubes from BOTH pans to keep the scale balanced: 73 - 28 = 45 cubes remain.",
            "Read the isolated x-rod value: x = 45, and check by adding 28 back: 45 + 28 = 73!",
        ],
        "textbook_steps": "1. Identify the operation on the variable in x + 28 = 73: addition (+ 28).\n2. Apply the Subtraction Property of Equality (subtract 28 from both sides): x = 73 - 28 = 45.\n3. Check by substituting x = 45 into the original equation: 45 + 28 = 73.",
        "problem_methods": ("Subtraction Property of Equality", "Addition Property of Equality", "1-Step Inverse Equation & Check"),
    },
    "7.3": {
        "unit_name": "Unit 7: Equations & Inequalities",
        "big_ideas_method": "Division & Multiplication Properties of Equality & Reciprocal Multiplication for Fractional Coefficients",
        "block_steps": [
            "Open Kit ALGB-01 (Algebra Boxes & Stage) and place 8 green x-rods on the Left Pan and 136 unit cubes on the Right Pan (8x = 136).",
            "Divide the 136 cubes equally among the 8 x-rods: 136 ÷ 8 = 17 cubes per x-rod (x = 17).",
            "For k / 7 = 14.5 (1 seventh of k is 14.5), combine 7 equal parts: k = 14.5 × 7 = 101.5.",
        ],
        "textbook_steps": "1. To solve 8x = 136, use the Division Property of Equality (divide both sides by 8): x = 136 ÷ 8 = 17.\n2. To solve k / 7 = 14.5, use the Multiplication Property of Equality (multiply both sides by 7): k = 14.5 × 7 = 101.5.\n3. For fractional coefficients like (3/4)x = 18, multiply both sides by the reciprocal 4/3: x = 24.",
        "problem_methods": ("Division / Multiplication Property", "Reciprocal Coefficient Solver", "Rate & Geometry Formula Equation"),
    },
    "7.4": {
        "unit_name": "Unit 7: Equations & Inequalities",
        "big_ideas_method": "Writing, Graphing & Solving 1-Step Inequalities (Open Circle <, > vs. Solid Circle ≤, ≥)",
        "block_steps": [
            "Open Kit RACK-01 (Number Rack) and solve x - 7 ≥ 12 by adding 7 to both sides -> boundary at x = 19.",
            "Place a SOLID cap at 19 because ≥ includes 19 ('greater than or equal to'), and slide beads to the right (20, 21, ...).",
            "Test x = 20 in the original inequality: 20 - 7 = 13 ≥ 12 (True!).",
        ],
        "textbook_steps": "1. Solve x - 7 ≥ 12 using the Addition Property of Inequality (add 7 to both sides): x ≥ 19.\n2. Graph on a number line: use a SOLID circle (●) at 19 for ≥ or ≤ (use an OPEN circle ○ for > or <) and shade right.\n3. Test a number in the shaded region: for x = 20, 20 - 7 = 13 ≥ 12 (True).",
        "problem_methods": ("Inequality Phrase & Solution Test", "Open (○) vs. Solid (●) Graph", "Solving 1-Step Inequalities"),
    },
    "7.5": {
        "unit_name": "Unit 7: Equations & Inequalities",
        "big_ideas_method": "Independent (Input x) & Dependent (Output y) Variables — Multiplicative (y = kx) vs. Additive (y = x + b)",
        "block_steps": [
            "Open Kit COUNT-01 (Counting & Array Tiles) and compare the Input x and Output y columns for Table A and Table B.",
            "In Table A ((2, 14), (5, 35), (8, 56)), every Output y is 7 groups of x (y ÷ x = 7) -> Multiplicative rule y = 7x.",
            "In Table B ((10, 6), (15, 11), (22, 18)), every Output y is 4 tiles less than x (y - x = -4) -> Additive rule y = x - 4.",
        ],
        "textbook_steps": "1. Test for a Multiplicative Rule (y = kx): Divide y ÷ x for each pair: 14÷2 = 7, 35÷5 = 7, 56÷8 = 7 -> y = 7x.\n2. Test for an Additive Rule (y = x + b): Subtract y - x for each pair: 6-10 = -4, 11-15 = -4 -> y = x - 4.\n3. The Independent Variable is the input x; the Dependent Variable is the output y.",
        "problem_methods": ("Multiplicative (y = kx) vs. Additive", "Independent & Dependent Variables", "Two-Variable Rule & Prediction"),
    },

    # =========================================================================
    # UNIT 8: SURFACE AREA & VOLUME OF 3D SOLIDS (Sections 8.1 - 8.4)
    # =========================================================================
    "8.1": {
        "unit_name": "Unit 8: Surface Area & Volume of 3D Solids",
        "big_ideas_method": "Unfolding 3D Prisms into 2D Nets — Sum of 6 Rectangular Faces SA = 2(lw + lh + wh)",
        "block_steps": [
            "Open Kit COUNT-01 and inspect a rectangular prism measuring l = 8 cm, w = 5 cm, and h = 3 cm.",
            "Unfold its 6 faces into 3 congruent pairs: Top/Bottom (8 × 5 = 40 each), Front/Back (8 × 3 = 24 each), Left/Right (5 × 3 = 15 each).",
            "Sum the 3 distinct face areas (40 + 24 + 15 = 79 cm²) and double for the 3 opposite pairs: 2 × 79 = 158 cm²!",
        ],
        "textbook_steps": "1. Find the area of the 3 distinct face pairs: Bottom/Top = 8×5 = 40; Front/Back = 8×3 = 24; Sides = 5×3 = 15.\n2. Add the 3 areas together: 40 + 24 + 15 = 79 cm².\n3. Multiply by 2 to include all 6 faces: SA = 2 × 79 = 158 cm² (for a cube of edge s, SA = 6s²).",
        "problem_methods": ("Rectangular Prism Net SA = 2(lw+lh+wh)", "Cube SA (6s²) & Open-Top Box", "3D Solid Vertices, Edges & Faces"),
    },
    "8.2": {
        "unit_name": "Unit 8: Surface Area & Volume of 3D Solids",
        "big_ideas_method": "2D Nets of Triangular Prisms (2 Triangles + 3 Rectangles) & Square Pyramids (1 Base + 4 Triangles)",
        "block_steps": [
            "Open Kit COUNT-01 and unfold the Square Pyramid net flat onto the desk: 1 square base (10 × 10) surrounded by 4 triangles.",
            "Compute the square base area: 10 × 10 = 100 m².",
            "Compute 1 triangular face using slant height l = 12: ½ × 10 × 12 = 60 m², then add all 4 triangles: 100 + 4(60) = 340 m²!",
        ],
        "textbook_steps": "1. Square Base Area: B = 10 × 10 = 100 m².\n2. Area of 1 Triangular Face (using slant height l = 12 m): A = ½ × 10 × 12 = 60 m².\n3. Total Pyramid Surface Area: Base + 4 Triangles = 100 + 4(60) = 100 + 240 = 340 m².",
        "problem_methods": ("Square Pyramid Net (B + 4 Triangles)", "Triangular Prism Net (2 Tri + 3 Rect)", "Lateral vs. Total Surface Area"),
    },
    "8.3": {
        "unit_name": "Unit 8: Surface Area & Volume of 3D Solids",
        "big_ideas_method": "Base-Layer Volume Stacking (V = B · h = l · w · h) with Whole, Fractional & Decimal Edges",
        "block_steps": [
            "Open Kit COUNT-01 / FRAC-01 and build the bottom layer of a 12 in × 8 in crate: Base Area B = 12 × 8 = 96 unit cubes.",
            "Stack h = 5 identical layers high to find the total volume: V = 96 × 5 = 480 in³.",
            "For fractional edges (3 1/2 × 1 1/2 × 2), multiply the improper fractions: (7/2) × (3/2) × 2 = 21/2 = 10 1/2 ft³.",
        ],
        "textbook_steps": "1. Whole-Edge Crate: Multiply length × width × height: V = 12 × 8 × 5 = 480 in³.\n2. Fractional-Edge Aquarium: Convert to improper fractions and multiply: (7/2) × (3/2) × 2 = 10 1/2 ft³ (10.5 ft³).\n3. Missing Height/Depth: Divide Volume by Base Area (l × w): h = V ÷ (l × w).",
        "problem_methods": ("Prism Volume (V = l × w × h)", "Fractional Edge & Unit-Cube Packing", "Missing Height (h = V ÷ Base Area)"),
    },
    "8.4": {
        "unit_name": "Unit 8: Surface Area & Volume of 3D Solids",
        "big_ideas_method": "Circle Area (A = πr²) & Circumference (C = 2πr), Cone Volume (V = ⅓πr²h) & Right-Triangle Hypotenuse",
        "block_steps": [
            "Open Kit COUNT-01 / PROB-01 and place a circle of radius r = 6 inside a 2r × 2r square: Area = π × 6² ≈ 113.10 in².",
            "Compare a Cone to a Cylinder of the same radius and height: exactly 3 cones fill 1 cylinder (V = ⅓πr²h).",
            "Build squares on the legs of a 12 × 5 right triangle: 12² + 5² = 144 + 25 = 169, and √169 = 13 ft!",
        ],
        "textbook_steps": "1. Circle Area (r = 6): A = πr² = π × 36 ≈ 113.10 in² (Circumference C = 2πr = 12π ≈ 37.70 in).\n2. Right-Triangle Hypotenuse (a = 12, b = 5): c = √(12² + 5²) = √(144 + 25) = √169 = 13 ft.\n3. Cone Volume: V = ⅓ × π × r² × h.",
        "problem_methods": ("Circle Area (πr²) & Circumference", "Cone Volume & 3-4-5 / 5-12-13 Triangles", "Composite Semi-Circle & Ramp"),
    },

    # =========================================================================
    # UNIT 9: STATISTICAL MEASURES & DATA DISPLAYS (Sections 9.1 - 9.4)
    # =========================================================================
    "9.1": {
        "unit_name": "Unit 9: Statistical Measures & Data Displays",
        "big_ideas_method": "Statistical Questions, Dot Plot Frequencies & Fair-Share Leveling for the Mean (x̄ = Σx ÷ n)",
        "block_steps": [
            "Open Kit COUNT-01 (Counting & Array Tiles) and build 5 towers for the data values 18, 24, 15, 27, and 21.",
            "Move top tiles from the taller towers (27 and 24) to the shorter towers (15 and 18) until all 5 towers are level.",
            "All 5 leveled towers stand 21 tiles high—proving Sum Σx = 105, Count n = 5, and Fair-Share Mean x̄ = 105 ÷ 5 = 21!",
        ],
        "textbook_steps": "1. Add all data values to find the sum: Σx = 18 + 24 + 15 + 27 + 21 = 105.\n2. Count the number of values in the data set: n = 5.\n3. Divide the sum by the count: Mean x̄ = 105 ÷ 5 = 21.",
        "problem_methods": ("Fair-Share Mean (Σx ÷ n)", "Dot Plot Peak, Cluster & Gap", "Missing Target Score via Total Sum"),
    },
    "9.2": {
        "unit_name": "Unit 9: Statistical Measures & Data Displays",
        "big_ideas_method": "Ordering Data Least-to-Greatest for Median (Middle), Mode (Most Frequent), Range & Outlier Effect",
        "block_steps": [
            "Open Kit PROB-01 / COUNT-01 and line up the 8 shoe sizes in order from least to greatest: 6, 7, 7, 7, 8, 9, 9, 10.",
            "Find the middle pair (4th and 5th values: 7 and 8) and average them for the Median: (7 + 8) ÷ 2 = 7.5.",
            "Count the tallest frequency stack for the Mode (7 appears three times) and subtract Max - Min = 10 - 6 = 4 for Range.",
        ],
        "textbook_steps": "1. Order data from least to greatest: 6, 7, 7, 7, 8, 9, 9, 10 (n = 8).\n2. Median (average of two middle values): (7 + 8) ÷ 2 = 7.5. Mode (most frequent): 7. Mean: 63 ÷ 8 = 7.875.\n3. Range: Max - Min = 10 - 6 = 4 (when an extreme outlier is present, the Median is the best measure of center).",
        "problem_methods": ("Ordered Median, Mode & Range", "Even-Count Median & Outlier Impact", "Choosing Best Measure of Center"),
    },
    "9.3": {
        "unit_name": "Unit 9: Statistical Measures & Data Displays",
        "big_ideas_method": "5-Number Summary (Min, Q₁, Med, Q₃, Max), Interquartile Range (IQR = Q₃ - Q₁) & Box-and-Whisker Plots",
        "block_steps": [
            "Open Kit FRAC-01 / COUNT-01 and lay out the 9 ordered scores: 68, 72, 75, 78, [82], 85, 88, 92, 96.",
            "The middle (5th) score is Median = 82, splitting the remaining scores into a lower half of 4 and upper half of 4.",
            "Average the middle two of the lower half for Q₁ = (72+75)/2 = 73.5 and upper half for Q₃ = (88+92)/2 = 90 -> IQR = 90 - 73.5 = 16.5!",
        ],
        "textbook_steps": "1. Order the 9 values and identify Min = 68, Median (5th value) = 82, and Max = 96.\n2. Find Q₁ (median of lower 4 values: 68, 72, 75, 78) = 73.5, and Q₃ (median of upper 4: 85, 88, 92, 96) = 90.\n3. Compute Interquartile Range (middle 50% box width): IQR = Q₃ - Q₁ = 90 - 73.5 = 16.5.",
        "problem_methods": ("5-Number Summary & Quartiles", "Interquartile Range (IQR = Q₃ - Q₁)", "Box Plot 25% Quartile Sections"),
    },
    "9.4": {
        "unit_name": "Unit 9: Statistical Measures & Data Displays",
        "big_ideas_method": "Mean Absolute Deviation (MAD) — Average Distance of Data Values from the Mean",
        "block_steps": [
            "Open Kit COUNT-01 (Counting & Array Tiles) and build towers for 10, 12, 14, 16, 18 with the Mean line at x̄ = 14.",
            "Measure each tower's distance |x - 14| from the Mean line: 4, 2, 0, 2, and 4 tiles.",
            "Divide the total distance (4 + 2 + 0 + 2 + 4 = 12) by 5 towers to get MAD = 12 ÷ 5 = 2.4!",
        ],
        "textbook_steps": "1. Step 1 (Mean): Find the mean of 10, 12, 14, 16, 18 -> x̄ = 70 ÷ 5 = 14.\n2. Step 2 (Absolute Deviations): Find each distance from 14: |10-14|=4, |12-14|=2, |14-14|=0, |16-14|=2, |18-14|=4.\n3. Step 3 (Average of Distances): MAD = (4 + 2 + 0 + 2 + 4) ÷ 5 = 12 ÷ 5 = 2.4.",
        "problem_methods": ("3-Step MAD Calculation", "Deviation Distances from Mean", "Comparing MAD Consistency"),
    },

    # =========================================================================
    # UNIT 10: GRADE 7 BRIDGE — SIGNED RATIONALS, 2-STEP EQUATIONS & PROBABILITY (Sections 10.1 - 10.4)
    # =========================================================================
    "10.1": {
        "unit_name": "Unit 10: Grade 7 Bridge — Signed Rationals, 2-Step Equations & Probability",
        "big_ideas_method": "Zero-Pair Counter Cancellation & Add-the-Opposite Rule for Subtraction (a - b = a + (-b))",
        "block_steps": [
            "Open Kit BASE-10 (Ten-Frame Zero-Pair Counters) and place 8 red negative counters (-8) and 5 yellow positive counters (+5).",
            "Pair 5 red and 5 yellow counters into 5 Zero Pairs (each pair = 0) and remove them—3 red counters (-3) remain!",
            "For -6 + (-4), both sets are red negative counters, so no zero pairs form: combine 6 red + 4 red = 10 red (-10).",
        ],
        "textbook_steps": "1. Different Signs (-8 + 5): Subtract absolute values (8 - 5 = 3) and keep the sign of the larger absolute value -> -3.\n2. Same Signs (-6 + (-4)): Add absolute values (6 + 4 = 10) and keep the common sign -> -10.\n3. Subtracting Signed Numbers (a - b): Add the opposite: a + (-b) (so subtracting a negative adds a positive!).",
        "problem_methods": ("Zero-Pair Signed Addition", "Add-the-Opposite Subtraction", "Signed Fractions, Decimals & Change"),
    },
    "10.2": {
        "unit_name": "Unit 10: Grade 7 Bridge — Signed Rationals, 2-Step Equations & Probability",
        "big_ideas_method": "Sign Rules for Multiplying & Dividing Rational Numbers (Same Signs = +, Different Signs = -)",
        "block_steps": [
            "Open Kit BASE-10 (Ten-Frame Counters) and model 6 × (-4) as 6 groups of 4 red negative counters = -24.",
            "Treat a negative multiplier as 'Flip the Sign': (-6) × (-4) flips the 24 red counters over to 24 yellow positive counters (+24).",
            "For (-5)², multiply (-5) × (-5) -> 2 negatives flip to positive +25!",
        ],
        "textbook_steps": "1. Different Signs -> Negative (-): 6 × (-4) = -24.\n2. Same Signs -> Positive (+): (-6) × (-4) = +24 and (-5)² = (-5) × (-5) = +25.\n3. Multi-Factor Sign Rule: An EVEN number of negative factors gives (+); an ODD number of negative factors gives (-).",
        "problem_methods": ("Same/Different Sign Rules", "Signed Powers & Rational Products", "Multi-Factor Sign Counting"),
    },
    "10.3": {
        "unit_name": "Unit 10: Grade 7 Bridge — Signed Rationals, 2-Step Equations & Probability",
        "big_ideas_method": "Solving Two-Step Equations (ax + b = c) by Undoing Addition/Subtraction First, Then Multiplication/Division",
        "block_steps": [
            "Open Kit ALGB-01 (Algebra Boxes & Stage) and place 3 x-rods + 7 unit cubes on the Left Pan and 28 cubes on the Right Pan (3x + 7 = 28).",
            "Step 1 (Undo + 7): Remove 7 unit cubes from BOTH pans so the 3 x-rods equal 28 - 7 = 21 cubes (3x = 21).",
            "Step 2 (Undo × 3): Divide the 21 cubes equally across the 3 x-rods: 21 ÷ 3 = 7 cubes per x-rod (x = 7).",
        ],
        "textbook_steps": "1. Step 1 (Undo Addition or Subtraction): Subtract 7 from both sides of 3x + 7 = 28 -> 3x = 21.\n2. Step 2 (Undo Multiplication or Division): Divide both sides by 3 -> x = 21 ÷ 3 = 7.\n3. Check by substituting x = 7 back into the original equation: 3(7) + 7 = 21 + 7 = 28.",
        "problem_methods": ("2-Step Inverse Unwrapping", "Fractional & Negative Coefficients", "2-Step Word Problem Modeling"),
    },
    "10.4": {
        "unit_name": "Unit 10: Grade 7 Bridge — Signed Rationals, 2-Step Equations & Probability",
        "big_ideas_method": "Theoretical Probability P(E) = Favorable / Total, Complement P(not E), Factorials (n!) & Combinations (nCr)",
        "block_steps": [
            "Open Kit PROB-01 (Probability Studio) and inspect the 10-sector spinner (4 Blue, 3 Gold, 3 Red sectors).",
            "Count the 4 favorable Blue sectors out of 10 total sectors: P(Blue) = 4/10 = 2/5 = 0.4 = 40%.",
            "Line up 5 physical blocks to count permutations: 5 choices for spot 1 × 4 × 3 × 2 × 1 = 5! = 120 ways!",
        ],
        "textbook_steps": "1. Theoretical Probability: P(Blue) = Favorable / Total = 4/10 = 2/5 (simplified fraction) = 0.4 (decimal) = 40% (percent).\n2. Permutations of n items (order matters): n! = 5 × 4 × 3 × 2 × 1 = 120 ways (or nPr for choosing r in order).\n3. Combinations (order does NOT matter, like choosing a team): use nCr.",
        "problem_methods": ("Theoretical Probability & Complement", "Factorials (n!) & Permutations (nPr)", "Combinations (nCr) vs. Permutations"),
    },
}
