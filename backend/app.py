from flask import Flask
from routes.resume import resume_bp

app = Flask(__name__)
app.register_blueprint(resume_bp)

@app.route("/")
def home():
    return "Resume Coach Agent is running!"

if __name__ == "__main__":
    app.run(debug=True)