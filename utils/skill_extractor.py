"""
CareerPilot AI Pro
utils/skill_extractor.py

Extracts and categorizes technical skills from resume text.
"""

import re
from collections import defaultdict

SKILL_DATABASE = {
    "Programming": [
        "python", "java", "c", "c++", "c#", "javascript",
        "typescript", "go", "rust", "kotlin", "swift", "php"
    ],
    "Web Development": [
        "html", "css", "react", "angular", "vue", "next.js",
        "node.js", "express", "flask", "django", "fastapi"
    ],
    "Data Science": [
        "pandas", "numpy", "matplotlib", "plotly",
        "scikit-learn", "statistics", "data analysis"
    ],
    "Machine Learning": [
        "machine learning", "deep learning",
        "tensorflow", "keras", "pytorch",
        "xgboost", "lightgbm"
    ],
    "Artificial Intelligence": [
        "llm", "gpt", "gemini", "claude",
        "langchain", "rag", "nlp", "computer vision"
    ],
    "Cloud": [
        "aws", "azure", "gcp", "docker",
        "kubernetes", "terraform"
    ],
    "Databases": [
        "mysql", "postgresql", "sqlite",
        "mongodb", "redis", "firebase"
    ],
    "DevOps": [
        "git", "github", "github actions",
        "jenkins", "linux", "bash"
    ],
}

def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def extract_skills(text: str):
    """
    Extract all recognized skills from resume text.

    Returns:
        dict
    """
    text = normalize(text)

    results = defaultdict(list)

    for category, skills in SKILL_DATABASE.items():

        for skill in skills:

            if skill.lower() in text:

                results[category].append(skill)

    # remove duplicates

    for category in results:
        results[category] = sorted(
            list(set(results[category])),
            key=str.lower
        )

    return dict(results)


def all_skills(text: str):
    """
    Returns a flat list of unique skills.
    """
    categorized = extract_skills(text)

    output = []

    for skills in categorized.values():
        output.extend(skills)

    return sorted(set(output), key=str.lower)


def total_skills(text: str):
    return len(all_skills(text))


def category_statistics(text: str):
    categorized = extract_skills(text)

    stats = {}

    for category, skills in categorized.items():
        stats[category] = len(skills)

    return stats
