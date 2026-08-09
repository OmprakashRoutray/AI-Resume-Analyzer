import re


SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "Flask",
    "Django",
    "MySQL",
    "MongoDB",
    "SQL",
    "Git",
    "GitHub",
    "Docker",
    "AWS",
    "Machine Learning",
    "Artificial Intelligence",
    "Data Science",
    "Pandas",
    "NumPy",
    "TensorFlow",
    "PyTorch"
]


def detect_skills(text):

    detected_skills = []

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):

            detected_skills.append(skill)

    return detected_skills