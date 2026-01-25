import re

SKILLS = [
    "python", "django", "fastapi", "sql", "aws",
    "docker", "machine learning", "nlp", "react"
]


def parse_resume(text):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "experience": extract_experience(text),
        "resume_text": text
    }


# -----------------------------
# Extractors
# -----------------------------

def extract_email(text):
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group(0) if match else None


def extract_phone(text):
    match = re.search(r"(\+?\d{1,3}[\s-]?)?\d{10}", text)
    return match.group(0) if match else None


def extract_name(text):
    """
    Very simple heuristic:
    Take first non-empty line with alphabet-only words
    """
    for line in text.splitlines():
        line = line.strip()
        if len(line.split()) <= 4 and line.replace(" ", "").isalpha():
            return line
    return None


def extract_skills(text):
    found = []
    lower_text = text.lower()
    for skill in SKILLS:
        if skill in lower_text:
            found.append(skill)
    return ", ".join(found)


def extract_experience(text):
    """
    Looks for patterns like:
    - 3 years
    - 5+ years
    - 2.5 years
    """
    match = re.search(r"(\d+(\.\d+)?)\+?\s+years?", text.lower())
    return float(match.group(1)) if match else None
