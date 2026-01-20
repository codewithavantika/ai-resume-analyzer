# app.py
import matplotlib
matplotlib.use('Agg')  # ensure charts render correctly in Gradio
import matplotlib.pyplot as plt
import gradio as gr
from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from jd_matcher import calculate_match

# Function to create pie chart
def create_pie_chart(matched, missing):
    labels = ['Matched Skills', 'Missing Skills']
    sizes = [len(matched), len(missing)]
    colors = ['#4CAF50', '#F44336']  # green and red

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.0f%%', colors=colors, startangle=90)
    ax.axis('equal')
    plt.title('Resume Skill Match')
    plt.close(fig)  # Important to prevent display issues
    return fig

# Main function to analyze resume
def analyze_resume(resume_file, job_description):
    resume_text = extract_resume_text(resume_file.name)
    resume_skills = extract_skills(resume_text)
    matched, missing = calculate_match(resume_skills, job_description)

    # Calculate match percentage
    if len(resume_skills) > 0:
        match_percentage = (len(matched) / len(resume_skills)) * 100
    else:
        match_percentage = 0

    # Create pie chart
    fig = create_pie_chart(matched, missing)

    return {
        "Resume Skills": resume_skills,
        "Matched Skills": matched,
        "Missing Skills": missing,
        "Match Percentage": f"{match_percentage:.2f}%"
    }, fig

# Gradio interface
iface = gr.Interface(
    fn=analyze_resume,
    inputs=[
        gr.File(label="Upload Resume (PDF)"),
        gr.Textbox(label="Paste Job Description")
    ],
    outputs=[
        gr.JSON(label="Result"),
        gr.Plot(label="Match Chart")
    ],
    title="AI Resume Analyzer",
    description="Upload your resume (PDF) and paste the Job Description to see your matched and missing skills along with match percentage."
)

iface.launch()
