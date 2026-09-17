from app.nlp.ats_analyzer import analyze_resume


resume_text = """
Summary

Computer Science graduate looking for a software developer role.

Education

B.Tech in Computer Science.

Technical Skills

Python
SQL
Git
Docker

Projects

AI Resume Intelligence

Experience

Fresher
"""


resume_skills = [
    "python",
    "sql",
    "git",
    "docker"
]


job_skills = [
    "python",
    "sql",
    "git",
    "docker",
    "fastapi"
]


result = analyze_resume(
    resume_text,
    resume_skills,
    job_skills
)


print("ATS Score:", result["ats_score"])
print("Section Score:", result["section_score"])
print("Keyword Score:", result["keyword_score"])
print("Sections:", result["sections"])