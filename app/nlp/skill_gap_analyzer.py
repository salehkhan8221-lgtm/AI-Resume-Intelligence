# app/nlp/skill_gap_analyzer.py


# Skills that are generally more important
# for technical software-development roles.
HIGH_PRIORITY_SKILLS = {
    "python",
    "java",
    "c++",
    "javascript",
    "sql",
    "data structures",
    "algorithms",
    "machine learning",
    "docker",
    "fastapi",
    "rest api",
}


# Skills that are useful but usually secondary
# to the core technical requirements.
MEDIUM_PRIORITY_SKILLS = {
    "git",
    "github",
    "pandas",
    "numpy",
    "scikit-learn",
    "html",
    "css",
    "mysql",
    "postgresql",
    "streamlit",
}


def classify_skill_priority(skill):
    """
    Classify a missing skill as High, Medium, or Low priority.
    """

    skill = skill.lower().strip()

    if skill in HIGH_PRIORITY_SKILLS:
        return "High"

    elif skill in MEDIUM_PRIORITY_SKILLS:
        return "Medium"

    else:
        return "Low"


def analyze_skill_gaps(missing_skills):
    """
    Analyze missing skills and divide them by priority.
    """

    high_priority = []
    medium_priority = []
    low_priority = []

    for skill in missing_skills:

        priority = classify_skill_priority(skill)

        if priority == "High":
            high_priority.append(skill)

        elif priority == "Medium":
            medium_priority.append(skill)

        else:
            low_priority.append(skill)

    return {
        "high": sorted(high_priority),
        "medium": sorted(medium_priority),
        "low": sorted(low_priority)
    }