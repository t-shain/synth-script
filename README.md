# Synth-Script
A word to MIDI to audio Project

## Project Detail:
Write python files that convert words to midi sound data, output sound.
The broad strokes steps in this project are as follows:

### 1. Website 
**Get a string from a website that a user gives.**
The synth script website should have a box to input a string at the very least. 
This website will be able to get this given string (have some minor user input) then uses pythons

### 2. Algorithm
string is put into a custom algorithm that turns it into a midi file. 
The algorithm uses the vowels, spaces, punctuation, and string length to determine how to create the midi
file. 

Some things to note. 
- Midi files use integers to represent notes on a piano scale. the value `60` is the middle C of the keyboard
  (C3).
- The plan is to use a the starting vowel to creat a scale of notes major or minor that can be played. 

### 3. Audio file 
midi file is turned into an audio file

### 4. Output 
audio file is played by the website locally.


## Target market:
Music writers, producers, DJs, anybody in music industry




