#!/usr/bin/env python3
"""
Teacher Evaluation Kit Builder for StackCalc.

Generates:
1. docs/downloads/StackCalc_District_PO_Requisition_and_W9_Packet.pdf
2. docs/downloads/stackcalc-teacher-evaluation-kit.zip

Bundles official district requisition form, W-9 onboarding SLA, sample station guides,
curriculum preview, and Texas UIL competition materials into a single 1-click evaluation archive.
"""

import sys
import os
import zipfile
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
DOWNLOADS_DIR = DOCS_DIR / "downloads"
OUTPUT_PDF = DOWNLOADS_DIR / "StackCalc_District_PO_Requisition_and_W9_Packet.pdf"
OUTPUT_ZIP = DOWNLOADS_DIR / "stackcalc-teacher-evaluation-kit.zip"


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        # Running header
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(HexColor("#0D1017"))
        self.drawString(54, 750, "STACKCALC INSTRUMENTS // INSTITUTIONAL REQUISITION & W-9 ONBOARDING")
        self.setFont("Helvetica", 8)
        self.setFillColor(HexColor("#64748B"))
        self.drawRightString(612 - 54, 750, "NET-30 VENDOR PACKET")

        self.setStrokeColor(HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(54, 742, 612 - 54, 742)

        # Running footer
        self.line(54, 45, 612 - 54, 45)
        self.setFont("Helvetica", 8)
        self.setFillColor(HexColor("#64748B"))
        self.drawString(54, 32, "StackCalc Educational Instruments • quotes@stackcalc.io • stackcalc.io")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(612 - 54, 32, page_str)
        self.restoreState()


def build_requisition_pdf():
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54,
        title="StackCalc Institutional PO Requisition & W-9 Packet",
        author="StackCalc Instruments"
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=HexColor('#0D1017'),
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=HexColor('#475569'),
        spaceAfter=12
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=HexColor('#0F172A'),
        spaceBefore=10,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=HexColor('#1E293B'),
        spaceAfter=6
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=HexColor('#0F172A')
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=white
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=HexColor('#0F172A')
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=table_cell,
        fontName='Helvetica-Bold'
    )

    elements = []

    # Title Banner
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("School District Purchase Order Requisition & W-9 Packet", title_style))
    elements.append(Paragraph(
        "Official procurement requisition form, Net-30 payment terms, and vendor onboarding compliance for public school districts, charter networks, and STEM academies.",
        subtitle_style
    ))
    elements.append(HRFlowable(width="100%", thickness=1, color=HexColor('#0D1017'), spaceAfter=10))

    # Fast Facts Callout Box
    summary_data = [
        [
            Paragraph("<b>Vendor Name:</b> StackCalc Instruments<br/><b>Procurement Contact:</b> quotes@stackcalc.io<br/><b>Official Website:</b> https://stackcalc.io", callout_style),
            Paragraph("<b>Payment Terms:</b> Net-30 Terms on Official PO<br/><b>W-9 Turnaround SLA:</b> &lt; 24 Business Hours<br/><b>Reproduction License:</b> Perpetual (Unlimited Copies)", callout_style)
        ]
    ]
    summary_table = Table(summary_data, colWidths=[250, 254])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor('#F8FAFC')),
        ('BOX', (0, 0), (-1, -1), 1, HexColor('#CBD5E1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, HexColor('#E2E8F0')),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    elements.append(summary_table)
    elements.append(Spacer(1, 10))

    # Section 1: Standard Requisition Fleet Pricing
    elements.append(Paragraph("1. Classroom Fleet Pricing & Discount Schedule", h2_style))
    elements.append(Paragraph(
        "All hardware purchases include our lifetime <i>No Lost Piece Left Behind</i> warranty and a campus-wide <b>Perpetual Reproduction License</b> for all 120 station guides and 24 tournament contest exams.",
        body_style
    ))

    pricing_data = [
        [
            Paragraph("Item Description & SKU", table_header),
            Paragraph("Standard Unit", table_header),
            Paragraph("Fleet (30+ Units)", table_header),
            Paragraph("District Savings", table_header),
            Paragraph("Order Qty", table_header),
        ],
        [
            Paragraph("<b>SC-6 Elementary RPN Calculator</b><br/>4-line integer LCD, [123], [FDISP], [CLK], [%]", table_cell),
            Paragraph("$39.00", table_cell),
            Paragraph("<b>$33.00</b>", table_cell_bold),
            Paragraph("Save 15% ($990 / 30-pk)", table_cell),
            Paragraph("[ &nbsp; &nbsp; &nbsp; &nbsp; ]", table_cell_bold),
        ],
        [
            Paragraph("<b>SC-32 Scientific RPN Calculator</b><br/>4-line display, trig, vectors, stat, Brent solver", table_cell),
            Paragraph("$59.00", table_cell),
            Paragraph("<b>$49.66</b>", table_cell_bold),
            Paragraph("Save 16% ($1,490 / 30-pk)", table_cell),
            Paragraph("[ &nbsp; &nbsp; &nbsp; &nbsp; ]", table_cell_bold),
        ],
        [
            Paragraph("<b>Spiral-Bound Handbook (SC-32 or SC-6)</b><br/>100% lay-flat coil, 32lb synthetic archival paper", table_cell),
            Paragraph("$16.00", table_cell),
            Paragraph("<b>$11.00</b>", table_cell_bold),
            Paragraph("Save 31% (Fleet tier)", table_cell),
            Paragraph("[ &nbsp; &nbsp; &nbsp; &nbsp; ]", table_cell_bold),
        ],
        [
            Paragraph("<b>Ten-Frame Dual-Stage Station Fleet</b><br/>30 dual-stage trays, 600 counters, storage shelves", table_cell),
            Paragraph("$840.00", table_cell),
            Paragraph("<b>$688.80</b>", table_cell_bold),
            Paragraph("Save 18% (Classroom set)", table_cell),
            Paragraph("[ &nbsp; &nbsp; &nbsp; &nbsp; ]", table_cell_bold),
        ],
        [
            Paragraph("<b>Math Domino Studio Classroom Fleet</b><br/>30 12-frame trays, 900 laser-foamed dominoes", table_cell),
            Paragraph("$870.00", table_cell),
            Paragraph("<b>$713.40</b>", table_cell_bold),
            Paragraph("Save 18% (Classroom set)", table_cell),
            Paragraph("[ &nbsp; &nbsp; &nbsp; &nbsp; ]", table_cell_bold),
        ],
        [
            Paragraph("<b>Algebra Tile Lab Station Fleet</b><br/>30 2D coordinate stages, 2,160 color-coded tiles", table_cell),
            Paragraph("$780.00", table_cell),
            Paragraph("<b>$639.60</b>", table_cell_bold),
            Paragraph("Save 18% (Classroom set)", table_cell),
            Paragraph("[ &nbsp; &nbsp; &nbsp; &nbsp; ]", table_cell_bold),
        ],
    ]

    pricing_table = Table(pricing_data, colWidths=[200, 70, 84, 100, 50])
    pricing_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#0D1017')),
        ('BOX', (0, 0), (-1, -1), 1, HexColor('#CBD5E1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, HexColor('#E2E8F0')),
        ('PADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#FFFFFF'), HexColor('#F8FAFC')]),
    ]))
    elements.append(pricing_table)
    elements.append(Spacer(1, 10))

    # Section 2: Procurement & Submission Steps
    elements.append(Paragraph("2. Fast-Track District Purchase Order Instructions", h2_style))
    elements.append(Paragraph(
        "<b>Step 1: Formal Quote Generation.</b> Forward your itemized requisition quantities to <b>quotes@stackcalc.io</b> or submit online at <i>stackcalc.io/#school-po</i>.<br/>"
        "<b>Step 2: W-9 & Vendor Onboarding.</b> Our finance team returns a signed IRS Form W-9, EFT/ACH routing instructions, and Texas DIR / FERPA compliance letters within 24 business hours.<br/>"
        "<b>Step 3: Official PO Issuance.</b> Email your school district or university Purchase Order to <b>quotes@stackcalc.io</b>.<br/>"
        "<b>Step 4: Dispatch & Net-30 Invoicing.</b> Hardware and books dispatch via tracked courier within 48 hours. Electronic invoices are delivered with 30-day payment terms.",
        body_style
    ))
    elements.append(Spacer(1, 6))

    # Section 3: Fillable District Requisition Details
    elements.append(Paragraph("3. District Purchasing Agent & Shipping Authorization", h2_style))

    field_data = [
        [
            Paragraph("<b>School District / Institution:</b>", body_style),
            Paragraph("________________________________________________", body_style)
        ],
        [
            Paragraph("<b>Campus / Department:</b>", body_style),
            Paragraph("________________________________________________", body_style)
        ],
        [
            Paragraph("<b>Purchasing Agent / Teacher Name:</b>", body_style),
            Paragraph("________________________________________________", body_style)
        ],
        [
            Paragraph("<b>Email Address & Direct Phone:</b>", body_style),
            Paragraph("________________________________________________", body_style)
        ],
        [
            Paragraph("<b>Ship-To Address (No P.O. Boxes):</b>", body_style),
            Paragraph("________________________________________________", body_style)
        ],
        [
            Paragraph("<b>District Tax ID / Exemption #:</b>", body_style),
            Paragraph("________________________________________________", body_style)
        ],
        [
            Paragraph("<b>Authorized Signature & Date:</b>", body_style),
            Paragraph("____________________________________ Date: ______", body_style)
        ],
    ]

    field_table = Table(field_data, colWidths=[180, 324])
    field_table.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 0.75, HexColor('#CBD5E1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, HexColor('#F1F5F9')),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (0, -1), HexColor('#F8FAFC')),
    ]))
    elements.append(field_table)

    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"Generated PDF: {OUTPUT_PDF}")


def build_evaluation_zip():
    readme_text = """================================================================================
STACKCALC EDUCATIONAL EVALUATION KIT & DISTRICT REQUISITION BUNDLE
================================================================================

Welcome to the StackCalc Evaluation Kit. This bundle equips math coaches, STEM
department chairs, curriculum directors, and classroom teachers to evaluate
StackCalc Reverse Polish Notation (RPN) calculators, tactile manipulatives,
and classroom station labs.

CONTENTS OF THIS EVALUATION KIT:
--------------------------------------------------------------------------------
01_District_PO_Requisition_and_W9_Packet.pdf
    Official institutional requisition form, volume fleet pricing matrix, Net-30
    invoicing procedures, and 24-hour IRS Form W-9 onboarding SLA.

02_Teacher_Facilitation_Guide_and_Rubrics.pdf
    34-page master guide for station setup, 4-tier student mastery rubrics,
    and diagnostic remediation guides for common arithmetic misconceptions.

03_RPN_Math_Labs_Curriculum_Sample.pdf
    12-page sample instructional unit detailing the Concrete-Pictorial-Abstract (CPA)
    progression: fraction towers, base-10 regrouping, and introductory RPN stacks.

04_Singapore_Math_Station_Companion_FormA.pdf
    Publication-grade 2-page student station companion and teacher rubric for
    Singapore Dimensions Math (Grade 1 Number Bonds & Complements).

05_Bridges_Math_Station_Companion_FormA.pdf
    Publication-grade 2-page visual companion for Bridges in Mathematics
    (Grade 1 Addition & Fact Strategies).

06_Big_Ideas_Secondary_Station_Companion_FormA.pdf
    Publication-grade 2-page visual companion for Big Ideas Math
    (Grade 6 Numerical Expressions & Postfix Stack Tracing).

07_Texas_UIL_High_School_Exam_26A.pdf
    Full 70-problem official tournament sprint exam for High School Calculator
    Applications (UIL / TMSCA / TAPPS).

08_Texas_UIL_Official_Scoring_Key_26A.pdf
    Tournament-standard 4-column grading key with 3-significant-figure canonical
    answers and official acceptance intervals.

--------------------------------------------------------------------------------
ORDERING & EVALUATION ASSISTANCE:
Questions regarding classroom pilots, sample kits, or volume purchase orders?
Email: quotes@stackcalc.io
Web:   https://stackcalc.io/#school-po
Store: https://www.etsy.com/shop/StackCalc
================================================================================
"""

    with zipfile.ZipFile(OUTPUT_ZIP, 'w', zipfile.ZIP_DEFLATED) as zf:
        # 00 README
        zf.writestr("00_README_Teacher_Evaluation_Kit.txt", readme_text)

        # 01 Requisition PDF
        if OUTPUT_PDF.exists():
            zf.write(OUTPUT_PDF, arcname="01_District_PO_Requisition_and_W9_Packet.pdf")

        # 02 Teacher Guide
        tg_pdf = DOWNLOADS_DIR / "teacher-booklet-letter.pdf"
        if tg_pdf.exists():
            zf.write(tg_pdf, arcname="02_Teacher_Facilitation_Guide_and_Rubrics.pdf")

        # 03 Curriculum Sample
        cs_pdf = DOWNLOADS_DIR / "stackcalc-curriculum-sample-v0.2.0.pdf"
        if cs_pdf.exists():
            zf.write(cs_pdf, arcname="03_RPN_Math_Labs_Curriculum_Sample.pdf")

        # 04 Singapore Math
        sm_pdf = DOWNLOADS_DIR / "worksheets" / "dimensions_grade_1a_chapter_2_form_a.pdf"
        if sm_pdf.exists():
            zf.write(sm_pdf, arcname="04_Singapore_Math_Station_Companion_FormA.pdf")

        # 05 Bridges Math
        bm_pdf = DOWNLOADS_DIR / "worksheets" / "bridges_grade_1_unit_2_form_a.pdf"
        if bm_pdf.exists():
            zf.write(bm_pdf, arcname="05_Bridges_Math_Station_Companion_FormA.pdf")

        # 06 Big Ideas Secondary
        bi_pdf = DOWNLOADS_DIR / "worksheets" / "bigideas_grade_6_chapter_1_form_a.pdf"
        if bi_pdf.exists():
            zf.write(bi_pdf, arcname="06_Big_Ideas_Secondary_Station_Companion_FormA.pdf")

        # 07 UIL Exam 26A
        uil_exam = DOWNLOADS_DIR / "uil" / "uil_exam_26a.pdf"
        if uil_exam.exists():
            zf.write(uil_exam, arcname="07_Texas_UIL_High_School_Exam_26A.pdf")

        # 08 UIL Solutions 26A
        uil_sol = DOWNLOADS_DIR / "uil" / "uil_solutions_26a.pdf"
        if uil_sol.exists():
            zf.write(uil_sol, arcname="08_Texas_UIL_Official_Scoring_Key_26A.pdf")

    print(f"Generated ZIP: {OUTPUT_ZIP} ({OUTPUT_ZIP.stat().st_size} bytes)")


def main():
    build_requisition_pdf()
    build_evaluation_zip()


if __name__ == '__main__':
    main()
