from services.ollama_wrapper import query_ollama

def generate_feedback(resume: str, job: str = "") -> str:
    prompt = f"""
You are a resume coach. Analayze the following resume and give detailed feedback.

Resume:
{resume}

Job Description (if provided):
{job}

Provide constructive feedback on:
- Formatting
- Skills alignment
- Use of action verbs
- Technical and soft skill presentation
- Suggestions for improvement
"""
    return query_ollama(prompt)