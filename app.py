from score import calculate_score
from analyzer import detect_skills
from resume_parser import extract_text
from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "resume" not in request.files:
        return "No file selected"

    file = request.files["resume"]

    if file.filename == "":
        return "Please choose a file"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    resume_text = extract_text(filepath)
    detected_skills = detect_skills(resume_text)
    analysis =calculate_score(
        resume_text,
        detected_skills
    )

    return render_template(
        "result.html",
        resume_text=resume_text,
        detected_skills=detected_skills,
        analysis=analysis


    )

if __name__ == "__main__":
    app.run(debug=True)