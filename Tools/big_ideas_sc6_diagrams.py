#!/usr/bin/env python3
"""
Full-Width Textbook Concept & Hands-On Block Diagrams for all 45 Sections (1.1–10.4)
of the Big Ideas Math Middle School Supplement Workbook.

Each diagram is drawn in an 86 mm × 25 mm canvas box on Practice A and illustrates:
  1. The authentic Big Ideas Math textbook visual model (e.g., Venn Diagram, Factor Tree +
     Division Ladder, Long Division Bracket, PEMDAS Funnel, Fraction Strip LCD, 2D Fraction
     Area Grid, Double Number Line, Ratio Table, Cut-and-Slide Parallelogram, Box-and-Whisker
     Plot, MAD Deviation Line, Balance Scale, 2D Surface Area Net, etc.).
  2. How the physical StackCalc blocks reinforce that exact textbook concept (only in the
     sections where blocks naturally apply).
"""

from __future__ import annotations

import math
from typing import Any, Dict

INK = "#0F172A"
SLATE = "#334155"
MUTED = "#64748B"
BORDER = "#94A3B8"
LIGHT_BORDER = "#CBD5E1"
SUBTLE_HDR = "#F8FAFC"
WHITE = "#FFFFFF"
TEAL = "#0D5573"
BLUE_FILL = "#DBEAFE"
GREEN_FILL = "#DCFCE7"
GOLD_FILL = "#FEF3C7"
RED_FILL = "#FEE2E2"
PURPLE_FILL = "#F3E8FF"
GRAY_FILL = "#E2E8F0"


def draw_section_concept_diagram(
    p: Any,
    sec_num: str,
    sec: Dict[str, Any],
    ped: Dict[str, Any],
    x: float,
    y: float,
    w: float,
    h: float,
) -> None:
    """Draws a full-width (86 mm × 25 mm) section-specific textbook & block concept diagram."""
    p.rect(x, y, w, h, fill=WHITE, stroke=LIGHT_BORDER, r=0.9, line_w=0.25)
    mid_x = x + w / 2.0

    # =========================================================================
    # UNIT 1: NUMERICAL EXPRESSIONS & FACTORS (1.1 - 1.5)
    # =========================================================================
    if sec_num == "1.1":
        # Left: Textbook Long Division 23 ÷ 4 = 5 R 3
        p.text(x + 21.0, y + 3.1, "Way 1: Long Division (23 ÷ 4)", size=1.72, bold=True, color=INK, align="center")
        lx, ly = x + 8.5, y + 6.8
        p.text(lx + 7.5, ly - 0.8, "5  R 3", size=1.95, bold=True, mono=True, color=TEAL)
        p.text(lx, ly + 2.4, "4", size=2.0, bold=True, mono=True, color=INK)
        p.line(lx + 3.2, ly - 0.2, lx + 3.2, ly + 3.2, color=INK, width=0.32)
        p.line(lx + 3.2, ly - 0.2, lx + 16.5, ly - 0.2, color=INK, width=0.32)
        p.text(lx + 5.0, ly + 2.4, "23", size=2.0, bold=True, mono=True, color=INK)
        p.text(lx + 3.6, ly + 5.4, "-20", size=1.85, mono=True, color=SLATE)
        p.text(lx + 14.5, ly + 5.4, "(5×4)", size=1.55, mono=True, color=MUTED)
        p.line(lx + 3.6, ly + 6.2, lx + 12.0, ly + 6.2, color=INK, width=0.25)
        p.text(lx + 6.8, ly + 8.9, "3", size=1.95, bold=True, mono=True, color=TEAL)
        p.text(lx + 13.5, ly + 8.9, "(Rem < 4)", size=1.5, bold=True, color=SLATE)
        p.text(x + 21.0, y + h - 1.6, "Check: (5 × 4) + 3 = 23", size=1.65, bold=True, mono=True, color=INK, align="center")

        p.line(mid_x - 1.0, y + 1.5, mid_x - 1.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        # Right: Equal-Groups Array (5 rows of 4 + 3 leftover units)
        p.text(mid_x + 21.5, y + 3.1, "Equal-Groups Array: 5 Rows of 4 + 3", size=1.72, bold=True, color=TEAL, align="center")
        gx, gy = mid_x + 4.5, y + 4.8
        ts, gap = 2.7, 0.35
        for r in range(5):
            for c in range(4):
                p.rect(gx + c * (ts + gap), gy + r * (ts + gap), ts, ts, fill=BLUE_FILL, stroke=INK, r=0.35, line_w=0.2)
        p.text(gx + 6.0, y + h - 1.6, "5 Full Groups (20)", size=1.58, bold=True, color=INK, align="center")
        rx = gx + 4 * (ts + gap) + 4.8
        for rem_i in range(3):
            p.rect(rx, gy + (2 + rem_i) * (ts + gap), ts, ts, fill=GOLD_FILL, stroke=INK, r=0.35, line_w=0.22)
        p.text(rx + 1.35, gy + 4.2, "+3 Left", size=1.6, bold=True, color=SLATE, align="center")
        p.text(rx + 1.35, y + h - 1.6, "Rem = 3", size=1.58, bold=True, color=TEAL, align="center")

    elif sec_num == "1.2":
        # Left: Textbook Power Anatomy (4² = 4 × 4 = 16)
        p.text(x + 20.0, y + 3.1, "Power: Base × Base (Repeated Factor)", size=1.68, bold=True, color=INK, align="center")
        p.rect(x + 3.0, y + 5.2, 34.0, 11.2, fill=SUBTLE_HDR, stroke=BORDER, r=0.6, line_w=0.22)
        p.text(x + 8.5, y + 12.2, "4", size=4.2, bold=True, mono=True, color=INK)
        p.text(x + 12.2, y + 9.4, "2", size=2.4, bold=True, mono=True, color=TEAL)
        p.text(x + 16.5, y + 11.8, "= 4 × 4 = 16", size=2.05, bold=True, mono=True, color=INK)
        p.text(x + 8.5, y + 15.2, "Base", size=1.45, bold=True, color=SLATE, align="center")
        p.text(x + 13.5, y + 6.8, "Exponent (2 factors)", size=1.42, bold=True, color=TEAL)
        p.text(x + 20.0, y + h - 2.0, "Watch Out: 4² = 16 (NEVER 4×2 = 8!)", size=1.6, bold=True, color=TEAL, align="center")

        p.line(mid_x - 2.5, y + 1.5, mid_x - 2.5, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        # Right: 4×4 Square Array (16 units) vs 4×2 Array (8 units)
        p.text(mid_x + 20.0, y + 3.1, "Prime & Square Model: 4² (16) vs. 4×2 (8)", size=1.68, bold=True, color=TEAL, align="center")
        gx, gy = mid_x + 2.0, y + 5.0
        ts, gap = 3.0, 0.35
        for r in range(4):
            for c in range(4):
                p.rect(gx + c * (ts + gap), gy + r * (ts + gap), ts, ts, fill=BLUE_FILL, stroke=INK, r=0.3, line_w=0.2)
        p.text(gx + 6.5, y + h - 1.8, "4² = 4×4 = 16", size=1.62, bold=True, mono=True, color=INK, align="center")

        wx = gx + 4 * (ts + gap) + 5.5
        for r in range(2):
            for c in range(4):
                p.rect(wx + c * (ts + gap), gy + 3.2 + r * (ts + gap), ts, ts, fill=RED_FILL, stroke=SLATE, r=0.3, line_w=0.2)
        p.text(wx + 6.5, gy + 2.0, "4 × 2 = 8", size=1.6, bold=True, mono=True, color=SLATE, align="center")
        p.text(wx + 6.5, y + h - 1.8, "(Not a Square!)", size=1.52, bold=True, color=MUTED, align="center")

    elif sec_num == "1.3":
        # Textbook Order of Operations (PEMDAS) Step-by-Step Funnel for (8 + 4) × (9 - 3) = 72
        p.text(x + 26.0, y + 3.1, "Textbook PEMDAS Funnel: (8 + 4) × (9 - 3)", size=1.68, bold=True, color=INK, align="center")
        fx = x + 26.0
        p.text(fx, y + 6.8, "(8 + 4) × (9 - 3)", size=2.0, bold=True, mono=True, color=INK, align="center")
        p.line(fx - 14.0, y + 7.5, fx + 14.0, y + 7.5, color=LIGHT_BORDER, width=0.2)
        p.text(fx, y + 10.6, "= 12 × (9 - 3)   [1st ( )]", size=1.82, bold=True, mono=True, color=TEAL, align="center")
        p.text(fx, y + 14.2, "= 12 × 6         [2nd ( )]", size=1.82, bold=True, mono=True, color=INK, align="center")
        p.text(fx, y + 17.8, "Way 2: 8(6) + 4(6) = 48 + 24", size=1.62, bold=True, mono=True, color=SLATE, align="center")
        p.rect(fx - 9.0, y + 19.2, 18.0, 4.0, fill=GREEN_FILL, stroke=INK, r=0.5, line_w=0.22)
        p.text(fx, y + 21.9, "= 72", size=2.05, bold=True, mono=True, color=INK, align="center")

        p.line(x + 51.0, y + 1.5, x + 51.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)
        rx = x + 53.0
        rules = [
            ("1. ( ) [ ]", "Grouping Symbols"),
            ("2. b^n", "Exponents / Powers"),
            ("3. × and ÷", "Left -> Right (Equal!)"),
            ("4. + and -", "Left -> Right (Equal!)"),
        ]
        p.text(rx + 15.0, y + 3.1, "PEMDAS Priority Checklist", size=1.68, bold=True, color=TEAL, align="center")
        for idx, (rk, rv) in enumerate(rules):
            ry = y + 5.2 + idx * 4.5
            p.rect(rx, ry, 30.5, 3.9, fill=BLUE_FILL if idx == 2 else SUBTLE_HDR, stroke=BORDER, r=0.4, line_w=0.18)
            p.text(rx + 1.2, ry + 2.6, rk, size=1.6, bold=True, mono=True, color=INK)
            p.text(rx + 11.2, ry + 2.6, rv, size=1.52, color=SLATE)

    elif sec_num == "1.4":
        # 3 Ways for Prime Factorization of 60: Way 1 Factor Tree | Way 2 Division Ladder | Way 3 Prime Blocks
        w3 = w / 3.0
        # Col 1: Factor Tree
        c1x = x + w3 * 0.5
        p.text(c1x, y + 3.0, "Way 1: Factor Tree", size=1.68, bold=True, color=INK, align="center")
        p.text(c1x, y + 6.5, "60", size=2.0, bold=True, mono=True, color=INK, align="center")
        p.line(c1x - 1.5, y + 7.2, c1x - 6.0, y + 10.2, color=INK, width=0.25)
        p.line(c1x + 1.5, y + 7.2, c1x + 6.0, y + 10.2, color=INK, width=0.25)
        p.text(c1x - 6.5, y + 12.6, "6", size=1.9, bold=True, mono=True, color=SLATE, align="center")
        p.text(c1x + 6.5, y + 12.6, "10", size=1.9, bold=True, mono=True, color=SLATE, align="center")
        for bx_off, p1, p2 in [(-6.5, "2", "3"), (6.5, "2", "5")]:
            p.line(c1x + bx_off - 1.0, y + 13.2, c1x + bx_off - 3.2, y + 16.0, color=INK, width=0.22)
            p.line(c1x + bx_off + 1.0, y + 13.2, c1x + bx_off + 3.2, y + 16.0, color=INK, width=0.22)
            p.circle(c1x + bx_off - 3.4, y + 18.0, 2.0, fill=BLUE_FILL if p1 == "2" else GREEN_FILL, stroke=INK, line_w=0.22)
            p.text(c1x + bx_off - 3.4, y + 18.7, p1, size=1.7, bold=True, mono=True, color=INK, align="center")
            p.circle(c1x + bx_off + 3.4, y + 18.0, 2.0, fill=GREEN_FILL if p2 == "3" else GOLD_FILL, stroke=INK, line_w=0.22)
            p.text(c1x + bx_off + 3.4, y + 18.7, p2, size=1.7, bold=True, mono=True, color=INK, align="center")
        p.text(c1x, y + h - 1.5, "Circle prime leaves!", size=1.52, bold=True, color=SLATE, align="center")

        p.line(x + w3, y + 1.5, x + w3, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        # Col 2: Division Ladder
        c2x = x + w3 * 1.5
        p.text(c2x, y + 3.0, "Way 2: Division Ladder", size=1.68, bold=True, color=TEAL, align="center")
        lx = x + w3 + 6.5
        steps_lad = [("2", "60", y + 6.8), ("2", "30", y + 11.2), ("3", "15", y + 15.6)]
        for pdiv, quot, ly in steps_lad:
            p.text(lx, ly, pdiv, size=1.85, bold=True, mono=True, color=TEAL)
            p.line(lx + 3.0, ly - 2.3, lx + 3.0, ly + 0.8, color=INK, width=0.28)
            p.line(lx + 3.0, ly + 0.8, lx + 14.5, ly + 0.8, color=INK, width=0.28)
            p.text(lx + 5.2, ly, quot, size=1.85, bold=True, mono=True, color=INK)
        p.text(lx + 5.8, y + 19.6, "5 (Prime!)", size=1.8, bold=True, mono=True, color=TEAL)
        p.text(c2x, y + h - 1.5, "60 = 2² × 3 × 5", size=1.62, bold=True, mono=True, color=INK, align="center")

        p.line(x + w3 * 2, y + 1.5, x + w3 * 2, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        # Col 3: PRIME-01 Block Tower
        c3x = x + w3 * 2.5
        p.text(c3x, y + 3.0, "Way 3: Prime Blocks", size=1.68, bold=True, color=INK, align="center")
        bx = c3x - 7.0
        by_bot = y + 20.8
        blks = [("2", 3.4, BLUE_FILL), ("2", 3.4, BLUE_FILL), ("3", 4.2, GREEN_FILL), ("5", 5.0, GOLD_FILL)]
        cur_y = by_bot
        for lbl, bh, bcol in blks:
            p.rect(bx, cur_y - bh, 14.0, bh, fill=bcol, stroke=INK, r=0.4, line_w=0.22)
            p.text(c3x, cur_y - bh / 2.0 + 0.65, f"Prime [{lbl}]", size=1.6, bold=True, mono=True, color=INK, align="center")
            cur_y -= bh
        p.text(c3x, y + h - 1.5, "Tower = 2·2·3·5 = 60", size=1.55, bold=True, mono=True, color=TEAL, align="center")

    elif sec_num == "1.5":
        # Authentic Prime Factor Venn Diagram with PRIME-01 Blocks for 20 and 50!
        p.text(mid_x, y + 3.0, "Prime Factor Venn Diagram with Blocks (20 = 2·2·5 and 50 = 2·5·5)", size=1.72, bold=True, color=INK, align="center")
        cy = y + 11.8
        r_v = 7.2
        c_left = mid_x - 4.8
        c_right = mid_x + 4.8
        # Draw left & right circles + intersection highlight
        p.circle(c_left, cy, r_v, fill="#EFF6FF", stroke=INK, line_w=0.3)
        p.circle(c_right, cy, r_v, fill="#FEFCE8", stroke=INK, line_w=0.3)
        # Re-stroke left circle so both outlines show cleanly over the overlap lens
        p.circle(c_left, cy, r_v, fill=None, stroke=INK, line_w=0.3)

        # Labels cleanly outside left & right of circles (zero overlap with circle arcs!)
        p.text(mid_x - 27.5, cy - 2.2, "Primes of 20", size=1.68, bold=True, color=INK, align="center")
        p.text(mid_x - 27.5, cy + 0.3, "20 = 2 × 2 × 5", size=1.55, mono=True, color=SLATE, align="center")
        p.text(mid_x - 27.5, cy + 2.8, "Left only: [2]", size=1.50, bold=True, color=TEAL, align="center")

        p.text(mid_x + 27.5, cy - 2.2, "Primes of 50", size=1.68, bold=True, color=INK, align="center")
        p.text(mid_x + 27.5, cy + 0.3, "50 = 2 × 5 × 5", size=1.55, mono=True, color=SLATE, align="center")
        p.text(mid_x + 27.5, cy + 2.8, "Right only: [5]", size=1.50, bold=True, color="#854D0E", align="center")

        # Left-only Prime Block [2]
        p.rect(c_left - 5.2, cy - 1.9, 4.4, 3.8, fill=BLUE_FILL, stroke=INK, r=0.45, line_w=0.25)
        p.text(c_left - 3.0, cy + 0.65, "[2]", size=1.72, bold=True, mono=True, color=INK, align="center")

        # Shared Overlap Prime Blocks [2] and [5] (GCF!)
        p.rect(mid_x - 2.2, cy - 4.1, 4.4, 3.6, fill=BLUE_FILL, stroke=TEAL, r=0.45, line_w=0.28)
        p.text(mid_x, cy - 1.65, "[2]", size=1.68, bold=True, mono=True, color=INK, align="center")
        p.rect(mid_x - 2.2, cy + 0.3, 4.4, 3.6, fill=GOLD_FILL, stroke=TEAL, r=0.45, line_w=0.28)
        p.text(mid_x, cy + 2.75, "[5]", size=1.68, bold=True, mono=True, color=INK, align="center")

        # Right-only Prime Block [5]
        p.rect(c_right + 0.8, cy - 1.9, 4.4, 3.8, fill=GOLD_FILL, stroke=INK, r=0.45, line_w=0.25)
        p.text(c_right + 3.0, cy + 0.65, "[5]", size=1.72, bold=True, mono=True, color=INK, align="center")

        # Bottom summary callout
        p.rect(x + 2.5, y + h - 4.8, w - 5.0, 3.8, fill=SUBTLE_HDR, stroke=BORDER, r=0.5, line_w=0.2)
        p.text(
            mid_x,
            y + h - 2.2,
            "Overlap = GCF: 2 × 5 = 10   |   All Blocks = LCM: 2 × 2 × 5 × 5 = 100",
            size=1.68,
            bold=True,
            mono=True,
            color=TEAL,
            align="center",
        )

    # =========================================================================
    # UNIT 2: FRACTIONS & DECIMALS (2.1 - 2.5)
    # =========================================================================
    elif sec_num == "2.1":
        # Aligned Fraction Strips (FRAC-01) showing 1/3 + 1/4 = 4/12 + 3/12 = 7/12
        p.text(mid_x, y + 3.0, "Fraction Strips (FRAC-01): Trade 1/3 + 1/4 for LCD Twelfths (7/12)", size=1.70, bold=True, color=INK, align="center")
        bx = x + 4.0
        bw = 54.0
        # Row 1: 1 Whole
        p.rect(bx, y + 4.5, bw, 3.6, fill=GRAY_FILL, stroke=INK, line_w=0.22)
        p.text(bx + bw / 2.0, y + 6.9, "1 Whole Strip (12/12)", size=1.6, bold=True, mono=True, color=INK, align="center")
        # Row 2: 1/3 + 1/4
        w_13 = bw / 3.0
        w_14 = bw / 4.0
        p.rect(bx, y + 9.0, w_13, 4.0, fill=BLUE_FILL, stroke=INK, line_w=0.24)
        p.text(bx + w_13 / 2.0, y + 11.6, "1/3", size=1.75, bold=True, mono=True, color=INK, align="center")
        p.rect(bx + w_13, y + 9.0, w_14, 4.0, fill=GOLD_FILL, stroke=INK, line_w=0.24)
        p.text(bx + w_13 + w_14 / 2.0, y + 11.6, "1/4", size=1.75, bold=True, mono=True, color=INK, align="center")
        # Row 3: 4/12 + 3/12 = 7/12
        w_12 = bw / 12.0
        for i in range(7):
            p.rect(bx + i * w_12, y + 14.0, w_12, 4.2, fill=BLUE_FILL if i < 4 else GOLD_FILL, stroke=INK, line_w=0.22)
            p.text(bx + (i + 0.5) * w_12, y + 16.7, "1/12", size=1.18, bold=True, mono=True, color=INK, align="center")
        p.line(bx + 7 * w_12, y + 8.6, bx + 7 * w_12, y + 18.8, color=TEAL, width=0.35, dashed=True)
        p.text(bx + 3.5 * w_12, y + h - 2.0, "4/12 + 3/12 = 7/12 (Exact Length Match!)", size=1.62, bold=True, mono=True, color=TEAL, align="center")

        # Right box: Simplifying & Mixed Numbers
        rx = bx + bw + 3.0
        rw = w - (bw + 9.0)
        p.rect(rx, y + 4.5, rw, 18.5, fill=SUBTLE_HDR, stroke=BORDER, r=0.6, line_w=0.2)
        p.text(rx + rw / 2.0, y + 7.4, "Simplify:", size=1.55, bold=True, color=SLATE, align="center")
        p.text(rx + rw / 2.0, y + 10.2, "12/18 = 2/3", size=1.65, bold=True, mono=True, color=INK, align="center")
        p.line(rx + 2.0, y + 12.0, rx + rw - 2.0, y + 12.0, color=LIGHT_BORDER, width=0.2)
        p.text(rx + rw / 2.0, y + 14.8, "Mixed Number:", size=1.55, bold=True, color=SLATE, align="center")
        p.text(rx + rw / 2.0, y + 17.8, "2 1/3 = 7/3", size=1.65, bold=True, mono=True, color=TEAL, align="center")
        p.text(rx + rw / 2.0, y + 20.6, "(3×2 + 1)/3", size=1.45, mono=True, color=MUTED, align="center")

    elif sec_num == "2.2":
        # Left: 2D Fraction Area Model for 1/2 × 3/4 = 3/8
        p.text(x + 22.0, y + 3.0, "Way 1: Area Model (1/2 of 3/4 = 3/8)", size=1.68, bold=True, color=INK, align="center")
        gx, gy = x + 6.0, y + 5.0
        cw, ch_cell = 7.5, 6.2
        for r in range(2):
            for c in range(4):
                if r == 0 and c < 3:
                    fill_c = TEAL
                    txt_c = WHITE
                    lbl = "1/8"
                elif c < 3:
                    fill_c = BLUE_FILL
                    txt_c = INK
                    lbl = "1/8"
                else:
                    fill_c = WHITE
                    txt_c = MUTED
                    lbl = ""
                p.rect(gx + c * cw, gy + r * ch_cell, cw, ch_cell, fill=fill_c, stroke=INK, line_w=0.25)
                if lbl:
                    p.text(gx + (c + 0.5) * cw, gy + (r + 0.62) * ch_cell, lbl, size=1.55, bold=True, mono=True, color=txt_c, align="center")
        p.text(gx - 1.2, gy + 3.8, "1/2", size=1.65, bold=True, mono=True, color=TEAL, align="right")
        p.text(gx + 1.5 * cw, gy + 2 * ch_cell + 2.8, "3/4 Shaded Columns -> 3/8 Overlap", size=1.58, bold=True, color=INK, align="center")

        p.line(mid_x + 1.0, y + 1.5, mid_x + 1.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        # Right: Cross-Canceling Shortcut
        rx = mid_x + 21.8
        p.text(rx, y + 3.0, "Way 2 & 3: Multiply or Cross-Cancel", size=1.65, bold=True, color=TEAL, align="center")
        p.rect(mid_x + 2.0, y + 5.0, 39.5, 8.2, fill=SUBTLE_HDR, stroke=BORDER, r=0.6, line_w=0.2)
        p.text(rx, y + 8.0, "Multiply Across: (1×3) / (2×4) = 3/8", size=1.55, bold=True, mono=True, color=INK, align="center", max_w=37.5)
        p.text(rx, y + 11.4, "Mixed Numbers: 2 2/3 × 1 1/2 = 8/3 × 3/2", size=1.45, bold=True, mono=True, color=SLATE, align="center", max_w=37.5)
        p.rect(mid_x + 2.0, y + 14.4, 39.5, 8.2, fill=GREEN_FILL, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx, y + 17.6, "Cross-Cancel Common Factors First:", size=1.52, bold=True, color=INK, align="center", max_w=37.5)
        p.text(rx, y + 20.8, "(8÷2)/(3÷3) × (3÷3)/(2÷2) = 4/1 × 1/1 = 4", size=1.42, bold=True, mono=True, color=TEAL, align="center", max_w=37.5)

    elif sec_num == "2.3":
        # Fraction Division: Strip Measurement (3/4 ÷ 1/8 = 6) + Keep-Change-Flip
        p.text(x + 23.0, y + 3.0, "Way 1: Fraction Strips (How many 1/8s in 3/4?)", size=1.65, bold=True, color=INK, align="center")
        bx = x + 3.5
        bw = 39.0
        p.rect(bx, y + 5.2, bw, 4.8, fill=BLUE_FILL, stroke=INK, line_w=0.25)
        for q in range(1, 3):
            p.line(bx + q * (bw / 3.0), y + 5.2, bx + q * (bw / 3.0), y + 10.0, color=INK, width=0.22, dashed=True)
        p.text(bx + bw / 2.0, y + 8.3, "3/4 Strip (= 6/8)", size=1.7, bold=True, mono=True, color=INK, align="center")
        w8 = bw / 6.0
        for i in range(6):
            p.rect(bx + i * w8, y + 11.2, w8, 4.8, fill=GOLD_FILL, stroke=INK, line_w=0.22)
            p.text(bx + (i + 0.5) * w8, y + 14.3, "1/8", size=1.45, bold=True, mono=True, color=INK, align="center")
        p.text(x + 23.0, y + 19.6, "Six 1/8-strips fit inside 3/4!", size=1.62, bold=True, color=TEAL, align="center")
        p.text(x + 23.0, y + h - 1.6, "Way 3 (LCD): 6/8 ÷ 1/8 = 6 ÷ 1 = 6", size=1.58, bold=True, mono=True, color=SLATE, align="center")

        p.line(mid_x + 2.0, y + 1.5, mid_x + 2.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        rx = mid_x + 22.5
        p.text(rx, y + 3.0, "Way 2: Multiply by the Reciprocal", size=1.65, bold=True, color=TEAL, align="center")
        p.rect(mid_x + 4.5, y + 5.2, 36.0, 17.5, fill=SUBTLE_HDR, stroke=INK, r=0.7, line_w=0.22)
        p.text(rx, y + 8.8, "3/4  ÷  1/8", size=2.1, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 12.4, "Keep   Change   Flip!", size=1.62, bold=True, color=TEAL, align="center")
        p.text(rx, y + 16.2, "= 3/4  ×  8/1  =  24/4  =  6", size=1.85, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 20.4, "Reciprocals: 1/8 × 8/1 = 1", size=1.55, bold=True, mono=True, color=SLATE, align="center")

    elif sec_num == "2.4":
        # Decimal Line-Up (Addition/Subtraction) + Counting Decimal Places (Multiplication)
        p.text(x + 21.0, y + 3.0, "Add/Subtract: Line Up Decimal Points", size=1.65, bold=True, color=INK, align="center")
        p.rect(x + 3.0, y + 4.8, 36.0, 18.0, fill=SUBTLE_HDR, stroke=BORDER, r=0.6, line_w=0.22)
        p.text(x + 26.0, y + 8.6, "14.60", size=2.0, bold=True, mono=True, color=INK, align="right")
        p.text(x + 35.5, y + 8.6, "<- Annex 0", size=1.45, bold=True, color=TEAL, align="right")
        p.text(x + 26.0, y + 12.2, "+  3.85", size=2.0, bold=True, mono=True, color=INK, align="right")
        p.line(x + 10.0, y + 13.4, x + 27.0, y + 13.4, color=INK, width=0.28)
        p.text(x + 26.0, y + 16.8, "18.45", size=2.05, bold=True, mono=True, color=TEAL, align="right")
        p.line(x + 20.1, y + 6.0, x + 20.1, y + 17.5, color=TEAL, width=0.25, dashed=True)
        p.text(x + 21.0, y + 21.0, "Estimate: 15 + 4 = 19 (Close!)", size=1.55, bold=True, color=SLATE, align="center")

        p.line(mid_x - 1.0, y + 1.5, mid_x - 1.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        rx = mid_x + 21.5
        p.text(rx, y + 3.0, "Multiply: Count Total Decimal Places", size=1.65, bold=True, color=TEAL, align="center")
        p.rect(mid_x + 2.0, y + 4.8, 39.0, 18.0, fill=BLUE_FILL, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx, y + 8.6, "  4.5    (1 decimal place)", size=1.72, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 12.0, "× 1.80   (2 decimal places)", size=1.72, bold=True, mono=True, color=INK, align="center")
        p.line(mid_x + 6.0, y + 13.2, mid_x + 37.0, y + 13.2, color=INK, width=0.28)
        p.text(rx, y + 16.8, "= 8.100  (1 + 2 = 3 places)", size=1.75, bold=True, mono=True, color=TEAL, align="center")
        p.text(rx, y + 20.8, "= $8.10  (Check: 45×18 = 810)", size=1.6, bold=True, color=SLATE, align="center")

    elif sec_num == "2.5":
        # Decimal Division: Annexing Zeros (23.00 ÷ 4) + Shifting Decimal Point (6.75 ÷ 0.25)
        p.text(x + 21.0, y + 3.0, "Way 1: Annex Zeros (23 ÷ 4 = 5.75)", size=1.65, bold=True, color=INK, align="center")
        p.rect(x + 3.0, y + 4.8, 36.0, 18.0, fill=SUBTLE_HDR, stroke=BORDER, r=0.6, line_w=0.22)
        p.text(x + 21.0, y + 8.4, "5.75", size=2.0, bold=True, mono=True, color=TEAL, align="center")
        p.text(x + 21.0, y + 12.2, "4 ) 23.00", size=2.0, bold=True, mono=True, color=INK, align="center")
        p.text(x + 21.0, y + 16.2, "Way 2 (Mixed #): 23/4 = 5 3/4", size=1.62, bold=True, mono=True, color=INK, align="center")
        p.text(x + 21.0, y + 20.4, "Way 3 ( ÷100 ): 575/100 = 5.75", size=1.58, bold=True, mono=True, color=SLATE, align="center")

        p.line(mid_x - 1.0, y + 1.5, mid_x - 1.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        rx = mid_x + 21.5
        p.text(rx, y + 3.0, "Decimal Divisor: Shift Both Points Right!", size=1.65, bold=True, color=TEAL, align="center")
        p.rect(mid_x + 2.0, y + 4.8, 39.0, 18.0, fill=GOLD_FILL, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx, y + 8.6, "6.75 ÷ 0.25   (×100 both)", size=1.78, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 12.4, "Shift 2 places right ->  675 ÷ 25", size=1.68, bold=True, color=TEAL, align="center")
        p.text(rx, y + 16.6, "675 ÷ 25 = 27", size=2.0, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 20.6, "Check: 27 × 0.25 = 6.75", size=1.6, bold=True, mono=True, color=SLATE, align="center")

    # =========================================================================
    # UNIT 3: RATIOS, RATES & PERCENTS (3.1 - 3.5)
    # =========================================================================
    elif sec_num == "3.1":
        # Tape Diagram for 12 Builders and 8 Programmers (3:2 Part-to-Part and 3:5 Part-to-Whole)
        p.text(mid_x, y + 3.0, "Ratio Tape Diagram: 12 Builders & 8 Programmers (5 Total Boxes = 20 Members)", size=1.68, bold=True, color=INK, align="center")
        gx = x + 3.5
        p.text(gx, y + 8.2, "Builders (3):", size=1.68, bold=True, color=INK)
        p.text(gx, y + 15.6, "Program (2):", size=1.68, bold=True, color=INK)
        bx0 = gx + 20.5
        bw, bh = 8.2, 5.2
        for i in range(3):
            p.rect(bx0 + i * (bw + 0.6), y + 4.8, bw, bh, fill=BLUE_FILL, stroke=INK, r=0.4, line_w=0.22)
            p.text(bx0 + i * (bw + 0.6) + bw / 2.0, y + 8.1, "4", size=1.85, bold=True, mono=True, color=INK, align="center")
        for i in range(2):
            p.rect(bx0 + i * (bw + 0.6), y + 12.2, bw, bh, fill=GOLD_FILL, stroke=INK, r=0.4, line_w=0.22)
            p.text(bx0 + i * (bw + 0.6) + bw / 2.0, y + 15.5, "4", size=1.85, bold=True, mono=True, color=INK, align="center")
        p.text(bx0 + 3 * (bw + 0.6) + 2.0, y + 8.1, "= 12 Builders (3 × 4)", size=1.70, bold=True, mono=True, color=TEAL)
        p.text(bx0 + 2 * (bw + 0.6) + 2.0, y + 15.5, "= 8 Programmers (2 × 4)", size=1.70, bold=True, mono=True, color=SLATE)
        p.text(mid_x, y + h - 1.8, "Part-to-Part = 12:8 = 3:2   |   Part-to-Whole = 12:20 = 3:5 (Each box = 4 members)", size=1.60, bold=True, mono=True, color=TEAL, align="center")

    elif sec_num == "3.2":
        # Left: Ratio Table | Right: Double Number Line
        p.text(x + 21.0, y + 3.0, "Way 1 & 2: Ratio Table (×5 Scale)", size=1.65, bold=True, color=INK, align="center")
        tx, ty = x + 2.5, y + 4.8
        cw_t, rh_t = 7.2, 5.8
        headers = ["Time", "3", "6", "9", "15"]
        dists = ["Dist", "8", "16", "24", "40"]
        for c_i, (h_v, d_v) in enumerate(zip(headers, dists)):
            cx = tx + c_i * cw_t
            bg1 = SUBTLE_HDR if c_i == 0 else (BLUE_FILL if c_i == 4 else WHITE)
            bg2 = SUBTLE_HDR if c_i == 0 else (GOLD_FILL if c_i == 4 else WHITE)
            p.rect(cx, ty, cw_t, rh_t, fill=bg1, stroke=INK, line_w=0.22)
            p.rect(cx, ty + rh_t, cw_t, rh_t, fill=bg2, stroke=INK, line_w=0.22)
            p.text(cx + cw_t / 2.0, ty + 3.8, h_v, size=1.65, bold=True, mono=True, color=INK, align="center")
            p.text(cx + cw_t / 2.0, ty + rh_t + 3.8, d_v, size=1.65, bold=True, mono=True, color=INK, align="center")
        p.text(x + 21.0, y + 20.8, "3 × 5 = 15 s  and  8 × 5 = 40 m", size=1.58, bold=True, mono=True, color=TEAL, align="center")

        p.line(mid_x - 1.5, y + 1.5, mid_x - 1.5, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        rx = mid_x + 21.0
        p.text(rx, y + 3.0, "Way 3: Double Number Line", size=1.65, bold=True, color=TEAL, align="center")
        lx1, lx2 = mid_x + 7.5, x + w - 3.5
        y_top, y_bot = y + 9.2, y + 17.2
        p.text(mid_x + 0.5, y_top + 0.8, "Sec:", size=1.5, bold=True, color=INK)
        p.text(mid_x + 0.5, y_bot + 0.8, "Met:", size=1.5, bold=True, color=TEAL)
        p.line(lx1, y_top, lx2, y_top, color=INK, width=0.3)
        p.line(lx1, y_bot, lx2, y_bot, color=TEAL, width=0.3)
        for idx, (sv, mv) in enumerate([(0, 0), (3, 8), (6, 16), (9, 24), (12, 32), (15, 40)]):
            px = lx1 + idx * ((lx2 - lx1) / 5.0)
            p.line(px, y_top - 1.0, px, y_top + 1.0, color=INK, width=0.25)
            p.line(px, y_bot - 1.0, px, y_bot + 1.0, color=TEAL, width=0.25)
            p.text(px, y_top - 1.6, str(sv), size=1.5, bold=(idx == 5), mono=True, color=INK, align="center")
            p.text(px, y_bot + 3.2, str(mv), size=1.5, bold=(idx == 5), mono=True, color=TEAL, align="center")

    elif sec_num == "3.3":
        # Unit Rate Division + Better-Buy Comparison
        p.text(x + 21.0, y + 3.0, "Unit Rate: Denominator of 1 Unit", size=1.68, bold=True, color=INK, align="center")
        p.rect(x + 2.5, y + 4.8, 37.0, 18.0, fill=SUBTLE_HDR, stroke=INK, r=0.6, line_w=0.22)
        p.text(x + 21.0, y + 9.0, "315 words        63 words", size=1.75, bold=True, mono=True, color=INK, align="center")
        p.line(x + 5.5, y + 10.2, x + 19.5, y + 10.2, color=INK, width=0.28)
        p.line(x + 23.5, y + 10.2, x + 36.5, y + 10.2, color=TEAL, width=0.28)
        p.text(x + 21.0, y + 10.8, "÷5 ->", size=1.5, bold=True, color=TEAL, align="center")
        p.text(x + 21.0, y + 13.4, "5 minutes        1 minute", size=1.75, bold=True, mono=True, color=INK, align="center")
        p.text(x + 21.0, y + 18.0, "Unit Rate = 63 words/min", size=1.68, bold=True, color=TEAL, align="center")
        p.text(x + 21.0, y + 21.2, "In 8 min: 63 × 8 = 504 words", size=1.55, bold=True, mono=True, color=SLATE, align="center")

        p.line(mid_x - 1.0, y + 1.5, mid_x - 1.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        rx = mid_x + 21.5
        p.text(rx, y + 3.0, "Comparing Rates (Better Buy)", size=1.68, bold=True, color=TEAL, align="center")
        p.rect(mid_x + 2.0, y + 5.0, 39.0, 8.2, fill=WHITE, stroke=BORDER, r=0.5, line_w=0.2)
        p.text(rx, y + 8.2, "Pack A: $5.80 ÷ 4 = $1.45 / battery", size=1.62, bold=True, mono=True, color=SLATE, align="center")
        p.text(rx, y + 11.4, "(12 batteries = 3 × $5.80 = $17.40)", size=1.48, mono=True, color=MUTED, align="center")
        p.rect(mid_x + 2.0, y + 14.2, 39.0, 8.5, fill=GREEN_FILL, stroke=INK, r=0.5, line_w=0.24)
        p.text(rx, y + 17.4, "Pack B: $8.40 ÷ 6 = $1.40 / battery", size=1.62, bold=True, mono=True, color=TEAL, align="center")
        p.text(rx, y + 20.8, "Pack B is cheaper! ($16.80 for 12)", size=1.55, bold=True, color=INK, align="center")

    elif sec_num == "3.4":
        # Left: 10×10 Hundred-Grid (35/100 shaded = 35%) | Right: 3 Ways to Convert 7/20
        p.text(x + 19.0, y + 3.0, "10×10 Grid: 7/20 = 35/100 = 35%", size=1.65, bold=True, color=INK, align="center")
        gx, gy = x + 6.5, y + 4.5
        cs = 1.75
        for r in range(10):
            for c in range(10):
                idx = c * 10 + r
                p.rect(gx + c * cs, gy + r * cs, cs, cs, fill=BLUE_FILL if idx < 35 else WHITE, stroke=BORDER, line_w=0.14)
        p.rect(gx, gy, 10 * cs, 10 * cs, fill=None, stroke=INK, line_w=0.28)
        p.text(gx + 10 * cs + 2.2, gy + 5.0, "35 of 100", size=1.6, bold=True, color=TEAL)
        p.text(gx + 10 * cs + 2.2, gy + 8.0, "squares", size=1.55, color=SLATE)
        p.text(gx + 10 * cs + 2.2, gy + 11.5, "= 0.35", size=1.7, bold=True, mono=True, color=INK)
        p.text(gx + 10 * cs + 2.2, gy + 14.8, "= 35%", size=1.8, bold=True, mono=True, color=TEAL)

        p.line(mid_x - 2.0, y + 1.5, mid_x - 2.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        rx = mid_x + 20.5
        p.text(rx, y + 3.0, "3 Ways: Fraction <-> Decimal <-> %", size=1.65, bold=True, color=TEAL, align="center")
        ways = [
            ("Way 1 (Scale to 100):", "7/20 × 5/5 = 35/100 = 35%"),
            ("Way 2 (Divide):", "7 ÷ 20 = 0.35 -> 35%"),
            ("Way 3 (% of Whole):", "35% of 80 = 0.35 × 80 = 28"),
        ]
        for idx, (wt, wb) in enumerate(ways):
            wy = y + 4.8 + idx * 6.2
            p.rect(mid_x + 0.5, wy, 40.5, 5.4, fill=SUBTLE_HDR if idx != 1 else GOLD_FILL, stroke=BORDER, r=0.45, line_w=0.2)
            p.text(mid_x + 1.8, wy + 2.3, wt, size=1.48, bold=True, color=TEAL)
            p.text(mid_x + 1.8, wy + 4.4, wb, size=1.52, bold=True, mono=True, color=INK)

    elif sec_num == "3.5":
        # Percent Bar Model (25% Discount on $60) + Percent Change & Unit Conversion
        p.text(mid_x, y + 3.0, "Percent Discount Bar Model ($60 Hoodie at 25% Off) & Unit Conversion", size=1.68, bold=True, color=INK, align="center")
        bx, by, bw, bh = x + 3.5, y + 5.0, 46.0, 6.2
        p.rect(bx, by, bw * 0.75, bh, fill=GREEN_FILL, stroke=INK, line_w=0.25)
        p.rect(bx + bw * 0.75, by, bw * 0.25, bh, fill=RED_FILL, stroke=INK, line_w=0.25)
        p.text(bx + bw * 0.375, by + 4.0, "Sale Price: 75% of $60 = $45", size=1.62, bold=True, mono=True, color=INK, align="center")
        p.text(bx + bw * 0.875, by + 4.0, "-25% ($15)", size=1.45, bold=True, mono=True, color=SLATE, align="center")
        p.text(bx + bw / 2.0, y + 14.5, "Way 1: $60 - $15 = $45   |   Way 2: 0.75 × $60 = $45", size=1.58, bold=True, mono=True, color=TEAL, align="center")
        p.text(bx + bw / 2.0, y + 18.2, "% Change = (Change ÷ Original) × 100%", size=1.55, bold=True, color=INK, align="center")
        p.text(bx + bw / 2.0, y + 21.8, "Watch Out: Always divide by the ORIGINAL amount!", size=1.48, bold=True, color=SLATE, align="center")

        rx = bx + bw + 2.5
        rw = w - bw - 8.5
        p.rect(rx, y + 5.0, rw, 17.8, fill=SUBTLE_HDR, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx + rw / 2.0, y + 8.0, "Unit Conversion", size=1.6, bold=True, color=TEAL, align="center")
        p.text(rx + rw / 2.0, y + 11.4, "Cancel old units:", size=1.48, color=SLATE, align="center")
        p.text(rx + rw / 2.0, y + 15.0, "32 in × (2.54 cm / 1 in)", size=1.52, bold=True, mono=True, color=INK, align="center")
        p.text(rx + rw / 2.0, y + 18.8, "= 81.28 cm", size=1.7, bold=True, mono=True, color=TEAL, align="center")

    # =========================================================================
    # UNIT 4: ALGEBRAIC EXPRESSIONS & PROPERTIES (4.1 - 4.4)
    # =========================================================================
    elif sec_num == "4.1":
        # Expression Anatomy (4x + 7) + Place Value Substitution Boxes (x = 5 -> 27)
        p.text(x + 20.5, y + 3.0, "Parts of an Expression: 4x + 7", size=1.68, bold=True, color=INK, align="center")
        p.rect(x + 2.5, y + 4.8, 36.0, 18.0, fill=SUBTLE_HDR, stroke=BORDER, r=0.6, line_w=0.22)
        p.text(x + 20.5, y + 9.6, "4x  +  7", size=2.8, bold=True, mono=True, color=INK, align="center")
        p.text(x + 11.5, y + 14.0, "Coefficient = 4", size=1.52, bold=True, color=TEAL, align="center")
        p.text(x + 11.5, y + 16.8, "Variable = x", size=1.52, bold=True, color=INK, align="center")
        p.text(x + 29.5, y + 15.4, "Constant = 7", size=1.52, bold=True, color=SLATE, align="center")
        p.text(x + 20.5, y + 20.8, "2 Terms: 4x and 7", size=1.58, bold=True, mono=True, color=INK, align="center")

        p.line(mid_x - 2.0, y + 1.5, mid_x - 2.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        rx = mid_x + 20.5
        p.text(rx, y + 3.0, "Substitute x = 5 into 4x + 7 (PLACE-01)", size=1.65, bold=True, color=TEAL, align="center")
        bx = mid_x + 0.5
        for i in range(4):
            p.rect(bx + i * 7.2, y + 5.5, 6.2, 6.5, fill=GREEN_FILL, stroke=INK, r=0.5, line_w=0.22)
            p.text(bx + i * 7.2 + 3.1, y + 8.2, "x=5", size=1.5, bold=True, mono=True, color=INK, align="center")
            p.text(bx + i * 7.2 + 3.1, y + 10.8, "[5]", size=1.55, bold=True, mono=True, color=TEAL, align="center")
        p.rect(bx + 29.5, y + 5.5, 11.5, 6.5, fill=GOLD_FILL, stroke=INK, r=0.5, line_w=0.22)
        p.text(bx + 35.25, y + 9.6, "+ 7 ones", size=1.6, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 16.5, "4(5) + 7 = 20 + 7 = 27", size=1.9, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 20.8, "Multiply 4(5) BEFORE adding 7 (PEMDAS)!", size=1.52, bold=True, color=TEAL, align="center")

    elif sec_num == "4.2":
        # Combining Like Terms by Variable Power: 4x + 5 + 2x + 3 = 6x + 8
        p.text(mid_x, y + 3.0, "Combining Like Terms by Variable Power: 4x + 5 + 2x + 3 = 6x + 8", size=1.68, bold=True, color=INK, align="center")
        gx, gy = x + 3.0, y + 5.0
        # x² block for reference
        p.rect(gx, gy, 10.5, 10.5, fill=BLUE_FILL, stroke=INK, r=0.5, line_w=0.24)
        p.text(gx + 5.25, gy + 6.2, "x² Term", size=1.65, bold=True, mono=True, color=INK, align="center")
        p.text(gx + 5.25, y + 18.2, "(x by x)", size=1.45, color=SLATE, align="center")

        # 6 x-bars (4 green + 2 light-green)
        rx = gx + 13.5
        for i in range(6):
            p.rect(rx + i * 5.2, gy, 4.2, 10.5, fill=GREEN_FILL if i < 4 else "#BBF7D0", stroke=INK, r=0.35, line_w=0.22)
            p.text(rx + i * 5.2 + 2.1, gy + 6.2, "x", size=1.75, bold=True, mono=True, color=INK, align="center")
        p.text(rx + 15.0, y + 18.2, "4x + 2x = 6x Terms", size=1.62, bold=True, mono=True, color=TEAL, align="center")

        # 8 unit blocks (5 + 3)
        ux = rx + 33.5
        for r in range(2):
            for c in range(4):
                p.rect(ux + c * 4.2, gy + 1.2 + r * 4.4, 3.5, 3.5, fill=GOLD_FILL, stroke=INK, r=0.3, line_w=0.2)
                p.text(ux + c * 4.2 + 1.75, gy + 1.2 + r * 4.4 + 2.4, "1", size=1.45, bold=True, mono=True, color=INK, align="center")
        p.text(ux + 8.0, y + 18.2, "5 + 3 = 8 Ones", size=1.62, bold=True, mono=True, color=INK, align="center")
        p.text(mid_x, y + h - 1.6, "Watch Out: 6x and 8 are unlike terms -> NEVER combine into 14x!", size=1.55, bold=True, color=SLATE, align="center")

    elif sec_num == "4.3":
        # Distributive Property Area Model: 6(10 + 4) = 60 + 24 = 84 & 3(2x + 5) = 6x + 15
        p.text(x + 23.0, y + 3.0, "Area Model (PLACE-01): 6(10 + 4) = 60 + 24", size=1.65, bold=True, color=INK, align="center")
        rx, ry = x + 6.5, y + 6.8
        w1, w2, rh_box = 22.0, 11.0, 10.5
        p.rect(rx, ry, w1, rh_box, fill=BLUE_FILL, stroke=INK, line_w=0.28)
        p.rect(rx + w1, ry, w2, rh_box, fill=GOLD_FILL, stroke=INK, line_w=0.28)
        p.text(rx - 1.5, ry + 6.0, "6", size=1.95, bold=True, mono=True, color=INK, align="right")
        p.text(rx + w1 / 2.0, ry - 1.2, "10", size=1.75, bold=True, mono=True, color=INK, align="center")
        p.text(rx + w1 + w2 / 2.0, ry - 1.2, "+ 4", size=1.75, bold=True, mono=True, color=INK, align="center")
        p.text(rx + w1 / 2.0, ry + 6.2, "6 × 10 = 60", size=1.75, bold=True, mono=True, color=INK, align="center")
        p.text(rx + w1 + w2 / 2.0, ry + 6.2, "6×4=24", size=1.6, bold=True, mono=True, color=INK, align="center")
        p.text(x + 23.0, y + h - 1.8, "Total Area: 6(14) = 60 + 24 = 84", size=1.62, bold=True, mono=True, color=TEAL, align="center")

        p.line(mid_x + 1.5, y + 1.5, mid_x + 1.5, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        ax = mid_x + 22.0
        p.text(ax, y + 3.0, "Algebraic Distribution: a(b + c) = ab + ac", size=1.65, bold=True, color=TEAL, align="center")
        p.rect(mid_x + 3.5, y + 5.2, 37.5, 17.2, fill=SUBTLE_HDR, stroke=BORDER, r=0.6, line_w=0.22)
        p.text(ax, y + 9.4, "3 ( 2x  +  5 )", size=2.1, bold=True, mono=True, color=INK, align="center")
        p.text(ax, y + 13.4, "= 3(2x) + 3(5)", size=1.8, bold=True, mono=True, color=TEAL, align="center")
        p.text(ax, y + 17.4, "= 6x + 15", size=2.0, bold=True, mono=True, color=INK, align="center")
        p.text(ax, y + 20.8, "Multiply BOTH terms inside ( ) by 3!", size=1.52, bold=True, color=SLATE, align="center")

    elif sec_num == "4.4":
        # Factoring Using GCF (Reverse Area Model): 18x + 24 = 6(3x + 4)
        p.text(mid_x, y + 3.0, "Factoring = Undoing the Distributive Property Using the GCF: 18x + 24 = 6(3x + 4)", size=1.68, bold=True, color=INK, align="center")
        rx, ry = x + 10.0, y + 7.2
        w1, w2, rh_box = 24.0, 16.0, 11.0
        p.rect(rx, ry, w1, rh_box, fill=GREEN_FILL, stroke=INK, line_w=0.28)
        p.rect(rx + w1, ry, w2, rh_box, fill=GOLD_FILL, stroke=INK, line_w=0.28)
        p.text(rx - 1.8, ry + 6.4, "GCF = 6", size=1.85, bold=True, mono=True, color=TEAL, align="right")
        p.text(rx + w1 / 2.0, ry - 1.2, "18x ÷ 6 = 3x", size=1.68, bold=True, mono=True, color=INK, align="center")
        p.text(rx + w1 + w2 / 2.0, ry - 1.2, "+ 24 ÷ 6 = + 4", size=1.68, bold=True, mono=True, color=INK, align="center")
        p.text(rx + w1 / 2.0, ry + 6.4, "Area = 18x", size=1.85, bold=True, mono=True, color=INK, align="center")
        p.text(rx + w1 + w2 / 2.0, ry + 6.4, "Area = 24", size=1.85, bold=True, mono=True, color=INK, align="center")

        bx = rx + w1 + w2 + 3.0
        bw = w - (bx - x) - 2.5
        p.rect(bx, y + 5.2, bw, 15.0, fill=SUBTLE_HDR, stroke=INK, r=0.6, line_w=0.22)
        p.text(bx + bw / 2.0, y + 8.6, "Factored Form:", size=1.58, bold=True, color=SLATE, align="center")
        p.text(bx + bw / 2.0, y + 12.6, "6(3x + 4)", size=2.1, bold=True, mono=True, color=TEAL, align="center")
        p.text(bx + bw / 2.0, y + 16.4, "Check: 6(3x)+6(4)", size=1.5, mono=True, color=INK, align="center")
        p.text(bx + bw / 2.0, y + 19.0, "= 18x + 24", size=1.55, bold=True, mono=True, color=INK, align="center")
        p.text(mid_x, y + h - 1.6, "6 Equal Rows of (3x + 4) Tiles   |   GCF(3, 4) = 1 -> Factored Completely!", size=1.58, bold=True, color=TEAL, align="center")

    # =========================================================================
    # UNIT 5: AREAS OF POLYGONS & ELAPSED TIME (5.1 - 5.4)
    # =========================================================================
    elif sec_num == "5.1":
        # Parallelogram Cut-and-Slide Visual Proof into a b × h Rectangle
        p.text(mid_x, y + 3.0, "Parallelogram Cut-and-Slide Proof: Area = Base b × Perpendicular Height h", size=1.68, bold=True, color=INK, align="center")
        # Left: Parallelogram with right triangle shaded on left
        px0, py0 = x + 4.5, y + 6.0
        pts_main = [(px0 + 6.0, py0), (px0 + 28.0, py0), (px0 + 28.0, py0 + 11.5), (px0 + 6.0, py0 + 11.5)]
        p.polygon(pts_main, fill=BLUE_FILL, stroke=INK, line_w=0.26)
        pts_tri_l = [(px0 + 6.0, py0), (px0 + 6.0, py0 + 11.5), (px0, py0 + 11.5)]
        p.polygon(pts_tri_l, fill=GOLD_FILL, stroke=INK, line_w=0.28)
        pts_tri_ghost = [(px0 + 28.0, py0), (px0 + 34.0, py0), (px0 + 28.0, py0 + 11.5)]
        p.polygon(pts_tri_ghost, fill=WHITE, stroke=TEAL, line_w=0.25)
        p.line(px0 + 6.0, py0, px0 + 6.0, py0 + 11.5, color=TEAL, width=0.35, dashed=True)
        p.rect(px0 + 6.0, py0 + 9.7, 1.8, 1.8, fill=None, stroke=TEAL, line_w=0.22)
        p.text(px0 + 11.5, py0 + 6.5, "h = 8 cm (90°)", size=1.65, bold=True, mono=True, color=TEAL)
        p.text(px0 + 15.0, py0 + 14.2, "Base b = 12 cm", size=1.65, bold=True, mono=True, color=INK, align="center")
        p.text(px0 + 33.0, py0 + 7.5, "Slant 10", size=1.45, color=MUTED)
        p.text(px0 + 33.0, py0 + 9.8, "(Ignore!)", size=1.45, bold=True, color=SLATE)

        # Right: Resulting 12 × 8 Rectangle
        rx = mid_x + 6.0
        p.rect(rx, py0, 22.0, 11.5, fill=BLUE_FILL, stroke=INK, line_w=0.28)
        p.polygon([(rx + 22.0, py0), (rx + 28.0, py0), (rx + 22.0, py0 + 11.5)], fill=GOLD_FILL, stroke=INK, line_w=0.28)
        p.rect(rx, py0, 28.0, 11.5, fill=None, stroke=INK, line_w=0.3)
        p.text(rx + 14.0, py0 + 6.5, "Rectangle: 12 × 8 = 96 cm²", size=1.68, bold=True, mono=True, color=INK, align="center")
        p.text(rx + 14.0, py0 + 14.2, "Perimeter = 12+10+12+10 = 44 cm", size=1.55, bold=True, mono=True, color=TEAL, align="center")

    elif sec_num == "5.2":
        # Triangle Area = 1/2 of Enclosing Rectangle/Parallelogram (A = 1/2 bh)
        p.text(mid_x, y + 3.0, "Triangle Area Proof: Every Triangle Is 1/2 of a b × h Rectangle (A = ½bh)", size=1.68, bold=True, color=INK, align="center")
        rx, ry, rw, rh_b = x + 6.0, y + 5.5, 32.0, 12.5
        p.rect(rx, ry, rw, rh_b, fill=SUBTLE_HDR, stroke=BORDER, line_w=0.25)
        pts = [(rx, ry + rh_b), (rx + rw, ry + rh_b), (rx + 10.0, ry)]
        p.polygon(pts, fill=BLUE_FILL, stroke=INK, line_w=0.3)
        p.line(rx + 10.0, ry, rx + 10.0, ry + rh_b, color=TEAL, width=0.35, dashed=True)
        p.rect(rx + 10.0, ry + rh_b - 1.8, 1.8, 1.8, fill=None, stroke=TEAL, line_w=0.22)
        p.text(rx + 15.5, ry + 7.5, "h = 6 m", size=1.7, bold=True, mono=True, color=TEAL)
        p.text(rx + rw / 2.0, ry + rh_b + 3.2, "Base b = 10 m", size=1.7, bold=True, mono=True, color=INK, align="center")

        bx = mid_x + 2.0
        bw = w - (bx - x) - 2.5
        p.rect(bx, y + 5.2, bw, 17.2, fill=SUBTLE_HDR, stroke=INK, r=0.6, line_w=0.22)
        p.text(bx + bw / 2.0, y + 8.2, "Rectangle = 10 × 6 = 60 m²", size=1.62, bold=True, mono=True, color=SLATE, align="center")
        p.text(bx + bw / 2.0, y + 11.8, "Triangle = ½(10)(6) = 30 m²", size=1.75, bold=True, mono=True, color=TEAL, align="center")
        p.line(bx + 2.0, y + 13.6, bx + bw - 2.0, y + 13.6, color=LIGHT_BORDER, width=0.2)
        p.text(bx + bw / 2.0, y + 16.6, "Missing Height Formula:", size=1.55, bold=True, color=INK, align="center")
        p.text(bx + bw / 2.0, y + 19.8, "h = 2A ÷ b   (Double Area first!)", size=1.55, bold=True, mono=True, color=TEAL, align="center")

    elif sec_num == "5.3":
        # Left: Trapezoid A = 1/2 h (b1 + b2) | Right: Composite L-Shape / Gable Wall
        p.text(x + 21.5, y + 3.0, "Trapezoid: A = ½h(b₁ + b₂)", size=1.68, bold=True, color=INK, align="center")
        tx, ty = x + 5.0, y + 6.5
        pts_trap = [(tx + 6.0, ty), (tx + 24.0, ty), (tx + 30.0, ty + 10.5), (tx, ty + 10.5)]
        p.polygon(pts_trap, fill=GOLD_FILL, stroke=INK, line_w=0.28)
        p.line(tx + 6.0, ty, tx + 6.0, ty + 10.5, color=TEAL, width=0.32, dashed=True)
        p.rect(tx + 6.0, ty + 8.7, 1.8, 1.8, fill=None, stroke=TEAL, line_w=0.2)
        p.text(tx + 15.0, ty - 1.0, "b₁ = 8 m", size=1.6, bold=True, mono=True, color=INK, align="center")
        p.text(tx + 15.0, ty + 13.2, "b₂ = 14 m", size=1.6, bold=True, mono=True, color=INK, align="center")
        p.text(tx + 11.0, ty + 6.2, "h = 6", size=1.65, bold=True, mono=True, color=TEAL)
        p.text(x + 21.5, y + h - 1.5, "A = ½(6)(8+14) = 3(22) = 66 m²", size=1.58, bold=True, mono=True, color=TEAL, align="center")

        p.line(mid_x, y + 1.5, mid_x, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        rx = mid_x + 21.5
        p.text(rx, y + 3.0, "Composite: Decompose or Subtract", size=1.68, bold=True, color=TEAL, align="center")
        gx, gy = mid_x + 8.5, y + 9.5
        p.rect(gx, gy, 24.0, 8.5, fill=BLUE_FILL, stroke=INK, line_w=0.26)
        p.polygon([(gx, gy), (gx + 24.0, gy), (gx + 12.0, y + 4.5)], fill=GREEN_FILL, stroke=INK, line_w=0.26)
        p.text(gx + 12.0, gy + 5.2, "Rect: 12×8 = 96", size=1.55, bold=True, mono=True, color=INK, align="center")
        p.text(gx + 12.0, gy - 1.2, "Tri: ½(12)(5)=30", size=1.45, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + h - 1.5, "Total = 96 + 30 = 126 ft²", size=1.6, bold=True, mono=True, color=INK, align="center")

    elif sec_num == "5.4":
        # Left: Coordinate Plane Rectangle (2,3)-(9,3)-(9,8)-(2,8) | Right: Base-60 Clock & Regrouping
        p.text(x + 21.5, y + 3.0, "Polygon on Coordinate Grid", size=1.68, bold=True, color=INK, align="center")
        gx, gy, gw, gh = x + 6.0, y + 5.0, 28.0, 12.5
        p.line(gx - 2.0, gy + gh + 1.5, gx + gw + 3.0, gy + gh + 1.5, color=INK, width=0.28)
        p.line(gx - 1.5, gy - 1.0, gx - 1.5, gy + gh + 2.5, color=INK, width=0.28)
        p.rect(gx + 2.0, gy + 1.5, 22.0, 9.0, fill=BLUE_FILL, stroke=INK, line_w=0.28)
        p.text(gx + 2.0, gy + 0.8, "(2,8)", size=1.45, bold=True, mono=True, color=INK, align="center")
        p.text(gx + 24.0, gy + 0.8, "(9,8)", size=1.45, bold=True, mono=True, color=INK, align="center")
        p.text(gx + 2.0, gy + 12.6, "(2,3)", size=1.40, bold=True, mono=True, color=SLATE, align="center")
        p.text(gx + 24.0, gy + 12.6, "(9,3)", size=1.40, bold=True, mono=True, color=SLATE, align="center")
        p.text(gx + 13.0, gy + 6.8, "w = 9-2 = 7, h = 8-3 = 5", size=1.52, bold=True, mono=True, color=INK, align="center")
        p.text(x + 21.5, y + h - 1.5, "P = 2(7+5) = 24  |  Area = 35", size=1.58, bold=True, mono=True, color=TEAL, align="center")

        p.line(mid_x, y + 1.5, mid_x, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        rx = mid_x + 21.5
        p.text(rx, y + 3.0, "Elapsed Time (Base-60: 1 hr = 60 min)", size=1.65, bold=True, color=TEAL, align="center")
        cx, cy, r_c = mid_x + 10.5, y + 11.8, 6.2
        p.circle(cx, cy, r_c, fill=SUBTLE_HDR, stroke=INK, line_w=0.28)
        for hr in range(12):
            ang = math.radians(hr * 30 - 90)
            p.line(cx + (r_c - 1.0) * math.cos(ang), cy + (r_c - 1.0) * math.sin(ang), cx + r_c * math.cos(ang), cy + r_c * math.sin(ang), color=INK, width=0.2)
        p.line(cx, cy, cx + 3.4, cy - 1.5, color=INK, width=0.4)
        p.line(cx, cy, cx - 4.6, cy, color=TEAL, width=0.32)
        p.text(mid_x + 29.5, y + 8.8, "8:40 -> 9:00 (+20m)", size=1.5, bold=True, mono=True, color=INK, align="center")
        p.text(mid_x + 29.5, y + 12.2, "9:00 -> 12:30 (+3h 30m)", size=1.5, bold=True, mono=True, color=INK, align="center")
        p.text(mid_x + 29.5, y + 15.8, "Total = 3 hr 50 min", size=1.6, bold=True, mono=True, color=TEAL, align="center")
        p.text(rx, y + h - 1.5, "15 min = 0.25 hr  |  30 min = 0.5 hr", size=1.55, bold=True, mono=True, color=SLATE, align="center")

    # =========================================================================
    # UNIT 6: INTEGERS, RATIONAL NUMBERS & COORDINATE PLANE (6.1 - 6.5)
    # =========================================================================
    elif sec_num == "6.1":
        # Opposites on a Number Line + Zero-Pair Cancellation
        p.text(x + 23.0, y + 3.0, "Opposites on a Number Line (-15 and +15)", size=1.65, bold=True, color=INK, align="center")
        lx1, lx2, ny = x + 3.5, mid_x - 2.5, y + 12.2
        mx = (lx1 + lx2) / 2.0
        p.line(lx1, ny, lx2, ny, color=INK, width=0.32)
        for tx_pos, lbl, col in [(lx1 + 3.5, "-15", SLATE), (mx, "0", INK), (lx2 - 3.5, "+15", TEAL)]:
            p.line(tx_pos, ny - 1.3, tx_pos, ny + 1.3, color=INK, width=0.28)
            p.circle(tx_pos, ny, 1.0, fill=col, stroke=INK, line_w=0.2)
            p.text(tx_pos, ny + 3.8, lbl, size=1.65, bold=True, mono=True, color=col, align="center")
        p.text((lx1 + 3.5 + mx) / 2.0, ny - 2.4, "15 units", size=1.48, bold=True, color=SLATE, align="center")
        p.text((mx + lx2 - 3.5) / 2.0, ny - 2.4, "15 units", size=1.48, bold=True, color=TEAL, align="center")
        p.text(x + 23.0, y + h - 1.8, "Additive Inverses: -15 + 15 = 0", size=1.6, bold=True, mono=True, color=INK, align="center")

        p.line(mid_x, y + 1.5, mid_x, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        rx = mid_x + 21.5
        p.text(rx, y + 3.0, "Zero-Pair Cancellation: (+1)+(-1)=0", size=1.62, bold=True, color=TEAL, align="center")
        gx = mid_x + 6.5
        for i in range(4):
            cx = gx + i * 8.5
            p.circle(cx, y + 7.5, 2.3, fill=GOLD_FILL, stroke=INK, line_w=0.24)
            p.text(cx, y + 8.3, "+", size=1.9, bold=True, mono=True, color=INK, align="center")
            if i < 3:
                p.circle(cx, y + 13.8, 2.3, fill=RED_FILL, stroke=INK, line_w=0.24)
                p.text(cx, y + 14.6, "-", size=1.9, bold=True, mono=True, color=INK, align="center")
                p.rect(cx - 2.8, y + 4.8, 5.6, 11.8, fill=None, stroke=SLATE, r=0.9, line_w=0.2)
        p.text(rx, y + h - 1.8, "3 Zero Pairs cancel -> +1 Left!", size=1.6, bold=True, mono=True, color=TEAL, align="center")

    elif sec_num == "6.2":
        # Ordering Negative Integers (-18 vs -5) & Rationals (-4/5 vs -3/4) on a Horizontal Number Line
        p.text(mid_x, y + 3.0, "Comparing Negative Integers (-5 > -18) & Rationals (-0.75 > -0.80): Right Is Greater!", size=1.65, bold=True, color=INK, align="center")
        lx1, lx2, ny = x + 6.0, x + w - 6.0, y + 12.2
        p.line(lx1, ny, lx2, ny, color=INK, width=0.35)
        pts = [
            (-1.2, "-18 (or -1.2)", SLATE),
            (-0.80, "-4/5 (-0.80)", TEAL),
            (-0.52, "-5 (or -3/4 = -0.75)", INK),
            (0.0, "0", TEAL),
        ]
        for val, lbl, col in pts:
            px = lx1 + ((val - (-1.35)) / 1.45) * (lx2 - lx1)
            p.line(px, ny - 1.4, px, ny + 1.4, color=INK, width=0.28)
            p.circle(px, ny, 1.05, fill=col, stroke=INK, line_w=0.2)
            y_lbl = ny - 2.6 if val in (-0.80, 0.0) else ny + 4.2
            p.text(px, y_lbl, lbl, size=1.55, bold=True, mono=True, color=col, align="center")
        p.text(mid_x, y + h - 1.8, "-5 > -18 (since -5 is right of -18)   |   -3/4 (-0.75) > -4/5 (-0.80) (Closer to 0 = Greater!)", size=1.55, bold=True, mono=True, color=TEAL, align="center")

    elif sec_num == "6.3":
        # Absolute Value = Distance from 0 (Always >= 0)
        p.text(x + 25.0, y + 3.0, "Absolute Value |x| = Distance from 0 on the Number Line", size=1.65, bold=True, color=INK, align="center")
        lx1, lx2, ny = x + 4.0, mid_x + 5.0, y + 12.5
        z_x = lx1 + (lx2 - lx1) * 0.50
        p.line(lx1, ny, lx2, ny, color=INK, width=0.32)
        for px, lbl, col in [(lx1 + 2.5, "-14", SLATE), (z_x, "0", INK), (lx2 - 2.5, "+14", TEAL)]:
            p.line(px, ny - 1.3, px, ny + 1.3, color=INK, width=0.28)
            p.circle(px, ny, 1.0, fill=col, stroke=INK, line_w=0.2)
            p.text(px, ny + 3.8, lbl, size=1.65, bold=True, mono=True, color=col, align="center")
        p.text((lx1 + 2.5 + z_x) / 2.0, ny - 2.4, "|-14| = 14", size=1.58, bold=True, mono=True, color=SLATE, align="center")
        p.text((z_x + lx2 - 2.5) / 2.0, ny - 2.4, "|+14| = 14", size=1.58, bold=True, mono=True, color=TEAL, align="center")
        p.text(x + 25.0, y + h - 1.8, "Both -14 and +14 are 14 units from 0!", size=1.58, bold=True, mono=True, color=INK, align="center")

        p.line(mid_x + 7.5, y + 1.5, mid_x + 7.5, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)
        rx = mid_x + 25.5
        p.rect(mid_x + 9.0, y + 3.5, 33.0, 19.2, fill=SUBTLE_HDR, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx, y + 6.8, "Inside vs. Outside '-' Sign:", size=1.55, bold=True, color=TEAL, align="center")
        p.text(rx, y + 10.6, "|-14| = +14", size=1.8, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 14.4, "|14| = +14", size=1.8, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 18.4, "-|-14| = -14", size=1.8, bold=True, mono=True, color=SLATE, align="center")
        p.text(rx, y + 21.4, "(Evaluate | | bars first!)", size=1.42, bold=True, color=MUTED, align="center")

    elif sec_num == "6.4":
        # 4-Quadrant Coordinate Plane & Reflections Across Axes
        p.text(x + 23.0, y + 3.0, "Four-Quadrant Coordinate Plane", size=1.68, bold=True, color=INK, align="center")
        cx, cy = x + 23.0, y + 13.2
        span_x, span_y = 17.5, 8.2
        p.line(cx - span_x, cy, cx + span_x, cy, color=INK, width=0.32)
        p.line(cx, cy - span_y, cx, cy + span_y, color=INK, width=0.32)
        p.text(cx + 9.5, cy - 3.6, "QI (+, +)", size=1.58, bold=True, mono=True, color=INK, align="center")
        p.text(cx - 9.5, cy - 3.6, "QII (-, +)", size=1.58, bold=True, mono=True, color=SLATE, align="center")
        p.text(cx - 9.5, cy + 5.4, "QIII (-, -)", size=1.58, bold=True, mono=True, color=SLATE, align="center")
        p.text(cx + 9.5, cy + 5.4, "QIV (+, -)", size=1.58, bold=True, mono=True, color=INK, align="center")
        p.circle(cx - 7.0, cy - 2.0, 0.95, fill=TEAL, stroke=INK, line_w=0.2)
        p.circle(cx + 7.0, cy - 2.0, 0.95, fill=GOLD_FILL, stroke=INK, line_w=0.2)
        p.line(cx - 7.0, cy - 2.0, cx + 7.0, cy - 2.0, color=TEAL, width=0.24, dashed=True)

        p.line(mid_x + 1.0, y + 1.5, mid_x + 1.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)
        rx = mid_x + 22.0
        p.text(rx, y + 3.0, "Axis Reflection Rules", size=1.68, bold=True, color=TEAL, align="center")
        p.rect(mid_x + 3.0, y + 5.0, 38.0, 8.2, fill=BLUE_FILL, stroke=INK, r=0.5, line_w=0.22)
        p.text(rx, y + 8.0, "Reflect Across x-Axis:", size=1.58, bold=True, color=INK, align="center")
        p.text(rx, y + 11.2, "Keep x, flip y: (x, y) -> (x, -y)", size=1.58, bold=True, mono=True, color=TEAL, align="center")
        p.rect(mid_x + 3.0, y + 14.2, 38.0, 8.2, fill=GOLD_FILL, stroke=INK, r=0.5, line_w=0.22)
        p.text(rx, y + 17.2, "Reflect Across y-Axis:", size=1.58, bold=True, color=INK, align="center")
        p.text(rx, y + 20.4, "Flip x, keep y: (x, y) -> (-x, y)", size=1.58, bold=True, mono=True, color=INK, align="center")

    elif sec_num == "6.5":
        # Coordinate Plane Distance: Opposite Quadrants (-6,4) to (9,4) vs. Same Quadrant (-12,-3) to (-4,-3)
        p.text(mid_x, y + 3.0, "Coordinate Plane Distance: Crosses Axis -> ADD |x|   |   Same Side -> SUBTRACT |x|", size=1.65, bold=True, color=INK, align="center")
        # Left: Crosses y-axis (-6, 4) to (9, 4)
        p.rect(x + 2.5, y + 4.8, 39.0, 18.0, fill=BLUE_FILL, stroke=INK, r=0.6, line_w=0.22)
        p.text(x + 22.0, y + 7.8, "Different Quadrants (Crosses Axis):", size=1.58, bold=True, color=INK, align="center")
        p.text(x + 22.0, y + 11.4, "(-6, 4)  <--- y-axis --->  (9, 4)", size=1.62, bold=True, mono=True, color=TEAL, align="center")
        p.text(x + 22.0, y + 15.6, "ADD Distances: |-6| + |9| = 6 + 9 = 15", size=1.62, bold=True, mono=True, color=INK, align="center")
        p.text(x + 22.0, y + 19.8, "Coord Diff: |9 - (-6)| = |15| = 15 units", size=1.50, mono=True, color=SLATE, align="center")

        # Right: Same Quadrant (-12, -3) to (-4, -3)
        rx = mid_x + 2.0
        p.rect(rx, y + 4.8, 39.0, 18.0, fill=GOLD_FILL, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx + 19.5, y + 7.8, "Same Quadrant (Same Side of Axis):", size=1.58, bold=True, color=INK, align="center")
        p.text(rx + 19.5, y + 11.4, "(-12, -3)  and  (-4, -3)  in Quad III", size=1.60, bold=True, mono=True, color=SLATE, align="center")
        p.text(rx + 19.5, y + 15.6, "SUBTRACT: |-12| - |-4| = 12 - 4 = 8", size=1.62, bold=True, mono=True, color=TEAL, align="center")
        p.text(rx + 19.5, y + 19.8, "Coord Diff: |-4 - (-12)| = |8| = 8 units", size=1.50, mono=True, color=SLATE, align="center")

    # =========================================================================
    # UNIT 7: EQUATIONS & INEQUALITIES (7.1 - 7.5)
    # =========================================================================
    elif sec_num in ("7.1", "7.2", "7.3"):
        # Equation Balance Scale + Part-Whole Bar / Equal-Box Tape Model
        if sec_num == "7.1":
            l_pan, r_pan, step_txt, bar_title, bar_sub = (
                "4x + 5",
                "41",
                "At x = 9: 4(9) + 5 = 41 (Balanced!)",
                "Equation Translation Keywords",
                "'is/equals' -> =  |  '12 less than k' -> k - 12",
            )
        elif sec_num == "7.2":
            l_pan, r_pan, step_txt, bar_title, bar_sub = (
                "x + 28  (-28)",
                "73  (-28)",
                "Remove 28 from BOTH pans -> x = 45",
                "Part-Whole Bar Model (x + 28 = 73)",
                "[   x = 45   |  28  ]  <-- Total = 73",
            )
        else:
            l_pan, r_pan, step_txt, bar_title, bar_sub = (
                "8 x-boxes (÷8)",
                "136 units (÷8)",
                "Divide both sides by 8 -> x = 17",
                "Equal-Box Tape Model (8x = 136)",
                "8 boxes = 136  ->  1 box = 136 ÷ 8 = 17",
            )

        p.text(x + 22.0, y + 3.0, f"Balance Scale Model: {l_pan} = {r_pan}", size=1.62, bold=True, color=INK, align="center")
        cx, by = x + 22.0, y + 14.5
        p.line(x + 4.0, by, x + 40.0, by, color=INK, width=0.42)
        p.polygon([(cx, by), (cx - 2.4, by + 3.4), (cx + 2.4, by + 3.4)], fill=INK, stroke=INK)
        p.rect(x + 3.5, y + 5.5, 16.0, 7.6, fill=GREEN_FILL, stroke=INK, r=0.5, line_w=0.24)
        p.text(x + 11.5, y + 10.0, l_pan, size=1.62, bold=True, mono=True, color=INK, align="center")
        p.rect(x + 24.5, y + 5.5, 16.0, 7.6, fill=GOLD_FILL, stroke=INK, r=0.5, line_w=0.24)
        p.text(x + 32.5, y + 10.0, r_pan, size=1.62, bold=True, mono=True, color=INK, align="center")
        p.text(cx, y + h - 1.8, step_txt, size=1.55, bold=True, color=TEAL, align="center")

        p.line(mid_x, y + 1.5, mid_x, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)
        rx = mid_x + 21.5
        p.text(rx, y + 3.0, bar_title, size=1.65, bold=True, color=TEAL, align="center")
        p.rect(mid_x + 2.5, y + 5.5, 38.0, 16.8, fill=SUBTLE_HDR, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx, y + 10.2, bar_sub, size=1.58, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 15.2, "Inverse Operations Undo Each Other:", size=1.52, bold=True, color=SLATE, align="center")
        p.text(rx, y + 19.0, "+ <-> -     and     × <-> ÷ (or × b/a)", size=1.58, bold=True, mono=True, color=TEAL, align="center")

    elif sec_num == "7.4":
        # Inequality Number Line Graphs: Open Circle (<, >) vs. Solid Dot (<=, >=)
        p.text(mid_x, y + 3.0, "Graphing Inequalities on a Number Line: Open Circle (○) vs. Solid Dot (●)", size=1.68, bold=True, color=INK, align="center")
        # Left: Open Circle x > 19 or x < 19
        p.rect(x + 2.5, y + 4.8, 39.0, 18.0, fill=SUBTLE_HDR, stroke=INK, r=0.6, line_w=0.22)
        p.text(x + 22.0, y + 7.8, "Strict (< or >): OPEN Circle (○)", size=1.62, bold=True, color=INK, align="center")
        ny1 = y + 13.8
        p.line(x + 6.0, ny1, x + 38.0, ny1, color=INK, width=0.28)
        p.line(x + 18.0, ny1, x + 37.5, ny1, color=TEAL, width=0.75)
        p.circle(x + 18.0, ny1, 1.35, fill=WHITE, stroke=TEAL, line_w=0.38)
        p.text(x + 18.0, ny1 + 3.8, "19 (Not included)", size=1.5, bold=True, mono=True, color=SLATE, align="center")
        p.text(x + 22.0, y + 20.8, "x > 19  ('more than' / 'fewer than')", size=1.52, bold=True, color=TEAL, align="center")

        # Right: Solid Dot x >= 19
        rx = mid_x + 2.0
        p.rect(rx, y + 4.8, 39.0, 18.0, fill=BLUE_FILL, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx + 19.5, y + 7.8, "Inclusive (≤ or ≥): SOLID Dot (●)", size=1.62, bold=True, color=TEAL, align="center")
        p.line(rx + 3.5, ny1, rx + 35.5, ny1, color=INK, width=0.28)
        p.line(rx + 15.5, ny1, rx + 35.0, ny1, color=TEAL, width=0.75)
        p.circle(rx + 15.5, ny1, 1.35, fill=TEAL, stroke=INK, line_w=0.3)
        p.text(rx + 15.5, ny1 + 3.8, "19 (IS a solution!)", size=1.5, bold=True, mono=True, color=INK, align="center")
        p.text(rx + 19.5, y + 20.8, "x ≥ 19  ('at least' ≥  |  'at most' ≤)", size=1.52, bold=True, color=INK, align="center")

    elif sec_num == "7.5":
        # Two-Variable Equations: Multiplicative (y = kx) vs. Additive (y = x + b)
        p.text(mid_x, y + 3.0, "Two-Variable Equations: Independent Input (x) -> Dependent Output (y)", size=1.68, bold=True, color=INK, align="center")
        p.rect(x + 2.5, y + 4.8, 39.0, 18.0, fill=GREEN_FILL, stroke=INK, r=0.6, line_w=0.22)
        p.text(x + 22.0, y + 8.0, "Multiplicative: y = kx (e.g., y = 7x)", size=1.62, bold=True, color=INK, align="center")
        p.text(x + 22.0, y + 11.8, "Constant Ratio: y ÷ x = 7", size=1.62, bold=True, mono=True, color=TEAL, align="center")
        p.text(x + 22.0, y + 15.6, "(1, 7), (2, 14), (3, 21), (4, 28)", size=1.55, mono=True, color=INK, align="center")
        p.text(x + 22.0, y + 19.8, "Graph is a line through origin (0, 0)!", size=1.52, bold=True, color=SLATE, align="center")

        rx = mid_x + 2.0
        p.rect(rx, y + 4.8, 39.0, 18.0, fill=GOLD_FILL, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx + 19.5, y + 8.0, "Additive: y = x + b (e.g., y = x - 4)", size=1.62, bold=True, color=INK, align="center")
        p.text(rx + 19.5, y + 11.8, "Constant Difference: y - x = -4", size=1.62, bold=True, mono=True, color=TEAL, align="center")
        p.text(rx + 19.5, y + 15.6, "(10, 6), (12, 8), (15, 11), (20, 16)", size=1.55, mono=True, color=INK, align="center")
        p.text(rx + 19.5, y + 19.8, "Graph crosses y-axis at (0, b)!", size=1.52, bold=True, color=SLATE, align="center")

    # =========================================================================
    # UNIT 8: SURFACE AREA & VOLUME OF 3D SOLIDS (8.1 - 8.4)
    # =========================================================================
    elif sec_num == "8.1":
        # 3D Rectangular Prism (8×5×3) Unfolding into 6-Face 2D Net
        p.text(x + 19.0, y + 3.0, "3D Prism (8×5×3 cm)", size=1.65, bold=True, color=INK, align="center")
        bx, by, bw, bh = x + 6.0, y + 8.2, 16.0, 9.5
        dx, dy = 4.5, -3.2
        p.rect(bx, by, bw, bh, fill=BLUE_FILL, stroke=INK, line_w=0.26)
        p.polygon([(bx, by), (bx + dx, by + dy), (bx + bw + dx, by + dy), (bx + bw, by)], fill=GREEN_FILL, stroke=INK, line_w=0.24)
        p.polygon([(bx + bw, by), (bx + bw + dx, by + dy), (bx + bw + dx, by + bh + dy), (bx + bw, by + bh)], fill=GOLD_FILL, stroke=INK, line_w=0.24)
        p.text(bx + bw / 2.0, by + 5.6, "Front 8×3", size=1.52, bold=True, mono=True, color=INK, align="center")
        p.text(x + 19.0, y + h - 1.6, "SA = 2(40+24+15) = 158", size=1.55, bold=True, mono=True, color=TEAL, align="center")

        p.line(x + 36.0, y + 1.5, x + 36.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        # Right: Unfolded 6-Face Net
        nx, ny = x + 52.5, y + 8.6
        p.text(x + 61.0, y + 3.0, "Way 1: Unfolded 6-Face 2D Net", size=1.65, bold=True, color=TEAL, align="center")
        p.rect(nx, ny, 14.0, 4.4, fill=BLUE_FILL, stroke=INK, line_w=0.24)
        p.text(nx + 7.0, ny + 2.8, "Bottom (40)", size=1.42, bold=True, mono=True, color=INK, align="center")
        p.rect(nx, ny - 3.6, 14.0, 3.6, fill=GREEN_FILL, stroke=INK, line_w=0.24)
        p.text(nx + 7.0, ny - 1.2, "Back (24)", size=1.38, bold=True, mono=True, color=INK, align="center")
        p.rect(nx, ny + 4.4, 14.0, 3.6, fill=GREEN_FILL, stroke=INK, line_w=0.24)
        p.text(nx + 7.0, ny + 6.8, "Front (24)", size=1.38, bold=True, mono=True, color=INK, align="center")
        p.rect(nx, ny + 8.0, 14.0, 4.4, fill=BLUE_FILL, stroke=INK, line_w=0.24)
        p.text(nx + 7.0, ny + 10.8, "Top (40)", size=1.42, bold=True, mono=True, color=INK, align="center")
        p.rect(nx - 6.8, ny, 6.8, 4.4, fill=GOLD_FILL, stroke=INK, line_w=0.24)
        p.text(nx - 3.4, ny + 2.8, "L(15)", size=1.35, bold=True, mono=True, color=INK, align="center")
        p.rect(nx + 14.0, ny, 6.8, 4.4, fill=GOLD_FILL, stroke=INK, line_w=0.24)
        p.text(nx + 17.4, ny + 2.8, "R(15)", size=1.35, bold=True, mono=True, color=INK, align="center")

    elif sec_num == "8.2":
        # Left: Triangular Prism Net (2 Triangles + 3 Rectangles) | Right: Square Pyramid Star Net
        p.text(x + 21.5, y + 3.0, "Triangular Prism Net (5 Faces)", size=1.65, bold=True, color=INK, align="center")
        px, py = x + 15.0, y + 9.2
        p.rect(px, py, 13.0, 6.5, fill=BLUE_FILL, stroke=INK, line_w=0.24)
        p.rect(px - 8.5, py, 8.5, 6.5, fill=GREEN_FILL, stroke=INK, line_w=0.24)
        p.rect(px + 13.0, py, 8.5, 6.5, fill=GREEN_FILL, stroke=INK, line_w=0.24)
        p.polygon([(px, py), (px + 13.0, py), (px + 6.5, py - 4.2)], fill=GOLD_FILL, stroke=INK, line_w=0.24)
        p.polygon([(px, py + 6.5), (px + 13.0, py + 6.5), (px + 6.5, py + 10.7)], fill=GOLD_FILL, stroke=INK, line_w=0.24)
        p.text(x + 21.5, y + h - 1.5, "SA = 2 Tri Bases (½bh) + 3 Rect Sides", size=1.52, bold=True, color=TEAL, align="center")

        p.line(mid_x, y + 1.5, mid_x, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        rx = mid_x + 21.5
        p.text(rx, y + 3.0, "Square Pyramid Net (1 Base + 4 Triangles)", size=1.65, bold=True, color=TEAL, align="center")
        sx, sy, bs = rx - 4.0, y + 9.6, 8.0
        p.rect(sx, sy, bs, bs, fill=BLUE_FILL, stroke=INK, line_w=0.26)
        p.text(sx + 4.0, sy + 4.8, "B=s²", size=1.55, bold=True, mono=True, color=INK, align="center")
        p.polygon([(sx, sy), (sx + bs, sy), (sx + 4.0, sy - 4.8)], fill=GOLD_FILL, stroke=INK, line_w=0.24)
        p.polygon([(sx, sy + bs), (sx + bs, sy + bs), (sx + 4.0, sy + bs + 4.8)], fill=GOLD_FILL, stroke=INK, line_w=0.24)
        p.polygon([(sx, sy), (sx, sy + bs), (sx - 5.2, sy + 4.0)], fill=GOLD_FILL, stroke=INK, line_w=0.24)
        p.polygon([(sx + bs, sy), (sx + bs, sy + bs), (sx + bs + 5.2, sy + 4.0)], fill=GOLD_FILL, stroke=INK, line_w=0.24)
        p.text(rx, y + h - 1.5, "SA = Base B + 4(½ × b × slant l)", size=1.52, bold=True, color=INK, align="center")

    elif sec_num == "8.3":
        # Volume of Rectangular Prism: Layer Packing (B = l×w stacked h layers)
        p.text(x + 23.0, y + 3.0, "Unit-Cube Layer Packing (V = Bh)", size=1.68, bold=True, color=INK, align="center")
        bx, by, bw, bh = x + 7.5, y + 7.8, 22.0, 10.5
        dx, dy = 6.0, -3.6
        p.rect(bx, by, bw, bh, fill=BLUE_FILL, stroke=INK, line_w=0.28)
        p.polygon([(bx, by), (bx + dx, by + dy), (bx + bw + dx, by + dy), (bx + bw, by)], fill=GREEN_FILL, stroke=INK, line_w=0.25)
        p.polygon([(bx + bw, by), (bx + bw + dx, by + dy), (bx + bw + dx, by + bh + dy), (bx + bw, by + bh)], fill=GOLD_FILL, stroke=INK, line_w=0.25)
        # Grid lines on front face (4 cols × 3 layers)
        for c_i in range(1, 4):
            p.line(bx + c_i * (bw / 4.0), by, bx + c_i * (bw / 4.0), by + bh, color=INK, width=0.18)
        for r_i in range(1, 3):
            p.line(bx, by + r_i * (bh / 3.0), bx + bw, by + r_i * (bh / 3.0), color=INK, width=0.18)
        p.text(bx + bw / 2.0, y + h - 1.6, "Base B = 12×8 = 96  |  × 5 layers = 480 in³", size=1.55, bold=True, mono=True, color=TEAL, align="center")

        p.line(mid_x + 2.0, y + 1.5, mid_x + 2.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)
        rx = mid_x + 22.5
        p.rect(mid_x + 4.0, y + 4.2, 37.0, 18.8, fill=SUBTLE_HDR, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx, y + 7.6, "3 Ways to Find Prism Volume:", size=1.6, bold=True, color=TEAL, align="center")
        p.text(rx, y + 11.4, "Way 1 (Layers): V = Base Area B × h", size=1.55, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 15.0, "Way 2 (Formula): V = l × w × h", size=1.55, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 18.6, "Missing Height: h = V ÷ (l × w)", size=1.55, bold=True, mono=True, color=TEAL, align="center")
        p.text(rx, y + 21.6, "(Wait: 1/2-in cubes -> 8 fit per 1 in³!)", size=1.42, bold=True, color=SLATE, align="center")

    elif sec_num == "8.4":
        # 3 Panels: Circle Area (A = pi r^2) | Cone Volume (V = 1/3 pi r^2 h) | Right Triangle (a^2 + b^2 = c^2)
        w3 = w / 3.0
        # Col 1: Circle
        c1x = x + w3 * 0.5
        p.text(c1x, y + 3.0, "Circle: A = πr²", size=1.65, bold=True, color=INK, align="center")
        p.circle(c1x, y + 11.8, 6.2, fill=BLUE_FILL, stroke=INK, line_w=0.28)
        p.line(c1x, y + 11.8, c1x + 6.2, y + 11.8, color=TEAL, width=0.35)
        p.circle(c1x, y + 11.8, 0.7, fill=INK, stroke=INK)
        p.text(c1x + 3.1, y + 10.8, "r=6", size=1.55, bold=True, mono=True, color=TEAL, align="center")
        p.text(c1x, y + h - 1.5, "r = d ÷ 2  |  36π ≈ 113.10", size=1.48, bold=True, mono=True, color=INK, align="center")

        p.line(x + w3, y + 1.5, x + w3, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        # Col 2: Cone
        c2x = x + w3 * 1.5
        p.text(c2x, y + 3.0, "Cone: V = ⅓πr²h", size=1.65, bold=True, color=TEAL, align="center")
        p.polygon([(c2x - 6.5, y + 16.5), (c2x + 6.5, y + 16.5), (c2x, y + 5.8)], fill=GOLD_FILL, stroke=INK, line_w=0.26)
        p.line(c2x, y + 5.8, c2x, y + 16.5, color=TEAL, width=0.28, dashed=True)
        p.text(c2x + 2.2, y + 12.5, "h", size=1.6, bold=True, mono=True, color=TEAL)
        p.text(c2x, y + h - 1.5, "Cone = 1/3 of Cylinder!", size=1.48, bold=True, color=INK, align="center")

        p.line(x + w3 * 2, y + 1.5, x + w3 * 2, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        # Col 3: Right Triangle Pythagorean Theorem
        c3x = x + w3 * 2.5
        p.text(c3x, y + 3.0, "Right Triangle: a²+b²=c²", size=1.62, bold=True, color=INK, align="center")
        tx, ty = c3x - 7.5, y + 6.2
        p.polygon([(tx, ty + 11.0), (tx + 14.5, ty + 11.0), (tx, ty)], fill=GREEN_FILL, stroke=INK, line_w=0.28)
        p.rect(tx, ty + 9.2, 1.8, 1.8, fill=None, stroke=INK, line_w=0.2)
        p.text(tx - 1.8, ty + 6.2, "a=5", size=1.5, bold=True, mono=True, color=INK, align="right")
        p.text(tx + 7.2, ty + 13.4, "b=12", size=1.5, bold=True, mono=True, color=INK, align="center")
        p.text(tx + 9.2, ty + 5.2, "c=13", size=1.55, bold=True, mono=True, color=TEAL)
        p.text(c3x, y + h - 1.5, "c = √(5²+12²) = √169 = 13", size=1.45, bold=True, mono=True, color=TEAL, align="center")

    # =========================================================================
    # UNIT 9: STATISTICAL MEASURES & DATA DISPLAYS (9.1 - 9.4)
    # =========================================================================
    elif sec_num == "9.1":
        # Left: Fair-Share Block Leveling Towers | Right: Balance Point on Dot Plot
        p.text(x + 22.0, y + 3.0, "Way 2: Fair-Share Tower Leveling", size=1.65, bold=True, color=INK, align="center")
        towers = [18, 24, 15, 27, 21]
        base_y = y + 19.5
        scale = 12.5 / 27.0
        for idx, tv in enumerate(towers):
            tx = x + 4.5 + idx * 7.2
            th = tv * scale
            p.rect(tx, base_y - th, 5.0, th, fill=BLUE_FILL, stroke=INK, r=0.3, line_w=0.22)
            p.text(tx + 2.5, base_y + 2.5, str(tv), size=1.55, bold=True, mono=True, color=INK, align="center")
        my = base_y - 21 * scale
        p.line(x + 2.5, my, x + 41.5, my, color=TEAL, width=0.38, dashed=True)
        p.text(x + 22.0, y + h - 1.2, "Leveled Height = Mean = 21", size=1.55, bold=True, mono=True, color=TEAL, align="center")

        p.line(mid_x + 1.0, y + 1.5, mid_x + 1.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        rx = mid_x + 22.0
        p.text(rx, y + 3.0, "Way 1 & 3: Mean Formula & Balance Point", size=1.62, bold=True, color=TEAL, align="center")
        p.rect(mid_x + 3.0, y + 4.8, 38.0, 18.0, fill=SUBTLE_HDR, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx, y + 8.4, "Way 1: Sum ÷ Count = 105 ÷ 5 = 21", size=1.62, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 12.4, "Way 3 (Dot Plot Balance at 21):", size=1.55, bold=True, color=TEAL, align="center")
        p.text(rx, y + 16.0, "Left: (21-15) + (21-18) = 6 + 3 = 9", size=1.52, mono=True, color=SLATE, align="center")
        p.text(rx, y + 19.6, "Right: (24-21) + (27-21) = 3 + 6 = 9", size=1.52, mono=True, color=SLATE, align="center")

    elif sec_num == "9.2":
        # Ordered Data Strip showing Median (middle), Mode (most frequent), and Range (Max - Min)
        p.text(mid_x, y + 3.0, "Measures of Center & Variation: ALWAYS Order Data Least to Greatest First!", size=1.68, bold=True, color=INK, align="center")
        vals = ["6", "7", "7", "7", "8", "8", "9", "10"]
        bx0 = x + 5.5
        bw = 9.0
        for i, v in enumerate(vals):
            cx = bx0 + i * (bw + 0.5)
            is_med = i in (3, 4)
            is_mode = v == "7"
            fill_c = GOLD_FILL if is_med else (BLUE_FILL if is_mode else WHITE)
            p.rect(cx, y + 5.5, bw, 6.2, fill=fill_c, stroke=INK, r=0.45, line_w=0.24)
            p.text(cx + bw / 2.0, y + 9.4, v, size=1.95, bold=True, mono=True, color=INK, align="center")
        # Brackets / Callouts below
        p.text(bx0 + 2.0 * (bw + 0.5), y + 15.2, "Mode = 7 (Most frequent: 3 times)", size=1.58, bold=True, color=INK, align="center")
        p.text(bx0 + 4.2 * (bw + 0.5), y + 18.6, "Median (Even n=8): (7 + 8) ÷ 2 = 7.5", size=1.62, bold=True, mono=True, color=TEAL, align="center")
        p.text(mid_x, y + h - 1.6, "Range = Max - Min = 10 - 6 = 4   |   Use Median when an Outlier skews the Mean!", size=1.58, bold=True, color=SLATE, align="center")

    elif sec_num == "9.3":
        # Full-Width Annotated Box-and-Whisker Plot showing Min, Q1, Med, Q3, Max, 25% quarters, and IQR
        p.text(mid_x, y + 3.0, "Box-and-Whisker Plot: 5-Number Summary & Interquartile Range (IQR = Q₃ - Q₁)", size=1.68, bold=True, color=INK, align="center")
        by = y + 11.2
        x_min, x_q1, x_med, x_q3, x_max = x + 8.0, x + 24.0, x + 43.0, x + 62.0, x + 78.0
        # Whiskers
        p.line(x_min, by, x_q1, by, color=INK, width=0.38)
        p.line(x_q3, by, x_max, by, color=INK, width=0.38)
        p.line(x_min, by - 2.5, x_min, by + 2.5, color=INK, width=0.38)
        p.line(x_max, by - 2.5, x_max, by + 2.5, color=INK, width=0.38)
        # Middle 50% Box
        p.rect(x_q1, by - 3.8, x_q3 - x_q1, 7.6, fill=BLUE_FILL, stroke=INK, line_w=0.32)
        p.line(x_med, by - 3.8, x_med, by + 3.8, color=TEAL, width=0.5)
        # 25% labels
        p.text((x_min + x_q1) / 2.0, by - 1.5, "25%", size=1.45, bold=True, color=SLATE, align="center")
        p.text((x_q1 + x_med) / 2.0, by + 0.6, "25%", size=1.5, bold=True, color=INK, align="center")
        p.text((x_med + x_q3) / 2.0, by + 0.6, "25%", size=1.5, bold=True, color=INK, align="center")
        p.text((x_q3 + x_max) / 2.0, by - 1.5, "25%", size=1.45, bold=True, color=SLATE, align="center")
        # 5-Number labels
        for px, lbl, col in [
            (x_min, "Min (68)", INK),
            (x_q1, "Q₁ (73.5)", TEAL),
            (x_med, "Med (82)", TEAL),
            (x_q3, "Q₃ (90)", TEAL),
            (x_max, "Max (96)", INK),
        ]:
            p.text(px, by + 6.4, lbl, size=1.52, bold=True, mono=True, color=col, align="center")
        p.text(mid_x, y + h - 1.6, "Middle 50% Box = IQR = Q₃ - Q₁ = 90 - 73.5 = 16.5   |   Range = Max - Min = 28", size=1.58, bold=True, mono=True, color=TEAL, align="center")

    elif sec_num == "9.4":
        # 3-Step MAD Diagram: Distances |x - Mean| from the Mean for {10, 12, 14, 16, 18} (Mean = 14)
        p.text(mid_x, y + 3.0, "Mean Absolute Deviation (MAD): Average Distance of Data Values from the Mean", size=1.68, bold=True, color=INK, align="center")
        p.rect(x + 2.5, y + 4.8, 43.0, 18.0, fill=SUBTLE_HDR, stroke=INK, r=0.6, line_w=0.22)
        p.text(x + 24.0, y + 7.8, "Data: {10, 12, 14, 16, 18}  ->  Mean = 14", size=1.58, bold=True, mono=True, color=INK, align="center")
        ny = y + 13.5
        lx1, lx2 = x + 6.5, x + 41.5
        p.line(lx1, ny, lx2, ny, color=INK, width=0.3)
        for idx, (val, dist) in enumerate([(10, "4"), (12, "2"), (14, "0"), (16, "2"), (18, "4")]):
            px = lx1 + idx * ((lx2 - lx1) / 4.0)
            p.circle(px, ny, 1.05, fill=TEAL if val == 14 else BLUE_FILL, stroke=INK, line_w=0.22)
            p.text(px, ny + 3.5, str(val), size=1.55, bold=True, mono=True, color=INK, align="center")
            p.text(px, ny - 2.0, f"d={dist}", size=1.42, bold=True, mono=True, color=TEAL, align="center")
        p.text(x + 24.0, y + 20.8, "Distances |x - 14|: 4, 2, 0, 2, 4", size=1.52, bold=True, color=TEAL, align="center")

        rx = x + 47.5
        rw = w - 50.0
        p.rect(rx, y + 4.8, rw, 18.0, fill=GOLD_FILL, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx + rw / 2.0, y + 8.0, "3-Step MAD Recipe:", size=1.6, bold=True, color=INK, align="center")
        p.text(rx + rw / 2.0, y + 11.4, "1. Find Mean = 70 ÷ 5 = 14", size=1.5, bold=True, mono=True, color=INK, align="center")
        p.text(rx + rw / 2.0, y + 14.8, "2. Sum |x - 14| = 4+2+0+2+4 = 12", size=1.48, bold=True, mono=True, color=TEAL, align="center")
        p.text(rx + rw / 2.0, y + 18.2, "3. MAD = 12 ÷ 5 = 2.4", size=1.65, bold=True, mono=True, color=INK, align="center")
        p.text(rx + rw / 2.0, y + 21.2, "(Smaller MAD = More Consistent!)", size=1.4, bold=True, color=SLATE, align="center")

    # =========================================================================
    # UNIT 10: GRADE 7 BRIDGE — SIGNED RATIONALS, 2-STEP & PROBABILITY (10.1 - 10.4)
    # =========================================================================
    elif sec_num == "10.1":
        # Signed Addition/Subtraction: Zero-Pair Counters (-8 + 5 = -3) + Add the Opposite
        p.text(x + 24.0, y + 3.0, "Way 2: Zero-Pair Counters (-8 + 5 = -3)", size=1.65, bold=True, color=INK, align="center")
        gx = x + 3.5
        for i in range(8):
            cx = gx + i * 5.2
            p.circle(cx, y + 7.4, 2.0, fill=RED_FILL, stroke=INK, line_w=0.22)
            p.text(cx, y + 8.1, "-", size=1.75, bold=True, mono=True, color=INK, align="center")
            if i < 5:
                p.circle(cx, y + 12.8, 2.0, fill=GOLD_FILL, stroke=INK, line_w=0.22)
                p.text(cx, y + 13.5, "+", size=1.75, bold=True, mono=True, color=INK, align="center")
                p.rect(cx - 2.35, y + 5.0, 4.7, 10.2, fill=None, stroke=SLATE, r=0.7, line_w=0.18)
        p.text(x + 24.0, y + 18.2, "5 Zero Pairs cancel -> 3 Red (-) left = -3", size=1.55, bold=True, color=TEAL, align="center")
        p.text(x + 24.0, y + h - 1.6, "Same Signs: Add |x|  |  Diff Signs: Subtract |x|", size=1.5, bold=True, color=SLATE, align="center")

        p.line(mid_x + 3.0, y + 1.5, mid_x + 3.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)
        rx = mid_x + 23.0
        p.rect(mid_x + 4.5, y + 4.0, 36.5, 19.0, fill=SUBTLE_HDR, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx, y + 7.4, "Subtracting = Add the Opposite!", size=1.58, bold=True, color=TEAL, align="center")
        p.text(rx, y + 11.4, "a - b  =  a + (-b)", size=1.75, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 15.2, "a - (-b)  =  a + b", size=1.75, bold=True, mono=True, color=TEAL, align="center")
        p.text(rx, y + 19.6, "Ex: 10 - (-4) = 10 + 4 = 14", size=1.58, bold=True, mono=True, color=INK, align="center")

    elif sec_num == "10.2":
        # Multiplying & Dividing Signed Numbers: Sign Rules Table + Counter Flip Model
        p.text(x + 22.0, y + 3.0, "Sign Rules for × and ÷", size=1.68, bold=True, color=INK, align="center")
        p.rect(x + 2.5, y + 4.8, 39.0, 8.6, fill=GREEN_FILL, stroke=INK, r=0.5, line_w=0.22)
        p.text(x + 22.0, y + 8.0, "SAME Signs -> POSITIVE (+)", size=1.62, bold=True, color=INK, align="center")
        p.text(x + 22.0, y + 11.4, "(+) × (+) = +    |    (-) × (-) = +", size=1.58, bold=True, mono=True, color=TEAL, align="center")
        p.rect(x + 2.5, y + 14.2, 39.0, 8.6, fill=RED_FILL, stroke=INK, r=0.5, line_w=0.22)
        p.text(x + 22.0, y + 17.4, "DIFFERENT Signs -> NEGATIVE (-)", size=1.62, bold=True, color=INK, align="center")
        p.text(x + 22.0, y + 20.8, "(+) × (-) = -    |    (-) × (+) = -", size=1.58, bold=True, mono=True, color=SLATE, align="center")

        p.line(mid_x + 0.5, y + 1.5, mid_x + 0.5, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)
        rx = mid_x + 22.0
        p.text(rx, y + 3.0, "Multi-Factor & Power Sign Rule", size=1.68, bold=True, color=TEAL, align="center")
        p.rect(mid_x + 2.5, y + 4.8, 39.0, 18.0, fill=SUBTLE_HDR, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx, y + 8.6, "EVEN # of negatives -> Positive (+)", size=1.55, bold=True, color=TEAL, align="center")
        p.text(rx, y + 12.2, "Ex: (-5)² = (-5) × (-5) = +25", size=1.62, bold=True, mono=True, color=INK, align="center")
        p.text(rx, y + 16.4, "ODD # of negatives -> Negative (-)", size=1.55, bold=True, color=SLATE, align="center")
        p.text(rx, y + 20.0, "Ex: (-2)³ = (-2)(-2)(-2) = -8", size=1.62, bold=True, mono=True, color=INK, align="center")

    elif sec_num == "10.3":
        # Two-Step Balance Scale for 3x + 7 = 28 -> 3x = 21 -> x = 7
        p.text(mid_x, y + 3.0, "Two-Step Equation Balance Scale: Solve 3x + 7 = 28 in 2 Steps", size=1.68, bold=True, color=INK, align="center")
        # Step 1 box
        p.rect(x + 2.5, y + 4.8, 39.0, 18.0, fill=GREEN_FILL, stroke=INK, r=0.6, line_w=0.22)
        p.text(x + 22.0, y + 8.0, "Step 1: Undo + or - FIRST", size=1.65, bold=True, color=INK, align="center")
        p.text(x + 22.0, y + 11.8, "Remove 7 loose cubes from both pans:", size=1.5, color=SLATE, align="center")
        p.text(x + 22.0, y + 15.6, "3x + 7 - 7  =  28 - 7", size=1.72, bold=True, mono=True, color=TEAL, align="center")
        p.text(x + 22.0, y + 19.8, "3x  =  21", size=1.9, bold=True, mono=True, color=INK, align="center")

        # Step 2 box
        rx = mid_x + 2.0
        p.rect(rx, y + 4.8, 39.0, 18.0, fill=BLUE_FILL, stroke=INK, r=0.6, line_w=0.22)
        p.text(rx + 19.5, y + 8.0, "Step 2: Undo × or ÷ SECOND", size=1.65, bold=True, color=TEAL, align="center")
        p.text(rx + 19.5, y + 11.8, "Divide 21 cubes equally into 3 x-boxes:", size=1.5, color=SLATE, align="center")
        p.text(rx + 19.5, y + 15.6, "3x ÷ 3  =  21 ÷ 3", size=1.72, bold=True, mono=True, color=INK, align="center")
        p.text(rx + 19.5, y + 19.8, "x = 7   (Check: 3(7)+7 = 28!)", size=1.75, bold=True, mono=True, color=TEAL, align="center")

    else:  # 10.4
        # Theoretical Probability Fraction Ratios + Permutations (nPr) vs. Combinations (nCr)
        p.text(x + 19.5, y + 3.0, "Probability Ratio (FRAC-01)", size=1.68, bold=True, color=INK, align="center")
        cx, cy, r_s = x + 13.5, y + 11.8, 6.2
        p.circle(cx, cy, r_s, fill=BLUE_FILL, stroke=INK, line_w=0.28)
        for s_i in range(10):
            ang = math.radians(s_i * 36 - 90)
            p.line(cx, cy, cx + r_s * math.cos(ang), cy + r_s * math.sin(ang), color=INK, width=0.2)
        p.line(cx, cy, cx + 4.0, cy - 2.6, color=TEAL, width=0.42)
        p.text(x + 28.5, y + 9.2, "P(Blue) = 4/10", size=1.58, bold=True, mono=True, color=INK, align="center")
        p.text(x + 28.5, y + 12.6, "= 2/5 = 40%", size=1.62, bold=True, mono=True, color=TEAL, align="center")
        p.text(x + 28.5, y + 16.2, "P(not E) = 1 - P(E)", size=1.45, bold=True, mono=True, color=SLATE, align="center")
        p.text(x + 19.5, y + h - 1.5, "P(E) = Favorable ÷ Total", size=1.52, bold=True, color=INK, align="center")

        p.line(x + 39.0, y + 1.5, x + 39.0, y + h - 1.5, color=LIGHT_BORDER, width=0.22, dashed=True)

        rx = x + 61.5
        p.text(rx, y + 3.0, "Counting: Permutations vs. Combinations", size=1.65, bold=True, color=TEAL, align="center")
        p.rect(x + 41.0, y + 4.8, 42.5, 8.4, fill=GOLD_FILL, stroke=INK, r=0.5, line_w=0.22)
        p.text(rx, y + 7.8, "Permutation (nPr) — Order MATTERS!", size=1.55, bold=True, color=INK, align="center")
        p.text(rx, y + 11.2, "1st/2nd/3rd of 10: 10 × 9 × 8 = 720", size=1.55, bold=True, mono=True, color=TEAL, align="center")
        p.rect(x + 41.0, y + 14.0, 42.5, 8.8, fill=GREEN_FILL, stroke=INK, r=0.5, line_w=0.22)
        p.text(rx, y + 17.0, "Combination (nCr) — Order Does NOT Matter!", size=1.52, bold=True, color=INK, align="center")
        p.text(rx, y + 20.4, "3-person group of 10: 720 ÷ 3! = 120", size=1.55, bold=True, mono=True, color=INK, align="center")


# =============================================================================
# 2. SECTION-SPECIFIC COMMON TRAPS ("WATCH OUT!" ALERTS FOR ALL 45 SECTIONS)
# =============================================================================
COMMON_TRAPS: Dict[str, str] = {
    "1.1": "WATCH OUT: A remainder must ALWAYS be smaller than the divisor (Rem < Divisor). Check whether the problem asks for full groups, leftovers, or rounding up!",
    "1.2": "WATCH OUT: 4³ means 4 × 4 × 4 = 64 — NEVER multiply the base by the exponent (4 × 3 = 12)!",
    "1.3": "WATCH OUT: Multiply & Divide have EQUAL priority (go Left-to-Right!), and Add & Subtract have EQUAL priority (go Left-to-Right!).",
    "1.4": "WATCH OUT: Keep branching until EVERY bottom leaf is PRIME (do not stop at composite numbers like 4, 6, 8, or 9; and remember 1 is NOT prime).",
    "1.5": "WATCH OUT: GCF is a factor that divides IN (smaller or equal, Venn overlap); LCM is a multiple they build UP to (larger or equal, all Venn blocks).",
    "2.1": "WATCH OUT: Never add denominators directly (1/3 + 1/4 ≠ 2/7)! Rewrite with the Least Common Denominator (LCD) first, then add only the numerators.",
    "2.2": "WATCH OUT: For mixed numbers, ALWAYS convert to improper fractions (a b/c = (ac+b)/c) BEFORE multiplying!",
    "2.3": "WATCH OUT: Keep the FIRST fraction as-is and flip ONLY the SECOND fraction (the divisor): a/b ÷ c/d = a/b × d/c.",
    "2.4": "WATCH OUT: Line up decimal points for + and - (annex trailing 0s), but for × count the TOTAL decimal places in both factors!",
    "2.5": "WATCH OUT: When dividing by a decimal, shift the decimal point the SAME number of places right in BOTH the divisor and the dividend!",
    "3.1": "WATCH OUT: Order matters in ratios! Check whether the question asks for Part-to-Part (3:2) or Part-to-Whole (3:5).",
    "3.2": "WATCH OUT: Never add the same number to both rows of a ratio table — always MULTIPLY or DIVIDE both quantities by the same scale factor!",
    "3.3": "WATCH OUT: For unit price ('per item' or 'per ounce'), divide Money ÷ Quantity. The smaller unit cost is the better buy!",
    "3.4": "WATCH OUT: 'Percent' means per 100: move the decimal 2 places RIGHT for % (0.06 = 6%, NOT 60%), and 2 places LEFT for a decimal.",
    "3.5": "WATCH OUT: For percent change, ALWAYS divide the change by the ORIGINAL starting amount — never the new ending amount!",
    "4.1": "WATCH OUT: When substituting x into 4x + 7, 4x means 4 × x (multiply 4 × 5 = 20 first; do NOT write '45')!",
    "4.2": "WATCH OUT: Combine only terms with the EXACT same variable and exponent — never combine 6x + 8 into 14x!",
    "4.3": "WATCH OUT: Multiply the outside factor by EVERY term inside the parentheses: 3(2x + 5) = 6x + 15 (do not forget 3 × 5)!",
    "4.4": "WATCH OUT: Factor out the GREATEST common factor (GCF) so the terms left inside parentheses share no common factor > 1.",
    "5.1": "WATCH OUT: Always multiply Base b × Perpendicular Height h (at 90°) — ignore the slanted side length when finding area!",
    "5.2": "WATCH OUT: Don't forget to divide by 2 for triangles (A = ½bh)! And when solving for a missing height, double the area first (h = 2A ÷ b).",
    "5.3": "WATCH OUT: In a trapezoid, add the two parallel bases (b₁ + b₂) FIRST before multiplying by ½h!",
    "5.4": "WATCH OUT: Wait! 1 hour = 60 minutes (NOT 100): when borrowing 1 hour in elapsed time, add 60 minutes to the minutes column.",
    "6.1": "WATCH OUT: Zero (0) is its own opposite and is neither positive nor negative; -(-x) means the opposite of -x, which is +x!",
    "6.2": "WATCH OUT: With negative numbers, a larger digit means FURTHER LEFT (smaller/colder): -18 < -5, and -0.80 < -0.75!",
    "6.3": "WATCH OUT: Absolute value |x| is always ≥ 0, but a negative sign OUTSIDE the bars (-|-14| = -14) stays negative!",
    "6.4": "WATCH OUT: In (x, y), move horizontally (Left/Right) for x FIRST, then vertically (Up/Down) for y. Reflecting across the x-axis flips y!",
    "6.5": "WATCH OUT: If two points are in DIFFERENT quadrants (cross an axis), ADD |x|; if they are in the SAME quadrant, SUBTRACT |x|!",
    "7.1": "WATCH OUT: '12 less than k' translates to k - 12 (NOT 12 - k)! Always test your value by substituting it back into the original equation.",
    "7.2": "WATCH OUT: Use the INVERSE operation on BOTH sides of the '=' sign (+ undoes -, and - undoes +) to keep the equation balanced!",
    "7.3": "WATCH OUT: To solve (3/4)x = 18, multiply both sides by the RECIPROCAL (4/3); to solve k ÷ 7 = 14.5, multiply both sides by 7!",
    "7.4": "WATCH OUT: Use an OPEN circle (○) for < or >, and a SOLID dot (●) for ≤ ('at most') or ≥ ('at least')!",
    "7.5": "WATCH OUT: Check ALL rows of the table! Multiplicative y = kx passes through (0, 0); additive y = x + b has a constant difference y - x.",
    "8.1": "WATCH OUT: A rectangular prism has 6 faces (3 matching pairs: 2lw + 2lh + 2wh) — don't forget to double all three face pairs!",
    "8.2": "WATCH OUT: Use the ½ on EVERY triangular face (A = ½bh or ½bl), and count all faces in the net (5 for triangular prism, 5 for square pyramid)!",
    "8.3": "WATCH OUT: Volume is measured in CUBIC units (in.³, cm³). Eight ½-inch cubes (2 × 2 × 2 = 8) fit inside 1 cubic inch!",
    "8.4": "WATCH OUT: If given diameter d, divide by 2 FIRST to get radius r = d ÷ 2 before squaring r²! And don't forget the ⅓ for cones!",
    "9.1": "WATCH OUT: When finding a missing score for a target mean, multiply Target Mean × Total Count FIRST to find the required sum!",
    "9.2": "WATCH OUT: ALWAYS sort the data from least to greatest BEFORE finding the Median! If n is even, average the two middle numbers.",
    "9.3": "WATCH OUT: When n is odd, DO NOT include the overall Median in either the lower half or upper half when finding Q₁ and Q₃!",
    "9.4": "WATCH OUT: Distances |x - Mean| are ALWAYS positive (subtract the smaller number from the larger for every data value)!",
    "10.1": "WATCH OUT: To subtract a signed number, ADD ITS OPPOSITE: a - (-b) = a + b (subtracting a negative moves RIGHT on the number line)!",
    "10.2": "WATCH OUT: (-5)² = (-5) × (-5) = +25 (positive!), whereas -5² without parentheses means -(5 × 5) = -25!",
    "10.3": "WATCH OUT: In two-step equations (ax + b = c), undo addition/subtraction FIRST, then undo multiplication/division SECOND!",
    "10.4": "WATCH OUT: Ask 'Does order matter?' — awarding 1st/2nd/3rd medals is a Permutation (nPr); choosing a group/team is a Combination (nCr)!",
}


# =============================================================================
# 3. READY-TO-USE GRAPHIC ORGANIZERS INSIDE PROBLEM CARDS (PRACTICE A & B)
# =============================================================================
def draw_problem_workspace_organizer(
    p: Any,
    sec_num: str,
    sheet_type: str,
    prob_num: int,
    px: float,
    py: float,
    col_w: float,
    row_h: float,
    prob_prompt: str = "",
) -> None:
    """Draws a light, problem-aware graphic organizer (number line, ratio table, mini coordinate grid, or structured step template) inside the open workspace of warm-up/core problem cards across ALL 45 sections."""
    STROKE_FAINT = "#CBD5E1"
    TEXT_FAINT = "#64748B"
    pl = prob_prompt.lower()

    # Available lower-right workspace region inside card:
    org_y = py + row_h - 16.0
    org_x = px + col_w - 44.0
    org_w = 41.0

    # --- UNIT 1: NUMERICAL EXPRESSIONS & FACTORS ---
    if sec_num == "1.1" and prob_num <= 4:
        # Long Division Bracket + Division Algorithm Check
        lx, ly = org_x + 4.5, org_y + 3.2
        p.line(lx + 4.0, ly - 1.2, lx + 4.0, ly + 3.0, color=STROKE_FAINT, width=0.26)
        p.line(lx + 4.0, ly - 1.2, lx + 17.5, ly - 1.2, color=STROKE_FAINT, width=0.26)
        p.text(lx + 10.5, ly - 2.0, "Q:___ R:___", size=1.22, mono=True, color=TEXT_FAINT, align="center")
        p.text(org_x, org_y + 9.2, "Check: (___ × ___) + ___ = ___", size=1.22, mono=True, color=TEXT_FAINT)

    elif sec_num == "1.2" and prob_num <= 4:
        # Repeated Multiplication Expansion Box
        p.rect(org_x + 1.0, org_y + 1.5, org_w - 2.0, 8.2, fill="#F8FAFC", stroke=STROKE_FAINT, r=0.5, line_w=0.2)
        p.text(org_x + 2.5, org_y + 4.6, "Expand: ___ × ___ × ___", size=1.28, mono=True, color=TEXT_FAINT)
        p.text(org_x + 2.5, org_y + 8.0, "Value = _________", size=1.28, mono=True, color=TEXT_FAINT)

    elif sec_num == "1.3" and prob_num <= 4:
        # 3-Step PEMDAS Funnel Lines
        cx = org_x + org_w / 2.0
        p.text(cx, org_y + 1.4, "PEMDAS Funnel: ( ) -> b^n -> ×/÷ -> +/-", size=1.18, color=TEXT_FAINT, align="center")
        p.text(cx, org_y + 4.5, "= ___________________", size=1.25, mono=True, color=TEXT_FAINT, align="center")
        p.text(cx, org_y + 7.2, "= _____________", size=1.25, mono=True, color=TEXT_FAINT, align="center")
        p.text(cx, org_y + 9.8, "= _______", size=1.25, mono=True, color=TEXT_FAINT, align="center")

    elif sec_num == "1.4" and prob_num <= 4:
        # Mini Factor Tree starter branches on right side of workspace
        cx = org_x + org_w / 2.0
        p.circle(cx, org_y + 1.8, 2.2, fill="#F8FAFC", stroke=STROKE_FAINT, line_w=0.22)
        p.line(cx - 1.2, org_y + 3.8, cx - 6.5, org_y + 7.2, color=STROKE_FAINT, width=0.22)
        p.line(cx + 1.2, org_y + 3.8, cx + 6.5, org_y + 7.2, color=STROKE_FAINT, width=0.22)
        p.circle(cx - 7.0, org_y + 9.0, 2.0, fill=WHITE, stroke=STROKE_FAINT, line_w=0.2)
        p.circle(cx + 7.0, org_y + 9.0, 2.0, fill=WHITE, stroke=STROKE_FAINT, line_w=0.2)
        p.text(cx, org_y - 0.8, "Factor Tree", size=1.30, color=TEXT_FAINT, align="center")

    elif sec_num == "1.5" and prob_num <= 4:
        # Mini 2-circle Venn Diagram outline for GCF (overlap) & LCM (all)
        cx = org_x + org_w / 2.0
        cy = org_y + 5.2
        p.circle(cx - 3.8, cy, 5.2, fill=None, stroke=STROKE_FAINT, line_w=0.24)
        p.circle(cx + 3.8, cy, 5.2, fill=None, stroke=STROKE_FAINT, line_w=0.24)
        p.text(cx, cy + 0.5, "GCF", size=1.28, bold=True, color=TEXT_FAINT, align="center")

    # --- UNIT 2: FRACTIONS & DECIMALS ---
    elif sec_num == "2.1" and prob_num <= 4:
        if "in all" in pl or "remain" in pl or "+" in pl or "-" in pl:
            p.text(org_x, org_y + 3.2, "LCD = _____", size=1.28, mono=True, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "___/___  ±  ___/___  =  ___/___", size=1.28, mono=True, color=TEXT_FAINT)
        elif "improper" in pl or "mixed number" in pl:
            p.text(org_x, org_y + 3.2, "Whole × Denom + Num:", size=1.22, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "Improper = ___/___  Mixed = ___ ___/___", size=1.18, mono=True, color=TEXT_FAINT)
        else:
            p.text(org_x, org_y + 3.2, "Divide Top & Bottom by GCF:", size=1.22, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "(___ ÷ ___) / (___ ÷ ___) = ___/___", size=1.20, mono=True, color=TEXT_FAINT)

    elif sec_num == "2.2" and prob_num <= 4:
        has_mixed = any(m in prob_prompt for m in ("1 ", "2 ", "3 ", "4 ")) and "/" in prob_prompt and prob_num == 3 and sheet_type == "B"
        if has_mixed:
            p.text(org_x, org_y + 3.2, "Improper: (___/___) × (___/___)", size=1.24, mono=True, color=TEXT_FAINT)
        else:
            p.text(org_x, org_y + 3.2, "Setup: (___/___) × (___/___)", size=1.24, mono=True, color=TEXT_FAINT)
        p.text(org_x, org_y + 7.4, "= (___ × ___) / (___ × ___) = ___", size=1.24, mono=True, color=TEXT_FAINT)

    elif sec_num == "2.3" and prob_num <= 4:
        # Keep-Change-Flip Reciprocal Template
        p.rect(org_x + 0.5, org_y + 1.8, org_w - 1.0, 7.6, fill="#F8FAFC", stroke=STROKE_FAINT, r=0.5, line_w=0.2)
        p.text(org_x + 2.0, org_y + 4.8, "Keep      ×   Flip (Reciprocal)", size=1.18, color=TEXT_FAINT)
        p.text(org_x + 2.0, org_y + 8.0, "(___/___) × (___/___) = ___", size=1.25, mono=True, color=TEXT_FAINT)

    elif sec_num == "2.4" and prob_num <= 4:
        if "×" in prob_prompt or "cost of" in pl or "per pound" in pl:
            p.text(org_x, org_y + 3.2, "Multiply & Count Dec Places:", size=1.20, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "_____ × _____ = _____ (___ places)", size=1.20, mono=True, color=TEXT_FAINT)
        else:
            # Vertical Decimal Alignment Grid
            p.text(org_x + 4.0, org_y + 1.6, "Line Up Decimals:", size=1.20, color=TEXT_FAINT)
            p.text(org_x + 6.0, org_y + 4.6, "    .    ", size=1.35, bold=True, mono=True, color=TEXT_FAINT)
            p.text(org_x + 6.0, org_y + 7.4, "±   .    ", size=1.35, bold=True, mono=True, color=TEXT_FAINT)
            p.line(org_x + 5.0, org_y + 8.2, org_x + 26.0, org_y + 8.2, color=STROKE_FAINT, width=0.22)
            p.text(org_x + 6.0, org_y + 10.4, "    .    ", size=1.35, bold=True, mono=True, color=TEXT_FAINT)

    elif sec_num == "2.5" and prob_num <= 4:
        # Decimal Shift Division Bracket
        p.text(org_x, org_y + 2.6, "Shift Decimal Equally ->", size=1.18, color=TEXT_FAINT)
        lx, ly = org_x + 5.0, org_y + 6.6
        p.line(lx + 4.5, ly - 1.4, lx + 4.5, ly + 2.6, color=STROKE_FAINT, width=0.26)
        p.line(lx + 4.5, ly - 1.4, lx + 20.0, ly - 1.4, color=STROKE_FAINT, width=0.26)
        p.text(lx - 0.5, ly + 1.4, "___", size=1.22, mono=True, color=TEXT_FAINT)
        p.text(lx + 6.0, ly + 1.4, "______.___", size=1.22, mono=True, color=TEXT_FAINT)

    # --- UNIT 3: RATIOS, RATES & PERCENTS ---
    elif sec_num == "3.1" and prob_num <= 4:
        if "simplest form" in pl and "total" not in pl and "in all" not in pl:
            p.text(org_x, org_y + 3.2, "Divide Both Terms by GCF:", size=1.20, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "GCF = ___  ->  ___ : ___", size=1.26, mono=True, color=TEXT_FAINT)
        else:
            # Mini Tape Diagram boxes
            p.text(org_x, org_y + 1.2, "Tape Model:", size=1.32, color=TEXT_FAINT)
            for i in range(5):
                p.rect(org_x + i * 6.2, org_y + 2.4, 5.8, 3.6, fill=WHITE, stroke=STROKE_FAINT, line_w=0.2)
            for i in range(3):
                p.rect(org_x + i * 6.2, org_y + 6.6, 5.8, 3.6, fill=WHITE, stroke=STROKE_FAINT, line_w=0.2)

    elif sec_num == "3.2" and prob_num <= 6:
        # Blank 2-row × 4-column Ratio Table grid
        p.text(org_x, org_y + 0.8, "Ratio Table:", size=1.32, color=TEXT_FAINT)
        cw_cell = 9.5
        rh_cell = 4.2
        for r_i in range(2):
            for c_i in range(4):
                p.rect(
                    org_x + c_i * cw_cell,
                    org_y + 1.8 + r_i * rh_cell,
                    cw_cell,
                    rh_cell,
                    fill="#F8FAFC" if c_i == 0 else WHITE,
                    stroke=STROKE_FAINT,
                    line_w=0.22,
                )

    elif sec_num == "3.3" and prob_num <= 4:
        # Unit Rate Setup
        p.rect(org_x + 0.5, org_y + 1.8, org_w - 1.0, 7.6, fill="#F8FAFC", stroke=STROKE_FAINT, r=0.5, line_w=0.2)
        p.text(org_x + 2.0, org_y + 4.8, "Unit Rate = Total ÷ Units", size=1.20, color=TEXT_FAINT)
        p.text(org_x + 2.0, org_y + 8.0, "_____ ÷ _____ = _____ per 1", size=1.24, mono=True, color=TEXT_FAINT)

    elif sec_num == "3.4" and prob_num <= 4:
        # 0% to 100% Double Number Line scaffold
        ly = org_y + 6.0
        p.line(org_x + 2.0, ly, org_x + org_w - 2.0, ly, color=STROKE_FAINT, width=0.28)
        for idx, pct in enumerate(["0%", "25%", "50%", "75%", "100%"]):
            tx = org_x + 2.0 + idx * ((org_w - 4.0) / 4.0)
            p.line(tx, ly - 1.0, tx, ly + 1.0, color=STROKE_FAINT, width=0.22)
            p.text(tx, ly + 3.0, pct, size=1.25, mono=True, color=TEXT_FAINT, align="center")

    elif sec_num == "3.5" and prob_num <= 4:
        # Percent Proportion / Discount & Tax Bar
        p.text(org_x, org_y + 3.2, "Part = % × Whole: ___ × ___ = ___", size=1.22, mono=True, color=TEXT_FAINT)
        p.text(org_x, org_y + 7.4, "Orig: _____ ± %Amt: _____ = _____", size=1.22, mono=True, color=TEXT_FAINT)

    # --- UNIT 4: ALGEBRAIC EXPRESSIONS & PROPERTIES ---
    elif sec_num == "4.1" and prob_num <= 4:
        # Substitution Parentheses Template
        p.text(org_x, org_y + 3.2, "Substitute in ( ):", size=1.22, color=TEXT_FAINT)
        p.text(org_x, org_y + 7.2, "____( ___ ) ± ____ = _____", size=1.28, mono=True, color=TEXT_FAINT)

    elif sec_num == "4.2" and prob_num <= 4:
        # 2-Column Like Terms Sort Box
        hw = (org_w - 2.0) / 2.0
        p.rect(org_x, org_y + 1.6, hw, 8.0, fill="#F8FAFC", stroke=STROKE_FAINT, line_w=0.2)
        p.rect(org_x + hw, org_y + 1.6, hw, 8.0, fill=WHITE, stroke=STROKE_FAINT, line_w=0.2)
        p.text(org_x + hw / 2.0, org_y + 4.2, "Var Terms", size=1.18, bold=True, color=TEXT_FAINT, align="center")
        p.text(org_x + hw * 1.5, org_y + 4.2, "Constants", size=1.18, bold=True, color=TEXT_FAINT, align="center")

    elif sec_num == "4.3" and prob_num <= 4:
        # 2-Box Distributive Area Model
        p.text(org_x + 2.0, org_y + 6.4, "___", size=1.25, mono=True, color=TEXT_FAINT)
        p.rect(org_x + 8.0, org_y + 2.2, 14.0, 6.8, fill="#F8FAFC", stroke=STROKE_FAINT, line_w=0.22)
        p.rect(org_x + 22.0, org_y + 2.2, 14.0, 6.8, fill=WHITE, stroke=STROKE_FAINT, line_w=0.22)
        p.text(org_x + 15.0, org_y + 1.4, "Term 1", size=1.15, color=TEXT_FAINT, align="center")
        p.text(org_x + 29.0, org_y + 1.4, "Term 2", size=1.15, color=TEXT_FAINT, align="center")

    elif sec_num == "4.4" and prob_num <= 4:
        # GCF Factoring Box
        p.text(org_x, org_y + 3.2, "GCF = _____", size=1.28, mono=True, color=TEXT_FAINT)
        p.text(org_x, org_y + 7.4, "Factored: ____( _____ ± _____ )", size=1.26, mono=True, color=TEXT_FAINT)

    # --- UNIT 5: AREAS OF POLYGONS & ELAPSED TIME ---
    elif sec_num == "5.1" and prob_num <= 4:
        if "perimeter" in pl and "area" not in pl:
            p.text(org_x, org_y + 3.2, "Outer Sides: s₁=___  s₂=___", size=1.24, mono=True, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "Perimeter P = 2(s₁ + s₂) = _____", size=1.24, mono=True, color=TEXT_FAINT)
        else:
            p.text(org_x, org_y + 3.2, "b = _____   ⊥h = _____", size=1.26, mono=True, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "Area A = b × h = _________", size=1.26, mono=True, color=TEXT_FAINT)

    elif sec_num == "5.2" and prob_num <= 4:
        p.text(org_x, org_y + 3.2, "b = _____   ⊥h = _____", size=1.26, mono=True, color=TEXT_FAINT)
        p.text(org_x, org_y + 7.4, "Area A = ½ × b × h = _____", size=1.26, mono=True, color=TEXT_FAINT)

    elif sec_num == "5.3" and prob_num <= 4:
        if "trapezoid" in pl:
            p.text(org_x, org_y + 3.2, "b₁ + b₂ = ___ + ___ = ___", size=1.24, mono=True, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "A = ½ × h × (b₁+b₂) = _____", size=1.24, mono=True, color=TEXT_FAINT)
        else:
            p.text(org_x, org_y + 3.2, "Part 1 Area = _____________", size=1.22, mono=True, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "Part 2 Area = _____ -> Sum = ___", size=1.22, mono=True, color=TEXT_FAINT)

    elif sec_num == "5.4" and ((sheet_type == "A" and prob_num in (1, 2, 3, 4)) or (sheet_type == "B" and prob_num in (1, 5, 7))):
        # Mini Quadrant I coordinate grid
        gx, gy, gw, gh = org_x + 12.0, org_y + 0.5, 24.0, 10.0
        for c_i in range(7):
            lx = gx + c_i * (gw / 6.0)
            p.line(lx, gy, lx, gy + gh, color="#E2E8F0", width=0.16)
        for r_i in range(5):
            ly = gy + r_i * (gh / 4.0)
            p.line(gx, ly, gx + gw, ly, color="#E2E8F0", width=0.16)
        p.line(gx, gy + gh, gx + gw + 1.0, gy + gh, color=STROKE_FAINT, width=0.28)
        p.line(gx, gy - 0.8, gx, gy + gh, color=STROKE_FAINT, width=0.28)
        p.text(gx - 1.2, gy + gh + 0.8, "0", size=1.25, mono=True, color=TEXT_FAINT, align="right")

    # --- UNIT 6 & 10.1: INTEGERS, NUMBER LINES & COORDINATE PLANE ---
    elif sec_num in ("6.1", "6.2", "6.3", "10.1") and prob_num <= 4:
        # Signed Number Line with 0 in center
        ly = org_y + 6.0
        lx1, lx2 = org_x + 1.5, org_x + org_w - 1.5
        p.line(lx1, ly, lx2, ly, color=STROKE_FAINT, width=0.28)
        for t_i in range(9):
            tx = lx1 + t_i * ((lx2 - lx1) / 8.0)
            is_zero = t_i == 4
            p.line(tx, ly - (1.4 if is_zero else 0.8), tx, ly + (1.4 if is_zero else 0.8), color=STROKE_FAINT, width=0.25 if is_zero else 0.18)
            if is_zero:
                p.text(tx, ly + 3.2, "0", size=1.35, bold=True, mono=True, color=TEXT_FAINT, align="center")

    elif sec_num in ("6.4", "6.5") and prob_num <= 6:
        # 4-Quadrant Mini Coordinate Grid
        gx, gy, gw, gh = org_x + 14.0, org_y + 0.4, 22.0, 10.2
        cx, cy = gx + gw / 2.0, gy + gh / 2.0
        for c_i in range(7):
            lx = gx + c_i * (gw / 6.0)
            p.line(lx, gy, lx, gy + gh, color="#E2E8F0", width=0.16)
        for r_i in range(5):
            ly = gy + r_i * (gh / 4.0)
            p.line(gx, ly, gx + gw, ly, color="#E2E8F0", width=0.16)
        p.line(gx - 0.8, cy, gx + gw + 0.8, cy, color=STROKE_FAINT, width=0.28)
        p.line(cx, gy - 0.6, cx, gy + gh + 0.6, color=STROKE_FAINT, width=0.28)
        p.text(gx + gw + 1.2, cy + 0.5, "x", size=1.25, mono=True, color=TEXT_FAINT)
        p.text(cx, gy - 0.9, "y", size=1.25, mono=True, color=TEXT_FAINT, align="center")

    # --- UNIT 7: EQUATIONS & INEQUALITIES ---
    elif sec_num == "7.1" and prob_num <= 4:
        p.text(org_x, org_y + 3.2, "Sub Value: LHS = _________ = ___", size=1.22, mono=True, color=TEXT_FAINT)
        p.text(org_x, org_y + 7.4, "Compare:  LHS ___ ?=? RHS ___", size=1.22, mono=True, color=TEXT_FAINT)

    elif sec_num in ("7.2", "7.3") and prob_num <= 4:
        p.text(org_x, org_y + 3.2, "Inverse Op Both Sides: _________", size=1.22, mono=True, color=TEXT_FAINT)
        p.text(org_x, org_y + 7.4, "Solution = _____  (Check: _____)", size=1.22, mono=True, color=TEXT_FAINT)

    elif sec_num == "7.4" and prob_num <= 6:
        # Inequality Number Line with center boundary tick (○ or ●)
        ly = org_y + 6.2
        lx1, lx2 = org_x + 2.0, org_x + org_w - 2.0
        p.line(lx1, ly, lx2, ly, color=STROKE_FAINT, width=0.28)
        for t_i in range(7):
            tx = lx1 + t_i * ((lx2 - lx1) / 6.0)
            p.line(tx, ly - 0.9, tx, ly + 0.9, color=STROKE_FAINT, width=0.2)
        mid_t = (lx1 + lx2) / 2.0
        p.circle(mid_t, ly, 1.1, fill=WHITE, stroke=STROKE_FAINT, line_w=0.22)
        p.text(mid_t, ly - 1.8, "○ or ●", size=1.25, color=TEXT_FAINT, align="center")

    elif sec_num == "7.5" and prob_num <= 4:
        # Mini Input-Output (x | y) table
        cw_cell = 8.2
        rh_cell = 4.0
        headers = ["x", "", "", ""]
        rows2 = ["y", "", "", ""]
        for c_i in range(4):
            cx = org_x + 6.0 + c_i * cw_cell
            p.rect(cx, org_y + 1.8, cw_cell, rh_cell, fill="#F8FAFC" if c_i == 0 else WHITE, stroke=STROKE_FAINT, line_w=0.2)
            p.rect(cx, org_y + 1.8 + rh_cell, cw_cell, rh_cell, fill="#F8FAFC" if c_i == 0 else WHITE, stroke=STROKE_FAINT, line_w=0.2)
            if c_i == 0:
                p.text(cx + cw_cell / 2.0, org_y + 4.5, headers[0], size=1.4, bold=True, mono=True, color=TEXT_FAINT, align="center")
                p.text(cx + cw_cell / 2.0, org_y + 4.5 + rh_cell, rows2[0], size=1.4, bold=True, mono=True, color=TEXT_FAINT, align="center")

    # --- UNIT 8: SURFACE AREA & VOLUME OF 3D SOLIDS ---
    elif sec_num == "8.1" and prob_num <= 4:
        if "cube" in pl:
            p.text(org_x, org_y + 3.2, "1 Square Face = s² = _____", size=1.22, mono=True, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "Cube SA = 6 × s² = _________", size=1.22, mono=True, color=TEXT_FAINT)
        else:
            p.text(org_x, org_y + 3.2, "Faces: l·w=___  l·h=___  w·h=___", size=1.20, mono=True, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "SA = 2( ___ + ___ + ___ ) = _____", size=1.20, mono=True, color=TEXT_FAINT)

    elif sec_num == "8.2" and prob_num <= 4:
        p.text(org_x, org_y + 3.2, "Base Area(s) B = _________", size=1.22, mono=True, color=TEXT_FAINT)
        p.text(org_x, org_y + 7.4, "+ Lateral Faces = _____ -> SA=___", size=1.22, mono=True, color=TEXT_FAINT)

    elif sec_num == "8.3" and prob_num <= 4:
        if "cube" in pl and "cubic" not in pl.split("cube")[0]:
            p.text(org_x, org_y + 3.2, "Cube Edge s = _____", size=1.22, mono=True, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "Volume V = s³ = s×s×s = _____", size=1.22, mono=True, color=TEXT_FAINT)
        else:
            p.text(org_x, org_y + 3.2, "Base Area B = l × w = _____", size=1.22, mono=True, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "Volume V = B × h = _________", size=1.22, mono=True, color=TEXT_FAINT)

    elif sec_num == "8.4" and prob_num <= 4:
        if "right triangle" in pl or "hypotenuse" in pl or "ladder" in pl:
            p.text(org_x, org_y + 3.2, "a² + b² = ___ + ___ = ___", size=1.22, mono=True, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "c = √(a² + b²) = _________", size=1.22, mono=True, color=TEXT_FAINT)
        elif "cone" in pl:
            p.text(org_x, org_y + 3.2, "r = _____  |  r² = _____", size=1.22, mono=True, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "V = ⅓ × π × r² × h = _____", size=1.22, mono=True, color=TEXT_FAINT)
        elif "cylinder" in pl or "cylindrical" in pl:
            p.text(org_x, org_y + 3.2, "r = _____  |  r² = _____", size=1.22, mono=True, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "V = π × r² × h = _________", size=1.22, mono=True, color=TEXT_FAINT)
        else:
            p.text(org_x, org_y + 3.2, "r = _____  |  r² = _____", size=1.22, mono=True, color=TEXT_FAINT)
            p.text(org_x, org_y + 7.4, "Area A = π × r² ≈ _________", size=1.22, mono=True, color=TEXT_FAINT)

    # --- UNIT 9: STATISTICAL MEASURES & DATA DISPLAYS ---
    elif sec_num == "9.1" and prob_num <= 4:
        p.text(org_x, org_y + 3.2, "Sum = _________   Count n = ___", size=1.22, mono=True, color=TEXT_FAINT)
        p.text(org_x, org_y + 7.4, "Mean = Sum ÷ n = _____", size=1.22, mono=True, color=TEXT_FAINT)

    elif sec_num == "9.2" and prob_num <= 4:
        # Ordered data strip slots
        p.text(org_x, org_y + 3.2, "Sorted: [   ] [   ] [   ] [   ] [   ] [   ]", size=1.35, mono=True, color=TEXT_FAINT)
        p.text(org_x, org_y + 7.4, "Med: _____   Mode: _____   Rng: _____", size=1.35, mono=True, color=TEXT_FAINT)

    elif sec_num == "9.3" and prob_num <= 4:
        # 5-Number Summary + Box Plot axis
        p.text(org_x - 4.0, org_y + 2.8, "Min:___ Q1:___ Med:___ Q3:___ Max:___", size=1.28, mono=True, color=TEXT_FAINT)
        ly = org_y + 7.5
        p.line(org_x, ly, org_x + org_w - 1.5, ly, color=STROKE_FAINT, width=0.26)
        for t_i in range(6):
            tx = org_x + t_i * ((org_w - 1.5) / 5.0)
            p.line(tx, ly - 0.8, tx, ly + 0.8, color=STROKE_FAINT, width=0.2)

    elif sec_num == "9.4" and prob_num <= 4:
        # 3-Step MAD check lines
        p.text(org_x - 2.0, org_y + 2.8, "1. Mean = _____", size=1.32, mono=True, color=TEXT_FAINT)
        p.text(org_x - 2.0, org_y + 6.0, "2. |x - Mean|: ____, ____, ____, ____", size=1.32, mono=True, color=TEXT_FAINT)
        p.text(org_x - 2.0, org_y + 9.2, "3. MAD = Sum ÷ n = _____", size=1.32, mono=True, color=TEXT_FAINT)

    # --- UNIT 10: GRADE 7 BRIDGE (10.2 - 10.4) ---
    elif sec_num == "10.2" and prob_num <= 4:
        p.text(org_x, org_y + 3.2, "Sign Rule: [ ] Same(+)  [ ] Diff(-)", size=1.20, mono=True, color=TEXT_FAINT)
        p.text(org_x, org_y + 7.4, "Magnitude |a|×|b| = _________", size=1.22, mono=True, color=TEXT_FAINT)

    elif sec_num == "10.3" and prob_num <= 4:
        p.text(org_x, org_y + 3.2, "1. Undo +/-:  ax = _________", size=1.22, mono=True, color=TEXT_FAINT)
        p.text(org_x, org_y + 7.4, "2. Undo ×/÷:   x = _________", size=1.22, mono=True, color=TEXT_FAINT)

    elif sec_num == "10.4" and prob_num <= 4:
        p.text(org_x, org_y + 3.2, "P(E) = Favorable ___ / Total ___", size=1.20, mono=True, color=TEXT_FAINT)
        p.text(org_x, org_y + 7.4, "Simp = ___/___ = _____% ", size=1.22, mono=True, color=TEXT_FAINT)


# =============================================================================
# 4. TUTOR / COACH SETUP & INTERMEDIATE STEP FORMATTER FOR COACH GUIDE
# =============================================================================
def _fmt_frac_dot(tok: str) -> str:
    """Converts SC-6 dot-fraction notation like '1.2.3' -> '1 2/3' when appropriate."""
    parts = tok.split(".")
    if len(parts) == 3 and all(p.lstrip("-").isdigit() for p in parts):
        return f"{parts[0]} {parts[1]}/{parts[2]}"
    return tok


def _collapse_sc6_fraction_tokens(tokens: List[str]) -> List[str]:
    """Pre-collapses SC-6 '[.]' fraction key sequences:
    - ['w', '[.]', 'a', '[.]', 'b'] -> ['w a/b']
    - ['[.]', 'a', '[.]', 'b']      -> ['a/b']
    """
    out: List[str] = []
    i = 0
    n = len(tokens)
    while i < n:
        # Mixed number: w [.] a [.] b
        if (
            i + 4 < n
            and tokens[i].lstrip("-").isdigit()
            and tokens[i + 1] == "[.]"
            and tokens[i + 2].isdigit()
            and tokens[i + 3] == "[.]"
            and tokens[i + 4].rstrip(",;").isdigit()
        ):
            b_clean = tokens[i + 4].rstrip(",;")
            out.append(f"{tokens[i]} {tokens[i + 2]}/{b_clean}")
            i += 5
            continue
        # Proper fraction: [.] a [.] b
        if (
            i + 3 < n
            and tokens[i] == "[.]"
            and tokens[i + 1].isdigit()
            and tokens[i + 2] == "[.]"
            and tokens[i + 3].rstrip(",;").isdigit()
        ):
            b_clean = tokens[i + 3].rstrip(",;")
            out.append(f"{tokens[i + 1]}/{b_clean}")
            i += 4
            continue
        out.append(tokens[i])
        i += 1
    return out


def _parse_single_rpn_clause(clause: str, prev_pair: List[str]) -> str:
    """Parses a single RPN clause into a clean paper-and-pencil setup expression."""
    # Strip trailing inline result arrow annotation like '-> 2/part' or '-> 0.625'
    if "->" in clause and "[" in clause.split("->")[0]:
        clause = clause.split("->")[0].strip()

    raw_tokens = _collapse_sc6_fraction_tokens(clause.strip().split())
    if not raw_tokens:
        return ""
    if "[" not in clause:
        return clause.strip()

    # If the clause is a stats data-entry sequence ([Σ+], [g][x̄], [f][MED], [g][MAD], [IQR], etc.)
    if any(k in clause for k in ("[Σ+]", "[x̄]", "[MED]", "[MODE]", "[IQR]", "[MAD]", "[1Q]", "[3Q]", "[RNG]")):
        ops = []
        if "[x̄]" in clause:
            ops.append("Mean")
        if "[MED]" in clause:
            ops.append("Med")
        if "[MODE]" in clause:
            ops.append("Mode")
        if "[RNG]" in clause:
            ops.append("Range")
        if "[1Q]" in clause or "[3Q]" in clause or "[IQR]" in clause:
            ops.append("Q1/Q3/IQR")
        if "[MAD]" in clause:
            ops.append("MAD")
        stat_lbl = "/".join(ops) if ops else "Stats"
        if "Load" in clause:
            for t in raw_tokens:
                if t.isdigit():
                    return f"Sort/Load {t} values -> {stat_lbl}"
            return f"Load data -> {stat_lbl}"
        nums = [
            t.rstrip(",;")
            for t in raw_tokens
            if t.rstrip(",;").replace(".", "").replace("-", "").isdigit()
        ]
        if nums:
            return f"{stat_lbl}({', '.join(nums[:5])}{'...' if len(nums) > 5 else ''})"
        return f"Calc {stat_lbl}"

    stack: List[str] = []
    steps: List[str] = []
    bin_map = {"[+]": "+", "+": "+", "[-]": "-", "-": "-", "[×]": "×", "×": "×", "[÷]": "÷", "÷": "÷"}

    for raw_t in raw_tokens:
        if raw_t == "[FDISP]" and stack and not steps:
            steps.append(f"{stack[-1]} -> Dec/Frac")
            continue
        tk = raw_t.rstrip(",;.")
        if not tk or tk in ("[ENTER]", "ENTER", "[FDISP]", "[g][CLΣ]", "[FRQ]", "Load", "stats!", "nums", "temps", "sets", "both", "MADs", "vs"):
            continue
        if tk in ("[f]", "[g]"):
            continue
        if tk.startswith("(") and tk.endswith(")"):
            # Skip inline parenthetical result notes like '(12)' or '(120)' inside key strings
            continue
        if tk.startswith("[+/-]"):
            if stack:
                a = stack.pop()
                stack.append(f"-{a}" if not a.startswith("-") else a[1:])
            continue
        if tk == "[x⇄y]" and len(stack) >= 2:
            stack[-1], stack[-2] = stack[-2], stack[-1]
            continue
        if tk == "[π]" or tk.endswith("[π]"):
            stack.append("π")
            continue
        if tk in bin_map:
            if len(stack) >= 2:
                b, a = stack.pop(), stack.pop()
                if a.startswith("Repeat(") or b.startswith("Repeat("):
                    expr = f"{a}, {b}"
                else:
                    prev_pair[:] = [a, b]
                    op = bin_map[tk]
                    expr = f"({a} {op} {b})"
                stack.append(expr)
                steps.append(expr[1:-1] if (expr.startswith("(") and expr.endswith(")")) else expr)
            continue
        if tk.endswith("[÷R]") and len(stack) >= 2:
            b, a = stack.pop(), stack.pop()
            prev_pair[:] = [a, b]
            expr = f"{a} ÷ {b} (Q & R)"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk in ("[x²]", "[g][x²]") and stack:
            a = stack.pop()
            expr = f"{a}²"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[x³]") and stack:
            a = stack.pop()
            expr = f"{a}³"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[yˣ]") and len(stack) >= 2:
            b, a = stack.pop(), stack.pop()
            expr = f"{a}^{b}"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[√x]") and stack:
            a = stack.pop()
            expr = f"√({a})"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[FACT]") and stack:
            a = stack.pop()
            expr = f"Factors({a})"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[PRIME]") and stack:
            a = stack.pop()
            expr = f"Prime?({a})"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[GCF]"):
            if len(stack) >= 2:
                b, a = stack.pop(), stack.pop()
                prev_pair[:] = [a, b]
            elif len(prev_pair) == 2:
                a, b = prev_pair[0], prev_pair[1]
            else:
                a, b = "a", "b"
            expr = f"GCF({a}, {b})"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[LCM]"):
            if len(stack) >= 2:
                b, a = stack.pop(), stack.pop()
                prev_pair[:] = [a, b]
            elif len(prev_pair) == 2:
                a, b = prev_pair[0], prev_pair[1]
            else:
                a, b = "a", "b"
            expr = f"LCM({a}, {b})"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.startswith("[g][SIMP]") or tk.endswith("[SIMP]"):
            suffix = tk.replace("[g][SIMP]", "").replace("[f][SIMP]", "").replace("[SIMP]", "")
            if len(stack) >= 2:
                b, a = stack.pop(), stack.pop()
                expr = f"Simp({a}:{b}){suffix}"
            elif stack:
                a = stack.pop()
                expr = f"Simp({a}){suffix}"
            else:
                expr = f"Simplify{suffix}"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[a:b]") and len(stack) >= 2:
            b, a = stack.pop(), stack.pop()
            expr = f"Ratio({a}:{b})"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[d/c]") and stack:
            a = stack.pop()
            expr = f"Improper({a})"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[REP]") and stack:
            a = stack.pop()
            expr = f"Repeat(+{a})"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[1/x]") and stack:
            a = stack.pop()
            expr = f"1/({a})"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[%]"):
            if len(stack) >= 2:
                b, a = stack.pop(), stack.pop()
                expr = f"{b}% of {a}"
                stack.append(expr)
                steps.append(expr)
            elif stack:
                a = stack.pop()
                expr = f"{a}%"
                stack.append(expr)
                steps.append(expr)
            continue
        if tk.endswith("[%CHG]") and len(stack) >= 2:
            b, a = stack.pop(), stack.pop()
            expr = f"%Chg({a}->{b})"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[|x|]") and stack:
            a = stack.pop()
            expr = f"|{a}|"
            stack.append(expr)
            steps.append(expr)
            continue
        if (tk.endswith("[>]") or tk.endswith("[<]") or tk.endswith("[≤]")) and len(stack) >= 2:
            b, a = stack.pop(), stack.pop()
            sym = ">" if "[>]" in tk else ("<" if "[<]" in tk else "≤")
            expr = f"Compare {a} {sym} {b}"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[RECT]") and len(stack) >= 2:
            b, a = stack.pop(), stack.pop()
            stack.append(f"({a}×{b})")
            steps.append(f"A = {a} × {b}")
            continue
        if tk.endswith("[TRI]") and len(stack) >= 2:
            b, a = stack.pop(), stack.pop()
            stack.append(f"½({a}×{b})")
            steps.append(f"A = ½({a} × {b})")
            continue
        if tk.endswith("[PRISM]") and len(stack) >= 3:
            c, b, a = stack.pop(), stack.pop(), stack.pop()
            expr = f"Prism({a}×{b}×{c})"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[CIRC]") and stack:
            a = stack.pop()
            expr = f"π × {a}²"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[CONE]") and len(stack) >= 2:
            b, a = stack.pop(), stack.pop()
            expr = f"⅓π({a}²)({b})"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[HYP]") and len(stack) >= 2:
            b, a = stack.pop(), stack.pop()
            expr = f"√({a}² + {b}²)"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[nPr]") and len(stack) >= 2:
            b, a = stack.pop(), stack.pop()
            expr = f"P({a},{b})"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[nCr]") and len(stack) >= 2:
            b, a = stack.pop(), stack.pop()
            expr = f"C({a},{b})"
            stack.append(expr)
            steps.append(expr)
            continue
        if tk.endswith("[x!]") and stack:
            a = stack.pop()
            expr = f"{a}!"
            stack.append(expr)
            steps.append(expr)
            continue
        if any(tk.endswith(u) for u in ("[▸HR]", "[▸HMS]", "[CLK]", "[▸cm]", "[▸in]", "[▸kg]", "[▸lb]", "[▸L]", "[▸°F]")):
            unit_lbl = tk.split("[")[-1].rstrip("]").replace("▸", "to ")
            if len(stack) >= 2 and unit_lbl == "CLK":
                b, a = stack.pop(), stack.pop()
                expr = f"Time({a} to {b})"
            elif stack:
                a = stack.pop()
                expr = f"{a} ({unit_lbl})"
            else:
                expr = unit_lbl
            stack.append(expr)
            steps.append(expr)
            continue

        # Clean any remaining brackets on fallback tokens
        clean_tok = _fmt_frac_dot(tk.replace("[", "").replace("]", ""))
        stack.append(clean_tok)

    return steps[-1] if steps else (stack[-1] if stack else clause.replace("[", "").replace("]", ""))


def parse_tutor_setup_and_keys(sec_num: str, prob: Dict[str, Any]) -> tuple[str, str]:
    """Returns (paper_setup, sc6_keys) for a problem so the Coach Guide can display each on its own clean line."""
    keys = prob.get("keys", "").strip()
    if not keys:
        return ("", "")
    if "[" not in keys:
        return (keys, "Mental / Table Check")

    clauses = [c.strip() for c in keys.replace(" / ", "; ").split(";") if c.strip()]
    prev_pair: List[str] = []
    parsed_parts: List[str] = []
    for cl in clauses:
        p_str = _parse_single_rpn_clause(cl, prev_pair)
        if p_str:
            parsed_parts.append(p_str)
    paper_setup = "; ".join(parsed_parts) if parsed_parts else keys.replace("[", "").replace("]", "")
    return (paper_setup, keys)


def format_tutor_solution_step(sec_num: str, prob: Dict[str, Any]) -> str:
    """Converts a problem's RPN key sequence into a clear paper-and-pencil intermediate setup expression + SC-6 check for tutors and parents."""
    setup_str, keys_str = parse_tutor_setup_and_keys(sec_num, prob)
    if not setup_str:
        return ""
    if keys_str == "Mental / Table Check":
        return f"Setup: {setup_str}"
    return f"Setup: {setup_str}  |  SC-6: {keys_str}"

