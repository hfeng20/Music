from Chord import *
NOTES = ['Ab','A','A#','Bb','B','B#','Cb','C','C#','Db','D','D#','Eb','E','Fb','E#','F','F#','Gb','G', 'G#']

NOTES_DICT = dict()
NOTES_DICT[0] = ['A']
NOTES_DICT[1] = ['A#', 'Bb']
NOTES_DICT[2] = ['B', 'Cb']
NOTES_DICT[3] = ['C', 'B#']
NOTES_DICT[4] = ['C#','Db']
NOTES_DICT[5] = ['D']
NOTES_DICT[6] = ['D#','Eb']
NOTES_DICT[7] = ['E', 'Fb']
NOTES_DICT[8] = ['F', 'E#']
NOTES_DICT[9] = ['F#','Gb']
NOTES_DICT[10] = ['G']
NOTES_DICT[11] = ['G#','Ab']

LETTERS = ['A','B','C','D','E','F','G']

class Key:
    def __init__(self, key):
        self.scale = []
        self.key = key
        self.root = None
        self.quality = None
        if len(key) > 2:
            self.root = key[:2]
            self.quality = key[2:]
        else:
            self.root = key[0]
            self.quality = key[1]
        
        if self.root not in NOTES:
            raise Exception("Invalid key root.")
        if self.quality != 'M' and self.quality != 'm':
            raise Exception("Invalid key quality.")

        self.scale.append(self.root)
        index = 0
        for i in range(0, len(NOTES_DICT)):
            if self.root in NOTES_DICT[i]:
                index = i
        noteNumberArray = [index]

        if self.quality == 'M':
            for i in range(0,6):
                if i == 2:
                    noteNumberArray.append((noteNumberArray[len(noteNumberArray) - 1] + 1) % len(NOTES_DICT))
                else:
                    noteNumberArray.append((noteNumberArray[len(noteNumberArray) - 1] + 2) % len(NOTES_DICT))
        if self.quality == 'm':
            for i in range(0,6):
                if i == 1 or i == 4:
                    noteNumberArray.append((noteNumberArray[len(noteNumberArray) - 1] + 1) % len(NOTES_DICT))
                else:
                    noteNumberArray.append((noteNumberArray[len(noteNumberArray) - 1] + 2) % len(NOTES_DICT))
        for number in noteNumberArray[1:]:
            targetLetter = LETTERS[(LETTERS.index((self.scale[len(self.scale) - 1])[:1]) + 1) % len(LETTERS)]
            for possibleNote in NOTES_DICT[number]:
                if(possibleNote[:1] == targetLetter):
                    self.scale.append(possibleNote)
        conflict = False
        sharp = False
        flat = False
        for note in self.scale:
            if '#' in note:
                sharp = True
            if 'b' in note:
                flat = True
            if sharp and flat or len(self.scale) != 7:
                raise Exception("Invalid key.")


try:
    key = Key("C#m")
    print(key.scale)
except Exception as E:
    print(E)

