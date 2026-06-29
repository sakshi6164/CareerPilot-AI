import streamlit as st

from components.styles import load_css, section
from components.sidebar import render_sidebar
from components.header import render_header
from components.footer import render_footer

from utils.ai_client import generate_text
from utils.prompts import GITHUB_PROMPT
from utils.validators import validate_github_url

st.set_page_config(page_title="GitHub Analyzer", page_icon="💻", layout="wide")

load_css()
model=render_sidebar()
render_header("GitHub Analyzer","Analyze your GitHub profile using AI.","💻")

url=st.text_input("GitHub Profile URL")
repos=st.text_area("Or paste repository details / README content",height=250)

if st.button("Analyze GitHub",use_container_width=True):
    if url:
        if not validate_github_url(url):
            st.error("Please enter a valid GitHub profile URL.")
            st.stop()
    if not url and not repos.strip():
        st.error("Provide a GitHub URL or repository information.")
        st.stop()

    prompt=f"""{GITHUB_PROMPT}

GitHub URL:
{url}

Repository Information:
{repos}
"""
    with st.spinner("Analyzing GitHub profile..."):
        report=generate_text(prompt,model=model)

    section("AI GitHub Review")
    st.markdown(report)

    st.download_button(
        "Download Review (.md)",
        report,
        file_name="GitHub_Review.md",
        mime="text/markdown",
        use_container_width=True
    )

render_footer()
