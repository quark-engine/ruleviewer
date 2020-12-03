import json

from flask import Flask
from flask import request
from flask import render_template


DEVELOPMENT_ENV  = True

app = Flask(__name__)

app_data = {
    "name":         "Peter's Starter Template for a Flask Web App",
    "description":  "A basic Flask app using bootstrap for layout",
    "author":       "Peter Simeth",
    "html_title":   "Peter's Starter Template for a Flask Web App",
    "project_name": "Starter Template",
    "keywords":     "flask, webapp, template, basic"
}


@app.route('/')
def index():
    return render_template('index.html', data={})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=DEVELOPMENT_ENV)