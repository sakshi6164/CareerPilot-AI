"""
CareerPilot AI Pro
components/cards.py
"""

import streamlit as st

def metric_card(title:str,value,help_text:str="",icon:str="📊"):
    st.markdown(f"""
    <div style="
    background:#111827;
    border:1px solid #334155;
    border-radius:14px;
    padding:18px;
    text-align:center;">
    <div style="font-size:30px;">{icon}</div>
    <div style="font-size:14px;color:#94A3B8;">{title}</div>
    <div style="font-size:28px;font-weight:bold;">{value}</div>
    <div style="font-size:12px;color:#94A3B8;">{help_text}</div>
    </div>
    """,unsafe_allow_html=True)

def feature_card(title:str,description:str,icon:str="✨"):
    st.markdown(f"""
    <div style="
    background:#1E293B;
    border:1px solid #334155;
    border-radius:14px;
    padding:20px;
    min-height:170px;
    margin-bottom:15px;">
    <h3>{icon} {title}</h3>
    <p>{description}</p>
    </div>
    """,unsafe_allow_html=True)

def status_card(title:str,message:str,status="info"):
    if status=="success":
        st.success(f"**{title}**\n\n{message}")
    elif status=="warning":
        st.warning(f"**{title}**\n\n{message}")
    elif status=="error":
        st.error(f"**{title}**\n\n{message}")
    else:
        st.info(f"**{title}**\n\n{message}")

def stat_grid(stats:dict):
    cols=st.columns(len(stats))
    for col,(k,v) in zip(cols,stats.items()):
        with col:
            metric_card(k,v)

def section_card(title:str):
    st.markdown(f"### {title}")
