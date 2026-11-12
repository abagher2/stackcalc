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
import reportlab.platypus.paragraph as rl_para


def _install_reportlab_img_wrap_fix() -> None:
    """
    Fixes two upstream ReportLab Paragraph line-wrapping bugs with inline `<img .../>` tags:
      1. `_getFragWords` leaves a trailing space after `<img/>` as a separate 0-width `_HSFrag`
         instead of marking the `<img/>` word itself as space-followed (`_HSFrag`).
      2. `Paragraph.breakLines` only increments the line's word counter `n` when `nText` is
         non-empty (`if nText: n += 1`), so a sequence of inline `<img/>` keycaps keeps `n == 0`
         and `endLine = (newWidth > limWidth and n > 0)` is False—preventing multi-keycap
         cells from wrapping across lines!
    """
    if getattr(rl_para, "_stackcalc_img_wrap_patched", False):
        return
    orig_gfw = rl_para._getFragWords

    def _has_img(word_entry) -> bool:
        return any(getattr(x[0], "_fkind", None) == rl_para._FK_IMG for x in word_entry[1:])

    def _patched_gfw(frags, maxWidth=None):
        words = orig_gfw(frags, maxWidth=maxWidth)
        out = []
        i = 0
        while i < len(words):
            w = words[i]
            if (
                out
                and isinstance(w, rl_para._HSFrag)
                and w[0] == 0.0
                and len(w) == 2
                and w[1][1] == ""
                and _has_img(out[-1])
            ):
                if not isinstance(out[-1], rl_para._HSFrag):
                    out[-1] = rl_para._HSFrag(out[-1])
                i += 1
                continue
            out.append(w)
            i += 1
        # Glue any non-space-separated punctuation/text fragment (like opening `(` or closing `)`, `,`, `:`)
        # directly to its adjacent `<img .../>` word so `(` is never stranded at the end of a line and
        # `)` / `,` / `:` never wraps onto the next line by itself after a keycap.
        merged = []
        for w in out:
            if (
                merged
                and not isinstance(merged[-1], rl_para._HSFrag)
                and (_has_img(merged[-1]) or _has_img(w))
            ):
                prev = merged.pop()
                comb = [prev[0] + w[0]] + list(prev[1:]) + list(w[1:])
                if isinstance(w, rl_para._HSFrag):
                    comb = rl_para._HSFrag(comb)
                merged.append(comb)
            else:
                merged.append(w)
        return merged

    rl_para._getFragWords = _patched_gfw

    import inspect
    src = inspect.getsource(rl_para.Paragraph.breakLines)
    target_line = "if nText: n += 1"
    replacement_line = (
        "if nText or getattr(f, '_fkind', None) == _FK_IMG or "
        "any(getattr(x[0], '_fkind', None) == _FK_IMG for x in w[1:]): n += 1"
    )
    old_hy_guard = "and not hasattr(f,'cbDefn'):"
    new_hy_guard = (
        "and not hasattr(f,'cbDefn') and not any(getattr(x[0],'_fkind',None)==_FK_IMG for x in w[1:]):"
    )
    old_space_block = (
        "                                if wi._fkind==_FK_TEXT:\n"
        "                                    if not wi.text.endswith(' '):\n"
        "                                        wi.text += ' '\n"
        "                                    break"
    )
    new_space_block = (
        "                                if wi._fkind==_FK_IMG:\n"
        "                                    sp = wi.clone(_fkind=_FK_TEXT, text=' ')\n"
        "                                    if hasattr(sp, 'cbDefn'):\n"
        "                                        del sp.cbDefn\n"
        "                                    words.insert(i+2, sp)\n"
        "                                    break\n"
        "                                if wi._fkind==_FK_TEXT:\n"
        "                                    if not wi.text.endswith(' '):\n"
        "                                        wi.text += ' '\n"
        "                                    break"
    )
    if target_line in src:
        patched_src = (
            src.replace(target_line, replacement_line)
            .replace(old_hy_guard, new_hy_guard)
            .replace(old_space_block, new_space_block)
        )
        ns = dict(rl_para.__dict__)
        exec(
            "\n".join(line[4:] for line in patched_src.splitlines()),
            ns,
        )
        rl_para.Paragraph.breakLines = ns["breakLines"]
    rl_para._stackcalc_img_wrap_patched = True


_install_reportlab_img_wrap_fix()

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
BOOK_SERIF_AVAILABLE = False
BOOK_SANS_AVAILABLE = False
MATH_SERIF_AVAILABLE = False
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

    cmu_dir = FONT_DIR if (FONT_DIR / "CMUSerif-Regular.ttf").exists() else (WATCH_CALC_ROOT / "documentation")
    if (cmu_dir / "CMUSerif-Regular.ttf").exists() and (cmu_dir / "CMUSerif-Bold.ttf").exists():
        pdfmetrics.registerFont(TTFont("CMUSerif", str(cmu_dir / "CMUSerif-Regular.ttf")))
        pdfmetrics.registerFont(TTFont("CMUSerif-Bold", str(cmu_dir / "CMUSerif-Bold.ttf")))
        cmu_it = cmu_dir / ("CMUSerif-Italic.ttf" if (cmu_dir / "CMUSerif-Italic.ttf").exists() else "CMUSerif-Regular.ttf")
        cmu_bi = cmu_dir / ("CMUSerif-BoldItalic.ttf" if (cmu_dir / "CMUSerif-BoldItalic.ttf").exists() else "CMUSerif-Bold.ttf")
        pdfmetrics.registerFont(TTFont("CMUSerif-Italic", str(cmu_it)))
        pdfmetrics.registerFont(TTFont("CMUSerif-BoldItalic", str(cmu_bi)))
        pdfmetrics.registerFontFamily(
            "CMUSerif",
            normal="CMUSerif",
            bold="CMUSerif-Bold",
            italic="CMUSerif-Italic",
            boldItalic="CMUSerif-BoldItalic",
        )
        BOOK_SERIF_AVAILABLE = True

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
        if (dejavu_dir / "DejaVuSerif.ttf").exists():
            pdfmetrics.registerFont(TTFont("MathSerif", str(dejavu_dir / "DejaVuSerif.ttf")))
            bold_djs = dejavu_dir / ("DejaVuSerif-Bold.ttf" if (dejavu_dir / "DejaVuSerif-Bold.ttf").exists() else "DejaVuSerif.ttf")
            it_djs = dejavu_dir / ("DejaVuSerif-Italic.ttf" if (dejavu_dir / "DejaVuSerif-Italic.ttf").exists() else "DejaVuSerif.ttf")
            bi_djs = dejavu_dir / ("DejaVuSerif-BoldItalic.ttf" if (dejavu_dir / "DejaVuSerif-BoldItalic.ttf").exists() else "DejaVuSerif-Bold.ttf")
            pdfmetrics.registerFont(TTFont("MathSerif-Bold", str(bold_djs)))
            pdfmetrics.registerFont(TTFont("MathSerif-Italic", str(it_djs)))
            pdfmetrics.registerFont(TTFont("MathSerif-BoldItalic", str(bi_djs)))
            pdfmetrics.registerFontFamily(
                "MathSerif",
                normal="MathSerif",
                bold="MathSerif-Bold",
                italic="MathSerif-Italic",
                boldItalic="MathSerif-BoldItalic",
            )
            MATH_SERIF_AVAILABLE = True
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

FONT_BODY = "CMUSerif" if BOOK_SERIF_AVAILABLE else ("BookSans" if BOOK_SANS_AVAILABLE else "Times-Roman")
FONT_BODY_BOLD = "CMUSerif-Bold" if BOOK_SERIF_AVAILABLE else ("BookSans-Bold" if BOOK_SANS_AVAILABLE else "Times-Bold")
FONT_BODY_ITALIC = "CMUSerif-Italic" if BOOK_SERIF_AVAILABLE else ("BookSans-Italic" if BOOK_SANS_AVAILABLE else "Times-Italic")
FONT_MATH_SERIF = "MathSerif" if MATH_SERIF_AVAILABLE else ("MathSans" if MATH_SANS_AVAILABLE else FONT_BODY)
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

# Volume III Domain Series Palette (Cover & Optional Color Mode)
DOMAINS_COVER_BG = "#111318"     # Sculptural Matte Obsidian
DOMAINS_PRIMARY = "#111827" if BW_PRINT_INTERIOR else "#0369a1"
DOMAINS_ACCENT = "#000000" if BW_PRINT_INTERIOR else "#0284C7"
DOMAINS_COVER_ACCENT = "#0284C7" # Deep Industrial Cobalt Accent

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
MARGIN_PT = 42.0                 # 0.583 in base margin (shifted +/- 12pt -> 0.750 in gutter / 0.417 in outside)
PAGE_WIDTH = 432.0               # 6.00 in trade trim width
PAGE_HEIGHT = 648.0              # 9.00 in trade trim height
PRINTABLE_WIDTH = PAGE_WIDTH - (2 * MARGIN_PT)  # 348.0 pt (4.833 in)


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
        self.keepWithNext = True

    def draw(self):
        if self.level == 0:
            self.canv.is_chapter_opener_page = True
        if hasattr(self.canv, "_outline_entries"):
            clean_t = " ".join(str(self.title).replace("\t", " ").split())
            if clean_t:
                self.canv._outline_entries.append([int(self.level), int(self.canv.getPageNumber() - 1), clean_t])


class ChapterTracker(Flowable):
    """Tracks the active chapter title on the canvas for running headers."""
    def __init__(self, chapter_title: str):
        super().__init__()
        self.chapter_title = chapter_title
        self.width = 0
        self.height = 0
        self.keepWithNext = True

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
    Two-pass publication document template that intercepts flowables,
    implements a LaTeX-style [ht] float engine for tables, figures, and callouts
    (keeping tables intact while flowing subsequent prose into the bottom of the page),
    and notifies TableOfContents and SimpleIndex with exact Arabic page numbers
    synchronized with the printed page footers.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arabic_start_page = 9

    def build(self, flowables, *args, **kwargs):
        for fl in flowables:
            if hasattr(fl, "_float_bypass_count"):
                fl._float_bypass_count = 0
        super().build(flowables, *args, **kwargs)

    def filterFlowables(self, flowables):
        # Preserve strict sequential reading order so headings and post-table paragraphs
        # are never pulled out of order above the tables or figures they discuss.
        return
        frame = getattr(self, "frame", None)
        if not flowables or frame is None or getattr(frame, "_atTop", 1):
            return
        f0 = flowables[0]
        if f0 is None or not getattr(f0, "_is_latex_float", False):
            return

        bypass_cnt = getattr(f0, "_float_bypass_count", 0)
        if bypass_cnt >= 6:
            return

        aW = self.frame._getAvailableWidth()
        max_frame_h = self.frame._aH
        rem_h = self.frame._y - self.frame._y1p
        if rem_h < 24.0:
            return

        s_f = f0.getSpaceBefore()
        if self.frame._oASpace:
            s_f = max(s_f - self.frame._prevASpace, 0)
        try:
            _, h_f = f0.wrap(aW, max_frame_h)
        except Exception:
            return

        # [h] Here: If the float fits in the remaining space on the current page, place it in position.
        if (h_f + s_f) <= rem_h:
            return

        # If the table/block is taller than a single page (> 92% of frame height), let ReportLab split it across pages.
        if h_f > (max_frame_h * 0.92):
            return

        # [t] Top-of-next-page Float: f0 does not fit in rem_h, but WILL fit intact on the next page.
        # Scan ahead within the current section for prose paragraphs or subsections that can flow into rem_h.
        max_scan = min(len(flowables), 12)
        idx = 1
        while idx < max_scan:
            cand = flowables[idx]
            # Hard barriers: never float a table/figure past a PageBreak or an H1/H2 section boundary
            if isinstance(
                cand,
                (
                    PageBreak,
                    ChapterTracker,
                    EnsureRectoPageFlowable,
                    StartArabicPaginationFlowable,
                    TableOfContents,
                    SimpleIndex,
                ),
            ):
                break
            if isinstance(cand, Paragraph):
                st_name = getattr(getattr(cand, "style", None), "name", "")
                if st_name in ("Heading1", "Heading2"):
                    break

                # Case A: Subheading (Heading3 / Heading4) followed by a BodyText / ListBullet paragraph
                if st_name in ("Heading3", "Heading4"):
                    if rem_h < 46.0 or (idx + 1) >= len(flowables):
                        break
                    nxt = flowables[idx + 1]
                    if not isinstance(nxt, Paragraph) or getattr(getattr(nxt, "style", None), "name", "") not in ("BodyText", "ListBullet"):
                        break
                    s_h = cand.getSpaceBefore()
                    if self.frame._oASpace:
                        s_h = max(s_h - self.frame._prevASpace, 0)
                    _, h_h = cand.wrap(aW, max_frame_h)
                    avail_for_nxt = rem_h - (s_h + h_h + cand.getSpaceAfter() + nxt.getSpaceBefore())
                    if avail_for_nxt < 22.0:
                        break
                    _, h_nxt = nxt.wrap(aW, max_frame_h)
                    has_bm = idx > 1 and isinstance(flowables[idx - 1], BookmarkFlowable)
                    if h_nxt <= avail_for_nxt:
                        pulled = []
                        if has_bm:
                            pulled.append(flowables.pop(idx - 1))
                            idx -= 1
                        h_el = flowables.pop(idx)
                        p_el = flowables.pop(idx)
                        p_el.__dict__["keepWithNext"] = False
                        pulled.extend([h_el, p_el])
                        f0._float_bypass_count = bypass_cnt + 1
                        flowables[0:0] = pulled
                        return
                    else:
                        parts = nxt.split(aW, avail_for_nxt)
                        if len(parts) == 2:
                            _, h_p0 = parts[0].wrap(aW, max_frame_h)
                            if 18.0 <= h_p0 <= avail_for_nxt:
                                if hasattr(nxt, "_index_terms"):
                                    parts[0]._index_terms = nxt._index_terms
                                parts[0].__dict__["keepWithNext"] = False
                                flowables[idx + 1] = parts[1]
                                pulled = []
                                if has_bm:
                                    pulled.append(flowables.pop(idx - 1))
                                    idx -= 1
                                h_el = flowables.pop(idx)
                                pulled.extend([h_el, parts[0]])
                                f0._float_bypass_count = bypass_cnt + 1
                                flowables[0:0] = pulled
                                return
                    break

                # Case B: Regular BodyText or ListBullet paragraph
                if st_name in ("BodyText", "ListBullet"):
                    raw_vis = re.sub(r"<[^>]+>", "", getattr(cand, "text", "")).strip()
                    if raw_vis.endswith(":") and len(raw_vis) < 95:
                        idx += 1
                        continue
                    s_c = cand.getSpaceBefore()
                    if self.frame._oASpace:
                        s_c = max(s_c - self.frame._prevASpace, 0)
                    _, h_c = cand.wrap(aW, max_frame_h)
                    if (h_c + s_c) <= rem_h:
                        p_el = flowables.pop(idx)
                        p_el.__dict__["keepWithNext"] = False
                        f0._float_bypass_count = bypass_cnt + 1
                        flowables.insert(0, p_el)
                        return
                    elif (rem_h - s_c) >= 22.0:
                        parts = cand.split(aW, rem_h - s_c)
                        if len(parts) == 2:
                            _, h_p0 = parts[0].wrap(aW, max_frame_h)
                            if 18.0 <= h_p0 <= (rem_h - s_c):
                                if hasattr(cand, "_index_terms"):
                                    parts[0]._index_terms = cand._index_terms
                                parts[0].__dict__["keepWithNext"] = False
                                flowables[idx] = parts[1]
                                f0._float_bypass_count = bypass_cnt + 1
                                flowables.insert(0, parts[0])
                                return
                    idx += 1
                    continue

            idx += 1

    def afterFlowable(self, flowable):
        super().afterFlowable(flowable)
        if isinstance(flowable, StartArabicPaginationFlowable):
            self.arabic_start_page = self.page
        arabic_pg = max(1, self.page - getattr(self, "arabic_start_page", 7) + 1)
        items_to_check = [flowable]
        if isinstance(flowable, KeepTogether):
            items_to_check.extend(getattr(flowable, "_content", []))
        for sub_f in items_to_check:
            if hasattr(sub_f, '_toc_info'):
                level, text, _key = sub_f._toc_info
                # Pass a 3-tuple (level, text, pageNum) without key so ReportLab does NOT emit
                # interactive /Subtype /Link /Annots on TOC pages (which KDP flags as non-printable markup).
                self.notify('TOCEntry', (level, _protect_special_unicode_glyphs(text), arabic_pg))
            if hasattr(sub_f, '_index_terms'):
                for term in sub_f._index_terms:
                    self.notify('IndexEntry', (_protect_special_unicode_glyphs(term), arabic_pg))


# ---------------------------------------------------------------------------
# Two-Pass NumberedCanvas for KDP Interior Manuscript (Mirrored Gutter & Folios)
# ---------------------------------------------------------------------------
KDP_GUTTER_SHIFT_PT = 12.0  # Shifts 42pt base margin to 54pt (0.750 in) Inside Gutter & 30pt (0.417 in) Outside Margin

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
        self._outline_entries = []

    def showPage(self):
        state = dict(self.__dict__)
        state["page_chapter_title"] = getattr(self, "current_chapter_title", "")
        state["page_is_opener"] = getattr(self, "is_chapter_opener_page", False)
        self._saved_page_states.append(state)
        self.is_chapter_opener_page = False
        self._startPage()

    def save(self):
        recorded_outline = list(getattr(self, "_outline_entries", []))
        # Determine where Arabic Page 1 begins across saved page states
        arabic_start = 7
        for st in self._saved_page_states:
            if "arabic_start_raw_page" in st and st["arabic_start_raw_page"] != 7:
                arabic_start = st["arabic_start_raw_page"]
                break
        for idx_s, st in enumerate(self._saved_page_states):
            ch_t = st.get("page_chapter_title", "")
            if ch_t not in (
                "HALF TITLE",
                "SERIES FRONTISPIECE",
                "TITLE PAGE",
                "COPYRIGHT AND COLOPHON",
                "DEDICATION AND EPIGRAPH",
                "ARCHITECTURAL FRONTISPIECE",
                "TABLE OF CONTENTS",
                "BLANK_PAGE",
            ):
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
        try:
            fn = getattr(self, "_filename", None)
            if recorded_outline and isinstance(fn, (str, Path)) and not str(fn).startswith("<"):
                import json
                sidecar = Path(str(fn)).with_suffix(".outline.json")
                sidecar.write_text(json.dumps(recorded_outline, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception:
            pass

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
        if chapter_title in (
            "HALF TITLE",
            "SERIES FRONTISPIECE",
            "TITLE PAGE",
            "DEDICATION AND EPIGRAPH",
            "ARCHITECTURAL FRONTISPIECE",
            "BLANK_PAGE",
        ):
            return

        self.saveState()
        w, h = PAGE_WIDTH, PAGE_HEIGHT
        left_x = MARGIN_PT + gutter_shift
        right_x = (w - MARGIN_PT) + gutter_shift
        is_odd = (self._pageNumber % 2 == 1)
        is_front_matter = (self._pageNumber < arabic_start) or (
            chapter_title in ("COPYRIGHT AND COLOPHON", "DEDICATION AND EPIGRAPH", "ARCHITECTURAL FRONTISPIECE", "TABLE OF CONTENTS")
        )

        # 1. Top Running Header (Suppressed across all pages so Kindle & Print Replica conversions have zero running header artifacts)
        show_header = False
        if show_header:
            self.setStrokeColor(to_color(DIVIDER_HEX))
            self.setLineWidth(0.45)
            self.line(left_x, h - 29, right_x, h - 29)

            doc_hdr = "THINKING IN THE STACK" if getattr(self, "is_sc32", True) else "FROM BLOCKS TO THE STACK"
            max_title_w = (right_x - left_x) - self.stringWidth(doc_hdr, FONT_BODY_BOLD, 6.8) - 8.0
            disp_title = chapter_title or ""
            if disp_title.startswith("Prologue:") and self.stringWidth(disp_title, FONT_BODY_BOLD, 6.8) > max_title_w:
                disp_title = "Prologue: The Inside-Out Mind"
            if disp_title and self.stringWidth(disp_title, FONT_BODY_BOLD, 6.8) > max_title_w and disp_title.count(":") >= 2:
                disp_title = ":".join(disp_title.split(":")[:2]).strip()
            if disp_title and self.stringWidth(disp_title, FONT_BODY_BOLD, 6.8) > max_title_w and " & " in disp_title:
                disp_title = disp_title.split(" & ")[0].strip()
                if ", " in disp_title and " & " not in disp_title:
                    disp_title = disp_title.replace(", ", " & ", 1)
            if disp_title and self.stringWidth(disp_title, FONT_BODY_BOLD, 6.8) > max_title_w and ", " in disp_title:
                disp_title = disp_title.split(", ")[0].strip()
            if disp_title and self.stringWidth(disp_title, FONT_BODY_BOLD, 6.8) > max_title_w:
                while disp_title and self.stringWidth(disp_title + "...", FONT_BODY_BOLD, 6.8) > max_title_w:
                    disp_title = disp_title[:-1].rstrip()
                disp_title = disp_title + "..."

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
    (r"\uparrow", "↑"),
    (r"\downarrow", "↓"),
    (r"\Uparrow", "⇑"),
    (r"\Downarrow", "⇓"),
    (r"\implies", "⇒"),
    (r"\iff", "⇔"),
    (r"\parallel", "∥"),
    (r"\perp", "⊥"),
    (r"\notin", "∉"),
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
    (r"\odot", "☉"),
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
    (r"\ell", "ℓ"),
    (r"\hbar", "ℏ"),
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


def _is_paren_wrapped(s: str) -> bool:
    s = s.strip()
    if len(s) < 2 or s[0] != "(" or s[-1] != ")":
        return False
    depth = 0
    for idx, ch in enumerate(s):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0 and idx < len(s) - 1:
                return False
    return depth == 0


def _has_top_level_frac_op(s: str, include_mul: bool = False) -> bool:
    s = s.strip()
    depth = 0
    i = 0
    while i < len(s):
        ch = s[i]
        if ch in "{([":
            depth += 1
        elif ch in "})]":
            depth = max(0, depth - 1)
        elif depth == 0:
            if ch == "+" or (ch == "-" and i > 0 and s[i - 1] not in "^_({["):
                return True
            if s[i:].startswith(r"\pm") or s[i:].startswith(r"\mp") or s[i:].startswith(r"\div") or ch in "÷/":
                return True
            if include_mul and (s[i:].startswith(r"\times") or s[i:].startswith(r"\cdot") or ch in "×·"):
                return True
        i += 1
    return False


def replace_latex_frac(text: str) -> str:
    """Recursively replaces \\frac{num}{den} and \\binom{n}{k} handling nested braces."""
    for cmd, fmt in [(r"\dfrac", "frac"), (r"\tfrac", "frac"), (r"\cfrac", "frac"), (r"\frac", "frac"), (r"\binom", "binom")]:
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
            elif re.match(r'^\d+$', num.strip()) and re.match(r'^\d+$', den.strip()):
                if idx > 0 and text[idx - 1].isalpha():
                    text = text[:idx] + f"({num.strip()}/{den.strip()})" + text[j:]
                else:
                    lead_sp = " " if (idx > 0 and text[idx - 1].isdigit()) else ""
                    rest = text[j:].lstrip()
                    if rest and (rest[0].isalpha() or rest[0] == "\\"):
                        text = text[:idx] + f"{lead_sp}({num.strip()}/{den.strip()})" + text[j:]
                    else:
                        trail_sp = " " if (j < len(text) and text[j].isdigit()) else ""
                        text = text[:idx] + f"{lead_sp}{num.strip()}/{den.strip()}{trail_sp}" + text[j:]
            else:
                num_clean = num.strip()
                den_clean = den.strip()
                num_wrapped = not _is_paren_wrapped(num_clean) and _has_top_level_frac_op(num_clean, include_mul=False)
                den_wrapped = not _is_paren_wrapped(den_clean) and _has_top_level_frac_op(den_clean, include_mul=True)
                num_s = f"({num_clean})" if num_wrapped else num_clean
                den_s = f"({den_clean})" if den_wrapped else den_clean
                before = text[:idx].rstrip()
                after = text[j:].lstrip()
                already_enclosed = before.endswith("(") and after.startswith(")")
                needs_outer = (
                    (idx > 0 and text[idx - 1].isalpha())
                    or before.endswith(("/", "^"))
                    or (
                        bool(after)
                        and (after[0].isalnum() or after[0] in "([\\")
                        and not re.match(
                            r'^\\(?:text|mathrm|longrightarrow|to|approx|le|ge|leq|geq|ne|neq|pm|mp|times|cdot|quad|;|,)\b',
                            after,
                        )
                    )
                )
                is_compact = (
                    not num_wrapped
                    and not den_wrapped
                    and len(num_s) <= 10
                    and len(den_s) <= 10
                    and " " not in num_s
                    and " " not in den_s
                )
                sep = "/" if is_compact else " / "
                core = f"{num_s}{sep}{den_s}"
                if already_enclosed:
                    text = text[:idx] + core + text[j:]
                elif needs_outer:
                    text = text[:idx] + f"({core})" + text[j:]
                else:
                    text = text[:idx] + core + text[j:]
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
        prefix = f"^{{{root_deg}}}√" if root_deg else "√"
        if re.match(r'^[A-Za-z0-9\\]+$', rad_clean) or _is_paren_wrapped(rad_clean):
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
    has_leading_latex_space = bool(re.match(r'^\s*(?:\\[,;!: ]|\\quad\b|\\qquad\b|\\(?:text|mathrm)\{\s+)', text))
    has_trailing_latex_space = bool(re.search(r'(?:\\[,;!: ]|\\quad\b|\\qquad\b|\\(?:text|mathrm)\{[^{}]*\s+\})\s*$', text))
    # Strip backticks inside math spans
    text = re.sub(r'`\[([^`]+)\]`', r'[\1]', text)
    text = text.replace('`', '')

    # Handle \begin{...} / \end{...} environments (aligned, cases, pmatrix, bmatrix) and \\ BEFORE r"\ "
    if r"\begin{" in text:
        text = re.sub(r'\s*&\s*=', ' = ', text)
        text = re.sub(r'\s*&\s*', ', ', text)
    text = re.sub(r'\\begin\{bmatrix\}', '[', text)
    text = re.sub(r'\\end\{bmatrix\}', ']', text)
    text = re.sub(r'\\begin\{pmatrix\}', '(', text)
    text = re.sub(r'\\end\{pmatrix\}', ')', text)
    text = re.sub(r'\\begin\{[^}]*\}(?:\{[lcr|]+\})?', '', text)
    text = re.sub(r'\\end\{[^}]*\}', '', text)
    text = text.replace(r"\hline", "")
    text = text.replace(r"\\", "; ")

    # Unescape LaTeX literal escapes before XML escaping (keep \_ protected until after subscript parsing)
    text = text.replace(r"\%", "%").replace(r"\$", "$").replace("QQPH0QQ", "$").replace("QQPH1QQ", "%").replace(r"\_", "\x00ESC_US\x00").replace(r"\&", "&")
    text = text.replace(r"\{", "(").replace(r"\}", ")")
    text = text.replace(r"\ ", " ")

    # Escape XML special characters FIRST so < and > in inequalities never corrupt ReportLab tags
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    # 1. Strip \left, \right, and \big/\Big/\bigg/\Bigg delimiters FIRST so \le does not corrupt \left to ≤ft
    text = re.sub(r'\\left\s*([(\[{|.])', r'\1', text)
    text = re.sub(r'\\right\s*([)\]}|.])', r'\1', text)
    text = re.sub(r'\\left\b', '', text)
    text = re.sub(r'\\right\b', '', text)
    text = re.sub(r'\\[bB]igg?[lr]?\b\s*', '', text)
    text = re.sub(r'\\cancel\{([^{}]*)\}', r'\1', text)
    text = re.sub(r'\\underbrace\{((?:[^{}]|\{[^{}]*\})*)\}_\{((?:[^{}]|\{[^{}]*\})*)\}', r'\1 (\2)', text)

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
    text = re.sub(r'\\phantom\{[^{}]*\}', 'x', text)
    text = replace_latex_frac(text)
    text = re.sub(r'\\underbrace\{((?:[^{}]|\{[^{}]*\})*)\}_\{((?:[^{}]|\{[^{}]*\})*)\}', r'\1 (\2)', text)
    text = re.sub(r'\\overset\{((?:[^{}]|\{[^{}]*\})*)\}\{((?:[^{}]|\{[^{}]*\})*)\}', r'\2(\1)', text)
    text = re.sub(r'\\underset\{((?:[^{}]|\{[^{}]*\})*)\}\{((?:[^{}]|\{[^{}]*\})*)\}', r'\2(\1)', text)
    text = re.sub(r'\\xrightarrow\[([^\]]*)\]\{([^{}]*)\}', r'→[\2; \1]', text)
    text = replace_latex_sqrt(text)
    text = replace_latex_bold(text)

    # 4. Relational operators, arrows, and general symbols BEFORE stripping \text{...}
    # so \text{Pa}\cdot\text{s} never merges into \cdots when \text{s} becomes s.
    text = re.sub(r'\^\s*(?:\{\s*(?:\\circ|°)\s*\}|(?:\\circ|°))', '°', text)
    text = re.sub(r'\\le(?![a-zA-Z])', '≤', text)
    text = re.sub(r'\\ge(?![a-zA-Z])', '≥', text)
    text = re.sub(r'\\leq(?![a-zA-Z])', '≤', text)
    text = re.sub(r'\\geq(?![a-zA-Z])', '≥', text)
    text = re.sub(r'\\ll(?![a-zA-Z])', '≪', text)
    text = re.sub(r'\\ggg(?![a-zA-Z])', '≫', text)
    text = re.sub(r'\\gg(?![a-zA-Z])', '≫', text)
    text = re.sub(r'\\ne(?![a-zA-Z])', '≠', text)
    text = re.sub(r'\\neq(?![a-zA-Z])', '≠', text)
    text = re.sub(r'\\sim(?![a-zA-Z])\s*', '∼ ', text)
    text = re.sub(r'\\in(?![a-zA-Z])', '∈', text)
    text = re.sub(r'\\mid(?![a-zA-Z])', '|', text)
    text = re.sub(r'\\to(?![a-zA-Z])', '→', text)
    text = re.sub(r'\\pm(?![a-zA-Z])', '±', text)
    text = re.sub(r'\\Large(?![a-zA-Z])', '', text)
    text = re.sub(r'\\bmod(?![a-zA-Z])', ' mod ', text)

    text = re.sub(r'\\Delta(?![a-zA-Z])\s*(?=[a-zA-Z0-9\\])', 'Δ', text)
    text = re.sub(r'\\partial(?![a-zA-Z])\s*(?=[a-zA-Z0-9\\])', '∂', text)
    text = re.sub(r'\\nabla(?![a-zA-Z])\s*(?=[a-zA-Z0-9\\])', '∇', text)

    for pat, rep in MATH_REPLACEMENTS:
        if pat[-1].isalpha():
            text = re.sub(re.escape(pat) + r'(?![a-zA-Z])', lambda _, r=rep: r, text)
        else:
            text = text.replace(pat, rep)

    # 5. Handle standard math operators (\sin, \cos, \tan, \ln, \log, \exp, etc.) and upright text macros
    upright_tokens: Dict[str, str] = {}

    def _save_upright(val: str) -> str:
        k = f"\x00UP{len(upright_tokens)}\x00"
        upright_tokens[k] = val
        return k

    _MATH_OP_NAMES = r'(?:arcsin|arccos|arctan|sinh|cosh|tanh|sin|cos|tan|sec|csc|cot|ln|log|exp|det|lim|max|min|gcd|lcm|arg|deg|dim|ker|hom|sup|inf)'
    text = re.sub(rf'(?<=[0-9a-zA-Zα-ωΑ-Ω)\]])\\({_MATH_OP_NAMES})(?![a-zA-Z])', r' \\\1', text)
    text = re.sub(rf'(\\({_MATH_OP_NAMES})(?![a-zA-Z])(?:\s*\^(?:\{{[^{{}}]*\}}|[0-9a-zA-Z+-]+))?)\s*(?=[0-9a-zA-Zα-ωΑ-Ω\\])', r'\1 ', text)
    text = re.sub(rf'\\({_MATH_OP_NAMES})(?![a-zA-Z])', lambda m: _save_upright(m.group(1)), text)

    text = re.sub(r'\\underline\{\s*\\hspace\{[^{}]*\}\s*\}', '___', text)
    for _ in range(3):
        text = re.sub(
            r'\\(?:text|mathrm|operatorname|mathtt|texttt)\{([^{}]*)\}',
            lambda m: _save_upright(m.group(1)),
            text,
        )
        text = re.sub(r'\\(?:mathcal|mathbb|mathbin|mathrel|underline)\{([^{}]*)\}', r'\1', text)
        text = re.sub(r'\\(?:mathbf|textbf|boldsymbol)\{([^{}]*)\}', r'<b>\1</b>', text)
        text = re.sub(r'\\mathit\{([^{}]*)\}', r'<i>\1</i>', text)
        text = re.sub(r'\\(?:bar|overline)\{([^{}]*)\}', r'\1̄', text)
        text = re.sub(r'\\hat\{([^{}]*)\}', r'\1̂', text)
        text = re.sub(r'\\dot\{([^{}]*)\}', r'\1̇', text)
        text = re.sub(r'\\ddot\{([^{}]*)\}', "\\1\u0308", text)
        text = re.sub(r'\\tilde\{([^{}]*)\}', "\\1\u0303", text)
        text = re.sub(r'\\vec\{([^{}]*)\}', r'<b><i>\1</i></b>', text)
        text = re.sub(r'\\pmod\{((?:[^{}]|\{[^{}]*\})*)\}', lambda m: f" ({_save_upright('mod')} {m.group(1)})", text)
        text = re.sub(r'\\pmod\s+([a-zA-Z0-9]+)', lambda m: f" ({_save_upright('mod')} {m.group(1)})", text)
        text = re.sub(r'\\underbrace\{((?:[^{}]|\{[^{}]*\})*)\}_\{((?:[^{}]|\{[^{}]*\})*)\}', r'\1 (\2)', text)
        text = re.sub(r'\\overset\{((?:[^{}]|\{[^{}]*\})*)\}\{((?:[^{}]|\{[^{}]*\})*)\}', r'\2(\1)', text)
        text = re.sub(r'\\underset\{((?:[^{}]|\{[^{}]*\})*)\}\{((?:[^{}]|\{[^{}]*\})*)\}', r'\2(\1)', text)
        text = re.sub(r'\\xrightarrow\[([^\]]*)\]\{([^{}]*)\}', r'→[\2; \1]', text)
        text = re.sub(r'\\xrightarrow\{([^{}]*)\}', r'→[\1]', text)
        text = re.sub(r'\\hspace\{[^{}]*\}', ' ', text)

    # Clean any residual ^° into ° and prime/double-prime in math
    text = text.replace("^°", "°").replace("''", "″").replace("'", "′")

    # 6. Clean empty braces before superscripts/subscripts (e.g., {}^{40}K)
    text = text.replace("{}", "")
    for _ in range(2):
        text = re.sub(r'\^\{([^{}]*)\}', r'<sup>\1</sup>', text)
        text = re.sub(
            r'_\{([^{}]*)\}',
            lambda m: f"<sub>{_save_upright(m.group(1)) if re.match(r'^[a-zA-Z]{3,}$', m.group(1).strip()) else m.group(1)}</sub>",
            text,
        )
    text = re.sub(r'\^([0-9a-zA-Zα-ωΑ-Ω+*′∞∂∇ℓℏ⊕⊙⊖⊗⊥∥-])', r'<sup>\1</sup>', text)
    text = re.sub(r'_([0-9a-zA-Zα-ωΑ-Ω+*′∞∂∇ℓℏ⊕⊙⊖⊗⊥∥-])', r'<sub>\1</sub>', text)
    text = text.replace("\x00ESC_US\x00", "_")

    # Flatten nested and standard <sup>...</sup> or <sub>...</sub> using Unicode superscripts/subscripts
    # so PDF-to-Kindle converters (like Poppler pdftohtml, which ignores PDF Ts Text Rise) preserve exact superscripts/subscripts.
    _SUP_CHARS = "0123456789+-=()nixb"
    _SUP_MAP = str.maketrans(_SUP_CHARS, "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱˣᵇ")
    _SUB_CHARS = "0123456789+-=()aeoxhklmnpst"
    _SUB_MAP = str.maketrans(_SUB_CHARS, "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₕₖₗₘₙₚₛₜ")
    for _ in range(2):
        text = re.sub(
            r'<sup>([^<]*)<sup>([^<]*)</sup>([^<]*)</sup>',
            lambda m: f"<sup>{m.group(1)}{m.group(2).translate(_SUP_MAP)}{m.group(3)}</sup>",
            text,
        )
        text = re.sub(
            r'<sub>([^<]*)<sub>([^<]*)</sub>([^<]*)</sub>',
            lambda m: f"<sub>{m.group(1)}{m.group(2).translate(_SUB_MAP)}{m.group(3)}</sub>",
            text,
        )
    text = re.sub(
        r'<sup>([0123456789+\-=()nixb]+)</sup>',
        lambda m: m.group(1).translate(_SUP_MAP),
        text,
    )
    text = re.sub(
        r'<sub>([0123456789+\-=()aeoxhklmnpst]+)</sub>',
        lambda m: m.group(1).translate(_SUB_MAP),
        text,
    )

    # Strip remaining LaTeX command backslashes and leftover grouping braces
    text = re.sub(r'\\([a-zA-Z]+)', r'\1', text)
    text = text.replace("{", "").replace("}", "")
    text = text.replace("---", "—").replace("--", "–")

    # Italicize mathematical variable letters while preserving HTML tags, XML entities, and upright function names
    _UPRIGHT_WORDS = {"sin", "cos", "tan", "sec", "csc", "cot", "sinh", "cosh", "tanh", "arcsin", "arccos", "arctan", "ln", "log", "exp", "mod", "max", "min", "lim", "det", "gcd", "lcm", "rank", "erf", "erfc", "Si", "Ci", "Re", "Im", "and", "or", "if", "for", "vs"}

    def _italicize_math_vars(m: re.Match) -> str:
        if m.group(1):
            return m.group(1)
        word = m.group(2)
        if word in _UPRIGHT_WORDS:
            return word
        return f"<i>{word}</i>"

    text = re.sub(r'(<[^>]+>|&[a-zA-Z]+;|QQPH\d+QQ|\x00UP\d+\x00|[a-zA-Z][\u0304\u0302\u0307\u0308\u0303])|([a-zA-Z]+)', _italicize_math_vars, text)
    for k_up, v_up in reversed(list(upright_tokens.items())):
        text = text.replace(k_up, v_up)
    text = text.replace("\x00ESC_US\x00", "_")
    text = text.replace("---", "—").replace("--", "–")
    text = re.sub(r'<i>(?:<i>)+', '<i>', text)
    text = re.sub(r'</i>(?:</i>)+', '</i>', text)
    # Use <super rise='4.5' size='6.0'> (+4.5pt so bounding-box top < base top in pdftohtml/KDP) and <sub rise='2.2' size='6.0'> (-2.2pt in ReportLab)
    text = re.sub(r'<sup>(.*?)</sup>', r"<super rise='4.5' size='6.0'>\1</super>", text)
    text = re.sub(r'<sub>(.*?)</sub>', r"<sub rise='2.2' size='6.0'>\1</sub>", text)
    # Keep scientific notation (e.g., 6.6743 × 10^-11) on a single line using non-breaking spaces
    text = re.sub(r'(\d)\s*([×·])\s*(10\b)', "\\1\u00a0\\2\u00a0\\3", text)
    cleaned = text.strip()
    if has_leading_latex_space and cleaned:
        cleaned = " " + cleaned
    if has_trailing_latex_space and cleaned:
        cleaned = cleaned + " "
    return _protect_special_unicode_glyphs(cleaned)


_MATH_SERIF_GLYPH_RE = re.compile(
    r'([^\s<>][\u0304\u0302\u0307\u0308\u0303]|'
    r'[≤≥≠≈≡∞∑∏∫∬∭∂∇↔⇌⇒⇔↑↓⇑⇓∝∠∥⊕∓′″ˣᵇ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱ₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎□●⟨⟩ℏ⌊⌋⌈⌉])'
)

_MATH_SANS_GLYPH_RE = re.compile(
    r'([⊗⊙⊖⊘⊞⊟⊠⊡⊢⊣⊤⊥⊨⊩⊪⊫⊬⊭⊮⊯⊰⊱⊲⊳⊴⊵⊶⊷⊸⊹⊺⊻⊼⊽⊾⊿⋀⋁⋂⋃⋄⋅⋆⋇⋈⋉⋊⋋⋌⋍⋎⋏⋐⋑⋒⋓⋔⋕⋖⋗⋘⋙⋚⋛⋜⋝⋞⋟⋠⋡⋢⋣⋤⋥⋦⋧⋨⋩⋪⋫⋬⋭⋮⋯⋰⋱'
    r'⇐⇑⇓⇕↦↪↩↼⇀↽⇁⇋∀∃∅∈∉∋∌∐∔∕∖∗∘∙∛∜∟∡∢∣∤∦∧∨∮∯∰∱∲∳∴∵∶∷∸∹∺∻∼∽∾∿≀≁≂≃≄≅≆≇≉≊≋≌≍≎≏≐≑≒≓≔≕≖≗≘≙≚≛≜≝≞≟'
    r'≢≣≦≧≨≩≪≫≬≭≮≯≰≱≲≳≴≵≶≷≸≹≺≻≼≽≾≿⊀⊁⊂⊃⊄⊅⊆⊇⊈⊉⊊⊋⊌⊍⊎⊏⊐⊑⊒⊓⊔⟪⟫⟬⟭⟮⟯'
    r'ₐₑₒₓₔₕₖₗₘₙₚₛₜᵥᴺ⇄↰↱ȳℓ─○★✓✗↖↗■☉▸▲▼△])'
)


_ACTIVE_MANUAL_KIND: str = "sc32"


def _protect_special_unicode_glyphs(text: str, in_code: bool = False) -> str:
    """
    Wraps specialized mathematical/calculator Unicode glyphs (≤, ≥, ≠, ≈, ∞, ∑, ∫, ⊕, ⇒, ⇔, ∈, ∇, ∠, ∝, ∥, ⌊, ⌋, etc.)
    that are absent in CMUSerif or SpaceMono with DejaVuSerif (MathSerif) or DejaVuSans (MathSans) so zero tofu boxes (□) ever appear.
    """
    text = text.replace("^°", "°")
    grid_tok = "[TBL]" if _ACTIVE_MANUAL_KIND == "domains" else "[FRAME]"
    text = text.replace("🎲", "[DICE]").replace("🕒", "[CLOCK]").replace("▦", grid_tok).replace("⚡", "[QUIZ]")
    text = text.replace("\u20d7", "").replace("⟌", "/").replace("⬜", "□").replace("🔴", "●").replace("⚪", "○").replace("🟦", "■")
    if in_code and BOOK_SERIF_AVAILABLE:
        text = re.sub(r'([α-ωΑ-Ω])', f"<font face='{FONT_BODY}'>\\1</font>", text)
    if MATH_SERIF_AVAILABLE or MATH_SANS_AVAILABLE:
        text = _MATH_SERIF_GLYPH_RE.sub(f"<font face='{FONT_MATH_SERIF}'>\\1</font>", text)
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
_KEYCAP_CACHE_DIR = Path("/tmp/stackcalc_paper_keycaps_v8")


def _pad_keycap_horiz(im_in: PIL.Image.Image, margin_px: int = 4) -> PIL.Image.Image:
    """Adds clean horizontal breathing room outside the keycap border."""
    padded = PIL.Image.new("RGB", (im_in.width + 2 * margin_px, im_in.height), (255, 255, 255))
    padded.paste(im_in, (margin_px, 0))
    return padded


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
                crop_p = _pad_keycap_horiz(inner, margin_px=4)
            else:
                crop_p = _pad_keycap_horiz(im.crop((x0 - 1, y0 - 1, x1 + 1, y1 + 1)), margin_px=4)
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
                    bcrop = _pad_keycap_horiz(bcrop, margin_px=3)
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
                framed = _pad_keycap_horiz(framed, margin_px=3)
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
    grid_lbl = "TBL" if (is_sc32 or _ACTIVE_MANUAL_KIND == "domains") else "FRAME"
    disp = disp.replace("🎲", "DICE").replace("🕒", "CLOCK").replace("▦", grid_lbl)

    space_mono_bold = FONT_DIR / "SpaceMono-Bold.ttf"
    arial_bold = Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")
    dejavu_bold: Optional[Path] = None
    try:
        import matplotlib
        cand_dj = Path(matplotlib.get_data_path()) / "fonts" / "ttf" / "DejaVuSans-Bold.ttf"
        if cand_dj.exists():
            dejavu_bold = cand_dj
    except Exception:
        pass
    if all(ord(c) < 128 for c in disp) and space_mono_bold.exists():
        font_path = str(space_mono_bold)
    elif "ˣ" in disp and arial_bold.exists():
        font_path = str(arial_bold)
    elif dejavu_bold is not None:
        font_path = str(dejavu_bold)
    elif arial_bold.exists():
        font_path = str(arial_bold)
    else:
        font_path = str(space_mono_bold)
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
    img = _pad_keycap_horiz(img, margin_px=3)

    safe_name = re.sub(r'[^A-Za-z0-9_+-]', lambda m: f"u{ord(m.group(0)):04x}", clean_label)
    f_path = out_dir / f"soft_{safe_name}.png"
    img.save(f_path, format="PNG")
    res = (f_path, img.width, img.height)
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
            if entry.row == 0 or clean_k.upper().startswith("LFU"):
                png_info = _get_fallback_paper_keycap(clean_k, try_sc32)
                layer_kind = "menu"
                break
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

    # 1. Unescape existing HTML entities (CMUSerif and BookSans support Polish Ł/ł natively!)
    text = html.unescape(text)
    if not (BOOK_SERIF_AVAILABLE or BOOK_SANS_AVAILABLE):
        text = text.replace("Ł", "L").replace("ł", "l")

    # Convert inline HTML tags used inside markdown tables/lists to markdown equivalents first
    text = re.sub(r'<code>(.*?)</code>', r'`\1`', text)
    text = re.sub(r'<(?:strong|b)>(.*?)</(?:strong|b)>', r'**\1**', text)
    text = re.sub(r'<(?:em|i)>(.*?)</(?:em|i)>', r'*\1*', text)
    text = re.sub(r'<a\b[^>]*>(.*?)</a>', r'**\1**', text, flags=re.IGNORECASE | re.DOTALL)
    # When <br> follows a colon (e.g., **Title:**<br>Text), a bold heading (**30% fewer keystrokes**<br>Text),
    # or precedes a parenthetical/bullet, use clean punctuation/space rather than a mid-line bullet
    text = re.sub(r'(:\s*(?:\*+)?)\s*<br\s*/?>\s*', r'\1 ', text)
    text = re.sub(r'(\*\*[^*.!?:;\n]+?\*\*)\s*<br\s*/?>\s*', r'\1: ', text)
    text = re.sub(r'\s*<br\s*/?>\s*(?=[•(\[])', ' ', text)
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

    from book_engine import get_registry, get_model_registry
    registry = get_registry(is_sc32)
    alt_registry = get_registry(not is_sc32)

    _DOMAIN_KEYCAP_SET = {
        "ENTER", "ON", "C", "CLEAR", "AC", "<-", "BS", "DICE", "CLOCK", "FRAME", "TBL", "SOLVE", "XEQ",
        "FWD", "INV", "BRG", "WND", "ISA", "TRAV", "trav", "→HR", "→HMS", "POL", "REC",
        "SLOPE", "GRADE%", "PT+", "CLOSURE", "HCRV", "VCRV", "VCV", "3-W", "STA", "LVL", "WIND", "XWIND", "HW", "ALT", "TSD", "TOD", "VS", "TRI", "△",
        "RUN", "RISE", "DIAG", "HIP", "BEND", "VD", "3PH÷", "→mm", "→in", "AWG", "Cᵥ", "PUMP", "RPM", "SFM", "FEED", "TAP", "BOLT", "4-20", "RTD", "M·S", "HYD",
        "HEX", "DEC", "BIN", "OCT", "WSZ", "ENDN", "FLT", "AND", "OR", "XOR", "NOT", "NAND", "NOR",
        "SL", "SR", "ASR", "RL", "RR", "MOD", "ROL", "ROR", "2's", "BSWP", "BSET", "BCLR", "BTST", "MSK", "POP", "CLZ", "2ˣ", "LOG₂", "PWM", "ADC", "BAUD", "τ", "CRC", "CIDR",
        "TC", "+TC", "−TC", "-TC", "FPS", "DOF", "FOV", "EV", "SHUTTER", "CROP", "ASPECT", "EXP", "AUD", "dB⊕", "SPL", "dB", "λ", "vₛ",
        "dBm", "→W", "SWR", "VSWR", "RL", "FSPL", "FSL", "LNK", "EIRP", "SMTH", "NF", "ML", "Γ", "Z₀", "T₀", "c", "kB", "f₀", "fc", "λ/L", "F₁", "Δf", "RADAR", "C/B", "Pₙ",
        "FML", "MW", "Z", "ION", "MOL", "C₁V₁", "M₁V₁", "εbc", "pH", "pKₐ", "BUFF", "BUF", "ABS", "TITR", "10⁻ˣ", "Kₑq", "ΔG", "E°", "Eₐ", "t½", "RCF", "Nₐ", "R", "F",
        "FLR", "FLOUR", "BKR%", "BK%", "ΣW", "DIV", "Tw", "DDT", "ABV", "STRK", "MSH", "OG", "IBU", "SRM", "CO₂", "SO₂", "Aw", "YLD", "CST", "MGN", "MKP",
        "PT", "BSA", "IBW", "AdjW", "CrCl", "GFR", "DOS", "DRP", "IV", "MCG", "GTT", "PED", "AGE", "SEX", "SCR", "W", "H", "PK", "MAP", "BRN", "A-a", "AG", "Ca²⁺", "Na⁺", "QTc", "O₂",
        "N", "I/Y", "I%YR", "PV", "PMT", "FV", "CPK", "Cpk", "AMRT", "NPV", "IRR", "BOND", "BND", "CF", "NormCDF", "InvNorm",
        "pN", "qN", "rN", "pt", "qt", "rt", "pχ²", "qχ²", "rχ²", "pF", "qF", "rF", "pB", "qB", "rB", "z₀", "t₂", "CI", "n*", "ŷ", "ΔD", "%Σ", "Σ+",
        "SHOW", "x²", "yˣ", "√x", "1/x", "+/-", "x⇄y", "R↓", "←", "≪", "≫", "⊕", "x∥y",
    }
    for _dm in ("sc35", "sc14", "sc16", "sc24", "sc50", "sc60", "sc78", "sc80", "sc95"):
        try:
            _dreg = get_model_registry(_dm)
            for _entry in _dreg.entries.values():
                _DOMAIN_KEYCAP_SET.add(_entry.canonical)
        except Exception:
            pass

    def _is_valid_keycap(token: str) -> bool:
        t_clean = token.strip()
        if not t_clean:
            return False
        if t_clean.startswith("▸") and len(t_clean) <= 6:
            return True
        for reg in (registry, alt_registry):
            try:
                reg.resolve(t_clean)
                return True
            except ValueError:
                pass
        return t_clean in _DOMAIN_KEYCAP_SET or t_clean.upper() in _DOMAIN_KEYCAP_SET

    # Handle single-keycap backtick `[KEY]` BEFORE math so `[$]` never collides with $...$
    def sub_backtick_keycap(m):
        k = m.group(1).strip()
        if k and _is_valid_keycap(k):
            return save_placeholder(format_hardware_keycap_cartouche(k, is_sc32, target_h_pt=keycap_h))
        return m.group(0)
    text = re.sub(r'`\[([^`\]\n]+)\]`', sub_backtick_keycap, text)

    _SYM_SEQ_TOKENS = {
        "alpha": f"<font face='{FONT_MATH}'>α</font>",
        "beta": f"<font face='{FONT_MATH}'>β</font>",
        "theta": f"<font face='{FONT_MATH}'>θ</font>",
        "theta1": f"<font face='{FONT_MATH}'>θ</font><sub>1</sub>",
        "phi1": f"<font face='{FONT_MATH}'>φ</font><sub>1</sub>",
        "phi2": f"<font face='{FONT_MATH}'>φ</font><sub>2</sub>",
        "lam": f"<font face='{FONT_MATH}'>λ</font>",
        "lambda": f"<font face='{FONT_MATH}'>λ</font>",
        "lam1": f"<font face='{FONT_MATH}'>λ</font><sub>1</sub>",
        "lam2": f"<font face='{FONT_MATH}'>λ</font><sub>2</sub>",
        "mu": f"<font face='{FONT_MATH}'>μ</font>",
        "omega": f"<font face='{FONT_MATH}'>ω</font>",
        "rho": f"<font face='{FONT_MATH}'>ρ</font>",
        "sigma": f"<font face='{FONT_MATH}'>σ</font>",
        "eps": f"<font face='{FONT_MATH}'>ε</font>",
        "dx": f"<font face='{FONT_MATH}'>Δ</font><i>x</i>",
        "dP": f"<font face='{FONT_MATH}'>Δ</font><i>P</i>",
        "dH": f"<font face='{FONT_MATH}'>Δ</font><i>H</i>",
        "dT1": f"<font face='{FONT_MATH}'>Δ</font><i>T</i><sub>1</sub>",
        "dT2": f"<font face='{FONT_MATH}'>Δ</font><i>T</i><sub>2</sub>",
        "SNR_dB": "<i>SNR</i><sub>dB</sub>",
        "SNR": "<i>SNR</i>",
        "Tinf": f"<i>T</i><sub><font face='{FONT_MATH}'>∞</font></sub>",
        "thalf": "<i>t</i><sub>1/2</sub>",
        "xbar": f"<i>x</i><font face='{FONT_MATH}'>̄</font>",
        "H3O": "[H<sub>3</sub>O<super>+</super>]",
        "pKa": "p<i>K</i><sub>a</sub>",
        "pH": "pH",
        "Abot": "<i>A</i><sub>bot</sub>",
        "Amid": "<i>A</i><sub>mid</sub>",
        "Atop": "<i>A</i><sub>top</sub>",
        "Atot": "<i>A</i><sub>tot</sub>",
        "Vmax": "<i>V</i><sub>max</sub>",
        "Prms": "<i>P</i><sub>rms</sub>",
        "fobj": "<i>f</i><sub>obj</sub>",
        "feye": "<i>f</i><sub>eye</sub>",
        "ncore": "<i>n</i><sub>core</sub>",
        "nclad": "<i>n</i><sub>clad</sub>",
        "PnotA": f"<i>P</i>(<font face='{FONT_MATH}'>¬</font><i>A</i>)",
        "PBnotA": f"<i>P</i>(<i>B</i>|<font face='{FONT_MATH}'>¬</font><i>A</i>)",
        "PBA": "<i>P</i>(<i>B</i>|<i>A</i>)",
        "PA": "<i>P</i>(<i>A</i>)",
        "A1": "<i>A</i><sub>1</sub>", "A2": "<i>A</i><sub>2</sub>",
        "C1": "<i>C</i><sub>1</sub>", "C2": "<i>C</i><sub>2</sub>",
        "E0": "<i>E</i><sub>0</sub>", "Ea": "<i>E</i><sub>a</sub>",
        "I0": "<i>I</i><sub>0</sub>", "IS": "<i>I</i><sub>S</sub>",
        "Km": "<i>K</i><sub>m</sub>", "L0": "<i>L</i><sub>0</sub>", "Lv": "<i>L</i><sub>v</sub>",
        "N0": "<i>N</i><sub>0</sub>", "P1": "<i>P</i><sub>1</sub>", "P2": "<i>P</i><sub>2</sub>",
        "R1": "<i>R</i><sub>1</sub>", "R2": "<i>R</i><sub>2</sub>", "R3": "<i>R</i><sub>3</sub>",
        "Rf": "<i>R</i><sub>f</sub>", "Rg": "<i>R</i><sub>g</sub>", "Rh": "<i>R</i><sub>h</sub>",
        "T0": "<i>T</i><sub>0</sub>", "T1": "<i>T</i><sub>1</sub>", "T2": "<i>T</i><sub>2</sub>",
        "TC": "<i>T</i><sub>C</sub>", "TH": "<i>T</i><sub>H</sub>",
        "V0": "<i>V</i><sub>0</sub>", "VD": "<i>V</i><sub>D</sub>",
        "VDD": "<i>V</i><sub>DD</sub>", "VT": "<i>V</i><sub>T</sub>",
        "b1": "<i>b</i><sub>1</sub>", "b2": "<i>b</i><sub>2</sub>",
        "c1": "<i>c</i><sub>1</sub>", "c2": "<i>c</i><sub>2</sub>",
        "di": "<i>d</i><sub>i</sub>", "do": "<i>d</i><sub>o</sub>",
        "f0": "<i>f</i><sub>0</sub>", "k1": "<i>k</i><sub>1</sub>", "k2": "<i>k</i><sub>2</sub>",
        "m0": "<i>m</i><sub>0</sub>", "m1": "<i>m</i><sub>1</sub>",
        "m2": "<i>m</i><sub>2</sub>", "mf": "<i>m</i><sub>f</sub>",
        "n1": "<i>n</i><sub>1</sub>", "n2": "<i>n</i><sub>2</sub>",
        "rp": "<i>r</i><sub>p</sub>", "v0": "<i>v</i><sub>0</sub>",
        "ve": "<i>v</i><sub>e</sub>", "vi": "<i>v</i><sub>i</sub>", "vs": "<i>v</i><sub>s</sub>",
        "x0": "<i>x</i><sub>0</sub>", "x1": "<i>x</i><sub>1</sub>", "x2": "<i>x</i><sub>2</sub>",
        "y0": "<i>y</i><sub>0</sub>", "y1": "<i>y</i><sub>1</sub>", "y2": "<i>y</i><sub>2</sub>",
        "z1": "<i>z</i><sub>1</sub>", "z2": "<i>z</i><sub>2</sub>",
    }

    # Handle standard inline code `...` BEFORE math (converting any [KEY] inside backticks into Paper keycaps!)
    def sub_code(m):
        raw = m.group(1)
        # Split on [KEY] tokens inside the code span so keystroke sequences render with real Paper keycaps
        parts = re.split(r'(\[[^\]\n]+\])', raw)
        has_keycaps = any(
            pt.startswith("[") and pt.endswith("]") and bool(pt[1:-1].strip()) and _is_valid_keycap(pt[1:-1].strip())
            for pt in parts
        )
        rendered_parts = []
        for pt in parts:
            if not pt:
                continue
            if pt.startswith("[") and pt.endswith("]"):
                inner_k = pt[1:-1].strip()
                if inner_k and _is_valid_keycap(inner_k):
                    rendered_parts.append(format_hardware_keycap_cartouche(inner_k, is_sc32, target_h_pt=keycap_h))
                    continue
                if has_keycaps and inner_k in ("A⁻", "HA"):
                    chem_fmt = f"[A<font face='{FONT_MATH_SERIF}'>⁻</font>]" if inner_k == "A⁻" else "[HA]"
                    rendered_parts.append(f"<font face='{FONT_BODY}' color='{accent_hex}'><b>{chem_fmt}</b></font>")
                    continue
            if has_keycaps:
                sub_tokens = re.split(r'(\s+)', pt)
                sub_out = []
                for st in sub_tokens:
                    if not st:
                        continue
                    if st in _SYM_SEQ_TOKENS:
                        sym_html = _SYM_SEQ_TOKENS[st]
                        sym_html = re.sub(
                            r'<sub>([0123456789+\-=()aeoxhklmnpst]+)</sub>',
                            lambda m_s: _protect_special_unicode_glyphs(m_s.group(1).translate(str.maketrans("0123456789+-=()aeoxhklmnpst", "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₕₖₗₘₙₚₛₜ"))),
                            sym_html,
                        )
                        sym_html = re.sub(
                            r'<super>([0123456789+\-=()nixb]+)</super>',
                            lambda m_s: _protect_special_unicode_glyphs(m_s.group(1).translate(str.maketrans("0123456789+-=()nixb", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱˣᵇ"))),
                            sym_html,
                        )
                        sym_html = sym_html.replace("<sub>", "<sub rise='2.2' size='6.0'>").replace("<super>", "<super rise='4.5' size='6.0'>")
                        sub_out.append(f"<font face='{FONT_BODY}' color='{accent_hex}'><b>{sym_html}</b></font>")
                    else:
                        st_esc = st.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                        st_esc = _protect_special_unicode_glyphs(st_esc, in_code=True)
                        sub_out.append(f"<font face='{FONT_BODY_BOLD}' color='{accent_hex}'><b>{st_esc}</b></font>")
                rendered_parts.append("".join(sub_out))
                continue
            pt_esc = pt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            pt_esc = _protect_special_unicode_glyphs(pt_esc, in_code=True)
            rendered_parts.append(f"<font face='{FONT_BODY_BOLD}' color='{accent_hex}'><b>{pt_esc}</b></font>")
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
        if k.strip() and _is_valid_keycap(k):
            return save_placeholder(format_hardware_keycap_cartouche(k, is_sc32, target_h_pt=keycap_h))
        return m.group(0)
    text = re.sub(r'(?<!\!)\[([^\]\n]{1,12})\](?!\()', sub_bare_keycap, text)

    # 3. Escape remaining XML characters in regular text and protect special Unicode glyphs
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = _protect_special_unicode_glyphs(text)

    # Handle markdown links [text](url) -> <b>text</b>
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'<b>\1</b>', text)

    # 4. Handle markdown bold and italic (supporting nested *italic* inside **bold** and ***bold-italic***)
    text = re.sub(r'\*\*\*((?:(?!\*\*\*).)+)\*\*\*', r'<b><i>\1</i></b>', text)
    text = re.sub(r'\*\*((?:(?!\*\*).)+)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\w)__((?:(?!__).)+)__(?!\w)', r'<b>\1</b>', text)
    text = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', text)
    text = re.sub(r'(?<!\w)_([^_]+)_(?!\w)', r'<i>\1</i>', text)

    # 5. Restore placeholders in reverse order so nested placeholders resolve cleanly
    for key, val in reversed(list(placeholders.items())):
        text = text.replace(key, val)

    # Flatten any nested <i>...<i>...</i>...</i> or <b>...<b>...</b>...</b> tags so ReportLab XML parser never trips
    i_depth = 0
    b_depth = 0

    def _flatten_bi(m: re.Match) -> str:
        nonlocal i_depth, b_depth
        tag = m.group(0)
        if tag == "<i>":
            i_depth += 1
            return "<i>" if i_depth == 1 else ""
        if tag == "</i>":
            if i_depth > 0:
                i_depth -= 1
                return "</i>" if i_depth == 0 else ""
            return ""
        if tag == "<b>":
            b_depth += 1
            return "<b>" if b_depth == 1 else ""
        if tag == "</b>":
            if b_depth > 0:
                b_depth -= 1
                return "</b>" if b_depth == 0 else ""
            return ""
        return tag

    text = re.sub(r'</?[ib]>', _flatten_bi, text)
    if i_depth > 0:
        text += "</i>"
    if b_depth > 0:
        text += "</b>"

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
    if not (BOOK_SERIF_AVAILABLE or BOOK_SANS_AVAILABLE):
        t = t.replace("Ł", "L").replace("ł", "l")
    t = t.replace(r"\$", "QQESCDOLLARQQ").replace(r"\%", "%")
    t = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', t)
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
    t_plain = t.replace("↰", "f").replace("↱", "g").replace("⇄", "↔").replace("∥", "||").replace("▸", "→").replace("△", "TRI")
    t_plain = t_plain.replace("ᵥ", "v").replace("ᴺ", "N")
    grid_plain = "TBL" if (is_sc32 or _ACTIVE_MANUAL_KIND == "domains") else "FRAME"
    t_plain = t_plain.replace("🎲", "DICE").replace("🕒", "CLOCK").replace("▦", grid_plain)
    t_plain = t_plain.replace("⌊", "floor(").replace("⌋", ")").replace("⌈", "ceil(").replace("⌉", ")")
    for k, v in math_ph.items():
        v_plain = re.sub(r'</?[a-zA-Z][^>]*>', '', v)
        v_plain = v_plain.replace("∥", "||").replace("⌊", "floor(").replace("⌋", ")").replace("ᵥ", "v").replace("ᴺ", "N").replace("△", "TRI")
        t_plain = t_plain.replace(k, v_plain)
    plain = html.unescape(re.sub(r'</?[a-zA-Z][^>]*>', '', t_plain)).strip()

    # Styled version for Heading on page (with Paper-theme keycaps and Terminus glyph protection)
    from book_engine import get_registry, get_model_registry
    reg1 = get_registry(is_sc32)
    reg2 = get_registry(not is_sc32)
    _hdr_domain_keys = {
        "FWD", "INV", "BRG", "WND", "ISA", "TRAV", "trav", "→HR", "→HMS", "POL", "REC",
        "SLOPE", "GRADE%", "PT+", "CLOSURE", "HCRV", "VCRV", "VCV", "3-W", "STA", "LVL", "WIND", "XWIND", "HW", "ALT", "TSD", "TOD", "VS", "TRI", "△",
        "RUN", "RISE", "DIAG", "HIP", "BEND", "VD", "TBL", "3PH÷", "→mm", "→in", "AWG", "Cᵥ", "PUMP", "RPM", "SFM", "FEED", "TAP", "BOLT", "4-20", "RTD", "M·S", "HYD",
        "HEX", "DEC", "BIN", "OCT", "WSZ", "ENDN", "FLT", "AND", "OR", "XOR", "NOT", "NAND", "NOR",
        "SL", "SR", "ASR", "RL", "RR", "MOD", "ROL", "ROR", "2's", "BSWP", "BSET", "BCLR", "BTST", "MSK", "POP", "CLZ", "2ˣ", "LOG₂", "PWM", "ADC", "BAUD", "τ", "CRC", "CIDR",
        "TC", "+TC", "−TC", "-TC", "FPS", "DOF", "FOV", "EV", "SHUTTER", "CROP", "ASPECT", "EXP", "AUD", "dB⊕", "SPL", "dB", "λ", "vₛ",
        "dBm", "→W", "SWR", "VSWR", "FSPL", "FSL", "LNK", "EIRP", "SMTH", "NF", "ML", "Γ", "Z₀", "T₀", "c", "kB", "f₀", "fc", "λ/L", "F₁", "Δf", "RADAR", "C/B", "Pₙ",
        "FML", "MW", "Z", "ION", "MOL", "C₁V₁", "M₁V₁", "εbc", "pH", "pKₐ", "BUFF", "BUF", "ABS", "TITR", "10⁻ˣ", "Kₑq", "ΔG", "E°", "Eₐ", "t½", "RCF", "Nₐ", "R", "F",
        "FLR", "FLOUR", "BKR%", "BK%", "ΣW", "DIV", "Tw", "DDT", "ABV", "STRK", "MSH", "OG", "IBU", "SRM", "CO₂", "SO₂", "Aw", "YLD", "CST", "MGN", "MKP",
        "PT", "BSA", "IBW", "AdjW", "CrCl", "GFR", "DOS", "DRP", "IV", "MCG", "GTT", "PED", "AGE", "SEX", "SCR", "PK", "MAP", "BRN", "A-a", "AG", "Ca²⁺", "Na⁺", "QTc", "O₂",
        "N", "I/Y", "I%YR", "PV", "PMT", "FV", "CPK", "Cpk", "AMRT", "NPV", "IRR", "BOND", "BND", "CF", "NormCDF", "InvNorm",
        "pN", "qN", "rN", "pt", "qt", "rt", "pχ²", "qχ²", "rχ²", "pF", "qF", "rF", "pB", "qB", "rB", "z₀", "t₂", "CI", "n*", "ŷ", "ΔD", "%Σ", "Σ+",
        "SOLVE", "XEQ", "≪", "≫", "⊕", "x∥y",
    }
    for _dm in ("sc35", "sc14", "sc16", "sc24", "sc50", "sc60", "sc78", "sc80", "sc95"):
        try:
            _dreg = get_model_registry(_dm)
            for _entry in _dreg.entries.values():
                _hdr_domain_keys.add(_entry.canonical)
        except Exception:
            pass
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
        if (k_tok.startswith("▸") and len(k_tok) <= 6) or k_tok in _hdr_domain_keys:
            ph_k = f"QQHK{len(key_ph)}QQ"
            key_ph[ph_k] = format_hardware_keycap_cartouche(k_tok, is_sc32, target_h_pt=10.0)
            return ph_k
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
    ("36-Bit Word Architecture (IBM 7090 & DEC PDP-10)", [re.compile(r'\b(36-bit|pdp-10|ibm 7090)\b', re.IGNORECASE)]),
    ("4-Level XYZT Operational Stack", [re.compile(r'\b(xyzt stack|4-stack|register [xyzt]|four-shelf|four registers)\b', re.IGNORECASE)]),
    ("43-Key Tactile Matrix Keypad", [re.compile(r'\b(keypad matrix|43-key|tactile keypad|snap-dome)\b', re.IGNORECASE)]),
    ("Abel, Niels Henrik & Évariste Galois (Quintic Insolvability)", [re.compile(r'\b(abel|galois|quintic|degree 5)\b', re.IGNORECASE)]),
    ("AC Phasors, Impedance & Charles Proteus Steinmetz", [re.compile(r'\b(steinmetz|phasor|reactance|impedance)\b', re.IGNORECASE)]),
    ("Adaptive Romberg Quadrature ([∫]) & Werner Romberg", [re.compile(r'\b(romberg|adaptive quadrature|numerical integration)\b', re.IGNORECASE)]),
    ("Al-Khwarizmi & Completing the Square", [re.compile(r'\b(al-khwarizmi|completing the square|al-jabr)\b', re.IGNORECASE)]),
    ("Amortization Schedules & Mortgage Crossover", [re.compile(r'\b(amortization|mortgage|principal and interest)\b', re.IGNORECASE)]),
    ("Anscombe's Quartet & Visual Data Inspection", [re.compile(r'\b(anscombe|quartet|scatter cloud)\b', re.IGNORECASE)]),
    ("Archimedes (Sphere-Cylinder Ratio, Parabola & Buoyancy)", [re.compile(r'\b(archimedes|syracuse|buoyancy|parabola)\b', re.IGNORECASE)]),
    ("Arrhenius Chemical Kinetics & Activation Energy", [re.compile(r'\b(arrhenius|activation energy|rate constant)\b', re.IGNORECASE)]),
    ("Bessel's Correction (Sample Variance Degrees of Freedom n - 1)", [re.compile(r'\b(bessel|n\s*-\s*1|degrees? of freedom)\b', re.IGNORECASE)]),
    ("Binary ([BIN]), Octal ([OCT]), Decimal ([DEC]) & Hexadecimal ([HEX])", [re.compile(r'\b(hexadecimal|octal|binary|nibbles?)\b', re.IGNORECASE)]),
    ("Bitwise Logic, Bitfields & Subnet Masks ([BASE], [÷R])", [re.compile(r'\b(bitwise|subnet mask|boolean|rgb color)\b', re.IGNORECASE)]),
    ("Brent's Hybrid Root-Finding Algorithm ([SOLVE])", [re.compile(r'\b(richard brent|brent\'s|brent solver|inverse quadratic)\b', re.IGNORECASE)]),
    ("Bresenham's Line Algorithm & Affine Pixel Mapping", [re.compile(r'\b(bresenham|affine|pixel grid|viewport)\b', re.IGNORECASE)]),
    ("Carbon-14 Radiometric Dating & Willard Libby", [re.compile(r'\b(carbon-14|radiocarbon|willard libby|half-life)\b', re.IGNORECASE)]),
    ("Cardano, Gerolamo & Tartaglia (1535 Milan Cubic Contest)", [re.compile(r'\b(cardano|tartaglia|ars magna|cubic)\b', re.IGNORECASE)]),
    ("Carnot Heat-Engine Efficiency & Counter-Flow Heat Exchangers", [re.compile(r'\b(sadi carnot|carnot|heat exchanger|lmtd)\b', re.IGNORECASE)]),
    ("Catenary Curve (cosh x), Hanging Chains & Gateway Arch", [re.compile(r'\b(catenary|gateway arch|hanging chain|hyperbolic cosine)\b', re.IGNORECASE)]),
    ("Catastrophic Cancellation & Numerical Stability (William Kahan)", [re.compile(r'\b(catastrophic cancellation|kahan|loss of significance)\b', re.IGNORECASE)]),
    ("Cavalieri's Principle & 3D Solid Mensuration", [re.compile(r'\b(cavalieri|mensuration|frustum|torus)\b', re.IGNORECASE)]),
    ("Center of Mass, Moment of Inertia & Parallel-Axis Theorem", [re.compile(r'\b(center of mass|centroid|moment of inertia|steiner)\b', re.IGNORECASE)]),
    ("Central Difference Derivative & Taylor Error Cancellation", [re.compile(r'\b(central difference|numerical derivative|taylor series)\b', re.IGNORECASE)]),
    ("Claude Shannon & Boolean Switching Circuits (1937 Thesis)", [re.compile(r'\b(claude shannon|shannon|george boole|relay)\b', re.IGNORECASE)]),
    ("Complex Numbers ([CMPLX]) & 90-Degree Rotation (i = √-1)", [re.compile(r'\b(complex numbers?|complex plane|caspar wessel|argand)\b', re.IGNORECASE)]),
    ("Composite Cross-Sections, Parallel-Axis Theorem & Singularity Functions", [re.compile(r'\b(composite cross-section|neutral axis|singularity|macaulay)\b', re.IGNORECASE)]),
    ("Compound Microscopes & Thin-Lens Optics", [re.compile(r'\b(compound microscope|thin-lens|focal length|magnification)\b', re.IGNORECASE)]),
    ("Continued Fractions (Golden Ratio φ & Pi 355/113)", [re.compile(r'\b(continued fractions?|355/113|golden ratio|zu chongzhi)\b', re.IGNORECASE)]),
    ("De Moivre's Theorem & Roots of Unity", [re.compile(r'\b(de moivre|roots of unity)\b', re.IGNORECASE)]),
    ("Descartes, René & the Cartesian Coordinate Plane", [re.compile(r'\b(descartes|cartesian|analytic geometry)\b', re.IGNORECASE)]),
    ("Difference of Two Squares & Mental Multiplication", [re.compile(r'\b(difference of two squares|difference-of-squares|shakuntala devi)\b', re.IGNORECASE)]),
    ("Dijkstra's Shunting-Yard Algorithm & Charles Hamblin", [re.compile(r'\b(dijkstra|shunting-yard|hamblin)\b', re.IGNORECASE)]),
    ("Eratosthenes of Cyrene & Earth's Circumference", [re.compile(r'\b(eratosthenes|syene|alexandria|gnomon)\b', re.IGNORECASE)]),
    ("Error Catalog & Mathematical Singularities", [re.compile(r'\b(div by 0|singularit|domain error|overflow)\b', re.IGNORECASE)]),
    ("Euler's Column Buckling Law (Pcr = π²EI / L²)", [re.compile(r'\b(column buckling|critical buckling|slenderness)\b', re.IGNORECASE)]),
    ("Euler's Identity (eⁱπ + 1 = 0) & Complex Exponential", [re.compile(r'\b(euler\'s identity|feynman)\b', re.IGNORECASE)]),
    ("Euler's Natural Base e ([eˣ], [LN]) & Continuous Growth", [re.compile(r'\b(natural logarithm|natural base|euler\'s number)\b', re.IGNORECASE)]),
    ("Factorials ([x!]), Combinatorics & Lanczos Gamma Approximation", [re.compile(r'\b(factorial|lanczos|gamma function|combinatorics)\b', re.IGNORECASE)]),
    ("Fermi Estimation & Enrico Fermi's Trinity Paper-Drop Test", [re.compile(r'\b(enrico fermi|fermi|back-of-the-envelope|piano tuners)\b', re.IGNORECASE)]),
    ("Fibonacci (Leonardo of Pisa) & Present Value in Liber Abaci", [re.compile(r'\b(fibonacci|leonardo of pisa|liber abaci)\b', re.IGNORECASE)]),
    ("Galileo Galilei & the Square-Cube Scaling Law", [re.compile(r'\b(galileo|square-cube law|two new sciences)\b', re.IGNORECASE)]),
    ("Galton, Sir Francis (Quincunx Bean Machine & Regression to the Mean)", [re.compile(r'\b(galton|quincunx|bean machine|regression to the mean)\b', re.IGNORECASE)]),
    ("Gauss, Carl Friedrich (1801 Ceres Orbit, Least Squares & Bell Curve)", [re.compile(r'\b(ceres|piazzi|least squares|gaussian)\b', re.IGNORECASE)]),
    ("Great-Circle Navigation, Surveying Traverses & Crosswind Vectors", [re.compile(r'\b(great-circle|haversine|crosswind|traverse)\b', re.IGNORECASE)]),
    ("Heron's Triangle Formula & Ramanujan's Ellipse Approximation", [re.compile(r'\b(heron|semi-perimeter|ramanujan)\b', re.IGNORECASE)]),
    ("Horner's Nested Polynomial Scheme & Single-Entry LASTX Spine", [re.compile(r'\b(horner|nested polynomial|companion matrix)\b', re.IGNORECASE)]),
    ("Hyperbolic Functions ([HYP], sinh, cosh, tanh) & Ocean Waves", [re.compile(r'\b(hyperbolic|sinh|cosh|tanh|rapidity)\b', re.IGNORECASE)]),
    ("Inside-Out Thinking vs. Outside-In Paper Notation", [re.compile(r'\b(inside-out|outside-in|typesetters)\b', re.IGNORECASE)]),
    ("Kepler's Orbital Laws & Transcendental Anomaly Equation", [re.compile(r'\b(johannes kepler|kepler\'s|eccentric anomaly)\b', re.IGNORECASE)]),
    ("Keycap [1/x] (Reciprocal)", [re.compile(r'\[1\/x\]')]),
    ("Keycap [CMPLX] (Complex Prefix)", [re.compile(r'\[CMPLX\]', re.IGNORECASE)]),
    ("Keycap [E] (Scientific Exponent Entry)", [re.compile(r'\[E\]')]),
    ("Keycap [ENTER] (Stack Lift & Duplication)", [re.compile(r'\[ENTER\]', re.IGNORECASE)]),
    ("Keycap [HYP] (Hyperbolic Prefix)", [re.compile(r'\[HYP\]', re.IGNORECASE)]),
    ("Keycap [L.R.], [x̄,ȳ] & [s,σ] (Linear Regression & Sample Statistics)", [re.compile(r'\[(m,b|L\.R\.|x̄|sx|x̄w)\]', re.IGNORECASE)]),
    ("Keycap [LASTX] (Argument Recovery & Horner Verification)", [re.compile(r'\[LASTX\]', re.IGNORECASE)]),
    ("Keycap [LN] & [eˣ] (Natural Log & Exponential)", [re.compile(r'\[(LN|e[\^ˣx]+)\]')]),
    ("Keycap [LOG] & [10ˣ] (Common Base-10 Log & Antilog)", [re.compile(r'\[(LOG|10[\^ˣx]+)\]')]),
    ("Keycap [POLY] (Polynomial Root Solver)", [re.compile(r'\[POLY\]', re.IGNORECASE)]),
    ("Keycap [R↓] (Roll Stack Down)", [re.compile(r'\[R[↓\\]+\]')]),
    ("Keycap [SIN], [COS], [TAN] & Inverse Trig", [re.compile(r'\[(A?SIN|A?COS|A?TAN)\]', re.IGNORECASE)]),
    ("Keycap [SOLVE] (Brent Numerical Root Solver)", [re.compile(r'\[SOLVE\]', re.IGNORECASE)]),
    ("Keycap [STO] & [RCL] (Memory Storage & Recall)", [re.compile(r'\[(STO|RCL)\]', re.IGNORECASE)]),
    ("Keycap [x⇄y] (Register X-Y Swap)", [re.compile(r'\[x[⇄↔<->]+y\]', re.IGNORECASE)]),
    ("Keycap [yˣ] & [ˣ√y] (Powers & Roots)", [re.compile(r'\[(y[\^ˣx]+|ˣ√y)\]')]),
    ("Keycap [÷R] (Euclidean Integer Quotient & Remainder)", [re.compile(r'\[÷R\]')]),
    ("Keycap [∫] (Adaptive Romberg Numerical Quadrature)", [re.compile(r'\[∫\]')]),
    ("Keycap [▸θ,r] & [▸y,x] (Polar-Rectangular Vector Conversion)", [re.compile(r'\[(▸θ,r|▸y,x|→POL|→REC)\]')]),
    ("Keycap [x∥y] (Universal Harmonic / Parallel Operator)", [re.compile(r'\[(x?∥y?|\|\|)\]')]),
    ("Keycap [Σ+] (Statistical & Geometric Accumulator)", [re.compile(r'\[[Σ∑]\+\]')]),
    ("Kleiber's 3/4-Power Metabolic Scaling Law", [re.compile(r'\b(kleiber|metabolic|3/4)\b', re.IGNORECASE)]),
    ("Leibniz, Gottfried Wilhelm (Binary Arithmetic & Calculus)", [re.compile(r'\b(leibniz|binary medallion)\b', re.IGNORECASE)]),
    ("Linear Regression, Karl Pearson's Correlation (r) & Linearization", [re.compile(r'\b(karl pearson|correlation coefficient|linear regression|moore\'s law)\b', re.IGNORECASE)]),
    ("Loudspeaker Butterworth Crossovers & Standing-Wave Ratio (VSWR)", [re.compile(r'\b(butterworth|crossover|vswr|standing-wave)\b', re.IGNORECASE)]),
    ("Lukasiewicz, Jan & 1924 Warsaw Parenthesis-Free Logic", [re.compile(r'\b(łukasiewicz|lukasiewicz|warsaw|postfix)\b', re.IGNORECASE)]),
    ("Miller, George A. & Working-Memory Limits (1956 Paper)", [re.compile(r'\b(george a?\.?\s*miller|working memory|magical number seven)\b', re.IGNORECASE)]),
    ("Napier, John & Henry Briggs (1614 Invention of Logarithms)", [re.compile(r'\b(john napier|merchiston|henry briggs|logarithms?)\b', re.IGNORECASE)]),
    ("Net Present Value (NPV), Internal Rate of Return (IRR) & Bonds", [re.compile(r'\b(net present value|internal rate of return|\bnpv\b|\birr\b|bond price)\b', re.IGNORECASE)]),
    ("Newton's Law of Cooling & Thermal Relaxation", [re.compile(r'\b(newton\'s law of cooling|cooling coffee|thermal relaxation)\b', re.IGNORECASE)]),
    ("Normal Bell Curve, Central Limit Theorem & Cumulative Φ(z)", [re.compile(r'\b(central limit theorem|normal distribution|bell curve|cumulative normal)\b', re.IGNORECASE)]),
    ("Percentages ([%], [%CHG]), Multiplicative Asymmetry & Rule of 72", [re.compile(r'\b(rule of 72|percentage asymmetry|multiplicative asymmetry|percent change)\b', re.IGNORECASE)]),
    ("Quartz Crystal Oscillator (32,768 Hz = 2¹⁵ Hz) & Reflective LCD", [re.compile(r'\b(32,768|quartz|reflective|transflective)\b', re.IGNORECASE)]),
    ("Relativistic Time Dilation (Cosmic-Ray Muons & Lorentz Factor γ)", [re.compile(r'\b(lorentz factor|time dilation|muons?)\b', re.IGNORECASE)]),
    ("Reynolds Number, Pipe Turbulence & Venturi Pressure Drop", [re.compile(r'\b(osborne reynolds|reynolds number|laminar|venturi)\b', re.IGNORECASE)]),
    ("Richardson Extrapolation (4/3 - 1/3 Error Cancellation)", [re.compile(r'\b(lewis fry richardson|richardson extrapolation|4/3)\b', re.IGNORECASE)]),
    ("Root-Sum-Square (RSS) Mechanical Tolerance Stacking", [re.compile(r'\b(root-sum-square|tolerance stacking)\b', re.IGNORECASE)]),
    ("Sabine's Reverberation Law (Boston Symphony Hall) & Acoustics", [re.compile(r'\b(wallace.*sabine|sabine|reverberation|symphony hall)\b', re.IGNORECASE)]),
    ("Hewlett, Bill, Dave Packard & the HP-35 / HP-32SII RPN Lineage", [re.compile(r'\b(hewlett|packard|hp-35|hp-15c|hp-32sii|osborne|cochran|slide rule)\b', re.IGNORECASE)]),
    ("Stack Lift State Machine & Register T Replication", [re.compile(r'\b(stack lift|t-replication|t replication|conveyor belt)\b', re.IGNORECASE)]),
    ("Student's t-Distribution & William Sealy Gosset (Guinness Brewery)", [re.compile(r'\b(gosset|guinness|student\'s t)\b', re.IGNORECASE)]),
    ("Time Value of Money ([TVM]: [N], [I%], [PV], [PMT], [FV])", [re.compile(r'\b(time value of money|cash-flow sign|present value|future value)\b', re.IGNORECASE)]),
    ("Tsiolkovsky Rocket Equation, Saturn V & Clarke Geostationary Orbit", [re.compile(r'\b(tsiolkovsky|saturn v|geostationary|arthur c\. clarke)\b', re.IGNORECASE)]),
    ("Two's Complement Negative Numbers & Odometer Arithmetic", [re.compile(r'\b(two\'s complement|odometer|sign bit)\b', re.IGNORECASE)]),
    ("Unit Circle, Planar Triangulation & Law of Cosines", [re.compile(r'\b(unit circle|triangulation|law of cosines)\b', re.IGNORECASE)]),
    ("Van der Waals Real Gas Cubic & 3D Principal Stress Eigenvalues", [re.compile(r'\b(van der waals|molar volume|principal stress)\b', re.IGNORECASE)]),
    ("Viète's Nested Square-Root Cascade", [re.compile(r'\b(viète|viete|nested radical|radical pyramid)\b', re.IGNORECASE)]),
    ("Weber-Fechner Law (Decibels, Richter Scale, Stellar Magnitudes & pH)", [re.compile(r'\b(weber-fechner|decibels?|richter|stellar magnitude)\b', re.IGNORECASE)]),
    ("Weibull Reliability Distribution & Poisson Rare Events", [re.compile(r'\b(weibull|poisson)\b', re.IGNORECASE)]),
]

INDEX_CATALOG_SC6 = [
    ("Absolute Value & Distance from Zero ([|x|])", [re.compile(r'\b(absolute value|distance from zero)\b', re.IGNORECASE)]),
    ("Ada Lovelace & Charles Babbage (Analytical Engine)", [re.compile(r'\b(ada lovelace|babbage|analytical engine)\b', re.IGNORECASE)]),
    ("Addition & Make-a-Ten Strategy", [re.compile(r'\b(make-a-ten|making a ten|friends of ten|bridging across ten)\b', re.IGNORECASE)]),
    ("Ahmes & Ancient Egyptian Multiplication", [re.compile(r'\b(ahmes|rhind|rope-stretchers|harpedonaptai)\b', re.IGNORECASE)]),
    ("Al-Khwarizmi & Balancing Equations", [re.compile(r'\b(al-khwarizmi|hisab al-jabr)\b', re.IGNORECASE)]),
    ("Alvin Deep-Sea Submersible & Sea-Level Dives", [re.compile(r'\b(submersible alvin|woods hole|below sea level)\b', re.IGNORECASE)]),
    ("Apollo Guidance Computer & Margaret Hamilton", [re.compile(r'\b(apollo guidance computer|margaret hamilton|lunar module)\b', re.IGNORECASE)]),
    ("Archimedes (Sphere, Crown Test & Pi)", [re.compile(r'\b(archimedes|syracuse|water displacement)\b', re.IGNORECASE)]),
    ("Area & Perimeter of 2D Shapes ([RECT], [TRI], [CIRC])", [re.compile(r'\b(perimeter|area of a rectangle|area of a triangle|trapezoid)\b', re.IGNORECASE)]),
    ("Area-Model Factoring Tiles & L-Frame", [re.compile(r'\b(factoring tiles?|l-frame|area models?|partial products?)\b', re.IGNORECASE)]),
    ("Averages: Mean ([x̄]), Median ([MED]) & Mode ([MODE])", [re.compile(r'\b(fair-share average|median|mean absolute deviation)\b', re.IGNORECASE)]),
    ("Baker's Percentages & Recipe Scaling", [re.compile(r'\b(baker\'s percentage|recipe scaling|sourdough)\b', re.IGNORECASE)]),
    ("Base-10 Place Value ([PV]) & Regrouping", [re.compile(r'\b(place value|base-10|regrouping|ten-for-one)\b', re.IGNORECASE)]),
    ("Base-60 Clock Time ([H.MMSS], [->HR], [->HMS])", [re.compile(r'\b(base-60|decimal hours|h\.mmss)\b', re.IGNORECASE)]),
    ("Blaise Pascal (Pascaline & Hydraulic Syringe Press)", [re.compile(r'\b(blaise pascal|pascaline|hydraulic)\b', re.IGNORECASE)]),
    ("Box Plots, Quartiles & Interquartile Range ([IQR])", [re.compile(r'\b(box plot|interquartile range|outlier)\b', re.IGNORECASE)]),
    ("Carl Friedrich Gauss & Triangular Staircases", [re.compile(r'\b(carl friedrich gauss|triangular number|staircase)\b', re.IGNORECASE)]),
    ("Chessboard Doubling Legend & Exponents ([y^x])", [re.compile(r'\b(chessboard|sissa|exponents?|powers of two)\b', re.IGNORECASE)]),
    ("Cicadas (13-Year & 17-Year Prime Cycles)", [re.compile(r'\b(cicadas?|magicicada|prime cycle)\b', re.IGNORECASE)]),
    ("Circles, Pi ([π]) & Circumference", [re.compile(r'\b(circumference|radius|diameter)\b', re.IGNORECASE)]),
    ("Classroom Planetary Geared Clock ([CLOCK])", [re.compile(r'\b(planetary clock|geared clock|sun gear|planet gears)\b', re.IGNORECASE)]),
    ("Commutative, Associative & Distributive Laws", [re.compile(r'\b(commutative|associative|distributive|turn-around rule)\b', re.IGNORECASE)]),
    ("Common Denominators & Equivalent Fractions", [re.compile(r'\b(common denominator|equivalent fractions?|unreduced)\b', re.IGNORECASE)]),
    ("Concrete 1-2-3 Mixing Ratio", [re.compile(r'\b(1-2-3 rule|portland cement|concrete)\b', re.IGNORECASE)]),
    ("Counting Tiles (7.0 mm) & 24-Tile Arrays", [re.compile(r'\b(counting tiles?|24-tile|champion packing)\b', re.IGNORECASE)]),
    ("Decimals, Tenths, Hundredths & Repeating Bars", [re.compile(r'\b(tenths|hundredths|repeating decimal|simon stevin)\b', re.IGNORECASE)]),
    ("Dice, Spinners & 36-Outcome Probability Grid ([DICE])", [re.compile(r'\b(36-outcome|polyhedral dice|fair dice|spinner)\b', re.IGNORECASE)]),
    ("Difference of Two Squares & Odd-Number L-Borders", [re.compile(r'\b(difference of two squares|odd-number|l-border)\b', re.IGNORECASE)]),
    ("Eratosthenes (Sieve of Primes & Earth's Circumference)", [re.compile(r'\b(eratosthenes|sieve of)\b', re.IGNORECASE)]),
    ("Euclid's Elements & Remainder Algorithm", [re.compile(r'\b(euclid|euclidean|elements)\b', re.IGNORECASE)]),
    ("Euler's Polyhedron Formula (V - E + F = 2) & Soccer Balls", [re.compile(r'\b(leonhard euler|geodesic dome|pentagons and hexagons)\b', re.IGNORECASE)]),
    ("Fermi Estimation & Powers of Ten", [re.compile(r'\b(enrico fermi|fermi question|order of magnitude)\b', re.IGNORECASE)]),
    ("Fibonacci (Leonardo of Pisa) & Liber Abaci", [re.compile(r'\b(fibonacci|leonardo of pisa|liber abaci)\b', re.IGNORECASE)]),
    ("Florence Nightingale & Data Detective Work", [re.compile(r'\b(florence nightingale|data detective)\b', re.IGNORECASE)]),
    ("Four-Color Map Theorem (Francis Guthrie)", [re.compile(r'\b(four-color|francis guthrie)\b', re.IGNORECASE)]),
    ("Four-Shelf Stack (Shelf X, Y, Z, T) & Stack Lift", [re.compile(r'\b(4-shelf|four-shelf|stack lift|waiting shelf)\b', re.IGNORECASE)]),
    ("Fraction Studio (84.0 mm Proportional Towers)", [re.compile(r'\b(fraction studio|fraction towers?|84\.0\s*mm|84\s*mm)\b', re.IGNORECASE)]),
    ("Galileo Galilei (Square-Cube Law, Pendulums & Dice)", [re.compile(r'\b(galileo|square-cube law|penguin huddle)\b', re.IGNORECASE)]),
    ("Gear Ratios & Bicycle Sprockets", [re.compile(r'\b(gear ratio|chainring|sprocket|compound gear)\b', re.IGNORECASE)]),
    ("Grace Hopper & Kitchen-Table Stack Thinking", [re.compile(r'\b(grace hopper|compiler)\b', re.IGNORECASE)]),
    ("Greatest Common Factor ([GCF]) & Least Common Multiple ([LCM])", [re.compile(r'\b(greatest common factor|least common multiple|secret partner rule)\b', re.IGNORECASE)]),
    ("Hypatia of Alexandria & Conic Sections", [re.compile(r'\b(hypatia|conic sections?)\b', re.IGNORECASE)]),
    ("Jan Lukasiewicz & Parenthesis-Free Polish Notation", [re.compile(r'\b(lukasiewicz|łodź|warsaw|parenthesis-free)\b', re.IGNORECASE)]),
    ("John Harrison & the H4 Marine Sea Clock", [re.compile(r'\b(john harrison|sea clock|longitude)\b', re.IGNORECASE)]),
    ("John Napier & Diagonal Multiplication Strips", [re.compile(r'\b(john napier|napier\'s bones|rabdologia)\b', re.IGNORECASE)]),
    ("Kaprekar's Constant (6,174) & Palindrome Numbers", [re.compile(r'\b(kaprekar|6,174|6174|palindrome)\b', re.IGNORECASE)]),
    ("Katherine Johnson & NASA's Human Computers", [re.compile(r'\b(katherine johnson|human computers?|glenn)\b', re.IGNORECASE)]),
    ("Keycap [.] (Two-Dot Fraction Entry)", [re.compile(r'\btwo-dot\b', re.IGNORECASE), re.compile(r'\[\.\]')]),
    ("Keycap [?] (4-Second Math Quiz Game)", [re.compile(r'\b(quiz game|quiz engine|4-second)\b', re.IGNORECASE)]),
    ("Keycap [C] (Clear / Backspace)", [re.compile(r'\[(C|CLEAR)\]', re.IGNORECASE)]),
    ("Keycap [COUNT] (Two-Rail Number Rack)", [re.compile(r'\[COUNT\]', re.IGNORECASE), re.compile(r'\bnumber rack\b', re.IGNORECASE)]),
    ("Keycap [ENTER] (Stack Lift & Copy)", [re.compile(r'\[ENTER\]', re.IGNORECASE)]),
    ("Keycap [FRAME] (Ten-Frame Studio)", [re.compile(r'\bten-frame studio\b', re.IGNORECASE)]),
    ("Keycap [LASTX] (Undo & Inverse Check)", [re.compile(r'\[LASTX\]', re.IGNORECASE)]),
    ("Keycap [LINE] (Open Number Line)", [re.compile(r'\[LINE\]', re.IGNORECASE), re.compile(r'\bopen number line\b', re.IGNORECASE)]),
    ("Keycap [REP] (Constant Repeat & Skip-Counting)", [re.compile(r'\[REP\]', re.IGNORECASE)]),
    ("Keycap [R↓] (Roll Stack Carousel)", [re.compile(r'\[R[↓\\]+\]'), re.compile(r'\bcarousel\b', re.IGNORECASE)]),
    ("Keycap [SIMP] (Step-by-Step Fraction Reduction)", [re.compile(r'\[SIMP\]', re.IGNORECASE)]),
    ("Keycap [x<->y] (Swap Shelf X and Shelf Y)", [re.compile(r'\[x[⇄↔<->]+y\]', re.IGNORECASE)]),
    ("Keycap [÷R] (Whole-Number Quotient & Remainder)", [re.compile(r'\[(DivR|÷R)\]', re.IGNORECASE)]),
    ("Keycap [Σ+] (Wall & Data Basket Accumulator)", [re.compile(r'\[[Σ∑]\+\]')]),
    ("Leap Years & Calendar Remainders", [re.compile(r'\b(leap year|gregorian calendar|julius caesar)\b', re.IGNORECASE)]),
    ("Maryam Mirzakhani & Curved Surface Geometry", [re.compile(r'\b(maryam mirzakhani|fields medal)\b', re.IGNORECASE)]),
    ("Math Dominoes & Mental Math Shortcuts", [re.compile(r'\b(math dominoes?|shakuntala devi|mental math)\b', re.IGNORECASE)]),
    ("Negative Numbers, Zero Pairs & Sign Flip ([+/-])", [re.compile(r'\b(zero pairs?|negative numbers?|hot-air balloon)\b', re.IGNORECASE)]),
    ("Prime Numbers ([PRIME]), Factor Trees ([FACT]) & RSA Codes", [re.compile(r'\b(prime factorization|factor tree|rsa encryption|goldbach)\b', re.IGNORECASE)]),
    ("Pyramids, Cones ([CONE]) & the 3:1 Pouring Proof", [re.compile(r'\b(3:1 pouring|scott tent|square pyramid)\b', re.IGNORECASE)]),
    ("Pythagoras (3-4-5 Right Triangle & Musical Strings)", [re.compile(r'\b(pythagoras|3-4-5|monochord|hypotenuse)\b', re.IGNORECASE)]),
    ("Ratios, Tape Diagrams, Unit Rates & Percentages ([%])", [re.compile(r'\b(tape diagram|unit rate|sales tax|percent change)\b', re.IGNORECASE)]),
    ("Srinivasa Ramanujan & Taxicab Number 1,729", [re.compile(r'\b(ramanujan|1,729|1729|taxicab)\b', re.IGNORECASE)]),
    ("STEM Maker Labs (3D Printing, Solar Ovens, Catapults & Bridges)", [re.compile(r'\b(solar oven|catapult|paper truss|strength-to-weight)\b', re.IGNORECASE)]),
    ("Surface Area & Unfolding 3D Nets ([PRISM])", [re.compile(r'\b(surface area|folding net|twin walls)\b', re.IGNORECASE)]),
    ("Teacher Lesson Plans (25 Turnkey 45-Minute Stations)", [re.compile(r'\b(station f\.|station 3\.|station 4\.|station 5\.|station 6\.)\b', re.IGNORECASE)]),
    ("Thomas Jefferson & Decimal Currency (Pieces of Eight)", [re.compile(r'\b(thomas jefferson|piece of eight|two bits)\b', re.IGNORECASE)]),
    ("Volume of Prisms, Cylinders, Cones & Spheres", [re.compile(r'\b(volume of a|weather balloon|aqueduct)\b', re.IGNORECASE)]),
    ("Wright Brothers & the 1901 Bicycle-Shop Wind Tunnel", [re.compile(r'\b(wright brothers|orville|wind tunnel)\b', re.IGNORECASE)]),
]

INDEX_CATALOG_DOMAINS = [
    ("4-Register RPN Stack (T, Z, Y, X) & Vector Decomposition", [re.compile(r'\b(register [xyzt]|four-register|stack lift)\b', re.IGNORECASE)]),
    ("4–20 mA Current Loop Scaling & Live Zero ([mA])", [re.compile(r'\b(4-20|4\s*mA|20\s*mA|current loop|live zero)\b', re.IGNORECASE)]),
    ("ABV (Alcohol by Volume) & Specific Gravity ([ABV], [SGT])", [re.compile(r'\b(alcohol by volume|original gravity|final gravity|attenuation)\b', re.IGNORECASE)]),
    ("Acid-Base Titration & Henderson-Hasselbalch Buffers ([BUF], [EQV])", [re.compile(r'\b(henderson-hasselbalch|titration|conjugate base|buffer)\b', re.IGNORECASE)]),
    ("ADC Quantization, LSB Step & Mixed-Signal Resolution ([ADC])", [re.compile(r'\b(analog-to-digital|quantization|\badc\b)\b', re.IGNORECASE)]),
    ("Arrhenius Activation Energy & Chemical Kinetics ([Eₐ], [t½])", [re.compile(r'\b(arrhenius|activation energy|rate constant)\b', re.IGNORECASE)]),
    ("Avogadro, Amedeo & Stoichiometric Molar Bridge", [re.compile(r'\b(avogadro|cannizzaro|stoichiometr)\b', re.IGNORECASE)]),
    ("Aviation Wind Triangle, Crosswind & WCA ([WND], [XWC])", [re.compile(r'\b(wind triangle|crosswind|wind correction angle)\b', re.IGNORECASE)]),
    ("Baker's Percentage, Dough Hydration & Scaling ([BK%], [HYD], [SCL])", [re.compile(r'\b(baker\'s percentage|dough hydration|flour weight)\b', re.IGNORECASE)]),
    ("Beer-Lambert Law, Absorbance & Spectrophotometry ([εbc], [%T])", [re.compile(r'\b(beer-lambert|absorbance|transmittance|molar absorptivity)\b', re.IGNORECASE)]),
    ("Bitfield Masking, Population Count & Leading Zeros ([MSK], [#B], [CLZ])", [re.compile(r'\b(bitfield|hamming weight|population count|leading zeros)\b', re.IGNORECASE)]),
    ("Bitwise Logic, Shift/Rotate & Two's Complement ([NEG], [ASR], [ROR])", [re.compile(r'\b(two\'s complement|bitwise|rotate left|arithmetic shift)\b', re.IGNORECASE)]),
    ("Black-Scholes Option Pricing & Volatility", [re.compile(r'\b(black-scholes|call option|volatility|risk-free)\b', re.IGNORECASE)]),
    ("Body Surface Area (Du Bois & Mosteller Formula, [BSA])", [re.compile(r'\b(mosteller|du bois|body surface area|\bbsa\b)\b', re.IGNORECASE)]),
    ("Bolt Circle Coordinates & Rotary Machining ([BC], [SFM])", [re.compile(r'\b(bolt circle|surface feet per minute|spindle speed)\b', re.IGNORECASE)]),
    ("Bond Pricing, Macaulay Duration & Convexity ([BND])", [re.compile(r'\b(macaulay duration|yield to maturity|bond price|convexity)\b', re.IGNORECASE)]),
    ("Bowditch Compass Rule & Traverse Closure ([TRV], [CLS])", [re.compile(r'\b(bowditch|compass rule|misclosure|closure error)\b', re.IGNORECASE)]),
    ("Brake Horsepower & Control Valve Sizing ([PMP], [Cᵥ])", [re.compile(r'\b(brake horsepower|flow coefficient|\bcv\b)\b', re.IGNORECASE)]),
    ("Centrifuge Relative Centrifugal Force ([RCF])", [re.compile(r'\b(centrifugal force|\brcf\b|centrifuge)\b', re.IGNORECASE)]),
    ("CIDR IPv4 Subnetting & Host Capacity ([NET])", [re.compile(r'\b(cidr|subnet|netmask|broadcast address)\b', re.IGNORECASE)]),
    ("Circular Highway Curves, Tangent & Chord ([CRV])", [re.compile(r'\b(circular curve|deflection angle|long chord|middle ordinate)\b', re.IGNORECASE)]),
    ("Cockcroft-Gault Creatinine Clearance ([GFR])", [re.compile(r'\b(cockcroft-gault|creatinine clearance|renal|glomerular)\b', re.IGNORECASE)]),
    ("Color Temperature, Mired Shift & Inverse-Square Lux ([LUX], [GEL])", [re.compile(r'\b(mired|correlated color temperature|illuminance|foot-candles)\b', re.IGNORECASE)]),
    ("Conduit Offset Bends, Cosecant & Shrink ([OFS], [MIT])", [re.compile(r'\b(conduit|offset bend|shrinkage|saddle bend)\b', re.IGNORECASE)]),
    ("Coordinate Inverse & Forward Projection ([TRV], [INV], [BRG])", [re.compile(r'\b(coordinate geometry|azimuth|northing|easting|departure)\b', re.IGNORECASE)]),
    ("CRC-32 Polynomial Division & Checksums ([CRC])", [re.compile(r'\b(cyclic redundancy|crc-32|galois)\b', re.IGNORECASE)]),
    ("Decibel Power/Voltage Ratios & dBm ([dBm], [SPL])", [re.compile(r'\b(decibels?|\bdbm\b|incoherent|sound pressure level)\b', re.IGNORECASE)]),
    ("Density Altitude & International Standard Atmosphere ([ALT])", [re.compile(r'\b(density altitude|pressure altitude|standard atmosphere)\b', re.IGNORECASE)]),
    ("Depth of Field, Hyperfocal Distance & Circle of Confusion ([DOF], [HFD])", [re.compile(r'\b(hyperfocal|depth of field|circle of confusion)\b', re.IGNORECASE)]),
    ("Desired Dough Temperature & Mixer Friction ([Tw], [ICE])", [re.compile(r'\b(desired dough temperature|friction factor|strike-water)\b', re.IGNORECASE)]),
    ("Differential Spirit Leveling & Three-Wire Stadia ([LVL])", [re.compile(r'\b(differential leveling|backsight|foresight|stadia)\b', re.IGNORECASE)]),
    ("Dilution Conservation (C1V1 = C2V2, [C₁V₁])", [re.compile(r'\b(dilution|stock solution|aliquot)\b', re.IGNORECASE)]),
    ("Endianness Byte Swap & IEEE-754 Floating-Point ([SWP], [FLT])", [re.compile(r'\b(endianness|little-endian|big-endian|ieee-754|mantissa)\b', re.IGNORECASE)]),
    ("Exposure Value, f-Stops & Rotary Shutter Angle ([EV], [SHT])", [re.compile(r'\b(shutter angle|exposure value|aperture)\b', re.IGNORECASE)]),
    ("Fibonacci (Leonardo of Pisa) & Present-Value Discounting", [re.compile(r'\b(fibonacci|liber abaci|present value)\b', re.IGNORECASE)]),
    ("Field of View & Sensor Crop Factor ([FOV])", [re.compile(r'\b(field of view|focal length|rectilinear)\b', re.IGNORECASE)]),
    ("First-Order Pharmacokinetic Elimination & Half-Life ([PK])", [re.compile(r'\b(half-life|elimination rate|steady-state|trough)\b', re.IGNORECASE)]),
    ("Fixed-Point Q-Format Scaling & Memory Alignment ([Q.n], [ALN])", [re.compile(r'\b(fixed-point|q-format|cache-line|alignment)\b', re.IGNORECASE)]),
    ("Friis, Harald T. & Free-Space Link Budgets ([FSL], [LNK])", [re.compile(r'\b(friis|free-space path loss|link budget|\bfspl\b)\b', re.IGNORECASE)]),
    ("Gauss's Shoelace Polygon Area Formula ([CLS])", [re.compile(r'\b(shoelace|polygon area|acreage)\b', re.IGNORECASE)]),
    ("Gravity IV Drip Rates & Weight-Based Infusions ([DOS], [DRP], [gtt])", [re.compile(r'\b(drip factor|drops per minute|vasopressor|norepinephrine|titration)\b', re.IGNORECASE)]),
    ("Heaviside, Oliver & Transmission-Line Telegrapher Equations", [re.compile(r'\b(heaviside|characteristic impedance|transmission line)\b', re.IGNORECASE)]),
    ("Hexadecimal ([HEX]), Binary ([BIN]) & Word Sizes ([WSZ])", [re.compile(r'\b(hexadecimal|word size|nibble|radix)\b', re.IGNORECASE)]),
    ("Holliday-Segar 4-2-1 Pediatric Fluid Rule ([PED], [421])", [re.compile(r'\b(holliday-segar|4-2-1|pediatric maintenance)\b', re.IGNORECASE)]),
    ("Hop Utilization (Tinseth IBU) & Mash Strike Water ([MSH], [IBU])", [re.compile(r'\b(tinseth|strike water|alpha-acid|isomerization)\b', re.IGNORECASE)]),
    ("Ideal & Adjusted Body Weight (Devine Formula, [IBW], [ABW])", [re.compile(r'\b(ideal body weight|adjusted body weight|devine)\b', re.IGNORECASE)]),
    ("Ideal Gas Law (PV = nRT, [PVT])", [re.compile(r'\b(ideal gas|universal gas constant)\b', re.IGNORECASE)]),
    ("Kelvin, Lord (William Thomson) & Physical Measurement", [re.compile(r'\b(kelvin|william thomson)\b', re.IGNORECASE)]),
    ("Leibniz, Shannon & Boolean Switching Algebra", [re.compile(r'\b(leibniz|shannon|boolean)\b', re.IGNORECASE)]),
    ("Mason, Charles & Jeremiah Dixon (Geodetic Azimuth Survey)", [re.compile(r'\b(mason|dixon|theodolite)\b', re.IGNORECASE)]),
    ("Molar Mass, Stoichiometry & Molarity ([MW], [RXN])", [re.compile(r'\b(molar mass|molarity|formula weight)\b', re.IGNORECASE)]),
    ("NEC Conductor Resistance, Ampacity & Voltage Drop ([AWG])", [re.compile(r'\b(circular mils|voltage drop|american wire gauge|\bawg\b)\b', re.IGNORECASE)]),
    ("Net Present Value (NPV) & Internal Rate of Return ([CF])", [re.compile(r'\b(net present value|internal rate of return)\b', re.IGNORECASE)]),
    ("Ohm, Georg Simon & Feeder Loop Resistance ([Ω])", [re.compile(r'\b(ohm|feeder|conductor resistance)\b', re.IGNORECASE)]),
    ("Plato, Fritz & Balling Wort Gravity Scales ([SGT])", [re.compile(r'\b(plato|balling|wort|specific gravity)\b', re.IGNORECASE)]),
    ("Platinum RTD Callendar-Van Dusen Thermometry ([RTD])", [re.compile(r'\b(pt100|callendar-van dusen|\brtd\b)\b', re.IGNORECASE)]),
    ("PWM Timer Prescalers & UART Baud Divisors ([PWM], [BPS])", [re.compile(r'\b(pulse-width modulation|baud rate|prescaler|\buart\b|\bpwm\b)\b', re.IGNORECASE)]),
    ("Quarter-Wave Impedance Transformer ([TLN], [Z₀])", [re.compile(r'\b(quarter-wave|geometric mean|matching section)\b', re.IGNORECASE)]),
    ("Reflection Coefficient Γ, VSWR & Return Loss ([SWR], [RL], [Γ])", [re.compile(r'\b(reflection coefficient|\bvswr\b|standing wave|return loss|mismatch loss)\b', re.IGNORECASE)]),
    ("Sabine, Wallace Clement & Room Reverberation ([DLY], [λ])", [re.compile(r'\b(sabine|reverberation|\brt60\b)\b', re.IGNORECASE)]),
    ("SC-14 Electrical Power, Conduit & Industrial Trades Calculator", [re.compile(r'\bsc-14\b', re.IGNORECASE)]),
    ("SC-16 Binary Radix, Bitwise Logic & Embedded Calculator", [re.compile(r'\bsc-16\b', re.IGNORECASE)]),
    ("SC-24 Cinema Optics, Broadcast Timecode & Sound Calculator", [re.compile(r'\bsc-24\b', re.IGNORECASE)]),
    ("SC-35 Geomatics, Land Surveying & Flight Navigation Calculator", [re.compile(r'\bsc-35\b', re.IGNORECASE)]),
    ("SC-50 RF Engineering, Transmission Lines & Link Calculator", [re.compile(r'\bsc-50\b', re.IGNORECASE)]),
    ("SC-60 Stoichiometry, Equilibrium & Wet-Lab Calculator", [re.compile(r'\bsc-60\b', re.IGNORECASE)]),
    ("SC-78 Commercial Baking, Dough & Brewing Calculator", [re.compile(r'\bsc-78\b', re.IGNORECASE)]),
    ("SC-80 Clinical Dosing, Renal Clearance & ICU Calculator", [re.compile(r'\bsc-80\b', re.IGNORECASE)]),
    ("SC-95 Quantitative Finance, Valuation & Six Sigma Calculator", [re.compile(r'\bsc-95\b', re.IGNORECASE)]),
    ("Sexagesimal Degrees-Minutes-Seconds (DDD.MMSS, [▸HMS])", [re.compile(r'\b(sexagesimal|ddd\.mmss|arcminutes|arcseconds)\b', re.IGNORECASE)]),
    ("Shewhart, Walter A. & Six Sigma Process Capability ([Cpk], [pN])", [re.compile(r'\b(shewhart|six sigma|process capability|\bcpk\b)\b', re.IGNORECASE)]),
    ("Slope Distance Reduction & Architectural Feet-Inches ([SLP], [f-i])", [re.compile(r'\b(slope distance|zenith|fractional inches)\b', re.IGNORECASE)]),
    ("Smith, Phillip H. & Normalized Impedance Chart", [re.compile(r'\b(smith chart|phillip h\.? smith|normalized impedance)\b', re.IGNORECASE)]),
    ("SMPTE Timecode & 29.97 Drop-Frame Arithmetic ([TC], [FPS], [DF])", [re.compile(r'\b(smpte|timecode|drop-frame|29\.97)\b', re.IGNORECASE)]),
    ("Sørensen, Søren P. L. & Logarithmic pH Activity ([pH], [pKₐ])", [re.compile(r'\b(sørensen|sorensen|hydrogen-ion|acid dissociation)\b', re.IGNORECASE)]),
    ("Tesla, Nikola & Three-Phase AC Power Triangle ([PF], [kVA], [FLA])", [re.compile(r'\b(tesla|three-phase|power factor|apparent power|reactive power)\b', re.IGNORECASE)]),
    ("Thermal Noise Floor, Cascaded Noise Figure & IP3 ([NF], [IP3])", [re.compile(r'\b(noise figure|thermal noise|intermodulation|\bip3\b)\b', re.IGNORECASE)]),
    ("Time Value of Money & Loan Amortization ([TVM], [AMR])", [re.compile(r'\b(time value of money|amortization|compound interest)\b', re.IGNORECASE)]),
]


def extract_index_terms(
    text: str,
    is_sc32: bool,
    term_counts: Optional[Dict[str, int]] = None,
    max_per_term: int = 6,
    manual_kind: Optional[str] = None,
) -> List[str]:
    """
    Identifies relevant subject index terms from paragraph or heading text.
    Limits each term to at most `max_per_term` distinct references across the manual.
    """
    if term_counts is None:
        return []
    kind = manual_kind or ("sc32" if is_sc32 else "sc6")
    if kind == "domains":
        catalog = INDEX_CATALOG_DOMAINS
    elif kind == "sc32":
        catalog = INDEX_CATALOG_SC32
    else:
        catalog = INDEX_CATALOG_SC6
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
    G_CODES = [
        "0100111", "0110011", "0011011", "0100001", "0011101",
        "0111001", "0000101", "0010001", "0001001", "0010111",
    ]
    R_CODES = [
        "1110010", "1100110", "1101100", "1000010", "1011100",
        "1001110", "1010000", "1000100", "1001000", "1110100",
    ]
    digits = [int(ch) for ch in re.sub(r"\D", "", isbn_digits)[:13]]
    while len(digits) < 13:
        digits.append(0)

    # EAN-13 parity pattern for leading digit '9' (Bookland 978/979) is LLGLGG
    left_parity = "LLGLGG"
    bits = "101"  # Left guard
    for idx_d, d in enumerate(digits[1:7]):
        bits += L_CODES[d] if left_parity[idx_d] == "L" else G_CODES[d]
    bits += "01010"  # Center guard
    for d in digits[7:13]:
        bits += R_CODES[d]
    bits += "101"  # Right guard

    # 5-digit Bookland add-on ("90000" = No Suggested Retail Price Encoded; EAN-5 parity for 90000 is GLLGL)
    addon_parity = "GLLGL"
    addon_bits = "1011"
    for idx_a, d in enumerate([9, 0, 0, 0, 0]):
        addon_bits += L_CODES[d] if addon_parity[idx_a] == "L" else G_CODES[d]
        if idx_a < 4:
            addon_bits += "01"

    bar_x0 = x + 13.0
    module_w = 0.88
    bar_bottom = y + 18.0
    bar_top = y + h - 17.0
    bar_h = bar_top - bar_bottom

    c.setFillColor(to_color("#000000"))
    for idx_b, bit in enumerate(bits):
        if bit == "1":
            is_guard = (idx_b < 3) or (45 <= idx_b < 50) or (idx_b >= 92)
            by = bar_bottom - (4.0 if is_guard else 0.0)
            bh = bar_h + (4.0 if is_guard else 0.0)
            c.rect(bar_x0 + idx_b * module_w, by, module_w * 0.96, bh, fill=1, stroke=0)

    # Draw 5-digit "90000" add-on bars to the right
    addon_x0 = bar_x0 + len(bits) * module_w + 6.0
    addon_h = bar_h - 6.0
    c.setFont(FONT_MONO_BOLD, 6.2)
    c.drawCentredString(addon_x0 + (len(addon_bits) * module_w) * 0.5, bar_top - 4.5, "90000 >")
    for idx_b, bit in enumerate(addon_bits):
        if bit == "1":
            c.rect(addon_x0 + idx_b * module_w, bar_bottom, module_w * 0.96, addon_h, fill=1, stroke=0)

    # Bottom human-readable EAN-13 digits (no hardcoded price text)
    c.setFont(FONT_MONO_BOLD, 6.8)
    raw_d = "".join(str(d) for d in digits)
    c.drawString(bar_x0 - 6.0, y + 7.5, f"{raw_d[0]}  {raw_d[1:7]}  {raw_d[7:13]}")
    if price_label:
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
    bleed_b: float = 0.0,
    manual_kind: Optional[str] = None,
) -> None:
    """
    Renders a true minimalist NYT Bestseller 6x9 trade Front Cover ("very simple visuals with few words"):
    - Continuous Warm Archival Paper (#F7F4EB) across the entire cover with >65% open whitespace.
    - Only 11-14 words on the entire front cover:
      1. Monumental Title: "THINKING IN THE STACK" / "FROM BLOCKS TO THE STACK" / "THE OPERATIVE STACK"
      2. Concise Subtitle: "The Art of Solving Equations from the Inside Out" / "How Hands-On Blocks Make Numbers Click" / "Mathematics for the Real World"
      3. One simple, clever, unboxed minimalist vector illustration floating in the center.
      4. Single-word imprint at the foot: "StackCalc"
    All live elements sit well inside KDP's cover safe zone (>= 0.50 in / 36 pt inside trim).
    """
    c.saveState()
    kind = manual_kind or ("sc32" if is_sc32 else "sc6")

    paper_cream = "#F7F4EB"
    ink_obsidian = "#0F172A"
    ink_slate = "#475569"
    accent = "#0284C7" if kind == "domains" else ("#FF4F00" if kind == "sc32" else "#059669")

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
    if kind == "domains":
        c.setFont(FONT_BODY_BOLD, 36.0)
        c.drawCentredString(cx, oy + h - 118.0, "THE OPERATIVE")
        c.drawCentredString(cx, oy + h - 166.0, "STACK")
        subtitle_str = "Mathematics for the Real World"
    elif kind == "sc32":
        c.setFont(FONT_BODY_BOLD, 42.0)
        c.drawCentredString(cx, oy + h - 118.0, "THINKING IN")
        c.drawCentredString(cx, oy + h - 166.0, "THE STACK")
        subtitle_str = "The Art of Solving Equations from the Inside Out"
    else:
        c.setFont(FONT_BODY_BOLD, 38.0)
        c.drawCentredString(cx, oy + h - 118.0, "FROM BLOCKS")
        c.drawCentredString(cx, oy + h - 166.0, "TO THE STACK")
        subtitle_str = "How Hands-On Blocks Make Numbers Click"

    # 3. Short Subtitle
    c.setFont(FONT_BODY_ITALIC, 13.0)
    c.setFillColor(to_color(ink_slate))
    c.drawCentredString(cx, oy + h - 198.0, subtitle_str)

    # 4. Single Minimalist Iconic Visual Floating in Generous Whitespace (Center of Cover)
    if kind == "domains":
        # Part A: Row 0 Domain Softkey Bar (6 physical trade softkeys across the 9 instruments)
        softkeys = ["FWD", "3PH", "HEX", "TC", "SWR", "NPV"]
        pill_w = 34.0
        pill_h = 18.0
        pill_gap = 5.0
        total_pills_w = len(softkeys) * pill_w + (len(softkeys) - 1) * pill_gap
        start_px = cx - (total_pills_w * 0.5)
        pill_y = oy + 358.0
        for idx_s, sk_lbl in enumerate(softkeys):
            px = start_px + idx_s * (pill_w + pill_gap)
            c.setFillColor(to_color("#E2DDD0"))
            c.roundRect(px + 1.5, pill_y - 1.5, pill_w, pill_h, 3.5, fill=1, stroke=0)
            c.setFillColor(to_color("#1E293B"))
            c.roundRect(px, pill_y, pill_w, pill_h, 3.5, fill=1, stroke=0)
            c.setFillColor(to_color(accent if idx_s in (0, 4) else "#D97706"))
            c.rect(px + 5.0, pill_y + pill_h - 3.0, pill_w - 10.0, 1.5, fill=1, stroke=0)
            c.setFont(FONT_MONO_BOLD, 7.5)
            c.setFillColor(to_color("#FFFFFF"))
            c.drawCentredString(px + pill_w * 0.5, pill_y + 5.0, sk_lbl)

        # Part B: Four Minimalist Floating Stack Bars (T, Z, Y, X) holding authentic unitless trade quantities (left-aligned)
        bar_w = 229.0
        bar_h = 24.0
        bar_gap = 10.0
        bar_x = cx - (bar_w * 0.5)
        top_bar_y = oy + 312.0

        stack_bars = [
            ("T:", "50.0000", "#E6E1D3", "#64748B", "#475569"),
            ("Z:", "75.0000", "#DCD6C6", "#475569", "#334155"),
            ("Y:", "0.2000", "#1E293B", "#94A3B8", "#FFFFFF"),
            ("X:", "1.5000", "#0284C7", "#E0F2FE", "#FFFFFF"),
        ]
        for idx_b, (lbl, val, fill_hex, lbl_hex, val_hex) in enumerate(stack_bars):
            by = top_bar_y - idx_b * (bar_h + bar_gap)
            c.setFillColor(to_color(fill_hex))
            c.roundRect(bar_x, by, bar_w, bar_h, 4.0, fill=1, stroke=0)
            c.setFont(FONT_MONO_BOLD, 9.5)
            c.setFillColor(to_color(lbl_hex))
            c.drawString(bar_x + 14.0, by + 7.5, lbl)
            if val:
                c.setFont(FONT_MONO_BOLD, 10.5)
                c.setFillColor(to_color(val_hex))
                c.drawString(bar_x + 38.0, by + 7.5, val)
    elif kind == "sc32":
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

        # Part B: Four Minimalist Floating Stack Bars (T, Z, Y, X) — authentic RPN state after solving both inner branches (left-aligned)
        bar_w = 188.0
        bar_h = 24.0
        bar_gap = 10.0
        bar_x = cx - (bar_w * 0.5)
        top_bar_y = oy + 306.0

        stack_bars = [
            ("T:", "0", "#E6E1D3", "#64748B", "#64748B"),
            ("Z:", "0", "#DCD6C6", "#475569", "#334155"),
            ("Y:", "7", "#1E293B", "#94A3B8", "#FFFFFF"),
            ("X:", "11", "#FF4F00", "#FFE4D6", "#FFFFFF"),
        ]
        for idx_b, (lbl, val, fill_hex, lbl_hex, val_hex) in enumerate(stack_bars):
            by = top_bar_y - idx_b * (bar_h + bar_gap)
            c.setFillColor(to_color(fill_hex))
            c.roundRect(bar_x, by, bar_w, bar_h, 4.0, fill=1, stroke=0)
            c.setFont(FONT_MONO_BOLD, 9.5)
            c.setFillColor(to_color(lbl_hex))
            c.drawString(bar_x + 14.0, by + 7.5, lbl)
            if val:
                c.setFont(FONT_MONO_BOLD, 11.0)
                c.setFillColor(to_color(val_hex))
                c.drawString(bar_x + 38.0, by + 7.5, val)
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
    bleed_b: float = 0.0,
    manual_kind: Optional[str] = None,
) -> None:
    """
    Renders a minimalist 6x9 NYT Bestseller trade Back Cover on continuous Warm Archival Paper (#F7F4EB):
    - Generous open margins, one bold armchair-reader hook question, two short narrative paragraphs,
      a quiet 2-line note on the companion problems/equations inside, the StackCalc imprint, and
      KDP's mandatory 2.00 x 1.20 in white ISBN-13 barcode box.
    """
    c.saveState()
    kind = manual_kind or ("sc32" if is_sc32 else "sc6")

    paper_cream = "#F7F4EB"
    ink_obsidian = "#0F172A"
    ink_slate = "#334155"
    ink_muted = "#64748B"
    accent = "#0284C7" if kind == "domains" else ("#FF4F00" if kind == "sc32" else "#059669")

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
        "MATHEMATICS  /  APPLIED ENGINEERING & TRADES"
        if kind == "domains" else
        ("MATHEMATICS  /  POPULAR SCIENCE" if kind == "sc32" else "MATHEMATICS  /  EDUCATION")
    )

    # 3. Bold Armchair-Reader Hook Question
    c.setFillColor(to_color(ink_obsidian))
    c.setFont(FONT_BODY_BOLD, 17.5)
    if kind == "domains":
        c.drawString(safe_x, oy + h - 92.0, "Every physical trade speaks its own")
        c.drawString(safe_x, oy + h - 114.0, "dialect of mathematics.")
        p1_html = (
            "Why do land surveyors measure angles clockwise from true North instead of counterclockwise "
            "from East? Why do bakers anchor every ingredient to flour weight rather than total dough weight? "
            "Why does radio power decay with the square of distance and frequency, and why must clinical drug "
            "doses scale with body surface area and renal clearance rather than body weight alone?"
        )
        p2_html = (
            "<b>The Operative Stack</b> explores the first-principles mathematics behind nine physical disciplines—"
            "using compact operational acronyms (<b>FWD, INV, VD, BEND, HEX, TC, SWR, MW, BKR%, BSA, NPV</b>) to motivate "
            "each idea before showing how those equations unfold step by step across a four-register Reverse Polish Notation "
            "stack (<b>Registers T, Z, Y, X</b>) on the <b>SC-35, SC-14, SC-16, SC-24, SC-50, SC-60, SC-78, SC-80,</b> and <b>SC-95</b>."
        )
        ref_note_html = (
            "<b>Nine Disciplines Inside:</b> Geomatics &amp; Flight Navigation  •  Electrical &amp; Industrial Trades  "
            "•  Binary Logic &amp; Embedded Timing  •  Cinematography, Timecode &amp; Acoustics  •  RF Propagation &amp; Link Budgets  "
            "•  Stoichiometry &amp; Wet-Lab Analytics  •  Artisan Baking &amp; Zymurgy  •  Clinical Dosing &amp; Kinetics  •  Capital Valuation &amp; Statistical Inference."
        )
    elif kind == "sc32":
        c.drawString(safe_x, oy + h - 92.0, "Written for paper from the outside in.")
        c.drawString(safe_x, oy + h - 114.0, "Solved in time from the inside out.")
        p1_html = (
            "In 1924, the Polish logician Jan Łukasiewicz proved that algebraic parentheses are an artifact "
            "of sixteenth-century printing, not a law of mathematics. When an equation is solved "
            "from its innermost core outward across four visible registers, parentheses vanish, hidden memory "
            "states disappear, and complex derivations unfold one live physical quantity at a time."
        )
        p2_html = (
            "Across fourteen chapters—from William Hewlett's 1971 pocket-calculator "
            "challenge and John Napier's logarithms to Steinmetz's AC phasors, Cardano and Brent's root solvers, "
            "Gauss's recovery of Ceres by Least Squares, and Enrico Fermi's Trinity paper scraps—<b>Thinking in the "
            "Stack</b> connects the history of mathematical ideas with the <b>StackCalc SC-32</b>."
        )
        ref_note_html = (
            "Logarithms &amp; Power Laws  •  Vectors, Phasors &amp; Solid Geometry  •  Cardano's Cubic &amp; "
            "Brent's Root Solver  •  Romberg Quadrature &amp; Least Squares  •  36-Bit Binary, Time Value of Money "
            "&amp; Applied Engineering Case Studies."
        )
    else:
        c.drawString(safe_x, oy + h - 92.0, "What happens when you can hold")
        c.drawString(safe_x, oy + h - 114.0, "a number in your hands?")
        p1_html = (
            "Children rarely struggle with math because numbers are too hard. They struggle when flat worksheets "
            "and black-box calculators separate symbols from physical objects. When you snap physical tiles "
            "into a frame and watch those exact numbers ride a four-story elevator stack, arithmetic stops "
            "being a rule to memorize and becomes something you can see."
        )
        p2_html = (
            "Written for young explorers (Grades 3–6), parents, and teachers alike, <b>From Blocks to the Stack</b> "
            "connects hands-on 3D blocks with parenthesis-free thinking—serving as both an engaging guide to visual "
            "number sense and the complete companion to the <b>StackCalc SC-6</b>."
        )
        ref_note_html = (
            "<b>Inside the Book:</b> 9 story-driven chapters (Grades 3–6)  •  9 open-source 3D-printable "
            "math block studios  •  Step-by-step stack tables  •  25 classroom &amp; home station guides."
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

    # 5. Bottom Left Imprint (Bottom-right 2.00 x 1.20 in zone intentionally left clear for KDP's auto-stamped ISBN barcode)
    c.setFillColor(to_color(ink_obsidian))
    c.setFont(FONT_BODY_BOLD, 14.0)
    c.drawString(safe_x, oy + 88.0, "StackCalc")

    c.setFillColor(to_color(ink_muted))
    c.setFont(FONT_BODY, 8.5)
    c.drawString(safe_x, oy + 72.0, "Instruments, Software & Open-Source Models")
    c.setFont(FONT_MONO_BOLD, 8.0)
    c.setFillColor(to_color(accent))
    c.drawString(safe_x, oy + 56.0, "stackcalc.io")

    c.restoreState()


def build_kdp_front_matter(
    is_sc32: bool,
    styles: Dict[str, ParagraphStyle],
    is_hardcover: bool = False,
    manual_kind: Optional[str] = None,
) -> List[Flowable]:
    """
    Generates traditional KDP 6x9 trade/reference book front matter (Pages i–iv in lowercase Roman):
      - Page i   (Recto / Odd):  Half-Title Page (no header, no footer folio)
      - Page ii  (Verso / Even): Series Frontispiece ("The StackCalc Library") (no header, no footer folio)
      - Page iii (Recto / Odd):  Full Title Page with Title, Subtitle & StackCalc imprint (no header, no footer folio)
      - Page iv  (Verso / Even): Copyright, ISBN-13, Safety Notices & KDP Colophon (Roman folio 'iv')
    Covers are NEVER included inside the KDP interior manuscript PDF.
    """
    elements: List[Flowable] = []
    kind = manual_kind or ("sc32" if is_sc32 else "sc6")
    sc6_isbn = "979-8-16-593829-0" if is_hardcover else "979-8-16-592706-5"
    sc32_isbn = "979-8-16-745932-8" if is_hardcover else "979-8-16-742684-9"
    domains_isbn = "979-8-16-841932-1" if is_hardcover else "979-8-14-196167-0"
    binding_label = "Hardcover Edition" if is_hardcover else "Paperback Edition"

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

    if kind == "domains":
        main_title = "THE OPERATIVE STACK"
        vol_label = "THE STACKCALC LIBRARY  •  VOLUME III"
        sub_line = "Mathematics for the Real World"
        desc_line = (
            "First-Principles Applied Mathematics, Operational Shorthand, and Four-Register RPN Stack Traces "
            "Across Surveying, Electrical Trades, Embedded Systems, Cinema, RF, Chemistry, Brewing, Clinical Dosing &amp; Finance"
        )
    elif kind == "sc32":
        main_title = "THINKING IN THE STACK"
        vol_label = "THE STACKCALC LIBRARY  •  VOLUME II"
        sub_line = "The Art of Solving Equations from the Inside Out"
        desc_line = (
            "Reverse Polish Notation, Historical Derivations, Numerical Methods, "
            "and Applied Engineering on the <b>StackCalc SC-32</b>"
        )
    else:
        main_title = "FROM BLOCKS TO THE STACK"
        vol_label = "THE STACKCALC LIBRARY  •  VOLUME I"
        sub_line = "How Hands-On Blocks Make Numbers Click"
        desc_line = (
            "An Illustrated Guide to Visual Number Sense, Fractions, 3D-Printable Math Blocks, "
            "and Parenthesis-Free Thinking for Grades 3–6 (Ages 8–12) — with the <b>StackCalc SC-6</b>"
        )

    # Note: Series overview and architectural notation conventions are documented
    # here in code comments rather than printed as frontispiece pages in the book:
    # - Volume I (SC-6): Visual number sense & 3D math blocks (Grades 3-6)
    # - Volume II (SC-32): Scientific RPN, historical derivations & numerical methods
    # - Volume III (Domains): Applied mathematics across nine physical trades (SC-35..SC-95)

    # --- PAGE i (Recto): Full Title Page ---
    elements.append(ChapterTracker("TITLE PAGE"))
    elements.append(BookmarkFlowable("bm_titlepage", "Title Page", level=0))
    elements.append(Spacer(1, 70))
    elements.append(make_paragraph(vol_label, kicker_style))
    elements.append(Spacer(1, 10))
    if kind == "domains":
        full_page_title = "THE OPERATIVE<br/>STACK"
    elif kind == "sc32":
        full_page_title = "THINKING IN<br/>THE STACK"
    else:
        full_page_title = main_title
    elements.append(make_paragraph(full_page_title, full_title_style))
    elements.append(Spacer(1, 12))
    elements.append(HRFlowable(width="100%", thickness=1.8, color=to_color(TEXT_MAIN), spaceAfter=12))
    elements.append(make_paragraph(sub_line, full_sub_style))
    elements.append(Spacer(1, 8))
    elements.append(make_paragraph(desc_line, full_desc_style))
    elements.append(Spacer(1, 150))
    elements.append(HRFlowable(width="100%", thickness=0.75, color=to_color(DIVIDER_HEX), spaceAfter=8))
    elements.append(make_paragraph("StackCalc", imprint_style))
    elements.append(make_paragraph(
        "stackcalc.io<br/>First Edition",
        full_desc_style
    ))
    elements.append(PageBreak())

    # --- PAGE ii (Verso): Copyright, ISBN, Safety & KDP Colophon Page ---
    elements.append(ChapterTracker("COPYRIGHT AND COLOPHON"))
    elements.append(BookmarkFlowable("bm_copyright", "Copyright & Print Colophon", level=0))
    elements.append(Spacer(1, 24))
    isbn_str = domains_isbn if kind == "domains" else (sc32_isbn if kind == "sc32" else sc6_isbn)
    elements.append(make_paragraph(
        f"<b>{main_title}: {sub_line}</b><br/>"
        f"Copyright © 2026 by <b>StackCalc</b> (https://stackcalc.io). Some rights reserved.<br/>"
        f"Published by <b>StackCalc</b>.<br/>"
        f"<b>ISBN-13:</b> {isbn_str} ({binding_label}) &nbsp;&nbsp;|&nbsp;&nbsp; <b>First Edition</b>",
        copyright_style
    ))
    if kind == "domains":
        elements.append(make_paragraph(
            "<b>Open-Education License (CC BY-NC-SA 4.0):</b> Vocational instructors, university faculty, apprentices, "
            "and practicing engineers are expressly permitted to reproduce tables, 4-register stack traces, and worked "
            "field examples for non-commercial educational instruction under Creative Commons Attribution-NonCommercial-"
            "ShareAlike 4.0 International.",
            copyright_style
        ))
        elements.append(make_paragraph(
            "<b>Engineering, Aviation &amp; Clinical Practice Notice:</b> Worked examples in surveying (SC-35), electrical "
            "and structural trades (SC-14), aviation wind/density altitude, and clinical pharmacy/nursing dosage (SC-80) "
            "are presented for mathematical instruction and reference verification. Always verify operational flight plans, "
            "NEC/local electrical code compliance, and patient medication dosages against official institutional protocols "
            "and dual-clinician checks.",
            copyright_style
        ))
        elements.append(make_paragraph(
            "<b>Trademark Notice:</b> <i>StackCalc</i>, <i>SC-32</i>, <i>SC-6</i>, and <i>SC-35 / SC-14 / SC-16 / SC-24 / SC-50 / SC-60 / SC-78 / SC-80 / SC-95</i> "
            "are trademarks of StackCalc. <i>Hewlett-Packard</i>, <i>SMPTE</i>, <i>National Electrical Code (NEC)</i>, and other "
            "standard or historical names referenced for scholarly attribution are the property of their respective owners.",
            copyright_style
        ))
    elif kind == "sc32":
        elements.append(make_paragraph(
            "<b>Open-Education License (CC BY-NC-SA 4.0):</b> University instructors, classroom teachers, and "
            "students are expressly permitted to reproduce tables, 4-register stack traces, and worked engineering "
            "examples for non-commercial educational instruction under Creative Commons Attribution-NonCommercial-"
            "ShareAlike 4.0 International.",
            copyright_style
        ))
        elements.append(make_paragraph(
            "<b>Trademark Notice:</b> <i>StackCalc</i>, <i>SC-32</i>, and <i>SC-6</i> are trademarks of StackCalc. "
            "<i>Hewlett-Packard</i>, <i>HP-35</i>, <i>HP-15C</i>, <i>HP-32SII</i>, <i>Gridfinity</i>, and other historical "
            "instrument or standard names referenced for scholarly attribution and educational context are the property "
            "of their respective owners, none of whom endorse or sponsor this publication.",
            copyright_style
        ))
    else:
        elements.append(make_paragraph(
            "<b>Open-Education License (CC BY-NC-SA 4.0):</b> Classroom teachers, university instructors, parents, and "
            "students are expressly permitted to reproduce tables, 4-register stack traces, and 3D manipulative "
            "STL/3MF models for non-commercial educational instruction under Creative Commons Attribution-NonCommercial-"
            "ShareAlike 4.0 International.",
            copyright_style
        ))
        elements.append(make_paragraph(
            "<b>Regulatory &amp; Physical Safety Notice (Reese’s Law / P.L. 117-171 / 16 CFR Part 1263 &amp; ASTM F963):</b> "
            "Physical calculator instruments that utilize coin or button cell batteries must maintain a captive, tool-secured "
            "battery compartment compliant with UL 4200A. 3D-printed unit tiles and polyhedral dice "
            "constitute small parts under 16 CFR Part 1501; adult supervision is required for children under 6 years of age.",
            copyright_style
        ))
        elements.append(make_paragraph(
            "<b>Trademark Notice:</b> <i>StackCalc</i>, <i>SC-32</i>, and <i>SC-6</i> are trademarks of StackCalc. "
            "<i>Common Core State Standards</i>, <i>Singapore Math</i>, <i>Bridges in Mathematics</i>, <i>Hewlett-Packard</i>, "
            "and <i>Gridfinity</i> are trademarks of their respective owners, none of whom endorse or sponsor this publication.",
            copyright_style
        ))
    elements.append(make_paragraph(
        "<b>Print &amp; Typography Colophon:</b> Typeset in Computer Modern Unicode (CMU Serif), SpaceMono, STIX Math, and Terminus LCD "
        "on 6.00 × 9.00 in (152.4 × 228.6 mm) archival white paper in high-contrast monochrome ink for trade paperback "
        "and hardcover editions.",
        copyright_style
    ))
    elements.append(PageBreak())

    # --- PAGE iii (Recto): Dedication & Epigraph Page ---
    elements.append(ChapterTracker("DEDICATION AND EPIGRAPH"))
    elements.append(BookmarkFlowable("bm_dedication", "Dedication & Epigraph", level=0))
    dedication_style = ParagraphStyle(
        "KDPDedication",
        parent=styles["Normal"],
        fontName=FONT_BODY_ITALIC,
        fontSize=10.5,
        leading=15.5,
        textColor=to_color(TEXT_MAIN),
        alignment=1,
    )
    epigraph_quote_style = ParagraphStyle(
        "KDPEpigraphQuote",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=9.5,
        leading=14.2,
        textColor=to_color(TEXT_MUTED),
        alignment=1,
        leftIndent=14,
        rightIndent=14,
    )
    epigraph_attr_style = ParagraphStyle(
        "KDPEpigraphAttr",
        parent=styles["Normal"],
        fontName=FONT_BODY_BOLD,
        fontSize=8.3,
        leading=12.0,
        textColor=to_color(TEXT_MAIN),
        alignment=1,
    )
    elements.append(Spacer(1, 145))
    if kind == "domains":
        elements.append(make_paragraph(
            "<i>For the surveyors, electricians, systems programmers, focus pullers,<br/>"
            "RF engineers, chemists, bakers, brewmasters, clinical nurses, and analysts<br/>"
            "who put mathematics to work in the physical world.</i>",
            dedication_style
        ))
        elements.append(Spacer(1, 48))
        elements.append(make_paragraph(
            "“When you can measure what you are speaking about,<br/>"
            "and express it in numbers, you know something about it.”",
            epigraph_quote_style
        ))
        elements.append(Spacer(1, 6))
        elements.append(make_paragraph(
            "— WILLIAM THOMSON (LORD KELVIN), <i>Electrical Units of Measurement</i> (1883)",
            epigraph_attr_style
        ))
        elements.append(PageBreak())
        return elements
    elif kind == "sc32":
        elements.append(make_paragraph(
            "<i>For every engineer, scientist, and student who has ever wanted to see<br/>"
            "inside the equation—and for the pioneers of parenthesis-free calculation<br/>"
            "from Warsaw to Palo Alto.</i>",
            dedication_style
        ))
        elements.append(Spacer(1, 48))
        elements.append(make_paragraph(
            "“Civilization advances by extending the number of important operations<br/>"
            "which we can perform without thinking about them.”",
            epigraph_quote_style
        ))
        elements.append(Spacer(1, 6))
        elements.append(make_paragraph(
            "— ALFRED NORTH WHITEHEAD, <i>An Introduction to Mathematics</i> (1811)",
            epigraph_attr_style
        ) if False else make_paragraph(
            "— ALFRED NORTH WHITEHEAD, <i>An Introduction to Mathematics</i> (1911)",
            epigraph_attr_style
        ))
        elements.append(PageBreak())
        return elements
    else:
        elements.append(make_paragraph(
            "<i>For every young builder who learns best by holding an idea in their hands,<br/>"
            "and for the parents and teachers who light the spark of mathematical curiosity.</i>",
            dedication_style
        ))
        elements.append(Spacer(1, 48))
        elements.append(make_paragraph(
            "“What I cannot create, I do not understand.”",
            epigraph_quote_style
        ))
        elements.append(Spacer(1, 6))
        elements.append(make_paragraph(
            "— RICHARD P. FEYNMAN, blackboard inscription (1988)",
            epigraph_attr_style
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
    s = re.sub(r"\\begin\{bmatrix\}", r"\\left[ ", s)
    s = re.sub(r"\\end\{bmatrix\}", r" \\right]", s)
    s = re.sub(r"\\begin\{pmatrix\}", r"\\left( ", s)
    s = re.sub(r"\\end\{pmatrix\}", r" \\right)", s)
    s = re.sub(r"\\(?:begin|end)\{(?:aligned|align\*?|array|cases|matrix|pmatrix|bmatrix)\}(?:\{[lcr|]+\})?", "", s)
    s = s.replace(r"\hline", "")
    s = s.replace(r"\&", r"\;\mathrm{AND}\;")
    s = s.replace(r"\ggg", r"\gg")
    s = s.replace("&", " ").replace(r"\\", r", \; ")
    s = re.sub(r"</?[a-zA-Z][^>]*>", "", s)
    s = re.sub(r'"([^"]*)"', r"“\1”", s)
    s = re.sub(r"\{\{key:([^}]+)\}\}", r"[\1]", s)
    s = s.replace("`", "")
    s = re.sub(r"(?<!\\)\$", "", s)
    s = re.sub(r"\\(?:Large|large|small|normalsize|footnotesize|Huge|huge)\s*", "", s)
    s = re.sub(r"\\[bB]igg?[lr]?\b\s*", "", s)
    s = re.sub(r"\\cancel\{((?:[^{}]|\{[^{}]*\})*)\}", r"\1", s)
    s = re.sub(
        r"\\underbrace\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}_\{((?:[^{}]|\{[^{}]*\})*)\}",
        r"\\underset{[\2]}{\\left(\1\\right)}",
        s,
    )
    s = s.replace(r"\tfrac", r"\frac").replace(r"\dfrac", r"\frac").replace(r"\cfrac", r"\frac")
    s = s.replace(r"\leqslant", r"\leq").replace(r"\geqslant", r"\geq")
    s = re.sub(r"\\le(?![a-zA-Z])", r"\\leq", s)
    s = re.sub(r"\\ge(?![a-zA-Z])", r"\\geq", s)
    s = s.replace(r"\lvert", "|").replace(r"\rvert", "|")
    s = s.replace(r"\lVert", r"\|").replace(r"\rVert", r"\|")
    s = s.replace(r"\implies", r"\Rightarrow").replace(r"\iff", r"\Leftrightarrow")
    s = s.replace(r"\to", r"\rightarrow").replace(r"\gets", r"\leftarrow")
    s = s.replace(r"\land", r"\wedge").replace(r"\lor", r"\vee").replace(r"\lnot", r"\neg")
    s = s.replace(r"\empty", r"\emptyset").replace(r"\degree", r"^\circ")
    s = s.replace(r"\parallel", r"\Vert")
    s = s.replace(r"\Box", "□").replace(r"\square", "□")
    s = re.sub(r"\\pmod\{((?:[^{}]|\{[^{}]*\})*)\}", r"\\;(\\mathrm{mod}\\; \1)", s)
    s = re.sub(r"\\bmod\b", r"\\;\\mathrm{mod}\\;", s)
    s = s.replace("↓", r"\downarrow ").replace("↑", r"\uparrow ").replace("→", r"\rightarrow ").replace("←", r"\leftarrow ")
    for _ in range(3):
        s = re.sub(
            r"\\(?:text|textbf|textit|textrm|operatorname)\{([^{}]*)\}",
            lambda m: r"\mathrm{" + m.group(1).replace(" ", r"\ ") + "}",
            s,
        )
        s = re.sub(r"\\(?:text|textbf|textit|textrm|operatorname)\{\\mathrm\{([^{}]*)\}\}", r"\\mathrm{\1}", s)
        s = re.sub(
            r"\\(?:mathbf|boldsymbol|bm)\{((?:[^{}]|\{[^{}]*\})*)\}",
            lambda m: r"\mathbf{" + m.group(1).replace(r"\cdot", r"}\cdot\mathbf{") + "}",
            s,
        )
    s = re.sub(
        r"\\xrightarrow\[([^\]]*)\]\{((?:[^{}]|\{[^{}]*\})*)\}",
        r"\\overset{\2}{\\underset{\1}{\\longrightarrow}}",
        s,
    )
    s = re.sub(r"\\xrightarrow\{((?:[^{}]|\{[^{}]*\})*)\}", r"\\overset{\1}{\\longrightarrow}", s)
    s = s.replace("−", "-").replace("×", r"\times ").replace("÷", r"\div ").replace("±", r"\pm ")
    s = s.replace("≤", r"\leq ").replace("≥", r"\geq ").replace("≠", r"\neq ").replace("≈", r"\approx ")
    s = s.replace("∞", r"\infty ").replace("π", r"\pi ").replace("°", r"^\circ ")
    s = s.replace("√", r"\sqrt")
    s = re.sub(
        r"(?<=[0-9a-zA-Z\}\)])\s*\\(sin|cos|tan|cot|sec|csc|sinh|cosh|tanh|arcsin|arccos|arctan|ln|log|exp)\b",
        r"\\,\\\1",
        s,
    )
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
        _DISPLAY_EQ_CACHE_DIR = Path("/tmp/stackcalc_display_eqs_v8")
        _DISPLAY_EQ_CACHE_DIR.mkdir(parents=True, exist_ok=True)

    norm_tex = _normalize_mathtext_latex(raw_tex)
    has_label = bool(eq_label and eq_label.strip())
    eq_col_w = (PRINTABLE_WIDTH - 54.0) if has_label else PRINTABLE_WIDTH
    num_col_w = 54.0

    eq_num_style = ParagraphStyle(
        "EquationNumber",
        parent=styles["BodyText"],
        fontName=FONT_BODY_BOLD,
        fontSize=8.2,
        leading=10.2,
        alignment=2,
        textColor=to_color(TEXT_MAIN),
    )
    num_para = make_paragraph(f"({eq_label})", eq_num_style) if has_label else None

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
                f"${norm_tex}\\,$",
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
                    pad = 6
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
        # If single-line image would scale down too small (< 0.54), fall back to clean wrapped math paragraph
        if scale >= 0.54:
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

    if has_label and num_para is not None:
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
    else:
        eq_tbl = Table([[eq_flowable]], colWidths=[PRINTABLE_WIDTH])
        eq_tbl.setStyle(TableStyle([
            ("ALIGN", (0, 0), (0, 0), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 2),
            ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ("TOPPADDING", (0, 0), (-1, -1), 3.5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ]))
    eq_tbl.spaceBefore = 2.0
    eq_tbl.spaceAfter = 3.0
    return eq_tbl


# ---------------------------------------------------------------------------
# Markdown File to Flowables Parser (Archival White Paper Interior)
# ---------------------------------------------------------------------------
def parse_markdown_file(
    file_path: Path,
    chapter_idx: int,
    is_sc32: bool,
    styles: Dict[str, ParagraphStyle],
    term_counts: Optional[Dict[str, int]] = None,
    manual_kind: Optional[str] = None,
) -> List[Flowable]:
    """
    Parses a single manual markdown file and converts its headings, tables, code blocks,
    and text into publication-grade ReportLab Flowables on pure white paper.
    """
    kind = manual_kind or ("sc32" if is_sc32 else "sc6")
    elements: List[Flowable] = []
    if kind == "domains":
        primary_hex = DOMAINS_PRIMARY
        accent_hex = DOMAINS_ACCENT
    else:
        primary_hex = SC32_PRIMARY if is_sc32 else SC6_PRIMARY
        accent_hex = SC32_ACCENT if is_sc32 else SC6_ACCENT

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip YAML frontmatter and HTML comments
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    # Strip inline parenthetical notes (e.g. (Classroom Pod Note: ...), (Note: ...)) from PDF while keeping in source
    content = re.sub(r'\s*\((?:Classroom Pod )?Note:\s*[^)]+\)', '', content)

    # In the print PDF, Copyright, Safety & Trademark notices are already typeset on Page iv
    # of the KDP front matter, so omit the duplicate web-only notice block inside index.md
    if file_path.stem.lower() == "index":
        content = re.sub(
            r"\n## Safety, Regulatory, Trademark.*?(?=\n## |\n### |\Z)",
            "\n",
            content,
            flags=re.DOTALL,
        )
        if kind == "domains":
            # Strip repository directory tree block and software test file list from print interior
            content = re.sub(
                r"\n```\ndocumentation/manuals/domains/.*?\n```\n",
                "\n",
                content,
                flags=re.DOTALL,
            )
            content = re.sub(
                r"\n### Verification Suite & Source Grounding\n.*\Z",
                "\n",
                content,
                flags=re.DOTALL,
            )

    if kind == "domains":
        # Convert introductory reader orientation blockquotes (> **Who this is for:** / > *"...) into clean body paragraphs
        content = re.sub(r"^>\s*(\*\*Who this (?:series )?is for:\*\*.*)$", r"\1", content, flags=re.MULTILINE)
        content = re.sub(r'^>\s*(\*".*)$', r"\1", content, flags=re.MULTILINE)

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

    # Split any <div class="admonition...">...</div> block around embedded Markdown tables (| ... |)
    # so the table is rendered by the main ReportLab table engine rather than flattened into raw pipe text.
    def _split_admonition_tables(m):
        open_tag = m.group(1)
        inner = m.group(2)
        if not re.search(r"^\s*\|.*\|\s*$", inner, flags=re.M):
            return m.group(0)
        out_blocks = []
        cur_prose = []
        cur_table = []
        for ln in inner.splitlines():
            if re.match(r"^\s*\|.*\|\s*$", ln):
                if cur_prose:
                    prose_txt = "\n".join(cur_prose).strip()
                    if prose_txt:
                        out_blocks.append(f"{open_tag}\n{prose_txt}\n</div>")
                    cur_prose = []
                cur_table.append(ln.strip())
            else:
                if cur_table:
                    out_blocks.append("\n".join(cur_table))
                    cur_table = []
                cur_prose.append(ln)
        if cur_table:
            out_blocks.append("\n".join(cur_table))
        if cur_prose:
            prose_txt = "\n".join(cur_prose).strip()
            if prose_txt:
                out_blocks.append(f"{open_tag}\n{prose_txt}\n</div>")
        return "\n\n".join(out_blocks)

    content = re.sub(
        r'(<div\s+class=["\']admonition[^"\']*["\']\s*>)(.*?)</div\s*>',
        _split_admonition_tables,
        content,
        flags=re.DOTALL | re.IGNORECASE,
    )
    # Strip admonition note divs from the PDF (any tables inside were already split out above)
    content = re.sub(
        r'<div\s+class=["\']admonition[^"\']*["\']\s*>.*?</div\s*>',
        '',
        content,
        flags=re.DOTALL | re.IGNORECASE,
    )

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
    fig_counter = 0

    lines = content.split("\n")
    i = 0
    num_lines = len(lines)
    is_first_h1 = True
    last_h1_bm_level = 0

    while i < num_lines:
        line = lines[i].rstrip()

        # Empty line
        if not line:
            i += 1
            continue

        # Horizontal Rule (skip standalone markdown section dividers so only H1 chapter headers have rules)
        if re.match(r'^(?:---|\*\*\*|___)\s*$', line):
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
            div_text = re.sub(r'<a\b[^>]*>(.*?)</a>', r'**\1**', div_text, flags=re.IGNORECASE | re.DOTALL)
            div_text = re.sub(r'<p\s+class=["\']admonition-title["\']>\s*(.*?)\s*</p>', r'**\1**\n', div_text, flags=re.IGNORECASE | re.DOTALL)
            div_text = re.sub(
                r'<li>\s*(.*?)\s*</li>',
                lambda m: '\n• ' + re.sub(r'\s+', ' ', m.group(1)) + '\n',
                div_text,
                flags=re.IGNORECASE | re.DOTALL,
            )
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
            if is_centered_caption_div or re.match(r'^(?:\*|_)?Figure\s+[A-Za-z0-9]', flat_clean):
                if flat_clean:
                    fig_counter += 1
                    fig_label = f"Figure {eq_prefix}.{fig_counter}"
                    clean_cap_div = re.sub(r'^(?:\*|_)?Figure(?:\s+[A-Za-z0-9.]+)?:\s*', '', flat_clean, flags=re.IGNORECASE).strip('*_ ')
                    cap_san = sanitize_inline_markdown(clean_cap_div, is_sc32)
                    elements.append(make_paragraph(f"<font face='{FONT_BODY_BOLD}' color='{TEXT_MAIN}'><b>{fig_label}:</b></font> <i>{cap_san}</i>", styles["FigureCaption"]))
                    elements.append(Spacer(1, 4))
                continue
            div_rows = []
            div_plain_lines = []
            for raw_dl in clean_text.split("\n"):
                raw_dl = re.sub(r'^\s*>\s*', '', raw_dl)
                dl_clean = re.sub(r'\s+', ' ', raw_dl).strip()
                if dl_clean:
                    dl_clean = re.sub(r'^#{1,6}\s+(.*)$', r'**\1**', dl_clean)
                    dl_clean = re.sub(r'^[\*\-]\s+(.*)$', r'• \1', dl_clean)
                    dl_san = sanitize_inline_markdown(dl_clean, is_sc32)
                    div_rows.append([make_paragraph(dl_san, styles["CalloutText"])])
                    div_plain_lines.append(dl_clean)
            if len(div_rows) == 1 and re.match(r'^\*\*[^*]+\*\*$', div_plain_lines[0].strip()):
                raw_t = div_plain_lines[0].strip().strip('*').strip()
                t_san = sanitize_inline_markdown(raw_t, is_sc32)
                h4_p = make_paragraph(t_san, styles["Heading4"])
                h4_p.keepWithNext = True
                elements.append(h4_p)
            elif div_rows:
                d_style = [
                    ('BACKGROUND', (0,0), (-1,-1), to_color(CALLOUT_BG_SC32 if is_sc32 else CALLOUT_BG_SC6)),
                    ('LINEBEFORE', (0,0), (0,-1), 2.5, to_color(primary_hex)),
                    ('BOX', (0,0), (-1,-1), 0.5, to_color(DIVIDER_HEX)),
                    ('LEFTPADDING', (0,0), (-1,-1), 8),
                    ('RIGHTPADDING', (0,0), (-1,-1), 8),
                    ('TOPPADDING', (0,0), (-1,-1), 2),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
                    ('TOPPADDING', (0,0), (-1,0), 5),
                    ('BOTTOMPADDING', (0,-1), (-1,-1), 5),
                ]
                if len(div_rows) <= (4 if is_sc32 else 10) and sum(len(s) for s in div_plain_lines) < (520 if is_sc32 else 1600):
                    d_style.append(('NOSPLIT', (0, 0), (-1, -1)))
                else:
                    d_style.append(('NOSPLIT', (0, 0), (-1, min(1, len(div_rows) - 1))))
                    d_style.append(('NOSPLIT', (0, max(0, len(div_rows) - 2)), (-1, -1)))
                    for r_idx, pl in enumerate(div_plain_lines[:-1]):
                        if pl.rstrip('* ').endswith(':'):
                            d_style.append(('NOSPLIT', (0, r_idx), (-1, r_idx + 1)))
                callout_tbl = Table(div_rows, colWidths=[PRINTABLE_WIDTH], splitByRow=1)
                callout_tbl.setStyle(TableStyle(d_style))
                callout_tbl.spaceBefore = 2.5
                callout_tbl.spaceAfter = 3.5
                if len(div_rows) <= 10:
                    callout_tbl._is_latex_float = True
                elements.append(callout_tbl)
            continue

        # Blockquote / Note / Callout (e.g. > [!NOTE] or > note: strip from PDF while keeping in source)
        if line.startswith(">"):
            while i < num_lines and lines[i].startswith(">"):
                i += 1
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

            # Soft-wrap any non-diagram code line > 74 chars so code never overflows the 6x9 printable margin
            wrapped_code_lines = []
            MAX_CODE_COLS = 74
            for cl in code_lines:
                cl_exp = cl.replace("\t", "    ")
                if len(cl_exp) <= MAX_CODE_COLS:
                    wrapped_code_lines.append(cl_exp)
                elif re.match(r'^\s*//\s*=+\s*$', cl_exp):
                    wrapped_code_lines.append(cl_exp[:MAX_CODE_COLS])
                else:
                    indent_m = re.match(r'^(\s*)', cl_exp)
                    base_indent = indent_m.group(1) if indent_m else ""
                    cont_indent = base_indent + ("// " if cl_exp.lstrip().startswith("//") else "    ")
                    rem = cl_exp
                    while len(rem) > MAX_CODE_COLS:
                        cut = MAX_CODE_COLS
                        for sep in (" ", ", ", "; ", " + ", " - "):
                            pos = rem.rfind(sep, len(base_indent) + 10, MAX_CODE_COLS)
                            if pos != -1:
                                cut = pos + len(sep)
                                break
                        wrapped_code_lines.append(rem[:cut].rstrip())
                        rem = cont_indent + rem[cut:].lstrip()
                    if rem.strip():
                        wrapped_code_lines.append(rem)
            code_lines = wrapped_code_lines

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
                    inner_line = inner_line.replace(r'\$', '\x00DOLLAR\x00')
                    inner_line = re.sub(r'\{\{[^}]+\}\}', lambda m: m.group(0).replace('|', '\x00PIPE\x00'), inner_line)
                    inner_line = re.sub(r'`[^`]+`', lambda m: m.group(0).replace('|', '\x00PIPE\x00'), inner_line)
                    inner_line = re.sub(r'\[[^\]]+\]', lambda m: m.group(0).replace('|', '\x00PIPE\x00'), inner_line)
                    inner_line = re.sub(r'\$(?:(?!\s+\|\s+)[^\$\n])+\$', lambda m: m.group(0).replace('|', '\x00PIPE\x00'), inner_line)
                    raw_cells = [c.replace('\x00PIPE\x00', '|').replace('\x00DOLLAR\x00', r'\$').strip() for c in inner_line.split('|')]
                    parsed_rows.append((r_idx == 0, raw_cells))

                if parsed_rows:
                    # Drop redundant leading Step/# column on 7-column 4-register stack trace tables
                    # so all stack trace tables share a uniform 6-column layout.
                    first_hdr = parsed_rows[0][1]
                    if (
                        len(first_hdr) >= 6
                        and re.match(r'^\*?(?:Step|#)\*?$', first_hdr[0].strip(), flags=re.IGNORECASE)
                        and sum(
                            1 for hc in first_hdr[1:]
                            if re.match(r'^\*?(?:Register\s+[TZYX]|[TZYX])\*?$', hc.strip(), flags=re.IGNORECASE)
                        ) >= 3
                    ):
                        parsed_rows = [(is_h, rc[1:]) for is_h, rc in parsed_rows if len(rc) >= 2]

                    hdr_cols = len(parsed_rows[0][1])
                    num_cols = hdr_cols if hdr_cols >= 2 else max(len(cells) for _, cells in parsed_rows)
                    normalized_data = []
                    col_char_counts = [1] * num_cols
                    col_min_widths = [24.0] * num_cols
                    hdr_min_widths = [24.0] * num_cols
                    exact_floors = [20.0] * num_cols
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
                            if is_hdr:
                                # Ensure inline math ($Y, X$) and code inside header rows inherit TableHeader text color
                                sanitized = re.sub(r"\s*color=['\"][^'\"]*['\"]", "", sanitized)
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

                            words = [w for w in re.split(r'[ \t\n]+', plain_cell) if w]
                            longest_w = max((len(w) for w in words), default=0)
                            if is_hdr:
                                hdr_floor = min(68.0, longest_w * 4.55 + 8.5)
                                hdr_min_widths[c_idx] = max(hdr_min_widths[c_idx], hdr_floor)
                                col_min_widths[c_idx] = max(col_min_widths[c_idx], hdr_floor)
                            else:
                                word_floor = longest_w * 4.20 + 8.0
                                col_min_widths[c_idx] = max(col_min_widths[c_idx], min(88.0, word_floor))

                            cell_style = styles["TableHeader"] if is_hdr else styles["TableCell"]
                            cell_para = make_paragraph(sanitized, cell_style)
                            try:
                                fw = rl_para._getFragWords(cell_para.frags)
                                mw = max((w[0] for w in fw), default=0.0)
                                # Add 7.5pt (3.5pt left + 3.5pt right cell padding + 0.5pt safety margin)
                                exact_floors[c_idx] = max(exact_floors[c_idx], mw + 7.5)
                            except Exception:
                                pass
                            row_elements.append(cell_para)
                        normalized_data.append(row_elements)

                    # Special compact sizing for 4-register stack columns and Step column
                    for c_idx in range(num_cols):
                        if is_step_col[c_idx]:
                            col_min_widths[c_idx] = max(20.0, exact_floors[c_idx])
                            hdr_min_widths[c_idx] = max(20.0, exact_floors[c_idx])
                            col_char_counts[c_idx] = min(col_char_counts[c_idx], 3)
                        elif is_stack_col[c_idx]:
                            col_min_widths[c_idx] = max(32.0, exact_floors[c_idx], min(62.0, col_char_counts[c_idx] * 4.45 + 8.5))
                            hdr_min_widths[c_idx] = max(hdr_min_widths[c_idx], col_min_widths[c_idx], exact_floors[c_idx])
                        else:
                            col_min_widths[c_idx] = max(col_min_widths[c_idx], exact_floors[c_idx])
                            hdr_min_widths[c_idx] = max(hdr_min_widths[c_idx], exact_floors[c_idx])

                    # Scale down col_min_widths proportionally if their sum exceeds 88% of PRINTABLE_WIDTH,
                    # while never shrinking any column below its exact word floor (exact_floors)
                    min_sum = sum(col_min_widths)
                    if min_sum > PRINTABLE_WIDTH * 0.88:
                        scale_f = (PRINTABLE_WIDTH * 0.88) / min_sum
                        col_min_widths = [
                            max(exact_floors[c_i], hdr_min_widths[c_i], mw * scale_f)
                            for c_i, mw in enumerate(col_min_widths)
                        ]
                    if sum(col_min_widths) > PRINTABLE_WIDTH:
                        ef_sum = sum(exact_floors)
                        if ef_sum <= PRINTABLE_WIDTH:
                            slack = PRINTABLE_WIDTH - ef_sum
                            extra_req = sum(max(0.0, col_min_widths[c] - exact_floors[c]) for c in range(num_cols))
                            if extra_req > 0:
                                col_min_widths = [
                                    exact_floors[c] + slack * (max(0.0, col_min_widths[c] - exact_floors[c]) / extra_req)
                                    for c in range(num_cols)
                                ]
                            else:
                                col_min_widths = list(exact_floors)
                        else:
                            s_ef = PRINTABLE_WIDTH / ef_sum
                            col_min_widths = [ef * s_ef for ef in exact_floors]
                            exact_floors = list(col_min_widths)

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

                    # Final normalization that strictly preserves exact_floors[c] so no word ever splits or overflows
                    w_sum = sum(col_widths)
                    if w_sum > PRINTABLE_WIDTH + 0.01:
                        excess = w_sum - PRINTABLE_WIDTH
                        reducible = [max(0.0, col_widths[c] - exact_floors[c]) for c in range(num_cols)]
                        red_sum = sum(reducible)
                        if red_sum >= excess and red_sum > 0:
                            col_widths = [col_widths[c] - excess * (reducible[c] / red_sum) for c in range(num_cols)]
                        else:
                            col_widths = [(w / w_sum) * PRINTABLE_WIDTH for w in col_widths]
                    elif w_sum < PRINTABLE_WIDTH - 0.01:
                        deficit = PRINTABLE_WIDTH - w_sum
                        col_widths = [col_widths[c] + deficit * (weights[c] / total_weight) for c in range(num_cols)]

                    nosplit_end = min(2, len(normalized_data) - 1)
                    tbl_styles = [
                        ('BACKGROUND', (0,0), (-1,0), to_color("#e4e4e7")),
                        ('TEXTCOLOR', (0,0), (-1,0), to_color(TEXT_MAIN)),
                        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                        ('TOPPADDING', (0,0), (-1,-1), 2.0),
                        ('BOTTOMPADDING', (0,0), (-1,-1), 2.0),
                        ('LEFTPADDING', (0,0), (-1,-1), 3.5),
                        ('RIGHTPADDING', (0,0), (-1,-1), 3.5),
                        ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, to_color("#f8fafc")]),
                        ('GRID', (0,0), (-1,-1), 0.5, to_color(DIVIDER_HEX)),
                        ('LINEABOVE', (0,0), (-1,0), 1.2, to_color(primary_hex)),
                        ('LINEBELOW', (0,0), (-1,0), 1.0, to_color(primary_hex)),
                        ('BOX', (0,0), (-1,-1), 0.85, to_color(primary_hex)),
                    ]
                    total_tbl_chars = sum(len(str(c)) for r in table_lines for c in r)
                    is_compact_table = (
                        (len(normalized_data) <= 8 and total_tbl_chars < 950)
                        if is_sc32
                        else (len(normalized_data) <= 8 and total_tbl_chars < 950)
                    )
                    if is_compact_table:
                        tbl_styles.append(('NOSPLIT', (0, 0), (-1, -1)))
                    else:
                        tbl_styles.append(('NOSPLIT', (0, 0), (-1, nosplit_end)))
                        tbl_styles.append(('NOSPLIT', (0, max(0, len(normalized_data) - 2)), (-1, -1)))
                    reportlab_table = Table(normalized_data, colWidths=col_widths, repeatRows=1)
                    reportlab_table.setStyle(TableStyle(tbl_styles))
                    reportlab_table.spaceBefore = 2.5
                    reportlab_table.spaceAfter = 3.5
                    if is_compact_table:
                        # Mark table as a LaTeX [ht] float so it stays intact while allowing following prose to flow
                        # into the bottom of the current page if the table itself does not fit in the remaining space.
                        if elements and isinstance(elements[-1], Paragraph) and getattr(getattr(elements[-1], "style", None), "name", "") in ("Heading3", "Heading4"):
                            hdr_group: List[Flowable] = [elements.pop()]
                            if elements and isinstance(elements[-1], BookmarkFlowable):
                                hdr_group.insert(0, elements.pop())
                            hdr_group.append(reportlab_table)
                            kt = KeepTogether(hdr_group)
                            kt._is_latex_float = True
                            elements.append(kt)
                        else:
                            reportlab_table._is_latex_float = True
                            elements.append(reportlab_table)
                    else:
                        if elements and isinstance(elements[-1], Paragraph) and getattr(getattr(elements[-1], "style", None), "name", "") in ("Heading2", "Heading3", "Heading4"):
                            elements[-1].keepWithNext = False
                        elements.append(reportlab_table)
            continue

        # Heading 1 (# Chapter Title or # Unit Title)
        if line.startswith("# "):
            title = line[2:].strip()
            plain_title, styled_title = format_heading_text(title, is_sc32=is_sc32)

            m_unit_h1 = re.match(r"^Unit\s+([IVX]+)\b", plain_title, flags=re.IGNORECASE)
            m_ch_h1 = re.match(r"^Chapter\s+(\d+)\b", plain_title, flags=re.IGNORECASE)
            if m_unit_h1:
                eq_prefix = m_unit_h1.group(1).upper()
                eq_counter = 0
                fig_counter = 0
            elif m_ch_h1:
                eq_prefix = m_ch_h1.group(1)
                eq_counter = 0
                fig_counter = 0

            if chapter_idx > 0 or not is_first_h1:
                elements.append(PageBreak())
            is_first_h1 = False

            elements.append(ChapterTracker(plain_title))

            bm_key = f"bm_ch_{chapter_idx}_{i}"
            toc_title = plain_title
            is_domain_subchapter = (kind == "domains" and bool(m_ch_h1))
            bm_level = 1 if is_domain_subchapter else 0
            last_h1_bm_level = bm_level
            elements.append(BookmarkFlowable(bm_key, toc_title, level=bm_level))

            h1_p = make_paragraph(styled_title, styles["Heading1"])
            h1_p._toc_info = (bm_level, toc_title, bm_key)
            terms = extract_index_terms(plain_title, is_sc32, term_counts, manual_kind=kind)
            if terms:
                h1_p._index_terms = terms
            elements.append(h1_p)
            hr_h1 = HRFlowable(width="100%", thickness=1.5, color=to_color(primary_hex), spaceBefore=2, spaceAfter=10)
            hr_h1.keepWithNext = True
            elements.append(hr_h1)
            i += 1
            continue

        # Heading 2 (## Section Title)
        if line.startswith("## "):
            title = line[3:].strip()
            plain_title, styled_title = format_heading_text(title, is_sc32=is_sc32)

            bm_key = f"bm_sec_{chapter_idx}_{i}"
            elements.append(BookmarkFlowable(bm_key, plain_title, level=min(last_h1_bm_level + 1, 2)))

            h2_p = make_paragraph(styled_title, styles["Heading2"])
            if kind != "domains" and not (is_sc32 and file_path.name.startswith("appendix-")):
                h2_p._toc_info = (1, plain_title, bm_key)
            terms = extract_index_terms(plain_title, is_sc32, term_counts, manual_kind=kind)
            if terms:
                h2_p._index_terms = terms
            elements.append(h2_p)
            i += 1
            continue

        # Heading 3 (### Sub-section Title)
        if line.startswith("### "):
            title = line[4:].strip()
            plain_title, styled_title = format_heading_text(title, is_sc32=is_sc32)

            bm_key = f"bm_sub_{chapter_idx}_{i}"
            elements.append(BookmarkFlowable(bm_key, plain_title, level=2))

            h3_p = make_paragraph(styled_title, styles["Heading3"])
            terms = extract_index_terms(plain_title, is_sc32, term_counts, manual_kind=kind)
            if terms:
                h3_p._index_terms = terms
            elements.append(h3_p)
            i += 1
            continue

        # Heading 4 (#### Sub-sub-section Title)
        if line.startswith("#### "):
            title = line[5:].strip()
            plain_title, styled_title = format_heading_text(title, is_sc32=is_sc32)

            h4_p = make_paragraph(styled_title, styles["Heading4"])
            terms = extract_index_terms(plain_title, is_sc32, term_counts, manual_kind=kind)
            if terms:
                h4_p._index_terms = terms
            elements.append(h4_p)
            i += 1
            continue

        # Bullet List (- or *)
        if re.match(r'^\s*[-*]\s+', line):
            list_items = []
            while i < num_lines and re.match(r'^\s*[-*]\s+', lines[i]):
                lead_spaces = len(lines[i]) - len(lines[i].lstrip())
                is_sub = lead_spaces >= 2
                item_parts = [re.sub(r'^\s*[-*]\s+', '', lines[i]).strip()]
                i += 1
                while (
                    i < num_lines
                    and lines[i].strip()
                    and re.match(r'^\s{2,}\S', lines[i])
                    and not re.match(r'^\s*[-*]\s+', lines[i])
                    and not re.match(r'^\s*\d+\.\s+', lines[i])
                    and not lines[i].strip().startswith(("```", "|", "$$", ">", "#", "---", "{{blocks:", "{{screenshot:", "!["))
                ):
                    item_parts.append(lines[i].strip())
                    i += 1
                list_items.append((is_sub, " ".join(item_parts)))

            keep_short_list = (not is_sc32) and len(list_items) <= 3 and sum(len(x[1]) for x in list_items) < 420
            last_keep = False
            for idx, (is_sub, itm) in enumerate(list_items):
                sanitized = sanitize_inline_markdown(itm, is_sc32)
                if is_sub:
                    bullet_p = make_paragraph(f"&ndash; &nbsp; {sanitized}", styles["ListSubBullet"])
                else:
                    bullet_p = make_paragraph(f"&bull; &nbsp; {sanitized}", styles["ListBullet"])
                next_is_sub = (idx < len(list_items) - 1) and list_items[idx + 1][0]
                if (not is_sub) and next_is_sub:
                    bullet_p.keepWithNext = True
                    last_keep = False
                elif not is_sc32 and itm.rstrip('*` ').endswith(':') and len(itm) < 220:
                    bullet_p.keepWithNext = True
                    last_keep = True
                elif not is_sc32 and idx < len(list_items) - 1 and (
                    keep_short_list
                    or (idx == 0 and len(itm) < 180 and len(list_items[idx + 1][1]) < 180)
                    or (idx == len(list_items) - 2 and len(itm) < 180 and len(list_items[idx + 1][1]) < 180)
                ):
                    bullet_p.keepWithNext = True
                    last_keep = False
                else:
                    last_keep = False
                elements.append(bullet_p)
            sp = Spacer(1, 3)
            if last_keep:
                sp.keepWithNext = True
            elements.append(sp)
            continue

        # Numbered List (1. 2. etc.)
        if re.match(r'^\s*\d+\.\s+', line):
            num_items = []
            while i < num_lines and re.match(r'^\s*(\d+)\.\s+', lines[i]):
                m = re.match(r'^\s*(\d+)\.\s+(.*)$', lines[i])
                i += 1
                if m:
                    num_str = m.group(1)
                    item_parts = [m.group(2).strip()]
                    while (
                        i < num_lines
                        and lines[i].strip()
                        and re.match(r'^\s{2,}\S', lines[i])
                        and not re.match(r'^\s*[-*]\s+', lines[i])
                        and not re.match(r'^\s*\d+\.\s+', lines[i])
                        and not lines[i].strip().startswith(("```", "|", "$$", ">", "#", "---", "{{blocks:", "{{screenshot:", "!["))
                    ):
                        item_parts.append(lines[i].strip())
                        i += 1
                    num_items.append((num_str, " ".join(item_parts)))

            keep_short_num_list = (not is_sc32) and len(num_items) <= 3 and sum(len(x[1]) for x in num_items) < 420
            last_keep = False
            for idx, (num_str, itm) in enumerate(num_items):
                sanitized = sanitize_inline_markdown(itm, is_sc32)
                num_p = make_paragraph(f"<b>{num_str}.</b> &nbsp; {sanitized}", styles["ListBullet"])
                if itm.rstrip('*` ').endswith(':') and len(itm) < (140 if is_sc32 else 220):
                    num_p.keepWithNext = True
                    last_keep = True
                elif not is_sc32 and idx < len(num_items) - 1 and (
                    keep_short_num_list
                    or (idx == 0 and len(itm) < 180 and len(num_items[idx + 1][1]) < 180)
                    or (idx == len(num_items) - 2 and len(itm) < 180 and len(num_items[idx + 1][1]) < 180)
                ):
                    num_p.keepWithNext = True
                    last_keep = False
                else:
                    last_keep = False
                elements.append(num_p)
            sp = Spacer(1, 3)
            if last_keep:
                sp.keepWithNext = True
            elements.append(sp)
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
                MANUALS_ASSETS_DIR / "diagrams" / "domains" / Path(raw_path).name,
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
            explicit_caption_line = ""
            look_j = i + 1
            while look_j < num_lines and not lines[look_j].strip():
                look_j += 1
            if look_j < num_lines:
                nxt_s = lines[look_j].strip()
                if re.match(r'^(?:\*|_)?Figure\s+[A-Za-z0-9]', nxt_s):
                    has_explicit_next_caption = True
                    explicit_caption_line = nxt_s
                elif nxt_s.startswith("<div") and ("text-align: center" in "\n".join(lines[look_j:look_j+5]) or "Figure " in "\n".join(lines[look_j:look_j+5])):
                    has_explicit_next_caption = True

            if resolved_img:
                try:
                    import io
                    from PIL import ImageOps, ImageDraw
                    with PIL.Image.open(resolved_img) as pimg:
                        work_img = pimg
                        orig_w, orig_h = work_img.size
                        is_sc32_bezel_crop = (
                            is_sc32
                            and "screenshots" in str(resolved_img)
                            and orig_h > orig_w * 1.4
                            and "hero_stack" not in resolved_img.name
                            and "plot_" not in resolved_img.name
                        )
                        is_sc32_plot_crop = (
                            is_sc32
                            and "screenshots" in str(resolved_img)
                            and "plot_" in resolved_img.name
                        )
                        if is_sc32_bezel_crop:
                            work_img = work_img.crop(
                                (
                                    int(orig_w * 0.04),
                                    int(orig_h * 0.038),
                                    int(orig_w * 0.96),
                                    int(orig_h * 0.302),
                                )
                            )
                            orig_w, orig_h = work_img.size
                            max_w = 215.0
                            max_h = 85.0
                        elif is_sc32_plot_crop:
                            y0_crop = int(orig_h * 0.048) if ("romberg" in resolved_img.name or "normal" in resolved_img.name) else 0
                            work_img = work_img.crop((0, y0_crop, orig_w, int(orig_h * 0.902)))
                            orig_w, orig_h = work_img.size
                            max_w = 215.0
                            max_h = 138.0
                        else:
                            max_w = PRINTABLE_WIDTH
                            if "diagram_" in resolved_img.name:
                                max_h = 160.0
                            else:
                                max_h = 135.0 if is_sc32 else 142.0
                        scale = min(max_w / orig_w, max_h / orig_h, 1.0)
                        w = orig_w * scale
                        h = orig_h * scale
                        if BW_PRINT_INTERIOR:
                            if "diagram_" in resolved_img.name:
                                gray_img = work_img.convert("L")
                            else:
                                gray_img = ImageOps.autocontrast(work_img.convert("L"), cutoff=1)
                            if is_sc32_plot_crop:
                                dr_p = ImageDraw.Draw(gray_img)
                                dr_p.rectangle([0, 0, gray_img.width - 1, gray_img.height - 1], outline=40, width=3)
                            img_buf = io.BytesIO()
                            gray_img.save(img_buf, format="PNG")
                            img_buf.seek(0)
                            rl_img = RLImage(img_buf, width=w, height=h)
                        elif is_sc32_bezel_crop or is_sc32_plot_crop:
                            img_buf = io.BytesIO()
                            work_img.save(img_buf, format="PNG")
                            img_buf.seek(0)
                            rl_img = RLImage(img_buf, width=w, height=h)
                        else:
                            rl_img = RLImage(str(resolved_img), width=w, height=h)
                    rl_img.hAlign = 'CENTER'
                    fig_items: List[Flowable] = [Spacer(1, 2), rl_img]
                    fig_counter += 1
                    fig_label = f"Figure {eq_prefix}.{fig_counter}"
                    if explicit_caption_line:
                        cap_clean = re.sub(r'^(?:\*|_)?Figure(?:\s+[A-Za-z0-9.]+)?:\s*', '', explicit_caption_line.strip("*_ ").strip(), flags=re.IGNORECASE).strip("*_ ")
                        cap_san = sanitize_inline_markdown(cap_clean, is_sc32)
                        fig_items.append(make_paragraph(f"<font face='{FONT_BODY_BOLD}' color='{TEXT_MAIN}'><b>{fig_label}:</b></font> <i>{cap_san}</i>", styles["FigureCaption"]))
                        fig_items.append(Spacer(1, 3))
                        i = look_j + 1
                    elif alt_text and not has_explicit_next_caption:
                        alt_clean = re.sub(r'^(?:\*|_)?Figure(?:\s+[A-Za-z0-9.]+)?:\s*', '', alt_text.strip(), flags=re.IGNORECASE).strip("*_ ")
                        alt_san = sanitize_inline_markdown(alt_clean, is_sc32)
                        fig_items.append(make_paragraph(f"<font face='{FONT_BODY_BOLD}' color='{TEXT_MAIN}'><b>{fig_label}:</b></font> <i>{alt_san}</i>", styles["FigureCaption"]))
                        fig_items.append(Spacer(1, 3))
                        i += 1
                    else:
                        fig_items.append(make_paragraph(f"<font face='{FONT_BODY_BOLD}' color='{TEXT_MAIN}'><b>{fig_label}</b></font>", styles["FigureCaption"]))
                        fig_items.append(Spacer(1, 3))
                        i += 1
                    if elements and isinstance(elements[-1], Paragraph) and getattr(getattr(elements[-1], "style", None), "name", "") in ("Heading2", "Heading3", "Heading4"):
                        hdr_prefix: List[Flowable] = [elements.pop()]
                        if elements and isinstance(elements[-1], BookmarkFlowable):
                            hdr_prefix.insert(0, elements.pop())
                        fig_items = hdr_prefix + fig_items
                    fig_kt = KeepTogether(fig_items)
                    fig_kt._is_latex_float = True
                    elements.append(fig_kt)
                    continue
                except Exception as ex:
                    print(f"[WARN] Failed to load image {resolved_img}: {ex}")
            else:
                elements.append(make_paragraph(f"<b>[FIGURE: {alt_text}]</b> (Source: {raw_path})", styles["CalloutText"]))
            i += 1
            continue

        # Standalone LaTeX Display Equation ($$ ... $$)
        if line.strip().startswith("$$") and line.strip().endswith("$$") and len(line.strip()) > 4:
            inner_disp = line.strip()[2:-2].strip()
            is_softkey_ribbon = inner_disp.startswith((r"\mathtt{[", r"\texttt{["))
            if is_softkey_ribbon:
                eq_label = ""
                bm_key = ""
            else:
                eq_counter += 1
                eq_label = f"Eq. {eq_prefix}.{eq_counter}"
                bm_key = f"bm_eq_{chapter_idx}_{eq_prefix}_{eq_counter}"
            eq_flowable = _render_latex_display_equation(line.strip(), eq_label, bm_key, styles, is_sc32)
            # Only glue a display equation to its following paragraph in Appendix D (where each
            # equation block is a tight header+formula+explanation unit) or when the next line
            # is a direct "where ..." variable-definition clause. Otherwise, alternating
            # colon-ending paragraphs and display equations chain transitively into 35-line blocks!
            next_eq_idx = i + 1
            while next_eq_idx < num_lines and not lines[next_eq_idx].strip():
                next_eq_idx += 1
            nxt_after_eq = lines[next_eq_idx].strip() if next_eq_idx < num_lines else ""
            if eq_prefix == "D" or nxt_after_eq.startswith("where "):
                eq_flowable.keepWithNext = True
            elements.append(eq_flowable)
            i += 1
            continue

        # Regular Paragraph
        para_lines = []
        while (
            i < num_lines
            and lines[i].strip()
            and not (para_lines and re.match(r'^\*\*[A-Za-z0-9][^\*\n]{1,50}:\*\*', lines[i].strip()))
            and not (para_lines and re.match(r'^\*[A-Za-z0-9][^\*\n]{1,50}:\*', lines[i].strip()))
            and not (para_lines and lines[i - 1].rstrip('\r\n').endswith("  "))
            and not (para_lines and re.match(r'^`[^`\n]+`$', lines[i].strip()))
            and not (para_lines and re.match(r'^`[^`\n]+`$', para_lines[-1]))
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
            if is_sc32 and "appendix-e" in file_path.stem.lower() and re.search(r"\.\s+(?:15|16|17|18|19|20)\d{2}\.", raw_para):
                bib_style = ParagraphStyle(
                    "SC32BibItem",
                    parent=styles["BodyText"],
                    leftIndent=14,
                    firstLineIndent=-14,
                    spaceAfter=3.8,
                )
                para_p = make_paragraph(sanitized, bib_style)
            else:
                para_p = make_paragraph(sanitized, styles["BodyText"])
            if re.match(r'^\*(?:Variables|RPN Sequence|Benchmark):\*', raw_para.strip()):
                para_p.keepWithNext = True
            elif raw_para.rstrip('*` ').endswith(':') and len(raw_para) <= 240:
                # Only glue a concise colon-ending lead-in paragraph (<= 240 chars) to the next flowable
                # if the next non-empty line is a compact table, display equation, figure, code block, heading,
                # or a concise list item (< 240 chars)—never a long multi-line narrative paragraph.
                next_idx = i
                while next_idx < num_lines and not lines[next_idx].strip():
                    next_idx += 1
                if next_idx < num_lines:
                    nxt = lines[next_idx].strip()
                    is_list_nxt = bool(re.match(r'^(?:[-*]|\d+\.)\s+', nxt))
                    is_short_table = False
                    if nxt.startswith("|"):
                        tbl_scan = next_idx
                        tbl_chars = 0
                        while tbl_scan < num_lines and lines[tbl_scan].strip().startswith("|"):
                            tbl_chars += len(lines[tbl_scan])
                            tbl_scan += 1
                        is_short_table = (tbl_scan - next_idx) <= 8 and tbl_chars < 950
                    if (
                        is_short_table
                        or nxt.startswith(("$$", "```", "#", "![", "<figure", ">", "{{blocks:"))
                        or ":screenshot" in nxt
                        or is_list_nxt
                    ):
                        para_p.keepWithNext = True
            terms = extract_index_terms(raw_para, is_sc32, term_counts, manual_kind=kind)
            if terms:
                para_p._index_terms = terms
            elements.append(para_p)
        elif i < num_lines:
            i += 1

    return elements


# ---------------------------------------------------------------------------
# Manual Compilation Orchestrator
# ---------------------------------------------------------------------------
def compile_manual_pdf(is_sc32: bool = True, manual_kind: Optional[str] = None) -> Path:
    """Compiles the SC-6 (Volume I), SC-32 (Volume II), or Domain Series (Volume III) KDP-compliant 6x9 trade interior manuscript PDF."""
    global _ACTIVE_MANUAL_KIND
    kind = manual_kind or ("sc32" if is_sc32 else "sc6")
    _ACTIVE_MANUAL_KIND = kind
    if kind == "domains":
        is_sc32 = True
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if kind == "domains":
        pdf_filename = "sc-domains-manual.pdf"
    else:
        pdf_filename = "sc32-scientific-manual.pdf" if is_sc32 else "sc6-elementary-manual.pdf"
    output_pdf_path = OUTPUT_DIR / pdf_filename

    print(f"\n=======================================================")
    print(f"Compiling KDP 6x9 Interior Manuscript: {output_pdf_path.name}")
    print(f"=======================================================")

    if kind == "domains":
        primary_hex = DOMAINS_PRIMARY
        accent_hex = DOMAINS_ACCENT
        cover_bg_hex = DOMAINS_COVER_BG
        cover_accent_hex = DOMAINS_COVER_ACCENT
        doc_code = "STK-REF-DOM-V3"
    else:
        primary_hex = SC32_PRIMARY if is_sc32 else SC6_PRIMARY
        accent_hex = SC32_ACCENT if is_sc32 else SC6_ACCENT
        cover_bg_hex = SC32_COVER_BG if is_sc32 else SC6_COVER_BG
        cover_accent_hex = SC32_COVER_ACCENT if is_sc32 else SC6_COVER_ACCENT
        doc_code = "STK-REF-32-V2" if is_sc32 else "STK-REF-06-V1"

    # Style Sheet Setup (Calibrated for 6x9 Trade Paperback & Hardcover with Full Justification)
    styles = getSampleStyleSheet()

    styles["Heading1"].fontName = FONT_BODY_BOLD
    styles["Heading1"].fontSize = 15.5
    styles["Heading1"].leading = 19.0
    styles["Heading1"].textColor = to_color(primary_hex)
    styles["Heading1"].keepWithNext = True
    styles["Heading1"].spaceBefore = 0
    styles["Heading1"].spaceAfter = 4
    styles["Heading1"].spaceShrinkage = 0.0

    styles["Heading2"].fontName = FONT_BODY_BOLD
    styles["Heading2"].fontSize = 11.4
    styles["Heading2"].leading = 14.0
    styles["Heading2"].textColor = to_color(primary_hex)
    styles["Heading2"].keepWithNext = True
    styles["Heading2"].spaceBefore = 7
    styles["Heading2"].spaceAfter = 2.5
    styles["Heading2"].spaceShrinkage = 0.0

    styles["Heading3"].fontName = FONT_BODY_BOLD
    styles["Heading3"].fontSize = 9.6
    styles["Heading3"].leading = 12.0
    styles["Heading3"].textColor = to_color(TEXT_MAIN)
    styles["Heading3"].keepWithNext = True
    styles["Heading3"].spaceBefore = 5
    styles["Heading3"].spaceAfter = 1.5
    styles["Heading3"].spaceShrinkage = 0.0

    styles["Heading4"].fontName = FONT_BODY_BOLD
    styles["Heading4"].fontSize = 8.6
    styles["Heading4"].leading = 10.8
    styles["Heading4"].textColor = to_color(TEXT_MUTED)
    styles["Heading4"].keepWithNext = True
    styles["Heading4"].spaceBefore = 4
    styles["Heading4"].spaceAfter = 1.5
    styles["Heading4"].spaceShrinkage = 0.0

    styles["BodyText"].fontName = FONT_BODY
    styles["BodyText"].fontSize = 8.3 if is_sc32 else 8.6
    styles["BodyText"].leading = 10.7 if is_sc32 else 11.4
    styles["BodyText"].alignment = 4  # TA_JUSTIFY (Full Trade Book Justification)
    styles["BodyText"].textColor = to_color(TEXT_MAIN)
    styles["BodyText"].spaceAfter = 2.0 if is_sc32 else 2.4
    styles["BodyText"].spaceShrinkage = 0.0

    styles.add(ParagraphStyle(
        "ListBullet",
        parent=styles["BodyText"],
        alignment=4,  # TA_JUSTIFY
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=1.5,
        spaceShrinkage=0.0,
    ))

    styles.add(ParagraphStyle(
        "ListSubBullet",
        parent=styles["BodyText"],
        alignment=4,  # TA_JUSTIFY
        leftIndent=22,
        firstLineIndent=-8,
        spaceAfter=1.5,
        spaceShrinkage=0.0,
    ))

    styles.add(ParagraphStyle(
        "TableHeader",
        parent=styles["Normal"],
        fontName=FONT_BODY_BOLD,
        fontSize=6.8,
        leading=8.5,
        textColor=to_color(TEXT_MAIN),
        spaceShrinkage=0.0,
    ))

    styles.add(ParagraphStyle(
        "TableCell",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=6.6,
        leading=8.2,
        textColor=to_color(TEXT_MAIN),
        spaceShrinkage=0.0,
    ))

    styles.add(ParagraphStyle(
        "CalloutText",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=7.9,
        leading=10.3,
        alignment=4,  # TA_JUSTIFY
        textColor=to_color(TEXT_MAIN),
        spaceShrinkage=0.0,
    ))

    styles.add(ParagraphStyle(
        "FigureCaption",
        parent=styles["Normal"],
        fontName=FONT_BODY_ITALIC,
        fontSize=7.3,
        leading=9.4,
        textColor=to_color(TEXT_MUTED),
        alignment=1,
        spaceBefore=1.5,
        spaceAfter=2.5,
        spaceShrinkage=0.0,
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
    if kind == "domains":
        manual_dir = MANUALS_ROOT / "domains"
        chapter_files = [
            "index.md",
            "01-sc35-geomatics-navigation.md",
            "02-sc14-electrical-trades.md",
            "03-sc16-systems-cyber.md",
            "04-sc24-cinema-broadcast.md",
            "05-sc50-rf-spectrum.md",
            "06-sc60-chemistry-wetlab.md",
            "07-sc78-culinary-brewing.md",
            "08-sc80-clinical-pharmacy.md",
            "09-sc95-finance-statistics.md",
            "appendix-a-cross-domain-formula-compendium.md",
            "appendix-b-domain-keycap-and-softkey-directory.md",
            "appendix-c-solutions-to-practice-problems.md",
        ]
        doc_title = "THE OPERATIVE STACK: Mathematics for the Real World"
    elif is_sc32:
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
    story.extend(build_kdp_front_matter(is_sc32, styles, manual_kind=kind))

    # 2. Table of Contents (Pages v–vi in lowercase Roman numerals, Two-Pass Auto-Updated with Dot Leaders)
    story.append(ChapterTracker("TABLE OF CONTENTS"))
    story.append(BookmarkFlowable("bm_toc", "Table of Contents", level=0))
    toc_heading = make_paragraph("Table of Contents", styles["Heading1"])
    story.append(toc_heading)
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=1.5, color=to_color(primary_hex), spaceAfter=10))

    toc = TableOfContents()
    toc.dotsMinLevel = 0
    if is_sc32:
        toc.tableStyle = TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0.35),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0.35),
        ])
    toc_level0 = ParagraphStyle(
        "TOCLevel0",
        parent=styles["Normal"],
        fontName=FONT_BODY_BOLD,
        fontSize=7.4 if is_sc32 else 8.4,
        leading=9.2 if is_sc32 else 11.2,
        rightIndent=12 if is_sc32 else 28,
        textColor=to_color(primary_hex),
        spaceBefore=2.2 if is_sc32 else 4,
        spaceAfter=0.4 if is_sc32 else 1,
    )
    toc_level1 = ParagraphStyle(
        "TOCLevel1",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=7.1 if is_sc32 else 7.6,
        leading=8.6 if is_sc32 else 9.8,
        leftIndent=10,
        rightIndent=24 if is_sc32 else 28,
        textColor=to_color(TEXT_MAIN),
        spaceBefore=0.3 if is_sc32 else 1.0,
        spaceAfter=0.2 if is_sc32 else 0.5,
    )
    toc_level2 = ParagraphStyle(
        "TOCLevel2",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=7.2,
        leading=9.2,
        leftIndent=18,
        rightIndent=28,
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
        ch_elements = parse_markdown_file(fpath, ch_idx, is_sc32, styles, term_counts, manual_kind=kind)
        story.extend(ch_elements)

    # 4. Alphabetical Subject Index (Two-Pass Auto-Updated A-Z)
    story.append(PageBreak())
    story.append(ChapterTracker("SUBJECT INDEX"))
    story.append(BookmarkFlowable("bm_index", "Alphabetical Subject Index", level=0))
    idx_heading = make_paragraph("Alphabetical Subject Index", styles["Heading1"])
    story.append(idx_heading)
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=1.5, color=to_color(primary_hex), spaceAfter=10))

    class NoOrphanSimpleIndex(SimpleIndex):
        """Subclass of ReportLab SimpleIndex that binds each A–Z letter heading to its first entry and renders [KEY] as Paper keycaps."""
        def _build(self, availWidth, availHeight):
            super()._build(availWidth, availHeight)
            tbl = getattr(self, "_flowable", None)
            if tbl is not None and hasattr(tbl, "_cellvalues"):
                rows = tbl._cellvalues
                for r in rows:
                    if len(r) == 1 and isinstance(r[0], Paragraph):
                        p_obj = r[0]
                        st_name = getattr(getattr(p_obj, "style", None), "name", "")
                        if st_name == "IndexEntryStyle":
                            raw_txt = getattr(p_obj, "text", "")
                            if "[" in raw_txt and "]" in raw_txt:
                                clean_raw = re.sub(r"<font\b[^>]*>(.*?)</font>", r"\1", raw_txt)
                                new_txt = re.sub(
                                    r"\[([^\]\n]{1,12})\]",
                                    lambda m_k: format_hardware_keycap_cartouche(m_k.group(1).strip(), is_sc32, target_h_pt=7.2),
                                    clean_raw,
                                )
                                new_txt = _protect_special_unicode_glyphs(new_txt)
                                r[0] = make_paragraph(new_txt, p_obj.style)
                merged_rows = []
                r_idx = 0
                while r_idx < len(rows):
                    # Detect pattern: [Spacer(spaceBefore)], [Paragraph(header, IndexAlphaHead)], [Spacer(spaceAfter)], [Paragraph(first_entry)]
                    if (
                        r_idx + 3 < len(rows)
                        and len(rows[r_idx]) == 1
                        and len(rows[r_idx + 1]) == 1
                        and isinstance(rows[r_idx + 1][0], Paragraph)
                        and getattr(getattr(rows[r_idx + 1][0], "style", None), "name", "") == "IndexAlphaHead"
                    ):
                        combined_cell = (
                            list(rows[r_idx])
                            + list(rows[r_idx + 1])
                            + list(rows[r_idx + 2])
                            + list(rows[r_idx + 3])
                        )
                        merged_rows.append([combined_cell])
                        r_idx += 4
                    else:
                        merged_rows.append(rows[r_idx])
                        r_idx += 1
                self._flowable = Table(merged_rows, colWidths=[availWidth], style=self.tableStyle)

    idx = NoOrphanSimpleIndex(dot=' . ')
    idx_head = ParagraphStyle(
        "IndexAlphaHead",
        parent=styles["Heading2"],
        fontName=FONT_BODY_BOLD,
        fontSize=9.8 if is_sc32 else 10.0,
        leading=11.5 if is_sc32 else 12.8,
        textColor=to_color(primary_hex),
        spaceBefore=4.0 if is_sc32 else 6,
        spaceAfter=1.0 if is_sc32 else 2,
        keepWithNext=True,
    )
    idx_entry = ParagraphStyle(
        "IndexEntryStyle",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=7.5 if is_sc32 else 7.6,
        leading=9.3 if is_sc32 else 10.0,
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
    sanitize_pdf_for_kdp_and_kindle(output_pdf_path)
    print(f"  ✓ Successfully compiled & sanitized: {output_pdf_path} ({output_pdf_path.stat().st_size:,} bytes)")

    # Generate Hardcover Interior Manuscript variant for SC-32, SC-6, and Domain Series
    compile_hardcover_interior_variant(output_pdf_path, is_sc32, styles, custom_canvas_maker, manual_kind=kind)

    return output_pdf_path


def sanitize_pdf_for_kdp_and_kindle(pdf_path: Path) -> None:
    """
    Strips all PDF non-visual meta information (/Info dictionary, /Outlines, /Names, /Dests,
    /StructTreeRoot, /MarkInfo, /Metadata, /OCProperties, /PieceInfo, /PageMode), page /Annots,
    and unused unembedded Type 1 Helvetica (/F1) font resources so KDP and Kindle Create
    transforms encounter only clean embedded TrueType fonts and page streams.
    Before stripping /Outlines, saves any hierarchical bookmark outline to a sidecar .outline.json
    so generate_manual_kpf.py can still populate the Kindle Print Replica TOC navigation.
    """
    import json
    import pypdf
    from pypdf.generic import NameObject

    try:
        reader = pypdf.PdfReader(str(pdf_path))
        outline_entries = []

        def _walk_outline(items, depth):
            for item in items:
                if isinstance(item, list):
                    _walk_outline(item, depth + 1)
                else:
                    try:
                        p_idx = reader.get_destination_page_number(item)
                    except Exception:
                        p_idx = 0
                    if p_idx is None:
                        p_idx = 0
                    t_str = " ".join(str(getattr(item, "title", "")).replace("\t", " ").split())
                    if t_str:
                        outline_entries.append([depth, int(p_idx), t_str])

        if reader.outline:
            _walk_outline(reader.outline, 0)
        if outline_entries:
            sidecar_path = pdf_path.with_suffix(".outline.json")
            sidecar_path.write_text(json.dumps(outline_entries, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass

    writer = pypdf.PdfWriter(clone_from=str(pdf_path))
    root = writer._root_object
    for k in (
        "/Outlines",
        "/Names",
        "/Dests",
        "/PageLabels",
        "/StructTreeRoot",
        "/MarkInfo",
        "/Metadata",
        "/OCProperties",
        "/PieceInfo",
        "/PageMode",
    ):
        if k in root:
            del root[NameObject(k)]

    if writer._info is not None:
        writer._info.get_object().clear()

    for pg in writer.pages:
        if "/Annots" in pg:
            del pg[NameObject("/Annots")]
        res = pg.get("/Resources")
        if res:
            res_obj = res.get_object()
            fonts = res_obj.get("/Font")
            if fonts:
                fonts_obj = fonts.get_object()
                embedded_ref = None
                for fk in list(fonts_obj.keys()):
                    f_obj = fonts_obj[fk].get_object()
                    if f_obj.get("/Subtype") != "/Type1":
                        embedded_ref = fonts_obj.raw_get(fk)
                        break
                for fk in list(fonts_obj.keys()):
                    f_obj = fonts_obj[fk].get_object()
                    if f_obj.get("/Subtype") == "/Type1":
                        if embedded_ref is not None:
                            fonts_obj[NameObject(fk)] = embedded_ref
                        else:
                            del fonts_obj[NameObject(fk)]

    with open(pdf_path, "wb") as f_out:
        writer.write(f_out)


def compile_hardcover_interior_variant(
    paperback_pdf_path: Path,
    is_sc32: bool,
    styles: Dict[str, ParagraphStyle],
    custom_canvas_maker,
    manual_kind: Optional[str] = None,
) -> Path:
    """
    Generates a separate Hardcover Interior Manuscript PDF
    whose Series Frontispiece (Page ii) and Copyright/Colophon (Page iv) carry the dedicated
    Hardcover ISBN-13, while preserving 100% of the interior layout.
    """
    import io
    import pypdf
    kind = manual_kind or ("sc32" if is_sc32 else "sc6")
    hc_front_buf = io.BytesIO()
    hc_doc = ManualDocTemplate(
        hc_front_buf,
        pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
        leftMargin=MARGIN_PT,
        rightMargin=MARGIN_PT,
        topMargin=MARGIN_PT,
        bottomMargin=MARGIN_PT,
    )
    hc_story = build_kdp_front_matter(is_sc32, styles, is_hardcover=True, manual_kind=kind)
    hc_doc.multiBuild(hc_story, canvasmaker=custom_canvas_maker, maxPasses=2)
    hc_front_buf.seek(0)
    hc_front_reader = pypdf.PdfReader(hc_front_buf)

    if kind == "domains":
        hc_pdf_path = OUTPUT_DIR / "sc-domains-manual-hardcover.pdf"
    else:
        hc_pdf_path = OUTPUT_DIR / ("sc32-scientific-manual-hardcover.pdf" if is_sc32 else "sc6-elementary-manual-hardcover.pdf")
    writer = pypdf.PdfWriter(clone_from=str(paperback_pdf_path))
    for pg_idx in (1, 3):  # Page ii (index 1) and Page iv (index 3)
        writer.pages[pg_idx].replace_contents(None)
        writer.pages[pg_idx].merge_page(hc_front_reader.pages[pg_idx])
    with open(hc_pdf_path, "wb") as f_out:
        writer.write(f_out)
    sanitize_pdf_for_kdp_and_kindle(hc_pdf_path)
    print(f"  ✓ Successfully compiled Hardcover Interior Manuscript: {hc_pdf_path} ({hc_pdf_path.stat().st_size:,} bytes)")
    return hc_pdf_path


def compile_full_wrap_cover_spread(
    is_sc32: bool = True,
    is_hardcover: bool = False,
    manual_kind: Optional[str] = None,
) -> Path:
    """
    Generates a standalone KDP-compliant 3-panel 6x9 Full-Wrap Cover + Spine Spread PDF:
    - Paperback (is_hardcover=False): 0.125 in outer bleed, 6.00 x 9.00 in panels, spine = pages * 0.002252 in.
    - Hardcover Case-Laminate (is_hardcover=True): 0.591 in (15 mm) outer wrap, 0.394 in (10 mm) spine hinges,
      5.866 x 9.236 in boards (6.260 in panel+hinge width), spine = (pages * 0.002252 in) + 0.189 in.
    Continuous Warm Archival Paper (#F7F4EB) across Front, Spine, and Back with zero barcode (reserved for KDP).
    """
    import pypdf
    kind = manual_kind or ("sc32" if is_sc32 else "sc6")
    if kind == "domains":
        is_sc32 = True
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if kind == "domains":
        manual_name = "sc-domains-manual.pdf"
    else:
        manual_name = "sc32-scientific-manual.pdf" if is_sc32 else "sc6-elementary-manual.pdf"
    manual_path = OUTPUT_DIR / manual_name
    actual_pages = 540 if kind == "domains" else (500 if is_sc32 else 440)
    if manual_path.exists():
        try:
            actual_pages = len(pypdf.PdfReader(str(manual_path)).pages)
        except Exception:
            pass

    if kind == "domains":
        spread_name = "sc-domains-hardcover-wrap-cover.pdf" if is_hardcover else "sc-domains-full-wrap-cover.pdf"
    elif is_hardcover:
        spread_name = "sc32-hardcover-wrap-cover.pdf" if is_sc32 else "sc6-hardcover-wrap-cover.pdf"
    else:
        spread_name = "sc32-full-wrap-cover.pdf" if is_sc32 else "sc6-full-wrap-cover.pdf"
    spread_path = OUTPUT_DIR / spread_name

    if is_hardcover:
        bleed_x = 0.591 * 72.0          # Official KDP Hardcover 0.591 in (15 mm) left/right turn-in wrap
        bleed_y = 0.591 * 72.0          # Official KDP Hardcover 0.591 in (15 mm) top/bottom turn-in wrap
        hinge_pt = 0.394 * 72.0         # Official KDP Hardcover 0.394 in (10 mm) spine hinge
        board_w = 5.866 * 72.0          # Official KDP Hardcover 5.866 in (149 mm) board width
        panel_w = board_w + hinge_pt    # 6.260 in (board + hinge) per cover side
        panel_h = 9.236 * 72.0          # Official KDP Hardcover 9.236 in (234.6 mm) board height
        spine_in = (actual_pages * 0.002252) + 0.189  # KDP Hardcover spine width (+0.189 in board allowance)
        spine_w = spine_in * 72.0
    else:
        bleed_x = 9.0                   # Official KDP Paperback 0.125 in (3.2 mm) outer bleed
        bleed_y = 9.0
        hinge_pt = 0.0
        panel_w = PAGE_WIDTH            # 432.0 pt (6.00 in trade trim width)
        panel_h = PAGE_HEIGHT           # 648.0 pt (9.00 in trade trim height)
        spine_in = actual_pages * 0.002252  # Official KDP White Paper spine formula
        spine_w = spine_in * 72.0

    total_w = (2.0 * panel_w) + spine_w + (2.0 * bleed_x)
    total_h = panel_h + (2.0 * bleed_y)

    paper_cream = "#F7F4EB"
    ink_obsidian = "#0F172A"
    if kind == "domains":
        cover_accent = DOMAINS_COVER_ACCENT
    else:
        cover_accent = "#FF4F00" if is_sc32 else "#059669"

    c = canvas.Canvas(str(spread_path), pagesize=(total_w, total_h))

    # Fill entire full-wrap canvas (including wraps, hinges, boards, and spine) with Warm Archival Paper
    c.setFillColor(to_color(paper_cream))
    c.rect(0.0, 0.0, total_w, total_h, fill=1, stroke=0)

    # Panel X coordinates (centering the 6.00 x 9.00 live art inside each board area away from the spine hinge)
    spine_x = bleed_x + panel_w
    art_y = bleed_y + (panel_h - PAGE_HEIGHT) * 0.5
    if is_hardcover:
        back_art_x = bleed_x + (board_w - PAGE_WIDTH) * 0.5
        front_art_x = spine_x + spine_w + hinge_pt + (board_w - PAGE_WIDTH) * 0.5
    else:
        back_art_x = bleed_x
        front_art_x = spine_x + spine_w

    # 1. LEFT PANEL: Minimalist Bestseller Back Cover
    draw_bestseller_back_cover(
        c, back_art_x, art_y, PAGE_WIDTH, PAGE_HEIGHT, is_sc32,
        total_pages=actual_pages,
        bleed_l=0.0, bleed_r=0.0, bleed_t=0.0, bleed_b=0.0,
        manual_kind=kind,
    )

    # 2. RIGHT PANEL: Minimalist Bestseller Front Cover
    draw_bestseller_front_cover(
        c, front_art_x, art_y, PAGE_WIDTH, PAGE_HEIGHT, is_sc32,
        bleed_l=0.0, bleed_r=0.0, bleed_t=0.0, bleed_b=0.0,
        manual_kind=kind,
    )

    # 3. CENTER PANEL: Continuous Warm Archival Paper Spine (with >= 0.0625 in / 4.5 pt safe margin)
    c.saveState()
    c.setFillColor(to_color(paper_cream))
    c.rect(spine_x, 0.0, spine_w, total_h, fill=1, stroke=0)

    if is_hardcover or (actual_pages >= 79 and spine_w >= 12.5):
        spine_cx = spine_x + (spine_w / 2.0)
        base_y = bleed_y

        # Minimalist geometric accent bar at top of spine
        mark_w = max(4.0, min(spine_w - 10.0, 26.0))
        c.setFillColor(to_color(cover_accent))
        c.roundRect(spine_cx - mark_w * 0.5, base_y + panel_h - 62.0, mark_w, 6.0, 2.0, fill=1, stroke=0)

        # Vertical Rotated Spine Title (Standard US Top-to-Bottom Spine Orientation: -90 deg)
        spine_font_sz = min(13.5, max(7.0, (spine_w - 9.0) * 0.82))
        c.saveState()
        c.translate(spine_cx, base_y + (panel_h * 0.52))
        c.rotate(-90)
        c.setFillColor(to_color(ink_obsidian))
        c.setFont(FONT_BODY_BOLD, spine_font_sz)
        if kind == "domains":
            spine_main = "THE OPERATIVE STACK"
        else:
            spine_main = (
                "THINKING IN THE STACK"
                if is_sc32 else
                "FROM BLOCKS TO THE STACK"
            )
        c.drawCentredString(0.0, -spine_font_sz * 0.33, spine_main)
        c.restoreState()

        # Bottom Spine Company Imprint ('StackCalc' rotated inside safe zone)
        imp_font_sz = min(10.5, max(6.5, (spine_w - 9.0) * 0.72))
        c.saveState()
        c.translate(spine_cx, base_y + 82.0)
        c.rotate(-90)
        c.setFillColor(to_color(cover_accent))
        c.circle(-38.0, 0.0, min(2.5, spine_font_sz * 0.2), fill=1, stroke=0)
        c.setFillColor(to_color(ink_obsidian))
        c.setFont(FONT_BODY_BOLD, imp_font_sz)
        c.drawCentredString(0.0, -imp_font_sz * 0.33, "StackCalc")
        c.restoreState()

    c.restoreState()

    c.showPage()
    c.save()
    sanitize_pdf_for_kdp_and_kindle(spread_path)
    kind_lbl = "Hardcover Case-Laminate" if is_hardcover else "Paperback Full-Wrap"
    print(
        f"  ✓ Successfully compiled KDP 6x9 {kind_lbl} Cover + Spine Spread: {spread_path.name} "
        f"({actual_pages} pp -> spine {spine_in:.3f} in, total {total_w/72.0:.3f} x {total_h/72.0:.3f} in, {spread_path.stat().st_size:,} bytes)"
    )
    return spread_path


def compile_lulu_coil_cover_spread(
    is_sc32: bool = True,
    manual_kind: Optional[str] = None,
) -> Path:
    """
    Generates a standalone 2-page Lulu Coil-Bound Cover PDF (6.25" x 9.25" with 0.125" full bleed
    around 6.00" x 9.00" trade trim). Page 1 = Front Cover, Page 2 = Back Cover.
    """
    import pypdf
    kind = manual_kind or ("sc32" if is_sc32 else "sc6")
    if kind == "domains":
        is_sc32 = True
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if kind == "domains":
        manual_name = "sc-domains-manual.pdf"
        lulu_name = "sc-domains-lulu-cover.pdf"
    elif is_sc32:
        manual_name = "sc32-scientific-manual.pdf"
        lulu_name = "sc32-lulu-cover.pdf"
    else:
        manual_name = "sc6-elementary-manual.pdf"
        lulu_name = "sc6-lulu-cover.pdf"

    manual_path = OUTPUT_DIR / manual_name
    actual_pages = 540 if kind == "domains" else (500 if is_sc32 else 440)
    if manual_path.exists():
        try:
            actual_pages = len(pypdf.PdfReader(str(manual_path)).pages)
        except Exception:
            pass

    lulu_path = OUTPUT_DIR / lulu_name
    bleed = 9.0
    page_w = PAGE_WIDTH + 2.0 * bleed
    page_h = PAGE_HEIGHT + 2.0 * bleed

    c = canvas.Canvas(str(lulu_path), pagesize=(page_w, page_h))
    draw_bestseller_front_cover(
        c, bleed, bleed, PAGE_WIDTH, PAGE_HEIGHT, is_sc32,
        bleed_l=bleed, bleed_r=bleed, bleed_t=bleed, bleed_b=bleed,
        manual_kind=kind,
    )
    c.showPage()
    draw_bestseller_back_cover(
        c, bleed, bleed, PAGE_WIDTH, PAGE_HEIGHT, is_sc32,
        total_pages=actual_pages,
        bleed_l=bleed, bleed_r=bleed, bleed_t=bleed, bleed_b=bleed,
        manual_kind=kind,
    )
    c.showPage()
    c.save()
    sanitize_pdf_for_kdp_and_kindle(lulu_path)
    print(f"  ✓ Successfully compiled Lulu 2-Page Coil-Bound Cover: {lulu_path.name} ({lulu_path.stat().st_size:,} bytes)")
    return lulu_path


def rasterize_pdf_to_jpg(pdf_path: Path, jpg_path: Path, dpi: int = 300) -> Path:
    """
    Rasterizes a single-page front-cover PDF into a 300 DPI RGB JPEG for Amazon KDP Kindle eBook / Print Replica upload.
    """
    import shutil
    import subprocess
    jpg_path.parent.mkdir(parents=True, exist_ok=True)
    pdftoppm_bin = shutil.which("pdftoppm")
    if pdftoppm_bin:
        prefix = str(jpg_path.with_suffix(""))
        subprocess.run(
            [
                pdftoppm_bin,
                "-jpeg",
                "-jpegopt",
                "quality=95",
                "-r",
                str(dpi),
                "-singlefile",
                str(pdf_path),
                prefix,
            ],
            check=True,
        )
        return jpg_path

    magick_bin = shutil.which("magick")
    if magick_bin:
        subprocess.run(
            [
                magick_bin,
                "-density",
                str(dpi),
                f"{pdf_path}[0]",
                "-colorspace",
                "sRGB",
                "-quality",
                "95",
                str(jpg_path),
            ],
            check=True,
        )
        return jpg_path

    sips_bin = shutil.which("sips")
    if sips_bin:
        subprocess.run(
            [
                sips_bin,
                "-s",
                "format",
                "jpeg",
                "-s",
                "formatOptions",
                "95",
                str(pdf_path),
                "--out",
                str(jpg_path),
            ],
            check=True,
            capture_output=True,
        )
        return jpg_path

    raise RuntimeError("No PDF-to-JPEG rasterizer found (expected pdftoppm, magick, or sips).")


def compile_kindle_front_cover(
    is_sc32: bool = True,
    dpi: int = 300,
    manual_kind: Optional[str] = None,
) -> Tuple[Path, Path]:
    """
    Generates the standalone Amazon KDP Kindle eBook / Print Replica Primary Front Cover:
      - Vector front-cover PDF (6.00 x 9.00 in / 432 x 648 pt, no spine or back cover):
        sc32-kindle-cover.pdf, sc6-kindle-cover.pdf, or sc-domains-kindle-cover.pdf
      - High-resolution 300 DPI RGB JPEG (1800 x 2700 px):
        sc32-kindle-cover.jpg, sc6-kindle-cover.jpg, or sc-domains-kindle-cover.jpg
    """
    kind = manual_kind or ("sc32" if is_sc32 else "sc6")
    if kind == "domains":
        is_sc32 = True
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if kind == "domains":
        stem = "sc-domains-kindle-cover"
    else:
        stem = "sc32-kindle-cover" if is_sc32 else "sc6-kindle-cover"
    pdf_path = OUTPUT_DIR / f"{stem}.pdf"
    jpg_path = OUTPUT_DIR / f"{stem}.jpg"

    c = canvas.Canvas(str(pdf_path), pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    draw_bestseller_front_cover(
        c,
        0.0,
        0.0,
        PAGE_WIDTH,
        PAGE_HEIGHT,
        is_sc32=is_sc32,
        bleed_l=0.0,
        bleed_r=0.0,
        bleed_t=0.0,
        bleed_b=0.0,
        manual_kind=kind,
    )
    c.showPage()
    c.save()
    sanitize_pdf_for_kdp_and_kindle(pdf_path)

    rasterize_pdf_to_jpg(pdf_path, jpg_path, dpi=dpi)
    with PIL.Image.open(jpg_path) as im:
        px_w, px_h = im.size
    print(
        f"  ✓ Successfully compiled Kindle Primary Front Cover: {jpg_path.name} "
        f"({px_w}x{px_h} px @ {dpi} DPI, {jpg_path.stat().st_size:,} bytes) & {pdf_path.name}"
    )
    return pdf_path, jpg_path


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate publication-grade PDFs for StackCalc manuals.")
    parser.add_argument("--sc32-only", action="store_true", help="Compile only the SC-32 Scientific manual.")
    parser.add_argument("--sc6-only", action="store_true", help="Compile only the SC-6 Elementary manual.")
    parser.add_argument("--domains-only", action="store_true", help="Compile only the Volume III Domain Series manual.")
    parser.add_argument("--covers-only", action="store_true", help="Compile only the Print & Kindle covers.")
    parser.add_argument("--min-pages", type=int, default=240, help="Minimum required page count (default: 240).")
    args = parser.parse_args()

    build_all = not args.sc32_only and not args.sc6_only and not args.domains_only

    import shutil
    if (STACKCALC_ROOT / "docs" / "downloads").exists():
        (STACKCALC_ROOT / "docs" / "downloads" / "manuals").mkdir(parents=True, exist_ok=True)
    education_pdf_dir = WATCH_CALC_ROOT / "Education" / "output" / "pdf"
    mirror_out_dirs = [
        WATCH_CALC_ROOT / "Website" / "docs" / "manuals" / "output",
        WATCH_CALC_ROOT / "documentation" / "manuals" / "output" / "kdp_upload",
        STACKCALC_ROOT / "docs" / "manuals" / "output",
        STACKCALC_ROOT / "docs" / "manuals" / "output" / "kdp_upload",
        STACKCALC_ROOT / "docs" / "downloads" / "manuals",
        STACKCALC_ROOT / "Website" / "docs" / "manuals" / "output",
        STACKCALC_ROOT / "site" / "manuals" / "output",
        education_pdf_dir,
        education_pdf_dir / "kdp_upload",
        education_pdf_dir / "kdp_upload_ready",
    ]
    for kdp_dir in (
        WATCH_CALC_ROOT / "documentation" / "manuals" / "output" / "kdp_upload",
        STACKCALC_ROOT / "docs" / "manuals" / "output" / "kdp_upload",
        education_pdf_dir,
        education_pdf_dir / "kdp_upload",
        education_pdf_dir / "kdp_upload_ready",
    ):
        if kdp_dir.parent.exists():
            kdp_dir.mkdir(parents=True, exist_ok=True)

    if build_all or args.sc32_only:
        if not args.covers_only:
            compile_manual_pdf(is_sc32=True, manual_kind="sc32")
        compile_full_wrap_cover_spread(is_sc32=True, is_hardcover=False, manual_kind="sc32")
        compile_full_wrap_cover_spread(is_sc32=True, is_hardcover=True, manual_kind="sc32")
        compile_lulu_coil_cover_spread(is_sc32=True, manual_kind="sc32")
        compile_kindle_front_cover(is_sc32=True, manual_kind="sc32")
        for mdir in mirror_out_dirs:
            if mdir.exists():
                for fname in (
                    "sc32-scientific-manual.pdf",
                    "sc32-scientific-manual-hardcover.pdf",
                    "sc32-full-wrap-cover.pdf",
                    "sc32-hardcover-wrap-cover.pdf",
                    "sc32-lulu-cover.pdf",
                    "sc32-kindle-cover.pdf",
                    "sc32-kindle-cover.jpg",
                ):
                    src_f = OUTPUT_DIR / fname
                    if src_f.exists():
                        shutil.copy2(src_f, mdir / fname)
        if education_pdf_dir.exists() and (OUTPUT_DIR / "sc32-scientific-manual.pdf").exists():
            shutil.copy2(OUTPUT_DIR / "sc32-scientific-manual.pdf", education_pdf_dir / "StackCalc-Pro-Scientific-Edition.pdf")

    if build_all or args.sc6_only:
        if not args.covers_only:
            compile_manual_pdf(is_sc32=False, manual_kind="sc6")
        compile_full_wrap_cover_spread(is_sc32=False, is_hardcover=False, manual_kind="sc6")
        compile_full_wrap_cover_spread(is_sc32=False, is_hardcover=True, manual_kind="sc6")
        compile_lulu_coil_cover_spread(is_sc32=False, manual_kind="sc6")
        compile_kindle_front_cover(is_sc32=False, manual_kind="sc6")
        for mdir in mirror_out_dirs:
            if mdir.exists():
                for fname in (
                    "sc6-elementary-manual.pdf",
                    "sc6-elementary-manual-hardcover.pdf",
                    "sc6-full-wrap-cover.pdf",
                    "sc6-hardcover-wrap-cover.pdf",
                    "sc6-lulu-cover.pdf",
                    "sc6-kindle-cover.pdf",
                    "sc6-kindle-cover.jpg",
                ):
                    src_f = OUTPUT_DIR / fname
                    if src_f.exists():
                        shutil.copy2(src_f, mdir / fname)
        if education_pdf_dir.exists() and (OUTPUT_DIR / "sc6-elementary-manual.pdf").exists():
            shutil.copy2(OUTPUT_DIR / "sc6-elementary-manual.pdf", education_pdf_dir / "StackCalc-Elementary-Edition.pdf")

    if build_all or args.domains_only:
        if not args.covers_only:
            compile_manual_pdf(is_sc32=True, manual_kind="domains")
        compile_full_wrap_cover_spread(is_sc32=True, is_hardcover=False, manual_kind="domains")
        compile_full_wrap_cover_spread(is_sc32=True, is_hardcover=True, manual_kind="domains")
        compile_lulu_coil_cover_spread(is_sc32=True, manual_kind="domains")
        compile_kindle_front_cover(is_sc32=True, manual_kind="domains")
        for mdir in mirror_out_dirs:
            if mdir.exists():
                for fname in (
                    "sc-domains-manual.pdf",
                    "sc-domains-manual-hardcover.pdf",
                    "sc-domains-full-wrap-cover.pdf",
                    "sc-domains-hardcover-wrap-cover.pdf",
                    "sc-domains-lulu-cover.pdf",
                    "sc-domains-kindle-cover.pdf",
                    "sc-domains-kindle-cover.jpg",
                ):
                    src_f = OUTPUT_DIR / fname
                    if src_f.exists():
                        shutil.copy2(src_f, mdir / fname)
        if education_pdf_dir.exists():
            dom_pairs = [
                ("sc-domains-manual.pdf", "StackCalc-Volume-3-Domain-Calculators.pdf"),
                ("sc-domains-manual.pdf", "domain-calculators-manual.pdf"),
                ("sc-domains-full-wrap-cover.pdf", "domain-calculators-manual-kdp-cover.pdf"),
                ("sc-domains-lulu-cover.pdf", "domain-calculators-manual-lulu-cover.pdf"),
            ]
            for src_name, dst_name in dom_pairs:
                src_f = OUTPUT_DIR / src_name
                if src_f.exists():
                    shutil.copy2(src_f, education_pdf_dir / dst_name)

    print("\n=======================================================")
    print("PDF Generation Complete. Validating outputs...")
    print("=======================================================")
    try:
        import pypdf
        validation_targets = []
        if build_all or args.sc32_only:
            validation_targets.append(("sc32-scientific-manual.pdf", 180))
        if build_all or args.sc6_only:
            validation_targets.append(("sc6-elementary-manual.pdf", 180))
        if build_all or args.domains_only:
            validation_targets.append(("sc-domains-manual.pdf", 50))
        for pdf_name, min_p in validation_targets:
            pdf_path = OUTPUT_DIR / pdf_name
            if not pdf_path.exists():
                continue
            reader = pypdf.PdfReader(str(pdf_path))
            num_pages = len(reader.pages)
            root_obj = reader.trailer["/Root"].get_object()
            assert "/Outlines" not in root_obj, f"Found /Outlines metadata in {pdf_name}!"
            assert not reader.metadata, f"Found non-empty /Info metadata dictionary in {pdf_name}: {reader.metadata}!"
            assert num_pages >= min_p, f"{pdf_name} has only {num_pages} pages (expected >= {min_p})!"

            for pg_idx, page in enumerate(reader.pages):
                assert "/Annots" not in page, f"Found non-printable /Annots markup on page {pg_idx + 1} of {pdf_name}!"
                pg_text = page.extract_text() or ""
                assert "\x00" not in pg_text, f"Found unmapped NUL glyph on page {pg_idx + 1} of {pdf_name}!"
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
            print(f"    ✓ [{pdf_name}] Passed all forensic validation assertions across all {num_pages} pages (0 metadata/outlines/annots, 0 NUL glyphs, 0 naked mathbf, 0 raw LaTeX, 0 test identifiers, 0 leaked phrases, 0 contest acronyms)!")
    except Exception as e:
        print(f"  [ERROR] Validation failed: {e}")
        sys.exit(1)

    print("\nAll manuals compiled and validated successfully.")


if __name__ == "__main__":
    main()
