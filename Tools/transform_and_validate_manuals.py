#!/usr/bin/env python3
"""
Transforms and validates the StackCalc SC-32 and SC-6 manual manuscripts:
  1. Removes key/shift color references (since faceplate themes vary); uses Left Shift
     `{{key:↰}}` and Right Shift `{{key:↱}}` on SC-32, and `{{key:f}}` and `{{key:g}}`
     shifts on SC-6.
  2. Converts keystroke sequences into `{{key:...}}` / `{{keycap:...}}` macros grounded
     in `docs/assets/manuals/layout_data.json` and `layout_data_sc6.json`.
  3. Strips hardcoded section numbers from `## ` and `### ` headings so
     `book_engine.auto_number_headings` numbers them deterministically without duplicates.
  4. Fixes all inverted ` ```text\\n``` ` markdown code fences and repairs any
     unbalanced inline backticks.
  5. Replaces all `"The ... Persona"` headings with authentic editorial headings.
  6. Moves `CHAPTER BASELINE MODE` / `Unlocked Keycaps` banners after the opening
     narrative story in every chapter.
  7. Programmatically validates every `{{key:...}}` and `{{keycap:...}}` macro,
     code fence parity, inline backtick parity, and section numbering uniqueness.
"""

from __future__ import annotations

import os
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

TOOLS_DIR = Path(__file__).resolve().parent
REPO_ROOT = TOOLS_DIR.parent
MANUALS_DIR = (
    REPO_ROOT / "documentation" / "manuals"
    if (REPO_ROOT / "documentation" / "manuals").exists()
    else REPO_ROOT / "docs" / "manuals"
)
ASSETS_MANUALS_DIR = (
    MANUALS_DIR / "assets"
    if (MANUALS_DIR / "assets").exists()
    else REPO_ROOT / "docs" / "assets" / "manuals"
)
STACKCALC_DOCS_DIR = (
    REPO_ROOT / "docs"
    if (REPO_ROOT / "docs").exists()
    else REPO_ROOT.parent / "stackcalc" / "docs"
)
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from book_engine import (
    expand_key_macros,
    get_chapter_prefix,
    get_registry,
    process_manual_markdown,
    strip_manual_section_number,
)


def fix_inverted_code_fences(text: str) -> Tuple[str, int]:
    """
    Fixes blocks where ` ```text\\n```\\n...content...\\n```\\n``` ` was inverted.
    """
    pattern = re.compile(
        r"```text\s*\n```\s*\n(.*?)\n```\s*\n```",
        flags=re.DOTALL,
    )
    count = len(pattern.findall(text))
    fixed = pattern.sub(r"\n```text\n\1\n```", text)
    fixed = re.sub(
        r'(<p class="admonition-title">[^<]*</p>)\n(```)',
        r"\1\n\n\2",
        fixed,
    )
    return fixed, count


def replace_persona_headings(text: str) -> str:
    """Replaces internal rubric 'Persona' headings with natural editorial notes."""
    replacements = [
        (r"^(#{2,3})\s+(?:[0-9A-E.]+\s+)?(?:The )?Three Personas(?:\s+Master Perspectives|:\s*.*)?$", r"\1 Teaching & Misconception Notes"),
        (r"^(#{2,3})\s+(?:[0-9A-E.]+\s+)?(?:The )?Three Personas of the SC-(?:6|32).*$", r"\1 Instrument Architecture & Educational Foundations"),
        (r"^(#{2,3})\s+(?:[0-9A-E.]+\s+)?Pedagogical Review & Persona (?:Commentary|Reflections).*$", r"\1 Teaching & Misconception Notes"),
        (r"^(#{2,3})\s+(?:[0-9A-E.]+\s+)?(?:Persona 1:\s*)?The (?:Elementary )?Math Teacher Persona.*$", r"\1 Teaching & Misconception Notes"),
        (r"^(#{2,3})\s+(?:[0-9A-E.]+\s+)?Persona 1:\s*The Elementary Math Teacher.*$", r"\1 Teaching & Misconception Notes"),
        (r"^(#{2,3})\s+(?:[0-9A-E.]+\s+)?(?:Persona 2:\s*)?The Homeschool(?:er Advocate|ing Parent-Educator)(?: Persona)?.*$", r"\1 Guided Discovery & Problem Solving"),
        (r"^(#{2,3})\s+(?:[0-9A-E.]+\s+)?(?:Persona 3:\s*)?The Calculator (?:Enthusiast|Connoisseur).*$", r"\1 Instrument Architecture Notes"),
        (r"^(#{2,3})\s+(?:[0-9A-E.]+\s+)?The (?:UIL Contest & Competitive Math|Maker Space) Coach Persona.*$", r"\1 Applied Verification & Practical Notes"),
    ]
    lines = text.split("\n")
    out = []
    for line in lines:
        for pat, rep in replacements:
            if re.match(pat, line, flags=re.IGNORECASE):
                line = re.sub(pat, rep, line, flags=re.IGNORECASE)
                break
        line = line.replace("**Teacher Persona Note:**", "**Teaching Note:**")
        out.append(line)
    return "\n".join(out)


def remove_shift_color_terminology(text: str, is_sc32: bool) -> str:
    """
    Removes color-specific shift names ('Yellow Shift', 'Gold Shift', 'Blue Shift', etc.)
    because faceplate colors change by theme.
    On SC-32: Left Shift `{{key:↰}}` and Right Shift `{{key:↱}}`
    On SC-6: `{{key:f}}` Shift and `{{key:g}}` Shift
    """
    if is_sc32:
        rules = [
            (r"Gold Shift\s*`?\[f\]`?", "Left Shift `{{key:↰}}`"),
            (r"Yellow Shift\s*`?\[f\]`?", "Left Shift `{{key:↰}}`"),
            (r"Blue Shift\s*`?\[g\]`?", "Right Shift `{{key:↱}}`"),
            (r"`?\[↰\]`?\s*\((?:Gold|Yel|Yellow)\)", "`{{key:↰}}` (Left Shift)"),
            (r"`?\[↱\]`?\s*\((?:Blue|Blu)\)", "`{{key:↱}}` (Right Shift)"),
            (r"\*\((?:Gold|Yellow) Latch\)\*", "*(Left Shift Latch)*"),
            (r"\*\(Blue Latch\)\*", "*(Right Shift Latch)*"),
            (r"Primary (?:Gold|Yellow) Shift prefix", "Primary Left Shift prefix"),
            (r"Secondary Blue Shift prefix", "Secondary Right Shift prefix"),
            (r"(?:Gold|Yellow) Left Shift\s*(?:`?\[(?:f|↰)\]`?)?", "Left Shift `{{key:↰}}`"),
            (r"Blue Right Shift\s*(?:`?\[(?:g|↱)\]`?)?", "Right Shift `{{key:↱}}`"),
            (r"(?:Gold|Yellow) Shift\s*(?:`?\[(?:f|↰)\]`?)?", "Left Shift `{{key:↰}}`"),
            (r"Blue Shift\s*(?:`?\[(?:g|↱)\]`?)?", "Right Shift `{{key:↱}}`"),
            (r"(?:gold|yellow)-shifted", "left-shifted (`{{key:↰}}`)"),
            (r"blue-shifted", "right-shifted (`{{key:↱}}`)"),
            (r"(?:gold|yellow) and blue shift legends", "left (`{{key:↰}}`) and right (`{{key:↱}}`) shift legends"),
            (r"primary, (?:yellow|gold), and blue shifted", "primary, left-shifted (`{{key:↰}}`), and right-shifted (`{{key:↱}}`)"),
            (r"(?:gold|yellow) `\[f\]` and blue `\[g\]` shift", "left `{{key:↰}}` and right `{{key:↱}}` shift"),
            (r"Arms yellow shifted alternate functions", "Arms left-shifted alternate functions"),
            (r"Arms blue shifted alternate functions", "Arms right-shifted alternate functions"),
            (r"with amber shifted legends", "with high-contrast laser-foamed legends"),
            (r"`YELLOW` \+", "`{{key:↰}}` +"),
            (r"`BLUE` \+", "`{{key:↱}}` +"),
            (r"Yellow:\s*`TVM`,\s*Blue:\s*`PLOT`", "Left Shift `{{key:↰}}`: `TVM`, Right Shift `{{key:↱}}`: `PLOT`"),
        ]
    else:
        rules = [
            (r"(?:Yellow|Gold) Shift\s*`?\[f\]`?", "`{{key:f}}` Shift"),
            (r"Blue Shift\s*`?\[g\]`?", "`{{key:g}}` Shift"),
            (r"`?\[f\]`?\s*\((?:Yellow|Gold|Yel)\)", "`{{key:f}}` (f-Shift)"),
            (r"`?\[g\]`?\s*\((?:Blue|Blu)\)", "`{{key:g}}` (g-Shift)"),
            (r"\*\((?:Yellow|Gold) Latch\)\*", "*(f-Shift Latch)*"),
            (r"\*\(Blue Latch\)\*", "*(g-Shift Latch)*"),
            (r"Primary (?:Yellow|Gold) Shift prefix", "Primary `{{key:f}}` Shift prefix"),
            (r"Secondary Blue Shift prefix", "Secondary `{{key:g}}` Shift prefix"),
            (r"(?:Yellow|Gold) Left Shift\s*(?:`?\[f\]`?)?", "`{{key:f}}` Shift"),
            (r"Blue Right Shift\s*(?:`?\[g\]`?)?", "`{{key:g}}` Shift"),
            (r"(?:Yellow|Gold) Shift\s*(?:`?\[f\]`?)?", "`{{key:f}}` Shift"),
            (r"Blue Shift\s*(?:`?\[g\]`?)?", "`{{key:g}}` Shift"),
            (r"(?:yellow|gold)-shifted", "`{{key:f}}`-shifted"),
            (r"blue-shifted", "`{{key:g}}`-shifted"),
            (r"yellow and blue shift legends", "`{{key:f}}` and `{{key:g}}` shift legends"),
            (r"yellow and blue shifted commands", "`f`-shifted and `g`-shifted commands"),
            (r"primary, yellow, and blue shifted", "primary, `{{key:f}}`-shifted, and `{{key:g}}`-shifted"),
            (r"yellow `(?:\[f\]|\{\{key:f\}\})` shift key and blue `(?:\[g\]|\{\{key:g\}\})` shift key", "`{{key:f}}` shift key and `{{key:g}}` shift key"),
            (r"yellow `\[f\]` and blue `\[g\]` shift", "`{{key:f}}` and `{{key:g}}` shift"),
            (r"the blue shifted key", "the shifted key"),
            (r"the yellow shifted key", "the shifted key"),
            (r"Yellow\s+`?\[f\]`?", "`{{key:f}}`"),
            (r"Blue\s+`?\[g\]`?", "`{{key:g}}`"),
        ]

    for pat, rep in rules:
        text = re.sub(pat, rep, text)
    return text


def move_baseline_banner_after_opening_story(text: str, file_path: Path) -> str:
    """
    If a chapter file (`01-...` through `14-...`) has a `CHAPTER BASELINE MODE`
    div before the first `## ` heading, moves that banner block to the end of the
    first `## ` section (just before the second `## ` section).
    """
    if not re.match(r"^0*[1-9][0-9]*-.*\.md$", file_path.name):
        return text

    m_first_h2 = re.search(r"^##\s+", text, flags=re.MULTILINE)
    if not m_first_h2:
        return text

    pre_h2 = text[: m_first_h2.start()]
    post_h2 = text[m_first_h2.start() :]

    banner_pat = re.compile(
        r'(\n*<div class="p-4 rounded-xl bg-slate-900[^>]*>\s*<strong>CHAPTER BASELINE MODE:.*?</div>\s*(?:---\s*)?)',
        flags=re.DOTALL,
    )
    m_banner = banner_pat.search(pre_h2)
    if not m_banner:
        return text

    banner_block = m_banner.group(1).strip()
    if banner_block.endswith("---"):
        banner_block = banner_block[:-3].strip()

    new_pre_h2 = pre_h2[: m_banner.start()] + "\n\n" + pre_h2[m_banner.end() :].lstrip()

    h2_matches = list(re.finditer(r"^##\s+", post_h2, flags=re.MULTILINE))
    if len(h2_matches) >= 2:
        sec2_pos = h2_matches[1].start()
        before_sec2 = post_h2[:sec2_pos].rstrip()
        if before_sec2.endswith("---"):
            before_sec2 = before_sec2[:-3].rstrip()
        new_post_h2 = f"{before_sec2}\n\n{banner_block}\n\n---\n\n{post_h2[sec2_pos:]}"
        return new_pre_h2 + new_post_h2
    return text


def strip_all_manual_heading_numbers(text: str, file_path: Path) -> str:
    """
    Strips hardcoded section numbers (`## 1.1 `, `### 16.1 `, `## D.1 `) from
    the markdown source file so `book_engine.auto_number_headings` is the single
    deterministic numbering source.
    """
    if get_chapter_prefix(file_path) is None and file_path.name != "index.md":
        return text

    lines = text.split("\n")
    out = []
    in_fence = False
    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if line.startswith("## ") and not line.startswith("### "):
            clean = strip_manual_section_number(line[3:])
            out.append(f"## {clean}")
        elif line.startswith("### ") and not line.startswith("#### "):
            clean = strip_manual_section_number(line[4:])
            out.append(f"### {clean}")
        else:
            out.append(line)
    return "\n".join(out)


def _apply_safe_pair_sub(text: str, inner_pat: str, replacement_macro: str) -> str:
    """
    Replaces both:
      1. Separately backticked pairs: `` `[f]` `[KEY]` `` -> `` `{{key:KEY}}` ``
      2. Unbackticked or inside-code-span pairs: `[f] [KEY]` -> `{{key:KEY}}`
    without ever eating an outer opening or closing backtick.
    """
    # Case 1: each bracketed token has its own backticks
    pat_bt = re.sub(r"\\\[([^\]]+)\\\]", r"`\\[\1\\]`", inner_pat)
    text = re.sub(pat_bt, f"`{replacement_macro}`", text)
    # Case 2: plain brackets (either in prose or inside a multi-key backtick span)
    text = re.sub(inner_pat, replacement_macro, text)
    return text


def convert_keystrokes_to_macros(text: str, file_path: Path, is_sc32: bool) -> str:
    """
    Converts raw keystroke sequences and shifted key pairs in `text` into
    validated `{{key:NAME}}` or `{{keycap:NAME}}` macros grounded in
    `layout_data.json` (SC-32) and `layout_data_sc6.json` (SC-6).
    """
    if file_path.name == "appendix-e-annotated-bibliography.md":
        return text

    registry = get_registry(is_sc32)

    if is_sc32:
        pair_subs = [
            (r"\[(?:f|g|↰|↱)\]\s*\[E\]\s*\[π\]", "{{key:π}}"),
            (r"\[(?:f|g|↰|↱)\]\s*\[XEQ\]\s*\[∫\]", "{{key:∫}}"),
            (r"\[(?:f|g|↰|↱)\]\s*\[π\]", "{{key:π}}"),
            (r"\[(?:f|g|↰|↱)\]\s*\[SOLVE\]", "{{key:SOLVE}}"),
            (r"\[(?:f|g|↰|↱)\]\s*\[∫\]", "{{key:∫}}"),
            (r"\[(?:f|g|↰|↱)\]\s*\[CMPLX\]", "{{key:CMPLX}}"),
            (r"\[(?:f|g|↰|↱)\]\s*\[BASE\]", "{{key:BASE}}"),
            (r"\[(?:f|g|↰|↱)\]\s*\[CLEAR\]", "{{key:CLEAR}}"),
            (r"\[(?:f|g|↰|↱)\]\s*\[LAST[xX𝑥]\]", "{{key:LASTX}}"),
            (r"\[(?:f|g|↰|↱)\]\s*\[SHOW\]", "{{key:SHOW}}"),
        ]
        single_subs = [
            (r"\[->REC\]", "{{key:▸y,x}}"),
            (r"\[→REC\]", "{{key:▸y,x}}"),
            (r"\[->POL\]", "{{key:▸θ,r}}"),
            (r"\[→POL\]", "{{key:▸θ,r}}"),
            (r"\[->θ,r\]", "{{key:▸θ,r}}"),
            (r"\[->y,x\]", "{{key:▸y,x}}"),
            (r"\[\*\]", "{{key:×}}"),
            (r"\[/\]", "{{key:÷}}"),
            (r"\[<--\]", "{{key:<-}}"),
            (r"\[←\]", "{{key:<-}}"),
            (r"\[x<>y\]", "{{key:x⇄y}}"),
            (r"\[x↔y\]", "{{key:x⇄y}}"),
            (r"\{\{key(?:cap)?:√\}\}", "{{key:√x}}"),
            (r"\[√\]", "{{key:√x}}"),
        ]
    else:
        pair_subs = [
            (r"\[(?:f|g)\]\s*\[123\]", "{{key:PV}}"),
            (r"\[(?:f|g)\]\s*\[10F\]", "{{key:▦}}"),
            (r"\[(?:f|g)\]\s*\[RACK\]", "{{key:COUNT}}"),
            (r"\[(?:f|g)\]\s*\[y⟌x\]", "{{key:÷R}}"),
            (r"\[(?:f|g)\]\s*\[PRM\]", "{{key:PRIME}}"),
            (r"\[(?:f|g)\]\s*\[PRIME\]", "{{key:PRIME}}"),
            (r"\[(?:f|g)\]\s*\[GCF\]", "{{key:GCF}}"),
            (r"\[(?:f|g)\]\s*\[GCD\]", "{{key:GCF}}"),
            (r"\[(?:f|g)\]\s*\[LCM\]", "{{key:LCM}}"),
            (r"\[(?:f|g)\]\s*\[FACTORS\]", "{{key:FACT}}"),
            (r"\[(?:f|g)\]\s*\[FACT\]", "{{key:FACT}}"),
            (r"\[(?:f|g)\]\s*\[LAST\s*[xX𝑥]\]", "{{key:LASTX}}"),
            (r"\[(?:f|g)\]\s*\[π\]", "{{key:π}}"),
            (r"\[(?:f|g)\]\s*\[SKP\]", "{{key:REP}}"),
            (r"\[(?:f|g)\]\s*\[REP\]", "{{key:REP}}"),
            (r"\[(?:f|g)\]\s*\[SIMP\]", "{{key:SIMP}}"),
            (r"\[(?:f|g)\]\s*\[÷R\]", "{{key:÷R}}"),
            (r"\[(?:f|g)\]\s*\[R\s*⬇\]", "{{key:R↓}}"),
            (r"\[(?:f|g)\]\s*\[R\s*Up\]", "{{key:R↑}}"),
            (r"\[(?:f|g)\]\s*\[CLEAR\s*Σ\]", "{{key:CLΣ}}"),
            (r"\[(?:f|g)\]\s*\[RN\s*x\]", "{{key:1…x}}"),
            (r"\[(?:f|g)\]\s*\[y\s*RN\s*x\]", "{{key:t…x}}"),
            (r"\[(?:f|g)\]\s*\[MEAN\]", "{{key:x̄}}"),
            (r"\[(?:f|g)\]\s*\[QUIZ\]", "{{key:?}}"),
            (r"\[(?:f|g)\]\s*\[SUM\]", "{{key:Σx}}"),
        ]
        single_subs = [
            (r"\[\\mathtt\{ENTER\}\]", r"\\mathtt{ENTER}"),
            (r"\[\\mathtt\{f\}\]", r"\\mathtt{f}"),
            (r"\[\\mathtt\{g\}\]", r"\\mathtt{g}"),
            (r"\[123\]", "{{key:PV}}"),
            (r"\[🧮\]", "{{key:PV}}"),
            (r"\[10F\]", "{{key:▦}}"),
            (r"\[RACK\]", "{{key:COUNT}}"),
            (r"\[y⟌x\]", "{{key:÷R}}"),
            (r"\[PRM\]", "{{key:PRIME}}"),
            (r"\[GCD\]", "{{key:GCF}}"),
            (r"\[FACTORS\]", "{{key:FACT}}"),
            (r"\[LAST\s*[xX𝑥]\]", "{{key:LASTX}}"),
            (r"\[SKP\]", "{{key:REP}}"),
            (r"\[x<>y\]", "{{key:x⇄y}}"),
            (r"\[x↔y\]", "{{key:x⇄y}}"),
            (r"\[CLOCK\]", "{{key:🕒}}"),
            (r"\[TIME\]", "{{key:🕒}}"),
            (r"\[R\s*⬇\]", "{{key:R↓}}"),
            (r"\[R\s*Up\]", "{{key:R↑}}"),
            (r"\[CLEAR\s*Σ\]", "{{key:CLΣ}}"),
            (r"\[RN\s*x\]", "{{key:1…x}}"),
            (r"\[y\s*RN\s*x\]", "{{key:t…x}}"),
            (r"\[MEAN\]", "{{key:x̄}}"),
            (r"\[QUIZ\]", "{{key:?}}"),
            (r"\[SUM\]", "{{key:Σx}}"),
            (r"\[x\?y\]", "{{key:≠}}"),
            (r"\[x\?0\]", "{{key:≠}}"),
            (r"\[\*\]", "{{key:×}}"),
            (r"\[/\]", "{{key:÷}}"),
            (r"\[<--\]", "{{key:<-}}"),
            (r"\[←\]", "{{key:<-}}"),
            (r"\[MIX\]", "{{key:a ᵇ/c}}"),
            (r"\[IMP\]", "{{key:d/c}}"),
            (r"\[ratio\]", "{{key:a:b}}"),
        ]

    for pat, macro in pair_subs:
        text = _apply_safe_pair_sub(text, pat, macro)
    for pat, macro in single_subs:
        text = re.sub(pat, macro, text)

    # Collapse any remaining shifted pairs:
    # 1) Separately backticked `` `[f]` `[FUNC]` `` or `` `{{key:f}}` `[FUNC]` ``
    def _collapse_bt_pair(match: re.Match) -> str:
        func_tok = match.group(1).strip()
        try:
            entry = registry.resolve(func_tok)
            if entry.layer in ("yellow", "blue", "primary", "menu"):
                return f"`{{{{key:{entry.canonical}}}}}`"
        except ValueError:
            pass
        return match.group(0)

    text = re.sub(
        r"`(?:\[(?:f|g|↰|↱)\]|\{\{key:(?:f|g|↰|↱)\}\})`\s*`(?:\[([^\[\]`\n]{1,12})\]|\{\{key(?:cap)?:([^{}`\n]+)\}\})`",
        lambda m: _collapse_bt_pair_2(m, registry),
        text,
    )

    # 2) Inside same span or unbackticked: `[f] [FUNC]` or `{{key:f}} {{key:FUNC}}`
    text = re.sub(
        r"(?:\[(?:f|g|↰|↱)\]|\{\{key:(?:f|g|↰|↱)\}\})\s*(?:\[([^\[\]`\n]{1,12})\]|\{\{key(?:cap)?:([^{}`\n]+)\}\})",
        lambda m: _collapse_plain_pair(m, registry),
        text,
    )

    is_directory_file = file_path.name in (
        "appendix-a-stack-lift-state-machine.md",
        "appendix-c-keycap-directory.md",
        "appendix-d-keycap-directory.md",
    )

    unambiguous_keys: Set[str] = {
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "C", "E",
        "A", "B", "D", "N",
        "ENTER", "ENT", "STO", "RCL", "XEQ", "SIN", "COS", "TAN", "ASIN", "ACOS", "ATAN",
        "LN", "LOG", "√x", "√𝑥", "eˣ", "𝑒ˣ", "10ˣ", "yˣ", "𝑦ˣ", "ˣ√y", "ˣ√𝑦", "1/x", "x⁻¹", "𝑥⁻¹",
        "x²", "𝑥²", "x³", "x!", "𝑥!", "Σ+", "Σ-", "Σ−", "x⇄y", "𝑥⇄𝑦", "R↓", "R↑", "LASTX", "LAST𝑥",
        "SHOW", "+/-", "<-", "<--", "x∥y", "𝑥∥𝑦", "CMPLX", "SOLVE", "POLY", "EQN", "PLOT", "TVM",
        "PARTS", "PROB", "L.R.", "SUMS", "MODES", "DISP", "CLEAR", "BASE", "FLAGS", "MEM", "REGS",
        "FDISP", "SIMP", "GCF", "LCM", "PRIME", "FACT", "C.FAC", "REP", "÷R", "MOD", "PV",
        "FRQ", "RNG", "IQR", "MED", "MODE", "MIN", "MAX", "1Q", "3Q", "MAD", "x̄", "ȳ", "ȳ", "x̄w", "x̄_w", "x̄,ȳ", "x̄, ȳ", "%CHG",
        "a ᵇ/c", "d/c", "/c", "a:b", "🕒", "▦", "🎲", "LINE", "COUNT", "NUM", "CSTK", "CLΣ", "CLx",
        "RECT", "TRI", "CIRC", "HYP", "PRISM", "CONE", "1…x", "t…x", "▸HR", "▸HMS", "▸%",
        "▸km", "▸mi", "▸θ,r", "▸y,x", "▸DEG", "▸RAD", "▸kg", "▸lb", "▸°C", "▸°F", "▸cm", "▸in",
        "▸l", "▸L", "▸gal", "▸g", "▸oz", "▸ft", "▸mL", "▸fl",
        "->km", "->mi", "->HR", "->HMS", "->DEG", "->RAD", "->kg", "->lb", "->°C", "->°F", "->cm", "->in", "->l", "->gal",
        "LFU0", "LFU1", "LFU2", "LFU3", "LFU4", "LFU5",
        "FIX", "SCI", "ENG", "ALL", "DEG", "RAD", "GRAD", "HEX", "DEC", "OCT", "BIN",
        "CLEQN", "CLVARS", "CLALL", "CLREGS", "CLSTK", "4-LVL", "8-LVL", "2-LVL", "INF",
        "IP", "FP", "ABS", "SGN", "Cn,r", "Pn,r", "RAND", "EXEC", "CLR", "I%YR", "PMT", "FV",
        "π", "∫", "|x|", "≠", "+", "-", "×", "÷", "%", "$",
        "Σx", "Σy", "Σx²", "Σy²", "Σxy", "↓", "↑", "ŷ", "x̂", "sx", "sy", "σx", "σy",
        "0.3̄", "?", "RND", "OFF", "nCr", "nPr", "e", ">", "≥", "<", "≤",
        "x&parallel;y", "&radic;x", "-&gt;REC", "-&gt;POL", "&divide;",
        "f", "g", "↰", "↱",
    }
    if is_sc32:
        unambiguous_keys.update({"m", "b", "r", "n"})

    lines = text.split("\n")
    out_lines = []
    in_fence = False
    in_display_math = False

    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue

        if not in_fence and line.strip().startswith("$$"):
            if line.strip().count("$$") == 1:
                in_display_math = not in_display_math
                out_lines.append(line)
                continue
        if in_display_math:
            out_lines.append(line)
            continue

        # Never inject {{key:...}} macros into Markdown heading lines (#, ##, ###)
        if not in_fence and line.lstrip().startswith("#"):
            clean_h = re.sub(r"`?\{\{key(?:cap)?:([^{}]+)\}\}`?", r"\1", line)
            out_lines.append(clean_h)
            continue

        is_table_row = line.strip().startswith("|")

        # Temporarily mask inline math $...$ on this line so \sqrt[3]{...} or [a, b] in LaTeX is preserved
        math_spans: List[str] = []
        if not in_fence and "$" in line:
            def _mask_math(m_math: re.Match) -> str:
                idx = len(math_spans)
                math_spans.append(m_math.group(0))
                return f"\x00MATH{idx}\x00"
            work_line = re.sub(r"\$\$[^$]+\$\$|\$[^$\n]+\$", _mask_math, line)
        else:
            work_line = line

        def _tok_repl(m: re.Match) -> str:
            tok = m.group(1).strip()
            if tok not in unambiguous_keys:
                return m.group(0)
            try:
                entry = registry.resolve(tok)
            except ValueError:
                return m.group(0)

            if entry.shift is None:
                return f"{{{{key:{entry.canonical}}}}}"

            if is_directory_file or is_table_row or in_fence or tok in ("↓", "↑"):
                return f"{{{{keycap:{entry.canonical}}}}}"
            return f"{{{{key:{entry.canonical}}}}}"

        new_line = re.sub(r"(?<![!{\\])\[([^\[\]\n]{1,12})\](?!\()", _tok_repl, work_line)

        if math_spans:
            for idx, m_str in enumerate(math_spans):
                new_line = new_line.replace(f"\x00MATH{idx}\x00", m_str)

        # Repair any odd inline backtick caused by an earlier pass
        if not in_fence and new_line.count("`") % 2 != 0:
            fixed = re.sub(r"(`[^`\n]*\{\{key(?:cap)?:[^{}]+\}\})(?![`\w\[])", r"\1`", new_line)
            if fixed.count("`") % 2 != 0:
                fixed = re.sub(r"(?<![`\w\]])(\{\{key(?:cap)?:[^{}]+\}\}[^`\n]*`)", r"`\1", new_line)
            if fixed.count("`") % 2 == 0:
                new_line = fixed

        out_lines.append(new_line)

    return "\n".join(out_lines)


def _collapse_bt_pair_2(match: re.Match, registry: KeyRegistry) -> str:
    func_tok = (match.group(1) or match.group(2) or "").strip()
    try:
        entry = registry.resolve(func_tok)
        if entry.layer in ("yellow", "blue", "primary", "menu"):
            return f"`{{{{key:{entry.canonical}}}}}`"
    except ValueError:
        pass
    return match.group(0)


def _collapse_plain_pair(match: re.Match, registry: KeyRegistry) -> str:
    func_tok = (match.group(1) or match.group(2) or "").strip()
    try:
        entry = registry.resolve(func_tok)
        if entry.layer in ("yellow", "blue", "primary", "menu"):
            return f"{{{{key:{entry.canonical}}}}}"
    except ValueError:
        pass
    return match.group(0)


def add_faceplate_color_note(text: str, file_path: Path, is_sc32: bool) -> str:
    """
    Adds a concise note in Chapter 1 of the SC-6 manual explaining that key and shift
    accent colors vary depending on the faceplate theme. On SC-32, faceplate themes are
    not enumerated in Chapter 1 (Flag 3 is documented in the Appendix C Flags Directory).
    """
    if is_sc32:
        return text

    if (
        "Faceplate Themes & Shift Legend Conventions" in text
        or "Your Favorite Color Theme, Same Friendly Shift Keys" in text
        or "interchangeable faceplate" in text
    ):
        return text

    # Skip past YAML frontmatter if present
    m_fm = re.match(r"^(---\n.*?\n---\n)", text, flags=re.DOTALL)
    fm_end = m_fm.end() if m_fm else 0

    if not is_sc32 and file_path.name == "01-hardware-architecture.md":
        note = (
            "\n> **Faceplate Themes & Shift Legend Conventions:**  \n"
            "> Because the StackCalc SC-6 hardware faceplates and companion app support multiple visual themes (`Pure Black`, `Retro Futurism`, `Pioneer`, `Stealth`, `Supernova`, `Voyager`, and `Arcade`), keycap and shift accent colors vary by faceplate. Throughout this textbook, shifted operations are always referenced by their functional shift symbols rather than color: **`{{key:f}}` Shift** (Row 5, Col 0) and **`{{key:g}}` Shift** (Row 6, Col 0).\n"
        )
        idx = text.find("\n---\n", fm_end)
        if idx != -1:
            return text[:idx] + note + text[idx:]

    return text


def convert_images_and_sequences_to_macros(text: str, file_path: Path, is_sc32: bool) -> str:
    """
    1. Converts manipulative block and 3D hardware markdown images (`![Caption](../../assets/.../<png>)`)
       into `{{blocks:ID|Caption}}` macros grounded in `blocks_registry.json`.
    2. Converts SwiftUI screenshot markdown images into `{{res:ID:screenshot|Caption}}` macros.
    3. Strips any leaked internal registry callouts (`> **Verified Hardware Execution (...)`).
    """
    from book_engine import get_blocks_registry

    blocks = get_blocks_registry()
    png_to_block_id = {entry["png"]: bid for bid, entry in blocks.items()}

    lines = text.split("\n")
    out_lines = []
    in_fence = False

    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if in_fence:
            out_lines.append(line)
            continue

        # Strip leaked internal registry ID callouts
        if line.strip().startswith("> **Verified Hardware Execution ("):
            continue

        m_img = re.match(r"^!\[(.*?)\]\((.*?)\)\s*$", line.strip())
        if m_img:
            raw_caption = m_img.group(1).strip()
            clean_caption = re.sub(r"\{\{key(?:cap)?:([^{}]+)\}\}", r"[\1]", raw_caption)
            clean_caption = clean_caption.replace("|", "-").replace("{", "").replace("}", "")
            img_path = m_img.group(2).strip()
            img_name = Path(img_path).name

            if img_name in png_to_block_id:
                bid = png_to_block_id[img_name]
                out_lines.append(f"{{{{blocks:{bid}|{clean_caption}}}}}")
                continue

            if img_name.endswith(".png") and (ASSETS_MANUALS_DIR / "screenshots" / img_name).exists():
                shot_id = img_name[:-4]
                out_lines.append(f"{{{{res:{shot_id}:screenshot|{clean_caption}}}}}")
                continue

        out_lines.append(line)

    return "\n".join(out_lines)


def sync_consolidated_user_guides() -> None:
    """
    Synchronizes the single-page web manuals (`sc32-user-guide.md` and
    `sc6-user-guide.md`) directly from the rendered chapter files so
    they never drift from the chapter sources.
    """
    for is_sc32 in (True, False):
        sub = "sc32" if is_sc32 else "sc6"
        guide_name = "sc32-user-guide.md" if is_sc32 else "sc6-user-guide.md"
        guide_path = MANUALS_DIR / guide_name
        if not guide_path.exists():
            continue

        if is_sc32:
            header = (
                "---\n"
                'title: "Thinking in the Stack: The Art of Reverse Polish Notation (SC-32 Complete Edition)"\n'
                'description: "Complete single-page edition of Thinking in the Stack: Scientific Computing, Engineering Analysis & the StackCalc SC-32."\n'
                "---\n"
            )
        else:
            header = (
                "---\n"
                'title: "From Blocks to the Stack: Hands-On Math & the SC-6 Stack Calculator (Complete Edition)"\n'
                'description: "Complete single-page edition of From Blocks to the Stack: Hands-On Math & the SC-6 Stack Calculator."\n'
                "---\n"
            )

        chapter_files = sorted((MANUALS_DIR / sub).glob("*.md"))
        ordered = [p for p in chapter_files if p.name == "index.md"] + [
            p for p in chapter_files if p.name != "index.md"
        ]
        parts: List[str] = []
        for ch_path in ordered:
            ch_raw = ch_path.read_text(encoding="utf-8")
            ch_body = re.sub(r"^---\n.*?\n---\n", "", ch_raw, flags=re.DOTALL)
            ch_rendered = process_manual_markdown(ch_body, ch_path, is_sc32=is_sc32)
            # Rewrite relative image paths `../../assets/` -> `../assets/` for top-level manuals/ dir
            ch_rendered = ch_rendered.replace("(../../assets/", "(../assets/")
            ch_rendered = ch_rendered.replace("(../../curriculum/", "(../curriculum/")
            ch_rendered = ch_rendered.replace("(../../exam-compliance.md", "(../exam-compliance.md")
            ch_rendered = re.sub(
                r"\]\(((?:[0-9]{2}-[^)#]+|appendix-[a-e]-[^)#]+|index\.md)(?:#[^)]+)?)\)",
                rf"]({sub}/\1)",
                ch_rendered,
            )
            parts.append(ch_rendered.strip())

        guide_path.write_text(header + "\n" + "\n\n---\n\n".join(parts) + "\n", encoding="utf-8")

    # Sync SC-6 and SC-32 markdown sources and consolidated guides to mirror directories across workspaces
    import shutil
    mirror_manual_roots = [
        REPO_ROOT / "Website" / "docs" / "manuals",
        REPO_ROOT.parent / "stackcalc" / "docs" / "manuals",
        REPO_ROOT.parent / "stackcalc" / "Website" / "docs" / "manuals",
    ]
    for mroot in mirror_manual_roots:
        if mroot.exists():
            for sub_name, guide_fn in (("sc6", "sc6-user-guide.md"), ("sc32", "sc32-user-guide.md")):
                sub_dst = mroot / sub_name
                if sub_dst.exists():
                    for src_md in sorted((MANUALS_DIR / sub_name).glob("*.md")):
                        dst_file = sub_dst / src_md.name
                        if src_md.resolve() != dst_file.resolve():
                            shutil.copy2(src_md, dst_file)
                guide_src = MANUALS_DIR / guide_fn
                if guide_src.exists() and (mroot / guide_fn).exists():
                    dst_guide = mroot / guide_fn
                    if guide_src.resolve() != dst_guide.resolve():
                        shutil.copy2(guide_src, dst_guide)


def process_all_files() -> None:
    manual_files: List[Tuple[Path, bool]] = []
    for p in sorted((MANUALS_DIR / "sc32").glob("*.md")):
        manual_files.append((p, True))
    for p in sorted((MANUALS_DIR / "sc6").glob("*.md")):
        manual_files.append((p, False))

    total_fences_fixed = 0
    total_key_macros = 0
    total_seq_macros = 0
    total_res_macros = 0
    total_screenshot_macros = 0
    total_blocks_macros = 0
    total_cite_macros = 0
    total_bib_macros = 0

    for fpath, is_sc32 in manual_files:
        orig = fpath.read_text(encoding="utf-8")

        # Separate YAML frontmatter from body so macros never corrupt YAML metadata
        m_fm = re.match(r"^(---\n.*?\n---\n)", orig, flags=re.DOTALL)
        if m_fm:
            fm_block = m_fm.group(1)
            body = orig[m_fm.end():]
            # Clean any {{key:...}} from YAML frontmatter
            fm_block = re.sub(r"\{\{key(?:cap)?:([^{}]+)\}\}", r"[\1]", fm_block)
        else:
            fm_block = ""
            body = orig

        body, fences = fix_inverted_code_fences(body)
        total_fences_fixed += fences
        body = replace_persona_headings(body)
        body = remove_shift_color_terminology(body, is_sc32=is_sc32)
        body = move_baseline_banner_after_opening_story(body, fpath)
        body = strip_all_manual_heading_numbers(body, fpath)
        body = convert_keystrokes_to_macros(body, fpath, is_sc32=is_sc32)
        body = convert_images_and_sequences_to_macros(body, fpath, is_sc32=is_sc32)

        txt = fm_block + body
        txt = add_faceplate_color_note(txt, fpath, is_sc32=is_sc32)

        if txt != orig:
            fpath.write_text(txt, encoding="utf-8")

        # Validate macro expansion and auto-numbering via book_engine!
        rendered = process_manual_markdown(txt, fpath, is_sc32=is_sc32)
        total_key_macros += len(re.findall(r"\{\{(?:key|keycap):[^{}]+\}\}", txt))
        total_seq_macros += len(re.findall(r"\{\{(?:seq|seq_keys):[^{}]+\}\}|\{\{res:[^{}:]+:(?:keys|keystrokes|seq|seq_keys|both|inline)\}\}", txt))
        total_res_macros += len(re.findall(r"\{\{res:[^{}:]+(?::(?:value|res|result|number|both|inline|stack|table))?\}\}", txt))
        total_screenshot_macros += len(re.findall(r"\{\{(?:screenshot:[^{}\n]+|res:[^{}:]+:screenshot[^{}\n]*)\}\}", txt))
        total_blocks_macros += len(re.findall(r"\{\{blocks:[^\n]+\}\}", txt))
        total_cite_macros += len(re.findall(r"\{\{cite:[^{}]+\}\}", txt))
        total_bib_macros += len(re.findall(r"\{\{bibliography:[^{}]+\}\}", txt))

        # 0. Assert zero raw ![...](...) markdown image links remain in source (all must be {{res:ID:screenshot}} or {{blocks:...}})
        raw_imgs = re.findall(r"!\[[^\]]*\]\([^)]+\)", txt)
        assert not raw_imgs, f"Raw markdown image link(s) {raw_imgs} found in {fpath} (must use {{{{res:ID:screenshot}}}} or {{{{blocks:...}}}})"

        # 0a. Assert zero {{key:...}} or blockquotes inside YAML frontmatter
        m_fm_check = re.match(r"^---\n(.*?)\n---\n", txt, flags=re.DOTALL)
        if m_fm_check:
            fm_inner = m_fm_check.group(1)
            assert "{{key" not in fm_inner, f"Macro found inside YAML frontmatter in {fpath}"
            assert "\n>" not in fm_inner, f"Blockquote found inside YAML frontmatter in {fpath}"

        # 0a2. Assert zero leaked internal registry IDs ('Verified Hardware Execution (', 'StackCalc Live View (')
        assert "Verified Hardware Execution (" not in rendered, f"Leaked registry ID callout in {fpath}"
        assert "StackCalc Live View (" not in rendered, f"Leaked screenshot ID caption in {fpath}"

        # 0b. Assert zero ASCII +---+ / +===+ / +───+ / ┌───┐ boxes remain anywhere in source or rendered output
        ascii_box_lines = [
            (idx, l)
            for idx, l in enumerate(txt.splitlines(), 1)
            if re.search(r"(\+[-=─]{3,}\+|[┌┐└┘├┤┬┴┼][─═]{2,})", l)
        ]
        assert not ascii_box_lines, f"ASCII table/box found in {fpath}: {ascii_box_lines[:3]}"

        # 0b2. Assert zero dummy '| Field | Value |' headers and zero empty '|  |  |' rows
        assert "| Field | Value |" not in txt, f"Dummy '| Field | Value |' table header found in {fpath}"
        empty_cell_rows = [
            (idx, l)
            for idx, l in enumerate(txt.splitlines(), 1)
            if l.strip().startswith("|") and re.search(r"\|\s*\|\s*\|", l)
        ]
        assert not empty_cell_rows, f"Empty table cells found in {fpath}: {empty_cell_rows[:3]}"

        # 0b3. Assert zero 'Verified in RPNCore' placeholder strings in rendered output
        assert "Verified in RPNCore" not in rendered, f"Placeholder 'Verified in RPNCore' found in rendered {fpath}"

        # 0c. Assert zero double-shift expansions ([↰] [↰], [↱] [↱], [f] [f], [g] [g])
        for dbl_shift in ("[↰] [↰]", "[↱] [↱]", "[f] [f]", "[g] [g]"):
            assert dbl_shift not in rendered, f"Duplicate shift token {dbl_shift} found in rendered {fpath}"

        # 0d. Assert zero <number> {{key:ENTER}} {{key:<monadic>}} bugs in source
        monadic_enter_bugs = re.findall(
            r"(?:`[0-9.]+`|(?:^|\s)[0-9.]+)\s+\{\{key:ENTER\}\}\s+\{\{key:(?:x²|√x|1/x|SIN|COS|TAN|ASIN|ACOS|ATAN|LN|LOG|eˣ|10ˣ)\}\}",
            txt,
        )
        assert not monadic_enter_bugs, f"Redundant {{key:ENTER}} before monadic operator in {fpath}: {monadic_enter_bugs}"

        # 1. Assert zero unexpanded macros
        for m_kind in ("key", "keycap", "seq", "seq_keys", "res", "screenshot", "blocks", "cite", "bibliography"):
            assert f"{{{{{m_kind}:" not in rendered, f"Unexpanded {{{{{m_kind}:...}}}} macro in {fpath}"

        # 2. Assert code fence parity and inline backtick parity
        in_fence = False
        sec_nums: List[str] = []
        for idx, line in enumerate(rendered.splitlines(), 1):
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if not in_fence:
                assert line.count("`") % 2 == 0, f"Unbalanced inline backtick in {fpath}:{idx}: {line}"
                m_sec = re.match(r"^(#{2,3})\s+((?:[0-9]+|[A-E])(?:\.[0-9]+)+)\s+", line)
                if m_sec:
                    sec_nums.append(m_sec.group(2))
        assert not in_fence, f"Unclosed code fence in {fpath}"

        # 3. Assert zero duplicate section numbers
        dups = [k for k, v in Counter(sec_nums).items() if v > 1]
        assert not dups, f"Duplicate section numbers {dups} in {fpath}"

    # 4. Validate all entries in sequences_registry.json for monadic-ENTER, double-shift, or placeholder res defects
    import json
    seq_reg_path = ASSETS_MANUALS_DIR / "sequences_registry.json"
    seq_reg_data = json.loads(seq_reg_path.read_text(encoding="utf-8"))
    assert len(seq_reg_data) >= 650, f"Expected >= 650 sequences in sequences_registry.json, found {len(seq_reg_data)}"
    for seq_id, seq_entry in seq_reg_data.items():
        s_txt = seq_entry.get("seq", "")
        r_txt = seq_entry.get("res", "")
        assert r_txt and r_txt != "Verified in RPNCore" and not r_txt.startswith("Displays **"), (
            f"Invalid or placeholder res in sequences_registry.json[{seq_id}]: {r_txt!r}"
        )
        if seq_entry.get("model", "sc32") == "sc32":
            bad_monadic = re.findall(
                r"(?:`[0-9.]+`|(?:^|\s)[0-9.]+)\s+\{\{key:ENTER\}\}\s+\{\{key:(?:x²|√x|1/x|SIN|COS|TAN|ASIN|ACOS|ATAN|LN|LOG|eˣ|10ˣ)\}\}",
                s_txt,
            )
            assert not bad_monadic, f"Redundant {{key:ENTER}} before monadic operator in sequences_registry.json[{seq_id}]: {bad_monadic}"
        for shift_k in ("{{key:↰}} {{key:↰}}", "{{key:↱}} {{key:↱}}", "{{key:f}} {{key:f}}", "{{key:g}} {{key:g}}"):
            assert shift_k not in s_txt, f"Duplicate shift macro in sequences_registry.json[{seq_id}]: {s_txt}"

    # 4b. Validate citations_registry.json and bibliography.bib
    citations_reg_path = ASSETS_MANUALS_DIR / "citations_registry.json"
    assert citations_reg_path.exists(), f"Missing {citations_reg_path}"
    citations_reg_data = json.loads(citations_reg_path.read_text(encoding="utf-8"))
    assert len(citations_reg_data) >= 30, f"Expected >= 30 citations in citations_registry.json, found {len(citations_reg_data)}"
    for cid, c_entry in citations_reg_data.items():
        assert c_entry.get("author"), f"Missing author in citations_registry.json[{cid}]"
        assert c_entry.get("year"), f"Missing year in citations_registry.json[{cid}]"
        assert c_entry.get("title"), f"Missing title in citations_registry.json[{cid}]"
        assert c_entry.get("annotation"), f"Missing annotation in citations_registry.json[{cid}]"
        assert c_entry.get("volume_scope") in ("sc32", "sc6", "both"), f"Invalid volume_scope in citations_registry.json[{cid}]"

    # 5. Validate website curriculum, tutorial, and learning-lab pages (if present)
    curriculum_pages = [
        p for p in [
            STACKCALC_DOCS_DIR / "learning-lab.md",
            STACKCALC_DOCS_DIR / "tutorials.md",
            *(sorted((STACKCALC_DOCS_DIR / "curriculum").glob("*.md")) if (STACKCALC_DOCS_DIR / "curriculum").exists() else []),
        ]
        if p.exists()
    ]
    for cpath in curriculum_pages:
        ctxt = cpath.read_text(encoding="utf-8")
        crendered = expand_key_macros(ctxt, is_sc32=("elementary" not in cpath.name and "sc6" not in cpath.name), file_path=cpath)
        for m_kind in ("key", "keycap", "seq", "seq_keys", "res", "screenshot", "blocks", "cite", "bibliography"):
            assert f"{{{{{m_kind}:" not in crendered, f"Unexpanded {{{{{m_kind}:...}}}} macro in {cpath}"

    # 6. Export curriculum_uil_registry.json for RPNCore unit test verification
    export_curriculum_uil_registry()

    # Synchronize single-page user guides
    sync_consolidated_user_guides()

    # 7. Gate S10: Programmatic audit of 4-register (T, Z, Y, X) stack tables & Gate S15 inline traces
    from verify_and_sync_stack_tables import audit_all_tables_and_traces
    strict_stack = "--strict-stack" in sys.argv or "--check-stack" in sys.argv or os.environ.get("GATE_S10_STRICT") == "1"
    stack_stats = audit_all_tables_and_traces(repo_root=REPO_ROOT, strict=strict_stack, verbose=False)
    assert stack_stats["tables_checked"] >= 80, f"Expected >= 80 signature showcase tables in Gate S15, found {stack_stats['tables_checked']}"

    # 8. Gate S12: Assert zero single-brace {key:, {res:, or {cite: macro patterns in manuals/
    manuals_scanned = validate_no_single_brace_macros(MANUALS_DIR)

    # 9. Gate S16: Assert zero persona-bleed callout labels or explicit CRA scaffolding in chapter files & consolidated guides
    validate_no_persona_or_cra_bleed(MANUALS_DIR)

    # 10. Gate S17: Assert SC-32 3-section narrative/calculator architecture, 3-decimal precision, and 43-key appendix parity
    s17_stats = validate_sc32_chapter_architecture_and_precision(MANUALS_DIR, seq_reg_data)

    print(f"✅ Transformed and validated {len(manual_files)} manual chapter/appendix files + {len(curriculum_pages)} curriculum pages + 2 consolidated guides.")
    print(f"   - Validated {{key:...}} / {{keycap:...}} macros: {total_key_macros:,}")
    print(f"   - Validated {{res:ID:keys}} & {{res:ID:value}}:  {total_seq_macros:,} sequences / {total_res_macros:,} results ({len(seq_reg_data):,} registered in sequences_registry.json)")
    print(f"   - Validated {{res:ID:screenshot}} macros:        {total_screenshot_macros:,}")
    print(f"   - Validated {{blocks:...}} macros:               {total_blocks_macros:,}")
    print(f"   - Validated {{cite:...}} macros:                 {total_cite_macros:,} citations / {total_bib_macros:,} bibliographies ({len(citations_reg_data):,} registered in citations_registry.json)")
    disc_msg = "100% PASS" if stack_stats["table_discrepancies"] == 0 else f"{stack_stats['table_discrepancies']} discrepancies tracked"
    print(f"   - Gate S10 Stack Verification:                   {stack_stats['tables_checked']:,} tables / {stack_stats['traces_checked']:,} inline traces audited ({disc_msg})")
    print(f"   - Gate S12 Single-Brace Macro Audit:             {manuals_scanned} manual files scanned (0 single-brace {{key:/{{res:/{{cite: defects)")
    print("   - Gate S16 Persona-Bleed & CRA Scaffolding:      0 persona labels / 0 explicit CRA bullets: 100% PASS")
    print(
        f"   - Gate S17 SC-32 Narrative & Precision Audit:    {s17_stats['chapters_checked']} chapters (0 keycaps in N.1/N.2 & N.3 prose, "
        f"{s17_stats['stack_tables']} stack tables, {s17_stats['screenshots']} LCD figures, <=3-decimal res values, 43-key parity): 100% PASS"
    )
    print("   - Zero ASCII boxes, zero dummy tables, zero placeholder results, zero double-shifts, zero monadic-ENTER bugs: 100% PASS")
    print("   - Code fence parity, inline backtick parity, and section numbering uniqueness: 100% PASS")


def validate_no_single_brace_macros(manuals_dir: Path) -> int:
    """
    Gate S12: Scans all .md files in manuals_dir and asserts that zero single-brace
    (?<!{){key:, (?<!{){res:, or (?<!{){cite: macro patterns exist.
    """
    single_brace_pat = re.compile(r"(?<!\{)\{(?:key|res|cite):")
    violations: List[str] = []
    files_checked = 0
    for md_file in sorted(manuals_dir.rglob("*.md")):
        files_checked += 1
        content = md_file.read_text(encoding="utf-8")
        matches = list(single_brace_pat.finditer(content))
        if matches:
            line_numbers = [content[:m.start()].count("\n") + 1 for m in matches[:5]]
            violations.append(f"{md_file.relative_to(REPO_ROOT)} ({len(matches)} violations at lines {line_numbers})")
    assert not violations, (
        f"Gate S12 Validation Failure: Single-brace macro pattern(s) (?<!\\{{)\\{{key:, \\{{res:, or \\{{cite: found in {len(violations)} manual file(s):\n  "
        + "\n  ".join(violations)
    )
    return files_checked


def validate_no_persona_or_cra_bleed(manuals_dir: Path) -> None:
    """
    Gate S16: Asserts that zero design-persona labels, explicit CRA scaffolding tags,
    prompt-to-prose echoes, or AI-slop templates bleed into the chapter manuscripts
    or consolidated user guides.
    """
    banned_patterns = [
        r"Homeschooler Diagnostic Checkpoint",
        r"Stack Verification Checkpoint",
        r"Diagnostic Checkpoint \d",
        r"Calculator Enthusiast Note",
        r"Note for HP Purists",
        r"HP Purist Tip",
        r"For Parents &(?:amp;)? Teachers:",
        r"For Educators &(?:amp;)? Parents:",
        r"Parent's De-Stressing Guide:",
        r"For the Skeptical Parent:",
        r"Contest Quick-Lookup Cross-Reference:",
        r"CRA Pedagogical Sequence",
        r"\*Concrete:\*",
        r"\*Representational:\*",
        r"\*Abstract:\*",
        r"Thematic Arc",
        r"Mission Briefing:",
        r"Scale Big on (?:StackCalc|your SC-6)",
        r"Model(?:ing)? small with blocks",
        r"\\le 24\$\s*tiles",
        r"\(\$\\le 24\$\)",
        r"Teaching & Instrument Architecture",
        r"Instrument Architecture & Diagnostic",
        r"Automated Engine Reliability",
        r"100% Engine Grounding",
        r"\*Physical & Geometric Motivation:\*",
        r"\*Curriculum Cross-Reference:\*",
        r"Superpower Showdown",
        r"Superpower [1-4]",
        r"Hands-On Studio Proof",
        r"Deviation Rubric",
        r"button rubric",
        r"publication-grade",
        r"masterwork",
        r"To evaluate [^\n]+ without nested parentheses",
        r"On the RPN stack, we evaluate this relationship",
        r"Classroom Script \d",
        r"Script \d+\.\d+:",
        r"Verbatim Teacher Dialogue",
        r"```(?:openscad|scad|python|swift|c|cpp)\b",
        r"<div\b",
        r"\[!(?:NOTE|TIP|IMPORTANT|WARNING|CAUTION|CHECKPOINT|TEACHER)\]",
        r"&(?:amp|bull|rarr|theta);",
    ]
    combined_pat = re.compile("|".join(banned_patterns), flags=re.IGNORECASE)
    target_files = [
        *sorted((manuals_dir / "sc32").glob("*.md")),
        *sorted((manuals_dir / "sc6").glob("*.md")),
        *([manuals_dir / "sc32-user-guide.md"] if (manuals_dir / "sc32-user-guide.md").exists() else []),
        *([manuals_dir / "sc6-user-guide.md"] if (manuals_dir / "sc6-user-guide.md").exists() else []),
    ]
    violations: List[str] = []
    for fpath in target_files:
        txt = fpath.read_text(encoding="utf-8")
        for m in combined_pat.finditer(txt):
            line_no = txt[:m.start()].count("\n") + 1
            violations.append(f"{fpath.relative_to(REPO_ROOT)}:{line_no} -> {m.group(0)!r}")
    assert not violations, (
        f"Gate S16 Anti-AI-Slop / Persona-Bleed / Explicit CRA Scaffolding Failure ({len(violations)} violation(s)):\n  "
        + "\n  ".join(violations[:15])
    )


def validate_sc32_chapter_architecture_and_precision(
    manuals_dir: Path, seq_reg_data: Dict[str, Any]
) -> Dict[str, int]:
    """
    Gate S17: Enforces Volume II (SC-32) structural, narrative, and precision invariants:
      1. Every chapter (01..14) has exactly 3 `## ` sections (N.1, N.2, N.3).
      2. Narrative sections N.1 and N.2 contain zero `{{key:...}}` or `{{keycap:...}}` macros.
      3. The opening of Section N.3 (before the first `### ` subsection) contains a
         self-contained Keypad & Softkey Orientation Block (>= 3 `{{key:...}}` macros).
      4. All `### ` narrative subsections of Section N.3 contain zero inline `{{key:...}}`
         macros outside markdown tables.
      5. Every chapter contains 1 or 2 four-register stack tables (<= 22 total across Vol II),
         and <= 16 LCD screenshot figures across Vol II.
      6. Every `{{res:ID:value}}` referenced in SC-32 chapters has <= 3 decimal places.
      7. Appendix A, C, and D maintain full 43-key hardware and 14-chapter worked-example parity.
      8. Every Markdown table row across all SC-32 files has the exact same unescaped `|` count as its header.
      9. Every register cell (`T, Z, Y, X`) in all SC-32 4-register stack tables matches RPNStackSimulator within 6e-4.
      10. Every executable worked-example sequence in Appendix D matches its Verified Result column under RPNStackSimulator.
      11. Every `Eq. X.Y` and `Figure X.Y` reference across all SC-32 files resolves to a defined equation/figure after rendering.
    """
    import verify_and_sync_stack_tables as vst
    import book_engine

    sc32_dir = manuals_dir / "sc32"
    chapter_files = sorted(sc32_dir.glob("[0-9][0-9]-*.md"))
    assert len(chapter_files) == 14, f"Expected 14 SC-32 chapter files, found {len(chapter_files)}"

    # Check 8: Markdown table pipe-count parity across all SC-32 files
    pipe_violations: List[str] = []
    for md_file in sorted(sc32_dir.glob("*.md")):
        md_lines = md_file.read_text(encoding="utf-8").splitlines()
        in_table = False
        expected_pipes = 0
        for line_idx, ln in enumerate(md_lines, 1):
            s = ln.strip()
            if s.startswith("|") and s.endswith("|"):
                pipes = len(re.findall(r"(?<!\\)\|", s))
                if not in_table:
                    in_table = True
                    expected_pipes = pipes
                elif pipes != expected_pipes:
                    pipe_violations.append(
                        f"{md_file.name}:{line_idx} has {pipes} pipes (expected {expected_pipes})"
                    )
            else:
                in_table = False
    assert not pipe_violations, (
        "Gate S17 Failure: Unescaped pipe mismatch in SC-32 Markdown table(s):\n  "
        + "\n  ".join(pipe_violations)
    )

    key_pat = re.compile(r"\{\{key(?:cap)?:[^}]+\}\}")
    res_val_pat = re.compile(r"\{\{res:([^:}]+):value\}\}")
    screenshot_pat = re.compile(r"\{\{res:[^:}]+:screenshot(?:\|[^}]*)?\}\}")

    total_stack_tables = 0
    total_screenshots = 0
    referenced_res_ids: Set[str] = set()

    for ch_file in chapter_files:
        txt = ch_file.read_text(encoding="utf-8")
        lines = txt.splitlines()
        h2_indices = [i for i, ln in enumerate(lines) if ln.startswith("## ")]
        assert len(h2_indices) == 3, (
            f"Gate S17 Failure in {ch_file.name}: Expected exactly 3 `## ` sections (N.1, N.2, N.3), "
            f"found {len(h2_indices)}: {[lines[i] for i in h2_indices]}"
        )

        # Sections N.1 and N.2 must have zero {{key:...}} macros
        sec_1_and_2_txt = "\n".join(lines[h2_indices[0] : h2_indices[2]])
        s12_keys = key_pat.findall(sec_1_and_2_txt)
        assert not s12_keys, (
            f"Gate S17 Failure in {ch_file.name}: Sections N.1/N.2 must contain zero keycap macros, "
            f"found {len(s12_keys)}: {s12_keys[:5]}"
        )

        # Section N.3 structure: orientation block before first `### `, then `### ` narrative subsections
        sec_3_lines = lines[h2_indices[2] :]
        h3_rel_indices = [i for i, ln in enumerate(sec_3_lines) if ln.startswith("### ")]
        assert h3_rel_indices, f"Gate S17 Failure in {ch_file.name}: Section N.3 has no `### ` subsections"

        n3_intro_txt = "\n".join(sec_3_lines[: h3_rel_indices[0]])
        intro_keys = key_pat.findall(n3_intro_txt)
        assert len(intro_keys) >= 3, (
            f"Gate S17 Failure in {ch_file.name}: Section N.3 opening orientation block must introduce "
            f"chapter keys (>= 3 `{{{{key:...}}}}` macros), found {len(intro_keys)}"
        )

        # Inside N.3 `### ` subsections, zero `{{key:...}}` allowed outside markdown table rows
        for rel_idx in range(h3_rel_indices[0], len(sec_3_lines)):
            ln = sec_3_lines[rel_idx]
            if not ln.strip().startswith("|"):
                prose_keys = key_pat.findall(ln)
                assert not prose_keys, (
                    f"Gate S17 Failure in {ch_file.name} (line {h2_indices[2] + rel_idx + 1}): "
                    f"Inline keycap macro(s) {prose_keys} found in N.3 `###` narrative prose outside stack table"
                )

        # Count 4-register stack tables and screenshots
        ch_stack_tables = sum(
            1 for ln in lines if ln.strip().startswith("|") and "Register T" in ln and "Register X" in ln
        )
        assert 1 <= ch_stack_tables <= 2, (
            f"Gate S17 Failure in {ch_file.name}: Expected 1 or 2 four-register stack tables, found {ch_stack_tables}"
        )
        total_stack_tables += ch_stack_tables
        total_screenshots += len(screenshot_pat.findall(txt))

        for m in res_val_pat.finditer(txt):
            referenced_res_ids.add(m.group(1))

    assert total_stack_tables <= 22, (
        f"Gate S17 Failure: Expected <= 22 four-register stack tables across SC-32 chapters, found {total_stack_tables}"
    )
    assert total_screenshots <= 16, (
        f"Gate S17 Failure: Expected <= 16 LCD screenshots across SC-32 chapters, found {total_screenshots}"
    )

    # Check 3-decimal precision on all referenced {{res:ID:value}} entries in SC-32 chapters
    over_precision: List[str] = []
    for rid in sorted(referenced_res_ids):
        r_val = str(seq_reg_data.get(rid, {}).get("res", ""))
        if re.search(r"\.\d{4,}", r_val):
            over_precision.append(f"{rid}: {r_val!r}")
    assert not over_precision, (
        f"Gate S17 Failure: SC-32 {{res:ID:value}} entries exceed 3 decimal places:\n  " + "\n  ".join(over_precision)
    )

    # Check Appendix A, C, and D hardware/chapter parity
    app_a = (sc32_dir / "appendix-a-stack-lift-state-machine.md").read_text(encoding="utf-8")
    app_c = (sc32_dir / "appendix-c-keycap-directory.md").read_text(encoding="utf-8")
    app_d = (sc32_dir / "appendix-d-constants-and-equations.md").read_text(encoding="utf-8")
    assert "`TVM` / `PLOT`" in app_a, "Gate S17 Failure: Appendix A missing `TVM` / `PLOT` on `x∥y`"
    for k_idx in range(1, 44):
        assert re.search(rf"^\|\s*\*\*{k_idx}\*\*\s*\|", app_c, re.MULTILINE), (
            f"Gate S17 Failure: Appendix C missing key #{k_idx}"
        )
    assert "{{key:PLOT}}" in app_c, "Gate S17 Failure: Appendix C missing `{{key:PLOT}}` on R7, C3 (`x∥y`)"
    for ch_num in range(1, 15):
        assert f"**Ch {ch_num}:" in app_d, f"Gate S17 Failure: Appendix D missing worked sequences for Ch {ch_num}"

    # Check 9: Strict 3-decimal stack table cell accuracy (tol = 6e-4) across all SC-32 files
    strict_table_drifts: List[str] = []
    for ch_file in sorted(sc32_dir.glob("*.md")):
        tables = vst.find_4_register_tables(ch_file)
        for tbl in tables:
            sim = vst.RPNStackSimulator()
            if "05-complex" in str(tbl.file_path):
                sim.angle_mode = "rad"
            if any("{{key:A}}" in r[1] or "{{key:XEQ}}" in r[1] or "{{key:EXEC}}" in r[1] for r in tbl.row_lines):
                sim.poly_mode = True
            if any(
                re.search(r"^\s*[\$`\*]*0[0-9A-Fa-f]*h[\$`\*]*\s*$", r[1].split("|")[tbl.col_t + 1])
                for r in tbl.row_lines
                if len(r[1].split("|")) > tbl.col_t + 1
            ):
                sim.base_mode = "hex"
            for r_idx, (line_num, raw_line) in enumerate(tbl.row_lines):
                cells = [c.strip() for c in raw_line.split("|")[1:-1]]
                if len(cells) <= max(tbl.col_k, tbl.col_t, tbl.col_z, tbl.col_y, tbl.col_x):
                    continue
                k_cell = cells[tbl.col_k]
                step_x = vst.parse_register_cell(cells[tbl.col_x])
                step_y = vst.parse_register_cell(cells[tbl.col_y])
                vst.execute_keystroke_sequence(sim, k_cell, step_x=step_x, step_y=step_y)
                reg_cells = [cells[tbl.col_t], cells[tbl.col_z], cells[tbl.col_y], cells[tbl.col_x]]
                sim_vals = [sim.t, sim.z, sim.y, sim.x]
                for reg_name, doc_cell, sim_val in zip(["T", "Z", "Y", "X"], reg_cells, sim_vals):
                    doc_num = vst.parse_register_cell(doc_cell)
                    if doc_num is not None and abs(doc_num - sim_val) > 6e-4:
                        strict_table_drifts.append(
                            f"{ch_file.name}:L{line_num} row {r_idx+1} {reg_name}: "
                            f"doc={doc_cell!r} ({doc_num}) vs sim={sim_val:.6f}"
                        )
    assert not strict_table_drifts, (
        "Gate S17 Failure: SC-32 4-register stack table cell(s) drift from 3-decimal rounding (> 6e-4):\n  "
        + "\n  ".join(strict_table_drifts)
    )

    # Check 10: Programmatic simulation of Appendix D worked sequences (tol = 6e-4) AND chapter cross-reference parity
    app_d_mismatches: List[str] = []
    app_d_checked = 0
    ch_rendered_map: Dict[int, str] = {}
    for ch_f in chapter_files:
        m_ch = re.match(r"^(\d\d)-", ch_f.name)
        if m_ch:
            raw_ch = ch_f.read_text(encoding="utf-8")
            raw_ch = re.sub(
                r"\{\{res:([^:}]+):value\}\}",
                lambda m: str(seq_reg_data.get(m.group(1), {}).get("res", "")),
                raw_ch,
            )
            ch_rendered_map[int(m_ch.group(1))] = raw_ch.replace("{,}", "").replace(",", "")
    for line_idx, ln in enumerate(app_d.splitlines(), 1):
        s = ln.strip()
        if s.startswith("| **Ch ") and "`" in s:
            cols = [c.strip() for c in s.strip("|").split("|")]
            if len(cols) >= 4:
                ex_name, expr, seq_col, res_col = cols[0], cols[1], cols[2], cols[3]
                m_ch_num = re.search(r"\*\*Ch (\d+):", ex_name)
                ch_num = int(m_ch_num.group(1)) if m_ch_num else 0
                res_no_sub = re.sub(r"\^\{[^}]+\}|\^\d+|_\{[^}]+\}|_\d+", "", res_col)
                ch_nums = [
                    n.replace("{,}", "").replace(",", "")
                    for n in re.findall(r"[-+]?\d+(?:\{,\}\d{3}|,\d{3})*(?:\.\d+)?", res_no_sub)
                ]
                if ch_num in ch_rendered_map and ch_nums:
                    ch_txt = ch_rendered_map[ch_num]
                    missing_in_ch = [n for n in ch_nums if n not in ch_txt and n.lstrip("+-") not in ch_txt]
                    if missing_in_ch:
                        app_d_mismatches.append(
                            f"appendix-d:L{line_idx} {ex_name}: result number(s) {missing_in_ch} missing in Ch {ch_num}"
                        )
                if "EQN" in seq_col or "Transform" in seq_col:
                    continue
                sub_seqs = re.findall(r"`([^`]+)`", seq_col)
                all_sim_vals: List[float] = []
                for sub_s in sub_seqs:
                    sim = vst.RPNStackSimulator()
                    if "{{key:POLY}}" in sub_s:
                        sim.poly_mode = True
                    vst.execute_keystroke_sequence(sim, sub_s)
                    all_sim_vals.extend([sim.x, sim.y, sim.z, sim.t])
                    all_sim_vals.extend(sim.regs.values())
                if all_sim_vals:
                    app_d_checked += 1
                    res_clean = res_col.replace("{,}", "").replace(",", "").replace("\\$", "")
                    res_clean = re.sub(r"_\{[^}]+\}", "", res_clean)
                    res_clean = re.sub(r"r_[123]\s*=", "", res_clean)
                    res_clean = re.sub(r"\\sigma_[123]\s*=", "", res_clean)
                    res_clean = re.sub(r"f\([^)]+\)\s*=", "", res_clean)
                    res_clean = re.sub(r"\\hat\{y\}\([^)]+\)\s*=", "", res_clean)
                    res_clean = re.sub(r"([+-]?\d+(?:\.\d+)?)\s*\\times\s*10\^\{([+-]?\d+)\}", r"\1e\2", res_clean)
                    doc_nums = [
                        float(x)
                        for x in re.findall(r"(?<![A-Za-z0-9_])[-+]?\d+(?:\.\d+)?(?:e[-+]?\d+)?", res_clean)
                    ]
                    if doc_nums and not any(
                        abs(dn - sv) <= (6e-4 if abs(dn) < 1e6 else abs(dn) * 1e-3)
                        for dn in doc_nums
                        for sv in all_sim_vals
                    ):
                        app_d_mismatches.append(
                            f"appendix-d:L{line_idx} {ex_name}: doc={doc_nums} vs sim={[round(v, 4) for v in all_sim_vals[:4]]}"
                        )
    assert not app_d_mismatches, (
        "Gate S17 Failure: Appendix D worked sequence(s) do not match RPNStackSimulator or Chapter narrative:\n  "
        + "\n  ".join(app_d_mismatches)
    )

    # Check 11: Every Eq. X.Y and Figure X.Y reference resolves to a real equation/figure after rendering
    dangling_refs: List[str] = []
    for md_file in sorted(sc32_dir.glob("*.md")):
        rendered = book_engine.process_manual_markdown(
            md_file.read_text(encoding="utf-8"), md_file, is_sc32=True, target_format="web"
        )
        defined_figs = set(re.findall(r"!\[(Figure\s+[A-Za-z0-9.]+):", rendered))
        ref_figs = set(re.findall(r"\b(Figure\s+[A-Za-z0-9.]+)\b", rendered)) - defined_figs
        defined_eqs = set(re.findall(r"\\tag\{(Eq\.\s+[A-Za-z0-9.]+)\}", rendered))
        ref_eqs = set(re.findall(r"\b(Eq\.\s+[A-Za-z0-9.]+)\b", rendered)) - defined_eqs
        for rf in sorted(ref_figs | ref_eqs):
            dangling_refs.append(f"{md_file.name}: unresolved reference {rf!r}")
    assert not dangling_refs, (
        "Gate S17 Failure: Unresolved Eq. X.Y or Figure X.Y reference(s) in SC-32 manual:\n  "
        + "\n  ".join(dangling_refs)
    )

    # Check 12: Every {{res:ID:value}} in SC-32 matches RPNStackSimulator, 3-decimal rounding, unit-free purity, and \approx sign
    from decimal import Decimal, ROUND_HALF_UP
    res_binding_errors: List[str] = []
    for md_file in sorted(sc32_dir.glob("*.md")):
        for line_idx, ln in enumerate(md_file.read_text(encoding="utf-8").splitlines(), 1):
            for m in res_val_pat.finditer(ln):
                sid = m.group(1)
                entry = seq_reg_data.get(sid, {})
                res_s = str(entry.get("res", ""))
                x_s = str(entry.get("stack", {}).get("X", ""))
                seq_s = str(entry.get("seq", ""))
                sim = vst.RPNStackSimulator()
                vst.execute_keystroke_sequence(sim, seq_s)
                res_clean = res_s.replace(",", "").replace("\\times 10^{", "e").replace("}", "").replace(" ", "")
                m_num = re.match(r"^[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", res_clean)
                res_num = float(m_num.group(0)) if m_num else None
                try:
                    x_num = float(x_s.replace(",", ""))
                except ValueError:
                    x_num = None
                if x_num is not None and abs(sim.x - x_num) > max(1e-4, abs(sim.x) * 1e-4):
                    res_binding_errors.append(
                        f"{md_file.name}:L{line_idx} {sid}: sim.x={sim.x:.6g} != stack.X={x_num:.6g}"
                    )
                if res_num is not None and x_num is not None and abs(res_num) < 1e6 and "E" not in res_s and "times" not in res_s:
                    half_up = float(Decimal(str(x_num)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP))
                    if abs(res_num - half_up) > 1e-6 and abs(res_num - round(x_num, 3)) > 6e-4:
                        res_binding_errors.append(
                            f"{md_file.name}:L{line_idx} {sid}: 3-decimal drift res={res_s!r} vs X={x_s!r}"
                        )
                if re.search(r"[a-zA-Z]", res_s.replace("E", "").replace("\\times", "")):
                    res_binding_errors.append(f"{md_file.name}:L{line_idx} {sid}: unit string embedded in res={res_s!r}")
                prefix = ln[max(0, m.start() - 45) : m.start()]
                is_exact = (
                    res_num is not None
                    and x_num is not None
                    and abs(res_num - x_num) <= 1e-7
                    and abs(res_num - sim.x) <= 1e-7
                )
                if not is_exact and prefix.rfind("=") > prefix.rfind("\\approx"):
                    res_binding_errors.append(
                        f"{md_file.name}:L{line_idx} {sid}: rounded result res={res_s!r} (X={x_s!r}) preceded by '=' instead of '\\approx'"
                    )
    assert not res_binding_errors, (
        "Gate S17 Failure: SC-32 {{res:ID:value}} binding/rounding/approximation error(s):\n  "
        + "\n  ".join(res_binding_errors)
    )

    # Check 13: Hardware shift-direction and host-key claims across SC-32 match Appendix C 43-key directory
    import unicodedata
    hw_key_map: Dict[str, Tuple[str, str]] = {}
    for ln in app_c.splitlines():
        m_hw = re.match(r"^\|\s*\*\*(\d+)\*\*\s*\|\s*`?R\d+,\s*C[\d-]+`?\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|", ln)
        if m_hw:
            prim_m = re.search(r"\{\{key(?:cap)?:([^}]+)\}\}", m_hw.group(2))
            prim = unicodedata.normalize("NFC", prim_m.group(1) if prim_m else m_hw.group(2).strip().strip("`*"))
            l_m = re.search(r"\{\{key(?:cap)?:([^}]+)\}\}", m_hw.group(3)) or re.search(r"`([^`]+)`", m_hw.group(3))
            r_m = re.search(r"\{\{key(?:cap)?:([^}]+)\}\}", m_hw.group(4)) or re.search(r"`([^`]+)`", m_hw.group(4))
            hw_key_map[prim] = (
                unicodedata.normalize("NFC", l_m.group(1) if l_m else ""),
                unicodedata.normalize("NFC", r_m.group(1) if r_m else ""),
            )
    assert len(hw_key_map) == 43, f"Gate S17 Failure: Expected 43 keys in hw_key_map, found {len(hw_key_map)}"
    shift_claim_errors: List[str] = []
    shift_claim_pats = [
        re.compile(
            r"`\{\{key(?:cap)?:([^}]+)\}\}`\s*\((?:the\s+)?(left|right)-shifted(?:\s+function|\s+partner|\s+counterpart)?\s+on\s+(?:the\s+)?`\{\{key(?:cap)?:([^}]+)\}\}`",
            re.IGNORECASE,
        ),
        re.compile(
            r"`\{\{key(?:cap)?:([^}]+)\}\}`\s+on\s+(Left|Right)[\s-]Shift(?:\s+`\{\{key:[↰↱]\}\}`)?\s+`\{\{key(?:cap)?:([^}]+)\}\}`",
            re.IGNORECASE,
        ),
    ]
    for md_file in sorted(sc32_dir.glob("*.md")):
        for line_idx, ln in enumerate(md_file.read_text(encoding="utf-8").splitlines(), 1):
            for pat in shift_claim_pats:
                for m_sc in pat.finditer(ln):
                    fn = unicodedata.normalize("NFC", m_sc.group(1))
                    side = m_sc.group(2).lower()
                    host = unicodedata.normalize("NFC", m_sc.group(3))
                    if host in hw_key_map:
                        actual_l, actual_r = hw_key_map[host]
                        expected_fn = actual_l if side == "left" else actual_r
                        if expected_fn != fn:
                            shift_claim_errors.append(
                                f"{md_file.name}:L{line_idx} claims {fn!r} is {side}-shifted on {host!r}, "
                                f"but Appendix C has left={actual_l!r}, right={actual_r!r}"
                            )
            m_menu_row = re.match(
                r"^\|\s*\*\*`([^`]+)`\*\*\s*\|\s*`\{\{key:([↰↱])\}\}`\s*\+\s*`\{\{key:([^}]+)\}\}`\s*\|",
                ln,
            )
            if m_menu_row:
                fn = unicodedata.normalize("NFC", m_menu_row.group(1))
                arrow = m_menu_row.group(2)
                host = unicodedata.normalize("NFC", m_menu_row.group(3))
                if host in hw_key_map:
                    actual_l, actual_r = hw_key_map[host]
                    expected_fn = actual_l if arrow == "↰" else actual_r
                    if expected_fn != fn:
                        shift_claim_errors.append(
                            f"{md_file.name}:L{line_idx} menu table claims {fn!r} is {arrow} on {host!r}, "
                            f"but Appendix C 43-key table has left={actual_l!r}, right={actual_r!r}"
                        )
    assert not shift_claim_errors, (
        "Gate S17 Failure: SC-32 prose shift/host-key claim mismatch against Appendix C:\n  "
        + "\n  ".join(shift_claim_errors)
    )

    # Check 14: Zero unapproved 4+ decimal floating-point numbers across index.md and Chapters 01..14
    allowed_4dec = {
        "0.0025", "0.0022", "0.0000006328", "0.3048", "0.00225", "0.0048", "0.0182", "0.0134", "0.0118",
        "0.0301", "14.6875", "0.6875", "35.1536", "1.0003", "42.1836", "2.2236", "0.0185", "0.0016",
        "7.2436", "1.0825", "0.0425",
    }
    literal_4dec_violations: List[str] = []
    for md_file in [sc32_dir / "index.md", *chapter_files]:
        for line_idx, ln in enumerate(md_file.read_text(encoding="utf-8").splitlines(), 1):
            for m_4d in re.finditer(r"(?<![A-Za-z0-9_])(\d+\.\d{4,})(?![A-Za-z0-9_])", ln):
                num_tok = m_4d.group(1)
                if num_tok not in allowed_4dec:
                    literal_4dec_violations.append(f"{md_file.name}:L{line_idx} -> {num_tok!r}")
    assert not literal_4dec_violations, (
        "Gate S17 Failure: Unapproved 4+ decimal number(s) in SC-32 narrative chapters:\n  "
        + "\n  ".join(literal_4dec_violations)
    )

    # Check 15: Zero dangling Section X.Y refs, broken relative links/anchors, or unbalanced LaTeX delimiters
    def _slugify_heading(heading: str) -> str:
        h = re.sub(r"`([^`]+)`", r"\1", heading)
        h = re.sub(r"\$([^$]+)\$", r"\1", h)
        h = re.sub(r"[*_~]", "", h).strip().lower()
        h = re.sub(r"[^\w\s-]", "", h)
        return re.sub(r"[\s]+", "-", h)

    sc32_heading_slugs: Dict[str, set] = {}
    for md_file in sorted(sc32_dir.glob("*.md")):
        slugs = set()
        for ln in md_file.read_text(encoding="utf-8").splitlines():
            m_hd = re.match(r"^(#{1,6})\s+(.+)$", ln.strip())
            if m_hd:
                slugs.add(_slugify_heading(m_hd.group(2)))
        sc32_heading_slugs[md_file.name] = slugs

    structural_latex_errors: List[str] = []
    for md_file in sorted(sc32_dir.glob("*.md")):
        raw_txt = md_file.read_text(encoding="utf-8")
        for dm in re.finditer(r"\$\$(.*?)\$\$", raw_txt, re.DOTALL):
            body = dm.group(1)
            lineno = raw_txt[: dm.start()].count("\n") + 1
            b_clean = body.replace(r"\{", "").replace(r"\}", "")
            if b_clean.count("{") != b_clean.count("}"):
                structural_latex_errors.append(f"{md_file.name}:L{lineno} unbalanced braces in $$...$$")
            if len(re.findall(r"\\left\b", body)) != len(re.findall(r"\\right\b", body)):
                structural_latex_errors.append(f"{md_file.name}:L{lineno} unbalanced \\left/\\right in $$...$$")
        for line_idx, ln in enumerate(raw_txt.splitlines(), 1):
            if re.search(r"\bSections?\s+\d+\.\d+", ln):
                structural_latex_errors.append(f"{md_file.name}:L{line_idx} dangling numbered Section X.Y reference")
            for m_lnk in re.finditer(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)", ln):
                url = m_lnk.group(2)
                if url.startswith(("http://", "https://", "mailto:")):
                    continue
                parts = url.split("#", 1)
                t_file, anchor = parts[0], (parts[1] if len(parts) > 1 else None)
                if t_file:
                    t_base = Path(t_file).name
                    if not t_base.endswith(".md"):
                        t_base += ".md"
                    if t_base not in sc32_heading_slugs:
                        structural_latex_errors.append(f"{md_file.name}:L{line_idx} broken file link {url!r}")
                    elif anchor and anchor not in sc32_heading_slugs[t_base]:
                        structural_latex_errors.append(f"{md_file.name}:L{line_idx} broken anchor link {url!r}")
                elif anchor and anchor not in sc32_heading_slugs[md_file.name]:
                    structural_latex_errors.append(f"{md_file.name}:L{line_idx} broken self-anchor #{anchor}")
            ln_no_code = re.sub(r"`[^`]+`", "", re.sub(r"\$\$.*?\$\$", "", ln))
            if len(re.findall(r"(?<!\\)\$", ln_no_code)) % 2 != 0:
                structural_latex_errors.append(f"{md_file.name}:L{line_idx} odd unescaped '$' delimiter count")
            for im in re.finditer(r"(?<!\\)\$((?:\\.|[^$])+)(?<!\\)\$", ln_no_code):
                ib = im.group(1)
                ib_clean = ib.replace(r"\{", "").replace(r"\}", "")
                if ib_clean.count("{") != ib_clean.count("}"):
                    structural_latex_errors.append(f"{md_file.name}:L{line_idx} unbalanced braces in ${ib}$")
                if len(re.findall(r"\\left\b", ib)) != len(re.findall(r"\\right\b", ib)):
                    structural_latex_errors.append(f"{md_file.name}:L{line_idx} unbalanced \\left/\\right in ${ib}$")
    assert not structural_latex_errors, (
        "Gate S17 Failure: SC-32 structural link/section/LaTeX delimiter error(s):\n  "
        + "\n  ".join(structural_latex_errors)
    )

    # Check 16: Zero RCL <digit> sequences, index.md Chapter H1 title parity, and prose paragraph word-count ceiling (<= 220 words)
    check16_errors: List[str] = []
    for md_file in sorted(sc32_dir.glob("*.md")):
        raw_txt = md_file.read_text(encoding="utf-8")
        for line_idx, ln in enumerate(raw_txt.splitlines(), 1):
            if re.search(r"\{\{key(?:cap)?:RCL\}\}\s*`?\s*\d\b", ln):
                check16_errors.append(
                    f"{md_file.name}:L{line_idx} invalid '{{{{key:RCL}}}} <digit>' sequence (RCL activates Alpha mode A-Z/(i) on SC-32)"
                )

    idx_txt = (sc32_dir / "index.md").read_text(encoding="utf-8")
    idx_titles: Dict[str, str] = {}
    for m_row in re.finditer(
        r"\|\s*\*\*\[Chapter\s+\d+\]\(([^)]+)\)\*\*\s*\|\s*\*\*([^*]+)\*\*\s*\|",
        idx_txt,
    ):
        idx_titles[m_row.group(1).strip()] = m_row.group(2).strip()

    for ch_file in chapter_files:
        ch_txt = ch_file.read_text(encoding="utf-8")
        m_h1 = re.search(r"^#\s+Chapter\s+\d+:\s+(.+)$", ch_txt, re.MULTILINE)
        assert m_h1, f"Gate S17 Failure: Missing '# Chapter N: <Title>' in {ch_file.name}"
        h1_title = m_h1.group(1).strip()
        if ch_file.name not in idx_titles:
            check16_errors.append(f"index.md missing Organization table row for {ch_file.name}")
        elif idx_titles[ch_file.name] != h1_title:
            check16_errors.append(
                f"index.md title mismatch for {ch_file.name}: table has {idx_titles[ch_file.name]!r} vs H1 {h1_title!r}"
            )
        if "### Try It on the Stack" not in ch_txt:
            check16_errors.append(f"{ch_file.name} missing '### Try It on the Stack' end-of-chapter practice block")
        else:
            try_block = ch_txt.split("### Try It on the Stack", 1)[1]
            for prob_idx in (1, 2, 3):
                if not re.search(rf"^{prob_idx}\.\s+\*\*", try_block, re.MULTILINE):
                    check16_errors.append(f"{ch_file.name} '### Try It on the Stack' missing problem #{prob_idx}")
        ch_lines = ch_txt.splitlines()
        h2_indices = [idx for idx, line in enumerate(ch_lines) if line.startswith("## ")]
        n3_start = h2_indices[-1] if h2_indices else 0
        for idx, line in enumerate(ch_lines[:n3_start], 1):
            if ":screenshot" in line:
                check16_errors.append(
                    f"{ch_file.name}:L{idx} calculator UI screenshot macro found in Section N.1/N.2 (must reside in Section N.3)"
                )

    seen_screenshots: Dict[str, str] = {}
    for md_file in sorted(sc32_dir.glob("*.md")):
        for line_idx, ln in enumerate(md_file.read_text(encoding="utf-8").splitlines(), 1):
            for m_resval in re.finditer(r"\{\{res:([^:}]+):value\}\}", ln):
                check16_errors.append(
                    f"{md_file.name}:L{line_idx} unexpanded {{res:{m_resval.group(1)}:value}} macro found (replace with verified <=3-decimal literal)"
                )
            for m_shot in re.finditer(r"\{\{res:([^:}]+):screenshot", ln):
                shot_id = m_shot.group(1).strip()
                if "plot_" in shot_id:
                    check16_errors.append(f"{md_file.name}:L{line_idx} non-hardware plot screenshot {shot_id!r} used in SC-32 manual")
                if shot_id in seen_screenshots:
                    check16_errors.append(
                        f"{md_file.name}:L{line_idx} duplicate screenshot {shot_id!r} (already used in {seen_screenshots[shot_id]})"
                    )
                else:
                    seen_screenshots[shot_id] = f"{md_file.name}:L{line_idx}"

    for req_menu in (
        "DISP", "MODES", "BASE", "CLEAR", "FLAGS", "STACK", "PARTS", "PROB",
        "SUMS", "x̄,ȳ", "s,σ", "L.R.", "x?y", "x?0", "POLY", "TVM",
        "EQN", "SOLVE", "∫", "PLOT", "REGS", "MEM",
    ):
        if f"| **`{req_menu}`**" not in unicodedata.normalize("NFC", app_c):
            check16_errors.append(f"appendix-c-keycap-directory.md missing softkey menu row for {req_menu!r}")

    for p_file in [sc32_dir / "index.md"] + chapter_files:
        in_fm = False
        p_txt = p_file.read_text(encoding="utf-8")
        web_rendered = process_manual_markdown(p_txt, p_file, is_sc32=True, target_format="web")
        if re.search(r"\\(?:mathtt|texttt)\{\[[^\n]*\\tag\{Eq\.", web_rendered):
            check16_errors.append(f"{p_file.name}: softkey ribbon diagram erroneously tagged as an equation")
        valid_eq_tags = set(re.findall(r"\\tag\{(Eq\.\s*[0-9A-Z]+\.\d+)\}", web_rendered))
        for m_eqref in re.finditer(r"\b(Eq\.\s*[0-9A-Z]+\.\d+)\b", p_txt):
            ref_str = re.sub(r"\s+", " ", m_eqref.group(1).strip())
            if ref_str not in valid_eq_tags:
                check16_errors.append(
                    f"{p_file.name}: equation reference {ref_str!r} does not match any numbered equation in chapter (max/valid: {sorted(valid_eq_tags)[-3:] if valid_eq_tags else 'none'})"
                )
        for line_idx, ln in enumerate(p_txt.splitlines(), 1):
            s = ln.strip()
            if line_idx == 1 and s == "---":
                in_fm = True
                continue
            if in_fm:
                if s == "---":
                    in_fm = False
                continue
            if not s or s.startswith(("#", "|", "!", ">", "-", "*", "$$", "{{", "```")):
                continue
            wc = len(s.split())
            if wc > 220:
                check16_errors.append(
                    f"{p_file.name}:L{line_idx} prose paragraph exceeds 220-word ceiling ({wc} words)"
                )

    pdf_gen_path = REPO_ROOT / "Tools" / "generate_manual_pdfs.py"
    if pdf_gen_path.exists():
        pdf_gen_txt = pdf_gen_path.read_text(encoding="utf-8")
        for bad_tok in ("<b>STAT</b>", "<b>CONST</b>", "<b>CONV</b>", "<b>↖</b>", "<b>↗</b>"):
            if bad_tok in pdf_gen_txt:
                check16_errors.append(f"generate_manual_pdfs.py contains obsolete/phantom SC-32 frontispiece token {bad_tok!r}")

    assert not check16_errors, (
        "Gate S17 Failure: SC-32 Check 16 (RCL grammar, index title parity, or paragraph length) error(s):\n  "
        + "\n  ".join(check16_errors)
    )

    return {
        "chapters_checked": len(chapter_files),
        "stack_tables": total_stack_tables,
        "screenshots": total_screenshots,
        "appendix_d_verified": app_d_checked,
    }


def export_curriculum_uil_registry() -> None:
    """Export all 650 UIL competition problems and 452 curriculum items to curriculum_uil_registry.json."""
    import json
    edu_tools = (
        REPO_ROOT / "Education" / "tools"
        if (REPO_ROOT / "Education" / "tools").exists()
        else REPO_ROOT.parent / "watch-calc-32" / "Education" / "tools"
    )
    if not edu_tools.exists():
        return
    if str(edu_tools) not in sys.path:
        sys.path.insert(0, str(edu_tools))
    from catalogs import uil_tests, singapore, bridges, bigideas

    def _tokens_to_macro_seq(tokens: List[str]) -> str:
        out: List[str] = []
        num_buf = ""
        for i, tok in enumerate(tokens):
            t = tok.strip()
            if not t:
                continue
            prev = tokens[i - 1].strip() if i > 0 else ""
            if prev in ("STO", "RCL"):
                if num_buf:
                    out.append(num_buf)
                    num_buf = ""
                out.append(f"{{{{key:{t}}}}}")
                continue
            if re.match(r"^[\d.]+$", t):
                num_buf += t
            elif re.match(r"^[0-9A-Fa-f]{2}$", t) and any(x in tokens[:i] for x in ("HEX",)):
                if num_buf:
                    out.append(num_buf)
                    num_buf = ""
                out.append(t)
            else:
                if num_buf:
                    out.append(num_buf)
                    num_buf = ""
                out.append(f"{{{{key:{t}}}}}")
        if num_buf:
            out.append(num_buf)
        return " ".join(out)

    def _parse_ans_to_float(ans_str: str) -> float:
        s = ans_str.strip()
        m_hex = re.search(r"0x([0-9A-Fa-f]+)", s)
        if m_hex:
            return float(int(m_hex.group(1), 16))
        m_clk = re.match(r"^(\d+):(\d{2})\b", s)
        if m_clk:
            return float(f"{m_clk.group(1)}.{m_clk.group(2)}")
        m_rem = re.search(r"(\d+)\s*(?:,?\s*R(?:emainder)?\s*|:?\s*R\s*)(\d+)", s, re.IGNORECASE)
        if m_rem:
            return float(m_rem.group(1))
        m_mix = re.match(r"^(-?\d+)\s+(\d+)/(\d+)\b", s)
        if m_mix:
            w, n, d = int(m_mix.group(1)), int(m_mix.group(2)), int(m_mix.group(3))
            return float(w) + (float(n) / float(d) if w >= 0 else -float(n) / float(d))
        m_frac = re.match(r"^(-?\d+)/(\d+)\b", s)
        if m_frac:
            return float(m_frac.group(1)) / float(m_frac.group(2))
        s_clean = re.sub(r"\bx[12]\s*=", "=", s)
        s_clean = re.sub(r"(\d),(\d{3})", r"\1\2", s_clean)
        m_num = re.search(r"(-?\d+(?:\.\d+)?)", s_clean)
        if m_num:
            return float(m_num.group(1))
        return 0.0

    registry = {}
    for tid, test in uil_tests.ALL_UIL_TESTS.items():
        model = "sc6" if tid in ("SC6-G3", "SC6-G4", "SC6-G5", "SC6-G6") else "sc32"
        for p in test.problems:
            item_id = f"uil_{tid}_{p.num}"
            registry[item_id] = {
                "kind": "uil",
                "model": model,
                "seq": _tokens_to_macro_seq(p.rpn_keys),
                "expected": p.val,
                "is_int": p.is_int,
                "label": p.label,
                "prompt": p.expression,
            }

    all_ch = singapore.SINGAPORE_DIMENSIONS_CATALOG + bridges.BRIDGES_CATALOG + bigideas.BIG_IDEAS_CATALOG
    for c_idx, ch in enumerate(all_ch, 1):
        model = "sc6" if "SC-6" in ch.calculator_model else "sc32"
        ex_id = f"curr_ch{c_idx:02d}_exemplar"
        registry[ex_id] = {
            "kind": "exemplar",
            "model": model,
            "seq": _tokens_to_macro_seq(ch.exemplar_keystrokes),
            "expected": _parse_ans_to_float(ch.exemplar_answer),
            "ans_str": ch.exemplar_answer,
            "prompt": f"{ch.curriculum} {ch.grade_level} {ch.chapter_number}: {ch.exemplar_prompt}",
        }
        for p_idx, w in enumerate(ch.sample_problems, 1):
            raw_toks = re.findall(r"\[([^\[\]]+)\]", w["keys"])
            w_id = f"curr_ch{c_idx:02d}_A{p_idx}"
            wp = w["prompt"]
            registry[w_id] = {
                "kind": "worksheet",
                "model": model,
                "seq": _tokens_to_macro_seq(raw_toks),
                "expected": _parse_ans_to_float(w["ans"]),
                "ans_str": w["ans"],
                "prompt": f"{ch.curriculum} {ch.grade_level} {ch.chapter_number} A{p_idx}: {wp}",
            }
        for p_idx, w in enumerate(ch.sample_problems_form_b, 1):
            raw_toks = re.findall(r"\[([^\[\]]+)\]", w["keys"])
            w_id = f"curr_ch{c_idx:02d}_B{p_idx}"
            wp = w["prompt"]
            registry[w_id] = {
                "kind": "worksheet",
                "model": model,
                "seq": _tokens_to_macro_seq(raw_toks),
                "expected": _parse_ans_to_float(w["ans"]),
                "ans_str": w["ans"],
                "prompt": f"{ch.curriculum} {ch.grade_level} {ch.chapter_number} B{p_idx}: {wp}",
            }

    out_path = ASSETS_MANUALS_DIR / "curriculum_uil_registry.json"
    out_path.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    process_all_files()

