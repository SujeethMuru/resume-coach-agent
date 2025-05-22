from flask import Blueprint, render_template, request
from utils.resume_parser import extract_text_from_pdf
from services.coach import generate_feedback
from utils.cache import cache

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route("/ui", methods=["GET", "POST"])
def ui():
    feedback = None
    resume_text = ""
    job_text = ""

    if request.method == "POST":
        job_text = request.form.get("job", "")

        if 'resume' in request.files:
            file = request.files['resume']
            resume_text = extract_text_from_pdf(file)

        if resume_text:
            feedback = generate_feedback(resume_text, job_text)
            cache["resume_text"] = resume_text
            cache["job_text"] = job_text
            cache["feedback"] = feedback

    return render_template("index.html", feedback=feedback, resume_text=resume_text, job_text=job_text)