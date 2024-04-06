# Mido Tester
# Given the String "To be or not to be" the method "string2Midi" converts it into a midi
# file that is in the synth script directory.
from scale import Scale
from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo, second2tick
import random

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


# Algorithm to write out to MIDI file.
# params: timeSignature is a string that will run a curtain section of code based off if time signature is
# 3/4 or 4/4, letter is the starting note that the major scale will be created from. t is the track object from Mido,
# and str is the string that will be used to generate the pattern.
def writeOutMIDI(timeSignature, letter, t, strng):
    # creates dictionary
    scale = Scale(letter)
    # makes scale only have major key values.
    majorScale = scale.major()
    # created an array with the values of the keys in scale.
    majorKeys = list(majorScale.keys())
    # goes through each character in string and does something.
    for i in range(0, len(strng)):
        if strng[i] in 'aeiouAEIOU':
            lowerCase = strng[i].lower()
            if lowerCase == 'e':
                # put one cord on midi track
                print('e')
                t.append(Message('note_on', channel=1, note=scale.getEntry(majorKeys[0]), velocity=64, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(majorKeys[2]), velocity=64, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(majorKeys[4]), velocity=64, time=1))
                # 480 time = quarter note, #960 = half note
                t.append(Message('note_off', channel=1, note=scale.getEntry(majorKeys[0]), velocity=64, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(majorKeys[2]), velocity=64, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(majorKeys[4]), velocity=64, time=960))
            elif lowerCase == 'u':
                # put two cord on midi track
                print('u')
                t.append(Message('note_on', channel=1, note=scale.getEntry(majorKeys[1]), velocity=64, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(majorKeys[3]), velocity=64, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(majorKeys[5]), velocity=64, time=1))
                t.append(Message('note_off', channel=1, note=scale.getEntry(majorKeys[1]), velocity=64, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(majorKeys[3]), velocity=64, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(majorKeys[5]), velocity=64, time=960))
            elif lowerCase == 'a':
                # put four cord on midi track
                print('a')
                t.append(Message('note_on', channel=1, note=scale.getEntry(majorKeys[3]), velocity=64, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(majorKeys[5]), velocity=64, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(majorKeys[0]), velocity=64, time=1))
                t.append(Message('note_off', channel=1, note=scale.getEntry(majorKeys[3]), velocity=64, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(majorKeys[5]), velocity=64, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(majorKeys[0]), velocity=64, time=960))
            elif lowerCase == 'i':
                # put five cord on midi track
                print('i')
                t.append(Message('note_on', channel=1, note=scale.getEntry(majorKeys[4]), velocity=64, time=1))
                t.append(Message('note_off', channel=1, note=scale.getEntry(majorKeys[4]), velocity=64, time=960))
            elif lowerCase == 'o':
                # put six cord on midi track
                print('o')
                t.append(Message('note_on', channel=1, note=scale.getEntry(majorKeys[5]), velocity=64, time=1))
                t.append(Message('note_off', channel=1, note=scale.getEntry(majorKeys[5]), velocity=64, time=960))
        else:
            if strng[i] == ' ':
                # no notes played
                print("//")
            if string[i] == '.':
                # do something fun!
                print(".")

            # for all other letters or numbers print a random value
            if strng[i] != len(strng) - 1:
                random.seed(strng[i])
                r = random.randint(0, len(majorKeys) - 1)
                if r % 2 == 0:
                    timeRest = 240
                else:
                    timeRest = 480
                t.append(Message('note_on', channel=1, note=scale.getEntry(majorKeys[r]), velocity=64, time=1))
                t.append(Message('note_off', channel=1, note=scale.getEntry(majorKeys[r]), velocity=64, time=timeRest))

    t.append(MetaMessage('end_of_track'))


# default midi file creator
mid = MidiFile()
track = MidiTrack()
string = "Father and Mother"

# creates a dictionary called scale with A major notes.

# create midi track
#create random bpm
randomBPM = random.randint(60, 165)
mid.tracks.append(track)
track.append(MetaMessage('key_signature', key='D'))
track.append(MetaMessage('set_tempo', tempo=bpm2tempo(randomBPM)))

# run algo with a 4/4 time signature
track.append(MetaMessage('time_signature', numerator=4, denominator=4))
writeOutMIDI("4/4", 'D', track, string)

mid.save('test.mid')
