import streamlit as st

from components.styles import load_css, hero, section, card, footer
from components.sidebar import render_sidebar
from components.cards import feature_card, stat_grid
from components.header import render_header

st.set_page_config(
    page_title="CareerPilot AI Pro",
    page_icon="🚀",
    layout="wide"
)

load_css()
selected_model = render_sidebar()

render_header(
    "CareerPilot AI Pro",
    "Your AI-powered career development platform.",
    "🚀"
)

hero(
    "CareerPilot AI Pro",
    "Build better resumes, match jobs, generate cover letters, prepare for interviews and accelerate your career using AI."
)

stat_grid({
    "AI Modules":12,
    "Supported Models":6,
    "Report Types":5,
    "Status":"Ready"
})

section("Core Features")

c1,c2,c3=st.columns(3)

with c1:
    feature_card("Resume Analyzer","Analyze resumes against job descriptions using AI.","📄")
    feature_card("Resume Builder","Generate ATS-friendly resumes.","📝")

with c2:
    feature_card("Job Matcher","Find skill gaps and improve your chances.","💼")
    feature_card("Cover Letter","Generate personalized cover letters.","✉️")

with c3:
    feature_card("Career Coach","Get AI career guidance and interview preparation.","🤖")
    feature_card("Dashboard","Track your career progress and reports.","📊")

section("Getting Started")

card(
    "Step 1",
    "Open the Resume Analyzer page, upload your resume and paste a job description."
)

card(
    "Step 2",
    "Review the ATS score, improve missing skills and download your report."
)

card(
    "Step 3",
    "Use Resume Builder, Cover Letter Generator and Career Coach to strengthen your applications."
)

section("Current AI Model")
st.success(f"Using: {selected_model}")

footer()
