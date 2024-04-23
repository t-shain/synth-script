# SYNTH-SCIPT
# Tests fluid synth by running a simple MIDI file using the desired sound found. 

# give permission for file to run
chmod +x /home/thaddeus/Desktop/synth-script/finalproj/static

# kill all other running's of fluidsynth
killall fluidsynth
# destroy old midi file

#create midi file with string

# set sound
export DESIRED_SOUNDFONT=/Users/thaddeus/Documents/GitHub/synth-script/soundFonts/Piano.sf2
export MIDI=in.mid

rm 'in.wav'

wait

# create .wav file using soundfont and MIDI file.
fluidsynth -a coreaudio -m coremidi -i -F in.wav "${DESIRED_SOUNDFONT}" "${MIDI}" &

wait

exit 0


