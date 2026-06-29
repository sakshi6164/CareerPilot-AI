"""
CareerPilot AI Pro - constants.py
"""

from pathlib import Path

APP_NAME = "CareerPilot AI Pro"
APP_VERSION = "2.5.0"
APP_AUTHOR = "Sakshi Chauhan"

ROOT_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT_DIR / "assets"
DATA_DIR = ROOT_DIR / "data"
REPORTS_DIR = ROOT_DIR / "reports"

RESUME_REPORTS_DIR = REPORTS_DIR / "resumes"
ANALYSIS_REPORTS_DIR = REPORTS_DIR / "analysis"
COVER_LETTER_REPORTS_DIR = REPORTS_DIR / "cover_letters"

SUPPORTED_RESUME_TYPES = ["pdf"]

ATS_EXCELLENT = 80
ATS_GOOD = 60
ATS_AVERAGE = 40

MODELS = {
    "Gemini 2.5 Flash Lite": "google/gemini-2.5-flash-lite",
    "GPT-4.1 Mini": "openai/gpt-4.1-mini",
    "Claude Sonnet 4": "anthropic/claude-sonnet-4",
    "DeepSeek V3": "deepseek/deepseek-chat",
    "Llama 3.3 70B": "meta-llama/llama-3.3-70b-instruct",
    "Qwen 3": "qwen/qwen3-32b",
}

DEFAULT_MODEL = MODELS["Gemini 2.5 Flash Lite"]

PRIMARY_COLOR = "#2563EB"
SECONDARY_COLOR = "#7C3AED"
SUCCESS_COLOR = "#16A34A"
WARNING_COLOR = "#F59E0B"
ERROR_COLOR = "#DC2626"
BACKGROUND_COLOR = "#0F172A"

PAGES = [
    "Home",
    "Resume Analyzer",
    "Resume Builder",
    "Job Matcher",
    "Cover Letter",
    "Career Roadmap",
    "Interview Preparation",
    "LinkedIn Analyzer",
    "GitHub Analyzer",
    "AI Career Coach",
    "Dashboard",
    "Settings",
]

SKILL_CATEGORIES = [
    "Programming",
    "Web Development",
    "Data Science",
    "Machine Learning",
    "Artificial Intelligence",
    "Cloud",
    "DevOps",
    "Databases",
    "Soft Skills",
]

DEFAULT_TEMPERATURE = 0.3
MAX_RESUME_PREVIEW = 1500
