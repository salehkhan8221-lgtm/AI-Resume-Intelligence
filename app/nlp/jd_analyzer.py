import re
from app.nlp.skill_extractor import extract_skills

def extract_experience(text):
    """
    Extract required years of experience from a job description.
    """

    text = text.lower()

    # Fresher-friendly indicators
    fresher_patterns = [
        r"\bfreshers?\b",
        r"\bentry[\s-]?level\b",
        r"\bno experience required\b",
        r"\b0 years?\b",
        r"\b0-1 years?\b",
        r"\b0-2 years?\b",
    ]

    is_fresher_friendly = any(
        re.search(pattern, text)
        for pattern in fresher_patterns
    )

    # Range: 2-5 years
    range_pattern = r"(\d+)\s*[-–]\s*(\d+)\s*(?:years?|yrs?)"

    range_match = re.search(range_pattern, text)

    if range_match:
        return {
            "min_years": int(range_match.group(1)),
            "max_years": int(range_match.group(2)),
            "is_fresher_friendly": is_fresher_friendly,
        }

    # 5+ years / 5 or more years
    plus_patterns = [
        r"(\d+)\s*\+\s*(?:years?|yrs?)",
        r"(\d+)\s*or\s*more\s*(?:years?|yrs?)",
        r"minimum\s*(?:of\s*)?(\d+)\s*(?:years?|yrs?)",
        r"at\s*least\s*(\d+)\s*(?:years?|yrs?)",
    ]

    for pattern in plus_patterns:
        match = re.search(pattern, text)

        if match:
            return {
                "min_years": int(match.group(1)),
                "max_years": None,
                "is_fresher_friendly": is_fresher_friendly,
            }

    # Simple "3 years experience"
    simple_pattern = (
        r"(\d+)\s*(?:years?|yrs?)"
        r"(?:\s+of)?\s+(?:relevant\s+)?experience"
    )

    simple_match = re.search(simple_pattern, text)

    if simple_match:
        return {
            "min_years": int(simple_match.group(1)),
            "max_years": None,
            "is_fresher_friendly": is_fresher_friendly,
        }

    return {
        "min_years": None,
        "max_years": None,
        "is_fresher_friendly": is_fresher_friendly,
    }


def extract_skill_sections(text):
    """
    Detect mandatory and preferred sections in a JD.

    This is rule-based and looks for common section headings.
    """

    lines = text.splitlines()

    mandatory = []
    preferred = []

    current_section = None

    mandatory_keywords = [
        "mandatory",
        "required",
        "requirements",
        "must have",
        "must-have",
        "essential",
        "qualifications",
    ]

    preferred_keywords = [
        "preferred",
        "nice to have",
        "nice-to-have",
        "good to have",
        "desired",
        "plus",
        "preferred qualifications",
    ]

    for line in lines:

        clean_line = line.strip()

        if not clean_line:
            continue

        lower_line = clean_line.lower()

        # Detect section
        if any(keyword in lower_line for keyword in mandatory_keywords):
            current_section = "mandatory"
            continue

        if any(keyword in lower_line for keyword in preferred_keywords):
            current_section = "preferred"
            continue

        # Store bullet/list items
        if current_section == "mandatory":
            mandatory.append(clean_line)

        elif current_section == "preferred":
            preferred.append(clean_line)

    return {
        "mandatory": mandatory,
        "preferred": preferred,
    }


def analyze_job_description(text):
    """
    Complete Job Description analysis.

    Extracts:
    - Experience requirement
    - Mandatory skills
    - Preferred skills
    """

    experience = extract_experience(text)

    sections = extract_skill_sections(text)

    mandatory_text = " ".join(sections["mandatory"])
    preferred_text = " ".join(sections["preferred"])

    mandatory_skills = extract_skills(mandatory_text)
    preferred_skills = extract_skills(preferred_text)

    return {
        "experience": experience,

        "mandatory_items": sections["mandatory"],
        "preferred_items": sections["preferred"],

        "mandatory_skills": mandatory_skills,
        "preferred_skills": preferred_skills,
    }