import streamlit as st

from components.styles import load_css, section
from components.sidebar import render_sidebar
from components.header import render_header
from components.footer import render_footer

from utils.ai_client import generate_text
from utils.prompts import CAREER_ROADMAP_PROMPT

st.set_page_config(page_title="Career Roadmap", page_icon="🎯", layout="wide")

load_css()
model=render_sidebar()
render_header("Career Roadmap","Generate a personalized AI learning roadmap.","🎯")

c1,c2=st.columns(2)
with c1:
    target=st.text_input("Target Career")
    level=st.selectbox("Current Level",["Beginner","Intermediate","Advanced"])
    timeline=st.selectbox("Target Timeline",["3 Months","6 Months","12 Months","24 Months"])
with c2:
    skills=st.text_area("Current Skills")
    interests=st.text_area("Interests / Preferred Domains")

if st.button("Generate Roadmap",use_container_width=True):
    prompt=f"""{CAREER_ROADMAP_PROMPT}

Target Career: {target}
Current Level: {level}
Timeline: {timeline}
Current Skills:
{skills}

Interests:
{interests}
"""
    with st.spinner("Generating roadmap..."):
        roadmap=generate_text(prompt,model=model)

    section("Your Career Roadmap")
    st.markdown(roadmap)

    st.download_button(
        "Download Roadmap (.md)",
        roadmap,
        file_name="Career_Roadmap.md",
        mime="text/markdown",
        use_container_width=True
    )

render_footer()
