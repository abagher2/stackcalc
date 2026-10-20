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

from big_ideas_sc6_pedagogy import SECTION_PEDAGOGY
from big_ideas_sc6_sections_data import CHAPTERS_DATA
from big_ideas_sc6_sheet_b_data import (
    MULTI_METHOD_BLOCK_NOTES,
    SHEET_B_PROBLEMS,
    clean_section_title,
    clean_sheet_a_prompt,
)

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
    """Normalizes any Unicode glyphs outside SpaceMono/Arial to 100% supported glyphs."""
    if not txt:
        return ""
    s = txt
    replacements = {
        "★★": "[+20 FAST]",
        "★": "*",
        "x⇄y": "x↔y",
        "⇄": "↔",
        "▸": "->",
        "yˣ": "y^x",
        "ˣ√y": "x√y",
        "ˣ": "^x",
        "⁴": "^4",
        "⁵": "^5",
        "⁶": "^6",
        "ⁿ": "^n",
        "₁": "1",
        "₂": "2",
        "₃": "3",
        "≟": "=",
        "x̄": "x-bar",
        "X̄": "x-bar",
    }
    for k, v in replacements.items():
        s = s.replace(k, v)
    return s


class CanvasPage:
    """Millimeter-calibrated ReportLab canvas helper (top-down Y coordinates in mm)."""

    def __init__(self, c: canvas.Canvas, size: Tuple[float, float] = letter):
        self.c = c
        self.w = size[0] / mm
        self.h = size[1] / mm

    def _pick_font(self, txt: str, bold: bool, italic: bool, mono: bool) -> str:
        if mono and "Σ" not in txt and "π" not in txt:
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
        if max_w is not None:
            s = self.fit_text(s, max_w, size, bold=bold, italic=italic, mono=mono)
        font = self._pick_font(s, bold, italic, mono)
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
        lines: List[str] = []
        for raw_ln in s.split("\n"):
            wrapped = simpleSplit(raw_ln, font, size * mm, max_w * mm)
            lines.extend(wrapped if wrapped else [""])
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
        """Draws the SC-6 Tutorial left-shift label: ONLY the Question Mark in a Circle (?)."""
        self.rect(x, y, w, h, fill=WHITE, stroke=INK, r=0.75, line_w=0.28)
        cx = x + w / 2.0
        cy = y + h / 2.0
        r_circ = min(w, h) * 0.34
        self.circle(cx, cy, r_circ, fill=WHITE, stroke=INK, line_w=0.28)
        self.text(cx, cy + r_circ * 0.56, "?", size=r_circ * 1.45, bold=True, mono=True, color=INK, align="center")
        return w

    def draw_keycap(self, label: str, x: float, y: float, h: float = 3.6) -> float:
        """Draws a crisp hardware calculator keycap squircle with full glyph support."""
        raw_lbl = label.strip()
        if raw_lbl in ("?", "[?]", "C?"):
            return self.draw_tutorial_keycap(x, y, w=h * 1.2, h=h)
        is_xbar = raw_lbl == "x̄"
        lbl = "x" if is_xbar else clean_pdf_text(raw_lbl)
        char_len = len(lbl)
        w = max(h * 1.12, char_len * 1.62 + 2.1)
        if lbl.upper() in ("ENTER", "LASTX", "FDISP", "PRIME", "PRISM", "%CHG"):
            w = max(w, h * 1.65)

        if lbl in ("f",):
            bg, fg, border = "#D97706", "#FFFFFF", "#92400E"
        elif lbl in ("g",):
            bg, fg, border = "#0284C7", "#FFFFFF", "#075985"
        elif lbl.upper() in ("ENTER", "+", "-", "×", "÷", "+/-"):
            bg, fg, border = "#1E293B", "#FFFFFF", "#0F172A"
        elif lbl.replace(".", "").replace("-", "").isdigit():
            bg, fg, border = "#FFFFFF", "#0F172A", "#475569"
        else:
            bg, fg, border = "#F1F5F9", "#0F172A", "#334155"

        self.rect(x, y, w, h, fill=bg, stroke=border, r=0.7, line_w=0.24)
        fsize = min(h * 0.48, (w - 0.85) / max(1, char_len) * 1.35)
        self.text(x + w / 2.0, y + h * 0.71, lbl, size=fsize, bold=True, mono=True, color=fg, align="center")
        if is_xbar:
            self.line(x + w / 2.0 - 0.85, y + h * 0.28, x + w / 2.0 + 0.85, y + h * 0.28, color=fg, width=0.26)
        return w

    def draw_keycap_sequence(
        self,
        keys: List[str],
        x: float,
        y: float,
        max_w: float,
        h: float = 3.5,
        gap: float = 0.75,
    ) -> float:
        if len(keys) > 10:
            h = 3.1
            gap = 0.55
        elif len(keys) > 8:
            h = 3.3
            gap = 0.65
        cur_x = x
        cur_y = y
        for k in keys:
            lbl = clean_pdf_text(k.strip())
            est_w = max(h * 1.12, len(lbl) * 1.62 + 2.1)
            if cur_x + est_w > x + max_w and cur_x > x:
                cur_x = x
                cur_y += h + 0.8
            kw = self.draw_keycap(k, cur_x, cur_y, h=h)
            cur_x += kw + gap
        return cur_y + h

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
            self.text(x + w / 2.0, y + 4.0, f"Input: {num_str}", size=2.0, bold=True, mono=True, color=INK, align="center")
            bw = (w - 5.6) / 2.0
            self.rect(x + 1.8, y + 6.0, bw, 13.6, fill="#F1F5F9", stroke=INK, r=0.8, line_w=0.25)
            self.text(x + 1.8 + bw / 2.0, y + 9.8, "M1: Whole", size=1.7, bold=True, color=SLATE, align="center")
            self.text(x + 1.8 + bw / 2.0, y + 14.2, ip_str, size=2.0, bold=True, mono=True, color=INK, align="center", max_w=bw - 1.5)
            self.text(x + 1.8 + bw / 2.0, y + 17.8, "[f] [IP]", size=1.65, mono=True, color=MUTED, align="center")

            rx = x + 3.8 + bw
            self.rect(rx, y + 6.0, bw, 13.6, fill="#E2E8F0", stroke=INK, r=0.8, line_w=0.25)
            self.text(rx + bw / 2.0, y + 9.8, "M2: Decimal", size=1.7, bold=True, color=TEAL_ACCENT, align="center")
            self.text(rx + bw / 2.0, y + 14.2, fp_str, size=2.0, bold=True, mono=True, color=INK, align="center", max_w=bw - 1.5)
            self.text(rx + bw / 2.0, y + 17.8, "[g] [FP]", size=1.65, mono=True, color=MUTED, align="center")

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
            self.text(x + w / 2.0, y + 18.0, "M1: Sort Shapes | M2: Sub x", size=1.7, bold=True, color=SLATE, align="center")
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
            self.text(cx, y + 21.8, "M1: Base-60 | M2: [f][CLK]", size=1.72, bold=True, mono=True, color=INK, align="center")

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
            "1. AUTHENTIC BIG IDEAS METHODS",
            "Every worksheet uses the exact vocabulary and two core methods taught in Big Ideas Math: Factor Trees & Division Ladders, LCD Fraction Towers & Reciprocals, Tape Diagrams & Ratio Tables, Area Models & Balance Scales.",
        ),
        (
            "2. TWO WAYS = DOUBLE POINTS (+20)",
            "Every Worked Example models TWO ways to solve: Method 1 (+10 pts — 1st Token) and Method 2 (+20 pts DOUBLE — 2nd Token) alongside step-by-step physical Block Kit instructions and SC-6 verification.",
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
        "HANDS-ON MANIPULATIVE BLOCK KITS & SIMPLIFIED 2-PIECE QUEST-01 SCOREBOARD (+10 / +20 TOKENS)",
        size=2.2,
        bold=True,
        mono=True,
        color=INK,
    )
    p.draw_tutorial_keycap(margin + uw - 7.6, 60.6, w=4.6, h=4.0)
    showcase = [
        ("counting_tiles_array_3x8.png", "COUNT-01: Array Tiles"),
        ("prime_lcm_gcd_venn.png", "PRIME-01: Prime Towers"),
        ("fraction_studio_common_denominator.png", "FRAC-01: 84mm Fractions"),
        ("algebra_factoring_area.png", "ALGB-01: Algebra Stage"),
        ("planetary_geared_clock_330.png", "TIME-01: Geared Clock"),
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
        2: "LCD Towers vs Cross-Mult; Reciprocals",
        3: "Tape Diagrams vs Ratio Tables & Rates",
        4: "Substitution, Like Terms & Area vs GCF",
        5: "Cut-and-Slide Grids vs Polygon Formulas",
        6: "Number Lines vs Opposites & |x| Sums",
        7: "Mental Inspection vs Inverse Operations",
        8: "Unfolded 2D Nets vs Prism/Cone Formulas",
        9: "Fair-Share Leveling vs IQR & MAD Sums",
        10: "Zero-Pair Chips vs Rules & Sample Space",
    }
    row_h = 16.2
    for idx, ch in enumerate(chapters):
        ry = ty + 6.0 + idx * row_h
        bg = WHITE if idx % 2 == 0 else SUBTLE_HDR
        p.rect(margin, ry, uw, row_h, fill=bg, stroke=LIGHT_BORDER, line_w=0.2)
        p.line(margin + 70.0, ry, margin + 70.0, ry + row_h, color=LIGHT_BORDER, width=0.2)
        p.line(margin + 142.0, ry, margin + 142.0, ry + row_h, color=LIGHT_BORDER, width=0.2)

        p.text(margin + 2.2, ry + 4.3, f"Unit {ch['num']}: {ch['title']}", size=2.3, bold=True, color=INK, max_w=66.0)
        p.para(margin + 2.2, ry + 7.8, f"{ch['big_ideas_book']} • {ch['kit_summary']}", max_w=66.0, size=1.9, color=SLATE, max_lines=2)

        for li, s in enumerate(ch["sections"]):
            pg_a = 2 + (s["day_num"] - 1) * 2
            pg_b = pg_a + 1
            stitle = clean_section_title(s["sec_num"], s["title"])
            sl = f"[ ] Sec {s['sec_num']} (pp.{pg_a}-{pg_b}): {stitle}"
            p.text(margin + 71.5, ry + 3.4 + li * 2.9, sl, size=1.82, color=INK, max_w=69.0)

        m_sum = unit_methods_summary.get(ch["num"], "")
        n_probs = len(ch["sections"]) * 20
        p.text(margin + 143.5, ry + 5.0, m_sum, size=1.85, bold=True, color=INK, max_w=46.0)
        p.text(margin + 143.5, ry + 9.4, f"Kit: {ch['kit_summary'].split('+')[0].strip()}", size=1.78, mono=True, color=SLATE, max_w=46.0)
        p.text(margin + 143.5, ry + 13.7, f"[ ] {len(ch['sections'])*2} Sheets ({n_probs} Problems)", size=1.82, bold=True, color=TEAL_ACCENT)

    p.text(
        margin,
        p.h - 6.0,
        "StackCalc Learning Systems  •  Big Ideas Math Middle School Supplement (10 Units • 45 Sections • 90 Worksheets • 900 Problems)",
        size=2.0,
        mono=True,
        color=MUTED,
    )
    p.text(margin + uw, p.h - 6.0, "Page 1 of 91", size=2.0, bold=True, mono=True, color=INK, align="right")


def draw_student_section_page_a(p: CanvasPage, ch: Dict[str, Any], sec: Dict[str, Any], page_num: int, total_pages: int) -> None:
    """Renders Worksheet A for a section: Key Ideas, Step-by-Step Blocks, 2-Method Worked Example, and 10 Clean Problems."""
    margin = 11.0
    uw = p.w - 2 * margin
    sec_num = sec["sec_num"]
    stitle = clean_section_title(sec_num, sec["title"])
    ped = SECTION_PEDAGOGY[sec_num]

    # 1. Clean Textbook Header (y = 9.0 .. 24.8 mm)
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
    kit_badge = f"BLOCK KIT: {sec['kit_id']} • {sec['kit_name']}"
    p.rect(margin + uw - 70.0, 9.0, 70.0, 4.6, fill=SUBTLE_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(margin + uw - 35.0, 12.1, kit_badge, size=1.82, bold=True, mono=True, color=INK, align="center", max_w=67.0)

    p.text(margin, 18.2, f"Section {sec_num} — Practice A: {stitle}", size=4.0, bold=True, color=INK, max_w=uw)

    p.text(
        margin,
        23.2,
        f"Key Vocabulary: {ped['key_vocab']}",
        size=1.92,
        bold=True,
        color=SLATE,
        max_w=115.0,
    )
    p.text(
        margin + uw,
        23.2,
        "Name: ______________________   Date: __________   Score: ____ / 10",
        size=1.92,
        bold=True,
        color=INK,
        align="right",
    )
    p.line(margin, 24.8, margin + uw, 24.8, color=INK, width=0.45)

    # 2. Top Instruction & Worked Example Band (y = 26.0 .. 83.5 mm, height = 57.5 mm)
    left_w = 90.0
    right_w = uw - left_w - 2.5
    right_x = margin + left_w + 2.5
    band_y = 26.0
    band_h = 57.5

    # --- LEFT PANEL: Block Kit & Two-Method Physical Demonstration ---
    bm = MULTI_METHOD_BLOCK_NOTES[sec_num]
    p.rect(margin, band_y, left_w, band_h, fill=WHITE, stroke=INK, r=1.0, line_w=0.3)
    p.rect(margin, band_y, left_w, 4.8, fill=INK, stroke=INK, r=0.8, line_w=0.2)
    p.text(
        margin + 2.4,
        band_y + 3.4,
        f"BLOCK KIT: 2 WAYS TO BUILD IT ({sec['kit_id']}: {sec['kit_name'].upper()})",
        size=1.82,
        bold=True,
        mono=True,
        color=WHITE,
        max_w=left_w - 4.8,
    )

    img_box_x = margin + 2.0
    img_box_y = band_y + 5.6
    img_box_w = 39.0
    img_box_h = 24.2
    p.rect(img_box_x, img_box_y, img_box_w, img_box_h, fill=WHITE, stroke=LIGHT_BORDER, r=0.8, line_w=0.2)
    p.image(ASSETS_MANUALS_DIR / sec["asset_png"], img_box_x + 0.8, img_box_y + 0.8, img_box_w - 1.6, img_box_h - 1.6)

    sch_x = img_box_x + img_box_w + 1.5
    sch_w = left_w - img_box_w - 5.5
    p.draw_block_schematic(sec["diagram_type"], sec["diagram_data"], sch_x, img_box_y, sch_w, img_box_h)

    steps_box_y = band_y + 30.6
    steps_box_h = band_h - 32.0
    p.rect(margin + 2.0, steps_box_y, left_w - 4.0, steps_box_h, fill=SUBTLE_HDR, stroke=BORDER, r=0.8, line_w=0.22)
    p.text(
        margin + 3.5,
        steps_box_y + 3.1,
        f"DEMONSTRATE BOTH METHODS WITH {sec['kit_id']} BLOCKS:",
        size=1.78,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=left_w - 7.0,
    )
    sy_cur = steps_box_y + 5.9
    block_demo_lines = [
        (bm["block_m1"], True, INK),
        (bm["block_m2"], True, TEAL_ACCENT),
        (bm["block_compare"], False, SLATE),
    ]
    for btext, bbold, bcol in block_demo_lines:
        sy_cur = p.para(
            margin + 3.5,
            sy_cur,
            btext,
            max_w=left_w - 7.0,
            size=1.82,
            bold=bbold,
            color=bcol,
            leading=1.15,
            max_lines=2,
        )
        sy_cur += 0.38

    # --- RIGHT PANEL: Two-Method Worked Example (+10 pts vs. +20 pts Double Points) ---
    ex1 = sec["examples"][0]
    p.rect(right_x, band_y, right_w, band_h, fill=WHITE, stroke=INK, r=1.0, line_w=0.3)
    p.rect(right_x, band_y, right_w, 4.8, fill=SUBTLE_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(
        right_x + 2.5,
        band_y + 3.4,
        "WORKED EXAMPLE — 2 TEXTBOOK WAYS FOR DOUBLE POINTS (+20)",
        size=1.85,
        bold=True,
        mono=True,
        color=INK,
        max_w=right_w - 10.0,
    )
    p.draw_tutorial_keycap(right_x + right_w - 5.8, band_y + 0.55, w=4.4, h=3.7)

    # Problem Statement
    p.para(
        right_x + 2.6,
        band_y + 7.8,
        f"Problem: {ex1['problem']}",
        max_w=right_w - 5.2,
        size=2.12,
        bold=True,
        color=INK,
        leading=1.16,
        max_lines=2,
    )

    # Method 1 Box (+10 pts — 1st Token)
    m1_y = band_y + 13.6
    m1_h = 13.4
    p.rect(right_x + 2.2, m1_y, right_w - 4.4, m1_h, fill=M1_BG, stroke=BORDER, r=0.7, line_w=0.22)
    m1_hdr = ped["ex1_m1_title"].replace("METHOD 1 (+10 pts):", "METHOD 1 (+10 pts — 1st Token):")
    p.text(
        right_x + 3.8,
        m1_y + 3.1,
        m1_hdr,
        size=1.82,
        bold=True,
        color=INK,
        max_w=right_w - 7.6,
    )
    p.para(
        right_x + 3.8,
        m1_y + 6.0,
        ped["ex1_m1_steps"],
        max_w=right_w - 7.6,
        size=1.82,
        color=SLATE,
        leading=1.16,
        max_lines=3,
    )

    # Method 2 Box (+20 pts DOUBLE — 2nd Token)
    m2_y = band_y + 28.0
    m2_h = 13.4
    p.rect(right_x + 2.2, m2_y, right_w - 4.4, m2_h, fill=M2_BG, stroke=TEAL_ACCENT, r=0.7, line_w=0.24)
    m2_hdr = ped["ex1_m2_title"].replace("METHOD 2 (+20 pts DOUBLE):", "METHOD 2 (+20 pts DOUBLE — 2nd Token):")
    p.text(
        right_x + 3.8,
        m2_y + 3.1,
        m2_hdr,
        size=1.82,
        bold=True,
        color=TEAL_ACCENT,
        max_w=right_w - 7.6,
    )
    p.para(
        right_x + 3.8,
        m2_y + 6.0,
        ped["ex1_m2_steps"],
        max_w=right_w - 7.6,
        size=1.82,
        color=INK,
        leading=1.16,
        max_lines=3,
    )

    # SC-6 Keystrokes
    ky = band_y + 42.6
    p.text(right_x + 2.6, ky + 2.6, "SC-6 Keystrokes:", size=1.88, bold=True, mono=True, color=INK)
    p.draw_keycap_sequence(ex1["keys"], right_x + 25.5, ky + 0.1, max_w=right_w - 28.0, h=3.45, gap=0.7)

    # Final Answer Bar
    bar_y = band_y + band_h - 6.8
    p.line(right_x + 2.2, bar_y, right_x + right_w - 2.2, bar_y, color=INK, width=0.25)
    p.text(
        right_x + 2.6,
        bar_y + 4.3,
        f"Answer: {ex1['ans']}",
        size=2.15,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=right_w * 0.56,
    )
    p.text(
        right_x + right_w - 2.6,
        bar_y + 4.3,
        "1 Method = +10 pts  |  Both Methods = +20 pts!",
        size=1.75,
        bold=True,
        color=SLATE,
        align="right",
        max_w=right_w * 0.43,
    )

    # 3. Practice A Grid (y = 84.8 .. 269.0 mm, 10 Clean Textbook Problems in 5 Rows × 2 Columns)
    hdr_y = 84.8
    p.rect(margin, hdr_y, uw, 4.6, fill=INK, stroke=INK, r=0.7, line_w=0.2)
    p.text(
        margin + 2.5,
        hdr_y + 3.2,
        f"SECTION {sec_num} PRACTICE A — SOLVE USING METHOD 1 (+10 PTS) OR BOTH METHODS (+20 PTS DOUBLE)",
        size=1.9,
        bold=True,
        mono=True,
        color=WHITE,
    )
    p.text(
        margin + uw - 2.5,
        hdr_y + 3.2,
        f"Methods: {ped['big_ideas_method']}",
        size=1.75,
        mono=True,
        color="#E2E8F0",
        align="right",
        max_w=78.0,
    )

    grid_y0 = 90.5
    col_w = (uw - 3.0) / 2.0
    row_h = 34.6
    row_gap = 1.15

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

        # Clean textbook prompt directly at top of card — zero boilerplate header line!
        cleaned_prompt = clean_sheet_a_prompt(sec_num, p_num, prob["prompt"])
        p.para(
            px + 8.2,
            py + 4.4,
            cleaned_prompt,
            max_w=col_w - 10.2,
            size=2.12,
            bold=True,
            color=INK,
            leading=1.18,
            max_lines=3,
        )

        # Clean, unobstructed open workspace for working out the problem!
        p.text(
            px + col_w - 2.4,
            py + row_h - 1.8,
            "Ans: ____________________________",
            size=1.95,
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
    """Renders Worksheet B for a section: Modeling Real Life 2-Method Worked Example + 10 Engaging Real-World Applications."""
    margin = 11.0
    uw = p.w - 2 * margin
    sec_num = sec["sec_num"]
    stitle = clean_section_title(sec_num, sec["title"])
    ped = SECTION_PEDAGOGY[sec_num]
    bm = MULTI_METHOD_BLOCK_NOTES[sec_num]
    ex2 = ped["ex2"]
    b_probs = SHEET_B_PROBLEMS[sec_num]

    # 1. Clean Textbook Header (y = 9.0 .. 24.8 mm)
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
    kit_badge = f"BLOCK KIT: {sec['kit_id']} • {sec['kit_name']}"
    p.rect(margin + uw - 70.0, 9.0, 70.0, 4.6, fill=SUBTLE_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(margin + uw - 35.0, 12.1, kit_badge, size=1.82, bold=True, mono=True, color=INK, align="center", max_w=67.0)

    p.text(margin, 18.2, f"Section {sec_num} — Practice B: Modeling Real Life ({stitle})", size=3.85, bold=True, color=INK, max_w=uw)

    p.text(
        margin,
        23.2,
        f"Textbook Methods: {ped['big_ideas_method']}",
        size=1.92,
        bold=True,
        color=SLATE,
        max_w=115.0,
    )
    p.text(
        margin + uw,
        23.2,
        "Name: ______________________   Date: __________   Score: ____ / 10",
        size=1.92,
        bold=True,
        color=INK,
        align="right",
    )
    p.line(margin, 24.8, margin + uw, 24.8, color=INK, width=0.45)

    # 2. Top Modeling Real Life Two-Method Worked Example (y = 26.0 .. 67.5 mm, height = 41.5 mm)
    band_y = 26.0
    band_h = 41.5
    p.rect(margin, band_y, uw, band_h, fill=WHITE, stroke=INK, r=1.0, line_w=0.3)
    p.rect(margin, band_y, uw, 4.8, fill=SUBTLE_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(
        margin + 2.5,
        band_y + 3.4,
        f"MODELING REAL LIFE WORKED EXAMPLE — {ex2['title'].upper()} (SOLVE 2 WAYS = +20 PTS DOUBLE)",
        size=1.88,
        bold=True,
        mono=True,
        color=INK,
        max_w=uw - 10.0,
    )
    p.draw_tutorial_keycap(margin + uw - 5.8, band_y + 0.55, w=4.4, h=3.7)

    # Real-Life Problem Statement
    p.para(
        margin + 2.6,
        band_y + 7.8,
        f"Problem: {ex2['problem']}",
        max_w=uw - 5.2,
        size=2.12,
        bold=True,
        color=INK,
        leading=1.18,
        max_lines=2,
    )

    # Side-by-Side Method 1 (+10 pts) & Method 2 (+20 pts DOUBLE) with explicit Block Kit builds for BOTH methods
    half_w = (uw - 6.8) / 2.0
    m_box_y = band_y + 13.6
    m_box_h = 19.2

    # Left Half: Method 1 (+10 pts — 1st Token) + Block Kit Way 1
    p.rect(margin + 2.2, m_box_y, half_w, m_box_h, fill=M1_BG, stroke=BORDER, r=0.7, line_w=0.22)
    m1_b_hdr = ex2["m1_title"].replace("METHOD 1 (+10 pts):", "METHOD 1 (+10 pts — 1st Token):")
    p.text(
        margin + 3.8,
        m_box_y + 3.2,
        m1_b_hdr,
        size=1.82,
        bold=True,
        color=INK,
        max_w=half_w - 3.2,
    )
    after_m1 = p.para(
        margin + 3.8,
        m_box_y + 6.0,
        ex2["m1_steps"],
        max_w=half_w - 3.2,
        size=1.80,
        color=SLATE,
        leading=1.15,
        max_lines=3,
    )
    p.para(
        margin + 3.8,
        max(after_m1 + 0.45, m_box_y + 12.8),
        bm["ex2_block_m1"],
        max_w=half_w - 3.2,
        size=1.74,
        italic=True,
        color=TEAL_ACCENT,
        leading=1.13,
        max_lines=2,
    )

    # Right Half: Method 2 (+20 pts DOUBLE — 2nd Token) + Block Kit Way 2
    m2_x = margin + 4.6 + half_w
    p.rect(m2_x, m_box_y, half_w, m_box_h, fill=M2_BG, stroke=TEAL_ACCENT, r=0.7, line_w=0.24)
    m2_b_hdr = ex2["m2_title"].replace("METHOD 2 (+20 pts DOUBLE):", "METHOD 2 (+20 pts DOUBLE — 2nd Token):")
    p.text(
        m2_x + 1.6,
        m_box_y + 3.2,
        m2_b_hdr,
        size=1.82,
        bold=True,
        color=TEAL_ACCENT,
        max_w=half_w - 3.2,
    )
    after_m2 = p.para(
        m2_x + 1.6,
        m_box_y + 6.0,
        ex2["m2_steps"],
        max_w=half_w - 3.2,
        size=1.80,
        color=INK,
        leading=1.15,
        max_lines=3,
    )
    p.para(
        m2_x + 1.6,
        max(after_m2 + 0.45, m_box_y + 12.8),
        bm["ex2_block_m2"],
        max_w=half_w - 3.2,
        size=1.74,
        italic=True,
        color=TEAL_ACCENT,
        leading=1.13,
        max_lines=2,
    )

    # Bottom Bar: SC-6 Keystrokes (left) + Final Answer (right)
    ky = band_y + 34.0
    p.text(margin + 2.6, ky + 2.7, "SC-6 Keystrokes:", size=1.88, bold=True, mono=True, color=INK)
    p.draw_keycap_sequence(ex2["keys"], margin + 25.5, ky + 0.2, max_w=92.0, h=3.45, gap=0.7)
    p.text(
        margin + uw - 2.6,
        ky + 2.8,
        f"Answer: {ex2['ans']}",
        size=2.05,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        align="right",
        max_w=85.0,
    )

    # 3. Practice B Application Grid (y = 69.0 .. 269.0 mm, 10 Engaging Applications in 5 Rows × 2 Columns)
    hdr_y = 69.0
    p.rect(margin, hdr_y, uw, 4.6, fill=INK, stroke=INK, r=0.7, line_w=0.2)
    p.text(
        margin + 2.5,
        hdr_y + 3.2,
        f"SECTION {sec_num} PRACTICE B — MODELING REAL LIFE & MULTI-METHOD APPLICATIONS",
        size=1.9,
        bold=True,
        mono=True,
        color=WHITE,
    )
    p.text(
        margin + uw - 2.5,
        hdr_y + 3.2,
        "1 Way = +10 pts  |  2 Ways = +20 pts Double",
        size=1.75,
        mono=True,
        color="#E2E8F0",
        align="right",
        max_w=76.0,
    )

    grid_y0 = 74.8
    col_w = (uw - 3.0) / 2.0
    row_h = 37.8
    row_gap = 1.15

    for idx, prob in enumerate(b_probs[:10]):
        r = idx // 2
        c = idx % 2
        px = margin + c * (col_w + 3.0)
        py = grid_y0 + r * (row_h + row_gap)

        p.rect(px, py, col_w, row_h, fill=WHITE, stroke=SLATE, r=0.9, line_w=0.28)

        p_num = prob["num"]
        p.rect(px + 2.0, py + 1.8, 5.0, 4.4, fill=TEAL_ACCENT, stroke=TEAL_ACCENT, r=0.65, line_w=0.2)
        p.text(px + 4.5, py + 4.8, str(p_num), size=2.15, bold=True, mono=True, color=WHITE, align="center")

        p.para(
            px + 8.2,
            py + 4.4,
            prob["prompt"],
            max_w=col_w - 10.2,
            size=2.08,
            bold=True,
            color=INK,
            leading=1.18,
            max_lines=3,
        )

        p.text(
            px + col_w - 2.4,
            py + row_h - 1.8,
            "Ans: ____________________________",
            size=1.95,
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


def generate_student_workbook_pdf(chapters: List[Dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_path), pagesize=letter)
    c.setTitle("StackCalc SC-6 Big Ideas Math Middle School Section-by-Section Supplement Workbook (90 Worksheets)")
    c.setAuthor("StackCalc Learning Lab")

    total_secs = sum(len(ch["sections"]) for ch in chapters)
    total_pages = 1 + total_secs * 2

    p = CanvasPage(c, letter)
    draw_student_cover_page(p, chapters)
    c.showPage()

    page_num = 2
    for ch in chapters:
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

    c.save()
    print(f"[OK] Built Student Supplement Workbook: {output_path} ({output_path.stat().st_size / 1024:.1f} KB, {page_num - 1} pages)")


# =============================================================================
# 2. COMPACT 10-PAGE COACH & SOLUTION GUIDE (EXACTLY 1 Page Per Chapter!)
# =============================================================================
def draw_coach_chapter_page(p: CanvasPage, ch: Dict[str, Any], total_chapters: int) -> None:
    margin = 10.0
    uw = p.w - 2 * margin
    ch_num = ch["num"]

    # 1. Top Chapter Header (y = 8.5 .. 22.8 mm)
    p.text(
        margin,
        11.6,
        f"STACKCALC SC-6 TEACHER & PARENT COACH GUIDE  •  1-PAGE UNIT SOLUTION KEY (UNIT {ch_num} OF {total_chapters})",
        size=2.1,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
    )
    p.draw_tutorial_keycap(margin + uw - 5.6, 8.6, w=4.8, h=4.0)
    p.text(margin, 17.2, f"Unit {ch_num}: {ch['title']} — Practice A & B Complete Key", size=4.15, bold=True, color=INK, max_w=uw - 10.0)
    p.text(margin, 21.3, f"{ch['big_ideas_book']}  •  Manipulative Kits: {ch['kit_summary']}", size=2.05, bold=True, color=SLATE, max_w=uw)
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
        "QUEST-01 Double-Points Scoring: 1 '+10' token = Method 1 (1st Way); stack a 2nd '+10' token (+20 pts) = Method 2 (2nd Way + SC-6 Check)!",
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
        ped = SECTION_PEDAGOGY[sec_num]
        ex2 = ped["ex2"]
        pg_a = 2 + (sec["day_num"] - 1) * 2
        pg_b = pg_a + 1
        p.text(
            margin + 2.0,
            sy + 3.2,
            f"SEC {sec_num} (pp.{pg_a}-{pg_b}): {stitle.upper()} [{sec['kit_id']}]",
            size=1.82,
            bold=True,
            mono=True,
            color=WHITE,
            max_w=98.0,
        )
        p.text(
            margin + uw - 2.0,
            sy + 3.2,
            f"Methods: {ped['big_ideas_method']} | ExA: {ex1['ans']} | ExB: {ex2['ans']}",
            size=1.68,
            mono=True,
            color="#E2E8F0",
            align="right",
            max_w=95.0,
        )

        # Sub-header strip (3.4 mm tall) for Practice A (Left) vs. Practice B (Right)
        sub_y = sy + 4.6
        sub_h = 3.4
        half_w = uw / 2.0
        p.rect(margin, sub_y, half_w, sub_h, fill=M1_BG, stroke=LIGHT_BORDER, line_w=0.18)
        p.rect(margin + half_w, sub_y, half_w, sub_h, fill=M2_BG, stroke=LIGHT_BORDER, line_w=0.18)
        p.text(
            margin + 2.0,
            sub_y + 2.45,
            f"PRACTICE A (p.{pg_a}): KEY IDEAS & TWO-METHOD PRACTICE (#1-#10)",
            size=1.62,
            bold=True,
            mono=True,
            color=INK,
        )
        p.text(
            margin + half_w + 2.0,
            sub_y + 2.45,
            f"PRACTICE B (p.{pg_b}): MODELING REAL LIFE APPLICATIONS (#1-#10)",
            size=1.62,
            bold=True,
            mono=True,
            color=TEAL_ACCENT,
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
                p.text(ax + 1.4, cy + row_h * 0.43, f"A{pa_prob['num']}:", size=1.68, bold=True, mono=True, color=INK)
                p.text(
                    ax + 6.8,
                    cy + row_h * 0.43,
                    pa_prob["ans"],
                    size=1.68,
                    bold=True,
                    mono=True,
                    color=TEAL_ACCENT,
                    max_w=qcol_w - 8.0,
                )
                p.text(
                    ax + 1.4,
                    cy + row_h * 0.85,
                    f"Keys: {pa_prob['keys']}",
                    size=1.48,
                    mono=True,
                    color=SLATE,
                    max_w=qcol_w - 2.6,
                )

                # --- Practice B cell ---
                pb_prob = b_probs[p_idx]
                bx = margin + half_w + c * qcol_w
                p.text(bx + 1.4, cy + row_h * 0.43, f"B{pb_prob['num']}:", size=1.68, bold=True, mono=True, color=TEAL_ACCENT)
                p.text(
                    bx + 6.8,
                    cy + row_h * 0.43,
                    pb_prob["ans"],
                    size=1.68,
                    bold=True,
                    mono=True,
                    color=INK,
                    max_w=qcol_w - 8.0,
                )
                p.text(
                    bx + 1.4,
                    cy + row_h * 0.85,
                    f"Keys: {pb_prob['keys']}",
                    size=1.48,
                    mono=True,
                    color=SLATE,
                    max_w=qcol_w - 2.6,
                )

    p.text(
        margin,
        p.h - 5.0,
        f"StackCalc SC-6 Coach & Solution Guide (1 Page Per Unit • Practice A & B Keys)  •  Unit {ch_num}: {ch['title']}",
        size=1.85,
        mono=True,
        color=MUTED,
        max_w=uw - 38.0,
    )
    p.text(margin + uw, p.h - 5.0, f"Coach Guide Page {ch_num} of {total_chapters}", size=1.85, bold=True, mono=True, color=INK, align="right")


def generate_coach_guide_pdf(chapters: List[Dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_path), pagesize=letter)
    c.setTitle("StackCalc SC-6 Big Ideas Math Middle School 10-Page Coach & Solution Guide (Practice A & B)")
    c.setAuthor("StackCalc Learning Lab")

    total_ch = len(chapters)
    for ch in chapters:
        p = CanvasPage(c, letter)
        draw_coach_chapter_page(p, ch, total_ch)
        c.showPage()

    c.save()
    print(f"[OK] Built 10-Page Coach Guide: {output_path} ({output_path.stat().st_size / 1024:.1f} KB, {total_ch} pages — 1 page per chapter)")


# =============================================================================
# 3. SYNCHRONIZE WEBSITE MARKDOWN (docs/curriculum/big-ideas-middle-school-sc6-workbook.md)
# =============================================================================
def sync_curriculum_markdown(chapters: List[Dict[str, Any]], md_path: Path) -> None:
    lines: List[str] = [
        "# Big Ideas Math Middle School: Two-Method Hands-On Block & SC-6 Supplement",
        "",
        "**Grade 6 Complete + Grade 7 Bridge • 10 Units • 45 Textbook Sections • 90 Printable Worksheets (Practice A & B) • 90 Two-Method Worked Examples • 900 Practice Problems**",
        "",
        "<div class=\"hero-buttons\" style=\"margin: 1.25rem 0 1.75rem 0;\">",
        "  <a href=\"../../downloads/worksheets/bigideas_middle_school_sc6_daily_student_workbook.pdf\" class=\"md-button md-button--primary\">📄 Download Student Supplement Workbook PDF (91 Pages • 90 Worksheets & 900 Problems)</a>",
        "  <a href=\"../../downloads/worksheets/bigideas_middle_school_sc6_teacher_coach_guide.pdf\" class=\"md-button\">🔑 Download Compact 10-Page Coach & Answer Key PDF (1 Page Per Unit)</a>",
        "</div>",
        "",
        "!!! abstract \"Built for Students Who Need Extra Practice: Authentic Big Ideas Methods, Two-Method Double Points & Clean Workspaces\"",
        "    - **100% Authentic *Big Ideas Math* Concepts & Vocabulary:** Every section tracks the exact textbook vocabulary (*dividend, divisor, quotient, prime factorization, GCF, LCM, reciprocal, tape diagram, ratio table, unit rate, equivalent expressions, Distributive Property, inverse operations, net, interquartile range (IQR), mean absolute deviation (MAD)*) and exercise formats (*Error Analysis*, *Modeling Real Life*, *Different Words, Same Question*).",
        "    - **Two-Method Worked Examples for Double Points (`+10` vs. `+20`):** Every Worked Example explicitly teaches the **two distinct methods from the *Big Ideas Math* textbook** side-by-side—**Method 1 (`+10 pts` — 1st Token)** and **Method 2 (`+20 pts DOUBLE` — 2nd Token)**—alongside step-by-step physical Block Kit instructions and SC-6 verification.",
        "    - **2 Full Worksheets Per Section (90 Worksheets • 900 Problems):** Each of the 45 textbook sections includes **Practice A (*Key Ideas & Two-Method Practice*)** and **Practice B (*Modeling Real Life & Multi-Method Applications*)** with generous, uncluttered white space to work out each problem and write the final answer.",
        "    - **Compact 10-Page Coach Guide:** The **Coach & Solution Guide PDF** fits every unit's misconception coaching, manipulative setup, and all 80–100 section answers (`Practice A #1–#10` and `Practice B #1–#10`) onto **1 single page per unit (10 pages total)**.",
        "",
        "---",
        "",
        "## 🏆 Optional Desk Companion: The Simplified 2-Piece `3x1x7U` SC-6 Scoreboard (`QUEST-01`)",
        "",
        "To motivate students to master both textbook methods on every worksheet, pair the workbook with the **`3x1x7U` Gridfinity SC-6 Scoreboard & Token Kit (`QUEST-01`)**:",
        "",
        "| Hardware Component | Dimensions & Gridfinity Standard | How Double-Points Scoring Works |",
        "| :--- | :--- | :--- |",
        "| **1. Snapfinity Scoreboard Lid (`1–10` + `100` + `(?)`)** | `125.5 × 42.0 mm` (`3x1` Stackable Lid, `6×2 = 12` sockets) | **Left 5×2 Grid:** Numbered **`1`–`5`** (top row) and **`6`–`10`** (bottom row), matching **Problems `#1–#10`**. **Rightmost Column:** Top socket **`100`** (for a 10-block Mastery Tower) and bottom **Question Mark in a Circle (`?`)** tutorial keycap badge. |",
        "| **2. `3x1x7U` Token Bank Box (`QUEST BOARD`)** | `125.5 × 42.0 × 49.0 mm` (`7U` height, `(?` tutorial badge) | Holds all **60 universal `+10` Quarter-Block tokens** in 5 neat layers of 12 (`6×2`) directly on its Gridfinity floor—no separate inner tray needed! |",
        "| **3. 60 Identical `+10` Quarter-Block Tokens** | `19.0 × 19.0 × 8.85 mm` (`7.0 mm` visible `1U` height) | Every token is identical (`+10` on top and all 4 sides):<br>• **1 Block (`+10 pts`)** = Solved with **Textbook Method 1**<br>• **2 Stacked Blocks (`+20 pts DOUBLE`)** = Verified with **Textbook Method 2** + Blocks/SC-6<br>• **10 Blocks (`100 pts`)** = **100% Worksheet Mastery!** |",
        "",
        "---",
        "",
    ]

    for ch in chapters:
        lines.append(f"## Unit {ch['num']}: {ch['title']}")
        lines.append("")
        lines.append(f"*{ch['big_ideas_book']} — {ch['subtitle']}*")
        lines.append("")
        lines.append(f"- **Manipulative Kits:** `{ch['kit_summary']}`")
        lines.append(f"- **Target Misconception:** {ch['coach_misconception']}")
        lines.append(f"- **Hands-On Remediation:** {ch['coach_remediation']}")
        lines.append("")

        for sec in ch["sections"]:
            sec_num = sec["sec_num"]
            stitle = clean_section_title(sec_num, sec["title"])
            ped = SECTION_PEDAGOGY[sec_num]
            bm = MULTI_METHOD_BLOCK_NOTES[sec_num]
            bi_method = ped["big_ideas_method"]
            ex1 = sec["examples"][0]
            ex2 = ped["ex2"]
            keys1_fmt = " ".join(f"`[{k}]`" for k in ex1["keys"])
            keys2_fmt = " ".join(f"`[{k}]`" for k in ex2["keys"])
            pg_a = 2 + (sec["day_num"] - 1) * 2
            pg_b = pg_a + 1

            lines.append(f"### Section {sec_num}: {stitle} (Workbook pp. {pg_a}–{pg_b})")
            lines.append("")
            lines.append(f"**Textbook Alignment:** {sec['big_ideas_ref']} (`{sec['ccss']}`) • **Big Ideas Methods:** *{bi_method}* • **Block Kit:** `{sec['kit_id']}` ({sec['kit_name']})")
            lines.append("")
            lines.append(f"**Key Vocabulary:** {ped['key_vocab']}")
            lines.append("")
            lines.append(f"![{stitle}](../assets/manuals/{sec['asset_png']}){{ width=\"320\" }}")
            lines.append("")
            lines.append(f"> **Key Concept:** {sec['concept']}")
            lines.append("")
            lines.append(f"#### Demonstrate Both Textbook Methods with `{sec['kit_id']}` Blocks ({sec['kit_name']})")
            lines.append("")
            lines.append(f"1. **{bm['block_m1'].split(':', 1)[0]}:**{bm['block_m1'].split(':', 1)[1]}")
            lines.append(f"2. **{bm['block_m2'].split(':', 1)[0]}:**{bm['block_m2'].split(':', 1)[1]}")
            lines.append(f"3. **{bm['block_compare'].split(':', 1)[0]}:**{bm['block_compare'].split(':', 1)[1]}")
            lines.append("")
            lines.append("#### Two-Method Worked Examples (`Method 1: +10 pts` vs. `Method 2: +20 pts DOUBLE`)")
            lines.append("")
            lines.append("| Worksheet | Problem | Method 1 (`+10 pts` — 1st Token) | Method 2 (`+20 pts DOUBLE` — 2nd Token) | SC-6 Keystrokes | Final Answer |")
            lines.append("| :--- | :--- | :--- | :--- | :--- | :--- |")
            lines.append(
                f"| **Practice A** (`p.{pg_a}`) | **{ex1['problem']}** | **{ped['ex1_m1_title']}:** {ped['ex1_m1_steps']}<br>*(See `{sec['kit_id']}` Block Way 1 above)* | **{ped['ex1_m2_title']}:** {ped['ex1_m2_steps']}<br>*(See `{sec['kit_id']}` Block Way 2 above)* | {keys1_fmt} | **{ex1['ans']}** |"
            )
            lines.append(
                f"| **Practice B** (`p.{pg_b}`) | **{ex2['problem']}** | **{ex2['m1_title']}:** {ex2['m1_steps']}<br>*{bm['ex2_block_m1']}* | **{ex2['m2_title']}:** {ex2['m2_steps']}<br>*{bm['ex2_block_m2']}* | {keys2_fmt} | **{ex2['ans']}** |"
            )
            lines.append("")
            lines.append(f"#### Practice A (p. {pg_a}): Key Ideas & Two-Method Practice (10 Exercises)")
            lines.append("")
            lines.append("| # | Problem Prompt | Coach Key: SC-6 Keystrokes | Final Answer |")
            lines.append("| :---: | :--- | :--- | :--- |")
            for prob in sec["problems"][:10]:
                cprompt = clean_sheet_a_prompt(sec_num, prob["num"], prob["prompt"])
                lines.append(f"| **A{prob['num']}** | {cprompt} | `{prob['keys']}` | **{prob['ans']}** |")
            lines.append("")
            lines.append(f"#### Practice B (p. {pg_b}): Modeling Real Life & Multi-Method Applications (10 Exercises)")
            lines.append("")
            lines.append("| # | Modeling Real Life Application Prompt | Coach Key: SC-6 Keystrokes | Final Answer |")
            lines.append("| :---: | :--- | :--- | :--- |")
            for bprob in SHEET_B_PROBLEMS[sec_num][:10]:
                lines.append(f"| **B{bprob['num']}** | {bprob['prompt']} | `{bprob['keys']}` | **{bprob['ans']}** |")
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
    generate_student_workbook_pdf(CHAPTERS_DATA, STUDENT_PDF)
    generate_coach_guide_pdf(CHAPTERS_DATA, TEACHER_PDF)
    sync_curriculum_markdown(CHAPTERS_DATA, SOURCE_MD)


if __name__ == "__main__":
    main()
