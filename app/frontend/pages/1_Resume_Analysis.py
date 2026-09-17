import os
import sys
import streamlit as st

ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../..")
)

if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
from app.parser.resume_parser import extract_resume_text
from app.nlp.skill_extractor import extract_skills
from styles import apply_dark_theme

st.set_page_config(
    page_title="Resume Analysis",
    page_icon="📄",
    layout="wide"
)
apply_dark_theme()

st.title("📄 Resume Analysis")

st.write(
    "Upload your resume and let the system extract your technical skills."
)


resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)


if resume:

    st.success(f"Uploaded: {resume.name}")

    extracted_text = extract_resume_text(resume)

    skills = extract_skills(extracted_text)


    # Save information globally
    st.session_state.resume_text = extracted_text
    st.session_state.resume_skills = skills


    st.markdown("---")

    st.subheader("🛠️ Detected Skills")

    if skills:

        columns = st.columns(3)

        for index, skill in enumerate(skills):

            with columns[index % 3]:
                st.success(skill)

    else:

        st.warning("No known technical skills detected.")


    st.markdown("---")

    with st.expander("📄 View Extracted Resume Text"):

        st.text_area(
            "Resume Content",
            extracted_text,
            height=400
        )

else:

    st.info(
        "Upload a PDF or DOCX resume to begin analysis."
    )