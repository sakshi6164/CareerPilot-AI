"""
CareerPilot AI Pro
components/sidebar.py

Reusable application sidebar.
"""

import streamlit as st

from utils.constants import APP_NAME, APP_VERSION, MODELS, DEFAULT_MODEL


def render_sidebar():
    """
    Render the global sidebar.

    Returns
    -------
    str
        Selected OpenRouter model.
    """

    with st.sidebar:

        st.title("🚀 " + APP_NAME)

        st.caption(f"Version {APP_VERSION}")

        st.divider()

        st.subheader("🤖 AI Model")

        model_name = st.selectbox(
            "Choose Model",
            list(MODELS.keys()),
            index=list(MODELS.values()).index(DEFAULT_MODEL)
        )

        st.divider()

        st.subheader("✨ Modules")

        st.markdown("""
- 🏠 Home
- 📄 Resume Analyzer
- 📝 Resume Builder
- 💼 Job Matcher
- ✉ Cover Letter
- 🎯 Career Roadmap
- 🎤 Interview Preparation
- 🔗 LinkedIn Analyzer
- 💻 GitHub Analyzer
- 🤖 AI Career Coach
- 📊 Dashboard
- ⚙ Settings
""")

        st.divider()

        st.info(
            """
CareerPilot AI Pro helps you:

✅ Improve your Resume

✅ Match Jobs

✅ Generate Cover Letters

✅ Prepare for Interviews

✅ Build your Career Roadmap
"""
        )

        st.divider()

        st.success("Powered by OpenRouter AI")

    return MODELS[model_name]
