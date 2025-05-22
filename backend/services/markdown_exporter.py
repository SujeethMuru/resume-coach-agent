def generate_markdown_feedback(resume_text: str, feedback_text: str) -> str:
    """
    Combines resume content and AI feedback into a clean Markdown format.

    Args:
        resume_text (str): The raw resume text (from PDF or user input)
        feedback_text (str): The generated AI feedback

    Returns:
        str: A markdown-formatted string
    """
    return f"""# 🧠 Resume Coach Feedback

## 📄 Submitted Resume

```
{resume_text.strip()}
```

---

## ✅ AI Feedback

{feedback_text.strip()}
"""
