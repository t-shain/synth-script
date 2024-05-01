# Synth-Script
A string-to-WAV Project that implements Python, Flask, JavaScript, HTML, and CSS, and the Mido and FluidSynth Python libraries.

## Project Detail:
This program converts user-inputted strings into WAV files that are then
outputted for the user as an audio file. 

### 1. Website 
**Get a string from a website that a user gives.**
A user is able to enter a string into the text box on the website. Our website allows for added
effects depending on what the user enters, such as ! and ... adding a more upbeat
and softer effect to the output, respectively. The string is then converted into JavaScript and displayed back to the user, and then is put through our algorithm. The user is also able to choose the key, instrument, and mode of the desired WAV file.

### 2. Algorithm
**The algorithm in MidiCreate.py is applied to the string.**
The string is put into our custom algorithm. The algorithm uses the vowels, spaces, punctuation, string length, and the user-inputted choices of key, instrument, and mode to determine how to create the MIDI file. 

### 3. Creating the audio file 
**After the algorithm is finished, it exists as a MIDI file.** Because MIDIs are not actual audio files, one more conversion needs to happen, that being the conversion from MIDI to WAV. This happens in fluidPlay.sh.

### 4. Output 
**The WAV file conversion is complete.** Finally, the fully converted WAV is returned to the user as a fully playable website element. The user might have to refresh the page for the audio file to appear.

**Note: The output process may work slightly different depending on the browser. Our code is optimized for Safari, and has worked decently enough on Chrome. Other browsers were not tested.**


## References

Ardour Digital Audio Workstation. (n.d). Creating Music with Ardour. https://manual.ardour.org/introduction-to-ardour/welcome-to-ardour/ 

Avid. (2023, November 22). What is a DAW? Your Guide to Digital Audio Workstations. https://www.avid.com/resource-center/what-is-a-daw 

Derselbst. (2003, March 9).  FluidSynth. https://github.com/FluidSynth/fluidsynth.

Floyd Steinburg. (2019, December 10). How to use a Raspberry PI as a synthesizer [Video]. YouTube. https://youtu.be/ae5TYhnhp3w?si=UZyRmO26huN4v60r

Fluidsynth. (n.d.). A SoundFont Synthesizer. https://www.fluidsynth.org/

MDN Web Docs. (2023, December 5). Web MIDI API. https://developer.mozilla.org/en-US/docs/Web/API/Web_MIDI_API 

Michael Hahn.  (2023, July 25). What Is MIDI? How To Use the Most Powerful Tool in Music. LANDR Blog. https://blog.landr.com/what-is-midi/

Ole Martin Bjørndalen Raphaël Doursenaud. (n.d). Mido - MIDI Objects For Python. https://mido.readthedocs.io/en/latest/intro.html 

Python Software Foundation. (n.d.). Python 3.12.2 documentation. https://docs.python.org/3/ 








