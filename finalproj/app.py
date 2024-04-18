from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/led_on", methods=["POST"])
def led_on_r():
    print("LED on")
    return "ok"

@app.route("/led_off", methods=["POST"])
def led_off_r():
    print("LED off")
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return render_template("website.html")
