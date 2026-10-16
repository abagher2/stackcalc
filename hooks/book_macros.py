"""MkDocs hook to expand validated keystroke macros and auto-number book sections."""
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT / "Tools") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "Tools"))

from book_engine import process_manual_markdown, expand_key_macros


def on_page_markdown(markdown, page, config, files, **kwargs):
    src_path = Path(config["docs_dir"]) / page.file.src_path
    rel = page.file.src_path.replace("\\", "/")
    if rel.startswith("manuals/sc32/") or rel.startswith("manuals/sc6/"):
        is_sc32 = rel.startswith("manuals/sc32/")
        return process_manual_markdown(markdown, src_path, is_sc32=is_sc32)
    elif "{{" in markdown and not rel.endswith("bestseller-rubric-and-editorial-guide.md") and not rel.endswith("critical-editorial-review-and-school-adoption.md"):
        is_sc32 = ("sc6" not in rel) and ("elementary" not in rel)
        return expand_key_macros(markdown, is_sc32=is_sc32, file_path=src_path)
    return markdown
