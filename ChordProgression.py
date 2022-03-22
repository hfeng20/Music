from Key import *

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class ProgressionGraph:
    def __init__(self, headNode):
        self.head = headNode

MAJOR_NUMERALS = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii']
#MAJOR
I = Node('I')
II = Node('ii')
III = Node('iii')
IV = Node('IV')
V = Node('V')
VI = Node('vi')
VII = Node('vii')
I.children = [II, III, IV, V, VI, VII]
II.children = [V, VII]
III.children = [II, IV, VI]
IV.children = [II, V, VII]
V.children = [I, VI, VII]
VI.children = [II, IV]
VII.children = [I, V, VI]
MAJOR_GRAPH = ProgressionGraph(I)

MINOR_NUMERALS = ['i', 'ii', 'III', 'iv', 'V', 'VI', 'vii']
#MINOR
i = Node('i')
ii = Node('ii')
iii = Node('III')
iv = Node('iv')
v = Node('V')
vi = Node('VI')
vii = Node('vii')
i.children = ['ii', 'III', 'iv', 'V', 'VI', 'vii']
ii.children = [v, vii]
iii.children = [ii, iv, vi]
iv.children = [ii, v, vii]
v.children = [i, vi, vii]
vi.children = [ii, iv]
vii.children = [i, v, vi]
MINOR_GRAPH = ProgressionGraph(i)



class ChordProgression:
    def __init__(self, key, progression):
        self.key = Key(key)
        self.progression = progression
        for i in range(1, len(progression)):
            if progression[i][:-3] not in progression[i - 1][:-3]:
                raise Exception("Invalid progression.")

try:
    progression = ['I', 'ii', 'V', 'I']
except Exception as E:
    print(E)




    
