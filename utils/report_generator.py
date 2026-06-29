"""
CareerPilot AI Pro
utils/report_generator.py

Reusable PDF report generator.
"""

from pathlib import Path
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from utils.helpers import ensure_directories, report_filename
from utils.constants import ANALYSIS_REPORTS_DIR


styles = getSampleStyleSheet()


def _heading(text):
    return Paragraph(f"<b>{text}</b>", styles["Heading2"])


def _body(text):
    return Paragraph(text, styles["BodyText"])


def _bullet(text):
    return Paragraph(f"• {text}", styles["BodyText"])


def create_ats_report(data):
    """
    Creates a PDF ATS report.

    Returns:
        Path to generated PDF.
    """

    ensure_directories()

    filename = ANALYSIS_REPORTS_DIR / report_filename(
        "ATS_Report",
        "pdf"
    )

    doc = SimpleDocTemplate(str(filename))

    story = []

    story.append(
        Paragraph(
            "<b>CareerPilot AI Pro - ATS Resume Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 12))

    story.append(
        _body(f"<b>ATS Score:</b> {data['ats_score']}%")
    )

    sections = [
        ("Matching Skills", data["matching_skills"]),
        ("Missing Skills", data["missing_skills"]),
        ("Strengths", data["strengths"]),
        ("Weaknesses", data["weaknesses"]),
        ("Suggestions", data["suggestions"]),
    ]

    for title, items in sections:

        story.append(Spacer(1, 10))
        story.append(_heading(title))

        for item in items:
            story.append(_bullet(item))

    story.append(Spacer(1, 12))

    story.append(
        _body(
            f"<b>Recommendation:</b> {data['recommendation']}"
        )
    )

    doc.build(story)

    return str(filename)


def create_text_report(
    title,
    content,
    filename_prefix="Report"
):
    """
    Generic PDF report.
    """

    ensure_directories()

    filename = ANALYSIS_REPORTS_DIR / report_filename(
        filename_prefix,
        "pdf"
    )

    doc = SimpleDocTemplate(str(filename))

    story = [
        Paragraph(
            f"<b>{title}</b>",
            styles["Title"]
        ),
        Spacer(1, 15),
        Paragraph(content.replace("\n", "<br/>"), styles["BodyText"]),
    ]

    doc.build(story)

    return str(filename)
