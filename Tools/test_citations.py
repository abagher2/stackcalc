"""Unit and regression tests for StackCalc Citation & Bibliography pipeline."""
import unittest
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT / "Tools") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "Tools"))

from book_engine import (
    get_citations_registry,
    expand_cite_macros,
    expand_bibliography_macros,
    generate_bibliography_markdown,
    scan_citation_backreferences,
    process_manual_markdown,
    REPO_ROOT as ENGINE_REPO_ROOT,
)

class TestCitationPipeline(unittest.TestCase):
    def setUp(self):
        self.registry = get_citations_registry()
        self.citations_json_path = REPO_ROOT / "docs" / "assets" / "manuals" / "citations_registry.json"
        self.bib_path = REPO_ROOT / "docs" / "assets" / "manuals" / "bibliography.bib"

    def test_registry_file_exists_and_has_required_fields(self):
        self.assertTrue(self.citations_json_path.exists())
        self.assertTrue(self.bib_path.exists())
        self.assertGreaterEqual(len(self.registry), 30)

        for cid, entry in self.registry.items():
            self.assertIn("author", entry, f"Missing author for {cid}")
            self.assertIn("year", entry, f"Missing year for {cid}")
            self.assertIn("title", entry, f"Missing title for {cid}")
            self.assertIn("annotation", entry, f"Missing annotation for {cid}")
            self.assertIn("category", entry, f"Missing category for {cid}")
            self.assertIn("volume_scope", entry, f"Missing volume_scope for {cid}")
            self.assertIn(entry["volume_scope"], ("sc32", "sc6", "both"))

    def test_bibtex_file_contains_all_registry_keys(self):
        bib_content = self.bib_path.read_text(encoding="utf-8")
        for cid in self.registry.keys():
            self.assertIn(f"{{{cid},", bib_content, f"BibTeX missing citation key @...{{{cid},")

    def test_expand_cite_single_web(self):
        md = "According to {{cite:lukasiewicz1924}}, prefix notation is parenthesis-free."
        fake_path = REPO_ROOT / "docs" / "manuals" / "sc32" / "02-rpn-stack-dynamics.md"
        expanded = expand_cite_macros(md, is_sc32=True, file_path=fake_path, target_format="web")
        self.assertIn("[Łukasiewicz, 1924]", expanded)
        self.assertIn("appendix-e-annotated-bibliography.md#cite-lukasiewicz1924", expanded)

    def test_expand_cite_single_pdf(self):
        md = "According to {{cite:lukasiewicz1924}}, prefix notation is parenthesis-free."
        fake_path = REPO_ROOT / "docs" / "manuals" / "sc32" / "02-rpn-stack-dynamics.md"
        expanded = expand_cite_macros(md, is_sc32=True, file_path=fake_path, target_format="pdf")
        self.assertEqual(expanded, "According to *(Łukasiewicz, 1924)*, prefix notation is parenthesis-free.")

    def test_expand_cite_multi(self):
        md = "Stack systems {{cite:lukasiewicz1924,burks1954}} revolutionized computing."
        fake_path = REPO_ROOT / "docs" / "manuals" / "sc32" / "02-rpn-stack-dynamics.md"
        expanded_web = expand_cite_macros(md, is_sc32=True, file_path=fake_path, target_format="web")
        self.assertIn("Łukasiewicz, 1924", expanded_web)
        self.assertIn("Burks et al., 1954", expanded_web)

        expanded_pdf = expand_cite_macros(md, is_sc32=True, file_path=fake_path, target_format="pdf")
        self.assertEqual(expanded_pdf, "Stack systems *(Łukasiewicz, 1924; Burks et al., 1954)* revolutionized computing.")

    def test_expand_cite_case_insensitive_and_whitespace(self):
        md = "Citation {{cite: LUKASIEWICZ1924 , BURKS1954 }} test."
        fake_path = REPO_ROOT / "docs" / "manuals" / "sc32" / "02-rpn-stack-dynamics.md"
        expanded_pdf = expand_cite_macros(md, is_sc32=True, file_path=fake_path, target_format="pdf")
        self.assertEqual(expanded_pdf, "Citation *(Łukasiewicz, 1924; Burks et al., 1954)* test.")

    def test_unknown_citation_raises_value_error(self):
        md = "Invalid citation {{cite:unknown_author_2099}}."
        fake_path = REPO_ROOT / "docs" / "manuals" / "sc32" / "02-rpn-stack-dynamics.md"
        with self.assertRaises(ValueError) as ctx:
            expand_cite_macros(md, is_sc32=True, file_path=fake_path, target_format="web")
        self.assertIn("unknown_author_2099", str(ctx.exception))

    def test_sc6_target_url_routing(self):
        md = "Concrete learning {{cite:bruner1966}}."
        fake_path = REPO_ROOT / "docs" / "manuals" / "sc6" / "02-rpn-for-young-learners.md"
        expanded_web = expand_cite_macros(md, is_sc32=False, file_path=fake_path, target_format="web")
        self.assertIn("appendix-c-formulas-and-conversions.md#cite-bruner1966", expanded_web)

    def test_backreferences_scanning(self):
        sc32_backrefs = scan_citation_backreferences("sc32")
        self.assertIn("lukasiewicz1924", sc32_backrefs)
        self.assertIn("Ch 02", [ref[0] for ref in sc32_backrefs["lukasiewicz1924"]])

        sc6_backrefs = scan_citation_backreferences("sc6")
        self.assertIn("bruner1966", sc6_backrefs)
        self.assertIn("Ch 02", [ref[0] for ref in sc6_backrefs["bruner1966"]])

    def test_generate_bibliography_markdown_sc32(self):
        bib_md = generate_bibliography_markdown("sc32", target_format="web")
        self.assertIn("### Foundations of Logic & Computer Architecture", bib_md)
        self.assertIn("### Complete BibTeX Catalog (StackCalc SC-32 Scientific)", bib_md)
        self.assertIn('<a id="cite-lukasiewicz1924"></a>', bib_md)
        self.assertIn("@article{lukasiewicz1924,", bib_md)

    def test_generate_bibliography_markdown_sc6(self):
        bib_md = generate_bibliography_markdown("sc6", target_format="web")
        self.assertIn("### Pedagogy, Cognitive Science & Manipulatives", bib_md)
        self.assertIn('<a id="cite-bruner1966"></a>', bib_md)
        self.assertIn("@book{bruner1966,", bib_md)

    def test_process_manual_markdown_bibliography_expansion(self):
        sc32_bib_file = REPO_ROOT / "docs" / "manuals" / "sc32" / "appendix-e-annotated-bibliography.md"
        content = sc32_bib_file.read_text(encoding="utf-8")
        processed = process_manual_markdown(content, sc32_bib_file, is_sc32=True)
        self.assertNotIn("{{bibliography:sc32}}", processed)
        self.assertIn("Jan Łukasiewicz", processed)


if __name__ == "__main__":
    unittest.main()
