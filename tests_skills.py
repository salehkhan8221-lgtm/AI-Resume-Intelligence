from app.nlp.skill_extractor import extract_skills


resume_text = """
I have experience with Python, SQL, Pandas, NumPy,
Machine Learning, Docker, Git and CloudSim.
"""


skills = extract_skills(resume_text)

print("Detected Skills:")
print(skills)