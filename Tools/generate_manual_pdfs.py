#!/usr/bin/env python3
"""
Publication-Grade Multi-Page PDF Manual Generator for StackCalc SC-32 and SC-6.

Builds downloadable, publication-grade masterwork reference manuals from markdown:
- docs/downloads/manuals/sc32-scientific-manual.pdf
- docs/downloads/manuals/sc6-elementary-manual.pdf

Design Strategy: Retrofuturistic Brutalism (Surface Rubric & Aesthetics Strategy)
- Monolithic dark wrap covers (Midnight Navy #28334A & Technical Black #101114) with stark white foil lettering
- Archival white paper (#FFFFFF) interior book layout for crisp physical print reading
- Deep black/charcoal body typography (#101114) with generous 0.75 in (54 pt) margins
- Deep technical navy (#142240) and emerald (#064e3b) headings with crisp section badges
- Monospaced stack dump frames: bordered boxes with crisp dark text on subtle #F5F5F7 fill
- High-contrast squircle cartouches for hardware keycap glyphs ([ENTER], [x⇄y], [Σ+], [LASTX])
- Vector-styled tables with text wrapping and repeating headers
- 100% verified against RPNCore engine (51 Textbook Verification Tests)
"""

import sys
import os
import re
import html
from pathlib import Path
from typing import List, Tuple, Dict, Any, Optional

from reportlab.lib import colors
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, Flowable, Preformatted, HRFlowable, Image as RLImage
)
import PIL.Image
from reportlab.platypus.tableofcontents import TableOfContents, SimpleIndex
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfdoc import PDFObjectReference
from reportlab.pdfgen import canvas

# ---------------------------------------------------------------------------
# Path & Directory Setup
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
WATCH_CALC_ROOT = REPO_ROOT if (REPO_ROOT / "documentation" / "manuals").exists() else (REPO_ROOT.parent / "watch-calc-32")
STACKCALC_ROOT = REPO_ROOT if (REPO_ROOT / "docs").exists() else (REPO_ROOT.parent / "stackcalc")
DOCS_DIR = STACKCALC_ROOT / "docs"
MANUALS_ROOT = (
    WATCH_CALC_ROOT / "documentation" / "manuals"
    if (WATCH_CALC_ROOT / "documentation" / "manuals" / "sc32").exists()
    else DOCS_DIR / "manuals"
)
MANUALS_ASSETS_DIR = (
    MANUALS_ROOT / "assets"
    if (MANUALS_ROOT / "assets" / "layout_data.json").exists()
    else DOCS_DIR / "assets" / "manuals"
)
FONT_DIR = (
    DOCS_DIR / "assets" / "fonts"
    if (DOCS_DIR / "assets" / "fonts" / "SpaceMono-Regular.ttf").exists()
    else (WATCH_CALC_ROOT / "documentation")
)
OUTPUT_DIR = (
    MANUALS_ROOT / "output"
    if (WATCH_CALC_ROOT / "documentation" / "manuals" / "sc32").exists()
    else (DOCS_DIR / "downloads" / "manuals")
)

# ---------------------------------------------------------------------------
# Font Registration (Full Unicode TrueType Body & Monospace Families)
# ---------------------------------------------------------------------------
FONTS_AVAILABLE = False
BOOK_SANS_AVAILABLE = False
MATH_SANS_AVAILABLE = False
try:
    if (FONT_DIR / "SpaceMono-Regular.ttf").exists():
        pdfmetrics.registerFont(TTFont("SpaceMono", str(FONT_DIR / "SpaceMono-Regular.ttf")))
        pdfmetrics.registerFont(TTFont("SpaceMono-Bold", str(FONT_DIR / "SpaceMono-Bold.ttf")))
        pdfmetrics.registerFontFamily(
            "SpaceMono",
            normal="SpaceMono",
            bold="SpaceMono-Bold",
            italic="SpaceMono",
            boldItalic="SpaceMono-Bold",
        )
        pdfmetrics.registerFont(TTFont("Terminus", str(FONT_DIR / "TerminusTTF-4.49.3.ttf")))
        pdfmetrics.registerFont(TTFont("Terminus-Bold", str(FONT_DIR / "TerminusTTF-Bold-4.49.3.ttf")))
        pdfmetrics.registerFontFamily(
            "Terminus",
            normal="Terminus",
            bold="Terminus-Bold",
            italic="Terminus",
            boldItalic="Terminus-Bold",
        )
        if (FONT_DIR / "Tiny5-Regular.ttf").exists():
            pdfmetrics.registerFont(TTFont("Tiny5", str(FONT_DIR / "Tiny5-Regular.ttf")))
        FONTS_AVAILABLE = True
    arial_dir = Path("/System/Library/Fonts/Supplemental")
    if (arial_dir / "Arial.ttf").exists() and (arial_dir / "Arial Bold.ttf").exists():
        pdfmetrics.registerFont(TTFont("BookSans", str(arial_dir / "Arial.ttf")))
        pdfmetrics.registerFont(TTFont("BookSans-Bold", str(arial_dir / "Arial Bold.ttf")))
        italic_ttf = arial_dir / ("Arial Italic.ttf" if (arial_dir / "Arial Italic.ttf").exists() else "Arial.ttf")
        bi_ttf = arial_dir / ("Arial Bold Italic.ttf" if (arial_dir / "Arial Bold Italic.ttf").exists() else "Arial Bold.ttf")
        pdfmetrics.registerFont(TTFont("BookSans-Italic", str(italic_ttf)))
        pdfmetrics.registerFont(TTFont("BookSans-BoldItalic", str(bi_ttf)))
        pdfmetrics.registerFontFamily(
            "BookSans",
            normal="BookSans",
            bold="BookSans-Bold",
            italic="BookSans-Italic",
            boldItalic="BookSans-BoldItalic",
        )
        BOOK_SANS_AVAILABLE = True
    try:
        import matplotlib
        dejavu_dir = Path(matplotlib.get_data_path()) / "fonts" / "ttf"
        if (dejavu_dir / "DejaVuSans.ttf").exists():
            pdfmetrics.registerFont(TTFont("MathSans", str(dejavu_dir / "DejaVuSans.ttf")))
            bold_dj = dejavu_dir / ("DejaVuSans-Bold.ttf" if (dejavu_dir / "DejaVuSans-Bold.ttf").exists() else "DejaVuSans.ttf")
            it_dj = dejavu_dir / ("DejaVuSans-Oblique.ttf" if (dejavu_dir / "DejaVuSans-Oblique.ttf").exists() else "DejaVuSans.ttf")
            bi_dj = dejavu_dir / ("DejaVuSans-BoldOblique.ttf" if (dejavu_dir / "DejaVuSans-BoldOblique.ttf").exists() else "DejaVuSans-Bold.ttf")
            pdfmetrics.registerFont(TTFont("MathSans-Bold", str(bold_dj)))
            pdfmetrics.registerFont(TTFont("MathSans-Italic", str(it_dj)))
            pdfmetrics.registerFont(TTFont("MathSans-BoldItalic", str(bi_dj)))
            pdfmetrics.registerFontFamily(
                "MathSans",
                normal="MathSans",
                bold="MathSans-Bold",
                italic="MathSans-Italic",
                boldItalic="MathSans-BoldItalic",
            )
            MATH_SANS_AVAILABLE = True
    except Exception:
        pass
except Exception as e:
    print(f"[WARN] Could not register TrueType fonts: {e}. Falling back to standard Helvetica/Courier.")

FONT_BODY = "BookSans" if BOOK_SANS_AVAILABLE else "Helvetica"
FONT_BODY_BOLD = "BookSans-Bold" if BOOK_SANS_AVAILABLE else "Helvetica-Bold"
FONT_BODY_ITALIC = "BookSans-Italic" if BOOK_SANS_AVAILABLE else "Helvetica-Oblique"
FONT_MATH = "MathSans" if MATH_SANS_AVAILABLE else FONT_BODY
FONT_MONO = "SpaceMono" if FONTS_AVAILABLE else "Courier"
FONT_MONO_BOLD = "SpaceMono-Bold" if FONTS_AVAILABLE else "Courier-Bold"
FONT_DISPLAY = "Terminus" if FONTS_AVAILABLE else "Courier"
FONT_DISPLAY_BOLD = "Terminus-Bold" if FONTS_AVAILABLE else "Courier-Bold"
FONT_KEYCAP = "SpaceMono-Bold" if FONTS_AVAILABLE else "Courier-Bold"

# ---------------------------------------------------------------------------
# Color Palettes & Helpers
# ---------------------------------------------------------------------------
def to_color(c: Any) -> Color:
    if isinstance(c, Color):
        return c
    return HexColor(str(c))

# KDP Black & White Cost-Optimized Interior Mode (Default: True -> saves ~77% print cost vs Premium Color)
BW_PRINT_INTERIOR = True

# SC-32 Scientific Palette (Cover & Optional Color Mode)
SC32_COVER_BG = "#111318"        # Sculptural Matte Obsidian
SC32_PRIMARY = "#111827" if BW_PRINT_INTERIOR else "#142240"
SC32_ACCENT = "#000000" if BW_PRINT_INTERIOR else "#0284c7"
SC32_COVER_ACCENT = "#FF5500"    # International Orange / Dieter Rams Signal Accent

# SC-6 Elementary Palette (Cover & Optional Color Mode)
SC6_COVER_BG = "#111318"         # Sculptural Matte Obsidian
SC6_PRIMARY = "#111827" if BW_PRINT_INTERIOR else "#064e3b"
SC6_ACCENT = "#000000" if BW_PRINT_INTERIOR else "#059669"
SC6_COVER_ACCENT = "#059669"     # Vibrant Emerald Accent

# Print Book Interior Palette (Archival White Paper — High-Contrast KDP B&W Ready)
PAGE_BG = "#ffffff"              # Pure Archival White
TEXT_MAIN = "#000000" if BW_PRINT_INTERIOR else "#101114"
TEXT_MUTED = "#3f3f46"           # High-contrast dark slate for crisp B&W laser printing
STACK_FRAME_BG = "#f4f4f5"       # Clean 4% gray fill
DIVIDER_HEX = "#d4d4d8"          # Crisp rule border
CALLOUT_BG_SC32 = "#f4f4f5" if BW_PRINT_INTERIOR else "#f0f9ff"
CALLOUT_BG_SC6 = "#f4f4f5" if BW_PRINT_INTERIOR else "#f0fdf4"

# Exterior Cover Gallery & Foil Typography
COVER_GALLERY_IVORY = "#F7F4EB"  # Warm Archival Gallery Paper (NYT Bestseller Trade Matte)
COVER_INK_OBSIDIAN = "#0F172A"   # Deep Editorial Ink
COVER_FOIL_WHITE = "#ffffff"     # Stark White
COVER_FOIL_CREAM = "#e2e8f0"     # Warm Silver-Cream
COVER_TAXONOMY_MUTED = "#64748B" # Muted Editorial Slate

# 6.00 x 9.00 in Trade Paperback & Hardcover Geometry (432.0 x 648.0 pt)
MARGIN_PT = 40.0                 # 0.556 in base margin (shifted +/- 14pt -> 0.750 in gutter / 0.361 in outside)
PAGE_WIDTH = 432.0               # 6.00 in trade trim width
PAGE_HEIGHT = 648.0              # 9.00 in trade trim height
PRINTABLE_WIDTH = PAGE_WIDTH - (2 * MARGIN_PT)  # 352.0 pt (4.89 in)


def to_roman(n: int) -> str:
    """Converts a positive integer to lowercase Roman numerals (i, ii, iii, iv, v...) for Front Matter."""
    if n <= 0:
        return "i"
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]
    roman_num = ""
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syb[i]
            n -= val[i]
        i += 1
    return roman_num


# ---------------------------------------------------------------------------
# Flowables for PDF Outlines, Chapter Tracking & KDP Pagination
# ---------------------------------------------------------------------------
class BookmarkFlowable(Flowable):
    """Inserts a PDF bookmark and outline entry into the PDF catalog."""
    def __init__(self, key: str, title: str, level: int = 0):
        super().__init__()
        self.key = key
        self.title = title
        self.level = level
        self.width = 0
        self.height = 0

    def draw(self):
        pg = self.canv._pageNumber
        if self.level == 0:
            self.canv.is_chapter_opener_page = True
        dest = self.canv.bookmarkPage(self.key)
        dest.setPage(PDFObjectReference(f"Page{pg}"))
        self.canv.addOutlineEntry(self.title, self.key, level=self.level, closed=False)


class ChapterTracker(Flowable):
    """Tracks the active chapter title on the canvas for running headers."""
    def __init__(self, chapter_title: str):
        super().__init__()
        self.chapter_title = chapter_title
        self.width = 0
        self.height = 0

    def draw(self):
        self.canv.current_chapter_title = self.chapter_title


class EnsureRectoPageFlowable(Flowable):
    """
    If placed at the start of a page and the current physical page is even (verso),
    consumes the even page as an intentional blank verso page so the next flowable
    begins on a right-hand odd (recto) page.
    """
    def __init__(self):
        super().__init__()
        self.width = 0
        self.height = 0
        self._is_even = False

    def wrap(self, availWidth, availHeight):
        pg = getattr(getattr(self, "canv", None), "_pageNumber", 1)
        if pg % 2 == 0:
            self._is_even = True
            return (0, max(1.0, availHeight - 1.0))
        self._is_even = False
        return (0, 0)

    def draw(self):
        if self._is_even:
            self.canv.current_chapter_title = "BLANK_PAGE"


class StartArabicPaginationFlowable(Flowable):
    """Marks the transition from Front Matter (Roman i, ii, iii...) to Main Text (Arabic 1, 2, 3...)."""
    def __init__(self):
        super().__init__()
        self.width = 0
        self.height = 2.0

    def wrap(self, availWidth, availHeight):
        return (0, 2.0)

    def draw(self):
        self.canv.arabic_start_raw_page = self.canv._pageNumber


class ManualDocTemplate(SimpleDocTemplate):
    """
    Two-pass publication document template that intercepts flowables
    and notifies TableOfContents and SimpleIndex with exact Arabic page numbers
    synchronized with the printed page footers.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arabic_start_page = 7

    def afterFlowable(self, flowable):
        super().afterFlowable(flowable)
        if isinstance(flowable, StartArabicPaginationFlowable):
            self.arabic_start_page = self.page
        arabic_pg = max(1, self.page - getattr(self, "arabic_start_page", 7) + 1)
        if hasattr(flowable, '_toc_info'):
            level, text, key = flowable._toc_info
            self.notify('TOCEntry', (level, text, arabic_pg, key))
        if hasattr(flowable, '_index_terms'):
            for term in flowable._index_terms:
                self.notify('IndexEntry', (term, arabic_pg))


# ---------------------------------------------------------------------------
# Two-Pass NumberedCanvas for KDP Interior Manuscript (Mirrored Gutter & Folios)
# ---------------------------------------------------------------------------
KDP_GUTTER_SHIFT_PT = 14.0  # Shifts 40pt base margin to 54pt (0.750 in) Inside Gutter & 26pt (0.361 in) Outside Margin

class NumberedCanvas(canvas.Canvas):
    """
    Two-pass KDP 6x9 Trade Interior Manuscript canvas:
    - Zero covers inside the interior PDF (covers are separate full-wrap files).
    - Front Matter (Pages i, ii, iii, iv, v...): Suppresses headers/footers on Half-Title,
      Series Frontispiece, and Full Title pages; uses lowercase Roman numerals on Copyright & TOC.
    - Main Text & Appendices (Pages 1, 2, 3...): Starts on an odd (recto) page, uses Arabic
      folios on the outside bottom corner, suppresses top running header on chapter opening pages,
      and shifts content by +/- 14pt for KDP's 0.750 in inside binding gutter.
    - Back Matter: Appends a clean blank final even page reserved for KDP's manufacturing barcode.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []
        self.doc_title = "THINKING IN THE STACK"
        self.primary_hex = SC32_PRIMARY
        self.cover_bg_hex = SC32_COVER_BG
        self.cover_accent_hex = SC32_COVER_ACCENT
        self.doc_code = "STK-REF-32-V2"
        self.current_chapter_title = ""
        self.is_chapter_opener_page = False
        self.arabic_start_raw_page = 7
        self.is_sc32 = True

    def showPage(self):
        state = dict(self.__dict__)
        state["page_chapter_title"] = getattr(self, "current_chapter_title", "")
        state["page_is_opener"] = getattr(self, "is_chapter_opener_page", False)
        self._saved_page_states.append(state)
        self.is_chapter_opener_page = False
        self._startPage()

    def save(self):
        # Determine where Arabic Page 1 begins across saved page states
        arabic_start = 7
        for st in self._saved_page_states:
            if "arabic_start_raw_page" in st and st["arabic_start_raw_page"] != 7:
                arabic_start = st["arabic_start_raw_page"]
                break
        for idx_s, st in enumerate(self._saved_page_states):
            ch_t = st.get("page_chapter_title", "")
            if ch_t not in ("HALF TITLE", "SERIES FRONTISPIECE", "TITLE PAGE", "COPYRIGHT AND COLOPHON", "TABLE OF CONTENTS", "BLANK_PAGE"):
                arabic_start = idx_s + 1
                break

        # KDP reserves the final page of the interior block for its manufacturing barcode.
        # Ensure at least 1 trailing blank page at the end AND ensure total page count is an EVEN integer.
        if self._saved_page_states:
            last_blank = dict(self._saved_page_states[-1])
            last_blank["_code"] = []
            last_blank["page_chapter_title"] = "BLANK_PAGE"
            last_blank["page_is_opener"] = False
            last_blank["_pageNumber"] = len(self._saved_page_states) + 1
            self._saved_page_states.append(last_blank)

            if len(self._saved_page_states) % 2 == 1:
                even_blank = dict(last_blank)
                even_blank["_code"] = []
                even_blank["page_chapter_title"] = "BLANK_PAGE"
                even_blank["page_is_opener"] = False
                even_blank["_pageNumber"] = len(self._saved_page_states) + 1
                self._saved_page_states.append(even_blank)

        total_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            # Apply KDP Mirrored Gutter Shift (+14pt on odd recto pages -> 0.750 in left gutter;
            # -14pt on even verso pages -> 0.750 in right gutter)
            gutter_shift = KDP_GUTTER_SHIFT_PT if (self._pageNumber % 2 == 1) else -KDP_GUTTER_SHIFT_PT
            flowables_code = list(self._code)
            self._code = [f"q 1 0 0 1 {gutter_shift:.2f} 0 cm"] + flowables_code + ["Q"]
            self.draw_interior_page_decorations(
                total_pages,
                state.get("page_chapter_title", ""),
                is_opener=state.get("page_is_opener", False),
                arabic_start=arabic_start,
                gutter_shift=gutter_shift
            )
            super().showPage()
        super().save()

    def draw_interior_page_decorations(
        self,
        total_pages: int,
        chapter_title: str,
        is_opener: bool = False,
        arabic_start: int = 7,
        gutter_shift: float = 0.0
    ):
        """
        Draws traditional 6x9 trade book running headers and outside folios:
        - Display Front Matter (Half-Title, Series, Title) and Blank Pages: completely blank (no header/footer).
        - Copyright & Table of Contents: lowercase Roman numerals (iv, v, vi...) on outside footer.
        - Chapter Openers: no top running header; Arabic folio on outside footer.
        - Regular Body Pages: mirrored running header + outside Arabic folio (1, 2, 3...).
        """
        if chapter_title in ("HALF TITLE", "SERIES FRONTISPIECE", "TITLE PAGE", "BLANK_PAGE"):
            return

        self.saveState()
        w, h = PAGE_WIDTH, PAGE_HEIGHT
        left_x = MARGIN_PT + gutter_shift
        right_x = (w - MARGIN_PT) + gutter_shift
        is_odd = (self._pageNumber % 2 == 1)
        is_front_matter = (self._pageNumber < arabic_start) or (chapter_title in ("COPYRIGHT AND COLOPHON", "TABLE OF CONTENTS"))

        # 1. Top Running Header (Suppressed on Copyright Page and on Chapter Opening Pages)
        show_header = (not is_opener) and (chapter_title != "COPYRIGHT AND COLOPHON")
        if show_header:
            self.setStrokeColor(to_color(DIVIDER_HEX))
            self.setLineWidth(0.45)
            self.line(left_x, h - 29, right_x, h - 29)

            doc_hdr = "THINKING IN THE STACK" if getattr(self, "is_sc32", True) else "FROM BLOCKS TO THE STACK"
            disp_title = (chapter_title[:42] + ("..." if len(chapter_title) > 42 else "")) if chapter_title else ""

            if is_odd:
                # Recto (Odd): Chapter title on outside (right), Book title on inside (left)
                self.setFont(FONT_BODY, 6.8)
                self.setFillColor(to_color(TEXT_MUTED))
                self.drawString(left_x, h - 24, doc_hdr)
                if disp_title:
                    self.setFont(FONT_BODY_BOLD, 6.8)
                    self.setFillColor(to_color(TEXT_MAIN))
                    self.drawRightString(right_x, h - 24, disp_title)
            else:
                # Verso (Even): Book title on outside (left), Chapter title on inside (right)
                self.setFont(FONT_BODY_BOLD, 6.8)
                self.setFillColor(to_color(TEXT_MAIN))
                self.drawString(left_x, h - 24, doc_hdr)
                if disp_title:
                    self.setFont(FONT_BODY, 6.8)
                    self.setFillColor(to_color(TEXT_MUTED))
                    self.drawRightString(right_x, h - 24, disp_title)

        # 2. Bottom Folio (Roman i, ii, iii in Front Matter; Arabic 1, 2, 3 in Main Text)
        if is_front_matter:
            folio_str = to_roman(self._pageNumber)
        else:
            folio_str = str(max(1, self._pageNumber - arabic_start + 1))

        self.setFont(FONT_BODY_BOLD if not is_front_matter else FONT_BODY_ITALIC, 8.0)
        self.setFillColor(to_color(TEXT_MAIN))
        if is_odd:
            self.drawRightString(right_x, 22, folio_str)
        else:
            self.drawString(left_x, 22, folio_str)

        self.restoreState()


# ---------------------------------------------------------------------------
# LaTeX Math & Typographic Sanitization
# ---------------------------------------------------------------------------
MATH_REPLACEMENTS = [
    (r"\longleftrightarrow", "↔"),
    (r"\rightleftharpoons", "⇌"),
    (r"\Longleftrightarrow", "⇔"),
    (r"\longrightarrow", "→"),
    (r"\longleftarrow", "←"),
    (r"\Longrightarrow", "⇒"),
    (r"\leftrightarrow", "↔"),
    (r"\leftarrow", "←"),
    (r"\rightarrow", "→"),
    (r"\implies", "⇒"),
    (r"\iff", "⇔"),
    (r"\parallel", "∥"),
    (r"\times", "×"),
    (r"\div", "÷"),
    (r"\cdot", "·"),
    (r"\cdots", "⋯"),
    (r"\dots", "..."),
    (r"\ldots", "..."),
    (r"\pm", "±"),
    (r"\mp", "∓"),
    (r"\approx", "≈"),
    (r"\equiv", "≡"),
    (r"\propto", "∝"),
    (r"\infty", "∞"),
    (r"\partial", "∂"),
    (r"\nabla", "∇"),
    (r"\angle", "∠"),
    (r"\lVert", "‖"),
    (r"\rVert", "‖"),
    (r"\Vert", "‖"),
    (r"\lvert", "|"),
    (r"\rvert", "|"),
    (r"\vert", "|"),
    (r"\Box", "□"),
    (r"\oplus", "⊕"),
    (r"\prime", "′"),
    (r"\langle", "⟨"),
    (r"\rangle", "⟩"),
    (r"\alpha", "α"),
    (r"\beta", "β"),
    (r"\gamma", "γ"),
    (r"\Gamma", "Γ"),
    (r"\delta", "δ"),
    (r"\Delta", "Δ"),
    (r"\varepsilon", "ε"),
    (r"\epsilon", "ε"),
    (r"\zeta", "ζ"),
    (r"\eta", "η"),
    (r"\theta", "θ"),
    (r"\Theta", "Θ"),
    (r"\kappa", "κ"),
    (r"\lambda", "λ"),
    (r"\Lambda", "Λ"),
    (r"\mu", "μ"),
    (r"\nu", "ν"),
    (r"\xi", "ξ"),
    (r"\pi", "π"),
    (r"\Pi", "Π"),
    (r"\rho", "ρ"),
    (r"\sigma", "σ"),
    (r"\Sigma", "∑"),
    (r"\tau", "τ"),
    (r"\varphi", "φ"),
    (r"\phi", "φ"),
    (r"\Phi", "Φ"),
    (r"\chi", "χ"),
    (r"\psi", "ψ"),
    (r"\Psi", "Ψ"),
    (r"\omega", "ω"),
    (r"\Omega", "Ω"),
    (r"\sum", "∑"),
    (r"\prod", "∏"),
    (r"\iiint", "∭"),
    (r"\iint", "∬"),
    (r"\oint", "∮"),
    (r"\int", "∫"),
    (r"\sqrt", "√"),
    (r"\circ", "°"),
    (r"\qquad", "    "),
    (r"\quad", "  "),
    (r"\,", " "),
    (r"\;", " "),
    (r"\:", " "),
    (r"\!", ""),
]
MATH_REPLACEMENTS.sort(key=lambda x: -len(x[0]))


def _extract_braced(text: str, open_brace_idx: int):
    """Returns (content_inside_braces, index_after_closing_brace) or (None, -1)."""
    if open_brace_idx >= len(text) or text[open_brace_idx] != "{":
        return None, -1
    depth = 1
    i = open_brace_idx + 1
    while i < len(text) and depth > 0:
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
        i += 1
    if depth != 0:
        return None, -1
    return text[open_brace_idx + 1 : i - 1], i


def replace_latex_frac(text: str) -> str:
    """Recursively replaces \\frac{num}{den} and \\binom{n}{k} handling nested braces."""
    for cmd, fmt in [(r"\dfrac", "frac"), (r"\tfrac", "frac"), (r"\frac", "frac"), (r"\binom", "binom")]:
        while True:
            idx = text.find(cmd + "{")
            if idx == -1:
                break
            num, i = _extract_braced(text, idx + len(cmd))
            if num is None:
                break
            den, j = _extract_braced(text, i)
            if den is None:
                break
            if fmt == "binom":
                text = text[:idx] + f"C({num}, {den})" + text[j:]
            else:
                text = text[:idx] + f"({num} / {den})" + text[j:]
    return text


def replace_latex_sqrt(text: str) -> str:
    """Replaces \\sqrt[n]{arg} and \\sqrt{arg} cleanly without leaving stray braces."""
    while True:
        m = re.search(r'\\sqrt(?:\[([^\]]+)\])?\{', text)
        if not m:
            break
        root_deg = m.group(1)
        brace_start = m.end() - 1
        radicand, end_idx = _extract_braced(text, brace_start)
        if radicand is None:
            break
        rad_clean = radicand.strip()
        prefix = "∛" if root_deg == "3" else ("∜" if root_deg == "4" else (f"root({root_deg}, " if root_deg else "√"))
        if root_deg and root_deg not in ("3", "4"):
            rep = f"{prefix}{rad_clean})"
        elif re.match(r'^[A-Za-z0-9\\]+$', rad_clean):
            rep = f"{prefix}{rad_clean}"
        else:
            rep = f"{prefix}({rad_clean})"
        text = text[:m.start()] + rep + text[end_idx:]
    return text


def replace_latex_bold(text: str) -> str:
    """Recursively replaces \\mathbf{...}, \\textbf{...}, and \\boldsymbol{...} handling nested braces."""
    pattern = re.compile(r'\\(?:mathbf|textbf|boldsymbol)\s*\{')
    start_pos = 0
    while True:
        m = pattern.search(text, start_pos)
        if not m:
            break
        brace_idx = m.end() - 1
        content, end_idx = _extract_braced(text, brace_idx)
        if content is None:
            start_pos = m.end()
            continue
        inner = replace_latex_bold(content)
        rep = f"<b>{inner}</b>"
        text = text[:m.start()] + rep + text[end_idx:]
        start_pos = m.start() + len(rep)
    return text


def clean_latex_math(text: str) -> str:
    """Converts LaTeX math expressions into vector-sharp unicode typography."""
    # Strip backticks inside math spans
    text = re.sub(r'`\[([^`]+)\]`', r'[\1]', text)
    text = text.replace('`', '')

    # Handle \begin{...} / \end{...} environments (aligned, cases, pmatrix, bmatrix) and \\ BEFORE r"\ "
    if r"\begin{" in text:
        text = re.sub(r'\s*&\s*=', ' = ', text)
        text = re.sub(r'\s*&\s*', '  ', text)
    text = re.sub(r'\\begin\{[^}]*\}', '', text)
    text = re.sub(r'\\end\{[^}]*\}', '', text)
    text = text.replace(r"\\", "; ")

    # Unescape LaTeX literal escapes before XML escaping
    text = text.replace(r"\%", "%").replace(r"\$", "$").replace(r"\_", "_")
    text = text.replace(r"\{", "(").replace(r"\}", ")")
    text = text.replace(r"\ ", " ")

    # Escape XML special characters FIRST so < and > in inequalities never corrupt ReportLab tags
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    # 1. Strip \left and \right delimiters FIRST so \le does not corrupt \left to ≤ft
    text = re.sub(r'\\left\s*([(\[{|.])', r'\1', text)
    text = re.sub(r'\\right\s*([)\]}|.])', r'\1', text)
    text = re.sub(r'\\left\b', '', text)
    text = re.sub(r'\\right\b', '', text)

    # 2. Floor and ceil delimiters
    text = re.sub(r'\\lfloor\b', '⌊', text)
    text = re.sub(r'\\rfloor\b', '⌋', text)
    text = re.sub(r'\\lceil\b', '⌈', text)
    text = re.sub(r'\\rceil\b', '⌉', text)
    text = re.sub(r'\\lVert\b', '‖', text)
    text = re.sub(r'\\rVert\b', '‖', text)
    text = re.sub(r'\\Vert\b', '‖', text)
    text = re.sub(r'\\lvert\b', '|', text)
    text = re.sub(r'\\rvert\b', '|', text)
    text = re.sub(r'\\vert\b', '|', text)

    # 3. Handle fractions, binomials, roots, and bold macros with balanced braces
    text = replace_latex_frac(text)
    text = replace_latex_sqrt(text)
    text = replace_latex_bold(text)

    # 4. Handle font, text, and accent macros (iterated for nesting)
    for _ in range(3):
        text = re.sub(r'\\(?:text|mathrm|operatorname|mathcal|mathbb|mathbin|mathrel|mathtt|texttt|underline)\{([^{}]*)\}', r'\1', text)
        text = re.sub(r'\\(?:mathbf|textbf|boldsymbol)\{([^{}]*)\}', r'<b>\1</b>', text)
        text = re.sub(r'\\mathit\{([^{}]*)\}', r'<i>\1</i>', text)
        text = re.sub(r'\\(?:bar|overline)\{([^{}]*)\}', r'\1̄', text)
        text = re.sub(r'\\hat\{([^{}]*)\}', r'\1̂', text)
        text = re.sub(r'\\dot\{([^{}]*)\}', r'\1̇', text)
        text = re.sub(r'\\vec\{([^{}]*)\}', r'\1⃗', text)
        text = re.sub(r'\\pmod\{((?:[^{}]|\{[^{}]*\})*)\}', r' (mod \1)', text)
        text = re.sub(r'\\xrightarrow\{([^{}]*)\}', r'→[\1]', text)
        text = re.sub(r'\\hspace\{[^{}]*\}', ' ', text)

    text = re.sub(r'\\Large\b', '', text)
    text = re.sub(r'\\bmod\b', ' mod ', text)
    # Normalize degree superscripts (^\circ, ^{\circ}, ^°) into ° before general replacements
    text = re.sub(r'\^\s*\{?\s*(?:\\circ|°)\s*\}?', '°', text)

    # 5. Relational operators and arrows with word boundaries
    text = re.sub(r'\\le\b', '≤', text)
    text = re.sub(r'\\ge\b', '≥', text)
    text = re.sub(r'\\leq\b', '≤', text)
    text = re.sub(r'\\geq\b', '≥', text)
    text = re.sub(r'\\ll\b', '≪', text)
    text = re.sub(r'\\gg\b', '≫', text)
    text = re.sub(r'\\ne\b', '≠', text)
    text = re.sub(r'\\neq\b', '≠', text)
    text = re.sub(r'\\sim\b', '~', text)
    text = re.sub(r'\\in\b', '∈', text)
    text = re.sub(r'\\mid\b', '|', text)
    text = re.sub(r'\\to\b', '→', text)
    text = re.sub(r'\\pm\b', '±', text)

    # 6. General symbol replacements
    for pat, rep in MATH_REPLACEMENTS:
        text = text.replace(pat, rep)

    # Clean any residual ^° into °
    text = text.replace("^°", "°")

    # 7. Clean empty braces before superscripts/subscripts (e.g., {}^{40}K)
    text = text.replace("{}", "")
    for _ in range(2):
        text = re.sub(r'\^\{([^{}]*)\}', r'<sup>\1</sup>', text)
        text = re.sub(r'_\{([^{}]*)\}', r'<sub>\1</sub>', text)
    text = re.sub(r'\^([0-9a-zA-Z+-]+)', r'<sup>\1</sup>', text)
    text = re.sub(r'_([0-9a-zA-Z+-]+)', r'<sub>\1</sub>', text)

    # Flatten any nested <sup>...<sup>...</sup></sup> or <sub>...<sub>...</sub></sub>
    text = re.sub(r'<sup>([^<]*)<sup>([^<]*)</sup>([^<]*)</sup>', r'<sup>\1^\2\3</sup>', text)
    text = re.sub(r'<sub>([^<]*)<sub>([^<]*)</sub>([^<]*)</sub>', r'<sub>\1_\2\3</sub>', text)

    # Strip remaining LaTeX command backslashes and leftover grouping braces
    text = re.sub(r'\\([a-zA-Z]+)', r'\1', text)
    text = text.replace("{", "").replace("}", "")
    # Use <super rise='2.5' size='6.5'> (+2.5pt) and <sub rise='1.8' size='6.5'> (-1.8pt in ReportLab)
    text = re.sub(r'<sup>(.*?)</sup>', r"<super rise='2.5' size='6.5'>\1</super>", text)
    text = re.sub(r'<sub>(.*?)</sub>', r"<sub rise='1.8' size='6.5'>\1</sub>", text)
    # Keep scientific notation (e.g., 6.6743 × 10^-11) on a single line using non-breaking spaces
    text = re.sub(r'(\d)\s*([×·])\s*(10\b)', "\\1\u00a0\\2\u00a0\\3", text)
    return _protect_special_unicode_glyphs(text.strip())


_MATH_SANS_GLYPH_RE = re.compile(
    r'([⊕⊗⊙⊖⊘⊞⊟⊠⊡⊢⊣⊤⊥⊨⊩⊪⊫⊬⊭⊮⊯⊰⊱⊲⊳⊴⊵⊶⊷⊸⊹⊺⊻⊼⊽⊾⊿⋀⋁⋂⋃⋄⋅⋆⋇⋈⋉⋊⋋⋌⋍⋎⋏⋐⋑⋒⋓⋔⋕⋖⋗⋘⋙⋚⋛⋜⋝⋞⋟⋠⋡⋢⋣⋤⋥⋦⋧⋨⋩⋪⋫⋬⋭⋮⋯⋰⋱'
    r'⇒⇔⇐⇑⇓⇕↦↪↩↼⇀↽⇁⇌⇋∀∃∅∇∈∉∋∌∏∐∓∔∕∖∗∘∙∛∜∝∟∠∡∢∣∤∥∦∧∨∬∭∮∯∰∱∲∳∴∵∶∷∸∹∺∻∼∽∾∿≀≁≂≃≄≅≆≇≉≊≋≌≍≎≏≐≑≒≓≔≕≖≗≘≙≚≛≜≝≞≟'
    r'≢≣≦≧≨≩≪≫≬≭≮≯≰≱≲≳≴≵≶≷≸≹≺≻≼≽≾≿⊀⊁⊂⊃⊄⊅⊆⊇⊈⊉⊊⊋⊌⊍⊎⊏⊐⊑⊒⊓⊔⌊⌋⌈⌉⟨⟩⟪⟫⟬⟭⟮⟯])'
)


def _protect_special_unicode_glyphs(text: str) -> str:
    """
    Wraps specialized mathematical/calculator Unicode glyphs (⊕, ⇒, ⇔, ∈, ∇, ∠, ∝, ⊥, ∥, ⌊, ⌋, ⌈, ⌉, etc.)
    that are absent in Arial with DejaVuSans (MathSans) or Terminus so zero tofu boxes (□) ever appear.
    """
    text = text.replace("⇄", "↔").replace("↰", "↖").replace("↱", "↗").replace("▸", "→").replace("^°", "°")
    text = text.replace("🎲", "[DICE]").replace("🕒", "[CLOCK]").replace("▦", "[FRAME]")
    if MATH_SANS_AVAILABLE:
        text = _MATH_SANS_GLYPH_RE.sub(f"<font face='{FONT_MATH}'>\\1</font>", text)
    elif FONTS_AVAILABLE:
        text = re.sub(r'([∥⌊⌋⌈⌉])', f"<font face='{FONT_DISPLAY}'>\\1</font>", text)
    else:
        text = text.replace("∥", "||").replace("⌊", "floor(").replace("⌋", ")").replace("⌈", "ceil(").replace("⌉", ")")
    return text


# ---------------------------------------------------------------------------
# Authentic Paper-Theme Button Keycap Image Engine (Zero Line-Split Keycaps)
# ---------------------------------------------------------------------------
_PAPER_KEYCAP_ATLAS: Dict[bool, Dict[Tuple[str, int, int], Tuple[Path, int, int]]] = {}
_PAPER_FALLBACK_CACHE: Dict[Tuple[bool, str], Tuple[Path, int, int]] = {}
_KEYCAP_CACHE_DIR = Path("/tmp/stackcalc_paper_keycaps_v5")


def _ensure_paper_keycap_atlas(is_sc32: bool) -> Dict[Tuple[str, int, int], Tuple[Path, int, int]]:
    """
    Extracts all 43 physical primary buttons, right-shifted pill boxes, and left-shifted
    legends directly from the Paper-theme calculator renders (`sc32_hero_stack.png` and
    `sc6_hero_calculator.png`) and caches them as high-resolution PNG files.
    """
    if is_sc32 in _PAPER_KEYCAP_ATLAS:
        return _PAPER_KEYCAP_ATLAS[is_sc32]

    import json
    import numpy as np
    from scipy.ndimage import label, find_objects
    from PIL import ImageDraw

    model_slug = "sc32" if is_sc32 else "sc6"
    out_dir = _KEYCAP_CACHE_DIR / model_slug
    out_dir.mkdir(parents=True, exist_ok=True)

    img_name = "sc32_hero_stack.png" if is_sc32 else "sc6_hero_calculator.png"
    json_name = "layout_data.json" if is_sc32 else "layout_data_sc6.json"

    img_candidates = [
        MANUALS_ASSETS_DIR / "screenshots" / img_name,
        DOCS_DIR / "assets" / "manuals" / "screenshots" / img_name,
        REPO_ROOT / "Books" / "assets" / "manuals" / "screenshots" / img_name,
        REPO_ROOT.parent / "watch-calc-32" / "documentation" / "manuals" / "assets" / "screenshots" / img_name,
        REPO_ROOT.parent / "stackcalc" / "docs" / "assets" / "manuals" / "screenshots" / img_name,
    ]
    json_candidates = [
        MANUALS_ASSETS_DIR / json_name,
        DOCS_DIR / "assets" / "manuals" / json_name,
        REPO_ROOT / "Books" / "assets" / "manuals" / json_name,
        REPO_ROOT.parent / "watch-calc-32" / "documentation" / "manuals" / "assets" / json_name,
        REPO_ROOT.parent / "stackcalc" / "docs" / "assets" / "manuals" / json_name,
    ]
    img_p = next((p for p in img_candidates if p.exists()), None)
    json_p = next((p for p in json_candidates if p.exists()), None)

    atlas: Dict[Tuple[str, int, int], Tuple[Path, int, int]] = {}
    if not img_p or not json_p:
        _PAPER_KEYCAP_ATLAS[is_sc32] = atlas
        return atlas

    im_orig = PIL.Image.open(img_p).convert("RGBA")
    bg = PIL.Image.new("RGBA", im_orig.size, (255, 255, 255, 255))
    im_comp = PIL.Image.alpha_composite(bg, im_orig).convert("RGB")
    gray = np.array(im_comp.convert("L"))
    gray_crisp = np.where(gray < 215, np.minimum(gray, 35), 255).astype(np.uint8)
    im = PIL.Image.fromarray(gray_crisp).convert("RGB")
    dark = gray_crisp < 128

    labeled, _ = label(dark[850:2220, 40:1210])
    raw_boxes = []
    for sl in find_objects(labeled):
        y0, y1 = sl[0].start + 850, sl[0].stop + 850
        x0, x1 = sl[1].start + 40, sl[1].stop + 40
        w, h = x1 - x0, y1 - y0
        if 95 <= w <= 350 and 70 <= h <= 120:
            raw_boxes.append((y0, x0, y1, x1, w, h))
    boxes = [
        b for b in raw_boxes
        if not any(o != b and o[0] <= b[0] and o[1] <= b[1] and o[2] >= b[2] and o[3] >= b[3] for o in raw_boxes)
    ]
    rows: Dict[int, list] = {}
    for b in boxes:
        rows.setdefault(round(b[0] / 80.0), []).append(b)
    sorted_rows = [sorted(v, key=lambda x: x[1]) for _, v in sorted(rows.items())]

    data = json.loads(json_p.read_text(encoding="utf-8"))
    for r_idx, r_boxes in enumerate(sorted_rows):
        row_keys = sorted([k for k in data.get("keys", []) if k["row"] == r_idx], key=lambda k: k["col"])
        for c_idx, (b, kinfo) in enumerate(zip(r_boxes, row_keys)):
            y0, x0, y1, x1, w, h = b
            k_col = kinfo["col"]

            # 1. Primary physical button crop
            if w > 200:
                # Wide ENTER key: trim horizontal whitespace slightly inside button so aspect ratio is ~2.1:1
                inner = im.crop((x0 + 38, y0, x1 - 38, y1))
                dr = ImageDraw.Draw(inner)
                dr.rounded_rectangle([1, 1, inner.width - 2, inner.height - 2], radius=12, outline=(0, 0, 0), width=3)
                crop_p = inner
            else:
                crop_p = im.crop((x0 - 1, y0 - 1, x1 + 1, y1 + 1))
            p_path = out_dir / f"primary_r{r_idx}_c{k_col}.png"
            crop_p.save(p_path, format="PNG")
            atlas[("primary", r_idx, k_col)] = (p_path, crop_p.width, crop_p.height)

            yel_lbl = kinfo.get("yellowLabel", "").strip()
            blu_lbl = kinfo.get("blueLabel", "").strip()
            if not yel_lbl and not blu_lbl:
                continue

            y_top = max(822, y0 - 74)
            y_bot = y0 - 5
            sx0 = max(30, x0 - 18)
            sx1 = min(1220, x1 + 18)
            strip = dark[y_top:y_bot, sx0:sx1].copy()
            slabeled, snum = label(strip)
            sobjs = find_objects(slabeled) if snum > 0 else []

            if blu_lbl and sobjs:
                candidates = [
                    sl for sl in sobjs
                    if (sl[1].stop - sl[1].start) >= 24 and (sl[0].stop - sl[0].start) >= 28
                ]
                if candidates:
                    pill_sl = max(candidates, key=lambda s: s[1].stop)
                    by0, by1 = y_top + pill_sl[0].start, y_top + pill_sl[0].stop
                    bx0, bx1 = sx0 + pill_sl[1].start, sx0 + pill_sl[1].stop
                    bcrop = im.crop((bx0, by0, bx1, by1))
                    dr_b = ImageDraw.Draw(bcrop)
                    dr_b.rounded_rectangle([0, 0, bcrop.width - 1, bcrop.height - 1], radius=4, outline=(0, 0, 0), width=2)
                    b_path = out_dir / f"blue_r{r_idx}_c{k_col}.png"
                    bcrop.save(b_path, format="PNG")
                    atlas[("blue", r_idx, k_col)] = (b_path, bcrop.width, bcrop.height)
                    strip[:, max(0, pill_sl[1].start - 2):] = False

            if yel_lbl and strip.any():
                ys, xs = np.where(strip)
                cy0, cy1 = y_top + ys.min(), y_top + ys.max() + 1
                cx0, cx1 = sx0 + xs.min(), sx0 + xs.max() + 1
                ycrop = im.crop((cx0, cy0, cx1, cy1))
                pad_x, pad_y = 10, 7
                framed = PIL.Image.new("RGB", (ycrop.width + 2 * pad_x, ycrop.height + 2 * pad_y), (255, 255, 255))
                framed.paste(ycrop, (pad_x, pad_y))
                dr_y = ImageDraw.Draw(framed)
                dr_y.rounded_rectangle([1, 1, framed.width - 2, framed.height - 2], radius=5, outline=(0, 0, 0), width=2)
                y_path = out_dir / f"yellow_r{r_idx}_c{k_col}.png"
                framed.save(y_path, format="PNG")
                atlas[("yellow", r_idx, k_col)] = (y_path, framed.width, framed.height)

    _PAPER_KEYCAP_ATLAS[is_sc32] = atlas
    return atlas


def _get_fallback_paper_keycap(clean_label: str, is_sc32: bool) -> Tuple[Path, int, int]:
    """Renders a high-DPI Paper-theme softkey/button PNG for menu, alpha, or generic key tokens."""
    cache_key = (is_sc32, clean_label)
    if cache_key in _PAPER_FALLBACK_CACHE:
        return _PAPER_FALLBACK_CACHE[cache_key]

    from PIL import ImageDraw, ImageFont

    model_slug = "sc32" if is_sc32 else "sc6"
    out_dir = _KEYCAP_CACHE_DIR / model_slug
    out_dir.mkdir(parents=True, exist_ok=True)

    disp = clean_label.replace("⇄", "↔").replace("↰", "f").replace("↱", "g").replace("▸", "→")
    disp = disp.replace("🎲", "DICE").replace("🕒", "CLOCK").replace("▦", "FRAME")

    arial_bold = Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")
    font_path = str(arial_bold) if arial_bold.exists() else str(FONT_DIR / "SpaceMono-Bold.ttf")
    try:
        fnt = ImageFont.truetype(font_path, 34)
    except Exception:
        fnt = ImageFont.load_default()

    dummy = PIL.Image.new("RGB", (400, 100), (255, 255, 255))
    dr = ImageDraw.Draw(dummy)
    bbox = dr.textbbox((0, 0), disp, font=fnt)
    tw = max(24, bbox[2] - bbox[0])
    th = max(24, bbox[3] - bbox[1])

    pad_x = 18
    h = 68
    w = max(76, tw + 2 * pad_x)
    img = PIL.Image.new("RGB", (w, h), (255, 255, 255))
    dr = ImageDraw.Draw(img)
    dr.rounded_rectangle([1, 1, w - 2, h - 2], radius=10, fill=(255, 255, 255), outline=(0, 0, 0), width=3)
    tx = (w - tw) / 2.0 - bbox[0]
    ty = (h - th) / 2.0 - bbox[1]
    dr.text((tx, ty), disp, font=fnt, fill=(0, 0, 0))

    safe_name = re.sub(r'[^A-Za-z0-9_+-]', lambda m: f"u{ord(m.group(0)):04x}", clean_label)
    f_path = out_dir / f"soft_{safe_name}.png"
    img.save(f_path, format="PNG")
    res = (f_path, w, h)
    _PAPER_FALLBACK_CACHE[cache_key] = res
    return res


def format_hardware_keycap_cartouche(key_token: str, is_sc32: bool, target_h_pt: float = 9.0) -> str:
    """
    Renders an authentic, unbreakable inline Paper-theme button keycap image (`<img .../>`)
    sourced directly from our Paper-theme calculator artwork (`sc32_hero_stack.png` / `sc6_hero_calculator.png`).
    Because ReportLab treats inline `<img .../>` tags as atomic glyphs, keycaps NEVER break
    mid-word across table lines and NEVER suffer from missing font characters.
    """
    from book_engine import get_registry
    clean_k = key_token.strip()
    atlas = _ensure_paper_keycap_atlas(is_sc32)

    png_info: Optional[Tuple[Path, int, int]] = None
    layer_kind = "primary"
    for try_sc32 in (is_sc32, not is_sc32):
        reg = get_registry(try_sc32)
        try:
            entry = reg.resolve(clean_k)
            if entry.layer in ("yellow", "blue") and entry.canonical in {"x²", "ˣ√y", "x!", "1/x", "|x|"}:
                png_info = _get_fallback_paper_keycap(entry.canonical, try_sc32)
                layer_kind = entry.layer
                break
            try_atlas = _ensure_paper_keycap_atlas(try_sc32)
            lookup = (entry.layer, entry.row, entry.col)
            if lookup in try_atlas:
                png_info = try_atlas[lookup]
                layer_kind = entry.layer
                break
        except ValueError:
            continue

    if png_info is None:
        png_info = _get_fallback_paper_keycap(clean_k, is_sc32)
        layer_kind = "menu"

    p_path, px_w, px_h = png_info
    # Scale shifted pills slightly more compactly than primary physical buttons, matching faceplate proportions
    h_pt = target_h_pt * (0.88 if layer_kind in ("yellow", "blue") else 1.0)
    w_pt = h_pt * (px_w / float(max(1, px_h)))
    valign = -2.1 if h_pt >= 8.5 else -1.7
    return f"<img src='{p_path}' width='{w_pt:.2f}' height='{h_pt:.2f}' valign='{valign:.2f}'/>"


def sanitize_inline_markdown(text: str, is_sc32: bool, in_table: bool = False) -> str:
    """
    Sanitizes markdown inline syntax and escapes XML characters for ReportLab Paragraphs.
    Formats authentic Paper-theme button keycaps, math blocks, bold, italic, and links.
    """
    accent_hex = SC32_ACCENT if is_sc32 else SC6_ACCENT
    keycap_h = 8.4 if in_table else 9.2

    # 1. Unescape existing HTML entities (BookSans supports Polish Ł/ł natively!)
    text = html.unescape(text)
    if not BOOK_SANS_AVAILABLE:
        text = text.replace("Ł", "L").replace("ł", "l")

    # Convert inline HTML tags used inside markdown tables/lists to markdown equivalents first
    text = re.sub(r'<code>(.*?)</code>', r'`\1`', text)
    text = re.sub(r'<(?:strong|b)>(.*?)</(?:strong|b)>', r'**\1**', text)
    text = re.sub(r'<(?:em|i)>(.*?)</(?:em|i)>', r'*\1*', text)
    text = re.sub(r'<br\s*/?>', ' • ', text)

    # 2. Extract and protect escaped currency/percent symbols, code spans, math spans, and keycaps
    placeholders = {}
    p_idx = 0

    def save_placeholder(val: str) -> str:
        nonlocal p_idx
        key = f"QQPH{p_idx}QQ"
        placeholders[key] = val
        p_idx += 1
        return key

    # Protect escaped \$ and \% FIRST so \$100 never collides with $...$ math delimiters
    text = text.replace(r"\$", save_placeholder("$"))
    text = text.replace(r"\%", save_placeholder("%"))

    # Protect currency parentheticals like ($) or ($ per period) without matching ($f(x)$) math
    text = re.sub(r'\(\$(\s*|\s+per\b[^)\$]*|\s*/[a-zA-Z]+[^)\$]*)\)', lambda m: f"({save_placeholder('$')}{m.group(1)})", text)

    from book_engine import get_registry
    registry = get_registry(is_sc32)
    alt_registry = get_registry(not is_sc32)

    def _is_valid_keycap(token: str) -> bool:
        t_clean = token.strip()
        if not t_clean:
            return False
        for reg in (registry, alt_registry):
            try:
                reg.resolve(t_clean)
                return True
            except ValueError:
                pass
        return t_clean.upper() in {"ENTER", "ON", "C", "CLEAR", "AC", "<-", "BS", "DICE", "CLOCK", "FRAME"}

    # Handle single-keycap backtick `[KEY]` BEFORE math so `[$]` never collides with $...$
    def sub_backtick_keycap(m):
        k = m.group(1)
        return save_placeholder(format_hardware_keycap_cartouche(k, is_sc32, target_h_pt=keycap_h))
    text = re.sub(r'`\[([^`\]\n]+)\]`', sub_backtick_keycap, text)

    # Handle standard inline code `...` BEFORE math (converting any [KEY] inside backticks into Paper keycaps!)
    text = re.sub(r'\$\s*`([^`\n]+)`\s*\$', r'`\1`', text)
    def sub_code(m):
        raw = m.group(1)
        # Split on [KEY] tokens inside the code span so keystroke sequences render with real Paper keycaps
        parts = re.split(r'(\[[^\]\n]+\])', raw)
        rendered_parts = []
        for pt in parts:
            if not pt:
                continue
            if pt.startswith("[") and pt.endswith("]"):
                inner_k = pt[1:-1].strip()
                if _is_valid_keycap(inner_k):
                    rendered_parts.append(format_hardware_keycap_cartouche(inner_k, is_sc32, target_h_pt=keycap_h))
                    continue
            pt_esc = pt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            pt_esc = _protect_special_unicode_glyphs(pt_esc)
            rendered_parts.append(f"<font face='{FONT_MONO}' size='7.5' color='{accent_hex}'><b>{pt_esc}</b></font>")
        return save_placeholder("".join(rendered_parts))
    text = re.sub(r'`([^`\n]+)`', sub_code, text)

    # Handle display math $$...$$
    def sub_display_math(m):
        raw = m.group(1)
        cleaned = clean_latex_math(raw)
        return save_placeholder(f"<b><font color='{accent_hex}'>{cleaned}</font></b>")
    text = re.sub(r'\$\$([^\$]+)\$\$', sub_display_math, text)

    # Handle inline math $...$
    def sub_inline_math(m):
        raw = m.group(1)
        cleaned = clean_latex_math(raw)
        return save_placeholder(f"<font color='{accent_hex}'>{cleaned}</font>")
    text = re.sub(r'\$([^\$\n]+)\$', sub_inline_math, text)

    # Handle bare hardware keycaps [KEY] (only if recognized by KeyRegistry)
    def sub_bare_keycap(m):
        k = m.group(1)
        if _is_valid_keycap(k):
            return save_placeholder(format_hardware_keycap_cartouche(k, is_sc32, target_h_pt=keycap_h))
        return m.group(0)
    text = re.sub(r'(?<!\!)\[([^\]\n]{1,12})\](?!\()', sub_bare_keycap, text)

    # 3. Escape remaining XML characters in regular text and protect special Unicode glyphs
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = _protect_special_unicode_glyphs(text)

    # Handle markdown links [text](url) -> <b>text</b>
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'<b>\1</b>', text)

    # 4. Handle markdown bold and italic (guarded against word boundaries)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\w)__([^_]+)__(?!\w)', r'<b>\1</b>', text)
    text = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', text)
    text = re.sub(r'(?<!\w)_([^_]+)_(?!\w)', r'<i>\1</i>', text)

    # 5. Restore placeholders in reverse order so nested placeholders resolve cleanly
    for key, val in reversed(list(placeholders.items())):
        text = text.replace(key, val)

    # Keep scientific notation outside inline math (e.g., 6.6743 × 10⁻¹¹) on a single line
    text = re.sub(r'(\d)\s*([×·])\s*(10\b)', "\\1\u00a0\\2\u00a0\\3", text)
    return text.strip()


def format_heading_text(raw_title: str, is_sc32: bool = True) -> Tuple[str, str]:
    """
    Formats a markdown heading into (plain_toc_title, styled_paragraph_title),
    converting inline $...$ LaTeX math into clean Unicode typography and rendering
    [KEY] badges as Paper-theme keycaps in the heading while keeping clean text in the TOC.
    """
    t = html.unescape(raw_title.strip())
    if not BOOK_SANS_AVAILABLE:
        t = t.replace("Ł", "L").replace("ł", "l")
    t = t.replace(r"\$", "QQESCDOLLARQQ").replace(r"\%", "%")
    t = re.sub(r'`\[([^`]+)\]`', r'[\1]', t)
    math_ph = {}
    def _save_h_math(m):
        k = f"QQHM{len(math_ph)}QQ"
        math_content = m.group(1).replace("QQESCDOLLARQQ", "$")
        math_ph[k] = clean_latex_math(math_content)
        return k
    t = re.sub(r'\$([^\$\n]+)\$', _save_h_math, t)
    t = t.replace("QQESCDOLLARQQ", "$")
    t = re.sub(r'[*`]', '', t)

    # Plain version for TOC & PDF Bookmarks (convert special key symbols to clean readable ASCII/Unicode)
    t_plain = t.replace("↰", "f").replace("↱", "g").replace("⇄", "↔").replace("∥", "||").replace("▸", "→")
    t_plain = t_plain.replace("🎲", "DICE").replace("🕒", "CLOCK").replace("▦", "FRAME")
    t_plain = t_plain.replace("⌊", "floor(").replace("⌋", ")").replace("⌈", "ceil(").replace("⌉", ")")
    for k, v in math_ph.items():
        v_plain = re.sub(r'</?[a-zA-Z][^>]*>', '', v)
        v_plain = v_plain.replace("∥", "||").replace("⌊", "floor(").replace("⌋", ")")
        t_plain = t_plain.replace(k, v_plain)
    plain = html.unescape(re.sub(r'</?[a-zA-Z][^>]*>', '', t_plain)).strip()

    # Styled version for Heading on page (with Paper-theme keycaps and Terminus glyph protection)
    from book_engine import get_registry
    reg1 = get_registry(is_sc32)
    reg2 = get_registry(not is_sc32)
    key_ph = {}
    def _save_h_key(m):
        k_tok = m.group(1).strip()
        for r in (reg1, reg2):
            try:
                r.resolve(k_tok)
                ph_k = f"QQHK{len(key_ph)}QQ"
                key_ph[ph_k] = format_hardware_keycap_cartouche(k_tok, is_sc32, target_h_pt=10.0)
                return ph_k
            except ValueError:
                pass
        return m.group(0)
    t_styled = re.sub(r'\[([^\]\n]{1,12})\]', _save_h_key, t)
    t_styled = t_styled.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t_styled = _protect_special_unicode_glyphs(t_styled)
    for k, v in math_ph.items():
        t_styled = t_styled.replace(k, v)
    for k, v in key_ph.items():
        t_styled = t_styled.replace(k, v)
    styled = t_styled.strip()
    return plain, styled


def make_paragraph(text: str, style: ParagraphStyle) -> Paragraph:
    """Safely creates a Paragraph, falling back to escaped plain text if XML parsing fails."""
    try:
        return Paragraph(text, style)
    except Exception:
        plain_text = re.sub(r'</?[a-zA-Z][^>]*>', '', text)
        safe_text = plain_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return Paragraph(safe_text, style)


# ---------------------------------------------------------------------------
# Subject Index Catalogs & Term Extraction
# ---------------------------------------------------------------------------
INDEX_CATALOG_SC32 = [
    ("Hardware Architecture & Dovetail Chassis", [re.compile(r'\b(hardware architecture|craftsmanship|dovetail|snap-dome)\b', re.IGNORECASE)]),
    ("43-Key Matrix Keypad", [re.compile(r'\b(keypad matrix|43-key|snap-dome keypad)\b', re.IGNORECASE)]),
    ("Transflective Monochrome LCD", [re.compile(r'\b(transflective lcd|monochrome lcd|132\s*[x×]\s*65)\b', re.IGNORECASE)]),
    ("RPN (Reverse Polish Notation)", [re.compile(r'\b(reverse polish notation|postfix notation)\b', re.IGNORECASE), re.compile(r'\bRPN\b')]),
    ("4-Level XYZT Operational Stack", [re.compile(r'\b(xyzt stack|4-stack|register [xyzt])\b', re.IGNORECASE)]),
    ("Stack Lift State Machine", [re.compile(r'\b(stack lift|lift enabled|lift disabled)\b', re.IGNORECASE)]),
    ("Roll Down (R↓) & Stack Cycling", [re.compile(r'\b(stack drop|roll down|stack cycl)\b', re.IGNORECASE), re.compile(r'\[R[↓\\]+\]')]),
    ("LASTX Preservation & Recovery", [re.compile(r'\b(lastx|last x)\b', re.IGNORECASE)]),
    ("Register Swap (x⇄y)", [re.compile(r'\b(swap x and y|x-y swap)\b', re.IGNORECASE), re.compile(r'\[x[⇄↔<->]+y\]')]),
    ("Deep Stack Architecture", [re.compile(r'\b(deep stack|arbitrary depth stack)\b', re.IGNORECASE)]),
    ("Algebraic Functions & Powers", [re.compile(r'\b(transcendentals|powers and roots|algebraic evaluation)\b', re.IGNORECASE)]),
    ("Trigonometry & Polar Coordinates", [re.compile(r'\b(polar coordinates|rectangular coordinates|geodetic traverse)\b', re.IGNORECASE)]),
    ("2D Vector Operations", [re.compile(r'\b(2d vectors?|vector addition|vector magnitude)\b', re.IGNORECASE)]),
    ("Complex Numbers & AC Phasors", [re.compile(r'\b(complex numbers?|phasor analysis|euler\'s identity|complex impedance)\b', re.IGNORECASE)]),
    ("Geometry & Surface Area via [Σ+]", [re.compile(r'\b(surface area via|mensuration|prism volume)\b', re.IGNORECASE), re.compile(r'\[[Σ∑]\+\]')]),
    ("Brent's Root Finding Algorithm ([SOLVE])", [re.compile(r'\b(brent\'s solver|brent solver|numerical root|colebrook)\b', re.IGNORECASE)]),
    ("Adaptive Romberg Quadrature ([∫])", [re.compile(r'\b(romberg quadrature|adaptive quadrature|numerical integration)\b', re.IGNORECASE)]),
    ("Polynomial Root Extraction ([POLY])", [re.compile(r'\b(polynomial solver|polynomial roots|companion matrix|cardano)\b', re.IGNORECASE)]),
    ("Bivariate Statistics & Curve Fitting ([L.R.])", [re.compile(r'\b(bivariate statistics|linear regression|curve fitting|correlation coefficient)\b', re.IGNORECASE)]),
    ("Computer Science & 36-Bit Integers", [re.compile(r'\b(36-bit|two\'s complement|subnet masking|bitwise|amdahl)\b', re.IGNORECASE)]),
    ("Financial TVM Solver & Amortization", [re.compile(r'\b(tvm solver|financial mathematics|amortization schedule|perpetuit|npv|irr)\b', re.IGNORECASE)]),
    ("Function & Scatter Plotting Engine ([PLOT])", [re.compile(r'\b(scatter plotting|function plotting|pixel grid)\b', re.IGNORECASE)]),
    ("3D Printing Extrusion Fluid Dynamics", [re.compile(r'\b(extrusion fluid dynamics|volumetric flow|filament density)\b', re.IGNORECASE)]),
    ("Audio Engineering Crossover Filters", [re.compile(r'\b(crossover filter|butterworth|linkwitz-riley)\b', re.IGNORECASE)]),
    ("Civil Surveying & Closed Traverses", [re.compile(r'\b(closed-loop traverse|traverse misclosure|geodetic azimuth|haversine)\b', re.IGNORECASE)]),
    ("High-Speed Equation Entry & Inside-Out Mastery", [re.compile(r'\b(inside-out|radical pyramid|nested fraction|high-speed equation)\b', re.IGNORECASE)]),
    ("Classical Mechanics, Kinematics & Projectiles", [re.compile(r'\b(projectile|centripetal|kinematic|moment of inertia|pendulum)\b', re.IGNORECASE)]),
    ("Orbital Mechanics, Escape Velocity & Tsiolkovsky Rocket Equation", [re.compile(r'\b(tsiolkovsky|hohmann|vis-viva|kepler|escape velocity|orbital)\b', re.IGNORECASE)]),
    ("Fluid Mechanics, Reynolds Number & Bernoulli Equation", [re.compile(r'\b(reynolds|bernoulli|poiseuille|darcy-weisbach|torricelli|mach number)\b', re.IGNORECASE)]),
    ("Thermodynamics, Ideal Gas Law & Carnot Efficiency", [re.compile(r'\b(carnot|ideal gas|stefan-boltzmann|adiabatic|rankine|brayton|fourier)\b', re.IGNORECASE)]),
    ("Electricity, RLC Resonance & Parallel Impedance ([∥])", [re.compile(r'\b(rlc|reactance|inductance|capacitance|coulomb|poynting|parallel resistor)\b', re.IGNORECASE)]),
    ("Optics, Thin-Lens Equation & Snell's Refraction", [re.compile(r'\b(snell|thin lens|doppler|brewster|rayleigh|diffraction)\b', re.IGNORECASE)]),
    ("Relativity, Quantum Mechanics & Radioactive Decay", [re.compile(r'\b(lorentz|de broglie|planck|half-life|carbon-14|rydberg|photoelectric)\b', re.IGNORECASE)]),
    ("Chemistry, pH Buffers, Nernst & Arrhenius Kinetics", [re.compile(r'\b(henderson-hasselbalch|nernst|arrhenius|beer-lambert|clausius-clapeyron|michaelis-menten|ionic strength)\b', re.IGNORECASE)]),
    ("Probability Distributions (Binomial, Poisson, Bayes & Normal)", [re.compile(r'\b(binomial|poisson|bayes|gaussian|confidence interval|process capability)\b', re.IGNORECASE)]),
    ("Information Theory, Shannon Entropy & Channel Capacity", [re.compile(r'\b(shannon|channel capacity|queueing|entropy)\b', re.IGNORECASE)]),
    ("Structural Mechanics, Euler Buckling & Beam Deflection", [re.compile(r'\b(euler column|buckling|beam deflection|hooke|young\'s modulus)\b', re.IGNORECASE)]),
    ("Semiconductors, Shockley Diode, Op-Amps & Friis RF Link", [re.compile(r'\b(shockley|operational amplifier|op-amp|friis|path loss)\b', re.IGNORECASE)]),
    ("Keycap [ENTER]", [re.compile(r'\[ENTER\]', re.IGNORECASE)]),
    ("Keycap [LASTX]", [re.compile(r'\[LASTX\]', re.IGNORECASE)]),
    ("Keycap [x⇄y]", [re.compile(r'\[x[⇄↔<->]+y\]', re.IGNORECASE)]),
    ("Keycap [R↓]", [re.compile(r'\[R[↓\\]+\]')]),
    ("Keycap [Σ+]", [re.compile(r'\[[Σ∑]\+\]')]),
    ("Keycap [STO]", [re.compile(r'\[STO\]', re.IGNORECASE)]),
    ("Keycap [RCL]", [re.compile(r'\[RCL\]', re.IGNORECASE)]),
    ("Keycap [SIN] / [COS] / [TAN]", [re.compile(r'\[(SIN|COS|TAN)\]', re.IGNORECASE)]),
    ("Keycap [√x]", [re.compile(r'\[[√\\]+x\]')]),
    ("Keycap [eˣ]", [re.compile(r'\[e[\^ˣx]+\]')]),
    ("Keycap [LN]", [re.compile(r'\[LN\]')]),
    ("Keycap [yˣ]", [re.compile(r'\[y[\^ˣx]+\]')]),
    ("Keycap [1/x]", [re.compile(r'\[1\/x\]')]),
    ("Keycap [+/-]", [re.compile(r'\[\+\/\-\]')]),
    ("Keycap [E] (Scientific E)", [re.compile(r'\[E\]')]),
    ("Keycap [∥] (Parallel)", [re.compile(r'\[[∥\|]{2}\]')]),
]

INDEX_CATALOG_SC6 = [
    ("Hardware Architecture & Classroom Durability", [re.compile(r'\b(hardware architecture|classroom durability|sliding desk-stand|protective cowl)\b', re.IGNORECASE)]),
    ("Snap-Dome 400g Keypad", [re.compile(r'\b(snap-dome|tactile feedback|400g actuation)\b', re.IGNORECASE)]),
    ("Transflective Ambient Display", [re.compile(r'\b(transflective|ambient-light|high-contrast display)\b', re.IGNORECASE)]),
    ("Fraction Studio 84mm Towers", [re.compile(r'\b(fraction studio|proportional towers|84\s*mm)\b', re.IGNORECASE)]),
    ("Ten-Frames & Desk Counters", [re.compile(r'\b(ten-frames?|desk counters?|counting grid|make-ten)\b', re.IGNORECASE)]),
    ("Classroom Planetary Clock", [re.compile(r'\b(planetary clock|geared clock|modulo 60|elapsed time)\b', re.IGNORECASE)]),
    ("Math Domino Studio", [re.compile(r'\b(math dominoes?|domino studio|dot arrays?)\b', re.IGNORECASE)]),
    ("Algebra Boxes & Tiles", [re.compile(r'\b(algebra boxes|algebra tiles|area models?)\b', re.IGNORECASE)]),
    ("Probability Dice & Spinners", [re.compile(r'\b(probability dice|dice and spinner|random generator)\b', re.IGNORECASE)]),
    ("RPN 4-Story Glass Elevator Metaphor", [re.compile(r'\b(elevator metaphor|elevator model|ground floor|glass elevator)\b', re.IGNORECASE)]),
    ("2-Stack Operational Display", [re.compile(r'\b(2-stack|two-stack|upper stack|lower stack)\b', re.IGNORECASE)]),
    ("Counting, Place Value & Base-10 Regrouping", [re.compile(r'\b(place value|base-10|units and tens|hundreds board|regrouping)\b', re.IGNORECASE)]),
    ("Number Lines & Skip-Counting", [re.compile(r'\b(number lines?|skip-counting|skip counting)\b', re.IGNORECASE)]),
    ("Superpower [REP] (Repeat Ladder)", [re.compile(r'\[REP\]'), re.compile(r'\bskip-counting ladder\b', re.IGNORECASE)]),
    ("Superpower [÷R] (Quotient & Remainder)", [re.compile(r'\[(DivR|÷R)\]', re.IGNORECASE), re.compile(r'\bquotient and remainder\b', re.IGNORECASE)]),
    ("Superpower [SIMP] (Factor Reduction)", [re.compile(r'\[SIMP\]', re.IGNORECASE), re.compile(r'\bfactor reduction\b', re.IGNORECASE)]),
    ("Superpower [LASTX] (Undo & Inverse)", [re.compile(r'\[LASTX\]', re.IGNORECASE), re.compile(r'\bundoing operations\b', re.IGNORECASE)]),
    ("Two-Dot Fraction Entry Syntax", [re.compile(r'\btwo-dot|fraction entry|mixed fractions?\b', re.IGNORECASE)]),
    ("Ratio Mode, Unit Rates & Percentages", [re.compile(r'\bratio mode|proportional reasoning|unit rate|sales tax|discount\b', re.IGNORECASE)]),
    ("Geometry, Perimeter, Area & Surface Area via [Σ+]", [re.compile(r'\bsurface area via|rectangular prism|cylinder volume|pythagorean|triangle area\b', re.IGNORECASE), re.compile(r'\[[Σ∑]\+\]')]),
    ("Discrete Probability, Prime Numbers & Factor Trees", [re.compile(r'\bdiscrete probability|prime factorization|sieve of eratosthenes|twin prime|goldbach|lcm\b', re.IGNORECASE)]),
    ("Negative Numbers, Zero Pairs & Absolute Value", [re.compile(r'\bzero pairs?|negative integer|submarine depth|temperature swing|absolute value\b', re.IGNORECASE)]),
    ("Gamified Math Quiz Engine ([?])", [re.compile(r'\bmath quiz engine|gamified quiz|flashcard mode\b', re.IGNORECASE)]),
    ("Applied Elementary STEM Labs", [re.compile(r'\bapplied stem|paper circuits?|batch cubes?|maker labs?\b', re.IGNORECASE)]),
    ("Curriculum Standards (CCSS-M, Singapore, Bridges, Big Ideas)", [re.compile(r'\bbridges in math|ccss alignment|curriculum matrix|singapore dimensions\b', re.IGNORECASE)]),
    ("Teacher Lesson Plans (25 Turnkey 45-Minute Stations)", [re.compile(r'\blesson plan|station guide|teacher script\b', re.IGNORECASE)]),
    ("Keycap [ENTER]", [re.compile(r'\[ENTER\]', re.IGNORECASE)]),
    ("Keycap [C] / [CLEAR]", [re.compile(r'\[(C|CLEAR)\]', re.IGNORECASE)]),
    ("Keycap [LASTX]", [re.compile(r'\[LASTX\]', re.IGNORECASE)]),
    ("Keycap [x⇄y]", [re.compile(r'\[x[⇄↔<->]+y\]', re.IGNORECASE)]),
    ("Keycap [REP]", [re.compile(r'\[REP\]', re.IGNORECASE)]),
    ("Keycap [÷R]", [re.compile(r'\[(DivR|÷R)\]', re.IGNORECASE)]),
    ("Keycap [SIMP]", [re.compile(r'\[SIMP\]', re.IGNORECASE)]),
    ("Keycap [Σ+]", [re.compile(r'\[[Σ∑]\+\]')]),
    ("Keycap [COUNT] (Number Rack)", [re.compile(r'\[COUNT\]', re.IGNORECASE)]),
    ("Keycap [CLOCK]", [re.compile(r'\[CLOCK\]', re.IGNORECASE)]),
    ("Keycap [.] (Fraction Two-Dot)", [re.compile(r'\[\.\]')]),
]

def extract_index_terms(text: str, is_sc32: bool, term_counts: Optional[Dict[str, int]] = None, max_per_term: int = 8) -> List[str]:
    """
    Identifies relevant subject index terms from paragraph or heading text.
    Limits each term to at most `max_per_term` distinct references across the manual.
    """
    if term_counts is None:
        return []
    catalog = INDEX_CATALOG_SC32 if is_sc32 else INDEX_CATALOG_SC6
    matched = []
    for canonical_name, patterns in catalog:
        if term_counts.get(canonical_name, 0) >= max_per_term:
            continue
        for pat in patterns:
            if pat.search(text):
                term_counts[canonical_name] = term_counts.get(canonical_name, 0) + 1
                matched.append(canonical_name)
                break
    return matched


# ---------------------------------------------------------------------------
# Direct-Canvas NYT Bestseller & KDP Print Cover Engine (Zero Tables!)
# ---------------------------------------------------------------------------
_COVER_IMAGE_CACHE: Dict[Tuple[str, int, int, str], Any] = {}

def draw_cropped_image_on_canvas(
    c: canvas.Canvas,
    img_path: Path,
    x: float,
    y: float,
    w: float,
    h: float,
    focus: str = "center",
    zoom: float = 1.0
) -> None:
    """
    Center-crops (with optional zoom) a high-resolution studio render to the exact
    aspect ratio of `(w, h)` and draws it onto the ReportLab canvas with cached speed.
    """
    if not img_path.exists():
        return
    from reportlab.lib.utils import ImageReader
    cache_key = (str(img_path), int(round(w * 2)), int(round(h * 2)), f"{focus}_{zoom:.2f}")
    if cache_key not in _COVER_IMAGE_CACHE:
        with PIL.Image.open(img_path) as im:
            im = im.convert("RGB")
            iw, ih = im.size
            target_ratio = w / float(h)
            src_ratio = iw / float(ih)
            if src_ratio > target_ratio:
                crop_h = ih / zoom
                crop_w = crop_h * target_ratio
            else:
                crop_w = iw / zoom
                crop_h = crop_w / target_ratio
            cx = iw * 0.5
            cy = ih * (0.46 if focus == "upper" else 0.5)
            left = max(0, int(round(cx - crop_w / 2.0)))
            top = max(0, int(round(cy - crop_h / 2.0)))
            right = min(iw, int(round(left + crop_w)))
            bottom = min(ih, int(round(top + crop_h)))
            cropped = im.crop((left, top, right, bottom))
            target_px_w = max(300, int(round(w * 3.0)))
            target_px_h = max(300, int(round(h * 3.0)))
            cropped = cropped.resize((target_px_w, target_px_h), PIL.Image.Resampling.LANCZOS)
            _COVER_IMAGE_CACHE[cache_key] = ImageReader(cropped)
    c.drawImage(_COVER_IMAGE_CACHE[cache_key], x, y, width=w, height=h, preserveAspectRatio=False, mask='auto')


def draw_vector_isbn_barcode(
    c: canvas.Canvas,
    x: float,
    y: float,
    w: float,
    h: float,
    isbn_formatted: str,
    isbn_digits: str,
    price_label: str
) -> None:
    """
    Draws an official KDP-compliant 2.00 in x 1.20 in (144 pt x 86.4 pt) white barcode zone
    with true vector EAN-13 + 5-digit price add-on bars (zero ASCII pipe characters).
    """
    c.saveState()
    # Crisp white KDP barcode box
    c.setFillColor(to_color("#FFFFFF"))
    c.setStrokeColor(to_color("#CBD5E1"))
    c.setLineWidth(0.75)
    c.roundRect(x, y, w, h, 3.0, fill=1, stroke=1)

    # Top ISBN-13 human-readable header
    c.setFillColor(to_color("#0F172A"))
    c.setFont(FONT_MONO_BOLD, 7.2)
    c.drawCentredString(x + w * 0.5, y + h - 12.0, f"ISBN {isbn_formatted}")

    # Deterministic EAN-13 + EAN-5 bar pattern encoded as high-precision vector rectangles
    L_CODES = [
        "0001101", "0011001", "0010011", "0111101", "0100011",
        "0110001", "0101111", "0111011", "0110111", "0001011",
    ]
    R_CODES = [
        "1110010", "1100110", "1101100", "1000010", "1011100",
        "1001110", "1010000", "1000100", "1001000", "1110100",
    ]
    digits = [int(ch) for ch in re.sub(r"\D", "", isbn_digits)[:13]]
    while len(digits) < 13:
        digits.append(0)

    bits = "101"  # Left guard
    for d in digits[1:7]:
        bits += L_CODES[d]
    bits += "01010"  # Center guard
    for d in digits[7:13]:
        bits += R_CODES[d]
    bits += "101"  # Right guard

    # 5-digit price add-on ("51900" = $19.00 US)
    addon_bits = "1011"
    for idx_a, d in enumerate([5, 1, 9, 0, 0]):
        addon_bits += L_CODES[d]
        if idx_a < 4:
            addon_bits += "01"

    bar_x0 = x + 13.0
    module_w = 0.88
    bar_bottom = y + 22.0
    bar_top = y + h - 17.0
    bar_h = bar_top - bar_bottom

    c.setFillColor(to_color("#000000"))
    for idx_b, bit in enumerate(bits):
        if bit == "1":
            is_guard = (idx_b < 3) or (45 <= idx_b < 50) or (idx_b >= 92)
            by = bar_bottom - (4.0 if is_guard else 0.0)
            bh = bar_h + (4.0 if is_guard else 0.0)
            c.rect(bar_x0 + idx_b * module_w, by, module_w * 0.96, bh, fill=1, stroke=0)

    # Draw 5-digit price add-on bars to the right
    addon_x0 = bar_x0 + len(bits) * module_w + 6.0
    addon_h = bar_h - 6.0
    c.setFont(FONT_MONO_BOLD, 6.2)
    c.drawCentredString(addon_x0 + (len(addon_bits) * module_w) * 0.5, bar_top - 4.5, "51900 >")
    for idx_b, bit in enumerate(addon_bits):
        if bit == "1":
            c.rect(addon_x0 + idx_b * module_w, bar_bottom, module_w * 0.96, addon_h, fill=1, stroke=0)

    # Bottom human-readable digits & retail price
    c.setFont(FONT_MONO_BOLD, 6.8)
    raw_d = "".join(str(d) for d in digits)
    c.drawString(bar_x0 - 6.0, y + 12.5, f"{raw_d[0]}  {raw_d[1:7]}  {raw_d[7:13]}")
    c.setFont(FONT_BODY_BOLD, 6.5)
    c.setFillColor(to_color("#334155"))
    c.drawCentredString(x + w * 0.5, y + 4.0, price_label)
    c.restoreState()


def draw_bestseller_front_cover(
    c: canvas.Canvas,
    ox: float,
    oy: float,
    w: float,
    h: float,
    is_sc32: bool,
    bleed_l: float = 0.0,
    bleed_r: float = 0.0,
    bleed_t: float = 0.0,
    bleed_b: float = 0.0
) -> None:
    """
    Renders a true minimalist NYT Bestseller 6x9 trade Front Cover ("very simple visuals with few words"):
    - Continuous Warm Archival Paper (#F7F4EB) across the entire cover with >65% open whitespace.
    - Only 11-12 words on the entire front cover:
      1. Monumental Title: "THINKING IN THE STACK" / "FROM BLOCKS TO THE STACK"
      2. Concise 6-word Subtitle: "The Art of Calculating Without Parentheses" / "How Hands-On Blocks Make Numbers Click"
      3. One simple, clever, unboxed minimalist vector illustration floating in the center.
      4. Single-word imprint at the foot: "StackCalc"
    All live elements sit well inside KDP's cover safe zone (>= 0.50 in / 36 pt inside trim).
    """
    c.saveState()

    paper_cream = "#F7F4EB"
    ink_obsidian = "#0F172A"
    ink_slate = "#475569"
    accent = "#FF4F00" if is_sc32 else "#059669"

    # 1. Single Continuous Warm Archival Paper Background (#F7F4EB)
    c.setFillColor(to_color(paper_cream))
    c.rect(
        ox - bleed_l,
        oy - bleed_b,
        w + bleed_l + bleed_r,
        h + bleed_t + bleed_b,
        fill=1,
        stroke=0
    )

    cx = ox + (w * 0.5)

    # 2. Monumental Centered Bestseller Title (Upper Third)
    c.setFillColor(to_color(ink_obsidian))
    if is_sc32:
        c.setFont(FONT_BODY_BOLD, 42.0)
        c.drawCentredString(cx, oy + h - 118.0, "THINKING IN")
        c.drawCentredString(cx, oy + h - 166.0, "THE STACK")
        subtitle_str = "The Art of Calculating Without Parentheses"
    else:
        c.setFont(FONT_BODY_BOLD, 39.0)
        c.drawCentredString(cx, oy + h - 118.0, "FROM BLOCKS")
        c.drawCentredString(cx, oy + h - 166.0, "TO THE STACK")
        subtitle_str = "How Hands-On Blocks Make Numbers Click"

    # 3. Short 6-Word Subtitle
    c.setFont(FONT_BODY_ITALIC, 13.0)
    c.setFillColor(to_color(ink_slate))
    c.drawCentredString(cx, oy + h - 198.0, subtitle_str)

    # 4. Single Minimalist Iconic Visual Floating in Generous Whitespace (Center of Cover)
    if is_sc32:
        # Part A: The Parenthesis Trap — lightly struck through with a single bold orange slash
        expr_y = oy + 372.0
        c.setFont(FONT_MONO, 17.0)
        c.setFillColor(to_color("#64748B"))
        c.drawCentredString(cx, expr_y, "( 3 + 4 ) × ( 5 + 6 )")

        # Crisp International Orange diagonal strike-through
        c.setStrokeColor(to_color(accent))
        c.setLineWidth(2.6)
        c.setLineCap(1)
        c.line(cx - 102.0, expr_y - 4.0, cx + 102.0, expr_y + 16.0)

        # Part B: Four Minimalist Floating Stack Bars (T, Z, Y, X) — authentic RPN state after 3 ENTER 4 + 5 ENTER 6
        bar_w = 188.0
        bar_h = 24.0
        bar_gap = 10.0
        bar_x = cx - (bar_w * 0.5)
        top_bar_y = oy + 306.0

        stack_bars = [
            ("T", "0.0000", "#E6E1D3", "#64748B", "#64748B"),
            ("Z", "7.0000", "#DCD6C6", "#475569", "#334155"),
            ("Y", "5.0000", "#1E293B", "#94A3B8", "#FFFFFF"),
            ("X", "6.0000", "#FF4F00", "#FFE4D6", "#FFFFFF"),
        ]
        for idx_b, (lbl, val, fill_hex, lbl_hex, val_hex) in enumerate(stack_bars):
            by = top_bar_y - idx_b * (bar_h + bar_gap)
            c.setFillColor(to_color(fill_hex))
            c.roundRect(bar_x, by, bar_w, bar_h, 4.0, fill=1, stroke=0)
            c.setFont(FONT_MONO_BOLD, 9.5)
            c.setFillColor(to_color(lbl_hex))
            c.drawString(bar_x + 10.0, by + 8.0, lbl)
            if val:
                c.setFont(FONT_MONO_BOLD, 11.0)
                c.setFillColor(to_color(val_hex))
                c.drawRightString(bar_x + bar_w - 12.0, by + 7.5, val)
    else:
        # Minimalist Gauss 1-2-3-4 Tactile Block Staircase (Ten-Frame blocks stepping into the 4-level stack)
        block_sz = 34.0
        block_gap = 6.0
        total_stair_w = 4 * block_sz + 3 * block_gap
        start_x = cx - (total_stair_w * 0.5)
        base_stair_y = oy + 206.0

        # 4 rows (Bottom to Top = X, Y, Z, T): 4 blocks, 3 blocks, 2 blocks, 1 block (= 10)
        rows_spec = [
            (0, 4, "#059669"),  # Bottom row (4 Emerald blocks)
            (1, 3, "#0284C7"),  # Second row (3 Sky blocks)
            (2, 2, "#F59E0B"),  # Third row (2 Amber blocks)
            (3, 1, "#E11D48"),  # Top row (1 Coral block)
        ]
        for r_idx, count, col_hex in rows_spec:
            ry = base_stair_y + r_idx * (block_sz + block_gap)
            # Offset horizontally so the staircase rises left-to-right toward the stack
            row_start_x = start_x + (4 - count) * (block_sz + block_gap)
            for c_idx in range(count):
                bx = row_start_x + c_idx * (block_sz + block_gap)
                # Subtle tactile shadow
                c.setFillColor(to_color("#E2DDD0"))
                c.roundRect(bx + 2.0, ry - 2.0, block_sz, block_sz, 5.0, fill=1, stroke=0)
                # Crisp geometric block
                c.setFillColor(to_color(col_hex))
                c.roundRect(bx, ry, block_sz, block_sz, 5.0, fill=1, stroke=0)
                # Subtle inner highlight stud (tactile block feel)
                c.setStrokeColor(to_color("#FFFFFF"))
                c.setLineWidth(0.75)
                c.circle(bx + block_sz * 0.5, ry + block_sz * 0.5, 6.5, fill=0, stroke=1)

    # 5. Minimalist Single-Word Imprint at the Foot
    c.setFillColor(to_color(accent))
    c.rect(cx - 14.0, oy + 78.0, 28.0, 2.5, fill=1, stroke=0)

    c.setFillColor(to_color(ink_obsidian))
    c.setFont(FONT_BODY_BOLD, 14.0)
    c.drawCentredString(cx, oy + 54.0, "StackCalc")

    c.restoreState()


def draw_bestseller_back_cover(
    c: canvas.Canvas,
    ox: float,
    oy: float,
    w: float,
    h: float,
    is_sc32: bool,
    total_pages: int = 468,
    bleed_l: float = 0.0,
    bleed_r: float = 0.0,
    bleed_t: float = 0.0,
    bleed_b: float = 0.0
) -> None:
    """
    Renders a minimalist 6x9 NYT Bestseller trade Back Cover on continuous Warm Archival Paper (#F7F4EB):
    - Generous open margins, one bold armchair-reader hook question, two short narrative paragraphs,
      a quiet 2-line note on the companion problems/equations inside, the StackCalc imprint, and
      KDP's mandatory 2.00 x 1.20 in white ISBN-13 barcode box.
    """
    c.saveState()

    paper_cream = "#F7F4EB"
    ink_obsidian = "#0F172A"
    ink_slate = "#334155"
    ink_muted = "#64748B"
    accent = "#FF4F00" if is_sc32 else "#059669"

    # 1. Continuous Warm Archival Paper Background (#F7F4EB)
    c.setFillColor(to_color(paper_cream))
    c.rect(
        ox - bleed_l,
        oy - bleed_b,
        w + bleed_l + bleed_r,
        h + bleed_t + bleed_b,
        fill=1,
        stroke=0
    )

    safe_x = ox + 42.0
    safe_w = w - 84.0  # 348.0 pt on 6x9 trim

    # 2. Quiet Category Line at Top Left
    c.setFont(FONT_MONO_BOLD, 7.5)
    c.setFillColor(to_color(ink_muted))
    c.drawString(
        safe_x,
        oy + h - 52.0,
        "MATHEMATICS  /  POPULAR SCIENCE" if is_sc32 else "MATHEMATICS  /  EDUCATION"
    )

    # 3. Bold Armchair-Reader Hook Question
    c.setFillColor(to_color(ink_obsidian))
    c.setFont(FONT_BODY_BOLD, 17.5)
    if is_sc32:
        c.drawString(safe_x, oy + h - 92.0, "Why do we write equations one way,")
        c.drawString(safe_x, oy + h - 114.0, "yet solve them in our heads another?")
        p1_html = (
            "In 1924, the Polish logician Jan Łukasiewicz realized that parentheses are not a law of "
            "nature—they are merely a patch for writing algebra on flat paper. When you build a calculation "
            "from the inside out on a four-level stack, parentheses vanish, hidden memory traps disappear, "
            "and complex ideas unfold one transparent step at a time."
        )
        p2_html = (
            "Written for both the armchair reader on a plane and the practicing engineer or student at a desk, "
            "<b>Thinking in the Stack</b> pairs the historical stories behind great mathematical breakthroughs "
            "with a complete hands-on reference for the <b>StackCalc SC-32</b>."
        )
        ref_note_html = (
            "<b>Inside the Desk Reference:</b> 14 narrative chapters  •  100 essential STEM equations  •  "
            "698+ engine-verified problems across physics, electronics, calculus, statistics, and finance."
        )
    else:
        c.drawString(safe_x, oy + h - 92.0, "What happens when you can hold")
        c.drawString(safe_x, oy + h - 114.0, "a number in your hands?")
        p1_html = (
            "Children rarely struggle with math because numbers are too hard. They struggle when flat worksheets "
            "and black-box calculators sever symbols from physical reality. When a learner snaps physical tiles "
            "into a frame and watches those exact numbers ride a four-story elevator stack, arithmetic stops "
            "being a rule to memorize and becomes something they can see."
        )
        p2_html = (
            "Written for curious readers, parents, and educators alike, <b>From Blocks to the Stack</b> connects "
            "hands-on 3D blocks with parenthesis-free thinking—serving as both an engaging guide to visual number "
            "sense and the complete companion to the <b>StackCalc SC-6</b>."
        )
        ref_note_html = (
            "<b>Inside the Companion Guide:</b> 9 story-driven chapters (Grades K–6)  •  552+ realistic math quests  •  "
            "7 open-source 3D-printable manipulative kits  •  25 turnkey 45-minute lesson plans."
        )

    # Short accent bar under hook question
    c.setFillColor(to_color(accent))
    c.rect(safe_x, oy + h - 128.0, 44.0, 2.5, fill=1, stroke=0)

    body_style = ParagraphStyle(
        "BackCoverMinimalBody",
        fontName=FONT_BODY,
        fontSize=10.2,
        leading=15.4,
        textColor=to_color(ink_slate),
    )
    p1 = Paragraph(p1_html, body_style)
    _, h1 = p1.wrap(safe_w, 160.0)
    y_cursor = oy + h - 146.0 - h1
    p1.drawOn(c, safe_x, y_cursor)

    p2 = Paragraph(p2_html, body_style)
    _, h2 = p2.wrap(safe_w, 160.0)
    y_cursor = y_cursor - 14.0 - h2
    p2.drawOn(c, safe_x, y_cursor)

    # 4. Minimalist Desk-Reference Note (Separated by subtle hairline rules)
    rule_y1 = y_cursor - 20.0
    c.setStrokeColor(to_color("#D6D1C2"))
    c.setLineWidth(0.75)
    c.line(safe_x, rule_y1, safe_x + safe_w, rule_y1)

    note_style = ParagraphStyle(
        "BackCoverMinimalNote",
        fontName=FONT_BODY,
        fontSize=8.8,
        leading=13.0,
        textColor=to_color(ink_obsidian),
    )
    p_note = Paragraph(ref_note_html, note_style)
    _, hn = p_note.wrap(safe_w, 80.0)
    note_y = rule_y1 - 10.0 - hn
    p_note.drawOn(c, safe_x, note_y)

    rule_y2 = note_y - 10.0
    c.line(safe_x, rule_y2, safe_x + safe_w, rule_y2)

    # 5. Bottom Left Imprint & Bottom Right KDP 2.00 x 1.20 in White ISBN Barcode Box
    c.setFillColor(to_color(ink_obsidian))
    c.setFont(FONT_BODY_BOLD, 14.0)
    c.drawString(safe_x, oy + 88.0, "StackCalc")

    c.setFillColor(to_color(ink_muted))
    c.setFont(FONT_BODY, 8.5)
    c.drawString(safe_x, oy + 72.0, "Instruments, Software & Open-Source Models")
    c.setFont(FONT_MONO_BOLD, 8.0)
    c.setFillColor(to_color(accent))
    c.drawString(safe_x, oy + 56.0, "stackcalc.io")

    # Official KDP 2.00 in x 1.20 in (144 pt x 86.4 pt) White Barcode Box at bottom-right
    bc_w = 144.0
    bc_h = 86.4
    bc_x = safe_x + safe_w - bc_w
    bc_y = oy + 44.0
    if is_sc32:
        draw_vector_isbn_barcode(c, bc_x, bc_y, bc_w, bc_h, "979-8-9914832-2-3", "9798991483223", "$19.00 US  •  CAN $25.99")
    else:
        draw_vector_isbn_barcode(c, bc_x, bc_y, bc_w, bc_h, "979-8-9914832-1-6", "9798991483216", "$19.00 US  •  CAN $25.99")

    c.restoreState()


def build_kdp_front_matter(is_sc32: bool, styles: Dict[str, ParagraphStyle]) -> List[Flowable]:
    """
    Generates traditional KDP 6x9 trade/reference book front matter (Pages i–iv in lowercase Roman):
      - Page i   (Recto / Odd):  Half-Title Page (no header, no footer folio)
      - Page ii  (Verso / Even): Series Frontispiece ("The StackCalc Library") (no header, no footer folio)
      - Page iii (Recto / Odd):  Full Title Page with Title, Subtitle & StackCalc imprint (no header, no footer folio)
      - Page iv  (Verso / Even): Copyright, ISBN-13, Safety Notices & KDP Colophon (Roman folio 'iv')
    Covers are NEVER included inside the KDP interior manuscript PDF.
    """
    elements: List[Flowable] = []

    half_title_style = ParagraphStyle(
        "KDPHalfTitle",
        parent=styles["Normal"],
        fontName=FONT_BODY_BOLD,
        fontSize=22.0,
        leading=27.0,
        textColor=to_color(TEXT_MAIN),
        alignment=0,
    )
    half_sub_style = ParagraphStyle(
        "KDPHalfSub",
        parent=styles["Normal"],
        fontName=FONT_BODY_ITALIC,
        fontSize=11.0,
        leading=15.0,
        textColor=to_color(TEXT_MUTED),
        alignment=0,
    )
    kicker_style = ParagraphStyle(
        "KDPFrontKicker",
        parent=styles["Normal"],
        fontName=FONT_MONO_BOLD,
        fontSize=7.8,
        leading=11.0,
        textColor=to_color(TEXT_MUTED),
        alignment=0,
    )
    full_title_style = ParagraphStyle(
        "KDPFullTitle",
        parent=styles["Normal"],
        fontName=FONT_BODY_BOLD,
        fontSize=30.0,
        leading=35.0,
        textColor=to_color(TEXT_MAIN),
        alignment=0,
    )
    full_sub_style = ParagraphStyle(
        "KDPFullSub",
        parent=styles["Normal"],
        fontName=FONT_BODY_BOLD,
        fontSize=13.0,
        leading=17.5,
        textColor=to_color(TEXT_MAIN),
        alignment=0,
    )
    full_desc_style = ParagraphStyle(
        "KDPFullDesc",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=9.8,
        leading=14.0,
        textColor=to_color(TEXT_MUTED),
        alignment=0,
    )
    imprint_style = ParagraphStyle(
        "KDPImprint",
        parent=styles["Normal"],
        fontName=FONT_BODY_BOLD,
        fontSize=12.0,
        leading=15.5,
        textColor=to_color(TEXT_MAIN),
        alignment=0,
    )
    copyright_style = ParagraphStyle(
        "KDPCopyright",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=7.8,
        leading=11.0,
        textColor=to_color(TEXT_MAIN),
        spaceAfter=5,
    )

    main_title = "THINKING IN THE STACK" if is_sc32 else "FROM BLOCKS TO THE STACK"
    vol_label = "THE STACKCALC LIBRARY  •  VOLUME II" if is_sc32 else "THE STACKCALC LIBRARY  •  VOLUME I"
    sub_line = (
        "The Art of Calculating Without Parentheses"
        if is_sc32 else
        "How Hands-On Blocks Make Numbers Click"
    )
    desc_line = (
        "A Popular Guide &amp; Complete Desk Reference to Reverse Polish Notation, Tactile 3D Geometry, "
        "698+ Solved Problems, and 100 Master Equations — for the <b>StackCalc SC-32</b>"
        if is_sc32 else
        "A Visual Adventure &amp; Complete K–6 Reference Guide to Number Sense, Fractions, 3D Manipulative "
        "Blocks, and 552+ Real-World Problems — for the <b>StackCalc SC-6</b>"
    )

    # --- PAGE i (Recto): Half-Title Page ---
    elements.append(ChapterTracker("HALF TITLE"))
    elements.append(BookmarkFlowable("bm_halftitle", "Half-Title Page", level=0))
    elements.append(Spacer(1, 120))
    elements.append(make_paragraph(vol_label, kicker_style))
    elements.append(Spacer(1, 6))
    elements.append(make_paragraph(main_title, half_title_style))
    elements.append(Spacer(1, 8))
    elements.append(HRFlowable(width="25%", thickness=1.5, color=to_color(TEXT_MAIN), hAlign='LEFT', spaceAfter=8))
    elements.append(make_paragraph(sub_line, half_sub_style))
    elements.append(PageBreak())

    # --- PAGE ii (Verso): Series Frontispiece ("The StackCalc Library") ---
    elements.append(ChapterTracker("SERIES FRONTISPIECE"))
    elements.append(Spacer(1, 100))
    elements.append(make_paragraph("BOOKS &amp; OPEN-SOURCE HARDWARE IN THE STACKCALC ECOSYSTEM", kicker_style))
    elements.append(Spacer(1, 8))
    elements.append(HRFlowable(width="100%", thickness=1.0, color=to_color(TEXT_MAIN), spaceAfter=10))
    elements.append(make_paragraph(
        "<b>Volume I — From Blocks to the Stack (StackCalc SC-6 Elementary Edition, Grades K–6)</b><br/>"
        "<i>How Hands-On Blocks Make Numbers Click</i><br/>"
        "ISBN 979-8-9914832-1-6  •  9 Chapters, 552+ Kid-Friendly Quests, 7 3D Manipulative Studios &amp; 25 Teacher Guides",
        copyright_style
    ))
    elements.append(Spacer(1, 6))
    elements.append(make_paragraph(
        "<b>Volume II — Thinking in the Stack (StackCalc SC-32 Scientific &amp; Engineering Edition)</b><br/>"
        "<i>The Art of Calculating Without Parentheses</i><br/>"
        "ISBN 979-8-9914832-2-3  •  14 Chapters, 698+ Solved STEM Problems, 100 Master Equations &amp; Numerical Methods",
        copyright_style
    ))
    elements.append(Spacer(1, 6))
    elements.append(make_paragraph(
        "<b>Companion Software &amp; 3D-Printable Manipulative Studios (stackcalc.io)</b><br/>"
        "• <b>StackCalc iOS, iPadOS &amp; watchOS Simulators:</b> Run the exact <code>RPNCore</code> engine on your phone, tablet, or wrist.<br/>"
        "• <b>OpenSCAD 42mm Gridfinity 3D Models:</b> Print Ten-Frames, 84mm Fraction Towers, Prime Blocks, Volvelles &amp; Geared Clocks.",
        copyright_style
    ))
    elements.append(PageBreak())

    # --- PAGE iii (Recto): Full Title Page ---
    elements.append(ChapterTracker("TITLE PAGE"))
    elements.append(BookmarkFlowable("bm_titlepage", "Title Page", level=0))
    elements.append(Spacer(1, 70))
    elements.append(make_paragraph(vol_label, kicker_style))
    elements.append(Spacer(1, 10))
    elements.append(make_paragraph(main_title, full_title_style))
    elements.append(Spacer(1, 12))
    elements.append(HRFlowable(width="100%", thickness=1.8, color=to_color(TEXT_MAIN), spaceAfter=12))
    elements.append(make_paragraph(sub_line, full_sub_style))
    elements.append(Spacer(1, 8))
    elements.append(make_paragraph(desc_line, full_desc_style))
    elements.append(Spacer(1, 150))
    elements.append(HRFlowable(width="100%", thickness=0.75, color=to_color(DIVIDER_HEX), spaceAfter=8))
    elements.append(make_paragraph("StackCalc", imprint_style))
    elements.append(make_paragraph(
        "San Francisco  •  Austin  •  stackcalc.io<br/>First Edition (Revision 1.2)",
        full_desc_style
    ))
    elements.append(PageBreak())

    # --- PAGE iv (Verso): Copyright, ISBN, Safety & KDP Colophon Page ---
    elements.append(ChapterTracker("COPYRIGHT AND COLOPHON"))
    elements.append(BookmarkFlowable("bm_copyright", "Copyright & Print Colophon", level=0))
    elements.append(Spacer(1, 24))
    isbn_str = "979-8-9914832-2-3" if is_sc32 else "979-8-9914832-1-6"
    sku_str = "STK-REF-32-V2" if is_sc32 else "STK-REF-06-V1"
    elements.append(make_paragraph(
        f"<b>{main_title}: {sub_line}</b><br/>"
        f"Copyright © 2026 by <b>StackCalc</b> (https://stackcalc.io). Some rights reserved.<br/>"
        f"Published by <b>StackCalc</b>, San Francisco, California &amp; Austin, Texas.<br/>"
        f"<b>ISBN-13:</b> {isbn_str} &nbsp;&nbsp;|&nbsp;&nbsp; <b>Catalog ID:</b> {sku_str} &nbsp;&nbsp;|&nbsp;&nbsp; <b>First Edition (Rev 1.2)</b>",
        copyright_style
    ))
    elements.append(make_paragraph(
        "<b>Open-Ecosystem License (CC BY-NC-SA 4.0):</b> Classroom teachers, university instructors, parents, and "
        "students are expressly permitted to reproduce worksheet tables, 4-register stack traces, and 3D manipulative "
        "STL/3MF models for non-commercial educational instruction under Creative Commons Attribution-NonCommercial-"
        "ShareAlike 4.0 International.",
        copyright_style
    ))
    elements.append(make_paragraph(
        "<b>100% Engine-Verified Mathematical Guarantee:</b> Every 4-register stack table (T, Z, Y, X), postfix keystroke "
        "sequence, and numerical solution in this volume has been programmatically executed and verified against the "
        "production <code>RPNCore</code> engine.",
        copyright_style
    ))
    elements.append(make_paragraph(
        "<b>Regulatory &amp; Physical Safety Notice (Reese’s Law / P.L. 117-171 / 16 CFR Part 1263 &amp; ASTM F963):</b> "
        "Physical calculator instruments that utilize coin or button cell batteries must maintain a captive, tool-secured "
        "battery compartment compliant with UL 4200A. 3D-printed 1×1 unit tiles (12 mm × 12 mm × 8 mm) and polyhedral dice "
        "constitute small parts under 16 CFR Part 1501; adult supervision is required for learners under 6 years of age.",
        copyright_style
    ))
    elements.append(make_paragraph(
        "<b>Trademark Notice:</b> <i>StackCalc</i>, <i>SC-32</i>, <i>SC-6</i>, and <i>RPNCore</i> are trademarks of StackCalc. "
        "<i>Common Core State Standards</i>, <i>Singapore Math</i>, <i>Bridges in Mathematics</i>, <i>AP</i>, <i>Hewlett-Packard</i>, "
        "and <i>Gridfinity</i> are trademarks of their respective owners, none of whom endorse or sponsor this publication.",
        copyright_style
    ))
    elements.append(make_paragraph(
        "<b>KDP Archival Print &amp; Typography Colophon:</b> Typeset in Nimbus Sans L, Nimbus Mono L, and Terminus LCD "
        "on 6.00 × 9.00 in (152.4 × 228.6 mm) archival white paper in high-contrast monochrome ink for Kindle Direct "
        "Publishing Paperback and Hardcover editions. Standalone full-bleed wrap cover (<code>"
        + ("sc32-full-wrap-cover.pdf" if is_sc32 else "sc6-full-wrap-cover.pdf")
        + "</code>) generated separately to exact KDP spine and bleed tolerances.",
        copyright_style
    ))
    elements.append(PageBreak())
    return elements


# ---------------------------------------------------------------------------
# 2D LaTeX Display Equation Renderer with Right-Aligned Equation Numbers
# ---------------------------------------------------------------------------
_DISPLAY_EQ_CACHE_DIR: Optional[Path] = None
_MATHTEXT_INITIALIZED: bool = False


def _chapter_eq_prefix(file_path: Path) -> str:
    """Returns the canonical chapter/appendix prefix for equation numbers (e.g., '0', '1'..'14', 'A'..'E')."""
    stem = file_path.stem.lower()
    if stem == "index":
        return "0"
    m = re.match(r"^0*(\d+)-", stem)
    if m:
        return m.group(1)
    m_app = re.match(r"^appendix-([a-z])-", stem)
    if m_app:
        return m_app.group(1).upper()
    return "X"


def _normalize_mathtext_latex(raw_tex: str) -> str:
    """Normalizes LaTeX display equation markup for matplotlib STIX mathtext rendering."""
    s = raw_tex.strip()
    if s.startswith("$$") and s.endswith("$$"):
        s = s[2:-2].strip()
    elif s.startswith("$") and s.endswith("$"):
        s = s[1:-1].strip()
    s = " ".join(line.strip() for line in s.splitlines() if line.strip())
    s = re.sub(r"\\(?:begin|end)\{(?:aligned|align\*?|array|cases|matrix|pmatrix|bmatrix)\}", "", s)
    s = s.replace("&", " ").replace(r"\\", r", \quad ")
    s = re.sub(r"</?[a-zA-Z][^>]*>", "", s)
    s = re.sub(r"\{\{key:([^}]+)\}\}", r"[\1]", s)
    s = s.replace(r"\tfrac", r"\frac").replace(r"\dfrac", r"\frac")
    s = s.replace(r"\leqslant", r"\leq").replace(r"\geqslant", r"\geq")
    s = s.replace(r"\lvert", "|").replace(r"\rvert", "|")
    s = s.replace(r"\lVert", r"\|").replace(r"\rVert", r"\|")
    s = s.replace(r"\implies", r"\Rightarrow").replace(r"\iff", r"\Leftrightarrow")
    s = s.replace(r"\to", r"\rightarrow").replace(r"\gets", r"\leftarrow")
    s = s.replace(r"\land", r"\wedge").replace(r"\lor", r"\vee").replace(r"\lnot", r"\neg")
    s = s.replace(r"\empty", r"\emptyset").replace(r"\degree", r"^\circ")
    s = s.replace(r"\parallel", r"\Vert")
    s = s.replace(r"\Box", r"\square")
    s = re.sub(r"\\pmod\{((?:[^{}]|\{[^{}]*\})*)\}", r"\\;(\\mathrm{mod}\\; \1)", s)
    s = re.sub(r"\\bmod\b", r"\\;\\mathrm{mod}\\;", s)
    s = re.sub(r"\\xrightarrow\{([^{}]*)\}", r"\\stackrel{\1}{\\longrightarrow}", s)
    for _ in range(3):
        s = re.sub(
            r"\\(?:text|textbf|textit|textrm|operatorname)\{([^{}]*)\}",
            lambda m: r"\mathrm{" + m.group(1).replace(" ", r"\ ") + "}",
            s,
        )
        s = re.sub(
            r"\\(?:mathbf|boldsymbol|bm)\{([^{}]*)\}",
            lambda m: r"\mathbf{" + m.group(1).replace(r"\cdot", r"}\cdot\mathbf{") + "}",
            s,
        )
    s = s.replace("−", "-").replace("×", r"\times ").replace("÷", r"\div ").replace("±", r"\pm ")
    s = s.replace("≤", r"\leq ").replace("≥", r"\geq ").replace("≠", r"\neq ").replace("≈", r"\approx ")
    s = s.replace("∞", r"\infty ").replace("π", r"\pi ").replace("°", r"^\circ ")
    s = s.replace("√", r"\sqrt")
    return s.strip()


def _render_latex_display_equation(
    raw_tex: str,
    eq_label: str,
    bm_key: str,
    styles: Dict[str, ParagraphStyle],
    is_sc32: bool,
) -> Flowable:
    """
    Renders a standalone $$...$$ LaTeX display formula as a high-DPI 2D mathematical
    typeset block centered in the text frame with a right-aligned equation number (Eq. C.N).
    """
    global _DISPLAY_EQ_CACHE_DIR, _MATHTEXT_INITIALIZED
    import hashlib
    if _DISPLAY_EQ_CACHE_DIR is None:
        _DISPLAY_EQ_CACHE_DIR = Path("/tmp/stackcalc_display_eqs_v4")
        _DISPLAY_EQ_CACHE_DIR.mkdir(parents=True, exist_ok=True)

    norm_tex = _normalize_mathtext_latex(raw_tex)
    eq_col_w = PRINTABLE_WIDTH - 54.0
    num_col_w = 54.0

    eq_num_style = ParagraphStyle(
        "EquationNumber",
        parent=styles["BodyText"],
        fontName=FONT_BODY_BOLD,
        fontSize=8.0,
        leading=10.0,
        alignment=2,
        textColor=to_color(TEXT_MUTED),
    )
    num_para = make_paragraph(f"<a name='{bm_key}'/>({eq_label})", eq_num_style)

    eq_flowable: Optional[Flowable] = None
    try:
        import matplotlib
        if not _MATHTEXT_INITIALIZED:
            matplotlib.use("Agg")
            from matplotlib import rcParams
            rcParams["mathtext.fontset"] = "stix"
            rcParams["font.family"] = "STIXGeneral"
            _MATHTEXT_INITIALIZED = True
        from matplotlib import mathtext
        from matplotlib.font_manager import FontProperties
        from PIL import Image, ImageChops

        digest = hashlib.sha1(norm_tex.encode("utf-8")).hexdigest()[:16]
        png_path = _DISPLAY_EQ_CACHE_DIR / f"eq_{digest}.png"
        meta_path = _DISPLAY_EQ_CACHE_DIR / f"eq_{digest}.txt"

        if not png_path.exists() or not meta_path.exists():
            prop = FontProperties(size=10.5)
            dpi = 300
            mathtext.math_to_image(
                f"${norm_tex}$",
                str(png_path),
                prop=prop,
                dpi=dpi,
                format="png",
                color="#111827",
            )
            with Image.open(png_path) as im:
                im = im.convert("RGBA")
                bg = Image.new("RGBA", im.size, (255, 255, 255, 0))
                diff = ImageChops.difference(im, bg)
                bbox = diff.getbbox()
                if bbox:
                    pad = 4
                    left = max(0, bbox[0] - pad)
                    top = max(0, bbox[1] - pad)
                    right = min(im.size[0], bbox[2] + pad)
                    bottom = min(im.size[1], bbox[3] + pad)
                    im = im.crop((left, top, right, bottom))
                white_bg = Image.new("RGB", im.size, (255, 255, 255))
                white_bg.paste(im, mask=im.split()[3])
                white_bg.save(png_path, format="PNG")
                w_px, h_px = white_bg.size
            meta_path.write_text(f"{w_px},{h_px}", encoding="utf-8")
        else:
            w_str, h_str = meta_path.read_text(encoding="utf-8").strip().split(",")
            w_px, h_px = int(w_str), int(h_str)

        w_pt = (w_px / 300.0) * 72.0
        h_pt = (h_px / 300.0) * 72.0
        max_w = eq_col_w - 8.0
        max_h = 44.0
        scale = min(max_w / max(1.0, w_pt), max_h / max(1.0, h_pt), 1.0)
        # If single-line image would scale down too small (< 0.66), fall back to clean wrapped math paragraph
        if scale >= 0.66:
            rl_img = RLImage(str(png_path), width=w_pt * scale, height=h_pt * scale)
            rl_img.hAlign = "CENTER"
            eq_flowable = rl_img
    except Exception:
        eq_flowable = None

    if eq_flowable is None:
        inner_raw = raw_tex.strip()
        if inner_raw.startswith("$$") and inner_raw.endswith("$$"):
            inner_raw = inner_raw[2:-2].strip()
        cleaned = clean_latex_math(inner_raw)
        disp_style = ParagraphStyle(
            "DisplayMathFallback",
            parent=styles["BodyText"],
            fontName=FONT_BODY_BOLD,
            fontSize=8.8,
            leading=11.6,
            alignment=1,
            textColor=to_color(TEXT_MAIN),
        )
        eq_flowable = make_paragraph(cleaned, disp_style)

    eq_tbl = Table([[eq_flowable, num_para]], colWidths=[eq_col_w, num_col_w])
    eq_tbl.setStyle(TableStyle([
        ("ALIGN", (0, 0), (0, 0), "CENTER"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
    ]))
    return KeepTogether([
        Spacer(1, 2.0),
        eq_tbl,
        Spacer(1, 3.0),
    ])


# ---------------------------------------------------------------------------
# Markdown File to Flowables Parser (Archival White Paper Interior)
# ---------------------------------------------------------------------------
def parse_markdown_file(
    file_path: Path,
    chapter_idx: int,
    is_sc32: bool,
    styles: Dict[str, ParagraphStyle],
    term_counts: Optional[Dict[str, int]] = None
) -> List[Flowable]:
    """
    Parses a single manual markdown file and converts its headings, tables, code blocks,
    and text into publication-grade ReportLab Flowables on pure white paper.
    """
    elements: List[Flowable] = []
    primary_hex = SC32_PRIMARY if is_sc32 else SC6_PRIMARY
    accent_hex = SC32_ACCENT if is_sc32 else SC6_ACCENT

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip YAML frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

    # Auto-number sections and expand/validate keystroke macros from app layout JSON
    from book_engine import process_manual_markdown
    content = process_manual_markdown(content, file_path, is_sc32=is_sc32, target_format="pdf")

    # Normalize multi-line display math blocks ($$ ... $$) outside fenced code blocks into standalone $$ ... $$ lines
    fenced_blocks = {}
    def _save_fenced(m):
        k = f"QQFENCE{len(fenced_blocks)}QQ"
        fenced_blocks[k] = m.group(0)
        return k
    content = re.sub(r'```.*?```', _save_fenced, content, flags=re.DOTALL)
    content = re.sub(
        r'(?<!\\)\$\$(.+?)(?<!\\)\$\$',
        lambda m: (
            m.group(0)
            if "\n>" in m.group(0)
            else "\n$$" + " ".join(l.strip() for l in m.group(1).splitlines() if l.strip()) + "$$\n"
        ),
        content,
        flags=re.DOTALL
    )
    # Ensure any inline $$ ... $$ on a prose line (not inside a table or blockquote) sits on its own standalone line
    # and split any trailing horizontal rule (---) at the end of a prose line onto its own line
    norm_prose_lines = []
    for raw_ln in content.split("\n"):
        s_ln = raw_ln.strip()
        if not s_ln.startswith("|") and not s_ln.startswith(">") and not re.match(r'^(?:---|\*\*\*|___)\s*$', s_ln):
            raw_ln = re.sub(r'\s+---\s*$', '\n---\n', raw_ln)
        if not s_ln.startswith("|") and not s_ln.startswith(">") and "$$" in s_ln:
            raw_ln = re.sub(
                r'(?<!\\)\$\$(.+?)(?<!\\)\$\$',
                lambda m: "\n$$" + " ".join(x.strip() for x in m.group(1).splitlines() if x.strip()) + "$$\n",
                raw_ln,
            )
        norm_prose_lines.append(raw_ln)
    content = "\n".join(norm_prose_lines)
    for k, v in fenced_blocks.items():
        content = content.replace(k, v)

    eq_prefix = _chapter_eq_prefix(file_path)
    eq_counter = 0

    lines = content.split("\n")
    i = 0
    num_lines = len(lines)
    is_first_h1 = True

    while i < num_lines:
        line = lines[i].rstrip()

        # Empty line
        if not line:
            i += 1
            continue

        # Horizontal Rule
        if re.match(r'^(?:---|\*\*\*|___)\s*$', line):
            elements.append(Spacer(1, 4))
            elements.append(HRFlowable(width="100%", thickness=0.5, color=to_color(DIVIDER_HEX), spaceAfter=8))
            i += 1
            continue

        # HTML figure block (defensive fallback: ignore raw HTML figure wrappers)
        if line.startswith("<figure") or line.startswith("</figure>") or line.startswith("<figcaption"):
            i += 1
            continue

        # HTML Callout div block (skip web-only te-viewport-header banners; render figure captions or admonitions)
        if line.startswith("<div") or line.startswith("<span"):
            div_lines = []
            div_depth = 0
            while i < num_lines:
                cur_l = lines[i]
                div_lines.append(cur_l)
                div_depth += len(re.findall(r'<div\b', cur_l))
                div_depth -= len(re.findall(r'</div>', cur_l))
                i += 1
                if div_depth <= 0 and ("</div>" in cur_l or "</span>" in cur_l):
                    break
            div_text = "\n".join(div_lines)
            if "te-viewport-header" in div_text:
                continue
            is_centered_caption_div = ("text-align: center" in div_text or "text-align:center" in div_text)
            # Convert inline HTML tags to markdown before splitting into structured lines
            div_text = re.sub(r'<code>(.*?)</code>', r'`\1`', div_text)
            div_text = re.sub(r'<(?:strong|b)>(.*?)</(?:strong|b)>', r'**\1**', div_text)
            div_text = re.sub(r'<(?:em|i)>(.*?)</(?:em|i)>', r'*\1*', div_text)
            div_text = re.sub(r'<p\s+class=["\']admonition-title["\']>\s*(.*?)\s*</p>', r'**\1**\n', div_text, flags=re.IGNORECASE | re.DOTALL)
            div_text = re.sub(r'<li>\s*', '\n• ', div_text, flags=re.IGNORECASE)
            div_text = re.sub(r'(?:<br\s*/?>|</p>|</li>|</ul>|</ol>)', '\n', div_text, flags=re.IGNORECASE)
            # Only strip valid HTML tags starting with </?[a-zA-Z] so math inequalities like < 10 are never eaten!
            clean_text = re.sub(r'</?[a-zA-Z][^>]*>', ' ', div_text)
            clean_text = re.sub(
                r'(?<!\\)\$\$(.+?)(?<!\\)\$\$',
                lambda m: '$$' + ' '.join(s.strip() for s in m.group(1).splitlines() if s.strip()) + '$$',
                clean_text,
                flags=re.DOTALL,
            )
            flat_clean = re.sub(r'\s+', ' ', clean_text).strip()
            if is_centered_caption_div or re.match(r'^(?:\*|_)?Figure\s+\d', flat_clean):
                if flat_clean:
                    cap_san = sanitize_inline_markdown(flat_clean, is_sc32)
                    elements.append(make_paragraph(f"<i>{cap_san}</i>", styles["FigureCaption"]))
                    elements.append(Spacer(1, 4))
                continue
            div_rows = []
            for raw_dl in clean_text.split("\n"):
                dl_clean = re.sub(r'\s+', ' ', raw_dl).strip()
                if dl_clean:
                    dl_san = sanitize_inline_markdown(dl_clean, is_sc32)
                    div_rows.append([make_paragraph(dl_san, styles["CalloutText"])])
            if div_rows:
                callout_tbl = Table(div_rows, colWidths=[PRINTABLE_WIDTH], splitByRow=1)
                callout_tbl.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,-1), to_color(CALLOUT_BG_SC32 if is_sc32 else CALLOUT_BG_SC6)),
                    ('LINEBEFORE', (0,0), (0,-1), 2.5, to_color(primary_hex)),
                    ('BOX', (0,0), (-1,-1), 0.5, to_color(DIVIDER_HEX)),
                    ('LEFTPADDING', (0,0), (-1,-1), 8),
                    ('RIGHTPADDING', (0,0), (-1,-1), 8),
                    ('TOPPADDING', (0,0), (-1,-1), 2),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
                    ('TOPPADDING', (0,0), (-1,0), 5),
                    ('BOTTOMPADDING', (0,-1), (-1,-1), 5),
                ]))
                elements.append(Spacer(1, 3))
                elements.append(callout_tbl)
                elements.append(Spacer(1, 5))
            continue

        # Blockquote (e.g. > [!NOTE] or > quote)
        if line.startswith(">"):
            quote_lines = []
            while i < num_lines and lines[i].startswith(">"):
                quote_lines.append(lines[i].lstrip("> ").strip())
                i += 1

            # Detect callout badge on first non-empty line
            while quote_lines and not quote_lines[0]:
                quote_lines.pop(0)
            badge_title = ""
            badge_color = primary_hex
            if quote_lines:
                badge_match = re.match(r'^\[!(NOTE|IMPORTANT|TIP|WARNING|CHECKPOINT|TEACHER)\]\s*(.*)$', quote_lines[0], flags=re.IGNORECASE)
                if badge_match:
                    tag = badge_match.group(1).upper()
                    rem = badge_match.group(2).strip()
                    if rem:
                        quote_lines[0] = rem
                    else:
                        quote_lines.pop(0)
                    if tag == "IMPORTANT":
                        badge_title = "CRITICAL CHECKPOINT // ARCHITECTURAL INVARIANT"
                        badge_color = primary_hex
                    elif tag == "NOTE":
                        badge_title = "OPERATIONAL NOTE // RPN STACK INSIGHT"
                        badge_color = accent_hex
                    elif tag == "TIP":
                        badge_title = "PRO TIP // KEYSTROKE ACCELERATOR"
                        badge_color = accent_hex
                    elif tag == "WARNING":
                        badge_title = "SINGULARITY WARNING // HARDWARE RECOVERY"
                        badge_color = "#b91c1c"
                    elif tag == "CHECKPOINT":
                        badge_title = "DIAGNOSTIC CHECKPOINT // VERIFY YOUR STACK"
                        badge_color = primary_hex
                    elif tag == "TEACHER":
                        badge_title = "GUIDED DISCOVERY // HANDS-ON EXTENSION"
                        badge_color = primary_hex
                    else:
                        badge_title = f"{tag} // STACKCALC REFERENCE"
                        badge_color = primary_hex

            quote_joined = "\n".join(quote_lines)
            quote_joined = re.sub(
                r'\$\$([^\$]+)\$\$',
                lambda m: '$$' + ' '.join(s.strip() for s in m.group(1).splitlines() if s.strip()) + '$$',
                quote_joined,
            )
            quote_lines = quote_joined.split("\n") if quote_joined else []

            quote_rows = []
            extra_top_rows = []
            if badge_title:
                badge_html = f"<b><font size='8.5' face='{FONT_BODY_BOLD}' color='{badge_color}'>{badge_title}</font></b>"
                quote_rows.append([make_paragraph(badge_html, styles["CalloutText"])])

            prev_blank = bool(badge_title)
            for ql in quote_lines:
                if not ql:
                    prev_blank = True
                else:
                    ql_norm = re.sub(r'^[\*\-]\s+', '• ', ql)
                    ql_san = sanitize_inline_markdown(ql_norm, is_sc32)
                    if prev_blank and quote_rows:
                        extra_top_rows.append(len(quote_rows))
                    quote_rows.append([make_paragraph(ql_san, styles["CalloutText"])])
                    prev_blank = False

            if quote_rows:
                q_style = [
                    ('BACKGROUND', (0,0), (-1,-1), to_color(CALLOUT_BG_SC32 if is_sc32 else CALLOUT_BG_SC6)),
                    ('LINEBEFORE', (0,0), (0,-1), 3.5, to_color(badge_color)),
                    ('BOX', (0,0), (-1,-1), 0.5, to_color(DIVIDER_HEX)),
                    ('LEFTPADDING', (0,0), (-1,-1), 10),
                    ('RIGHTPADDING', (0,0), (-1,-1), 10),
                    ('TOPPADDING', (0,0), (-1,-1), 1.5),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
                    ('TOPPADDING', (0,0), (-1,0), 6),
                    ('BOTTOMPADDING', (0,-1), (-1,-1), 6),
                ]
                for r_idx in extra_top_rows:
                    q_style.append(('TOPPADDING', (0, r_idx), (-1, r_idx), 5))
                callout_tbl = Table(quote_rows, colWidths=[PRINTABLE_WIDTH], splitByRow=1)
                callout_tbl.setStyle(TableStyle(q_style))
                elements.append(Spacer(1, 4))
                elements.append(callout_tbl)
                elements.append(Spacer(1, 6))
            continue

        # Code Block or ASCII Art Diagram (``` ... ```)
        if line.startswith("```"):
            code_lines = []
            i += 1
            while i < num_lines and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            if i < num_lines and lines[i].startswith("```"):
                i += 1

            # Chunk into at most 35 lines per table to allow clean page breaking across frames
            MAX_CODE_CHUNK = 35
            line_chunks = [code_lines[c_idx:c_idx + MAX_CODE_CHUNK] for c_idx in range(0, max(1, len(code_lines)), MAX_CODE_CHUNK)]

            for chunk_idx, ch_lines in enumerate(line_chunks):
                raw_code = "\n".join(ch_lines)
                raw_code = raw_code.replace("\t", "    ")
                raw_code = raw_code.replace("⇄", "↔").replace("∑", "Σ").replace("🎲", "[DICE]").replace("🕒", "[CLOCK]").replace("↰", "↲").replace("↱", "↳").replace("▸", "->")

                # Check if this represents an LCD preview or hardware diagram
                is_lcd_preview = any(k in raw_code for k in ["TRANSFLECTIVE", "LCD", "OPERATIONAL DISPLAY", "+===+", "+---+", "T:", "Z:", "Y:", "X:"])

                pre_style = styles["CodePreformatted"]
                pre_flowable = Preformatted(raw_code, pre_style)
                code_table = Table([[pre_flowable]], colWidths=[PRINTABLE_WIDTH])
                if is_lcd_preview:
                    code_table.setStyle(TableStyle([
                        ('BACKGROUND', (0,0), (-1,-1), to_color(STACK_FRAME_BG)),
                        ('LINEBEFORE', (0,0), (0,-1), 2.5, to_color(primary_hex)),
                        ('BOX', (0,0), (-1,-1), 0.75, to_color(DIVIDER_HEX)),
                        ('TOPPADDING', (0,0), (-1,-1), 5),
                        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
                        ('LEFTPADDING', (0,0), (-1,-1), 8),
                        ('RIGHTPADDING', (0,0), (-1,-1), 8),
                    ]))
                else:
                    code_table.setStyle(TableStyle([
                        ('BACKGROUND', (0,0), (-1,-1), to_color(STACK_FRAME_BG)),
                        ('BOX', (0,0), (-1,-1), 0.75, to_color(DIVIDER_HEX)),
                        ('TOPPADDING', (0,0), (-1,-1), 4),
                        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
                        ('LEFTPADDING', (0,0), (-1,-1), 7),
                        ('RIGHTPADDING', (0,0), (-1,-1), 7),
                    ]))
                if chunk_idx == 0:
                    elements.append(Spacer(1, 4))
                elements.append(code_table)
                if chunk_idx < len(line_chunks) - 1:
                    elements.append(Spacer(1, 2))
                else:
                    elements.append(Spacer(1, 6))
            continue

        # Markdown Table (| col 1 | col 2 |)
        if line.startswith("|"):
            table_lines = []
            while i < num_lines and lines[i].strip().startswith("|"):
                t_l = lines[i].strip()
                if not t_l.endswith("|"):
                    t_l += " |"
                table_lines.append(t_l)
                i += 1

            if len(table_lines) >= 2:
                parsed_rows = []
                for r_idx, t_line in enumerate(table_lines):
                    if re.match(r'^\|(?:\s*:?-+:?\s*\|)+$', t_line):
                        continue
                    inner_line = t_line.strip()
                    if inner_line.startswith('|'):
                        inner_line = inner_line[1:]
                    if inner_line.endswith('|'):
                        inner_line = inner_line[:-1]
                    inner_line = inner_line.replace(r'\|', '\x00PIPE\x00')
                    inner_line = re.sub(r'\{\{[^}]+\}\}', lambda m: m.group(0).replace('|', '\x00PIPE\x00'), inner_line)
                    inner_line = re.sub(r'`[^`]+`', lambda m: m.group(0).replace('|', '\x00PIPE\x00'), inner_line)
                    inner_line = re.sub(r'\$[^\$\n]+\$', lambda m: m.group(0).replace('|', '\x00PIPE\x00'), inner_line)
                    raw_cells = [c.replace('\x00PIPE\x00', '|').strip() for c in inner_line.split('|')]
                    parsed_rows.append((r_idx == 0, raw_cells))

                if parsed_rows:
                    hdr_cols = len(parsed_rows[0][1])
                    num_cols = hdr_cols if hdr_cols >= 2 else max(len(cells) for _, cells in parsed_rows)
                    normalized_data = []
                    col_char_counts = [1] * num_cols
                    col_min_widths = [24.0] * num_cols
                    is_stack_col = [False] * num_cols
                    is_step_col = [False] * num_cols

                    for is_hdr, cells in parsed_rows:
                        row_elements = []
                        while len(cells) < num_cols:
                            cells.append("")
                        if len(cells) > num_cols:
                            cells = cells[:num_cols - 1] + [" | ".join(cells[num_cols - 1:])]
                        for c_idx, cell_str in enumerate(cells):
                            if is_hdr and num_cols >= 5:
                                # Compact verbose stack table headers for 6x9 trade width so they never wrap onto 2 lines
                                h_clean = cell_str.strip()
                                if re.match(r'^\*?Register\s+([TZYX])\*?$', h_clean, flags=re.IGNORECASE):
                                    reg_letter = re.sub(r'^\*?Register\s+([TZYX])\*?$', r'\1', h_clean, flags=re.IGNORECASE).upper()
                                    cell_str = f"Reg {reg_letter}"
                                    is_stack_col[c_idx] = True
                                elif re.match(r'^\*?[TZYX]\*?$', h_clean):
                                    is_stack_col[c_idx] = True
                                elif re.match(r'^\*?Step\*?$', h_clean, flags=re.IGNORECASE) and num_cols >= 6:
                                    cell_str = "#"
                                    is_step_col[c_idx] = True

                            sanitized = sanitize_inline_markdown(cell_str, is_sc32, in_table=True)
                            # Convert inline <img width="W".../> tags (and any immediately following space) into
                            # contiguous synthetic characters so ReportLab's <img/> + word run never overflows a column
                            measured_str = re.sub(
                                r"<img\b[^>]*width=['\"]([\d.]+)['\"][^>]*/?>\s*",
                                lambda m: "K" * max(4, int(round(float(m.group(1)) / 3.4))),
                                sanitized,
                            )
                            plain_cell = re.sub(r'</?[a-zA-Z][^>]*>', '', measured_str)
                            plain_cell = html.unescape(plain_cell).strip()
                            col_char_counts[c_idx] = max(col_char_counts[c_idx], len(plain_cell))

                            words = [w for w in re.split(r'[ \t\n/—–]+', plain_cell) if w]
                            longest_w = max((len(w) for w in words), default=0)
                            char_pt = 4.35 if is_hdr else 4.10
                            word_floor = longest_w * char_pt + 8.0
                            col_min_widths[c_idx] = max(col_min_widths[c_idx], min(82.0, word_floor))

                            cell_style = styles["TableHeader"] if is_hdr else styles["TableCell"]
                            row_elements.append(make_paragraph(sanitized, cell_style))
                        normalized_data.append(row_elements)

                    # Special compact sizing for 4-register stack columns and Step column
                    for c_idx in range(num_cols):
                        if is_step_col[c_idx]:
                            col_min_widths[c_idx] = 20.0
                            col_char_counts[c_idx] = min(col_char_counts[c_idx], 3)
                        elif is_stack_col[c_idx]:
                            col_min_widths[c_idx] = max(32.0, min(55.0, col_char_counts[c_idx] * 3.85 + 7.5))

                    # Scale down col_min_widths proportionally if their sum exceeds 88% of PRINTABLE_WIDTH
                    min_sum = sum(col_min_widths)
                    if min_sum > PRINTABLE_WIDTH * 0.88:
                        scale_f = (PRINTABLE_WIDTH * 0.88) / min_sum
                        col_min_widths = [mw * scale_f for mw in col_min_widths]

                    # Damped power-law distribution so long commentary paragraphs never starve label/keycap columns
                    weights = [max(1.0, float(c_cnt)) ** 0.58 for c_cnt in col_char_counts]
                    for c_idx in range(num_cols):
                        if is_step_col[c_idx]:
                            weights[c_idx] = 0.6
                        elif is_stack_col[c_idx]:
                            weights[c_idx] = min(weights[c_idx], 3.1)

                    total_weight = max(0.01, sum(weights))
                    col_widths = [(w / total_weight) * PRINTABLE_WIDTH for w in weights]

                    locked = [is_step_col[c] or is_stack_col[c] for c in range(num_cols)]
                    for c_idx in range(num_cols):
                        if locked[c_idx]:
                            col_widths[c_idx] = col_min_widths[c_idx]

                    for _ in range(num_cols + 1):
                        locked_sum = sum(col_widths[c] for c in range(num_cols) if locked[c])
                        rem_w = max(10.0, PRINTABLE_WIDTH - locked_sum)
                        unlocked_w = sum(weights[c] for c in range(num_cols) if not locked[c])
                        if unlocked_w > 0:
                            for c in range(num_cols):
                                if not locked[c]:
                                    col_widths[c] = (weights[c] / unlocked_w) * rem_w
                        changed = False
                        for c in range(num_cols):
                            if not locked[c] and col_widths[c] < col_min_widths[c]:
                                col_widths[c] = col_min_widths[c]
                                locked[c] = True
                                changed = True
                        if not changed:
                            break

                    w_sum = sum(col_widths)
                    col_widths = [(w / w_sum) * PRINTABLE_WIDTH for w in col_widths]

                    reportlab_table = Table(normalized_data, colWidths=col_widths, repeatRows=1)
                    reportlab_table.setStyle(TableStyle([
                        ('BACKGROUND', (0,0), (-1,0), to_color(primary_hex)),
                        ('TEXTCOLOR', (0,0), (-1,0), white),
                        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                        ('TOPPADDING', (0,0), (-1,-1), 2.5),
                        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
                        ('LEFTPADDING', (0,0), (-1,-1), 3.5),
                        ('RIGHTPADDING', (0,0), (-1,-1), 3.5),
                        ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, to_color("#f8fafc")]),
                        ('GRID', (0,0), (-1,-1), 0.5, to_color(DIVIDER_HEX)),
                        ('LINEBELOW', (0,0), (-1,0), 1.0, to_color(primary_hex)),
                        ('BOX', (0,0), (-1,-1), 0.85, to_color(primary_hex)),
                    ]))
                    if len(normalized_data) <= 28:
                        # Float table as an unsplit block so it never splits across a page break
                        if len(elements) >= 2 and isinstance(elements[-2], Paragraph):
                            vis_txt = re.sub(r"<[^>]+>", "", getattr(elements[-2], "text", ""))
                            if len(vis_txt) < 260:
                                elements[-2].keepWithNext = True
                        elements.append(KeepTogether([Spacer(1, 3), reportlab_table, Spacer(1, 5)]))
                    else:
                        elements.append(Spacer(1, 3))
                        elements.append(reportlab_table)
                        elements.append(Spacer(1, 5))
            continue

        # Heading 1 (# Chapter Title)
        if line.startswith("# "):
            title = line[2:].strip()
            plain_title, styled_title = format_heading_text(title, is_sc32=is_sc32)

            if chapter_idx > 0 or not is_first_h1:
                elements.append(PageBreak())
            is_first_h1 = False

            elements.append(ChapterTracker(plain_title))

            bm_key = f"bm_ch_{chapter_idx}_{i}"
            elements.append(BookmarkFlowable(bm_key, plain_title, level=0))

            h1_p = make_paragraph(styled_title, styles["Heading1"])
            h1_p._toc_info = (0, plain_title, bm_key)
            terms = extract_index_terms(plain_title, is_sc32, term_counts)
            if terms:
                h1_p._index_terms = terms
            elements.append(h1_p)
            elements.append(Spacer(1, 3))
            elements.append(HRFlowable(width="100%", thickness=1.5, color=to_color(primary_hex), spaceAfter=10))
            i += 1
            continue

        # Heading 2 (## Section Title)
        if line.startswith("## "):
            title = line[3:].strip()
            plain_title, styled_title = format_heading_text(title, is_sc32=is_sc32)

            bm_key = f"bm_sec_{chapter_idx}_{i}"
            elements.append(BookmarkFlowable(bm_key, plain_title, level=1))

            h2_p = make_paragraph(styled_title, styles["Heading2"])
            h2_p._toc_info = (1, plain_title, bm_key)
            terms = extract_index_terms(plain_title, is_sc32, term_counts)
            if terms:
                h2_p._index_terms = terms
            elements.append(Spacer(1, 6))
            elements.append(h2_p)
            elements.append(Spacer(1, 3))
            i += 1
            continue

        # Heading 3 (### Sub-section Title)
        if line.startswith("### "):
            title = line[4:].strip()
            plain_title, styled_title = format_heading_text(title, is_sc32=is_sc32)

            bm_key = f"bm_sub_{chapter_idx}_{i}"
            elements.append(BookmarkFlowable(bm_key, plain_title, level=2))

            h3_p = make_paragraph(styled_title, styles["Heading3"])
            terms = extract_index_terms(plain_title, is_sc32, term_counts)
            if terms:
                h3_p._index_terms = terms
            elements.append(Spacer(1, 5))
            elements.append(h3_p)
            elements.append(Spacer(1, 2))
            i += 1
            continue

        # Heading 4 (#### Sub-sub-section Title)
        if line.startswith("#### "):
            title = line[5:].strip()
            plain_title, styled_title = format_heading_text(title, is_sc32=is_sc32)

            h4_p = make_paragraph(styled_title, styles["Heading4"])
            terms = extract_index_terms(plain_title, is_sc32, term_counts)
            if terms:
                h4_p._index_terms = terms
            elements.append(Spacer(1, 4))
            elements.append(h4_p)
            elements.append(Spacer(1, 2))
            i += 1
            continue

        # Bullet List (- or *)
        if re.match(r'^\s*[-*]\s+', line):
            list_items = []
            while i < num_lines and re.match(r'^\s*[-*]\s+', lines[i]):
                item_text = re.sub(r'^\s*[-*]\s+', '', lines[i]).strip()
                list_items.append(item_text)
                i += 1

            for itm in list_items:
                sanitized = sanitize_inline_markdown(itm, is_sc32)
                bullet_p = make_paragraph(f"&bull; &nbsp; {sanitized}", styles["ListBullet"])
                elements.append(bullet_p)
            elements.append(Spacer(1, 3))
            continue

        # Numbered List (1. 2. etc.)
        if re.match(r'^\s*\d+\.\s+', line):
            num_items = []
            while i < num_lines and re.match(r'^\s*(\d+)\.\s+', lines[i]):
                m = re.match(r'^\s*(\d+)\.\s+(.*)$', lines[i])
                if m:
                    num_items.append((m.group(1), m.group(2).strip()))
                i += 1

            for num_str, itm in num_items:
                sanitized = sanitize_inline_markdown(itm, is_sc32)
                num_p = make_paragraph(f"<b>{num_str}.</b> &nbsp; {sanitized}", styles["ListBullet"])
                elements.append(num_p)
            elements.append(Spacer(1, 3))
            continue

        # Markdown Image (![caption](path))
        img_match = re.match(r'^!\[(.*?)\]\((.*?)\)\s*$', line)
        if img_match:
            alt_text = img_match.group(1).strip()
            raw_path = img_match.group(2).strip()
            resolved_img = None
            candidates = [
                file_path.parent / raw_path,
                MANUALS_ROOT / raw_path.lstrip("/"),
                MANUALS_ASSETS_DIR / "screenshots" / Path(raw_path).name,
                MANUALS_ASSETS_DIR / Path(raw_path).name,
                REPO_ROOT / raw_path.lstrip("/"),
                DOCS_DIR / raw_path.lstrip("/"),
                REPO_ROOT / "docs" / raw_path.lstrip("/"),
                WATCH_CALC_ROOT / raw_path.lstrip("/"),
                WATCH_CALC_ROOT / "Education" / raw_path.lstrip("/"),
                WATCH_CALC_ROOT / "scratch" / "previews" / "education" / raw_path.lstrip("/"),
                DOCS_DIR / "assets" / "manuals" / "screenshots" / Path(raw_path).name,
                DOCS_DIR / "assets" / "manuals" / Path(raw_path).name,
                DOCS_DIR / "assets" / "renders" / Path(raw_path).name,
            ]
            for c in candidates:
                if c.exists() and c.is_file():
                    resolved_img = c
                    break

            # Check if the immediately following non-empty line in markdown is already an explicit Figure X.Y caption
            has_explicit_next_caption = False
            look_j = i + 1
            while look_j < num_lines and not lines[look_j].strip():
                look_j += 1
            if look_j < num_lines:
                nxt_s = lines[look_j].strip()
                if re.match(r'^(?:\*|_)?Figure\s+\d', nxt_s):
                    has_explicit_next_caption = True
                elif nxt_s.startswith("<div") and ("text-align: center" in "\n".join(lines[look_j:look_j+5]) or "Figure " in "\n".join(lines[look_j:look_j+5])):
                    has_explicit_next_caption = True

            if resolved_img:
                try:
                    import io
                    from PIL import ImageOps
                    with PIL.Image.open(resolved_img) as pimg:
                        orig_w, orig_h = pimg.size
                        max_w = PRINTABLE_WIDTH
                        max_h = 160.0
                        scale = min(max_w / orig_w, max_h / orig_h, 1.0)
                        w = orig_w * scale
                        h = orig_h * scale
                        if BW_PRINT_INTERIOR:
                            gray_img = ImageOps.autocontrast(pimg.convert("L"), cutoff=1)
                            img_buf = io.BytesIO()
                            gray_img.save(img_buf, format="PNG")
                            img_buf.seek(0)
                            rl_img = RLImage(img_buf, width=w, height=h)
                        else:
                            rl_img = RLImage(str(resolved_img), width=w, height=h)
                    rl_img.hAlign = 'CENTER'
                    elements.append(Spacer(1, 3))
                    elements.append(rl_img)
                    if alt_text and not has_explicit_next_caption:
                        elements.append(make_paragraph(f"<i>Figure: {alt_text}</i>", styles["FigureCaption"]))
                    elements.append(Spacer(1, 5))
                except Exception as ex:
                    print(f"[WARN] Failed to load image {resolved_img}: {ex}")
            else:
                elements.append(make_paragraph(f"<b>[FIGURE: {alt_text}]</b> (Source: {raw_path})", styles["CalloutText"]))
            i += 1
            continue

        # Standalone LaTeX Display Equation ($$ ... $$)
        if line.strip().startswith("$$") and line.strip().endswith("$$") and len(line.strip()) > 4:
            eq_counter += 1
            eq_label = f"Eq. {eq_prefix}.{eq_counter}"
            bm_key = f"bm_eq_{chapter_idx}_{eq_prefix}_{eq_counter}"
            eq_flowable = _render_latex_display_equation(line.strip(), eq_label, bm_key, styles, is_sc32)
            elements.append(eq_flowable)
            i += 1
            continue

        # Regular Paragraph
        para_lines = []
        while (
            i < num_lines
            and lines[i].strip()
            and not re.match(r'^(?:---|\*\*\*|___)\s*$', lines[i].strip())
            and not lines[i].strip().startswith("$$")
            and not lines[i].startswith("#")
            and not lines[i].startswith("```")
            and not lines[i].startswith("|")
            and not lines[i].startswith(">")
            and not re.match(r'^\s*[-*]\s+', lines[i])
            and not re.match(r'^\s*\d+\.\s+', lines[i])
            and not lines[i].startswith("<div")
            and not lines[i].startswith("![")
            and not lines[i].startswith("<figure")
            and not lines[i].startswith("</figure")
            and not lines[i].startswith("<figcaption")
        ):
            para_lines.append(lines[i].strip())
            i += 1

        if para_lines:
            raw_para = " ".join(para_lines)
            sanitized = sanitize_inline_markdown(raw_para, is_sc32)
            para_p = make_paragraph(sanitized, styles["BodyText"])
            terms = extract_index_terms(raw_para, is_sc32, term_counts)
            if terms:
                para_p._index_terms = terms
            elements.append(para_p)
            elements.append(Spacer(1, 2.5))
        elif i < num_lines:
            i += 1

    return elements


# ---------------------------------------------------------------------------
# Manual Compilation Orchestrator
# ---------------------------------------------------------------------------
def compile_manual_pdf(is_sc32: bool) -> Path:
    """Compiles either the SC-32 or SC-6 KDP-compliant 6x9 trade interior manuscript PDF."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pdf_filename = "sc32-scientific-manual.pdf" if is_sc32 else "sc6-elementary-manual.pdf"
    output_pdf_path = OUTPUT_DIR / pdf_filename

    print(f"\n=======================================================")
    print(f"Compiling KDP 6x9 Interior Manuscript: {output_pdf_path.name}")
    print(f"=======================================================")

    primary_hex = SC32_PRIMARY if is_sc32 else SC6_PRIMARY
    accent_hex = SC32_ACCENT if is_sc32 else SC6_ACCENT
    cover_bg_hex = SC32_COVER_BG if is_sc32 else SC6_COVER_BG
    cover_accent_hex = SC32_COVER_ACCENT if is_sc32 else SC6_COVER_ACCENT
    doc_code = "STK-REF-32-V2" if is_sc32 else "STK-REF-06-V1"

    # Style Sheet Setup (Calibrated for 6x9 Trade Paperback & Hardcover)
    styles = getSampleStyleSheet()

    styles["Heading1"].fontName = FONT_BODY_BOLD
    styles["Heading1"].fontSize = 16.5
    styles["Heading1"].leading = 20.0
    styles["Heading1"].textColor = to_color(primary_hex)
    styles["Heading1"].keepWithNext = True
    styles["Heading1"].spaceBefore = 0
    styles["Heading1"].spaceAfter = 5

    styles["Heading2"].fontName = FONT_BODY_BOLD
    styles["Heading2"].fontSize = 11.8
    styles["Heading2"].leading = 14.8
    styles["Heading2"].textColor = to_color(primary_hex)
    styles["Heading2"].keepWithNext = True
    styles["Heading2"].spaceBefore = 9
    styles["Heading2"].spaceAfter = 3

    styles["Heading3"].fontName = FONT_BODY_BOLD
    styles["Heading3"].fontSize = 9.8
    styles["Heading3"].leading = 12.5
    styles["Heading3"].textColor = to_color(TEXT_MAIN)
    styles["Heading3"].keepWithNext = True
    styles["Heading3"].spaceBefore = 6
    styles["Heading3"].spaceAfter = 2

    styles["Heading4"].fontName = FONT_BODY_BOLD
    styles["Heading4"].fontSize = 8.8
    styles["Heading4"].leading = 11.2
    styles["Heading4"].textColor = to_color(TEXT_MUTED)
    styles["Heading4"].keepWithNext = True
    styles["Heading4"].spaceBefore = 5
    styles["Heading4"].spaceAfter = 2

    styles["BodyText"].fontName = FONT_BODY
    styles["BodyText"].fontSize = 8.4
    styles["BodyText"].leading = 11.1
    styles["BodyText"].textColor = to_color(TEXT_MAIN)
    styles["BodyText"].spaceAfter = 2.4

    styles.add(ParagraphStyle(
        "ListBullet",
        parent=styles["BodyText"],
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2,
    ))

    styles.add(ParagraphStyle(
        "TableHeader",
        parent=styles["Normal"],
        fontName=FONT_BODY_BOLD,
        fontSize=6.8,
        leading=8.6,
        textColor=white,
    ))

    styles.add(ParagraphStyle(
        "TableCell",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=6.6,
        leading=8.4,
        textColor=to_color(TEXT_MAIN),
    ))

    styles.add(ParagraphStyle(
        "CalloutText",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=8.0,
        leading=10.8,
        textColor=to_color(TEXT_MAIN),
    ))

    styles.add(ParagraphStyle(
        "FigureCaption",
        parent=styles["Normal"],
        fontName=FONT_BODY_ITALIC,
        fontSize=7.4,
        leading=9.8,
        textColor=to_color(TEXT_MUTED),
        alignment=1,
        spaceBefore=2,
        spaceAfter=4,
    ))

    # LCD display and monospaced stack frame text: Terminus LCD font on white paper
    styles.add(ParagraphStyle(
        "CodePreformatted",
        fontName=FONT_DISPLAY,
        fontSize=5.8,
        leading=7.3,
        textColor=to_color(TEXT_MAIN),
    ))

    # Chapter Ordering
    if is_sc32:
        manual_dir = MANUALS_ROOT / "sc32"
        chapter_files = [
            "index.md",
            "01-craftsmanship-hardware.md",
            "02-rpn-stack-dynamics.md",
            "03-algebra-transcendentals.md",
            "04-trig-vectors-polar.md",
            "05-complex-numbers-phasors.md",
            "06-geometry-surface-area.md",
            "07-polynomials-brent-solver.md",
            "08-calculus-romberg-quadrature.md",
            "09-statistics-curve-fitting.md",
            "10-computer-science-bases.md",
            "11-financial-tvm.md",
            "12-function-scatter-plotting.md",
            "13-applied-stem-case-studies.md",
            "14-uil-contest-playbook.md",
            "appendix-a-stack-lift-state-machine.md",
            "appendix-b-error-catalog.md",
            "appendix-c-keycap-directory.md",
            "appendix-d-constants-and-equations.md",
            "appendix-e-annotated-bibliography.md",
        ]
        doc_title = "THINKING IN THE STACK"
    else:
        manual_dir = MANUALS_ROOT / "sc6"
        chapter_files = [
            "index.md",
            "01-hardware-architecture.md",
            "02-rpn-for-young-learners.md",
            "03-counting-place-value.md",
            "04-operations-skip-counting.md",
            "05-fractions-decimals-ratios.md",
            "06-geometry-surface-area.md",
            "07-data-probability-primes.md",
            "08-math-quiz-engine.md",
            "09-applied-stem-labs.md",
            "appendix-a-manipulative-blueprints.md",
            "appendix-b-teacher-lesson-plans.md",
            "appendix-c-formulas-and-conversions.md",
            "appendix-d-keycap-directory.md",
        ]
        doc_title = "FROM BLOCKS TO THE STACK"

    # Assemble Flowables
    story: List[Flowable] = []

    # 1. Build KDP Front Matter (Pages i–iv: Half-Title, Series Frontispiece, Title Page, Copyright/Colophon)
    story.extend(build_kdp_front_matter(is_sc32, styles))

    # 2. Table of Contents (Pages v–vi in lowercase Roman numerals, Two-Pass Auto-Updated with Dot Leaders)
    story.append(ChapterTracker("TABLE OF CONTENTS"))
    story.append(BookmarkFlowable("bm_toc", "Table of Contents", level=0))
    toc_heading = make_paragraph("Table of Contents", styles["Heading1"])
    story.append(toc_heading)
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=1.5, color=to_color(primary_hex), spaceAfter=10))

    toc = TableOfContents()
    toc.dotsMinLevel = 0
    toc_level0 = ParagraphStyle(
        "TOCLevel0",
        parent=styles["Normal"],
        fontName=FONT_BODY_BOLD,
        fontSize=8.4,
        leading=11.2,
        textColor=to_color(primary_hex),
        spaceBefore=4,
        spaceAfter=1,
    )
    toc_level1 = ParagraphStyle(
        "TOCLevel1",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=7.6,
        leading=9.8,
        leftIndent=10,
        textColor=to_color(TEXT_MAIN),
        spaceBefore=1.0,
        spaceAfter=0.5,
    )
    toc_level2 = ParagraphStyle(
        "TOCLevel2",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=7.2,
        leading=9.2,
        leftIndent=18,
        textColor=to_color(TEXT_MUTED),
        spaceBefore=0.8,
        spaceAfter=0.5,
    )
    toc.levelStyles = [toc_level0, toc_level1, toc_level2]
    story.append(toc)
    story.append(PageBreak())

    # Ensure Main Text (Arabic Page 1) ALWAYS starts on a Right-Hand (Recto / Odd) Page
    story.append(EnsureRectoPageFlowable())
    story.append(StartArabicPaginationFlowable())

    # 3. Parse and Append Each Chapter (Archival White Paper Interior, Pages 1..N)
    term_counts: Dict[str, int] = {}
    for ch_idx, fname in enumerate(chapter_files):
        fpath = manual_dir / fname
        if not fpath.exists():
            print(f"  [WARN] Missing chapter file: {fpath}")
            continue
        print(f"  -> Processing: {fpath.name}")
        ch_elements = parse_markdown_file(fpath, ch_idx, is_sc32, styles, term_counts)
        story.extend(ch_elements)

    # 4. Alphabetical Subject Index (Two-Pass Auto-Updated A-Z)
    story.append(PageBreak())
    story.append(ChapterTracker("SUBJECT INDEX"))
    story.append(BookmarkFlowable("bm_index", "Alphabetical Subject Index", level=0))
    idx_heading = make_paragraph("Alphabetical Subject Index", styles["Heading1"])
    story.append(idx_heading)
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=1.5, color=to_color(primary_hex), spaceAfter=10))

    idx = SimpleIndex(dot=' . ')
    idx_head = ParagraphStyle(
        "IndexAlphaHead",
        parent=styles["Heading2"],
        fontName=FONT_BODY_BOLD,
        fontSize=10.0,
        leading=12.8,
        textColor=to_color(primary_hex),
        spaceBefore=6,
        spaceAfter=2,
        keepWithNext=True,
    )
    idx_entry = ParagraphStyle(
        "IndexEntryStyle",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=7.6,
        leading=10.0,
        textColor=to_color(TEXT_MAIN),
    )
    idx.setup(style=idx_entry, dot=' . ', headers=True)
    idx.textStyle = [idx_head, idx_entry]
    story.append(idx)

    # Document Geometry: 6.00 x 9.00 in (432 x 648 pt) with 0.750 in inside gutter & 0.361 in outside margin
    doc = ManualDocTemplate(
        str(output_pdf_path),
        pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
        leftMargin=MARGIN_PT,
        rightMargin=MARGIN_PT,
        topMargin=MARGIN_PT,
        bottomMargin=MARGIN_PT
    )

    # Custom canvas maker configuring NumberedCanvas properties
    def custom_canvas_maker(*args, **kwargs):
        c = NumberedCanvas(*args, **kwargs)
        c.doc_title = doc_title
        c.primary_hex = primary_hex
        c.cover_bg_hex = cover_bg_hex
        c.cover_accent_hex = cover_accent_hex
        c.doc_code = doc_code
        c.is_sc32 = is_sc32
        return c

    print("  Building PDF document with multiBuild (two-pass TOC and Subject Index)...")
    passes = doc.multiBuild(story, canvasmaker=custom_canvas_maker, maxPasses=6)
    print(f"  ✓ MultiBuild converged in {passes} passes.")
    print(f"  ✓ Successfully compiled: {output_pdf_path} ({output_pdf_path.stat().st_size:,} bytes)")

    return output_pdf_path


def compile_full_wrap_cover_spread(is_sc32: bool) -> Path:
    """
    Generates a standalone KDP-compliant 3-panel 6x9 Full-Wrap Cover + Spine Spread PDF:
    - Left Panel: Back Cover (6.00 x 9.00 in trim)
    - Center Panel: Dynamic KDP White-Paper Spine (actual_pages * 0.002252 in/page @ 444 PPI)
    - Right Panel: Front Cover (6.00 x 9.00 in trim)
    Continuous Warm Archival Paper (#F7F4EB) across Front, Spine, and Back with exact 0.125 in (9.0 pt)
    outer bleed on all 4 edges, KDP-compliant 0.0625 in spine hinge clearance, zero visible crop/fold lines,
    and a vector EAN-13 barcode inside KDP's mandatory 2.00 x 1.20 in white barcode zone.
    """
    import pypdf
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manual_name = "sc32-scientific-manual.pdf" if is_sc32 else "sc6-elementary-manual.pdf"
    manual_path = OUTPUT_DIR / manual_name
    actual_pages = 500 if is_sc32 else 440
    if manual_path.exists():
        try:
            actual_pages = len(pypdf.PdfReader(str(manual_path)).pages)
        except Exception:
            pass

    spread_name = "sc32-full-wrap-cover.pdf" if is_sc32 else "sc6-full-wrap-cover.pdf"
    spread_path = OUTPUT_DIR / spread_name

    bleed = 9.0            # Official KDP 0.125 in (3.2 mm) outer bleed
    panel_w = PAGE_WIDTH   # 432.0 pt (6.00 in trade trim width)
    panel_h = PAGE_HEIGHT  # 648.0 pt (9.00 in trade trim height)
    spine_in = actual_pages * 0.002252  # Official KDP White Paper spine formula
    spine_w = spine_in * 72.0

    total_w = (2.0 * panel_w) + spine_w + (2.0 * bleed)
    total_h = panel_h + (2.0 * bleed)

    paper_cream = "#F7F4EB"
    ink_obsidian = "#0F172A"
    cover_accent = "#FF4F00" if is_sc32 else "#059669"

    c = canvas.Canvas(str(spread_path), pagesize=(total_w, total_h))

    # Panel X coordinates (inside 0.125 in bleed)
    back_x = bleed
    spine_x = bleed + panel_w
    front_x = bleed + panel_w + spine_w
    base_y = bleed

    # 1. LEFT PANEL: Minimalist Bestseller Back Cover (with left/top/bottom 0.125 in bleed)
    draw_bestseller_back_cover(
        c, back_x, base_y, panel_w, panel_h, is_sc32,
        total_pages=actual_pages,
        bleed_l=bleed, bleed_r=0.0, bleed_t=bleed, bleed_b=bleed
    )

    # 2. RIGHT PANEL: Minimalist Bestseller Front Cover (with right/top/bottom 0.125 in bleed)
    draw_bestseller_front_cover(
        c, front_x, base_y, panel_w, panel_h, is_sc32,
        bleed_l=0.0, bleed_r=bleed, bleed_t=bleed, bleed_b=bleed
    )

    # 3. CENTER PANEL: Continuous Warm Archival Paper Spine (with >= 0.0625 in / 4.5 pt safe margin)
    c.saveState()
    c.setFillColor(to_color(paper_cream))
    c.rect(spine_x, 0.0, spine_w, total_h, fill=1, stroke=0)

    spine_cx = spine_x + (spine_w / 2.0)

    # Minimalist geometric accent bar at top of spine
    mark_w = min(spine_w - 18.0, 26.0)
    c.setFillColor(to_color(cover_accent))
    c.roundRect(spine_cx - mark_w * 0.5, base_y + panel_h - 62.0, mark_w, 6.0, 2.0, fill=1, stroke=0)

    # Vertical Rotated Spine Title (Standard US Top-to-Bottom Spine Orientation: -90 deg)
    c.saveState()
    c.translate(spine_cx, base_y + (panel_h * 0.52))
    c.rotate(-90)
    c.setFillColor(to_color(ink_obsidian))
    c.setFont(FONT_BODY_BOLD, 13.5)
    spine_main = (
        "THINKING IN THE STACK"
        if is_sc32 else
        "FROM BLOCKS TO THE STACK"
    )
    c.drawCentredString(0.0, -4.5, spine_main)
    c.restoreState()

    # Bottom Spine Company Imprint ('StackCalc' rotated or horizontal inside safe zone)
    c.saveState()
    c.translate(spine_cx, base_y + 82.0)
    c.rotate(-90)
    c.setFillColor(to_color(cover_accent))
    c.circle(-38.0, 0.0, 2.5, fill=1, stroke=0)
    c.setFillColor(to_color(ink_obsidian))
    c.setFont(FONT_BODY_BOLD, 10.5)
    c.drawCentredString(0.0, -3.5, "StackCalc")
    c.restoreState()

    c.restoreState()

    c.showPage()
    c.save()
    print(
        f"  ✓ Successfully compiled KDP 6x9 Full-Wrap Cover + Spine Spread: {spread_path.name} "
        f"({actual_pages} pp -> spine {spine_in:.3f} in, total {total_w/72.0:.3f} x {total_h/72.0:.3f} in, {spread_path.stat().st_size:,} bytes)"
    )
    return spread_path


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate publication-grade PDFs for StackCalc manuals.")
    parser.add_argument("--sc32-only", action="store_true", help="Compile only the SC-32 Scientific manual.")
    parser.add_argument("--sc6-only", action="store_true", help="Compile only the SC-6 Elementary manual.")
    parser.add_argument("--min-pages", type=int, default=300, help="Minimum required page count (default: 300).")
    args = parser.parse_args()

    build_both = not args.sc32_only and not args.sc6_only

    if build_both or args.sc32_only:
        compile_manual_pdf(is_sc32=True)
        compile_full_wrap_cover_spread(is_sc32=True)

    if build_both or args.sc6_only:
        compile_manual_pdf(is_sc32=False)
        compile_full_wrap_cover_spread(is_sc32=False)

    print("\n=======================================================")
    print("PDF Generation Complete. Validating outputs...")
    print("=======================================================")
    try:
        import pypdf
        for pdf_name in ["sc32-scientific-manual.pdf", "sc6-elementary-manual.pdf"]:
            pdf_path = OUTPUT_DIR / pdf_name
            if not pdf_path.exists():
                continue
            reader = pypdf.PdfReader(str(pdf_path))
            num_pages = len(reader.pages)

            def count_bookmarks(outline_list):
                cnt = 0
                for item in outline_list:
                    if isinstance(item, list):
                        cnt += count_bookmarks(item)
                    else:
                        cnt += 1
                return cnt

            def collect_dest_pages(outline_list):
                pages = []
                for item in outline_list:
                    if isinstance(item, list):
                        pages.extend(collect_dest_pages(item))
                    else:
                        try:
                            pages.append(reader.get_destination_page_number(item))
                        except Exception:
                            pass
                return pages

            dest_pages = set(collect_dest_pages(reader.outline))
            print(f"    Unique bookmark destination pages: {len(dest_pages)}")
            assert len(dest_pages) >= 50, f"Outline bookmarks collapsed to {len(dest_pages)} unique pages (expected >= 50)!"
            assert num_pages >= 300, f"{pdf_name} has only {num_pages} pages (expected >= 300)!"

            for pg_idx, page in enumerate(reader.pages):
                pg_text = page.extract_text() or ""
                assert "RP2350" not in pg_text, f"Found prohibited token RP2350 on page {pg_idx + 1} of {pdf_name}!"
                assert "ST7567A" not in pg_text, f"Found prohibited token ST7567A on page {pg_idx + 1} of {pdf_name}!"
                assert not re.search(r'\bmathbf\b', pg_text), f"Found naked mathbf on page {pg_idx + 1} of {pdf_name}!"
                raw_latex = re.search(r'\\[a-zA-Z]+', pg_text)
                assert not raw_latex, f"Found raw LaTeX backslash command '{raw_latex.group(0)}' on page {pg_idx + 1} of {pdf_name}!"
                test_ident = re.search(r'\b(?:testSC\w*|testComplex\w*|testEuler\w*)\b|\.swift\b', pg_text)
                assert not test_ident, f"Found test/codebase identifier '{test_ident.group(0)}' on page {pg_idx + 1} of {pdf_name}!"
                assert "the automated verification suite" not in pg_text, f"Found leaked phrase 'the automated verification suite' on page {pg_idx + 1} of {pdf_name}!"
                contest_match = re.search(r'\b(UIL|TMSCA|PSIA)\b', pg_text)
                assert not contest_match, f"Found regional contest token '{contest_match.group(0)}' on page {pg_idx + 1} of {pdf_name}!"
            print(f"    ✓ Passed all forensic validation assertions across all {num_pages} pages (>= 300 pp, 0 naked mathbf, 0 raw LaTeX, 0 test identifiers, 0 leaked phrases, 0 contest acronyms)!")
    except Exception as e:
        print(f"  [ERROR] Validation failed: {e}")
        sys.exit(1)

    print("\nAll manuals compiled and validated successfully.")


if __name__ == "__main__":
    main()
