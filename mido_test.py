# Mido Tester
# Given the String "To be or not to be" the method "string2Midi" converts it into a midi
# file that is in the synth script directory.
from scale import Scale
from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo, second2tick


# TODO: Get Value that randomly generates a BPM between 60-150
# TODO: Make Function that places notes on midi file
# TODO: Within this function make chords using vowels, and single notes using non vowels.
# e = one chord, u = two chord, y = three chord, a = four chord , i = five chord, o = six chord



# Gets the number of vowels in a given string
def countVowel(string):
    # start at 0 vowels
    numVowels = 0
    for i in range(len(string)):
        # if char is a vowel add to vowel counter
        if string[i] in "aeiouAEIOU":
            numVowels += 1
    return numVowels



# VVVVVVV This is a default midi creator that is commented out for now VVVVVVV

# mid = MidiFile()
# track = MidiTrack()
# mid.tracks.append(track)
# track.append(MetaMessage('key_signature', key='Dm'))
# track.append(MetaMessage('set_tempo', tempo=bpm2tempo(120)))
# if (length % 2 == 0):
#     track.append(MetaMessage('time_signature', numerator=4, denominator=4))
# else:
#     track.append(MetaMessage('time_signature', numerator=3, denominator=4))
#
# track.append(Message('note_on', channel=2, note=60, velocity=64, time=1))
# track.append(Message('note_off', channel=2, note=60, velocity=100, time=2))
# track.append(Message('note_off', channel=2, note=60, velocity=100, time=3))
#
# track.append(MetaMessage('end_of_track'))
#
# mid.save('new_song.mid')

# This creates a D major scale

scale = Scale('A')
scale.display_entries()
scale.display_entries()
