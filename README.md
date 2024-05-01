# Synth-Script
A string-to-WAV Project that implements Python, Flask, JavaScript, HTML, and CSS.

## Project Detail:
This program converts user-inputted strings into WAV files that are then
outputted for the user as an audio file. 

### 1. Website 
**Get a string from a website that a user gives.**
A user is able to enter a string into the text box on the website. Our website allows for added
effects depending on what the user enters, such as ! and ... adding a more upbeat
and softer effect to the output, respectively.

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


#### Cool strings I found so far
- `Father and Mother` sounds like parenthood. 
- `I will show you fear in a handful of dust`

