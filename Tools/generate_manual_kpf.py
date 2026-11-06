#!/usr/bin/env python3
"""
Generate Kindle Print Replica (.kpf) packages and standalone Kindle Primary Front
Covers (.jpg 300 DPI RGB + .pdf) for the StackCalc Library, and package all KDP
print and Kindle deliverables into the kdp_upload directories:

  Flagship 6x9 Reference Manuals:
    - Volume I (SC-6):  sc6-elementary-manual.kpf + sc6-kindle-cover.jpg/.pdf
    - Volume II (SC-32): sc32-scientific-manual.kpf + sc32-kindle-cover.jpg/.pdf

  US Letter (8.5x11) Curriculum Books (Book 1, 2A, 2B, 3, 4, 5):
    - Book-1-Teaching-with-the-Stack-Kindle.kpf + Kindle-Cover.jpg/.pdf
    - Book-2A-Early-Elementary-Math-Lab-Kindle.kpf + Kindle-Cover.jpg/.pdf
    - Book-2B-Upper-Elementary-Math-Lab-Kindle.kpf + Kindle-Cover.jpg/.pdf
    - Book-3-Middle-School-Math-Lab-Kindle.kpf + Kindle-Cover.jpg/.pdf
    - Book-4-High-School-and-STEM-Lab-Kindle.kpf + Kindle-Cover.jpg/.pdf
    - Book-5-Stack-Speed-and-Fluency-Kindle.kpf + Kindle-Cover.jpg/.pdf

Uses Kindle Create's native KAF/KDF engine (EpubToKFXConverter-4.0.jar +
libKAFJNI-shared.dylib) to build genuine SQLite KDF databases (book.kdf) with
fixed-layout PDF page templates, PageList navigation, hierarchical TOC from the
PDF bookmark tree, and bcRawMedia PDF stream resources (res/rsrc0), packaged
with a Kindle Create book.kcb manifest into a .kpf archive ready for Amazon KDP.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
import zipfile
from pathlib import Path
from typing import Any

from pypdf import PdfReader

REPO_ROOT = Path(__file__).resolve().parent.parent
WATCH_CALC_ROOT = (
    REPO_ROOT
    if (REPO_ROOT / "documentation" / "manuals").exists()
    else (REPO_ROOT.parent / "watch-calc-32")
)
STACKCALC_ROOT = (
    REPO_ROOT
    if (REPO_ROOT / "docs").exists()
    else (REPO_ROOT.parent / "stackcalc")
)

MANUAL_OUTPUT_DIR = WATCH_CALC_ROOT / "documentation" / "manuals" / "output"
WEBSITE_OUTPUT_DIR = WATCH_CALC_ROOT / "Website" / "docs" / "manuals" / "output"
STACKCALC_MANUAL_OUTPUT_DIR = STACKCALC_ROOT / "docs" / "manuals" / "output"
STACKCALC_DOWNLOADS_MANUAL_DIR = STACKCALC_ROOT / "docs" / "downloads" / "manuals"
EDUCATION_PDF_DIR = WATCH_CALC_ROOT / "Education" / "output" / "pdf"
EDUCATION_KDP_READY_DIR = EDUCATION_PDF_DIR / "kdp_upload_ready"

KDP_UPLOAD_DIRS = [
    MANUAL_OUTPUT_DIR / "kdp_upload",
    STACKCALC_MANUAL_OUTPUT_DIR / "kdp_upload",
    EDUCATION_KDP_READY_DIR,
    EDUCATION_PDF_DIR / "kdp_upload",
]

KINDLE_CREATE_CONVGEN = Path("/Applications/Kindle Create.app/Contents/ConvGen")
KAF_JAR = KINDLE_CREATE_CONVGEN / "lib" / "EpubToKFXConverter-4.0.jar"
KAF_SHARED_LIBS = KINDLE_CREATE_CONVGEN / "lib" / "shared_libs"

MANUALS = [
    {
        "key": "sc6",
        "is_sc32": False,
        "pdf": MANUAL_OUTPUT_DIR / "sc6-elementary-manual.pdf",
        "hardcover_pdf": MANUAL_OUTPUT_DIR / "sc6-elementary-manual-hardcover.pdf",
        "paperback_cover": MANUAL_OUTPUT_DIR / "sc6-full-wrap-cover.pdf",
        "hardcover_cover": MANUAL_OUTPUT_DIR / "sc6-hardcover-wrap-cover.pdf",
        "kpf": MANUAL_OUTPUT_DIR / "sc6-elementary-manual.kpf",
        "kindle_cover_pdf": MANUAL_OUTPUT_DIR / "sc6-kindle-cover.pdf",
        "kindle_cover_jpg": MANUAL_OUTPUT_DIR / "sc6-kindle-cover.jpg",
        "kdp_prefix": "Volume-I-SC6-From-Blocks-to-the-Stack",
        "title": "From Blocks to the Stack: How Hands-On Blocks Make Numbers Click",
        "author": "StackCalc",
    },
    {
        "key": "sc32",
        "is_sc32": True,
        "manual_kind": "sc32",
        "pdf": MANUAL_OUTPUT_DIR / "sc32-scientific-manual.pdf",
        "hardcover_pdf": MANUAL_OUTPUT_DIR / "sc32-scientific-manual-hardcover.pdf",
        "paperback_cover": MANUAL_OUTPUT_DIR / "sc32-full-wrap-cover.pdf",
        "hardcover_cover": MANUAL_OUTPUT_DIR / "sc32-hardcover-wrap-cover.pdf",
        "kpf": MANUAL_OUTPUT_DIR / "sc32-scientific-manual.kpf",
        "kindle_cover_pdf": MANUAL_OUTPUT_DIR / "sc32-kindle-cover.pdf",
        "kindle_cover_jpg": MANUAL_OUTPUT_DIR / "sc32-kindle-cover.jpg",
        "kdp_prefix": "Volume-II-SC32-Thinking-in-the-Stack",
        "title": "Thinking in the Stack: The Art of Solving Equations from the Inside Out",
        "author": "StackCalc",
    },
    {
        "key": "domains",
        "is_sc32": True,
        "manual_kind": "domains",
        "pdf": MANUAL_OUTPUT_DIR / "sc-domains-manual.pdf",
        "hardcover_pdf": MANUAL_OUTPUT_DIR / "sc-domains-manual-hardcover.pdf",
        "paperback_cover": MANUAL_OUTPUT_DIR / "sc-domains-full-wrap-cover.pdf",
        "hardcover_cover": MANUAL_OUTPUT_DIR / "sc-domains-hardcover-wrap-cover.pdf",
        "kpf": MANUAL_OUTPUT_DIR / "sc-domains-manual.kpf",
        "kindle_cover_pdf": MANUAL_OUTPUT_DIR / "sc-domains-kindle-cover.pdf",
        "kindle_cover_jpg": MANUAL_OUTPUT_DIR / "sc-domains-kindle-cover.jpg",
        "kdp_prefix": "Volume-III-SC-Domains-The-Stack-in-the-Field",
        "title": "The Stack in the Field: When Mathematics Meets the Physical Trades",
        "author": "StackCalc",
    },
]

CURRICULUM_BOOKS = [
    {
        "key": "book1",
        "cover_spec_key": "teacher_guide",
        "prefix": "Book-1-Teaching-with-the-Stack",
        "pdf": EDUCATION_KDP_READY_DIR / "Book-1-Teaching-with-the-Stack-Interior-46pp.pdf",
        "fallback_pdf": EDUCATION_PDF_DIR / "teacher-curriculum-guide-letter.pdf",
        "kdp_cover": EDUCATION_KDP_READY_DIR / "Book-1-Teaching-with-the-Stack-KDP-Cover.pdf",
        "fallback_cover": EDUCATION_PDF_DIR / "teacher-curriculum-guide-kdp-cover.pdf",
        "kpf": EDUCATION_KDP_READY_DIR / "Book-1-Teaching-with-the-Stack-Kindle.kpf",
        "kindle_cover_pdf": EDUCATION_KDP_READY_DIR / "Book-1-Teaching-with-the-Stack-Kindle-Cover.pdf",
        "kindle_cover_jpg": EDUCATION_KDP_READY_DIR / "Book-1-Teaching-with-the-Stack-Kindle-Cover.jpg",
        "title": "Teaching with the Stack: A Practical Concept-First Teacher & Homeschool Guide",
        "author": "StackCalc",
    },
    {
        "key": "book2a",
        "cover_spec_key": "early_elementary_lab",
        "prefix": "Book-2A-Early-Elementary-Math-Lab",
        "pdf": EDUCATION_KDP_READY_DIR / "Book-2A-Early-Elementary-Math-Lab-Interior-128pp.pdf",
        "fallback_pdf": EDUCATION_PDF_DIR / "early-elementary-lab-workbook-letter.pdf",
        "kdp_cover": EDUCATION_KDP_READY_DIR / "Book-2A-Early-Elementary-Math-Lab-KDP-Cover.pdf",
        "fallback_cover": EDUCATION_PDF_DIR / "early-elementary-lab-workbook-kdp-cover.pdf",
        "kpf": EDUCATION_KDP_READY_DIR / "Book-2A-Early-Elementary-Math-Lab-Kindle.kpf",
        "kindle_cover_pdf": EDUCATION_KDP_READY_DIR / "Book-2A-Early-Elementary-Math-Lab-Kindle-Cover.pdf",
        "kindle_cover_jpg": EDUCATION_KDP_READY_DIR / "Book-2A-Early-Elementary-Math-Lab-Kindle-Cover.jpg",
        "title": "Early Elementary Math Lab (Grades K-2)",
        "author": "StackCalc",
    },
    {
        "key": "book2b",
        "cover_spec_key": "upper_elementary_lab",
        "prefix": "Book-2B-Upper-Elementary-Math-Lab",
        "pdf": EDUCATION_KDP_READY_DIR / "Book-2B-Upper-Elementary-Math-Lab-Interior-128pp.pdf",
        "fallback_pdf": EDUCATION_PDF_DIR / "upper-elementary-lab-workbook-letter.pdf",
        "kdp_cover": EDUCATION_KDP_READY_DIR / "Book-2B-Upper-Elementary-Math-Lab-KDP-Cover.pdf",
        "fallback_cover": EDUCATION_PDF_DIR / "upper-elementary-lab-workbook-kdp-cover.pdf",
        "kpf": EDUCATION_KDP_READY_DIR / "Book-2B-Upper-Elementary-Math-Lab-Kindle.kpf",
        "kindle_cover_pdf": EDUCATION_KDP_READY_DIR / "Book-2B-Upper-Elementary-Math-Lab-Kindle-Cover.pdf",
        "kindle_cover_jpg": EDUCATION_KDP_READY_DIR / "Book-2B-Upper-Elementary-Math-Lab-Kindle-Cover.jpg",
        "title": "Upper Elementary Math Lab (Grades 3-5)",
        "author": "StackCalc",
    },
    {
        "key": "book3",
        "cover_spec_key": "big_ideas",
        "prefix": "Book-3-Middle-School-Math-Lab",
        "pdf": EDUCATION_KDP_READY_DIR / "Book-3-Middle-School-Math-Lab-Interior-128pp.pdf",
        "fallback_pdf": STACKCALC_ROOT / "docs" / "downloads" / "worksheets" / "bigideas_middle_school_sc6_daily_student_workbook.pdf",
        "kdp_cover": EDUCATION_KDP_READY_DIR / "Book-3-Middle-School-Math-Lab-KDP-Cover.pdf",
        "fallback_cover": STACKCALC_ROOT / "docs" / "downloads" / "worksheets" / "bigideas_middle_school_sc6_workbook_kdp_cover.pdf",
        "kpf": EDUCATION_KDP_READY_DIR / "Book-3-Middle-School-Math-Lab-Kindle.kpf",
        "kindle_cover_pdf": EDUCATION_KDP_READY_DIR / "Book-3-Middle-School-Math-Lab-Kindle-Cover.pdf",
        "kindle_cover_jpg": EDUCATION_KDP_READY_DIR / "Book-3-Middle-School-Math-Lab-Kindle-Cover.jpg",
        "title": "Middle School Math Lab (Grades 6-8)",
        "author": "StackCalc",
    },
    {
        "key": "book4",
        "cover_spec_key": "high_school_lab",
        "prefix": "Book-4-High-School-and-STEM-Lab",
        "pdf": EDUCATION_KDP_READY_DIR / "Book-4-High-School-and-STEM-Lab-Interior-128pp.pdf",
        "fallback_pdf": EDUCATION_PDF_DIR / "high-school-lab-workbook-letter.pdf",
        "kdp_cover": EDUCATION_KDP_READY_DIR / "Book-4-High-School-and-STEM-Lab-KDP-Cover.pdf",
        "fallback_cover": EDUCATION_PDF_DIR / "high-school-lab-workbook-kdp-cover.pdf",
        "kpf": EDUCATION_KDP_READY_DIR / "Book-4-High-School-and-STEM-Lab-Kindle.kpf",
        "kindle_cover_pdf": EDUCATION_KDP_READY_DIR / "Book-4-High-School-and-STEM-Lab-Kindle-Cover.pdf",
        "kindle_cover_jpg": EDUCATION_KDP_READY_DIR / "Book-4-High-School-and-STEM-Lab-Kindle-Cover.jpg",
        "title": "High School & STEM Lab (Grades 9-12 & AP)",
        "author": "StackCalc",
    },
    {
        "key": "book5",
        "cover_spec_key": "proficiency_trials",
        "prefix": "Book-5-Stack-Speed-and-Fluency",
        "pdf": EDUCATION_KDP_READY_DIR / "Book-5-Stack-Speed-and-Fluency-Interior-128pp.pdf",
        "fallback_pdf": EDUCATION_PDF_DIR / "student-proficiency-trials-letter.pdf",
        "kdp_cover": EDUCATION_KDP_READY_DIR / "Book-5-Stack-Speed-and-Fluency-KDP-Cover.pdf",
        "fallback_cover": EDUCATION_PDF_DIR / "student-proficiency-trials-kdp-cover.pdf",
        "kpf": EDUCATION_KDP_READY_DIR / "Book-5-Stack-Speed-and-Fluency-Kindle.kpf",
        "kindle_cover_pdf": EDUCATION_KDP_READY_DIR / "Book-5-Stack-Speed-and-Fluency-Kindle-Cover.pdf",
        "kindle_cover_jpg": EDUCATION_KDP_READY_DIR / "Book-5-Stack-Speed-and-Fluency-Kindle-Cover.jpg",
        "title": "Stack Speed & Fluency: 15 Speed Lessons & 180 Progressive Practice Tests",
        "author": "StackCalc",
    },
]

KAF_EXCEPTION_JAVA = """\
package com.amazon.kaf.exception;

public class KAFException extends Exception {
    public KAFException() {
        super();
    }

    public KAFException(String message) {
        super(message);
    }

    public KAFException(String message, Throwable cause) {
        super(message, cause);
    }

    public KAFException(Throwable cause) {
        super(cause);
    }
}
"""

KDF_BUILDER_JAVA = """\
import com.amazon.kaf.jni.adapters.c;
import com.amazon.kaf.jni.adapters.PageTemplate;
import com.amazon.kaf.jni.adapters.PropertyName;
import com.amazon.kaf.jni.adapters.JNIHandle;
import com.amazon.kaf.c.*;
import com.amazon.kaf.util.PropertyNameUtil;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.lang.reflect.Method;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

public class KDFPrintReplicaBuilder {
    static class TocEntry {
        int depth;
        int pageIndex;
        String title;
    }

    public static void main(String[] args) throws Exception {
        if (args.length < 7) {
            throw new IllegalArgumentException(
                "Usage: KDFPrintReplicaBuilder <workDir> <pdfPath> <numPages> <widthPt> <heightPt> <tocTsvPath> <title> <author>"
            );
        }
        String workDir = args[0];
        String pdfPath = args[1];
        int numPages = Integer.parseInt(args[2]);
        int widthPt = Math.round(Float.parseFloat(args[3]));
        int heightPt = Math.round(Float.parseFloat(args[4]));
        float widthPtFloat = Float.parseFloat(args[3]);
        float heightPtFloat = Float.parseFloat(args[4]);
        String tocTsvPath = args[5];
        String bookTitle = args[6];
        String bookAuthor = args.length > 7 ? args[7] : "StackCalc";

        List<TocEntry> tocEntries = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(
                new InputStreamReader(new FileInputStream(tocTsvPath), StandardCharsets.UTF_8))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (line.trim().isEmpty()) continue;
                String[] parts = line.split("\\t", 3);
                if (parts.length == 3) {
                    TocEntry entry = new TocEntry();
                    entry.depth = Integer.parseInt(parts[0]);
                    entry.pageIndex = Integer.parseInt(parts[1]);
                    entry.title = parts[2];
                    tocEntries.add(entry);
                }
            }
        }

        Method getHandleMethod = JNIHandle.class.getDeclaredMethod("getHandle");
        getHandleMethod.setAccessible(true);
        Method addCondMethod = PageTemplate.class.getDeclaredMethod("addNativeconditionalProperty", long.class);
        addCondMethod.setAccessible(true);

        c kaf = c.a();
        PropertyNameUtil.a();
        m bookFactory = kaf.b();
        bookFactory.b();
        an storageFactory = kaf.c();
        x storage = storageFactory.a(workDir, "resources", aB.R.SQLITE);
        y book = bookFactory.a(storage);
        S objFactory = book.b();
        aa propMgr = book.c();
        l bookContent = book.d();
        ad readingOrder = book.e();

        // Configure DocumentData for Print Replica (Fixed Layout with pan/zoom)
        z docData = bookContent.a();
        docData.a(PropertyNameUtil.a(581), propMgr.b(441L)); // pan_zoom = enabled
        docData.a(PropertyNameUtil.a(216), propMgr.b(220L)); // binding_direction = binding_direction_left
        docData.a(PropertyNameUtil.a(230), propMgr.a(heightPt, aB.Y.kUnits_Point)); // target_WideDimension
        docData.a(PropertyNameUtil.a(231), propMgr.a(widthPt, aB.Y.kUnits_Point));  // target_NarrowDimension
        docData.a(propMgr.a(b.SpacingPercentBase), propMgr.a(b.Width, book));       // spacing_percent_base = width

        // Set book title & author metadata in kindle_title_metadata
        book.a("kindle_title_metadata", new PropertyName("title"), propMgr.a(bookTitle, book));
        book.a("kindle_title_metadata", new PropertyName("author"), propMgr.a(bookAuthor, book));
        book.a("kindle_title_metadata", new PropertyName("language"), propMgr.a("en", book));

        // Populate Kindle Create 1.105.0.0 audit, ebook, and capability metadata categories
        book.a("kindle_audit_metadata", propMgr.a("file_creator"), propMgr.a("KC", book));
        book.a("kindle_audit_metadata", propMgr.a("creator_version"), propMgr.a("1.105.0.0", book));
        book.a("kindle_ebook_metadata", propMgr.a("selection"), propMgr.a("enabled", book));
        book.a("kindle_ebook_metadata", propMgr.a("nested_span"), propMgr.a("enabled", book));
        book.a("kindle_ebook_metadata", propMgr.a("multipage_selection"), propMgr.a("enabled", book));
        book.a("kindle_ebook_metadata", propMgr.a("book_orientation_lock"), propMgr.a("none", book));
        book.a("kindle_ebook_metadata", propMgr.a("user_visible_labeling"), propMgr.a("disabled", book));
        book.a("kindle_capability_metadata", propMgr.a("graphical_highlights"), propMgr.a(1L));
        book.a("kindle_capability_metadata", propMgr.a("yj_fixed_layout"), propMgr.a(1L));
        book.a("kindle_capability_metadata", propMgr.a("yj_textbook"), propMgr.a(1L));

        // Insert PDF resource stream into resources/res/rsrc0 and register bcRawMedia fragment
        String relResPath = objFactory.c(pdfPath);

        long[] outerContIds = new long[numPages];
        for (int pageIdx = 0; pageIdx < numPages; pageIdx++) {
            // 1. Create Section (creates default portrait PageTemplate + Storyline)
            aj section = objFactory.b();
            List<U> pts = section.h();
            U pt1 = pts.get(0);
            s ptCont1 = pt1.b();
            ptCont1.a(PropertyNameUtil.a(156), propMgr.b(323L)); // layout = vertical (323)
            ptCont1.a(PropertyNameUtil.a(159), propMgr.b(270L)); // type = container (270)
            ptCont1.a(PropertyNameUtil.a(56), propMgr.a(100, aB.Y.kUnits_Percent)); // width = 100%
            ptCont1.a(PropertyNameUtil.a(66), propMgr.a(100, aB.Y.kUnits_Percent)); // fixed_width = 100%
            ac portraitCond = propMgr.b();
            portraitCond.k().a(propMgr.b(526L)); // isPortrait (526)
            addCondMethod.invoke(pt1, (Long) getHandleMethod.invoke(portraitCond));

            ao storyline = pt1.a();

            // 2. Create landscape PageTemplate sharing the same Storyline
            U pt2 = objFactory.a();
            s ptCont2 = pt2.b();
            ptCont2.a(PropertyNameUtil.a(156), propMgr.b(325L)); // layout = overflow (325)
            ptCont2.a(PropertyNameUtil.a(159), propMgr.b(270L)); // type = container (270)
            ac landscapeCond = propMgr.b();
            landscapeCond.k().a(propMgr.b(525L)); // isLandscape (525)
            addCondMethod.invoke(pt2, (Long) getHandleMethod.invoke(landscapeCond));
            pt2.a(storyline);
            section.a(pt2);

            // 3. Create outer scale_fit Container (7200 DPI bounds per YJOPFrameCreationTask::updateScaleFitContainerBoundsTo7200DPI)
            s outerCont = objFactory.e();
            outerCont.a(PropertyNameUtil.a(156), propMgr.b(326L)); // layout = scale_fit (326)
            outerCont.a(PropertyNameUtil.a(66), propMgr.a((long)(widthPt * 100), aB.Y.kUnits_Point));  // fixed_width (7200 DPI)
            outerCont.a(PropertyNameUtil.a(67), propMgr.a((long)(heightPt * 100), aB.Y.kUnits_Point)); // fixed_height (7200 DPI)
            outerCont.a(PropertyNameUtil.a(475), propMgr.b(472L)); // fit_text = force (472)

            // 4. Create ImageContainer inside outerCont
            F imgCont = objFactory.d();
            s imgAsCont = imgCont.q();
            outerCont.a(imgAsCont);
            imgAsCont.a(PropertyNameUtil.a(57), propMgr.a(100, aB.Y.kUnits_Percent)); // height = 100%
            imgAsCont.a(PropertyNameUtil.a(56), propMgr.a(100, aB.Y.kUnits_Percent)); // width = 100%

            // 5. Create PDF ExternalResource for this page
            ae res = objFactory.j();
            res.a(PropertyNameUtil.a(165), propMgr.a(relResPath, book)); // location = "rsrc0"
            res.a(PropertyNameUtil.a(422), propMgr.a(widthPtFloat));     // resource_width
            res.a(PropertyNameUtil.a(423), propMgr.a(heightPtFloat));    // resource_height
            res.a(PropertyNameUtil.a(161), propMgr.b(565L));             // format = pdf (565)
            res.a(PropertyNameUtil.a(564), propMgr.a((long) pageIdx));   // page_index (0-based)
            res.a(PropertyNameUtil.a(48), propMgr.a(0.0f));              // margin_left
            res.a(PropertyNameUtil.a(50), propMgr.a(0.0f));              // margin_right
            res.a(PropertyNameUtil.a(47), propMgr.a(0.0f));              // margin_top
            res.a(PropertyNameUtil.a(49), propMgr.a(0.0f));              // margin_bottom
            imgCont.a(res);

            // 6. Set float = center on outerCont and attach to storyline & readingOrder
            outerCont.a(PropertyNameUtil.a(140), propMgr.b(320L)); // float = center (320)
            storyline.a(outerCont);
            outerContIds[pageIdx] = outerCont.a();
            readingOrder.c(section);
        }

        // 7. Build PageList Navigation (1-based page numbers)
        P navProvider = book.c(readingOrder.d());
        O pageListNav = objFactory.a(aB.H.PageList);
        pageListNav.c();
        for (int idx = 0; idx < numPages; idx++) {
            T offset = objFactory.a(0L);
            Y pos = objFactory.a(outerContIds[idx], offset);
            Q navUnit = objFactory.a(pos);
            navUnit.a(PropertyNameUtil.a(244), propMgr.a(String.valueOf(idx + 1), book));
            pageListNav.a(navUnit);
        }
        navProvider.a(pageListNav);

        // 8. Build Hierarchical Table of Contents Navigation from PDF Bookmarks
        O tocNav = objFactory.a(aB.H.TOC);
        tocNav.c();
        List<Q> parentStack = new ArrayList<>();
        for (TocEntry entry : tocEntries) {
            int pageIdx = Math.max(0, Math.min(numPages - 1, entry.pageIndex));
            T offset = objFactory.a(0L);
            Y pos = objFactory.a(outerContIds[pageIdx], offset);
            Q navUnit = objFactory.a(pos);
            navUnit.a(PropertyNameUtil.a(244), propMgr.a(entry.title, book));

            int depth = Math.max(0, entry.depth);
            while (parentStack.size() > depth) {
                parentStack.remove(parentStack.size() - 1);
            }
            if (parentStack.isEmpty()) {
                tocNav.a(navUnit);
            } else {
                parentStack.get(parentStack.size() - 1).a(navUnit);
            }
            parentStack.add(navUnit);
        }
        navProvider.a(tocNav);

        // 9. Configure Print Replica content features (matching Kindle Create YJOPFrameCreationTask)
        try { book.a("com.amazon.yjconversion", "yj_audio"); } catch (Exception ignored) {}
        try { book.a("com.amazon.yjconversion", "yj_video"); } catch (Exception ignored) {}
        try { book.a("com.amazon.yjconversion", "yj_interactive_image"); } catch (Exception ignored) {}
        book.a("com.amazon.yjconversion", "yj_textbook", 1L, 0L);
        book.a("com.amazon.yjconversion", "yj_fixed_layout", 1L, 0L);
        book.a("com.amazon.yjconversion", "yj_low_vision", 1L, 0L);

        // 10. Save & close SQLite KDF database
        book.a(true, true);
        ((JNIHandle) book).dispose();
        ((JNIHandle) storage).dispose();
    }
}
"""


def extract_pdf_outline(
    reader: PdfReader, default_title: str, pdf_path: Path | None = None
) -> list[tuple[int, int, str]]:
    """
    Return a flat list of (depth, 0_based_page_index, title) from a PdfReader outline,
    or from a sidecar .outline.json if /Outlines was already stripped from the PDF.
    Falls back to a top-level entry pointing at page 0 if neither has outline bookmarks.
    """
    entries: list[tuple[int, int, str]] = []

    def walk(items: list[Any], depth: int) -> None:
        for item in items:
            if isinstance(item, list):
                walk(item, depth + 1)
            else:
                try:
                    page_idx = reader.get_destination_page_number(item)
                except Exception:
                    page_idx = 0
                if page_idx is None:
                    page_idx = 0
                title = " ".join(str(item.title).replace("\t", " ").split())
                if title:
                    entries.append((depth, int(page_idx), title))

    if reader.outline:
        walk(reader.outline, 0)
    elif pdf_path is not None:
        sidecar = pdf_path.with_suffix(".outline.json")
        if sidecar.is_file():
            try:
                raw_list = json.loads(sidecar.read_text(encoding="utf-8"))
                for row in raw_list:
                    if isinstance(row, list) and len(row) == 3:
                        entries.append((int(row[0]), int(row[1]), str(row[2])))
            except Exception:
                pass
    if not entries and default_title:
        entries.append((0, 0, default_title))
    return entries


def md5_file(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build_kcb_manifest(kdf_md5: str, rsrc0_md5: str) -> str:
    """
    Build the Kindle Create 1.105.0.0 book.kcb JSON manifest for a Print Replica KPF/KCB package.
    Matches Kindle Create's BookState::toJson, KCBManifest::save, and KPFExporter::exportKpf:
      - book_input_type = 1 (PDF)
      - book_target_type = 1 (Print Replica / Fixed Layout)
      - book_reading_direction = 1 (Left-to-Right)
      - book_fl_type = 0, book_reading_option = 0, book_virtual_panelmovement = 0
      - metadata.book_path = "resources"
      - tool_data.cache_path = "resources/.cache"
    """
    manifest = {
        "book_state": {
            "book_fl_type": 0,
            "book_input_type": 1,
            "book_reading_direction": 1,
            "book_reading_option": 0,
            "book_target_type": 1,
            "book_virtual_panelmovement": 0,
        },
        "content_hash": {
            "resources/book.kdf": kdf_md5,
            "resources/res/rsrc0": rsrc0_md5,
        },
        "metadata": {
            "book_path": "resources",
            "edited_tool_versions": ["1.105.0.0"],
            "format": "yj",
            "global_styling": True,
            "id": str(uuid.uuid4()),
            "log_path": "",
            "platform": "mac",
            "quality_report": "",
            "source_path": [""],
            "tool_name": "KC",
            "tool_version": "1.105.0.0",
        },
        "tool_data": {
            "cache_path": "resources/.cache",
            "created_on": "2026-Nov-05 00:30:00",
            "last_modified_time": "2026-Nov-05 00:30:00",
            "link_extract_choice": False,
            "link_notification_preference": True,
        },
    }
    return json.dumps(manifest, indent=3)


def copy_kcb_project_dir(src_kcb_dir: Path, dst_kcb_dir: Path) -> Path:
    """
    Copy a Kindle Create project directory (<Name>_KCB/) to dst_kcb_dir and ensure
    its primary .kcb file matches <dst_kcb_dir.name>.kcb as required by Workspace::open/save.
    """
    if dst_kcb_dir.exists():
        shutil.rmtree(dst_kcb_dir)
    shutil.copytree(src_kcb_dir, dst_kcb_dir)

    src_primary = dst_kcb_dir / f"{src_kcb_dir.name}.kcb"
    dst_primary = dst_kcb_dir / f"{dst_kcb_dir.name}.kcb"
    if src_primary.is_file() and src_primary != dst_primary:
        shutil.move(str(src_primary), str(dst_primary))
    return dst_primary


def verify_kpf(kpf_path: Path, expected_pages: int) -> dict[str, Any]:
    """
    Validate a generated .kpf file's ZIP structure, BookState fields, MD5 hashes in book.kcb,
    and SQLite KDF fragments in resources/book.kdf.
    """
    if not kpf_path.is_file():
        raise RuntimeError(f"Missing KPF output: {kpf_path}")

    with zipfile.ZipFile(kpf_path, "r") as zf:
        names = zf.namelist()
        expected_names = ["resources/book.kdf", "resources/res/rsrc0", "book.kcb"]
        if names != expected_names:
            raise RuntimeError(
                f"{kpf_path.name}: unexpected ZIP entries {names} (expected {expected_names})"
            )
        kcb_info = zf.getinfo("book.kcb")
        if kcb_info.compress_type != zipfile.ZIP_STORED:
            raise RuntimeError(f"{kpf_path.name}: book.kcb must use ZIP_STORED")

        kdf_bytes = zf.read("resources/book.kdf")
        rsrc0_bytes = zf.read("resources/res/rsrc0")
        kcb_data = json.loads(zf.read("book.kcb").decode("utf-8"))

    book_state = kcb_data.get("book_state", {})
    if (
        book_state.get("book_input_type") != 1
        or book_state.get("book_target_type") != 1
        or book_state.get("book_reading_direction") != 1
    ):
        raise RuntimeError(
            f"{kpf_path.name}: invalid Print Replica book_state in book.kcb: {book_state}"
        )
    if kcb_data.get("metadata", {}).get("book_path") != "resources":
        raise RuntimeError(
            f"{kpf_path.name}: metadata.book_path must be 'resources'"
        )

    kdf_md5 = hashlib.md5(kdf_bytes).hexdigest()
    rsrc0_md5 = hashlib.md5(rsrc0_bytes).hexdigest()
    if kcb_data["content_hash"].get("resources/book.kdf") != kdf_md5:
        raise RuntimeError(f"{kpf_path.name}: resources/book.kdf MD5 mismatch in book.kcb")
    if kcb_data["content_hash"].get("resources/res/rsrc0") != rsrc0_md5:
        raise RuntimeError(f"{kpf_path.name}: resources/res/rsrc0 MD5 mismatch in book.kcb")

    if not kdf_bytes.startswith(b"SQLite format 3\x00"):
        raise RuntimeError(f"{kpf_path.name}: resources/book.kdf is not a SQLite3 database")
    if not rsrc0_bytes.startswith(b"%PDF-"):
        raise RuntimeError(f"{kpf_path.name}: resources/res/rsrc0 is not a PDF stream")

    for required_marker in [
        b"document_data",
        b"book_metadata",
        b"kindle_audit_metadata",
        b"kindle_ebook_metadata",
        b"kindle_capability_metadata",
        b"book_navigation",
        b"content_features",
        b"yj_textbook",
        b"yj_fixed_layout",
        b"yj_low_vision",
        b"bcRawMedia",
        b"res/rsrc0",
    ]:
        if required_marker not in kdf_bytes:
            raise RuntimeError(
                f"{kpf_path.name}: resources/book.kdf missing required KDF marker {required_marker!r}"
            )

    section_count = len(set(re.findall(rb"(c[0-9A-Za-z]+-spm)blob", kdf_bytes)))
    if section_count != expected_pages:
        raise RuntimeError(
            f"{kpf_path.name}: expected {expected_pages} section_position_id_map entries, found {section_count}"
        )

    return {
        "kpf_size_bytes": kpf_path.stat().st_size,
        "kdf_size_bytes": len(kdf_bytes),
        "pdf_size_bytes": len(rsrc0_bytes),
        "sections": section_count,
        "kdf_md5": kdf_md5,
        "rsrc0_md5": rsrc0_md5,
    }


def sanitize_pdf_file(pdf_path: Path) -> None:
    """
    Strip non-visual PDF metadata (/Info, /Outlines, /Names, /Dests, /PageLabels, /StructTreeRoot,
    /MarkInfo, /Metadata, /OCProperties, /PieceInfo, /PageMode), page /Annots, and unused
    unembedded Type 1 Helvetica (/F1) font entries before packaging into KPF/KCB.
    Preserves any existing /Outlines to a .outline.json sidecar before stripping.
    """
    from pypdf import PdfWriter
    from pypdf.generic import NameObject

    try:
        pre_reader = PdfReader(str(pdf_path))
        if pre_reader.outline:
            extracted = extract_pdf_outline(pre_reader, default_title="")
            if extracted:
                sidecar = pdf_path.with_suffix(".outline.json")
                sidecar.write_text(
                    json.dumps([[d, p, t] for d, p, t in extracted], ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )
    except Exception:
        pass

    writer = PdfWriter(clone_from=str(pdf_path))
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

    with pdf_path.open("wb") as f_out:
        writer.write(f_out)


def build_kpf_package(
    key: str,
    pdf_path: Path,
    kpf_path: Path,
    title: str,
    author: str,
    java_build_dir: Path,
) -> dict[str, Any]:
    if not pdf_path.is_file():
        raise FileNotFoundError(f"Source PDF not found for {key}: {pdf_path}")

    sanitize_pdf_file(pdf_path)
    reader = PdfReader(str(pdf_path))
    num_pages = len(reader.pages)
    width_pt = float(reader.pages[0].mediabox.width)
    height_pt = float(reader.pages[0].mediabox.height)
    toc_entries = extract_pdf_outline(reader, default_title=title, pdf_path=pdf_path)

    print(
        f"[{key.upper()}] Building KPF & KCB from {pdf_path.name}: "
        f"{num_pages} pages ({width_pt:.0f}x{height_pt:.0f} pt), {len(toc_entries)} TOC entries..."
    )

    with tempfile.TemporaryDirectory(prefix=f"kpf_{key}_") as tmp_dir_str:
        tmp_dir = Path(tmp_dir_str)
        toc_tsv = tmp_dir / "toc.tsv"
        with toc_tsv.open("w", encoding="utf-8") as f:
            for depth, page_idx, entry_title in toc_entries:
                f.write(f"{depth}\t{page_idx}\t{entry_title}\n")

        cmd = [
            "java",
            f"-Djava.library.path={KAF_SHARED_LIBS}",
            "-cp",
            f"{KAF_JAR}{os.pathsep}{java_build_dir}",
            "KDFPrintReplicaBuilder",
            str(tmp_dir),
            str(pdf_path),
            str(num_pages),
            str(width_pt),
            str(height_pt),
            str(toc_tsv),
            title,
            author,
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            raise RuntimeError(
                f"KDFPrintReplicaBuilder failed for {key} (exit {proc.returncode}):\n"
                f"STDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
            )

        resources_dir = tmp_dir / "resources"
        book_kdf = resources_dir / "book.kdf"
        rsrc0 = resources_dir / "res" / "rsrc0"
        if not book_kdf.is_file() or not rsrc0.is_file():
            raise RuntimeError(
                f"Expected resources/book.kdf and resources/res/rsrc0 in {resources_dir}"
            )

        kdf_md5 = md5_file(book_kdf)
        rsrc0_md5 = md5_file(rsrc0)
        kcb_content = build_kcb_manifest(kdf_md5, rsrc0_md5)

        kpf_path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(kpf_path, "w") as zf:
            zf.write(book_kdf, "resources/book.kdf", compress_type=zipfile.ZIP_DEFLATED)
            zf.write(rsrc0, "resources/res/rsrc0", compress_type=zipfile.ZIP_DEFLATED)
            zf.writestr(
                zipfile.ZipInfo("book.kcb"),
                kcb_content.encode("utf-8"),
                compress_type=zipfile.ZIP_STORED,
            )

        # Also materialize the complete Kindle Create project directory (<stem>_KCB/)
        # so the project can be opened directly in Kindle Create via <stem>_KCB/<stem>_KCB.kcb
        kcb_project_dir = kpf_path.parent / f"{kpf_path.stem}_KCB"
        if kcb_project_dir.exists():
            shutil.rmtree(kcb_project_dir)
        (kcb_project_dir / "resources" / "res").mkdir(parents=True, exist_ok=True)
        (kcb_project_dir / "resources" / ".cache").mkdir(parents=True, exist_ok=True)
        shutil.copy2(book_kdf, kcb_project_dir / "resources" / "book.kdf")
        shutil.copy2(rsrc0, kcb_project_dir / "resources" / "res" / "rsrc0")
        kcb_file = kcb_project_dir / f"{kcb_project_dir.name}.kcb"
        kcb_file.write_text(kcb_content, encoding="utf-8")

    stats = verify_kpf(kpf_path, expected_pages=num_pages)
    stats["kcb_project_dir"] = kcb_project_dir
    stats["kcb_file"] = kcb_file
    print(
        f"[{key.upper()}] Verified {kpf_path.name} + {kcb_file.relative_to(kpf_path.parent)}: "
        f"{stats['kpf_size_bytes'] / (1024 * 1024):.2f} MB "
        f"(book.kdf: {stats['kdf_size_bytes'] / 1024:.1f} KB, "
        f"res/rsrc0: {stats['pdf_size_bytes'] / (1024 * 1024):.2f} MB, "
        f"sections: {stats['sections']})"
    )
    return stats


def ensure_manual_kindle_cover(manual: dict[str, Any]) -> None:
    """
    Generate the standalone Kindle Primary Front Cover (.pdf + 300 DPI RGB .jpg)
    for Volume I (SC-6), Volume II (SC-32), or Volume III (Domain Series).
    """
    tools_dir = str(WATCH_CALC_ROOT / "Tools")
    if tools_dir not in sys.path:
        sys.path.insert(0, tools_dir)
    from generate_manual_pdfs import compile_kindle_front_cover

    compile_kindle_front_cover(
        is_sc32=manual["is_sc32"],
        dpi=300,
        manual_kind=manual.get("manual_kind"),
    )


def sync_manual_to_outputs_and_kdp_upload(manual: dict[str, Any]) -> None:
    """
    Mirror the manual's .kpf, .kcb project directory, Kindle Primary Front Cover (.jpg + .pdf),
    and KDP print interior/cover PDFs to Website/docs/manuals/output, stackcalc/docs/manuals/output,
    and all kdp_upload directories.
    """
    kpf_path: Path = manual["kpf"]
    kcb_project_dir = kpf_path.parent / f"{kpf_path.stem}_KCB"
    kindle_cover_pdf: Path = manual["kindle_cover_pdf"]
    kindle_cover_jpg: Path = manual["kindle_cover_jpg"]
    pdf_path: Path = manual["pdf"]
    hardcover_pdf: Path = manual["hardcover_pdf"]
    paperback_cover: Path = manual["paperback_cover"]
    hardcover_cover: Path = manual["hardcover_cover"]
    prefix: str = manual["kdp_prefix"]

    num_pages = len(PdfReader(str(pdf_path)).pages) if pdf_path.is_file() else 0

    mirror_dirs = [
        WEBSITE_OUTPUT_DIR,
        STACKCALC_MANUAL_OUTPUT_DIR,
        STACKCALC_DOWNLOADS_MANUAL_DIR,
    ]
    for mdir in mirror_dirs:
        if mdir.parent.is_dir():
            mdir.mkdir(parents=True, exist_ok=True)
            for src in (kpf_path, kindle_cover_pdf, kindle_cover_jpg):
                if src.is_file():
                    shutil.copy2(src, mdir / src.name)
            if kcb_project_dir.is_dir():
                copy_kcb_project_dir(kcb_project_dir, mdir / kcb_project_dir.name)

    for kdp_dir in KDP_UPLOAD_DIRS:
        if kdp_dir.parent.is_dir():
            kdp_dir.mkdir(parents=True, exist_ok=True)
            # Copy canonical manual filenames
            for src in (
                pdf_path,
                hardcover_pdf,
                paperback_cover,
                hardcover_cover,
                kpf_path,
                kindle_cover_pdf,
                kindle_cover_jpg,
            ):
                if src.is_file():
                    shutil.copy2(src, kdp_dir / src.name)
            if kcb_project_dir.is_dir():
                copy_kcb_project_dir(kcb_project_dir, kdp_dir / kcb_project_dir.name)
                copy_kcb_project_dir(kcb_project_dir, kdp_dir / f"{prefix}-Kindle_KCB")

            # Remove any stale descriptive Interior PDFs with a previous page count
            for old_interior in kdp_dir.glob(f"{prefix}-*Interior-*pp.pdf"):
                if old_interior.name not in (
                    f"{prefix}-Interior-{num_pages}pp.pdf",
                    f"{prefix}-Hardcover-Interior-{num_pages}pp.pdf",
                ):
                    old_interior.unlink()

            # Also copy descriptive Volume-I / Volume-II filenames matching Book-1..Book-5
            descriptive_pairs = [
                (pdf_path, f"{prefix}-Interior-{num_pages}pp.pdf"),
                (hardcover_pdf, f"{prefix}-Hardcover-Interior-{num_pages}pp.pdf"),
                (paperback_cover, f"{prefix}-KDP-Paperback-Cover.pdf"),
                (hardcover_cover, f"{prefix}-KDP-Hardcover-Cover.pdf"),
                (kpf_path, f"{prefix}-Kindle.kpf"),
                (kindle_cover_pdf, f"{prefix}-Kindle-Cover.pdf"),
                (kindle_cover_jpg, f"{prefix}-Kindle-Cover.jpg"),
            ]
            for src, dst_name in descriptive_pairs:
                if src.is_file():
                    shutil.copy2(src, kdp_dir / dst_name)


def process_curriculum_book(cbook: dict[str, Any], java_build_dir: Path) -> None:
    """
    Generate the Kindle Primary Front Cover (.pdf + 300 DPI RGB .jpg), Kindle
    Print Replica (.kpf), and Kindle Create (.kcb) project directory for a US Letter
    curriculum book (Book 1, 2A, 2B, 3, 4, 5), and sync to all kdp_upload directories.
    """
    stackcalc_tools = str(STACKCALC_ROOT / "Tools")
    if stackcalc_tools not in sys.path:
        sys.path.insert(0, stackcalc_tools)
    from curriculum_shared import generate_kindle_front_cover

    pdf_path: Path = cbook["pdf"]
    if not pdf_path.is_file() and cbook["fallback_pdf"].is_file():
        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(cbook["fallback_pdf"], pdf_path)

    kdp_cover: Path = cbook["kdp_cover"]
    if not kdp_cover.is_file() and cbook["fallback_cover"].is_file():
        kdp_cover.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(cbook["fallback_cover"], kdp_cover)

    if not pdf_path.is_file():
        print(f"[SKIP] Curriculum PDF not found for {cbook['key']}: {pdf_path}")
        return

    # 1. Generate standalone Kindle Primary Front Cover (.pdf + 300 DPI RGB .jpg)
    generate_kindle_front_cover(
        cbook["kindle_cover_pdf"],
        cbook["kindle_cover_jpg"],
        cbook["cover_spec_key"],
        dpi=300,
    )
    print(
        f"[{cbook['key'].upper()}] Generated Kindle Primary Front Cover: "
        f"{cbook['kindle_cover_jpg'].name} ({cbook['kindle_cover_jpg'].stat().st_size:,} bytes)"
    )

    # 2. Build Kindle Print Replica (.kpf) + Kindle Create (.kcb) project folder
    build_kpf_package(
        key=cbook["key"],
        pdf_path=pdf_path,
        kpf_path=cbook["kpf"],
        title=cbook["title"],
        author=cbook["author"],
        java_build_dir=java_build_dir,
    )

    kcb_project_dir = cbook["kpf"].parent / f"{cbook['kpf'].stem}_KCB"

    # 3. Sync to all kdp_upload directories
    for kdp_dir in KDP_UPLOAD_DIRS:
        if kdp_dir.parent.is_dir():
            kdp_dir.mkdir(parents=True, exist_ok=True)
            for src in (
                pdf_path,
                kdp_cover,
                cbook["kpf"],
                cbook["kindle_cover_pdf"],
                cbook["kindle_cover_jpg"],
            ):
                if src.is_file() and src.parent.resolve() != kdp_dir.resolve():
                    shutil.copy2(src, kdp_dir / src.name)
            if (
                kcb_project_dir.is_dir()
                and kcb_project_dir.parent.resolve() != kdp_dir.resolve()
            ):
                copy_kcb_project_dir(kcb_project_dir, kdp_dir / kcb_project_dir.name)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate Kindle Print Replica (.kpf) files and Kindle Primary Covers for StackCalc books."
    )
    parser.add_argument(
        "--manual",
        choices=["all", "sc6", "sc32", "domains", "none"],
        default="all",
        help="Which flagship manual KPF to generate (default: all).",
    )
    parser.add_argument(
        "--include-curriculum",
        action="store_true",
        default=True,
        help="Also generate KPF and Kindle covers for Book 1-5 curriculum workbooks (default: True).",
    )
    parser.add_argument(
        "--manuals-only",
        action="store_true",
        help="Generate only the SC-6 and SC-32 flagship manuals (skip Book 1-5 curriculum workbooks).",
    )
    args = parser.parse_args()

    if not KAF_JAR.is_file() or not KAF_SHARED_LIBS.is_dir():
        print(
            f"ERROR: Kindle Create KAF libraries not found at {KINDLE_CREATE_CONVGEN}",
            file=sys.stderr,
        )
        return 1

    with tempfile.TemporaryDirectory(prefix="kpf_java_build_") as build_dir_str:
        build_dir = Path(build_dir_str)
        exc_dir = build_dir / "com" / "amazon" / "kaf" / "exception"
        exc_dir.mkdir(parents=True, exist_ok=True)
        (exc_dir / "KAFException.java").write_text(KAF_EXCEPTION_JAVA, encoding="utf-8")
        (build_dir / "KDFPrintReplicaBuilder.java").write_text(
            KDF_BUILDER_JAVA, encoding="utf-8"
        )

        compile_cmd = [
            "javac",
            "-cp",
            f"{KAF_JAR}{os.pathsep}{build_dir}",
            str(exc_dir / "KAFException.java"),
            str(build_dir / "KDFPrintReplicaBuilder.java"),
        ]
        proc = subprocess.run(compile_cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            print(
                f"ERROR: javac compilation failed:\n{proc.stderr}",
                file=sys.stderr,
            )
            return 1

        if args.manual != "none":
            selected = [
                m for m in MANUALS if args.manual in ("all", m["key"])
            ]
            for manual in selected:
                ensure_manual_kindle_cover(manual)
                build_kpf_package(
                    key=manual["key"],
                    pdf_path=manual["pdf"],
                    kpf_path=manual["kpf"],
                    title=manual["title"],
                    author=manual["author"],
                    java_build_dir=build_dir,
                )
                sync_manual_to_outputs_and_kdp_upload(manual)

        if args.include_curriculum and not args.manuals_only:
            for cbook in CURRICULUM_BOOKS:
                process_curriculum_book(cbook, build_dir)

    print("All requested Kindle Print Replica (.kpf) packages and Kindle Primary Covers generated and synced to kdp_upload.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
