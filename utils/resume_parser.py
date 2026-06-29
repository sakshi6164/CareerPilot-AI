"""
CareerPilot AI Pro
utils/resume_parser.py

Basic resume parsing utilities.
"""

import re
from typing import Dict, List


SECTION_HEADERS = {
    "education": ["education", "academic"],
    "experience": ["experience", "work experience", "employment"],
    "projects": ["projects", "project"],
    "skills": ["skills", "technical skills"],
    "certifications": ["certifications", "certificates"],
}


EMAIL_RE = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
PHONE_RE = r"(\+?\d[\d\-\s]{8,}\d)"


def _find_section(text: str, names: List[str]) -> str:
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip().lower() in names:
            start = i + 1
            break
    if start is None:
        return ""
    end = len(lines)
    for j in range(start, len(lines)):
        current = lines[j].strip().lower()
        if any(current in vals for vals in SECTION_HEADERS.values()):
            end = j
            break
    return "\n".join(lines[start:end]).strip()


def parse_resume(text: str) -> Dict:
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    name = lines[0] if lines else ""

    email = ""
    phone = ""

    e = re.search(EMAIL_RE, text)
    if e:
        email = e.group()

    p = re.search(PHONE_RE, text)
    if p:
        phone = p.group()

    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "education": _find_section(text, SECTION_HEADERS["education"]),
        "experience": _find_section(text, SECTION_HEADERS["experience"]),
        "projects": _find_section(text, SECTION_HEADERS["projects"]),
        "skills": _find_section(text, SECTION_HEADERS["skills"]),
        "certifications": _find_section(text, SECTION_HEADERS["certifications"]),
        "raw_text": text,
    }

    return data


def extract_skills(parsed: Dict) -> List[str]:
    skills = parsed.get("skills", "")
    if not skills:
        return []

    items = re.split(r"[,\n•|]", skills)
    cleaned = sorted(
        {item.strip() for item in items if item.strip()},
        key=str.lower
    )
    return cleaned
