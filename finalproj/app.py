from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("website.html")

@app.route("/string_return", methods=["GET"])
def string_return():
    text_string = request.values["text_string"]
    return json.dumps(text_string)
