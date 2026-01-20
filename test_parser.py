from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from jd_matcher import calculate_match

# Full path of your resume
resume_path = r"C:\Users\HP\OneDrive\Desktop\Resume_1.pdf"

# Extract resume text
resume_text = extract_resume_text(resume_path)

# Extract skills from resume
resume_skills = extract_skills(resume_text)

# Job description text
job_description = """
We are hiring an AI Developer.
Required skills: Python, AI, Machine Learning, Deep Learning, Data Science,
Pandas, NumPy, SQL, Excel, HTML, CSS, Power BI, TensorFlow, PyTorch, NLP.
"""

# Match resume skills with JD
matched, missing = calculate_match(resume_skills, job_description)

# Print results
print("\nSKILLS FOUND IN RESUME:")
print(resume_skills)

print("\nMATCHED SKILLS:")
print(matched)

print("\nMISSING SKILLS:")
print(missing)

# Calculate match percentage
if len(resume_skills) > 0:
    match_percentage = (len(matched) / len(resume_skills)) * 100
else:
    match_percentage = 0

print(f"\nMATCH PERCENTAGE: {match_percentage:.2f}%")

