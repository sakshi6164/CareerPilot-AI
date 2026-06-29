import streamlit as st

from components.styles import load_css, section
from components.sidebar import render_sidebar
from components.header import render_header
from components.footer import render_footer
from components.cards import stat_grid
from utils.pdf_reader import extract_text_from_pdf
from utils.validators import validate_resume_file, validate_job_description
from utils.prompts import ATS_PROMPT
from utils.ai_client import analyze_resume
from utils.report_generator import create_ats_report
from utils.resume_parser import parse_resume
from utils.skill_extractor import category_statistics

st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="wide")

load_css()
model=render_sidebar()
render_header("Resume Analyzer","Analyze your resume against a job description.","📄")

uploaded=st.file_uploader("Upload Resume (PDF)",type=["pdf"])
jd=st.text_area("Job Description",height=220)

if st.button("Analyze Resume",use_container_width=True):
    ok,msg=validate_resume_file(uploaded)
    if not ok:
        st.error(msg); st.stop()
    ok,msg=validate_job_description(jd)
    if not ok:
        st.error(msg); st.stop()

    resume=extract_text_from_pdf(uploaded)
    parsed=parse_resume(resume)

    prompt=f"""
    {ATS_PROMPT}

Resume:
{resume}

Job Description:
{jd}
"""
    with st.spinner("Analyzing..."):
        result=analyze_resume(prompt)

    stat_grid({
        "ATS":f"{result['ats_score']}%",
        "Matched":len(result["matching_skills"]),
        "Missing":len(result["missing_skills"]),
        "Recommendation":result["recommendation"]
    })

    st.progress(result["ats_score"]/100)

    c1,c2=st.columns(2)
    with c1:
        section("Resume Details")
        st.write(parsed)
        section("Strengths")
        for x in result["strengths"]:
            st.success(x)
        section("Suggestions")
        for x in result["suggestions"]:
            st.info(x)

    with c2:
        section("Missing Skills")
        for x in result["missing_skills"]:
            st.error(x)
        section("Skill Categories")
        st.json(category_statistics(resume))

    pdf=create_ats_report(result)
    with open(pdf,"rb") as f:
        st.download_button("Download PDF Report",f,"ATS_Report.pdf","application/pdf",use_container_width=True)

render_footer()
