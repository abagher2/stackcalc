#!/usr/bin/env python3
"""
Publication-Grade Section-by-Section Textbook Supplement & 10-Page Coach Guide Generator
for Big Ideas Math Middle School (SC-6 Elementary Calculator & Physical Manipulatives).

Produces:
  1. docs/downloads/worksheets/bigideas_middle_school_sc6_daily_student_workbook.pdf
     - 91 pages total (Page 1 Cover/Index + 90 Full Worksheets = 2 Worksheets per Section across all 45 Sections):
       * Practice A (Section X.Y — Key Ideas & Two-Method Practice):
         - Tracks exact Big Ideas Math Unit, Section, CCSS, and Key Vocabulary
         - Block Kit Used + 3D Render + 2D Vector Schematic + Step 1, Step 2, Step 3 physical block instructions
         - Worked Example teaching BOTH Big Ideas textbook methods side-by-side:
           Method 1 (+10 pts — 1st Token) vs. Method 2 (+20 pts DOUBLE — 2nd Token) + SC-6 Keystrokes + Final Answer
         - 10 Clean Textbook Practice Problems (#1-#10) using authentic Big Ideas Math terminology
           (Error Analysis, Modeling Real Life, etc.), zero boilerplate inside cards, and generous open workspace
       * Practice B (Section X.Y — Modeling Real Life & Multi-Method Applications):
         - Real-World Worked Example showing Method 1 (+10 pts) vs. Method 2 (+20 pts DOUBLE) + Block Connection + SC-6 Keys
         - 10 High-Interest "Modeling Real Life" Application Problems (#1-#10) with large open workspace
  2. docs/downloads/worksheets/bigideas_middle_school_sc6_teacher_coach_guide.pdf
     - Compact 10-Page Coach & Solution Guide (EXACTLY 1 page per Chapter for Units 1-10).
     - Includes Chapter Misconception & Block Remediation notes, Method 1 & Method 2 summary,
       Worked Example keys, and all 900 Practice Problem solutions + SC-6 keystrokes (Practice A #1-#10 & Practice B #1-#10).
  3. Synchronizes docs/curriculum/big-ideas-middle-school-sc6-workbook.md with all 45 sections,
     Key Vocabulary, Two-Method Worked Examples, Practice A (#1-#10), and Practice B (#1-#10).
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT / "Tools") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "Tools"))

from big_ideas_sc6_diagrams import (
    COMMON_TRAPS,
    draw_problem_workspace_organizer,
    draw_section_concept_diagram,
    format_tutor_solution_step,
    parse_tutor_setup_and_keys,
)
from big_ideas_sc6_pedagogy import SECTION_PEDAGOGY
from big_ideas_sc6_sections_data import CHAPTERS_DATA
from big_ideas_sc6_sheet_b_data import (
    MULTI_METHOD_BLOCK_NOTES,
    SHEET_B_PROBLEMS,
    clean_ex1_ans,
    clean_ex1_problem,
    clean_section_title,
    clean_sheet_a_prompt,
    get_starter_scaffold,
)
from big_ideas_sc6_stories import SC6_SECTION_CHECK_GUIDE, SECTION_STORY_PARAGRAPHS, UNIT_STORIES
from curriculum_shared import (
    BOOK_COVER_SPECS,
    draw_curriculum_bestseller_front_cover,
    draw_paper_keycap_sequence,
    generate_lulu_coil_cover_pdf,
    get_paper_keycap_png,
)


def clean_manipulative_label(raw: str) -> str:
    """Replaces internal SKU codes and 3D-printing jargon with clean pedagogical manipulative names."""
    replacements = {
        "COUNT-01 + PRIME-01": "Array Tiles & Prime Factor Towers",
        "FRAC-01 + PLACE-01": "Fraction Strips & Place Value Blocks",
        "FRAC-01 + BASE-10": "Fraction Strips & Ten-Frame Grids",
        "ALGB-01 + COUNT-01": "Algebra Tiles & Array Tiles",
        "COUNT-01 + TIME-01": "Polygon Grids & Geared Clock",
        "BASE-10 + PLACE-01": "Two-Tone Counters & Number Lines",
        "ALGB-01 + DOMI-01": "Balance Scale & Algebra Tiles",
        "PLACE-01 + ALGB-01": "Unit Cubes & 3D Nets",
        "COUNT-01 + PROB-01": "Data Towers & Quartile Strips",
        "PROB-01 + BASE-10": "Two-Tone Counters & Probability Dice",
        "COUNT-01": "Counting & Array Tiles",
        "PRIME-01": "Prime Factor Towers",
        "FRAC-01": "Fraction Strips",
        "PLACE-01": "Place Value Blocks",
        "BASE-10": "Ten-Frames & Two-Tone Counters",
        "DOMI-01": "Part-Whole Dominoes",
        "ALGB-01": "Algebra & Area Tiles",
        "TIME-01": "Geared Modulo-60 Clock",
        "PROB-01": "Probability Dice & Spinner",
        "STAT-01": "Data Distribution Towers",
        "QUEST-01": "100-Point Scoreboard",
        "84mm Fraction Studio": "Fraction Strips",
        "3x1x7U": "",
    }
    out = raw
    for k, v in replacements.items():
        out = out.replace(k, v)
    return " ".join(out.split())


DOCS_DIR = REPO_ROOT / "docs"
ASSETS_MANUALS_DIR = DOCS_DIR / "assets" / "manuals"
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
SCORING_GUIDE_PDF = OUT_DIR / "sc6_quest_token_scoring_guide.pdf"

FONT_SANS = "Helvetica"
FONT_SANS_BOLD = "Helvetica-Bold"
FONT_SANS_ITALIC = "Helvetica-Oblique"
FONT_MONO = "Courier"
FONT_MONO_BOLD = "Courier-Bold"

try:
    if (FONT_DIR / "SpaceMono-Regular.ttf").exists():
        pdfmetrics.registerFont(TTFont("SpaceMono", str(FONT_DIR / "SpaceMono-Regular.ttf")))
        pdfmetrics.registerFont(TTFont("SpaceMonoBold", str(FONT_DIR / "SpaceMono-Bold.ttf")))
        FONT_MONO = "SpaceMono"
        FONT_MONO_BOLD = "SpaceMonoBold"
    cmu_dir = FONT_DIR if (FONT_DIR / "CMUSerif-Regular.ttf").exists() else (WATCH_CALC_ROOT / "documentation")
    if (cmu_dir / "CMUSerif-Regular.ttf").exists() and (cmu_dir / "CMUSerif-Bold.ttf").exists():
        pdfmetrics.registerFont(TTFont("CMUSerif", str(cmu_dir / "CMUSerif-Regular.ttf")))
        pdfmetrics.registerFont(TTFont("CMUSerifBold", str(cmu_dir / "CMUSerif-Bold.ttf")))
        italic_ttf = cmu_dir / ("CMUSerif-Italic.ttf" if (cmu_dir / "CMUSerif-Italic.ttf").exists() else "CMUSerif-Regular.ttf")
        pdfmetrics.registerFont(TTFont("CMUSerifItalic", str(italic_ttf)))
        FONT_SANS = "CMUSerif"
        FONT_SANS_BOLD = "CMUSerifBold"
        FONT_SANS_ITALIC = "CMUSerifItalic"
    else:
        arial_dir = Path("/System/Library/Fonts/Supplemental")
        if (arial_dir / "Arial.ttf").exists() and (arial_dir / "Arial Bold.ttf").exists():
            pdfmetrics.registerFont(TTFont("BookSans", str(arial_dir / "Arial.ttf")))
            pdfmetrics.registerFont(TTFont("BookSansBold", str(arial_dir / "Arial Bold.ttf")))
            italic_ttf = arial_dir / ("Arial Italic.ttf" if (arial_dir / "Arial Italic.ttf").exists() else "Arial.ttf")
            pdfmetrics.registerFont(TTFont("BookSansItalic", str(italic_ttf)))
            FONT_SANS = "BookSans"
            FONT_SANS_BOLD = "BookSansBold"
            FONT_SANS_ITALIC = "BookSansItalic"
except Exception as exc:
    print(f"[WARN] Font registration fallback: {exc}")

# Clean Monochrome + Subtle Slate Palette (Kid-Friendly Print Clarity, Zero Visual Clutter)
INK = "#0F172A"
SLATE = "#334155"
MUTED = "#64748B"
BORDER = "#94A3B8"
LIGHT_BORDER = "#CBD5E1"
SUBTLE_HDR = "#F8FAFC"
M1_BG = "#F8FAFC"
M2_BG = "#F0F9FF"
WHITE = "#FFFFFF"
TEAL_ACCENT = "#0D5573"


def clean_pdf_text(txt: str) -> str:
    """Normalizes any Unicode glyphs outside CMUSerif/SpaceMono to 100% supported glyphs."""
    if not txt:
        return ""
    s = txt
    replacements = {
        "★★": "[+20 FAST]",
        "★": "*",
        "x⇄y": "x swap y",
        "⇄": " swap ",
        "↔": " swap ",
        "▸": "->",
        "yˣ": "y^x",
        "ˣ√y": "x√y",
        "ˣ": "^x",
        "⁰": "^0",
        "⁴": "^4",
        "⁵": "^5",
        "⁶": "^6",
        "⁷": "^7",
        "⁸": "^8",
        "⁹": "^9",
        "ⁿ": "^n",
        "₁": "1",
        "₂": "2",
        "₃": "3",
        "⅓": "1/3",
        "≈": "~",
        "≟": "=",
        "≠": "!=",
        "≤": "<=",
        "≥": ">=",
        "𝑥": "x",
        "●": "•",
        "a ᵇ/c": "a b/c",
        "0.3̄": "0.3-rep",
        "🕒": "CLK",
        "▦": "10F",
        "🎲": "DICE",
        "1…x": "1..x",
        "t…x": "t..x",
        "x̄": "x-bar",
        "X̄": "x-bar",
    }
    for k, v in replacements.items():
        s = s.replace(k, v)
    sku_replacements = {
        " (COUNT-01 / FRAC-01)": "",
        " (FRAC-01, 1 Whole = 84 mm)": "",
        "(TIME-01: 1 hr = 60 min)": "(1 hr = 60 min)",
        "COUNT-01: ": "Block Array: ",
        " in COUNT-01": "",
        "from Kit ALGB-01 ": "",
        "COUNT-01 grid": "coordinate grid",
        "FRAC-01 tray": "fraction tray",
        "PRIME-01 blocks": "prime blocks",
        "PRIME-01 Blocks": "Prime Blocks",
        " + Gridfinity 3x1 Sorting Tray": "",
        "Gridfinity ": "",
        "3x1x7U ": "",
        "84mm ": "",
    }
    for k, v in sku_replacements.items():
        s = s.replace(k, v)
    s = re.sub(
        r"\s*\((?:COUNT-01|PRIME-01|FRAC-01|PLACE-01|BASE-10|DOMI-01|ALGB-01|TIME-01|PROB-01|STAT-01|QUEST-01)\)",
        "",
        s,
    )
    return s


class CanvasPage:
    """Millimeter-calibrated ReportLab canvas helper (top-down Y coordinates in mm)."""

    def __init__(self, c: canvas.Canvas, size: Tuple[float, float] = letter):
        self.c = c
        self.w = size[0] / mm
        self.h = size[1] / mm

    def _pick_font(self, txt: str, bold: bool, italic: bool, mono: bool) -> str:
        if mono and not any(ch in txt for ch in ("Σ", "π", "≠", "≥", "≤", "√")):
            return FONT_MONO_BOLD if bold else FONT_MONO
        return FONT_SANS_BOLD if bold else (FONT_SANS_ITALIC if italic else FONT_SANS)

    def fit_text(self, txt: str, max_w: float, size: float, bold: bool = False, italic: bool = False, mono: bool = False) -> str:
        s = clean_pdf_text(txt)
        font = self._pick_font(s, bold, italic, mono)
        if self.c.stringWidth(s, font, size * mm) / mm <= max_w:
            return s
        while len(s) > 4 and self.c.stringWidth(s + "..", font, size * mm) / mm > max_w:
            s = s[:-1]
        return s.rstrip() + ".."

    def text(
        self,
        x: float,
        y: float,
        txt: str,
        size: float = 3.2,
        bold: bool = False,
        italic: bool = False,
        mono: bool = False,
        color: str = INK,
        align: str = "left",
        max_w: Optional[float] = None,
    ) -> float:
        s = clean_pdf_text(txt)
        font = self._pick_font(s, bold, italic, mono)
        if max_w is not None:
            actual_w = self.c.stringWidth(s, font, size * mm) / mm
            if actual_w > max_w and actual_w > 0:
                min_sz = max(1.08, size * 0.62)
                size = max(min_sz, size * (max_w / actual_w) * 0.99)
            s = self.fit_text(s, max_w, size, bold=bold, italic=italic, mono=mono)
        self.c.setFillColor(HexColor(color))
        self.c.setFont(font, size * mm)
        py = (self.h - y) * mm
        if align == "right":
            self.c.drawRightString(x * mm, py, s)
        elif align == "center":
            self.c.drawCentredString(x * mm, py, s)
        else:
            self.c.drawString(x * mm, py, s)
        return self.c.stringWidth(s, font, size * mm) / mm

    def para(
        self,
        x: float,
        y: float,
        txt: str,
        max_w: float,
        size: float = 2.9,
        bold: bool = False,
        italic: bool = False,
        mono: bool = False,
        color: str = INK,
        leading: float = 1.25,
        max_lines: Optional[int] = None,
    ) -> float:
        s = clean_pdf_text(txt)
        font = self._pick_font(s, bold, italic, mono)
        min_sz = size * 0.72
        while True:
            lines: List[str] = []
            for raw_ln in s.split("\n"):
                wrapped = simpleSplit(raw_ln, font, size * mm, max_w * mm)
                lines.extend(wrapped if wrapped else [""])
            if max_lines is None or len(lines) <= max_lines or size <= min_sz:
                break
            size = max(min_sz, size * 0.93)
        if max_lines is not None and len(lines) > max_lines:
            lines = lines[:max_lines]
        cur_y = y
        for ln in lines:
            self.text(x, cur_y, ln, size=size, bold=bold, italic=italic, mono=mono, color=color)
            cur_y += size * leading
        return cur_y

    def rect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        fill: Optional[str] = WHITE,
        stroke: Optional[str] = BORDER,
        r: float = 0.0,
        line_w: float = 0.25,
    ) -> None:
        self.c.saveState()
        self.c.setLineWidth(line_w * mm)
        if fill:
            self.c.setFillColor(HexColor(fill))
        if stroke:
            self.c.setStrokeColor(HexColor(stroke))
        if r > 0:
            self.c.roundRect(
                x * mm,
                (self.h - y - h) * mm,
                w * mm,
                h * mm,
                r * mm,
                fill=1 if fill else 0,
                stroke=1 if stroke else 0,
            )
        else:
            self.c.rect(
                x * mm,
                (self.h - y - h) * mm,
                w * mm,
                h * mm,
                fill=1 if fill else 0,
                stroke=1 if stroke else 0,
            )
        self.c.restoreState()

    def circle(
        self,
        cx: float,
        cy: float,
        r: float,
        fill: Optional[str] = WHITE,
        stroke: Optional[str] = INK,
        line_w: float = 0.25,
    ) -> None:
        self.c.saveState()
        self.c.setLineWidth(line_w * mm)
        if fill:
            self.c.setFillColor(HexColor(fill))
        if stroke:
            self.c.setStrokeColor(HexColor(stroke))
        self.c.circle(cx * mm, (self.h - cy) * mm, r * mm, fill=1 if fill else 0, stroke=1 if stroke else 0)
        self.c.restoreState()

    def line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        color: str = BORDER,
        width: float = 0.25,
        dashed: bool = False,
    ) -> None:
        self.c.saveState()
        self.c.setStrokeColor(HexColor(color))
        self.c.setLineWidth(width * mm)
        if dashed:
            self.c.setDash(2, 2)
        self.c.line(x1 * mm, (self.h - y1) * mm, x2 * mm, (self.h - y1 if y1 == y2 else self.h - y2) * mm)
        self.c.restoreState()

    def polygon(
        self,
        pts: List[Tuple[float, float]],
        fill: Optional[str] = None,
        stroke: Optional[str] = INK,
        line_w: float = 0.28,
    ) -> None:
        self.c.saveState()
        self.c.setLineWidth(line_w * mm)
        if fill:
            self.c.setFillColor(HexColor(fill))
        if stroke:
            self.c.setStrokeColor(HexColor(stroke))
        p = self.c.beginPath()
        p.moveTo(pts[0][0] * mm, (self.h - pts[0][1]) * mm)
        for px, py in pts[1:]:
            p.lineTo(px * mm, (self.h - py) * mm)
        p.close()
        self.c.drawPath(p, fill=1 if fill else 0, stroke=1 if stroke else 0)
        self.c.restoreState()

    def image(self, img_path: Path, x: float, y: float, w: float, h: float) -> None:
        if not img_path.exists():
            return
        self.c.drawImage(
            str(img_path),
            x * mm,
            (self.h - y - h) * mm,
            width=w * mm,
            height=h * mm,
            preserveAspectRatio=True,
            anchor="c",
            mask="auto",
        )

    def draw_tutorial_keycap(self, x: float, y: float, w: float = 4.6, h: float = 3.9) -> float:
        """Draws the authentic SC-6 Paper-theme [C] / Tutorial (?) keycap."""
        p_path, px_w, px_h, _ = get_paper_keycap_png("C", is_sc32=False)
        draw_w = h * (px_w / float(max(1, px_h)))
        self.c.drawImage(
            str(p_path),
            x * mm,
            (self.h - y - h) * mm,
            width=draw_w * mm,
            height=h * mm,
            preserveAspectRatio=True,
            mask="auto",
        )
        return draw_w

    def draw_keycap(self, label: str, x: float, y: float, h: float = 3.6) -> float:
        """Draws an authentic SC-6 Paper-theme hardware keycap."""
        raw_lbl = label.strip()
        if raw_lbl in ("?", "[?]", "C?"):
            return self.draw_tutorial_keycap(x, y, w=h * 1.25, h=h)
        end_x_pt = draw_paper_keycap_sequence(
            self.c,
            x * mm,
            (self.h - y - h) * mm,
            [raw_lbl],
            is_sc32=False,
            height=h * mm,
            spacing=0.45 * mm,
        )
        return max(h, (end_x_pt / mm) - x)

    def draw_keycap_sequence(
        self,
        keys: List[str],
        x: float,
        y: float,
        max_w: float,
        h: float = 3.5,
        gap: float = 0.75,
    ) -> float:
        """Draws an authentic SC-6 Paper-theme keycap sequence scaled cleanly to fit within `max_w`."""
        h_draw = max(h, 3.25)
        draw_paper_keycap_sequence(
            self.c,
            x * mm,
            (self.h - y - h_draw) * mm,
            keys,
            is_sc32=False,
            height=h_draw * mm,
            spacing=min(gap, 0.55) * mm,
            max_width=max_w * mm,
        )
        return y + h

    # =========================================================================
    # VECTOR BLOCK SCHEMATICS (100% Authentic Physical Block Diagrams)
    # =========================================================================
    def draw_block_schematic(self, dtype: str, ddata: Dict[str, Any], x: float, y: float, w: float, h: float) -> None:
        """Draws a crisp 2D schematic of the StackCalc blocks for the section's worked example."""
        self.rect(x, y, w, h, fill=WHITE, stroke=LIGHT_BORDER, r=1.0, line_w=0.25)

        if dtype == "array_rem":
            tile_s = 3.4
            gap = 0.42
            gx0 = x + 3.2
            gy0 = y + 4.0
            for r in range(5):
                for c in range(4):
                    self.rect(gx0 + c * (tile_s + gap), gy0 + r * (tile_s + gap), tile_s, tile_s, fill="#E2E8F0", stroke=INK, r=0.5, line_w=0.22)
            rx0 = gx0 + 4 * (tile_s + gap) + 3.8
            for rem_i in range(3):
                self.rect(rx0, gy0 + (2 + rem_i) * (tile_s + gap), tile_s, tile_s, fill="#CBD5E1", stroke=INK, r=0.5, line_w=0.25)
            self.text(gx0 + 7.6, y + 2.9, "M1: 5×4 Array (20)", size=1.82, bold=True, color=INK, align="center")
            self.text(rx0 + 1.8, gy0 + 4.0, "+3 Rem", size=1.82, bold=True, color=SLATE, align="center")
            self.text(rx0 + 1.8, gy0 + 6.5, "M2: 20+3", size=1.6, bold=True, mono=True, color=TEAL_ACCENT, align="center")

        elif dtype == "power_array":
            ts = 3.4
            gap = 0.42
            gx0 = x + 2.8
            gy0 = y + 4.8
            for r in range(4):
                for c in range(4):
                    self.rect(gx0 + c * (ts + gap), gy0 + r * (ts + gap), ts, ts, fill="#E2E8F0", stroke=INK, r=0.4, line_w=0.22)
            self.text(gx0 + 7.5, y + 3.3, "M1: 4² = 4×4 (16)", size=1.85, bold=True, color=INK, align="center")
            tx0 = gx0 + 4 * (ts + gap) + 4.4
            for r in range(2):
                for c in range(4):
                    self.rect(tx0 + c * (ts * 0.78 + gap), gy0 + 3.6 + r * (ts * 0.78 + gap), ts * 0.78, ts * 0.78, fill=WHITE, stroke=SLATE, r=0.3, line_w=0.2)
            self.text(tx0 + 6.2, gy0 + 2.2, "M2: Not 4×2 (8)!", size=1.7, bold=True, color=TEAL_ACCENT, align="center")

        elif dtype == "two_room":
            r1 = ddata.get("room1", "8 + 4 = 12")
            r2 = ddata.get("room2", "9 - 3 = 6")
            res = ddata.get("res", "72")
            self.rect(x + 2.0, y + 2.2, w - 4.0, 6.8, fill="#F1F5F9", stroke=INK, r=0.8, line_w=0.25)
            self.text(x + w / 2.0, y + 4.8, "M1 ZONE 1 TILES:", size=1.7, bold=True, mono=True, color=SLATE, align="center")
            self.text(x + w / 2.0, y + 7.5, r1, size=1.9, bold=True, mono=True, color=INK, align="center", max_w=w - 6.0)

            self.rect(x + 2.0, y + 10.4, w - 4.0, 6.8, fill="#E2E8F0", stroke=INK, r=0.8, line_w=0.25)
            self.text(x + w / 2.0, y + 13.0, "M2 ZONE 2 / SPLIT:", size=1.7, bold=True, mono=True, color=SLATE, align="center")
            self.text(x + w / 2.0, y + 15.7, r2, size=1.9, bold=True, mono=True, color=INK, align="center", max_w=w - 6.0)

            self.text(x + w / 2.0, y + 21.0, f"M1 = M2 ==> {res}", size=1.95, bold=True, mono=True, color=TEAL_ACCENT, align="center", max_w=w - 4.0)

        elif dtype == "prime_tower":
            base_y = y + h - 2.6
            axis_x = x + 8.8
            self.line(axis_x, y + 2.6, axis_x, base_y, color=INK, width=0.35)
            for val, frac_h in [(1, 0.0), (2, 0.17), (4, 0.34), (12, 0.61), (60, 1.0)]:
                ty = base_y - frac_h * (h - 6.2)
                self.line(axis_x - 1.4, ty, axis_x, ty, color=INK, width=0.25)
                self.text(axis_x - 1.9, ty + 0.75, str(val), size=1.7, bold=(val == 60), mono=True, color=INK, align="right")

            bx = axis_x + 3.8
            bw = 12.5
            tot_h = h - 6.2
            blocks = [(2, 0.17, "#DBEAFE"), (2, 0.17, "#DBEAFE"), (3, 0.27, "#DCFCE7"), (5, 0.39, "#FEF3C7")]
            cur_by = base_y
            for pval, ph_ratio, bcol in blocks:
                bh = ph_ratio * tot_h
                self.rect(bx, cur_by - bh, bw, bh, fill=bcol, stroke=INK, r=0.4, line_w=0.25)
                self.text(bx + bw / 2.0, cur_by - bh / 2.0 + 0.7, f"[{pval}]", size=1.9, bold=True, mono=True, color=INK, align="center")
                cur_by -= bh
            self.line(axis_x, cur_by, bx, cur_by, color=TEAL_ACCENT, width=0.3, dashed=True)
            self.text(bx + bw + 1.4, y + 6.8, "M1: Tree", size=1.75, bold=True, mono=True, color=INK)
            self.text(bx + bw + 1.4, y + 9.8, "M2: Ladder", size=1.75, bold=True, mono=True, color=TEAL_ACCENT)
            self.text(bx + bw + 1.4, y + 13.0, "2²×3×5=60", size=1.75, bold=True, mono=True, color=INK)

        elif dtype == "gcf_lcm_towers":
            base_y = y + h - 2.8
            tot_h = h - 6.6
            cols = [
                ("20", [(2, 0.2), (2, 0.2), (5, 0.35)], x + 2.2),
                ("50", [(2, 0.2), (5, 0.35), (5, 0.35)], x + 12.4),
                ("GCF=10", [(2, 0.2), (5, 0.35)], x + 22.6),
                ("LCM=100", [(2, 0.18), (2, 0.18), (5, 0.32), (5, 0.32)], x + 32.8),
            ]
            for lbl, blks, cx in cols:
                cur_y = base_y
                for pval, r_h in blks:
                    bh = r_h * tot_h
                    fill_c = "#DBEAFE" if pval == 2 else "#FEF3C7"
                    self.rect(cx, cur_y - bh, 7.8, bh, fill=fill_c, stroke=INK, r=0.3, line_w=0.22)
                    self.text(cx + 3.9, cur_y - bh / 2.0 + 0.65, str(pval), size=1.7, bold=True, mono=True, color=INK, align="center")
                    cur_y -= bh
                self.text(cx + 3.9, base_y + 2.0, lbl, size=1.5, bold=True, mono=True, color=INK, align="center")

        elif dtype == "fraction_towers":
            base_y = y + h - 3.1
            max_h = h - 6.6
            bars = [
                ("1", [1.0], "#E2E8F0", x + 2.8),
                ("2/3", [1 / 3, 1 / 3], "#DBEAFE", x + 13.0),
                ("4/6", [1 / 6] * 4, "#DCFCE7", x + 23.2),
                ("7/12", [1 / 3, 1 / 4], "#FEF3C7", x + 33.4),
            ]
            for lbl, segs, col_hex, bx in bars:
                cur_y = base_y
                for s in segs:
                    sh = s * max_h
                    self.rect(bx, cur_y - sh, 7.8, sh, fill=col_hex, stroke=INK, r=0.3, line_w=0.22)
                    cur_y -= sh
                self.text(bx + 3.9, base_y + 2.1, lbl, size=1.65, bold=True, mono=True, color=INK, align="center")
            y_23 = base_y - (2 / 3) * max_h
            self.line(x + 13.0, y_23, x + 31.0, y_23, color=TEAL_ACCENT, width=0.3, dashed=True)

        elif dtype == "place_value":
            num_str = ddata.get("num", "14.85")
            ip_str = ddata.get("ip", "14")
            fp_str = ddata.get("fp", "0.85")
            self.text(x + w / 2.0, y + 4.0, f"Value: {num_str}", size=2.0, bold=True, mono=True, color=INK, align="center")
            bw = (w - 5.6) / 2.0
            self.rect(x + 1.8, y + 6.0, bw, 13.6, fill="#F1F5F9", stroke=INK, r=0.8, line_w=0.25)
            self.text(x + 1.8 + bw / 2.0, y + 9.8, "Whole Part", size=1.7, bold=True, color=SLATE, align="center")
            self.text(x + 1.8 + bw / 2.0, y + 14.2, ip_str, size=2.0, bold=True, mono=True, color=INK, align="center", max_w=bw - 1.5)
            self.text(x + 1.8 + bw / 2.0, y + 17.8, "Tens & Ones", size=1.55, mono=True, color=MUTED, align="center")

            rx = x + 3.8 + bw
            self.rect(rx, y + 6.0, bw, 13.6, fill="#E2E8F0", stroke=INK, r=0.8, line_w=0.25)
            self.text(rx + bw / 2.0, y + 9.8, "Decimal Part", size=1.7, bold=True, color=TEAL_ACCENT, align="center")
            self.text(rx + bw / 2.0, y + 14.2, fp_str, size=2.0, bold=True, mono=True, color=INK, align="center", max_w=bw - 1.5)
            self.text(rx + bw / 2.0, y + 17.8, "0.1 & 0.01", size=1.55, mono=True, color=MUTED, align="center")

        elif dtype == "ratio_tape":
            a = min(5, int(ddata.get("a", 3)))
            b = min(5, int(ddata.get("b", 2)))
            uval = ddata.get("unit_val", 4)
            ts = 5.8
            gap = 0.55
            gx0 = x + 3.2
            self.text(gx0, y + 3.9, f"Part A ({a} boxes):", size=1.8, bold=True, color=INK)
            for i in range(a):
                self.rect(gx0 + i * (ts + gap), y + 5.0, ts, 4.6, fill="#DBEAFE", stroke=INK, r=0.5, line_w=0.25)
                self.text(gx0 + i * (ts + gap) + ts / 2.0, y + 8.0, str(uval), size=1.9, bold=True, mono=True, color=INK, align="center")
            self.text(gx0, y + 12.8, f"Part B ({b} boxes):", size=1.8, bold=True, color=INK)
            for i in range(b):
                self.rect(gx0 + i * (ts + gap), y + 13.9, ts, 4.6, fill="#FEF3C7", stroke=INK, r=0.5, line_w=0.25)
                self.text(gx0 + i * (ts + gap) + ts / 2.0, y + 16.9, str(uval), size=1.9, bold=True, mono=True, color=INK, align="center")
            self.text(x + w / 2.0, y + 21.8, f"M1: {a}:{b} Tape | M2: {a+b} Boxes", size=1.72, bold=True, mono=True, color=TEAL_ACCENT, align="center")

        elif dtype == "percent_bar":
            bw = w - 5.6
            bx = x + 2.8
            by = y + 7.0
            bh = 5.8
            self.rect(bx, by, bw, bh, fill="#F1F5F9", stroke=INK, r=0.6, line_w=0.25)
            self.rect(bx, by, bw * 0.75, bh, fill="#DBEAFE", stroke=INK, r=0.6, line_w=0.25)
            for q in range(1, 4):
                qx = bx + bw * (q * 0.25)
                self.line(qx, by, qx, by + bh, color=INK, width=0.22, dashed=True)
            self.text(x + w / 2.0, y + 4.9, "M1: 3/4  |  M2: 0.75 = 75%", size=1.82, bold=True, mono=True, color=INK, align="center")
            self.text(bx, by + bh + 3.1, "0%", size=1.7, mono=True, color=SLATE)
            self.text(bx + bw * 0.75, by + bh + 3.1, "75%", size=1.8, bold=True, mono=True, color=TEAL_ACCENT, align="center")
            self.text(bx + bw, by + bh + 3.1, "100%", size=1.7, mono=True, color=SLATE, align="right")

        elif dtype == "algebra_tiles":
            gx = x + 2.8
            gy = y + 3.6
            self.rect(gx, gy, 9.5, 9.5, fill="#DBEAFE", stroke=INK, r=0.6, line_w=0.25)
            self.text(gx + 4.75, gy + 5.5, "x²", size=2.2, bold=True, mono=True, color=INK, align="center")
            rx = gx + 11.4
            for i in range(3):
                self.rect(rx + i * 4.5, gy, 3.8, 9.5, fill="#DCFCE7", stroke=INK, r=0.4, line_w=0.22)
                self.text(rx + i * 4.5 + 1.9, gy + 5.5, "x", size=1.85, bold=True, mono=True, color=INK, align="center")
            ux = rx + 14.8
            for r in range(2):
                for c in range(2):
                    self.rect(ux + c * 3.8, gy + r * 3.8, 3.2, 3.2, fill="#FEF3C7", stroke=INK, r=0.3, line_w=0.2)
                    self.text(ux + c * 3.8 + 1.6, gy + r * 3.8 + 2.2, "1", size=1.55, bold=True, mono=True, color=INK, align="center")
            self.text(x + w / 2.0, y + 18.0, "M1: Like Terms | M2: Sub x", size=1.7, bold=True, color=SLATE, align="center")
            self.text(x + w / 2.0, y + 21.2, "x²-Flats | x-Rods | 1-Cubes", size=1.7, bold=True, mono=True, color=INK, align="center")

        elif dtype == "polygon_area":
            shape = ddata.get("shape", "parallelogram")
            if shape == "parallelogram":
                pts = [(x + 7.5, y + 5.0), (x + 31.0, y + 5.0), (x + 26.0, y + 16.5), (x + 2.5, y + 16.5)]
                self.polygon(pts, fill="#E2E8F0", stroke=INK, line_w=0.3)
                self.line(x + 7.5, y + 5.0, x + 7.5, y + 16.5, color=TEAL_ACCENT, width=0.3, dashed=True)
                self.text(x + w / 2.0, y + 20.5, "M1: Cut-Slide | M2: b×h=12×8", size=1.68, bold=True, mono=True, color=INK, align="center")
                self.text(x + 13.0, y + 12.0, "h = 8", size=1.85, bold=True, mono=True, color=TEAL_ACCENT)
                self.text(x + 31.8, y + 12.0, "x10", size=1.65, mono=True, color=MUTED)
            elif shape == "triangle":
                self.rect(x + 5.5, y + 4.2, 27.0, 12.2, fill="#F8FAFC", stroke=BORDER, line_w=0.2)
                pts = [(x + 5.5, y + 16.4), (x + 32.5, y + 16.4), (x + 5.5, y + 4.2)]
                self.polygon(pts, fill="#DBEAFE", stroke=INK, line_w=0.3)
                self.text(x + w / 2.0, y + 20.6, "M1: ½(b×h) | M2: (b÷2)×h", size=1.7, bold=True, mono=True, color=INK, align="center")
            else:
                self.rect(x + 9.5, y + 9.8, 21.0, 9.0, fill="#E2E8F0", stroke=INK, line_w=0.28)
                pts = [(x + 9.5, y + 9.8), (x + 30.5, y + 9.8), (x + 20.0, y + 3.5)]
                self.polygon(pts, fill="#DBEAFE", stroke=INK, line_w=0.28)
                self.text(x + 20.0, y + 15.2, "Rectangle", size=1.75, bold=True, color=INK, align="center")
                self.text(x + 20.0, y + 8.8, "Triangle", size=1.65, bold=True, color=INK, align="center")
                self.text(x + w / 2.0, y + 21.8, "M1: Split Sum | M2: Box-Cut", size=1.68, bold=True, color=TEAL_ACCENT, align="center")

        elif dtype == "clock_dial":
            cx = x + w / 2.0
            cy = y + 10.6
            r = 7.5
            self.circle(cx, cy, r, fill="#F8FAFC", stroke=INK, line_w=0.3)
            for hr in range(12):
                ang = math.radians(hr * 30 - 90)
                self.line(
                    cx + (r - 1.1) * math.cos(ang),
                    cy + (r - 1.1) * math.sin(ang),
                    cx + r * math.cos(ang),
                    cy + r * math.sin(ang),
                    color=INK,
                    width=0.22,
                )
            self.line(cx, cy, cx + 4.0, cy - 1.7, color=INK, width=0.45)
            self.line(cx, cy, cx - 5.6, cy, color=TEAL_ACCENT, width=0.35)
            self.text(cx, y + 21.8, "M1: Jump Line | M2: 1 hr = 60 min", size=1.65, bold=True, mono=True, color=INK, align="center")

        elif dtype == "zero_pairs":
            gx = x + 5.2
            gy = y + 5.5
            for i in range(4):
                cx = gx + i * 8.2
                self.circle(cx, gy, 2.5, fill="#FEF3C7", stroke=INK, line_w=0.25)
                self.text(cx, gy + 0.8, "+", size=2.0, bold=True, mono=True, color=INK, align="center")
                if i < 3:
                    self.circle(cx, gy + 6.8, 2.5, fill="#FEE2E2", stroke=INK, line_w=0.25)
                    self.text(cx, gy + 7.6, "-", size=2.0, bold=True, mono=True, color=INK, align="center")
                    self.rect(cx - 2.95, gy - 2.95, 5.9, 12.7, fill=None, stroke=SLATE, r=1.0, line_w=0.2)
            ny = y + 19.8
            self.line(x + 2.4, ny, x + w - 2.4, ny, color=INK, width=0.3)
            self.line(x + w / 2.0, ny - 1.3, x + w / 2.0, ny + 1.3, color=INK, width=0.3)
            self.text(x + w / 2.0, ny + 2.8, "M1: Chips | M2: Line", size=1.6, bold=True, mono=True, color=INK, align="center")
            self.text(x + 2.8, ny - 1.6, "<- (-)", size=1.55, color=SLATE)
            self.text(x + w - 2.8, ny - 1.6, "(+) ->", size=1.55, color=TEAL_ACCENT, align="right")

        elif dtype == "coord_plane":
            cx = x + w / 2.0
            cy = y + 11.6
            span = 8.5
            self.line(cx - span - 2.5, cy, cx + span + 2.5, cy, color=INK, width=0.3)
            self.line(cx, cy - span, cx, cy + span, color=INK, width=0.3)
            self.text(cx + 6.2, cy - 3.9, "QI (+,+)", size=1.6, bold=True, mono=True, color=INK, align="center")
            self.text(cx - 6.2, cy - 3.9, "QII (-,+)", size=1.6, bold=True, mono=True, color=SLATE, align="center")
            self.text(cx - 6.2, cy + 5.8, "QIII (-,-)", size=1.6, bold=True, mono=True, color=SLATE, align="center")
            self.text(cx + 6.2, cy + 5.8, "QIV (+,-)", size=1.6, bold=True, mono=True, color=INK, align="center")
            self.circle(cx + 4.8, cy - 2.6, 0.95, fill=TEAL_ACCENT, stroke=INK, line_w=0.2)
            self.circle(cx - 4.8, cy - 2.6, 0.95, fill="#D97706", stroke=INK, line_w=0.2)

        elif dtype == "balance_scale":
            left_lbl = ddata.get("left", "3x + 7")
            right_lbl = ddata.get("right", "28")
            sol_lbl = ddata.get("sol", "x = 7")
            cx = x + w / 2.0
            by = y + 14.8
            self.line(x + 3.2, by, x + w - 3.2, by, color=INK, width=0.45)
            self.polygon([(cx, by), (cx - 2.5, by + 3.6), (cx + 2.5, by + 3.6)], fill=INK, stroke=INK)
            self.text(cx, by - 1.0, "=", size=2.3, bold=True, mono=True, color=INK, align="center")
            pw = (w - 8.5) / 2.0
            self.rect(x + 2.2, y + 5.4, pw, 7.8, fill="#DCFCE7", stroke=INK, r=0.6, line_w=0.25)
            self.text(x + 2.2 + pw / 2.0, y + 8.4, "Left Side:", size=1.6, bold=True, color=SLATE, align="center")
            self.text(x + 2.2 + pw / 2.0, y + 11.6, left_lbl, size=1.85, bold=True, mono=True, color=INK, align="center", max_w=pw - 1.5)
            rx = x + w - 2.2 - pw
            self.rect(rx, y + 5.4, pw, 7.8, fill="#FEF3C7", stroke=INK, r=0.6, line_w=0.25)
            self.text(rx + pw / 2.0, y + 8.4, "Right Side:", size=1.6, bold=True, color=SLATE, align="center")
            self.text(rx + pw / 2.0, y + 11.6, right_lbl, size=1.85, bold=True, mono=True, color=INK, align="center", max_w=pw - 1.5)
            self.text(cx, y + 22.0, f"M1/M2: {sol_lbl}", size=1.72, bold=True, mono=True, color=TEAL_ACCENT, align="center", max_w=w - 3.0)

        elif dtype == "solid_3d":
            mode = ddata.get("mode", "net")
            if mode == "net":
                cx = x + 15.8
                cy = y + 8.2
                self.rect(cx, cy, 7.6, 4.5, fill="#DBEAFE", stroke=INK, line_w=0.25)
                self.rect(cx, cy - 3.6, 7.6, 3.6, fill="#DCFCE7", stroke=INK, line_w=0.25)
                self.rect(cx, cy + 4.5, 7.6, 3.6, fill="#DCFCE7", stroke=INK, line_w=0.25)
                self.rect(cx, cy + 8.1, 7.6, 4.5, fill="#DBEAFE", stroke=INK, line_w=0.25)
                self.rect(cx - 4.5, cy, 4.5, 4.5, fill="#FEF3C7", stroke=INK, line_w=0.25)
                self.rect(cx + 7.6, cy, 4.5, 4.5, fill="#FEF3C7", stroke=INK, line_w=0.25)
                self.text(x + w / 2.0, y + 22.2, "M1: 2D Net | M2: Face Pairs", size=1.68, bold=True, mono=True, color=INK, align="center")
            else:
                bx, by, bw, bh = x + 8.5, y + 7.0, 17.0, 10.0
                dx, dy = 4.8, -3.5
                self.rect(bx, by, bw, bh, fill="#E2E8F0", stroke=INK, line_w=0.28)
                self.polygon([(bx, by), (bx + dx, by + dy), (bx + bw + dx, by + dy), (bx + bw, by)], fill="#F1F5F9", stroke=INK, line_w=0.25)
                self.polygon([(bx + bw, by), (bx + bw + dx, by + dy), (bx + bw + dx, by + bh + dy), (bx + bw, by + bh)], fill="#CBD5E1", stroke=INK, line_w=0.25)
                self.text(x + w / 2.0, y + 21.6, "M1: Layer×h | M2: V = l×w×h", size=1.65, bold=True, mono=True, color=TEAL_ACCENT, align="center")

        elif dtype == "stat_plot":
            mode = ddata.get("mode", "mean_towers")
            if mode == "boxplot":
                by = y + 10.6
                x_min, x_q1, x_med, x_q3, x_max = x + 4.2, x + 11.5, x + 20.8, x + 30.0, x + 38.2
                self.line(x_min, by, x_q1, by, color=INK, width=0.35)
                self.line(x_q3, by, x_max, by, color=INK, width=0.35)
                self.line(x_min, by - 2.2, x_min, by + 2.2, color=INK, width=0.35)
                self.line(x_max, by - 2.2, x_max, by + 2.2, color=INK, width=0.35)
                self.rect(x_q1, by - 3.6, x_q3 - x_q1, 7.2, fill="#DBEAFE", stroke=INK, line_w=0.3)
                self.line(x_med, by - 3.6, x_med, by + 3.6, color=TEAL_ACCENT, width=0.45)
                self.text(x_min, by + 5.8, "Min", size=1.5, bold=True, mono=True, align="center")
                self.text(x_q1, by + 5.8, "Q1", size=1.5, bold=True, mono=True, align="center")
                self.text(x_med, by + 5.8, "Med", size=1.5, bold=True, mono=True, color=TEAL_ACCENT, align="center")
                self.text(x_q3, by + 5.8, "Q3", size=1.5, bold=True, mono=True, align="center")
                self.text(x_max, by + 5.8, "Max", size=1.5, bold=True, mono=True, align="center")
                self.text(x + w / 2.0, y + 21.6, "M1: Peel Ends | M2: IQR=Q3-Q1", size=1.65, bold=True, mono=True, color=INK, align="center")
            else:
                towers = ddata.get("towers", [3, 7, 5, 9, 6])[:5]
                mean_v = ddata.get("mean", 6)
                base_y = y + 19.2
                max_v = max(towers + [1])
                scale_h = 12.8 / max_v
                for idx, tv in enumerate(towers):
                    tx = x + 4.8 + idx * 6.5
                    th = tv * scale_h
                    self.rect(tx, base_y - th, 4.5, th, fill="#DBEAFE", stroke=INK, r=0.3, line_w=0.22)
                    self.text(tx + 2.25, base_y + 2.4, str(tv), size=1.6, bold=True, mono=True, align="center")
                my = base_y - mean_v * scale_h
                self.line(x + 2.4, my, x + w - 2.4, my, color=TEAL_ACCENT, width=0.35, dashed=True)
                self.text(x + w / 2.0, y + 3.6, f"M1: Level={mean_v} | M2: Sum÷5", size=1.68, bold=True, mono=True, color=TEAL_ACCENT, align="center")

        else:  # prob_spinner
            cx = x + 13.0
            cy = y + 11.4
            r = 7.2
            self.circle(cx, cy, r, fill="#F8FAFC", stroke=INK, line_w=0.3)
            for s in range(10):
                ang = math.radians(s * 36 - 90)
                self.line(cx, cy, cx + r * math.cos(ang), cy + r * math.sin(ang), color=BORDER, width=0.2)
            self.line(cx, cy, cx + 4.5, cy - 3.0, color=INK, width=0.45)
            self.rect(x + 25.0, y + 6.6, 10.0, 10.0, fill="#E2E8F0", stroke=INK, r=1.1, line_w=0.28)
            for dx, dy in [(-2.2, -2.2), (2.2, -2.2), (0, 0), (-2.2, 2.2), (2.2, 2.2)]:
                self.circle(x + 30.0 + dx, y + 11.6 + dy, 0.6, fill=INK, stroke=INK)
            self.text(x + w / 2.0, y + 21.8, "M1: Grid/Tree | M2: Count Rule", size=1.62, bold=True, mono=True, color=INK, align="center")


# =============================================================================
# 1. STUDENT WORKBOOK GENERATOR (1 Cover Page + 90 Full Worksheets = 91 Pages)
# =============================================================================
def draw_student_cover_page(p: CanvasPage, chapters: List[Dict[str, Any]]) -> None:
    margin = 12.0
    uw = p.w - 2 * margin

    p.text(
        margin,
        14.0,
        "STACKCALC LEARNING LAB  •  BIG IDEAS MATH MIDDLE SCHOOL SUPPLEMENT (90 WORKSHEETS • 900 PROBLEMS)",
        size=2.5,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
    )
    p.text(margin, 21.8, "Big Ideas Math Middle School: Two-Method Block & SC-6 Workbook", size=5.2, bold=True, color=INK)
    p.text(
        margin,
        27.2,
        "45 Textbook Sections × 2 Full Practice Sheets (Practice A: Key Ideas + Practice B: Modeling Real Life) • 90 Two-Method Worked Examples",
        size=2.65,
        color=SLATE,
    )
    p.line(margin, 29.8, margin + uw, 29.8, color=INK, width=0.5)

    cw = (uw - 6.0) / 3.0
    cards = [
        (
            "1. HOW THE BOOK TEACHES IT",
            "Every worksheet teaches the exact vocabulary, algorithms, and two core solution methods from Big Ideas Math so students master the exact concepts they are tested on in class.",
        ),
        (
            "2. TWO WAYS = DOUBLE POINTS (+20)",
            "Every Worked Example models TWO textbook ways to solve: Method 1 (+10 pts — 1st Token) and Method 2 (+20 pts DOUBLE — 2nd Token), reinforced by hands-on blocks where applicable and SC-6 check.",
        ),
        (
            "3. 2 SHEETS PER SECTION (900 PROBLEMS)",
            "Each section includes Practice A (Key Ideas & Error Analysis) and Practice B (Modeling Real Life Applications) with generous open workspace to work out every problem and write your final answer.",
        ),
    ]
    for i, (ctitle, cbody) in enumerate(cards):
        cx = margin + i * (cw + 3.0)
        p.rect(cx, 32.2, cw, 25.2, fill=WHITE, stroke=INK, r=1.2, line_w=0.3)
        p.rect(cx, 32.2, cw, 5.4, fill=INK, stroke=INK, r=0.8, line_w=0.2)
        p.text(cx + 2.5, 35.9, ctitle, size=1.95, bold=True, mono=True, color=WHITE)
        if i == 1:
            p.draw_tutorial_keycap(cx + cw - 6.2, 32.8, w=4.6, h=4.0)
        p.para(cx + 2.5, 40.8, cbody, max_w=cw - 5.0, size=2.25, color=INK, leading=1.25)

    p.rect(margin, 59.8, uw, 30.8, fill=SUBTLE_HDR, stroke=BORDER, r=1.2, line_w=0.25)
    p.text(
        margin + 3.0,
        64.0,
        "HANDS-ON MANIPULATIVES REINFORCE TEXTBOOK CONCEPTS & DOUBLE-POINTS SCORING (+10 / +20 TOKENS)",
        size=2.12,
        bold=True,
        mono=True,
        color=INK,
    )
    p.draw_tutorial_keycap(margin + uw - 7.6, 60.6, w=4.6, h=4.0)
    showcase = [
        ("counting_tiles_array_3x8.png", "Counting & Array Tiles"),
        ("prime_lcm_gcd_venn.png", "Prime Factor Towers"),
        ("fraction_studio_common_denominator.png", "Fraction Strips"),
        ("algebra_factoring_area.png", "Algebra & Area Tiles"),
        ("planetary_geared_clock_330.png", "Geared Base-60 Clock"),
    ]
    sw_w = (uw - 10.0) / 5.0
    for idx, (png_name, cap) in enumerate(showcase):
        sx = margin + 2.0 + idx * sw_w
        p.rect(sx + 1.0, 65.8, sw_w - 2.0, 19.2, fill=WHITE, stroke=LIGHT_BORDER, r=0.8, line_w=0.2)
        p.image(ASSETS_MANUALS_DIR / png_name, sx + 2.0, 66.6, sw_w - 4.0, 17.6)
        p.text(sx + sw_w / 2.0, 88.4, cap, size=1.95, bold=True, color=SLATE, align="center")

    ty = 93.6
    p.rect(margin, ty, uw, 6.0, fill=INK, stroke=INK, line_w=0.3)
    p.text(margin + 2.5, ty + 4.1, "UNIT / CHAPTER & BIG IDEAS ALIGNMENT", size=2.05, bold=True, mono=True, color=WHITE)
    p.text(margin + 71.5, ty + 4.1, "SECTIONS & WORKSHEETS (PRACTICE A & B)", size=2.05, bold=True, mono=True, color=WHITE)
    p.text(margin + 143.5, ty + 4.1, "TWO-METHOD DOUBLE POINTS FOCUS", size=2.0, bold=True, mono=True, color=WHITE)

    unit_methods_summary = {
        1: "Arrays vs Div Check; Trees vs Ladders",
        2: "LCD Strips vs Cross-Mult; Reciprocals",
        3: "Tape Diagrams vs Ratio Tables & Rates",
        4: "Substitution, Like Terms & Area vs GCF",
        5: "Cut-and-Slide Grids vs Polygon Formulas",
        6: "Number Lines vs Opposites & |x| Sums",
        7: "Mental Inspection vs Inverse Operations",
        8: "Unfolded 2D Nets vs Prism/Cone Formulas",
        9: "Fair-Share Leveling vs IQR & MAD Tables",
        10: "Zero-Pair Chips vs Rules & Sample Space",
    }
    row_h = 16.2
    for idx, ch in enumerate(chapters):
        ry = ty + 6.0 + idx * row_h
        bg = WHITE if idx % 2 == 0 else SUBTLE_HDR
        p.rect(margin, ry, uw, row_h, fill=bg, stroke=LIGHT_BORDER, line_w=0.2)
        p.line(margin + 70.0, ry, margin + 70.0, ry + row_h, color=LIGHT_BORDER, width=0.2)
        p.line(margin + 142.0, ry, margin + 142.0, ry + row_h, color=LIGHT_BORDER, width=0.2)

        unit_story_pg = 3 + (ch["num"] - 1) + (ch["sections"][0]["day_num"] - 1) * 2
        clean_tools = clean_manipulative_label(ch["kit_summary"])
        p.text(margin + 2.2, ry + 4.3, f"Unit {ch['num']} (p.{unit_story_pg}): {ch['title']}", size=2.22, bold=True, color=INK, max_w=66.0)
        p.para(margin + 2.2, ry + 7.8, f"{ch['big_ideas_book']} • {clean_tools}", max_w=66.0, size=1.9, color=SLATE, max_lines=2)

        for li, s in enumerate(ch["sections"]):
            pg_a = 3 + ch["num"] + (s["day_num"] - 1) * 2
            pg_b = pg_a + 1
            stitle = clean_section_title(s["sec_num"], s["title"])
            sl = f"[ ] Sec {s['sec_num']} (pp.{pg_a}-{pg_b}): {stitle}"
            p.text(margin + 71.5, ry + 3.4 + li * 2.9, sl, size=1.82, color=INK, max_w=69.0)

        m_sum = unit_methods_summary.get(ch["num"], "")
        n_probs = len(ch["sections"]) * 20
        p.text(margin + 143.5, ry + 5.0, m_sum, size=1.85, bold=True, color=INK, max_w=46.0)
        p.text(margin + 143.5, ry + 9.4, f"Model: {clean_tools.split('&')[0].strip()}", size=1.78, mono=True, color=SLATE, max_w=46.0)
        p.text(margin + 143.5, ry + 13.7, f"[ ] Story + {len(ch['sections'])*2} Sheets ({n_probs} Probs)", size=1.78, bold=True, color=TEAL_ACCENT, max_w=46.0)

    p.text(
        margin,
        p.h - 6.0,
        "StackCalc Learning Systems  •  Big Ideas Math Middle School Supplement (Token Scoring Guide p.2 • 10 Unit Stories • 45 Sections • 90 Worksheets)",
        size=1.92,
        mono=True,
        color=MUTED,
        max_w=uw - 28.0,
    )
    p.text(margin + uw, p.h - 6.0, "Page 1 of 111", size=2.0, bold=True, mono=True, color=INK, align="right")


def draw_token_scoring_guide_page(p: CanvasPage, chapters: List[Dict[str, Any]], page_label: str = "Page 2 of 111") -> None:
    """Renders the 1-Page Token Scoring & SC-6 Work-Check Guide."""
    margin = 11.0
    uw = p.w - 2 * margin

    # 1. Top Header (y = 9.0 .. 24.8 mm)
    p.text(
        margin,
        12.2,
        "STACKCALC LEARNING LAB  •  TWO-METHOD TOKEN SCORING & SC-6 WORK-CHECK PROTOCOL",
        size=2.0,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=120.0,
    )
    p.rect(margin + uw - 72.0, 9.0, 72.0, 4.6, fill=SUBTLE_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(
        margin + uw - 36.0,
        12.1,
        "100-POINT GOAL: +10 (1ST WAY) & +20 (2ND WAY)",
        size=1.72,
        bold=True,
        mono=True,
        color=INK,
        align="center",
        max_w=69.0,
    )

    p.text(
        margin,
        18.2,
        "1-Page Token Scoring & SC-6 Work-Check Guide",
        size=4.2,
        bold=True,
        color=INK,
        max_w=uw,
    )
    p.text(
        margin,
        23.2,
        "How to Solve by Hand First, Earn +10 Single-Way & +20 Double-Points Tokens, Check Your Work on the SC-6, and Reach 100 Points",
        size=1.92,
        bold=True,
        color=SLATE,
        max_w=uw,
    )
    p.line(margin, 24.8, margin + uw, 24.8, color=INK, width=0.45)

    # 2. The 4-Step "Learn First, Then Check" Daily Loop (y = 26.2 .. 68.2 mm, height = 42.0 mm)
    step_y = 26.2
    step_h = 42.0
    col_w = (uw - 7.5) / 4.0
    step_cards = [
        (
            "STEP 1: 1ST WAY (+10 PTS)",
            INK,
            "Study the Worked Example first. Solve a problem by hand in your open workspace using your 1st Textbook Way. Drop 1 Gold [+10] token into that problem's socket (1-10) and check off [x] +10 (1 Way).",
        ),
        (
            "STEP 2: 2ND WAY (+20 PTS)",
            TEAL_ACCENT,
            "Solve the SAME problem a 2nd independent way (the 2nd Textbook Way or hands-on block model). When both ways give the exact same answer, stack a 2nd [+10] token right on top (+20 pts DOUBLE)!",
        ),
        (
            "STEP 3: CHECK ON SC-6",
            INK,
            "Never guess! Use the section's 'Check Your Work on the SC-6 Calculator' box to verify your hand-written answer—using Two-Dot fractions ([.] n [.] d), [≠] equality tests, and [f][LINE] mode.",
        ),
        (
            "STEP 4: 100-PT TOWER!",
            "#854D0E",
            "As soon as you earn 10 tokens (100 points) on a worksheet—or in the SC-6 [f][?] Tutorial Quiz—transfer all 10 tokens into the [100] socket to build your 70 mm tall 100-Point Mastery Tower!",
        ),
    ]

    for s_idx, (stitle, shdr_col, sbody) in enumerate(step_cards):
        sx = margin + s_idx * (col_w + 2.5)
        p.rect(sx, step_y, col_w, step_h, fill=WHITE, stroke=INK, r=0.9, line_w=0.28)
        p.rect(sx, step_y, col_w, 4.4, fill=shdr_col, stroke=shdr_col, r=0.7, line_w=0.2)
        p.text(sx + 2.0, step_y + 3.1, stitle, size=1.72, bold=True, mono=True, color=WHITE, max_w=col_w - 4.0)

        # Mini graphic box inside each step card (y = 31.6 .. 44.6 mm)
        gy = step_y + 5.4
        gh = 13.0
        p.rect(sx + 2.0, gy, col_w - 4.0, gh, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.6, line_w=0.2)
        gcx = sx + col_w / 2.0

        if s_idx == 0:
            # Socket [1] with 1 Gold +10 Token
            p.rect(gcx - 15.0, gy + 7.8, 12.0, 3.6, fill="#CBD5E1", stroke=INK, r=0.4, line_w=0.22)
            p.text(gcx - 9.0, gy + 10.4, "Socket 1", size=1.45, bold=True, mono=True, color=INK, align="center")
            p.rect(gcx - 13.5, gy + 2.6, 9.0, 5.2, fill="#FDE047", stroke=INK, r=0.45, line_w=0.26)
            p.text(gcx - 9.0, gy + 6.0, "+10", size=1.95, bold=True, mono=True, color=INK, align="center")
            p.text(gcx + 8.0, gy + 5.8, "1 Block =", size=1.65, bold=True, color=SLATE, align="center")
            p.text(gcx + 8.0, gy + 9.2, "+10 PTS", size=2.1, bold=True, mono=True, color=INK, align="center")
        elif s_idx == 1:
            # Socket [1] with 2 Stacked +10 Tokens = +20 DOUBLE!
            p.rect(gcx - 15.0, gy + 9.0, 12.0, 2.8, fill="#CBD5E1", stroke=INK, r=0.4, line_w=0.22)
            p.rect(gcx - 13.5, gy + 5.2, 9.0, 3.8, fill="#FDE047", stroke=INK, r=0.35, line_w=0.24)
            p.text(gcx - 9.0, gy + 7.8, "+10", size=1.55, bold=True, mono=True, color=INK, align="center")
            p.rect(gcx - 13.5, gy + 1.4, 9.0, 3.8, fill="#86EFAC", stroke=INK, r=0.35, line_w=0.24)
            p.text(gcx - 9.0, gy + 4.0, "+10", size=1.55, bold=True, mono=True, color=INK, align="center")
            p.text(gcx + 8.0, gy + 5.6, "2 Stacked =", size=1.60, bold=True, color=TEAL_ACCENT, align="center")
            p.text(gcx + 8.0, gy + 9.0, "+20 PTS!", size=2.1, bold=True, mono=True, color=TEAL_ACCENT, align="center")
        elif s_idx == 2:
            # SC-6 2-Line LCD + Keycaps
            p.rect(sx + 3.5, gy + 1.4, col_w - 7.0, 6.0, fill="#E2E8F0", stroke=INK, r=0.4, line_w=0.22)
            p.text(sx + 5.0, gy + 3.9, "Y: 5 (Quotient)", size=1.42, bold=True, mono=True, color=SLATE)
            p.text(sx + 5.0, gy + 6.4, "X: 3 (Remainder)", size=1.42, bold=True, mono=True, color=TEAL_ACCENT)
            p.draw_keycap_sequence(["23", "ENTER", "4", "g", "÷R"], sx + 4.2, gy + 8.4, max_w=col_w - 8.4, h=3.2, gap=0.5)
        else:
            # 10-Token Mastery Tower in [100] Socket
            p.rect(gcx - 14.5, gy + 10.2, 11.0, 2.0, fill="#FDE047", stroke=INK, r=0.3, line_w=0.22)
            for t_i in range(5):
                ty_blk = gy + 8.4 - t_i * 1.6
                b_fill = "#FDE047" if t_i % 2 == 0 else "#86EFAC"
                p.rect(gcx - 13.0, ty_blk, 8.0, 1.55, fill=b_fill, stroke=INK, line_w=0.18)
            p.text(gcx + 7.5, gy + 5.6, "10 Blocks =", size=1.60, bold=True, color="#854D0E", align="center")
            p.text(gcx + 7.5, gy + 9.0, "100 PTS!", size=2.1, bold=True, mono=True, color="#854D0E", align="center")

        p.para(
            sx + 2.2,
            step_y + 20.6,
            sbody,
            max_w=col_w - 4.4,
            size=1.80,
            color=INK,
            leading=1.18,
            max_lines=9,
        )

    # 3. Middle Split: Anatomy of QUEST-01 Scoreboard (Left) & Three Flexible Paths to 100 Points (Right) (y = 70.0 .. 144.0 mm)
    mid_y = 70.0
    mid_h = 74.0
    left_w = 102.0
    right_w = uw - left_w - 2.5
    right_x = margin + left_w + 2.5

    # --- Left Panel: Scoreboard Lid Schematic + 3 Hardware Photos ---
    p.rect(margin, mid_y, left_w, mid_h, fill=WHITE, stroke=INK, r=1.0, line_w=0.3)
    p.rect(margin, mid_y, left_w, 4.6, fill=INK, stroke=INK, r=0.8, line_w=0.2)
    p.text(
        margin + 2.5,
        mid_y + 3.2,
        "HOW THE 100-POINT TOKEN SCOREBOARD WORKS",
        size=1.80,
        bold=True,
        mono=True,
        color=WHITE,
        max_w=left_w - 9.0,
    )
    p.draw_tutorial_keycap(margin + left_w - 5.5, mid_y + 0.5, w=4.0, h=3.5)

    # Top-Down Vector Diagram of 6×2 Scoreboard Lid
    lid_x = margin + 2.5
    lid_y = mid_y + 6.2
    lid_w = 60.0
    lid_h = 24.5
    p.rect(lid_x, lid_y, lid_w, lid_h, fill="#1E293B", stroke=INK, r=1.2, line_w=0.32)
    p.text(lid_x + lid_w / 2.0, lid_y + 2.9, "10-PROBLEM TOKEN SCOREBOARD (6×2 SOCKET GRID)", size=1.42, bold=True, mono=True, color="#E2E8F0", align="center")

    sock_w = 8.4
    sock_h = 8.4
    sgap_x = 1.15
    sgap_y = 1.4
    sx0 = lid_x + 2.2
    sy0 = lid_y + 4.2

    # Sample score state showing 5 problems solved in 2 Ways (+20 each = 100 pts!)
    sample_tokens = {1: 2, 2: 2, 3: 2, 5: 2, 9: 2}
    for r_i in range(2):
        for c_i in range(6):
            cell_x = sx0 + c_i * (sock_w + sgap_x)
            cell_y = sy0 + r_i * (sock_h + sgap_y)
            if c_i < 5:
                q_num = r_i * 5 + (c_i + 1)
                ntok = sample_tokens.get(q_num, 0)
                s_fill = "#DCFCE7" if ntok == 2 else "#F8FAFC"
                s_stroke = TEAL_ACCENT if ntok == 2 else BORDER
                p.rect(cell_x, cell_y, sock_w, sock_h, fill=s_fill, stroke=s_stroke, r=0.5, line_w=0.22)
                p.text(cell_x + sock_w / 2.0, cell_y + 3.2, f"#{q_num}", size=1.45, bold=True, mono=True, color=INK, align="center")
                if ntok == 2:
                    p.rect(cell_x + 1.0, cell_y + 4.1, sock_w - 2.0, 3.4, fill="#FDE047", stroke=INK, r=0.3, line_w=0.18)
                    p.text(cell_x + sock_w / 2.0, cell_y + 6.5, "+20", size=1.35, bold=True, mono=True, color=INK, align="center")
                else:
                    p.text(cell_x + sock_w / 2.0, cell_y + 6.5, "10/20", size=1.18, mono=True, color=MUTED, align="center")
            else:
                if r_i == 0:
                    # Top-right [100] Mastery Tower Socket
                    p.rect(cell_x, cell_y, sock_w, sock_h, fill="#FEF08A", stroke="#CA8A04", r=0.5, line_w=0.28)
                    p.text(cell_x + sock_w / 2.0, cell_y + 3.4, "100", size=1.65, bold=True, mono=True, color="#854D0E", align="center")
                    p.text(cell_x + sock_w / 2.0, cell_y + 6.6, "TOWER", size=1.15, bold=True, mono=True, color="#854D0E", align="center")
                else:
                    # Bottom-right (?) Tutorial Keycap Badge
                    p.draw_tutorial_keycap(cell_x, cell_y, w=sock_w, h=sock_h)

    # Callout descriptions to the right of the Lid Diagram
    call_x = lid_x + lid_w + 2.2
    call_w = left_w - lid_w - 6.8
    callouts = [
        ("Sockets #1–#10:", "Match Problems #1–#10. 1 token = +10 (1st Way); 2 stacked = +20 (2nd Way)."),
        ("Socket [100]:", "Stack 10 tokens here to build your 100-Point Mastery Tower!"),
        ("(?) Keycap Badge:", "Matches [f][C] (?) on the SC-6 to launch built-in Tutorial Quiz Mode."),
    ]
    cy_call = lid_y + 1.8
    for c_head, c_desc in callouts:
        p.text(call_x, cy_call, c_head, size=1.55, bold=True, color=TEAL_ACCENT, max_w=call_w)
        cy_call = p.para(call_x, cy_call + 2.1, c_desc, max_w=call_w, size=1.45, color=INK, leading=1.12, max_lines=3)
        cy_call += 1.0

    # Bottom half of Left Panel: 3 Hardware Photos
    photos = [
        ("quest_scoreboard_lid.png", "1. Scoreboard Grid (#1–#10, 100, ?)"),
        ("quest_scoreboard_box.png", "2. Desk Token Bank"),
        ("quest_scoreboard_parts.png", "3. 60 Universal [+10] Tokens"),
    ]
    ph_w = (left_w - 8.0) / 3.0
    ph_y = mid_y + 33.0
    for p_idx, (png_name, p_cap) in enumerate(photos):
        px = margin + 2.5 + p_idx * (ph_w + 1.5)
        p.rect(px, ph_y, ph_w, 34.5, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.7, line_w=0.2)
        p.image(ASSETS_MANUALS_DIR / png_name, px + 1.2, ph_y + 1.2, ph_w - 2.4, 28.0)
        p.text(px + ph_w / 2.0, ph_y + 32.4, p_cap, size=1.52, bold=True, color=INK, align="center", max_w=ph_w - 1.5)

    p.text(
        margin + left_w / 2.0,
        mid_y + mid_h - 2.2,
        "Solve by hand in 1 Way for +10 points, or verify with a 2nd Textbook Way for +20 Double Points!",
        size=1.55,
        bold=True,
        color=TEAL_ACCENT,
        align="center",
        max_w=left_w - 4.0,
    )

    # --- Right Panel: Three Flexible Paths to the 100-Point Daily Goal ---
    p.rect(right_x, mid_y, right_w, mid_h, fill=WHITE, stroke=INK, r=1.0, line_w=0.3)
    p.rect(right_x, mid_y, right_w, 4.6, fill=TEAL_ACCENT, stroke=TEAL_ACCENT, r=0.8, line_w=0.2)
    p.text(
        right_x + 2.5,
        mid_y + 3.2,
        "3 FLEXIBLE PATHS TO THE 100-POINT DAILY GOAL",
        size=1.80,
        bold=True,
        mono=True,
        color=WHITE,
        max_w=right_w - 5.0,
    )

    paths = [
        (
            "PATH A: DEEP MASTERY — ANY 5 PROBLEMS IN 2 WAYS = 100 PTS",
            "5 Problems × 2 Ways (+20 pts each) = 10 Tokens (100 Points)",
            "Best when a 10-problem page feels overwhelming! Pick any 5 problems (for example: Warm-Ups #1-#2, Core #3-#4, and Challenge #9), solve each using BOTH Textbook Ways, and verify on your SC-6. You do half as many problems, but understand them twice as deeply!",
            M2_BG,
            TEAL_ACCENT,
            TEAL_ACCENT,
        ),
        (
            "PATH B: FULL SHEET — ALL 10 PROBLEMS IN 1 WAY = 100 PTS",
            "10 Problems × 1 Way (+10 pts each) = 10 Tokens (100 Points)",
            "Best for building speed and accuracy across every problem type on the worksheet. Solve all 10 problems (#1-#10) using your favorite Textbook Way, drop 1 [+10] token in each socket, and check every answer on your SC-6.",
            M1_BG,
            BORDER,
            INK,
        ),
        (
            "PATH C: MIX & MATCH — ANY COMBINATION OF 10 TOKENS = 100 PTS",
            "Example: 3 Problems in 2 Ways (60 pts) + 4 Problems in 1 Way (40 pts) = 100 Points",
            "You are in control! Combine 2-Way (+20) and 1-Way (+10) solutions in any order until you collect 10 tokens to build your [100] Mastery Tower. Want a Super-Boss Challenge? Solve all 10 problems in 2 Ways for a 200-Point Double Tower!",
            "#FEFCE8",
            "#CA8A04",
            "#854D0E",
        ),
    ]
    py0 = mid_y + 6.0
    ph_box = 21.2
    pgap = 1.4
    for path_idx, (ptitle, pformula, pdesc, pbg, pstroke, ptcol) in enumerate(paths):
        py_cur = py0 + path_idx * (ph_box + pgap)
        p.rect(right_x + 2.2, py_cur, right_w - 4.4, ph_box, fill=pbg, stroke=pstroke, r=0.7, line_w=0.24)
        p.text(right_x + 3.6, py_cur + 3.1, ptitle, size=1.68, bold=True, color=ptcol, max_w=right_w - 7.2)
        p.text(right_x + 3.6, py_cur + 5.8, pformula, size=1.62, bold=True, mono=True, color=INK, max_w=right_w - 7.2)
        p.para(
            right_x + 3.6,
            py_cur + 8.5,
            pdesc,
            max_w=right_w - 7.2,
            size=1.62,
            color=SLATE,
            leading=1.14,
            max_lines=5,
        )

    # 4. Master SC-6 Calculator Work-Check Reference Table (Units 1–10) (y = 145.8 .. 232.2 mm)
    tbl_y = 145.8
    p.rect(margin, tbl_y, uw, 4.6, fill=INK, stroke=INK, r=0.7, line_w=0.2)
    p.text(
        margin + 2.4,
        tbl_y + 3.2,
        "MASTER SC-6 CALCULATOR WORK-CHECK CHEAT SHEET (UNITS 1–10: SOLVE BY HAND FIRST, THEN VERIFY!)",
        size=1.80,
        bold=True,
        mono=True,
        color=WHITE,
        max_w=uw - 4.8,
    )

    col_hdr_y = tbl_y + 4.6
    col_hdr_h = 3.8
    c1_w, c2_w, c3_w = 40.0, 42.0, 58.0
    c4_w = uw - c1_w - c2_w - c3_w
    p.rect(margin, col_hdr_y, uw, col_hdr_h, fill=SUBTLE_HDR, stroke=INK, line_w=0.22)
    p.text(margin + 1.8, col_hdr_y + 2.7, "UNIT & TOPIC", size=1.55, bold=True, mono=True, color=INK)
    p.text(margin + c1_w + 1.8, col_hdr_y + 2.7, "SOLVE BY HAND FIRST (2 WAYS)", size=1.55, bold=True, mono=True, color=INK)
    p.text(margin + c1_w + c2_w + 1.8, col_hdr_y + 2.7, "SC-6 WORK-CHECK KEYSTROKES", size=1.55, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin + c1_w + c2_w + c3_w + 1.8, col_hdr_y + 2.7, "WHAT TO VERIFY ON THE SC-6 DISPLAY", size=1.55, bold=True, mono=True, color=INK)

    unit_check_rows = [
        ("Unit 1: Whole Numbers & Factors", "Long Div / Tree vs. Array / Venn", ["23", "ENTER", "4", "g", "÷R"], "Line Y = Quotient, Line X = Remainder; [PRIME], [g][FACT], [GCF], [f][LCM], [x²], [x³]"),
        ("Unit 2: Fractions & Decimals", "LCD Strips & Reciprocals vs. Cross-Mult", [".", "2", ".", "3", "ENTER", ".", "1", ".", "4", "+"], "HP-32 Two-Dot fraction entry ([.] n [.] d & w [.] n [.] d); [g][SIMP], [FDISP], [a b/c], [f][d/c], [PV], [$]"),
        ("Unit 3: Ratios, Rates & Percents", "Tape Diagrams vs. Ratio Tables & % Prop", ["12", "ENTER", "8", "g", "a:b"], "[g][a:b] Ratio Mode (+ [10F] table), [g][REP], [%] part of whole, [g][%CHG], [f][▸cm]/[g][▸in]"),
        ("Unit 4: Algebraic Expressions", "Area Model / Like Terms vs. GCF Factor", ["4", "ENTER", "5", "×", "7", "+"], "Evaluate at x = 5 in both original & simplified forms and press [≠] (flashes NO when equal!)"),
        ("Unit 5: Area & Elapsed Time", "Cut-and-Slide Grid vs. Polygon Formulas", ["12", "ENTER", "8", "f", "RECT"], "[f][RECT] area/perim, [g][TRI] ½bh, [Σ+]/[f][Σx] composite sum, [CLK] + [f][▸HR]/[g][▸HMS]"),
        ("Unit 6: Integers & Coord Plane", "Number Line Jumps vs. Absolute Value |x|", ["f", "LINE", "18", "+/-", "5", "+/-", "f", ">"], "[f][LINE] Number Line jumps, [+/-] sign, [g][|x|] distance, [f][>]/[g][<] (flashes YES/NO!)"),
        ("Unit 7: Equations & Inequalities", "Balance Scale vs. Inverse Operations", ["41", "ENTER", "4", "ENTER", "9", "×", "5", "+", "≠"], "Equality test [≠] flashes NO when Left = Right (balanced!); [f][≥] & [g][≤] flash YES/NO"),
        ("Unit 8: 3D Surface Area & Volume", "Unfolded 2D Net vs. Prism/Cone Formulas", ["12", "ENTER", "8", "ENTER", "5", "f", "PRISM"], "[f][PRISM] 3D volume, [g][CLΣ]+[Σ+]+[f][Σx] 2D net surface area, [f][CIRC], [g][HYP], [g][CONE]"),
        ("Unit 9: Statistics & Distributions", "Fair-Share Leveling / Peel vs. IQR & MAD", ["g", "CLΣ", "18", "Σ+", "24", "Σ+", "g", "x̄"], "Enter list with [Σ+] (or [FRQ]): check [g][x̄], [f][MED], [g][MODE], [RNG], [f][1Q], [g][3Q], [IQR], [g][MAD]"),
        ("Unit 10: Signed Ops & Probability", "Zero-Pair Chips & Trees vs. Sign Rules", ["f", "LINE", "10", "ENTER", "4", "+/-", "-"], "[f][LINE] signed hops, [+/-], [≠] 2-step equation check, [DICE]/[f][1..x], [x!], [f][nCr], [g][nPr]"),
    ]
    r_y0 = col_hdr_y + col_hdr_h
    r_h = 7.75
    for u_idx, (u_name, u_hand, u_keys, u_verify) in enumerate(unit_check_rows):
        ry = r_y0 + u_idx * r_h
        r_bg = WHITE if u_idx % 2 == 0 else SUBTLE_HDR
        p.rect(margin, ry, uw, r_h, fill=r_bg, stroke=LIGHT_BORDER, line_w=0.18)
        p.line(margin + c1_w, ry, margin + c1_w, ry + r_h, color=LIGHT_BORDER, width=0.18)
        p.line(margin + c1_w + c2_w, ry, margin + c1_w + c2_w, ry + r_h, color=LIGHT_BORDER, width=0.18)
        p.line(margin + c1_w + c2_w + c3_w, ry, margin + c1_w + c2_w + c3_w, ry + r_h, color=LIGHT_BORDER, width=0.18)

        p.text(margin + 1.6, ry + 4.8, u_name, size=1.58, bold=True, color=INK, max_w=c1_w - 3.0)
        p.text(margin + c1_w + 1.6, ry + 4.8, u_hand, size=1.52, color=SLATE, max_w=c2_w - 3.0)
        p.draw_keycap_sequence(u_keys, margin + c1_w + c2_w + 1.6, ry + 2.35, max_w=c3_w - 3.0, h=3.0, gap=0.45)
        p.para(
            margin + c1_w + c2_w + c3_w + 1.6,
            ry + 3.0,
            u_verify,
            max_w=c4_w - 3.0,
            size=1.48,
            color=INK,
            leading=1.12,
            max_lines=2,
        )

    # 5. Bottom Tracker: 45-Section 100-Point Mastery Tower Log (y = 233.5 .. 268.5 mm, height = 35.0 mm)
    bot_y = 233.5
    bot_h = 35.0
    p.rect(margin, bot_y, uw, bot_h, fill=WHITE, stroke=INK, r=0.9, line_w=0.28)
    p.rect(margin, bot_y, uw, 4.5, fill=SUBTLE_HDR, stroke=INK, r=0.7, line_w=0.22)
    p.text(
        margin + 2.4,
        bot_y + 3.1,
        "45-SECTION 100-POINT MASTERY TOWER LOG (CHECK OFF EACH SECTION AS YOU EARN 100 POINTS ON PRACTICE A & B!)",
        size=1.74,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=uw - 10.0,
    )
    p.draw_tutorial_keycap(margin + uw - 5.5, bot_y + 0.45, w=4.0, h=3.5)

    # 2 Columns × 5 Rows of Units inside the bottom log
    u_col_w = (uw - 6.0) / 2.0
    u_row_h = 5.6
    for idx, ch in enumerate(chapters):
        uc = idx // 5
        ur = idx % 5
        ux = margin + 2.2 + uc * (u_col_w + 1.6)
        uy = bot_y + 5.8 + ur * u_row_h
        p.rect(ux, uy, u_col_w, u_row_h - 0.5, fill=SUBTLE_HDR if ur % 2 == 0 else WHITE, stroke=LIGHT_BORDER, r=0.4, line_w=0.16)
        p.text(ux + 1.4, uy + 3.4, f"Unit {ch['num']}:", size=1.58, bold=True, color=INK)
        sec_checks = "   ".join(f"[ ] {s['sec_num']}" for s in ch["sections"])
        p.text(ux + 16.5, uy + 3.4, sec_checks, size=1.58, bold=True, mono=True, color=TEAL_ACCENT, max_w=u_col_w - 18.0)

    p.text(
        margin,
        p.h - 5.2,
        "StackCalc SC-6 Textbook Supplement  •  1-Page Token Scoring & SC-6 Work-Check Guide",
        size=1.88,
        mono=True,
        color=MUTED,
        max_w=uw - 28.0,
    )
    p.text(margin + uw, p.h - 5.2, page_label, size=1.88, bold=True, mono=True, color=INK, align="right")


def generate_token_scoring_guide_pdf(chapters: List[Dict[str, Any]], output_path: Path) -> None:
    """Generates the standalone 1-page printable Token Scoring & SC-6 Work-Check Guide PDF."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_path), pagesize=letter)
    c.setTitle("StackCalc SC-6 1-Page Token Scoring & Work-Check Guide")
    c.setAuthor("StackCalc Learning Lab")
    p = CanvasPage(c, letter)
    draw_token_scoring_guide_page(p, chapters, page_label="1-Page Reference Guide")
    c.showPage()
    c.save()
    print(f"[OK] Built 1-Page Token Scoring Guide: {output_path} ({output_path.stat().st_size / 1024:.1f} KB, 1 page)")


def draw_unit_story_page(p: CanvasPage, ch: Dict[str, Any], page_num: int, total_pages: int) -> None:
    """Renders a 1-page Unit Introduction & Story Opener before each Unit (zero metadata banners, no section paragraphs here)."""
    margin = 11.0
    uw = p.w - 2 * margin
    ch_num = ch["num"]
    story = UNIT_STORIES[ch_num]

    # 1. Clean Top Header (y = 9.0 .. 24.8 mm)
    p.text(
        margin,
        12.2,
        f"UNIT {ch_num} INTRODUCTION  •  {ch['big_ideas_book'].upper()}",
        size=2.0,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=122.0,
    )
    clean_tools = clean_manipulative_label(ch["kit_summary"])
    p.rect(margin + uw - 70.0, 9.0, 70.0, 4.6, fill=SUBTLE_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(
        margin + uw - 35.0,
        12.1,
        f"MODELS: {clean_tools.upper()}",
        size=1.68,
        bold=True,
        mono=True,
        color=INK,
        align="center",
        max_w=67.0,
    )

    p.text(
        margin,
        18.2,
        f"Unit {ch_num}: {ch['title']} — {story['story_title']}",
        size=3.75,
        bold=True,
        color=INK,
        max_w=uw,
    )
    p.text(
        margin,
        23.2,
        ch["subtitle"],
        size=1.92,
        bold=True,
        color=SLATE,
        max_w=uw,
    )
    p.line(margin, 24.8, margin + uw, 24.8, color=INK, width=0.45)

    # 2. Multi-Paragraph Unit Story (y = 26.2 .. 124.0 mm, no metadata title bar)
    box_y = 26.2
    box_h = 97.8
    p.rect(margin, box_y, uw, box_h, fill=WHITE, stroke=LIGHT_BORDER, r=1.0, line_w=0.25)

    essay_w = uw - 62.0
    cur_ey = box_y + 4.5
    for p_idx, para_txt in enumerate(story["paragraphs"]):
        cur_ey = p.para(
            margin + 3.4,
            cur_ey,
            para_txt,
            max_w=essay_w,
            size=2.42,
            bold=(p_idx == 2),
            color=INK if p_idx < 2 else TEAL_ACCENT,
            leading=1.23,
            max_lines=8,
        )
        cur_ey += 2.2

    rc_x = margin + essay_w + 5.2
    rc_w = uw - essay_w - 7.4
    p.rect(rc_x, box_y + 3.6, rc_w, box_h - 10.6, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.8, line_w=0.22)
    p.image(ASSETS_MANUALS_DIR / ch["hero_png"], rc_x + 1.8, box_y + 5.2, rc_w - 3.6, box_h - 13.8)

    # Bottom ribbon inside story box: Companion Book Story & Hands-On Models
    p.rect(margin + 2.0, box_y + box_h - 5.8, uw - 4.0, 4.8, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.6, line_w=0.18)
    p.text(
        margin + 3.6,
        box_y + box_h - 2.5,
        f"Companion Story in From Blocks to the Stack (SC-6 Elementary Guide)  •  Hands-On Models: {clean_tools}",
        size=1.55,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=uw - 7.2,
    )

    # 3. Unit Lesson & SC-6 Work-Check Directory (y = 126.5 .. 268.2 mm)
    hdr_y = 126.5
    p.rect(margin, hdr_y, uw, 5.0, fill=INK, stroke=INK, r=0.7, line_w=0.2)
    p.text(
        margin + 2.6,
        hdr_y + 3.4,
        f"UNIT {ch_num} LESSONS — LEARN TWO TEXTBOOK WAYS FIRST, THEN CHECK YOUR WORK ON THE SC-6 CALCULATOR",
        size=1.84,
        bold=True,
        mono=True,
        color=WHITE,
        max_w=uw - 10.0,
    )
    p.draw_tutorial_keycap(margin + uw - 5.6, hdr_y + 0.65, w=4.2, h=3.6)

    secs = ch["sections"]
    n_secs = len(secs)
    cards_y0 = 132.8
    avail_h = 268.2 - cards_y0
    c_gap = 1.8
    card_h = (avail_h - (n_secs - 1) * c_gap) / n_secs

    for idx, sec in enumerate(secs):
        snum = sec["sec_num"]
        stitle = clean_section_title(snum, sec["title"])
        ped = SECTION_PEDAGOGY[snum]
        check_info = SC6_SECTION_CHECK_GUIDE[snum]
        ex1_keys = sec["examples"][0]["keys"]
        pg_a = 3 + ch_num + (sec["day_num"] - 1) * 2
        pg_b = pg_a + 1
        cy = cards_y0 + idx * (card_h + c_gap)

        p.rect(margin, cy, uw, card_h, fill=WHITE, stroke=SLATE, r=0.9, line_w=0.26)
        p.rect(margin, cy, uw, 4.8, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.7, line_w=0.2)
        p.rect(margin + 1.8, cy + 0.65, 25.0, 3.5, fill=TEAL_ACCENT, stroke=TEAL_ACCENT, r=0.5, line_w=0.15)
        p.text(
            margin + 14.3,
            cy + 3.0,
            f"SEC {snum} (pp.{pg_a}-{pg_b})",
            size=1.62,
            bold=True,
            mono=True,
            color=WHITE,
            align="center",
            max_w=24.0,
        )
        p.text(
            margin + 28.6,
            cy + 3.3,
            stitle,
            size=1.95,
            bold=True,
            color=INK,
            max_w=96.0,
        )
        p.text(
            margin + uw - 2.4,
            cy + 3.3,
            f"Textbook Ways: {ped['big_ideas_method']}",
            size=1.62,
            bold=True,
            color=TEAL_ACCENT,
            align="right",
            max_w=uw - 127.0,
        )

        # Left column: What You Will Learn (Paper-and-Pencil + Block Concept)
        left_col_w = 104.0
        intro_sent = sec["concept"]
        p.para(
            margin + 2.8,
            cy + 7.6,
            f"Learn by Hand: {intro_sent}",
            max_w=left_col_w,
            size=1.78,
            color=INK,
            leading=1.16,
            max_lines=4,
        )

        # Right column: How to Check Your Work on SC-6
        rx = margin + left_col_w + 5.5
        rw = uw - left_col_w - 7.5
        p.line(rx - 2.2, cy + 5.6, rx - 2.2, cy + card_h - 1.2, color=LIGHT_BORDER, width=0.22)
        p.text(
            rx,
            cy + 7.4,
            "Check Your Work on the SC-6 Calculator:",
            size=1.68,
            bold=True,
            color=TEAL_ACCENT,
            max_w=rw,
        )
        after_keys_y = p.draw_keycap_sequence(ex1_keys, rx, cy + 8.3, max_w=rw, h=2.6, gap=0.42)
        check_short = check_info["check_a"].split(":", 1)[-1].strip()
        if check_short:
            check_short = check_short[0].upper() + check_short[1:]
        p.para(
            rx,
            after_keys_y + 2.3,
            check_short,
            max_w=rw,
            size=1.62,
            color=SLATE,
            leading=1.13,
            max_lines=3,
        )

    p.text(
        margin,
        p.h - 5.2,
        f"StackCalc SC-6 Textbook Supplement  •  Unit {ch_num}: {ch['title']}",
        size=1.88,
        mono=True,
        color=MUTED,
        max_w=uw - 28.0,
    )
    p.text(margin + uw, p.h - 5.2, f"Page {page_num} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")


def draw_sc6_check_box(
    p: CanvasPage,
    sec_num: str,
    keys: List[str],
    check_text: str,
    x: float,
    y: float,
    w: float,
    h: float,
    sheet_label: str,
) -> None:
    """Renders a dedicated, separate SC-6 Calculator Work-Check section with hardware keycaps and step-by-step instructions."""
    p.rect(x, y, w, h, fill="#F0F9FF", stroke=TEAL_ACCENT, r=0.85, line_w=0.28)
    p.rect(x, y, w, 3.7, fill=TEAL_ACCENT, stroke=TEAL_ACCENT, r=0.65, line_w=0.2)
    p.text(
        x + 2.5,
        y + 2.65,
        f"CHECK YOUR WORK ON THE SC-6 CALCULATOR — {sheet_label} (SOLVE BY HAND FIRST, THEN VERIFY!)",
        size=1.74,
        bold=True,
        mono=True,
        color=WHITE,
        max_w=w - 10.0,
    )
    p.draw_tutorial_keycap(x + w - 5.2, y + 0.25, w=3.8, h=3.2)

    # Left Keycap Tray (w = 81.2 mm)
    tray_x = x + 1.8
    tray_w = 81.2
    p.rect(tray_x, y + 4.2, tray_w, h - 4.8, fill=WHITE, stroke=LIGHT_BORDER, r=0.6, line_w=0.2)
    if len(keys) > 10:
        p.text(
            tray_x + 1.6,
            y + 5.7,
            "Worked Example SC-6 Check Keystrokes:",
            size=1.38,
            bold=True,
            mono=True,
            color=SLATE,
            max_w=tray_w - 3.2,
        )
        p.draw_keycap_sequence(keys, tray_x + 1.6, y + 6.3, max_w=tray_w - 3.2, h=2.55, gap=0.42)
    else:
        p.text(
            tray_x + 1.8,
            y + 6.4,
            "Worked Example SC-6 Check Keystrokes:",
            size=1.52,
            bold=True,
            mono=True,
            color=SLATE,
            max_w=tray_w - 3.6,
        )
        p.draw_keycap_sequence(keys, tray_x + 1.8, y + 7.4, max_w=tray_w - 3.6, h=3.25, gap=0.58)

    # Right Step-by-Step Verification Instructions
    rx = x + tray_w + 4.8
    rw = w - tray_w - 6.8
    if ":" in check_text:
        lead_lbl, rest_txt = check_text.split(":", 1)
        rest_clean = rest_txt.strip()
        if rest_clean:
            rest_clean = rest_clean[0].upper() + rest_clean[1:]
        p.text(
            rx,
            y + 5.9,
            lead_lbl.strip() + ":",
            size=1.72,
            bold=True,
            color=TEAL_ACCENT,
            max_w=rw,
        )
        p.para(
            rx,
            y + 8.1,
            rest_clean,
            max_w=rw,
            size=1.72,
            color=INK,
            leading=1.15,
            max_lines=3,
        )
    else:
        p.para(
            rx,
            y + 6.2,
            check_text,
            max_w=rw,
            size=1.72,
            color=INK,
            leading=1.15,
            max_lines=4,
        )


def draw_student_section_page_a(p: CanvasPage, ch: Dict[str, Any], sec: Dict[str, Any], page_num: int, total_pages: int) -> None:
    """Renders Worksheet A for a section: Key Ideas, Textbook Concept & Visual/Block Model, 2-or-3-Way Worked Example, Separate SC-6 Work-Check Part, and 10 Clean Problems."""
    margin = 11.0
    uw = p.w - 2 * margin
    sec_num = sec["sec_num"]
    stitle = clean_section_title(sec_num, sec["title"])
    ped = SECTION_PEDAGOGY[sec_num]
    uses_blocks = ped.get("uses_blocks", True)
    check_info = SC6_SECTION_CHECK_GUIDE[sec_num]

    # 1. Clean Textbook Header (y = 9.0 .. 24.5 mm)
    p.text(
        margin,
        12.2,
        f"{ped['unit_name'].upper()}  •  {sec['big_ideas_ref'].upper()} ({sec['ccss']})",
        size=2.0,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=122.0,
    )
    kit_name_clean = clean_manipulative_label(sec["kit_name"])
    kit_badge = f"HANDS-ON MODEL: {kit_name_clean.upper()}" if uses_blocks else "TEXTBOOK MODEL: PAPER / GRAPH / FORMULA"
    p.rect(margin + uw - 70.0, 9.0, 70.0, 4.6, fill=SUBTLE_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(margin + uw - 35.0, 12.1, kit_badge, size=1.82, bold=True, mono=True, color=INK, align="center", max_w=67.0)

    p.text(margin, 18.0, f"Section {sec_num} — Practice A: {stitle}", size=3.95, bold=True, color=INK, max_w=uw)

    p.text(
        margin,
        22.9,
        f"Key Vocabulary: {ped['key_vocab']}",
        size=1.90,
        bold=True,
        color=SLATE,
        max_w=115.0,
    )
    p.text(
        margin + uw,
        22.9,
        "Name: ____________________   Date: ________   Score: ____ / 100",
        size=1.90,
        bold=True,
        color=INK,
        align="right",
    )
    p.line(margin, 24.4, margin + uw, 24.4, color=INK, width=0.45)

    # 2. Top Instruction & Worked Example Band (y = 25.4 .. 78.4 mm, height = 53.0 mm)
    left_w = 90.0
    right_w = uw - left_w - 2.5
    right_x = margin + left_w + 2.5
    band_y = 25.4
    band_h = 53.0

    # --- LEFT PANEL: Textbook Concept, Custom Section Visual/Block Diagram & Reinforcement ---
    bm = MULTI_METHOD_BLOCK_NOTES[sec_num]
    p.rect(margin, band_y, left_w, band_h, fill=WHITE, stroke=INK, r=1.0, line_w=0.3)
    p.rect(margin, band_y, left_w, 4.5, fill=INK, stroke=INK, r=0.8, line_w=0.2)
    left_hdr_title = (
        f"TEXTBOOK CONCEPT & HANDS-ON MODEL ({kit_name_clean.upper()})"
        if uses_blocks
        else "TEXTBOOK CONCEPT & VISUAL DIAGRAM"
    )
    p.text(
        margin + 2.4,
        band_y + 3.2,
        left_hdr_title,
        size=1.78,
        bold=True,
        mono=True,
        color=WHITE,
        max_w=left_w - 4.8,
    )

    # Full-width section-specific concept & block diagram (86.0 mm × 24.2 mm)
    draw_section_concept_diagram(p, sec_num, sec, ped, margin + 2.0, band_y + 5.0, left_w - 4.0, 24.2)

    steps_box_y = band_y + 29.8
    steps_box_h = band_h - 30.8
    p.rect(margin + 2.0, steps_box_y, left_w - 4.0, steps_box_h, fill=SUBTLE_HDR, stroke=BORDER, r=0.8, line_w=0.22)
    p.text(
        margin + 3.5,
        steps_box_y + 2.9,
        "HOW THE TEXTBOOK & VISUAL MODEL WORK TOGETHER:",
        size=1.72,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=left_w - 7.0,
    )
    sy_cur = steps_box_y + 5.4
    trap_txt = COMMON_TRAPS.get(sec_num, bm["block_compare"])
    block_demo_lines = [
        (bm["block_m1"], True, INK),
        (bm["block_m2"], True, TEAL_ACCENT),
        (trap_txt, True, "#B91C1C"),
    ]
    for btext, bbold, bcol in block_demo_lines:
        sy_cur = p.para(
            margin + 3.5,
            sy_cur,
            btext,
            max_w=left_w - 7.0,
            size=1.74,
            bold=bbold,
            color=bcol,
            leading=1.12,
            max_lines=2,
        )
        sy_cur += 0.3

    # --- RIGHT PANEL: Worked Example (2 or 3 Authentic Textbook Ways) ---
    ex1 = sec["examples"][0]
    ex1_prob_txt = clean_ex1_problem(sec_num, ex1["problem"])
    ex1_ans_txt = clean_ex1_ans(sec_num, ex1["ans"])
    has_m3 = bool(ped.get("ex1_m3_title"))

    p.rect(right_x, band_y, right_w, band_h, fill=WHITE, stroke=INK, r=1.0, line_w=0.3)
    p.rect(right_x, band_y, right_w, 4.5, fill=SUBTLE_HDR, stroke=INK, r=0.8, line_w=0.25)
    we_hdr = (
        "WORKED EXAMPLE — 3 TEXTBOOK WAYS (ANY 2 WAYS = +20 PTS)"
        if has_m3
        else "WORKED EXAMPLE — 2 TEXTBOOK WAYS FOR DOUBLE POINTS (+20)"
    )
    p.text(
        right_x + 2.5,
        band_y + 3.2,
        we_hdr,
        size=1.80,
        bold=True,
        mono=True,
        color=INK,
        max_w=right_w - 10.0,
    )
    p.draw_tutorial_keycap(right_x + right_w - 5.6, band_y + 0.45, w=4.2, h=3.5)

    # Problem Statement
    p.para(
        right_x + 2.6,
        band_y + 7.1,
        f"Problem: {ex1_prob_txt}",
        max_w=right_w - 5.2,
        size=2.02,
        bold=True,
        color=INK,
        leading=1.14,
        max_lines=2,
    )

    if has_m3:
        # Render 3 Authentic Textbook Ways stacked cleanly
        way_boxes = [
            (ped["ex1_m1_title"], ped["ex1_m1_steps"], M1_BG, BORDER, INK, SLATE),
            (ped["ex1_m2_title"], ped["ex1_m2_steps"], M2_BG, TEAL_ACCENT, TEAL_ACCENT, INK),
            (ped["ex1_m3_title"], ped["ex1_m3_steps"], "#FEFCE8", "#CA8A04", "#854D0E", INK),
        ]
        wy0 = band_y + 12.1
        wh = 10.9
        wgap = 0.70
        for w_idx, (w_title, w_steps, w_bg, w_stroke, w_tcol, w_scol) in enumerate(way_boxes):
            wy = wy0 + w_idx * (wh + wgap)
            p.rect(right_x + 2.2, wy, right_w - 4.4, wh, fill=w_bg, stroke=w_stroke, r=0.65, line_w=0.22)
            p.text(
                right_x + 3.6,
                wy + 2.7,
                w_title,
                size=1.70,
                bold=True,
                color=w_tcol,
                max_w=right_w - 7.2,
            )
            p.para(
                right_x + 3.6,
                wy + 5.0,
                w_steps,
                max_w=right_w - 7.2,
                size=1.66,
                color=w_scol,
                leading=1.11,
                max_lines=2,
            )
    else:
        # Render 2 Authentic Textbook Ways
        m1_y = band_y + 12.3
        m1_h = 16.2
        p.rect(right_x + 2.2, m1_y, right_w - 4.4, m1_h, fill=M1_BG, stroke=BORDER, r=0.7, line_w=0.22)
        p.text(
            right_x + 3.8,
            m1_y + 3.1,
            ped["ex1_m1_title"],
            size=1.80,
            bold=True,
            color=INK,
            max_w=right_w - 7.6,
        )
        p.para(
            right_x + 3.8,
            m1_y + 6.0,
            ped["ex1_m1_steps"],
            max_w=right_w - 7.6,
            size=1.78,
            color=SLATE,
            leading=1.14,
            max_lines=3,
        )

        m2_y = band_y + 29.6
        m2_h = 16.2
        p.rect(right_x + 2.2, m2_y, right_w - 4.4, m2_h, fill=M2_BG, stroke=TEAL_ACCENT, r=0.7, line_w=0.24)
        p.text(
            right_x + 3.8,
            m2_y + 3.1,
            ped["ex1_m2_title"],
            size=1.80,
            bold=True,
            color=TEAL_ACCENT,
            max_w=right_w - 7.6,
        )
        p.para(
            right_x + 3.8,
            m2_y + 6.0,
            ped["ex1_m2_steps"],
            max_w=right_w - 7.6,
            size=1.78,
            color=INK,
            leading=1.14,
            max_lines=3,
        )

    # Final Answer Bar
    bar_y = band_y + band_h - 6.0
    p.line(right_x + 2.2, bar_y, right_x + right_w - 2.2, bar_y, color=INK, width=0.25)
    if len(ex1_ans_txt) > 30:
        ans_sz = 1.66 if len(ex1_ans_txt) > 48 else 1.78
        p.text(
            right_x + 2.6,
            bar_y + 3.9,
            f"Answer: {ex1_ans_txt}",
            size=ans_sz,
            bold=True,
            mono=True,
            color=TEAL_ACCENT,
            max_w=right_w - 5.2,
        )
    else:
        p.text(
            right_x + 2.6,
            bar_y + 3.9,
            f"Answer: {ex1_ans_txt}",
            size=2.0,
            bold=True,
            mono=True,
            color=TEAL_ACCENT,
            max_w=right_w * 0.62,
        )
        p.text(
            right_x + right_w - 2.6,
            bar_y + 3.9,
            "1 Way = +10  |  2 Ways = +20!",
            size=1.68,
            bold=True,
            color=SLATE,
            align="right",
            max_w=right_w * 0.36,
        )

    # 3. Separate Part: How to Use the SC-6 Calculator to Check Your Work (y = 79.2 .. 92.8 mm, height = 13.6 mm)
    draw_sc6_check_box(
        p,
        sec_num,
        ex1["keys"],
        check_info["check_a"],
        margin,
        79.2,
        uw,
        13.6,
        f"SECTION {sec_num} PRACTICE A",
    )

    # 4. Practice A Grid (y = 93.8 .. 268.5 mm, 10 Clean Textbook Problems in 5 Rows × 2 Columns)
    hdr_y = 93.8
    p.rect(margin, hdr_y, uw, 4.4, fill=INK, stroke=INK, r=0.7, line_w=0.2)
    p.text(
        margin + 2.5,
        hdr_y + 3.1,
        f"SECTION {sec_num} PRACTICE A — KEY IDEAS & MULTI-METHOD PRACTICE",
        size=1.84,
        bold=True,
        mono=True,
        color=WHITE,
        max_w=105.0,
    )
    p.text(
        margin + uw - 2.5,
        hdr_y + 3.1,
        "100-PT GOAL: Any 5 in 2 Ways (+20) OR All 10 in 1 Way (+10)!",
        size=1.70,
        bold=True,
        mono=True,
        color="#E2E8F0",
        align="right",
        max_w=86.0,
    )

    grid_y0 = 99.1
    col_w = (uw - 3.0) / 2.0
    row_h = 33.0
    row_gap = 1.1

    probs = sec["problems"]
    for idx, prob in enumerate(probs[:10]):
        r = idx // 2
        c = idx % 2
        px = margin + c * (col_w + 3.0)
        py = grid_y0 + r * (row_h + row_gap)

        p.rect(px, py, col_w, row_h, fill=WHITE, stroke=SLATE, r=0.9, line_w=0.28)

        p_num = prob["num"]
        part = prob.get("part", "A")
        badge_fill = INK if part != "C" else TEAL_ACCENT
        p.rect(px + 2.0, py + 1.8, 5.0, 4.4, fill=badge_fill, stroke=badge_fill, r=0.65, line_w=0.2)
        p.text(px + 4.5, py + 4.8, str(p_num), size=2.15, bold=True, mono=True, color=WHITE, align="center")

        # Clean textbook prompt directly at top of card
        cleaned_prompt = clean_sheet_a_prompt(sec_num, p_num, prob["prompt"])
        after_prompt = p.para(
            px + 8.2,
            py + 4.4,
            cleaned_prompt,
            max_w=col_w - 10.2,
            size=2.08,
            bold=True,
            color=INK,
            leading=1.15,
            max_lines=3,
        )

        # Warm-Up Starter Step 1 scaffold on Problems #1 and #2
        starter_txt = get_starter_scaffold(sec_num, "A", p_num)
        if starter_txt:
            p.para(
                px + 8.2,
                after_prompt + 0.35,
                starter_txt,
                max_w=col_w - 10.2,
                size=1.70,
                italic=True,
                color=TEAL_ACCENT,
                leading=1.12,
                max_lines=1,
            )

        # Light ready-to-use graphic organizer in lower-right workspace where applicable
        draw_problem_workspace_organizer(p, sec_num, "A", p_num, px, py, col_w, row_h, cleaned_prompt)

        # Bottom-left tier & token checkoffs + Bottom-right Ans line (leaves middle workspace 100% open!)
        tier_lbl = "WARM-UP" if p_num <= 2 else ("CORE" if p_num <= 8 else "CHALLENGE")
        p.text(
            px + 2.4,
            py + row_h - 1.8,
            f"{tier_lbl} • [ ] +10 (1 Way)  [ ] +20 (2 Ways)",
            size=1.55,
            mono=True,
            color=MUTED,
            max_w=col_w - 43.0,
        )
        p.text(
            px + col_w - 2.4,
            py + row_h - 1.8,
            "Ans: ________________________",
            size=1.92,
            bold=True,
            mono=True,
            color=INK,
            align="right",
        )

    p.text(
        margin,
        p.h - 5.2,
        f"StackCalc SC-6 Textbook Supplement  •  {ped['unit_name']} — Section {sec_num} Practice A ({sec['big_ideas_ref']})",
        size=1.88,
        mono=True,
        color=MUTED,
        max_w=uw - 28.0,
    )
    p.text(margin + uw, p.h - 5.2, f"Page {page_num} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")


def draw_student_section_page_b(p: CanvasPage, ch: Dict[str, Any], sec: Dict[str, Any], page_num: int, total_pages: int) -> None:
    """Renders Worksheet B for a section: Modeling Real Life 2-or-3-Way Worked Example + Separate SC-6 Check Box + Section Story Paragraph right before the 10 Word Problems."""
    margin = 11.0
    uw = p.w - 2 * margin
    sec_num = sec["sec_num"]
    stitle = clean_section_title(sec_num, sec["title"])
    ped = SECTION_PEDAGOGY[sec_num]
    uses_blocks = ped.get("uses_blocks", True)
    bm = MULTI_METHOD_BLOCK_NOTES[sec_num]
    ex2 = ped["ex2"]
    b_probs = SHEET_B_PROBLEMS[sec_num]
    check_info = SC6_SECTION_CHECK_GUIDE[sec_num]

    # 1. Clean Textbook Header (y = 9.0 .. 24.4 mm)
    p.text(
        margin,
        12.2,
        f"{ped['unit_name'].upper()}  •  {sec['big_ideas_ref'].upper()} — MODELING REAL LIFE & APPLICATIONS",
        size=2.0,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=122.0,
    )
    kit_name_clean = clean_manipulative_label(sec["kit_name"])
    kit_badge = f"HANDS-ON MODEL: {kit_name_clean.upper()}" if uses_blocks else "TEXTBOOK MODEL: PAPER / GRAPH / FORMULA"
    p.rect(margin + uw - 70.0, 9.0, 70.0, 4.6, fill=SUBTLE_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(margin + uw - 35.0, 12.1, kit_badge, size=1.82, bold=True, mono=True, color=INK, align="center", max_w=67.0)

    p.text(margin, 18.0, f"Section {sec_num} — Practice B: Modeling Real Life ({stitle})", size=3.85, bold=True, color=INK, max_w=uw)

    compact_methods = (
        ped["big_ideas_method"]
        .replace("Way 1: ", "")
        .replace("Way 2: ", "")
        .replace("Way 3: ", "")
        .replace("Method 1: ", "")
        .replace("Method 2: ", "")
    )
    p.text(
        margin,
        22.9,
        f"Textbook Ways: {compact_methods}",
        size=1.90,
        bold=True,
        color=SLATE,
        max_w=112.0,
    )
    p.text(
        margin + uw,
        22.9,
        "Name: ____________________   Date: ________   Score: ____ / 100",
        size=1.90,
        bold=True,
        color=INK,
        align="right",
    )
    p.line(margin, 24.4, margin + uw, 24.4, color=INK, width=0.45)

    # 2. Top Modeling Real Life Worked Example (y = 25.4 .. 62.2 mm, height = 36.8 mm)
    band_y = 25.4
    band_h = 36.8
    has_m3 = bool(ex2.get("m3_title"))

    p.rect(margin, band_y, uw, band_h, fill=WHITE, stroke=INK, r=1.0, line_w=0.3)
    p.rect(margin, band_y, uw, 4.4, fill=SUBTLE_HDR, stroke=INK, r=0.8, line_w=0.25)
    ex2_clean_title = ex2["title"].replace("Modeling Real Life: ", "").upper()
    b_hdr = (
        f"WORKED EXAMPLE — {ex2_clean_title} (3 TEXTBOOK WAYS • ANY 2 = +20 PTS)"
        if has_m3
        else f"WORKED EXAMPLE — {ex2_clean_title} (2 TEXTBOOK WAYS = +20 PTS DOUBLE)"
    )
    p.text(
        margin + 2.5,
        band_y + 3.1,
        b_hdr,
        size=1.82,
        bold=True,
        mono=True,
        color=INK,
        max_w=uw - 10.0,
    )
    p.draw_tutorial_keycap(margin + uw - 5.6, band_y + 0.45, w=4.2, h=3.5)

    # Real-Life Problem Statement
    p.para(
        margin + 2.6,
        band_y + 7.1,
        f"Problem: {ex2['problem']}",
        max_w=uw - 5.2,
        size=2.02,
        bold=True,
        color=INK,
        leading=1.14,
        max_lines=2,
    )

    m_box_y = band_y + 12.1
    m_box_h = 18.8

    if has_m3:
        # 3 Side-by-Side Textbook Ways
        col3_w = (uw - 7.6) / 3.0
        way3_cols = [
            (ex2["m1_title"], ex2["m1_steps"], M1_BG, BORDER, INK, SLATE),
            (ex2["m2_title"], ex2["m2_steps"], M2_BG, TEAL_ACCENT, TEAL_ACCENT, INK),
            (ex2["m3_title"], ex2["m3_steps"], "#FEFCE8", "#CA8A04", "#854D0E", INK),
        ]
        for c_idx, (w_title, w_steps, w_bg, w_stroke, w_tcol, w_scol) in enumerate(way3_cols):
            cx = margin + 2.2 + c_idx * (col3_w + 1.6)
            p.rect(cx, m_box_y, col3_w, m_box_h, fill=w_bg, stroke=w_stroke, r=0.7, line_w=0.22)
            p.text(
                cx + 1.5,
                m_box_y + 2.9,
                w_title,
                size=1.68,
                bold=True,
                color=w_tcol,
                max_w=col3_w - 3.0,
            )
            p.para(
                cx + 1.5,
                m_box_y + 5.4,
                w_steps,
                max_w=col3_w - 3.0,
                size=1.64,
                color=w_scol,
                leading=1.12,
                max_lines=5,
            )
    else:
        # 2 Side-by-Side Textbook Ways
        half_w = (uw - 6.8) / 2.0
        p.rect(margin + 2.2, m_box_y, half_w, m_box_h, fill=M1_BG, stroke=BORDER, r=0.7, line_w=0.22)
        p.text(
            margin + 3.8,
            m_box_y + 2.9,
            ex2["m1_title"],
            size=1.78,
            bold=True,
            color=INK,
            max_w=half_w - 3.2,
        )
        after_m1 = p.para(
            margin + 3.8,
            m_box_y + 5.5,
            ex2["m1_steps"],
            max_w=half_w - 3.2,
            size=1.74,
            color=SLATE,
            leading=1.13,
            max_lines=3,
        )
        p.para(
            margin + 3.8,
            max(after_m1 + 0.35, m_box_y + 12.1),
            bm["ex2_block_m1"],
            max_w=half_w - 3.2,
            size=1.66,
            italic=True,
            color=TEAL_ACCENT,
            leading=1.11,
            max_lines=2,
        )

        m2_x = margin + 4.6 + half_w
        p.rect(m2_x, m_box_y, half_w, m_box_h, fill=M2_BG, stroke=TEAL_ACCENT, r=0.7, line_w=0.24)
        p.text(
            m2_x + 1.6,
            m_box_y + 2.9,
            ex2["m2_title"],
            size=1.78,
            bold=True,
            color=TEAL_ACCENT,
            max_w=half_w - 3.2,
        )
        after_m2 = p.para(
            m2_x + 1.6,
            m_box_y + 5.5,
            ex2["m2_steps"],
            max_w=half_w - 3.2,
            size=1.74,
            color=INK,
            leading=1.13,
            max_lines=3,
        )
        p.para(
            m2_x + 1.6,
            max(after_m2 + 0.35, m_box_y + 12.1),
            bm["ex2_block_m2"],
            max_w=half_w - 3.2,
            size=1.66,
            italic=True,
            color=TEAL_ACCENT,
            leading=1.11,
            max_lines=2,
        )

    # Bottom Bar: Common Trap Alert (left) + Final Answer (right)
    ky = band_y + 31.3
    ex2_ans_txt = ex2["ans"]
    ans_b_w = min(82.0, max(44.0, (len(ex2_ans_txt) + 8) * 1.18))
    ans_b_sz = 1.72 if len(ex2_ans_txt) > 44 else 1.88
    trap_b_txt = COMMON_TRAPS.get(sec_num, bm["ex2_block_m1"])
    p.para(
        margin + 2.6,
        ky + 1.9,
        trap_b_txt,
        max_w=uw - ans_b_w - 6.0,
        size=1.50,
        bold=True,
        color="#B91C1C",
        leading=1.08,
        max_lines=2,
    )
    p.text(
        margin + uw - 2.6,
        ky + 3.2,
        f"Answer: {ex2_ans_txt}",
        size=ans_b_sz,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        align="right",
        max_w=ans_b_w,
    )

    # 3. Separate Part: How to Use the SC-6 Calculator to Check Your Work (y = 63.0 .. 76.6 mm, height = 13.6 mm)
    draw_sc6_check_box(
        p,
        sec_num,
        ex2["keys"],
        check_info["check_b"],
        margin,
        63.0,
        uw,
        13.6,
        f"SECTION {sec_num} PRACTICE B",
    )

    # 4. Section Story Paragraph right before the Word Problems (y = 77.4 .. 93.0 mm, height = 15.6 mm, zero metadata banners)
    story_para = SECTION_STORY_PARAGRAPHS[sec_num]
    p.rect(margin, 77.4, uw, 15.6, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.8, line_w=0.22)
    p.para(
        margin + 2.6,
        80.2,
        story_para,
        max_w=uw - 5.2,
        size=1.82,
        color=INK,
        leading=1.16,
        max_lines=5,
    )

    # 5. Practice B Application Grid (y = 93.8 .. 268.5 mm, 10 Engaging Applications in 5 Rows × 2 Columns, matching Practice A!)
    hdr_y = 93.8
    p.rect(margin, hdr_y, uw, 4.4, fill=INK, stroke=INK, r=0.7, line_w=0.2)
    p.text(
        margin + 2.5,
        hdr_y + 3.1,
        f"SECTION {sec_num} PRACTICE B — MODELING REAL LIFE & APPLICATIONS",
        size=1.84,
        bold=True,
        mono=True,
        color=WHITE,
        max_w=105.0,
    )
    p.text(
        margin + uw - 2.5,
        hdr_y + 3.1,
        "100-PT GOAL: Any 5 in 2 Ways (+20) OR All 10 in 1 Way (+10)!",
        size=1.70,
        bold=True,
        mono=True,
        color="#E2E8F0",
        align="right",
        max_w=86.0,
    )

    grid_y0 = 99.1
    col_w = (uw - 3.0) / 2.0
    row_h = 33.0
    row_gap = 1.1

    for idx, prob in enumerate(b_probs[:10]):
        r = idx // 2
        c = idx % 2
        px = margin + c * (col_w + 3.0)
        py = grid_y0 + r * (row_h + row_gap)

        p.rect(px, py, col_w, row_h, fill=WHITE, stroke=SLATE, r=0.9, line_w=0.28)

        p_num = prob["num"]
        p.rect(px + 2.0, py + 1.8, 5.0, 4.4, fill=TEAL_ACCENT, stroke=TEAL_ACCENT, r=0.65, line_w=0.2)
        p.text(px + 4.5, py + 4.8, str(p_num), size=2.15, bold=True, mono=True, color=WHITE, align="center")

        after_prompt = p.para(
            px + 8.2,
            py + 4.4,
            prob["prompt"],
            max_w=col_w - 10.2,
            size=2.06,
            bold=True,
            color=INK,
            leading=1.16,
            max_lines=3,
        )

        # Warm-Up Starter Step 1 scaffold on Problems #1 and #2
        starter_txt = get_starter_scaffold(sec_num, "B", p_num)
        if starter_txt:
            p.para(
                px + 8.2,
                after_prompt + 0.35,
                starter_txt,
                max_w=col_w - 10.2,
                size=1.72,
                italic=True,
                color=TEAL_ACCENT,
                leading=1.12,
                max_lines=1,
            )

        # Light ready-to-use graphic organizer in lower-right workspace where applicable
        draw_problem_workspace_organizer(p, sec_num, "B", p_num, px, py, col_w, row_h, prob["prompt"])

        tier_lbl = "WARM-UP" if p_num <= 2 else ("CORE" if p_num <= 8 else "CHALLENGE")
        p.text(
            px + 2.4,
            py + row_h - 1.8,
            f"{tier_lbl} • [ ] +10 (1 Way)  [ ] +20 (2 Ways)",
            size=1.55,
            mono=True,
            color=MUTED,
            max_w=col_w - 43.0,
        )
        p.text(
            px + col_w - 2.4,
            py + row_h - 1.8,
            "Ans: ________________________",
            size=1.92,
            bold=True,
            mono=True,
            color=INK,
            align="right",
        )

    p.text(
        margin,
        p.h - 5.2,
        f"StackCalc SC-6 Textbook Supplement  •  {ped['unit_name']} — Section {sec_num} Practice B ({sec['big_ideas_ref']})",
        size=1.88,
        mono=True,
        color=MUTED,
        max_w=uw - 28.0,
    )
    p.text(margin + uw, p.h - 5.2, f"Page {page_num} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")


def draw_workbook_front_matter(c: canvas.Canvas, chapters: List[Dict[str, Any]], is_coach: bool = False) -> None:
    """Renders Pages i and ii (Title Page + How to Use This Workbook / Pacing Guide) for the Spiral Edition."""
    margin = 13.0
    uw = (letter[0] / mm) - 2 * margin

    # ---------------------------------------------------------
    # PAGE i: Half-Title & Full Title Page
    # ---------------------------------------------------------
    p = CanvasPage(c, letter)
    p.rect(margin, 10.0, uw, p.h - 20.0, fill=SUBTLE_HDR, stroke=INK, r=1.5, line_w=0.35)
    p.rect(margin, 10.0, uw, 11.5, fill=INK, stroke=INK, r=1.2, line_w=0.2)
    kicker = (
        "STACKCALC LEARNING LAB  •  MIDDLE SCHOOL TEACHER & PARENT COACH EDITION"
        if is_coach
        else "STACKCALC LEARNING LAB  •  MIDDLE SCHOOL TWO-METHOD STUDENT WORKBOOK"
    )
    p.text(margin + 4.0, 17.2, kicker, size=2.3, bold=True, mono=True, color=WHITE, max_w=uw - 12.0)
    p.draw_tutorial_keycap(margin + uw - 8.0, 12.2, w=5.2, h=4.4)

    title_1 = "MIDDLE SCHOOL MATH LAB:"
    title_2 = (
        "10-UNIT TEACHER & PARENT COACH GUIDE"
        if is_coach
        else "BIG IDEAS TWO-METHOD STUDENT WORKBOOK"
    )
    subtitle = (
        "Compact 1-Page Per Unit Solution Keys (Practice A & B #1–#10), Target Misconceptions, Hands-On Block Remediations & Classroom Pacing"
        if is_coach
        else "Grade 6 Complete + Grade 7 Bridge • 10 Unit Stories • 45 Textbook Sections • 90 Two-Method Worksheets (Practice A & B) • 900 Problems"
    )
    p.text(margin + 5.0, 31.0, title_1, size=5.8, bold=True, color=INK, max_w=uw - 10.0)
    p.text(margin + 5.0, 39.5, title_2, size=5.8, bold=True, color=TEAL_ACCENT, max_w=uw - 10.0)
    p.para(margin + 5.0, 46.5, subtitle, max_w=uw - 10.0, size=2.45, bold=True, color=SLATE, leading=1.25)
    p.line(margin + 5.0, 56.0, margin + uw - 5.0, 56.0, color=TEAL_ACCENT, width=0.5)

    # Companion Book & Manipulative Studio Alignment Box
    p.rect(margin + 5.0, 59.5, uw - 10.0, 32.0, fill=M2_BG, stroke=TEAL_ACCENT, r=1.2, line_w=0.28)
    p.text(
        margin + 8.0,
        65.0,
        "COMPANION TO FROM BLOCKS TO THE STACK & HANDS-ON CLASSROOM MANIPULATIVES",
        size=2.35,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
    )
    p.text(
        margin + 8.0,
        71.0,
        "• Illustrated Companion Book: From Blocks to the Stack: Hands-On Math & the SC-6 Stack Calculator",
        size=2.1,
        bold=True,
        color=INK,
        max_w=uw - 16.0,
    )
    p.text(
        margin + 8.0,
        76.2,
        "• Double-Points Mastery Scoring: Earn +10 points for your 1st Textbook Way and +20 points for verifying with a 2nd Way.",
        size=2.05,
        color=INK,
        max_w=uw - 16.0,
    )
    p.text(
        margin + 8.0,
        81.4,
        "• Hands-On Models: Array Tiles, Prime Factor Towers, Fraction Strips, Place Value Blocks, Two-Tone Counters, Algebra Tiles & Geared Clock.",
        size=2.05,
        color=INK,
        max_w=uw - 16.0,
    )
    p.text(
        margin + 8.0,
        86.6,
        "• Solve by Hand First, Then Check on SC-6: Every section includes a dedicated SC-6 Calculator Work-Check box with hardware keycaps.",
        size=2.05,
        bold=True,
        color=TEAL_ACCENT,
        max_w=uw - 16.0,
    )

    # 5 Manipulative Photos Showcase Strip
    p.rect(margin + 5.0, 95.0, uw - 10.0, 34.0, fill=WHITE, stroke=LIGHT_BORDER, r=1.0, line_w=0.22)
    showcase = [
        ("counting_tiles_array_3x8.png", "Counting & Array Tiles"),
        ("prime_lcm_gcd_venn.png", "Prime Factor Towers"),
        ("fraction_studio_common_denominator.png", "Fraction Strips"),
        ("algebra_factoring_area.png", "Algebra & Area Tiles"),
        ("planetary_geared_clock_330.png", "Geared Base-60 Clock"),
    ]
    sw_w = (uw - 18.0) / 5.0
    for idx, (png_name, cap) in enumerate(showcase):
        sx = margin + 7.0 + idx * (sw_w + 1.0)
        p.rect(sx, 97.5, sw_w, 23.0, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.7, line_w=0.18)
        p.image(ASSETS_MANUALS_DIR / png_name, sx + 1.2, 98.5, sw_w - 2.4, 20.8)
        p.text(sx + sw_w / 2.0, 125.0, cap, size=1.8, bold=True, color=INK, align="center", max_w=sw_w - 1.0)

    # What Is Inside This Spiral Edition
    p.rect(margin + 5.0, 132.5, uw - 10.0, 118.0, fill=WHITE, stroke=INK, r=1.2, line_w=0.28)
    p.rect(margin + 5.0, 132.5, uw - 10.0, 6.0, fill=INK, stroke=INK, r=0.9, line_w=0.2)
    p.text(
        margin + 8.0,
        136.6,
        "WHAT IS INSIDE THIS EDITION (FRONT MATTER, CORE UNITS & BACK MATTER APPENDICES)",
        size=2.05,
        bold=True,
        mono=True,
        color=WHITE,
    )
    edition_items = (
        [
            ("Front Matter (pp. i–ii)", "Title Page, Classroom Reproduction License, Pacing Guide & Companion Book Directory."),
            ("Core Unit Keys 1–5 (pp. 1–5)", "1-Page Coach & Answer Keys for Units 1–5 (Whole Numbers, Fractions/Decimals, Ratios/Percents, Expressions, Area/Time)."),
            ("Core Unit Keys 6–10 (pp. 6–10)", "1-Page Coach & Answer Keys for Units 6–10 (Integers/Coord Plane, Equations/Inequalities, 3D Solids, Statistics, Grade 7 Bridge)."),
            ("Appendix A (p. 11)", "Master Diagnostic Misconception Matrix, Hands-On Block Remediations & 45-Day / 9-Week Pacing Schedule."),
            ("Appendix B (p. 12)", "Photocopiable Classroom & Homeschool Student Progress Roster & 100-Point Mastery Tower Log."),
        ]
        if is_coach
        else [
            ("Front Matter & Index (pp. i–ii, 1–2)", "Title Page, Pacing Guide, 10-Unit Scope & Sequence, and 1-Page Double-Points Scoring & SC-6 Guide."),
            ("Units 1–10 (pp. 3–102)", "10 Real-World Unit Story Openers + 90 Two-Method Worksheets (45 Practice A: Key Ideas + 45 Practice B: Modeling Real Life)."),
            ("Appendix A (p. 103)", "Middle School Math Formula Reference, Fraction-Decimal-Percent Benchmarks & Unit Conversions (Units 1–10)."),
            ("Appendix B (p. 104)", "SC-6 Elementary Calculator Keycap Directory, 4-Register Stack Elevator (T, Z, Y, X) & Two-Dot Fraction Reference."),
            ("Appendix C (p. 105)", "Hands-On Manipulative Models & Visual Tools Guide across all 10 Middle School Units."),
            ("Appendix D (p. 106)", "Official 100-Point Mastery Certificate of Achievement & Dot-Grid Mathematical Scratchpad."),
            ("Appendix E (pp. 107–111)", "Compact Student Self-Check Answer Key for all 900 Problems (Units 1–10, Practice A & B #1–#10)."),
        ]
    )
    ey = 141.0
    step_ey = 15.2 if not is_coach else 18.0
    box_ey_h = 13.8 if not is_coach else 16.0
    for e_head, e_desc in edition_items:
        p.rect(margin + 8.0, ey, uw - 16.0, box_ey_h, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.7, line_w=0.18)
        p.text(margin + 10.5, ey + 4.6, e_head, size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
        p.text(margin + 10.5, ey + 9.6, e_desc, size=1.84, color=INK, max_w=uw - 21.0)
        ey += step_ey

    p.text(
        margin + 5.0,
        259.5,
        "STACKCALC LEARNING LAB  •  OPEN-HARDWARE K–12 MATHEMATICS  •  STACKCALC.IO",
        size=2.1,
        bold=True,
        mono=True,
        color=INK,
    )
    p.text(margin + uw - 5.0, 259.5, "Front Matter • Page i", size=2.1, bold=True, mono=True, color=TEAL_ACCENT, align="right")
    c.showPage()

    # ---------------------------------------------------------
    # PAGE ii: How to Study with Two Methods, Pacing Guide & Reproduction License
    # ---------------------------------------------------------
    p = CanvasPage(c, letter)
    p.text(
        margin,
        12.2,
        "FRONT MATTER  •  HOW TO USE THIS WORKBOOK, PACING GUIDE & CLASSROOM REPRODUCTION LICENSE",
        size=2.0,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
    )
    p.text(
        margin,
        18.2,
        "Why Two Textbook Methods + Hands-On Models + RPN Verification Work",
        size=3.9,
        bold=True,
        color=INK,
        max_w=uw,
    )
    p.line(margin, 21.5, margin + uw, 21.5, color=INK, width=0.45)

    # Box 1: Pedagogical Philosophy
    p.rect(margin, 24.5, uw, 52.0, fill=WHITE, stroke=INK, r=1.0, line_w=0.28)
    p.rect(margin, 24.5, uw, 5.2, fill=INK, stroke=INK, r=0.8, line_w=0.2)
    p.text(margin + 3.0, 28.2, "1. THE THREE-PART MASTERY LOOP: SOLVE BY HAND IN TWO WAYS, MODEL, THEN VERIFY", size=1.95, bold=True, mono=True, color=WHITE)
    colophon_lines = [
        "• Step 1 — Solve by Hand in Your 1st Textbook Way (+10 Points): Study the section's Worked Example and solve the problem using your primary textbook method.",
        "• Step 2 — Verify with a 2nd Independent Textbook Way (+20 Points Double): Solve the same problem using a second textbook pathway or hands-on block model.",
        "• Step 3 — Check Your Work on the SC-6 Stack Calculator: Enter the postfix verification sequence shown in the section's SC-6 Check Box to confirm your result.",
        "• Step 4 — Self-Check & Diagnose: Compare your final answer against Appendix E (pp. 107–111) or consult the Unified Teacher's Guide for full setups.",
        "• Mathematical Verification: All 90 worked examples and 900 practice problem solutions are verified against the StackCalc RPNCore engine.",
        "• Copyright © 2026 StackCalc Learning Systems. Big Ideas Math® is a trademark of Larson Texts, Inc., which does not sponsor or endorse this supplement.",
    ]
    cy = 34.0
    for c_line in colophon_lines:
        p.text(margin + 3.5, cy, c_line, size=1.84, color=INK, max_w=uw - 7.0)
        cy += 6.6

    # Box 2: Perpetual Classroom & Homeschool Reproduction License
    p.rect(margin, 80.0, uw, 38.0, fill=M2_BG, stroke=TEAL_ACCENT, r=1.0, line_w=0.28)
    p.rect(margin, 80.0, uw, 5.2, fill=TEAL_ACCENT, stroke=TEAL_ACCENT, r=0.8, line_w=0.2)
    p.text(margin + 3.0, 83.7, "2. CLASSROOM & HOMESCHOOL REPRODUCTION PERMISSION", size=1.95, bold=True, mono=True, color=WHITE)
    p.para(
        margin + 3.5,
        89.5,
        "Teachers, parents, tutors, homeschool families, and school mathematics departments are granted a perpetual, royalty-free license to photocopy or print unlimited copies of all 90 Practice A & Practice B worksheets, the 1-Page Token Scoring Guide, and the 10 standalone Chapter Packet PDFs for their own students. Commercial resale or redistribution to third parties is prohibited.",
        max_w=uw - 7.0,
        size=1.95,
        color=INK,
        leading=1.22,
    )
    p.text(
        margin + 3.5,
        114.0,
        "Print Individual Chapters (Units 1–10 Separate PDFs): https://stackcalc.io/curriculum/big-ideas-middle-school-sc6-workbook/",
        size=1.9,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=uw - 7.0,
    )

    # Box 3: Companion Curriculum Lineup (The 4 Books)
    p.rect(margin, 121.5, uw, 80.0, fill=WHITE, stroke=INK, r=1.0, line_w=0.28)
    p.rect(margin, 121.5, uw, 5.2, fill=INK, stroke=INK, r=0.8, line_w=0.2)
    p.text(margin + 3.0, 125.2, "3. THE COMPLETE STACKCALC CURRICULUM LINEUP & COMPANION RESOURCES", size=1.95, bold=True, mono=True, color=WHITE)

    channels = [
        (
            "BOOK 1 — TEACHING WITH THE STACK: UNIFIED K–12 MASTER TEACHER'S GUIDE (BY CONCEPT)",
            "Organizes all K–12 concept domains and all 10 Middle School Big Ideas units into a single concept-by-concept teaching reference with target misconceptions, hands-on block remediations, and complete worked setups & RPN keys.",
            TEAL_ACCENT,
        ),
        (
            "BOOK 2 & BOOK 3 — HANDS-ON MATH LAB (K–12) & MIDDLE SCHOOL MATH LAB (BIG IDEAS SUPPLEMENT)",
            "Dedicated lay-flat student workbooks pairing concrete manipulative models, story openers from From Blocks to the Stack and Thinking in the Stack, guided keycap walkthroughs, and compact self-check answer keys.",
            INK,
        ),
        (
            "BOOK 4 — STACK SPEED & FLUENCY: STUDENT SPEED & PROFICIENCY TRIALS WORKBOOK",
            "15 progressive 10-minute timed RPN fluency sprints (Aligned to UIL Calculator Applications & Number Sense), inside-out postfix speed tactics, personal progress graphing, and complete self-check answer keys.",
            TEAL_ACCENT,
        ),
        (
            "COMPANION TRADE BOOKS & HANDS-ON MANIPULATIVE BLOCK SETS",
            "Read the illustrated stories in From Blocks to the Stack (SC-6 Elementary) and Thinking in the Stack (SC-32 Scientific) on Amazon, and explore physical manipulative kits and free print files at stackcalc.io.",
            INK,
        ),
    ]
    chy = 129.0
    for ch_head, ch_body, ch_col in channels:
        p.rect(margin + 3.0, chy, uw - 6.0, 16.8, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.7, line_w=0.18)
        p.text(margin + 5.0, chy + 4.2, ch_head, size=1.88, bold=True, mono=True, color=ch_col, max_w=uw - 10.0)
        p.para(margin + 5.0, chy + 8.2, ch_body, max_w=uw - 10.0, size=1.78, color=INK, leading=1.16, max_lines=3)
        chy += 18.0

    # Box 4: Pacing & Book Alignment Summary
    p.rect(margin, 205.0, uw, 54.0, fill=SUBTLE_HDR, stroke=BORDER, r=1.0, line_w=0.25)
    p.text(margin + 3.5, 210.5, "4. FLEXIBLE 45-DAY / FULL-YEAR PACING & ALIGNMENT WITH FROM BLOCKS TO THE STACK", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    pacing_notes = [
        "• Daily Classroom Supplement (90 Days): Assign Practice A (Key Ideas) on Day 1 of a textbook section and Practice B (Modeling Real Life) on Day 2.",
        "• 45-Day Catch-Up / Summer Bridge (9 Weeks): Complete 1 Section per day (5 problems in 2 Ways = 100 Points on Practice A, plus 2 Real-Life problems on Practice B).",
        "• Story-First Hook: Begin each of the 10 Units by reading the 1-page Unit Story Opener together and exploring the matching chapter in From Blocks to the Stack.",
        "• Self-Checking Without Guessing: Students write their paper-and-pencil steps first, verify on the SC-6 calculator, and check final answers in Appendix E.",
    ]
    py_n = 216.5
    for p_line in pacing_notes:
        p.text(margin + 3.5, py_n, p_line, size=1.85, color=INK, max_w=uw - 7.0)
        py_n += 6.2

    p.text(margin, p.h - 5.2, "StackCalc SC-6 Textbook Supplement  •  Middle School Math Lab Workbook", size=1.88, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 5.2, "Front Matter • Page ii", size=1.88, bold=True, mono=True, color=INK, align="right")
    c.showPage()


def draw_student_workbook_back_matter(c: canvas.Canvas, chapters: List[Dict[str, Any]], start_page: int, total_pages: int) -> None:
    """Renders 9 Back Matter Appendix Pages (Appendices A–D + 5-Page Compact Student Self-Check Answer Key in Appendix E)."""
    margin = 13.0
    uw = (letter[0] / mm) - 2 * margin

    # ---------------------------------------------------------
    # APPENDIX A (Page 103): Middle School Math Formulas, Benchmarks & Conversions
    # ---------------------------------------------------------
    p = CanvasPage(c, letter)
    p.text(margin, 12.0, "BACK MATTER  •  APPENDIX A: MIDDLE SCHOOL FORMULAS, BENCHMARKS & CONVERSIONS", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin, 18.0, "Appendix A: Middle School Math Formulas & Reference Sheet (Units 1–10)", size=3.9, bold=True, color=INK, max_w=uw)
    p.line(margin, 21.2, margin + uw, 21.2, color=INK, width=0.45)

    formula_sections = [
        (
            "UNITS 1–2: FACTORS, FRACTIONS & DECIMALS",
            [
                "• Division Check Identity: Dividend = (Divisor × Quotient) + Remainder, with 0 <= Remainder < Divisor. Verify on SC-6: [n] [ENTER] [d] [g][÷R].",
                "• GCF & LCM Product Law: For any two positive integers a and b, GCF(a, b) × LCM(a, b) = a × b. Verify on SC-6: [a] [ENTER] [b] [GCF] and [f][LCM].",
                "• Fraction Multiplication & Division: (a/b) × (c/d) = (a·c)/(b·d);  (a/b) ÷ (c/d) = (a/b) × (d/c) (Multiply by the Reciprocal!).",
            ],
        ),
        (
            "UNIT 3: RATIOS, RATES, PERCENTS & MEASUREMENT CONVERSIONS",
            [
                "• Percent Proportion & Equation: Part / Whole = Percent / 100  <=>  Part = (Percent / 100) × Whole. Percent Change = (|New - Old| / Old) × 100%.",
                "• Key Fraction-Decimal-Percent Benchmarks: 1/8 = 0.125 = 12.5% | 1/5 = 0.20 = 20% | 1/4 = 0.25 = 25% | 1/3 = 0.3-rep = 33.3% | 3/8 = 0.375 = 37.5% | 1/2 = 0.5 = 50% | 3/4 = 0.75 = 75%.",
                "• Customary & Metric Conversions: 1 ft = 12 in | 1 yd = 3 ft | 1 mi = 5,280 ft | 1 in = 2.54 cm | 1 m = 100 cm = 1,000 mm | 1 km = 1,000 m | 1 lb = 16 oz | 1 kg ~= 2.205 lb | 1 gal = 4 qt = 8 pt = 16 c.",
            ],
        ),
        (
            "UNITS 4, 6 & 7: ALGEBRAIC EXPRESSIONS, INTEGERS, EQUATIONS & INEQUALITIES",
            [
                "• Distributive, Commutative & Associative Properties: a(b + c) = ab + ac;  a + b = b + a;  ab = ba;  (a + b) + c = a + (b + c).",
                "• Signed Integer Rules: Adding an opposite gives zero: a + (-a) = 0 (1 Zero-Pair). Subtracting a number is adding its opposite: a - b = a + (-b). Product/quotient of same signs is (+); opposite signs is (-).",
                "• Coordinate Plane Distance: Horizontal distance = |x2 - x1|; Vertical distance = |y2 - y1|; Reflection across x-axis: (x, y) -> (x, -y); across y-axis: (x, y) -> (-x, y).",
            ],
        ),
        (
            "UNITS 5 & 8: 2D POLYGON AREA, ELAPSED TIME & 3D SURFACE AREA / VOLUME",
            [
                "• 2D Polygon Areas: Rectangle A = l·w, P = 2(l+w) | Parallelogram A = b·h | Triangle A = (1/2)·b·h | Trapezoid A = (1/2)·(b1 + b2)·h | Circle C = 2·π·r = π·d, A = π·r².",
                "• 3D Solid Volumes & Nets: Rectangular Prism V = l·w·h = B·h, SA = 2(lw + lh + wh) | Triangular Prism V = B·h | Pyramid SA = B + Sum(Lateral Triangle Areas) | Cylinder V = π·r²·h | Cone V = (1/3)·π·r²·h.",
                "• Modulo-60 Time (Geared Clock): 1 hr = 60 min = 3,600 sec. Convert H.MMSS to decimal hours on SC-6 with [f][▸HR], and back with [g][▸HMS].",
            ],
        ),
        (
            "UNITS 9 & 10: STATISTICAL MEASURES (MEAN, MEDIAN, IQR, MAD) & PROBABILITY",
            [
                "• Center & Spread: Mean (x-bar) = (Sum of values) / n | Median = middle value of ordered list | Range = Max - Min | IQR = Q3 - Q1 | Mean Absolute Deviation (MAD) = (Sum |xi - x-bar|) / n.",
                "• Theoretical & Compound Probability: P(Event) = (Favorable Outcomes) / (Total Possible Outcomes), 0 <= P(E) <= 1; P(not E) = 1 - P(E); Independent events: P(A and B) = P(A) × P(B).",
            ],
        ),
    ]
    fy = 24.5
    for f_title, f_lines in formula_sections:
        box_h = 44.5 if len(f_lines) == 3 else 34.0
        p.rect(margin, fy, uw, box_h, fill=WHITE, stroke=INK, r=0.9, line_w=0.25)
        p.rect(margin, fy, uw, 4.8, fill=INK, stroke=INK, r=0.7, line_w=0.2)
        p.text(margin + 2.8, fy + 3.3, f_title, size=1.85, bold=True, mono=True, color=WHITE)
        ly = fy + 8.5
        for fl in f_lines:
            ly = p.para(margin + 3.0, ly, fl, max_w=uw - 6.0, size=1.80, color=INK, leading=1.18, max_lines=3)
            ly += 1.4
        fy += box_h + 3.2

    p.text(margin, p.h - 5.2, "StackCalc SC-6 Textbook Supplement  •  Appendix A: Middle School Math Formulas & Conversions", size=1.88, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 5.2, f"Page {start_page} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")
    c.showPage()

    # ---------------------------------------------------------
    # APPENDIX B (Page 104): SC-6 Elementary Keycap Directory & 4-Stack Reference
    # ---------------------------------------------------------
    p = CanvasPage(c, letter)
    p.text(margin, 12.0, "BACK MATTER  •  APPENDIX B: SC-6 ELEMENTARY CALCULATOR & 4-STACK DIRECTORY", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin, 18.0, "Appendix B: SC-6 Keycap Directory & 4-Register Stack Guide", size=3.9, bold=True, color=INK, max_w=uw)
    p.line(margin, 21.2, margin + uw, 21.2, color=INK, width=0.45)

    p.rect(margin, 24.0, uw, 28.0, fill=M2_BG, stroke=TEAL_ACCENT, r=1.0, line_w=0.28)
    p.text(margin + 3.0, 29.0, "THE 4-FLOOR NUMBER ELEVATOR (REGISTERS T, Z, Y, X) — ZERO PARENTHESES NEEDED", size=2.1, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin + 3.0, 34.5, "• Floor 1 (Register X — Bottom Line): Shows the number you are typing right now, or the answer to the operation you just pressed.", size=1.88, color=INK, max_w=uw - 6.0)
    p.text(margin + 3.0, 39.8, "• Floor 2 (Register Y — Upper Line): Holds your first number after you press [ENTER]. Pressing [+], [-], [×], or [÷] combines Y with X.", size=1.88, color=INK, max_w=uw - 6.0)
    p.text(margin + 3.0, 45.1, "• Floors 3 & 4 (Registers Z & T): Hold extra numbers during multi-step problems. Press [4-LV] to view all 4 floors at once!", size=1.88, bold=True, color=INK, max_w=uw - 6.0)

    p.rect(margin, 55.0, uw, 5.0, fill=INK, stroke=INK, r=0.7, line_w=0.2)
    p.text(margin + 2.5, 58.4, "KEYCAP / SHIFT", size=1.75, bold=True, mono=True, color=WHITE)
    p.text(margin + 36.0, 58.4, "FUNCTION NAME", size=1.75, bold=True, mono=True, color=WHITE)
    p.text(margin + 82.0, 58.4, "EXAMPLE KEYSTROKES", size=1.75, bold=True, mono=True, color=WHITE)
    p.text(margin + 136.0, 58.4, "WHAT IT DOES ON THE SC-6", size=1.75, bold=True, mono=True, color=WHITE)

    sc6_keys_dir = [
        ("[ENTER]", "Stack Lift / Push", ["14", "ENTER", "6", "+"], "Pushes X up to Y so you can type the 2nd number; [ENTER][+] doubles X."),
        ("[g] [÷R]", "Quotient & Remainder", ["23", "ENTER", "4", "g", "÷R"], "Divides Y by X, placing whole Quotient in Y (5) and Remainder in X (3)."),
        ("[g] [FACT]", "Prime Factorization", ["24", "g", "FACT"], "Decomposes whole number into prime powers (2³ × 3¹); [PRIME] tests primality."),
        ("[GCF] / [f][LCM]", "GCF & LCM", ["24", "ENTER", "36", "GCF"], "Computes Greatest Common Factor (12); press [f][LCM] for Least Common Multiple (72)."),
        ("[.] n [.] d", "Two-Dot Fraction", [".", "2", ".", "3", "ENTER", ".", "1", ".", "4", "+"], "Enters proper fraction 2/3 or mixed number w[.]n[.]d; [g][SIMP] simplifies step-by-step."),
        ("[FDISP]", "Fraction / Dec / %", ["FDISP"], "Cycles exact fraction (3/4) <-> decimal (0.75) <-> percent (75%) on the LCD."),
        ("[g] [a:b]", "Ratio Simplifier", ["12", "ENTER", "8", "g", "a:b"], "Simplifies ratio Y:X to lowest terms (3:2); press [10F] to step through ratio table."),
        ("[≠] / [f][>]", "Equality & Compare", ["41", "ENTER", "4", "ENTER", "9", "×", "5", "+", "≠"], "Tests Y ≠ X (flashes NO when both sides are equal!). [f][>], [g][<], [f][≥], [g][≤]."),
        ("[f] [LINE]", "Number Line Mode", ["f", "LINE", "4", "+/-", "7", "+"], "Animates signed hops right (+) and left (-) along a visual number line on screen."),
        ("[f][RECT] / [g][TRI]", "2D Polygon Area", ["12", "ENTER", "8", "f", "RECT"], "Computes rectangle area (96) & perimeter (40) or triangle area (1/2)·b·h."),
        ("[f][PRISM] / [g][CONE]", "3D Solid Volume", ["12", "ENTER", "8", "ENTER", "5", "f", "PRISM"], "Computes 3D rectangular prism volume l·w·h (480) or cone volume (1/3)·B·h."),
        ("[Σ+] / [g][x̄] / [IQR]", "Statistics Suite", ["g", "CLΣ", "18", "Σ+", "24", "Σ+", "g", "x̄"], "Accumulates data list; computes Mean [g][x̄], Median [f][MED], [IQR], and [g][MAD]."),
        ("[DICE] / [f][nCr]", "Probability & Combos", ["6", "ENTER", "2", "f", "nCr"], "Simulates fair dice/coin trials [DICE] and computes combinations nCr (15) & nPr."),
        ("[f] [?] (Tutorial)", "Built-In Math Quiz", ["f", "C"], "Launches interactive step-by-step Tutorial & Quiz Mode for 100-Point Mastery!"),
    ]
    ky = 60.0
    kh = 14.2
    for idx, (k_lbl, k_name, k_seq, k_desc) in enumerate(sc6_keys_dir):
        p.rect(margin, ky, uw, kh, fill=WHITE if idx % 2 == 0 else SUBTLE_HDR, stroke=LIGHT_BORDER, line_w=0.18)
        p.text(margin + 2.0, ky + 8.2, k_lbl, size=1.82, bold=True, mono=True, color=TEAL_ACCENT, max_w=32.0)
        p.text(margin + 36.0, ky + 8.2, k_name, size=1.80, bold=True, color=INK, max_w=44.0)
        p.draw_keycap_sequence(k_seq, margin + 82.0, ky + 4.2, max_w=51.0, h=2.85, gap=0.4)
        p.para(margin + 136.0, ky + 4.4, k_desc, max_w=uw - 138.0, size=1.65, color=INK, leading=1.15, max_lines=3)
        ky += kh

    p.text(margin, p.h - 5.2, "StackCalc SC-6 Textbook Supplement  •  Appendix B: SC-6 Keycap & 4-Stack Reference", size=1.88, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 5.2, f"Page {start_page + 1} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")
    c.showPage()

    # ---------------------------------------------------------
    # APPENDIX C (Page 105): Hands-On Manipulative Models & Visual Tools Guide
    # ---------------------------------------------------------
    p = CanvasPage(c, letter)
    p.text(margin, 12.0, "BACK MATTER  •  APPENDIX C: HANDS-ON MANIPULATIVE MODELS & VISUAL TOOLS GUIDE", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin, 18.0, "Appendix C: Hands-On Classroom Manipulatives & Visual Modeling Guide", size=3.9, bold=True, color=INK, max_w=uw)
    p.line(margin, 21.2, margin + uw, 21.2, color=INK, width=0.45)

    p.rect(margin, 24.0, uw, 5.2, fill=INK, stroke=INK, r=0.7, line_w=0.2)
    p.text(margin + 2.5, 27.6, "MANIPULATIVE MODEL", size=1.75, bold=True, mono=True, color=WHITE)
    p.text(margin + 56.0, 27.6, "UNITS", size=1.75, bold=True, mono=True, color=WHITE)
    p.text(margin + 78.0, 27.6, "HOW TO MODEL TEXTBOOK CONCEPTS WITH THE BLOCKS", size=1.75, bold=True, mono=True, color=WHITE)

    kit_guide_rows = [
        ("Counting & Array Tiles", "Units 1, 4, 5, 9", "Build m×n rectangular tile arrays for factor pairs, area/perimeter, Distributive Property a(b+c), and fair-share mean leveling towers."),
        ("Prime Factor Towers & Venn Tray", "Unit 1", "Stack proportional prime factor blocks (2, 3, 5, 7) and place shared prime blocks in the intersection of the Prime Factor Venn Diagram for GCF & LCM."),
        ("Fraction Strips & Comparator", "Units 2, 3", "Compare fraction strips side-by-side inside the twin comparator channel to find common denominators, model fraction division (how many fit?), and build tape diagrams."),
        ("Base-10 Place Value Blocks", "Units 2, 6, 8", "Trade 100-flats, 10-rods, and 1-unit cubes across decimal place columns, and pack unit cubes into 3D rectangular prisms to prove V = l·w·h."),
        ("Ten-Frames & Two-Tone Counters", "Units 3, 6, 10", "Model percents on 10×10 grids and pair +1 and -1 two-tone counters to form Zero Pairs (1 + (-1) = 0) for signed integer addition and subtraction."),
        ("Part-Whole Math Dominoes", "Unit 7", "Model part-part-whole missing addends (x + a = b) before solving one-step equations with inverse operations."),
        ("Algebra & Area Tiles", "Units 4, 7, 8", "Arrange x², x, and unit tiles on the factoring frame to see equivalent expressions, balance equations on a two-pan scale, and unfold 2D surface-area nets."),
        ("Modulo-60 Geared Clock", "Unit 5", "Turn the minute hand through a true 12:1 planetary gear train to measure elapsed time and convert minutes to base-60 fractions of an hour."),
        ("Probability Dice & Spinner", "Units 9, 10", "Roll fair polyhedral dice and spin the 10-part dial to compare experimental relative frequencies against theoretical sample spaces."),
        ("100-Point Token Scoreboard", "All 10 Units", "Drop 1 [+10] token into Sockets #1–#10 for solving in 1st Way; stack a 2nd [+10] token (+20 DOUBLE) for verifying with 2nd Way; build a 10-token [100] Tower!"),
    ]
    gy = 29.2
    gh = 19.5
    for idx, (k_sku, k_units, k_how) in enumerate(kit_guide_rows):
        p.rect(margin, gy, uw, gh, fill=WHITE if idx % 2 == 0 else SUBTLE_HDR, stroke=LIGHT_BORDER, line_w=0.18)
        p.text(margin + 2.2, gy + 10.5, k_sku, size=1.82, bold=True, color=TEAL_ACCENT, max_w=52.0)
        p.text(margin + 56.0, gy + 10.5, k_units, size=1.80, bold=True, mono=True, color=INK, max_w=20.0)
        p.para(margin + 78.0, gy + 5.2, k_how, max_w=uw - 80.5, size=1.78, color=INK, leading=1.18, max_lines=3)
        gy += gh

    p.rect(margin, 227.5, uw, 34.0, fill=M2_BG, stroke=TEAL_ACCENT, r=1.0, line_w=0.28)
    p.text(margin + 3.0, 232.8, "COMPANION RESOURCES & OPEN CURRICULUM LIBRARY", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin + 3.0, 238.5, "• Spiral-Bound Lay-Flat Student Workbooks & Unified Teacher's Guide: https://www.lulu.com/spotlight/stackcalc", size=1.85, bold=True, color=INK)
    p.text(margin + 3.0, 244.0, "• Illustrated Companion Book — From Blocks to the Stack (Amazon): https://link.amazon/B0f5cP0Ur", size=1.85, color=INK)
    p.text(margin + 3.0, 249.5, "• Classroom Manipulative Sets & Hardware: https://stackcalcmath.etsy.com  |  https://stackcalc.io", size=1.85, color=INK)
    p.text(margin + 3.0, 255.0, "• Printable Individual Chapter Packets (Units 1–10): https://stackcalc.io/curriculum/big-ideas-middle-school-sc6-workbook/", size=1.85, color=INK)

    p.text(margin, p.h - 5.2, "StackCalc SC-6 Textbook Supplement  •  Appendix C: Hands-On Manipulative Models Guide", size=1.88, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 5.2, f"Page {start_page + 2} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")
    c.showPage()

    # ---------------------------------------------------------
    # APPENDIX D (Page 106): Official 100-Point Mastery Certificate & Dot-Grid Scratchpad
    # ---------------------------------------------------------
    p = CanvasPage(c, letter)
    p.text(margin, 12.0, "BACK MATTER  •  APPENDIX D: CERTIFICATE OF MASTERY & DOT-GRID WORKSPACE", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin, 18.0, "Appendix D: 100-Point Mastery Certificate & Graph Scratchpad", size=3.9, bold=True, color=INK, max_w=uw)
    p.line(margin, 21.2, margin + uw, 21.2, color=INK, width=0.45)

    # Certificate Box (top half)
    cert_y = 25.0
    cert_h = 102.0
    p.rect(margin, cert_y, uw, cert_h, fill="#FEFCE8", stroke="#CA8A04", r=2.0, line_w=0.45)
    p.rect(margin + 3.0, cert_y + 3.0, uw - 6.0, cert_h - 6.0, fill=WHITE, stroke=TEAL_ACCENT, r=1.5, line_w=0.3)
    p.text(margin + uw / 2.0, cert_y + 14.0, "STACKCALC LEARNING LAB  •  BIG IDEAS MATH MIDDLE SCHOOL SUPPLEMENT", size=2.1, bold=True, mono=True, color=TEAL_ACCENT, align="center")
    p.text(margin + uw / 2.0, cert_y + 24.5, "CERTIFICATE OF TWO-METHOD MATHEMATICAL MASTERY", size=4.6, bold=True, color=INK, align="center")
    p.text(margin + uw / 2.0, cert_y + 35.5, "This certifies that: ________________________________________________________________", size=2.8, bold=True, color=INK, align="center")
    p.para(
        margin + 12.0,
        cert_y + 43.0,
        "has successfully completed the 10-Unit Big Ideas Math Middle School Two-Method Block & SC-6 Supplement—solving problems by hand using multiple textbook pathways (+10 Single-Way & +20 Double-Points Tokens), modeling concepts with hands-on manipulatives, and verifying work on the 4-register StackCalc SC-6 calculator.",
        max_w=uw - 24.0,
        size=2.15,
        color=SLATE,
        leading=1.25,
    )
    # 10 Unit Checkboxes inside Certificate
    u_line_1 = "   ".join(f"[ ] Unit {u_i}" for u_i in range(1, 6))
    u_line_2 = "   ".join(f"[ ] Unit {u_i}" for u_i in range(6, 11))
    p.text(margin + uw / 2.0, cert_y + 68.0, u_line_1, size=2.2, bold=True, mono=True, color=TEAL_ACCENT, align="center")
    p.text(margin + uw / 2.0, cert_y + 75.0, u_line_2, size=2.2, bold=True, mono=True, color=TEAL_ACCENT, align="center")
    p.text(margin + 14.0, cert_y + 90.0, "Teacher / Parent Coach Signature: _____________________________   Date: _______________   100-Pt Towers Built: _____", size=2.15, bold=True, color=INK)

    # Dot-Grid Scratchpad (bottom half)
    grid_y = 132.0
    grid_h = 130.0
    p.rect(margin, grid_y, uw, grid_h, fill=WHITE, stroke=INK, r=1.0, line_w=0.28)
    p.rect(margin, grid_y, uw, 5.0, fill=INK, stroke=INK, r=0.8, line_w=0.2)
    p.text(margin + 3.0, grid_y + 3.5, "EXTRA 5 MM DOT-GRID MATHEMATICAL SCRATCHPAD (TAPE DIAGRAMS, NUMBER LINES, NETS & COORDINATE GRAPHS)", size=1.80, bold=True, mono=True, color=WHITE)
    for gx_mm in range(int(margin + 6), int(margin + uw - 4), 5):
        for gy_mm in range(int(grid_y + 10), int(grid_y + grid_h - 4), 5):
            p.circle(float(gx_mm), float(gy_mm), 0.22, fill=BORDER, stroke=BORDER, line_w=0.05)

    p.text(margin, p.h - 5.2, "StackCalc SC-6 Textbook Supplement  •  Appendix D: Mastery Certificate & Scratchpad", size=1.88, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 5.2, f"Page {start_page + 3} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")
    c.showPage()

    # ---------------------------------------------------------
    # APPENDIX E (Pages 107–111): Compact Student Self-Check Answer Key (All 900 Problems, 2 Units per Page)
    # ---------------------------------------------------------
    for pair_idx in range(5):
        u_pair = chapters[pair_idx * 2 : pair_idx * 2 + 2]
        pg_cur = start_page + 4 + pair_idx
        p = CanvasPage(c, letter)
        u_nums_str = f"UNITS {u_pair[0]['num']} & {u_pair[1]['num']}"
        p.text(
            margin,
            11.5,
            f"BACK MATTER  •  APPENDIX E: STUDENT SELF-CHECK ANSWER KEY ({u_nums_str} — FINAL ANSWERS ONLY)",
            size=1.95,
            bold=True,
            mono=True,
            color=TEAL_ACCENT,
        )
        p.text(
            margin,
            17.2,
            f"Appendix E: Student Self-Check Answer Key — Units {u_pair[0]['num']} & {u_pair[1]['num']}",
            size=3.75,
            bold=True,
            color=INK,
            max_w=uw,
        )
        p.text(
            margin,
            21.2,
            "Solve by hand first and verify on your SC-6 calculator before checking your final answer here. Full worked setups are in the Teacher's Guide.",
            size=1.78,
            color=SLATE,
            max_w=uw,
        )
        p.line(margin, 22.6, margin + uw, 22.6, color=INK, width=0.4)

        uy = 24.4
        for ch_obj in u_pair:
            secs = ch_obj["sections"]
            unit_box_h = 117.5
            p.rect(margin, uy, uw, unit_box_h, fill=WHITE, stroke=INK, r=0.9, line_w=0.26)
            p.rect(margin, uy, uw, 5.0, fill=INK, stroke=INK, r=0.7, line_w=0.2)
            p.text(
                margin + 2.5,
                uy + 3.4,
                f"UNIT {ch_obj['num']}: {ch_obj['title'].upper()} ({ch_obj['big_ideas_book'].upper()})",
                size=1.80,
                bold=True,
                mono=True,
                color=WHITE,
                max_w=uw - 5.0,
            )

            sec_avail_h = unit_box_h - 5.8
            sec_h = sec_avail_h / len(secs)
            for s_i, sec_obj in enumerate(secs):
                snum = sec_obj["sec_num"]
                stitle_clean = clean_section_title(snum, sec_obj["title"])
                sy = uy + 5.2 + s_i * sec_h
                if s_i > 0:
                    p.line(margin + 1.0, sy, margin + uw - 1.0, sy, color=BORDER, width=0.22)

                # Section title strip
                p.rect(margin + 0.8, sy + 0.4, uw - 1.6, 3.6, fill=SUBTLE_HDR, stroke=None)
                p.text(
                    margin + 2.2,
                    sy + 2.8,
                    f"Section {snum}: {stitle_clean}",
                    size=1.62,
                    bold=True,
                    color=TEAL_ACCENT,
                    max_w=uw - 4.4,
                )

                a_list = sec_obj["problems"][:10]
                b_list = SHEET_B_PROBLEMS[snum][:10]
                a_line_1 = "   ".join(f"A{pr['num']}: {pr['ans']}" for pr in a_list[:5])
                a_line_2 = "   ".join(f"A{pr['num']}: {pr['ans']}" for pr in a_list[5:10])
                b_line_1 = "   ".join(f"B{pr['num']}: {pr['ans']}" for pr in b_list[:5])
                b_line_2 = "   ".join(f"B{pr['num']}: {pr['ans']}" for pr in b_list[5:10])

                row_y0 = sy + 6.4
                step_r = (sec_h - 4.8) / 4.0
                p.text(margin + 2.4, row_y0, a_line_1, size=1.46, bold=True, mono=True, color=INK, max_w=uw - 4.8)
                p.text(margin + 2.4, row_y0 + step_r, a_line_2, size=1.46, bold=True, mono=True, color=INK, max_w=uw - 4.8)
                p.text(margin + 2.4, row_y0 + step_r * 2, b_line_1, size=1.46, mono=True, color=SLATE, max_w=uw - 4.8)
                p.text(margin + 2.4, row_y0 + step_r * 3, b_line_2, size=1.46, mono=True, color=SLATE, max_w=uw - 4.8)

            uy += unit_box_h + 3.2

        p.text(
            margin,
            p.h - 5.2,
            f"StackCalc SC-6 Textbook Supplement  •  Appendix E: Student Self-Check Answer Key (Units {u_pair[0]['num']}–{u_pair[1]['num']})",
            size=1.88,
            mono=True,
            color=MUTED,
        )
        p.text(margin + uw, p.h - 5.2, f"Page {pg_cur} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")
        c.showPage()


def draw_coach_guide_back_matter(c: canvas.Canvas, chapters: List[Dict[str, Any]], total_chapters: int) -> None:
    """Renders 2 Extra Back Matter Appendix Pages (Pages 11–12) at the end of the Coach Guide."""
    margin = 13.0
    uw = (letter[0] / mm) - 2 * margin

    # Page 11 (Appendix A): Master Diagnostic Misconception Matrix & 45-Day Pacing Schedule
    p = CanvasPage(c, letter)
    p.text(margin, 12.0, "TEACHER GUIDE BACK MATTER  •  DIAGNOSTIC MISCONCEPTION & REMEDIATION MATRIX", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin, 18.0, "Middle School 10-Unit Misconception & Hands-On Remediation Matrix", size=3.9, bold=True, color=INK, max_w=uw)
    p.line(margin, 21.2, margin + uw, 21.2, color=INK, width=0.45)

    p.rect(margin, 24.0, uw, 5.0, fill=INK, stroke=INK, r=0.7, line_w=0.2)
    p.text(margin + 2.2, 27.4, "UNIT & HANDS-ON MODEL", size=1.75, bold=True, mono=True, color=WHITE)
    p.text(margin + 46.0, 27.4, "TARGET CLASSROOM MISCONCEPTION", size=1.75, bold=True, mono=True, color=WHITE)
    p.text(margin + 116.0, 27.4, "HANDS-ON BLOCK & SC-6 REMEDIATION", size=1.75, bold=True, mono=True, color=WHITE)

    my = 29.0
    mh = 22.8
    for idx, ch in enumerate(chapters):
        clean_tools = clean_manipulative_label(ch["kit_summary"])
        p.rect(margin, my, uw, mh, fill=WHITE if idx % 2 == 0 else SUBTLE_HDR, stroke=LIGHT_BORDER, line_w=0.18)
        p.text(margin + 2.0, my + 6.0, f"Unit {ch['num']}: {ch['title'][:18]}", size=1.75, bold=True, color=TEAL_ACCENT, max_w=42.0)
        p.text(margin + 2.0, my + 11.5, clean_tools[:24], size=1.55, mono=True, color=SLATE, max_w=42.0)
        p.para(margin + 46.0, my + 4.8, ch["coach_misconception"], max_w=67.0, size=1.62, color=INK, leading=1.14, max_lines=4)
        p.para(margin + 116.0, my + 4.8, ch["coach_remediation"], max_w=uw - 118.0, size=1.62, color=SLATE, leading=1.14, max_lines=4)
        my += mh

    p.text(margin, p.h - 5.0, "Teaching with the Stack  •  Middle School Diagnostic Misconception Matrix", size=1.85, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 5.0, f"Part II Page {total_chapters + 1} of {total_chapters + 2}", size=1.85, bold=True, mono=True, color=INK, align="right")
    c.showPage()

    # Page 12 (Appendix B): Photocopiable Classroom / Homeschool Progress Roster & Notes
    p = CanvasPage(c, letter)
    p.text(margin, 12.0, "TEACHER GUIDE BACK MATTER  •  CLASSROOM & HOMESCHOOL PROGRESS ROSTER", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin, 18.0, "Photocopiable 10-Unit Middle School Student Mastery Tracker", size=3.9, bold=True, color=INK, max_w=uw)
    p.line(margin, 21.2, margin + uw, 21.2, color=INK, width=0.45)

    p.rect(margin, 24.0, uw, 5.5, fill=INK, stroke=INK, r=0.7, line_w=0.2)
    p.text(margin + 2.5, 27.8, "STUDENT NAME / PERIOD", size=1.75, bold=True, mono=True, color=WHITE)
    for u_i in range(1, 11):
        ux = margin + 56.0 + (u_i - 1) * 13.0
        p.text(ux, 27.8, f"U{u_i}", size=1.75, bold=True, mono=True, color=WHITE)

    ry = 29.5
    rh = 9.0
    for r_i in range(20):
        p.rect(margin, ry, uw, rh, fill=WHITE if r_i % 2 == 0 else SUBTLE_HDR, stroke=LIGHT_BORDER, line_w=0.18)
        p.text(margin + 2.5, ry + 6.0, f"{r_i + 1:02d}. ________________________", size=1.75, color=SLATE, max_w=52.0)
        for u_i in range(1, 11):
            ux = margin + 55.0 + (u_i - 1) * 13.0
            p.rect(ux, ry + 2.0, 9.5, 5.0, fill=WHITE, stroke=BORDER, r=0.4, line_w=0.15)
        ry += rh

    p.rect(margin, 214.0, uw, 48.0, fill=WHITE, stroke=TEAL_ACCENT, r=1.0, line_w=0.28)
    p.rect(margin, 214.0, uw, 5.2, fill=TEAL_ACCENT, stroke=TEAL_ACCENT, r=0.8, line_w=0.2)
    p.text(margin + 3.0, 217.6, "TEACHER OBSERVATION NOTES & INTERVENTION LOG", size=1.85, bold=True, mono=True, color=WHITE)
    p.text(margin + 3.5, 224.5, "• Spiral-Bound Student Workbooks & Teacher Guides (Lulu): https://www.lulu.com/spotlight/stackcalc", size=1.85, bold=True, color=INK)
    p.text(margin + 3.5, 230.0, "• Companion Book — From Blocks to the Stack (Amazon): https://link.amazon/B0f5cP0Ur  |  Manipulatives: https://stackcalc.io", size=1.85, color=INK)
    for ln_i in range(3):
        ly = 238.5 + ln_i * 7.0
        p.line(margin + 3.5, ly, margin + uw - 3.5, ly, color=LIGHT_BORDER, width=0.25)

    p.text(margin, p.h - 5.0, "Teaching with the Stack  •  Middle School Student Mastery Roster", size=1.85, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 5.0, f"Part II Page {total_chapters + 2} of {total_chapters + 2}", size=1.85, bold=True, mono=True, color=INK, align="right")
    c.showPage()


def generate_student_workbook_pdf(chapters: List[Dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_path), pagesize=letter)
    c.setTitle("Middle School Math Lab: Big Ideas Two-Method Block & SC-6 Student Workbook")
    c.setAuthor("StackCalc Learning Lab")

    total_secs = sum(len(ch["sections"]) for ch in chapters)
    core_pages = 2 + len(chapters) + total_secs * 2  # 102 core numbered pages
    total_pages = core_pages + 9  # + 9 Back Matter Appendix pages (pp. 103-111, including 5-page Compact Answer Key)

    # Page 1: Bestseller Minimalist Front Cover (matching SC-6 & SC-32 books)
    draw_curriculum_bestseller_front_cover(c, 0.0, 0.0, letter[0], letter[1], BOOK_COVER_SPECS["big_ideas"])
    c.showPage()

    # Front Matter Pages i and ii (Title Page + How to Use / Pacing Guide)
    draw_workbook_front_matter(c, chapters, is_coach=False)

    # Page 1: Master Unit & Section Index
    p = CanvasPage(c, letter)
    draw_student_cover_page(p, chapters)
    c.showPage()

    # Page 2: 1-Page Token Scoring & SC-6 Work-Check Guide
    pg_score = CanvasPage(c, letter)
    draw_token_scoring_guide_page(pg_score, chapters, page_label=f"Page 2 of {total_pages}")
    c.showPage()

    page_num = 3
    for ch in chapters:
        # Unit "How Things Work" Multi-Paragraph Story & Application Opener Page
        pu = CanvasPage(c, letter)
        draw_unit_story_page(pu, ch, page_num, total_pages)
        c.showPage()
        page_num += 1

        for sec in ch["sections"]:
            # Worksheet A: Key Ideas & Two-Method Practice
            pa = CanvasPage(c, letter)
            draw_student_section_page_a(pa, ch, sec, page_num, total_pages)
            c.showPage()
            page_num += 1

            # Worksheet B: Modeling Real Life & Multi-Method Applications
            pb = CanvasPage(c, letter)
            draw_student_section_page_b(pb, ch, sec, page_num, total_pages)
            c.showPage()
            page_num += 1

    # Extra Back Matter Pages 103–111 (Appendices A–E)
    draw_student_workbook_back_matter(c, chapters, page_num, total_pages)

    c.save()
    print(f"[OK] Built Student Supplement Workbook (Spiral Edition): {output_path} ({output_path.stat().st_size / 1024:.1f} KB, Cover + 2 Front Matter + {total_pages} numbered pages = {total_pages + 3} total pages)")


# =============================================================================
# 2. COMPACT 10-PAGE COACH & SOLUTION GUIDE (EXACTLY 1 Page Per Chapter!)
# =============================================================================
def draw_coach_chapter_page(p: CanvasPage, ch: Dict[str, Any], total_chapters: int) -> None:
    margin = 10.0
    uw = p.w - 2 * margin
    ch_num = ch["num"]
    clean_tools = clean_manipulative_label(ch["kit_summary"])

    # 1. Top Chapter Header (y = 8.5 .. 22.8 mm)
    p.text(
        margin,
        11.6,
        f"TEACHING WITH THE STACK  •  MIDDLE SCHOOL CONCEPT & SECTION KEY (UNIT {ch_num} OF {total_chapters})",
        size=2.1,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
    )
    p.draw_tutorial_keycap(margin + uw - 5.6, 8.6, w=4.8, h=4.0)
    p.text(margin, 17.2, f"Unit {ch_num}: {ch['title']} — Practice A & B Complete Key", size=4.15, bold=True, color=INK, max_w=uw - 10.0)
    p.text(margin, 21.3, f"{ch['big_ideas_book']}  •  Hands-On Models: {clean_tools}", size=2.05, bold=True, color=SLATE, max_w=uw)
    p.line(margin, 22.6, margin + uw, 22.6, color=INK, width=0.45)

    # 2. Coaching & Manipulative Setup Strip (y = 23.6 .. 39.6 mm, height = 16.0 mm)
    p.rect(margin, 23.6, uw, 16.0, fill=SUBTLE_HDR, stroke=INK, r=0.9, line_w=0.28)
    p.rect(margin + uw - 25.5, 24.5, 24.0, 14.2, fill=WHITE, stroke=LIGHT_BORDER, r=0.6, line_w=0.2)
    p.image(ASSETS_MANUALS_DIR / ch["hero_png"], margin + uw - 25.0, 25.0, 23.0, 13.2)

    text_w = uw - 29.0
    p.para(
        margin + 2.2,
        26.7,
        f"Target Misconception: {ch['coach_misconception']}",
        max_w=text_w,
        size=1.9,
        bold=True,
        color=INK,
        leading=1.18,
        max_lines=2,
    )
    p.para(
        margin + 2.2,
        31.8,
        f"Hands-On Block Remediation: {ch['coach_remediation']}",
        max_w=text_w,
        size=1.86,
        color=SLATE,
        leading=1.18,
        max_lines=2,
    )
    p.text(
        margin + 2.2,
        38.0,
        "Double-Points Mastery Scoring: +10 points = Textbook Method 1 (1st Way); +20 points = Verified with Textbook Method 2 (2nd Way)!",
        size=1.78,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=text_w,
    )

    # 3. Section-by-Section Complete Answer Key Bands (y = 41.0 .. 269.0 mm)
    #    Each section displays Practice A (#1-#10) on the Left Half and Practice B (#1-#10) on the Right Half!
    secs = ch["sections"]
    n_secs = len(secs)
    avail_h = 228.0
    sec_gap = 1.6
    sec_h = (avail_h - (n_secs - 1) * sec_gap) / n_secs

    for s_idx, sec in enumerate(secs):
        sec_num = sec["sec_num"]
        stitle = clean_section_title(sec_num, sec["title"])
        sy = 41.0 + s_idx * (sec_h + sec_gap)
        p.rect(margin, sy, uw, sec_h, fill=WHITE, stroke=INK, r=0.8, line_w=0.28)

        # Section Header Bar (4.6 mm tall)
        p.rect(margin, sy, uw, 4.6, fill=INK, stroke=INK, r=0.6, line_w=0.2)
        ex1 = sec["examples"][0]
        ex1_ans_txt = clean_ex1_ans(sec_num, ex1["ans"])
        ped = SECTION_PEDAGOGY[sec_num]
        ex2 = ped["ex2"]
        pg_a = 3 + ch_num + (sec["day_num"] - 1) * 2
        pg_b = pg_a + 1
        compact_ways = (
            ped["big_ideas_method"]
            .replace("Way 1: ", "W1: ")
            .replace("Way 2: ", "W2: ")
            .replace("Way 3: ", "W3: ")
        )
        p.text(
            margin + 2.0,
            sy + 3.2,
            f"SEC {sec_num} (pp.{pg_a}-{pg_b}): {stitle.upper()}",
            size=1.80,
            bold=True,
            mono=True,
            color=WHITE,
            max_w=99.0,
        )
        p.text(
            margin + uw - 2.0,
            sy + 3.2,
            f"Methods: {compact_ways}",
            size=1.64,
            mono=True,
            color="#E2E8F0",
            align="right",
            max_w=94.0,
        )

        # Sub-header strip (3.4 mm tall) for Practice A (Left) vs. Practice B (Right) + Worked Example Keys
        sub_y = sy + 4.6
        sub_h = 3.4
        half_w = uw / 2.0
        p.rect(margin, sub_y, half_w, sub_h, fill=M1_BG, stroke=LIGHT_BORDER, line_w=0.18)
        p.rect(margin + half_w, sub_y, half_w, sub_h, fill=M2_BG, stroke=LIGHT_BORDER, line_w=0.18)
        p.text(
            margin + 1.8,
            sub_y + 2.45,
            f"PRACTICE A (p.{pg_a}): KEY IDEAS (#1-#10)",
            size=1.55,
            bold=True,
            mono=True,
            color=INK,
            max_w=46.0,
        )
        p.text(
            margin + half_w - 1.8,
            sub_y + 2.45,
            f"ExA: {ex1_ans_txt}",
            size=1.50,
            bold=True,
            mono=True,
            color=TEAL_ACCENT,
            align="right",
            max_w=48.0,
        )
        p.text(
            margin + half_w + 1.8,
            sub_y + 2.45,
            f"PRACTICE B (p.{pg_b}): REAL LIFE (#1-#10)",
            size=1.55,
            bold=True,
            mono=True,
            color=TEAL_ACCENT,
            max_w=46.0,
        )
        p.text(
            margin + uw - 1.8,
            sub_y + 2.45,
            f"ExB: {ex2['ans']}",
            size=1.50,
            bold=True,
            mono=True,
            color=INK,
            align="right",
            max_w=48.0,
        )

        # 5 Rows × 4 Columns Grid:
        #   Left Half (Practice A): 5 rows × 2 cols (#1-#10)
        #   Right Half (Practice B): 5 rows × 2 cols (#1-#10)
        grid_y = sub_y + sub_h
        grid_h = sec_h - 8.0
        row_h = grid_h / 5.0
        qcol_w = half_w / 2.0

        p.line(margin + half_w, sy + 4.6, margin + half_w, sy + sec_h, color=INK, width=0.3)
        p.line(margin + qcol_w, grid_y, margin + qcol_w, sy + sec_h, color=LIGHT_BORDER, width=0.18)
        p.line(margin + half_w + qcol_w, grid_y, margin + half_w + qcol_w, sy + sec_h, color=LIGHT_BORDER, width=0.18)

        a_probs = sec["problems"][:10]
        b_probs = SHEET_B_PROBLEMS[sec_num][:10]

        for r in range(5):
            cy = grid_y + r * row_h
            if r > 0:
                p.line(margin, cy, margin + uw, cy, color=LIGHT_BORDER, width=0.16)

            for c in range(2):
                p_idx = r * 2 + c
                # --- Practice A cell ---
                pa_prob = a_probs[p_idx]
                ax = margin + c * qcol_w
                pa_setup, pa_keys = parse_tutor_setup_and_keys(sec_num, pa_prob)
                p.text(ax + 1.3, cy + row_h * 0.32, f"A{pa_prob['num']}:", size=1.60, bold=True, mono=True, color=INK)
                p.text(
                    ax + 6.4,
                    cy + row_h * 0.32,
                    pa_prob["ans"],
                    size=1.60,
                    bold=True,
                    mono=True,
                    color=TEAL_ACCENT,
                    max_w=qcol_w - 7.6,
                )
                p.text(
                    ax + 1.3,
                    cy + row_h * 0.62,
                    f"Setup: {pa_setup}",
                    size=1.35,
                    bold=True,
                    color=SLATE,
                    max_w=qcol_w - 2.4,
                )
                p.text(
                    ax + 1.3,
                    cy + row_h * 0.90,
                    f"SC-6: {pa_keys}",
                    size=1.28,
                    mono=True,
                    color=MUTED,
                    max_w=qcol_w - 2.4,
                )

                # --- Practice B cell ---
                pb_prob = b_probs[p_idx]
                bx = margin + half_w + c * qcol_w
                pb_setup, pb_keys = parse_tutor_setup_and_keys(sec_num, pb_prob)
                p.text(bx + 1.3, cy + row_h * 0.32, f"B{pb_prob['num']}:", size=1.60, bold=True, mono=True, color=TEAL_ACCENT)
                p.text(
                    bx + 6.4,
                    cy + row_h * 0.32,
                    pb_prob["ans"],
                    size=1.60,
                    bold=True,
                    mono=True,
                    color=INK,
                    max_w=qcol_w - 7.6,
                )
                p.text(
                    bx + 1.3,
                    cy + row_h * 0.62,
                    f"Setup: {pb_setup}",
                    size=1.35,
                    bold=True,
                    color=SLATE,
                    max_w=qcol_w - 2.4,
                )
                p.text(
                    bx + 1.3,
                    cy + row_h * 0.90,
                    f"SC-6: {pb_keys}",
                    size=1.28,
                    mono=True,
                    color=MUTED,
                    max_w=qcol_w - 2.4,
                )

    p.text(
        margin,
        p.h - 5.0,
        f"Teaching with the Stack (Middle School Section Key • Practice A & B)  •  Unit {ch_num}: {ch['title']}",
        size=1.85,
        mono=True,
        color=MUTED,
        max_w=uw - 38.0,
    )
    p.text(margin + uw, p.h - 5.0, f"Part II Page {ch_num} of {total_chapters}", size=1.85, bold=True, mono=True, color=INK, align="right")


def generate_coach_guide_pdf(chapters: List[Dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_path), pagesize=letter)
    c.setTitle("Teaching with the Stack: Middle School Coach & Solution Guide")
    c.setAuthor("StackCalc Learning Lab")

    draw_curriculum_bestseller_front_cover(c, 0.0, 0.0, letter[0], letter[1], BOOK_COVER_SPECS["teacher_guide"])
    c.showPage()

    total_ch = len(chapters)
    draw_workbook_front_matter(c, chapters, is_coach=True)
    for ch in chapters:
        p = CanvasPage(c, letter)
        draw_coach_chapter_page(p, ch, total_ch + 2)
        c.showPage()
    draw_coach_guide_back_matter(c, chapters, total_ch)

    c.save()
    print(f"[OK] Built Spiral Coach Guide: {output_path} ({output_path.stat().st_size / 1024:.1f} KB, 15 total pages: Cover + pp. i-ii + 1-12)")


def generate_big_ideas_lulu_covers(chapters: List[Dict[str, Any]], out_dir: Path) -> None:
    """Generates 2-page US Letter + 0.125-inch bleed (8.75\" x 11.25\") Lulu Coil-Bound Front & Back Cover PDFs using the Bestseller Cover Engine."""
    out_dir.mkdir(parents=True, exist_ok=True)
    wb_cover = out_dir / "bigideas_middle_school_sc6_workbook_lulu_cover.pdf"
    coach_cover = out_dir / "bigideas_middle_school_sc6_coach_lulu_cover.pdf"
    generate_lulu_coil_cover_pdf(wb_cover, "big_ideas")
    generate_lulu_coil_cover_pdf(coach_cover, "teacher_guide")
    print(f"[OK] Built Lulu Coil-Bound Cover PDFs: {wb_cover.name}, {coach_cover.name}")


def generate_chapter_pdfs(chapters: List[Dict[str, Any]], out_dir: Path) -> None:
    """Generates 10 standalone, parent-friendly Chapter/Unit PDFs (Units 1-10) so each chapter can be printed separately."""
    out_dir.mkdir(parents=True, exist_ok=True)
    total_ch = len(chapters)
    for ch in chapters:
        ch_num = ch["num"]
        unit_pdf_path = out_dir / f"bigideas_middle_school_sc6_unit_{ch_num:02d}.pdf"
        c = canvas.Canvas(str(unit_pdf_path), pagesize=letter)
        c.setTitle(f"StackCalc SC-6 Big Ideas Math Supplement — Unit {ch_num}: {ch['title']} (Printable Chapter Packet)")
        c.setAuthor("StackCalc Learning Lab")

        unit_total_pages = 1 + len(ch["sections"]) * 2 + 1
        page_num = 1

        # Page 1: Unit Story & Concept Opener
        pu = CanvasPage(c, letter)
        draw_unit_story_page(pu, ch, page_num, unit_total_pages)
        c.showPage()
        page_num += 1

        # Section Practice A & Practice B Worksheets
        for sec in ch["sections"]:
            pa = CanvasPage(c, letter)
            draw_student_section_page_a(pa, ch, sec, page_num, unit_total_pages)
            c.showPage()
            page_num += 1

            pb = CanvasPage(c, letter)
            draw_student_section_page_b(pb, ch, sec, page_num, unit_total_pages)
            c.showPage()
            page_num += 1

        # Final Page: 1-Page Parent & Teacher Coach Answer Key for this Unit
        pc = CanvasPage(c, letter)
        draw_coach_chapter_page(pc, ch, total_ch)
        c.showPage()

        c.save()
        print(
            f"[OK] Built Standalone Unit {ch_num:02d} PDF: {unit_pdf_path.name} "
            f"({unit_pdf_path.stat().st_size / 1024:.1f} KB, {unit_total_pages} pages)"
        )


UNIT_BOOK_REFS: Dict[int, str] = {
    1: "**\"Why 24 Is the Champion Packing Number & The 17-Year Cicada Mystery\"** — [SC-6 Ch. 4: Operations & Skip-Counting](../manuals/sc6/04-operations-skip-counting.md) & [Ch. 7: Data, Probability & Primes](../manuals/sc6/07-data-probability-primes.md) ([Appendix B Lessons 9–12](../manuals/sc6/appendix-b-teacher-lesson-plans.md))",
    2: "**\"The Pharaoh's Bakery, 84mm Fraction Towers & Simon Stevin's Decimals\"** — [SC-6 Ch. 5: Fractions, Decimals & Ratios](../manuals/sc6/05-fractions-decimals-ratios.md) ([Appendix B Lessons 15–19](../manuals/sc6/appendix-b-teacher-lesson-plans.md))",
    3: "**\"Pythagoras's Guitar Strings & The Hunting-Tooth Bicycle Gear Secret\"** — [SC-6 Ch. 5: Fractions, Decimals & Ratios](../manuals/sc6/05-fractions-decimals-ratios.md) ([Appendix B Lesson 18](../manuals/sc6/appendix-b-teacher-lesson-plans.md))",
    4: "**\"Breaking Apart Rectangles, Frame Borders & Al-Khwarizmi's Squares\"** — [SC-6 Ch. 4: Operations & Skip-Counting](../manuals/sc6/04-operations-skip-counting.md) & [SC-32 Ch. 7: Polynomials](../manuals/sc32/07-polynomials-brent-solver.md)",
    5: "**\"Why Babylonians Counted to 60 & The Rope-Stretchers of the Nile\"** — [SC-6 Ch. 6: Geometry, Time & Surface Area](../manuals/sc6/06-geometry-surface-area.md) ([Appendix B Lessons 20–21](../manuals/sc6/appendix-b-teacher-lesson-plans.md))",
    6: "**\"Zero-Pair Counters, Sub-Zero Number Lines & Descartes's Coordinate Fly\"** — [SC-6 Ch. 3: Counting & Place Value](../manuals/sc6/03-counting-place-value.md) & [Ch. 6: Geometry](../manuals/sc6/06-geometry-surface-area.md)",
    7: "**\"Al-Jabr's Balanced Two-Pan Scale & Missing-Addend Mysteries\"** — [SC-6 Ch. 8: Math Quiz Engine](../manuals/sc6/08-math-quiz-engine.md) & [SC-32 Ch. 3: Algebra](../manuals/sc32/03-algebra-transcendentals.md)",
    8: "**\"Galileo's Giant Bone Mystery (The Square-Cube Law) & Archimedes's Crown\"** — [SC-6 Ch. 6: Geometry & Surface Area](../manuals/sc6/06-geometry-surface-area.md) ([Appendix B Lesson 22](../manuals/sc6/appendix-b-teacher-lesson-plans.md))",
    9: "**\"Becoming a Data Detective: Leveling Mean Towers, Quartiles & Outliers\"** — [SC-6 Ch. 7: Data, Probability & Primes](../manuals/sc6/07-data-probability-primes.md) ([Appendix B Lessons 23–25](../manuals/sc6/appendix-b-teacher-lesson-plans.md))",
    10: "**\"Sir Francis Galton's 1873 Bean Machine & Fair Polyhedral Dice\"** — [SC-6 Ch. 7: Data, Probability & Primes](../manuals/sc6/07-data-probability-primes.md) & [Ch. 9: Applied STEM Labs](../manuals/sc6/09-applied-stem-labs.md)",
}

UNIT_PRODUCT_LINKS: Dict[int, str] = {
    1: "[Counting & Array Studio (`COUNT-01`)](../products/counting-tiles/index.md) &bull; [Prime Factor Studio (`PRIME-01`)](../products/prime-factor-studio/index.md)",
    2: "[84mm Fraction Comparator Studio (`FRAC-01`)](../products/fraction-studio/index.md) &bull; [Place Value Studio (`PLACE-01`)](../products/place-value/index.md)",
    3: "[84mm Fraction Studio (`FRAC-01`)](../products/fraction-studio/index.md) &bull; [Ten-Frame Studio (`BASE-10`)](../products/ten-frames/index.md)",
    4: "[Algebra Tile Studio (`ALGB-01`)](../products/algebra-boxes/index.md) &bull; [Counting & Array Studio (`COUNT-01`)](../products/counting-tiles/index.md)",
    5: "[Counting & Array Studio (`COUNT-01`)](../products/counting-tiles/index.md) &bull; [Modulo-60 Classroom Clock (`TIME-01`)](../products/classroom-clock/index.md)",
    6: "[Ten-Frame Two-Tone Studio (`BASE-10`)](../products/ten-frames/index.md) &bull; [Place Value Studio (`PLACE-01`)](../products/place-value/index.md)",
    7: "[Algebra Tile Studio (`ALGB-01`)](../products/algebra-boxes/index.md) &bull; [Math Domino Studio (`DOMI-01`)](../products/math-dominoes/index.md)",
    8: "[Place Value 3D Cubes (`PLACE-01`)](../products/place-value/index.md) &bull; [Algebra & Geometry Studio (`ALGB-01`)](../products/algebra-boxes/index.md)",
    9: "[Counting & Data Tower Studio (`COUNT-01`)](../products/counting-tiles/index.md) &bull; [Probability & Stats Studio (`PROB-01`)](../products/dice-and-spinner/index.md)",
    10: "[Probability Dice & Spinner Studio (`PROB-01`)](../products/dice-and-spinner/index.md) &bull; [Ten-Frame Studio (`BASE-10`)](../products/ten-frames/index.md)",
}


# =============================================================================
# 3. SYNCHRONIZE WEBSITE MARKDOWN (docs/curriculum/big-ideas-middle-school-sc6-workbook.md)
# =============================================================================
def sync_curriculum_markdown(chapters: List[Dict[str, Any]], md_path: Path) -> None:
    lines: List[str] = [
        "# Big Ideas Math Middle School: Two-Method Hands-On Block & SC-6 Supplement",
        "",
        "<div class=\"te-viewport-header mb-6\">",
        "  <span class=\"te-viewport-sku\">BIG IDEAS MATH SUPPLEMENT // 10 UNITS &bull; 45 SECTIONS &bull; 90 WORKSHEETS</span>",
        "  <span class=\"te-viewport-status text-amber-400\">● 900 MULTI-METHOD PRACTICE PROBLEMS &bull; 100-POINT DAILY GOAL</span>",
        "</div>",
        "",
        "<nav class=\"curriculum-subnav flex flex-wrap gap-2 p-2.5 rounded-xl bg-[#0D1017] border border-white/10 mb-8 font-mono text-xs\" aria-label=\"Curriculum Navigation\">",
        "  <a href=\"../\" class=\"px-3 py-1.5 rounded bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white transition font-bold\">📖 Master Guide</a>",
        "  <a href=\"../sc6-elementary-companion-workbook/\" class=\"px-3 py-1.5 rounded bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 border border-emerald-500/30 transition font-bold\">📗 SC-6 Companion Workbook (253 Problems)</a>",
        "  <a href=\"../sc32-scientific-companion-workbook/\" class=\"px-3 py-1.5 rounded bg-sky-500/20 hover:bg-sky-500/30 text-sky-300 border border-sky-500/30 transition font-bold\">📘 SC-32 Companion Casebook (339 Problems)</a>",
        "  <a href=\"./\" class=\"px-3 py-1.5 rounded bg-white text-slate-950 font-bold transition\">🚀 Big Ideas 45-Day Catch-Up (SC-6)</a>",
        "  <a href=\"../rpn-elementary-guide/\" class=\"px-3 py-1.5 rounded bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white transition font-bold\">⚡ RPN Power Guide</a>",
        "  <a href=\"../worksheets/\" class=\"px-3 py-1.5 rounded bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white transition font-bold\">📝 120 Station Worksheets</a>",
        "  <a href=\"../alignment-matrix/\" class=\"px-3 py-1.5 rounded bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white transition font-bold\">🎯 Standards Matrix</a>",
        "  <a href=\"../teacher-guide/\" class=\"px-3 py-1.5 rounded bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white transition font-bold\">🧑‍🏫 Teacher Guide</a>",
        "  <a href=\"../uil-competition/\" class=\"px-3 py-1.5 rounded bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white transition font-bold\">🏆 UIL Competition</a>",
        "</nav>",
        "",
        "**Grade 6 Complete + Grade 7 Bridge • Spiral Front & Back Matter • 10 Unit Introductions • 45 Textbook Sections • 90 Printable Worksheets (Practice A & B) • 90 Multi-Way Worked Examples • 900 Practice Problems • 5 Reference Appendices (Including Student Self-Check Answer Key)**",
        "",
        "<div class=\"hero-buttons\" style=\"margin: 1.25rem 0 1.75rem 0;\">",
        "  <a href=\"../../downloads/worksheets/bigideas_middle_school_sc6_daily_student_workbook.pdf\" class=\"md-button md-button--primary\">📄 Download Complete Spiral Student Workbook PDF (114 Pages • Cover + pp. i–ii + 1–111)</a>",
        "  <a href=\"https://www.lulu.com/spotlight/stackcalc\" class=\"md-button\">📘 Order Spiral-Bound Lay-Flat Workbook on Lulu ↗</a>",
        "  <a href=\"#print-individual-chapters-units-110-separate-pdfs-for-parents-teachers\" class=\"md-button\">🖨️ Print Individual Chapters (Units 1–10 Separate PDFs)</a>",
        "  <a href=\"../../downloads/worksheets/sc6_quest_token_scoring_guide.pdf\" class=\"md-button\">🏆 Download 1-Page Token Scoring & SC-6 Work-Check Guide PDF</a>",
        "  <a href=\"../../downloads/stackcalc-curriculum-guide-letter.pdf\" class=\"md-button\">🔑 Download Unified Master Teacher's Guide PDF (Includes Complete 900-Problem Worked Setups & Keys)</a>",
        "  <a href=\"../../downloads/worksheets/bigideas_middle_school_sc6_workbook_lulu_cover.pdf\" class=\"md-button\">🎨 Student Workbook Lulu Coil Cover PDF</a>",
        "</div>",
        "",
        "!!! abstract \"Built for Students Who Need Extra Practice: Two Textbook Ways, Hands-On Block Models & 100-Point Daily Goal\"",
        "    - **Relatable Real-World Stories & Honest Student Perspectives:** Every Unit and lesson connects the math to real-world situations—from packing drone batteries, building skate ramps, and comparing bicycle gear sprockets to engineering workshops, Antarctic penguin huddles, and wildlife puzzles—showing how students who initially doubt themselves discover why each mathematical concept works.",
        "    - **100% Focused on How *Big Ideas Math* Teaches & Tests Each Concept:** Every section tracks the exact paper-and-pencil algorithms, conceptual models, and vocabulary (*dividend, divisor, quotient, prime factorization, GCF, LCM, reciprocal, tape diagram, ratio table, unit rate, equivalent expressions, Distributive Property, inverse operations, net, interquartile range (IQR), mean absolute deviation (MAD)*) that students are tested on in school.",
        "    - **2 or 3 Authentic Textbook Ways & 100-Point Daily Goal:** Every Worked Example explicitly teaches the **distinct textbook solution pathways from *Big Ideas Math*** (`WAY 1`, `WAY 2`, and `WAY 3` where applicable). Students reach the **100-Point Daily Goal** either by solving **any 5 problems in 2 Ways (`5 × 20 = 100 pts`)** OR **all 10 problems in 1 Way (`10 × 10 = 100 pts`)**.",
        "    - **Warm-Up Step 1 Starter Scaffolds (`#1–#2`), Common-Trap Alerts & Graphic Organizers:** Every worksheet includes a section-specific **`⚠️ WATCH OUT:`** misconception alert, a 1-line **Starter Step 1** prompt on Problems `#1–#2` to eliminate blank-page anxiety, and faint ready-to-use graphic organizers (number lines, ratio tables, mini coordinate grids, Venn diagrams, and box-plot axes) right inside the problem cards.",
        "    - **Blocks Reinforce Textbook Concepts Where Applicable:** Physical manipulatives (Array Tiles, Prime Factor Towers, Fraction Strips, Place Value Blocks, Two-Tone Zero-Pair Counters, Geared Modulo-60 Clock, Algebra Tiles, and Probability Dice) reinforce textbook concepts where they naturally fit, while paper/number-line/graph/table/formula sections focus directly on the textbook strategy.",
        "    - **Spiral-Bound Lay-Flat Edition on Lulu, Complete 114-Page PDF (with Student Self-Check Answer Key), or Individual Chapter Packets:** Order the **Coil-Bound Lay-Flat Edition on [Lulu Press ↗](https://www.lulu.com/spotlight/stackcalc)** (including Front Matter `pp. i–ii` and Back Matter `Appendices A–E` on `pp. 103–111` with final answers for all 900 problems), print the complete PDF, or download any of the **10 standalone Chapter/Unit PDFs below** (10–14 pages each).",
        "",
        "---",
        "",
        "## 🖨️ Print Individual Chapters (Units 1–10 Separate PDFs for Parents & Teachers)",
        "",
        "Don't want to print all 114 pages at once? Each standalone **Chapter Packet PDF** below contains that unit's **1-Page Real-World Story & Concept Opener**, all **Practice A & Practice B Section Worksheets** (`20 problems per section`), and the **1-Page Parent & Teacher Coach Answer Key** at the back of the packet.",
        "",
        "| Unit | Big Ideas Math Chapter & Grade | Sections & Practice Load | *From Blocks to the Stack* Story & Block Listings | Standalone Printable Chapter PDF |",
        "| :---: | :--- | :--- | :--- | :--- |",
    ]

    for ch in chapters:
        ch_num = ch["num"]
        secs = ch["sections"]
        sec_range = f"Sections {secs[0]['sec_num']}–{secs[-1]['sec_num']}"
        n_ws = len(secs) * 2
        n_probs = len(secs) * 20
        unit_pages = 1 + n_ws + 1
        unit_pdf_md = f"../downloads/worksheets/bigideas_middle_school_sc6_unit_{ch_num:02d}.pdf"
        book_ref = UNIT_BOOK_REFS.get(ch_num, "[SC-6 Elementary Manual](../manuals/sc6/index.md)")
        prod_links = UNIT_PRODUCT_LINKS.get(ch_num, "[Manipulative Kits](../products/curriculum-and-decks.md)")
        lines.append(
            f"| **[Unit {ch_num}](#unit-{ch_num})** | **{ch['title']}**<br>*{ch['big_ideas_book']}* | {sec_range}<br>(`{n_ws} Worksheets • {n_probs} Problems`) | {book_ref}<br>**Blocks:** {prod_links} &bull; [Etsy ↗](https://stackcalcmath.etsy.com) &bull; [Slant 3D ↗](https://teleportpod.com/portals/profile/StackCalc) &bull; [Printables ↗](https://www.printables.com/@StackCalc_5593834) | [**📄 Print Unit {ch_num} PDF ({unit_pages} pp.)**]({unit_pdf_md}) |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 🏆 Optional Desk Companion: The 100-Point Double-Points Scoreboard (`QUEST-01`)",
        "",
        "To motivate students to master multiple textbook methods on every worksheet, pair the workbook with the **[100-Point SC-6 Scoreboard & Token Kit (`QUEST-01`)](../products/quest-scoreboard/index.md)** ([Order on Etsy ↗](https://stackcalcmath.etsy.com) • [Order Factory Print on Slant 3D ↗](https://teleportpod.com/portals/profile/StackCalc) • [Free Print Files on Printables ↗](https://www.printables.com/@StackCalc_5593834)):",
        "",
        "| Component | Layout | How Double-Points Scoring Works |",
        "| :--- | :--- | :--- |",
        "| **1. 10-Problem Scoreboard Grid (`1–10` + `100` + `(?)`)** | `6×2 = 12` sockets | **Left 5×2 Grid:** Numbered **`1`–`5`** (top row) and **`6`–`10`** (bottom row), matching **Problems `#1–#10`**. **Rightmost Column:** Top socket **`100`** (for a 10-block Mastery Tower) and bottom **Question Mark in a Circle (`?`)** tutorial keycap badge. |",
        "| **2. Desk Token Bank Box** | Holds 60 tokens | Stores all **60 universal `+10` tokens** in 5 neat layers of 12 (`6×2`) for quick classroom setup and cleanup. |",
        "| **3. 60 Identical `+10` Mastery Tokens** | Universal `+10` blocks | Every token is identical (`+10` on top and all 4 sides):<br>• **1 Block (`+10 pts`)** = Solved with **1st Textbook Way**<br>• **2 Stacked Blocks (`+20 pts DOUBLE`)** = Verified with **2nd Textbook Way**<br>• **10 Blocks (`100 pts`)** = **100-Point Daily Goal** (any 5 problems in 2 Ways OR all 10 in 1 Way)! |",
        "",
        "---",
        "",
    ])

    for ch in chapters:
        ch_num = ch["num"]
        unit_story_pg = 3 + (ch_num - 1) + (ch["sections"][0]["day_num"] - 1) * 2
        story = UNIT_STORIES[ch_num]
        n_ws = len(ch["sections"]) * 2
        unit_pages = 1 + n_ws + 1
        unit_pdf_rel = f"../../downloads/worksheets/bigideas_middle_school_sc6_unit_{ch_num:02d}.pdf"
        book_ref = UNIT_BOOK_REFS.get(ch_num, "[SC-6 Elementary Manual](../manuals/sc6/index.md)")
        prod_links = UNIT_PRODUCT_LINKS.get(ch_num, "[Manipulative Kits](../products/curriculum-and-decks.md)")
        lines.append(f"## Unit {ch_num}: {ch['title']} — {story['story_title']} (p. {unit_story_pg}) {{#unit-{ch_num}}}")
        lines.append("")
        lines.append(f"*{ch['big_ideas_book']} — {ch['subtitle']}*")
        lines.append("")
        lines.append(
            f"<div class=\"hero-buttons\" style=\"margin: 0.75rem 0 1.25rem 0;\">\n"
            f"  <a href=\"{unit_pdf_rel}\" class=\"md-button md-button--primary\">📄 Print Unit {ch_num} Chapter Packet PDF ({unit_pages} Pages: Story Opener + {n_ws} Worksheets + 1-Page Answer Key)</a>\n"
            f"</div>"
        )
        lines.append("")
        lines.append(f"- **Manipulative Kits (`{ch['kit_summary']}`):** {prod_links}")
        lines.append(f"- **Where to Get the Spiral Workbook, Books & Blocks:** [Spiral-Bound Workbook on Lulu ↗](https://www.lulu.com/spotlight/stackcalc) &bull; [Illustrated Book on Amazon ↗](https://link.amazon/B0f5cP0Ur) &bull; [Boxed Block Kits on Etsy ↗](https://stackcalcmath.etsy.com) &bull; [Factory Print on Slant 3D ↗](https://teleportpod.com/portals/profile/StackCalc) &bull; [Free STLs on Printables ↗](https://www.printables.com/@StackCalc_5593834)")
        lines.append(f"- **Aligned *From Blocks to the Stack* Story & Chapter:** {book_ref}")
        lines.append(f"- **Target Misconception:** {ch['coach_misconception']}")
        lines.append(f"- **Hands-On Remediation:** {ch['coach_remediation']}")
        lines.append("")
        for para_txt in story["paragraphs"]:
            lines.append(para_txt)
            lines.append("")

        for sec in ch["sections"]:
            sec_num = sec["sec_num"]
            stitle = clean_section_title(sec_num, sec["title"])
            ped = SECTION_PEDAGOGY[sec_num]
            bm = MULTI_METHOD_BLOCK_NOTES[sec_num]
            story_para = SECTION_STORY_PARAGRAPHS[sec_num]
            check_info = SC6_SECTION_CHECK_GUIDE[sec_num]
            bi_method = ped["big_ideas_method"]
            ex1 = sec["examples"][0]
            ex1_prob_txt = clean_ex1_problem(sec_num, ex1["problem"])
            ex1_ans_txt = clean_ex1_ans(sec_num, ex1["ans"])
            ex2 = ped["ex2"]
            keys1_fmt = " ".join(f"`[{k}]`" for k in ex1["keys"])
            keys2_fmt = " ".join(f"`[{k}]`" for k in ex2["keys"])
            pg_a = 3 + ch["num"] + (sec["day_num"] - 1) * 2
            pg_b = pg_a + 1

            lines.append(f"### Section {sec_num}: {stitle} (Workbook pp. {pg_a}–{pg_b})")
            lines.append("")
            lines.append(f"**Textbook Alignment:** {sec['big_ideas_ref']} (`{sec['ccss']}`) • **Big Ideas Methods:** *{bi_method}* • **Block Kit:** `{sec['kit_id']}` ({sec['kit_name']})")
            lines.append("")
            lines.append(f"**Key Vocabulary:** {ped['key_vocab']}")
            lines.append("")
            lines.append(f"![{stitle}](../assets/manuals/{sec['asset_png']}){{ width=\"320\" }}")
            lines.append("")
            lines.append(sec["concept"])
            lines.append("")
            lines.append(f"> **⚠️ {COMMON_TRAPS[sec_num]}**")
            lines.append("")
            lines.append(f"#### Textbook Concepts & Hands-On Reinforcement (`{sec['kit_id']}`: {sec['kit_name']})")
            lines.append("")
            lines.append(f"1. **{bm['block_m1'].split(':', 1)[0]}:**{bm['block_m1'].split(':', 1)[1]}")
            lines.append(f"2. **{bm['block_m2'].split(':', 1)[0]}:**{bm['block_m2'].split(':', 1)[1]}")
            lines.append(f"3. **{bm['block_compare'].split(':', 1)[0]}:**{bm['block_compare'].split(':', 1)[1]}")
            lines.append("")
            lines.append("#### Authentic Textbook Worked Examples (Learn & Solve by Hand First in 1 Way `+10 pts` or 2 Ways `+20 pts`)")
            lines.append("")
            ex1_ways_col2 = f"**{ped['ex1_m2_title']}:** {ped['ex1_m2_steps']}"
            if ped.get("ex1_m3_title"):
                ex1_ways_col2 += f"<br>**{ped['ex1_m3_title']}:** {ped['ex1_m3_steps']}"
            ex2_ways_col2 = f"**{ex2['m2_title']}:** {ex2['m2_steps']}<br>*{bm['ex2_block_m2']}*"
            if ex2.get("m3_title"):
                ex2_ways_col2 += f"<br>**{ex2['m3_title']}:** {ex2['m3_steps']}"
            lines.append("| Worksheet | Problem | Way 1 | Way 2 (& Way 3 Where Applicable) | Final Answer |")
            lines.append("| :--- | :--- | :--- | :--- | :--- |")
            lines.append(
                f"| **Practice A** (`p.{pg_a}`) | **{ex1_prob_txt}** | **{ped['ex1_m1_title']}:** {ped['ex1_m1_steps']} | {ex1_ways_col2} | **{ex1_ans_txt}** |"
            )
            lines.append(
                f"| **Practice B** (`p.{pg_b}`) | **{ex2['problem']}** | **{ex2['m1_title']}:** {ex2['m1_steps']}<br>*{bm['ex2_block_m1']}* | {ex2_ways_col2} | **{ex2['ans']}** |"
            )
            lines.append("")
            lines.append("#### How to Use the SC-6 Calculator to Check Your Work")
            lines.append("")
            lines.append(f"- **Practice A Work-Check (`p.{pg_a}`):** {check_info['check_a']} *(Worked Example Keystrokes: {keys1_fmt} → **`{ex1_ans_txt}`**)*")
            lines.append(f"- **Practice B Real-Life Work-Check (`p.{pg_b}`):** {check_info['check_b']} *(Worked Example Keystrokes: {keys2_fmt} → **`{ex2['ans']}`**)*")
            lines.append("")
            lines.append(f"#### Practice A (p. {pg_a}): Key Ideas & Multi-Method Practice (10 Exercises)")
            lines.append("")
            lines.append("| # | Problem Prompt | Tutor Setup & SC-6 Check | Final Answer |")
            lines.append("| :---: | :--- | :--- | :--- |")
            for prob in sec["problems"][:10]:
                cprompt = clean_sheet_a_prompt(sec_num, prob["num"], prob["prompt"])
                tstep = format_tutor_solution_step(sec_num, prob)
                lines.append(f"| **A{prob['num']}** | {cprompt} | `{tstep}` | **{prob['ans']}** |")
            lines.append("")
            lines.append(f"#### Practice B (p. {pg_b}): Modeling Real Life & Multi-Method Applications (10 Exercises)")
            lines.append("")
            lines.append(story_para)
            lines.append("")
            lines.append("| # | Modeling Real Life Application Prompt | Tutor Setup & SC-6 Check | Final Answer |")
            lines.append("| :---: | :--- | :--- | :--- |")
            for bprob in SHEET_B_PROBLEMS[sec_num][:10]:
                tstep_b = format_tutor_solution_step(sec_num, bprob)
                lines.append(f"| **B{bprob['num']}** | {bprob['prompt']} | `{tstep_b}` | **{bprob['ans']}** |")
            lines.append("")
            lines.append("---")
            lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] Synchronized curriculum markdown: {md_path} ({len(lines)} lines)")


def main() -> None:
    total_secs = sum(len(ch["sections"]) for ch in CHAPTERS_DATA)
    total_a_probs = sum(len(sec["problems"]) for ch in CHAPTERS_DATA for sec in ch["sections"])
    total_b_probs = sum(len(SHEET_B_PROBLEMS[sec["sec_num"]]) for ch in CHAPTERS_DATA for sec in ch["sections"])
    print(
        f"Loaded {len(CHAPTERS_DATA)} units, {total_secs} sections, "
        f"{total_secs * 2} worksheets, {total_a_probs + total_b_probs} practice problems."
    )
    generate_token_scoring_guide_pdf(CHAPTERS_DATA, SCORING_GUIDE_PDF)
    generate_student_workbook_pdf(CHAPTERS_DATA, STUDENT_PDF)
    generate_coach_guide_pdf(CHAPTERS_DATA, TEACHER_PDF)
    generate_big_ideas_lulu_covers(CHAPTERS_DATA, OUT_DIR)
    generate_chapter_pdfs(CHAPTERS_DATA, OUT_DIR)
    sync_curriculum_markdown(CHAPTERS_DATA, SOURCE_MD)


if __name__ == "__main__":
    main()
