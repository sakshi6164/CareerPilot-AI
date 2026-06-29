"""
CareerPilot AI Pro
components/footer.py

Reusable footer component.
"""

import streamlit as st

from utils.constants import APP_NAME, APP_VERSION, APP_AUTHOR


def render_footer():
    """
    Render a consistent footer for all pages.
    """

    st.divider()

    st.markdown(
        f"""
<div style="
text-align:center;
padding:20px;
color:#94A3B8;
font-size:14px;
">

<b>{APP_NAME}</b><br>

Version {APP_VERSION}<br><br>

Built with ❤️ using
<b>Streamlit</b> + <b>OpenRouter AI</b>

<br><br>

Developed by <b>{APP_AUTHOR}</b>

</div>
""",
        unsafe_allow_html=True,
    )


def render_small_footer():
    """
    Compact footer.
    """

    st.caption(
        f"{APP_NAME} • v{APP_VERSION}"
    )
