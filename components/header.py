"""
CareerPilot AI Pro
components/header.py
"""

import streamlit as st

def render_header(title:str, subtitle:str="", icon:str="🚀", show_divider:bool=True):
    st.markdown(f"## {icon} {title}")
    if subtitle:
        st.caption(subtitle)
    if show_divider:
        st.divider()

def breadcrumb(*items):
    st.caption("  >  ".join(items))

def page_actions(left_label=None,right_label=None):
    c1,c2=st.columns([1,1])
    left=False; right=False
    with c1:
        if left_label:
            left=st.button(left_label,use_container_width=True)
    with c2:
        if right_label:
            right=st.button(right_label,use_container_width=True)
    return left,right

def info_banner(text:str):
    st.info(text)
