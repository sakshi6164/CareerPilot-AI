import streamlit as st

from components.styles import load_css, section
from components.sidebar import render_sidebar
from components.header import render_header
from components.footer import render_footer

from utils.ai_client import generate_text
from utils.prompts import CAREER_COACH_PROMPT

st.set_page_config(
    page_title="AI Career Coach",
    page_icon="🤖",
    layout="wide"
)

load_css()
model = render_sidebar()

render_header(
    "AI Career Coach",
    "Ask career-related questions and receive AI guidance.",
    "🤖"
)

st.info(
    "Examples: Improve my resume • What should I learn after Python? • "
    "How do I become an ML Engineer? • Suggest projects for my portfolio."
)

question = st.text_area(
    "Ask your question",
    height=180,
    placeholder="Type your career question here..."
)

if st.button("Ask CareerPilot AI", use_container_width=True):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    prompt = f"""
{CAREER_COACH_PROMPT}

User Question:
{question}
"""

    with st.spinner("Thinking..."):
        answer = generate_text(
            prompt,
            model=model
        )

    section("AI Response")

    st.markdown(answer)

    st.download_button(
        "Download Response (.md)",
        answer,
        file_name="Career_Coach_Response.md",
        mime="text/markdown",
        use_container_width=True
    )

render_footer()
