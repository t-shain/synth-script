# SYNTH-SCIPT
# Tests fluid synth by running a simple MIDI file using the desired sound found. 

# give permission for file to run
# TODO: This path needs to change if you want to run this file
chmod +x /home/thaddeus/Desktop/synth-script/finalproj/static

# kill all other running's of fluidsynth
killall fluidsynth
# destroy old midi file

#create midi file with string

# set sound
# TODO: these paths need to be changed and the soundFonts folder needs to be added to your PI if its not already
export DESIRED_SOUNDFONT=/Users/thaddeus/Documents/GitHub/synth-script/soundFonts/Piano.sf2
export MIDI=in.mid

# TODO: might need to change path here as well.
rm 'in.wav'

wait

# create .wav file using soundfont and MIDI file.
# TODO: figure out what the coreaudio of the pie is, i think some of these need to be changed for the pi's OS. '
fluidsynth -a coreaudio -m coremidi -i -F in.wav "${DESIRED_SOUNDFONT}" "${MIDI}" &

wait

exit 0


