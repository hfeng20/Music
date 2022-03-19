from Chord import *

class Key:
    def __init__(self, key):
        self.key = key
        if len(key > 2):
            self.root = key[:2]
            self.quality = key[2:]
        else:
            self.root = key[0]
            self.quallity = key[1]

