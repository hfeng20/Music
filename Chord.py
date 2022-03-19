from Note import *

NOTES = ['Ab','A','A#','Bb','B','B#','Cb','C','C#','Db','D','D#','Eb','E','E#','Fb','F','F#','Gb','G','G#']

FIFTH_STRUCTURES = ['5','63','64']
SEVENTH_STRUCTURES = ['7','65','43', '42']

class Chord():

    def __init__(self, root, quality, structure, duration, volume):
        self.root = root
        self.quality = quality
        self.structure = structure
        self.duration = duration
        self.volume = volume
        if self.isSeventh:
            self.size = 4
        else:
            self.size = 3
        self.notes = []

    
    def isSeventh(self):
        if self.structure in SEVENTH_STRUCTURES:
            return True
        return False