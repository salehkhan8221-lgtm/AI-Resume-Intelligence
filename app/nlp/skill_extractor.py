import re


# ============================================================
# TECHNICAL SKILLS
# ============================================================

TECHNICAL_SKILLS = [

    # Programming Languages
    "python",
    "java",
    "c++",
    "c",
    "c#",
    "javascript",
    "typescript",
    "go",
    "rust",
    "ruby",
    "php",

    # Databases
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",
    "redis",
    "oracle",

    # Data Science
    "pandas",
    "numpy",
    "scikit-learn",
    "matplotlib",
    "seaborn",
    "scipy",
    "statistics",
    "data analysis",
    "data visualization",

    # AI / Machine Learning
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "ai",
    "nlp",
    "natural language processing",
    "computer vision",
    "tensorflow",
    "pytorch",
    "keras",
    "transformers",
    "llm",
    "large language models",
    "generative ai",

    # Web Development
    "html",
    "css",
    "javascript",
    "react",
    "angular",
    "vue",
    "node.js",
    "nodejs",
    "fastapi",
    "flask",
    "django",
    "streamlit",

    # APIs
    "api",
    "apis",
    "rest api",
    "rest apis",
    "restful api",
    "graphql",

    # DevOps / Cloud
    "git",
    "github",
    "gitlab",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
    "cloud computing",
    "cloud platforms",
    "cloud-native",
    "cloud native",
    "devops",
    "ci/cd",
    "ci cd",
    "continuous integration",
    "continuous deployment",
    "jenkins",
    "terraform",

    # Software Engineering
    "software engineering",
    "software development",
    "software development lifecycle",
    "sdlc",
    "unit testing",
    "automated testing",
    "software testing",
    "test automation",
    "secure coding",
    "code quality",
    "clean code",
    "version control",
    "scalable software",
    "software architecture",

    # Containers / Infrastructure
    "containerization",
    "containers",
    "virtualization",
    "on-premises",
    "on premise",
    "networking",

    # Automation
    "automation",
    "workflow automation",
    "intelligent automation",
    "ai-powered automation",
    "scripting",

    # Tools
    "jira",
    "postman",
    "linux",
    "windows",
    "excel",
    "power bi",
    "tableau",

    # Existing project-related skill
    "cloudsim",

    # CS Fundamentals
    "data structures",
    "algorithms",
    "object oriented programming",
    "oop",
]


# ============================================================
# SOFT SKILLS
# ============================================================

SOFT_SKILLS = [

    "communication",
    "written communication",
    "verbal communication",
    "collaboration",
    "teamwork",
    "leadership",
    "problem solving",
    "problem-solving",
    "critical thinking",
    "analytical thinking",
    "creativity",
    "adaptability",
    "flexibility",
    "time management",
    "organization",
    "presentation",
    "presentation skills",
    "interpersonal skills",
    "customer focus",
    "customer service",
    "curiosity",
    "empathy",
    "coaching",
    "mentoring",
    "decision making",
    "decision-making",
    "attention to detail",
]


# ============================================================
# PROFESSIONAL / ENGINEERING SKILLS
# ============================================================

PROFESSIONAL_SKILLS = [

    "agile",
    "scrum",
    "design thinking",
    "project management",
    "product management",
    "technical design",
    "technical documentation",
    "requirements analysis",
    "requirements gathering",
    "software development lifecycle",
    "sdlc",
    "code review",
    "best practices",
    "engineering practices",
    "secure development",
    "release management",
    "product development",
]


# ============================================================
# ALIASES
# ============================================================

# Different ways of writing the same skill are mapped
# to one canonical skill.

SKILL_ALIASES = {

    # AI
    "ai": "artificial intelligence",
    "artificial intelligence": "artificial intelligence",

    # NLP
    "natural language processing": "nlp",

    # Machine Learning
    "ml": "machine learning",
    "machine-learning": "machine learning",

    # Deep Learning
    "deep-learning": "deep learning",

    # APIs
    "api": "api",
    "apis": "api",
    "rest api": "rest api",
    "rest apis": "rest api",
    "restful api": "rest api",

    # CI/CD
    "ci/cd": "ci/cd",
    "ci cd": "ci/cd",
    "continuous integration": "ci/cd",
    "continuous deployment": "ci/cd",

    # Cloud
    "cloud-native": "cloud native",
    "cloud native": "cloud native",

    # Node
    "nodejs": "node.js",

    # C++
    "c++": "c++",

    # OOP
    "oop": "object oriented programming",

    # Problem solving
    "problem-solving": "problem solving",

    # Decision making
    "decision-making": "decision making",

    # SDLC
    "sdlc": "software development lifecycle",
}


# ============================================================
# COMBINE ALL SKILLS
# ============================================================

ALL_SKILLS = (
    TECHNICAL_SKILLS
    + SOFT_SKILLS
    + PROFESSIONAL_SKILLS
)


# Remove duplicates
ALL_SKILLS = list(set(ALL_SKILLS))


# ============================================================
# SKILL EXTRACTION
# ============================================================

def extract_skills(text):
    """
    Extract technical, soft and professional skills
    from resume or job description text.

    Returns:
        list: detected canonical skills
    """

    if not text:
        return []

    text = text.lower()

    found_skills = set()

    # Check longer phrases first.
    # This helps avoid partial matches.
    sorted_skills = sorted(
        ALL_SKILLS,
        key=len,
        reverse=True
    )

    for skill in sorted_skills:

        # Escape regex special characters
        escaped_skill = re.escape(skill)

        # Match complete terms without requiring
        # traditional word boundaries.
        pattern = r"(?<!\w)" + escaped_skill + r"(?!\w)"

        if re.search(pattern, text):

            canonical_skill = SKILL_ALIASES.get(
                skill,
                skill
            )

            found_skills.add(canonical_skill)

    return sorted(found_skills)