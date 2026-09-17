# app/nlp/skill_normalizer.py

SKILL_ALIASES = {

    # =========================
    # Technical SKILL ALIASES
    # =========================
       
    # JavaScript
    "js": "javascript",
    "javascript": "javascript",

    # Node.js
    "node": "node.js",
    "nodejs": "node.js",
    "node js": "node.js",
    "node.js": "node.js",

    # C++
    "cpp": "c++",
    "c plus plus": "c++",
    "c++": "c++",

    # C#
    "c sharp": "c#",
    "csharp": "c#",
    "c#": "c#",

    # PostgreSQL
    "postgres": "postgresql",
    "postgres db": "postgresql",
    "postgresql": "postgresql",

    # MySQL
    "mysql": "mysql",
    "mysql database": "mysql",

    # HTML
    "html": "html",
    "html5": "html",

    # CSS
    "css": "css",
    "css3": "css",

    # Git
    "git": "git",
    "git version control": "git",

    # Machine Learning
    "ml": "machine learning",
    "machine learning": "machine learning",

    # Data Structures
    "dsa": "data structures",
    "data structures": "data structures",
    "data structures and algorithms": "data structures",

    # REST API
    "rest api": "rest api",
    "rest apis": "rest api",
    "restful api": "rest api",

    # FastAPI
    "fast api": "fastapi",
    "fastapi": "fastapi",

    # =========================
    # SOFT SKILL ALIASES
    # =========================

    "strong communication": "communication",
    "excellent communication": "communication",
    "effective communication": "communication",
    "communication skills": "communication",
    "strong communication skills": "communication",

    "written communication": "written communication",
    "verbal communication": "verbal communication",
    "oral communication": "verbal communication",

    "collaborative": "collaboration",
    "collaboration skills": "collaboration",
    "cross-functional collaboration": "collaboration",

    "team player": "teamwork",
    "team player skills": "teamwork",
    "teamwork skills": "teamwork",

    "problem-solving": "problem solving",
    "problem solving skills": "problem solving",
    "strong problem-solving": "problem solving",
    "strong problem-solving skills": "problem solving",

    "critical thinking skills": "critical thinking",
    "analytical skills": "analytical thinking",
    "analytical thinking skills": "analytical thinking",

    "leadership skills": "leadership",
    "leadership abilities": "leadership",

    "attention-to-detail": "attention to detail",
    "attention to details": "attention to detail",
    "strong attention to detail": "attention to detail",

    "detail-oriented": "detail oriented",
    "detail oriented": "detail oriented",

    "organizational skills": "organization",
    "organizational ability": "organization",

    "time management skills": "time management",

    "presentation skills": "presentation",

    "interpersonal skill": "interpersonal skills",
    "strong interpersonal skills": "interpersonal skills",

    "decision-making": "decision making",
    "decision making skills": "decision making",

    "self-motivated": "self motivated",
    "self motivated": "self motivated",

    "customer-oriented": "customer focus",
    "customer focused": "customer focus",

    "conflict resolution skills": "conflict resolution",

    "negotiation skills": "negotiation",

    "work ethic": "work ethic",

    "initiative and ownership": "ownership",

    # =========================
    # MORE TECHNICAL SKILL ALIASES
    # =========================

    # Python
    "python": "python",
    "python programming": "python",
    "python development": "python",
    "python developer": "python",

    # Java
    "java": "java",
    "java programming": "java",
    "java development": "java",

    # SQL / Databases
    "sql": "sql",
    "sql server": "sql",
    "mssql": "sql",
    "database": "database",
    "databases": "database",
    "dbms": "dbms",

    # MongoDB
    "mongo": "mongodb",
    "mongodb": "mongodb",
    "mongo db": "mongodb",

    # Pandas
    "pandas": "pandas",
    "python pandas": "pandas",

    # NumPy
    "numpy": "numpy",
    "numpy library": "numpy",

    # Scikit-learn
    "sklearn": "scikit-learn",
    "scikit learn": "scikit-learn",
    "scikit-learn": "scikit-learn",

    # Artificial Intelligence
    "ai": "artificial intelligence",
    "artificial intelligence": "artificial intelligence",

    # Deep Learning
    "dl": "deep learning",
    "deep learning": "deep learning",

    # NLP
    "nlp": "nlp",
    "natural language processing": "nlp",

    # Computer Vision
    "cv": "computer vision",
    "computer vision": "computer vision",

    # TensorFlow
    "tensorflow": "tensorflow",
    "tensor flow": "tensorflow",

    # PyTorch
    "pytorch": "pytorch",
    "py torch": "pytorch",

    # Keras
    "keras": "keras",

    # Transformers / LLM
    "transformers": "transformers",
    "transformer": "transformers",
    "llm": "llm",
    "large language model": "llm",
    "large language models": "llm",

    # Generative AI
    "genai": "generative ai",
    "gen ai": "generative ai",
    "generative ai": "generative ai",

    # JavaScript
    "js": "javascript",
    "javascript": "javascript",
    "javascript programming": "javascript",

    # TypeScript
    "ts": "typescript",
    "typescript": "typescript",

    # React
    "react": "react",
    "reactjs": "react",
    "react js": "react",

    # Angular
    "angular": "angular",
    "angularjs": "angular",

    # Vue
    "vue": "vue",
    "vue.js": "vue",

    # Node.js
    "node": "node.js",
    "nodejs": "node.js",
    "node js": "node.js",
    "node.js": "node.js",

    # Backend
    "backend": "backend development",
    "backend development": "backend development",
    "backend engineering": "backend development",

    # APIs
    "api": "api",
    "apis": "api",
    "rest api": "rest api",
    "rest apis": "rest api",
    "restful api": "rest api",
    "restful apis": "rest api",
    "rest services": "rest api",

    # GraphQL
    "graphql": "graphql",
    "graph ql": "graphql",

    # Flask
    "flask": "flask",
    "flask framework": "flask",

    # Django
    "django": "django",
    "django framework": "django",

    # Git / GitHub
    "git": "git",
    "git version control": "git",
    "github": "github",
    "git hub": "github",
    "gitlab": "gitlab",
    "git lab": "gitlab",

    # Docker
    "docker": "docker",
    "docker containers": "docker",
    "container": "containerization",
    "containers": "containerization",
    "containerization": "containerization",

    # Kubernetes
    "kubernetes": "kubernetes",
    "k8s": "kubernetes",
    "kube": "kubernetes",

    # Cloud
    "cloud computing": "cloud computing",
    "cloud platform": "cloud computing",
    "cloud platforms": "cloud computing",
    "cloud infrastructure": "cloud infrastructure",
    "cloud-native": "cloud native",
    "cloud native": "cloud native",

    # AWS
    "aws": "aws",
    "amazon web services": "aws",

    # Azure
    "azure": "azure",
    "microsoft azure": "azure",

    # GCP
    "gcp": "gcp",
    "google cloud": "gcp",
    "google cloud platform": "gcp",

    # DevOps
    "devops": "devops",
    "dev ops": "devops",

    # CI/CD
    "ci/cd": "ci/cd",
    "ci cd": "ci/cd",
    "cicd": "ci/cd",
    "continuous integration": "ci/cd",
    "continuous delivery": "ci/cd",
    "continuous deployment": "ci/cd",

    # Jenkins
    "jenkins": "jenkins",

    # Terraform
    "terraform": "terraform",

    # Linux
    "linux": "linux",
    "unix": "linux",

    # Windows
    "windows": "windows",
    "windows os": "windows",

    # Networking
    "networking": "networking",
    "computer networking": "networking",
    "computer networks": "networking",
    "tcp/ip": "networking",
    "tcp ip": "networking",

    # Automation
    "automation": "automation",
    "workflow automation": "workflow automation",
    "intelligent automation": "intelligent automation",
    "ai automation": "ai automation",
    "ai-powered automation": "ai automation",

    # Software Engineering
    "software engineering": "software engineering",
    "software engineer": "software engineering",
    "software development": "software development",
    "software developer": "software development",

    # Software Design
    "software architecture": "software architecture",
    "system design": "system design",
    "technical design": "technical design",

    # Programming Concepts
    "oop": "object oriented programming",
    "object oriented programming": "object oriented programming",
    "object-oriented programming": "object oriented programming",

    "dsa": "data structures",
    "data structures": "data structures",
    "algorithms": "algorithms",
    "data structures and algorithms": "data structures",

    # Testing
    "unit testing": "unit testing",
    "unit test": "unit testing",
    "automated testing": "automated testing",
    "automation testing": "automated testing",
    "software testing": "software testing",
    "test automation": "test automation",

    # Security
    "secure coding": "secure coding",
    "secure development": "secure development",
    "application security": "application security",
    "cybersecurity": "cybersecurity",

    # SDLC
    "sdlc": "software development lifecycle",
    "software development lifecycle": "software development lifecycle",

    # Agile
    "agile": "agile",
    "agile methodology": "agile",

    # Scrum
    "scrum": "scrum",

    # Tools
    "postman": "postman",
    "jira": "jira",

    # Data Visualization / BI
    "power bi": "power bi",
    "powerbi": "power bi",
    "tableau": "tableau",
    "excel": "excel",

    # CloudSim
    "cloudsim": "cloudsim",
}


def normalize_skill(skill):
    """
    Convert a skill variation into a standard skill name.
    """

    skill = skill.strip().lower()

    return SKILL_ALIASES.get(skill, skill)


def normalize_skills(skills):
    """
    Normalize a complete list of skills
    and remove duplicates.
    """

    normalized = set()

    for skill in skills:

        standard_skill = normalize_skill(skill)

        if standard_skill:
            normalized.add(standard_skill)

    return sorted(normalized)