"""
CareerPilot AI Pro
utils/helpers.py

Reusable helper functions used across the application.
"""

from pathlib import Path
from datetime import datetime

from utils.constants import (
    ATS_EXCELLENT,
    ATS_GOOD,
    ATS_AVERAGE,
    REPORTS_DIR,
    RESUME_REPORTS_DIR,
    ANALYSIS_REPORTS_DIR,
    COVER_LETTER_REPORTS_DIR,
)


def ensure_directories():
    """Create project report directories if they do not exist."""
    for directory in [
        REPORTS_DIR,
        RESUME_REPORTS_DIR,
        ANALYSIS_REPORTS_DIR,
        COVER_LETTER_REPORTS_DIR,
    ]:
        Path(directory).mkdir(parents=True, exist_ok=True)


def ats_badge(score: int) -> str:
    """Return a text label for an ATS score."""
    if score >= ATS_EXCELLENT:
        return "Excellent ⭐"
    if score >= ATS_GOOD:
        return "Good 👍"
    if score >= ATS_AVERAGE:
        return "Average 🙂"
    return "Needs Improvement ⚠️"


def score_color(score: int) -> str:
    """Return a hex color for an ATS score."""
    if score >= ATS_EXCELLENT:
        return "#16A34A"
    if score >= ATS_GOOD:
        return "#F59E0B"
    return "#DC2626"


def timestamp() -> str:
    """Current timestamp for filenames."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def safe_filename(name: str) -> str:
    """Convert text into a safe filename."""
    keep = []
    for ch in name:
        if ch.isalnum():
            keep.append(ch)
        elif ch in (" ", "-", "_"):
            keep.append("_")
    return "".join(keep).strip("_") or "file"


def report_filename(prefix: str = "report", extension: str = "pdf") -> str:
    """Generate a timestamped report filename."""
    return f"{safe_filename(prefix)}_{timestamp()}.{extension}"


def truncate(text: str, length: int = 250) -> str:
    """Short preview of long text."""
    if len(text) <= length:
        return text
    return text[:length].rstrip() + "..."


def list_to_markdown(items):
    """Convert a list into markdown bullets."""
    return "\n".join(f"- {item}" for item in items)


def percentage(value: int, total: int) -> float:
    """Return percentage safely."""
    if total == 0:
        return 0.0
    return round((value / total) * 100, 2)
