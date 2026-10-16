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
DOCS_DIR = REPO_ROOT / "docs"
FONT_DIR = DOCS_DIR / "assets" / "fonts"
OUTPUT_DIR = DOCS_DIR / "downloads" / "manuals"

# ---------------------------------------------------------------------------
# Font Registration
# ---------------------------------------------------------------------------
FONTS_AVAILABLE = False
try:
    if (FONT_DIR / "SpaceMono-Regular.ttf").exists():
        pdfmetrics.registerFont(TTFont("SpaceMono", str(FONT_DIR / "SpaceMono-Regular.ttf")))
        pdfmetrics.registerFont(TTFont("SpaceMono-Bold", str(FONT_DIR / "SpaceMono-Bold.ttf")))
        pdfmetrics.registerFont(TTFont("Terminus", str(FONT_DIR / "TerminusTTF-4.49.3.ttf")))
        pdfmetrics.registerFont(TTFont("Terminus-Bold", str(FONT_DIR / "TerminusTTF-Bold-4.49.3.ttf")))
        if (FONT_DIR / "Tiny5-Regular.ttf").exists():
            pdfmetrics.registerFont(TTFont("Tiny5", str(FONT_DIR / "Tiny5-Regular.ttf")))
        FONTS_AVAILABLE = True
except Exception as e:
    print(f"[WARN] Could not register TrueType fonts: {e}. Falling back to standard Helvetica/Courier.")

FONT_BODY = "Helvetica"
FONT_BODY_BOLD = "Helvetica-Bold"
FONT_BODY_ITALIC = "Helvetica-Oblique"
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

# SC-32 Scientific Palette
SC32_COVER_BG = "#28334A"        # Sunlu Midnight Navy PLA 2.0+
SC32_PRIMARY = "#142240"         # Deep Technical Navy
SC32_ACCENT = "#0284c7"          # Technical Sky Blue
SC32_COVER_ACCENT = "#38bdf8"    # Foil Cyan Accent

# SC-6 Elementary Palette
SC6_COVER_BG = "#101114"         # Technical Matte Black PLA / PETG
SC6_PRIMARY = "#064e3b"          # Forest Slate 900
SC6_ACCENT = "#059669"           # Emerald Green 600
SC6_COVER_ACCENT = "#10b981"     # Foil Mint Accent

# Print Book Interior Palette (Archival White Paper)
PAGE_BG = "#ffffff"              # Pure Archival White
TEXT_MAIN = "#101114"            # Deep Technical Charcoal / Black
TEXT_MUTED = "#4b4e54"           # Elegoo Space Gray PLA (#4B4E54)
STACK_FRAME_BG = "#f5f5f7"       # Subtle Technical Fill
DIVIDER_HEX = "#cbd5e1"          # Crisp Slate Border
CALLOUT_BG_SC32 = "#f0f9ff"      # Light Cyan Tint
CALLOUT_BG_SC6 = "#f0fdf4"       # Light Mint Tint

# Exterior Cover Foil Typography
COVER_FOIL_WHITE = "#ffffff"     # 1064nm IR Micro-Foam Stark White (15.2:1 AAA)
COVER_FOIL_CREAM = "#f5f5f3"     # Sunlu Antique White / Cream
COVER_TAXONOMY_MUTED = "#94a3b8" # Technical Taxonomy Gray

MARGIN_PT = 54.0                 # 0.75 in margins for physical book binding
PAGE_WIDTH = 612.0               # Letter width
PAGE_HEIGHT = 792.0              # Letter height
PRINTABLE_WIDTH = PAGE_WIDTH - (2 * MARGIN_PT)  # 504.0 pt

# ---------------------------------------------------------------------------
# Flowables for PDF Outlines and Chapter Tracking
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


class ManualDocTemplate(SimpleDocTemplate):
    """
    Two-pass publication document template that intercepts flowables
    and notifies TableOfContents and SimpleIndex with exact page numbers.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def afterFlowable(self, flowable):
        super().afterFlowable(flowable)
        if hasattr(flowable, '_toc_info'):
            level, text, key = flowable._toc_info
            self.notify('TOCEntry', (level, text, self.page, key))
        if hasattr(flowable, '_index_terms'):
            for term in flowable._index_terms:
                self.notify('IndexEntry', (term, self.page))


# ---------------------------------------------------------------------------
# Two-Pass NumberedCanvas for Retrofuturistic Brutalist Layouts
# ---------------------------------------------------------------------------
class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas that renders monolithic retrofuturistic brutalist cover framing
    on page 1, and running headers, footers, and 'Page X of Y' on subsequent pages.
    All interior pages are formatted on pure white backgrounds for print reading.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []
        self.doc_title = "STACKCALC REFERENCE MANUAL"
        self.primary_hex = SC32_PRIMARY
        self.cover_bg_hex = SC32_COVER_BG
        self.cover_accent_hex = SC32_COVER_ACCENT
        self.doc_code = "STK-REF-32-V2"
        self.current_chapter_title = ""
        self.is_sc32 = True

    def showPage(self):
        state = dict(self.__dict__)
        state["page_chapter_title"] = getattr(self, "current_chapter_title", "")
        self._saved_page_states.append(state)
        self._startPage()

    def save(self):
        total_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            if self._pageNumber == 1:
                flowables_code = list(self._code)
                self._code = []
                self.draw_brutalist_cover_canvas()
                self._code.extend(flowables_code)
            else:
                self.draw_interior_page_decorations(total_pages, state.get("page_chapter_title", ""))
            super().showPage()
        super().save()

    def draw_brutalist_cover_canvas(self):
        """Draws monolithic retrofuturistic brutalist cover wrap with coordinate grid."""
        self.saveState()
        w, h = PAGE_WIDTH, PAGE_HEIGHT

        # 1. Monolithic technical thermoplastic field (Midnight Navy / Technical Black)
        self.setFillColor(to_color(self.cover_bg_hex))
        self.rect(0, 0, w, h, fill=1, stroke=0)

        # 2. Brutalist engineering coordinate outer frame
        self.setStrokeColor(to_color(self.cover_accent_hex))
        self.setLineWidth(1.2)
        self.rect(28, 28, w - 56, h - 56, fill=0, stroke=1)

        # 3. Inner registration rule
        self.setStrokeColor(to_color(COVER_TAXONOMY_MUTED))
        self.setLineWidth(0.5)
        self.rect(32, 32, w - 64, h - 64, fill=0, stroke=1)

        # 4. Corner crosshair ticks (Engineering grid fiducials)
        cross_len = 10
        corners = [(32, 32), (w - 32, 32), (32, h - 32), (w - 32, h - 32)]
        self.setStrokeColor(to_color(COVER_FOIL_WHITE))
        self.setLineWidth(0.75)
        for cx, cy in corners:
            dx = 1 if cx < w / 2 else -1
            dy = 1 if cy < h / 2 else -1
            self.line(cx, cy, cx + (dx * cross_len), cy)
            self.line(cx, cy, cx, cy + (dy * cross_len))

        # 5. Top technical taxonomy bar
        self.setFont(FONT_MONO, 7.0)
        self.setFillColor(to_color(self.cover_accent_hex))
        if getattr(self, "is_sc32", True):
            self.drawString(38, h - 22, "ARCHIVAL INSTRUMENT REFERENCE // EDITION 1.2")
            self.drawRightString(w - 38, h - 22, "PRECISION RPN ENGINEERING & APPLIED STEM HANDBOOK")
        else:
            self.drawString(38, h - 22, "HANDS-ON MATHEMATICS STUDIO SERIES // EDITION 1.2")
            self.drawRightString(w - 38, h - 22, "CONCRETE – REPRESENTATIONAL – ABSTRACT (CRA) CURRICULUM")

        # 6. Bottom coordinate baseline
        self.setFont(FONT_MONO, 6.5)
        self.setFillColor(to_color(COVER_TAXONOMY_MUTED))
        self.drawString(38, 18, "STACKCALC LABORATORY PRESS // SAN FRANCISCO & AUSTIN // OPEN REVERSE POLISH NOTATION")
        if getattr(self, "is_sc32", True):
            self.drawRightString(w - 38, 18, "COLLEGIATE, ENGINEERING & CONTEST REFERENCE EDITION")
        else:
            self.drawRightString(w - 38, 18, "ELEMENTARY & MIDDLE SCHOOL CLASSROOM EDITION (GRADES K–6)")

        self.restoreState()

    def draw_interior_page_decorations(self, total_pages: int, chapter_title: str):
        """Draws clean running header and footer on pure white interior pages."""
        self.saveState()
        w, h = PAGE_WIDTH, PAGE_HEIGHT
        m = MARGIN_PT

        # Running Header
        self.setStrokeColor(to_color(DIVIDER_HEX))
        self.setLineWidth(0.6)
        self.line(m, h - 36, w - m, h - 36)

        self.setFont(FONT_MONO, 7.5)
        self.setFillColor(to_color(TEXT_MUTED))
        self.drawString(m, h - 30, getattr(self, "doc_title", "STACKCALC MANUAL"))

        if chapter_title:
            self.setFont(FONT_MONO_BOLD, 7.5)
            self.setFillColor(to_color(self.primary_hex))
            disp_title = chapter_title[:45] + ("..." if len(chapter_title) > 45 else "")
            self.drawRightString(w - m, h - 30, disp_title)

        # Running Footer
        self.line(m, 36, w - m, 36)

        self.setFont(FONT_MONO, 7.0)
        self.setFillColor(to_color(TEXT_MUTED))
        self.drawString(m, 24, "STACKCALC INSTRUMENT CORP // REVISION 1.2 // STACKCALC.IO")

        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.setFont(FONT_MONO_BOLD, 8.0)
        self.setFillColor(to_color(TEXT_MAIN))
        self.drawRightString(w - m, 24, page_str)

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

    # Unescape LaTeX literal escapes before XML escaping
    text = text.replace(r"\%", "%").replace(r"\$", "$").replace(r"\_", "_")
    text = text.replace(r"\{", "(").replace(r"\}", ")")
    text = text.replace(r"\ ", " ")

    # Escape XML special characters FIRST so < and > in inequalities never corrupt ReportLab tags
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    # Handle \begin{...} / \end{...} environments (aligned, cases, pmatrix)
    text = re.sub(r'\\begin\{[^}]*\}', '', text)
    text = re.sub(r'\\end\{[^}]*\}', '', text)
    text = text.replace(r"\\", "; ")

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
        text = re.sub(r'\\pmod\{([^{}]*)\}', r' (mod \1)', text)
        text = re.sub(r'\\xrightarrow\{([^{}]*)\}', r'→[\1]', text)
        text = re.sub(r'\\hspace\{[^{}]*\}', ' ', text)

    text = re.sub(r'\\Large\b', '', text)
    text = re.sub(r'\\bmod\b', ' mod ', text)

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

    # 6. General symbol replacements
    for pat, rep in MATH_REPLACEMENTS:
        text = text.replace(pat, rep)

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
    return text.strip()


def format_hardware_keycap_cartouche(key_token: str, is_sc32: bool) -> str:
    """
    Renders an authentic squircle keycap matching the app in black and white:
    - Primary action keys (ENTER, ON, C, CLEAR, AC, <-, BS): Solid black keycap (#101114) with stark white SpaceMono-Bold text.
    - Standard keys (digits, arithmetic, scientific functions): Tactile light gray keycap (#E5E7EB) with crisp black SpaceMono-Bold text (#101114).
    """
    clean_k = key_token.strip()
    clean_k = clean_k.replace("⇄", "↔").replace("Σ", "∑").replace("∥", "||").replace("↰", "↖").replace("↱", "↗").replace("▸", "→")
    clean_k = clean_k.replace("🎲", "DICE").replace("🕒", "CLOCK").replace("▦", "FRAME")
    is_inverted = clean_k.upper() in ["ENTER", "ON", "C", "CLEAR", "AC", "<-", "BS"]
    if is_inverted:
        return f"<b><font face='{FONT_KEYCAP}' color='#ffffff' backColor='#101114'>&nbsp;[{clean_k}]&nbsp;</font></b>"
    else:
        return f"<b><font face='{FONT_KEYCAP}' color='#101114' backColor='#e5e7eb'>&nbsp;[{clean_k}]&nbsp;</font></b>"


def sanitize_inline_markdown(text: str, is_sc32: bool) -> str:
    """
    Sanitizes markdown inline syntax and escapes XML characters for ReportLab Paragraphs.
    Formats retrofuturistic keycaps, math blocks, bold, italic, and links.
    """
    accent_hex = SC32_ACCENT if is_sc32 else SC6_ACCENT

    # 1. Unescape existing HTML entities and normalize non-Latin1 characters
    text = html.unescape(text)
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

    # Handle backtick hardware keycaps `[KEY]` BEFORE math so `[$]` never collides with $...$
    def sub_backtick_keycap(m):
        k = m.group(1)
        return save_placeholder(format_hardware_keycap_cartouche(k, is_sc32))
    text = re.sub(r'`\[([^`\n]+)\]`', sub_backtick_keycap, text)

    # Handle standard inline code `...` BEFORE math (unless wrapped directly in $`...`$)
    text = re.sub(r'\$\s*`([^`\n]+)`\s*\$', r'`\1`', text)
    def sub_code(m):
        raw = m.group(1)
        raw = raw.replace("↰", "↖").replace("↱", "↗").replace("▸", "→")
        raw_esc = raw.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return save_placeholder(f"<font face='{FONT_MONO}' size='7.5' color='{accent_hex}'><b>{raw_esc}</b></font>")
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
    from book_engine import get_registry
    registry = get_registry(is_sc32)
    def sub_bare_keycap(m):
        k = m.group(1)
        try:
            registry.resolve(k)
            return save_placeholder(format_hardware_keycap_cartouche(k, is_sc32))
        except ValueError:
            return m.group(0)
    text = re.sub(r'(?<!\!)\[([A-Za-z0-9⇄↔↓↑↰↱↖↗▸∫Σ∑🎲🕒▦+×÷\-\/%=|²³√•.,?<>≤≥≠$]+)\](?!\()', sub_bare_keycap, text)

    # 3. Escape remaining XML characters in regular text
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

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

    return text.strip()


def format_heading_text(raw_title: str) -> Tuple[str, str]:
    """
    Formats a markdown heading into (plain_toc_title, styled_paragraph_title),
    converting inline $...$ LaTeX math into clean Unicode typography.
    """
    t = html.unescape(raw_title.strip())
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
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for k, v in math_ph.items():
        t = t.replace(k, v)
    styled = t.strip()
    plain = html.unescape(re.sub(r'</?[a-zA-Z][^>]*>', '', styled)).strip()
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
    ("Brent's Root Finding Algorithm", [re.compile(r'\b(brent\'s solver|brent solver|numerical root)\b', re.IGNORECASE)]),
    ("Adaptive Romberg Quadrature", [re.compile(r'\b(romberg quadrature|adaptive quadrature|numerical integration)\b', re.IGNORECASE)]),
    ("Polynomial Root Extraction", [re.compile(r'\b(polynomial solver|polynomial roots|companion matrix)\b', re.IGNORECASE)]),
    ("Bivariate Statistics & Curve Fitting", [re.compile(r'\b(bivariate statistics|linear regression|curve fitting|correlation coefficient)\b', re.IGNORECASE)]),
    ("Computer Science & 36-Bit Integers", [re.compile(r'\b(36-bit|two\'s complement|subnet masking|bitwise)\b', re.IGNORECASE)]),
    ("Financial TVM Solver", [re.compile(r'\b(tvm solver|financial mathematics|amortization schedule)\b', re.IGNORECASE)]),
    ("Function & Scatter Plotting Engine", [re.compile(r'\b(scatter plotting|function plotting|pixel grid)\b', re.IGNORECASE)]),
    ("3D Printing Extrusion Fluid Dynamics", [re.compile(r'\b(extrusion fluid dynamics|volumetric flow|filament density)\b', re.IGNORECASE)]),
    ("Audio Engineering Crossover Filters", [re.compile(r'\b(crossover filter|butterworth|linkwitz-riley)\b', re.IGNORECASE)]),
    ("Civil Surveying & Closed Traverses", [re.compile(r'\b(closed-loop traverse|traverse misclosure|geodetic azimuth)\b', re.IGNORECASE)]),
    ("High-Speed Equation Entry & Inside-Out Mastery", [re.compile(r'\b(inside-out|radical pyramid|nested fraction|high-speed equation)\b', re.IGNORECASE)]),
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
    ("Ten-Frames & Desk Counters", [re.compile(r'\b(ten-frames?|desk counters?|counting grid)\b', re.IGNORECASE)]),
    ("Classroom Planetary Clock", [re.compile(r'\b(planetary clock|geared clock|modulo 60)\b', re.IGNORECASE)]),
    ("Math Domino Studio", [re.compile(r'\b(math dominoes?|domino studio|dot arrays?)\b', re.IGNORECASE)]),
    ("Algebra Boxes & Tiles", [re.compile(r'\b(algebra boxes|algebra tiles|area models?)\b', re.IGNORECASE)]),
    ("Probability Dice & Spinners", [re.compile(r'\b(probability dice|dice and spinner|random generator)\b', re.IGNORECASE)]),
    ("RPN Elevator Metaphor", [re.compile(r'\b(elevator metaphor|elevator model|ground floor)\b', re.IGNORECASE)]),
    ("2-Stack Operational Display", [re.compile(r'\b(2-stack|two-stack|upper stack|lower stack)\b', re.IGNORECASE)]),
    ("Counting, Place Value & Base-10", [re.compile(r'\b(place value|base-10|units and tens|hundreds board)\b', re.IGNORECASE)]),
    ("Number Lines & Skip-Counting", [re.compile(r'\b(number lines?|skip-counting|skip counting)\b', re.IGNORECASE)]),
    ("Superpower [REP] (Repeat Ladder)", [re.compile(r'\[REP\]'), re.compile(r'\bskip-counting ladder\b', re.IGNORECASE)]),
    ("Superpower [DivR] (Quotient & Remainder)", [re.compile(r'\[DivR\]', re.IGNORECASE), re.compile(r'\bquotient and remainder\b', re.IGNORECASE)]),
    ("Superpower [SIMP] (Factor Reduction)", [re.compile(r'\[SIMP\]', re.IGNORECASE), re.compile(r'\bfactor reduction\b', re.IGNORECASE)]),
    ("Superpower [LASTX] (Undo & Inverse)", [re.compile(r'\[LASTX\]', re.IGNORECASE), re.compile(r'\bundoing operations\b', re.IGNORECASE)]),
    ("Two-Dot Fraction Entry Syntax", [re.compile(r'\btwo-dot|fraction entry|mixed fractions?\b', re.IGNORECASE)]),
    ("Ratio Mode & Proportions", [re.compile(r'\bratio mode|proportional reasoning|unit rate\b', re.IGNORECASE)]),
    ("Geometry & Surface Area via [Σ+]", [re.compile(r'\bsurface area via|rectangular prism|cylinder volume\b', re.IGNORECASE), re.compile(r'\[[Σ∑]\+\]')]),
    ("Discrete Probability & Primes", [re.compile(r'\bdiscrete probability|prime factorization|sieve of eratosthenes\b', re.IGNORECASE)]),
    ("Gamified Math Quiz Engine", [re.compile(r'\bmath quiz engine|gamified quiz|flashcard mode\b', re.IGNORECASE)]),
    ("Applied Elementary STEM Labs", [re.compile(r'\bapplied stem|paper circuits?|batch cubes?|maker labs?\b', re.IGNORECASE)]),
    ("Bridges in Mathematics CCSS Alignment", [re.compile(r'\bbridges in math|ccss alignment|curriculum matrix\b', re.IGNORECASE)]),
    ("Keycap [ENTER]", [re.compile(r'\[ENTER\]', re.IGNORECASE)]),
    ("Keycap [C] / [CLEAR]", [re.compile(r'\[(C|CLEAR)\]', re.IGNORECASE)]),
    ("Keycap [LASTX]", [re.compile(r'\[LASTX\]', re.IGNORECASE)]),
    ("Keycap [x⇄y]", [re.compile(r'\[x[⇄↔<->]+y\]', re.IGNORECASE)]),
    ("Keycap [REP]", [re.compile(r'\[REP\]', re.IGNORECASE)]),
    ("Keycap [DivR]", [re.compile(r'\[DivR\]', re.IGNORECASE)]),
    ("Keycap [SIMP]", [re.compile(r'\[SIMP\]', re.IGNORECASE)]),
    ("Keycap [PRISM]", [re.compile(r'\[PRISM\]', re.IGNORECASE)]),
    ("Keycap [Σ+]", [re.compile(r'\[[Σ∑]\+\]')]),
    ("Keycap [DICE]", [re.compile(r'\[DICE\]', re.IGNORECASE)]),
    ("Keycap [CLOCK]", [re.compile(r'\[CLOCK\]', re.IGNORECASE)]),
    ("Keycap [FRAME]", [re.compile(r'\[FRAME\]', re.IGNORECASE)]),
    ("Keycap [.] (Fraction Two-Dot)", [re.compile(r'\[\.\]')]),
]

def extract_index_terms(text: str, is_sc32: bool, term_counts: Optional[Dict[str, int]] = None, max_per_term: int = 4) -> List[str]:
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
# Cover Page Generation (Monolithic Retrofuturistic Brutalism)
# ---------------------------------------------------------------------------
def build_cover_page(is_sc32: bool, styles: Dict[str, ParagraphStyle]) -> List[Flowable]:
    """
    Builds a monolithic retrofuturistic brutalist publication cover page.
    Matches the Surface Rubric and Aesthetics design master strategy.
    """
    elements: List[Flowable] = []

    cover_accent = SC32_COVER_ACCENT if is_sc32 else SC6_COVER_ACCENT
    dark_primary = SC32_PRIMARY if is_sc32 else SC6_PRIMARY
    model_name = "STACKCALC SC-32" if is_sc32 else "STACKCALC SC-6"
    sub_title = "Scientific Reference Manual & Applied STEM Handbook" if is_sc32 else "Elementary Reference Manual & Manipulative Companion"
    edition_label = "COLLEGIATE STEM EDITION & HIGH-SPEED EQUATION HANDBOOK" if is_sc32 else "CLASSROOM COMPANION FOR GRADES K–6 & CONCRETE MATH LAB"

    elements.append(Spacer(1, 15))

    # Top Kicker
    kicker_style = ParagraphStyle(
        "CoverKicker",
        parent=styles["Normal"],
        fontName=FONT_MONO_BOLD,
        fontSize=8.5,
        leading=11.0,
        textColor=to_color(cover_accent),
        alignment=0,
        spaceAfter=12
    )
    elements.append(Paragraph("STACKCALC INSTRUMENT CORP // FORMAL PUBLICATION SERIES", kicker_style))

    # Brutalist Accent Stripe Table
    bar_table = Table([[""]], colWidths=[PRINTABLE_WIDTH], rowHeights=[4])
    bar_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), to_color(cover_accent)),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    elements.append(bar_table)
    elements.append(Spacer(1, 18))

    # Title in stark white foil
    title_style = ParagraphStyle(
        "CoverTitle",
        parent=styles["Normal"],
        fontName=FONT_BODY_BOLD,
        fontSize=28.0,
        leading=34.0,
        textColor=to_color(COVER_FOIL_WHITE),
        spaceAfter=8
    )
    elements.append(Paragraph(model_name, title_style))

    # Subtitle in warm cream
    subtitle_style = ParagraphStyle(
        "CoverSubtitle",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=13.5,
        leading=18.0,
        textColor=to_color(COVER_FOIL_CREAM),
        spaceAfter=8
    )
    elements.append(Paragraph(sub_title, subtitle_style))

    # Edition Banner
    edition_style = ParagraphStyle(
        "CoverEdition",
        parent=styles["Normal"],
        fontName=FONT_MONO_BOLD,
        fontSize=8.0,
        leading=11.5,
        textColor=to_color(cover_accent),
        spaceAfter=18
    )
    elements.append(Paragraph(f"// {edition_label} • FIRMWARE REVISION 1.2", edition_style))

    # Architectural Specification Card (Dark Monolithic Brutalist Box)
    cover_spec_hdr = ParagraphStyle("CoverSpecHdr", parent=styles["Normal"], fontName=FONT_MONO_BOLD, fontSize=7.5, leading=9.5, textColor=to_color(COVER_FOIL_WHITE))
    cover_spec_bold = ParagraphStyle("CoverSpecBold", parent=styles["Normal"], fontName=FONT_BODY_BOLD, fontSize=7.0, leading=8.8, textColor=to_color(cover_accent))
    cover_spec_text = ParagraphStyle("CoverSpecText", parent=styles["Normal"], fontName=FONT_BODY, fontSize=7.0, leading=8.8, textColor=to_color(COVER_FOIL_CREAM))

    if is_sc32:
        specs_data = [
            [Paragraph("<b>HARDWARE ARCHITECTURE</b>", cover_spec_hdr), Paragraph("<b>INSTRUMENT SPECIFICATIONS &amp; VERIFICATION</b>", cover_spec_hdr)],
            [Paragraph("<b>Silicon Engine</b>", cover_spec_bold), Paragraph("Dedicated Dual-Core Embedded 32-bit Microcontroller (150 MHz, 5ms Cold Boot)", cover_spec_text)],
            [Paragraph("<b>Display Subsystem</b>", cover_spec_bold), Paragraph("132 × 65 High-Contrast Ambient-Light Transflective Monochrome Dot-Matrix LCD", cover_spec_text)],
            [Paragraph("<b>Keypad &amp; Marking</b>", cover_spec_bold), Paragraph("Tactile Elastomeric Keycaps • 1064nm IR Fiber Laser Micro-Foaming (15.2:1 AAA)", cover_spec_text)],
            [Paragraph("<b>Faceplate Themes</b>", cover_spec_bold), Paragraph("Interchangeable Physical &amp; App Faceplate Editions • Left [↰] &amp; Right [↱] Shift Architecture", cover_spec_text)],
            [Paragraph("<b>Stack Dynamics</b>", cover_spec_bold), Paragraph("Operational 4-Stack XYZT • Deep Stack Modes (8-LV, INF) • Continuous Non-Volatile EEPROM", cover_spec_text)],
            [Paragraph("<b>Engine Grounding</b>", cover_spec_bold), Paragraph("100% Codebase Grounded: 84 Textbook Verification Tests &amp; 607 Verified Sequences in RPNCore", cover_spec_text)],
            [Paragraph("<b>Equation Speedcraft</b>", cover_spec_bold), Paragraph("Parenthesis-Free Inside-Out Equation Entry, Radical Pyramids &amp; Exam Memory Reset", cover_spec_text)],
        ]
    else:
        specs_data = [
            [Paragraph("<b>EDUCATIONAL ARCHITECTURE</b>", cover_spec_hdr), Paragraph("<b>CLASSROOM &amp; HOME STUDIO SPECIFICATIONS (GRADES K–6)</b>", cover_spec_hdr)],
            [Paragraph("<b>Silicon Engine</b>", cover_spec_bold), Paragraph("Dedicated Dual-Core Embedded 32-bit Microcontroller (Microamp Standby, Instant Boot)", cover_spec_text)],
            [Paragraph("<b>Display Subsystem</b>", cover_spec_bold), Paragraph("132 × 65 High-Contrast Ambient-Light Transflective Monochrome Dot-Matrix LCD", cover_spec_text)],
            [Paragraph("<b>Ergonomics &amp; Stand</b>", cover_spec_bold), Paragraph("Sliding Protective Desk-Stand Cowl (15° Classroom Viewing Angle) • 400g Snap-Domes", cover_spec_text)],
            [Paragraph("<b>Pedagogical Method</b>", cover_spec_bold), Paragraph("Concrete-Representational-Abstract (CRA) Framework • Singapore Dimensions &amp; Bridges Aligned", cover_spec_text)],
            [Paragraph("<b>Physical Manipulatives</b>", cover_spec_bold), Paragraph("Modular Classroom Manipulative Studios: Ten-Frames, Dominoes, 84mm Towers, Planetary Clock", cover_spec_text)],
            [Paragraph("<b>Stack Progression</b>", cover_spec_bold), Paragraph("The Elevator Metaphor • Automatic 2-Stack Sandbox Mode • 4-Stack Base-10 Arithmetic", cover_spec_text)],
            [Paragraph("<b>Curriculum Ribbon</b>", cover_spec_bold), Paragraph("Strict Progressive Keycap Ribbon (K–5 Shielded from Advanced Transcendentals)", cover_spec_text)],
        ]

    spec_table = Table(specs_data, colWidths=[135, PRINTABLE_WIDTH - 135])
    spec_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), to_color("#0f172a")),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [to_color("#161e2e" if is_sc32 else "#181a1f"), to_color("#1e293b" if is_sc32 else "#20232a")]),
        ('GRID', (0,0), (-1,-1), 0.5, to_color("#334155")),
        ('BOX', (0,0), (-1,-1), 1.0, to_color(cover_accent)),
    ]))
    elements.append(spec_table)
    elements.append(Spacer(1, 16))

    # Epigraph / Philosophy Card (Retrofuturistic Brutalist Quote)
    if is_sc32:
        quote_text = (
            "<i>\"In an era of frictionless automated computation, students and engineers choose Reverse Polish Notation "
            "not merely to execute calculations, but to develop spatial clarity, intermediate awareness, and a transformative "
            "way of thinking in the stack. By combining registers without parentheses, every intermediate state is visible, "
            "every operand is respected, and computation becomes an active craft of precision engineering.\"</i>"
        )
    else:
        quote_text = (
            "<i>\"Mathematics begins not with abstract symbols on a page, but with the tactile feel of blocks in the hand "
            "and numbers moving on an elevator. The SC-6 transforms Reverse Polish Notation into an intuitive, joyful companion "
            "where combining numbers <b>is</b> the answer—fostering intermediate awareness, eliminating fear of the '=' key, "
            "and empowering young minds with mathematical confidence.\"</i>"
        )

    cover_quote_style = ParagraphStyle(
        "CoverQuoteBrutalist",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=7.8,
        leading=11.2,
        textColor=to_color(COVER_FOIL_CREAM)
    )
    quote_para = Paragraph(quote_text, cover_quote_style)
    quote_card = Table([[quote_para]], colWidths=[PRINTABLE_WIDTH])
    quote_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), to_color("#1e293b" if is_sc32 else "#181a1f")),
        ('LINEBEFORE', (0,0), (0,-1), 3.0, to_color(cover_accent)),
        ('BOX', (0,0), (-1,-1), 0.75, to_color("#334155")),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ]))
    elements.append(quote_card)
    elements.append(Spacer(1, 22))

    # Bottom Publication Colophon
    colophon_style = ParagraphStyle(
        "CoverColophon",
        parent=styles["Normal"],
        fontName=FONT_MONO,
        fontSize=7.0,
        leading=9.5,
        textColor=to_color(cover_accent),
        alignment=1
    )
    elements.append(Paragraph(
        "STACKCALC LABORATORY PRESS // SAN FRANCISCO &amp; AUSTIN<br/>"
        "PUBLISHED UNDER OPEN DOCUMENTATION &amp; HARDWARE DISTRIBUTION LICENSES // STACKCALC.IO",
        colophon_style
    ))

    elements.append(PageBreak())
    return elements


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

    # Normalize multi-line display math blocks ($$ ... $$) outside fenced code blocks into single-line $$ ... $$
    fenced_blocks = {}
    def _save_fenced(m):
        k = f"QQFENCE{len(fenced_blocks)}QQ"
        fenced_blocks[k] = m.group(0)
        return k
    content = re.sub(r'```.*?```', _save_fenced, content, flags=re.DOTALL)
    content = re.sub(
        r'^\s*\$\$\s*\n([^\$]+?)\n\s*\$\$\s*$',
        lambda m: "$$" + " ".join(l.strip() for l in m.group(1).splitlines() if l.strip()) + "$$",
        content,
        flags=re.MULTILINE
    )
    for k, v in fenced_blocks.items():
        content = content.replace(k, v)

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

        # HTML Callout div block (skip web-only te-viewport-header banners; render admonitions)
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
            div_text = " ".join(div_lines)
            if "te-viewport-header" in div_text:
                continue
            # Convert inline HTML tags to markdown before stripping block HTML tags
            div_text = re.sub(r'<code>(.*?)</code>', r'`\1`', div_text)
            div_text = re.sub(r'<(?:strong|b)>(.*?)</(?:strong|b)>', r'**\1**', div_text)
            div_text = re.sub(r'<(?:em|i)>(.*?)</(?:em|i)>', r'*\1*', div_text)
            div_text = re.sub(r'<li>\s*', ' • ', div_text)
            # Only strip valid HTML tags starting with </?[a-zA-Z] so math inequalities like < 10 are never eaten!
            clean_text = re.sub(r'</?[a-zA-Z][^>]*>', ' ', div_text)
            clean_text = re.sub(r'\s+', ' ', clean_text).strip()
            if clean_text:
                sanitized = sanitize_inline_markdown(clean_text, is_sc32)
                callout_p = make_paragraph(sanitized, styles["CalloutText"])
                callout_tbl = Table([[callout_p]], colWidths=[PRINTABLE_WIDTH])
                callout_tbl.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,-1), to_color(CALLOUT_BG_SC32 if is_sc32 else CALLOUT_BG_SC6)),
                    ('LINEBEFORE', (0,0), (0,-1), 2.5, to_color(primary_hex)),
                    ('BOX', (0,0), (-1,-1), 0.5, to_color(DIVIDER_HEX)),
                    ('LEFTPADDING', (0,0), (-1,-1), 8),
                    ('RIGHTPADDING', (0,0), (-1,-1), 8),
                    ('TOPPADDING', (0,0), (-1,-1), 4),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
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
            raw_quote = " ".join(quote_lines)

            # Detect callout badge
            badge_match = re.match(r'^\[!(NOTE|IMPORTANT|TIP|WARNING|CHECKPOINT|TEACHER)\]\s*(.*)$', raw_quote, flags=re.IGNORECASE)
            badge_title = ""
            badge_color = primary_hex
            if badge_match:
                tag = badge_match.group(1).upper()
                raw_quote = badge_match.group(2)
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
                    badge_title = "TEACHER / HOMESCHOOLER SCRIPT // CRA MODEL"
                    badge_color = primary_hex
                else:
                    badge_title = f"{tag} // STACKCALC REFERENCE"
                    badge_color = primary_hex

            sanitized = sanitize_inline_markdown(raw_quote, is_sc32)
            if badge_title:
                sanitized = f"<b><font size='8.5' face='{FONT_BODY_BOLD}' color='{badge_color}'>{badge_title}</font></b><br/><br/>{sanitized}"

            callout_p = make_paragraph(sanitized, styles["CalloutText"])
            callout_tbl = Table([[callout_p]], colWidths=[PRINTABLE_WIDTH])
            callout_tbl.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), to_color(CALLOUT_BG_SC32 if is_sc32 else CALLOUT_BG_SC6)),
                ('LINEBEFORE', (0,0), (0,-1), 3.5, to_color(badge_color)),
                ('BOX', (0,0), (-1,-1), 0.5, to_color(DIVIDER_HEX)),
                ('LEFTPADDING', (0,0), (-1,-1), 10),
                ('RIGHTPADDING', (0,0), (-1,-1), 10),
                ('TOPPADDING', (0,0), (-1,-1), 6),
                ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ]))
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
        if line.startswith("|") and line.endswith("|"):
            table_lines = []
            while i < num_lines and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
                table_lines.append(lines[i].strip())
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
                    col_char_counts = [0] * num_cols
                    hdr_min_widths = [38.0] * num_cols

                    for is_hdr, cells in parsed_rows:
                        row_elements = []
                        while len(cells) < num_cols:
                            cells.append("")
                        if len(cells) > num_cols:
                            cells = cells[:num_cols - 1] + [" | ".join(cells[num_cols - 1:])]
                        for c_idx, cell_str in enumerate(cells):
                            plain_cell = re.sub(r'</?[a-zA-Z][^>]*>', '', sanitize_inline_markdown(cell_str, is_sc32))
                            plain_cell = html.unescape(plain_cell)
                            col_char_counts[c_idx] = max(col_char_counts[c_idx], len(plain_cell))
                            if is_hdr:
                                longest_hdr_word = max((len(w) for w in plain_cell.split()), default=0)
                                # Ensure header words like 'Keystroke' (9 chars) never wrap mid-word
                                hdr_min_widths[c_idx] = max(38.0, min(76.0, longest_hdr_word * 5.2 + 12.0))
                            sanitized = sanitize_inline_markdown(cell_str, is_sc32)
                            cell_style = styles["TableHeader"] if is_hdr else styles["TableCell"]
                            row_elements.append(make_paragraph(sanitized, cell_style))
                        normalized_data.append(row_elements)

                    total_chars = max(1, sum(col_char_counts))
                    col_widths = [(c_cnt / total_chars) * PRINTABLE_WIDTH for c_cnt in col_char_counts]
                    # Respect header word minimum widths while preserving total PRINTABLE_WIDTH
                    if sum(hdr_min_widths) <= PRINTABLE_WIDTH * 0.92:
                        locked = [False] * num_cols
                        for _ in range(num_cols):
                            changed = False
                            for c_idx in range(num_cols):
                                if not locked[c_idx] and col_widths[c_idx] < hdr_min_widths[c_idx]:
                                    col_widths[c_idx] = hdr_min_widths[c_idx]
                                    locked[c_idx] = True
                                    changed = True
                            if not changed:
                                break
                            locked_sum = sum(col_widths[c_idx] for c_idx in range(num_cols) if locked[c_idx])
                            rem_w = max(10.0, PRINTABLE_WIDTH - locked_sum)
                            unlocked_chars = sum(col_char_counts[c_idx] for c_idx in range(num_cols) if not locked[c_idx])
                            if unlocked_chars > 0:
                                for c_idx in range(num_cols):
                                    if not locked[c_idx]:
                                        col_widths[c_idx] = (col_char_counts[c_idx] / unlocked_chars) * rem_w
                    w_sum = sum(col_widths)
                    col_widths = [(w / w_sum) * PRINTABLE_WIDTH for w in col_widths]

                    reportlab_table = Table(normalized_data, colWidths=col_widths, repeatRows=1)
                    reportlab_table.setStyle(TableStyle([
                        ('BACKGROUND', (0,0), (-1,0), to_color(primary_hex)),
                        ('TEXTCOLOR', (0,0), (-1,0), white),
                        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                        ('VALIGN', (0,0), (-1,-1), 'TOP'),
                        ('TOPPADDING', (0,0), (-1,-1), 4),
                        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
                        ('LEFTPADDING', (0,0), (-1,-1), 5),
                        ('RIGHTPADDING', (0,0), (-1,-1), 5),
                        ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, to_color("#f8fafc")]),
                        ('GRID', (0,0), (-1,-1), 0.5, to_color(DIVIDER_HEX)),
                        ('LINEBELOW', (0,0), (-1,0), 1.2, to_color(primary_hex)),
                        ('BOX', (0,0), (-1,-1), 1.0, to_color(primary_hex)),
                    ]))
                    elements.append(Spacer(1, 4))
                    elements.append(reportlab_table)
                    elements.append(Spacer(1, 6))
            continue

        # Heading 1 (# Chapter Title)
        if line.startswith("# "):
            title = line[2:].strip()
            plain_title, styled_title = format_heading_text(title)

            if chapter_idx > 0 or not is_first_h1:
                elements.append(PageBreak())
            is_first_h1 = False

            elements.append(ChapterTracker(plain_title))

            bm_key = f"bm_ch_{chapter_idx}_{i}"
            elements.append(BookmarkFlowable(bm_key, plain_title, level=0))

            h1_p = make_paragraph(styled_title, styles["Heading1"])
            h1_p._toc_info = (0, styled_title, bm_key)
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
            plain_title, styled_title = format_heading_text(title)

            bm_key = f"bm_sec_{chapter_idx}_{i}"
            elements.append(BookmarkFlowable(bm_key, plain_title, level=1))

            h2_p = make_paragraph(styled_title, styles["Heading2"])
            h2_p._toc_info = (1, styled_title, bm_key)
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
            plain_title, styled_title = format_heading_text(title)

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
            plain_title, styled_title = format_heading_text(title)

            h4_p = make_paragraph(styled_title, styles["Heading4"])
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
                REPO_ROOT / raw_path.lstrip("/"),
                DOCS_DIR / raw_path.lstrip("/"),
                REPO_ROOT / "docs" / raw_path.lstrip("/"),
                REPO_ROOT.parent / "watch-calc-32" / raw_path.lstrip("/"),
                REPO_ROOT.parent / "watch-calc-32" / "Education" / raw_path.lstrip("/"),
                REPO_ROOT.parent / "watch-calc-32" / "scratch" / "previews" / "education" / raw_path.lstrip("/"),
                DOCS_DIR / "assets" / "manuals" / "screenshots" / Path(raw_path).name,
                DOCS_DIR / "assets" / "manuals" / Path(raw_path).name,
                DOCS_DIR / "assets" / "renders" / Path(raw_path).name,
            ]
            for c in candidates:
                if c.exists() and c.is_file():
                    resolved_img = c
                    break

            if resolved_img:
                try:
                    with PIL.Image.open(resolved_img) as pimg:
                        orig_w, orig_h = pimg.size
                    max_w = PRINTABLE_WIDTH
                    max_h = 220.0
                    scale = min(max_w / orig_w, max_h / orig_h, 1.0)
                    w = orig_w * scale
                    h = orig_h * scale
                    rl_img = RLImage(str(resolved_img), width=w, height=h)
                    rl_img.hAlign = 'CENTER'
                    elements.append(Spacer(1, 4))
                    elements.append(rl_img)
                    if alt_text:
                        elements.append(make_paragraph(f"<i>Figure: {alt_text}</i>", styles["FigureCaption"]))
                    elements.append(Spacer(1, 6))
                except Exception as ex:
                    print(f"[WARN] Failed to load image {resolved_img}: {ex}")
            else:
                elements.append(make_paragraph(f"<b>[FIGURE: {alt_text}]</b> (Source: {raw_path})", styles["CalloutText"]))
            i += 1
            continue

        # Regular Paragraph
        para_lines = []
        while i < num_lines and lines[i].strip() and not lines[i].startswith("#") and not lines[i].startswith("```") and not lines[i].startswith("|") and not lines[i].startswith(">") and not re.match(r'^\s*[-*]\s+', lines[i]) and not re.match(r'^\s*\d+\.\s+', lines[i]) and not lines[i].startswith("<div") and not lines[i].startswith("![") and not lines[i].startswith("<figure") and not lines[i].startswith("</figure") and not lines[i].startswith("<figcaption"):
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
            elements.append(Spacer(1, 3))

    return elements


# ---------------------------------------------------------------------------
# Manual Compilation Orchestrator
# ---------------------------------------------------------------------------
def compile_manual_pdf(is_sc32: bool) -> Path:
    """Compiles either the SC-32 or SC-6 complete multi-page publication manual."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pdf_filename = "sc32-scientific-manual.pdf" if is_sc32 else "sc6-elementary-manual.pdf"
    output_pdf_path = OUTPUT_DIR / pdf_filename

    print(f"\n=======================================================")
    print(f"Compiling: {output_pdf_path.name}")
    print(f"=======================================================")

    primary_hex = SC32_PRIMARY if is_sc32 else SC6_PRIMARY
    accent_hex = SC32_ACCENT if is_sc32 else SC6_ACCENT
    cover_bg_hex = SC32_COVER_BG if is_sc32 else SC6_COVER_BG
    cover_accent_hex = SC32_COVER_ACCENT if is_sc32 else SC6_COVER_ACCENT
    doc_code = "STK-REF-32-V2" if is_sc32 else "STK-REF-06-V1"

    # Style Sheet Setup
    styles = getSampleStyleSheet()

    styles["Heading1"].fontName = FONT_BODY_BOLD
    styles["Heading1"].fontSize = 20.0
    styles["Heading1"].leading = 24.0
    styles["Heading1"].textColor = to_color(primary_hex)
    styles["Heading1"].keepWithNext = True
    styles["Heading1"].spaceBefore = 0
    styles["Heading1"].spaceAfter = 6

    styles["Heading2"].fontName = FONT_BODY_BOLD
    styles["Heading2"].fontSize = 13.5
    styles["Heading2"].leading = 17.0
    styles["Heading2"].textColor = to_color(primary_hex)
    styles["Heading2"].keepWithNext = True
    styles["Heading2"].spaceBefore = 12
    styles["Heading2"].spaceAfter = 4

    styles["Heading3"].fontName = FONT_BODY_BOLD
    styles["Heading3"].fontSize = 11.0
    styles["Heading3"].leading = 14.0
    styles["Heading3"].textColor = to_color(TEXT_MAIN)
    styles["Heading3"].keepWithNext = True
    styles["Heading3"].spaceBefore = 8
    styles["Heading3"].spaceAfter = 3

    styles["Heading4"].fontName = FONT_BODY_BOLD
    styles["Heading4"].fontSize = 9.8
    styles["Heading4"].leading = 12.5
    styles["Heading4"].textColor = to_color(TEXT_MUTED)
    styles["Heading4"].keepWithNext = True
    styles["Heading4"].spaceBefore = 6
    styles["Heading4"].spaceAfter = 2

    styles["BodyText"].fontName = FONT_BODY
    styles["BodyText"].fontSize = 9.2
    styles["BodyText"].leading = 13.0
    styles["BodyText"].textColor = to_color(TEXT_MAIN)
    styles["BodyText"].spaceAfter = 4

    styles.add(ParagraphStyle(
        "ListBullet",
        parent=styles["BodyText"],
        leftIndent=14,
        firstLineIndent=-9,
        spaceAfter=3,
    ))

    styles.add(ParagraphStyle(
        "TableHeader",
        parent=styles["Normal"],
        fontName=FONT_BODY_BOLD,
        fontSize=8.0,
        leading=10.0,
        textColor=white,
    ))

    styles.add(ParagraphStyle(
        "TableCell",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=7.8,
        leading=9.8,
        textColor=to_color(TEXT_MAIN),
    ))

    styles.add(ParagraphStyle(
        "CalloutText",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=8.8,
        leading=12.2,
        textColor=to_color(TEXT_MAIN),
    ))

    styles.add(ParagraphStyle(
        "FigureCaption",
        parent=styles["Normal"],
        fontName=FONT_BODY_ITALIC,
        fontSize=8.2,
        leading=11.0,
        textColor=to_color(TEXT_MUTED),
        alignment=1,
        spaceBefore=3,
        spaceAfter=6,
    ))

    # LCD display and monospaced stack frame text: Terminus LCD font on white paper
    styles.add(ParagraphStyle(
        "CodePreformatted",
        fontName=FONT_DISPLAY,
        fontSize=7.2,
        leading=9.0,
        textColor=to_color(TEXT_MAIN),
    ))

    # Chapter Ordering
    if is_sc32:
        manual_dir = DOCS_DIR / "manuals" / "sc32"
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
        doc_title = "STACKCALC SC-32 SCIENTIFIC MANUAL"
    else:
        manual_dir = DOCS_DIR / "manuals" / "sc6"
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
        doc_title = "STACKCALC SC-6 ELEMENTARY MANUAL"

    # Assemble Flowables
    story: List[Flowable] = []

    # 1. Build Cover Page (Monolithic Dark Wrap)
    story.extend(build_cover_page(is_sc32, styles))

    # 2. Table of Contents (Two-Pass Auto-Updated with Dot Leaders)
    story.append(ChapterTracker("TABLE OF CONTENTS"))
    story.append(BookmarkFlowable("bm_toc", "Table of Contents", level=0))
    toc_heading = make_paragraph("Table of Contents", styles["Heading1"])
    story.append(toc_heading)
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=1.5, color=to_color(primary_hex), spaceAfter=12))

    toc = TableOfContents()
    toc.dotsMinLevel = 0
    toc_level0 = ParagraphStyle(
        "TOCLevel0",
        parent=styles["Normal"],
        fontName=FONT_BODY_BOLD,
        fontSize=9.2,
        leading=12.5,
        textColor=to_color(primary_hex),
        spaceBefore=5,
        spaceAfter=1,
    )
    toc_level1 = ParagraphStyle(
        "TOCLevel1",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=8.2,
        leading=10.8,
        leftIndent=12,
        textColor=to_color(TEXT_MAIN),
        spaceBefore=1.5,
        spaceAfter=0.5,
    )
    toc_level2 = ParagraphStyle(
        "TOCLevel2",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=7.8,
        leading=10.0,
        leftIndent=22,
        textColor=to_color(TEXT_MUTED),
        spaceBefore=1.0,
        spaceAfter=0.5,
    )
    toc.levelStyles = [toc_level0, toc_level1, toc_level2]
    story.append(toc)
    story.append(PageBreak())

    # 3. Parse and Append Each Chapter (Archival White Paper Interior)
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
    story.append(HRFlowable(width="100%", thickness=1.5, color=to_color(primary_hex), spaceAfter=12))

    idx = SimpleIndex(dot=' . ')
    idx_head = ParagraphStyle(
        "IndexAlphaHead",
        parent=styles["Heading2"],
        fontName=FONT_BODY_BOLD,
        fontSize=11.0,
        leading=14.0,
        textColor=to_color(primary_hex),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True,
    )
    idx_entry = ParagraphStyle(
        "IndexEntryStyle",
        parent=styles["Normal"],
        fontName=FONT_BODY,
        fontSize=8.2,
        leading=11.0,
        textColor=to_color(TEXT_MAIN),
    )
    idx.setup(style=idx_entry, dot=' . ', headers=True)
    idx.textStyle = [idx_head, idx_entry]
    story.append(idx)

    # Document Geometry (0.75 in / 54 pt margins)
    doc = ManualDocTemplate(
        str(output_pdf_path),
        pagesize=letter,
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

    if build_both or args.sc6_only:
        compile_manual_pdf(is_sc32=False)

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
