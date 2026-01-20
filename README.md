# AI Resume Analyzer

**AI Resume Analyzer** is a Python tool that extracts skills from a PDF resume, compares them with a Job Description (JD), and provides a visual report showing matched and missing skills along with a match percentage. This project demonstrates practical skills in Python, AI, and resume analysis.

---

## Features

- Extract skills from PDF resumes
- Compare resume skills with Job Description
- Show matched skills
- Show missing skills
- Calculate match percentage
- Visualize results with  a pie chart
- Interactive web interface using Gradio

---

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

## echnologies Used

1. Python

2. Gradio (Web Interface)

3. Matplotlib (Visualization)

4. PDF Parsing

5. Basic AI / Keyword Matching

## Author

Avantika Gupta
📧 avantikamahajan001@gmail.com

💻 GitHub
