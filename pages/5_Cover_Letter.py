import streamlit as st

from components.styles import load_css, section
from components.sidebar import render_sidebar
from components.header import render_header
from components.footer import render_footer

from utils.ai_client import generate_text
from utils.prompts import COVER_LETTER_PROMPT
from utils.pdf_reader import extract_text_from_pdf
from utils.validators import validate_resume_file

st.set_page_config(
    page_title="Cover Letter",
    page_icon="✉️",
    layout="wide"
)

load_css()
model = render_sidebar()

render_header(
    "Cover Letter Generator",
    "Generate an AI-powered ATS-friendly cover letter.",
    "✉️"
)

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

col1, col2 = st.columns(2)

with col1:
    company = st.text_input("Company Name")
    role = st.text_input("Target Role")

with col2:
    hiring_manager = st.text_input("Hiring Manager (Optional)")
    applicant_name = st.text_input("Your Name")

job_description = st.text_area(
    "Paste Job Description",
    height=220
)

if st.button("Generate Cover Letter", use_container_width=True):

    ok, msg = validate_resume_file(uploaded_resume)

    if not ok:
        st.error(msg)
        st.stop()

    resume_text = extract_text_from_pdf(uploaded_resume)

    prompt = f"""
{COVER_LETTER_PROMPT}

Applicant:
{applicant_name}

Company:
{company}

Role:
{role}

Hiring Manager:
{hiring_manager}

Resume:
{resume_text}

Job Description:
{job_description}
"""

    with st.spinner("Generating Cover Letter..."):
        cover_letter = generate_text(
            prompt,
            model=model
        )

    section("Generated Cover Letter")

    st.markdown(cover_letter)

    st.download_button(
        "Download Cover Letter (.md)",
        cover_letter,
        file_name="Cover_Letter.md",
        mime="text/markdown",
        use_container_width=True
    )

render_footer()
