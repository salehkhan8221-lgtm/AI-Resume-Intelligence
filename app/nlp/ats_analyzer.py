# app/nlp/ats_analyzer.py


REQUIRED_SECTIONS = {
    "summary": [
        "summary",
        "profile",
        "objective"
    ],

    "education": [
        "education",
        "academic"
    ],

    "skills": [
        "skills",
        "technical skills",
        "technical skills:"
    ],

    "projects": [
        "projects",
        "project"
    ],

    "experience": [
        "experience",
        "work experience",
        "employment"
    ]
}


def check_sections(resume_text):
    """
    Check whether important resume sections exist.
    """

    text = resume_text.lower()

    section_results = {}

    for section, keywords in REQUIRED_SECTIONS.items():

        found = False

        for keyword in keywords:

            if keyword in text:
                found = True
                break

        section_results[section] = found

    return section_results


def calculate_section_score(section_results):
    """
    Calculate score based on important resume sections.
    """

    total_sections = len(section_results)

    completed_sections = sum(
        section_results.values()
    )

    if total_sections == 0:
        return 0

    score = (
        completed_sections / total_sections
    ) * 100

    return round(score, 2)


def calculate_keyword_coverage(
    resume_skills,
    job_skills
):
    """
    Calculate how many required job skills
    are present in the resume.
    """

    if not job_skills:
        return 0

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched = resume_set.intersection(job_set)

    coverage = (
        len(matched) / len(job_set)
    ) * 100

    return round(coverage, 2)


def analyze_resume(
    resume_text,
    resume_skills,
    job_skills
):
    """
    Perform complete ATS-style resume analysis.
    """

    sections = check_sections(
        resume_text
    )

    section_score = calculate_section_score(
        sections
    )

    keyword_score = calculate_keyword_coverage(
        resume_skills,
        job_skills
    )

    # Overall ATS score
    ats_score = (
        section_score * 0.4
        +
        keyword_score * 0.6
    )

    return {
        "ats_score": round(ats_score, 2),
        "section_score": section_score,
        "keyword_score": keyword_score,
        "sections": sections
    }