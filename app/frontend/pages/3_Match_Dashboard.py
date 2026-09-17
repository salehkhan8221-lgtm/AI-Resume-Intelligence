import streamlit as st

from app.nlp.matching_engine import calculate_skill_match
from app.nlp.skill_gap_analyzer import analyze_skill_gaps
from styles import apply_dark_theme

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Match Dashboard",
    page_icon="📊",
    layout="wide"
)
apply_dark_theme()
# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📊 Resume–Job Match Dashboard")

st.write(
    "Compare your resume with the selected job description "
    "and identify your strengths and skill gaps."
)


# --------------------------------------------------
# CHECK RESUME
# --------------------------------------------------

if not st.session_state.resume_skills:

    st.warning(
        "⚠️ Please upload and analyze your resume first."
    )

    st.page_link(
        "pages/1_Resume_Analysis.py",
        label="📄 Go to Resume Analysis →"
    )

    st.stop()


# --------------------------------------------------
# CHECK JOB DESCRIPTION
# --------------------------------------------------

if not st.session_state.job_skills:

    st.warning(
        "⚠️ Please analyze a job description first."
    )

    st.page_link(
        "pages/2_Job_Description.py",
        label="💼 Go to Job Description →"
    )

    st.stop()


# --------------------------------------------------
# CALCULATE MATCH
# --------------------------------------------------

result = calculate_skill_match(
    resume_skills=st.session_state.resume_skills,
    job_skills=st.session_state.job_skills
)

st.session_state.match_result = result


score = result["score"]
matched_skills = result["matched_skills"]
missing_skills = result["missing_skills"]

# Analyze missing skills by priority
skill_gap = analyze_skill_gaps(missing_skills)

high_priority = skill_gap["high"]
medium_priority = skill_gap["medium"]
low_priority = skill_gap["low"]

resume_count = len(st.session_state.resume_skills)
job_count = len(st.session_state.job_skills)
matched_count = len(matched_skills)
missing_count = len(missing_skills)


# --------------------------------------------------
# MATCH CATEGORY
# --------------------------------------------------

if score >= 80:

    match_status = "🟢 Strong Match"
    status_message = (
        "Your profile aligns very well with the requirements."
    )

elif score >= 60:

    match_status = "🟡 Good Match"
    status_message = (
        "Your profile matches most of the required skills."
    )

elif score >= 40:

    match_status = "🟠 Moderate Match"
    status_message = (
        "You have several relevant skills, but some important "
        "skills are missing."
    )

else:

    match_status = "🔴 Low Match"
    status_message = (
        "There are significant skill gaps for this position."
    )


# --------------------------------------------------
# OVERALL MATCH
# --------------------------------------------------

st.markdown("---")

st.subheader("🎯 Overall Compatibility")

score_col, status_col = st.columns([1, 2])

with score_col:

    st.metric(
        "Match Score",
        f"{score}%"
    )

with status_col:

    st.markdown(f"### {match_status}")
    st.write(status_message)


# --------------------------------------------------
# PROGRESS BAR
# --------------------------------------------------

st.progress(
    min(score / 100, 1.0)
)

st.markdown("---")


# --------------------------------------------------
# SKILL SUMMARY
# --------------------------------------------------

st.subheader("📈 Skill Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Resume Skills",
        resume_count
    )

with col2:

    st.metric(
        "Required Skills",
        job_count
    )

with col3:

    st.metric(
        "Matched Skills",
        matched_count
    )

with col4:

    st.metric(
        "Missing Skills",
        missing_count
    )


st.markdown("---")


# --------------------------------------------------
# MATCHED AND MISSING SKILLS
# --------------------------------------------------

left, right = st.columns(2)


# --------------------------------------------------
# MATCHED SKILLS
# --------------------------------------------------

with left:

    st.subheader("✅ Matched Skills")

    if matched_skills:

        st.success(
            f"{matched_count} required skill(s) found in your resume."
        )

        for skill in matched_skills:

            st.markdown(
                f"🟢 **{skill}**"
            )

    else:

        st.warning(
            "No matching skills were found."
        )


# --------------------------------------------------
# MISSING SKILLS
# --------------------------------------------------

with right:

    st.subheader("❌ Missing Skills")

    if missing_skills:

        st.error(
            f"{missing_count} required skill(s) are missing."
        )

        for skill in missing_skills:

            st.markdown(
                f"🔴 **{skill}**"
            )

    else:

        st.success(
            "Excellent! No required skills are missing."
        )


st.markdown("---")


# --------------------------------------------------
# INTELLIGENT SKILL GAP ANALYSIS
# --------------------------------------------------

st.subheader("🔍 Intelligent Skill Gap Analysis")

st.write(
    "The system categorizes missing skills based on their "
    "importance for the target software-development role."
)


# -----------------------------
# HIGH PRIORITY
# -----------------------------

if high_priority:

    st.markdown("### 🔴 High Priority")

    st.write(
        "These skills should be your primary focus."
    )

    for skill in high_priority:

        st.error(
            f"🔴 {skill}"
        )

else:

    st.success(
        "No high-priority skill gaps detected."
    )


# -----------------------------
# MEDIUM PRIORITY
# -----------------------------

if medium_priority:

    st.markdown("### 🟡 Medium Priority")

    st.write(
        "These skills can strengthen your profile."
    )

    for skill in medium_priority:

        st.warning(
            f"🟡 {skill}"
        )

else:

    st.info(
        "No medium-priority skill gaps detected."
    )


# -----------------------------
# LOW PRIORITY
# -----------------------------

if low_priority:

    st.markdown("### 🟢 Low Priority")

    st.write(
        "These skills are useful but less critical."
    )

    for skill in low_priority:

        st.info(
            f"🟢 {skill}"
        )

else:

    st.success(
        "No low-priority skill gaps detected."
    )


# --------------------------------------------------
# RECOMMENDATION
# --------------------------------------------------

st.subheader("💡 Recommendation")

if score >= 80:

    st.success(
        "Strong match! Your resume covers most of the required "
        "skills. You can consider applying for this position."
    )

elif score >= 60:

    st.info(
        "Good match! Your profile is relevant, but improving "
        "the missing skills could increase your compatibility."
    )

elif score >= 40:

    st.warning(
        "Moderate match. Focus on the missing technical skills "
        "before applying to improve your profile."
    )

else:

    st.error(
        "Low match. Consider developing the missing skills "
        "and tailoring your resume to this job description."
    )


# --------------------------------------------------
# NEXT ACTIONS
# --------------------------------------------------

st.markdown("---")

st.subheader("🚀 Next Actions")

col1, col2 = st.columns(2)

with col1:

    st.page_link(
        "pages/1_Resume_Analysis.py",
        label="📄 Analyze Resume Again"
    )

with col2:

    st.page_link(
        "pages/2_Job_Description.py",
        label="💼 Try Another Job Description"
    )