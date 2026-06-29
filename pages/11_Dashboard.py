import streamlit as st
import pandas as pd

from components.styles import load_css, section
from components.sidebar import render_sidebar
from components.header import render_header
from components.footer import render_footer
from components.cards import stat_grid, feature_card

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

load_css()
render_sidebar()

render_header(
    "Dashboard",
    "Overview of your CareerPilot AI activity.",
    "📊"
)

stat_grid({
    "AI Modules": 10,
    "Reports": 5,
    "Career Tools": 12,
    "Status": "Active"
})

section("Platform Modules")

c1, c2, c3 = st.columns(3)

with c1:
    feature_card("Resume Analyzer", "Analyze resumes with ATS scoring.", "📄")
    feature_card("Resume Builder", "Create ATS-friendly resumes.", "📝")

with c2:
    feature_card("Job Matcher", "Compare resumes with job descriptions.", "💼")
    feature_card("Career Coach", "Ask AI career questions.", "🤖")

with c3:
    feature_card("Interview Prep", "Generate interview questions.", "🎤")
    feature_card("Career Roadmap", "Build a learning roadmap.", "🎯")

section("Career Progress")

progress = pd.DataFrame({
    "Metric": [
        "Resume",
        "Job Matching",
        "Interview Prep",
        "Career Planning",
        "Profile Optimization"
    ],
    "Completion": [85, 70, 60, 55, 75]
})

st.bar_chart(
    progress.set_index("Metric")
)

section("Recent Activity")

st.dataframe(
    pd.DataFrame({
        "Module": [
            "Resume Analyzer",
            "Resume Builder",
            "Career Coach",
            "Cover Letter"
        ],
        "Status": [
            "Completed",
            "Generated",
            "Used",
            "Generated"
        ]
    }),
    use_container_width=True
)

render_footer()
