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
    generate_kdp_full_wrap_cover_pdf,
    generate_lulu_coil_cover_pdf,
    get_paper_keycap_png,
)


def clean_manipulative_label(raw: str) -> str:
    """Replaces internal SKU codes with clean pedagogical manipulative names for the three published block kits."""
    replacements = {
        "PLACE-01 + FRAC-01 + PRIME-01": "Place Value, Fraction & Prime Blocks",
        "Place Value Studio (PLACE-01) + Fraction Studio (FRAC-01) + Prime Factor Studio (PRIME-01)": "Place Value, Fraction & Prime Blocks",
        "Place Value Studio (PLACE-01) + Prime Factor Studio (PRIME-01)": "Place Value & Prime Factor Blocks",
        "Fraction Studio (FRAC-01) + Place Value Studio (PLACE-01)": "Fraction Strips & Place Value Blocks",
        "Place Value Studio (PLACE-01) + Fraction Studio (FRAC-01)": "Place Value Blocks & Fraction Strips",
        "PLACE-01 + PRIME-01": "Place Value & Prime Factor Blocks",
        "FRAC-01 + PLACE-01": "Fraction Strips & Place Value Blocks",
        "PLACE-01 + FRAC-01": "Place Value Blocks & Fraction Strips",
        "PRIME-01": "Prime Factor Towers",
        "FRAC-01": "Fraction Strips",
        "PLACE-01": "Place Value Blocks",
        "84mm Fraction Studio": "Fraction Strips",
        "Place Value Studio": "Place Value Blocks",
        "Prime Factor Studio": "Prime Factor Towers",
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
FONT_MATH_SYM = "Courier"
FONT_MATH_SYM_BOLD = "Courier-Bold"

try:
    if (FONT_DIR / "SpaceMono-Regular.ttf").exists():
        pdfmetrics.registerFont(TTFont("SpaceMono", str(FONT_DIR / "SpaceMono-Regular.ttf")))
        pdfmetrics.registerFont(TTFont("SpaceMonoBold", str(FONT_DIR / "SpaceMono-Bold.ttf")))
        FONT_MONO = "SpaceMono"
        FONT_MONO_BOLD = "SpaceMonoBold"
        FONT_MATH_SYM = "SpaceMono"
        FONT_MATH_SYM_BOLD = "SpaceMonoBold"
    arial_dir = Path("/System/Library/Fonts/Supplemental")
    if (arial_dir / "Arial.ttf").exists() and (arial_dir / "Arial Bold.ttf").exists():
        pdfmetrics.registerFont(TTFont("MathSym", str(arial_dir / "Arial.ttf")))
        pdfmetrics.registerFont(TTFont("MathSymBold", str(arial_dir / "Arial Bold.ttf")))
        FONT_MATH_SYM = "MathSym"
        FONT_MATH_SYM_BOLD = "MathSymBold"
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

# Clean Monochrome + Subtle Slate Palette (High-Contrast Print & B&W Photocopy Clarity, Zero Visual Clutter)
INK = "#0F172A"
SLATE = "#334155"
MUTED = "#475569"
BORDER = "#94A3B8"
LIGHT_BORDER = "#CBD5E1"
SUBTLE_HDR = "#F8FAFC"
BAND_HDR = "#E2E8F0"
M1_BG = "#FFFFFF"
M2_BG = "#FFFFFF"
WHITE = "#FFFFFF"
TEAL_ACCENT = "#1E293B"


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
        "<=>": " = ",
        "<->": " = ",
        "↔": " swap ",
        " -> ": " → ",
        "->": "→",
        " <- ": " ← ",
        "<-": "←",
        "▸": "→",
        "yˣ": "y^x",
        "ˣ√y": "x√y",
        "ˣ": "^x",
        "¹⁰": "^10",
        "¹²": "^12",
        "²⁴": "^24",
        "⁻¹": "^(-1)",
        "⁻²": "^(-2)",
        "⁰": "^0",
        "¹": "^1",
        "²": "^2",
        "³": "^3",
        "⁴": "^4",
        "⁵": "^5",
        "⁶": "^6",
        "⁷": "^7",
        "⁸": "^8",
        "⁹": "^9",
        "ⁿ": "^n",
        "ᵗ": "^t",
        "ᵇ": "^b",
        "₁₀": "_10",
        "₁₆": "_16",
        "₀": "_0",
        "₁": "_1",
        "₂": "_2",
        "₃": "_3",
        "₄": "_4",
        "₅": "_5",
        "₆": "_6",
        "₈": "_8",
        "₉": "_9",
        "∛": "^3√",
        "∜": "^4√",
        "½": "1/2",
        "¼": "1/4",
        "¾": "3/4",
        "⅓": "1/3",
        " ~ ": " ≈ ",
        "≟": "=",
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
        " (FRAC-01, 1 Whole = 84 mm)": "",
        "FRAC-01 tray": "fraction tray",
        "PRIME-01 blocks": "prime blocks",
        "PRIME-01 Blocks": "Prime Blocks",
        "Place Value Studio": "Place Value Blocks",
        "Fraction Studio": "Fraction Strips",
        "Prime Factor Studio": "Prime Factor Towers",
        "3x1x7U ": "",
        "84mm ": "",
    }
    for k, v in sku_replacements.items():
        s = s.replace(k, v)
    s = re.sub(
        r"\s*\((?:PRIME-01|FRAC-01|PLACE-01|ALGB-01|BASE-10|DOMI-01)\)",
        "",
        s,
    )
    s = re.sub(
        r"\b(?:PRIME-01|FRAC-01|PLACE-01|ALGB-01|BASE-10|DOMI-01)\s*:?\s*",
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
        if mono and not any(ch in txt for ch in ("Σ", "π", "√")):
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
        has_math_tokens = (
            bool(re.search(r"(?:(?<=[A-Za-z0-9.)\]σπμθ°])\^(?:\([^)]+\)|-?[0-9]+(?:\.[0-9]+)?|[a-zA-Z])|\^[34](?=√))", s))
            or any(sym in s for sym in ("≈", "≤", "≥", "≠"))
            or bool(re.search(r"(?<=[A-Za-z0-9.)\]σπμθ])_[A-Za-z0-9]+(?!_)", s))
        )
        if has_math_tokens:
            return self.math_text(x, y, s, size=size, bold=bold, italic=italic, mono=mono, color=color, align=align, max_w=max_w)
        if max_w is not None:
            actual_w = self.c.stringWidth(s, font, size * mm) / mm
            if actual_w > max_w and actual_w > 0:
                min_sz = max(0.74, size * 0.38)
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

    def math_text(
        self,
        x: float,
        y: float,
        s: str,
        size: float = 3.2,
        bold: bool = False,
        italic: bool = False,
        mono: bool = False,
        color: str = INK,
        align: str = "left",
        max_w: Optional[float] = None,
    ) -> float:
        s_norm = s.replace("²", "^2").replace("³", "^3")
        font = self._pick_font(s_norm, bold, italic, mono)
        sym_font = FONT_MATH_SYM_BOLD if bold else FONT_MATH_SYM
        tokens = re.split(r"((?<=[A-Za-z0-9.)\]σπμθ°])\^\([^)]+\)|(?<=[A-Za-z0-9.)\]σπμθ°])\^(?:-?[0-9]+(?:\.[0-9]+)?|[a-zA-Z])|\^[34](?=√)|(?<=[A-Za-z0-9.)\]σπμθ])_[A-Za-z0-9]+(?!_)|[≈≤≥≠])", s_norm)
        parsed = []
        for tok in tokens:
            if not tok:
                continue
            if tok.startswith("^(") and tok.endswith(")"):
                parsed.append(("sup", tok[2:-1]))
            elif tok.startswith("^"):
                parsed.append(("sup", tok[1:]))
            elif tok.startswith("_"):
                parsed.append(("sub", tok[1:]))
            elif tok in ("≈", "≤", "≥", "≠"):
                parsed.append(("sym", tok))
            else:
                parsed.append(("norm", tok))

        def measure_mm(base_sz: float) -> float:
            tot = 0.0
            for kind, val in parsed:
                if kind in ("sup", "sub"):
                    sz = base_sz * 0.72
                    tot += self.c.stringWidth(val, font, sz * mm) / mm
                elif kind == "sym":
                    sz = base_sz * 0.88
                    tot += self.c.stringWidth(val, sym_font, sz * mm) / mm
                else:
                    tot += self.c.stringWidth(val, font, base_sz * mm) / mm
            return tot

        draw_sz = size
        tot_w = measure_mm(draw_sz)
        if max_w is not None and tot_w > max_w and tot_w > 0:
            min_sz = max(0.74, size * 0.38)
            draw_sz = max(min_sz, size * (max_w / tot_w) * 0.99)
            tot_w = measure_mm(draw_sz)

        self.c.setFillColor(HexColor(color))
        if align == "right":
            cur_x_mm = x - tot_w
        elif align == "center":
            cur_x_mm = x - tot_w / 2.0
        else:
            cur_x_mm = x
        start_x_mm = cur_x_mm
        base_y_pt = (self.h - y) * mm
        for kind, val in parsed:
            if kind == "sup":
                sz = draw_sz * 0.72
                self.c.setFont(font, sz * mm)
                self.c.drawString(cur_x_mm * mm, base_y_pt + (draw_sz * 0.36) * mm, val)
                cur_x_mm += self.c.stringWidth(val, font, sz * mm) / mm
            elif kind == "sub":
                sz = draw_sz * 0.72
                self.c.setFont(font, sz * mm)
                self.c.drawString(cur_x_mm * mm, base_y_pt - (draw_sz * 0.22) * mm, val)
                cur_x_mm += self.c.stringWidth(val, font, sz * mm) / mm
            elif kind == "sym":
                sz = draw_sz * 0.88
                self.c.setFont(sym_font, sz * mm)
                self.c.drawString(cur_x_mm * mm, base_y_pt, val)
                cur_x_mm += self.c.stringWidth(val, sym_font, sz * mm) / mm
            else:
                self.c.setFont(font, draw_sz * mm)
                self.c.drawString(cur_x_mm * mm, base_y_pt, val)
                cur_x_mm += self.c.stringWidth(val, font, draw_sz * mm) / mm
        return cur_x_mm - start_x_mm

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
        """No-op: omit decorative [C] keycap badge on section headers for clean textbook presentation."""
        return 0.0

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
            blocks = [(2, 0.17, "#F1F5F9"), (2, 0.17, "#F1F5F9"), (3, 0.27, "#E2E8F0"), (5, 0.39, "#CBD5E1")]
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
                    fill_c = "#F1F5F9" if pval == 2 else "#E2E8F0"
                    self.rect(cx, cur_y - bh, 7.8, bh, fill=fill_c, stroke=INK, r=0.3, line_w=0.22)
                    self.text(cx + 3.9, cur_y - bh / 2.0 + 0.65, str(pval), size=1.7, bold=True, mono=True, color=INK, align="center")
                    cur_y -= bh
                self.text(cx + 3.9, base_y + 2.0, lbl, size=1.5, bold=True, mono=True, color=INK, align="center")

        elif dtype == "fraction_towers":
            base_y = y + h - 3.1
            max_h = h - 6.6
            bars = [
                ("1", [1.0], "#E2E8F0", x + 2.8),
                ("2/3", [1 / 3, 1 / 3], "#F1F5F9", x + 13.0),
                ("4/6", [1 / 6] * 4, "#CBD5E1", x + 23.2),
                ("7/12", [1 / 3, 1 / 4], "#F8FAFC", x + 33.4),
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
                self.rect(gx0 + i * (ts + gap), y + 5.0, ts, 4.6, fill="#F1F5F9", stroke=INK, r=0.5, line_w=0.25)
                self.text(gx0 + i * (ts + gap) + ts / 2.0, y + 8.0, str(uval), size=1.9, bold=True, mono=True, color=INK, align="center")
            self.text(gx0, y + 12.8, f"Part B ({b} boxes):", size=1.8, bold=True, color=INK)
            for i in range(b):
                self.rect(gx0 + i * (ts + gap), y + 13.9, ts, 4.6, fill="#E2E8F0", stroke=INK, r=0.5, line_w=0.25)
                self.text(gx0 + i * (ts + gap) + ts / 2.0, y + 16.9, str(uval), size=1.9, bold=True, mono=True, color=INK, align="center")
            self.text(x + w / 2.0, y + 21.8, f"M1: {a}:{b} Tape | M2: {a+b} Boxes", size=1.72, bold=True, mono=True, color=TEAL_ACCENT, align="center")

        elif dtype == "percent_bar":
            bw = w - 5.6
            bx = x + 2.8
            by = y + 7.0
            bh = 5.8
            self.rect(bx, by, bw, bh, fill="#F8FAFC", stroke=INK, r=0.6, line_w=0.25)
            self.rect(bx, by, bw * 0.75, bh, fill="#E2E8F0", stroke=INK, r=0.6, line_w=0.25)
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
            self.rect(gx, gy, 9.5, 9.5, fill="#CBD5E1", stroke=INK, r=0.6, line_w=0.25)
            self.text(gx + 4.75, gy + 5.5, "x²", size=2.2, bold=True, mono=True, color=INK, align="center")
            rx = gx + 11.4
            for i in range(3):
                self.rect(rx + i * 4.5, gy, 3.8, 9.5, fill="#E2E8F0", stroke=INK, r=0.4, line_w=0.22)
                self.text(rx + i * 4.5 + 1.9, gy + 5.5, "x", size=1.85, bold=True, mono=True, color=INK, align="center")
            ux = rx + 14.8
            for r in range(2):
                for c in range(2):
                    self.rect(ux + c * 3.8, gy + r * 3.8, 3.2, 3.2, fill="#F8FAFC", stroke=INK, r=0.3, line_w=0.2)
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
                self.polygon(pts, fill="#E2E8F0", stroke=INK, line_w=0.3)
                self.text(x + w / 2.0, y + 20.6, "M1: ½(b×h) | M2: (b÷2)×h", size=1.7, bold=True, mono=True, color=INK, align="center")
            else:
                self.rect(x + 9.5, y + 9.8, 21.0, 9.0, fill="#E2E8F0", stroke=INK, line_w=0.28)
                pts = [(x + 9.5, y + 9.8), (x + 30.5, y + 9.8), (x + 20.0, y + 3.5)]
                self.polygon(pts, fill="#F1F5F9", stroke=INK, line_w=0.28)
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
                self.circle(cx, gy, 2.5, fill="#F8FAFC", stroke=INK, line_w=0.25)
                self.text(cx, gy + 0.8, "+", size=2.0, bold=True, mono=True, color=INK, align="center")
                if i < 3:
                    self.circle(cx, gy + 6.8, 2.5, fill="#E2E8F0", stroke=INK, line_w=0.25)
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
            self.circle(cx + 4.8, cy - 2.6, 0.95, fill=INK, stroke=INK, line_w=0.2)
            self.circle(cx - 4.8, cy - 2.6, 0.95, fill=WHITE, stroke=INK, line_w=0.25)

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
            self.rect(x + 2.2, y + 5.4, pw, 7.8, fill="#F1F5F9", stroke=INK, r=0.6, line_w=0.25)
            self.text(x + 2.2 + pw / 2.0, y + 8.4, "Left Side:", size=1.6, bold=True, color=SLATE, align="center")
            self.text(x + 2.2 + pw / 2.0, y + 11.6, left_lbl, size=1.85, bold=True, mono=True, color=INK, align="center", max_w=pw - 1.5)
            rx = x + w - 2.2 - pw
            self.rect(rx, y + 5.4, pw, 7.8, fill="#E2E8F0", stroke=INK, r=0.6, line_w=0.25)
            self.text(rx + pw / 2.0, y + 8.4, "Right Side:", size=1.6, bold=True, color=SLATE, align="center")
            self.text(rx + pw / 2.0, y + 11.6, right_lbl, size=1.85, bold=True, mono=True, color=INK, align="center", max_w=pw - 1.5)
            self.text(cx, y + 22.0, f"M1/M2: {sol_lbl}", size=1.72, bold=True, mono=True, color=TEAL_ACCENT, align="center", max_w=w - 3.0)

        elif dtype == "solid_3d":
            mode = ddata.get("mode", "net")
            if mode == "net":
                cx = x + 15.8
                cy = y + 8.2
                self.rect(cx, cy, 7.6, 4.5, fill="#E2E8F0", stroke=INK, line_w=0.25)
                self.rect(cx, cy - 3.6, 7.6, 3.6, fill="#F1F5F9", stroke=INK, line_w=0.25)
                self.rect(cx, cy + 4.5, 7.6, 3.6, fill="#F1F5F9", stroke=INK, line_w=0.25)
                self.rect(cx, cy + 8.1, 7.6, 4.5, fill="#E2E8F0", stroke=INK, line_w=0.25)
                self.rect(cx - 4.5, cy, 4.5, 4.5, fill="#CBD5E1", stroke=INK, line_w=0.25)
                self.rect(cx + 7.6, cy, 4.5, 4.5, fill="#CBD5E1", stroke=INK, line_w=0.25)
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
                self.rect(x_q1, by - 3.6, x_q3 - x_q1, 7.2, fill="#E2E8F0", stroke=INK, line_w=0.3)
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
                    self.rect(tx, base_y - th, 4.5, th, fill="#E2E8F0", stroke=INK, r=0.3, line_w=0.22)
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
SECTION_TEKS: Dict[str, str] = {
    "1.1": "TEKS 6.3E",
    "1.2": "TEKS 6.7A",
    "1.3": "TEKS 6.7A",
    "1.4": "TEKS 6.7A",
    "1.5": "TEKS 6.7A",
    "2.1": "TEKS 6.3E",
    "2.2": "TEKS 6.3E",
    "2.3": "TEKS 6.3E",
    "2.4": "TEKS 6.3E",
    "2.5": "TEKS 6.3E",
    "3.1": "TEKS 6.4B",
    "3.2": "TEKS 6.4B, 6.5A",
    "3.3": "TEKS 6.4D, 6.4H",
    "3.4": "TEKS 6.4G, 6.5C",
    "3.5": "TEKS 6.5B",
    "4.1": "TEKS 6.7A",
    "4.2": "TEKS 6.7B",
    "4.3": "TEKS 6.7C, 6.7D",
    "4.4": "TEKS 6.7D",
    "5.1": "TEKS 6.8B, 6.8D",
    "5.2": "TEKS 6.8B, 6.8D",
    "5.3": "TEKS 6.8B, 6.8D",
    "5.4": "TEKS 6.8D",
    "6.1": "TEKS 6.2B",
    "6.2": "TEKS 6.2C, 6.2D",
    "6.3": "TEKS 6.2C, 6.2D",
    "6.4": "TEKS 6.11A",
    "6.5": "TEKS 6.11A",
    "7.1": "TEKS 6.9A",
    "7.2": "TEKS 6.10A",
    "7.3": "TEKS 6.10A",
    "7.4": "TEKS 6.6A, 6.6C",
    "7.5": "TEKS 6.9B, 6.10B",
    "8.1": "TEKS 6.8D",
    "8.2": "TEKS 7.9D",
    "8.3": "TEKS 7.9D",
    "8.4": "TEKS 6.8D, 7.9A",
    "9.1": "TEKS 6.12C",
    "9.2": "TEKS 6.12C",
    "9.3": "TEKS 6.12C, 8.11B",
    "9.4": "TEKS 6.12A, 6.13A",
    "10.1": "TEKS 6.3D",
    "10.2": "TEKS 6.3D",
    "10.3": "TEKS 7.11A",
    "10.4": "TEKS 7.6I",
}

UNIT_QUIZZES_DATA: Dict[int, Dict[str, Any]] = {
    1: {
        "ccss": "CCSS 6.NS.B.2–4, 6.EE.A.1",
        "teks": "TEKS 6.7A",
        "best": "FL MA.6.NSO.2–3",
        "contest": "UIL Number Sense & MathCounts Prime/GCF/LCM",
        "problems": [
            {"num": 1, "tag": "CORE FLUENCY (SEC 1.1)", "prompt": "Find the whole-number quotient and remainder: 1,745 ÷ 16.", "ans": "109 R1"},
            {"num": 2, "tag": "CORE FLUENCY (SEC 1.1)", "prompt": "Evaluate the exact multi-digit quotient: 2,484 ÷ 23.", "ans": "108"},
            {"num": 3, "tag": "CORE FLUENCY (SEC 1.2)", "prompt": "Evaluate the sum of powers: 4³ + 5².", "ans": "89"},
            {"num": 4, "tag": "CORE FLUENCY (SEC 1.3)", "prompt": "Evaluate using order of operations: 60 − 3 × (2³ + 4) ÷ 2.", "ans": "42"},
            {"num": 5, "tag": "CORE FLUENCY (SEC 1.4)", "prompt": "Write the prime factorization of 180 using exponents.", "ans": "2² · 3² · 5"},
            {"num": 6, "tag": "CORE FLUENCY (SEC 1.5)", "prompt": "Find both the GCF and the LCM of 24 and 36.", "ans": "GCF=12, LCM=72"},
            {"num": 7, "tag": "REAL LIFE (SEC 1.5)", "prompt": "A florist has 48 red roses and 64 white roses to make identical bouquets with none left over. What is the greatest number of bouquets she can make, and how many red roses are in each?", "ans": "16 bouquets (3 red)"},
            {"num": 8, "tag": "REAL LIFE (SEC 1.5)", "prompt": "Two airport shuttles leave together. Shuttle A returns every 12 minutes and Shuttle B every 18 minutes. In how many minutes will both shuttles next leave together?", "ans": "36 min"},
            {"num": 9, "tag": "REAL LIFE (SEC 1.3)", "prompt": "A robotics club buys 4 motor kits for $18 each and 3 sensor packs for $12 each, then splits the cost equally among 6 members. How much does each member pay?", "ans": "$18"},
            {"num": 10, "tag": "ERROR ANALYSIS (SEC 1.3)", "prompt": "Alex evaluated 50 − 4 × 2³ by subtracting 50 − 4 = 46 and writing 2³ = 6 to get 46 × 6 = 276. Identify both errors and find the true value.", "ans": "2³=8 & mult first: 18"},
        ],
    },
    2: {
        "ccss": "CCSS 6.NS.A.1, 6.NS.B.3",
        "teks": "TEKS 6.3E",
        "best": "FL MA.6.NSO.2.1–2",
        "contest": "UIL Number Sense & Calculator Fractions/Decimals",
        "problems": [
            {"num": 1, "tag": "CORE FLUENCY (SEC 2.1)", "prompt": "Multiply and write in simplest form: (3/4) × (8/9).", "ans": "2/3"},
            {"num": 2, "tag": "CORE FLUENCY (SEC 2.1)", "prompt": "Multiply the mixed numbers: 2 1/4 × 1 1/3.", "ans": "3"},
            {"num": 3, "tag": "CORE FLUENCY (SEC 2.2)", "prompt": "Divide and write in simplest form: (5/6) ÷ (5/12).", "ans": "2"},
            {"num": 4, "tag": "CORE FLUENCY (SEC 2.3)", "prompt": "Divide the mixed numbers: 3 3/4 ÷ 1 1/4.", "ans": "3"},
            {"num": 5, "tag": "CORE FLUENCY (SEC 2.4)", "prompt": "Evaluate the decimal expression: 24.8 + 7.65 − 9.4.", "ans": "23.05"},
            {"num": 6, "tag": "CORE FLUENCY (SEC 2.5)", "prompt": "Multiply and divide: (a) 4.5 × 0.24   (b) 15.6 ÷ 0.6.", "ans": "(a) 1.08  (b) 26"},
            {"num": 7, "tag": "REAL LIFE (SEC 2.2)", "prompt": "A carpenter has a cedar board 7/8 meter long and cuts it into pieces each 1/16 meter long. How many pieces does she get?", "ans": "14 pieces"},
            {"num": 8, "tag": "REAL LIFE (SEC 2.5)", "prompt": "Trail mix costs $4.80 per pound. How much does 2.25 pounds of trail mix cost?", "ans": "$10.80"},
            {"num": 9, "tag": "REAL LIFE (SEC 2.3)", "prompt": "A 6 1/2-quart jug of sports drink is poured equally into 1/2-quart bottles. How many bottles are filled?", "ans": "13 bottles"},
            {"num": 10, "tag": "ERROR ANALYSIS (SEC 2.2)", "prompt": "To solve (2/3) ÷ (1/6), Maya flipped the first fraction and multiplied (3/2) × (1/6) = 1/4. Explain her error and find the true quotient.", "ans": "Flip divisor (6/1): 4"},
        ],
    },
    3: {
        "ccss": "CCSS 6.RP.A.1–3",
        "teks": "TEKS 6.4B–H, 6.5B",
        "best": "FL MA.6.AR.3.1–5",
        "contest": "MathCounts & TMSCA Ratios, Rates & Percents",
        "problems": [
            {"num": 1, "tag": "CORE FLUENCY (SEC 3.1)", "prompt": "Write the ratio 18 : 24 in simplest form and find an equivalent ratio with second term 40.", "ans": "3 : 4 and 30 : 40"},
            {"num": 2, "tag": "CORE FLUENCY (SEC 3.2)", "prompt": "In a ratio table, if 4 laps take 10 minutes, how many minutes do 14 laps take at the same rate?", "ans": "35 min"},
            {"num": 3, "tag": "CORE FLUENCY (SEC 3.3)", "prompt": "Find the unit rate in miles per gallon: 270 miles driven on 12 gallons of gas.", "ans": "22.5 mpg"},
            {"num": 4, "tag": "CORE FLUENCY (SEC 3.4)", "prompt": "Write the fraction 3/8 as an exact decimal and as a percent.", "ans": "0.375 and 37.5%"},
            {"num": 5, "tag": "CORE FLUENCY (SEC 3.5)", "prompt": "Find 35% of 80.", "ans": "28"},
            {"num": 6, "tag": "CORE FLUENCY (SEC 3.5)", "prompt": "18 is 24% of what number?", "ans": "75"},
            {"num": 7, "tag": "REAL LIFE (SEC 3.1)", "prompt": "Bronze alloy is mixed in a copper-to-tin ratio of 5 : 2. If a batch has 35 kg of total alloy, how many kilograms of copper are in the batch?", "ans": "25 kg"},
            {"num": 8, "tag": "REAL LIFE (SEC 3.3)", "prompt": "Store A sells 5 avocados for $6.25. Store B sells 8 avocados for $9.60. Which store has the lower unit price, and what is that price?", "ans": "Store B ($1.20)"},
            {"num": 9, "tag": "REAL LIFE (SEC 3.5)", "prompt": "A $60 backpack is on sale for 25% off. What is the sale price before tax?", "ans": "$45"},
            {"num": 10, "tag": "ERROR ANALYSIS (SEC 3.1)", "prompt": "In a club with 12 boys and 18 girls, Leo says the ratio of boys to the whole club is 12 : 18 = 2 : 3. Explain the mistake and write the true ratio.", "ans": "Whole is 30 -> 2 : 5"},
        ],
    },
    4: {
        "ccss": "CCSS 6.EE.A.2–4",
        "teks": "TEKS 6.7A–D",
        "best": "FL MA.6.AR.1.1–4",
        "contest": "MathCounts & UIL Algebraic Evaluation & Factoring",
        "problems": [
            {"num": 1, "tag": "CORE FLUENCY (SEC 4.1)", "prompt": "Evaluate 3x² − 4y when x = 4 and y = 5.", "ans": "28"},
            {"num": 2, "tag": "CORE FLUENCY (SEC 4.2)", "prompt": "Write an algebraic expression for: '8 less than the product of 5 and n.'", "ans": "5n − 8"},
            {"num": 3, "tag": "CORE FLUENCY (SEC 4.3)", "prompt": "Combine like terms to simplify: 7x + 9 + 4x − 3.", "ans": "11x + 6"},
            {"num": 4, "tag": "CORE FLUENCY (SEC 4.4)", "prompt": "Use the Distributive Property to expand: 6(3x + 4).", "ans": "18x + 24"},
            {"num": 5, "tag": "CORE FLUENCY (SEC 4.4)", "prompt": "Simplify by expanding and combining like terms: 4(2x + 3) + 5x.", "ans": "13x + 12"},
            {"num": 6, "tag": "CORE FLUENCY (SEC 4.4)", "prompt": "Factor the expression completely using the GCF: 24x + 36.", "ans": "12(2x + 3)"},
            {"num": 7, "tag": "REAL LIFE (SEC 4.1)", "prompt": "The surface area of a cube with edge length s is 6s². Find the surface area when s = 5 cm.", "ans": "150 cm²"},
            {"num": 8, "tag": "REAL LIFE (SEC 4.2)", "prompt": "Museum admission costs $12 plus $4 per planetarium show s. Write an expression and find the total cost for 3 shows.", "ans": "12 + 4s; $24"},
            {"num": 9, "tag": "REAL LIFE (SEC 4.4)", "prompt": "A rectangular garden has width 5 meters and length (2x + 7) meters. Write an expanded expression for its area.", "ans": "10x + 35"},
            {"num": 10, "tag": "ERROR ANALYSIS (SEC 4.4)", "prompt": "Noah simplified 5(2x + 3) as 10x + 3, and then combined 10x + 3 = 13x. Identify both algebraic errors and write the true simplified expression.", "ans": "5·3=15; keep 10x + 15"},
        ],
    },
    5: {
        "ccss": "CCSS 6.G.A.1",
        "teks": "TEKS 6.8B–D",
        "best": "FL MA.6.GR.2.1–2",
        "contest": "UIL Calculator Applications & MathCounts 2D Geometry",
        "problems": [
            {"num": 1, "tag": "CORE FLUENCY (SEC 5.1)", "prompt": "Find the area of a parallelogram with base b = 15 cm and perpendicular height h = 8 cm.", "ans": "120 cm²"},
            {"num": 2, "tag": "CORE FLUENCY (SEC 5.2)", "prompt": "Find the area of a triangle with base b = 18 m and height h = 11 m.", "ans": "99 m²"},
            {"num": 3, "tag": "CORE FLUENCY (SEC 5.3)", "prompt": "Find the area of a trapezoid with parallel bases b₁ = 9 in., b₂ = 15 in., and height h = 7 in.", "ans": "84 in²"},
            {"num": 4, "tag": "CORE FLUENCY (SEC 5.2)", "prompt": "A triangle has an area of 60 ft² and a base of 15 ft. What is its perpendicular height h?", "ans": "8 ft"},
            {"num": 5, "tag": "CORE FLUENCY (SEC 5.4)", "prompt": "Find the total area of an L-shaped deck composed of a 10 ft by 8 ft rectangle and a 6 ft by 4 ft rectangle.", "ans": "104 ft²"},
            {"num": 6, "tag": "CORE FLUENCY (SEC 5.4)", "prompt": "A train departs at 1:45 PM and arrives at 4:20 PM. What is the elapsed travel time in hours and minutes?", "ans": "2 hr 35 min"},
            {"num": 7, "tag": "REAL LIFE (SEC 5.2)", "prompt": "A triangular sailboat sail has base 12 ft and height 25 ft. If sailcloth costs $4 per square foot, how much does the cloth cost?", "ans": "$600 (150 ft²)"},
            {"num": 8, "tag": "REAL LIFE (SEC 5.3)", "prompt": "A trapezoidal courtyard has parallel sides of 20 m and 28 m and a width (height) of 10 m. How many square meters of pavers are needed?", "ans": "240 m²"},
            {"num": 9, "tag": "REAL LIFE (SEC 5.4)", "prompt": "A rectangular wall is 14 ft wide and 9 ft tall with a 3 ft by 4 ft window. Find the painted wall area excluding the window.", "ans": "114 ft²"},
            {"num": 10, "tag": "ERROR ANALYSIS (SEC 5.1)", "prompt": "A parallelogram has base 12 cm, slant side 10 cm, and perpendicular height 8 cm. Chloe multiplied 12 × 10 = 120 cm². Explain her error and find the true area.", "ans": "Use perp h=8: 96 cm²"},
        ],
    },
    6: {
        "ccss": "CCSS 6.NS.C.5–8",
        "teks": "TEKS 6.2B–D, 6.11A",
        "best": "FL MA.6.NSO.1.1–4, MA.6.GR.1",
        "contest": "UIL & MathCounts Signed Rationals & Coordinate Geometry",
        "problems": [
            {"num": 1, "tag": "CORE FLUENCY (SEC 6.1)", "prompt": "Write the opposite of −14 and evaluate |−14| + |−5|.", "ans": "14; 19"},
            {"num": 2, "tag": "CORE FLUENCY (SEC 6.2)", "prompt": "Order the integers from least to greatest: −3, 4, −8, 0, −1.", "ans": "−8, −3, −1, 0, 4"},
            {"num": 3, "tag": "CORE FLUENCY (SEC 6.3)", "prompt": "Compare using <, >, or =:  (a) −3/4 ___ −1/2    (b) −1.8 ___ −1.25.", "ans": "(a) <   (b) <"},
            {"num": 4, "tag": "CORE FLUENCY (SEC 6.4)", "prompt": "Identify the quadrant of point P(−6, 5) and write the coordinates of its reflection across the x-axis.", "ans": "Quad II; (−6, −5)"},
            {"num": 5, "tag": "CORE FLUENCY (SEC 6.5)", "prompt": "Find the distance between A(−4, 3) and B(7, 3) on the coordinate plane.", "ans": "11 units"},
            {"num": 6, "tag": "CORE FLUENCY (SEC 6.5)", "prompt": "Find the perimeter of a rectangle with vertices (−3, 2), (5, 2), (5, −4), and (−3, −4).", "ans": "28 units"},
            {"num": 7, "tag": "REAL LIFE (SEC 6.2)", "prompt": "A research submarine is at −240 m and a diving bell is at −185 m. Which vessel is deeper, and by how many meters?", "ans": "Submarine by 55 m"},
            {"num": 8, "tag": "REAL LIFE (SEC 6.1)", "prompt": "The morning temperature in Fairbanks was −16°F. By afternoon it reached 0°F. How many degrees did the temperature change?", "ans": "16°F"},
            {"num": 9, "tag": "REAL LIFE (SEC 6.5)", "prompt": "On a town grid where 1 unit = 1 block, the library is at (−5, −2) and the park is at (−5, 6). How many blocks apart are they?", "ans": "8 blocks"},
            {"num": 10, "tag": "ERROR ANALYSIS (SEC 6.2)", "prompt": "Sam claims that −12 > −5 because 12 is greater than 5. Use a number line to explain why Sam is incorrect and write the true inequality.", "ans": "−12 is left of −5; −12 < −5"},
        ],
    },
    7: {
        "ccss": "CCSS 6.EE.B.5–8, 6.EE.C.9",
        "teks": "TEKS 6.9A–C, 6.10A",
        "best": "FL MA.6.AR.2.1–4",
        "contest": "MathCounts & TMSCA Equations & Inequalities",
        "problems": [
            {"num": 1, "tag": "CORE FLUENCY (SEC 7.1)", "prompt": "Write an equation and solve: 'A number x decreased by 17 equals 29.'", "ans": "x − 17 = 29; x = 46"},
            {"num": 2, "tag": "CORE FLUENCY (SEC 7.2)", "prompt": "Solve the addition equation: x + 18.5 = 42.", "ans": "x = 23.5"},
            {"num": 3, "tag": "CORE FLUENCY (SEC 7.3)", "prompt": "Solve the multiplication equation: 8x = 136.", "ans": "x = 17"},
            {"num": 4, "tag": "CORE FLUENCY (SEC 7.3)", "prompt": "Solve the division equation: x / 6 = 14.", "ans": "x = 84"},
            {"num": 5, "tag": "CORE FLUENCY (SEC 7.4)", "prompt": "A train travels at 65 mph for t hours, covering d miles. Write an equation relating d and t, and find d when t = 4.", "ans": "d = 65t; 260 mi"},
            {"num": 6, "tag": "CORE FLUENCY (SEC 7.5)", "prompt": "Tell whether x = 6 is a solution of 3x − 4 ≥ 14, and state whether the number line graph of x ≥ 6 has an open or closed circle.", "ans": "Yes (14≥14); closed circle"},
            {"num": 7, "tag": "REAL LIFE (SEC 7.2)", "prompt": "After spending $28 on a hoodie, Elena has $37 left. Write and solve an equation to find how much money m she had at first.", "ans": "m − 28 = 37; $65"},
            {"num": 8, "tag": "REAL LIFE (SEC 7.3)", "prompt": "Three-fourths of the students in a band play wind instruments. If 27 play wind instruments, how many students n are in the band?", "ans": "(3/4)n = 27; 36"},
            {"num": 9, "tag": "REAL LIFE (SEC 7.5)", "prompt": "An elevator has a maximum weight limit of 1,800 lb. Write an inequality for the allowed weight w and tell whether w = 1,800 lb is allowed.", "ans": "w ≤ 1,800; Yes"},
            {"num": 10, "tag": "ERROR ANALYSIS (SEC 7.3)", "prompt": "To solve x / 4 = 12, Jordan divided 12 by 4 and wrote x = 3. Explain the inverse-operation mistake and find the true solution.", "ans": "Multiply 12 × 4: x = 48"},
        ],
    },
    8: {
        "ccss": "CCSS 6.G.A.2, 6.G.A.4",
        "teks": "TEKS 6.8D, 7.9A, 7.9D",
        "best": "FL MA.6.GR.2.3–4",
        "contest": "UIL Calculator Applications 3D Solids, Surface Area & Volume",
        "problems": [
            {"num": 1, "tag": "CORE FLUENCY (SEC 8.1)", "prompt": "How many faces, edges, and vertices does a rectangular prism have?", "ans": "6 faces, 12 edges, 8 vertices"},
            {"num": 2, "tag": "CORE FLUENCY (SEC 8.2)", "prompt": "Find the total surface area of a rectangular prism with length 8 cm, width 5 cm, and height 4 cm.", "ans": "184 cm²"},
            {"num": 3, "tag": "CORE FLUENCY (SEC 8.2)", "prompt": "Find the total surface area of a cube with edge length 6 in.", "ans": "216 in²"},
            {"num": 4, "tag": "CORE FLUENCY (SEC 8.3)", "prompt": "A square pyramid has a 10 m by 10 m base and four triangular lateral faces each with slant height 12 m. Find its total surface area.", "ans": "340 m²"},
            {"num": 5, "tag": "CORE FLUENCY (SEC 8.4)", "prompt": "Find the volume of a rectangular prism with length 9 ft, width 4.5 ft, and height 6 ft.", "ans": "243 ft³"},
            {"num": 6, "tag": "CORE FLUENCY (SEC 8.4)", "prompt": "How many 1/2-inch cubes are needed to completely fill a rectangular box measuring 3 in. by 2 in. by 1 1/2 in.?", "ans": "72 cubes (Vol = 9 in³)"},
            {"num": 7, "tag": "REAL LIFE (SEC 8.2)", "prompt": "A gift box is 10 in. long, 6 in. wide, and 5 in. tall. How many square inches of wrapping paper are needed to cover all 6 faces with no overlap?", "ans": "280 in²"},
            {"num": 8, "tag": "REAL LIFE (SEC 8.4)", "prompt": "A rectangular aquarium holds 360,000 cm³ of water. If its base is 100 cm long and 60 cm wide, what is the water depth h?", "ans": "60 cm"},
            {"num": 9, "tag": "REAL LIFE (SEC 8.3)", "prompt": "A triangular prism tent has two triangular ends (base 6 ft, height 4 ft) and three 6 ft by 8 ft rectangular sides (including the floor). Find the total surface area.", "ans": "168 ft²"},
            {"num": 10, "tag": "ERROR ANALYSIS (SEC 8.2)", "prompt": "Liam found the surface area of a 5 cm by 4 cm by 3 cm prism by multiplying 5 × 4 × 3 = 60 cm². Explain what he actually found and compute the true surface area.", "ans": "60 is Vol; SA = 94 cm²"},
        ],
    },
    9: {
        "ccss": "CCSS 6.SP.A.1–3, 6.SP.B.4–5",
        "teks": "TEKS 6.12A–D, 6.13A",
        "best": "FL MA.6.DP.1.1–6",
        "contest": "MathCounts & TMSCA Data Analysis, Mean, Median, IQR & MAD",
        "problems": [
            {"num": 1, "tag": "CORE FLUENCY (SEC 9.1)", "prompt": "Find the mean, median, and mode of the quiz scores: 14, 18, 20, 18, 25.", "ans": "Mean=19, Med=18, Mode=18"},
            {"num": 2, "tag": "CORE FLUENCY (SEC 9.2)", "prompt": "Find the median and range of the ordered dataset: 8, 12, 15, 19, 22, 26.", "ans": "Median = 17, Range = 18"},
            {"num": 3, "tag": "CORE FLUENCY (SEC 9.3)", "prompt": "For the ordered data 4, 6, 8, 10, 12, 16, 20, find Q₁, the median, Q₃, and the interquartile range (IQR).", "ans": "Q₁=6, Med=10, Q₃=16, IQR=10"},
            {"num": 4, "tag": "CORE FLUENCY (SEC 9.3)", "prompt": "Compute the Mean Absolute Deviation (MAD) of the dataset: 6, 8, 10, 16.", "ans": "Mean = 10, MAD = 3"},
            {"num": 5, "tag": "CORE FLUENCY (SEC 9.4)", "prompt": "A box plot has minimum 12, Q₁ = 18, median = 24, Q₃ = 31, and maximum 40. What percent of the data lies between 18 and 31, and what is the IQR?", "ans": "50%; IQR = 13"},
            {"num": 6, "tag": "CORE FLUENCY (SEC 9.1)", "prompt": "After 4 games, Mia's mean score is 15 points. How many points must she score in Game 5 to raise her 5-game mean to 17?", "ans": "25 points"},
            {"num": 7, "tag": "REAL LIFE (SEC 9.2)", "prompt": "Five house prices on a block (in $1,000s) are 220, 230, 240, 250, and 960. Find the mean and median, and state which better represents a typical house.", "ans": "Mean=380, Med=240 (Median)"},
            {"num": 8, "tag": "REAL LIFE (SEC 9.3)", "prompt": "Battery life tests (in hours) for Brand A have IQR = 1.5 hr and Brand B have IQR = 4.8 hr. Which brand is more consistent?", "ans": "Brand A (smaller IQR)"},
            {"num": 9, "tag": "REAL LIFE (SEC 9.4)", "prompt": "In a histogram of 40 hikers, 12 hiked 0–2 mi, 18 hiked 3–5 mi, and 10 hiked 6–8 mi. What percent of hikers walked 3 miles or more?", "ans": "70% (28 / 40)"},
            {"num": 10, "tag": "ERROR ANALYSIS (SEC 9.2)", "prompt": "To find the median of 15, 8, 22, 10, 19, Ben picked the middle number as written and said 22. Explain his error and find the true median.", "ans": "Sort first (8,10,15,19,22): 15"},
        ],
    },
    10: {
        "ccss": "CCSS 7.NS.A, 7.EE.B.4, 7.SP.C",
        "teks": "TEKS 6.3D, 7.11A, 7.6I",
        "best": "FL MA.7.NSO.2, MA.7.AR.2, MA.7.DP.2",
        "contest": "MathCounts & UIL Signed Arithmetic, 2-Step Equations & Probability",
        "problems": [
            {"num": 1, "tag": "CORE FLUENCY (SEC 10.1)", "prompt": "Evaluate the signed expressions: (a) −9 + 14    (b) −6 − (−15).", "ans": "(a) 5   (b) 9"},
            {"num": 2, "tag": "CORE FLUENCY (SEC 10.2)", "prompt": "Evaluate the signed products and powers: (a) (−7) × (−8)    (b) (−5)².", "ans": "(a) 56   (b) 25"},
            {"num": 3, "tag": "CORE FLUENCY (SEC 10.2)", "prompt": "Evaluate using order of operations: (−48) ÷ 6 + (−3) × (−4).", "ans": "4"},
            {"num": 4, "tag": "CORE FLUENCY (SEC 10.3)", "prompt": "Solve the two-step equation: 3x − 7 = 20.", "ans": "x = 9"},
            {"num": 5, "tag": "CORE FLUENCY (SEC 10.3)", "prompt": "Solve the two-step equation: (x / 4) + 5 = 11.", "ans": "x = 24"},
            {"num": 6, "tag": "CORE FLUENCY (SEC 10.4)", "prompt": "A bag holds 5 red, 3 blue, and 4 green marbles. Find the probability of drawing a blue marble in simplest form.", "ans": "1/4"},
            {"num": 7, "tag": "REAL LIFE (SEC 10.1)", "prompt": "A scuba diver starts at −18 meters, descends 12 meters, and then ascends 9 meters. What is the diver's final elevation?", "ans": "−21 m"},
            {"num": 8, "tag": "REAL LIFE (SEC 10.3)", "prompt": "A kayak rental costs a $15 safety fee plus $12 per hour h. If a family paid $63 total, how many hours did they rent the kayak?", "ans": "4 hours"},
            {"num": 9, "tag": "REAL LIFE (SEC 10.4)", "prompt": "You flip a fair coin and roll a standard 6-sided die. What is the compound probability of getting Heads AND a number greater than 4?", "ans": "1/6"},
            {"num": 10, "tag": "ERROR ANALYSIS (SEC 10.3)", "prompt": "To solve 2x + 6 = 18, Ava divided 18 by 2 first to get x + 6 = 9, then subtracted 6 to get x = 3. Check x = 3 and solve correctly.", "ans": "2(3)+6=12≠18; x = 6"},
        ],
    },
}


def draw_student_cover_page(p: CanvasPage, chapters: List[Dict[str, Any]]) -> None:
    margin = 12.0
    uw = p.w - 2 * margin

    p.text(
        margin,
        14.0,
        "STACKCALC LEARNING LAB  •  GRADES 6–8 TWO-METHOD MASTERY WORKBOOK (90 WORKSHEETS • 900 PROBLEMS)",
        size=2.45,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
    )
    p.text(margin, 21.8, "Middle School Math Lab: Two-Method Block & SC-6 Workbook", size=5.2, bold=True, color=INK)
    p.text(
        margin,
        27.2,
        "45 Core Sections × 2 Full Practice Sheets (Practice A: Key Ideas + Practice B: Real Life) • Works with Homeschool & School Curricula",
        size=2.60,
        color=SLATE,
    )
    p.line(margin, 29.8, margin + uw, 29.8, color=INK, width=0.5)

    cw = (uw - 6.0) / 3.0
    cards = [
        (
            "1. SELF-CONTAINED PAPER MASTERY",
            "Every worksheet teaches the core vocabulary, visual model, and two paper-and-pencil solution methods—compatible with Saxon, Singapore, AoPS, and Big Ideas Math.",
        ),
        (
            "2. TWO WAYS = DOUBLE POINTS (+20)",
            "Every Worked Example models TWO ways to solve on paper: Method 1 (+10 pts) and Method 2 (+20 pts DOUBLE), reinforced by tactile blocks and distraction-free SC-6 check.",
        ),
        (
            "3. 5 IN 2 WAYS OR 10 IN 1 WAY",
            "Students can earn 100 points by solving ANY 5 problems in 2 Ways (+20 each)—building twice the understanding without tedious drill—or all 10 problems in 1 Way (+10 each)!",
        ),
    ]
    for i, (ctitle, cbody) in enumerate(cards):
        cx = margin + i * (cw + 3.0)
        p.rect(cx, 32.2, cw, 25.2, fill=WHITE, stroke=INK, r=1.2, line_w=0.3)
        p.rect(cx, 32.2, cw, 5.4, fill=BAND_HDR, stroke=INK, r=0.8, line_w=0.25)
        p.text(cx + 2.5, 35.9, ctitle, size=1.95, bold=True, mono=True, color=INK)
        if i == 1:
            p.draw_tutorial_keycap(cx + cw - 6.2, 32.8, w=4.6, h=4.0)
        p.para(cx + 2.5, 40.8, cbody, max_w=cw - 5.0, size=2.22, color=INK, leading=1.24)

    p.rect(margin, 59.8, uw, 30.8, fill=SUBTLE_HDR, stroke=BORDER, r=1.2, line_w=0.25)
    p.text(
        margin + 3.0,
        64.0,
        "HANDS-ON MANIPULATIVES REINFORCE TEXTBOOK CONCEPTS & TWO-METHOD MASTERY (+10 / +20 RUBRIC)",
        size=2.12,
        bold=True,
        mono=True,
        color=INK,
    )
    p.draw_tutorial_keycap(margin + uw - 7.6, 60.6, w=4.6, h=4.0)
    showcase = [
        ("place_value_regrouping.png", "Place Value Regrouping"),
        ("prime_studio_commutativity.png", "Prime Factor Blocks"),
        ("prime_lcm_gcd_venn.png", "Prime Factor Towers"),
        ("fraction_studio_common_denominator.png", "Fraction Strips"),
        ("fraction_studio_twin_comparator.png", "Fraction Comparator"),
    ]
    sw_w = (uw - 10.0) / 5.0
    for idx, (png_name, cap) in enumerate(showcase):
        sx = margin + 2.0 + idx * sw_w
        p.rect(sx + 1.0, 65.8, sw_w - 2.0, 19.2, fill=WHITE, stroke=LIGHT_BORDER, r=0.8, line_w=0.2)
        p.image(ASSETS_MANUALS_DIR / png_name, sx + 2.0, 66.6, sw_w - 4.0, 17.6)
        p.text(sx + sw_w / 2.0, 88.4, cap, size=1.95, bold=True, color=SLATE, align="center")

    ty = 93.6
    p.rect(margin, ty, uw, 6.0, fill=BAND_HDR, stroke=INK, line_w=0.3)
    p.text(margin + 2.5, ty + 4.1, "UNIT / TOPIC & CURRICULUM ALIGNMENT", size=2.05, bold=True, mono=True, color=INK)
    p.text(margin + 71.5, ty + 4.1, "SECTIONS & WORKSHEETS (PRACTICE A & B)", size=2.05, bold=True, mono=True, color=INK)
    p.text(margin + 143.5, ty + 4.1, "TWO-METHOD DOUBLE POINTS FOCUS", size=2.0, bold=True, mono=True, color=INK)

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
        p.text(margin + 143.5, ry + 5.0, m_sum, size=1.85, bold=True, color=INK, max_w=46.0)
        p.text(margin + 143.5, ry + 9.4, f"Model: {clean_tools.split('&')[0].strip()}", size=1.78, mono=True, color=SLATE, max_w=46.0)
        p.text(margin + 143.5, ry + 13.7, f"[ ] {len(ch['sections'])*2} Sheets + Unit Quiz (p.{111 + ch['num']})", size=1.78, bold=True, color=TEAL_ACCENT, max_w=46.0)

    p.text(
        margin,
        p.h - 8.2,
        "StackCalc Learning Systems  •  Big Ideas Math Middle School Supplement (Two-Method Guide p.2 • 90 Worksheets • 10 Unit Quizzes pp.112–121)",
        size=1.92,
        mono=True,
        color=MUTED,
        max_w=uw - 28.0,
    )
    p.text(margin + uw, p.h - 8.2, "Page 1 of 123", size=2.0, bold=True, mono=True, color=INK, align="right")


def draw_token_scoring_guide_page(p: CanvasPage, chapters: List[Dict[str, Any]], page_label: str = "Page 2 of 123") -> None:
    """Renders the 1-Page Two-Method Mastery Scoring & SC-6 Work-Check Guide."""
    margin = 11.0
    uw = p.w - 2 * margin

    # 1. Top Header (y = 9.0 .. 24.8 mm)
    p.text(
        margin,
        12.2,
        "STACKCALC LEARNING LAB  •  TWO-METHOD MASTERY RUBRIC & SC-6 WORK-CHECK PROTOCOL",
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
        "Two-Method Mastery Scoring & SC-6 Work-Check Guide",
        size=4.2,
        bold=True,
        color=INK,
        max_w=uw,
    )
    p.text(
        margin,
        23.2,
        "How to Solve by Hand First, Earn +10 Single-Method or +20 Double Credit, and Verify Your Work on the SC-6",
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
            BAND_HDR,
            "Study the Worked Example first. Solve a problem by hand in the left column of your workspace using your 1st Textbook Way, and check off [x] +10 (1 Way) at the bottom of the box.",
        ),
        (
            "STEP 2: 2ND WAY (+20 PTS)",
            BAND_HDR,
            "Solve the SAME problem a 2nd independent way in the right column (using the 2nd Textbook Way, a visual model, or one of the 3 block kits). When both ways agree, check off [x] +20 (2 Ways)!",
        ),
        (
            "STEP 3: CHECK ON SC-6",
            BAND_HDR,
            "Never guess! Use the section's 'Check Your Work on the SC-6 Calculator' box to verify your hand-written answer—using Two-Dot fractions ([.] n [.] d), [≠] equality tests, and [f][LINE] mode.",
        ),
        (
            "STEP 4: 100-PT DAILY GOAL",
            BAND_HDR,
            "Reach your 100-Point Daily Goal by solving any 5 problems in 2 Ways (5 × 20 = 100 pts), all 10 problems in 1 Way (10 × 10 = 100 pts), or any mix that totals 100 points on the page!",
        ),
    ]

    for s_idx, (stitle, shdr_col, sbody) in enumerate(step_cards):
        sx = margin + s_idx * (col_w + 2.5)
        p.rect(sx, step_y, col_w, step_h, fill=WHITE, stroke=INK, r=0.9, line_w=0.28)
        p.rect(sx, step_y, col_w, 4.4, fill=shdr_col, stroke=INK, r=0.7, line_w=0.22)
        p.text(sx + 2.0, step_y + 3.1, stitle, size=1.72, bold=True, mono=True, color=INK, max_w=col_w - 4.0)

        # Mini graphic box inside each step card (y = 31.6 .. 44.6 mm)
        gy = step_y + 5.4
        gh = 13.0
        p.rect(sx + 2.0, gy, col_w - 4.0, gh, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.6, line_w=0.2)
        gcx = sx + col_w / 2.0

        if s_idx == 0:
            # Paper Checkoff [x] +10 (1 Way)
            p.rect(gcx - 16.5, gy + 2.8, 13.0, 7.4, fill=WHITE, stroke=INK, r=0.45, line_w=0.24)
            p.text(gcx - 10.0, gy + 6.0, "Way 1", size=1.45, bold=True, mono=True, color=SLATE, align="center")
            p.text(gcx - 10.0, gy + 9.0, "[x] +10", size=1.65, bold=True, mono=True, color=INK, align="center")
            p.text(gcx + 8.0, gy + 5.8, "1st Method =", size=1.60, bold=True, color=SLATE, align="center")
            p.text(gcx + 8.0, gy + 9.2, "+10 PTS", size=2.1, bold=True, mono=True, color=INK, align="center")
        elif s_idx == 1:
            # Two-Column Paper Verification = +20 DOUBLE!
            p.rect(gcx - 17.5, gy + 2.8, 7.2, 7.4, fill=WHITE, stroke=INK, r=0.4, line_w=0.22)
            p.text(gcx - 13.9, gy + 7.2, "W1", size=1.45, bold=True, mono=True, color=INK, align="center")
            p.rect(gcx - 9.5, gy + 2.8, 7.2, 7.4, fill="#E2E8F0", stroke=TEAL_ACCENT, r=0.4, line_w=0.24)
            p.text(gcx - 5.9, gy + 7.2, "W2", size=1.45, bold=True, mono=True, color=TEAL_ACCENT, align="center")
            p.text(gcx + 8.5, gy + 5.6, "2 Methods =", size=1.60, bold=True, color=TEAL_ACCENT, align="center")
            p.text(gcx + 8.5, gy + 9.0, "+20 PTS!", size=2.1, bold=True, mono=True, color=TEAL_ACCENT, align="center")
        elif s_idx == 2:
            # SC-6 2-Line LCD + Keycaps
            p.rect(sx + 3.5, gy + 1.4, col_w - 7.0, 6.0, fill="#E2E8F0", stroke=INK, r=0.4, line_w=0.22)
            p.text(sx + 5.0, gy + 3.9, "Y: 5 (Quotient)", size=1.42, bold=True, mono=True, color=SLATE)
            p.text(sx + 5.0, gy + 6.4, "X: 3 (Remainder)", size=1.42, bold=True, mono=True, color=TEAL_ACCENT)
            p.draw_keycap_sequence(["23", "ENTER", "4", "g", "÷R"], sx + 4.2, gy + 8.4, max_w=col_w - 8.4, h=3.2, gap=0.5)
        else:
            # 100-Point Worksheet Mastery Badge
            p.rect(gcx - 15.5, gy + 2.6, 13.0, 7.8, fill="#E2E8F0", stroke=INK, r=0.5, line_w=0.26)
            p.text(gcx - 9.0, gy + 6.2, "100 / 100", size=1.55, bold=True, mono=True, color=INK, align="center")
            p.text(gcx - 9.0, gy + 9.2, "MASTERY", size=1.25, bold=True, mono=True, color=TEAL_ACCENT, align="center")
            p.text(gcx + 8.0, gy + 5.6, "5×20 or 10×10", size=1.48, bold=True, color=SLATE, align="center")
            p.text(gcx + 8.0, gy + 9.0, "100 PTS!", size=2.1, bold=True, mono=True, color=INK, align="center")

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

    # 3. Middle Split: Two-Method Mastery Grid (Left) & Three Flexible Paths to 100 Points (Right) (y = 70.0 .. 144.0 mm)
    mid_y = 70.0
    mid_h = 74.0
    left_w = 102.0
    right_w = uw - left_w - 2.5
    right_x = margin + left_w + 2.5

    # --- Left Panel: 10-Problem Mastery Grid Schematic + 3 Published Block Kit Photos ---
    p.rect(margin, mid_y, left_w, mid_h, fill=WHITE, stroke=INK, r=1.0, line_w=0.3)
    p.rect(margin, mid_y, left_w, 4.6, fill=BAND_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(
        margin + 2.5,
        mid_y + 3.2,
        "HOW TWO-METHOD (+10 / +20) WORKSHEET SCORING WORKS",
        size=1.80,
        bold=True,
        mono=True,
        color=INK,
        max_w=left_w - 9.0,
    )

    # Top-Down Vector Diagram of 10-Problem Checkoff Grid
    lid_x = margin + 2.5
    lid_y = mid_y + 6.2
    lid_w = 60.0
    lid_h = 24.5
    p.rect(lid_x, lid_y, lid_w, lid_h, fill=SUBTLE_HDR, stroke=INK, r=1.2, line_w=0.32)
    p.text(lid_x + lid_w / 2.0, lid_y + 2.9, "SAMPLE 10-PROBLEM WORKSHEET SCORE (#1–#10 = 100 PTS)", size=1.38, bold=True, mono=True, color=INK, align="center")

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
                s_fill = "#E2E8F0" if ntok == 2 else WHITE
                s_stroke = INK if ntok == 2 else BORDER
                p.rect(cell_x, cell_y, sock_w, sock_h, fill=s_fill, stroke=s_stroke, r=0.5, line_w=0.22)
                p.text(cell_x + sock_w / 2.0, cell_y + 3.2, f"#{q_num}", size=1.45, bold=True, mono=True, color=INK, align="center")
                if ntok == 2:
                    p.rect(cell_x + 1.0, cell_y + 4.1, sock_w - 2.0, 3.4, fill=WHITE, stroke=INK, r=0.3, line_w=0.18)
                    p.text(cell_x + sock_w / 2.0, cell_y + 6.5, "+20", size=1.35, bold=True, mono=True, color=INK, align="center")
                else:
                    p.text(cell_x + sock_w / 2.0, cell_y + 6.5, "10/20", size=1.18, mono=True, color=MUTED, align="center")
            else:
                if r_i == 0:
                    # Top-right [100] Mastery Goal Box
                    p.rect(cell_x, cell_y, sock_w, sock_h, fill="#E2E8F0", stroke=INK, r=0.5, line_w=0.28)
                    p.text(cell_x + sock_w / 2.0, cell_y + 3.4, "100", size=1.65, bold=True, mono=True, color=INK, align="center")
                    p.text(cell_x + sock_w / 2.0, cell_y + 6.6, "GOAL", size=1.15, bold=True, mono=True, color=SLATE, align="center")
                else:
                    # Bottom-right SC-6 Check Badge
                    p.rect(cell_x, cell_y, sock_w, sock_h, fill=WHITE, stroke=TEAL_ACCENT, r=0.5, line_w=0.24)
                    p.text(cell_x + sock_w / 2.0, cell_y + 3.6, "SC-6", size=1.35, bold=True, mono=True, color=TEAL_ACCENT, align="center")
                    p.text(cell_x + sock_w / 2.0, cell_y + 6.6, "CHECK", size=1.10, bold=True, mono=True, color=INK, align="center")

    # Callout descriptions to the right of the Tracker Diagram
    call_x = lid_x + lid_w + 2.2
    call_w = left_w - lid_w - 6.8
    callouts = [
        ("Problems #1–#10:", "Check off +10 for solving in 1st Way; check off +20 for verifying in a 2nd Way."),
        ("100-Point Goal:", "Reach 100 points by solving any 5 problems in 2 Ways OR all 10 in 1 Way."),
        ("SC-6 Verification:", "After solving on paper, use the SC-6 Work-Check box to confirm every answer."),
    ]
    cy_call = lid_y + 1.8
    for c_head, c_desc in callouts:
        p.text(call_x, cy_call, c_head, size=1.55, bold=True, color=TEAL_ACCENT, max_w=call_w)
        cy_call = p.para(call_x, cy_call + 2.1, c_desc, max_w=call_w, size=1.45, color=INK, leading=1.12, max_lines=3)
        cy_call += 1.0

    # Bottom half of Left Panel: 3 Published Manipulative Block Photos
    photos = [
        ("place_value_regrouping.png", "1. Place Value Blocks (PLACE-01)"),
        ("prime_lcm_gcd_venn.png", "2. Prime Factor Towers (PRIME-01)"),
        ("fraction_studio_common_denominator.png", "3. Fraction Strips (FRAC-01)"),
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
    p.rect(right_x, mid_y, right_w, 4.6, fill=BAND_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(
        right_x + 2.5,
        mid_y + 3.2,
        "3 FLEXIBLE PATHS TO THE 100-POINT DAILY GOAL",
        size=1.80,
        bold=True,
        mono=True,
        color=INK,
        max_w=right_w - 5.0,
    )

    paths = [
        (
            "PATH A: DEEP MASTERY — ANY 5 PROBLEMS IN 2 WAYS = 100 PTS",
            "5 Problems × 2 Ways (+20 pts each) = 100 Points",
            "Best when a 10-problem page feels overwhelming! Pick any 5 problems (for example: Warm-Ups #1-#2, Core #3-#4, and Challenge #9), solve each using BOTH Textbook Ways, and verify on your SC-6. You do half as many problems, but understand them twice as deeply!",
            M2_BG,
            TEAL_ACCENT,
            TEAL_ACCENT,
        ),
        (
            "PATH B: FULL SHEET — ALL 10 PROBLEMS IN 1 WAY = 100 PTS",
            "10 Problems × 1 Way (+10 pts each) = 100 Points",
            "Best for building speed and accuracy across every problem type on the worksheet. Solve all 10 problems (#1-#10) using your favorite Textbook Way, check off [x] +10 on each card, and verify every answer on your SC-6.",
            M1_BG,
            BORDER,
            INK,
        ),
        (
            "PATH C: MIX & MATCH — ANY COMBINATION TOTALLING 100 PTS",
            "Example: 3 Problems in 2 Ways (60 pts) + 4 Problems in 1 Way (40 pts) = 100 Points",
            "Students and teachers can customize the assignment! Combine 2-Way (+20) and 1-Way (+10) solutions in any order to reach 100 points. Want an Honors Extension? Solve all 10 problems in 2 Ways for 200/100 Extra Credit!",
            SUBTLE_HDR,
            INK,
            INK,
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
    p.rect(margin, tbl_y, uw, 4.6, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.25)
    p.text(
        margin + 2.4,
        tbl_y + 3.2,
        "MASTER SC-6 CALCULATOR WORK-CHECK CHEAT SHEET (UNITS 1–10: SOLVE BY HAND FIRST, THEN VERIFY!)",
        size=1.80,
        bold=True,
        mono=True,
        color=INK,
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

    # 5. Bottom Tracker: 45-Section 100-Point Mastery Tower Log (y = 233.0 .. 266.5 mm, height = 33.5 mm)
    bot_y = 233.0
    bot_h = 33.5
    p.rect(margin, bot_y, uw, bot_h, fill=WHITE, stroke=INK, r=0.9, line_w=0.28)
    p.rect(margin, bot_y, uw, 4.5, fill=SUBTLE_HDR, stroke=INK, r=0.7, line_w=0.22)
    p.text(
        margin + 2.4,
        bot_y + 3.1,
        "45-SECTION 100-POINT MASTERY PROGRESS LOG (CHECK OFF EACH SECTION AS YOU EARN 100 POINTS ON PRACTICE A & B!)",
        size=1.74,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=uw - 10.0,
    )
    p.draw_tutorial_keycap(margin + uw - 5.5, bot_y + 0.45, w=4.0, h=3.5)

    # 2 Columns × 5 Rows of Units inside the bottom log
    u_col_w = (uw - 6.0) / 2.0
    u_row_h = 5.4
    for idx, ch in enumerate(chapters):
        uc = idx // 5
        ur = idx % 5
        ux = margin + 2.2 + uc * (u_col_w + 1.6)
        uy = bot_y + 5.6 + ur * u_row_h
        p.rect(ux, uy, u_col_w, u_row_h - 0.5, fill=SUBTLE_HDR if ur % 2 == 0 else WHITE, stroke=LIGHT_BORDER, r=0.4, line_w=0.16)
        p.text(ux + 1.4, uy + 3.3, f"Unit {ch['num']}:", size=1.58, bold=True, color=INK)
        sec_checks = "   ".join(f"[ ] {s['sec_num']}" for s in ch["sections"])
        p.text(ux + 16.5, uy + 3.3, sec_checks, size=1.58, bold=True, mono=True, color=TEAL_ACCENT, max_w=u_col_w - 18.0)

    p.text(
        margin,
        p.h - 8.2,
        "StackCalc SC-6 Textbook Supplement  •  Two-Method Mastery Scoring & SC-6 Work-Check Guide",
        size=1.88,
        mono=True,
        color=MUTED,
        max_w=uw - 28.0,
    )
    p.text(margin + uw, p.h - 8.2, page_label, size=1.88, bold=True, mono=True, color=INK, align="right")


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
    u_quiz_meta = UNIT_QUIZZES_DATA[ch_num]
    p.text(
        margin,
        12.2,
        f"UNIT {ch_num} INTRODUCTION  •  {ch['big_ideas_book'].upper()} ({u_quiz_meta['ccss']} • {u_quiz_meta['teks']})",
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

    # Bottom ribbon inside story box: Real-World Mathematical Context & Hands-On Models
    p.rect(margin + 2.0, box_y + box_h - 5.8, uw - 4.0, 4.8, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.6, line_w=0.18)
    p.text(
        margin + 3.6,
        box_y + box_h - 2.5,
        f"Real-World Mathematical Context & Two-Method Mastery  •  Hands-On Models: {clean_tools}",
        size=1.55,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=uw - 7.2,
    )

    # 3. Unit Lesson & SC-6 Work-Check Directory (y = 126.5 .. 268.2 mm)
    hdr_y = 126.5
    p.rect(margin, hdr_y, uw, 5.0, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.25)
    p.text(
        margin + 2.6,
        hdr_y + 3.4,
        f"UNIT {ch_num} LESSONS — LEARN TWO TEXTBOOK WAYS FIRST, THEN CHECK YOUR WORK ON THE SC-6 CALCULATOR",
        size=1.84,
        bold=True,
        mono=True,
        color=INK,
        max_w=uw - 10.0,
    )
    p.draw_tutorial_keycap(margin + uw - 5.6, hdr_y + 0.65, w=4.2, h=3.6)

    secs = ch["sections"]
    n_secs = len(secs)
    cards_y0 = 132.8
    avail_h = 266.2 - cards_y0
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
        p.rect(margin + 1.8, cy + 0.65, 25.0, 3.5, fill=BAND_HDR, stroke=INK, r=0.5, line_w=0.2)
        p.text(
            margin + 14.3,
            cy + 3.0,
            f"SEC {snum} (pp.{pg_a}-{pg_b})",
            size=1.62,
            bold=True,
            mono=True,
            color=INK,
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
            size=1.95,
            color=INK,
            leading=1.18,
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
            size=1.80,
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
            size=1.82,
            color=SLATE,
            leading=1.16,
            max_lines=3,
        )

    p.text(
        margin,
        p.h - 8.2,
        f"StackCalc SC-6 Textbook Supplement  •  Unit {ch_num}: {ch['title']}",
        size=1.88,
        mono=True,
        color=MUTED,
        max_w=uw - 28.0,
    )
    p.text(margin + uw, p.h - 8.2, f"Page {page_num} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")


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
    p.rect(x, y, w, h, fill=SUBTLE_HDR, stroke=INK, r=0.85, line_w=0.28)
    p.rect(x, y, w, 3.7, fill=BAND_HDR, stroke=INK, r=0.65, line_w=0.22)
    p.text(
        x + 2.5,
        y + 2.65,
        f"CHECK YOUR WORK ON THE SC-6 CALCULATOR — {sheet_label} (SOLVE BY HAND FIRST, THEN VERIFY!)",
        size=1.74,
        bold=True,
        mono=True,
        color=INK,
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
    teks_lbl = SECTION_TEKS.get(sec_num, "TEKS 6.7A")
    p.text(
        margin,
        12.2,
        f"{ped['unit_name'].upper()}  •  {sec['big_ideas_ref'].upper()} ({sec['ccss']} • {teks_lbl})",
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
        max_w=101.0,
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
    p.rect(margin, band_y, left_w, 4.5, fill=BAND_HDR, stroke=INK, r=0.8, line_w=0.25)
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
        color=INK,
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
        (bm["block_m2"], True, SLATE),
        (trap_txt, True, INK),
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
    p.rect(right_x, band_y, right_w, 4.5, fill=BAND_HDR, stroke=INK, r=0.8, line_w=0.25)
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
            (ped["ex1_m3_title"], ped["ex1_m3_steps"], SUBTLE_HDR, INK, INK, SLATE),
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
    p.rect(margin, hdr_y, uw, 4.4, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.25)
    p.text(
        margin + 2.5,
        hdr_y + 3.1,
        f"SECTION {sec_num} PRACTICE A — KEY IDEAS & MULTI-METHOD PRACTICE",
        size=1.84,
        bold=True,
        mono=True,
        color=INK,
        max_w=105.0,
    )
    p.text(
        margin + uw - 2.5,
        hdr_y + 3.1,
        "100-PT GOAL: Any 5 in 2 Ways (+20) OR All 10 in 1 Way (+10)!",
        size=1.70,
        bold=True,
        mono=True,
        color=SLATE,
        align="right",
        max_w=86.0,
    )

    grid_y0 = 99.1
    col_w = (uw - 3.0) / 2.0
    row_h = 32.5
    row_gap = 1.05

    probs = sec["problems"]
    for idx, prob in enumerate(probs[:10]):
        r = idx // 2
        c = idx % 2
        px = margin + c * (col_w + 3.0)
        py = grid_y0 + r * (row_h + row_gap)

        p.rect(px, py, col_w, row_h, fill=WHITE, stroke=SLATE, r=0.9, line_w=0.28)

        p_num = prob["num"]
        p.rect(px + 2.0, py + 1.8, 5.0, 4.4, fill=BAND_HDR, stroke=INK, r=0.65, line_w=0.22)
        p.text(px + 4.5, py + 4.8, str(p_num), size=2.15, bold=True, mono=True, color=INK, align="center")

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
        p.h - 8.2,
        f"StackCalc SC-6 Textbook Supplement  •  {ped['unit_name']} — Section {sec_num} Practice A ({sec['big_ideas_ref']})",
        size=1.88,
        mono=True,
        color=MUTED,
        max_w=uw - 28.0,
    )
    p.text(margin + uw, p.h - 8.2, f"Page {page_num} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")


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
    teks_lbl = SECTION_TEKS.get(sec_num, "TEKS 6.7A")
    p.text(
        margin,
        12.2,
        f"{ped['unit_name'].upper()}  •  {sec['big_ideas_ref'].upper()} ({sec['ccss']} • {teks_lbl}) — MODELING REAL LIFE",
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
        max_w=101.0,
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
    p.rect(margin, band_y, uw, 4.4, fill=BAND_HDR, stroke=INK, r=0.8, line_w=0.25)
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
            (ex2["m3_title"], ex2["m3_steps"], SUBTLE_HDR, INK, INK, SLATE),
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
            m_box_y + 3.1,
            ex2["m1_title"],
            size=1.80,
            bold=True,
            color=INK,
            max_w=half_w - 3.2,
        )
        p.para(
            margin + 3.8,
            m_box_y + 6.0,
            ex2["m1_steps"],
            max_w=half_w - 3.2,
            size=1.78,
            color=SLATE,
            leading=1.16,
            max_lines=5,
        )

        m2_x = margin + 4.6 + half_w
        p.rect(m2_x, m_box_y, half_w, m_box_h, fill=M2_BG, stroke=TEAL_ACCENT, r=0.7, line_w=0.24)
        p.text(
            m2_x + 1.6,
            m_box_y + 3.1,
            ex2["m2_title"],
            size=1.80,
            bold=True,
            color=TEAL_ACCENT,
            max_w=half_w - 3.2,
        )
        after_m2 = p.para(
            m2_x + 1.6,
            m_box_y + 6.0,
            ex2["m2_steps"],
            max_w=half_w - 3.2,
            size=1.78,
            color=INK,
            leading=1.15,
            max_lines=3,
        )
        if ex2.get("block_step"):
            p.para(
                m2_x + 1.6,
                max(after_m2 + 0.4, m_box_y + 12.6),
                ex2["block_step"],
                max_w=half_w - 3.2,
                size=1.68,
                italic=True,
                color=TEAL_ACCENT,
                leading=1.12,
                max_lines=2,
            )

    # Bottom Bar: Common Trap Alert (left) + Final Answer (right)
    ky = band_y + 31.3
    ex2_ans_txt = ex2["ans"]
    ans_b_w = min(82.0, max(44.0, (len(ex2_ans_txt) + 8) * 1.18))
    ans_b_sz = 1.72 if len(ex2_ans_txt) > 44 else 1.88
    trap_b_txt = COMMON_TRAPS.get(sec_num, ex2.get("block_step", bm["ex2_block_m1"]))
    p.para(
        margin + 2.6,
        ky + 1.9,
        trap_b_txt,
        max_w=uw - ans_b_w - 6.0,
        size=1.50,
        bold=True,
        color=SLATE,
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
    p.rect(margin, hdr_y, uw, 4.4, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.25)
    p.text(
        margin + 2.5,
        hdr_y + 3.1,
        f"SECTION {sec_num} PRACTICE B — MODELING REAL LIFE & APPLICATIONS",
        size=1.84,
        bold=True,
        mono=True,
        color=INK,
        max_w=105.0,
    )
    p.text(
        margin + uw - 2.5,
        hdr_y + 3.1,
        "100-PT GOAL: Any 5 in 2 Ways (+20) OR All 10 in 1 Way (+10)!",
        size=1.70,
        bold=True,
        mono=True,
        color=SLATE,
        align="right",
        max_w=86.0,
    )

    grid_y0 = 99.1
    col_w = (uw - 3.0) / 2.0
    row_h = 32.5
    row_gap = 1.05

    for idx, prob in enumerate(b_probs[:10]):
        r = idx // 2
        c = idx % 2
        px = margin + c * (col_w + 3.0)
        py = grid_y0 + r * (row_h + row_gap)

        p.rect(px, py, col_w, row_h, fill=WHITE, stroke=SLATE, r=0.9, line_w=0.28)

        p_num = prob["num"]
        p.rect(px + 2.0, py + 1.8, 5.0, 4.4, fill=BAND_HDR, stroke=INK, r=0.65, line_w=0.22)
        p.text(px + 4.5, py + 4.8, str(p_num), size=2.15, bold=True, mono=True, color=INK, align="center")

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
        p.h - 8.2,
        f"StackCalc SC-6 Textbook Supplement  •  {ped['unit_name']} — Section {sec_num} Practice B ({sec['big_ideas_ref']})",
        size=1.88,
        mono=True,
        color=MUTED,
        max_w=uw - 28.0,
    )
    p.text(margin + uw, p.h - 8.2, f"Page {page_num} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")


def draw_workbook_front_matter(c: canvas.Canvas, chapters: List[Dict[str, Any]], is_coach: bool = False) -> None:
    """
    Renders the traditional 4-page book opening sequence matching From Blocks to the Stack and Thinking in the Stack:
      - Page i (Recto, unnumbered display page): Full Title Page with bottom StackCalc imprint.
      - Page ii (Verso, folio 'ii'): Series Frontispiece + Copyright, State Standards Alignment & Colophon.
      - Page iii (Recto, folio 'iii'): Table of Contents (before the Preface).
      - Page iv (Verso, folio 'iv'): Preface (Motivation, Why No [=] Key, 3 Published Block Kits & Ecosystem Overview).
    """
    margin = 16.0
    uw = (letter[0] / mm) - 2 * margin
    left_x = 30.0
    right_x = (letter[0] / mm) - 30.0
    content_w = right_x - left_x
    doc_footer = (
        "MIDDLE SCHOOL MATH LAB • TEACHER & PARENT COACH GUIDE"
        if is_coach
        else "MIDDLE SCHOOL MATH LAB • STUDENT PRACTICE WORKBOOK"
    )

    # =========================================================
    # PAGE i (RECTO): FULL TITLE PAGE (UNNUMBERED DISPLAY PAGE)
    # =========================================================
    p = CanvasPage(c, letter)
    series_kicker = (
        "THE STACKCALC LIBRARY  •  CURRICULUM SERIES — BOOK 3 COACH GUIDE"
        if is_coach
        else "THE STACKCALC LIBRARY  •  CURRICULUM SERIES — BOOK 3 OF 5"
    )
    p.text(left_x, 54.0, series_kicker, size=2.35, bold=True, mono=True, color=INK)

    if is_coach:
        p.text(left_x, 68.0, "MIDDLE SCHOOL", size=9.2, bold=True, color=INK)
        p.text(left_x, 80.5, "COACH GUIDE", size=9.2, bold=True, color=INK)
        subtitle = "10-Unit Teacher & Homeschool Parent Facilitation Guide, Misconception Diagnostics & Complete 900-Problem Worked Keys"
        desc_body = (
            "A self-contained, open-and-go middle school coaching companion for Grades 6–8 connecting universal middle school topics "
            "(compatible with Saxon 7/6 & 8/7, Singapore Dimensions 6–8, AoPS Prealgebra, Math Mammoth, Big Ideas Math, and Common Core/TEKS) "
            "with our three physical block kits—Place Value Studio (PLACE-01), Fraction Studio (FRAC-01), and Prime Factor Studio (PRIME-01)—"
            "two-method paper problem solving, and distraction-free verification on the four-line StackCalc SC-6 calculator."
        )
    else:
        p.text(left_x, 68.0, "MIDDLE SCHOOL", size=9.2, bold=True, color=INK)
        p.text(left_x, 80.5, "MATH LAB", size=9.2, bold=True, color=INK)
        subtitle = "Two-Method Student Practice Workbook with Physical Blocks, Real-World Stories & Four-Line Stack Verification"
        desc_body = (
            "A self-contained Grades 6–8 practice workbook (10 Units, 45 Sections, 90 Practice A & B Worksheets, and 900 "
            "problems) for homeschooling families and classrooms. Teaches students to solve every concept by hand on paper in two "
            "independent ways, model quantities with our three physical block kits—Place Value Studio (PLACE-01), Fraction Studio "
            "(FRAC-01), and Prime Factor Studio (PRIME-01)—and verify their paper work on the distraction-free StackCalc SC-6 calculator."
        )

    p.line(left_x, 88.0, right_x, 88.0, color=INK, width=0.65)
    sub_end_y = p.para(left_x, 96.5, subtitle, max_w=content_w, size=3.35, bold=True, color=INK, leading=1.25)
    p.para(left_x, sub_end_y + 3.5, desc_body, max_w=content_w, size=2.30, color=SLATE, leading=1.36)

    imprint_rule_y = p.h - 52.0
    p.line(left_x, imprint_rule_y, right_x, imprint_rule_y, color=BORDER, width=0.30)
    p.text(left_x, imprint_rule_y + 7.5, "StackCalc", size=3.8, bold=True, color=INK)
    p.text(left_x, imprint_rule_y + 13.0, "stackcalc.io", size=2.45, color=SLATE)
    p.text(left_x, imprint_rule_y + 18.0, "First Edition", size=2.45, color=SLATE)
    c.showPage()

    # =========================================================
    # PAGE ii (VERSO): SERIES FRONTISPIECE & COPYRIGHT COLOPHON
    # =========================================================
    p = CanvasPage(c, letter)
    p.text(left_x, 28.0, "BOOKS, BLOCKS & INSTRUMENTS IN THE STACKCALC LIBRARY", size=2.25, bold=True, mono=True, color=INK)
    p.line(left_x, 31.5, right_x, 31.5, color=INK, width=0.40)

    library_entries = [
        (
            "Illustrated Companion Trade Books (History of Mathematics & Stack Thinking)",
            "• Volume I — From Blocks to the Stack: How Hands-On Blocks Make Numbers Click (Grades K–6 / StackCalc SC-6)\n"
            "• Volume II — Thinking in the Stack: The Art of Solving Equations from the Inside Out (Grades 7–12, AP & Engineers / StackCalc SC-32)",
        ),
        (
            "K–12 Concept-First Curriculum & Student Workbooks (US Letter 8.5\" × 11\" Editions)",
            "• Book 1 — Teaching with the Stack: Unified K–12 Master Teacher & Homeschool Guide, Lessons & Complete Answer Keys\n"
            "• Book 2A & 2B — Early Elementary (K–2) & Upper Elementary (3–5) Math Labs: Student Manipulative & Stack Workbooks\n"
            "• Book 3 — Middle School Math Lab: Grades 6–8 Two-Method Student Practice Workbook (900 Problems • ISBN 979-8-16-653215-2)\n"
            "• Book 4 — High School & STEM Lab: Grades 9–12 & AP Scientific RPN & Engineering Student Workbook\n"
            "• Book 5 — Stack Speed & Fluency: 15 Speed Lessons, Shortcut Playbooks & 180 Progressive Practice Tests (3,690 Problems)",
        ),
        (
            "Three Published Physical Manipulative Block Studios & Four-Line Stack Calculators (stackcalc.io)",
            "• Place Value Studio (PLACE-01): 6×2 Whole & Decimal Trays, Digit Blocks (0–9) & Stackable Gold [+1] Carry Tokens\n"
            "• Fraction Studio (FRAC-01): 84.0 mm Proportional Fraction Towers (1 Whole to 1/12) & 12-Socket Comparator Lid\n"
            "• Prime Factor Studio (PRIME-01): Logarithmic Prime Blocks (2, 3, 5, 7 where equal products stand flush) & GCF/LCM Comparator\n"
            "• StackCalc Calculators: SC-6 Elementary/Middle School Calculator & SC-32 Scientific Calculator (Distraction-Free Hardware)",
        ),
    ]
    ly = 37.5
    for lib_head, lib_body in library_entries:
        p.text(left_x, ly, lib_head, size=2.05, bold=True, color=INK, max_w=content_w)
        ly = p.para(left_x, ly + 4.2, lib_body, max_w=content_w, size=1.88, color=INK, leading=1.26) + 2.8

    p.line(left_x, 128.0, right_x, 128.0, color=INK, width=0.40)
    p.text(left_x, 134.5, "COPYRIGHT, CURRICULUM ALIGNMENT & OPEN-EDUCATION LICENSE", size=2.25, bold=True, mono=True, color=INK)

    colophon_blocks = [
        (
            f"MIDDLE SCHOOL MATH LAB: {subtitle}",
            "Copyright © 2026 by StackCalc (https://stackcalc.io). Some rights reserved. Published by StackCalc Learning Lab, San Francisco, California. ISBN-13: 979-8-16-653215-2 (9798166532152) • First Edition (US Letter 8.50 × 11.00 in / 215.9 × 279.4 mm).",
        ),
        (
            "Homeschool & Classroom Curriculum Compatibility:",
            "Covers the 10 universal middle school mathematics domains (Grades 6–8). Works seamlessly alongside homeschool curricula (Saxon Math 7/6 & 8/7, Singapore Dimensions 6–8, Math Mammoth, RightStart, and AoPS Prealgebra) and state-mandated school textbooks (Big Ideas Math®, Illustrative Mathematics®, Eureka Math®, enVision®, Common Core CCSS & Texas TEKS).",
        ),
        (
            "Open-Education License (CC BY-NC-SA 4.0) & Perpetual Family/Classroom Reproduction Permission:",
            "Homeschool families, classroom teachers, math coaches, interventionists, and schools are expressly permitted to photocopy or print unlimited copies of all 90 Practice A & B worksheets, the 1-Page Scoring Guide, and the 10 Chapter Packets for non-commercial educational instruction.",
        ),
        (
            "Regulatory & Physical Safety Notice (Reese's Law / P.L. 117-171 / 16 CFR Part 1263 & ASTM F963):",
            "Physical calculator instruments that utilize coin or button cell batteries must maintain a captive, tool-secured battery compartment compliant with UL 4200A. 3D-printed manipulative blocks constitute small parts under 16 CFR Part 1501; adult supervision is required for children under 6 years of age.",
        ),
        (
            "Trademark Notice & Print Colophon:",
            "StackCalc, SC-32, and SC-6 are trademarks of StackCalc. Big Ideas Math® is a trademark of Larson Texts, Inc., which does not sponsor or endorse this independent publication. Typeset in Computer Modern Unicode (CMU Serif), SpaceMono, and STIX Math in high-contrast monochrome ink on archival white paper.",
        ),
    ]
    cy = 141.5
    for c_head, c_body in colophon_blocks:
        p.text(left_x, cy, c_head, size=1.95, bold=True, color=INK, max_w=content_w)
        cy = p.para(left_x, cy + 4.0, c_body, max_w=content_w, size=1.82, color=SLATE, leading=1.22) + 2.8

    p.line(margin, p.h - 12.2, margin + uw, p.h - 12.2, color=BORDER, width=0.25)
    p.text(margin, p.h - 8.2, f"THE STACKCALC LIBRARY  •  {doc_footer}", size=1.88, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 8.2, "ii", size=2.1, bold=True, mono=True, color=INK, align="right")
    c.showPage()

    # =========================================================
    # PAGE iii (RECTO): TABLE OF CONTENTS (BEFORE THE PREFACE)
    # =========================================================
    p = CanvasPage(c, letter)
    p.text(
        margin,
        12.2,
        "TABLE OF CONTENTS  •  COMPLETE UNIT, SECTION & APPENDIX DIRECTORY",
        size=1.95,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
    )
    p.text(margin, 18.2, "Table of Contents", size=4.2, bold=True, color=INK, max_w=uw)
    p.line(margin, 21.5, margin + uw, 21.5, color=INK, width=0.45)

    p.rect(margin, 24.5, uw, 5.5, fill=BAND_HDR, stroke=INK, r=0.6, line_w=0.25)
    p.text(margin + 2.5, 28.3, "Section / Unit & Mathematical Topic", size=1.95, bold=True, color=INK)
    p.text(margin + 86.0, 28.3, "Sections & Standards", size=1.95, bold=True, color=INK)
    p.text(margin + 123.0, 28.3, "Hands-On Models & Focus", size=1.95, bold=True, color=INK)
    p.text(margin + uw - 2.5, 28.3, "Pages", size=1.95, bold=True, color=INK, align="right")

    toc_entries = []
    if is_coach:
        toc_entries.append((
            "Preface: Why Two Paper Methods + Blocks + Stack Work",
            "Parents & Teachers",
            "Paper-First Mastery, Homeschool & School Fit",
            "p. iv",
        ))
        for ch in chapters:
            ch_num = ch["num"]
            secs = ch["sections"]
            sec_range = f"Sec {secs[0]['sec_num']}–{secs[-1]['sec_num']} ({secs[0]['ccss'].split(',')[0]})"
            toc_entries.append((
                f"Unit {ch_num:02d}: {ch['title']} (180 Solutions)",
                sec_range,
                clean_manipulative_label(ch["kit_summary"]),
                f"p. {ch_num}",
            ))
        toc_entries.extend([
            ("Appendix A: 10-Unit Diagnostic Misconception Matrix", "All 10 Units", "Target Classroom Errors & Block Remediations", "p. 11"),
            ("Appendix B: Photocopiable Student Mastery Roster", "Class Tracker", "10-Unit Progress Grid & Observation Notes", "p. 12"),
        ])
    else:
        toc_entries.extend([
            ("Preface: Why Two Paper Methods + Blocks + Stack Work", "Students & Families", "Paper First, 3 Block Kits & Quick-Start", "p. iv"),
            ("Master 10-Unit & 45-Section Progress Index", "All 45 Sections", "Daily Section & Score Check-Off Directory", "p. 1"),
            ("100-Point Two-Method Scoring & SC-6 Check Guide", "Scoring Rules", "+10 (1 Way) vs. +20 (2 Ways) & Stack Check", "p. 2"),
        ])
        for ch in chapters:
            ch_num = ch["num"]
            secs = ch["sections"]
            u_start = 3 + (ch_num - 1) + (secs[0]["day_num"] - 1) * 2
            u_end = 3 + ch_num + (secs[-1]["day_num"] - 1) * 2 + 1
            sec_range = f"Sec {secs[0]['sec_num']}–{secs[-1]['sec_num']} + Quiz p.{111 + ch_num}"
            toc_entries.append((
                f"Unit {ch_num:02d}: {ch['title']}",
                sec_range,
                clean_manipulative_label(ch["kit_summary"]),
                f"pp. {u_start}–{u_end}",
            ))
        toc_entries.extend([
            ("Appendix A: Middle School Math Formulas & Benchmarks", "Units 1–10", "Formulas, Conversions & Fraction Benchmarks", "p. 103"),
            ("Appendix B: Complete SC-6 Keycap & Two-Dot Guide", "SC-6 Reference", "4-Level Stack (T, Z, Y, X) & Exact Fractions", "p. 104"),
            ("Appendix C: Hands-On Manipulative & Visual Modeling Guide", "All 10 Units", "How to Model Textbook Concepts with the 3 Block Kits", "p. 105"),
            ("Appendix D: Mastery Certificate & Dot-Grid Scratchpad", "Certificate & Grid", "100-Point Mastery Certificate & Graph Workspace", "p. 106"),
            ("Appendix E: Compact Student Self-Check Answer Key", "All 900 Problems", "Final Answers for All 90 Practice A & B Sheets", "pp. 107–111"),
            ("Appendix F: 10 End-of-Unit Mastery Quizzes (Units 1–10)", "100 Assessment Items", "1-Page Unscaffolded Summative Quiz per Unit", "pp. 112–121"),
            ("Appendix G: Quiz Keys, Standards & 3D Block Studios", "CCSS • TEKS • 3D Kits", "Unit Quiz Keys, Crosswalk & Official 3D Block Studios", "pp. 122–124"),
        ])

    ty = 30.2
    th = 11.0 if not is_coach else 16.5
    for idx, (c1, c2, c3, c4) in enumerate(toc_entries):
        bg = WHITE if idx % 2 == 0 else SUBTLE_HDR
        p.rect(margin, ty, uw, th, fill=bg, stroke=LIGHT_BORDER, line_w=0.18)
        p.text(margin + 2.5, ty + th * 0.60, c1, size=1.95, bold=True, color=INK, max_w=81.0)
        p.text(margin + 86.0, ty + th * 0.60, c2, size=1.85, color=SLATE, max_w=35.0)
        p.text(margin + 123.0, ty + th * 0.60, c3, size=1.80, color=TEAL_ACCENT, max_w=42.0)
        p.text(margin + uw - 2.5, ty + th * 0.60, c4, size=1.95, bold=True, mono=True, color=INK, align="right")
        ty += th

    p.line(margin, p.h - 12.2, margin + uw, p.h - 12.2, color=BORDER, width=0.25)
    p.text(margin, p.h - 8.2, f"THE STACKCALC LIBRARY  •  {doc_footer}", size=1.88, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 8.2, "iii", size=2.1, bold=True, mono=True, color=INK, align="right")
    c.showPage()

    # =========================================================
    # PAGE iv (VERSO): PREFACE (AFTER THE TABLE OF CONTENTS)
    # =========================================================
    p = CanvasPage(c, letter)
    p.text(
        margin,
        12.2,
        "PREFACE FOR PARENTS, TEACHERS & COACHES  •  TWO-METHOD PAPER MASTERY, BLOCKS & STACK CHECK"
        if is_coach
        else "PREFACE FOR STUDENTS & FAMILIES  •  WHY TWO PAPER METHODS + BLOCKS + STACK BUILD REAL MASTERY",
        size=1.95,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
    )
    p.text(
        margin,
        18.2,
        "Preface: Why Two Paper Methods + Physical Blocks + Stack Work",
        size=3.80,
        bold=True,
        color=INK,
        max_w=uw,
    )
    p.line(margin, 21.5, margin + uw, 21.5, color=INK, width=0.45)

    # Box 1: Why Paper & Blocks Come First — and Why the Stack Has No [=] Key
    p.rect(margin, 24.0, uw, 51.0, fill=WHITE, stroke=INK, r=1.0, line_w=0.28)
    p.rect(margin, 24.0, uw, 5.0, fill=BAND_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(
        margin + 3.0,
        27.6,
        "1. PAPER & BLOCKS FIRST: WHY THIS WORKBOOK NEVER BECOMES A CALCULATOR CRUTCH",
        size=1.88,
        bold=True,
        mono=True,
        color=INK,
    )
    p.para(
        margin + 3.5,
        32.8,
        "Middle school is where many students begin memorizing formulas ('flip and multiply,' 'move the x') without understanding why they work—and where standard [=] calculators often become a mental crutch. In this workbook, students NEVER use a calculator to skip paper-and-pencil math: they solve every problem by hand on paper first (often in two independent ways!), model quantities with physical blocks, and use the distraction-free SC-6 calculator strictly at the end to verify their work.\n"
        "Why does the SC-6 have an [ENTER] key and a 4-line Stack screen (T, Z, Y, X) instead of an [=] sign? Because on paper, you write your first number on a top Waiting Line (Line Y), write your second number below it on your Workbench (Line X), and then apply the operation (+, −, ×, ÷). Try these two checks right now:",
        max_w=uw - 7.0,
        size=1.95,
        color=INK,
        leading=1.20,
    )
    p.text(margin + 3.5, 60.2, "• Try Basic Addition on the Stack (8 + 5 = 13):", size=1.95, bold=True, color=INK)
    p.draw_keycap_sequence(["8", "ENTER", "5", "+"], margin + 88.0, 56.6, max_w=96.0, h=4.5, gap=0.9)
    p.text(margin + 3.5, 67.6, "• Try Two-Dot Exact Fractions (1/3 + 1/4 = 7/12):", size=1.95, bold=True, color=INK)
    p.draw_keycap_sequence([".", "1", ".", "3", "ENTER", ".", "1", ".", "4", "+"], margin + 88.0, 64.0, max_w=96.0, h=4.5, gap=0.9)

    # 5 Manipulative Photos Showcase Strip (Our 3 Published Block Studios!)
    p.rect(margin, 77.5, uw, 30.5, fill=WHITE, stroke=LIGHT_BORDER, r=1.0, line_w=0.22)
    showcase = [
        ("place_value_regrouping.png", "Place Value Regrouping"),
        ("prime_studio_commutativity.png", "Prime Factor Blocks"),
        ("prime_lcm_gcd_venn.png", "Prime Factor Towers"),
        ("fraction_studio_common_denominator.png", "Fraction Strips"),
        ("fraction_studio_twin_comparator.png", "Fraction Comparator"),
    ]
    sw_w = (uw - 10.0) / 5.0
    for idx, (png_name, cap) in enumerate(showcase):
        sx = margin + 3.0 + idx * (sw_w + 1.0)
        p.rect(sx, 79.2, sw_w, 21.0, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.7, line_w=0.18)
        p.image(ASSETS_MANUALS_DIR / png_name, sx + 1.2, 80.0, sw_w - 2.4, 19.2)
        p.text(sx + sw_w / 2.0, 104.8, cap, size=1.75, bold=True, color=INK, align="center", max_w=sw_w - 1.0)

    # Box 2: How Students, Homeschool Parents & Teachers Use the Three-Step Loop
    p.rect(margin, 110.5, uw, 43.0, fill=M2_BG, stroke=TEAL_ACCENT, r=1.0, line_w=0.28)
    p.rect(margin, 110.5, uw, 5.0, fill=BAND_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(
        margin + 3.0,
        114.1,
        "2. HOW EVERY SECTION WORKS: TWO PAPER WAYS (+10 / +20), HANDS-ON BLOCKS, THEN SELF-CHECK",
        size=1.88,
        bold=True,
        mono=True,
        color=INK,
    )
    loop_bullets = [
        "• Step 1 — Solve by Hand in Your 1st Paper Way (+10 Points): Study the self-contained Worked Example and solve on paper using Method 1.",
        "• Step 2 — Solve in a 2nd Independent Paper Way or Block Model (+20 Points Double!): Confirm your answer using Method 2 or our Place Value, Fraction, or Prime Factor blocks. Solving ANY 5 problems in 2 Ways earns a full 100 Points—twice the depth in half the tedium!",
        "• Step 3 — Independent Self-Check on the SC-6 Stack: Verify your hand-written answer using the section's SC-6 Check Box and Appendix E (pp. 107–111).",
        "• Works with Homeschool & School Curricula: Pairs effortlessly with Saxon 7/6 & 8/7, Singapore Dimensions 6–8, Math Mammoth, AoPS, or Big Ideas Math.",
    ]
    lby = 119.5
    for lb in loop_bullets:
        lby = p.para(margin + 3.5, lby, lb, max_w=uw - 7.0, size=1.95, color=INK, leading=1.20, max_lines=2) + 1.6

    # Box 3: Companion Curriculum Lineup (The StackCalc Library)
    p.rect(margin, 156.0, uw, 68.0, fill=WHITE, stroke=INK, r=1.0, line_w=0.28)
    p.rect(margin, 156.0, uw, 5.0, fill=BAND_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(margin + 3.0, 159.6, "3. THE COMPLETE STACKCALC LIBRARY CURRICULUM LINEUP (100% SELF-CONTAINED)", size=1.92, bold=True, mono=True, color=INK)

    channels = [
        (
            "BOOK 1 — TEACHING WITH THE STACK: UNIFIED K–12 MASTER TEACHER & HOMESCHOOL GUIDE",
            "Organizes all K–12 concept domains and all 10 Middle School units into a single open-and-go reference with word-for-word scripts, target misconceptions, block remediations, and complete worked keys.",
            TEAL_ACCENT,
        ),
        (
            "BOOKS 2A, 2B, 3 & 4 — GRADE-BAND HANDS-ON MATH LABS (K–2, 3–5, 6–8 & 9–12/AP)",
            "Self-contained lay-flat student workbooks pairing concrete 3D Block Studios, real-world mathematical story openers, guided paper-and-pencil methods, and step-by-step stack verification.",
            INK,
        ),
        (
            "BOOK 5 — STACK SPEED & FLUENCY: SPEED LESSONS, PLAYBOOKS & 180 PROGRESSIVE PRACTICE TESTS",
            "15 speed lessons ('Slow Way vs. Champion Way' playbooks + 90 guided drills) and 180 progressive 20-problem practice tests (Tests A1–D3, 3,690 problems) for full-year computational fluency.",
            TEAL_ACCENT,
        ),
        (
            "COMPANION ILLUSTRATED STORYBOOKS & 3D MANIPULATIVE BLOCK STUDIOS",
            "Explore From Blocks to the Stack (Grades K–6) and Thinking in the Stack (Grades 7–12), plus our Place Value, Fraction, and Prime Factor 3D Block Studios at stackcalc.io.",
            INK,
        ),
    ]
    chy = 162.5
    for ch_head, ch_body, ch_col in channels:
        p.rect(margin + 3.0, chy, uw - 6.0, 14.0, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.7, line_w=0.18)
        p.text(margin + 5.0, chy + 3.8, ch_head, size=1.86, bold=True, mono=True, color=ch_col, max_w=uw - 10.0)
        p.para(margin + 5.0, chy + 7.5, ch_body, max_w=uw - 10.0, size=1.82, color=INK, leading=1.14, max_lines=2)
        chy += 15.0

    # Box 4: Pacing & Book Alignment Summary
    p.rect(margin, 226.5, uw, 34.5, fill=SUBTLE_HDR, stroke=BORDER, r=1.0, line_w=0.25)
    p.text(margin + 3.5, 231.0, "4. RECOMMENDED MIDDLE SCHOOL KIT, FREE WEB SIMULATOR & FLEXIBLE PACING", size=1.92, bold=True, mono=True, color=TEAL_ACCENT)
    pacing_notes = [
        "• Core Kit for Book 3: StackCalc SC-6 Calculator + Place Value, Fraction & Prime Factor Block Kits (pp. 123–124) + Volume I & II Trade Books!",
        "• Waiting for Your Physical SC-6? Practice every lesson today on our free interactive web simulator or iOS/watchOS app at https://stackcalc.io!",
        "• Daily Supplement + 10 Unit Quizzes (pp. 112–121): Solve any 5 problems in 2 Ways (+20 pts each = 100 pts) or all 10 in 1 Way (+10 each).",
    ]
    py_n = 236.5
    for p_line in pacing_notes:
        p.text(margin + 3.5, py_n, p_line, size=1.85, color=INK, max_w=uw - 7.0)
        py_n += 7.2

    p.line(margin, p.h - 12.2, margin + uw, p.h - 12.2, color=BORDER, width=0.25)
    p.text(margin, p.h - 8.2, f"THE STACKCALC LIBRARY  •  {doc_footer}", size=1.88, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 8.2, "iv", size=2.1, bold=True, mono=True, color=INK, align="right")
    c.showPage()


def draw_unit_mastery_quiz_page(
    p: CanvasPage,
    ch: Dict[str, Any],
    page_num: int,
    total_pages: int,
    page_label_override: Optional[str] = None,
) -> None:
    """Renders a 1-Page Unscaffolded End-of-Unit Mastery Assessment (10 problems × 10 pts = 100 pts)."""
    margin = 11.0
    uw = p.w - 2 * margin
    ch_num = ch["num"]
    quiz = UNIT_QUIZZES_DATA[ch_num]
    probs = quiz["problems"]

    # 1. Top Assessment Header (y = 9.0 .. 24.4 mm)
    p.text(
        margin,
        12.2,
        f"APPENDIX F • END-OF-UNIT MASTERY QUIZ — UNIT {ch_num:02d} OF 10 ({quiz['ccss']} • {quiz['teks']})",
        size=1.95,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=122.0,
    )
    p.rect(margin + uw - 70.0, 9.0, 70.0, 4.6, fill=SUBTLE_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(
        margin + uw - 35.0,
        12.1,
        "SUMMATIVE QUIZ: 10 ITEMS × 10 PTS = 100",
        size=1.75,
        bold=True,
        mono=True,
        color=INK,
        align="center",
        max_w=67.0,
    )

    p.text(
        margin,
        18.0,
        f"Unit {ch_num} Mastery Quiz: {ch['title']}",
        size=3.95,
        bold=True,
        color=INK,
        max_w=uw,
    )
    p.text(
        margin,
        22.9,
        "Directions: Show all paper steps in each box (+6 pts work, +4 pts answer).",
        size=1.88,
        bold=True,
        color=SLATE,
        max_w=101.0,
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

    # 2. Assessment Rubric Banner (y = 25.4 .. 35.8 mm, height = 10.4 mm)
    p.rect(margin, 25.4, uw, 10.4, fill=SUBTLE_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.rect(margin, 25.4, uw, 4.0, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.22)
    p.text(
        margin + 2.5,
        28.2,
        f"ASSESSMENT BREAKDOWN: #1–#6 CORE FLUENCY (60 PTS)  •  #7–#9 REAL-LIFE APPLICATIONS (30 PTS)  •  #10 ERROR ANALYSIS (10 PTS)",
        size=1.72,
        bold=True,
        mono=True,
        color=INK,
        max_w=uw - 5.0,
    )
    p.text(
        margin + 2.5,
        33.4,
        f"Standards Assessed: {quiz['ccss']}  •  {quiz['teks']}  •  {quiz['best']}  •  {quiz['contest']}",
        size=1.72,
        bold=True,
        color=TEAL_ACCENT,
        max_w=uw - 5.0,
    )

    # 3. 10 Unscaffolded Quiz Cards (y = 37.2 .. 265.1 mm, 5 Rows × 2 Columns)
    grid_y0 = 37.2
    col_w = (uw - 3.0) / 2.0
    row_h = 44.5
    row_gap = 1.35

    for idx, qprob in enumerate(probs[:10]):
        r = idx // 2
        c_idx = idx % 2
        px = margin + c_idx * (col_w + 3.0)
        py = grid_y0 + r * (row_h + row_gap)

        p.rect(px, py, col_w, row_h, fill=WHITE, stroke=SLATE, r=0.9, line_w=0.28)
        q_num = qprob["num"]
        p.rect(px + 2.0, py + 1.8, 5.4, 4.4, fill=BAND_HDR, stroke=INK, r=0.65, line_w=0.22)
        p.text(px + 4.7, py + 4.8, str(q_num), size=2.10, bold=True, mono=True, color=INK, align="center")

        p.text(
            px + 8.8,
            py + 4.7,
            f"{qprob['tag']} • 10 PTS",
            size=1.55,
            bold=True,
            mono=True,
            color=TEAL_ACCENT,
            max_w=col_w - 11.0,
        )

        p.para(
            px + 2.6,
            py + 9.2,
            qprob["prompt"],
            max_w=col_w - 5.2,
            size=1.96,
            bold=True,
            color=INK,
            leading=1.15,
            max_lines=3,
        )

        # Clean 5 mm dot-grid scratch workspace (unscaffolded — zero giveaway hints)
        for gx_mm in range(int(px + 5), int(px + col_w - 3), 5):
            for gy_mm in range(int(py + 21), int(py + row_h - 6), 5):
                p.circle(float(gx_mm), float(gy_mm), 0.19, fill=BORDER, stroke=BORDER, line_w=0.04)

        p.text(
            px + 2.4,
            py + row_h - 2.0,
            "[ ] Work (+6)  [ ] Ans (+4)",
            size=1.50,
            mono=True,
            color=MUTED,
            max_w=col_w - 45.0,
        )
        p.text(
            px + col_w - 2.4,
            py + row_h - 2.0,
            "Ans: ________________________",
            size=1.90,
            bold=True,
            mono=True,
            color=INK,
            align="right",
        )

    p.text(
        margin,
        p.h - 8.2,
        f"StackCalc SC-6 Textbook Supplement  •  Unit {ch_num}: {ch['title']} — Summative Unit Mastery Quiz ({quiz['ccss']} • {quiz['teks']})",
        size=1.85,
        mono=True,
        color=MUTED,
        max_w=uw - 28.0,
    )
    pg_lbl = page_label_override or f"Page {page_num} of {total_pages}"
    p.text(margin + uw, p.h - 8.2, pg_lbl, size=1.88, bold=True, mono=True, color=INK, align="right")


def draw_student_workbook_back_matter(c: canvas.Canvas, chapters: List[Dict[str, Any]], start_page: int, total_pages: int) -> None:
    """Renders 21 Reference & Assessment Appendix Pages (Appendices A–E on pp. 103–111, Appendix F Unit Quizzes on pp. 112–121, and Appendix G Quiz Keys, Crosswalk & Printable Manipulatives on pp. 122–123)."""
    margin = 13.0
    uw = (letter[0] / mm) - 2 * margin

    # ---------------------------------------------------------
    # APPENDIX A (Page 103): Middle School Math Formulas, Benchmarks & Conversions
    # ---------------------------------------------------------
    p = CanvasPage(c, letter)
    p.text(margin, 12.0, "REFERENCE APPENDIX A  •  MIDDLE SCHOOL FORMULAS, BENCHMARKS & CONVERSIONS", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin, 18.0, "Appendix A: Middle School Math Formulas & Reference Sheet (Units 1–10)", size=3.9, bold=True, color=INK, max_w=uw)
    p.line(margin, 21.2, margin + uw, 21.2, color=INK, width=0.45)

    formula_sections = [
        (
            "UNITS 1–2: FACTORS, FRACTIONS & DECIMALS",
            [
                "• Division Check Identity: Dividend = (Divisor × Quotient) + Remainder, with 0 ≤ Remainder < Divisor. Verify on SC-6: [n] [ENTER] [d] [g][÷R].",
                "• GCF & LCM Product Law: For any two positive integers a and b, GCF(a, b) × LCM(a, b) = a × b. Verify on SC-6: [a] [ENTER] [b] [GCF] and [f][LCM].",
                "• Fraction Multiplication & Division: (a/b) × (c/d) = (a·c)/(b·d);  (a/b) ÷ (c/d) = (a/b) × (d/c) (Multiply by the Reciprocal!).",
            ],
        ),
        (
            "UNIT 3: RATIOS, RATES, PERCENTS & MEASUREMENT CONVERSIONS",
            [
                "• Percent Proportion & Equation: Part / Whole = Percent / 100  →  Part = (Percent / 100) × Whole. Percent Change = (|New - Old| / Old) × 100%.",
                "• Key Fraction-Decimal-Percent Benchmarks: 1/8 = 0.125 = 12.5% | 1/5 = 0.20 = 20% | 1/4 = 0.25 = 25% | 1/3 ≈ 0.333 = 33.3% | 3/8 = 0.375 = 37.5% | 1/2 = 0.5 = 50% | 3/4 = 0.75 = 75%.",
                "• Customary & Metric Conversions: 1 ft = 12 in | 1 yd = 3 ft | 1 mi = 5,280 ft | 1 in = 2.54 cm | 1 m = 100 cm = 1,000 mm | 1 km = 1,000 m | 1 lb = 16 oz | 1 kg ≈ 2.205 lb | 1 gal = 4 qt = 8 pt = 16 c.",
            ],
        ),
        (
            "UNITS 4, 6 & 7: ALGEBRAIC EXPRESSIONS, INTEGERS, EQUATIONS & INEQUALITIES",
            [
                "• Distributive, Commutative & Associative Properties: a(b + c) = ab + ac;  a + b = b + a;  ab = ba;  (a + b) + c = a + (b + c).",
                "• Signed Integer Rules: Adding an opposite gives zero: a + (-a) = 0 (1 Zero-Pair). Subtracting a number is adding its opposite: a - b = a + (-b). Product/quotient of same signs is (+); opposite signs is (-).",
                "• Coordinate Plane Distance: Horizontal distance = |x_2 - x_1|; Vertical distance = |y_2 - y_1|; Reflection across x-axis: (x, y) -> (x, -y); across y-axis: (x, y) -> (-x, y).",
            ],
        ),
        (
            "UNITS 5 & 8: 2D POLYGON AREA, ELAPSED TIME & 3D SURFACE AREA / VOLUME",
            [
                "• 2D Polygon Areas: Rectangle A = l·w, P = 2(l+w) | Parallelogram A = b·h | Triangle A = (1/2)·b·h | Trapezoid A = (1/2)·(b_1 + b_2)·h | Circle C = 2·π·r = π·d, A = π·r².",
                "• 3D Solid Volumes & Nets: Rectangular Prism V = l·w·h = B·h, SA = 2(lw + lh + wh) | Triangular Prism V = B·h | Pyramid SA = B + Sum(Lateral Triangle Areas) | Cylinder V = π·r²·h | Cone V = (1/3)·π·r²·h.",
                "• Base-60 Elapsed Time: 1 hr = 60 min = 3,600 sec. Convert H.MMSS to decimal hours on SC-6 with [f][▸HR], and back with [g][▸HMS].",
            ],
        ),
        (
            "UNITS 9 & 10: STATISTICAL MEASURES (MEAN, MEDIAN, IQR, MAD) & PROBABILITY",
            [
                "• Center & Spread: Mean (x-bar) = (Sum of values) / n | Median = middle value of ordered list | Range = Max - Min | IQR = Q_3 - Q_1 | Mean Absolute Deviation (MAD) = (Sum |x_i - x-bar|) / n.",
                "• Theoretical & Compound Probability: P(Event) = (Favorable Outcomes) / (Total Possible Outcomes), 0 ≤ P(E) ≤ 1; P(not E) = 1 - P(E); Independent events: P(A and B) = P(A) × P(B).",
            ],
        ),
    ]
    fy = 24.5
    for f_title, f_lines in formula_sections:
        box_h = 44.5 if len(f_lines) == 3 else 34.0
        p.rect(margin, fy, uw, box_h, fill=WHITE, stroke=INK, r=0.9, line_w=0.25)
        p.rect(margin, fy, uw, 5.2, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.25)
        p.text(margin + 2.8, fy + 3.6, f_title, size=1.95, bold=True, mono=True, color=INK)
        ly = fy + 10.2
        for fl in f_lines:
            ly = p.para(margin + 3.2, ly, fl, max_w=uw - 6.4, size=2.15, color=INK, leading=1.32, max_lines=3)
            ly += 2.6
        fy += box_h + 3.2

    p.text(margin, p.h - 8.2, "StackCalc SC-6 Textbook Supplement  •  Appendix A: Middle School Math Formulas & Conversions", size=1.88, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 8.2, f"Page {start_page} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")
    c.showPage()

    # ---------------------------------------------------------
    # APPENDIX B (Page 104): SC-6 Elementary Keycap Directory & 4-Stack Reference
    # ---------------------------------------------------------
    p = CanvasPage(c, letter)
    p.text(margin, 12.0, "REFERENCE APPENDIX B  •  SC-6 ELEMENTARY CALCULATOR & 4-STACK DIRECTORY", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin, 18.0, "Appendix B: SC-6 Keycap Directory & 4-Register Stack Guide", size=3.9, bold=True, color=INK, max_w=uw)
    p.line(margin, 21.2, margin + uw, 21.2, color=INK, width=0.45)

    p.rect(margin, 24.0, uw, 28.0, fill=M2_BG, stroke=TEAL_ACCENT, r=1.0, line_w=0.28)
    p.text(margin + 3.0, 29.0, "THE 4-FLOOR NUMBER ELEVATOR (REGISTERS T, Z, Y, X) — ZERO PARENTHESES NEEDED", size=2.1, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin + 3.0, 34.5, "• Floor 1 (Register X — Bottom Line): Shows the number you are typing right now, or the answer to the operation you just pressed.", size=1.88, color=INK, max_w=uw - 6.0)
    p.text(margin + 3.0, 39.8, "• Floor 2 (Register Y — Upper Line): Holds your first number after you press [ENTER]. Pressing [+], [-], [×], or [÷] combines Y with X.", size=1.88, color=INK, max_w=uw - 6.0)
    p.text(margin + 3.0, 45.1, "• Floors 3 & 4 (Registers Z & T): Hold extra numbers during multi-step problems. Press [4-LV] to view all 4 floors at once!", size=1.88, bold=True, color=INK, max_w=uw - 6.0)

    p.rect(margin, 55.0, uw, 5.0, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.25)
    p.text(margin + 2.5, 58.4, "KEYCAP / SHIFT", size=1.75, bold=True, mono=True, color=INK)
    p.text(margin + 36.0, 58.4, "FUNCTION NAME", size=1.75, bold=True, mono=True, color=INK)
    p.text(margin + 82.0, 58.4, "EXAMPLE KEYSTROKES", size=1.75, bold=True, mono=True, color=INK)
    p.text(margin + 136.0, 58.4, "WHAT IT DOES ON THE SC-6", size=1.75, bold=True, mono=True, color=INK)

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
        ("[f] [?] (Tutorial)", "Built-In Math Quiz", ["f", "?"], "Launches interactive step-by-step Tutorial & Quiz Mode for 100-Point Mastery!"),
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

    p.text(margin, p.h - 8.2, "StackCalc SC-6 Textbook Supplement  •  Appendix B: SC-6 Keycap & 4-Stack Reference", size=1.88, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 8.2, f"Page {start_page + 1} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")
    c.showPage()

    # ---------------------------------------------------------
    # APPENDIX C (Page 105): Hands-On Manipulative Models & Visual Tools Guide
    # ---------------------------------------------------------
    p = CanvasPage(c, letter)
    p.text(margin, 12.0, "REFERENCE APPENDIX C  •  HANDS-ON MANIPULATIVE MODELS & VISUAL TOOLS GUIDE", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin, 18.0, "Appendix C: Hands-On Classroom Manipulatives & Visual Modeling Guide", size=3.9, bold=True, color=INK, max_w=uw)
    p.line(margin, 21.2, margin + uw, 21.2, color=INK, width=0.45)

    p.rect(margin, 24.0, uw, 5.2, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.25)
    p.text(margin + 2.5, 27.6, "MANIPULATIVE MODEL", size=1.75, bold=True, mono=True, color=INK)
    p.text(margin + 56.0, 27.6, "UNITS", size=1.75, bold=True, mono=True, color=INK)
    p.text(margin + 78.0, 27.6, "HOW TO MODEL TEXTBOOK CONCEPTS WITH THE BLOCKS", size=1.75, bold=True, mono=True, color=INK)

    kit_guide_rows = [
        ("Prime Factor Towers & Venn Tray", "Unit 1", "Stack proportional prime factor blocks (2, 3, 5, 7) to model exponents and place shared prime blocks in the Venn intersection for GCF & LCM."),
        ("Place Value Whole-Number Tray", "Unit 1", "Model multi-digit division quotients and remainders across base-10 place columns and hold partial sub-results on stack shelf Y."),
        ("Fraction Strips & Comparator", "Unit 2", "Compare fraction strips side-by-side inside the 84 mm twin comparator channel to find common denominators and model fraction division."),
        ("Place Value Decimal Tray", "Unit 2", "Trade ones, tenths, hundredths, and thousandths across decimal columns before verifying exact decimal operations on the stack."),
        ("Fraction Tape Diagrams & Ratios", "Unit 3", "Use equal-length fraction strips as physical Tape Diagram bars to compare part-to-part vs. part-to-whole ratios, unit rates, and percents."),
        ("Place Value & Prime Factor Models", "Unit 4", "Treat variable powers (x², x, 1) as distinct place columns that cannot be combined, and use Prime Factor blocks to factor out the GCF."),
        ("Fraction & Place Value + Grids", "Unit 5", "Decompose parallelograms, triangles, and trapezoids on grid diagrams, accumulate composite areas with [Σ+], and regroup base-60 time with [CLK]."),
        ("Place Value, Number Line & Scale", "Units 6, 7", "Model signed opposites and zero pairs along the [f][LINE] number line, and solve one-step equations as balanced scales verified with [≠]."),
        ("Place Value Unit Cubes & 2D Nets", "Unit 8", "Pack unit blocks into rectangular prisms to see V = l·w·h across 3 stack levels (Z, Y, X) and sum unfolded 2D face pairs with [Σ+]."),
        ("Place Value Towers & Fraction Ratios", "Units 9, 10", "Level unequal Place Value stacks to find the fair-share Mean, divide ordered data into 4 quarters (FRAC-01) for IQR, and model probability ratios."),
    ]
    gy = 29.2
    gh = 19.5
    for idx, (k_sku, k_units, k_how) in enumerate(kit_guide_rows):
        p.rect(margin, gy, uw, gh, fill=WHITE if idx % 2 == 0 else SUBTLE_HDR, stroke=LIGHT_BORDER, line_w=0.18)
        p.text(margin + 2.2, gy + 8.2, k_sku, size=1.92, bold=True, color=TEAL_ACCENT, max_w=52.0)
        p.text(margin + 56.0, gy + 8.2, k_units, size=1.88, bold=True, mono=True, color=INK, max_w=20.0)
        p.para(margin + 78.0, gy + 6.2, k_how, max_w=uw - 80.5, size=1.95, color=INK, leading=1.24, max_lines=3)
        gy += gh

    p.rect(margin, 227.5, uw, 34.0, fill=M2_BG, stroke=TEAL_ACCENT, r=1.0, line_w=0.28)
    p.text(margin + 3.0, 232.8, "COMPANION RESOURCES & OPEN CURRICULUM LIBRARY", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin + 3.0, 238.5, "• Print & Digital Workbooks + Unified Teacher's Guide (The StackCalc Library): https://stackcalc.io/curriculum/", size=1.85, bold=True, color=INK)
    p.text(margin + 3.0, 244.0, "• Illustrated Companion Book — From Blocks to the Stack (Amazon): https://link.amazon/B0f5cP0Ur", size=1.85, color=INK)
    p.text(margin + 3.0, 249.5, "• Classroom Manipulative Sets & Hardware: https://stackcalcmath.etsy.com  |  https://stackcalc.io", size=1.85, color=INK)
    p.text(margin + 3.0, 255.0, "• Printable Individual Chapter Packets (Units 1–10): https://stackcalc.io/curriculum/big-ideas-middle-school-sc6-workbook/", size=1.85, color=INK)

    p.text(margin, p.h - 8.2, "StackCalc SC-6 Textbook Supplement  •  Appendix C: Hands-On Manipulative Models Guide", size=1.88, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 8.2, f"Page {start_page + 2} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")
    c.showPage()

    # ---------------------------------------------------------
    # APPENDIX D (Page 106): Official 100-Point Mastery Certificate & Dot-Grid Scratchpad
    # ---------------------------------------------------------
    p = CanvasPage(c, letter)
    p.text(margin, 12.0, "REFERENCE APPENDIX D  •  CERTIFICATE OF MASTERY & DOT-GRID WORKSPACE", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin, 18.0, "Appendix D: 100-Point Mastery Certificate & Graph Scratchpad", size=3.9, bold=True, color=INK, max_w=uw)
    p.line(margin, 21.2, margin + uw, 21.2, color=INK, width=0.45)

    # Certificate Box (top half)
    cert_y = 25.0
    cert_h = 102.0
    p.rect(margin, cert_y, uw, cert_h, fill=SUBTLE_HDR, stroke=INK, r=2.0, line_w=0.45)
    p.rect(margin + 3.0, cert_y + 3.0, uw - 6.0, cert_h - 6.0, fill=WHITE, stroke=TEAL_ACCENT, r=1.5, line_w=0.3)
    p.text(margin + uw / 2.0, cert_y + 14.0, "STACKCALC LEARNING LAB  •  BIG IDEAS MATH MIDDLE SCHOOL SUPPLEMENT", size=2.1, bold=True, mono=True, color=TEAL_ACCENT, align="center")
    p.text(margin + uw / 2.0, cert_y + 24.5, "CERTIFICATE OF TWO-METHOD MATHEMATICAL MASTERY", size=4.6, bold=True, color=INK, align="center")
    p.text(margin + uw / 2.0, cert_y + 35.5, "This certifies that: __________________________________________________", size=2.65, bold=True, color=INK, align="center", max_w=uw - 18.0)
    p.para(
        margin + 12.0,
        cert_y + 43.0,
        "has successfully completed the 10-Unit Big Ideas Math Middle School Two-Method Block & SC-6 Supplement—solving problems by hand using multiple textbook pathways (+10 Single-Method & +20 Two-Method Mastery), modeling concepts with hands-on manipulatives, and verifying work on the 4-register StackCalc SC-6 calculator.",
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
    p.rect(margin, grid_y, uw, 5.0, fill=BAND_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(margin + 3.0, grid_y + 3.5, "EXTRA 5 MM DOT-GRID MATHEMATICAL SCRATCHPAD (TAPE DIAGRAMS, NUMBER LINES, NETS & COORDINATE GRAPHS)", size=1.80, bold=True, mono=True, color=INK)
    for gx_mm in range(int(margin + 6), int(margin + uw - 4), 5):
        for gy_mm in range(int(grid_y + 10), int(grid_y + grid_h - 4), 5):
            p.circle(float(gx_mm), float(gy_mm), 0.22, fill=BORDER, stroke=BORDER, line_w=0.05)

    p.text(margin, p.h - 8.2, "StackCalc SC-6 Textbook Supplement  •  Appendix D: Mastery Certificate & Scratchpad", size=1.88, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 8.2, f"Page {start_page + 3} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")
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
            f"REFERENCE APPENDIX E  •  STUDENT SELF-CHECK ANSWER KEY ({u_nums_str} — FINAL ANSWERS ONLY)",
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
            p.rect(margin, uy, uw, 5.0, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.25)
            p.text(
                margin + 2.5,
                uy + 3.4,
                f"UNIT {ch_obj['num']}: {ch_obj['title'].upper()} ({ch_obj['big_ideas_book'].upper()})",
                size=1.80,
                bold=True,
                mono=True,
                color=INK,
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
                p.text(margin + 2.4, row_y0, a_line_1, size=1.72, bold=True, mono=True, color=INK, max_w=uw - 4.8)
                p.text(margin + 2.4, row_y0 + step_r, a_line_2, size=1.72, bold=True, mono=True, color=INK, max_w=uw - 4.8)
                p.text(margin + 2.4, row_y0 + step_r * 2, b_line_1, size=1.72, mono=True, color=SLATE, max_w=uw - 4.8)
                p.text(margin + 2.4, row_y0 + step_r * 3, b_line_2, size=1.72, mono=True, color=SLATE, max_w=uw - 4.8)

            uy += unit_box_h + 3.2

        p.text(
            margin,
            p.h - 8.2,
            f"StackCalc SC-6 Textbook Supplement  •  Appendix E: Student Self-Check Answer Key (Units {u_pair[0]['num']}–{u_pair[1]['num']})",
            size=1.88,
            mono=True,
            color=MUTED,
        )
        p.text(margin + uw, p.h - 8.2, f"Page {pg_cur} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")
        c.showPage()

    # ---------------------------------------------------------
    # APPENDIX F (Pages 112–121): 10 End-of-Unit Mastery Quizzes (Units 1–10, 1 Page per Unit)
    # ---------------------------------------------------------
    for u_idx, ch_quiz in enumerate(chapters):
        pg_quiz = start_page + 9 + u_idx
        pq = CanvasPage(c, letter)
        draw_unit_mastery_quiz_page(pq, ch_quiz, pg_quiz, total_pages)
        c.showPage()

    # ---------------------------------------------------------
    # APPENDIX G, PART 1 (Page 122): Unit Mastery Quiz Answer Keys & State Standards Crosswalk
    # ---------------------------------------------------------
    pg_g1 = start_page + 19
    p = CanvasPage(c, letter)
    p.text(
        margin,
        11.5,
        "REFERENCE APPENDIX G (PART 1)  •  UNIT MASTERY QUIZ ANSWER KEYS & STATE STANDARDS CROSSWALK",
        size=1.95,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
    )
    p.text(
        margin,
        17.2,
        "Appendix G: Unit Mastery Quiz Keys & State Standards Crosswalk (Units 1–10)",
        size=3.70,
        bold=True,
        color=INK,
        max_w=uw,
    )
    p.text(
        margin,
        21.2,
        "Complete answers for all 10 End-of-Unit Mastery Quizzes (pp. 112–121) plus Common Core (CCSS), Texas TEKS & Florida B.E.S.T. alignment.",
        size=1.78,
        color=SLATE,
        max_w=uw,
    )
    p.line(margin, 22.6, margin + uw, 22.6, color=INK, width=0.4)

    # Top Section: 10 Unit Quiz Answer Key Strips (y = 24.0 .. 166.5 mm)
    qy = 24.0
    qh = 13.7
    qgap = 0.55
    for ch_obj in chapters:
        u_num = ch_obj["num"]
        q_meta = UNIT_QUIZZES_DATA[u_num]
        q_probs = q_meta["problems"]
        p.rect(margin, qy, uw, qh, fill=WHITE, stroke=INK, r=0.7, line_w=0.22)
        p.rect(margin, qy, uw, 3.9, fill=BAND_HDR, stroke=INK, r=0.6, line_w=0.20)
        p.text(
            margin + 2.2,
            qy + 2.8,
            f"UNIT {u_num:02d} MASTERY QUIZ KEY (p. {111 + u_num}): {ch_obj['title'].upper()}",
            size=1.60,
            bold=True,
            mono=True,
            color=INK,
            max_w=105.0,
        )
        p.text(
            margin + uw - 2.2,
            qy + 2.8,
            f"{q_meta['ccss']} • {q_meta['teks']} • {q_meta['best']}",
            size=1.48,
            bold=True,
            mono=True,
            color=TEAL_ACCENT,
            align="right",
            max_w=80.0,
        )
        q_line_1 = "   ".join(f"Q{qp['num']}: {qp['ans']}" for qp in q_probs[:5])
        q_line_2 = "   ".join(f"Q{qp['num']}: {qp['ans']}" for qp in q_probs[5:10])
        p.text(margin + 2.4, qy + 7.6, q_line_1, size=1.66, bold=True, mono=True, color=INK, max_w=uw - 4.8)
        p.text(margin + 2.4, qy + 11.6, q_line_2, size=1.66, mono=True, color=SLATE, max_w=uw - 4.8)
        qy += qh + qgap

    # Bottom Section: Middle School State Standards & Competition Crosswalk (y = 169.0 .. 266.5 mm)
    st_y = 169.0
    p.rect(margin, st_y, uw, 4.8, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.25)
    p.text(margin + 2.0, st_y + 3.3, "UNIT & TOPIC", size=1.60, bold=True, mono=True, color=INK)
    p.text(margin + 50.0, st_y + 3.3, "COMMON CORE (CCSS)", size=1.60, bold=True, mono=True, color=INK)
    p.text(margin + 90.0, st_y + 3.3, "TEXAS TEKS", size=1.60, bold=True, mono=True, color=INK)
    p.text(margin + 120.0, st_y + 3.3, "FLORIDA B.E.S.T.", size=1.60, bold=True, mono=True, color=INK)
    p.text(margin + 150.0, st_y + 3.3, "CONTEST / CURRICULUM", size=1.60, bold=True, mono=True, color=INK)

    ry_st = st_y + 4.8
    rh_st = 9.2
    for idx_u, ch_obj in enumerate(chapters):
        u_num = ch_obj["num"]
        q_meta = UNIT_QUIZZES_DATA[u_num]
        p.rect(margin, ry_st, uw, rh_st, fill=WHITE if idx_u % 2 == 0 else SUBTLE_HDR, stroke=LIGHT_BORDER, line_w=0.18)
        p.text(margin + 2.0, ry_st + 5.8, f"U{u_num:02d}: {ch_obj['title']}", size=1.68, bold=True, color=INK, max_w=46.0)
        p.text(margin + 50.0, ry_st + 5.8, q_meta["ccss"].replace("CCSS ", ""), size=1.62, color=SLATE, max_w=38.0)
        p.text(margin + 90.0, ry_st + 5.8, q_meta["teks"].replace("TEKS ", ""), size=1.62, bold=True, color=TEAL_ACCENT, max_w=28.0)
        p.text(margin + 120.0, ry_st + 5.8, q_meta["best"].replace("FL ", ""), size=1.62, color=SLATE, max_w=28.0)
        p.text(margin + 150.0, ry_st + 5.8, q_meta["contest"], size=1.58, color=INK, max_w=uw - 152.0)
        ry_st += rh_st

    p.text(
        margin,
        p.h - 8.2,
        "StackCalc SC-6 Textbook Supplement  •  Appendix G (Part 1): Unit Mastery Quiz Answer Keys & Standards Crosswalk",
        size=1.88,
        mono=True,
        color=MUTED,
    )
    p.text(margin + uw, p.h - 8.2, f"Page {pg_g1} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")
    c.showPage()

    # ---------------------------------------------------------
    # APPENDIX G, PART 2 (Page 123): Official 3D Manipulative Block Studios & Desk Activities
    # ---------------------------------------------------------
    pg_g2 = start_page + 20
    p = CanvasPage(c, letter)
    p.text(
        margin,
        11.5,
        "REFERENCE APPENDIX G (PART 2)  •  OFFICIAL 3D MANIPULATIVE BLOCK STUDIOS & DESK ACTIVITIES",
        size=1.95,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
    )
    p.text(
        margin,
        17.2,
        "Official 3D Manipulative Block Studios & Middle School Activities",
        size=3.75,
        bold=True,
        color=INK,
        max_w=uw,
    )
    p.text(
        margin,
        21.2,
        "How our three precision 3D-printed Block Studios make middle school factors, fractions, ratios, and decimals physical.",
        size=1.78,
        color=SLATE,
        max_w=uw,
    )
    p.line(margin, 22.6, margin + uw, 22.6, color=INK, width=0.4)

    studio_cards = [
        (
            "1. PLACE VALUE STUDIO (PLACE-01) — 6×2 WHOLE & DECIMAL TRAYS, DIGIT BLOCKS (0–9) & GOLD [+1] CARRY TOKENS",
            "place_value_regrouping.png",
            "• Middle School Units 1, 2, 6, 7 & 10: Dock the 6×2 Whole Number Tray and Decimal Tray side-by-side at the raised decimal point (•) to model multi-digit division remainders ([÷R]), decimal place-value shifts (×10 / ÷10), and signed integer differences across Row 1 (Register Y) and Row 0 (Register X).\n"
            "• 2-Second Desk Check: Every socket holds a single Digit Block [0]–[9]; whenever a column reaches 10, snap a Gold [+1] Carry Token one column left.",
            "Try on SC-6 (Decimal Split 14.75 -> IP=14, FP=0.75):",
            ["14.75", "ENTER", "f", "IP"],
        ),
        (
            "2. FRACTION STUDIO (FRAC-01) — 84.0 MM PROPORTIONAL FRACTION TOWERS & 12-SOCKET COMPARATOR LID",
            "fraction_studio_twin_comparator.png",
            "• Middle School Units 2, 3, 5 & 8: Because 1 Whole stands 84.0 mm tall (2² × 3 × 7), halves (42 mm), thirds (28 mm), fourths (21 mm), sixths (14 mm), sevenths (12 mm), eighths (10.5 mm), and twelfths (7 mm) stand side-by-side in the 12-Socket Comparator Lid to prove common denominators, tape-diagram ratios, and Split-and-Rebuild fraction division by touch!\n"
            "• 4-Face Rotational Engraving: Rotate any block 90° to read its Fraction (1/4), Decimal (0.25), Percent (25%), and Two-Dot Key (.1.4).",
            "Try on SC-6 (Two-Dot Division 3/4 ÷ 3/8 = 2):",
            [".", "3", ".", "4", "ENTER", ".", "3", ".", "8", "÷"],
        ),
        (
            "3. PRIME FACTOR STUDIO (PRIME-01) — LOGARITHMIC PRIME BLOCKS (h(p) = 7.0·log2(p) MM FOR PRIMES 2, 3, 5, 7)",
            "prime_lcm_gcd_venn.png",
            "• Middle School Units 1, 4 & 10: Each prime block's physical height is proportional to its logarithm: [2] = 7.00 mm (1U), [3] = 11.09 mm, [5] = 16.25 mm, [7] = 19.65 mm. Stacking prime blocks adds their heights to multiply factors—so 2 × 2 × 3 = 12 stands dead-flush with 3 × 2 × 2!\n"
            "• GCF & LCM Comparator: Shared prime blocks between two towers form the GCF sub-tower; the tallest count of each prime forms the LCM tower.",
            "Try on SC-6 (GCF of 24 and 36 = 12):",
            ["24", "ENTER", "36", "GCF"],
        ),
    ]

    scy = 25.0
    sch = 76.5
    for sc_title, sc_img, sc_body, sc_klbl, sc_keys in studio_cards:
        p.rect(margin, scy, uw, sch, fill=WHITE, stroke=INK, r=0.9, line_w=0.26)
        p.rect(margin, scy, uw, 5.0, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.25)
        p.text(margin + 2.5, scy + 3.6, sc_title, size=1.72, bold=True, mono=True, color=INK, max_w=uw - 5.0)
        p.rect(margin + 2.5, scy + 6.8, 56.0, sch - 9.2, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.6, line_w=0.18)
        p.image(ASSETS_MANUALS_DIR / sc_img, margin + 3.5, scy + 7.8, 54.0, sch - 11.2)
        p.para(margin + 61.5, scy + 10.5, sc_body, max_w=uw - 64.5, size=1.82, color=INK, leading=1.22, max_lines=9)
        p.rect(margin + 61.5, scy + sch - 14.5, uw - 64.5, 11.8, fill=M2_BG, stroke=TEAL_ACCENT, r=0.6, line_w=0.22)
        p.text(margin + 64.0, scy + sch - 7.2, sc_klbl, size=1.72, bold=True, color=INK, max_w=68.0)
        p.draw_keycap_sequence(sc_keys, margin + 134.0, scy + sch - 11.0, max_w=uw - 138.0, h=4.5, gap=0.9)
        scy += sch + 3.2

    p.text(
        margin,
        p.h - 8.2,
        "THE STACKCALC LIBRARY  •  Appendix G (Part 2): Official 3D Manipulative Block Studios & Desk Activities",
        size=1.88,
        mono=True,
        color=MUTED,
    )
    p.text(margin + uw, p.h - 8.2, f"Page {pg_g2} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")
    c.showPage()

    # ---------------------------------------------------------
    # APPENDIX G, PART 3 (Page 124 / PDF Page 128): Official StackCalc Hardware Ecosystem & Ordering Directory
    # ---------------------------------------------------------
    pg_g3 = start_page + 21
    p = CanvasPage(c, letter)
    p.text(
        margin,
        11.5,
        "REFERENCE APPENDIX G (PART 3)  •  OFFICIAL STACKCALC HARDWARE ECOSYSTEM & LIBRARY DIRECTORY",
        size=1.95,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
    )
    p.text(
        margin,
        17.2,
        "Official StackCalc Block Studios, Calculators & Library Guide",
        size=3.75,
        bold=True,
        color=INK,
        max_w=uw,
    )
    p.text(
        margin,
        21.2,
        "Explore our 3D Manipulative Block Studios, distraction-free calculators, and companion books at https://stackcalc.io",
        size=1.78,
        color=SLATE,
        max_w=uw,
    )
    p.line(margin, 22.6, margin + uw, 22.6, color=INK, width=0.4)

    # Box 1: Hardware & Block Studio Table
    p.rect(margin, 25.0, uw, 96.0, fill=WHITE, stroke=INK, r=0.9, line_w=0.26)
    p.rect(margin, 25.0, uw, 5.0, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.25)
    p.text(margin + 2.5, 28.6, "1. OFFICIAL 3D MANIPULATIVE BLOCK STUDIOS & FOUR-LINE STACK CALCULATORS (STACKCALC.IO)", size=1.75, bold=True, mono=True, color=INK)

    hw_rows = [
        ("BLOCK KIT 1", "Place Value Studio — Digit Blocks & Carry Trays", "6×2 Whole & Decimal Trays, 40 Digit Blocks (0–9), Gold [+1] Carry Tokens & Base-10 Set", "Core Kit • K–8"),
        ("BLOCK KIT 2", "Fraction Studio — 84.0 mm Fraction Towers & Lid", "78 Proportional Fraction Towers (84.0 mm Whole down to 1/12) & 12-Socket Comparator Lid", "Core Kit • 2–8"),
        ("BLOCK KIT 3", "Prime Factor Studio — Logarithmic Prime Blocks", "Logarithmic Prime Blocks (h(p) = 7.0·log2(p) mm for primes 2, 3, 5, 7) & Comparator Lid", "Core Kit • 3–10"),
        ("SC-6 CALC", "StackCalc SC-6 Elementary & Middle School Calculator", "4-Register Visible Stack (T, Z, Y, X), Two-Dot Fractions (.a.b), [÷R], [FACT], [GCF] + Web Sim", "Core Calc • K–8"),
        ("SC-32 CALC", "StackCalc SC-32 Scientific & STEM Calculator", "32-Key Scientific RPN: [POLY], [▸θ,r], [SIN/COS/TAN], [LN/LOG], [BASE] + iOS/watchOS App", "Next Step • 8–12"),
    ]
    hy = 32.0
    for sku_c, hw_name, hw_spec, hw_grd in hw_rows:
        p.rect(margin + 2.5, hy, uw - 5.0, 16.5, fill=SUBTLE_HDR if int(hy) % 2 == 0 else WHITE, stroke=LIGHT_BORDER, r=0.6, line_w=0.20)
        p.rect(margin + 4.5, hy + 2.2, 24.0, 5.4, fill=BAND_HDR, stroke=TEAL_ACCENT, r=0.5, line_w=0.20)
        p.text(margin + 16.5, hy + 6.0, sku_c, size=1.68, bold=True, mono=True, color=TEAL_ACCENT, align="center")
        p.text(margin + 31.5, hy + 6.0, hw_name, size=1.95, bold=True, color=INK, max_w=95.0)
        p.text(margin + uw - 5.0, hy + 6.0, hw_grd, size=1.72, bold=True, color=TEAL_ACCENT, align="right")
        p.text(margin + 4.5, hy + 13.0, hw_spec, size=1.72, color=SLATE, max_w=uw - 10.0)
        hy += 17.5

    # Box 2: Complete Books in The StackCalc Library
    p.rect(margin, 124.5, uw, 90.0, fill=WHITE, stroke=INK, r=0.9, line_w=0.26)
    p.rect(margin, 124.5, uw, 5.0, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.25)
    p.text(margin + 2.5, 128.1, "2. COMPANION BOOKS & WORKBOOKS IN THE STACKCALC LIBRARY (US LETTER & 7\" × 10\" PRINT EDITIONS)", size=1.75, bold=True, mono=True, color=INK)

    lib_books = [
        ("Volume I", "From Blocks to the Stack (Grades K–6 Trade Book)", "Illustrated history of mathematics, physical block studios, and SC-6 discovery stories."),
        ("Volume II", "Thinking in the Stack (Grades 7–12 & AP Trade Book)", "Parenthesis-free algebraic, trigonometric, vector, and engineering mastery on the SC-32."),
        ("Book 1", "Teaching with the Stack (Master Teacher & Homeschool Guide)", "Unified K–12 concept guide, word-for-word scripts, misconception matrix, and middle school coaching."),
        ("Book 2A / 2B", "Early Elementary (K–2) & Upper Elementary (3–5) Math Labs", "128-page student lab workbooks (10 units, Practice A–F, STEM cases, and 4 cumulative exams each)."),
        ("Book 4", "High School & STEM Lab (Grades 9–12 & AP • SC-32)", "128-page secondary math & engineering lab workbook (840 problems across Algebra, Trig, Vectors & CS)."),
        ("Book 5", "Stack Speed & Fluency (Full-Year Timed Fluency Edition)", "15 speed lessons, Champion playbooks, and 180 progressive 20-problem timed tests (3,690 problems)."),
    ]
    by_l = 131.5
    for b_code, b_name, b_desc in lib_books:
        p.rect(margin + 2.5, by_l, uw - 5.0, 12.8, fill=WHITE if int(by_l) % 2 == 0 else SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.5, line_w=0.18)
        p.text(margin + 4.5, by_l + 5.0, f"{b_code}: {b_name}", size=1.82, bold=True, color=INK, max_w=uw - 10.0)
        p.text(margin + 4.5, by_l + 10.2, b_desc, size=1.68, color=SLATE, max_w=uw - 10.0)
        by_l += 13.6

    # Box 3: Online Answer Key Portal (kept above y = 242 mm to leave bottom-right KDP barcode zone clear)
    p.rect(margin, 218.0, uw, 24.0, fill=M2_BG, stroke=TEAL_ACCENT, r=0.9, line_w=0.26)
    p.text(margin + 3.5, 223.2, "3. ONLINE WORKED SOLUTIONS, FREE WEB SIMULATOR & HARDWARE ORDERING PORTAL", size=1.80, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin + 3.5, 229.4, "• Full Worked Solutions & Free Web/iOS Simulator:  https://stackcalc.io/curriculum/answers#middle-school", size=1.80, bold=True, color=INK)
    p.text(margin + 3.5, 235.6, "• Order Physical 3D Block Kits (Place Value Blocks, Fraction Strips & Prime Factor Towers) & Calculators (SC-6, SC-32):  https://stackcalc.io", size=1.78, color=INK)

    p.text(
        margin,
        p.h - 8.2,
        "THE STACKCALC LIBRARY  •  Appendix G (Part 3): Official StackCalc Block Studios & Hardware Ecosystem",
        size=1.88,
        mono=True,
        color=MUTED,
    )
    p.text(margin + uw, p.h - 8.2, f"Page {pg_g3} of {total_pages}", size=1.88, bold=True, mono=True, color=INK, align="right")
    c.showPage()


def draw_coach_guide_back_matter(
    c: canvas.Canvas,
    chapters: List[Dict[str, Any]],
    total_chapters: int,
    start_master_page: Optional[int] = None,
) -> None:
    """Renders 2 Reference Appendix Pages at the end of the Coach Guide."""
    margin = 13.0
    uw = (letter[0] / mm) - 2 * margin

    # Page 11 (Appendix A): Master Diagnostic Misconception Matrix & 45-Day Pacing Schedule
    p = CanvasPage(c, letter)
    p.text(margin, 12.0, "PART II • MIDDLE SCHOOL DIAGNOSTIC MISCONCEPTION & REMEDIATION MATRIX", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin, 18.0, "Middle School 10-Unit Misconception & Hands-On Remediation Matrix", size=3.9, bold=True, color=INK, max_w=uw)
    p.line(margin, 21.2, margin + uw, 21.2, color=INK, width=0.45)

    p.rect(margin, 24.0, uw, 5.0, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.25)
    p.text(margin + 2.2, 27.4, "UNIT & HANDS-ON MODEL", size=1.82, bold=True, mono=True, color=INK)
    p.text(margin + 46.0, 27.4, "TARGET CLASSROOM MISCONCEPTION", size=1.82, bold=True, mono=True, color=INK)
    p.text(margin + 116.0, 27.4, "HANDS-ON BLOCK & SC-6 REMEDIATION", size=1.82, bold=True, mono=True, color=INK)

    my = 29.0
    mh = 22.8
    for idx, ch in enumerate(chapters):
        clean_tools = clean_manipulative_label(ch["kit_summary"])
        p.rect(margin, my, uw, mh, fill=WHITE if idx % 2 == 0 else SUBTLE_HDR, stroke=LIGHT_BORDER, line_w=0.18)
        p.para(margin + 2.0, my + 5.0, f"Unit {ch['num']}: {ch['title']}", max_w=42.0, size=1.82, bold=True, color=TEAL_ACCENT, leading=1.14, max_lines=2)
        p.para(margin + 2.0, my + 12.2, clean_tools, max_w=42.0, size=1.60, mono=True, color=SLATE, leading=1.14, max_lines=2)
        p.para(margin + 46.0, my + 5.0, ch["coach_misconception"], max_w=67.0, size=1.88, color=INK, leading=1.18, max_lines=5)
        p.para(margin + 116.0, my + 5.0, ch["coach_remediation"], max_w=uw - 118.0, size=1.88, color=SLATE, leading=1.18, max_lines=5)
        my += mh

    p1_lbl = str(start_master_page) if start_master_page is not None else f"Part II Page {total_chapters + 1} of {total_chapters + 2}"
    p.text(margin, p.h - 8.2, "THE STACKCALC LIBRARY  •  TEACHING WITH THE STACK • MIDDLE SCHOOL MISCONCEPTION MATRIX", size=1.85, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 8.2, p1_lbl, size=2.1, bold=True, mono=True, color=INK, align="right")
    c.showPage()

    # Page 12 (Appendix B): Photocopiable Classroom / Homeschool Progress Roster & Notes
    p = CanvasPage(c, letter)
    p.text(margin, 12.0, "PART II • MIDDLE SCHOOL CLASSROOM & HOMESCHOOL PROGRESS ROSTER", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin, 18.0, "Photocopiable 10-Unit Middle School Student Mastery Tracker", size=3.9, bold=True, color=INK, max_w=uw)
    p.line(margin, 21.2, margin + uw, 21.2, color=INK, width=0.45)

    p.rect(margin, 24.0, uw, 5.5, fill=BAND_HDR, stroke=INK, r=0.7, line_w=0.25)
    p.text(margin + 2.5, 27.8, "STUDENT NAME / PERIOD", size=1.75, bold=True, mono=True, color=INK)
    for u_i in range(1, 11):
        ux = margin + 56.0 + (u_i - 1) * 13.0
        p.text(ux, 27.8, f"U{u_i}", size=1.75, bold=True, mono=True, color=INK)

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
    p.rect(margin, 214.0, uw, 5.2, fill=BAND_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(margin + 3.0, 217.6, "TEACHER OBSERVATION NOTES & INTERVENTION LOG", size=1.85, bold=True, mono=True, color=INK)
    p.text(margin + 3.5, 224.5, "• Print & Digital Student Workbooks & Teacher Guides (The StackCalc Library): https://stackcalc.io/curriculum/", size=1.85, bold=True, color=INK)
    p.text(margin + 3.5, 230.0, "• Companion Book — From Blocks to the Stack (Amazon): https://link.amazon/B0f5cP0Ur  |  Manipulatives: https://stackcalc.io", size=1.85, color=INK)
    for ln_i in range(3):
        ly = 238.5 + ln_i * 7.0
        p.line(margin + 3.5, ly, margin + uw - 3.5, ly, color=LIGHT_BORDER, width=0.25)

    p2_lbl = str(start_master_page + 1) if start_master_page is not None else f"Part II Page {total_chapters + 2} of {total_chapters + 2}"
    p.text(margin, p.h - 8.2, "THE STACKCALC LIBRARY  •  TEACHING WITH THE STACK • MIDDLE SCHOOL MASTERY ROSTER", size=1.85, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 8.2, p2_lbl, size=2.1, bold=True, mono=True, color=INK, align="right")
    c.showPage()


def generate_student_workbook_pdf(chapters: List[Dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_path), pagesize=letter)
    c.setTitle("Middle School Math Lab: Big Ideas Two-Method Block & SC-6 Student Workbook")
    c.setAuthor("The StackCalc Library")

    total_secs = sum(len(ch["sections"]) for ch in chapters)
    core_pages = 2 + len(chapters) + total_secs * 2  # 102 core numbered pages
    total_pages = core_pages + 22  # + 22 Appendix pages (pp. 103-124: Appendices A-E, 10 Unit Quizzes in Appendix F, and 3 Appendix G pages)

    # Pages i–iv: Title Page (i), Copyright Page (ii), Table of Contents (iii), Preface (iv)
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

    # Extra Back Matter Pages 103–124 (Appendices A–G)
    draw_student_workbook_back_matter(c, chapters, page_num, total_pages)

    c.save()
    print(f"[OK] Built Student Supplement Workbook (KDP Print & Digital Edition): {output_path} ({output_path.stat().st_size / 1024:.1f} KB, pp. i-iv + {total_pages} numbered pages = {total_pages + 4} total pages)")


# =============================================================================
# 2. COMPACT 10-PAGE COACH & SOLUTION GUIDE (EXACTLY 1 Page Per Chapter!)
# =============================================================================
UNIT_COACH_TRIAD: Dict[int, Dict[str, str]] = {
    1: {
        "concept": "1. Concept (Stack Approach): Multi-step expressions evaluate from the inside out—holding completed groups on shelf Y while building the next group on X. Every whole number factors uniquely into primes.",
        "blocks": "2. Blocks (Place Value & Prime): Model division quotients/remainders on the Place Value tray (PLACE-01) and stack Prime Factor blocks (PRIME-01) to see exponents (2³), GCF (overlap), and LCM (union).",
        "calc": "3. Calculator (SC-6): Use [g][÷R] to split Quotient (Y) and Remainder (X), [g][FACT] for prime powers, and [GCF]/[f][LCM] to verify Venn diagram results.",
    },
    2: {
        "concept": "1. Concept (Stack Approach): Rational operations require common units before adding/subtracting and multiplicative inverses (reciprocals) when dividing, holding the first operand on Y while transforming X.",
        "blocks": "2. Blocks (Fraction & Place Value): Compare 84 mm Fraction Strips (FRAC-01) side-by-side to see common denominators and 'how many fit' division; align tenths and hundredths on the Decimal Tray (PLACE-01).",
        "calc": "3. Calculator (SC-6): Enter fractions with Two-Dot notation ([.] n [.] d), flip only the divisor in X with [f][1/x] before [×], and split decimals with [f][IP] and [g][FP].",
    },
    3: {
        "concept": "1. Concept (Stack Approach): Ratios, unit rates, and percents are multiplicative comparisons. Keeping Y and X paired preserves the two quantities being compared across scaling steps.",
        "blocks": "2. Blocks (Fraction & Place Value): Lay out equal-length Fraction Strips (FRAC-01) as physical Tape Diagram bars to distinguish Part-to-Part (3:2) from Part-to-Whole (3/5) and model benchmark percents.",
        "calc": "3. Calculator (SC-6): Simplify ratios on Y:X with [g][a:b], step through ratio tables with [g][REP], swap upside-down unit rates with [x⇄y], and toggle forms with [FDISP].",
    },
    4: {
        "concept": "1. Concept (Stack Approach): Algebraic expressions are recipes of operations waiting for an input value. Evaluating an expression means pushing the substituted value onto the stack and executing inner terms first.",
        "blocks": "2. Blocks (Place Value & Prime): Treat 1, x, and x² as distinct Place Value columns (PLACE-01) so unlike terms are never combined, and use Prime Factor blocks (PRIME-01) to factor out the GCF.",
        "calc": "3. Calculator (SC-6): Substitute a test value (e.g., x = 5) into both original and simplified expressions on Y and X, then press [≠] (flashes NO when equivalent).",
    },
    5: {
        "concept": "1. Concept (Stack Approach): Every polygon area formula decomposes into base-times-height products held on the stack, while elapsed time regroups in base-60 rather than base-10.",
        "blocks": "2. Blocks (When Applicable — Fraction & Place Value): Use Fraction Strips (FRAC-01) for fractional edge lengths and Place Value columns (PLACE-01) to contrast base-10 regrouping with 60-minute hours.",
        "calc": "3. Calculator (SC-6): Compute rectangle [f][RECT] and triangle [g][TRI] areas, accumulate composite sub-areas with [Σ+] and [f][Σx], and convert H.MMSS time via [f][▸HR] and [g][▸HMS].",
    },
    6: {
        "concept": "1. Concept (Stack Approach): A signed number combines direction (+/-) and magnitude (|x|). In postfix entry, typing the magnitude first and pressing [+/-] attaches the sign to the number in X.",
        "blocks": "2. Blocks (Place Value & Fraction): Pair positive and negative Place Value blocks (PLACE-01) to form Zero Pairs, and compare rational magnitudes with 84 mm Fraction Strips (FRAC-01).",
        "calc": "3. Calculator (SC-6): Distinguish [+/-] (change sign of X) from [-] (subtract X from Y), animate signed hops on [f][LINE], find distance with [g][|x|], and test order with [f][>]/[g][<].",
    },
    7: {
        "concept": "1. Concept (Stack Approach): An equation is a balanced two-register comparison (Y = X). Solving isolates the unknown by applying inverse operations in reverse order.",
        "blocks": "2. Blocks (Place Value & Fraction): Model both sides of an equation on the Place Value tray (PLACE-01) or with Fraction Strips (FRAC-01) so removing/dividing equal amounts preserves balance.",
        "calc": "3. Calculator (SC-6): Solve with inverse operations on the stack, then push the left and right sides into Y and X and press [≠] (flashes NO when both sides are equal).",
    },
    8: {
        "concept": "1. Concept (Stack Approach): Surface area sums 2D face areas across an unfolded net, whereas 3D volume multiplies three orthogonal dimensions (l, w, h) held simultaneously in registers Z, Y, and X.",
        "blocks": "2. Blocks (When Applicable — Place Value & Fraction): Pack Place Value unit blocks (PLACE-01) to see V = l·w·h in layers, and use Fraction Strips (FRAC-01) to model fractional edge lengths.",
        "calc": "3. Calculator (SC-6): Accumulate opposite face pairs with [Σ+] -> [f][Σx] for surface area, multiply Z·Y·X with [f][PRISM] for volume, and verify [f][CIRC], [g][CONE], and [g][HYP].",
    },
    9: {
        "concept": "1. Concept (Stack Approach): Statistical summaries condense a list of numbers into measures of center (Mean, Median) and spread (IQR, MAD) by accumulating data into dedicated statistical registers.",
        "blocks": "2. Blocks (Place Value & Fraction): Level unequal Place Value digit stacks (PLACE-01) to model the Mean as a fair share, and use 4 equal Fraction Strips (FRAC-01) to visualize 25% quartiles.",
        "calc": "3. Calculator (SC-6): Clear with [g][CLΣ], enter data once with [Σ+] (or [FRQ]), and read [g][x̄], [f][MED], [g][MODE], [RNG], [f][1Q], [g][3Q], [IQR], and [g][MAD].",
    },
    10: {
        "concept": "1. Concept (Stack Approach): Two-step equations unwrap in reverse order of operations (undo ±b first, then ÷a second), and squaring a negative in X ([+/-][x²]) squares the entire signed value.",
        "blocks": "2. Blocks (Place Value, Fraction & Prime): Model zero pairs and 2-step balance with Place Value blocks (PLACE-01) and probability part-to-whole ratios with Fraction Strips (FRAC-01).",
        "calc": "3. Calculator (SC-6): Verify signed powers (5 [+/-][x²] = +25), check 2-step equations with [≠], and evaluate factorials [x!], combinations [f][nCr], and permutations [g][nPr].",
    },
}


def draw_coach_chapter_page(
    p: CanvasPage,
    ch: Dict[str, Any],
    total_chapters: int,
    master_page_num: Optional[int] = None,
) -> None:
    margin = 10.0
    uw = p.w - 2 * margin
    ch_num = ch["num"]
    clean_tools = clean_manipulative_label(ch["kit_summary"])
    triad = UNIT_COACH_TRIAD[ch_num]

    # 1. Top Chapter Header (y = 8.5 .. 22.8 mm)
    p.text(
        margin,
        11.6,
        f"PART II • MIDDLE SCHOOL CONCEPT & SECTION KEY (UNIT {ch_num:02d} OF 10)",
        size=2.1,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
    )
    p.draw_tutorial_keycap(margin + uw - 5.6, 8.6, w=4.8, h=4.0)
    p.text(margin, 17.2, f"Unit {ch_num}: {ch['title']} — Practice A & B Complete Key", size=4.15, bold=True, color=INK, max_w=uw - 10.0)
    p.text(margin, 21.3, f"{ch['big_ideas_book']}  •  Concept -> Blocks (When Applicable: {clean_tools}) -> Calculator", size=1.95, bold=True, color=SLATE, max_w=uw)
    p.line(margin, 22.6, margin + uw, 22.6, color=INK, width=0.45)

    # 2. Coaching Strip: 1. Concept (Stack) -> 2. Blocks (When Applicable) -> 3. Calculator (y = 23.4 .. 39.8 mm, height = 16.4 mm)
    p.rect(margin, 23.4, uw, 16.4, fill=SUBTLE_HDR, stroke=INK, r=0.9, line_w=0.28)
    p.rect(margin + uw - 25.5, 24.4, 24.0, 14.4, fill=WHITE, stroke=LIGHT_BORDER, r=0.6, line_w=0.2)
    p.image(ASSETS_MANUALS_DIR / ch["hero_png"], margin + uw - 25.0, 24.9, 23.0, 13.4)

    text_w = uw - 29.0
    p.para(
        margin + 2.2,
        26.0,
        triad["concept"],
        max_w=text_w,
        size=1.82,
        bold=True,
        color=INK,
        leading=1.14,
        max_lines=2,
    )
    p.para(
        margin + 2.2,
        31.2,
        triad["blocks"],
        max_w=text_w,
        size=1.80,
        color=SLATE,
        leading=1.14,
        max_lines=2,
    )
    p.para(
        margin + 2.2,
        36.4,
        triad["calc"],
        max_w=text_w,
        size=1.80,
        bold=True,
        color=TEAL_ACCENT,
        leading=1.14,
        max_lines=2,
    )

    # 3. Section-by-Section Complete Answer Key Bands (y = 41.0 .. 259.6 mm)
    #    Each section displays Practice A (#1-#10) on the Left Half and Practice B (#1-#10) on the Right Half!
    secs = ch["sections"]
    n_secs = len(secs)
    avail_h = 216.2
    sec_gap = 1.4
    sec_h = (avail_h - (n_secs - 1) * sec_gap) / n_secs

    for s_idx, sec in enumerate(secs):
        sec_num = sec["sec_num"]
        stitle = clean_section_title(sec_num, sec["title"])
        sy = 41.0 + s_idx * (sec_h + sec_gap)
        p.rect(margin, sy, uw, sec_h, fill=WHITE, stroke=INK, r=0.8, line_w=0.28)

        # Section Header Bar (4.6 mm tall)
        p.rect(margin, sy, uw, 4.6, fill=BAND_HDR, stroke=INK, r=0.6, line_w=0.25)
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
            color=INK,
            max_w=99.0,
        )
        p.text(
            margin + uw - 2.0,
            sy + 3.2,
            f"Methods: {compact_ways}",
            size=1.64,
            mono=True,
            color=SLATE,
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
                # --- Practice A cell (2 crisp, high-contrast lines instead of 3 microscopic lines) ---
                pa_prob = a_probs[p_idx]
                ax = margin + c * qcol_w
                pa_setup, pa_keys = parse_tutor_setup_and_keys(sec_num, pa_prob)
                pa_line1 = f"A{pa_prob['num']}: {pa_prob['ans']}"
                if pa_setup and pa_setup != pa_prob["ans"] and len(pa_prob["ans"]) + len(pa_setup) <= 58:
                    pa_line1 = f"A{pa_prob['num']}: {pa_prob['ans']}  ({pa_setup})"
                pa_keys_compact = pa_keys.replace("[ENTER]", "[ENT]")
                p.text(
                    ax + 1.3,
                    cy + row_h * 0.43,
                    pa_line1,
                    size=1.78,
                    bold=True,
                    color=INK,
                    max_w=qcol_w - 2.4,
                )
                p.text(
                    ax + 1.3,
                    cy + row_h * 0.85,
                    f"Check: {pa_keys_compact}",
                    size=1.60,
                    bold=False,
                    mono=False,
                    color=SLATE,
                    max_w=qcol_w - 2.4,
                )

                # --- Practice B cell (2 crisp, high-contrast lines instead of 3 microscopic lines) ---
                pb_prob = b_probs[p_idx]
                bx = margin + half_w + c * qcol_w
                pb_setup, pb_keys = parse_tutor_setup_and_keys(sec_num, pb_prob)
                pb_line1 = f"B{pb_prob['num']}: {pb_prob['ans']}"
                if pb_setup and pb_setup != pb_prob["ans"] and len(pb_prob["ans"]) + len(pb_setup) <= 58:
                    pb_line1 = f"B{pb_prob['num']}: {pb_prob['ans']}  ({pb_setup})"
                pb_keys_compact = pb_keys.replace("[ENTER]", "[ENT]")
                p.text(
                    bx + 1.3,
                    cy + row_h * 0.43,
                    pb_line1,
                    size=1.78,
                    bold=True,
                    color=INK,
                    max_w=qcol_w - 2.4,
                )
                p.text(
                    bx + 1.3,
                    cy + row_h * 0.85,
                    f"Check: {pb_keys_compact}",
                    size=1.60,
                    bold=False,
                    mono=False,
                    color=SLATE,
                    max_w=qcol_w - 2.4,
                )

    # 4. Bottom Strip: Unit Mastery Quiz Answer Key (Q1-Q10) & Standards (y = 258.2 .. 266.2 mm, h = 8.0 mm)
    q_meta = UNIT_QUIZZES_DATA[ch_num]
    q_probs = q_meta["problems"]
    q_bar_y = 258.2
    p.rect(margin, q_bar_y, uw, 8.0, fill=SUBTLE_HDR, stroke=TEAL_ACCENT, r=0.6, line_w=0.24)
    q_ans_line1 = "  ".join(f"Q{qp['num']}: {qp['ans']}" for qp in q_probs[:5])
    q_ans_line2 = "  ".join(f"Q{qp['num']}: {qp['ans']}" for qp in q_probs[5:10])
    p.text(
        margin + 2.0,
        q_bar_y + 3.1,
        f"UNIT {ch_num:02d} MASTERY QUIZ KEY (p.{111 + ch_num} • {q_meta['teks']}):  {q_ans_line1}",
        size=1.52,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=uw - 4.0,
    )
    p.text(
        margin + 2.0,
        q_bar_y + 6.5,
        f"Quiz Q6–Q10 Answers:  {q_ans_line2}",
        size=1.52,
        bold=True,
        mono=True,
        color=INK,
        max_w=uw - 4.0,
    )

    pg_lbl = str(master_page_num) if master_page_num is not None else f"Part II Page {ch_num} of {total_chapters}"
    p.text(
        margin,
        p.h - 8.2,
        f"STACKCALC MATHEMATICS  •  TEACHING WITH THE STACK (MIDDLE SCHOOL KEY • UNIT {ch_num:02d})",
        size=1.85,
        mono=True,
        color=MUTED,
        max_w=uw - 38.0,
    )
    p.text(margin + uw, p.h - 8.2, pg_lbl, size=2.1, bold=True, mono=True, color=INK, align="right")


def generate_coach_guide_pdf(chapters: List[Dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_path), pagesize=letter)
    c.setTitle("Teaching with the Stack: Middle School Coach & Solution Guide")
    c.setAuthor("StackCalc Learning Lab")

    total_ch = len(chapters)
    # Pages i–iv: Title Page (i), Copyright Page (ii), Table of Contents (iii), Preface (iv)
    draw_workbook_front_matter(c, chapters, is_coach=True)
    for ch in chapters:
        p = CanvasPage(c, letter)
        draw_coach_chapter_page(p, ch, total_ch + 2)
        c.showPage()
    draw_coach_guide_back_matter(c, chapters, total_ch)

    c.save()
    print(f"[OK] Built Spiral Coach Guide: {output_path} ({output_path.stat().st_size / 1024:.1f} KB, 16 total pages: pp. i-iv + 1-12)")


def generate_big_ideas_lulu_covers(chapters: List[Dict[str, Any]], out_dir: Path) -> None:
    """Generates Amazon KDP Full-Wrap Paperback Cover + Spine Spread PDF (and 2-page Front/Back Cover PDF) for Book 3 without ISBN barcodes."""
    out_dir.mkdir(parents=True, exist_ok=True)
    wb_kdp_cover = out_dir / "bigideas_middle_school_sc6_workbook_kdp_cover.pdf"
    generate_kdp_full_wrap_cover_pdf(wb_kdp_cover, "big_ideas", interior_pdf_path=STUDENT_PDF, default_pages=128)
    wb_cover = out_dir / "bigideas_middle_school_sc6_workbook_lulu_cover.pdf"
    generate_lulu_coil_cover_pdf(wb_cover, "big_ideas")
    print(f"[OK] Built KDP Full-Wrap & 2-Page Cover PDFs: {wb_kdp_cover.name}, {wb_cover.name}")


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

        unit_total_pages = 1 + len(ch["sections"]) * 2 + 2
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

        # Second-to-Last Page: 1-Page End-of-Unit Mastery Quiz
        pq = CanvasPage(c, letter)
        draw_unit_mastery_quiz_page(pq, ch, page_num, unit_total_pages)
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
    1: "[Place Value Studio (`PLACE-01`)](../products/place-value/index.md) &bull; [Prime Factor Studio (`PRIME-01`)](../products/prime-factor-studio/index.md)",
    2: "[84mm Fraction Comparator Studio (`FRAC-01`)](../products/fraction-studio/index.md) &bull; [Place Value Studio (`PLACE-01`)](../products/place-value/index.md)",
    3: "[84mm Fraction Studio (`FRAC-01`)](../products/fraction-studio/index.md) &bull; [Place Value Studio (`PLACE-01`)](../products/place-value/index.md)",
    4: "[Place Value Studio (`PLACE-01`)](../products/place-value/index.md) &bull; [Prime Factor Studio (`PRIME-01`)](../products/prime-factor-studio/index.md)",
    5: "[84mm Fraction Studio (`FRAC-01`)](../products/fraction-studio/index.md) &bull; [Place Value Studio (`PLACE-01`)](../products/place-value/index.md)",
    6: "[Place Value Studio (`PLACE-01`)](../products/place-value/index.md) &bull; [84mm Fraction Studio (`FRAC-01`)](../products/fraction-studio/index.md)",
    7: "[Place Value Studio (`PLACE-01`)](../products/place-value/index.md) &bull; [84mm Fraction Studio (`FRAC-01`)](../products/fraction-studio/index.md)",
    8: "[Place Value Studio (`PLACE-01`)](../products/place-value/index.md) &bull; [84mm Fraction Studio (`FRAC-01`)](../products/fraction-studio/index.md)",
    9: "[Place Value Studio (`PLACE-01`)](../products/place-value/index.md) &bull; [84mm Fraction Studio (`FRAC-01`)](../products/fraction-studio/index.md)",
    10: "[Place Value Studio (`PLACE-01`)](../products/place-value/index.md) &bull; [84mm Fraction Studio (`FRAC-01`)](../products/fraction-studio/index.md) &bull; [Prime Factor Studio (`PRIME-01`)](../products/prime-factor-studio/index.md)",
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
        "**Grade 6 Complete + Grade 7 Bridge • Title Page & Preface • 10 Unit Introductions • 45 Textbook Sections • 90 Printable Worksheets (Practice A & B) • 90 Multi-Way Worked Examples • 900 Practice Problems + 10 End-of-Unit Mastery Quizzes (100 Quiz Items) • 7 Reference Appendices (Answer Keys, Standards Crosswalk & Official 3D Block Studio Guides)**",
        "",
        "<div class=\"hero-buttons\" style=\"margin: 1.25rem 0 1.75rem 0;\">",
        "  <a href=\"../../downloads/worksheets/bigideas_middle_school_sc6_daily_student_workbook.pdf\" class=\"md-button md-button--primary\">📄 Download Complete Student Workbook PDF (128 Pages • pp. i–iv + 1–124)</a>",
        "  <a href=\"#print-individual-chapters-units-110-separate-pdfs-for-parents-teachers\" class=\"md-button\">🖨️ Print Individual Chapters (Units 1–10 Separate PDFs)</a>",
        "  <a href=\"../../downloads/worksheets/sc6_quest_token_scoring_guide.pdf\" class=\"md-button\">🏆 Download 1-Page Token Scoring & SC-6 Work-Check Guide PDF</a>",
        "  <a href=\"../../downloads/stackcalc-curriculum-guide-letter.pdf\" class=\"md-button\">🔑 Download Unified Master Teacher's Guide PDF (Includes Complete 900-Problem Worked Setups & Keys)</a>",
        "  <a href=\"../../downloads/worksheets/bigideas_middle_school_sc6_workbook_kdp_cover.pdf\" class=\"md-button\">🎨 Student Workbook KDP Paperback Full-Wrap Cover PDF</a>",
        "</div>",
        "",
        "!!! abstract \"Built for Students Who Need Extra Practice: Two Textbook Ways, Hands-On Block Models & 100-Point Daily Goal\"",
        "    - **Relatable Real-World Stories & Honest Student Perspectives:** Every Unit and lesson connects the math to real-world situations—from packing drone batteries, building skate ramps, and comparing bicycle gear sprockets to engineering workshops, Antarctic penguin huddles, and wildlife puzzles—showing how students who initially doubt themselves discover why each mathematical concept works.",
        "    - **100% Focused on How *Big Ideas Math* Teaches & Tests Each Concept:** Every section tracks the exact paper-and-pencil algorithms, conceptual models, and vocabulary (*dividend, divisor, quotient, prime factorization, GCF, LCM, reciprocal, tape diagram, ratio table, unit rate, equivalent expressions, Distributive Property, inverse operations, net, interquartile range (IQR), mean absolute deviation (MAD)*) that students are tested on in school.",
        "    - **2 or 3 Authentic Textbook Ways & 100-Point Daily Goal:** Every Worked Example explicitly teaches the **distinct textbook solution pathways from *Big Ideas Math*** (`WAY 1`, `WAY 2`, and `WAY 3` where applicable). Students reach the **100-Point Daily Goal** either by solving **any 5 problems in 2 Ways (`5 × 20 = 100 pts`)** OR **all 10 problems in 1 Way (`10 × 10 = 100 pts`)**.",
        "    - **Warm-Up Step 1 Starter Scaffolds (`#1–#2`), Common-Trap Alerts & Graphic Organizers:** Every worksheet includes a section-specific **`⚠️ WATCH OUT:`** misconception alert, a 1-line **Starter Step 1** prompt on Problems `#1–#2` to eliminate blank-page anxiety, and faint ready-to-use graphic organizers (number lines, ratio tables, mini coordinate grids, Venn diagrams, and box-plot axes) right inside the problem cards.",
        "    - **10 Unscaffolded End-of-Unit Mastery Quizzes & Official 3D Block Studio Guides:** Appendix F (`pp. 112–121`) includes a 1-page Summative Unit Mastery Quiz (`10 problems / 100 points`) for every unit, while Appendix G (`pp. 122–124`) provides the Quiz Answer Keys, State Standards Crosswalk (`CCSS • Texas TEKS • Florida B.E.S.T.`), and Official 3D Manipulative Block Studio & Hardware Guides (`PLACE-01`, `FRAC-01`, `PRIME-01`, `SC-6`, `SC-32`).",
        "    - **The StackCalc Library Print Edition on Amazon, Complete 128-Page PDF, or Individual Chapter Packets:** Available in **Paperback as part of *The StackCalc Library* on Amazon** (including Front Matter `pp. i–iv` and Reference `Appendices A–G` on `pp. 103–124`), as a complete downloadable PDF, or as **10 standalone Chapter/Unit PDFs below** (11–13 pages each).",
        "",
        "---",
        "",
        "## 🖨️ Print Individual Chapters (Units 1–10 Separate PDFs for Parents & Teachers)",
        "",
        "Don't want to print all 127 pages at once? Each standalone **Chapter Packet PDF** below contains that unit's **1-Page Real-World Story & Concept Opener**, all **Practice A & Practice B Section Worksheets** (`20 problems per section`), the **1-Page Unscaffolded End-of-Unit Mastery Quiz**, and the **1-Page Parent & Teacher Coach Answer Key** at the back of the packet.",
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
        unit_pages = 1 + n_ws + 2
        unit_pdf_md = f"../downloads/worksheets/bigideas_middle_school_sc6_unit_{ch_num:02d}.pdf"
        book_ref = UNIT_BOOK_REFS.get(ch_num, "[SC-6 Elementary Manual](../manuals/sc6/index.md)")
        prod_links = UNIT_PRODUCT_LINKS.get(ch_num, "[Manipulative Kits](../products/curriculum-and-decks.md)")
        lines.append(
            f"| **[Unit {ch_num}](#unit-{ch_num})** | **{ch['title']}**<br>*{ch['big_ideas_book']}* | {sec_range}<br>(`{n_ws} Worksheets • {n_probs} Problems + Quiz`) | {book_ref}<br>**Blocks:** {prod_links} | [**📄 Print Unit {ch_num} PDF ({unit_pages} pp.)**]({unit_pdf_md}) |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 🏆 How the 100-Point Two-Method Mastery System Works",
        "",
        "Every worksheet encourages students to master two independent solution methods and verify their work on the stack calculator:",
        "",
        "| Mastery Step | Points Earned | How Two-Method Verification Works |",
        "| :--- | :--- | :--- |",
        "| **1. Solve in Your 1st Textbook Way** | **`+10 Points`** | Solve a problem by hand in the open workspace using the first textbook method (`WAY 1`) and check off `[x] +10 (1 Way)`. |",
        "| **2. Verify with a 2nd Textbook Way** | **`+20 Points (Double)`** | Solve the same problem using a second independent textbook method (`WAY 2` or a hands-on block model) and check off `[x] +20 (2 Ways)`. |",
        "| **3. Reach the 100-Point Daily Goal** | **`100 Points`** | Reach **100 points** either by solving **any 5 problems in 2 Ways (`5 × 20 = 100 pts`)** OR **all 10 problems in 1 Way (`10 × 10 = 100 pts`)**, then verify your answers using the section's **SC-6 Calculator Work-Check** box. |",
        "",
        "---",
        "",
    ])

    for ch in chapters:
        ch_num = ch["num"]
        unit_story_pg = 3 + (ch_num - 1) + (ch["sections"][0]["day_num"] - 1) * 2
        story = UNIT_STORIES[ch_num]
        n_ws = len(ch["sections"]) * 2
        unit_pages = 1 + n_ws + 2
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
        lines.append(f"- **Hands-On Block Kits (When Applicable — `{ch['kit_summary']}`):** {prod_links}")
        lines.append(f"- **Aligned *From Blocks to the Stack* Story & Chapter:** {book_ref}")
        lines.append(f"- **Target Misconception:** {ch['coach_misconception']}")
        lines.append(f"- **Hands-On & Stack Remediation:** {ch['coach_remediation']}")
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
    generate_big_ideas_lulu_covers(CHAPTERS_DATA, OUT_DIR)
    generate_chapter_pdfs(CHAPTERS_DATA, OUT_DIR)
    sync_curriculum_markdown(CHAPTERS_DATA, SOURCE_MD)


if __name__ == "__main__":
    main()
