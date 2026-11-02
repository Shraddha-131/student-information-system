from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = []

@app.route("/")
def home():
    search = request.args.get("search", "").strip().lower()

    if search:
        filtered_students = [
            student for student in students
            if search in student["name"].lower()
            or search in student["roll"].lower()
        ]
    else:
        filtered_students = students

    return render_template("index.html", students=filtered_students, search=search)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form.get("name", "").strip()
    roll = request.form.get("roll", "").strip()
    course = request.form.get("course", "").strip()

    if name and roll and course:
        students.append({
            "name": name,
            "roll": roll,
            "course": course
        })

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)