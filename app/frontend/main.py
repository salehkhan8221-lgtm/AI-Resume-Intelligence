import streamlit as st
from styles import apply_dark_theme


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Resume Intelligence",
    page_icon="📄",
    layout="wide"
)
apply_dark_theme()


# ==================================================
# CUSTOM STYLING
# ==================================================

st.markdown(
    """
    <style>

    /* Hide Streamlit's automatic page navigation */
    [data-testid="stSidebarNav"] {
        display: none;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #080C12;
        border-right: 1px solid #1F2937;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.5rem;
    }

    /* Main application */
    .stApp {
        background-color: #0B0F14;
        color: #FFFFFF;
    }

    /* Headings */
    h1, h2, h3 {
        color: #FFFFFF !important;
    }

    /* Normal text */
    p, span, label {
        color: #E5E7EB;
    }

    /* Dividers */
    hr {
        border-color: #1F2937;
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        background-color: #111827;
        border: 1px solid #1F2937;
        border-radius: 12px;
        padding: 18px;
    }

    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
    }

    [data-testid="stMetricLabel"] {
        color: #94A3B8 !important;
    }

    /* Buttons */
    .stButton > button {
        background-color: #2563EB;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #3B82F6;
        color: white;
    }

    /* Text inputs */
    input, textarea {
        background-color: #111827 !important;
        color: #FFFFFF !important;
        border: 1px solid #374151 !important;
    }

    /* Links */
    a {
        color: #60A5FA !important;
    }

    /* Streamlit top toolbar */
       [data-testid="stHeader"] {
       background-color: #080C12 !important;
    }

    /* Header decoration line */
       [data-testid="stDecoration"] {
       background-color: #080C12 !important;
    }

    /* Toolbar buttons/icons */
       [data-testid="stHeader"] button {
       color: #FFFFFF !important;
    }

    /* Top-right toolbar area */
       [data-testid="stToolbar"] {
       background-color: #080C12 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# SESSION STATE
# ==================================================

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "resume_skills" not in st.session_state:
    st.session_state.resume_skills = []

if "job_description" not in st.session_state:
    st.session_state.job_description = ""

if "job_skills" not in st.session_state:
    st.session_state.job_skills = []

if "match_result" not in st.session_state:
    st.session_state.match_result = None


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("📄 AI Resume")

st.sidebar.caption(
    "Resume Intelligence Platform"
)

st.sidebar.divider()

st.sidebar.subheader("Workspace")

st.sidebar.page_link(
    "pages/1_Resume_Analysis.py",
    label="📄 Resume Analysis"
)

st.sidebar.page_link(
    "pages/2_Job_Description.py",
    label="💼 Job Description"
)

st.sidebar.page_link(
    "pages/3_Match_Dashboard.py",
    label="📊 Match Dashboard"
)

st.sidebar.page_link(
    "pages/4_ATS_Analysis.py",
    label="🎯 ATS Analysis"
)

st.sidebar.divider()

st.sidebar.subheader("Analysis Status")

if st.session_state.resume_text:
    st.sidebar.success("Resume • Ready")
else:
    st.sidebar.info("Resume • Not Ready")

if st.session_state.job_description:
    st.sidebar.success("Job Description • Ready")
else:
    st.sidebar.info("Job Description • Not Ready")

if st.session_state.match_result:

    score = st.session_state.match_result["score"]

    st.sidebar.metric(
        "Match Score",
        f"{score}%"
    )

else:

    st.sidebar.metric(
        "Match Score",
        "—"
    )

st.sidebar.divider()

st.sidebar.caption(
    "AI Resume Intelligence • v1.0"
)


# ==================================================
# HERO SECTION
# ==================================================

st.title("📄 AI Resume Intelligence")

st.subheader(
    "Smart Resume & Job Matching Platform"
)

st.caption(
    "Analyze your resume against job requirements using "
    "NLP-based skill extraction, intelligent matching, "
    "skill-gap detection and ATS analysis."
)

st.divider()

st.markdown(
    """
    <style>

    /* Main page title */
    h1 {
        font-size: 2.7rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.2rem !important;
    }

    /* Subtitle */
    h2 {
        font-size: 1.35rem !important;
        font-weight: 500 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ==================================================
# ANALYSIS OVERVIEW
# ==================================================

st.markdown(
    '<div class="section-title">📊 Analysis Overview</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)


# Resume
with col1:

    if st.session_state.resume_text:

        st.metric(
            "📄 Resume",
            "Ready"
        )

    else:

        st.metric(
            "📄 Resume",
            "Not Ready"
        )


# Resume skills
with col2:

    st.metric(
        "🧠 Resume Skills",
        len(st.session_state.resume_skills)
    )


# JD skills
with col3:

    st.metric(
        "💼 JD Skills",
        len(st.session_state.job_skills)
    )


# Match score
with col4:

    if st.session_state.match_result:

        score = st.session_state.match_result["score"]

        st.metric(
            "🎯 Match Score",
            f"{score}%"
        )

    else:

        st.metric(
            "🎯 Match Score",
            "—"
        )


st.divider()


# ==================================================
# GET STARTED
# ==================================================

st.markdown(
    '<div class="section-title">🚀 Get Started</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown("### 📄 Resume Analysis")

    st.write(
        "Upload your PDF or DOCX resume and "
        "extract relevant technical skills."
    )

    st.page_link(
        "pages/1_Resume_Analysis.py",
        label="Analyze Resume →",
        icon="📄"
    )


with col2:

    st.markdown("### 💼 Job Description")

    st.write(
        "Paste a job description and identify "
        "the skills required for the role."
    )

    st.page_link(
        "pages/2_Job_Description.py",
        label="Analyze Job →",
        icon="💼"
    )


with col3:

    st.markdown("### 📊 Match Analysis")

    st.write(
        "Compare resume skills with job requirements "
        "and identify missing skills."
    )

    st.page_link(
        "pages/3_Match_Dashboard.py",
        label="View Match →",
        icon="📊"
    )


st.divider()


# ==================================================
# WORKFLOW
# ==================================================

st.markdown(
    '<div class="section-title">⚙️ How It Works</div>',
    unsafe_allow_html=True
)

w1, w2, w3, w4 = st.columns(4)


with w1:

    st.markdown(
        """
        <div class="workflow-card">

        <div class="workflow-number">STEP 01</div>

        <div class="workflow-title">
        📄 Upload Resume
        </div>

        <div class="workflow-text">
        Upload your resume and extract
        relevant technical skills.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with w2:

    st.markdown(
        """
        <div class="workflow-card">

        <div class="workflow-number">STEP 02</div>

        <div class="workflow-title">
        💼 Analyze Job
        </div>

        <div class="workflow-text">
        Extract skills and requirements
        from the target job description.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with w3:

    st.markdown(
        """
        <div class="workflow-card">

        <div class="workflow-number">STEP 03</div>

        <div class="workflow-title">
        🎯 Match Skills
        </div>

        <div class="workflow-text">
        Compare resume skills with
        job-required skills.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with w4:

    st.markdown(
        """
        <div class="workflow-card">

        <div class="workflow-number">STEP 04</div>

        <div class="workflow-title">
        📋 ATS Analysis
        </div>

        <div class="workflow-text">
        Evaluate resume ATS compatibility
        and identify improvement areas.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# ==================================================
# CURRENT ANALYSIS
# ==================================================

st.markdown(
    '<div class="section-title">📈 Current Analysis</div>',
    unsafe_allow_html=True
)


if st.session_state.match_result:

    result = st.session_state.match_result

    score = result["score"]

    matched_count = len(
        result.get("matched_skills", [])
    )

    missing_count = len(
        result.get("missing_skills", [])
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🎯 Compatibility",
            f"{score}%"
        )

        st.progress(score / 100)


    with col2:

        st.metric(
            "✅ Matched Skills",
            matched_count
        )


    with col3:

        st.metric(
            "❌ Missing Skills",
            missing_count
        )


    if score >= 80:

        st.success(
            "Strong match! Your resume aligns well "
            "with the selected job."
        )

    elif score >= 60:

        st.info(
            "Good match. Improving the missing skills "
            "could strengthen your profile."
        )

    elif score >= 40:

        st.warning(
            "Moderate match. Consider working on "
            "the missing technical skills."
        )

    else:

        st.error(
            "Low match. Significant skill gaps exist "
            "for this position."
        )

else:

    st.info(
        "No analysis available yet. Start by uploading "
        "your resume and analyzing a job description."
    )


# ==================================================
# FINAL ACTIONS
# ==================================================

st.divider()

st.markdown(
    '<div class="section-title">🚀 Continue Your Analysis</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.page_link(
        "pages/1_Resume_Analysis.py",
        label="📄 Analyze Resume Again"
    )


with col2:

    st.page_link(
        "pages/4_ATS_Analysis.py",
        label="🎯 Open ATS Analysis"
    )