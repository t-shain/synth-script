#!/bin/bash
# SYNTH-SCIPT
# Tests fluid synth by running a simple MIDI file using the desired sound found.

# give permission for file to run
# TODO: This path needs to change if you want to run this file
chmod +x fluiPlay.sh

# kill all other running's of fluidsynth
killall fluidsynth
#create midi file with string

# set sound
# TODO: these paths need to be changed and the soundFonts folder needs to be added to your PI if its not already
export DESIRED_SOUNDFONT="/home/thaddeus/Desktop/synth-script/finalproj/soundFonts/$1"
export MIDI=in.mid

rm 'static/in.wav'

wait

# create .wav file using soundfont and MIDI file.
fluidsynth -a alsa -m coremidi -i -F in.wav "${DESIRED_SOUNDFONT}" "${MIDI}" &

wait

# move to static directory so html can play it
mv 'in.wav' static

exit 0

