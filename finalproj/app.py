# like website.js, this technically does not work, so edit as necessary 
# comments are what SHOULD be happening but isn't


from flask import Flask, render_template, request
import json
import subprocess


app = Flask(__name__)


# loads initial webpage, do not change this part
@app.route("/", methods=["GET"])
def home():
    return render_template("website.html")


# string_return is called from website.js
@app.route("/string_return", methods=["GET"])
def string_return():
    # user input is received from text_string (the form)
    text_string = request.values["text_string"]

    # run shell commands
    subprocess.Popen('echo "Running conversion.."', shell=True)

    # run midi create
    # command in terminal looks like: python3 static/MidiCreate.py 'hello' 'C' 'minor'
    midiProcess = subprocess.run(['python3', 'static/MidiCreate.py', text_string, 'C', 'minor'])
    if midiProcess.returncode == 0:
        subprocess.Popen("echo 'MIDI file created!'", shell=True)
    else:
        subprocess.Popen("echo 'ERROR'", shell=True)

    # converted to json data and returned to website.js
    return json.dumps(text_string)
