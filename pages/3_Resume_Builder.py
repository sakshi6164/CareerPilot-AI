import streamlit as st

from components.styles import load_css, section
from components.sidebar import render_sidebar
from components.header import render_header
from components.footer import render_footer
from utils.ai_client import generate_text
from utils.prompts import RESUME_BUILDER_PROMPT

st.set_page_config(page_title="Resume Builder",page_icon="📝",layout="wide")

load_css()
model=render_sidebar()
render_header("Resume Builder","Generate an ATS-friendly resume with AI.","📝")

c1,c2=st.columns(2)
with c1:
    name=st.text_input("Full Name")
    role=st.text_input("Target Role")
    skills=st.text_area("Skills")
    education=st.text_area("Education")
with c2:
    experience=st.text_area("Experience")
    projects=st.text_area("Projects")
    certifications=st.text_area("Certifications")
    extras=st.text_area("Additional Information")

if st.button("Generate Resume",use_container_width=True):
    profile=f"""
Name: {name}
Target Role: {role}
Skills: {skills}
Education: {education}
Experience: {experience}
Projects: {projects}
Certifications: {certifications}
Additional Information: {extras}
"""
    prompt=RESUME_BUILDER_PROMPT+"\n\n"+profile
    with st.spinner("Generating resume..."):
        resume=generate_text(prompt,model=model)

    section("Generated Resume")
    st.markdown(resume)

    st.download_button(
        "Download Resume (.md)",
        resume,
        file_name="ATS_Resume.md",
        mime="text/markdown",
        use_container_width=True
    )

render_footer()
