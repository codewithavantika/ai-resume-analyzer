def extract_skills(text):
    skills_list = [
        "python", "ai", "machine learning", "deep learning",
        "data science", "pandas", "numpy", "sql", "excel",
        "html", "css", "javascript", "power bi", "tensorflow",
        "pytorch", "nlp", "opencv", "scikit-learn"
    ]

    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills

