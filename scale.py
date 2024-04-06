class Scale:
    def __init__(self, note):
        # creates a dictionary with integers that correspond to keyboard notes.
        # Define the notes from C to B including sharps
        # Create the dictionary
        self.note = note
        self.scale = {}
        self.notesList = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        midiPitch = 60
        startingNoteIndex = 0


        if note != 'C':
            # Gets the starting note index so below code knows where to start in the notesList array.
            for j in range(0,  len(self.notesList)):
                if(note == self.notesList[j]):
                    startingNoteIndex = j
            # Concatenate notesList to make note index 0
            self.notesList = self.notesList[startingNoteIndex:] + self.notesList[:startingNoteIndex]

        # make scale dictionary filled with 'Note' and then the proper midiPitch value.
        midiPitch = 60 + startingNoteIndex
        for i in range(0, len(self.notesList)):
            self.scale[self.notesList[i]] = midiPitch
            # gives sharps and flats the same value
            # move to next midiPitch
            midiPitch += 1
        # make Given note the new starting value.

    def key(self, i):
        if(i >= len(self.notesList)):
            print("ERROR INVALID KEY")
        else:
            return self.notesList[i]

    # This function returns a dictionary that is a major scale that can be used for chord creation.
    def major(self):
        # array that stores the values that will be erased in the major scales pattern
        majorArray = [1, 3, 6, 8, 10]
        # copy over scale dictionary to majorDict variable
        majorDict = self.scale

        # make scale dictionary only have major key values
        for i in majorArray:
            del majorDict[self.notesList[i]]

        return majorDict

    # This function returns a dictionary that is a minor scale that can be used for chord creation.
    def minor(self):
        # array that stores the values that will be erased in the major scales pattern
        minorArray = [1, 4, 6, 9, 11]
        minorDict = self.scale

        # make scale dictionary only have major key values
        for i in minorArray:
            del minorDict[self.notesList[i]]

        return minorDict

    def getEntry(self, key):
        if key in self.scale:
            return self.scale[key]
    def updateEntry(self, key, value):
        if key in self.scale:
            self.scale[key] = value
    def setStartinPitch(self, pitch):
        self.midiPitch = pitch

    def display_entries(self):
        print(self.scale)

