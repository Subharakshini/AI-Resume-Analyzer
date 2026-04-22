from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def match_score(resume, job_desc):
    text = [resume, job_desc]
    cv = CountVectorizer()
    matrix = cv.fit_transform(text)
    score = cosine_similarity(matrix)[0][1]
    return round(score * 100, 2)

# 👇 PASTE HERE (outside functions)
skills_list = [
    "python", "c++", "sql", "machine learning",
    "data structures", "dbms", "html", "css", "git",
    "java", "react", "aws", "docker", "kubernetes", "mongodb"
]

def extract_skills(text):
    found = []
    for skill in skills_list:
        if skill in text.lower():
            found.append(skill)
    return found