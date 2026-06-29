import streamlit as st

from components.styles import load_css, section
from components.sidebar import render_sidebar
from components.header import render_header
from components.footer import render_footer

from utils.constants import MODELS, DEFAULT_MODEL

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

load_css()
render_sidebar()

render_header(
    "Settings",
    "Configure your CareerPilot AI Pro experience.",
    "⚙️"
)

section("AI Configuration")

selected_model = st.selectbox(
    "Default AI Model",
    list(MODELS.keys()),
    index=list(MODELS.values()).index(DEFAULT_MODEL)
)

temperature = st.slider(
    "Creativity (Temperature)",
    min_value=0.0,
    max_value=1.0,
    value=0.3,
    step=0.1
)

section("Application Preferences")

dark_mode = st.toggle(
    "Enable Dark Mode",
    value=True
)

show_tips = st.toggle(
    "Show Tips",
    value=True
)

default_export = st.selectbox(
    "Default Export Format",
    ["Markdown (.md)", "PDF (.pdf)"]
)

section("Session")

if st.button("Save Settings", use_container_width=True):
    st.success("Settings saved for this session.")

st.info(
    "Persistent user settings and profile management "
    "can be added in a future version."
)

render_footer()
