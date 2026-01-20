def calculate_match(resume_skills, jd_text):
    jd_text = jd_text.lower()

    matched = []
    missing = []

    # Match exact skills
    for skill in resume_skills:
        if skill in jd_text:
            matched.append(skill)

    # Find missing skills (check all skills in JD text)
    possible_skills = [
        "python", "ai", "machine learning", "deep learning",
        "data science", "pandas", "numpy", "sql", "excel",
        "html", "css", "javascript", "power bi", "tensorflow",
        "pytorch", "nlp", "opencv", "scikit-learn"
    ]

    for skill in possible_skills:
        if skill in jd_text and skill not in resume_skills:
            missing.append(skill)

    return matched, missing

