"""
CareerPilot AI Pro
components/styles.py

Global styling utilities for the Streamlit application.
"""

import streamlit as st

GLOBAL_CSS = """
<style>

.block-container{
    padding-top:1.2rem;
    padding-bottom:2rem;
    max-width:1400px;
}

.main{
    background:#0F172A;
}

.hero-card{
    background:linear-gradient(135deg,#2563EB,#7C3AED);
    color:white;
    padding:30px;
    border-radius:18px;
    margin-bottom:25px;
}

.cp-card{
    background:#1E293B;
    border:1px solid #334155;
    border-radius:15px;
    padding:20px;
    margin-bottom:15px;
}

.metric-card{
    background:#111827;
    border-radius:15px;
    padding:18px;
    text-align:center;
}

.section-title{
    font-size:28px;
    font-weight:700;
    margin-top:20px;
    margin-bottom:15px;
}

.footer{
    text-align:center;
    color:#94A3B8;
    margin-top:50px;
    padding:15px;
}

div[data-testid="stMetric"]{
    background:#111827;
    border-radius:15px;
    padding:12px;
    border:1px solid #334155;
}

.stButton>button{
    width:100%;
    border-radius:10px;
    font-weight:600;
    height:3rem;
}

</style>
"""


def load_css():
    """Load global application styles."""
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


def hero(title: str, subtitle: str):
    """Display hero banner."""
    st.markdown(
        f"""
        <div class="hero-card">
            <h1>{title}</h1>
            <p style="font-size:18px;">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section(title: str):
    """Display section heading."""
    st.markdown(
        f'<div class="section-title">{title}</div>',
        unsafe_allow_html=True,
    )


def card(title: str, body: str):
    """Display a reusable content card."""
    st.markdown(
        f"""
        <div class="cp-card">
            <h4>{title}</h4>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer():
    """Display footer."""
    st.markdown(
        """
        <div class="footer">
            CareerPilot AI Pro • Powered by OpenRouter & Streamlit
        </div>
        """,
        unsafe_allow_html=True,
    )
