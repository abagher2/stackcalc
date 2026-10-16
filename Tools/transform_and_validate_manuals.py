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
from typing import List, Set, Tuple

TOOLS_DIR = Path(__file__).resolve().parent
REPO_ROOT = TOOLS_DIR.parent
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
    if get_chapter_prefix(file_path) is None:
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
    Adds a concise note in Chapter 1 of both manuals explaining that key and shift
    accent colors vary depending on the faceplate theme, so shifts are referenced
    as Left Shift `{{key:↰}}` and Right Shift `{{key:↱}}` on SC-32, and `{{key:f}}`
    and `{{key:g}}` on SC-6.
    """
    marker = "Faceplate Themes & Shift Legend Conventions"
    if marker in text:
        return text

    # Skip past YAML frontmatter if present
    m_fm = re.match(r"^(---\n.*?\n---\n)", text, flags=re.DOTALL)
    fm_end = m_fm.end() if m_fm else 0

    if is_sc32 and file_path.name == "01-craftsmanship-hardware.md":
        note = (
            "\n> [!NOTE]\n"
            "> **Faceplate Themes & Shift Legend Conventions:**  \n"
            "> Because both the physical StackCalc SC-32 faceplate editions and the companion software app support multiple interchangeable faceplate themes (`Pure Black`, `Retro Futurism`, `Pioneer Brown`, `Pioneer Black`, `Stealth`, `Supernova`, `Deep Space`, `Voyager`, `Synthwave`, and `Arcade`), shift accent colors adapt dynamically to the active faceplate palette. Throughout this manual, shifted functions are referenced independent of color using the hardware directional shift symbols: **Left Shift `{{key:↰}}`** (Row 5, Col 0) and **Right Shift `{{key:↱}}`** (Row 6, Col 0).\n"
        )
        idx = text.find("\n---\n", fm_end)
        if idx != -1:
            return text[:idx] + note + text[idx:]

    if not is_sc32 and file_path.name == "01-hardware-architecture.md":
        note = (
            "\n> [!NOTE]\n"
            "> **Faceplate Themes & Shift Legend Conventions:**  \n"
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

            if img_name.endswith(".png") and (REPO_ROOT / "docs" / "assets" / "manuals" / "screenshots" / img_name).exists():
                shot_id = img_name[:-4]
                out_lines.append(f"{{{{res:{shot_id}:screenshot|{clean_caption}}}}}")
                continue

        out_lines.append(line)

    return "\n".join(out_lines)


def sync_consolidated_user_guides() -> None:
    """
    Synchronizes the single-page web manuals (`docs/manuals/sc32-user-guide.md` and
    `docs/manuals/sc6-user-guide.md`) directly from the rendered chapter files so
    they never drift from the chapter sources.
    """
    for is_sc32 in (True, False):
        sub = "sc32" if is_sc32 else "sc6"
        guide_name = "sc32-user-guide.md" if is_sc32 else "sc6-user-guide.md"
        guide_path = REPO_ROOT / "docs" / "manuals" / guide_name
        if not guide_path.exists():
            continue

        orig_guide = guide_path.read_text(encoding="utf-8")
        # Preserve frontmatter and header banner up to first `---`
        m_fm = re.match(r"^(---\n.*?\n---\n.*?---\n)", orig_guide, flags=re.DOTALL)
        header = m_fm.group(1) if m_fm else ""

        chapter_files = sorted((REPO_ROOT / "docs" / "manuals" / sub).glob("*.md"))
        ordered = [p for p in chapter_files if p.name == "index.md"] + [
            p for p in chapter_files if p.name != "index.md"
        ]
        parts = [header]
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

        guide_path.write_text("\n\n---\n\n".join(parts) + "\n", encoding="utf-8")


def process_all_files() -> None:
    manual_files: List[Tuple[Path, bool]] = []
    for p in sorted((REPO_ROOT / "docs" / "manuals" / "sc32").glob("*.md")):
        manual_files.append((p, True))
    for p in sorted((REPO_ROOT / "docs" / "manuals" / "sc6").glob("*.md")):
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
    seq_reg_path = REPO_ROOT / "docs" / "assets" / "manuals" / "sequences_registry.json"
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
    citations_reg_path = REPO_ROOT / "docs" / "assets" / "manuals" / "citations_registry.json"
    assert citations_reg_path.exists(), f"Missing {citations_reg_path}"
    citations_reg_data = json.loads(citations_reg_path.read_text(encoding="utf-8"))
    assert len(citations_reg_data) >= 30, f"Expected >= 30 citations in citations_registry.json, found {len(citations_reg_data)}"
    for cid, c_entry in citations_reg_data.items():
        assert c_entry.get("author"), f"Missing author in citations_registry.json[{cid}]"
        assert c_entry.get("year"), f"Missing year in citations_registry.json[{cid}]"
        assert c_entry.get("title"), f"Missing title in citations_registry.json[{cid}]"
        assert c_entry.get("annotation"), f"Missing annotation in citations_registry.json[{cid}]"
        assert c_entry.get("volume_scope") in ("sc32", "sc6", "both"), f"Invalid volume_scope in citations_registry.json[{cid}]"

    # 5. Validate website curriculum, tutorial, and learning-lab pages
    curriculum_pages = [
        REPO_ROOT / "docs" / "learning-lab.md",
        REPO_ROOT / "docs" / "tutorials.md",
        *sorted((REPO_ROOT / "docs" / "curriculum").glob("*.md")),
    ]
    for cpath in curriculum_pages:
        ctxt = cpath.read_text(encoding="utf-8")
        crendered = expand_key_macros(ctxt, is_sc32=("elementary" not in cpath.name), file_path=cpath)
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
    assert stack_stats["tables_checked"] >= 1000, f"Expected >= 1,000 4-register tables in Gate S10, found {stack_stats['tables_checked']}"

    print(f"✅ Transformed and validated {len(manual_files)} manual chapter/appendix files + {len(curriculum_pages)} curriculum pages + 2 consolidated guides.")
    print(f"   - Validated {{key:...}} / {{keycap:...}} macros: {total_key_macros:,}")
    print(f"   - Validated {{res:ID:keys}} & {{res:ID:value}}:  {total_seq_macros:,} sequences / {total_res_macros:,} results ({len(seq_reg_data):,} registered in sequences_registry.json)")
    print(f"   - Validated {{res:ID:screenshot}} macros:        {total_screenshot_macros:,}")
    print(f"   - Validated {{blocks:...}} macros:               {total_blocks_macros:,}")
    print(f"   - Validated {{cite:...}} macros:                 {total_cite_macros:,} citations / {total_bib_macros:,} bibliographies ({len(citations_reg_data):,} registered in citations_registry.json)")
    disc_msg = "100% PASS" if stack_stats["table_discrepancies"] == 0 else f"{stack_stats['table_discrepancies']} discrepancies tracked"
    print(f"   - Gate S10 Stack Verification:                   {stack_stats['tables_checked']:,} tables / {stack_stats['traces_checked']:,} inline traces audited ({disc_msg})")
    print("   - Zero ASCII boxes, zero dummy tables, zero placeholder results, zero double-shifts, zero monadic-ENTER bugs: 100% PASS")
    print("   - Code fence parity, inline backtick parity, and section numbering uniqueness: 100% PASS")


def export_curriculum_uil_registry() -> None:
    """Export all 650 UIL competition problems and 452 curriculum items to curriculum_uil_registry.json."""
    import json
    edu_tools = REPO_ROOT.parent / "watch-calc-32" / "Education" / "tools"
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

    out_path = REPO_ROOT / "docs" / "assets" / "manuals" / "curriculum_uil_registry.json"
    out_path.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    process_all_files()

