
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
    # user input is received
    text_string = request.values["text_string"]
    key_string = request.values["key_string"]
    mode_string = request.values["mode_string"]
    inst_string = "Cello.sf2"

    # run shell commands
    subprocess.Popen('echo "Running conversion.."', shell=True)

    # run midi create
    # TODO: Add a call to fluidPlay.sh to make a wav file using the midi file that was made
    # TODO: the command to run the bash file is `bash fluidPlay.sh`
    midiProcess = subprocess.run(['python3', 'static/MidiCreate.py', text_string, key_string, mode_string])
    # if return code is 0 then the shell call above ran correctly.
    if midiProcess.returncode == 0:
        # get wav file
        wavProcess = subprocess.run(['bash', 'fluidPlay.sh', inst_string])
        if wavProcess.returncode == 0:
            subprocess.Popen(f"echo 'WAV file created using {inst_string}'",shell=True)
        else:
            subprocess.Popen("echo 'ERROR on WAV'", shell=True)
    else:
        subprocess.Popen("echo 'ERROR on MIDI'", shell=True)

    # converted to json data and returned to website.js
    return json.dumps(text_string)
