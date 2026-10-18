#!/usr/bin/env python3
"""
Authoritative Keystroke Macro & Section Auto-Numbering Engine for StackCalc Manuals.

Reads key layouts and menus directly from the app-exported JSON files:
  - docs/assets/manuals/layout_data.json     (StackCalc SC-32 Scientific)
  - docs/assets/manuals/layout_data_sc6.json (StackCalc SC-6 Elementary)

Provides:
  1. Programmatic validation and expansion of `{{key:NAME}}` and `{{keycap:NAME}}`
     macros into exact hardware shift + keycap sequences (`[LABEL]`, `[f] [LABEL]`,
     or `[g] [LABEL]`).
  2. Deterministic auto-numbering of `##` and `###` section headings across all
     chapters and appendices, plus automatic cross-reference anchor synchronization.
"""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
MANUALS_ASSETS_DIR = DOCS_DIR / "assets" / "manuals"

SC32_JSON_PATH = MANUALS_ASSETS_DIR / "layout_data.json"
SC6_JSON_PATH = MANUALS_ASSETS_DIR / "layout_data_sc6.json"


def normalize_key_token(raw: str) -> str:
    """
    Normalizes Unicode math italic glyphs and arrow variants to canonical ASCII/Unicode
    forms used in textbook prose while preserving mathematical symbols (π, √, ∫, Σ, ⇄, ∥).
    """
    s = raw.strip()
    replacements = {
        "𝑥": "x",
        "𝑦": "y",
        "𝑒": "e",
        "−": "-",
        "–": "-",
        "—": "-",
        "x⁻¹": "1/x",
        "𝑥⁻¹": "1/x",
        "LASTx": "LASTX",
        "LAST𝑥": "LASTX",
        "LAST X": "LASTX",
        "LAST x": "LASTX",
        "x<>y": "x⇄y",
        "x↔y": "x⇄y",
        "x≶y": "x⇄y",
        "123": "PV",
        "CLK": "🕒",
        "<--": "<-",
        "&lt;-": "<-",
        "&lt;--": "<-",
        "⌫": "<-",
        "←": "<-",
        "ENT": "ENTER",
        "CLSTAT": "CLΣ",
        "CLEAR Σ": "CLΣ",
        "ȳ": "ȳ",
        "x̄_w": "x̄w",
        "x̄, ȳ": "x̄,ȳ",
        "x̄,ȳ": "x̄,ȳ",
        "x&parallel;y": "x∥y",
        "&radic;x": "√x",
        "-&gt;REC": "▸y,x",
        "-&gt;POL": "▸θ,r",
        "&divide;": "÷",
    }
    for k, v in replacements.items():
        if s == k:
            s = v
    # Also replace math italics inside composite strings (like √𝑥 -> √x, 𝑥² -> x²)
    s = s.replace("𝑥", "x").replace("𝑦", "y").replace("𝑒", "e").replace("−", "-")
    if s == "x⁻¹":
        s = "1/x"
    if s == "LASTx":
        s = "LASTX"
    return s


@dataclass(frozen=True)
class KeyEntry:
    canonical: str       # Display label inside brackets, e.g. "SIN", "SOLVE", "π", "1/x"
    shift: Optional[str] # None (primary/softkey/alpha), or exact shift key label ("↰"/"↱" on SC-32, "f"/"g" on SC-6)
    layer: str           # "primary", "yellow", "blue", "menu", "alpha"
    row: int
    col: int

    def format_keystroke(self) -> str:
        if self.shift:
            return f"[{self.shift}] [{self.canonical}]"
        return f"[{self.canonical}]"

    def format_keycap(self) -> str:
        return f"[{self.canonical}]"


class KeyRegistry:
    """Authoritative key and softkey lookup grounded in layout_data*.json from RPNCore."""

    def __init__(self, json_path: Path, is_sc32: bool):
        self.json_path = json_path
        self.is_sc32 = is_sc32
        self.entries: Dict[str, KeyEntry] = {}
        self.primary_labels: Set[str] = set()
        self.yellow_labels: Set[str] = set()
        self.blue_labels: Set[str] = set()
        self.menu_labels: Set[str] = set()
        self.alpha_labels: Set[str] = set()
        self.raw_data = json.loads(json_path.read_text(encoding="utf-8"))
        self.left_shift_label = "↰" if is_sc32 else "f"
        self.right_shift_label = "↱" if is_sc32 else "g"
        for k in self.raw_data.get("keys", []):
            if k.get("isShiftYellow") and k.get("primaryLabel"):
                self.left_shift_label = k["primaryLabel"].strip()
            if k.get("isShiftBlue") and k.get("primaryLabel"):
                self.right_shift_label = k["primaryLabel"].strip()
        self._build()

    def _register(self, alias: str, entry: KeyEntry, overwrite: bool = False) -> None:
        norm = normalize_key_token(alias)
        for key in {alias.strip(), norm, alias.strip().upper(), norm.upper()}:
            if not key:
                continue
            # Do not let case-insensitive upper alias clobber distinct case-sensitive keys (like 'e' vs 'E' or 'm' vs 'M')
            if key in ("E", "M", "B", "R", "N", "S") and key != alias.strip() and key != norm:
                continue
            if overwrite or key not in self.entries:
                self.entries[key] = entry

    def _build(self) -> None:
        # 1. Register softkey LFU0..LFU5 and shift keys first
        for i in range(6):
            lfu = f"LFU{i}"
            self.primary_labels.add(lfu)
            self._register(lfu, KeyEntry(lfu, None, "primary", 0, i), overwrite=True)

        # Register shift keys themselves (mapping both f/↰ -> left_shift_label and g/↱ -> right_shift_label)
        for sh_lbl in ("f", "↰", self.left_shift_label):
            self._register(sh_lbl, KeyEntry(self.left_shift_label, None, "primary", 5, 0), overwrite=True)
        for sh_lbl in ("g", "↱", self.right_shift_label):
            self._register(sh_lbl, KeyEntry(self.right_shift_label, None, "primary", 6, 0), overwrite=True)

        # 2. Register Menus from JSON (lower precedence than physical keys)
        menus = self.raw_data.get("menus", {})
        for menu_name, items in menus.items():
            for item_lbl in items:
                clean_lbl = normalize_key_token(item_lbl.replace(" ▸", "").strip())
                if not clean_lbl:
                    continue
                self.menu_labels.add(clean_lbl)
                self._register(clean_lbl, KeyEntry(clean_lbl, None, "menu", 0, 0), overwrite=False)
                self._register(item_lbl.strip(), KeyEntry(clean_lbl, None, "menu", 0, 0), overwrite=False)

        # Additional contextual softkeys in STAT / EQN / PLOT / TVM modes
        extra_softkeys = [
            "CLx", "CLΣ", "2-LV", "4-LV", "8-LV",
            "I%", "END/BEG", "BGN/END", "d/dx",
            "NEW", "VARS", "PRGM",
        ]
        for sk in extra_softkeys:
            self.menu_labels.add(sk)
            self._register(sk, KeyEntry(sk, None, "menu", 0, 0), overwrite=False)

        # 3. Register Alpha labels from JSON (lower precedence than physical primary/shift keys)
        for k in self.raw_data.get("keys", []):
            alpha = k.get("alphaLabel", "").strip()
            if alpha:
                self.alpha_labels.add(alpha)
                self._register(alpha, KeyEntry(alpha, None, "alpha", k["row"], k["col"]), overwrite=False)

        # 4. Register Physical Keys (Right/Blue shift, Left/Yellow shift, and Primary) with highest priority
        for k in self.raw_data.get("keys", []):
            r, c = k["row"], k["col"]

            # Right Shift ([↱] on SC-32, [g] on SC-6)
            blu_raw = k.get("blueLabel", "").strip()
            blu_suf = k.get("blueSuffix")
            if blu_raw:
                blu_disp = normalize_key_token(blu_raw)
                self.blue_labels.add(blu_disp)
                entry_b = KeyEntry(blu_disp, self.right_shift_label, "blue", r, c)
                self._register(blu_raw, entry_b, overwrite=True)
                self._register(blu_disp, entry_b, overwrite=True)
                if blu_raw.startswith("▸"):
                    arrow_alias = "->" + blu_raw[1:]
                    r_arrow_alias = "→" + blu_raw[1:]
                    self._register(arrow_alias, entry_b, overwrite=True)
                    self._register(r_arrow_alias, entry_b, overwrite=True)
                if blu_suf:
                    self._register(f"->{blu_suf}", entry_b, overwrite=True)
                    self._register(f"▸{blu_suf}", entry_b, overwrite=True)

            # Left Shift ([↰] on SC-32, [f] on SC-6)
            yel_raw = k.get("yellowLabel", "").strip()
            yel_suf = k.get("yellowSuffix")
            if yel_raw:
                yel_disp = normalize_key_token(yel_raw)
                self.yellow_labels.add(yel_disp)
                entry_y = KeyEntry(yel_disp, self.left_shift_label, "yellow", r, c)
                self._register(yel_raw, entry_y, overwrite=True)
                self._register(yel_disp, entry_y, overwrite=True)
                if yel_raw.startswith("▸"):
                    arrow_alias = "->" + yel_raw[1:]
                    r_arrow_alias = "→" + yel_raw[1:]
                    self._register(arrow_alias, entry_y, overwrite=True)
                    self._register(r_arrow_alias, entry_y, overwrite=True)
                if yel_suf:
                    self._register(f"->{yel_suf}", entry_y, overwrite=True)
                    self._register(f"▸{yel_suf}", entry_y, overwrite=True)

            # Primary Key
            prim_raw = k.get("primaryLabel", "").strip()
            if prim_raw:
                prim_disp = normalize_key_token(prim_raw)
                self.primary_labels.add(prim_disp)
                entry_p = KeyEntry(prim_disp, None, "primary", r, c)
                self._register(prim_raw, entry_p, overwrite=True)
                self._register(prim_disp, entry_p, overwrite=True)
                if prim_raw in ("𝑥⁻¹", "x⁻¹", "1/x"):
                    self.primary_labels.add("1/x")
                    self.primary_labels.add("x⁻¹")
                    self._register("1/x", KeyEntry("1/x", None, "primary", r, c), overwrite=True)
                    self._register("x⁻¹", KeyEntry("1/x", None, "primary", r, c), overwrite=True)

        # Common coordinate conversion aliases on SC-32 (▸θ,r is Polar, ▸y,x is Rectangular)
        if self.is_sc32:
            if "▸θ,r" in self.entries:
                pol_entry = self.entries["▸θ,r"]
                for alias in ("->POL", "→POL", "▸POL", "->θ,r", "→θ,r", "->P", "→P", "▸P", "->POLAR", "→POLAR", "POLAR"):
                    self.entries[alias] = pol_entry
            if "▸y,x" in self.entries:
                rec_entry = self.entries["▸y,x"]
                for alias in ("->REC", "→REC", "▸REC", "->y,x", "→y,x"):
                    self.entries[alias] = rec_entry

    def resolve(self, key_name: str) -> KeyEntry:
        clean = key_name.strip()
        norm = normalize_key_token(clean)
        for candidate in (clean, norm, clean.upper(), norm.upper()):
            if candidate in self.entries:
                return self.entries[candidate]
        model = "SC-32" if self.is_sc32 else "SC-6"
        raise ValueError(
            f"Unknown key macro '{key_name}' (normalized: '{norm}') for {model} "
            f"(not found in {self.json_path.name})"
        )


_REGISTRIES: Dict[bool, KeyRegistry] = {}


def get_registry(is_sc32: bool) -> KeyRegistry:
    if is_sc32 not in _REGISTRIES:
        path = SC32_JSON_PATH if is_sc32 else SC6_JSON_PATH
        _REGISTRIES[is_sc32] = KeyRegistry(path, is_sc32=is_sc32)
    return _REGISTRIES[is_sc32]


SEQUENCES_JSON_PATH = MANUALS_ASSETS_DIR / "sequences_registry.json"
BLOCKS_JSON_PATH = MANUALS_ASSETS_DIR / "blocks_registry.json"
CITATIONS_JSON_PATH = MANUALS_ASSETS_DIR / "citations_registry.json"
BIBLIOGRAPHY_BIB_PATH = MANUALS_ASSETS_DIR / "bibliography.bib"
SCREENSHOTS_DIR = MANUALS_ASSETS_DIR / "screenshots"

_SEQUENCES_CACHE: Optional[Dict[str, dict]] = None
_BLOCKS_CACHE: Optional[Dict[str, dict]] = None
_CITATIONS_CACHE: Optional[Dict[str, dict]] = None


def get_sequences_registry() -> Dict[str, dict]:
    global _SEQUENCES_CACHE
    if _SEQUENCES_CACHE is None:
        if SEQUENCES_JSON_PATH.exists():
            _SEQUENCES_CACHE = json.loads(SEQUENCES_JSON_PATH.read_text(encoding="utf-8"))
        else:
            _SEQUENCES_CACHE = {}
    return _SEQUENCES_CACHE


def get_blocks_registry() -> Dict[str, dict]:
    global _BLOCKS_CACHE
    if _BLOCKS_CACHE is None:
        if BLOCKS_JSON_PATH.exists():
            _BLOCKS_CACHE = json.loads(BLOCKS_JSON_PATH.read_text(encoding="utf-8"))
        else:
            _BLOCKS_CACHE = {}
    return _BLOCKS_CACHE


def get_citations_registry() -> Dict[str, dict]:
    global _CITATIONS_CACHE
    if _CITATIONS_CACHE is None:
        if CITATIONS_JSON_PATH.exists():
            _CITATIONS_CACHE = json.loads(CITATIONS_JSON_PATH.read_text(encoding="utf-8"))
        else:
            _CITATIONS_CACHE = {}
    return _CITATIONS_CACHE


def resolve_citation(cite_id: str, file_path: Optional[Path] = None) -> dict:
    reg = get_citations_registry()
    clean_id = cite_id.strip()
    if clean_id in reg:
        return reg[clean_id]
    clean_lower = clean_id.lower()
    for k, v in reg.items():
        if k.lower() == clean_lower:
            return v
    loc = f" in {file_path}" if file_path else ""
    raise ValueError(f"Unknown citation ID '{cite_id}' (not found in citations_registry.json){loc}")


CITE_MACRO_PATTERN = re.compile(r"\{\{cite:([^{}]+)\}\}")
BIBLIOGRAPHY_MACRO_PATTERN = re.compile(r"\{\{bibliography:(sc32|sc6)\}\}")


def get_chapter_label(file_path: Path) -> str:
    name = file_path.name
    if name == "index.md":
        return "Foreword"
    m_ch = re.match(r"^0*([1-9][0-9]*)-", name)
    if m_ch:
        return f"Ch {int(m_ch.group(1)):02d}"
    m_app = re.match(r"^appendix-([a-z])-", name, flags=re.IGNORECASE)
    if m_app:
        return f"App {m_app.group(1).upper()}"
    return file_path.stem


def scan_citation_backreferences(volume: str) -> Dict[str, List[Tuple[str, str]]]:
    """
    Scans all .md files in docs/manuals/{volume}/ (excluding the bibliography page itself)
    for {{cite:...}} macros.
    Returns a mapping: cite_id (canonical) -> list of unique (chapter_label, relative_md_filename).
    """
    manuals_dir = DOCS_DIR / "manuals" / volume
    bib_file = "appendix-e-annotated-bibliography.md" if volume == "sc32" else "appendix-c-formulas-and-conversions.md"
    backrefs: Dict[str, List[Tuple[str, str]]] = {}

    if not manuals_dir.exists():
        return backrefs

    for md_path in sorted(manuals_dir.glob("*.md")):
        if md_path.name == bib_file:
            continue
        text = md_path.read_text(encoding="utf-8")
        ch_label = get_chapter_label(md_path)
        for m in CITE_MACRO_PATTERN.finditer(text):
            raw_payload = m.group(1)
            ids = [s.strip() for s in raw_payload.split(",") if s.strip()]
            for cid in ids:
                try:
                    entry = resolve_citation(cid, file_path=md_path)
                    canon_id = entry["id"]
                    if canon_id not in backrefs:
                        backrefs[canon_id] = []
                    item = (ch_label, md_path.name)
                    if item not in backrefs[canon_id]:
                        backrefs[canon_id].append(item)
                except ValueError:
                    continue

    return backrefs


def get_bibtex_blocks_for_volume(volume: str) -> str:
    if not BIBLIOGRAPHY_BIB_PATH.exists():
        return ""
    text = BIBLIOGRAPHY_BIB_PATH.read_text(encoding="utf-8")
    reg = get_citations_registry()
    allowed_ids = {
        k.lower() for k, v in reg.items()
        if v.get("volume_scope") in (volume, "both")
    }
    pattern = re.compile(r"(@[a-zA-Z]+\s*\{\s*([a-zA-Z0-9_-]+)\s*,.*?\n\})", re.DOTALL)
    blocks = []
    for m in pattern.finditer(text):
        entry_key = m.group(2).lower()
        if entry_key in allowed_ids:
            blocks.append(m.group(1).strip())
    return "\n\n".join(blocks)


def generate_bibliography_markdown(volume: str, target_format: str = "web", file_path: Optional[Path] = None) -> str:
    reg = get_citations_registry()
    backrefs = scan_citation_backreferences(volume)

    CATEGORY_ORDER = [
        "Foundations of Logic & Computer Architecture",
        "Corvallis Silicon & Handheld Architecture",
        "Numerical Stability & Scientific Algorithms",
        "Breakout Mathematics & Scientific Nonfiction",
        "Pedagogy, Cognitive Science & Manipulatives",
        "Standards & Hardware Handbooks",
    ]

    cat_entries: Dict[str, List[dict]] = {cat: [] for cat in CATEGORY_ORDER}
    other_entries: List[dict] = []

    for entry in reg.values():
        scope = entry.get("volume_scope", "both")
        if scope != "both" and scope != volume:
            continue
        cat = entry.get("category", "")
        if cat in cat_entries:
            cat_entries[cat].append(entry)
        else:
            other_entries.append(entry)

    for cat in CATEGORY_ORDER:
        cat_entries[cat].sort(key=lambda x: (x.get("year", 0), x.get("author", "")))
    other_entries.sort(key=lambda x: (x.get("year", 0), x.get("author", "")))

    lines: List[str] = []

    for cat in CATEGORY_ORDER:
        entries = cat_entries[cat]
        if not entries:
            continue
        lines.append(f"### {cat}")
        lines.append("")
        for e in entries:
            eid = e["id"]
            author = e.get("author", "")
            year = e.get("year", "")
            title = e.get("title", "")
            pub = e.get("journal") or e.get("publisher") or e.get("institution") or e.get("organization") or ""
            if e.get("volume") and e.get("number"):
                pub += f", Vol. {e['volume']}, No. {e['number']}"
            elif e.get("volume"):
                pub += f", Vol. {e['volume']}"
            if e.get("pages"):
                pub += f", pp. {e['pages']}"
            if e.get("address"):
                pub += f", {e['address']}"
            annotation = e.get("annotation", "")

            refs = backrefs.get(eid, [])
            if refs:
                refs_sorted = sorted(refs, key=lambda x: x[0])
                if target_format == "web":
                    ref_links = [f"[{lbl}]({fn})" for lbl, fn in refs_sorted]
                    cited_str = ", ".join(ref_links)
                else:
                    cited_str = ", ".join(lbl for lbl, _ in refs_sorted)
            else:
                cited_str = "*Foundational reference & curriculum background*"

            pub_part = f" *{pub}*." if pub else ""
            lines.append(f"<a id=\"cite-{eid}\"></a>")
            lines.append(f"**[{eid}] {author} ({year})** — *{title}*.{pub_part}")
            lines.append(f"> **Annotation:** {annotation}  ")
            lines.append(f"> **Cited in Chapters:** {cited_str}")
            lines.append("")

    if other_entries:
        lines.append("### Additional References")
        lines.append("")
        for e in other_entries:
            eid = e["id"]
            author = e.get("author", "")
            year = e.get("year", "")
            title = e.get("title", "")
            annotation = e.get("annotation", "")
            refs = backrefs.get(eid, [])
            if refs:
                refs_sorted = sorted(refs, key=lambda x: x[0])
                if target_format == "web":
                    ref_links = [f"[{lbl}]({fn})" for lbl, fn in refs_sorted]
                    cited_str = ", ".join(ref_links)
                else:
                    cited_str = ", ".join(lbl for lbl, _ in refs_sorted)
            else:
                cited_str = "*Foundational reference & curriculum background*"

            lines.append(f"<a id=\"cite-{eid}\"></a>")
            lines.append(f"**[{eid}] {author} ({year})** — *{title}*.")
            lines.append(f"> **Annotation:** {annotation}  ")
            lines.append(f"> **Cited in Chapters:** {cited_str}")
            lines.append("")

    bibtex_content = get_bibtex_blocks_for_volume(volume)
    if bibtex_content:
        vol_label = "StackCalc SC-32 Scientific" if volume == "sc32" else "StackCalc SC-6 Elementary"
        lines.append(f"### Complete BibTeX Catalog ({vol_label})")
        lines.append("")
        lines.append("```bibtex")
        lines.append(bibtex_content)
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def expand_cite_macros(markdown: str, is_sc32: bool, file_path: Optional[Path] = None, target_format: str = "web") -> str:
    loc = f" in {file_path}" if file_path else ""

    bib_filename = "appendix-e-annotated-bibliography.md" if is_sc32 else "appendix-c-formulas-and-conversions.md"
    bib_rel_path = bib_filename
    if file_path:
        if file_path.name == bib_filename:
            bib_rel_path = ""
        else:
            p_str = str(file_path).replace("\\", "/")
            if "/manuals/sc32/" in p_str:
                bib_rel_path = "appendix-e-annotated-bibliography.md"
            elif "/manuals/sc6/" in p_str:
                bib_rel_path = "appendix-c-formulas-and-conversions.md"
            elif file_path.parent == DOCS_DIR:
                sub = "sc32" if is_sc32 else "sc6"
                bib_rel_path = f"manuals/{sub}/{bib_filename}"
            elif file_path.parent.parent == DOCS_DIR:
                sub = "sc32" if is_sc32 else "sc6"
                bib_rel_path = f"../manuals/{sub}/{bib_filename}"

    def _repl(match: re.Match) -> str:
        payload = match.group(1).strip()
        ids = [i.strip() for i in payload.split(",") if i.strip()]
        if not ids:
            raise ValueError(f"Empty citation macro {{{{cite:{payload}}}}}{loc}")

        entries = []
        for cid in ids:
            entry = resolve_citation(cid, file_path=file_path)
            entries.append(entry)

        if target_format == "pdf":
            cites = [e.get("short_cite") or f"{e.get('short_author', e.get('author'))}, {e.get('year')}" for e in entries]
            return f"*({'; '.join(cites)})*"
        else:
            linked_cites = []
            for e in entries:
                eid = e["id"]
                short_text = e.get("short_cite") or f"{e.get('short_author', e.get('author'))}, {e.get('year')}"
                target_url = f"{bib_rel_path}#cite-{eid}" if bib_rel_path else f"#cite-{eid}"
                linked_cites.append(f"[{short_text}]({target_url})")
            return f"*({'; '.join(linked_cites)})*"

    return CITE_MACRO_PATTERN.sub(_repl, markdown)


def expand_bibliography_macros(markdown: str, file_path: Optional[Path] = None, target_format: str = "web") -> str:
    def _repl(match: re.Match) -> str:
        volume = match.group(1).lower()
        return generate_bibliography_markdown(volume, target_format=target_format, file_path=file_path)

    return BIBLIOGRAPHY_MACRO_PATTERN.sub(_repl, markdown)


# ---------------------------------------------------------------------------
# Macro Expansion & Programmatic Validation (key, keycap, seq, res, screenshot, blocks, icon, cite)
# ---------------------------------------------------------------------------
ICON_REGISTRY: Dict[str, dict] = {
    "button_prime": {
        "id": "button_prime",
        "svg": "Education/scad/lib/icons/button_prime.svg",
        "scad": "Education/scad/prime_studio_box.scad",
        "kit": "PRIME-01",
        "key": "FACT",
        "model": "sc6",
        "label": "Factor Tree Icon ([PRIME] / [g][FACT])",
    },
    "button_fraction": {
        "id": "button_fraction",
        "svg": "Education/scad/lib/icons/button_fraction.svg",
        "scad": "Education/scad/fraction_studio_box.scad",
        "kit": "FRAC-01",
        "key": "FDISP",
        "model": "sc6",
        "label": "Fraction Display Icon ([FDISP] & [g][SIMP])",
    },
    "button_algebra": {
        "id": "button_algebra",
        "svg": "Education/scad/lib/icons/button_algebra.svg",
        "scad": "Education/scad/algebra_factoring_box.scad",
        "kit": "ALGB-01",
        "key": "POLY",
        "model": "sc32",
        "label": "Polynomial Solver Icon ([↱][EQN] & [↱][POLY])",
    },
    "button_clock": {
        "id": "button_clock",
        "svg": "Education/scad/lib/icons/button_clock.svg",
        "scad": "Education/scad/clock_system_box.scad",
        "kit": "TIME-01",
        "key": "🕒",
        "model": "sc6",
        "label": "Clock HMS Icon ([🕒] / [g][▸HMS] / [f][▸HR])",
    },
    "button_ten_frame": {
        "id": "button_ten_frame",
        "svg": "Education/scad/lib/icons/button_ten_frame.svg",
        "scad": "Education/scad/ten_frames_box.scad",
        "kit": "BASE-10",
        "key": "▦",
        "model": "sc6",
        "label": "Ten-Frame Icon ([▦] & [PV])",
    },
    "button_place_value": {
        "id": "button_place_value",
        "svg": "Education/scad/lib/icons/button_place_value.svg",
        "scad": "Education/scad/place_value_box.scad",
        "kit": "PLACE-01",
        "key": "PV",
        "model": "sc6",
        "label": "Place Value Icon ([PV] & [g][÷R])",
    },
    "button_domino": {
        "id": "button_domino",
        "svg": "Education/scad/lib/icons/button_domino.svg",
        "scad": "Education/scad/math_dominoes_box.scad",
        "kit": "DOMI-01",
        "key": "COUNT",
        "model": "sc6",
        "label": "Domino Pip Pattern Icon ([g][COUNT] & [g][a:b])",
    },
    "button_dice": {
        "id": "button_dice",
        "svg": "Education/scad/lib/icons/button_dice.svg",
        "scad": "Education/scad/dice_and_spinner_box.scad",
        "kit": "PROB-01",
        "key": "🎲",
        "model": "sc6",
        "label": "Dice & Statistics Icon ([🎲], [Σ+] & [g][x̄])",
    },
    "button_volvelle": {
        "id": "button_volvelle",
        "svg": "Education/scad/lib/icons/button_volvelle.svg",
        "scad": "Hardware/designs/volvelle.scad",
        "kit": "VOLV-01",
        "key": "▸y,x",
        "model": "sc32",
        "label": "Unit Circle Radian Icon ([COS], [SIN] & [↱][▸y,x])",
    },
    "button_unifix": {
        "id": "button_unifix",
        "svg": "Education/scad/lib/icons/button_unifix.svg",
        "scad": "Education/scad/unifix_cubes_box.scad",
        "kit": "COUNT-01",
        "key": "ENTER",
        "model": "sc6",
        "label": "Counting & Stack Lift Icon ([ENTER])",
    },
    "button_number_rack": {
        "id": "button_number_rack",
        "svg": "Education/scad/lib/icons/button_number_rack.svg",
        "scad": "Education/scad/number_rack_box.scad",
        "kit": "RACK-01",
        "key": "▦",
        "model": "sc6",
        "label": "Number Rack Subitizing Icon ([▦])",
    },
}


def get_icons_registry() -> Dict[str, dict]:
    return ICON_REGISTRY


def resolve_icon(icon_id: str, file_path: Optional[Path] = None) -> dict:
    clean = icon_id.strip()
    if clean.endswith(".svg"):
        clean = clean[:-4]
    if clean in ICON_REGISTRY:
        return ICON_REGISTRY[clean]
    if f"button_{clean}" in ICON_REGISTRY:
        return ICON_REGISTRY[f"button_{clean}"]
    loc = f" in {file_path}" if file_path else ""
    raise ValueError(f"Unknown {{{{icon:{icon_id}}}}} macro (not in ICON_REGISTRY){loc}")


KEY_MACRO_PATTERN = re.compile(r"\{\{(key|keycap):([^{}]+)\}\}")
UNIFIED_MACRO_PATTERN = re.compile(r"\{\{(seq|seq_keys|res|screenshot|blocks|icon):([^{}]+)\}\}")


def _expand_only_keys(markdown: str, is_sc32: bool, file_path: Optional[Path] = None) -> str:
    registry = get_registry(is_sc32)
    is_strict_manual = False
    if file_path:
        p_str = str(file_path).replace("\\", "/")
        if "/manuals/sc32/" in p_str or "/manuals/sc6/" in p_str or p_str.endswith("sc32-user-guide.md") or p_str.endswith("sc6-user-guide.md"):
            is_strict_manual = True

    def _repl(match: re.Match) -> str:
        kind = match.group(1)
        raw_name = match.group(2).strip()
        try:
            entry = registry.resolve(raw_name)
        except ValueError as err:
            if not is_strict_manual:
                try:
                    entry = get_registry(not is_sc32).resolve(raw_name)
                except ValueError:
                    loc = f" in {file_path}" if file_path else ""
                    raise ValueError(f"{err}{loc}") from err
            else:
                loc = f" in {file_path}" if file_path else ""
                raise ValueError(f"{err}{loc}") from err
        if kind == "keycap":
            return entry.format_keycap()
        return entry.format_keystroke()

    expanded = KEY_MACRO_PATTERN.sub(_repl, markdown)
    expanded = re.sub(r"\[(↰|↱|f|g)\](\s*`?\s*`?)\[\1\]", r"[\1]\2", expanded)
    return expanded


def expand_key_macros(markdown: str, is_sc32: bool, file_path: Optional[Path] = None, target_format: str = "web") -> str:
    """
    Expands all unified textbook macros in `markdown`:
      - `{{res:ID}}` or `{{res:ID:value}}` / `{{res:ID:number}}`: Verified calculator result inline as numbers
      - `{{res:ID:keys}}` / `{{res:ID:keystrokes}}` / `{{res:ID:seq}}` (or `{{seq:ID}}`): Verified keystroke sequence
      - `{{res:ID:seq_keys}}` (or `{{seq_keys:ID}}`): Verified keystroke sequence with digits as keycaps
      - `{{res:ID:both}}` / `{{res:ID:inline}}`: Both keystrokes and resulting value inline together
      - `{{res:ID:stack}}` / `{{res:ID:table}}`: Resulting 4-register stack (T, Z, Y, X) from CalculatorEngine
      - `{{res:ID:screenshot}}` or `{{res:ID:screenshot|Caption}}` (or `{{screenshot:ID}}`): Verified SwiftUI screenshot
      - `{{blocks:ID}}` or `{{blocks:ID|Caption}}`: Verified OpenSCAD orthographic diagram from blocks_registry.json
      - `{{icon:ID}}`: Verified Box Button Icon mapped to its physical calculator operation key
      - `{{key:NAME}}` / `{{keycap:NAME}}`: Verified hardware shift + keycap sequence from layout_data*.json
    Raises ValueError if any macro references a non-existent key, sequence, screenshot, or block diagram,
    or if any sequence result contains a placeholder string like 'Verified in RPNCore'.
    """
    sequences = get_sequences_registry()
    blocks = get_blocks_registry()
    loc = f" in {file_path}" if file_path else ""

    assets_prefix = "../../assets/manuals"
    renders_prefix = "../../assets/renders"
    if file_path:
        if file_path.parent == DOCS_DIR:
            assets_prefix = "assets/manuals"
            renders_prefix = "assets/renders"
        elif file_path.parent.parent == DOCS_DIR:
            assets_prefix = "../assets/manuals"
            renders_prefix = "../assets/renders"

    def _resolve_screenshot(item_id: str, custom_caption: Optional[str]) -> str:
        filename: Optional[str] = None
        default_caption = item_id
        if item_id in sequences and sequences[item_id].get("screenshot"):
            filename = sequences[item_id]["screenshot"]
            default_caption = sequences[item_id].get("description", item_id)
        else:
            candidate = item_id if item_id.endswith(".png") else f"{item_id}.png"
            if (SCREENSHOTS_DIR / candidate).exists():
                filename = candidate
            elif (MANUALS_ASSETS_DIR / candidate).exists():
                caption = custom_caption or default_caption
                return f"![{caption}]({assets_prefix}/{candidate})"
        if not filename or not (SCREENSHOTS_DIR / filename).exists():
            raise ValueError(
                f"Unknown or missing screenshot for '{item_id}' "
                f"(looked in {SCREENSHOTS_DIR}){loc}"
            )
        caption = custom_caption or default_caption
        return f"![{caption}]({assets_prefix}/screenshots/{filename})"

    def _unified_repl(match: re.Match) -> str:
        kind = match.group(1)
        payload = match.group(2).strip()
        if "|" in payload:
            target_spec, custom_caption = [p.strip() for p in payload.split("|", 1)]
        else:
            target_spec, custom_caption = payload, None

        if kind in ("seq", "seq_keys"):
            item_id = target_spec
            if item_id not in sequences:
                raise ValueError(f"Unknown {{{{{kind}:{item_id}}}}} macro (not in sequences_registry.json){loc}")
            entry = sequences[item_id]
            seq_is_sc32 = entry.get("model", "sc32") == "sc32"
            raw_seq = (entry["seqKeys"] if kind == "seq_keys" else entry["seq"]).replace("`", "")
            return _expand_only_keys(raw_seq, is_sc32=seq_is_sc32, file_path=file_path)

        if kind == "res":
            if ":" in target_spec:
                item_id, op = [p.strip() for p in target_spec.split(":", 1)]
                op = op.lower()
            else:
                item_id, op = target_spec, "value"

            if op in ("screenshot", "image"):
                return _resolve_screenshot(item_id, custom_caption)

            if item_id not in sequences:
                raise ValueError(f"Unknown {{{{res:{target_spec}}}}} macro (ID '{item_id}' not in sequences_registry.json){loc}")
            entry = sequences[item_id]
            seq_is_sc32 = entry.get("model", "sc32") == "sc32"
            res_str = str(entry.get("res", ""))
            if "Verified in RPNCore" in res_str or res_str == "NEED_ENGINE":
                raise ValueError(f"Placeholder '{res_str}' is forbidden for {{{{res:{target_spec}}}}}{loc}")

            if op in ("value", "number", "res"):
                return res_str
            if op in ("keys", "keystrokes", "seq"):
                return _expand_only_keys(entry["seq"].replace("`", ""), is_sc32=seq_is_sc32, file_path=file_path)
            if op == "seq_keys":
                return _expand_only_keys(entry["seqKeys"].replace("`", ""), is_sc32=seq_is_sc32, file_path=file_path)
            if op in ("both", "inline"):
                expanded_seq = _expand_only_keys(entry["seq"].replace("`", ""), is_sc32=seq_is_sc32, file_path=file_path)
                return f"`{expanded_seq}` → **`{res_str}`**"
            if op == "stack":
                st = entry.get("stack") or {"T": "0", "Z": "0", "Y": "0", "X": res_str}
                return f"T: {st.get('T', '0')} | Z: {st.get('Z', '0')} | Y: {st.get('Y', '0')} | X: {st.get('X', res_str)}"
            if op == "table":
                st = entry.get("stack") or {"T": "0", "Z": "0", "Y": "0", "X": res_str}
                return (
                    "| Register T | Register Z | Register Y | Register X |\n"
                    "| :--- | :--- | :--- | :--- |\n"
                    f"| `{st.get('T', '0')}` | `{st.get('Z', '0')}` | `{st.get('Y', '0')}` | **`{st.get('X', res_str)}`** |"
                )
            raise ValueError(f"Unknown operation '{op}' in {{{{res:{target_spec}}}}}{loc}")

        if kind == "screenshot":
            return _resolve_screenshot(target_spec, custom_caption)

        if kind == "blocks":
            item_id = target_spec
            if item_id not in blocks:
                raise ValueError(f"Unknown {{{{blocks:{item_id}}}}} macro (not in blocks_registry.json){loc}")
            b_entry = blocks[item_id]
            png_name = b_entry["png"]
            caption = custom_caption or b_entry.get("alt", item_id)
            if (MANUALS_ASSETS_DIR / png_name).exists():
                return f"![{caption}]({assets_prefix}/{png_name})"
            if (DOCS_DIR / "assets" / "renders" / png_name).exists():
                return f"![{caption}]({renders_prefix}/{png_name})"
            raise ValueError(
                f"Missing rendered PNG '{png_name}' for {{{{blocks:{item_id}}}}} in {MANUALS_ASSETS_DIR}{loc}"
            )

        if kind == "icon":
            ic_entry = resolve_icon(target_spec, file_path=file_path)
            return custom_caption or ic_entry["label"]

        return match.group(0)

    step0 = _expand_only_keys(markdown, is_sc32=is_sc32, file_path=file_path)
    step1 = UNIFIED_MACRO_PATTERN.sub(_unified_repl, step0)
    step2 = _expand_only_keys(step1, is_sc32=is_sc32, file_path=file_path)
    return expand_cite_macros(step2, is_sc32=is_sc32, file_path=file_path, target_format=target_format)


def build_svg_macro_manifest(
    kit_id: str,
    blocks_ids: List[str],
    seq_ids: List[str],
    icon_ids: Optional[List[str]] = None,
) -> str:
    """
    Constructs a structured <metadata id="stackcalc-book-macro-manifest"> XML block
    for reference card and booklet SVGs. Validates every {{blocks:ID}}, {{seq:ID}},
    {{res:ID}}, {{res:ID:stack}}, and {{icon:ID}} against the authoritative book
    registries so unit tests can cross-reference images, keystrokes, results, and
    programmatic scenes while keeping student-facing <text> nodes 100% clean.
    """
    from xml.sax.saxutils import escape as _xml_esc

    def _attr(val: str) -> str:
        return _xml_esc(str(val), {'"': "&quot;"})

    sequences = get_sequences_registry()
    blocks = get_blocks_registry()
    lines = [
        f'  <metadata id="stackcalc-book-macro-manifest" data-kit="{_attr(kit_id)}">',
        "    <stackcalc-macros>",
    ]
    for bid in dict.fromkeys(blocks_ids):
        if bid not in blocks:
            raise ValueError(f"Unknown {{{{blocks:{bid}}}}} macro in SVG manifest for {kit_id}")
        b = blocks[bid]
        scad_str = ",".join(b.get("scad_sources", []))
        stl_str = ",".join(b.get("stls", []))
        lines.append(
            f'      <macro-ref token="{{{{blocks:{_attr(bid)}}}}}" kind="blocks" id="{_attr(bid)}" '
            f'png="{_attr(b["png"])}" svg="{_attr(b["svg"])}" scene="{_attr(b.get("scene", ""))}" '
            f'scad="{_attr(b.get("scad", ""))}" scad-sources="{_attr(scad_str)}" stls="{_attr(stl_str)}" />'
        )
    for sid in dict.fromkeys(seq_ids):
        if sid not in sequences:
            raise ValueError(f"Unknown {{{{seq:{sid}}}}} macro in SVG manifest for {kit_id}")
        s = sequences[sid]
        seq_is_sc32 = s.get("model", "sc32") == "sc32"
        expanded_seq = _expand_only_keys(s["seq"], is_sc32=seq_is_sc32)
        res_val = str(s.get("res", ""))
        st = s.get("stack") or {"T": "0", "Z": "0", "Y": "0", "X": res_val}
        stack_str = f"T:{st.get('T','0')}|Z:{st.get('Z','0')}|Y:{st.get('Y','0')}|X:{st.get('X',res_val)}"
        lines.append(
            f'      <macro-ref token="{{{{seq:{_attr(sid)}}}}}" res-token="{{{{res:{_attr(sid)}}}}}" '
            f'stack-token="{{{{res:{_attr(sid)}:stack}}}}" kind="sequence" id="{_attr(sid)}" '
            f'model="{_attr(s.get("model", "sc32"))}" expanded-seq="{_attr(expanded_seq)}" '
            f'res="{_attr(res_val)}" stack="{_attr(stack_str)}" />'
        )
    for iid in dict.fromkeys(icon_ids or []):
        ic = resolve_icon(iid)
        lines.append(
            f'      <macro-ref token="{{{{icon:{_attr(ic["id"])}}}}}" kind="icon" id="{_attr(ic["id"])}" '
            f'svg="{_attr(ic["svg"])}" scad="{_attr(ic["scad"])}" key="{_attr(ic["key"])}" model="{_attr(ic["model"])}" />'
        )
    lines.append("    </stackcalc-macros>")
    lines.append("  </metadata>")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Deterministic Section Auto-Numbering & Cross-Reference Resolver
# ---------------------------------------------------------------------------
def get_chapter_prefix(file_path: Path) -> Optional[str]:
    """
    Returns the section numbering prefix for a manual file:
      - '01-craftsmanship-hardware.md' -> '1'
      - '14-uil-contest-playbook.md'   -> '14'
      - 'appendix-a-...'               -> 'A'
      - 'index.md'                     -> '' (top-level 1., 1.1)
      - other files                    -> None (no auto-numbering)
    """
    name = file_path.name
    m_ch = re.match(r"^0*([1-9][0-9]*)-.*\.md$", name)
    if m_ch:
        return m_ch.group(1)
    m_app = re.match(r"^appendix-([a-z])-.*\.md$", name, flags=re.IGNORECASE)
    if m_app:
        return m_app.group(1).upper()
    if name == "index.md" and file_path.parent.name in ("sc32", "sc6"):
        return ""
    return None


def strip_manual_section_number(heading_text: str) -> str:
    """
    Strips any leading section number like '1.1 ', '14.2.1 ', 'C.1 ', '1. ',
    or trailing '{: #...}' attribute list from a heading title.
    """
    s = heading_text.strip()
    # Strip trailing '{: #...}' attribute lists so MkDocs uses standard auto-numbered slugs
    s = re.sub(r"\s*\{:\s*#[^}]+\}\s*$", "", s)
    # Strip e.g. '1.1 ', '1.1.2 ', 'A.1 ', 'C.3.1 '
    s = re.sub(r"^(?:[0-9]+|[A-E])(?:\.[0-9]+)+\.?\s+", "", s)
    # Strip e.g. '1. ' on H2 in index.md
    s = re.sub(r"^[0-9]+\.\s+", "", s)
    return s.strip()


def mkdocs_slugify(heading_text: str, is_sc32: bool = True) -> str:
    """
    Computes the standard Python-Markdown / MkDocs anchor slug for a heading after
    key macros have been expanded.
    """
    expanded = expand_key_macros(heading_text, is_sc32=is_sc32)
    # Strip markdown formatting characters (*, _, `, [, ])
    s = re.sub(r"[*_`\[\]]", "", expanded)
    # Normalize unicode and keep ascii word chars, spaces, hyphens
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = s.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[-\s]+", "-", s).strip("-")
    return s


def auto_number_headings(markdown: str, file_path: Path) -> str:
    """
    Deterministically numbers all `## ` and `### ` headings in a manual chapter
    or appendix file outside fenced code blocks.
    """
    prefix = get_chapter_prefix(file_path)
    if prefix is None:
        return markdown

    lines = markdown.split("\n")
    out_lines: List[str] = []
    in_fence = False
    h2_count = 0
    h3_count = 0

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue

        if in_fence:
            out_lines.append(line)
            continue

        if line.startswith("## ") and not line.startswith("### "):
            raw_title = line[3:].strip()
            clean_title = strip_manual_section_number(raw_title)
            h2_count += 1
            h3_count = 0
            if prefix == "":
                numbered = f"## {h2_count}. {clean_title}"
            else:
                numbered = f"## {prefix}.{h2_count} {clean_title}"
            out_lines.append(numbered)
            continue

        if line.startswith("### ") and not line.startswith("#### "):
            raw_title = line[4:].strip()
            clean_title = strip_manual_section_number(raw_title)
            if h2_count > 0:
                h3_count += 1
                if prefix == "":
                    numbered = f"### {h2_count}.{h3_count} {clean_title}"
                else:
                    numbered = f"### {prefix}.{h2_count}.{h3_count} {clean_title}"
                out_lines.append(numbered)
            else:
                out_lines.append(f"### {clean_title}")
            continue

        out_lines.append(line)

    return "\n".join(out_lines)


def build_heading_anchor_map(manual_dir: Path, is_sc32: bool) -> Dict[Tuple[str, str], Tuple[str, str]]:
    """
    Scans all markdown files in `manual_dir`, applies auto-numbering, and maps
    (filename, unnumbered_slug_prefix) -> (sec_num, full_auto_numbered_slug).
    """
    anchor_map: Dict[Tuple[str, str], Tuple[str, str]] = {}
    for md_file in sorted(manual_dir.glob("*.md")):
        raw = md_file.read_text(encoding="utf-8")
        numbered = auto_number_headings(raw, md_file)
        in_fence = False
        for line in numbered.splitlines():
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            m = re.match(r"^(#{2,3})\s+((?:[0-9]+|[A-E])(?:\.[0-9]+)+)\s+(.*)$", line)
            if m:
                sec_num = m.group(2)
                clean_title = m.group(3)
                full_slug = mkdocs_slugify(f"{sec_num} {clean_title}", is_sc32=is_sc32)
                base_slug = mkdocs_slugify(clean_title, is_sc32=is_sc32)
                anchor_map[(md_file.name, base_slug)] = (sec_num, full_slug)
    return anchor_map


def sync_cross_reference_anchors(markdown: str, file_path: Path, is_sc32: bool) -> str:
    """
    Automatically updates internal and cross-chapter section links (such as
    `[Ch 3.1 Title](03-algebra-transcendentals.md#31-...)` or `[Sec C.5](#c5-...)`)
    to match the current auto-numbered section numbers and slugs.
    """
    manual_dir = file_path.parent
    if manual_dir.name not in ("sc32", "sc6"):
        return markdown

    anchor_map = build_heading_anchor_map(manual_dir, is_sc32=is_sc32)

    def _link_repl(match: re.Match) -> str:
        link_text = match.group(1)
        target_file = match.group(2) or file_path.name
        old_anchor = match.group(3)

        # Strip leading digits/letters from old_anchor to get base_slug
        base_anchor = re.sub(r"^[0-9a-e]+-", "", old_anchor)
        base_anchor_norm = re.sub(r"-(?:f|g)-", "-", base_anchor)
        lookup_file = Path(target_file).name

        found = anchor_map.get((lookup_file, base_anchor)) or anchor_map.get((lookup_file, base_anchor_norm))
        if not found:
            # Try prefix or substring match on base_anchor
            for (fn, b_slug), val in anchor_map.items():
                if fn == lookup_file and (
                    b_slug.startswith(base_anchor[:18])
                    or base_anchor.startswith(b_slug[:18])
                    or b_slug.startswith(base_anchor_norm[:18])
                    or base_anchor_norm.startswith(b_slug[:18])
                    or (len(base_anchor) >= 16 and base_anchor[:20] in b_slug)
                ):
                    found = val
                    break

        if not found:
            return match.group(0)

        new_sec_num, new_slug = found
        # Update 'Ch X.Y' or 'Sec X.Y' in link_text if present
        new_link_text = re.sub(
            r"\b(Ch|Sec)\s+(?:[0-9]+|[A-E])(?:\.[0-9]+)+",
            rf"\1 {new_sec_num}",
            link_text,
        )
        prefix_part = match.group(2) if match.group(2) else ""
        return f"[{new_link_text}]({prefix_part}#{new_slug})"

    return re.sub(r"\[([^\]]+)\]\(([^)#]*?)#([a-z0-9_-]+)\)", _link_repl, markdown)


def process_manual_markdown(
    markdown: str,
    file_path: Path,
    is_sc32: Optional[bool] = None,
    target_format: str = "web",
) -> str:
    """
    Complete pipeline for a manual markdown file:
      0. Expands {{bibliography:sc32}} and {{bibliography:sc6}} with chapter back-references
      1. Auto-numbers `##` and `###` section headings
      2. Synchronizes any `#anchor` cross-references to auto-numbered sections
      3. Validates and expands all `{{key:...}}`, `{{keycap:...}}`, `{{seq:...}}`,
         `{{res:...}}`, `{{screenshot:...}}`, `{{blocks:...}}`, and `{{cite:...}}` macros.
    """
    if is_sc32 is None:
        is_sc32 = "sc32" in str(file_path)
    step0 = expand_bibliography_macros(markdown, file_path=file_path, target_format=target_format)
    step1 = auto_number_headings(step0, file_path)
    step2 = sync_cross_reference_anchors(step1, file_path, is_sc32=is_sc32)
    step3 = expand_key_macros(step2, is_sc32=is_sc32, file_path=file_path, target_format=target_format)
    return step3


if __name__ == "__main__":
    from transform_and_validate_manuals import process_all_files
    process_all_files()

