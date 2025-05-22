from flask import Flask
from routes.resume import resume_bp
from routes.frontend import frontend_bp
from routes.download import download_bp
from flask import redirect

app = Flask(__name__)
app.register_blueprint(resume_bp)
app.register_blueprint(frontend_bp)
app.register_blueprint(download_bp)

@app.route("/")
def home():
    return redirect("/ui")

if __name__ == "__main__":
    app.run(debug=True)