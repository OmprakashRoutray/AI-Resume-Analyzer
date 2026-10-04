def calculate_score(text, detected_skills):
    
    score = 0
    suggestions = []

    text_lower = text.lower()

    # -------------------------
    # 1. Skills - 40 points
    # -------------------------

    skill_count = len(detected_skills)

    if skill_count >= 10:
        skill_score = 40

    elif skill_count >= 7:
        skill_score = 35

    elif skill_count >= 5:
        skill_score = 30

    elif skill_count >= 3:
        skill_score = 20

    elif skill_count >= 1:
        skill_score = 10

    else:
        skill_score = 0

    score += skill_score


    # -------------------------
    # 2. Education - 20 points
    # -------------------------

    education_keywords = [
        "education",
        "b.tech",
        "btech",
        "bachelor",
        "degree",
        "college",
        "university",
        "cgpa",
        "gpa"
    ]

    education_found = any(
        keyword in text_lower
        for keyword in education_keywords
    )

    if education_found:
        education_score = 20
    else:
        education_score = 0
        suggestions.append(
            "Add a clear Education section."
        )

    score += education_score


    # -------------------------
    # 3. Projects - 20 points
    # -------------------------

    project_keywords = [
        "project",
        "projects",
        "developed",
        "built",
        "created",
        "implemented"
    ]

    project_found = any(
        keyword in text_lower
        for keyword in project_keywords
    )

    if project_found:
        project_score = 20
    else:
        project_score = 0
        suggestions.append(
            "Add projects to demonstrate your practical skills."
        )

    score += project_score


    # -------------------------
    # 4. Contact Information - 10 points
    # -------------------------

    contact_score = 0

    if "@" in text:
        contact_score += 5
    else:
        suggestions.append(
            "Add a professional email address."
        )

    if any(char.isdigit() for char in text):
        contact_score += 5
    else:
        suggestions.append(
            "Add a phone number."
        )

    score += contact_score


    # -------------------------
    # 5. Resume Sections - 10 points
    # -------------------------

    section_keywords = [
        "skills",
        "education",
        "experience",
        "projects",
        "certifications"
    ]

    sections_found = 0

    for section in section_keywords:

        if section in text_lower:
            sections_found += 1

    section_score = min(
        sections_found * 2,
        10
    )

    score += section_score


    # -------------------------
    # Final Suggestions
    # -------------------------

    if skill_count < 5:
        suggestions.append(
            "Add more relevant technical skills."
        )

    if "experience" not in text_lower:
        suggestions.append(
            "Consider adding internship or work experience."
        )

    if "certification" not in text_lower:
        suggestions.append(
            "Add relevant certifications if available."
        )


    return {
        "score": score,
        "skill_score": skill_score,
        "education_score": education_score,
        "project_score": project_score,
        "contact_score": contact_score,
        "section_score": section_score,
        "suggestions": suggestions
    }