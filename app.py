from flask import Flask, request, render_template
from utils import extract_text, match_score, extract_skills

app = Flask(__name__)   # ✅ MUST BE HERE (before route)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["resume"]
        job_desc = request.form["job_desc"]

        resume_text = extract_text(file)

        score = match_score(resume_text, job_desc)

        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_desc)

        missing = list(set(job_skills) - set(resume_skills))

        return render_template("index.html",
                               score=score,
                               skills=resume_skills,
                               missing=missing)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)