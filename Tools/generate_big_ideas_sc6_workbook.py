#!/usr/bin/env python3
"""
Generate Printable PDF Workbooks for the Big Ideas Math Middle School SC-6 Catch-Up Program.

Reads the single-source-of-truth curriculum markdown:
  - docs/curriculum/big-ideas-middle-school-sc6-workbook.md

Produces two publication-grade ReportLab PDFs:
  1. docs/downloads/worksheets/bigideas_middle_school_sc6_daily_student_workbook.pdf
     (45 Daily 15-Minute Student Missions with fillable 3-Box "Touch • Stack • Prove"
      Work Tickets, "One Build, Multiple Ways" Decoders, and 45-Day Streak Tracker)
  2. docs/downloads/worksheets/bigideas_middle_school_sc6_teacher_coach_guide.pdf
     (Parent & Teacher "No-Battle" Coaching Guide + Complete 45-Day Stack Trace & Solutions Key)
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT / "Tools") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "Tools"))

from book_engine import expand_key_macros

DOCS_DIR = REPO_ROOT / "docs"
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

# Register TrueType Fonts with full Unicode math coverage
FONT_BODY = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_ITALIC = "Helvetica-Oblique"
FONT_MONO = "Courier"
FONT_MONO_BOLD = "Courier-Bold"

try:
    if (FONT_DIR / "SpaceMono-Regular.ttf").exists():
        pdfmetrics.registerFont(TTFont("SpaceMono", str(FONT_DIR / "SpaceMono-Regular.ttf")))
        pdfmetrics.registerFont(TTFont("SpaceMono-Bold", str(FONT_DIR / "SpaceMono-Bold.ttf")))
        FONT_MONO = "SpaceMono"
        FONT_MONO_BOLD = "SpaceMono-Bold"
    arial_dir = Path("/System/Library/Fonts/Supplemental")
    if (arial_dir / "Arial.ttf").exists() and (arial_dir / "Arial Bold.ttf").exists():
        pdfmetrics.registerFont(TTFont("BookSans", str(arial_dir / "Arial.ttf")))
        pdfmetrics.registerFont(TTFont("BookSans-Bold", str(arial_dir / "Arial Bold.ttf")))
        italic_ttf = arial_dir / ("Arial Italic.ttf" if (arial_dir / "Arial Italic.ttf").exists() else "Arial.ttf")
        pdfmetrics.registerFont(TTFont("BookSans-Italic", str(italic_ttf)))
        FONT_BODY = "BookSans"
        FONT_BOLD = "BookSans-Bold"
        FONT_ITALIC = "BookSans-Italic"
except Exception as exc:
    print(f"[WARN] Font registration fallback: {exc}")


def clean_inline_md(text: str) -> str:
    """Convert inline markdown/LaTeX into clean ReportLab XML markup."""
    s = text.strip()
    # Replace emojis with clean ASCII badges so TTF fonts never render tofu boxes
    emoji_map = {
        "🧱": "[BLOCKS]",
        "📟": "[STACK]",
        "✅": "[PROVE]",
        "🏆": "[BADGE]",
        "🚀": "",
        "📖": "",
        "⚡": "",
        "📝": "",
        "🎯": "",
        "🧑‍🏫": "",
        "🕒": "CLK",
        "▦": "10F",
        "🎲": "DICE",
        "●": "*",
        "○": "o",
        "&bull;": "•",
        "&amp;": "&",
        "&rarr;": "->",
        "&darr;": "v",
        "&le;": "<=",
        "&ge;": ">=",
        "&#124;": "|",
    }
    for k, v in emoji_map.items():
        s = s.replace(k, v)

    # Convert common LaTeX commands to clean Unicode
    s = re.sub(r"\\frac\{([^{}]+)\}\{([^{}]+)\}", r"\1/\2", s)
    s = re.sub(r"\\text\{([^{}]+)\}", r"\1", s)
    s = re.sub(r"\\sqrt\{([^{}]+)\}", r"√(\1)", s)
    latex_repls = {
        r"\times": "×",
        r"\div": "÷",
        r"\cdot": "·",
        r"\to": "->",
        r"\leftrightarrow": "<->",
        r"\ge": ">=",
        r"\le": "<=",
        r"\pi": "π",
        r"\bar{x}": "x̄",
        r"\sum": "Σ",
        r"\approx": "≈",
        r"^\circ": "°",
        r"\_": "_",
        r"\{": "{",
        r"\}": "}",
        r"\$": "$",
    }
    for k, v in latex_repls.items():
        s = s.replace(k, v)
    # Strip inline $...$ math delimiters
    s = re.sub(r"\$([^$]+)\$", r"\1", s)
    # Extract inline code spans `...` first so inner * or | are never mangled
    code_tokens: List[str] = []

    def _stash_code(m: re.Match) -> str:
        idx = len(code_tokens)
        escaped_code = html.escape(m.group(1))
        code_tokens.append(f'<font name="{FONT_MONO_BOLD}" color="#0F172A">{escaped_code}</font>')
        return f"@@CODE{idx}@@"

    s = re.sub(r"`([^`]+)`", _stash_code, s)
    s = s.replace("<br>", "@@BR@@").replace("<br/>", "@@BR@@")
    s = html.escape(s)
    s = s.replace("@@BR@@", "<br/>")

    # Restore bold **...** and italic *...*
    s = re.sub(r"\*\*([^*]+)\*\*", lambda m: f"<b>{m.group(1)}</b>", s)
    s = re.sub(r"\*([^*]+)\*", lambda m: f"<i>{m.group(1)}</i>", s)

    for idx, tok in enumerate(code_tokens):
        s = s.replace(f"@@CODE{idx}@@", tok)
    return s


def split_md_row(line: str) -> List[str]:
    """Split a markdown table row on | outside backticks."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    cells: List[str] = []
    cur: List[str] = []
    in_code = False
    for ch in s:
        if ch == "`":
            in_code = not in_code
            cur.append(ch)
        elif ch == "|" and not in_code:
            cells.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    cells.append("".join(cur).strip())
    return cells


def parse_workbook_markdown(md_path: Path) -> List[Dict]:
    """Parse chapters and daily lessons from the markdown source."""
    raw = md_path.read_text(encoding="utf-8")
    expanded = expand_key_macros(raw, is_sc32=False, file_path=md_path, target_format="pdf")

    chapters: List[Dict] = []
    current_chapter: Optional[Dict] = None
    current_day: Optional[Dict] = None
    mode: Optional[str] = None

    for line in expanded.splitlines():
        ch_match = re.match(r"^#\s+CHAPTER\s+(\d+):\s+(.+)$", line)
        if ch_match:
            current_chapter = {
                "num": int(ch_match.group(1)),
                "title": ch_match.group(2).strip(),
                "subtitle": "",
                "days": [],
            }
            chapters.append(current_chapter)
            current_day = None
            mode = "chapter_intro"
            continue

        day_match = re.match(r"^###\s+Day\s+(\d+)\s+\(Lesson\s+([\d.]+)\):\s+(.+)$", line)
        if day_match and current_chapter is not None:
            current_day = {
                "day_num": int(day_match.group(1)),
                "lesson_num": day_match.group(2).strip(),
                "title": day_match.group(3).strip(),
                "alignment": "",
                "question": "",
                "hook": "",
                "decoder_lines": [],
                "problems": [],
            }
            current_chapter["days"].append(current_day)
            mode = "day_meta"
            continue

        if re.match(r"^##\s+4\.\s+The 45-Day Student Streak", line):
            current_day = None
            mode = "end"
            break

        if current_day is None:
            if mode == "chapter_intro" and current_chapter and line.startswith("*") and line.endswith("*"):
                current_chapter["subtitle"] = line.strip("*")
            continue

        if line.startswith("#### ") and ("Decoder" in line or "Elevator Trace" in line):
            mode = "decoder"
            continue
        if line.startswith("#### Daily 3-Problem Workout"):
            mode = "problems"
            continue

        if mode == "day_meta":
            if line.startswith("- **Big Ideas"):
                current_day["alignment"] = re.sub(r"^-\s*\*\*[^*]+\*\*\s*", "", line).strip()
            elif line.startswith("- **The Real Question:**"):
                current_day["question"] = line.replace("- **The Real Question:**", "").strip()
            elif line.startswith("- **Why Should I Care? (2-Min Hook):**"):
                current_day["hook"] = line.replace("- **Why Should I Care? (2-Min Hook):**", "").strip()
        elif mode == "decoder":
            if line.strip() and not line.strip().startswith("{{blocks:") and not line.strip().startswith("```"):
                current_day["decoder_lines"].append(line)
        elif mode == "problems":
            prob_match = re.match(r"^(\d+)\.\s+\*\*Problem\s+\d+\s*\(([^)]+)\):\*\*\s*(.+)$", line)
            if prob_match:
                current_day["problems"].append({
                    "num": int(prob_match.group(1)),
                    "tag": prob_match.group(2).strip(),
                    "prompt": prob_match.group(3).strip(),
                    "touch": "",
                    "stack": "",
                    "prove": "",
                })
            elif current_day["problems"]:
                last_p = current_day["problems"][-1]
                stripped = line.strip()
                if stripped.startswith("- **") and "Touch It" in stripped:
                    last_p["touch"] = re.sub(r"^-\s*\*\*[^*]+\*\*\s*", "", stripped)
                elif stripped.startswith("- **") and ("Stack It" in stripped or "Way A" in stripped or "Way B" in stripped):
                    val = re.sub(r"^-\s*\*\*([^*]+)\*\*\s*", r"**\1** ", stripped)
                    last_p["stack"] = (last_p["stack"] + " • " + val) if last_p["stack"] else val
                elif stripped.startswith("- **") and ("Prove It" in stripped or "Answer" in stripped):
                    last_p["prove"] = re.sub(r"^-\s*\*\*[^*]+\*\*\s*", "", stripped)

    return chapters


def build_styles() -> Dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "CoverKicker": ParagraphStyle(
            "CoverKicker",
            parent=base["Normal"],
            fontName=FONT_MONO_BOLD,
            fontSize=9,
            leading=12,
            textColor=HexColor("#059669"),
            spaceAfter=4,
        ),
        "CoverTitle": ParagraphStyle(
            "CoverTitle",
            parent=base["Title"],
            fontName=FONT_BOLD,
            fontSize=22,
            leading=26,
            textColor=HexColor("#0F172A"),
            alignment=0,
            spaceAfter=6,
        ),
        "CoverSub": ParagraphStyle(
            "CoverSub",
            parent=base["Normal"],
            fontName=FONT_BODY,
            fontSize=10.5,
            leading=14.5,
            textColor=HexColor("#334155"),
            spaceAfter=10,
        ),
        "ChapterHeader": ParagraphStyle(
            "ChapterHeader",
            parent=base["Heading1"],
            fontName=FONT_BOLD,
            fontSize=15,
            leading=19,
            textColor=HexColor("#FFFFFF"),
            spaceBefore=0,
            spaceAfter=2,
        ),
        "ChapterSub": ParagraphStyle(
            "ChapterSub",
            parent=base["Normal"],
            fontName=FONT_ITALIC,
            fontSize=8.5,
            leading=11.5,
            textColor=HexColor("#E2E8F0"),
        ),
        "DayHeader": ParagraphStyle(
            "DayHeader",
            parent=base["Heading2"],
            fontName=FONT_BOLD,
            fontSize=11.5,
            leading=14.5,
            textColor=HexColor("#064E3B"),
            spaceBefore=6,
            spaceAfter=2,
        ),
        "BodySmall": ParagraphStyle(
            "BodySmall",
            parent=base["Normal"],
            fontName=FONT_BODY,
            fontSize=8.5,
            leading=11.5,
            textColor=HexColor("#1E293B"),
            spaceAfter=3,
        ),
        "HookBox": ParagraphStyle(
            "HookBox",
            parent=base["Normal"],
            fontName=FONT_BODY,
            fontSize=8.2,
            leading=11.0,
            textColor=HexColor("#0F172A"),
        ),
        "TableCell": ParagraphStyle(
            "TableCell",
            parent=base["Normal"],
            fontName=FONT_BODY,
            fontSize=7.8,
            leading=10.2,
            textColor=HexColor("#0F172A"),
        ),
        "TableHeader": ParagraphStyle(
            "TableHeader",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=7.8,
            leading=10.2,
            textColor=HexColor("#FFFFFF"),
        ),
        "TicketTitle": ParagraphStyle(
            "TicketTitle",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=8.6,
            leading=11.2,
            textColor=HexColor("#0F172A"),
        ),
        "TicketMono": ParagraphStyle(
            "TicketMono",
            parent=base["Normal"],
            fontName=FONT_MONO,
            fontSize=7.8,
            leading=10.2,
            textColor=HexColor("#0F172A"),
        ),
    }


def render_markdown_table(lines: List[str], styles: Dict[str, ParagraphStyle], usable_w: float) -> Optional[Table]:
    """Extract and render the first markdown table in decoder_lines."""
    table_lines = [ln.strip() for ln in lines if ln.strip().startswith("|") and ln.strip().endswith("|")]
    if len(table_lines) < 3:
        return None
    rows_raw = []
    for idx, ln in enumerate(table_lines):
        cells = split_md_row(ln)
        if idx == 1 and all(re.match(r"^[:\-]+$", c.replace(" ", "")) for c in cells if c):
            continue
        rows_raw.append(cells)
    if len(rows_raw) < 2:
        return None
    ncols = max(len(r) for r in rows_raw)
    data = []
    for r_idx, r in enumerate(rows_raw):
        padded = (r + [""] * ncols)[:ncols]
        st = styles["TableHeader"] if r_idx == 0 else styles["TableCell"]
        data.append([Paragraph(clean_inline_md(c), st) for c in padded])

    col_w = usable_w / ncols
    t = Table(data, colWidths=[col_w] * ncols, repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), HexColor("#1E293B")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#F8FAFC"), HexColor("#FFFFFF")]),
                ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#CBD5E1")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 3.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return t


def build_student_ticket(prob: Dict, styles: Dict[str, ParagraphStyle], usable_w: float) -> Table:
    """Create the fillable 3-Box 'Touch • Stack • Prove' student work ticket."""
    header_p = Paragraph(
        clean_inline_md(f"**Problem {prob['num']} ({prob['tag']}):** {prob['prompt']}"),
        styles["TicketTitle"],
    )
    touch_hint = prob["touch"].replace("[ ]", "").strip() if prob["touch"] else "Build with blocks on your desk first!"
    col1 = Paragraph(
        clean_inline_md(f"<b>1. [BLOCKS] TOUCH IT</b><br/>[  ] {touch_hint}<br/><i>(1 Build = All Book Ways!)</i>"),
        styles["TableCell"],
    )
    col2 = Paragraph(
        f'<b>2. [STACK] ELEVATOR SNAPSHOT</b><br/>'
        f'<font name="{FONT_MONO}" size="7.5">Floor 2 (Y): ___________<br/>Floor 1 (X): ___________</font>',
        styles["TableCell"],
    )
    col3 = Paragraph(
        f'<b>3. [PROVE] GREEN-LIGHT CHECK</b><br/>'
        f'<font name="{FONT_MONO}" size="7.5">FINAL ANSWER: __________</font><br/>'
        f'[  ] Proven with [f][LASTX]!',
        styles["TableCell"],
    )

    data = [
        [header_p, "", ""],
        [col1, col2, col3],
    ]
    w1 = usable_w * 0.36
    w2 = usable_w * 0.32
    w3 = usable_w * 0.32
    t = Table(data, colWidths=[w1, w2, w3])
    t.setStyle(
        TableStyle(
            [
                ("SPAN", (0, 0), (2, 0)),
                ("BACKGROUND", (0, 0), (2, 0), HexColor("#ECFDF5")),
                ("BACKGROUND", (0, 1), (0, 1), HexColor("#FFFFFF")),
                ("BACKGROUND", (1, 1), (1, 1), HexColor("#F8FAFC")),
                ("BACKGROUND", (2, 1), (2, 1), HexColor("#FFFFFF")),
                ("BOX", (0, 0), (-1, -1), 0.8, HexColor("#10B981")),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, HexColor("#CBD5E1")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return t


def build_teacher_ticket(prob: Dict, styles: Dict[str, ParagraphStyle], usable_w: float) -> Table:
    """Create the filled Teacher/Coach Solution & Stack Trace ticket."""
    header_p = Paragraph(
        clean_inline_md(f"**Problem {prob['num']} ({prob['tag']}):** {prob['prompt']}"),
        styles["TicketTitle"],
    )
    touch_txt = prob["touch"] or "Hands-on manipulative build verified."
    stack_txt = prob["stack"] or "Verified on 4-line XYZT stack."
    prove_txt = prob["prove"] or "Verified via [f][LASTX] inverse operation."

    col1 = Paragraph(clean_inline_md(f"<b>1. [BLOCKS] TOUCH IT:</b><br/>{touch_txt}"), styles["TableCell"])
    col2 = Paragraph(clean_inline_md(f"<b>2. [STACK] KEYSTROKES &amp; Y|X:</b><br/>{stack_txt}"), styles["TableCell"])
    col3 = Paragraph(clean_inline_md(f"<b>3. [PROVE] VERIFIED SOLUTION:</b><br/>{prove_txt}"), styles["TableCell"])

    data = [
        [header_p, "", ""],
        [col1, col2, col3],
    ]
    w1 = usable_w * 0.28
    w2 = usable_w * 0.42
    w3 = usable_w * 0.30
    t = Table(data, colWidths=[w1, w2, w3])
    t.setStyle(
        TableStyle(
            [
                ("SPAN", (0, 0), (2, 0)),
                ("BACKGROUND", (0, 0), (2, 0), HexColor("#EFF6FF")),
                ("BACKGROUND", (0, 1), (2, 1), HexColor("#FFFFFF")),
                ("BOX", (0, 0), (-1, -1), 0.8, HexColor("#3B82F6")),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, HexColor("#CBD5E1")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return t


def add_footer(canvas_obj, doc, title_str: str):
    canvas_obj.saveState()
    canvas_obj.setFont(FONT_MONO, 7.5)
    canvas_obj.setFillColor(HexColor("#64748B"))
    canvas_obj.drawString(36, 22, title_str)
    canvas_obj.drawRightString(letter[0] - 36, 22, f"Page {doc.page}")
    canvas_obj.restoreState()


def generate_pdf(chapters: List[Dict], output_path: Path, is_teacher: bool) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    styles = build_styles()
    usable_w = letter[0] - 72.0

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=38,
        title=(
            "StackCalc SC-6 Big Ideas Middle School Coach & Answer Key"
            if is_teacher
            else "StackCalc SC-6 Big Ideas Middle School Daily Catch-Up Student Workbook"
        ),
        author="StackCalc Learning Lab",
    )

    story = []

    # Cover / Intro Banner
    kicker = (
        "STACKCALC LEARNING LAB // OFFICIAL TEACHER & PARENT COACHING KEY"
        if is_teacher
        else "STACKCALC LEARNING LAB // 45-DAY MIDDLE SCHOOL CATCH-UP WORKBOOK"
    )
    main_title = (
        "Big Ideas Math Middle School: Coach Guide & Stack Trace Solutions"
        if is_teacher
        else "Big Ideas Math Middle School: Daily 'Touch • Stack • Prove' Workbook"
    )
    subtitle = (
        "Complete 10-Chapter, 45-Day Facilitation Playbook, 'Multiple-Ways' Manipulative Translators, and Verified SC-6 RPN Stack Snapshots (Grades 6–7 Bridge)."
        if is_teacher
        else "45 Daily 15-Minute Hands-On Missions for Kids Who Hate Showing Busywork or Repeating Operations 4 Ways. Powered by StackCalc Blocks & the SC-6 Calculator."
    )

    story.append(Paragraph(kicker, styles["CoverKicker"]))
    story.append(Paragraph(main_title, styles["CoverTitle"]))
    story.append(Paragraph(subtitle, styles["CoverSub"]))
    story.append(HRFlowable(width="100%", thickness=1.5, color=HexColor("#0F172A"), spaceAfter=8))

    # Explain the 3-Box Ticket & Streak Map on Page 1
    rules_data = [
        [
            Paragraph("<b>RULE 1: ZERO BUSYWORK REWRITES</b>", styles["TableHeader"]),
            Paragraph("<b>RULE 2: ONE BUILD = ALL BOOK WAYS</b>", styles["TableHeader"]),
            Paragraph("<b>RULE 3: INSTANT GREEN-LIGHT PROOF</b>", styles["TableHeader"]),
        ],
        [
            Paragraph(
                "Never copy 6 lines of algebra steps! Your SC-6 4-line elevator holds intermediate numbers on <b>Floor 2 (Y)</b> and <b>Floor 1 (X)</b>. Writing down the 2 numbers on <b>Y</b> and <b>X</b> before your final keypress IS your work!",
                styles["TableCell"],
            ),
            Paragraph(
                "When the textbook asks for a Factor Tree, a List, AND a Venn Diagram (or a Tape Diagram, Ratio Table, AND Equation), build it <b>ONCE</b> with physical blocks. They are just 3 camera angles of the same blocks!",
                styles["TableCell"],
            ),
            Paragraph(
                "Don't wait until tomorrow for red ink! Press <b>[f] [LASTX]</b> (or <b>[g] [SIMP]</b> / <b>[g] [FACT]</b>) right after solving. When your starting number bounces back on screen, you know you're 100% right!",
                styles["TableCell"],
            ),
        ],
    ]
    rules_tbl = Table(rules_data, colWidths=[usable_w / 3.0] * 3)
    rules_tbl.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), HexColor("#064E3B") if not is_teacher else HexColor("#1E3A8A")),
                ("BACKGROUND", (0, 1), (-1, 1), HexColor("#F0FDF4") if not is_teacher else HexColor("#EFF6FF")),
                ("GRID", (0, 0), (-1, -1), 0.6, HexColor("#94A3B8")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(rules_tbl)
    story.append(Spacer(1, 10))

    # 45-Day Pacing & Streak Checklist Table on Page 1
    streak_rows = [
        [
            Paragraph("<b>Chapter &amp; Big Ideas Topic</b>", styles["TableHeader"]),
            Paragraph("<b>Daily 15-Minute Missions (Check Off Each Win!)</b>", styles["TableHeader"]),
            Paragraph("<b>Boss Badge</b>", styles["TableHeader"]),
        ]
    ]
    badge_names = [
        "1. Prime Architect",
        "2. Tower Master",
        "3. Ratio Navigator",
        "4. Tile Alchemist",
        "5. Polygon Engineer",
        "6. Zero-Pair Commander",
        "7. Balance Breaker",
        "8. 3D Solid Builder",
        "9. Data Scientist",
        "10. Stack Champion",
    ]
    for idx, ch in enumerate(chapters):
        day_checks = "  ".join(f"[  ] Day {d['day_num']} ({d['lesson_num']})" for d in ch["days"])
        b_name = badge_names[idx] if idx < len(badge_names) else f"Badge {idx+1}"
        streak_rows.append(
            [
                Paragraph(clean_inline_md(f"<b>Ch. {ch['num']}:</b> {ch['title'].split('(')[0].strip()}"), styles["TableCell"]),
                Paragraph(clean_inline_md(day_checks), styles["TableCell"]),
                Paragraph(clean_inline_md(f"[  ] <b>{b_name}</b>"), styles["TableCell"]),
            ]
        )
    streak_tbl = Table(streak_rows, colWidths=[usable_w * 0.30, usable_w * 0.48, usable_w * 0.22])
    streak_tbl.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), HexColor("#0F172A")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#FFFFFF"), HexColor("#F8FAFC")]),
                ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#CBD5E1")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 3.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(streak_tbl)
    story.append(PageBreak())

    # Render each Chapter & its Daily Missions
    for ch in chapters:
        ch_banner = Table(
            [
                [
                    Paragraph(clean_inline_md(f"CHAPTER {ch['num']}: {ch['title']}"), styles["ChapterHeader"]),
                ],
                [
                    Paragraph(clean_inline_md(ch["subtitle"]), styles["ChapterSub"]),
                ],
            ],
            colWidths=[usable_w],
        )
        ch_banner.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), HexColor("#0F172A")),
                    ("TOPPADDING", (0, 0), (-1, 0), 7),
                    ("BOTTOMPADDING", (0, -1), (-1, -1), 7),
                    ("LEFTPADDING", (0, 0), (-1, -1), 10),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ]
            )
        )
        story.append(ch_banner)
        story.append(Spacer(1, 6))

        for d_idx, day in enumerate(ch["days"]):
            day_flow = []
            day_flow.append(
                Paragraph(
                    clean_inline_md(f"Day {day['day_num']} (Lesson {day['lesson_num']}): {day['title']}"),
                    styles["DayHeader"],
                )
            )
            if day["question"]:
                day_flow.append(
                    Paragraph(clean_inline_md(f"<b>The Real Question:</b> {day['question']}"), styles["BodySmall"])
                )
            if day["hook"]:
                hook_box = Table(
                    [[Paragraph(clean_inline_md(f"<b>Why Should I Care? (2-Min Hook):</b> {day['hook']}"), styles["HookBox"])]],
                    colWidths=[usable_w],
                )
                hook_box.setStyle(
                    TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, -1), HexColor("#FEF3C7")),
                            ("BOX", (0, 0), (-1, -1), 0.6, HexColor("#F59E0B")),
                            ("TOPPADDING", (0, 0), (-1, -1), 4),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                        ]
                    )
                )
                day_flow.append(hook_box)
                day_flow.append(Spacer(1, 4))

            # Render Decoder Table if present
            dec_tbl = render_markdown_table(day["decoder_lines"], styles, usable_w)
            if dec_tbl is not None:
                day_flow.append(dec_tbl)
                day_flow.append(Spacer(1, 4))

            story.append(KeepTogether(day_flow))

            # Render the 3 Daily Workout Problems
            for prob in day["problems"]:
                if is_teacher:
                    t_box = build_teacher_ticket(prob, styles, usable_w)
                else:
                    t_box = build_student_ticket(prob, styles, usable_w)
                story.append(KeepTogether([t_box, Spacer(1, 4)]))

            story.append(HRFlowable(width="100%", thickness=0.6, color=HexColor("#CBD5E1"), spaceBefore=4, spaceAfter=6))

        story.append(PageBreak())

    footer_label = (
        "StackCalc SC-6 // Big Ideas Middle School Coach Guide & Answer Key"
        if is_teacher
        else "StackCalc SC-6 // Big Ideas Middle School Daily Student Workbook (Touch • Stack • Prove)"
    )
    doc.build(
        story,
        onFirstPage=lambda c, d: add_footer(c, d, footer_label),
        onLaterPages=lambda c, d: add_footer(c, d, footer_label),
    )
    print(f"[OK] Built {output_path} ({output_path.stat().st_size / 1024:.1f} KB)")


def main() -> None:
    chapters = parse_workbook_markdown(SOURCE_MD)
    total_days = sum(len(c["days"]) for c in chapters)
    total_probs = sum(len(d["problems"]) for c in chapters for d in c["days"])
    print(f"Parsed {len(chapters)} chapters, {total_days} daily lessons, {total_probs} workout problems.")
    generate_pdf(chapters, STUDENT_PDF, is_teacher=False)
    generate_pdf(chapters, TEACHER_PDF, is_teacher=True)


if __name__ == "__main__":
    main()
