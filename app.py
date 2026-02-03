from flask import Flask, render_template, request
from predictor import analyze_company

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        company = request.form.get("company")
        try:
            result = analyze_company(company)
        except Exception as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
