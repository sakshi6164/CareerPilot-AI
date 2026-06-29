import streamlit as st

from components.styles import load_css, section
from components.sidebar import render_sidebar
from components.header import render_header
from components.footer import render_footer
from utils.ai_client import generate_text
from utils.prompts import LINKEDIN_PROMPT
from utils.validators import validate_linkedin_url

st.set_page_config(page_title="LinkedIn Analyzer", page_icon="🔗", layout="wide")

load_css()
model=render_sidebar()
render_header("LinkedIn Analyzer","Optimize your LinkedIn profile with AI.","🔗")

url=st.text_input("LinkedIn Profile URL (optional)")
profile=st.text_area("Or paste your LinkedIn profile/about section",height=250)

if st.button("Analyze Profile",use_container_width=True):
    if url:
        if not validate_linkedin_url(url):
            st.error("Please enter a valid LinkedIn profile URL.")
            st.stop()
    if not url and not profile.strip():
        st.error("Provide either a LinkedIn URL or profile content.")
        st.stop()

    prompt=f"""{LINKEDIN_PROMPT}

LinkedIn URL:
{url}

Profile Content:
{profile}
"""
    with st.spinner("Analyzing profile..."):
        report=generate_text(prompt,model=model)

    section("AI Analysis")
    st.markdown(report)

    st.download_button(
        "Download Analysis (.md)",
        report,
        file_name="LinkedIn_Analysis.md",
        mime="text/markdown",
        use_container_width=True
    )

render_footer()
