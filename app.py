from flask import Flask, render_template, request
from model import summarize_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        input_text = request.form["input_text"]
        summary = summarize_text(input_text)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
