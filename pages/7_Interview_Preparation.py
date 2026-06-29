import streamlit as st

from components.styles import load_css, section
from components.sidebar import render_sidebar
from components.header import render_header
from components.footer import render_footer

from utils.ai_client import generate_text
from utils.prompts import INTERVIEW_PROMPT

st.set_page_config(page_title="Interview Preparation", page_icon="🎤", layout="wide")

load_css()
model=render_sidebar()
render_header("Interview Preparation","Generate AI interview questions and preparation guide.","🎤")

c1,c2=st.columns(2)
with c1:
    role=st.text_input("Target Role")
    level=st.selectbox("Experience Level",["Fresher","0-2 Years","3-5 Years","5+ Years"])
with c2:
    skills=st.text_area("Key Skills")
    company=st.text_input("Target Company (Optional)")

if st.button("Generate Interview Guide",use_container_width=True):
    prompt=f"""{INTERVIEW_PROMPT}

Target Role: {role}
Experience Level: {level}
Target Company: {company}
Skills:
{skills}
"""
    with st.spinner("Generating interview guide..."):
        guide=generate_text(prompt,model=model)

    section("Interview Guide")
    st.markdown(guide)

    st.download_button(
        "Download Guide (.md)",
        guide,
        file_name="Interview_Guide.md",
        mime="text/markdown",
        use_container_width=True
    )

render_footer()
