from app.nlp.skill_normalizer import normalize_skills

def calculate_skill_match(resume_skills, job_skills):

    """
    Compare resume skills with job-required skills.
    """
    resume_skills = normalize_skills(resume_skills)
    job_skills = normalize_skills(job_skills)
    
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = sorted(resume_set.intersection(job_set))
    missing_skills = sorted(job_set - resume_set)

    if len(job_set) == 0:
        score = 0
    else:
        score = (len(matched_skills) / len(job_set)) * 100

    return {
        "score": round(score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }