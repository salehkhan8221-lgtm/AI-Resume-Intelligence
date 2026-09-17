import streamlit as st

from app.nlp.skill_extractor import extract_skills
from app.nlp.jd_analyzer import analyze_job_description
from styles import apply_dark_theme

st.set_page_config(
    page_title="Job Description",
    page_icon="💼",
    layout="wide"
)
apply_dark_theme()

st.title("💼 Job Description Analysis")

st.write(
    "Paste the job description to identify the required skills."
)


job_description = st.text_area(
    "Job Description",
    height=350,
    placeholder="""
Example:

We are looking for a Python Developer.

Requirements:
Python
FastAPI
SQL
PostgreSQL
Docker
Git
REST APIs
Machine Learning
Pandas
NumPy
"""
)


if st.button("🔍 Analyze Job Description"):

    if not job_description.strip():

        st.warning("Please enter a job description.")

    else:

        job_skills = extract_skills(job_description)
        jd_analysis = analyze_job_description(job_description)

        st.session_state.job_description = job_description
        st.session_state.job_skills = job_skills
        st.session_state.jd_analysis = jd_analysis


        st.success("Job description analyzed successfully!")

        


        st.markdown("---")

        st.subheader("🎯 Required Skills")

        


        if job_skills:

            columns = st.columns(3)

            for index, skill in enumerate(job_skills):

                with columns[index % 3]:
                    st.info(skill)

        else:

            st.warning(
                "No known technical skills were detected."
            )