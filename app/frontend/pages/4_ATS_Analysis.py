import os
import sys
import streamlit as st

ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../..")
)

if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app.nlp.ats_analyzer import analyze_resume
from styles import apply_dark_theme


st.set_page_config(
    page_title="ATS Analysis",
    page_icon="📋",
    layout="wide"
)
apply_dark_theme()

st.title("📋 ATS Resume Analysis")

st.write(
    "Evaluate your resume structure and job-specific "
    "keyword coverage."
)

st.markdown("---")


# --------------------------------------------------
# CHECK RESUME
# --------------------------------------------------

if not st.session_state.resume_text:

    st.warning(
        "Please upload and analyze your resume first."
    )

    st.stop()


# --------------------------------------------------
# RUN ATS ANALYSIS
# --------------------------------------------------

result = analyze_resume(
    resume_text=st.session_state.resume_text,
    resume_skills=st.session_state.resume_skills,
    job_skills=st.session_state.job_skills
)


# --------------------------------------------------
# MAIN SCORE
# --------------------------------------------------

ats_score = result["ats_score"]

st.subheader("🎯 ATS Score")

st.metric(
    "Overall ATS Score",
    f"{ats_score}%"
)

st.progress(
    min(ats_score / 100, 1.0)
)


st.markdown("---")


# --------------------------------------------------
# SCORE BREAKDOWN
# --------------------------------------------------

st.subheader("📊 Score Breakdown")


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "Resume Structure",
        f"{result['section_score']}%"
    )


with col2:

    st.metric(
        "JD Keyword Coverage",
        f"{result['keyword_score']}%"
    )


st.markdown("---")


# --------------------------------------------------
# RESUME SECTIONS
# --------------------------------------------------

st.subheader("📑 Resume Section Analysis")

sections = result["sections"]


col1, col2 = st.columns(2)


with col1:

    st.write("### Required Sections")

    for section, found in sections.items():

        section_name = section.title()

        if found:

            st.success(
                f"✓ {section_name}"
            )

        else:

            st.error(
                f"✗ {section_name}"
            )


with col2:

    st.write("### Analysis")

    completed = sum(
        sections.values()
    )

    total = len(sections)

    st.info(
        f"{completed} out of {total} "
        "important resume sections detected."
    )


st.markdown("---")


# --------------------------------------------------
# RECOMMENDATION
# --------------------------------------------------

st.subheader("💡 ATS Recommendation")


if ats_score >= 80:

    st.success(
        "Excellent ATS readiness! Your resume has "
        "strong structure and good keyword coverage."
    )

elif ats_score >= 60:

    st.info(
        "Good ATS readiness. Consider improving "
        "your missing sections or job-specific keywords."
    )

elif ats_score >= 40:

    st.warning(
        "Moderate ATS readiness. Your resume needs "
        "improvement in structure and keyword coverage."
    )

else:

    st.error(
        "Low ATS readiness. Improve your resume "
        "structure and add relevant job-specific skills."
    )


st.markdown("---")


# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------

st.subheader("🚀 Next Actions")


col1, col2 = st.columns(2)


with col1:

    st.page_link(
        "pages/1_Resume_Analysis.py",
        label="📄 Analyze Resume Again"
    )


with col2:

    st.page_link(
        "pages/3_Match_Dashboard.py",
        label="📊 View Match Dashboard"
    )