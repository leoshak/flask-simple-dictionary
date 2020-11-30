import io
from flask import Flask, jsonify, render_template, request, redirect

app = Flask(__name__)
app.debug = True
app.config['EXPLAIN_TEMPLATE_LOADING'] = True

words = []
with io.open("allwords.csv", "r", encoding="utf-8") as file:
    for line in file.readlines():
        words.append(line.rstrip())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def registrants():
    q = request.args.get("q")
    matches = [word for word in words if (word.startswith(q))]
    return render_template('search.html', words=matches)
    # return jsonify(matches)
    
# FLASK_APP=application.py FLASK_ENV=development python -m flask run