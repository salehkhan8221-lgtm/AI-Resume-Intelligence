# 📄 AI Resume Intelligence

### Smart Resume & Job Matching Platform

AI Resume Intelligence is an end-to-end Streamlit application that analyzes resumes against job descriptions using skill extraction, skill normalization, intelligent matching, skill-gap analysis, experience requirement detection, and ATS-oriented evaluation.

The platform helps users understand how closely their resume aligns with a target job description and identifies skills and requirements that may need improvement.

---

## 🚀 Live Demo

🔗 **Live Application:**  
https://ai-resume-intelligence-n3ozrf5mhwtg2fe7shd7jt.streamlit.app/

🔗 **GitHub Repository:**  
https://github.com/salehkhan8221-lgtm/AI-Resume-Intelligence

---

## 🎯 Project Objective

Recruiters and candidates often need to compare resumes with job descriptions to determine whether the candidate's skills and experience align with the role.

AI Resume Intelligence automates several parts of this process by:

- Extracting text from resumes
- Identifying technical skills
- Identifying soft and professional skills
- Analyzing job descriptions
- Normalizing different skill names and variations
- Comparing resume skills with job requirements
- Identifying matched and missing skills
- Categorizing skill gaps by priority
- Detecting mandatory and preferred requirements
- Detecting experience requirements
- Performing ATS-oriented resume analysis
- Providing an interactive analysis dashboard

---

## ✨ Key Features

### 📄 1. Resume Analysis

Users can upload resumes in:

- PDF
- DOCX

The application extracts resume content and identifies relevant skills.

#### Output includes:

- Extracted resume text
- Technical skills
- Soft skills
- Professional skills
- Normalized skills

---

### 💼 2. Job Description Analysis

Users can paste a complete job description and analyze its requirements.

The system identifies:

- Technical skills
- Soft skills
- Professional skills
- Mandatory requirements
- Preferred requirements
- Experience requirements

---

### 🔍 3. Intelligent Skill Matching

The matching engine compares skills detected in the resume with skills required by the job description.

The system identifies:

- Matched skills
- Missing skills
- Overall skill compatibility

The matching process uses skill normalization to handle common variations.

Examples:

```text
JS                  → JavaScript
NodeJS              → Node.js
CPP                 → C++
Postgres            → PostgreSQL
ML                  → Machine Learning
REST APIs           → REST API
Fast API            → FastAPI

---

🔄 Application Workflow

Upload Resume
      ↓
Extract Resume Text
      ↓
Extract Resume Skills
      ↓
Normalize Skills
      ↓
Paste Job Description
      ↓
Analyze Job Description
      ↓
Extract Required Skills
      ↓
Detect Experience Requirement
      ↓
Identify Mandatory & Preferred Requirements
      ↓
Compare Resume vs Job Description
      ↓
Identify Matched & Missing Skills
      ↓
Perform Skill Gap Analysis
      ↓
Perform ATS Analysis
      ↓
Display Results

---

🧩 Project Structure

AI Resume Intelligence/
│
├── app/
│   ├── __init__.py
│   │
│   ├── parser/
│   │   ├── __init__.py
│   │   └── resume_parser.py
│   │
│   ├── nlp/
│   │   ├── __init__.py
│   │   ├── ats_analyzer.py
│   │   ├── jd_analyzer.py
│   │   ├── matching_engine.py
│   │   ├── skill_extractor.py
│   │   ├── skill_gap_analyzer.py
│   │   └── skill_normalizer.py
│   │
│   └── frontend/
│       ├── main.py
│       ├── styles.py
│       │
│       └── pages/
│           ├── 1_Resume_Analysis.py
│           ├── 2_Job_Description.py
│           ├── 3_Match_Dashboard.py
│           └── 4_ATS_Analysis.py
│
├── data/
│
├── tests/
│
├── .gitignore
├── requirements.txt
└── README.md

---
🛠️ Tech Stack

Technology:                                           Purpose:
Python	                  |                           Core programming language
Streamlit	              |                           Web application and interactive dashboard
Pandas	                  |                           Data processing
NumPy	                  |                           Numerical operations
Scikit-learn	          |                           Machine learning utilities
PDFPlumber	              |                           PDF text extraction
python-docx               |                           DOCX text extraction
Regex	                  |                           Pattern-based text and skill extraction
Git	                      |                           Version control
GitHub	                  |                           Source code hosting
Streamlit Community Cloud | 	                      Cloud deployment

---

🧠 Core Technical Concepts

This project demonstrates practical implementation of:

Text preprocessing
Regular expressions
Rule-based NLP
Skill extraction
Skill normalization
Set-based skill matching
Requirement classification
Experience pattern detection
Keyword coverage analysis
ATS-oriented scoring
Streamlit session state
Modular Python architecture
Git and GitHub workflow
Cloud deployment

----

📊 Matching Logic

The application normalizes skills from both the resume and job description before performing the comparison.

Resume Skills              Job Skills
      │                         │
      ▼                         ▼
Normalize                   Normalize
      │                         │
      └───────────┬─────────────┘
                  ▼
            Set Comparison
                  │
          ┌───────┴───────┐
          ▼               ▼
    Matched Skills    Missing Skills
          │               │
          └───────┬───────┘
                  ▼
          Compatibility Score


---

⚙️ Installation

1. Clone the Repository
git clone https://github.com/salehkhan8221-lgtm/AI-Resume-Intelligence.git

2. Navigate to the Project
cd AI-Resume-Intelligence

3. Create a Virtual Environment
Windows
python -m venv .venv

Activate it:

.venv\Scripts\activate
Linux / macOS
python3 -m venv .venv

Activate it:

source .venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt

▶️ Running the Application

Run the following command from the project root:

python -m streamlit run app/frontend/main.py

The application will open in your default browser.

🌐 Deployment

The application is deployed using Streamlit Community Cloud.

Live Application

https://ai-resume-intelligence-n3ozrf5mhwtg2fe7shd7jt.streamlit.app/

Entry Point
app/frontend/main.py