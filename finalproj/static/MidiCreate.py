# Mido Tester
# Given the String "To be or not to be" the method "string2Midi" converts it into a midi
# file that is in the synth script directory.
import sys

from scale import Scale
from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo
import random


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
def writeOutMIDI(mode, letter, t, strng, ):
    # creates dictionary
    scale = Scale(letter)
    # makes scale major or minor values depending on param mode
    if mode == 'minor':
        mde = scale.minor()
    else:
        mde = scale.major()
    # created an array with the values of the keys in scale.
    keys = list(mde.keys())
    # goes through each character in string and does something.

    for i in range(0, len(strng)):
        velocity = random.randint(55, 68)
        if strng[len(strng) - 1] == '!':
            velocity = 100

        if strng[i] not in 'aeiouAEIOU':
            if strng[i] == '.':
                # do something fun!
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[0]), velocity=velocity, time=1))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[0]), velocity=velocity, time=960))

            # for all other letters or numbers print a random value
            if strng[i] != len(strng) - 1:
                random.seed(strng[i])
                r = random.randint(0, len(keys) - 1)
                if r % 2 == 0:
                    timeRest = 240
                else:
                    timeRest = 480
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[r]), velocity=velocity, time=1))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[r]), velocity=velocity, time=timeRest))
        else:
            lowerCase = strng[i].lower()
            if lowerCase == 'e':
                # put one cord on midi track
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[0]), velocity=velocity, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[2]), velocity=velocity, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[4]), velocity=velocity, time=1))
                # 480 time = quarter note, #960 = half note
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[0]), velocity=velocity, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[2]), velocity=velocity, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[4]), velocity=velocity, time=960))
            elif lowerCase == 'u':
                # put two cord on midi track
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[1]), velocity=velocity, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[3]), velocity=velocity, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[5]), velocity=velocity, time=1))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[1]), velocity=velocity, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[3]), velocity=velocity, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[5]), velocity=velocity, time=960))
            elif lowerCase == 'a':
                # put four cord on midi track
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[3]), velocity=velocity, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[5]), velocity=velocity, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[0]), velocity=velocity, time=1))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[3]), velocity=velocity, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[5]), velocity=velocity, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[0]), velocity=velocity, time=960))
            elif lowerCase == 'i':
                # put five cord on midi track
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[4]), velocity=velocity, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[6]), velocity=velocity, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[1]), velocity=velocity, time=1))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[4]), velocity=velocity, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[6]), velocity=velocity, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[1]), velocity=velocity, time=960))
            elif lowerCase == 'o':
                # put six cord on midi track
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[5]), velocity=velocity, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[0]), velocity=velocity, time=1))
                t.append(Message('note_on', channel=1, note=scale.getEntry(keys[2]), velocity=velocity, time=1))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[5]), velocity=velocity, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[0]), velocity=velocity, time=960))
                t.append(Message('note_off', channel=1, note=scale.getEntry(keys[2]), velocity=velocity, time=960))
    t.append(MetaMessage('end_of_track'))
    print(f"{strng} has been written to MIDI")


# create midi file and assign string to sys argument
def run(s, k, m):
    mid = MidiFile()
    track = MidiTrack()
    string = s

    key = k
    mode = m

    if m not in ['major', 'minor', ]:
        mode = 'major'
    elif k not in ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']:
        key = 'C'



    # create midi track
    # create random bpm using seed
    random.seed(len(string))
    randomBPM = random.randint(60, 130)

    # create midi track
    mid.tracks.append(track)
    track.append(MetaMessage('key_signature', key=key))
    track.append(MetaMessage('set_tempo', tempo=bpm2tempo(randomBPM)))

    if len(string) % 2 != 0:
        tempo = '3/4'
        track.append(MetaMessage('time_signature', numerator=3, denominator=4))
    else:
        temp = '4/4'
        track.append(MetaMessage('time_signature', numerator=4, denominator=4))

    # run algo with a 4/4 time signature
    writeOutMIDI(mode, key, track, string)

    mid.save('in.mid')


run(sys.argv[1],sys.argv[2],sys.argv[3])