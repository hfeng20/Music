NOTES = ['Ab','A','A#','Bb','B','B#','Cb','C','C#','Db','D','D#','Eb','E','Fb','E#','F','F#','Gb','G', 'G#']
MAJOR_THIRDS = dict()
MAJOR_THIRDS['A'] = 'C#'
MAJOR_THIRDS['B'] = 'D#'
MAJOR_THIRDS['C'] = 'E'
MAJOR_THIRDS['D'] = 'F#'
MAJOR_THIRDS['E'] = 'G#'
MAJOR_THIRDS['F'] = 'A'
MAJOR_THIRDS['G'] = 'B'

MINOR_THIRDS = dict()
MINOR_THIRDS['A'] = 'C'
MINOR_THIRDS['B'] = 'D'
MINOR_THIRDS['C'] = 'Eb'
MINOR_THIRDS['D'] = 'F'
MINOR_THIRDS['E'] = 'G'
MINOR_THIRDS['F'] = 'Ab'
MINOR_THIRDS['G'] = 'Bb'

LETTERS = ['A','B','C','D','E','F','G']

class Note():
    def __init__(self, note, octave, duration, volume):
        self.note = note
        self.letter = note[:1]
        self.octave = octave
        self.duration = duration
        self.volume = volume

    def getMinorThird(self):
        note = MINOR_THIRDS[self.letter]
        for character in self.note:
            if character == 'b':
                note = note + 'b'
            elif character == '#':
                if 'b' in note:
                    note = note[:-1]
                else:
                    note = note + '#'
        return note

    
    def getMajorThird(self):
        note = MAJOR_THIRDS[self.letter]
        for character in self.note:
            if character == '#':
                note = note + '#'
            elif character == 'b':
                if '#' in note:
                    note = note[:-1]
                else:
                    note = note + 'b'
        return note