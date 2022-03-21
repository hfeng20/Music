from multiprocessing.pool import TERMINATE
from Note import *

NOTES = ['Ab','A','A#','Bb','B','B#','Cb','C','C#','Db','D','D#','Eb','E','E#','Fb','F','F#','Gb','G','G#']

STRUCTURES = ['5','6','64']
SEVENTH_STRUCTURES = ['7','65','43', '42']

CHORD_STACKS = dict()
CHORD_STACKS['M'] = ['M','m','M']
CHORD_STACKS['m'] = ['m','M','m']
CHORD_STACKS['+'] = ['M','M','M']
CHORD_STACKS['aug'] = ['M','M','M']
CHORD_STACKS['o'] = ['m','m','m']
CHORD_STACKS['ø'] = ['m','m','M']
CHORD_STACKS['dim'] = ['m','m','m']
CHORD_STACKS['half-dim'] = ['m','m','M']
CHORD_STACKS['dom'] = ['M','m','m']

class Chord():

    def __init__(self, root, quality, structure):
        try:
            if quality not in CHORD_STACKS.keys():
                raise Exception("Invalid chord quality.")
            if structure not in STRUCTURES and structure not in SEVENTH_STRUCTURES:
                raise Exception("Invalid chord inversion.")
        except Exception as E:
            raise
            return
        self.root = root
        self.quality = quality
        self.structure = structure
        if self.isSeventh:
            self.size = 4
        else:
            self.size = 3
        self.notes = [root]
        curNote = self.notes[len(self.notes) - 1]
        if self.isSeventh():
            for third in CHORD_STACKS[quality]:
                if(third == 'M'):
                    nextNote = curNote.getMajorThird()
                    if curNote.letter == 'G' or curNote.letter == 'F':
                        self.notes.append(Note(nextNote, curNote.octave + 1, curNote.duration, curNote.volume))
                    else:
                        self.notes.append(Note(nextNote, curNote.octave, curNote.duration, curNote.volume))
                else:
                    nextNote = curNote.getMinorThird()
                    if curNote.letter == 'G' or curNote.letter == 'F':
                        self.notes.append(Note(nextNote, curNote.octave + 1, curNote.duration, curNote.volume))
                    else:
                        self.notes.append(Note(nextNote, curNote.octave, curNote.duration, curNote.volume))
                curNote = self.notes[len(self.notes) - 1]
            inverted = False
            for i in range(SEVENTH_STRUCTURES.index(structure)):
                inverted = True
                self.notes[0].octave += 1
                self.notes.append(self.notes.pop(0))
            if inverted:
                for note in self.notes:
                    note.octave -= 1
        else:
            for third in (CHORD_STACKS[quality])[:2]:
                if third == "M":
                    nextNote = curNote.getMajorThird()
                    if curNote.letter == 'G' or curNote.letter == 'F':
                        self.notes.append(Note(nextNote, curNote.octave + 1, curNote.duration, curNote.volume))
                    else:
                        self.notes.append(Note(nextNote, curNote.octave, curNote.duration, curNote.volume))
                else:
                    nextNote = curNote.getMinorThird()
                    if curNote.letter == 'G' or curNote.letter == 'F':
                        self.notes.append(Note(nextNote, curNote.octave + 1, curNote.duration, curNote.volume))
                    else:
                        self.notes.append(Note(nextNote, curNote.octave, curNote.duration, curNote.volume))
                curNote = self.notes[len(self.notes) - 1]
            inverted = False
            for i in range(STRUCTURES.index(structure)):
                inverted = True
                self.notes[0].octave += 1
                self.notes.append(self.notes.pop(0))
            if inverted:
                for note in self.notes:
                    note.octave -= 1


    
    def isSeventh(self):
        if self.structure in SEVENTH_STRUCTURES:
            return True
        return False
# try:
#     root = Note('C#', 4, 1/4, 6)
#     chord = Chord(root, 'half-dim', '42')
#     for note in chord.notes:
#         print(note.note + " " + (str)(note.octave))
# except Exception as E:
#     print(E)