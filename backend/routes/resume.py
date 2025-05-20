from flask import Blueprint, request, jsonify
from services.coach import generate_feedback
from utils.resume_parser import extract_text_from_pdf

resume_bp = Blueprint("resume", __name__)

@resume_bp.route("/api/feedback", methods=["POST"])
def feedback():
    resume_text = ""
    job_description =""

    # Handle file upload (PDF resume)
    if 'resume' in request.files:
        file = request.files['resume']
        if file.filename.endswith('.pdf'):
            resume_text = extract_text_from_pdf(file)
        else:
            return jsonify({"error": "Only PDF files are supported."}), 400
        
    # Fallback to raw resume text (JSON)
    elif request.is_json:
        data = request.get_json()
        resume_text = data.get("resume", "")
        job_description = data.get("job", "")

    else:
        return jsonify({"error": "Unsupported content type"}), 415
    
    if not resume_text:
        return jsonify({"error": "Resume content is missing"}), 400
        
    feedback = generate_feedback(resume_text, job_description)
    return jsonify({"feedback": feedback})
