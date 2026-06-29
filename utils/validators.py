"""
CareerPilot AI Pro
utils/validators.py

Validation helpers used across the application.
"""

import re
from pathlib import Path
from urllib.parse import urlparse

from utils.constants import SUPPORTED_RESUME_TYPES


def validate_resume_file(uploaded_file):
    """
    Validate uploaded resume file.
    Returns:
        (bool, message)
    """

    if uploaded_file is None:
        return False, "Please upload a resume."

    extension = Path(uploaded_file.name).suffix.lower().replace(".", "")

    if extension not in SUPPORTED_RESUME_TYPES:
        return (
            False,
            f"Unsupported file type. Allowed: {', '.join(SUPPORTED_RESUME_TYPES)}"
        )

    return True, "Valid resume."


def validate_text(text, minimum_length=30):
    """
    Validate generic text.
    """

    if not text:
        return False, "Input cannot be empty."

    if len(text.strip()) < minimum_length:
        return (
            False,
            f"Please enter at least {minimum_length} characters."
        )

    return True, "Valid."


def validate_email(email):
    """
    Validate email.
    """

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return bool(re.match(pattern, email))


def validate_url(url):
    """
    Validate URL without external libraries.
    """

    try:
        parsed = urlparse(url)

        return all([
            parsed.scheme in ("http", "https"),
            parsed.netloc != ""
        ])

    except Exception:
        return False


def validate_linkedin_url(url):
    """
    Validate LinkedIn URL.
    """

    if not validate_url(url):
        return False

    return "linkedin.com" in url.lower()


def validate_github_url(url):
    """
    Validate GitHub URL.
    """

    if not validate_url(url):
        return False

    return "github.com" in url.lower()


def validate_job_description(text):
    """
    Validate job description.
    """

    return validate_text(text, minimum_length=10)


def validate_resume_text(text):
    """
    Validate extracted resume text.
    """

    return validate_text(text, minimum_length=150)


def validate_ai_prompt(prompt):
    """
    Validate AI prompt.
    """

    return bool(prompt and prompt.strip())