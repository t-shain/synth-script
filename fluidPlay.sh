# SYNTH-SCIPT
# Tests fluid synth by running a simple MIDI file using the desired sound found. 

# give permission for file to run
chmod +x /Users/thaddeus/Documents/GitHub/synth-script/fluidPlay.sh

# kill all other running's of fluidsynth
killall fluidsynth

#create midi file with string
python3 MidiCreate.py 'to be or not to be' 'A' 'minor'

# set sound
export DESIRED_SOUNDFONT=/Users/thaddeus/Documents/GitHub/synth-script/soundFonts/FluidR3gm.sf2
export MIDI=test.mid

# create .wav file using soundfont and MIDI file. 

fluidsynth -a coreaudio -m coremidi -i -F out.wav "${DESIRED_SOUNDFONT}" "${MIDI}" &

