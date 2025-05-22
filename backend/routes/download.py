# backend/routes/download.py

from flask import Blueprint, request, send_file
from io import BytesIO
from utils.resume_parser import extract_text_from_pdf
from services.coach import generate_feedback
from services.markdown_exporter import generate_markdown_feedback
from utils.cache import cache

# Register a new Blueprint for this route
download_bp = Blueprint("download", __name__)

@download_bp.route("/api/download-feedback", methods=["POST"])
def download_feedback():
    """
    Serves the previously generated feedback as a Markdown download.
    """

    from utils.cache import cache 

    # Try to use cached feedback
    resume_text = cache.get("resume_text", "")
    job_text = cache.get("job_text", "")
    feedback = cache.get("feedback", "")

    # Make sure somethin exists in cache
    if not resume_text or not feedback:
        return {"error": "No feedback available for download."}, 400
    
    # 📝 Format as Markdown string
    markdown = generate_markdown_feedback(resume_text, feedback)

    # Convert string to in-memory file-like object
    buffer = BytesIO()
    buffer.write(markdown.encode("utf-8"))
    buffer.seek(0)

    # 📤 Return file download to browser
    return send_file(
        buffer,
        as_attachment=True,
        download_name="resume_feedback.md",
        mimetype="text/markdown"
    )

    
