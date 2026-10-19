#!/usr/bin/env python3
r"""
Comprehensive Forensic PDF Audit Script for StackCalc Manuals.

Audits compiled publication PDFs:
  - docs/downloads/manuals/sc6-elementary-manual.pdf
  - docs/downloads/manuals/sc32-scientific-manual.pdf

Verifies:
  1. Minimum page count: >= 300 pages each.
  2. Zero reader-facing contest acronyms: \b(UIL|TMSCA|PSIA)\b.
  3. Zero raw LaTeX math leaks ($...$, \mathbf, \frac, \sqrt, etc.).
  4. Zero test or internal harness leaks (testSC*, .swift, "automated verification suite").
  5. Zero prohibited hardware silicon/display part numbers (RP2350, ST7567A).
  6. Zero SEC CLASS headers.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import pypdf

REPO_ROOT = Path(__file__).resolve().parent.parent
WATCH_CALC_ROOT = REPO_ROOT if (REPO_ROOT / "documentation" / "manuals").exists() else (REPO_ROOT.parent / "watch-calc-32")
MANUALS_DIR = (
    WATCH_CALC_ROOT / "documentation" / "manuals" / "output"
    if (WATCH_CALC_ROOT / "documentation" / "manuals" / "output").exists()
    else (REPO_ROOT / "docs" / "downloads" / "manuals")
)

TARGET_PDFS = [
    "sc6-elementary-manual.pdf",
    "sc32-scientific-manual.pdf",
]

# Prohibited regexes and descriptions
AUDIT_RULES: List[Tuple[str, re.Pattern, str]] = [
    (
        "CONTEST_ACRONYMS",
        re.compile(r"\b(UIL|TMSCA|PSIA)\b"),
        "Reader-facing contest acronym (UIL, TMSCA, PSIA)",
    ),
    (
        "LATEX_COMMANDS",
        re.compile(r"\\[a-zA-Z]+"),
        "Raw LaTeX backslash command (e.g. \\mathbf, \\frac, \\sqrt)",
    ),
    (
        "LATEX_NAKED_MACROS",
        re.compile(r"\b(?:mathbf|boldsymbol|mathrm|operatorname)\b"),
        "Naked LaTeX macro without backslash (e.g. mathbf, boldsymbol)",
    ),
    (
        "LATEX_INLINE_MATH",
        re.compile(r"(?<!\\)\$(?:[a-zA-Z\\]|\s+[a-zA-Z\\])[^\$\n]*\$"),
        "Raw inline LaTeX math delimiter ($...$ with math tokens)",
    ),
    (
        "LATEX_DISPLAY_MATH",
        re.compile(r"\$\$[^\$]+\$\$"),
        "Raw display LaTeX math delimiter ($$...$$)",
    ),
    (
        "TEST_IDENTIFIERS",
        re.compile(r"\b(?:testSC\w*|testComplex\w*|testEuler\w*)\b|\.swift\b"),
        "Test harness or Swift source identifier",
    ),
    (
        "HARNESS_PHRASES",
        re.compile(r"the automated verification suite", re.IGNORECASE),
        "Internal test suite phrasing",
    ),
    (
        "PROHIBITED_SILICON",
        re.compile(r"\bRP2350\b"),
        "Prohibited silicon part number RP2350",
    ),
    (
        "PROHIBITED_LCD",
        re.compile(r"\bST7567A\b"),
        "Prohibited LCD controller part number ST7567A",
    ),
    (
        "SEC_CLASS_HEADERS",
        re.compile(r"\bSEC CLASS\b", re.IGNORECASE),
        "Security classification header tag",
    ),
    (
        "UNEXPANDED_MACROS",
        re.compile(r"\{\{[a-zA-Z_]+:[^\}]+\}\}"),
        "Unexpanded book_engine macro (e.g. {{key:...}}, {{res:...}}, {{blocks:...}})",
    ),
    (
        "LEAKED_FILE_URIS",
        re.compile(r"file:///"),
        "Leaked local filesystem URI (file:///)",
    ),
    (
        "RAW_HTML_TAGS",
        re.compile(r"</?(?:div|span|p|br|strong|em|ul|li|table|tr|td)\b[^>]*>"),
        "Unparsed raw HTML tag in PDF text",
    ),
    (
        "UNPARSED_MD_BOLD",
        re.compile(r"\*\*[^\*]+\*\*"),
        "Unparsed Markdown bold syntax (**...**)",
    ),
    (
        "UNPARSED_MD_LINKS",
        re.compile(r"\]\([^\)\s]+\.md[^\)]*\)"),
        "Unparsed Markdown link syntax ([...](....md))",
    ),
    (
        "EXPLICIT_CRA_SCAFFOLDING",
        re.compile(r"\b(?:CRA Pedagogical|Concrete-Representational-Abstract|Concrete Level|Representational Level|Abstract Level|Homeschooler Diagnostic Checkpoint)\b", re.IGNORECASE),
        "Explicit pedagogical scaffolding label instead of integrated narrative",
    ),
    (
        "SWALLOWED_HRULE",
        re.compile(r"[.!?\"”)]\s+---\s*(?:\n|$)"),
        "Swallowed markdown horizontal rule (---) at end of paragraph",
    ),
]


def audit_pdf(pdf_path: Path) -> Tuple[bool, Dict[str, any]]:
    if not pdf_path.exists():
        return False, {"error": f"File not found: {pdf_path}"}

    reader = pypdf.PdfReader(str(pdf_path))
    num_pages = len(reader.pages)

    stats = {
        "file": pdf_path.name,
        "pages": num_pages,
        "total_chars": 0,
        "violations": [],
    }

    page_fail = num_pages < 300
    if page_fail:
        stats["violations"].append(
            f"Page count violation: {num_pages} pages (expected >= 300)"
        )

    for page_idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        stats["total_chars"] += len(text)

        for rule_id, pattern, desc in AUDIT_RULES:
            matches = pattern.findall(text)
            if matches:
                # Deduplicate samples
                samples = list(dict.fromkeys(matches))[:5]
                stats["violations"].append(
                    f"Page {page_idx + 1}: [{rule_id}] {desc} -> {samples}"
                )

    passed = len(stats["violations"]) == 0
    return passed, stats


def main() -> int:
    print("=" * 70)
    print("StackCalc PDF Forensic Audit Suite")
    print("=" * 70)

    overall_pass = True

    for pdf_name in TARGET_PDFS:
        pdf_path = MANUALS_DIR / pdf_name
        passed, stats = audit_pdf(pdf_path)

        print(f"\nAuditing: {pdf_name}")
        if "error" in stats:
            print(f"  ❌ ERROR: {stats['error']}")
            overall_pass = False
            continue

        print(f"  Page Count:  {stats['pages']} (Threshold: >= 300)")
        print(f"  Total Chars: {stats['total_chars']:,}")

        if passed:
            print("  Status:      ✅ PASS (0 violations across all pages)")
        else:
            print(f"  Status:      ❌ FAIL ({len(stats['violations'])} violations found)")
            for violation in stats["violations"][:20]:
                print(f"    - {violation}")
            if len(stats["violations"]) > 20:
                print(f"    ... and {len(stats['violations']) - 20} more violations.")
            overall_pass = False

    print("\n" + "=" * 70)
    if overall_pass:
        print("ALL PDF FORENSIC AUDIT CHECKS PASSED: 100% CLEAN & >= 300 PAGES EACH")
        print("=" * 70)
        return 0
    else:
        print("PDF FORENSIC AUDIT FAILED")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    sys.exit(main())
