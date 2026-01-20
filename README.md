# AI Resume Analyzer

An AI-powered Python tool that analyzes resumes against job descriptions using a local Large Language Model (LLM) via Ollama. Automatically identifies matched and missing skills, calculates a match percentage, and generates a structured visual report.
Demonstrates hands-on experience in Python, AI, and resume analysis with structured JSON outputs.

## Features

- Extract skills from PDF resumes
- Compare resume skills with Job Description
- Show matched skills
- Show missing skills
- Calculate match percentage
- Visualize results with  a pie chart
- Interactive web interface using Gradio

## Problem Statement
Manual resume screening is slow, inconsistent, and error-prone. This tool automates resume evaluation, helping recruiters quickly identify candidate–job fit and skill gaps.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/codewithavantika/ai-resume-analyzer.git
cd ai-resume-analyzer

2. Create a virtual environment (optional but recommended):

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

3. Install dependencies:

pip install -r requirements.txt

## Usage

1. Run the Gradio app:

python app.py

2. Open the Gradio link in your browser (it will appear in terminal)

3. Upload your resume (PDF)

4. Paste the Job Description in the textbox

5. Click Submit

You will see:

1. Resume Skills
2. Matched Skills
3. Missing Skills
4. Match Percentage
5. Pie chart visualization

## Example Job Description (JD)
We are hiring an AI Developer.
Required skills: Python, AI, Machine Learning, Deep Learning, Data Science,
Pandas, NumPy, SQL, Excel, HTML, CSS, Power BI, TensorFlow, PyTorch, NLP.

## Project Structure

ai-resume-analyzer/
│
├── resume_parser.py
├── skill_extractor.py
├── jd_matcher.py
├── test_parser.py
├── app.py
├── README.md
├── requirements.txt
└── Resume_1.pdf

## Technologies used

1. Python

2. Gradio (Web Interface)

3. Matplotlib (Visualization)

4. PDF Parsing

5. Basic AI / Keyword Matching

## Future Improvements

1. Add advanced AI-based scoring for soft skills

2. Streamlit integration for enhanced interface

3. Cloud deployment for scalable resume analysis

## Author
Avantika Gupta 
📧 Email: avantikamahajan001@gmail.com  
💻 GitHub: https://github.com/codewithavantika  

