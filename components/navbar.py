"""
CareerPilot AI Pro
components/navbar.py

Reusable top navigation bar.
"""

import streamlit as st

from utils.constants import APP_NAME, APP_VERSION


def render_navbar(page_title: str, icon: str = "🚀"):
    """
    Render a reusable top navigation bar.
    """

    left, right = st.columns([5, 1])

    with left:
        st.markdown(
            f"## {icon} {page_title}"
        )

    with right:
        st.caption(f"{APP_NAME}")
        st.caption(f"v{APP_VERSION}")

    st.divider()


def quick_actions():
    """
    Render common quick actions.
    """

    c1, c2, c3 = st.columns(3)

    with c1:
        refresh = st.button("🔄 Refresh", use_container_width=True)

    with c2:
        clear = st.button("🧹 Clear", use_container_width=True)

    with c3:
        help_btn = st.button("❓ Help", use_container_width=True)

    return {
        "refresh": refresh,
        "clear": clear,
        "help": help_btn,
    }


def page_description(text: str):
    """
    Display a consistent page description.
    """

    st.caption(text)
