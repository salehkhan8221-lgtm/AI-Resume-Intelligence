from app.nlp.skill_gap_analyzer import analyze_skill_gaps


missing_skills = [
    "python",
    "fastapi",
    "pandas",
    "kubernetes"
]


result = analyze_skill_gaps(missing_skills)


print("High Priority:")
print(result["high"])

print("\nMedium Priority:")
print(result["medium"])

print("\nLow Priority:")
print(result["low"])