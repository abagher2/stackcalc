#!/usr/bin/env python3
"""
Shared Paper-Theme Keycap Renderer & Bestseller Cover Engine for the 4 StackCalc
US Letter (8.5" x 11") Curriculum & Student Workbook Volumes:

  1. Book 1: Teaching with the Stack — Unified Master Teacher's Guide by Concept
  2. Book 2: Hands-On Math Lab — General K–12 Student Exploration Workbook
  3. Book 3: Middle School Math Lab — Big Ideas Math (Grades 6–8) Student Workbook
  4. Book 4: Stack Speed & Fluency — Student Speed & Proficiency Trials Workbook

Directly reuses the authoritative Paper-theme keycap atlas and Bestseller cover
typography from `Tools/generate_manual_pdfs.py` and `Tools/book_engine.py`.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Sequence, Tuple, Union

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

from book_engine import get_registry, normalize_key_token
from generate_manual_pdfs import (
    FONT_BODY,
    FONT_BODY_BOLD,
    FONT_BODY_ITALIC,
    FONT_MONO,
    FONT_MONO_BOLD,
    _KEYCAP_CACHE_DIR,
    _ensure_paper_keycap_atlas,
    _get_fallback_paper_keycap,
    draw_vector_isbn_barcode,
    format_hardware_keycap_cartouche,
    to_color,
)


_DISK_ATLAS_FALLBACK = {}


def _get_atlas_safe(is_sc32: bool):
    """Loads the Paper-theme keycap atlas, falling back to cached PNGs on disk if numpy/scipy is absent."""
    try:
        return _ensure_paper_keycap_atlas(is_sc32)
    except ImportError:
        if is_sc32 in _DISK_ATLAS_FALLBACK:
            return _DISK_ATLAS_FALLBACK[is_sc32]
        from PIL import Image
        model_slug = "sc32" if is_sc32 else "sc6"
        out_dir = _KEYCAP_CACHE_DIR / model_slug
        atlas = {}
        if out_dir.exists():
            for p in out_dir.glob("*.png"):
                m = re.match(r"^(primary|yellow|blue)_r(\d+)_c(\d+)\.png$", p.name)
                if m:
                    layer, r_s, c_s = m.group(1), int(m.group(2)), int(m.group(3))
                    with Image.open(p) as im:
                        atlas[(layer, r_s, c_s)] = (p, im.width, im.height)
        _DISK_ATLAS_FALLBACK[is_sc32] = atlas
        return atlas

# Legacy alias map from older curriculum scripts to canonical SC-6 / SC-32 keys
LEGACY_KEY_MAP = {
    "plus": "+",
    "minus": "-",
    "times": "×",
    "*": "×",
    "divide": "÷",
    "/": "÷",
    "dot": ".",
    "enter": "ENTER",
    "plus_minus": "+/-",
    "chs": "+/-",
    "x_swap_y": "x⇄y",
    "swap": "x⇄y",
    "y_to_x": "yˣ",
    "y^x": "yˣ",
    "sigma_plus": "Σ+",
    "yellow_▸θ_r": "▸θ,r",
    "▸θ_r": "▸θ,r",
    "toPolar": "▸θ,r",
    "toRectangular": "▸y,x",
    "▸y_x": "▸y,x",
    "yellow_𝑥!": "x!",
    "yellow_x!": "x!",
    "𝑥!": "x!",
    "yellow_base": "BASE",
    "ln": "LN",
    "sin": "SIN",
    "cos": "COS",
    "tan": "TAN",
    "asin": "ASIN",
    "acos": "ACOS",
    "atan": "ATAN",
    "and": "AND",
    "or": "OR",
    "xor": "XOR",
    "𝑒ˣ": "eˣ",
    "√𝑥": "√x",
    "¹/𝑥": "1/x",
    "x⁻¹": "1/x",
}


def normalize_and_split_key_tokens(
    raw_input: Union[str, Sequence[str]],
    is_sc32: bool = False,
) -> List[str]:
    """
    Converts any raw keystroke sequence (list of tokens or bracketed string) into
    an exact sequence of atomic physical button presses on the SC-6 or SC-32.
    - Multi-digit numbers like '10', '255', '0.07' or two-dot fractions like '.3.4', '2.1.2'
      are split into individual physical digit/dot keys ('1', '0', '.', '3', '.', '4').
    - Composite strings like '12 ENTER 4 -' or '4 sigma_plus' are split cleanly.
    - Shifted keys automatically receive their authentic shift prefix ('f'/'g' on SC-6,
      '↰'/'↱' on SC-32) without duplicating an existing shift prefix.
    """
    if isinstance(raw_input, str):
        # Extract bracketed tokens if present, or whitespace tokens
        s = raw_input.strip()
        if "[" in s and "]" in s:
            # Split into bracketed chunks and non-bracketed chunks
            parts = re.findall(r"\[([^\]]+)\]|([^\s\[\]]+)", s)
            raw_list = [a if a else b for a, b in parts if (a or b)]
        else:
            raw_list = s.split()
    else:
        raw_list = []
        for item in raw_input:
            item_s = str(item).strip()
            if not item_s:
                continue
            if " " in item_s and item_s not in ("a ᵇ/c", "a b/c"):
                for sub in item_s.split():
                    raw_list.append(sub.strip("[]"))
            else:
                raw_list.append(item_s.strip("[]"))

    atomic_tokens: List[str] = []
    for tok in raw_list:
        t = tok.strip()
        if not t:
            continue
        if t in ("a b/c", "a ᵇ/c"):
            atomic_tokens.append("a ᵇ/c")
            continue
        if t in LEGACY_KEY_MAP:
            t = LEGACY_KEY_MAP[t]
        elif t.lower() in LEGACY_KEY_MAP:
            t = LEGACY_KEY_MAP[t.lower()]

        # Drop generic 'yellow' or 'blue' shift words because registry resolution adds the exact shift key
        if t.lower() in ("yellow", "blue"):
            continue

        # Check if token is purely digits and decimal points (e.g. '10', '0.07', '.3.4', '2.1.2', '1000')
        if len(t) > 1 and re.fullmatch(r"[0-9.]+", t):
            for ch in t:
                atomic_tokens.append(ch)
            continue

        # Check if token is negative number like '-2'
        if len(t) > 1 and re.fullmatch(r"-[0-9.]+", t):
            for ch in t[1:]:
                atomic_tokens.append(ch)
            atomic_tokens.append("+/-")
            continue

        atomic_tokens.append(t)

    # Now resolve each atomic token through KeyRegistry and insert shift prefixes where needed
    reg_primary = get_registry(is_sc32)
    reg_alt = get_registry(not is_sc32)
    shift_keys = {"f", "g", "↰", "↱"}

    final_keys: List[str] = []
    for tok in atomic_tokens:
        entry = None
        for reg in (reg_primary, reg_alt):
            try:
                entry = reg.resolve(tok)
                break
            except ValueError:
                continue
        if entry is not None:
            if entry.shift:
                # Only prepend shift if the immediately preceding token isn't already a shift key
                if not final_keys or final_keys[-1] not in shift_keys:
                    final_keys.append(entry.shift)
                else:
                    # Replace generic f/g with the target model's shift key
                    final_keys[-1] = entry.shift
            final_keys.append(entry.canonical)
        else:
            final_keys.append(normalize_key_token(tok))

    return final_keys


def get_paper_keycap_png(key_token: str, is_sc32: bool = False) -> Tuple[Path, int, int, str]:
    """
    Returns `(png_path, px_width, px_height, layer_kind)` for a single canonical key token
    using the exact Paper-theme keycap atlas from `Tools/generate_manual_pdfs.py`.
    """
    clean_k = key_token.strip()
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
            try_atlas = _get_atlas_safe(try_sc32)
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

    return png_info[0], png_info[1], png_info[2], layer_kind


def draw_paper_keycap_sequence(
    c: canvas.Canvas,
    x: float,
    y: float,
    raw_tokens: Union[str, Sequence[str]],
    is_sc32: bool = False,
    height: float = 11.5,
    spacing: float = 2.5,
    max_width: Optional[float] = None,
) -> float:
    """
    Draws a sequence of authentic Paper-theme SC-6 / SC-32 keycap PNGs onto `c` at `(x, y)`.
    Automatically scales down if `max_width` is provided and the row would exceed `max_width`.
    Returns the final x coordinate after the last drawn keycap.
    """
    keys = normalize_and_split_key_tokens(raw_tokens, is_sc32=is_sc32)
    if not keys:
        return x

    items = []
    for k in keys:
        p_path, px_w, px_h, layer_kind = get_paper_keycap_png(k, is_sc32=is_sc32)
        h_pt = height * (0.88 if layer_kind in ("yellow", "blue") else 1.0)
        w_pt = h_pt * (px_w / float(max(1, px_h)))
        items.append((p_path, w_pt, h_pt, layer_kind))

    total_w = sum(it[1] for it in items) + spacing * max(0, len(items) - 1)
    scale = 1.0
    if max_width and total_w > max_width and total_w > 0:
        scale = max(0.42, max_width / total_w)

    cur_x = x
    for p_path, w_pt, h_pt, layer_kind in items:
        sw = w_pt * scale
        sh = h_pt * scale
        dy = (height * scale - sh) * 0.5
        c.drawImage(
            str(p_path),
            cur_x,
            y + dy,
            width=sw,
            height=sh,
            preserveAspectRatio=True,
            mask="auto",
        )
        cur_x += sw + (spacing * scale)

    return cur_x


def format_paper_keycaps_inline_html(
    raw_tokens: Union[str, Sequence[str]],
    is_sc32: bool = False,
    target_h_pt: float = 8.8,
) -> str:
    """
    Returns an inline HTML string of Paper-theme `<img .../>` keycaps suitable for ReportLab Paragraphs.
    """
    keys = normalize_and_split_key_tokens(raw_tokens, is_sc32=is_sc32)
    return " ".join(format_hardware_keycap_cartouche(k, is_sc32=is_sc32, target_h_pt=target_h_pt) for k in keys)


@dataclass
class CurriculumBookCoverSpec:
    book_id: str                # "teacher_guide", "student_lab", "big_ideas", "proficiency_trials"
    title_line_1: str           # e.g. "TEACHING WITH"
    title_line_2: str           # e.g. "THE STACK"
    subtitle: str               # e.g. "Hands-On Mathematics & Concept Facilitation Guide (K–12)"
    edition_badge: str          # e.g. "UNIFIED MASTER TEACHER'S EDITION  •  US LETTER (8.5 × 11 IN)"
    accent_hex: str             # e.g. "#059669"
    category_line: str          # e.g. "MATHEMATICS  /  CURRICULUM & INSTRUCTION"
    hook_line_1: str
    hook_line_2: str
    paragraph_1_html: str
    paragraph_2_html: str
    inside_note_html: str
    isbn_hyphenated: str
    isbn_digits: str
    price_label: str = "$24.00 US  •  CAN $32.99"


BOOK_COVER_SPECS = {
    "teacher_guide": CurriculumBookCoverSpec(
        book_id="teacher_guide",
        title_line_1="TEACHING WITH",
        title_line_2="THE STACK",
        subtitle="Hands-On Mathematics & Concept Facilitation Guide (K–12)",
        edition_badge="UNIFIED TEACHER'S CONCEPT GUIDE  •  GRADES K–12",
        accent_hex="#059669",
        category_line="MATHEMATICS  /  TEACHING & CURRICULUM",
        hook_line_1="How do you turn abstract math symbols",
        hook_line_2="into concepts students can hold?",
        paragraph_1_html=(
            "Great mathematics instruction moves from concrete physical models to visual representations "
            "and finally to fluent symbolic reasoning. When students build a quantity with physical math blocks, "
            "predict the outcome, and watch those exact numbers move across a four-level RPN stack, "
            "arithmetic and algebra become transparent from the inside out."
        ),
        paragraph_2_html=(
            "Organized by <b>mathematical concept rather than isolated textbook chapters</b>, "
            "<b>Teaching with the Stack</b> unifies K–12 hands-on math lab facilitation with middle school "
            "<b>Big Ideas Math</b> coaching notes, cross-curriculum pacing tables for <b>Singapore Math</b> and "
            "<b>Bridges in Mathematics</b>, misconception diagnostics, and complete worked answer keys."
        ),
        inside_note_html=(
            "<b>Inside the Master Teacher's Guide:</b> 12 Concept Domains (Pre-K to AP)  •  Cross-curriculum alignment index  "
            "•  Big Ideas Math Grades 6–8 teaching notes  •  Diagnostic remediations &amp; complete answer keys."
        ),
        isbn_hyphenated="979-8-9914832-3-0",
        isbn_digits="9798991483230",
        price_label="$29.00 US  •  CAN $38.99",
    ),
    "student_lab": CurriculumBookCoverSpec(
        book_id="student_lab",
        title_line_1="HANDS-ON",
        title_line_2="MATH LAB",
        subtitle="Student Explorations from Physical Blocks to the Stack",
        edition_badge="STUDENT LAB WORKBOOK  •  UNITS 1–12",
        accent_hex="#0D9488",
        category_line="MATHEMATICS  /  STUDENT LAB WORKBOOK",
        hook_line_1="Build it with blocks. Predict the pattern.",
        hook_line_2="Prove it on the stack.",
        paragraph_1_html=(
            "Every mathematical idea in this workbook begins in your hands. Before you write an equation "
            "or press a calculator key, you will arrange Place Value Digit &amp; Carry Blocks, 84 mm Fraction Towers, "
            "or Logarithmic Prime Factor Blocks on your desk to see why the pattern works."
        ),
        paragraph_2_html=(
            "Designed as the student lab companion to <b>From Blocks to the Stack</b> (SC-6) and "
            "<b>Thinking in the Stack</b> (SC-32), <b>Hands-On Math Lab</b> guides learners through "
            "12 progressive concept investigations with visual block sketches, guided stack walkthroughs, "
            "structured lab recording sheets, and a self-check answer key."
        ),
        inside_note_html=(
            "<b>Inside the Student Lab Workbook:</b> 12 Hands-On Lab Units  •  Story openers &amp; visual block rules  "
            "•  Guided SC-6 &amp; SC-32 stack traces  •  72 structured lab investigations &amp; student answer key."
        ),
        isbn_hyphenated="979-8-9914832-4-7",
        isbn_digits="9798991483247",
        price_label="$19.00 US  •  CAN $25.99",
    ),
    "big_ideas": CurriculumBookCoverSpec(
        book_id="big_ideas",
        title_line_1="MIDDLE SCHOOL",
        title_line_2="MATH LAB",
        subtitle="Student Practice Workbook for Big Ideas Math (Grades 6–8)",
        edition_badge="BIG IDEAS MATH COMPANION  •  10 UNITS / 900 PROBLEMS",
        accent_hex="#0284C7",
        category_line="MATHEMATICS  /  MIDDLE SCHOOL WORKBOOK",
        hook_line_1="Why solve a problem only one way when",
        hook_line_2="three perspectives make it unforgettable?",
        paragraph_1_html=(
            "Middle school is the bridge between elementary arithmetic and high school algebra. "
            "When students solve every section three ways—by hand on paper, with physical math blocks, "
            "and step-by-step on the <b>StackCalc SC-6</b> four-register stack—ratios, fractions, integers, "
            "equations, geometry, and statistics lock into place."
        ),
        paragraph_2_html=(
            "Aligned section-by-section to the <b>Big Ideas Math Middle School</b> sequence (Grades 6–8), "
            "this workbook delivers 45 core sections, 90 tiered Practice A &amp; Practice B worksheets, "
            "900 multi-method problems, chapter stories from <b>From Blocks to the Stack</b>, and a complete "
            "back-of-book student answer key."
        ),
        inside_note_html=(
            "<b>Inside the Workbook:</b> 10 Middle School Units  •  45 Concept Openers &amp; Worked Examples  "
            "•  90 Practice A &amp; B Worksheets (900 problems)  •  Complete self-check answer key."
        ),
        isbn_hyphenated="979-8-9914832-5-4",
        isbn_digits="9798991483254",
        price_label="$24.00 US  •  CAN $32.99",
    ),
    "proficiency_trials": CurriculumBookCoverSpec(
        book_id="proficiency_trials",
        title_line_1="STACK SPEED",
        title_line_2="& FLUENCY",
        subtitle="15 Speed Lessons, Shortcut Playbooks & 60 Progressive Practice Tests (Levels 1–4)",
        edition_badge="SPEED LESSONS & PROGRESSIVE PRACTICE TESTS  •  15 LESSONS / 60 TESTS",
        accent_hex="#FF4F00",
        category_line="MATHEMATICS  /  SPEED LESSONS & FLUENCY PRACTICE TESTS",
        hook_line_1="Learn the Champion Way first—then build",
        hook_line_2="speed across four progressive test levels.",
        paragraph_1_html=(
            "Taking timed tests without learning faster methods only makes slow habits permanent. Every section in "
            "<b>Stack Speed &amp; Fluency</b> opens with a <b>1-Page Speed Lesson &amp; Shortcut Playbook</b> contrasting "
            "the <i>Slow / Amateur Way</i> against the <i>Champion Speed Way</i>, followed by 6 untimed guided warm-up "
            "drills so students master algebraic shortcuts and zero-memory stack pipelines before starting the timer."
        ),
        paragraph_2_html=(
            "Designed for homeschooling families, classrooms, and competitive math/calculator teams, each section then "
            "provides four 20-problem practice tests in increasing difficulty—<b>Test A (Level 1: Foundation)</b>, "
            "<b>Test B (Level 2: Core Fluency)</b>, <b>Test C (Level 3: Multi-Step Speed)</b>, and <b>Test D (Level 4: "
            "Advanced Challenge)</b>—plus complete answer keys with Optimal Champion Pipelines."
        ),
        inside_note_html=(
            "<b>Inside the Workbook:</b> 15 Speed Lessons &amp; 'Slow vs. Champion' Playbooks  •  90 Guided Warm-Up Drills  "
            "•  60 Progressive Practice Tests (1,200 problems)  •  Answer keys with Optimal Champion Pipelines."
        ),
        isbn_hyphenated="979-8-9914832-6-1",
        isbn_digits="9798991483261",
        price_label="$19.00 US  •  CAN $25.99",
    ),
}


def _draw_cover_centerpiece_illustration(
    c: canvas.Canvas,
    cx: float,
    cy: float,
    book_id: str,
    accent_hex: str,
) -> None:
    """
    Draws a clean, minimalist, unboxed geometric vector illustration floating in the open
    center of the Warm Archival Paper (#F7F4EB) cover, tailored to each of the 4 books.
    """
    c.saveState()
    if book_id == "teacher_guide":
        # Left side: 1-2-3-4 Tactile Block Staircase; Right side: 4-Level Stack Bars (T, Z, Y, X)
        block_sz = 30.0
        block_gap = 6.0
        stair_w = 4 * block_sz + 3 * block_gap
        left_x = cx - 170.0
        base_y = cy - 68.0
        rows_spec = [
            (0, 4, "#059669"),
            (1, 3, "#0284C7"),
            (2, 2, "#F59E0B"),
            (3, 1, "#E11D48"),
        ]
        for r_idx, count, col_hex in rows_spec:
            ry = base_y + r_idx * (block_sz + block_gap)
            row_start_x = left_x + (4 - count) * (block_sz + block_gap)
            for c_idx in range(count):
                bx = row_start_x + c_idx * (block_sz + block_gap)
                c.setFillColor(to_color("#E2DDD0"))
                c.roundRect(bx + 2.0, ry - 2.0, block_sz, block_sz, 5.0, fill=1, stroke=0)
                c.setFillColor(to_color(col_hex))
                c.roundRect(bx, ry, block_sz, block_sz, 5.0, fill=1, stroke=0)
                c.setStrokeColor(to_color("#FFFFFF"))
                c.setLineWidth(0.8)
                c.circle(bx + block_sz * 0.5, ry + block_sz * 0.5, 5.8, fill=0, stroke=1)

        # Connecting arrow
        c.setStrokeColor(to_color("#64748B"))
        c.setLineWidth(1.8)
        c.line(cx - 12.0, cy, cx + 14.0, cy)
        c.line(cx + 8.0, cy + 5.0, cx + 14.0, cy)
        c.line(cx + 8.0, cy - 5.0, cx + 14.0, cy)

        # Right side: 4 Stack Bars (T, Z, Y, X)
        bar_x = cx + 28.0
        bar_w = 148.0
        bar_h = 26.0
        bar_gap = 10.0
        top_bar_y = base_y + 3 * (bar_h + bar_gap)
        stack_bars = [
            ("T", "1.0000", "#E6E1D3", "#64748B", "#475569"),
            ("Z", "2.0000", "#DCD6C6", "#475569", "#334155"),
            ("Y", "3.0000", "#1E293B", "#94A3B8", "#FFFFFF"),
            ("X", "4.0000", "#059669", "#D1FAE5", "#FFFFFF"),
        ]
        for idx_b, (lbl, val, fill_hex, lbl_hex, val_hex) in enumerate(stack_bars):
            by = top_bar_y - idx_b * (bar_h + bar_gap)
            c.setFillColor(to_color(fill_hex))
            c.roundRect(bar_x, by, bar_w, bar_h, 4.5, fill=1, stroke=0)
            c.setFont(FONT_MONO_BOLD, 9.5)
            c.setFillColor(to_color(lbl_hex))
            c.drawString(bar_x + 10.0, by + 8.5, lbl)
            c.setFont(FONT_MONO_BOLD, 11.0)
            c.setFillColor(to_color(val_hex))
            c.drawRightString(bar_x + bar_w - 10.0, by + 8.0, val)

    elif book_id == "student_lab":
        # Proportional 84mm Fraction Towers side-by-side (1 Whole, 1/2 + 1/2, 1/3 + 1/3 + 1/3, 1/4 x 4)
        tower_w = 38.0
        tower_gap = 14.0
        full_h = 144.0
        total_w = 4 * tower_w + 3 * tower_gap
        sx = cx - total_w * 0.5
        by = cy - full_h * 0.5

        towers = [
            [(1.0, "#1E293B", "1", "#FFFFFF")],
            [(0.5, "#E11D48", "1/2", "#FFFFFF"), (0.5, "#E11D48", "1/2", "#FFFFFF")],
            [(1/3, "#F59E0B", "1/3", "#0F172A"), (1/3, "#F59E0B", "1/3", "#0F172A"), (1/3, "#F59E0B", "1/3", "#0F172A")],
            [(0.25, "#0D9488", "1/4", "#FFFFFF")] * 4,
        ]
        for t_idx, segs in enumerate(towers):
            tx = sx + t_idx * (tower_w + tower_gap)
            cur_y = by
            for frac, col_hex, lbl, txt_hex in segs:
                sh = full_h * frac - 2.0
                c.setFillColor(to_color("#E2DDD0"))
                c.roundRect(tx + 2.0, cur_y - 2.0, tower_w, sh, 4.0, fill=1, stroke=0)
                c.setFillColor(to_color(col_hex))
                c.roundRect(tx, cur_y, tower_w, sh, 4.0, fill=1, stroke=0)
                c.setFont(FONT_MONO_BOLD, 9.5)
                c.setFillColor(to_color(txt_hex))
                c.drawCentredString(tx + tower_w * 0.5, cur_y + sh * 0.5 - 3.5, lbl)
                cur_y += full_h * frac

    elif book_id == "big_ideas":
        # Prime Factor Towers (2×2×3 = 12 and 2×3×3 = 18 -> GCF = 6, LCM = 36) paired with Stack Registers
        left_x = cx - 165.0
        base_y = cy - 68.0
        tower_w = 42.0
        # Tower 1: 12 = 2 * 2 * 3
        t1_segs = [
            (38.0, "#E11D48", "×2", "#FFFFFF"),
            (38.0, "#E11D48", "×2", "#FFFFFF"),
            (54.0, "#F59E0B", "×3", "#0F172A"),
        ]
        cur_y = base_y
        for sh, col_hex, lbl, txt_hex in t1_segs:
            c.setFillColor(to_color("#E2DDD0"))
            c.roundRect(left_x + 2.0, cur_y - 2.0, tower_w, sh - 3.0, 4.0, fill=1, stroke=0)
            c.setFillColor(to_color(col_hex))
            c.roundRect(left_x, cur_y, tower_w, sh - 3.0, 4.0, fill=1, stroke=0)
            c.setFont(FONT_MONO_BOLD, 10.0)
            c.setFillColor(to_color(txt_hex))
            c.drawCentredString(left_x + tower_w * 0.5, cur_y + (sh - 3.0) * 0.5 - 3.5, lbl)
            cur_y += sh

        # Tower 2: 18 = 2 * 3 * 3
        t2_x = left_x + 56.0
        t2_segs = [
            (38.0, "#E11D48", "×2", "#FFFFFF"),
            (54.0, "#F59E0B", "×3", "#0F172A"),
            (54.0, "#F59E0B", "×3", "#0F172A"),
        ]
        cur_y = base_y
        for sh, col_hex, lbl, txt_hex in t2_segs:
            c.setFillColor(to_color("#E2DDD0"))
            c.roundRect(t2_x + 2.0, cur_y - 2.0, tower_w, sh - 3.0, 4.0, fill=1, stroke=0)
            c.setFillColor(to_color(col_hex))
            c.roundRect(t2_x, cur_y, tower_w, sh - 3.0, 4.0, fill=1, stroke=0)
            c.setFont(FONT_MONO_BOLD, 10.0)
            c.setFillColor(to_color(txt_hex))
            c.drawCentredString(t2_x + tower_w * 0.5, cur_y + (sh - 3.0) * 0.5 - 3.5, lbl)
            cur_y += sh

        # Right side: 4 Stack Bars (T, Z, Y, X) showing GCF & LCM
        bar_x = cx + 10.0
        bar_w = 158.0
        bar_h = 26.0
        bar_gap = 10.0
        top_bar_y = base_y + 3 * (bar_h + bar_gap)
        stack_bars = [
            ("T", "12.000", "#E6E1D3", "#64748B", "#475569"),
            ("Z", "18.000", "#DCD6C6", "#475569", "#334155"),
            ("Y", "GCF: 6", "#1E293B", "#94A3B8", "#FFFFFF"),
            ("X", "LCM: 36", "#0284C7", "#E0F2FE", "#FFFFFF"),
        ]
        for idx_b, (lbl, val, fill_hex, lbl_hex, val_hex) in enumerate(stack_bars):
            by = top_bar_y - idx_b * (bar_h + bar_gap)
            c.setFillColor(to_color(fill_hex))
            c.roundRect(bar_x, by, bar_w, bar_h, 4.5, fill=1, stroke=0)
            c.setFont(FONT_MONO_BOLD, 9.5)
            c.setFillColor(to_color(lbl_hex))
            c.drawString(bar_x + 10.0, by + 8.5, lbl)
            c.setFont(FONT_MONO_BOLD, 11.0)
            c.setFillColor(to_color(val_hex))
            c.drawRightString(bar_x + bar_w - 10.0, by + 8.0, val)

    else:
        # Proficiency Trials: Struck-through Parenthesis Trap + 4 Floating Stack Bars
        expr_y = cy + 68.0
        c.setFont(FONT_MONO, 18.0)
        c.setFillColor(to_color("#64748B"))
        c.drawCentredString(cx, expr_y, "( 3 + 4 ) × ( 5 + 6 )")

        c.setStrokeColor(to_color(accent_hex))
        c.setLineWidth(2.8)
        c.setLineCap(1)
        c.line(cx - 108.0, expr_y - 4.0, cx + 108.0, expr_y + 16.0)

        bar_w = 204.0
        bar_h = 26.0
        bar_gap = 10.0
        bar_x = cx - (bar_w * 0.5)
        top_bar_y = cy + 16.0
        stack_bars = [
            ("T", "0.0000", "#E6E1D3", "#64748B", "#64748B"),
            ("Z", "7.0000", "#DCD6C6", "#475569", "#334155"),
            ("Y", "5.0000", "#1E293B", "#94A3B8", "#FFFFFF"),
            ("X", "6.0000", "#FF4F00", "#FFE4D6", "#FFFFFF"),
        ]
        for idx_b, (lbl, val, fill_hex, lbl_hex, val_hex) in enumerate(stack_bars):
            by = top_bar_y - idx_b * (bar_h + bar_gap)
            c.setFillColor(to_color(fill_hex))
            c.roundRect(bar_x, by, bar_w, bar_h, 4.5, fill=1, stroke=0)
            c.setFont(FONT_MONO_BOLD, 10.0)
            c.setFillColor(to_color(lbl_hex))
            c.drawString(bar_x + 12.0, by + 8.5, lbl)
            c.setFont(FONT_MONO_BOLD, 11.5)
            c.setFillColor(to_color(val_hex))
            c.drawRightString(bar_x + bar_w - 12.0, by + 8.0, val)

    c.restoreState()


def draw_curriculum_bestseller_front_cover(
    c: canvas.Canvas,
    ox: float,
    oy: float,
    w: float,
    h: float,
    spec: CurriculumBookCoverSpec,
    bleed_l: float = 0.0,
    bleed_r: float = 0.0,
    bleed_t: float = 0.0,
    bleed_b: float = 0.0,
) -> None:
    """
    Renders a US Letter (8.5" x 11") Bestseller minimalist Front Cover on Warm Archival Paper (#F7F4EB),
    matching our SC-6 and SC-32 flagship book covers.
    """
    c.saveState()

    paper_cream = "#F7F4EB"
    ink_obsidian = "#0F172A"
    ink_slate = "#475569"

    # 1. Continuous Warm Archival Paper Background (#F7F4EB)
    c.setFillColor(to_color(paper_cream))
    c.rect(
        ox - bleed_l,
        oy - bleed_b,
        w + bleed_l + bleed_r,
        h + bleed_t + bleed_b,
        fill=1,
        stroke=0,
    )

    cx = ox + (w * 0.5)

    # Subtle top edition line
    c.setFont(FONT_MONO_BOLD, 8.5)
    c.setFillColor(to_color(spec.accent_hex))
    c.drawCentredString(cx, oy + h - 86.0, spec.edition_badge)

    # 2. Monumental Centered Bestseller Title (Upper Third)
    c.setFillColor(to_color(ink_obsidian))
    c.setFont(FONT_BODY_BOLD, 46.0)
    c.drawCentredString(cx, oy + h - 152.0, spec.title_line_1)
    c.drawCentredString(cx, oy + h - 208.0, spec.title_line_2)

    # 3. Concise Italic Subtitle
    c.setFont(FONT_BODY_ITALIC, 15.0)
    c.setFillColor(to_color(ink_slate))
    c.drawCentredString(cx, oy + h - 248.0, spec.subtitle)

    # 4. Minimalist Centerpiece Vector Illustration
    _draw_cover_centerpiece_illustration(c, cx, oy + h * 0.43, spec.book_id, spec.accent_hex)

    # 5. Minimalist Single-Word Imprint at the Foot
    c.setFillColor(to_color(spec.accent_hex))
    c.rect(cx - 18.0, oy + 96.0, 36.0, 3.0, fill=1, stroke=0)

    c.setFillColor(to_color(ink_obsidian))
    c.setFont(FONT_BODY_BOLD, 16.0)
    c.drawCentredString(cx, oy + 68.0, "StackCalc")

    c.restoreState()


def draw_curriculum_bestseller_back_cover(
    c: canvas.Canvas,
    ox: float,
    oy: float,
    w: float,
    h: float,
    spec: CurriculumBookCoverSpec,
    bleed_l: float = 0.0,
    bleed_r: float = 0.0,
    bleed_t: float = 0.0,
    bleed_b: float = 0.0,
) -> None:
    """
    Renders a US Letter (8.5" x 11") Bestseller minimalist Back Cover on Warm Archival Paper (#F7F4EB),
    matching our SC-6 and SC-32 flagship book covers.
    """
    c.saveState()

    paper_cream = "#F7F4EB"
    ink_obsidian = "#0F172A"
    ink_slate = "#334155"
    ink_muted = "#64748B"

    # 1. Continuous Warm Archival Paper Background (#F7F4EB)
    c.setFillColor(to_color(paper_cream))
    c.rect(
        ox - bleed_l,
        oy - bleed_b,
        w + bleed_l + bleed_r,
        h + bleed_t + bleed_b,
        fill=1,
        stroke=0,
    )

    safe_x = ox + 64.0
    safe_w = w - 128.0

    # 2. Quiet Category Line at Top Left
    c.setFont(FONT_MONO_BOLD, 8.5)
    c.setFillColor(to_color(ink_muted))
    c.drawString(safe_x, oy + h - 72.0, spec.category_line)

    # 3. Bold Hook Question
    c.setFillColor(to_color(ink_obsidian))
    c.setFont(FONT_BODY_BOLD, 21.0)
    c.drawString(safe_x, oy + h - 122.0, spec.hook_line_1)
    c.drawString(safe_x, oy + h - 148.0, spec.hook_line_2)

    # Short accent bar under hook question
    c.setFillColor(to_color(spec.accent_hex))
    c.rect(safe_x, oy + h - 166.0, 52.0, 3.0, fill=1, stroke=0)

    body_style = ParagraphStyle(
        f"BackCoverBody_{spec.book_id}",
        fontName=FONT_BODY,
        fontSize=11.5,
        leading=17.5,
        textColor=to_color(ink_slate),
    )
    p1 = Paragraph(spec.paragraph_1_html, body_style)
    _, h1 = p1.wrap(safe_w, 200.0)
    y_cursor = oy + h - 192.0 - h1
    p1.drawOn(c, safe_x, y_cursor)

    p2 = Paragraph(spec.paragraph_2_html, body_style)
    _, h2 = p2.wrap(safe_w, 200.0)
    y_cursor = y_cursor - 18.0 - h2
    p2.drawOn(c, safe_x, y_cursor)

    # 4. Minimalist Desk-Reference Note between hairline rules
    rule_y1 = y_cursor - 28.0
    c.setStrokeColor(to_color("#D6D1C2"))
    c.setLineWidth(0.85)
    c.line(safe_x, rule_y1, safe_x + safe_w, rule_y1)

    note_style = ParagraphStyle(
        f"BackCoverNote_{spec.book_id}",
        fontName=FONT_BODY,
        fontSize=10.0,
        leading=14.8,
        textColor=to_color(ink_obsidian),
    )
    p_note = Paragraph(spec.inside_note_html, note_style)
    _, hn = p_note.wrap(safe_w, 100.0)
    note_y = rule_y1 - 14.0 - hn
    p_note.drawOn(c, safe_x, note_y)

    rule_y2 = note_y - 14.0
    c.line(safe_x, rule_y2, safe_x + safe_w, rule_y2)

    # 5. Bottom Left Imprint & Bottom Right Official 2.00 x 1.20 in White ISBN Barcode Box
    c.setFillColor(to_color(ink_obsidian))
    c.setFont(FONT_BODY_BOLD, 16.0)
    c.drawString(safe_x, oy + 104.0, "StackCalc")

    c.setFillColor(to_color(ink_muted))
    c.setFont(FONT_BODY, 9.5)
    c.drawString(safe_x, oy + 86.0, "Instruments, Books & Classroom Manipulatives")
    c.setFont(FONT_MONO_BOLD, 9.0)
    c.setFillColor(to_color(spec.accent_hex))
    c.drawString(safe_x, oy + 68.0, "stackcalc.io")

    bc_w = 144.0
    bc_h = 86.4
    bc_x = safe_x + safe_w - bc_w
    bc_y = oy + 56.0
    draw_vector_isbn_barcode(
        c,
        bc_x,
        bc_y,
        bc_w,
        bc_h,
        spec.isbn_hyphenated,
        spec.isbn_digits,
        spec.price_label,
    )

    c.restoreState()


def generate_lulu_coil_cover_pdf(out_path: Path, book_key: str) -> None:
    """
    Generates a standalone 2-page Lulu Coil-Bound Cover PDF (8.75" x 11.25" with 0.125" full bleed
    around 8.5" x 11.0" US Letter trim) using the Bestseller Warm Archival Paper (#F7F4EB) cover design.
    Page 1 = Front Cover, Page 2 = Back Cover.
    """
    spec = BOOK_COVER_SPECS[book_key]
    bleed = 9.0  # 0.125 in = 9 pt
    trim_w, trim_h = letter  # 612 x 792 pt
    page_w = trim_w + 2 * bleed
    page_h = trim_h + 2 * bleed

    out_path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(out_path), pagesize=(page_w, page_h))
    c.setTitle(f"{spec.title_line_1} {spec.title_line_2} — Lulu Coil-Bound Cover")
    c.setAuthor("StackCalc Learning Lab")

    # Page 1: Front Cover
    draw_curriculum_bestseller_front_cover(
        c,
        ox=bleed,
        oy=bleed,
        w=trim_w,
        h=trim_h,
        spec=spec,
        bleed_l=bleed,
        bleed_r=bleed,
        bleed_t=bleed,
        bleed_b=bleed,
    )
    c.showPage()

    # Page 2: Back Cover
    draw_curriculum_bestseller_back_cover(
        c,
        ox=bleed,
        oy=bleed,
        w=trim_w,
        h=trim_h,
        spec=spec,
        bleed_l=bleed,
        bleed_r=bleed,
        bleed_t=bleed,
        bleed_b=bleed,
    )
    c.showPage()
    c.save()
