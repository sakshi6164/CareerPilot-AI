import streamlit as st

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.hero {
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    padding:40px;
    border-radius:20px;
    color:white;
    text-align:center;
    margin-bottom:30px;
}

.feature-card{
    background:#1e293b;
    padding:25px;
    border-radius:15px;
    border:1px solid #334155;
    min-height:180px;
}

.metric-card{
    background:#0f172a;
    padding:20px;
    border-radius:15px;
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🚀 CareerPilot AI")

st.sidebar.success("Version 2.0")

st.sidebar.markdown("---")

st.sidebar.write("### Available Modules")

st.sidebar.write("🏠 Home")
st.sidebar.write("📄 Resume Analyzer")
st.sidebar.write("📝 Resume Builder")
st.sidebar.write("💼 Job Matcher")
st.sidebar.write("✉ Cover Letter Generator")
st.sidebar.write("🎯 Career Roadmap")
st.sidebar.write("🎤 Interview Preparation")
st.sidebar.write("📊 Dashboard")

st.sidebar.markdown("---")

st.sidebar.info(
"""
Open the pages from the sidebar after we add them.

This project uses:

• Streamlit

• OpenRouter AI

• Professional ATS Analysis

• Resume Intelligence
"""
)

# ---------------- HERO ---------------- #

st.markdown("""
<div class="hero">

<h1>🚀 CareerPilot AI</h1>

<h3>Your Complete AI Career Assistant</h3>

<p>
Analyze resumes, match jobs, generate cover letters,
prepare for interviews and build your career using AI.
</p>

</div>
""", unsafe_allow_html=True)

# ---------------- METRICS ---------------- #

st.subheader("Platform Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Modules", "7")

with c2:
    st.metric("AI Powered", "100%")

with c3:
    st.metric("Reports", "PDF")

with c4:
    st.metric("ATS Engine", "Professional")

st.divider()

# ---------------- FEATURES ---------------- #

st.header("✨ Features")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
<div class="feature-card">

<h3>📄 AI Resume Analyzer</h3>

<p>
Upload your resume and compare it with a Job Description.
Get ATS score, strengths, weaknesses, missing skills,
and improvement suggestions.
</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

<h3>💼 AI Job Matcher</h3>

<p>
Find how well your resume matches a job.
Receive personalized recommendations to improve
your chances.
</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

<h3>🎤 Interview Preparation</h3>

<p>
Generate interview questions,
technical questions,
HR questions,
and AI feedback.
</p>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="feature-card">

<h3>📝 Resume Builder</h3>

<p>
Generate a professional ATS-friendly resume
using AI with modern formatting.
</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

<h3>✉ AI Cover Letter Generator</h3>

<p>
Generate customized cover letters
for every company and role.
</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

<h3>🎯 Career Roadmap</h3>

<p>
Generate personalized learning paths,
skills roadmap,
and certification recommendations.
</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------- WHY CHOOSE ---------------- #

st.header("Why CareerPilot AI?")

left, right = st.columns(2)

with left:

    st.success("✔ Professional ATS Analysis")

    st.success("✔ OpenRouter AI Models")

    st.success("✔ Resume Intelligence")

    st.success("✔ Career Recommendations")

    st.success("✔ Multi-page Professional UI")

with right:

    st.info("📈 Resume Insights")

    st.info("💼 Job Matching")

    st.info("🎤 Interview Preparation")

    st.info("📄 PDF Reports")

    st.info("🚀 Career Growth")

st.divider()

# ---------------- GET STARTED ---------------- #

st.header("🚀 Get Started")

st.write(
    """
Use the navigation menu on the left.

As we build Version 2, each module will appear
there automatically as a separate page.
"""
)

st.button(
    "Open Resume Analyzer from Sidebar",
    use_container_width=True
)

st.divider()

st.markdown(
"""
<div class="footer">

CareerPilot AI • Version 2.0

Built with Streamlit + OpenRouter AI

</div>
""",
unsafe_allow_html=True
)