# SYNTH-SCIPT
# Tests fluid synth by running a simple MIDI file using the desired sound found. 

# give permission for file to run
chmod +x /Users/thaddeus/Documents/GitHub/synth-script/fluidPlay.sh

# kill all other runnings of fluidsynth 
killall fluidsynth

# set sound
export DESIRED_SOUNDFONT=//Users/thaddeus/Desktop/FluidR3_GM/FluidR3gm.sf2
export MIDI=MainBells.mid

# create .wav file using soundfont and MIDI file. 

fluidsynth -a coreaudio -m coremidi -i -F out.wav "${DESIRED_SOUNDFONT}" "${MIDI}" & 

