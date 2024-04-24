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
    key_string = request.values["key_string"]
    mode_string = request.values["mode_string"]

    # run shell commands
    subprocess.Popen('echo "Running conversion.."', shell=True)

    # run midi create
    # command in terminal looks like: python3 static/MidiCreate.py 'hello' 'C' 'minor'
    # TODO: Add a call to fluidPlay.sh to make a wav file using the midi file that was made
    midiProcess = subprocess.run(['python3', 'static/MidiCreate.py', text_string, 'C', 'minor'])
    # if return code is 0 then the shell call above ran correctly.
    if midiProcess.returncode == 0:
        subprocess.Popen("echo 'MIDI file created!'", shell=True)
        subprocess.run(['echo', f'{key_string} {mode_string}'], shell=True)
    else:
        subprocess.Popen("echo 'ERROR'", shell=True)

    # converted to json data and returned to website.js
    return json.dumps(text_string)
