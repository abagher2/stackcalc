#!/usr/bin/env python3
"""
Publication-Grade Section-by-Section Textbook Supplement & 10-Page Coach Guide Generator
for Big Ideas Math Middle School (SC-6 Elementary Calculator & Physical Manipulatives).

Produces:
  1. docs/downloads/worksheets/bigideas_middle_school_sc6_daily_student_workbook.pdf
     - 46 pages total (Page 1 Cover/Index + 45 Section Pages, 1 per textbook section).
     - Clean, concept-focused archival white textbook layout.
     - Every section tracks the exact Big Ideas Math Unit, Section, and Textbook Method, and features:
       * Which Manipulative Block Kit Is Used + High-Res 3D Render + 2D Vector Schematic
       * Step-by-Step Physical Block Instructions (Step 1, Step 2, Step 3)
       * 1 Comprehensive Worked Example combining the Big Ideas Textbook Method, Physical Blocks,
         and SC-6 Keystrokes + Final Answer
       * 10 Graded Practice Problems (#1-#10) with Big Ideas Method tags, generous open workspace
         to work out each problem, and a clean Final Answer line (zero filler text or stack registers).
  2. docs/downloads/worksheets/bigideas_middle_school_sc6_teacher_coach_guide.pdf
     - Compact 10-Page Coach & Solution Guide (EXACTLY 1 page per Chapter for Chapters 1-10).
     - Includes Chapter Misconception & Block Remediation notes, Big Ideas Method keys,
       Worked Example keys, and all 450 Practice Problem solutions + SC-6 keystrokes.
  3. Synchronizes docs/curriculum/big-ideas-middle-school-sc6-workbook.md with all 45 sections,
     Big Ideas methods, step-by-step block instructions, worked examples, and 450 practice problems.
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

# Clean Monochrome + Subtle Slate Palette (Kid-Friendly Print Clarity, No Rainbow Boxes)
INK = "#0F172A"
SLATE = "#334155"
MUTED = "#64748B"
BORDER = "#94A3B8"
LIGHT_BORDER = "#CBD5E1"
SUBTLE_HDR = "#F8FAFC"
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
        # Note: Arial (BookSans) supports Σ and π whereas SpaceMono does not.
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

    def draw_tutorial_keycap(self, x: float, y: float, w: float = 4.8, h: float = 4.0) -> float:
        """Draws the SC-6 Tutorial keycap showing ONLY the Question Mark in a Circle (?) label."""
        self.rect(x, y, w, h, fill=WHITE, stroke=INK, r=0.75, line_w=0.28)
        cx = x + w / 2.0
        cy = y + h / 2.0
        r_circ = min(w, h) * 0.34
        self.circle(cx, cy, r_circ, fill=WHITE, stroke=INK, line_w=0.28)
        self.text(cx, cy + r_circ * 0.56, "?", size=r_circ * 1.45, bold=True, mono=True, color=INK, align="center")
        return w

    def draw_keycap(self, label: str, x: float, y: float, h: float = 3.8) -> float:
        """Draws a crisp hardware calculator keycap squircle with full glyph support."""
        raw_lbl = label.strip()
        if raw_lbl in ("?", "[?]", "C?"):
            return self.draw_tutorial_keycap(x, y, w=h * 1.2, h=h)
        is_xbar = raw_lbl == "x̄"
        lbl = "x" if is_xbar else clean_pdf_text(raw_lbl)
        char_len = len(lbl)
        w = max(h * 1.12, char_len * 1.65 + 2.2)
        if lbl.upper() in ("ENTER", "LASTX", "FDISP", "PRIME", "PRISM", "%CHG"):
            w = max(w, h * 1.68)

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

        self.rect(x, y, w, h, fill=bg, stroke=border, r=0.75, line_w=0.25)
        fsize = min(h * 0.48, (w - 0.9) / max(1, char_len) * 1.35)
        self.text(x + w / 2.0, y + h * 0.71, lbl, size=fsize, bold=True, mono=True, color=fg, align="center")
        if is_xbar:
            self.line(x + w / 2.0 - 0.9, y + h * 0.28, x + w / 2.0 + 0.9, y + h * 0.28, color=fg, width=0.28)
        return w

    def draw_keycap_sequence(
        self,
        keys: List[str],
        x: float,
        y: float,
        max_w: float,
        h: float = 3.7,
        gap: float = 0.85,
    ) -> float:
        if len(keys) > 10:
            h = 3.2
            gap = 0.6
        elif len(keys) > 8:
            h = 3.45
            gap = 0.7
        cur_x = x
        cur_y = y
        for k in keys:
            lbl = clean_pdf_text(k.strip())
            est_w = max(h * 1.12, len(lbl) * 1.65 + 2.2)
            if cur_x + est_w > x + max_w and cur_x > x:
                cur_x = x
                cur_y += h + 0.9
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
            tile_s = 3.5
            gap = 0.45
            gx0 = x + 3.5
            gy0 = y + 4.2
            for r in range(5):
                for c in range(4):
                    self.rect(gx0 + c * (tile_s + gap), gy0 + r * (tile_s + gap), tile_s, tile_s, fill="#E2E8F0", stroke=INK, r=0.5, line_w=0.22)
            rx0 = gx0 + 4 * (tile_s + gap) + 4.0
            for rem_i in range(3):
                self.rect(rx0, gy0 + (2 + rem_i) * (tile_s + gap), tile_s, tile_s, fill="#CBD5E1", stroke=INK, r=0.5, line_w=0.25)
            self.text(gx0 + 8.0, y + 3.0, "5 Rows of 4 (=20)", size=1.95, bold=True, color=INK, align="center")
            self.text(rx0 + 2.0, gy0 + 4.2, "+3 Left", size=1.95, bold=True, color=SLATE, align="center")
            self.text(rx0 + 2.0, gy0 + 6.8, "(Rem=3)", size=1.75, mono=True, color=SLATE, align="center")

        elif dtype == "power_array":
            ts = 3.5
            gap = 0.45
            gx0 = x + 3.0
            gy0 = y + 5.0
            for r in range(4):
                for c in range(4):
                    self.rect(gx0 + c * (ts + gap), gy0 + r * (ts + gap), ts, ts, fill="#E2E8F0", stroke=INK, r=0.4, line_w=0.22)
            self.text(gx0 + 7.8, y + 3.5, "4² = 4×4 (16)", size=2.0, bold=True, color=INK, align="center")
            tx0 = gx0 + 4 * (ts + gap) + 4.8
            for r in range(2):
                for c in range(4):
                    self.rect(tx0 + c * (ts * 0.8 + gap), gy0 + 3.8 + r * (ts * 0.8 + gap), ts * 0.8, ts * 0.8, fill=WHITE, stroke=SLATE, r=0.3, line_w=0.2)
            self.text(tx0 + 6.5, gy0 + 2.3, "NOT 4×2 (8)!", size=1.85, bold=True, color=SLATE, align="center")

        elif dtype == "two_room":
            r1 = ddata.get("room1", "8 + 4 = 12")
            r2 = ddata.get("room2", "9 - 3 = 6")
            res = ddata.get("res", "72")
            self.rect(x + 2.0, y + 2.5, w - 4.0, 7.2, fill="#F1F5F9", stroke=INK, r=0.8, line_w=0.25)
            self.text(x + w / 2.0, y + 5.2, "GROUP 1 TILES:", size=1.8, bold=True, mono=True, color=SLATE, align="center")
            self.text(x + w / 2.0, y + 8.1, r1, size=1.95, bold=True, mono=True, color=INK, align="center", max_w=w - 6.0)

            self.rect(x + 2.0, y + 11.2, w - 4.0, 7.2, fill="#E2E8F0", stroke=INK, r=0.8, line_w=0.25)
            self.text(x + w / 2.0, y + 13.9, "GROUP 2 TILES:", size=1.8, bold=True, mono=True, color=SLATE, align="center")
            self.text(x + w / 2.0, y + 16.8, r2, size=1.95, bold=True, mono=True, color=INK, align="center", max_w=w - 6.0)

            self.text(x + w / 2.0, y + 22.2, f"==> {res}", size=2.1, bold=True, mono=True, color=TEAL_ACCENT, align="center", max_w=w - 4.0)

        elif dtype == "prime_tower":
            base_y = y + h - 2.8
            axis_x = x + 9.0
            self.line(axis_x, y + 2.8, axis_x, base_y, color=INK, width=0.35)
            for val, frac_h in [(1, 0.0), (2, 0.17), (4, 0.34), (12, 0.61), (60, 1.0)]:
                ty = base_y - frac_h * (h - 6.5)
                self.line(axis_x - 1.5, ty, axis_x, ty, color=INK, width=0.25)
                self.text(axis_x - 2.0, ty + 0.8, str(val), size=1.75, bold=(val == 60), mono=True, color=INK, align="right")

            bx = axis_x + 4.0
            bw = 13.0
            tot_h = h - 6.5
            blocks = [(2, 0.17, "#DBEAFE"), (2, 0.17, "#DBEAFE"), (3, 0.27, "#DCFCE7"), (5, 0.39, "#FEF3C7")]
            cur_by = base_y
            for pval, ph_ratio, bcol in blocks:
                bh = ph_ratio * tot_h
                self.rect(bx, cur_by - bh, bw, bh, fill=bcol, stroke=INK, r=0.4, line_w=0.25)
                self.text(bx + bw / 2.0, cur_by - bh / 2.0 + 0.7, f"[{pval}]", size=1.95, bold=True, mono=True, color=INK, align="center")
                cur_by -= bh
            self.line(axis_x, cur_by, bx, cur_by, color=TEAL_ACCENT, width=0.3, dashed=True)
            self.text(bx + bw + 2.0, y + 7.5, "2×2×3×5", size=1.95, bold=True, mono=True, color=INK)
            self.text(bx + bw + 2.0, y + 11.0, "= 60!", size=2.1, bold=True, mono=True, color=TEAL_ACCENT)

        elif dtype == "gcf_lcm_towers":
            base_y = y + h - 3.0
            tot_h = h - 7.0
            cols = [
                ("20", [(2, 0.2), (2, 0.2), (5, 0.35)], x + 2.5),
                ("50", [(2, 0.2), (5, 0.35), (5, 0.35)], x + 13.0),
                ("GCF=10", [(2, 0.2), (5, 0.35)], x + 23.5),
                ("LCM=100", [(2, 0.18), (2, 0.18), (5, 0.32), (5, 0.32)], x + 34.0),
            ]
            for lbl, blks, cx in cols:
                cur_y = base_y
                for pval, r_h in blks:
                    bh = r_h * tot_h
                    fill_c = "#DBEAFE" if pval == 2 else "#FEF3C7"
                    self.rect(cx, cur_y - bh, 8.0, bh, fill=fill_c, stroke=INK, r=0.3, line_w=0.22)
                    self.text(cx + 4.0, cur_y - bh / 2.0 + 0.7, str(pval), size=1.75, bold=True, mono=True, color=INK, align="center")
                    cur_y -= bh
                self.text(cx + 4.0, base_y + 2.1, lbl, size=1.55, bold=True, mono=True, color=INK, align="center")

        elif dtype == "fraction_towers":
            base_y = y + h - 3.3
            max_h = h - 7.0
            bars = [
                ("1", [1.0], "#E2E8F0", x + 3.0),
                ("2/3", [1 / 3, 1 / 3], "#DBEAFE", x + 13.5),
                ("4/6", [1 / 6] * 4, "#DCFCE7", x + 24.0),
                ("7/12", [1 / 3, 1 / 4], "#FEF3C7", x + 34.5),
            ]
            for lbl, segs, col_hex, bx in bars:
                cur_y = base_y
                for s in segs:
                    sh = s * max_h
                    self.rect(bx, cur_y - sh, 8.0, sh, fill=col_hex, stroke=INK, r=0.3, line_w=0.22)
                    cur_y -= sh
                self.text(bx + 4.0, base_y + 2.2, lbl, size=1.7, bold=True, mono=True, color=INK, align="center")
            y_23 = base_y - (2 / 3) * max_h
            self.line(x + 13.5, y_23, x + 32.0, y_23, color=TEAL_ACCENT, width=0.3, dashed=True)

        elif dtype == "place_value":
            num_str = ddata.get("num", "14.85")
            ip_str = ddata.get("ip", "14")
            fp_str = ddata.get("fp", "0.85")
            self.text(x + w / 2.0, y + 4.2, f"Input: {num_str}", size=2.1, bold=True, mono=True, color=INK, align="center")
            bw = (w - 6.0) / 2.0
            self.rect(x + 2.0, y + 6.5, bw, 14.2, fill="#F1F5F9", stroke=INK, r=0.8, line_w=0.25)
            self.text(x + 2.0 + bw / 2.0, y + 10.4, "[f] [IP]", size=1.85, bold=True, mono=True, color=SLATE, align="center")
            self.text(x + 2.0 + bw / 2.0, y + 15.0, ip_str, size=2.05, bold=True, mono=True, color=INK, align="center", max_w=bw - 1.5)
            self.text(x + 2.0 + bw / 2.0, y + 18.8, "Whole", size=1.7, color=MUTED, align="center")

            rx = x + 4.0 + bw
            self.rect(rx, y + 6.5, bw, 14.2, fill="#E2E8F0", stroke=INK, r=0.8, line_w=0.25)
            self.text(rx + bw / 2.0, y + 10.4, "[g] [FP]", size=1.85, bold=True, mono=True, color=SLATE, align="center")
            self.text(rx + bw / 2.0, y + 15.0, fp_str, size=2.05, bold=True, mono=True, color=INK, align="center", max_w=bw - 1.5)
            self.text(rx + bw / 2.0, y + 18.8, "Decimal", size=1.7, color=MUTED, align="center")

        elif dtype == "ratio_tape":
            a = min(5, int(ddata.get("a", 3)))
            b = min(5, int(ddata.get("b", 2)))
            uval = ddata.get("unit_val", 4)
            ts = 6.0
            gap = 0.6
            gx0 = x + 3.5
            self.text(gx0, y + 4.2, f"Part A ({a} tiles):", size=1.85, bold=True, color=INK)
            for i in range(a):
                self.rect(gx0 + i * (ts + gap), y + 5.4, ts, 4.9, fill="#DBEAFE", stroke=INK, r=0.5, line_w=0.25)
                self.text(gx0 + i * (ts + gap) + ts / 2.0, y + 8.6, str(uval), size=1.95, bold=True, mono=True, color=INK, align="center")
            self.text(gx0, y + 13.6, f"Part B ({b} tiles):", size=1.85, bold=True, color=INK)
            for i in range(b):
                self.rect(gx0 + i * (ts + gap), y + 14.8, ts, 4.9, fill="#FEF3C7", stroke=INK, r=0.5, line_w=0.25)
                self.text(gx0 + i * (ts + gap) + ts / 2.0, y + 18.0, str(uval), size=1.95, bold=True, mono=True, color=INK, align="center")
            self.text(x + w / 2.0, y + 23.0, f"Ratio {a}:{b} ({a+b} boxes total)", size=1.85, bold=True, mono=True, color=TEAL_ACCENT, align="center")

        elif dtype == "percent_bar":
            bw = w - 6.0
            bx = x + 3.0
            by = y + 7.5
            bh = 6.2
            self.rect(bx, by, bw, bh, fill="#F1F5F9", stroke=INK, r=0.6, line_w=0.25)
            self.rect(bx, by, bw * 0.75, bh, fill="#DBEAFE", stroke=INK, r=0.6, line_w=0.25)
            for q in range(1, 4):
                qx = bx + bw * (q * 0.25)
                self.line(qx, by, qx, by + bh, color=INK, width=0.22, dashed=True)
            self.text(x + w / 2.0, y + 5.2, "3/4  =  0.75  =  75%", size=2.05, bold=True, mono=True, color=INK, align="center")
            self.text(bx, by + bh + 3.3, "0%", size=1.75, mono=True, color=SLATE)
            self.text(bx + bw * 0.75, by + bh + 3.3, "75%", size=1.85, bold=True, mono=True, color=TEAL_ACCENT, align="center")
            self.text(bx + bw, by + bh + 3.3, "100%", size=1.75, mono=True, color=SLATE, align="right")

        elif dtype == "algebra_tiles":
            gx = x + 3.0
            gy = y + 4.0
            self.rect(gx, gy, 10.0, 10.0, fill="#DBEAFE", stroke=INK, r=0.6, line_w=0.25)
            self.text(gx + 5.0, gy + 5.8, "x²", size=2.3, bold=True, mono=True, color=INK, align="center")
            rx = gx + 12.0
            for i in range(3):
                self.rect(rx + i * 4.8, gy, 4.0, 10.0, fill="#DCFCE7", stroke=INK, r=0.4, line_w=0.22)
                self.text(rx + i * 4.8 + 2.0, gy + 5.8, "x", size=1.95, bold=True, mono=True, color=INK, align="center")
            ux = rx + 15.5
            for r in range(2):
                for c in range(2):
                    self.rect(ux + c * 4.0, gy + r * 4.0, 3.4, 3.4, fill="#FEF3C7", stroke=INK, r=0.3, line_w=0.2)
                    self.text(ux + c * 4.0 + 1.7, gy + r * 4.0 + 2.3, "1", size=1.6, bold=True, mono=True, color=INK, align="center")
            self.text(x + w / 2.0, y + 19.2, "Sort by Shape:", size=1.85, bold=True, color=SLATE, align="center")
            self.text(x + w / 2.0, y + 22.5, "x²-Flats | x-Rods | 1-Cubes", size=1.75, bold=True, mono=True, color=INK, align="center")

        elif dtype == "polygon_area":
            shape = ddata.get("shape", "parallelogram")
            if shape == "parallelogram":
                pts = [(x + 8.0, y + 5.5), (x + 32.0, y + 5.5), (x + 27.0, y + 17.5), (x + 3.0, y + 17.5)]
                self.polygon(pts, fill="#E2E8F0", stroke=INK, line_w=0.3)
                self.line(x + 8.0, y + 5.5, x + 8.0, y + 17.5, color=TEAL_ACCENT, width=0.3, dashed=True)
                self.text(x + 17.5, y + 21.5, "Base b = 12", size=1.95, bold=True, mono=True, color=INK, align="center")
                self.text(x + 13.5, y + 12.8, "h = 8", size=1.95, bold=True, mono=True, color=TEAL_ACCENT)
                self.text(x + 33.0, y + 12.8, "x10", size=1.75, mono=True, color=MUTED)
            elif shape == "triangle":
                self.rect(x + 6.0, y + 4.5, 28.0, 13.0, fill="#F8FAFC", stroke=BORDER, line_w=0.2)
                pts = [(x + 6.0, y + 17.5), (x + 34.0, y + 17.5), (x + 6.0, y + 4.5)]
                self.polygon(pts, fill="#DBEAFE", stroke=INK, line_w=0.3)
                self.text(x + w / 2.0, y + 21.8, "[g] [TRI] = ½ × b × h", size=1.85, bold=True, mono=True, color=INK, align="center")
            else:
                self.rect(x + 10.0, y + 10.5, 22.0, 9.5, fill="#E2E8F0", stroke=INK, line_w=0.28)
                pts = [(x + 10.0, y + 10.5), (x + 32.0, y + 10.5), (x + 21.0, y + 3.8)]
                self.polygon(pts, fill="#DBEAFE", stroke=INK, line_w=0.28)
                self.text(x + 21.0, y + 16.2, "[f][RECT]", size=1.8, bold=True, mono=True, color=INK, align="center")
                self.text(x + 21.0, y + 9.4, "[g][TRI]", size=1.7, bold=True, mono=True, color=INK, align="center")
                self.text(x + w / 2.0, y + 23.0, "Sum chunks with [Σ+]!", size=1.75, bold=True, color=TEAL_ACCENT, align="center")

        elif dtype == "clock_dial":
            cx = x + w / 2.0
            cy = y + 11.2
            r = 8.0
            self.circle(cx, cy, r, fill="#F8FAFC", stroke=INK, line_w=0.3)
            for hr in range(12):
                ang = math.radians(hr * 30 - 90)
                self.line(
                    cx + (r - 1.2) * math.cos(ang),
                    cy + (r - 1.2) * math.sin(ang),
                    cx + r * math.cos(ang),
                    cy + r * math.sin(ang),
                    color=INK,
                    width=0.22,
                )
            self.line(cx, cy, cx + 4.2, cy - 1.8, color=INK, width=0.45)
            self.line(cx, cy, cx - 6.0, cy, color=TEAL_ACCENT, width=0.35)
            self.text(cx, y + 23.0, "60 min = 1 hr ([CLK])", size=1.85, bold=True, mono=True, color=INK, align="center")

        elif dtype == "zero_pairs":
            gx = x + 5.5
            gy = y + 6.0
            for i in range(4):
                cx = gx + i * 8.5
                self.circle(cx, gy, 2.6, fill="#FEF3C7", stroke=INK, line_w=0.25)
                self.text(cx, gy + 0.85, "+", size=2.1, bold=True, mono=True, color=INK, align="center")
                if i < 3:
                    self.circle(cx, gy + 7.2, 2.6, fill="#FEE2E2", stroke=INK, line_w=0.25)
                    self.text(cx, gy + 8.05, "-", size=2.1, bold=True, mono=True, color=INK, align="center")
                    self.rect(cx - 3.1, gy - 3.1, 6.2, 13.4, fill=None, stroke=SLATE, r=1.1, line_w=0.2)
            ny = y + 21.0
            self.line(x + 2.5, ny, x + w - 2.5, ny, color=INK, width=0.3)
            self.line(x + w / 2.0, ny - 1.4, x + w / 2.0, ny + 1.4, color=INK, width=0.3)
            self.text(x + w / 2.0, ny + 3.0, "0", size=1.75, bold=True, mono=True, color=INK, align="center")
            self.text(x + 3.0, ny - 1.7, "<- Colder (-)", size=1.6, color=SLATE)
            self.text(x + w - 3.0, ny - 1.7, "Warmer (+) ->", size=1.6, color=TEAL_ACCENT, align="right")

        elif dtype == "coord_plane":
            cx = x + w / 2.0
            cy = y + 12.2
            span = 9.0
            self.line(cx - span - 3, cy, cx + span + 3, cy, color=INK, width=0.3)
            self.line(cx, cy - span, cx, cy + span, color=INK, width=0.3)
            self.text(cx + 6.5, cy - 4.2, "QI (+,+)", size=1.65, bold=True, mono=True, color=INK, align="center")
            self.text(cx - 6.5, cy - 4.2, "QII (-,+)", size=1.65, bold=True, mono=True, color=SLATE, align="center")
            self.text(cx - 6.5, cy + 6.2, "QIII (-,-)", size=1.65, bold=True, mono=True, color=SLATE, align="center")
            self.text(cx + 6.5, cy + 6.2, "QIV (+,-)", size=1.65, bold=True, mono=True, color=INK, align="center")
            self.circle(cx + 5.0, cy - 2.8, 1.0, fill=TEAL_ACCENT, stroke=INK, line_w=0.2)
            self.circle(cx - 5.0, cy - 2.8, 1.0, fill="#D97706", stroke=INK, line_w=0.2)

        elif dtype == "balance_scale":
            left_lbl = ddata.get("left", "3x + 7")
            right_lbl = ddata.get("right", "28")
            sol_lbl = ddata.get("sol", "x = 7")
            cx = x + w / 2.0
            by = y + 15.5
            self.line(x + 3.5, by, x + w - 3.5, by, color=INK, width=0.45)
            self.polygon([(cx, by), (cx - 2.6, by + 3.9), (cx + 2.6, by + 3.9)], fill=INK, stroke=INK)
            self.text(cx, by - 1.1, "=", size=2.4, bold=True, mono=True, color=INK, align="center")
            pw = (w - 9.0) / 2.0
            self.rect(x + 2.5, y + 5.8, pw, 8.2, fill="#DCFCE7", stroke=INK, r=0.6, line_w=0.25)
            self.text(x + 2.5 + pw / 2.0, y + 8.9, "Left Pan:", size=1.65, bold=True, color=SLATE, align="center")
            self.text(x + 2.5 + pw / 2.0, y + 12.2, left_lbl, size=1.9, bold=True, mono=True, color=INK, align="center", max_w=pw - 1.5)
            rx = x + w - 2.5 - pw
            self.rect(rx, y + 5.8, pw, 8.2, fill="#FEF3C7", stroke=INK, r=0.6, line_w=0.25)
            self.text(rx + pw / 2.0, y + 8.9, "Right Pan:", size=1.65, bold=True, color=SLATE, align="center")
            self.text(rx + pw / 2.0, y + 12.2, right_lbl, size=1.9, bold=True, mono=True, color=INK, align="center", max_w=pw - 1.5)
            self.text(cx, y + 23.2, sol_lbl, size=1.8, bold=True, mono=True, color=TEAL_ACCENT, align="center", max_w=w - 3.0)

        elif dtype == "solid_3d":
            mode = ddata.get("mode", "net")
            if mode == "net":
                cx = x + 16.5
                cy = y + 8.8
                self.rect(cx, cy, 8.0, 4.8, fill="#DBEAFE", stroke=INK, line_w=0.25)
                self.rect(cx, cy - 3.8, 8.0, 3.8, fill="#DCFCE7", stroke=INK, line_w=0.25)
                self.rect(cx, cy + 4.8, 8.0, 3.8, fill="#DCFCE7", stroke=INK, line_w=0.25)
                self.rect(cx, cy + 8.6, 8.0, 4.8, fill="#DBEAFE", stroke=INK, line_w=0.25)
                self.rect(cx - 4.8, cy, 4.8, 4.8, fill="#FEF3C7", stroke=INK, line_w=0.25)
                self.rect(cx + 8.0, cy, 4.8, 4.8, fill="#FEF3C7", stroke=INK, line_w=0.25)
                self.text(x + w / 2.0, y + 23.4, "3 Face Pairs -> [Σ+] (n=3)", size=1.75, bold=True, mono=True, color=INK, align="center")
            else:
                bx, by, bw, bh = x + 9.0, y + 7.5, 18.0, 10.5
                dx, dy = 5.0, -3.8
                self.rect(bx, by, bw, bh, fill="#E2E8F0", stroke=INK, line_w=0.28)
                self.polygon([(bx, by), (bx + dx, by + dy), (bx + bw + dx, by + dy), (bx + bw, by)], fill="#F1F5F9", stroke=INK, line_w=0.25)
                self.polygon([(bx + bw, by), (bx + bw + dx, by + dy), (bx + bw + dx, by + bh + dy), (bx + bw, by + bh)], fill="#CBD5E1", stroke=INK, line_w=0.25)
                self.text(x + w / 2.0, y + 22.8, "l [ENTER] w [ENTER] h [f][PRISM]", size=1.65, bold=True, mono=True, color=TEAL_ACCENT, align="center")

        elif dtype == "stat_plot":
            mode = ddata.get("mode", "mean_towers")
            if mode == "boxplot":
                by = y + 11.2
                x_min, x_q1, x_med, x_q3, x_max = x + 4.5, x + 12.0, x + 21.5, x + 31.0, x + 39.5
                self.line(x_min, by, x_q1, by, color=INK, width=0.35)
                self.line(x_q3, by, x_max, by, color=INK, width=0.35)
                self.line(x_min, by - 2.3, x_min, by + 2.3, color=INK, width=0.35)
                self.line(x_max, by - 2.3, x_max, by + 2.3, color=INK, width=0.35)
                self.rect(x_q1, by - 3.8, x_q3 - x_q1, 7.6, fill="#DBEAFE", stroke=INK, line_w=0.3)
                self.line(x_med, by - 3.8, x_med, by + 3.8, color=TEAL_ACCENT, width=0.45)
                self.text(x_min, by + 6.2, "MIN", size=1.55, bold=True, mono=True, align="center")
                self.text(x_q1, by + 6.2, "1Q", size=1.55, bold=True, mono=True, align="center")
                self.text(x_med, by + 6.2, "MED", size=1.55, bold=True, mono=True, color=TEAL_ACCENT, align="center")
                self.text(x_q3, by + 6.2, "3Q", size=1.55, bold=True, mono=True, align="center")
                self.text(x_max, by + 6.2, "MAX", size=1.55, bold=True, mono=True, align="center")
                self.text(x + w / 2.0, y + 22.8, "Box = Middle 50% ([IQR])", size=1.75, bold=True, mono=True, color=INK, align="center")
            else:
                towers = ddata.get("towers", [3, 7, 5, 9, 6])[:5]
                mean_v = ddata.get("mean", 6)
                base_y = y + 20.2
                max_v = max(towers + [1])
                scale_h = 13.5 / max_v
                for idx, tv in enumerate(towers):
                    tx = x + 5.0 + idx * 6.8
                    th = tv * scale_h
                    self.rect(tx, base_y - th, 4.8, th, fill="#DBEAFE", stroke=INK, r=0.3, line_w=0.22)
                    self.text(tx + 2.4, base_y + 2.6, str(tv), size=1.65, bold=True, mono=True, align="center")
                my = base_y - mean_v * scale_h
                self.line(x + 2.5, my, x + w - 2.5, my, color=TEAL_ACCENT, width=0.35, dashed=True)
                self.text(x + w / 2.0, y + 3.8, f"Fair-Share Mean = {mean_v}", size=1.75, bold=True, mono=True, color=TEAL_ACCENT, align="center")

        else:  # prob_spinner
            cx = x + 13.5
            cy = y + 12.0
            r = 7.6
            self.circle(cx, cy, r, fill="#F8FAFC", stroke=INK, line_w=0.3)
            for s in range(10):
                ang = math.radians(s * 36 - 90)
                self.line(cx, cy, cx + r * math.cos(ang), cy + r * math.sin(ang), color=BORDER, width=0.2)
            self.line(cx, cy, cx + 4.8, cy - 3.2, color=INK, width=0.45)
            self.rect(x + 26.0, y + 7.0, 10.5, 10.5, fill="#E2E8F0", stroke=INK, r=1.2, line_w=0.28)
            for dx, dy in [(-2.3, -2.3), (2.3, -2.3), (0, 0), (-2.3, 2.3), (2.3, 2.3)]:
                self.circle(x + 31.25 + dx, y + 12.25 + dy, 0.65, fill=INK, stroke=INK)
            self.text(x + w / 2.0, y + 23.2, "[DICE] • [x!] • [f][nCr] • [g][nPr]", size=1.65, bold=True, mono=True, color=INK, align="center")


# =============================================================================
# 1. STUDENT WORKBOOK GENERATOR (1 Cover Page + 45 Full Section Pages)
# =============================================================================
def draw_student_cover_page(p: CanvasPage, chapters: List[Dict[str, Any]]) -> None:
    margin = 12.0
    uw = p.w - 2 * margin

    p.text(margin, 14.0, "STACKCALC LEARNING LAB  •  MIDDLE SCHOOL TEXTBOOK SUPPLEMENT & WORKBOOK", size=2.6, bold=True, mono=True, color=TEAL_ACCENT)
    p.text(margin, 22.0, "Big Ideas Math Middle School: Hands-On Block & SC-6 Supplement", size=5.4, bold=True, color=INK)
    p.text(margin, 27.5, "Section-by-Section Textbook Methods, Step-by-Step Manipulative Block Instructions, Worked Examples & 450 Practice Problems", size=2.75, color=SLATE)
    p.line(margin, 30.0, margin + uw, 30.0, color=INK, width=0.5)

    cw = (uw - 6.0) / 3.0
    cards = [
        (
            "1. BIG IDEAS TEXTBOOK METHODS",
            "Every section aligns directly to Big Ideas Math (Units 1–10) and tracks the exact textbook methods: Factor Trees, Tape Diagrams, Ratio Tables, LCD Towers, Area Models, Balance Scales, Nets, and Box Plots.",
        ),
        (
            "2. STEP-BY-STEP BLOCK KITS",
            "Each section names the exact StackCalc Block Kit used and walks through Step 1, Step 2, and Step 3 with physical blocks alongside 1 clear Worked Example showing both the textbook method and SC-6 keystrokes.",
        ),
        (
            "3. WORKSPACE & +10 SCOREBOARD",
            "Every problem gives open workspace to work out the math and write the final answer—never the calculator stack! Optional QUEST-01 Scoreboard: 1 block = +10 pts (1st Way), 2 blocks = +20 pts (2nd Way).",
        ),
    ]
    for i, (ctitle, cbody) in enumerate(cards):
        cx = margin + i * (cw + 3.0)
        p.rect(cx, 32.5, cw, 25.0, fill=WHITE, stroke=INK, r=1.2, line_w=0.3)
        p.rect(cx, 32.5, cw, 5.5, fill=INK, stroke=INK, r=0.8, line_w=0.2)
        p.text(cx + 2.5, 36.3, ctitle, size=2.0, bold=True, mono=True, color=WHITE)
        if i == 2:
            p.draw_tutorial_keycap(cx + cw - 6.4, 33.1, w=4.8, h=4.2)
        p.para(cx + 2.5, 41.2, cbody, max_w=cw - 5.0, size=2.3, color=INK, leading=1.26)

    p.rect(margin, 60.0, uw, 31.0, fill=SUBTLE_HDR, stroke=BORDER, r=1.2, line_w=0.25)
    p.text(margin + 3.0, 64.2, "MANIPULATIVE BLOCK KITS & THE 3x1x7U SC-6 SCOREBOARD KIT (QUEST-01)", size=2.25, bold=True, mono=True, color=INK)
    p.draw_tutorial_keycap(margin + uw - 7.8, 60.8, w=4.8, h=4.2)
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
        p.rect(sx + 1.0, 66.0, sw_w - 2.0, 19.5, fill=WHITE, stroke=LIGHT_BORDER, r=0.8, line_w=0.2)
        p.image(ASSETS_MANUALS_DIR / png_name, sx + 2.0, 66.8, sw_w - 4.0, 18.0)
        p.text(sx + sw_w / 2.0, 88.8, cap, size=2.0, bold=True, color=SLATE, align="center")

    ty = 94.0
    p.rect(margin, ty, uw, 6.0, fill=INK, stroke=INK, line_w=0.3)
    p.text(margin + 2.5, ty + 4.1, "UNIT / CHAPTER & BIG IDEAS ALIGNMENT", size=2.1, bold=True, mono=True, color=WHITE)
    p.text(margin + 72.0, ty + 4.1, "SECTIONS & WORKBOOK PAGES", size=2.1, bold=True, mono=True, color=WHITE)
    p.text(margin + 143.5, ty + 4.1, "BIG IDEAS TEXTBOOK METHODS", size=2.05, bold=True, mono=True, color=WHITE)

    unit_methods_summary = {
        1: "Arrays, Factor Trees & Venn GCF/LCM",
        2: "LCD Towers, Reciprocals & Place Value",
        3: "Tape Diagrams, Ratio Tables, Rates & %",
        4: "Substitution, Like Terms, Area & GCF",
        5: "Cut-and-Slide Polygons, Trapezoids & Time",
        6: "Number Lines, Opposites, |x| & 4-Quad",
        7: "Balance Scale Inverse Ops & Inequalities",
        8: "2D Prism/Pyramid Nets, V=lwh, π & Cones",
        9: "Dot Plots, Fair-Share Mean, IQR & MAD",
        10: "Zero-Pair Chips, 2-Step Eq. & Probability",
    }
    row_h = 16.2
    for idx, ch in enumerate(chapters):
        ry = ty + 6.0 + idx * row_h
        bg = WHITE if idx % 2 == 0 else SUBTLE_HDR
        p.rect(margin, ry, uw, row_h, fill=bg, stroke=LIGHT_BORDER, line_w=0.2)
        p.line(margin + 70.0, ry, margin + 70.0, ry + row_h, color=LIGHT_BORDER, width=0.2)
        p.line(margin + 142.0, ry, margin + 142.0, ry + row_h, color=LIGHT_BORDER, width=0.2)

        p.text(margin + 2.2, ry + 4.3, f"Unit {ch['num']}: {ch['title']}", size=2.35, bold=True, color=INK, max_w=66.0)
        p.para(margin + 2.2, ry + 7.8, f"{ch['big_ideas_book']} • {ch['kit_summary']}", max_w=66.0, size=1.95, color=SLATE, max_lines=2)

        for li, s in enumerate(ch["sections"]):
            sl = f"[ ] Sec {s['sec_num']} (p.{s['day_num']+1}): {s['title']}"
            p.text(margin + 71.5, ry + 3.4 + li * 2.9, sl, size=1.85, color=INK, max_w=69.0)

        m_sum = unit_methods_summary.get(ch["num"], "")
        n_probs = len(ch["sections"]) * 10
        p.text(margin + 143.5, ry + 5.2, m_sum, size=1.9, bold=True, color=INK, max_w=46.0)
        p.text(margin + 143.5, ry + 9.6, f"Kit: {ch['kit_summary'].split('+')[0].strip()}", size=1.8, mono=True, color=SLATE, max_w=46.0)
        p.text(margin + 143.5, ry + 13.8, f"[ ] Unit {ch['num']} Complete ({n_probs}/{n_probs})", size=1.85, bold=True, color=TEAL_ACCENT)

    p.text(margin, p.h - 6.0, "StackCalc Learning Systems  •  Big Ideas Math Middle School Supplement (10 Units • 45 Sections • 450 Practice Problems)", size=2.05, mono=True, color=MUTED)
    p.text(margin + uw, p.h - 6.0, "Page 1 of 46", size=2.05, bold=True, mono=True, color=INK, align="right")


def draw_student_section_page(p: CanvasPage, ch: Dict[str, Any], sec: Dict[str, Any], page_num: int) -> None:
    margin = 11.0
    uw = p.w - 2 * margin
    sec_num = sec["sec_num"]
    ped = SECTION_PEDAGOGY.get(
        sec_num,
        {
            "unit_name": f"Unit {ch['num']}: {ch['title']}",
            "big_ideas_method": "Big Ideas Textbook Model & Inverse Operation Check",
            "block_steps": [sec["examples"][0]["block_step"], "Model the quantities on the Gridfinity stage.", "Verify the result with SC-6 keystrokes."],
            "textbook_steps": sec["examples"][0]["block_step"],
            "problem_methods": ("Guided Method", "Textbook Practice", "Application & Check"),
        },
    )

    # 1. Top Unit & Section Banner (y = 9.0 .. 25.2 mm)
    p.text(
        margin,
        12.4,
        f"{ped['unit_name'].upper()}  •  {sec['big_ideas_ref'].upper()} ({sec['ccss']})",
        size=2.05,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=122.0,
    )
    kit_badge = f"BLOCK KIT: {sec['kit_id']} • {sec['kit_name']}"
    p.rect(margin + uw - 70.0, 9.1, 70.0, 4.8, fill=SUBTLE_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(margin + uw - 35.0, 12.3, kit_badge, size=1.85, bold=True, mono=True, color=INK, align="center", max_w=67.0)

    # Main Section Title
    p.text(margin, 18.6, f"Section {sec_num}: {sec['title']}", size=4.2, bold=True, color=INK, max_w=uw)

    # Big Ideas Method Tag (Left) + Student Name / Date / Score Line (Right)
    p.text(
        margin,
        23.4,
        f"Big Ideas Method: {ped['big_ideas_method']}",
        size=2.0,
        bold=True,
        color=SLATE,
        max_w=114.0,
    )
    p.text(
        margin + uw,
        23.4,
        "Name: ______________________   Date: __________   Score: ____ / 10",
        size=1.95,
        bold=True,
        color=INK,
        align="right",
    )
    p.line(margin, 25.0, margin + uw, 25.0, color=INK, width=0.45)

    # 2. Concept Strip (y = 26.2 .. 35.6 mm)
    p.rect(margin, 26.2, uw, 9.4, fill=WHITE, stroke=SLATE, r=0.9, line_w=0.25)
    p.text(margin + 2.2, 29.4, "CONCEPT SUMMARY & TEXTBOOK CONNECTION:", size=2.0, bold=True, mono=True, color=TEAL_ACCENT)
    p.para(margin + 2.2, 32.5, sec["concept"], max_w=uw - 4.4, size=2.15, color=INK, leading=1.2, max_lines=2)

    # 3. Top Band (y = 36.8 .. 100.8 mm, height = 64.0 mm)
    #    LEFT: Block Kit Used + Diagram + Step-by-Step Block Instructions
    #    RIGHT: 1 Thorough Worked Example (Big Ideas Textbook Method + Blocks + SC-6 Keystrokes + Final Answer)
    left_w = 92.0
    right_w = uw - left_w - 2.5
    right_x = margin + left_w + 2.5
    band_y = 36.8
    band_h = 64.0

    # --- LEFT PANEL: Block Kit & Step-by-Step Instructions ---
    p.rect(margin, band_y, left_w, band_h, fill=WHITE, stroke=INK, r=1.0, line_w=0.3)
    p.rect(margin, band_y, left_w, 5.0, fill=INK, stroke=INK, r=0.8, line_w=0.2)
    p.text(
        margin + 2.5,
        band_y + 3.5,
        f"BLOCK KIT & STEP-BY-STEP GUIDE ({sec['kit_id']}: {sec['kit_name'].upper()})",
        size=1.9,
        bold=True,
        mono=True,
        color=WHITE,
        max_w=left_w - 5.0,
    )

    img_box_x = margin + 2.0
    img_box_y = band_y + 6.0
    img_box_w = 40.0
    img_box_h = 25.5
    p.rect(img_box_x, img_box_y, img_box_w, img_box_h, fill=WHITE, stroke=LIGHT_BORDER, r=0.8, line_w=0.2)
    p.image(ASSETS_MANUALS_DIR / sec["asset_png"], img_box_x + 0.8, img_box_y + 0.8, img_box_w - 1.6, img_box_h - 1.6)

    sch_x = img_box_x + img_box_w + 1.5
    sch_w = left_w - img_box_w - 5.5
    p.draw_block_schematic(sec["diagram_type"], sec["diagram_data"], sch_x, img_box_y, sch_w, img_box_h)

    # Step-by-Step Physical Block Instructions Box (y = band_y + 32.5 .. band_y + 62.5 mm)
    steps_box_y = band_y + 32.5
    steps_box_h = band_h - 34.0
    p.rect(margin + 2.0, steps_box_y, left_w - 4.0, steps_box_h, fill=SUBTLE_HDR, stroke=BORDER, r=0.8, line_w=0.22)
    p.text(
        margin + 3.8,
        steps_box_y + 3.5,
        f"HOW TO BUILD IT WITH {sec['kit_id']} ({sec['kit_name'].upper()}):",
        size=1.85,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=left_w - 7.6,
    )
    sy_cur = steps_box_y + 6.7
    for s_idx, bstep in enumerate(ped["block_steps"][:3], start=1):
        sy_cur = p.para(
            margin + 3.8,
            sy_cur,
            f"Step {s_idx}: {bstep}",
            max_w=left_w - 7.6,
            size=1.92,
            bold=(s_idx == 1),
            color=INK if s_idx == 1 else SLATE,
            leading=1.18,
            max_lines=2,
        )
        sy_cur += 0.55

    # --- RIGHT PANEL: 1 Comprehensive Worked Example ---
    ex1 = sec["examples"][0]
    p.rect(right_x, band_y, right_w, band_h, fill=WHITE, stroke=INK, r=1.0, line_w=0.3)
    p.rect(right_x, band_y, right_w, 5.0, fill=SUBTLE_HDR, stroke=INK, r=0.8, line_w=0.25)
    p.text(
        right_x + 2.5,
        band_y + 3.5,
        f"WORKED EXAMPLE — {ex1['title'].upper()}",
        size=1.95,
        bold=True,
        mono=True,
        color=INK,
        max_w=right_w - 5.0,
    )

    # Problem Statement
    after_prob_y = p.para(
        right_x + 2.8,
        band_y + 8.4,
        f"Problem: {ex1['problem']}",
        max_w=right_w - 5.6,
        size=2.25,
        bold=True,
        color=INK,
        leading=1.2,
        max_lines=2,
    )

    # Big Ideas Textbook Method Step-by-Step Solution
    tb_hdr_y = after_prob_y + 1.0
    p.text(
        right_x + 2.8,
        tb_hdr_y,
        f"Big Ideas Textbook Method ({ped['big_ideas_method']}):",
        size=1.9,
        bold=True,
        color=TEAL_ACCENT,
        max_w=right_w - 5.6,
    )
    after_tb_y = p.para(
        right_x + 2.8,
        tb_hdr_y + 2.8,
        ped["textbook_steps"],
        max_w=right_w - 5.6,
        size=1.95,
        color=INK,
        leading=1.22,
        max_lines=5,
    )

    # Physical Block Takeaway
    blk_note_y = max(after_tb_y + 0.8, band_y + 34.5)
    p.rect(right_x + 2.5, blk_note_y, right_w - 5.0, 9.2, fill=SUBTLE_HDR, stroke=LIGHT_BORDER, r=0.7, line_w=0.2)
    p.para(
        right_x + 4.0,
        blk_note_y + 3.1,
        f"Block Connection ({sec['kit_id']}): {ex1['block_step']}",
        max_w=right_w - 8.0,
        size=1.9,
        color=SLATE,
        leading=1.18,
        max_lines=2,
    )

    # SC-6 Keystrokes
    ky = band_y + band_h - 17.5
    p.text(right_x + 2.8, ky + 2.8, "SC-6 Keystrokes:", size=1.95, bold=True, mono=True, color=INK)
    p.draw_keycap_sequence(ex1["keys"], right_x + 26.5, ky + 0.1, max_w=right_w - 29.0, h=3.7, gap=0.8)

    # Final Answer & Verification Bar (Answer only — zero stack snapshot!)
    bar_y = band_y + band_h - 8.2
    p.line(right_x + 2.2, bar_y, right_x + right_w - 2.2, bar_y, color=INK, width=0.25)
    p.text(
        right_x + 2.8,
        bar_y + 4.8,
        f"Answer: {ex1['ans']}",
        size=2.25,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=right_w * 0.54,
    )
    p.text(
        right_x + right_w - 2.8,
        bar_y + 4.8,
        ex1.get("note", ""),
        size=1.8,
        italic=True,
        color=SLATE,
        align="right",
        max_w=right_w * 0.44,
    )

    # 4. Practice Problems Grid (y = 102.2 .. 269.0 mm, 10 Problems in 5 Rows × 2 Columns)
    hdr_y = 102.2
    p.rect(margin, hdr_y, uw, 5.0, fill=INK, stroke=INK, r=0.7, line_w=0.2)
    p.text(
        margin + 2.5,
        hdr_y + 3.5,
        f"SECTION {sec_num} PRACTICE — WORK OUT EACH PROBLEM & WRITE YOUR ANSWER",
        size=2.0,
        bold=True,
        mono=True,
        color=WHITE,
    )
    p.text(
        margin + uw - 2.5,
        hdr_y + 3.5,
        f"Method Focus: {ped['big_ideas_method']}",
        size=1.8,
        mono=True,
        color="#E2E8F0",
        align="right",
        max_w=88.0,
    )

    grid_y0 = 108.3
    col_w = (uw - 3.0) / 2.0
    row_h = 31.0
    row_gap = 1.05

    pmethods = ped["problem_methods"]
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
        p.rect(px + 2.0, py + 1.6, 5.2, 4.6, fill=badge_fill, stroke=badge_fill, r=0.65, line_w=0.2)
        p.text(px + 4.6, py + 4.8, str(p_num), size=2.2, bold=True, mono=True, color=WHITE, align="center")

        # Track the specific Big Ideas textbook method for this problem tier (NO "LID SOCKET" or keycap filler!)
        m_label = pmethods[0] if part == "A" else (pmethods[1] if part == "B" else pmethods[2])
        tier_prefix = "Application & 2-Way Check" if part == "C" else "Big Ideas Method"
        p.text(
            px + 8.4,
            py + 4.1,
            f"{tier_prefix}: {m_label}",
            size=1.75,
            bold=True,
            mono=True,
            color=TEAL_ACCENT if part == "C" else MUTED,
            max_w=col_w - 10.4,
        )

        # Problem Prompt (top of card)
        p.para(
            px + 8.4,
            py + 7.2,
            prob["prompt"],
            max_w=col_w - 10.4,
            size=2.18,
            bold=True,
            color=INK,
            leading=1.18,
            max_lines=2,
        )

        # Open Workspace Area (py + 12.8 .. py + 25.5 mm — plenty of room to work out the problem!)
        ws_top = py + 12.8
        ws_bot = py + row_h - 5.6
        p.line(px + 2.0, ws_top, px + col_w - 2.0, ws_top, color="#E2E8F0", width=0.2)
        p.text(px + 2.4, ws_top + 2.8, "Work:", size=1.7, italic=True, color=MUTED)

        # Subtle notebook scratch lines on the right half so students can both sketch & write steps
        p.line(px + 50.0, ws_top + 4.5, px + col_w - 2.5, ws_top + 4.5, color="#F1F5F9", width=0.18)
        p.line(px + 50.0, ws_top + 8.8, px + col_w - 2.5, ws_top + 8.8, color="#F1F5F9", width=0.18)

        # Bottom Answer Line (Answers ONLY — zero stack Y|X or checkboxes!)
        p.line(px + 2.0, ws_bot, px + col_w - 2.0, ws_bot, color=LIGHT_BORDER, width=0.22)
        p.text(
            px + col_w - 2.5,
            py + row_h - 1.8,
            "Answer: ________________________________________",
            size=2.0,
            bold=True,
            mono=True,
            color=INK,
            align="right",
        )

    p.text(
        margin,
        p.h - 5.2,
        f"StackCalc SC-6 Textbook Supplement  •  {ped['unit_name']} — Section {sec_num} ({sec['big_ideas_ref']})",
        size=1.9,
        mono=True,
        color=MUTED,
        max_w=uw - 28.0,
    )
    p.text(margin + uw, p.h - 5.2, f"Page {page_num} of 46", size=1.9, bold=True, mono=True, color=INK, align="right")


def generate_student_workbook_pdf(chapters: List[Dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_path), pagesize=letter)
    c.setTitle("StackCalc SC-6 Big Ideas Math Middle School Section-by-Section Supplement Workbook")
    c.setAuthor("StackCalc Learning Lab")

    p = CanvasPage(c, letter)
    draw_student_cover_page(p, chapters)
    c.showPage()

    page_num = 2
    for ch in chapters:
        for sec in ch["sections"]:
            p = CanvasPage(c, letter)
            draw_student_section_page(p, ch, sec, page_num)
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

    # 1. Top Chapter Header (y = 8.5 .. 22.5 mm)
    p.text(
        margin,
        11.8,
        f"STACKCALC SC-6 TEACHER & PARENT COACH GUIDE  •  1-PAGE UNIT SOLUTION KEY (UNIT {ch_num} OF {total_chapters})",
        size=2.15,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
    )
    p.draw_tutorial_keycap(margin + uw - 5.8, 8.8, w=5.0, h=4.2)
    p.text(margin, 17.5, f"Unit {ch_num}: {ch['title']} — Complete Key", size=4.3, bold=True, color=INK, max_w=uw - 10.0)
    p.text(margin, 21.6, f"{ch['big_ideas_book']}  •  Manipulative Kits: {ch['kit_summary']}", size=2.1, bold=True, color=SLATE, max_w=uw)
    p.line(margin, 23.0, margin + uw, 23.0, color=INK, width=0.45)

    # 2. Coaching & Manipulative Setup Strip (y = 24.0 .. 40.5 mm, height = 16.5 mm)
    p.rect(margin, 24.0, uw, 16.5, fill=SUBTLE_HDR, stroke=INK, r=0.9, line_w=0.28)
    p.rect(margin + uw - 26.0, 25.0, 24.5, 14.5, fill=WHITE, stroke=LIGHT_BORDER, r=0.6, line_w=0.2)
    p.image(ASSETS_MANUALS_DIR / ch["hero_png"], margin + uw - 25.5, 25.5, 23.5, 13.5)

    text_w = uw - 30.0
    p.para(
        margin + 2.2,
        27.2,
        f"Target Misconception: {ch['coach_misconception']}",
        max_w=text_w,
        size=1.95,
        bold=True,
        color=INK,
        leading=1.2,
        max_lines=2,
    )
    p.para(
        margin + 2.2,
        32.5,
        f"Hands-On Block Remediation: {ch['coach_remediation']}",
        max_w=text_w,
        size=1.9,
        color=SLATE,
        leading=1.2,
        max_lines=2,
    )
    p.text(
        margin + 2.2,
        38.8,
        "Optional QUEST-01 Scoreboard: 1 '+10' block = Solved 1 Way; stack a 2nd '+10' block (+20) = Solved 2 Ways (Blocks + Textbook/SC-6)!",
        size=1.82,
        bold=True,
        mono=True,
        color=TEAL_ACCENT,
        max_w=text_w,
    )

    # 3. Section-by-Section Complete Answer Key Bands (y = 42.0 .. 269.0 mm)
    secs = ch["sections"]
    n_secs = len(secs)
    avail_h = 227.0
    sec_gap = 1.8
    sec_h = (avail_h - (n_secs - 1) * sec_gap) / n_secs

    for s_idx, sec in enumerate(secs):
        sy = 42.0 + s_idx * (sec_h + sec_gap)
        p.rect(margin, sy, uw, sec_h, fill=WHITE, stroke=INK, r=0.8, line_w=0.28)

        # Section Header Bar (5.0 mm tall)
        p.rect(margin, sy, uw, 5.0, fill=INK, stroke=INK, r=0.6, line_w=0.2)
        ex1 = sec["examples"][0]
        ped = SECTION_PEDAGOGY.get(sec["sec_num"], {})
        method_short = ped.get("big_ideas_method", "")
        p.text(
            margin + 2.0,
            sy + 3.5,
            f"SEC {sec['sec_num']}: {sec['title'].upper()} [{sec['kit_id']}]",
            size=1.9,
            bold=True,
            mono=True,
            color=WHITE,
            max_w=105.0,
        )
        p.text(
            margin + uw - 2.0,
            sy + 3.5,
            f"Method: {method_short}  |  Ex: {ex1['ans']}",
            size=1.75,
            mono=True,
            color="#E2E8F0",
            align="right",
            max_w=85.0,
        )

        # 5 Rows × 2 Columns Table for Problems #1 through #10
        grid_y = sy + 5.2
        grid_h = sec_h - 5.4
        row_h = grid_h / 5.0
        col_w = uw / 2.0

        p.line(margin + col_w, grid_y, margin + col_w, sy + sec_h, color=BORDER, width=0.25)

        for p_idx, prob in enumerate(sec["problems"][:10]):
            r = p_idx // 2
            c = p_idx % 2
            cx = margin + c * col_w
            cy = grid_y + r * row_h

            if r > 0 and c == 0:
                p.line(margin, cy, margin + uw, cy, color=LIGHT_BORDER, width=0.18)

            pnum = prob["num"]
            part = prob.get("part", "A")
            num_lbl = f"#{pnum}{'*' if part == 'C' else ''}:"
            p.text(cx + 1.8, cy + row_h * 0.43, num_lbl, size=1.85, bold=True, mono=True, color=TEAL_ACCENT if part == "C" else INK)

            p.text(cx + 9.2, cy + row_h * 0.43, prob["prompt"], size=1.8, color=SLATE, max_w=col_w - 11.0)

            line2_y = cy + row_h * 0.84
            keys_str = f"SC-6 Keys: {prob['keys']}"
            p.text(cx + 9.2, line2_y, keys_str, size=1.7, mono=True, color=INK, max_w=col_w * 0.54)

            ans_str = f"Ans: {prob['ans']}"
            p.text(cx + col_w - 1.8, line2_y, ans_str, size=1.8, bold=True, mono=True, color=TEAL_ACCENT, align="right", max_w=col_w * 0.38)

    p.text(
        margin,
        p.h - 5.0,
        f"StackCalc SC-6 Coach & Solution Guide (1 Page Per Unit)  •  Unit {ch_num}: {ch['title']}",
        size=1.9,
        mono=True,
        color=MUTED,
        max_w=uw - 38.0,
    )
    p.text(margin + uw, p.h - 5.0, f"Coach Guide Page {ch_num} of {total_chapters}", size=1.9, bold=True, mono=True, color=INK, align="right")


def generate_coach_guide_pdf(chapters: List[Dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_path), pagesize=letter)
    c.setTitle("StackCalc SC-6 Big Ideas Math Middle School 10-Page Coach & Solution Guide")
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
        "# Big Ideas Math Middle School: Section-by-Section Hands-On Block & SC-6 Supplement",
        "",
        "**Grade 6 Complete + Grade 7 Bridge • 10 Units • 45 Textbook Sections • Step-by-Step Block Instructions • 450 Practice Problems**",
        "",
        "<div class=\"hero-buttons\" style=\"margin: 1.25rem 0 1.75rem 0;\">",
        "  <a href=\"../../downloads/worksheets/bigideas_middle_school_sc6_daily_student_workbook.pdf\" class=\"md-button md-button--primary\">📄 Download Student Supplement Workbook PDF (46 Pages • Block Steps & 450 Problems)</a>",
        "  <a href=\"../../downloads/worksheets/bigideas_middle_school_sc6_teacher_coach_guide.pdf\" class=\"md-button\">🔑 Download Compact 10-Page Coach & Answer Key PDF (1 Page Per Unit)</a>",
        "</div>",
        "",
        "!!! abstract \"Designed Around Big Ideas Math Textbook Methods & Hands-On Manipulatives\"",
        "    - **Aligned to Every Unit & Section:** Tracks the exact **Big Ideas Math** textbook methods across all 10 Units and 45 Sections (*Arrays & Division Check*, *Factor Trees*, *Venn GCF/LCM*, *84mm LCD Fraction Towers*, *Reciprocal Multiplication*, *Tape Diagrams*, *Ratio Tables*, *Double Number Lines*, *Distributive Area Models*, *Balance Scale Inverse Operations*, *2D Geometric Nets*, and *5-Number Box Plots*).",
        "    - **Explicit Block Kit & Step-by-Step Instructions:** Every section names which StackCalc Block Kit is used (`COUNT-01`, `PRIME-01`, `FRAC-01`, `PLACE-01`, `ALGB-01`, `RACK-01`, `TIME-01`, `PROB-01`) with **Step 1, Step 2, and Step 3** physical block instructions alongside **1 comprehensive Worked Example** with keystrokes and blocks.",
        "    - **Focus on Concepts, Workspace & Final Answers:** Students never have to write out calculator stack registers (which vary depending on prior values on the stack). Every worksheet question provides generous open workspace to work out the problem using the section's Big Ideas method and write the final answer.",
        "    - **Compact 10-Page Coach Guide:** The **Coach & Solution Guide PDF** fits every unit's misconception coaching, manipulative setup, and all 40–50 section answers onto **1 single page per unit (10 pages total)**.",
        "",
        "---",
        "",
        "## 🏆 Optional Desk Companion: The Simplified 2-Piece `3x1x7U` SC-6 Scoreboard (`QUEST-01`)",
        "",
        "To reward students for trying multiple approaches (e.g., solving with physical blocks *and* verifying with the textbook method or SC-6), pair the workbook with the **`3x1x7U` Gridfinity SC-6 Scoreboard & Token Kit (`QUEST-01`)**:",
        "",
        "| Hardware Component | Dimensions & Gridfinity Standard | How It Works (Zero Sorting, Zero Extra Trays) |",
        "| :--- | :--- | :--- |",
        "| **1. Snapfinity Scoreboard Lid (`1–10` + `100` + `(?)`)** | `125.5 × 42.0 mm` (`3x1` Stackable Lid, `6×2 = 12` sockets) | **Left 5×2 Grid:** Numbered **`1`–`5`** (top row) and **`6`–`10`** (bottom row), matching **Problems `#1–#10`** (or **Units `1–10`**). **Rightmost Column:** Top socket **`100`** (for a 10-block Mastery Tower) and bottom **Question Mark in a Circle (`?`)** tutorial keycap badge. |",
        "| **2. `3x1x7U` Token Bank Box (`QUEST BOARD`)** | `125.5 × 42.0 × 49.0 mm` (`7U` height, `(?` tutorial badge) | Holds all **60 universal `+10` Quarter-Block tokens** in 5 neat layers of 12 (`6×2`) directly on its Gridfinity floor—no separate inner tray needed! |",
        "| **3. 60 Identical `+10` Quarter-Block Tokens** | `19.0 × 19.0 × 8.85 mm` (`7.0 mm` visible `1U` height) | Every token is identical (`+10` on top and all 4 sides):<br>• **1 Block (`+10 pts`)** = Solved 1st Way (Blocks, Textbook Method, *or* SC-6)<br>• **2 Stacked Blocks (`+20 pts`)** = Solved 2nd Way (\"Twin-Way Proof\" *or* Fast `<4s` in `[f]` `[C]` Quiz Mode)<br>• **10 Blocks (`100 pts`)** = **100% Section Mastery!** |",
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
            ped = SECTION_PEDAGOGY.get(sec["sec_num"], {})
            bi_method = ped.get("big_ideas_method", "")
            bsteps = ped.get("block_steps", [])
            tsteps = ped.get("textbook_steps", "").replace("\n", "<br>")
            ex1 = sec["examples"][0]
            keys_fmt = " ".join(f"`[{k}]`" for k in ex1["keys"])

            lines.append(f"### Section {sec['sec_num']}: {sec['title']}")
            lines.append("")
            lines.append(f"**Textbook Alignment:** {sec['big_ideas_ref']} (`{sec['ccss']}`) • **Big Ideas Method:** *{bi_method}* • **Block Kit:** `{sec['kit_id']}` ({sec['kit_name']})")
            lines.append("")
            lines.append(f"![{sec['title']}](../assets/manuals/{sec['asset_png']}){{ width=\"320\" }}")
            lines.append("")
            lines.append(f"> **Key Concept:** {sec['concept']}")
            lines.append("")
            lines.append(f"#### Physical Block Kit Instructions (`{sec['kit_id']}: {sec['kit_name']}`)")
            lines.append("")
            for s_i, bs in enumerate(bsteps, start=1):
                lines.append(f"{s_i}. **Step {s_i}:** {bs}")
            lines.append("")
            lines.append("#### Worked Example (Big Ideas Method + Blocks + SC-6 Keystrokes)")
            lines.append("")
            lines.append("| Problem | Big Ideas Textbook Method Steps | SC-6 Keystrokes | Final Answer |")
            lines.append("| :--- | :--- | :--- | :--- |")
            lines.append(f"| **{ex1['problem']}** | {tsteps} | {keys_fmt} | **{ex1['ans']}** |")
            lines.append("")
            lines.append("#### Section Practice Problems (10 Exercises)")
            lines.append("")
            lines.append("| # | Big Ideas Method Focus | Problem Prompt | Coach Key: SC-6 Keystrokes | Final Answer |")
            lines.append("| :---: | :--- | :--- | :--- | :--- |")
            pmethods = ped.get("problem_methods", ("Guided Method", "Textbook Practice", "Application"))
            for prob in sec["problems"]:
                m_lbl = pmethods[0] if prob["part"] == "A" else (pmethods[1] if prob["part"] == "B" else pmethods[2])
                lines.append(
                    f"| **{prob['num']}** | {m_lbl} | {prob['prompt']} | `{prob['keys']}` | **{prob['ans']}** |"
                )
            lines.append("")
            lines.append("---")
            lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] Synchronized curriculum markdown: {md_path} ({len(lines)} lines)")


def main() -> None:
    total_secs = sum(len(ch["sections"]) for ch in CHAPTERS_DATA)
    total_probs = sum(len(sec["problems"]) for ch in CHAPTERS_DATA for sec in ch["sections"])
    print(f"Loaded {len(CHAPTERS_DATA)} units, {total_secs} sections, {total_probs} practice problems.")
    generate_student_workbook_pdf(CHAPTERS_DATA, STUDENT_PDF)
    generate_coach_guide_pdf(CHAPTERS_DATA, TEACHER_PDF)
    sync_curriculum_markdown(CHAPTERS_DATA, SOURCE_MD)


if __name__ == "__main__":
    main()
